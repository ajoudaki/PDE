// Exact connected-recursion compiler for Campaign 2.
//
// The raw state is a connected bipartite tree.  Row vertices carry powers of
// the readout Gaussian a.  Column vertices carry raw exponent pairs
// (power of u^1, power of u^2).  Coefficients are exact signed polynomials in
// theta.  The two-input covariance Q(theta) is used both in the terminal
// bivariate Gaussian moments and in the first-layer gradient rewrite.

#include <algorithm>
#include <array>
#include <boost/multiprecision/cpp_int.hpp>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

using Integer = boost::multiprecision::checked_int1024_t;
using Poly = std::vector<Integer>;  // coefficient of theta^r

struct Tree {
  std::vector<unsigned char> a;
  std::vector<std::array<unsigned char, 2>> h;
  std::vector<std::pair<unsigned char, unsigned char>> edges;
};

static Integer odd_df(int k) {
  Integer ans = 1;
  for (int q = k; q >= 1; q -= 2) ans *= q;
  return ans;
}

static void trim(Poly &p) {
  while (p.size() > 1 && p.back() == 0) p.pop_back();
  if (p.empty()) p.push_back(0);
}

static bool is_zero(const Poly &p) {
  return p.empty() || (p.size() == 1 && p[0] == 0);
}

static void add_shift(Poly &out, const Poly &p, const Integer &scale,
                      int shift = 0) {
  if (scale == 0 || is_zero(p)) return;
  if (out.size() < p.size() + static_cast<size_t>(shift))
    out.resize(p.size() + static_cast<size_t>(shift), 0);
  for (size_t i = 0; i < p.size(); ++i) out[i + shift] += scale * p[i];
  trim(out);
}

static Poly multiply(const Poly &p, const Poly &q) {
  if (is_zero(p) || is_zero(q)) return Poly{0};
  Poly out(p.size() + q.size() - 1, 0);
  for (size_t i = 0; i < p.size(); ++i)
    for (size_t j = 0; j < q.size(); ++j) out[i + j] += p[i] * q[j];
  trim(out);
  return out;
}

static Poly bivariate_moment(int p, int q) {
  Poly ans(static_cast<size_t>(std::min(p, q) + 1), 0);
  for (int r = 0; r <= std::min(p, q); ++r) {
    if ((p - r) & 1 || (q - r) & 1) continue;
    Integer coefficient = 1;
    // choose(p,r) choose(q,r) r!
    for (int j = 1; j <= r; ++j) {
      coefficient *= (p - r + j);
      coefficient /= j;
      coefficient *= (q - r + j);
      coefficient /= j;
      coefficient *= j;
    }
    coefficient *= odd_df(p - r - 1) * odd_df(q - r - 1);
    ans[r] += coefficient;
  }
  trim(ans);
  return ans;
}

static std::string rooted_code(
    int vertex, int parent, const Tree &t,
    const std::vector<std::vector<int>> &neighbors) {
  const int rows = static_cast<int>(t.a.size());
  std::vector<std::string> children;
  for (int w : neighbors[vertex]) if (w != parent)
    children.push_back(rooted_code(w, vertex, t, neighbors));
  std::sort(children.begin(), children.end());
  std::string out;
  out.push_back('(');
  if (vertex < rows) {
    out.push_back('A');
    out.push_back(static_cast<char>(1 + t.a[vertex]));
  } else {
    const auto &z = t.h[vertex - rows];
    out.push_back('H');
    out.push_back(static_cast<char>(1 + z[0]));
    out.push_back(static_cast<char>(1 + z[1]));
  }
  for (const auto &child : children) out += child;
  out.push_back(')');
  return out;
}

static std::string canonical_key(const Tree &t) {
  const int rows = static_cast<int>(t.a.size());
  const int n = rows + static_cast<int>(t.h.size());
  std::vector<std::vector<int>> neighbors(n);
  for (auto [u, v] : t.edges) {
    neighbors[u].push_back(rows + v);
    neighbors[rows + v].push_back(u);
  }
  if (static_cast<int>(t.edges.size()) + 1 != n)
    throw std::logic_error("component is not a tree");
  std::vector<int> degree(n), leaves;
  for (int v = 0; v < n; ++v) {
    degree[v] = static_cast<int>(neighbors[v].size());
    if (degree[v] <= 1) leaves.push_back(v);
  }
  int remaining = n;
  while (remaining > 2) {
    remaining -= static_cast<int>(leaves.size());
    std::vector<int> next;
    for (int v : leaves) {
      degree[v] = 0;
      for (int w : neighbors[v]) if (degree[w] > 0) {
        --degree[w];
        if (degree[w] == 1) next.push_back(w);
      }
    }
    leaves.swap(next);
  }
  std::vector<int> centers;
  for (int v = 0; v < n; ++v)
    if (degree[v] > 0 || n == 1) centers.push_back(v);
  if (centers.empty()) centers = leaves;
  std::string best;
  for (int center : centers) {
    std::string candidate = rooted_code(center, -1, t, neighbors);
    if (best.empty() || candidate < best) best = std::move(candidate);
  }
  return best;
}

static std::vector<Tree> split_components(const Tree &t) {
  int rows = static_cast<int>(t.a.size());
  int cols = static_cast<int>(t.h.size());
  int n = rows + cols;
  std::vector<std::vector<int>> neighbors(n);
  for (auto [u, v] : t.edges) {
    neighbors[u].push_back(rows + v);
    neighbors[rows + v].push_back(u);
  }
  std::vector<unsigned char> seen(n, 0);
  std::vector<Tree> out;
  for (int seed = 0; seed < n; ++seed) if (!seen[seed]) {
    std::vector<int> vertices{seed};
    seen[seed] = 1;
    for (size_t q = 0; q < vertices.size(); ++q)
      for (int w : neighbors[vertices[q]]) if (!seen[w]) {
        seen[w] = 1;
        vertices.push_back(w);
      }
    std::vector<int> row_map(rows, -1), col_map(cols, -1);
    Tree child;
    for (int v : vertices) if (v < rows) {
      row_map[v] = static_cast<int>(child.a.size());
      child.a.push_back(t.a[v]);
    }
    for (int v : vertices) if (v >= rows) {
      col_map[v - rows] = static_cast<int>(child.h.size());
      child.h.push_back(t.h[v - rows]);
    }
    for (auto [u, v] : t.edges)
      if (row_map[u] >= 0 && col_map[v] >= 0)
        child.edges.push_back({static_cast<unsigned char>(row_map[u]),
                               static_cast<unsigned char>(col_map[v])});
    out.push_back(std::move(child));
  }
  return out;
}

static Integer choose(int n, int k) {
  if (k < 0 || k > n) return 0;
  k = std::min(k, n - k);
  Integer ans = 1;
  for (int q = 1; q <= k; ++q) ans = ans * (n - k + q) / q;
  return ans;
}

// A second, exact terminal contraction.  A surviving leading quotient of a
// connected 2P-edge raw tree has P+1 vertices and P occupied covariance
// cells; hence it is a tree and every occupied cell contains exactly two raw
// W edges.  We enumerate the corresponding bipartition-respecting vertex
// partitions directly.  This is the bivariate-column analogue of the checked
// parent compiler's VertexPartitionWickEvaluator.
struct VertexPartitionBivariate {
  const Tree &tree;
  int rows, cols, pairs, target;
  std::vector<std::vector<int>> incidence;

  explicit VertexPartitionBivariate(const Tree &t)
      : tree(t), rows(static_cast<int>(t.a.size())),
        cols(static_cast<int>(t.h.size())),
        pairs(static_cast<int>(t.edges.size() / 2)), target(pairs + 1),
        incidence(rows, std::vector<int>(cols, 0)) {
    for (auto [u, v] : t.edges) ++incidence[u][v];
  }

  struct ColumnType {
    int h0{}, h1{};
    std::vector<int> signature;
    int multiplicity{};
  };

  struct ColumnDP {
    const std::vector<ColumnType> &types;
    int row_blocks;
    std::unordered_map<std::string, Poly> memo;

    std::string key(const std::vector<int> &remaining, int blocks) const {
      std::string out;
      out.push_back(static_cast<char>(blocks));
      for (int z : remaining) out.push_back(static_cast<char>(z));
      return out;
    }

    Poly rec(const std::vector<int> &remaining, int blocks) {
      int count = std::accumulate(remaining.begin(), remaining.end(), 0);
      if (blocks == 0) return count == 0 ? Poly{1} : Poly{0};
      if (count < blocks) return Poly{0};
      std::string memo_key = key(remaining, blocks);
      auto found = memo.find(memo_key);
      if (found != memo.end()) return found->second;

      int distinguished = 0;
      while (distinguished < static_cast<int>(remaining.size()) &&
             remaining[distinguished] == 0) ++distinguished;
      std::vector<int> take(types.size(), 0), edge_sum(row_blocks, 0);
      take[distinguished] = 1;
      int h0_sum = types[distinguished].h0;
      int h1_sum = types[distinguished].h1;
      for (int q = 0; q < row_blocks; ++q)
        edge_sum[q] = types[distinguished].signature[q];
      for (int z : edge_sum) if (z > 2) return Poly{0};

      Poly total{0};
      auto enumerate = [&](auto &&self, int type_index,
                           int current_h0, int current_h1) -> void {
        if (type_index == static_cast<int>(types.size())) {
          for (int z : edge_sum) if (z == 1) return;
          std::vector<int> child = remaining;
          Integer choices = 1;
          for (int q = 0; q < static_cast<int>(types.size()); ++q) {
            int available = remaining[q] - (q == distinguished);
            int selected = take[q] - (q == distinguished);
            choices *= choose(available, selected);
            child[q] -= take[q];
          }
          Poly product = multiply(bivariate_moment(current_h0, current_h1),
                                  rec(child, blocks - 1));
          add_shift(total, product, choices);
          return;
        }
        int already = take[type_index];
        int available = remaining[type_index] - already;
        int maximum = available;
        for (int q = 0; q < row_blocks; ++q) {
          int degree = types[type_index].signature[q];
          if (degree)
            maximum = std::min(maximum, (2 - edge_sum[q]) / degree);
        }
        for (int extra = 0; extra <= maximum; ++extra) {
          take[type_index] += extra;
          for (int q = 0; q < row_blocks; ++q)
            edge_sum[q] += extra * types[type_index].signature[q];
          self(self, type_index + 1,
               current_h0 + extra * types[type_index].h0,
               current_h1 + extra * types[type_index].h1);
          for (int q = 0; q < row_blocks; ++q)
            edge_sum[q] -= extra * types[type_index].signature[q];
          take[type_index] -= extra;
        }
      };
      enumerate(enumerate, 0, h0_sum, h1_sum);
      memo.emplace(std::move(memo_key), total);
      return total;
    }
  };

  Poly evaluate_row_partition(
      int row_blocks, const std::vector<int> &a_sum,
      const std::vector<int> &degree_sum,
      const std::vector<std::vector<int>> &block_incidence) const {
    int column_blocks = target - row_blocks;
    if (column_blocks < 1 || column_blocks > cols) return Poly{0};
    Integer row_moment = 1;
    for (int q = 0; q < row_blocks; ++q) {
      if ((a_sum[q] & 1) || (degree_sum[q] & 1)) return Poly{0};
      row_moment *= odd_df(a_sum[q] - 1);
    }
    std::map<std::vector<int>, int> type_ids;
    std::vector<ColumnType> types;
    for (int v = 0; v < cols; ++v) {
      std::vector<int> signature(row_blocks, 0);
      for (int block = 0; block < row_blocks; ++block)
        signature[block] = block_incidence[block][v];
      std::vector<int> type_key{tree.h[v][0], tree.h[v][1]};
      type_key.insert(type_key.end(), signature.begin(), signature.end());
      auto [it, inserted] = type_ids.emplace(type_key, types.size());
      if (inserted)
        types.push_back({tree.h[v][0], tree.h[v][1], signature, 0});
      ++types[it->second].multiplicity;
    }
    std::vector<int> remaining;
    for (const auto &type : types) remaining.push_back(type.multiplicity);
    ColumnDP dp{types, row_blocks};
    Poly ans = dp.rec(remaining, column_blocks);
    for (auto &coefficient : ans) coefficient *= row_moment;
    return ans;
  }

  Poly run() const {
    if (tree.edges.size() & 1) return Poly{0};
    if (tree.edges.empty()) {
      if (rows == 1 && cols == 0)
        return (tree.a[0] & 1) ? Poly{0} : Poly{odd_df(tree.a[0] - 1)};
      if (rows == 0 && cols == 1)
        return bivariate_moment(tree.h[0][0], tree.h[0][1]);
      return Poly{0};
    }
    int total_a = std::accumulate(tree.a.begin(), tree.a.end(), 0);
    if (total_a & 1) return Poly{0};
    std::vector<int> assignment(rows, 0), a_sum(rows, 0),
        degree_sum(rows, 0), row_degree(rows, 0);
    std::vector<std::vector<int>> block_incidence(
        rows, std::vector<int>(cols, 0));
    for (auto [u, v] : tree.edges) ++row_degree[u];
    a_sum[0] = tree.a[0];
    degree_sum[0] = row_degree[0];
    block_incidence[0] = incidence[0];
    Poly total{0};
    std::unordered_map<std::string, Poly> partition_cache;

    auto enumerate = [&](auto &&self, int row, int blocks) -> void {
      int remaining_rows = rows - row;
      if (blocks > target - 1 || blocks + remaining_rows < target - cols)
        return;
      int bad = 0;
      for (int q = 0; q < blocks; ++q)
        bad += ((a_sum[q] | degree_sum[q]) & 1) != 0;
      if (bad > remaining_rows) return;
      if (row == rows) {
        std::vector<std::string> codes(blocks);
        for (int block = 0; block < blocks; ++block) {
          codes[block].push_back(static_cast<char>(a_sum[block]));
          for (int v = 0; v < cols; ++v)
            codes[block].push_back(static_cast<char>(block_incidence[block][v]));
        }
        std::sort(codes.begin(), codes.end());
        std::string cache_key;
        cache_key.push_back(static_cast<char>(blocks));
        for (const auto &code : codes) cache_key += code;
        auto found = partition_cache.find(cache_key);
        Poly value;
        if (found != partition_cache.end()) {
          value = found->second;
        } else {
          value = evaluate_row_partition(blocks, a_sum, degree_sum,
                                         block_incidence);
          partition_cache.emplace(std::move(cache_key), value);
        }
        add_shift(total, value, 1);
        return;
      }
      int last = blocks < target - 1 ? blocks : blocks - 1;
      for (int block = 0; block <= last; ++block) {
        bool overfull = false;
        for (int v = 0; v < cols; ++v)
          if (block_incidence[block][v] + incidence[row][v] > 2) {
            overfull = true; break;
          }
        if (overfull) continue;
        assignment[row] = block;
        a_sum[block] += tree.a[row];
        degree_sum[block] += row_degree[row];
        for (int v = 0; v < cols; ++v)
          block_incidence[block][v] += incidence[row][v];
        self(self, row + 1, blocks + (block == blocks));
        for (int v = 0; v < cols; ++v)
          block_incidence[block][v] -= incidence[row][v];
        degree_sum[block] -= row_degree[row];
        a_sum[block] -= tree.a[row];
      }
    };
    enumerate(enumerate, 1, 1);
    return total;
  }
};

// Exact quotient-Wick recursion.  Unlike the one-color parent evaluator, the
// leaf is a polynomial because each surviving column class has a bivariate
// Gaussian moment.
struct WickEvaluator {
  int pairs{};
  std::unordered_map<std::string, Poly> memo;

  static void merge_rows(int x, int y, std::vector<unsigned char> &a,
                         std::vector<std::vector<unsigned char>> &m,
                         std::vector<std::vector<unsigned char>> &sealed) {
    if (x == y) return;
    if (x > y) std::swap(x, y);
    a[x] += a[y];
    for (size_t v = 0; v < m[x].size(); ++v) {
      m[x][v] += m[y][v];
      sealed[x][v] += sealed[y][v];
    }
    a.erase(a.begin() + y);
    m.erase(m.begin() + y);
    sealed.erase(sealed.begin() + y);
  }

  static void merge_cols(
      int x, int y, std::vector<std::array<unsigned char, 2>> &h,
      std::vector<std::vector<unsigned char>> &m,
      std::vector<std::vector<unsigned char>> &sealed) {
    if (x == y) return;
    if (x > y) std::swap(x, y);
    h[x][0] += h[y][0];
    h[x][1] += h[y][1];
    h.erase(h.begin() + y);
    for (size_t u = 0; u < m.size(); ++u) {
      m[u][x] += m[u][y];
      m[u].erase(m[u].begin() + y);
      sealed[u][x] += sealed[u][y];
      sealed[u].erase(sealed[u].begin() + y);
    }
  }

  static bool is_forest(const std::vector<std::vector<unsigned char>> &s) {
    int rows = static_cast<int>(s.size());
    int cols = rows ? static_cast<int>(s[0].size()) : 0;
    std::vector<int> parent(rows + cols), rank(rows + cols, 0);
    std::iota(parent.begin(), parent.end(), 0);
    auto root = [&](int x) {
      int y = x;
      while (parent[y] != y) y = parent[y];
      while (parent[x] != x) { int z = parent[x]; parent[x] = y; x = z; }
      return y;
    };
    for (int u = 0; u < rows; ++u) for (int v = 0; v < cols; ++v) {
      if (s[u][v] > 1) return false;
      if (!s[u][v]) continue;
      int x = root(u), y = root(rows + v);
      if (x == y) return false;
      if (rank[x] < rank[y]) std::swap(x, y);
      parent[y] = x;
      if (rank[x] == rank[y]) ++rank[x];
    }
    return true;
  }

  std::string key_of(
      const std::vector<unsigned char> &a,
      const std::vector<std::array<unsigned char, 2>> &h,
      const std::vector<std::vector<unsigned char>> &m,
      const std::vector<std::vector<unsigned char>> &sealed) const {
    std::string key;
    key.push_back(static_cast<char>(pairs));
    key.push_back(static_cast<char>(a.size()));
    key.push_back(static_cast<char>(h.size()));
    for (auto z : a) key.push_back(static_cast<char>(z));
    for (auto z : h) { key.push_back(static_cast<char>(z[0])); key.push_back(static_cast<char>(z[1])); }
    for (const auto &row : m) for (auto z : row) key.push_back(static_cast<char>(z));
    for (const auto &row : sealed) for (auto z : row) key.push_back(static_cast<char>(z));
    return key;
  }

  Poly leaf(const std::vector<unsigned char> &a,
            const std::vector<std::array<unsigned char, 2>> &h) const {
    if (static_cast<int>(a.size() + h.size()) != pairs + 1) return Poly{0};
    Poly ans{1};
    for (auto z : a) {
      if (z & 1) return Poly{0};
      for (auto &x : ans) x *= odd_df(static_cast<int>(z) - 1);
    }
    for (auto z : h) ans = multiply(ans, bivariate_moment(z[0], z[1]));
    return ans;
  }

  Poly rec(std::vector<unsigned char> a,
           std::vector<std::array<unsigned char, 2>> h,
           std::vector<std::vector<unsigned char>> m,
           std::vector<std::vector<unsigned char>> sealed,
           int remaining) {
    int remaining_pairs = remaining / 2;
    int vertices = static_cast<int>(a.size() + h.size());
    if (pairs + 1 > vertices || pairs + 1 < vertices - 2 * remaining_pairs)
      return Poly{0};
    for (size_t u = 0; u < m.size(); ++u)
      for (size_t v = 0; v < m[u].size(); ++v)
        if (m[u][v] + 2 * sealed[u][v] > 2) return Poly{0};

    int forced = 0;
    for (size_t u = 0; u < m.size(); ++u)
      for (size_t v = 0; v < m[u].size(); ++v) if (m[u][v] == 2) {
        m[u][v] = 0;
        ++sealed[u][v];
        ++forced;
      }
    if (forced) {
      if (!is_forest(sealed)) return Poly{0};
      return rec(std::move(a), std::move(h), std::move(m), std::move(sealed),
                 remaining - 2 * forced);
    }
    if (!remaining) return leaf(a, h);

    std::string key = key_of(a, h, m, sealed);
    auto found = memo.find(key);
    if (found != memo.end()) return found->second;

    int u0 = -1, v0 = -1;
    for (size_t u = 0; u < m.size() && u0 < 0; ++u)
      for (size_t v = 0; v < m[u].size(); ++v) if (m[u][v]) {
        u0 = static_cast<int>(u); v0 = static_cast<int>(v); break;
      }
    auto after = m;
    --after[u0][v0];
    Poly total{0};
    for (size_t u1 = 0; u1 < after.size(); ++u1)
      for (size_t v1 = 0; v1 < after[u1].size(); ++v1) {
        unsigned multiplicity = after[u1][v1];
        if (!multiplicity) continue;
        auto ca = a;
        auto ch = h;
        auto cm = after;
        auto cs = sealed;
        --cm[u1][v1];
        merge_rows(u0, static_cast<int>(u1), ca, cm, cs);
        merge_cols(v0, static_cast<int>(v1), ch, cm, cs);
        int nu = std::min(u0, static_cast<int>(u1));
        int nv = std::min(v0, static_cast<int>(v1));
        ++cs[nu][nv];
        if (!is_forest(cs)) continue;
        add_shift(total, rec(std::move(ca), std::move(ch), std::move(cm),
                             std::move(cs), remaining - 2), multiplicity);
      }
    memo.emplace(std::move(key), total);
    return total;
  }

  Poly run(const Tree &t) {
    if (t.edges.size() & 1) return Poly{0};
    pairs = static_cast<int>(t.edges.size() / 2);
    std::vector<std::vector<unsigned char>> m(
        t.a.size(), std::vector<unsigned char>(t.h.size(), 0));
    for (auto [u, v] : t.edges) ++m[u][v];
    std::vector<std::vector<unsigned char>> sealed(
        t.a.size(), std::vector<unsigned char>(t.h.size(), 0));
    return rec(t.a, t.h, std::move(m), std::move(sealed), t.edges.size());
  }
};

struct Recursion {
  int sigma;
  std::unordered_map<std::string, Poly> value_memo;
  std::unordered_map<std::string, Poly> wick_memo;
  size_t base_evaluations = 0;

  explicit Recursion(int sign) : sigma(sign) {}

  std::string key(const Tree &t, int k) const {
    std::string out;
    out.push_back(static_cast<char>(k));
    out += canonical_key(t);
    return out;
  }

  Poly base(const Tree &t) {
    std::string k = canonical_key(t);
    auto found = wick_memo.find(k);
    if (found != wick_memo.end()) return found->second;
    Poly ans = VertexPartitionBivariate(t).run();
    wick_memo.emplace(std::move(k), ans);
    ++base_evaluations;
    return ans;
  }

  Poly value(const Tree &t, int k) {
    if (t.edges.size() & 1) return Poly{0};
    int parity = static_cast<int>(t.edges.size()) +
                 std::accumulate(t.a.begin(), t.a.end(), 0);
    if ((parity + k) & 1) return Poly{0};
    std::string memo_key = key(t, k);
    auto found = value_memo.find(memo_key);
    if (found != value_memo.end()) return found->second;
    if (k == 0) {
      Poly ans = base(t);
      value_memo.emplace(std::move(memo_key), ans);
      return ans;
    }
    Poly ans{0};
    std::array<Integer, 2> sign{Integer(1), Integer(sigma)};

    // Dtilde a rewrite.
    for (size_t u = 0; u < t.a.size(); ++u) if (t.a[u])
      for (int alpha = 0; alpha < 2; ++alpha) {
        Tree child = t;
        unsigned multiplicity = child.a[u];
        --child.a[u];
        std::array<unsigned char, 2> exponent{0, 0};
        exponent[alpha] = 2;
        unsigned char v0 = static_cast<unsigned char>(child.h.size());
        child.h.push_back(exponent);
        child.h.push_back(exponent);
        child.edges.push_back({static_cast<unsigned char>(u), v0});
        child.edges.push_back({static_cast<unsigned char>(u),
                               static_cast<unsigned char>(v0 + 1)});
        add_shift(ans, value(child, k - 1), Integer(multiplicity) * sign[alpha]);
      }

    // Dtilde u rewrite, including Q_beta,alpha.
    for (size_t v = 0; v < t.h.size(); ++v)
      for (int beta = 0; beta < 2; ++beta) if (t.h[v][beta])
        for (int alpha = 0; alpha < 2; ++alpha) {
          Tree child = t;
          unsigned multiplicity = 4 * child.h[v][beta];
          --child.h[v][beta];
          ++child.h[v][alpha];
          unsigned char u0 = static_cast<unsigned char>(child.a.size());
          unsigned char v1 = static_cast<unsigned char>(child.h.size());
          child.a.push_back(1);
          std::array<unsigned char, 2> exponent{0, 0};
          exponent[alpha] = 2;
          child.h.push_back(exponent);
          child.edges.push_back({u0, static_cast<unsigned char>(v)});
          child.edges.push_back({u0, v1});
          add_shift(ans, value(child, k - 1),
                    Integer(multiplicity) * sign[alpha], alpha != beta);
        }

    // Dtilde W rewrite.  The removed bridge splits the raw tree.
    for (size_t edge = 0; edge < t.edges.size(); ++edge)
      for (int alpha = 0; alpha < 2; ++alpha) {
        Tree forest = t;
        auto [u, v] = forest.edges[edge];
        ++forest.a[u];
        forest.h[v][alpha] += 2;
        unsigned char fresh = static_cast<unsigned char>(forest.h.size());
        std::array<unsigned char, 2> exponent{0, 0};
        exponent[alpha] = 2;
        forest.h.push_back(exponent);
        forest.edges.erase(forest.edges.begin() + edge);
        forest.edges.push_back({u, fresh});
        auto children = split_components(forest);
        if (children.size() != 2)
          throw std::logic_error("W hit did not split the tree");
        Poly convolution{0};
        for (int q = 0; q <= k - 1; ++q) {
          Poly product = multiply(value(children[0], q),
                                  value(children[1], k - 1 - q));
          add_shift(convolution, product, choose(k - 1, q));
        }
        add_shift(ans, convolution, Integer(2) * sign[alpha]);
      }

    trim(ans);
    value_memo.emplace(std::move(memo_key), ans);
    return ans;
  }
};

static Tree root_for_alpha(int alpha) {
  Tree root;
  root.a = {1};
  std::array<unsigned char, 2> exponent{0, 0};
  exponent[alpha] = 2;
  root.h = {exponent, exponent};
  root.edges = {{0, 0}, {0, 1}};
  return root;
}

static std::string poly_json(const Poly &p) {
  std::ostringstream out;
  out << '[';
  for (size_t i = 0; i < p.size(); ++i) {
    if (i) out << ',';
    out << '"' << p[i] << '"';
  }
  out << ']';
  return out.str();
}

int main(int argc, char **argv) {
  try {
    if (argc != 3)
      throw std::invalid_argument("usage: two_input_connected SIGN ORDER");
    std::string channel = argv[1];
    int sigma = channel == "plus" ? 1 : channel == "minus" ? -1 : 0;
    if (!sigma) throw std::invalid_argument("SIGN must be plus or minus");
    int max_order = std::stoi(argv[2]);
    if (max_order < 0 || max_order > 7)
      throw std::invalid_argument("ORDER must be between zero and seven");

    Recursion recursion(sigma);
    std::cout << "{\"channel\":\"" << channel << "\",\"raw_theta\":[";
    for (int k = 0; k <= max_order; ++k) {
      auto start = std::chrono::steady_clock::now();
      Poly result{0};
      add_shift(result, recursion.value(root_for_alpha(0), k), 1);
      add_shift(result, recursion.value(root_for_alpha(1), k), Integer(sigma));
      auto stop = std::chrono::steady_clock::now();
      if (k) std::cout << ',';
      std::cout << poly_json(result);
      std::cerr << channel << " order=" << k
                << " seconds="
                << std::chrono::duration<double>(stop - start).count()
                << " value_cache=" << recursion.value_memo.size()
                << " wick_cache=" << recursion.wick_memo.size() << '\n';
    }
    std::cout << "],\"normalization\":\"divide order k by 2^(k+1)\","
              << "\"value_cache\":" << recursion.value_memo.size()
              << ",\"wick_cache\":" << recursion.wick_memo.size()
              << ",\"base_evaluations\":" << recursion.base_evaluations
              << "}" << std::endl;
    return 0;
  } catch (const std::exception &error) {
    std::cerr << "error: " << error.what() << '\n';
    return 2;
  }
}

#include <algorithm>
#include <boost/multiprecision/cpp_int.hpp>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

// The recursion has non-negative integer coefficients.  Fixed-width checked
// arithmetic is both substantially cheaper than heap-allocated cpp_int and
// exact: any intermediate reaching 2^512 throws instead of silently wrapping.
// Hence a completed run is a machine-checkable proof that every intermediate
// represented below was evaluated over the ordinary non-negative integers.
// A separate degree/L1 audit gives, after k derivatives, total Gaussian degree
// d_k=7+5k, coefficient L1 norm C_{k+1} <= 8 d_k C_k, and Gaussian moment at
// most (d_k-1)!!.  Therefore every positive subtotal through k=13 is bounded
// by U_k=[product_{j<k} 8(7+5j)](d_k-1)!!; U_13 has only 275 bits.
using cpp_int = boost::multiprecision::checked_uint512_t;

// A connected scalarized peeling term.  Row vertices carry powers of the
// readout Gaussian a_i, column vertices carry half-powers of u_j (so h=3
// means u_j^6), and every edge is one W_ij factor.
struct Tree {
  std::vector<unsigned char> a;
  std::vector<unsigned char> h;
  std::vector<std::pair<unsigned char, unsigned char>> edges;
};

static cpp_int odd_double_factorial(int k) {
  cpp_int z = 1;
  for (int q = k; q >= 1; q -= 2) z *= q;
  return z;
}

static std::string rooted_code(
    int v, int parent, const Tree &t,
    const std::vector<std::vector<int>> &neighbors) {
  const int na = static_cast<int>(t.a.size());
  std::vector<std::string> children;
  for (int w : neighbors[v])
    if (w != parent) children.push_back(rooted_code(w, v, t, neighbors));
  std::sort(children.begin(), children.end());
  std::string code;
  code.push_back('(');
  code.push_back(v < na ? 'A' : 'H');
  code.push_back(static_cast<char>(1 + (v < na ? t.a[v] : t.h[v - na])));
  for (const auto &child : children) code += child;
  code.push_back(')');
  return code;
}

static std::string canonical_key(const Tree &t) {
  const int na = static_cast<int>(t.a.size());
  const int n = na + static_cast<int>(t.h.size());
  std::vector<std::vector<int>> neighbors(n);
  for (auto [u, v0] : t.edges) {
    int v = na + v0;
    neighbors[u].push_back(v);
    neighbors[v].push_back(u);
  }
  if (static_cast<int>(t.edges.size()) + 1 != n) {
    std::cerr << "component is not a tree\n";
    std::abort();
  }
  std::vector<int> degree(n), leaves;
  for (int v = 0; v < n; ++v) {
    degree[v] = static_cast<int>(neighbors[v].size());
    if (degree[v] <= 1) leaves.push_back(v);
  }
  int remaining = n;
  while (remaining > 2) {
    std::vector<int> next;
    remaining -= static_cast<int>(leaves.size());
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
    std::string code = rooted_code(center, -1, t, neighbors);
    if (best.empty() || code < best) best = std::move(code);
  }
  return best;
}

// Exact Wick pairing after quotienting indistinguishable unpaired W factors.
// A pairing merges both row indices and both column indices.  Only leaves with
// P+1 free classes survive for a connected component normalized by n^-(P+1).
struct WickEvaluator {
  int P{};
  std::unordered_map<std::string, cpp_int> local_memo;
  std::unordered_map<std::string, cpp_int> *memo{&local_memo};

  static void merge_rows(int x, int y, std::vector<unsigned char> &a,
                         std::vector<std::vector<unsigned char>> &m) {
    if (x == y) return;
    if (x > y) std::swap(x, y);
    a[x] += a[y];
    for (size_t j = 0; j < m[x].size(); ++j) m[x][j] += m[y][j];
    a.erase(a.begin() + y);
    m.erase(m.begin() + y);
  }

  static void merge_cols(int x, int y, std::vector<unsigned char> &h,
                         std::vector<std::vector<unsigned char>> &m) {
    if (x == y) return;
    if (x > y) std::swap(x, y);
    h[x] += h[y];
    for (auto &row : m) {
      row[x] += row[y];
      row.erase(row.begin() + y);
    }
    h.erase(h.begin() + y);
  }

  std::string key_of(
      const std::vector<unsigned char> &a,
      const std::vector<unsigned char> &h,
      const std::vector<std::vector<unsigned char>> &m,
      const std::vector<std::vector<unsigned char>> &paired) const {
    std::string key;
    key.push_back(static_cast<char>(P));
    key.push_back(static_cast<char>(a.size()));
    key.push_back(static_cast<char>(h.size()));
    for (auto z : a) key.push_back(static_cast<char>(z));
    for (auto z : h) key.push_back(static_cast<char>(z));
    for (const auto &row : m)
      for (auto z : row) key.push_back(static_cast<char>(z));
    for (const auto &row : paired)
      for (auto z : row) key.push_back(static_cast<char>(z));
    return key;
  }

  // The already-created covariance edges must be a forest.  If they ever
  // contain a cycle (including a parallel two-cycle), later vertex
  // identifications can only lower the number of free classes, so that branch
  // can never recover the leading relation V=P+1.
  static bool is_forest(
      const std::vector<std::vector<unsigned char>> &paired) {
    const int rows = static_cast<int>(paired.size());
    const int cols = rows ? static_cast<int>(paired[0].size()) : 0;
    std::vector<int> parent(rows + cols), rank(rows + cols, 0);
    std::iota(parent.begin(), parent.end(), 0);
    auto root = [&](int x) {
      int y = x;
      while (parent[y] != y) y = parent[y];
      while (parent[x] != x) {
        int next = parent[x];
        parent[x] = y;
        x = next;
      }
      return y;
    };
    for (int i = 0; i < rows; ++i) {
      for (int j = 0; j < cols; ++j) {
        if (paired[i][j] > 1) return false;
        if (!paired[i][j]) continue;
        int x = root(i), y = root(rows + j);
        if (x == y) return false;
        if (rank[x] < rank[y]) std::swap(x, y);
        parent[y] = x;
        if (rank[x] == rank[y]) ++rank[x];
      }
    }
    return true;
  }

  cpp_int leaf(const std::vector<unsigned char> &a,
               const std::vector<unsigned char> &h) const {
    if (static_cast<int>(a.size() + h.size()) != P + 1) return 0;
    cpp_int ans = 1;
    for (auto z : a) {
      if (z & 1) return 0;
      ans *= odd_double_factorial(static_cast<int>(z) - 1);
    }
    for (auto z : h)
      ans *= odd_double_factorial(2 * static_cast<int>(z) - 1);
    return ans;
  }

  cpp_int rec(const std::vector<unsigned char> &a,
              const std::vector<unsigned char> &h,
              const std::vector<std::vector<unsigned char>> &m,
              const std::vector<std::vector<unsigned char>> &paired,
              int remaining_edges) {
    if (!remaining_edges) return leaf(a, h);
    const int remaining_pairs = remaining_edges / 2;
    const int vertices = static_cast<int>(a.size() + h.size());
    if (P + 1 > vertices || P + 1 < vertices - 2 * remaining_pairs) return 0;
    std::string key = key_of(a, h, m, paired);
    auto found = memo->find(key);
    if (found != memo->end()) return found->second;

    int u0 = -1, v0 = -1;
    for (size_t u = 0; u < m.size() && u0 < 0; ++u)
      for (size_t v = 0; v < m[u].size(); ++v)
        if (m[u][v]) { u0 = static_cast<int>(u); v0 = static_cast<int>(v); break; }

    auto after_first = m;
    --after_first[u0][v0];
    cpp_int ans = 0;
    for (size_t u1 = 0; u1 < after_first.size(); ++u1) {
      for (size_t v1 = 0; v1 < after_first[u1].size(); ++v1) {
        unsigned multiplicity = after_first[u1][v1];
        if (!multiplicity) continue;
        auto child_a = a;
        auto child_h = h;
        auto child_m = after_first;
        auto child_paired = paired;
        --child_m[u1][v1];
        merge_rows(u0, static_cast<int>(u1), child_a, child_m);
        // Apply precisely the same quotient operation to prior covariance
        // edges.  Its exponent vector is irrelevant, hence the dummy one.
        {
          std::vector<unsigned char> dummy(child_paired.size(), 0);
          merge_rows(u0, static_cast<int>(u1), dummy, child_paired);
        }
        merge_cols(v0, static_cast<int>(v1), child_h, child_m);
        {
          std::vector<unsigned char> dummy(
              child_paired.empty() ? 0 : child_paired[0].size(), 0);
          merge_cols(v0, static_cast<int>(v1), dummy, child_paired);
        }
        int new_u = std::min(u0, static_cast<int>(u1));
        int new_v = std::min(v0, static_cast<int>(v1));
        ++child_paired[new_u][new_v];
        if (!is_forest(child_paired)) continue;
        ans += multiplicity * rec(child_a, child_h, child_m, child_paired,
                                  remaining_edges - 2);
      }
    }
    memo->emplace(std::move(key), ans);
    return ans;
  }

  cpp_int run(const Tree &t,
              std::unordered_map<std::string, cpp_int> *shared = nullptr) {
    if (shared) memo = shared;
    P = static_cast<int>(t.edges.size() / 2);
    std::vector<std::vector<unsigned char>> m(
        t.a.size(), std::vector<unsigned char>(t.h.size(), 0));
    for (auto [u, v] : t.edges) ++m[u][v];
    std::vector<std::vector<unsigned char>> paired(
        t.a.size(), std::vector<unsigned char>(t.h.size(), 0));
    return rec(t.a, t.h, m, paired, static_cast<int>(t.edges.size()));
  }
};

static std::vector<Tree> split_components(const Tree &t) {
  const int na = static_cast<int>(t.a.size());
  const int nh = static_cast<int>(t.h.size());
  const int n = na + nh;
  std::vector<std::vector<int>> neighbors(n);
  for (auto [u, v0] : t.edges) {
    int v = na + v0;
    neighbors[u].push_back(v);
    neighbors[v].push_back(u);
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
    std::vector<int> row_map(na, -1), col_map(nh, -1);
    Tree c;
    for (int v : vertices) if (v < na) {
      row_map[v] = static_cast<int>(c.a.size());
      c.a.push_back(t.a[v]);
    }
    for (int v : vertices) if (v >= na) {
      col_map[v - na] = static_cast<int>(c.h.size());
      c.h.push_back(t.h[v - na]);
    }
    for (auto [u, v] : t.edges)
      if (row_map[u] >= 0 && col_map[v] >= 0)
        c.edges.push_back({static_cast<unsigned char>(row_map[u]),
                           static_cast<unsigned char>(col_map[v])});
    out.push_back(std::move(c));
  }
  return out;
}

static cpp_int choose(int n, int k) {
  if (k < 0 || k > n) return 0;
  k = std::min(k, n - k);
  cpp_int z = 1;
  for (int q = 1; q <= k; ++q) z = z * (n - k + q) / q;
  return z;
}

struct PeelingRecursion {
  std::unordered_map<std::string, cpp_int> value_memo;
  std::unordered_map<std::string, cpp_int> wick_memo;
  std::map<int, size_t> calls_by_order;
  std::map<int, size_t> misses_by_order;
  std::map<int, cpp_int> root_by_a_hit, root_by_h_hit, root_by_w_hit;
  size_t completed_base_evaluations = 0;

  std::string value_key(const Tree &t, int k) const {
    std::string key;
    key.push_back(static_cast<char>(k));
    key += canonical_key(t);
    return key;
  }

  cpp_int base(const Tree &t) {
    std::string key = canonical_key(t);
    auto found = wick_memo.find(key);
    if (found != wick_memo.end()) return found->second;
    WickEvaluator evaluator;
    // Deliberately keep the quotient-Wick memo local to this one base tree.
    // Sharing it across distinct base trees saves recomputation at low order,
    // but its memory grows without bound at orders 11 and 13.  A fresh memo
    // changes only running time: every returned integer is the same exact
    // Wick contraction.  Destroying it here gives the direct evaluator a
    // sharply smaller memory footprint.
    cpp_int ans = evaluator.run(t);
    wick_memo.emplace(std::move(key), ans);
    ++completed_base_evaluations;
    if (completed_base_evaluations % 10000 == 0)
      std::cerr << "completed base contractions="
                << completed_base_evaluations
                << " value_cache=" << value_memo.size() << '\n';
    return ans;
  }

  cpp_int value(const Tree &t, int k, bool is_root = false) {
    ++calls_by_order[k];
    // Every rewrite changes the number of W factors by zero or two.  Thus its
    // parity is invariant.  Odd total W degree has zero centered-Gaussian
    // expectation.  After a W split, the child parities sum to the parent
    // parity, so at least one factor remains zero.
    if (t.edges.size() & 1) return 0;
    // Under global parameter negation, a component has parity
    // (-1)^(sum a-exponents + number of W factors); every application of D
    // flips that parity because f is odd and grad(f) is even.  Centered
    // Gaussian expectation kills the odd sector exactly.
    int degree_parity = static_cast<int>(t.edges.size()) +
                        std::accumulate(t.a.begin(), t.a.end(), 0);
    if ((degree_parity + k) & 1) return 0;
    std::string key = value_key(t, k);
    auto found = value_memo.find(key);
    if (found != value_memo.end()) return found->second;
    ++misses_by_order[k];
    if (k == 0) {
      cpp_int ans = base(t);
      value_memo.emplace(std::move(key), ans);
      return ans;
    }

    cpp_int ans = 0;
    cpp_int subtotal_a = 0, subtotal_h = 0, subtotal_w = 0;

    // d(a_u^p)/ds: p a_u^(p-1) z_u^2.
    for (size_t u = 0; u < t.a.size(); ++u) if (t.a[u]) {
      Tree child = t;
      unsigned multiplicity = child.a[u];
      --child.a[u];
      unsigned char v0 = static_cast<unsigned char>(child.h.size());
      child.h.push_back(1);
      child.h.push_back(1);
      child.edges.push_back({static_cast<unsigned char>(u), v0});
      child.edges.push_back({static_cast<unsigned char>(u),
                             static_cast<unsigned char>(v0 + 1)});
      subtotal_a += multiplicity * value(child, k - 1);
    }

    // d(u_v^(2p))/ds: 8p times a fresh row wedge attached at v.
    for (size_t v = 0; v < t.h.size(); ++v) if (t.h[v]) {
      Tree child = t;
      unsigned multiplicity = 8 * child.h[v];
      unsigned char u0 = static_cast<unsigned char>(child.a.size());
      unsigned char v1 = static_cast<unsigned char>(child.h.size());
      child.a.push_back(1);
      child.h.push_back(1);
      child.edges.push_back({u0, static_cast<unsigned char>(v)});
      child.edges.push_back({u0, v1});
      subtotal_h += multiplicity * value(child, k - 1);
    }

    // dW_uv/ds: 2 a_u u_v^2 times a fresh z_u edge.  Removing the
    // differentiated tree edge splits the component into exactly two trees.
    for (size_t e = 0; e < t.edges.size(); ++e) {
      Tree forest = t;
      auto [u, v] = forest.edges[e];
      ++forest.a[u];
      ++forest.h[v];
      unsigned char fresh = static_cast<unsigned char>(forest.h.size());
      forest.h.push_back(1);
      forest.edges.erase(forest.edges.begin() + e);
      forest.edges.push_back({u, fresh});
      auto children = split_components(forest);
      if (children.size() != 2) std::abort();
      cpp_int convolution = 0;
      for (int q = 0; q <= k - 1; ++q)
        convolution += choose(k - 1, q) * value(children[0], q) *
                       value(children[1], k - 1 - q);
      subtotal_w += 2 * convolution;
    }
    ans = subtotal_a + subtotal_h + subtotal_w;
    if (is_root) {
      root_by_a_hit[k] = subtotal_a;
      root_by_h_hit[k] = subtotal_h;
      root_by_w_hit[k] = subtotal_w;
    }
    value_memo.emplace(std::move(key), ans);
    return ans;
  }
};

int main(int argc, char **argv) {
  int max_order = argc > 1 ? std::stoi(argv[1]) : 13;
  Tree root;
  root.a = {1};
  root.h = {1, 1};
  root.edges = {{0, 0}, {0, 1}};

  PeelingRecursion recursion;
  for (int k = 0; k <= max_order; ++k) {
    auto start = std::chrono::steady_clock::now();
    cpp_int z = recursion.value(root, k, true);
    auto stop = std::chrono::steady_clock::now();
    std::cout << "D^" << k << " f = " << z << "\n";
    if (k > 0) {
      std::cout << "  root hits: a=" << recursion.root_by_a_hit[k]
                << " h=" << recursion.root_by_h_hit[k]
                << " W=" << recursion.root_by_w_hit[k] << "\n";
    }
    std::cout << "  seconds="
              << std::chrono::duration<double>(stop - start).count()
              << " value_cache=" << recursion.value_memo.size()
              << " wick_cache=" << recursion.wick_memo.size()
              << "\n";
  }
  std::cout << "memo misses by remaining order:";
  for (auto [k, count] : recursion.misses_by_order)
    std::cout << " [" << k << ':' << count << ']';
  std::cout << "\n";
  return 0;
}

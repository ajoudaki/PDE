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
static bool first_wick_only = false;

// A connected scalarized peeling term.  Row vertices carry powers of the
// readout Gaussian a_i, column vertices carry half-powers of u_j (so h=3
// means u_j^6), and every edge is one W_ij factor.
struct Tree {
  std::vector<unsigned char> a;
  std::vector<unsigned char> h;
  std::vector<std::pair<unsigned char, unsigned char>> edges;
};

struct RollbackDSU {
  std::vector<int> parent, size;
  std::vector<std::tuple<int, int, int>> history;
  int classes;

  explicit RollbackDSU(int n) : parent(n), size(n, 1), classes(n) {
    std::iota(parent.begin(), parent.end(), 0);
  }
  int root(int x) const {
    while (parent[x] != x) x = parent[x];
    return x;
  }
  int snapshot() const { return static_cast<int>(history.size()); }
  void unite(int x, int y) {
    x = root(x); y = root(y);
    if (x == y) {
      history.emplace_back(-1, -1, -1);
      return;
    }
    if (size[x] < size[y]) std::swap(x, y);
    history.emplace_back(y, x, size[x]);
    parent[y] = x;
    size[x] += size[y];
    --classes;
  }
  void rollback(int snap) {
    while (static_cast<int>(history.size()) > snap) {
      auto [child, root_vertex, old_size] = history.back();
      history.pop_back();
      if (child >= 0) {
        parent[child] = child;
        size[root_vertex] = old_size;
        ++classes;
      }
    }
  }
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

// Labelled-edge Wick recursion.  This is mathematically independent of the
// multiplicity recursion below and is substantially faster on some highly
// symmetric 20--28-edge trees.  The memo cap affects time only.
struct LabelledWickEvaluator {
  const Tree &t;
  int rows, vertices, target;
  RollbackDSU dsu;
  std::unordered_map<std::string, cpp_int> memo;
  static constexpr size_t memo_entry_cap = 200000;

  explicit LabelledWickEvaluator(const Tree &tree)
      : t(tree), rows(static_cast<int>(tree.a.size())),
        vertices(rows + static_cast<int>(tree.h.size())),
        target(static_cast<int>(tree.edges.size() / 2 + 1)), dsu(vertices) {}

  std::pair<int, int> edge(int e) const {
    return {t.edges[e].first, rows + t.edges[e].second};
  }

  cpp_int leaf() {
    if (dsu.classes != target) return 0;
    std::vector<int> ae(vertices, 0), he(vertices, 0);
    for (int u = 0; u < rows; ++u) ae[dsu.root(u)] += t.a[u];
    for (int v = rows; v < vertices; ++v)
      he[dsu.root(v)] += t.h[v - rows];
    cpp_int ans = 1;
    for (int v = 0; v < vertices; ++v) if (dsu.root(v) == v) {
      if (ae[v] & 1) return 0;
      ans *= odd_double_factorial(ae[v] - 1);
      ans *= odd_double_factorial(2 * he[v] - 1);
    }
    return ans;
  }

  std::string key_of(uint32_t mask) const {
    std::string key(4 + vertices, '\0');
    key[0] = static_cast<char>(mask);
    key[1] = static_cast<char>(mask >> 8);
    key[2] = static_cast<char>(mask >> 16);
    key[3] = static_cast<char>(mask >> 24);
    int next = 0;
    std::vector<int> label(vertices, -1);
    for (int v = 0; v < vertices; ++v) {
      int r = dsu.root(v);
      if (label[r] < 0) label[r] = next++;
      key[4 + v] = static_cast<char>(label[r]);
    }
    return key;
  }

  cpp_int rec(uint32_t mask) {
    if (!mask) return leaf();
    int pairs_left = __builtin_popcount(mask) / 2;
    if (dsu.classes < target || dsu.classes - 2 * pairs_left > target)
      return 0;

    int cell_count[32][32]{};
    int remaining_count[32][32]{};
    int first_remaining[32][32];
    std::fill(&first_remaining[0][0], &first_remaining[0][0] + 32 * 32, -1);
    for (int e = 0; e < static_cast<int>(t.edges.size()); ++e) {
      auto [u, v] = edge(e);
      u = dsu.root(u); v = dsu.root(v);
      if (++cell_count[u][v] > 2) return 0;
      if (mask & (uint32_t(1) << e)) {
        ++remaining_count[u][v];
        first_remaining[u][v] = e;
      }
    }

    // A cell is either one still-unpaired raw edge or one sealed pair.
    // Seal all double-unpaired cells in a single commuting batch.
    uint32_t forced_mask = 0;
    for (int u = 0; u < vertices; ++u)
      for (int v = 0; v < vertices; ++v) {
        int all = cell_count[u][v], rem = remaining_count[u][v];
        if (rem != 0 && rem != all) return 0;
        if (all == 2 && rem == 2) {
          uint32_t bits = mask;
          while (bits) {
            int e = __builtin_ctz(bits);
            bits &= bits - 1;
            auto [x, y] = edge(e);
            if (dsu.root(x) == u && dsu.root(y) == v)
              forced_mask |= uint32_t(1) << e;
          }
        }
      }
    if (forced_mask) return rec(mask & ~forced_mask);

    bool active[32]{};
    for (uint32_t bits = mask; bits; bits &= bits - 1) {
      int e = __builtin_ctz(bits);
      auto [u, v] = edge(e);
      active[dsu.root(u)] = true;
      active[dsu.root(v)] = true;
    }
    int a_parity[32]{};
    for (int u = 0; u < rows; ++u)
      a_parity[dsu.root(u)] ^= (t.a[u] & 1);
    int odd_classes = 0, active_rows = 0, active_cols = 0;
    for (int v = 0; v < vertices; ++v)
      if (dsu.root(v) == v && a_parity[v]) {
        ++odd_classes;
        if (!active[v]) return 0;
      }
    for (int v = 0; v < vertices; ++v) if (dsu.root(v) == v && active[v]) {
      if (v < rows) ++active_rows;
      else ++active_cols;
    }
    int identifications_needed = dsu.classes - target;
    if (odd_classes / 2 > pairs_left ||
        odd_classes / 2 > identifications_needed) return 0;
    int current_rows = 0, current_cols = 0;
    for (int v = 0; v < vertices; ++v) if (dsu.root(v) == v) {
      if (v < rows) ++current_rows;
      else ++current_cols;
    }
    int minimum_final_vertices =
        (current_rows - active_rows) + (active_rows != 0) +
        (current_cols - active_cols) + (active_cols != 0);
    if (target < minimum_final_vertices) return 0;
    int max_row_unions = std::min(pairs_left, std::max(0, active_rows - 1));
    int max_col_unions = std::min(pairs_left, std::max(0, active_cols - 1));
    if (identifications_needed > max_row_unions + max_col_unions) return 0;

    std::string key = key_of(mask);
    auto found = memo.find(key);
    if (found != memo.end()) return found->second;

    int e0 = __builtin_ctz(mask);
    uint32_t partners = mask & ~(uint32_t(1) << e0);
    cpp_int total = 0;
    auto [u0, v0] = edge(e0);
    while (partners) {
      int e1 = __builtin_ctz(partners);
      partners &= partners - 1;
      auto [u1, v1] = edge(e1);
      int snap = dsu.snapshot();
      dsu.unite(u0, u1);
      dsu.unite(v0, v1);
      total += rec(mask & ~(uint32_t(1) << e0) & ~(uint32_t(1) << e1));
      dsu.rollback(snap);
    }
    if (memo.size() < memo_entry_cap) memo.emplace(std::move(key), total);
    return total;
  }

  cpp_int run() {
    int E = static_cast<int>(t.edges.size());
    if (E & 1 || E >= 32) return 0;
    int asum = std::accumulate(t.a.begin(), t.a.end(), 0);
    if (asum & 1) return 0;
    return rec((uint32_t(1) << E) - 1);
  }
};

// Vertex-partition evaluator.  A leading quotient of a connected 2P-edge
// raw tree has P+1 vertices and P covariance cells.  Hence it is a tree and
// every occupied cell contains exactly two raw edges.  Conversely, every
// bipartition-respecting vertex partition with P+1 blocks and cell
// multiplicities 0 or 2 defines exactly one Wick pairing.  This evaluator
// sums those vertex partitions directly.  It is especially effective when
// many columns have the same incidence signature after a row partition.
struct VertexPartitionWickEvaluator {
  const Tree &t;
  int rows, cols, P, target;
  std::vector<std::vector<int>> incidence;
  std::vector<int> first_scalar, second_scalar;

  explicit VertexPartitionWickEvaluator(const Tree &tree, int orientation = 0)
      : t(tree), P(static_cast<int>(tree.edges.size() / 2)), target(P + 1) {
    // The partition characterization is symmetric in the two vertex
    // classes.  Enumerate restricted-growth partitions on the smaller side;
    // scalar multiplicities are a[u] on the original row side and 2*h[v]
    // on the original column side.
    bool transpose = orientation == 0 ? tree.h.size() < tree.a.size()
                                      : orientation > 0;
    rows = transpose ? static_cast<int>(tree.h.size())
                     : static_cast<int>(tree.a.size());
    cols = transpose ? static_cast<int>(tree.a.size())
                     : static_cast<int>(tree.h.size());
    incidence.assign(rows, std::vector<int>(cols, 0));
    first_scalar.resize(rows);
    second_scalar.resize(cols);
    if (!transpose) {
      for (int u = 0; u < rows; ++u) first_scalar[u] = tree.a[u];
      for (int v = 0; v < cols; ++v) second_scalar[v] = 2 * tree.h[v];
      for (auto [u, v] : t.edges) ++incidence[u][v];
    } else {
      for (int v = 0; v < rows; ++v) first_scalar[v] = 2 * tree.h[v];
      for (int u = 0; u < cols; ++u) second_scalar[u] = tree.a[u];
      for (auto [u, v] : t.edges) ++incidence[v][u];
    }
    // Restricted-growth strings enumerate the same set partitions in any
    // vertex order.  Put highly incident vertices first so irreversible
    // cell-occupancy violations are exposed as early as possible.
    std::vector<int> order(rows);
    std::iota(order.begin(), order.end(), 0);
    std::stable_sort(order.begin(), order.end(), [&](int x, int y) {
      int dx = std::accumulate(incidence[x].begin(), incidence[x].end(), 0);
      int dy = std::accumulate(incidence[y].begin(), incidence[y].end(), 0);
      if (dx != dy) return dx > dy;
      return first_scalar[x] > first_scalar[y];
    });
    auto old_incidence = incidence;
    auto old_scalar = first_scalar;
    for (int u = 0; u < rows; ++u) {
      incidence[u] = old_incidence[order[u]];
      first_scalar[u] = old_scalar[order[u]];
    }
  }

  static cpp_int choose_small(int n, int k) {
    if (k < 0 || k > n) return 0;
    k = std::min(k, n - k);
    cpp_int ans = 1;
    for (int q = 1; q <= k; ++q) ans = ans * (n - k + q) / q;
    return ans;
  }

  struct ColumnType {
    int scalar{};
    std::vector<int> signature;
    int multiplicity{};
  };

  struct ColumnDP {
    const std::vector<ColumnType> &types;
    int row_blocks;
    std::unordered_map<std::string, cpp_int> memo;
    static constexpr size_t memo_entry_cap = 200000;

    std::string key(const std::vector<int> &remaining, int blocks) const {
      std::string out;
      out.push_back(static_cast<char>(blocks));
      for (int z : remaining) out.push_back(static_cast<char>(z));
      return out;
    }

    cpp_int rec(const std::vector<int> &remaining, int blocks) {
      int count = std::accumulate(remaining.begin(), remaining.end(), 0);
      if (blocks == 0) return count == 0 ? cpp_int(1) : cpp_int(0);
      if (count < blocks) return 0;
      std::string memo_key = key(remaining, blocks);
      auto found = memo.find(memo_key);
      if (found != memo.end()) return found->second;

      int distinguished = 0;
      while (distinguished < static_cast<int>(remaining.size()) &&
             remaining[distinguished] == 0) ++distinguished;
      std::vector<int> take(types.size(), 0), edge_sum(row_blocks, 0);
      take[distinguished] = 1;
      int scalar_sum = types[distinguished].scalar;
      for (int q = 0; q < row_blocks; ++q)
        edge_sum[q] = types[distinguished].signature[q];
      for (int z : edge_sum) if (z > 2) {
        if (memo.size() < memo_entry_cap) memo.emplace(std::move(memo_key), 0);
        return 0;
      }

      cpp_int total = 0;
      auto enumerate = [&](auto &&self, int type_index,
                           int current_scalar) -> void {
        if (type_index == static_cast<int>(types.size())) {
          for (int z : edge_sum) if (z == 1) return;
          if (current_scalar & 1) return;
          std::vector<int> child = remaining;
          cpp_int choices = 1;
          for (int q = 0; q < static_cast<int>(types.size()); ++q) {
            int available = remaining[q] - (q == distinguished);
            int selected = take[q] - (q == distinguished);
            choices *= VertexPartitionWickEvaluator::choose_small(
                available, selected);
            child[q] -= take[q];
          }
          cpp_int block_moment = odd_double_factorial(current_scalar - 1);
          total += choices * block_moment * rec(child, blocks - 1);
          return;
        }

        int already = take[type_index];
        int available = remaining[type_index] - already;
        int maximum = available;
        for (int q = 0; q < row_blocks; ++q) {
          int degree = types[type_index].signature[q];
          if (degree) maximum = std::min(maximum, (2 - edge_sum[q]) / degree);
        }
        for (int add = 0; add <= maximum; ++add) {
          take[type_index] += add;
          for (int q = 0; q < row_blocks; ++q)
            edge_sum[q] += add * types[type_index].signature[q];
          self(self, type_index + 1,
               current_scalar + add * types[type_index].scalar);
          for (int q = 0; q < row_blocks; ++q)
            edge_sum[q] -= add * types[type_index].signature[q];
          take[type_index] -= add;
        }
      };
      enumerate(enumerate, 0, scalar_sum);
      if (memo.size() < memo_entry_cap)
        memo.emplace(std::move(memo_key), total);
      return total;
    }
  };

  cpp_int evaluate_row_partition(const std::vector<int> &assignment,
                                 int row_blocks,
                                 const std::vector<int> &a_sum,
                                 const std::vector<int> &degree_sum,
                                 const std::vector<std::vector<int>>
                                     &block_incidence) const {
    int column_blocks = target - row_blocks;
    if (column_blocks < 1 || column_blocks > cols) return 0;
    cpp_int row_moment = 1;
    for (int q = 0; q < row_blocks; ++q) {
      if ((a_sum[q] & 1) || (degree_sum[q] & 1)) return 0;
      row_moment *= odd_double_factorial(a_sum[q] - 1);
    }

    std::map<std::vector<int>, int> type_ids;
    std::vector<ColumnType> types;
    for (int v = 0; v < cols; ++v) {
      std::vector<int> signature(row_blocks, 0);
      for (int block = 0; block < row_blocks; ++block)
        signature[block] = block_incidence[block][v];
      std::vector<int> type_key;
      type_key.push_back(second_scalar[v]);
      type_key.insert(type_key.end(), signature.begin(), signature.end());
      auto [it, inserted] = type_ids.emplace(type_key, types.size());
      if (inserted) types.push_back({second_scalar[v], signature, 0});
      ++types[it->second].multiplicity;
    }
    std::vector<int> remaining;
    for (const auto &type : types) remaining.push_back(type.multiplicity);
    ColumnDP dp{types, row_blocks};
    return row_moment * dp.rec(remaining, column_blocks);
  }

  cpp_int run() const {
    if (t.edges.size() & 1) return 0;
    if (t.edges.empty()) {
      if (rows == 1 && cols == 0)
        return (t.a[0] & 1) ? cpp_int(0)
                            : odd_double_factorial(t.a[0] - 1);
      if (rows == 0 && cols == 1)
        return odd_double_factorial(2 * t.h[0] - 1);
      return 0;
    }
    int total_a = std::accumulate(t.a.begin(), t.a.end(), 0);
    if (total_a & 1) return 0;
    std::vector<int> assignment(rows, 0), a_sum(rows, 0), degree_sum(rows, 0);
    std::vector<std::vector<int>> block_incidence(
        rows, std::vector<int>(cols, 0));
    std::vector<int> row_degree(rows, 0);
    for (auto [u, v] : t.edges) ++row_degree[u];
    a_sum[0] = first_scalar[0];
    degree_sum[0] = row_degree[0];
    block_incidence[0] = incidence[0];
    cpp_int total = 0;
    std::unordered_map<std::string, cpp_int> row_partition_cache;
    auto enumerate = [&](auto &&self, int row, int blocks) -> void {
      int remaining_rows = rows - row;
      if (blocks > target - 1 || blocks + remaining_rows < target - cols)
        return;
      int parity_bad_blocks = 0;
      for (int q = 0; q < blocks; ++q)
        parity_bad_blocks += ((a_sum[q] | degree_sum[q]) & 1) != 0;
      if (parity_bad_blocks > remaining_rows) return;
      if (row == rows) {
        std::vector<std::string> block_codes(blocks);
        for (int block = 0; block < blocks; ++block) {
          auto &code = block_codes[block];
          code.push_back(static_cast<char>(a_sum[block]));
          for (int v = 0; v < cols; ++v)
            code.push_back(static_cast<char>(block_incidence[block][v]));
        }
        std::sort(block_codes.begin(), block_codes.end());
        std::string partition_key;
        partition_key.push_back(static_cast<char>(blocks));
        for (const auto &code : block_codes) partition_key += code;
        auto found = row_partition_cache.find(partition_key);
        if (found != row_partition_cache.end()) {
          total += found->second;
        } else {
          cpp_int value = evaluate_row_partition(
              assignment, blocks, a_sum, degree_sum, block_incidence);
          if (row_partition_cache.size() < 200000)
            row_partition_cache.emplace(std::move(partition_key), value);
          total += value;
        }
        return;
      }
      // Existing blocks are 0,...,blocks-1.  The value `blocks` opens one
      // new restricted-growth block when the target still allows it.
      int last_block = blocks < target - 1 ? blocks : blocks - 1;
      for (int block = 0; block <= last_block; ++block) {
        bool overfull = false;
        for (int v = 0; v < cols; ++v)
          if (block_incidence[block][v] + incidence[row][v] > 2) {
            overfull = true;
            break;
          }
        if (overfull) continue;
        assignment[row] = block;
        a_sum[block] += first_scalar[row];
        degree_sum[block] += row_degree[row];
        for (int v = 0; v < cols; ++v)
          block_incidence[block][v] += incidence[row][v];
        self(self, row + 1, blocks + (block == blocks));
        for (int v = 0; v < cols; ++v)
          block_incidence[block][v] -= incidence[row][v];
        a_sum[block] -= first_scalar[row];
        degree_sum[block] -= row_degree[row];
      }
    };
    if (rows == 0) return 0;
    enumerate(enumerate, 1, 1);
    return total;
  }
};

// Exact Wick pairing after quotienting indistinguishable unpaired W factors.
// A pairing merges both row indices and both column indices.  Only leaves with
// P+1 free classes survive for a connected component normalized by n^-(P+1).
struct WickEvaluator {
  int P{};
  std::unordered_map<std::string, cpp_int> local_memo;
  std::unordered_map<std::string, cpp_int> *memo{&local_memo};
  static constexpr size_t memo_entry_cap = 200000;

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
    const int remaining_pairs = remaining_edges / 2;
    const int vertices = static_cast<int>(a.size() + h.size());
    if (P + 1 > vertices || P + 1 < vertices - 2 * remaining_pairs) return 0;

    // In a surviving connected leading quotient, every covariance cell
    // contains exactly the two raw W factors consumed by one Wick pair.
    // Vertex identifications only merge cells, so occupancy above two is
    // irreversible and kills the branch.
    for (size_t u = 0; u < m.size(); ++u)
      for (size_t v = 0; v < m[u].size(); ++v)
        if (m[u][v] + 2 * paired[u][v] > 2) return 0;

    // Seal every forced double cell in one commuting batch.  Each contains
    // exactly the two occurrences of its unique Wick pair, so its
    // multiplicity is one and it performs no vertex identification.
    int forced_cells = 0;
    for (size_t u = 0; u < m.size(); ++u)
      for (size_t v = 0; v < m[u].size(); ++v)
        if (m[u][v] == 2) ++forced_cells;
    if (forced_cells) {
      auto forced_m = m;
      auto forced_paired = paired;
      for (size_t u = 0; u < forced_m.size(); ++u)
        for (size_t v = 0; v < forced_m[u].size(); ++v)
          if (forced_m[u][v] == 2) {
            forced_m[u][v] = 0;
            ++forced_paired[u][v];
          }
      if (!is_forest(forced_paired)) return 0;
      return rec(a, h, forced_m, forced_paired,
                 remaining_edges - 2 * forced_cells);
    }

    const int rows_now = static_cast<int>(a.size());
    const int cols_now = static_cast<int>(h.size());
    // An inactive odd readout class can no longer be merged and therefore
    // can never acquire a nonzero centered-Gaussian moment.
    int active_rows = 0, active_cols = 0, odd_rows = 0;
    for (int u = 0; u < rows_now; ++u) {
      bool active = false;
      for (int v = 0; v < cols_now; ++v) active |= m[u][v] != 0;
      active_rows += active;
      odd_rows += a[u] & 1;
      if ((a[u] & 1) && !active) return 0;
    }
    for (int v = 0; v < cols_now; ++v) {
      bool active = false;
      for (int u = 0; u < rows_now; ++u) active |= m[u][v] != 0;
      active_cols += active;
    }

    // Each pair can perform at most one row union; making o odd row classes
    // even needs at least o/2 such unions.  It also needs that many of the
    // total V-(P+1) still-required vertex identifications.
    int identifications_needed = vertices - (P + 1);
    if (odd_rows / 2 > remaining_pairs || odd_rows / 2 > identifications_needed)
      return 0;

    // Inactive classes can never merge.  On each side, all active classes can
    // contribute no fewer than one final class, giving a sharp cheap lower
    // bound on the achievable final vertex count.
    int minimum_final_vertices =
        (rows_now - active_rows) + (active_rows != 0) +
        (cols_now - active_cols) + (active_cols != 0);
    if (P + 1 < minimum_final_vertices) return 0;
    int max_row_unions = std::min(remaining_pairs, std::max(0, active_rows - 1));
    int max_col_unions = std::min(remaining_pairs, std::max(0, active_cols - 1));
    if (identifications_needed > max_row_unions + max_col_unions) return 0;

    // Completed covariance cells are a forest.  If it has more than one
    // component, every component must be incident to a remaining W factor;
    // otherwise no future contraction can attach the untouched component.
    if (remaining_edges) {
      std::vector<int> parent(rows_now + cols_now), rank(rows_now + cols_now, 0);
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
      auto unite = [&](int x, int y) {
        x = root(x); y = root(y);
        if (x == y) return;
        if (rank[x] < rank[y]) std::swap(x, y);
        parent[y] = x;
        if (rank[x] == rank[y]) ++rank[x];
      };
      for (int u = 0; u < rows_now; ++u)
        for (int v = 0; v < cols_now; ++v)
          if (paired[u][v]) unite(u, rows_now + v);
      std::vector<unsigned char> touched(rows_now + cols_now, 0);
      for (int u = 0; u < rows_now; ++u)
        for (int v = 0; v < cols_now; ++v) if (m[u][v]) {
          touched[root(u)] = 1;
          touched[root(rows_now + v)] = 1;
        }
      int components = 0;
      for (int v = 0; v < rows_now + cols_now; ++v)
        if (root(v) == v) ++components;
      if (components > 1)
        for (int v = 0; v < rows_now + cols_now; ++v)
          if (root(v) == v && !touched[v]) return 0;
    }

    if (!remaining_edges) return leaf(a, h);
    std::string key = key_of(a, h, m, paired);
    auto found = memo->find(key);
    if (found != memo->end()) return found->second;

    int u0 = -1, v0 = -1;
    for (size_t u = 0; u < m.size() && u0 < 0; ++u)
      for (size_t v = 0; v < m[u].size(); ++v)
        if (m[u][v]) {
          u0 = static_cast<int>(u);
          v0 = static_cast<int>(v);
          break;
        }

    auto after_first = m;
    --after_first[u0][v0];
    cpp_int ans = 0;
    for (int pass = 0; pass < (first_wick_only ? 2 : 1); ++pass) {
    for (size_t u1 = 0; u1 < after_first.size(); ++u1) {
      for (size_t v1 = 0; v1 < after_first[u1].size(); ++v1) {
        unsigned multiplicity = after_first[u1][v1];
        if (!multiplicity) continue;
        if (first_wick_only) {
          bool adjacent = ((u0 == static_cast<int>(u1)) !=
                           (v0 == static_cast<int>(v1)));
          if ((pass == 0) != adjacent) continue;
        }
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
        cpp_int child_value = rec(child_a, child_h, child_m, child_paired,
                                  remaining_edges - 2);
        ans += multiplicity * child_value;
        if (first_wick_only && child_value) {
          memo->emplace(std::move(key), ans);
          return ans;
        }
      }
    }
    }
    // Refusing new transposition entries can only repeat exact work.
    if (memo->size() < memo_entry_cap) memo->emplace(std::move(key), ans);
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
  std::unordered_map<std::string, cpp_int> wick_subproblem_memo;
  std::map<int, size_t> calls_by_order;
  std::map<int, size_t> misses_by_order;
  std::map<std::pair<int, int>, cpp_int> root_by_a_hit, root_by_h_hit,
      root_by_w_hit;
  size_t completed_base_evaluations = 0;

  std::string value_key(const Tree &t, int k, int w) const {
    std::string key;
    key.push_back(static_cast<char>(k));
    key.push_back(static_cast<char>(w));
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
    cpp_int ans = t.edges.size() >= 16
        ? LabelledWickEvaluator(t).run()
        : evaluator.run(t, &wick_subproblem_memo);
    wick_memo.emplace(std::move(key), ans);
    ++completed_base_evaluations;
    if (completed_base_evaluations % 10000 == 0)
      std::cerr << "completed base contractions="
                << completed_base_evaluations
                << " value_cache=" << value_memo.size() << '\n';
    return ans;
  }

  cpp_int value(const Tree &t, int k, int w, bool is_root = false) {
    ++calls_by_order[k];
    if (w < 0 || w > k) return 0;
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
    std::string key = value_key(t, k, w);
    auto found = value_memo.find(key);
    if (found != value_memo.end()) return found->second;
    ++misses_by_order[k];
    if (k == 0) {
      cpp_int ans = w == 0 ? base(t) : 0;
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
      subtotal_a += multiplicity * value(child, k - 1, w);
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
      subtotal_h += multiplicity * value(child, k - 1, w);
    }

    // dW_uv/ds: 2 a_u u_v^2 times a fresh z_u edge.  Removing the
    // differentiated tree edge splits the component into exactly two trees.
    for (size_t e = 0; w > 0 && e < t.edges.size(); ++e) {
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
        for (int s = 0; s <= w - 1; ++s)
          convolution += choose(k - 1, q) * value(children[0], q, s) *
                         value(children[1], k - 1 - q, w - 1 - s);
      subtotal_w += 2 * convolution;
    }
    ans = subtotal_a + subtotal_h + subtotal_w;
    if (is_root) {
      root_by_a_hit[{k, w}] = subtotal_a;
      root_by_h_hit[{k, w}] = subtotal_h;
      root_by_w_hit[{k, w}] = subtotal_w;
    }
    value_memo.emplace(std::move(key), ans);
    return ans;
  }
};

int main(int argc, char **argv) {
  int max_order = argc > 1 ? std::stoi(argv[1]) : 13;
  int max_w_hits = argc > 2 ? std::stoi(argv[2]) : max_order;
  Tree root;
  root.a = {1};
  root.h = {1, 1};
  root.edges = {{0, 0}, {0, 1}};

  PeelingRecursion recursion;
  for (int k = max_order; k <= max_order; ++k) {
    for (int w = 0; w <= std::min(k, max_w_hits); ++w) {
    auto start = std::chrono::steady_clock::now();
    cpp_int z = recursion.value(root, k, w, true);
    auto stop = std::chrono::steady_clock::now();
    std::cout << "D^" << k << " P=" << (k + 1 - w)
              << " (W_hits=" << w << ") = " << z << "\n";
    if (k > 0) {
      std::cout << "  root hits: a=" << recursion.root_by_a_hit[{k, w}]
                << " h=" << recursion.root_by_h_hit[{k, w}]
                << " W=" << recursion.root_by_w_hit[{k, w}] << "\n";
    }
    std::cout << "  seconds="
              << std::chrono::duration<double>(stop - start).count()
              << " value_cache=" << recursion.value_memo.size()
              << " wick_cache=" << recursion.wick_memo.size()
              << " wick_subproblems=" << recursion.wick_subproblem_memo.size()
              << "\n";
    }
  }
  std::cout << "memo misses by remaining order:";
  for (auto [k, count] : recursion.misses_by_order)
    std::cout << " [" << k << ':' << count << ']';
  std::cout << "\n";
  return 0;
}

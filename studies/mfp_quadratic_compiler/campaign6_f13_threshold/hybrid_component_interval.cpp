#include <algorithm>
#ifdef CHECKED_ARITHMETIC
#include <boost/multiprecision/cpp_int.hpp>
#endif
#include <chrono>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <sys/resource.h>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

// The default native type is intended only for fast pilot runs.  A decisive
// certificate must be compiled with -DCHECKED_ARITHMETIC: the independent
// degree/L1 bound is 275 bits through order 13, so checked_uint512_t is exact
// and throws on any unexpected overflow.
#ifdef CHECKED_ARITHMETIC
using cpp_int = boost::multiprecision::checked_uint512_t;
#else
using cpp_int = unsigned __int128;
#endif
static int base_edge_cap = 1000;
// Optional rigorous sub-sum: retain only the first nonzero Wick branch at
// every recursive pairing node.  Multiplicities on the retained branch are
// kept.  Since all summands are nonnegative this is an exact lower bound and
// makes large terminal components cheap enough to explore.
static bool first_wick_only = false;
static bool adjacent_wick_only = false;
// -1 means no restriction; otherwise at most this many Wick pairs may fail
// to share exactly one endpoint at the instant they are contracted.
static int nonadjacent_wick_budget = -1;
// Optional history truncation: discard a positive branch as soon as its
// current connected component exceeds this many raw edges.  This is stricter
// than the terminal base cap and is useful for fast, independently auditable
// lower bounds.
static int path_edge_cap = 1000;
// If nonnegative, use complete Wick enumeration through this raw edge count
// and the fast one-adjacent-branch certificate above it.
static int hybrid_full_cap = -1;
static bool hybrid_all_adjacent = false;
static int hybrid_nonadjacent_budget = -1;
// Optional exact split of the first derivative rewrite.  This affects only
// the root call and permits three independent checked certificate runs:
// 0=all, 1=readout hit, 2=activation hit, 3=weight hit.
static int root_rewrite_mode = 0;
static bool wick_upper_bound = false;
static bool disable_wick_subproblem_memo = false;
// Campaign 6 interval mode.  Components with at most this many raw W edges
// are evaluated by the exact leading-width Wick recursion; larger components
// use the rigorous unrestricted-pairing cap.  Setting -1 disables the mode.
// Because the forest expectation factors over components, this yields a
// certified upper bound which monotonically decreases to the exact answer as
// the cap grows.
static int exact_then_upper_cap = -1;

static std::ostream &operator<<(std::ostream &out, cpp_int x) {
  if (!x) return out << '0';
  std::string digits;
  while (x) {
    digits.push_back(static_cast<char>('0' + x % 10));
    x /= 10;
  }
  std::reverse(digits.begin(), digits.end());
  return out << digits;
}

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
      const std::vector<std::vector<unsigned char>> &paired,
      int nonadjacent_budget) const {
    const int rows_count = static_cast<int>(a.size());
    const int cols_count = static_cast<int>(h.size());
    const int n = rows_count + cols_count;
    std::vector<int> color(n);
    {
      std::map<std::pair<int, int>, int> ids;
      for (int u = 0; u < rows_count; ++u)
        ids.try_emplace({0, a[u]}, static_cast<int>(ids.size()));
      for (int v = 0; v < cols_count; ++v)
        ids.try_emplace({1, h[v]}, static_cast<int>(ids.size()));
      // Reassign in lexicographic map order, independent of insertion order.
      int next = 0;
      for (auto &[label, id] : ids) id = next++;
      for (int u = 0; u < rows_count; ++u) color[u] = ids[{0, a[u]}];
      for (int v = 0; v < cols_count; ++v)
        color[rows_count + v] = ids[{1, h[v]}];
    }
    while (true) {
      std::vector<std::vector<int>> signatures(n);
      for (int u = 0; u < rows_count; ++u) {
        auto &s = signatures[u];
        s.push_back(color[u]);
        std::vector<std::tuple<int, int, int>> neighbors;
        for (int v = 0; v < cols_count; ++v)
          if (m[u][v] || paired[u][v])
            neighbors.push_back({color[rows_count + v], m[u][v], paired[u][v]});
        std::sort(neighbors.begin(), neighbors.end());
        for (auto [c, x, y] : neighbors) {
          s.push_back(c); s.push_back(x); s.push_back(y);
        }
        s.push_back(-1);
      }
      for (int v = 0; v < cols_count; ++v) {
        auto &s = signatures[rows_count + v];
        s.push_back(color[rows_count + v]);
        std::vector<std::tuple<int, int, int>> neighbors;
        for (int u = 0; u < rows_count; ++u)
          if (m[u][v] || paired[u][v])
            neighbors.push_back({color[u], m[u][v], paired[u][v]});
        std::sort(neighbors.begin(), neighbors.end());
        for (auto [c, x, y] : neighbors) {
          s.push_back(c); s.push_back(x); s.push_back(y);
        }
        s.push_back(-1);
      }
      std::map<std::vector<int>, int> ids;
      for (const auto &s : signatures)
        ids.try_emplace(s, static_cast<int>(ids.size()));
      int next = 0;
      for (auto &[signature, id] : ids) id = next++;
      std::vector<int> refined(n);
      for (int v = 0; v < n; ++v) refined[v] = ids[signatures[v]];
      if (refined == color) break;
      color.swap(refined);
    }

    std::vector<int> rows(rows_count), cols(cols_count);
    std::iota(rows.begin(), rows.end(), 0);
    std::iota(cols.begin(), cols.end(), 0);
    std::stable_sort(rows.begin(), rows.end(),
                     [&](int x, int y) { return color[x] < color[y]; });
    std::stable_sort(cols.begin(), cols.end(), [&](int x, int y) {
      return color[rows_count + x] < color[rows_count + y];
    });

    std::string key;
    key.push_back(static_cast<char>(P));
    key.push_back(static_cast<char>(nonadjacent_budget + 2));
    key.push_back(static_cast<char>(rows_count));
    key.push_back(static_cast<char>(cols_count));
    for (int u : rows) key.push_back(static_cast<char>(a[u]));
    for (int v : cols) key.push_back(static_cast<char>(h[v]));
    for (int u : rows) for (int v : cols)
      key.push_back(static_cast<char>(m[u][v]));
    for (int u : rows) for (int v : cols)
      key.push_back(static_cast<char>(paired[u][v]));
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
              int remaining_edges, int nonadjacent_budget) {
    if (!remaining_edges) return leaf(a, h);
    const int remaining_pairs = remaining_edges / 2;
    const int vertices = static_cast<int>(a.size() + h.size());
    if (P + 1 > vertices || P + 1 < vertices - 2 * remaining_pairs) return 0;
    std::string key = key_of(a, h, m, paired, nonadjacent_budget);
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
        // A further rigorous sub-sum: only pair raw edges that currently
        // share exactly one endpoint.  Such a pair makes precisely one new
        // vertex identification, the amount required by a leading tree
        // contraction.  This restriction is optional and discards positive
        // branches only.
        bool nonadjacent =
            ((u0 == static_cast<int>(u1)) ==
             (v0 == static_cast<int>(v1)));
        if ((adjacent_wick_only || nonadjacent_budget == 0) && nonadjacent)
          continue;
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
                                  remaining_edges - 2,
                                  nonadjacent_budget < 0 ? -1 :
                                  nonadjacent_budget - (nonadjacent ? 1 : 0));
        ans += multiplicity * child_value;
        if (first_wick_only && child_value) {
          memo->emplace(std::move(key), ans);
          return ans;
        }
      }
    }
    memo->emplace(std::move(key), ans);
    return ans;
  }

  // Fast exact certificate for the ``one adjacent Wick branch'' sub-sum.
  // It deliberately does no isomorphism memoization: terminal trees here
  // have at most 28 raw edges, and a leaf-first search usually finds a
  // surviving contraction immediately.  Backtracking keeps the result exact
  // even when the first adjacent partner leaves an unpairable raw forest.
  cpp_int rec_first_adjacent(
      const std::vector<unsigned char> &a,
      const std::vector<unsigned char> &h,
      const std::vector<std::vector<unsigned char>> &m,
      const std::vector<std::vector<unsigned char>> &paired,
      int remaining_edges) {
    if (!remaining_edges) return leaf(a, h);
    const int remaining_pairs = remaining_edges / 2;
    const int vertices = static_cast<int>(a.size() + h.size());
    if (P + 1 > vertices || P + 1 < vertices - 2 * remaining_pairs) return 0;

    int u0 = -1, v0 = -1;
    // Prefer a raw leaf edge: every adjacent pairing must match it at its
    // non-leaf endpoint, which sharply limits branching.
    std::vector<int> row_degree(a.size(), 0), col_degree(h.size(), 0);
    for (size_t u = 0; u < m.size(); ++u)
      for (size_t v = 0; v < m[u].size(); ++v) {
        row_degree[u] += m[u][v];
        col_degree[v] += m[u][v];
      }
    for (size_t u = 0; u < m.size() && u0 < 0; ++u)
      for (size_t v = 0; v < m[u].size(); ++v)
        if (m[u][v] && (row_degree[u] == 1 || col_degree[v] == 1)) {
          u0 = static_cast<int>(u); v0 = static_cast<int>(v); break;
        }
    if (u0 < 0)
      for (size_t u = 0; u < m.size() && u0 < 0; ++u)
        for (size_t v = 0; v < m[u].size(); ++v)
          if (m[u][v]) { u0 = static_cast<int>(u); v0 = static_cast<int>(v); break; }

    auto after_first = m;
    --after_first[u0][v0];
    for (size_t u1 = 0; u1 < after_first.size(); ++u1) {
      for (size_t v1 = 0; v1 < after_first[u1].size(); ++v1) {
        unsigned multiplicity = after_first[u1][v1];
        if (!multiplicity) continue;
        if ((u0 == static_cast<int>(u1)) ==
            (v0 == static_cast<int>(v1))) continue;
        auto child_a = a;
        auto child_h = h;
        auto child_m = after_first;
        auto child_paired = paired;
        --child_m[u1][v1];
        merge_rows(u0, static_cast<int>(u1), child_a, child_m);
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
        cpp_int z = rec_first_adjacent(child_a, child_h, child_m,
                                       child_paired, remaining_edges - 2);
        if (z) return multiplicity * z;
      }
    }
    return 0;
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
    if (first_wick_only && adjacent_wick_only)
      return rec_first_adjacent(t.a, t.h, m, paired,
                                static_cast<int>(t.edges.size()));
    int budget = adjacent_wick_only ? 0 : nonadjacent_wick_budget;
    return rec(t.a, t.h, m, paired, static_cast<int>(t.edges.size()), budget);
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
  std::map<int, cpp_int> root_by_a_hit, root_by_h_hit, root_by_w_hit;

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
    const bool use_upper = wick_upper_bound ||
        (exact_then_upper_cap >= 0 &&
         static_cast<int>(t.edges.size()) > exact_then_upper_cap);
    if (use_upper) {
      int E = static_cast<int>(t.edges.size());
      int A = std::accumulate(t.a.begin(), t.a.end(), 0);
      int H = std::accumulate(t.h.begin(), t.h.end(), 0);
      cpp_int ans = 0;
      if (!(E & 1) && !(A & 1)) {
        // At most (E-1)!! pairings.  For every surviving quotient, merging
        // all row classes and all column classes only increases the product
        // of their centered Gaussian even moments.
        ans = odd_double_factorial(E - 1) * odd_double_factorial(A - 1) *
              odd_double_factorial(2*H - 1);
      }
      wick_memo.emplace(std::move(key), ans);
      return ans;
    }
    WickEvaluator evaluator;
    cpp_int ans = 0;
    if (t.edges.size() <= (size_t)base_edge_cap) {
      bool saved_first = first_wick_only;
      bool saved_adjacent = adjacent_wick_only;
      int saved_nonadjacent_budget = nonadjacent_wick_budget;
      if (hybrid_full_cap >= 0) {
        bool use_subsum = static_cast<int>(t.edges.size()) > hybrid_full_cap;
        first_wick_only = use_subsum && !hybrid_all_adjacent;
        adjacent_wick_only = use_subsum && hybrid_nonadjacent_budget < 0;
        nonadjacent_wick_budget = use_subsum ? hybrid_nonadjacent_budget : -1;
      }
      ans = disable_wick_subproblem_memo ? evaluator.run(t) :
            evaluator.run(t, &wick_subproblem_memo);
      first_wick_only = saved_first;
      adjacent_wick_only = saved_adjacent;
      nonadjacent_wick_budget = saved_nonadjacent_budget;
    }
    wick_memo.emplace(std::move(key), ans);
    return ans;
  }

  cpp_int value(const Tree &t, int k, bool is_root = false) {
    ++calls_by_order[k];
    if (static_cast<int>(t.edges.size()) > path_edge_cap) return 0;
    // Under global parameter negation, a component has parity
    // (-1)^(sum a-exponents + number of W factors); every application of D
    // flips that parity because f is odd and grad(f) is even.  Centered
    // Gaussian expectation kills the odd sector exactly.
    int degree_parity = static_cast<int>(t.edges.size()) +
                        std::accumulate(t.a.begin(), t.a.end(), 0);
    if ((degree_parity + k) & 1) return 0;
    // Feasibility for the positive component-size truncation.  If w of the k
    // remaining rewrites are W-hits, the final forest has 1+w components and
    // E+2(k-w) raw edges.  With every retained component having at most C
    // edges, necessarily E+2(k-w) <= C(1+w).  If even w=k cannot meet this,
    // or the required number exceeds k, this branch is identically discarded.
    {
      int E = static_cast<int>(t.edges.size());
      int numerator = E + 2*k - base_edge_cap;
      int required_w = numerator <= 0 ? 0 :
          (numerator + base_edge_cap + 1) / (base_edge_cap + 2);
      if (required_w > k) return 0;
    }
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
    if (!is_root || root_rewrite_mode == 0 || root_rewrite_mode == 1)
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
    if (!is_root || root_rewrite_mode == 0 || root_rewrite_mode == 2)
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
    if (!is_root || root_rewrite_mode == 0 || root_rewrite_mode == 3)
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
  base_edge_cap = argc > 2 ? std::stoi(argv[2]) : 1000;
  root_rewrite_mode = argc > 3 ? std::stoi(argv[3]) : 0;
  first_wick_only = argc > 4 && std::stoi(argv[4]) != 0;
  adjacent_wick_only = argc > 5 && std::stoi(argv[5]) != 0;
  path_edge_cap = argc > 6 ? std::stoi(argv[6]) : 1000;
  hybrid_full_cap = argc > 7 ? std::stoi(argv[7]) : -1;
  hybrid_all_adjacent = argc > 8 && std::stoi(argv[8]) != 0;
  hybrid_nonadjacent_budget = argc > 9 ? std::stoi(argv[9]) : -1;
  wick_upper_bound = argc > 10 && std::stoi(argv[10]) != 0;
  disable_wick_subproblem_memo = argc > 11 && std::stoi(argv[11]) != 0;
  exact_then_upper_cap = argc > 12 ? std::stoi(argv[12]) : -1;
  Tree root;
  root.a = {1};
  root.h = {1, 1};
  root.edges = {{0, 0}, {0, 1}};

  PeelingRecursion recursion;
  for (int k = max_order; k <= max_order; ++k) {
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
              << " wick_subproblems=" << recursion.wick_subproblem_memo.size()
              << "\n";
    struct rusage usage {};
    if (getrusage(RUSAGE_SELF, &usage) == 0)
      std::cout << "  maxrss_kib=" << usage.ru_maxrss << "\n";
  }
  std::cout << "memo misses by remaining order:";
  for (auto [k, count] : recursion.misses_by_order)
    std::cout << " [" << k << ':' << count << ']';
  std::cout << "\n";
}

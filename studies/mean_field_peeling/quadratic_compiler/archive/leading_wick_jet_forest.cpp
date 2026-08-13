#include <algorithm>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

#ifdef _OPENMP
#include <omp.h>
#endif

#include <boost/multiprecision/cpp_int.hpp>

using boost::multiprecision::cpp_int;

struct State {
  int r{};
  std::vector<unsigned char> a;
  std::vector<unsigned char> h;
  std::vector<std::pair<unsigned char, unsigned char>> edges;
};

static std::string encode_ordered(const State &s) {
  std::string k;
  k.reserve(4 + s.a.size() + s.h.size() + 2 * s.edges.size());
  k.push_back(static_cast<char>(s.r));
  k.push_back(static_cast<char>(s.a.size()));
  k.push_back(static_cast<char>(s.h.size()));
  k.push_back(static_cast<char>(s.edges.size()));
  for (auto x : s.a) k.push_back(static_cast<char>(x));
  for (auto x : s.h) k.push_back(static_cast<char>(x));
  for (auto [u, v] : s.edges) {
    k.push_back(static_cast<char>(u));
    k.push_back(static_cast<char>(v));
  }
  return k;
}

static State decode(const std::string &k) {
  State s;
  size_t q = 0;
  auto byte = [&]() { return static_cast<unsigned char>(k[q++]); };
  s.r = byte();
  int na = byte(), nh = byte(), ne = byte();
  s.a.resize(na);
  s.h.resize(nh);
  for (auto &x : s.a) x = byte();
  for (auto &x : s.h) x = byte();
  s.edges.resize(ne);
  for (auto &e : s.edges) e = {byte(), byte()};
  return s;
}

// Ordered equitable refinement for a vertex-colored bipartite multigraph.
static void refine_partition(
    const std::vector<std::vector<unsigned char>> &adj,
    std::vector<std::vector<int>> &cells) {
  while (true) {
    bool changed = false;
    std::vector<std::vector<int>> out;
    for (const auto &cell : cells) {
      std::map<std::vector<int>, std::vector<int>> groups;
      for (int v : cell) {
        std::vector<int> sig;
        sig.reserve(cells.size());
        for (const auto &target : cells) {
          int z = 0;
          for (int w : target) z += adj[v][w];
          sig.push_back(z);
        }
        groups[sig].push_back(v);
      }
      if (groups.size() > 1) changed = true;
      for (auto &[sig, vertices] : groups) out.push_back(std::move(vertices));
    }
    cells.swap(out);
    if (!changed) return;
  }
}

static std::string discrete_code(
    const State &s, const std::vector<std::vector<unsigned char>> &adj,
    const std::vector<std::vector<int>> &cells) {
  const int na = static_cast<int>(s.a.size());
  std::vector<int> rows, cols;
  for (const auto &cell : cells) {
    int v = cell.front();
    if (v < na) rows.push_back(v);
    else cols.push_back(v);
  }
  State t;
  t.r = s.r;
  for (int v : rows) t.a.push_back(s.a[v]);
  for (int v : cols) t.h.push_back(s.h[v - na]);
  for (size_t i = 0; i < rows.size(); ++i) {
    for (size_t j = 0; j < cols.size(); ++j) {
      for (int m = 0; m < adj[rows[i]][cols[j]]; ++m)
        t.edges.push_back({static_cast<unsigned char>(i),
                           static_cast<unsigned char>(j)});
    }
  }
  return encode_ordered(t);
}

static std::string canonical_search(
    const State &s, const std::vector<std::vector<unsigned char>> &adj,
    std::vector<std::vector<int>> cells) {
  refine_partition(adj, cells);
  int chosen = -1;
  // Smallest nonsingleton cell generally gives the least branching.
  for (size_t i = 0; i < cells.size(); ++i) {
    if (cells[i].size() > 1 &&
        (chosen < 0 || cells[i].size() < cells[chosen].size()))
      chosen = static_cast<int>(i);
  }
  if (chosen < 0) return discrete_code(s, adj, cells);

  std::string best;
  const auto branch_cell = cells[chosen];
  for (int v : branch_cell) {
    std::vector<std::vector<int>> child;
    child.reserve(cells.size() + 1);
    for (int i = 0; i < chosen; ++i) child.push_back(cells[i]);
    child.push_back({v});
    std::vector<int> rest;
    for (int w : branch_cell) if (w != v) rest.push_back(w);
    if (!rest.empty()) child.push_back(std::move(rest));
    for (size_t i = chosen + 1; i < cells.size(); ++i)
      child.push_back(cells[i]);
    std::string candidate = canonical_search(s, adj, std::move(child));
    if (best.empty() || candidate < best) best = std::move(candidate);
  }
  return best;
}

static std::string canonical_encode(const State &s) {
  const int na = static_cast<int>(s.a.size());
  const int nh = static_cast<int>(s.h.size());
  const int n = na + nh;
  std::vector<std::vector<unsigned char>> adj(
      n, std::vector<unsigned char>(n, 0));
  for (auto [u, v] : s.edges) {
    ++adj[u][na + v];
    ++adj[na + v][u];
  }

  // Initial ordered colors: side first, then factor exponent.
  std::map<std::pair<int, int>, std::vector<int>> groups;
  for (int u = 0; u < na; ++u) groups[{0, s.a[u]}].push_back(u);
  for (int v = 0; v < nh; ++v) groups[{1, s.h[v]}].push_back(na + v);
  std::vector<std::vector<int>> cells;
  for (auto &[color, vertices] : groups) cells.push_back(std::move(vertices));
  return canonical_search(s, adj, std::move(cells));
}

static cpp_int odd_double_factorial(int odd) {
  cpp_int z = 1;
  for (int j = odd; j >= 1; j -= 2) z *= j;
  return z;
}

static std::string normalize_classes(std::vector<unsigned char> c) {
  unsigned char next = 0;
  unsigned char map[64];
  std::fill(std::begin(map), std::end(map), 255);
  std::string out;
  out.resize(c.size());
  for (size_t i = 0; i < c.size(); ++i) {
    if (map[c[i]] == 255) map[c[i]] = next++;
    out[i] = static_cast<char>(map[c[i]]);
  }
  return out;
}

static void unite_classes(std::vector<unsigned char> &c, int x, int y) {
  unsigned char cx = c[x], cy = c[y];
  if (cx == cy) return;
  for (auto &z : c) if (z == cy) z = cx;
  std::string norm = normalize_classes(c);
  for (size_t i = 0; i < c.size(); ++i)
    c[i] = static_cast<unsigned char>(norm[i]);
}

struct PairEvaluator {
  const State &s;
  int P;
  std::unordered_map<std::string, cpp_int> memo;

  cpp_int leaf(const std::vector<unsigned char> &cls) {
    const int na = static_cast<int>(s.a.size());
    const int nv = static_cast<int>(cls.size());
    int V = 0;
    for (auto x : cls) V = std::max(V, static_cast<int>(x) + 1);
    if (V - P - s.r != 0) return 0;

    std::vector<int> ae(V, 0), he(V, 0);
    for (int i = 0; i < na; ++i) ae[cls[i]] += s.a[i];
    for (int i = na; i < nv; ++i) he[cls[i]] += s.h[i - na];
    cpp_int ans = 1;
    for (int q = 0; q < V; ++q) {
      if (ae[q] & 1) return 0;
      ans *= odd_double_factorial(ae[q] - 1);
      ans *= odd_double_factorial(2 * he[q] - 1);
    }
    return ans;
  }

  cpp_int rec(uint32_t mask, const std::vector<unsigned char> &cls) {
    if (!mask) return leaf(cls);

    int V = 0;
    for (auto x : cls) V = std::max(V, static_cast<int>(x) + 1);
    int rem_pairs = __builtin_popcount(mask) / 2;
    int target = P + s.r;
    if (target > V || target < V - 2 * rem_pairs) return 0;

    std::string key;
    key.resize(4 + cls.size());
    key[0] = static_cast<char>(mask & 255);
    key[1] = static_cast<char>((mask >> 8) & 255);
    key[2] = static_cast<char>((mask >> 16) & 255);
    key[3] = static_cast<char>((mask >> 24) & 255);
    for (size_t i = 0; i < cls.size(); ++i)
      key[4 + i] = static_cast<char>(cls[i]);
    auto it = memo.find(key);
    if (it != memo.end()) return it->second;

    int e0 = __builtin_ctz(mask);
    uint32_t rest = mask & ~(uint32_t(1) << e0);
    cpp_int ans = 0;
    const int na = static_cast<int>(s.a.size());
    for (uint32_t bits = rest; bits; bits &= bits - 1) {
      int e1 = __builtin_ctz(bits);
      std::vector<unsigned char> child = cls;
      unite_classes(child, s.edges[e0].first, s.edges[e1].first);
      unite_classes(child, na + s.edges[e0].second,
                    na + s.edges[e1].second);
      ans += rec(rest & ~(uint32_t(1) << e1), child);
    }
    memo.emplace(std::move(key), ans);
    return ans;
  }

  explicit PairEvaluator(const State &state)
      : s(state), P(static_cast<int>(state.edges.size()) / 2) {}

  cpp_int run() {
    if (s.edges.size() & 1 || s.edges.size() >= 32) return 0;
    std::vector<unsigned char> cls(s.a.size() + s.h.size());
    std::iota(cls.begin(), cls.end(), 0);
    uint32_t mask = (uint32_t(1) << s.edges.size()) - 1;
    return rec(mask, cls);
  }
};

static cpp_int pairing_sum(const State &s) {
  PairEvaluator evaluator(s);
  return evaluator.run();
}

// Equivalent Wick recursion after quotienting indistinguishable remaining
// edge factors.  A state consists only of current row/column equality classes,
// their accumulated exponents, and the multiplicity matrix of unpaired W's.
// Fixing one representative of the first nonempty edge type and multiplying by
// the number of possible partners preserves the count of labelled pairings.
struct TypePairEvaluator {
  int P;
  int r;
  std::unordered_map<std::string, cpp_int> local_memo;
  std::unordered_map<std::string, cpp_int> *memo;

  static bool is_forest(
      const std::vector<std::vector<unsigned char>> &paired) {
    int rows=paired.size(), cols=rows?paired[0].size():0;
    std::vector<int> parent(rows+cols),rank(rows+cols,0);
    std::iota(parent.begin(),parent.end(),0);
    auto root=[&](int x){int y=x;while(parent[y]!=y)y=parent[y];
      while(parent[x]!=x){int q=parent[x];parent[x]=y;x=q;}return y;};
    for(int i=0;i<rows;++i)for(int j=0;j<cols;++j){
      if(paired[i][j]>1)return false;if(!paired[i][j])continue;
      int x=root(i),y=root(rows+j);if(x==y)return false;
      if(rank[x]<rank[y])std::swap(x,y);parent[y]=x;if(rank[x]==rank[y])++rank[x];
    }return true;
  }

  static std::string key_of(const std::vector<unsigned char> &a,
                            const std::vector<unsigned char> &h,
                            const std::vector<std::vector<unsigned char>> &m,
                            const std::vector<std::vector<unsigned char>> &paired) {
    State quotient;
    quotient.a = a;
    quotient.h = h;
    for (size_t u = 0; u < m.size(); ++u)
      for (size_t v = 0; v < m[u].size(); ++v)
        for (int q = 0; q < m[u][v]; ++q)
          quotient.edges.push_back({static_cast<unsigned char>(u),
                                    static_cast<unsigned char>(v)});
    // Row/column merges always retain the lower current index, so the ordered
    // quotient is independent of the order in which a fixed pair of set
    // partitions was reached.  Ordered encoding is therefore an exact memo
    // key here; canonical graph isomorphism is unnecessary and much slower.
    std::string key=encode_ordered(quotient);key.push_back('|');
    for(const auto&row:paired)for(auto z:row)key.push_back((char)z);
    return key;
  }

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

  cpp_int leaf(const std::vector<unsigned char> &a,
               const std::vector<unsigned char> &h) const {
    if (static_cast<int>(a.size() + h.size()) != P + r) return 0;
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
    int remaining_pairs = remaining_edges / 2;
    int V = a.size() + h.size();
    int target = P + r;
    if (target > V || target < V - 2 * remaining_pairs) return 0;

    std::string key = key_of(a, h, m, paired);
    key.insert(key.begin(), static_cast<char>(P));
    auto found = memo->find(key);
    if (found != memo->end()) return found->second;

    int u0 = -1, v0 = -1;
    for (size_t u = 0; u < m.size() && u0 < 0; ++u)
      for (size_t v = 0; v < m[u].size(); ++v) if (m[u][v]) {
        u0 = u; v0 = v; break;
      }

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
        merge_rows(u0, u1, child_a, child_m);
        {std::vector<unsigned char> dummy(child_paired.size(),0);
         merge_rows(u0,u1,dummy,child_paired);}
        merge_cols(v0, v1, child_h, child_m);
        {std::vector<unsigned char> dummy(child_paired.empty()?0:child_paired[0].size(),0);
         merge_cols(v0,v1,dummy,child_paired);}
        int nu=std::min(u0,(int)u1),nv=std::min(v0,(int)v1);
        ++child_paired[nu][nv];
        if(!is_forest(child_paired))continue;
        ans += multiplicity *
               rec(child_a, child_h, child_m, child_paired, remaining_edges - 2);
      }
    }
    memo->emplace(std::move(key), ans);
    return ans;
  }

  explicit TypePairEvaluator(
      const State &s,
      std::unordered_map<std::string, cpp_int> *shared_memo = nullptr)
      : P(static_cast<int>(s.edges.size()) / 2), r(s.r),
        memo(shared_memo ? shared_memo : &local_memo) {}

  cpp_int run(const State &s) {
    if (s.edges.size() & 1) return 0;
    auto a = s.a;
    auto h = s.h;
    std::vector<std::vector<unsigned char>> m(
        a.size(), std::vector<unsigned char>(h.size(), 0));
    for (auto [u, v] : s.edges) ++m[u][v];
    std::vector<std::vector<unsigned char>> paired(
        a.size(),std::vector<unsigned char>(h.size(),0));
    return rec(a, h, m, paired, s.edges.size());
  }
};

static cpp_int pairing_sum_types(const State &s) {
  TypePairEvaluator evaluator(s);
  return evaluator.run(s);
}

static cpp_int pairing_sum_types(
    const State &s, std::unordered_map<std::string, cpp_int> &shared_memo) {
  TypePairEvaluator evaluator(s, &shared_memo);
  return evaluator.run(s);
}

// All derivative states are decorated bipartite forests.  The following AHU
// encoding is a linearithmic canonical key for an unrooted colored forest.
static std::string rooted_tree_code(
    int v, int parent, const State &s,
    const std::vector<std::vector<int>> &neighbors) {
  const int na = static_cast<int>(s.a.size());
  std::vector<std::string> children;
  for (int w : neighbors[v]) if (w != parent)
    children.push_back(rooted_tree_code(w, v, s, neighbors));
  std::sort(children.begin(), children.end());
  std::string code;
  code.push_back('(');
  code.push_back(v < na ? 'A' : 'H');
  code.push_back(static_cast<char>(1 + (v < na ? s.a[v] : s.h[v - na])));
  for (const auto &child : children) code += child;
  code.push_back(')');
  return code;
}

static std::string forest_key(const State &s) {
  const int na = static_cast<int>(s.a.size());
  const int n = na + static_cast<int>(s.h.size());
  std::vector<std::vector<int>> neighbors(n);
  for (auto [u, v0] : s.edges) {
    int v = na + v0;
    neighbors[u].push_back(v);
    neighbors[v].push_back(u);
  }

  std::vector<unsigned char> seen(n, 0);
  std::vector<std::string> components;
  int checked_edges = 0;
  for (int seed = 0; seed < n; ++seed) if (!seen[seed]) {
    std::vector<int> vertices{seed};
    seen[seed] = 1;
    for (size_t q = 0; q < vertices.size(); ++q) {
      int v = vertices[q];
      checked_edges += neighbors[v].size();
      for (int w : neighbors[v]) if (!seen[w]) {
        seen[w] = 1;
        vertices.push_back(w);
      }
    }
    int edge_count = 0;
    for (int v : vertices) edge_count += neighbors[v].size();
    edge_count /= 2;
    if (edge_count + 1 != static_cast<int>(vertices.size())) {
      std::cerr << "forest invariant violated\n";
      std::abort();
    }

    std::vector<int> degree(n, 0), leaves;
    for (int v : vertices) {
      degree[v] = neighbors[v].size();
      if (degree[v] <= 1) leaves.push_back(v);
    }
    int remaining = vertices.size();
    while (remaining > 2) {
      std::vector<int> next_leaves;
      remaining -= leaves.size();
      for (int v : leaves) {
        degree[v] = 0;
        for (int w : neighbors[v]) if (degree[w] > 0) {
          --degree[w];
          if (degree[w] == 1) next_leaves.push_back(w);
        }
      }
      leaves.swap(next_leaves);
    }
    std::vector<int> centers;
    for (int v : vertices) if (degree[v] > 0 || vertices.size() == 1)
      centers.push_back(v);
    if (centers.empty()) {
      // A two-vertex tree is peeled to two zero-degree centers.
      centers = leaves;
    }
    std::string best;
    for (int center : centers) {
      std::string code = rooted_tree_code(center, -1, s, neighbors);
      if (best.empty() || code < best) best = std::move(code);
    }
    components.push_back(std::move(best));
  }
  if (checked_edges != 2 * static_cast<int>(s.edges.size())) std::abort();
  std::sort(components.begin(), components.end());
  std::string key;
  key.push_back(static_cast<char>(s.r));
  for (const auto &component : components) key += component;
  return key;
}

// The derivative graphs are forests and the explicit normalization exponent
// equals the number of raw components.  Any Wick pair joining two distinct
// raw components loses at least one extra free index, hence is subleading.
// The leading contraction therefore factors exactly over components.
static cpp_int pairing_sum_components(
    const State &s, std::unordered_map<std::string, cpp_int> &cache,
    std::unordered_map<std::string, cpp_int> &type_cache) {
  const int na = static_cast<int>(s.a.size());
  const int nh = static_cast<int>(s.h.size());
  const int n = na + nh;
  std::vector<std::vector<int>> neighbors(n);
  for (auto [u0, v0] : s.edges) {
    int u = u0, v = na + v0;
    neighbors[u].push_back(v);
    neighbors[v].push_back(u);
  }
  std::vector<unsigned char> seen(n, 0);
  cpp_int answer = 1;
  int component_count = 0;
  for (int seed = 0; seed < n; ++seed) if (!seen[seed]) {
    ++component_count;
    std::vector<int> vertices{seed};
    seen[seed] = 1;
    for (size_t q = 0; q < vertices.size(); ++q) {
      int v = vertices[q];
      for (int w : neighbors[v]) if (!seen[w]) {
        seen[w] = 1;
        vertices.push_back(w);
      }
    }
    std::vector<int> row_map(na, -1), col_map(nh, -1);
    State component;
    component.r = 1;
    for (int v : vertices) if (v < na) {
      row_map[v] = component.a.size();
      component.a.push_back(s.a[v]);
    }
    for (int v : vertices) if (v >= na) {
      col_map[v - na] = component.h.size();
      component.h.push_back(s.h[v - na]);
    }
    for (auto [u, v] : s.edges) {
      if (row_map[u] >= 0 && col_map[v] >= 0)
        component.edges.push_back({
            static_cast<unsigned char>(row_map[u]),
            static_cast<unsigned char>(col_map[v])});
    }
    if (component.edges.size() + 1 !=
        component.a.size() + component.h.size()) std::abort();
    std::string key = forest_key(component);
    auto found = cache.find(key);
    cpp_int value;
    if (found != cache.end()) {
      value = found->second;
    } else {
      value = component.edges.size() <= 18
                  ? pairing_sum(component)
                  : pairing_sum_types(component, type_cache);
      cache.emplace(std::move(key), value);
    }
    if (value == 0) return 0;
    answer *= value;
  }
  if (component_count != s.r) std::abort();
  return answer;
}

struct WeightedState {
  State state;
  cpp_int coefficient{};
};

// Optional monotone pruning for fixed-lambda-sector runs.  Derivative
// rewrites never decrease the number of W-pairs, so states above this bound
// can never return to a requested lower sector.
static int generation_max_pairs = 1000000;

static void add_term(std::unordered_map<std::string, WeightedState> &terms,
                     State state, const cpp_int &coefficient) {
  if (static_cast<int>(state.edges.size() / 2) > generation_max_pairs) return;
  std::string key = forest_key(state);
  auto [it, inserted] = terms.try_emplace(
      std::move(key), WeightedState{state, coefficient});
  if (!inserted) it->second.coefficient += coefficient;
}

int main(int argc, char **argv) {
  int max_order = argc > 1 ? std::stoi(argv[1]) : 7;
  int min_pairs = argc > 2 ? std::stoi(argv[2]) : 0;
  int max_pairs_to_evaluate = argc > 3 ? std::stoi(argv[3]) : 100;
  std::string export_path = argc > 4 ? argv[4] : "";
  size_t final_parent_limit = argc > 5 ? std::stoull(argv[5]) : 0;
  // With no W-hit, order k has exactly k+1 raw W-pairs.  Therefore selecting
  // the maximal sector forces every rewrite to be an a- or h-hit.  Generate
  // only this sector when requested, instead of carrying the enormous lower
  // sectors which can never return to it.
  bool maximal_sector_only =
      min_pairs == max_order + 1 && max_pairs_to_evaluate == max_order + 1;
  generation_max_pairs = max_pairs_to_evaluate;
  State init;
  init.r = 1;
  init.a = {1};
  init.h = {1, 1};
  init.edges = {{0, 0}, {0, 1}};
  std::unordered_map<std::string, WeightedState> terms, next;
  add_term(terms, init, 1);

  for (int order = 1; order <= max_order; ++order) {
    auto start = std::chrono::steady_clock::now();
    next.clear();
    next.reserve(terms.size() * 6);
    size_t parents_used = 0;
    for (const auto &[key, weighted] : terms) {
      if (order == max_order && final_parent_limit &&
          parents_used++ >= final_parent_limit) break;
      const State &s = weighted.state;
      const cpp_int &coeff = weighted.coefficient;
      for (size_t u = 0; u < s.a.size(); ++u) if (s.a[u]) {
        State t = s;
        unsigned mult = t.a[u];
        --t.a[u];
        unsigned char l = static_cast<unsigned char>(t.h.size());
        t.h.push_back(1); t.h.push_back(1);
        t.edges.push_back({static_cast<unsigned char>(u), l});
        t.edges.push_back({static_cast<unsigned char>(u),
                           static_cast<unsigned char>(l + 1)});
        add_term(next, std::move(t), coeff * mult);
      }
      for (size_t v = 0; v < s.h.size(); ++v) if (s.h[v]) {
        State t = s;
        unsigned mult = t.h[v];
        unsigned char u = static_cast<unsigned char>(t.a.size());
        unsigned char w = static_cast<unsigned char>(t.h.size());
        t.a.push_back(1); t.h.push_back(1);
        t.edges.push_back({u, static_cast<unsigned char>(v)});
        t.edges.push_back({u, w});
        add_term(next, std::move(t), coeff * mult * 8);
      }
      for (size_t q = 0; q < s.edges.size(); ++q) {
        if (maximal_sector_only) break;
        State t = s;
        auto [u, v] = t.edges[q];
        ++t.a[u]; ++t.h[v];
        unsigned char w = static_cast<unsigned char>(t.h.size());
        t.h.push_back(1);
        t.edges.erase(t.edges.begin() + q);
        t.edges.push_back({u, w});
        ++t.r;
        add_term(next, std::move(t), coeff * 2);
      }
    }
    terms.swap(next);
    auto end = std::chrono::steady_clock::now();
    std::cerr << "order " << order << " canonical states " << terms.size()
              << " generation_seconds "
              << std::chrono::duration<double>(end - start).count() << "\n";

    if (order == max_order) {
      std::map<int, size_t> count_by_pairs;
      for (const auto &[key, weighted] : terms)
        ++count_by_pairs[weighted.state.edges.size() / 2];
      std::cerr << "  state counts by pairs:";
      for (auto [p, count] : count_by_pairs)
        std::cerr << " [" << p << ":" << count << "]";
      std::cerr << "\n";
      if (!export_path.empty()) {
        size_t export_count = 0;
        for (const auto &[key, weighted] : terms) {
          int pairs = weighted.state.edges.size() / 2;
          if (pairs >= min_pairs && pairs <= max_pairs_to_evaluate)
            ++export_count;
        }
        std::ofstream out(export_path);
        out << export_count << "\n";
        for (const auto &[key, weighted] : terms) {
          const State &s = weighted.state;
          int pairs = s.edges.size() / 2;
          if (pairs < min_pairs || pairs > max_pairs_to_evaluate) continue;
          out << weighted.coefficient << ' ' << s.r << ' '
              << s.a.size() << ' ' << s.h.size();
          for (auto z : s.a) out << ' ' << static_cast<int>(z);
          for (auto z : s.h) out << ' ' << (2 * static_cast<int>(z));
          for (size_t u = 0; u < s.a.size(); ++u)
            for (size_t v = 0; v < s.h.size(); ++v) {
              int count = 0;
              for (auto [x, y] : s.edges) if (x == u && y == v) ++count;
              out << ' ' << count;
            }
          out << "\n";
        }
      }
    }

    if (export_path.empty() && (order & 1) &&
        (order <= 5 || order == max_order)) {
      start = std::chrono::steady_clock::now();
      cpp_int total = 0;
      std::vector<cpp_int> by_pairs(max_order + 4);
      std::vector<const WeightedState *> todo;
      for (const auto &[key, weighted] : terms) {
        int pair_count = weighted.state.edges.size() / 2;
        if (pair_count >= min_pairs && pair_count <= max_pairs_to_evaluate)
          todo.push_back(&weighted);
      }
#ifdef _OPENMP
      int thread_count = omp_get_max_threads();
#else
      int thread_count = 1;
#endif
      std::vector<std::vector<cpp_int>> thread_sums(
          thread_count, std::vector<cpp_int>(max_order + 4));
      std::vector<size_t> thread_nonzero(thread_count, 0);
      std::vector<std::unordered_map<std::string, cpp_int>> component_caches(
          thread_count);
      std::vector<std::unordered_map<std::string, cpp_int>> type_caches(
          thread_count);
#pragma omp parallel for schedule(dynamic, 1)
      for (size_t item = 0; item < todo.size(); ++item) {
#ifdef _OPENMP
        int tid = omp_get_thread_num();
#else
        int tid = 0;
#endif
        const State &s = todo[item]->state;
        cpp_int wick = pairing_sum_components(
            s, component_caches[tid], type_caches[tid]);
        if (wick != 0) ++thread_nonzero[tid];
        thread_sums[tid][s.edges.size() / 2] +=
            todo[item]->coefficient * wick;
      }
      size_t nonzero = 0;
      for (int tid = 0; tid < thread_count; ++tid) {
        nonzero += thread_nonzero[tid];
        for (size_t p = 0; p < by_pairs.size(); ++p)
          by_pairs[p] += thread_sums[tid][p];
      }
      for (const auto &z : by_pairs) total += z;
      end = std::chrono::steady_clock::now();
      std::cout << "D^" << order << " f leading expectation = " << total
                << "\n";
      std::cout << "  variance polynomial:";
      for (size_t p = 0; p < by_pairs.size(); ++p) if (by_pairs[p] != 0)
        std::cout << " [lambda^" << p << ": " << by_pairs[p] << "]";
      std::cout << "\n";
      std::cerr << "  nonzero states " << nonzero << " evaluation_seconds "
                << std::chrono::duration<double>(end - start).count() << "\n";
    }
  }
}

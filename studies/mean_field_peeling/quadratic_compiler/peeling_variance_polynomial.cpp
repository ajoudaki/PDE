// Exact low-degree variance polynomial for the leading mean-field jet.
//
// If Var(B_pi)=lambda/n, every terminal Wick pair contributes one lambda.
// The connected-component peeling recurrence can therefore carry a short
// polynomial rather than a scalar.  With component_edge_cap=2*max_degree,
// all coefficients through lambda^max_degree are exact: a terminal forest
// of total Wick degree at most max_degree cannot contain a component with
// more than 2*max_degree raw B edges.

#define main peeling_lower_bound_hidden_main
#include "peeling_lower_bound.cpp"
#undef main

#include <array>

static constexpr int POLY_MAX = 16;
static int requested_degree = POLY_MAX;

struct Poly {
  std::array<cpp_int, POLY_MAX + 1> z{};
};

static Poly add(Poly x, const Poly &y) {
  for (int j = 0; j <= POLY_MAX; ++j) x.z[j] += y.z[j];
  return x;
}

static Poly scale(Poly x, cpp_int c) {
  for (auto &v : x.z) v *= c;
  return x;
}

static Poly multiply(const Poly &x, const Poly &y) {
  Poly out;
  for (int i = 0; i <= POLY_MAX; ++i)
    for (int j = 0; i + j <= requested_degree; ++j)
      out.z[i + j] += x.z[i] * y.z[j];
  return out;
}

struct PolynomialPeeling {
  std::unordered_map<std::string, Poly> value_memo;
  std::unordered_map<std::string, cpp_int> wick_memo;
  std::unordered_map<std::string, cpp_int> wick_subproblem_memo;

  std::string key(const Tree &t, int k) const {
    std::string out;
    out.push_back(static_cast<char>(k));
    out += canonical_key(t);
    return out;
  }

  cpp_int wick(const Tree &t) {
    std::string k = canonical_key(t);
    auto found = wick_memo.find(k);
    if (found != wick_memo.end()) return found->second;
    WickEvaluator evaluator;
    cpp_int ans = t.edges.size() <= static_cast<size_t>(base_edge_cap)
        ? evaluator.run(t, &wick_subproblem_memo) : 0;
    wick_memo.emplace(std::move(k), ans);
    return ans;
  }

  Poly value(const Tree &t, int remaining) {
    int parity = static_cast<int>(t.edges.size()) +
        std::accumulate(t.a.begin(), t.a.end(), 0);
    if ((parity + remaining) & 1) return {};

    // Same safe component-cap feasibility pruning as the scalar certificate.
    int edge_count = static_cast<int>(t.edges.size());
    int numerator = edge_count + 2 * remaining - base_edge_cap;
    int required_w = numerator <= 0 ? 0 :
        (numerator + base_edge_cap + 1) / (base_edge_cap + 2);
    if (required_w > remaining) return {};

    std::string k = key(t, remaining);
    auto found = value_memo.find(k);
    if (found != value_memo.end()) return found->second;
    if (remaining == 0) {
      Poly out;
      int degree = static_cast<int>(t.edges.size() / 2);
      if (degree <= requested_degree) out.z[degree] = wick(t);
      value_memo.emplace(std::move(k), out);
      return out;
    }

    Poly out;
    for (size_t u = 0; u < t.a.size(); ++u) if (t.a[u]) {
      Tree child = t;
      unsigned mult = child.a[u];
      --child.a[u];
      unsigned char v = static_cast<unsigned char>(child.h.size());
      child.h.push_back(1); child.h.push_back(1);
      child.edges.push_back({static_cast<unsigned char>(u), v});
      child.edges.push_back({static_cast<unsigned char>(u),
                             static_cast<unsigned char>(v + 1)});
      out = add(out, scale(value(child, remaining - 1), mult));
    }
    for (size_t v = 0; v < t.h.size(); ++v) if (t.h[v]) {
      Tree child = t;
      unsigned mult = 8 * child.h[v];
      unsigned char u = static_cast<unsigned char>(child.a.size());
      unsigned char fresh = static_cast<unsigned char>(child.h.size());
      child.a.push_back(1); child.h.push_back(1);
      child.edges.push_back({u, static_cast<unsigned char>(v)});
      child.edges.push_back({u, fresh});
      out = add(out, scale(value(child, remaining - 1), mult));
    }
    for (size_t e = 0; e < t.edges.size(); ++e) {
      Tree forest = t;
      auto [u, v] = forest.edges[e];
      ++forest.a[u]; ++forest.h[v];
      unsigned char fresh = static_cast<unsigned char>(forest.h.size());
      forest.h.push_back(1);
      forest.edges.erase(forest.edges.begin() + e);
      forest.edges.push_back({u, fresh});
      auto children = split_components(forest);
      if (children.size() != 2) std::abort();
      Poly convolution;
      for (int q = 0; q < remaining; ++q) {
        Poly term = multiply(value(children[0], q),
                             value(children[1], remaining - 1 - q));
        convolution = add(convolution,
                          scale(term, choose(remaining - 1, q)));
      }
      out = add(out, scale(convolution, 2));
    }
    value_memo.emplace(std::move(k), out);
    return out;
  }
};

int main(int argc, char **argv) {
  int order = argc > 1 ? std::stoi(argv[1]) : 11;
  int max_degree = argc > 2 ? std::stoi(argv[2]) : 10;
  if (max_degree > POLY_MAX) return 2;
  requested_degree = max_degree;
  base_edge_cap = 2 * max_degree;
  Tree root;
  root.a = {1}; root.h = {1, 1}; root.edges = {{0, 0}, {0, 1}};
  PolynomialPeeling recurrence;
  auto start = std::chrono::steady_clock::now();
  Poly p = recurrence.value(root, order);
  auto stop = std::chrono::steady_clock::now();
  std::cout << "D^" << order << " f variance polynomial:";
  for (int j = 0; j <= max_degree; ++j)
    if (p.z[j]) std::cout << " [lambda^" << j << ": " << p.z[j] << ']';
  std::cout << "\nseconds="
            << std::chrono::duration<double>(stop - start).count()
            << " value_cache=" << recurrence.value_memo.size()
            << " wick_cache=" << recurrence.wick_memo.size()
            << " wick_subproblems=" << recurrence.wick_subproblem_memo.size()
            << "\n";
}

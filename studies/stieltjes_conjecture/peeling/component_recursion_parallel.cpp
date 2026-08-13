// Parallel two-phase driver for the exact connected-component peeling
// recursion.  The mathematical recurrence and Wick evaluator live in
// component_recursion_fast2.cpp; renaming its command-line entry point lets
// this audit driver reuse exactly the same implementation rather than fork it.
#define main component_recursion_serial_main
#include "component_recursion_fast2.cpp"
#undef main

#include <atomic>
#include <unordered_set>

#ifdef _OPENMP
#include <omp.h>
#endif

// Phase one traverses the dependency DAG without evaluating a Wick base case.
// This is exact because every recurrence coefficient is non-negative and the
// traversal applies precisely the same structural parity zeros as value().
struct DependencyDiscovery {
  std::unordered_set<std::string> seen;
  std::unordered_map<std::string, Tree> bases;
  std::map<int, std::size_t> states_by_remaining_order;

  static std::string state_key(const Tree &t, int k) {
    std::string key;
    key.push_back(static_cast<char>(k));
    key += canonical_key(t);
    return key;
  }

  void visit(const Tree &t, int k) {
    const int degree_parity = static_cast<int>(t.edges.size()) +
        std::accumulate(t.a.begin(), t.a.end(), 0);
    if ((degree_parity + k) & 1) return;
    if (t.edges.size() & 1) return;
    if (!seen.emplace(state_key(t, k)).second) return;
    ++states_by_remaining_order[k];

    if (k == 0) {
      bases.try_emplace(canonical_key(t), t);
      return;
    }

    for (std::size_t u = 0; u < t.a.size(); ++u) if (t.a[u]) {
      Tree child = t;
      --child.a[u];
      const auto v0 = static_cast<unsigned char>(child.h.size());
      child.h.push_back(1);
      child.h.push_back(1);
      child.edges.push_back({static_cast<unsigned char>(u), v0});
      child.edges.push_back({static_cast<unsigned char>(u),
                             static_cast<unsigned char>(v0 + 1)});
      visit(child, k - 1);
    }

    for (std::size_t v = 0; v < t.h.size(); ++v) if (t.h[v]) {
      Tree child = t;
      const auto u0 = static_cast<unsigned char>(child.a.size());
      const auto v1 = static_cast<unsigned char>(child.h.size());
      child.a.push_back(1);
      child.h.push_back(1);
      child.edges.push_back({u0, static_cast<unsigned char>(v)});
      child.edges.push_back({u0, v1});
      visit(child, k - 1);
    }

    for (std::size_t e = 0; e < t.edges.size(); ++e) {
      Tree forest = t;
      const auto [u, v] = forest.edges[e];
      ++forest.a[u];
      ++forest.h[v];
      const auto fresh = static_cast<unsigned char>(forest.h.size());
      forest.h.push_back(1);
      forest.edges.erase(forest.edges.begin() + e);
      forest.edges.push_back({u, fresh});
      auto children = split_components(forest);
      if (children.size() != 2) std::abort();
      for (int q = 0; q <= k - 1; ++q) {
        visit(children[0], q);
        visit(children[1], k - 1 - q);
      }
    }
  }
};

int main(int argc, char **argv) {
  const int max_order = argc > 1 ? std::stoi(argv[1]) : 13;
  Tree root;
  root.a = {1};
  root.h = {1, 1};
  root.edges = {{0, 0}, {0, 1}};

  const auto discovery_start = std::chrono::steady_clock::now();
  DependencyDiscovery discovery;
  for (int k = 0; k <= max_order; ++k) discovery.visit(root, k);
  const auto discovery_stop = std::chrono::steady_clock::now();

  std::vector<std::pair<std::string, Tree>> bases;
  bases.reserve(discovery.bases.size());
  for (auto &item : discovery.bases) bases.push_back(item);
  // Dynamic scheduling already balances irregular Wick costs; processing the
  // largest edge counts first reduces the final long-tail imbalance.
  std::sort(bases.begin(), bases.end(), [](const auto &x, const auto &y) {
    return x.second.edges.size() > y.second.edges.size();
  });
  std::vector<cpp_int> base_values(bases.size());
  std::atomic<std::size_t> completed{0};

#ifdef _OPENMP
  const int thread_count = omp_get_max_threads();
#else
  const int thread_count = 1;
#endif
  std::vector<std::unordered_map<std::string, cpp_int>> thread_memos(
      thread_count);
  const auto wick_start = std::chrono::steady_clock::now();
#pragma omp parallel for schedule(dynamic, 1)
  for (std::size_t j = 0; j < bases.size(); ++j) {
#ifdef _OPENMP
    const int tid = omp_get_thread_num();
#else
    const int tid = 0;
#endif
    WickEvaluator evaluator;
    base_values[j] = evaluator.run(bases[j].second, &thread_memos[tid]);
    ++completed;
  }
  const auto wick_stop = std::chrono::steady_clock::now();

  PeelingRecursion recursion;
  for (std::size_t j = 0; j < bases.size(); ++j)
    recursion.wick_memo.emplace(bases[j].first, base_values[j]);

  std::cout << "discovered_states=" << discovery.seen.size()
            << " unique_bases=" << bases.size()
            << " discovery_seconds="
            << std::chrono::duration<double>(discovery_stop - discovery_start).count()
            << " wick_seconds="
            << std::chrono::duration<double>(wick_stop - wick_start).count()
            << " threads=" << thread_count << "\n";
  std::cout << "states_by_remaining_order:";
  for (auto [k, count] : discovery.states_by_remaining_order)
    std::cout << " [" << k << ':' << count << ']';
  std::cout << "\nbase_counts_by_edge_pairs:";
  std::map<int, std::size_t> bases_by_pairs;
  for (const auto &item : bases) ++bases_by_pairs[item.second.edges.size() / 2];
  for (auto [p, count] : bases_by_pairs)
    std::cout << " [" << p << ':' << count << ']';
  std::cout << "\n";

  for (int k = 0; k <= max_order; ++k) {
    const auto start = std::chrono::steady_clock::now();
    const cpp_int z = recursion.value(root, k, true);
    const auto stop = std::chrono::steady_clock::now();
    std::cout << "D^" << k << " f = " << z << "\n";
    if (k > 0) {
      std::cout << "  root hits: a=" << recursion.root_by_a_hit[k]
                << " h=" << recursion.root_by_h_hit[k]
                << " W=" << recursion.root_by_w_hit[k] << "\n";
    }
    std::cout << "  numeric_seconds="
              << std::chrono::duration<double>(stop - start).count()
              << " value_cache=" << recursion.value_memo.size() << "\n";
  }
}

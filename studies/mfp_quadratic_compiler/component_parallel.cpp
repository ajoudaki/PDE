// Parallel exact evaluator for the connected-component peeling recurrence.
//
// Build this file after component_recursion.cpp.  It deliberately reuses the
// audited Tree, WickEvaluator, and PeelingRecursion definitions, but renames
// their serial main function.  Phase 1 discovers all A_0 trees symbolically;
// phase 2 computes their exact Wick values independently in parallel; phase 3
// reruns the cheap connected recurrence using the prefilled cache.

#define main component_recursion_serial_main
#include "component_recursion.cpp"
#undef main

#include <mutex>
#include <fstream>
#include <filesystem>
#ifdef _OPENMP
#include <omp.h>
#endif

struct DiscoveryRecursion {
  std::unordered_map<std::string, unsigned char> seen;
  std::unordered_map<std::string, Tree> bases;

  std::string key(const Tree &t, int k) {
    std::string out;
    out.push_back(static_cast<char>(k));
    out += canonical_key(t);
    return out;
  }

  void visit(const Tree &t, int k) {
    int degree_parity = static_cast<int>(t.edges.size()) +
                        std::accumulate(t.a.begin(), t.a.end(), 0);
    if ((degree_parity + k) & 1) return;
    if (t.edges.size() & 1) return;
    std::string memo_key = key(t, k);
    if (!seen.emplace(std::move(memo_key), 1).second) return;
    if (k == 0) {
      bases.try_emplace(canonical_key(t), t);
      return;
    }

    for (size_t u = 0; u < t.a.size(); ++u) if (t.a[u]) {
      Tree child = t;
      --child.a[u];
      unsigned char v0 = static_cast<unsigned char>(child.h.size());
      child.h.push_back(1); child.h.push_back(1);
      child.edges.push_back({static_cast<unsigned char>(u), v0});
      child.edges.push_back({static_cast<unsigned char>(u),
                             static_cast<unsigned char>(v0 + 1)});
      visit(child, k - 1);
    }
    for (size_t v = 0; v < t.h.size(); ++v) if (t.h[v]) {
      Tree child = t;
      unsigned char u0 = static_cast<unsigned char>(child.a.size());
      unsigned char v1 = static_cast<unsigned char>(child.h.size());
      child.a.push_back(1); child.h.push_back(1);
      child.edges.push_back({u0, static_cast<unsigned char>(v)});
      child.edges.push_back({u0, v1});
      visit(child, k - 1);
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
      for (int q = 0; q <= k - 1; ++q) {
        visit(children[0], q);
        visit(children[1], k - 1 - q);
      }
    }
  }
};

int main(int argc, char **argv) {
  int max_order = argc > 1 ? std::stoi(argv[1]) : 13;
  std::string checkpoint = argc > 2 ? argv[2] : "";
  Tree root;
  root.a = {1}; root.h = {1, 1}; root.edges = {{0, 0}, {0, 1}};

  auto start = std::chrono::steady_clock::now();
  DiscoveryRecursion discovery;
  for (int k = 0; k <= max_order; ++k) discovery.visit(root, k);
  auto discovered = std::chrono::steady_clock::now();
  std::cout << "discovered states=" << discovery.seen.size()
            << " base_trees=" << discovery.bases.size()
            << " seconds="
            << std::chrono::duration<double>(discovered - start).count()
            << "\n";

  std::vector<std::pair<std::string, Tree>> jobs;
  jobs.reserve(discovery.bases.size());
  for (auto &[key, tree] : discovery.bases)
    jobs.push_back({key, std::move(tree)});
  std::sort(jobs.begin(), jobs.end(),
            [](const auto &x, const auto &y) { return x.first < y.first; });
  std::vector<cpp_int> values(jobs.size());

  size_t resume_index = 0;
  if (!checkpoint.empty()) {
    std::ifstream in(checkpoint);
    std::string decimal;
    while (resume_index < values.size() && (in >> decimal)) {
      cpp_int value = 0;
      for (char digit : decimal) value = value * 10 + (digit - '0');
      values[resume_index++] = value;
    }
    std::cout << "resumed contracted values=" << resume_index << "\n";
  }

  // Checkpoint in moderate batches.  Each batch is an exact independent list
  // of connected Wick contractions, so interruption never corrupts completed
  // work and ordering is deterministic after sorting the canonical keys.
  const size_t batch = 4096;
  for (size_t begin = resume_index; begin < jobs.size(); begin += batch) {
    size_t end = std::min(jobs.size(), begin + batch);
#pragma omp parallel for schedule(dynamic, 1)
    for (size_t q = begin; q < end; ++q) {
      WickEvaluator evaluator;
      values[q] = evaluator.run(jobs[q].second);
    }
    if (!checkpoint.empty()) {
      // Replace atomically: a crash can leave the previous complete batch or
      // the new complete batch, never a partially rewritten checkpoint.
      std::string temporary = checkpoint + ".tmp";
      std::ofstream out(temporary);
      for (size_t q = 0; q < end; ++q) out << values[q] << '\n';
      out.close();
      std::filesystem::rename(temporary, checkpoint);
    }
    std::cout << "contracted " << end << '/' << jobs.size() << "\n";
  }
  auto contracted = std::chrono::steady_clock::now();
  std::cout << "contracted base trees seconds="
            << std::chrono::duration<double>(contracted - discovered).count()
            << "\n";

  PeelingRecursion recursion;
  recursion.wick_memo.reserve(jobs.size() * 2);
  for (size_t q = 0; q < jobs.size(); ++q)
    recursion.wick_memo.emplace(std::move(jobs[q].first), values[q]);
  for (int k = 0; k <= max_order; ++k) {
    auto t0 = std::chrono::steady_clock::now();
    cpp_int value = recursion.value(root, k, true);
    auto t1 = std::chrono::steady_clock::now();
    std::cout << "D^" << k << " f = " << value << "\n";
    if (k > 0)
      std::cout << "  root hits: a=" << recursion.root_by_a_hit[k]
                << " h=" << recursion.root_by_h_hit[k]
                << " W=" << recursion.root_by_w_hit[k] << "\n";
    std::cout << "  reconstruction_seconds="
              << std::chrono::duration<double>(t1 - t0).count() << "\n";
  }
  return 0;
}

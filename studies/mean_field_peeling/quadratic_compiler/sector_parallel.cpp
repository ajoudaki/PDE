// Checkpointed parallel driver for the exact W-hit-graded connected peeling
// recurrence.  The included source contains the checked_uint512_t arithmetic,
// canonical tree representation, exact sector recurrence, and audited Wick
// prunes.  This driver separates dependency discovery, independent base Wick
// contractions, and cheap reconstruction.
#define main component_sector_serial_main
#include "sector_engine_checked.cpp"
#undef main

#include <atomic>
#include <filesystem>
#include <fstream>
#include <mutex>
#include <unordered_set>

#ifdef _OPENMP
#include <omp.h>
#endif
struct SectorDiscovery {
  std::unordered_set<std::string> seen;
  std::unordered_map<std::string, Tree> bases;
  std::map<std::pair<int, int>, size_t> states_by_kw;

  static std::string state_key(const Tree &t, int k, int w) {
    std::string key;
    key.push_back(static_cast<char>(k));
    key.push_back(static_cast<char>(w));
    key += canonical_key(t);
    return key;
  }

  void visit(const Tree &t, int k, int w) {
    if (w < 0 || w > k || (t.edges.size() & 1)) return;
    int parity = static_cast<int>(t.edges.size()) +
                 std::accumulate(t.a.begin(), t.a.end(), 0);
    if ((parity + k) & 1) return;
    if (!seen.emplace(state_key(t, k, w)).second) return;
    ++states_by_kw[{k, w}];
    if (k == 0) {
      if (w == 0) bases.try_emplace(canonical_key(t), t);
      return;
    }

    for (size_t u = 0; u < t.a.size(); ++u) if (t.a[u]) {
      Tree child = t;
      --child.a[u];
      auto v0 = static_cast<unsigned char>(child.h.size());
      child.h.push_back(1); child.h.push_back(1);
      child.edges.push_back({static_cast<unsigned char>(u), v0});
      child.edges.push_back({static_cast<unsigned char>(u),
                             static_cast<unsigned char>(v0 + 1)});
      visit(child, k - 1, w);
    }
    for (size_t v = 0; v < t.h.size(); ++v) if (t.h[v]) {
      Tree child = t;
      auto u0 = static_cast<unsigned char>(child.a.size());
      auto v1 = static_cast<unsigned char>(child.h.size());
      child.a.push_back(1); child.h.push_back(1);
      child.edges.push_back({u0, static_cast<unsigned char>(v)});
      child.edges.push_back({u0, v1});
      visit(child, k - 1, w);
    }
    if (w == 0) return;
    for (size_t e = 0; e < t.edges.size(); ++e) {
      Tree forest = t;
      auto [u, v] = forest.edges[e];
      ++forest.a[u]; ++forest.h[v];
      auto fresh = static_cast<unsigned char>(forest.h.size());
      forest.h.push_back(1);
      forest.edges.erase(forest.edges.begin() + e);
      forest.edges.push_back({u, fresh});
      auto children = split_components(forest);
      if (children.size() != 2) std::abort();
      for (int q = 0; q <= k - 1; ++q)
        for (int s = 0; s <= w - 1; ++s) {
          visit(children[0], q, s);
          visit(children[1], k - 1 - q, w - 1 - s);
        }
    }
  }
};

static cpp_int parse_checked(const std::string &decimal) {
  cpp_int value = 0;
  for (char digit : decimal) value = value * 10 + (digit - '0');
  return value;
}

#ifndef COMPONENT_SECTOR_NO_MAIN
int main(int argc, char **argv) {
  int order = argc > 1 ? std::stoi(argv[1]) : 9;
  int min_w = argc > 2 ? std::stoi(argv[2]) : 0;
  int max_w = argc > 3 ? std::stoi(argv[3]) : min_w;
  std::string checkpoint = argc > 4 ? argv[4] : "";
  int evaluator_mode = argc > 5 ? std::stoi(argv[5]) : 0;
  // evaluator_mode: 0=audited multiplicity recursion, 1=labelled recursion,
  // 2=hybrid (labelled at >=16 edges), 3=vertex-partition recursion,
  // 4=structural portfolio (partition while its enumerated side has <=11
  // vertices, otherwise multiplicity recursion).

  Tree root;
  root.a = {1}; root.h = {1, 1}; root.edges = {{0, 0}, {0, 1}};
  auto start = std::chrono::steady_clock::now();
  SectorDiscovery discovery;
  for (int w = min_w; w <= max_w; ++w) discovery.visit(root, order, w);
  auto discovered = std::chrono::steady_clock::now();

  std::vector<std::pair<std::string, Tree>> jobs;
  jobs.reserve(discovery.bases.size());
  for (auto &[key, tree] : discovery.bases) jobs.push_back({key, tree});
  std::sort(jobs.begin(), jobs.end(),
            [](const auto &x, const auto &y) { return x.first < y.first; });
  std::vector<cpp_int> values(jobs.size());
  size_t resume = 0;
  if (!checkpoint.empty()) {
    std::ifstream in(checkpoint);
    std::string decimal;
    while (resume < values.size() && in >> decimal)
      values[resume++] = parse_checked(decimal);
  }

  std::cout << "discovered_states=" << discovery.seen.size()
            << " unique_bases=" << jobs.size()
            << " discovery_seconds="
            << std::chrono::duration<double>(discovered - start).count()
            << " resumed=" << resume << '\n' << std::flush;
  std::map<int, size_t> bases_by_pairs;
  for (const auto &job : jobs) ++bases_by_pairs[job.second.edges.size() / 2];
  std::cout << "bases_by_pairs:";
  for (auto [pairs, count] : bases_by_pairs)
    std::cout << " [" << pairs << ':' << count << ']';
  std::cout << '\n' << std::flush;

#ifdef _OPENMP
  int threads = omp_get_max_threads();
#else
  int threads = 1;
#endif
  std::vector<std::unordered_map<std::string, cpp_int>> thread_memos(threads);
  // Small batches bound lost work when one high-order contraction has an
  // unusually long tail; checkpoint rewrites are tiny relative to Wick work.
  const size_t batch = 32;
  for (size_t begin = resume; begin < jobs.size(); begin += batch) {
    size_t end = std::min(jobs.size(), begin + batch);
#pragma omp parallel for schedule(dynamic, 1)
    for (size_t q = begin; q < end; ++q) {
#ifdef _OPENMP
      int tid = omp_get_thread_num();
#else
      int tid = 0;
#endif
      if (evaluator_mode == 3 ||
          (evaluator_mode == 4 &&
           std::min(jobs[q].second.a.size(), jobs[q].second.h.size()) <= 11)) {
        values[q] = VertexPartitionWickEvaluator(jobs[q].second).run();
      } else if (evaluator_mode == 1 ||
          (evaluator_mode == 2 && jobs[q].second.edges.size() >= 16)) {
        values[q] = LabelledWickEvaluator(jobs[q].second).run();
      } else {
        WickEvaluator evaluator;
        values[q] = evaluator.run(jobs[q].second, &thread_memos[tid]);
      }
    }
    if (!checkpoint.empty()) {
      std::string temporary = checkpoint + ".tmp";
      std::ofstream out(temporary);
      for (size_t q = 0; q < end; ++q) out << values[q] << '\n';
      out.close();
      std::filesystem::rename(temporary, checkpoint);
    }
    std::cout << "contracted=" << end << '/' << jobs.size() << '\n'
              << std::flush;
  }

  PeelingRecursion recursion;
  recursion.wick_memo.reserve(jobs.size() * 2);
  for (size_t q = 0; q < jobs.size(); ++q)
    recursion.wick_memo.emplace(jobs[q].first, values[q]);
  for (int w = min_w; w <= max_w; ++w) {
    auto t0 = std::chrono::steady_clock::now();
    cpp_int value = recursion.value(root, order, w, true);
    auto t1 = std::chrono::steady_clock::now();
    std::cout << "D^" << order << " P=" << (order + 1 - w)
              << " (W_hits=" << w << ") = " << value << '\n'
              << "  reconstruction_seconds="
              << std::chrono::duration<double>(t1 - t0).count() << '\n'
              << std::flush;
  }
  auto stop = std::chrono::steady_clock::now();
  std::cout << "total_seconds="
            << std::chrono::duration<double>(stop - start).count()
            << " threads=" << threads << '\n';
  return 0;
}
#endif

#define COMPONENT_SECTOR_NO_MAIN
#include "sector_parallel.cpp"
#define MATROID_WICK_ENGINE_ALREADY_INCLUDED
#include "matroid_wick_evaluator.cpp"

int main(int argc, char **argv) {
  int order = argc > 1 ? std::stoi(argv[1]) : 9;
  int min_w = argc > 2 ? std::stoi(argv[2]) : 0;
  int max_w = argc > 3 ? std::stoi(argv[3]) : min_w;
  Tree root;
  root.a = {1}; root.h = {1, 1}; root.edges = {{0, 0}, {0, 1}};
  SectorDiscovery discovery;
  for (int w = min_w; w <= max_w; ++w) discovery.visit(root, order, w);
  std::vector<std::pair<std::string, Tree>> jobs;
  for (auto &entry : discovery.bases) jobs.push_back(entry);
  std::sort(jobs.begin(), jobs.end(),
            [](auto &a, auto &b) { return a.first < b.first; });
  std::vector<cpp_int> values(jobs.size());
#pragma omp parallel for schedule(dynamic, 1)
  for (size_t q = 0; q < jobs.size(); ++q)
    values[q] = MatroidWickEvaluator(jobs[q].second).run();
  PeelingRecursion recursion;
  recursion.wick_memo.reserve(jobs.size() * 2);
  for (size_t q = 0; q < jobs.size(); ++q)
    recursion.wick_memo.emplace(jobs[q].first, values[q]);
  for (int w = min_w; w <= max_w; ++w)
    std::cout << "P=" << order + 1 - w << ' '
              << recursion.value(root, order, w, true) << '\n';
}

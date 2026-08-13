// Sparse, canonical-keyed checkpoint driver for a target W-hit sector.
// It imports a completed (or partial) values-only checkpoint from a source
// sector, so every shared base contraction is reused exactly.
#define COMPONENT_SECTOR_NO_MAIN
#include "sector_parallel.cpp"

#include <sstream>

static std::vector<std::pair<std::string, Tree>> sorted_jobs(
    const SectorDiscovery &discovery) {
  std::vector<std::pair<std::string, Tree>> jobs;
  jobs.reserve(discovery.bases.size());
  for (const auto &[key, tree] : discovery.bases) jobs.push_back({key, tree});
  std::sort(jobs.begin(), jobs.end(),
            [](const auto &x, const auto &y) { return x.first < y.first; });
  return jobs;
}
static std::string hex_key(const std::string &key) {
  static constexpr char digit[] = "0123456789abcdef";
  std::string out;
  out.reserve(2 * key.size());
  for (unsigned char c : key) {
    out.push_back(digit[c >> 4]);
    out.push_back(digit[c & 15]);
  }
  return out;
}

static int hex_digit(char c) {
  if (c >= '0' && c <= '9') return c - '0';
  if (c >= 'a' && c <= 'f') return c - 'a' + 10;
  if (c >= 'A' && c <= 'F') return c - 'A' + 10;
  return -1;
}

static bool unhex_key(const std::string &hex, std::string &key) {
  if (hex.size() & 1) return false;
  key.clear();
  key.reserve(hex.size() / 2);
  for (size_t q = 0; q < hex.size(); q += 2) {
    int high = hex_digit(hex[q]), low = hex_digit(hex[q + 1]);
    if (high < 0 || low < 0) return false;
    key.push_back(static_cast<char>(16 * high + low));
  }
  return true;
}

int main(int argc, char **argv) {
  if (argc < 7) {
    std::cerr << "usage: ORDER SOURCE_W SOURCE_VALUES TARGET_W "
                 "SPARSE_KEY_VALUES MODE [TARGET_PREFIX_VALUES]\n";
    return 2;
  }
  int order = std::stoi(argv[1]);
  int source_w = std::stoi(argv[2]);
  std::string source_checkpoint = argv[3];
  int target_w = std::stoi(argv[4]);
  std::string sparse_checkpoint = argv[5];
  int evaluator_mode = std::stoi(argv[6]);
  std::string target_prefix = argc > 7 ? argv[7] : "";

  Tree root;
  root.a = {1}; root.h = {1, 1}; root.edges = {{0, 0}, {0, 1}};
  SectorDiscovery source_discovery, target_discovery;
  source_discovery.visit(root, order, source_w);
  target_discovery.visit(root, order, target_w);
  auto source_jobs = sorted_jobs(source_discovery);
  auto target_jobs = sorted_jobs(target_discovery);

  std::unordered_map<std::string, size_t> target_index;
  target_index.reserve(2 * target_jobs.size());
  for (size_t q = 0; q < target_jobs.size(); ++q)
    target_index.emplace(target_jobs[q].first, q);
  std::vector<cpp_int> values(target_jobs.size());
  std::vector<unsigned char> done(target_jobs.size(), 0);

  size_t source_values = 0, reused = 0;
  {
    std::ifstream in(source_checkpoint);
    std::string decimal;
    while (source_values < source_jobs.size() && in >> decimal) {
      auto found = target_index.find(source_jobs[source_values].first);
      if (found != target_index.end() && !done[found->second]) {
        values[found->second] = parse_checked(decimal);
        done[found->second] = 1;
        ++reused;
      }
      ++source_values;
    }
  }

  // Optionally import an existing ordinary prefix checkpoint for the target
  // sector.  Its position is meaningful only against this same sorted target
  // job list; future progress is stored by canonical key instead.
  size_t imported_prefix = 0;
  if (!target_prefix.empty()) {
    std::ifstream in(target_prefix);
    std::string decimal;
    while (imported_prefix < target_jobs.size() && in >> decimal) {
      values[imported_prefix] = parse_checked(decimal);
      done[imported_prefix] = 1;
      ++imported_prefix;
    }
  }

  // Sparse lines are `hex(canonical_key) decimal_value`.  Malformed/torn
  // lines are ignored; duplicate keys are harmless and the latest exact
  // value simply overwrites the same slot.
  size_t sparse_loaded = 0;
  {
    std::ifstream in(sparse_checkpoint);
    std::string line;
    while (std::getline(in, line)) {
      std::istringstream fields(line);
      std::string hex, decimal, extra, key;
      if (!(fields >> hex >> decimal) || (fields >> extra) ||
          !unhex_key(hex, key)) continue;
      auto found = target_index.find(key);
      if (found == target_index.end()) continue;
      values[found->second] = parse_checked(decimal);
      done[found->second] = 1;
      ++sparse_loaded;
    }
  }

  std::vector<size_t> unknown;
  for (size_t q = 0; q < target_jobs.size(); ++q)
    if (!done[q]) unknown.push_back(q);
  std::cout << "source_jobs=" << source_jobs.size()
            << " source_values=" << source_values
            << " target_jobs=" << target_jobs.size()
            << " reused=" << reused
            << " imported_prefix=" << imported_prefix
            << " sparse_lines=" << sparse_loaded
            << " unknown=" << unknown.size() << '\n' << std::flush;

#ifdef _OPENMP
  int threads = omp_get_max_threads();
#else
  int threads = 1;
#endif
  std::vector<std::unordered_map<std::string, cpp_int>> thread_memos(threads);
  std::ofstream checkpoint_out(sparse_checkpoint, std::ios::app);
  // Separate any torn prior final line before appending new complete records.
  checkpoint_out << '\n';
  checkpoint_out.flush();
  constexpr size_t batch = 32;
  for (size_t begin = 0; begin < unknown.size(); begin += batch) {
    size_t end = std::min(unknown.size(), begin + batch);
#pragma omp parallel for schedule(dynamic, 1)
    for (size_t z = begin; z < end; ++z) {
      size_t q = unknown[z];
#ifdef _OPENMP
      int tid = omp_get_thread_num();
#else
      int tid = 0;
#endif
      if (evaluator_mode == 3 ||
          (evaluator_mode == 4 &&
           std::min(target_jobs[q].second.a.size(),
                    target_jobs[q].second.h.size()) <= 11)) {
        values[q] = VertexPartitionWickEvaluator(target_jobs[q].second).run();
      } else if (evaluator_mode == 1 ||
                 (evaluator_mode == 2 &&
                  target_jobs[q].second.edges.size() >= 16)) {
        values[q] = LabelledWickEvaluator(target_jobs[q].second).run();
      } else {
        WickEvaluator evaluator;
        values[q] = evaluator.run(target_jobs[q].second, &thread_memos[tid]);
      }
    }
    for (size_t z = begin; z < end; ++z) {
      size_t q = unknown[z];
      done[q] = 1;
      checkpoint_out << hex_key(target_jobs[q].first) << ' '
                     << values[q] << '\n';
    }
    checkpoint_out.flush();
    std::cout << "computed=" << end << '/' << unknown.size()
              << " complete="
              << std::count(done.begin(), done.end(), static_cast<unsigned char>(1))
              << '/' << target_jobs.size() << '\n' << std::flush;
  }

  if (std::find(done.begin(), done.end(), 0) != done.end()) return 3;
  PeelingRecursion recursion;
  recursion.wick_memo.reserve(2 * target_jobs.size());
  for (size_t q = 0; q < target_jobs.size(); ++q)
    recursion.wick_memo.emplace(target_jobs[q].first, values[q]);
  cpp_int answer = recursion.value(root, order, target_w, true);
  std::cout << "D^" << order << " P=" << (order + 1 - target_w)
            << " (W_hits=" << target_w << ") = " << answer << '\n'
            << "threads=" << threads << '\n';
}

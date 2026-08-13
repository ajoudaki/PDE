// One-process-per-sector exact evaluator for the Campaign 1 metric polynomial.
//
// The two monotone grades are the number of D_W hits and D_a hits.  At total
// derivative order k, the desired power of lambda in
// D_a + lambda(D_u + D_W) is k-D_a_hits.  Running each (D_W,D_a) sector in a
// fresh process makes the external 4 GB memory cap a genuine per-sector cap.
#define main accepted_sector_engine_main
#include "../sector_engine_checked.cpp"
#undef main

#include <sstream>
#include <stdexcept>

struct DoubleGradedRecursion {
  std::unordered_map<std::string, cpp_int> value_memo;
  std::unordered_map<std::string, cpp_int> wick_memo;
  std::unordered_map<std::string, cpp_int> wick_subproblem_memo;
  size_t completed_base_evaluations = 0;

  std::string key(const Tree &tree, int k, int w_hits, int a_hits) const {
    std::string out;
    out.push_back(static_cast<char>(k));
    out.push_back(static_cast<char>(w_hits));
    out.push_back(static_cast<char>(a_hits));
    out += canonical_key(tree);
    return out;
  }

  cpp_int base(const Tree &tree) {
    std::string base_key = canonical_key(tree);
    auto found = wick_memo.find(base_key);
    if (found != wick_memo.end()) return found->second;
    WickEvaluator evaluator;
    cpp_int ans = std::min(tree.a.size(), tree.h.size()) <= 11
        ? VertexPartitionWickEvaluator(tree).run()
        : evaluator.run(tree, &wick_subproblem_memo);
    wick_memo.emplace(std::move(base_key), ans);
    ++completed_base_evaluations;
    return ans;
  }

  cpp_int value(const Tree &tree, int k, int w_hits, int a_hits) {
    if (k < 0 || w_hits < 0 || a_hits < 0 || w_hits + a_hits > k)
      return 0;
    if (tree.edges.size() & 1) return 0;
    int parity = static_cast<int>(tree.edges.size()) +
                 std::accumulate(tree.a.begin(), tree.a.end(), 0);
    if ((parity + k) & 1) return 0;

    std::string memo_key = key(tree, k, w_hits, a_hits);
    auto found = value_memo.find(memo_key);
    if (found != value_memo.end()) return found->second;
    if (k == 0) {
      cpp_int ans = (w_hits == 0 && a_hits == 0) ? base(tree) : cpp_int(0);
      value_memo.emplace(std::move(memo_key), ans);
      return ans;
    }

    cpp_int ans = 0;

    if (a_hits > 0) {
      for (size_t u = 0; u < tree.a.size(); ++u) if (tree.a[u]) {
        Tree child = tree;
        unsigned multiplicity = child.a[u];
        --child.a[u];
        unsigned char v0 = static_cast<unsigned char>(child.h.size());
        child.h.push_back(1);
        child.h.push_back(1);
        child.edges.push_back({static_cast<unsigned char>(u), v0});
        child.edges.push_back({static_cast<unsigned char>(u),
                               static_cast<unsigned char>(v0 + 1)});
        ans += multiplicity * value(child, k - 1, w_hits, a_hits - 1);
      }
    }

    // A first-feature hit changes neither explicit grade.
    for (size_t v = 0; v < tree.h.size(); ++v) if (tree.h[v]) {
      Tree child = tree;
      unsigned multiplicity = 8 * child.h[v];
      unsigned char u0 = static_cast<unsigned char>(child.a.size());
      unsigned char v1 = static_cast<unsigned char>(child.h.size());
      child.a.push_back(1);
      child.h.push_back(1);
      child.edges.push_back({u0, static_cast<unsigned char>(v)});
      child.edges.push_back({u0, v1});
      ans += multiplicity * value(child, k - 1, w_hits, a_hits);
    }

    if (w_hits > 0) {
      for (size_t edge = 0; edge < tree.edges.size(); ++edge) {
        Tree forest = tree;
        auto [u, v] = forest.edges[edge];
        ++forest.a[u];
        ++forest.h[v];
        unsigned char fresh = static_cast<unsigned char>(forest.h.size());
        forest.h.push_back(1);
        forest.edges.erase(forest.edges.begin() + edge);
        forest.edges.push_back({u, fresh});
        auto children = split_components(forest);
        if (children.size() != 2)
          throw std::logic_error("W hit did not split a tree in two");

        cpp_int convolution = 0;
        for (int q = 0; q <= k - 1; ++q)
          for (int w0 = 0; w0 <= w_hits - 1; ++w0)
            for (int a0 = 0; a0 <= a_hits; ++a0)
              convolution += choose(k - 1, q)
                  * value(children[0], q, w0, a0)
                  * value(children[1], k - 1 - q,
                          w_hits - 1 - w0, a_hits - a0);
        ans += 2 * convolution;
      }
    }

    value_memo.emplace(std::move(memo_key), ans);
    return ans;
  }
};

static int integer_argument(const char *text, const std::string &name) {
  try {
    return std::stoi(text);
  } catch (...) {
    throw std::invalid_argument("invalid " + name);
  }
}

int main(int argc, char **argv) {
  try {
    if (argc != 5)
      throw std::invalid_argument(
          "usage: graded_sector ROOT ORDER W_HITS A_HITS");
    std::string root_name = argv[1];
    int order = integer_argument(argv[2], "order");
    int w_hits = integer_argument(argv[3], "W-hit count");
    int a_hits = integer_argument(argv[4], "a-hit count");
    if (order < 0 || order > 9 || w_hits < 0 || a_hits < 0 ||
        w_hits + a_hits > order)
      throw std::invalid_argument("sector is outside Campaign 1 safety caps");

    Tree root;
    if (root_name == "f") {
      root.a = {1};
      root.h = {1, 1};
      root.edges = {{0, 0}, {0, 1}};
    } else if (root_name == "q2") {
      root.a = {0};
      root.h = {1, 1};
      root.edges = {{0, 0}, {0, 1}};
    } else {
      throw std::invalid_argument("ROOT must be f or q2");
    }

    DoubleGradedRecursion recursion;
    auto start = std::chrono::steady_clock::now();
    cpp_int result = recursion.value(root, order, w_hits, a_hits);
    auto stop = std::chrono::steady_clock::now();
    std::cout << "{\"root\":\"" << root_name
              << "\",\"order\":" << order
              << ",\"w_hits\":" << w_hits
              << ",\"a_hits\":" << a_hits
              << ",\"lambda_degree\":" << order - a_hits
              << ",\"value\":\"" << result
              << "\",\"seconds\":"
              << std::chrono::duration<double>(stop - start).count()
              << ",\"value_cache\":" << recursion.value_memo.size()
              << ",\"wick_cache\":" << recursion.wick_memo.size()
              << ",\"wick_subproblem_cache\":"
              << recursion.wick_subproblem_memo.size()
              << ",\"parent_source_sha256\":"
              << "\"1931b628b25d2a7c018bc20a06d14aee6ee86ca702d8abcbec17e1ec719be260\"}"
              << std::endl;
    return 0;
  } catch (const std::exception &error) {
    std::cerr << "error: " << error.what() << '\n';
    return 2;
  }
}

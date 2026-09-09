// Exact connected-tree coefficient probe for beta=1.
//
// V(T,k,r) extracts [alpha^r] after k applications of
//     D_a + D_W + alpha D_u
// to a connected decorated tree T.  The tree representation, canonicalizer,
// checked uint512 arithmetic, Wick contraction, and leading-width recurrence
// are imported unchanged from the accepted quadratic compiler.
#define main accepted_sector_engine_main
#include "../../mean_field_peeling/quadratic_compiler/sector_engine_checked.cpp"
#undef main

#include <stdexcept>

struct AlphaGradedRecursion {
  std::unordered_map<std::string, cpp_int> value_memo;
  std::unordered_map<std::string, cpp_int> wick_memo;
  std::unordered_map<std::string, cpp_int> wick_subproblem_memo;

  std::string key(const Tree &tree, int k, int u_hits) const {
    std::string out;
    out.push_back(static_cast<char>(k));
    out.push_back(static_cast<char>(u_hits));
    out += canonical_key(tree);
    return out;
  }

  cpp_int base(const Tree &tree) {
    std::string base_key = canonical_key(tree);
    auto found = wick_memo.find(base_key);
    if (found != wick_memo.end()) return found->second;
    WickEvaluator evaluator;
    cpp_int answer = std::min(tree.a.size(), tree.h.size()) <= 11
        ? VertexPartitionWickEvaluator(tree).run()
        : evaluator.run(tree, &wick_subproblem_memo);
    wick_memo.emplace(std::move(base_key), answer);
    return answer;
  }

  cpp_int value(const Tree &tree, int k, int u_hits) {
    if (k < 0 || u_hits < 0 || u_hits > k) return 0;
    if (tree.edges.size() & 1) return 0;
    int parity = static_cast<int>(tree.edges.size())
        + std::accumulate(tree.a.begin(), tree.a.end(), 0);
    if ((parity + k) & 1) return 0;

    std::string memo_key = key(tree, k, u_hits);
    auto found = value_memo.find(memo_key);
    if (found != value_memo.end()) return found->second;
    if (k == 0) {
      cpp_int answer = u_hits == 0 ? base(tree) : cpp_int(0);
      value_memo.emplace(std::move(memo_key), answer);
      return answer;
    }

    cpp_int answer = 0;

    // D_a: alpha degree is unchanged.
    for (size_t u = 0; u < tree.a.size(); ++u) if (tree.a[u]) {
      Tree child = tree;
      unsigned multiplicity = child.a[u];
      --child.a[u];
      auto fresh = static_cast<unsigned char>(child.h.size());
      child.h.push_back(1);
      child.h.push_back(1);
      child.edges.push_back({static_cast<unsigned char>(u), fresh});
      child.edges.push_back(
          {static_cast<unsigned char>(u),
           static_cast<unsigned char>(fresh + 1)});
      answer += multiplicity * value(child, k - 1, u_hits);
    }

    // alpha D_u: consume one alpha degree.
    if (u_hits > 0) {
      for (size_t v = 0; v < tree.h.size(); ++v) if (tree.h[v]) {
        Tree child = tree;
        unsigned multiplicity = 8 * child.h[v];
        auto row = static_cast<unsigned char>(child.a.size());
        auto column = static_cast<unsigned char>(child.h.size());
        child.a.push_back(1);
        child.h.push_back(1);
        child.edges.push_back({row, static_cast<unsigned char>(v)});
        child.edges.push_back({row, column});
        answer += multiplicity * value(child, k - 1, u_hits - 1);
      }
    }

    // D_W: split the tree, then distribute both derivative order and alpha
    // degree by the exact Leibniz convolution.
    for (size_t edge = 0; edge < tree.edges.size(); ++edge) {
      Tree forest = tree;
      auto [u, v] = forest.edges[edge];
      ++forest.a[u];
      ++forest.h[v];
      auto fresh = static_cast<unsigned char>(forest.h.size());
      forest.h.push_back(1);
      forest.edges.erase(forest.edges.begin() + edge);
      forest.edges.push_back({u, fresh});
      auto children = split_components(forest);
      if (children.size() != 2)
        throw std::logic_error("W hit did not split a tree in two");
      cpp_int convolution = 0;
      for (int q = 0; q <= k - 1; ++q)
        for (int r0 = 0; r0 <= u_hits; ++r0)
          convolution += choose(k - 1, q)
              * value(children[0], q, r0)
              * value(children[1], k - 1 - q, u_hits - r0);
      answer += 2 * convolution;
    }

    value_memo.emplace(std::move(memo_key), answer);
    return answer;
  }
};

int main(int argc, char **argv) {
  try {
    if (argc != 3)
      throw std::invalid_argument(
          "usage: alpha_connected_sector_probe ORDER ALPHA_POWER");
    int order = std::stoi(argv[1]);
    int alpha_power = std::stoi(argv[2]);
    if (order < 0 || order > 13 || alpha_power < 0 || alpha_power > order)
      throw std::invalid_argument("outside the fixed order-13 probe cap");

    Tree root;
    root.a = {1};
    root.h = {1, 1};
    root.edges = {{0, 0}, {0, 1}};
    AlphaGradedRecursion recursion;
    auto start = std::chrono::steady_clock::now();
    cpp_int answer = recursion.value(root, order, alpha_power);
    auto stop = std::chrono::steady_clock::now();
    std::cout << "{\"order\":" << order
              << ",\"alpha_power\":" << alpha_power
              << ",\"value\":\"" << answer
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

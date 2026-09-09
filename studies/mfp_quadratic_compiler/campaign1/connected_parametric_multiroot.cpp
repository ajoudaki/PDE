// Exact connected-recursion compiler for Campaign 1.
//
// The accepted scalar tree representation, canonicalizer, component splitter,
// and Wick evaluator are included verbatim.  The default is the checked
// portfolio evaluator in sector_engine_checked.cpp.  Defining
// CAMPAIGN1_DENSE_PRIMARY_PARENT rebuilds the historical dense run against
// component_recursion.cpp; neither accepted parent is modified.
#define main accepted_component_recursion_main
#ifdef CAMPAIGN1_DENSE_PRIMARY_PARENT
#include "../component_recursion.cpp"
#else
#include "../sector_engine_checked.cpp"
#endif
#undef main

#include <array>
#include <fstream>
#include <sstream>
#include <stdexcept>

using Poly = std::vector<cpp_int>;

static void trim_poly(Poly &p) {
  while (p.size() > 1 && p.back() == 0) p.pop_back();
  if (p.empty()) p.push_back(0);
}

static bool zero_poly(const Poly &p) {
  return p.empty() || (p.size() == 1 && p[0] == 0);
}

static void add_scaled_shift(Poly &dst, const Poly &src,
                             const cpp_int &scale, int shift) {
  if (shift < 0) throw std::invalid_argument("negative lambda exponent");
  if (scale == 0 || zero_poly(src)) return;
  if (dst.size() < src.size() + static_cast<size_t>(shift))
    dst.resize(src.size() + static_cast<size_t>(shift), 0);
  for (size_t i = 0; i < src.size(); ++i)
    dst[i + static_cast<size_t>(shift)] += scale * src[i];
  trim_poly(dst);
}

static Poly multiply_poly(const Poly &left, const Poly &right) {
  if (zero_poly(left) || zero_poly(right)) return Poly{0};
  Poly out(left.size() + right.size() - 1, 0);
  for (size_t i = 0; i < left.size(); ++i)
    for (size_t j = 0; j < right.size(); ++j)
      out[i + j] += left[i] * right[j];
  trim_poly(out);
  return out;
}

static cpp_int evaluate_poly(const Poly &p, unsigned value) {
  cpp_int ans = 0;
  for (auto it = p.rbegin(); it != p.rend(); ++it)
    ans = ans * value + *it;
  return ans;
}

static std::string integer_string(const cpp_int &z) {
  std::ostringstream out;
  out << z;
  return out.str();
}

static std::string json_poly(const Poly &p) {
  std::ostringstream out;
  out << '[';
  for (size_t i = 0; i < p.size(); ++i) {
    if (i) out << ',';
    out << '"' << p[i] << '"';
  }
  out << ']';
  return out.str();
}

struct MetricExponents {
  int a = 0;
  int u = 1;
  int w = 1;
};

struct ParametricPeelingRecursion {
  MetricExponents exponents;
  std::unordered_map<std::string, Poly> value_memo;
  std::unordered_map<std::string, cpp_int> wick_memo;
#ifndef CAMPAIGN1_DENSE_PRIMARY_PARENT
  std::unordered_map<std::string, cpp_int> wick_subproblem_memo;
#endif
  std::map<int, size_t> calls_by_order;
  std::map<int, size_t> misses_by_order;
  size_t completed_base_evaluations = 0;

  explicit ParametricPeelingRecursion(MetricExponents exponents0)
      : exponents(exponents0) {
    if (exponents.a < 0 || exponents.u < 0 || exponents.w < 0)
      throw std::invalid_argument("metric exponents must be nonnegative");
  }

  std::string value_key(const Tree &tree, int k) const {
    std::string key;
    key.push_back(static_cast<char>(k));
    key += canonical_key(tree);
    return key;
  }

  cpp_int base(const Tree &tree) {
    std::string key = canonical_key(tree);
    auto found = wick_memo.find(key);
    if (found != wick_memo.end()) return found->second;
    WickEvaluator evaluator;
#ifdef CAMPAIGN1_DENSE_PRIMARY_PARENT
    cpp_int ans = evaluator.run(tree);
#else
    cpp_int ans = std::min(tree.a.size(), tree.h.size()) <= 11
        ? VertexPartitionWickEvaluator(tree).run()
        : evaluator.run(tree, &wick_subproblem_memo);
#endif
    wick_memo.emplace(std::move(key), ans);
    ++completed_base_evaluations;
    if (completed_base_evaluations % 10000 == 0)
      std::cerr << "completed base contractions="
                << completed_base_evaluations
                << " value_cache=" << value_memo.size() << '\n';
    return ans;
  }

  Poly value(const Tree &tree, int k) {
    ++calls_by_order[k];
    if (tree.edges.size() & 1) return Poly{0};
    int parity = static_cast<int>(tree.edges.size()) +
                 std::accumulate(tree.a.begin(), tree.a.end(), 0);
    if ((parity + k) & 1) return Poly{0};

    std::string key = value_key(tree, k);
    auto found = value_memo.find(key);
    if (found != value_memo.end()) return found->second;
    ++misses_by_order[k];
    if (k == 0) {
      Poly ans{base(tree)};
      value_memo.emplace(std::move(key), ans);
      return ans;
    }

    Poly ans{0};

    // D_a: d(a_u^p)/ds = p a_u^(p-1) z_u^2.
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
      add_scaled_shift(ans, value(child, k - 1), multiplicity, exponents.a);
    }

    // D_u: d(u_v^(2p))/ds = 8p times a fresh row wedge at v.
    for (size_t v = 0; v < tree.h.size(); ++v) if (tree.h[v]) {
      Tree child = tree;
      unsigned multiplicity = 8 * child.h[v];
      unsigned char u0 = static_cast<unsigned char>(child.a.size());
      unsigned char v1 = static_cast<unsigned char>(child.h.size());
      child.a.push_back(1);
      child.h.push_back(1);
      child.edges.push_back({u0, static_cast<unsigned char>(v)});
      child.edges.push_back({u0, v1});
      add_scaled_shift(ans, value(child, k - 1), multiplicity, exponents.u);
    }

    // D_W: remove one bridge, split, and distribute the remaining k-1 hits.
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

      Poly convolution{0};
      for (int q = 0; q <= k - 1; ++q) {
        Poly product = multiply_poly(value(children[0], q),
                                     value(children[1], k - 1 - q));
        add_scaled_shift(convolution, product, choose(k - 1, q), 0);
      }
      add_scaled_shift(ans, convolution, 2, exponents.w);
    }

    trim_poly(ans);
    value_memo.emplace(std::move(key), ans);
    return ans;
  }
};

struct ObservableRun {
  std::string name;
  std::vector<Poly> jets;
  double seconds = 0.0;
  size_t cache_before = 0;
  size_t cache_after = 0;
};

static ObservableRun evaluate_root(ParametricPeelingRecursion &recursion,
                                   const std::string &name,
                                   const Tree &root, int max_order) {
  ObservableRun result;
  result.name = name;
  result.cache_before = recursion.value_memo.size();
  auto start = std::chrono::steady_clock::now();
  for (int k = 0; k <= max_order; ++k) {
    auto one_start = std::chrono::steady_clock::now();
    result.jets.push_back(recursion.value(root, k));
    auto one_stop = std::chrono::steady_clock::now();
    std::cerr << name << " order=" << k
              << " coefficients=" << result.jets.back().size()
              << " seconds="
              << std::chrono::duration<double>(one_stop - one_start).count()
              << " value_cache=" << recursion.value_memo.size()
              << " wick_cache=" << recursion.wick_memo.size() << '\n';
  }
  auto stop = std::chrono::steady_clock::now();
  result.seconds = std::chrono::duration<double>(stop - start).count();
  result.cache_after = recursion.value_memo.size();
  return result;
}

static void require_equal(const cpp_int &actual, const cpp_int &expected,
                          const std::string &message) {
  if (actual != expected) {
    std::ostringstream error;
    error << message << ": expected " << expected << ", got " << actual;
    throw std::runtime_error(error.str());
  }
}

static void require_zero(const Poly &actual, const std::string &message) {
  if (!zero_poly(actual))
    throw std::runtime_error(message + ": polynomial is nonzero");
}

static void audit(const ObservableRun &f, const ObservableRun &q1,
                  const ObservableRun &q2, const MetricExponents &exponents) {
  const std::array<std::pair<int, cpp_int>, 5> accepted{{
      {1, cpp_int(111)},
      {3, cpp_int(1685184)},
      {5, cpp_int(77400633120ULL)},
      {7, cpp_int("7315868433079296")},
      {9, cpp_int("1181161141825400561664")},
  }};
  for (const auto &[order, expected] : accepted)
    if (order < static_cast<int>(f.jets.size()))
      require_equal(evaluate_poly(f.jets[order], 1), expected,
                    "canonical output regression order " +
                    std::to_string(order));

  for (size_t order = 0; order < f.jets.size(); order += 2)
    require_zero(f.jets[order], "output parity order " +
                                  std::to_string(order));
  for (size_t order = 1; order < q1.jets.size(); order += 2)
    require_zero(q1.jets[order], "Q1 parity order " +
                                   std::to_string(order));
  for (size_t order = 1; order < q2.jets.size(); order += 2)
    require_zero(q2.jets[order], "Q2 parity order " +
                                   std::to_string(order));

  require_equal(evaluate_poly(q1.jets[0], 1), 1, "Q1 initial value");
  require_equal(evaluate_poly(q2.jets[0], 1), 3, "Q2 initial value");
  if (exponents.a == 0 && exponents.u == 1 && exponents.w == 1) {
    require_equal(evaluate_poly(f.jets[1], 0), 27,
                  "readout-only output speed");
    if (f.jets.size() > 3)
      require_equal(evaluate_poly(f.jets[3], 0), 0,
                    "readout-only linearity");
    for (size_t order = 1;
         order < q1.jets.size() && order - 1 < f.jets.size(); ++order) {
      Poly expected{0};
      add_scaled_shift(expected, f.jets[order - 1], 8, 1);
      if (q1.jets[order] != expected)
        throw std::runtime_error("Q1 Euler identity failed at order " +
                                 std::to_string(order));
    }
  }

  if (q2.jets.size() > 4) {
    const Poly expected2{0, 2916, 9456};
    const Poly expected4{0, 0, 20751552, 123392448, 167175936};
    if (q2.jets[2] != expected2)
      throw std::runtime_error("Q2 order-two Python-reference gate failed");
    if (q2.jets[4] != expected4)
      throw std::runtime_error("Q2 order-four Python-reference gate failed");
  }
}

static std::string observable_json(const ObservableRun &run) {
  std::ostringstream out;
  out << "{\"max_order\":" << run.jets.size() - 1
      << ",\"seconds\":" << run.seconds
      << ",\"cache_before\":" << run.cache_before
      << ",\"cache_after\":" << run.cache_after
      << ",\"jets\":[";
  for (size_t order = 0; order < run.jets.size(); ++order) {
    if (order) out << ',';
    out << "{\"order\":" << order
        << ",\"lambda_coefficients\":" << json_poly(run.jets[order])
        << ",\"lambda_one\":\""
        << evaluate_poly(run.jets[order], 1) << "\"}";
  }
  out << "]}";
  return out.str();
}

static int parse_int(const char *value, const std::string &name) {
  try {
    return std::stoi(value);
  } catch (...) {
    throw std::invalid_argument("invalid integer for " + name);
  }
}

int main(int argc, char **argv) {
  try {
    int max_f = 9;
    int max_q2 = 8;
    int max_q1 = 8;
    MetricExponents exponents;
    std::string output_path;

    for (int i = 1; i < argc; ++i) {
      std::string arg = argv[i];
      auto take = [&](const std::string &name) {
        if (++i >= argc) throw std::invalid_argument("missing value for " + name);
        return argv[i];
      };
      if (arg == "--max-f") max_f = parse_int(take(arg), arg);
      else if (arg == "--max-q2") max_q2 = parse_int(take(arg), arg);
      else if (arg == "--max-q1") max_q1 = parse_int(take(arg), arg);
      else if (arg == "--a-exponent") exponents.a = parse_int(take(arg), arg);
      else if (arg == "--u-exponent") exponents.u = parse_int(take(arg), arg);
      else if (arg == "--w-exponent") exponents.w = parse_int(take(arg), arg);
      else if (arg == "--output") output_path = take(arg);
      else throw std::invalid_argument("unknown argument " + arg);
    }
    if (max_f < 0 || max_q2 < 0 || max_q1 < 0)
      throw std::invalid_argument("orders must be nonnegative");
    if (max_f > 9 || max_q2 > 8 || max_q1 > 8)
      throw std::invalid_argument(
          "Campaign 1 safety cap is f<=9 and Q1,Q2<=8");

    Tree f_root;
    f_root.a = {1};
    f_root.h = {1, 1};
    f_root.edges = {{0, 0}, {0, 1}};

    Tree q2_root;
    q2_root.a = {0};
    q2_root.h = {1, 1};
    q2_root.edges = {{0, 0}, {0, 1}};

    Tree q1_root;
    q1_root.h = {1};

    ParametricPeelingRecursion recursion(exponents);
    ObservableRun f = evaluate_root(recursion, "f", f_root, max_f);
    ObservableRun q2 = evaluate_root(recursion, "q2", q2_root, max_q2);
    ObservableRun q1 = evaluate_root(recursion, "q1", q1_root, max_q1);
    audit(f, q1, q2, exponents);

    std::ostringstream json;
    json << "{\n"
         << "  \"schema_version\": 1,\n"
         << "  \"parent_source_sha256\": "
#ifdef CAMPAIGN1_DENSE_PRIMARY_PARENT
         << "\"ad53d2d786393cafc9d034685638348afa19f08dbb8d5aeb3110f8e24c7847ad\",\n"
#else
         << "\"1931b628b25d2a7c018bc20a06d14aee6ee86ca702d8abcbec17e1ec719be260\",\n"
#endif
         << "  \"metric_exponents\": {\"a\":" << exponents.a
         << ",\"u\":" << exponents.u << ",\"w\":" << exponents.w
         << "},\n"
         << "  \"safety_caps\": {\"f\":9,\"q1\":8,\"q2\":8},\n"
         << "  \"regression_gates_passed\": true,\n"
         << "  \"observables\": {\n"
         << "    \"f\": " << observable_json(f) << ",\n"
         << "    \"q1\": " << observable_json(q1) << ",\n"
         << "    \"q2\": " << observable_json(q2) << "\n"
         << "  },\n"
         << "  \"cache\": {\"value_entries\":" << recursion.value_memo.size()
         << ",\"wick_entries\":" << recursion.wick_memo.size()
#ifndef CAMPAIGN1_DENSE_PRIMARY_PARENT
         << ",\"wick_subproblem_entries\":"
         << recursion.wick_subproblem_memo.size()
#endif
         << ",\"completed_base_evaluations\":"
         << recursion.completed_base_evaluations << "},\n"
         << "  \"misses_by_remaining_order\": {";
    bool first = true;
    for (const auto &[order, count] : recursion.misses_by_order) {
      if (!first) json << ',';
      first = false;
      json << '"' << order << "\":" << count;
    }
    json << "}\n}\n";

    if (output_path.empty()) {
      std::cout << json.str();
    } else {
      std::ofstream output(output_path);
      if (!output) throw std::runtime_error("could not open output path");
      output << json.str();
      if (!output) throw std::runtime_error("failed while writing output");
      std::cout << "wrote=" << output_path << '\n';
    }
    return 0;
  } catch (const std::exception &error) {
    std::cerr << "error: " << error.what() << '\n';
    return 2;
  }
}

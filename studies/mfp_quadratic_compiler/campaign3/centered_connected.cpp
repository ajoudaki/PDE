// Checked connected/vertex-partition compiler for Campaign 3.
//
// The first hidden activation is X+t with X=u^2-1 and t=1-c.  A tree row
// stores the power of a readout Gaussian, a tree column stores the power of
// X (including zero), and every edge is one middle-weight factor.  All
// affine factors are expanded exactly, while coefficients are retained as
// exact polynomials in t.  Terminal X moments obey
//
//   C_0=1, C_1=0, C_{p+1}=2p(C_p+C_{p-1}).

#include <algorithm>
#include <boost/multiprecision/cpp_int.hpp>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

using Integer = boost::multiprecision::checked_uint1024_t;
using Poly = std::vector<Integer>;  // coefficient of t^r

struct Tree {
  std::vector<unsigned char> a;
  std::vector<unsigned char> x;
  std::vector<std::pair<unsigned char, unsigned char>> edges;
};

static Integer odd_df(int k) {
  Integer out = 1;
  for (int q = k; q >= 1; q -= 2) out *= q;
  return out;
}

static Integer centered_moment(int power) {
  static std::vector<Integer> moments{1, 0};
  while (static_cast<int>(moments.size()) <= power) {
    int p = static_cast<int>(moments.size()) - 1;
    moments.push_back(Integer(2 * p) * (moments[p] + moments[p - 1]));
  }
  return moments[power];
}

static void trim(Poly &poly) {
  while (poly.size() > 1 && poly.back() == 0) poly.pop_back();
  if (poly.empty()) poly.push_back(0);
}

static bool zero(const Poly &poly) {
  return poly.empty() || (poly.size() == 1 && poly[0] == 0);
}

static void add_shift(Poly &out, const Poly &poly, const Integer &scale,
                      int shift = 0) {
  if (scale == 0 || zero(poly)) return;
  if (out.size() < poly.size() + static_cast<size_t>(shift))
    out.resize(poly.size() + static_cast<size_t>(shift), 0);
  for (size_t q = 0; q < poly.size(); ++q)
    out[q + shift] += scale * poly[q];
  trim(out);
}

static Poly multiply(const Poly &left, const Poly &right) {
  if (zero(left) || zero(right)) return Poly{0};
  Poly out(left.size() + right.size() - 1, 0);
  for (size_t i = 0; i < left.size(); ++i)
    for (size_t j = 0; j < right.size(); ++j)
      out[i + j] += left[i] * right[j];
  trim(out);
  return out;
}

static Integer choose(int n, int k) {
  if (k < 0 || k > n) return 0;
  k = std::min(k, n-k);
  Integer out = 1;
  for (int q = 1; q <= k; ++q) out = out * (n-k+q) / q;
  return out;
}

static std::string rooted_code(
    int vertex, int parent, const Tree &tree,
    const std::vector<std::vector<int>> &neighbors) {
  int rows = static_cast<int>(tree.a.size());
  std::vector<std::string> children;
  for (int w : neighbors[vertex]) if (w != parent)
    children.push_back(rooted_code(w, vertex, tree, neighbors));
  std::sort(children.begin(), children.end());
  std::string out;
  out.push_back('(');
  out.push_back(vertex < rows ? 'A' : 'X');
  out.push_back(static_cast<char>(1 + (vertex < rows ? tree.a[vertex]
                                      : tree.x[vertex-rows])));
  for (const auto &child : children) out += child;
  out.push_back(')');
  return out;
}

static std::string canonical_key(const Tree &tree) {
  int rows = static_cast<int>(tree.a.size());
  int n = rows + static_cast<int>(tree.x.size());
  std::vector<std::vector<int>> neighbors(n);
  for (auto [u, v] : tree.edges) {
    neighbors[u].push_back(rows+v);
    neighbors[rows+v].push_back(u);
  }
  if (static_cast<int>(tree.edges.size()) + 1 != n)
    throw std::logic_error("connected state is not a tree");
  std::vector<int> degree(n), leaves;
  for (int v = 0; v < n; ++v) {
    degree[v] = static_cast<int>(neighbors[v].size());
    if (degree[v] <= 1) leaves.push_back(v);
  }
  int remaining = n;
  while (remaining > 2) {
    remaining -= static_cast<int>(leaves.size());
    std::vector<int> next;
    for (int v : leaves) {
      degree[v] = 0;
      for (int w : neighbors[v]) if (degree[w] > 0) {
        --degree[w];
        if (degree[w] == 1) next.push_back(w);
      }
    }
    leaves.swap(next);
  }
  std::vector<int> centers;
  for (int v = 0; v < n; ++v)
    if (degree[v] > 0 || n == 1) centers.push_back(v);
  if (centers.empty()) centers = leaves;
  std::string best;
  for (int center : centers) {
    std::string code = rooted_code(center, -1, tree, neighbors);
    if (best.empty() || code < best) best = std::move(code);
  }
  return best;
}

static std::vector<Tree> split_components(const Tree &tree) {
  int rows = static_cast<int>(tree.a.size());
  int cols = static_cast<int>(tree.x.size());
  int n = rows + cols;
  std::vector<std::vector<int>> neighbors(n);
  for (auto [u, v] : tree.edges) {
    neighbors[u].push_back(rows+v);
    neighbors[rows+v].push_back(u);
  }
  std::vector<unsigned char> seen(n, 0);
  std::vector<Tree> out;
  for (int seed = 0; seed < n; ++seed) if (!seen[seed]) {
    std::vector<int> vertices{seed};
    seen[seed] = 1;
    for (size_t q = 0; q < vertices.size(); ++q)
      for (int w : neighbors[vertices[q]]) if (!seen[w]) {
        seen[w] = 1;
        vertices.push_back(w);
      }
    std::vector<int> row_map(rows, -1), col_map(cols, -1);
    Tree child;
    for (int v : vertices) if (v < rows) {
      row_map[v] = static_cast<int>(child.a.size());
      child.a.push_back(tree.a[v]);
    }
    for (int v : vertices) if (v >= rows) {
      col_map[v-rows] = static_cast<int>(child.x.size());
      child.x.push_back(tree.x[v-rows]);
    }
    for (auto [u, v] : tree.edges)
      if (row_map[u] >= 0 && col_map[v] >= 0)
        child.edges.push_back({static_cast<unsigned char>(row_map[u]),
                               static_cast<unsigned char>(col_map[v])});
    out.push_back(std::move(child));
  }
  return out;
}

// Exact leading-width terminal contraction.  A surviving quotient of a
// connected 2P-edge tree is equivalently a bipartition-respecting vertex
// partition into P+1 blocks whose occupied covariance cells all contain two
// raw edges.  Rows use Gaussian moments; columns use centered chi-square
// moments.  Zero column decorations are legitimate and retained.
struct VertexPartitionCentered {
  const Tree &tree;
  int rows, cols, pairs, target;
  std::vector<std::vector<int>> incidence;

  explicit VertexPartitionCentered(const Tree &value)
      : tree(value), rows(static_cast<int>(value.a.size())),
        cols(static_cast<int>(value.x.size())),
        pairs(static_cast<int>(value.edges.size()/2)), target(pairs+1),
        incidence(rows, std::vector<int>(cols, 0)) {
    for (auto [u, v] : value.edges) ++incidence[u][v];
    std::vector<int> order(rows);
    std::iota(order.begin(), order.end(), 0);
    std::stable_sort(order.begin(), order.end(), [&](int left, int right) {
      int dl = std::accumulate(incidence[left].begin(), incidence[left].end(), 0);
      int dr = std::accumulate(incidence[right].begin(), incidence[right].end(), 0);
      if (dl != dr) return dl > dr;
      return tree.a[left] > tree.a[right];
    });
    auto old_incidence = incidence;
    // The row exponents must follow the same optimization permutation.
    reordered_a.resize(rows);
    for (int u = 0; u < rows; ++u) {
      incidence[u] = old_incidence[order[u]];
      reordered_a[u] = tree.a[order[u]];
    }
  }

  std::vector<int> reordered_a;

  struct ColumnType {
    int exponent{};
    std::vector<int> signature;
    int multiplicity{};
  };

  struct ColumnDP {
    const std::vector<ColumnType> &types;
    int row_blocks;
    std::unordered_map<std::string, Integer> memo;

    std::string key(const std::vector<int> &remaining, int blocks) const {
      std::string out;
      out.push_back(static_cast<char>(blocks));
      for (int value : remaining) out.push_back(static_cast<char>(value));
      return out;
    }

    Integer rec(const std::vector<int> &remaining, int blocks) {
      int count = std::accumulate(remaining.begin(), remaining.end(), 0);
      if (blocks == 0) return count == 0 ? Integer(1) : Integer(0);
      if (count < blocks) return 0;
      std::string memo_key = key(remaining, blocks);
      auto found = memo.find(memo_key);
      if (found != memo.end()) return found->second;
      int distinguished = 0;
      while (distinguished < static_cast<int>(remaining.size()) &&
             remaining[distinguished] == 0) ++distinguished;
      if (distinguished == static_cast<int>(remaining.size())) return 0;
      std::vector<int> take(types.size(), 0), edge_sum(row_blocks, 0);
      take[distinguished] = 1;
      int exponent_sum = types[distinguished].exponent;
      for (int q = 0; q < row_blocks; ++q)
        edge_sum[q] = types[distinguished].signature[q];
      for (int value : edge_sum) if (value > 2) return 0;

      Integer total = 0;
      auto enumerate = [&](auto &&self, int type_index,
                           int current_exponent) -> void {
        if (type_index == static_cast<int>(types.size())) {
          for (int value : edge_sum) if (value == 1) return;
          std::vector<int> child = remaining;
          Integer choices = 1;
          for (int q = 0; q < static_cast<int>(types.size()); ++q) {
            int available = remaining[q] - (q == distinguished);
            int selected = take[q] - (q == distinguished);
            choices *= choose(available, selected);
            child[q] -= take[q];
          }
          Integer moment = centered_moment(current_exponent);
          if (moment != 0)
            total += choices * moment * rec(child, blocks-1);
          return;
        }
        int already = take[type_index];
        int available = remaining[type_index] - already;
        int maximum = available;
        for (int q = 0; q < row_blocks; ++q) {
          int degree = types[type_index].signature[q];
          if (degree) maximum = std::min(maximum, (2-edge_sum[q])/degree);
        }
        for (int add = 0; add <= maximum; ++add) {
          take[type_index] += add;
          for (int q = 0; q < row_blocks; ++q)
            edge_sum[q] += add * types[type_index].signature[q];
          self(self, type_index+1,
               current_exponent + add*types[type_index].exponent);
          for (int q = 0; q < row_blocks; ++q)
            edge_sum[q] -= add * types[type_index].signature[q];
          take[type_index] -= add;
        }
      };
      enumerate(enumerate, 0, exponent_sum);
      if (memo.size() < 200000) memo.emplace(std::move(memo_key), total);
      return total;
    }
  };

  Integer evaluate_row_partition(
      int row_blocks, const std::vector<int> &a_sum,
      const std::vector<int> &degree_sum,
      const std::vector<std::vector<int>> &block_incidence) const {
    int column_blocks = target-row_blocks;
    if (column_blocks < 1 || column_blocks > cols) return 0;
    Integer row_moment = 1;
    for (int q = 0; q < row_blocks; ++q) {
      if ((a_sum[q] & 1) || (degree_sum[q] & 1)) return 0;
      row_moment *= odd_df(a_sum[q]-1);
    }
    std::map<std::vector<int>, int> type_ids;
    std::vector<ColumnType> types;
    for (int v = 0; v < cols; ++v) {
      std::vector<int> signature(row_blocks, 0);
      for (int block = 0; block < row_blocks; ++block)
        signature[block] = block_incidence[block][v];
      std::vector<int> key{tree.x[v]};
      key.insert(key.end(), signature.begin(), signature.end());
      auto [it, inserted] = type_ids.emplace(key, types.size());
      if (inserted) types.push_back({tree.x[v], signature, 0});
      ++types[it->second].multiplicity;
    }
    std::vector<int> remaining;
    for (const auto &type : types) remaining.push_back(type.multiplicity);
    ColumnDP dp{types, row_blocks};
    return row_moment * dp.rec(remaining, column_blocks);
  }

  Integer run() const {
    if (tree.edges.size() & 1) return 0;
    if (tree.edges.empty()) {
      if (rows == 1 && cols == 0)
        return (tree.a[0]&1) ? Integer(0) : odd_df(tree.a[0]-1);
      if (rows == 0 && cols == 1) return centered_moment(tree.x[0]);
      return 0;
    }
    int total_a = std::accumulate(reordered_a.begin(), reordered_a.end(), 0);
    if (total_a & 1) return 0;
    std::vector<int> a_sum(rows, 0), degree_sum(rows, 0);
    std::vector<std::vector<int>> block_incidence(
        rows, std::vector<int>(cols, 0));
    std::vector<int> row_degree(rows, 0);
    for (int u = 0; u < rows; ++u)
      row_degree[u] = std::accumulate(incidence[u].begin(), incidence[u].end(), 0);
    a_sum[0] = reordered_a[0];
    degree_sum[0] = row_degree[0];
    block_incidence[0] = incidence[0];
    Integer total = 0;
    std::unordered_map<std::string, Integer> partition_cache;
    auto enumerate = [&](auto &&self, int row, int blocks) -> void {
      int remaining_rows = rows-row;
      if (blocks > target-1 || blocks+remaining_rows < target-cols) return;
      int parity_bad = 0;
      for (int q = 0; q < blocks; ++q)
        parity_bad += ((a_sum[q] | degree_sum[q]) & 1) != 0;
      if (parity_bad > remaining_rows) return;
      if (row == rows) {
        std::vector<std::string> codes(blocks);
        for (int block = 0; block < blocks; ++block) {
          codes[block].push_back(static_cast<char>(a_sum[block]));
          for (int v = 0; v < cols; ++v)
            codes[block].push_back(static_cast<char>(block_incidence[block][v]));
        }
        std::sort(codes.begin(), codes.end());
        std::string key;
        key.push_back(static_cast<char>(blocks));
        for (const auto &code : codes) key += code;
        auto found = partition_cache.find(key);
        if (found != partition_cache.end()) total += found->second;
        else {
          Integer value = evaluate_row_partition(
              blocks, a_sum, degree_sum, block_incidence);
          if (partition_cache.size() < 200000)
            partition_cache.emplace(std::move(key), value);
          total += value;
        }
        return;
      }
      int last_block = blocks < target-1 ? blocks : blocks-1;
      for (int block = 0; block <= last_block; ++block) {
        bool overfull = false;
        for (int v = 0; v < cols; ++v)
          if (block_incidence[block][v] + incidence[row][v] > 2) {
            overfull = true;
            break;
          }
        if (overfull) continue;
        a_sum[block] += reordered_a[row];
        degree_sum[block] += row_degree[row];
        for (int v = 0; v < cols; ++v)
          block_incidence[block][v] += incidence[row][v];
        self(self, row+1, blocks+(block==blocks));
        for (int v = 0; v < cols; ++v)
          block_incidence[block][v] -= incidence[row][v];
        degree_sum[block] -= row_degree[row];
        a_sum[block] -= reordered_a[row];
      }
    };
    enumerate(enumerate, 1, 1);
    return total;
  }
};

struct Recursion {
  std::unordered_map<std::string, Poly> value_memo;
  std::unordered_map<std::string, Integer> terminal_memo;
  size_t terminal_evaluations = 0;
  std::map<int, size_t> misses;

  std::string value_key(const Tree &tree, int order) const {
    std::string out;
    out.push_back(static_cast<char>(order));
    out += canonical_key(tree);
    return out;
  }

  Integer base(const Tree &tree) {
    std::string key = canonical_key(tree);
    auto found = terminal_memo.find(key);
    if (found != terminal_memo.end()) return found->second;
    Integer value = VertexPartitionCentered(tree).run();
    terminal_memo.emplace(std::move(key), value);
    ++terminal_evaluations;
    return value;
  }

  Poly value(const Tree &tree, int order) {
    if (tree.edges.size() & 1) return Poly{0};
    int parity = static_cast<int>(tree.edges.size()) +
                 std::accumulate(tree.a.begin(), tree.a.end(), 0);
    if ((parity + order) & 1) return Poly{0};
    std::string key = value_key(tree, order);
    auto found = value_memo.find(key);
    if (found != value_memo.end()) return found->second;
    ++misses[order];
    if (order == 0) {
      Poly answer{base(tree)};
      value_memo.emplace(std::move(key), answer);
      return answer;
    }
    Poly answer{0};

    // D a^p: p a^(p-1) z^2, each activation z edge decorated by X+t.
    for (size_t u = 0; u < tree.a.size(); ++u) if (tree.a[u]) {
      int multiplicity = tree.a[u];
      for (int left = 0; left <= 1; ++left)
        for (int right = 0; right <= 1; ++right) {
          Tree child = tree;
          --child.a[u];
          unsigned char v0 = static_cast<unsigned char>(child.x.size());
          child.x.push_back(left);
          child.x.push_back(right);
          child.edges.push_back({static_cast<unsigned char>(u), v0});
          child.edges.push_back({static_cast<unsigned char>(u),
                                 static_cast<unsigned char>(v0+1)});
          add_shift(answer, value(child, order-1), multiplicity, 2-left-right);
        }
    }

    // D X^p: 8p X^(p-1)(X+1) times a fresh row wedge and z edge.
    for (size_t v = 0; v < tree.x.size(); ++v) if (tree.x[v]) {
      int multiplicity = 8*tree.x[v];
      for (int increment = 0; increment <= 1; ++increment)
        for (int fresh = 0; fresh <= 1; ++fresh) {
          Tree child = tree;
          child.x[v] = tree.x[v]-1+increment;
          unsigned char u1 = static_cast<unsigned char>(child.a.size());
          unsigned char v1 = static_cast<unsigned char>(child.x.size());
          child.a.push_back(1);
          child.x.push_back(fresh);
          child.edges.push_back({u1, static_cast<unsigned char>(v)});
          child.edges.push_back({u1, v1});
          add_shift(answer, value(child, order-1), multiplicity, 1-fresh);
        }
    }

    // D W_uv: 2 a_u z_u (X_v+t), with exact bridge convolution.
    for (size_t edge_index = 0; edge_index < tree.edges.size(); ++edge_index) {
      for (int increment = 0; increment <= 1; ++increment)
        for (int fresh = 0; fresh <= 1; ++fresh) {
          Tree forest = tree;
          auto [u, v] = forest.edges[edge_index];
          ++forest.a[u];
          forest.x[v] += increment;
          unsigned char v1 = static_cast<unsigned char>(forest.x.size());
          forest.x.push_back(fresh);
          forest.edges.erase(forest.edges.begin()+edge_index);
          forest.edges.push_back({u, v1});
          auto children = split_components(forest);
          if (children.size() != 2)
            throw std::logic_error("W hit did not split into two components");
          Poly convolution{0};
          for (int q = 0; q <= order-1; ++q) {
            Poly product = multiply(value(children[0], q),
                                    value(children[1], order-1-q));
            add_shift(convolution, product, choose(order-1, q));
          }
          add_shift(answer, convolution, 2, 2-increment-fresh);
        }
    }
    value_memo.emplace(std::move(key), answer);
    return answer;
  }
};

static void print_poly(const Poly &poly) {
  std::cout << '[';
  for (size_t q = 0; q < poly.size(); ++q) {
    if (q) std::cout << ',';
    std::cout << '"' << poly[q] << '"';
  }
  std::cout << ']';
}

int main(int argc, char **argv) {
  int max_order = argc > 1 ? std::stoi(argv[1]) : 7;
  if (max_order < 0 || max_order > 7)
    throw std::invalid_argument("this audited compiler is capped at order 7");
  Recursion recursion;
  std::vector<Poly> jets;
  std::vector<double> seconds;
  std::vector<size_t> states, terminals;
  for (int order = 0; order <= max_order; ++order) {
    auto start = std::chrono::steady_clock::now();
    Poly result{0};
    // f=a W_i W_j (X_i+t)(X_j+t), expanded over the four affine sectors.
    for (int left = 0; left <= 1; ++left)
      for (int right = 0; right <= 1; ++right) {
        Tree root{{1}, {static_cast<unsigned char>(left),
                        static_cast<unsigned char>(right)}, {{0,0},{0,1}}};
        add_shift(result, recursion.value(root, order), 1, 2-left-right);
      }
    auto stop = std::chrono::steady_clock::now();
    jets.push_back(result);
    seconds.push_back(std::chrono::duration<double>(stop-start).count());
    states.push_back(recursion.value_memo.size());
    terminals.push_back(recursion.terminal_memo.size());
    std::cerr << "order=" << order << " seconds=" << seconds.back()
              << " states=" << states.back()
              << " terminals=" << terminals.back() << '\n';
  }
  std::cout << "{\n  \"schema_version\":1,\n"
            << "  \"parameter\":\"t=1-c in [-1,1]\",\n"
            << "  \"arithmetic\":\"checked_uint1024_t\",\n"
            << "  \"terminal\":\"vertex partitions with centered-X recurrence\",\n"
            << "  \"max_order\":" << max_order << ",\n"
            << "  \"jets_t\":[\n";
  for (size_t q = 0; q < jets.size(); ++q) {
    std::cout << "    "; print_poly(jets[q]);
    std::cout << (q+1 == jets.size() ? "\n" : ",\n");
  }
  std::cout << "  ],\n  \"seconds\":[";
  for (size_t q = 0; q < seconds.size(); ++q) {
    if (q) std::cout << ',';
    std::cout << seconds[q];
  }
  std::cout << "],\n  \"value_states\":[";
  for (size_t q = 0; q < states.size(); ++q) {
    if (q) std::cout << ',';
    std::cout << states[q];
  }
  std::cout << "],\n  \"terminal_trees\":[";
  for (size_t q = 0; q < terminals.size(); ++q) {
    if (q) std::cout << ',';
    std::cout << terminals[q];
  }
  std::cout << "]\n}\n";
  return 0;
}

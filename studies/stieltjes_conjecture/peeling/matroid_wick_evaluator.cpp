#ifndef MATROID_WICK_ENGINE_ALREADY_INCLUDED
#define main matroid_wick_embedded_engine_main
#include "sector_engine_checked.cpp"
#undef main
#endif

#include <iomanip>

// Exact leading Wick evaluator based on parity-valid row partitions.  In the
// tight-nullity case its column partition is recovered from binary-matroid
// connected components.  Otherwise it falls back to the audited ColumnDP.
struct MatroidWickEvaluator {
  const Tree &t;
  int R, C, P, target;
  std::vector<std::vector<int>> incidence;
  std::vector<int> scalar, degree;

  struct Block {
    uint32_t mask;
    int scalar, degree;
    std::vector<int> signature;
  };
  std::vector<Block> blocks;
  std::vector<std::vector<int>> by_first;

  struct Profile {
    std::vector<int> row_scalar, row_color;
    std::vector<std::vector<unsigned char>> columns;
    cpp_int value;
  };
  std::unordered_map<std::string, std::vector<Profile>> leaf_memo;
  size_t cache_hits = 0, isomorphism_tests = 0;

  explicit MatroidWickEvaluator(const Tree &tree)
      : t(tree), R(tree.a.size()), C(tree.h.size()),
        P(tree.edges.size() / 2), target(P + 1),
        incidence(R, std::vector<int>(C)), scalar(R), degree(R),
        by_first(R) {
    for (int u = 0; u < R; ++u) scalar[u] = tree.a[u];
    for (auto [u, v] : tree.edges) {
      ++incidence[u][v];
      ++degree[u];
    }
    precompute_blocks();
  }

  void precompute_blocks() {
    for (uint32_t mask = 1; mask < (uint32_t(1) << R); ++mask) {
      int scalar_sum = 0, degree_sum = 0;
      std::vector<int> signature(C);
      bool valid = true;
      for (int u = 0; u < R; ++u) if (mask >> u & 1) {
        scalar_sum += scalar[u];
        degree_sum += degree[u];
        for (int v = 0; v < C; ++v)
          if ((signature[v] += incidence[u][v]) > 2) valid = false;
      }
      // A Gaussian row block must have even a-power.  Its total number of
      // incident raw W factors is also even when every final cell is 0 or 2.
      if (valid && !(scalar_sum & 1) && !(degree_sum & 1)) {
        int id = blocks.size();
        blocks.push_back({mask, scalar_sum, degree_sum,
                          std::move(signature)});
        by_first[__builtin_ctz(mask)].push_back(id);
      }
    }
  }

  cpp_int tight_column_sum(const std::vector<int> &chosen,
                           int column_blocks) {
    int row_blocks = chosen.size();
    if (C - column_blocks != row_blocks) return 0;

    std::vector<uint32_t> vector(C);
    for (int v = 0; v < C; ++v)
      for (int q = 0; q < row_blocks; ++q)
        if (blocks[chosen[q]].signature[v] & 1)
          vector[v] |= uint32_t(1) << q;

    // Find a binary basis.
    std::vector<uint32_t> echelon(row_blocks);
    std::vector<int> pivot(row_blocks, -1), basis_column;
    int rank = 0;
    for (int v = 0; v < C; ++v) {
      uint32_t x = vector[v];
      for (int p = row_blocks - 1; p >= 0; --p) if (x >> p & 1) {
        if (pivot[p] >= 0) x ^= echelon[p];
        else {
          echelon[p] = x;
          pivot[p] = v;
          basis_column.push_back(v);
          ++rank;
          break;
        }
      }
    }
    if (rank != row_blocks) return 0;

    // Invert the basis matrix and express all columns in basis coordinates.
    std::vector<uint32_t> row(row_blocks);
    for (int q = 0; q < row_blocks; ++q) {
      for (int b = 0; b < row_blocks; ++b)
        if (vector[basis_column[b]] >> q & 1)
          row[q] |= uint32_t(1) << b;
      row[q] |= uint32_t(1) << (row_blocks + q);
    }
    for (int c = 0; c < row_blocks; ++c) {
      int p = c;
      while (p < row_blocks && !((row[p] >> c) & 1)) ++p;
      if (p == row_blocks) return 0;
      std::swap(row[c], row[p]);
      for (int q = 0; q < row_blocks; ++q)
        if (q != c && ((row[q] >> c) & 1)) row[q] ^= row[c];
    }
    std::vector<uint32_t> coordinates(C);
    for (int v = 0; v < C; ++v)
      for (int q = 0; q < row_blocks; ++q)
        if (__builtin_parity((row[q] >> row_blocks) & vector[v]))
          coordinates[v] |= uint32_t(1) << q;

    // Fundamental circuits generate the matroid connected components.
    std::vector<int> parent(C), size(C, 1);
    std::iota(parent.begin(), parent.end(), 0);
    auto root = [&](int x) {
      while (parent[x] != x) {
        parent[x] = parent[parent[x]];
        x = parent[x];
      }
      return x;
    };
    auto unite = [&](int x, int y) {
      x = root(x); y = root(y);
      if (x == y) return;
      if (size[x] < size[y]) std::swap(x, y);
      parent[y] = x; size[x] += size[y];
    };
    for (int v = 0; v < C; ++v) {
      int first = -1;
      for (int b = 0; b < row_blocks; ++b)
        if (coordinates[v] >> b & 1) {
          int w = basis_column[b];
          if (first < 0) first = w;
          else unite(first, w);
          unite(v, w);
        }
    }

    std::map<int, std::vector<int>> components;
    for (int v = 0; v < C; ++v) components[root(v)].push_back(v);
    if (static_cast<int>(components.size()) != column_blocks) return 0;

    cpp_int column_moment = 1;
    for (auto &[unused, vertices] : components) {
      uint32_t dependence = 0;
      int exponent = 0;
      for (int v : vertices) {
        dependence ^= vector[v];
        exponent += 2 * t.h[v];
      }
      if (dependence) return 0;
      // This is redundant under connectedness plus the target P+1 quotient
      // vertex count, but makes the 0-or-2 cell invariant executable.
      for (int q = 0; q < row_blocks; ++q) {
        int cell = 0;
        for (int v : vertices) cell += blocks[chosen[q]].signature[v];
        if (cell != 0 && cell != 2) return 0;
      }
      column_moment *= odd_double_factorial(exponent - 1);
    }
    cpp_int row_moment = 1;
    for (int id : chosen)
      row_moment *= odd_double_factorial(blocks[id].scalar - 1);
    return row_moment * column_moment;
  }

  // The fallback memoizer uses stable color refinement followed by an exact
  // row-permutation isomorphism check.  It affects running time only.
  std::pair<std::string, Profile> profile(const std::vector<int> &chosen) {
    int row_blocks = chosen.size(), N = row_blocks + C;
    Profile p;
    p.row_scalar.resize(row_blocks);
    p.columns.assign(C, std::vector<unsigned char>(row_blocks));
    for (int q = 0; q < row_blocks; ++q) {
      p.row_scalar[q] = blocks[chosen[q]].scalar;
      for (int v = 0; v < C; ++v)
        p.columns[v][q] = blocks[chosen[q]].signature[v];
    }
    std::vector<int> color(N);
    std::map<std::pair<int, int>, int> initial;
    for (int x = 0; x < N; ++x) {
      auto key = x < row_blocks
          ? std::pair<int, int>{0, p.row_scalar[x]}
          : std::pair<int, int>{1, 2 * t.h[x - row_blocks]};
      initial.try_emplace(key, 0);
    }
    int next = 0;
    for (auto &entry : initial) entry.second = next++;
    for (int x = 0; x < N; ++x)
      color[x] = x < row_blocks
          ? initial[{0, p.row_scalar[x]}]
          : initial[{1, 2 * t.h[x - row_blocks]}];
    for (int iteration = 0; iteration < N; ++iteration) {
      std::vector<std::string> signature(N);
      for (int q = 0; q < row_blocks; ++q) {
        auto &s = signature[q];
        s.push_back('R'); s.push_back(char(p.row_scalar[q]));
        s.push_back(char(color[q]));
        std::vector<std::pair<int, int>> neighbors;
        for (int v = 0; v < C; ++v) if (p.columns[v][q])
          neighbors.push_back({color[row_blocks + v], p.columns[v][q]});
        std::sort(neighbors.begin(), neighbors.end());
        for (auto [a, b] : neighbors) {
          s.push_back(char(a)); s.push_back(char(b));
        }
      }
      for (int v = 0; v < C; ++v) {
        auto &s = signature[row_blocks + v];
        s.push_back('C'); s.push_back(char(2 * t.h[v]));
        s.push_back(char(color[row_blocks + v]));
        std::vector<std::pair<int, int>> neighbors;
        for (int q = 0; q < row_blocks; ++q) if (p.columns[v][q])
          neighbors.push_back({color[q], p.columns[v][q]});
        std::sort(neighbors.begin(), neighbors.end());
        for (auto [a, b] : neighbors) {
          s.push_back(char(a)); s.push_back(char(b));
        }
      }
      std::map<std::string, int> ids;
      for (auto &s : signature) ids.try_emplace(s, 0);
      next = 0;
      for (auto &entry : ids) entry.second = next++;
      std::vector<int> refined(N);
      for (int x = 0; x < N; ++x) refined[x] = ids[signature[x]];
      if (refined == color) break;
      color.swap(refined);
    }
    p.row_color.assign(color.begin(), color.begin() + row_blocks);
    std::string key;
    key.push_back(char(row_blocks));
    auto sorted_colors = color;
    std::sort(sorted_colors.begin(), sorted_colors.end());
    for (int z : sorted_colors) key.push_back(char(z));
    std::vector<std::tuple<int, int, int>> edges;
    for (int v = 0; v < C; ++v)
      for (int q = 0; q < row_blocks; ++q) if (p.columns[v][q])
        edges.push_back({color[q], color[row_blocks + v], p.columns[v][q]});
    std::sort(edges.begin(), edges.end());
    for (auto [a, b, m] : edges) {
      key.push_back(char(a)); key.push_back(char(b)); key.push_back(char(m));
    }
    return {key, std::move(p)};
  }

  bool isomorphic(const Profile &a, const Profile &b) {
    ++isomorphism_tests;
    int row_blocks = a.row_scalar.size();
    if (b.row_scalar.size() != a.row_scalar.size()) return false;
    std::map<std::pair<int, int>, std::vector<int>> ga, gb;
    for (int q = 0; q < row_blocks; ++q) {
      ga[{a.row_scalar[q], a.row_color[q]}].push_back(q);
      gb[{b.row_scalar[q], b.row_color[q]}].push_back(q);
    }
    if (ga.size() != gb.size()) return false;
    for (auto &[key, vertices] : ga)
      if (gb[key].size() != vertices.size()) return false;
    std::vector<std::pair<std::vector<int>, std::vector<int>>> groups;
    for (auto &[key, vertices] : ga) groups.push_back({vertices, gb[key]});
    std::vector<int> map_row(row_blocks, -1);
    auto target_columns = b.columns;
    std::sort(target_columns.begin(), target_columns.end());
    auto test = [&]() {
      std::vector<std::vector<unsigned char>> columns;
      for (auto &column : a.columns) {
        std::vector<unsigned char> x(row_blocks);
        for (int q = 0; q < row_blocks; ++q) x[map_row[q]] = column[q];
        columns.push_back(std::move(x));
      }
      std::sort(columns.begin(), columns.end());
      return columns == target_columns;
    };
    auto recurse = [&](auto &&self, int group) -> bool {
      if (group == static_cast<int>(groups.size())) return test();
      auto left = groups[group].first, right = groups[group].second;
      std::sort(right.begin(), right.end());
      do {
        for (int q = 0; q < static_cast<int>(left.size()); ++q)
          map_row[left[q]] = right[q];
        if (self(self, group + 1)) return true;
      } while (std::next_permutation(right.begin(), right.end()));
      return false;
    };
    return recurse(recurse, 0);
  }

  cpp_int evaluate_row_partition(const std::vector<int> &chosen) {
    int row_blocks = chosen.size(), column_blocks = target - row_blocks;
    if (column_blocks < 1 || column_blocks > C) return 0;
    if (C - column_blocks == row_blocks)
      return tight_column_sum(chosen, column_blocks);

    auto [memo_key, p] = profile(chosen);
    auto found = leaf_memo.find(memo_key);
    if (found != leaf_memo.end())
      for (auto &representative : found->second)
        if (isomorphic(p, representative)) {
          ++cache_hits;
          return representative.value;
        }

    cpp_int row_moment = 1;
    for (int id : chosen)
      row_moment *= odd_double_factorial(blocks[id].scalar - 1);
    std::vector<VertexPartitionWickEvaluator::ColumnType> types;
    std::map<std::vector<int>, int> type_ids;
    for (int v = 0; v < C; ++v) {
      std::vector<int> key{2 * t.h[v]};
      for (int id : chosen) key.push_back(blocks[id].signature[v]);
      auto [it, inserted] = type_ids.emplace(key, types.size());
      if (inserted)
        types.push_back({2 * t.h[v],
                         std::vector<int>(key.begin() + 1, key.end()), 0});
      ++types[it->second].multiplicity;
    }
    std::vector<int> remaining;
    for (auto &type : types) remaining.push_back(type.multiplicity);
    VertexPartitionWickEvaluator::ColumnDP dp{types, row_blocks};
    cpp_int value = row_moment * dp.rec(remaining, column_blocks);
    p.value = value;
    leaf_memo[std::move(memo_key)].push_back(std::move(p));
    return value;
  }

  cpp_int recurse(uint32_t remaining, std::vector<int> &chosen) {
    if (!remaining) return evaluate_row_partition(chosen);
    int have = chosen.size(), left = __builtin_popcount(remaining);
    if (have >= target - 1 || have + left < target - C) return 0;
    int first = __builtin_ctz(remaining);
    cpp_int total = 0;
    for (int id : by_first[first])
      if ((blocks[id].mask & remaining) == blocks[id].mask) {
        chosen.push_back(id);
        total += recurse(remaining ^ blocks[id].mask, chosen);
        chosen.pop_back();
      }
    return total;
  }

  cpp_int run() {
    if (std::accumulate(t.a.begin(), t.a.end(), 0) & 1) return 0;
    std::vector<int> chosen;
    return recurse((uint32_t(1) << R) - 1, chosen);
  }
};

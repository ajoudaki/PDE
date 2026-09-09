// Memory-bounded exact driver: evaluate one root order directly with the
// connected recurrence.  Unlike the two-phase runner, this retains only Wick
// subproblems reachable from the current base tree and releases them before
// moving to the next base tree.  It is slower but bounds peak memory sharply.
#define main component_recursion_serial_main
#include "component_recursion.cpp"
#undef main

int main(int argc, char **argv) {
  const int order = argc > 1 ? std::stoi(argv[1]) : 11;
  Tree root;
  root.a = {1};
  root.h = {1, 1};
  root.edges = {{0, 0}, {0, 1}};

  PeelingRecursion recursion;
  const auto start = std::chrono::steady_clock::now();
  const cpp_int value = recursion.value(root, order, true);
  const auto stop = std::chrono::steady_clock::now();
  std::cout << "D^" << order << " f = " << value << "\n"
            << "root hits: a=" << recursion.root_by_a_hit[order]
            << " h=" << recursion.root_by_h_hit[order]
            << " W=" << recursion.root_by_w_hit[order] << "\n"
            << "seconds="
            << std::chrono::duration<double>(stop - start).count()
            << " value_cache=" << recursion.value_memo.size()
            << " base_cache=" << recursion.wick_memo.size() << "\n";
  return 0;
}

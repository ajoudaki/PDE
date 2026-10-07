"""Bounded exact-algebra checks for scheduling refinements, not a neural run.

Fixed cases test packed Toeplitz hashing, depth-first generator traversal,
cached metric products, exact tiled reductions, and indexed pivot heaps.
No random sampling, GPU timing, precision sufficiency, or neural fidelity
conclusion is inferred. Run with python3 -B and no output files are created.
"""

from fractions import Fraction
import unittest


def toeplitz_reference(value, coefficients, offset, width):
    mask = (1 << width) - 1
    result = offset
    for output_bit in range(width):
        window = (coefficients >> output_bit) & mask
        result ^= ((window & value).bit_count() % 2) << output_bit
    return result & mask


def toeplitz_packed(value, coefficients, offset, width, word_bits):
    """Chunked shift/XOR implementation of the same binary convolution."""
    result = offset
    word_mask = (1 << word_bits) - 1
    for input_bit in range(width):
        if (value >> input_bit) & 1:
            for start in range(0, width, word_bits):
                chunk = (coefficients >> (input_bit + start)) & word_mask
                result ^= chunk << start
    return result & ((1 << width) - 1)


def generator_leaf(seed, hashes, index):
    value = seed
    for level in range(len(hashes) - 1, -1, -1):
        if (index >> level) & 1:
            value = hashes[level](value)
    return value


def generator_stream(seed, hashes, counters):
    """Exact left-to-right recursive output with an explicitly counted stack."""
    stack = [(len(hashes), seed)]
    while stack:
        counters['peak_stack'] = max(counters['peak_stack'], len(stack))
        level, value = stack.pop()
        if level == 0:
            yield value
        else:
            right = hashes[level - 1](value)
            counters['hashes'] += 1
            stack.append((level - 1, right))
            stack.append((level - 1, value))


class IndexedPivotHeap:
    """One entry per upper-triangle position; no growing stale-entry list."""

    def __init__(self, matrix):
        self.matrix = matrix
        self.heap = [(i, j) for i in range(len(matrix))
                     for j in range(i + 1, len(matrix))]
        self.position = {pair: index for index, pair in enumerate(self.heap)}
        for index in range(len(self.heap) // 2 - 1, -1, -1):
            self._down(index)

    def _key(self, pair):
        i, j = pair
        return -abs(self.matrix[i][j]), i, j

    def _swap(self, first, second):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]
        self.position[self.heap[first]] = first
        self.position[self.heap[second]] = second

    def _up(self, index):
        while index:
            parent = (index - 1) // 2
            if self._key(self.heap[parent]) <= self._key(self.heap[index]):
                break
            self._swap(parent, index)
            index = parent
        return index

    def _down(self, index):
        while 2 * index + 1 < len(self.heap):
            child = 2 * index + 1
            if (child + 1 < len(self.heap)
                    and self._key(self.heap[child + 1]) < self._key(self.heap[child])):
                child += 1
            if self._key(self.heap[index]) <= self._key(self.heap[child]):
                break
            self._swap(index, child)
            index = child

    def set_entry(self, i, j, value):
        """Apply one symmetric entry change and immediately restore the heap."""
        self.matrix[i][j] = self.matrix[j][i] = value
        if i != j:
            pair = min(i, j), max(i, j)
            index = self._up(self.position[pair])
            self._down(index)

    def largest(self):
        return self.heap[0] if self.heap else None


class StreamlineChecks(unittest.TestCase):
    def test_packed_hash(self):
        for width in (1, 2, 3, 7, 8, 15, 16, 33):
            mask = (1 << width) - 1
            values = (0, 1, mask, 0x13579BDF & mask)
            coefficients = (0, (1 << (2 * width - 1)) - 1,
                            0xCAFEBABEF00D12345 & ((1 << (2 * width - 1)) - 1))
            for value in values:
                for coeff in coefficients:
                    for word_bits in (1, 3, 8, 16, 64):
                        self.assertEqual(
                            toeplitz_reference(value, coeff, mask // 3, width),
                            toeplitz_packed(value, coeff, mask // 3, width, word_bits))

    def test_generator_stream(self):
        width = 11
        mask = (1 << width) - 1
        for depth in range(8):
            hashes = [lambda value, level=level: toeplitz_reference(
                value, (0x16D35B * (level + 1)) & ((1 << (2 * width - 1)) - 1),
                (37 * level + 3) & mask, width) for level in range(depth)]
            for seed in (0, 1, 123, mask):
                counters = {'hashes': 0, 'peak_stack': 0}
                result = list(generator_stream(seed, hashes, counters))
                expected = [generator_leaf(seed, hashes, i)
                            for i in range(1 << depth)]
                self.assertEqual(result, expected)
                self.assertEqual(counters['hashes'], (1 << depth) - 1)
                self.assertLessEqual(counters['peak_stack'], depth + 1)

    def test_cached_metric_pairs(self):
        for dimension in range(1, 7):
            basis = [[Fraction(((i + 2) * (j + 3)) % 11 - 5, 8)
                      for j in range(dimension)] for i in range(dimension)]
            metric = [[sum(basis[k][i] * basis[k][j] for k in range(dimension))
                       for j in range(dimension)] for i in range(dimension)]
            fields = [[Fraction(((r + 1) * (i + 2)) % 13 - 6, 16)
                       for i in range(dimension)] for r in range(8)]
            cache = [[sum(metric[i][j] * field[j] for j in range(dimension))
                      for i in range(dimension)] for field in fields]
            for first, u in enumerate(fields):
                for second, v in enumerate(fields):
                    direct = sum(u[i] * metric[i][j] * v[j]
                                 for i in range(dimension) for j in range(dimension))
                    cached = sum(u[i] * cache[second][i] for i in range(dimension))
                    self.assertEqual(direct, cached, (first, second))

    def test_tiled_exact_reduction(self):
        products = [Fraction((i * 17) % 23 - 11, 128) for i in range(37)]
        reference = sum(products)
        for tile_size in (1, 2, 3, 8, 16, 37, 64):
            tiled = sum(sum(products[start:start + tile_size])
                        for start in range(0, len(products), tile_size))
            self.assertEqual(tiled, reference)

    def test_indexed_heap_matches_scan(self):
        for dimension in range(1, 10):
            matrix = [[Fraction(0) for _ in range(dimension)]
                      for _ in range(dimension)]
            heap = IndexedPivotHeap(matrix)
            pairs = [(i, j) for i in range(dimension)
                     for j in range(i + 1, dimension)]
            for step in range(80):
                rows = (step % dimension, (3 * step + 1) % dimension)
                for i, j in pairs:
                    if i in rows or j in rows:
                        heap.set_entry(i, j, Fraction((17 * i + 3 * j + step) % 9 - 4, 8))
                expected = min(pairs, key=lambda pair: (-abs(matrix[pair[0]][pair[1]]),
                                                       *pair), default=None)
                self.assertEqual(heap.largest(), expected)
                self.assertEqual(len(heap.heap), len(pairs))
                self.assertEqual(len(heap.position), len(pairs))


if __name__ == '__main__':
    unittest.main(verbosity=2)

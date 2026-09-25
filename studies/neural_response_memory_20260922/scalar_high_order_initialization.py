"""Exact ordered directional tensors T1,...,T6 at canonical initialization.

T1[q]=f_q and Tp[q,b,i1,...,i_(p-2)]=D_i_(p-2)...D_i1 Theta[q,b].
Every direction is a training direction. Neuron fields and Gaussian matrices
are temporary initializer storage only; returned arrays have scalar axes.
The GPU implementation uses float64, exact low-rank derivative actions,
cached lower ordered words, and shared-matrix GEMMs over word chunks.
"""

import hashlib
from itertools import product
import os
import resource
import time

import numpy as np
import torch

import scalar_aggregate_engine as aggregate


FIELD_NAMES = ("h", "z", "delta", "back", "gate")
CUDA_LIMIT = 12 * 2**30
RSS_LIMIT = 8 * 2**30


class InitializationLimit(RuntimeError):
    """A resource stop; partial coefficients must not be interpreted as complete."""

    def __init__(self, message, metadata):
        super().__init__(message)
        self.metadata = dict(metadata, status="resource_limit", message=message)


def array_hash(*arrays):
    digest = hashlib.sha256()
    for array in arrays:
        array = np.asarray(array)
        digest.update(str(array.shape).encode())
        digest.update(str(array.dtype).encode())
        digest.update(array.tobytes(order="C"))
    return digest.hexdigest()


def _subsets(mask):
    """All position submasks, including both endpoints; repeats stay distinct."""
    subset = mask
    while True:
        yield subset
        if subset == 0:
            break
        subset = (subset-1) & mask


def _positions(mask, length):
    return tuple(i for i in range(length) if mask & (1 << i))


class _Budget:
    def __init__(self, device, max_wall_seconds, max_cuda_bytes, max_rss_bytes):
        self.device, self.start = device, time.monotonic()
        self.max_wall_seconds = max_wall_seconds
        self.max_cuda_bytes, self.max_rss_bytes = max_cuda_bytes, max_rss_bytes
        self.completed_word_chunks = 0
        self.metadata = {}

    def check(self, *, synchronize=False):
        if self.device.type == "cuda" and synchronize:
            torch.cuda.synchronize(self.device)
        self.metadata.update(
            wall_seconds=time.monotonic()-self.start,
            peak_process_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024,
            peak_cuda_allocated_bytes=(torch.cuda.max_memory_allocated(self.device)
                                       if self.device.type == "cuda" else 0),
            peak_cuda_reserved_bytes=(torch.cuda.max_memory_reserved(self.device)
                                      if self.device.type == "cuda" else 0),
            completed_word_chunks=self.completed_word_chunks)
        for actual, limit in (("wall_seconds", self.max_wall_seconds),
                              ("peak_process_rss_bytes", self.max_rss_bytes),
                              ("peak_cuda_allocated_bytes", self.max_cuda_bytes)):
            if self.metadata[actual] >= limit:
                raise InitializationLimit(actual + " reached its cap", self.metadata)


class _Fields:
    """Ordered derivatives on one query batch; directions use training fields."""

    def __init__(self, params, inputs, training, word_chunk_size, budget):
        self.params, self.inputs = params, inputs
        self._training = training
        self.n, self.depth = len(params[-1]), len(params)-1
        self.m = len(inputs) if training is None else training.m
        self.q, self.device = len(inputs), inputs.device
        self.word_chunk_size, self.budget = word_chunk_size, budget
        self.index_cache = {} if training is None else training.index_cache
        base = {name: [] for name in FIELD_NAMES}
        previous = inputs.T
        for matrix in params[:-1]:
            z = matrix @ previous
            h = torch.tanh(z)
            base["z"].append(z[None])
            base["h"].append(h[None])
            base["gate"].append((1-h*h)[None])
            previous = h
        base["back"], base["delta"] = [None]*self.depth, [None]*self.depth
        for layer in range(self.depth-1, -1, -1):
            back = (params[-1][:, None].expand(-1, self.q) if layer == self.depth-1
                    else params[layer+1].T @ base["delta"][layer+1][0])
            base["back"][layer] = back[None]
            base["delta"][layer] = base["gate"][layer]*back[None]
        self.cache = [base]
        self.gram_cache = []
        self.input_gram = inputs @ self.training.inputs.T

    @property
    def training(self):
        # A self-reference here would keep large GPU caches alive until cyclic GC.
        return self if self._training is None else self._training

    def words(self, degree):
        if degree == 0:
            return np.zeros((1, 0), dtype=np.int64)
        return np.asarray(tuple(product(range(self.m), repeat=degree)), dtype=np.int64)

    def chunks(self, degree):
        words = self.words(degree)
        for start in range(0, len(words), self.word_chunk_size):
            yield start, words[start:start+self.word_chunk_size]

    def _indices(self, words, mask):
        key = ("word", words.shape[1], words[0].tobytes(), len(words), mask)
        if key in self.index_cache:
            return self.index_cache[key]
        positions = _positions(mask, words.shape[1])
        if not positions:
            value = torch.zeros(len(words), dtype=torch.long, device=self.device)
        else:
            indices = np.zeros(len(words), dtype=np.int64)
            for position in positions:
                indices = indices*self.m+words[:, position]
            value = torch.as_tensor(indices, dtype=torch.long, device=self.device)
        self.index_cache[key] = value
        return value

    def _samples(self, words, position):
        key = ("sample", words.shape[1], words[0].tobytes(), len(words), position)
        if key not in self.index_cache:
            self.index_cache[key] = torch.as_tensor(words[:, position].copy(), dtype=torch.long, device=self.device)
        return self.index_cache[key]

    def get(self, field, layer, words, mask, current=None):
        degree = int(mask.bit_count())
        if mask == (1 << words.shape[1])-1 and current is not None:
            return current[field][layer]
        value = self.cache[degree][field][layer]
        if degree == 0:
            return value.expand(len(words), -1, -1)
        return value.index_select(0, self._indices(words, mask))

    def train_column(self, field, layer, words, mask, first_position):
        """Gather just n-vectors, without materializing n-by-M intermediate copies."""
        indices = self._indices(words, mask)
        samples = self._samples(words, first_position)
        return self.training.cache[mask.bit_count()][field][layer][indices, :, samples]

    @staticmethod
    def shared_action(matrix, values):
        """One matrix GEMM for every word's query columns."""
        count, width, queries = values.shape
        flat = values.permute(1, 0, 2).reshape(width, count*queries)
        return (matrix @ flat).reshape(matrix.shape[0], count, queries).permute(1, 0, 2)

    def low_rank_actions(self, layer, field, field_layer, words, transpose=False):
        """Sum (D_subword W) times the complementary field derivative.

        Derivative matrices are never formed. For degree four there are 40
        rank-one terms across all nonempty subwords. Process eight at a time
        to bound temporary copies of the n-by-query fields.
        """
        length, count = words.shape[1], len(words)
        full = (1 << length)-1
        terms = []
        for matrix_mask in range(1, full+1):
            first_position = (matrix_mask & -matrix_mask).bit_length()-1
            tail = matrix_mask & ~(1 << first_position)
            for left_mask in _subsets(tail):
                terms.append((first_position, left_mask, tail ^ left_mask, full ^ matrix_mask))
        result = self.inputs.new_zeros((count, self.n, self.q))
        for start in range(0, len(terms), 8):
            left, right, values = [], [], []
            for first, left_mask, right_mask, value_mask in terms[start:start+8]:
                a = self.train_column("delta", layer, words, left_mask, first)
                b = self.train_column("h", layer-1, words, right_mask, first)
                left.append(b if transpose else a)
                right.append(a if transpose else b)
                values.append(self.get(field, field_layer, words, value_mask))
            left, right, values = torch.stack(left, 1), torch.stack(right, 1), torch.stack(values, 1)
            rank = left.shape[1]
            contraction = torch.bmm(right.reshape(count*rank, 1, self.n),
                                    values.reshape(count*rank, self.n, self.q))
            result.add_(torch.bmm(left.transpose(1, 2), contraction.reshape(count, rank, self.q)),
                        alpha=1/self.n)
        return result

    def evaluate(self, words):
        """A same-degree chunk; only proper-subword fields need be cached."""
        length, count = words.shape[1], len(words)
        if length == 0:
            return self.cache[0]
        full, tail = (1 << length)-1, ((1 << length)-1) ^ 1
        current = {name: [None]*self.depth for name in FIELD_NAMES}
        for layer in range(self.depth):
            if layer == 0:
                delta = self.train_column("delta", 0, words, tail, 0)
                samples = self._samples(words, 0)
                gram = self.training.inputs[samples] @ self.inputs.T
                z = delta[:, :, None]*gram[:, None, :]
            else:
                z = self.shared_action(self.params[layer], current["h"][layer-1])
                z = z+self.low_rank_actions(layer, "h", layer-1, words)
            current["z"][layer] = z
            # D_w tanh(z)=sum_{S subset tail(w)} gate_S z_(first,tail\S).
            h = self.cache[0]["gate"][layer]*z
            for subset in _subsets(tail):
                if subset:
                    h = h+self.get("gate", layer, words, subset)*self.get("z", layer, words, full ^ subset)
            current["h"][layer] = h
            # Pair complementary subsets: -D_w(h*h)=-2 sum_{S containing first} h_S h_Sc.
            gate = -2*h*self.cache[0]["h"][layer]
            for subset in range(1, full):
                if subset & 1:
                    gate = gate-2*self.get("h", layer, words, subset)*self.get("h", layer, words, full ^ subset)
            current["gate"][layer] = gate
        for layer in range(self.depth-1, -1, -1):
            if layer == self.depth-1:
                back = self.train_column("h", layer, words, tail, 0)[:, :, None].expand(-1, -1, self.q)
            else:
                back = self.shared_action(self.params[layer+1].T, current["delta"][layer+1])
                back = back+self.low_rank_actions(layer+1, "delta", layer+1, words, transpose=True)
            current["back"][layer] = back
            delta = self.cache[0]["gate"][layer]*back+current["gate"][layer]*self.cache[0]["back"][layer]
            for subset in range(1, full):
                delta = delta+self.get("gate", layer, words, subset)*self.get("back", layer, words, full ^ subset)
            current["delta"][layer] = delta
        self.budget.completed_word_chunks += 1
        self.budget.check()
        return current

    def build_lower(self, maximum_degree):
        for degree in range(1, maximum_degree+1):
            level = {name: [self.inputs.new_empty((self.m**degree, self.n, self.q))
                            for _ in range(self.depth)] for name in FIELD_NAMES}
            for start, words in self.chunks(degree):
                values = self.evaluate(words)
                for name in FIELD_NAMES:
                    for layer in range(self.depth):
                        level[name][layer][start:start+len(words)].copy_(values[name][layer])
            self.cache.append(level)
            self.budget.check()

    def chunk_fields(self, degree, start, words):
        if degree >= len(self.cache):
            return self.evaluate(words)
        return {name: [value[start:start+len(words)] for value in self.cache[degree][name]]
                for name in FIELD_NAMES}

    def gram_fields(self, words, query_current, train_current):
        full = (1 << words.shape[1])-1
        result = {name: [] for name in ("h", "delta")}
        for name in result:
            for layer in range(self.depth):
                gram = self.inputs.new_zeros((len(words), self.q, self.m))
                for subset in range(full+1):
                    left = self.get(name, layer, words, subset, query_current)
                    right = self.training.get(name, layer, words, full ^ subset, train_current)
                    gram.add_(torch.bmm(left.transpose(1, 2), right), alpha=1/self.n)
                result[name].append(gram)
        return result

    def get_gram(self, name, layer, words, mask, current):
        if mask == (1 << words.shape[1])-1:
            return current[name][layer]
        value = self.gram_cache[mask.bit_count()][name][layer]
        if mask == 0:
            return value.expand(len(words), -1, -1)
        return value.index_select(0, self._indices(words, mask))

    def coefficients(self, order):
        maximum_degree = order-2
        result = {"T1": (self.params[-1] @ self.cache[0]["h"][-1][0]/self.n).cpu().numpy().copy()}
        for degree in range(maximum_degree+1):
            tensor = np.empty((self.q,)+(self.m,)*(degree+1), dtype=np.float64)
            flat = tensor.reshape(self.q, self.m, -1)
            gram_level = ({name: [self.inputs.new_empty((self.m**degree, self.q, self.m))
                                 for _ in range(self.depth)] for name in ("h", "delta")}
                          if degree < maximum_degree else None)
            for start, words in self.chunks(degree):
                query_current = self.chunk_fields(degree, start, words)
                train_current = (query_current if self is self.training
                                 else self.training.chunk_fields(degree, start, words))
                grams = self.gram_fields(words, query_current, train_current)
                value = self.input_gram*grams["delta"][0]+grams["h"][-1]
                full = (1 << degree)-1
                for layer in range(1, self.depth):
                    for subset in range(full+1):
                        value = value+self.get_gram("h", layer-1, words, subset, grams)*self.get_gram(
                            "delta", layer, words, full ^ subset, grams)
                flat[:, :, start:start+len(words)] = value.permute(1, 2, 0).cpu().numpy()
                if gram_level is not None:
                    for name in grams:
                        for layer in range(self.depth):
                            gram_level[name][layer][start:start+len(words)].copy_(grams[name][layer])
                self.budget.check()
            if gram_level is not None:
                self.gram_cache.append(gram_level)
            result["T"+str(degree+2)] = tensor
        return result


@torch.no_grad()
def initialize_probe_coefficients(params, train_inputs, probe_inputs, order=6, *,
                                  device="cuda:0", batch_size=32, word_chunk_size=16,
                                  max_wall_seconds=600., max_cuda_bytes=CUDA_LIMIT,
                                  max_rss_bytes=RSS_LIMIT, return_metadata=False):
    """Return T1..Torder arrays, with shape (N,)+(M,)*(p-1) for Tp.

    Inputs are already normalized. `params` must be the original NumPy arrays;
    no random draw occurs here. CPU is supported for deterministic small tests.
    Caps may be tightened but not raised beyond 12 GiB CUDA/8 GiB process RSS.
    At order six, degree<=3 fields are cached; degree4 fields are streamed.
    """
    if isinstance(order, bool) or not isinstance(order, int) or not 2 <= order <= 6:
        raise ValueError("order must be an integer from 2 through 6")
    for name, value in (("batch_size", batch_size), ("word_chunk_size", word_chunk_size)):
        aggregate._positive_integer(value, name)
    if not np.isfinite(max_wall_seconds) or max_wall_seconds <= 0:
        raise ValueError("positive finite max_wall_seconds required")
    for name, value, ceiling in (("max_cuda_bytes", max_cuda_bytes, CUDA_LIMIT),
                                 ("max_rss_bytes", max_rss_bytes, RSS_LIMIT)):
        if isinstance(value, bool) or not isinstance(value, int) or not 0 < value <= ceiling:
            raise ValueError(name+" must be a positive integer within its protocol ceiling")
    params, train_inputs = aggregate._validated_network(params, train_inputs)
    _, probe_inputs = aggregate._validated_network(params, probe_inputs)
    if len(params) != 4:
        raise ValueError("this initializer requires three hidden tanh layers")
    device = torch.device(device)
    if device.type not in ("cpu", "cuda"):
        raise ValueError("device must be cpu or cuda")
    os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
    torch.use_deterministic_algorithms(True)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False
    if device.type == "cuda":
        if not torch.cuda.is_available():
            raise RuntimeError("CUDA requested but unavailable; no CPU fallback")
        if device.index is None:
            device = torch.device("cuda", torch.cuda.current_device())
        torch.cuda.set_device(device)
        torch.cuda.reset_peak_memory_stats(device)
    budget = _Budget(device, max_wall_seconds, max_cuda_bytes, max_rss_bytes)
    budget.check()
    initial_hash = array_hash(*params)
    tensors = tuple(torch.tensor(value, dtype=torch.float64, device=device) for value in params)
    if array_hash(*(value.cpu().numpy() for value in tensors)) != initial_hash:
        raise RuntimeError("initialization changed during device transfer")
    train = torch.tensor(train_inputs, dtype=torch.float64, device=device)
    training = _Fields(tensors, train, None, word_chunk_size, budget)
    training.build_lower(max(0, order-3))
    budget.check(synchronize=True)
    training_cache_seconds = budget.metadata["wall_seconds"]
    count, m = len(probe_inputs), len(train_inputs)
    result = {"T"+str(p): np.empty((count,)+(m,)*(p-1), dtype=np.float64) for p in range(1, order+1)}
    if np.array_equal(probe_inputs, train_inputs):
        result = training.coefficients(order)
    else:
        for start in range(0, count, batch_size):
            stop = min(count, start+batch_size)
            probe = torch.tensor(probe_inputs[start:stop], dtype=torch.float64, device=device)
            fields = _Fields(tensors, probe, training, word_chunk_size, budget)
            fields.build_lower(max(0, order-3))
            coefficients = fields.coefficients(order)
            for name, value in coefficients.items():
                result[name][start:stop] = value
            del fields, coefficients, probe
            budget.check()
    budget.check(synchronize=True)
    metadata = dict(budget.metadata, status="complete", order=order, width=len(params[-1]),
                    sample_count=m, query_count=count, device=str(device), dtype="float64",
                    initialization_hash=initial_hash, training_input_hash=array_hash(train_inputs),
                    probe_input_hash=array_hash(probe_inputs), batch_size=batch_size,
                    word_chunk_size=word_chunk_size, cached_maximum_word_degree=max(0, order-3),
                    streamed_word_degree=order-2, deterministic_algorithms=True, tf32=False,
                    source="exact ordered-word derivative recursion", coefficient_bytes=
                    sum(value.nbytes for value in result.values()),
                    training_cache_seconds=training_cache_seconds,
                    coefficient_evaluation_seconds=budget.metadata["wall_seconds"]-training_cache_seconds,
                    rss_note="process lifetime peak; use a fresh process for per-run attribution")
    return (result, metadata) if return_metadata else result


def initialize_coefficients(params, inputs, order=6, **kwargs):
    """Training tensors; do this before expensive passive-circle initialization."""
    return initialize_probe_coefficients(params, inputs, inputs, order=order, **kwargs)


def initialize_antipodal_probe_coefficients(params, train_inputs, half_inputs, order=6, **kwargs):
    """Initialize supplied inputs and their EXACT negatives by oddness.

    The output query order is concatenate((half_inputs,-half_inputs)). This
    explicit API avoids silently identifying approximately opposite rows.
    No training input or training direction is added, removed or quotiented.
    """
    start = time.monotonic()
    with_metadata = kwargs.pop("return_metadata", False)
    values, metadata = initialize_probe_coefficients(params, train_inputs, half_inputs,
                                                     order, return_metadata=True, **kwargs)
    result = {name: np.concatenate((value, -value), axis=0) for name, value in values.items()}
    metadata.update(antipodal_reconstruction=True, computed_query_count=len(half_inputs),
                    query_count=2*len(half_inputs), coefficient_bytes=sum(v.nbytes for v in result.values()),
                    wall_seconds=time.monotonic()-start,
                    peak_process_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024,
                    probe_input_hash=array_hash(np.concatenate((half_inputs, -np.asarray(half_inputs)), axis=0)))
    if metadata["peak_process_rss_bytes"] >= kwargs.get("max_rss_bytes", RSS_LIMIT):
        raise InitializationLimit("peak_process_rss_bytes reached its cap during antipodal expansion", metadata)
    if metadata["wall_seconds"] >= kwargs.get("max_wall_seconds", 600.):
        raise InitializationLimit("wall_seconds reached its cap during antipodal expansion", metadata)
    return (result, metadata) if with_metadata else result

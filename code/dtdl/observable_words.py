"""Exact initialized observable words and their exhaustive natural encoding.

Scalars and deterministic bounds are Fractions. No numerical conversion,
arithmetic precision, rank decision, code ceiling or recursion-depth setting
enters this syntax module. Finite-resource policies belong to its callers.
"""
from fractions import Fraction
import math
import operator


def _integer(value, name, minimum=0):
    if isinstance(value, bool):
        raise ValueError(f"{name} must be an integer")
    try:
        result = operator.index(value)
    except TypeError as exc:
        raise ValueError(f"{name} must be an integer") from exc
    if result < minimum:
        raise ValueError(f"{name} must be at least {minimum}")
    return result


def _rational(value):
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise ValueError("initialized word scalars must be integers or Fractions")
    return Fraction(value)


class Word:
    """Immutable typed DAG node with exact bounds and literal syntax equality.

    Hashes are formed from already cached child hashes, never recursively.
    Equality traverses a stack of node pairs and memoizes repeated DAG pairs.
    Thus shared graphs are compared by their literal unfolded syntax without
    expanding their potentially exponential trees.
    """
    __slots__ = ("op", "population", "args", "scalar", "envelope", "_hash")

    def __init__(self, op, population, args=(), scalar=None):
        population = _integer(population, "population", 1)
        if population not in (1, 2):
            raise ValueError("population must be 1 or 2")
        args = tuple(args)
        arities = {"one": 0, "g1": 0, "g2": 0, "scale": 1,
                   "sin": 1, "cos": 1, "tanh": 1, "action": 1,
                   "add": 2, "multiply": 2}
        if op not in arities or len(args) != arities[op]:
            raise ValueError("unsupported initialized operation or arity")
        if any(not isinstance(arg, Word) for arg in args):
            raise ValueError("word operands must be exact initialized Words")
        if op in ("g1", "g2") and population != 1:
            raise ValueError("Gaussian seeds belong to population 1")
        if op == "action":
            if args[0].population != 3-population or not args[0].bounded:
                raise ValueError("actions require a bounded opposite-population word")
        elif any(arg.population != population for arg in args):
            raise ValueError("coordinate operations require one population")
        if op == "multiply" and not all(arg.bounded for arg in args):
            raise ValueError("products require bounded operands")
        if op == "scale":
            scalar = _rational(scalar)
        elif scalar is not None:
            raise ValueError("only scale words have a scalar")
        envelope = None
        if op in ("one", "sin", "cos", "tanh"):
            envelope = Fraction(1)
        elif op == "scale" and args[0].bounded:
            envelope = abs(scalar)*args[0].envelope
        elif op == "add" and all(arg.bounded for arg in args):
            envelope = args[0].envelope+args[1].envelope
        elif op == "multiply":
            envelope = args[0].envelope*args[1].envelope
        object.__setattr__(self, "op", op)
        object.__setattr__(self, "population", population)
        object.__setattr__(self, "args", args)
        object.__setattr__(self, "scalar", scalar)
        object.__setattr__(self, "envelope", envelope)
        object.__setattr__(self, "_hash", hash((op, population,
                                             tuple(arg._hash for arg in args), scalar)))

    def __setattr__(self, name, value):
        raise AttributeError("initialized Words are immutable")

    def __delattr__(self, name):
        raise AttributeError("initialized Words are immutable")

    @property
    def bounded(self):
        return self.envelope is not None

    def __hash__(self):
        return self._hash

    def __eq__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        pending, seen = [(self, other)], set()
        while pending:
            left, right = pending.pop()
            if left is right:
                continue
            pair = (id(left), id(right))
            if pair in seen:
                continue
            if (left._hash != right._hash or left.op != right.op
                    or left.population != right.population
                    or left.scalar != right.scalar or len(left.args) != len(right.args)):
                return False
            seen.add(pair)
            pending.extend(zip(left.args, right.args))
        return True

    def __repr__(self):
        # Summarize rather than recursively expanding a graph or formatting an
        # arbitrarily large rational through a decimal-integer string limit.
        return (f"Word(op={self.op!r}, population={self.population}, "
                f"arity={len(self.args)}, bounded={self.bounded})")


def constant(population):
    return Word("one", population)


def seed(name):
    if name not in ("g1", "g2"):
        raise ValueError("initialized Gaussian seed must be g1 or g2")
    return Word(name, 1)


def unary(op, word):
    if op not in ("sin", "cos", "tanh"):
        raise ValueError("unknown unary operation")
    return Word(op, word.population, (word,))


def add(left, right):
    return Word("add", left.population, (left, right))


def multiply(left, right):
    return Word("multiply", left.population, (left, right))


def scale(value, word):
    return Word("scale", word.population, (word,), _rational(value))


def action(word):
    return Word("action", 3-word.population, (word,))


def pair(a, b):
    a, b = _integer(a, "a"), _integer(b, "b")
    return (a+b)*(a+b+1)//2+b


def unpair(code):
    code = _integer(code, "code")
    total = (math.isqrt(8*code+1)-1)//2
    b = code-total*(total+1)//2
    return total-b, b


def rational_code(code):
    p, q = unpair(code)
    signed = 0 if p == 0 else (p+1)//2 if p % 2 else -(p//2)
    return Fraction(signed, q+1)


_DECODED = {0: constant(1), 1: constant(2), 2: seed("g1"), 3: seed("g2")}


def decode_word(code):
    """Decode the original natural-number grammar by an explicit stack.

    Only requested dependencies are decoded, even for a very large isolated
    code. Invalid codes cache None, exactly as in the established grammar.
    Dependencies have strictly smaller codes, so every finite request ends.
    """
    code = _integer(code, "word code")
    pending = [code]
    while pending:
        current = pending[-1]
        if current in _DECODED:
            pending.pop()
            continue
        k, op = divmod(current-4, 8)
        if op <= 3:
            dependencies = (k,)
        else:
            a, b = unpair(k)
            dependencies = (b,) if op == 6 else (a, b)
        missing = next((child for child in dependencies if child not in _DECODED), None)
        if missing is not None:
            pending.append(missing)
            continue
        operands = tuple(_DECODED[child] for child in dependencies)
        if any(operand is None for operand in operands):
            result = None
        else:
            try:
                if op <= 2:
                    result = unary(("sin", "cos", "tanh")[op], operands[0])
                elif op == 3:
                    result = action(operands[0])
                elif op == 6:
                    result = scale(rational_code(a), operands[0])
                elif op == 5:
                    result = multiply(*operands)
                else:
                    result = add(*operands)
            except ValueError:
                result = None
        _DECODED[current] = result
        pending.pop()
    return _DECODED[code]

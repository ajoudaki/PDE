"""Deterministic finite-width interpreter for the primitive typed language.

This module performs actual array arithmetic, with no Gaussian integration,
random sampling, symbolic differentiation, or call to the limit compiler.
Integer and Fraction inputs stay exact. Supplied matrices contain the actual
entries of W; the interpreter applies no extra 1/sqrt(n) scaling. Only mean()
introduces 1/n, and represented rank-one actions have already been lowered to
primitive operations by Program.call(). Vector results are immutable tuples.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from fractions import Fraction
from math import isfinite
from typing import Callable

from .mfp_compiler import Matrix, Node, ProgramError


Number = int | Fraction | float


def _number(value, location):
    if isinstance(value, Fraction):
        return value
    if type(value) is int:
        return Fraction(value)
    if type(value) is float and isfinite(value):
        return value
    raise ProgramError(f"{location} must contain finite int, Fraction, or float values")


def _vector(values, width, location):
    if (not isinstance(values, Sequence) or isinstance(values, (str, bytes))
            or len(values) != width):
        raise ProgramError(f"{location} must have length {width}")
    return tuple(_number(value, location) for value in values)


def evaluate_finite(
    output: Node,
    width: int,
    roots: Mapping[Node, Sequence[Number]],
    matrices: Mapping[Matrix, Sequence[Sequence[Number]]],
    parameters: Mapping[Node, Number] | None = None,
    activation: Callable[[int, Number], Number] | None = None,
):
    """Evaluate a scalar/vector primitive DAG at a supplied finite state.

    All reachable roots, named matrices, and scalar parameters require values;
    no declared initialization law supplies missing data. ``activation(r, x)``
    supplies the r-th activation derivative and is needed only for phi nodes.
    Freeze preserves its numerical value (its derivative rule lives elsewhere).
    Invalid widths, types, missing values, shapes, and operations raise
    ProgramError. Unused supplied entries are validated too.
    """
    if not isinstance(output, Node):
        raise ProgramError("Finite evaluation needs a program Node output")
    if type(width) is not int or width <= 0:
        raise ProgramError("Finite width must be a positive integer")
    program = output.program
    parameters = {} if parameters is None else parameters
    if not all(isinstance(mapping, Mapping) for mapping in (roots, matrices, parameters)):
        raise ProgramError("Roots, matrices, and parameters must be mappings")
    root_values, matrix_values, parameter_values = {}, {}, {}
    for node, values in roots.items():
        if not isinstance(node, Node) or node.program is not program or node.op != "root":
            raise ProgramError("Root data keys must be root leaves of this program")
        root_values[node] = _vector(values, width, f"Root {node.data!r}")
    for matrix, rows in matrices.items():
        if not isinstance(matrix, Matrix) or matrix.program is not program:
            raise ProgramError("Matrix data keys must be named matrices of this program")
        if (not isinstance(rows, Sequence) or isinstance(rows, (str, bytes))
                or len(rows) != width):
            raise ProgramError(f"Matrix {matrix.name!r} must have shape {width} by {width}")
        matrix_values[matrix] = tuple(
            _vector(row, width, f"Matrix {matrix.name!r} row") for row in rows)
    for node, value in parameters.items():
        if (not isinstance(node, Node) or node.program is not program
                or node.op != "parameter"):
            raise ProgramError("Parameter data keys must be scalar parameter leaves of this program")
        parameter_values[node] = _number(value, f"Parameter {node.data!r}")
    if activation is not None and not callable(activation):
        raise ProgramError("activation must be callable")

    cache, active = {}, set()

    def visit(node):
        if not isinstance(node, Node) or node.program is not program:
            raise ProgramError("Every expression node must belong to the output program")
        if node in cache:
            return cache[node]
        if node in active:
            raise ProgramError("Finite programs must be acyclic")
        active.add(node)
        args = tuple(visit(arg) for arg in node.args)
        if node.op == "const":
            value = _number(node.data.value, "Constant")
        elif node.op == "root":
            if node not in root_values:
                raise ProgramError(f"Missing finite values for root {node.data!r}")
            value = root_values[node]
        elif node.op == "parameter":
            if node not in parameter_values:
                raise ProgramError(f"Missing finite value for parameter {node.data!r}")
            value = parameter_values[node]
        elif node.op == "broadcast":
            value = (args[0],) * width
        elif node.op == "freeze":
            value = args[0]
        elif node.op in ("add", "mul"):
            left, right = args
            operation = ((lambda x, y: x + y) if node.op == "add"
                         else (lambda x, y: x * y))
            if node.kind is None:
                value = operation(left, right)
            else:
                left = left if node.args[0].kind is not None else (left,) * width
                right = right if node.args[1].kind is not None else (right,) * width
                value = tuple(operation(x, y) for x, y in zip(left, right))
        elif node.op == "phi":
            if activation is None:
                raise ProgramError("Finite evaluation of phi needs activation(order, x)")
            value = tuple(_number(activation(node.data, x), "Activation result") for x in args[0])
        elif node.op == "mean":
            value = sum(args[0], Fraction(0)) / width
        elif node.op == "matmul":
            matrix, transpose = node.data
            if matrix not in matrix_values:
                raise ProgramError(f"Missing finite values for matrix {matrix.name!r}")
            entries = matrix_values[matrix]
            value = tuple(sum(((entries[j][i] if transpose else entries[i][j]) * args[0][j]
                               for j in range(width)), Fraction(0)) for i in range(width))
        else:
            raise ProgramError(f"Unsupported finite operation {node.op!r}")
        active.remove(node)
        cache[node] = value
        return value

    return visit(output)

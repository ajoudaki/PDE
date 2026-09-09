"""Typed G0 compiler for the canonical one-sample dense MLP.

The notation labels an edge by its destination hidden layer: G_2 maps x_1
to h_2, ..., G_H maps x_{H-1} to h_H. This makes the automatically emitted
H=3 edge word directly readable as 2^- 3^- 3^+ 2^+.

This module proves no probabilistic limit. It only emits exact finite
algebra and syntactic proof obligations.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import argparse
import json
from typing import Iterable


@dataclass(frozen=True)
class ActivationSignature:
    """Only algebraically relevant activation flags belong at G0."""

    name: str
    second_derivative_zero: bool

    @classmethod
    def identity(cls) -> "ActivationSignature":
        return cls(name="identity", second_derivative_zero=True)

    @classmethod
    def nonlinear(cls, name: str = "generic_nonlinear") -> "ActivationSignature":
        return cls(name=name, second_derivative_zero=False)


@dataclass(frozen=True)
class CurvatureWord:
    """One summand in the same-time Hessian/backward-response recursion."""

    curvature_layer: int
    factors: tuple[str, ...]
    edge_word: tuple[str, ...]

    @property
    def colour_count(self) -> int:
        return len({token[:-1] for token in self.edge_word})

    @property
    def promotion_class(self) -> str:
        if not self.edge_word:
            return "local_diagonal"
        if self.colour_count == 1:
            return "one_colour_return"
        return "multi_colour_return"


@dataclass(frozen=True)
class CompiledMLP:
    hidden_depth: int
    activation: ActivationSignature
    forward_equations: tuple[str, ...]
    backward_equations: tuple[str, ...]
    feature_velocities: tuple[str, ...]
    raw_kernel_terms: tuple[str, ...]
    curvature_recursion: tuple[str, ...]
    curvature_words: tuple[CurvatureWord, ...]

    def to_dict(self) -> dict:
        data = asdict(self)
        for word in data["curvature_words"]:
            original = CurvatureWord(
                curvature_layer=word["curvature_layer"],
                factors=tuple(word["factors"]),
                edge_word=tuple(word["edge_word"]),
            )
            word["colour_count"] = original.colour_count
            word["promotion_class"] = original.promotion_class
        return data


def _forward(depth: int) -> tuple[str, ...]:
    lines = ["h_1 = u", "x_1 = phi(h_1)"]
    for layer in range(2, depth + 1):
        lines.extend(
            [
                f"h_{layer} = G_{layer} x_{layer - 1}",
                f"x_{layer} = phi(h_{layer})",
            ]
        )
    lines.append(f"f = <A, x_{depth}>_n")
    return tuple(lines)


def _backward(depth: int) -> tuple[str, ...]:
    lines = [f"b_{depth} = A * d_{depth}"]
    for layer in range(depth - 1, 0, -1):
        lines.extend(
            [
                f"v_{layer} = G_{layer + 1}^* b_{layer + 1}",
                f"b_{layer} = d_{layer} * v_{layer}",
            ]
        )
    return tuple(lines)


def _velocities(depth: int) -> tuple[str, ...]:
    lines = [f"A' = x_{depth}", "u' = b_1"]
    for destination in range(2, depth + 1):
        lines.append(
            f"G_{destination}' = b_{destination} tensor_n x_{destination - 1}"
        )
    return tuple(lines)


def _kernel(depth: int) -> tuple[str, ...]:
    terms = [f"||x_{depth}||_n^2", "||b_1||_n^2"]
    terms.extend(
        f"||b_{destination}||_n^2 ||x_{destination - 1}||_n^2"
        for destination in range(2, depth + 1)
    )
    return tuple(terms)


def _curvature_word(curvature_layer: int) -> CurvatureWord:
    """Expand the curvature source E_m down to the bottom layer.

    R_H = E_H and
    R_l = E_l + D_l G_{l+1}^* R_{l+1} G_{l+1} D_l.
    """

    if curvature_layer == 1:
        return CurvatureWord(
            curvature_layer=1,
            factors=("E_1",),
            edge_word=(),
        )

    left: list[str] = ["D_1"]
    edge_word: list[str] = []
    for destination in range(2, curvature_layer + 1):
        left.append(f"G_{destination}^*")
        edge_word.append(f"{destination}-")
        if destination < curvature_layer:
            left.append(f"D_{destination}")

    right: list[str] = []
    for destination in range(curvature_layer, 1, -1):
        right.append(f"G_{destination}")
        edge_word.append(f"{destination}+")
        right.append(f"D_{destination - 1}")

    return CurvatureWord(
        curvature_layer=curvature_layer,
        factors=tuple(left + [f"E_{curvature_layer}"] + right),
        edge_word=tuple(edge_word),
    )


def _curvature_recursion(depth: int) -> tuple[str, ...]:
    lines = [f"R_{depth} = E_{depth}"]
    for layer in range(depth - 1, 0, -1):
        lines.append(
            f"R_{layer} = E_{layer} + D_{layer} G_{layer + 1}^* "
            f"R_{layer + 1} G_{layer + 1} D_{layer}"
        )
    return tuple(lines)


def compile_mlp(
    hidden_depth: int, activation: ActivationSignature
) -> CompiledMLP:
    if hidden_depth < 1:
        raise ValueError("hidden_depth must be at least one")

    words: Iterable[CurvatureWord]
    if activation.second_derivative_zero:
        words = ()
    else:
        words = (
            _curvature_word(layer) for layer in range(1, hidden_depth + 1)
        )

    return CompiledMLP(
        hidden_depth=hidden_depth,
        activation=activation,
        forward_equations=_forward(hidden_depth),
        backward_equations=_backward(hidden_depth),
        feature_velocities=_velocities(hidden_depth),
        raw_kernel_terms=_kernel(hidden_depth),
        curvature_recursion=_curvature_recursion(hidden_depth),
        curvature_words=tuple(words),
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--depth", type=int, required=True)
    parser.add_argument(
        "--activation",
        choices=("identity", "arctan", "generic_nonlinear"),
        required=True,
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    activation = (
        ActivationSignature.identity()
        if args.activation == "identity"
        else ActivationSignature.nonlinear(args.activation)
    )
    print(json.dumps(compile_mlp(args.depth, activation).to_dict(), indent=2))


if __name__ == "__main__":
    main()


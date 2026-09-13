"""Exact finite descriptions and midpoint rules for the proposed H4 arc laws.

No trajectory, Gaussian initialization or theorem verification occurs here.
The normalized input is U(r*s)=((1-r*r*s*s)/(1+r*r*s*s),
2*r*s/(1+r*r*s*s)); the negative cluster is its quarter-turn rotation.
Both clusters have mass 1/2 and labels +1,-1. Endpoints lie in [-1,1].

The law remains fixed as numerical precision changes. A radius too small for
the declared working precision may be replaced by zero in the returned rule,
with that approximation explicitly reported and bounded in exact metadata.
The exact positive symbolic radius is always retained. For each fixed finite
exponent, increasing precision eventually leaves that branch, provided the
caller also raises finite resource limits enough to permit the requested work.

Bounds concern the exact rational input rule before arithmetic conversion.
Metadata separately records coordinate/probability rounding bounds. Neither
these representation bounds nor a scope tag is a trajectory error certificate.
"""
from dataclasses import asdict, dataclass
from fractions import Fraction
import json

import numpy as np

from pde.observable_solver import DataLaw


class LawResourceLimit(ValueError):
    """The exact requested finite operation exceeds an adjustable allowance."""


def _count(value, name, minimum=1):
    if type(value) is not int or value < minimum:
        raise ValueError(name + " must be an integer at least " + str(minimum))
    return value


def _rational(value):
    if isinstance(value, bool) or not isinstance(value, (int, Fraction, str)):
        raise ValueError("exact law parameters require integers, Fractions or rational strings")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError("invalid exact rational parameter") from exc


def _fraction_record(value):
    value = Fraction(value)
    return dict(numerator=hex(value.numerator), denominator=hex(value.denominator))


def _fraction_from_record(value):
    if not isinstance(value, dict) or set(value) != {"numerator", "denominator"}:
        raise ValueError("invalid exact rational record")
    if not all(isinstance(value[k], str) for k in value):
        raise ValueError("hexadecimal rational fields must be strings")
    numerator, denominator = int(value["numerator"], 16), int(value["denominator"], 16)
    if denominator <= 0:
        raise ValueError("rational denominator must be positive")
    return Fraction(numerator, denominator)


@dataclass(frozen=True)
class LawLimits:
    max_expression_nodes: int = 1024
    max_expression_depth: int = 64
    max_literal_bits: int = 16384
    max_exact_scalar_bits: int = 65536
    max_rule_nodes: int = 100000

    def __post_init__(self):
        for name in self.__dataclass_fields__:
            _count(getattr(self, name), name)


@dataclass(frozen=True)
class IntegerExpression:
    """A positive integer described by literal, add, multiply or pow2 nodes.

    ``bounded_value(cap)`` returns the exact integer if it is at most cap,
    otherwise cap+1. It does not form a huge intermediate integer merely to
    determine that it exceeds the cap. Literal records use hexadecimal strings.
    """
    op: str
    value: object = None
    args: tuple = ()

    def __post_init__(self):
        object.__setattr__(self, "args", tuple(self.args))
        if self.op == "integer":
            _count(self.value, "positive integer literal")
            if self.args:
                raise ValueError("literal cannot have children")
        elif self.op in ("add", "multiply", "pow2"):
            expected = 1 if self.op == "pow2" else 2
            if self.value is not None or len(self.args) != expected:
                raise ValueError("invalid integer expression arity")
            if not all(isinstance(arg, IntegerExpression) for arg in self.args):
                raise ValueError("integer expression children must be IntegerExpression objects")
        else:
            raise ValueError("unknown positive integer expression operation")

    @classmethod
    def integer(cls, value):
        return cls("integer", value)

    @classmethod
    def pow2(cls, exponent):
        return cls("pow2", args=(_expression(exponent),))

    @classmethod
    def add(cls, first, second):
        return cls("add", args=(_expression(first), _expression(second)))

    @classmethod
    def multiply(cls, first, second):
        return cls("multiply", args=(_expression(first), _expression(second)))

    def validate(self, limits=None):
        limits = limits or LawLimits()
        stack, nodes = [(self, 1)], 0
        while stack:
            current, depth = stack.pop()
            nodes += 1
            if nodes > limits.max_expression_nodes or depth > limits.max_expression_depth:
                raise LawResourceLimit("symbolic exponent exceeds its node/depth allowance")
            if current.op == "integer" and current.value.bit_length() > limits.max_literal_bits:
                raise LawResourceLimit("symbolic exponent literal exceeds max_literal_bits")
            stack.extend((child, depth+1) for child in current.args)
        return self

    def bounded_value(self, cap, *, limits=None):
        _count(cap, "comparison cap", minimum=0)
        self.validate(limits)

        def evaluate(node, ceiling):
            if ceiling == 0:
                return 1
            if node.op == "integer":
                return min(node.value, ceiling+1)
            if node.op == "pow2":
                bit_count = ceiling.bit_length()
                exponent = evaluate(node.args[0], bit_count)
                return ceiling+1 if exponent >= bit_count else 1 << exponent
            first = evaluate(node.args[0], ceiling)
            if first > ceiling:
                return ceiling+1
            if node.op == "add":
                second = evaluate(node.args[1], ceiling-first)
                return min(first+second, ceiling+1)
            second = evaluate(node.args[1], ceiling//first)
            return min(first*second, ceiling+1)

        return evaluate(self, cap)

    def to_record(self, *, limits=None):
        self.validate(limits)

        def encode(node):
            if node.op == "integer":
                return dict(op=node.op, value=hex(node.value))
            return dict(op=node.op, args=[encode(child) for child in node.args])

        return encode(self)

    @classmethod
    def from_record(cls, record, *, limits=None):
        limits = limits or LawLimits()
        used = 0

        def decode(value, depth):
            nonlocal used
            used += 1
            if used > limits.max_expression_nodes or depth > limits.max_expression_depth:
                raise LawResourceLimit("symbolic record exceeds node/depth allowance")
            if not isinstance(value, dict):
                raise ValueError("integer expression record must be a mapping")
            if value.get("op") == "integer" and set(value) == {"op", "value"}:
                literal = value["value"]
                if not isinstance(literal, str):
                    raise ValueError("integer literal must be a hexadecimal string")
                if len(literal) > (limits.max_literal_bits+3)//4+3:
                    raise LawResourceLimit("encoded integer literal exceeds its allowance")
                return cls.integer(int(literal, 16))
            if set(value) != {"op", "args"} or not isinstance(value["args"], list):
                raise ValueError("invalid integer expression record")
            return cls(value["op"], args=tuple(decode(child, depth+1) for child in value["args"]))

        return decode(record, 1).validate(limits)


def _expression(value):
    return value if isinstance(value, IntegerExpression) else IntegerExpression.integer(value)


@dataclass(frozen=True)
class DyadicRadius:
    """The exact positive radius 2**(-exponent), without expanding it."""
    exponent: IntegerExpression

    def __post_init__(self):
        object.__setattr__(self, "exponent", _expression(self.exponent))

    def to_record(self, *, limits=None):
        return dict(kind="dyadic", exponent=self.exponent.to_record(limits=limits))

    def below_binary(self, power, *, limits=None):
        # Strict comparison 2**(-E) < 2**(-power) is E > power.
        return self.exponent.bounded_value(power, limits=limits) > power

    def materialize(self, *, limits=None):
        limits = limits or LawLimits()
        exponent = self.exponent.bounded_value(limits.max_exact_scalar_bits-1, limits=limits)
        if exponent >= limits.max_exact_scalar_bits:
            raise LawResourceLimit("dyadic denominator exceeds max_exact_scalar_bits")
        return Fraction(1, 1 << exponent)


@dataclass(frozen=True)
class RationalRadius:
    """An arbitrary positive exact rational radius; scientific use is exploratory."""
    value: Fraction

    def __post_init__(self):
        value = _rational(self.value)
        if value <= 0:
            raise ValueError("radius must be positive")
        object.__setattr__(self, "value", value)

    def to_record(self, *, limits=None):
        self.materialize(limits=limits)
        return dict(kind="rational", value=_fraction_record(self.value))

    def below_binary(self, power, *, limits=None):
        limits = limits or LawLimits()
        self.materialize(limits=limits)
        if power+1 > limits.max_exact_scalar_bits:
            raise LawResourceLimit("precision comparison exceeds max_exact_scalar_bits")
        return self.value < Fraction(1, 1 << power)

    def materialize(self, *, limits=None):
        limits = limits or LawLimits()
        if max(abs(self.value.numerator).bit_length(), self.value.denominator.bit_length()) > limits.max_exact_scalar_bits:
            raise LawResourceLimit("rational radius exceeds max_exact_scalar_bits")
        return self.value


def radius_from_record(record, *, limits=None):
    if not isinstance(record, dict):
        raise ValueError("radius record must be a mapping")
    if set(record) == {"kind", "exponent"} and record["kind"] == "dyadic":
        return DyadicRadius(IntegerExpression.from_record(record["exponent"], limits=limits))
    if set(record) == {"kind", "value"} and record["kind"] == "rational":
        result = RationalRadius(_fraction_from_record(record["value"]))
        result.materialize(limits=limits)
        return result
    raise ValueError("unsupported exact radius record")


def _represented(value, arithmetic):
    # float(Fraction) avoids overflowing its numerator/denominator separately.
    # No binary conversion enters either arbitrary-precision backend.
    return arithmetic.real(float(value) if arithmetic.digits is None else value)


@dataclass(frozen=True)
class OrthogonalArcLaw:
    """Equal-mass rational-parametrized arcs around e1 and e2.

    Each nondegenerate interval defines a nonatomic component because U(r*s)
    is injective for r>0. A degenerate interval defines an atom. The radius
    is fixed by the exact description, never selected from numerical results.
    The optional scope label is provenance supplied by the caller, not proof.
    """
    radius: object
    a: Fraction = Fraction(-1)
    b: Fraction = Fraction(1)
    c: Fraction = Fraction(-1)
    d: Fraction = Fraction(1)
    scope_tag: str = "H4_symbolic_candidate_theorem_scope_pending"

    def __post_init__(self):
        if not isinstance(self.radius, (DyadicRadius, RationalRadius)):
            raise ValueError("radius must be DyadicRadius or RationalRadius")
        for key in ("a", "b", "c", "d"):
            object.__setattr__(self, key, _rational(getattr(self, key)))
        if not -1 <= self.a <= self.b <= 1 or not -1 <= self.c <= self.d <= 1:
            raise ValueError("arc endpoints must be ordered and in [-1,1]")
        if not isinstance(self.scope_tag, str) or not self.scope_tag or len(self.scope_tag) > 512:
            raise ValueError("scope_tag must be a nonempty string of at most 512 characters")
        if isinstance(self.radius, RationalRadius):
            object.__setattr__(self, "scope_tag", "exploratory_rational_radius_no_T40_guarantee")

    def exact_description(self, *, limits=None):
        limits = limits or LawLimits()
        for value in (self.a, self.b, self.c, self.d):
            if max(abs(value.numerator).bit_length(), value.denominator.bit_length()) > limits.max_exact_scalar_bits:
                raise LawResourceLimit("interval endpoint exceeds max_exact_scalar_bits")
        return dict(format="h4-orthogonal-arcs-v1", radius=self.radius.to_record(limits=limits),
                    endpoints={key: _fraction_record(getattr(self, key)) for key in ("a", "b", "c", "d")},
                    mass_per_component=_fraction_record(Fraction(1, 2)),
                    labels=[1, -1], second_rotation=[[0, -1], [1, 0]],
                    scope_tag=self.scope_tag)

    @classmethod
    def from_description(cls, record, *, limits=None):
        required = {"format", "radius", "endpoints", "mass_per_component", "labels", "second_rotation", "scope_tag"}
        if not isinstance(record, dict) or set(record) != required or record["format"] != "h4-orthogonal-arcs-v1":
            raise ValueError("unsupported exact law schema")
        if (record["mass_per_component"] != _fraction_record(Fraction(1, 2))
                or record["labels"] != [1, -1] or record["second_rotation"] != [[0, -1], [1, 0]]):
            raise ValueError("law schema has different masses, labels or rotation")
        if not isinstance(record["endpoints"], dict) or set(record["endpoints"]) != {"a", "b", "c", "d"}:
            raise ValueError("invalid interval schema")
        result = cls(radius_from_record(record["radius"], limits=limits),
                     **{key: _fraction_from_record(value) for key, value in record["endpoints"].items()},
                     scope_tag=record["scope_tag"])
        result.exact_description(limits=limits)
        return result

    def quadrature(self, nodes_per_arc, arithmetic, *, limits=None, allow_collapse=True):
        """Return a DataLaw with exact law/refinement/collapse provenance.

        Collapse uses E>4*(p+8)+2 for p decimal digits (p=17 for float64).
        Then r<2**(-cutoff) and every input changes by at most 2*r,
        less than 10**(-p-8). This is an explicit approximation, not a claim
        that tiny nonzero coordinates round to zero in floating arithmetic.
        With allow_collapse=False an unmaterializable radius raises instead.
        """
        limits = limits or LawLimits()
        _count(nodes_per_arc, "nodes_per_arc")
        if not isinstance(allow_collapse, bool):
            raise ValueError("allow_collapse must be boolean")
        exact = self.exact_description(limits=limits)
        counts = [1 if left == right else nodes_per_arc for left, right in ((self.a, self.b), (self.c, self.d))]
        if sum(counts) > limits.max_rule_nodes:
            raise LawResourceLimit("quadrature exceeds max_rule_nodes")
        digits = 17 if arithmetic.digits is None else arithmetic.digits
        precision_bits = 4*digits+64
        if precision_bits > limits.max_exact_scalar_bits:
            raise LawResourceLimit("working-precision scalar estimate exceeds max_exact_scalar_bits")
        cutoff = 4*(digits+8)+2
        collapsed = allow_collapse and self.radius.below_binary(cutoff, limits=limits)
        radius = None if collapsed else self.radius.materialize(limits=limits)
        endpoint_bits = max(max(abs(v.numerator).bit_length(), v.denominator.bit_length())
                            for v in (self.a, self.b, self.c, self.d))
        anticipated = 0
        # Rational products below cannot exceed this deliberately loose bit cap.
        # It covers midpoint construction, r*s, squaring and rational U.
        if radius is not None:
            radius_bits = max(abs(radius.numerator).bit_length(), radius.denominator.bit_length())
            anticipated = 16*(radius_bits+endpoint_bits+nodes_per_arc.bit_length()+4)
            if anticipated > limits.max_exact_scalar_bits:
                raise LawResourceLimit("exact midpoint coordinate arithmetic exceeds max_exact_scalar_bits")
        # Exact rounding bounds are measured against each intended rational value.
        inputs, labels, weights = [], [], []
        coordinate_rounding, weight_rounding = Fraction(0), Fraction(0)
        all_working_reference, exact_midpoint_nonreference = True, False
        reference_coordinate_rounding_count = 0
        with arithmetic.context():
            for index, (left, right, count) in enumerate(((self.a, self.b, counts[0]), (self.c, self.d, counts[1]))):
                for j in range(count):
                    if collapsed:
                        u, v = Fraction(1), Fraction(0)
                    else:
                        s = left+(right-left)*Fraction(2*j+1, 2*count)
                        z = radius*s
                        u, v = (1-z*z)/(1+z*z), 2*z/(1+z*z)
                    if index == 1:
                        u, v = -v, u
                    reference = (Fraction(1), Fraction(0)) if index == 0 else (Fraction(0), Fraction(1))
                    represented = [_represented(value, arithmetic) for value in (u, v)]
                    exact_midpoint_nonreference |= (u, v) != reference
                    all_working_reference &= all(got == ref for got, ref in zip(represented, reference))
                    reference_coordinate_rounding_count += sum(
                        wanted != ref and got == ref
                        for wanted, got, ref in zip((u, v), represented, reference))
                    coordinate_rounding = max(coordinate_rounding, sum(
                        abs(_working_fraction(got)-wanted) for got, wanted in zip(represented, (u, v))))
                    weight = Fraction(1, 2*count)
                    represented_weight = _represented(weight, arithmetic)
                    weight_rounding += abs(_working_fraction(represented_weight)-weight)
                    inputs.append(represented)
                    labels.append(arithmetic.real(1 if index == 0 else -1))
                    weights.append(represented_weight)
        quadrature_coefficient = ((self.b-self.a)+(self.d-self.c))/Fraction(4*nodes_per_arc)
        collapse_coefficient = (max(abs(self.a), abs(self.b))+max(abs(self.c), abs(self.d))) if collapsed else Fraction(0)
        bound = dict(kind="coefficient_times_exact_radius", radius=exact["radius"],
                     coefficient=_fraction_record(quadrature_coefficient+collapse_coefficient))
        rounding_collapse = exact_midpoint_nonreference and all_working_reference
        metadata = dict(
            exact_law=exact, quadrature_rule="componentwise_uniform_midpoints-v1",
            nodes_per_arc=nodes_per_arc, returned_component_node_counts=counts,
            component_is_nonatomic=[self.a < self.b, self.c < self.d],
            collapsed_to_reference=collapsed or rounding_collapse,
            collapse_reason=("radius below declared precision cutoff" if collapsed else
                             "nonreference exact midpoint rule rounds to reference" if rounding_collapse else None),
            radius_replaced_by_zero=collapsed,
            exact_midpoint_rule_collapsed_by_rounding=rounding_collapse,
            all_working_inputs_are_reference=all_working_reference,
            reference_coordinate_rounding_count=reference_coordinate_rounding_count,
            collapse_binary_cutoff=cutoff if collapsed else None,
            collapse_is_explicit_approximation=True if collapsed else False,
            radius_used_in_coordinate_arithmetic=not collapsed,
            dyadic_denominator_materialized=(not collapsed) if isinstance(self.radius, DyadicRadius) else None,
            exact_midpoint_transport_coefficient=_fraction_record(quadrature_coefficient),
            radius_replacement_transport_coefficient=_fraction_record(collapse_coefficient),
            exact_rule_transport_bound=bound,
            transport_metric="Euclidean normalized direction plus absolute label difference",
            transport_bound_scope="Exact rational midpoint/reference rule before scalar rounding; not flow error",
            maximum_coordinate_rounding_l1=_fraction_record(coordinate_rounding),
            total_probability_rounding_l1=_fraction_record(weight_rounding),
            rounded_rule_normalized_transport_addition=_fraction_record(coordinate_rounding+8*weight_rounding),
            rounded_transport_scope="After normalizing returned weights only for probability-law interpretation; weights in the dynamics remain unchanged",
            scientific_scope=self.scope_tag,
            scope_authority="caller-supplied provenance label; this module verifies no population theorem",
            arithmetic_backend="float64" if arithmetic.digits is None else arithmetic.backend,
            arithmetic_digits=arithmetic.digits,
            exact_description_utf8_bytes=len(json.dumps(exact, separators=(",", ":")).encode("utf-8")),
            estimated_exact_coordinate_working_bits=anticipated,
            estimated_precision_scalar_bits=precision_bits,
            resource_limits=asdict(limits),
        )
        return DataLaw(np.asarray(inputs, dtype=arithmetic.dtype), np.asarray(labels, dtype=arithmetic.dtype),
                       np.asarray(weights, dtype=arithmetic.dtype), metadata).validate(arithmetic)


def _working_fraction(value):
    if hasattr(value, "fraction"):
        return value.fraction()
    # Includes exact conversion from a represented binary float or Decimal.
    return Fraction(value)


def supported_radius():
    """Fixed radius of C.4.7.10.D: E0=8192, E(j+1)=2**Ej, rho=2**(-E10).

    This builds eleven small syntax nodes, never the expanded exponent. The
    radius is independent of every numerical-resolution and resource argument.
    """
    exponent = IntegerExpression.integer(8192)
    for _ in range(10):
        exponent = IntegerExpression.pow2(exponent)
    return DyadicRadius(exponent)


def supported_law(*, a=-1, b=1, c=-1, d=1):
    """The fixed-radius binary law proved in C.4.7.10.D.

    Rational interval endpoints lie in [-1,1]; equal endpoints denote atoms.
    For example a=b=0,c=d=1 gives a nonorthogonal atomic law. Nondegenerate
    intervals give nonatomic components. Working precision may collapse their
    tiny perturbation; quadrature reports that approximation explicitly.
    """
    return OrthogonalArcLaw(supported_radius(), a=a, b=b, c=c, d=d,
                            scope_tag="H4_explicit_supported_T40")


# Transport accounting used above:
# U has |U'(z)|=2/(1+z*z), so |U(r*s)-U(r*t)|<=2*r*|s-t|.
# Uniform-to-midpoint mean |s-t| is (b-a)/(4*m); both component masses are
# 1/2. Replacing each midpoint by its cluster center costs at most
# r*(max(|a|,|b|)+max(|c|,|d|)). Their sum is the symbolic coefficient.
# For arithmetic rounding let e be the largest coordinate L1 error and let
# rho=sum_i |q_i-w_i|, where w are exact midpoint weights and q>=0 are the
# returned weights with positive total. Normalizing q only for interpretation
# gives sum_i |q_i/sum(q)-w_i| <= 2*rho. Every exact/rounded coordinate is
# in [-1,1], and labels are +/-1, so diameter in the stated metric is <8.
# Coupling each original point to its rounded point and then redistributing
# at most rho mass proves the additional bound e+8*rho. It does not modify
# vector-field weights. For Fixed and Decimal these errors use exact rational
# conversions of the working values, not a float64 diagnostic.

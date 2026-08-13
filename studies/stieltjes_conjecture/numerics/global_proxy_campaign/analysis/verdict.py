"""Fail-closed protocol decision rules.

The numerical constants are never chosen here.  A frozen protocol must supply
``DecisionThresholds``; absent thresholds cannot silently inherit defaults in
scientific production.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

from .comparison import BracketComparison


@dataclass(frozen=True)
class DecisionThresholds:
    confidence: float
    maximum_reference_to_bracket_width_ratio: float | None
    maximum_width_model_log_disagreement: float
    maximum_width_fit_relative_residual: float
    maximum_bootstrap_invalid_fraction: float
    maximum_relative_standard_error: float
    maximum_relative_jensen_gap: float
    maximum_transverse_leakage: float | None
    require_scientific_admissibility: bool = True

    @classmethod
    def from_mapping(cls, values: Mapping[str, Any]) -> "DecisionThresholds":
        required = {
            "confidence",
            "maximum_reference_to_bracket_width_ratio",
            "maximum_width_model_log_disagreement",
            "maximum_width_fit_relative_residual",
            "maximum_bootstrap_invalid_fraction",
            "maximum_relative_standard_error",
            "maximum_relative_jensen_gap",
            "maximum_transverse_leakage",
        }
        missing = sorted(required - values.keys())
        if missing:
            raise ValueError(f"protocol decision thresholds are missing {missing}")
        return cls(
            confidence=float(values["confidence"]),
            maximum_reference_to_bracket_width_ratio=(
                None
                if values["maximum_reference_to_bracket_width_ratio"] is None
                else float(values["maximum_reference_to_bracket_width_ratio"])
            ),
            maximum_width_model_log_disagreement=float(
                values["maximum_width_model_log_disagreement"]
            ),
            maximum_width_fit_relative_residual=float(
                values["maximum_width_fit_relative_residual"]
            ),
            maximum_bootstrap_invalid_fraction=float(
                values["maximum_bootstrap_invalid_fraction"]
            ),
            maximum_relative_standard_error=float(
                values["maximum_relative_standard_error"]
            ),
            maximum_relative_jensen_gap=float(values["maximum_relative_jensen_gap"]),
            maximum_transverse_leakage=(
                None
                if values["maximum_transverse_leakage"] is None
                else float(values["maximum_transverse_leakage"])
            ),
            require_scientific_admissibility=bool(
                values.get("require_scientific_admissibility", True)
            ),
        )


@dataclass(frozen=True)
class Decision:
    status: str
    reason: str
    validity_gates: Mapping[str, bool]


def decide_bracket(
    bracket: BracketComparison,
    *,
    thresholds: DecisionThresholds,
    evidence_admissible: bool,
    bootstrap_confidence: float,
    bootstrap_invalid_fraction: float,
    maximum_relative_standard_error: float,
    maximum_relative_jensen_gap: float,
    maximum_width_model_log_disagreement: float,
    maximum_width_fit_relative_residual: float,
    transverse_leakage: float | None,
    two_largest_widths_repeat_escape: bool = True,
) -> Decision:
    """Apply numerical-validity gates before the scientific discriminator."""

    gates = {
        "scientific_evidence_admissible": (
            evidence_admissible or not thresholds.require_scientific_admissibility
        ),
        "confidence_matches_protocol": abs(
            bootstrap_confidence - thresholds.confidence
        ) <= 8.0e-15,
        "bootstrap_validity": (
            bootstrap_invalid_fraction
            <= thresholds.maximum_bootstrap_invalid_fraction
        ),
        "relative_standard_error": (
            maximum_relative_standard_error
            <= thresholds.maximum_relative_standard_error
        ),
        "jensen_gap": (
            maximum_relative_jensen_gap <= thresholds.maximum_relative_jensen_gap
        ),
        "width_model_sensitivity": (
            maximum_width_model_log_disagreement
            <= thresholds.maximum_width_model_log_disagreement
        ),
        "width_fit_residual": (
            maximum_width_fit_relative_residual
            <= thresholds.maximum_width_fit_relative_residual
        ),
        "transverse_leakage": (
            True
            if thresholds.maximum_transverse_leakage is None
            else transverse_leakage is not None
            and transverse_leakage <= thresholds.maximum_transverse_leakage
        ),
    }
    failed_gates = [name for name, passed in gates.items() if not passed]
    if failed_gates:
        return Decision(
            "inconclusive",
            "numerical validity gate failed: " + ", ".join(failed_gates),
            gates,
        )
    if bracket.containment_status == "fail":
        if not two_largest_widths_repeat_escape:
            return Decision(
                "inconclusive",
                "extrapolated escape is not repeated with the same sign at both largest widths",
                gates,
            )
        return Decision(
            "fail",
            "the simultaneous reference band is definitely outside the proxy bracket",
            gates,
        )
    if bracket.containment_status != "pass":
        return Decision(
            "inconclusive",
            "the simultaneous reference band overlaps a proxy boundary",
            gates,
        )
    if (
        thresholds.maximum_reference_to_bracket_width_ratio is not None
        and bracket.reference_to_bracket_width_ratio
        > thresholds.maximum_reference_to_bracket_width_ratio
    ):
        return Decision(
            "inconclusive",
            "reference uncertainty is too large relative to this proxy bracket",
            gates,
        )
    return Decision(
        "pass",
        "the resolved simultaneous reference band is contained in the proxy bracket",
        gates,
    )


def decide_protocol_bracket(
    bracket: BracketComparison,
    *,
    validity_gates: Mapping[str, bool],
    two_largest_escape_directions: tuple[str, str] | None,
) -> Decision:
    """Apply the frozen protocol's exact prefix classifier.

    ``pass`` means protocol-compatible, while ``fail`` means protocol-contrary.
    A definite extrapolated escape is still inconclusive unless the two
    largest valid finite widths repeat the same nonzero signed escape.
    """

    failed = [name for name, passed in validity_gates.items() if not passed]
    if failed:
        return Decision(
            "inconclusive",
            "mandatory protocol gate failed: " + ", ".join(failed),
            validity_gates,
        )
    if bracket.containment_status == "pass":
        return Decision(
            "pass",
            "complete 99% simultaneous sensitivity-union band is inside the bracket",
            validity_gates,
        )
    if bracket.containment_status != "fail":
        return Decision(
            "inconclusive",
            "reference band overlaps at least one rational boundary",
            validity_gates,
        )
    if two_largest_escape_directions is None:
        return Decision(
            "inconclusive",
            "two-largest-width signed escape confirmation is unavailable",
            validity_gates,
        )
    left, right = two_largest_escape_directions
    if left == right == bracket.definite_escape_direction and left in {"above", "below"}:
        return Decision(
            "fail",
            "same signed bracket escape occurs in the union and both largest widths",
            validity_gates,
        )
    return Decision(
        "inconclusive",
        "same signed escape is absent at one or both largest widths",
        validity_gates,
    )

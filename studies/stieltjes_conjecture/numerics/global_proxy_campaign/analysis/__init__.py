"""Evidence-preserving postprocessing for the global proxy campaign.

The package is deliberately side-effect free on import.  In particular it
does not discover or inspect anything below ``reference/runs`` on its own.
Callers must supply an explicit ``summary.json`` path.
"""

from .bootstrap import BootstrapBand, PointBootstrap, bootstrap_point
from .comparison import ProxyComparison, compare_proxy_hierarchy
from .reference_data import ReferencePoint, ReferenceRun, load_reference_run
from .verdict import (
    Decision,
    DecisionThresholds,
    decide_bracket,
    decide_protocol_bracket,
)
from .width import (
    UnionWidthReference,
    WidthEstimate,
    extrapolate_widths,
    union_width_estimates,
)

__all__ = (
    "BootstrapBand",
    "Decision",
    "DecisionThresholds",
    "PointBootstrap",
    "ProxyComparison",
    "ReferencePoint",
    "ReferenceRun",
    "UnionWidthReference",
    "WidthEstimate",
    "bootstrap_point",
    "compare_proxy_hierarchy",
    "decide_bracket",
    "decide_protocol_bracket",
    "extrapolate_widths",
    "load_reference_run",
    "union_width_estimates",
)

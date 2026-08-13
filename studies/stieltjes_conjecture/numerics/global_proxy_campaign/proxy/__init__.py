"""Deterministic Stieltjes proxy hierarchy for the global-curve campaign.

The package deliberately contains no finite-width simulator and launches no
experiments on import.  It turns already accepted exact jets into conditional
Stieltjes rational proxies and supplies the exactly solvable variance-boundary
reference used to calibrate those proxies.
"""

from .hierarchy import (
    KernelApproximation,
    KernelBracket,
    build_kernel_brackets,
    build_kernel_hierarchy,
    stieltjes_s_fraction,
)
from .inventory import evaluate_family, family_inventory

__all__ = [
    "KernelApproximation",
    "KernelBracket",
    "build_kernel_brackets",
    "build_kernel_hierarchy",
    "evaluate_family",
    "family_inventory",
    "stieltjes_s_fraction",
]

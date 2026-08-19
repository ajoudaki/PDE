"""Exact finite-width jets and audited fixed-depth Gaussian recursions."""

from .finite_width_jet import DepthJet, feature_ascent_jet
from .gnf_recursion import DepthB1GNF, LayerGNFState, evaluate_depth_b1_gnf
from .model import DepthState, sample_state

__all__ = [
    "DepthB1GNF",
    "DepthJet",
    "DepthState",
    "LayerGNFState",
    "evaluate_depth_b1_gnf",
    "feature_ascent_jet",
    "sample_state",
]

"""Finite neural-network dynamics and exact rational Gaussian moments."""

from .finite_network import (
    ARCTAN,
    IDENTITY,
    TANH,
    Activation,
    ForwardPass,
    Parameters,
    backward,
    flow_velocity,
    forward,
    gd_step,
    initialize,
    kernel,
    kernel_blocks,
    loss,
    loss_gradients,
)
from .gaussian_moments import gaussian_moment

__all__ = [
    "ARCTAN", "IDENTITY", "TANH", "Activation", "ForwardPass", "Parameters",
    "backward", "flow_velocity", "forward", "gd_step", "initialize", "kernel",
    "kernel_blocks", "loss", "loss_gradients", "gaussian_moment",
]

"""Adaptive, never-forget conditional queries to W ~ N(0, 1/n).

Rows of x are query vectors. This module approximates a sequence of matrix
actions, not necessarily the gradient of one conditional-mean network: a later
query may enrich the transcript. Zero tolerance reveals every nonzero residual
up to a roundoff floor. The complete retained transcript has a Gaussian matrix
completion, including after adaptively skipped queries. See GAUSSIAN_QUERY_THEORY.

No manuscript code or other study implementation is imported.
"""
from __future__ import annotations

import math
import torch


class DeferredGaussian:
    def __init__(self, n, *, tolerance, seed, device="cpu", dtype=torch.float64,
                 rank_cap=None, initial_capacity=16, record_queries=False):
        self.n = int(n)
        self.tolerance = float(tolerance)
        if self.n < 1 or self.tolerance < 0:
            raise ValueError("positive dimension and nonnegative tolerance required")
        self.device = torch.device(device)
        self.dtype = dtype
        self.rank_cap = min(self.n, self.n if rank_cap is None else int(rank_cap))
        self.generator = torch.Generator(device=self.device).manual_seed(int(seed))
        cap = min(self.rank_cap, max(1, int(initial_capacity)))
        self.U = torch.empty((self.n, cap), device=self.device, dtype=dtype)
        self.Y = torch.empty_like(self.U)
        self.V = torch.empty_like(self.U)
        self.Z = torch.empty_like(self.U)
        self.r = self.s = 0
        self.calls = self.queries = 0
        self.max_remaining_rms = 0.0
        self.record_queries = record_queries
        self.records = []

    @staticmethod
    def _residual(x, basis):
        # Twice modified projection; basis columns are orthonormal.
        e = x - (x @ basis) @ basis.T
        return e - (e @ basis) @ basis.T

    def _grow(self, right):
        names = ("U", "Y") if right else ("V", "Z")
        rank = self.r if right else self.s
        capacity = getattr(self, names[0]).shape[1]
        if rank < capacity:
            return
        if rank >= self.rank_cap:
            raise RuntimeError(f"conditioning rank cap {self.rank_cap} exhausted")
        new_capacity = min(self.rank_cap, max(capacity + 1, 2 * capacity))
        for name in names:
            old = getattr(self, name)
            new = torch.empty((self.n, new_capacity), device=self.device,
                              dtype=self.dtype)
            new[:, :rank].copy_(old[:, :rank])
            setattr(self, name, new)

    def _append(self, direction, right):
        self._grow(right)
        U, V = self.U[:, :self.r], self.V[:, :self.s]
        Y, Z = self.Y[:, :self.r], self.Z[:, :self.s]
        noise = torch.randn(self.n, generator=self.generator,
                            device=self.device, dtype=self.dtype) / math.sqrt(self.n)
        if right:
            # W u = V Z^T u + (I - VV^T) g/sqrt(n).
            action = V @ (Z.T @ direction) + self._residual(noise, V)
            self.U[:, self.r].copy_(direction)
            self.Y[:, self.r].copy_(action)
            self.r += 1
        else:
            # W^T v = U Y^T v + (I - UU^T) g/sqrt(n).
            action = U @ (Y.T @ direction) + self._residual(noise, U)
            self.V[:, self.s].copy_(direction)
            self.Z[:, self.s].copy_(action)
            self.s += 1

    def mean_action(self, x, *, transpose=False):
        """Apply the current conditional mean, without adding constraints."""
        U, V = self.U[:, :self.r], self.V[:, :self.s]
        Y, Z = self.Y[:, :self.r], self.Z[:, :self.s]
        if not transpose:
            coeff = x @ U
            return coeff @ Y.T + ((x - coeff @ U.T) @ Z) @ V.T
        coeff = x @ V
        return (x @ Y) @ U.T + coeff @ Z.T - ((coeff @ Z.T) @ U) @ U.T

    def action(self, x, *, transpose=False):
        """Reveal large residual directions and apply the resulting mean.

        The selection is pivoted within this batch. It uses only known queries,
        norms and previously sampled constraints, not unseen matrix entries.
        """
        if x.ndim != 2 or x.shape[1] != self.n:
            raise ValueError("queries must have shape (batch, n)")
        if x.device != self.device or x.dtype != self.dtype:
            raise ValueError("query device/dtype must match the oracle")
        right = not transpose
        # With zero tolerance, do not append directions that are numerical zero.
        numerical_floor = 64 * torch.finfo(self.dtype).eps * max(
            1.0, float(torch.linalg.vector_norm(x, dim=1).max()) / math.sqrt(self.n)
        )
        threshold = max(self.tolerance, numerical_floor)
        while True:
            rank = self.r if right else self.s
            basis = self.U[:, :rank] if right else self.V[:, :rank]
            residual = self._residual(x, basis)
            norms = torch.linalg.vector_norm(residual, dim=1)
            value, index = torch.max(norms, dim=0)
            rms = float(value) / math.sqrt(self.n)
            if rms <= threshold or rank == self.n:
                self.max_remaining_rms = max(self.max_remaining_rms, rms)
                break
            self._append(residual[int(index)] / value, right)
        out = self.mean_action(x, transpose=transpose)
        self.calls += 1
        self.queries += x.shape[0]
        if self.record_queries:
            self.records.append((x.detach().clone(), out.detach().clone(),
                                 residual.detach().clone(), bool(transpose)))
        return out

    def complete(self, *, seed):
        """Draw an explicit matrix conditional on the transcript (validation).

        This quadratic operation is NOT used by a matrix-free production run.
        The fresh completion seed must not be selected using its outcome.
        """
        gen = torch.Generator(device=self.device).manual_seed(int(seed))
        G = torch.randn((self.n, self.n), generator=gen,
                        device=self.device, dtype=self.dtype) / math.sqrt(self.n)
        U, V = self.U[:, :self.r], self.V[:, :self.s]
        Y, Z = self.Y[:, :self.r], self.Z[:, :self.s]
        mean = Y @ U.T + V @ (Z.T - (Z.T @ U) @ U.T)
        residual = G - V @ (V.T @ G)
        residual = residual - (residual @ U) @ U.T
        return mean + residual

    def statistics(self):
        U, V = self.U[:, :self.r], self.V[:, :self.s]
        Y, Z = self.Y[:, :self.r], self.Z[:, :self.s]
        mismatch = V.T @ Y - Z.T @ U
        return dict(
            n=self.n, tolerance=self.tolerance, right_rank=self.r, left_rank=self.s,
            calls=self.calls, vector_queries=self.queries,
            max_remaining_rms=self.max_remaining_rms,
            constraint_mismatch=float(mismatch.abs().max()) if mismatch.numel() else 0.0,
            stored_numbers=2*self.n*(self.U.shape[1]+self.V.shape[1]),
            used_numbers=2*self.n*(self.r+self.s),
        )

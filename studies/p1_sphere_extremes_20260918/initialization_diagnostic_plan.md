# Bounded initialization diagnostic

Frozen before execution. The decision is whether a simple pointwise-positive
formula can establish the initialized effective coefficient at
v=(1,1,1)/sqrt(3), needed by the independent positive-family proof route.

Use exactly the general-d p=1 Gaussian initialization in
docs/observable_p1.md, with eta=1/4096. No trajectory is simulated and no
parameter is fitted. After conditioning on G_j, the effective row coefficient
is A tanh(G_j)+B E_Z tanh(sqrt(tau)Z+alpha tanh(G_j)). The primary observables
are A and the resulting diagonal-direction coefficient Z0.

H1: A is positive with a robust margin, making an elementary sign proof
plausible. H0: A is nonpositive, so that particular sign proof is unavailable.
A third outcome is a numerically unresolved value. For either sign the
diagnostic is only evidence for selecting an analytic argument, never a
proof of a dynamical theorem.

Use deterministic Gauss--Hermite orders 64, 128 and 256, float64, with all
source variances and the reverse response term retained. Report all orders.
The validity gate is finite positive Cholesky radicands and absolute
agreement within 1e-5 in A and Z0 for the last two orders. The sign decision
requires |A|>1e-3; otherwise it is inconclusive. No stochastic seeds apply.

Cap: one program, three predetermined orders, one CPU process, at most
60 wall seconds and 256 MiB of numerical arrays. Stop after those orders.
No additional numerical branch is authorized by this plan. If a rigorous
certificate is useful, it requires a separate explicit error derivation
and precommitted computation.

Preserve the study-owned source and its output under this study's generated
namespace. Record versions, command and hashes after execution. A failed
validity gate remains inconclusive; refinement alone will not be treated
as a rigorous error certificate.

# A continuous additive-noise extension of the conditioning flow

2026-09-19. Lead candidate, same-study continuation. No experiments,
finite-width identification or promotion.

## 1. Motivation and exact process

NATURAL_CONDITIONING_FLOW.md proves continuous pathwise exponential fitting
for a current-state conditioning correction. Its optional randomness
acts through bounded readout mobilities. This note instead adds an
explicit small continuous random force to the readout. It preserves
the same exact loss and potential inequalities.

Use the complete model, positive-Gram starting domain, initialization
scope, potential and safeguard from that source, with P_t=I:

\[
R=\operatorname{tr}K^{-1},\quad
\Phi_\varepsilon=L(1+\varepsilon R),\quad
\beta_\varepsilon=
\frac{\varepsilon L[-\langle\nabla L,\nabla R\rangle]_+}
{\|\nabla_c L\|_2^2}.
\tag{1}
\]

Set beta=0 at zero loss, which is absorbing. Let z=nabla_c L and define
the bounded operator on the readout Hilbert space

\[
B(S)u=
\frac{\|z\|_2^2u-z\langle z,u\rangle}{1+\|z\|_2^2}.
\tag{2}
\]

This formula has no division by ||z||. It is locally Lipschitz even
at z=0 and satisfies

\[
\langle z,B(S)u\rangle=0,\qquad
\|B(S)\|_{\rm op}\le1.
\tag{3}
\]

To verify the norm bound when z!=0, B is zero along z and multiplication
by ||z||^2/(1+||z||^2) on its orthogonal complement; at z=0 it is zero.

Fix a physical refresh interval tau>0 and independent identically
distributed readout fields U_j of norm at most one, with symmetric law.
For example, take a fixed unit field q and independently set U_j=+q
or -q with equal probability. One may instead choose random signs and
directions from a finite fixed orthonormal family, including initial
feature directions. Only fixed known fields and fresh finite randomness
are required. Put U_t=U_j on [j tau,(j+1)tau).

For a noise amplitude nu>=0, define

\[
\dot S=
-\nabla\Phi_\varepsilon
-\beta_\varepsilon(0,\nabla_cL,0)
+(0,\nu\sqrt L\,B(S)U_t,0).
\tag{4}
\]

All state components evolve continuously, and their equations run at
every physical time. There is no accept/reject step, hidden pause, or
state jump when U changes. This is an ODE with a bounded colored random
forcing, not an Ito diffusion. Conditional on a fresh draw at a refresh
time the prescribed U has zero mean; its subsequent correlation with
the evolving state is not asserted to vanish.

The actual physical noise velocity obeys, pathwise,

\[
\|\nu\sqrt L\,B(S)U_t\|_2\le\nu\sqrt L.
\tag{5}
\]

In particular it is globally at most nu sqrt(L0) along the decreasing-loss
process and vanishes as fitting occurs.

## 2. Exact evolution and global continuation

R is independent of c, so
nabla_c Phi=(1+epsilon R)z. Equation (3) makes the noise exactly tangent
to both current L and current Phi level sets. By the ordinary chain
rule for this continuous piecewise-ODE process, its contribution to
both derivatives is zero. There is no Ito second-order term.

The source's complete algebra therefore gives, wherever K>0,

\[
\dot L\le-4\varepsilon L,\qquad
\dot\Phi_\varepsilon\le-4\varepsilon\Phi_\varepsilon.
\tag{6}
\]

Thus the same physical-time pathwise bounds hold:

\[
L(t)\le L_0e^{-4\varepsilon t},\qquad
\Phi_\varepsilon(t)\le
\Phi_\varepsilon(0)e^{-4\varepsilon t}.
\tag{7}
\]

The noise coefficient is locally Lipschitz on the Hilbert state:
sqrt L=|e| is locally Lipschitz, nabla_c L is locally Lipschitz,
and (2) is a smooth bounded-operator-valued function of z.
The source already supplies local Lipschitzness of the other terms,
including the zero-loss safeguard. Thus every fixed U interval has
a unique local solution on K>0.

Let D_t=-dot Phi. The deterministic part of (4) has the same pointwise
bound as source (13)--(14), now with a=b=1:

\[
\|-\nabla\Phi-\beta(0,\nabla_cL,0)\|
\le\frac{D_t}{\sqrt{\varepsilon\Phi}}.
\tag{8}
\]

The tangent noise does not change D_t, so integrating (8) bounds
deterministic-part travel by 2 sqrt(Phi0/epsilon). Equation (5) and
(7) bound total noise travel by

\[
\int_0^\infty\nu\sqrt{L(t)}\,dt
\le\frac{\nu\sqrt{L_0}}{2\varepsilon}.
\tag{9}
\]

Consequently the full path has the deterministic finite bound

\[
\operatorname{Var}_{[0,\infty)}S
\le2\sqrt{\Phi_\varepsilon(0)/\varepsilon}
   +\frac{\nu\sqrt{L_0}}{2\varepsilon}.
\tag{10}
\]

The same argument on a partial maximal interval ensures a strong limit
at a finite endpoint. If K stays positive there, local existence
continues the process. If K becomes singular, bounded
Phi=L(1+epsilon R) forces limiting loss zero; absorb there, with the
source's explicit Phi=0 extension at such a fitted singular endpoint.
Finite norm blowup and positive-loss singular termination are excluded.
This proves global wellposedness for the defined absorbing process.
Finite total variation in the complete Hilbert space and (7) give
a finite strong zero-loss endpoint for every realization.

No fixed neighborhood of initial hidden fields is prescribed. The
finite-travel estimate is a consequence of the global potential,
and its bound may be large as epsilon tends to zero.

## 3. Near-GF meaning and its limitation

Along these initialized loss-decreasing trajectories, the noise force
is uniformly small in the physical metric: its bound (5) does not
require a lower Gram eigenvalue. This is not a uniform bound over
ambient states with arbitrarily large loss.
The deterministic conditioning correction has a different status.
On every bounded region with K>=k0 I, it tends to zero uniformly
as epsilon tends to zero. The source proves this directly for
Phi and beta; its comparison argument then yields

\[
\sup_{0\le t\le T}
\|S^{\varepsilon,\nu}(t)-S^0(t)\|
\le C_T(\varepsilon+\nu)
\tag{11}
\]

for every forcing realization, on any fixed T where the
unmodified GF path S^0 has positive Gram throughout. The constant
does not depend on the noise signs or the chosen U_j, since ||U_j||<=1.
No derivative with respect to the random refresh times is needed;
the comparison integrates a uniformly bounded drift difference.

The hypothesis about the reference Gram remains essential to this
proof. An almost-everywhere or random-time positivity statement
does not supply a uniform lower bound on [0,T] if an isolated Gram
zero lies inside it. The present result does not claim (11) past
such an unproved degeneracy.

Nor is the total modified vector field uniformly close to GF on
the entire state space. The conditioning terms contain K^{-1}
and its derivatives and can become large near degeneracy. This is
true even though the noise term is uniformly small along these
loss-decreasing trajectories. It would be
incorrect to summarize (4) as ordinary GF plus only a uniformly
small random force.

Setting nu=0 retains every fitting guarantee. Hence it is the
conditioning correction that proves convergence; the tangent noise
can explore level-set directions without spoiling that proof.
For one data point, readout noise orthogonal to its activation has
no immediate prediction effect, but it may alter subsequent hidden
backward fields. No usefulness of that exploration or superiority
over the noiseless corrected optimizer is asserted.

## 4. Scope and check record

For canonical p=1,2 and every compatible finite binary circle dataset:
unconditional pathwise exponential loss and potential decay;
continuous evolution of all fields; finite strong fitted endpoint;
no accept/reject or held-state stages; bounded small readout noise
velocity; and a precise local-in-conditioning small-parameter GF
limit. This does not extend canonical p=3 initial Gram positivity.

All scientific dependencies are the complete
NATURAL_CONDITIONING_FLOW.md and its model/initialization dependencies.
The new orthogonality, operator bound, continuation and travel
estimates are derived above. This is a candidate pending a separate
internal mathematical check; no external stochastic theorem or
numerical result is used.

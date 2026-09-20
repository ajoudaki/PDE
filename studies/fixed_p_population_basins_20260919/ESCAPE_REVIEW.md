# Independent audit of escape, cone, and partially fitted saddle claims

Date: 2026-09-19.

**Verdict: PASS within the precise scopes below.** I found no blocking
mathematical error in the final frozen inputs. One inaccurate equality
description of a basin was reported and corrected to containment; the
correction was verified. This is an internal independent audit, not
promotion or a theorem about all bad equilibria or prescribed-initialization
training.

## Inputs and review boundary

Complete study inputs reviewed:

| File | Final reviewed SHA256 |
|---|---|
| `ESCAPE_AND_LIMITS.md` | `544a5fde3b224cfa30539754c5d27123b900c12ed3fe5df98df00d5a8dd20ac2` |
| `PARTIALLY_FITTED_SADDLE.md` | `35f41f4d6516c68d4c3f36fe8eb52d7a6d9c719a0f5bf974f3eb405baa20f9ab` |
| `CLOSURE_ROUTE.md` | `2badec506d1ee61bc73cb41f8f93e6bdd1a0d8074d179b18e8d16e4a3df30c70` |

The cone report was initially designated unavailable, then explicitly
authorized as a frozen input with the last hash above. I read it completely.
I verified the source equations, canonical dictionaries, mark laws,
normalization, and parity against the assigned parts B, C.1, and D.3 of
`docs/global_nonlinear.md` C.4.7.10. Initial source navigation also displayed
the opening contextual paragraphs and part of A.1--A.2; no reviewed claim
depends on those additional passages. No study README, research history,
other study, prior verdict, or another reviewer's findings was read.
The required `solve-math-rigorously` skill was read. No numerical test is
needed for these exact claims, and none was substituted for their proofs.

## 1. Population state space, regularity, and continuation

The equations use the correct negative gradient for the population
L2/Frobenius metric, unhalved loss, and actual matrix transpose. At the
canonical orders 1, 2, 3, the retained lists are precisely the full
polynomial cores, of dimensions (5,3), (15,6), and (35,10). Their boundedness
and positive-definite raw Grams follow from the positive core densities and
polynomial independence in the assigned source. The ridge normalization
is invertible and gives the contractions used in `CLOSURE_ROUTE.md`.

The full-Hilbert-space extension is justified. On a bounded state ball,
the lower moments are Lipschitz into a finite-dimensional coefficient
space; bounded upper marks turn their preactivations into uniformly
bounded L-infinity fields. Readout pairings with c in L2 are then bounded
and locally Lipschitz. The lower gate is Lipschitz into L2, and its
coefficient is bounded in L-infinity. These facts establish a vector field
that is Lipschitz on each bounded Hilbert ball, including at fields with
unbounded pointwise values.

The integrated lower Taylor remainder is bounded by C times the squared
L2 norm of the row displacement. In particular,

\[
 D a_i(w)[h]=E_1[b_1\phi'(w\cdot u_i)(h\cdot u_i)],
 \qquad
 \|Da_i(w)-Da_i(\widetilde w)\|_{\rm op}
 \le C\|w-\widetilde w\|_2.
\]

The remaining smooth finite-parameter maps and bounded pairings give a
C1 loss whose gradient is locally Lipschitz. The energy identity is
therefore valid. The successive speed estimates first bound c, then M,
then w on every finite time interval; bounded speed gives a strong limit
at any hypothetical finite endpoint. Local continuation excludes finite
forward blow-up. The same estimates are uniform in the unit input, so
the bounded-label probability-law version in the cone report is also
valid.

The explicit warning against assuming an L2-to-L2 C1 Nemytskii gate, or
an everywhere C2 loss, is appropriate. None of the later conclusions
requires that invalid strengthening.

## 2. Curvature, stationary loss, and vanishing sample gradients

The two-block second-variation formula is correct. Orthogonality
\(k\perp\operatorname{span}\{H_i\}\) eliminates the readout contribution
to the first output variation, and the mixed second output variation is
\(2\alpha E_2[k\delta H_i]\). Differentiating the unhalved square loss
therefore produces exactly \(A(v)+4\alpha B(k,v)\), with no missing
factor or positive \(\alpha^2\) term. A nonzero projected mixed feature
provides a bounded k because it differs from a bounded field by a finite
linear combination of bounded features.

At \((w,0,0)\), every sample gradient vanishes, not only the full-batch
average. The proposed \(k=b_2^Te\) and matrix direction
\((Ge)v^T\) give mixed coefficient \(-|Ge|^2|v|^2\) whenever the stated
v is nonzero. Thus strict negative curvature and identically absent
minibatch noise coexist in the actual closure.

Taking the readout stationarity equation against c gives
\(\sum_i\mu_i r_i f_i=0\), hence the stationary identity
\(L=\sum_i\mu_i y_i^2-\sum_i\mu_i f_i^2\). The level-one exclusion for
binary data, conditional on strict initial descent, is correct and only
excludes zero-predictor stationary limits. The scalar square-loss
counterexample correctly disproves inference of an empty-interior basin
from nearby lower losses alone.

## 3. Persistent accepted perturbations

The claimed result is valid for the explicitly modified, full-loss-tested
algorithm. It is not a result for ordinary gradient flow or SGD.

A Gaussian with strictly positive summable eigenvalues is an H-valued
random element with positive probability in every open H-ball. The
finite-projection density and independent small-tail argument given in
the input proves the required support statement. Conditioning on a fixed
positive-radius norm ball preserves positive mass in every open ball
strictly inside it.

Continuity supplies neighborhoods U and W and a fixed positive loss drop
delta whenever the current state is in U and the fresh proposal is in W.
The success probability q depends on that neighborhood but is fixed and
positive at its successive visits. The visit times are determined before
the corresponding fresh draws. More explicitly, the probability that
N successive finite visits after any fixed visit index all fail is at
most \((1-q)^N\). Letting N grow and taking a countable union over the
starting index shows that infinitely many visits entail infinitely many
successes almost surely. Monotonicity and nonnegative loss forbid that.

The countable-cover step is valid and essential: the open neighborhoods
of all offending states have a countable subcover in the separable metric
space. Excluding infinite visits to those countably many neighborhoods
simultaneously excludes every offending accumulation point, with no
uncountable union of probability-zero events.

Consequently the full-support proposal rule has only global-minimum
accumulation points, and the bounded-radius proposal rule has only
local-minimum accumulation points, almost surely. These conclusions do
not assert existence of an accumulation point. The conditional zero-loss
conclusion correctly adds both the landscape hypothesis and precompactness.
The distinctions concerning vanishing amplitudes, support of minibatch
noise, and the deterministic canonical initial state are also correct.

## 4. The three-input partially fitted equilibrium

The construction is an actual state of each canonical order, with three
distinct, nonparallel and nonantiparallel unit input directions. The lower
dictionary contains \(\tanh g_1\), so its positive pairing with
\(\operatorname{sign}g_1\) proves \(v_0\ne0\). The upper dictionary
contains X, and invertibility of the normalization supplies e. Thus the
claimed matrix gives preactivations \(aX,aX,bX\) exactly.

The proof that \(\tanh(bX)\notin V\) is valid. An almost-sure identity
extends to the open square by continuity and positive density. After
setting Y=0, multiplying through by both squared cosh factors gives an
entire identity. At the infinitely many b-poles, irrationality of a/b
prevents coincident a-poles. Absence of a double pole on the left forces
the polynomial Q to vanish at every such point, hence identically;
the remaining right side cannot supply the left side's simple poles.

The projection residual R is therefore a nonzero bounded field. The
normalization of c gives predictions exactly (0,0,1), all \(d_i=0\),
and residuals (-1,1,0). Both hidden velocities vanish and the two readout
terms cancel. The loss is exactly 2/3.

For \(\delta w=s(0,1)\), the differentiated upper features have the
reported opposite signs. The projected field k is nonzero by the
double-pole versus simple-pole argument at an a-pole. Its mixed coefficient
is exactly \(-2\kappa\|k\|_2^2/3\), proving strict negative curvature
with a finite readout multiplier. The mark-parity statements follow
because Cholesky normalization preserves parity, V is invariant under
mark reversal, and orthogonal projection onto V commutes with that
reversal. This confirms compatibility with the canonical parity
subsystem, without establishing reachability from canonical initialization.

## 5. Cone proof and q_i=0 extension

The cone report's full linearizations and spectra are correct. At
\((0,0,M_0)\), the off-diagonal pair is an operator and its actual
Hilbert adjoint. Positive-definite normalized Grams give exactly
\(\operatorname{rank}M_0\) positive eigenvalues when m is nonzero.
At \((w_*,0,0)\), the analogous middle/readout pair has exactly
\(d_2\) positive eigenvalues when the stated \(v_*\ne0\).
The remaining directions include the claimed infinite center spaces.

The small-Lipschitz-remainder proofs control differences of arbitrary
L2 displacements, including narrow spikes. The integrated lower moment
remainder uses Cauchy--Schwarz, while the lower pointwise gate difference
is only used in L2 and is multiplied by a small bounded coefficient.
No unjustified L2 differentiability of that gate is present.

For the more general finite-data criterion, write the lower velocity
as a finite sum of products of a gate \(g_i(w)\) and a bounded coefficient
field \(p_i(S)\), with \(p_i(S_*)=0\) because \(q_i(S_*)=0\).
The coefficient maps are C1 with locally Lipschitz derivatives.
After subtracting the linearization, the potentially delicate product is

\[
 [g_i(w)-g_i(w_*)]p_i(S).
\]

On a radius-r ball, each of its two difference terms is bounded in L2
by \(Cr\|S-\widetilde S\|_{\mathcal H}\). The coefficient Taylor
remainder has the same estimate. The other blocks have smooth
finite-parameter gate dependence. The resulting derivative is finite-rank;
it is selfadjoint because it is the derivative of a gradient. A negative
bounded second-variation direction gives a positive eigenvalue of the
negative-gradient linearization. This validates application to the
partially fitted state, where every d_i and hence every q_i vanishes.

The cone inequalities have the correct signs and constants. At a nonzero
boundary \(\alpha=\beta\), the derivative of
\(\alpha^2-\beta^2\) is strictly positive. The cone is forward invariant
while both trajectories remain in the chosen ball, and its unstable
component grows at least as \(e^{\lambda t/2}\). Two trapped trajectories
therefore satisfy \(\alpha\le\beta\), giving the stated Lipschitz graph
over a subset of the complementary space. The trapped set is closed and
nowhere dense, and each unstable fiber contains at most one point. Its
conditional measure is zero under precisely the stated finite-dimensional
absolute-continuity hypothesis.

Finite-time maps are open by local backward continuation along a bounded
finite segment, and are continuous by local Lipschitz dependence. Their
inverse images of these closed nowhere-dense sets are closed nowhere dense.
The half-radius countable covers and integer-time tail argument establish
meagreness for strong convergence to any member of each nondegenerate
collapsed family. They also establish meagreness of the point basin of
the partially fitted saddle. The corrected saddle report now properly
says this basin is **contained in** a countable union of trapped-set
pullbacks; equality would not follow because trapped points need not
converge to the selected equilibrium.

## Limits of the verdict

The reviewed results do not establish that every positive-loss equilibrium
is unstable, that every bad basin has zero probability for a specified
global Gaussian state law, or that the canonical trajectory converges to
zero loss. The family basin conclusions concern strong convergence to an
individual equilibrium in the family, not merely convergence of distance
to the family without a limiting state. The local conditional-null claims
and global category claims must remain distinct. Within those boundaries,
the stated results and the proof dependencies are complete.

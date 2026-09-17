> **Scope superseded by the 2026-09-16 continuation.** This document records
> the earlier near-antipodal result and its then-open questions. The current
> [all-angle result](all_angles_result.md) proves convergence and strict
> endpoint contrast gain at every separation for actual reflection pairs,
> and for antipodes in every orientation, at any label amplitude. It also
> proves convergence for arbitrary orientations with sufficiently small
> labels. Its new normalized-readout potential removes the old cross-sign
> bottleneck for the reflection theorem. Arbitrary-orientation unit-label
> convergence remains open. Read the [README](README.md) for current status.

# Current result: protected hidden contrast and finite state length

Research result for the exact p=1 population closure, 2026-09-16.
This study is not a promotion to established docs/ or code/.
The complete main argument is [proof.md](proof.md).
Independent routes and internal checks are linked in the README.

## Main theorem

Use exactly the canonical p=1 dictionary, eta=1/4096, inverse-Cholesky
normalization, correlated frozen marks, initial (w,c,M)=(g,0,D), actual
M transpose, and unhalved probability-weighted physical square loss.
For any fixed A>0 there is an explicitly defined epsilon_*(A)>0 such that
the theorem applies to all balanced pairs

u_+=(epsilon,sqrt(1-epsilon^2)),
nu_-=(epsilon,-sqrt(1-epsilon^2)),
(x_+,y_+)=(sqrt(2)nu_+,+A), (x_-,y_-)=(sqrt(2)nu_-,-A),
0<=epsilon<=epsilon_*(A).

Thus the angular separation varies through a positive-width interval
[2 arccos epsilon_*(A),pi]. Unit labels A=1 are included. The interval is
centered on antipodal coordinate-axis data, is restricted by the exact
reflection symmetry, and has extremely conservative unevaluated constants.
No rotational invariance of the finite dictionary is assumed.

Define, solely from the current state,

U_S=(H^2_S(nu_+)-H^2_S(nu_-))/2,
C(S)=E_2 U_S^2,
F(S)=(f_S(nu_+)-f_S(nu_-))/2,
Z_A={S: f_S(nu_+)=A and f_S(nu_-)=-A}.

C is one quarter of the squared population-L2 distance between the upper
hidden representations of opposite-label inputs. Z_A is the set of fitting
states, specified by data rather than by the trajectory's eventual answer.
On the initialized trajectory symmetry gives f(nu_-)=-f(nu_+), so L=(A-F)^2.

Explicit initialized constants kappa>0 and g_*>0 in the full proof give

C(S_t)>=kappa,
L(t)<=A^2 exp(-4 kappa t),
int_t^infty ||(w_dot,c_dot,M_dot)||_physical dt
 <=sqrt(L(t)/kappa),
C(S_infty)>=C(S_0)+g_*/2.

The physical squared norm is E_1|w_dot|^2+E_2|c_dot|^2+||M_dot||_F^2.
Consequently the complete state converges to a finite S_infty in Z_A.
Both full joint populations converge in W2 under their common frozen-mark
couplings; the characteristic fields w-g and c also converge in supremum
norm, and M in Frobenius norm. In particular

||H^2_infty(nu_+)-H^2_infty(nu_-)||_2^2
 >=||H^2_0(nu_+)-H^2_0(nu_-)||_2^2+2g_*.

This is a genuine increase in a fixed physical hidden distance. We do not
claim its derivative is nonnegative at every time away from the exact axis.

## Why the theorem is more than loss dissipation

For the reflection-symmetric family, the exact evolution is

S_dot=2(A-F(S)) grad_physical F(S).

The trajectory is therefore a gradient curve of the signed prediction F;
the positive residual determines its speed. Its autonomous parameter s obeys
S_s=grad F and s_dot=2(A-F). This is an analysis coordinate with no extra
saved state. For a fixed pair of inputs, changing the positive label
amplitude changes the physical clock and stopping level on the same curve,
not the direction of the gradient curve. This statement follows from the
same autonomous equation and uniqueness, not from fitting observed paths.

The substantive new estimate is that its readout component U_S cannot
collapse on the proved family. At the exact antipodal axis, the complete
closure reduces by proved symmetries to scalar upper preactivation beta k,
with a lower block B, active middle row m, lower preactivation W, and

k=m·E_1[B tanh W],
k_s=d(|a|^2+E_1[(m·B)^2 sech^4 W])>=0,
d=E_2[beta c sech^2(beta k)]>=0.

The exact initialization gives k(0)>0; c acquires the sign of beta, which
preserves these inequalities. Thus E tanh^2(beta k) stays positive and
increases strictly. Finite gradient-time perturbation estimates extend
noncollapse and a definite endpoint increase to the stated non-antipodal
family. This avoids an unproved sign assumption about lower cross terms.

On the axis there is also the exact full-state balance

||m||^2-E_1 sinh^2 W = constant.

Both terms increase together after initialization. The finite-time Gaussian
exponential moments justify the transformed lower expectation. This is a
constraint on coupled hidden/middle organization and permits expansion.
It does not assert a uniquely desirable individual hidden representation.

The lower bound on C converts energy dissipation into integrable physical
speed, which supplies full-state convergence; square-integrable speed alone
would not do so. The readout contrast also determines a fitting correction
from the current state, as detailed below.

## A current-state fitting certificate and neutral directions

On every reached state in the theorem let e=A-F. Keeping w,M fixed, set

c_fit=c+e U_S/C(S).

Reflection sends H_+ to H_- and U to -U, so U is orthogonal to
(H_++H_-)/2. Therefore E[(c_fit-c)H_+]=e and
E[(c_fit-c)H_-]=-e; both required labels are fitted. Any readout correction
fitting the pair satisfies E[delta c U]=e. Cauchy-Schwarz gives
||delta c||_2^2>=e^2/C, with equality exactly for delta c=e U/C.
Thus this is the unique minimum-norm readout correction, and

inf_{S' in Z_A} d_state(S,S') <= |e|/sqrt(C(S)),

d_state(S,S')^2=W2(Gamma_1,Gamma'_1)^2
              +W2(Gamma_2,Gamma'_2)^2+||M-M'||_F^2.

Here the population W2 metrics use their complete Euclidean joint
coordinates, including frozen marks. The explicit correction and all
trajectory comparisons admit couplings with identical frozen marks.
These are fixed metrics; no collapsing metric is used.

The squared correction distance Psi=e^2/C is NOT separately asserted to
be decreasing for every non-antipodal pair. Its exact physical derivative is

Psi_dot=-(4K+C_dot/C)Psi,
K=||grad_physical F||^2.

At the axis C_dot>=0, but away from it our proof only supplies a lower
bound and an endpoint increase. Including the C_dot term is essential.
The loss with the proved contrast estimate is sufficient for the theorem.

There are infinitely many fitting states: after reaching any fit, add any
readout function orthogonal to both H_+ and H_-; all residuals remain zero
and all exact velocities vanish. Hence contraction of every full-state
direction, or convergence to a prescribed unique representation, is not
the right conclusion. The main proof instead supplies finite length and
convergence to the data-defined set Z_A.

## Independent complementary result near orthogonal data

The independently developed [route_local.md](route_local.md) gives a
separate basin theorem around two linearly independent output constraints.
Its exact initialized Gaussian integral m_0>0 equals the initial upper
feature variance on a coordinate axis. Put lambda=m_0/8. For

u_1=e_1, |nu_2-e_2|<=sqrt(m_0)/4,
y_1=+a, y_2=-a, 0<a<=lambda/(8 sqrt(5)),

it proves L(t)<=a^2 exp(-lambda t) and physical tail length at most
2a/sqrt(lambda) exp(-lambda t/2), with convergence of the full state.
The fitting set is locally a codimension-two Hilbert manifold. The Hessian
has two positive normal eigenvalues and an infinite tangent kernel.
This supplements the unit-label symmetric theorem; it does not replace
its stronger-amplitude but narrower-geometry assumptions. It is a
perturbative regime, compatible with predominantly readout-driven fitting.
Root checked its complete derivation in [check_local_root.md](check_local_root.md);
it has not received a separate fresh full audit or any promotion review.

## Stress tests, obstructions and exact remaining estimate

1. Coincident inputs with balanced contradictory labels have minimum loss
A^2. At the canonical zero-output initialization the two gradient
contributions cancel and the state remains fixed. No positive uniform
fitting rate can extend to that degeneration.
2. Input oddness makes equal nonzero labels at antipodes incompatible.
3. In the ambient state space M=0,c=0 is stationary with positive loss for
nonzero labels, regardless of w. Thus an unconditional nonstall theorem
for every ambient state is false. Our theorem depends on proved properties
of the actual canonical initialized trajectory.
4. The same signed-prediction gradient structure alone does not prove
noncollapse for arbitrary angles. The frozen independent axis route gives
an exact lower cross term C_cross=E[k_1 k_2 sech^4(w·nu_+)]. A direct
cone extension lacks the reached-trajectory sign B_1 C_cross<=0 and
positive initial antisymmetric signal over any proposed larger class. The
post-freeze [cross_sign_note.md](cross_sign_note.md) shows that the one
cross-sign estimate would also control the common upper coefficient and
thereby protect readout contrast; those are not independent additional
dynamical gaps. Positive semidefiniteness of the tangent matrix does not
determine the cross sign. This is an open estimate, not a claim disproved
by evidence. The main theorem proves a restricted family through continuity
without assuming it.
5. Increasing hidden separation is useful here because the labels are
opposite. Neither universal alignment nor universal separation is claimed.
6. No generalization, arbitrary-data convergence, all-angle result,
closure-order limit, or all-time neural-network identification is proved.

All positive results here are analytic. No simulation, empirical monotonicity,
quadrature result or unpromoted result from another study is used.

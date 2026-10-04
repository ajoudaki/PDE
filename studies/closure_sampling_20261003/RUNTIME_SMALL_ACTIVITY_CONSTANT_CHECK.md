# Reconstruction of the activity-sensitive runtime constants

2026-10-04. Complete coordinator reconstruction of
RUNTIME_SMALL_ACTIVITY_CONSTANT_ROUTE.md, frozen SHA-256
061d46972a7b026bd6b6b5176fc411214e82bd1e9d9e18ec5bd8e119fedbeaa2.
This is a collaborative internal check, not independent promotion. The
coordinator proposed preserving the activity factors and helped develop
the comparison strategy. The candidate author and its scoped child
derived the finite inequalities; the coordinator read the complete
candidate, reconstructed the algebra, and independently implemented the
constant evaluation and rational certificate below.

The inherited canonical source-selection/insertion and corrected-readout
construction are exactly those in the complete inputs named by the
candidate. Their relevant source/runtime proofs were already read during
this continuation. This check verifies the sharper implication from those
interfaces, not a fresh independent review of the entire earlier study.

**Conclusion:** the candidate passes within that scope. The simple
depth-two certificate is
\[
Y\le 2.8\,10^{-7}\frac\gamma m,
\qquad
\sup_{t\in[0,\infty],\,\|x\|=\sqrt d}|f_C(t,x)-f_n(t,x)|
\le 2.8\,10^5Y(m/\gamma)^{3/2}n^{-1/2}.
\tag{1}
\]
Here Y is label RMS, gamma is the smallest eigenvalue of the unnormalized
initialized feature covariance, and both hidden layers of the canonical
dense reference have width n. The source rank/storage theorem is unchanged
from ACTIVATION_CONSTANTS_REFINEMENT_ROUTE.md. Fixed data and architecture,
positive gamma, fixed confidence and sufficiently large width remain the
scope. Zero labels give identically zero outputs and are handled separately.

## 1. Normalizations and source forcing

Write lambda=gamma/m<=1, u=Y/lambda, alpha=Y/sqrt(lambda),
epsilon=n^-1 and r=epsilon/sqrt(lambda). These are precisely the physical
clock and metric normalizations of EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md.
The source approximation multiplier is one. The initialized mixer cap
7/2, real tube 15/4 and carrier coefficient K_src are separate constants.
No Gaussian maximum coefficient is substituted for a coordinate error.

For the candidate's cap c, u<=c and alpha<=u, so the forward/reverse
learned action errors retain u alpha<=c^2. This gives its
A_0=10+8c^2(D_delta P_h+hP_delta), not the old value obtained by setting
the activity to one. The forward recurrence uses actual g=2 and R=15/4.
The direct-sum norm and the slope bound g>=1 justify using C_f for both
preactivation and feature errors. No derivative of a source approximation
is taken.

The exact readout cancellation has two orthogonal projection terms,
whose combined norm is bounded by b=||p||+||zeta||. The coefficient is
one. Applying ||T_C||<=3/sqrt(lambda) to the feature and pairing errors
gives exactly
\[
\|\eta\|\le b+u(3WC_f)(a+\epsilon)+u(3D_r)r.
\]
In particular, one does not multiply the entire hidden/readout error by
3WC_f. The normalized response-pair Gram error retains alpha and alpha^2,
which are bounded above by c and c^2 in D(c).

For every backward layer, there are four terms: propagated readout
difference, changed mixer times an RMS carrier, reverse source forcing,
and changed gate times the actual coordinate carrier. The three descending
recurrences X,Y,Z count each term once. Minkowski in the hidden-parameter
tuple gives
\[
\|\Delta\mathcal J\|
\le Ub+u(E_a+E_q\chi)(a+\epsilon)+(\bar Y+uUB_r)r,
\qquad \chi=\sqrt{\log(en)}.
\]
The coordinate carrier is 16 K_src u chi. It has no additive constant
independent of label activity. The extra feature factor in a hidden
matrix update accounts for h^2 in the tuple norm; the reference-response
times changed-feature term accounts for sqrt(L-1). This verifies the
candidate's (5)--(11) from the actual source and layer estimates.

## 2. Damping and the inhomogeneous comparison

With P=||p||, Z=int ||e||^2/P, and I the integrated lifted forcing, the
exact residual-energy estimate is
\[
P+(2-18J_0^2u^2)Z\le I.
\]
The quotient is zero when both numerator and denominator vanish; norm
regularization gives the integrated form. The lift bound implies
int||e||<=3Z/sqrt(lambda), including those zero points.

Adding the readout and hidden inequalities leaves the coefficient
18J_0^2u^2+6J_0u on Z. Put v=6J_0u<=1. Then
v^2/2+v<=2-v^2/2. Thus the same damping pays both terms:
\[
a+b\le2I+2C_f\int\rho_n(a+\epsilon)
                 +2\int\rho_n\|\Delta\mathcal J\|.
\]
There is no second independent use of the full damping budget.

Substitution yields the nonnegative L_a,L_b,L_r of candidate (15).
Because a,b>=0 and a+b=E, taking k=max(L_a,L_b) is sufficient;
their sum is unnecessary. The source term is
r(sqrt(lambda)L_a+L_r). The Gram approximation in L_r remains a source
term throughout the integrating-factor argument, and does not enter k.

Using int rho_n,int rho_C<=4u, int nu<=(W/2)alpha, and lambda<=1 gives
\[
\int k\le Au+B_{\exp}u^2\chi,\qquad
\int(\sqrt\lambda L_a+L_r)
 \le u(F_{\rm src}+B_{\exp}u\chi).
\]
Every coefficient in candidate (17) follows directly: the 6 C_f W
comes from 12 C_f int nu/sqrt(lambda); the 8 T' c comes from the
compressed residual integral; the 48 D(c) is an additive forcing.
The resulting bound (18) is valid at equal physical times without a
loss-matching or activity-clock substitution.

## 3. Output, width conversion and endpoint

The direct query decomposition gives candidate (19), with
O=max(h,WC_f c(3h+1)) and R_out=(3h+1)(WC_f+D_r). It applies to the
whole sphere on the common source event. Since ur=Y epsilon/lambda^(3/2),
one factor n^-1/2 is available to absorb the mild width-dependent
amplification. For chi=sqrt(log(en)), n^-1/2=sqrt(e)exp(-chi^2/2).

The square-completion calculation in (20) is valid for all chi>=1.
For the smaller coefficient (24), the logarithmic derivative of its
chi-dependent part is
\[
\frac{B_{\exp}c}{F_{\rm src}+B_{\exp}c\chi}
       +B_{\exp}c^2-\chi.
\]
It is decreasing in chi. Candidate (23) therefore makes its maximum
occur at chi=1. This optimization is over all widths and does not move
a structural coefficient into a hidden large-width threshold.

The tail uses the exact differentiated corrected readout, including both
the moving projection and moving inverse. Its norm bounds retain u^2.
The resulting T_tail bounds both dense and compressed prediction speeds.
Residual decay rho<=Y exp(-lambda t/4) gives each tail at most
4 T_tail Y lambda^-3/2 exp(-lambda t/4). At the existing horizon
T=32 lambda^-1 log(en), the sum contributes
8 T_tail exp(-8)n^-8 Y lambda^-3/2. Replacing n^-8 by n^-1/2 is valid
for every n>=1. Both trajectories converge, so the argument includes
their endpoint predictions. No all-time coordinate source is assumed.

## 4. Exact depth-two certificate

The standalone deterministic verification is
`python studies/closure_sampling_20261003/check_small_activity_constants.py`.
It verifies the frozen source-evaluator hash, reconstructs the new runtime
recurrences separately, and uses Fraction arithmetic for the following
certificate. The floating-point table is diagnostic only.

The elementary brackets 2.718<e<2.719 follow by summing through 1/8!
and bounding the remainder by (10/9)/9!. The exact source values are
A_H=57032/225, H_2=64712/225, D_H=4. Substitution gives D_0<1810000
and 128 G<1810000, hence eta>=1/1810000. The feedback budget is at
most 128(2.719)^2<947; D_1<=576(2.719)^3 4^3. The cutoff logarithm
Lambda is less than 22 because
\[
2.719+128(2.719)^2<(2.718)^7,
\qquad1810000<(2.718)^{15}.
\]

At u_0=2.8*10^-7 and S_0=16u_0, the largest normalized source
feedback test is
\[
1810000^2\,4718592\,(2.719)^5S_0^4
 =0.925396112468\ldots<1.
\]
All quantities in this comparison are rational, so its strict sign is
certified. The other normalized tests are at most 0.00455, 0.58124,
0.30690, and 0.00080. The script also checks the first-matrix and
real-fitting restrictions and the exact angular/time radius recurrences.
These imply c_ang>2*10^-5 and c_time>1.3*10^-6. The runtime restrictions
follow from U<16, F=19, J_0<306. Thus every entry in the cap minimum
exceeds u_0; the claimed label allowance is a certified lower bound,
not a rounded estimate of the minimum.

For the error calculation the source cap is below 3*10^-7, as proved
from its feedback entry in candidate Section 6. For every c<=3*10^-7,
the exact recurrence admits
\[
C_f<210,\quad E_a<656000,\quad E_q<17670000,
\quad D(c)<17.001,\quad g_c<2.003,
\]
\[
A<85700,\quad B_{\exp}<142000000,\quad F_{\rm src}<86700,
\quad O=2,\quad R_{\rm out}<95032,\quad T_{\rm tail}<56.000001.
\]
The lower bound F_src>=5016 proves the decreasing-chi criterion.
The exponent is below 0.026 and exp(0.026)<=1/(1-0.026)<1.027.
Substitution into (24), still with exact rational inequalities and the
lower bracket for e in the tail, gives C_all<273202<280000.
This proves both constants in (1). The same rational source checks
were separately repeated by the candidate author and agreed.

The independently recomputed diagnostic values are:

| Hidden depth | Complete cap c | All-time coefficient from (24) |
| ---: | ---: | ---: |
| 2 | 2.8576808963764503e-7 | 271420.3954621694 |
| 3 | 1.1380464798151872e-9 | 2043381.1114346955 |
| 5 | 3.5674114931936606e-14 | 115214443.77219956 |

All three satisfy (23). For other depths use the finite minimum and
general expression (20)--(22), or (24) only after its displayed test.
No unproved extrapolation of the rounded table is needed.

## 5. Scope and supersession

The result preserves the canonical reference, autonomous corrected-readout
compressor, source accuracy epsilon=n^-1, whole-sphere norm, and original
physical time. It inherits the already counted retained matrices, metrics,
data and work arrays. It does not impose clipping, a rank restriction, or
an extra condition on the labels' signs. The small-label coefficient is
improved. Constants do not depend on width or time; data, architecture,
confidence and a sufficiently large width threshold remain fixed as before.

This supersedes only the earlier runtime cap/error bookkeeping in
ACTIVATION_CONSTANTS_REFINEMENT_ROUTE.md, not its source/storage proof.
The earlier moderate-exponent table remains a valid weaker result.
The two-layer numerical constants are much better but still conservative;
the source gap dependence, large dimension-dependent storage prefactors,
preprocessing cost and precision questions are not resolved by this check.
No manuscript edit, training experiment, or promotion was performed.

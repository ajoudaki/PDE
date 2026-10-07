# Cross-route audit of restarted dense Taylor setup

2026-10-06. Mathematical reconstruction audit, with no numerical experiment.
This is a cross-route check within the study, not an independent original
attempt or a promotion review. The reviewer authored the separate streamed
assembly candidate and received the supervisor's proposed bridge to it.

**Verdict:** no outstanding substantive defect was found in
LOCAL_CONTINUATION_SETUP.md at the final hash below, for its inherited source
event and exact-real activation-backend contract. The approximate-anchor
complex restart, defect estimate and global induction provide a constructive
source-value procedure. The algorithm does not require exact future trajectory
values. Efficient total arithmetic remains conditional on the specified
activation backend and the existing event/width qualifications.

## Frozen inputs and coverage

Read every line of the revised continuation candidate, Sections 1--7:

- LOCAL_CONTINUATION_SETUP.md:
  c4c12b38e49e37ac5096e69ceabee1d41be6ad6bc4a1c57ece943959ef425bbe.
- POLYNOMIAL_SETUP_ODE_ROUTE.md:
  46e9c2b4ed9f118b3812ce8208d26ebbfa9c9f1fb3efc6e68f3854e0be8cf5a6.
- RESULT.md:
  c2cbd1bb0e6a39de87181df89be977eaf2e272fda4f1459ac934396d84e1b278.
- POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md:
  2d58da5a418f6d5a8f1bb54ce343b205978770424c0940789b15231e251daf42.
- docs/notation.qmd:
  78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023.

The entire ODE and quadrature route notes were read. The RESULT.md inputs
checked include source constants and complex maxima, S.6--S.8; source families
and analytic-extension gates; the full all-horizon extension proof; source
approximation, pairing and exact source metric; and complete relevant
arithmetic derivations. The source probability event is imported by the
candidate and was not independently re-proved here.

For the separate synthesis check below, the additional inputs were the
reviewer's LOCAL_CONTINUATION_ASSEMBLY.md, hash
488216678b1ea31fcfb8da5f396c8323eae3a38be067c2e431de21a600df2fe2,
and the supervisor's explicit proposed bridge. This exposure prevents treating
the check as independent of assembly authorship.

Applied the accessible rigorous-math and conjecture-audit skills, the current
repository instructions and the notation contract. The required canonical
notation skill remained inaccessible at its prescribed path; no accessible
copy was found in the available skill roots. No other study, archived book,
previous chat or historical research input was read.

## 1. The corrected complex margin

The original source domain gives imaginary preactivations at most \(a/4\)
through its original horizon. The all-horizon extension controls them by
\(3a/8\). The corrected candidate uses this latter bound uniformly and sets

\[
b_n\le\frac{a}{16\sqrt nP_*}.
\]

Along a parameter segment from the exact complex center, forward subtraction
gives coordinate variation at most \(\sqrt nP_*b_n\le a/16\). Stopping at
the first half-strip exit is legitimate: before that exit the derivative
bounds apply. The resulting imaginary bound is
\(3a/8+a/16=7a/16<a/2\), preventing the alleged exit. Operator and readout
margins also hold because the normalized parameter change is at most \(1/4\).
The supervisor's correction is present in the imported statement and restart
proof.

## 2. Endpoint, carrier and Lipschitz recurrences

Forward subtraction gives
\(P_1=1\), \(P_j=H_{j-1}+11sP_{j-1}\): the two terms are the
changed-mixer action and propagated feature difference. The first matrix is
normalized by \(\sqrt n\), and each block discrepancy is bounded by the full
normalized parameter discrepancy.

For backward propagation only the reference endpoint needs carrier maximum
\(M\). The changed gate contributes \(t_2MP_jE\) to RMS response error.
The next mixer contributes \(11D_{j+1}(M)E+B_{j+1}E\). Substituting
\(D_{j+1}=s\kappa_{j+1}+t_2MP_{j+1}\) gives exactly the candidate's
\(\kappa_j\) recurrence. The top carrier is the readout, with RMS discrepancy
at most \(E\). Thus equations (8)--(9) do not assume carrier control for the
perturbed endpoint.

The gradient-block bounds \(B_1,B_jH_{j-1},H_L\) give \(G\) by summing
block norms. Splitting a changed hidden block as
\(\Delta\delta\,h(u)^T+\delta(v)\Delta h^T\) gives the stated \(J(M)\).
Complex algebraic transposes cause no difficulty: these absolute Euclidean
bounds do not require a positive complex Gram matrix.

When the parameter segment is admissible, integration of the gradient gives
prediction discrepancy at most \(GE\). Splitting the vector field using the
reference residual then gives

\[
\|F(u)-F(v)\|_2\le
[2G^2+2\rho(v)J(M)]\|u-v\|_2.
\]

The early complex training-carrier maximum is present in RESULT.md S.23,
whose construction explicitly uses a complex time rectangle. For late times,
the all-horizon extension places the exact complex state within \(Z_n\) of
the real state at \(T_0\). The endpoint estimate therefore gives

\[
M_c=M_0+\sqrt n\,\kappa_*(M_0)Z_n.
\]

No coordinate maximum on the entire late parameter ball is assumed.
Since \(Z_n\) contains \((en)^{-16}\), \(M_c=O(\sqrt{\log(en)})\) at
fixed parameters. Applying the estimate inside a moving radius-\(b_n\) ball
gives carrier maximum \(M_c+1\). Its convexity makes the prediction and
vector-field estimates apply between every pair of states in that ball.
The stated \(L_n\) is consequently a genuine local pairwise Lipschitz bound.

## 3. Complex restart and reference-path provenance

The contraction acts on the closed radius-\(b_n\) ball in the complete
supremum-norm space of continuous disk-holomorphic vector functions.
\(L_nR_n\le1/4\) gives contraction factor \(1/4\); restart error at most
\(b_n/4\) puts its image in the radius-\(b_n/2\) ball. Every vector-field
evaluation therefore lies in the established parameter domain.

The holomorphic integrand has a primitive on the disk. Bounding its integral
along straight radii is valid. Uniform convergence preserves holomorphy by
Cauchy's formula on smaller circles. The fixed point gives an exact local
solution from the approximate anchor, with discrepancy at most \(4/3\)
times the anchor discrepancy. The residual/gradient bounds give
\(V=2G(2Y+G)\). Conjugation and uniqueness make the local solution real on
the real diameter.

The true trajectory is a proof device for this existence and error argument.
The algorithm's coefficient recurrence does not evaluate it. Constants
\(b_n,R_n,K\) depend on source coefficients, labels, width and tolerance.
The algorithm need not measure its exact anchor errors; the theorem guarantees
them on the imported event. This is an a priori certificate, not a hidden
trajectory oracle or an a posteriori test requiring unknown exact states.

## 4. Taylor tail, defect and prefix induction

Vector-valued Cauchy estimates take the norm of a contour integral and cost
no factor \(\sqrt P\). The bound
\(\|v_t(\zeta)-u_0\|_2\le VR_n\) gives coefficient norms at most
\(VR_n^{1-k}\). On a half-radius panel,

\[
\sum_{k=K+1}^{\infty}2^{-k}=2^{-K},\qquad
\sum_{k=K+1}^{\infty}k2^{1-k}=(2K+4)2^{-K}.
\]

These reproduce (19). The exact local restart is within \(b_n/3\) of the
true center. A polynomial tail at most \(b_n/3\) leaves the polynomial
in the same radius-\(b_n\) ball. The Lipschitz correction to the derivative
tail is at most \(V2^{-K}/4\), below the rounded defect
\(V(2K+5)2^{-K}\).

The real defect lemma was reconstructed from the ODE route. Keeping the
negative sample-prediction discrepancy square gives

\[
E'\le2J^{\rm r}\rho E+
\tfrac12(C^{\rm r}+J^{\rm r})^2E^3+\|d\|_2.
\]

Its integrated linear coefficient is at most
\(A_n=4J^{\rm r}Y/\lambda\), without a factor \(T\). The smallness
conditions in (23) give amplification \(2e^{A_n}\). The minimum in (24)
enforces these conditions, final source accuracy, and
\(2e^{A_n}\varepsilon_d\le b_n/4\).

For \(K\ge8\), \(2K+5\le4\,2^{K/2}\), so (25) makes the integrated
defect at most \(\varepsilon_d\) and the local polynomial tail at most
\(b_n/3\). Panel lengths are at most \(R_n/2\).

The induction is noncircular. The first anchor is exact. The already
constructed prefix has the asserted defect; applying the real lemma to that
prefix places its final anchor within \(b_n/4\). Only then is the next
local theorem invoked. No assertion about unconstructed numerical panels is
used. The joined polynomial path is continuous and absolutely continuous;
finitely many derivative jumps at panel boundaries cause no defect atoms.

At fixed parameters and polynomial accuracy,
\(A_n=O(\sqrt{\log n})\), the needed degree is \(O(\log n)\), and the
panel count is \(O((\log n)^{3/2})\), as claimed.

## 5. Source values, pairing and arithmetic

The recurrence

\[
u_{k+1}=\frac{[h^k]F(\sum_{i=0}^{k}u_ih^i)}{k+1}
\]

is causal. Its network coefficient is obtained from previous parameter
coefficients and the specified activation backend. Induction identifies it
with the exact local Taylor coefficient. Training uses the actual training
samples; all other source queries remain passive.

At a node, the candidate evaluates the parameter polynomial and the nonlinear
network on that state. The ODE route's coordinate source bound
\(C_{\rm src}nE\) applies because the state is real and lies in its required
tube. It separately controls initialized images. Multiplying each computed
base vector by the fixed \(W_0\) enforces exact pairing even when its current
trained mixer differs from \(W_0\).

Piecewise analyticity suffices for the numerical representation. Quadrature
is proved for the exact analytic source, then its finite sum is perturbed
using nodal accuracy. The approximation need not itself be globally analytic.
This preserves the original retained coefficient set and source rank.

Each materialized scalar series multiplication is an online two-index
convolution. With intermediate forward, backward and residual coefficients
retained, the non-activation cost is \(O(mPK^2)\) per panel. No parameter
Hessian or nonlinear factorization is needed. The separate
\(Lmn\mathcal A_\phi(K)\) term covers activation composition and derivative
generation. The \(PK\) parameter coefficients, training buffers and backend
state appear in memory.

Horner evaluation costs \(PKN_t\); passive forward/backward and initialized
image actions cost \(PN_tN_x\), with scalar calls charged separately.
These reconstruct (34). Physical-time ordering permits one continuation
pass. The stated alternatives storing panels or nodal states also remain
near quadratic at fixed parameters. Quadrature, selection and assembly are
additional costs, as the candidate states.

## 6. Separate check of the supervisor's source-jet bridge

The frozen continuation candidate uses direct nodal evaluation. The assembly
candidate instead assumes local source Taylor polynomials with Euclidean
nodal error at most \(\delta_{\rm node}/8\). The following supervisor-supplied
synthesis closes this gap and is not attributed to the frozen candidate.

Write \(\delta=\delta_{\rm node}\) for the assembly tolerance. Run the core
construction with \(\widehat\delta=\delta/(64\sqrt n)\). Every computed
anchor then has error

\[
E_{\rm anchor}\le\frac{\delta}{64C_{\rm src}n^{3/2}}.
\]

The exact local restarted solution \(v_t\) obeys
\(\|v_t-\theta\|_2\le(4/3)E_{\rm anchor}\). On the real panel its source
coordinate discrepancy is at most \(\delta/(48\sqrt n)\), and hence its
source Euclidean discrepancy is at most \(\delta/48\).

Set \(B_*=\max_j\{H_j,B_j\}\), using the candidate's complex feature and
response RMS bounds. For each real passive query, either base source along
\(v_t\) is holomorphic on the restart disk and has Euclidean norm at most
\(\sqrt nB_*\). The moving-ball half-strip proof applies to every real
sphere query. Vector-valued Cauchy on the half-radius panel gives the
conservative source Taylor tail

\[
2\sqrt nB_*2^{-K}\le\delta/16
\]

when

\[
K\ge\left\lceil
\log_2\max\{1,32\sqrt nB_*/\delta\}\right\rceil.
\]

Take the maximum of this degree and the core degree. Increasing degree
preserves the earlier defect inequalities. The total Euclidean source error
is then

\[
\delta/48+\delta/16=\delta/12<\delta/8,
\]

which satisfies the assembly interface. Existing parameter jets determine
source jets through degree \(K\); no future coefficient or exact path sample
is needed. The passive activation backend must include degree-\(K\)
compositions with both \(\phi\) and \(\phi'\), already counted in assembly.
The tightened accuracy and added cutoff preserve \(K=O(\log n)\) and
the fixed-parameter \(n^{2+o(1)}\) arithmetic order.

## Remaining scope

Exact-real source construction and the explicit activation-backend contract
are consistent. Approximate scalar activation evaluations require another
error allocation; primitive error and roundoff are not covered. The phrase
about query evaluation cost at requested accuracy must not be used to claim
such a finite-precision theorem.

Analytic regularity alone supplies no efficient computable activation oracle.
The inherited source event retains its eventual-width qualification. Rank
detection, selector conditioning, bit complexity and wall-clock gains remain
outside this audit. Dense-solver comparisons must specify their horizon, step
and accuracy convention. These qualifications are not newly found defects
in the stated conditional exact-real result.

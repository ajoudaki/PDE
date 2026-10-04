# Bounded assembly check of the input/depth refinement

2026-10-04. **PASS for the scoped assembly, conditional on the new source
lemma specified below.** One minor edge-case wording repair is requested.
This is an internal composition check, not an independent promotion review,
and it does not certify the new complex-radius proof or the separate
source-space lower bound.

## 1. Scope and frozen inputs

The assignment is to check INPUT_DEPTH_REFINEMENT.md's norm, physical clock,
labels, actual dense reference, autonomous retained-state contract, state
count, and weaker-error folding corollary. The complete draft and the complete
following inputs were read; no other review verdict or current agent report
was read. The intrinsic-route note is this agent's own frozen derivation.

| File | SHA-256 at this check |
|---|---|
| INPUT_DEPTH_REFINEMENT.md | `def524b223d09747b6ab6ac5d96461ff291c4d2e3b280387bdecbc42efb3d830` |
| STORAGE_QUADRATIC_IMPROVEMENT.md | `ec18f54a3e3977bf9c99ce5c26066f48688848f8b5a9c142b75424badeb025e2` |
| WHOLE_QUERY_RESPONSE_SOURCE.md | `9222c93f0bb9d0c6943f86192cc4a8ad1bbb6b3f6199dd2b056b15fc3adec0d4` |
| INTRINSIC_INPUT_DIMENSION_ROUTE.md | `4714d01381ad2bc0aaf9cfcf1572ffedddff30ff0767188e691df42b55ec13e4` |

The canonical-notation and rigorous-math instructions continue to apply.
The source proof is being checked separately. For this assembly the new
lemma input is: under the same fixed-data assumptions and Y<=c lambda,
with probability at least the assigned confidence for every sufficiently
large width, all required actual dense sources are jointly holomorphic
on the physical-time horizon T=C lambda^(-1)log(en), with common time and
query-angle radius c log(en)^(-1/2), pole-safe activations, bounded mixer
operators, and coordinate magnitude C sqrt(n). The same event retains the
training-carrier bound C S sqrt(log(en)), where S=C Y/lambda. The source
families, separate coordinate accuracy for both paired matrix images, and
finite initialization-derivative construction are those of the whole-query
source note. This check independently verifies the degree and state-count
consequences of those interfaces.

Section 3 of the draft cites a source-space lower bound. Its proof and
numerical rate were not among this assembly's frozen mathematical inputs
and are not certified here. Its stated limitations correctly distinguish
hidden-vector approximation from scalar output approximation and from
arbitrary autonomous representations.

## 2. Reference, labels, norm, and clock

The draft's normalized query v=x/sqrt(d) lies on the unit sphere. Its
f_n(t,v) is the same scalar function as the source/runtime notes evaluated
at x=sqrt(d)v. Thus the two displayed query suprema are identical; there
is no norm conversion or missing factor sqrt(d) in the output error.

The draft uses residual r_a=f_n(v_a)-y_a. The runtime note uses
c_a=y_a-f_n(v_a), so r=-c. With this substitution, the three reference
equations agree exactly, including factors 2/m and 2/(mn). The width-n
initialization is the same realized Gaussian A_0 and W_0, with w_0=0.
No independent reference network, population-training trajectory, averaged
kernel, or rescaled physical time is introduced.

The normalized gap is lambda=min(1,gamma/m), with gamma the smallest
eigenvalue of the specified initialized limiting top-feature covariance.
The inherited sufficient regime is Y<=c lambda. For tanh, gamma<=1 because
gamma<=tr(Q)/m<=1; hence gamma/m<=1 and this is exactly Y<=c gamma/m.
For the general bounded activation class, the cap is explicitly displayed.
Structural smallness constants can be reduced to satisfy all inherited
source and runtime conditions without introducing a new sample-dependent
label factor. The zero-label case is separately stationary.

Both the source horizon and the comparison retain physical time. The
error is uniform over the whole sphere and t in [0,infinity], including
the endpoint. The fixed-data and per-width confidence quantifiers are
stated accurately: this is neither a simultaneous event over all widths
nor a growing-dimension/sample theorem.

## 3. Degree arithmetic and complete retained size

Write ell=log(en), q=ell+log(e/lambda), and let r_n=c ell^(-1/2).
At source coordinate tolerance epsilon=n^(-1), log(C sqrt(n)/epsilon)
is O(ell). Polynomial prefactors from the time interval, strips, and
fixed-dimensional interpolation have logarithms O(q). Consequently the
displayed sufficient degrees are

\[
 p\le C(T/r_n)q=C\lambda^{-1}\ell^{3/2}q,
 \qquad J\le Cr_n^{-1}q=C\ell^{1/2}q.
\]

The time degree and d-1 angular degrees give

\[
 (p+1)(2J+1)^{d-1}
 \le C\lambda^{-1}\ell^{3/2+(d-1)/2}q^d
 =C\lambda^{-1}\ell^{d/2+1}q^d.
\]

There is a fixed number of source families per layer. Exact initial
training features and their initialized images add O(m+d) vectors. If
B_phi bounds the activations, then

\[
 m\lambda\le\gamma\le\operatorname{tr}(Q)/m\le B_\phi^2.
\]

Thus m<=B_phi^2/lambda, and the exact additions are absorbed in the same
bound with constants depending only on fixed structural parameters.
They are not absorbed by making log(n) exceed a power of m. Including
the constant vector and d first-weight columns likewise costs only the
already allowed structural enlargement. Denote the resulting source
dimension by R.

The existing runtime selects N_ell<=9R coordinates in each layer.
Its moving state requires

\[
 dN_1+\sum_{\ell=2}^L N_\ell N_{\ell-1}+N_L+m
\]

reals for first weights, hidden matrices, raw readout, and residuals.
The fixed metric matrices and optional inverses require O(sum N_ell^2).
Training data cost m(d+1). Exact preservation of the full-rank initial
training Gram implies m<=N_L, so training-feature caches, the current
m-by-m Gram and its solve workspace also cost O(R^2). With fixed d,L,
all of these give

\[
 \operatorname{size}\le C(R^2+dR)+Cm(d+1)
 \le C\lambda^{-2}\ell^{d+2}q^{2d}+Cm(d+1).
\]

For ell>=log(e/lambda), q<=2ell, yielding
C lambda^(-2)ell^(3d+2)+Cm(d+1). This confirms draft equations (2)--(3),
including the quadratic prefactor C m^2/gamma^2 when the cap is inactive.
For d=L=2, the old exponent is 2[2(2+5)+1]=30 and the new exponent is
3(2)+2=8. Depth persists in constants, selected layer count, and the
width threshold, not the new displayed logarithmic exponent.

## 4. Autonomous runtime and strict accuracy transfer

The runtime state and equations are unchanged. Its fixed matrices H_ell
are positive and comparable to diagonal positive masses, so source
coordinate errors and pointwise gates have the already proved weighted
norm bounds independent of the smallest selected mass.

Let F_C be its current top training-feature matrix and Q_C=F_C^top H_L F_C.
The effective readout is exactly

\[
 \widehat w_C=w_C+F_CQ_C^{-1}(y-c_C-F_C^\top H_Lw_C).
\]

Multiplication by F_C^top H_L proves y-f_C(training)=c_C at every state
with Q_C invertible. Thus the internally evolved c_C is the actual residual
of the model's own current predictions. Its positive Gram evolution and
raw parameter velocity energy identity preserve the fitting tube globally
under Y<=c lambda. Every hidden update is present. The metric backward
signals and residual Gram are not falsely identified with ordinary
parameter-gradient backpropagation under a non-diagonal metric.

The setup uses finite initial derivatives, initialized arrays, and data.
Both members of each forward/reverse initialized matrix pair receive their
own coordinate error bound and identical scalar coefficient operations.
After selection, the width-n bases, source arrays, and matrices are discarded.
No source interpolation table or prescribed trajectory is an argument of
the runtime. Its matrix solves use current features, current state, and the
retained labels. Unlimited setup work/precision is explicit and does not
exclude any retained coefficients from the count.

The deterministic comparison uses only the source tolerance, exact paired
images, retained-state norm, true training-carrier maximum, and residual
activity. It does not depend on the former smaller source radius. Its bound
at epsilon=n^(-1) has the form

\[
 C_{\rm data}n^{-1}\exp(C_{\rm data}\sqrt{\ell}).
\]

For fixed data this is at most C_data/sqrt(n) at every sufficiently large
width. The C sqrt(n) whole-query source magnitude affects approximation
degrees only; it is not substituted into the training-carrier stability
bound. This distinction is preserved by the source interface.

Both models have their own sphere-uniform tails bounded by
C_data exp(-c lambda t). A sufficiently large structural multiplier in
T=C lambda^(-1)ell makes both tails O(C_data/n). Comparison at T followed
by these tails proves the stated strict bound for all later times and
the endpoint. Neither optimizer stops or freezes at T. Thus draft (4)
follows from the new source lemma and the existing runtime, with no new
population or endpoint assumption.

## 5. Weaker-error folding corollary

For the nontrivial reduction assume r+1<d, where r is the training-span
rank. Choose a fixed orthonormal basis U of that span and a fixed unit
e in its orthogonal complement. The projected first matrix A_0[U,e] has
independent standard Gaussian entries by rowwise orthogonal invariance,
independently of the unchanged hidden matrices. The normalized training
vectors are (U^top v_a,0) in S^r; equivalently the canonical unnormalized
inputs are sqrt(r+1)(U^top v_a,0). Their pairwise inner products and gamma
are unchanged.

The actual first-weight ODE is supported in the training span, so the
projected model has exactly the original training trajectory and physical
clock. This is an exact restriction of the same realization. The passive
columns discarded from the query description remain independent of its
training information, which is the conditioning used in the intrinsic note.

The proved folding estimate has error C_data,eta sqrt(log(en)/n) uniformly
over the original sphere and all time. The strict theorem, applied to the
same realized (r+1)-dimensional restriction, has error C_data,eta/sqrt(n).
Taking each event at half the failure budget and using a union bound does
not require independence. The triangle inequality therefore proves the
weaker error in draft (9).

Runtime stores U, costing dr reals, and evaluates the fixed map

\[
 v\longmapsto
 (U^\top v,\sqrt{\|v\|^2-\|U^\top v\|^2}).
\]

The transverse vector e is needed for initialization only, and no unused
original random columns are retained. O(d+r) current projection/norm
workspace fits within the displayed count. The explicit radial preprocessing
allowance is necessary if the alternative contract demanded a linear first
layer in the original coordinates; the draft states this distinction.

When r+1>=d, using the original representation gives D=d and no folding
cost is needed. Hence the formula with D=min(d,r+1), exponent 3D+2, and
additional O(dr) storage is valid as an upper bound in every case.
The corollary retains the label condition and autonomous own-residual
training. Its additional sqrt(log n) error is not hidden in a constant.
The draft correctly leaves the strict dimension-reduced root-width theorem
open rather than inferring it from the fixed-slice concentration statement.

## 6. Minor wording repairs and disposition

1. In Section 4, introduce e and the folded query only after the branch
   r+1<d. The current paragraph asks for a unit e in V-perpendicular
   before the later full-rank fallback, although no such e exists when
   r=d. The subsequent branch makes the intended valid construction
   clear; this is an edge-case presentation repair, not a change to (9).
2. Section 2's historical sentence that the old endpoint estimate
   multiplied sqrt(log n) at every layer should be phrased more generally
   as propagating a width-dependent lower-layer maximum. The old displayed
   source argument uses a weak log(n) training-carrier cap at that stage.
   This wording does not affect the conditional degree/count calculation.

No blocking assembly defect was found. The strict result is a valid
composition if the new source lemma supplies the stated radius, bounds,
probability event, paired approximation, and initialization-only interfaces.
This report does not turn those lemma hypotheses or the separate lower-bound
claim into reviewed theorems; their assigned checks remain necessary.

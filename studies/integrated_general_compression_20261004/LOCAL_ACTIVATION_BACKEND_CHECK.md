# Cross-route audit of the real-value activation backend

2026-10-06. Complete mathematical reconstruction audit; no experiment or
implementation was run. This is an internal cross-route check, not a promotion
review. The reviewer authored the assembly route and had previously audited
the Taylor core and real-node Picard alternative. No independence from that
study context is claimed.

**Verdict:** no substantive defect was found in the frozen activation-backend
candidate. Its real-node polynomial approximation controls values and the first
two derivatives on the needed complex domain; its perturbed field has the
claimed local restart and original-field defect bounds. Source error and exact
pairing are preserved. The stated near-quadratic arithmetic remains subject
to the inherited ordinary scalar-evaluation contract, source event and
exact-real interpretation.

## Inputs and reading

Read LOCAL_ACTIVATION_BACKEND.md in full, all 507 lines, at SHA-256

25e8c6dd6381d46b561a839339d538ea38926f4130af62dfb848f91cc6f54cbb.

Its corrected core, read completely and separately audited, is
LOCAL_CONTINUATION_SETUP.md at

c4c12b38e49e37ac5096e69ceabee1d41be6ad6bc4a1c57ece943959ef425bbe.

Other dependencies used were:

- RESULT.md:
  c2cbd1bb0e6a39de87181df89be977eaf2e272fda4f1459ac934396d84e1b278.
- POLYNOMIAL_SETUP_ODE_ROUTE.md:
  46e9c2b4ed9f118b3812ce8208d26ebbfa9c9f1fb3efc6e68f3854e0be8cf5a6.
- POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md:
  2d58da5a418f6d5a8f1bb54ce343b205978770424c0940789b15231e251daf42.
- docs/notation.qmd:
  78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023.

Both earlier route notes were read in full. Relevant complete RESULT.md
sections include the source constants and whole-sphere domain, initial sphere
maximum, complex source maxima, all-horizon extension, source pairing and
exact initial additions, and setup/activation cost derivations. The underlying
probabilistic source event is imported, not independently re-proved.

The accessible rigorous-math and conjecture-audit instructions and repository
notation contract were applied. The prescribed canonical-notation skill
remained inaccessible, as already disclosed. No other study or archive was
read.

## 1. Real-part bound and nested ellipse geometry

The initial sphere-coordinate maximum and source time-velocity bound give the
first terms of \(Z_*\). Integrating
\(2\rho SU\sqrt{\log(en)}\) against the existing activity bound costs
at most \(US^2\sqrt{\log(en)}/2\), below the stated conservative allowance.
The short complex segment contributes at most \(a/8\).
For late times the core forward endpoint estimate contributes
\(\sqrt nP_*Z_n\) relative to the state at \(T_0\). Thus (A1) covers every
real query on the exact complex time disks; no complex query input is needed.
The core moving-ball radius contributes at most \(a/16\) to each coordinate,
giving (A2).

The outer ellipse has imaginary semiaxis \(31a/64<a/2\), and
\(B=8(Z_*+a+1)>8a\). Integrating the derivative of \(\operatorname{arsinh}\)
over the interval in (A3), where that derivative exceeds \(1/2\), gives
\(\Delta\ge a/(64B)\). The other stated bounds on \(\Delta,\tau_o\) follow
from their positive arguments being less than one.

For a point within distance \(a/512\) of (A2) and its Cauchy circle of
radius \(a/512\), the total coordinate perturbation is at most \(a/256\).
Its normalized real coordinate is less than \(1/8\), because
\(Z_*+a/16+a/256<Z_*+a+1=B/8\). Its normalized imaginary coordinate is
at most \(226/232\). The squared sum
\((1/8)^2+(226/232)^2<1\) places the entire disk strictly inside the inner
ellipse. This verifies the nested complex domain actually used by substitution
and derivative estimates.

The segment from zero to any outer-ellipse point remains in the half-strip.
Linear activation growth then gives \(M_\phi=b+s(B+a)\):
\(B\cosh\tau_o=\sqrt{B^2+(31a/64)^2}\le B+a\).

## 2. Real-node coefficients, aliasing and derivative accuracy

The even function \(g(u)=\phi(B\cos u)\) is analytic in the stated strip.
Fourier contour translation gives
\(|\widehat g_k|\le M_\phi e^{-|k|\tau_o}\).
For positive degrees its Chebyshev coefficient is \(2\widehat g_k\);
the degree-zero coefficient has no factor two. The finite cosine formulas
in (A7) have exactly those normalizations.

On the inner ellipse, \(|T_k(z/B)|\le e^{k\tau_i}\). Consequently the
exact degree-\(D\) tail is bounded by

\[
\frac{2M_\phi e^{-(D+1)\Delta}}{1-e^{-\Delta}}
\le\frac{4M_\phi}{\Delta}e^{-(D+1)\Delta}.
\]

Absolute Fourier convergence allows the discrete average to select the
frequencies \(k+qN_\phi\). For \(0\le k\le D<N_\phi/2\), the two
geometric alias tails, and the positive-mode factor two, give precisely the
stated safe factor four. Since \(N_\phi=4(D+1)\) and
\((D+1)\Delta\ge1\), its denominator is at least \(1/2\).
Summing the alias error on the inner ellipse yields the intermediate bound

\[
8M_\phi(D+1)e^{-2(D+1)\tau_o}.
\]

For \(x=(D+1)\tau_o\), use \(xe^{-x}\le1\) and
\(\tau_o\ge\Delta\) to obtain the final (A9). Adding (A8) and (A9)
gives at most
\(12M_\phi\Delta^{-1}e^{-(D+1)\Delta}\le\epsilon_p/2\), by (A6).
This checks the finite coefficient rule, not only the exact Chebyshev tail.

A nodal value error at most (A10) changes each coefficient by at most
\(2\epsilon_{\rm eval}\). Summing its \(D+1\) inner-ellipse contributions
costs at most
\(2(D+1)e^{D\tau_i}\epsilon_{\rm eval}=\epsilon_p/2\).
Thus the candidate correctly reserves half the polynomial error for such
value-call error.

Cauchy's formula on the verified radius-\(a/512\) disks multiplies the
value-error bound by \(512/a\) or \(2(512/a)^2\) for the first or second
derivative. These are exactly the factors in \(C_a\). This proves (A11)
throughout its stated neighborhood. No complex activation evaluations or
high-order derivative values are required for this construction.

## 3. Perturbing the network at one parameter value

At the first layer the original and polynomial preactivations agree. At
later layers their RMS difference is at most eleven times the preceding
feature discrepancy. Splitting
\(\psi(z^p)-\phi(z^0)\) through \(\phi(z^p)\) gives
\(U_j=1+11sU_{j-1}\). The constraint
\(\epsilon\le a/(5632\sqrt nU_*)\) gives

\[
11\sqrt nU_*\epsilon\le a/512.
\]

Hence each polynomial preactivation remains in the region where (A11) was
proved, so the induction is valid at every layer. The extra feature RMS is
at most one.

For backward error, the carrier difference costs \(11Q_{j+1}\epsilon\),
multiplied by the polynomial gate bound \(s+1\). The original carrier
multiplied by the derivative-approximation error costs \(K_j\epsilon\).
Its multiplication by the original gate change costs
\(11t_2MU_{j-1}\epsilon\). These are the three terms of (A15);
the top carrier difference is zero, correctly handled by \(Q_{L+1}=0\).

The gradient-block discrepancy consists of the response error times the
polynomial feature, plus the original response times feature error. Their
RMS bounds give exactly \(Q_\xi\) in (A17). The prediction discrepancy
is at most \(RU_L\epsilon=Q_f\epsilon\). Under
\(Q_\xi\epsilon\le1\), the polynomial gradient has norm at most \(G+1\).
Splitting the residual-gradient product gives

\[
\|\widetilde F-F\|_2
\le[2Q_f(G+1)+2(2Y+G)Q_\xi]\epsilon=C_F\epsilon.
\]

This is a vector-field norm bound uniform on the complex moving ball.
It includes all trainable blocks and the change in the residual.

## 4. Parameter-direction Cauchy and modified-field continuation

For a state in the radius-\(b_n/2\) ball and any unit complex parameter
direction, its radius-\(b_n/2\) scalar disk lies in the full radius-\(b_n\)
ball. Applying vector-valued Cauchy to \(\widetilde F-F\) gives
\(2\zeta_F/b_n\). Taking the supremum over unit directions is exactly
the operator norm. There is no coordinate derivative estimate requiring
an extra \(\sqrt P\).

Because \(\zeta_F\le b_nL_n/4\), the polynomial field is at most
\(3L_n/2\)-Lipschitz in the smaller ball, below the claimed \(2L_n\).
On the disk of radius \(\widehat R_n\), the modified error map contracts
by at most \(1/4\). Its forcing contribution is at most
\(\widehat R_n\zeta_F\le b_n/32\). Adding its anchor and Lipschitz terms
gives \(9b_n/32<b_n/2\). The fixed-point error is at most

\[
\frac{b_n/8+b_n/32}{1-1/4}=\frac{5b_n}{24}<\frac{b_n}{4}.
\]

Its velocity is bounded by \(V+\zeta_F\le2V\). Vector-valued Cauchy gives
Taylor tail \(2V\widehat R_n2^{-K}\). When this is at most \(b_n/4\),
the polynomial stays in the smaller ball where the field Lipschitz bound
applies. The geometric derivative tail plus field mismatch gives (A21).

The first cutoff in (A22) ensures that the integrated polynomial-field defect
is at most \(e_d/2\), using \(2K+5\le4\,2^{K/2}\). The perturbation
defect integrates to at most \(e_d/2\) by (A19). The second cutoff ensures
the required parameter tail. The prefix induction and the original real
defect theorem therefore give (A23), simultaneously preserving restart
accuracy and half of the nodal source allowance.

The defect throughout is measured against the original field \(F\).
The polynomial dynamics are a disposable computation; their use does not
replace the target dynamics in the theorem.

## 5. Passive source error and exact initialization

For real passive queries the original carrier maximum is bounded by
\(M_q=\sqrt n\max_jK_j\). Applying the same backward error recurrence,
then converting RMS to coordinate error, gives \(C_p\epsilon\) for every
source family. The initialized-image factor eight is included in \(C_p\).
The final scalar choice (A25) makes this error at most
\(\delta_{\rm node}/2\). Original-field parameter error contributes at
most the other half by (A23). All denominators in (A25) are positive under
the stated positive-label branch.

Initialized images are formed directly from computed base vectors using
\(W_0\) or \(W_0^T\). Applying the same finite quadrature therefore
preserves pairing exactly, even though source values and training field are
approximated.

The candidate separately evaluates exact initialized training features with
the original activation. It does not use the polynomial initialization to
claim equality of the original training Gram. These initial additions need
only original activation values because backward fields initially vanish.
The retained compressed runtime continues to use the original activation and
derivative. This is the required distinction between disposable setup
approximation and the final model.

## 6. Degree and operation counts

At fixed parameters \(C_p=O(n)\), while training perturbation coefficients
are \(O(\sqrt{\log n})\). The signed stability amplification is
\(\exp(O(\sqrt{\log n}))\). Hence (A25) only asks for polynomially small
\(\epsilon\). Since \(B=O(\sqrt{\log n})\) and
\(\Delta^{-1}=O(B/a)\), the activation polynomial degree is
\(D=O((\log n)^{3/2})\). Also \(D\tau_i=O(\log n)\), so (A10)
requires only polynomially small real value-call error. These are precision
requirements, not bit-complexity estimates.

The coefficient transforms and optional derivative-polynomial preparation
cost \(O(LD^2)\) arithmetic. An online degree-\(K\) activation composition
can retain the Chebyshev recurrence coefficients through all \(D\) degrees.
For each recurrence product, summing the convolution lengths through degree
\(K\) costs \(O(K^2)\), giving \(O(DK^2)\) time and \(O(DK)\)
workspace. At a fixed series degree the recurrence is evaluated in increasing
Chebyshev degree; the input coefficients at that degree are already available.
Thus the online claim does not require an uncounted full recomposition after
each new coefficient.

Combining this with materialized dense parameter jets gives exactly the
training terms in (A27). Passive polynomial forward/backward evaluation adds
\(LnDN_tN_x\); initialized images remain inside \(PN_tN_x\).
Exact initialized additions cost \(mP\) arithmetic and \(Lmn\) original
scalar value calls. The \(PK\), \(LmnDK\), polynomial coefficients and
query buffers are present in (A28). Quadrature, source selection and model
assembly remain additional, as stated.

At fixed structural parameters all these bounds are
\(n^{2+o(1)}\), including the explicitly counted scalar-call counts.
The Euler comparison is valid for its stipulated inverse-square-root step
and horizon convention; it is not a necessary-step theorem or a separation
from efficient high-order dense solvers.

## Remaining qualifications

The candidate supplies the promised value-based setup backend. Its optional
inexact value calls have an explicit error allowance, while exact initialized
additions retain the inherited exact-real convention. This is not a complete
finite-precision implementation: arithmetic roundoff, exact initial-feature
computation, rank detection, selector conditioning and bit cost remain outside
the claim.

Ordinary original activation values still require a specified representation
or separately charged primitive. The source event and its width qualifications
are unchanged. No further must-fix mathematical or arithmetic-count defect
was identified at the frozen hash.

## Qualification of the notation-only final version

The later presentation-cleaned candidate has SHA-256

cbf26326c081fc19da31f5d38781eff2dfa2a5b97dee12eb1a8022770a2843e4.

The original reviewed hash above remains the record for the complete audit.
Verified the final version by reversing its declared edits in memory: removed
the four newly added provenance lines, replaced the 18 explicit occurrences
of \(\log(en)\) by the former logarithm alias, and restored that alias's
defining sentence. A read-only Node computation of SHA-256 then returned
exactly the original reviewed hash

25e8c6dd6381d46b561a839339d538ea38926f4130af62dfb848f91cc6f54cbb.

The reversal changes the line count from 511 back to 507 and reproduces the
old candidate byte for byte. No candidate file was written. Thus the cleanup
introduces no scientific change beyond the stated notation expansion and
provenance text. The audit verdict and qualifications apply to the final
candidate hash as well.

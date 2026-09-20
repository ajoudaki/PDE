# Independent internal audit of the global positive route

Date: 2026-09-18. This is an isolated internal mathematical audit, not a
promotion review or a proof of convergence for three nonparallel inputs.
Only this report is written. No numerical experiment was performed.

## Verdict and exact scope

**PASS for the stated scalar theorem and its canonical p=1 application,
including convergence of all moving blocks; PASS for the multi-residual
identities, axis jet independence, divided-difference scaling, and conditional
small-correction obstruction.** I found no blocking mathematical error in
these claims. The regularity statement about uniform third-order Taylor
remainders must be understood in bounded characteristic-displacement
neighborhoods, as used for existence and movement in Section 2. It should
not be advertised for arbitrary balls in the physical L2 metric. The
conditional small-correction conclusion itself remains valid even for
strong L2 convergence of the lower row, by a C2 argument given below.

The candidate explicitly leaves the nonparallel three-input convergence
problem open. Nothing checked here resolves that problem, proves a sign for
its residual-rotation contribution, or proves a nonzero limiting angular
curvature. These are limitations of the proved scope, not flaws in the
stated scalar theorem.

Scientific sources actually read:

| Source | Actual reading | SHA256 of whole file |
| --- | --- | --- |
| `global_positive_route.md` in this study | Complete frozen candidate, lines 1–346 | `36830e4ad5d89ce983c2c0144055dc6e52c82b6192f8b238bd5d41a4ac18b487` |
| `initial_geometry.md` in this study | Complete dependency | `6856fb3d2cca5d59d1b00c4bd3cf87dd74f87315999e244b42dd1662647f091d` |
| `docs/observable_p1.md` | Complete | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` |
| `docs/global_nonlinear.md` | C.4.7.9.3–4 completely, lines 12249–12377; C.4.7.10.D.3 completely, lines 15146–15528 | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |

The whole-file hash of `global_nonlinear.md` does not imply whole-file
reading. Its section headings were inspected only for navigation. The
required `/etc/codex/skills/solve-math-rigorously/SKILL.md` was read completely
(SHA256 `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`).
The scientific hashes were checked again after the mathematical audit and
were unchanged. No study README, study history, Git history, code, other
study, previous audit, competing derivation, external scientific source,
or numerical result was read. In particular `stationary_geometry.md` was
not supplied to this audit and was not read. The candidate's descriptions
of what that file does or does not establish are therefore not verified
here; none is needed for the affirmative conclusions of this audit.

## 1. The abstract scalar argument is valid

An explicit sufficient interpretation of the regularity premise is that
the hidden space is a real Hilbert space X, H is C1 from an open subset of
X into the readout Hilbert space, and the stated physical solution is C1
and exists at every finite time. The candidate separately assumes local
well-posedness. These hypotheses give continuous DH along the solution
and justify every derivative actually used; a second hidden derivative
of H is unnecessary.

With e=1-F and c(0)=0, differentiating the unhalved loss gives precisely

\[
 \dot c=2eH,\qquad \dot\vartheta=2e(DH)^*c,
 \qquad \dot e=-2e\bigl(\|H\|^2+\|(DH)^*c\|^2\bigr).
\]

The coefficient is continuous and finite on each compact physical-time
interval. Therefore e is its positive exponential integrating factor,
starting at one; there is no finite-time division by zero in the clock
ds/dt=2e. The clock image can have a finite upper endpoint, which is
compatible with the proof.

In that clock c_s=H and c_ss=DH(DH)*c. The hidden derivative and its
adjoint are taken in the same fixed Hilbert metric, so the final pairing
is exactly the nonnegative squared norm asserted in (4). Near zero,
c=sH0+o(s), whence q>0 and q_s tends to ||H0||. On the connected positive
interval of q, q_ss>=0 implies q_s>=||H0|| and q>=s||H0||. Continuity
rules out a later zero. Consequently

\[
 F_s=(q q_s)_s=q_s^2+q q_{ss}\ge\|H_0\|^2.
\]

Multiplication by ds/dt=2e gives e_dot<=-2||H0||^2 e, and squaring gives
the claimed loss rate **4||H0||²**, not 2||H0||². Every step remains on
the attained clock interval. The zero of q at initialization is handled
by the one-sided limit rather than an illicit division there.

There is no frozen hidden block in this proof. In fact Cauchy–Schwarz also
gives ||H||>=q_s>=||H0|| along this particular initialized trajectory;
the feature lower bound is a consequence, not an extra assumption.

## 2. Hilbert derivatives and characteristic existence are compatible

The source constructs the closure in the Banach space of bounded w-g,
bounded c, and finite M. This is its existence topology. The metric of
the gradient is nevertheless the physical L2/L2/Frobenius metric.
The distinction is harmless here because the finite population contraction
makes the required feature map genuinely C1 on the hidden Hilbert space.

For the signed feature H=y tanh(b2^T M a), put
g1=sech²(w·u), g2=sech²(b2^T M a), and
d=E2[b2 c g2]. For a variation (v,L) in L2 times the coefficient matrix
space, its derivative and Hilbert adjoint are

\[
 Da(w)v=E_1[b_1g_1(v\cdot u)],
\]
\[
 DH(w,M)[v,L]
 =y g_2 b_2^T\{L a+M E_1[b_1g_1(v\cdot u)]\},
\]
\[
 (DH)^*c
 =\bigl(y g_1(b_1^TM^Td)u,\ y d a^T\bigr).
\]

For example, bounded tanh'' and the vector feature envelope B1 give
|a(w+v)-a(w)-Da(w)v|<=C B1||v||2². Moreover the operator norm of
Da(w)-Da(w') is at most C B1||w-w'||2. The remaining operations pass
through a finite vector and bounded b2. Thus DH is a continuous bounded
Hilbert derivative. The displayed adjoint never requires multiplication
of two unrestricted L2 fields at the same unintegrated lower mark. This
explicitly validates the adjoint and chain rule used in (3).

The signed factor y in both adjoint blocks is necessary and agrees with
the source's residual f-y, since f-y=-y(1-yf). It does not change any
norm estimate. A law on (u,y),(-u,-y) has exactly the same scalar loss
and vector field because the bias-free prediction is odd in its input.

The read source continuation argument applies to fixed-order closure for
arbitrary unit-input bounded-label laws, through each finite physical
time. The separate time-40 support restriction on identification with
the full neural population does not restrict this fixed-order existence
argument. The candidate does not import that full-model identification.

## 3. Initialization and finite-endpoint movement bounds check

The complete initialization dependency retains the reverse-reuse term
tau gamma and the right normalization transpose. I checked its scalar
regression and positivity proof: v>1/4 gives tau>1/7;
alpha<6/7<arsinh(1) gives jU/jL<2; conditional Gaussian integration by
parts supplies Var(k|h)>=tau j(h)²; these imply 0<B<1/jL and then the
strict lower bound for ell'. The Gaussian correlation derivative has the
claimed sign, with correlation endpoints covered by continuity. Hence
V(u)=(F(u1),F(u2)) is nonzero for every unit direction. The upper mark law
has positive density on its open square, so tanh(b2^T V(u)) has strictly
positive L2 norm. This proves k0>0 for every direction without an axis
rotation argument.

I also checked the dependency's finite feature independence argument,
stationarity classification, compact every-angle Gram minimum, and
noncovariance argument. The asymptotic separation of distinct positive
tanh frequencies handles even collinear upper vectors of different
lengths. The correlation third derivative and the strictly decreasing
even derivative of psi give the claimed obstruction to full rotational
covariance. No error in these parts invalidates the required initialization
or jet properties.

In the scalar clock, F>=k0 s and F<1 imply s<1/k0. Let s_* be the
increasing clock limit. Normalized feature synthesis is contractive, so
||a||<=1, ||d||<=||c||2, and ||D||op<=2. Therefore the exact speed bounds are

\[
 \|c_s\|_\infty\le1,\quad
 \|M_s\|_F\le s,\quad
 \|w_s\|_\infty\le B_1(2+s^2/2)s.
\]

Integrating yields exactly (6), including the coefficient **1/8** of
s^4 in the row bound. Here B1 means the essential supremum of the
Euclidean norm of the feature column; the larger coordinate-envelope
constant used in the source would also suffice.

Convergence follows from these speed bounds on the finite interval
[0,s_*), not from boundedness alone: integrating between two clock times
gives a Cauchy estimate in L∞ for c and w-g, and in Frobenius norm for M.
Their spaces are complete. Prediction continuity identifies the endpoint,
and the exponential bound gives yf_infinity(u)=1. This is an endpoint
at infinite physical time; no finite-time exact fit is claimed.

## 4. The multi-input residual term has the stated factors and sign

Interpret the finite data space as L2(mu), removing zero-mass atoms or
quotienting their null coordinates. With that convention the weighted
adjoint in K=DF(DF)* includes exactly one data weight in each contraction.
For rho>0,

\[
 \dot\rho=-2\rho k,\quad
 \dot v=-2(K-kI)v,\quad
 \rho_s=-k,\quad v_s=-(K-kI)v/\rho.
\]

Holding v fixed for the state derivative gives c_s=H_v and
theta_s=(Dtheta H_v)*c. The actual derivative of c_s must additionally
differentiate v, giving the stated H_{v_s} term. Since
<v,v_s>_mu=0 and f=y-rho v,

\[
 \langle c,H_{v_s}\rangle=\langle y,v_s\rangle_\mu,
 \qquad
 k=\|H_v\|^2+\|(D_\vartheta H_v)^*c\|^2.
\]

These yield (9) exactly. Projecting y onto the orthogonal complement of
v proves (10), since the projection has norm sqrt(1-beta²) for unit
binary labels and a probability law. The independent identity
q q_s=beta-rho gives (q q_s)_s=beta_s+k and confirms all factors.

Positive semidefiniteness alone cannot discard beta_s. For example, even
a constant diagonal positive kernel with two unequal eigenvalues rotates
a residual initialized with a nonzero component in each eigendirection
away from its initial direction, so beta decreases. This is sufficient
to refute an algebraic nonnegative-sign inference from K>=0; it is not a
counterexample to convergence in the canonical three-input problem.
The candidate properly restricts its q identity to q>0 and its clock to
rho>0, and does not transfer the scalar no-return proof for q to this case.

## 5. Axis jets and the conditional correction obstruction

Section 4 implicitly chooses the positive axis target (u,y)=(e1,1),
as is required by its statements f(0)=1 and c_s=tanh(b_x z). Under this
choice its invariant class is correct: w2 stays g2; the first lower
coordinate evolves independently of the second pair; the first middle
row has only axis entries; the second row is its initialized perpendicular
row; c depends only on b_x. Independence, centering, and upper parity
make every omitted velocity zero. The limiting state has the same class.

Differentiating z=m·a along the scalar clock gives

\[
 z_s=d\{\|a\|^2+E[v_1^2\operatorname{sech}^4w_1]\}.
\]

As long as z>0, integrating c_s shows b_x c>=0, so d>=0. Initialization
has z>0; monotonicity up to a hypothetical first zero rules it out. At
the endpoint z remains at least its positive initialized value. The
perpendicular first derivative is

\[
 \ell=\frac{E[\psi(G)G]}{c_*}\,
             E[\operatorname{sech}^2 w_1]>0.
\]

The first factor is positive by the odd strict increase of psi; the
second is positive since the limiting w1 is finite almost surely. Axis
reflection makes the other first derivative zero and the perpendicular
second derivative zero. Thus the vector jets and all three formulas in
(12) are correct. A linear relation among them first loses h'_0 by
oddness in b_y, then loses h''_0 by its nonzero b_y² coefficient, then
loses h0. Continuity and positive density justify working throughout the
open square. The three-function jet Gram is positive definite, including
at the scalar endpoint.

For exact divided-difference features (h0,B_delta,C_delta), reconstruction
is

\[
 h(-\delta)=h_0-\delta B_\delta+\tfrac12\delta^2 C_\delta,
 \qquad
 h(\delta)=h_0+\delta B_\delta+\tfrac12\delta^2 C_\delta.
\]

The feature map for (h0,B_delta,C_delta) is uniformly bounded above and
below near zero. Reconstruction is a fixed invertible matrix combined
with diag(1,delta,delta²). The singular values therefore have two-sided
orders 1,delta,delta², and the Gram eigenvalues have orders 1,delta²,delta⁴.
Fixed positive sample weights preserve these orders. Weights vanishing
with delta would require a separate statement, which the candidate does
not make.

At the fitted reference, all three new targets are 1. The readout
correction therefore has exactly the second divided-difference pairing
displayed before (13). Its right side tends to -f''(0), while the feature
there tends in L2 to h''_0. Cauchy–Schwarz proves (13); jet independence
ensures its denominator is nonzero. No nonzero value of f''(0) has been
proved, and the candidate correctly keeps this an explicit condition.

For movement of all parameters, a precise version is: no sequence of
exact three-point interpolants can converge to this reference in
(L2 row, L2 readout, Frobenius matrix) if its f''(0) is nonzero. Indeed,
the first two angular derivatives of the contracted lower vector are
expectations of bounded gates times at most two factors of w. Strong
L2 convergence makes quadratic products converge in L1; bounded gate
differences multiplying the fixed limiting |w|² vanish by dominated
convergence in probability. The resulting convergence of a and its
first two angular derivatives is uniform in angle. The finite upper
contraction then gives uniform C2 convergence of the predictions.

For each interpolant f_delta the centered second divided difference is
zero. Its exact integral representation is

\[
 0=\int_{-1}^{1}(1-|r|)f_\delta''(r\delta)\,dr.
\]

Uniform C2 convergence makes the limit f_reference''(0), a contradiction
when that derivative is nonzero. This verifies the all-parameter
small-correction obstruction without silently freezing hidden blocks.

## Precision points and remaining limitations

1. Candidate lines 237–238 should specify that bounded neighborhoods for
   the O(theta³) remainder are in bounded displacement/readout/matrix
   norms. Gaussian moments give uniform third derivatives there.
   An unrestricted L2 ball need not have bounded third moments. The
   C2 argument above avoids this stronger requirement for the convergence
   obstruction.
2. Candidate line 225 should explicitly identify the positive e1 axis
   reference. Its following signs and target value already select that
   case, so this is a clarification rather than a change to the proof.
3. The weighted data metric should explicitly mean L2(mu) if zero
   sample weights are allowed. Deleting null atoms leaves all identities
   unchanged.
4. Assertions describing `stationary_geometry.md` were not checked
   because it is outside the assigned scientific input scope. The
   initialization, scalar theorem, and jet obstruction do not depend on
   those assertions.

None of these points supplies a three-input convergence theorem. The
sign/control of beta_s and the effect of a finite curvature-mode change
remain open in the candidate. In particular an internal PASS for the
scalar result is neither promotion nor completion of the original
three-input research target.

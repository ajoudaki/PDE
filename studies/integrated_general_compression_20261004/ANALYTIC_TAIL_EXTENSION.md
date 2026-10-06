# All-time analytic source domain and variable-tolerance comparison

2026-10-05. New deterministic extension within the integrated study.
This note preserves the original model, label allowance, physical time,
whole-sphere norm, and initialization-only preprocessing contract. It is
conditional on the existing source event, not a new Gaussian insertion
theorem. The only additional width requirements below are deterministic,
eventual, and independent of the approximation order and tolerance.

## 1. Inputs and claim

Use the complete source recurrences and event in
[UNBOUNDED_COMPRESSOR_BRIDGE.md](UNBOUNDED_COMPRESSOR_BRIDGE.md), the
all-time dense fitting theorem in
[GENERAL_EXPLICIT_FITTING.md](GENERAL_EXPLICIT_FITTING.md), and the
independent compact fitting theorem in
[EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md](EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md).
The label allowance is their existing intersection, without modification.
The comparison argument is
[COMPACT_FULL_LABEL_RANGE.md](COMPACT_FULL_LABEL_RANGE.md), §§2–7.

In this proof only, write
\(\lambda=\gamma/m\), \(S=16Y/\lambda\), and
\(T_0=32\lambda^{-1}\log(en)\). The source supplies the positive
time and query radii
\[
r_t=\frac{a}{64YSU\sqrt{\log(en)}},\qquad
r_q=\frac{\min\{1/8,a/(8V)\}}{\sqrt{\log(en)}}.
\tag{1}
\]
Here \(a\) is the activation strip width and \(U,V\) are precisely
source (25), evaluated at the actual activity \(S\). All symbols in
this paragraph are local source coefficients, not extra model orders.
The source event gives joint holomorphy through \([0,T_0]\) and the
intrinsic query tube of radius \(r_q\), with all preactivation imaginary
parts at most \(a/4\), by source (32).

After an additional explicit eventual deterministic width condition,
the same time/query radii work over **every finite real time interval**.
The same initialization event works for every such interval simultaneously.
Consequently, for every source-coordinate tolerance
\[
0<\eta\le\min\{1,Y,S\}
\tag{2}
\]
and every finite horizon \(T\), paired approximation/selection on that
domain gives a compact model with
\[
\begin{split}
\|f_{\mathrm{compact}}-f_n\|_*
\le{}& C\beta^{CL}\frac{Y}{\lambda}
 (1+\lambda^{-1/2})\left[
 \eta e^{C\sqrt{\log(en)}}+e^{-\lambda T/4}\right].
\end{split}
\tag{3}
\]
This is uniform over the entire real training trajectory, including
endpoints. Selection and initialization requirements are those proved in
[COMPACT_VARIABLE_SOURCE.md](COMPACT_VARIABLE_SOURCE.md), not an
assumption that an arbitrary smaller network has the required source
isometry. Constants denoted by \(C\) are numerical and may be enlarged.
The power envelope in (3) holds on the full recurrence allowance.

## 2. A small parameter ball around the last source time

Use the dense parameter Hilbert norm
\[
\|\theta\|_{\rm par}^2=
 \|A\|_F^2/n+\sum_{j=2}^L\|W^{(j)}\|_F^2+\|w\|_2^2/n,
\]
and its complex Euclidean extension. Write \(H_j,P_j\) for source
(5)–(6), \(H_L\) for its last feature bound, and let
\(P_* =\max_jP_j\). The unweighted covariance recursion implies
\(\sqrt\lambda\le H_L\). The real fitting proof improves all
operator caps below \(8+1/8\), and gives
\(\|w(t)\|_2/\sqrt n\le2Y/\sqrt\lambda\le SH_L/8\).

At the real state \(\theta(T_0)\), every query in the closed source
tube has preactivation imaginary part at most \(a/4\). On the ball
of parameter radius
\[
b_n=\min\left\{\frac14,\frac{SH_L}{4},
                       \frac{a}{8\sqrt n P_*}\right\}
\tag{4}
\]
around that state, all query preactivations have imaginary part below
\(3a/8\). To verify this without assuming the conclusion, follow a
straight parameter segment until the first exit from the safe strip.
Source (6)'s forward derivative recurrence bounds the normalized
preactivation differential by \(P_j\) times parameter displacement:
the first direct map has norm at most two, and the later direct matrix
maps cost at most \(H_{j-1}\), with propagation \(10s\).
The coordinate differential is therefore at most \(\sqrt n P_j\)
times the displacement. Equation (4) limits it to \(a/8\), improving
the stopped boundary. The operator norms remain below ten and the
readout RMS below \(SH_L\). Linear growth of the activations then
gives exactly the complex feature and response RMS bounds of source
(5)–(6). No coordinate maximum for a passive-query response is needed.

Let \(\mathcal K\) be the finite source coefficient in §8:
\[
\mathcal K=H_L^2+S^2\left[\tau_1^2+
                         \sum_{j=2}^L\tau_j^2H_{j-1}^2\right].
\tag{5}
\]
On this ball the complex normalized tangent Gram has operator norm at
most \(\mathcal K\), and the physical velocity obeys
\(\|\dot\theta\|_{\rm par}\le2\sqrt{\mathcal K}\,\rho\),
where \(\rho=\|f-y\|_2/\sqrt m\). These bounds use absolute
Cauchy–Schwarz on the algebraic, non-Hermitian complex Gram, not positivity.

## 3. Uniform late-time analytic continuation

The dense energy identity and Gram margin imply, starting at any real
time \(t\),
\[
\int_t^\infty\|\dot\theta(s)\|_{\rm par}\,ds
 \le \frac{2\rho(t)}{\sqrt\lambda}
 \le \frac{2Y}{\sqrt\lambda}e^{-\lambda t/2}.
\tag{6}
\]
Indeed \(-\dot\rho\ge\lambda\rho/2\) and
\(\|\dot\theta\|_{\rm par}^2=2\rho(-\dot\rho)\) imply
\(\|\dot\theta\|_{\rm par}\le2(-\dot\rho)/\sqrt\lambda\).
The zero-residual case is stationary and follows by continuity.

The original width conditions include
\(4\mathcal K r_t\le\log2\) and \(r_t\le1/8\).
Impose additionally
\[
\left(\frac{2Y}{\sqrt\lambda}
             +8Y\sqrt{\mathcal K}\,r_t\right)(en)^{-16}
 <\frac{b_n}{2}.
\tag{7}
\]
This is an explicit, eventually true condition: its left side is a fixed
coefficient times \(n^{-16}\), whereas (4) is bounded below by a
fixed positive multiple of \(n^{-1/2}\). It is independent of \(T\)
and \(\eta\); it does not shrink the label allowance.

For any real anchor \(t\ge T_0\), solve the analytic finite-dimensional
ODE on a complex disk of radius \(2r_t\) about \(t\), stopped in the
ball (4). Along a radial segment of length at most \(2r_t\), the exact
residual equation and (5) give
\[
\rho(z)\le\rho(t)e^{2\mathcal K|z-t|}\le2\rho(t),
\qquad
\|\theta(z)-\theta(t)\|_{\rm par}
 \le8r_t\sqrt{\mathcal K}\,\rho(t).
\tag{8}
\]
Together with (6), these inequalities keep the solution strictly inside
half the ball (4), by (7). The local holomorphic ODE theorem here follows
from Picard iteration on a smaller ball: the vector field is holomorphic
and has bounded derivative on every closed smaller parameter ball, so
the integral map is a contraction for a sufficiently short complex time
disk. The strict interior bound (8) permits repeated continuation; a
finite-radius singularity inside \(|z-t|<2r_t\) would have a bounded
state with positive distance from the boundary, where that same local
construction extends it. Uniqueness glues overlapping analytic germs.

All anchors use the same fixed ball around \(\theta(T_0)\), rather
than accumulating small errors over successive time steps. This proves
joint time/query holomorphy for every later anchor. It agrees with the
original source function on overlaps and covers every finite extended
source rectangle. The disks of radius \(2r_t\) contain the late-time
rectangle with strict slack, and the parameter ball leaves a strict
preactivation margin below \(a/2\). The original closed domain already
has a holomorphic neighborhood. Compactness of each finite closed
time/query domain therefore gives the required neighborhood without
shrinking either radius. There is no union over new random events and
no long-horizon Gaussian net.

All four source families, including initialized images and passive
backward fields, have the same RMS bounds as on the original domain.
Thus their coordinate modulus is still bounded by \(M_0\sqrt n\)
with the original \(M_0=10\max(H_{\max},\max_j\tau_j)\).

## 4. Real carrier maximum after the original horizon

The comparison proof needs a maximum only for the actual real training
carriers. Source §12 already extends their real running maximum to all
time by the fitting tail. Here is a direct bound sufficient for its use.
For fixed depth, forward subtraction and backward subtraction between
two real parameter states in the operator tube give
\[
\max_{a,j}\|k_a^{(j)}(t)-k_a^{(j)}(T_0)\|_\infty
\le C_{\rm tail}\,n\,
             \|\theta(t)-\theta(T_0)\|_{\rm par}.
\tag{9}
\]
The finite coefficient in this proof-local inequality is independent of
width and time. Explicitly, with \(s,t\) the source bounds on the first
and second derivatives, define the finite downward recurrence
\[
C_L^k=1,\qquad
C_j^k=S\tau_{j+1}+10sC_{j+1}^k
                 +10tSP_{j+1}k_{j+1}\quad(j<L),
\qquad C_{\rm tail}=\max_j C_j^k.
\tag{9a}
\]
To verify it, first bound the preactivation RMS changes
by the finite forward subtraction recurrence and multiply by \(\sqrt n\)
for their coordinate maxima. In each backward layer, split a difference
into a changed gate, a changed matrix, and a changed upper response.
The changed gate costs its coordinate preactivation change times the
bounded second derivative and the reference carrier RMS. The changed
matrix costs its Frobenius norm times the reference response RMS.
Propagation costs at most \(9s\). A final conversion from RMS to
coordinate maximum supplies at most the second \(\sqrt n\).
The resulting carrier RMS bound is
\(\sqrt n C_j^k\|\theta(t)-\theta(T_0)\|_{\rm par}\);
the top carrier change is just the readout change. This proves (9) by
a finite downward induction. All coefficients are fixed polynomial
expressions in the finite real feature/response bounds.

By (6), the right side of (9) is \(O_{\rm task}(n^{-15})\).
The explicit additional eventual deterministic width condition is
\[
\frac{2C_{\rm tail}Y}{\sqrt\lambda}\,n(en)^{-16}
 \le K_{\rm src}S\sqrt{\log(en)}.
\tag{9b}
\]
The original source maximum
therefore implies, simultaneously for all real time,
\[
\max_{a,j,i}|k_{a,i}^{(j)}(t)|
 \le2K_{\rm src}S\sqrt{\log(en)}.
\tag{10}
\]
This use of a task-dependent coefficient is confined to a width qualification;
it does not insert a parameter-dependent coefficient into the error
exponential. The original coefficient \(K_{\rm src}\) in (10) is
unchanged except for the explicit factor two.

## 5. Arbitrary tolerance in the geometric comparison

Take any paired source approximation satisfying (2) on the extended
domain through \(T\). All source/action/pairing estimates in source
§13 are inequalities in the coordinate error, valid for arbitrary
\(\eta\le\min(1,Y,S)\): their sole quadratic remainder is bounded
using \(\eta\le1\) or \(\eta\le S\). No derivative of an
approximation error is taken. Exact initialized additions make initial
parameter and residual discrepancies zero for every tolerance.

In the full-range comparison, substitute \(\eta\) for its proof-local
\(\epsilon\). Equations (2)–(6) there use only \(\eta\le Y\),
not \(\eta=1/n\). Equations (7)–(24) are exact runtime identities
and norm inequalities and contain no horizon dependence. The scalar
reduction (D) uses only the all-time integrals of the residuals and
selected readout velocity. Replacing its carrier maximum by (10) doubles
only its \(\sqrt{\log(en)}\) term. The same original-label
absorptions (F) therefore give
\[
B(t)\le44+64\sqrt{\log(en)},\qquad
 B(t)/(Y/\lambda)\le C\beta^{38L}(1+\sqrt{\log(en)}).
\tag{11}
\]
The query-output estimate (E) and
\(e^B-1\le Be^B\) now give
\[
\sup_{t\le T,\ \|x\|=\sqrt d}|f_{\mathrm{compact}}-f_n|
 \le C\beta^{42L}\frac{Y}{\lambda}
 (1+\lambda^{-1/2})\,
 \eta(1+\sqrt{\log(en)})e^{64\sqrt{\log(en)}}.
\tag{12}
\]
The harmless extra factor \(1+\sqrt{\log(en)}\) is absorbed by
enlarging the numerical coefficient in the exponent in (3).

For later times compare both trajectories to their values at \(T\).
Dense fitting (11) and compact fitting (12) bound the sum of these
motions, including the limits, by
\[
C\beta^{CL}\frac{Y}{\lambda}
 (1+\lambda^{-1/2})e^{-\lambda T/4}.
\tag{13}
\]
The full-range polynomial bounds for the two tail coefficients are
proved in §7 of COMPACT_FULL_LABEL_RANGE. Equations (12)–(13) prove (3).
The runtime never freezes and receives no external trajectory input.

## 6. Scope and provenance

The new argument is deterministic analytic continuation using the proved
late-time parameter tail. It does not claim that the old stochastic
long-horizon net argument was uniform in an arbitrary horizon. It adds
neither a learned coordinate nor a retained coefficient: only the source
cutoff and proof horizon vary during preprocessing. Both are discarded.
Arbitrary coefficient precision and preprocessing work remain outside
the real-coordinate storage contract.

The source event and selection interface remain inherited research
dependencies. In particular this note does not independently establish
their Gaussian insertion theorem or make the stochastic width threshold
effective. It is not promotion to the maintained book or paper.

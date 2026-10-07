# General dense variability and compression below the actual variability

**Interface correspondence (2026-10-05).** [RESULT.md](RESULT.md) gives
the shared accuracy/storage interface and its full recurrence label
allowance. The references below point directly to the current proofs.
The lower theorem and its proof are unchanged.

2026-10-04. Continuation requested by the user: integrate only the general
lower results, retaining the activation, depth, input-geometry and small-label
scope of the merged theorem. These are internal research results. The special
endpoint examples are not dependencies of this result.

## 1. Setting and conclusion

Use the canonical dense model: all \(L\ge2\) hidden layers have width \(n\),
\[
z^1=Ax/\sqrt d,\qquad z^\ell=W^\ell h^{\ell-1},\qquad
h^\ell=\phi_\ell(z^\ell),\qquad f_n=w^\top h^L/n.
\]
Initialize \(A\) with independent \(N(0,1)\) entries, every hidden mixer
with independent \(N(0,1/n)\) entries, and \(w=0\), independently across
blocks. Train mean squared loss with block mobilities
\((n,1,\ldots,1,n)\). A second copy \(\widetilde f_n\) has an independent
initialization and trains on the same data at the same physical times.

Fix \(m\ge2\) inputs of norm \(\sqrt d\), and fixed nonzero real labels.
Write
\[
Y=\|y\|_2/\sqrt m,\quad Q^0_{ab}=x_a^\top x_b/d,\quad
Q^\ell_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
\quad Z\sim N(0,Q^{\ell-1}),\quad
\gamma=\lambda_{\min}(Q^L)>0.
\]
The activations may differ by layer. They are real on the real axis,
holomorphic on a common strip \(|\operatorname{Im}z|<a\), and have
bounded first derivative there. Their values may be unbounded. No
centering, oddness, input orthogonality, input-space rank condition,
sign pattern, clipping, or extra nondegeneracy hypothesis is imposed.

Use the existing full common label allowance in
[RESULT.md](RESULT.md), §6. In particular the already checked simple
sufficient condition is
\[
0<Y\le\frac{\gamma}{m}\beta^{-30L},\qquad
\beta=\max\left\{10,\ 1+\max_\ell|\phi_\ell(0)|,\ 16/a,\
\max_{\ell,j=1,2}\sup_{|\operatorname{Im}z|\le a/2}
|\phi_\ell^{(j)}(z)|\right\}.
\tag{1}
\]
The theorem also retains that larger recurrence-based allowance;
(1) is not a newly imposed restriction.

For every fixed \(0<\delta<1\), at every sufficiently large individual
width, with probability at least \(1-\delta\),
\[
\boxed{
\|f_n-\widetilde f_n\|_*
\ge
c_{\phi,L,\delta}\,
\frac{Y\sqrt\gamma}{\sqrt n\, [\log(en)]^{5/2}},
\qquad
\|f-g\|_*=\sup_{t\in[0,\infty]}
                    \sup_{\|x\|=\sqrt d}|f(t,x)-g(t,x)|.
}
\tag{2}
\]
Here \(c_{\phi,L,\delta}>0\) depends only on the fixed activations,
depth, and confidence. It does not depend on \(m,d,\gamma,Y,n\), or
time. The sufficient width threshold may depend on all fixed problem
parameters and is not currently effective.

The lower bound is witnessed at a training input and at some strictly
positive time
\[
0<t\le c_{\phi,L}\frac{m}{\gamma\sqrt{\log(en)}}.
\tag{3}
\]
Under the simpler allowance (1), \(c_{\phi,L}=1\) is valid. This is
an actual-prediction result for the nonlinear training trajectory, not
just a result about its initial derivative. The witnessing time may
depend on width and initialization. All problem parameters other than
width are fixed before taking the limit; (2) is not a joint
growing-\(m,d\) theorem.

For a fully specified coefficient in (2), define the scalar marginal
moments
\[
q_0=1,\qquad q_\ell=\mathbb E\phi_\ell(\sqrt{q_{\ell-1}}Z)^2,\qquad
\mu_4=\mathbb E\phi_L(\sqrt{q_{L-1}}Z)^4,\quad Z\sim N(0,1).
\]
Let \(\Phi\) be the standard normal distribution function. Under (1),
one can take
\[
c_{\phi,L,\delta}
=\frac{\Phi^{-1}(1/2+\delta/4)}{128}
       \sqrt{\frac{q_L}{\mu_4}}.
\tag{4}
\]
Both moments are positive and finite under \(m\ge2,\gamma>0\).
Under the larger recurrence allowance, multiply (4) by the positive
activation/depth-only time coefficient defined in
[GENERAL_TRAJECTORY_LOWER_BRIDGE.md](GENERAL_TRAJECTORY_LOWER_BRIDGE.md).
That note specifies it arithmetically from the existing source recurrences.

## 2. Why positive feature rank forces variability

The complete moment inequality is proved in
[GENERAL_INNOVATION_LOWER.md](GENERAL_INNOVATION_LOWER.md).
Here is the core argument and its connection to the dynamics.

Let \(H=(\phi_L(Z_a))_{a=1}^m\) be one population feature vector at
initialization, with \(Z\sim N(0,Q^{L-1})\). Its second-moment matrix is
\(Q=Q^L\). Put \(S=y^\top H\). If the vector \(HS\) had zero
variance, it would equal \(Qy\) almost surely. Multiplying by \(y^\top\)
would make \(S^2=y^\top Qy>0\) deterministic; hence \(H=(Qy)/S\)
would lie on one fixed line. That contradicts \(Q\succ0\) for \(m\ge2\).

The quantitative version uses the squared area between \(Qy\) and \(H\).
Since \(HS\) is parallel to \(H\),
\[
\|(Qy)\wedge H\|^2
\le \|HS-Qy\|^2\|H\|^2.
\]
Truncating only the last norm and using its fourth moment gives
\[
\operatorname{tr}\operatorname{Cov}(HS)
\ge
\frac{\{y^\top Q^2[(\operatorname{tr}Q)I-Q]y\}^2}
     {4\,\mathbb E\|H\|^4\,\|Qy\|^2}
\ge
\frac{\gamma^3q_L}{16\mu_4}\|y\|^2.
\tag{5}
\]
The equal input norms imply common marginal moments and
\(\mathbb E\|H\|^4\le m^2\mu_4\). The remaining bound is spectral
algebra; it makes no independence assumption between samples.

At zero readout, every hidden initial velocity is zero, and exactly
\[
\dot f_n(0,x_a)=\frac2m(K_ny)_a,\qquad
(K_n)_{ab}=\frac1n h_0^L(x_a)^\top h_0^L(x_b).
\]
The initialized Gram central limit theorem in
[EARLY_VARIABILITY_AND_STORAGE.md](EARLY_VARIABILITY_AND_STORAGE.md)
includes a positive semidefinite last-layer innovation with covariance
\(\operatorname{Cov}(HH^\top)\). Thus (5) implies that at least one
deterministic training index \(a\) satisfies
\[
\sqrt n[\dot f_n(0,x_a)-\dot{\widetilde f}_n(0,x_a)]
\ \Longrightarrow\ N(0,\sigma_a^2),\qquad
\sigma_a^2\ge\frac{\gamma^3q_LY^2}{2m^2\mu_4}.
\tag{6}
\]
This central limit theorem holds for arbitrary correlated inputs,
including singular intermediate preactivation covariances.

The final step is not a width-independent Taylor remainder. The proved
complex-time source event supplies a bounded holomorphic extension near
the early real trajectory. Restricting the source construction to the
finite training-query set gives radius proportional to
\(m/[\gamma\sqrt{\log(en)}]\), with no input-dimensional covering factor.
For a holomorphic function bounded by \(M\) on the parameter-two
Bernstein ellipse of \([0,r]\), Chebyshev approximation and the
endpoint polynomial derivative inequality give, for every integer \(N\ge1\),
\[
\sup_{0\le t\le r}|g(t)|
\ge\frac{r}{2N^2}|g'(0)|-24M\,2^{-N}.
\]
Apply this to the difference of the two actual predictions, with
\(N\) proportional to \(\log(en)\). The remainder is negligible
relative to (6), and the product of the time radius and onset standard
deviation cancels the explicit \(m\) factors. This proves (2).
The finite-query source extension, confidence calculation, and exact
recurrence-label interface are proved in
[GENERAL_TRAJECTORY_LOWER_BRIDGE.md](GENERAL_TRAJECTORY_LOWER_BRIDGE.md).

## 3. Compression compared with actual dense variability

The new lower bound can be compared with the sharper compression
estimates already proved, rather than merely with the dense upper bound.
Fix any one admissible task with \(m\ge2\).

For the existing compact autonomous model, the all-time conclusion of
[COMPACT_FULL_LABEL_RANGE.md](COMPACT_FULL_LABEL_RANGE.md) gives
\[
\|f_C-f_n\|_*\le n^{-1+o(1)}.
\]
Its full bound retains the actual labels and polynomial task dependence;
this line states only its fixed-task width asymptotics. Consequently
\[
\|f_C-f_n\|_*
=o\!\left(\frac1{\sqrt n[\log(en)]^{5/2}}\right)
\]
on the existing source event. No change in the compact model or its
retained-state count is required.

For Legendre, let \(q_n\) be the explicit order in
[EXPLICIT_LEGENDRE_COMPARISON.md](EXPLICIT_LEGENDRE_COMPARISON.md), (6),
under its full recurrence-based allowance. Under the simpler cap (1),
use the sharper order in
[LEGENDRE_SAMPLE_EXPONENT_REFINEMENT.md](LEGENDRE_SAMPLE_EXPONENT_REFINEMENT.md), (4).
In either case choose
\[
q'_n=\left\lceil q_n[\log(en)]^{3/2}\right\rceil.
\]
The existing comparison holds simultaneously in order. Its explicit
\(q^{-2}\sqrt{\log(eq)}\) dependence gives, eventually,
\[
\|f_{n,q'_n}-f_n\|_*
\le\frac{2Y}{\sqrt n[\log(en)]^3}
=o\!\left(\frac1{\sqrt n[\log(en)]^{5/2}}\right).
\tag{7}
\]
In particular \(q'_n=n^{1/4+o(1)}\), and the exact moving-state count
is \(n(d+1)+1+2(L-1)mnq'_n=n^{5/4+o(1)}\).
The additional fixed initialized mixers still contain \((L-1)n^2\)
entries.

Using (2) at any chosen confidence and a union bound with the source
events proves the general lower-calibrated statements
\[
\boxed{
\frac{\|f_C-f_n\|_*}{\|f_n-\widetilde f_n\|_*}
 \ \xrightarrow{\mathbb P}\ 0,\qquad
\frac{\|f_{n,q'_n}-f_n\|_*}{\|f_n-\widetilde f_n\|_*}
 \ \xrightarrow{\mathbb P}\ 0.
}
\tag{8}
\]
The events need not be independent. Ratios may be assigned any value on
the vanishing-probability event where the denominator is zero. The
comparisons are between the same physical-time, whole-sphere norms.
They do not claim a pointwise ratio at each time, or an endpoint ratio.

Thus the width-asymptotic compression conclusion is supported by a lower
bound for actual dense variability. It does not depend only on the
possibly loose upper bound. Compact storage remains
\(O_{\rm fixed}([\log(en)]^{3d+2})\), counting all retained coordinates;
Legendre moving storage retains its \(5/4\) width exponent. The extra
logarithmic order in (7) is part of the stated Legendre conclusion.

## 4. What is and is not calibrated

- **Width:** the lower rate \(n^{-1/2}\log(en)^{-5/2}\) and the general
  dense upper rate \(n^{-1/2+o(1)}\) identify the same power \(1/2\).
  They do not establish strict matching constant-times-root bounds.
- **Sample count and geometry:** (2) has the explicit amplitude
  \(Y\sqrt\gamma\), without an extra \(m\) or \(d\) factor. This is a
  general floor, not a sharp characterization of sample or conditioning
  dependence. It does not justify the powers of \(m/\gamma\) in the dense
  upper coefficient, and does not preclude a stronger dimensional lower
  bound for some geometries. Sample count also enters the label allowance,
  witness-time scale, and sufficient width threshold.
- **Endpoint:** both runs interpolate every training query. The
  fluctuation used in this proof is therefore transient, even though
  the observation norm includes the endpoint. No general fitted-function
  lower bound is inferred. Initial predictor values themselves are
  exactly zero.
- **One sample and zero labels:** zero labels give zero variability.
  For \(m=1\), a nonzero constant final activation gives positive
  uncentered gap but a deterministic predictor, so a universal positive
  lower bound for that case is false under the original class.
  A nonconstant effective final feature has a positive scalar innovation;
  the exact classification is in
  [GENERAL_ONSET_NONDEGENERACY.md](GENERAL_ONSET_NONDEGENERACY.md).

Fix a failure probability \(0<\delta<1/2\) and a nondegenerate task.
In the large-width regime, a canonical dense family whose independent-copy
discrepancy is at most \(\varepsilon\) with probability at least
\(1-\delta\) must have
\[
n[\log(en)]^5\gtrsim_{\phi,L,\delta}Y^2\gamma/\varepsilon^2.
\tag{9}
\]
Indeed the upper-accuracy and lower-discrepancy events have a nonempty
intersection because their failure probabilities sum to less than one.
Along any such sequence with \(n\to\infty\), the parameter count is
\(\Omega_{\rm fixed}(\varepsilon^{-4}
[\log(1/\varepsilon)]^{-10})\).
Together with the proved sufficient
\(\varepsilon^{-4+o(1)}\) count, this calibrates the dense width exponent.
The compression counts remain sufficient
\(\varepsilon^{-5/2+o(1)}\) moving Legendre coordinates and
\(O_{\rm fixed}(\log^{3d+2}(1/\varepsilon))\) retained compact coordinates.
Equation (9) is not a dimension or bit-complexity lower bound against
arbitrary alternative representations.

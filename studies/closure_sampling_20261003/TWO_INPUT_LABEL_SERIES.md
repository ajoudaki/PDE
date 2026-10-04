# Two-input label series: polynomial time-mode count and the remaining tube estimate

2026-10-03. Scoped proof route for the same study. This candidate was developed
before exchanging mathematical findings with the other two-input routes.
Authorized scientific inputs were the setting in `paper/main.tex`, the complete
`paper/proof_alltime.tex`, and the four assigned study notes
`CANONICAL_NEURON_COMPRESSION.md`, `COMPLEX_ACTIVITY_ROUTE.md`,
`CANONICAL_SCALAR_AUTONOMY_ROUTE.md`, and
`TWO_INPUT_EXTENSION_ASSESSMENT.md`. The canonical-notation skill and its
neural-network reference, rigorous-proof skill, and conjecture contract and
adversarial-audit instructions were applied. No experiments, other-study
research, trajectory snapshots, or Git operations were used. First-layer
initialization is \(N(0,1)\), as in the manuscript; only the middle matrix has
entry variance \(1/n\).

**Result.** The proposed polynomial source-count mechanism is valid. Through
label order \(p\), every response is a combination of at most \(O(p^3)\)
exponential-polynomial time functions. Their coefficient vectors are obtained
from initialization by a finite algebraic recurrence. Noncommutation of the
two activity fields does not produce an exponential count here. A uniform
complex label tube of width \(c/\sqrt{\log n}\), if proved for the actual dense
sources, would therefore yield initialization-only source spaces of dimension

\[
 C\exp(C\sqrt{\log(en/\eta)})[\log(en/\eta)]^{9/2}
 =n^{o(1)}
\]

for the entire physical-time trajectory and input circle. This note proves
uniform-time analyticity on the weaker disk \(|\lambda|<cn^{-1/4}\) and proves
the conditional source-space construction. It does **not** prove the needed
fixed-label tube or the final autonomous reduced-flow stability theorem.

## 1. Canonical equations and the label parameter

Take training inputs \(x_1=\sqrt2e_1,x_2=\sqrt2e_2\). The reference is

\[
 h(x)=\tanh(Ax/\sqrt2),\qquad g(x)=\tanh(Wh(x)),
 \qquad f(x)=w^\top g(x)/n,
\]

where \(A\in\mathbb R^{n\times2}\), \(W\in\mathbb R^{n\times n}\),
and \(w\in\mathbb R^n\). Independently initialize \(A_{0,ia}\sim N(0,1)\),
\(W_{0,ji}\sim N(0,1/n)\), and \(w_0=0\). Write the nonzero label vector as
\(y=\lambda_*v\), with \(\lambda_*=\|y\|_2>0\) and
\(v=y/\lambda_*\in\mathbb R^2\). Thus \(\|v\|_2=1\), with either sign allowed
in each component. The zero-label case is stationary. In the analytic family,
replace \(y\) by \(\lambda v\), allowing complex \(\lambda\).

For the training inputs define

\[
 a_a=Ae_a,\quad h_a=\tanh a_a,\quad z_a=Wh_a,\quad
 g_a=\tanh z_a,\quad \delta_a=w\odot\operatorname{sech}^2z_a,
 \quad k_a=W^\top\delta_a,\quad c_a=\lambda v_a-f_a.
\]

The loss is \(\tfrac12\sum_a(f_a-\lambda v_a)^2\). With mobilities
\((n,1,n)\), physical time satisfies

\[
 \dot a_a=c_a\operatorname{sech}^2a_a\odot k_a,
 \qquad \dot W=\frac1n\sum_a c_a\delta_a h_a^\top,
 \qquad \dot w=\sum_a c_a g_a.                         \tag{1}
\]

Use the assigned coordinate change

\[
 F(s)=s/2+\sinh(2s)/4,\quad u_a=F(a_a),\quad
 \sigma=\tanh\circ F^{-1},\quad H=\sqrt nW,
 \quad \Theta=(u_1,u_2,H,w).
\]

The inverse is the real branch continued to the fixed strip established in
`COMPLEX_ACTIVITY_ROUTE.md`. Let \(V_a(\Theta)\) have \(u_a\)-block \(k_a\),
other first-layer block zero, \(H\)-block \(\delta_a h_a^\top/\sqrt n\), and
\(w\)-block \(g_a\). Equation (1) becomes

\[
 \dot\Theta=\sum_a c_aV_a(\Theta),\qquad
 \dot c=-K(\Theta)c,\qquad c(0)=\lambda v,               \tag{2}
\]

where the exact tangent matrix is

\[
 K_{ab}=
 \frac{g_a^\top g_b}{n}
 +\frac{\delta_a^\top\delta_b}{n}\frac{h_a^\top h_b}{n}
 +\mathbf1_{a=b}\frac{q_a^\top q_a}{n},\qquad
 q_a=\operatorname{sech}^2a_a\odot k_a.                  \tag{3}
\]

For example, \(Df_a[V_b]=K_{ab}\); orthogonality of the two inputs produces
the indicator in the first-layer term. In complex equations all transposes
are algebraic, without conjugation. Complex Euclidean norms used for bounds
do use conjugation.

Put \(G_0=(g_{1,0},g_{2,0})\in\mathbb R^{n\times2}\). At initialization,

\[
 K_0=G_0^\top G_0/n.
\]

Work on \(\|W_0\|_{\rm op}\le K_*\) and \(K_0\succeq\gamma I_2\), with
fixed \(K_*,\gamma>0\). This event has probability tending to one by the
initialized Gram calculation in the assigned all-time proof. The two
orthogonal Gaussian first-layer preactivations have independent, nonconstant
tanh features, so their limiting first Gram is a positive multiple of \(I_2\);
the second-layer limiting Gram is also a positive multiple of \(I_2\).
Let \(\kappa_1,\kappa_2\ge\gamma\) be the two real eigenvalues of \(K_0\).
Coincident eigenvalues are allowed.

## 2. Exact finite label jets have polynomially many time modes

For finite physical horizons, the vector field is holomorphic near the real
initialized state. Taylor coefficients at \(\lambda=0\) are therefore
defined by

\[
 \Theta(t,\lambda)=\Theta_0+\sum_{k\ge1}\lambda^k\Theta_k(t),
 \qquad c(t,\lambda)=\sum_{k\ge1}\lambda^k c_k(t).       \tag{4}
\]

This equation initially denotes a local expansion, not convergence at the
fixed target \(\lambda_*\). Coefficients are divided by \(k!\).

For \(k\ge1\), let \(\mathcal E_k\) be the scalar span of

\[
 1,\qquad t^d e^{-(a\kappa_1+b\kappa_2)t},\quad
 a,b\in\mathbb N_0,\quad1\le a+b\le k,\quad0\le d\le k-1.
                                                               \tag{5}
\]

Let \(\mathcal E_k^+\) omit the constant. All these functions are bounded
on \(0\le t\le\infty\), with each nonconstant function tending to zero.
The number displayed, including possible duplicates, is

\[
 D_k=1+k\left[\frac{(k+1)(k+2)}2-1\right]=O(k^3).       \tag{6}
\]

**Proposition.** Every coordinate of \(\Theta_k\) belongs to
\(\mathcal E_k\), and every coordinate of \(c_k\) belongs to
\(\mathcal E_k^+\). If \(R(\Theta)\) is any fixed finite-dimensional
holomorphic source near \(\Theta_0\), then the order-\(k\) coefficient of
\(R(\Theta(t,\lambda))\) belongs coordinatewise to \(\mathcal E_k\).
Every coefficient vector is obtained from initialization and \(v\) by finite
algebraic operations, derivatives of the specified activation, diagonalization
of the \(2\times2\) matrix \(K_0\), and integration of the displayed scalar
exponential-polynomial functions.

**Proof.** Expand \(V_a(\Theta)=\sum_{j\ge0}\lambda^j V_{a,j}(t)\) and
\(K(\Theta)=K_0+\sum_{j\ge1}\lambda^j K_j(t)\). Equating powers in (2)
gives the triangular recurrence

\[
 c_1(t)=e^{-K_0t}v,
\]

\[
 \dot c_k=-K_0c_k-\sum_{j=1}^{k-1}K_jc_{k-j},\quad
 c_k(0)=0\quad(k\ge2),                                  \tag{7}
\]

\[
 \dot\Theta_k=\sum_{a=1}^2\sum_{j=0}^{k-1}
             (c_{k-j})_a V_{a,j},\qquad \Theta_k(0)=0.    \tag{8}
\]

For \(k=1\), (7) has only the two decaying rates. Integration in (8)
adds a constant and those same rates. In particular

\[
 w_1(t)=G_0K_0^{-1}(I-e^{-K_0t})v,
 \qquad (u_1)_1=(u_2)_1=H_1=0.                           \tag{9}
\]

For the induction, a coefficient of order \(j\ge1\) in any analytic state
function is a finite sum of products of factors \(\Theta_{i_1},\ldots,
\Theta_{i_r}\), where \(i_s\ge1\) and \(\sum_s i_s=j\), contracted with
derivative tensors evaluated at \(\Theta_0\). The total exponential index
\(a+b\) of a product is at most \(j\), its polynomial degree is at most
\(\sum_s(i_s-1)=j-r\le j-1\), and its zero-rate part is constant. Hence
\(V_{a,j},K_j\in\mathcal E_j\) coordinatewise.

Each forcing product \(K_jc_{k-j}\) in (7) has strictly positive rate,
index at most \(k\), and polynomial degree at most \(k-2\). Diagonalize
\(K_0\) by a real orthogonal matrix and apply variation of constants.
Convolution of \(t^de^{-\mu t}\) with \(e^{-\kappa_i t}\) has the original
rate and rate \(\kappa_i\) with degree at most \(d\) if \(\mu\ne\kappa_i\);
if \(\mu=\kappa_i\), it is \(t^{d+1}e^{-\kappa_i t}/(d+1)\).
Thus \(c_k\in\mathcal E_k^+\). This also covers accidental integer-rate
resonances and repeated eigenvalues.

The terms in (8) all have strictly positive rate. The \(j=0\) terms have
degree at most \(k-1\), and the others degree at most \(k-2\). Integration
from zero adds only a constant, preserves the positive rate, and does not
raise polynomial degree. This gives \(\Theta_k\in\mathcal E_k\).
The analytic-source assertion follows from the same product argument.
The recurrence uses no positive-time network evaluation. It closes using
only its finite coefficient arrays, which proves the provenance assertion.
\(\square\)

The absence of zero-rate polynomials \(t,t^2,\ldots\) is significant. Every
state velocity contains a residual factor, and every residual coefficient
has a positive rate. Consequently each fixed-order label jet is bounded
uniformly in physical time and has an endpoint. A generic analytic ODE
expansion about a center subspace would not provide this conclusion.

The exact parity \(\Theta_{\rm hidden}(t,-\lambda)=
\Theta_{\rm hidden}(t,\lambda)\), \(w(t,-\lambda)=-w(t,\lambda)\), and
\(c(t,-\lambda)=-c(t,\lambda)\) removes further coefficients. It follows
by substitution in (1), since \(\delta_a,k_a\) reverse sign with \(w\).
The count (6) does not need this improvement.

Noncommuting products of the two fields can contribute different vector
coefficients. Their time factors nevertheless collapse onto (5). This is
not an assumption that \(V_1,V_2\) commute or that residual direction stays
fixed. It is a consequence of expansion about the stationary zero-label
path with a two-dimensional initial damping matrix.

## 3. A uniform-time complex disk that can be proved directly

There is a deterministic \(c_0>0\), depending only on \(K_*,\gamma\), such
that the complete finite-width training solution is holomorphic in

\[
 |\lambda|<c_0 n^{-1/4}                                  \tag{10}
\]

for every \(0\le t\le\infty\). Its residual decays exponentially, uniformly
on that disk. This supplies a genuine uniform-time local germ, but its radius
shrinks too fast to resolve the fixed-label target by the intended argument.

Here are the estimates proving (10). Stop before either first-layer inverse
strip or any second-layer tanh strip loses a fixed pole margin, and before
the operator norm leaves \(K_*+1\). Write

\[
 B(t)=\int_0^t\|c(s)\|_2\,ds.
\]

On this stopped region, bounded gates and (1)--(2) give

\[
 \|w\|_\infty\le CB,
 \quad \|W-W_0\|_{\rm op}\le CB^2,
 \quad \sum_a\|u_a-u_{a,0}\|_2/\sqrt n\le CB^2,
 \quad \sum_a\|g_a-g_{a,0}\|_2/\sqrt n\le CB^2.         \tag{11}
\]

For example, \(\|\delta_a\|_2/\sqrt n\le CB\),
\(\|k_a\|_2/\sqrt n\le CB\), and integrating the product of these bounds
with \(\|c\|_2\) gives the quadratic displacements. The inverse strip gives
a fixed Lipschitz bound for \(a_a=F^{-1}(u_a)\) and \(h_a=\sigma(u_a)\).
Equation (3), using these normalized norms, yields

\[
 \|K(\Theta)-K_0\|_{\rm op}\le CB^2.                    \tag{12}
\]

No positive-semidefinite claim is made for complex \(K\). Instead (12)
implies

\[
 \operatorname{Re}(z^*Kz)\ge(\gamma-CB^2)\|z\|_2^2
 \quad\text{for every }z\in\mathbb C^2.
\]

Bootstrap \(B\le C_*|\lambda|\), choosing \(C_*>2/\gamma\) fixed and
\(|\lambda|\) sufficiently small. Then

\[
 \|c(t)\|_2\le|\lambda|e^{-\gamma t/2},\qquad
 B(t)\le2|\lambda|/\gamma,                                \tag{13}
\]

which strictly improves the activity cap. The operator cap also improves.
To close the coordinate pole caps directly, use (11) and the forward pass:

\[
 \max_a\left(\|u_a-u_{a,0}\|_\infty+
                   \|z_a-z_{a,0}\|_\infty\right)
 \le C\sqrt n\,|\lambda|^2.                              \tag{14}
\]

For (10), choose \(c_0\) so the right side is strictly smaller than the
fixed pole margin. This excludes every stop. Finite-dimensional continuation
gives existence on all finite horizons. Bounds (11)--(13) give an exponentially
small tail for all parameters in their respective normalized norms; at fixed
\(n\), the same is true coordinatewise. The convergence is uniform on every
closed smaller disk in (10). Finite-time holomorphic dependence followed by
this uniform convergence proves endpoint holomorphy. Cauchy's formula, with
uniform bounds on each such disk, also proves that all the finite-order jets
in Section 2 are the true uniform-time Taylor coefficients.

For real query angles, \(\tanh(A(\cos\theta,\sin\theta)^\top)\) has the
same \(C\sqrt n|\lambda|^2\) first-layer coordinate perturbation. The
second-layer query perturbation has the same bound by the operator estimate.
Thus (10) also gives simultaneous holomorphy of the query sources for all
real angles. A logarithmic joint complex angular strip is a stronger input
in the next section.

## 4. Conditional continuation gives small source spaces

Here is the precise sufficient regularity claim still needed. Put
\(\ell=\log(en/\eta)\). On an initialization event of probability at least
\(1-\eta\), assume all source coordinates

\[
 h_\theta(t,\lambda),\quad g_\theta(t,\lambda),\quad
 W_0h_\theta(t,\lambda),\quad
 \delta_a(t,\lambda),\quad W_0^\top\delta_a(t,\lambda)    \tag{15}
\]

are jointly holomorphic and bounded by \(M_n\le C\sqrt\ell\), uniformly
for \(t\in[0,\infty]\), on

\[
 |\operatorname{Re}\lambda|<\lambda_*+2r_n,
 \quad |\operatorname{Im}\lambda|<r_n,
 \quad |\operatorname{Im}\theta|<r_{\theta,n},\qquad
 r_n,r_{\theta,n}\ge c/\sqrt\ell.                         \tag{16}
\]

The last two sources have only the training sample index and do not require
an angular argument. The constants must be independent of width and
confidence, and \(\lambda_*\) must be a fixed sufficiently small label norm.
A polynomial-in-\(n\) bound on \(M_n\) would also suffice after altering
constants and logarithmic factors.

Apply the explicitly proved disk-to-rectangle map from
`CANONICAL_SCALAR_AUTONOMY_ROUTE.md` in the variable \(\lambda\), with \(t\)
held as an arbitrary external parameter. It gives scalar coefficients
\(\psi_{k,p}(\lambda_*)\), independent of time, neurons, source, and query,
such that

\[
 R(t,\lambda_*,\theta)\simeq
 \sum_{k=0}^p\psi_{k,p}(\lambda_*)
                  \partial_\lambda^kR(t,0,\theta),       \tag{17}
\]

with coordinate error at most \(\epsilon\) uniformly in time and throughout
a smaller angular strip. For \(\epsilon=n^{-B}\), any fixed \(B>0\), it
suffices to choose

\[
 p\le C e^{C\lambda_*\sqrt\ell}\ell.                     \tag{18}
\]

This is analytic continuation in the label, not Taylor truncation outside
its initial convergence disk. The bound uses the assumed whole rectangle;
the small disk (10) cannot replace that hypothesis.

By Section 2, the right side of (17) is a vector-valued combination of the
common \(D_p=O(p^3)\) time functions (5). For a fixed target label, combine
the vectors from the different orders \(k\le p\) which multiply the same
time function. This avoids an unnecessary additional factor \(p\). All
combined vectors are computed from initialized formal coefficients.

Periodic trigonometric interpolation in \(\theta\), at \(2L+1\) equally
spaced real angles, has error at most \(\epsilon\) when

\[
 L\le C\ell^{3/2}                                       \tag{19}
\]

is sufficiently large. This follows by shifting the Fourier coefficient
integral inside the angular strip, summing the exponential Fourier tail,
and bounding interpolation aliasing by that same absolute tail. Perform the
label continuation first: its approximation is still bounded by \(M_n+\epsilon\)
on the smaller angular strip. The interpolation coefficients are finite
linear combinations of its values at the chosen angles. The two operations
are linear and commute, so all vectors still come from initialized label
jets at a finite list of angles.

For the lower-layer source space retain the coefficient vectors of the
approximations to \(h_\theta,W_0^\top\delta_1,W_0^\top\delta_2\), together
with both initial first-layer columns and both initial training features.
For the upper-layer source space retain those for
\(g_\theta,W_0h_\theta,\delta_1,\delta_2\), together with both initial
training features \(g_{a,0}\). Include each paired matrix image as the actual
image of its corresponding source coefficient. Because (17) and angular
interpolation use identical scalar coefficients on a source and its image,
both approximations and their image approximations have coordinate error
\(C\epsilon\). Their dimensions satisfy

\[
 r_1,r_2\le C(p+1)^3(L+1)+C.                              \tag{20}
\]

Positive cubature matching all products in these spaces requires at most
\(1+r_i(r_i+1)/2\) selected original neurons in each layer. The two-sided
projected initialized mixer in the assigned neuron-compression note then
preserves both matrix orientations on the paired source spaces. A fully
evolved small weighted dense network would have total stored and moving
array count at most

\[
 C(p+1)^{12}(L+1)^4
 \le C e^{C\sqrt\ell}\ell^{18}=n^{o(1)}.                  \tag{21}
\]

This is a conditional count and consistency construction, not a completed
error theorem for that reduced dynamics. Two-input all-time stability with
the reduced model's own residuals remains a separate proof obligation.
No time-mode clock or externally prescribed residual needs to enter the
small network's evolution; the time functions are used only to prove that
its initialization-derived cubature spaces approximate the reference sources.
The finite coefficient recurrence can be expensive and ill-conditioned.
No practical setup-time or finite-precision claim is made.

## 5. Why complex damping alone does not prove the missing tube

Equations (11)--(13) show that complex residual damping is available whenever
the gates have a fixed pole margin. This avoids the false assertion that the
complex tangent matrix is positive semidefinite. It also rules out a
standalone obstruction from arbitrarily long physical time: on any
pole-safe complex branch, the residual is integrable uniformly in time.

The gap is the coordinate pole margin over a label rectangle reaching the
fixed real value \(\lambda_*\). The direct normalized estimates only give
(14), which does not close there. To use the width \(r_n\asymp\ell^{-1/2}\)
around each real label, one needs, for example,

\[
 \sup_{t,\lambda}\left(
 \|\partial_\lambda u_a(t,\lambda)\|_\infty+
 \|\partial_\lambda z_a(t,\lambda)\|_\infty
 \right)\le C\sqrt\ell,                                  \tag{22}
\]

on appropriate stopped domains, with analogous passive-query control.
Vertical integration in \(\lambda\) would then bound imaginary coordinates
by \(C\sqrt\ell\,r_n\). The two-input fixed-control activity result does
not establish (22), since varying labels changes the residual controls.

The actual sensitivity system exposes the issue. Define
\(\Xi=\partial_\lambda\Theta\) and \(d=\partial_\lambda c\). Then

\[
 \dot\Xi=\sum_a c_aDV_a[\Xi]+\sum_a d_aV_a,
 \qquad
 \dot d=-Kd-DK[\Xi]c,
 \qquad \Xi(0)=0,\quad d(0)=v.                            \tag{23}
\]

Although \(DV_a\) has a width-independent Euclidean bound in the transformed
coordinates, the same assertion does not follow for \(DK\). Already the
first-layer contribution \(K_{aa}^{(1)}=q_a^\top q_a/n\) has variation

\[
 \mathrm dK_{aa}^{(1)}
 =\frac2n\sum_i q_{a,i}
   \left[\operatorname{sech}^2a_{a,i}\,\mathrm dk_{a,i}
   +\tanh''(a_{a,i})k_{a,i}\,\mathrm da_{a,i}\right].     \tag{24}
\]

The second term includes \(k_{a,i}^2\,\mathrm da_{a,i}\). A normalized
Euclidean perturbation cannot bound this term from the carrier RMS alone.
For example, Cauchy--Schwarz bounds its size by a constant times
\((n^{-1}\sum_i|k_{a,i}|^4)^{1/2}\,\|\mathrm da_a\|_2/\sqrt n\), which
requires a fourth-moment estimate; a carrier-maximum bound is another, less
sharp option. Higher label derivatives introduce further products. A
sub-Gaussian *real-time marginal* statement is not automatically a uniform
complex-domain sensitivity estimate and cannot be substituted here.

A singleton cavity driven by its own residuals would preserve independence
of the omitted Gaussian row or column, but its controls differ from those
of the original network. Bounding that discrepancy in integrable physical
time while retaining coordinate sensitivity is exactly the additional work.
Using original-network controls would remove the discrepancy only by losing
the independence needed for conditional Gaussian bounds.

Thus (22) is an open sufficient estimate, not a proved bound or a no-go
claim. Even its failure would not disprove the broader compression target.
The established result of this route is the finite-jet mode collapse plus
the conditional reduction (16)--(21). It removes exponential word count as
an obstruction; it leaves complex tube control and autonomous all-time
comparison explicit.

## 6. Claim status and hostile checks

| Claim | Status and limitation |
|---|---|
| Exact two-input residual equations and initial damping matrix | Proved for the canonical finite network. |
| At most \(O(p^3)\) scalar time modes through label order \(p\) | Proved, with repeated rates and resonances included. |
| Initial coefficient provenance | Proved by the finite triangular recurrence; no trained snapshots are used. |
| Bounded fixed-order coefficients and fitted endpoints | Proved; residual factors exclude zero-rate secular terms. |
| Uniform-time complex disk \(cn^{-1/4}\) | Proved on the initial operator/Gram event. Too small for the target fixed labels. |
| Logarithmic complex label-and-query tube | Open. Residual damping supplies only the pole-safe part. |
| Source dimensions \(n^{o(1)}\) and total array count \(n^{o(1)}\) | Conditional on the specified tube; all fixed arrays are counted. |
| \(C/\sqrt n\) uniform-time autonomous prediction error | Not established here; also needs the two-input stability bridge. |

The count uses finitely many ordinary real coefficients and a specified
initialization-only recurrence, not an arbitrary-precision encoding of the
trajectory. Exact arithmetic is nonetheless allowed, as in the assigned
one-input construction. Repeated or almost repeated rates can worsen
conditioning without increasing the displayed dimension. The result applies
to a single chosen label direction \(v\); no common compression over all
label directions has been claimed. The small label is fixed as \(n\to\infty\),
and the radius (10) has not been confused with a uniform neighborhood of that
fixed label. Finally, proving this source-space count does not grant either
the unproved tube or the nonlinear stability of the reduced system.

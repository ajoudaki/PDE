# Canonical one-input activity and analytic source approximation

2026-10-03. Scoped independent continuation for two equal-width tanh hidden
layers, ordinary independent Gaussian initialization, zero readout, and one
fixed sphere training input with a sufficiently small fixed nonzero label.
This note owns no manuscript or maintained-code change.

**Supersession update, 2026-10-03.** The complex-regularity obligation
recorded below was subsequently proved in
[COMPLEX_ACTIVITY_ROUTE.md](COMPLEX_ACTIVITY_ROUTE.md), including circle
queries, and reconstructed in
[COMPLEX_ACTIVITY_CHECK.md](COMPLEX_ACTIVITY_CHECK.md).
[CANONICAL_NEURON_COMPRESSION.md](CANONICAL_NEURON_COMPRESSION.md) now
combines that result with this note's analytic approximation and clock
comparison to prove the requested all-time \(o(n)\) moving-state
compression in the stated canonical one-input setting. Its complete
internal reconstruction is
[CANONICAL_NEURON_COMPRESSION_CHECK.md](CANONICAL_NEURON_COMPRESSION_CHECK.md).
The original status and open-obligation discussion below are retained as
the historical route record.

**Status.** The exact scalar activity reduction and the analytic source
approximation lemma below are proved. They identify a potentially sufficient
route to an autonomous sublinear moving-state sampler. The required complex
activity estimate for the actual Gaussian dense network is **not proved**.
Consequently this note does not establish the requested all-time compression,
and does not replace it by an initial-derivative theorem or an impossibility
claim. A real carrier maximum alone does not close the missing estimate.

Inputs were the assigned current manuscript setting, its real fitting and
population-response arguments, the current study README and prior
`NEURON_GLOBAL_POSITIVE.md`, and the user-authorized prior study's finite
mixed-moment calculation/check and complete local insertion argument in
`Q_ORDER_POSITIVE_ROUTE.md`. Canonical notation, rigorous proof, and
conjecture-investigation instructions were applied. No experiment, Git write,
other new route-file read, or trained-path evaluation was performed.

## 1. The actual one-input dense trajectory

Let the training input be \(x_*\in\mathbb R^d\), with
\(v=x_*/\sqrt d\) and \(\|v\|_2=1\). Write the first matrix as
\(A\in\mathbb R^{n\times d}\), the hidden matrix as
\(W\in\mathbb R^{n\times n}\), and the stored readout as
\(w\in\mathbb R^n\). The training forward pass is

\[
 a=Av,\quad h=\tanh a,\quad z=Wh,\quad
 u=\tanh z,\quad f=n^{-1}w^\top u.
\]

The loss is \((f-y)^2\). Initialization is independent
\(A_{0,ij}\sim N(0,1)\), \(W_{0,ij}\sim N(0,1/n)\), and
\(w_0=0\). Take \(y>0\); the negative-label case is obtained by changing
the readout sign.

For as long as \(f<y\), define activity by

\[
 \frac{ds}{dt}=2(y-f),\qquad s(0)=0.
\tag{1}
\]

Primes below mean derivatives in \(s\), not physical time. The canonical
gradient equations become exactly

\[
 \begin{aligned}
  A'&=[\operatorname{sech}^2a\odot k]v^\top,
  &k&=W^\top\delta,\\
  W'&=\delta h^\top/n,
  &\delta&=w\odot\operatorname{sech}^2z,\\
  w'&=u.
 \end{aligned}
\tag{2}
\]

These equations do not involve \(y\). The label chooses the stopping point
on this common activity curve. If \(F(s)\) denotes its training prediction,
the chain rule gives

\[
 F'(s)=\frac{\|u\|_2^2}{n}
       +\frac{\|\delta\|_2^2}{n}\frac{\|h\|_2^2}{n}
       +\frac{\|\operatorname{sech}^2a\odot k\|_2^2}{n}.
\tag{3}
\]

For example, the middle summand follows from

\[
 n^{-1}\delta^\top W'h
 =n^{-2}\|\delta\|_2^2\|h\|_2^2.
\]

Thus the surviving readout feature gap makes \(F'\ge\kappa>0\) on a
fixed short activity interval. The small-label fitting argument places the
whole physical trajectory, including its fitted limit, in such an interval
\(0\le s\le S\), where \(S=O(y)\). This is the actual nonlinear path;
\(F'\) in (3) is state dependent.

There is an exact useful symmetry. Uniqueness of (2), and direct substitution
of \((A(-s),W(-s),-w(-s))\), give

\[
 A(-s)=A(s),\qquad W(-s)=W(s),\qquad w(-s)=-w(s)
\tag{4}
\]

on their common real interval of existence. Hence first features, second
features, and hidden parameters are even in activity; readout and prediction
are odd. This allows a source approximation centered at the initialized
state to use a symmetric complex neighborhood.

The path retains both hidden learning mechanisms. At initialization set
\(h_0=\tanh(A_0v)\), \(z_0=W_0h_0\), and
\(b_0=\tanh z_0\odot\operatorname{sech}^2z_0\). Then

\[
 W''(0)=b_0h_0^\top/n,
 \qquad
 a''(0)=\operatorname{sech}^2(A_0v)\odot W_0^\top b_0.
\tag{5}
\]

Both are nonzero almost surely: \(W_0\) is invertible almost surely,
\(h_0\ne0\), and \(b_0\ne0\). Equation (5) alone is an initial activity
certificate, not an all-time feature-learning lower bound. The proposed
comparison would retain the actual complete path (2), not replace it by its
acceleration or by the first term of (3).

There is also an exact squared-activity representation. Where the finite
trajectory is analytic, (4) allows \(\sigma=s^2\) and
\(w(s)=s\,b(\sigma)\), with \(A\) and \(W\) viewed as functions of
\(\sigma\). Substitution into (2) gives

\[
 \begin{aligned}
 \partial_\sigma A
   &=\tfrac12[\operatorname{sech}^2a\odot
                  W^\top(b\odot\operatorname{sech}^2z)]v^\top,\\
 \partial_\sigma W
   &=\tfrac1{2n}(b\odot\operatorname{sech}^2z)h^\top,\\
 2\sigma\partial_\sigma b+b&=\tanh z,\qquad b(0)=\tanh z_0.
 \end{aligned}
\]

The apparent singularity in the last equation has the regular integral
form

\[
 b(\sigma)=\int_0^1\tanh z(\sigma u^2)\,du,
\]

obtained by integrating \(w'=\tanh z\) and substituting \(s'=su\).
Thus the hidden curve has geometric interval \(0\le\sigma\le S^2\).
A logarithmic complex rectangle proved for these fields would replace
\(S\) by \(S^2\) in the exponent below. This is a conditional advantage,
not a proved wider complex domain. In particular, the integral equation
must be controlled through \(\sigma=0\); dividing by \(\sigma\) there
would not define a valid autonomous update.

## 2. An explicit whole-activity approximation from initialization

The next lemma is purely deterministic. Its premise is deliberately stated
as the unresolved complex-domain requirement, rather than silently inferred
from real smoothness.

**Lemma.** Fix \(S,r,M>0\). Let \(g\) be a scalar holomorphic function on
the rectangle

\[
 \mathcal R_{S,r}
 =\{z\in\mathbb C: |\operatorname{Re}z|<S+2r,
                         |\operatorname{Im}z|<r\},
 \qquad |g(z)|\le M.
\tag{6}
\]

There are scalar functions \(\psi_{j,p}(s)\), depending only on \(S,r,p\),
such that the approximation

\[
 g_p(s)=\sum_{j=0}^p\psi_{j,p}(s)g^{(j)}(0)
\tag{7}
\]

satisfies, for \(0\le s\le S\),

\[
 |g(s)-g_p(s)|\le\frac{M q^{p+1}}{1-q},\qquad
 1-q\ge (1-e^{-\pi})e^{-\pi S/(2r)}.
\tag{8}
\]

Thus, with an absolute constant \(C\), it suffices for error at most
\(\varepsilon\in(0,M]\) to take

\[
 p+1\ge C e^{\pi S/(2r)}
              [\log(M/\varepsilon)+S/r+1].
\tag{9}
\]

The same statement holds coordinatewise for any finite family of functions
with the common bound \(M\), using the same functions \(\psi_{j,p}\).
Consequently the approximating vector remains in the span of its initial
derivative vectors through order \(p\).

**Proof.** Define

\[
 a=\tanh\frac{\pi(S+2r)}{4r},\qquad
 z(\zeta)=\frac{2r}{\pi}
              \log\frac{1+a\zeta}{1-a\zeta},
 \qquad |\zeta|<1,
\tag{10}
\]

with the holomorphic logarithm equal to zero at the origin. The fraction
has positive real part, so its argument lies strictly between
\(-\pi/2\) and \(\pi/2\). This gives
\(|\operatorname{Im}z(\zeta)|<r\). Also

\[
 \left|\log\left|\frac{1+a\zeta}{1-a\zeta}\right|\right|
 <\log\frac{1+a}{1-a}
 =\frac{\pi(S+2r)}{2r},
\]

which gives the real-coordinate condition in (6). Therefore
\(g(z(\zeta))=\sum_{k\ge0}c_k\zeta^k\) is holomorphic and bounded by
\(M\) in the unit disk. Cauchy's integral formula on circles of radius
\(R<1\), followed by \(R\uparrow1\), yields \(|c_k|\le M\).

The Taylor coefficient \(c_k\) is a scalar linear combination of
\(g^{(j)}(0)\), \(0\le j\le k\), since \(z(0)=0\). For real
\(0\le s\le S\), its inverse coordinate is

\[
 \zeta(s)=\frac{\tanh(\pi s/(4r))}{a},\qquad
 q=\zeta(S)<1.
\]

Truncating the disk Taylor series at \(p\) gives (7) and the geometric
tail in (8). Write \(u=\pi S/(4r)\) and \(b=\pi/2\). Direct subtraction
of the two hyperbolic tangents gives

\[
 1-q=\frac{\sinh b}{\cosh u\,\sinh(u+b)}
 \ge 2e^{-b}\sinh b\,e^{-2u}
 =(1-e^{-\pi})e^{-\pi S/(2r)}.
\]

Finally \(q^{p+1}\le e^{-(p+1)(1-q)}\), and substitution proves (9).

This construction uses initial derivatives and fixed scalar functions only.
It does not take snapshots of a trained path. Unlike ordinary Taylor
truncation in \(s\), it proves a remainder over the whole activity interval
under the stated domain bound.

## 3. Why a logarithmic complex width would already suffice

Suppose, provisionally, that the actual finite dense source coordinates
needed by the two-sided sampler satisfy (6), with probability at least
\(1-\delta\), for

\[
 r_n=\frac{c_\delta}{\log(e+n)},\qquad M_n\le n^{B_\delta},
\tag{11}
\]

where \(c_\delta>0\) and \(B_\delta<\infty\) are independent of width.
Taking the source error \(\varepsilon=n^{-B}\), with \(B\) any required
fixed accuracy exponent, gives

\[
 p=n^{\pi S/(2c_\delta)+o(1)}.
\tag{12}
\]

The existing exact two-sided derivative cubature uses \(O(p^2)\) retained
neurons for a fixed finite probe list. A weighted dense reduced model would
then have \(O(p^4)\) moving parameters. At that resource level, (12) is
strictly sublinear whenever

\[
 S<\frac{c_\delta}{2\pi}.
\tag{13}
\]

This arithmetic is conditional. It also requires a reference-source
consistency and trajectory-stability argument, and a finite-dimensional
spatial approximation for the complete query law. It is not a theorem
deduced solely from derivative cubature. A better strip
\(r_n\asymp1/\sqrt{\log n}\) would give \(p=n^{o(1)}\), but that
stronger scale is unnecessary for a sufficiently small fixed label.

If the confidence parameter changes the admissible label threshold, the
resulting quantifiers need care. To prove one fixed label works for every
fixed confidence, a common positive strip constant must be established;
one cannot choose the label after the requested confidence while claiming
the stronger statement.

## 4. Exact transfer from activity back to all physical time

The scalar clock removes a separate infinite-time obstacle. Let \(F\) and
\(F_C\) be the training predictions of the reference and an autonomous
reduced activity system, respectively. Assume on \([0,S]\)

\[
 F(0)=F_C(0)=0,
 \quad F'(s)\ge\kappa>0,
 \quad\sup_{0\le s\le S}|F_C(s)-F(s)|\le\varepsilon,
 \quad F(S),F_C(S)>y.
\tag{14}
\]

Assume both scalar equations below are locally well posed and their
solutions remain in \([0,S]\), as they do when both activity curves have a
positive training slope. Define their own physical clocks by

\[
 \dot s=2(y-F(s)),\qquad
 \dot s_C=2(y-F_C(s_C)),\qquad s(0)=s_C(0)=0.
\]

For \(e=s_C-s\), subtraction gives

\[
 \dot e=-2[F(s_C)-F(s)]+2[F(s_C)-F_C(s_C)].
\]

The mean value theorem and (14), with the upper right derivative at
\(e=0\), imply

\[
 \frac{d^+}{dt}|e|\le-2\kappa|e|+2\varepsilon,
 \qquad
 \sup_{t\ge0}|s_C(t)-s(t)|\le\varepsilon/\kappa.
\tag{15}
\]

Let \(f(s,x)\) and \(f_C(s,x)\) denote passive query predictions. If

\[
 E_\mu=
 \left(\int\sup_{0\le s\le S}|f_C(s,x)-f(s,x)|^2d\mu(x)\right)^{1/2},
 \quad
 L_\mu=
 \left(\int\sup_{0\le s\le S}|\partial_s f(s,x)|^2d\mu(x)\right)^{1/2},
\]

the triangle inequality, the fundamental theorem of calculus, and (15)
give

\[
 \left(\int\sup_{t\ge0}
 |f_C(s_C(t),x)-f(s(t),x)|^2d\mu(x)\right)^{1/2}
 \le E_\mu+L_\mu\varepsilon/\kappa.
\tag{16}
\]

The same estimate includes the fitted limits whenever the two clocks
converge. Thus the required physical-time supremum does not force analytic
continuation along a physical interval of length \(\log n\). Its geometric
length is the fixed short activity interval \(S=O(y)\).

## 5. The missing complex estimate and a possible proof route

The currently established finite Gaussian carrier bound is real. In this
notation it controls \(k=W^\top\delta\) on the real training path. It does
not by itself guarantee (6), even for training sources. In particular,

\[
 z'=\delta\frac{h^\top h}{n}
       +W[\operatorname{sech}^4a\odot k].
\tag{17}
\]

The second term is a new forward use of the same matrix after a reverse
response. A real bound on \(\|k\|_\infty\), together with
\(\|W\|_{\rm op}=O(1)\), gives a coordinatewise bound as large as
\(O(\sqrt n\|k\|_\infty)\) for this term. The Gaussian structure may
give a much better result, but operator-norm algebra alone does not.

Likewise, holomorphic tanh and real RMS control do not imply a
width-independent Banach-space analytic neighborhood. To avoid tanh's
complex poles, the imaginary part of every relevant preactivation must stay
away from \(\pm\pi/2\). A normalized RMS perturbation only bounds an
individual coordinate after multiplication by \(\sqrt n\). The prior
zero-radius Gaussian affine-displacement diagnostic also prevents simply
asserting a common population Taylor radius.

A possible new argument is the following, with every unproved implication
left visible.

1. Run (2) along prescribed complex activity contours, stopped before any
   first- or second-layer preactivation reaches imaginary part \(\pi/4\).
   On this stopped domain, tanh and every fixed-order derivative are
   bounded. Fixed short contour length gives the same operator and RMS
   tube estimates by absolute-value integration. The single-sample
   activity equations have no adaptive residual derivative.
2. Extend the finite column deletion/reinsertion argument to these complex
   contours to bound the complex reverse carriers. Complex Gaussian
   linear and quadratic forms can be split into real and imaginary parts,
   but the simultaneous source-control event and empirical budget
   bootstrap must still be proved on the stopped domain.
3. Add a row deletion argument for the upper forward preactivation. Given
   its row-deleted cavity, the deleted Gaussian row is independent of the
   cavity first feature. The cavity difference between activity \(s\) and
   \(s+iu\) has RMS at most \(CS|u|\). Its Gaussian linear contribution
   therefore has standard deviation \(O(S|u|)\). Reinsertion also adds a
   self-response mean and a nonlinear remainder. Their imaginary
   increments must be bounded, not discarded because the first Gaussian
   term is centered.
4. A simultaneous estimate of the form
   \(\max_i|\operatorname{Im}a_i|+\max_j|\operatorname{Im}z_j|
     \le C|u|\log n\)
   would exclude the first strip exit for \(|u|\le c/\log n\).
   A polynomial complex-time grid needs continuity control and a common
   stopping-time argument. Passive sphere queries require the analogous
   forward estimate, uniformly in the query or in a sufficient spatial
   analytic representation.

These steps are not obtained by merely replacing real quantities by their
absolute values in the existing proof. Row deletion, imaginary-increment
control, a common complex stopping domain, and the query class are new
requirements. In particular, the real carrier theorem cannot be cited as
though it already proved them.

The highest-leverage unresolved statement is therefore a finite-width,
two-sided complex activity estimate of logarithmic strip width for the
actual one-input dense Gaussian network. If it can be proved with constants
compatible with a fixed small label, (7)--(16) provide a concrete route from
initialization-derived source spaces to an all-physical-time comparison.
If this analytic route fails, the general source-dependent sampler remains
open; failure would not yield the Gaussian-sampler lower bound that the user
has already rejected as insufficient.

# Gaussian averaging does not supply the growing-order NTH upper bound

This is the scoped Gaussian-averaging proof route for the standard frozen-top
neural tangent hierarchy (NTH). It does not prove an unconditional growing-order
upper bound for the assigned network. It proves a quantitative obstruction to
one proposed inference: analyticity after averaging the initialization, together
with concentration at every fixed order, does not imply useful concentration
of the empirical Taylor truncation at growing order. The obstruction holds for
an explicitly Gaussian-smoothed tanh observable whose mean is analytic on a
width-independent disk. It therefore persists even when the desired smoothing
of the mean has succeeded.

The result is a proof-route bottleneck, not a counterexample to the network
conjecture. No conclusion about divergence of actual NTH predictions is drawn.
In particular, the calculations below do not replace the two-hidden-layer
network by the scalar example.

Author: `/root/nth_average_upper`, 2026-10-10. Scientific inputs: the supervisor's
neutral assignment, the complete same-study `TANH_UPPER_ROUTE.md`, and
`docs/notation.qmd`. Required scoped-work, canonical-notation, research, and proof
instructions were read. No other study, archived chapter, external scientific
source, experiment, or Git operation was used. The present proof is newly
derived and awaits a separate mathematical check; it is not marked internally
checked.

## 1. The network question retained by this route

Let \(v_a\in\mathbb R^d\), \(1\le a\le m\), be fixed unit inputs, with
\(m\ge2\), and optionally include a fixed finite panel of passive unit queries.
The input Gram is \(G_{ab}=v_a^\top v_b\); no orthogonality is assumed. The network
and loss are

\[
\begin{aligned}
z_a^{(1)}&=W^{(1)}v_a,& h_a^{(1)}&=\tanh z_a^{(1)},\\
z_a^{(2)}&=W^{(2)}h_a^{(1)},& h_a^{(2)}&=\tanh z_a^{(2)},\\
f_a&=u^\top h_a^{(2)}/n,& r_a&=f_a-y_a,
&\mathcal L&=\frac1{2m}\sum_{a=1}^m r_a^2.
\end{aligned}
\]

The shapes of \(W^{(1)},W^{(2)},u\) are \(n\times d,n\times n,n\). Independent
initial entries of the first two matrices have laws \(N(0,1)\) and
\(N(0,1/n)\), respectively, and \(u_0=0\). The mobility blocks are \(n,1,n\).
With \(\theta=(W^{(1)},W^{(2)},u)\), the unit driving fields are

\[
\begin{aligned}
\delta_b^{(2)}&=u\odot\tanh'(z_b^{(2)}),\\
\delta_b^{(1)}&=\tanh'(z_b^{(1)})\odot W^{(2)\top}\delta_b^{(2)},\\
V_b(\theta)&=
\left(\delta_b^{(1)}v_b^\top,
\frac{\delta_b^{(2)}h_b^{(1)\top}}n,h_b^{(2)}\right).
\end{aligned}
\]

Thus \(\dot\theta=\sum_b c_bV_b(\theta)\), where
\(c_b=(y_b-f_b)/m\). The hierarchy is defined by

\[
K_{1,a}=f_a,\qquad
K_{s+1,a_1\ldots a_s b}=D K_{s,a_1\ldots a_s}[V_b].
\]

The order-\(q\) system retains ranks \(1,\ldots,q\), initializes every tensor
at the realized \(\theta_0\), freezes rank \(q\), and evolves lower ranks using
its own residual control \(c_b^{(q)}=(y_b-f_b^{(q)})/m\).

The target is a sufficient \(q=q(n)\) giving all-time finite-panel prediction
error of order \(n^{-1/2}\) at fixed confidence, for a positive population
final-feature Gram gap \(\gamma\) and fixed nonzero
\(Y=\|y\|_2/\sqrt m\le\gamma/(64m)\). The labels cannot shrink with width.
The conditional ordered-derivative criterion in `TANH_UPPER_ROUTE.md` is an
available reduction, not a solved premise of this route.

## 2. An analytic Gaussian mean with unusable empirical Taylor truncations

Here the scalar random variables \(Z_i,g_i\), \(i\ge1\), are independent
standard Gaussians; they are diagnostic variables, not network coordinates.
For a fixed real \(s\), define

\[
\psi(x)=\tanh^2x,\qquad
F_n(s)=\frac1n\sum_{i=1}^n\psi(Z_i+s g_i),\qquad
a_k(x)=\frac{\psi^{(k)}(x)}{k!},
\]

and take the literal Taylor polynomial of the realized empirical observable:

\[
P_{n,q}(s)=\frac1n\sum_{i=1}^n\sum_{k=0}^q a_k(Z_i)(s g_i)^k.
\tag{1}
\]

There exists an absolute constant \(c_0>0\) such that the following statements
hold.

1. The mean \(F(s)=\mathbb E F_n(s)\) extends holomorphically to \(|s|<1\).
   For every fixed order, averaging (1) gives the Taylor polynomial of \(F\).
2. For every fixed real \(s\ne0\), every fixed finite \(C>0\), and every integer
   sequence \(q(n)\to\infty\) with \(q(n)\le c_0\log n\),

   \[
   \mathbb P\left(
   |P_{n,q(n)}(s)-F_n(s)|\le\frac C{\sqrt n}
   \right)\longrightarrow0.
   \tag{2}
   \]

One admissible explicit choice is

\[
c_0=\frac1{4\log(256e^2)}.
\tag{3}
\]

The constants in intermediate bounds may depend on the fixed \(s\), but (3)
does not. Statement (2) includes all parities of \(q\). It concerns error
against the same empirical observable, not error against its population mean.

### Analyticity of the mean

For real \(s\), \(Z+s g\) is a centered Gaussian of variance \(1+s^2\), so

\[
F(s)=\frac1{\sqrt{2\pi(1+s^2)}}
\int_{\mathbb R}\psi(x)
\exp\left(-\frac{x^2}{2(1+s^2)}\right)dx.
\tag{4}
\]

For \(|s|<1\), \(1+s^2\) lies in the right half-plane. Use the holomorphic
square-root branch that is positive at \(s=0\). On every disk \(|s|\le R<1\),

\[
\operatorname{Re}\frac1{1+s^2}
\ge\frac{1-R^2}{(1+R^2)^2}>0.
\]

Since \(0\le\psi(x)\le1\) on the real axis, the integral and its complex
derivatives on smaller compact disks are dominated by Gaussian integrable
functions. This proves the asserted holomorphic extension. Each fixed real
derivative can also be passed under the original expectation: all fixed real
derivatives of tanh are bounded and all Gaussian moments are finite. Hence
\(\mathbb E P_{n,q}\) is exactly the Taylor polynomial of (4).

In particular, for \(|s|<R<1\) its mean error is bounded by

\[
|\mathbb E P_{n,q}(s)-F(s)|
\le\frac{B_R}{1-|s|/R}\left(\frac{|s|}{R}\right)^{q+1},
\qquad B_R=\max_{|w|=R}|F(w)|<\infty.
\tag{5}
\]

Thus the obstruction in (2) is present despite a geometric bound for the
averaged Taylor tail.

### The real derivatives retain the nearest complex poles in their second moment

Put \(r=\pi/2\). There are absolute constants \(c>0\) and \(q_0\) such that

\[
\mathbb E[a_q(Z)^2]\ge c q r^{-2q}
\qquad(q\ge q_0).
\tag{6}
\]

Here is a direct proof, including both parities. The only poles of \(\psi\)
inside \(|z|<3r\) are the double poles at \(\pm ir\). Because
\(\tanh(ir+w)=\coth w=w^{-1}+w/3+O(w^3)\), their principal parts are
\((z-ir)^{-2}\) and \((z+ir)^{-2}\), with no simple-pole terms. Therefore

\[
J(z)=\psi(z)-(z-ir)^{-2}-(z+ir)^{-2}
\]

is holomorphic on \(|z|<3r\). It is bounded by some finite \(M\) on
\(|z|\le2r\). For real \(|x|\le r/2\), Cauchy's derivative estimate on the
circle centered at \(x\) of radius \(3r/2\) gives

\[
\left|\frac{J^{(q)}(x)}{q!}\right|
\le M(3r/2)^{-q}.
\tag{7}
\]

The sum of the two principal-part coefficients is

\[
(-1)^q(q+1)\big[(x-ir)^{-q-2}+(x+ir)^{-q-2}\big].
\tag{8}
\]

Define \(\delta_q=0\) for even \(q\), \(\delta_q=\pi/2\) for odd \(q\), and
\(x_q=r\tan(\delta_q/(q+2))\). On the interval

\[
|x-x_q|\le\frac r{16(q+2)},
\tag{9}
\]

the phase \((q+2)\arg(x+ir)\) differs from an integer multiple of \(\pi\)
by at most \(1/16\): the phase is exactly such a multiple at \(x_q\), and its
derivative in absolute value is at most \((q+2)/r\). Also \(|x|=O(r/q)\), so

\[
(x^2+r^2)^{-(q+2)/2}
=r^{-q-2}(1+O(q^{-2}))^{-(q+2)/2}
\ge\tfrac34r^{-q-2}
\]

for all sufficiently large \(q\), uniformly on (9). Consequently the absolute
value of (8) is at least \((q+1)r^{-q-2}\) there. The ratio of (7) to this
lower bound tends to zero geometrically. Enlarging \(q_0\) therefore gives

\[
|a_q(x)|\ge\tfrac12(q+1)r^{-q-2}
\quad\hbox{on (9), for }q\ge q_0.
\]

The Gaussian density has a fixed positive lower bound on these intervals, whose
length is of order \(q^{-1}\). Integrating the square proves (6).

We also have the upper bound

\[
\sup_{x\in\mathbb R}|a_k(x)|\le (2/r)^k.
\tag{10}
\]

Indeed, \(|\tanh(x+iy)|\le1\) for real \(x\) and \(|y|\le\pi/4=r/2\): its
squared modulus is
\((\sinh^2x+\sin^2y)/(\sinh^2x+\cos^2y)\). Apply Cauchy's coefficient estimate
on the radius-\(r/2\) disk centered at the real point \(x\).

### The highest Gaussian polynomial component cannot cancel against lower orders

For one pair of independent standard Gaussians \(Z,g\), write

\[
X_q=\sum_{k=0}^q a_k(Z)(s g)^k-\psi(Z+s g),\qquad
\sigma_q^2=\operatorname{Var}(X_q).
\]

Let \(H_q\) be the probabilists' Hermite polynomial, defined by
\(H_q(x)e^{-x^2/2}=(-1)^q(d/dx)^q e^{-x^2/2}\). Repeated Gaussian integration
by parts gives

\[
\mathbb E[g^k H_q(g)]=0\ (k<q),\qquad
\mathbb E[g^q H_q(g)]=q!,\qquad
\mathbb E H_q(g)^2=q!.
\]

The boundary terms vanish because a polynomial times a Gaussian density and
each of its derivatives vanish at infinity. The last identity also follows
by integrating against the monic degree-\(q\) polynomial \(H_q\).

The orthogonal projection in \(L^2(Z,g)\) onto functions of the form
\(B(Z)H_q(g)/\sqrt{q!}\) sends the polynomial part of \(X_q\) to

\[
s^q\sqrt{q!}\,a_q(Z)\frac{H_q(g)}{\sqrt{q!}}.
\]

The projection of \(\psi(Z+s g)\) has norm at most one. Centering \(X_q\)
does not affect this projection, because \(q\ge1\). By contraction of
orthogonal projection, the triangle inequality, and (6),

\[
\sigma_q\ge
|s|^q\sqrt{q!}\,\|a_q(Z)\|_{L^2}-1
\ge c\sqrt q\,\sqrt{q!}\left(\frac{|s|}{r}\right)^q-1.
\tag{11}
\]

The constant \(c\) has been decreased if necessary. For each fixed nonzero
\(s\), this tends to infinity as \(q\to\infty\). The factorial is a variance
effect that the analytic first moment in (4) does not see. Equation (11)
controls the complete truncation error, so it does not assume that the last
ordinary monomial dominates all preceding terms pointwise.

### Growing-order concentration and the probability statement

Set \(U=2/r\). The Gaussian moment identity and an elementary bound give

\[
\|g^k\|_{L^4}=\big((4k-1)!!\big)^{1/4}\le(4k)^{k/2}.
\]

Using (10), Minkowski's inequality, boundedness of \(\psi\), and then
centering, we obtain, for each fixed \(s\ne0\) and all sufficiently large \(q\),

\[
\|X_q-\mathbb E X_q\|_{L^4}
\le C(q+1)(2U|s|\sqrt q)^q.
\tag{12}
\]

To see that this bounds the entire sum, each summand has norm at most
\((2U|s|\sqrt k)^k\); when \(2U|s|\sqrt q\ge1\), every such term for
\(k\le q\) is at most \((2U|s|\sqrt q)^q\). Also
\(q!\ge(q/e)^q\), as follows by comparing \(\sum_{j=1}^q\log j\) with
\(\int_1^q\log x\,dx\). Combining this with (11), and absorbing its final
\(-1\) for large \(q\), yields

\[
\frac{\mathbb E|X_q-\mathbb E X_q|^4}{\sigma_q^4}
\le C q^2(4\sqrt e)^{4q}
=Cq^2(256e^2)^q.
\tag{13}
\]

For \(q=q(n)\) in (3), the right-hand side of (13), divided by \(n\), tends
to zero. Let \(X_{q,1},\ldots,X_{q,n}\) be the independent copies constructed
from the \(n\) Gaussian pairs, and define

\[
T_n=\frac{\sum_{i=1}^n(X_{q,i}-\mathbb E X_q)}{\sqrt n\,\sigma_q}.
\]

Then \(T_n\) converges in distribution to a standard Gaussian. For completeness,
the characteristic-function proof uses

\[
\mathbb E e^{it(X_q-\mathbb E X_q)/(\sqrt n\sigma_q)}
=1-\frac{t^2}{2n}
 +O\left(\frac{|t|^3\mathbb E|X_q-\mathbb E X_q|^3}
                  {n^{3/2}\sigma_q^3}\right).
\]

Cauchy--Schwarz bounds the error after multiplication by \(n\) by a constant
times \([\mathbb E|X_q-\mathbb E X_q|^4/(n\sigma_q^4)]^{1/2}\), which tends
to zero by (13). Independence raises this expression to the \(n\)-th power,
giving \(e^{-t^2/2}\); the continuity theorem for characteristic functions
gives the asserted convergence.

Since the Gaussian distribution function is continuous, this convergence also
implies that the largest probability of any interval of length tending to zero
tends to zero. One can verify this directly by dividing a fixed bounded interval
into a sufficiently fine fixed mesh, using convergence at its endpoints, and
then controlling the two tails.

Finally,

\[
\sqrt n\,[P_{n,q}(s)-F_n(s)]
=\sqrt n\,\mathbb E X_q+\sigma_q T_n.
\]

The event in (2) restricts \(T_n\) to an interval of length \(2C/\sigma_q\),
with an arbitrary center. Its length tends to zero by (11), proving (2).
This argument allows any deterministic mean bias; no small-bias assumption
is hidden in the probability claim.

## 3. What this proves about the proposed NTH proof mechanism

The following implication is false, even for a bounded tanh observable driven
by independent Gaussians:

> The averaged response is analytic on a fixed disk, and each fixed Taylor
> coefficient has an empirical fluctuation of order \(n^{-1/2}\); therefore
> Taylor truncation at a growing logarithmic order approximates the same
> empirical response at the \(n^{-1/2}\) scale.

The fixed-order fluctuation assertion in this example follows directly from
finite variance and independence. What fails is uniformity in the order. The
first-moment integration-by-parts cancellation responsible for (4) does not
control the second moment of the empirical truncation error. In (11), an
orthogonal Gaussian polynomial component explicitly survives every cancellation
among its lower-order terms.

This is more specific than the coordinate-strip obstruction already in
`TANH_UPPER_ROUTE.md`: the mean here really has a fixed holomorphic disk.
It also differs from the example \(\mathbb E\tanh^2(sg)\), which has zero Taylor
radius. The present failure survives after a separate initial Gaussian \(Z\)
repairs that radius.

The proof does not identify such an uncancelled component in the actual NTH
observable. A corresponding identification would require a separate network
argument; neither (6) nor (11) is asserted for a network tensor.

## 4. The actual network still has a second-moment and adaptivity gap

For a deterministic control \(c=(c_1,\ldots,c_m)\), write \(\theta_c(t)\) for
the solution of \(\dot\theta_c=\sum_b c_bV_b(\theta_c)\), wherever it exists,
with the realized Gaussian initialization. Define the ordered integrals

\[
I_{b_1\ldots b_k}[c](t)
=\int_{0\le t_k\le\cdots\le t_1\le t}
\prod_{i=1}^k c_{b_i}(t_i)\,dt_k\cdots dt_1.
\]

The kernel generated by freezing at rank \(q\) along this control is exactly

\[
\mathcal K_{n,q}[c]_{jb}(t)=
\sum_{k=0}^{q-2}\sum_{b_1,\ldots,b_k}
K_{k+2,jb b_1\ldots b_k}(\theta_0)
I_{b_1\ldots b_k}[c](t).
\tag{14}
\]

The quantity that an averaging argument must estimate is the complete,
realization-dependent response defect

\[
K_{2,jb}(\theta_c(t))-\mathcal K_{n,q}[c]_{jb}(t).
\tag{15}
\]

Even a geometric bound on the expectation of (15), for every deterministic
control of small total action, does not bound its second moment. Applying
separate fixed-order concentration inequalities to the initialized tensors
does not close that gap: their constants may grow as in (11)--(13).
The example proves that one must control cancellations in (15) itself, or
establish an order-uniform estimate strong enough to imply such control.

There is a second distinction. The dense residual control and the closure's
residual control depend on the same Gaussian initialization used in their
tensors. A concentration assertion for each prescribed deterministic control
cannot simply be evaluated at either random control. One needs uniform control
over an adequate reachable class, or a direct argument that retains this
dependence. The ordered-integral stability argument in `TANH_UPPER_ROUTE.md`
addresses propagation once the required source estimate is available; it does
not supply this missing estimate.

The Gaussian carrier causing concern is genuinely present in the network,
although its eventual contribution to (15) remains unresolved. Along the
single actual hierarchy direction \(d\theta/ds=V_b(\theta)\), put
\(h=h_{b,0}^{(1)}\), \(z=z_{b,0}^{(2)}\), and
\(w=\tanh z\odot\tanh' z\). Direct differentiation at \(u_0=0\) gives

\[
z_b^{(1)\prime\prime}(0)
=\tanh'(z_{b,0}^{(1)})\odot W_0^{(2)\top}w.
\tag{16}
\]

Conditional on \(h,z\), Gaussian row regression gives exactly

\[
W_0^{(2)\top}w\overset{\rm law}=
\frac{z^\top w}{\|h\|_2^2}h
+\frac{\|w\|_2}{\sqrt n}
\left(g-h\frac{h^\top g}{\|h\|_2^2}\right),
\qquad g\sim N(0,I_n).
\tag{17}
\]

The event \(\|h\|_2=0\) has probability zero. Formula (17) follows by
decomposing each Gaussian row into its projection onto \(h\) and its independent
orthogonal component. It is included to identify the actual shared-disorder
issue, not to infer high-order behavior from the second derivative.

Higher derivatives in (15) differentiate both this carrier and its coefficients,
and sum paths through both hidden layers. Their possible cancellation cannot
be inferred either from the mean response or from (16). The unresolved
network-specific step is precisely whether those cancellations suppress the
growing-order fluctuation that survives in the scalar diagnostic.

## 5. The nonlinear first-layer carrier has the same factorial fluctuation

After Sections 1--4 were frozen, the supervisor authorized comparison with
`/root/nth_gaussian_tail_lower`. That exchange supplied the first-layer
star expression, including its induced-readout term. The following argument
was then derived here. It makes the carrier obstruction more specific to the
network geometry, but does not claim a growing-order cavity expansion for the
full network.

For \(x\in(-1,1)\), let \(H(\tau,x)\) be the real solution of

\[
\partial_\tau H=(1-H^2)^2,\qquad H(0,x)=x.
\tag{18}
\]

It is defined for all real \(\tau\) and remains in \((-1,1)\): the endpoints
are equilibria, uniqueness prevents crossing, and the bounded solution
continues. If \(x=\tanh X\), then

\[
H(\tau,\tanh X)=\tanh(F^{-1}(F(X)+\tau)),\qquad
F(w)=\frac w2+\frac{\sinh(2w)}4.
\]

Indeed \(F'(w)=\cosh^2w\), so the inverse flow has
\(\partial_\tau w=\operatorname{sech}^2w\) and (18) follows by the chain rule.
Here \(F^{-1}\) denotes the real inverse; no complex inverse is needed below.

The complete scalar star response, including both the direct feature change
and the induced readout change, is the following defined function:

\[
\begin{aligned}
S(s;x,g)={}&s g[H(gs^2/2,x)-x]\\
&+\int_0^s g[H(gt^2/2,x)-x]dt.
\end{aligned}
\tag{19}
\]

Formula (19) is the exact observable of this frozen-background scalar system.
It is not asserted to equal the whole network's observable. Let

\[
A_0(x)=x,\qquad
A_{k+1}(x)=(1-x^2)^2A_k'(x),\qquad a_k^*(x)=A_k(x)/k!.
\tag{20}
\]

The Taylor polynomial of (19) through degree \(2K+1\) is exactly

\[
S_K(s;x,g)=\sum_{k=1}^K b_k(s)a_k^*(x)g^{k+1},\qquad
b_k(s)=\frac{s^{2k+1}}{2^k}\left(1+\frac1{2k+1}\right).
\tag{21}
\]

The extra factor \(1+1/(2k+1)\) is obtained by integrating \(t^{2k}\) in the
second term of (19); discarding that term would give the wrong source
coefficient. These formulas hold for every finite Taylor order, independently
of convergence of an infinite expansion.

### A derivative estimate valid at every order and both parities

For a standard Gaussian \(X\), there are absolute constants \(c,C>0\) such that
for all \(k\ge1\),

\[
\|a_k^*(\tanh X)\|_{L^2}\ge\frac{c\,64^{-k}}{\sqrt k},
\qquad
\sup_{|x|\le1}|a_k^*(x)|\le12^k.
\tag{22}
\]

The polynomial \(A_k\) has degree \(D=3k+1\) and leading coefficient
\(\prod_{j=0}^{k-1}(3j+1)\). This follows by induction from (20), since the
leading term of \((1-x^2)^2\) is \(x^4\). The leading coefficient of
\(a_k^*\) is therefore at least one. The density of \(\tanh X\) is

\[
\frac{\exp[-(\operatorname{arctanh}x)^2/2]}
     {\sqrt{2\pi}(1-x^2)},\qquad -1<x<1,
\]

and has a positive lower bound on \([-1/2,1/2]\). For a degree-\(D\)
polynomial \(p\) with leading coefficient \(c_D\), its component along the
degree-\(D\) Legendre polynomial gives

\[
\left(\int_{-1/2}^{1/2}p(x)^2dx\right)^{1/2}
\ge\frac{|c_D|4^{-D}}{\sqrt{2D+1}}.
\tag{23}
\]

To verify the normalization, the Legendre polynomial on \([-1,1]\) has leading
coefficient \(2^{-D}\binom{2D}{D}\le2^D\) and squared norm \(2/(2D+1)\).
These identities follow from its Rodrigues formula by integration by parts.
Substitute \(x=t/2\) and retain its orthogonal component; (23) follows.
Applying (23) with \(D=3k+1\) proves the lower bound in (22), after absorbing
the fixed factor \(4^{-1}\) and the factor between \(\sqrt{6k+3}\) and
\(\sqrt k\) into \(c\).

For the upper bound, let \(B_k\) be the sum of the absolute coefficients of
\(A_k\). Recursion (20) gives
\(B_{k+1}\le4(3k+1)B_k\), with \(B_0=1\). Since
\(3k+1\le3(k+1)\), we get \(B_k\le12^k k!\), proving the second part of
(22). This proof supplies the all-order lower bound without a nearest-pole
asymptotic or a parity restriction.

For independent pairs \((X_i,g_i)\), the empirical difference between (19)
and (21) obeys the same growing-order failure as (2): for every fixed
\(s\ne0,C>0\), and every \(K(n)\to\infty\) with
\(K(n)\le c_1\log n\),

\[
\mathbb P\left(
\left|\frac1n\sum_{i=1}^n
 [S_K(s;\tanh X_i,g_i)-S(s;\tanh X_i,g_i)]\right|
\le C n^{-1/2}\right)\longrightarrow0
\tag{24}
\]

for an absolute \(c_1>0\). Here is the quantitative verification. Project
the single-pair error onto Hermite degree \(K+1\) in \(g\). Equations
(21)--(22) and \(|S(s;x,g)|\le4|s||g|\) give

\[
\operatorname{sd}(S_K-S)
\ge c|s|\sqrt{K!}\left(\frac{s^2}{128}\right)^K-4|s|.
\tag{25}
\]

The normalized fourth moment is bounded by
\(C_s K^6(4096)^{4K}\) for all sufficiently large \(K\). To obtain this bound,
use \(|b_k(s)|\le2|s|(s^2/2)^k\), (22), and
\(\|g^{k+1}\|_4\le[4(k+1)]^{(k+1)/2}\). Their sum is at most
\(C_s K^{3/2}(12s^2\sqrt{K+1})^K\). Divide by (25), using
\(\sqrt{K!}\ge(K/e)^{K/2}\). The exponential factor in the resulting norm
ratio is \(1536\sqrt e<4096\), and the remaining factors are polynomial
in \(K\). The centering and the bounded contribution of (19) only change
\(C_s\).

For example, \(c_1=1/(16\log4096)\) makes this normalized fourth moment
divided by \(n\) tend to zero. The characteristic-function and small-interval
argument used for (2) now proves (24). Thus the nonlinear inverse-coordinate
flow proposed for the first-layer star does not remove the fluctuation
obstruction.

### The actual Gaussian projection constraint also preserves this sector

One can retain exactly the Gaussian correlation in (17) for the star system.
Let \(h_j=\tanh X_j\), with \(X_j\) independent standard Gaussians, and set

\[
P=I-hh^\top/\|h\|_2^2,\qquad g=\mu h+\sigma P\xi,
\qquad \xi\sim N(0,I_n),
\tag{26}
\]

conditional on \(h\), where \(|\mu|\le M\) and
\(0<\sigma_0\le\sigma\le M\). These parameters may depend on other
conditioned variables; the following estimates are uniform over this range.
Define the averages \(\overline S=n^{-1}\sum_j S(s;h_j,g_j)\) and
\(\overline S_K=n^{-1}\sum_j S_K(s;h_j,g_j)\).

For \(K\to\infty\) with \(K\le c_2\log n\), there is an event in \(h\)
of probability tending to one on which the conditional centered defect obeys

\[
\sqrt{\operatorname{Var}_\xi(\overline S_K-\overline S\mid h)}
\ge\frac1{\sqrt n}\left[
c|s|\sigma\sqrt{K!}
 \left(\frac{\sigma s^2}{128}\right)^K-C_{s,M}
\right].
\tag{27}
\]

This is a second-moment statement; a fixed-confidence claim for the correlated
model is not inferred from (27) alone.

To prove it, put \(d=K+1\). The highest homogeneous Gaussian-chaos component
of \(\overline S_K\) has squared norm

\[
\frac{b_K(s)^2\sigma^{2d}d!}{n^2}
\sum_{i,j=1}^n a_K^*(h_i)a_K^*(h_j)P_{ij}^{d}.
\tag{28}
\]

This identity follows from Wick's formula: the degree-\(d\) centered Wick
powers of jointly Gaussian coordinates of covariance \(P\) have covariance
\(d!P_{ij}^d\). It can also be checked by comparing degree-\(d\) coefficients
in the Gaussian identity
\(\mathbb E e^{t(P\xi)_i-t^2P_{ii}/2}
e^{u(P\xi)_j-u^2P_{jj}/2}=e^{tuP_{ij}}\).
The drift \(\mu h\) contributes only lower degrees and does not alter (28).

With probability tending to one, \(\|h\|_2^2\ge c n\). On that event,
\(P_{ii}\ge1-C/n\) and \(|P_{ij}|\le C/n\) for \(i\ne j\). Writing
\(a_i=a_K^*(h_i)\), Cauchy--Schwarz gives

\[
\begin{aligned}
\sum_{i,j}a_i a_jP_{ij}^d
&\ge(1-C/n)^d\sum_i a_i^2
 -(C/n)^d\left(\sum_i|a_i|\right)^2\\
&\ge\big[(1-C/n)^d-n(C/n)^d\big]\sum_i a_i^2
\ge\tfrac12\sum_i a_i^2
\end{aligned}
\tag{29}
\]

for \(d\ge2\) and \(d=O(\log n)\), when \(n\) is sufficiently large.
Let \(m_K=\mathbb E[a_K^*(\tanh X)^2]\). By (22),
\(m_K\ge c64^{-2K}/K\) and \(a_K^*(h)^2\le144^K\). Thus

\[
\mathbb P\left(\frac1n\sum_i a_K^*(h_i)^2<\frac{m_K}2\right)
\le\frac{4\,144^K}{n m_K}
\le\frac{C K(589824)^K}{n}.
\tag{30}
\]

For example, \(c_2=1/[4\log589824]\) makes this tend to zero. Combining
(28)--(30) yields the first term on the right of (27).

It remains to ensure that the complete real star observable cannot itself
cancel this term in conditional \(L^2\). Differentiating (19), and using
\(|H-x|\le2\), \(0\le\partial_\tau H\le1\), gives

\[
|\partial_g S(s;x,g)|
\le4|s|+\tfrac23|s|^3|g|.
\tag{31}
\]

Since \(P\) has operator norm at most one, Gaussian Poincare's inequality gives

\[
\operatorname{Var}_\xi(\overline S\mid h)
\le\mathbb E_\xi\|\nabla_\xi\overline S\|_2^2
\le\frac{C_{s,M}}n.
\tag{32}
\]

The first inequality can be proved by expanding a square-integrable Gaussian
function in multivariate Hermite polynomials: its variance sums squared
coefficients of total degrees at least one, whereas the squared-gradient
integral weights each such coefficient by its total degree. The function
here and its gradient are square-integrable by (19), (26), and (31), so
Gaussian polynomial approximation extends the inequality to it. For the
second inequality, the gradient is
\(\sigma n^{-1}P(\partial_g S(s;h_j,g_j))_{j=1}^n\); (31) and
\(\mathbb E g_j^2\le M^2+M^2\) complete the bound.

Projecting the centered difference onto degree \(d\), and subtracting the
square root of (32) from the square root of (28), proves (27).

Equations (26)--(32) handle precisely the finite-rank Gaussian projection
arising in one-input row regression; they do not require independent carriers
after conditioning. In the actual network the bounds on \(\mu,\sigma\) in
(17) hold with probability tending to one, as proved in the supplied upper
route. What remains unproved is identifying (28) as an uncancelled part of
the complete growing-order NTH response, rather than of its frozen-background
star sector. Other network terms can have the same Gaussian-chaos degree,
and powers of higher ordinary degree also project onto that degree. A uniform
cavity remainder estimate or an exact cancellation classification is needed
before (27) can imply anything about full NTH prediction error.

## 6. Route disposition

The Gaussian-averaging route has not produced the requested unconditional
\(q(n)\). Its sharp additional bottleneck is now quantitative: an analytic mean
does not justify even root-width accuracy of the empirical Taylor truncation,
and a complete tanh example proves failure for every growing order in a
logarithmic range. The same factorial fluctuation is proved for the proposed
nonlinear first-layer star, including the exact projected Gaussian carrier.
This is a sector calculation; the full-network cancellation question is open.
The network route can reopen only with an actual bound for
the mixed-response defect (15) at growing order, including its fluctuations
and the dependence on the residual control, or with a network-specific
cancellation mechanism that proves such a bound.

Replacing initialized NTH tensors by their Gaussian expectations, averaging
several independent initializations, damping high orders, or analytically
resumming an expansion would change the prescribed frozen-top approximation.
Those constructions may warrant separate analysis, but none is used here as a
substitute for the standard hierarchy.

## 7. Subsequent exact rank-eight feedback audit

The supervisor subsequently requested an algebraic check of the proposed
single-carrier grading at rank eight. The following identity was derived
before that task was redirected to the sinusoidal-family remainder bound.
It preserves the full feedback terms and is useful for auditing any claimed
star dominance. It does not prove their probabilistic size.

For a fixed source contraction \(c_a\), use Euclidean hidden coordinates
\(x=(W^{(1)}/\sqrt n,W^{(2)})\), normalized readout \(a=u/\sqrt n\), and
normalized source-feature map

\[
B(x)=n^{-1/2}\sum_a c_a h_a^{(2)}(x).
\]

The actual source equations are exactly
\(a'=B(x)\), \(x'=DB(x)^\top a\), and its scalar source prediction is
\(F=a^\top B(x)\). At \(x=x_0\), write

\[
b=B(x_0),\quad J=DB(x_0),\quad H=D^2B(x_0),\quad T=D^3B(x_0),
\]
\[
A=J^\top b,\qquad L=J^\top J,\qquad
Qv=H[v,\cdot]^\top b.
\]

Here \(Q\) is self-adjoint. All pairings and norms below are ordinary
Euclidean ones in these normalized coordinates. The complete derivative is

\[
\begin{aligned}
F^{(7)}(0)={}&64\|LA\|_2^2
+352\langle LA,QA\rangle
+272\langle JA,H[A,A]\rangle\\
&+480\|QA\|_2^2
+240\langle b,T[A,A,A]\rangle.
\end{aligned}
\tag{33}
\]

To verify it directly, expand
\(x=x_0+x_2s^2+x_4s^4+x_6s^6+O(s^8)\) and
\(B(x(s))=b+B_2s^2+B_4s^4+B_6s^6+O(s^8)\).
The source equations give

\[
x_2=A/2,\qquad x_4=(LA+3QA)/24,
\]
\[
\begin{aligned}
x_6={}&L^2A/720+LQA/240+J^\top H[A,A]/240\\
&+H[A,\cdot]^\top JA/72+QLA/144
+Q^2A/48+T[A,A,\cdot]^\top b/48.
\end{aligned}
\]

Furthermore

\[
B_2=JA/2,\quad
B_4=J(LA+3QA)/24+H[A,A]/8,
\]
\[
B_6=Jx_6+H[A,LA+3QA]/48+T[A,A,A]/48.
\]

Since \(a'=B\) and \(a(0)=0\), the coefficient of \(s^7\) in \(F\) is
\((8/7)\langle b,B_6\rangle+(8/15)\langle B_2,B_4\rangle\).
Substituting the preceding formulas and multiplying by \(7!\) gives (33).
As a normalization check, if \(B\) is linear then only the first term
remains, agreeing with the linear-system expansion.

The last two terms in (33) equal the rank-eight star contribution for the
potential \(\psi(x)=b^\top B(x)\) on the *entire* hidden parameter space.
Indeed \((\nabla\psi\cdot\nabla)^3\psi
=4\|QA\|_2^2+2\langle b,T[A,A,A]\rangle\), and the source/readout factor
in (13) at \(k=3\) is \(120\). The single-neuron first-layer star is only
the local first-layer subpart of these two terms. Their other hidden-layer
and off-diagonal contributions, as well as the first three terms of (33),
remain to be graded.

No rank-eight algebraic counterexample to leading star dominance was found
in this scoped calculation. This is not a proof of the joint-grading lemma.
In particular, operator-norm estimates alone can lose a factor \(n^{1/2}\)
relative to the proposed extra \(n^{-1}\) suppression; differently weighted
column contractions are not annihilated merely by conditioning away the
original reverse carrier. A probabilistic contraction estimate or a complete
response-tree bound is required for the quantitative remainder.

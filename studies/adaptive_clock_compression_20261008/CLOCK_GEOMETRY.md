# Exact clocks, endpoint regularity, and source rank

This is one bounded theoretical route, written on 2026-10-08. Its scientific
inputs were the supervisor's self-contained assignment, the complete notation
contract `docs/notation.qmd`, the model/dissipation/existence sections 1–3 of
`docs/01-training-geometry.qmd`, and the complete pre-target feature-budget and
physical-clock subsection at lines 4805–4889 of
`docs/10-correlated-pairs.qmd`. No other study, paper, history, or competing
route was read. Required mathematical-presentation, rigorous-proof, and
conjecture-investigation instructions were applied. No training or numerical
experiment was run. The statements below have derivations but have not received
independent review or promotion.

The conclusion is conditional and constructive: finite training motion permits
bounded clocks, and a scalar-residual feature clock can remove the fitted
endpoint singularity at fixed width. Finite length and exponential loss decay
alone do not supply endpoint analyticity. Reparameterization preserves optimal
uniform linear source rank exactly, although it can improve a particular
polynomial construction. These facts leave the proposed improvement from
`log(n)^5` to `log(n)^2` open for the assigned neural model.

## 1. Canonical model and the exact dissipation identities

Fix width $n$, hidden depth $L$, and $m$ training samples
$(x_a,y_a)$, with $x_a\in\mathbb R^d$. For scalar analytic activation
$\phi$, the maintained normalization is

\[
z_a^{(1)}=W^{(1)}x_a/\sqrt d,\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\phi(z_a^{(\ell)}),\qquad
f_a=\frac{W^{(L+1)\top}h_a^{(L)}}n.
\]

Here $W^{(1)}\in\mathbb R^{n\times d}$, the middle weights belong to
$\mathbb R^{n\times n}$, and $W^{(L+1)}\in\mathbb R^n$. The first
weights are independently $N(0,1)$, the middle entries independently
$N(0,1/n)$, and this assignment specifies the exactly zero stored readout.
All blocks train. The residual-free backward fields are

\[
\delta_a^{(L)}=W^{(L+1)}\odot\phi'(z_a^{(L)}),\qquad
\delta_a^{(\ell)}=\phi'(z_a^{(\ell)})\odot
W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]

Stack the raw parameters into $\theta\in\mathbb R^P$. Let $D$ be the
constant positive block mobility: $n\kappa_1$ on the first block,
$\kappa_\ell$ on middle block $\ell$, and $n\kappa_{L+1}$ on the
readout. Write

\[
F(\theta)=(f_a)_{a=1}^m,\quad r=F(\theta)-y,\quad
E=\mathcal L_n=\frac{\|r\|_2^2}{m},\quad
J=\frac{\partial F}{\partial\theta},\quad K=JDJ^\top.
\]

Physical gradient flow and its two immediate consequences are

\[
\dot\theta=-\frac2m DJ^\top r,\qquad
\dot r=-\frac2m Kr,\qquad
\dot E=-\frac4{m^2}r^\top Kr
       =-\|D^{-1/2}\dot\theta\|_2^2.                 \tag{1}
\]

Every assertion below concerning a general training trajectory assumes the
global trajectory exists and, along it,

\[
0<\kappa I_m\preceq K(t)\preceq\Lambda I_m.          \tag{2}
\]

The small-label theorem mentioned in the assignment is an upstream source of
such control; this route does not reprove it or silently infer (2) from
positive definiteness only at initialization. Constants in (2) may depend on
width unless a separate theorem makes them uniform.

Set $\rho(t)=\sqrt{E(t)}=\|r(t)\|_2/\sqrt m$. When
$r(0)\ne0$, put

\[
k(t)=\frac{r(t)^\top K(t)r(t)}{\|r(t)\|_2^2}.
\]

Then (1) gives

\[
\dot\rho=-\frac{2k}{m}\rho,\quad
\rho(0)e^{-2\Lambda t/m}\le\rho(t)
\le\rho(0)e^{-2\kappa t/m},\quad
v(t):=\|D^{-1/2}\dot\theta\|_2
=\frac{2\sqrt{k}}{\sqrt m}\rho.                     \tag{3}
\]

The lower exponential bound ensures the quotients used below are defined at
every finite time. The solution cannot hit $r=0$ at finite time: such a
parameter state is an equilibrium of the locally Lipschitz vector field, and
uniqueness backward over a finite interval would force the whole trajectory
to be constant. This is also immediate from the lower bound in (3).

Dividing the last identity in (3) by its first one yields a sharper finite
length estimate than separately integrating upper exponential bounds:

\[
\int_0^\infty v(t)\,dt
=\int_0^{\rho(0)}\sqrt{\frac m{k}}\,d\rho
\le\sqrt{\frac m\kappa}\rho(0).                     \tag{4}
\]

The integral notation uses the strictly decreasing inverse $t=t(\rho)$.
Consequently $D^{-1/2}\theta(t)$, and hence $\theta(t)$ at each fixed
width, converges to a finite $\theta_\infty$, with
$F(\theta_\infty)=y$. Finite-panel $h,\delta$, and any specified
initialized forward or transpose images of them converge by continuity.
No complex-time neighborhood is claimed by (4).

If $r(0)=0$, the physical solution is constant. Define every progress or
length clock below to be zero and use that constant continuation. A clock
inverse is unnecessary and does not exist in this degenerate case. In the
zero-readout initialization this case includes $y=0$.

## 2. Exact clocks and their inverses

For any continuously positive speed $c(t)$, define

\[
s(t)=\int_0^t c(u)\,du,\qquad
\Theta(s)=\theta(t(s)).
\]

On the open range of this strictly increasing clock,

\[
\frac{d\Theta}{ds}
=-\frac{2DJ(\Theta)^\top r(\Theta)}{m\,c(\Theta)},
\qquad
\frac{dt}{ds}=\frac1{c(\Theta)},\qquad t(0)=0.       \tag{5}
\]

The notation $c(\Theta)$ applies when the chosen speed is evaluated from
the current state. Equations (5) are exact reparameterizations of the full
network, not closed compressed models. To compare responses at the same
physical time, one must use this inverse relation or an equivalent evolution
of $s(t)$. An approximation evaluated at the same numerical clock value
has not automatically been compared at the same physical time.

### Loss logarithm and bounded loss progress

For $E(0)>0$, define

\[
\tau(t)=\log\frac{E(0)}{E(t)}.
\]

By (1),

\[
\dot\tau=\frac{4k}{m},\quad
\frac{d\theta}{d\tau}=-\frac{DJ^\top r}{2k},\quad
\frac{dt}{d\tau}=\frac m{4k}.                      \tag{6}
\]

Thus $\tau\in[0,\infty)$; it makes the loss exactly exponential,
$E=E(0)e^{-\tau}$, but does not compactify the all-time interval.
Assumption (2) makes $\tau$ quantitatively equivalent to physical time.

The bounded loss-progress clock is

\[
p(t)=1-\frac{E(t)}{E(0)}\in[0,1).
\]

Its equations are

\[
\dot p=\frac{4k}{m}(1-p),\qquad
\frac{d\theta}{dp}
=-\frac{mE(0)}{2}\frac{DJ^\top r}{r^\top Kr},\qquad
\frac{dt}{dp}=\frac{m}{4k(1-p)}.                   \tag{7}
\]

In particular $t(p)\to\infty$ as $p\uparrow1$. The denominator in
the parameter equation is quadratic in the residual while its numerator is
linear. The apparent endpoint singularity requires analysis, not cancellation
based only on $\dot E\to0$.

A potentially better finite clock for amplitude-like observables is

\[
b(t)=1-\sqrt{E(t)/E(0)}=1-\rho(t)/\rho(0).
\]

It satisfies $\dot b=(2k/m)(1-b)$. Removing this square root addresses
the elementary amplitude-versus-energy mismatch but does not remove the
multiple-rate obstruction in Section 3.

### Residual budget and actual residual-curve length

Two different quantities are sometimes called residual arc length. Their
definitions must not be interchanged. The integrated residual magnitude is

\[
s_r(t)=\int_0^t\rho(u)\,du,\qquad
\frac{d\theta}{ds_r}=-\frac{2}{\sqrt m}DJ^\top\frac r{\|r\|_2},
\qquad \frac{dt}{ds_r}=\frac1\rho.                 \tag{8}
\]

Its endpoint lies between $m\rho(0)/(2\Lambda)$ and
$m\rho(0)/(2\kappa)$. Its exact endpoint value generally depends on
the future path and is not available as causal initialization data. An upper
bound is available from the assumptions.

The actual length of the residual curve, in sample RMS units, is

\[
\sigma_r(t)=\int_0^t\frac{\|\dot r(u)\|_2}{\sqrt m}\,du
=\frac2{m\sqrt m}\int_0^t\|K(u)r(u)\|_2\,du.
\]

Its exact equations are

\[
\frac{d\theta}{d\sigma_r}
=-\sqrt m\frac{DJ^\top r}{\|Kr\|_2},\qquad
\frac{dt}{d\sigma_r}=\frac{m\sqrt m}{2\|Kr\|_2}.    \tag{9}
\]

Since $-\dot\rho\le\|\dot r\|_2/\sqrt m$ and
$\|Kr\|_2/\|r\|_2\le\Lambda$, substitution of (3) gives

\[
\rho(0)\le\sigma_r(\infty)
\le\frac\Lambda\kappa\rho(0).                    \tag{10}
\]

In (8) and (9), a normalized residual direction remains. Its endpoint
regularity is extra information.

### Parameter length and feature length

The mobility-metric parameter-length clock is

\[
\ell(t)=\int_0^t v(u)\,du,
\qquad
\frac{d\theta}{d\ell}=-\frac{DJ^\top r}{\sqrt{r^\top Kr}},
\qquad
\frac{dt}{d\ell}=\frac{m}{2\sqrt{r^\top Kr}}.       \tag{11}
\]

The transformed parameter path has unit speed in the $D^{-1}$ metric
and its length obeys (4). Unit speed gives a Lipschitz path through the
endpoint; it does not give differentiability of all orders there.

For a specified feature vector $H(\theta)$, an alternative is
$s_H(t)=\int_0^t\|\dot H(u)\|_2\,du$, using the desired RMS factors
explicitly when constructing $H$. If
$\|H_\theta D^{1/2}\|\le C$ along the path, then
$s_H(\infty)\le C\ell(\infty)$. But $\dot H$ can vanish while
other responses move. At zero readout, all hidden weight velocities and
hidden feature velocities vanish initially, whereas the readout can move
immediately.

More precisely, if for the selected hidden features and another required
response $B$,

\[
H(t)=H(0)+\tfrac12 A t^2+O(t^3),\quad A\ne0,
\qquad B(t)=B(0)+Ct+O(t^2),\quad C\ne0,
\]

then $s_H(t)=\|A\|_2t^2/2+O(t^3)$ and

\[
B(t(s_H))=B(0)+C\sqrt{2s_H/\|A\|_2}+O(s_H).
\]

This conditional calculation shows why a clock built from forward hidden
motion alone can introduce an initial square-root singularity in a backward
response. It is not a claim that these nonzero derivatives occur for every
activation or datum. A feature clock with plateaus also lacks an ordinary
inverse; identifying equal-clock states is valid only when all responses
being represented are constant on those plateaus.

### Physical-time comparisons and history weights

For an exact response $G(s)=H(\theta(t(s)))$, and a proposed approximation
$\widehat G,\widehat s$, the elementary decomposition is

\[
\|H(\theta(t))-\widehat G(\widehat s(t))\|
\le \|G(s(t))-\widehat G(s(t))\|
+\|\widehat G(s(t))-\widehat G(\widehat s(t))\|.    \tag{12}
\]

The second term is a synchronization error. It can be bounded by a modulus
of continuity when one is available; it cannot be omitted because the
representation error is small. Divergence of $dt/ds$ near fitting does
not itself prove that observables are unstable: their own motion may vanish
there. A useful proof estimates (12) in the actual response norm.

Likewise changing clocks in a memory integral requires the Jacobian:

\[
\int_0^t A(u)\,du
=\int_0^{s(t)} A(t(v))\frac{dv}{c(t(v))}.            \tag{13}
\]

In gradient-history integrals $A$ often contains a residual factor;
some speed factors can then cancel. The resulting normalized residual
direction or gate still needs its own regularity estimate. Clock choice
does not remove these factors by definition.

## 3. Exact two-mode obstruction to endpoint analyticity

This example concerns a generic analytic, stable gradient system. It is
**not** a counterexample satisfying the assigned Gaussian neural
initialization, depth, zero-readout, and finite-panel model contract.
Its purpose is to test an implication based only on exponential decay,
finite path length, and analyticity of the physical vector field.

Let $\alpha=\sqrt2$, $\theta=(x,z)\in\mathbb R^2$, and take

\[
F(x,z)=(x,\sqrt\alpha\,z),\quad y=0,\quad m=2,
\quad D=I_2,
\quad E(x,z)=\tfrac12(x^2+\alpha z^2).
\]

Starting at $(1,1)$, exact gradient flow is

\[
\dot x=-x,\quad \dot z=-\alpha z,\qquad
x(t)=e^{-t},\quad z(t)=e^{-\alpha t}.               \tag{14}
\]

The training Gram is the constant matrix
$K=\operatorname{diag}(1,\alpha)$; all the hypotheses (1)–(4) hold.
The vector field and all physical-time responses are entire. Write
$q=e^{-t}\in(0,1]$, so that $x=q,z=q^\alpha$.

For bounded loss progress the remaining clock interval is

\[
u=1-p=\frac{q^2+\alpha q^{2\alpha}}{1+\alpha}.
\]

Consequently $x\sim\sqrt{1+\alpha}\,u^{1/2}$, which is not
differentiable at $u=0$. Even a single decaying mode produces this
amplitude-versus-energy square root.

For square-root loss progress, $u=1-b=\sqrt{E/E(0)}\sim
q/\sqrt{1+\alpha}$. The second response then satisfies
$z\sim(1+\alpha)^{\alpha/2}u^\alpha$, with a nonintegral exponent.

For residual budget, actual residual-curve length, and parameter length,
the remaining lengths are respectively

\[
\begin{aligned}
s_r(\infty)-s_r(t)
 &=\frac1{\sqrt2}\int_0^q\sqrt{1+\alpha w^{2\alpha-2}}\,dw,\\
\sigma_r(\infty)-\sigma_r(t)
 &=\frac1{\sqrt2}\int_0^q\sqrt{1+\alpha^3w^{2\alpha-2}}\,dw,\\
\ell(\infty)-\ell(t)
 &=\int_0^q\sqrt{1+\alpha^2w^{2\alpha-2}}\,dw.
\end{aligned}                                                   \tag{15}
\]

Each remaining length is $Cq+o(q)$, with $C>0$. Thus its
second response has leading order $C^{-\alpha}u^\alpha$, which
cannot be real analytic at zero: a nonzero analytic function vanishing
at zero has an integral order of vanishing. For parameter length the
first response also exposes the singularity, since Taylor expansion of
the integrand gives

\[
u=q+\frac{\alpha^2}{2(2\alpha-1)}q^{2\alpha-1}
+o(q^{2\alpha-1}),\qquad
x=u-\frac{\alpha^2}{2(2\alpha-1)}u^{2\alpha-1}
+o(u^{2\alpha-1}).                                  \tag{16}
\]

Here $1<2\alpha-1<2$. In particular unit parameter speed does not
make the endpoint twice differentiable.

There is a stronger coordinate-independent statement for this example.
Suppose any scalar reparameterization approaching a finite endpoint made
both $x(u)$ and $z(u)$ real analytic there, positive on the interior,
and zero at the endpoint. Let their first nonzero Taylor orders be
integers $j,k\ge1$. The exact relation $z=x^\alpha$ forces
$k=\alpha j$, contradicting irrationality of $\alpha$. An analytic
function with every Taylor coefficient zero is identically zero near the
endpoint, so that case cannot evade the contradiction.

The logarithmic loss clock has no finite fitted endpoint; compactifying
it by $e^{-\tau/2}=\sqrt{E/E(0)}$ returns to the square-root-loss
case above. Therefore loss-log linearization alone is not a common
analytic compactification of a response panel.

This disproves the generic implication

> analytic gradient field + uniform positive Gram + exponentially decaying
> residual + finite motion implies a scalar finite clock in which every
> response is analytic through fitting.

It does not disprove the existence of a low-rank neural approximation,
nor a `log(n)^2` bound, nor useful nonpolynomial clock bases. Indeed this
example's complete state curve is contained in a two-dimensional linear
space despite its endpoint nonanalyticity.

### Why geometric polynomial approximation would be stronger

For completeness, geometric best uniform polynomial approximation on a
closed interval implies analytic extension to a complex neighborhood.
Here is the implication needed for the obstruction, without importing a
specialized approximation theorem.

Rescale the interval to $[-1,1]$. Suppose polynomials $P_N$ of degree
at most $N$ obey $\|g-P_N\|_\infty\le C\rho^{-N}$, with fixed
$\rho>1$. Then
$\|P_{N+1}-P_N\|_\infty\le C(1+\rho^{-1})\rho^{-N}$.
The Chebyshev coefficients of a polynomial of supremum norm $M$ are
bounded by $2M$, by their cosine-integral formula. On the complex
ellipse parametrized by $z=(w+w^{-1})/2$, $|w|=r>1$,
$T_j(z)=(w^j+w^{-j})/2$, so $|T_j(z)|\le r^j$.
The degree-$(N+1)$ difference therefore has complex supremum bounded
by $2(N+2)C(1+\rho^{-1})\rho^{-N}r^{N+1}$. For $1<r<\rho$
these bounds are summable. The telescoping polynomial series converges
uniformly on the ellipse and locally uniformly in its interior, defining
a holomorphic function whose restriction is $g$. Holomorphicity follows
from the Cauchy integral formula applied to the uniformly convergent
series on smaller contours.

Applying this scalar argument to a nonanalytic coordinate of (14) shows
that its endpoint obstruction rules out geometric-in-degree polynomial
convergence for that clock. It does not rule out slower polynomial
convergence or low source rank.

## 4. Optimal uniform linear source rank is clock invariant

Let $g_j(t)\in\mathcal H$, $1\le j\le N$, be any finite family
of sources in one fixed finite-dimensional normed space or Hilbert space.
For the neural application the sources can include all named sample/layer
features and backward fields, and their initialized forward/transpose
images, within each compatible layer space. Take the required finite RMS
normalizations in the norm, for example $\|v\|_2/\sqrt n$. Different
layer spaces may instead be treated separately or combined in a specified
direct sum. Define the best rank-$k$ uniform linear-source error by

\[
d_k=\inf_{\dim V\le k}\sup_{t\in I}\max_{1\le j\le N}
       \inf_{v\in V}\|g_j(t)-v\|.                       \tag{17}
\]

Let $\psi:J\to I$ be onto and monotone, and set
$\widetilde g_j(s)=g_j(\psi(s))$. For every fixed subspace $V$,
surjectivity alone gives

\[
\sup_{s\in J}\max_j\operatorname{dist}(\widetilde g_j(s),V)
=\sup_{t\in I}\max_j\operatorname{dist}(g_j(t),V).
\]

Taking the identical infimum over $V$ proves exact equality of all
$d_k$, and hence equality of the minimal rank achieving any specified
uniform error. Monotonicity is relevant for a training clock but unnecessary
for this set-theoretic identity. Adding an endpoint limit does not change
the supremum because distance to a fixed subspace is continuous.

The same proof works for affine source spaces, for a common family of
subspaces with layerwise budgets, and for an infimum over admissibly chosen
subspaces provided the admissibility/provenance restrictions are unchanged.
It does not grant a trajectory-dependent oracle subspace to a causal
construction. A non-onto clock, discarded tail, altered time weight, or
different norm would be a different approximation problem.

A degree-$p$ vector polynomial
$P(s)=\sum_{j=0}^p v_js^j$ has values in
$\operatorname{span}\{v_0,\ldots,v_p\}$. Better clock regularity can
therefore improve the rank upper bound obtained from this particular
construction. It cannot reduce the already optimal error (17), because
the set of vectors to be approximated did not change. These statements
are compatible: a better construction can approach the invariant optimum
more efficiently.

## 5. Chebyshev and Legendre are the same degree spaces

On a fixed clock interval, degree-$p$ Chebyshev and Legendre expansions
both span all polynomials of degree at most $p$. Hence their best
uniform approximation errors are exactly equal. Choice of basis can
change projection error, coefficient conditioning, quadrature, and an
implementation's stability, but cannot by itself improve the best
uniform-error exponent attached to that space.

The orthogonality measures differ. In a normalized clock variable
$u\in[-1,1]$, they are $du/\sqrt{1-u^2}$ for Chebyshev and $du$
for Legendre. Pulling a weighted clock projection back to physical time
replaces $w(u)du$ by $w(u(t))\dot u(t)dt$. This is not the same
projection as one using uniform physical time. Weighted $L^2$ accuracy,
especially for a measure that underweights part of the path, does not
by itself prove the original all-time supremum criterion.

A nonconstant polynomial in physical time cannot remain bounded on
$[0,\infty)$, so a single such polynomial cannot uniformly approximate
a genuinely nonconstant convergent response to arbitrary accuracy.
This does not preclude polynomial approximation on a truncated physical
interval with a separately controlled tail, on finite panels, or in a
bounded clock. The latter still requires endpoint regularity if geometric
degree convergence is claimed.

## 6. A positive result: the scalar-residual feature clock

For one training sample, $m=1$, retain the full finite-width analytic
network, all trainable blocks, the same metric, and a nonzero initial
residual. Suppose $K(t)\ge\kappa>0$ along the full trajectory. Put
$\varepsilon=\operatorname{sign}(r(0))$, and define

\[
s(t)=\int_0^t2|r(u)|\,du.
\]

Equation (1), together with preservation of the residual sign, gives
the exact feature equation

\[
\frac{d\theta}{ds}=-\varepsilon D\nabla f(\theta),
\qquad
\frac{d|r|}{ds}=-K(\theta).                        \tag{18}
\]

The residual has cancelled entirely from the parameter equation; this
is stronger than mere finite parameter length. From (18),

\[
0<s_*:=s(\infty)\le |r(0)|/\kappa.
\]

By (4), the path tends to a finite $\theta_\infty$ as $s\uparrow s_*$,
and $f(\theta_\infty)=y$. The right side of (18) is real analytic
in a neighborhood of every reached finite state, including
$\theta_\infty$. It is bounded near that endpoint. Extending the
integral equation continuously to $s_*$, then solving the same locally
Lipschitz ODE from $\theta_\infty$, gives a continuation through $s_*$.
Uniqueness on the overlap identifies it with the original path.

Here the continuation is analytic. To justify the local assertion, complexify
the real analytic vector field in a sufficiently small polydisc about a
reached state. In a smaller closed polydisc its norm and first derivative
are bounded. On a complex time disc of sufficiently small radius, the
integral Picard map sends the closed ball of bounded holomorphic paths
to itself and contracts by the derivative bound times the time radius.
Its successive holomorphic iterates converge uniformly and yield a
holomorphic solution. Uniqueness identifies its real restriction with
the real solution. Finitely many such time discs cover the compact
interval $[0,s_*]$; their solutions agree on overlapping real intervals
and hence on complex overlaps by analytic uniqueness. Shrinking them
if needed supplies a complex neighborhood of the entire interval.

Every finite-panel $h_a^{(\ell)}$, $\delta_a^{(\ell)}$, and fixed
initialized linear image of these fields is analytic in the finite state.
For a fixed finite panel, their compositions with the feature path
therefore have a common complex neighborhood of $[0,s_*]$. This is
an exact finite-width positive statement, including nontraining panel
inputs; it is not a frozen-feature or changed-optimizer argument.

The physical inverse is also exact:

\[
t(s)=\int_0^s\frac{du}{2|f(\theta(u))-y|}.
\]

Near $s_*$, continuity and positivity of $K$ imply
$|r(s)|=\int_s^{s_*}K(\theta(u))du\asymp s_*-s$, so the integral
diverges logarithmically. The analytic feature continuation beyond
fitting is only an approximation-theoretic extension; finite physical
times remain strictly before $s_*$.

For degree estimates, normalize the feature interval to $[-1,1]$.
Choose an ellipse parameter $R>1$ whose closed ellipse lies in the
common complex neighborhood, and let $M$ bound the complex norm of
each required response there. For a Banach-valued response the contour
formula for its Chebyshev coefficients gives
$\|a_j\|\le2MR^{-j}$: substitute $z=(w+w^{-1})/2$ and take the
Laurent coefficient integral on $|w|=R$. Summing the tail gives

\[
\sup_{0\le s\le s_*}\|G(s)-P_p(s)\|
\le \frac{2M R^{-p}}{R-1}.                         \tag{19}
\]

This proves geometric degree convergence at each fixed width. It does
not prove the desired rank exponent because the argument supplies no
width-uniform lower bound on $R-1$, no width-uniform bound on $M$,
and no permissible compressed procedure for obtaining the coefficients
without observing the future target path. The exact clock is causal
in the full network; its use in a compressed autonomous model is a
separate proof obligation.

The same cancellation applies conditionally to a multi-sample trajectory
whose residual remains in a fixed one-dimensional direction,
$r(t)=a(t)v$, with fixed $v\ne0$ and nonzero scalar $a$ of constant
sign. With $\Phi(\theta)=v^\top F(\theta)$ and
$\dot s=2|a|/m$, one has
$d\theta/ds=-\operatorname{sign}(a)D\nabla\Phi(\theta)$.
The required fixed residual direction is a substantive invariant-subspace
condition; it is not implied by positive definiteness of the training Gram.

A second elementary positive case is an exactly linear stable system
whose nonzero decay rates are integer multiples $k_j\lambda_0$ of a
common rate. In the clock $q=e^{-\lambda_0t}$, its state is
$\theta_\infty+\sum_j c_jq^{k_j}v_j$, an exact polynomial. Analytic
observables then extend through $q=0$ locally. This identifies the
spectral mechanism that succeeds in contrast to (14), but establishes
no such commensurability for neural training.

## 7. What remains open for the neural compression target

The proposal has a valid motivation: a clock adapted to finite training
motion can shorten the interval on which one constructs an approximation.
The substantive missing neural implication is a quantitative regularity
estimate for the entire required response panel in one admissible common
clock, uniform to the fitted endpoint and with explicit width dependence.

If such a clock supplied ellipse parameters $R_n>1$, response bounds
$M_n$, and allowed coefficient construction, (19) would require roughly

\[
p\ge
\frac{\log\!\bigl(2M_n/[(R_n-1)\epsilon_n]\bigr)}{\log R_n}
\]

to achieve error $\epsilon_n$. Thus merely proving analyticity at
each finite width is insufficient: a shrinking complex neighborhood can
reintroduce powers of $\log n$, or worse. For example, if
$M_n\le n^C$, $\epsilon_n=n^{-a}$, and
$\log R_n\gtrsim(\log n)^{-b}$, this bound is
$O((\log n)^{b+1})$, with the remaining rank/storage conversion still
to be specified. No precise conversion to the assigned `log(n)^2`
target is asserted without its complete complexity theorem.

The relevant status distinctions are:

| Statement | Status in this route |
|---|---|
| Exact clock equations and finite real path length under (2) | Proved by (1)–(11) |
| Optimal uniform linear-source rank is unchanged by an onto clock | Proved by (17) |
| Chebyshev versus Legendre changes the best degree-$p$ uniform space | False; the spaces coincide |
| Finite motion and positive Gram alone imply common analytic compactification | False for generic analytic gradient systems, by (14)–(16) |
| One-sample neural feature clock has analytic endpoint continuation at fixed width | Proved under the stated analytic activation and positive-Gram hypotheses |
| That continuation has sufficient width-uniform constants and admissible coefficient provenance | Open |
| The generic two-mode example occurs in the assigned Gaussian neural class with the required uniform probability | Not proved or asserted |
| `log(n)^2` neural compression is impossible | Not proved or asserted |

The highest-leverage theoretical check for this route is therefore to identify
the quantitative complex neighborhood, or an alternative approximation class
that handles nonintegral endpoint powers, for the actual reachable neural
response panel. That check must also retain the initialized transpose images
and same-physical-time reconstruction; residual decay by itself does not
control their source approximation errors.

Source snapshots read for this route:

- `docs/notation.qmd`: SHA-256
  `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023`.
- `docs/01-training-geometry.qmd`: SHA-256
  `ea3b9bf0d19ed2c1023f234737b58e9cb83fc641caf2f7e5ee5b249d30618711`.
- `docs/10-correlated-pairs.qmd`: SHA-256
  `375655f8ef4324488af10f2726231310010748de11758af725c182bd375f39d7`.

## Bounded synthesis check, 2026-10-08

After this route was frozen, the supervisor authorized reading these two
complete frozen files; their four stated synthesis claims pass this scoped check.

- `SOURCE_RANK_LEDGER.md`, SHA-256
  `98387ad80255c1452562dc0d0e78b00e9ceca690ecf67024c3bb77c0fc102edd`.
- `ADAPTIVE_APPROXIMATION.md`, SHA-256
  `671fcb7f0e9863d3939eb9b5bbc0fabc3f0a75a14a772ea0fe3615544247a235`.

The oscillatory construction obstructs improved source rank from the generic
strip/tail/speed estimates alone; it is not a neural or arbitrary-encoding no-go.
Sections 2 and 6 above need no inverse-clock runtime state when the clock is used
only offline to construct source spans and is then discarded. Their synchronization
warning applies to a surrogate that actually evolves in a changed clock.
Certified finite-horizon source computation from initialization is permitted by
the frozen interface; it is not a future-trajectory oracle. The conditional fixed
ellipse gives squared-logarithmic storage; the stated sector/panel recipe adds
the squared-loglog factor. The two-mode nonanalyticity example has source rank
at most two, so its common-clock obstruction cannot be read as a rank lower bound.

# Old-clock route: uniform consistency and continuation, with the remaining feedback gap

This is a scoped independent attempt for the existing learning-speed-clock
closure in `paper/main.tex`. Inputs were that manuscript's setting, closure and
old-clock proof, `paper/comparison_appendix.tex`, and `docs/notation.qmd`. No
other study, sibling analysis or previous verdict was used. The mathematical
skill `solve-math-rigorously` was applied. This note changes no manuscript.

**Outcome.** For tanh, arbitrary fixed sample count and finite depth, the old
closure is globally continuable and has an accumulated velocity defect
`O(P^-1)` with width-independent constants having all moments under Gaussian
initialization. Neither closure boundedness nor closure continuation needs to
be assumed. A complete width-uniform trajectory theorem is **not** obtained:
the unproved step is the stability of the nonlinear finite-width flow under
this particular accumulated defect. Ordinary dense-population path regularity
does not supply the required estimate. A concrete Gaussian construction below
shows why uniform Lipschitz or one-sided Lipschitz estimates on a population-
scale tube cannot simply be asserted.

## 1. A complete uniform continuation and consistency lemma

Use exactly the manuscript's canonical mobilities, training data and raw old-
clock ODE, with every activation equal to tanh. Let

\[
 X=\max_a\|x_a\|_2/\sqrt d,
 \qquad Y=(m^{-1}\sum_a y_a^2)^{1/2},
 \qquad K_\ell=\|W^{(\ell)}_0\|_{\rm op}\quad(2\le\ell\le L).
\]

For a fixed physical horizon \(T\), define the following finite constants from
initialization and data alone:

\[
 B=\bigl(\|w_0\|_2^2/n+Y^2T\bigr)^{1/2},
 \quad q=B+Y,\quad S=Tq,\quad A=1+S.
\]

Starting with \(\beta_L=B\), recursively set, downward in layer,

\[
 D_\ell=K_\ell+2A\beta_\ell,
 \qquad \beta_{\ell-1}=D_\ell\beta_\ell
 \quad(\ell=L,L-1,\ldots,2).
\tag{1}
\]

Define upward in layer

\[
 Z_1^*=4SX^4\beta_1^2,
 \qquad
 Z_\ell^*=3\left[4S\beta_\ell^2+
 (D_\ell^2+2A^2\beta_\ell^2)Z_{\ell-1}^*\right]
 \quad(2\le\ell\le L).
\tag{2}
\]

Then for **every finite width and every \(P\ge1\)** the old closure exists
uniquely through \(T\), and on that interval

\[
 \frac{\|\widehat w\|_2}{\sqrt n}\le B,
 \quad \widehat\rho\le q,\quad 1\le\tau\le A,
 \quad \|\widehat W^{(\ell)}\|_{\rm op}\le D_\ell,
 \quad \max_a\frac{\|\widehat\delta_a^{(\ell)}\|_2}{\sqrt n}
 \le\beta_\ell.
\tag{3}
\]

Its physical parameter path satisfies exactly

\[
 \dot{\widehat\theta}=F_n(\widehat\theta)+E,
 \qquad E_1=E_w=0,
\]

and

\[
 \int_0^T\sum_{\ell=2}^L\|E_\ell(t)\|_F\,dt
 \le \frac{C_T}{\sqrt{P(P+1)}},
 \qquad
 C_T=A\sum_{\ell=2}^L\beta_\ell\sqrt{S Z_{\ell-1}^*}.
\tag{4}
\]

The constants in (1)--(4) have no explicit width dependence except the
normalized initial readout and the initialized hidden operator norms. In
particular, these are genuinely uniform constants on any events where those
initial quantities are bounded uniformly.

### Proof of bounds and continuation

The unchanged readout equation gives the exact identity

\[
 \frac{d}{dt}\frac{\|\widehat w\|_2^2}{n}
 =Y^2-\frac4m\sum_a(\widehat f_a-y_a/2)^2\le Y^2.
\]

Since \(|\tanh|\le1\), predictions have absolute value at most
\(\|\widehat w\|_2/\sqrt n\). Hence the first three bounds in (3) hold on
every regular existence interval through time \(T\).

Write \(b_a^{(\ell)}=\widehat r_a\widehat\delta_a^{(\ell)}/\widehat\rho\)
in the clock coordinate, with zero backward prefix, and use the manuscript's
constant forward prefix. At the top layer, \(|\tanh'|\le1\) yields the
backward bound \(\beta_L=B\). Suppose the bound for layer \(\ell\) has been
proved. It implies

\[
 \frac1{mn}\sum_a\|b_a^{(\ell)}(\xi)\|_2^2\le\beta_\ell^2,
 \qquad
 \frac1{mn}\sum_a\int_0^\tau\|b_a^{(\ell)}\|_2^2,d\xi
 \le S\beta_\ell^2.
\]

Every forward history has squared normalized integral at most \(A\).
Projection contraction, the rank-one identity
\(\|uv^T/n\|_{\rm op}=\|u\|_2\|v\|_2/n\), and Cauchy--Schwarz over samples
and history therefore give

\[
 \|\widehat W^{(\ell)}-W_0^{(\ell)}\|_{\rm op}
 \le 2\sqrt{AS}\,\beta_\ell\le2A\beta_\ell.
\]

The backward recursion then proves the bound for layer \(\ell-1\), completing
the downward induction. There is no assumption on the closure path in this
induction. Also,

\[
 \frac{\|\widehat W^{(1)}(t)\|_F}{\sqrt n}
 \le \frac{\|W^{(1)}_0\|_F}{\sqrt n}+2SX\beta_1.
\tag{5}
\]

For each fixed \(n,P\), the moment integral representations now bound every
raw moment on \([0,T]\); the clock denominator is at least one. The raw
vector field is locally Lipschitz, including at \(\rho=0\), since it uses
\(\rho\) and \(r_a\delta_a\), with no division by \(\rho\). All finite state
coordinates remain in a bounded closed subset of its regular domain. If a
maximal endpoint were finite, boundedness of the vector field on this compact
set would give a limiting state, and local existence at that state would
extend the solution. This proves continuation and uniqueness for every
\(P\). At a zero-residual initial state the raw system is stationary; otherwise
local backward uniqueness excludes reaching such an equilibrium at a finite
regular time, justifying use of clock coordinates on compact subintervals.

### Proof of uniform accumulated defect

All following identities are for histories produced by the closure itself.
Let \(D_{h,\ell,a}\) and \(D_{b,\ell,a}\) denote its unnormalized squared
history projection errors. Differentiating moment energies and the
reconstruction, exactly as in the manuscript, gives

\[
 \dot D_h=\rho\|h-h^*\|_2^2,\quad
 \dot D_b=\rho\|b-b^*\|_2^2,
 \quad E_\ell=\frac{2\rho}{nm}\sum_a(b_a-b_a^*)(h_a-h_a^*)^T.
\tag{6}
\]

In particular,

\[
 \int_0^t\|E_\ell\|_F,ds
 \le\frac2{nm}\sum_a\sqrt{D_{b,\ell,a}D_{h,\ell,a}}.
\tag{7}
\]

Define the normalized forward history derivative energy, with the factors
displayed explicitly,

\[
 Z_\ell(t)=\frac1{mn}\sum_a\int_0^{\tau(t)}
       \|(h_a^{(\ell)})'(\xi)\|_2^2,d\xi.
\]

The first-layer clock derivative has normalized norm at most
\(2X^2\beta_1\), so \(Z_1\le Z_1^*\). For subsequent layers,
\(\|F_\ell/\rho\|_F\le2\beta_\ell\). Endpoint evaluation of degree below
\(P\) has norm \(P/\sqrt\tau\). Consequently the sample RMS of the normalized
backward endpoint error is at most \((P+1)\beta_\ell\). Using (6) and the
Legendre tail bound yields

\[
 \int_0^t\rho\|E_\ell/\rho\|_F^2,ds
 \le 2\beta_\ell^2 A^2 Z_{\ell-1}(t).
\tag{8}
\]

For clarity, before the final simplification its right side is
\(\beta_\ell^2A^2(P+1)Z_{\ell-1}/P\), at most the displayed bound for
\(P\ge1\). Thus the endpoint amplification has exactly cancelled the
projection factor, with no width loss.

The chain rule for \(h_a^{(\ell)}=\tanh(\widehat W^{(\ell)}
h_a^{(\ell-1)})\), the operator bound (3), and
\(\|h_a^{(\ell-1)}\|_2/\sqrt n\le1\), give

\[
 Z_\ell\le3\left[4S\beta_\ell^2+
 (D_\ell^2+2A^2\beta_\ell^2)Z_{\ell-1}\right].
\]

Induction proves (2). The backward mass estimate and the forward Legendre
estimate are

\[
 \frac1{mn}\sum_aD_{b,\ell,a}\le S\beta_\ell^2,
 \qquad
 \frac1{mn}\sum_aD_{h,\ell,a}
 \le\frac{A^2Z_{\ell-1}^*}{4P(P+1)}.
\]

Substitution into (7), followed by Cauchy--Schwarz over samples and summation
over links, proves (4).

### Gaussian widths

The preceding result is deterministic. It transfers to Gaussian
initialization without using dense-population convergence. For an initialized
matrix with independent \(N(0,1/n)\) entries, a \(1/4\)-net of the Euclidean
unit sphere with at most \(9^n\) elements gives

\[
 \Pr\{\|W_0\|_{\rm op}>u\}
 \le2\exp(2n\log9-nu^2/8).
\tag{9}
\]

Indeed the operator norm is at most twice the largest bilinear form over
the two nets, and each fixed bilinear form is \(N(0,1/n)\). The union bound
and scalar Gaussian tail prove (9). Thus the finitely many \(K_\ell\) are
uniformly bounded with probability \(1-O(e^{-cn})\), and have every positive
moment bounded uniformly in \(n\). The stored small-readout convention
\(w_{0,i}\sim N(0,1/n^2)\) also gives uniform moments of
\(\|w_0\|_2/\sqrt n\). Recursions (1)--(2) involve only finitely many sums,
products and square roots. Therefore, for every finite \(p\),

\[
 \sup_n\mathbb E C_T^p<\infty.
\]

In particular (4) is an \(L^2\)-in-initialization estimate with a deterministic
width-independent constant. This proves a width-uniform *consistency*
estimate, not a trajectory estimate.

## 2. Exactly what a feedback proof would still have to establish

The natural population-scale parameter distance is

\[
 d_n(\theta,\theta')^2=
 \frac{\|W^{(1)}-W'^{(1)}\|_F^2}{n}
 +\sum_{\ell=2}^L\|W^{(\ell)}-W'^{(\ell)}\|_F^2
 +\frac{\|w-w'\|_2^2}{n}.
\tag{10}
\]

On the operator and readout bounds above, an \(O(P^{-1})\) estimate in (10)
would immediately imply the same rate for predictions uniformly on bounded
input sets, by the forward recurrence in the comparison appendix. Raw
Euclidean first-layer and readout errors carry an additional \(\sqrt n\)
factor; that normalization issue is separate from the feedback issue.

After (4), the desired missing conclusion is an estimate such as

\[
 \sup_{t\le T}d_n(\widehat\theta(t),\theta_n(t))
 \le H_T\int_0^T\sum_{\ell=2}^L\|E_\ell(t)\|_F,dt
\tag{11}
\]

with \(H_T\) independent of width for the actual old-clock defect, or a
different argument proving the same \(P^{-1}\) trajectory rate directly.
Assuming (11), or assuming uniform Lipschitz constants sufficient to prove
it, would assume the missing theorem. It is not a permissible regularity
hypothesis under the assignment.

The derivative term that the operator bounds fail to control is transparent.
Writing \(q_a^{(\ell)}=(W^{(\ell+1)})^T\delta_a^{(\ell+1)}\),

\[
 D\delta_a^{(\ell)}[v]
 =\tanh''(z_a^{(\ell)})\odot q_a^{(\ell)}\odot Dz_a^{(\ell)}[v]
 +\tanh'(z_a^{(\ell)})\odot Dq_a^{(\ell)}[v].
\tag{12}
\]

The first term contains a multiplication operator. In normalized Euclidean
space its norm is the largest coordinate of
\(|\tanh''(z_a^{(\ell)})q_a^{(\ell)}|\), not its RMS. In the population
\(L^2\) space it is the essential supremum of the same quantity. Bounded
operator norms and arbitrary finite moments of dense population fields do
not bound that essential supremum. Temporal smoothness of the dense path
alone does not repair this multiplication estimate.

This observation is an obstruction to this proof route, not a counterexample
to the requested closure theorem: the closure defect has special structure,
and a proof exploiting that structure could still establish (11) or bypass
it.

## 3. A Gaussian example rules out the naive uniform-tube argument

Even for two hidden layers, one sample, \(d=x=y=1\), the vector field need not
have width-uniform Lipschitz or one-sided Lipschitz constants in arbitrarily
small fixed-radius balls in (10) around Gaussian initialization.

Here is an explicit high-probability construction. Keep the hidden matrix
equal to its Gaussian initialization. Replace the first first-layer coordinate
by \(z_*=-1\), leaving all others initialized. Write
\(g_i=\sqrt n\,W_{0,i1}^{(2)}\), and replace the readout by

\[
 w_i=\varepsilon\,\operatorname{sgn}(g_i)
\]

for an arbitrarily small fixed \(\varepsilon>0\). The distance from the
original initialization is \(\varepsilon+o_{\Pr}(1)\); the first-layer
replacement costs only \(O_{\Pr}(n^{-1/2})\). All hidden operator norms remain
bounded with high probability, all readout coordinates are bounded by
\(\varepsilon\), and the forward coordinates are tanh-bounded.

Conditionally on the other first-layer coordinates, write

\[
 z_i^{(2)}=s_i+n^{-1/2}g_i\tanh(z_*),
 \qquad
 s_i\sim N(0,\sigma_n^2),
 \quad \sigma_n^2=n^{-1}\sum_{j\ge2}\tanh^2(W^{(1)}_{0,j}).
\]

The pairs \((s_i,g_i)\) are independent across rows, and each \(s_i\) is
independent of \(g_i\). The variance \(\sigma_n^2\) converges to a positive
constant \(\sigma^2\). Bounded derivatives and elementary laws of large
numbers now give

\[
 \frac{q_1^{(1)}}{\sqrt n}
 =\frac\varepsilon n\sum_i|g_i|\tanh'(z_i^{(2)})
 \longrightarrow
 \varepsilon c,
 \quad
 c=\mathbb E|G|\,\mathbb E\tanh'(\sigma G)>0,
 \qquad f\longrightarrow0.
\tag{13}
\]

For example, replacing \(z_i^{(2)}\) by \(s_i\) changes the first average by
at most \(C\varepsilon n^{-1/2}n^{-1}\sum g_i^2=o_{\Pr}(1)\).
The prediction limit follows from the zero mean of
\(\operatorname{sgn}(g_i)\tanh(s_i)\), with the same replacement bound.

Differentiate the first coordinate of the first-layer velocity while keeping
the readout fixed. Since

\[
 F_{1,1}=-2r\tanh'(z_*)q_1^{(1)},
 \qquad
 \frac{\partial r}{\partial W^{(1)}_1}
 =\frac{\tanh'(z_*)q_1^{(1)}}n,
 \qquad
 \frac{\partial q_1^{(1)}}{\partial W^{(1)}_1}=O_{\Pr}(\varepsilon),
\]

equation (13) implies

\[
 \frac{\partial F_{1,1}}{\partial W^{(1)}_1}
 =2\varepsilon c\tanh''(-1)\sqrt n+o_{\Pr}(\sqrt n).
\tag{14}
\]

The coefficient is positive. In the direction supported on this first-layer
coordinate, both input and output norms in (10) have the same \(n^{-1/2}\)
factor, so (14) is also a lower bound of order \(\sqrt n\) for the local
Lipschitz constant. Its positive quadratic form is a lower bound of the same
order for a one-sided Lipschitz constant. This rules out a width-independent
Gronwall argument on such a tube, even one allowing a very small tube radius.

These are nearby states, not states proved to be reached by dense training or
the closure. Thus the example does **not** rule out stability restricted to
the actual pair of trajectories and the actual moment defect. Its role is to
identify an invalid shortcut, including an attempted gradient-flow
semiconvexity shortcut.

## 4. Other routes examined and their boundary

For one sample at the first layer, set \(u(z)=\int_0^z1/\tanh'(s)\,ds\).
When \(\dot z=-2r\tanh'(z)q\), one has \(\dot u=-2rq\), and the dangerous
derivative of the gate disappears from this scalar equation. This calculation
is exact. It does not produce the requested theorem for arbitrary correlated
samples: a first-layer row then evolves by a sum of
\(r_a\tanh'(z_a)q_a x_a\), with different gates and generally nonorthogonal
inputs. There is no common scalar integrating factor in that calculation.
Even for one sample, at later layers
\(\dot z_\ell=\dot W_\ell h_{\ell-1}+W_\ell\dot h_{\ell-1}\); division by
\(\tanh'(z_\ell)\) leaves the second term with an uncontrolled reciprocal
gate. I did not derive a response-adapted metric closing these terms.

Direct output comparison gives residual dynamics with different evolving
tangent kernels. Controlling their difference returns to derivatives of the
backward responses in (12). A reference-propagator argument would instead
require a uniform bound for the finite-width linearized propagator applied to
the particular defect, plus a nonlinear remainder estimate. Merely assuming
those bounds would again assume the missing feedback theorem.

High finite moments or exponential tails can replace the multiplier bound by
a weaker continuity modulus. For example, a sub-Gaussian dense multiplier
and a bounded gate difference lead by truncation at size \(R\) to a term
of order \(R e+Ce^{-cR^2}\), where \(e\) is the unweighted discrepancy.
Optimizing gives a modulus of order \(e\sqrt{\log(1/e)}\). Its associated
comparison equation amplifies an initial \(P^{-1}\) scale by a factor such
as \(\exp(C_T\sqrt{\log P})\); it does not preserve an exact constant-times-
\(P^{-1}\) estimate. This illustrates why generic moment regularity is not
by itself the requested endpoint result.

## 5. A potentially stronger oracle route, still incomplete

A reference-driven oracle may leave enough approximation slack to avoid
proving an endpoint Lipschitz stability estimate. Place the *dense* histories
in the closure clock, using forward history \(h_d(t(\xi))\) and backward
history \(r_d\delta_d/\widehat\rho\). Their unprojected pairing reproduces the
exact dense learned matrix because \(d\xi=\widehat\rho\,dt\). On a bootstrap
interval with \(\widehat\rho\ge\mu>0\), suitable bounds on the dense first
time derivatives make the forward history \(H^1\), and the backward history
piecewise \(H^1\), with its one prefix jump. The derivative of
\(\widehat\rho\) can be bounded using the already-proved squared defect
bound (8) and the bounded prediction differential; no derivative of the
closure backward response is required for this particular step.

The expected approximation orders are then \(P^{-1}\) for the forward
history and \(P^{-1/2}\) for the backward jump, giving a signed oracle matrix
error of order \(P^{-3/2}\). This is a proposed route, not a theorem here:
the uniform dense derivative/tail bounds and the necessary step-projection
estimate have not been proved in this attempt.

One supporting estimate *can* be proved directly. For every Hilbert-valued
\(H^1\) function on \([0,\tau]\),

\[
 \|\Pi_Pq\|_{L^\infty}
 \le \tau^{-1/2}\|q\|_{L^2}
       +C\tau^{1/2}\|q'\|_{L^2},
\tag{15}
\]

with an absolute constant independent of \(P\). On \([0,1]\), integration
by parts gives, for \(k\ge1\),

\[
 (2k+1)\int q p_k
 =-\tfrac12\int q'(p_{k+1}-p_{k-1}).
\]

In the resulting derivative kernel for \(\Pi_Pq(x)\), the interior
Legendre coefficients are \(p_{j-1}(x)-p_{j+1}(x)\), and there are only
finitely many end coefficients of absolute value at most one. Parseval for
the scalar indicator of \([0,x]\), using

\[
 \int_0^xp_j(s)\,ds
   =\frac{p_{j+1}(x)-p_{j-1}(x)}{2(2j+1)}\quad(j\ge1),
\]

shows that the sum of squared interior coefficients divided by \(2j+1\)
is at most \(4x(1-x)\le1\). Thus the derivative kernel has uniformly bounded
\(L^2\) norm. Hilbert-valued Cauchy--Schwarz proves (15), and rescaling gives
the displayed factors. This supplies a uniform pointwise bound for the
projected closure forward histories by (2).

Why pointwise projection bounds matter: contraction alone bounds differences
of reconstructed products by \((\int\omega(e)^2)^{1/2}\). With the
sub-Gaussian modulus \(\omega(e)=e\sqrt{\log(1/e)}\), squaring that inequality
leads to a logarithmic Osgood modulus and potentially loses a fixed power of
\(P\). By contrast, if the projected oracle backward history also has a
uniform pointwise bound, orthogonality permits the splitting

\[
 \langle\Pi\widehat b,\Pi\widehat h\rangle
 -\langle\Pi b_d,\Pi h_d\rangle
 =\langle\widehat b-b_d,\Pi\widehat h\rangle
  +\langle\Pi b_d,\widehat h-h_d\rangle.
\]

That would give an \(L^1\) Volterra inequality with modulus \(\omega\).
Its subpower amplification \(\exp(C_T\sqrt{\log P})\) can be absorbed by the
extra \(P^{-1/2}\) from the oracle consistency, yielding a constant-times-
\(P^{-1}\) estimate for every fixed \(T\). A uniform partial-projection bound
for a Legendre expansion of a step would handle the prefix jump in this
strategy. More substantially, one must prove the finite Gaussian dense
sub-Gaussian and derivative estimates from the permitted population
regularity, rather than assume uniform finite-network stability or silently
replace a population limit by a finite-width bound. That transfer remains
unproved here.

**Final scope.** This attempt proves a useful uniform theorem about the
actual old-clock closure: boundedness, continuation for every order, and
uniform accumulated defect with Gaussian moment control. It does not prove
the requested width-uniform error theorem. The remaining work is a
noncircular stability estimate that uses the special network-generated
forcing or another mechanism, and then any separate matched dense-width
limit required for a population-prediction conclusion.

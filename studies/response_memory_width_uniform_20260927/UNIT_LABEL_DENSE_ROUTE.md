# A scalar readout invariant removes label smallness for dense GF

Scoped derivation, 28 September 2026. Inputs: the canonical equations and
finite-GF energy argument in `paper/main.tex`, `docs/notation.qmd`, and the
assigned small-label/activity reports. The `solve-math-rigorously` skill was
applied. No other study, experiment, external source, or maintained-file edit
was used. This is an internally derived result, not an independent review.

**Result.** For one nonzero input, every fixed finite depth, tanh, and zero
readout, dense GF preserves a lower bound on its scalar readout-feature Gram
for arbitrary label amplitude. It fits exponentially and has finite total
activity, with constants uniform in width whenever the initial feature norm
and hidden operator norms have uniform bounds. Sufficiently small nonzero
readout gives the same conclusions uniformly over all labels of magnitude at
most one; this includes canonical Gaussian readout. The proof is a normalized
readout identity, not a small-label perturbation argument. General multiple
nonproportional inputs remain unresolved.

## 1. Exact scalar invariant and arbitrary-label theorem

Use one sample `(x,y)`, with `X=||x||_2/sqrt(d)>0`, and arbitrary fixed
`L>=2`. All finite norms are ordinary norms. Let

\[
 B=\frac{\|w\|_2}{\sqrt n},\qquad
 k=\frac{\|h^{(L)}\|_2^2}{n},\qquad
 \lambda_{\rm init}=k(0)>0.
 \tag{1}
\]

The scalar full prediction kernel is

\[
 \Gamma=k+X^2\frac{\|\delta^{(1)}\|_2^2}{n}
 +\sum_{\ell=2}^L
 \frac{\|\delta^{(\ell)}\|_2^2
       \|h^{(\ell-1)}\|_2^2}{n^2}.
 \tag{2}
\]

In particular `Gamma>=k`, and Cauchy--Schwarz gives `f^2<=B^2 k`.
Finite dense GF exists globally: its mobility-metric squared speed has
integral at most its initial loss, so the displacement on any finite time
interval is bounded and has a limit at a finite maximal endpoint; the smooth
finite-dimensional ODE can then be restarted there.

**Theorem 1.** If `w(0)=0`, then for every scalar label `y`,

\[
 k(t)\ge\lambda_{\rm init},\qquad
 \rho(t)=|f(t)-y|\le |y|e^{-2\lambda_{\rm init}t},\qquad
 \int_0^\infty\rho(t)\,dt\le\frac{|y|}{2\lambda_{\rm init}}.
 \tag{3}
\]

The parameters have finite total variation in the mobility norm and converge
to an interpolator. The readout also satisfies

\[
 \sup_t B(t)\le\frac{|y|}{\sqrt{\lambda_{\rm init}}}.
 \tag{4}
\]

**Proof.** The case `y=0` is stationary. Otherwise put
`epsilon=sign(y)` and `g=epsilon f`. The residual equation is exactly
`dot r=-2 Gamma r`, so `r` retains its initial sign on every finite time
interval and `0<=g<|y|`. Use the activity coordinate
`s(t)=integral_0^t rho(u)du`. For finite physical times its derivative is
positive, and the exact equations give

\[
 \frac{dg}{ds}=2\Gamma,\qquad
 \frac{dw}{ds}=2\epsilon h^{(L)},\qquad
 \frac{d B^2}{ds}=4g.
 \tag{5}
\]

Where `B>0`, set `q=g/B`. Substitution of (5) gives

\[
 \frac{dq}{ds}=\frac{2}{B}(\Gamma-q^2)\ge0,
 \qquad q^2\le k\le\Gamma.
 \tag{6}
\]

The initial zero denominator is removable. The feature and output equations
are differentiable at `s=0`, all initial backward responses vanish, and

\[
 w(s)=2\epsilon h^{(L)}(0)s+o(s),\quad
 g(s)=2\lambda_{\rm init}s+o(s),\quad
 B(s)=2\sqrt{\lambda_{\rm init}}s+o(s).
 \tag{7}
\]

Thus `q(0+)=sqrt(lambda_init)`. Equation (6) keeps `q` at least this
value. Moreover `dB/ds=2q>0`, so the interval on which `B>0` cannot
end by `B` returning to zero. This proves `k>=q^2>=lambda_init` for
all positive times; it holds at zero by definition. The exact equation
`dot rho=-2Gamma rho` now proves (3), and `g<|y|` proves (4).
Parameter convergence follows from the quantitative bounds below. No sign
condition on individual neurons, weight matrices, or gates was used.

### Width-independent parameter bounds from the finite activity

More generally, suppose `s(infinity)<=S` and `B(t)<=B_*`. Write
`K_ell=||W^(ell)(0)||_op` for `ell>=2`, and define downward

\[
 \beta_L=B_*,\qquad D_\ell=K_\ell+2S\beta_\ell,
 \qquad \beta_{\ell-1}=D_\ell\beta_\ell
 \quad(\ell=L,\ldots,2).
 \tag{8}
\]

The exact hidden rank-one equations and `|tanh|,|tanh'|<=1` give

\[
 \sup_t\|W^{(\ell)}(t)\|_{\rm op}\le D_\ell,\quad
 \sup_t\frac{\|\delta^{(\ell)}(t)\|_2}{\sqrt n}
       \le\beta_\ell,
 \tag{9}
\]

\[
 \int_0^\infty\left[
  \frac{\|\dot W^{(1)}\|_F}{\sqrt n}
  +\sum_{\ell=2}^L\|\dot W^{(\ell)}\|_F
  +\frac{\|\dot w\|_2}{\sqrt n}\right]dt
 \le 2S\left[X\beta_1+\sum_{\ell=2}^L\beta_\ell+1\right].
 \tag{10}
\]

For example, the hidden velocity has Frobenius norm at most
`2rho beta_ell`; integration bounds its learned operator increment by
`2S beta_ell`, and descending induction then proves (8)--(9). The
first-layer bound uses its actual input factor `X`. The finite-dimensional
parameter spaces are complete, so (10) gives a limiting parameter.
Prediction continuity and (3) show that it interpolates. The same velocity
bound integrated from `t` to infinity gives an exponential parameter tail.
For Theorem 1 take `S=|y|/(2lambda_init)` and
`B_*=|y|/sqrt(lambda_init)`.

## 2. A fixed initial activity interval handles vanishing readout

The ratio in (6) is monotone for any scalar residual sign, but its initial
value for a small random readout need not be positive. The following argument
enters a positive-ratio region using a fixed short activity interval. Label
magnitude is unrestricted during this interval.

Assume `k(0)>=lambda_0>0`, `lambda_0<=1`, and
`max_(ell>=2) ||W^(ell)(0)||_op<=K`, with `K>=1`. Put `R=K+1` and
define positive constants

\[
 A_1=6X^2R^{L-1},\qquad
 A_\ell=RA_{\ell-1}+6R^{L-\ell}\quad(2\le\ell\le L),
 \tag{11}
\]

\[
 s_b=\min\left\{1,\frac{1}{\sqrt{12R^{L-2}}},
                \sqrt{\frac{\lambda_0}{4A_L}}\right\},\qquad
 b_b=\frac{\lambda_0s_b}{2},\qquad
 \kappa=\frac{\lambda_0^2}{36}.
 \tag{12}
\]

**Theorem 2.** If `B(0)<=b_b`, dense GF satisfies for every label `y`

\[
 k(t)\ge\kappa,\qquad
 \rho(t)\le\rho(0)e^{-2\kappa t},\qquad
 \int_0^\infty\rho(t)dt\le\frac{\rho(0)}{2\kappa}.
 \tag{13}
\]

It has finite total parameter variation and converges to an interpolator.
In particular, for all `|y|<=1` the constants are common, since
`rho(0)<=1+b_b`. This includes zero labels.

**Proof.** A fitted initial state is stationary. Otherwise the scalar residual
keeps its initial sign. Define `epsilon=sign(y-f(0))`, `g=epsilon f`, and
use `s=int rho`. Equations (5)--(6) still hold wherever `B>0`.

First stop before `s=s_b` and before any hidden operator exceeds `R`.
The readout equation gives `B<=B(0)+2s<=3s_b`. Therefore

\[
 \frac{\|\delta^{(\ell)}\|_2}{\sqrt n}
       \le3s_bR^{L-\ell},\qquad
 \|W^{(\ell)}-W^{(\ell)}(0)\|_F
       \le6s_b^2R^{L-\ell}\le\frac12\quad(\ell\ge2).
 \tag{14}
\]

The strict operator margin excludes that stopping event. Forward subtraction
and the Lipschitz property of tanh give, inductively,

\[
 \frac{\|h^{(\ell)}(s)-h^{(\ell)}(0)\|_2}{\sqrt n}
       \le A_\ell s_b^2.
 \tag{15}
\]

For the first layer use its increment at most
`6X s_b^2 R^(L-1)` in row RMS, followed by the input factor `X`.
At later layers write the preactivation difference as the current operator
times the preceding feature difference plus the operator increment times the
initial feature; this gives precisely (11). Since both top feature norms
are at most one in RMS,

\[
 |k(s)-k(0)|\le2A_Ls_b^2\le\lambda_0/2.
 \tag{16}
\]

Thus `k>=lambda_0/2` throughout this initial activity interval.
If `s_b` is never attained at a finite physical time, this already gives
the asserted bound for every finite time. Otherwise, at its first attainment,

\[
 g(s_b)\ge g(0)+\lambda_0s_b
       \ge-B(0)+\lambda_0s_b\ge\lambda_0s_b/2,
 \qquad B(s_b)\le3s_b,
 \tag{17}
\]

so `q(s_b)>=lambda_0/6>0`. Equation (6) makes `q` nondecreasing
afterward, and `dB/ds=2q>0` prevents a later zero denominator. Hence
`k>=q^2>=kappa`. Before this time (16) is stronger, since
`lambda_0/2>=lambda_0^2/36`. Integrating the residual equation proves
(13). Apply (8)--(10) with `S=rho(0)/(2kappa)` and
`B_*=B(0)+2S` to obtain convergence. If the directed target
`epsilon y` is nonpositive, (17) simply cannot be reached; the first
case of the argument applies. Consequently no assumption `y!=0` or
`sign(y-f(0))=sign(y)` was used.

## 3. Canonical Gaussian consequence

For a fixed nonzero scalar training input vector `x`, set

\[
 q_1=\mathbb E\tanh^2(XZ),\qquad
 q_\ell=\mathbb E\tanh^2(\sqrt{q_{\ell-1}}Z),
 \quad Z\sim N(0,1).
 \tag{18}
\]

Every `q_ell` is positive. The first-layer law of large numbers and,
conditionally at each subsequent layer, independent Gaussian rows and
boundedness of tanh imply `k(0)->q_L` in probability. More explicitly,
conditional averaging has variance at most `1/n`, and its mean is the
continuous function in (18) of the preceding feature mean square. Induction
proves the assertion.

One may take the common hidden operator bound `K=10` on an event whose
probability tends to one. Indeed a quarter-net of the unit sphere has at most
`9^n` points; two such nets give
`||W||_op<=2 max_(u,v in nets)|u^T Wv|`, and each displayed bilinear
form has law `N(0,1/n)`. Thus

\[
 \Pr\{\|W\|_{\rm op}>10\}
 \le2\exp\{2n\log9-100n/8\}\longrightarrow0.
 \tag{19}
\]

A union bound covers fixed depth. For canonical stored readout
`w_i(0)~N(0,n^-2)`, `nB(0)->1` in probability by the law of large
numbers for the squared Gaussian entries. Take `lambda_0=q_L/2` and
the constants (11)--(12). Their values are independent of width. The joint
event `k(0)>=lambda_0`, all hidden operator norms at most ten, and
`B(0)<=b_b` therefore has probability tending to one.

On this event Theorem 2 holds simultaneously for every `|y|<=1`, at every
physical time, with common constants. With exactly zero readout, Theorem 1
gives the sharper exponent and activity bound. This is an all-time
finite-width dense-GF statement. The identities also hold on any regular
strong population flow with the stated Hilbert gradient structure, but this
note does not construct the general-depth global population flow or prove
autonomous memory tracking.

## 4. Exact boundary for multiple inputs

For `m>1` use sample RMS pairing `<u,v>_m=u^T v/m`, `B=||w||/sqrt(n)`,
and, where `B>0`, the vector `Q=f/B`. Let `Gamma` be the canonical
sample kernel including the factor `1/m`. Cauchy--Schwarz in readout space
gives the matrix inequality

\[
 \Gamma\succeq\Gamma_w\succeq\frac{QQ^T}{m}.
 \tag{20}
\]

The exact equations imply

\[
 \dot B=-2\langle r,Q\rangle_m,\qquad
 \dot Q=-\frac2B\left(\Gamma-\frac{QQ^T}{m}\right)r.
 \tag{21}
\]

The matrix in parentheses is positive semidefinite, but the derivative of
`||Q||_m^2` has sign determined by its bilinear pairing between `Q` and
`r`; that sign is unrestricted. Thus (6) is genuinely scalar. Even a lower
bound on `||Q||_m` would not bound the kernel in residual directions
orthogonal to `Q`. For example the abstract identities allow
`y=(1,0)`, `f=Q=(1/2,1/2)`, `B=1`, and `Gamma=QQ^T/2`; then
`r=(-1/2,1/2)` is nonzero but `Gamma r=0`. This is an obstruction to an
inference from (20)--(21), not a claimed reachable Gaussian tanh state.

A fixed-readout regret calculation has a related limitation. If `v` is any
fixed readout and `f_v(t)=H_L(t)^T v/n`, its exact identity is

\[
 \int_0^T\rho^2dt
 =\frac{\|w(0)-v\|_2^2-\|w(T)-v\|_2^2}{4n}
  +\int_0^T\langle r,f_v-y\rangle_mdt.
 \tag{22}
\]

Fitting the labels with the initial features does not bound the last term
under trained feature motion. Even eliminating that term would bound
`integral rho^2`, not the required `integral rho`.

The precise dense activity obligation can be weaker than a uniform kernel
gap. Where `rho>0`, put

\[
 \gamma_r(t)=\frac{\langle r,\Gamma r\rangle_m}{\rho^2}.
 \qquad \frac{d\rho}{ds}=-2\gamma_r.
 \tag{23}
\]

An a priori lower bound `gamma_r(s)>=a(s)>=0` on every activity-stopped
interval, with `2 integral_0^S a(s)ds>rho(0)` for a finite `S`, would
exclude attainment of `S` and supply finite dense activity for arbitrary
labels. The scalar invariant proves this with a positive constant. No such
nonperturbative bound is proved here for multiple nonproportional inputs.
In addition, transferring dense finite activity to width-uniform all-time
autonomous tracking requires stability of the actual closure and a regular
terminal fitting neighborhood. Increasing memory order does not establish
either missing property of the unchanged dense flow.

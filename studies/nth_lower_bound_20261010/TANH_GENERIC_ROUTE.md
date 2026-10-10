# Gaussian reverse carriers and the analytic route for fixed-top NTH

This scoped route studies the stated two-hidden-layer tanh network at its
Gaussian initialization. It proves a width-dependent obstruction to a
bounded-coordinate analytic proof of NTH convergence, and an exact polynomial
description of every initialized NTH tensor after conditioning on initialized
features. It does **not** establish a growing-order NTH accuracy or storage
theorem. In particular, a large coordinate derivative or a growing tensor
coefficient is not itself a lower bound for the prediction error.

Inputs used: the supervisor's assignment, `docs/notation.qmd`, and the complete
setup, public source proposition, dense-variability section, and initialized-jet
compiler passage of `docs/08b-trajectory-compression.qmd`. No other study,
another route's report, external source, or experiment was used. The source
proposition and compiler are used below only to identify what their conclusions
do and do not imply; their small-label assumptions are not imported into the
new initialization calculation.

## Setup and exact source directions

Let $v_a\in\mathbb R^d$, $\|v_a\|_2=1$, $1\le a\le m$, be fixed
training inputs, and let $y\in\mathbb R^m\setminus\{0\}$ be fixed labels.
There are two hidden layers of width $n$:

\[
z_a^{(1)}=W^{(1)}v_a,\qquad h_a^{(1)}=\tanh z_a^{(1)},\qquad
z_a^{(2)}=W^{(2)}h_a^{(1)},\qquad h_a^{(2)}=\tanh z_a^{(2)},\qquad
f_a=\frac{u^\top h_a^{(2)}}n.
\]

The shapes are $W^{(1)}\in\mathbb R^{n\times d}$,
$W^{(2)}\in\mathbb R^{n\times n}$, and $u\in\mathbb R^n$.
The initialization has independent $W^{(1)}_{ij}\sim N(0,1)$,
$W^{(2)}_{ij}\sim N(0,1/n)$, and $u=0$. The mobility matrix $M$ acts
as multiplication by $n,1,n$ on these three parameter blocks.

Put

\[
F_y(\theta)=\frac1m\sum_a y_af_a(\theta),\qquad
V_a=M\nabla f_a,\qquad V_y=M\nabla F_y=\frac1m\sum_a y_aV_a.
\]

Here $V_a g=Dg[V_a]$ denotes a directional derivative of a scalar function
$g$. The auxiliary source flow is $d\theta/ds=V_y(\theta)$. It is used
to analyze initialization derivatives, not as a replacement optimizer.
Physical training uses

\[
\mathcal L=\frac1{2m}\sum_a(f_a-y_a)^2,\qquad
\dot\theta=-\frac1m\sum_a(f_a-y_a)V_a.
\]

Their initial velocities agree. Their first-hidden-feature second derivatives
also agree, as shown below.

The first-layer population feature Gram is

\[
Q^{(1)}_{ab}=\mathbb E[\tanh(X_a)\tanh(X_b)],\qquad
(X_1,\ldots,X_m)\sim N(0,G),\qquad G_{ab}=v_a^\top v_b.
\]

For the nondegeneracy result assume $Q^{(1)}\succ0$. The input Gram $G$
may be correlated or singular. For tanh and unit inputs this assumption is
equivalent to requiring that no two inputs are equal up to sign. In particular,
it follows from a positive final population feature Gram: equal or opposite
inputs give equal or opposite features at every layer of this bias-free odd
network. No label bound is imposed and nothing shrinks with $n$.

Here is a direct proof of the stated equivalence. If a vector $c$ is in the
nullspace of $Q^{(1)}$, continuity and the full support of the first Gaussian
weight row imply
$\sum_a c_a\tanh(w^\top v_a)=0$ for every $w\in\mathbb R^d$.
When no inputs agree up to sign, choose $\xi$ outside the finitely many
hyperplanes on which $\xi^\top v_a=0$ or
$|\xi^\top v_a|=|\xi^\top v_b|$. Restrict to $w=t\xi$, absorb the
signs into the coefficients, and order the distinct positive slopes as
$0<\alpha_1<\cdots<\alpha_m$. The resulting identity is
$\sum_a d_a\tanh(\alpha_at)=0$. Its limit at infinity gives
$\sum_a d_a=0$; subtract this constant and use
$\tanh(\alpha t)-1=-2e^{-2\alpha t}(1+o(1))$. Dividing by
$e^{-2\alpha_1t}$ gives $d_1=0$, and iteration gives all $d_a=0$.
The converse is immediate for equal or opposite inputs.

## Exact conditional Gaussian decomposition

All matrices in this paragraph are evaluated at initialization. Set

\[
H=(h_1^{(1)},\ldots,h_m^{(1)})\in\mathbb R^{n\times m},\qquad
Z=W^{(2)}H\in\mathbb R^{n\times m},\qquad Q_n=H^\top H/n.
\]

With probability tending to one, $H$ has full column rank. Conditional on
$W^{(1)}$ and $Z$, the exact Gaussian regression formula is

\[
W^{(2)}=Z(H^\top H)^{-1}H^\top+\Xi(I-P),\qquad
P=H(H^\top H)^{-1}H^\top,
\]

where $\Xi$ has independent $N(0,1/n)$ entries and is independent of the
conditioning variables. This follows row by row by orthogonally projecting
an isotropic Gaussian row onto the column space of $H$. A pseudoinverse
gives the analogous identity without the full-rank event.

Define the initialized readout source and $m$ reverse-source columns by

\[
b_i=\frac1m\sum_a y_a\tanh Z_{ia},\qquad
C_{ia}=b_i\operatorname{sech}^2 Z_{ia},\qquad
C\in\mathbb R^{n\times m}.
\]

The initialized reverse carriers are the columns of

\[
W^{(2)\top}C
=H Q_n^{-1}\frac{Z^\top C}{n}+(I-P)U,
\qquad U=\Xi^\top C.
\tag{1}
\]

Conditional on $W^{(1)},Z$, the rows $U_j\in\mathbb R^m$ are
independent centered Gaussians with covariance

\[
\Sigma_n=C^\top C/n.
\tag{2}
\]

The laws of large numbers needed here are elementary. The rows of $H$
are i.i.d. bounded vectors, so $Q_n\to Q^{(1)}$. Conditional on $H$,
the rows of $Z$ are i.i.d. $N(0,Q_n)$. The functions defining $C$ are
bounded and continuous. Conditional variances are $O(n^{-1})$, and
continuous Gaussian covariance square roots therefore give

\[
\Sigma_n\ \xrightarrow{\mathbb P}\ \Sigma,
\qquad
\Sigma_{ab}=\mathbb E\left[
b(Z)^2\operatorname{sech}^2Z_a\operatorname{sech}^2Z_b\right],
\quad Z\sim N(0,Q^{(1)}),
\tag{3}
\]

where $b(z)=m^{-1}\sum_a y_a\tanh z_a$. The same argument, using bounded
Gaussian second moments, shows that $Z^\top C/n$ converges in probability
to a finite matrix.

In fact $\Sigma\succ0$. If $c^\top\Sigma c=0$, the real-analytic
function

\[
b(z)\sum_a c_a\operatorname{sech}^2z_a
\]

vanishes almost everywhere under a Gaussian density positive on all of
$\mathbb R^m$, hence everywhere by continuity. The function $b$ is
nonzero because $y\ne0$. On an open set where $b\ne0$, the second
factor vanishes, and real-analytic continuation makes it vanish everywhere.
Differentiating with respect to $z_a$ then forces $c_a=0$ for each $a$.

The projection correction in (1) is uniformly negligible:

\[
\max_j\|(PU)_j\|_2=O_{\mathbb P}(n^{-1/2}).
\tag{4}
\]

Indeed, let $A=(H^\top H)^{-1}H^\top U$. Conditional on $H,Z$,

\[
\mathbb E[\|A\|_F^2\mid H,Z]
=\operatorname{tr}((H^\top H)^{-1})\operatorname{tr}\Sigma_n
=O(n^{-1})
\]

on events where $Q_n^{-1}$ is bounded. Every row of $H$ has norm at
most $\sqrt m$, so $PU=HA$ proves (4). The conditional mean in (1)
is uniformly $O_{\mathbb P}(1)$, by the same row bound and the convergence
of $Q_n^{-1}$ and $Z^\top C/n$.

## A proved obstruction to a uniform bounded-coordinate analytic disk

**Proposition.** Under the preceding fixed-data assumptions, choose any
training index $a$ with $y_a\ne0$. There are constants $c,C>0$,
depending on the fixed inputs and labels but not on $n$, such that

\[
\Pr\left\{
c\sqrt{\log n}\le
\max_{1\le j\le n}\left|
\frac{d^2}{ds^2}h_{a,j}^{(1)}(0)\right|
\le C\sqrt{\log n}\right\}\longrightarrow1.
\tag{5}
\]

The same statement holds with physical training time $t$ in place of the
source time $s$.

**Proof.** At initialization the hidden-layer velocities vanish, while
$u'=b$. Differentiating the exact first-layer source equation therefore gives

\[
\frac{d^2W^{(1)}}{ds^2}(0)
=\frac1m\sum_b y_b\left[
\operatorname{sech}^2(z_b^{(1)})\odot
W^{(2)\top}(b\odot\operatorname{sech}^2Z_b)
\right]v_b^\top.
\]

Consequently, with $X_{ja}=z_{a,j}^{(1)}(0)$,

\[
\frac{d^2 h_{a,j}^{(1)}}{ds^2}(0)
=\sum_b \ell_{j,b}(W^{(2)\top}C)_{jb},
\qquad
\ell_{j,b}=\frac{y_b}{m}
\operatorname{sech}^2X_{ja}\operatorname{sech}^2X_{jb}G_{ab}.
\tag{6}
\]

These coefficients are uniformly bounded. Choose a fixed $R<\infty$
such that the event $\max_b|X_b|\le R$ has probability $p>0$.
An ordinary law of large numbers gives at least $pn/2$ such rows with
probability tending to one. On those rows,

\[
\|\ell_j\|_2\ge|\ell_{j,a}|
\ge\frac{|y_a|}{m}\operatorname{sech}^4R>0,
\]

because $G_{aa}=1$. Combining (1)--(4), the quantities in (6) equal

\[
\mu_j+\ell_j^\top U_j+e_j,
\qquad
\max_j|\mu_j|=O_{\mathbb P}(1),\qquad
\max_j|e_j|=O_{\mathbb P}(n^{-1/2}).
\tag{7}
\]

Conditional on $H,Z$, the middle terms are independent Gaussian variables.
Their variances are bounded above uniformly. On at least $pn/2$ rows
their variances are bounded below by a positive constant, by (3) and the
lower bound on $\|\ell_j\|_2$.

The upper bound in (5) follows by a Gaussian union bound. For the lower
bound, a centered Gaussian maximizes the probability of a symmetric interval
among all translates of the same Gaussian. For $cn$ independent Gaussians
with variances at least $\sigma^2>0$, the probability all their absolute
values are at most $\sigma\sqrt{\log n}$ is at most

\[
\left(1-2\Pr\{N(0,1)>\sqrt{\log n}\}\right)^{cn}
\longrightarrow0.
\]

For completeness, the Gaussian tail is bounded below by integrating its
density on $[x,x+1/x]$; at $x=\sqrt{\log n}$ this is a constant times
$n^{-1/2}/\sqrt{\log n}$. The negligible errors in (7) do not affect the
conclusion.

For physical training, differentiating its first-layer velocity gives the
same expression: terms differentiating the residual multiply the initially
zero backward signal; terms differentiating $W^{(2)}$ or hidden activations
also vanish initially. Only $u'(0)=b$ remains. This proves the last claim.

**Analytic consequence.** Fix a constant $M>0$. Suppose all first-layer
feature coordinates extend holomorphically to $|s|<R_n$, with modulus at
most $M$ there. Cauchy's estimate gives

\[
\max_j |h_{a,j}^{(1)\prime\prime}(0)|\le\frac{2M}{R_n^2}.
\]

On an event of probability tending to one, (5) consequently forces

\[
R_n\le C_M(\log n)^{-1/4}.
\tag{8}
\]

Thus an analytic convergence proof that requires a common complex disk of
fixed radius and a fixed coordinatewise source bound cannot work in this
model. This is a proof-route obstruction, not a prediction-error theorem.
It also does not contradict the maintained chapter's source proposition:
that proposition supplies shrinking domains and permits coordinate bounds
that grow with $n$.

## Exact initialized-tensor polynomial structure

Define the metric NTH tensors by

\[
K^{(2)}_{ab}=Df_a[V_b],\qquad
K^{(r+1)}_{a_1\ldots a_{r+1}}
=D K^{(r)}_{a_1\ldots a_r}[V_{a_{r+1}}].
\]

All differentiation here is done in the original network before any
conditioning. Once the resulting expression is evaluated at initialization,
conditioning on $W^{(1)},Z$ yields the following exact facts.

1. Every odd initialized tensor is zero.
2. Each entry of $K^{(2k+2)}(0)$ is a polynomial in the unused Gaussian
   matrix $\Xi(I-P)$, of degree at most $2k$.
3. The homogeneous degree-$2k$ part arises entirely from first-layer
   parameter contractions and the locally affine part of the first activation.

To verify these facts, expand the repeated directional derivatives into
contractions of derivatives of the outputs. An entry of $K^{(r)}$ is a sum
of tree contractions with $r$ output factors and $r-1$ parameter edges.
This description follows inductively: applying another $V_a$ differentiates
one output derivative factor and attaches one new output factor by a metric
edge. The metric is constant, so no derivative of the metric occurs.

Each output is linear in $u$. At $u=0$, every surviving output factor
must therefore receive exactly one $u$-derivative: zero such derivatives
leave a factor of $u$, and two such derivatives annihilate the factor.
The readout edges form a perfect matching of the $r$ vertices. Hence $r$
must be even. When $r=2k+2$, exactly $k+1$ edges are readout edges and
exactly $k$ are hidden-parameter edges.

An endpoint differentiation in a first-layer parameter can contribute at
most one factor of $W^{(2)}$. A second-layer differentiation contributes
no additional such factor. There are at most $2k$ first-layer endpoints,
so the conditional degree is at most $2k$. Degree $2k$ requires all
hidden edges to be first-layer edges, and each first-layer derivative to hit
a separate outer-preactivation factor. Higher derivatives of the first
activation combine several first-layer derivatives into one $W^{(2)}$
factor and thus lower the degree. This proves all three assertions.

This structure validates a conditional Wiener-chaos approach, but does not
supply the needed lower bound. Polynomial degree alone cannot bound a chaos
norm from below: coefficient sizes, $n$-dependent contractions, and
cancellation between tree terms must all be controlled. In particular, the
highest Gaussian degree does not isolate first-layer tanh curvature.

## Why averaging is a genuine remaining issue

Unbounded Gaussian carriers and shrinking coordinatewise analytic domains do
not imply nonanalyticity after averaging. A direct counterexample to that
inference is

\[
A(s)=\mathbb E[\tanh^2(X+sG)],\qquad X,G\ \text{independent }N(0,1).
\]

For real $s$, $X+sG\sim N(0,1+s^2)$. Therefore $A$ has the holomorphic
continuation near zero

\[
A(s)=\frac1{\sqrt{2\pi(1+s^2)}}
\int_{\mathbb R}\tanh^2x\,
\exp\!\left(-\frac{x^2}{2(1+s^2)}\right)dx.
\tag{9}
\]

For $|s|<1/2$, use the square-root branch equal to one at zero; the real
part of $1/(1+s^2)$ is uniformly positive on compact subsets, so a Gaussian
integrable majorant proves holomorphy by differentiation under the integral.
Yet individual random integrands $s\mapsto\tanh^2(X+sG)$ can have poles
arbitrarily close to zero as $|G|$ grows. Formula (9) is an illustration of
the logical issue, not a replacement neural model or an NTH theorem.

## Exact unresolved bridge to accuracy and storage

For the fixed-top hierarchy, the initial tensors are contracted against
ordered integrals of its own residual. The public source proposition concerns
physical-time holomorphy along the dense solution. The initialized-jet compiler
uses an analytic coordinate change to continue beyond the original Taylor
disk. Neither conclusion is a bound on the fixed-top NTH's word series or its
own-residual feedback.

To turn the conditional polynomial structure into a dense-variability lower
bound, a proof still needs all of the following, with constants controlled for
growing order:

- A specified nonzero conditional chaos projection of the **prediction
  error**, or a tensor projection together with a valid quantitative transfer
  to that error. A high-order initialization derivative alone is insufficient.
- Its size uniformly in the relevant joint range of $q,n$, including all
  same-degree tree contractions and the rank-$m$ conditioning correction.
- Protection against cancellation between different hierarchy levels that
  contribute to the same chaos degree at a fixed positive time.
- A lower-tail estimate adequate for the promised probability, and control
  of the surrogate's own-residual evolution.

A second-moment lower bound alone does not give a fixed-confidence lower
bound; a fourth-moment or small-ball argument is also required, and its
constants may deteriorate with $q$. Conversely, a conditional upper bound
on initialized tensors alone does not bound the exact remainder along a
controlled path.

**Current conclusion.** Equation (5), its analytic consequence (8), and the
conditional polynomial structure are proved for fixed arbitrary nonzero
labels and general correlated inputs with $Q^{(1)}\succ0$. They rule out
one tempting width-uniform coordinatewise analytic proof and make the
conditional Gaussian degrees precise. They establish neither failure nor
success of fixed-top NTH at order growing with $n$, and hence do not justify
an accuracy-dependent NTH storage exponent.

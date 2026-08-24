# Archived proof attempt: an autonomous source at every fixed linear depth

Status: superseded by `CANONICAL_NOTE.md` after the 20 August 2026
supervisory audit.

> **Audit correction.**  The finite-width identities and the internal
> deterministic path ODE are rigorous.  The compact-positive-time
> finite-width identification asserted below is rigorous for `L=1,2`, but
> remains conditional for `L>=3`.  Section 8 sketches rather than proves the
> required multi-edge Wick and coefficient-lift lemmas.  This file is kept as
> a proof-attempt record and is not the authoritative claim statement.

## 1. Model and result

Let `L >= 1` be the number of trainable hidden layers.  Put

\[
 q=L-1.
\]

After projecting the first-layer weights onto the single unit-normalized
sample, the width-`n` identity network is

\[
 f_{n,L}=n^{-(L+1)/2}v_L^T W_q\cdots W_1v_0.                 \tag{1.1}
\]

The matrix product is empty for `L=1`.  All entries of the vectors and
matrices at time zero are mutually independent `N(0,1)`, and all raw
parameters obey the full-MSE muP flow

\[
 \dot\Theta=-\eta n\nabla_\Theta (y_\star-f_{n,L})^2,
 \qquad \eta>0.                                             \tag{1.2}
\]

There is, for every fixed `L`, a deterministic and autonomous candidate
infinite-width description with one fixed rooted-path source operator.  It has an `O(1)`
list of state objects: two Hilbert vectors, one Hilbert--Schmidt block
operator, and one scalar residual.  Its size is independent of width and of
the number of loss derivatives requested.  The graded source depends on
`L`; evaluation is not claimed to have cost independent of depth.

The closure is most compactly stated after constructing its source.

## 2. The one rooted-path source

Consider the layer chain

\[
 0--1--\cdots--q.
\]

There are two colored roots: `a` at layer `0` and `b` at layer `q`.  A rooted
path ending at layer `j` is

\[
 s=(\sigma;s_0,s_1,\ldots,s_r),\qquad
 \sigma\in\{a,b\},\quad s_0=0\ \hbox{if }\sigma=a,
 \quad s_0=q\ \hbox{if }\sigma=b,
\]

with `s_r=j` and `|s_k-s_(k-1)|=1`.  The colors keep the two length-zero
roots distinct even when `q=0`.  Let

\[
 \mathcal S_q(j)=\{\hbox{finite rooted paths ending at }j\},\qquad
 \mathcal H_j=\ell^2(\mathcal S_q(j)),\qquad
 \mathcal H=\bigoplus_{j=0}^q\mathcal H_j.                  \tag{2.1}
\]

Write `e_s` for a path basis vector, `s star j` for appending the vertex `j`,
and `s^-` for deleting the final vertex.  For `1 <= j <= q`, define

\[
 \Lambda_j e_s
 =e_{s\star j}
  +\mathbf 1_{\{r\ge1,\ s_{r-1}=j\}}e_{s^-},
 \qquad s\in\mathcal S_q(j-1).                             \tag{2.2}
\]

Thus multiplication by a fresh Gaussian edge creates one longer Wick word;
if the last step used the transpose of the same edge, it also annihilates
that last step.  Creation and annihilation are partial isometries, so

\[
 \|\Lambda_j\|\le2.                                        \tag{2.3}
\]

Let `iota_j` be the inclusion of `H_j` into `H` and set

\[
 \boxed{\displaystyle
 \Lambda^{(L)}=\sum_{j=1}^q
 \iota_j\Lambda_j\iota_{j-1}^*.}                           \tag{2.4}
\]

This single bounded, forward, depth-graded operator is the entire
initialization source.  Put

\[
 \alpha=e_{(a;0)}\in\mathcal H_0,
 \qquad \beta=e_{(b;q)}\in\mathcal H_q.                    \tag{2.5}
\]

For `q=0`, the sum (2.4) is empty, `H_0` contains the two orthogonal colored
roots, and all formulas below remain valid with zero operator powers
interpreted as the identity.

## 3. The autonomous operator ODE

Let

\[
 \mathfrak G_L=\bigoplus_{j=1}^q
 \operatorname{HS}(\mathcal H_{j-1},\mathcal H_j)           \tag{3.1}
\]

be the forward-block Hilbert--Schmidt space.  The state is

\[
 A(t)\in\mathcal H_0,\quad B(t)\in\mathcal H_q,\quad
 G(t)\in\mathfrak G_L,\quad e(t)\in\mathbb R,              \tag{3.2}
\]

and

\[
 M(t)=\Lambda^{(L)}+G(t).                                   \tag{3.3}
\]

Define the forward and backward features

\[
 p_j=M^jA\in\mathcal H_j,qquad
 z_j=(M^*)^{q-j}B\in\mathcal H_j,qquad 0\le j\le q,        \tag{3.4}
\]

and the scalar feature kernel

\[
 \boxed{\displaystyle
 K=\|z_0\|^2+\|p_q\|^2+
 \sum_{j=1}^q\|z_j\|^2\|p_{j-1}\|^2.}                    \tag{3.5}
\]

For vectors `u,v`, `u tensor v` denotes the rank-one operator
`x -> u <v,x>`.  With `c=2 eta`, the physical full-MSE closure is

\[
 \boxed{
 \begin{aligned}
 \dot A&=ce\,z_0,\\
 \dot B&=ce\,p_q,\\
 \dot G&=ce\sum_{j=1}^q z_j\otimes p_{j-1},\\
 \dot e&=-ceK,
 \end{aligned}}                                             \tag{3.6}
\]

initialized by

\[
 A(0)=\alpha,\qquad B(0)=\beta,\qquad G(0)=0,
 \qquad e(0)=y_\star.                                      \tag{3.7}
\]

The output and loss are the immediate readouts

\[
 \boxed{
 f(t)=\langle B,M^qA\rangle=y_\star-e(t),
 \qquad \mathcal L(t)=e(t)^2.}                             \tag{3.8}
\]

For the half-MSE convention, replace `c=2 eta` by `c=eta`.

### Coordinate IDE form

Equation (3.6) is an operator ODE and simultaneously an
integro-differential equation on one fixed countable source.  With counting
measure on the path sets, write

\[
 M_j(s,s')=\Lambda_j(s,s')+G_j(s,s').
\]

Then

\[
 \begin{aligned}
 p_j(s)&=\int_{\mathcal S_q(j-1)}M_j(s,s')p_{j-1}(s')\,d\#(s'),\\
 z_{j-1}(s')&=\int_{\mathcal S_q(j)}M_j(s,s')z_j(s)\,d\#(s),\\
 \partial_tG_j(s,s')&=ce\,z_j(s)p_{j-1}(s').               \tag{3.9}
 \end{aligned}
\]

Together with the endpoint and residual equations in (3.6), these sums are
a single-source autonomous IDE.  No trajectory history is stored.

## 4. Proved internal theorem and conditional width theorem

**Internal theorem.**  Fix `L`, `eta > 0`, and `y_star in R`.  Equations
(3.3)--(3.7) have a unique global solution and satisfy (4.2)--(4.3).

**Conditional width theorem.**  Assume the multi-edge rooted-word and
coefficient-lift lemmas isolated in the authoritative `CANONICAL_NOTE.md`.
For every finite `T`, if
`f_(n,L)`, `K_(n,L)`, and `loss_(n,L)` are generated by (1.1)--(1.2), then

\[
 \sup_{0\le t\le T}
 \left(
 |f_{n,L}(t)-f(t)|+|K_{n,L}(t)-K(t)|
 +|(y_\star-f_{n,L}(t))^2-e(t)^2|
 \right)\xrightarrow[n\to\infty]{\mathbb P}0.              \tag{4.1}
\]

At initialization,

\[
 f(0)=0,\qquad K(0)=L+1.                                   \tag{4.2}
\]

If `y_star != 0`, `e` preserves its sign, `f` moves monotonically from zero
towards `y_star`, and there are trajectory-dependent constants `C,gamma>0`
such that

\[
 |e(t)|\le Ce^{-\gamma t},\qquad
 \mathcal L(t)\le C^2e^{-2\gamma t}.                        \tag{4.3}
\]

When `y_star=0`, the deterministic path state is stationary and already has
zero loss.  Statement (4.1) is unconditional for `L=1,2`; at `L>=3` it has
the conditional status just stated.  Equation (4.3) is an unconditional
long-time assertion about the deterministic path equation itself.

## 5. Exact finite-width normalization and kernel

Set

\[
 a_n=v_0/\sqrt n,\qquad b_n=v_L/\sqrt n,
 \qquad M_{j,n}=W_j/\sqrt n.                                \tag{5.1}
\]

Then

\[
 f_{n,L}=\langle b_n,M_{q,n}\cdots M_{1,n}a_n\rangle.       \tag{5.2}
\]

Let

\[
 p_{0,n}=a_n,\quad p_{j,n}=M_{j,n}p_{j-1,n},\qquad
 z_{q,n}=b_n,\quad z_{j-1,n}=M_{j,n}^Tz_{j,n}.              \tag{5.3}
\]

Since differentiation with respect to a raw block contributes a factor
`n^(-1/2)` relative to its normalized block, (1.2) is exactly

\[
 \dot a_n=ce_nz_{0,n},\quad
 \dot b_n=ce_np_{q,n},\quad
 \dot M_{j,n}=ce_nz_{j,n}p_{j-1,n}^T,                       \tag{5.4}
\]

where `e_n=y_star-f_(n,L)`.  Hence

\[
 \begin{aligned}
 K_{n,L}=n\|\nabla_{\rm raw} f_{n,L}\|^2
 &=\|z_{0,n}\|^2+\|p_{q,n}\|^2\\
 &\quad+\sum_{j=1}^q\|z_{j,n}\|^2\|p_{j-1,n}\|^2,        \tag{5.5}\\
 \dot f_{n,L}&=ce_nK_{n,L},\qquad
 \dot e_n=-ce_nK_{n,L}.                                    \tag{5.6}
 \end{aligned}
\]

Thus (3.5)--(3.6) are not guessed loss equations: they are the exact
normalized finite-width gradient algebra with the Gaussian initialization
replaced by its deterministic path source.

## 6. Internal proof: derivative identity and well-posedness

The differential of

\[
 f(A,B,G)=\langle B,M^qA\rangle                            \tag{6.1}
\]

is

\[
 \nabla_Af=z_0,\qquad \nabla_Bf=p_q,qquad
 \nabla_{G_j}f=z_j\otimes p_{j-1}.                          \tag{6.2}
\]

Different `j` blocks are orthogonal in Hilbert--Schmidt norm.  Equations
(3.5) and (6.2) therefore give

\[
 K=\|\nabla f\|^2,qquad \dot f=ceK.                        \tag{6.3}
\]

Consequently `f+e` is constant.  Its initial value is `y_star`, proving
(3.8), and

\[
 \frac d{dt}e^2=-2ce^2K=-4\eta K\mathcal L.                 \tag{6.4}
\]

The source is bounded, every `G` in (3.1) is bounded, and `q` is finite.
Thus the maps in (3.4)--(3.6) are finite polynomials of bounded multilinear
maps on

\[
 \mathcal H_0\times\mathcal H_q\times\mathfrak G_L
 \times\mathbb R.
\]

They are locally Lipschitz, so Picard--Lindelof gives a unique maximal
solution.

There is no finite-time escape.  If `K_X` is the contribution of any one
state block to `K`, then (6.4) and Cauchy--Schwarz imply, for finite `T`,

\[
 \begin{aligned}
 \|X(t)-X(0)\|
 &\le\int_0^t c|e|\sqrt{K_X}\,ds\\
 &\le\sqrt{t\int_0^t c^2e^2K\,ds}
 \le |e(0)|\sqrt{cT/2}.                                    \tag{6.5}
 \end{aligned}
\]

The continuation criterion therefore extends the solution globally.

The monotone direct paths from `a` and from `b` have unit norm and are
mutually orthogonal.  At `G=0`, all `p_j` and `z_j` in (3.4) consequently
have norm one, while `p_q` is orthogonal to `B`.  There are two endpoint
terms and `q=L-1` matrix terms in (3.5), proving (4.2).

## 7. Global loss convergence

Suppose first that `y_star != 0` and write

\[
 g=\operatorname{sgn}(y_\star)f,\qquad r=|e|.
\]

The scalar equation for `e` preserves its sign.  Hence

\[
 g'=crK,\qquad g(0)=0,qquad r=|y_\star|-g.                 \tag{7.1}
\]

Since `K(0)=L+1`, `g(t)>0` for every `t>0`.  Also

\[
 \frac d{dt}\|A\|^2=2ce f
 =\frac d{dt}\|B\|^2=2crg.                                \tag{7.2}
\]

Both initial norms equal one, so call their common square `h`.  From
`f=<A,z_0>=<B,p_q>` and Cauchy--Schwarz,

\[
 K\ge \frac{g^2}{\|A\|^2}+\frac{g^2}{\|B\|^2}
 =\frac{2g^2}{h}.                                           \tag{7.3}
\]

Fix any `t_0>0` and put `g_0=g(t_0)>0`, `h_0=h(t_0)`.  Dividing (7.2) by
(7.1) and using (7.3) gives

\[
 \frac{dh}{dg}=\frac{2g}{K}\le\frac hg.
\]

Therefore `h/g` is nonincreasing for `t>=t_0`, and

\[
 K(t)\ge\frac{2g(t)^2}{h(t)}
 \ge\frac{2g_0^2}{h_0}=:\kappa>0.                           \tag{7.4}
\]

Now `r'=-crK` proves

\[
 r(t)\le r(t_0)e^{-c\kappa(t-t_0)},                         \tag{7.5}
\]

which is (4.3).  This argument also shows that every state block has finite
total variation after `t_0`, because

\[
 \int_{t_0}^\infty c r\sqrt{K_X}\,dt
 \le\int_{g_0}^{|y_\star|}\frac{dg}{\sqrt K}
 \le\frac{|y_\star|-g_0}{\sqrt\kappa}.                    \tag{7.6}
\]

Thus the closure is not merely loss-global: its state converges in its
natural Hilbert norm.

## 8. Gaussian-word and positive-time proof program

The required initialization fact is the following fixed-depth lemma target.

**Rooted-word lemma target.**  Fix `q` and a finite maximum path length
`R`.  For each layer there are random evaluation maps

\[
 J_{j,n}:\operatorname{span}\{e_s:|s|\le R,\ s\in
 \mathcal S_q(j)\}\longrightarrow\mathbb R^n              \tag{8.1}
\]

such that the two roots evaluate to `a_n(0)` and `b_n(0)`, and, in
probability,

\[
 J_{j,n}^*J_{j,n}\longrightarrow I,                        \tag{8.2}
\]

\[
 M_{j,n}(0)J_{j-1,n}-J_{j,n}\Lambda_j\longrightarrow0,
 \qquad
 M_{j,n}(0)^TJ_{j,n}-J_{j-1,n}\Lambda_j^*\longrightarrow0  \tag{8.3}
\]

in operator norm on every fixed truncated path span (with the output span
enlarged by one level).

Here is the intended proof mechanism.  For a path
`s=(sigma;s_0,...,s_r)`, define the unnormalized finite-width word by summing
the product of the traversed Gaussian matrix entries and the Gaussian root
entry over neuron indices, with indices at repeated visits to the same layer
required to be distinct.  Give each traversed edge a factor `n^(-1/2)` and
the resulting vector one final factor `n^(-1/2)`; this is `J_(j,n)e_s`.

Expand an inner product of two such words.  Wick's rule makes its expectation
zero unless every Gaussian entry and the root color can be paired.  The
unique pairing with the maximal number of free neuron indices occurs when
the colored paths are identical, and contributes one.  Every other pairing
identifies at least one additional neuron index and is `O(n^(-1))`.  In the
doubled expansion for the variance, the two disconnected maximal pairings
cancel the square of the expectation; each remaining diagram again loses a
free index.  Hence every fixed Gram entry is

\[
 \langle J_{j,n}e_s,J_{j,n}e_t\rangle
 =\mathbf1_{s=t}+O_{\mathbb P}(n^{-1/2}).                   \tag{8.4}
\]

There are finitely many paths below `R`, so the claimed entrywise estimates
would imply (8.2) in operator norm.  The preceding free-index sentence does
not itself supply the required labelled-chain variance enumeration.

For (8.3), multiply a word by the next Gaussian matrix and split the new
neuron-index sum.  A previously unused index is exactly the appended path
`s star j`.  If the last edge traversed the same matrix in the reverse
direction, its Wick contraction is exactly the shortened path `s^-`.
Every other collision or crossing contraction should lose a free index.  A
separate action-residual diagram lemma is required to turn that observation
into the stated `O_{L^2}(n^(-1/2))` bound.  A finite union bound gives (8.3)
only after this missing moment estimate is proved.

Conditionally on that lemma and a compatible coefficient-lift lemma, one can
pass from fixed words to positive time.  On the event

\[
 \max_j\|M_{j,n}(0)\|\le C_0,qquad
 \|a_n(0)\|+\|b_n(0)\|\le C_0,                             \tag{8.5}
\]

whose probability tends to one by the Gaussian operator-norm bound and the
law of large numbers, (5.6) gives the same estimate as (6.5), uniformly in
`n`.  Thus, on every fixed time interval, all endpoint changes and all
matrix changes in Frobenius norm are bounded independently of width.  In
particular the matrix operator norms and the local Lipschitz constants of
the finite and limiting vector fields share one deterministic stopped bound.

Picard iteration would then close the ODE-stability part of the argument.
Its `r`-th iterate is a finite linear combination of rooted
Gaussian words of a finite maximum length.  Equations (8.2)--(8.3) therefore
show inductively that the finite-width iterate, its output, and its kernel
converge to the corresponding iterate of (3.6).  On the stopped bounded set,
the Picard remainders are bounded uniformly by the usual factorial estimate

\[
 \frac{(C\Delta t)^r}{r!}.                                  \tag{8.6}
\]

First choose `r` so that (8.6) is small and then send `n` to infinity.  With
the missing lift and leakage estimates, this would give (4.1).  The ODE
stability argument uses no analyticity of the final trajectory and no
all-order Taylor assumption; it does not replace the omitted multi-edge
Gaussian combinatorics.

## 9. Checks at small depth

### `L=1`

There is no middle operator.  The closure is

\[
 \dot A=ceB,\qquad \dot B=ceA,
 \qquad K=\|A\|^2+\|B\|^2.                                \tag{9.1}
\]

In feature-ascent time (`ce=1`) and from orthonormal roots,

\[
 F(s)=\sinh(2s),\qquad K(s)=2\cosh(2s).                    \tag{9.2}
\]

Thus `F'(0)=2` and `K(0)=2`, matching the previously proved depth-one closed
form.

### `L=2`

There is one edge source, one Hilbert--Schmidt block, and `K(0)=3`.  This is
the path-basis form of the previously proved depth-two mean-field flow.  The
special depth-two balancedness invariant reduces it further, by the scalar
spectral theorem, to the explicit one-measure oscillator in
`../depth2_autonomous_mse_closure/THEOREM_AND_PROOF.md`.  Since both systems
are positive-time limits of the same finite-width flow, their output and
loss readouts coincide.

## 10. Why a scalar spectral measure does not simply persist

For a deep linear chain, gradient flow conserves the adjacent balancedness
operators

\[
 \Theta_j\Theta_j^*-\Theta_{j+1}^*\Theta_{j+1}.             \tag{10.1}
\]

At `L=2`, the relevant dynamics can be reduced to one self-adjoint operator,
which is why one scalar spectral coordinate suffices.  At `L>=3`, the
initial data contain mixed words in several independent nonnormal Gaussian
edge operators and their adjoints.  The adjacent invariants live at
different grades and are not jointly diagonalizable.  A scalar spectral
measure of one conserved matrix therefore loses mixed-word information.

The rooted-path source retains exactly that information in one
noncommutative block operator.  This disproves only the *naive simultaneous
scalar diagonalization route*.  It is not a theorem that no more ingenious
scalar encoding can ever exist.

## 11. Relation to Stieltjes and exact scope

The deterministic operator IDE determines its entire physical loss curve
and, by repeated differentiation, every finite feature derivative at every
fixed depth.  At `L>=3`, identifying that curve with the network's
positive-time width limit is conditional as stated above.  The IDE
does not prove that the transformed output-kernel coefficients form a
Stieltjes moment sequence for all `L`.  That positivity question remains a
specialization of the broader autonomous-closure result.

The representation has one source operator and an `O(1)` number of state
objects even when written for symbolic `L`.  Its graded path space and the
finite sum in (3.5)--(3.6) contain `L-1` edge grades.  Hence it is compressed
with respect to width and derivative order, and uniform in formula, but not
a constant-work algorithm as `L -> infinity`.

## 12. Relation to the published construction

Chizat, Colombo, Fernandez-Real, and Figalli rigorously derive the
corresponding deterministic `ell^2` gradient system for one middle random
matrix.  Their Section 6 gives the same arbitrary-depth path sets, Gaussian
bases, edge operators, and coefficient dynamics.  The paper explicitly
labels that multi-layer section formal and says that the missing technical
details follow the core method.  Section 8 above outlines the analogous
specialization; it does not supply the missing multi-edge Wick enumeration
or coefficient-lift lemma.  See `CANONICAL_NOTE.md` for the corrected claim
boundary and the precise conditional theorem.

Reference: L. Chizat, M. Colombo, X. Fernandez-Real, and A. Figalli,
*Infinite-width limit of deep linear neural networks*, Communications on
Pure and Applied Mathematics 77 (2024), 3958--4007,
<https://doi.org/10.1002/cpa.22200>.

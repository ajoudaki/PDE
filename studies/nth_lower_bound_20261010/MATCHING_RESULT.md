# Matching local upper and lower storage for the original frozen-top NTH

Status: internally checked theorem, 2026-10-10; complete scoped
reconstruction in [MATCHING_CHECK.md](MATCHING_CHECK.md).
This continues the same lower-bound investigation. No experiment, changed
closure, paper edit, or promotion is involved.

## What is now closed, and what is not

For the correlated, growing-sample, two-hidden-layer identity-activation
family in [WORST_CASE_RESULT.md](WORST_CASE_RESULT.md), the necessary
literal-array storage scale is also sufficient:

\[
\operatorname{optimal\ literal\ storage}
=\exp\!\big[\Theta_\eta(\log m\,\log n)\big],
\qquad 4\mid m,\quad 4\le m\le\sqrt n,\quad d=m+1.
\tag{1}
\]

Here labels have fixed magnitude `0<eta<=1`. Optimal means the minimum
deterministic order's literal-array count achieving any prescribed fixed
success probability `p in (0,1)` and any prescribed positive constant factor
of the actual iid dense-pair discrepancy. The threshold in width can
depend on those fixed choices. The upper below in fact makes the
compression error at most `1/n` times that realized discrepancy, with
probability tending to one. The lower excludes every insufficient order
simultaneously and therefore also applies to order selection constrained
by a deterministic budget.

For `m=4 floor(n^a/4)` and fixed `0<a<=1/2`, (1) becomes

\[
\operatorname{optimal\ literal\ storage}
=\exp\!\big[\Theta_{\eta,a}((\log n)^2)\big].
\tag{2}
\]

Thus the previous example cannot furnish a larger asymptotic storage
exponent on its stated interval. This resolves that example, not the
existence of a harder example in the full nonlinear class.

The interval remains exactly `0<=t<=T=1/32768`. Neither (1) nor (2) is
an all-time upper, an upper on every fixed longer interval, a nonlinear
activation theorem, or a lower bound on factored/implicit tensor encodings.
The training metric is the canonical feature-learning metric and the
readout is zero, not the native Huang--Yau NTK scaling. Fixed labels are
not subjected to the older sample-dependent `Y=O(1/m)` restriction.

## A broader deep-linear upper theorem

The upper is not restricted to that hard dataset. Let `n>=4`, `1<=d<=n`,
and let any deterministic dataset have normalized inputs `v_a=x_a/sqrt(d)`
of norm at most one and labels `|y_a|<=1`, for `a=1,...,m`. The dataset
is independent of the initialization; it may vary with `n`. Use

\[
f_n(t,v)=c(t)^\top W(t)B(t)v,
\qquad \mathcal L=\frac1{2m}\sum_a(f_n(t,v_a)-y_a)^2.
\tag{3}
\]

Here `B=W^(1)/sqrt(n)` is `n` by `d`, `W=W^(2)` is `n` by `n`,
and `c=u/sqrt(n)` is an `n`-vector. Their Euclidean/Frobenius gradient
flow is exactly the original mobilities `(n,1,n)`. Entries of `B_0,W_0`
are independent `N(0,1/n)`, and `c_0=0`. Both activations are identity.

The original ordered hierarchy is defined by
`K_1(v)=f_n(v)` and
`K_(r+1)(...,v)=D K_r[grad f_n(v)]`. Its order `q` copies the initial
tensors through rank `q`, freezes that rank, and evolves every lower
rank with its own residual `(y_a-f_(n,q)(v_a))/m`. Passive query indices
do not enter the loss. These definitions are identical to those in
[UPPER_LOCAL_GEOMETRIC.md](UPPER_LOCAL_GEOMETRIC.md), whose complete
ordered-integral proof is a dependency of this theorem.

Define both errors on the same interval and the same whole input sphere:

\[
E_n(q)=\sup_{0\le t\le T}\sup_{\|v\|_2=1}
 |f_n(t,v)-f_{n,q}(t,v)|,
\qquad
D_n=\sup_{0\le t\le T}\sup_{\|v\|_2=1}
 |f_n(t,v)-\widetilde f_n(t,v)|,
\tag{4}
\]

where the tilde is an independent copy of the same dense model.
No lower bound is obtained by substituting an upper concentration rate
for `D_n`.

Set

\[
q_n=\left\lceil\frac{\log(2^{37}n^3)}{\log1024}\right\rceil.
\tag{5}
\]

For every such dataset, with probability at least

\[
1-\frac{4e}{\sqrt n}-4e^{-c_*n},
\qquad c_*=4-\frac32\log9>0,
\tag{6}
\]

the dense and original NTH solutions exist throughout the interval and

\[
E_n(q_n)\le\frac{D_n}{n}.
\tag{7}
\]

There is no initial Gram-gap or positive-label-mean assumption for this
upper. If the dynamics stalls because the label-weighted input mean is
zero, both sides of (7) are exactly zero; no ratio is taken in that case.
Probability (6) is for each fixed deterministic dataset, not one
simultaneous anti-concentration event for all possible datasets.

For `m>=2`, retaining the training hierarchy and `d` passive coordinate
queries requires at most

\[
\begin{aligned}
\text{moving arrays}&\le2(m+d)m^{q_n-2},\\
\text{frozen top}&=(m+d)m^{q_n-1},\\
\text{all arrays}&\le2(m+d)m^{q_n-1}.
\end{aligned}
\tag{8}
\]

The fixed dataset, if retained, adds at most `md+m` scalars. The coordinate
outputs decode any later unseen input by linearity, so the sphere guarantee
does not hide infinitely many stored query arrays. In particular the
retained size is at most

\[
(m+d)\exp[O(\log m\,\log n)]+O(md+m).
\tag{9}
\]

For polynomially growing `m` and `d<=n`, this is
`exp(O((log n)^2))`. When `m=1`, the exact count is `(1+d)(q_n-1)`
moving plus `1+d` frozen coordinates. Coefficient-generation work,
initialization peak memory, numerical integration, and bit precision
are not included in these retained real-coordinate counts.

## Proof of the actual-variability comparison

The geometric upper alone is not enough for (7). The additional step
below proves that the actual iid dense discrepancy is not too small.
All constants are deliberately conservative, since any inverse-polynomial
bound suffices for the matching logarithmic order.

### 1. Exact data contraction and geometric NTH error

Only within the proof write

\[
Q=\frac1m\sum_a v_av_a^\top,\qquad
b=\frac1m\sum_a y_av_a,\qquad
w(t)=B(t)^\top W(t)^\top c(t).
\tag{10}
\]

Then `||Q||op<=1`, `||b||<=1`, and `f_n(t,v)=v^T w(t)`.
The exact dense equations are

\[
\dot B=W^\top c(b-Qw)^\top,\quad
\dot W=c[B(b-Qw)]^\top,\quad
\dot c=WB(b-Qw).
\tag{11}
\]

On the event `||B_0||op,||W_0||op<=4`, the complete proof in
UPPER_LOCAL_GEOMETRIC yields

\[
E_n(q)\le64\|b\|_2\,1024^{-q},\qquad q\ge2.
\tag{12}
\]

Its key bounds are reproduced to identify precisely the used theorem:
the initialized ordered source coefficients satisfy

\[
|K_{k+1}(v_0,\ldots,v_k;0)|
\le32\,4^k(k+2)!\prod_{i=0}^k\|v_i\|_2.
\]

Their ordered integral against `b-Qw_q` has simplex factor `T^k/k!`.
On `||w_q||<=||b||`, the own-residual map is a contraction with constant
less than `1/32`. Dense repeated integration has remainder at most
`(125/2)(k+1)(k+2)(10||b||T)^k`, which tends to zero. Thus the dense
path is the infinite map's fixed point and the original finite closure
is its truncated map's fixed point. Their difference is bounded by the
omitted tail divided by `1-1/32`. Zero-readout parity and an elementary
geometric-tail bound give (12). This is not a time-polynomial substitute
or a supplied dense residual.

The same input's Gaussian-net proof gives failure at most
`2 exp(-c_*n)` for the two matrix norms of each dense initialization.
For the independent pair their combined bad event is at most
`4 exp(-c_*n)`.

### 2. A uniform complex disk with the label-mean factor retained

We need a second-derivative bound proportional to `||b||`, even when
this quantity is small. Extend (11) holomorphically by retaining ordinary
transposes, not conjugates. In the maximum block norm
`max(||B||op,||W||op,||c||2)`, use the ball of radius one around an
initial state with the two matrix norms at most four and zero `c`.
All block norms are then at most five. Since `||w||<=125`, the residual
vector has norm at most `126`, so every block velocity has norm at most
`3150`.

For a variation of maximum block norm one, the prediction vector changes
by at most `75`. Differentiating each velocity in (11) therefore gives
at most `5*126+5*126+25*75=3135`. Picard integration on the complex disk

\[
|t|\le R_0=1/4096
\]

maps this path ball into itself and is a contraction, since both
`3150 R_0<1` and `3135 R_0<1`. Starting from constant paths, its uniform
limit is holomorphic in the disk and is the real dense solution on the
real interval. All estimates are independent of the dimensions.

On this disk, the derivative of the vector prediction obeys the norm
bound

\[
\|w'(t)\|_2\le1875(\|b\|_2+\|w(t)\|_2).
\]

Indeed the derivative of a cubic prediction gives three terms bounded
by `5^4` times the residual-vector norm; transposes have the same
operator norm also over the complex field. Integration along each radial
segment, followed by the scalar integral comparison, proves

\[
\|w(t)\|_2\le\|b\|_2(e^{1875|t|}-1)<\|b\|_2,
\qquad |t|\le R_0.
\tag{13}
\]

In the last inequality one uses `1875/4096<log 2`. If `b=0`, uniqueness
in (11) gives the stationary dense flow. The finite own-residual map in
step 1 also has the stationary solution, giving (7) exactly. Henceforth
suppose `b!=0`.

Let `v_*=b/||b||` and let
`g(t)=f_n(t,v_*)-tilde f_n(t,v_*)`. On the pair's good event, (13)
implies `|g(t)|<=2||b||` on the disk. Put `R=1/8192`, so `T=R/4`.
At every real `0<=t<=T`, the complex circle of radius `R/2` centered
at `t` lies strictly inside the preceding disk. Cauchy's formula gives

\[
|g''(t)|\le\frac{2!\,2\|b\|_2}{(R/2)^2}
=2^{30}\|b\|_2.
\tag{14}
\]

### 3. Small-ball estimate for the initial prediction velocity

At zero readout, `B'(0)=W'(0)=0` and `c'(0)=W_0B_0b`. Thus

\[
f_n'(0,v_*)=\|b\|_2\,\|W_0B_0v_*\|_2^2.
\tag{15}
\]

Because `v_*` is deterministic and has norm one,

\[
H:=\|W_0B_0v_*\|_2^2
\ \overset{\mathrm{law}}=\ A B,
\qquad A,B\ \text{independent with law }\chi_n^2/n.
\tag{16}
\]

To check independence, `A=||B_0v_*||^2` has that law; conditional on
the full vector `B_0v_*`, the ratio `||W_0B_0v_*||^2/A` has the same
chi-square law, independent of the conditioning vector. The zero-norm
event has probability zero.

Here is an elementary uniform density bound without a central limit
approximation. The density `p` of `A` has shape
`p(a)=C_n a^(n/2-1) exp(-na/2)` for `a>0`. For `n>=4` its maximum is
at `a_0=1-2/n>=1/2`. On `[a_0,a_0+1/sqrt(n)]`,

\[
(\log p)'(a_0)=0,\qquad
(\log p)''(a)=-\frac{n/2-1}{a^2}\ge-2n.
\]

Consequently `p(a)>=exp(-1)p(a_0)` throughout this interval. Its
integral is at most one, giving `||p||infinity<=e sqrt(n)`.
Integration by parts in the same density gives
`E(1/B)=n/(n-2)<=2`. The product density therefore satisfies

\[
\|p_H\|_\infty
\le\|p\|_\infty\,\mathbb E(1/B)
\le2e\sqrt n.
\tag{17}
\]

For independent `H,tilde H`, convolution bounds the density of their
difference by the same supremum. Hence, for every `a>=0`,

\[
\Pr\{|H-\widetilde H|\le a\}\le4e\sqrt n\,a.
\tag{18}
\]

In particular, except with probability `4e/sqrt(n)`, (15) gives

\[
|g'(0)|\ge\frac{\|b\|_2}{n}.
\tag{19}
\]

This probability estimate is unconditional. We intersect it with the
matrix-norm event afterward; there is no conditioning error in (18).

### 4. Transfer to actual dense-pair discrepancy and choose the order

Since `g(0)=0`, Taylor's integral formula and (14), evaluated at the
deterministic time `t_n=1/(2^30 n)<=T`, give on (19)

\[
\begin{aligned}
|g(t_n)|
&\ge |g'(0)|t_n-\tfrac12\,2^{30}\|b\|_2t_n^2\\
&\ge\frac{\|b\|_2}{2^{31}n^2}.
\end{aligned}
\tag{20}
\]

Thus the actual whole-sphere dense discrepancy satisfies the same lower
bound. Combining (12) and (20) yields

\[
\frac{E_n(q)}{D_n}\le2^{37}n^2\,1024^{-q}.
\tag{21}
\]

The norm of the label-weighted input mean cancels exactly. Choice (5)
proves (7), and the union of the two bad events gives (6). A lower bound
on the actual dense discrepancy, not its upper bound, is the needed
probability step for this sufficient-storage conclusion.

### 5. Storage and the matching lower

For each training or coordinate-query first slot, the lower ranks have
`sum_(r=1)^(q-1) m^(r-1)` entries and the frozen top has `m^(q-1)`.
This proves (8). Input linearity is preserved in the first slot by every
original NTH equation, so `f_(n,q)(t,v)=sum_i v_i f_(n,q)(t,e_i)` is
an exact decoder of the same closure, not a replacement dynamical model.

For the hard family, `d=m+1` and `m>=4`, the upper count is at most
`5m^q+md+m`. Since `q_n=O(log n)`, it gives the upper in (1).
The complete lower in WORST_CASE_RESULT gives

\[
\log\operatorname{storage}\ge
c_\eta\log m\,\log\frac{n}{m+\log(en)}.
\]

Uniformly over `4<=m<=sqrt(n)`, the last logarithm is between positive
absolute multiples of `log n` for sufficiently large `n`. The same
lower holds for the moving literal arrays, with an adjusted constant.
It therefore gives the lower in (1), and substitution of `m` as a fixed
power of `n` gives (2). The lower at the particular passive query also
applies to the larger sphere error used here.

## Boundary of this result and remaining search

The exact original closure, initialization provenance, Gaussian metric,
own-residual feedback, and actual-discrepancy benchmark are all retained.
The matching upper is uniform over data inside the stated deep-linear,
short-time class; it is not merely an upper on one favored dataset.

It cannot be promoted to general strip-analytic nonlinear activations by
calling their equations analytic. Such a step requires an all-order bound
on the complete ordered source tensors and their evolving remainder,
uniform in width and growing order. Nor can the source expansion be
restarted to cover a longer interval without changing the prescribed
frozen-top initialization rule. The independent harder-witness and
nonlinear-upper routes record these separate unresolved directions.

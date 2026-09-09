# Reachable-tail and early-layer audit

Status: rigorous partial exclusions and an exact remaining stopping problem;
not a compact-time convergence theorem.

All times below are feature-ascent times.  Physical MSE time is a positive
scalar time change while the residual has its initial sign.

## 1. The only dangerous nonnegative terms

Put

\[
h=\langle H^2\rangle_n,
\qquad C=A-fY,
\qquad R={2\over\beta}ZC,
\qquad T=(I-H\otimes H)G^TR.
\]

Then

\[
f'=K=\langle Y^2\rangle_n
{4h\over\beta^2}\langle Z^2C^2\rangle_n
{4\over\alpha}\langle HT^2\rangle_n.       \tag{1.1}
\]

Thus a sufficient spatial-tail condition for compact-time output
equicontinuity is, for every fixed `S,eta>0`,

\[
\lim_{L\to\infty}\limsup_{n\to\infty}
\Pr\left\{\int_0^S \mathcal U_{n,L}(s)\,ds>\eta\right\}=0, \tag{UI}
\]

where

\[
\mathcal U_{n,L}=
\beta^{-2}\langle Z^2C^2
 1_{\{Z^2+C^2>L\}}\rangle_n
+\alpha^{-1}\langle HT^2
 1_{\{H+T^2>L\}}\rangle_n.                 \tag{1.2}
\]

The logically weaker necessary target is uniform absolute continuity in
time of the last two terms of (1.1).  The exact loss identity only bounds
their total integral and does not imply either property.

## 2. Exact current-plus-memory decomposition

The learned matrix is rank-one integrated:

\[
G_t=G_0+\int_0^t R_s\otimes H_s\,ds.          \tag{2.1}
\]

Consequently

\[
Z_t=G_0H_t+\int_0^tR_s\langle H_s,H_t\rangle_n\,ds, \tag{2.2}
\]

\[
T_t=P_{H_t}G_0^TR_t+
\int_0^tP_{H_t}H_s\langle R_s,R_t\rangle_n\,ds,     \tag{2.3}
\]

with `P_H=I-H tensor H`.  For coordinate `j`, the learned-memory
integrand in (2.3) is

\[
\{H_j(s)-H_j(t)\langle H_s,H_t\rangle_n\}
\langle R_s,R_t\rangle_n.                    \tag{2.4}
\]

This displays both effects exactly.  A persistent lone winner is opposed by
the normalization contraction, but rotated historical directions are not
annihilated.  Replacing (2.3) by a current scalar variance discards precisely
the unresolved adaptive information.

## 3. Initialization has no concentrated pack

Gaussian order statistics and conditional row regression imply that, for
every fixed `a>0`, with probability at least
`1-C_a n^{-a}-2 exp(-c_epsilon n/log n)`, simultaneously for every
`1<=k<=n`,

\[
\sup_{|J|=k}\langle1_JH^2\rangle_n,
\quad
\sup_{|I|=k}\langle1_IY^2\rangle_n,
\quad
\sup_{|I|=k}\langle1_IR^2\rangle_n
\le C_{\epsilon,a}\left\{
{k\over n}\log^2{en\over k}+{\log^2n\over n}\right\}, \tag{3.1}
\]

and

\[
\sup_{|J|=k}\langle1_JT^2\rangle_n
\le C_{\epsilon,a}\left\{
{k\over n}\log{en\over k}+{\log n\over n}\right\}.     \tag{3.2}
\]

In particular every sublinear pack has vanishing normalized initial mass.
Likewise a union bound over Gaussian submatrices gives, for row and column
sets of sizes `r,c`,

\[
\|G_{0,IJ}\|_{op}\lesssim {1\over\sqrt n}
\left[\sqrt r+\sqrt c+
\sqrt{r\log(en/r)+c\log(en/c)+x}\right]       \tag{3.3}
\]

outside probability at most `2 exp(-x)`.  Every block with both dimensions
`o(n)` therefore has vanishing operator norm, even after selecting the block
from the observed matrix.

At time zero the transpose message can be computed exactly.  Conditional on
`H,Z,A`, with `q_R=<R^2>` and
`s=<Z,R>=2 epsilon f/beta^2`,

\[
G_0^TR={s\over h}H+\xi,
\qquad
\xi\sim N\left(0,q_R\{I-HH^T/(nh)\}\right),
\qquad \langle H,\xi\rangle_n=0.              \tag{3.4}
\]

This proves the required Gaussian pack estimates at initialization.  It does
not justify applying an independent-Gaussian bound to the adaptive `R_t`.

## 4. What can be excluded unconditionally at short times

Let `D_T=f(T)-f(0)=int_0^T K`.  Monotonicity and `A'=Y` give

\[
D_T\le 2\|A(0)\|_n+T=:B_T,                   \tag{4.1}
\]

and hence

\[
\|G_T-G_0\|_F,\ \|u_T-u_0\|_n\le\sqrt{TB_T},
\qquad \|A_T-A_0\|_n\le T.                  \tag{4.2}
\]

Thus the learned part cannot create a new order-one singular direction in
`o(1)` time.  More quantitatively, a column pack of sublinear cardinality
cannot acquire a fixed fraction of `H` mass in time `o(n^-1/2)`, and a row
pack cannot acquire a fixed fraction of `Y` mass in time `o(n^-1)`.  The
proof uses (4.2),

\[
\|D\{x\mapsto N_\epsilon(x^2)\}\|_{2\to2}
\le2\sqrt2\,\epsilon^{-1/4}n^{1/4},           \tag{4.3}
\]

and the finite-dimensional inequality relating empirical fourth and second
norms.  Therefore simultaneous fixed-mass row/column concentration is
excluded on `o(n^-1/2)` horizons.

There is also a completely unconditional, but smaller, no-action window.
With probability tending to one,

\[
D_T\le C_{\epsilon,a}
\{T\sqrt n\log n+n^{3/2}T^2+T\}.             \tag{4.4}
\]

Hence `D_{T_n}->0` whenever

\[
T_n\sqrt n\log n+n^{3/2}T_n^2\to0;           \tag{4.5}
\]

in particular, no nonzero output/kernel-action layer occurs on
`T_n=o(n^-3/4)`.

These estimates are genuine exclusions, but they leave the interval from
roughly `n^-1/2` to `o(1)` open.

## 5. The exact probability estimate still missing

For a column pack `J`, stop before it contains normalized mass `rho`.  A
mechanism-specific proof needs the adaptive leave-one-pack bound

\[
\sup_{\substack{|J|\le k_n\\t\le T_n\wedge\tau_J(\rho)}}
{\|1_JP_{H_t}G_0^TR_t\|_n^2\over\|R_t\|_n^2+1}
\lesssim {k_n\over n}\log{en\over k_n}+\rho, \tag{5.1}
\]

and its row analogue.  The obstacle is not a missing union bound: `R_t`
depends on the same columns of `G_0`.  It requires a cavity trajectory and a
uniform stability estimate at the entropy cost
`k_n log(en/k_n)`.

The learned-memory term additionally requires a temporal coercivity estimate
for (2.4).  The exact replicator identity

\[
\log{H_j(t)\over H_j(0)}=
4\int_0^t{T_j-\langle H^2,T\rangle_n\over\alpha}\,ds       \tag{5.2}
\]

shows how much relative advantage a growing coordinate must accumulate, but
the total action bound does not control the signed, rotating integral in
(2.4).

Accordingly, neither an iid-reachable `o(1)` concentration layer nor its
absence has been proved on the full remaining scale.  Ambient spike states
and low-energy paths cannot decide (5.1).


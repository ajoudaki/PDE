# (H=3,4), (B=1), generic activation through (F^{(5)}(0))

## Current conclusion

For each of the separately fixed hidden depths `H=3` and `H=4`, the
order-five mean-field peel closes into a finite deterministic arithmetic DAG
whose only stochastic leaves are explicitly declared one-dimensional
Gaussian activation moments.  No tangent, backward, innovation, covariance,
pseudoinverse, or unevaluated recursion variable survives in the four
terminal formulas embedded below.

Two independently frozen symbolic routes agree coefficient by coefficient.
In the common layer-tagged `Q0=1` quotient, the discrepancy counts for
`(A,B,C)` are zero over `(4,342,27421)` terms at `H=3` and
`(5,1929,462776)` terms at `H=4`.  In the unit-Gram quotient they are zero
over `(4,160,6519)` and `(5,350,17641)` terms.  The exact symbolic-`Q0`
audit is recorded below.

The algebraic result becomes an annealed large-width theorem under the
polynomial-smooth tensor-program hypotheses in Section 9.  A merely `C^5`
activation gives the exact finite-width identities but does not, by itself,
justify expectation convergence.

## 1. Exact model and coefficient convention

For one deterministic input `x`, common hidden width `n`, and

\[
Q^0={\|x\|^2\over d_0},
\]

use

\[
u^1_j={w_j^Tx\over\sqrt{d_0}},\qquad h^\ell=\phi(u^\ell),
\]

\[
u^\ell_i={1\over\sqrt n}\sum_{j=1}^nW^\ell_{ij}h^{\ell-1}_j,
\qquad 2\leq\ell\leq H,
\]

\[
f_n={1\over n}\sum_{i=1}^na_i h^H_i.
\tag{1.1}
\]

Every entry of `w,W^2,...,W^H,a` is an independent standard Gaussian at
initialization and every displayed parameter is trained.  Define

\[
D_n=n\nabla f_n\mathbin\cdot\nabla,
\qquad
F_H^{(k)}(0)=\lim_{n\to\infty}\mathbb E[D_n^kf_n].
\tag{1.2}
\]

The characteristic is feature ascent, `theta_dot=n grad f_n`.  Ordinary
Taylor coefficients therefore satisfy

\[
f_n(\theta(t))=\sum_{k=0}^5{D_n^kf_n\over k!}t^k+O(t^6).
\tag{1.3}
\]

The exact finite-width forward/reverse equations and the population peel are
given in the embedded arbitrary-depth derivation in Part II.

## 2. Canonical Gaussian moment grammar

Define forward variances recursively by

\[
Q^\ell=\mathbb E_{G\sim N(0,Q^{\ell-1})}[\phi(G)^2].
\tag{2.1}
\]

For `1<=ell<=H` and `nu=(nu0,...,nu5)`, the arbitrary-variance atom is

\[
\boxed{
L_{\ell,\nu}
=\mathbb E_{G\sim N(0,Q^{\ell-1})}
 \prod_{r=0}^5\phi^{(r)}(G)^{\nu_r}.}
\tag{2.2}
\]

The terminal files write this as `Lell_{nu0...nu5}`.  Layer tags are retained
until specialization.  The only other non-rational leaf is the explicit
metric factor `Q0=Q^0`.

For the clean unit-Gram quotient `Q^0=...=Q^H=1`, put

\[
\boxed{M_\nu=\mathbb E_{G\sim N(0,1)}
 \prod_{r=0}^5\phi^{(r)}(G)^{\nu_r},}
\tag{2.3}
\]

identify every `Lell_nu` with `M_nu`, and impose `M_200000=1`.  This quotient
is distinct from the unnormalized quadratic control: for `phi(x)=x^2`, the
forward variances are `1,3,27,2187,14348907`, not all one.

## 3. Explicit first coefficient

Write `dell=Lell_020000` and `qell=Lell_200000=Q^ell`.  Directly from the
frozen tagged formula,

\[
\boxed{
A_3=q_3+q_2d_3+q_1d_2d_3+Q^0d_1d_2d_3,}
\tag{3.1}
\]

\[
\boxed{
A_4=q_4+q_3d_4+q_2d_3d_4+q_1d_2d_3d_4
       +Q^0d_1d_2d_3d_4.}
\tag{3.2}
\]

If `d=M_020000` in the unit quotient, these reduce to

\[
\boxed{A_3=1+d+d^2+d^3,\qquad A_4=1+d+d^2+d^3+d^4.}
\tag{3.3}
\]

The explicit `B_H` and `C_H` formulas are the finite dependency-first
arithmetic DAGs embedded in Parts III--VI.  A line `t_j = ...` contains only
rational arithmetic, earlier `t` nodes, and atoms (2.2) or (2.3); the final
three lines assign `A,B,C`.  Those appendices are the terminal formulas, not
instructions to evaluate the response recursion in Part II.  Fully
distributed coefficient dictionaries are hash-identified in Section 7.

## 4. Stieltjes coefficients, kernel series, and Padé curve

For either depth, define exactly

\[
\boxed{
\mu_{0,H}={B_H\over2A_H^2},\qquad
\mu_{1,H}={4B_H^2-A_HC_H\over24A_H^5}.}
\tag{4.1}
\]

Then

\[
\boxed{
K_H(y)=F_H'(F_H^{-1}(y))
=A_H+\mu_{0,H}y^2-\mu_{1,H}y^4+O(y^6).}
\tag{4.2}
\]

When `mu0` is nonzero, the first one-pole Padé approximation is

\[
\boxed{
K_{H,[0/1]}(y)=A_H+
 {\mu_{0,H}y^2\over1+(\mu_{1,H}/\mu_{0,H})y^2}.}
\tag{4.3}
\]

It is a Stieltjes interpretation only when the required moment signs and
nondegeneracy are verified, in particular `A_H>0`, `mu0>=0`, and `mu1>=0`.
Otherwise (4.3) is called Padé only.

For one-sample MSE with label one, the rational kernel induces

\[
\dot y=2\eta(1-y)K_{H,[0/1]}(y),\qquad L=(1-y)^2,
\tag{4.4}
\]

or equivalently

\[
2\eta t=\int_0^{y(t)}
{1+(\mu_{1,H}/\mu_{0,H})s^2\over
(1-s)[A_H+(A_H\mu_{1,H}/\mu_{0,H}+\mu_{0,H})s^2]}
\,ds,
\quad L_{H,[0/1]}(t)=(1-y(t))^2.
\tag{4.5}
\]

The approximation is constructed for `K_H`; (4.4)--(4.5) are the loss curve
induced by that rational kernel.

## 5. Exact controls

All entries below are exact integers obtained from the layer-tagged formulas.
The independent frozen route reproduces the same table.

| activation | depth | `A` | `B` | `C` |
|---|---:|---:|---:|---:|
| constant `c` | any | `c^2` | `0` | `0` |
| `1+x` | 3 | `10` | `540` | `71152` |
| `1+x` | 4 | `15` | `1848` | `591176` |
| `x` | 3 | `4` | `160` | `13888` |
| `x` | 4 | `5` | `400` | `73240` |
| `x^2` | 3 | `14175` | `139445032896` | `4298284752832899360` |
| `x^2` | 4 | `138351807` | `59385566223611232192` | `81427352525619060193821492876576` |

For the linear control,

\[
(\mu_{0,3},\mu_{1,3})=(5,61/32),\qquad
(\mu_{0,4},\mu_{1,4})=(8,1369/375).
\tag{5.1}
\]

For the unnormalized quadratic control,

\[
(\mu_{0,3},\mu_{1,3})=
\left({95641312\over275625},
{3963629647049188\over3230587705078125}\right),
\tag{5.2}
\]

\[
(\mu_{0,4},\mu_{1,4})=
\left({25547421088\over16468947},
{262886046677291254852\over112573910972933256083589}\right).
\tag{5.3}
\]

A separate leading-width Wick/path enumerator proves the linear values after
exhausting 22,012 derivative histories at `H=3` and 102,582 at `H=4`.

For

\[
\phi(x)={\sin x\over\sqrt{(1-e^{-2})/2}},
\tag{5.4}
\]

all forward Grams equal one.  An 80-digit finite-Fourier evaluation of the
declared atoms gives

| depth | `A` | `B` | `C` | `mu0` | `mu1` |
|---:|---:|---:|---:|---:|---:|
| 3 | `6.300850741691` | `-854.3718615769` | `1076854.459362` | `-10.76015573635` | `-16.21718023510` |
| 4 | `9.273239352505` | `-4566.130252113` | `19488618.52478` | `-26.54943975998` | `-59.13618915685` |

Both `mu` values are negative at both depths, so (4.3) is Padé, not a
positive Stieltjes one-pole approximation, for this activation.

The preregistered finite-width discriminator used 7,700 independent networks
at widths `32,64,128,256` and fit the frozen affine-in-`1/n` extrapolator.
Every finite-value and four-batch heavy-tail gate passed.  At `H=3`, the
intercept comparison gives `z=1.2002` with `chi^2=1.8194`, two degrees of
freedom, and `p=0.4026`; at `H=4`, `z=0.4749`, `chi^2=2.0174`, and
`p=0.3647`.  Both satisfy the frozen `|z|<=3` and `p>=0.01` rules, so the
experiment is a **pass**.  This is empirical support only.  The exact result
file has SHA-256
`2b9250cbad87ce388d268a0cbe4d378b2e4d0924cb65f4003e2344fa118adccc`.

## 6. Mandatory structural audits

1. **Finite-width identity.**  Direct differentiation gives
   `a_dot=h^H`, `Mell_dot=b^ell(h^(ell-1))^T/n`, and
   `u1_dot=Q0 b1`.  Their ordinary-series convolution is exact at every
   finite `n,H` and is displayed in Part II.
2. **Parity.**  Negating only the initialized readout gives
   `(D_n^k f_n)(-a)=(-1)^(k+1)(D_n^k f_n)(a)`.  Hence
   `E f_n=E D_n^2 f_n=E D_n^4 f_n=0` exactly at every width.
3. **Equality/width census.**  At a fixed reused matrix and Taylor order `k`,
   a forward multiplication has one fresh sector, `k` earlier transpose
   responses, and `k(k+1)/2` literal rank updates.  A reverse multiplication
   has one fresh sector, `k+1` forward responses (including the
   chronologically earlier same-order forward use), and `k(k+1)/2` transpose
   rank updates.  Any further same-type equality loses a free width sum and
   is `O(1/n)`; indices at distinct layers are different types and cannot
   Wick-contract.
4. **Transpose closure.**  Per matrix, the retained registry has 21 forward
   covariances, 15 reverse covariances, 15 `alpha` responses, and 15 `beta`
   responses: 66 states.  The precise equations and the terminal
   Wick--Stein reduction are in Part II.
5. **Derivative ceiling.**  Independent scans of both frozen maps give
   maximum activation derivative `(1,3,5)` in `(A,B,C)`; no atom above
   `phi^(5)` survives.
6. **Independent canonicalization.**  The two producer manifests were frozen
   before comparison.  Every one of the tagged and unit maps at both depths
   has zero exact-rational discrepancies.
7. **Finite-width oracle gate.**  Two separately written moving-flow jets
   agree seedwise for `H=3,4`, widths `1,2,5`, and three seeds per cell; the
   worst scaled discrepancy is `2.7441e-14`, below the frozen `1e-10` gate.

8. **Symbolic `Q0` audit.**  With layer moments kept formal, the explicit
   `Q0` degrees are bounded by `(1,3,5)` for `(A,B,C)`: each directional
   derivative inserts at most one first-layer metric factor, and
   Wick--Stein reduction cannot raise Taylor order.  The independent route
   and primary route agree exactly at the six rational interpolation points
   `1/2,1,3/2,2,5/2,3`; the unused holdout `7/2` also has zero discrepancies,
   at both depths and for every coefficient.  This proves equality of the
   complete symbolic-`Q0` maps.  The post-freeze audit file has SHA-256
   `fb7dbab7cea9b6e1a2e18275ee695f6be56e8640199640a2bb1758ea864ee6ef`.

## 7. Frozen artifact ledger

Primary freeze manifest SHA-256:

`f4838437c1fb70b14713d39e8438d703434c49ffd72001beeb6fee8d53366b30`.

Independent freeze manifest SHA-256:

`dee0198e119864a90195101466f29f3ab2f248495c6e6a3494f35cafd3f2502b`.

| formula | CSE SHA-256 | distributed terms `(A,B,C)` | distributed-map SHA-256 |
|---|---|---:|---|
| `H3` tagged | `d9429b70d3513b1c0a4193f73c867db05b33d7ef81093d1ab2b2070992c66b83` | `(4,342,27421)` | `72d220fd8c855b07568ba513087a40dcbd9883bf96d26d04a919ff218b8cf5c4` |
| `H3` unit | `e84b07dd1d7befd5585163d0c11de3215323ba8659b421c0fcd2825ba9c90eaa` | `(4,160,6519)` | `564c6a27d6071e8601d21fd167dfd8f21d7ac9fe2323695a626eeebf73b980c6` |
| `H4` tagged | `9f2380ec15aa2b342c0dde025a03db9ad31b2c9b3fcb85f3bced1997994a0bb5` | `(5,1929,462776)` | `02b6d94798ccc19204852fe8298d4ef38d86124326ee721ca83fdefa6fb00ceb` |
| `H4` unit | `5459dfef9d487dd75f81fd7147389973e3e8c63c646f5266df24041c949199c2` | `(5,350,17641)` | `b3b220b76c8d30037cf0bfc0a8a1dc05884b28601a1c28e45b0daf9ff64faa5d` |

The primary layer-tagged maps retain symbolic `Q0`; the frozen independent
maps initially used `Q0=1`.  The post-freeze symbolic-`Q0` certificate in
Section 6 is therefore a distinct audit and does not mutate either freeze.

## 8. Complexity and arbitrary fixed depth

At fixed derivative order five, the compiler is a forward/reverse sweep with
66 response/covariance states per initialized hidden matrix, hence
`66(H-1)` registry entries and `O(H)` outer transitions.  The terminal
factor DAG is finite for every fixed `H`.  Full distribution is much larger:
the tagged `C` map grows from 1,045 terms at `H=2` to 27,421 at `H=3` and
462,776 at `H=4`.

Part II gives the finite-state arbitrary-fixed-`H` construction and an exact
deep-linear sequence through `H=10`.  The displayed arbitrary-`H` formulas
for deep-linear `B_H,C_H` are explicitly labeled as finite-difference
discoveries until a symbolic depth-degree bound is proved.  Nothing here
claims a simultaneous `H=H(n)` limit or a depth-uniform flat formula size.

## 9. Activation regularity and theorem boundary

The exact finite-width order-five algebra needs

\[
\phi\in C^5,\qquad
|\phi^{(r)}(x)|\le C_r(1+|x|^{m_r}),\quad0\le r\le5,
\tag{9.1}
\]

or any weaker envelope that makes every displayed contraction integrable.
This does not alone prove a population or annealed limit.

For a direct theorem-level bridge at each separately fixed `H`, a sufficient
hypothesis is

\[
\phi\in C^\infty,\qquad
\forall r\ge0\ \exists C_r,m_r:
|\phi^{(r)}(x)|\le C_r(1+|x|^{m_r}).
\tag{9.2}
\]

The finite jet is then one fixed NETSOR-transpose-plus program.  Setup 3.6
and Theorem 3.7 of Golikov--Yang, *Non-Gaussian Tensor Programs*, give almost
sure and every-finite-`L^p` convergence; in particular `L^1` identifies the
displayed deterministic coefficient with
`lim_n E[D_n^k f_n]`.  Gaussian matrices are a special case.  Singular Grams
do not require a pseudoinverse in this theorem route.

In a weaker tier with only convergence in probability or almost surely,
assume separately, for some `epsilon>0`,

\[
\sup_n\mathbb E|D_n^kf_n|^{1+\epsilon}<\infty,
\qquad k\in\{1,3,5\}.
\tag{9.3}
\]

This bound gives uniform integrability and therefore expectation convergence.
It is not equivalent to `L^(1+epsilon)` convergence.

## 10. Claim-status ladder

- **Exact finite width:** the ordinary-series forward/reverse equations and
  readout parity.
- **Formal population construction:** the 66-state-per-matrix response peel
  followed by terminating Wick--Stein elimination.
- **Algebraically audited normal forms:** the frozen `H=3,4` terminal DAGs,
  zero two-route coefficient discrepancies, derivative scan, and exact
  controls.
- **Empirical support only:** the normalized-sine finite-width regression in
  Section 5; it cannot prove the partition census or width theorem.
- **Theorem-level annealed result:** the same formulas under (9.2), or under a
  separately established probability limit plus (9.3).
- **Open:** simultaneous growing-depth limits, compact-time convergence of
  the full untruncated series, and a compact symbolic proof of the proposed
  arbitrary-`H` deep-linear closed form.

# Independent Route A: amortized observable DAG and hidden-activation RMS head

## Status and scope

This document was derived and frozen before inspecting any competing
Gamma_04 formula.  It concerns one sample, shared activation, arbitrary
separately fixed hidden depth H, unit forward Grams, and feature-ascent time

\[
\dot\theta=p(\theta):=n\nabla f(\theta),\qquad
D=p\mathbin\cdot\nabla .
\]

The universal order-five backbone is the already audited six-sweep scalar
recurrence.  Route A first derived and froze a three-coordinate post-R3
head, then proved that its third coordinate is the known deterministic
quantity \(\tau_l-1\).  The final dynamic head therefore has two scalars and
computes

\[
\Gamma_{04}^\ell
=\lim_{n\to\infty}\mathbb E\frac1n
 \langle X_0^\ell,X_4^\ell\rangle .
\]

The pre-reduction producer artifacts, frozen before comparison, are

- `FROZEN_GAMMA04_RECURRENCE.json`, SHA-256
  `724da08f11bc3ec71b90ad12305a5e1ebed4f00a2a7e116f99f7d6ce02a401b5`;
- `FROZEN_GAMMA04_TRANSITIONS.md`, SHA-256
  `ce658f1cfdebfeb090fb0fb12dd43801a3ebd0ed8123e8a90244c5a62be4d786`.

The final two-state map is `REDUCED_GAMMA04_RECURRENCE.json`, SHA-256
`32b5ee0f87562b6f15e2139682d9437bd4f691f90ac9ffa495d3efd5ccfc033c`.
It agrees atom-for-atom with the separately frozen Route-S map, SHA-256
`e97a3f6afda6ae17d1be498ac79b308b64fc71e7fd94a1f343e0e28844762122`.

The head has passed Route A's exact finite-width, Wick--Stein,
canonicalization, control, parity, and preregistered nonpolynomial checks.
Canonical promotion remains subject to the final hostile synthesis.

## 1. How to read the existing F^(5) DAG

Let

\[
\widehat X_r^\ell
=\left.\partial_t^rX^\ell(\theta_0+t p_0)\right|_{t=0},
\qquad
X_r^\ell
=\left.\frac{d^r}{ds^r}X^\ell(\theta(s))\right|_{s=0},
\]

be respectively the frozen-line and moving-flow activation jets.  Define
the analogous frozen and moving reverse jets \(\widehat\Delta_r^\ell\) and
\(\Delta_r^\ell\).  The two notions coincide at grades zero and one but not
from grade two onward.

Every sweep contains exactly H nearest-neighbour layer cells.  F1's special
first-layer initialization is precisely its ordinary transition evaluated
on the zero layer-0 state, so it is also one of those H cells.  Within one
sweep, every layer applies the same polynomial template; only b_l,
tau_(l-1), and the stored input state change.  The six templates are not the
same map: F1, R1, F2, R2, F3, and R3 carry successively different jet grades
and alternate directions.

With

\[
d=M_{020000},\qquad b_\ell=d^{H-\ell},\qquad
\tau_\ell=1+d+\cdots+d^\ell,
\]

the chronological dependency is

\[
F1\longrightarrow R1\longrightarrow F2\longrightarrow R2
\longrightarrow F3\longrightarrow R3.
\]

At d=1, b_l=1 and tau_l=l+1 with the present indexing, so the local map can
still depend numerically on l through tau_(l-1)=l and through stored states.

### 1.1 Meaning of all 29 dynamic backbone coordinates

Write \(\langle v,w\rangle_n=n^{-1}v^Tw\).  The letters F_r, E_r, J_r below
denote the centered forward, frozen-reverse, and moving-reverse Gaussian
innovations in the local derivation.  They are semantic aids only; no such
random variable remains in the final recurrence.

| sweep | state | derivative/covariance meaning |
|---|---|---|
| F1 | u | \(\mathbb E\langle\widehat X_0,\widehat X_2\rangle_n\) |
| F1 | v | \(\mathbb E\langle\widehat X_0,\widehat X_4\rangle_n\); this is the frozen-line G_04, not moving Gamma_04 |
| F1 | w | \(\mathbb E\langle X_1,X_1\rangle_n\) |
| F1 | x | \(\mathbb E\langle\widehat X_1,\widehat X_3\rangle_n\) |
| F1 | y | \(\mathbb E\langle\widehat X_2,\widehat X_2\rangle_n\) |
| F1 | j | mean local response \(\mathbb E[\partial_{E_0}\widehat X_3]\) |
| F1 | k | mean local response \(\mathbb E[\partial_{E_0}\widehat X_5]\) |
| R1 | e02 | \(\mathbb E[E_0E_2]\) |
| R1 | e11 | \(\mathbb E[E_1^2]\) |
| R1 | e13 | \(\mathbb E[E_1E_3]\) |
| R1 | e22 | \(\mathbb E[E_2^2]\) |
| R1 | c10 | response in \(\widehat\Delta_1=E_1+c10\,\widehat X_0\) |
| R1 | c21 | response in \(\widehat\Delta_2=E_2+c21\,\widehat X_1\) |
| R1 | c30 | \(\widehat X_0\) response in \(\widehat\Delta_3=E_3+c30\widehat X_0+c32\widehat X_2\) |
| R1 | c32 | \(\widehat X_2\) response in the preceding decomposition |
| F2 | q02 | moving \(\Gamma_{02}=\mathbb E\langle X_0,X_2\rangle_n\) |
| F2 | q22 | moving \(\Gamma_{22}=\mathbb E\langle X_2,X_2\rangle_n\) |
| F2 | qfm | mixed \(\mathbb E\langle\widehat X_2,X_2\rangle_n\) |
| F2 | a2 | mean response \(\mathbb E[\partial_{E_1}X_2]\) |
| R2 | r02 | \(\mathbb E[E_0J_2]\) |
| R2 | r22 | \(\mathbb E[J_2^2]\) |
| R2 | rfm | mixed \(\mathbb E[E_2J_2]\) |
| R2 | d21 | response in \(\Delta_2=J_2+d21\,X_1\) |
| F3 | q13 | moving \(\Gamma_{13}=\mathbb E\langle X_1,X_3\rangle_n\) |
| F3 | a30 | mean response \(\mathbb E[\partial_{E_0}X_3]\) |
| F3 | a32 | mean response \(\mathbb E[\partial_{J_2}X_3]\) |
| R3 | r13 | \(\mathbb E[E_1J_3]\) |
| R3 | d30 | \(X_0\) response in \(\Delta_3=J_3+d30X_0+d32X_2\) |
| R3 | d32 | \(X_2\) response in the preceding decomposition |

The order-three graph is the autonomous projection

\[
(w,u,j;\ e11,c10)\subset(F1,R1).
\]

No higher-grade coordinate feeds this projection.

### 1.2 Reading A_H, B_H, and C_H

The backbone nodes and deterministic terminal accumulators have meanings

\[
\begin{aligned}
S_3&=j_H+3u_H,& S_5&=k_H+5v_H,\\
\mathcal H&=\|\nabla^2f\,p\|^2,&
AC&=\nabla^4f[\nabla^2f\,p,p,p],\\
Bm2&=\langle\nabla^3f[p,p],D^2p\rangle,&
M2&=\|D^2p\|^2,\\
Am3&=\langle\nabla^2f\,p,D^3p\rangle .
\end{aligned}
\]

They are read once at the terminals:

\[
\boxed{
A_H=\tau_H,\quad
B_H=2S_3+4\mathcal H,\quad
C_H=2S_5+10AC+10Bm2+4M2+12Am3.}
\]

Thus A is a backbone scalar, B uses the order-three projection plus one R1
accumulator, and C uses all six sweeps plus four further accumulators.

## 2. Universal-observable principle

The parameter-flow jets

\[
p_0=p,\qquad p_1=Dp,\qquad p_2=D^2p,\qquad p_3=D^3p
\]

depend only on f and the initialization, not on the observable.  For any
\(C^4\) scalar observable O(theta), repeated ordinary differentiation gives
the exact finite-width identities

\[
\begin{aligned}
O'={}&O^{(1)}[p_0],\\
O''={}&O^{(2)}[p_0,p_0]+O^{(1)}[p_1],\\
O'''={}&O^{(3)}[p_0,p_0,p_0]
 +3O^{(2)}[p_0,p_1]+O^{(1)}[p_2],\\
O^{(4)}={}&O^{(4)}[p_0,p_0,p_0,p_0]
 +6O^{(3)}[p_0,p_0,p_1]+3O^{(2)}[p_1,p_1]\\
&+4O^{(2)}[p_0,p_2]+O^{(1)}[p_3].
\end{aligned}
\]

This is the amortization principle: F1/R1/F2/R2/F3/R3 computes a universal
flow backbone once; a new observable supplies only its derivative tensors
contracted against p_0,...,p_3.  A small head may need one more traversal to
peel those contractions, but it does not recompute the parameter jets.

## 3. Hidden squared RMS and RMS

For hidden activation vector X^l(s), define

\[
Q_l(s)=\frac1n\|X^l(s)\|^2,\qquad
R_l(s)=\sqrt{Q_l(s)},
\]

and

\[
\Gamma_{rs}^l
=\lim_{n\to\infty}\mathbb E\frac1n
 \langle X_r^l,X_s^l\rangle .
\]

Leibniz's rule is exact before taking width to infinity:

\[
\frac{d^kQ_l}{ds^k}(0)
=\sum_{r=0}^k{\binom kr}\frac1n
 \langle X_r^l,X_{k-r}^l\rangle .
\]

Consequently, under the stated expectation-limit bridge,

\[
\boxed{Q_l^{(k)}(0)=\sum_{r=0}^k\binom kr\Gamma_{r,k-r}^l.}
\]

The existing-node dictionary is therefore exact:

\[
\Gamma_{11}^l=w_l,\qquad
\Gamma_{02}^l=q02_l,\qquad
\Gamma_{22}^l=q22_l,\qquad
\Gamma_{13}^l=q13_l.
\]

In particular,

\[
Q_l''(0)=2(w_l+q02_l),
\]

and the only missing fourth-order atom is
\(\gamma04_l:=\Gamma_{04}^l\):

\[
\boxed{Q_l^{(4)}(0)=2\gamma04_l+8q13_l+6q22_l.}
\]

At unit Gram, Q_l(0)=R_l(0)=1 and odd annealed derivatives vanish.  Expanding
the square root gives

\[
\boxed{R_l''(0)=w_l+q02_l,}
\]

\[
\boxed{
R_l^{(4)}(0)=\gamma04_l+4q13_l+3q22_l
-3(w_l+q02_l)^2.}
\]

## 4. Exact layer-four schedule and the two-state head

Let A_l(s)=W_l(s)/sqrt(n) for l>=2, with the first-layer Gram-scaled analogue,
and suppress layer labels.  Exact finite-width product differentiation gives

\[
Z_4=A X_4+4A_1X_3+6A_2X_2+4A_3X_1+A_4X_0,
\]

where feature ascent implies, without approximation,

\[
A_a=\sum_{r=0}^{a-1}\binom{a-1}{r}
 \Delta_rX_{a-1-r}^T
\]

with the model's fixed normalization understood.  Thus all ten rank-one
product branches are

\[
\begin{array}{c|l}
A_1&\Delta_0X_0^T\\
A_2&\Delta_1X_0^T+\Delta_0X_1^T\\
A_3&\Delta_2X_0^T+2\Delta_1X_1^T+\Delta_0X_2^T\\
A_4&\Delta_3X_0^T+3\Delta_2X_1^T+3\Delta_1X_2^T+\Delta_0X_3^T.
\end{array}
\]

Grouping every A/A^T transpose-response branch by reverse grade gives

\[
\begin{array}{c|c|c}
\text{reverse jet}&\text{direct coefficient}&\text{after parity}\\\hline
\Delta_0&4\Gamma_{03}+6\Gamma_{12}+4\Gamma_{21}+\Gamma_{30}&0\\
\Delta_1&6\Gamma_{02}+8\Gamma_{11}+3\Gamma_{20}&9\Gamma_{02}+8\Gamma_{11}\\
\Delta_2&4\Gamma_{01}+3\Gamma_{10}&0\\
\Delta_3&\Gamma_{00}&1.
\end{array}
\]

The inherited lower-layer transpose responses add a41 and a43.  Therefore
the fourth preactivation jet has exactly the local form

\[
Z_4=G_4+\lambda_{41}\Delta_1+\lambda_{43}\Delta_3,
\]

\[
\boxed{
\lambda_{41}=9q02_{l-1}+8w_{l-1}+a41_{l-1},\qquad
\lambda_{43}=1+a43_{l-1}.}
\]

There is no surviving grade-zero or grade-two branch.

The activation Bell polynomial is

\[
X_4=\phi^{(4)}Z_1^4+6\phi^{(3)}Z_1^2Z_2
+3\phi''Z_2^2+4\phi''Z_1Z_3+\phi'Z_4.
\]

Define the observable state

\[
(\gamma04_l,a41_l,a43_l)
=\left(
\mathbb E\langle X_0,X_4\rangle_n,
\mathbb E[\partial_{E_1}X_4],
\mathbb E[\partial_{J_3}X_4]
\right).
\]

The derivation state initializes at (0,0,0) below layer one.  Its third
transition is

\[
a43_l=d(1+a43_{l-1}),\qquad a43_0=0.
\]

Thus \(t_l:=1+a43_l\) satisfies \(t_l=1+dt_{l-1}\), \(t_0=1\), and hence

\[
t_l=\tau_l,\qquad l43=1+a43_{l-1}=\tau_{l-1}=l1.
\]

The coordinate a43 is therefore eliminated exactly.  The dynamic state is

\[
\boxed{(\gamma04_l,a41_l)},\qquad (\gamma04_0,a41_0)=(0,0).
\]

Two is the smallest dimension found; no minimality theorem is claimed.
Because it needs stored R3 states, this is exactly one additional bottom-up
sweep after R3.

For a layer transition, all unsuffixed forward states on the right are from
layer l-1, all reverse states are the already stored layer-l values, and

\[
\begin{aligned}
b&=b_l,&l1&=\tau_{l-1},&l2&=1+a2,\\
l30&=4q02+3w+a30,&l32&=1+a32,\\
l41&=9q02+8w+a41,&l43&=l1=\tau_{l-1}.
\end{aligned}
\]

Complete Wick--Stein elimination gives the following literal M-only map.

### a41 transition

```text
a41_next = 3*M002000*l1*q02 + 6*M002000*l2*q02 + 8*M002000*l32*w + 3*M010100*l1*q02 + 3*M010100*l1*w + 6*M010100*l2*q02 + 6*M010100*l2*w + M020000*l41 + 3*M022000*b*l1^2*l2 + 10*M022000*b*l1^2*l32 + 6*M022000*b*l1*l2^2 + 5*M022000*b*l1*l2*l32 + 3*M030100*b*l1^3 + 9*M030100*b*l1^2*l2 + M040000*d32*l1*l2 + 6*M121000*c10*l1*l2 + 6*M121000*c10*l2^2
```

### gamma04 transition

```text
gamma04_next = 3*M002000*q02^2 + 6*M010100*q02^2 + 6*M010100*q02*w + M020000*gamma04 + 6*M022000*b*l1*l2*q02 + 5*M022000*b*l1*l32*q02 + 9*M030100*b*l1^2*q02 + M040000*d32*l1*q02 + 3*M100010*q02^2 + 6*M100010*q02*w + 3*M100010*w^2 + M101000*gamma04 + 4*M101000*q13 + 3*M101000*q22 + 6*M103000*b*l1*l2*q02 + 5*M103000*b*l1*l32*q02 + 3*M103000*b*l2^2*w + 4*M103000*b*l2*l32*w + 18*M111100*b*l1^2*q02 + 12*M111100*b*l1*l2*q02 + 21*M111100*b*l1*l2*w + 10*M111100*b*l1*l32*q02 + 13*M111100*b*l1*l32*w + 9*M120010*b*l1^2*q02 + 9*M120010*b*l1^2*w + 5*M121000*b*l1*l30 + M121000*b*l1*l41 + 6*M121000*c10*l1*q02 + 12*M121000*c10*l2*q02 + 3*M121000*d21*l1*w + 4*M121000*d21*l32*w + 3*M121000*d32*l1*q02 + M121000*d32*l1*w + 3*M121000*e11*l1*l2 + 3*M121000*e11*l2^2 + 3*M121000*l1^2*r02 + 5*M121000*l1*l32*r02 + 9*M123000*b^2*l1^2*l2^2 + 15*M123000*b^2*l1^2*l2*l32 + 27*M131100*b^2*l1^3*l2 + 15*M131100*b^2*l1^3*l32 + 6*M140010*b^2*l1^4 + 3*M141000*b*d21*l1^3 + 5*M141000*b*d21*l1^2*l32 + M141000*b*d32*l1^3 + M141000*b*d32*l1^2*l2 + 3*M202000*c10*l1*q02 + 6*M202000*c10*l2*q02 + 8*M202000*c10*l32*w + 3*M210100*c10*l1*q02 + 3*M210100*c10*l1*w + 6*M210100*c10*l2*q02 + 6*M210100*c10*l2*w + M220000*c10*l41 + M220000*d30*l1 + 3*M222000*b*c10*l1^2*l2 + 10*M222000*b*c10*l1^2*l32 + 6*M222000*b*c10*l1*l2^2 + 5*M222000*b*c10*l1*l2*l32 + 3*M230100*b*c10*l1^3 + 9*M230100*b*c10*l1^2*l2 + M240000*c10*d32*l1*l2 + 3*M321000*c10^2*l1*l2 + 3*M321000*c10^2*l2^2
```

The two outputs have 64 and 17 contracted monomials.  The head itself
uses activation derivatives only through phi^(4); attaching it does not
raise the universal backbone's already audited ceiling phi^(5).

## 5. Equality partitions, width counting, and canonicalization

Before Wick contraction, the local targets have the following complete
innovation-degree census.  Each entry is
`(forward degree, reverse degree): number of local monomials`.

```text
gamma04:
(0,0):3 (0,1):4 (0,2):6 (0,3):2 (0,4):3
(1,0):3 (1,1):7 (1,2):4 (1,3):3
(2,0):5 (2,1):4 (2,2):3 (3,0):1 (3,1):2 (4,0):1

a41:
(0,0):3 (0,1):1 (0,2):2 (1,0):1 (1,1):2 (2,0):2

a43:
(0,0):1
```

This is exhaustive because both innovation degrees are at most four.  For
reverse degree m, every leading equality partition is a perfect pairing:
the counts for m=0,...,4 are 1,0,1,0,3.  For forward degree m, a leg is either
paired to another forward leg or attached to the base Gaussian by Stein;
the complete partial-matching counts are 1,1,2,4,10.  The contraction code
expands every choice of activation factor hit by each Stein derivative.

After the forced A/A^T identifications in Section 4 are extracted, let c be
the number of distinct leading covariance/Stein index blocks merged by an
additional equality partition.  The merged sector loses c free width sums
without gaining a normalization, hence is O(n^(-c)).  Thus all c>=1 sectors
are negative-width and vanish for fixed H under the uniform moment bound.
The c=0 partial-match/pair sectors are exactly the emitted Wick--Stein map.
No positive-width sector exists.  The machine-readable exhaustive ledger is
`EQUALITY_PARTITION_LEDGER.json`.

The producer eliminates reverse innovations first and then the lowest
forward innovation.  An independent canonicalizer instead eliminates the
highest forward innovation first and the highest reverse innovation last.
Before deterministic reduction, the two independent local producers agree
coefficient-by-coefficient on all 83/20/1 monomials.  After independently
substituting l43=l1, Route A and the separately frozen Route-S public map
agree on all 64/17 monomials with zero missing, extra, or unequal
coefficients.

## 6. Readout-reflection parity

Let T flip only the readout.  Since f(Ttheta)=-f(theta), orthogonality of T
gives

\[
p(T\theta)=-T p(\theta).
\]

If theta(s) solves feature ascent from theta_0, then Ttheta(-s) solves it
from Ttheta_0.  Hidden features are invariant under T itself, so

\[
X^l_{T\theta_0}(s)=X^l_{\theta_0}(-s),\qquad
X^l_r(T\theta_0)=(-1)^rX^l_r(\theta_0).
\]

The initialization law is T-invariant.  Therefore every annealed
Gamma_rs with r+s odd vanishes, as do all odd feature-ascent derivatives of
Q_l and R_l.  The finite-width oracle verifies the stronger seedwise jet
transformation before expectation.

## 7. Exact MSE time change

For one-sample, label-1 MSE, set c=2eta.  Along the same feature-ascent
trajectory,

\[
\frac{ds}{dt}=c(1-F(s)).
\]

With F'(0)=A_H, F'''(0)=B_H and even F derivatives zero, direct
differentiation gives

\[
s_1=c,\quad s_2=-c^2A_H,\quad s_3=c^3A_H^2,
\quad s_4=-c^4(A_H^3+B_H).
\]

Let q_2=Q_l''(0) and q_4=Q_l^(4)(0).  Faà di Bruno's formula then yields

\[
\boxed{Q_t''(0)=c^2q_2,}
\]

\[
\boxed{Q_t'''(0)=-3c^3A_Hq_2,}
\]

\[
\boxed{Q_t^{(4)}(0)=c^4(q_4+7A_H^2q_2),}
\]

\[
\boxed{
Q_t^{(5)}(0)=-5c^5\left[(3A_H^3+B_H)q_2+2A_Hq_4\right].}
\]

An exact rational ordinary-series audit independently reproduces all four
coefficients.

## 8. Audits and controls

### 8.1 Exact finite width

The ordinary-series feature-flow implementation and a separate raw
multivariate parameter Taylor algebra agree seedwise on every Q_l
derivative through order four for

\[
(H,n)=(1,1),(1,2),(2,1),(2,2),(3,1)
\]

with a generic quartic activation.  This comparison differentiates the raw
network by D=n grad(f).grad and does not use the population recurrence.

### 8.2 Exact moment controls at H=2

The following are exact rational specializations of the contracted map.

| activation | layer | Gamma04 | Q'' | Q^(4) | R'' | R^(4) |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 1,2 | 0 | 0 | 0 | 0 | 0 |
| x | 1 | 17 | 6 | 96 | 3 | 21 |
| x | 2 | 53 | 18 | 528 | 9 | 21 |
| (3+4x)/5 | 1 | 1581824/390625 | 33792/15625 | 172045824/9765625 | 16896/15625 | 1294148352/244140625 |
| (3+4x)/5 | 2 | 103905536/9765625 | 2221344/390625 | 3705931776/48828125 | 1110672/390625 | 2089741525248/152587890625 |

The constant control kills every head state.  The affine activation is a
genuine unit-Gram control.

### 8.3 Preregistered smooth nonpolynomial regression

For normalized sine and H=2, the frozen prediction at the second hidden
layer is

\[
Q_2^{(4)}(0)=-2454.0373996768317,
\qquad \Gamma_{04}^2=1521.9148073719157.
\]

The preregistered 8,000-network experiment at widths 32,64,128,256 passed:
the primary Q^(4) intercept had z=-1.140 and affine-fit goodness p=0.110.
The Gamma04 secondary intercept had z=0.715 and p=0.463.  This is empirical
support only.  Raw data and hashes are in
`NORMALIZED_SINE_GAMMA04_RESULT.json` and
`NORMALIZED_SINE_GAMMA04_RAW.npz`.

## 9. Probability and regularity boundary

The exact finite-width Q identities require X(s) to be four times
differentiable and the displayed random variables integrable.  The formal
head contraction uses only phi through phi^(4).  A convenient sufficient
theorem boundary for the head attached to the full order-five backbone is:

1. H is separately fixed before n tends to infinity;
2. phi is C-infinity and every derivative has polynomial growth;
3. the finite tensor program converges in every finite L^p.

For a weaker route, it is enough to prove the required convergence in
probability and, for some epsilon>0,

\[
\sup_n\mathbb E
\left|\frac1n\langle X_r^l,X_s^l\rangle\right|^{1+\epsilon}<\infty
\]

for (r,s) in {(1,1),(0,2),(2,2),(1,3),(0,4)}, together with the analogous
UI bounds for the output coefficients A_H and B_H used by the time change.
These hypotheses justify taking annealed expectations and do not cover
H=H(n), positive training intervals, or an all-orders expansion.

## 10. Amortized architecture and cost

The resulting architecture is:

1. one reusable F1/R1/F2/R2/F3/R3 feature-ascent backbone;
2. an output head reading A_H,B_H,C_H;
3. a kernel head forming the local K(y) coefficients;
4. a loss head applying the label-dependent scalar time change;
5. hidden-activation Q/R heads using the two-state Gamma04 sweep;
6. separate preactivation-RMS heads that would read Z_r rather than X_r.

The 29 backbone states are universal.  Gamma04,a41 and the Q/R terminal
arithmetic are observable-specific; a43 is a derived tau value, not dynamic
state.  A head for one chosen layer can stop
after that layer, costing O(l) scalar cells after the O(H) backbone.  The
same forward head sweep emits all H layer RMS derivatives in O(H) time;
retaining every output costs O(H) storage instead of O(1).  It is not H
independent O(H) sweeps.

A preactivation RMS P_l=n^(-1)||Z_l||^2 reuses the same parameter jets and
the local Z_r Bell schedule, but its own contracted head has not been
constructed or audited here.  It must not be identified with the activation
RMS head by deleting phi factors informally.

## 11. F^(7) roadmap only

Route A investigated, but does not promote, the following possibilities:

- grade triangularity suggests the F^(5) graph should embed unchanged;
- moving grades four and five suggest possible new F4/R4 and F5/R5 passes;
- raw differential order suggests, but does not prove after peeling, a
  terminal derivative ceiling phi^(7);
- a center-canonicalized free-tree growth calculation finds 23 shapes for
  D^7f and reproduces the exact F^(5) coefficient multiset
  {2,14,16,22,30,36};
- fixed-dimensional M-only closure and O(H) factored complexity remain open.

The tree evidence is stored in `F7_TREE_ROADMAP_ROUTE_A.json`.  It lacks an
independent tree canonicalization, an explicit rank-labelled 23-family
tensor identity, equality/transpose audits, and any F7 scalar recurrence.
Therefore the count 23, sweep count, state dimension, phi^(7) ceiling, fixed
closure, and O(H) complexity are all roadmap hypotheses, not results.

## 12. Claim levels

- Exact finite-width: the observable chain rule, Q Leibniz identity, k=4
  layer schedule, readout equivariance, and MSE time change.
- Formal Gaussian normal form: the three displayed M-only transitions.
- Route-A algebraically audited: alternate atom canonicalization, complete
  local partition ledger, seedwise raw-AD comparison, and exact controls.
- Empirical: the normalized-sine regression.
- Theorem-level annealed result: conditional on the fixed-depth convergence
  and UI bridge in Section 9, and pending the external mandatory audit before
  canonical promotion.

Run the independent checks with

```bash
python -m studies.mean_field_peeling.generic_first_stieltjes.depth_order5_scalar.multi_observable.independent_route_a.run_checks
```

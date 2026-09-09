# Width-first order-five artifact audit

Date: 25 August 2026.

## Bottom line

There is already a positive arbitrary-activation result at the level of the
**exact local fifth coefficient**, stronger than the near-identity program had
recorded.  For every separately fixed hidden depth (L), let

\[
 \Delta_{t,L}(h)=F_{2t,L}(h)-F_{t,L}(2h).
\]

Under the normalized weighted-(C^{12}) activation assumptions of
`temporary_depth_time_doubling/PROOF.md`, there are five explicit,
activation-and-depth-only Gaussian-compiler numbers
\(\Theta_{5,1},\ldots,\Theta_{5,5}\) such that

\[
 \boxed{
 [h^5]\Delta_{t,L}(h)
 =\sum_{m=1}^5 d_{5,m}(t)\Theta_{5,m},}
 \tag{1}
\]

where

\[
\begin{aligned}
d_{5,1}(t)&=-30t,\\
d_{5,2}(t)&=t(15-14t),\\
d_{5,3}(t)&=-2t(t-1)(2t-5),\\
d_{5,4}(t)&={t(t-1)\over6}(-4t^2+32t-45),\\
d_{5,5}(t)&={t(t-1)(t-2)\over3}(4t-9).
\end{aligned}
\tag{2}
\]

Thus the fifth coefficient is an exact polynomial of degree at most four in
(t), at (L=2), (L=3), and every other separately fixed (L).  This is a
local coefficient theorem, not the still-open horizon-uniform finite-(h)
remainder theorem.

## 1. Noncircular Gaussian-integral constants

Let \(\mathcal J^{\rm PJ}_{5,j,L}(\phi)\) be the signed singular-Price
compiler output at horizon (j), constructed before it is identified with an
output derivative, and put

\[
 q_{j,L}(\phi)={\mathcal J^{\rm PJ}_{5,j,L}(\phi)\over120},
 \qquad q_{0,L}=0.
 \tag{3}
\]

Define the Newton coefficients using only the five fixed horizons
(j=1,\ldots,5):

\[
 \boxed{
 \Theta_{5,m}(\phi,L)
 =\sum_{j=0}^m(-1)^{m-j}{m\choose j}q_{j,L}(\phi),
 \qquad1\le m\le5.}
 \tag{4}
\]

These are not output-defined constants.  Each \(\mathcal J^{\rm PJ}_{5,j,L}\)
is a terminating chronological Gaussian recursion; at the coalesced
covariance it is a finite sum of products of one-dimensional atoms of the
form

\[
 \mathbb E\!\left[G^a\prod_{r=0}^{12}
                   \phi^{(r)}(G)^{\beta_r}\right].
 \tag{5}
\]

The order-five marked temporal/static intertwining gives the Newton identity

\[
 [h^5]F_{N,L}(h)=\sum_{m=1}^5{N\choose m}\Theta_{5,m}.
 \tag{6}
\]

Substituting (N=2t) and (N=t), with the chain factor (2^5=32), gives
(1)--(2).  Equivalently,

\[
 \Delta_{t,L}^{(5)}(0)
 =120\sum_{m=1}^5d_{5,m}(t)\Theta_{5,m}.
 \tag{7}
\]

## 2. An explicit quartic bound

For every integer (t\ge1), direct inspection of (2) gives

\[
\begin{array}{c|ccccc}
m&1&2&3&4&5\\ \hline
|d_{5,m}(t)|/t^4
&\le30&\le14&\le4&\le2/3&\le4/3.
\end{array}
\tag{8}
\]

For (m=4), handle (t=1,\ldots,6) directly and use
\(|-4t^2+32t-45|\le4t^2\) for (t\ge7); the other bounds are immediate
from the factored formulas.  Therefore the explicit Gaussian-integral
constant

\[
 \boxed{
 C^{\rm loc}_{\phi,L}
 =30|\Theta_{5,1}|+14|\Theta_{5,2}|+4|\Theta_{5,3}|
  +{2\over3}|\Theta_{5,4}|+{4\over3}|\Theta_{5,5}|}
 \tag{9}
\]

satisfies

\[
 \boxed{|[h^5]\Delta_{t,L}(h)|
 \le C^{\rm loc}_{\phi,L}t^4\qquad(t\ge1).}
 \tag{10}
\]

There is also a completely numerical envelope.  With
(B_\phi=\max\{4,M_\phi\}\), the proved compiler estimate and horizon
monotonicity give

\[
 |q_{j,L}|\le {B_\phi^{E_{L,5}}\over120},
 \qquad1\le j\le5,
\]

so (4) gives

\[
 |\Theta_{5,m}|\le(2^m-1){B_\phi^{E_{L,5}}\over120}.
\]

Substitution in (9) yields the explicit uniform coefficient bound

\[
 \boxed{
 |[h^5]\Delta_{t,L}(h)|
 \le {227\over180}B_\phi^{E_{L,5}}t^4.}
 \tag{11}
\]

For (L\ge2), the exact numerical exponent is

\[
 E_{L,5}=2L\,p_5^{11(L-1)}
 +r_5{p_5^{11(L-1)}-1\over p_5-1},
 \tag{12}
\]

where (p_5,r_5) are the terminating numerical recursions in
`COMPILER_DEPTH_TIME.md`, (5.1)--(5.5).  In particular the powers in (12)
are (11) at (L=2) and (22) at (L=3).  The constant is extremely
coarse, but it is independent of (t), explicit, and noncircular.

For the normalized residual class

\[
 \psi_{\alpha,\varphi}(x)
 ={x+\alpha\varphi(x)\over\|G+\alpha\varphi(G)\|_2},
 \qquad
 \max_{0\le r\le12}\|\varphi^{(r)}\|_\infty\le R,
 \quad |\alpha|R\le\tfrac14,
\]

one has \(3/4\le\|G+\alpha\varphi(G)\|_2\), and hence

\[
 M_{\psi_{\alpha,\varphi}}\le {5\over3},
 \qquad B_{\psi_{\alpha,\varphi}}=4.
\]

Thus (11) is uniform over this genuine nonlinear class:

\[
 |[h^5]\Delta^{(\alpha)}_{t,L}(h)|
 \le {227\over180}4^{E_{L,5}}t^4.
 \tag{13}
\]

No small-(\alpha) continuity argument is needed for this coefficient-level
result.

## 3. What `generic_first_stieltjes` contributes

The arbitrary-fixed-depth scalar recurrence there proves

\[
 C_L=\lim_{n\to\infty}\mathbb E[D_n^5f_n]
\]

as an explicit polynomial in the one-dimensional atoms

\[
 M_{\nu_0\ldots\nu_5}
 =\mathbb E\prod_{r=0}^5\phi^{(r)}(G)^{\nu_r}.
\]

In the composition notation above,

\[
 \boxed{C_L=\Theta_{5,5}.}
 \tag{14}
\]

Indeed, the only ordered composition of (5) into five positive parts is
(1+1+1+1+1), and (A_1=D_n).  The identity control confirms the
normalization: at (L=2), both calculations give
(\Theta_{5,5}=C_2=1464).

This is highly relevant but not sufficient by itself for the time-doubling
coefficient: (1) also needs \(\Theta_{5,1},\ldots,\Theta_{5,4}\).  In
particular the leading quartic coefficient is

\[
 [t^4h^5]\Delta_{t,L}
 ={4\Theta_{5,5}-2\Theta_{5,4}\over3}.
 \tag{15}
\]

The fixed-horizon Price compiler supplies the four missing constants via
(3)--(4), although not in the compact flattened \(M_\nu\)-only form achieved
for \(\Theta_{5,5}\) by `generic_first_stieltjes`.

## 4. Sign and limit-order audit

The orientation in this note is

\[
 \Delta_{t,L}=F_{2t,L}(h)-F_{t,L}(2h).
\]

Its cubic coefficient is

\[
 [h^3]\Delta_{t,L}
 ={t(2t-1)\over2}J_{\phi,L}.
\]

The opposite convention used in `temporary_depth_time_doubling`,

\[
 D_{t,L}=F_{t,L}(2h)-F_{2t,L}(h)=-\Delta_{t,L},
\]

has both cubic and fifth coefficients negated.  For the identity activation
at (L=2), the audited check is

\[
 [h^5]D_{t,2}
 =-{2452\over3}t^4+1896t^3-{4403\over3}t^2+369t,
\]

so

\[
 [h^5]\Delta_{t,2}
 ={2452\over3}t^4-1896t^3+{4403\over3}t^2-369t.
\]

The limit order is the required one throughout:

1. take (n\to\infty) at each fixed finite (N,L,h\ne0);
2. identify the width-first inverse-free Gaussian DAG;
3. extend and differentiate that DAG at (h=0) using singular Price;
4. only then form the coefficient and its time polynomial.

No finite-width Taylor coefficient is passed through the width limit.

## 5. Hostile boundary

The order-five marked proof is algebraic at a fixed finite truncation.  To
make its bookkeeping explicit at order five one uses

\[
 \mathbb R[z]/(z)^6,\qquad
 \mathcal T_r\ (0\le r\le5),\qquad
 \mathcal G_r\ (0\le r\le4),
\]

and repeats the chronological multiindex/naturality induction for
(|\alpha|\le5\).  The product, activation, Gram, response-convolution, and
singular-quotient identities used in the order-three proof are independent of
the cutoff.  The (C^{12}) budget is exactly the already audited fifth-Price
budget.  This closes a minor bookkeeping omission in the phrase “replace
every upper bound three by five” in the source; no horizon-uniform estimate is
introduced.

What (1)--(13) do **not** prove is

\[
 |\Delta_{t,L}(h)-[h^3]\Delta_{t,L}\,h^3|
 \le C_{\phi,L}t^4|h|^5,
 \qquad |h|\le c_{\phi,L}/t,
\]

at (L=2) or (L=3).  That statement controls the fifth derivative on a
whole (t)-dependent interval, not only its value at zero.  The independent
uniform audit still records: (L=1) proved, (L=2) open, (L=3) open.

## 6. Primary source ledger

- Width-first theorem, activation class, fixed-((L,t)) remainder, and limit
  order: `temporary_depth_time_doubling/PROOF.md`, lines 5--35, 133--164,
  647--740, 916--962, and 979--1010.
- Explicit fixed-horizon exponent: `temporary_depth_time_doubling/
  COMPILER_DEPTH_TIME.md`, lines 377--555 and 735--831; hostile pass in
  `AUDIT_COMPILER.md`, lines 203--227 and 229--273.
- Exact degree-four fifth coefficient: `temporary_general_depth_general_time_
  stepdoubling_bound/CUBIC_MARKED_BRIDGE.md`, lines 1383--1427, and
  `ABSTRACT_STEP_DOUBLING.md`, lines 146--166 and 223--236.  The scoped status
  is recorded in its `EVIDENCE_LEDGER.md`, lines 38--54.
- Generic flattened fifth-flow coefficient: `generic_first_stieltjes/
  depth_order5_scalar/ARBITRARY_DEPTH_B1_ORDER5_SCALAR_RECURRENCE.md`, lines
  1--38 and 528--576; theorem boundary in its `EVIDENCE_LEDGER.md`, lines
  6--15 and 57--75.
- Exact identity (L=2) sign check: `temporary_general_time_doubling/
  LINEAR_ACTIVATION_AUDIT.md`, lines 255--325.
- Uniform-remainder boundary: `temporary_depth_time_doubling/
  AUDIT_UNIFORM_L23.md`, lines 30--42 and 82--91.


# A full two-hidden-layer bounded-slope counterexample

## 1. The theorem and the object being falsified

For the `q=1`, two-hidden-layer network, let

\[
 \Delta_1^\phi(h)=F_2^\phi(h)-F_1^\phi(2h),
 \qquad
 {cal C}_\phi(1,r;\kappa)
 =\sup_{0<|h|\le r}
 { |\Delta_1^\phi(h)-\kappa h^3|\over |h|^5}.
 \tag{1.1}
\]

Here each `F_k` is the width-first limit at the displayed fixed nonzero
step, not a finite-width Taylor polynomial.

### Theorem 1.1

There is an RMS-normalized activation

\[
 \phi\in C^\infty(\mathbb R),\qquad
 0<c\le \phi'(x)\le C<\infty,\qquad
 |\phi(x)|\le C(1+|x|),                         \tag{1.2}
\]

for which the one- and two-step width-first expected outputs exist and are
finite for every fixed `h`, but

\[
 \boxed{
 {cal C}_\phi(1,r;\kappa)=\infty
 \quad\hbox{for every }r>0\hbox{ and every }\kappa\in\mathbb R.}
 \tag{1.3}
\]

Thus linear growth does not imply a finite uniform fifth-remainder
coefficient.  The failure already occurs at the first coarse/fine pair; it
is stronger than growth faster than any finite power of the horizon.

The theorem does **not** contradict the temporal fifth-jet identity.  Every
finite truncation used below has a perfectly finite fifth jet, and for every
activation for which the final fifth jet exists the paired coefficient is
quartic in the horizon.  The final activation in Theorem 1.1 has no finite
uniform fifth remainder at the origin.

## 2. Exact network and an activation metric

At width `n`, initialize all `a_i,W_ij,u_j` as mutually independent standard
Gaussians and put

\[
 H_j=\psi(u_j),\qquad
 z_i={1\over\sqrt n}\sum_jW_{ij}H_j,qquad
 f_n={1\over n}\sum_i a_i\psi(z_i).             \tag{2.1}
\]

One simultaneous ascent step of size `h` is

\[
\begin{aligned}
 a_i^+&=a_i+h\psi(z_i),\\
 W_{ij}^+&=W_{ij}+{h\over\sqrt n}
              a_i\psi'(z_i)H_j,\\
 u_j^+&=u_j+h b_j\psi'(u_j),\qquad
 b_j={1\over\sqrt n}\sum_iW_{ij}a_i\psi'(z_i).
\end{aligned}                                  \tag{2.2}
\]

For linearly growing `C^1` activations define

\[
 d_1(\psi,\widetilde\psi)
 =\sup_x{|\psi(x)-\widetilde\psi(x)|\over1+|x|}
  +\|\psi'-\widetilde\psi'\|_\infty .          \tag{2.3}
\]

### Lemma 2.1 (fixed-schedule uniform approximation)

Fix a `C^2` activation `psi` with bounded first two derivatives and at most
linear growth, a finite number `k` of steps, and a compact step interval
`|h|<=R`.  There are `epsilon>0` and `C<infinity`, depending only on this
fixed activation, `k`, and `R`, such that every `C^1` activation
`tilde psi` satisfying

\[
 d_1(\psi,\widetilde\psi)\le\varepsilon,
 \qquad \|\widetilde\psi'\|_\infty
 \le1+\|\psi'\|_\infty                         \tag{2.4}
\]

obeys

\[
 \sup_{n\ge1}\sup_{|h|\le R}
 \mathbb E|f_{k,n}^{\widetilde\psi}(h)
              -f_{k,n}^{\psi}(h)|
 \le C d_1(\psi,\widetilde\psi).               \tag{2.5}
\]

#### Proof

Use the normalized vector norm
`||x||_n^2=n^{-1}sum_i x_i^2` and put
`M=W/sqrt(n)`.  From (2.2),

\[
 \|M^+\|_{op}\le\|M\|_{op}
   +|h|\|a\psi'(z)\|_n\|\psi(u)\|_n.           \tag{2.6}
\]

The linear-growth and slope bounds therefore give, at each of the finitely
many steps, a deterministic polynomial bound in

\[
 1+\|a^0\|_n+\|u^0\|_n+\|M^0\|_{op}.           \tag{2.7}
\]

The polynomial and its degree depend only on `(psi,k,R)`.  All moments of
(2.7) are bounded uniformly in `n`: the two normalized Gaussian vector
norms have uniformly bounded moments, and the Gaussian matrix estimate

\[
 \sup_n\mathbb E\|W/\sqrt n\|_{op}^p<\infty
 \quad(p<\infty)                                \tag{2.8}
\]

follows, for example, from the standard `1/2`-net proof of the Gaussian
operator-norm tail bound.

Couple the two networks with the same initialization.  At an activation
node use

\[
\begin{aligned}
 \|\widetilde\psi(x)-\psi(y)\|_n
 &\le L\|x-y\|_n
 +d_1(\psi,\widetilde\psi)(1+\|y\|_n),\\
 \|\widetilde\psi'(x)-\psi'(y)\|_n
 &\le d_1(\psi,\widetilde\psi)
       +\|\psi''\|_\infty\|x-y\|_n,
\end{aligned}                                   \tag{2.9}
\]

where `L=1+||psi'||_infinity`.  Matrix-vector products are bounded by the
operator norm and a rank-one update by the product of its two normalized
vector norms.  Substitution into (2.2), followed by induction over the
finite schedule, bounds every state difference and the terminal output
difference by

\[
 d_1(\psi,\widetilde\psi)P(1+\|a^0\|_n
 +\|u^0\|_n+\|M^0\|_{op})                       \tag{2.10}
\]

for another fixed polynomial `P`.  Take expectations and use (2.8).
This proves (2.5).  Notice that no bound on
`||tilde psi''||_infinity` was used. `square`

An immediate consequence will be used repeatedly.  If `psi_N` are smooth
bounded-derivative activations with known width-first limits and
`psi_N -> psi` in `d_1`, with the tails chosen so that the right side of
(2.5) tends to zero, then the exact finite-width outputs for `psi` have the
same iterated limit.  This is a uniform-in-width three-epsilon argument,
not an exchange of a width limit with a learning-rate Taylor expansion.

## 3. The universal paired fifth tensor

Let `f` be `C^5` on a finite-dimensional Euclidean space and `g=grad f`.
Write `H,T,U,V` for its derivatives of orders two through five, with one
index raised when the result is used as a vector.  Two fine Euler steps give

\[
\begin{aligned}
 E_h^2\theta-\theta={}&2hg+h^2Hg+{h^3\over2}T[g,g]
 +{h^4\over6}U[g,g,g]+{h^5\over24}V[g,g,g,g]+O(h^6).
\end{aligned}                                   \tag{3.1}
\]

Taylor expansion of the terminal observable, followed by subtraction of
the one coarse step, gives the exact fifth coefficient

\[
\boxed{
\begin{aligned}
 \mathfrak B_5(f)={}&{1\over24}V[g,g,g,g,g]
 +{5\over3}U[Hg,g,g,g]
 +T[T[g,g],g,g]\\
 &+{1\over2}T[H^2g,g,g]+T[Hg,Hg,g].
\end{aligned}}                                  \tag{3.2}
\]

Indeed, the order-five terms of `f(theta+delta)` are

\[
 Df[v_5]+H[v_1,v_4]+H[v_2,v_3]
 +\tfrac12T[v_1,v_1,v_3]+\tfrac12T[v_1,v_2,v_2]
 +\tfrac16U[v_1,v_1,v_1,v_2]+\tfrac1{120}V[v_1^5],
\]

with `v_1=2g`, `v_2=Hg`, `v_3=T[g,g]/2`,
`v_4=U[g,g,g]/6`, and `v_5=V[g,g,g,g]/24`.
Collecting coefficients and subtracting `V[(2g)^5]/120` proves (3.2).

The same identity holds with a constant positive metric by whitening the
coordinates.  For (2.2) that metric is the factor `n` multiplying the raw
Euclidean gradient.

## 4. Principal single-node lemma

Let one activation node have preactivation `x(theta)`, activation value
`y=Phi(x)`, and downstream derivative

\[
 r={\partial f\over\partial y}.
\]

Let `G` be the constant gradient metric, and, before inserting a new narrow
transition, put

\[
 \ell=\nabla x,qquad s=\ell^TG\ell,qquad
 v=\ell^TG\nabla f.                             \tag{4.1}
\]

Choose `rho in C_c^infinity((-1/4,1/4))`, `rho>=0`,
`int rho=1`, and set `R(y)=int_{-infinity}^y rho`.  On a neighborhood of
`X`, replace the old constant slope `b` by

\[
 \Phi'(x)=b+\delta R((x-X)/w).                  \tag{4.2}
\]

### Lemma 4.1 (negative principal symbol)

In the integral of (3.2), the part of scale `delta^2 w^{-3}` for which all
singular activation derivatives occur at this one node is

\[
 \boxed{
 -{11\over24}\,r^2s v^4\,
 {\delta^2\over w^3}\int_{\mathbb R}(\rho')^2.}
 \tag{4.3}
\]

Here `r,s,v` are frozen at the left affine slope.  In particular the
coefficient is nonpositive, independently of every sign in the network.

#### Proof

The principal part of the `k`th derivative tensor at this node is

\[
 r\Phi^{(k)}(x)\ell^{\otimes k}.                \tag{4.4}
\]

Changing the slope by `delta R` changes the velocity in (4.1) by
`r s delta R`.  At quadratic amplitude and total singular weight four, the
first three terms in (3.2) and the first-order variation of its `V` term
give, after writing `g_0=b`,

\[
 r^2sv^4{\delta^2\over w^4}
 \left\{
 {5\over24}R\rho'''
 +{5\over3}\rho\rho''+(\rho')^2
 \right\}.                                     \tag{4.5}
\]

The last two terms of (3.2) contain at least three singular factors at
weight four, or have singular weight at most three, and hence do not enter
the quadratic principal part.  Integrating (4.5), using

\[
 \int R\rho'''=\int(\rho')^2,
 \qquad \int\rho\rho''=-\int(\rho')^2,
\]

gives

\[
 {5\over24}-{5\over3}+1=-{11\over24}.
\]

The change of variables `x=X+wy` supplies the remaining factor `w`, proving
(4.3). `square`

Terms involving two distinct transition nodes are smaller by at least one
power of `w`: the total singular weight in (3.2) is at most four, whereas
two independent transition integrations supply `w^2`.  Terms in which a
derivative hits `r`, `ell`, or another smooth network factor also lose at
least one unit of singular weight.  This proves that (4.3), summed over
activation nodes, is the complete `w^{-3}` quadratic sector.

## 5. The sector survives the width limit

Apply Lemma 4.1 at initialization to the lower nodes of (2.1).  With

\[
 C_i=a_i\psi'(z_i),\qquad
 b_j={1\over\sqrt n}\sum_iW_{ij}C_i,
\]

one has exactly

\[
 r_j={\partial f_n\over\partial H_j}={b_j\over n},
 \qquad s_j=n,
 \qquad v_j=b_j b                              \tag{5.1}
\]

on a region where the old lower slope is `b`.  Therefore the lower-node
weight in (4.3) is

\[
 \sum_{j=1}^n r_j^2s_jv_j^4
 ={b^4\over n}\sum_{j=1}^n b_j^6.              \tag{5.2}
\]

For every fixed smooth bounded-derivative background in a sufficiently
small `d_1` neighborhood of the identity, the initialization cavity law
gives, conditionally on `u_j=X`,

\[
 b_j\Longrightarrow B\sim N(0,d),\qquad
 d=\mathbb E\psi'(G)^2>0,                       \tag{5.3}
\]

and the twelfth-moment bound needed for uniform integrability follows from
bounded `psi'` and Gaussian Wick expansion.  Consequently

\[
 \lim_{n\to\infty}\mathbb E\left[
 {1\over n}\sum_jb_j^6\mid u_j=X\right]
 =\mathbb EB^6=15d^3.                           \tag{5.4}
\]

The top-node contribution has the same sign by Lemma 4.1 and may be
discarded in an upper estimate.  Since both initialization preactivations
have standard-normal marginal after RMS normalization, (4.3)--(5.4) imply
the following finite-diagram asymptotic for the width-first fifth
coefficient `beta=[h^5]Delta_1` when a new transition is inserted at `X`:

\[
 \beta_{\delta,w,X}-\beta_0
 \le -{55\over8}d^3b^4\gamma(X)
 {\delta^2\over w^3}\int(\rho')^2
 +\operatorname{Rem}_{\delta,w,X}.             \tag{5.5}
\]

We record the structural estimate which makes the word "finite" in the
preceding sentence quantitative.  Every monomial produced from (3.2) by
the two-layer chain rule is a product of one-coordinate Gaussian atoms

\[
 \mathbb E\prod_{r=0}^5\psi^{(r)}(G)^{\nu_r}.   \tag{5.6}
\]

If

\[
 e(\nu)=\sum_{r=2}^5(r-1)\nu_r                 \tag{5.7}
\]

is its singular excess, the sum of the excesses in a monomial is at most
four.  This follows directly, term by term, from (3.2): `V` has excess at
most four, `U H` at most `3+1`, `T T` at most `2+2`, and `T H H` at most
`2+1+1`.  Faa di Bruno only partitions these integers and cannot increase
their sum.

On the new transition, a factor `psi^(r)`, `r>=2`, is bounded by
`C delta w^(1-r)`, and integration over its support contributes
`C P(X) gamma(X) w`.  Therefore a block containing `k` new-transition
derivative factors and excess `e` is bounded by

\[
 C P(X)\delta^k\gamma(X)w^{1-e}.                \tag{5.8}
\]

There are only four exceptional cases to classify.

1. If `e<=3`, division by the principal scale
   `delta^2 gamma(X)w^(-3)` gives
   `C P(X) delta^(k-2)w^(4-e)`.
2. If `e=4` and `k>=3`, the ratio is at most `C delta`.
3. If `e=4`, `k=2`, and the two factors occur at distinct neuron nodes,
   two Gaussian integrations supply `w^2`; its ratio is
   `O(P(X)gamma(X)w)`.
4. If `e=4`, `k=1`, the only possible top derivative is a single fifth
   activation derivative.  Three integrations by parts, equivalently the
   identities `int rho'''=int y rho'''=int y^2 rho'''=0`, remove its
   apparent `w^(-3)` scale.  A second factor `R` at the same node is exactly
   the quadratic term already retained in (4.5).

The change on the permanent right tail of the slope step is at most
`C delta P(X) gamma([X-1,infinity))`.  Products of several atoms do not
alter these estimates: all atoms not containing the new transition are
fixed finite constants, and at most one atom can carry the single-node
principal sector.  It follows that, with

\[
 w=\delta\sqrt{\gamma(X)},                     \tag{5.9}
\]

the complete remainder satisfies

\[
 { |\operatorname{Rem}_{\delta,w,X}| 
  \over \gamma(X)\delta^2w^{-3}}
 \le C\{\delta+P(X)\sqrt{\gamma(X)}\}.          \tag{5.10}
\]

The Gaussian density ratio on the transition is harmless because
`Xw -> 0`; its Taylor remainder is included in the polynomial in (5.10).
This proves the claimed finite-diagram bound without taking an absolute
value before the cancellation in (4.5).

Similarly the complete cubic formula gives

\[
 |\kappa_{\delta,w,X}-\kappa_0|
 \le C P(X)\left({\delta^2\gamma(X)\over w}
       +\delta\,\gamma([X-1,\infty))\right).    \tag{5.11}
\]

The principal cubic terms are
`(1/2)Phi'''(Phi')^3+2(Phi'')^2(Phi')^2`;
their quadratic integral is a finite multiple of
`delta^2 gamma(X)/w`.  Every other cubic diagram has lower singular weight,
which proves (5.11) by the same excess count, now with maximum excess two.

By taking `X` large enough that `P(X)sqrt(gamma(X))` is small and then
`delta` small, (5.5) and (5.9)--(5.11) give

\[
 \beta_{\delta,w,X}-\beta_0\longrightarrow-\infty,
 \qquad
 \kappa_{\delta,w,X}-\kappa_0\longrightarrow0. \tag{5.12}
\]

The normalization factor changes by `o(1)` and stays in a fixed compact
subset of `(0,infinity)`; it therefore only multiplies the strictly
negative principal coefficient by a bounded positive factor.  Equations
(5.5)--(5.12) remain valid after RMS normalization.

## 6. Diagonal construction and the nonlocal conclusion

Choose the bump `rho` from Section 4.  Recursively choose disjoint centers
`X_N -> infinity`, amplitudes `delta_N>0`, and widths

\[
 w_N=\delta_N\sqrt{\gamma(X_N)}                 \tag{6.1}
\]

and define

\[
 g_N(x)=1+\sum_{m\le N}\delta_m
 R((x-X_m)/w_m),\qquad
 \Phi_N(x)=\int_0^xg_N(y)dy,qquad
 \psi_N={\Phi_N\over\|\Phi_N(G)\|_2}.          \tag{6.2}
\]

At stage `N`, first choose `X_N` and then `delta_N` so small that

\[
 \beta(\psi_N)\le-N,
 \qquad
 |\kappa(\psi_N)-\kappa(\psi_{N-1})|\le e_N,    \tag{6.3}
\]

This is possible by (5.12).  Also impose `delta_N<=2^(-N-4)` and all
finitely many amplitude ceilings created at earlier stages.  The number
`e_N` is not chosen in advance: after `h_1,...,h_(N-1)` exist, require

\[
 e_N\le2^{-N-2}\min_{j<N}h_j^2,                 \tag{6.3a}
\]

with the empty minimum equal to one.  Then automatically
`sum_(m>N)e_m<=h_N^2/2` after the same rule is imposed at later stages.

With `psi_N` fixed, its bounded derivatives and the established
width-first order-five theorem give

\[
 \Delta_1^{\psi_N}(h)
 =\kappa(\psi_N)h^3+\beta(\psi_N)h^5+o(h^5).
\]

Choose `h_N>0` so that

\[
 h_N<N^{-1},\qquad
 |\beta(\psi_N)|h_N^2\le N^{-1},                \tag{6.4}
\]

and

\[
 \left|
 {\Delta_1^{\psi_N}(h_N)-\kappa(\psi_N)h_N^3
  \over h_N^5}-\beta(\psi_N)
 \right|\le1.                                  \tag{6.5}
\]

After `h_N` has been chosen, Lemma 2.1 supplies a positive activation
radius which makes the exact one- and two-step outputs change by at most
`h_N^5`.  Make the sum of every future amplitude smaller than this radius
and smaller than the analogous radii for all earlier stages.  A geometric
choice of the future amplitudes realizes all these countably many nested
budgets.  More explicitly, also apply Lemma 2.1 to `psi_N`, both terminal
times `k=1,2`, and every integer step interval `|h|<=m`, `1<=m<=N`.  Let
`r_N>0` be the minimum of the finitely many resulting radii after dividing
the desired output errors by their constants.  Require recursively

\[
 \sum_{q>N}\delta_q
 \le2^{-N}\min\{r_1,\ldots,r_N,h_N^5\}.         \tag{6.5a}
\]

At a later stage there are still only finitely many old constraints, and
(5.12) remains available for arbitrarily small `delta`; hence the recursion
does not get stuck.

The locally finite limit

\[
 g=1+\sum_{m\ge1}\delta_mR((x-X_m)/w_m),
 \qquad \Phi(x)=\int_0^xg,
 \qquad \phi={\Phi\over\|\Phi(G)\|_2}           \tag{6.6}
\]

is `C^infinity`.  Moreover `1<=g<=1+sum delta_m<2`; hence (1.2) holds.
The compact-`h` budgets (6.5a) make the finite-width outputs of `phi`
uniform limits of those of `psi_N`.  For clarity, if `|h|<=m` and `N>=m`,

\[
 \sup_n|F_{k,n}^{\phi}(h)-F_{k,n}^{\psi_N}(h)|\le2^{-N},
 \qquad k=1,2.                                  \tag{6.6a}
\]

Since each `psi_N` has the established fixed-step width-first limit, first
choose `N`, then take `n -> infinity`, and finally let `N -> infinity` in
(6.6a).  This proves that the exact width-first `F_1^phi` and `F_2^phi`
exist and are finite at every fixed `h`.

Let

\[
 \kappa_\infty=\lim_N\kappa(\psi_N),
\]

which exists by the budgets in (6.3).  The output and cubic-tail budgets,
together with (6.5), imply

\[
 \left|
 {\Delta_1^\phi(h_N)-\kappa_\infty h_N^3\over h_N^5}
 \right|
 \ge |\beta(\psi_N)|-3\longrightarrow\infty.   \tag{6.7}
\]

If `kappa!=kappa_infinity`, then (6.4) also gives

\[
 h_N^2{\Delta_1^\phi(h_N)-\kappa h_N^3\over h_N^5}
 \longrightarrow\kappa_\infty-\kappa\ne0,      \tag{6.8}
\]

so the unscaled quotient diverges for every other `kappa` as well.  Since
`h_N -> 0`, every interval `(0,r]` contains all sufficiently late `h_N`.
Equations (6.7)--(6.8) prove (1.3). `square`

## 7. Audit boundary

The proof uses local fifth coefficients only for the smooth finite
truncations `psi_N`.  The conclusion (1.3) is an exact fixed-nonzero-step,
width-first statement about the single final activation `phi`; it is not a
claim obtained by interchanging `n -> infinity` and `h -> 0`.

The construction also shows why a request for a *finite* super-`t^5`
literal fifth coefficient is impossible: whenever that coefficient exists,
Euler chronology makes it a polynomial of degree at most four in `t`.
What fails under linear growth alone is existence of a finite interval
remainder coefficient.

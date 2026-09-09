# Full response-aware audit of the narrow-transition mechanism

## 1. Result

For the RMS-normalized `q=1`, two-hidden-layer model, orient the first paired
Euler defect as

\[
 \Delta_1(h)=F_2(h)-F_1(2h).
\]

At the identity background, insert a slope transition

\[
 \phi'(x)=1+\delta R((x-X)/w),\qquad R'=\rho,
 \quad \rho\in C_c^\infty.
\]

The complete width-first fifth coefficient, including every forward Gram,
transpose response, and reused-matrix contraction, has quadratic principal
part

\[
 \boxed{
 [h^5]\Delta_1
 =-{2365\over8}\,\gamma(X){\delta^2\over w^3}
      \int_{\mathbb R}(\rho')^2+\text{nonprincipal terms}. }
 \tag{1.1}
\]

The lower hidden layer contributes `-55/8`; the upper hidden layer contributes
`-1155/4`.  Thus the lower-layer estimate used in the diagonal construction
has the correct sign and is conservative.  The earlier claim that every
flattened monomial has total singular excess at most four is false: the exact
map reaches total excess eight.  Section 5 gives the replacement argument
which controls all such terms without that claim.

The machine-checkable certificate is
[`audit_full_l2_paired_transition.py`](audit_full_l2_paired_transition.py).
It consumes the frozen 979-term map
[`FULL_L2_PAIRED_ORDER5_MAP.json`](FULL_L2_PAIRED_ORDER5_MAP.json).

## 2. Exact paired tensor and why the 974-term flow map is insufficient

For a finite-dimensional `C^5` potential `f`, write `g=grad f` and let
`H,T,U,V` be its second through fifth derivatives.  Two fine Euler steps
give

\[
 E_h^2x-x=2hg+h^2Hg+{h^3\over2}T[g,g]
 +{h^4\over6}U[g,g,g]+{h^5\over24}V[g,g,g,g]+O(h^6).
\]

Substitution into the Taylor formula for `f` and subtraction of
`f(x+2hg)` gives

\[
\boxed{
 \mathfrak B_5={1\over24}V[g^5]+{5\over3}U[Hg,g^3]
 +T[T[g,g],g,g]+{1\over2}T[H^2g,g,g]+T[Hg,Hg,g]. }
\tag{2.1}
\]

There is no `||H^2g||^2` term.  In the ordered elementary-differential
basis

\[
 \bigl(V[g^5],U[Hg,g^3],T[T[g,g],g,g],T[H^2g,g,g],
       T[Hg,Hg,g],\|H^2g\|^2\bigr),
\]

the paired weights are

\[
 \left({1\over24},{5\over3},1,{1\over2},1,0\right).
 \tag{2.2}
\]

By contrast, the existing 974-term continuous-flow map has weights

\[
 \left({1\over60},{11\over60},{7\over60},{1\over4},
       {3\over10},{2\over15}\right).
 \tag{2.3}
\]

Consequently the 974 already-summed monomials cannot simply be declared to
be the paired coefficient.  They must be separated before the Euler weights
are changed.

## 3. Five-path separation and the full Gaussian peel

For numbers `lambda_0,...,lambda_4`, define a formal gradient curve by

\[
 [h^{m+1}]\theta_\lambda(h)
 =\lambda_m[h^m]g(\theta_\lambda(h)),\qquad0\le m\le4.
 \tag{3.1}
\]

Let `Q(lambda)=[h^5]f(theta_lambda(h))`.  Direct tensor expansion gives the
following sparse paths:

| path | `lambda` | nonzero elementary-differential weights |
|---|---|---|
| `Q0` | `(1,0,0,0,0)` | `E1/120` |
| `Q1` | `(1,0,0,1,0)` | `E1/120+E2/6` |
| `Q2` | `(1,0,1,0,0)` | `E1/120+E3/4` |
| `Q3` | `(1,0,1,1,0)` | `E1/120+E2/6+E3/4+E4/2` |
| `Q4` | `(1,1,0,0,0)` | `E1/120+E2/6+E5/2` |

Here `E1,...,E6` denote the ordered basis in Section 2.  Therefore

\[
 \boxed{\mathfrak B_5=-8Q_0+7Q_1+3Q_2+Q_3+2Q_4.}
 \tag{3.2}
\]

The compiler implements (3.1) at the finite feature-jet level.  If
`M=W/sqrt(n)`, then coefficient `m>=1` of its learned rank-one part is

\[
 M_m={\lambda_{m-1}\over n}
      \sum_{p+q=m-1}b_p h_q^T.                 \tag{3.3}
\]

The readout and lower preactivation coefficients are, with the same weight,

\[
 a_m=\lambda_{m-1}g_{m-1},\qquad
 u_m=\lambda_{m-1}\sum_{p+q=m-1}\phi'(u)_p r_q.
 \tag{3.4}
\]

Substitution of (3.3) into both `M h` and `M^T b`, before taking any
expectation, gives exactly the Gram terms in the compiler.  The dense
initial matrix is peeled chronologically:

\[
 M_0h_k=F_k+\sum_{s<k}b_s\,E\,\partial_{R_s}h_k,
 \quad
 M_0^Tb_k=R_k+\sum_{s\le k}h_s\,E\,\partial_{F_s}b_k.
 \tag{3.5}
\]

Thus every `W/W^T` reuse is retained.  The rest is the terminating
Wick--Stein recursion of the audited order-five compiler.  Setting
`lambda_m=1/(m+1)` makes (3.3)--(3.4) literally the continuous-flow source
code and hence recovers the 974-term map.  Applying (3.2) instead produces
979 nonzero layer-separated monomials, 954 after identifying the two
unit-Gaussian layer alphabets, and maximum activation derivative five.
The identity activation evaluates to `20`, agreeing with the independently
known coefficient `[h^5](F_2(h)-F_1(2h))=20`.

## 4. Exact principal coefficient across all 979 monomials

On the transition,

\[
 \phi''={\delta\over w}\rho,
 \quad\phi'''={\delta\over w^2}\rho',
 \quad\phi^{(4)}={\delta\over w^3}\rho'',
 \quad\phi^{(5)}={\delta\over w^4}\rho'''.     \tag{4.1}
\]

At amplitude order two and scale `w^-3`, all nonsingular moment atoms are
evaluated at the identity.  There are exactly three possible singular
atoms.  Exhaustive exact substitution in the 979-term map gives

| singular atom | lower `X` weight | upper `Y` weight | total |
|---|---:|---:|---:|
| `(phi''')^2` | `15` | `768` | `783` |
| `phi'' phi^(4)` | `25` | `1456` | `1481` |
| one slope variation times `phi^(5)` | `25/8` | `1597/4` | `3219/8` |

Put `I=int (rho')^2`.  Compact support gives

\[
 \int\rho\rho''=-I,
 \qquad \int R\rho'''=I.                      \tag{4.2}
\]

The total integrated weight is therefore

\[
 783-1481+{3219\over8}=-{2365\over8}.          \tag{4.3}
\]

Layer by layer,

\[
 15-25+{25\over8}=-{55\over8},
 \qquad
 768-1456+{1597\over4}=-{1155\over4}.          \tag{4.4}
\]

Equations (4.1)--(4.4) prove (1.1).  This calculation does not isolate a
frozen scalar route: the weights were extracted only after the complete
response-aware Gaussian peel.

There is also an exact check on the naively most singular 36 monomials.
They factor as

\[
\begin{aligned}
 &X_{220000}^2(X_{020000}+X_{200000})^3\\
 &\quad\times
 (Y_{000200}+2Y_{001010}+Y_{010001})
 (Y_{002000}+Y_{010100})^2.                    \tag{4.5}
\end{aligned}
\]

The last two factors are exactly

\[
 E[(\phi'\phi''')''],\qquad E[(\phi'\phi'')'].
 \tag{4.6}
\]

Thus their apparent constant-density `w^-5` contribution cancels before an
absolute value is taken.  This is one explicit place where the reused-source
sum is better behaved than its individual monomials.

## 5. Correct control of every higher-excess monomial

The false statement “the total excess is at most four” is not needed.  For
a moment atom let

\[
 e=\sum_{r=2}^5(r-1)\nu_r,
 \qquad k=\sum_{r=2}^5\nu_r.                  \tag{5.1}
\]

The exact 979-term census has total monomial excess

\[
\begin{array}{c|rrrrrrrrr}
\text{total }e&0&1&2&3&4&5&6&7&8\\ \hline
\text{terms}&6&24&86&126&244&198&186&73&36.
\end{array}                                    \tag{5.2}
\]

Nevertheless each individual atom has `e<=4`, no monomial contains two
quadratic excess-four atoms, and the atomwise integration supplies the
missing control.  A nonempty transition atom obeys

\[
 |M_\nu^{\rm tr}|
 \le C P(X)\gamma(X)\delta^k w^{1-e},          \tag{5.3}
\]

apart from the harmless permanent-tail term.  Here `P` is a fixed
polynomial determined by the finite moment map.

There is one necessary refinement.  An `(e,k)=(4,1)` atom contains one
`phi^(5)`.  Its amplitude-linear part is

\[
 \delta w^{-3}\int A(X+wy)\rho'''(y)
                 \gamma(X+wy)\,dy.
\]

The moments of `rho'''` of degrees zero, one, and two vanish.  Taylor's
formula therefore makes this part `O(delta P(X)gamma(X))`, with no negative
power of `w`.  If a derivative instead hits the transition-dependent slope
inside `A`, there is a second factor `delta`; this is precisely an effective
`(e,k)=(4,2)` block.  Further slope factors carry further positive powers
of `delta`.

Now set

\[
 w=\delta\sqrt{\gamma(X)},\qquad
 S=\delta^2\gamma(X)w^{-3}
   =\delta^{-1}\gamma(X)^{-1/2}.               \tag{5.4}
\]

For a product of transition atoms `(e_i,k_i)`, after replacing `(4,1)` by
its first nontrivial effective value `(4,2)`, division by `S` gives powers

\[
 m_\delta=1+\sum_i(k_i+1-e_i),
 \qquad
 2m_\gamma=1+\sum_i(3-e_i).                   \tag{5.5}
\]

An exhaustive rational census first treating every high-derivative atom as
new proves

\[
 m_\delta\ge0,qquad m_\gamma\ge0.            \tag{5.6}
\]

Equality in both occurs for exactly 63 flattened monomials, and every one
contains a single effective `(4,2)` atom and no other new singular atom.
Their complete true quadratic principal sum is the strictly negative
coefficient (4.3).  Every other monomial has either `m_delta>0` or
`m_gamma>0`.  Hence, choosing first
`X` large and then `delta` small relative to the finitely many powers of
`X`, their sum is `o(S)`.  The right-tail change is bounded by
`C delta P(X) gamma([X-1,infinity))` and is also `o(S)`.

This is the valid replacement for the earlier total-excess argument.  It
uses a finite exact census, but not a finite-source approximation: the 979
monomials are the complete order-five response-aware map.

### 5.1 Insertion over an arbitrary finite old ladder

The identity-background table alone would not justify an infinite diagonal:
old narrow transitions can have arbitrarily large derivative moments even
when the old activation is close to the identity in `C^1`.  The required
insertion statement is instead local in the **new** transition and does not
bound old derivatives by a `C^1` distance.

Fix any finite old ladder `phi_old`.  All of its Gaussian derivative moments
through order five are finite numbers.  Put the new interval strictly to the
right of every old transition.  On that interval `phi_old` is affine.  In a
single one-dimensional moment atom, a product containing both an old
singular derivative and a new singular derivative is identically zero,
because their supports are disjoint.  Therefore, after expanding each
moment polynomial, every old singular atom is merely a fixed coefficient;
all powers of the new `(delta,w,gamma(X))` still come from the blocks counted
in (5.5).

For completeness, the hostile certificate enumerates **every nonempty
subset** of high-derivative atoms in each of the 979 monomials as the new
subset, leaving the complement arbitrary and old.  There are no negative
margin subset instances.  There are 267 conservative zero-margin instances;
each consists of one effective `(4,2)` new block.  Some arise from a lone
`phi^(5)` atom with no same-source slope factor.  Those are not actual
quadratic principal terms: the three integrations by parts above give them
positive margin.  The remaining zero-margin candidates must be grouped
before signs are taken, and their grouping is exactly the node symbol
(5.9)--(5.10).

It remains to identify the zero-margin sum without assuming that those fixed
old coefficients are small.  This follows before the Gaussian peel from a
nodewise principal-symbol identity.  For one activation node write locally

\[
 f(\theta)=\widehat f(\theta,\Phi(x(\theta))),\qquad
 r=\partial_y\widehat f,\quad \ell=\nabla x,
 \quad s=\ell^TG\ell,\quad v=\ell^TG\nabla f,   \tag{5.7}
\]

where `G` is the constant positive gradient metric.  The highest-new-excess
part of the `k`th derivative tensor is

\[
 r\Phi^{(k)}\ell^{\otimes k}.                  \tag{5.8}
\]

Every derivative of `r`, `ell`, or a higher derivative of `x` lowers the new
excess and hence has positive margin.  At quadratic amplitude and new excess
four, the five terms in (2.1) reduce exactly to

\[
 r^2sv^4{\delta^2\over w^4}
 \left\{{5\over24}R\rho'''
       +{5\over3}\rho\rho''+(\rho')^2\right\}. \tag{5.9}
\]

Indeed, the three displayed summands come respectively from the first-order
velocity variation in `V[g^5]`, from `U[Hg,g^3]`, and from
`T[T[g,g],g,g]`.  The last two terms of (2.1) require at least three new
singular factors to reach excess four and therefore have no quadratic part.
Using (4.2), (5.9) integrates to

\[
 -{11\over24}r^2sv^4{\delta^2\over w^3}I\le0. \tag{5.10}
\]

This grouping is compatible with the reused-matrix peel, rather than an
identity asserted only after flattening.  At finite width, attach a formal
mark to each occurrence of the new transition and differentiate the exact
paired B-series before taking expectations.  The coefficient with two
marks at one node is the tensor contraction (5.9).  Conditional on all
previously exposed rows and columns, every remaining matrix source `J` is
standard Gaussian and its adjoint occurrence is eliminated by the exact
finite-dimensional identity

\[
 \mathbb E[J V(J)]=\mathbb E[D_JV(J)].
\]

Mark extraction, finite differentiation, and this identity are linear and
therefore commute.  Iterating over the finitely many reused row/column
sources gives (3.5), including every response term, while preserving the
already grouped marked coefficient.  Polynomial moment bounds from the
bounded old slope give uniform integrability, so the marked identity passes
to the width limit.  Thus (5.10) is the principal symbol of the full
979-term OMFP map, not of a frozen scalar subgraph.

This identity allows arbitrary old derivatives inside the fixed quantities
`r,ell,s,v`; it is not a continuity assertion in a norm that ignores them.
Terms involving new singular factors at two distinct nodes receive two new
transition integrations and have positive margin, exactly as certified by
(5.5)--(5.6).

For a lower-layer node in the finite network, on the old affine slope `b`,

\[
 r_j={b_j\over n},\qquad s_j=n,qquad v_j=b_jb.
\]

Consequently its total node weight is

\[
 {b^4\over n}\sum_{j=1}^n b_j^6.
\]

At initialization and conditional on the new preactivation location, the
width limit is `15 d^3 b^4`, where
`d=E phi_old'(G)^2>0`.  Bounded old slope gives the required twelfth-moment
uniform integrability.  Hence the lower nodes alone give the strict bound

\[
 -{55\over8}d^3b^4\gamma(X){\delta^2\over w^3}I. \tag{5.11}
\]

The frozen map gives an independent general-background certificate for this
factor.  The only three layer-`X` principal terms are, at canonical indices
685, 686, and 691,

\[
 \left(15X_{040200}+25X_{041010}+{5\over8}X_{050001}\right)
 Y_{020000}^3.                                 \tag{5.12}
\]

On the new interval the old slope is `b`, while `Y_020000=d`.  The first
two terms give `15 b^4 I` and `-25 b^4 I`; the last has five choices for
the one slope variation and gives `(25/8)b^4 I`.  Thus (5.12) is exactly
`-(55/8)b^4d^3I`.  No term contains a layer-`X` principal atom together
with an old high-derivative atom.

All upper-node zero-margin contributions are nonpositive by (5.10) and may
be discarded.  This proves a background-uniform **sign** and strict lower
weight for every finite old ladder.  Constants multiplying positive-margin
terms may depend arbitrarily on the old derivative moments; they are finite.
Choose `X` after the old ladder so that every term with positive
`m_gamma` is small, and then choose `delta` so that every term with positive
`m_delta` is small.  Since there are only 979 terms at each insertion, this
ordered choice always terminates.  Thus huge old derivative moments do not
invalidate the diagonal construction.

Finally, RMS renormalization is additive, not merely a common unexplained
multiplier.  If `Phi_old` is the unnormalized old activation and
`Phi_new-Phi_old=delta (x-X)_+` off the transition strip, then

\[
 |\|\Phi_{new}(G)\|_2-\|\Phi_{old}(G)\|_2|
 \le C\delta\|(G-X)_+\|_2+C\delta w\sqrt{\gamma(X)}. \tag{5.13}
\]

Both norms stay in a fixed compact subset of `(0,infinity)`.  Expanding the
finite 979-monomial map in the resulting scalar normalization change gives
an additive error bounded by the right side of (5.13) times a finite
old-ladder constant, plus an `O(delta)` relative change of the new principal
term.  The former has positive margin and the latter preserves the strict
negative sign after `delta` is chosen small.  This also applies to the cubic
map.  No global-rescaling term is omitted.

## 6. Cubic coefficient audit

The same Euler calculation at order three gives

\[
 \mathfrak B_3={1\over2}T[g,g,g]+2\|Hg\|^2.   \tag{6.1}
\]

The response-aware compiler produces 50 layer-separated monomials.  At
quadratic transition order their exact weights are

| singular atom | lower | upper | total |
|---|---:|---:|---:|
| `(phi'')^2` | `6` | `68` | `74` |
| one slope variation times `phi'''` | `9/2` | `55` | `119/2` |

Because `int R rho'=-int rho^2`, the integrated total is

\[
 74-{119\over2}={29\over2}.                   \tag{6.2}
\]

Thus the leading cubic change has magnitude

\[
 C\delta^2\gamma(X)w^{-1}=C\delta\sqrt{\gamma(X)}\to0. \tag{6.3}
\]

The full cubic all-new margin census has no negative margin.  Enumerating
every old/new atom subset also has no negative margin and gives 44
conservative zero-margin instances, each a single effective quadratic
excess-two atom.  Lone `phi'''` instances without a slope factor improve
after integration by parts; the true quadratic group is (6.2).  Hence all
other cubic terms are smaller under the same ordered choice of `X` and
`delta`.

## 7. Audit conclusion

The full `L=2` transition mechanism passes the source/reused-adjoint audit
after one correction:

1. the 974-term continuous-flow map is replaced by the exact 979-term paired
   Euler map;
2. the false total-excess-four assertion is deleted;
3. the exact atomwise margin census (5.5)--(5.6) controls all multi-atom
   terms;
4. the complete quadratic principal coefficient is `-2365/8`, while the
   conservative lower-layer coefficient remains `-55/8`;
5. the cubic change is `O(delta sqrt(gamma(X)))` and therefore can be made
   summable in the diagonal construction.

These statements concern the finite smooth truncations, for which the
width-first fifth and cubic maps are already valid.  Passing to the final
globally Lipschitz activation still requires the separate fixed-step
uniform-approximation diagonal argument; no Taylor expansion of the final
activation is used.

## 8. General horizon and a genuine super-`t^5` effective sequence

Let

\[
 \Delta_t(h)=F_{2t}(h)-F_t(2h).
\]

The universal Euler recurrence can be carried out before inserting any
network.  In the six-element basis of Section 2, the exact `[h^5]` weights
of `Delta_t` are

\[
\begin{aligned}
 W_1(t)&={1\over3}t^4-{1\over3}t^3+{1\over24}t,\\
 W_2(t)&={19\over3}t^4-{23\over3}t^3
          +{35\over12}t^2+{1\over12}t,\\
 W_3(t)&={13\over3}t^4-6t^3+{35\over12}t^2-{1\over4}t,\\
 W_4(t)&={43\over3}t^4-27t^3+{203\over12}t^2-{15\over4}t,\\
 W_5(t)&={46\over3}t^4-26t^3+{91\over6}t^2-{7\over2}t,\\
 W_6(t)&={32\over3}t^4-28t^3+{70\over3}t^2-6t.
\end{aligned}                                  \tag{8.1}
\]

The exact recurrence and its rational finite-difference audit are in
[`general_t_transition_weights.py`](general_t_transition_weights.py).  One
derivation is as follows.  If

\[
 x_N-x_0=h x_1+h^2x_2+h^3x_3+h^4x_4+h^5x_5+O(h^6),
\]

then one Euler step updates

\[
\begin{aligned}
 x_1^+&=x_1+g,\\
 x_2^+&=x_2+Hx_1,\\
 x_3^+&=x_3+Hx_2+\tfrac12T[x_1,x_1],\\
 x_4^+&=x_4+Hx_3+T[x_1,x_2]+\tfrac16U[x_1^3],
\end{aligned}
\]

with the analogous displayed order-five Taylor increment.  Reducing the
terminal observable to the six scalar contractions gives a degree-five
polynomial in `N`.  Evaluating it at `N=2t` and subtracting 32 times its
value at `N=t` cancels the degree-five part and gives (8.1).  At `t=1`,
(8.1) reduces to (2.2), providing a direct control.

Only the first three elementary differentials contribute at quadratic
amplitude and new excess four.  Therefore the integrated single-node symbol
is

\[
\begin{aligned}
 \Xi_5(t)
 &=5W_1(t)-W_2(t)+W_3(t)\\
 &=-{t^4\over3}-{t\over8}.
\end{aligned}                                  \tag{8.2}
\]

Consequently the general-horizon version of (5.10) is

\[
 \boxed{
 -\left({t^4\over3}+{t\over8}\right)
 r^2sv^4\gamma(X){\delta^2\over w^3}I.}       \tag{8.3}
\]

It is strictly negative for every integer `t>=1`.  The lower hidden layer
alone gives

\[
 -15\left({t^4\over3}+{t\over8}\right)
 d^3b^4\gamma(X){\delta^2\over w^3}I.         \tag{8.4}
\]

### 8.1 The sixth elementary differential and the complete support

There is a subtlety which the special `t=1` map cannot detect:
`W_6(1)=0`, whereas `W_6(t)` is nonzero for general `t`.  We therefore
compiled all six elementary differentials separately.  If `Q_i` are the
five sparse paths of Section 3 and `Q_5=Q(1,1,1,0,0)`, direct Taylor
expansion of
`delta theta=h g+h^2Hg+h^3(H^2g+T[g,g]/2)` gives

\[
 Q_5={E_1\over120}+{E_2\over6}+{E_3\over4}
       +E_4+{E_5\over2}+E_6.                 \tag{8.5}
\]

Thus `E_6=Q_5-Q_0+2Q_1+Q_2-2Q_3-Q_4`, an exact sparse-path
isolation.  The six layer-separated maps contain respectively

\[
 76,\ 383,\ 192,\ 496,\ 770,\ 515
\]

monomials; after attaching the polynomial weights (8.1), their union has
1045 monomials.  Exhaustively assigning every nonempty subset of the
high-derivative atoms to the new bump gives no negative-margin case.  There
are 267 conservative zero-margin assignments, each a single effective
`(e,k)=(4,2)` block.

The sixth map alone has 84 conservative zero-margin assignments.  They are
flattening artifacts: its three raw identity-background principal weights
are `16,16,0` for `(phi''')^2`, `phi''phi^(4)`, and the
slope--`phi^(5)` term, so their integrated sum is `16-16+0=0`.  More
importantly, this cancellation is background-uniform before peeling.  In
`E_6=||H^2g||^2`, new excess four requires four singular Hessian factors,
hence new amplitude order four; there is no quadratic `(e,k)=(4,2)` marked
source.  Exact marked Gaussian integration by parts commutes with source
extraction, so the 84 flattened entries recombine to zero for an arbitrary
old complement.

The complete integrated principal polynomials are

\[
\begin{aligned}
 P_{\rm all}(t)&=-215t^4-{645\over8}t,\\
 P_X(t)&=-5t^4-{15\over8}t,\\
 P_Y(t)&=-210t^4-{315\over4}t.
\end{aligned}                                  \tag{8.6}
\]

This independently recovers (8.3)--(8.4).  The executable certificate is
[`audit_general_t_transition_map.py`](audit_general_t_transition_map.py),
and its successful exact-rational output is frozen in
[`GENERAL_T_ALL_SIX_AUDIT.json`](GENERAL_T_ALL_SIX_AUDIT.json).

### 8.2 Compact insertion

Choose `p in C_c^infinity((-1/4,1/4))` with `int p=0` and
`I_p=int(p'')^2>0`, put `P(y)=int_(-infinity)^y p(s)ds`, and add

\[
 q_{X,w,\delta}(x)=\delta wP((x-X)/w).         \tag{8.7}
\]

Both the value and slope perturbations are compactly supported.  Since
`int pp''''=I_p` and `int p'p'''=-I_p`, the principal term is

\[
 -\left({t^4\over3}+{t\over8}\right)
 r^2sv^4\gamma(X){\delta^2\over w^3}I_p.      \tag{8.8}
\]

Set `w=delta sqrt(gamma(X))`.  Before the Gaussian peel an order-five
marked source has total new excess `e<=4`.  If `k` high derivatives occupy
`R` distinct Gaussian endpoint classes, localization gives

\[
 C_{t,{\rm old}}P_{t,{\rm old}}(X)
 \delta^k\gamma(X)^R w^{R-e}.                 \tag{8.9}
\]

After division by the principal scale
`S=delta^(-1)gamma(X)^(-1/2)`, its margins are

\[
 m_\delta=k+R-e+1,\qquad 2m_\gamma=3R-e+1.   \tag{8.10}
\]

For `R>=2` the Gaussian margin is positive.  For `R=1`, both can vanish
only at `e=4,k=2`.  A lone fifth derivative has four vanishing moments
after integration by parts; its first nonzero transition-dependent term
has effective `k=2`.  The true zero sector is (8.8).  The all-six audit is
the flattened certificate: `E_4,E_5` need at least three new singular
factors at excess four and `E_6` needs four, so only `E_1,E_2,E_3`
contribute quadratically.

It follows that for every finite smooth old activation, fixed `t`, target
`A`, and `epsilon>0`, one can choose `X`, then `delta`, so that the
RMS-normalized new activation is within `epsilon` in

\[
 d_1(u,v)=\sup_x{|u(x)-v(x)|\over1+|x|}
             +\|u'-v'\|_\infty               \tag{8.11}
\]

and its exact width-first fifth coefficient is at most `-A`.  Indeed,
choose `X` to suppress every positive Gaussian margin, then `delta` to
suppress every positive amplitude margin.  The strict lower-node term
diverges as `t^4/(delta sqrt(gamma(X)))`, while `d_1(q,0)<=C_p delta`.
The normalizer changes by at most
`C delta w sqrt(w gamma(X))` (take `Xw<=1`), which has positive margin.
All old constants are finite and only 1045 monomials occur, so the ordered
choice terminates.

### 8.3 Two-rate diagonal

For `rho>0` define

\[
 {\cal B}_\phi(t,\rho)=
 \inf_{\kappa\in\mathbb R}\sup_{0<|h|\le\rho/t}
 { |\Delta_t^\phi(h)-\kappa h^3|\over |h|^5}. \tag{8.12}
\]

Choose increasing integers `t_N`.  Recursively apply the compact insertion
on disjoint supports, below every old `d_1` ceiling, so that the smooth
normalized truncation `psi_N` obeys

\[
 |\beta_N|:=|[h^5]\Delta_{t_N}^{\psi_N}(h)|
 \ge20t_N^{N+5}.                              \tag{8.13}
\]

After `psi_N` is fixed, let `kappa_N` be its cubic coefficient and choose
`0<h_N<=rho/t_N` so that, for `r=h_N,h_N/2`,

\[
 \left|{\Delta_{t_N}^{\psi_N}(r)-\kappa_Nr^3\over r^5}
             -\beta_N\right|
 \le {|\beta_N|\over20}.                      \tag{8.14}
\]

This Taylor choice is made only for the fixed smooth width-first
truncation.  Reserve future `d_1` budgets so that the final activation
`phi` satisfies at both rates

\[
 |\Delta_{t_N}^{\phi}(r)-\Delta_{t_N}^{\psi_N}(r)|
 \le {|\beta_N|\over20}(h_N/2)^5.             \tag{8.15}
\]

These budgets exist uniformly in width.  For any fixed `C^2` background,
finite schedule, and compact step interval, coupling the finite-width
networks gives

\[
 \sup_n\mathbb E|f_{k,n}^{u}(h)-f_{k,n}^{v}(h)|\le C d_1(u,v). \tag{8.16}
\]

In normalized vector norm the state and difference recurrences are
`S_{j+1}<=P(S_j)` and
`D_{j+1}<=Q(S_j)(D_j+d_1(u,v))`; Gaussian vector moments and
`sup_n E||W/sqrt(n)||_op^p<infinity` make the polynomial integrable.
Splitting `v'(x)-u'(y)` at `u'(x)` uses only the fixed background's bounded
second derivative.  Since every later compact insertion can have
arbitrarily small `d_1` size, geometric allocation meets the finitely many
old constraints at every stage.  Enumerating all finite horizon/compact
step pairs proves, by the same three-epsilon argument, that the locally
finite limit has every fixed-step width-first output.  Summable amplitudes
make the one final normalized `phi` smooth, globally Lipschitz, linearly
growing, with slope bounded away from zero.

For arbitrary `kappa`, put `x=(kappa_N-kappa)/h_N^2`.  Equations
(8.14)--(8.15) give

\[
 Q(h_N)=x+\beta_N+e_1,\qquad
 Q(h_N/2)=4x+\beta_N+e_2,                     \tag{8.17}
\]

where `Q(r)=(Delta_{t_N}^phi(r)-kappa r^3)/r^5` and
`|e_1|,|e_2|<=|beta_N|/10`.  The exact minimax identity

\[
 3|\beta|=|4(x+\beta)-(4x+\beta)|
 \le5\max\{|x+\beta|,|4x+\beta|\}            \tag{8.18}
\]

therefore yields, uniformly in `kappa`,

\[
 \boxed{{\cal B}_\phi(t_N,\rho)
        \ge{1\over2}|\beta_N|
        \ge10t_N^{N+5}.}                      \tag{8.19}
\]

Thus `B_phi(t_N,rho)/t_N^q` tends to infinity for every fixed `q`, in
particular for `q=5`.  No cubic or fifth jet of the final activation is
assumed: the witnesses are two exact nonzero learning rates preserved
after the width-first limit.

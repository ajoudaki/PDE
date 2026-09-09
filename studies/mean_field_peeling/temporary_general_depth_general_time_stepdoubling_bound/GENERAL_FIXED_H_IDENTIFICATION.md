# Arbitrary finite-horizon fixed-step identification

This note proves the width-first bridge used by `FIXED_T_THEOREM.md` for
every fixed finite horizon.  The horizon is arbitrary but fixed throughout
the proof.  No statement here is uniform as the horizon tends to infinity,
and no learning-rate derivative is taken before the width limit.

## 1. Finite-width chronology

Fix integers \(T\ge1\) and \(L\ge2\), and fix \(h\ne0\).  For
\(0\le s<T\), the exact recomputed ascent step first performs the forward
actions

\[
 X_\ell^s=\frac{W_\ell^0H_{\ell-1}^s}{\sqrt n},
 \qquad \ell=2,\ldots,L,
 \tag{1.1}
\]

in increasing layer order, and then the transpose actions

\[
 R_{\ell-1}^s=\frac{(W_\ell^0)^TC_\ell^s}{\sqrt n},
 \qquad \ell=L,\ldots,2,
 \tag{1.2}
\]

in decreasing layer order.  After the \(T\)-th update, the terminal
forward sweep performs (1.1) at \(s=T\), with no subsequent transpose
action.  Thus the ordered action list is

\[
 \begin{aligned}
 {\cal A}_{T,L}=(&\uparrow,0,2),\ldots,(\uparrow,0,L),
 (\downarrow,0,L),\ldots,(\downarrow,0,2);\ \ldots;\\
 & (\uparrow,T-1,2),\ldots,(\uparrow,T-1,L),
 (\downarrow,T-1,L),\ldots,(\downarrow,T-1,2);\\
 & (\uparrow,T,2),\ldots,(\uparrow,T,L)).
 \end{aligned}                                           \tag{1.3}
\]

It has

\[
 A_{T,L}^{\rm act}=(2T+1)(L-1)                         \tag{1.4}
\]

entries.  More explicitly, for \(0\le s<T\),

\[
 \iota(\uparrow,s,\ell)=2s(L-1)+\ell-1,
\]

\[
 \iota(\downarrow,s,\ell)
 =2s(L-1)+(L-1)+(L-\ell+1),                            \tag{1.5}
\]

and

\[
 \iota(\uparrow,T,\ell)=2T(L-1)+\ell-1.
\]

The exact accumulated learned pieces are, with

\[
 Q_{\ell,rs}^{(n)}=n^{-1}(H_\ell^r)^TH_\ell^s,
 \qquad
 K_{\ell,rs}^{(n)}=n^{-1}(C_\ell^r)^TC_\ell^s,
\]

\[
 Z_\ell^s=X_\ell^s+h\sum_{r<s}Q_{\ell-1,rs}^{(n)}C_\ell^r,
 \tag{1.6}
\]

\[
 B_{\ell-1}^s=R_{\ell-1}^s
 +h\sum_{r<s}K_{\ell,rs}^{(n)}H_{\ell-1}^r,           \tag{1.7}
\]

\[
 a^s=a^0+h\sum_{r<s}H_L^r,
 \qquad
 Z_1^s=Z_1^0+h\sum_{r<s}C_1^r.                        \tag{1.8}
\]

Consequently a forward action at time \(s\) regresses only against
\(Q^{[s-1]},K^{[s-1]}\), and a transpose action at time \(s\) only
against \(Q^{[s]},K^{[s-1]}\).  The largest histories inverted are

\[
 Q_\ell^{[T-1]},\qquad K_\ell^{[T-1]};                \tag{1.9}
\]

the terminal time-\(T\) feature Gram is formed but never inverted.

## 2. Parameterized inverse-free population DAG

For every connector \(2\le\ell\le L\), introduce centered Gaussian
blocks

\[
 \xi_\ell=(\xi_{\ell,0},\ldots,\xi_{\ell,T}),
 \qquad
 \chi_\ell=(\chi_{\ell,0},\ldots,\chi_{\ell,T-1}),    \tag{2.1}
\]

and independent \(U,A\sim N(0,1)\).  Different connectors and directions
use independent primitive Gaussian reservoirs.  Chronologically set

\[
 \mathbb E\xi_{\ell,r}\xi_{\ell,s}
 =Q_{\ell-1,rs}:=\mathbb E[H_{\ell-1}^rH_{\ell-1}^s],
\]

\[
 \mathbb E\chi_{\ell,r}\chi_{\ell,s}
 =K_{\ell,rs}:=\mathbb E[C_\ell^rC_\ell^s].            \tag{2.2}
\]

At each \(0\le s\le T\), ascend using

\[
 \rho_{\ell,sr}=\mathbb E[\partial_{\chi_{\ell,r}}
 H_{\ell-1}^s],\qquad0\le r<s,
\]

\[
 Z_\ell^s=\xi_{\ell,s}
 +\sum_{r<s}(\rho_{\ell,sr}+hQ_{\ell-1,rs})C_\ell^r,
 \qquad H_\ell^s=\phi(Z_\ell^s).                     \tag{2.3}
\]

For \(0\le s<T\), set

\[
 a^s=A+h\sum_{r<s}H_L^r,
 \qquad C_L^s=a^s\phi'(Z_L^s),                        \tag{2.4}
\]

and descend using

\[
 \sigma_{\ell,sr}=\mathbb E[\partial_{\xi_{\ell,r}}C_\ell^s],
 \qquad0\le r\le s,
\]

\[
 B_{\ell-1}^s=\chi_{\ell,s}
 +\sum_{r\le s}\sigma_{\ell,sr}H_{\ell-1}^r
 +h\sum_{r<s}K_{\ell,rs}H_{\ell-1}^r,
\]

\[
 C_{\ell-1}^s=B_{\ell-1}^s\phi'(Z_{\ell-1}^s),
 \qquad Z_1^{s+1}=Z_1^s+hC_1^s.                       \tag{2.5}
\]

At the terminal time,

\[
 a^T=A+h\sum_{r<T}H_L^r,
 \qquad F_{T,L}(h)=\mathbb E[a^TH_L^T].               \tag{2.6}
\]

Equations (2.1)--(2.6) are acyclic in exactly the order (1.3).  They use
no covariance inverse, so the same formulas also define the singular
coalesced DAG at \(h=0\).

## 3. Rank interval

Let \({\cal S}_{T,L}\) be the explicit compiler envelope.  If
\(\phi\) is nonconstant and

\[
 0<|h|\le r_{T,L}:=\frac1{2T\sqrt{{\cal S}_{T,L}}},    \tag{3.1}
\]

then

\[
 Q_\ell^{[s]}\succ0\quad(0\le s\le T),
 \qquad
 K_\ell^{[s]}\succ0\quad(0\le s<T).                 \tag{3.2}
\]

Here is the horizon-parameterized induction.  At \(s=0\), RMS
normalization gives \(Q_{\ell,00}=1\), while

\[
 K_{\ell,00}=d^{L-\ell+1},\qquad
 d=\mathbb E\phi'(G)^2>0.                              \tag{3.3}
\]

Assume (3.2) through the histories required before time \(s+1\).  The
new Schur complement of \(\chi_{2,s}\) is positive.  Conditional on all
other primitive variables, its fresh normal \(E\) enters

\[
 Z_1^{s+1}=R+h\phi'(Z_1^s)\sqrt{k_{2,s}}E.
\]

The event \(\phi'(Z_1^s)\ne0\) has positive probability, and Gaussian
full support plus continuity and nonconstancy of \(\phi\) makes the
conditional variance of \(H_1^{s+1}\) positive there.  The conditional
variance criterion therefore enlarges \(Q_1^{[s]}\) to a positive
definite \(Q_1^{[s+1]}\).  Upward, the new Schur complement of
\(\xi_{\ell,s+1}\) enters \(Z_\ell^{s+1}\) additively, while every
learned or response term uses only older cotangents.  The same criterion
proves each \(Q_\ell^{[s+1]}\succ0\).

For a non-affine activation, the fresh forward innovation in
\(Z_L^{s+1}\) is absent from all older top cotangents and
\(\phi'\) is continuous and nonconstant.  Moreover, for \(s+1<T\),

\[
 \|a^{s+1}-A\|_2
 \le |h|T\sqrt{{\cal S}_{T,L}}\le\frac12.             \tag{3.4}
\]

Thus \(a^{s+1}\) is nonzero and the new top cotangent has positive
conditional variance.  This proves \(K_L^{[s+1]}\succ0\).  Each
downward fresh transpose innovation then enters \(B_{\ell}^{s+1}\)
additively and is multiplied by a \(\phi'(Z_\ell^{s+1})\) which is
nonzero with positive probability.  The conditional-variance criterion
proves all lower \(K\)-ranks.

If \(\phi(x)=\alpha x+\beta\), \(\alpha\ne0\), the new innovation in
\(H_L^s\) enters

\[
 C_L^{s+1}=\alpha a^s+h\alpha H_L^s
\]

with nonzero coefficient, giving the top \(K\)-rank; multiplication by
the constant \(\alpha\) gives all lower ranks.  This closes the induction
for every \(s=0,\ldots,T-1\).  If \(d=0\), continuity gives
\(\phi\equiv\pm1\), which is treated separately and needs no Gram
inversion.

## 4. Conditional Gaussian action and population cancellation

At an action of one initialization matrix \(M\), collect the previously
revealed row queries, column queries, and actions as

\[
 H,\quad C,\quad Y=MH/\sqrt n,\quad D=M^TC/\sqrt n.
\]

Conditionally on the global predictable filtration,

\[
 M=P_CM+MP_H-P_CMP_H+P_C^\perp\widetilde MP_H^\perp, \tag{4.1}
\]

where the residuals of different connectors remain conditionally
independent standard Gaussian matrices.  Indeed, a new row query is
\(P_Hq+q_\perp\).  Revealing its residual action exposes only
\(P_C^\perp\widetilde M e e^T\), with
\(e=q_\perp/\|q_\perp\|\); its orthogonal complement remains an
independent Gaussian matrix.  The transpose case is the same with rows
and columns exchanged.  Iterating this argument over the explicitly
indexed list (1.3) proves (4.1) at every one of its
\((2T+1)(L-1)\) actions.

Put

\[
 Q=H^TH/n,\quad K=C^TC/n,\quad {\cal R}=C^TY/n=D^TH/n.
\]

Orthogonal regression gives, for a new transpose query \(c\),

\[
 \frac{M^Tc}{\sqrt n}
 =DK^{-1}k+HQ^{-1}(r-{\cal R}^TK^{-1}k)
 +\tau_cP_H^\perp g,                                  \tag{4.2}
\]

and, for a new row query \(x\),

\[
 \frac{Mx}{\sqrt n}
 =YQ^{-1}q+CK^{-1}(v-{\cal R}Q^{-1}q)
 +\tau_xP_C^\perp g.                                  \tag{4.3}
\]

Here \(k=C^Tc/n,r=Y^Tc/n,q=H^Tx/n,v=D^Tx/n\), and the squared
innovation scales are their positive Schur complements.  At population
level write old actions as

\[
 y=\xi+Pc,\qquad d=\chi+Sx.
\]

Gaussian integration by parts gives

\[
 {\cal R}=SQ+KP^T.
\]

For a new row field let

\[
 \rho=\mathbb E[\nabla_\chi H_{\rm new}],
\]

and for a new transpose field let

\[
 \sigma=\mathbb E[\nabla_\xi C_{\rm new}].
\]

Then

\[
 v=K\rho+Sq,\qquad r=Q\sigma+Pk.                      \tag{4.4}
\]

Substitution of (4.4) into (4.2)--(4.3) cancels every old-action
projection and leaves

\[
 y_{\rm new}=\xi_{\rm new}+\rho^Tc,
 \qquad
 d_{\rm new}=\chi_{\rm new}+\sigma^Tx.                \tag{4.5}
\]

Adding (1.6)--(1.7) gives precisely (2.3) and (2.5).  This calculation
does not depend on the number of old history columns, only on their
finiteness and invertibility, both supplied by (1.3) and (3.2).

## 5. One compatible ideal array and action-indexed good events

For every physical coordinate in layer one take an iid copy of
\((U,\chi_{2,0:T-1})\); for an interior layer \(2\le\ell<L\), take an
iid copy of
\((\xi_{\ell,0:T},\chi_{\ell+1,0:T-1})\); and at the top take an iid
copy of \((\xi_{L,0:T},A)\).  Arrays belonging to distinct physical
layers are independent.  Extend each Gaussian block chronologically by
regression from its population Gram.  At action \(i\) in (1.3), use the
same fresh standard Gaussian vector in the residual term of (4.1) and in
the corresponding ideal innovation.  Because (4.1) preserves the fresh
residual after each exposure, these choices define one compatible ideal
array for all \(A_{T,L}^{\rm act}\) actions, rather than a different
coupling at each action.

For fixed admissible \(h\), (3.2) gives a finite set consisting of every
population old-Gram eigenvalue and every population query Schur
complement used in (1.3).  Define

\[
 4\gamma_{T,L,h}
 =\min\{\hbox{that finite set}\}>0.                    \tag{5.1}
\]

Let \({\cal L}_i^{(n)}\) contain every empirical Gram, rectangular cross
block, and query overlap formed up to action \(i\).  Concretely, at a
forward action \((\uparrow,s,\ell)\) this means the old blocks
\(Q_{\ell-1}^{[s-1]},K_\ell^{[s-1]}\), their rectangular action block,
and the new overlaps
\[
 n^{-1}(H_{\ell-1}^{0:s-1})^TH_{\ell-1}^s,\qquad
 n^{-1}(R_{\ell-1}^{0:s-1})^TH_{\ell-1}^s.            \tag{5.2}
\]
At a transpose action \((\downarrow,s,\ell)\), it means the old blocks
\(Q_{\ell-1}^{[s]},K_\ell^{[s-1]}\), their rectangular action block, and
\[
 n^{-1}(C_\ell^{0:s-1})^TC_\ell^s,\qquad
 n^{-1}(X_\ell^{0:s})^TC_\ell^s.                      \tag{5.3}
\]
Empty histories are omitted.  At the terminal action, the ledger also
contains \(n^{-1}(a^T)^TH_L^T\).  These are exactly the quantities
appearing in (4.2)--(4.3); no cross-connector Gram is inverted.

Let
\({\cal G}_0=\Omega\), and, for \(1\le i\le A_{T,L}^{\rm act}\), let
\({\cal G}_i\) be \({\cal G}_{i-1}\) intersected with the events that
the old empirical Grams inverted at action \(i\) have smallest eigenvalue
at least \(2\gamma_{T,L,h}\) and that its new-query Schur complement, if
nonempty, is at least \(2\gamma_{T,L,h}\).  These quantities are
predictable before the fresh residual at action \(i\) is exposed.  Stop
only the conditional representation at the first failed event; leave the
raw network unchanged.  Off the good event, extend inverse coefficients
and innovation scales by their deterministic population values.

## 6. Fully quantified finite-action induction

Fix finite exponents \(p,P\ge2\) and an arbitrary failure exponent
\(m\ge1\).  The required moment orders are fixed before the induction as
follows.  Expand the predictable-query expression at action \(i\) into
the grammar whose leaves have degree one, whose sum degree is the maximum
of its child degrees, whose product degree is the sum of its child
degrees, whose \(\phi\)-composition has degree
\(\max\{1,\deg(\text{child})\}\), and whose bounded
\(\phi^{(r)}\)-composition has degree zero.  Let \(r_i\ge1\) be the
largest degree returned by that finite grammar, including its ledger
products.  Starting from
\[
 R_{A_{T,L}^{\rm act}}=\max\{P,2mP\},
\]
define backwards
\[
 R_{i-1}=2r_iR_i,\qquad
 i=A_{T,L}^{\rm act},\ldots,1.                        \tag{6.0}
\]
This is a terminating list of \(A_{T,L}^{\rm act}\) integer operations.
At action \(i\), use moment order \(R_i\); (6.0) supplies every Hölder
factor needed by (6.2) and every \(2m\)-moment needed by Markov's
inequality.
For every integer

\[
 0\le i\le A_{T,L}^{\rm act},                          \tag{6.1}
\]

we prove the following four assertions.

1. Every stopped field constructed by action \(i\) differs from its
   compatible ideal field by \(O(n^{-1/2})\) in
   \(L^P(\|\cdot\|_{n,p})\).
2. Every stopped and ideal field constructed by action \(i\) has the
   finite \(L^{R_i}(\|\cdot\|_{n,p})\) moments required by all remaining
   operations, uniformly in \(n\).
3. Every entry of \({\cal L}_i^{(n)}\) differs from its population value
   by \(O(n^{-1/2})\) in \(L^P\).
4. For every \(1\le r\le i\),
   \(\mathbb P({\cal G}_r^c\cap{\cal G}_{r-1})=O(n^{-m})\).

At \(i=0\), the leaves \(u^0,a^0\) and the primitive Gaussian reservoirs
are coupled identically.  The coordinates of every initialization-only
ideal observable are iid and have all finite moments.  Rosenthal's
inequality therefore gives assertion 3 for every ledger entry already
formed, at every auxiliary moment order.  Assertions 1, 2, and 4 are then
immediate.

Assume all four assertions at \(i-1\), and consider the unique action
with index \(i\) from (1.5).

*First, form its predictable query.*  It is obtained from old fields and
ledger scalars by the finite sums, products, \(\phi\), and \(\phi'\)
displayed in (1.6)--(1.8).  The weighted activation envelope and the
mean-value theorem give, for a finite exponent depending only on
\((T,L)\),

\[
 |\Psi(x;\theta)-\Psi(x';\theta')|
 \le C(1+\|x\|^r+\|x'\|^r)
 (\|x-x'\|+\|\theta-\theta'\|).                       \tag{6.2}
\]

Assertions 1--3 at \(i-1\), followed by Hölder at the preselected
auxiliary orders, prove the query version of assertions 1 and 2.

*Second, expose the matrix action.*  On \({\cal G}_i\), every inverse in
(4.2)--(4.3) has norm at most \((2\gamma_{T,L,h})^{-1}\), and the square
root is Lipschitz on the innovation-variance interval
\([2\gamma_{T,L,h},\infty\)).  The inverse identity

\[
 A^{-1}-B^{-1}=A^{-1}(B-A)B^{-1}
\]

and assertion 3 at \(i-1\) show that all empirical regression
coefficients and innovation scales differ from their population values by
\(O(n^{-1/2})\) in \(L^P\).  Couple the fresh residuals as in Section 5.
The projection of an independent standard Gaussian onto a fixed number
of old query columns satisfies

\[
 \bigl\|\|P_Vg\|_{n,p}\bigr\|_{L^P(g\mid V)}
 \le C_{T,L,h,p,P}n^{-1/2}\sum_j\|V_j\|_{n,p}.         \tag{6.3}
\]

Equations (4.2)--(4.5), (6.3), and assertions 1--2 at \(i-1\) prove
assertions 1--2 for the new action.

*Third, update the ledger.*  Every new ideal-coordinate ledger observable
has iid coordinates and finite moments.  Rosenthal gives

\[
 \left\|n^{-1}\sum_{a=1}^n\Theta_a-\mathbb E\Theta_1
 \right\|_{L^P}=O(n^{-1/2}).                           \tag{6.4}
\]

The actual-minus-ideal average is \(O(n^{-1/2})\) by (6.2), Hölder, and
the just-proved field estimate.  This includes the rectangular block
\({\cal R}=C^TY/n=D^TH/n\) and all row/transpose query overlaps.
Assertion 3 follows.

*Fourth, update the good event.*  Every relevant population eigenvalue or
Schur complement is at least \(4\gamma_{T,L,h}\).  Weyl's inequality and
the Schur-complement formula reduce failure of its empirical counterpart
to a fixed positive deviation of entries in \({\cal L}_i^{(n)}\).
Repeat (6.4) and the actual-minus-ideal estimate at moment order \(2m\)
or higher.  Markov's inequality then gives

\[
 \mathbb P({\cal G}_i^c\cap{\cal G}_{i-1})=O(n^{-m}), \tag{6.5}
\]

which is assertion 4.  This completes the implication from index \(i-1\)
to index \(i\).  Since (6.1) is the explicit finite integer interval
\(0,\ldots,(2T+1)(L-1)\), the four assertions hold after the terminal
forward action.

## 7. Removing the stopping and terminal uniform integrability

The raw network is bounded without any inverse.  Define nonnegative
majorants from the initialization norms by

\[
 U_0=\|u^0\|_{n,2},\quad A_0=\|a^0\|_{n,2},\quad
 \Omega_{\ell,0}=\|W_\ell^0/\sqrt n\|_{\rm op}.
\]

For each \(0\le s<T\), recursively set

\[
 Z_{1,s}=U_s,\quad H_{1,s}=M_\phi(1+Z_{1,s}),
\]

\[
 Z_{\ell,s}=\Omega_{\ell,s}H_{\ell-1,s},\quad
 H_{\ell,s}=M_\phi(1+Z_{\ell,s}),\qquad2\le\ell\le L,
\]

\[
 C_{L,s}=M_\phi A_s,\quad
 B_{\ell-1,s}=\Omega_{\ell,s}C_{\ell,s},\quad
 C_{\ell-1,s}=M_\phi B_{\ell-1,s},
\]

\[
 A_{s+1}=A_s+|h|H_{L,s},\qquad
 U_{s+1}=U_s+|h|C_{1,s},
\]

\[
 \Omega_{\ell,s+1}=\Omega_{\ell,s}
 +|h|C_{\ell,s}H_{\ell-1,s}.                          \tag{7.1}
\]

At \(s=T\), perform only the forward part of (7.1).  The normalized
Euclidean and operator-norm inequalities for the exact network show
chronologically that every raw field norm is bounded by its namesake in
(7.1).  Because (7.1) has exactly \(T\) update rounds, every terminal
majorant is a polynomial with nonnegative coefficients in

\[
 1+M_\phi+\|u^0\|_{n,2}+\|a^0\|_{n,2}
 +\sum_{\ell=2}^L\|W_\ell^0/\sqrt n\|_{\rm op}.       \tag{7.2}
\]

The Gaussian vector norms and Gaussian matrix operator norms in (7.2)
have moments of every fixed order uniformly in \(n\).  Hence so does every
raw field at this fixed \((T,L,h)\).  By (6.5) and the union bound,

\[
 \mathbb P({\cal G}_{A_{T,L}^{\rm act}}^c)=O(n^{-m})
\]

for arbitrary \(m\).  Hölder, the raw moment bounds, and

\[
 \|x\|_{n,p}\le n^{(1/2-1/p)_+}\|x\|_{n,2}
\]

show that every stopped-versus-raw exceptional-event contribution tends
to zero after choosing \(m\) larger than the displayed finite power of
\(n\).  Thus the unstopped fields and ledgers converge to the compatible
ideal array.

Finally,

\[
 |f_{n,L}^T|\le\|a^T\|_{n,2}\|H_L^T\|_{n,2},
\]

and (7.1)--(7.2) give a uniform \(L^{1+\epsilon}\) bound for some fixed
\(\epsilon>0\).  The terminal outputs are uniformly integrable, and hence

\[
 n^{-1}(a^T)^TH_L^T
 \longrightarrow \mathbb E[a^TH_L^T]=F_{T,L}(h)
\]

in \(L^1\): on the good event this is assertion 3 applied to the terminal
product ledger entry, and the complement vanishes by the preceding raw
bound.  Consequently

\[
 \lim_{n\to\infty}\mathbb E f_{n,L}^{T}(h)=F_{T,L}(h) \tag{7.3}
\]

for every fixed nonzero \(h\) satisfying (3.1).  The same proof stopped
at any \(k\le T\) identifies \(F_{k,L}(h)\).  For \(L=1\), the exact iid
coordinate recursion gives (7.3) directly.  For
\(\phi\equiv\pm1\), \(F_{k,L}(h)=kh\) and no rank argument is needed.

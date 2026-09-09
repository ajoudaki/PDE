# One-sample square loss: exact order-five paired expansion and mesh status

## 1. Convention and exact reduction

Use the half-square loss

\[
 \ell(\theta)=\frac12(1-f(\theta))^2
\]

and the same mean-field-scaled parameter metric as in the feature-ascent
study.  The calculation assumes the established fixed, flat population
metric/adjoint realization; this identification is part of the OMFP bridge,
not a formal change of coordinates.  One gradient-descent step is

\[
 \theta^+=\theta-\eta\nabla\ell(\theta)
 =\theta+\eta(1-f(\theta))\nabla f(\theta).
 \tag{1.1}
\]

Put

\[
 P(\theta)=f(\theta)-\frac12f(\theta)^2.
\]

Then `ell=1/2-P`, and (1.1) is exactly one gradient-ascent Euler step for
`P`.  This is a state-dependent time rescaling of feature ascent, not a
constant replacement of the learning rate.

Let

\[
 v=\nabla P=(1-f)\nabla f,
 \qquad E_hx=x+hv(x),
\]

and define

\[
 D_t^\ell(h)=\ell(E_h^{2t}x_0)-\ell(E_{2h}^{t}x_0).
 \tag{1.2}
\]

For the width-first network, every statement below is applied only after
the fixed-step population DAG and the required local regularity have been
identified.  No finite-width Taylor expansion is interchanged with width.

## 2. Exact order-five pullback formula

For a scalar test function `u`, define the differential operators

\[
 T_ku={1\over k!}D^ku[v,\ldots,v],\qquad k\ge1.
 \tag{2.1}
\]

For `1<=r<=m`, put

\[
 W_{m,r}
 =\sum_{\substack{k_1+\cdots+k_r=m\\k_i\ge1}}
 T_{k_1}\cdots T_{k_r},
 \qquad
 \Lambda_{m,r}=(W_{m,r}\ell)(x_0),
 \tag{2.2}
\]

and

\[
 q_{m,r}(t)={2t\choose r}-2^m{t\choose r}.
 \tag{2.3}
\]

If the population DAG is `C^6` on the complete step segment used below,
then

\[
 \boxed{
 D_t^\ell(h)
 =\sum_{m=2}^{5}h^m\sum_{r=1}^m
 q_{m,r}(t)\Lambda_{m,r}+R_{6,t}(h).}
 \tag{2.4}
\]

Here

\[
 R_{6,t}(h)
 ={h^6\over5!}\int_0^1(1-s)^5
 {d^6\over dh^6}D_t^\ell(sh)\,ds.
 \tag{2.5}
\]

The nonzero rows of (2.3) are

\[
\begin{array}{c|ccccc}
m\backslash r&1&2&3&4&5\\ \hline
2&-2t&t\\[2pt]
3&-6t&-2t^2+3t&2t(t-1)\\[2pt]
4&-14t&-6t^2+7t&-\frac43t^3+6t^2-\frac{14}3t
 &2t^3-\frac{11}2t^2+\frac72t\\[2pt]
5&-30t&-14t^2+15t&-4t^3+14t^2-10t
 &-\frac23t^4+6t^3-\frac{77}6t^2+\frac{15}2t
 &\frac43t^4-7t^3+\frac{35}3t^2-6t.
\end{array}
\tag{2.6}
\]

### Proof

The one-step pullback is the exact Taylor operator

\[
 (U_hu)(x)=u(x+hv(x))
 =\left(I+\sum_{k\ge1}h^kT_k\right)u(x).
\]

Writing `A_h=sum_(k>=1)h^kT_k`, the identical one-step operator occurs at
every time, so

\[
 U_h^N=(I+A_h)^N=\sum_{r=0}^N{N\choose r}A_h^r.
\]

The coefficient of `h^m` in `A_h^r` is exactly `W_(m,r)`.  Subtracting
`U_(2h)^t` from `U_h^(2t)` gives (2.3)--(2.4).  Direct substitution into
(2.3) gives the finite table (2.6).  Taylor's integral theorem gives
(2.5).  This proof terminates after the displayed five rows.

The operators in (2.2) are evaluated at initialization.  In the established
smooth OMFP calculus, source differentiation and Gaussian peeling reduce
each `Lambda_(m,r)` to a terminating Gaussian activation integral.  Thus
they are not constants defined from a trained trajectory or output
supremum.

## 3. Explicit quadratic and cubic terms at depth two

At initialization let

\[
 g=\nabla f,\qquad
 \Theta=\|g\|^2,qquad
 \mathsf H=\|Dg[g]\|^2,qquad
 \mathsf S=D^3f[g,g,g].
 \tag{3.1}
\]

Readout reflection gives

\[
 D^2f[g,g]=0.
 \tag{3.2}
\]

The first two rows of (2.4) reduce to

\[
 \boxed{
 D_t^\ell(h)
 =t\Theta^2h^2
 -{t(2t-1)\over2}
 \{4\Theta^3+\mathsf S+4\mathsf H\}h^3
 +K_{4,\phi}(t)h^4+K_{5,\phi}(t)h^5+R_{6,t}(h),}
 \tag{3.3}
\]

where

\[
 K_{m,\phi}(t)=\sum_{r=1}^mq_{m,r}(t)\Lambda_{m,r},
 \qquad m=4,5.
 \tag{3.4}
\]

In particular, `deg K_(4,phi)<=3` and `deg K_(5,phi)<=4`.

For the `q=1`, two-hidden-layer network,

\[
 \Theta=1+d+d^2,qquad d=\mathbb E\phi'(G)^2.
 \tag{3.5}
\]

The constants `mathsf S,mathsf H` are the already established two-hidden
layer cubic invariants.  To make their activation provenance explicit, set

\[
\begin{array}{lll}
d=\mathbb E p^2,&u=\mathbb E p^4,&v=\mathbb E[g_0q],\\
m=\mathbb E[g_0p^2q],&r=\mathbb E[pr_3],&s=\mathbb E q^2,\\
j=\mathbb E[p^3r_3],&e=\mathbb E[p^2q^2],
&\ell_0=\mathbb E[g_0^2p^2],
\end{array}
\tag{3.6}
\]

where `G~N(0,1)`, `g_0=phi(G)`, `p=phi'(G)`, `q=phi''(G)`, and
`r_3=phi'''(G)`.  Put

\[
 c=1+d,\qquad \beta=v+cr,\qquad
 \delta=d+cs,\qquad k=d+\beta+\delta.
\]

Then

\[
 \mathsf S
 =3c^2m+3c^3j+3du\beta+3dkm+3d^2j,
 \tag{3.7}
\]

\[
\begin{aligned}
 \mathsf H={}&c^2u+c\ell_0+2c^2m+3c^3e+c\,u\,d\,s
 +2ud^2+3d^2e\\
 &+k^2\ell_0+2d\,k\,m.
\end{aligned}
\tag{3.8}
\]

Thus every displayed coefficient through cubic order is an explicit finite
formula in Gaussian activation moments.  Equations (2.2), (2.6), and the
finite source-peeling compiler give the same property at orders four and
five.

## 4. Hard ReLU/leaky-ReLU candidate

For normalized ReLU or conventional normalized leaky ReLU, `d=1`, hence
`Theta=3`.  The smooth `C^6` formula is not applicable at the kink.  If the
two still-open indicator-DAG and marked-source intertwining bridges from
`RELU_LEAKY_FINAL_STATUS.md` are assumed, the previously computed gate
coefficient changes sign because `ell'(0)=-1`.  Consequently

\[
 D_t^\ell(h)
 =9t h^2-tD_{a,b}h|h|+o_t(h^2).
 \tag{4.1}
\]

For positive `h`, this is `t(9-D_(a,b))h^2+o_t(h^2)`.  Formula (4.1) is
conditional; loss training does not close either hard-kink bridge.

## 5. Why no finite expansion decides mesh removal

At every fixed order `m`, (2.3) has degree at most `m-1` in `t`: the
degree-`m` terms in `{2t choose r}` and `2^m{t choose r}` cancel after all
`r` are assembled, equivalently because equal physical time cancels the
exact-flow principal term.  Therefore, at `T=2th`, every fixed-order term
in (2.4) is at most

\[
 C_{m,\phi,T}t^{m-1}h^m=O_{m,\phi,T}(t^{-1}).
 \tag{5.1}
\]

This includes the hard-kink term in (4.1).  The uncontrolled integral
remainder (2.5), or an all-source nonanalytic tail, can nevertheless fail
to be uniform in `t`.  Hence no finite jet, including the complete order-five
jet, proves or disproves a continuous-time limit.

A sufficient state estimate is the following.  On an activation-envelope
defined reachable set through time `T`, suppose

\[
 \|v\|\le M_T,\qquad
 \|v(x)-v(y)\|\le L_T\|x-y\|,qquad
 |\ell(x)-\ell(y)|\le R_T\|x-y\|.
 \tag{5.2}
\]

Then the exact one-pair state defect is

\[
 E_h^2x-E_{2h}x=h\{v(x+hv(x))-v(x)\},
\]

and the hybrid telescope gives

\[
 \boxed{
 |D_t^\ell(h)|
 \le R_TL_TM_T\,t h^2e^{2L_Tt|h|}.}
 \tag{5.3}
\]

For `h=T/(2t)`, the right side is

\[
 {R_TL_TM_TT^2e^{L_TT}\over4t},
\]

which is summable along dyadic refinements.  This proves scalar dyadic mesh
convergence, and the analogous state bound plus generator consistency proves
the population flow.

For nonlinear reused-matrix OMFP, (5.2) has not been derived from activation
envelopes on a restartable reachable set.  Defining its constants by a
supremum over the unknown trained trajectory would be circular.  Exact
ReLU/leaky-ReLU also lack a classical Lipschitz vector field at their gate
surfaces.  Therefore the current rigorous verdict is:

* the loss discrepancy is compatible with an ordinary first-order
  continuous-time limit;
* neither the quadratic kink term nor the super-fifth feature-ascent
  construction refutes that limit;
* the actual nonlinear width-first loss-gradient flow remains open until a
  reachable state stability estimate such as (5.2), or a proved Osgood/BV
  replacement, is supplied.

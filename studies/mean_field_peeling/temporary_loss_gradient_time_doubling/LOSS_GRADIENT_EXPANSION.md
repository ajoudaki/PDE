# Loss-gradient time doubling for one sample

## 1. Setup and claim status

Use the same scalar-input, two-hidden-layer, width-first OMFP network as in
the feature-ascent studies.  Let $f$ denote its population output and let
$g$ denote the population feature-gradient field, with the constant
μP metric absorbed into $g$.  For the single label $y=1$, put

\[
 r=1-f,  \ell={r^2\over2},  v=-\nabla\ell=r g.
\]

Thus one loss-gradient descent step is

\[
 E_h(x)=x+h v(x).
\]

At finite width this is the exact identity

\[
 \theta^+=\theta-hn\nabla_\theta\ell
          =\theta+h(1-f_n)n\nabla_\theta f_n.
\]

For every fixed finite schedule, the smooth-activation OMFP chronology is
unchanged except that every learned rank-one update is multiplied by the
current scalar residual.  Output concentration makes that multiplier
deterministic in the width limit.  The calculation below is therefore made
inside the already identified width-first population DAG.  It is not a
finite-width Taylor expansion.

Write

\[
 L_N(h)=\ell(E_h^Nx_0), 
 \mathfrak D_t(h)=L_{2t}(h)-L_t(2h).
\]

For hard ReLU and leaky-ReLU, the differentiable expansion below remains
conditional on the unresolved indicator-DAG and singular-boundary
identification.  The exact pullback algebra itself does not require a
neural-network interpretation.

## 2. Exact pullback coefficients through order five

For a scalar test function $u$, define

\[
 \mathcal T_k u(x)
 ={1\over k!}D^ku(x)[v(x),\ldots,v(x)],  k\ge1,
\]

and, for $1\le q\le m$,

\[
 \mathcal W_{m,q}
 =\sum_{\substack{k_1+\cdots+k_q=m\\k_i\ge1}}
   \mathcal T_{k_1}\cdots\mathcal T_{k_q}.
\]

Operators act from right to left.  Set

\[
 \Lambda_{m,q}
 = (\mathcal W_{m,q}\ell)(x_0).
\]

These numbers have the finite recursion

\[
 U_{0,0}=\ell,  U_{m,0}=0\ (m>0),
\]

\[
 U_{m,q}
 =\sum_{k=1}^{m-q+1}\mathcal T_kU_{m-k,q-1}, 
 \Lambda_{m,q}=U_{m,q}(x_0).
\]

The recursion strictly decreases $m$, so it terminates.  Applied to the
width-first OMFP initialization germ, it is a finite Gaussian activation
integral compiler; it uses no nonzero-time output supremum or trained
trajectory constant.

Indeed, for the pullback $P_hu=u\circ E_h$,

\[
 P_h=I+A_h,  A_h=\sum_{k\ge1}h^k\mathcal T_k.
\]

There is one operator $A_h$, so the ordinary binomial identity gives

\[
 [h^m]L_N(h)
 =\sum_{q=1}^m{N\choose q}\Lambda_{m,q}.
\]

Consequently

\[
 [h^m]\mathfrak D_t(h)
 =\sum_{q=1}^m
 \left\{{2t\choose q}-2^m{t\choose q}\right\}\Lambda_{m,q}.
\tag{2.1}
\]

The linear coefficient vanishes.  Through degree five, (2.1) is

\[
\begin{aligned}
 [h^2]\mathfrak D_t
 &=-2t\Lambda_{2,1}+t\Lambda_{2,2},\\
 [h^3]\mathfrak D_t
 &=-6t\Lambda_{3,1}+(-2t^2+3t)\Lambda_{3,2}
   +2t(t-1)\Lambda_{3,3},\\
 [h^4]\mathfrak D_t
 &=-14t\Lambda_{4,1}+(-6t^2+7t)\Lambda_{4,2}\\
 &\quad+⁠\left(-{4\over3}t^3+6t^2-{14\over3}t\right)\Lambda_{4,3}
 +\left(2t^3-{11\over2}t^2+{7\over2}t\right)\Lambda_{4,4},\\
 [h^5]\mathfrak D_t
 &=-30t\Lambda_{5,1}+(-14t^2+15t)\Lambda_{5,2}\\
 &\quad+(-4t^3+14t^2-10t)\Lambda_{5,3}\\
 &\quad+⁠\left(-{2\over3}t^4+6t^3-{77\over6}t^2
                   +{15\over2}t\right)\Lambda_{5,4}\\
 &\quad+⁠\left({4\over3}t^4-7t^3+{35\over3}t^2-6t\right)
       \Lambda_{5,5}.
\end{aligned}
\tag{2.2}
\]

If the paired width-first map is $C^6$ on the relevant segment, the
corresponding exact Taylor identity is

\[
 \mathfrak D_t(h)
 =\sum_{m=2}^5h^m[h^m]\mathfrak D_t
 +{h^6\over5!}\int_0^1(1-s)^5
      \mathfrak D_t^{(6)}(sh)\,ds.
\tag{2.3}
\]

Equation (2.3) is an identity, not a time-uniform remainder theorem.

## 3. Explicit quadratic and cubic coefficients

All quantities in this section are evaluated in the width-first population
germ at initialization.  Let

\[
 A=Df[g],  B=D^2f[g,g], 
 C=D^3f[g,g,g],  H=\|Dg[g]\|^2.
\]

The gradient identity in the constant μP metric gives

\[
 B=Df[Dg[g]].
\]

Feature-ascent parity makes $F_1(h)$ odd, hence $B=0$.  Direct
differentiation of ℓ gives

\[
 \Lambda_{2,1}={A^2\over2}, 
 \Lambda_{2,2}=2A^2.
\tag{3.1}
\]

For cubic order, use (D_gA=2B) and

\[
 D_gB=C+2H.
\tag{3.2}
\]

Since $r=1$ and $B=0$ at initialization, differentiating

\[
 \mathcal T_1\ell=-r^2A, 
 \mathcal T_2\ell={1\over2}(r^2A^2-r^3B)
\]

gives

\[
\begin{aligned}
 \Lambda_{3,1}&=-{C\over6},\\
 \Lambda_{3,2}&=-2A^3-{3\over2}C-2H,\\
 \Lambda_{3,3}&=-4A^3-2C-4H.
\end{aligned}
\tag{3.3}
\]

For example,

\[
 \mathcal T_1\mathcal T_2\ell
 =-A^3-{C\over2}-H, 
 \mathcal T_2\mathcal T_1\ell=-A^3-C-H,
\]

whose sum is the middle line of (3.3).

For two hidden layers, let

\[
 d=\mathbb E\phi'(G)^2,  A=1+d+d^2.
\]

Comparison with the already established feature-ascent cubic recursion
identifies

\[
 C=\mathsf S_\phi,  H=\mathsf H_\phi, 
 J_\phi=\mathsf S_\phi+4\mathsf H_\phi.
\]

Substitution of (3.1)--(3.3) into (2.2) proves

\[
\boxed{
 \mathfrak D_t(h)
 =tA^2h^2
 -{t(2t-1)\over2}\bigl(4A^3+J_\phi\bigr)h^3
 +K_{4,\phi}(t)h^4+K_{5,\phi}(t)h^5+R_{6,t}(h),
}
\tag{3.4}
\]

where $K_{4,\phi}$ and $K_{5,\phi}$ are exactly the fourth and fifth
rows of (2.2).  They are activation-defined polynomials of degrees at most
three and four, respectively.

For normalized ReLU and normalized leaky-ReLU, $d=1$, so $A=3$ and
the analytic quadratic term is $9t h^2$.  Formula (3.4) itself is not
claimed for these hard activations because their singular boundary terms
must first be identified.

## 4. What this proves about mesh removal

Put $T=2th$.  Every displayed coefficient in (2.2) has time degree at
most $m-1$.  Hence each of the terms of orders two through five is

\[
 O_{\phi,T}(t^{m-1}h^m)=O_{\phi,T}(t^{-1}).
\]

Thus no finite jet through order five obstructs a continuous-time limit.
The leading discrepancy is the usual first-order Euler global error,

\[
 tA^2h^2={A^2T^2\over4t}.
\]

A finite jet cannot prove mesh removal.  Here is an exact sufficient
estimate.  Suppose that on a population reachable tube through total time
$T$,

\[
 \|v\|\le M,  \|Dv\|\le L,  \|D\ell\|\le R.
\tag{4.1}
\]

The exact local state defect satisfies

\[
 E_h^2x-E_{2h}x
 =h\{v(x+hv(x))-v(x)\},
\]

and therefore has norm at most $LMh^2$.  Propagating it across $t$
macro-steps with

\[
 \operatorname{Lip}(E_h^2)\le(1+L|h|)^2
\]

gives

\[
 |L_{2t}(h)-L_t(2h)|
 \le RLM\,t h^2 e^{2Lt|h|}.
\tag{4.2}
\]

At $h=T/(2t)$,

\[
 |L_{2t}(h)-L_t(2h)|
 \le {RLMT^2e^{LT}\over4t}.
\tag{4.3}
\]

This is summable along dyadic refinement and therefore proves a scalar
continuous-time limit if (4.1) holds uniformly for the width-first
population state.

The current OMFP results do not supply (4.1) on a horizon-uniform
all-source reachable tube for the actual reused-matrix state.  Consequently
the fifth-order calculation is compatible with continuous time and (4.2)
gives a precise sufficient theorem, but it does not by itself establish an
unconditional continuous-time limit.

## 5. Conditional hard-kink consequence

If the separately proposed ReLU/leaky-ReLU boundary identification is
eventually proved and its feature-output coefficient is

\[
 F_{2t}(h)-F_t(2h)=tD_{a,b}h|h|+o_t(h^2),
\]

then the loss observable reverses that boundary contribution at leading
order, while the residual multiplier contributes the analytic term in
(3.4):

\[
 L_{2t}(h)-L_t(2h)
 =tA^2h^2-tD_{a,b}h|h|+o_t(h^2).
\tag{5.1}
\]

For positive learning rate and normalized ReLU/leaky-ReLU this becomes

\[
 t(9-D_{a,b})h^2+o_t(h^2).
\]

Even this kink term is $O(T^2/t)$ at fixed total time.  It is not a
continuous-time obstruction.  Equation (5.1) remains conditional for the
same two nonsmooth OMFP bridges as the underlying feature-output formula.

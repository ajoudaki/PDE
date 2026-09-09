# Final claim status: ReLU, leaky ReLU, and smooth ReLU-like activations

## Object

For the `q=1`, two-hidden-layer network, put

\[
 \Delta_t^\phi(h)=F_{2t}^\phi(h)-F_t^\phi(2h),
 \qquad
 \mathcal B_\phi(t,\rho)
 =\inf_{\kappa\in\mathbb R}\sup_{0<|h|\le\rho/t}
 { |\Delta_t^\phi(h)-\kappa h^3|\over |h|^5}.
\]

## Hard kink: proved calculation and open bridge

For

\[
 \phi_{a,b}(x)=
 \begin{cases}ax,&x\ge0,\\ bx,&x<0,\end{cases}
 \qquad 0\le b<a,\qquad {a^2+b^2\over2}=1,
\]

let

\[
 e={a^4+b^4\over2},\qquad
 p=Y+2bA,\qquad q=Y+2aA,
\]

where `A~N(0,1)` and `Y~N(0,e)` are independent.  The exact affine-hinge
calculation for one marked top gate gives

\[
 D_{a,b}=\gamma(0)\mathbb E[(a-b)Apq
 \mathbf1_{\{p>0\ \mathrm{or}\ q<0\}}]>0.
\]

Equivalently,

\[
 D_{a,b}={3(a-b)\over4\pi\sqrt e}
 \int_{2b}^{2a}{(y-2b)(2a-y)\over(1+y^2/e)^{5/2}}\,dy.
\]

The exact all-horizon scalar identity is `J_t=tJ_1`.  If the proposed
indicator-valued OMFP DAG is identified with the actual fixed-step network
and its marked-source response paths intertwine with the full terminal
gradient, these facts imply

\[
 \Delta_t(h)=tD_{a,b}h|h|+o_t(h^2)
\]

and hence `mathcal B_phi(t,rho)=+infinity` for every fixed `t,rho`.

Those two bridges are not currently proved.  In particular, the existing
smooth-activation width theorem cannot be applied to the discontinuous
derivative, and a finite-width sign-cell expansion followed by exchanging
the width and step limits is invalid.  Therefore the displayed hard-kink
network conclusion remains **conditional/open**.

For normalized ReLU the audited candidate constant is

\[
 D_{\rm ReLU}={\sqrt2\over\pi}\left(1-{1\over\sqrt5}\right).
\]

## Smooth ReLU-like activation: unconditional result

For every leak `lambda in [0,1)`, smoothing scale `tau>0`, tolerance
`epsilon>0`, and `rho>0`, there is one RMS-normalized activation
`widetilde phi` which is `C^infinity`, globally bounded-slope, linearly
growing, and satisfies

\[
 d_1(\widetilde\phi,\phi_{\lambda,\tau}^{\rm base})<\epsilon,
 \qquad
 \phi_{\lambda,\tau}^{\rm base}
 ={b_{\lambda,\tau}\over\|b_{\lambda,\tau}(G)\|_2},
\]

with

\[
 d_1(f,g)=\sup_x{|f(x)-g(x)|\over1+|x|}+\|f'-g'\|_\infty,
\]

where the base is the RMS-normalized exact-affine-tail smooth
ReLU/leaky-ReLU from `SMOOTH_RELU_LADDER.md`, and such that

\[
 \boxed{
 \mathcal B_{\widetilde\phi}(N,\rho)
 \ge {3\over5}N^{N+6}-2\ge N^N,
 \qquad N\ge2.}
\]

This is unconditional relative to the already audited smooth full-`L=2`
insertion theorem.  It is a statement about exact fixed-nonzero-step
width-first outputs, not about a formal fifth jet of the final activation.
The construction uses a smooth compact transition near zero and an
arbitrarily small, locally finite ladder of compact derivative bumps in the
positive affine tail.  The unperturbed ordinary softplus or unperturbed
single-scale smoothing is not classified by this theorem.

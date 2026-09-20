# Zero training loss alone does not organize closure-order endpoints

Lead candidate, 2026-09-20. Exact population hierarchy of
docs/global_nonlinear.md C.4.7.10.B; no other study is an input.

Fix any finite compatible circle dataset and merge repeated/antipodal
constraints, leaving normalized directions u_1,...,u_m distinct modulo sign.
Choose a further direction u_* outside those classes. All labels are bounded.
Let H_p^0(u)=tanh(B_p tanh(g dot u)) be the initialized upper fields on their
common canonical carrier, and H^0(u)=tanh(A_0 tanh(g dot u)).

The full augmented family (H^0(u_1),...,H^0(u_m),H^0(u_*)) has positive
definite unweighted Gram G. Here is the required elementary justification.
If a linear combination of tanh(g dot u_i) vanishes in Gaussian L2, it
vanishes everywhere by continuity and Gaussian full support. Restrict g to
t v for a direction v with nonzero, pairwise distinct absolute projections
on all the u_i. All odd Taylor coefficients of tanh are nonzero: from
tanh'=1-tanh^2 their alternating positive magnitudes satisfy
(2k-1)a_k=sum_(i+j=k)a_i a_j, a_1=1. The first m+1 odd derivatives therefore
form an invertible Vandermonde system, proving lower-feature independence.
The initialized forward-query vector is consequently a nondegenerate
Gaussian. A linear combination of its coordinatewise tanh functions can
vanish almost surely only if it vanishes everywhere; vary one coordinate
at a time to force each coefficient to zero. This proves G>0.

Strong convergence B_p->A_0 is uniform on the compact initialized lower
feature image. Thus H_p^0(u)->H^0(u) uniformly in u in L2, and the finite
augmented Grams G_p converge to G. There is p0 such that
G_p>=lambda_min(G) I/2 for every p>=p0.

For each such p, set z_p=(y_1,...,y_m,(-1)^p) and choose the bounded readout

\[
 c_p=\sum_{j=1}^{m+1}(G_p^{-1}z_p)_j H_p^0(u_j),
 \qquad u_{m+1}=u_*.
\]

Its boundedness at each order follows from |H_p^0|<=1 and the finite sum.
Matrix multiplication proves exactly

\[
 f_p(u_i)=y_i\quad(1\le i\le m),\qquad f_p(u_*)=(-1)^p.
\]

Moreover

\[
 \|c_p\|_2^2=z_p^T G_p^{-1}z_p
 \le \frac{2(1+\sum_i y_i^2)}{\lambda_{\min}(G)}.
\]

The hidden parameters are exactly their own canonical initialization w=g,
M=D_p, so both hidden displacements are zero. The readout norms are uniformly
bounded, and ||B_p||op<=2. Every state has zero training loss and is an
equilibrium of its own exact closure gradient flow. Nevertheless

\[
 \|f_{p+1}-f_p\|_{C(\sqrt2 S^1)}\ge2
 \qquad(p\ge p0).
\]

This is a counterexample to deducing cross-order predictor closeness from
interpolation and bounded displacement alone, in the actual closure state
spaces. It is NOT a counterexample to endpoint convergence from the prescribed
canonical initial readout c=0. No reachability claim for these particular
equilibria is made. The dynamics' selection rule, not just fitting, is an
essential hypothesis of any positive endpoint theorem.

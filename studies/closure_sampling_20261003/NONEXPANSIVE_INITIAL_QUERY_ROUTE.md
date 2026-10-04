# Real query derivatives at Gaussian initialization need no depth factor

2026-10-04. Bounded independent calculation by the coordinator during the
activation/depth-constant continuation. This is an initialization theorem
and an explicitly unclosed training extension, not an all-time compression
theorem or a lower bound. No experiment or other-study input was used.
The model and normalizations are those in INPUT_DIMENSION_REFINEMENT.md
and SPHERICAL_SOURCE_DIMENSION_ROUTE.md. Required notation, neural-network,
rigorous-proof, and research-audit instructions were applied.

## 1. A uniform initialization estimate

Fix input dimension d and hidden depth L. Let A have independent N(0,1)
entries and each W^(ell), ell>=2, independent N(0,1/n) entries, with all
blocks independent. Write

\[
z^{(1)}(v)=Av,\qquad
z^{(\ell)}(v)=W^{(\ell)}\phi_{\ell-1}(z^{(\ell-1)}(v)),
\qquad J^{(\ell)}(v,u)=D_vz^{(\ell)}(v)[u].
\]

Assume each real activation is C^2, |phi'_ell|<=1 and |phi''_ell|<=T
for a fixed finite T. Bounded activation values are unnecessary here.
Use ||a||_(2,n)=||a||_2/sqrt(n). For every fixed epsilon>0,

\[
\Pr\left\{\sup_{\|v\|\le1,\ \|u\|=1}
       \max_{1\le\ell\le L}\|J^{(\ell)}(v,u)\|_{2,n}
                   \le1+\epsilon\right\}\longrightarrow1.
\tag{1}
\]

The leading constant in (1) does not grow with L. The width threshold
and the convergence rate in this statement may depend on fixed L,d,T
and epsilon. In particular this does not assert a joint growing-depth
limit.

To prove it, first restrict to the Gaussian operator event
||A||_op/sqrt(n)<=2 and ||W^(ell)||_op<=8. The elementary Gaussian
net estimate used by the source proof gives probability tending to one,
with exponentially small failure at fixed d,L. The exact tangent
recursion is

\[
J^{(1)}=Au,\qquad
J^{(\ell)}=W^{(\ell)}q^{(\ell-1)},\qquad
q^{(\ell-1)}=\phi'_{\ell-1}(z^{(\ell-1)})\odot J^{(\ell-1)}.
\tag{2}
\]

The operator event gives deterministic bounds
sup||J^(ell)||_(2,n)<=2*8^(ell-1). Differentiating (2) once more
with respect to v and using
||a b||_(2,n)<=sqrt(n)||a||_(2,n)||b||_(2,n) gives

\[
\sup_{\|u\|=\|w\|=1,\ \|v\|\le1}
\|D_vJ^{(\ell)}(v,u)[w]\|_{2,n}\le C_{L,T}\sqrt n.
\tag{3}
\]

The same estimate holds for q; its dependence on u is linear with a
bounded operator norm. These coarse estimates are used only for filling
in a net, never as the final depth-dependent multiplier.

Choose deterministic nets of mesh n^-2 in the unit ball and unit sphere.
Their joint cardinality is at most C_d n^(4d). Conditional on all layers
below ell, every q^(ell-1) at a net point is independent of W^(ell).
For any nonzero fixed q,

\[
\frac{\|W^{(\ell)}q\|_{2,n}^2}{\|q\|_{2,n}^2}
                          \overset{d}=\frac{\chi_n^2}{n}.
\]

The Gaussian-square moment-generating function therefore gives, for
0<eta<1,

\[
\Pr\{\|Wq\|_{2,n}>(1+\eta)\|q\|_{2,n}\mid q\}
                                      \le e^{-c\eta^2n}.
\tag{4}
\]

For q=0 the event is empty. The estimate is uniform in the conditioned
lower layers. A union bound over the polynomial net and finitely many
layers is valid without conditioning on the full operator event. On
its intersection with that event, (3) fills in the net with additive
error C_(L,T)n^-3/2. Since |phi'|<=1, (2)-(4) imply

\[
\sup_{v,u}\|J^{(\ell)}\|_{2,n}
 \le (1+\eta)\sup_{v,u}\|J^{(\ell-1)}\|_{2,n}+o(1).
\]

Finally ||A||_op/sqrt(n) tends to one for fixed d: apply the same
Gaussian-square bound to a fixed sufficiently fine net of S^(d-1)
and use the operator norm net inequality. Choose eta so that
(1+eta)^L<1+epsilon/2, and take n large. This proves (1).

## 2. Initial coordinate maxima have the same improvement

The preceding argument also yields, at sufficiently large width,

\[
\Pr\left\{\max_{\ell,i}\sup_{\|v\|\le1,\|u\|=1}
 |J_i^{(\ell)}(v,u)|\le
            16\sqrt{(d+3)\log(en)}\right\}\longrightarrow1.
\tag{5}
\]

For ell>=2 condition on the lower layers; on their own version of
(1) with epsilon=1, the Gaussian row pairing has variance at most four.
Take the preceding polynomial net, then union over its points and nL
row coordinates. A threshold 8 sqrt((d+3)log(en)) has tail exponent
at least 8(d+3)log(en), exceeding the net/coordinate exponent 4d+1.
The complement of the lower-layer event has probability tending to
zero. The first layer is the simpler Gaussian pairing A_i u. The
coordinate modulus from (3) is at most C_(L,T)n, so net filling costs
O(n^-1). The factor two in (5) leaves a strict margin. All conditioning
is on lower layers, not on full-network survival.

Thus the source proof's factor (10s)^(L-1) is not necessary for real
query tangents at initialization for tanh, identity, or any activation
with nonexpansive real slope. This result concerns derivatives of hidden
preactivations; it is not merely the zero initialized output.

## 3. The attempted all-time extension and its exact open term

On the actual training trajectory define J as above using A(t),W(t).
Its time derivative satisfies

\[
\begin{split}
\dot J^{(1)}&=\dot A u,\\
\dot J^{(\ell)}&=\dot W^{(\ell)}[\phi'J^{(\ell-1)}]
 +W^{(\ell)}[\phi''\dot z^{(\ell-1)}J^{(\ell-1)}]
 +W^{(\ell)}[\phi'\dot J^{(\ell-1)}].
\end{split}
\tag{6}
\]

Here every gate is evaluated at the current lower-layer preactivation.
If R_a^(ell)=D_Theta z^(ell) grad_Theta(n f_a) is the source proof's
residual-free response in mobility coordinates, then
dot z^(ell)=-(2/m)sum_a r_a R_a^(ell). The middle term of (6) requires
control of the actual mixed quantity

\[
 \sup_{t,v,u,a}\|R_a^{(\ell)}(t,v)
                         J^{(\ell)}(t,v,u)\|_{2,n}.
\tag{7}
\]

Separate RMS estimates do not bound (7). Using coordinate maxima gives
a sqrt(log n) loss, which cannot be absorbed by a fixed positive label
size uniformly for all width. Holder would instead use fourth moments
of both factors, but a uniform adaptive bound for their product, with
the needed depth dependence, has not been proved in this calculation.
Moreover the row used in (4) is reused in training. Lower-layer
conditioning therefore ceases to justify its independent Gaussian law.
An actual insertion comparison, including its adaptive mean and mixed
responses, is required.

This identifies an unclosed step, not evidence that a depth-independent
training estimate is false. Failure of a neuron maximum estimate would
not imply failure of the weighted mixed-moment route. The present note
does not supply that route or use the initialization lemma as a premise
for an unproved all-time compression improvement.

## 4. Relevance to the current refinement

The separately derived activity-sensitive source constants retain small
label factors in the learned corrections and sharpen the proved all-time
radius without requiring (7). A contractive activation subclass can
bound the deterministic layer products directly. Those are distinct
routes. For ordinary tanh, (1)-(5) show that removing the remaining
geometric layer product is a concrete adaptive-response problem, not
an unavoidable effect already present at initialization.

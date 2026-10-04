# Check of the general explicit dense-fitting theorem

2026-10-04. Scoped mathematical reconstruction. Scientific input: the complete
`GENERAL_EXPLICIT_FITTING.md`, SHA-256
`3bead0ab281dcd6a7120643ab1a2b13c52b6dc5b6626792eb2d6e7ea8d0b1b71`.
The subsequent formatting-only change to the width and beta displays was
inspected; the final source hash is
`5c6f12b78847a2b2874c5bc82eb1cea5f4929ee071b114d09b098397c5e2b8d6`.
No older study, other report, or external scientific source was consulted
for this fitting check. The source was reread completely after the beta
envelope was made explicit; the recorded hash identifies that revision.
The canonical-notation skill, its neural-network conventions, and the
rigorous-math skill were applied. This is an internal component check, not
promotion review.

## Finding

The quantitative initialization theorem (5)--(6), all-time fitting theorem
(7)--(10), and uniform sphere tail (11) are valid under their stated real
assumptions. They require no bounded activation values, Gaussian forward
normalization, sample separation, or additional training geometry beyond
unit input norms and the stated positive top-layer covariance gap.

The revised Section 6 defines its strip-activation envelope explicitly.
It satisfies \(\beta_\partial\ge\max\{10,b,s\}\), which verifies the
previously missing premise \(\beta_\partial\ge6\). Thus the
\(\beta_\partial^{-5L}\) label cap is sufficient, with no unresolved issue
in this component. The envelope is finite for the stated holomorphic strip
class: a uniform bound on the first derivative on the full strip bounds
the second and third derivatives on the half-strip by Cauchy's formula.

## Exact flow and loss factors

Write \(\mathcal L=\|r\|_2^2/m=\rho^2\), where
\(r_a=w^\top h_a^{(L)}/n-y_a\). The backward signals in (1) obey

\[
\nabla_A\mathcal L=\frac{2}{mn}\sum_a r_a\delta_a^{(1)}v_a^\top,
\quad
\nabla_{W^{(\ell)}}\mathcal L
=\frac{2}{mn}\sum_a r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},
\quad
\nabla_w\mathcal L=\frac{2}{mn}\sum_a r_a h_a^{(L)}.
\]

Thus (1) has mobility \(n\) on \(A,w\), and mobility one on each hidden
matrix. For the parameter norm stated in the source,

\[
-\dot{\mathcal L}
=n\|\nabla_A\mathcal L\|_F^2
 +\sum_{\ell=2}^L\|\nabla_{W^{(\ell)}}\mathcal L\|_F^2
 +n\|\nabla_w\mathcal L\|_2^2
=\|\dot\theta\|_{\rm par}^2.
\]

There is no missing factor of two or width factor in (16). If
\(K=\mathsf H^\top\mathsf H/(mn)\) and
\(\lambda_{\min}(K)\ge\lambda/4\), the readout contribution alone gives

\[
\|\dot w\|_2^2/n
=\frac4m r^\top K r
\ge\lambda\rho^2.
\]

Consequently \(\rho(t)\le Y e^{-\lambda t/2}\) and
\(\int_0^T\rho\,dt\le2Y/\lambda\) on each stopped interval. While
\(\rho>0\),

\[
\int_0^T\frac{\|\dot\theta\|_{\rm par}^2}{\rho}\,dt
=2(Y-\rho(T))\le2Y.
\]

Weighted Cauchy--Schwarz therefore gives
\(\int_0^T\|\dot\theta\|_{\rm par}\,dt\le2Y/\sqrt\lambda\).
If the residual reaches zero, every block velocity vanishes. This also
justifies the zero-residual treatment in the source.

## Initialization probability and covariance propagation

For independent Gaussian initialization, two \(1/4\)-nets give
\(\|B\|_{\rm op}\le2\max|u^\top Bv|\). A fixed bilinear form has
variance \(1/n\) for a hidden matrix and variance one for \(A\).
Applying the Gaussian tail at thresholds \(4\) and \(4\sqrt n\),
respectively, gives exactly

\[
2e^{-(8-2\log9)n},\qquad
2e^{-(8-\log9)n+d\log9}.
\]

The logarithmic terms in (5) allocate less than \(\delta/2\) to the
union of all \(L-1\) hidden matrices and \(A\). Both denominators in
(5) are positive.

For a positive definite covariance \(C\), differentiating the Gaussian
density gives the identity
\(D\mathbb E_C g(Z)[E]=\tfrac12\sum_{ij}E_{ij}\mathbb E_C\partial_{ij}g(Z)\).
Here \(g(Z)=\phi_\ell(Z_a)\phi_\ell(Z_b)\) is \(C^2\), grows at most
quadratically, and its Hessian grows at most linearly, so the density
differentiation and two integrations by parts are justified. The two
off-diagonal Hessian entries combine to coefficient \(E_{ab}\), giving
(13). When \(a=b\), the derivative is

\[
E_{aa}\mathbb E\big[(\phi_\ell')^2+\phi_\ell\phi_\ell''\big].
\]

Along covariance segments with diagonals at most \(2H^2\),
\(\mathbb E|\phi_\ell(Z_a)|\le b+\sqrt2sH\). Bounding the three terms
of (13) gives precisely
\(A_*=s^2+t_2(b+\sqrt2sH)\), without a factor depending on the number
of samples. Singular endpoints can be regularized by adding
\(\varepsilon I\) to the whole segment. The bound then has
\(b+s\sqrt{2H^2+\varepsilon}\) in place of
\(b+\sqrt2sH\); taking \(\varepsilon\downarrow0\) proves the stated
constant. The scalar variance map has the same estimate.

For variance at most \(2H^2\),

\[
\mathbb E|\phi_\ell(Z)|^4
\le8b^4+8s^4\mathbb E|Z|^4
\le8b^4+96s^4H^4=M_4.
\]

Cauchy--Schwarz gives second moment at most \(M_4\) for each covariance
product. Conditional on all preceding layers, the next layer's rows are
independent Gaussians with covariance equal to the preceding empirical
Gram. Each empirical entry therefore has conditional variance at most
\(M_4/n\). At tolerance \(e/T_L\), its conditional failure probability
is at most \(M_4T_L^2/(ne^2)\).

Define the tests in increasing layer order. If all tests through layer
\(\ell-1\) have passed, entrywise covariance error and each net-query
variance error at that layer are at most
\((e/T_L)\sum_{j=0}^{\ell-2}A_*^j\le e\).
Every next conditional variance is thus at most \(H^2+e<2H^2\),
so the conditional bound applies. A union bound at the first failing
layer, over \(m^2\) training entries and at most \(P\) query variances,
gives (15). Dependence between queries or between different tests does
not affect this argument. A full Gram matrix for the query net is
unnecessary.

The resulting top empirical training Gram has operator error at most
\(me\le\gamma/2\). Dividing its least eigenvalue bound by \(m\)
gives the gap in (6).

The deterministic sphere extension also checks. On the matrix event,
the normalized feature map at layer \(\ell\) is \((8s)^\ell\)-Lipschitz.
On the query net its norm is at most
\(\sqrt{H^2+e}\le\sqrt{5/4}H\). The stated choice of \(h\) gives
\((8s)^Lh\le H/4\) in both branches of its definition. Thus the
whole-sphere norm is at most
\((\sqrt{5/4}+1/4)H<3H/2\). Adding the matrix and covariance failure
budgets proves the full probability claim for every
\(n\ge N_{\rm fit}(\delta)\).

## Hidden motion, continuation, and endpoint tail

Let \(u=\|w\|_2/\sqrt n\). On the stopped tube, backward propagation
gives \(\|\delta_a^{(\ell)}\|_2/\sqrt n\le D_\ell u\). Hence the
normalized hidden block velocities are bounded by
\(2\rho U_\ell u\). Integrating, using
\(u\le2Y/\sqrt\lambda\), proves the constants
\(8U_\ell Y^2/\lambda^{3/2}\) in (10).

Feature subtraction and differentiation both obey the recursion with
coefficient \(s(2H U_\ell+9F_{\ell-1})\). Unrolling it at the top
layer gives exactly

\[
F_L=s^2(9s)^{2L-2}
 +4H^2s^2\sum_{j=0}^{L-2}(9s)^{2j}.
\]

The sequence \(F_\ell\) is increasing, and its final value dominates
every \(U_\ell\) and one, since \(s,H\ge1\). Thus the common
displacement bound used in the bootstrap is valid.

The label condition is \(Y\le\lambda/(8H\sqrt F)\), so

\[
8FY^2/\lambda^{3/2}
\le\frac{\sqrt\lambda}{8H^2}
\le\frac1{8H},
\qquad \lambda=\gamma/m\le H^2/m\le H^2.
\]

The mixer and feature bounds strictly improve their stopping caps.
For \(\mathsf H/\sqrt{mn}\), the operator perturbation is at most
the largest normalized sample-feature displacement, hence at most
\(\sqrt\lambda/(8H^2)\). Its least singular value remains at least

\[
\sqrt\lambda\left(\frac1{\sqrt2}-\frac18\right)
>\frac{\sqrt\lambda}{2}.
\]

This strictly improves the stopped gap. The whole-sphere cap is a
continuous function of the finite-dimensional parameters because the
unit sphere is compact. There is consequently no finite first exit.
The \(C^2\) activations make the finite-dimensional vector field locally
Lipschitz; finite path length prevents finite-time escape, and implies
convergence of every parameter for each finite width. Residual decay
then gives exact fitting at the limiting parameters.

Finally,

\[
\|\dot w\|_2/\sqrt n\le4H\rho,
\qquad
\sup_{\|v\|=1}\|\dot h^{(L)}(v)\|_2/\sqrt n\le2\rho Fu.
\]

Differentiating \(f_n=w^\top h^{(L)}/n\) therefore gives
\(|\dot f_n|\le8H^2\rho+2F\rho u^2
\le8(H^2+FY^2/\lambda)\rho\), uniformly on the sphere.
Its integral is the first bound in (11). The second follows from
\(FY^2/\lambda\le\lambda/(64H^2)\le1/64\) and \(H\ge1\).
The tail is uniform in width after the initialization event, in query
direction, and in physical time, with the displayed problem-dependent
constants.

## Verification of the beta simplification

The revised envelope satisfies \(\beta_\partial\ge\max\{10,b,s\}\).
Minkowski's inequality
gives \(\sqrt{q_\ell}\le b+s\sqrt{q_{\ell-1}}\), and induction gives
\(H\le(2\beta_\partial)^L\). Also, because \(9s\ge9\),

\[
1+4\sum_{k=1}^{L-1}(9s)^{-2k}
\le1+\frac4{(9s)^2-1}\le\frac{21}{20}.
\]

Using \(H\ge1\) to absorb the first term of \(F\), and
\(8\sqrt{21/20}<9\), yields

\[
8H\sqrt F\le H^2(9s)^L
\le36^L\beta_\partial^{3L}
\le\beta_\partial^{5L}.
\]

This proves (19) implies (7) for the explicitly defined envelope.
For the same envelope, its \(-62L\) label cap is smaller and therefore
also sufficient for this dense-fitting component. No compressor,
analytic-source, runtime, or independent-dense comparison claim is
established by this check.

# Additional author checks for the spherical source candidate

2026-10-04. This is a bounded author follow-up check, not an independent
review. It checks the frozen SPHERICAL_SOURCE_DIMENSION_ROUTE.md at
SHA-256 `bba804ec958860eff8eceaeda212a1e6bf391fb82c5b0e0224bfe870d98728a8`.
That candidate is unchanged. The supervisor requested three checks:
preprocessing-only storage of harmonic coefficients, off-grid derivatives
in the geodesic insertion extension, and the elementary harmonic
reconstruction argument. In addition to the candidate's previously read
inputs, STORAGE_QUADRATIC_IMPROVEMENT.md and
DEPTH_CONSTANT_SEPARATION.md were read completely. No experiment,
other-study access, Git operation, or maintained-file edit occurred.

**Outcome:** the harmonic basis introduces no retained evaluator or extra
runtime coefficients. The geodesic first-derivative graph gives the
needed off-grid bounds under the same stopped caps. An explicit positive
polynomial approximate identity can replace Stone--Weierstrass entirely.
These are supplementary author checks; the coordinator's separate
reconstruction remains a different artifact.

## 1. Harmonic coefficients are setup data only

The source theorem constructs, for each hidden layer, a subspace
\(S_\ell\subset\mathbb R^n\) containing the real coefficient vectors
and exact initialized additions. The spherical polynomials only certify
that the actual dense vectors admit approximants in these spaces with
coordinate error \(n^{-1}\). They are not the compressed predictor's
query representation.

The runtime construction in STORAGE_QUADRATIC_IMPROVEMENT.md, Section 2,
takes an empirical orthonormal basis \(U_\ell\) of \(S_\ell\), chooses
at most \(9\dim S_\ell\) coordinate indices, and constructs a fixed
positive metric \(H_\ell\) on those coordinates. Its restricted basis
\(P_\ell=(U_\ell)_{I_\ell}\) satisfies
\(P_\ell^\top H_\ell P_\ell=I\). The initialized reduced mixer is
\[
 B_0^{(\ell)}=P_\ell
 \frac{U_\ell^\top W_0^{(\ell)}U_{\ell-1}}n
 P_{\ell-1}^\top H_{\ell-1}.
 \tag{1}
\]
This formula preserves exactly every initialized forward/transpose image
pair in the source spaces. The source candidate uses identical scalar
linear coefficient operations on each pair, so it supplies precisely
this interface, independently of its choice of polynomial basis.

After forming (1) and the metrics, discard the harmonic basis,
quadrature nodes and weights, degree index sets, analytic radii,
original-width source vectors, \(U_\ell\), \(P_\ell\), and middle
matrices in (1). The runtime's stored moving state is only
\((A_C,B_C^{(2)},\ldots,B_C^{(L)},w_C,c_C)\), along with the fixed
metrics and the data. A query \(v=x/\sqrt d\) is evaluated by
\[
 z_C^{(1)}=A_Cv,\qquad z_C^{(\ell)}=B_C^{(\ell)}h_C^{(\ell-1)},
 \qquad h_C^{(\ell)}=\phi_\ell(z_C^{(\ell)}).
 \tag{2}
\]
If \(F_C\) is the current top training-feature matrix and
\(Q_C=F_C^\top H_LF_C\), its corrected readout is
\[
 \widehat w_C=w_C+F_CQ_C^{-1}
             (y-c_C-F_C^\top H_Lw_C),\qquad
 f_C(x)=\widehat w_C^\top H_Lh_C^{(L)}(x).
 \tag{3}
\]
The autonomous updates use these current features, current readout,
current residual \(c_C\), and metric adjoints
\(H_{\ell-1}^{-1}B_C^{(\ell)\top}H_\ell\). None evaluates a harmonic
polynomial or consults a source table. The model also needs no original
neuron indices after its selected arrays have been initialized.

Thus even an expensive harmonic-basis construction contributes only to
setup work and precision. Its only retained-size consequence is the
dimension of \(S_\ell\), already counted in the candidate. The metric
arrays, learned matrices, inverse/copies and feature/Gram solve caches
remain exactly those in the supplied quadratic inventory. In particular
there is no uncounted fixed array of harmonic basis coefficients with
exponential size.

## 2. Explicit off-grid bounds for geodesic query sources

Use an orthonormal frame \((u,v)\), the tube coordinate \(s\), and
\[
 q=u\cosh s+i v\sinh s,\qquad
 w=-i u\sinh s+v\cosh s.
\]
Here \(w=\partial_z(u\cos z+v\sin z)|_{z=is}\), and the stopped
geodesic response is \(J^{(\ell)}=D_qz^{(\ell)}[w]\). Throughout
the tube, \(\|q\|,\|w\|\le2\). Along a unit-speed local frame path
or the \(s\) direction, write \(p\) for its scalar parameter. The
input derivatives \(q_p,w_p\) have uniformly bounded norms; for the
tube direction they are \(iw\) and \(-iq\). Local orthonormal-frame
paths have this property by the polar-normalized interpolation used in
the candidate.

Write \(\|a\|_{2,n}=\|a\|_2/\sqrt n\). Put
\(Z_p^{(\ell)}=\partial_pz^{(\ell)}\) and
\(J_p^{(\ell)}=\partial_pJ^{(\ell)}\), holding trained parameters
fixed for these query derivatives. Their exact recursions are
\[
 Z_p^{(1)}=Aq_p,\qquad
 Z_p^{(\ell)}=W^{(\ell)}
                    [\phi'_{\ell-1}Z_p^{(\ell-1)}],
\]
\[
 J_p^{(1)}=Aw_p,\qquad
 J_p^{(\ell)}=W^{(\ell)}
 [\phi''_{\ell-1}Z_p^{(\ell-1)}\odot J^{(\ell-1)}
                         +\phi'_{\ell-1}J_p^{(\ell-1)}].
 \tag{4}
\]
Activation derivatives here are evaluated at the current preactivations.
Bounded input derivatives, \(\|A\|_{\rm op}/\sqrt n\le10\), and
bounded gates/mixers give
\(\|Z_p^{(\ell)}\|_{2,n}\le C_{L,\phi}\) by induction. The
stopped cap \(\|J^{(\ell)}\|_\infty\le
\widetilde V_*\sqrt{\ell_n}\) then gives
\[
 \|Z_p^{(\ell)}\odot J^{(\ell)}\|_{2,n}
 \le\|Z_p^{(\ell)}\|_{2,n}\|J^{(\ell)}\|_\infty
 \le C_{d,L,\phi}\sqrt{\ell_n}.
\]
Induction in (4) proves
\(\|J_p^{(\ell)}\|_{2,n}\le C_{d,L,\phi}(1+\sqrt{\ell_n})\).
Consequently the actual Gaussian source
\(\partial_z h^{(\ell)}=\phi'_\ell J^{(\ell)}\) has the same
normalized RMS derivative bound. Its ordinary Euclidean derivative is
therefore at most \(\sqrt n\) times a fixed polynomial in \(\ell_n\).

The residual-free forward-response source has the same property. Its
recurrence is
\[
 R_a^{(1)}=\delta_a^{(1)}v_a^\top q,
\quad R_a^{(\ell)}=\delta_a^{(\ell)}
       \frac{h_a^{(\ell-1)\top}h^{(\ell-1)}}n
          +W^{(\ell)}[\phi'_{\ell-1}R_a^{(\ell-1)}].
 \tag{5}
\]
After \(\partial_p\), the derivative of its normalized feature pairing
is bounded by the query derivative RMS above. Its gate-curvature product
is \(\phi''Z_p\odot R_a\); the stopped coordinate cap for \(R_a\)
and the bounded RMS of \(Z_p\) control it exactly as in (4). Therefore
\(\partial_p(\phi'R_a)\) also has Euclidean norm at most
\(\sqrt n\operatorname{polylog}(n)\), with fixed-parameter constants.

For the time directions, differentiate (4) before holding parameters
fixed: add \(\dot A q\), \(\dot A w\), and \(\dot W\) times the
existing bounded-RMS sources. Their RMS/operator bounds follow from the
actual residual-activity equations. The remaining gate term contains
\(\dot z\odot J\), or \(\dot z\odot R_a\), and is bounded by the
coordinate response cap times the RMS time velocity. The assigned source
proof already controls the time derivatives of the training backward
factors in (5). Thus the two real time directions have the same
\(\sqrt n\operatorname{polylog}(n)\) Euclidean derivative bound.

An omitted hidden-matrix root has bounded Euclidean norm on the inherited
initialization event. The unnormalized first-layer Gaussian rows are
handled separately: at fixed \(d\), their maximum norm is at most a
fixed multiple of \(\sqrt{\ell_n}\) with probability tending to one,
so their direct input-pairing interpolation has only another logarithmic
factor. A query mesh of spacing \(n^{-2}\) therefore
interpolates its Gaussian pairings with error at most
\(C_{d,L,\phi}n^{-3/2}\operatorname{polylog}(n)=o(1)\). The time,
tube, and frame dimensions give the net exponent already counted in the
candidate. These off-grid coefficients only multiply a vanishing error;
the nonvanishing Gaussian multiplier \(16\sqrt{d+3}\) remains explicit
in the response cap and analytic radius.

The enlarged insertion event also needs derivatives of coefficient maps
such as \(D_\Theta(\partial_z h)\). Differentiating the finite graph
(4)--(5) adds only bounded strip derivatives, stopped coordinate factors,
bounded input derivatives, and matrix actions with their original
\(n^{-1/2}\) normalization. Fixed polynomial bounds in \(n\) suffice
for that event; its superpolynomial Gaussian concentration allows a
finer polynomial mesh. No new family of controls depending on two
continuous time variables is introduced: at each frozen query the
controls are still functions on one physical-time contour. Direct
deleted sources remain \(x_i\partial_z h_i\), with no extra reverse
observable source. Their time derivatives have the preceding bounds.

Finally every interpolation path stays within the current stopped query
domain: the frame path remains orthonormal and keeps \(s\) fixed, while
varying \(s\) stays in its current interval. Therefore using the stopped
gate bounds in (4) does not assume analytic continuation outside the
domain being proved. Cavity comparisons are still made on the common
prefix and transferred using the inherited coordinate-small insertion
remainders. This checks the new off-grid requirements without assuming
Gaussian independence of trained full-network vectors.

## 3. Harmonic reconstruction without an external density theorem

The candidate's harmonic identities use finite polynomial algebra,
the polar-coordinate Laplacian, integration by parts, and scalar complex
analytic continuation. No representation-theoretic irreducibility or
external spherical approximation theorem is used. In particular its
one-dimensional space of zonal degree-\(j\) harmonics follows by applying
the Laplacian successively to an invariant homogeneous polynomial;
the Gegenbauer generating function is directly checked against the same
ODE. Kernel invariance follows from changing an orthonormal basis of a
finite-dimensional rotation-invariant space.

The self-adjoint spherical mean also has a concrete frame explanation.
For real angle \(z\), map a frame \((x,u)\) to
\[
 y=x\cos z+u\sin z,\qquad
 w=x\sin z-u\cos z.
\]
This is an orthogonal transformation of its two columns, hence preserves
the uniform orthonormal-frame law. It exchanges the ordered pair
\((x,y)\) with \((y,x)\), because
\(x=y\cos z+w\sin z\). Thus the mean is self-adjoint. One explicit
way to check the frame-law invariance is to take a \(d\)-by-2 matrix
of independent standard Gaussians and normalize its columns jointly by
\(X(X^\top X)^{-1/2}\). Its law is invariant under every orthogonal
mixing of the two columns and every real ambient rotation; conditioned
on its first column, its second is uniform on the unit tangent sphere.
This is the normalized surface-frame law used in the integrals.

Even Stone--Weierstrass can be omitted. For an integer \(N\ge1\), set
\[
 K_N(x,y)=c_N\left(\frac{1+x\cdot y}{2}\right)^N,
 \qquad \int_{S^{d-1}}K_N(x,y)\,d\sigma(y)=1.
 \tag{6}
\]
Rotational invariance makes the positive normalizing number \(c_N\)
independent of \(x\). For fixed \(0<\varepsilon<2\), outside the
Euclidean spherical cap \(\|x-y\|<\varepsilon\), the unnormalized
factor in (6) is at most \((1-\varepsilon^2/4)^N\). Its denominator
is at least the positive measure of the cap of radius
\(\varepsilon/2\), times \((1-\varepsilon^2/16)^N\). Therefore
the total normalized mass outside the larger cap tends to zero,
uniformly in \(x\), by the ratio of these two geometric sequences.

For every continuous \(f\), uniform continuity and a split into these
two regions prove
\(\int K_N(x,y)f(y)\,d\sigma(y)\to f(x)\) uniformly. If every
harmonic coefficient of \(f\) is zero, the elementary homogeneous
harmonic decomposition makes it orthogonal to every polynomial
restriction. The left-hand side then vanishes for every \(N,x\),
because (6) is a polynomial in \(y\). Hence \(f=0\). Applied to
the difference between the function and the absolutely uniformly
convergent harmonic series in the candidate, this proves reconstruction
without any external density theorem. The \(d=1\) two-point case is
already separate, and needs no harmonic completeness argument.

This alternative changes neither the candidate's coefficient decay,
degree cutoff, retained count, nor runtime. The kernels in (6) are solely
a proof device and require no retained numerical arrays.

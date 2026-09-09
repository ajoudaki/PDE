# Exact near-identity population flow: energy-preserving Galerkin route

2026-09-08. This note responds to the accepted activation constraint

\[
\phi_\theta(z)=z+\theta\psi(z),
\]

with a bounded smooth nonlinearity and no overall gain. The earlier large-gain candidate is outside this constraint. Its audit remains a separate mathematical record and is not evidence for this route.

**Status.** The finite-dimensional population approximants below are rigorously global, retain the restricted original raw metric and genuine adjacent adjoints, and satisfy uniform compact-time primal bounds by their true energy identity. A sufficient strong-compactness bridge is stated and proved conditionally. That bridge has not been established for these approximants. Consequently this note does not prove the global canonical strong flow, full-sequence finite-width limits, or global fitting for the accepted near-identity family. No experiment is proposed or run here.

## 1. Setup and the exact analytic difficulty

Fix three RMS-normalized inputs and binary labels, and fix any finite hidden depth \(L\ge2\). Singular input Grams are allowed. Let \(\psi\in C^\infty(\mathbb R)\) be bounded with bounded first and second derivatives. Choose \(\theta>0\) so \(\theta\|\psi'\|_\infty\le1/2\). Then

\[
\tfrac12\le\phi_\theta'\le\tfrac32,
\qquad \|\phi_\theta-\mathrm{id}\|_\infty
\le\theta\|\psi\|_\infty.
\]

Use the canonical Gaussian layer spaces \(H_\ell=L^2(\Omega_\ell,\mu_\ell)\), initialized bounded actions \(A_{\ell,0}:H_{\ell-1}\to H_\ell\), and their actual adjoints. The raw increments lie in

\[
\mathcal X=L^2(\Omega_1;\mathbb R^d)
\oplus\bigoplus_{\ell=2}^L\mathrm{HS}(H_{\ell-1},H_\ell)
\oplus H_L,
\]

with the original first-block factor \(d\). The loss is \(\mathcal E=\frac12\sum_i(f_i-y_i)^2\).

The scalar predictor is continuously Fréchet differentiable in this raw norm, by the bounded-multiplier and weighted scalar Taylor arguments in the existing foundations. Its gradient is continuous and bounded on bounded primal balls. It need not be locally Lipschitz on an ambient \(L^2\) ball. The obstruction is the derivative of a backward gate,

\[
\partial_z[\phi_\theta'(z)q]=\theta\psi''(z)q,
\]

where \(q\) is controlled in \(L^2\), not in \(L^\infty\).

This is a real obstruction to that particular local-Lipschitz argument, not a counterexample to existence of the desired neural flow. For example, on \((0,1)\), take \(C(\omega)=\omega^{-1/4}\in L^2\), a constant \(z_*\) with \(\psi''(z_*)\ne0\), and the scalar loss \(\frac12(\langle C,\phi_\theta(z)\rangle-y)^2\), with nonzero residual at \(z_*\). Perturb \(z_*\) by \(\varepsilon\mathbf1_{\{C>M\}}\). For fixed sufficiently small \(\varepsilon>0\), the ratio of the change in the gate-gradient term to the \(L^2\) state change is bounded below by a positive multiple of

\[
\frac{\|C\mathbf1_{\{C>M\}}\|_2}
{\sqrt{\mu(C>M)}}\ge M.
\]

The additional residual-change contribution, divided by the same state change, tends to zero by Cauchy–Schwarz and the vanishing \(L^2\) tail of \(C\). Thus arbitrarily small fixed \(\theta>0\) does not itself provide the missing ambient Lipschitz bound. This example concerns a related scalar loss and arbitrary states; it does not show that the canonical reached states have such bad behavior.

## 2. What scalar cutoffs do and do not repair

If \(G=\nabla_{\rm raw}\mathcal E\) is the true gradient and \(0\le\chi_R\le1\), then the auxiliary direction

\[
\dot\Theta=-\chi_R(\Theta)G(\Theta)
\]

satisfies \(\dot{\mathcal E}=-\chi_R\|G\|^2\). It is energy decreasing. However, a smooth radial cutoff that is nonzero near a state leaves the unbounded gate derivative present. It bounds speed or support; it does not automatically make this continuous vector field locally Lipschitz. A speed normalization that is a locally invertible radial map on the relevant range has the same limitation.

Conversely, if \(G_R\) is obtained by clipping backward gates internally, then

\[
\frac d{dt}\mathcal E(\Theta)=-\chi_R\langle G,G_R\rangle.
\]

A nonnegative common scalar cannot turn a negative alignment into positive alignment. Thus multiplying an already clipped backward direction by a radial/speed factor does not supply the missing true energy identity. These are failures of the proposed repairs, not impossibility statements about other energy-preserving regularizations.

## 3. A concrete energy-preserving approximation

Choose increasing finite measurable partitions \(\mathcal F_{\ell,N}\) generating each canonical layer sigma-field. Let \(P_{\ell,N}\) be conditional expectation onto that partition and \(H_{\ell,N}=\operatorname{ran}P_{\ell,N}\). Each space is finite dimensional, contains constants, and is closed under coordinatewise scalar functions. The projections are orthogonal contractions and converge strongly to the identity on \(H_\ell\).

The projected initialized action is

\[
A_{\ell,0,N}=P_{\ell,N}A_{\ell,0}P_{\ell-1,N},
\qquad
A_{\ell,0,N}^*=P_{\ell-1,N}A_{\ell,0}^*P_{\ell,N}.
\]

Its norm is at most the canonical initialized norm. Its reverse is its genuine adjoint. Take \(w_{0,N}=P_{1,N}w_0\), \(C_{0,N}=0\), and learned matrices \(U_{\ell,N}:H_{\ell-1,N}\to H_{\ell,N}\). Use the network with current action \(A_{\ell,0,N}+U_{\ell,N}\), the exact activation \(\phi_\theta\), and the exact raw metric restricted to these finite spaces. Train by its **true** raw gradient.

The finite partition is an auxiliary population approximation, not a replacement of the actual finite-width Gaussian training initialization. No finite-width identification is asserted at this stage.

Because all partition atoms form a finite coordinate system, the resulting loss is a smooth finite-dimensional function. Its gradient flow is locally well posed and satisfies exactly

\[
\frac d{dt}\mathcal E_N
=-d\|\dot w_N\|_2^2
-\sum_{\ell=2}^L\|\dot U_{\ell,N}\|_{\rm HS}^2
-\|\dot C_N\|_2^2.
\]

Since \(C_{0,N}=0\), \(\mathcal E_N(0)=3/2\). Hence, for every finite \(T\),

\[
\int_0^T\|\dot\Theta_N(t)\|_{\rm raw}^2dt\le\tfrac32,
\qquad
\sup_{t\le T}\|\Theta_N(t)-\Theta_N(0)\|_{\rm raw}
\le\sqrt{3T/2}.
\tag{1}
\]

No finite-dimensional solution can escape in finite time. At any finite maximal endpoint, the same length estimate on \([s,t]\) makes the state Cauchy as \(s,t\) approach the endpoint; smooth local existence then continues it. Every projected true flow is therefore global.

The bounds are independent of \(N\). In particular,

\[
\|A_{\ell,0,N}+U_{\ell,N}(t)\|_{\rm op}
\le\|A_{\ell,0}\|_{\rm op}+\sqrt{3T/2}.
\]

Forward/backward induction using bounded \(\phi_\theta'\), linear growth of \(\phi_\theta\), and \(\|r_N\|_2\le\sqrt3\) gives a common compact-time bound on all forward and backward \(L^2\) norms and on the raw direction norm. Thus the increment paths are also equi-Lipschitz in raw norm on each \([0,T]\), with a constant depending on fixed \(L,T,\theta,\psi\).

## 4. The precise unclosed strong-compactness bridge

A sufficient additional assertion is: for each finite \(T\), for the finite list of first-weight coordinates, readout, forward features and true backward fields generated by the projected flows,

\[
\lim_{m\to\infty}\sup_N\sup_{t\le T}
\|(I-P_{\ell,m})X_{\ell,N}(t)\|_2=0.
\tag{SC}
\]

It is enough to prove (SC) for sufficiently large \(N\); any finitely many earlier paths have compact images and can be added separately. This is control of unresolved coordinates of the canonical probability space, not merely a bound on the scalar amplitude tail \(|X|>R\).

Here is why (SC) would close existence. For each rank-one update,

\[
\|b\otimes h-(P_m b)\otimes(P_m h)\|_{\rm HS}
\le\|(I-P_m)b\|_2\|h\|_2
+\|b\|_2\|(I-P_m)h\|_2.
\]

Integrating the finite sum of updates, using bounded residuals and (SC), gives uniform finite-dimensional projection tails for every learned HS increment. The corresponding first-weight and readout tails are included directly. The uniform time modulus and finite-dimensional projection bounds give subsequential compactness in \(C([0,T];\mathcal X)\): on each fixed finite projection choose a uniformly convergent subsequence, diagonalize over projections, and use the uniform tails to make this subsequence Cauchy in the full raw norm.

Along such a subsequence, initial projections converge strongly and learned increments converge uniformly in HS. Although \(P_NA_0P_N\) need not converge in operator norm, it converges strongly, with uniform operator bound. Strong convergence is uniform on every compact input set by a finite-net argument. Forward induction therefore passes all preactivations and features to their canonical counterparts. The same argument with the genuine adjoints and bounded-multiplier continuity passes true backward fields. Rank-one gradient blocks converge uniformly in raw norm, so the integral equations pass to

\[
\dot\Theta=-\nabla_{\rm raw}\mathcal E(\Theta)
\]

with a continuous raw derivative. A diagonal subsequence over integer horizons gives a global canonical strong solution. The exact energy identity and the same raw metric survive the limit.

This conditional proof establishes existence from (SC). It does **not** by itself establish uniqueness, full-sequence convergence, finite-width GF/GD identification, or global fitting.

If one additionally proves compact-time subGaussian tails for the limiting true incoming fields, the existing reference-only gate comparison can give uniqueness without tails of a competitor. Optimizing

\[
\|F(\Theta)-F(\bar\Theta)\|
\le C(1+R)\|\Theta-\bar\Theta\|+Ce^{-cR^2}
\]

in \(R\) yields an Osgood modulus of order
\(s\sqrt{\log(e/s)}\). Its reciprocal has divergent integral at zero. This identifies a separate sufficient uniqueness bridge; it is not supplied merely by (1).

## 5. Why energy and marginal tails do not yet prove (SC)

The energy estimate controls norms and time variation, but bounded sets in the canonical infinite-dimensional Hilbert spaces are not strongly precompact. The constant paths \(X_N(t)=e_N\) for an orthonormal sequence have bounded norms and zero speeds while no strong subsequence exists. These paths do not have the shared neural initialization and are not gradient approximants above. They only refute an inference based on norm and speed bounds alone.

Even uniform scalar subGaussian tails do not imply (SC): distinct independent standard Gaussian coordinates have identical Gaussian marginal laws but pairwise \(L^2\) distance \(\sqrt2\). Bounded Rademacher coordinates give the same issue with compactly supported marginal laws. Neither example is a counterexample to the neural approximants. A source proof must control their joint canonical coordinate complexity or establish a direct Cauchy estimate; marginal moment bounds alone are insufficient for this Galerkin route.

Nor does the operator bound \(\|A_0\|_{2\to2}\le2\) imply invariance of a chosen weighted Gaussian Banach space or a higher-moment operator bound. Such invariance must be proved for the actual canonical actions. A generic Gaussian Sobolev bound without coordinate weights also need not provide compactness on a countably infinite Gaussian space, because the first chaos has infinite multiplicity.

The highest-leverage next theoretical step for this route is therefore a direct (SC) estimate, or a replacement common-space Cauchy estimate, for the energy-preserving projected flows. An argument must use their actual Gaussian initialization, source correlations, and true-gradient structure. No failure of (SC) for these flows has been established.

## 6. An independent accepted small-offset activation candidate

The family

\[
\phi_\theta(z)=z+\theta\bigl(b+\varepsilon\arctan z\bigr),
\qquad b>0,\quad\varepsilon>0,
\tag{2}
\]

has linear coefficient exactly one. Its departure from identity satisfies

\[
\|\phi_\theta-\mathrm{id}\|_\infty
\le\theta(b+\varepsilon\pi/2),
\qquad
\|\phi_\theta'-1\|_\infty\le\theta\varepsilon.
\]

One may choose the nonlinear amplitude \(\varepsilon\) much smaller than the offset coefficient \(b\), while retaining a genuinely nonlinear activation. This uses only the user-permitted small offset and near-identity perturbation; it does not introduce an overall gain.

For its affine reference \(z\mapsto z+\beta\), \(\beta=\theta b\ne0\), the first initialized feature Gram is

\[
\Gamma+\beta^2\mathbf1\mathbf1^T.
\]

It is positive definite for three distinct unit inputs. Indeed a vector in its kernel must satisfy both \(\sum_i v_i u_i=0\) and \(\sum_i v_i=0\), making the three points affinely dependent. Three distinct points on a Euclidean sphere cannot lie on an affine line, since a line meets a sphere in at most two points. Pairwise absolute separation ensures distinctness. At initialized higher affine layers the Gram is \(\Gamma+\ell\beta^2\mathbf1\mathbf1^T\), by the centered Gaussian action rule.

This repairs the rank-two affine initialization obstruction and suggests a comparison with small-offset affine dynamics. It is only an initialization statement. A global residual-clock or fitting theorem for the affine reference at gain one has not been proved in this note, so no nonlinear global fitting conclusion follows from (2) here.

**Research state:** exact global energy-preserving approximants established; strong canonical population existence remains conditional on (SC) or an equivalent direct source/Cauchy estimate. The small-offset family is an independent admissible candidate, not a solved theorem.

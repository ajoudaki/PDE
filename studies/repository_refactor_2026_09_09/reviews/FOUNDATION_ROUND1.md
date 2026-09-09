# Isolated adversarial mathematical review

## Verdict

**CLEAN.** I found no incorrect identity, missing hypothesis invalidating a stated result, or unsupported finite-to-population implication in these three documents. No mathematical correction is required. This verdict concerns precisely their stated results; it does not certify a general joint limit, a population network construction, or convergence of gradient descent.

## Scope and exact inputs

Reviewed on 2026-09-09. I read all 503 numbered lines, including every statement, proof, displayed equation, and qualification, in these three files in `/tmp/pde-established-foundation-review.kDRjhe`:

| File | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `NOTATION.md` | 98 | 5110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `finite_dynamics.md` | 214 | 8355 | `486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c` |
| `gaussian_calculus.md` | 191 | 8056 | `f7b02a49c4cb9da1ef47069bb4e0c46da5993a8f1428856638bcb7316f6dcd4a` |

No other files, project state, histories, prior reviews, skill instructions, agents, experiments, Git, or internet sources were consulted. The inputs were not modified. The review uses independent mathematical derivations, not numerical tests. References below are to the numbered lines of these exact inputs.

## Finite dynamics and the global energy argument

### Derivatives, mobilities, kernel, and dissipation

All formulas (1)–(5) in `finite_dynamics.md` are correct.

The readout normalization gives

\[
\partial_{z_a^{(\ell)}}f_{n,a}=\delta_a^{(\ell)}/n.
\]

For a middle block, applying a variation to the forward map therefore gives the Frobenius gradient \(\delta_a^{(\ell)}(h_a^{(\ell-1)})^T/n\). The first block instead has the input \(x_a/\sqrt d\), and the readout derivative is \(h_a^{(L)}/n\). These prove (1), with no residual in any backward coordinate.

Since \(\nabla\mathcal L_n=(2/m)\sum_a r_{n,a}\nabla f_{n,a}\), multiplying these derivatives by the stated block mobilities gives exactly (2). In particular, the factors of \(n\) cancel for the first and readout updates and remain as \(1/n\) for a middle update. Simultaneous evaluation of the right-hand sides is the correct raw GD convention.

The mobility factors in the three kernel types are respectively

\[
\frac{n\kappa_1}{n^2d},\qquad
\frac{\kappa_\ell}{n^2},\qquad
\frac{n\kappa_{L+1}}{n^2}.
\]

Factoring the corresponding outer-product pairings yields exactly (3). The first block uses the actual input Gram \(x_a^Tx_b/d\); no orthogonality or invertibility is needed. Each block is a Gram matrix in the positive learning metric and hence is positive semidefinite, even when individual entries are negative.

The chain rule then gives \(\dot f_n=-(2/m)K_nr_n\). Consequently,

\[
\dot{\mathcal L}_n
=-\frac4{m^2}r_n^TK_nr_n
=-\nabla\mathcal L_n^TD\nabla\mathcal L_n
=-\|D^{-1/2}\dot\theta\|_2^2.
\]

This checks the sign, both factors of \(m\), and the energy weights in (4)–(5). The middle blocks in (5) correctly have no additional normalization by \(n\).

### Global existence for arbitrary real \(C^2\) activations

The argument at lines 113–135 is complete and does not require bounded activations, bounded derivatives, coercivity of the loss, or a width-uniform equivalence of norms.

At fixed finite width, the loss is a finite-valued \(C^2\) function on the entire finite-dimensional parameter space. Its metric gradient field is \(C^1\), hence locally Lipschitz, so the stated local contraction argument applies. Nonnegativity of squared loss bounds the integrated squared velocity in the fixed positive metric by the finite initial loss.

For \(0\le s<t\) before a possible maximal endpoint, integrating the velocity and applying Cauchy–Schwarz proves (6). If that endpoint were finite, the upper bound \(\sqrt{(t-s)\mathcal L_n(0)}\) would force the entire parameter path to be Cauchy there. Positivity of every mobility makes its limit a finite Euclidean state. Local existence at this state extends the path; continuity of the field also matches the derivative at the joining time. Thus finite-time escape is impossible, even for arbitrarily fast-growing \(C^2\) activations.

Taking one block of the same weighted displacement estimate gives exactly (7). For the subsequent modulus assertion, the corresponding displacement is \(W(t)-W(s)\), and its bound has \(t-s\) in place of \(T\). The operator bound for a middle increment follows from \(\|A\|_{\mathrm{op}}\le\|A\|_F\).

### Width-independent bounds and Gaussian initialization

The stronger conclusions at lines 157–189 explicitly assume bounded activation derivatives, bounded initial normalized first/readout norms and middle operator norms, bounded initial loss, fixed data, and fixed depth. The proof does not silently infer these assumptions from general \(C^2\) regularity.

The two displayed forward inequalities follow from the Frobenius bound for the first matrix and the operator bound for a middle matrix. The estimate \(|\phi(z)|\le|\phi(0)|+\sup|\phi'|\,|z|\) closes the RMS induction, including nonzero activation offsets. The two backward inequalities use the operator norm of the same transposed matrix and the bound on the diagonal derivative multiplier. Cauchy–Schwarz then bounds every kernel entry. None of these operations requires coordinatewise bounds or a bound on \(\phi''\).

The initialization verification at lines 191–209 has the correct normalization. The first-block squared Frobenius norm divided by \(n\) converges in probability to fixed \(d\). For the stored readout,

\[
\mathbb E\!\left[\frac{\|W^{(L+1)}(0)\|_2^2}{n}\right]=n^{-2},
\]

so its squared RMS tends to zero in probability. A maximal \(1/4\)-separated subset of the unit sphere is a \(1/4\)-net; disjoint radius-\(1/8\) balls lie in the radius-\(9/8\) ball, giving the claimed \(9^n\) bound. Approximating each of two unit vectors incurs total error at most \(\|W\|_{\mathrm{op}}/2\). Thus \(\|W\|_{\mathrm{op}}>M\) requires a net bilinear form of absolute value greater than \(M/2\). Each such form has variance \(1/n\), yielding exactly

\[
\mathbb P(\|W\|_{\mathrm{op}}>M)
\le 2\,9^{2n}e^{-nM^2/8}.
\]

For example, any fixed \(M\) with \(M^2>16\log9\) makes this tend to zero. Fixed depth permits the final union bound. The initial forward and readout estimates also supply the claimed initial loss bound for the fixed labels. This is a high-probability event as width grows, not an assertion of deterministic bounds for every Gaussian realization.

## Gaussian reuse and conditioning

### One forward call, transpose response, and the empirical law

All formulas (1)–(5) in `gaussian_calculus.md` are correct under the stated growth and differentiability assumptions.

Each row of \(W\) has covariance \(I/n\). Its component determined by its row sum is \(y_i\mathbf1^T/n\), and its remaining covariance is \(P/n\). Gaussian orthogonality gives the first conditional representation. Multiplication by the fixed conditional vector \(g(y)\) gives mean \(a_n\mathbf1\) and covariance

\[
P\left(\frac1n\sum_i g(y_i)^2\right)IP=\sigma_n^2P,
\]

which proves the second representation and (2). In particular, the empirical mean of \(q\) is exactly \(a_n\), since \(\mathbf1^TP=0\); it is not the deterministic limiting response at finite width.

The rows make the \(y_i\) independent standard Gaussians. Polynomial growth supplies all the integrability needed for the laws of large numbers in (3). Taking nonnegative square roots gives \(\sigma_n\to\sigma\), including when \(\sigma=0\). On the displayed coupling, writing \(P\gamma=\gamma-\bar\gamma\mathbf1\) proves (4) exactly. The Gaussian RMS tends to one and \(\bar\gamma\) tends to zero, so the bound vanishes in probability.

Matching coordinates couples the two empirical measures at squared transportation cost at most the squared RMS error. The reference Gaussian empirical law converges in quadratic Wasserstein distance: a countable convergence-determining family of bounded Lipschitz tests gives weak convergence, and the second empirical moment converges as well. The truncation argument stated in the document is sufficient: weak convergence and second-moment convergence give vanishing limiting squared tails; on a bounded interval quantile coupling gives convergence of the squared cost. The triangle inequality therefore proves quadratic-Wasserstein convergence in probability of the empirical law of \(q_i\) to \(N(a,\sigma^2)\), with the degenerate Gaussian included.

No independence of the actual \(q_i\) is used or implied. No empirical joint law pairing row and column coordinates is asserted. Under the additional \(C^1\) and polynomial-growth derivative assumptions, integration by parts has a vanishing boundary term and proves \(a=\mathbb E[g'(G)]\) with the stated sign and scale.

### Conditioning after both directions and adaptive queries

Formulas (6)–(7) and their supporting linear algebra are correct. Write \(Q_V=I-P_V\) and \(Q_U=I-P_U\). Compatibility gives

\[
MV=Y,\qquad
M^TU=V(V^TV)^{-1}Y^TU+Q_VR=P_VR+Q_VR=R.
\]

The space of homogeneous solutions is precisely \(\{A:A=Q_UAQ_V\}\). The first term of \(M\) has its right support in \(\operatorname{span}(V)\), and the second has its left support in \(\operatorname{span}(U)\); both are Frobenius-orthogonal to that homogeneous space. Hence \(M\) is its affine constraint set's minimum-norm point. Vectorizing the centered matrix gives an isotropic Gaussian of covariance \(I/n\), so orthogonal conditioning leaves exactly \(Q_U\widetilde WQ_V\). This also covers full spans and empty query lists, with the usual zero-dimensional matrix convention.

The adaptive extension at lines 127–135 supplies the essential information restriction: roots are independent of \(W\), and each query is chosen measurably from recorded roots and earlier answers before its own answer is observed. Conditional on that past, the next query is fixed. Its answer imposes a linear constraint inside the remaining affine Gaussian space. Induction therefore establishes the asserted conditional law despite adaptive directions. The proof does not improperly treat random adaptive directions as independent deterministic inputs. Its express exclusion of unrecorded observations and anticipation is necessary and sufficient for the stated query setting.

For a new query under this same restriction, the conditional mean is

\[
Mv=Y(V^TV)^{-1}V^Tv+U(U^TU)^{-1}R^TQ_Vv,
\]

and the conditional covariance of the remaining answer is

\[
\frac{\|Q_Vv\|_2^2}{n}Q_U.
\]

These verify every term and the noise scale in (7). Exchanging domain and codomain gives the transpose formula using the same constrained matrix. Exact dependent columns can be removed because their answers are the same known linear combinations. This operation supplies no control of nearly dependent directions as width changes; the document explicitly preserves that distinction.

## Finite-order calculus

All three identities in (8), the constant-metric coordinate change, and the chain-rule statement are correct with the specified \(C^3\) regularity.

Applying the variable vector field \(g=\nabla F\) to \(F\) gives \(\|g\|^2\). Differentiating this gives \(2\langle g,Hg\rangle\). Differentiating its two gradient factors gives \(4\|Hg\|^2\), and differentiating the Hessian gives \(2T[g,g,g]\). In particular, the computation correctly differentiates the direction itself; it does not mistake repeated differentiation along a gradient field for repeated differentiation along a fixed vector.

For \(\widehat F(q)=F(D^{1/2}q)\), one has \(\nabla_q\widehat F=D^{1/2}\nabla_\theta F\). Thus either sign of Euclidean gradient flow in \(q\) maps to the same sign of metric gradient flow in \(\theta\). The positive-gradient chain-rule statement at lines 186–188 is consistent with the earlier descent convention, since the sign of the flow is explicitly specified locally. Squaring the scalar prediction introduces its residual factor; physical differentiation must differentiate that factor as stated. There is no claim of an infinite Taylor expansion, or an exchange of time differentiation and width limits.

## Shared notation, populations, and dependency boundary

The finite shapes, normalization by \(\sqrt d\), readout normalization by \(n\), backward recursion, residual convention, loss normalization, and block mobilities agree across the documents. The one-forward-call example fixes a middle Gaussian matrix and keeps its row and column populations distinct. The later scalar and vector auxiliary variables are locally typed; they do not alter the network definitions.

The population rank-one convention agrees with the finite action: \((uv^T/n)g=u(v^Tg/n)\), so the expectation contracts the input population only. Using an adjoint for the reverse action is consistent with both finite transpose-conditioning formulas. The observation that a bounded Gaussian action need not be Hilbert–Schmidt is mathematically possible: for independent standard Gaussians \(G_j\), the map \((c_j)\mapsto\sum_jc_jG_j\) from \(\ell^2\) into \(L^2\) is an isometry, while the sum of its squared basis-image norms is infinite. That notation remark does not construct a population network or identify a finite-width limit.

For one sample with label one, \(\dot\theta=-2rD\nabla f\) gives the stated feature-time factor \(ds/dt=-2r=2(1-f)\) on intervals where it is positive. The two arctangent primitives have derivatives \(1+z^2\) and \(10(1+z^2)\), respectively, which are exactly reciprocal to the corresponding activation derivatives. A nonlinear coordinate change preserves the continuous chain rule; in general it does not commute with a raw Euler/GD step. The clock and discretization distinctions are consistent.

The only asymptotic results actually established here are the explicit initialization estimates and the single-call Gaussian empirical-law result. Neither is promoted to a trained population trajectory, a uniform bound on population multiplication operators, a growing-depth theorem, a growing-time theorem, or a theorem for a width-dependent number of adaptive queries. Standard finite-dimensional ODE, Gaussian, law-of-large-numbers, and Wasserstein facts are invoked with their relevant hypotheses and/or supporting arguments. No result depends on an unseen project document or an unproved external population construction.

## Required corrections

None.

## Optional clarity suggestions

These are presentation improvements, not conditions on the verdict.

1. In `gaussian_calculus.md`, lines 143–151, repeat that the new query is measurable with respect to the recorded roots and past answers, and say explicitly that the displayed Gaussian noise is fresh conditional on that information. The preceding adaptive-query paragraph already supplies this restriction.
2. At lines 99–106 of that file, explicitly state that an empty query list has zero projector and contributes a zero term to \(M\). This makes the standard zero-dimensional matrix convention easier to read.
3. At lines 188–189, spell out the scalar squared-loss example as \(\mathcal L=(F-y)^2\), with velocity \(-2(F-y)D\nabla F\). For comparison, the main multi-sample convention has velocity \(-(2/m)\sum_a r_aD\nabla f_a\), as already proved in `finite_dynamics.md`. This would help prevent readers from trying to use a single residual clock for an arbitrary multi-sample trajectory.
4. In `NOTATION.md`, lines 65–66, write the rank-one action with its types, for example \(U\in L^2(\Omega_\ell)\), \(V,g\in L^2(\Omega_{\ell-1})\), and \((U\otimes V)g=U\mathbb E_{\ell-1}[Vg]\). This makes the existing population-contraction rule immediately visible in the example.

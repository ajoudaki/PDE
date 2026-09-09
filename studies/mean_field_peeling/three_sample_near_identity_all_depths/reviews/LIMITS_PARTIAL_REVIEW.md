# LIMITS review: accepted near-identity partial results

Date: 2026-09-08. Verdict: **PASS for the initialization theorem and the conditional necessary fitting-distance/time estimates only.** The complete global canonical near-identity population/GF/raw-GD target remains unproved in these artifacts. No counterexample to its qualitative positive-theta conclusion is established.

## Reviewed file identity

The final local SHA-256 values read for this review are:

| File | SHA-256 |
|---|---|
| INITIALIZATION.md | `f53b4893ae4cacc2180ab1149c2c00a1b8f8b0b941d3319df5a3c0009f531163` |
| NECESSARY_FITTING_SCALE.md | `98705d5550bb977f26712e273b47592340ba2899cf952025889b386349af1fbd` |
| CONTRACT.md | `55c3075fa8f699cc7f44542a814393dbcbc3cb6645b1c822b29b793cde6ee6ce` |

I read the complete two mathematical files and checked their inequalities directly. The fixed-radius time addendum in NECESSARY_FITTING_SCALE was developed by this reviewer and appended at the coordinator's request; the source reviewer independently checked that addition at the final hash and returned PASS. This provenance distinction does not affect the independent checks of the pre-existing initialization and fitting-distance arguments. No experiment was run.

## 1. Scope and exact model

The activation is exactly

\[
\phi_\theta(z)=(1-\theta)z+\theta\arctan z,
\qquad 0<\theta\le\tfrac12.
\]

There is no overall gain or altered metric. The initialized forward recursion uses the full covariance Gram of the actual Gaussian inputs to each independent adjacent action. The initialization result includes singular input Grams and every finite depth. It concerns initialized scalar laws, not trained laws assumed to remain Gaussian.

The necessary fitting estimates use the canonical population readout \(C_0=0\), initialized action norms at most two, and Hilbert–Schmidt learned increments. These are the canonical population counterparts of the original raw initialization and metric. The estimates do not reset the actual finite Gaussian readout, and they make no finite-width conclusion that would require doing so.

## 2. Initialized variance bounds

The ratio representation

\[
\arctan z/z=\int_0^1(1+t^2z^2)^{-1}\,dt
\]

and two applications of convexity give
\(\phi_\theta(z)/z\ge(1+\theta z^2/3)^{-1}\). Squaring is legitimate because both ratios are nonnegative. Under the probability measure with density \(G^2\), the expectation of \(G^2\) is three. Weighted Jensen then yields

\[
q_{k+1}\ge q_k/(1+\theta q_k)^2.
\]

Since \(q_k\le1\) and \(\theta\le1/2\), the reciprocal increment is at most \(2\theta+\theta^2q_k\le(5/2)\theta\). This proves the claimed lower variance bound without a hidden small-variance hypothesis.

For the upper bound, the displayed \(h(z)\) satisfies
\(h(z)\ge z^2/[3(1+z^2)]\) and
\(1-(1-\theta h)^2\ge\theta h\). The identity

\[
E\frac{G^4}{1+G^2}=E\frac1{1+G^2}\ge\tfrac12
\]

is correct. Thus \(q_k-q_{k+1}\ge\theta q_k^2/6\), and the reciprocal increment is at least \(\theta/6\). Both sides of equation (1) follow for every integer \(k\ge0\).

## 3. Hermite derivative estimate and absolute nonaffinity

Oddness removes the constant and every even Hermite coefficient. The first coefficient is \(\sqrt q\,E\phi_\theta'(\sqrt qG)\), so the squared affine-regression residual is exactly the sum of squared coefficients in odd degrees at least three.

Three Gaussian integrations by parts give the coefficient multiplier
\(\sqrt{m(m-1)(m-2)}\). The function has at most linear growth, and the derivatives needed at the boundaries are bounded. The Gaussian boundary terms therefore vanish. Applying Bessel to the third derivative and using \(m(m-1)(m-2)\ge6\) gives

\[
\mathcal R_\theta(q)\le\tfrac23\theta^2q^3.
\]

The bound \(|\arctan'''|\le2\) used here is valid. The cubic coefficient is

\[
-\frac{2\theta q^{3/2}}{\sqrt6}
E\frac{G^2}{(1+qG^2)^2}.
\]

Weighted Jensen bounds the expectation below by \((1+3q)^{-2}\). Squaring gives the stated lower bound, and \((1+3q)^4\le256\) for \(q\le1\) gives the constant \(1/384\). Thus the initialized regression error has the asserted \(q^3\) scale and, at fixed positive theta, depth order \(\ell^{-3}\).

This establishes the claimed limitation: a positive absolute nonaffinity constant independent of depth is impossible for this activation even at initialization. It does not rule out a time-uniform constant depending on each fixed depth.

## 4. Normalized spectral monotonicity and the first cubic floor

The Gaussian generating-function identity gives the Hermite cross-covariance formula including correlations \(\pm1\). Its passage to the infinite expansion is justified by Gaussian \(L^2\) convergence, Cauchy–Schwarz, and absolute entrywise convergence. The normalized output Gram is consequently a convex combination of \(R^{\circ m}\) for odd integers \(m\ge1\).

For each such \(m\), \(S=R^{\circ(m-1)}\) is a positive semidefinite correlation matrix; at \(m=1\), it is the all-ones matrix. Applying the tensor-Gram proof of the Schur product theorem to \(R-\lambda I\) and \(\Lambda I-R\), respectively, gives

\[
\lambda I\preceq R\circ S\preceq\Lambda I,
\quad\lambda=\lambda_{\min}(R),\quad
\Lambda=\lambda_{\max}(R).
\]

The identity \(I\circ S=I\) is essential and holds because \(S\) has unit diagonal. Convex combination and matrix-norm convergence prove both normalized spectral-extremum inequalities. This works for singular \(R\); it neither divides by its smallest eigenvalue nor asserts the different Loewner inequality \(R_{\rm new}\succeq R\).

The tensor test vectors used for the input cubic lift are unit, annihilate the two unwanted sample cubes, and pair with the desired cube by at least \(\delta(2-\delta)\). Summing the three Cauchy–Schwarz inequalities gives the stated cubic Gram lower bound. The integral estimate of the arctangent cubic coefficient at standard variance gives exactly \(\eta_0=1/(108\pi e)\). Its projection is orthogonal across all three sample coordinates, including singular input covariance.

Normalized spectral monotonicity then propagates this first-layer floor with factor \(q_L/q_1\), and \(q_1\le1\) gives equation (2). No cumulative exponential factor is necessary. Together with \(\lambda_{\min}(Q_L)\le q_L\), the variance bounds establish the stated order \(1/L\) at fixed theta and delta, uniformly over the admissible triples.

## 5. Necessary fitting distance at general fixed depth

The equilateral planar triple has \(\sum_i u_i=0\), pairwise correlation \(-1/2\), and is admissible for every \(0<\delta\le1/2\). At every raw state, not only along a solution, the first preactivation sum is zero. Therefore

\[
S_1=\theta T_1,
\qquad S_\ell=(1-\theta)A_\ell S_{\ell-1}+\theta T_\ell
\]

are exact identities in the appropriate layer spaces. The boundedness of arctangent gives \(\|T_\ell\|_2\le3\pi/2\), and expansion yields the displayed product sum with the correct empty product.

Loss at most \(3/8\) implies \(\sum_i f_i\ge3/2\), by Cauchy–Schwarz on the three residuals. Pairing the readout with \(S_L\) therefore gives equation (2). Since the readout starts at zero and each initialized action has norm at most two, joint raw displacement \(R\) gives \(\|C\|_2\le R\) and \(\|A_j\|_{\rm op}\le2+R\). These facts establish all inequalities in (3), including the final positive-part lower bound. The first-layer increment is included in \(R\); omitting it from an upper bound on the remaining blocks only weakens that bound.

For the asymptotic constant there are exactly \(L\) factors: the readout norm and the \(L-1\) adjacent learned matrix norms. Their squared sum is at most \(R^2\). Arithmetic–geometric mean gives

\[
c\prod_{j=2}^L d_j\le(R^2/L)^{L/2}.
\]

Only the earliest nonlinear source term has degree \(L\) in these variables; its coefficient is at most one. Every remaining expanded term has degree at most \(L-1\), with coefficients bounded in terms of fixed \(L\). Thus, along any subsequence on which \(\theta^{1/L}R\) stays bounded, multiplying by theta makes all lower-degree terms vanish. The stated result follows:

\[
\liminf_{\theta\downarrow0}\theta^{1/L}R
\ge\sqrt L\,\pi^{-1/L}.
\]

If there is no such bounded subsequence the inequality is automatic. This is a necessary bound for successful states, with no presupposed trained distribution and no claim of sharpness.

## 6. Conditional time bounds and the fixed-radius addition

For a true strong raw GF, the exact scalar gradient chain rule gives
\(\int_0^T\|\dot\Theta\|_{\rm raw}^2dt\le3/2\). Cauchy–Schwarz therefore gives \(R^2\le(3/2)T\). This yields the stated finite bound and the leading constant

\[
\liminf\theta^{2/L}T\ge(2L/3)\pi^{-2/L}.
\]

The additional fixed-radius argument is valid and stronger in theta order when \(L>2\). With \(B_L=(3^L-1)/2\) and \(\theta<1/(\pi B_L)\), a successful state cannot have \(R\le1\). Every successful continuous strong trajectory consequently has a first time \(t_1\le T\) at distance one. At that time the readout norm is at most one and all current adjacent norms are at most three, so

\[
\mathcal E(0)-\mathcal E(t_1)
=\sum_i f_i(t_1)-\tfrac12\sum_i f_i(t_1)^2
\le\tfrac{3\pi\theta}{2}B_L.
\]

The first-exit chord and energy identity give
\(1\le t_1[\mathcal E(0)-\mathcal E(t_1)]\). Hence

\[
T\ge\frac4{3\pi(3^L-1)\theta}.
\]

This argument does not require monotonic raw displacement, sample symmetry, a uniqueness theorem, or a global solution constructed beforehand. It applies to any true strong trajectory that reaches the target loss. For fixed \(L>2\), its direct consequence is \(\liminf\theta^{2/L}T=+\infty\), while \(\liminf\theta T\) has the displayed positive lower bound at every fixed depth.

These estimates rule out a positive loss-decay rate and finite prefactor both independent of theta for all theta below a cutoff in the admissible equilateral class. They leave possible theta-dependent rates and theorems selecting one fixed positive theta. Neither necessary distance nor necessary time establishes that fitting happens.

## Disposition

No blocking gap was found in the reviewed partial results. The initialization theorem and conditional obstructions are supported at the stated hashes. They do not supply trained Gram control, global source continuation, strong cap removal, nonsymmetric global uniqueness, or the compact-time full-sequence finite GF/raw-GD observation theorem. Those remain separate unresolved obligations for the accepted global target.

**Final verdict: PASS for these partial results only; the full near-identity global target remains unproved.**

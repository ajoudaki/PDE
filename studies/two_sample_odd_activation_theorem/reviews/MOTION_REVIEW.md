# Independent motion and complete-theorem audit

Date: 2026-09-07.

**Verdict: PASS.** I found no substantive mathematical gap in the frozen candidate for the contract's two-input class. This verdict includes the construction and limit bridges on which the initial-motion statements depend. It is not a claim about endpoint data, a three-input extension, or an infinite-time uniform width limit.

## Scope and independence

I read `CONTRACT.md` and all four candidate proof files in full, used the `solve-math-rigorously` skill, and independently recalculated the candidate SHA-256 hashes before and after the mathematical audit. Before finalizing, I inspected the revised scalar-reduction paragraphs in `PROOF.md` and `AFFINE_CORE.md` and verified the refreshed manifest; this verdict applies to the final hashes below. I did not read sibling or historical review reports, task status files, or their conversations. Source-document status prose was not used as a mathematical premise. I ran no numerical experiment, changed no proof, spawned no agent, and made no commit.

The target audited is

\[
\forall\delta\in(0,1]\;\exists e_\delta>0\;
\forall a\in[1/2,1]\;\forall e\in(0,e_\delta]\;
\forall (x_1,x_2,y_1,y_2)\text{ satisfying the contract}.
\]

In particular, the inputs obey \(\|x_i\|^2=d\), \(|\rho|\le1-\delta\), and both labels can independently be either sign. The original Gaussian initialization, raw metric, all three common hidden activations, and simultaneous raw GD step \(n^{-2}\) are retained. Each width-limit assertion concerns a fixed dataset and finite physical horizon.

## Verified identities of the inspected candidate

| File | SHA-256 | Result |
| --- | --- | --- |
| `PROOF.md` | `a4d6ed0ee99a1e111b5eba068f2219cf561a2281b1828b26227aca7a0a54a050` | Match |
| `AFFINE_CORE.md` | `634dd3bbc35436e9d1760bee5c11cbf2124b3c42e8920a1bf3a4fcbb15039711` | Match |
| `SOURCE_AND_LIMIT_BRIDGE.md` | `2a140f2a5a39f911b5c2ca51bc79102d20e9209f1450d38005360c88103f6e77` | Match |
| `INITIAL_MOTION_AND_NORMALIZATION.md` | `c96316fdc481ef3f9e6fc402514ca9b45bcff12e199023505fbbb86d4e15bf24` | Match |

The inspected contract has SHA-256 `3b7631880fe9438f778de1d07797aae7b2f083c57730d368fb1fa57e3f3c0d20`. I also independently verified all eleven entries of `SOURCE_HASHES.json`; every attached source matched. Hash verification of a source is distinguished from reading every line of that source.

The original mathematical dependencies inspected were:

- `THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA.md`, in full, including the expanded response inequalities and four-stage closure.
- `PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md`, in full.
- `FIXED_CAP_VELOCITY_BRIDGE.md`, in full.
- `INITIAL_FEATURE_LEARNING.md`, in full, as the source of the fixed-transcript motion argument; its shifted-activation conclusions were not imported for the odd family.
- `L3_LOCAL_COMPLETE_PROOF.md`: finite Gaussian conditioning, source-derivative identification, singular-query regularization, common bounded actions and actual adjunction, scalar gradient differentiability, trajectory chain rules, and the explicit initialized-transpose calculation.
- `TWO_SAMPLE_SOURCE_BASELINE.md`, Sections 5–8: finite-array primal hypothesis, affine norm and probe estimates, response constants, and the passage from bounded population reference paths to finite-array bounds.
- `NONLINEAR_RESPONSE_PERTURBATION.md`, its closure and current-return section, cross-checked against the expanded controlled-response proof.

## Obligations and findings

### 1. Initial Gaussian support and both label sectors — satisfied

For \(\phi(z)=az+e\arctan z\), strict monotonicity gives both
\(|\phi(u)-\phi(v)|\ge a|u-v|\) and, by oddness, \(|\phi(u)+\phi(v)|\ge a|u+v|\). Consequently

\[
q_\ell\pm c_\ell\ge a^{2\ell}(1\pm\rho),\qquad
\kappa_0=(q_3+\tau c_3)/2\ge\delta/128.
\]

The separated input covariance is positive definite. Full Gaussian density and the nonconstant, strictly increasing activation make each successive feature Gram positive definite; the next fresh Gaussian forward call is therefore nondegenerate. No shifted-activation kernel formula is used. At \(e=0\), the correct reference value is \(a^6(1+\tau\rho)/2\).

Label folding is exact at finite width: replacing \((x_i,y_i)\) by \((y_i x_i,1)\) preserves the entire loss as a function of raw parameters, hence its gradient and both algorithms. The derivative of an odd activation is even, so the backward residual-free fields have the required transformation. The folded angle is \(\tau\rho\), still in the same separated class. The caps preserve this equivariance because their nonlinear gate coefficient is even in the preactivation and their incoming-field clips are odd.

The scalar population symmetry is obtained from deterministic fixed-program contractions and exchange-invariant initialization, then passed through strong limits. It does not presume uniqueness before constructing the flow, and it is not incorrectly asserted for finite-width predictions. In the final revision, the scalar prediction/loss identities are explicitly separated from the gradient identities: the uncut physical equation is \(\dot\Theta=2(1-g)\nabla g\), while the capped equation is \(\dot\Theta=2(1-g)V_R\). The capped feature field need not be a gradient, and the revised text correctly withholds its uncut kernel-derivative identity. The later cap-clock and comparison arguments already use precisely this distinction.

### 2. Both reused transposes retain the full covariance — satisfied

The first backward query is \(\beta_i^3=H_0\phi'(Z_i^3)\). Its full second-moment matrix \(S_3\) is positive definite for every fixed \(e>0\). A vanishing quadratic form yields an everywhere product identity; the first factor has at most one zero in either freely varied coordinate. The second factor must therefore vanish everywhere, and the nonconstant derivative \(\phi'\) forces both coefficients to vanish. This covers the same-label sector as well as the opposite-label sector. A uniform lower bound on \(\lambda_{\min}(S_3)\) as \(e\downarrow0\) is neither claimed nor needed.

The formula

\[
B_0^*\beta_i^3=G_i^2+\sum_jh_j^2 E[\partial_{z_j}\beta_i^3],
\qquad \operatorname{Cov}(G^2)=S_3,
\]

has the correct covariance and response. Direct finite Gaussian conditioning confirms this: after conditioning on the forward outputs, the remaining random term is a Gaussian transpose multiplied by a finite-rank projection in the input-neuron space. Removing that projection costs normalized mean square of order \(1/n\) per fixed rank. The coordinate covariance thus remains the full query second moment; one must not subtract the forward regression contribution from \(S_3\). Gaussian integration by parts identifies the deterministic response coefficients written in the candidate.

Conditionally on the middle forward pair,
\(\operatorname{Cov}(\beta^2)=\operatorname{diag}(D^2)S_3\operatorname{diag}(D^2)\), so \(S_2\succeq a^2\lambda_{\min}(S_3)I>0\). For the next reuse of \(A_0^*\), the innovation likewise has full covariance \(S_2\) and is independent of the bottom root pair. Its source derivative holds the deterministic first response and Gaussian covariance parameters fixed, keeps the new Gaussian source as a separate formal argument, and differentiates the actual \(h^2\)-dependent response. The relevant current return is not omitted.

The initialized queries have the finite Gaussian moments needed for smooth truncation at this single transcript. The proof does not infer a mesh-uniform truncation result from that single-transcript argument.

### 3. Every hidden block and every sample/layer moves — satisfied

For matrix blocks, the identity

\[
\|V^\ell\|_{\rm HS}^2
=\operatorname{tr}\bigl(S\operatorname{diag}(p)F\operatorname{diag}(p)\bigr)>0
\]

is correctly normalized: a finite rank-one update is \(uv^T/n\), whose ordinary Frobenius norm is \(\|u\|_n\|v\|_n\). Both matrices in the trace product are positive definite. The bottom conditional covariance gives
\(dE\|V^1\|^2\ge a^2\lambda_{\min}(S_2)/2>0\), using the raw first-layer factor \(d\).

The bottom sample acceleration is
\(U_i^1=\sum_j\Gamma_{ij}p_j\beta_j^1\). Its conditional variance is at least \(a^2\lambda_{\min}(S_2)/4\), since \(\Gamma_{ii}=1\). The upper-layer adjoint identities give a positive aggregate pairing with \(U^2\) and \(U^3\). They alone would only establish one moving sample per layer; the proof supplies the additional required symmetry.

Under the input-exchange reflection and readout sign change \((w,A,B,C)\mapsto(Qw,A,B,\tau C)\), the initial beta fields transform as \(\beta_i^\ell\mapsto\tau\beta_{\pi i}^\ell\). The hidden block directions transform as \(V^1\mapsto QV^1\), with \(V^2,V^3\) unchanged, and the preactivation accelerations exchange sample indices. Thus their two squared population norms agree. The aggregate strict positivity makes each sample acceleration nonzero in both upper layers. Multiplication by \(D_i^\ell\ge a\) preserves nonzeroness for features.

The strong expansion uses bounded continuous multipliers acting on fixed \(L^2\) variables and operator-norm continuity of the trained actions. It does not assume Fréchet differentiability of the nonlinear activation map from all of \(L^2\) to \(L^2\). It proves
\(b_i^\ell(s)/s\to\beta_i^\ell\), followed by
\(\vartheta(s)=\vartheta(0)+s^2V/2+o(s^2)\) in the raw hidden norm. The claim is blockwise; it correctly excludes any assertion that scalar first-layer directions orthogonal to the input span move.

### 4. Kernel and physical-time coefficients — satisfied

Adjunction gives \(V=J_0^*H_0\), and hence

\[
\kappa_4(s)=\kappa_0+s^2\|V\|^2+o(s^2),\qquad
\kappa(s)=\kappa_0+2s^2\|V\|^2+o(s^2).
\]

The first added contribution comes from the readout feature Gram; the hidden-gradient squared norm supplies the second. Both use the projection \(y^TKy/4\), consistent with \(p_i=y_i/2\).

Since \(s'=2(1-g)\), \(s'(0)=2\), \(s''(0)=-4\kappa_0\). Therefore hidden physical acceleration is \(4V\), and the quadratic coefficients of \(\kappa_4(t)\) and \(\kappa(t)\) are respectively \(4\|V\|^2\) and \(8\|V\|^2\). The readout has feature-time derivatives \(C_s'(0)=H_0\), \(C_s''(0)=0\), but physical derivatives \(\dot C(0)=2H_0\), \(\ddot C(0)=-4\kappa_0H_0\). There is no mistaken transfer of zero feature-time readout acceleration to physical time.

### 5. Uniform affine reference and nonaffinity — satisfied

The affine gradient is a locally Lipschitz polynomial field on the raw increment Hilbert space. The radial identity \(C''=JJ^*C\) makes \(\|C\|\) convex and yields \(\|C'\|^2\ge\kappa_0\). Before the hit of \(g=3/2\), the energy bounds raw displacement and gives a strong endpoint at a finite maximal time. Local affine existence then rules out premature termination. The bounds \(S\le192/\delta\), \(\|\Theta-\Theta_0\|\le12\sqrt{2/\delta}\) are arithmetically correct and independent of the data and gain in the stated ranges.

The inactive fields are frozen by a conditional finite-width calculation, not by an unsupported deduction from bounded learned operators. The affine training fields depend only on the active root and initial matrices, while the inactive Gaussian root is conditionally independent. A bounded Frobenius learned increment acts on it with normalized mean square \(v_v\|\Delta A\|_F^2/n\to0\). The analogous product-operator and scalar-contraction estimates justify the higher-layer freezing and active/inactive orthogonality. Strong affine Euler limits preserve these facts.

Affine coordinate programs remain linear in jointly Gaussian sources with deterministic scalar contractions. Their centered Gaussian laws therefore persist in the strong limit. The frozen inactive variance gives the required uniform lower variance \(\delta/32\); the bounded reference gives the upper standard deviation \(U^3\).

The Gaussian arctangent regression residual has a strictly positive minimum on this compact interval of nonzero standard deviations. The perturbative transfer correctly controls the optimal slope of the perturbed regression by \(\pi/m\), using \(\operatorname{sd}(Z)\ge m/2\). Thus the uniform \(L^2\) comparison transfers the residual lower bound without asserting Gaussianity of trained nonlinear preactivations. The activation's affine regression error is exactly \(e^2\mathcal R(Z)\). It is uniformly positive over the full constructed feature interval, hence at all finite physical times.

### 6. Source threshold, construction, and global continuation — satisfied

The extension of the controlled-response argument checks the actual places where gain and offset enter. Removing the offset decreases the available norm upper bounds; factors of \(a\in[1/2,1]\) are dominated by one. The finite-array affine premise is obtained from strong affine Euler approximation and exact rank-one unrolling, without claiming finite trained-operator norm convergence. The same-state perturbation estimate is independent of cap, and comparison uses only the affine field's Lipschitz constant.

The source proof retains full second moments, separate formal variables at singular covariances, both orientations, learned memories, and both current transpose returns. The four response stages are causal. The derivative envelope includes the current backward-output factor, and its moments follow from weighted sums of Gaussian-tail variables rather than a random supremum over source times. Replacing gains by upper bounds before selecting the finite response constant produces one positive threshold, not an unproved positive infimum over pointwise thresholds.

The asymmetric gate comparison has one factor proportional to \(eR\); propagated incoming errors do not accumulate extra factors of \(R\). Reference Gaussian tails therefore defeat its exponential stability factor. This supplies strong convergence of caps and raw directions, the autonomous uncut equation, and uniqueness against bounded-primal competitors without imposing tails or symmetry on the competitor. Starting the comparison at a reached state proves unique continuation there.

The endpoint comparison gives \(g(S)>1\). The first hit of one is strictly before \(S\), and the bounded feature-time derivative implies that the physical-time integral diverges at that hit. The same clock construction for capped paths does not require their vector field to be a gradient or their prediction to be monotone. The resulting global physical paths stay in the compact feature interval; no further smallness condition depending on physical horizon is introduced. For the uncut path, the radial estimate also gives the displayed loss bound \(\mathcal L(t)\le e^{-\delta t/32}\).

### 7. Finite GF, simultaneous raw GD, and observables — satisfied

The finite physical equations use both actual residuals. Fixed-cap fixed-mesh laws identify their scalar contractions causally, and finite rank-one unrolling supplies a larger primal ball with slack. Width-independent deterministic Euler comparison then removes the auxiliary mesh. The asymmetric comparison identifies uncut finite GF; for the raw GD interpolation, its direction is evaluated at the preceding raw node and the extra fixed-cap reference error is \(O_{R,T}(n^{-2})\). No Gaussian law is applied to an increasing transcript.

The original random readout is retained and has normalized initial norm \(O_{\mathbb P}(n^{-1})\); fixed-program stability yields its zero population limit. The theorem does not silently substitute a different finite initialization.

The velocity bridge first truncates the product queries that do not have bounded coordinate derivatives. The two appended forward action queries retain their response and learned-memory terms. For cap removal, the deterministic velocity comparison truncates the reference velocity factor. Compactness of the uncut velocity's continuous \(L^2\) time image provides uniform tail decay, so the argument does not need a bound on the growth of cap-dependent fourth moments. The order width, cap, and velocity truncation is adequate for the claimed same-layer laws and integrated speeds.

Finally, the path interpolation inequality controls the empirical mean squared supremum error by integrated squared speeds, and fixed-grid joint laws then yield the stated \(\mathcal W_2(C([0,T]))\) path limits. The proof does not infer path-space convergence from marginal state convergence alone. The four raw kernel matrices follow from the retained \(L^2\) contractions, including off-diagonal entries.

### 8. Convex and Gaussian-unit-energy witnesses — satisfied

For \(0<\theta\le e_\delta\le1/4\), \(a=1-\theta\) and \(e=\theta\) lie in the proved rectangle, giving the genuine convex mixture. For the normalized family, with \(m=E[G\arctan G]\) and \(b=E[(\arctan G)^2]\), pointwise strict contraction gives \(0<b<m<1\), and

\[
D_r^2=1+2mr+br^2,\qquad 1<D_r<1+r\le2.
\]

Thus \(a_r=D_r^{-1}\in[1/2,1]\), \(0<e_r=r/D_r\le e_\delta\), and the Gaussian energy is exactly one. Every initialized forward preactivation marginal is then standard Gaussian by the fresh Gaussian variance recursion. No trained-variance conservation is asserted.

A positive nontrivial convex mixture of these two specific functions has Gaussian energy strictly below one. The normalized positive weights sum to more than one. The candidate explicitly distinguishes these compatible separate witnesses from an impossible simultaneous convex-weight and exact-unit-energy demand.

## Remaining issues and limits of this verdict

**No substantive proof gap or counterexample was found for the stated contract.** All motion claims concern the population path and initial derivatives; they do not claim perpetual motion of every block or coordinate, finite-width exact scalar symmetry, or convergence uniformly on the entire physical half-line. The incompatible endpoint cases are correctly excluded. The selected threshold may be very small, but is mathematically positive and depends only on \(\delta\).

The final scalar-reduction scope correction has been checked directly in both changed files. There is no outstanding correction requested by this review.

# Scoped adversarial audit: input nonlinearity and nonlinear feature increments

Date: 2026-10-10. Reviewer: fresh scoped agent `audit_joint_input`.

**Verdict: PASS within the assigned conditional scope.** The full Hermite/kernel/four-input argument, the nonlinear first-layer increment argument, and their transfer to the compressed predictors are valid under the stated hypotheses and the separately assumed initialization, strong-time, and compression conclusions. No unresolved mathematical correction was found in these components. This is not a complete audit of those assumed dependencies, the full paper, or a promotion review.

## Inputs, coverage, and isolation

The neutral assignment restricted scientific inputs to `paper/compact.tex` through its setup/headline/proof architecture, `paper/feature_learning_theorem.tex`, and `paper/feature_learning_proof.tex`. It specifically instructed the reviewer to treat `fl:initial-activity` and `fl:strong-time` as hypotheses, and to attack even activations, excess sample count, two-dimensional training span, affine training labels, and unbounded activation values.

Read completely: both feature-learning files, including all bodies in the proof file. Audited in detail: `fl:input-lemma`, `fl:bootstrap`, `fl:nonlinear-feature`, and the theorem-transfer argument. The strong-time body was read, but its validity remains an assigned hypothesis rather than a component certified by this report. The initialization file included by the proof was not opened. No study history, previous report, other reviewer result, other study, archived book, or external source was read.

Required instructions read: root `AGENTS.md`, `RESEARCH_WORKFLOW.md`, `solve-math-rigorously/SKILL.md`, and `explain-with-canonical-notation/SKILL.md` including its neural-network reference. No ordinary author startup reading was performed.

Coverage disclosure: the initial `compact.tex` display ran through line 290, incidentally exposing the start of the assembly paragraph beyond the assigned proof-architecture boundary at line 254. None of the additional cited dependencies was fetched or audited. The scoped conditional verdict does not rely on that incidental text.

Files changed during review. Both feature-learning files were reread completely after the first changes; the theorem was reread again after the final Taylor-panel clarification. The final checked hashes are:

| File | SHA-256 |
|---|---|
| `paper/compact.tex` | `5abb853fb955e97b6babf994f2f003faad70ac3e3e0aa4121edddd43a6d337b1` |
| `paper/feature_learning_theorem.tex` | `f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f` |
| `paper/feature_learning_proof.tex` | `3dfdef1a4d9faa89ec4ebbdce03a53cdae63cdbde5e4a2b9bd192e7cb8f6da63` |

Repository HEAD at review: `c17cb8c2e8d486ccc1d2b80e8cd173ba551145ae`. The worktree was dirty. No paper or Git-index changes were made by this reviewer; only this report was written.

## Mathematical checks

### Full Hermite expansion and composition

The assumptions imply linear growth of every activation on the real axis, hence Gaussian square integrability at each positive variance. The Hermite covariance identity is correctly normalized for the orthonormal Hermite polynomials. Completeness follows from the entire Gaussian transform argument: Cauchy–Schwarz provides locally uniform integrability of every exponential derivative, and evaluating the zero transform on the imaginary axis gives the Fourier transform of an integrable function.

A finite Hermite expansion would equal a polynomial almost everywhere under a Gaussian with positive density, hence everywhere by continuity. A polynomial with bounded real derivative is affine. Thus every nonaffine activation has unbounded positive Hermite support. This argument does not require odd coefficients, a nonzero first Hermite coefficient, zero activation mean, or bounded activation values.

At each layer, the diagonal variance is strictly positive because a nonzero continuous activation cannot vanish Gaussian-almost everywhere. The composition at `feature_learning_proof.tex:50` preserves nonnegative coefficients even with a nonzero inner constant coefficient. Their sum is finite by evaluating at one and applying Tonelli. This establishes absolute uniform convergence on the full interval, including both endpoints. Selecting one nonconstant positive inner coefficient and arbitrarily high positive outer coefficients proves unbounded support of the composed series.

### Projected kernel and arbitrary nonzero labels

The affine projection has the correct factor of the input dimension. Applying it to the tensor kernel removes precisely its degree-zero and degree-one spherical components:

\[
(I-P)_v(v^\top u)^k=(v^\top u)^k-a_k-b_kv^\top u.
\]

The removed expression is affine in both variables. Consequently a second projection in the other variable leaves the same residual, and the residual is the Gram kernel of the projected tensor feature. This verifies the positive-semidefinite claim, rather than assuming that subtracting arbitrary positive kernels preserves positivity.

For distinct nonparallel normalized training inputs, every off-diagonal absolute inner product is strictly below one. In dimension at least two, the exceptional sphere points with inner product of absolute value one have surface measure zero. Therefore the projected training matrices converge to the identity as the degree tends to infinity. Every sufficiently large degree is strictly positive definite. Unbounded positive coefficient support then makes the residual kernel strictly positive on every nonzero label vector. This remains true for even activations, for more samples than input dimensions, and for labels obtained by restricting an affine function to the training data.

The finite-query covariance convergence uses conditional independence only in the forward pass. Gaussian fourth moments and linear growth control the conditional product variance, and covariance-square-root coupling handles singular covariance matrices. No full-rank input assumption is hidden in this step.

### Four deterministic points

The great-circle reduction is valid. If every great-circle restriction were affine, the antipodal average would be the same constant globally, because any two sphere points belong to a common great circle. The remaining odd function extends homogeneously to the ambient space, and its restriction to every plane is linear. Every pair of vectors lies in such a plane, proving additivity and global linearity.

On a circle witnessing nonaffinity, three distinct circle points are not collinear and determine an affine function on their plane. A fourth discrepancy gives an affine dependence annihilating constants and all ambient linear functions. Normalizing its coefficients in absolute sum gives exactly the uniform-norm witness used later. Dependence on the fixed labels is allowed because labels are available before initialization. No realized weights, trained weights, or passive labels are used.

### Nonlinear first-layer increments

The deterministic geometric claim at `feature_learning_proof.tex:392` is valid even when the training span has dimension two. For nonzero row vectors \(g,r\) in that span, suppose

\[
\phi_1'(g^\top v)(r^\top v)=a^\top v+b
\]

on its unit sphere. Evaluating at the equator perpendicular to \(r\), including its antipodes, gives \(b=0\) and \(a\) parallel to \(r\). The equator consists of only two points in dimension two, but they still span the one-dimensional orthogonal complement, so this case causes no failure. Division away from the equator, followed by continuity, forces \(\phi_1'\) to be constant on a nontrivial interval. Analyticity forces global affinity, a contradiction. Neither independence of \(g\) and \(r\) nor an odd activation is required.

The asserted joint empirical convergence with second moments is sufficient for the projected squared acceleration to converge: the integrand is continuous and bounded by a fixed constant times \(\|r\|^2\). The Gaussian marginal gives \(g\ne0\) almost surely, while positive acceleration second moment gives positive probability that \(r\ne0\). This yields a strictly positive expectation without any independence assumption.

The remainder argument legitimately uses second moments rather than a hidden fourth-moment assumption. The truncated Taylor error divided by \(t^2\) is at most \(\|\phi_1''\|_\infty t^2D^2/8\); the complement is controlled by \(\|\phi_1'\|_\infty\|r\|\). Choosing the truncation before the deterministic time gives the stated remainder quantifier. Contractive affine projection and the first-layer weight expansion then give a positive squared distance of order \(t^4\). Unbounded values of \(\phi_1\) do not enter these increment estimates.

### Quantifiers, comparisons, and transfer

The bootstrap constants do close: its chosen time satisfies \(ET^2\le1/2\), and the claimed first-order output remainder follows from the stated readout and feature bounds. Thus convergence of the four initial velocities gives a width-independent short interval on which their signed output combination is bounded below by a positive multiple of time.

The frozen-initial-kernel comparison is exactly readout-only training here: at zero initial readout, every hidden-weight derivative of the output is zero. With hidden features fixed, readout gradient flow has the constant initial feature Gram and the same passive-input cross-kernel. The assumed positive cubic label projection gives a coordinate gap through division by the nonzero quantity \(\|y\|_1\).

For each fixed positive time, an error converging to zero in probability transfers both positive dense gaps. Finite intersections allow common deterministic constants for the three constructions and finitely many layer claims. The result does not assert transfer uniformly as time shrinks with width; that stronger claim would require a relative-in-time error estimate. The theorem correctly fixes time before taking width to infinity.

A deep linear network, including biases and time-dependent parameters, is affine in the input at each fixed time, so the first comparison excludes every such predictor on the promised set. The second comparison excludes the coupled reference's initial frozen kernel, not every possible fixed nonlinear feature representation. The internal feature statements concern dense neurons; no correspondence to individual compressed coordinates is established or claimed.

## Adversarial deterministic checks

The following bounded numerical checks supplemented the proofs; they are sanity checks, not evidence replacing them. A `python`/NumPy command ran in `/home/amir/Codes/PDE`, exited zero, and wrote no files. It used dimension two, five unit training vectors at angles \(0,0.43,1.10,2.20,2.80\), and affine training labels \(y_a=0.3+0.2(v_a)_1-0.4(v_a)_2\). The maximum off-diagonal absolute correlation was `0.9422223406686581`, and the training span had rank two.

At depth two, the even activation \(\phi(z)=\cos z\) has
\(F_1(s)=e^{-1}\cosh s\) and \(F_2(s)=e^{-F_1(1)}\cosh(F_1(s))\).
For the unbounded activation \(\phi(z)=z+\cos z\), the same formulas acquire the linear term \(s\) in \(F_1\) and the term \(F_1(s)\) in \(F_2\). Both satisfy the stipulated strip and derivative hypotheses. A uniform 16,384-point circle quadrature gave:

| Activation | Minimum eigenvalue, layer one | Minimum eigenvalue, layer two | Affine-projected velocity RMS |
|---|---:|---:|---:|
| \(\cos z\) | 0.0007427332 | 0.0009077067 | 0.0063990664 |
| \(z+\cos z\) | 0.0097810765 | 0.0379610902 | 0.0410374069 |

The projected power-kernel minimum eigenvalues at degrees 2, 10, 50, and 200 were respectively approximately `-2.35e-16`, `0.145388`, `0.461245`, and `0.718260`. The degree-two numerical zero is consistent with low-rank spherical harmonics; strict positivity only at sufficiently high degree is essential to the proof.

For \(g=(0.7,-1.1)\), \(r=(0.3,0.8)\), the affine-projected squared circle norm of \(\phi'(g^\top v)r^\top v\) was `0.1054264531` for both activations. The equality is expected because their derivatives differ by a constant and the resulting extra term is linear in \(v\).

The numeric label scale was chosen to expose cancellation, not to reproduce the small-label condition. Multiplying the labels by any positive sufficiently small scalar enforces that condition, preserves positivity of both Gram matrices, and merely rescales the nonzero projected velocity. No neural-training experiment or approximation-storage reproduction was performed.

## Repair status and remaining boundary

One statement clarification was recommended during review: explicitly enlarge Taylor's \(\mathcal X\) before the inequalities. An arbitrary original panel can admit exact affine interpolation. The coordinator applied this change, and the final theorem now states the augmented query set and its count of at most \(p+4\). This resolves the ambiguity. The existing proof already supplied the deterministic witnesses and the factors of at most nine and three in the quadratic and linear storage terms.

No further repair is required for the audited components. Acceptance of the complete theorem still requires the independently checked initialization/activity lemma, strong-time expansion, and compression construction bounds. This report must not be represented as having verified those omitted dependencies, fitted-endpoint activity, population test risk, or a neuron-level feature correspondence for the compressed systems.

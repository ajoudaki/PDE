# Independent final audit: nonlinear reference and scope

Verdict: **PASS for the stated partial claims only.** This is not certification of the requested global joint population/GF/raw-GD theorem. No polynomial activation threshold for that theorem is proved or refuted by these files.

Audit date: 2026-09-08. No experiments were run and no canonical files were edited. The five candidate files were read directly. Previous review verdicts were not used as premises.

## Exact audited versions

| File under `studies/mean_field_peeling/three_sample_odd_activation_depth2/` | SHA-256 |
|---|---|
| `REPORT.md` | `25cfd1e93b619b6c5aabc674cab7170199024ac7a3cb700365a23048e62d341f` |
| `CONTRACT.md` | `e4acafb4b6dee57ab867bd3947a92b6b25d994c51e62bbfaeaaccebede6c113d` |
| `GEOMETRY_AND_NECESSARY_SCALES.md` | `37a6c0bf1715ab5a182ecfd9a6a3213cddf9cb4a0ae95fd441a5a6a7d46f61e6` |
| `SOURCE_AND_CONTINUATION.md` | `4c3b8c54893a417ce210f73eaae2b8e71a71eac8f3205f5fdc32da9480c2a568` |
| `NONLINEAR_REFERENCE.md` | `778793eb7a832f16dadc5b5746e9b705c02ca08a74ab9e3f81748962a958a422` |

The source file hash includes the corrected statement about uniform integrability of **squared magnitudes** on bounded L2 balls.

## Actual dependencies checked

The following mathematical sources, rather than their review files, were inspected:

- `two_sample_odd_activation_depth56/PROOF.md`, for raw normalization and the exact old quantitative loss conclusion;
- `two_sample_odd_activation_depth56/AFFINE_CERTIFICATE.md`, Section 1, for the initialized action bound;
- `two_sample_odd_activation_theorem/sources/L3_LOCAL_COMPLETE_PROOF.md`, the finite Gaussian conditioning and singular-query derivation, followed by the common population action/adjunction construction;
- `two_sample_odd_activation_theorem/sources/TWO_SAMPLE_SOURCE_BASELINE.md`, for chronological query and formal derivative conventions;
- `two_sample_odd_activation_theorem/sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md`, for the conditional asymmetric gate/cap-removal implication.

The Gaussian norm input was also verified against the author's primary text: Vershynin, [High-Dimensional Probability, Theorem 7.3.1 and the Gaussian matrix tail corollary](https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-2.pdf). For an n-by-n standard Gaussian matrix G it gives E||G|| <= 2 sqrt(n) and P(||G|| >= 2 sqrt(n)+t) <= 2 exp(-c t^2). Substitution W=G/sqrt(n), followed by the finite-generated-query limit and dense-span extension, supports the canonical action norm at most two. It does not assert operator-norm convergence of finite matrices.

## Nonlinear-reference checks

1. **The initialized isometry is used on a legitimate fixed span.** The three frozen first-layer features depend only on the initial first-neuron root, independently of the initialized adjacent matrix. Conditional Gaussian averaging therefore gives the forward Gram identity `<A0 h_i,A0 h_j>=<h_i,h_j>`. By linearity it holds on their finite span. This is not an assertion that A0 is an isometry on all adaptive inputs. The construction retains the actual adjoint A0*, including its reverse response.

2. **The invariant and global reference theorem are correct.** Put S=H Q^(-1/2); then S*S=I, B=AS, and direct substitution gives Bdot=a C e^T Q^(1/2), Cdot=a B Q^(1/2)e. Starting with C=0 and B0 an isometry, the equations preserve E=ran(B0) and their cross terms cancel in d(BB*-C tensor C)/dt. Thus BB*|E=I+C tensor C and B*B>=I. The readout kernel is at least a^2 Q, so loss decreases at rate at least 2a^2 lambda_min(Q). The identity ||B*C||^2=c^2+c^4 and ||f||<=2sqrt(3) supply the stated uniform c and B bounds. The increment A-A0=(B-B0)S* has finite rank and the same operator bound; its HS norm has only a fixed factor sqrt(3). The resulting finite-dimensional locally Lipschitz system continues globally. This proves the separate frozen-bottom, affine-top reference theorem, not a theorem for the user's model.

3. **The equilateral one-feature solution is exact.** Permutation symmetry gives `<e0,h_i>=mu` for each sample, since the average is v=mu e0. The Gaussian fixed-span identity then gives `<p0,A0 h_i>=mu`. Hence the stated C=c p0 and A=A0+(d-1)p0 tensor e0 solve ascent on J=a<C,Av>, with c'=a mu d, d'=a mu c. They produce equal reference predictions J=a mu cd and are actual reparametrizations of the reference physical GF up to every fixed j<1. At J=j, c^2 has the displayed exact quadratic solution, a theta c^2 -> j/tau, and c,d are of order theta^(-1/2).

4. **The affine-top bottom-force limit retains the reverse action correctly.** The equality A*C=c A0*p0+c(d-1)e0 is exact. Since ||A0*p0||<=2 and c diverges, A*C/c^2 -> e0 in L2. The gate cancellation sum u_i=0 gives grad_w J=a theta(A*C)U. U is bounded, so multiplication preserves the strong convergence and yields j TU/tau^2. At (Z1,Z2,Z3)=(t,t,-2t), t>0, both T and U are nonzero; continuity and the Gaussian plane's positive density establish ||TU||_2>0. No unjustified replacement A0*p0=e0 is made.

5. **Restoring the true top nonlinearity preserves the nonzero physical defect.** The upper tuple `(p0,xi_1,xi_2,xi_3)` is centered jointly Gaussian and permutation invariant, so alpha_i=E[p0^2 g(z_i^2)] is common and lies in [0,1]. Expanding A*{C[a+theta g(z_i^2)]} gives exactly the three terms in the note. The A0* remainder has norm at most a fixed multiple of theta c=O(sqrt(theta)). In the rank-one remainder the common alpha permits the crucial cancellation of the bottom linear gate, leaving O(theta^2 c(d-1))=O(theta). Also |J_true-J|<=pi theta c/2 ->0, and Gaussian sample symmetry makes all three true predictions equal at the reference state. The actual physical bottom block therefore converges strongly to 3j(1-j)TU/tau^2, a nonzero vector. This statement concerns vector fields evaluated at explicit reference states, and the document correctly avoids claiming that a true trajectory passes through them or must stay far from the reference.

## Geometry/source context and inference limits

The geometry argument handles singular input Grams without inversion. Each dual tensor has unit norm and isolates one cubic tensor with pairing at least delta(2-delta); summing its three coordinate bounds proves the stated cubic Gram floor. The arctangent cubic Hermite coefficient is `(1-2E(1+G^2)^(-1))/sqrt(6)`, which is nonzero by strict Jensen. The layer-two first Gaussian component retains a factor at least a^2. The numerical constant in the report follows from the elementary interval lower bound in the companion.

The nearly collinear family and the two successive second-difference bounds give the claimed upper scale theta^2 delta^2 for delta<=1/4, through the second hidden layer. The fixed positive-theta readout witness is therefore valid and is explicitly kept separate from joint fitting.

For equilateral labels (1,1,1), the affine initialized flow is stationary, but positive theta has a nonzero readout gradient. The exact initial derivative rules out a theta-independent exponential rate with the exact initial prefactor. The independent raw-state cancellation and energy/path-length calculation give R >= sqrt(9+2/(pi theta))-3 and the stated fitting-time lower bound, ruling out a uniform rate even with a fixed finite larger prefactor. Neither calculation rules out positive-theta fitting with a theta-dependent rate.

The source companion keeps the correct forward strict-past and reverse current/past structure, all sample/time covariances, and the actual current return E[phi''(Z_i)C]. Its conditional moment estimates and Jacobian envelopes follow from the stated coefficient prefix bounds. In particular, the derivative coefficient production bounds depend nonlinearly on those very prefix radii and do not close them on arbitrary horizons. The text does not promote these conditional inequalities to an unconditional source theorem. The revised L2-tail statement is precise. Finite-width GF continuation and conditional population energy/endpoints are correctly distinguished from construction or continuation of the uncut population solution.

The symmetric scalar-clock argument is valid conditional on strong ascent continuation through the first hit and the stated canonical symmetry. Monotonicity of J/c gives J'>=||H0||^2; bounded gradient through the hit forces divergence of the physical clock integral. Generic triples are not assigned that scalar clock.

No false positive full theorem claim or false negative qualitative impossibility claim was found. The report explicitly leaves global uncut construction, uniqueness/restart, full-width GF/GD and velocity/path conclusions, generic three-residual fitting, and trained nonaffinity unresolved. Its final positive result is initialization geometry, supported by the other clearly labeled partial results. **PASS applies only to that scope.**

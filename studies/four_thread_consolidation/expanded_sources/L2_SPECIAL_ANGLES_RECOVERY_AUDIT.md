# Recovered L2 special-angle theorem and all-angle partial result

Read-only evidence consolidation, 8 September 2026. The recovered 1,977-line special-angle proof, its certificate, and all three complete round-two reviewer reports were read. Their hashes were independently compared with the certificate and all match. No proof search or experiments were performed. The separate 1,595-line all-angle author snapshot and the final all-angle certificate were also read in full. The exact 1,623-line final all-angle source was subsequently recovered, its certificate hash verified, and its entire notation-only delta from the fully read snapshot checked with context.

## 1. Global special-angle result: exact source and reviews

The recovered primary source is [L2_TWO_SAMPLE_SPECIAL_ANGLES_COMPLETE_PROOF.md](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OLDER_TWO_SAMPLE_RECOVERED/l2-two-sample-proof-0ywjpp/L2_TWO_SAMPLE_SPECIAL_ANGLES_COMPLETE_PROOF.md): 94,653 bytes, 1,977 lines, SHA-256

`830ca8830edddd5acf351664e71a346a702dd8c73e9191775458fec8b6df71e0`.

The [6 September certificate](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OLDER_TWO_SAMPLE_RECOVERED/l2-two-sample-proof-0ywjpp/SPECIAL_ANGLES_AUDIT_CERTIFICATE.md) records three fresh-context, isolated, full-document PASS reviews with no required mathematical correction. Recovered report hashes match its table:

| Report | Lines | SHA-256 |
|---|---:|---|
| [Round 2 A](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OLDER_TWO_SAMPLE_RECOVERED/l2-two-sample-proof-0ywjpp/SPECIAL_ANGLES_COMPLETE_REVIEW_ROUND2_A.md) | 427 | `801a661c457579f6aec06f9a9c2ffc9c671ae83acdf974c91035b32df4fc63ed` |
| [Round 2 B](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OLDER_TWO_SAMPLE_RECOVERED/l2-two-sample-proof-0ywjpp/SPECIAL_ANGLES_COMPLETE_REVIEW_ROUND2_B.md) | 328 | `7b631fd210553ba669a5c315fa1776aa892e31487b4b57facf788aa6b684a359` |
| [Round 2 C](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OLDER_TWO_SAMPLE_RECOVERED/l2-two-sample-proof-0ywjpp/SPECIAL_ANGLES_COMPLETE_REVIEW_ROUND2_C.md) | 480 | `3acd8233637f1353fba2f9c88b16065535f719e577e6648d89a3afb3f931dcb9` |

The reports identify the same sole source, before/after hash, all 107 numbered equations and complete proof coverage. They used no other mathematical files or experiments. The final proof reproves its specialized Gaussian-program input; its provenance list does not import a softplus theorem or any unproved external result.

## 2. Exact model and positive statement

There are **two hidden layers**, each width n; arctangent in both layers; no biases; two deterministic normalized inputs `||x_1||²=||x_2||²=d`; correlation `ρ=x_1^T x_2/d` is **0 or −1**; labels are `(1,−1)`. Orthogonality requires d≥2. At ρ=−1 the inputs are exactly antiparallel. Inputs are fixed before initialization.

The independent Gaussian arrays have variances

`Var W^(1)=1/d`, `Var W^(2)=1/n`, `Var W^(3)=n^-2`.

Here W^(3) is already the **rescaled** readout, and prediction is `f_a=(1/n)(W^(3))^T h_a^(2)`. Thus its scale is equivalent to the raw n^-4 readout variance used in the modern one-sample theorem, rather than the old order-one-readout quadratic/ReLU setting. The loss is the **sum** `(f_1−1)²+(f_2+1)²`.

The parameter metric is

`(d/n)||ΔW^(1)||_F² + ||ΔW^(2)||_F² + (1/n)||ΔW^(3)||_2²`.

Consequently GF directions are `−(2/d)Σ r_a δ_a^(1)x_a^T`, `−(2/n)Σ r_a δ_a^(2)(h_a^(1))^T`, and `−2Σ r_a h_a^(2)`. Exact simultaneous GD multiplies these directions by `η_n=n^-2`. Physical time is `t=kη_n`, raw arrays are linearly interpolated, and every nonlinear field is recomputed from those arrays. Ordinary Euclidean GD on all three displayed rescaled arrays would be a different model.

**Accepted theorem:** one deterministic, canonical population flow exists uniquely for all finite physical times. It is autonomous and uniquely restartable from each reached **entire** state. Actual finite GF and the stipulated exact raw GD converge in probability along the **full width sequence**, on every fixed `[0,T]`, to that same population flow.

The state uses separate countably generated neuron probability spaces, a first-row field, a bounded middle operator with Hilbert–Schmidt increments, and the readout field. The initial middle source is canonical on its generated action spaces and its reverse action is its actual Hilbert adjoint. Restart retains it and all current fields. No initialization is resampled, and no artificial neuron pairing across populations is asserted.

The observable contract is unusually strong:

- Same-neuron path tuples containing both samples and all listed forward/backward fields converge separately in each population in **every fixed finite Wasserstein order** on continuous-path space with the supremum metric. The first tuple includes the complete first row, preactivation, activation, reverse query and first delta; the second includes readout, second preactivation/activation and second delta.
- Every fixed finite list of continuous polynomial-growth tests and observation times converges jointly. Predictions, loss and **all three NTK blocks** converge uniformly in time in probability.
- Fixed admissible finite-program probes in both matrix orientations converge in Wasserstein order 2, including their explicitly justified uniform L2 approximation closure. The grammar excludes width-dependent amplification of the vanishing readout and arbitrary width-dependent directions.
- All hidden preactivation/activation velocities and the readout velocity have fixed-time joint W2 convergence, the stated integrated mean-square comparisons, and squared normalized norms converging uniformly in time in probability. Parameter speeds, their integrals, individual hidden energies and parameter-increment quadratic metrics converge. The middle increment is Hilbert–Schmidt; no Hilbert–Schmidt norm is assigned to the initial source. No continuous-path law is asserted for discontinuous mesh velocities.

### Persistent activity is global in finite time

This source proves more than activity only on an initial positive window. For **every finite t≥0**, each layer/sample has strictly positive distributional distance from an affine activation law:

`inf_(u,v) E[(atan Z_a^(ℓ)(t)−u Z_a^(ℓ)(t)−v)²]>0`.

For **every t>0**, all four preactivation speeds, all four activation speeds, both hidden-parameter speeds and the readout speed are strictly positive. Their energies are positive on every positive-time interval of positive length. Hidden speeds at t=0 are zero, because the population readout starts at zero. There is no lower bound independent of t as t→∞.

Writing `κ=(1/4)y^T K y`, the full label-direction kernel satisfies

`κ(t)=κ(0)+32d_* t²+o(t²)`, with `d_*>0`.

Both hidden and readout contributions are included, so the leading changes cannot cancel. This proves kernel nonconstancy near zero, not global kernel monotonicity. The prediction obeys `f_2=−f_1` and `0<f_1(t)<1` at all finite t>0. The proof does not establish an infinite-time interchange or a uniform-in-T convergence rate, and this audit does not add a loss→0 conclusion.

### Proof mechanisms checked against the complete source

The first coordinate `F(z)=z+z³/3` exactly cancels its own arctangent derivative. At ρ=0 the input Gram is diagonal; at ρ=−1 the exact odd/even architecture relation reduces to one independent coordinate with control `−4r_1`. The loss-sum metric counts its first-row energy once.

Ordinary L2 local stability, bounded readout and finite residual action give global well-posedness. Same-width raw GD has exact cubic transformation defect, yielding uniform transformed error O_T(n^-3/2) and original hidden-velocity error O_T(n^-1). Fixed finite Gaussian programs, actual query noise at singular Grams, empirical-feedback coupling and a dense queried grammar construct the canonical actual adjoint. Fixed meshes are then removed by dimension-independent comparisons.

The global nonaffinity and strict-motion proof uses a separate substantive step: **actual fresh-root forcing** bounds each past response coefficient by C_T times its mesh step. The order is fixed mesh, nonzero forcing, width limit, Gaussian integration by parts in the independent new root, then forcing→0. Thus complete response rows have bounded absolute sums on every finite horizon. This yields Gaussian-plus-**bounded** remainders, unbounded field tails, nondegenerate reverse sources and, through the adjoint cancellation identity and exchange law, strictly positive individual hidden speeds. A primal L2 bound alone would not yield these conclusions.

At intermediate nonzero correlation the same transformed first equation contains `(1+Z_a²)/(1+Z_b²)`, an uncontrolled multiplier. Therefore this global proof does not extend itself to all angles. Newer all-angle finite-window results can coexist with this stronger persistent special-angle theorem.

## 3. All-angle result: strong first-layer compactness only

The recovered [ALL_ANGLE_FIRST_LAYER_COMPACTNESS_AUTHOR_SNAPSHOT.md](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OLDER_TWO_SAMPLE_RECOVERED/l2-two-sample-proof-0ywjpp/ALL_ANGLE_FIRST_LAYER_COMPACTNESS_AUTHOR_SNAPSHOT.md) was fully read: 1,595 lines, 65,292 bytes, SHA-256 `a3aa59799be06b90322b3825f56ed19c3f0b21d69f8a52de51518f0cfaa97586`.

The exact recovered [ALL_ANGLE_FIRST_LAYER_COMPACTNESS_COMPLETE_PROOF.md](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OLDER_TWO_SAMPLE_RECOVERED/l2-two-sample-proof-0ywjpp/ALL_ANGLE_FIRST_LAYER_COMPACTNESS_COMPLETE_PROOF.md) has 1,623 lines and 66,690 bytes. Its independently verified SHA-256 matches the [final certificate](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/OLDER_TWO_SAMPLE_RECOVERED/l2-two-sample-proof-0ywjpp/ALL_ANGLE_FIRST_COMPACTNESS_AUDIT_CERTIFICATE.md):

`910f4df8fdcaf79313858fd5a8bfe8f58dd5a655b7bb90181ef97233fa5ba8a9`.

The certificate records three isolated full-document PASS reviews and a subsequent notation-only diff read by the original supervisor. This consolidation has now read the entire [snapshot-to-final diff](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/ALL_ANGLE_COMPACTNESS_FINAL_NOTATION_DIFF.txt), with context. It capitalizes the raw parameter symbol, replaces the derivative alias by explicit activation derivatives, spells out normalized Euclidean and Frobenius norms, and displays an already-used gate-difference moment bound. The theorem assumptions, constants and convergence claims are unchanged. Thus the final certified primary source is now verified, not merely inferred from the author snapshot. This is a source-and-scope reconciliation, not a new independent mathematical certification. The three all-angle full reviewer reports are recovered, but were not reread in full in this bounded follow-up; certificate evidence is distinguished from the fully reread special-angle reviewers above.

The same L2 arctangent model, opposite labels, rescaled tiny readout, metric and η_n=n^-2 GD are used, now for **each fixed correlation −1≤ρ<1**, on every fixed finite `[0,T]`. Constants for strong compactness may depend on the fixed angle; the statement is not uniform for varying correlations approaching an endpoint.

For the first neuron keep both samples together in

`E_T = C([0,T];R²) × L²([0,T];R²) × C([0,T];R²) × L²([0,T];R²)`,

with coordinates first preactivation, its actual velocity, first activation and its actual velocity; both L2 velocity topologies are **strong**. The empirical laws lie with probability→1 in one deterministic compact subset of P2(E_T), for actual GF and actual raw GD. More strongly, a deterministic compact set contains **all** initial outcomes satisfying the specified operator/readout/fourth-moment bounds, at every GF width and every sufficiently large GD width.

Along **any** W2-convergent subsequence, the limit satisfies the position/velocity integral relations and the activation chain rule. Fixed linear reconstruction yields first-row **increments and velocities**; the unchanged initial orthogonal row component is not encoded by the two sample evaluations. Three kinetic densities converge in time L1 with no defect: first preactivation speed, first activation speed and first raw-row metric speed.

All four entries of the **node-controlled** first kernel converge in matrix-valued time L1. If `c_a=−2r_a`, these entries are `j_ab=c_a c_b K_ab^(1)`. They are reconstructed from velocity through `D=C^-1` in the interior, and `D=C/4` on the exact antiparallel invariant subspace. Their full sum equals the raw first-row speed density. This is not reconstruction of the unweighted K^(1), does not divide by possibly zero controls, and uses held node controls/deltas for GD rather than recomputed interior-cell kernels.

The proof obtains a row-work identity and an L3 space-time velocity gain from regularity of the actual reused-transpose query. The bounded logarithmic derivative of the arctangent gate gives strong time translations; combining the GD step-function bound with the mesh estimate gives a uniform **squared** L2 translation modulus O(τ^(2/5)). Finite time projections and explicit measure couplings then yield strong W2 compact containment. These are substantive positive compactness results, not full population identification.

The final certificate expressly does **not** establish full-sequence mean-field identification, uniqueness, equality of GF/GD subsequential limits, second-layer compactness, unweighted first-kernel recovery or nontrivial feature activity. The all-angle full theorem was still open in that certificate. Later complete finite-window results may supersede that open problem, but neither this partial theorem nor its certificate should be presented as the completed joint autonomous flow.

# Within-study cross-check of shared spectral memory

2026-09-29. This is a scoped internal cross-check after the independent candidate routes were frozen. It is not a fresh independent promotion review. The complete supplied `RESULT.md`, `CAUSAL_ROUTE.md`, and `spectral_memory.py` were read. No other study, book material, or manuscript was inspected. The required research/proof skills had already been read and applied in this scoped route.

## Verdict

**Accept the stated finite-width, finite-horizon, sample-uniform theorem in exact arithmetic, with the discrete-scheme and resource qualifications already stated in the reports.** No mathematical error requiring a repair was found in the strongest bounded-activation claim.

More precisely, fix width n, input dimension d, depth L, initial parameters, horizon T, globally bounded activation and derivative, with the derivative locally Lipschitz. Fix a normalized training-input bound X and a label RMS bound Y. For each rank cap r and step h>0, the specified own-response, frozen-pass, singular-shrinkage integrator is well defined through T. For any bounded test-input set, its held predictions approximate those of the canonical dense gradient flow with error

\[
\sup_{t\leq T,x\in K}|\widehat f_{r,h}(t,x)-f(t,x)|
\leq C_{T,n,d,L,\theta_0,X,Y,\phi,K}
\bigl((r+1)^{-1}+h\bigr),
\]

where the constant can be chosen independently of m, the dataset within the prescribed class, r, h, and the fixed sample ordering. At r>=n, compression is disabled and its error contribution is zero. The right-hand side can be very large; the theorem does not assert useful compression at every rank.

The moving learned middle matrices use O(Lnr) factor storage for r>=1. Full moving storage additionally includes exact outer parameters/accumulators and single-sample scratch. All original samples and initialized dense matrices remain statically accessible. Full-batch runtime still depends on m. A sample-loop index needs O(log m) bits, as already acknowledged in the causal report.

## Frozen inputs

The inspected files match the supervisor's frozen SHA-256 values:

| File | SHA-256 |
|---|---|
| `RESULT.md` | `bb12cc693c83cd2661762fd3aae33b780feac2430cdcadb9bad37c92e64cbc06` |
| `CAUSAL_ROUTE.md` | `407ba0a7162de58a136130d98f51f6f058734cd8db7cc9ffb0f9140dd5c5142a` |
| `spectral_memory.py` | `9cdbfc8084ff84de322bc43de967b94eefa3fb1eb262665534eaec769b61cc57` |

Acceptance is conditional on the canonical equations explicitly specified in `CAUSAL_ROUTE.md` Section 1. This cross-check did not independently compare those equations with external canonical sources or the maintained book.

## 1. Source compression and proximal interpretation

For each rank-one insertion A, the conceptual candidate C=M+A has rank at most r+1. If d=\(\sigma_{r+1}(C)>0\), subtracting d from every positive singular value removes nuclear mass exactly (r+1)d. The discarded matrix has operator norm d and Frobenius norm \(\sqrt{r+1}d\), including at singular-value ties. If d=0, all three corresponding identities hold with zero discard.

Thus the potential inequality

\[
\|M_q\|_*+(r+1)\sum_{i\leq q}d_i
\leq\sum_{i\leq q}\|A_i\|_*
\]

and the cumulative identity
\(\sum_{i\leq q}A_i-M_q=\sum_{i\leq q}D_i\)
give both claimed prefix bounds by the triangle inequality. This is valid for adaptive signed sources. There is no independent-source assumption and no hidden multiplication of a one-step bound by the total number of steps.

The proximal-nuclear formulation in `RESULT.md` is also correct. With B the soft-shrunk matrix and d>0, Z=(C-B)/d has operator norm at most one and pairs with B to give \(\|B\|_*\). Consequently Z is a nuclear-norm subgradient at B by the displayed duality argument. Expanding the quadratic objective proves global uniqueness of B. The rank cap selects the threshold d; this does not turn the original neural loss into a nuclear-regularized objective.

This source estimate closes the gap identified by the earlier functional route: it supplies a causal accumulated-defect bound, not just existence of a low-rank snapshot. The retained singular basis is allowed to change after every atom. Ordinary tangent-projected low-rank gradient flow and hard truncation would require different proofs.

## 2. Backward bounds and absence of first-exit dependence

The bounded-activation proof does not assume a bound on the very layer it is trying to control.

First, \(\|h_L\|/\sqrt n\leq H\) gives \(|f|\leq HB\), where \(B=\|w\|/\sqrt n\). The exact readout update in every frozen pass implies

\[
B_{k+1}\leq(1+2hH^2)B_k+2hHY.
\]

Only the mean absolute label enters, and it is at most the label RMS bound Y. The sharper readout constant in `RESULT.md` and the looser constant in `CAUSAL_ROUTE.md` both follow from this inequality and both are valid independently of rank and step count, for kh<=T. The same differential inequality bounds the exact readout.

Next, the top adjoint depends only on the bounded derivative and the bounded readout:
\(\|\delta_L\|/\sqrt n\leq s\overline B\).
Its update budget bounds the top learned matrix through the nuclear potential. For the next layer down, its adjoint depends on this already bounded upper matrix. Repeating downward yields the acyclic recursion in the reports. The first-layer update is bounded only after all upper-layer bounds have been obtained.

This argument bounds the source variation generated by the compressed trajectory itself. It does not substitute dense-network responses into the sketch. It also holds for every intermediate prefix of a completed frozen pass, because the potential bound is a prefix bound and the sources continue to use the frozen network.

These estimates give a convex bounded product of parameter norm balls containing both held numerical states and the exact trajectory. At fixed finite width, that set is compact. Therefore the bounded-gate theorem needs no first-exit argument, sufficiently large rank, sufficiently small step, fitting assumption, or maximum-label bound.

The general unbounded-activation theorem is different: its first-exit condition is necessary to the supplied proof and has not been dropped. Its bootstrap at the first exiting grid state is valid, since all source evaluations for that state occurred in preceding in-region frozen states; the endpoint itself contributes no time interval to the integral.

## 3. From operator defect to the neural trajectory

Frozen full-pass source evaluation and simultaneous outer updates give the exact cumulative relation

\[
\widehat\theta_k
=\theta_0+h\sum_{j<k}F(\widehat\theta_j)-E_k,
\]

with zero outer blocks in E and middle-block operator defects controlled by the streaming lemma. Recomputing later samples after installing earlier updates would break this identity; the prescribed algorithm does not do that.

Local Lipschitz regularity of the derivative of the activation is enough to bound \(\nabla f\) and its parameter Lipschitz constant on the common compact parameter/input set. A classical Hessian everywhere is unnecessary. The empirical vector field is an average of terms of the form \((f-y)\nabla f\). Splitting their differences as in `CAUSAL_ROUTE.md` equation (15) uses only the first absolute moment of labels, hence produces a constant uniform in m under the label RMS bound.

The conversion to the mixed operator norm is legitimate at fixed n. In the normalized norm used by the bounded-gate theorem,
\(\|\Delta\theta\|_E\leq\sqrt{nL}\|\Delta\theta\|_N\),
and the reverse comparison needed for the vector field is also valid. The resulting Lipschitz constant may depend on n; the reports correctly retain that dependence.

The held trajectory differs from its own vector-field integral by the cumulative compression defect plus an incomplete-step remainder of norm at most hM. Thus the integral inequality and Gronwall estimate are valid, including at grid jumps. No differentiability of the sketch factors or limit as h tends to zero at fixed rank is invoked.

The forward observable estimate follows by induction through the network using the global derivative bound and normalized operator estimates. For a test set larger than the training-input ball, use its own bound in the first-layer forward-difference constant; the parameter-region and feedback constants can remain those determined by the training class. This gives the advertised arbitrary bounded test-set statement.

The distinction between the two mixed norms in the reports—separate normalized outer blocks in `RESULT.md`, their combined Euclidean block in `CAUSAL_ROUTE.md`—only changes constants by a factor at most \(\sqrt2\). Each argument defines its own valid constants, so this notation difference does not invalidate either theorem.

## 4. Autonomy, ordering, and resource semantics

The accepted object is an autonomous *discrete recursion* conditional on fixed data, fixed initialized matrices, fixed h, fixed rank caps, and a fixed sample ordering. Restarting within a pass additionally keeps the frozen/working factor buffers, exact outer accumulators, and the current sample index. All those objects are explicitly accounted for.

The method need not be permutation invariant. Different sample orders can produce different compressed updates, and changing m by duplicating samples can change the atom sequence. The uniform error guarantee nevertheless holds for each such order and sample count. No order-invariance claim is needed for the proof.

Only the moving middle-layer update representation is O(Lnr). Exact first-layer/readout state and scratch add O(nd+n+Ln+d), and static initialization/data storage is not compressed. At r near n the factors can cost as much as dense learned matrices. The theorem therefore removes explicit sample-indexed response histories but does not establish simultaneous width, total-storage, or runtime independence.

The rank-zero mathematical case is valid but freezes the learned middle increments. The supplied Python class accepts ranks from 1 through the smaller matrix dimension; it does not implement rank zero or accept caps above full dimension. For a cap at full dimension, the code correctly has zero exact-arithmetic shrinkage. These implementation conventions agree with the main result's stated r>=1 scope and its full-rank saturation convention.

## 5. Implementation inspection and deterministic rerun

The skinny update factors the candidate as
\([U\operatorname{diag}(s),a][V,b]^\top\).
Reduced QR on the two factors followed by SVD of the small core yields exactly the conceptual singular shrinkage. This remains dimensionally correct for rectangular matrices, rank-deficient augmented columns, and full-rank saturation. Retaining columns with zero singular coefficient does not change the represented matrix or exceed the cap. Inverse singular values are not used.

The only dense learned matrices are produced by the separate verification helper. The production insertion and action methods retain factor arrays and an at-most-(r+1)-dimensional core; at full rank that core is naturally a full-dimensional matrix.

The authorized deterministic verification was rerun unchanged:

```sh
OPENBLAS_NUM_THREADS=1 python -B studies/shared_response_basis_20260929/spectral_memory.py --out data/generated/shared_response_basis_20260929/algebra_functional_crosscheck_001
```

It exited successfully under NumPy 1.26.4. Its new record is
`data/generated/shared_response_basis_20260929/algebra_functional_crosscheck_001/verification.json`.

| Check | Rerun result |
|---|---:|
| Adaptive stream prefixes checked | 480 |
| Maximum difference from dense one-step SVD oracle | 2.7006733775686547e-14 |
| Maximum numerical nuclear-potential excess | 8.881784197001252e-16 |
| Sharp example operator error | 1 |
| Sharp example Frobenius error | 2 |
| Repeated-update hard truncation operator error | 4.000000000000003 |
| Repeated-update soft shrinkage operator error | 1.0000000000000036 |

These checks validate the sketch algebra and its implementation on the deterministic fixtures. They do not implement or test the complete canonical neural integrator, establish arbitrary-roundoff guarantees, or constitute a neural training experiment. The reports make this distinction correctly.

Finite input arrays can still overflow or underflow in floating-point norm/product calculations; for example, extremely small nonzero factors can lead to the numerical zero-mass fast path. This is outside the exact-arithmetic theorem and outside the verified moderate-scale fixtures. It is an implementation limitation, not a contradiction of the stated theorem; no production numerical robustness claim should be added without a separate error analysis.

## 6. Repairs and remaining acceptance limits

No repair to the three frozen inputs is required for the accepted claim. The following stronger conclusions remain unproved and must not be inferred from this acceptance:

- a unique autonomous smooth ODE at fixed rank;
- a feedback constant uniform in width, or a useful rank much smaller than width in every instance;
- all-time approximation or statistical generalization to unknown labels;
- sample-independent total data storage or full-batch runtime;
- a floating-point theorem for arbitrary scale and arbitrarily long streams;
- novelty of the matrix-sketching mechanism or priority of the full neural application.

Separately, the supervisor identified a missing clock statistic in the earlier polynomial route. `FUNCTIONAL_ROUTE.md` has been corrected: \(\mathbb E_m[y^2]\) is mandatory when retaining the residual-RMS clock, although it is absent from the loss gradient itself. It adds one scalar to the displayed sufficient-statistic count. That correction does not affect the spectral-streaming theorem reviewed here.

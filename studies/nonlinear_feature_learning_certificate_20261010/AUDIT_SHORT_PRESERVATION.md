# Preservation audit of the shortened feature-learning proof

Date: 2026-10-10. Reviewer: fresh scoped agent `audit_short_preservation`.

Verdict: **PASS for preservation and the replacement argument within the assigned scope.** No theorem conclusion, hypothesis, probability qualification, activation qualification, or query-domain restriction is lost. I found no necessary hypothesis hidden in the removed technical claims. This is a proof-preservation audit of the latest theorem, not a new review of the entire compression paper or a promotion approval.

## Inputs and independence

The assignment supplied the current compact-paper setup through its proof architecture, the complete fitting source, the common feature-learning theorem, the complete old proof and initialization supplement, and the complete proposed shorter proof. I read the old and new proof bodies and the fitting source completely; a truncated read of old proof lines 363 onward was repaired by a targeted read. I used `solve-math-rigorously`, `explain-with-canonical-notation`, and its neural-network reference. I read the shared instructions and workflow, but no study README, history, previous review, other reviewer finding, other study, or archived book material.

Scope disclosure: my initial whole-file read of `paper/compact.tex` accidentally exposed its subsequent short assembly tail, beyond the requested proof-architecture boundary. This contained no reviewer material. I reported the overread to the supervisor; the replacement argument below does not use that tail as an additional scientific dependency.

The unreviewed compression constructions remain external dependencies of this scoped audit. Their stated approximation conclusions are inherited exactly as before. This report does not certify that older paper files were unchanged against an earlier repository snapshot; the supervisor must make that integration comparison.

Repository HEAD during review: `c17cb8c2e8d486ccc1d2b80e8cd173ba551145ae`. The index was empty when inspected. SHA-256 hashes of the supplied files:

| File | SHA-256 |
| --- | --- |
| `paper/compact.tex` | `5944806ea716f04baea2a8e56d79db913613c3a168dc2644cf5d81cd53daec21` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `paper/feature_learning_theorem.tex` | `f03155050f7ab9dcbe8567bb53b148da294c0c11d3bb0147dd294f2692e7403f` |
| `paper/feature_learning_proof.tex` | `0a1daaa8085fb89bb4f7c8e0fb18ff729dee30011ece0c5d9f06bccb3fbcc13c` |
| `paper/feature_learning_initialization.tex` | `f132f884304c09f32759ec63baba5bc8be056944baf514200141e597399e9ff2` |
| `paper/compact_feature_learning.tex` | `71f50a55613a3df12398d6226b8fe2380805f2f32082e134e7ab45846bfa4bd1` |

## Theorem preservation

The same theorem source is used for both proofs. The following conclusions have complete replacements in `paper/compact_feature_learning.tex`:

| Requirement | New proof location and check |
| --- | --- |
| Distance at least $c_*t$ from every affine predictor, including biases | Lines 17–75 establish the nonaffine limiting initial velocity and deterministic four-point witness; lines 179–192 give the uniform real $O(t^2)$ output remainder; lines 315–320 apply the affine-annihilating combination. |
| Distance at least $c_*t^3$ from the coupled dense reference's frozen initial kernel | Lines 253–275 prove the same positive label-projected cubic coefficient; lines 320–322 divide by $\|y\|_1$. Training inputs belong to every promised query domain. |
| RMS training-feature displacement at least $c_*t^2$ at every hidden layer | Lines 227–251 test the actual feature increment against its initial adjoint and obtain a positive partial sum of weight-acceleration energies. This directly controls features, rather than inferring feature motion from weight motion alone. |
| Nonlinear part of the first-layer increment has mean-square size at least $c_*t^4$ | Lines 280–312 preserve the exact integral and infimum over affine functions on the unit sphere of the training span. |
| One positive $c_*,t_*$, independent of width, with probability tending to one at each fixed $0<t\le t_*$ | Lines 172–174 define the required uniform small-time remainder; lines 202–207 obtain a deterministic cutoff before choosing time; lines 325–328 take the fixed-time compression limit and common smaller constants. |
| Legendre/Harmonic whole-sphere domains; Taylor's deterministic passive augmentation | Lines 329–332 retain at most four witnesses fixed before initialization, no supplied passive labels, and the replacement of $p$ by at most $p+4$. The factors $9$ and $3$ follow from $m+p\ge2$. |
| Unchanged storage orders and approximation promises | The transfer changes only Taylor's panel count. It does not assert a new endpoint gap, test-risk conclusion, or identification of compressed coordinates with dense neurons. |

All inherited assumptions remain used at their stated strength: physical gradient-flow time; mobilities $(n,1,\ldots,1,n)$; zero initial readout; Gaussian initialized blocks; fixed data, $m,d,L$ and activations, with $m,L\ge2$; fixed nonzero labels; positive final Gram gap and the existing small-label bound. The additional theorem still requires every activation to be nonaffine and $|x_a^\top x_b|<d$ for distinct training inputs. Together with $m\ge2$, the latter gives both $d\ge2$ and a training span of dimension at least two.

There is no added bounded-activation, zero-mean, label-sign, full-input-rank, or orthogonality hypothesis. Bounded first and second real derivatives follow from the already assumed holomorphic-strip bounds. Linear activation growth suffices throughout. In particular, the backward conditioning inverts only positive feature Grams $Q^{(\ell)}$, $\ell\ge1$, never the possibly singular input Gram $Q^{(0)}$.

## Why the deleted results are unnecessary

**The propagated forward-acceleration law.** The old initialization supplement constructed preactivation and feature accelerations at every layer by a third pass through the Gaussian matrices. The new theorem proof needs only the forward fields, the backward fields $P_a^{(\ell)},B_a^{(\ell)}$, the weight accelerations, and the joint first-layer weight/acceleration rows. A forward pass followed by a backward pass supplies these variables, with empirical quadratic-Wasserstein convergence. Each matrix is queried only once in each direction, so the one-sided reverse-conditioning formula suffices. The fresh Gaussian innovation has the advertised covariance and is independent of the lower-layer tuple in the limit; its finite-rank projection has vanishing RMS. The stronger old propagated row law is no longer invoked.

More concretely, put $k=2/m$ and use the new proof's energies $E_{1,n}=\|\ddot W^{(1)}(0)\|_F^2/n$, $E_{\ell,n}=\|\ddot W^{(\ell)}(0)\|_F^2$ for $\ell\ge2$. The initial adjoints are defined by $P_a^{(L)}=\sum_b y_bh_b^{(L)}(0)$, $B_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)}(0))\odot P_a^{(\ell)}$, and $P_a^{(\ell-1)}=W^{(\ell)}(0)^\top B_a^{(\ell)}$. Here $\Delta h$ and $\Delta W$ denote increments from time zero, and $\langle u,v\rangle_n=u^\top v/n$. Its actual-increment identity is

\[
\sum_a y_a\langle P_a^{(\ell)},\Delta h_a^{(\ell)}\rangle_n
=\frac{t^2}{2k^2}\sum_{j\le\ell}E_{j,n}+o_*(t^2).
\]

For a hidden layer, the learned-link pairing is exactly $k^{-2}\langle\ddot W^{(\ell)}(0),\Delta W^{(\ell)}\rangle_F$; the first layer has the additional factor $1/n$. The term with $W^{(\ell)}(0)\Delta h^{(\ell-1)}$ is exactly the lower adjoint pairing, and the remaining product is $O(t^4)$. The displayed identity therefore telescopes without a law for propagated feature accelerations. Cauchy–Schwarz converts its positive coefficient into the required actual feature displacement, since the finitely many initial $P$-field norms are bounded with probability tending to one.

**Initial norm uniform integrability and expectation limits.** The theorem makes probability statements and lower bounds, not claims about expectations of initial energies. Deterministic empirical row-law limits with convergent second moments are retained. They give both convergence in probability of the energies and the squared-coordinate-tail control needed in the multiplier estimate. Uniform integrability of these random norms across initialization, and the corresponding $L^1$ convergence, are stronger old technical conclusions that no longer enter the proof. Their deletion is harmless. Deleting the retained empirical second-moment convergence would not be harmless; the new source does retain and justify it.

**The full second-order kernel coefficient.** For the mobility-weighted training tangent kernel $K(t)$, a matrix expansion $K(t)=K(0)+t^2K_2+o_*(t^2)$ is unnecessary. The new proof retains the operator bound $K(t)-K(0)=O(t^2)$, and the adjoint identity gives precisely

\[
y^\top[K(t)-K(0)]y
=\frac{2t^2}{k^2}\sum_\ell E_{\ell,n}+o_*(t^2).
\]

The readout and hidden-kernel parts each contribute $t^2\sum_\ell E_{\ell,n}/k^2$. In the exact variation-of-constants formula, replacing the exponential by the identity costs $O(t^4)$, using the operator bound and bounded $K(0)$; replacing $y-f_n(s)$ by $y$ costs $O(t^4)$, using $f_n(s)=O(s)$. Integrating the displayed scalar coefficient gives $2/(3k)=m/3$, exactly the old cubic coefficient. No entrywise or operator limit for $K_2$ is needed.

## Probability, boundary cases, and completion

The crucial quantifier is preserved. For a prescribed error tolerance, deterministic empirical second-moment limits allow a deterministic tail cutoff whose failure probability tends to zero. Only after that cutoff is fixed does the proof choose a deterministic small time. Together with the fitting event, this yields the stated $o_*$ bounds, not merely a confidence-dependent time. Positive deterministic energy limits then give one small interval with probability tending to one for the dense internal conclusions. For compressed prediction gaps, the proof fixes each $t>0$ before taking width to infinity; it correctly avoids claiming a uniform relative comparison as $t\downarrow0$.

I checked singular $Q^{(0)}$, nonzero activation means, unbounded activation values, arbitrary nonzero label signs, $d=2$, and a training span of dimension two. The positive tensor-coefficient argument, backward covariance positivity, Schur-product energy bound, and first-layer nonlinear projection remain valid in these cases. The zero-label case is excluded by the inherited $Y>0$, and no division by a potentially zero label norm occurs within the admissible theorem.

Checks performed: complete source comparison, direct derivation of both adjoint and cubic coefficients, explicit tracking of norms and factors of $n$, probability-quantifier inspection, and input-hash verification. No numerical experiment is needed for these exact checks. No required correction was found. Only this report was written; no paper, code, book, or Git-index changes were made by this reviewer.

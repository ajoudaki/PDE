# Internal checks of the endpoint and trajectory lower-bound continuation

2026-10-04. Coordinator check and assembly record. These checks are internal
research reconstructions, not promotion reviews or external validation.
No numerical experiment was used.

## Frozen mathematical inputs

| File | SHA-256 |
|---|---|
| TANH_ENDPOINT_VARIABILITY_LOWER.md | 227a88cb199ea84a8f2ec8bfce1c7eb3589dd1be5d7bab0818f37e1c5c04ae67 |
| LINEAR_ENDPOINT_VARIABILITY_LOWER.md | 212841e1591ce11a632e0e68d2e7a1f39286ee41ec599d552ab550578dc8c66f |
| NONLINEAR_ENDPOINT_VARIABILITY_LOWER.md | f4e9ab753a91c928b850ea9aece4810b6f12407ebb88b28bec8d80152f39838c |
| ONSET_TO_TRAJECTORY_LOWER.md | 34db6bf196433afd1c042832063f9fcc5c578a8aa389ec891ba3312dd345b5cd |
| ENDPOINT_LOWER_RESULT.md | 14e97aabaaebdcacb41e927674e7344921a2f2a6afb9305197c9fddca23982f7 |
| GENERAL_EXPLICIT_FITTING.md | 5c6f12b78847a2b2874c5bc82eb1cea5f4929ee071b114d09b098397c5e2b8d6 |
| EARLY_VARIABILITY_AND_STORAGE.md | 54744f6e58fe0f03f0349041100664dbd55c1335e5edc80d574979b128d960ea |
| UNBOUNDED_COMPRESSOR_BRIDGE.md | 63b0613ca4c028f780e3342fb3ddf21efc739fa9257f903691ee967276f8cc08 |
| SIMPLE_CONSTANTS_SOURCE_CHECK.md | cc1096f354e38c97b5cab8fe2000323ca21811c9801a4a33a4c5dbaf0a08938a |

The coordinator read all four new proof notes and reconstructed their
nontrivial arguments. The real fitting proof was reread completely.
The source's exact complex rectangle/RMS interface and the source power
envelopes were checked against the onset bridge. The previously checked
insertion proof underlying that source event was not independently rebuilt
in this continuation; the onset result retains that inherited dependency.
The two principal endpoint results have no insertion/source-event input.

## 1. Two-tanh endpoint: checks and corrections

The author is the coordinator. A separate reconstruction by
merge_general_dense is recorded in
[TANH_ENDPOINT_VARIABILITY_LOWER_CHECK.md](TANH_ENDPOINT_VARIABILITY_LOWER_CHECK.md).
The independent identity--tanh derivation also supplied a bounded check
of the distinct-product coefficient mechanism.

The checks covered:

- Canonical factors in all three block equations, with zero readout and
  unchanged physical time.
- Exact closure of training on its input span, and independence of unused
  Gaussian read-in columns from every active parameter and its endpoint.
- Application of the fitting event in the reduced input dimension.
  Applying the original full-dimensional sphere event would invalidate
  the conditional Gaussian assertion; the proof explicitly avoids this.
- Exact three-coordinate integration identity, symmetric tilted laws,
  matching of the first three moments in the Gaussian replacement, and
  bounded seventh derivative sufficient for the coefficient remainder.
- Uniform row coefficient error of order \(\log(en)/n\), hence matrix
  Frobenius error of order \(\log(en)/\sqrt n\), despite the cubic number
  of projection columns.
- The elementary symmetric-polynomial identity for the distinct cubic
  tensor Gram. Its off-diagonal absolute row sums tend to zero, while its
  diagonal is bounded below uniformly.
- Strict negative third-response coefficient for tanh, with the actual
  shared argument scale retained in the separated-interval estimate.
- Stability of the covariance gap under the actual Frobenius displacement
  of the trained mixer, without assuming trained rows remain Gaussian.
- Final training Gram upper comparison \(G_\infty\preceq2Q\) and the
  forced readout energy
  \(\|w_\infty\|^2/n\ge y^\top Q^{-1}y/2\).
- Gaussian second/fourth moment bounds and the probability argument,
  conditional on active states rather than on unused query randomness.

Three presentation corrections were made before the frozen version:
the orthonormal cubic product was written explicitly as
\(\sigma^{-3}\prod_{j\in J}H_j\); independence was stated for the active
trained state rather than the entire first-weight matrix; and the Stein
identity was correctly described as two integrations by parts. Inline
math delimiters were repaired and checked. None of these changes altered
the proved endpoint scale.

Outcome: the stated fixed-probability endpoint lower bound reconstructs.
Constants are deliberately loose. The proof covers correlated data with
a proper input span and positive initialized feature gap, not every
full-span nonlinear dataset.

## 2. Deep-linear endpoint

The author is merge_general_dense. A separate complete reconstruction by
merge_unbounded_compressor is retained in
[LINEAR_ENDPOINT_VARIABILITY_LOWER_CHECK.md](LINEAR_ENDPOINT_VARIABILITY_LOWER_CHECK.md).
The coordinator also checked the candidate against the full fitting source.

Interpolation fixes the active coefficient to \(V(V^\top V)^{-1}y\).
The remaining coefficient is exactly the unused Gaussian matrix
transposed against the active effective readout. Its conditional law is
Gaussian, not merely asymptotically Gaussian. The source feature bound
for the identity first layer gives the stronger operator cap
\(\|A|_S\|_{\rm op}\le2\sqrt n\); this is the cap used in the lower bound.
Every threshold specialization, chi-square moment, Chernoff parameter and
probability allocation was checked. The resulting full-sphere factor is
\(\sqrt{d-m}\); it must not be included in a single fixed-query variance.

Outcome: PASS for the exact law and all stated probability bounds. The
matching \(Y\sqrt{m(d-m)/(\gamma n)}\) formula requires labels in the
weakest covariance eigenspace. With \(m=d\), endpoint variability is
exactly zero, as the candidate states.

## 3. Identity--tanh endpoint baseline

The author is merge_general_legendre. The coordinator checked the complete
note, including the finite row event, Hermite coefficient, and constants.
The coefficient lower bound uses the correctly ordered extremes
\(\operatorname{sech}^2(11/20)-\operatorname{sech}^2(27/20)>1/2\).
The cubic correlation Gram row sum is at most
\(64\log(en)^{3/2}/\sqrt n\), less than \(1/2\) at the displayed width
and decreasing thereafter. The trained perturbation allowance
\(1/340<1/(200\sqrt2)\) leaves the asserted covariance gap.
The fourth-moment and label-energy steps agree with the tanh proof.
Two missing TeX command backslashes in the conditioning notation of
equation (4) were repaired before the frozen hash above; its mathematical
conditioning and probability inequality are unchanged.

Outcome: the endpoint result reconstructs under the dense fitter's larger
label cap. This is a separate simpler proof; the first hidden activation
is identity, and it is never advertised as two nonlinear activations.

## 4. Onset-to-actual-prediction bridge

The author is merge_unbounded_compressor. The coordinator checked the full
new argument and its exact inherited interfaces:

1. The joint initialized Gram CLT in the earlier note is a conditional
   iid-row CLT plus the differentiated Gaussian covariance map. The onset
   derivative is exactly \(2\kappa_n^\top y/m\). Two independent copies
   give the factor eight in the variance.
2. The source rectangle has the stated radius
   \(a\lambda/(1024Y^2U\sqrt{\log(en)})\). Its RMS bounds imply the
   width-independent complex predictor envelope used in the bridge.
   The smaller ellipse lies strictly inside that rectangle.
3. Chebyshev coefficient decay, the differentiated tail sum, and the
   endpoint Lagrange-polynomial derivative bound give the stated
   real-time-supremum inequality. The latter is the missing mathematical
   step that a bare onset derivative did not supply.
4. Taking degree proportional to \(\log(en)\) yields the factor
   \(\log(en)^{-5/2}\), including the time-radius factor. The
   \(n^{-2}\) remainder is negligible at the claimed scale.
5. The source event need not be independent of onset fluctuations:
   subtracting its vanishing failure probability is enough.
6. On orthogonal data with odd activations, off-diagonal innovations
   have covariance \(q_\ell^2 I\) and propagate with multiplier
   \((\mathbb E\phi_\ell')^2\). The displayed onset variance,
   all-label nondegeneracy and \(\gamma Y/\sqrt m\) lower coefficient
   follow with the stated constants.

Outcome: PASS for the bridge using the inherited source theorem. It is
near-root, has an unquantified source/CLT confidence threshold, keeps all
problem parameters fixed in its width limit, and makes no endpoint claim.

## 5. Synthesis and matching upper bound

The coordinator derived the fixed-query matching upper bound in the
synthesis. Both merge_general_dense and merge_general_legendre checked
it separately. Conditional second moment is at most
\(648Y^2m/(\gamma n)\). Threshold
\(36Y\sqrt{m/(\delta\gamma n)}\) gives conditional failure \(\delta/2\);
two reduced fitting failures of \(\delta/4\) each complete the assertion.
This is not a sphere upper bound.

The synthesis was also read in full by merge_general_legendre against all
four proof notes. Its scope audit found no substantive error. The
weakest-label-direction condition was repeated immediately before the
two-sided linear formula to prevent accidental generalization.
Both-tanh one-datum hidden accelerations were differentiated directly;
the factors \(4y^2\), first-layer derivative and factor \(1/n\) in the
mixer acceleration are correct.

The lower bounds imply lower bounds for the all-time norm by inclusion.
An endpoint upper bound does not imply an all-time upper bound. No claim
of universal nonlinear dimension matching, necessary exponential
sample dependence, or a storage lower bound against arbitrary encodings
is made.

## Validation record

Files were inspected completely as described above, with individual
reads used to repair tool-output truncation. SHA-256 hashes bind the
checked versions. A Python text check found no control characters and,
after delimiter repair, balanced inline and display math delimiters.
The scientific checks are the mathematical reconstructions in this file
and the two separate reports, not the formatting check.

No numerical network training, manuscript edit, maintained-code edit,
repository reset or Git-index mutation was performed.

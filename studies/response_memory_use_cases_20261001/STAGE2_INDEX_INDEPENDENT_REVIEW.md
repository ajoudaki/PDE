# Independent internal review of stage2 shared indexing

Reviewed 2026-10-02. This is an isolated internal research review, not a
promotion review. The main algebraic distinction and the reported failure of
the frozen practical criterion are supported. I found one minor mathematical
presentation/initialization defect, described below; it does not invalidate
those findings. No major or critical defect was found within the assigned
scope.

## Scope and independence

I read the ten files named by `STAGE2_INDEX_FREEZE.json`, the complete model
reconciliation and input-field derivation, `input_field.py`, the relevant
network/Flow/LowRankFlow implementation in `baseline_compact_flow.py`, the
complete stage2 data protocol and preparation implementation, the model and
learning-speed construction in `paper/main.tex`, and `paper/results.tex`.
Only the finite-width model and moment definitions are used from the paper;
none of its approximation theorems is imported. The canonical-notation skill,
its neural-response-memory reference, and the rigorous-math skill governed
the review.

I inspected the assigned pilot, confirmation, adaptation, refinement, oracle,
analysis and check artifacts and the retained stage2 data sources. I did not
read another study, another review, coordination outcomes, study history or
the archived book. The author's verdict and existing checks were treated as
claims to audit. A supervisor message during finalization reiterated the
constant-prefix condition and the sign-flip witness discussed below; that
witness is verified explicitly here and supplies no empirical evidence.

The only writes are this report, `stage2_index_review.py`, and
`data/generated/response_memory_use_cases_20261001/stage2_index_review01/`.
There were no Git mutations or edits to the frozen inputs.

## Exact claims

The normalization agrees with the declared network. For API input rows
\(u=x/\sqrt d\), the forward pass is
\(h^{(1)}=\tanh(W^{(1)}u)\),
\(h^{(2)}=\tanh(W^{(2)}h^{(1)})\), and
\(f=w^\top h^{(2)}/n\). For the unhalved loss
\(\mathcal L=\mathbb E[(f-y)^2]\), define \(r=f-y\) and
\(\delta=w\odot(1-h^{(2)}\odot h^{(2)})\). Then
\(G=-2\mathbb E[r\delta h^{(1)\top}]/n\) is exactly the negative
hidden-matrix gradient. The outer velocities use mobilities \(n\), as
specified. The code includes the residual in `_loss_fields()` backward
arrays; it must not be multiplied by the residual again.

For positive selected eigenvalues \(\Lambda\) of
\(C_h=\mathbb E[hh^\top]\), with \(h=h^{(1)}\) and orthonormal
eigenvectors \(V\), substituting
\(\psi=\Lambda^{-1/2}V^\top h\) gives

\[
\mathbb E[r\delta\psi^\top]\mathbb E[h\psi^\top]^\top
=\mathbb E[r\delta h^\top]V\Lambda^{-1}V^\top C_h
=\mathbb E[r\delta h^\top]VV^\top.
\]

The projected velocity and loss derivative \(-\|GV\|_F^2\) are therefore
correct. This statement applies to the instantaneous current-feature
dictionary, not automatically to the history-based learner's velocity.
The theory preserves that distinction and does not infer a fixed-rank
integrated correction from changing instantaneous subspaces.

The retrospective information obstruction is valid for the stated encoder.
If a new basis function \(\eta\) has nonzero
\(v=(I-P_S)\eta\), where \(P_S\) projects onto the old span, the histories
zero and \(v\) have identical old coefficients but new coefficients differing
by \(\langle v,\eta\rangle=\|v\|^2\). No decoder of just those old
coefficients can distinguish them. Conversely, span containment permits an
explicit linear change of coordinates. The differentiated connection term
has the correct sign and index orientation, and its missing component is
exactly the pairing with the history outside the old span. This does not
prove an obstruction for arbitrary encoders or for all reachable neural
histories; the report appropriately avoids those stronger conclusions.

For write-time indexing, fix a terminal clock value \(\tau\). Let
\(p_j(s)=P_j(2s-1)\) be shifted Legendre polynomials, where \(P_j\) is the
ordinary Legendre polynomial, and let
\(u_{c,j}(x,\xi)=\psi_c(x,\xi)p_j(\xi/\tau)\). Orthonormality in input
space at almost every \(\xi\) gives
\(\langle u_{c,j},u_{d,k}\rangle
=\tau\delta_{cd}\delta_{jk}/(2j+1)\). Consequently the product-tail
identity follows by expanding both histories into their orthogonal
projections and complements. Both cross terms vanish coordinatewise; the
Frobenius norm of the remaining interaction is bounded by the product of
the two omitted-history \(L^2\) norms. This is an exact same-history
statement, with no small-tail, loss-descent or trajectory conclusion.

I independently tested the instantaneous projection identity, the
indistinguishable-history construction, and joint orthogonality/product-tail
cancellation for a dictionary whose span actually moves, rather than only
rotates within a fixed span. The maximum error was
\(9.77\times10^{-15}\). The numerical product-tail bound also held.

## Minor defect: make the prefix assumptions explicit

**Severity: minor; does not invalidate the main findings.**
`STAGE2_INDEX_THEORY.md:108` allows arbitrary measurable write-time
dictionaries, but lines 123–124 then prescribe only a zeroth forward moment
at initialization. This initialization is correct when the dictionary is
constant on the artificial unit prefix (or under a sufficient equivalent
condition on the projected prefix history). It is not correct for every
measurable dictionary allowed by the preceding sentence. In general, the
initial forward moments must be their defining integrals over that prefix.

The rotating-basis example also takes \(h=b=e_1\) over the whole history,
whereas the earlier setup sets \(b=0\) on the prefix. A full turn over the
whole interval additionally changes the prefix dictionary. It is a valid
counterexample for unrestricted square-integrable histories, but it should
be labeled that way or replaced when illustrating the initialized learner.
Also fix the terminal clock value in advance when defining the rotation;
the historical write-time dictionary cannot depend retrospectively on the
current upper limit.

Here is a fully prefix-compatible replacement. Let \(e_1,e_2\) be
orthonormal input functions, \(\tau=2\), and \(q=1\). Set \(h=e_1\)
throughout; set \(b=0\) on \([0,1]\) and \(b=e_1\) on \((1,2]\).
Use dictionary \((e_1,e_2)\) on the prefix and
\((-e_1,-e_2)\) afterward. The span never changes. The forward zeroth
coefficient vector is \((1,0)+(-1,0)=(0,0)\), and the backward vector is
\((-1,0)\). The paired reconstruction is zero, whereas

\[
\int_0^2\mathbb E[bh],d\xi=1.
\]

Keeping the initial dictionary throughout instead gives forward vector
\((2,0)\), backward vector \((1,0)\), and reconstruction one. This example
uses precisely the measurable, piecewise-constant dictionary class admitted
by the theorem and the initialized constant prefix. It is still a history
representation example, not a claim of a realized neural trajectory.

The saved independent quadrature check additionally verifies cancellation
for a continuously rotating dictionary with a zero backward prefix; that
check concerns the general integral projection, not the stronger
constant-prefix initialization. The implemented campaign uses a constant
initial dictionary until time 64, so the identified omission does not alter
any campaign fit.

## Raw empirical audit and reproduction

All ten frozen source hashes match. The source snapshots in all four fit
stages match their manifests and current frozen sources. All 99 per-fit
configuration/result records agree with their aggregate files. Every saved
fit has the four declared checkpoints, reports completion and a finite
final state, and selects the validation-minimizing checkpoint. I recomputed
every saved test RMSE from its raw predictions and targets; the maximum
difference was \(5.20\times10^{-8}\), attributable to float32 versus
float64 reduction.

All three stored datasets were independently reconstructed from the retained
raw archive rows, including training-only means/scales, clipping, appended
constant coordinate, unit normalization, labels, and housing target
transformation. Every reconstructed input and target matched exactly.
The source and NPZ hashes match their manifest. Index uniqueness and required
split separation passed, including the HAR subject separation and the four
prescribed validation subjects. No source download was required.

Pilot selection recomputes exactly from validation losses. The selected
fields' time-64 drift values are 0.330567, 0.387230 and 0.107717 for Fashion,
HAR and housing, so the two-domain adaptation trigger holds. Independent
recomputation of paired ratios gives:

| Method | Fashion ratio / wins | HAR ratio / wins | Housing ratio / wins |
|---|---:|---:|---:|
| Fixed field | 0.988265 / 3 | 1.378856 / 0 | 1.007905 / 1 |
| Retrospective overlap | 0.987737 / 4 | 1.370972 / 0 | 1.006486 / 1 |
| Write-time replacement | 0.987737 / 4 | 1.367307 / 0 | 1.006373 / 1 |

Each ratio is the median of four paired test-RMSE ratios to the frozen tuned
factor control; wins are strict improvements out of four. No candidate
achieves the required five-percent gain on even one domain. The negative
practical conclusion is therefore supported without interpreting marginal
improvements as success. Both adaptive Fashion branches select the
pre-refresh checkpoint for every seed; their equal median is not evidence
for a beneficial refresh. The fixed Fashion seed 203 selects time 128,
which explains why the fixed and adaptive paired ratios/win counts differ
despite identical table medians.

All six refinement discrepancies satisfy both prescribed bounds: one percent
of label RMS and one-third of the seed-201 field/factor gap. Their maximum
selected test-RMSE change is \(1.1594\times10^{-5}\). No positive claim is
supported by the small unrefined adaptive differences, and the report does
not make one.

I recomputed all oracle target RMSEs and all pairwise prediction RMS
differences from the saved float64 prediction arrays. They match their
records within \(10^{-14}\). The large Fashion functional discrepancy is
real in those saved frozen-state interventions; it neither demonstrates an
oracle-trained learner nor shows that restoring history improves loss.
The source implementation correctly holds outer parameters fixed during
the intervention and excludes observer state from learner updates.

One fresh full Fashion seed-201 field replay used the exact confirmation
configuration \(C=8,q=3\), step \(1/32\), and horizon 128 on GPU0. Every
checkpoint test prediction matched the saved array **bit for bit**. The
selected time was 64 and test RMSE was 0.6675752997398376. The recorded fit
time was 1.2999 seconds, within the assigned two-fit/five-GPU-minute cap;
only one full fit was run. Environment: RTX 3090, PyTorch 2.9.0+cu130,
NumPy 1.26.4, one CPU thread, TF32 disabled.

The replay's initial float32 dictionary Gram error was
\(1.20\times10^{-7}\). A post-replay no-training refresh had the same
maximum Gram error, and evaluating its stored PCA/rotation function on the
training inputs agreed with its cached basis within
\(5.97\times10^{-7}\). Source inspection verifies that the in-place basis
and moment copies preserve the tensor addresses used by captured updates;
write-time replacement leaves old moments intact, while retrospective
replacement multiplies them by the correctly oriented overlap.

## State accounting and comparison limits

The counted evolving field state is
\(n(d+1)+2nCq+1\). Rank-24 factors have
\(n(d+1)+2n\cdot24\); projected descent has
\(n(d+1)+n\cdot24\), with its right basis fixed. The initialized dense
hidden matrix remains stored in each correction method. The field's
additional first-layer copy, PCA transform and cached training basis are
also present in the records. I checked the moving-state counts in every
fit and the field dictionary counts against the dimensions.

For Fashion, the field retains 232841 scalars when moving state, base,
dictionary and cached basis are summed, compared with 116992 for dense and
123136 for factors. For housing those totals are 34185, 17664 and 23808.
These are the declared model/dictionary accounting categories, not total
CUDA allocations or graph workspaces. The report correctly makes no total
memory or speed advantage claim. The in-function campaign time recomputes
as 72.9941 seconds; setup ordering, diagnostics, and uncounted interpreter
startup make it unsuitable as a general hardware benchmark.

The factor control has the declared random initialization, matched rank
bound, canonical outer mobilities, and validation-tuned factor mobility.
This is a defensible frozen comparison, not equality of optimization
geometry or effective numerical rank. The current-feature PCA identity
does not turn the fixed initial dictionary into a continuously adaptive
projected-gradient method. That potential conflation is avoided in the
theory and report.

The empirical result remains specific to these domains, fixed data splits,
four confirmation initializations, ranks, orders and horizons. A failed
preregistered gate is not a statistical impossibility theorem or proof that
all adaptive indices are ineffective. Historical state is not saved for
all 99 fits, so their final-state finiteness is supported by recorded checks
and source inspection, with a fresh replay for one fit; it was not
independently replayed for every model. Original float64 oracle histories
were not regenerated under this review budget. These limits are compatible
with the report's restrained conclusions.

## Evidence identity and commands

`stage2_index_review.py` contains the independent audit and numerical checks.
The complete input/evidence SHA256 inventory is
`stage2_index_review01/source_evidence_hashes.json`; it records all consumed
raw files, fit records, prediction arrays, source snapshots and analysis
artifacts. Key hashes are:

| Artifact | SHA256 |
|---|---|
| Frozen ten-file inventory | `5a2e6035a209cdab338fb1187ad54eb22247b78c67f442a25e452fa459c50c3b` |
| Frozen theory | `985c2cdb31b31429b509e46ef6c54ccd319e319f9f96d9817d84001824033532` |
| Frozen author report | `2a50248bcf1c68840b9e18aeb98a87254f5acc009657417316629f648484b075` |
| Frozen experiment implementation | `5b8181551b6793c5c6302caf25d8ebfa2e48c567a16031ec6e8816351aab363f` |
| Independent review implementation | `2b49e80067afb9f7fb8cbc396b74adf2685113d8357aede2fc22f91290258da6` |
| Complete source/evidence inventory | `590a250603421f63b64a885a534ade7376cc1cbaa1a7334bd286743dee7583d6` |
| Raw audit result | `a8d5d83a09bb72d050decc15c1e0a167f02a944d11fd5bc127b27a86887078cb` |
| Independent algebra result | `12a12373257a3d7d6526e34bf0e3e0c560804b19bdef8e6e9b93f131b0ee961a` |
| Fresh replay result | `5820862a291c150234271eacb0622c2d821ef621b7cae74a7b6d703506d2d1c1` |

From `/home/amir/Codes/PDE`, use a fresh output directory for the first
command and that same directory for the replay:

```bash
/home/amir/miniconda3/bin/python -B studies/response_memory_use_cases_20261001/stage2_index_review.py --out FRESH_REVIEW_DIRECTORY
/home/amir/miniconda3/bin/python -B studies/response_memory_use_cases_20261001/stage2_index_review.py --out FRESH_REVIEW_DIRECTORY --replay
```

The review supports retention of the exact representation distinction and
the bounded negative empirical finding as internally reviewed study
results, with the prefix clarification above. It supplies no promotion
approval, broad novelty verdict, or adaptive-training approximation theorem.

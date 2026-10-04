# Exact temporal rearrangement: fixed-support results

The preregistered cross-domain coordination claim fails. Exact time reversal
preserves both separate empirical histories but does not systematically damage
held-out prediction: it slightly improves Fashion-MNIST and HAR, while its
Housing damage is far below the registered threshold and below the strong
Gram-preserving control. Ordinary gradient controls remain competitive or better.
This is adverse evidence for a useful necessity-of-chronology interpretation,
not evidence that the representation lacks chronological information.

There is a positive exact tool result with a different scope: reversal is diagonal
in Legendre coordinates, so an odd-mode memory can construct the intervention
without storing every training step. The algebra, complete empirical history
permutation, and product-tail error bound are in STAGE2_COORD_THEORY.md. These
identities do not guarantee any favorable endpoint or optimizer behavior.

## Fixed contract and execution

All settings and thresholds were frozen in STAGE2_COORD_PROTOCOL.md. There are
three datasets with unchanged labels,512 training rows and1024 held-out test rows,
canonical two-layer tanh dense training, Gaussian initialization, zero readout,
width256, horizon32 and Euler step1/16. Pilot seed3101 is excluded from the table.
The four new confirmation seeds are3201–3204. All five equal-budget T4 continuation
arms were executed at every confirmation endpoint. Half-step seed3201 and
width512 seed3202 repeats were executed on every domain, then all15 prescribed
causal blockwise arms were executed at fresh seed3301. No pilot-driven changes
of data, labels, horizon, width, step, intervention, or thresholds occurred.

The root prepared and hash-verified datasets under stage2_data01: Fashion-MNIST
T-shirt/top versus shirt; bounded California housing regression; HAR moving versus
stationary using engineered features and disjoint test subjects. Preprocessing
uses all1024 root-designated training inputs while this route trains on their
first512. This transductive preprocessing within the designated training pool is
explicit; no validation/test labels or inputs fitted its normalizer. There is no
claim about full Fashion-MNIST, raw-price regression, or raw-sensor learning.

## Fresh confirmation

Entries below are median percentage changes in held-out MSE relative to the same
untouched endpoint; negative means improvement. "Sign" is the within-seed median
of five edits preserving both edit Grams, then the median across seeds. The
gradient/sign/isotropic controls have the reversal edit's exact norm; sign controls additionally preserve
its left/right singular axes and spectrum.

| Domain | Full reversal | q1 replacement | Sign control | Gradient descent | Gradient ascent |
|---|---:|---:|---:|---:|---:|
| Fashion | -0.498% | -0.135% | +0.524% | +0.407% | -0.284% |
| Housing | +0.238% | +0.041% | +0.445% | -0.613% | +0.809% |
| HAR | -3.312% | -4.698% | +14.783% | -14.819% | +19.089% |

Reversal improves Fashion and HAR in4/4 seeds each, and damages Housing in4/4.
No domain passes the registered >=10% damage requirement. The registered
reversal excess over sign controls is negative in all three domains. Thus even
Housing fails the directional-control gate. The exact input history still
carries chronological information: its rearranged weights and predictions differ.
The failed claim concerns positive task-relevant necessity of that information.

The stronger controls explain why isotropic perturbation alone would be weak:
randomized singular directions change held-out MSE by only about0.001–0.01%,
while sign controls retaining learned axes can cause substantial HAR damage.
That comparison identifies sensitivity along learned directions, not a unique
temporal mechanism. Mean-only q1 is again a strong simpler alternative on HAR.

Continuation does not yield broad superiority. After the same T4 further dense
training, reversal changes MSE relative to untouched continuation by -0.281%,
-0.164%, and -6.525% on Fashion, Housing, HAR. The corresponding gradient-descent
control changes are +0.299%, -0.658%, and -12.835%. In particular, the meaningful
HAR improvement remains smaller than an ordinary norm-matched gradient edit.

The fresh single-seed causal block intervention has negligible effects on Fashion
and Housing (reversal +0.031%,+0.028%). On HAR reversal improves2.416%, the exact
Gram control improves2.338%, and the ordinary gradient edit improves3.889%.
This reachable changed optimizer supplies no distinct temporal-coordination win.
Only one seed/domain was registered for this feasibility stress; it is not a
four-seed confirmation or an optimizer-superiority claim.

## Compressed reversal and valid negative evidence

The supervisor added exact reflection reconstruction after the fixed confirmation
ran, without changing any training arm or running extra solves. Original pilot/
confirmation coefficients allow q4/q8 reconstruction; subsequent numerical/width
repeats also retain q16/q32. No retrospective q16/q32 coefficients are invented.
The old producer is preserved byte-for-byte as stage2_coord_experiment_v1.py.

| Four-seed domain | Largest q4 relative edit error | Largest q8 relative edit error | Largest q8 test prediction RMS error |
|---|---:|---:|---:|
| Fashion | .04535 | .002094 | .0000371 |
| Housing | .05241 | .001129 | .0000201 |
| HAR | .03246 | .02403 | .0005879 |

q1's reversal edit is exactly zero because it contains no odd Legendre mode.
This is a statement about reversing the represented history; it differs from
replacing the whole recorded increment by its mean-only approximation.
Higher-order accuracy is not asserted monotone. Across the six numerical/width
repeats, the largest q16 relative reversal-edit error is0.000346, and largest
q32 error is0.00001891. Every tested odd-tail product bound holds. These are
observer accuracy checks; no autonomous response-memory feedback is used.

The odd coefficient count is2mn floor(q/2), while full paired histories use2mnN.
In this campaign m=512; a q8 odd-memory set can exceed a single n-by-n matrix.
The demonstrated compression is of time histories, not necessarily of total
training state or of one accumulated dense edit. Timings include diagnostic
histories and explicit dense edits and do not establish a practical speedup.

## Numerical validity and source checks

The models are nonlazy: first-layer relative motion is0.333–0.522 in fresh
confirmations, above the0.03 gate; tanh nonlinearity gates also pass. Exact
permutation/Gram invariants have maximal relative error3.82e-13, below1e-9.
The one-step source/autograd mobility oracle is accurate to2.2e-16. Direct
accumulated-update parity, zero-residual handling, independent Legendre interval
quadrature, exhaustive4! permutation mean/variance, reflected-coefficient parity,
and reflected odd-tail bound tests pass. These checks cover the implementation
producer, not just a re-expression of its outputs.

At half the step, held-out baseline prediction RMS changes are0.000341,
0.0000436,0.000120 for Fashion,Housing,HAR. Each primary signed effect is more
than twice its refinement change; all signs and conclusions persist. Width512
stress also preserves the three signs. These are finite numerical checks, not
width-limit or all-time theorems. One-step exactness concerns the Euler map;
continuous-time approximation is supported only by the declared refinement.

All96 planned solves completed (counting every short continuation separately).
Total producer wall time is168.565seconds across GPU processes, including archive
writing. The GPU1 analysis used9.95seconds and no new solves. Small CPU checks
used0.156seconds initially and0.119seconds after reflection strengthening,
excluding interpreter startup. These fit comfortably inside the100fit/75GPUminute
route ceiling. Two final width/causal processes briefly overlapped on our
exclusively assigned GPU1; their process wall times are both counted. No timing
comparison or peak-memory claim is based on this execution.

## Evidence and reproduction

Frozen inputs and SHA256s are in each producer manifest. Exact source snapshots
and complete outputs are in stage2_coord_pilot01, stage2_coord_confirm01,
stage2_coord_refine01, stage2_coord_width01, and stage2_coord_causal01 under this
study's generated namespace. Each manifest includes unchanged data hashes,
precision, device, thread settings, command, source hashes and UTC start. Every
saved NPZ is hashed by its completion record. Summary/input hashes are in
stage2_coord_analysis01/summary.json; small-oracle reports are in
stage2_coord_checks01 and stage2_coord_checks02. Source/analysis remain flat in
this study. Independent review is pending; these are author-checked results.

From the repository root, use the commands in the exact saved manifests and a
fresh output path. The current source adds reflection diagnostics only; use the
preserved V1 producer for byte-identical pilot/confirmation reproduction. The
current analyzer reconstructs q4/q8 edits directly from the old saved coefficients
and verifies the larger retained mode sets on subsequent runs. A full report
must retain this failed registered claim even if a later support-shift experiment
finds a different, restricted positive effect.

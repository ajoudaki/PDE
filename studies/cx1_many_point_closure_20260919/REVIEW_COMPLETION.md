# C-X1 completion and acceptance record

Date: 2026-09-19. **C-X1 is resolved as an independently reviewed study.**
Both fresh complete scientific reviews accept all conclusions of THEOREM.md;
the separate integration review passes its assigned scope. There is no
remaining required scientific correction. This is not book/code promotion,
formal proof-assistant verification, or a wider research-program acceptance.

## Result and exact scope

For every separately fixed `1 <= m <= d`, arbitrary binary labels, equal
training weights and unit input directions in the explicit positive neighborhood
of distinct axes, the exact two-tanh-hidden-layer model has its canonical
strong population flow through `T=5m`. It retains the full first row, actual
Gaussian action and adjoint, initialized stored variances `(1,1/n,1/n^2)`,
mobilities `(n,1,n)` and unhalved mean loss. Its training loss at that horizon
is below `9/64`, with positive paired activation motion in both layers at a
specified earlier time and positive visited-law nonaffinity there.

Actual finite GF and simultaneous raw GD converge to this flow in the stated
whole-sphere/time prediction and fixed typed joint-observation senses. The
raw-GD condition proved by the fixed-proxy bridge is `eta_n -> 0`; the finite
random readout is retained. The complete current hierarchy is determining,
and the explicit autonomous dense closure converges in the separately stated
numerical and dictionary-order limits. Initialization uses no trained trajectory.
The closure state size is fixed during time evolution.

The radius is positive but extremely conservative and not numerically evaluated.
Dimensions and data are fixed before limits. Equal weights and binary labels
remain part of the learning theorem. There is no growing-m/d result, order
rate, automatic accuracy selector, arbitrary simultaneous diagonal, practical
cost-to-accuracy claim, model-superiority theorem or unseen-risk assertion.
The operational nonorthogonal example is not certified inside the radius.
For `m=d=1`, the discrete sphere has no nontrivial small angular perturbation.

## Frozen review edition and complete reviews

The complete candidate was committed as
`07e627a7b5e6254c2a033b7273bb3649473b50e1`, following scoped commits
`60ba365` and `4c4bef5`. The 30 original scientific inputs are frozen by
REVIEW_INPUTS_R1.json, SHA256:

`55a69888bfd1a234d01d44012cc33c6820ef9b54636aa459c7c0aa151fe38051`.

REVIEW_DEPENDENCY_SUPPLEMENT_R1.json adds three unchanged eager package imports:
`pde/__init__.py`, `finite_network.py` and `gaussian_moments.py`. Its SHA256 is

`14602d8f0bc03cc4aa4544a5756f8a14432134446972de068b7ffa78dd5fa21b`.

The supplement was supplied to all three reviewers as complete additional
inputs. It did not change the candidate. The supervisor read all three final
reports in full and verified all 33 frozen source hashes after completion.
No theorem or executable input changed while these reviews ran or afterward.
Pre-review status sentences in the frozen units are historical metadata,
superseded by this record and the current README.

| Report | Complete scope and verdict |
| --- | --- |
| SCIENTIFIC_REVIEW_R1_A.md | ACCEPT for all five theorem conclusions, all five proof units, necessary complete maintained mathematical/runtime dependencies, implementation and all numerical limits. No required correction. |
| SCIENTIFIC_REVIEW_R1_B.md | PASS for the same complete scientific contract and necessary dependencies, with independent source/clock/capture and numerical-interface checks. No required correction. |
| INTEGRATION_REVIEW_R1.md | PASS for source/interface correspondence and the five prescribed operational reproductions. Explicitly not a mathematical theorem acceptance or promotion review. |

The two mathematical reviewers started in fresh isolated contexts with only
the neutral assignment, complete frozen candidates, explicit dependencies,
allowed generated evidence and required skills. They did not receive study
history, earlier verdicts, each other's findings or author conclusions.
Their complete coverage and limits are stated in their own reports. The
earlier conditional implementation audit is preserved but is not counted as
either complete acceptance. Its recursion-ceiling objection was corrected
before the fresh frozen edition; both complete reviews include the repair.

FINAL_ACCEPTANCE_HASHES.json records exact hashes of the manifests, all frozen
inputs, reports, independently reproducible check source and final evidence.

## Independent validation and reproduction

- Review A ran all seven semantic tests once: 7 passes, no errors/failures,
  14.80 seconds, within 120 seconds and 512 MiB. Evidence is in
  `data/generated/cx1_many_point_closure_20260919/review_r1_a/`.
- Review B independently reran the exact rational certificate and checked
  all 43 moving-coordinate gradients on a supplied state, the energy identity
  and actual weighted adjunction. Maximum discrepancies were respectively
  `1.62e-10`, `4.61e-11` and `5.21e-18`; all declared checks passed in
  3.253 seconds under 60 seconds/512 MiB. Its permanent reproduction source
  is review_r1_b_independent_checks.py; outputs remain in the separate
  `review_r1_b/` generated directory. The source is byte-identical to the
  preserved scratch version; relocating it required no scientific rerun.
- The integration reviewer reproduced all five predeclared operational runs
  once in `integration_r1_operational/`: 15.994 seconds, peak resident memory
  41,588 KiB. Every numerical loss, paired RMS and passive prediction matched
  the baseline bitwise. All five checkpoint and five observation-file hashes
  matched. Every run retained its state dimensions and exact own-state restart.
- The final-source fresh-working-directory initialization in `standalone_02/`
  passed in 0.134 seconds. It loaded only this study's solver and maintained
  code, without a historical array or trajectory. All ten loaded project
  source hashes match the combined frozen manifests. The earlier standalone
  check predates the iterator repair and is retained as earlier evidence only.

The supervisor independently rechecked both manifests, the baseline's ten
output hashes, the reproduced ten output hashes, all loaded standalone
sources and the independent-check source's byte identity. No neural training
experiment or additional trajectory search was run during final review.

Reproduce the semantic suite from the repository root, using a fresh output
directory and the original caps:

```sh
CX1_CLOSURE_CHECK_OUTPUT=data/generated/cx1_many_point_closure_20260919/reproduction_semantics_01 \
PYTHONPATH=code OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
PYTHONDONTWRITEBYTECODE=1 timeout 120s prlimit --as=536870912 --cpu=120 -- \
python -B studies/cx1_many_point_closure_20260919/test_cx1_closure.py
```

The exact five-run operational reproduction, with internal 360-second and
512-MiB caps, is:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH=code \
python -B studies/cx1_many_point_closure_20260919/validate_trajectories.py \
  --output data/generated/cx1_many_point_closure_20260919/reproduction_operational_01
```

The standalone certificate command and the independent algebra command are
given in README.md and SCIENTIFIC_REVIEW_R1_B.md. Validation source and exact
configurations are versioned; generated products are separately stored and
are not theorem premises.

## Integration findings and their disposition

1. The operational driver's per-run source list is not the exhaustive import
   closure. Use it together with the two complete frozen manifests and the
   final standalone import inventory. These jointly identify every executed
   project module. A later promoted driver should emit that complete closure
   itself; the frozen driver is left unchanged to preserve its valid reviews.
2. The three package-import hashes were independently verified after the
   integration run, not independently snapshotted before it. This limited
   historical-provenance caveat is retained. Full source inspection found
   definitions/imports only, with no import-time training or array loading.
3. The theorem's normalized notation `f_n(u)` denotes the physical prediction
   `f_n(sqrt(d)u)` in the reference and finite-capture units. README.md now
   states this identification explicitly. The implementation consumes unit
   directions; no equation or model was changed.
4. The original validation plan mentions six semantic tests. The final suite
   has seven, as already explained in VALIDATION.md and independently rerun.
   The original plan is retained; its five operational configurations did
   not change. A later plan edition should use the current seven-test count.

These are provenance/presentation limitations and clarifications, not unclosed
scientific proof obligations. Numerical refinement differences remain material:
the recorded eight-probe prediction change is about `1.82e-7` for time
refinement but `0.061` for integration/population refinement. Small training
loss and exact reproducibility do not certify distance to the population flow.

## Repository and promotion boundary

All work is in this flat study and its separately generated data namespace.
The task preserved concurrent changes and made no maintained docs/code edits.
Scoped commits use the shared Git writer lock and an explicitly checked index.
The study is ready to serve as input to a concrete canonical promotion package.
That later assembly must be self-contained, receive its required integration
review and obtain explicit user approval before established files change.

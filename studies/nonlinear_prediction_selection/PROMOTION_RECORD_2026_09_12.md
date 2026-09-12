# Approved promotion of nonlinear prediction selection

The user replied **“yes I approve”** in this task after being presented with
[PROMOTION_PROPOSAL.md](PROMOTION_PROPOSAL.md), canonical proof v3 and final
integration edition/patch v4. Approval is for precisely C.4.9 and its two guide
scope/navigation additions. It is retained here under workflow Part 2.5.
The approval does not authorize starting the separately recommended next study.

## Incorporated scope and exact correspondence

Applied [PROPOSED_EDITION_v4.patch](PROPOSED_EDITION_v4.patch), SHA-256
`f15934b5cf3b2b9db9bc7bab32109a8146ba9f0d31baef36d99a89ca9a0c3dbd`,
using its two unique guide replacements and its chapter overview/append.
The complete canonical addition is v3, SHA-256
`c858c7b41d90b490871450b8bf7494afe8c6cd7f39bebd3f1faa89f3604a5879`.
No scientific statement, proof, coefficient, hypothesis or scope was changed
at integration. Only the two approved established paths were edited.

| Live established file | Reviewed final SHA-256 | Correspondence |
|---|---|---|
| docs/global_nonlinear.md | `7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465` | Byte-identical to standalone_v4; entire canonical proof at lines 12994–15322 |
| docs/README.md | `26c5f81ad355b892430e015a786df1d0e2e4f6c9a1fc920ea634bd311558412e` | Byte-identical to PROPOSED_GUIDE_v4.md and standalone_v4 |

The promoted theorem retains the canonical two-hidden tanh model, stored
variances `(1,1/n,1/n²)`, mobilities `(n,1,n)`, unhalved mean-square physical GF,
actual finite Gaussian readout, full first rows and true initialized adjoint.
For the stated one-atom angle/label rectangle it characterizes a nonlinear
whole-circle episode at `T_epsilon=tau0/epsilon`, proves unweighted added-risk
and paired second-hidden margins, and captures actual finite GF with width
first at each positive epsilon, then epsilon to zero. The proof's original
initial layer, finite episode and qualitative constants remain explicit.
There is no new changed-law endpoint, raw-GD, generalization, first-hidden
margin, solver or superiority claim.

## Reused complete review evidence

The approved scientific and integration inputs were rechecked unchanged against
REVIEW_MANIFEST_v3.json and INTEGRATION_INPUTS_v4.json. The original full reports
are preserved exactly, were previously read completely by the coordinator,
and have these unchanged SHA-256 values:

- [Adversarial A v3](ADVERSARIAL_A_v3.md):
  `5121dff3f35b60e3201efed3d98c002cacce14cf66288d2100722c9ee2a1394a`.
- [Adversarial B v3](ADVERSARIAL_B_v3.md):
  `88447dec945f203b876c9b4b91a5b921d72356245a580196f2fdfc35c9fd3a46`.
- [Integration v4](INTEGRATION_REVIEW_v4.md):
  `356070cc6e08172f7af98d82af66f956d01a79c97b14f139277509811d26e1c6`.

The separate `/root/promotion_fingerprint_check` agent performed an independent
mechanical fidelity check at 2026-09-12 11:01:52 UTC. All 20 manifest entries
(15 distinct files), original reports and live scientific baselines matched,
including exact current-guide equality. Its scope was instructions, metadata
manifests and byte processing only; this is not represented as a new scientific
review. No changed scientific dependency required reopening the completed reviews.

## Actual integration checks and preservation

The coordinator reread current AGENTS.md and the complete workflow. The shared
index was empty, and concurrent dirty paths were retained without content reads
outside this study's allowed scope. Before application, `git apply --check`
passed against the approved patch. Application used the nonblocking common
`pde-writer.lock`, rechecked HEAD/index and both baseline hashes, and applied
only that exact patch. The lock was released before the separate checks.

Actual post-application checks under Python 3.10.12 passed:

- both live files equal the reviewed standalone edition byte for byte;
- the entire new section equals the frozen canonical addition;
- reversing the additions recovers all older global text and the complete
  current guide, including the entire concurrent strategic roadmap;
- all eight other documentation files retain their before-application hashes;
- all three new C.4.9 links resolve, labels NS1–NS9 are present exactly once,
  and new mathematical delimiters are balanced.

The patch emitted an informational warning about its approved trailing blank
line. Those exact reviewed bytes were retained. No code was edited, PDF/exporter
work was touched, or training experiment run. The unchanged reference certificate
and complete standalone review checks had already passed; exact live/draft
correspondence transfers those checks without changing their stated scope.

Recheck the approved correspondence with:

```text
sha256sum docs/global_nonlinear.md docs/README.md
cmp docs/global_nonlinear.md data/generated/nonlinear_prediction_selection/standalone_v4/docs/global_nonlinear.md
cmp docs/README.md studies/nonlinear_prediction_selection/PROPOSED_GUIDE_v4.md
```

Generated machine-readable before/application/after records are in
`data/generated/nonlinear_prediction_selection/promotion_20260912/`.
The essential values are also retained here; generated products are not committed.

Application record:

```json
{
  "user_approval": "yes I approve",
  "applied_utc": "2026-09-12T11:02:37.528195+00:00",
  "head_at_application": "747e0faac467fb9431d9a96ae920c87984870406",
  "final_hashes": {
    "docs/global_nonlinear.md": "7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465",
    "docs/README.md": "26c5f81ad355b892430e015a786df1d0e2e4f6c9a1fc920ea634bd311558412e"
  }
}
```

Post-application result:

```json
{
  "checked_utc": "2026-09-12T11:03:02.573755+00:00",
  "python": "3.10.12",
  "exact_reviewed_file_correspondence": true,
  "entire_canonical_append_equal": true,
  "prior_global_recovery": true,
  "complete_guide_and_roadmap_recovery": true,
  "unchanged_other_docs": 8,
  "new_links_resolve": 3,
  "new_section_line": 12994,
  "new_statement_labels_valid": true,
  "new_math_delimiters_balanced": true,
  "final_hashes": {
    "docs/global_nonlinear.md": "7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465",
    "docs/README.md": "26c5f81ad355b892430e015a786df1d0e2e4f6c9a1fc920ea634bd311558412e"
  },
  "code_changed_by_this_task": false,
  "training_experiments_run": false
}
```

## Git correspondence

Integration commit: to be recorded after the locked transaction.
The commit stages only the two approved established files, the updated study
README and this promotion record. Earlier study evidence and unrelated concurrent
changes are preserved.

# Main-agent routing repairs: A3–A5 and A8

Date: 9 September 2026. This is an implementation record, not an independent
acceptance review or a new scientific result. The broader static routing review
identified these outstanding groups after the initial mechanical migration.

## Scope

`resnet_dense_long_horizon`: one selected generated output root now carries raw
traces, processed summaries, figures, report and metadata. The reproduction
script passes it to both producers and the post-run manifest. The manifest
separates source/run roots; its checksum labels are virtual, resolved through
the manifest. Source and retained evidence cannot be chosen as output roots.

`resnet_dense_early_audit`: both current-directory defaults now select the
repository's generated study directory. Existing explicit overrides remain.

`resnet_operator_core`: a small study-local path module separates source,
selected evidence and generated products. Runners, restarted traces, merged
references, statistical and variance analyses agree on the selected roots.
Analysis import no longer creates directories. Historical replay is an explicit
input override, not a silent fallback. The advertised commands no longer rely
on the removed relative virtual-environment path.

`mfp_quadratic_compiler`: campaign 2/3/4 postprocessors, campaign 6 diagnostic
writers and the centered-depth-one writer now export fresh products below data.
Their direct consumers select retained numerical inputs and source-controlled
exact certificates separately. An explicit input-tree override selects replay
certificates too. Historical absolute/relative sector labels resolve without
modifying any frozen manifest or expected hash. All 125 sector bytes were
checked against the retained result manifest.

Campaign 4's cumulative-budget producer and historical provenance builder are
explicitly archive-only and refuse at the start of `main`, before arguments,
subprocesses, directories, ledgers or seals are touched. Their original bodies
remain inspectable. This does not manufacture a fresh budget or authorize a
new campaign. Old live-source hash comparisons still expose migrated bytes;
those seals are not regenerated, waived or described as fresh passing reviews.

## Bounded validation

From repository root, with no optional scientific imports or training runs:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python studies/repository_refactor_2026_09_09/test_resnet_routing.py -v
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python studies/repository_refactor_2026_09_09/test_quadratic_routing.py -v
make check
```

At this checkpoint: 7 ResNet routing tests, 6 quadratic routing tests and all
52 core tests pass. The routing tests cover defaults, independent input/output
selection, no directory creation on helper import, protected destinations,
post-run metadata roundtrip, producer/consumer bindings, shell syntax,
historical sector bytes and actual early archive refusals. The first sector
path test found the older `mean_field_peeling/quadratic_compiler` prefix; the
resolver was corrected and all 125 retained labels then passed. This failed
first check is not counted as a successful review.

The numerical calculation bodies, accepted certificate bytes, historical
result/manifest bytes, constants and resource budgets were not rewritten.
No expensive compiler, simulation, plotting workflow, package installation or
scientific reanalysis was run. Syntax and routing checks do not establish that
all historical workflows reproduce in the minimal core environment. Independent
routing acceptance remains required.

# Shared-consumer final recheck after evidence archival

The completed worker suite passed 32 tiny tests: 15 routing cases, 13 shared
consumer/helper-placement cases and four retained-reference-loader cases.
The final four-file hashes are in `ROUTING_EXTENSION_FINAL_HASHES.json`;
the full preceding import/helper inventory is in
`ROUTING_REFERENCE_LOADER_HASHES.json`. These are implementation checks, not
the independent Gaussian/MFP routing acceptance.

Main repeated the original 15 cases successfully. After copying the exact
historical test source into this study, repeating the other 17 found one
**test-discovery false positive**: the original broad text search matched its
own archived string containing the old import statement. The original method
treated any text match as a live import, including string literals. The other
16 cases passed. Neither a scientific source defect nor an actual old live
import was found; the unsuccessful repeat has not been relabeled as a pass.

`routing_final_recheck.py` preserves the same 39 exact mechanical importer
comparisons, but replaces that method's lexical absence check with parsing of
actual Python import nodes in every matching source file. It does not ignore
an actual import merely because the file is archival. All 17 cases then passed
(0.374 seconds), including every other original case unchanged. The source
implementation and original harness/report bytes were not edited to satisfy
this recheck. No coefficient was generated or scientific experiment run.

The private command was:

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B /tmp/pde-routing-final-recheck.RVTHAhPt/recheck.py
```

This is a recorded audit harness, not a supported library command. Its original
private-path dependencies remain explicit. Preserved source correspondence:

| Original private source | Preserved source in this directory |
|---|---|
| `pde-routing-completeness-acofeOTG/test_routing.py` | `routing_slice1_tests.py` |
| `pde-shared-consumers-ulZD7W/test_shared_consumers.py` | `routing_shared_consumer_tests.py` |
| `pde-shared-consumers-ulZD7W/BEFORE.json` | `routing_shared_consumer_baseline.json` |
| `pde-frozen-reference-fix-slZtav/test_connected_reference.py` | `routing_reference_loader_tests.py` |
| `pde-frozen-reference-fix-slZtav/BEFORE.json` | `routing_reference_loader_baseline.json` |
| `pde-routing-final-recheck.RVTHAhPt/recheck.py` | `routing_final_recheck.py` |

The original directories are under `/tmp` on the recorded host. Their source
and baseline copies are retained to make the predicates inspectable after
those temporary directories disappear. Reusing them elsewhere requires
explicitly reconstructing/remapping that private fixture layout; no claim
that these historical harnesses are portable standalone repository entrypoints
is made. The maintained core tests require none of these files.

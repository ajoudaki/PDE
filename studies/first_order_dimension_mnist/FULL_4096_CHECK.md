# Independent verification of the full n=P4096 continuation

This check is confined to the current study's full-width continuation:
three seeds (1729, 2718, 3141), the existing MNIST 3/5 split and normalized
784-dimensional inputs, unchanged network and fixed-p=1 closure engines,
float32 with TF32 disabled, block2048, and the declared Heun steps 0.25
(network) and 0.125 (closure). No training is performed by this reviewer.
The closure has nominal sign-paired population P4096 and 2048 stored rows.

`REPLAY.py` now accepts `--run-group main4096` and
`--control-group controls4096`. Its independent forward calculations use
NumPy float64 and saved arrays, importing neither engine, runner,
initializer, nor data producer. Checkpoint replay accepts completed run
directories directly. The analysis audit checks every saved common time,
all 1000 validation IDs, all nine closure/network seed pairs, within-class
metrics, diagnostic-label metrics, and the exported sample arrays.

The completed reproduction checks answer separate questions:

- Recompute selected and terminal checkpoint predictions directly from
  saved weights, with absolute tolerance 8e-6 for the float32 runs; record
  sign changes explicitly.
- Compare the seed1729 trajectory through T100 with both earlier
  `speed4096` repetitions. Require per-time RMS at most 1e-5, maximum
  difference at most 1e-4, and identical prediction signs; record bitwise
  equality separately.
- Compare fresh half-step runs with seed1729 at every matching saved time
  through its actual terminal horizon. The declared numerical gate is
  validation RMS at most 0.002 and accuracy difference at most 0.2
  percentage points. This is refined-step numerical reproduction. It does
  not establish a same-configuration bitwise full-horizon rerun.

Generated evidence is retained under
`data/generated/first_order_dimension_mnist/replaychecks/full4096/`.
The grouped command-line interface loads successfully. The generalized
primary and secondary analysis sources and `WIDTH_COMPARE.py` were read
completely. Their same-time indexing and normalization are correct. The
width comparison uses each width's own network mean at the exact common
time intersection. The requested provenance guard now also asserts the
input widths and run groups.

All six main runs reach T600 and their direct selected/terminal checkpoint
replays pass, with maximum prediction error 5.13316e-7 and no
prediction-sign changes. For both models, every seed1729 saved
train/validation prediction and Gram array through T100 is bitwise
identical to both earlier speed repetitions. The six-run configuration
audit verifies actual 4096 network / 2048 folded closure checkpoint row
counts, full evolving matrix shapes, float32 saved arrays and settings,
the exact data hash, and complete 2400/4800-step horizons. Every frozen
runner, engine, initializer, and data source matches the current unchanged
core bytes. Evidence: `configuration_audit.json`, individual reports in
`main/`, and the two `*_prefix_audit.json` files.

**Primary and width-comparison audits PASS.** `validation4096_001` is
independently reproduced for all 61 common times through T600, all 1000
validation IDs, all nine seed pairs, within-class and true-label diagnostic
metrics, and exact exported NPZ/CSV predictions and worst-example IDs.
The largest scalar discrepancy is 8.89e-16. `width_comparison_001` is
independently reproduced at all 51 shared times through T500, using each
width's own network mean. Its largest scalar discrepancy is 1.67e-15.
The mean individual closure-to-network-mean RMS at the same T500 decreases
from 0.06524577 at2048 to 0.05402190 at4096, a descriptive 17.20245%
reduction for these three seeds. These are equal-time numbers; the
width4096 T600 headline is a separate comparison.

**Full-horizon half-step checks and direct control replay PASS.** Both
fresh seed1729 controls reach T600 with unchanged core source/data/settings
and half-sized steps (network0.125, closure0.0625). All 61 saved times pass
the declared validation RMS/accuracy gate. Direct saved-weight replay
has maximum prediction discrepancies 4.43977e-7 (network) and 5.23659e-7
(closure), with no sign changes. Thus all eight main/control checkpoint
replays pass, and their maximum prediction discrepancy is 5.23659e-7.

| Numerical comparison with the original step | Network | Closure |
|---|---:|---:|
| T600 validation RMS difference | 1.18309314e-5 | 5.58943189e-6 |
| T600 maximum absolute difference | 9.31620598e-5 | 7.00950623e-5 |
| T600 prediction-sign changes | 0 | 0 |
| Largest RMS over all 61 saved times | 5.83752087e-4 | 1.15026229e-4 |
| Largest absolute difference over saved times | 8.83340836e-4 | 2.11119652e-4 |

`analysis4096_001` control summaries agree with independent recomputation;
its tiny final-RMS rounding differences come from float32 versus float64
reductions. Reported main test accuracies and production memory peaks also
match the saved arrays and run summaries. Evidence is in `controls/` and
`analysis/secondary_audit.json` beneath the replay namespace. The new
Full4096 report section was checked against these artifacts: its shared-
T500 comparison, separate T600 prediction headline, within-class and tail
metrics, and finite-resolution qualifications are supported. No full-
horizon same-step bitwise rerun at4096 is asserted or established.

No unresolved implementation, artifact-arithmetic, or correspondence issue
remains within this scoped check. The half-step runs are numerical
reproductions at a refined step, and the bitwise repetition evidence is
limited to the recorded T100 prefix.

All conclusions remain about this finite numerical resolution at fixed
p=1, the measured seeds, and the existing data split. Increasing the
population and network width does not itself establish convergence of
the closure or exact sample-by-sample agreement.

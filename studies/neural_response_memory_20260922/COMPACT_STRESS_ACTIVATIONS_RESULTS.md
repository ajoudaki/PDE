# ReLU and SELU on the fitted stress tasks

Internally checked experiment, 2026-09-25. Same four tasks and initialization as
the earlier GELU fit-first batch: width2048, 10 hidden layers, non-affine
LayerNorm after activation, 64 training samples, seed20260920, float32, fixed
Euler step1/128. Training target RMS0.04. The numerical core is unchanged;
fit_stress_tasks.py only gained an activation CLI argument.

Test RMS below means closure versus the matching dense endpoint across all8192
whole-circle or equal-area whole-sphere queries. It includes the unobserved
complement of the training arc/cap and is not error against the target labels.

| Activation | Task | Dense train | P1 train | P2 train | P3 train | P1 test | P2 test | P3 test |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| relu | circle_full | 0.03942 | 0.03743 | 0.03741 | 0.03713 | 0.05131 | 0.07427 | 0.06831 |
| relu | circle_patch | 0.03352 | 0.03991 | 0.03925 | 0.03988 | 0.77476 | 0.83307 | 0.77708 |
| relu | sphere_full | 0.03966 | 0.03986 | 0.03978 | 0.03994 | 0.05711 | 0.06814 | 0.05721 |
| relu | sphere_patch | 0.03936 | 0.03999 | 0.03988 | 0.03989 | 0.08382 | 0.15356 | 0.07333 |
| selu | circle_full | 0.31958 | 0.99938 | 0.98515 | 1.00075 | 0.74584 | 0.75271 | 0.76196 |
| selu | circle_patch | 0.03909 | 0.99620 | 0.86087 | 0.71687 | 0.50818 | 0.47451 | 0.50630 |
| selu | sphere_full | 0.03939 | 1.00670 | 1.05046 | 0.73833 | 0.79006 | 0.85601 | 0.71938 |
| selu | sphere_patch | 0.03963 | 0.98470 | 0.93994 | 0.87261 | 0.67936 | 1.00487 | 0.61121 |

ReLU: all16/16 selected fits reached training RMS<=0.04. Model times were
3.59–49.93 seconds including setup and evaluation. The three arc closures used
the single60-second-cap rerun; other selected runs used the30-second cap.
Their whole-circle discrepancy remains0.775–0.833 despite successful fitting:
RMS inside the observed arc is0.0444–0.0460, versus0.894–0.962 outside it.

SELU: only3/16 selected fits reached0.04 (dense on the arc and both sphere tasks).
Dense full-circle RMS is0.31958; closure training RMS is0.71687–1.05046.
Every SELU row therefore has unfinished fitting and cannot be used as a clean
comparison of fitted predictors. All SELU closure runs hit their time caps.
Extending the arc from30 to60 seconds did not fix fitting; the report uses the
predeclared extension endpoints, not whichever attempt had the lowest error.

One bounded SELU/full-sphere/P1 check used step1/512 for30 seconds: training
RMS improved from1.00670 to0.23658 but did not reach the0.065 continuation gate.
No additional smaller-step sweep was launched. This shows sensitivity to the
numerical setting; these runs do not establish an intrinsic positive-loss floor
or distinguish all remaining optimization, integration and closure errors.

These are finite-step fitted-endpoint comparisons, not a verified continuous-flow
limit; endpoints stop independently at the training target or declared time cap.
Higher P does not monotonically reduce test discrepancy in the ReLU results.
The earlier GELU batch remains16/16 fitted and is retained separately.

Evidence: data/generated/neural_response_memory_20260922/compact_stress_activations01/.
The combined rms.csv contains32 selected model rows, including per-model training,
whole-space, region and outside-region errors. selected/selection.json identifies
each retained attempt; selected/ directories use relative links to original output.
All32 primary fits, six arc reruns and one smaller-step pilot are preserved.
The analyzer independently recomputed the selected scores and verified reference
configurations and archive checksums. All39 raw records match current source
hashes and the GELU baseline's inputs, labels, queries and region arrays bit-for-bit.

Reproduce with fit_stress_tasks.py --activation relu (or selu), --task <task>,
--device cuda:0 --out <fresh-root>; add --fit-seconds 60 for the arc extension
and --step 0.001953125 for the pilot.
Every result.json records the exact executable command. Analyze a complete
four-task root with summarize_fitted_stress.py <root>.

The bounded activation check is complete. No further runs are queued.

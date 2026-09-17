# Frozen actual-network extension: three- and four-point circle data

Frozen 2026-09-15 before preparation, worker checks, or training. This is the user-authorized continuation of the same study. The old closure and pair-network campaigns and their producers remain unchanged. Only the six cases below are admitted; there are no outcome-dependent additions.

## Question and competing outcomes

At common physical time T=100, do the unfitted N=1,3,5 closure functions approach the actual dense finite-network functions for the study's three- and four-point circle datasets? H1 is a resolved reduction of closure/network discrepancy with both successive closure orders. H0 is that the apparent ordering is absent, reversed, or explained by seed, width, time-step, precision, or closure-quadrature uncertainty. A result can be inconclusive. This is finite-width, finite-time empirical evidence; it cannot prove convergence as width/order/time tends to infinity. Off-training points have no teacher labels.

The test preserves both hidden layers, all dense stored weights, nonlinear tanh feature evolution, the exact mean-squared-loss normalization, training geometry and labels. No surrogate, rank approximation, initialization conditioning, whitening, fitted clock, fitted template, or altered mobility replaces the network.

## Canonical model and fixed inputs

Reuse `Network` and deterministic correctness checks from frozen `NET_RUN.py`, whose initialization calls maintained `code/pde/finite_network.py`. Physical inputs are x=sqrt(2)(cos(theta),sin(theta)); the trainer stores u=x/sqrt(2). Independently initialize W1~N(0,1), V~N(0,1/n), c~N(0,1/n^2) in the maintained NumPy generator draw order. Output is c^T tanh(V tanh(W1u))/n. Use mean unhalved squared loss, stored-block mobilities (n,1,n), simultaneous Heun on all actual parameters, main float32 with TF32 off. Float64 controls use the identical underlying NumPy float64 initializer, so rounding is explicitly part of the precision comparison.

Copy name/kind/delta/rotation/amplitude/angles_degrees/labels without transformation from `campaign_001/<case>_N1_main/config.json`, verify these exact SHA-256 values at preparation and execution, and archive the input files:

| Case | Training angles, degrees | Labels | Config SHA-256 |
| --- | --- | --- | --- |
| triple_d20 | 25,45,65 | 1,-1,1 | cf1bfe2d79f5d8dcd5fc7a2fbf7e61b2c3bb9afba04c6477c4173df96cd65e0b |
| triple_d40 | 5,45,85 | 1,-1,1 | 2dc8ae649f3b688d147f2e5a77f1ae1f1c8e69fe51b57280299074ebb21559e6 |
| triple_d60 | -15,45,105 | 1,-1,1 | 63501efd8bacedf926a6d6c808099b6f55852641a3de932238c2664268f3e4f6 |
| quad_d15 | 22.5,37.5,52.5,67.5 | -1,1,-1,1 | 70b46f4041348fe1b248356a77927a00ce415a30dbe2643fd378967d9652c269 |
| quad_d30 | 0,30,60,90 | -1,1,-1,1 | 4ccd4bba3cb837ef307304b6973753cd827edf16a4a74bf4f144b169d308cd61 |
| quad_d45 | -22.5,22.5,67.5,112.5 | -1,1,-1,1 | 0a176591e90e346de83969de105c6389f476d4302a705024ecacc83e1a4b40fa |

## Fixed design, horizon, and observables

For each of the six cases run widths 1024 and 4096 with seeds 1729,2718,3141: 36 main trajectories, h=.02, float32. For each case also run a width4096/seed1729 h=.01 float32 half-step control and a width1024/seed1729 h=.02 float64 precision control: 12 controls, 48 total. The controls share the corresponding main initialization. Every trajectory ends at the same T=120 regardless of its settling flag. No continuation is authorized.

Record at times 0,10,...,120: predictions on the fixed 512-angle uniform circle panel, training predictions and MSE. Preserve 1440-angle uniform-circle predictions at both common T=100 and T=120, the initial/final two hidden training Grams, initial/final training predictions, and paired hidden-activation motion on the fixed 128-angle panel. Preserve the complete final W,V,c arrays for all 48 jobs. Record initializer digest, sources, input-config identity, output hashes, commands, environment, per-job logs and failures.

At T=120 only, set `settled` when final training MSE<=1e-6 and max circle changes from T=80 to100 and T=100 to120 both do not exceed .002*max(1,max|f(T120)|), using the 512-angle panel. An unmet gate stays labeled finite T=120; even a met mild numerical settling gate is not a proof of equilibrium. `stop_reason` remains `fixed_T120`.

Primary assessment uses raw closure versus network predictions at the common T=100. Endpoint shapes are secondary and clearly labeled by each endpoint time/settling status. Report each seed and ensemble relative RMS(circle), maximum discrepancy, normalized-shape discrepancy, width drift and seed spread. Maintain closure quadrature qualification: a closure/network order claim cannot bypass unresolved closure quadrature uncertainty, and a stable network calculation does not validate closure quadrature.

Reuse the old NET_PLAN's uncertainty discriminator: both N1->N3 and N3->N5 must reduce average squared circle error by at least10%, with paired mean squared-error gain greater than twice its seed standard error and twice the measured same-case time/precision-control effects. Report actual gains and uncertainty, classify smaller gains as ties/inconclusive, and label any order reversed between widths as width-sensitive. Main/half-step and float32/64 relative RMS curve discrepancies must each be<=.002 for resolved numerical conclusions. Width drift and seed variance remain uncertainty rather than correctness failures. No single-pair template is imposed on these multi-point data.

## Numerical and identity gates

Before training, run the old finite-width deterministic NumPy/GPU forward, RHS, independent autograd mobility, simultaneous-Heun, disk-replay and restart checks on each GPU in float64; all errors must be below1e-10. Both GPU worker checks share a separate total120-second wall budget. These checks have no scientific outcome interpretation.

Campaign gates: unchanged frozen producer/model/plan and input hashes; finite states and outputs; recorded loss increases<=1e-6; dense antipodal oddness<=2e-5 for float32 or1e-10 for float64; replay of every retained final state within the same tolerance. Postprocessing checks 1440-v720 bandwidth discrepancy<=.005 before a resolved shape conclusion. Source identity covers MULTI_NET_PLAN.md, MULTI_NET_RUN.py, NET_PLAN.md, NET_RUN.py and maintained finite_network.py; it excludes mutable presentation/report files. Archive exact bytes before launch and retain manifest/config hashes.

## Hard bounds, retention and terminal stop

New campaign namespace: `data/generated/closure_circle_spectral_mechanism/network_comparison_multi_001/`. Worker checks: `data/generated/closure_circle_spectral_mechanism/multi_worker_checks_001/`. Refuse existing output directories. Two GPU workers on the current host, one BLAS/OpenMP CPU thread each, using the existing CUDA-enabled `/home/amir/miniconda3/bin/python` outside the device-hiding sandbox. Balance the fixed 48-job queue by width/control work; do not select cases using outcomes.

Scientific campaign wall cap1200seconds from first worker launch; every job wall cap120seconds including initialization, observation, state saving and replay; new campaign output cap4GiB; minimum free disk10GiB. A supervisor checks live workers and these caps and stops both workers on any failure or exceeded cap. Preserve partial files/failure status and never overwrite/delete old data. Full state retention is expected below2GiB. No retries, extra seeds, extra widths, extra controls or horizon extensions after the terminal condition. Postprocessing scientific computation remains separately bounded by the supervisor's assigned task.

Outcomes update only the finite-case, finite-time closure-versus-network evidence. Existing algebra remains unchanged. A validity failure or cap gives an incomplete/inconclusive campaign, not permission to adapt the design.

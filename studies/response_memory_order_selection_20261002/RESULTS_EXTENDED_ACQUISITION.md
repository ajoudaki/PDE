# A substantial order effect washes out under common continuation

The extended seed101 experiment produced a large immediate ordering effect, followed by almost complete agreement after the fixed common continuation. This witness stops without a response-memory refinement or proof campaign. The important general question remains open.

This was the exploratory amendment recorded in `AMENDMENT_EXTENDED_ACQUISITION.md`, selected after the original prefix gate failed. The original protocol, gate failure and source remain preserved. No scientific parameter or horizon was changed after the amended outcomes.

## The intervention was substantial

Both n=512 networks began from the same128-epoch checkpoint, then saw every training example64times. AB processed all majority-source minibatches before all minority-source minibatches; BA reversed those blocks. Both received the identical subsequent2368-epoch mixed continuation. Batch size64, raw SGD step0.01, data, initialization and canonical mobilities were unchanged. The total fixed horizon wasT=512, where T is step size times update count.

The primary shifted distribution preserved the shortcut marginal while removing its association with the label. Its label second moment was V_y=0.195001989603. Immediately after the source blocks, atT=38.4, the shifted-risk difference BA minus AB was0.05759999, or **0.29538 V_y**. Shortcut-replacement sensitivities were0.11066394 forAB and0.23552687 forBA. The intervention therefore changed both predictions and shortcut use appreciably; failure was not caused by an imperceptibly small intervention.

At the fixed endpoint:

| Learner | Training MSE | Shifted test MSE | Zero-shortcut test MSE |
|---|---:|---:|---:|
| Width512, AB |0.001275516|0.078347079|0.055427425|
| Width512, BA |0.001298664|0.078129984|0.055292208|
| Width64, AB |0.006818888|0.060635611|0.043020368|
| Width64, BA |0.006804261|0.060677022|0.043034822|
| Width512, no-shortcut feasibility control |0.001316522|Not applicable|0.027474005|

The final wide risk difference was **−0.000217095=−0.00111330 V_y**, well below the frozen0.05 V_y significance threshold. The two wide predictors differed by RMS0.00347369 over the8192 shifted test inputs. The large post-intervention contrast thus became negligible under common continued training.

Neither wide branch reached the exact training-MSE0.001 threshold within the cap. The stipulated first-fit comparison is therefore untested; no extra training was added. At the lowest training loss attained by both,0.0012986638, AB crossed at approximatelyT=509.2 andBA atT=512. Their interpolated matched-loss shifted-risk contrast was−0.00148494 V_y, also negligible. The raw epoch brackets and interpolation are retained; this is not an exact continuous hitting-time calculation.

## The nonlinear signal does learn

The no-shortcut feasibility control reached held-out invariant risk0.0274740, or0.140891 V_y, with a minimum0.0266307 over the fixed run. Its final trainingMSE0.0013165 narrowly missed the exact0.001 cutoff. Consequently the strict joint fitting flag in the raw summary is false, but it would be scientifically incorrect to call this a failure of nonlinear learnability: held-out error fell by about86% from the zero-prediction baseline.

The original spurious branches also acquired useful invariant prediction: their zero-shortcut risks were about0.284 V_y. Thus the early prefix's lack of useful invariant prediction did not persist. The zero-shortcut control changes one input coordinate and is only a feasibility check; its better performance alone does not prove that label correlation suppresses representation learning. The conditional marginal-preserving uncorrelated-shortcut control was not triggered because both original branches did acquire invariant prediction.

## Ordinary forecast and stopping decision

The width64 nonlinear learner completed both schedules before either wide target branch ran; its forecast was saved at producer time43.65seconds. It predicted a final risk contrast+0.0000414103=+0.00021236 V_y. Its tiny sign was wrong, so it did not pass the formal sign-sensitive capture criterion. It did correctly forecast the negligible scale. The primary wide effect already failed the substantive magnitude requirement, independently of that rival's status.

No moving-linear-response run, response-memory computation, readout-refitting experiment, fixed-middle-matrix experiment, additional seed or parameter search followed. Those conditional experiments would not change the current decision: there is no consequential persistent contrast here to explain. This single witness neither establishes absence of ordering effects in general nor rules out useful history-based forecasts elsewhere.

## Verification, resources and artifacts

The original manual gradients and directional derivatives passed numerical checks. An independent CPU check also matched the field Jacobian-vector product to an autograd Hessian-vector calculation at3.39e-16 relative error and the output directional derivative at1.60e-16. All extended states and metrics stayed finite. The reported update maxima sample epoch endpoints, not every update. Raw SGD itself is the target; no gradient-flow accuracy theorem is claimed.

There were two additional GPU processes: GPU1's no-shortcut run took24.10producer seconds; GPU0's proxy and target runs took93.08seconds. Their additive recorded runtime was117.18seconds, below the20-minute additional process budget; interpreter startup adds only a small unmeasured overhead. Both processes completed and both GPUs are released. The wall interval from amendment preparation to completion was under10minutes.

Source: `/home/amir/Codes/PDE/studies/response_memory_order_selection_20261002/run_extended_acquisition.py`.

Raw products: `/home/amir/Codes/PDE/data/generated/response_memory_order_selection_20261002/extended_seed_101_nospur/` and `extended_seed_101_target/`. Each contains source/amendment hashes, complete schedules, epoch metrics and partial-run journals, endpoint weights and test predictions. The target directory also contains the forecast saved before wide branches and `summary.json`, whose decision is `STOP_SMALL_PERSISTENT_EFFECT`. The two stdout logs are in the common generated-data parent. No book, paper, maintained code or Git state was changed.

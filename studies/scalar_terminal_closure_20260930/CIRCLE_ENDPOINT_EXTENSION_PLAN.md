# Conditional continuation to a fitted endpoint

Recorded during the original campaign, before any extension implementation or
execution. The original `CIRCLE_EXPERIMENT_PLAN.md` and its results remain
unchanged. This is an explicitly additional, post-initial-results continuation
to answer the user's request for comparison at the end of training.

The original common-time cap is 512. Intermediate observations show that the
center/edges task can converge much more slowly than the first three tasks.
No completed endpoint for that task has yet been inspected. A horizon cap is
not evidence of a fitted endpoint. The user has authorized running the models
and comparing their final circle functions; this continuation keeps the same
scientific models, datasets, initialization, handoffs, and numerical methods.

After the original five-task campaign finishes, extend **every** task whose
selected full-model endpoint MSE exceeds 1e-6, provided its original numerical
refinement passed and the cumulative 3600-second training/analysis budget has
enough time. Do not extend tasks selected for favorable scalar error. Preserve
the original comparison at time 512 regardless of the continuation outcome.

Continue both coarse and fine full states from their saved common endpoint,
at steps 1/8 and 1/16 respectively. The coarse continuation stops at the first
checked common time with both dense and q1 losses <=1e-7, or at time 1024.
The fine continuation reaches that same physical time. Use the three original
coarse-chosen handoff times and the original frozen scalar coefficients. No
new handoff, mode count, random seed, coefficient projection, or tolerance
selection is allowed. Scalar continuations are evaluated up to the extended
endpoint using their original autonomous equations.

Use the same endpoint/loss refinement thresholds and require both selected
full-model losses <=1e-6 before calling the result fitted. No further step
refinement or horizon extension is authorized by this supplemental plan. If
either numerical sensitivity or fitting fails, report the unresolved endpoint
explicitly. Report the initial protocol results and this supplemental result
separately, including when conclusions differ.

Only one sequential CPU training worker, at most two BLAS threads. The original
3600-second cumulative training/analysis budget is unchanged. Retain an
additional conservative 120 seconds for final analysis and checks. Check the
remaining extension deadline during RK steps and before endpoint/scalar
evaluation. Save a partial state/trajectory on interruption. Check all state
blocks for finiteness at accepted steps and record process high-water RSS,
stopping if it exceeds 4 GiB. Originals are read-only inputs; write extension
artifacts into a fresh study-generated directory with source and input hashes.

Validation before extension training: compare one resumed RK4 step to a direct
step using the frozen producer, check saved-state loss reconstruction, and
verify that resuming at zero extra duration reproduces endpoint/scalar outputs.
Independent analysis must reconstruct metrics, scalar/Fourier outputs, and
coarse/fine sensitivity from the extension data. This is additional finite-time
evidence, not an infinite-time endpoint or terminal-tube certificate.

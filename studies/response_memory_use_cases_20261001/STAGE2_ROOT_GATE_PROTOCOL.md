# Exact loss certificate and gated memory: fixed root follow-up

This follow-up was chosen after the index-route pilot/confirmation reports
failed their practical advantage gate and the challenge route derived its
finite-order physical-velocity certificate. Those outcomes motivate testing a
constructive safeguard, not retuning the original comparison.

Use stage2_data01, all1024training rows, the exact canonical tanh model and
prefix/clock normalization in MODEL_RECONCILIATION. Width256, fixed train-only
PCA8 input dictionary from initialized first features, Legendre order3.
Compare ordinary indexed memory; the same model with all memory AND clock
velocities multiplied by gamma=clip(-S/kappa,0,1); and rank24 conventional
factors. S is the exact current contribution of the ungated reconstructed
hidden velocity to loss motion. Set kappa=0.001*initial training label MSE,
with no tuning. Both outer-layer flows remain canonical. The gate is a new
optimizer, not the paper's unchanged autonomous closure. Its continuous-time
descent certificate is not a finite-Euler-step guarantee or a fitting theorem.

Three fresh initialization seeds4101,4102,4103, all three frozen domains,
three methods =27 fits. Factor mobilities are the separately selected stage2
pilot values(fashion0.25,housing4,HAR4), without retuning on these seeds.
Use T128, step1/32, validation-only selection among checkpoints16,32,64,128.
Record train/validation/test RMSE and raw test predictions at every checkpoint,
plus each one-unit-time diagnostic sample of loss, outer dissipation D,
hidden contribution S, gate gamma, and exact ungated/gated derivative.
The measured frequency of positive S is a sampled-time statistic, not an
assertion about every continuous instant. Total state and runtime include the
retained base and dictionary. GPU0 after index-route runs finish, TF32off,
one CPU thread, float32 primary arithmetic.

Repeat seed4101 ordinary/gated on all three domains at half step1/64=6fits.
Thus33 scientific fits charged to root's100-fit reserve. No rescue hyperparameter
search. Numerical validity requires finite states, independent float64
autograd directional-derivative agreement<1e-9, the exact low-rank velocity
identity<1e-9, and captured/eager four-step parity<2e-5. Refinement requires
target RMSE change<0.01*training label RMS; any claimed practical improvement
must exceed three times the refinement change. Record all failures.

The primary question is whether naturally occurring hidden ascent exists in
these actual finite-q indexed trajectories and whether the derived gate
prevents it as predicted. Report absence, inactivity, and harmful slowing.
Practical superiority is a separate demanding prediction: gated test RMSE
at least5% below BOTH ordinary memory and tuned factors, median over three
seeds, in at least two domains; all three seeds must beat both on each passing
domain, and remaining-domain median degradation<=5%. Otherwise do not call
this a useful new architecture. The exact mathematical construction remains
valid independently of practical gate success.

## Mechanism decomposition follow-up, fixed after initial results

The original-field Fashion trajectory for seed4101 has positive hidden loss
contribution at90.6% of sampled times, although the total loss still decreases.
This motivates exactly3 diagnostic replays(seed4101,ordinary field,all domains,
same settings), charged to root reserve. Split the exact velocity into the
instantaneous input-projected velocity and the temporal-lag correction:
V=-(2/n)[R H^T+(R-rho bstar)(hstar-H)^T], summing address columns.
Their separate loss contributions identify whether the harmful direction is
already in current spatial projection or arises from the finite history.
Also record the normalized feature-Gram/dictionary off-diagonal operator block.
No method or test-metric selection follows. Preserve initial33fit source snapshot;
this addition only enriches diagnostics and runs the three declared replays.

# Progressive endpoint search — frozen before execution, 2026-09-14

The user now authorizes numerical testing, starting simple and increasing
complexity until at least one adjacent N=1,3,5 comparison separates. This
supersedes the earlier design-only restriction and single-candidate menu in
README.md. The earlier proposal remains historical design evidence. Execution
uses only this study and maintained docs/code. All sources remain flat here;
all generated material stays under data/generated/closure_endpoint_discrimination.

## Fixed ladder and model

All six cases use the README's 24 equally weighted inputs: cluster centers
(15,35,50,75,100,170) degrees, offsets (-4,-4/3,4/3,4). Normalized directions
u=(cos(theta),sin(theta)), physical x=sqrt(2)u. Define
A=theta-17 degrees, B=theta+11 degrees, C=theta-23 degrees.

| Stage | Labels |
|---|---|
| 0 | cos(A) |
| 1 | cos(3A) |
| 2 | .60 cos(3A)+.40 sin(5A) |
| 3 | .40 cos(3A)+.35 sin(5A)+.25 cos(7B) |
| 4 | .20 cos(3A)+.25 sin(5A)+.30 cos(7B)+.25 sin(11C) |
| 5 | sign(stage4 target), with sign(0)=0 |

No alternate phases, label seeds or input locations are searched. Every target
is bounded by one and odd under theta->theta+pi. Stages are increasing demands
on angular structure; this is not a theorem of monotone task difficulty. The
held-out arc G=(104,166) union (284,346) degrees is fixed before outputs exist.
These two antipodal pieces are not independent evidence. Full-circle output
is also measured; all passive inputs are excluded from training.

Retain the original bias-free two-hidden-layer tanh architecture, Gaussian
variances (1,1/n,1/n^2), unhalved uniform MSE, physical mobilities (n,1,n), true
middle action/transpose and jointly moving hidden fields. Use simultaneous
Heun h=.02. No fitted clock, prediction amplitude or phase correction. Network
float32 disables TF32; closure GPU arithmetic is float64 and checked against
the maintained NumPy initializer/vector field/Heun. Standard ridge schedule
is part of each order. No other study implementation is imported or copied.

## Sequential screens and confirmation

Run N=1,3,5 at Q=2048,P=1024 for stage0; advance only after analyzing that stage.
Observe every5 time units on training inputs plus720 uniform circle points;
save a final1440-point circle and complete final state. Also retain training
activation Grams and paired activation RMS/movement for both hidden layers.

Screen from t=0 through at least100, at most600. At multiples of25, stop a worker
when its whole-circle maximum output change is <.005 in each of its last two
25-unit windows and each corresponding absolute loss change is <.0005. This
is a diagnostic plateau, not an infinite-time theorem. Record each stop time.
If an adjacent pair has gap RMS distance >=.075 and maximum gap difference
>=.15, it is a provisional separation. This may trigger confirmation even if
settling was not achieved; the lack of settling must subsequently be resolved.
If neither pair qualifies, advance to the next stage. Preserve every stage.

Confirm the first provisional case before moving to higher complexity. Run
all three closures at Q=8192,P=4096 and the actual network at width8192 seeds
11,29,47; use width4096 seed11 as a width control. Each worker uses the same
plateau rule and t<=600 initially. For the provisionally separating pair only,
also run Q=16384,P=8192 and h=.01 at the Q=8192,P=4096 rule. If this refinement
still changes a compared radial curve by more than .025 maximum, permit exactly
one further Q=32768,P=16384 run for each member of that pair. Initializer resource
allowances may rise to2GiB and8e9 work units for that declared refinement only;
the feature dictionary is unchanged. No further quadrature grid is authorized.
Reference controls: width8192 seed11 h=.01 and width4096 seed11 float64 h=.02.

Bring all confirmation models to a common time T*, at least100 after their
latest first plateau or initial cap, by checkpoint continuation. Require
T*<=1600. Continue in common100-unit blocks only if some relevant model has
not settled, or its last100-unit whole-circle drift exceeds .01. Stop at the
first common checkpoint where those conditions hold and the separation decision
is numerically resolved, or when the declared cap/budget is reached. Resolution
and step controls must refer to the same T*; comparisons at different times
are exploratory screens only. A provisional case rejected by a correctness
gate is not evidence. If correct but unresolved by its allotted caps, record
that result and advance to the next stage while budget remains.

## Decision and comparison conventions

For each adjacent pair compute D=RMS_G(f_N-f_M) and S=max_G|f_N-f_M|.
Visible separation requires D>=.075 and S>=.15 at the common settled endpoint,
and persistence at the previous100-unit checkpoint with both thresholds met.
At both Q=8192/P=4096 and the finest executed resolution, the same pair must
qualify. Gap metrics use uniform angular weights. Do not search the circle
for a favorable subarc after seeing the result.

The actual network reference is the arithmetic mean of three width8192 outputs;
report the seed range and mean of seed losses. Pairwise differences between
closures, closure errors against the network, and errors against the synthetic
target are distinct. "Higher order worse" is reported only if its gap RMSE
against the network exceeds its predecessor by at least .025 and five times
the corresponding uncertainty; it is not synonymous with visible separation.
The user's requested stopping target is at least ONE validated adjacent-pair
separation. Do not continue to make both pairs separate once that is achieved.

At the endpoint require maximum full-circle changes under the last quadrature
refinement <=.025 and time-step/precision changes <=.002; loss changes under
these controls <=.001. Require D and S to each exceed five times the largest
corresponding gap-norm discrepancy from quadrature, time-step, reference seed
spread, width control or remaining100-unit drift. Report actual uncertainties
even when they fail. No arbitrary population limit or certified error is inferred.
For the stronger claim of different extensions at equally good training fit,
add training MSE<.005 for each compared closure/reference and pairwise training
output RMS difference<.02. Settled but unequal training fit is a separate kind
of approximation failure and may still satisfy the user's shape-separation
request if labeled explicitly. Unsettled curves never count as final success.

All saved data must be finite. Check equation/initialization/Heun identities
against maintained APIs and autograd in float64, tolerance1e-10; Gram symmetry,
PSD up to1e-5, MSE and Gram/RMS identities, positive unit sample weights and
oddness. Reject loss increase >1e-5 per saved interval. Preserve failed outputs.
Check complete checkpoint restart, source/config/input/output hashes. The final
endpoint and plotted dense output must replay from saved parameters/state.

## Runtime, storage and stop

Maximum six screened laws; at most18 initial screen trajectories and22 initial
confirmation/control trajectories per candidate, without replacement seeds.
Continuation is the same trajectory, never a reinitialization. Hard campaign
cap45 minutes scientific wall time,1200 seconds per worker invocation,6GiB of
generated products, and at least2GiB remaining disk. Use at most two GPU workers
and two single-thread CPU workers; CPU may do initialization or low-order work.
Abort exhausted branches cleanly; retain source and partial evidence. Stop
after the first verified adjacent-pair success or at the hard caps, with an
honest unresolved result if success was not obtained. Postprocessing/independent
verification has a separate five-minute budget and performs no training.

A fully automated fresh-run supervisor will retain all decisions, commands,
environment, source versions/hashes, endpoint data and unsuccessful cases.
Final deliverables: radial overlays and differences, angle plot with gap shading,
training loss and settling diagnostics, complexity-ladder outcome table, numerical
controls, and an updated README. Use a common radial offset R=2 when positive,
otherwise R=1+max|f| across all displayed models. No visual exaggeration is
presented as physical output; a difference plot is explicitly labeled.

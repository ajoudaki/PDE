# Stronger controls and interpretation of label design

This addendum supersedes the untested-control statements in the frozen
HYPERGRADIENT_REPORT.md. It does not alter that report or its independently
reviewed manifest. The original five-seed q1 result remains supported. These
additional controls show a useful advantage over the particular alternatives
tested; they do not identify response memory as the only useful compact learner.

## Moving first layer, fixed middle matrix

The frozen-middle learner trains W^(1) and readout w with their canonical
mobilities n and retains W^(2)=W_0^(2). Its hidden features can therefore learn.
Everything else follows the original experiment: two tanh layers, n=512,
zero readout, m=8, T=8, Euler step1/32, 24 Adam label updates, label box[-3,3].
All errors below evaluate a freshly restarted dense learner on the designed
labels, with the same initialization as its designer. Own-surrogate error is
not the selection metric. The fixed protocol is HYPERGRADIENT_CONTROL_PROTOCOL.md.

| Support / seed | Original labels | Dense-designed | q1-designed | Frozen-middle-designed |
|---|---:|---:|---:|---:|
| Regular / 201 | .295037 | .034650 | .059460 | .272051 |
| Regular / 202 | .298426 | .035627 | .059522 | .249521 |
| Irregular / 401 | .331522 | .038105 | .066307 | .209896 |
| Irregular / 402 | .330533 | .035109 | .064161 | .186484 |

The irregular support uses independent, preassigned angular jitter of each
regular point (NumPy seed12345), breaking exact antipodal pairing. q1 retains
90.39% and90.17% of the dense-design improvement on the two new initializations.
This is a two-seed stress test, not a second five-seed task-family confirmation.
The frozen-middle surrogate's own regular-support errors are .051946 and
.055601, much smaller than its dense transfer errors. Its outer optimizer is
making useful labels for its own dynamics, but those dynamics misrepresent
the intended dense learner in this problem.

Code: hypergradient_controls.py. Raw results and exact source snapshots:
`hypergradient_strong_regular01/` and `hypergradient_irregular01/` in the
generated study namespace. Eight outer designs required212 inner solves and
68.61 summed GPU-process seconds, running on GPU0 andGPU1 concurrently.

## Matched moving-state low-rank learner

The separately assigned factor control trains a rank-eight additive matrix
on the same fixed Gaussian base and keeps the same first-layer/readout dynamics.
It has9728 moving scalars versus9729 for q1. Factor mobilities .25,1,4 were
specified before results; the complete comparison is in
[FACTOR_HYPERGRADIENT_REPORT.md](FACTOR_HYPERGRADIENT_REPORT.md).

| Seed | q1 | Factor mobility .25 | Factor mobility1 | Factor mobility4 |
|---|---:|---:|---:|---:|
| 201 | .059460 | .122440 | .240448 | .273412 |
| 202 | .059522 | .073777 | .233653 | .269076 |

The slow-factor control substantially improves over original labels. q1 still
has lower error than every tested rate on both seeds; its advantage over the
best tested factor rate is51.4% and19.3%. Two seeds and three prescribed rates
do not exclude other factor dynamics, random-factor seeds, or rate schedules.
No factor rate was selected and carried into an additional favorable task.

This control reveals a practical requirement: a good surrogate must reproduce
how the intended learner responds to a proposed training signal. Fitting well
itself is insufficient. In both seeds the mobility1 factor learner has lower
own-model error than the mobility.25 learner but substantially worse dense
transfer. This is an empirical contrast between specified dynamics, not a
proof that temporal moments are uniquely necessary.

## Checks and failed check retained

An independently differentiated nonzero-state scalar loss agrees with the
frozen-middle vector field to6.94e-17; its middle matrix stays exactly fixed.
A nonzero label-direction finite difference agrees with its discrete
hypergradient to1.07e-10 relative. All eight final designs and four original
label baselines were replayed through dense training at half the step.

The blanket10% relative-improvement-drift gate **fails** for the weak
regular-support frozen-middle seed201 improvement: its transfer MSE changes
from .272051 to .274067, and its small improvement over original labels changes
by10.65%. This qualifies the size of that control's modest benefit. It does
not endanger the large q1-versus-control gap. Every other comparison passes;
irregular-support q1 improvement drifts by.624% and.661%, and the conclusions
survive at the refined step. No continuous-time hypergradient claim follows.

The first checker asserted the blanket gate before persisting numeric rows.
Its failure and source remain in `hypergradient_controls_check01/`. The
unchanged calculations were repeated with write-before-report behavior in
`hypergradient_controls_check02/`; all values and the false gate are retained.
The two checks count32 inner solves; total root-control accounting is244.
The checker is hypergradient_controls_check.py. No reoptimization followed.

## Corrections from independent review

[HYPERGRADIENT_INDEPENDENT_REVIEW.md](HYPERGRADIENT_INDEPENDENT_REVIEW.md)
independently reproduces complete dense/q1 designs at n128/seed101 and
n512/seed201, with MSE differences below6e-8. It also checks discrete gradients,
explicit matrix reconstruction, checkpoint parity, source parity and the
convex frozen control. This is internal checking, not promotion.

The following qualifications apply to all summaries of the frozen candidate:

- The256-point evaluation grid is excluded from gradients, but its pilot
  errors helped choose q. The same grid and teacher are reused in confirmation.
  Fresh seeds test initialization sensitivity, not an untouched task or domain.
- The regular support's antipodal pairs make the full eight-sample Gram rank
  at most4. The manuscript's positive full-Gram hypothesis therefore fails,
  independently of the unverified small-label requirement. No theorem-backed
  hypergradient accuracy is claimed for these practical examples.
- The dense mathematical RHS needs no additional fixed matrix, but its actual
  functional implementation retains its initializer for restarting too. The
  measured peak includes that storage. The state-count table is not a literal
  resident-memory inventory.
- The54.29MiB versus21.09MiB comparison uses identical16-step checkpointing and
  includes fixed matrices, but is one warmed measurement. It is not an optimal
  memory lower bound or a statistically established runtime comparison. q1
  was slower (.870s versus.539s per gradient).
- The original summary script regenerates its results table and figure, not
  every auxiliary export. The frozen label CSV is preserved with hashed raw
  label vectors; fresh designs are reproducible with the adapter or the
  independent CPU review scripts. CUDA-only run mode requires a CUDA device.

The stronger controls resolve two omissions of the frozen review, but they
were not in that review's input packet. Their oracles and finite differences
are internal checks with separate evidence. Calibrated kernel surrogates,
other low-rank parameterizations, new-initialization transfer and larger tasks
remain open. No manuscript text was modified.

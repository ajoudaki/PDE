# Exploratory extension: can ordering enable invariant feature acquisition?

Authorized and frozen before new outcomes on2026-10-02. This amendment was selected after the failed prefix gate documented in RESULTS_FIRST_GATE.md. It is an exploratory follow-up, not independent preregistered confirmation. The original protocol and its failed gate remain unchanged.

The earlier gate required a useful invariant predictor before changing order. It therefore could not answer whether ordering creates that predictor. This extension retains the teacher, finite training data, Gaussian initialization, architecture, batch size64, fixed raw SGD step0.01, prefix128epochs, and64-epoch-equivalent AB/BA interventions. Independent Gaussian signal coordinates continue to eliminate a population linear shortcut to y=tanh(z1*z2*z3).

## One fixed longer horizon and task-learnability control

All extended learners stop at totalphysicaltime512, equivalently51200SGDupdates or2560full-data-equivalent epochs. After the original prefix2560updates and intervention1280updates, both order branches receive the same47360-update mixed continuation (2368epochs). Its first256epochs equal the original stored continuation; the extra2112epochs use a fixed RNG stream seeded by seed+300000. No horizon or parameter search is allowed.

An independent n=512 no-shortcut control trains the same data/labels with input coordinate4 set to zero, from the same initialization, under mixed ordering through the same total horizon. At evaluation its shortcut coordinate is also zero, with all other inputs unchanged. This is explicitly a different input condition used only to establish nonlinear-task learnability, not an answer for the original spurious task. It is useful if it reaches trainingMSE0.001 and held-out invariant risk below0.5V_y within the cap. Failure does not prove representational impossibility; it marks capacity/optimization/sample/horizon uncertainty in this witness.

## Forecast before outcomes

Run the ordinary n=64 network's prefix and AB/BA branches through the same horizon before either wide target branch. Save its signed endpoint-risk forecast before wide branches execute. The costly moving linear-response control is deferred unless a consequential wide gap survives and the narrow learner misses it. The existing source formula and derivative checks remain available.

Primary shifted risk retains exactly the original marginal-preserving shortcut decoupling. Require an endpoint contrast at least0.05V_y, a same-sign contrast of at least0.05V_y between the two branches at their respective first trainingMSE0.001 crossings, and matching signs when both are compared at each of those identical physical times. These three conditions separate matched-loss selection from time-to-fit effects. Also compare at the lowest training loss attained by both branches, exposing interpolation and unequal-time effects. First crossings are at epoch boundaries; no continuous hitting-time claim. A matched loss need not select equal physical time, so it supplements rather than replaces the endpoint comparison.

A narrow rival captures the endpoint contrast under the original sign plus max(25% of effect,0.02V_y) criterion. The endpoint contrast must survive the ordinary rivals before any response-memory claim is considered. If both branches fit and their later primary contrast is below0.05V_y, stop without a q campaign. No-spur failure makes an absent invariant-selection result inconclusive about task learnability. No result is rebranded as a domain theorem.

If a consequential contrast survives and the narrow learner misses it, notify root before further design. Conditional readout refitting and fixed-middle-matrix rivals remain required before interpreting the result as useful hidden-representation selection. They may run only within the original additional budget. No q computation is authorized by this amendment.

Additional pre-outcome interpretation branch: if the zero-shortcut control learns useful invariant prediction but both spurious branches do not, one conditional n=512 control may retain the training shortcut marginal while breaking its label association, using independent y' plus0.1*epsilon, under the same mixed schedule and horizon. This distinguishes the effect of label correlation from removing an input coordinate and changing its scale. The s=0 control alone is a feasibility check, not a matched proof of suppression. Execute only within the unchanged budget; no parameter grid.

## Resource feasibility, validity and records

The completed2560-step width512 prefix took1.72seconds on the producer's timer, including every-epoch full diagnostics. Straight-line extrapolation gives roughly35seconds for51200steps; even a20-fold slowdown leaves a single long trajectory below12minutes. The extension runs independent no-shortcut control onGPU1 and proxy/target work onGPU0. The proxy is64times smaller in hidden-matrix arithmetic; actual timings are recorded instead of relying on this forecast.

At most20additional cumulative GPU-process minutes and30additional wall minutes. Each process has a600-second wall cap; simultaneous processes consume the process budget additively. Check finite weights and training risk each epoch. The implemented driver retains full metrics and predictions everyepoch, exceeding the planned8-epoch reporting resolution and making paired comparisons at either branch's fitting time exact on that epoch grid. Retain all schedules/data/checkpoints and numerical failures. The producer hashes the unchanged original source and this driver/amendment. No new packages or shared file/Git mutations.

Only seed101 is initially authorized by this amended producer. Its consequential unexplained positive contrast earns a separate decision about exact replication; a failed or explained contrast terminates this witness. Changing data, step, width, labels or ordering after outcomes requires new authorization.

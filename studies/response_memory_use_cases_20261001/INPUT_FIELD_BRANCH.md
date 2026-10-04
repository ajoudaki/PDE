# Frozen streaming choice after deterministic pilots

This records the original input-scaled pilot decision. It is preserved as
historical selection provenance, not a canonical-model result. The later
normalization correction in INPUT_FIELD_PROTOCOL.md keeps its teacher B,
C=5, q=3 choice fixed and reruns all 81 configurations without reselection.
The canonical outcomes are authoritative in INPUT_FIELD_REPORT.md and
`input_field_canonical_analysis/summary.json`.

The 36 preregistered deterministic fits all completed, in 8.50 seconds of GPU
fit-loop wall time, after exact captured/eager stochastic update checks.
This artifact is written before any streaming fit. Sources were copied into
the run directory before execution; no code is reconstructed from a hash alone.

At C=17,q=3,T=64, the median prediction discrepancy to dense, divided by
teacher RMS, was 0.00098819 for A and 0.00065359 for B. Both teachers passed
the stage2 gates. The lower discrepancy selects B. For B, C=5 already passes:
median normalized prediction discrepancy 0.02333397; median target RMSE
0.05735368 versus dense0.04682182 (allowed1.25*dense+0.02=0.07852728).
Thus the fixed streaming configuration is teacher B, C=5, q=3. No retuning
uses later streaming outcomes. Interpret the protocol's teacher-selection
comparison at its explicit stage2 screening configuration C=17,q=3.

Next commands use stream seeds101,102,103, then201,202,203,204,205, all at
T=128,dt=1/32,batch64; positive results trigger the declared refinement.
The main algorithm has 3*128+2*5*3*128+1=4225 moving scalars, fixed128²
initial matrix scalars, and transient current-batch storage. A rank15 factor
control has4224 moving scalars. Dense has16768 moving scalars. Controls and
stream RNG seeds are unchanged from the protocol.

The generic C=5 dictionary retains only frequency1 among the odd responses
(constant and frequency2 vanish in exact symmetric quadrature). This is a
severe input truncation. Its adequacy at these tolerances is an empirical
pilot result, not a statement that frequency3/5 teachers have first-harmonic
features: the first layer and readout continue learning in every active model.
The frozen-internal comparator tests how much of the gain those outer layers
can explain.

The 15 streaming pilots passed the narrow learning gates: median RMSE field
0.03316964, dense0.02513445, readout-only0.56618905, frozen-internal0.03631745,
rank15 factors0.01805048. All batch fingerprints agree across models. This
permits the existing five-seed confirmation and numerical-refinement branch.
It does not establish a distinctive improvement over the stronger controls.
Before confirmation, the runner adds direct final-state finiteness and
maximum-absolute-state logging; dynamics, random streams, configurations and
selection rules are unchanged. Exact pre-change source snapshots remain in
the deterministic and pilot run directories.

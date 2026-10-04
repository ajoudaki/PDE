# Round 2: frozen small-state feedback candidates

Freeze before candidate integration. User-authorized continuation under
CUBIC_REPAIR_PROTOCOL_20260930.md. Round1 ablations remove much but not all
error: deleting completion changes hard-case RMS1.2056/1.3378 to0.7277/0.7066.
Passive moving-feature transport gives0.6774/0.7261. Neither is a repair.

Run exactly the following three candidates first on near_pair_sin9,
cluster_triple_cos9 and cluster_triple_cos1, same saved initialization,
MSE.001, seed1, n1024 and256 passive circle points. No tuned constants.

1. Bilinear self-consistent readout/hidden-feature feedback, frozen in
   CUBIC_FEEDBACK_REPAIR_ROUTE_20260930.md. Training m²+m; passive full-function
   response integrals m³. Use restored A/B decoder, and separately retain
   direct bilinear decoding as a diagnostic (not a separately trained model).
2. Congruence-evolving bounded Gram, frozen in
   CUBIC_ENERGY_REPAIR_ROUTE_20260930.md. Training m+m(m+1)/2; passive queries
   cost m+1 aggregate states EACH. The batch256 test evaluates a mesh, does
   not establish a fixed-size full-function decoder, and must not be described
   as having only the training-state count. Query states never feed training.
3. The same moving Gram with gates fixed to one, isolating the saturation
   constraint. Its feature diagonals need not remain below one.

Candidate2/3 preserve exact surrogate loss/energy identities and training
cubic response, but their simple projected-readout query does not preserve
all cubic query terms. This is a disclosed model limitation, not an exact
extension of the original full-query theorem. Candidate1 restores those
terms but still lacks true nonlinear tanh curvature.

Integrator: small_scalar_integrator.py, max scaled RMS over training/query
blocks, rtol1e-8/atol1e-10, target.001, timecap3000,10sec/run. Follow the
round1 gates and transfer branch unchanged. Record initial and endpoint
Gram conditions, prediction aliases, scalar counts and costs, all failed
or partial outcomes, and source/configuration hashes. Generated output is
cubic_feedback_repair_20260930/round2/. No reused file is overwritten.

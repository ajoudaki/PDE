# Frozen comparison of derivative and polynomial dictionaries

Authorized 2026-09-21 by the user's request to compare the newly indexed
dictionary at p=1,2,3 with the old p=1,2,3 on the existing circle cases. This
continues this study's dictionary question. The user explicitly authorizes
reuse of the earlier cases and scores: the narrow archival input exception is
`studies/random_dictionary_learned_circle_20260920/` and its matching generated
namespace, for case definitions, baseline states, settings and producers only.
No other study is an input. Earlier experiments remain untouched.

## Scope fixed before training

Two surviving width-4096 cases: `quadrant_pairs` (angles 10,20,...,80 degrees;
labels ++--++--) and `two_outliers_alternating` (15,27,39,51,63,75,165,285
degrees; labels +-+-+-+-). No rotated fresh configurations or negative controls.
This assumes the recommended two-case suite in the optional scope question;
a later explicit user scope answer supersedes it. No outcome selects cases.

Recover the same actual initialized w,c,W2 from the archived full-network
initial checkpoint, seed20260920. Retain actual random finite readout. Width,
physical circle radius sqrt(2), all trainable read-in/readout vectors, tanh,
unhalved mean squared loss, and mobilities (n,1,n) are unchanged. The whole
middle layer is compressed as B2 M B1^T/n; there is no retained dense residual.
M0=B2^T W20 B1/n. Use maintained ClosureEngine, block256, and the exact archived
adaptive simultaneous Heun trajectory producer. This numerically integrates
full-batch coefficient gradient flow; it is not Adam or SGD.

New p=0 denotes the vanishing order-t increment. New p=1,2,3 retain increment
factors through t^2,t^3,t^4 respectively; old p denotes Chebyshev total degree.
For matching the historical baselines both constructions use the historical
normalized probes e1,e2 (physical inputs sqrt(2)e1,sqrt(2)e2). This explicit
rescaling from the literal physical e probes in the derivation changes the
formula below from F=2vU+W20L to F=vU+W20L.

Set h_a=tanh(w_a), Y_a=W20 h_a, H_a=tanh(Y_a), d_a=1-H_a^2,
U_ab=d_a H_b, L_ab=(1-h_a^2)^2 (W20^T U_ab), and
F_ab=v U_ab+W20 L_ab, v=E[tanh(G)^2], G~N(0,1).
Compute v by Gauss-Hermite quadrature, comparing 128/256 nodes and using 256;
no task data or label enters a frozen field. The implementation uses this
whole-line Gaussian rule instead of the initially proposed truncated Legendre
rule; its agreement check is recorded before any training.

New p1 and p2: lower h1,h2; upper U11,U12,U21,U22. New p3 adds lower L_ab
and eight collected upper quartic-label coefficient functions. With
A_abc=d_a d_b F_bc and B_abc=H_c tanh''(Y_a) F_ab, these are
`A111+3B111`, `A112+3(B112+B121)`, `A121+3B122`, `A122`, `A211`,
`A212+3B211`, `A221+3(B212+B221)`, `A222+3B222`.
This collects symbolic label monomials, rather than retaining all 16 separate
ordered factors. The frozen list is label independent. It is an empirical
full-layer compression candidate; exact preservation of initial probe jets or
the initialized dense function is not claimed.

Dimensions lower/upper: new (2,4),(2,4),(6,12); old (5,3),(15,6),(35,10).
Total vectors: new 6,6,18; old 8,21,45. Free middle entries: new 8,8,72;
old 15,90,350. Both train 3n additional read-in/readout scalars. Use prescribed
raw fields, G=psi^T psi/n, eta_p=1/[1024(p+1)^2], B=psi chol(G+eta I)^(-T),
with no column RMS rescaling or rank deletion. Thus new p1 and p2 have identical
raw spans and differ only in ridge. This inherited regularization is basis
dependent, and ordinary M flow is the inherited filtered coefficient metric.

## Outcomes and scientific interpretation

Reuse archived old p1/p3 and full endpoints at both levels from
`scaling_width4096_primary01` and `scaling_width4096_refined01`. Old p2 was
never executed: run it, rather than relabeling p3. Run new p1/p2/p3. Each model
stops at its own first detected MSE1e-3 crossing; compare on 8192 uniform angles
to the full network at its own crossing. The primary outcome is circle RMS
function discrepancy; sampled maximum and L1 are secondary. This measures
approximation of the dense learned function, not teacher generalization.

H1: the new dictionary has lower RMS at the corresponding p despite fewer
vectors. H0/contrary outcome: it does not. Support or contrary evidence requires
the same ordering at both selected numerical levels and valid endpoints.
Report every case/order, actual errors and ratios. Reversed numerical rankings,
nonfitting endpoints or failed gates are unresolved. Report also actual vector
and middle-parameter counts; p is not an equal size budget across families.
No asymptotic rate, population convergence, universal superiority, or speed
claim follows from this finite single-seed comparison. No performance-triggered
basis changes, new tasks, seeds, activations or normalization tuning.

## Numerical checks and bounded execution

Base 16 new trajectories: two cases times (new p1,p2,p3; old p2) times two
tolerance levels. Level0=(6.25e-5,6.25e-7), level1=(1.5625e-5,1.5625e-7).
Inherited h0=.05, hmax=2, hmin=1e-7, physical T<=10000, accepted steps<=30000,
decreasing-loss acceptance, chord/bisection threshold interpolation, integration
cap180 seconds/cell. Preserve all accepted losses/times, reconstructible states,
2048-angle snapshots, 8192-angle endpoints and failed/capped attempts.

Preflight: algebraic coefficient collection, identical raw p1/p2 features,
projected initialization, maintained all-block gradient agreement, and exact
reproduction of archived old p1/p3 bases and initial predictions (not training).
Require regularized raw Gram condition<=1e10, triangular residual<=1e-8,
finite values; record raw/normalized eigenvalues and numerical ranks.
After execution independently check predictions/losses from states <=1e-10,
same initialization/cases/grids, hashes, fitted status, and endpoint refinement
sampled maximum<=.01 for each predictor and reference. Check 8192 vs4096 errors.

At most one additional level per new cell, only when both preceding endpoints
fit and their own cross-level difference exceeds .01. Divide tolerances by four,
retain latest two attempts, and preserve all earlier files. At most8 extra
trajectories, ordered lexically if resources constrain them. No attempt for a
performance reversal alone; unresolved cells remain explicit.

Use both available RTX3090s; float64 CUDA for dictionaries, training, replay and
scientific metrics. CPU handles file I/O, plotting and scalar quadrature. GPU
access requires the existing sandbox escalation. A successful read-only check
found GPUs free apart from desktop allocation; do not disturb unrelated jobs.

Conservatively retain the previous unspent allowance2609.255107037723 summed
worker seconds. Reserve1600 before launch (four main invocations <=400 each),
and at most400 more for the conditional resolution branch (two <=200 workers).
Release unused reservations after each completion. At most2000 newly reserved
training-worker seconds, within that balance; preflight <=120 GPU seconds.
Record actual worker seconds including construction and outputs. Stop at the
completed comparison or bounds; no automatic experiment expansion.

Root owns this protocol, runner, run record and README. Scoped implementation
agent owns new_dictionary.py and its algebra/preflight check; analysis agent
owns comparison_analyze.py and comparison_plots.py. A separate checker will
audit raw results and metrics without importing that analyzer. All additions
are study-local and internally checked, not established-source promotion.

# Dense finite identities and response-tail assembly

## Contract and candidate

The candidate is `../DENSE_RESPONSE_ADDITION.md`, proposed as Section14 of
`docs/continuous_depth.md`. It is a self-contained proof addition, with no
runtime implementation, solver, experiment, historical arrays, or dependency
on studies. Root remains the sole Git writer. This assembly does not modify
the maintained chapter or its scalar-particle results.

The mathematical contract is fixed finite `n,L,d,m`; arbitrary fixed finite
data; `h0=B x` without input normalization; dense untied residual matrices;
coordinatewise tanh; residual amplitude gamma/L; stored order-one readout;
Gaussian variances sigma_w²/n,1,A² for residual matrices,input,readout;
all blocks trained with mobilities L,n,n; and full mean-square loss in
physical time. The stated Gaussian initialization is contextual only: the
finite algebra and global ODE proof hold for every finite parameter state.

The source's half-sum flow is multiplied everywhere by2/m. Normalized finite
norms and pairings are always written with their factors. The parameter
continuation argument uses the ordinary Euclidean norm after multiplication
by the inverse square root of the explicitly defined flattened diagonal
mobility, not an extra named normalized norm.

## Complete source reads

All ranges below were read in full, with bounded paginated outputs and no
truncation. Source and audit conclusions were checked against their actual
derivations; earlier verdicts are not proof dependencies of the candidate.

| Source | Complete lines read | SHA256 |
|---|---:|---|
| `studies/resnet_dense_long_horizon/theory/dense_euclidean_continuous_depth_pde_conjecture.md` | 1–2309 | `51b3aa5a76c28c5a29c908dc4d12615cc15fea409711d647e744a7ff826c0d70` |
| `studies/resnet_dense_early_audit/notes/hostile_audit.md` | 1–1122 | `ac3f26eaf98b60120a241675ba3f8081425d64891ee6d5555ef839e592365aa5` |
| `studies/resnet_dense_early_audit/notes/response_galerkin.md` | 1–1070 | `49e17f3983dd6289559d9559728b2f47c1890e2f48e9de7cba52c9487e1fce30` |
| `studies/resnet_dense_early_audit/notes/fresh_final_audits.md` | 1–54 | `c80887de02209c4ad29cf99fee64db8120b4c43ea31ca27114227290ba89c858` |
| `docs/NOTATION.md` | 1–98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

The primary manuscript was read in consecutive ranges1–420,421–850,
851–1300,1301–1770,1771–2309. The hostile audit was read in1–400,401–800,
801–1122; response_galerkin in1–380,381–760,761–1070.
For integration only, existing chapter lines1–120 and1380–1490 were read;
this is not a complete review of its existing scalar-particle theorem.

The assembler personally read `solve-math-rigorously/SKILL.md`,
`investigate-conjectures/SKILL.md`, and the latter's complete
`research-contract.md`, `evidence-ledger.md`, and `adversarial-audit.md`.
No experiment-design or proof-campaign authorization was inferred.

## Promoted claims and proof provenance

| Claim | Status and exact scope | Imported proof/dependency |
|---|---|---|
| Dense finite adjoint, parameter gradients, kernel and energy | Exact at every finite state and along its full-mean GF | Primary equations5–11, rederived with every2/m factor; PSD proved as tensor Gram, so no Schur-product theorem is external |
| Global finite physical flow | Proved for every finite initialization | Smooth local integral contraction is proved directly; energy bounds displacement in the constant inverse mobility coordinates and give endpoint continuation |
| Finite-horizon parameter, feature and adjoint envelopes | Proved, with displayed initial-state and T dependence | Energy plus Cauchy–Schwarz; the input feature bound is derived for linear Bx, not copied from the older tanh-input audit |
| Exact training derivatives | Exact along the full finite trajectory | Primary equations14–22 and26h–26k; source and terminal terms retain physical2/m and dense transpose orientation |
| Ordered-product response grades | Exact finite recurrence, including boundary and forcing | Primary equations17–25a; all grades aboveL vanish; forcing is grade0 and each propagator counts only extra ordered factors |
| Factorial tail | Proved under actual finite-trajectory budgets | Distinct-index scalar expansion proves j! counting; no noncommutative simplification, spectral theorem, continuous-depth limit or training analyticity is used |
| Recomputed backward-source bound | Exact perturbation inequality on the same supplied trajectory | Primary25b and the explicit source-difference product are expanded; additional coordinate multiplier bound is stated with its full constant |

These are claim-ladder rungA finite identities and an elementary finite
well-posedness result. The trajectory response recursion is neither a
width-independent state nor an independently evolving surrogate. No
convergence claim at higher claim-ladder rungs is promoted.

## Corrections and deliberate exclusions

1. The older hostile/response notes contain a different input map
   `h0=tanh(Bx)` (or a general chi). Their uniform feature bound2 does not
   apply to the selected linear input map. Candidate14.11 proves the
   appropriate bound using B's normalized Frobenius displacement.
2. The source uses half-sum loss and sample residual `e`. Candidate uses
   canonical residual `r`, full mean loss, and the explicit2/m clock
   translation. Bold readout a separates that vector from the sample index;
   the generator is a distinct typed symbol from the readout varianceA.
3. A factorial backward propagator tail requires the exact source. The
   candidate proves a separate source-error term when it is replaced, and
   its specialized source identity keeps Wdot and the trajectory exact.
   If an approximate training evolution changes them, that identity is
   not the whole defect. The coordinate multiplier in14.21 has no asserted
   width-independent estimate.
4. No Gaussian operator concentration, fixed-depth tensor-program/DMFT
   theorem, iid-depth Young-measure limit, source compiler termination,
   conditioning or closure theorem is imported. The primary manuscript's
   external literature and full infinite-hierarchy dependencies are not
   used. Every required argument for the accepted finite package is inside
   the candidate, so no specialized external theorem needs adoption.
5. No limit is exchanged; width-first and depth-first claims are both
   excluded. In particular independent raw matrices are not replaced by a
   smooth depth field, and the scalar-particle chapter is not used to
   identify the dense architecture.
6. No uniform all-time response envelope, kernel floor, finite total feature
   arclength, fitting, nonlazy limit, strong outgoing nonlinear residual,
   autonomous finite response PDE, or general operator-Galerkin existence
   conclusion is claimed. Finite energy and finite-time tail propagation do
   not supply these missing bridges.
7. The older reports' nonlinear-feedback, continuation-witness, full-matrix
   rank, spectral-Galerkin and anti-oracle arguments are not silently
   bundled into this section. Their architectures, hypotheses, norms and
   needed proofs would require separate bounded acceptance decisions.
8. All historical empirical response-order, width/depth, coercivity and
   restart tables are excluded. No historical computation was rerun and no
   training experiment was conducted. The candidate contains no numerical
   performance claim or reproduction-sensitive result.

## Deterministic arithmetic validation

Two single-state, deterministic float64 sanity checks were run with
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python -B`.
They used direct forward evaluation and a separately differentiated
recurrence, not a time integrator or a stored historical trajectory.
They supplement the proofs; they are not empirical evidence for any limit.

Common parameters were n=3,L=4,d=2,gamma=0.7,
`B=arange(6).reshape(3,2)/9-0.2`,
`W=arange(36).reshape(4,3,3)/70-0.15`, and
`a=(0.3,-0.4,0.6)`. Input arrays below have samples as columns.

The first check used m=2,
`X=((1,0.3),(-0.2,1.1))`, labels `(0.4,-0.6)`, and a central
directional difference of size1e-5 along the exact parameter field.

| Check | Maximum absolute discrepancy |
|---|---:|
| Degree0–L forward sum versus exact differentiated forward recurrence | `1.1102230246251565e-16` |
| Degree0–L backward sum versus exact differentiated adjoint recurrence | `5.551115123125783e-17` |
| Forward training derivative versus central directional difference | `3.2640556923979602e-12` |
| Adjoint training derivative versus central directional difference | `6.045479221394867e-12` |
| Output derivative versus `-(2/m) K r` | `3.20798942965439e-13` |
| Kernel loss dissipation versus inverse-mobility squared speed | `0` |

For every K=0,…,L, the direct recomputed backward source was additionally
subtracted from the exact source and compared to14.20; all discrepancies
were below1e-13.

To test the nontrivial full-mean clock factor separately, the second check
used m=3, rank-two input array
`X=((1,0.3,-0.8),(-0.2,1.1,0.4))`, labels `(0.4,-0.6,0.2)`, and central
coordinate differences of size1e-6 for all45 parameter coordinates.

| Check | Maximum absolute discrepancy |
|---|---:|
| Displayed physical velocity versus negative mobility times numerical loss gradient | `1.2085146772200517e-10` |
| Displayed K versus numerical output-Jacobian mobility Gram | `4.9856785366841905e-12` |
| Kernel energy versus inverse-mobility squared speed | `2.7755575615628914e-17` |

All checked discrepancies were required below1e-8. These validation snippets
are temporary arithmetic checks, not a maintained ResNet implementation;
the promoted content consists of the complete formulas and proofs only.

## Freeze and integration notes

Candidate SHA256:
`446c817b40cb7b32cf83a0fd1bdc3dd54461dbc7bf7b688eacdd9f5dbe9e0286`.

The candidate was read completely after assembly and the mobility-notation
correction. It has no local links, studies paths, external theorems, code
imports, or numerical-result dependencies. Independent isolated full reviews
are still required before promotion; no earlier report is an acceptance
verdict for this candidate.

Appending this section requires a scoped update to the maintained chapter
title/opening and guide description: Sections1–13 remain the scalar particle
benchmark, while Section14 contains only the finite dense identities and
supplied-trajectory bounds stated above. The broad scalar-particle claim in
the existing opening must not acquire dense scope by the append operation.

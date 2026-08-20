# ResNet PDE program

This umbrella collects the repository's three studies of finite causal PDE
descriptions for the canonical fully connected residual \(\mu\)P network. It
does not concern convolutional ResNets or claim a theorem for ResNets in
general.

The intended target takes width \(n\to\infty\) at each fixed residual depth
\(L\), then \(L\to\infty\). The candidate operator PDE also has a source
cutoff \(P\). Identifying the PDE with the ordered dense limit and proving
convergence as \(P\to\infty\) are separate open problems.

## How the three studies fit together

| Study | Role | Strongest durable result | What it does not establish |
|---|---|---|---|
| [`dense_response`](dense_response/) | Finite-matrix precursor | Exact finite-network response structure and audited evidence that low chronological response order accurately reproduces 16 tested finite-network trajectories | Every executed surrogate retains the dense \(W\) matrices; no finite PDE or dense-limit theorem is produced |
| [`operator_pde`](operator_pde/) | Constructive and empirical centerpiece | An explicit finite-\(P\) autonomous candidate PDE with no network-width coordinate, exact internal projected-gradient/shared-transpose identities, and close finite-network agreement on the tested benchmark and transfer panel | Neither equality with the ordered dense limit nor convergence as \(P\to\infty\) is proved |
| [`pde_convergence`](pde_convergence/) | Corrective convergence audit | Exact parity reduction, executed finite-cutoff diagnostics, and a precise compactness/stability obstruction | No compact-time or all-time arbitrary-accuracy theorem, and no replicated aggregate Cauchy contraction |

These are stages of one evidence chain, not three independent confirmations of
the same claim.

## Evidence ledger

### Exact or proved within a finite declared system

- The dense residual network's forward, adjoint, response, tangent-kernel,
  and loss-dissipation identities are finite-system statements.
- At each fixed \(P\), where the candidate PDE solution exists, its shared
  forward/transpose pairing, projected gradient identity, positive
  semidefinite kernel blocks, and loss dissipation are internal identities of
  that PDE.
- For odd activation and symmetric initialization, the even source-Hermite
  shells are exactly inert. The physical ladder begins
  \(P=5\to35\to126\), not \(P=5\to15\to35\).

None of these statements identifies a finite-\(P\) PDE with the trained dense
limit.

### Executed and audited numerical evidence

- `dense_response/long_horizon` ran 16 finite-network cases through response
  orders \(K=0,1,2,3\). Errors fell strongly with order, but all runs retained
  dense matrices.
- `operator_pde/core` directly integrated the finite-\(P\) PDE. On the
  canonical comparison, the Gram-increment gap was about \(1.14\%\) of the
  observed feature motion. The transfer campaign recorded errors below
  \(5\%\) in all 14 tested cases, but its preregistered simultaneous
  equivalence rule was unresolved. These are finite-ensemble consistency
  results, not limit theorems.
- `pde_convergence` phases 02--05 ran bounded diagnostics with retained result
  arrays. The final common-reference audit did not show aggregate contraction:
  its last state and observable Cauchy ratios were about \(1.32\) and \(1.64\).

A plateau observed through \(T=32\) is evidence only on that simulated
horizon, not an all-time bound.

### Incomplete or non-executed work

- `pde_convergence/01_proof_audit` built a substantial seven-gate framework,
  but only 2 of its 12 planned jobs completed and no scientific gate passed.
  Its tests validate infrastructure, not the convergence conjecture.
- The `dense_response` \(K/J/N\) compiler is a formal proposal. No compiled
  width-independent PDE was emitted or run there.
- Conditional compactness and stability reductions identify what would
  suffice for finite-\(P\) convergence, but their hypotheses have not been
  proved for the trained reachable family.

## Current conclusion

The lasting result is that a very small, literal candidate PDE is useful on
the tested nonlazy ResNet dynamics, and its internal geometry is exact. The
central theorem remains open: one still needs collective source compactness,
uniqueness and cutoff-uniform forced stability, followed by trained
width/depth-limit identification. Failure of the present pure-Hermite witness
would not by itself rule out a response-enriched finite causal PDE.

## Supersession rules

- Do not use the old \(P=5\to15\) comparison as evidence against Hermite
  convergence; exact parity makes that step inert.
- Treat the phase-03 lifted outgoing-tail contraction as a local boundary
  diagnostic, not contraction of the trained high-shell tail.
- Use
  [`pde_convergence/05_tail_and_compactness/COMPACTNESS_REPORT.md`](pde_convergence/05_tail_and_compactness/COMPACTNESS_REPORT.md)
  for the current convergence status.
- Use the scoped phase reports for numerical claims. Raw arrays are retained
  for the dense long-horizon study, the convergence phases, and the later
  operator rerun; some original compact operator campaigns retain sealed
  processed evidence but omit their complete raw trajectories.

These three substudies live only under `studies/resnet_pde/`.

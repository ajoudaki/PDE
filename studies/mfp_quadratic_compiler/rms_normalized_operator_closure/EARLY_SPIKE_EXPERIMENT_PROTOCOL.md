# Preregistered early-spike diagnostic

Status: frozen before implementation or execution.  This experiment selects
a proof route; it cannot establish a closure or a width-limit theorem.

## Decision question

Do Gaussian extreme rows create an early width-growing kernel concentration
or output boundary layer in the exact doubly RMS-normalized physical flow?

## H1 / H0

- `H_barrier`: outer RMS competition and trained-readout balance keep the
  early kernel tight and the loss curves equicontinuous at the tested widths.
- `H_spike`: a rare row/column produces a growing early kernel peak and a
  hitting time for a fixed output level that decreases systematically with
  width.
- A mixed/nonmonotone panel is inconclusive.

## Mechanism-preserving testbed

Use the exact one-sample, two-hidden-layer model in `PROTOCOL.md`, iid
Gaussian initialization, `epsilon=1`, target one, `eta=1`, training of all
layers, and exact differentiation through both denominators.  No layer,
matrix core, normalization term, or physical residual factor is removed.

## Primary metrics and controls

For widths `128,256,512,1024`, use matched deterministic seed labels and
record on `t in [0,0.25]`:

1. `max_t K_n(t)` and its time;
2. first hitting times of `f=0.05` and `f=0.10`;
3. maximum coordinates of `A,u,Z,H,Y,R,T`;
4. the three layerwise kernel contributions;
5. loss-dissipation residual and the exact row/column balance residuals.

The matched control is the same initial tensors integrated with half the time
step.  There is no fitted nuisance model.

## Thresholds

- Evidence for `H_spike`: both upper-width successive median ratios of
  `max K` exceed `1.25`, or both hitting-time ratios are below `0.8`, while
  every validity gate passes.
- Evidence for `H_barrier`: both successive median ratios for `max K` lie in
  `[0.8,1.25]`, hitting-time ratios lie in `[0.8,1.25]`, and no upper-tail
  replicate shows a step-sensitive peak.
- Otherwise: inconclusive.

These thresholds update only the priority of the reachable-spike versus
weighted-compactness proof routes.

## Numerical validity gates

- float64 throughout;
- fixed-step RK4, primary `dt=5e-4`, matched control `dt=2.5e-4`;
- maximum relative discrepancy in `f` and integrated loss identity below
  `5e-4`; balance-law residual below `2e-3` after scale normalization;
- all denominators finite and at least `sqrt(epsilon)` to roundoff;
- no excluded replicate; nonfinite arithmetic makes the panel inconclusive.

## Replication, branch, and budget

Use four matched seed labels at every width.  If and only if one threshold is
met but a single replicate determines it, add four seeds at widths 512 and
1024.  Hard cap: 40 integrations including half-step controls (32 in the
frozen primary panel and at most eight additional primary integrations in the
branch), ten wall minutes, and 3 GB of new artifacts.  Stop after that panel
regardless of outcome.

The initially typed cap of 24 was arithmetically inconsistent with four
widths, four seeds, and two step sizes; it was corrected to 40 before any code
or data existed.

## Ledger consequence

`H_spike` prioritizes a probabilistic reachable-extreme stopping theorem;
`H_barrier` prioritizes a weighted moment/traffic cutoff-removal theorem.
Neither promotes E6 or E7.

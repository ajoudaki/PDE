# Initialization-only finite-panel compression

## Contract and source scope

This new theoretical study follows the user's request to complete the analysis
of the empirically successful metric/source compression, permit construction
at q<m, and obtain an explicit dense-variability comparison with logarithmic
width dependence. It is distinct from the closed unseen-input experiment
campaign. No new training campaign, paper promotion or empirical retuning is
authorized here.

The target is the canonical finite Gaussian network and nonlinear gradient
flow in the current paper: fixed hidden depth L, first entries N(0,1), hidden
entries N(0,1/n), zero readout, MSE loss and mobilities (n,1,...,1,n), strip
analytic activations with bounded derivative but possibly unbounded values,
positive unweighted initial feature-Gram gap gamma, and the existing small
fixed label allowance. There are m training inputs and p additional passive
inputs declared at initialization; passive labels never enter setup or flow.
Track the complete physical-time trajectory and fitted limit on this panel.
Do not silently replace a whole-sphere benchmark by a panel quantile, or a
coupled realization by an independent reference.

Required outputs: a construction defined even at q<m; rigorous storage and
error dependencies on n,m,p,d,gamma,L,beta (and confidence/label scale where
needed); exact provenance of coefficients; initialization-only jet existence
separate from practical setup work and from global-trajectory distillation.
A full rollout is not relabelled as a cheap initialization-only algorithm
merely because an ODE is determined by its initial state. All fixed matrices,
data, residual state and temporary costs must be accounted for. No log^5 n
accuracy claim follows from prescribing the empirical q law alone.

Allowed scientific inputs are the user-referenced paper and its capture
implementation, established docs/code, and (explicit user approval in this
turn) directly relevant proofs in finite_panel_absolute_compression_20261005
and integrated_general_compression_20261004. Those proofs require fresh checks;
their prior conclusions are not premises by reputation. No other study is an
input. Generated checks belong to data/generated/initialization_panel_compression_20261008/.

## Work and ownership

Lead: source reconciliation, complete integrated argument and this README.
Scoped routes own separate flat proof notes: OPTIMIZER.md (q<m construction),
PANEL_BOUND.md (source rank and storage), INITIALIZATION.md (jets and setup).
They do not read each other's drafts during the initial round. Route claims
remain candidates until reconstruction and adversarial checks; unresolved
implications are recorded explicitly. Shared paper/code and earlier studies
remain unchanged. The lead is the only Git writer.

## Starting point

- Empirical runtime: uses a positive-definite m-by-m readout Gram and rejects
  q<m. Its sources come from a disposable full-interval dense RK4 rollout.
- Prescribing q proportional to log(en)^(5/2) gives a logarithmic inventory,
  not a theorem that its source approximation attains dense variability.
- Target theorem, removal of the construction restriction, and efficient
  strictly initialization-only setup are open at the start of this study.

## Current result and limitations

[RESULT.md](RESULT.md) is the integrated report. Detailed arguments are in
[OPTIMIZER.md](OPTIMIZER.md), [PANEL_BOUND.md](PANEL_BOUND.md), and
[INITIALIZATION.md](INITIALIZATION.md).

- A smooth bounded spectral readout and source truncation define the corrected
  metric/deficit optimizer at every positive width, including q<m. The old
  complete-source trajectory is unchanged on its certified Gram domain. The
  construction still retains m deficits; below that domain their energy is not
  necessarily prediction loss. A fresh isolated review passed these exact
  deterministic and conditional-transfer claims:
  [OPTIMIZER_REVIEW.md](OPTIMIZER_REVIEW.md).
- The finite-panel source count gives absolute log(en)^5 retained storage,
  with leading coefficient explicitly proportional to
  (L+1)(2m+p)^2[U_fin/a]^2(Ym/gamma)^4. The conservative beta-only envelope is
  beta^(120L). This is a sufficient bound, not a sharp optimum. No label-cap
  substitution is used to remove the fourth power. All data/metric/deficit and
  execution workspace charges are recorded. The guarantee is for the declared
  panel, not arbitrary undeclared queries.
  An exact, fully counted projection onto the panel's input span reduces the
  additive ambient-dimension overhead to O((L+1)(m+p)^2+(m+p)d).
- Literal zero-time-jet compilation is explicit and uses no later dense
  weights, but its certified jet count is superpolynomial. The finite compiler,
  a generic analytic-source obstruction, and a focused label-amplitude route
  are recorded separately. The latter yields norm sensitivity and a narrow
  complex disk, not the required cheap all-time compiler.
  The deterministic compiler and inverse received a separate scoped conditional
  review: [COMPILER_REVIEW.md](COMPILER_REVIEW.md). Its scalar elementary-function
  accounting observation is addressed explicitly in INITIALIZATION.md.
- A cheap polynomial/near-quadratic strictly local setup with the unchanged
  guarantee remains open. It has not been replaced by a full-interval rollout
  under another name. The experimental source producer does use such a rollout,
  and its heuristic rank and selector are not certified by this theorem.

The lead reconstructed the relevant current paper source foundation,
coordinate-selection, comparison and initialized-variance arguments; the
storage route separately checked finite-query localization and tolerance
inversion. A concrete import correction is recorded: the full-range comparison
uses coefficient 64, not the older finite-panel coefficient 32. These checks
are targeted dependency checks, not a new review of the entire paper.
The new deterministic compiler/rank implications remain explicitly separated
from the inherited stochastic source event and its qualitative width onset.

No new training experiment or shared paper/code change was made. The next
research obligation is the reachable-coordinate/complex-amplitude estimate
identified in INITIALIZATION.md, not a new empirical sweep. Nothing has been
promoted into the established book or paper.

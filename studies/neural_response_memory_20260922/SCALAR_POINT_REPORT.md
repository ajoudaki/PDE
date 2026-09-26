# Direct passive-point test of the scalar closure

2026-09-25. User-requested sanity check separating aggregate compression from
the preceding Fourier readout. Study-local empirical result, not promotion.

## Finding

**The implemented K=5 scalar truncation fails even with one direct passive test
point.** Its construction and passive bookkeeping pass independent checks, but
its fitted prediction at the unseen input is inaccurate. Thus the preceding
failure cannot be attributed solely to Fourier representation or angular
quadrature. This rejects this low-cutoff practical witness, not all scalar
closures or the separate theorem for a saturated hierarchy.

The model is unchanged: three hidden tanh layers, width 16, no biases, normalized
circle inputs, seed 20260920, Gaussian initialization with stored readout divided
by n, mean squared loss and mobilities (n,1,1,n). Active training points are
10° and 125°, labels +1,-1. The test point is fixed at 60° before the run, without
a label or contribution to the loss. History order P=1 and the old activity
clock are unchanged. The protocol is SCALAR_POINT_PROTOCOL.md.

| Model | Fitted prediction at 60° | Absolute difference from fitted dense | Fitting time |
|---|---:|---:|---:|
| Dense | 0.6431604545 | 0 | 4.0444070 |
| Population P=1 | 0.6163626931 | 0.0267977614 | 4.2349259 |
| Scalar K=5 | 0.2064426036 | 0.4367178509 | 2.8239351 |

Every model reaches training RMS sqrt(0.001)=0.0316228. The point error exceeds
the predeclared 0.10 failure threshold. At the scalar stopping time, dense and
population predict 0.5758054250 and 0.5435747815; the matched-time scalar errors
are therefore 0.3693628213 and 0.3371321779. Different stopping times do not explain
the result. The largest coordinatewise training-output trajectory discrepancy
against dense on the fixed temporal panel [0,2.8239351] is 1.03336. Small final training loss
does not imply that this scalar closure tracks the network's training path.

## Exactly what was added

Let q be the retained training aggregates and p the additional point-containing
aggregates. The implemented structure is

    q_dot=F_K(q,L),   p_dot=G_K(q,p,L;U_*),
    L_dot=sqrt((r_1^2+r_2^2)/2),   r_a=f_a(q)-y_a.

The passive field h_(ell,*) has the same response-lift chain rule as any forward
input, with first-layer input Gram U_*·U_a against the two active samples.
There is no r_*, point loss, point history A/B, or change from M=2 to M=3.
Point descendants are ordinary scalar tree contractions. Training and passive
output roots both have grade 3; there is no angle vertex, weight tag, Fourier
coefficient, integration over input space, or query quadrature.

At initialization, scalar contractions are evaluated on the realized initialized
network, including its actual reused matrices. During evolution the state and
RHS contain global scalar coordinates and coefficient tables only. An input is
registered and initialized before training; the current finite state does not
provide missing query coordinates retrospectively.

## Controls and numerical reliability

The separate training-only scalar solve matches the scalar solve with the passive
point to 7.41e-8 maximum training-output difference on 121 common time points, below
the 1e-5 gate. Structural checks additionally prove no retained training row reads
a passive coordinate. Arbitrary passive-coordinate perturbations leave training
velocities and the clock unchanged exactly.

Placing the passive point at a training input gives an exact algebra identity:
all 193 passive-containing rows become corresponding training rows after renaming
the input species. The initial coordinates agree. ODE uniqueness then preserves
the duplicate-input identity over the interval of existence. This is a useful
consistency check, but it is not an accuracy test at an unseen input.

Independent checks compare all 18 exact primitive templates at nonzero histories
against direct physical differentiation, including initialized transposes and
inverse-clock derivatives. Errors are at most 2.09e-15. Full output product rules,
independently retained terms, every scalar row, initialization, zero-residual
stationarity and a stripped scalar-only runtime pass. See SCALAR_POINT_AUDIT.md
and scalar_point01/algebra_checks.json. The audit is collaborative internal
checking, not an independent promotion review.

Refining the point solver from rtol 1e-7, atol 1e-9 to rtol 1e-9, atol 1e-11 changes
its fitted point output by 2.78e-9. Dense and population changes are 5.47e-11 and
6.99e-10. There is no angular quadrature to refine. The failure is therefore
numerically resolved for this fixed test, rather than an ODE-tolerance effect.

## Cost and tested limits

K=5 uses 331 training-only patterns and 193 point-containing patterns, plus the
clock: 525 evolving scalars and 271606 retained equation terms. Compilation takes
13.10s and the primary solve7.78s; initialization takes0.011s. Peak reported RSS
is about 245 MiB. The dictionary type count is independent of width, but the
coefficient tables and initialization cost matter; this is not a demonstrated
practical compression advantage over the 560 dense parameter entries at width 16.

K=7 was allowed ten times the preceding Fourier experiment's term cap. It still
stopped at 2000185 retained terms, after 53.35s, before compilation completed.
At that point 2799 patterns had been discovered (1677 training-only and 1122
passive). Its peak reported RSS was about 780 MiB. There is no K=7 fitted result;
no accuracy trend or impossibility conclusion can be inferred for higher K.

Recorded compilation/initialization/integration phases sum to 108.78s, below the
600s campaign budget; the independent algebra replay uses 27.08 CPU seconds of
its separate 120s budget. This accounting excludes authoring, imports, plotting
and reporting. No additional scientific runs followed the declared stop.

## Another route to a whole function

The existing constructive alternative in SCALAR_DECODER_LIMITS.md, section 4,
is a terminal polynomial decoder. Before training, include the contractions
needed to express a polynomial approximation of the entire forward readout:

    fhat(U)=sum_alpha D_alpha(q(T),L(T)) U^alpha.

The coefficients D_alpha are formed from terminal aggregate coordinates. A
new input requires only evaluating this polynomial. On the circle substitute
U=(cos theta,sin theta), so no test mesh or separately evolved Fourier block is
needed. This returns an approximate function, not the original labelled weights.

Specifically, replace each tanh in the terminal readout by a bounded Bernstein
polynomial on a predeclared preactivation interval, substitute the exact
initialized-plus-history matrix formulas, and expand. Every coefficient is a
finite expression in initialized-edge contractions, first-layer weight-column
fields, c and A/B fields. The source's explicit activation error is R/sqrt(m)
for degree m on [-R,R], and its layerwise output estimate separates this readout
error from aggregate and parent-closure errors.

The required contractions, including first-layer weight-column fields, must
be retained before training; the current output-reachable K=5 dictionary does
not contain them all. Its efficiency and required degree are unresolved. More
fundamentally, a different decoder does not repair inaccurate aggregate dynamics.
The present point experiment identifies that as a prior practical problem.
This alternative was assessed from the existing study construction; it was
not implemented or tested in this bounded diagnostic.

## Artifacts and reproduction

New sources: scalar_point_engine.py, run_scalar_point.py,
check_scalar_point.py and plot_scalar_point.py. The engine reuses the checked
exact tree/template helpers in scalar_fourier_engine.py; it does not run that
module's Fourier solver. The physical reference module is unchanged. Root owns
the protocol, runner, plot and synthesis; point_probe owns the engine;
point_audit owns the checker/audit. point_whole_function read the existing
terminal-decoder construction for the alternative above. No other study was
used and no maintained book/code or Git-index changes were made.

Products are in data/generated/neural_response_memory_20260922/scalar_point01/:
raw checkpoints, trajectories, solver interpolants, coefficient-table restart
objects, source hashes, capped-run metadata, scores.json and PNG/PDF plot.
The primary and refined runs use identical scientific evolution code; the
runner's later changes only add separate refinement invocation and distinguish
unfitted terminal-time comparisons from fitted comparisons.

For a fresh reproduction, replace scalar_point02 below with a new directory:

```text
python -B studies/neural_response_memory_20260922/run_scalar_point.py --phase references --out data/generated/neural_response_memory_20260922/scalar_point02
python -B studies/neural_response_memory_20260922/check_scalar_point.py --output data/generated/neural_response_memory_20260922/scalar_point02/algebra_checks.json
python -B studies/neural_response_memory_20260922/run_scalar_point.py --phase scalars --out data/generated/neural_response_memory_20260922/scalar_point02
python -B studies/neural_response_memory_20260922/run_scalar_point.py --phase controls --refine-cutoff 5 --out data/generated/neural_response_memory_20260922/scalar_point02
python -B studies/neural_response_memory_20260922/run_scalar_point.py --phase analyze --out data/generated/neural_response_memory_20260922/scalar_point02
python -B studies/neural_response_memory_20260922/plot_scalar_point.py data/generated/neural_response_memory_20260922/scalar_point02
```

The actual run split controls and the scalar refinement into two commands,
using --phase controls and then --phase refine-scalar --refine-cutoff 5.
Training used NumPy 1.26.4/SciPy 1.13.0 with one numerical CPU thread; plotting
used Matplotlib 3.8.4 from /home/amir/miniconda3/bin/python and explicit
MPLCONFIGDIR=/tmp/pde_scalar_point_mpl. There was no query/label/seed search.

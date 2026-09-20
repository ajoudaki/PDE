# Single-input closure order and trajectory error

This study investigates whether the maintained autonomous observable closure
admits a quantitative relation between closure order and error for the canonical
two-hidden-layer tanh network trained on one normalized input with label +1.
It was opened on 2026-09-20 at repository commit
`bcee9782651c34ae1204d37186e5c57e9282b273` in response to the user's request.

## Contract

Retain the standard Gaussian initialization, small random finite readout,
unhalved squared loss and mobilities (n,1,n). The population initial readout
is its zero limit. Preserve both orientations of the actual Gaussian action
and nonlinear training of all blocks. The primary target is an explicit
vanishing bound in a specified maintained closure order for prediction error
over a fixed positive physical-time interval and the whole unit input circle.
Track stronger all-training-time and state-error statements separately.
An estimate in terms of an unknown target projection tail alone is a useful
reduction but does not settle the requested order-to-error relation. Neither
a redefined order based on future trajectories nor a Taylor approximation
may silently replace the maintained autonomous closure.

## Inputs and ownership

Permitted scientific inputs are this study and maintained `docs/`, `code/`
with their designated reproduction inputs. The user's 2026-09-20 follow-up
explicitly additionally authorizes consulting the studies nominated in the
attached 39-item accounting for a surgical closure-error investigation. This
scoped exception does not establish those studies' claims or authorize unrelated
cross-study retrieval. The follow-up uses the original-gradient-flow scalar
residual argument in `closure_lyapunov_p1_20260916/all_angles_result.md`, the
current full-kernel identity in
`closure_gaussian_reduction_p1_20260917/exact_reduction.md`, and the
state-to-passive-prediction distinctions in
`fixed_p_predictor_uniqueness_20260919/PASSIVE_LIMITS.md`. Necessary arguments
are rederived in the new result; no modified optimizer is identified
with the canonical flow. The previously frozen result and its checks retain
their original narrower input scope.
The supervising task owns this README and final synthesis. Independent route
agents receive explicit scopes and own separate flat route files. Generated
checks and scratch, if needed, belong in
`data/generated/single_input_closure_rate_20260920/`.

No training experiments are authorized or planned. No established files will
be changed. Research and internal checks are separate from promotion.

## Current status

The maintained H2 comparison controls error by a target projection defect, but
obtains that defect's decay only qualitatively. The primary approximation here
is specifically H3's polynomial-core-plus-bounded-word-prefix dictionary, with
ridge `1/[1024(N+1)^2]`; it is not polynomial degree on the fixed core alone.

**Resolved as an internally checked theoretical study.** The primary result
is [RESULT.md](RESULT.md): explicit increasing thresholds P_j such that
every maintained H3 order N>=P_j satisfies

    sup_(t>=0,u in S1) |f_N(t,u)-f(t,u)| <= 2^(-j).

This includes identical physical times through the fitted endpoint and the
whole passive circle. It concerns exact population-closure truncation error;
numerical errors and finite-neural-width errors are separate. The thresholds
are astronomically large. A useful algebraic/geometric rate and a theory of
practical low-order accuracy remain open.

The complete argument and internal checks are:

- [ROUTE_DICTIONARY.md](ROUTE_DICTIONARY.md): quantitative bounded-word
  approximation, rational proof witnesses, explicit source-moment and actual
  code-size bounds, and the maintained positive-ridge estimate.
- [ROUTE_DYNAMICS.md](ROUTE_DYNAMICS.md): exact single-input transformed flow,
  fitting within finite feature time, and linear source-error transfer
  uniform over all physical times and the whole circle.
- [DICTIONARY_INTERNAL_CHECK.md](DICTIONARY_INTERNAL_CHECK.md) and
  [DYNAMICS_INTERNAL_CHECK.md](DYNAMICS_INTERNAL_CHECK.md): complete component
  reads and independent mathematical reconstructions, with no blocking gap.
  Rational Gaussian-moment choices are existential proof witnesses; the
  theorem does not rely on an additional certified quadrature algorithm.
- [CORE_OBSTRUCTION.md](CORE_OBSTRUCTION.md), checked in
  [CORE_INTERNAL_CHECK.md](CORE_INTERNAL_CHECK.md): a distinct diagnostic
  showing that polynomial degree on the fixed Gaussian core alone has a
  positive cubic prediction discrepancy. It does not contradict the complete
  maintained hierarchy's convergence.

The supervising author read every line of all proofs and reports, verified
their input hashes, and checked the combined threshold shift. The component
audits are internal checks, not two fresh blind promotion reviews of a
canonical book addition. The separate assembly check preserves its minor
integer-versus-dyadic wording correction and final source hash.

Contributors/write ownership: supervising task owns this README, final
assembly, `CORE_OBSTRUCTION.md` and `validate_bounds.py`; route agents
`single_input_rate_dynamics` and `single_input_rate_dictionary` own their
named route files and assigned component-check reports. They started with
separate scoped contexts; concrete route findings were then exchanged for
assembly. Internal component checks are not promotion reviews.

Deterministic validation completed with exit zero:

```text
python -B studies/single_input_closure_rate_20260920/validate_bounds.py > data/generated/single_input_closure_rate_20260920/validation_01/exact_bounds.log
```

The script reproduces the maintained exact rational Gaussian certificate,
obtaining the certified lower bound
`E tanh²(sqrt(E tanh²G) G) >= 116560367809/500000000000 > 1/5`,
and checks the feature-horizon comparison constants in exact arithmetic.
No training experiment was run. [CHECK_INPUTS.json](CHECK_INPUTS.json)
records proof, review, maintained-dependency and validation hashes.

## Promotion and concurrent work

Promotion has not been attempted or approved. Established book/code is
unchanged. Existing unrelated untracked study directories were preserved and
not used as scientific inputs. A metadata-only agent-list call unexpectedly
returned an unrelated completed status summary; it was not used in this
study's arguments, and the component review records the exposure.

## Bounded endpoint follow-up (2026-09-20)

The user subsequently requested a surgical attempt using the nominated newer
long-horizon studies, explicitly allowing comparison of the fitted whole-circle
predictors. [ENDPOINT_ROUTE.md](ENDPOINT_ROUTE.md) proves two complementary
statements for the unchanged canonical single-input tanh GF and H3 closure:

- The endpoint difference is the signed integral, over training prediction
  from zero to one, of their normalized current full tangent-kernel columns.
  A common kernel rescaling cancels. The actual coefficient Frobenius metric
  and all three trained gradient blocks are retained.
- A residual of size `alpha` leaves at most `T(m) alpha` whole-circle output
  travel, where `m` is the initial upper-feature squared norm and `T` is explicit.
  It is less than `22 alpha` for the exact flow and less than `25 alpha`
  for any closure with `m_N>=9/50`. Consequently, for that closure,

      endpoint whole-circle error <= error at physical time 40 + 1.7e-5.

This is a finite-horizon-to-endpoint transfer, not a computation of its unknown
finite-horizon discrepancy. The normalized-kernel identity isolates a sharper
quantity for understanding order than raw state error, but no new useful
algebraic/geometric rate in order, finite-width endpoint convergence, or numerical
quadrature certificate is claimed. A further exact identity selects the component
of the omitted middle-update source affecting normalized passive motion; its
effect on subsequent feature motion remains unbounded at a useful scale.

The most relevant nominated results concern the original GF's finite remaining
travel and its full evolving kernel. Landscape/fitting results alone do not
compare passive predictors, and modified optimizers need not select the same
endpoint. The single-input scope avoids transferring a p=1 reflection symmetry
to an arbitrary hierarchy dictionary or nonsymmetric two-input law.

Agent `endpoint_error_surgical` authored the route. The supervisor read its
complete proof and independently reconstructed the gradient metric and bounds;
fresh scoped agent `endpoint_internal_check` owns the internal check report.
Its [complete internal check](ENDPOINT_INTERNAL_CHECK.md) accepts the final
candidate, including the time-40 corollary; the supervisor read the complete
report and verified its final input hashes. This is internal research checking,
not the promotion gate. [ENDPOINT_INPUTS.json](ENDPOINT_INPUTS.json) records
the follow-up's source and deterministic-output versions.
No training experiment or established-file edit was made. Exact arithmetic:

```text
python -B studies/single_input_closure_rate_20260920/validate_endpoint.py > data/generated/single_input_closure_rate_20260920/endpoint_check_01/exact_bounds_v2.log
```

Exit zero; checks cover the two tail constants, the time-40 exponential bound,
the positive nonprojector filter identity and cancellation of speed errors.
The earlier `exact_bounds.log` is preserved; the v2 output includes the added
time-40 check. The old `CHECK_INPUTS.json` describes the prior frozen result,
not this expanded README or the follow-up. Promotion remains unattempted.

## Quantitative order follow-up (2026-09-20)

The user correctly distinguished endpoint transfer from a rate in order and
requested an actual asymptotic insight. The continuation therefore targets
error production as retained information increases, in the same single-input
investigation. No additional empirical campaign or promotion is authorized.

The new candidate results are:

- [TAME_GATE_RATE.md](TAME_GATE_RATE.md) proves the global sensitivity bound
  `0<partial_g J(g,V)<=1+2|V|` for the exact inverse gate. It replaces the
  old exponential-in-cutoff compiler bound by a polynomial one, while leaving
  the canonical closure and its numeric order unchanged.
- [ORDER_RATE_INVERSION.md](ORDER_RATE_INVERSION.md) consequently proves
  `sup_(t>=0,u)|f_N-f| <= 2^433448 (log2 log2 N)^(-1/28)` whenever
  `log2 log2 log2 N>=28*433448`. This is a named asymptotic upper bound in
  the **actual finite maintained order**, including the whole circle and
  fitted endpoints. Constants are impractical and the exponent is not sharp.
  Raw retained counts grow as `N^4/24` in total, and coefficient-matrix size
  as `N^6/48`, so these conventions for size preserve the same rate class.
- [ORDER_TAIL_STRUCTURE.md](ORDER_TAIL_STRUCTURE.md) proves that projecting
  onto r successive forward/reverse action generations omits a source bounded
  by a fixed constant times `A^r/r!`. The corresponding autonomous projected
  flow has the same all-time prediction bound. This auxiliary result retains
  a whole sigma-field at each generation; it is **not** a factorial error
  bound for finite maintained order N. Its proof uses Picard integral
  iterations, not convergence of time Taylor series.

Together these separate the dynamical suppression of deep action generations
from the cost of approximating functions in them by a finite dictionary.
Polynomial refinement of the fixed initial Gaussian core alone still has the
previously proved nonzero global error floor. No sharp low-order accuracy,
monotonic error ordering, finite quadrature guarantee or finite-width all-time
limit follows from any of these statements.

The supervising task owns `TAME_GATE_RATE.md` and the validation script.
Fresh scoped routes `order_rate_inversion` and `order_tail_structure` own
their respective proofs. They began from separate assigned inputs; the root's
concrete inverse-gate lemma was then shared with both, and the rate route used
it. Agent `order_rate_internal_check` owns the independent internal check.
All work stays in this study and its generated namespace. Exact arithmetic:

```text
python -B studies/single_input_closure_rate_20260920/validate_order_rates.py > data/generated/single_input_closure_rate_20260920/order_rate_check_01/exact_bounds.log
```

Exit zero. The script checks the Bernstein margin, constant exponents,
squaring-recurrence majorants and Picard constants without allocating the
astronomical thresholds. These checks support, rather than replace, the
analytic proofs. No training experiments were run.

The [independent internal check](ORDER_RATE_INTERNAL_CHECK.md) passes the new
gate, finite-order inversion and factorial action-generation chain. The
supervisor read all three complete proofs and the complete report, checked
their composition, and verified the version hashes recorded in
[ORDER_RATE_INPUTS.json](ORDER_RATE_INPUTS.json). The report explicitly
preserves the inherited canonical Gaussian source rule and rational fitting
certificate as dependencies; this is not a fresh whole-book or numerical-code
audit. It also records an incidental read of a neighboring maintained section.
These are internally checked study results, not promoted material. The old
proofs and their original threshold formula remain preserved; the new compiler
and inversion give a strictly improved sufficient order bound.

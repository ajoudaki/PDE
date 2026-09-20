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
with their designated reproduction inputs. Other studies are excluded.
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

The next substantive research question, if requested, is a useful rate in
the retained action information, rather than the current exhaustive-code
worst-case bound. No new experiment or extension is automatically authorized
by this completed result.

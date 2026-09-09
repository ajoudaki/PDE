# Canonical high-order successor

This directory contains the bounded exact successor that extends the canonical
one-input quadratic feature jet from order thirteen through order seventeen.
The accepted result is summarized in [RESULTS.md](RESULTS.md): two isolated
exact recurrences agree on $F^{(15)}(0)$ and $F^{(17)}(0)$, and exact
series inversion gives $\mu_6,\mu_7$ together with positive-definite
$H_3$ and $H_3^+$.

The claim is deliberately finite-order.  It establishes compatibility of the
first eight canonical moments with the Stieltjes conditions; it does not prove
the all-order moment property, a positive-time width limit, determinacy, or
identification with the neural loss curve.  The frozen protocol ended at
order seventeen, and no order-nineteen computation was attempted.

## Artifact map

- [PROTOCOL.md](PROTOCOL.md) is the protocol frozen before either new
  derivative was computed.
- [RESULTS.md](RESULTS.md) is the compact authoritative result and scope
  statement.
- [production_canonical_recurrence.py](production_canonical_recurrence.py)
  is the production scalar specialization of the proved Gaussian-program
  recurrence.
- [PRODUCTION_RESULT.json](PRODUCTION_RESULT.json) binds the production
  source and frozen order-thirteen inputs and retains its exact jet,
  checkpoints, resource use, cache sizes, and arithmetic diagnostics.
- [independent_canonical_recurrence.py](independent_canonical_recurrence.py)
  is an isolated implementation with a different sparse-monomial and Wick
  engine.
- [INDEPENDENT_RECURRENCE_AUDIT.md](INDEPENDENT_RECURRENCE_AUDIT.md) explains
  the independent recurrence, dependency cuts, prefix gate, and resources.
- [INDEPENDENT_RESULT.json](INDEPENDENT_RESULT.json) retains its exact jet,
  commands, checkpoints, and resource measurements.
- [moment_hankel_audit.py](moment_hankel_audit.py) performs exact direct
  coefficientwise series reversion and enumerates every available principal
  minor.
- [F15_MOMENT_HANKEL_AUDIT.json](F15_MOMENT_HANKEL_AUDIT.json) retains the
  order-fifteen moment and ordinary $H_3$ certificate.
- [F17_MOMENT_HANKEL_AUDIT.json](F17_MOMENT_HANKEL_AUDIT.json) retains the
  complete eight-moment prefix and shifted $H_3^+$ certificate.
- [NOTES.md](NOTES.md) gives the exact affine order-fifteen and
  order-seventeen Hankel gates.

## Reproduction

The exact downstream audit is inexpensive:

```bash
python moment_hankel_audit.py \
  --f15 49079184579077107476764629402991788032 \
  --f17 30555969894096099495444855650521777374167040
```

The independent recurrence can be rerun under the frozen cap with:

```bash
python independent_canonical_recurrence.py \
  --max-order 17 --progress \
  --wall-cap-seconds 1800 --memory-cap-mib 8192
```

The production recurrence uses the same cap:

```bash
python production_canonical_recurrence.py \
  --max-order 17 --progress \
  --wall-cap-seconds 1800 --memory-cap-mib 8192
```

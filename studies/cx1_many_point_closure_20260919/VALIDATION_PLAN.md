# Bounded C-X1 implementation validation

Declared before execution, 2026-09-19. This checks the new dimension-general
closure implementation, not a full neural network or an empirical proof of
the theorem. No fitted trajectory supplies its coefficients.

Five deterministic float64 runs use d=m=3, labels (+1,-1,+1), uniform
weights, horizon 15, covariance regularizer 1/1000, and initialization from
the generic joint Gaussian compiler. The reference inputs are the three
coordinate directions.

| Run | Order | Coefficient nodes Q | Population nodes P | Heun steps |
| --- | ---: | ---: | ---: | ---: |
| reference_o1 | 1 | 256 | 64 | 1500 |
| reference_o3 | 3 | 256 | 64 | 1500 |
| reference_o3_time | 3 | 256 | 64 | 3000 |
| reference_o3_integration | 3 | 512 | 128 | 1500 |
| perturbed_o3 | 3 | 256 | 64 | 1500 |

The final run uses u1=(399,40,0)/401, u2=e2, u3=e3. Its displacement is
NOT asserted to lie inside the theorem's as-yet unevaluated radius. It
checks that the same solver operates on nonorthogonal data. It supports no
theoretical neighborhood-size or accuracy claim.

Record loss, paired layer RMS, fixed passive predictions, time, retained
state size, and peak process memory. Every run compares a direct continuation
against a serialized own-state restart at the midpoint; equality must be
bitwise. States/predictions must stay finite and storage shapes unchanged.
Report time/integration differences without imposing a posterior tolerance
or treating them as a certificate. Order comparisons are descriptive only.
The existing six semantic tests supply independent gradient/adjoint and
rational-arithmetic checks; no additional precision sweep is needed here.

Limits: one process, one numerical thread, 360 seconds aggregate, 512 MiB
address-space cap. Stop on the first failed criterion, numerical exception,
or limit. No automatic enlargement or rerun search. All runs, including any
failure, are preserved under a fresh study-owned generated directory.

Reproduce from repository root:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH=code \
python -B studies/cx1_many_point_closure_20260919/validate_trajectories.py \
--output data/generated/cx1_many_point_closure_20260919/operational_01
```

The driver records its exact configuration, input source hashes, command,
environment, result and output hashes. Generated outputs are not unique
proof dependencies and are not committed.

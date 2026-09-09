# Compiler audit: L=2, B=1 first nonlinear correction

**Date:** 2026-08-18  
**Scope:** implementation and special-case audit only; this file does not
certify the finite-width-to-mean-field probability theorem.

## Exact gates

The exact polynomial Wick evaluator applied to the emitted 17-atom DAG gives

| activation | `q0` | `A` | `C` |
|---|---:|---:|---:|
| (2) | 1 | 4 | 0 |
| (x) | 1 | 3 | 48 |
| (x) | general | (3q_0) | (48q_0^2) |
| (1+x) | 1 | 6 | 112 |
| (x^2) | 1 | 111 | 1,685,184 |
| (x^3) | 1 | 305,775 | 154,118,008,098,000 |

The cubic gate activates every derivative through order three. For (x^2),
the independent generic finite-width Taylor propagator agrees
seed-by-seed through order three with the pre-existing quadratic reference,
not merely after ensemble averaging. For (x), the independent raw-coordinate
calculation proves the finite-width identity

\[
\mathbb E[D_n^3f_n]=48+60/n.
\]

The full test command is

```bash
python - <<'PY'
from studies.mean_field_peeling.generic_first_stieltjes.compiler import test_normal_form, test_finite_width_jet
for module in (test_normal_form, test_finite_width_jet):
    for name in sorted(n for n in dir(module) if n.startswith('test_')):
        getattr(module, name)()
print('ALL TEST FUNCTIONS PASSED')
PY
```

It passed all twelve test functions on 2026-08-18.

## Exact finite-width two-route identity

`finite_width_contraction.py` independently implements equations
(3.1)--(3.10) of `PEELING_AND_PROBABILITY_LEDGER.md`. It directly forms
`zeta`, `sigma`, `tau`, the differentiated backward vector, the straight-line
third derivative, and all three Hessian-square blocks. It does not import the
Taylor propagator.

For a shared initialization, its scalar

```text
2*T_n + 4*(H_a,n + H_W,n + H_u,n)
```

equals `feature_jet(...).derivatives[3]` seedwise for:

- widths 1, 2, 5, and 9;
- seeds 0, 3, and 17;
- linear, affine, quadratic, cubic, sine, and tanh activations.

The same equality passes for affine, sine, and tanh at nonunit metrics
`q0=0.25` and `q0=2.5`. This checks the exact finite-width scalar encoding and
all explicit `q0` powers independently of the Gaussian-limit calculation.

## Deterministic quadrature gates

Tensor Gauss--Hermite evaluation of the literal atoms gives, for (q_0=1),

| activation | quadrature order | `A` | `C` | `C/(2A^2)` |
|---|---:|---:|---:|---:|
| sin | 64 | 1.000000000000000 | -1.886999827305931 | -0.943499913652965 |
| tanh | 160 | 0.783049566725857 | -1.746872139497285 | -1.424467731336440 |

Increasing the tanh rule to order 256 changed (C) to
(-1.746872162134656). The order-160 value is therefore retained only to the
tolerance used in the automated quadrature regression.

These negative values are important: the algebraic first correction exists,
but it is not automatically a nonnegative Stieltjes moment for a generic
smooth activation.

## Exploratory finite-width audit

This panel was run as an implementation audit, not a preregistered decisive
experiment. Exact finite-width jets were averaged independently at each width.
The reported uncertainty is one ordinary standard error and includes no
finite-width bias correction.

Commands:

```bash
python -m studies.mean_field_peeling.generic_first_stieltjes.compiler.audit_monte_carlo \
  --activation sin --widths 16,32,64 --seeds 4096,2048,1024 \
  --seed-offset 0 --quadrature-order 64

python -m studies.mean_field_peeling.generic_first_stieltjes.compiler.audit_monte_carlo \
  --activation tanh --widths 16,32,64 --seeds 4096,2048,1024 \
  --seed-offset 10000 --quadrature-order 160
```

Results for (F'''(0)):

| activation | target (C) | (n=16) | (n=32) | (n=64) |
|---|---:|---:|---:|---:|
| sin | -1.8869998 | -2.1513 ± 0.1067 | -1.8839 ± 0.0781 | -1.8237 ± 0.0720 |
| tanh | -1.7468721 | -1.9837 ± 0.1054 | -1.8070 ± 0.0949 | -1.7463 ± 0.0788 |

The width-64 means lie within one standard error of the emitted GNF targets.
This supports the implementation and detects the sign, but it does not prove
convergence, determine its rate, or close the response-channel theorem.

## Structural audit gates

- `emit_l2_b1.py --format summary` reports exactly 17 unique atoms for
  ((A,C)); every covariance is explicit and every surviving atom is
  one-dimensional.
- The maximum activation derivative order is three.
- The two response terms that a naive independent-Gaussian substitution would
  delete are represented algebraically by the (q_0d_1) part of
  (c=q_1+q_0d_1) and by the nested response
  (d_2+b_2+c(r_2+s_2)).
- The independent analytic derivation and the canonical note agree
  atom-for-atom: its (T_\star) satisfies (S_\star=3T_\star), so both emit
  (C=2S_\star+4H_\star=6T_\star+4H_\star).

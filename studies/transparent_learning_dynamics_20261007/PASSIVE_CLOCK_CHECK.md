# Passive cubic-clock coefficient check

2026-10-07. Initialization-only deterministic Gaussian quadrature.

## Frozen design, before execution

Evaluate \(k_1+s k_2\) and \(\kappa_{3,s}\) for unit label directions
\((1,s)\), \(s=-1,+1\), using equations (10), (14), and (15) of
ANALYTICAL_LEARNING_PROFILES.md. No trained trajectory or later-time fit
is an input.

The numerical question is whether deterministic refinements stably
resolve those four coefficients. This is not a test of their later-time
predictive accuracy or of a global approximation theorem.

Use tensor Gauss--Hermite orders 24, 40, 64, and 96. Lower expectations
are two-dimensional, and the upper correlated Gaussian expectations
are three-dimensional. Stream the latter one slice at a time.
At the highest order repeat with fixed orthogonal coordinate rotations
in both populations. The initial upper covariance uses the nonlinear
first-layer Gram, not a linear formula for the passive upper field.

Pass the six-decimal freeze gate if every target changes by at most
\(10^{-7}\) both under final order refinement and under coordinate
rotation. Additional checks: positive upper covariance, normalized
quadrature weights, and agreement of the training cubic coefficient and
cross-feature coefficients with their independent scalar formulas.

If the order-96 gate fails and elapsed compute time is below 35 seconds,
the sole permitted resolution branch is order 128 in both coordinate
systems. Otherwise stop as inconclusive. A gate failure is numerical
inconclusiveness, not evidence against the analytic formula.

Hard limits: one single-thread process, at most 60 seconds CPU/wall
budget and 512 MB address space; soft wall stop 55 seconds.
No seeds, trajectories, fitted parameters, or exploratory grid.

## Result: numerical refinement PASS

The following coefficients were frozen before the lead's subsequent
dense-trajectory comparison:

| Unit label direction | \(k_1+s k_2\) | \(\kappa_{3,s}\) |
|---|---:|---:|
| \((1,-1)\) | 0.109231031201 | 0.103459101946 |
| \((1,+1)\) | 0.303835390402 | 0.183394342628 |

Six decimal places pass the preregistered numerical gate. Additional
digits are recorded for reproducibility, not as a rigorous error interval.
The predictive formulas are
\[
f_3^{(-)}(u)\simeq0.109231031201\,u+0.103459101946\,u^3,
\]
\[
f_3^{(+)}(u)\simeq0.303835390402\,u+0.183394342628\,u^3.
\]
The actual label magnitude enters the separately specified clock
\(\dot u=Y-\nu u-\kappa u^3\), not these unit-direction coefficients.
At order 96, \(\nu=0.236450410504\) and
\(\kappa=0.181152636696\).

The largest target change from order 64 to 96 was \(3.2761\,10^{-8}\).
The largest order-96 coordinate-rotation discrepancy was
\(2.7717\,10^{-10}\). No order-128 branch was triggered.
The opposite-label cubic coefficient, the least quickly converging
target, was

| Order | \(\kappa_{3,-}\) |
|---|---:|
| 24 | 0.103527161120 |
| 40 | 0.103461543448 |
| 64 | 0.103459134706 |
| 96 | 0.103459101946 |

The smallest upper-covariance eigenvalue was \(0.00979644\).
Realized Gaussian covariance error was \(2.3\,10^{-16}\) or smaller.
The training coefficient identities disagreed by at most
\(5.6\,10^{-17}\) in the ordinary coordinates and \(9.2\,10^{-10}\)
after rotation. The quadrature construction normalizes each Gaussian
rule and enforces the known exact equal variances and zero training
cross covariance; the unused raw lower variance discrepancy was
\(1.2\,10^{-11}\).

The passive cubic coefficient also separates numerically into the same
three initialization-only terms as the analytic formula:

| Direction | Learned middle matrix | Lower Gaussian return | Lower reaction alignment |
|---|---:|---:|---:|
| Opposite | 0.032421995138 | 0.038915473199 | 0.032121633609 |
| Equal | 0.067436601784 | 0.075598187683 | 0.040359553161 |

These are an algebraic decomposition of the full coefficient, not
predictions for ablated systems without recomputing their own laws.

## Reproduction and provenance

Command:

    timeout 60s python studies/transparent_learning_dynamics_20261007/passive_clock_quadrature.py --output data/generated/transparent_learning_dynamics_20261007/beyond_initialization_v1/passive_quadrature

The script refuses to overwrite an existing output directory. It sets
all relevant numerical thread counts to one and applies a 512 MB
address-space limit and 60-second CPU limit.
Measured calculation time was 0.358 seconds; process peak RSS was
53.78 MB. The whole command completed in 0.443 seconds.
Environment: Python 3.10.12, NumPy 1.26.4, SciPy 1.13.0.

The full order-by-order matrices, coefficient decompositions, covariance
checks, source hashes, and environment are in
data/generated/transparent_learning_dynamics_20261007/beyond_initialization_v1/passive_quadrature/coefficients.json.

- Script SHA-256:
  a3b47d2fd026c45ca4b00e4c8006ffe332aa04c3c28ea10cf0760fa741d8feb1.
- Initialization-formula note SHA-256:
  a6d454fc98c53de44b5bc989469649dcba671fa0b1717c02dddfa341ba5351a0.
- Raw result SHA-256:
  28ee2042e0c73b721a6a46aa935b8ef6782653e17454f72ccc268af375222e8a.

The script has no trained-trajectory input. No passive output, late-time
coefficient, or fitted nuisance parameter was used. This PASS concerns
deterministic numerical refinement of initialization integrals only.
It is not interval-arithmetic certification of their absolute error,
and it does not establish accuracy of the cubic passive clock on a
trained trajectory.

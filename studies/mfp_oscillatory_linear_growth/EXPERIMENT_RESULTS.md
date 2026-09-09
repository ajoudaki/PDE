# Scalar proxy scan results

The preregistered proxy was run with `2^17` common Gaussian particles as a
pilot (smaller than the preregistered confirmatory size).  Therefore these
figures are mechanism evidence only.

At `rho=0.05`, the identity and `p=3` candidates had stable sample means
which decreased with the horizon.  For example:

| activation | `t` | mean fine-minus-coarse | 99.9%-trimmed mean | maximum absolute contribution |
|---|---:|---:|---:|---:|
| identity | 16 | `6.02e-5` | `5.81e-5` | `3.72e-3` |
| `p=3, lambda=.10` | 16 | `1.31e-4` | `9.28e-5` | `.292` |
| `p=3, lambda=.25` | 16 | `3.49e-4` | `1.79e-4` | `2.30` |

The `p=5` means were not statistically meaningful.  They were controlled
by one or a few observations while the trimmed mean stayed near zero:

| activation | `t` | ordinary mean | 99.9%-trimmed mean | maximum absolute contribution |
|---|---:|---:|---:|---:|
| `p=5, lambda=.05` | 3 | `4.96e47` | `-7.62e-4` | `6.50e52` |
| `p=5, lambda=.10` | 2 | `-1.68e22` | `-2.47e-3` | `2.21e27` |
| `p=5, lambda=.10` | 12 | `2.18e62` | `-2.05e-4` | `2.86e67` |

This is evidence for catastrophic loss of uniform integrability, but it is
not evidence for the sign or magnitude of the exact Gaussian expectation.
Increasing the Monte Carlo sample size would expose still rarer events and
does not resolve the expectation without analytic tail control.  The pilot
therefore triggered the precommitted “rare-tail mechanism, no theorem”
outcome rather than a confirmatory large-sample run.


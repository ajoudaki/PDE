# Early-spike diagnostic: capped partial panel

Status: **inconclusive numerical route-selection evidence**.  This file is
not evidence for a width-limit theorem.

The frozen run was stopped once its ten-wall-minute cap had been exceeded.
Ten of the sixteen matched `(seed,width)` cases completed, each with the
primary and half-step RK4 integrations.  The script wrote its JSON artifact
only after the whole panel, so interruption left no full diagnostic file;
the emitted summaries are preserved below.  The stop occurred at about
638.6 seconds because the polling interval first returned after the nominal
600-second boundary.

| seed | width | max K | first f=0.10 | max primary/control f discrepancy | elapsed s |
|---:|---:|---:|---:|---:|---:|
| 31001 | 128 | 3.0078870977 | 0.0117693 | 5.2e-12 | 4.0 |
| 31001 | 256 | 2.8406372356 | 0.0243529 | 1.0e-11 | 9.5 |
| 31001 | 512 | 2.5057430780 | 0.0243957 | 5.0e-12 | 24.6 |
| 31001 | 1024 | 2.4258446550 | 0.0218413 | 3.6e-12 | 95.7 |
| 31002 | 128 | 2.3720018520 | 0.0405125 | 7.1e-12 | 99.7 |
| 31002 | 256 | 2.5513296340 | 0.0333725 | 7.4e-12 | 106.7 |
| 31002 | 512 | 2.3911854820 | 0.00912969 | 2.36e-12 | 183.9 |
| 31002 | 1024 | 2.4098348797 | 0.01629371 | 4.45e-12 | 588.8 |
| 31003 | 128 | 2.0948985439 | 0.03395392 | 3.05e-12 | 604.2 |
| 31003 | 256 | 2.1817601498 | 0.03308976 | 4.75e-12 | 638.6 |

Using only the two seeds having every width, the median maximum-kernel
values at widths 128, 256, 512, and 1024 are approximately

`2.68994, 2.69598, 2.44846, 2.41784`.

The two upper successive ratios are approximately `0.908` and `0.987`, both
inside the frozen barrier interval.  The corresponding median `f=0.10`
hitting times are approximately

`0.02614, 0.02886, 0.01676, 0.01907`,

whose upper ratios are approximately `0.581` and `1.138`.  They satisfy
neither the two-ratio spike criterion nor the barrier criterion.  Moreover,
the primary panel is incomplete and its full balance-law diagnostics were
not serialized.  The only valid preregistered verdict is therefore
**inconclusive**.


# FP64 n=8192 successive-proxy experiment

Status: **complete**. The experiment uses the validated one-input FP64
explicit-Euler engine, 16 whole antithetic lineages per configuration, step
size `1e-5`, seed `2026081407`, and physical output nodes
`(0.5, 0.75, 0.9, 0.95)`. The lineages, seeds, horizons, clock construction,
proxies, and bootstrap draws are matched to the retained n=4096 experiment.
No coefficient was derived or recomputed.

## Main n=8192 result

The central adjacent-order error sequences still **fail strict improvement
for all four configurations**, but the detailed pattern changes for V.

The aggregate error is

\[
E_r=\max_{y\in\{.5,.75,.9,.95\}}
\left|\log\frac{K_{M_r}(y)}{\widehat K_{8192}(y)}\right|.
\]

| configuration | M0 | M1 | M2 | M3 | M4 | M5 | central best |
|---|---:|---:|---:|---:|---:|---:|---|
| C | 0.39821 | 0.04393 | **0.01697** | 0.02038 | 0.01976 | 0.01988 | M2 |
| A | 0.75320 | 0.09751 | **0.01825** | 0.02939 | — | — | M2 |
| M | 0.42577 | 0.04750 | **0.01645** | 0.02033 | 0.01950 | — | M2 |
| V | 0.93465 | 0.11827 | 0.04549 | 0.02890 | **0.01758** | 0.02025 | M4 |

The 99% whole-lineage percentile intervals for the winning sup errors are C
`[0.00109, 0.04715]`, A `[0.01257, 0.04848]`, M
`[0.00118, 0.04679]`, and V `[0.00286, 0.04114]`.

For C, A, and M, M0 to M1 and M1 to M2 improve, M2 to M3 worsens,
and any later levels form a small alternating plateau. For V, the aggregate
error decreases centrally through M4 and then increases at M5. V therefore
still has a central sequence that fails strict all-order improvement, but its
central optimum is later than at n=4096.

## Nodewise absolute log errors

| C | y=.50 | y=.75 | y=.90 | y=.95 | sup |
|---|---:|---:|---:|---:|---:|
| M0 | 0.12303 | 0.26727 | 0.36488 | 0.39821 | 0.39821 |
| M1 | 0.02023 | 0.03028 | 0.03995 | 0.04393 | 0.04393 |
| **M2** | **0.01697** | **0.01647** | **0.01467** | **0.01388** | **0.01697** |
| M3 | 0.01721 | 0.01854 | 0.01971 | 0.02038 | 0.02038 |
| M4 | 0.01720 | 0.01840 | 0.01926 | 0.01976 | 0.01976 |
| M5 | 0.01720 | 0.01842 | 0.01934 | 0.01988 | 0.01988 |

| A | y=.50 | y=.75 | y=.90 | y=.95 | sup |
|---|---:|---:|---:|---:|---:|
| M0 | 0.28179 | 0.54267 | 0.70125 | 0.75320 | 0.75320 |
| M1 | 0.03415 | 0.06492 | 0.08895 | 0.09751 | 0.09751 |
| **M2** | **0.01825** | **0.00771** | **0.00663** | **0.01289** | **0.01825** |
| M3 | 0.02078 | 0.02419 | 0.02783 | 0.02939 | 0.02939 |

| M | y=.50 | y=.75 | y=.90 | y=.95 | sup |
|---|---:|---:|---:|---:|---:|
| M0 | 0.13462 | 0.28801 | 0.39081 | 0.42577 | 0.42577 |
| M1 | 0.02038 | 0.03206 | 0.04305 | 0.04750 | 0.04750 |
| **M2** | **0.01645** | **0.01567** | **0.01330** | **0.01223** | **0.01645** |
| M3 | 0.01677 | 0.01829 | 0.01961 | 0.02033 | 0.02033 |
| M4 | 0.01676 | 0.01810 | 0.01901 | 0.01950 | 0.01950 |

| V | y=.50 | y=.75 | y=.90 | y=.95 | sup |
|---|---:|---:|---:|---:|---:|
| M0 | 0.37781 | 0.69152 | 0.87511 | 0.93465 | 0.93465 |
| M1 | 0.03886 | 0.07999 | 0.10875 | 0.11827 | 0.11827 |
| M2 | **0.01219** | **0.00906** | 0.03461 | 0.04549 | 0.04549 |
| M3 | 0.01767 | 0.02245 | 0.02718 | 0.02890 | 0.02890 |
| **M4** | 0.01717 | 0.01758 | **0.01555** | **0.01413** | **0.01758** |
| M5 | 0.01726 | 0.01913 | 0.02011 | 0.02025 | 0.02025 |

Thus V is M2-best at the early nodes `.50` and `.75`, but M4-best at `.90`
and `.95`; M4 wins both the sup and mean aggregate metrics.

## Neural references and uncertainty

Every one of the 20,000 whole-lineage bootstrap draws covered the common
clock. The intervals below are 99% studentized max-|t| simultaneous log
bands.

| configuration | y=.50 | y=.75 | y=.90 | y=.95 |
|---|---:|---:|---:|---:|
| C | 125.531 [121.609, 129.581] | 145.009 [141.130, 148.996] | 159.877 [156.047, 163.802] | 165.296 [161.496, 169.186] |
| A | 79.530 [77.001, 82.142] | 103.236 [100.632, 105.907] | 120.976 [118.241, 123.774] | 127.428 [124.621, 130.298] |
| M | 223.100 [216.215, 230.205] | 260.086 [253.254, 267.102] | 288.245 [281.455, 295.199] | 298.499 [291.731, 305.423] |
| V | 53.621 [52.200, 55.082] | 73.380 [71.939, 74.850] | 88.168 [86.679, 89.683] | 93.577 [92.055, 95.124] |

For the aggregate sup error, the bootstrap probability that an adjacent step
improves is:

| transition | C | A | M | V |
|---|---:|---:|---:|---:|
| M0 to M1 | + (1.000) | + (1.000) | + (1.000) | + (1.000) |
| M1 to M2 | + (0.998) | + (1.000) | + (0.999) | + (1.000) |
| M2 to M3 | - (0.040) | - (0.173) | - (0.039) | + (0.927) |
| M3 to M4 | + (0.961) | — | + (0.964) | + (0.997) |
| M4 to M5 | - (0.041) | — | — | - (0.011) |

Here `+` and `-` are central signs and the parenthesized value is the
bootstrap probability of a positive improvement margin. V's M3-to-M4 margin
is resolved at 99% (`[0.00050, 0.01459]`); its favorable M2-to-M3 margin is
not (`[-0.01004, 0.04929]`).

## Paired n=4096 to n=8192 comparison

The two campaigns use the same 16 nested lineages and the same bootstrap
lineage multiplicities. Each width's common output clock is nevertheless
inverted separately inside every draw.

| configuration/level | error at 4096 | error at 8192 | paired change | 99% paired interval | P(error decreases) |
|---|---:|---:|---:|---:|---:|
| C M2 | 0.03556 | 0.01697 | -0.01859 | [-0.06447, 0.02191] | 0.866 |
| A M2 | 0.03159 | 0.01825 | -0.01334 | [-0.04955, 0.02402] | 0.710 |
| M M2 | 0.03441 | 0.01645 | -0.01795 | [-0.06511, 0.02025] | 0.876 |
| V M2 | 0.02915 | 0.04549 | +0.01634 | [-0.02670, 0.03062] | 0.220 |
| V M4 | 0.03284 | 0.01758 | -0.01526 | [-0.05025, 0.01607] | 0.871 |

The neural reference rises centrally at all 16 configuration/node cells by
about 1.07% to 2.24%. Higher proxies generally become closer while M0 becomes
farther; V M2 is the important exception at late nodes because the rising
neural curve moves beyond that lower proxy. However, **every 99% paired neural
shift and every 99% paired proxy-error change interval crosses zero**.

C, A, and M retain M2 as the central best level under both aggregate metrics.
V changes centrally from M2 to M4. At n=8192, bootstrap resamples select V M4
as the best sup-error level with probability 0.963 and as the best mean-error
level with probability 0.838. The paired probability that the identity of the
V best level differs across widths is only 0.547 for the sup metric and 0.649
for the mean metric, so the cross-width switch itself is not established at
99%.

## Interpretation

The doubled width generally strengthens the central accuracy of most accepted
higher proxies and reveals a later central optimum for V, but the central
sequences still do not show strict all-order successive improvement. C, A,
and M worsen centrally at M2 to M3; V worsens centrally at M4 to M5. The
result is two-width empirical evidence with paired lineage uncertainty, not a
width-limit extrapolation or a new Stieltjes theorem.

No discretization uncertainty is included: both widths use the same FP64
Euler step. No n=16384 or two-input branch was run.

## Execution and retained artifacts

All eight GPU blocks passed their numerical and resource gates. Block times
were C 147.62/156.23 s, A 207.55/211.55 s, M 100.22/101.02 s, and V
286.87/282.38 s. Total GPU execution time was 1493.44 s. Peak allocated GPU
memory was 3.409 GiB and peak host RSS was 1.670 GiB. Both V blocks remained
inside the 300-second cap.

- `RESULTS.json`: complete n=8192 analysis and exact provenance
- `nodewise_errors.csv`, `aggregate_errors.csv`, `transition_margins.csv`
- `proxy_curves.png`, `aggregate_errors.png`, `transition_margins.png`
- `WIDTH_COMPARISON.json`: paired n=4096/n=8192 analysis
- `width_nodewise.csv`, `width_aggregate.csv`, `width_transitions.csv`,
  `width_best_levels.csv`
- `width_reference_log_ratio.png`, `width_proxy_error_change.png`,
  `width_aggregate_change.png`

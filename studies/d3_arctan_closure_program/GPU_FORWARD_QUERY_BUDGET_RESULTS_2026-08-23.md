# GPU result: forward-query characteristic budget

**Run date:** 23 August 2026.  **Status:** the frozen formal-support rule
passed.  This is numerical evidence only.

## Outcome

The cumulative characteristic field
\[
 W_i(T)=\int_0^T |(G_2(t)\dot X_2(t))_i|\,dt
\]
was stable over widths \(256,512,1024,2048,4096\), through \(T=4\).
Every primary cell in the preregistration passed:

- the largest central log-width slope was \(0.007624\);
- the largest 95-percent upper slope endpoint was \(0.025182\);
- the largest median \(4096/256\) ratio was \(1.01617\);
- the largest median step-halving discrepancy was \(2.184\times10^{-5}\);
- the largest float32/float64 discrepancy was \(1.227\times10^{-7}\); and
- the largest static-plus-learned decomposition residual was
  \(1.572\times10^{-6}\), below the frozen dtype-specific thresholds.

There were no evidence-against cells.  Hence

\[
 \boxed{\text{formal empirical support: yes; empirical evidence against: no.}}
\]

## Representative values

At \(T=4\), the median full-field statistics across increasing widths were

| statistic | 256 | 512 | 1024 | 2048 | 4096 |
|---|---:|---:|---:|---:|---:|
| \(\|W\|_{8,n}\) | 1.7980 | 1.7897 | 1.8224 | 1.8166 | 1.8150 |
| \(\log\langle e^W\rangle_n\) | 1.2907 | 1.2863 | 1.2913 | 1.2923 | 1.2996 |
| 0.999 quantile | 2.8476 | 3.0201 | 3.0794 | 3.1429 | 3.1345 |
| coordinate maximum | 2.8699 | 3.1427 | 3.3375 | 3.4298 | 3.4768 |

The growing coordinate maximum is compatible with ordinary extreme-value
growth and did not produce growth in the empirical exponential statistic.
At the same horizon, the median static/learned eighth moments at width 4096
were \(1.6398\) and \(0.3942\), and their \(\lambda=1\) log-mean-exponential
statistics were \(1.0709\) and \(0.2708\).  This agrees with the exact bound
that makes the learned part endpoint-tail safe and identifies the static
forward action as the substantive term.

## Numerical checks

The main calculation used explicit midpoint, step \(0.01\), float32 state
evolution, and float64 aggregation.  The exact velocity
\[
 \dot X_2=D_2\{\|X_1\|_n^2B_2+G_1D_1^2Q_1\}
\]
was evaluated at midpoint states.  Common-draw \(h=0.005\) runs at widths
256 and 512 and common-draw float64 runs at widths 128 and 256 passed all
frozen tolerances.  Raw arrays and the complete 4000-replicate-bootstrap
analysis are in `gpu_forward_query_results/` and
`GPU_FORWARD_QUERY_BUDGET_RESULTS_2026-08-23.json`.

## Claim boundary

This run samples ordinary coordinate tails and cannot exclude a much rarer
width-dependent localization event.  More importantly, the proof needs a
*conditional*, jointly rerun row/column-cavity exponential estimate, whereas
the statistic above is unconditional on the full trajectory.  The result
therefore supports the coupled forward/transpose route and rejects no theorem
alternative, but it does not prove the forward-query lemma or any rung of the
frozen contract.

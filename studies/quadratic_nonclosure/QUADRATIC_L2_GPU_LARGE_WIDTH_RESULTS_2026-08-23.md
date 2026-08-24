# Quadratic L2 GPU large-width ladder: results

**Date:** 23 August 2026.

## Qualified outcome

The preregistered GPU experiment records:

> **evidence for a resolved positive-time scale, not a visible shrinking
> boundary layer.**

Across the 16-fold extension from width 2048 to 32768, median hitting times
change by only 2.6% to 4.7%, are not monotone with width, and have fitted
log-log slopes near zero. This does not prove that the infinite-width hitting
time has a positive limit, but it gives no numerical indication that it is
collapsing toward zero on the accessible ladder.

## Frozen experiment

- exact quadratic activation phi(v)=v^2/2;
- exact simultaneous metric-gradient update in the original parameters;
- widths 2048, 4096, 8192, 16384, 32768;
- six independent keys at every width;
- paired steps 0.000625 and 0.0003125;
- float64 on two RTX 3090 GPUs;
- 60 trajectories in 30 paired bundles;
- no clipping, normalization, regularization, or planted extremes.

The non-scientific qualification passed before launch. NumPy-versus-GPU
field errors were at most 1.6e-15, updates agreed exactly at the recorded
precision, both devices replayed bit-for-bit, and the width-32768 state used
8.03 GiB.

## Numerical validity

Every frozen gate passed:

- all coarse and fine trajectories were finite and crossed f=0.95;
- the 95th-percentile paired curve error was 0.00212 to 0.00285, below 0.01;
- the largest median paired threshold-time discrepancy was 1.44e-4, below
  0.001;
- every recorded fine-step loss increment was negative;
- the median normalized one-step flow defect was 0.00163, below 0.01;
- peak Torch allocation was 8.035 GiB, below the 18 GiB cap.

The raw file contains all 30 unique bundles, six at each width and 15 from
each GPU, with no error or timeout record.

## Hitting-time scaling

The table uses the fine-step seed medians and the frozen 5000-resample
bootstrap.

| q | tau at n=2048 | tau at n=32768 | endpoint ratio | log-log slope | bootstrap 95% interval |
|---:|---:|---:|---:|---:|---:|
| .25 | .05635 | .05368 | .9526 | -.0212 | [-.0490, .0135] |
| .50 | .07945 | .07701 | .9694 | -.0157 | [-.0397, .0125] |
| .75 | .09695 | .09445 | .9742 | -.0137 | [-.0302, .0115] |
| .90 | .11180 | .10874 | .9726 | -.0132 | [-.0245, .0113] |

None of the four median sequences is strictly decreasing over the last four
widths. All endpoint ratios, slopes, and confidence intervals satisfy the
frozen positive-time-scale criteria. None comes close to the registered
shrinking-boundary-layer thresholds.

At the registered early time t=0.005, median predictors are:

| n | 2048 | 4096 | 8192 | 16384 | 32768 |
|---:|---:|---:|---:|---:|---:|
| median f(0.005) | .01187 | .01619 | .02699 | .01877 | .01545 |

The sequence is nonmonotone and remains far below the 0.75 early-jump
threshold.

## Seedwise and tail audit

The absence of shrinkage is not an artifact of reporting only medians. For
q=0.25, seedwise hitting times range from [.04662,.06365] at width 2048 and
[.05332,.05630] at width 32768. For q=0.90 they range from
[.09497,.11869] and [.10685,.11213], respectively. The fastest observed
large-width seeds are not faster than the fastest width-2048 seeds.

Gaussian extremes do grow with width. For example, the median initial
max-absolute readout mark grows from 3.70 to 4.33. Nevertheless, the median
largest-coordinate fraction of the readout kernel falls

- initially from 0.0301 to 0.00316;
- maximized before f=0.75 from 0.0778 to 0.0188.

Thus the measured extreme coordinates do not condense the empirical kernel
or create rare rapidly training trajectories on this ladder.

## Kernel scaling

The median initial tangent kernel changes from 1.628 at width 2048 to 1.746
at width 32768: endpoint factor 1.072 and slope 0.0267. The median maximum
kernel before f=0.75 changes from 26.418 to 26.505: factor 1.0033 and slope
0.00325. Both comfortably pass the frozen stability criteria.

## Relation to the earlier CPU experiment

The new independent GPU ensemble reproduces the previous width-2048 time
scale. The earlier fine CPU medians for q=.25,.50,.75,.90 were
.05621,.08136,.10019,.11586; the new GPU medians are
.05635,.07945,.09695,.11180. This is a useful backend and ensemble bridge,
not an exact paired-seed comparison.

## Runner-status disclosure

The parent wrapper printed a nonzero final status because its cleanup block
sent SIGTERM to one worker after receiving that worker's done sentinel but
before its queue feeder process had exited. All 30 bundles and both done
sentinels had already been received. The immutable raw data are structurally
complete; the precise causal adjudication is recorded separately. No rerun
or raw-file edit was made.

## Scope

This experiment rules against a **visible** width-driven collapse over
2048 to 32768. It does not establish compact-uniform mean-field convergence,
well-posedness, or a strictly positive limiting hitting time. A much slower
tail mechanism appearing only at vastly larger widths remains logically
possible, although this experiment supplies no positive evidence for it.

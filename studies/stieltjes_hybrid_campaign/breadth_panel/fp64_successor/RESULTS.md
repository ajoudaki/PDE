# FP64 explicit-Euler local qualification — terminal result

**Status:** accepted local-method pass on 17 August 2026.

The separately frozen FP64 successor completed its one authorized GPU
preflight and the serial A → M → V local qualification.  Independent
read-back from the retained raw arrays reproduced every decision: all 20
registered gates passed for each configuration.  No tolerance was relaxed,
no step was changed, and no attempt was repeated.

## Scope

This experiment changed one axis of the stopped FP32 breadth validation.  It
regenerated the exact frozen FP32 initial tensors and monitor coordinates,
cast `a`, `W`, and `u` exactly to FP64, and then evolved the same width-4096
antithetic lineage with explicit Euler at `h=2e-5` and `h=1e-5`.  It retained
the seed, horizons, output clock, observables, update diagnostics, and original
gates.

The result qualifies these three fixed-step FP64 Euler witnesses.  It does
not retroactively repair the failed FP32 runs, provide a width extrapolation,
compare NTK/M1/M2 against a neural confidence band, or add Stieltjes evidence.

## Preflight

The one-shot deterministic replay passed on `cuda:0`, an NVIDIA GeForce RTX
3090 with UUID `dca1675a-2081-5d8c-d5d6-8ec5dc75b44e`.  PyTorch was
`2.9.0+cu130`, CUDA was `13.0`, TF32 was disabled, deterministic algorithms
were enabled, and the FP64 initialization contract was verified.  Peak GPU
allocation was 0.0314 GiB.

## Decisive results

All discrepancies below are symmetric relative differences.  Percentages are
reported only for readability; the JSON artifacts retain the full values.

| configuration | max coarse/fine $K_{\rm eff}$ | max coarse/fine $Q_2$ | fine min sampled-$W$ cosine | fine max driver defect | decision |
|---|---:|---:|---:|---:|---|
| A: centered activation, $c=1$ | $0.0219707\%$ | $0.0117275\%$ (diagnostic) | $0.9999999999999996$ | $0.0203976\%$ | pass |
| M: relative metric, $\lambda=2$ | $0.0409925\%$ | $0.0200449\%$ (gated) | $0.9999999999999996$ | $0.0310565\%$ | pass |
| V: variance, $v=1/2$ | $0.0175974\%$ | $0.0085563\%$ (diagnostic) | $0.9999999999999996$ | $0.0174403\%$ | pass |

The frozen ceilings were `0.20%` for coarse/fine effective kernel, `0.20%`
for M's $Q_2$, `0.20%` for maximum driver defect, and `.995` for the sampled
middle-weight cosine.  Every readout/hidden update cosine was within
$7\times10^{-16}$ of one; every update-norm ratio was within
$2.6\times10^{-11}$ of one.  The maximum unchanged-coordinate fractions were
diagnostics only: $1/4096$ for A's readout, $1/4096$ for M's readout, and
$1/4096$ for V's readout and sampled middle weights.

The complete gate inventory also passed exact initialization/monitor hashes,
finite and positive arrays, component sums, mean-output and loss monotonicity,
driver RMS and cumulative defects, deterministic mode, per-point resources,
pair wall/GPU time, and all `a/u/W` ratio bounds.

## Resources and provenance

| group | recorded GPU-seconds | peak GPU GiB | peak host GiB |
|---|---:|---:|---:|
| A | 10.8985 | 0.8766 | 1.1005 |
| M | 6.2963 | 0.8762 | 1.0999 |
| V | 13.6824 | 0.8768 | 1.1009 |
| **total** | **30.8773** | — | — |

The stage ceiling was 270 GPU-seconds.  The frozen source-bundle digest is
`f370634a440210b13e6c3035840b7a24581223147b0f347a86c1daea891b3e9e`;
the source-lock digest is
`5f1bd2b4160eac4508e2fe34d39c7df6f44187100e1beaa650cbe9c208cd0ea6`.
The authoritative machine-readable decision is
[`LOCAL_QUALIFICATION_RESULT.json`](LOCAL_QUALIFICATION_RESULT.json), which
binds the unlock, preflight, attempt ledger, group results, watchdog records,
and six raw-array hashes.

## Interpretation and branch decision

Because the FP64 successor preserved the FP32-rounded initial state and all
other tested mechanics, the disappearance of the update-cosine and driver
failures is strong evidence that the stopped A/V failures were caused by the
FP32 update-rounding floor over this local validation scope.  It is not an
all-width or continuous-time theorem.

The preregistered next decision is therefore
`eligible_for_separate_authorization`: a replicated FP64 breadth screen at
widths 4096 and 8192 may now be designed and separately unlocked.  It was not
launched by this experiment.

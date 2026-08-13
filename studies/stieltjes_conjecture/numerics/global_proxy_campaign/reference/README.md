# Canonical finite-width reference engine

This directory contains the validation-gated simulator for the global proxy
campaign.  The original frozen Stage-2 pilot is closed inconclusive after its
precommitted horizon could not reach the last output node; it produced no NPZ
or accepted curve.  See `../FAILED_STAGE2.md`.  Successor 01 was rejected
before execution.  Successor 02 then passed CPU and both-GPU validation, was
hash-authorized, ran exactly once, and completed all five registered points.
Its frozen offline analysis was inconclusive, so the larger-width and
parameter-family neural branches were not authorized.  The terminal account
is [`../RESULTS.md`](../RESULTS.md).

## Two deliberately separate reference modes

For

\[
z=n^{-1/2}Wu^2,
\qquad
f=n^{-1}\sum_i a_i z_i^2,
\qquad
K_n=n\lVert\nabla f\rVert^2,
\]

`canonical_model.py` evaluates the gradients and (K_n) analytically.

1. `physical` uses ordinary Gaussian initialization with antithetic readout
   signs and integrates the true squared-loss flow

   \[
   \dot\theta=2(1-f)n\nabla f.
   \]

   On the ensemble mean-output grid \(\bar f=y\), its exact finite-ensemble
   effective kernel is

   \[
   K_{\rm eff}(y)=
   \frac{\mathbb E_n[(1-f)K_n]}{1-\mathbb E_n[f]}.
   \]

   Raw per-realization outputs, kernels, weighted kernels, and losses are
   preserved, so this quotient is not approximated by a product of means.

2. `output_clock` first projects each readout by one rank so that (f(0)=0)
   exactly, then integrates

   \[
   \frac{d\theta}{dy}=\frac{n\nabla f}{K_n}.
   \]

   This is a variance-reduced sensitivity ensemble, not the ordinary Gaussian
   ensemble.  Its output-clock defect is a mandatory solver diagnostic.

Neither mode replaces the other.  Agreement under step refinement and width
increase is intended to be a later validity gate.  Any failure of that gate is
inconclusive rather than evidence for or against the Stieltjes conjecture.

## Numerical and resource safeguards

- Float64 is mandatory.
- Every point declares wall, batch-step, host-RSS, GPU-allocation, raw-array,
  state-amplitude, kernel-floor, and kernel-ceiling caps.
- The shell launcher adds an independent external `timeout`.
- A first invalid point stops the configuration; no unregistered branch is
  launched.
- Configurations must be direct children of `configs/`, and outputs are written
  only below `runs/` without overwriting a nonempty run.
- Scientific execution is mechanically locked.  The executed successor used
  `configs/FROZEN_SUCCESSOR_02.json`,
  `configs/FROZEN_SUCCESSOR_02_ANALYSIS.json`, and
  `PRODUCTION_UNLOCK.json`, which bind the exact protocol, configuration,
  analysis rules, and source-bundle hashes.  The one-attempt rule now keeps
  this branch closed.
- Raw `.npz` arrays are excluded from Git by the study-level `.gitignore`; JSON
  summaries and manifests retain source and result hashes.

The memory guard checks PyTorch allocations.  GPU driver/library allocations
outside PyTorch are not included, so the protocol must retain explicit
headroom below physical VRAM.  Host RSS uses Linux `ru_maxrss`, a process peak.

## Validation commands

Run the small CPU tests and smoke configuration:

```bash
python -m unittest discover -s studies/stieltjes_conjecture/numerics/global_proxy_campaign/reference/tests -v
studies/stieltjes_conjecture/numerics/global_proxy_campaign/reference/run_capped_reference.sh cpu-validation
```

The two GPU validation configurations contain only tiny smoke trajectories and
are not scientific seeds.  Their preflight command was:

```bash
studies/stieltjes_conjecture/numerics/global_proxy_campaign/reference/run_capped_reference.sh gpu-preflight
```

The final validation-v3 actions were run separately on both devices before the
successor-02 unlock was written.  The scientific command was the distinct
`successor-02` action.  It must not be rerun.

On 2026-08-13, a read-only audit outside the restricted task sandbox saw two
RTX 3090 devices with 24 GiB each and driver 580.65.06, mostly free.  Inside
the sandbox, `nvidia-smi` could not contact the driver and PyTorch 2.9.0+cu130
reported zero CUDA devices.  This split is why all CUDA commands are explicit
launcher actions intended for separately approved external execution.  Both
GPU validation-v3 configurations subsequently passed through that launcher.

## Completed validation and scientific attempt

The validation suite checks analytic gradients and kernel versus autograd,
the two exact output chain rules, antithetic and microcanonical initialization,
output-clock step refinement, the physical effective-kernel definition, the
production lock, fail-path telemetry, and global deadlines.  The bounded CPU
and both-GPU validation-v3 runs completed before authorization.

The successor-02 scientific run then completed all five points in 59.934
seconds, using 18,360 batch-integrator steps.  Peak recorded PyTorch GPU
allocation was 0.133 GiB and peak host RSS was 0.951 GiB.  Its producer record
is
[`runs/canonical_pilot_successor02_20260813/summary.json`](runs/canonical_pilot_successor02_20260813/summary.json),
and its frozen 2,000-resample interpretation is
[`analysis_result.json`](runs/canonical_pilot_successor02_20260813/analysis_result.json).
All trajectory-validity gates except the deliberately exact paired-initial-
array gate passed, but the conservative width-sensitivity interval was 82.67
times wider than the registered resolution ceiling.  The result is therefore
protocol-inconclusive, not contrary evidence.

The earlier bounded CPU smoke also recorded:

- ordinary physical mode reached mean output `0.0458086` with strictly
  positive sampled mean-output increments;
- microcanonical output-clock mode had maximum clock defect
  `1.93e-10` and maximum initialization output `3.89e-16`;
- neither validation point approached its state, kernel, memory, step, or wall
  cap.

Its compact machine-readable record is
[`runs/reference_validation_cpu_20260813/summary.json`](runs/reference_validation_cpu_20260813/summary.json).
It explicitly marks `scientific_evidence_admissible: false`.

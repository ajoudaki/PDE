# Canonical finite-width reference engine

This directory contains the validation-gated simulator for the global proxy
campaign.  The original frozen Stage-2 pilot is closed inconclusive after its
precommitted horizon could not reach the last output node; it produced no NPZ
or accepted curve.  See `../FAILED_STAGE2.md`.  A separately named successor
is frozen but remains locked until its revised source bundle passes validation
and receives a matching unlock.

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
- Scientific execution is mechanically locked.  It requires a frozen
  `configs/FROZEN_PRODUCTION.json` and `PRODUCTION_UNLOCK.json` binding the
  exact configuration hash and source-bundle hash.  Neither file exists at
  this validation stage.
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
are not scientific seeds.  Before either is allowed, run the read-only/tiny-
allocation preflight outside the restricted sandbox:

```bash
studies/stieltjes_conjecture/numerics/global_proxy_campaign/reference/run_capped_reference.sh gpu-preflight
```

Then, if the preflight passes, run `gpu0-validation` and `gpu1-validation`
separately.  Do not run `production` until the campaign protocol has been
frozen and the hash-bound unlock has been reviewed.

On 2026-08-13, a read-only audit outside the restricted task sandbox saw two
RTX 3090 devices with 24 GiB each and driver 580.65.06, mostly free.  Inside
the sandbox, `nvidia-smi` could not contact the driver and PyTorch 2.9.0+cu130
reported zero CUDA devices.  This split is why all CUDA commands are explicit
launcher actions intended for separately approved external execution.  The
GPU smoke configurations have not been run.

## Completed CPU validation

The six CPU unit tests pass: analytic gradients and kernel versus autograd,
the two exact output chain rules, antithetic and microcanonical initialization,
output-clock step refinement, the physical effective-kernel definition, and
the production lock.  The bounded two-point CPU smoke run also completed:

- ordinary physical mode reached mean output `0.0458086` with strictly
  positive sampled mean-output increments;
- microcanonical output-clock mode had maximum clock defect
  `1.93e-10` and maximum initialization output `3.89e-16`;
- neither validation point approached its state, kernel, memory, step, or wall
  cap.

The compact machine-readable record is
[`runs/reference_validation_cpu_20260813/summary.json`](runs/reference_validation_cpu_20260813/summary.json).
It explicitly marks `scientific_evidence_admissible: false`.

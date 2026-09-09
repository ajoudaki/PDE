# O1 Results: Depth-Three Reachable Tail

## Claim level

This is empirical route evidence only.  It does not prove a uniform Orlicz
bound, response summability, source-compression convergence, or a width
limit.

The preregistered depth-three arctangent Euler flow was run with exact
rank-one histories and exact reuse of each Gaussian source and transpose.
The primary run used widths `1024,2048,4096` with eight trials and width
`8192` with four trials, step `0.005`, and horizon `T=1`.  Coupled hidden
clips were `1,2,3,4,6,8`, alongside the untruncated trajectory.  A
step-refinement control at width `1024` used steps `0.01,0.005,0.0025`.

Raw data and metadata are under:

- `outputs/d3_reachable_tail_primary_v2/`;
- `outputs/d3_reachable_tail_w8192_v2/`;
- `outputs/d3_reachable_tail_dt001/`;
- `outputs/d3_reachable_tail_dt0005/`;
- `outputs/d3_reachable_tail_dt00025/`.

The machine-readable analysis is
`outputs/d3_reachable_tail_summary.json`.

## 1. Step refinement passed

Against step `0.0025`, the maximum absolute discrepancies over all clips and
both trials at `T=1` were:

| step | `r2_l2` | `M8` | `M12` | `tau_2` | predictor | kernel |
|---:|---:|---:|---:|---:|---:|---:|
| 0.01 | 1.59e-3 | 1.99e-3 | 2.25e-3 | 3.33e-4 | 1.96e-3 | 2.21e-3 |
| 0.005 | 5.32e-4 | 6.62e-4 | 7.49e-4 | 1.11e-4 | 6.54e-4 | 7.38e-4 |

The primary step is therefore sufficiently resolved for the qualitative tail
comparison made here.

## 2. Width behavior of the untruncated field

At `T=1`, trial means were:

| width | `||r2||_2` | `M8/sqrt(8)` | `M10/10` | effective count for `M10` |
|---:|---:|---:|---:|---:|
| 1024 | 0.8239 | 0.5021 | 0.1552 | 10.5 |
| 2048 | 0.8245 | 0.5002 | 0.1544 | 18.7 |
| 4096 | 0.8321 | 0.5074 | 0.1576 | 22.7 |
| 8192 | 0.8284 | 0.5044 | 0.1562 | 51.5 |

There is no visible width growth.  Over the reliable moment range through
order ten, both `M_p/sqrt(p)` and `M_p/p` decrease with `p`; the former is
already nearly flat on the scale relevant to a subgaussian candidate.  Orders
twelve and sixteen were retained in the raw output but excluded whenever
their effective coordinate count fell below ten, as preregistered.

## 3. Excess-energy tail shape

Using thresholds `1,1.5,2,2.5`, a fit of `log(tau_S)` against `S^2` was
consistently better than a fit against `S`:

| width | quadratic RMSE | linear RMSE | quadratic slope |
|---:|---:|---:|---:|
| 1024 | 0.0343 | 0.1794 | -0.6550 |
| 2048 | 0.0349 | 0.1896 | -0.6728 |
| 4096 | 0.0362 | 0.1151 | -0.5991 |
| 8192 | 0.0229 | 0.1444 | -0.6238 |

This is compatible with a Gaussian large-width bulk tail on this finite
range.  It does not establish the asymptotic tail exponent.  In particular,
a uniform-in-all-widths Gaussian bound is false in scalar-width examples;
the relevant theorem uses the sequential large-width empirical law.

## 4. Self-clip behavior

The clip did not inflate the bulk or tail scale as its radius increased.
At all widths, radius two changed the bottom state at `T=1` by about
`8e-3` in normalized `L^2`; radius three reduced this to between `1.8e-4`
and `4.3e-4`; radii four and above were numerically indistinguishable from
the raw trajectory for these samples.  Radius one changed the dynamics
materially, as expected, but still did not create growing high-moment ratios.

## 5. Preregistered decision

- The empirical kill signal did **not** fire.
- The results are compatible with the projective `psi_1` envelope required
  by Yudovich--Orlicz stability.
- On the tested range they support the stronger large-width subgaussian
  candidate.
- They do not distinguish a true response theorem from finite-time/finite-
  width benign behavior, and they do not repair the quantitative
  complexity-versus-defect gate in causal source compression.

The appropriate theoretical investment remains a renormalized persistent-
query argument or a stability scheme that makes query tails unnecessary.

## 6. Post-experiment analytic correction

An exact later audit showed why the apparent Gaussian bulk tail cannot be
promoted to a finite-width `psi_2` certificate.  Conditional on the matrices,
`r_(2i)(0)` is Gaussian in `A` with a random variance of unbounded support;
therefore `E exp(lambda r_(2i)^2)=infinity` for every positive `lambda` at
every finite width.  The observed quadratic fit describes the typical
large-width bulk on the tested range, while exponentially rare
source/endpoint products force a subexponential extreme tail.

This does not invalidate the preregistered empirical decision.  It changes
the theoretical target: the plausible uniform Yudovich class is `psi_1`
(`||r_2||_p=O(p)`), not `psi_2` (`O(sqrt(p))`), unless a width-first
localization is explicitly retained.

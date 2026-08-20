# Frozen proof-obligation study: final report

**Freeze date:** 25 July 2026  
**Status:** stopped by user instruction; no further computation authorized  
**Scientific verdict:** incomplete and not a numerical verification of the PDE conjecture

## Executive conclusion

This study did **not** test the proposed proof-obligation chain to completion.
Most of the work went into designing, implementing, preregistering, and
auditing the experimental framework. At freeze time, only two scientific
trajectories had completed. Both were \(P=5\) instances of the first
numerical-screen configuration with different cubature scrambles.

Therefore this run establishes none of the following:

\[
\text{ordered dense limit}
\to
\text{conditional depth homogenization}
\to
\text{state sufficiency}
\to
\text{Hermite consistency}
\to
\text{finite-time stability}
\to
\text{all-time stability}.
\]

The only new numerical observation is that two \(P=5\) cubature scrambles
agree closely on one fixed configuration. This is useful as a preliminary
numerical check, but it does not test convergence in \(P\), identify the
ordered dense target, or validate any structural closure assumption.

Taking all earlier completed studies into account, the defensible project
conclusion remains:

> A genuine, autonomous, width-independent \(P=5\) operator–Liouville PDE is
> an unexpectedly accurate and portable low-order surrogate for the tested
> dense Euclidean \(\mu\)P dynamics. The evidence does not establish that the
> Hermite hierarchy converges to arbitrary accuracy or that the PDE equals
> the ordered \(n\to\infty\), then \(L\to\infty\) target.

In particular, the conjecture is **strongly motivated but not numerically
verified**.

## What the five-hour run actually produced

The run produced an extensive experimental framework:

- a seven-stage preregistered protocol;
- runners for numerical resolution, ordered width/depth scaling,
  homogenization diagnostics, same-state continuation attacks, generator
  defects, residual amplification, and late-time tails;
- exact source/configuration provenance and atomic archive validation;
- simultaneous-bootstrap and sequential-gate analysis machinery;
- 23 frozen source/protocol files;
- a 128-test software and infrastructure suite reported green before freeze.

Those 128 tests validate implementation properties. They are **not**
scientific tests of the seven assumptions.

The frozen scientific source-tree identity is
`99bef0bab910ccc75717c276e1dc50ae1bfb3082e2943ec0630603596d44e300`.
The evidence verifier reports two valid archives bound to that source tree.

The prioritization was wrong: the framework was overbuilt before a minimal
sequence of scientific experiments had been secured. The incomplete run must
not be described as having executed the proof-obligation program.

## Evidence present at freeze

Both completed jobs used

\[
P=5,\quad N=16,\quad M=625,\quad R=256,\quad
\Delta t=0.02,\quad T=2,
\]

with cubature seeds `20260723` and `20260724`. They are two of the four
planned \(P=5\) Phase-A scrambles. No \(P=15\) or \(P=35\) Phase-A trajectory
completed.

The two saved \(P=5\) curves differ by:

| Descriptive comparison | Maximum difference |
|---|---:|
| normalized output curve | \(2.8537\times10^{-4}\) |
| normalized all-depth Gram curve | \(3.3542\times10^{-4}\) |
| absolute loss curve | \(4.7977\times10^{-5}\) |

Their minimum stored `projected_energy` values are \(0.9999635\) and
\(0.9999623\). This diagnostic says that the simulated field is nearly
contained in the retained span for these runs. It does **not** measure the
outgoing generator residual or high-to-low feedback defect and therefore
cannot be used as a Hermite-consistency certificate.

Because only two of the twelve Phase-A jobs exist, no preregistered
simultaneous uncertainty bound or Phase-A decision is valid. Even a complete
four-scramble \(P=5\) result would test only one numerical slice; the missing
\(P=15\), \(P=35\), and upward refinements are necessary for the intended
cross-\(P\) numerical gate.

## Gate-by-gate status

| Proposed gate | New run status | Earlier relevant evidence | Defensible interpretation |
|---|---|---|---|
| 1. Ordered \(n\to\infty\), then \(L\to\infty\) target | **Not run** | Earlier work had only an L-shaped width/depth audit; its Cauchy gaps were not statistically resolved | The ordered target is not identified |
| 2. Direct trained-depth innovation and conditional/Onsager mean | **Not run** | Earlier paired-\(W\) experiment found variance slopes near \(-1\), hence RMS \(L^{-1/2}\), for hidden and adjoint fields | Centered cancellation is supported, but conditional-mean bias and the trained Onsager predictor remain unidentified |
| 3. Sufficiency of \((\theta,w)\) by same-state continuation attack | **Not run** | Earlier finite-matrix response enrichment improved rapidly from \(K=0\) to \(K=2\), but retained dense matrices and was not a same-state attack | Static-state sufficiency remains open; response/history coordinates remain a plausible repair |
| 4. Outgoing and high-to-low Hermite generator defects | **Not run** | Earlier `projected_energy` was favorable, while \(P=5,15,35\) accuracy against finite references was nonmonotone | No generator-level Hermite convergence evidence was obtained |
| 5. Worst-direction amplification of measured residuals | **Not run** | No prior adjoint/worst-direction residual certificate | Small closure errors have not been shown to remain small dynamically |
| 6. All-time tail arclength and late-time perturbation stability | **Not run** | Earlier \(P=5\) PDE was numerically flat through \(t=32\); dense comparison was principally through \(t=8\) | Operational plateau evidence exists, but no all-time stability certificate |
| 7. Cubature/discretization gate at every \(P\) | **Incomplete** | Two new \(P=5\) scrambles agree to \(3.35\times10^{-4}\) on the normalized Gram metric | Preliminary \(P=5\) consistency only; the cross-\(P\) and cofinal numerical gate is unresolved |

Thus none of the seven proposed gates passed in this new study. Gate 7 began
but did not reach a decision; Gates 1–6 produced no new scientific archive.

## What the completed earlier studies do establish

### 1. A literal finite PDE exists and is executable

The completed direct simulation constructed and integrated an explicit
Hermite/isonormal operator–Galerkin conditional Liouville PDE. At every finite
order it has no network width, no physical layer count, and no \(n\times n\)
matrix in its mathematical state. Its forward operator and transpose are
paired, it is autonomous and restartable, and it obeys the projected
Euclidean-gradient and positive-semidefinite tangent-kernel identities.

This resolves the earlier concern that the purported PDE was only a verbal
compiler or a disguised finite network.

### 2. The \(P=5\) PDE is an accurate low-order surrogate

For the canonical dense benchmark, the earlier primary comparison reported:

- nonlazy PDE feature motion \(0.633801\);
- dense feature motion \(0.639909\);
- maximum Gram-increment surface gap \(7.2433\times10^{-3}\);
- gap equal to \(1.1428\%\) of PDE feature motion.

The finite-network discrepancy was statistically distinguishable, so the
correct description is “close,” not “exact.”

### 3. The low-order success is portable

The preregistered generalization study held \(P=5\) fixed across 14
configurations involving changed labels, activations, sample counts, input
geometries, and crossed stresses. Every observed full-curve error was below
5%:

| Metric | Median | Maximum |
|---|---:|---:|
| Gram-increment curve | 1.71% | 4.14% |
| output-increment curve | 1.46% | 1.83% |
| loss curve | 0.63% | 1.97% |

This strongly weakens the claim that the PDE was tuned only to one dataset.
It did not pass the deliberately stringent simultaneous all-case
certification rule: the study was underpowered for that rule, six difficult
cases were not fully PDE-resolution-certified, and four missed both fixed
plateau windows.

### 4. The result is not merely the exact identity network

In the activation-continuation test at \(c=2\), the dense nonlinear Gram path
was \(36.38\%\) from the identity path, while the matched nonlinear PDE error
was \(1.09\%\). This decisively rejects exact identity/deep-linear dynamics as
the explanation of the PDE's success.

A gain-matched linear control was nevertheless only \(3.46\%\) from the
nonlinear dense Gram path. Hence higher-order activation effects were resolved
at roughly 1% accuracy, but were not necessary to reach the project's 5%
tolerance in that configuration.

### 5. The crucial arbitrary-accuracy evidence is missing

The earlier audited finite-reference errors did not improve with the first
Hermite refinements:

| PDE level | Gram-increment gap | Fraction of PDE feature motion |
|---:|---:|---:|
| \(P=5\) | \(7.243\times10^{-3}\) | 1.143% |
| \(P=15\) | \(9.202\times10^{-3}\) | 1.457% |
| \(P=35\) stress | \(1.373\times10^{-2}\) | 2.192% |

This is not a disproof: the references were finite \((n,L)\) ensembles,
low-order convergence need not be monotone, and \(P=35\) cubature was not
fully resolved. But it removes positive numerical evidence for
arbitrary-accuracy \(P\to\infty\) convergence. The unrun generator and
amplification tests were designed precisely to distinguish truncation,
missing state, finite-target bias, and numerical contamination; they cannot
be replaced by final-curve comparisons.

## Final scientific assessment

The evidence supports three nested statements with different confidence:

1. **Established construction:** a genuine finite, autonomous,
   width-independent operator–Liouville PDE can be written and simulated for
   the canonical dense Euclidean \(\mu\)P model.
2. **Strong empirical result:** the fixed \(P=5\) PDE predicts nonlazy output,
   loss, and hidden-Gram dynamics surprisingly well across the tested
   benchmark family.
3. **Open conjecture:** increasing finite closure complexity yields
   arbitrary-accuracy approximation to the true ordered dense limit,
   uniformly through all training time.

The present frozen study adds only a small numerical-consistency observation
to item 2. It does not advance item 3 to “numerically verified.”

\[
\boxed{
\text{Useful low-order neural PDE: strongly supported.}
\qquad
\text{Arbitrary-accuracy PDE conjecture: unresolved.}
}
\]

## Canonical report set

The project should treat the following as the nonduplicated final report set:

1. `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md` — central construction,
   evidence synthesis, sharp conjecture, and open obligations.
2. `PDE_GENERALIZATION_FINAL_REPORT(3).md` — fixed-\(P=5\) portability study.
   Versions `(2)` and `(3)` are byte-identical.
3. `ACTIVATION_LINEARITY_SMOKING_GUN_REPORT.md` — identity and
   gain-matched-linear falsification study.
4. `PDE_PROOF_OBLIGATION_STUDY_FROZEN_REPORT.md` — this freeze accounting and
   gate-by-gate final status.

`REPORT.md` is the foundational direct-simulation report, but its main
results are incorporated and qualified in
`FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`.

## Reproducibility status

The accompanying frozen bundle contains:

- this report;
- the exact preregistered protocol and source freeze;
- all runners and tests produced in the five-hour run;
- the two completed and seal-verified numerical archives;
- the nonduplicated canonical prior reports listed above.

No result is imputed for an absent archive, no unfinished stage is converted
to a pass or failure, and no new trajectory was generated after the user's
freeze instruction.

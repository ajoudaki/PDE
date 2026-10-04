# A faster implementation of nonlinear response-memory learning

The strongest empirical result is a way to remove the dense fixed mixer from
the two-layer order-one learner while retaining its observed Gaussian-ensemble
learning behavior. At width16,384 on the fixed digits3/8 problem, the fast
version used **5.22 times less training time and 5.40 times less peak allocated
CUDA memory**. This is a credible computational use case, not a new best
classifier or an established breakthrough. A narrower dense model solves this
small task equally well, and fast prescribed-spectrum transforms are prior art.

The more interesting scientific point is the design constraint: matching
forward random features is insufficient when learning repeatedly sends credit
back through the same matrix. Both spectral moments and how the singular
vectors mix coordinates matter. The evidence below separates an exact
diagnostic, an empirical learned-trajectory result, and theorem projects.

## What was changed, and what actually learns

The original raw q=1 state is A,w,H,D,tau, with H,D the paper's forward and
backward moments. Reconstruction is

    W^(2) = W0 - 2 D^T H/(m n tau).

The read-in and readout obey the original canonical physical velocities;
dot H=rho h, dot D=r delta, dot tau=rho, with H0=h0,D0=w0=0,tau0=1.
There are two tanh hidden layers and no biases. Only the initialized fixed
operator's law changes: independent signed/permuted Hadamard bases surround
a diagonal array whose singular values follow the Gaussian quarter-circle
law. Its singular values are positive; this fixed environment is full rank.
Its transpose reverses the exact same factors.

This costs O(n) fixed entries and O(n log n) work per matrix-vector action.
The moving state still contains 2mn raw memory coordinates plus A,w,tau.
Sample dependence is retained. We do not approximate a particular Gaussian
matrix in operator norm or couple finite-width realizations closely. The
comparison is between ensemble behavior of two different initializations.

## Derivation and checks

[REUSE_THEORY.md](REUSE_THEORY.md) proves an exact identity for an independent
Gaussian probe h, odd response psi, and row-normalized W. Put C=WW^T,
v=E psi(Z)^2, a=E Z psi(Z), and mu4=tr(C²)/n. Then

    E ||W^T psi(Wh)||²/n = v+a²(mu4-1)+R,
    0 <= R <= (v-a²) max_(i!=j)|C_ij|² (mu4-1).

Consequently identical forward Gaussian marginals do not fix nonlinear
transpose-return energy. Flat, Gaussian-spectrum and Gaussian-diagonal-core
initializations have different limiting return energies. The independent
[mathematical review](FAST_REUSE_REVIEW.md) checked the proof and reproduced
all16 CPU cases exactly. Its documented protocol deviations do not change
the original acceptance decision. This is internally checked in its precise
Gaussian-probe scope; it does not establish adaptive learning universality.

The [code review](TRAINING_CODE_REVIEW.md) independently verified physical
mobilities, raw moments, the product defect, Heun and fixed-feature dynamics.
A missing-activation retention bug in v1 was corrected, preserving v1 and the
original outputs. All24 pilot predictions reproduced bitwise in training02.
Because the initial aggregate comparison was underspecified, those pilot
comparisons remain exploratory. The later confirmation fixed all five metrics
before running fresh initialization seeds.

## Fresh-seed learning confirmation

The real-data mechanism task is sklearn's small handwritten digits3 versus8:
64 training images and293 fixed validation images. Centering uses training
statistics only; each centered image is normalized to norm sqrt(64). Both
labels are +/-1. The same data split was used in the pilot and confirmation,
so only the initializations are fresh, not the dataset. At width8192, five
seeds and four operator laws produced20 trained trajectories through time40.

For each operator law, average the five trajectories first. The table reports
RMS distances to the Gaussian ensemble mean, over all21 saved times; prediction
distance uses all357 examples and Grams use all64x64 training pairs.

| Observable | Flat spectrum | Gaussian spectrum | Gaussian diagonal |
|---|---:|---:|---:|
| Predictions | 0.01779 | **0.00194** | 0.02060 |
| First-layer Gram | 0.00859 | **0.00098** | 0.01067 |
| Second-layer Gram | 0.01746 | **0.00143** | 0.02805 |
| First-layer RMS-motion curve | 0.02148 | **0.00028** | 0.01334 |
| Second-layer RMS-motion curve | 0.02489 | **0.00098** | 0.04948 |

All five predeclared comparisons pass. All five Gaussian-spectrum runs show
substantial first-layer motion and approximately60% less final validation MSE
than their own analytic frozen-feature readout. All other operator laws also
learn useful features. The independent [confirmation review](CONFIRM_REVIEW.md)
recomputed every metric, checked initialization variability and reproduced two
trajectories on the other RTX3090 bit for bit. Root then reproduced the entire
20-run campaign: all120 saved array fields, data and indices match bitwise.

The measured Gaussian-spectrum prediction distance0.00194 is below the
paired empirical standard-error scale0.00235 of the ensemble-mean difference.
It is compatible with the initialization sampling floor; this does not prove
the two population laws equal. Every law made six classification errors on
293 validation images. The Gaussian-diagonal model actually had the lowest
mean MSE despite worse Gaussian-trajectory fidelity. These are distinct goals.

## Measured computational scope

The width16,384 comparison uses three new seeds, TF32 matrix multiplication
for BOTH methods, float32 state, the same Heun step. It includes actual training,
scheduled evaluation and host transfers, but excludes setup and final archive
serialization. Both implementations use CUDA graphs. Hardware is RTX3090.

| Quantity | Dense Gaussian fixed mixer | Fast Gaussian-spectrum mixer |
|---|---:|---:|
| Median training/evaluation time | 12.665 seconds | 2.427 seconds |
| Peak allocated CUDA bytes | 1,316,446,208 | 243,687,424 |
| Moving model scalars | 3,162,113 | 3,162,113 |
| Stored fixed mixer entries | 268,435,456 floats | 147,456 mixed float/index entries |

Integer and float entries have different byte widths; the allocator measurement
is the reported practical memory comparison. Setup took approximately3.8--4.9s
for Gaussian and0.061--0.062s for the fast version. Same-seed replay reproduced
both prediction trajectories bitwise. Disabling TF32 changed either trajectory
by less than7.9e-5 maximum-over-time RMS. Earlier step-halving at width2048
changed predictions by at most1.14e-5; larger-width continuous-time accuracy
is not independently certified by that smaller-width check.

The faster method is useful for simulating a very wide population, but width
is not itself a task requirement. The width2048 dense Gaussian pilot already
had the same six validation errors, took about0.784s and used63,059,968 peak
bytes. Thus this study does not show the fastest solution to digit recognition.
It shows a less expensive implementation at a specified large population width.
No superiority to trained Fastfood/ACDC, direct factors or dynamic low rank is
established by this comparison.

![Empirical learning fidelity and computational cost](/home/amir/Codes/PDE/data/generated/response_memory_fast_mixing_20261002/synthesis01/fast_environment.png)

Figure scope: first two panels use three pilot seeds at widths512/2048 and
five fresh seeds at8192; they are ensemble-mean distances, not per-network
approximation errors or confidence intervals. Last two panels use three seeds
at width16,384 with TF32 on both methods. The small validation dataset is shared.

## Adversarial spectrum and basis controls

Two additional predeclared conditions use exactly the five confirmation seeds.
The two-point spectrum (half0, half sqrt(2)) matches both second and fourth
Gaussian singular moments, but differs in higher moments. The other condition
keeps the quarter-circle spectrum and the left basis, removing only the right
Hadamard mixing. The latter preserves the expected independent Gaussian-probe
return energy EXACTLY; that statistic is blind to right orthogonal factors.

| Operator | Prediction distance | Second-layer Gram distance |
|---|---:|---:|
| Fully mixed Gaussian spectrum | 0.00194 | 0.00143 |
| Two-point spectrum | 0.00251 | 0.00267 |
| Gaussian spectrum, unmixed right basis | 0.00994 | 0.01693 |

The right-basis discriminator passes its frozen twofold separation criterion,
including every leave-one-seed-out comparison. Its initial second-layer Gram
discrepancy is0.00145, versus0.00165 for the fully mixed model; the large later
gap is not explained by a larger measured initial forward Gram gap. This
supports the need to preserve how credit returns to coordinates, not just
initial forward behavior or the one-pass return scalar.

The two-point discriminator **does not pass**. This task does not decisively
show that matching the full spectrum is needed beyond matching its fourth
moment. No width/horizon/seed search was performed to force that claim.
These controls are diagnostic, not competitive architecture benchmarks.

## Theory and novelty status

Fast prescribed-spectrum Hadamard constructions and nonlinear AMP universality
are already in [Wang--Zhong--Fan](https://arxiv.org/html/2206.13037v3).
[LITERATURE_AUDIT.md](LITERATURE_AUDIT.md) records this and strong nearby
architectures. The transform and broad idea of spectral universality are not
our novelty. Its application to a fixed-state response-memory learner is the
specific proposed use case.

[POLYNOMIAL_TRANSFER.md](POLYNOMIAL_TRANSFER.md) derives a complete finite-step
corollary for polynomial activations using the published alternating-tree
theorem, including adaptive residual/clock feedback. The separate internal
[polynomial audit](POLYNOMIAL_REVIEW.md) passes; polynomial activation is a
changed model. [TANH_TRANSFER.md](TANH_TRANSFER.md) assembles the actual tanh
extension, with a checked clipping bridge in
[TANH_CLIPPING_REVIEW.md](TANH_CLIPPING_REVIEW.md) and the complete reduction in
[LIPSCHITZ_PROGRAM_TRANSFER.md](LIPSCHITZ_PROGRAM_TRANSFER.md). The full integration
has now passed the separate internal [tanh audit](TANH_TRANSFER_REVIEW.md).
For fixed data, fixed step size/count and a finite query list, the actual tanh
closure has the same limiting predictions and qualified feature statistics
under the fast and Gaussian ensembles. This is a proved, internally checked
study result using the identified published universality inputs; it is not
promoted material. No finite-width rate, all-time, continuous-time or
same-realization matrix-approximation statement follows.

[CONTRIBUTION_REVIEW.md](CONTRIBUTION_REVIEW.md) independently assesses the
positioning as a serious supporting use case, with the broader architecture
claim still unproved. The bounded [recent-literature follow-up](NOVELTY_ADDENDUM.md)
found no direct additional match but does not establish priority.

## Reproduction and evidence

Source versions v1/v2/v3 and their exact frozen protocol versions are preserved.
Recovered protocol text was verified against its original SHA256 before being
saved; it was not silently rewritten to fit outcomes. All data arrays, software
versions, seeds, source hashes and failed-attempt logs are in the generated
namespace. Main commands from the repository root:

```bash
env CUDA_VISIBLE_DEVICES=1 /home/amir/miniconda3/bin/python \
 studies/response_memory_fast_mixing_20261002/fast_training.py \
 --out <fresh-directory> --widths 8192 --seeds 7501 7502 7503 7504 7505 \
 --protocol CONFIRM_PROTOCOL.md

/home/amir/miniconda3/bin/python \
 studies/response_memory_fast_mixing_20261002/analyze_training.py <run-directory>

/home/amir/miniconda3/bin/python \
 studies/response_memory_fast_mixing_20261002/verify_reproductions.py \
 --first <original-directory> --second <repeat-directory>
```

Exact original commands/configs are in training01/training02, refinement01,
confirmation01/confirmation_reproduction01, scaling01/scaling_ieee01/
scaling_reproduction01, and mechanism01/mechanism_reproduction01.
The plot producer is make_figures.py; its results and source hashes are in
synthesis01. Independent checks are under training_review and
reuse_training_review. The manuscript, maintained book/code and Git index
were not changed. None of these findings is promoted material.

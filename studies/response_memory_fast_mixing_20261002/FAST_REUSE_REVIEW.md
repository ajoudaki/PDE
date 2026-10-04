# Independent review of the Gaussian-probe reuse discriminator

Verdict: **PASS for the exact return-energy identity, its stated spectral
asymptotics, and the bounded numerical mechanism check.** No substantive
mathematical or numerical error was found in that scope. There are nonblocking
protocol and reporting discrepancies below. This verdict does not establish
trained-network universality, feature-learning usefulness, novelty, or measured
computational advantage, and is not a promotion approval.

Reviewed 2026-10-02. The reviewer read only the assigned frozen theory, protocol,
script, metrics, all saved probe arrays, and required process/notation skills.
No study history, manuscript, other studies, or other reviewers' findings were
used. No author sources were changed. Scratch and reproduction products are
under `data/generated/response_memory_fast_mixing_20261002/reuse_review/`.

## Frozen input identity

SHA-256 hashes were taken before reading the scientific inputs:

| Input | SHA-256 |
|---|---|
| `REUSE_THEORY.md` | `8a58f0b887ab5d907aeb1c1f849e4b623e58248650157a152132cb5b28be962d` |
| `REUSE_PROTOCOL.md` | `7b36ce6aa1a207f4d7bded8cf5b571800d4b35ed590a9158bd402f2d729c07b5` |
| `reuse_check.py` | `3eb7e3e3bd07f1c5ae636dd30b180e4f5fe2403d6a06f9fd9ad3a66aaae6a3b2` |
| `reuse_check01/metrics.json` | `c7dfe7005419361c31a137c0979ce3ce2c1be9bd51f2458cf7d1c9923b37374c` |
| `reuse_check01/probe_energies.npz` | `dd66f5800de2a826c275723240013cd55f32f2e08e8d9c5afc3632fc090b49fd` |

The hashes recorded by the original run for its script and protocol match these
inputs. Matching hashes establish reproducibility of the submitted artifacts;
they do not independently establish the historical assertion that the protocol
and amendment preceded every experiment.

## Mathematical audit

Let (W\in\mathbb R^{n\times n}), (C=WW^\top), (C_{ii}=1), and
(h\sim N(0,I_n)) independently of (W). For an odd function
(\psi\in L^2(N(0,1))), write
(v=\mathbb E\psi(Z)^2), (a=\mathbb E[Z\psi(Z)]),
(\mu_4=\operatorname{tr}(C^2)/n), and
(\epsilon=\max_{i\ne j}|C_{ij}|), with (\epsilon=0) when (n=1).
The claimed identity is valid under exactly these assumptions.

In normalized Hermite coordinates (\psi=\sum_{k\text{ odd}}c_k e_k),
one has (c_1=a), (\sum c_k^2=v), and, for jointly standard Gaussian
(Z_1,Z_2) with correlation (c),
(\mathbb E[e_k(Z_1)e_l(Z_2)]=\mathbf1_{k=l}c^k).
The generating-function derivation and the completeness argument in the input
are sufficient; (L^2) approximation also covers the degenerate cases (c=\pm1).
The remainder has the explicit form

\[
R=\frac1n\sum_{i\ne j}\sum_{k\ge3,\ k\text{ odd}}c_k^2 C_{ij}^{k+1}.
\]

Every term is nonnegative and
(C_{ij}^{k+1}\le\epsilon^2 C_{ij}^2).
Also (\sum_{i\ne j}C_{ij}^2/n=\mu_4-1), proving

\[
\mathbb E_h\frac{\|W^\top\psi(Wh)\|^2}{n}
=v+a^2(\mu_4-1)+R,
\qquad
0\le R\le(v-a^2)\epsilon^2(\mu_4-1).
\]

There is no independence assumption on the coordinates of (Wh). The proof
handles negative correlations, rank-deficient matrices, and (a=0). For an
independent numerical algebra check, two-dimensional Gaussian quadrature with
(\psi=.6e_1+.8e_3) and correlations (-1,-.7,0,.7,1) reproduced
(1+.6^2c^2+.8^2c^4) to less than (4\times10^{-15}); this example saturates
the remainder bound.

For the structured matrix in equation (3), direct multiplication gives
(C=D_LH\operatorname{diag}(s_i^2)H^\top D_L). Thus its diagonal and singular
values are as stated. An off-diagonal covariance is a centered sum from a
uniform sample of (n/2) of the prescribed squared singular values. If these
values lie in ([0,M]), the displayed Doob increments are correct and have
magnitude at most (2M/n) after scaling. Summing the conditional exponential
bounds over (n/2) increments gives

\[
\Pr(|C_{ij}|>t)\le2\exp\{-nt^2/(4M^2)\}.
\]

The union bound needs no independence between covariance entries. A uniformly
bounded (M), convergence of (\mu_4), and the deterministic remainder bound
prove equation (5). Quarter-circle midpoint quantiles followed by RMS
normalization satisfy these conditions, with limiting fourth singular moment
2. Flat singular values give (C=I_n) and exact energy (v).

For normalized Gaussian diagonal values, conditional on their magnitudes the
same permutation bound applies with random (M=O_P(\log n)).
Since (\mu_4\to3), the stated
(O_P((\log n)^{3/2}/\sqrt n)) off-diagonal bound is sufficient and the
limit is (v+2a^2). The terminology must remain restricted to the explicitly
defined Gaussian-diagonal core.

The iid Gaussian reference calculation is also correct. Conditional on
(h\ne0), the regression residual lies in the subspace perpendicular to (h),
so the two terms in (W^\top\psi(Wh)) are orthogonal. Writing
(s=\|h\|/\sqrt n), integration over the independent Gaussian rows gives
exactly

\[
(1-1/n)a_s^2/s^2+b_s/(ns^2)+(1-1/n)v_s.
\]

For (\psi=\tanh), (a_s^2/s^2\le v_s\le1) and
(b_s/s^2\le\mathbb E Z^2=1). The continuous extension at (s=0),
convergence (s\to1), and these uniform bounds justify the limit (v+a^2).
This establishes the Gaussian **joint expectation over (W,h)**. It does not
establish concentration of the conditional expectation for a single Gaussian
matrix. The structured result is instead convergence in probability of the
conditional expectation over (h). These levels of averaging must remain
explicit when comparing the two conclusions.

## Code and evidence audit

The script was rerun, unchanged, using `/home/amir/miniconda3/bin/python`, with
CPU float64 computation and output in the review scratch directory. All 16 case
records matched the submitted case records exactly; every value in all 20 saved
arrays matched exactly. Raw-array means, sample standard errors, and paired
differences were recomputed independently. Every array has 128 finite entries.

The maximum recorded relative forward/transpose error was
(6.13\times10^{-16}). An additional independent width-32 check constructed
the Sylvester matrix by block recursion and the permutation matrix explicitly;
both fast actions matched their explicit matrices to below
(3.36\times10^{-16}). This avoids relying only on an explicit matrix obtained
by calling the implementation on the identity. The stored inverse permutation
does implement the adjoint correctly.

The covariance moments, diagonal checks, remainder bounds, and sample means
are evaluated as specified. The largest distance from the permitted analytic
energy interval was 1.265 sample standard errors, below the four-error rule.
The two quadrature orders differ by (1.21\times10^{-13}), below the stated
(10^{-9}) threshold. The rerun took 1.33 recorded wall-clock seconds.

| Width | Quarter-circle minus flat mean | Pooled standard error | Gap / pooled error |
|---|---:|---:|---:|
| 512 | 0.3632774 | 0.0047425 | 76.60 |
| 1024 | 0.3660174 | 0.0036616 | 99.96 |

Thus the original pooled-error discrimination condition passes independently
of the implementation's choice to use paired errors. These sample-error rules
are numerical acceptance criteria, not proved finite-sample confidence bounds.
Only one matrix realization per case and width was tested.

## Nonblocking protocol and reporting discrepancies

1. **Gap statistic:** `REUSE_PROTOCOL.md:44` specifies pooled standard errors;
   `reuse_check.py:130` uses the standard error of paired differences from shared
   probes. Pairing is legitimate here, but it is a deviation from the written
   criterion. The table above checks the original criterion and preserves the
   PASS. Any account of adherence should disclose the deviation rather than
   retroactively rewriting the frozen protocol.
2. **Ensemble and seed details:** the protocol's initial formula at lines 20–22
   is narrower than the implemented signed/permuted construction. For this
   odd-ψ Gaussian-probe energy, right orthogonal factors preserve the probe
   distribution, and left row signs preserve the scalar energy after applying
   ψ. Consequently these additions do not invalidate the mechanism test.
   The code uses width-offset seeds `6101+n`, `6201+n`, and `6301+n`; the
   protocol only says fixed seed 6101, and the output metadata does not list
   these seed rules. They remain recoverable from the hashed code.
3. **Quantile tolerance and bookkeeping:** the protocol asks for a reported
   inversion tolerance, but the output reports only the Gaussian-moment
   quadrature discrepancy. The quantile routine performs 60 bisections and
   then RMS normalizes; no achieved CDF residual or final bracket width is
   reported. The protocol's “eight covariance matrices” is stale wording:
   the run has the separately specified 16 cases. Neither discrepancy affects
   the observed acceptance criteria, but exact protocol compliance should not
   be claimed.
4. **Budget and failure retention:** the script checks elapsed wall time only
   before each case, rather than enforcing a hard CPU-time limit, and an
   exception before the final save leaves no complete failure record. This
   did not affect the short successful run. Future uses of this protocol
   should record the actual timing convention and persist failed/partial
   outcomes instead of relying on successful completion to save evidence.

## Claim boundaries and missing evidence

The supported result is a discriminator: equal initial Gaussian forward
marginals do not determine a nonlinear return through the same transpose.
For diffuse covariance correlations, its leading difference is controlled by
the fourth singular moment. The quarter-circle construction matches the iid
Gaussian limiting expectation of this one observable; it does not establish
agreement of the full return vector or of all nonlinear observables.

The saved dense reference is **row-normalized Gaussian**, as the protocol
amendment states; it is not the iid Gaussian ensemble of the separate analytic
calculation. The numerical comparison therefore must not be described as a
finite-width simulation of that unnormalized iid ensemble.

Adaptive training, an endogenous non-Gaussian probe, repeated reuse,
singular-vector correlations, and trajectory-level equivalence are outside
the proved and measured scope. The operation and fixed-storage counts for a
single fast transform are justified, but the experiment deliberately forms
dense matrices and does not benchmark end-to-end training or total training
state. Matching this statistic is a necessary discriminator for proposals
claiming to match it, not a sufficient model-replacement criterion.

No independent priority or novelty determination was possible from the frozen
inputs, and none is claimed by the theory. The manuscript-specific assertions
about its physical update and original Fastfood guarantees were not audited
against their external sources, which were outside the assigned input scope.
There are no missing inputs needed to verify the standalone mathematical result
or reproduce this mechanism check. The stated stronger research obligations
remain open.

# Frozen bounded-DMFT protocol

Protocol version: `bounded-dmft-v1`, frozen before any positive-time DMFT run.

Parent protocol binding:

- path: `../PROTOCOL.md`;
- SHA-256: `d1e75ad896a3572f77b9bc6ec68a7047219a075645b87d44c520d677fc3b153a`;
- manifest: `../FROZEN_PROTOCOL.json`.

The parent protocol prevails if any prose below is ambiguous.

## 1. Decision question

Does the full two-response discrete DMFT candidate pass exact initialization,
low-order MFP, response, self-consistency, and refinement gates for the
bounded canonical model

\[
a_0\sim N(0,1)\mid |a_0|\le3
\]

without variance renormalization, on the first output interval
\(0\le F\le0.5\)?

This protocol tests the internal correctness of the current DMFT witness.  It
does not prove a finite-width limit, remove the cutoff, or test the unbounded
global Stieltjes claim.

## 2. Competing hypotheses

- **H1 (full response witness):** equations (8)--(16) of `DERIVATION.md`, with
  both reciprocal responses, have a numerically stable bounded solution that
  passes the exact gates.
- **H0 (gradient independence):** setting \(A=B=0\) is sufficient for the
  canonical curve.
- **H2 (invalid/currently unresolved witness):** the full fixed point is
  noncontracting, tail dominated, non-PSD, or fails exact MFP identities at
  the authorized resolution.

H0 is rejected as an architecture-level identity if the exact response gate
passes, but that alone does not establish H1.  Any failed numerical-validity
gate is classified as inconclusive/H2, never evidence for or against the
Stieltjes conjecture.

## 3. Frozen model and discretization

- Clock: feature time.
- Cutoff: \(A=3\) only.
- Feature horizon: \(s_{\max}=0.005\); results after the first node with
  \(F>0.5\) are discarded.
- Grid: \(t_k=kh\), \(0\le k\le L\), \(h=s_{\max}/L\).
- Authorized levels: \(L=64\) and, conditionally, \(L=128\).  \(L=256\)
  has zero budget.
- Integral convention: explicit left endpoint,
  \(\int_0^{t_k}g(t_k,s)ds\mapsto h\sum_{m<k}g_{k,m}\).
- Response contact convention: strict subdiagonal entries \(m<k\) enter the
  Volterra sums.  Diagonal response values are diagnostic only.  Entries
  \(m>k\) must vanish.
- Response normalization: raw discrete path derivatives
  \(R^x_{km}=\mathbb E[\partial U_k^2/\partial\Xi_m]\) and
  \(R^b_{km}=\mathbb E[\partial(2A_{r,k}Z_k)/\partial H_m]\) are stored as
  densities \(A_{km}=R^x_{km}/h\), \(B_{km}=R^b_{km}/h\).  The causal
  equations use \(h\sum(A+\Phi_1)\) and \(h\sum(B+G_2)\).
- State update: left Euler for \(U\) and \(A_r\), and the corresponding
  causal left sums for \(Q,Z\).
- Arithmetic: IEEE float64 throughout.
- Covariance factorization: symmetric eigendecomposition; a negative
  eigenvalue below the PSD tolerance is fatal.  Negative eigenvalues within
  tolerance are clipped to zero and their magnitude and count are recorded.
  Numerically null positive modes below \(10^{-14}\lambda_{\max}\) are also
  clipped to zero and recorded.  The frozen base normals are multiplied by
  the unique symmetric principal root
  \(C^{1/2}=V\operatorname{diag}(\sqrt{\lambda_{\rm clipped}})V^\top\), not by
  the sign/rotation-dependent rectangular eigenfactor.  This preserves common
  random numbers under arbitrary eigenvector sign changes and rotations in
  degenerate eigenspaces.  No positive jitter is added.

## 4. Population, seeds, and mixing

- Authorized population levels: \(S=2^{12}\) and, conditionally,
  \(S=2^{14}\).  \(S=2^{16}\) has zero budget.
- Primary population: scrambled Sobol points transformed by inverse Gaussian
  CDF, generated as \(S/2\) points plus their exact antithetic complements.
- Scramble seeds: `2026081401` for the first-layer species and `2026081402`
  for the second-layer species.
- One independent validity replication, if triggered: seeds `2026081411`
  and `2026081412`.
- The same base Sobol normals are reused at every fixed-point iteration and
  every response ablation at fixed \((L,S)\).
- Mixing: raw proposal \(\widetilde\Theta_r\) and current kernel state
  \(\Theta_r\) are combined as
  \(\Theta_{r+1}=0.75\Theta_r+0.25\widetilde\Theta_r\).
- Maximum iterations: 30.

No seed, mixing factor, contact convention, or cutoff may be changed inside
this protocol after seeing a positive-time curve.

## 5. Exact low-order reference

`truncated_mfp_reference.py` evaluates the MFP derivatives with every
readout Gaussian moment replaced by the exact conditional moment

\[
m_{2r}(3)=\mathbb E[Z^{2r}\mid |Z|\le3].
\]

The mandatory derivative references are finite-cutoff

\[
F_3^{(A=3)},\qquad F_5^{(A=3)},
\]

not the canonical Gaussian integers.  The implementation must independently
recover \(111,1685184,77400633120\) when its moment law is switched to the
untruncated Gaussian.  \(F_7\) is optional and cannot block the primary run.

Before Stage 1, a DMFT-side local jet routine must differentiate the **discrete
causal fixed-point map at \(h=0\)** by forward-mode/high-order differentiation
or a symbolic response recursion.  It may use fixed exact Gaussian moments or
fixed QMC controls, but it may not infer derivatives by fitting a computed
positive-time curve.  This independent local routine must reproduce both
(i) the canonical Gaussian integers \(F_3=1685184\),
\(F_5=77400633120\), and (ii) the finite-\(A\) MFP values
\(F_3^{(A=3)}\), \(F_5^{(A=3)}\), within the tolerances below.  Until that
routine exists and passes, Stage 1 is locked.

After a Stage-1 unlock, a curve-based fit may be reported as a descriptive
cross-check only.  It uses the preregistered odd basis

\[
F(s)=d_1s+d_3s^3/3!+d_5s^5/5!+d_7s^7/7!
\]

on the first 20% of feature-time nodes, using the exact \(d_1=27+84m_2(3)\)
as a fixed coefficient.  The same fit window is used at every refinement; its
outcome cannot retroactively unlock or invalidate the run.

Mandatory relative tolerances after estimated sampling error is included:

- \(F_3\): 5%;
- \(F_5\): 15%;
- \(F_7\), if reported: 30% and explicitly non-gating.

Failure of \(F_5\) at \(L=64,S=2^{12}\) authorizes only the declared
resolution branches; it does not authorize changing the fit window.

## 6. Numerical validity gates

All norms below are computed on the causal triangle retained up to \(F=0.5\).

### 6.1 Initialization

Each sampled component \(K_a,K_W,K_u\) must be within 0.5% of

\[
(27,36m_2(3),48m_2(3)),
\]

and their sum must be within 0.25% of \(27+84m_2(3)\).

### 6.2 Response and ablation

At \(L=64\), the pathwise response estimator must satisfy

\[
|A_{1,0}-4|\le0.02,
\]

and

\[
\left|B_{1,0}-\{12+28m_2(3)\}\right|
\le0.05\,\{12+28m_2(3)\}.
\]

The response-free ablation returns zero for both and must therefore fail.
If the full estimator also fails, positive-time computation remains locked.

### 6.3 Self-consistency residual

For each kernel family \(X\in\{\Phi_1,G_2,A,B\}\), define

\[
r_X=\frac{\|\widetilde X-X\|_{F,\triangle}}
{\max(1,\|X\|_{F,\triangle})},
\qquad r=\max_X r_X.
\]

Convergence requires \(r\le5\times10^{-3}\) on three consecutive iterations.
The contraction factor is the median of \(r_j/r_{j-1}\) over the last five
available iterations.  If after iteration 15 this factor is at least 0.98,
or \(r\) increases on five consecutive iterations, stop as noncontracting.

### 6.4 PSD and causality

For a covariance \(C\in\{\Phi_1,G_2\}\), require

\[
\lambda_{\min}(C)\ge-10^{-10}
\max\{1,\lambda_{\max}(C)\}.
\]

The maximum forbidden upper-triangular response magnitude must be at most

\[
10^{-9}\max\{1,\|A\|_\infty,\|B\|_\infty\}.
\]

### 6.5 Observable identity

Compute \(F_k=\mathbb E[A_r(t_k)Z(t_k)^2]\) directly from the sampled
second-layer paths; do not define it by integrating \(K\).  Define the left
difference

\[
D_k=(F_{k+1}-F_k)/h-K_k.
\]

The normalized RMS defect is

\[
e_{FK}=\left(\frac1N\sum_k
\frac{D_k^2}{\max(1,K_k^2)}\right)^{1/2}.
\]

It must be at most 2% at \(L=64\), and must decrease by a factor at least 1.6
when \(L\) doubles at fixed or larger \(S\).  A nondecreasing defect is fatal
to the current discretization.

### 6.6 Population-tail metric

For the diagonal contributions, audit the sample means of \(Z^4\) and
\(4(UQ)^2\) directly.  The middle-layer product

\[
4\,\mathbb E[(A_rZ)^2]\,\mathbb E[U^4]
\]

uses independent species, so audit the top-0.1% and largest-single-sample
shares of \((A_rZ)^2\) and \(U^4\) **separately**, never by artificially
pairing their samples.  If any share exceeds 25%, or the largest single sample
contributes more than 2%, stop as tail dominated.  Also stop if any state is
nonfinite.

The independent scramble replication is triggered only if the primary cell
otherwise passes but (i) any mandatory statistic is within 25% of its stated
pass/fail tolerance, or (ii) a top-0.1% tail share exceeds 15%.  The
replication must agree within the combined QMC between-scramble error; if it
does not, the result is inconclusive.  This replication consumes the same
cumulative stage budget.

## 7. Branch rules and hard budget

### Stage 0: no positive-time claim

Run unit tests, untruncated MFP recovery, truncated (A=3) reference
generation, initialization algebra, the one-step response gate, and the
independent DMFT-side \(h=0\) differentiation through \(F_5\).  These must all
pass before Stage 1.  Merely generating the MFP target does not pass the
DMFT-side jet gate.

### Stage 1: primary bounded cell

Run only \(A=3,L=64,S=2^{12}\), capped at **600 cumulative GPU seconds** for
this branch.  Stop immediately on a noncontracting residual, PSD failure,
causality failure, nonfinite state, or tail failure.

### Conditional Stage 2

An additional **1800 cumulative GPU seconds** is authorized only if Stage 1
passes every gate except a clearly identified discretization or population
resolution gate.  The only authorized refinement is the single cell
\(L=128,S=2^{14}\).  There are no alternate \(L=64,S=2^{14}\) or
\(L=128,S=2^{12}\) branches.  \(L=256\) and \(S=2^{16}\) have zero budget.

The 600-second and 1800-second budgets are cumulative, not per iteration or
per cell.  On exhaustion, stop and report inconclusive.

Matched finite-width, alternative-cutoff, cutoff-removal, physical-time,
\(y>0.5\), and unbounded-Gaussian runs require a separate future protocol.

## 8. Interpretation

- **Pass:** full response DMFT passes every exact and numerical gate through
  an authorized refinement.  This supports internal correctness of this
  bounded DMFT witness only.
- **Fail:** a replicated exact identity or refinement trend fails while every
  numerical-validity gate passes.  This falsifies the current discretization
  or response implementation, not the broad existence of a DMFT and not the
  Stieltjes conjecture.
- **Inconclusive:** a residual, PSD, causality, tail, time, sampling, or budget
  gate fails.  No conjecture-level update is allowed.

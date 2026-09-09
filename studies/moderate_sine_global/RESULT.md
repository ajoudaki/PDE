# Exact moderate sine: a local theorem and the global continuation gap

2026-09-08. **The requested unconditional global theorem has not been
proved.** This investigation proves a local joint population/GF/GD theorem
for the exact activation, finite-horizon bounds for the actual algorithms,
and a strong endpoint lemma. It also proves a conditional global population
construction from a specified exponential-tail hypothesis. That hypothesis
is still open for these training trajectories.

## The activation and unchanged target

\[
v=\frac{1-e^{-8}}2-4e^{-4},\qquad
\Phi(z)=\frac{z+\frac25[\sin(2z)-2e^{-2}z]}
 {\sqrt{1+\frac4{25}v}}.
\]

The coefficient 2/5 and frequency 2 are unchanged. The architecture,
Gaussian initialization, finite readout, raw metric and two actual finite
residuals are those of the original three-hidden-layer model. Inputs
satisfy |rho| <= 1-delta and labels are binary. The target is global strong
canonical population existence, uniqueness/restart, and the original full
joint GF/GD limit on every fixed finite physical interval. A new small
activation coefficient or a change of architecture is not an answer.

## 1. A positive local result at the exact coefficient

[LOCAL_SOURCE.md](LOCAL_SOURCE.md) proves that there is an explicit
universal S0>0 such that the canonical strong population flow and the
full original joint GF/raw-GD limits hold on [0,S0/3] in physical time.
This includes the raw kernels, both action orientations, same-layer
hidden paths and velocities, second moments and integrated speeds.
The interval is a conservative sufficient interval, not an estimate of
the flow's maximal existence time.

The proof uses time smallness rather than activation smallness. With
population C(0)=0, the reverse Gaussian source standard deviations are
O(S), the complete backward response rows are O(S), and the forward
response entries are O(h_j) at source step h_j. A four-stage causal
induction closes these bounds, retaining both current transpose returns.
The random derivative envelope has exponent O(S^2) times a Gaussian
envelope. This supplies Gaussian incoming-field tails uniformly in the
auxiliary cap and mesh and permits their removal.

The source statement includes its complete constants. In its pair-valued
moment estimates, the Lp norm means the Lp norm of the pointwise sample
maximum. Its previous-source inequality (21) is for k>=1; the initial
current return vanishes separately. The audit records these conventions.

This is a local theorem. At a reached positive time, the reverse fields
are no longer zero and the old Gaussian source history remains. The same
small-time initialization argument cannot simply be restarted with fresh
independent roots.

## 2. The finite algorithms do have global compact-time bounds

[PHYSICAL_CONTINUATION.md](PHYSICAL_CONTINUATION.md), Sections 2--5,
proves the following without a population-limit assumption:

- Every finite-width GF exists for all physical times, with
  integral_0^T ||dot Theta||_raw^2 <= L(0) and raw displacement at most
  sqrt(T L(0)).
- For each fixed T, the prescribed raw GD step n^-2 decreases the loss
  and has a uniform raw-energy/displacement bound for all sufficiently
  large widths on initialization events of probability tending to one.
- The joint same-layer empirical path laws are tight in the weak topology.
  Strong W2 compactness and identification do not follow from this bound.

For the GD statement the note derives, rather than assumes, a finite-width
raw Lipschitz bound 11000 sqrt(n) B^9 on a primal ball B. Multiplication
by n^-2 gives a vanishing descent-step restriction. The sqrt(n) factor
is not dropped or used to claim a population Lipschitz estimate.

## 3. A finite strong endpoint always exists along an existing flow

If a strong physical population solution exists on [0,T*) with T* finite,
then its full raw state has a strong endpoint Theta*. The exact estimate is

\[
\|\Theta(t)-\Theta(s)\|_{\rm raw}
\le\sqrt{(t-s)[\mathcal L(s)-\mathcal L(t)]}.
\]

Completeness gives the endpoint. The true raw gradient is continuous,
so the raw velocity and all forward/backward fields also converge
strongly there. Their compact time images give qualitative uniform L2
tails. This rules out raw-state or raw-velocity divergence as the reason
for failure of continuation at a finite time.

The missing step is existence and identification starting from that
reached endpoint. Continuity of an infinite-dimensional vector field
does not supply the needed local ODE theorem. The endpoint's qualitative
tails do not supply a quantitative source-response bound.

## 4. A sufficient global hypothesis, weakened to exponential tails

[CONDITIONAL_GLOBAL_AND_OBSTRUCTIONS.md](CONDITIONAL_GLOBAL_AND_OBSTRUCTIONS.md),
Sections 3--4, considers the actual recursively capped physical fields
with a scalar cutoff on the raw increment norm. The cutoff gives global
fixed-cap approximants without assuming that capped gates dissipate the
original loss.

A sufficient, unproved hypothesis is: for each finite T and the prescribed
raw cutoff radius, there are K_T,c_T>0, independent of the cap R, such that

\[
\sup_{R\ge1,\,t\le T,\,i,\ell}
\|q_{R,i}^{\ell}(t)\mathbf1_{|q_{R,i}^{\ell}(t)|>u}\|_2
\le K_T e^{-c_Tu}.
\tag{ET}
\]

Here q^3=C, and the lower q's are computed with the actual recursively
capped upper backward fields. The hypothesis concerns this specific
causal family, not arbitrary vectors fed into a Gaussian matrix.

The comparison costs only one power of a freely selected truncation u.
Optimizing u gives the modulus a log(e/a), with a the raw discrepancy.
It yields Cauchy convergence of the capped paths and directions. The
uncut limit then has the true energy identity, which removes the scalar
raw cutoff. Reference-only comparison gives uniqueness against arbitrary
bounded-primal strong competitors and consistency after restart.

Thus (ET) implies a global canonical strong population flow for the
exact activation. Gaussian tails are a stronger condition than needed.
The complete finite GF/GD and observable bridges would still need
reassembly for this global conditional construction; the conditional
note and its audit do not claim that reassembly is finished.

## 5. Why the special sine design does not yet prove (ET)

At initialization the Gaussian orthogonalization gives the previously
proved unit variance, approximately 6.4 percent nonlinear variance,
and correlation contraction. During training, the current top source
has a conditional Gaussian innovation of variance sigma_k^2. The exact
current curvature return is

\[
\mathbb E[\Phi''(Z_k)C_k\mid\text{past}]
=-4\beta e^{-2\sigma_k^2}C_k\sin(2\mu_k),
\qquad \Phi(z)=\alpha z+\beta\sin(2z).
\]

On bounded prefixes sigma_k^2 <= C h_{k-1}^2. Hence the damping factor
approaches one as the time mesh is refined. It is incorrect to apply the
initialized variance-one damping factor e^-2 at every training instant.

The conditional note also gives exact counterexamples to several proposed
ambient estimates: a bounded rank-one learned update can focus a Gaussian
transpose at one coordinate even for this positive-slope sine activation;
the raw loss is not weakly lower semicontinuous on the entire raw Hilbert
space; and its gradient is not locally Lipschitz or semiconvex there.
These are not states proved reachable by the actual initialized GF.
They invalidate those shortcuts without refuting the requested theorem.

## Research and review state

| Claim | Status |
| --- | --- |
| Exact-coefficient local population and full joint GF/GD theorem | Proved; independent hostile reconstruction passed |
| Actual finite GF global existence and compact-time raw-GD descent | Proved |
| Strong state/velocity endpoint of an existing population flow | Proved |
| Global canonical population flow conditional on (ET) | Proved conditional implication; independent review passed |
| (ET) for the actual sine training family | Open |
| Unconditional strong global population and full joint GF/GD limit | Open |
| Counterexample to the actual initialized global flow | Not obtained |

Three independent proof routes were pursued. Review scope and exact
versions are recorded in [REVIEW_STATUS.md](REVIEW_STATUS.md). No training
experiment was performed, and no older mathematical artifact was changed.

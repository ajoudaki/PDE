# Lean neural-PDE proof-obligation salvage

**Date:** 25 July 2026  
**Compute policy:** four bounded fresh diagnostics plus two reanalyses of completed raw trajectories; no full-grid campaigns  
**Fresh scientific compute:** approximately 179 seconds total  
**Claim scope:** diagnostic evidence, not preregistered full-gate certification

**Post-run audit:** every headline number below was independently recomputed
from the archived NPZ arrays. The recomputation matched the report exactly.
The same audit recovered one already-computed, previously omitted
same-dimension basis comparison; it is reported in Section 4.1. No additional
trajectory was run.

## Executive conclusion

Six research questions now have actual numerical evidence.

The evidence is favorable for the practical claim that the fixed \(P=5\)
neural PDE is a stable low-order surrogate:

- coupled width and depth corrections decreased at the tested scales;
- trained centered depth fluctuations followed the predicted
  \(L^{-1}\) variance law;
- a \(P\leq35\)-invisible same-state attack produced no large continuation
  gap;
- at the same rank five, a pilot-trained POD basis cut the held-out observable
  defect of the Hermite basis by about one half, while eight random
  orthonormal bases were orders of magnitude worse;
- two \(P=5\) cubature scrambles agreed to \(3.35\times10^{-4}\) in the
  normalized observable metric;
- both the dense ensemble and \(P=5\) PDE became extremely flat after fitting.

The result for the stronger arbitrary-accuracy conjecture is different:

> In the reduced nested \(P=5,15,35\) generator experiment, every principal
> defect was larger for \(15\leftarrow35\) than for \(5\leftarrow15\).

The adverse ratios ranged from \(2.54\) for the maximum high-to-low state
defect to \(26.53\) for the outgoing residual. The normalized observable
defects remained tiny in absolute size—at most \(3.83\times10^{-4}\)—so this
does not refute useful low-order accuracy. But it means this experiment gives
**no positive evidence that the pure Hermite hierarchy contracts with
increasing \(P\)**.

Accordingly:

\[
\boxed{\text{Useful low-order PDE: strengthened.}}
\qquad
\boxed{\text{Pure-Hermite arbitrary-accuracy convergence: still unresolved,
with a new adverse warning.}}
\]

## What was run

| Test | Fresh configuration | Wall time | Scope |
|---|---|---:|---|
| Ordered scaling | 4 coupled roots; \(n=64,128,256\); \(L=8,16,32\); \(T=0.5\) | 10.3 s | Reduced grid and horizon |
| Depth homogenization | \(n=128\); \(L=8,16,32,64\); 4 independent-\(W\) replicas; \(t=0,0.5\) | 4.4 s | Centered cancellation only |
| Same-state attack | \(n=128,L=16\); \(P\le35\)-invisible; 3 amplitudes; restart to \(0.5\) | 1.4 s | One reduced cell and root |
| Generator and shadow | Nested \(P=5,15,35\); \(M=625,N=4,R=128,\Delta t=0.04\); 6 checkpoints | 163.1 s | One seed; reduced \(N\), coarse \(\Delta t\) |
| Late-time drift | Reanalysis of canonical dense and PDE trajectories through \(t=8\) | no new solve | Observable tail only |
| \(P=5\) cubature | Reanalysis of the two completed frozen scrambles through \(t=2\) | no new solve | \(P=5\) only |

All numerical arrays in the seven new raw archives were checked to be finite.

## 1. Ordered width/depth target

Distances use

\[
d_{\rm obs}
=
\max\left\{
\sup_t\frac{\|\Delta f(t)\|_2}{S_f},
\sup_{t,s}\frac{\|\Delta G(s,t)\|_F}{S_G}
\right\}.
\]

For the four-root mean curves, successive width corrections contracted:

| Depth | \(D_{64\to128}\) | \(D_{128\to256}\) | Ratio |
|---:|---:|---:|---:|
| 8 | 0.10596 | 0.04891 | 0.462 |
| 16 | 0.09609 | 0.04685 | 0.488 |
| 32 | 0.09079 | 0.04707 | 0.518 |

At \(n=256\), the depth corrections were

\[
D_{8\to16}=0.02212,\qquad
D_{16\to32}=0.01278,\qquad
\frac{D_{16\to32}}{D_{8\to16}}=0.578.
\]

Every individual root also had a successive width ratio below one, and every
individual depth ratio was below one. Across-root RMS concentration fitted
log-width slopes from \(-0.621\) to \(-0.612\), comfortably steeper than the
protocol's directional target of \(-0.25\).

This is genuine evidence for an ordered limiting trend. It does not yet
resolve the target at the allocated accuracy: geometric continuation of the
observed ratios gives heuristic remaining width tails of \(4.2\%\)–\(5.1\%\)
after \(n=256\), and a \(1.75\%\) depth tail after \(L=32\).

**Verdict:** favorable contraction diagnostic; full ordered target unresolved.

## 2. Trained depth homogenization

At \(t=0.5\), the centered depth-average variance slopes were

\[
\alpha_{\rm forward}=-1.00219,\qquad
\alpha_{\rm backward}=-0.99982.
\]

The corresponding RMS slopes were \(-0.50110\) and \(-0.49991\). At
initialization the variance slopes were \(-1.00697\) and \(-1.01127\).
Thus the predicted

\[
\operatorname{Var}\!\left(L^{-1}\sum_\ell \xi_\ell\right)\asymp L^{-1},
\qquad
\operatorname{RMS}\asymp L^{-1/2}
\]

held almost exactly before and after training in this diagnostic.

The pooled-mean contrast did not decay with \(L\), but this statistic is not
the conditional/Onsager mean bias: it uses an in-sample pooled centering
reference and cannot identify a common missing mean term.

**Verdict:** strong support for centered trained-depth homogenization;
conditional/Onsager mean correctness remains untested.

## 3. Same-state continuation attack

The attack altered all \(16\) layers while preserving the retained
\(P=5,15,35\) row coordinates and current forward fields, adjoints, output,
Grams, and tangent kernel. The largest measured present-state relative defect
was

\[
5.28\times10^{-16}.
\]

For the strongest coherent amplitude \(\alpha=1\), the normalized observable
gap was

\[
0.00120\quad\text{at restart time }0.1,
\qquad
0.00332\quad\text{at restart time }0.5.
\]

The latter is \(0.332\%\), below the frozen \(1.5\%\) screen trigger. The
largest independent-attack gap was only \(3.36\times10^{-5}\).

**Verdict:** no large same-state counterexample was found. Because this is
one reduced cell and a null attack is one-sided evidence, it does not prove
that \((\theta,w)\) is sufficient.

## 4. Hermite generator consistency

The nested levels shared exactly the same valid \(P=70\)-compatible
quadrature master. The key successive-pair measurements were:

| Quantity | \(5\leftarrow15\) | \(15\leftarrow35\) | Successive ratio |
|---|---:|---:|---:|
| Integrated high-to-low state defect | \(1.526\times10^{-3}\) | \(4.016\times10^{-3}\) | 2.63 |
| Maximum high-to-low state defect | \(2.708\times10^{-3}\) | \(6.893\times10^{-3}\) | 2.54 |
| Maximum outgoing residual | \(1.233\times10^{-5}\) | \(3.271\times10^{-4}\) | 26.53 |
| Maximum normalized observable-generator defect | \(6.435\times10^{-5}\) | \(3.833\times10^{-4}\) | 5.96 |
| Maximum \(0.05\)-shadow observable error | \(2.916\times10^{-6}\) | \(1.733\times10^{-5}\) | 5.94 |

The high-to-low defects were at roundoff at initialization, became visible
after training, and failed to contract in the time-integrated, maximum,
observable, and shadow measurements. This is not a single-endpoint artifact.

The absolute observable defect is still only \(0.0383\%\), far below the
project's \(5\%\) practical tolerance. The warning concerns the direction of
the \(P\)-trend and therefore the arbitrary-accuracy claim.

Because this run used one cubature seed, \(N=4\), and
\(\Delta t=0.04\), it cannot distinguish a real noncontracting hierarchy from
a \(P=35\)-specific numerical issue. One matched resolution confirmation
would be required before treating it as a strong negative result.

**Verdict:** adverse noncontraction warning for pure-Hermite consistency.

### 4.1 Same-dimensional basis discriminator

The same generator archive also compared three rank-five subspaces inside the
resolved \(P=35\) coordinate space:

- the fixed first-five Hermite coordinates;
- eight seeded random orthonormal subspaces; and
- one trajectory-POD subspace fitted only on the predeclared pilot states at
  \(t=0,0.25,0.5\), then evaluated at held-out times \(t=1,1.5,2\).

The held-out maximum normalized observable defects were:

| Held-out time | Hermite | POD | POD/Hermite | Random median |
|---:|---:|---:|---:|---:|
| 1.0 | \(3.729\times10^{-4}\) | \(1.856\times10^{-4}\) | 0.498 | 0.610 |
| 1.5 | \(4.376\times10^{-4}\) | \(2.227\times10^{-4}\) | 0.509 | 0.671 |
| 2.0 | \(4.464\times10^{-4}\) | \(2.278\times10^{-4}\) | 0.510 | 0.679 |

POD also reduced the held-out state tail by \(76\%\)–\(79\%\). Its total
feedback defect was only \(2\%\) smaller at \(t=1\), but became \(36\%\) and
\(49\%\) smaller at \(t=1.5\) and \(t=2\).

This result rules out the idea that any arbitrary five-dimensional subspace
would work: Hermite is enormously better than random. It also shows that
Hermite is not dimension-optimal for this trajectory. But it does **not**
repair the adverse hierarchy result:

- the POD basis is trajectory-fitted and therefore is not an admissible fixed,
  architecture-local witness for the stated conjecture;
- its held-out window begins after the early \(t=0.25\)–\(0.5\) generator
  spike that controls the maximum noncontraction result; and
- even POD leaves a nonzero feedback defect, especially at \(t=1\).

**Verdict:** basis inefficiency is a real part of the obstruction, but the
experiment does not decide whether a fixed better basis suffices or whether
causal response/history coordinates are required.

## 5. Short-time amplification

Over a \(0.05\) shadow restart, the maximum normalized observable discrepancy
was \(2.92\times10^{-6}\) for \(5\leftarrow15\) and
\(1.73\times10^{-5}\) for \(15\leftarrow35\). There is no sign of explosive
short-time amplification in absolute terms, although the discrepancy again
grew rather than contracted with \(P\).

This is an actual shadow test, not the proposed worst-direction
tangent/adjoint gain over the full residual dictionary.

**Verdict:** small observed short-time amplification; worst-direction
finite-time stability unresolved.

## 6. Late-time observable tail

For the canonical \(\tanh\) model:

| System | Drift on \([2,4]\) | Drift on \([4,8]\) | Ratio |
|---|---:|---:|---:|
| Dense \(n=128,L=32\), 16-seed mean | \(5.413\times10^{-4}\) | \(6.920\times10^{-7}\) | \(1.28\times10^{-3}\) |
| \(P=5\) PDE | \(4.833\times10^{-4}\) | \(3.040\times10^{-7}\) | \(6.29\times10^{-4}\) |

The endpoint residual norms at \(t=8\) were \(4.99\times10^{-12}\) for the
dense mean and \(5.40\times10^{-13}\) for the PDE.

**Verdict:** very strong finite-horizon plateau evidence. State arclength,
late-time worst-direction perturbation stability, and a literal
\(t\to\infty\) envelope remain unresolved.

## 7. \(P=5\) cubature stability

The two completed \(P=5\), \(M=625,N=16,R=256\) scrambles differed by

\[
d_{\rm obs}=3.3542\times10^{-4}=0.0335\%,
\]

with output distance \(2.8537\times10^{-4}\), loss sup-difference
\(4.7977\times10^{-5}\), and minimum projected energies \(0.9999635\) and
\(0.9999623\).

**Verdict:** \(P=5\) numerical consistency is favorable; this does not resolve
\(P=15\) or \(P=35\).

## Gate ledger

| Proof obligation | Lean result | What remains |
|---|---|---|
| Ordered target | Favorable contraction | Full \(n,L,T\) grid and uncertainty |
| Depth homogenization | Favorable centered \(L^{-1}\) variance | Conditional/Onsager mean |
| State sufficiency | No large counterexample | More roots/cells; null is not proof |
| Hermite consistency | **Adverse noncontraction warning**; held-out POD improves rank-five defects | Matched resolution/seed confirmation; fixed-basis versus response enrichment |
| Finite-time stability | Small short shadow | Worst-direction tangent/adjoint gain |
| All-time stability | Extremely flat through \(t=8\) | State arclength, perturbations, infinite tail |
| Numerical cubature | Favorable at \(P=5\) | Higher-\(P\) cofinal resolution |

## Scientific interpretation

The new results make the mechanism more specific.

1. Failure of the ordered dense limit or of centered depth homogenization is
   not the leading explanation on the tested scales.
2. A gross failure of \(P\le35\) state sufficiency was not found.
3. The first clearly problematic link is the **generator-level Hermite
   contraction step**.

That points to three live explanations:

- \(P=35\) is numerically under-resolved even though \(P=5\) is stable; or
- the fixed Hermite ordering is inefficient, and another admissible
  architecture-local basis could contract; or
- pure static Hermite coordinates omit response/history information, so
  increasing \(P\) alone does not produce a contracting closure hierarchy.

The held-out POD result makes the second explanation concrete but does not
establish it, because POD was fitted to this trajectory and misses the early
defect peak. The present evidence therefore cannot choose among the three.
It does show why accurate \(P=5\) curves are not, by themselves, numerical
verification of the arbitrary-accuracy conjecture.

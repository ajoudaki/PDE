# Results: joint width/gradient-step side experiment

**Run date:** 23 August 2026.

**Frozen-rule verdict:** **evidence against a polynomially visible
instantaneous jump on the tested range**.  This is empirical evidence, not a
proof of the autonomous mean-field limit or of uniqueness.

The preregistration is
`DISCRETE_GD_JOINT_LIMIT_PREREGISTRATION_2026-08-23.md`.  The raw and
mechanically aggregated outputs are

- `experiment_discrete_gd_joint_limit_2026-08-23.jsonl`;
- `experiment_discrete_gd_joint_limit_summary_2026-08-23.json`.

## 1. Exact experiment

The run used ordinary simultaneous gradient descent in the original
parameters \((A,u,G_1,G_2)\), target \(y_\star=1\), and the exact frozen
metric/scaling.  Physical time was \(t=k\Delta\).  The grid contained

\[
n\in\{128,256,512,1024,2048\},\qquad
\Delta\in\{.04,.02,.01,.005,.0025\},
\]

six paired initialization keys, and horizon \(T=2\): 150 trajectories in
total.  Every trajectory completed and remained finite.

## 2. Step-size validity

For \(\Delta=.005\) versus \(.0025\), the largest 95th-percentile predictor
curve discrepancy over any width was

\[
3.32\times10^{-4}<10^{-2}.
\]

The largest median threshold-time discrepancy was \(1.42\times10^{-3}\).
At the finest step every loss increment was negative; the largest was
\(-6.44\times10^{-6}\).  The median normalized defect between the discrete
predictor increment and its gradient-flow derivative \(2eK\) was
\(2.00\times10^{-5}\).  Every preregistered numerical-validity gate passed.

## 3. Boundary-layer discriminator

At the finest step, the width-median threshold times were:

| threshold \(q\) | \(\tau_q(128)\) | \(\tau_q(2048)\) | endpoint ratio | width slope | bootstrap 95% slope interval |
|---:|---:|---:|---:|---:|---:|
| .25 | .1847 | .1751 | .948 | -.034 | [-.103, .024] |
| .50 | .4548 | .4476 | .984 | -.014 | [-.060, .034] |
| .75 | .8964 | .8942 | .997 | -.006 | [-.041, .030] |
| .90 | 1.4401 | 1.4402 | 1.000 | -.004 | [-.031, .025] |

An instantaneous limit \(f(t)=1\) for every \(t>0\) would require all these
times to shrink toward zero.  Instead, they stabilize at visibly positive
and threshold-dependent values.  All endpoint ratios and confidence
intervals passed the frozen regular-flow rule.

The maximum difference between the width-median \(n=1024\) and \(n=2048\)
predictor curves on the frozen time grid was \(0.0147<0.05\).  At \(n=2048\)
the median predictor was only \(0.0428\) at \(t=.02\), then \(0.1583\) at
\(t=.1\), \(0.5377\) at \(t=.5\), \(0.7897\) at \(t=1\), and \(0.9624\) at
\(t=2\).  This is a resolved continuous rise, not a numerically hidden jump.

## 4. Kernel mechanism

The median initial raw kernel changed from \(0.8305\) at width 128 to
\(0.8265\) at width 2048, an endpoint factor \(1.005\), with width slope
\(0.011\).  The maximum kernel before \(f=.75\) changed by a symmetric factor
only \(1.014\), with slope \(0.0014\).  Thus no growing initial or
pre-threshold kernel accompanies the width limit.

The compact-time median \(\|R_2\|_{p,n}/p\) also stayed stable descriptively:
its width-128/2048 values were \(.429/.437\) for \(p=2\), \(.280/.281\) for
\(p=4\), and \(.182/.187\) for \(p=8\).

## 5. Explicit joint-limit diagonal

Along the preregistered sequence

\[
(128,.04),(256,.02),(512,.01),(1024,.005),(2048,.0025),
\]

the median maximum predictor discrepancy from the finest-step curve at the
same width was, respectively,

\[
.00389,quad .00164,quad .000810,quad .000253,quad0.
\]

Thus the prescribed simultaneous \(n\uparrow\infty,\Delta\downarrow0\)
sequence is already inside the resolved step-size regime and approaches the
same stable family of curves over the tested range.

## 6. Claim-level interpretation

The experiment strongly distinguishes this arctangent depth-three model from
the proposed quadratic instantaneous-collapse mechanism at widths through
2048 and physical times through 2.  It provides no evidence of a shrinking
initial layer, divergent kernel, loss discontinuity, or path dependence in
the joint width/step limit.

It does **not** prove that a slower boundary layer cannot appear beyond the
tested widths, establish exponential tails through \(p\asymp\log n\), prove
operator-topology convergence, or supply uniqueness of the limiting IDE.
Those remain theorem-level obligations.

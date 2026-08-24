# Quadratic L=2 joint width/step experiment: results

**Date:** 23 August 2026.

## Outcome

The separately declared step-halving confirmation passes every frozen
numerical gate and records

> **confirmatory evidence against a polynomially visible instantaneous
> jump.**

Thus the quadratic model is quantitatively much faster and sharper than the
depth-three arctan control, but it does **not** show the opposite qualitative
width trend on \(n=128,\ldots,2048\).  In particular, its learning transition
does not visibly collapse toward \(t=0\).

This is a finite-width numerical result, not a proof of a continuous
mean-field limit.  It also cannot exclude a tail-driven boundary layer that
emerges only beyond these widths or on a slower-than-polynomial scale.

## Audit trail

The primary frozen grid contained 150 trajectories:

- widths \(128,256,512,1024,2048\);
- six independent keys per width;
- steps \(.02,.01,.005,.0025,.00125\);
- exact simultaneous metric GD through \(T=2\).

All trajectories were finite.  The primary verdict nevertheless remained
formally **inconclusive**, because the \(.0025\)-versus-\(.00125\) 95th
percentile maximum-curve discrepancy was \(0.0100\)--\(0.0124\) at four
widths, narrowly above the frozen \(0.0100\) gate.  Hitting-time discrepancies
were already below \(6.3\times10^{-4}\).

The two successive Euler discrepancies contracted by factors
\(2.01\)--\(2.02\), identifying ordinary first-order time-discretization error.
A separate confirmation was therefore frozen and then run at
\(\Delta=.000625\), without changing widths, seeds, architecture, horizon, or
scientific cutoffs.  This added 30 trajectories.

In the confirmation:

- every trajectory remained finite;
- the 95th-percentile curve discrepancy was \(0.00376\)--\(0.00616\) at every
  width, below \(0.01\);
- median threshold-time discrepancies were at most \(3.14\times10^{-4}\),
  below \(0.005\);
- loss was monotone up to \(1.8\times10^{-30}\) roundoff;
- the old/new Euler-error ratios were \(2.004\)--\(2.010\).

## Width scaling at the resolved step

The table reports median threshold times from the \(\Delta=.000625\)
trajectories.

| threshold \(q\) | \(\tau_q(128)\) | \(\tau_q(2048)\) | endpoint ratio | log--log slope | bootstrap 95% interval |
|---:|---:|---:|---:|---:|---:|
| .25 | .05621 | .05433 | .9666 | .0196 | [-.1724, .1454] |
| .50 | .08136 | .07617 | .9362 | -.0017 | [-.1608, .0751] |
| .75 | .10019 | .09242 | .9224 | -.0129 | [-.1569, .0432] |
| .90 | .11586 | .10584 | .9135 | -.0176 | [-.1520, .0303] |

All endpoint ratios lie in the frozen regular range \([.75,1.25]\), all
central slopes lie in \([-.10,.10]\), and all bootstrap intervals lie within
\((-.20,.20)\).  The maximum difference between the \(n=1024\) and \(2048\)
median curves on the registered time grid is \(0.01751<0.05\).

The early-time diagnostic is also far from a visible step: median
\(f_{2048}(.01)=0.03165\), not above \(0.75\), and the last three widths are
not monotone at this time.

## Kernel and extreme-neuron diagnostics

The median initial tangent kernel changes from \(1.466\) at width 128 to
\(1.768\) at width 2048 (factor \(1.206\), slope \(0.0398\)).  The median
maximum kernel before \(f=.75\) changes from \(21.48\) to \(26.55\) (factor
\(1.236\), slope \(0.0656\)).  Both pass the frozen stability gate.

The median fraction of the readout-kernel block carried by its largest
coordinate decreases with width:

- initially, from \(0.184\) at \(n=128\) to \(0.0307\) at \(n=2048\);
- maximized before \(f=.75\), from \(0.284\) to \(0.102\).

Thus this width range shows no growing single-coordinate condensation.  The
quadratic flow is fast because its kernel grows strongly during learning,
not because the measured transition time is vanishing with width.

## Scope of the inference

The conditional \(f(0)=0, f(t)=1\) trace in the quadratic audit depends on
an unproved tagged-site/Volterra representation and a relaxed solution
selection.  This experiment weighs against that discontinuity being visible
at polynomially accessible widths.  It does not logically refute the
conditional derivation, prove tightness or uniqueness of an infinite-width
path law, or establish uniform convergence on compact time intervals.

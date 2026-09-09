# Minimal scalar stress test of activation nonlinearity and Hermite order

**Date:** 25 July 2026  
**Scope:** canonical dense Euclidean \(\mu\)P residual model, reduced to
\(m=d=1\), plus one smooth odd activation stress  
**Scientific wall time:** 414.71 seconds across all admitted trajectories  
**Status:** complete; no computation remains running

## Executive verdict

The experiment resolves the user's proposed explanation in two different
directions.

1. **The old task was not maximally nonlinear relative to a gain-adjusted
   linear network.** A theory-selected scalar stress activation,

   \[
   \phi(z)=\frac{\sin(2.5z)}{2.5},
   \]

   makes the fixed initialization-gain linear control miss the learned Gram
   trajectory by \(17.70\%\) in the neural PDE and \(15.95\%\) in the paired
   dense-network ensemble. Even the RMS-matched linear control misses the PDE
   Gram trajectory by \(8.68\%\). This decisively exceeds the previous
   \(3.46\%\) gap.

2. **Strong activation nonlinearity does not imply strong dependence on
   higher immutable-label Hermites.** In the same stress case, the
   degree-one source-Hermite PDE is only \(0.339\%\) from degree 11 at
   \(y=2\), and only \(0.247\%\) from degree 13 after the predeclared
   \(y=4\) feature-learning escalation. Higher orders make small corrections,
   but the adjacent corrections are not monotone.

For canonical \(\tanh\), a properly resolved degree-\(7,9,11,13\) ladder was
run twice. The degree-\(11\to13\) projective state increment contracted by
\(4.2\%\) relative to \(9\to11\) in one cubature scramble, but grew by
\(91.3\%\) in the independent scramble. Therefore the turnover did not
replicate. The corresponding degree-\(11\to13\) Gram effects were only
\(0.0046\%\) and \(0.0061\%\) of total Gram motion.

The honest conclusion is:

> The scalar experiment strongly supports the practical usefulness of a
> very low-order PDE, and it decisively rejects the claim that this success
> is merely a fixed effective-gain linear model. It does not provide a
> replicated monotone \(P\)-convergence trend, so arbitrary-accuracy
> pure-Hermite convergence remains unproved.

## 1. Why the scalar reduction has high leverage

With one scalar input and one sample,

\[
X=[1],\qquad y\in\{2,4\},
\]

the immutable Gaussian neuron label is

\[
\theta=(B(0),a(0)/A)\in\mathbb R^2.
\]

For an odd activation, the exact global sign symmetry removes all even
Hermite degrees. The active mode counts are therefore:

| maximum odd degree | active modes |
|---:|---:|
| 1 | 2 |
| 3 | 6 |
| 5 | 12 |
| 7 | 20 |
| 9 | 30 |
| 11 | 42 |
| 13 | 56 |

The old four-label degree-seven experiment required 200 active modes. The
scalar case therefore reaches degree 13 with less than one third as many
active modes.

The observable remains nontrivial. At every physical-depth node,

\[
G(s,t)=\mathbb E[h(s,\theta,t)^2]
\]

is the scalar hidden Gram, so the experiment predicts a full variance path
over training time and continuous depth, as well as output and loss.

## 2. Theory-selected nonlinear stress

The stress activation was selected before running a trajectory. It is:

- smooth and entire;
- odd;
- bounded;
- exactly 1-Lipschitz, since \(\phi'(z)=\cos(2.5z)\).

At the initialization preactivation variance \(q=\sigma_w^2=0.65^2\), its
best zero-intercept Gaussian linear projection is

\[
\kappa_{\rm init}
=\mathbb E[\phi'(Z)]
=e^{-2.5^2q/2}
=0.2670518352.
\]

Its RMS-matched gain is

\[
\kappa_{\rm rms}
=\sqrt{\frac{\mathbb E[\phi(Z)^2]}{q}}
=0.4340346412.
\]

The fraction of activation \(L^2\) energy orthogonal to the first linear
Hermite component is

\[
1-\frac{\kappa_{\rm init}^2q}{\mathbb E[\phi(Z)^2]}
=62.14\%.
\]

For comparison, the same initialization quantity is \(3.01\%\) for
\(\tanh\), \(10.23\%\) for \(\tanh(2z)/2\), and \(19.79\%\) for
\(\tanh(4z)/4\). This is why the sine stress was used instead of another
activation grid.

## 3. Frozen decision tree

The admitted sequence was:

1. \(y=2\), \(\tanh\) and sine, odd degrees \(1,3,5,7,9,11\);
2. two fixed linear controls for sine;
3. eight paired dense-network seeds for sine and its initialization-gain
   linear control;
4. because the degree-one correction was below \(1\%\) and the top Cauchy
   increment did not contract, the sole \(y=4\), degree-13 escalation;
5. because the \(R=128\) degree-13 fast cubature was nearly rank deficient,
   one \(R=512\) canonical-\(\tanh\) rerun and one independent scramble
   containing only the top three degrees.

No activation grid, label grid, two-input extension, degree 15, long-time
campaign, bootstrap campaign, or subagent campaign was run.

The primary PDE settings were

| item | value |
|---|---:|
| depth nodes \(N\) | 4 |
| tensor base order | 14 |
| base points \(M\) | \(14^2=196\) |
| fast points \(R\) | 128 initially, 512 for the decisive tail check |
| time step | 0.025 |
| horizon | \(t=2\) |
| integrator | explicit midpoint |

The paired dense diagnostic used width \(128\), physical depth \(16\), and
eight seeds.

## 4. Gain-adjusted linear question

All reported curve distances use increments from initialization and a common
scale fixed across the compared trajectories.

### 4.1 Neural-PDE comparison

| linear control versus degree-11 sine PDE | Gram | output | loss |
|---|---:|---:|---:|
| initialization gain \(\kappa_{\rm init}\) | **17.70%** | 7.12% | 7.51% |
| RMS gain \(\kappa_{\rm rms}\) | **8.68%** | 3.95% | 4.68% |

Both fixed-gain controls fail the project's 5% Gram criterion.

### 4.2 Paired dense-network comparison

The paired dense ensemble gives:

| comparison | Gram | output | loss |
|---|---:|---:|---:|
| ensemble-mean linear versus sine | **15.95%** | 6.55% | 6.95% |
| mean of eight paired per-seed Gram distances | **16.47%** | — | — |
| standard error of paired per-seed Gram distances | 0.58% | — | — |
| per-seed Gram range | 14.40%–18.75% | — | — |

The degree-11 sine PDE was \(2.50\%\) from the dense ensemble-mean Gram
increment curve and \(2.81\%\) from its output curve. The loss distance was
\(5.54\%\), so this small dense diagnostic does not pass a joint all-metric
5% rule.

The gain result is nevertheless clear: every paired dense seed has a Gram
distance far above 5%.

## 5. Did higher Hermites become useful?

### 5.1 Sine stress

At \(y=2\), using degree 11 as the internal reference:

| source degree | Gram distance to degree 11 |
|---:|---:|
| 1 | 0.339% |
| 3 | 0.369% |
| 5 | 0.297% |
| 7 | 0.205% |
| 9 | 0.194% |

At the stronger \(y=4\) escalation, using degree 13 as reference:

| source degree | Gram distance to degree 13 |
|---:|---:|
| 1 | 0.247% |
| 3 | 0.274% |
| 5 | 0.233% |
| 7 | 0.178% |
| 9 | 0.174% |
| 11 | 0.115% |

There is a broad reduction after degree 3, and degree 11 is closer to degree
13 than degree 1 is. But the sequence is not monotone, and the entire
degree-one-to-degree-13 correction is only \(0.247\%\). Against the finite
dense target, all PDE orders lie near the same \(2.4\%\)–\(2.5\%\) Gram
error floor.

Thus this experiment does not exhibit a large practical payoff from higher
source-label Hermites. It shows something more informative: a trajectory can
be strongly nonlinear relative to every tested fixed gain while remaining
very simple as a function of the immutable neuron label.

### 5.2 Canonical \(\tanh\) Cauchy ladder

The \(R=128\) pilot was not admissible for a high-shell conclusion. Its raw
fast-cubature condition numbers were:

| degree | condition number |
|---:|---:|
| 7 | 6.29 |
| 9 | 25.59 |
| 11 | 157.97 |
| 13 | 2897.99 |

At \(R=512\), the degree-13 condition number fell to 3.47.

The two independent well-conditioned runs then gave:

| quantity | scramble 1 | scramble 2 |
|---|---:|---:|
| \(E_{11\to13}/E_{9\to11}\), projective state | 0.958 | 1.913 |
| outgoing-tail ratio | 0.894 | 1.893 |
| Gram-increment ratio | 1.138 | 3.989 |
| absolute \(E_{11\to13}\) | 0.008996 | 0.009350 |
| normalized degree-\(11\to13\) Gram effect | 0.00462% | 0.00608% |

The first aggregate turnover did not replicate. The absolute top state
increment is fairly consistent across scrambles, but the preceding
degree-\(9\to11\) denominator is not. There is therefore no resolved
monotone Cauchy trend through degree 13.

## 6. Why activation Hermites and source Hermites differ

The central conceptual distinction is:

- the PDE evaluates the full \(\phi(z)\) and \(\phi'(z)\) at every \(P\);
- \(P\) truncates only the dependence of the learned row operator on the
  immutable Gaussian neuron label \(\theta\).

Consequently, increasing activation nonlinearity can make a linear network a
bad predictor without forcing the learned row law to develop large
high-degree dependence on \((B(0),a(0))\).

The scalar sine result is a direct empirical example:

\[
\text{linear-control Gram error}=17.70\%,
\qquad
\text{degree-1 versus degree-11 Gram error}=0.339\%.
\]

These numbers answer different questions and differ by a factor of roughly
52.

## 7. What theory really guarantees

Let \(\{\psi_\alpha\}\) be the Hermite basis on
\(L^2(\gamma_2)\), and let

\[
\mathcal N\psi_\alpha=|\alpha|\psi_\alpha
\]

be the Gaussian number operator. For any fixed field \(u\) with

\[
\|u\|_{\mathcal H_\gamma^s}^2
=\sum_\alpha(1+|\alpha|)^s|u_\alpha|^2<\infty,
\]

the complete-degree projection \(\Pi_p\) obeys

\[
\|(I-\Pi_p)u\|_{L^2(\gamma_2)}
\le
(p+1)^{-s/2}\|u\|_{\mathcal H_\gamma^s}.
\]

If the coefficients have an exponential number-operator weight, the
projection tail is exponentially small. This is the rigorous reason a
Hermite expansion of a **fixed sufficiently regular field** converges.

It is not yet a convergence theorem for the trained Galerkin flows
\(Y_p(t)\). For that, one needs a cutoff-independent bound such as

\[
\sup_p\sup_{t\le T}
\|Y_p(t)\|_{\mathcal H_\gamma^s}<\infty
\]

in a source-mode-coercive class, plus uniqueness and cutoff-uniform forced
stability in a weaker norm. Under those assumptions, the projection tail
bound and a Grönwall/forced-stability estimate yield an arbitrary-accuracy
Galerkin bound.

The scalar reduction helps because shell cardinality grows only linearly and
the number-operator scale has a compact embedding into \(L^2(\gamma_2)\).
It does not itself propagate the required weighted regularity. The
unbounded Gaussian readout boundary and nonlinear adjoint products remain the
analytic difficulty identified in the previous compactness report.

## 8. Gate ledger

| gate | result |
|---|---|
| Construct a \(>5\%\) gain-adjusted-linear Gram failure | **Pass:** 17.70% PDE, 15.95% dense |
| Keep the high-order nonlinear PDE within 5% of dense Gram/output | **Pass:** 2.50% / 2.81% |
| Joint dense Gram/output/loss 5% rule | **Fail/boundary:** loss 5.54% |
| Make degree-one source truncation fail by \(>1\%\) | **Fail:** at most 0.339% |
| Show higher orders broadly reduce internal error | **Weak pass:** small overall reduction |
| Show monotone adjacent observable contraction | **Fail:** nonmonotone |
| Show replicated top state-tail contraction | **Fail:** ratios 0.958 and 1.913 |
| Prove arbitrary-accuracy convergence | **Not established** |

## 9. Final interpretation

The user's proposed minimal experiment was the right strategic reduction. It
produced two high-value results cheaply:

1. a decisive nonlinear regime in which gain-adjusted linear dynamics are
   genuinely inadequate;
2. evidence that this activation-level nonlinearity is not the missing
   mechanism behind the higher-\(P\) convergence difficulty.

The practical low-order PDE claim is stronger after this round: degree one
tracks a deliberately nonlinear scalar task extremely closely, and the
high-order PDE tracks the dense Gram/output curves within about 2.5%–2.8%.

The arbitrary-accuracy claim is not stronger in the required theorem-facing
sense. The remaining gap is still uniform source-mode regularity/compactness
and cutoff-uniform stability, not a lack of activation nonlinearity.

## 10. Reproducibility

The runner reuses the existing audited PDE and dense vector fields and adds
the sine activation only at process runtime. The raw archives include every
saved output, loss, and depth-Gram curve.

Key SHA-256 values:

- runner:
  `9a56b4f76870e168f39bb7a1a0e482a53dcbfb9d45436caac883eb1ddb512ee8`
- \(y=2\) main JSON:
  `0f72abbe78ec03e756e8411156375510255514aa7e503eb612dda29a73551b8f`
- \(y=2\) main NPZ:
  `26899c461de7983ae9d81f62c51694085de514a4b04e3213920961d1c43d257d`
- \(y=4\), degree-13 JSON:
  `873f6a797c46c4c257773c10d5dd358151e63789c6f073b9e91127763d944c5a`
- \(y=4\), degree-13 NPZ:
  `15385fef7edbf7db0186597cd07c69c62cbf75a19a9dd6319bad0c982027a9b8`
- high-resolution scramble 1 JSON:
  `7bb22a84f562a8762ce47772fa686f8afb12e3d77551ca329ac147efa6536bfe`
- high-resolution scramble 1 NPZ:
  `f366677ca6d650d57d61335c0c08fe386c4723e896f67332de3347e74dc7e154`
- high-resolution scramble 2 JSON:
  `432801dbc144fecbbfefa6f473c502ca6b570705dd3258a1385fd9860aef2ff9`
- high-resolution scramble 2 NPZ:
  `14ba72d080bf66b7074dc8c43fb5d466c106a5c61e593b2e08fb7c5aabbabbc3`

The first two pilot archives record the pre-dispatch runner hash
`ce75ef5d...`; the final runner adds only CLI switches that allow activation
and baseline subsets. The scientific default path used by those pilots is
unchanged. The two decisive \(R=512\) archives record and match the final
runner hash exactly.

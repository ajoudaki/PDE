# Direct scalar compression: population comparison without Fourier

Date: 2026-09-26. Status: internally checked implementation and bounded
experimental evidence; no promotion or impossibility theorem.

**The tested affordable aggregate truncations do not accurately replace the
population closure.** This conclusion no longer involves Fourier extraction:
the scalar ODE evolves the requested passive outputs directly. It also evolves
training-input Gram matrices at both hidden layers. Good training fit often
coexists with large passive-output errors and inconsistent Gram matrices.

The experiment implements the clipped contraction hierarchy proposed in
[the approximate scalar construction](APPROXIMATE_SCALAR_POPULATION_COMPRESSION.md).
It compares against the original-clock population closure at the **same
history order P**, initialization, data and physical time. It does not compare
against the dense network, so the discrepancy measured here isolates the
additional scalar approximation. A failure to track the parent does not
depend on how accurately that parent tracks dense training.

## What is implemented

There are two tanh hidden layers of width n:

\[
h_1(x)=\tanh(wx),\qquad h_2(x)=\tanh(Wh_1(x)),\qquad
f(x)=\frac1n c^\top h_2(x).
\]

The circle inputs here are the already normalized coordinates
\(x=(\cos\theta,\sin\theta)\). Training uses mean squared loss on m samples,
canonical block mobilities \((n,1,n)\), and the original activity clock.
The population parent retains P raw Legendre history modes per sample, uses
the constant-forward/zero-backward prefix of length one, and reconstructs W
with the unchanged initialized matrix plus its moment correction. No biases,
normalization layers or hidden initialization gains are used.

The scalar compiler starts from these requested observables:

\[
f(x_a),\quad f(q_j),\qquad
G^{(\ell)}_{ab}=\frac1n\sum_i h_{\ell,i}(x_a)h_{\ell,i}(x_b),
\quad \ell=1,2.
\]

Here \(x_a\) are training inputs and \(q_j\) are passive query inputs. The
queries have no labels, residuals, training weight or history sources. They
measure the same evolving fitted function without changing training.

For example, the exact product rule gives

\[
\dot f(q)=\frac1n\sum_i
 \bigl(\dot c_i h_{2,i}(q)+c_i\dot h_{2,i}(q)\bigr),
\quad
\dot G^{(\ell)}_{ab}=\frac1n\sum_i
 \bigl(\dot h_{\ell,i}(x_a)h_{\ell,i}(x_b)
       +h_{\ell,i}(x_a)\dot h_{\ell,i}(x_b)\bigr).
\]

Substituting the population equations introduces mixed activation, backward
response and history-moment contractions. The compiler recursively retains
the contractions needed for their equations. Shared initialized-matrix
contractions preserve the same W0 and its transpose. There is no redrawing
of W0 and no frozen response subspace.

Each connected contraction is represented by a decorated tree. Its grade K
counts vertices, edges and field decorations. A finite system deletes a
whole right-hand-side product when any connected factor exceeds the chosen
cutoff. It recursively includes the remaining factors. This is the additional
approximation being tested. P and K are different resolutions.

The primary variant clips arguments of the scalar right-hand side and its
reported observables to certified coordinate bounds for the parent on
\([0,12]\). It does not clip derivatives or project the state after a step.
These bounds leave the parent aggregates unchanged. They follow from
\(\|c(t)\|^2\le\|c(0)\|^2+n\,\mathrm{mean}(y^2)T\), bounded tanh,
history projection contraction, and positive contractions using entrywise
\(|W_0|\). They are derived from initialization and data, not fitted to a
reference trajectory. They do not enforce Gram positivity.

The scalar runtime contains only scalar initial conditions, caps, labels,
coefficient tables and index tables. It has no neuron arrays, initialized
matrices, population callbacks or Fourier coordinates. Neuron contractions
are used once to initialize it. Query and Gram descendants can make the
scalar state large, but its compiled dimension at fixed m, P and K does not
depend on n. Its cap values, initial values and accuracy can depend on n.

The reference is implemented independently using physical network responses
and raw history moments. Its hidden matrices are materialized for validation.
It represents exactly the same population equations as the main consolidated
implementation; fixed-state comparisons at depths two and three, orders one
and two, agreed to \(2.23\,10^{-16}\).

## Code and interface

The main consolidated suite is unchanged.

| File | Purpose |
|---|---|
| [scalar_direct.py](scalar_direct.py) | Scalar compiler, direct outputs, hidden Grams, caps and scalar-only runtime |
| [scalar_population_reference.py](scalar_population_reference.py) | Independent population reference and initialization |
| [run_scalar_direct.py](run_scalar_direct.py) | Fixed experiment panel, resource caps, trajectories and comparisons |
| [check_scalar_direct.py](check_scalar_direct.py) | Independent algebra and passive-query checks |
| [plot_scalar_direct.py](plot_scalar_direct.py) | Figures recomputed from saved trajectories |

Only ordinary contraction-tree utilities and coefficient-table packing are
imported from the existing scalar_fourier_engine.py. No Fourier block or
angular quadrature is instantiated.

With the study directory on the Python import path, the minimal interface is:

    import numpy as np
    from scipy.integrate import solve_ivp
    from scalar_direct import ScalarCompiler
    from scalar_population_reference import initialize, PopulationReference

    def circle(degrees):
        angle = np.deg2rad(degrees)
        return np.column_stack((np.cos(angle), np.sin(angle)))

    X, y = circle([10, 125]), np.array([1., -1.])
    Q = circle([55, 205, 310])
    parent = PopulationReference(X, y, initialize(16, 20260920), order=1)
    compiler = ScalarCompiler(X, y, Q, cutoff=3, order=1)
    runtime, bounds = compiler.initialize(parent, horizon=12.)
    # Only runtime is needed below; it can be pickled and run independently.
    solution = solve_ivp(runtime.rhs, (0., 12.), runtime.initial,
                         method="DOP853", rtol=2e-7, atol=2e-9)
    outputs = runtime.observables(solution.y[:, -1])
    # outputs contains train, test, grams and clock.

Compiler and parent must use identical inputs, labels, depth and P, and the
canonical initial history. The interface currently checks depth and P
explicitly; matching data is a caller precondition. Certified caps apply
through the selected horizon, not an arbitrary later time or arbitrary
memory restart. The example demonstrates the interface, not accurate
prediction at this cutoff.

## Fixed test panel

The [protocol](SCALAR_DIRECT_PROTOCOL.md) was written before the panel ran.

| Task | Training angles | Labels |
|---|---|---|
| broad_pair | 10°, 125° | +1, −1 |
| close_pair | 10°, 45° | +1, −1 |
| triple | 10°, 75°, 145° | +1, −1, +1 |

All tasks use passive angles 55°, 205°, 310°, widths 16 and 64, and seeds
20260920 and 20260921. Entries of w, W0 and c have standard deviations 1,
\(1/\sqrt n\), and \(1/n\), respectively. P=1 is tested on all tasks; P=2
is tested on broad_pair. The declared cutoffs are K=3,5,7, with a K=9
compilation attempt on broad_pair at P=1.

The horizon is 12, with 121 shared observation times. A path error is the
maximum of the samplewise RMS discrepancy over these observation times.
It is not a certified continuous-time supremum. Gram RMS uses all entries
of the training Gram matrix, separately at each layer. The success gate is
at most 0.02 for training outputs, passive outputs and both Gram errors;
an error above 0.10 in any one is the failure screen.

All sixteen parent runs completed. Thirteen reached training RMS 0.05;
the exceptions were three triple-task runs. All broad_pair and close_pair
parents fitted by the horizon. The triple comparisons remain valid
fixed-time tracking tests, but those three endpoints are not fitted models.

## Accuracy results

Forty primary scalar solves were attempted. Twenty-four completed; **all
twenty-four crossed the declared accuracy-failure screen**. Sixteen did not
produce a numerical endpoint within the gates/budget. The latter are not
counted as measured accuracy failures.

The following entries are medians over the four width/seed combinations.
Every listed row has four completed trajectories.

| Task | P | K | Scalar state size | Passive path RMS error | Passive final RMS error | Layer-1 Gram path error | Layer-2 Gram path error |
|---|---:|---:|---:|---:|---:|---:|---:|
| broad_pair | 1 | 3 | 53 | 0.124 | 0.110 | 0.140 | 0.285 |
| broad_pair | 1 | 7 | 2672 | 0.248 | 0.090 | 0.323 | 0.502 |
| close_pair | 1 | 3 | 53 | 0.928 | 0.914 | 0.146 | 0.140 |
| close_pair | 1 | 7 | 2672 | 0.525 | 0.357 | 0.307 | 0.148 |
| triple | 1 | 3 | 89 | 0.417 | 0.355 | 0.146 | 0.120 |
| broad_pair | 2 | 3 | 89 | 0.127 | 0.110 | 0.134 | 0.302 |

The close_pair K=7 models have median final training RMS
\(1.08\,10^{-7}\), while their median final passive discrepancy is 0.357.
Thus training loss alone would give a misleading impression of success.
K=7 improves the close_pair passive errors relative to K=3, but broad_pair
path errors worsen. These finite cutoffs show no general monotone improvement.

### A concrete fitted example

For broad_pair, P=1, n=16, seed 20260920, both the parent and K=7 scalar
model fit the training labels: final training RMS is 0.00420 and 0.00264,
respectively. Their final passive predictions are:

| Angle | Population parent | Scalar K=3 | Scalar K=7 |
|---|---:|---:|---:|
| 55° | 0.59845 | 0.27276 | 0.30195 |
| 205° | −0.95068 | −0.83192 | −0.85877 |
| 310° | 1.01651 | 1.06554 | 1.01903 |

The K=7 passive final RMS discrepancy is 0.17923, and its maximum sampled
path discrepancy is 0.22225. At the parent's first fitted time, the passive
RMS discrepancy is already 0.10902.

More diagnostically, the final first-layer training Grams are

\[
G_{\rm parent}=
\begin{pmatrix}0.68572&-0.37126\\-0.37126&0.49455\end{pmatrix},
\qquad
G_{\rm scalar}=
\begin{pmatrix}0.01341&0.18960\\0.18960&-0.07050\end{pmatrix}.
\]

The second diagonal entry of the scalar matrix purports to be an average of
squared activations, yet it is negative. It cannot describe any real neuron
population. Merely including Gram entries as evolving coordinates does not
preserve their algebraic and positivity constraints.

This is a feature-learning comparison: the parent's final-minus-initial
Gram RMS changes are 0.22380 and 0.32281 in the two layers.

### Integration, clipping and instantaneous defect controls

Tightening DOP853 tolerances from 2e-7/2e-9 to 2e-9/2e-11 changes the flagship
K=7 training outputs by at most \(2.55\,10^{-7}\), passive outputs by
\(1.31\,10^{-6}\), and Gram entries by \(6.35\,10^{-6}\), across the common
observation grid. The corresponding parent changes are below
\(8.23\,10^{-8}\). These changes are far below the discrepancies above.
This is a strong numerical check of the main witness, not a refinement
certificate for every cell in the panel.

The unclipped K=7 control also completes: passive path/final errors are
0.22225/0.17902, versus 0.22225/0.17923 with clipping. Its minimum sampled
Gram eigenvalue is −0.40554, versus −0.40549 with clipping. Clipping is
therefore not the main explanation of this example's failure.

For a separate diagnostic, the scalar right-hand side was evaluated on
**exact aggregates of the independently evolved parent**, at times 0,1,4,12.
These values were never supplied to the scalar solver. At t=1 in the same
flagship case, the passive-output velocity defect has RMS 0.09584 for K=3
and 0.41408 for K=7. Missing terms can already give a substantial velocity
error before any scalar-state discrepancy is introduced. Retaining more
terms at these low cutoffs does not necessarily improve cancellations.

## Numerical failures and computational costs

Every K=5 primary solve failed to return a certified numerical endpoint under
the declared limits: eight P=1 two-input runs triggered the state/clock
numerical gate; four triple P=1 and four broad_pair P=2 runs reached the
45-second solve cap. These outcomes do not prove blow-up of the clipped
continuous ODE, which has a separate global-existence argument.

Compilation of broad_pair P=1 K=9, triple P=1 K=7 and broad_pair P=2 K=7
stopped at the one-million-retained-term cap. Failed and incomplete records
are retained. No cutoff, label, seed or cap was adjusted after observing
accuracy.

| Two-input P=1 cutoff | Scalar state size | RHS terms | Coefficient/index table bytes |
|---|---:|---:|---:|
| K=3 | 53 | 574 | 18,368 |
| K=5 | 445 | 26,320 | 842,240 |
| K=7 | 2672 | 291,294 | 9,321,408 |

The K=7 runtime arrays, including caps and initial state, total 9,364,220
bytes. For comparison, the n=64 parent has 449 evolving scalar entries plus
4096 initialized-matrix entries, or 36,360 bytes for those arrays. These are
array-storage counts, not full process-memory or solver-workspace counts.
Width-independent state size does not imply a memory benefit at these widths.

Broad_pair P=1 median scalar solve times are 0.032 seconds at K=3 and
3.425 seconds at K=7. Compiler and initialization costs are additional.
Compilation is shared across widths and seeds. Runtime uses vectorized
products and grouped sums; pruning before tree canonicalization preserves
the selected equations while reducing compilation work.

The full declared campaign used 569.29 cumulative worker seconds, below its
1800-second cap, and ended after its fixed panel and controls. Algebra checks
and figure generation are separate from that campaign total.

## Validation and evidence

The pre-training algebra suite passed at P=1 and P=2 with nonzero history
states. It checks every packed retained row, independently splits selected
output/Gram/descendant product rules into retained and omitted contributions,
and exercises 16,233 nonzero omitted terms. Maximum primitive-template
discrepancy is \(4.17\,10^{-16}\); directional finite-difference error is
below \(4.83\,10^{-12}\).

Additional checks cover passive nonfeedback, a duplicate passive/training
query, zero residual, transpose orientation, clipping semantics, initial
outputs/Grams, and serializing a runtime containing only scalars and tables.
The independent reference also passes the local dense-gradient, reconstruction
derivative and query-derivative checks at depths one, two and three.

All campaign records match the frozen source hashes. Output and Gram scores
were recomputed from saved trajectories, and the plotted scores independently
agree with those recomputations.

- [Algebra evidence](../../data/generated/neural_response_memory_20260922/scalar_direct_checks01/checks.json)
- [Main-suite reference cross-check](../../data/generated/neural_response_memory_20260922/scalar_direct_checks01/compact_reference_check.json)
- [Raw comparison table](../../data/generated/neural_response_memory_20260922/scalar_direct01/comparison.csv)
- [Full scores and controls](../../data/generated/neural_response_memory_20260922/scalar_direct01/scores.json)
- [Checked summary](../../data/generated/neural_response_memory_20260922/scalar_direct01/final_summary.json)
- [Flagship trajectories](../../data/generated/neural_response_memory_20260922/scalar_direct01/flagship_trajectories.pdf)
- [Passive errors by cutoff](../../data/generated/neural_response_memory_20260922/scalar_direct01/cutoff_passive_errors.pdf)
- [Gram errors](../../data/generated/neural_response_memory_20260922/scalar_direct01/gram_errors.pdf)
- [Runtime and storage](../../data/generated/neural_response_memory_20260922/scalar_direct01/resource_costs.pdf)

To reproduce the campaign, choose a fresh output directory:

    python -B studies/neural_response_memory_20260922/check_scalar_direct.py \
      --output data/generated/neural_response_memory_20260922/scalar_direct_checks02/checks.json
    python -B studies/neural_response_memory_20260922/run_scalar_direct.py \
      --out data/generated/neural_response_memory_20260922/scalar_direct02
    python -B studies/neural_response_memory_20260922/plot_scalar_direct.py \
      --out data/generated/neural_response_memory_20260922/scalar_direct02

The numerical engine needs NumPy/SciPy; plotting additionally needs Matplotlib.
Each cell records success/failure, source hashes and tolerances. The campaign
directory includes immutable source snapshots, configuration, trajectories,
worker logs, compilation tables and resource accounting.

## What this establishes

Direct passive outputs are an effective way to isolate scalar compression
from function reconstruction. Training Grams supply a stronger diagnostic:
they expose inconsistent population statistics even when labels fit.

The construction follows the exact population hierarchy and is distinct from
freezing a learned response subspace. Nevertheless, deleting high-grade
contractions at the affordable cutoffs tested here gives a poor approximation.
The existing fixed-width, finite-horizon large-K convergence argument makes
no assertion that these cutoffs are sufficient, so the results do not refute
that theorem or all possible scalar closures.

The empirical obstacle is now concrete: a useful replacement must control
the omitted correlations and preserve compatible evolving statistics.
Adding observable names alone, including Grams, does not achieve that.
This experiment does not establish accurate whole-circle prediction, a
width-uniform cutoff, or a practical higher-order scalar replacement.

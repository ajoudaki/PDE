# Preregistered \(S=128\) exact-reference update

## Outcome

The fixed operator-Galerkin PDE is now statistically distinguishable from
the finite \(n=256,L=32\) exact-network ensemble mean in the preregistered
primary observable: the full time/depth curve of the
initialization-cancelled hidden-Gram increment.

\[
D_G^{\mathrm{inc}}
=
\max_{0\le t\le8,\;0\le s\le1}
\left\|
[G_{\mathrm{PDE}}(s,t)-G_{\mathrm{PDE}}(s,0)]
-
[\bar G_{128}(s,t)-\bar G_{128}(s,0)]
\right\|_F
=
7.2433433\times10^{-3}.
\]

The discrepancy exceeds the curvewise 95% bootstrap threshold under both
preregistered resampling schemes:

| Bootstrap | \(B\) | 95% threshold | observed / threshold | centered-bootstrap tail probability |
|---|---:|---:|---:|---:|
| pooled individual trajectories | 2,000 | \(5.01674\times10^{-3}\) | 1.444 | 0.00350 |
| stratified within the \(32/32/64\) blocks | 2,000 | \(4.94006\times10^{-3}\) | 1.466 | 0.00200 |

Therefore the frozen decision is:

> **The Gram-increment discrepancy is statistically resolved at the
> curvewise 5% level.**

This is a small but detectable discrepancy: it is \(1.143\%\) of the PDE's
terminal feature motion \(0.633801\). It does not show that the PDE is
qualitatively wrong, and it does not identify whether the source is finite
network width/depth or finite PDE basis/depth/cubature resolution.

## Frozen design and data integrity

The protocol in `REFERENCE_NOISE_PREREGISTRATION.md` was written and the
analysis script was syntax- and smoke-tested before the held-out block
appeared. No PDE state, coefficient, basis, quadrature, time step, time
window, observable, or exact-network seed was changed after reading it.

The exact reference concatenates, with equal weight per network seed:

- \(S=32\), seeds 6000--6031;
- \(S=32\), seeds 8000--8031;
- held-out \(S=64\), seeds 10000--10063.

The held-out archive has SHA-256
`32b102d70013c137a5ae6d4a1076eb0f83fe85ae2ccece866324c6b34a248b99`.
Its ZIP container, metadata, \(0:.04:8\) time grid, array shapes, 64 unique
seeds, finiteness, stored means/SEMs, Gram symmetry, and Gram/tangent-kernel
positive semidefiniteness all pass independent recomputation.

The PDE remains the already completed
`pde_QMC_P5_N16_M256_R128_s20260723_dt0p02_T8.npz`; no exact-network
archive is read by its drift.

## Blockwise stability

| Exact reference | seeds | output sup | loss-of-mean sup | absolute-Gram sup | Gram-increment sup | tangent-kernel sup |
|---|---:|---:|---:|---:|---:|---:|
| seed 6000 block | 32 | 0.007974 | 0.000925 | 0.031387 | 0.008076 | 0.047359 |
| seed 8000 block | 32 | 0.026287 | 0.003322 | 0.028419 | 0.006165 | 0.061016 |
| held-out seed 10000 block | 64 | 0.010018 | 0.005109 | 0.019438 | 0.007855 | 0.031340 |
| existing 6000+8000 pool | 64 | 0.017075 | 0.001498 | 0.027867 | 0.006731 | 0.051129 |
| full pool | 128 | 0.010753 | 0.001846 | 0.019408 | 0.007243 | 0.033404 |

The Gram-increment gap is stable under deletion of any one acquisition
block:

| Pool | seeds | Gram-increment sup |
|---|---:|---:|
| omit seed 6000 block | 96 | 0.007042 |
| omit seed 8000 block | 96 | 0.007852 |
| omit held-out seed 10000 block | 64 | 0.006731 |

The three pairwise block-to-block Gram-increment gaps are \(0.003929\),
\(0.004558\), and \(0.005446\). As a post-preregistered directional
diagnostic, the three blocks' terminal \(s=1\) residual matrices have cosine
similarities \(0.980\), \(0.978\), and \(0.994\) with the pooled residual.
Thus the resolved pooled effect is not produced by cancellation of
inconsistent block directions or by one anomalous block.

## Where the discrepancy occurs

The primary maximum is at the preregistered endpoint \(t=8,s=1\), which is
an original node of both depth grids, not an interpolated midpoint. The
PDE, exact-reference, and difference matrices there are:

\[
\Delta G_{\mathrm{PDE}}=
\begin{pmatrix}
 0.372679&-0.265550& 0.169952\\
-0.265550& 0.177192&-0.117109\\
 0.169952&-0.117109& 0.072021
\end{pmatrix},
\]

\[
\Delta\bar G_{128}=
\begin{pmatrix}
 0.376048&-0.269210& 0.171678\\
-0.269210& 0.176204&-0.118674\\
 0.171678&-0.118674& 0.070444
\end{pmatrix},
\]

\[
\Delta G_{\mathrm{PDE}}-\Delta\bar G_{128}=
\begin{pmatrix}
-0.003369& 0.003661&-0.001726\\
 0.003661& 0.000989& 0.001565\\
-0.001726& 0.001565& 0.001577
\end{pmatrix}.
\]

The discrepancy grows smoothly toward terminal training time and output
depth: the largest terminal errors at depth fractions
\(1,0.969,0.938,0.906\) are respectively
\(0.007243,0.006909,0.006499,0.006223\).

## Secondary metrics

The secondary discrepancies remain below their own curvewise bootstrap
thresholds:

| Metric | observed | pooled 95% | stratified 95% | classification |
|---|---:|---:|---:|---|
| output | 0.010753 | 0.015347 | 0.015683 | not resolved |
| output after \(t=0\) | 0.009463 | 0.013884 | 0.014105 | not resolved |
| loss of mean predictor | 0.001846 | 0.010866 | 0.010933 | not resolved |
| absolute Gram | 0.019408 | 0.029204 | 0.028979 | not resolved |
| tangent kernel | 0.033404 | 0.059053 | 0.058858 | not resolved |

Each secondary maximum occurs at initialization. That is consistent with
finite-ensemble initialization noise and is why the
initialization-cancelled Gram increment was preregistered as primary.

An implementation-independent sensitivity recomputation drew bootstrap
indices directly, used a fresh random seed and 3,000 replicates, and found a
pooled 95% threshold \(0.004922\) and tail probability \(0.00300\). This
agrees with the frozen multinomial-count implementation.

## Scientific interpretation

The experiment now resolves three logically distinct statements:

1. **A genuine finite, width-independent, autonomous PDE was simulated.**
   The prior algebraic, restart, refinement, nonlazy-feature, and plateau
   checks still stand.
2. **Its primary curve is close to the finite-network reference.**
   The full discrepancy is about \(1.14\%\) of the observed feature motion.
3. **It is not equal to the finite \(n=256,L=32\) mean at current
   resolution.** The remaining Gram-motion bias is now larger than
   exact-reference Monte Carlo uncertainty.

The third statement is not yet a test of the conjectured ordered
width-then-depth limit. Existing controlled PDE changes include
\(7.44\times10^{-3}\) in Grams for \(P=5\to15\),
\(8.45\times10^{-4}\) for \(N=16\to32\), and
\(7.83\times10^{-4}\) to \(1.16\times10^{-3}\) for isolated \(M/R\)
refinements. The independent GH/QMC Gram difference is
\(1.94\times10^{-2}\). Meanwhile the exact
\(n=256,L=32\to64\) Gram-increment difference is itself unresolved.
Consequently the present data cannot apportion the detected \(0.00724\)
between finite-\(P\)/cubature error, finite width/depth, or a structural
closure bias.

The correct next discriminating experiment is a cofinal nested-\(P\)
operator-PDE refinement with controlled quadrature, followed by quieter
width-then-depth exact references. Merely adding more seeds to the same
finite PDE/reference pair will estimate the already detected discrepancy
more precisely but will not identify its source.


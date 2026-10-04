# Fewer neurons: a proved initial construction and the unresolved training comparison

2026-10-03. Current result after the user's clarification. The original
memory-order theorem is unchanged. It does not answer the requested
neuron-reduction question by itself.

**Status:** an actual weighted neuron-selection construction is proved to
match the initialized learning response using polylogarithmically many
neurons in both hidden layers. The required all-time prediction comparison
with the original closure is still unproved. No impossibility theorem for
that goal has been obtained.

## Intended result

For the original realized width-n, order-q tanh closure, seek an autonomous
weighted model with N neurons per hidden population, preserving its own
coupled moments, residual RMS clock, and both directions of one fixed
compressed mixer. The comparison must control
\[
 \left(\int\sup_{t\ge0}
   |\widetilde f_{N,q}(t,x)-\widehat f_{n,q}(t,x)|^2d\mu(x)\right)^{1/2}
\]
against the actual finite reference, including systematic sampling bias and
its fitted unseen-input function. The intended root-width error is
C_delta/sqrt(n), with moving state O(Nq), preferably a fixed power below n.
Fixed coefficients, initialization work, retained neurons and evolving
moments must all be distinguished. A precomputed trained path is forbidden.

The earlier q=n^(1/6+o(1)) result reduces history order while retaining n
neurons. Combining it with a hypothetical N^(-alpha) full-dynamics sampling
rate would yield Nq=n^(1/(2alpha)+1/6+o(1)). A strict power below n requires
alpha>3/5. In particular an N^(-1) sampling theorem would give the user's
suggested scale Nq=n^(2/3+o(1)). These are requirements, not new proved
trained-network rates.

## Positive finite-network neuron-selection theorem at initialization

Fix d,m and confidence 1-delta. Inputs are on the radius-sqrt(d) sphere.
Use the actual canonical Gaussian first matrix A0 and mixer W0, zero
readout, and tanh. Write v=x/sqrt(d), and define each initialized upper
feature and its empirical training/query kernel by
\[
 b_j(v)=\tanh([W_0\tanh(A_0v)]_j),\qquad
 K_n(v,v_a)=\frac1n\sum_{j=1}^n b_j(v)b_j(v_a).
\]
Every closure order has initial prediction velocity
\[
 \partial_t\widehat f_{n,q}(0,x)
   =\frac2m\sum_a y_a K_n(v,v_a).
\]
Thus the nontrivial initialization observable is the initial learning
update, not the identically zero initial prediction.

With probability at least 1-delta at all sufficiently large n, there is
an explicit finite construction selecting original lower indices I and
upper indices J, assigning positive probability weights D1,D2, and forming
a fixed mixer B0 from W0, such that:

* Both support sizes are O_{d,m,delta}((log n)^(3d)).
* The reduced initial training kernel is exactly K_n on every training pair.
* Its initial training/query kernel differs from K_n by at most C/sqrt(n),
  uniformly on the entire normalized box [-1,1]^d and hence on the sphere.
* B0 has weighted operator norm at most ||W0||op and is always paired with
  its exact weighted adjoint D1^(-1) B0^T D2.
* After setup, evaluation and the defined reduced dynamics use only retained
  neurons. No original trained path or population limit is evaluated.

Consequently the reduced initial prediction velocity is exact at training
inputs and differs by at most C Y/sqrt(n) uniformly on sphere queries, where
Y is the label RMS. The snapshot theorem itself needs no small-label bound.
It is uniform in q because this initial velocity is identical at every order.
The number of samples improves on Monte Carlo for this observable of the
actual finite model; its fluctuation or bias relative to a population is
neither used nor discarded.

The mechanism is positive empirical cubature of response functions. A
Gaussian estimate supplies a common complex analytic strip for all initial
neuron functions. Their query dependence can therefore be approximated in a
common polynomial space of polylogarithmic dimension. Positive weighted
selection exactly matches the relevant coefficient averages. Both the
initial feature Gram and the projected mixer geometry are retained, rather
than only matching separate scalar weight histograms.

More precisely, choose an RMS-orthonormal lower basis V spanning the
first-feature polynomial coefficient columns and the exact training
features, and put U=W0 V. Lower and upper cubature preserve
\[
 V_I^\top D_1V_I=I,\qquad U_J^\top D_2U_J=U^\top U/n.
\]
The fixed reduced mixer is
\[
 B_0=U_JV_I^\top D_1,\qquad B_0^*=V_IU_J^\top D_2.
\]
This is a projection of the original mixer computed during setup, not a
new independent Gaussian mixer or the raw selected submatrix. Its omitted
actions outside the retained space are approximation errors that must be
controlled during training. Setup may be costly and numerically delicate;
only its finite mathematical construction and retained-state size are proved.

Use these two weighted populations in the original q-order moment equations,
with their own residual, clock and weighted contractions. This gives an
autonomous candidate with moving count
mq(|I|+|J|)+d|I|+|J|+1. The count is small, but its trained approximation
accuracy has not been certified. In particular substituting q=n^(1/6+o(1))
does not turn the snapshot theorem into a global compression theorem.

## Why the population-sampling intuition needs additional mathematics

Having finitely many populations does not mean their ordinary joint
marginal distribution determines their evolution. The fixed Gaussian
operator connects them in both directions. Even after conditioning on
all initial training features and their first backward response, the
actual next forward acceleration has a new Gaussian component of
nonvanishing size at fixed nonzero labels. This is an exact conditional
Gaussian calculation for the initialized closure. It proves that this
particular finite source list is incomplete, not that efficient
approximate source sampling is impossible.

There is also a useful difference between value accuracy and derivative
accuracy. In a block cubature, a discarded forward field e is orthogonal
to the retained upper population. Its first-order contribution to the
scalar output cancels, giving output error at most C Y ||e||_2^2/n.
The corresponding retained backward variation contains H^T D e, where
H is the discarded mixer action and D a blockwise gate/readout factor.
This need not vanish and is generally only first order in ||e||_2.
Thus excellent feature-value coverage is not automatically excellent
coverage of the responses that move those features.

The separate block construction supplies exact weighted equations and a
derived all-time source comparison. Its uncontrolled terms are the actual
forward and reverse actions omitted by the chosen subspaces, integrated
against residual activity, plus the initial state projection error. No
small bound on these terms is assumed as a replacement for the requested
theorem. Conditional Gaussian calculations explain why selecting only on
initial forward marks does not control them.

Finally, randomized stratification of the unchanged original neuron paths
is unbiased relative to that finite model. A proved path-variation bound
controls its full time supremum, and gives ordinary C_mu Y/sqrt(N)
sampling error for balanced cells. A stronger rate depends on the within-
cell variation of the actual response trajectories. Giving sampled
neurons their exact reference trajectories would require the full model;
the autonomous smaller model has an additional feedback error, kept
explicit in the decomposition. This term is currently unresolved.

## Evidence and current limit

* [JOINT_SOURCE_SAMPLING.md](JOINT_SOURCE_SAMPLING.md), Sections 3--4:
  complete top-only and joint-population cubature proofs; also exact source
  conditioning and a finite weighted candidate.
* [NEURON_CUBATURE_CONSTRUCTION.md](NEURON_CUBATURE_CONSTRUCTION.md):
  block candidate, weighted adjoint, fitting scope, all-time source
  certificate, quadratic observable cancellation and reverse-response gap.
* [EMPIRICAL_PATH_QUADRATURE.md](EMPIRICAL_PATH_QUADRATURE.md) and
  [its check](EMPIRICAL_PATH_QUADRATURE_CHECK.md): exact empirical full-time
  quadrature, actual-reference MC bound, and the missing feedback term.
* [NEURON_REDUCTION_CHECK.md](NEURON_REDUCTION_CHECK.md): complete
  collaborative internal reconstruction and source hashes.

The initialized joint-neuron construction is internally checked. The
requested all-time, all-query neuron reduction at matched root-width error
remains open. No full trained-error exponent, lower-bound impossibility,
arbitrary-depth extension, or numerical experiment is claimed. The paper
and the earlier memory-order theorem have not been modified.

# Frozen research contract: doubly RMS-normalized quadratic network

## Exact finite-width model

Fix `epsilon > 0`, a deterministic target `y_*` (the canonical case is
`y_* = 1`), and a learning-rate constant `eta > 0`.  Write

\[
\langle v,w\rangle_n=n^{-1}v^\top w,
\qquad
(p\otimes q)r=p\langle q,r\rangle_n .
\]

The parameters are `A,u in R^n` and `G=W/sqrt(n) in R^{n x n}`.  Initially,
the entries of `A`, `u`, and `W` are independent standard Gaussians.  Define

\[
X=u^{\odot2},\quad
\alpha=(\langle X,X\rangle_n+\epsilon)^{1/2},\quad H=X/\alpha,
\]
\[
Z=GH,\quad V=Z^{\odot2},\quad
\beta=(\langle V,V\rangle_n+\epsilon)^{1/2},\quad Y=V/\beta,
\]
\[
f_n=\langle A,Y\rangle_n,\qquad e_n=y_*-f_n,qquad
\mathcal L_n=e_n^2.
\]

The parameter metric in the `(A,u,G)` variables is the Euclidean-muP metric

\[
n^{-1}\|\delta A\|_2^2+n^{-1}\|\delta u\|_2^2+
\operatorname{Tr}(\delta G\delta G^\top).
\]

Equivalently, it is `n^{-1}` times the ordinary Euclidean metric on the raw
parameters `(A,u,W)`, with `G=W/sqrt(n)`.  Consequently a matrix feature
gradient is a normalized outer product: if
`(p tensor q)r=p<q,r>_n`, its entries are `p_i q_j/n`.

If a prime denotes feature ascent, namely the metric gradient of `f_n`, then
physical full-MSE flow is

\[
\dot\theta=2\eta e_n\theta',\qquad
\dot e_n=-2\eta e_nK_n,
\quad K_n=\|\nabla_{\!\mu P}f_n\|^2.
\]

Every layer is trained and both normalization denominators are differentiated.
Changing the loss convention or freezing a layer is outside this contract.

## Admissible closure class

An admissible closure must specify, before seeing a trajectory:

1. a fixed, width-independent source probability space and source law;
2. a state in a finite product of explicitly named scalar, finite-dimensional
   mark-field, probability-measure, kernel, or operator spaces on fixed domains;
3. an autonomous current-state vector field and restart map;
4. continuous current-state readouts for `f`, `K`, `e`, and `L=e^2` in the
   topology used for well-posedness and convergence.

The number and types of state components cannot grow with width, derivative
order, graph depth, requested accuracy, or time horizon.  The following are
inadmissible:

- DMFT or any two-time kernel;
- stored trajectory/history or a delay state;
- a source, forcing, or coefficient obtained from the unknown trajectory;
- width-indexed atoms, coordinates, or matrices retained in the limit;
- an ultraproduct, oracle, nonconstructive encoding of the answer, or a
  pretabulated loss/kernel curve;
- a field or measure whose coordinate algebra is explicitly indexed by all
  moments, rooted graphs, traffic words, iterated derivatives, or finite-width
  configurations.  Calling that hierarchy one measure/operator is disguised
  hierarchy storage.

A probability law on a fixed finite-dimensional mark space, or a finite list
of operators on a fixed explicitly described function space, is not rejected
merely for being infinite-dimensional.  It must nevertheless have an
independently stated topology, a closed current-state evolution, and continuous
readouts.  Any impossibility claim must name a mathematically precise subclass
of this contract and prove that the subclass exhausts the contract; a
topology-specific obstruction is not a universal theorem.

## Required positive theorem

A positive terminal result must give the source, state spaces and topologies,
initial state, autonomous equations, and readouts explicitly, and prove:

- exact restartability from every state in the claimed phase space;
- existence and uniqueness on every finite physical-time interval;
- finiteness and continuity of `f`, `K`, `e`, and `L`;
- for every deterministic `T < infinity`,

\[
\sup_{0\le t\le T}
\bigl(|f_n(t)-f(t)|+|\mathcal L_n(t)-\mathcal L(t)|\bigr)
\longrightarrow0
\quad\text{in probability}.
\]

The proof must include tightness, uniform integrability of every unbounded
readout, identification of every subsequential limit, and uniqueness.

## Required hostile audit

Every candidate must explicitly settle:

- coordinate spikes compatible with bounded empirical RMS;
- `alpha,beta >= sqrt(epsilon)` but possibly poor radial conditioning;
- the unbounded activation derivative `2z`;
- adaptive matrix--activation alignment;
- continuity/uniform integrability of output and tangent-kernel readouts;
- whether the projections suppress only radial growth or all relevant growth;
- whether the state is a relabelled full hierarchy;
- whether hidden-layer motion and hidden-layer NTK contributions stay
  nonzero, rather than becoming lazy, linear, frozen-feature, or readout-only.

## Claim ladder and gates

The levels are: exact finite-width identities; finite-width a priori bounds;
fixed-time tightness; subsequential limiting equations; uniqueness and
continuous readouts; compact-time convergence; terminal positive theorem.
No level inherits the next one without proof.  A terminal negative theorem
must instead rule out the entire frozen admissible class, not just one ansatz.

Independent construction and hostile-audit routes are kept separate until
their written claims can be compared.  Failed routes contribute only the
lemmas they actually establish.

## Terminal rule

This study is complete only after either the required positive theorem or a
canonical impossibility theorem for the entire frozen admissible class has
survived an independent audit.  Otherwise every report is headed
`NONTERMINAL CHECKPOINT`, preserves valid lemmas and counterexamples, states
the exact remaining obligation, and lists genuinely new next routes.

## Contract amendment log

- Before any finite-width claim was promoted, the initially written matrix
  metric `n^{-1} Tr(dG dG^T)` was corrected to `Tr(dG dG^T)`.  The former
  would be off by a factor of `n` relative to the canonical raw-`W`
  Euclidean-muP convention.  The present text is the frozen contract.

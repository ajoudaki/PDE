# Functional limits and the model-reduction connection

**Assessment update.** The NHL analysis is superseded by [AUDIT_NHL.md](AUDIT_NHL.md), including its proof gaps and reconstructed surviving results. The complete Chorin conceptual-source read below remains current.

## Chen: Neural Hilbert Ladders, JMLR 2024

[Published paper](https://www.jmlr.org/papers/volume25/23-1225/23-1225.pdf), 65 pages, read completely including Appendices A–E and references. Rendered pp. 13, 14, and 59 were checked against extracted equations. No code or experiments were reproduced.

This is a particularly useful comparator: it joins multilayer function-space representation, a static finite-network approximation theorem, generalization theory, and a limiting training dynamics. It is not merely an unevaluated formal operator.

**Static approximation.** Theorem 9, p. 9, supplies a squared-\(L^2\) finite-network approximation rate inversely proportional to width, with depth, Lipschitz, input-moment and function-complexity factors. The proof samples from a functional representation and propagates the layerwise error. It neither constructs a small autonomous model shadowing one finite initialized network nor allows one to choose separate approximants at each time and call the result a closed dynamics.

**Training limit.** Theorem 18, p. 13, proves finite-time convergence of finite-width predictions and feature laws to function-valued limiting dynamics. Its quantifier fixes each finite time; no uniform complete-trajectory, below-seed discrepancy rate is displayed. Assumptions include appropriate bounded/Lipschitz derivatives, initial moment bounds and input moments. The hidden-layer scaling is the mean-field average \(1/\text{width}\) with order-one weights, not the current manuscript's Gaussian \(1/\sqrt{\text{width}}\)-type hidden interactions.

Equations (12)–(13) carry two-time forward/backward kernels. Remark 21 explicitly discusses non-Markovian memory after eliminating weights. Appendix D reconstructs the dynamics using flow maps on function spaces. It is therefore wrong to say the theory is “not a dynamical system”: it is an infinite-dimensional dynamics whose reduced response representation has memory.

Remark 19 describes a degeneracy of sufficiently deep bias-free, i.i.d.-initialized networks in this particular scaling. The author discusses biases/correlated initialization as remedies. This is a distinction of regimes, not a universal impossibility for deep mean-field theory.

Experiments include deep linear networks and biased ReLU nonlinear networks. Smooth dynamical hypotheses and ReLU experiments must not be merged into one theorem. Section 9 explicitly leaves general long-time deep behavior open.

**Local printed inconsistencies.** Equation (14), p. 14, has a positive loss-gradient sign, inconsistent with the negative-gradient dynamics in the setup and Appendix D; the shallow equations show the same issue. The initialization of the zeroth kernel as 1 on p. 13 conflicts with the input inner product used on p. 14. These were visually checked. They are local formula inconsistencies, not grounds to dismiss the function-space construction. The comparison above does not rely on them.

## Chorin–Hald–Kupferman: optimal prediction and Mori–Zwanzig, 2000

[Author-hosted original](https://math.huji.ac.il/~razk/Publications/PDF/CHK00.pdf), PNAS 97:2968–2973, six pages, read completely including derivation, nonlinear Schrödinger example and references.

Equation (2.7) decomposes projected dynamics into a present-state contribution, a memory integral, and an unresolved-initial-state term. It is an identity before approximation. First-order optimal prediction drops memory/noise; the nonlinear Schrödinger example demonstrates why memory can be essential for relaxation. The example then approximates and truncates memory, with those limitations explicitly acknowledged.

**Useful connection:** eliminating variables can exchange state dimension for memory. A finite auxiliary-state representation of that memory is a route back to a small Markovian system. Legendre response moments fit this conceptual pattern.

**Qualification:** the paper's conditional-expectation framework uses an invariant statistical measure and averages over unresolved states. The manuscript instead uses its own exact response identities and a coupling to a particular dense initialization. Do not say its proof directly invokes the Mori–Zwanzig theorem or automatically inherits that theory's guarantees. The connection is structural, not an identification of the constructions.

## Nichani–Damian–Lee: deep nonlinear feature learning

[NeurIPS 2023 proceedings](https://proceedings.neurips.cc/paper_files/paper/2023/file/236b6a814a1d2c0ff504ca7bf380f7ff-Paper-Conference.pdf), *Provable Guarantees for Nonlinear Feature Learning in Three-Layer Neural Networks*.

The coordinator read the main text; a scoped reader subsequently completed the **48-page** proceedings PDF, including all appendices. See [NICHANI_CONTEXT.md](NICHANI_CONTEXT.md) for full coverage, theorem assumptions, proof structure and empirical distinctions. The earlier estimate of 34 pages was incorrect. Complete reading is not a claim to have independently reconstructed every lower-bound calculation.

Algorithm 1 freezes the first layer and biases, takes one gradient step on the middle matrix using one sample split, then trains the readout with weight decay using the second split. The theorem learns nonlinear quadratic features and obtains sample-complexity/depth separations. This is genuine deep nonlinear feature-learning theory; it must not be described as failing to study feature learning. Its object is learning/generalization under that structured training schedule, not autonomous compression of an ordinarily jointly trained supplied dense network.

This source supports a narrowly worded comparison. It does not support a blanket claim that all existing deep feature-learning results use this schedule.

Its appendix also contains a separate experiment training all layers jointly with maximal-update scaling and momentum SGD. The theorem's layerwise qualification must not be attributed to all of its experiments.

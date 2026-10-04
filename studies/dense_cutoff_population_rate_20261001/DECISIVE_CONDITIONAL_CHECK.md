# Internal reconstruction: width doubling and the local mean-response criterion

Coordinator reconstruction, 2026-10-01. This checks the complete frozen `DECISIVE_CONDITIONAL_ROUTE.md`, SHA-256

```text
f807cf687ee278ee64a28f18f9ed5a6aff490414c971e09862ca8ace1139c1ec
```

This is an internal mathematical check, not an independent promotion review. The checker authored the separate controlled-feedback and passive-query extensions; the checked route was authored by the scoped collaborator. No experiment, external source, or other study was used. The current manuscript and notation contract were read completely earlier in the task and their hashes remain those recorded in the route.

## Reconstructed statements

The auxiliary variance/mobility interpolation has exactly the claimed canonical endpoints. For width \(N=2n\), a diagonal block at \(s=0\) has initialized variance \(2/N=1/n\), hidden update coefficient \(2/N=1/n\), and the unchanged canonical first-layer and readout updates. The zero cross-block initialized entries have zero mobility and remain zero. The full output is one half the sum of the two block outputs. Their independence uses a deterministic common driver; it would fail for separate autonomous block residuals driven by the average output. The proof correctly does not make that substitution. At \(s=1/2\) all entries and mobilities are canonical width \(2n\).

For one entry initialized as \(\sqrt{c/N}\,G\), differentiating its Gaussian expectation gives \((2N)^{-1}\mathbb E\partial_W^2 q\). Differentiating the controlled ODE at fixed initialized entries additionally gives \(\mathbb E\partial_c q\). The two terms add. There are \(N^2/2\) within-block edges and the same number of cross-block edges, with profile derivatives \(-2\) and \(+2\). With the defined normalized response \(N^2\mathbb E[\partial_cq+(2N)^{-1}\partial_W^2q]\), these factors give precisely one cross-minus-within contrast at each hidden layer. No factor of width, two, or learning rate is missing.

Integrating the exact derivative against the proposed \(Ck(x)/\sqrt N\) bound gives a \(CSk(x)/\sqrt n\) dyadic difference of the finite means. The sum of the dyadic bounds is finite, with geometric ratio \(2^{-1/2}\). Bounded activations and finite control variation give uniformly bounded predictions. Therefore qualitative convergence identifies the dyadic limit of expectations; no quantitative bias estimate has been assumed in that identification. A uniform activity limit of continuous means is continuous, so pointwise identification at rational activity times suffices for the full interval. The \(L^2(\mu)\) envelope supplies the stated integrated norm. Every starting integer width can be used, so the conclusion is not restricted to powers of two.

For the initialized two-layer calculation, differentiating the single readout-feature average twice in one edge gives \(N^{-1}H_j^\top D^2F H_j\). Multiplication by \(N^2/(2N)\) produces the stated factor \(1/2\). The mobility derivative vanishes at zero readout. Exchanging the iid tagged within/cross feature vectors changes the row covariance by
\[
\frac{2(1-2s)}N(H_kH_k^\top-H_jH_j^\top).
\]
Bounded first-layer activations make this \(O(1/N)\). Gaussian covariance differentiation applied to \(D^2F\) is bounded by the fourth derivatives of \(F\), including singular covariance endpoints by continuity. It gives the stronger \(O(1/N)\) normalized contrast. The sum over training queries uses the \(\ell^1\)-bounded instantaneous driver and introduces no width factor.

## Adversarial scope checks

- A deterministic bias \(n^{-1/4}\) is not invisible to this argument: its dyadic difference is of that same order. The exact canonical block endpoint is what precludes adding an arbitrary width-dependent constant undetected by Gaussian derivatives.
- Matching initialization variance alone would give the wrong hidden learning rate at the block endpoint. Matching mobility alone would give the wrong initialized law. Both are present.
- The response hypothesis requires integrable derivatives of a trained observable. Finite-dimensional smoothness alone does not prove this. The route states the requirement explicitly.
- Exchangeability gives two edge classes; it does not make their expected responses equal or establish their root-width difference. This remains the substantive unproved part of H.
- The initialization argument ceases to be a simple iid swap after the first-layer features depend on the reused hidden matrix. The route explicitly does not propagate it through training.
- The general formulation strengthens activation regularity; its initialization verification uses four bounded derivatives. The later assembled two-tanh theorem satisfies both requirements.
- This route alone gives a conditional bias estimate for a prescribed control. Its statements about missing passive-query fluctuations and autonomous-feedback transfer are historically scoped to this note. The subsequent complete arguments and assembled implication are in `PASSIVE_QUERY_FLUCTUATIONS.md`, `CONTROLLED_FEEDBACK_STABILITY.md`, and `ROOT_WIDTH_CONDITIONAL_THEOREM.md`; they do not prove H.

## Outcome

The exact interpolation identity, its conditional strict root-width mean theorem, and its stronger initialization contrast were reconstructed without an unresolved mathematical objection. H is still open. This check establishes neither H nor the unconditional dense population rate. Validation was algebraic and analytic, including normalization, endpoint consistency, Gaussian differentiation, summability, and limit identification; no numerical evidence is claimed.

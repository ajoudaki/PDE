# Fourth primary-source applicability check: stochastic Taylor universality

Status: no direct application. This is a check of one additional theorem class, not a claim about the whole literature.

Primary source: Amir Dembo and Reza Gheissari, [Diffusions interacting through a random matrix: universality via stochastic Taylor expansion](https://link.springer.com/article/10.1007/s00440-021-01027-7), PTRF 180 (2021), 1057--1097. Inspected equations (1.1)--(1.12), Theorems 1--2, Corollary 3, and Proposition 4.3.

The model has fixed random affine drift (J+Lambda)^T X+h and diagonal affine diffusion. J=A/sqrt(N); centered entries are independent, optionally up to symmetry, with a bounded variance profile and uniform exponential tails. Initial coordinates are independent of J, product-distributed, with uniform moments. Deterministic coefficients obey the stated row/sparsity bounds. Theorem 1 compares fixed-degree polynomial observables under moment-matched disorders. Theorem 2 adds concentration assumptions and constant diffusion for trajectory concentration; zero diffusion is permitted. Proposition 4.3 obtains averaged-observable concentration from a localized full-state Lipschitz bound using operator norms. These results do not provide the deleted-column Jacobian trace/direction bounds needed here.

## Mapping to the canonical network

The disorder structure itself is compatible with a natural embedding:

    B = [ 0      W2_0*    0
          W2_0   0       W3_0*
          0      W3_0    0 ].

At N=3n, sqrt(N)B has independent centered Gaussian upper-triangle entries, allowing deterministic zero entries. Its nonzero variances are three. Thus neither transpose reuse nor the two-matrix variance pattern is the decisive obstruction for this class.

Choosing zero diffusion causes no conflict. Raw first-layer Gaussian roots and zero trained increments/readout satisfy the separate initial-law independence, moment, and concentration requirements; this does not construct an affine evolution in the same dimension. Indeed, the block embedding has dimension 3n, whereas retaining every trained matrix entry adds order n^2 state coordinates. Padding the block disorder to that dimension would change its N^(-1/2) scaling and violate a uniformly bounded rescaled variance profile. Derived initial hidden activations depend on B and cannot be silently substituted for independent initial coordinates. The transformed cubic-Gaussian root also needs a separate concentration check; using the raw root avoids that unnecessary issue.

The actual raw dynamics fails the affine-drift requirement: trained matrix increments multiply evolving activations and backward fields, and the middle derivative includes

    phi'(z2) W3* [W4 phi'(z3)].

These state-dependent coefficients cannot be placed into a prescribed deterministic Lambda or h. Eliminating learned matrices leaves history-dependent nonlinear contractions. No valid affine-state encoding has been established.

Augmenting the state by response variables does not repair this map: their equations contain the adapted factor phi''(z2)q2. The bound required in our deleted-query note concerns Tr(J_i)/n and J_i^T g/n, whereas a norm estimate treating that multiplier by max|q2| loses precisely the directional cancellation under investigation. Fixed-degree moment statements also give no p log p growth bound as the degree p increases.

Finally, universality compares disorders. Even a successful extension of that comparison would still need a Gaussian-limit existence/identification proof in this architecture, which is the current problem. The source offers a possible proof-method inspiration, but invoking its established theorems supplies neither global continuation nor the needed directional-response estimate.

# Three-input proof review record

Date: 2026-09-05.

Reviewed artifact: /tmp/THREE_INPUT_LOCAL_LIMIT_PROOF.md.

Claim: a local autonomous joint width/GD-step limit for three fixed normalized pairwise nonparallel inputs, arbitrary labels in {-1,1}, and any positive eta_n tending to zero. Singular input Gram matrices are explicitly included. The existence interval can be chosen uniformly over normalized triples, but no uniform convergence rate over width-dependent geometries is claimed. Strict feature-learning coefficients can depend on the fixed geometry.

Three independent adversarial reviewers were supplied the complete three-input proof and its cited primary reference. They were not supplied the exploratory derivations or one another's conclusions. All three returned PASS:

- Reviewer A checked singular geometry, the common population operator construction, uniform time bootstrap, actual-GD transfer, and the new per-input Gaussian-innovation argument.
- Reviewer B checked the Vandermonde feature-independence argument, the 3k-term Gaussian bound, probe conditions, ordered limits, and per-input activity.
- Reviewer C checked the conditional Gaussian variance and response coefficients in M18a–M18c, positive kernel blocks with singular G, all leading time coefficients, and uniform existence time.

All explicitly verified that the proof does not rely on a two-input exchange symmetry or on invertibility of the input Gram matrix. All found the factors in the three-input updates and activity expansions consistent.

No material fixes were requested. A final scope sentence clarifies that a common existence interval does not assert a convergence rate uniform over geometries changing with width.

These mathematical reviews are not formal proof-assistant verification. They apply to the local theorem; a global-in-time theorem for arbitrary input geometry is not established.

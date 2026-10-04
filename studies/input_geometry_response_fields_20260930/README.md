# Input geometry and response fields

This study asks what distribution-dependent structure can replace one response-memory state per training sample, including training on a continuum. It is a new functional/distribution direction, not an extension of a matrix-rank assumption.

## Contract

Preserve canonical deep nonlinear squared-loss gradient flow, trained hidden features, the actual initialized matrices and their transpose actions. Compare predictors uniformly on a specified finite physical-time interval and compact test-input set. Seek an autonomous approximation whose evolving state is independent of the number of data atoms. Width, intrinsic input dimension, accuracy, depth and horizon remain explicit. A width-uniform or all-time estimate is not assumed.

Inputs are the maintained book's `docs/index.qmd` and `docs/notation.qmd`, the canonical equations supplied in the task, and external primary mathematical sources checked for this study. Root also consulted the current `paper/main.tex` learning-speed theorem/proof (the manuscript's own Appendix A, lines 1023–1265) to check the canonical moment convention and depth cancellation; RESULT.md supplies its complete positive-weight extension and all needed arguments. No result from another study is a dependency. The independent routes received prompt-only scientific inputs.

## Work and ownership

- Root: full derivation, source checking, synthesis and this README.
- `input_field_route`: prompt-only independent field equations, `FIELD_ROUTE.md`.
- `distribution_cubature_route`: prompt-only independent moment-matching argument, `CUBATURE_ROUTE.md`.
- `population_structure_route`: prompt-only independent structure/obstruction analysis, `STRUCTURE_ROUTE.md`; after freezing that route, internal checking of the complete root candidate, `CHECK.md`.

The investigation is theoretical. No training campaign, paper change, promotion or Git commit is part of the current task. Existing unrelated changes are preserved.

## Results

[RESULT.md](RESULT.md) gives the self-contained principal result. For fixed width n, depth L, horizon T and analytic input chart of dimension s, tanh canonical GF on any probability data law with label RMS≤Y is approximated throughout [0,T] and uniformly over the input domain with error

`C_(T,n) [q^(-1) + exp(-c_(T,n) p)]`.

An explicit autonomous weighted response-memory closure uses at most `K≤2(p+1)^s+1` retained input-label pairs and `2(L−1)nqK+nd+n+1` moving scalars, independent of the original data count. This includes an empirical dataset of arbitrary size and an abstract continuum law. For finite data the positive summary is constructible by linear dependence elimination; an effective continuum implementation additionally needs access to a computable positive cubature. Constants are uniform in q, K, original sample count, minimum weights and maximum individual labels under the RMS bound, but **not asserted uniform in n or T**. Width, horizon, intrinsic dimension and conditioning can make the bounds costly.

The exact identity `B(t,x,y)=A(t,x)−yC(t,x)` separates irregular labels from regular response fields. Squared-loss training sees the data through its input marginal, first-label signed measure and (for the residual clock) second label moment. No low-rank hypothesis, frozen-feature training, loss fitting assumption, small-label assumption, future trajectory or dense teacher is used.

There is also exact data-moment compression for polynomial activations at fixed depth. One summary works for every width and every initialization; dense trajectories agree for all time, and finite-q closure trajectories agree on their common existence interval. Its degree grows exponentially in depth and it is not a replacement theorem for tanh.

## Proofs and checks

- [RESULT.md](RESULT.md): full model, positive moment construction, analytic neural drift approximation, probability-weight-uniform temporal-memory proof, combined trajectory theorem, state/runtime and exact polynomial example.
- [CUBATURE_ROUTE.md](CUBATURE_ROUTE.md): independent proof of analytic data compression, including a sharper total-degree node count and unbounded-label continuum convexity argument.
- [FIELD_ROUTE.md](FIELD_ROUTE.md): exact label separation and a direct finite coefficient ODE for H,A,C, with fixed-q spatial convergence and explicitly finite static data moments. Its q-dependent spatial constants must not be confused with the uniform-q combined bound in RESULT.md.
- [STRUCTURE_ROUTE.md](STRUCTURE_ROUTE.md): independent input-covering theorem, polynomial example, finite-moment exactness obstruction and a scoped all-time perturbation counterexample.
- [POLYNOMIAL_EXACT.md](POLYNOMIAL_EXACT.md): complete simultaneous-width/time exact data-reduction theorem for polynomial networks and coefficient-level verification for every finite temporal order.
- [CHECK.md](CHECK.md): completed internal mathematical check of the principal result; records hashes, every objection, corrections and scope. This is not promotion review. Root read all route arguments and checked their compatibility; no training or empirical validation is claimed.

Principal-result check status: **internally checked**, RESULT.md SHA256 `44c94275d490c119d0c85c155cd16b9924f260cc1f2c79c238f03b9d7abfb3d0`. The separate checker validated the full final candidate and the root verified its corrections; FIELD_ROUTE.md received root mathematical checking but is explicitly outside that separate check. Promotion status: not submitted or approved.

Primary source checks: Bayer–Teichmann's complete six-page cubature paper and Trefethen's complete Chapter 8 source were read via their authors' sites; the complete eleven-page CRAIG main paper was retrieved and read for positioning (its supplement is not a theorem dependency). Links and needed proof ingredients are in RESULT.md. A shell attempt to download source copies encountered restricted DNS; web retrieval supplied the full texts instead. No generated experimental evidence is being claimed.

## Remaining limits and next work

The sample-count-independent finite-time theorem is the concrete advance. Width-uniform input regularity and all-time stability remain separate obligations. Unknown data distributions incur statistical estimation error. Coreset arithmetic counts do not establish numerical conditioning or bit complexity. No priority claim or empirical efficiency claim has been established.

No paper/book edits, training runs or commits were performed. The independent coefficient ODE and positive cubature are alternative implementations; a subsequent empirical comparison requires a separate scoped experiment. The completed report answers the present theoretical investigation rather than authorizing a new campaign.

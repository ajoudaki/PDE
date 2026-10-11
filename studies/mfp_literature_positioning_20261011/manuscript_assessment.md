# MFP manuscript: actual theorem and implemented contract

Review target: `paper_MFP/main.tex` and its bundled `paper_MFP/code/`, as inspected on 2026-10-11. This assessment concerns the committed mathematical presentation and executable calculus. It does not import the separate proposed cavity proof or another study's findings. No manuscript edits are proposed implicitly by this audit.

## What the theorem says

The central result is a compilation theorem for a **specified finite language**, followed by a Gaussian-program limit theorem. Fix the program, input count, depth, derivative order, and number of discrete updates before sending the common population width n to infinity. Initial vector tuples are iid across neurons, Gaussian within each tuple, with fixed means and positive-semidefinite covariances; different populations and named matrices are independent. Covariances may be singular. Initial scalars are fixed deterministic constants. A scalar shared randomly across all neurons is not an allowed independent Gaussian root.

Each named matrix has independent N(0,1/n) entries and maps between distinct population types. Calls to its transpose use the actual same matrix. Coordinate maps are finite sums, products and compositions of a fixed smooth activation and its derivatives. Every activation derivative has polynomial growth. Normalized averages can feed later computations. The declared language also contains represented matrices consisting of an initialized matrix plus finitely many normalized outer products, with explicit lowering rules.

Physical differentiation takes place at finite width. Product, chain, adjoint, directional, update and finite-jet rules produce a new finite primitive program. Derivatives of scalar feedback and moving directions are included. Matrix directions and contractions must have the declared represented form; the theorem does not accept an arbitrary tensor formula merely because it is a neural-network derivative. Scaled vector gradients, represented matrix gradients, admitted gradient steps and finite flow jets are covered through these rules.

The compiled scalar observable O_n then satisfies, for every fixed finite p>=1,

    O_n -> Eval(GaussianDAG(O_n)) in L^p.

The right side is deterministic for fixed inputs/labels. Vector nodes have width-uniform moments of every fixed order; fixed same-population empirical tuples converge in quadratic Wasserstein distance in probability. The source representation preserves matrix identity, transpose history and all dependencies. It is not an assertion that every vector representative is Gaussian: nonlinear functions and response terms generally are not.

For forward queries W h_r and reverse queries W^T u_s, with representatives H_r,U_s, the Gaussian source covariances are E[H_r H_t] and E[U_s U_v], respectively. They use **uncentered second moments**. The two orientation source groups are independent, while the resulting outputs can be dependent through their response terms. For example, a reverse output is

    V_s = zeta_s + sum_(r earlier) H_r E[partial_(xi_r) U_s].

The partial derivative here is a formal derivative in the named Gaussian-source slots: already computed expectations, covariances and scalar limits are held fixed. It is different from physical differentiation of the original finite network. Distinct source names must remain distinct formal coordinates even if singular covariance makes them equal almost surely.

## Neural-network normalization and the examples

Use L for hidden depth, m for fixed sample count, d for fixed input dimension, and n for hidden width. In the showcased MLP, the first-layer preactivation is W_1 x/sqrt(d), hidden stored matrices have entry variance 1/n, and the readout is f_n(x)=w^T h_L(x)/n with order-one initialized readout coordinates. Under half-mean squared loss, vector blocks have mobility proportional to n and hidden matrix blocks have constant mobility. These choices matter: they allow order-one feature motion. They are a reparameterization of the maximal-update model in Tensor Programs IV, rather than an independent training regime.

The examples establish a concrete progression:

- Reuse: for J_n=||W^T phi(W1)||^2/n, the limit is E[phi(G)^2]+E[phi'(G)]^2. Conditioning also gives an exact finite-width correction for this particular example. The compiler's general output remains a width limit.
- Represented update: a rank-one state change lowers to a matrix call plus a normalized pairing, and its reuse response is retained.
- Singular queries: duplicate Gaussian sources remain distinct formal slots during source differentiation.
- Moving direction: for x_dot=-x^3 and O=x^2 with a standard Gaussian initial coordinate, E[O''(0)]=120, while a frozen-direction second derivative gives 30. The second Taylor coefficient is 60.
- An MLP gradient-energy calculation includes all relevant parameter blocks and has independently checkable polynomial specializations.
- The two-hidden-layer, two-sample example accepts symbolic geometry factors and symbolic labels, and produces the first three coefficients of the **final hidden feature kernel** under batch gradient flow. This is the readout contribution to the tangent kernel, not the full tangent kernel. Coefficients J_r include 1/r!; derivatives and coefficients must not be interchanged.

The last example uses shared Gaussian first-layer columns and input factors (alpha,0), (beta,gamma), giving G_11=alpha^2, G_12=alpha beta, G_22=beta^2+gamma^2. All positive-semidefinite 2-by-2 geometries can be represented this way, including singular cases, but the supplied interface does not automatically factor an arbitrary symbolic covariance matrix. Labels enter through ordinary symbolic scalar parameters and the finite-width loss.

## The stronger normal form has a smaller domain

The general output is a finite graph of explicit multivariate Gaussian expectations, ordinary arithmetic, and recursively defined covariance entries. Integrands may contain nested nonlinear expressions.

The activation-moment normal form applies to the separately defined initialization subclass: nonlinear arguments must be the specified original centered Gaussian preactivations. Wick and Stein reduction removes polynomial Gaussian factors in that subclass. It does not turn every expression such as phi(phi(G)) into a product of expectations of activation derivatives at original Gaussian preactivations. The paper appropriately states this restriction. An introduction should retain it.

## What the software accepts and returns

The interface is a typed mathematical builder, `Program`, rather than unrestricted LaTeX, Python tensor code, or natural-language parsing. The source program records populations, Gaussian roots, named matrices, coordinate operations, normalized averages, scalar symbols, represented updates and requested derivatives.

Physical AD includes directional derivatives, reverse gradients, divided-factorial jets, moving/frozen flow derivatives and finite curve jets. The state-update routines differentiate the ambient objective before substituting the update history. A frozen seed suppresses physical differentiation of the seed; it does not suppress its Gaussian-source dependence in reuse corrections.

The output contains a symbolic scalar expression; ordered expectation definitions with integrands, source coordinates and covariance matrices; vector representatives and source identities; and a transformation trace. It can print a readable formula and serialize its mathematical data. Generic integrals remain integrals. Polynomial specializations can be evaluated through exact Gaussian moments.

The `Program` Gaussian-root covariance interface checks **concrete** positive semidefiniteness. Symbolic geometry is supplied through scalar coefficients multiplying shared independent roots. The lower-level Gaussian-expression constructor can store symbolic covariance entries, with validity then the caller's responsibility. These are distinct capabilities; the frontend should not be described as accepting every symbolic covariance table directly.

Unsupported operations include unrestricted dense matrix directions, arbitrary indexed contractions, inverse operations or arbitrary negative/fractional powers, and cross-population coordinatewise operations. There is no general numerical integration backend or automatic complexity bound. Formula size, polynomial degree, covariance storage, exact-arithmetic cost and simplification can grow rapidly.

## Proof assessment and boundaries

The complete 2,967-line manuscript was read, including proofs, examples, appendix and implementation guide. Its logical separation is appropriate: exact finite algebra; bounded/smooth Gaussian-program foundation; removal of regularizations; raw-entry moment bounds and uniform integrability; and a separately delimited normal form. No new counterexample to its stated central smooth fixed-program theorem was found in this review. This is an inspected mathematical argument, not a machine-checked proof or a certification of every possible implementation execution.

The conditioning/source rules are substantially those of Tensor Programs III. The all-moment mechanism is substantially that of Non-Gaussian Tensor Programs Appendix J, which the manuscript credits. Independent derivations and an explicit constructive organization are worthwhile, but do not establish priority for the underlying probabilistic result.

A fresh isolated reviewer subsequently read the complete manuscript and guide, reconstructed the six main proof bridges, inspected the compiler/expression modules and example producers, and found no substantive missing step or accepted-example scope violation. Its [independent report](independent_mfp_audit.md) records exact locations, caller obligations and remaining checks. This is additional mathematical review, not machine verification. In particular, the frontend cannot automatically prove user-supplied activation growth assumptions or a user's identification of original network preactivations; these are disclosed caller obligations.

The theorem does not establish convergence of the Taylor series, reconstruction at positive physical time, a width-uniform flow existence interval, growing depth/input count/derivative order/update count, finite-width accuracy rates, efficient compilation, or arbitrary derivative-tensor contraction support. It also does not establish practical learning-performance improvements. These are absent guarantees, not defects in the finite-query theorem.

## Executed validation

The full bundled test selection `test_mfp_*.py` passed: **72 tests**, 19.689 seconds, exit status 0. Log: `data/generated/mfp_literature_positioning_20261011/mfp_tests.log`. The core compiler, expression representation, finite interpreter and kernel-jet example producer were inspected directly. All test bodies and every auxiliary module were not independently audited line by line.

The example producers were rerun into this study's generated directory; their commands, statuses and times are recorded in `data/generated/mfp_literature_positioning_20261011/mfp_examples/runs.json`. No producer writes to the manuscript or established example outputs. Passing tests and matching examples support the implemented contract; they do not prove correctness for every accepted program. No scalability benchmark was run.

Frozen SHA-256 values:

- `paper_MFP/main.tex`: `a43acbc76e53a3437ed5136137fd8e5497a6d65826447c1ac95764a1cba8d38e`.
- `paper_MFP/code/pde/mfp_compiler.py`: `19e862cf6863b28fc2949be3c9fa2a60ab13f985e2d4c7bb97928423127f12b6`.
- `paper_MFP/code/pde/mfp_expr.py`: `1340df2e1cd7279d568aa07610bfba033eaf95d8fc75426d8149b2b4d9cbcfa8`.
- `paper_MFP/code/pde/mfp_finite.py`: `84060153c467172eaabaed073ece4e8fd0d77fbc1ed2fee3e8a66542d2c7c037`.
- `paper_MFP/code/scripts/example_mfp_kernel_jets.py`: `3298421fad2776bf306b0928611517b938529429de7606efd53ecf1caaa2d03c`.

# Independent reassessment of the MFP calculus contribution

This assessment was made from the complete `paper_MFP/main.tex`, the complete bundled compiler, expression and finite-interpreter modules, the guide, three example producers and four test modules. The bundled Gaussian-moment and finite-network import dependencies were also read. No prior review, study finding or repository history was used. The canonical-notation skill, its neural-network reference, and `solve-math-rigorously` were applied. This is a scope and substance assessment, with targeted implementation checks, rather than a novelty claim or a formal verification of the software.

The strongest defensible characterization is: **MFP provides a constructive, mathematically justified calculus that takes an admitted finite neural derivative or training computation, expands it exactly at finite width, and produces its deterministic infinite-width Gaussian expectation graph, retaining matrix reuse, scalar feedback and moving directions.** At initialization a restricted class reduces further to activation-derivative moments. This is a substantive end-to-end result. Its differentiation rules use familiar calculus, and the manuscript explicitly does not claim a new general probabilistic program theorem. Calling the whole result only a set of conventions would omit its convergence, closure and reduction assertions; calling it a new general theory of all neural training dynamics would exceed its scope.

## The actual end-to-end assertion

Fix hidden depth $L$, sample count $m$, input dimension $d$, requested derivative order $R$, update count and the whole instruction list before the width $n\to\infty$. Each declared vector type is a separate population of $n$ coordinates. Named initialized matrices between distinct types have independent $N(0,1/n)$ entries; a transpose reuses the same named matrix. Root tuples have fixed Gaussian laws, are iid across coordinates within a type, and are independent across types and of matrices. Singular root and query covariance is allowed. The single activation satisfies $\phi\in C^\infty$, with every derivative of polynomial growth. The primitive language consists of coordinate expressions made from constants, sums, products and activation derivatives; normalized averages; scalar sums and products; and typed named matrix actions. These are genuine restrictions, not placeholders for arbitrary tensor operations. See the definition beginning at [main.tex:606](/home/amir/Codes/PDE/paper_MFP/main.tex:606), the growth hypothesis at [main.tex:652](/home/amir/Codes/PDE/paper_MFP/main.tex:652), and the exclusions immediately following it.

A current matrix is represented by

\[
A=W_0+\sum_{\nu=1}^{M}c_\nu u_\nu v_\nu^\top/n,
\]

and a matrix direction by the same finite rank sum without an initialized base. This permits exact lowering of $Ah$ and $A^\top u$ into initialized matrix calls and normalized scalar pairings. Physical derivatives include deterministic scalar/input derivatives, finite directional derivatives, scaled vector gradients, ordinary matrix gradients, their admitted contractions, fixed gradient updates and finite flow jets. The theorem is [“Scalar limits and uniform moments,” main.tex:694](/home/amir/Codes/PDE/paper_MFP/main.tex:694); its exact-compilation component is [“Exact compilation of admitted derivatives,” main.tex:1260](/home/amir/Codes/PDE/paper_MFP/main.tex:1260).

For every resulting scalar observable $O_n$, the theorem constructs a deterministic value $O_*$ and proves

\[
\mathbb E|O_n-O_*|^p\longrightarrow0\qquad(1\le p<\infty).
\]

It also proves uniform moments of each scalar node and of normalized vector-coordinate moments, and joint empirical convergence in probability in quadratic Wasserstein distance for every fixed same-type vector tuple. Thus it identifies expectation limits, not merely formal Gaussian approximations. Individual vector coordinates remain random in the limit. For finite jets this says that the **actual finite-width initial derivative coefficients** converge; it does not exchange a width limit with differentiation of an independently constructed positive-time limiting flow.

The output is a causal, finite graph of explicitly specified expectations,

\[
I_j=\int F_j(g;I_1,\ldots,I_{j-1})\,
       N(0,K_j(I_1,\ldots,I_{j-1}))(dg),
\qquad O_*=P(I_1,\ldots,I_N),
\]

where the final assembly $P$ is polynomial and fixed deterministic parameters can remain symbolic. The integrands and covariance dependencies come from the input program, not an unknown neural law. This graph is an exact specification of the limiting number under the assumptions; generic integrals are not numerically evaluated. See [main.tex:783](/home/amir/Codes/PDE/paper_MFP/main.tex:783).

## Which parts carry mathematical content

| Component | What it establishes | Assessment of its role |
| --- | --- | --- |
| Typed syntax, scaled adjoints, factorial-normalized jets | Specifies which finite object is requested and fixes all normalizations | Definitions and conventions. They avoid ambiguity but are not convergence theorems. |
| Exact derivative/update closure | Every admitted request becomes a finite primitive program with exactly the same finite-width value | A mathematical closure/correctness proposition. Its local ingredients are product, chain and adjoint rules; the meaningful assembly is that represented matrix directions, reuse and moving flow derivatives remain in the probabilistically controlled language. |
| Source-response law | Determines the limiting scalar fields after each forward/transpose call, including dependence caused by reuse | The main probabilistic identification step. A fresh independent Gaussian replacement alone would be wrong. Adaptive conditioning and its response cancellation are essential. |
| Singular-query treatment | Extends the scalar law without assuming stable query rank or continuity of empirical pseudoinverses | A genuine stability theorem, proved by perturbing queries and passing to zero perturbation through covariance square roots and derivative expectations. |
| Raw-entry moment bounds and unclipping | Gives uniform moments for polynomial-growth maps and promotes convergence to every finite scalar $L^p$ | An analytic result beyond symbolic bookkeeping; it controls correlated reuse and feedback. The manuscript attributes the raw-entry mechanism to Golikov and Yang. |
| Initialization activation-moment reduction | Eliminates explicit Gaussian polynomial factors and reduces a literal initial-preactivation subclass to recursively specified activation-derivative moments | A terminating symbolic normal-form result, based on Gaussian integration by parts and a syntactic closure induction. It does not apply to every general Gaussian graph. |
| Python implementation and tests | Exposes builders, differentiation, source evaluation, reductions and finite-array checks | Executable realization and evidence of implementation consistency, not a proof of the mathematical theorem or a novelty comparison. |

The source rule is particularly concrete. For calls $Wh_r$ and $W^\top u_s$, write $H_r,U_s$ for their scalar input representatives. A new forward answer is

\[
Y_r=\xi_r+\sum_{s\text{ earlier reverse}}U_s\,
          \mathbb E[\partial_{\zeta_s}H_r],
\qquad \operatorname{Cov}(\xi_r,\xi_t)=\mathbb E[H_rH_t],
\]

with the corresponding reversed formula. The separate oriented source groups are independent, while the resulting fields need not be. This is not an independence assumption on reused outputs. For example, $n^{-1}\|W^\top\phi(W\mathbf1)\|^2$ has limiting value

\[
\mathbb E\phi(G)^2+(\mathbb E\phi'(G))^2,
\qquad G\sim N(0,1).
\]

The second term is lost by treating $W^\top$ as independent. With identity activation the exact finite expectation is $2+1/n$, whereas the compiled limit is $2$. See [main.tex:760](/home/amir/Codes/PDE/paper_MFP/main.tex:760) and [main.tex:1425](/home/amir/Codes/PDE/paper_MFP/main.tex:1425).

The proof architecture is inspectable: the raw-entry lemma begins at [main.tex:813](/home/amir/Codes/PDE/paper_MFP/main.tex:813), the finite typed-graph bounded extension at [main.tex:938](/home/amir/Codes/PDE/paper_MFP/main.tex:938), and the clipping/removal proof at [main.tex:1031](/home/amir/Codes/PDE/paper_MFP/main.tex:1031). The appendix supplies the adaptive conditioning and source-rule proof, followed by singular-query regularization and causal scalar feedback. No special empirical inverse needs to converge in the final evaluation rule. This is why describing the result as “just AD followed by an expectation” understates the required probabilistic argument.

Conversely, the assertion that $P$ is polynomial should not be oversold on its own: arbitrary nonpolynomial coordinate effects can reside in expectation nodes, including zero-dimensional integrals for nonlinear deterministic scalar feedback. The stronger restricted normal form carries additional information about the integrands themselves.

## Neural queries enabled by the result

For the stated neural specialization, use

\[
z_a^{(1)}=W^{(1)}x_a/\sqrt d,\quad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\quad
h_a^{(\ell)}=\phi(z_a^{(\ell)}),\quad
f_{n,a}=W^{(L+1)\top}h_a^{(L)}/n.
\]

The first-matrix columns and stored readout are vector roots; first-layer entries have variance one, hidden entries variance $1/n$, and the stored readout a fixed variance $\tau^2$. With $r_{n,a}=f_{n,a}-y_a$, the manuscript's general loss is $\mathcal L_n=m^{-1}\sum_a r_{n,a}^2$, with vector mobilities $n\kappa_1,n\kappa_{L+1}$ and hidden-matrix mobilities $\kappa_\ell$. See [main.tex:1305](/home/amir/Codes/PDE/paper_MFP/main.tex:1305). The kernel example instead uses the half-mean loss, so its clock is slower by a factor of two.

For each fixed $L,m,d,R$, one can construct the forward program, form the loss gradient in the shared parameters, form any admitted scalar output/kernel/loss observable, and request moving derivatives through order $R$. A feature kernel $n^{-1}h_a^{(\ell)\top}h_b^{(\ell)}$ is directly a normalized pairing. A full mobility-weighted tangent kernel is also expressible: vector gradient blocks contract through normalized vector pairings and matrix gradient blocks through products of normalized pairings of their rank-one factors. The library's `frobenius` implements precisely this contraction. Output and loss jets are scalar instances of the same theorem; a separate probabilistic theorem is not needed for each observable.

Data geometry and labels can remain fixed symbolic coefficients. Shared first-weight columns are important: replacing each sample's correlated preactivation by an independently trainable parameter would change the finite gradient field. The producer correctly constructs $z_1^{(1)}=\alpha U$, $z_2^{(1)}=\beta U+\gamma V$ from shared columns $U,V$, so the geometry enters the actual parameter derivatives. It is not merely inserted into a terminal covariance formula.

The initialization normal form applies when every nonlinear node is literally $\phi^{(r)}(z_a^{(\ell)}(0))$ for an original feedforward preactivation. The ordinary finite-order derivatives of the stated feedforward network and polynomial squared-loss flow at initialization have this property: differentiating raises activation derivative order and multiplies by derivative fields without replacing the activation argument by a derivative field. The proposition then reduces their limiting scalars to finite polynomials in recursively determined activation-derivative moments. See [main.tex:1342](/home/amir/Codes/PDE/paper_MFP/main.tex:1342). An updated preactivation or a nonlinear function of a derivative field generally requires the general expectation graph instead. The restricted reduction is neither a Gaussianity claim about derivative fields nor a normal form for every trained state.

### A concrete initial-jet corollary and its integration dimension

For the stated standard zero-bias MLP, a polynomial loss in the predictions and fixed labels, fixed block mobilities, and an admitted scalar observable polynomially assembled from the original preactivations, activations, predictions and finitely many admitted parameter derivatives/gradient contractions, **every finite-order initial moving gradient-flow jet reduces to a finite polynomial in fixed model/data constants and activation-derivative moments under the original layerwise forward Gaussian laws**. Each remaining activation integral can be written in at most $m$ Gaussian coordinates, independently of derivative order and depth.

More precisely, define

\[
\Sigma^{(1)}_{ab}=x_a^\top x_b/d,\qquad
\Sigma^{(\ell+1)}_{ab}
 =\mathbb E_{Z\sim N(0,\Sigma^{(\ell)})}[\phi(Z_a)\phi(Z_b)].
\]

For each layer $\ell$ and finite list of sample/derivative-order pairs $(a_1,k_1),\ldots,(a_q,k_q)$, let

\[
M_{\ell;(a_1,k_1),\ldots,(a_q,k_q)}
 =\mathbb E_{Z\sim N(0,\Sigma^{(\ell)})}
       \prod_{j=1}^{q}\phi^{(k_j)}(Z_{a_j}).
\]

Repeated sample indices and different derivative orders at the same sample are allowed; the empty product is one. For each fixed $r$, the limit

\[
\lim_{n\to\infty}\mathbb E\!\left[
 \frac1{r!}\left.\frac{d^r}{dt^r}O_n(\theta_n(t))\right|_{t=0}\right]
\]

is a finite polynomial in finitely many such $M$'s and fixed model/data constants, including normalized input coordinates, labels, readout covariance, loss coefficients and block mobilities. The random coefficient also converges to that value in every finite $L^p$. This is pointwise in the fixed parameters. Neither uniformity nor a bound on the number of atoms as $r$ varies is asserted. The activation derivative orders needed after Stein reduction can exceed $r$, while remaining finite.

Here is the derivation.

1. Construct the complete original forward graph first. Let the subclass consist of primitive expressions whose only activation nodes are $\phi^{(k)}(z_a^{(\ell)}(0))$ at those literal original preactivation nodes. Forward physical differentiation preserves it:
   \[
   D[\phi^{(k)}(z_a^{(\ell)})][v]
   =\phi^{(k+1)}(z_a^{(\ell)})\,Dz_a^{(\ell)}[v].
   \]
   The activation argument remains the original node. Products, means, matrix actions and represented directions introduce no new activation argument. Reverse differentiation also inserts activation derivatives only at original arguments; matrix gradients remain finite normalized rank sums. These facts follow directly from the tables in the exact-compilation proposition.
2. A polynomial loss in the original predictions and labels belongs to this class, and so does its gradient field $V$ with the stated mobilities. Define $O_{n,0}=O_n$, $O_{n,j+1}=DO_{n,j}[V]$. The preceding closure proves by induction that every $O_{n,j}$ remains in the class. For each local smooth finite-width solution, its value at initialization is the actual $j$-th time derivative. Later iterations differentiate the inserted field, including residuals and $DV[V]$; no direction is frozen.
3. The limiting scalar representatives of the original forward preactivations at layer $\ell$ are jointly centered Gaussian with covariance $\Sigma^{(\ell)}$, since their construction requires no reverse call. This statement concerns the limiting representatives, not an unconditional Gaussian law for the finite-width deep preactivations. On that type's probability space, adjoin all auxiliary roots and named Gaussian sources used in the derivative computation. Together these form a finite joint Gaussian family with causally determined covariance entries. Every field is a finite sum of a polynomial in this Gaussian family times products of activation derivatives only at original preactivations, with deterministic coefficients polynomial in earlier expectation values. This is the normal-form proposition's symbolic induction.
4. Remove all explicit Gaussian polynomial factors using
   \[
   \mathbb E[G_iF]=\sum_j\operatorname{Cov}(G_i,G_j)\,
                            \mathbb E[\partial_jF].
   \]
   Removing the selected factor lowers explicit polynomial degree. A derivative hitting another polynomial factor lowers it further; a derivative hitting an activation raises its derivative order at the same original preactivation. No activation at an auxiliary source is introduced, so the procedure terminates.
5. The remaining integrand depends only on original layer-$\ell$ preactivations. Marginalizing the other Gaussian coordinates gives exactly an atom $M_{\ell;\cdots}$, whose covariance is a submatrix of the original $\Sigma^{(\ell)}$. One may also duplicate coordinates and use repeated-index covariances, but this is unnecessary: repeated factors at sample $a$ all use the same scalar $Z_a$. At most $m$ distinct sample coordinates remain. Cross-type coordinate products are excluded by the language; cross-layer scalar products are products of deterministic expectations, not a requirement to integrate a joint tuple across layers.
6. Auxiliary-source covariances occur as coefficient factors in these integration-by-parts steps. Each was computed from products of earlier input fields in the causal source graph. Apply the same reduction to those earlier expectations and substitute backward through the finite graph. The final result therefore uses fixed constants and the same original-forward activation-moment family, with no unidentified auxiliary covariance law, inverse or square-root coefficient. The covariance recursion for $\Sigma^{(\ell)}$ itself is included in this layerwise family.

This is a corollary of the manuscript's closure, normal-form and limit assertions, not a separate novelty claim. The bound is on each remaining activation integral, not the number of integrals, algebraic expression size, source-table size or computational work. Nonpolynomial losses applied to predictions, activations applied to derivative fields, updated preactivations, or state-dependent mobilities introducing new nonlinear arguments can leave this subclass. They may still be admitted by the general Gaussian-graph theorem, but the corollary then does not follow.

The mathematical re-expression should also be distinguished from the software output. With an explicit declaration of original preactivations, the implementation does contain integration-coordinate rebasing: [mfp_compiler.py:696](/home/amir/Codes/PDE/paper_MFP/code/pde/mfp_compiler.py:696) substitutes declared linear field expressions by preactivation aliases before requesting flat-only Stein reduction; [_atom at line 657](/home/amir/Codes/PDE/paper_MFP/code/pde/mfp_compiler.py:657) retains only Gaussian coordinates appearing in the remaining integrand; [_integration_cov at line 691](/home/amir/Codes/PDE/paper_MFP/code/pde/mfp_compiler.py:691) computes their induced covariance. Literal Gaussian preactivations already represented by single source/root symbols need no alias. Thus, for a successfully compiled graph in this declared standard-MLP subclass, activation atoms use the original preactivation coordinates, rather than every first-weight column or auxiliary source. Source and trace tables still retain the larger formal coordinate system. Without the preactivation declaration, general compilation does not promise this dimension reduction.

As a concrete check of the rebasing mechanism, I built five independent first-layer roots $U_j$, five fixed symbolic coefficients $a_j$, the single preactivation $z=\sum_{j=0}^4a_jU_j$, and the observable $\operatorname{mean}(U_0^2\phi''(z)^3)$. Compiling with that declared preactivation retains five root-source records but emits three one-dimensional activation atoms, each with variance $\sum_j a_j^2$. Their assembly is

\[
\mathbb E[\phi''(Z)^3]
 +3a_0^2\mathbb E[\phi^{(4)}(Z)\phi''(Z)^2]
 +6a_0^2\mathbb E[\phi''(Z)\phi'''(Z)^2],
\qquad Z\sim N(0,\textstyle\sum_j a_j^2),
\]

as independently obtained by two applications of Gaussian integration by parts. This checks a case with input dimension larger than sample count and illustrates the distinction between retained source dimension and activation integration dimension.

## What the implementation actually exposes

High-order moving flow is implemented in the **general** `Program` interface, not only by a query-specific kernel frontend. [`directional`, line 380](/home/amir/Codes/PDE/paper_MFP/code/pde/mfp_compiler.py:380) differentiates the finite graph, including means, products, activations and both matrix orientations. [`derivatives`, line 417](/home/amir/Codes/PDE/paper_MFP/code/pde/mfp_compiler.py:417) accepts every nonnegative integer order and repeatedly applies that operation. It freezes the direction expressions only when `moving=False`. With `moving=True`, later differentiation traverses the inserted vector field, retaining $DV[V]$ and all further state dependence. [`jets`, line 438](/home/amir/Codes/PDE/paper_MFP/code/pde/mfp_compiler.py:438) divides coefficient $r$ by $r!$. This repeated Lie-derivative implementation is mathematically equivalent to the manuscript's ODE coefficient recursion; it need not implement the same recurrence literally.

The kernel producer's [`compile_example`, line 56](/home/amir/Codes/PDE/paper_MFP/code/scripts/example_mfp_kernel_jets.py:56) calls `p.jets(network["kernel12"], flow, order=order, moving=True)` and then ordinary `compile`. Its command line accepts `--order`. There is no special-case order-two kernel differentiation routine. However, its architecture and batch are fixed to $L=m=d=2$, and it defaults to $R=2$. Arbitrary fixed depth/batch requires writing the corresponding builder program; no general neural architecture parser or parameterized MLP constructor is bundled. Thus “a general calculus with a two-layer/two-sample producer” is accurate; “only a bespoke second-order kernel calculator” is not.

The main theorem's core primitive grammar, admitted derivatives, updates and source evaluation are closely represented by the API. They are not identical to every statement elsewhere in the manuscript:

- The appendix also treats finite-second-moment, potentially non-Gaussian roots and locally Lipschitz feedback operations near their limiting arguments. The public root frontend is Gaussian, and the smooth main theorem/implemented grammar does not include general division or arbitrary scalar callbacks.
- Root covariance declarations accept concrete numbers, checked by exact rational arithmetic. They do not accept symbolic covariance matrices. Symbolic fixed geometry can be encoded through coefficients of actual shared Gaussian columns; finding a factorization of an arbitrary symbolic PSD covariance is not an API operation.
- The caller must supply the architecture, correct parameter sharing, the smooth polynomial-growth activation assumption, and which literal nodes really are the original preactivations. The compiler checks declared types and the literal-node/centered-linear conditions, not the architecture's provenance or analytic growth hypothesis.
- The convenience gradient-descent helper allows fixed deterministic steps and block factors and updates vector/matrix blocks. More general admitted finite arithmetic can be built directly; the helper is not an arbitrary optimizer interface.
- Mixed fixed-direction derivatives are assembled from successive directional calls and frozen seeds. There is no dedicated general multivariate jet frontend, although the primitive closure supports these finite requests.
- Python recursion, graph growth and exact rational expression expansion impose practical limits. There is no efficiency theorem or realistic claim that every large fixed order is computationally affordable.

The inherited `finite_network.py` is a distinct numerical API and is not the symbolic compiler's derivative frontend. In particular its default initializer has stored readout variance $1/n^2$, while the MFP neural examples explicitly choose fixed order-one readout variance. The manuscript correctly says the fixed-root-law theorem does not by itself cover that width-dependent default. The numerical module also supports layer-specific activation callbacks, which should not silently expand the single-activation symbolic grammar.

## Checks of the three delicate mechanisms

**Scalar feedback.** In physical AD the `mean` branch differentiates its input and averages the derivative; reverse AD propagates through means/broadcasts and averages the scalar contributions of vector operations. In Gaussian compilation a mean becomes an expectation coefficient before later source partials are taken. Consequently $c_n=\operatorname{mean}(\phi(W\mathbf1))$ is differentiated physically if it depends on a trainable state, but its limiting value $c_*$ is held fixed when computing the source partial of $c_*\phi(\xi)$. These are different mathematical derivatives, not a contradiction. The concrete compiler test at [test_mfp_compiler.py:553](/home/amir/Codes/PDE/paper_MFP/code/tests/test_mfp_compiler.py:553) checks the emitted derivative and the limit $c_*^2\{\mathbb E\phi(G)^2+(\mathbb E\phi'(G))^2\}$. Finite rational polynomial-oracle tests separately exercise derivatives and gradients with averages fed into scalar arithmetic and directions.

I also checked the general API through order six against a solvable feedback flow independent of the kernel producer. For $O_n=\operatorname{mean}(x^2)$, loss $O_n^2/4$ and vector mobility $n$, the exact field is $\dot x=-O_nx$; hence $\dot O_n=-2O_n^2$ and $O_n(t)=O_n(0)/(1+2O_n(0)t)$. Its normalized coefficient is $(-2)^rO_n(0)^{r+1}$. All coefficients $r=0,\ldots,6$ match the finite interpreter at exact rational arrays and compile to $(-2)^r$ for standard Gaussian roots. The reproducible check is [reassessment_calculus_checks.py](/home/amir/Codes/PDE/studies/mfp_literature_positioning_20261011/reassessment_calculus_checks.py). This is targeted software evidence, not a new all-order proof.

**Moving directions.** The simple producer uses the gradient of $\operatorname{mean}(x^4)/4$, yielding $\dot x=-x^3$. The code distinguishes the frozen second derivative $2\operatorname{mean}(x^6)$, with limit $30$, from the moving second derivative $8\operatorname{mean}(x^6)$, with limit $120$. In the neural producer, the loss includes the predictions and labels before `gradient` is called; all $U,V,W^{(2)},W^{(3)}$ blocks are included in `flow` ([example_mfp_kernel_jets.py:40](/home/amir/Codes/PDE/paper_MFP/code/scripts/example_mfp_kernel_jets.py:40)). Residuals are therefore differentiated with the field. The exact rational dense-backpropagation/coefficient-convolution oracle at [test_mfp_kernel_jets.py:195](/home/amir/Codes/PDE/paper_MFP/code/tests/test_mfp_kernel_jets.py:195) checks all blocks and moving jets through order two at widths two and three and distinguishes them from the straight path. The nonlinear kernel's long second-coefficient regression and generic-to-quadratic specialization share the source-rule implementation; neither alone independently proves that entire limiting polynomial.

**Singular sources.** Every matrix-call node obtains its own source symbol, and covariances are computed from the input Gram. Source differentiation uses the named expression before any integration-coordinate alias is introduced; no inverse or source-identity substitution appears in that branch ([mfp_compiler.py:748](/home/amir/Codes/PDE/paper_MFP/code/pde/mfp_compiler.py:748)). With two calls $y_1=W\mathbf1,y_2=W\mathbf1$, the test at [test_mfp_compiler.py:459](/home/amir/Codes/PDE/paper_MFP/code/tests/test_mfp_compiler.py:459) uses $y_1^2y_2$: the two response coefficients are separately $2$ and $1$, and the limit is $24$. This is stronger evidence than a test checking only covariance rank. The generic `singular_queries` producer uses $\phi(y_1+y_2)$, and the linear-alias test at [test_mfp_compiler.py:580](/home/amir/Codes/PDE/paper_MFP/code/tests/test_mfp_compiler.py:580) checks that a variance-four integration alias leaves both original formal source slots intact. Frozen physical seeds likewise retain their source dependence, checked at [test_mfp_compiler.py:374](/home/amir/Codes/PDE/paper_MFP/code/tests/test_mfp_compiler.py:374).

This source-slot convention is a sound way to implement the response formula; it should not be described as a claim that Gaussian support admits no equivalent reduced-coordinate description. The manuscript itself proves that contracted corrections are invariant under admissible expressions agreeing on singular support, although individual partial coefficients may differ. Its substantive analytic point is that rank loss does not invalidate the limit formula.

All 72 bundled tests passed in this assessment (`PYTHONPATH=code python -B -m unittest discover -s code/tests -p 'test_mfp_*.py' -v`, from `paper_MFP/`; 19.748 seconds). The separate order-six feedback check also passed. No manuscript or bundled implementation was modified.

The combined new checks are retained as [flat study source](/home/amir/Codes/PDE/studies/mfp_literature_positioning_20261011/reassessment_calculus_checks.py). From the checkout root, their exact command is:

    python -B studies/mfp_literature_positioning_20261011/reassessment_calculus_checks.py

The command exited with status zero. Orders zero through six passed the exact finite ODE and Gaussian-limit identities; the five-root/single-preactivation example passed the one-dimensional-atom and independent Stein-identity checks. The complete [check output](/home/amir/Codes/PDE/data/generated/mfp_literature_positioning_20261011/reassessment_calculus/checks.log) and [source SHA-256 manifest](/home/amir/Codes/PDE/data/generated/mfp_literature_positioning_20261011/reassessment_calculus/source_hashes.json) are generated artifacts. The manifest records the manuscript, guide, bundled Python sources/tests/producers and verification script. Principal frozen fingerprints are:

| Source | SHA-256 |
| --- | --- |
| Manuscript | a43acbc76e53a3437ed5136137fd8e5497a6d65826447c1ac95764a1cba8d38e |
| Compiler | 19e862cf6863b28fc2949be3c9fa2a60ab13f985e2d4c7bb97928423127f12b6 |
| Expression engine | 1340df2e1cd7279d568aa07610bfba033eaf95d8fc75426d8149b2b4d9cbcfa8 |
| New verification script | 1a4252e5fa3b5c47895c4bb98697cef357dffbe767945c5f59c9f547e1f231ca |

## Positioning language and overclaims

A defensible significance statement is:

> The contribution is an executable calculus for a precisely delimited class of finite neural derivative and training queries: exact finite-width differentiation and update lowering are connected to a causal Gaussian source-response limit theorem, including scalar feedback, repeated matrix/transposed-matrix use and singular query covariance. This connection permits systematic symbolic initial output, loss and kernel flow jets at any fixed depth, batch size and order under the stated assumptions, with an activation-moment reduction for the original-preactivation subclass.

This identifies what becomes possible without claiming that the component AD, Gaussian-conditioning, Stein or program-limit ideas are unprecedented. A defensible originality judgment would need a comparator that matches the admitted syntax, derivative/flow semantics, scalar feedback, singular handling, moment guarantees and executable frontend. Merely observing that the local differentiation rules are standard does not settle the contribution of the complete construction; merely presenting a compiler does not establish that no earlier calculus provided the same construction. The manuscript acknowledges the adapted moment mechanism and explicitly disclaims a new general probabilistic program theorem at [main.tex:303](/home/amir/Codes/PDE/paper_MFP/main.tex:303).

The following stronger claims would not be supported:

1. **Exact finite-width Gaussian compilation.** Only differentiation and represented-action lowering are exact at finite width; `compile` gives the width limit.
2. **Arbitrary neural architectures or arbitrary parameter tensors.** The typed language excludes many operations, dense arbitrary matrix directions, cross-type contractions and width-dependent primitives.
3. **All initializations or the numerical API's small-readout law.** The main theorem assumes fixed Gaussian roots and Gaussian initialized matrices; the separate bounded appendix does not transfer its broader root assumptions to the all-moment derivative theorem.
4. **A general activation-moment form after training.** Literal original initial preactivations are required. General updated computations produce general Gaussian integrands.
5. **Positive-time reconstruction or a finite autonomous population ODE.** A finite initial jet graph provides neither; no uniform time horizon or convergent infinite Taylor series is proved.
6. **Uniformity or efficiency as depth, batch, order or update count grow.** Each is fixed first. Finiteness of a construction is not a complexity or uniform-convergence guarantee.
7. **The supplied kernel example computes the full tangent kernel.** It computes the last-layer feature kernel/readout block. The full kernel is expressible in the general grammar, but that is a distinct observable.
8. **A wholly general neural frontend is already shipped.** The general engine is present; the bundled neural recipes are specific builders. Symbolic covariance factorization and architecture inference remain with the caller.
9. **Tests prove the limit theorem or independent correctness of every displayed long coefficient.** The theorem needs its analytic proof, and shared compiler paths are not independent probabilistic oracles.
10. **Novelty of the complete calculus established by this assessment.** This assessment verifies the internal contribution and its scope; priority and novelty require a direct external comparison.

The calibrated conclusion is that MFP supplies a meaningful constructive bridge from finite derivative/training queries to explicit deterministic Gaussian calculations. The most consequential content is the correctness of that bridge under reuse, feedback, polynomial-growth differentiation and singularity; the everyday differentiation identities are its necessary local machinery.

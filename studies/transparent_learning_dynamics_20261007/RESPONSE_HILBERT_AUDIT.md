# Scoped audit of the common Hilbert response realization

Date: 2026-10-07. Reviewer: causal-Gaussian route agent.

**Verdict: PASS for the stated countable generating family and its continuous $L^2$ extensions.** The bounded-operator, adjoint, nonlinear-closure and finite-Euler claims follow from the supplied finite-program law. No gradient-flow existence, uniqueness, uniform Euler approximation or all-time result is established by this audit.

The countable-language interpretation should be made explicit as described below. These are scope and construction clarifications, not a counterexample to the stated countable-family theorem. If the opening phrase “every prescribed finite program” is intended to include arbitrary new real constants, the enlargement argument in Section 2 supplies the required extension.

## 1. Read coverage, inputs and limits

I read RESPONSE_HILBERT_REALIZATION.md completely, lines 1–197, at SHA-256:

23118c6bfe5a6200a2653aad51d4de8813b7e4c2d049d13ed19e4915d8738ed3.

Permitted dependencies were this route's own finite Gaussian-program results and the complete UNCLIPPED_FINITE_HISTORY.md, most recently read at SHA-256:

9d842305cf984f2f5841466faf878e99f8f40815cebbc9f5ec341f9642b9ee81.

I did not read other studies, additional agent findings, integrated dense-flow premises or literature. I ran no experiment. Checks below are direct reconstructions of the argument. The original candidate was not edited.

The finite-program law is used in its actual scope: finite concatenated programs have deterministic limits of all needed same-population second and cross moments, with joint bounded-Lipschitz row-law convergence. It is not used as a uniform statement over growing programs. Every limit passage below concerns a single finite prefix before a deterministic Hilbert-space closure is taken.

This is a scoped internal research audit. Because the candidate depends on finite-program results to which I contributed, this is not an author-independent promotion review.

## 2. Countability, chronology and compatibility

The intended formal library can be made countable as follows:

* start with the finite named roots, constant-one fields, matrix interfaces and designated activations/gates;
* use rational coefficients for the generating linear combinations;
* use bounded piecewise-linear functions with **finitely many** rational breakpoints and rational values, with bounded tails;
* include the finitely or countably many named real data constants and scalar coefficient-map symbols in the prescribed program family;
* form finite expressions with explicitly named register dependencies.

The word “finitely” for the piecewise-linear descriptions is useful: arbitrary infinite rational breakpoint/value sequences do not form a countable instruction library. Finite descriptions are sufficient for every density argument in the note.

Each expression has a finite dependency graph. A fair enumeration exists: enumerate the countable set of finite expressions, and, at each stage, append any not-yet-generated dependency expressions before the selected expression. Every stage adds finitely many instructions; every selected expression eventually appears. No instruction is placed after infinitely many predecessors.

Interleaved neural runs must have their own named state/history registers while sharing the named initialized matrices and roots. Scalar coefficients use their explicitly declared earlier pairings; they do not depend on an unnamed mutable “current” global summary. With that ordinary formal-program convention, interleaving extra instructions leaves each original finite-width computation unchanged. The additional instructions only observe the same matrices and compute additional fields.

At every finite prefix, the finite-program theorem therefore applies to one concatenated program, including all branches and their common matrix reuse. The scalar-history recursion constructs concrete functions of finitely many Gaussian innovations in each population. A countable product of standard Gaussian coordinates supplies all prefixes on one probability space. This construction does not require a separate compactness theorem or an unproved infinite-time limit.

The candidate's consistency argument is sound. If two algebraic paths give the same finite-width field, append both to the same finite program. Their squared empirical difference is exactly zero, so the deterministic limiting squared difference is zero. Likewise, inserting unrelated queries can alter Gaussian regression coefficients used in the proof, but cannot alter the limiting joint law of a fixed collection of original registers: the underlying finite-width registers are identical and their joint limit is unique.

### Real constants and programs outside the initial enumeration

For rational linearity and density, no uncountable enumeration is needed. Real linear combinations are obtained by $L^2$ continuity after the norm bound is proved.

A slightly more general extension also justifies arbitrary real constants in a fixed additional neural program. Enlarge the countable library by that program's finitely many constants and instructions, and build a second realization. All old jointly generated fields have the same joint laws in the two realizations, by finite-prefix compatibility. Sending each old field to its copy defines an isometry of their closed spans. It preserves pointwise Lipschitz functions and bounded gated products, first on generated fields and then by continuity; it also intertwines every matrix and transpose action.

The old closed span already contains real multiples of its constant-one field, all real linear combinations, and the continuous nonlinear extensions. Induction over the new program consequently places its fields in the image of that old span. The enlarged realization identifies their dense finite-width limits, so the old realization has the same identification. This argument uses only finitely many new instructions at a time and does not claim one syntactic enumeration of uncountably many arbitrary function symbols.

The precise statement should thus remain tied to the designated activations/gates and a fixed generating language, with such continuous extensions where needed. The later scope sentence in Section 1 already points in this direction.

## 3. Linearity, null fields and the norm bound

Begin on the rational span of the generated fields. The grammar includes its formal sums and their matrix queries. In one finite program,

\[
G_n(u_n+v_n)-G_nu_n-G_nv_n=0.
\]

The finite second/cross-moment theorem transfers the squared norm of this difference to zero. The same argument proves rational homogeneity. Different representations of a rational linear combination therefore produce the same image after quotienting by null fields.

The Gaussian operator event is valid for arbitrary adapted query vectors; it does not require independence between $u_n$ and $G_n$. The elementary quarter-net argument gives

\[
\mathbb P(\|G_n\|_{\mathrm{op}}>8)
\leq2\exp\{(2\log9-8)n\}\longrightarrow0.
\]

For each fixed generated $u$, both quantities in

\[
\|G_nu_n\|_{2,n}^2\leq64\|u_n\|_{2,n}^2
\]

have deterministic limits. If their proposed limiting inequality failed by a positive amount, convergence in probability would force the opposite strict inequality with probability tending to one, contradicting the operator event. Hence

\[
\|Gu\|_2\leq8\|u\|_2.
\]

In particular, null inputs have null images. The action extends uniquely and continuously to the completion. Real homogeneity then follows by approximating a real scalar with rationals. No positive history gap, Gaussian independence of an adapted query, or uniform-in-program convergence is hidden in this step.

The image of the dense generated domain lies in the generated target space because the appropriate query answers were included in the grammar. Its continuous extension therefore also lands in that closed target space.

## 4. Transpose queries are the Hilbert adjoints

The transpose-query map has the same bound, because $\|G_n^\top\|_{\mathrm{op}}=\|G_n\|_{\mathrm{op}}$. For generated fields in adjacent populations,

\[
\langle G_nu_n,v_n\rangle_n
=\langle u_n,G_n^\top v_n\rangle_n
\]

is an exact finite-width identity. Its two sides converge by the allowed same-population cross-moment theorem. Thus the limiting forward map and transpose map are adjoints on their dense domains. Their bounded extensions preserve this equality for all source and target fields, which uniquely identifies the transpose map with $G^*$.

Only pairings within each neuron population are used. No unsupported pairing of corresponding coordinates from two unrelated populations occurs.

For the first-layer map, choose the advertised $d$ independent standard Gaussian root coordinates. Then

\[
\mathbb E[(A_0v)(A_0u)]=v^\top u
\]

for all $u,v\in\mathbb R^d$, first by finite coordinate expansion and then directly for real coefficients. This realizes the stated isometry. A smaller panel-root representation would need to be enlarged to these $d$ coordinates to obtain an operator on all of $\mathbb R^d$; the candidate explicitly makes that choice in Section 3.

## 5. Pointwise operations and identification with a full $L^2$ space

The Lipschitz activation estimate is correct. Since constant-one belongs to the space, $\phi(u)$ is square integrable even when $\phi(0)\ne0$. Approximating $u$ by generated fields and using the displayed Lipschitz inequality shows both membership in the closure and agreement with the pointwise function.

For the gate operation, the one-sided estimate in the source is also correct:

\[
\begin{aligned}
\|u a(v)-\widetilde u a(\widetilde v)\|_2
\leq{}&\|a\|_\infty\|u-\widetilde u\|_2\\
&+R\operatorname{Lip}(a)\|v-\widetilde v\|_2
+2\|a\|_\infty\|\widetilde u\mathbf1_{|\widetilde u|>R}\|_2 .
\end{aligned}
\]

When $(\widetilde u,\widetilde v)$ is a fixed target pair, its square tail tends to zero by integrability. The prescribed order, taking the sequence limit first at fixed $R$ and then increasing $R$, proves joint $L^2$ continuity. It asserts neither a global Lipschitz bound nor closure under products of arbitrary unbounded $L^2$ functions.

The density claim also passes. Here is a precise completion of its cylinder-set step:

1. Integer clipping levels use included rational piecewise-linear maps.
2. Finite products of clipped fields are generated using bounded Lipschitz gates that agree with the identity on the relevant bounded interval.
3. Polynomial approximations to continuous functions on compact cubes converge uniformly. Their real coefficients belong to the real linear span after completion.
4. For each of the countably many generated fields, choose a countable dense set of interval endpoints outside its atoms. These endpoints need not be rational. Piecewise-linear approximations with rational knots can approach them from either side. The boundary-strip probabilities tend to zero, so finite-coordinate rectangle indicators belong to the closed span.
5. These rectangles form a generating $\pi$-system. The collection of events whose indicators belong to the closed span is a Dynkin system: it contains the whole space, is closed under complements, and is closed under disjoint countable unions because the partial indicator sums converge in $L^2$. The $\pi$–$\lambda$ argument gives every event in the generated sigma-field. Simple-function approximation then gives its whole $L^2$ space.

This does not require nonatomic field laws. Choosing non-atom endpoints is compatible with rational piecewise-linear generating functions through the approximation in step 4.

Therefore the closed generated space is exactly $L^2$ of the sigma-field generated by its scalar fields, rather than merely an abstract Hilbert subspace lacking its pointwise operations. It need not be the whole ambient Gaussian $L^2$ space if some Gaussian coordinates never become observable through generated fields.

## 6. Exact membership of finite neural Euler computations

The normalization of the displayed Hilbert equations is correct. In finite width with inner product $\langle u,v\rangle_n=u^\top v/n$, the rank-one operator

\[
(u\otimes v)z=u\langle v,z\rangle_n
\]

has Euclidean matrix $uv^\top/n$. Thus the physical hidden update
$2c\,\delta h^\top/(mn)$ is exactly the operator update
$2c\,\delta\otimes h/m$. No factor of $n$ is missing when the normalization is absorbed into the probability inner product.

For a fixed Euler history,

\[
B_\ell^k u
=\frac{2h}{m}\sum_{s<k,a\leq m}
c_a^s\,\delta_{\ell,a}^s\,
\langle h_{\ell-1,a}^s,u\rangle,
\]

and its adjoint acts by the corresponding backward inner products. These are finite scalar linear combinations and allowed pairings. First-layer updates use the fixed input pairings; the readout is a finite feature sum; and its prediction is an allowed inner product.

Every stage is algebraically well defined in the stated spaces:

* a bounded operator sends an $L^2$ activation field to $L^2$;
* a globally Lipschitz activation with a constant intercept preserves $L^2$;
* multiplication of a backward field by a bounded gate preserves $L^2$;
* predictions are finite by Cauchy–Schwarz;
* a finite sum of rank-one increments is Hilbert–Schmidt, with each norm equal to the product of its two $L^2$ norms.

The first-layer operator has finite-dimensional domain, so its analogous finite-rank updates are also well defined. The initialization $B_\ell=0,w=0$ and the stated adjoint formulas agree with the finite neural program. The common realization consequently identifies each fixed finite Euler computation with its scalar limiting law, including multiple meshes declared in the generating family.

The vector field's asserted continuity in the product of the finite-dimensional-domain operator norm, hidden Hilbert–Schmidt norms and readout $L^2$ norm is justified by bounded operator evaluation, the Nemytskii continuity above, continuous inner products and continuity of the rank-one map. No ordinary local Lipschitz estimate is inferred from the gate-continuity argument.

## 7. What this audit establishes

The candidate supplies a valid common, separable probability/Hilbert realization of compatible finite response laws, with forward operators of norm at most eight and their true adjoints. It supports comparisons among finite Euler programs in one state space. It does not need to assert pathwise convergence of the full finite-width matrices, reconstruct their entries, or presume an a priori continuous-time Gaussian process.

Its realization is infinite dimensional and is explicitly not the proposed final interpretable finite state. The source correctly distinguishes this existence/consistency tool from a transparent closure.

The subsequent continuum proposal needs independent premises and estimates: an admissible state domain, carrier/tail control there, the stated modulus, uniform numerical error or compactness/Cauchy estimates, and any passage to global time. None was provided to this audit. The source's final paragraph treats these as future work, so the present PASS does not certify them.

Recommended clarifications are confined to the instruction-library presentation: finite piecewise-linear descriptions, named immutable register dependencies for interleaving, rational linearity before completion, and the real-constant enlargement argument when needed. No change to the finite-Hilbert mathematical conclusion is otherwise required.

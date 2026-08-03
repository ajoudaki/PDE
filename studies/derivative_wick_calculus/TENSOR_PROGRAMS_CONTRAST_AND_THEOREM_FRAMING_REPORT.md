# Mean-Field Peeling, Tensor Programs, and the Sharp Theorem Claim

**Status:** Research-positioning report  
**Date:** 2026-08-03  
**Scope:** Contrast with Tensor Programs, defensible novelty framing, sharp target theorem, and naming recommendations  
**Epistemic status:** The literature comparison is an evidence-based assessment, not a certification of novelty. The proposed theorem below is a target statement and must not be presented as proved until its observable grammar, closure, termination, limit justification, and complexity bounds have been established.

## 1. Executive conclusion

Tensor Programs does not merely prove that a suitable infinite-width limit exists. It gives constructive recursive semantics for a finite tensor computation: coordinatewise operations are transported to limiting coordinate variables, normalized width averages become expectations, matrix multiplication introduces jointly Gaussian source variables with recursively computed covariances, and reuse of a matrix and its transpose produces an explicit Onsager correction.

Consequently, the following is not a defensible novelty claim for mean-field peeling:

> Tensor Programs only proves that the answer exists, whereas mean-field peeling is the first method that shows how to compute it recursively as Gaussian expectations.

Tensor Programs already shows how at the level of recursive limiting semantics.

The meaningful distinction is instead between two levels of construction:

1. **Recursive limiting semantics:** associate recursively defined limiting random variables and scalar expectations to a finite tensor computation.
2. **Explicit Gaussian normal form:** eliminate all wide random objects, recursive limit variables, unresolved Onsager terms, neuron-index sums, and hidden dependence corrections, leaving a finite directed acyclic graph of fully specified Gaussian integrals.

Mean-field peeling can constitute a distinct contribution if it proves a source-to-source compilation theorem of the second kind for a precisely defined class of contracted higher-derivative observables. Its potential contribution is therefore not a new infinite-width existence principle. It is an explicit derivative-observable elimination calculus, a Gaussian normal-form theorem, and possibly a finite-state depth recursion with controlled complexity.

The recommended paper title is:

> **Mean-Field Peeling: Explicit Gaussian Normal Forms for Feature-Learning Jets**

The recommended method name is **mean-field derivative peeling**, shortened in prose to **mean-field peeling**. The recommended theorem name is **Mean-Field Derivative Peeling Theorem**. The output representation should be called the **Gaussian normal form**, and the finite collection of local Taylor coefficients should be called the **feature-learning jet**.

## 2. Claim ladder

The relevant claims should be separated rather than blended into one headline.

- **Normalized wide-network averages can have deterministic infinite-width limits.** Established broadly in prior work; not the proposed novelty.
- **A finite tensor computation can be assigned recursive limiting coordinate semantics and moment expectations.** Established by Tensor Programs; not the proposed novelty.
- **Discrete-time feature-learning limits in $\mu$P can be represented and computed through Tensor Programs.** Established in substance by Tensor Programs IV; not the proposed novelty.
- **First- and higher-order derivative kernels admit recursive analyses.** Significant prior art exists; not by itself the proposed novelty.
- **Every observable in a specified contracted derivative grammar can be mechanically reduced to an explicit Gaussian-integral normal form.** Open target claim; plausible contribution.
- **The reduction terminates by eliminating one maximal layer group at a time.** Open general theorem; supported by worked examples only.
- **For fixed batch size, derivative order, training-step count, and observable schema, the normal form closes on finitely many state types independent of width and depth.** Open and decisive claim.
- **After common-state sharing, the number of recursion nodes is at most a fixed constant times depth.** Open and potentially important algorithmic contribution.
- **Every Gaussian atom is exactly $B$-dimensional for a batch of size $B$.** Not currently established; should not be claimed without a factorization theorem.
- **Fixed Taylor coefficients determine positive-time feature-learning dynamics.** False without a separate convergence or analyticity theorem; outside the peeling theorem.

## 3. What “computable recursively” means in Tensor Programs

Tensor Programs supplies mathematically specified operational rules. In simplified notation, if a coordinatewise operation creates

$$
x_i=\phi(y_i^1,\ldots,y_i^k),
$$

then its limiting coordinate variable is defined recursively by

$$
Z^x=\phi(Z^{y^1},\ldots,Z^{y^k}).
$$

If a scalar is a normalized width average,

$$
q_n=\frac1n\sum_{i=1}^n
\psi(x_i^1,\ldots,x_i^k),
$$

then its limiting scalar is defined by

$$
q_n\longrightarrow
\mathbb E\left[\psi(Z^{x^1},\ldots,Z^{x^k})\right].
$$

For a Gaussian matrix $W$ reused in a computation, Tensor Programs decomposes the limiting coordinate of $Wx$ into a fresh Gaussian component and an Onsager component,

$$
Z^{Wx}=\widehat Z^{Wx}+\dot Z^{Wx}.
$$

The fresh components associated with the same matrix are jointly Gaussian, with covariance of the schematic form

$$
\operatorname{Cov}
\left(\widehat Z^{Wx},\widehat Z^{Wy}\right)
=
\sigma_W^2\,\mathbb E[Z^xZ^y].
$$

When $W^\top$ has occurred earlier in the program, the correction is defined through expected symbolic derivatives. Schematically,

$$
\dot Z^{Wx}
=
\sigma_W^2
\sum_a
Z^{y_a}
\mathbb E\left[
\frac{\partial Z^x}
{\partial \widehat Z^{W^\top y_a}}
\right].
$$

This is a constructive Stein/Onsager rule. It is not an assertion that an unspecified correction exists.

Algorithm 1 in the Tensor Programs IV supplement instructs the reader to write training and inference as a Tensor Program and recursively compute the limiting coordinate variable associated with every vector and the limiting value associated with every scalar. The same supplement explicitly discusses the symbolic unwinding needed to calculate the Onsager term and notes that the calculation can grow rapidly in complexity.

Thus Tensor Programs occupies the following level of explicitness:

> Given an admissible finite program, recursive rules define its limiting coordinate law and all scalar moments in that program.

This is stronger than an existence theorem.

## 4. What remains implicit or unnormalized in Tensor Programs

Although the semantics is constructive, several nontrivial compilation tasks can remain.

### 4.1 The derivative observable must first be represented

Tensor Programs begins with a straight-line computation involving vectors, matrices, scalars, coordinatewise functions, and moments. A mathematical expression containing an arbitrary contracted Hessian or higher parameter derivative is not automatically a Tensor Program input.

One must first:

- differentiate or expand the network computation;
- encode every derivative contraction in the permitted program language;
- determine the required width normalization;
- verify that the resulting computation satisfies the hypotheses of the Master Theorem.

Closure of a general higher-derivative observable grammar under this compilation is not itself the generic Tensor Programs theorem.

### 4.2 Limiting coordinate variables may remain recursively named

An answer of the form

$$
\mathbb E[\Psi(Z^1,\ldots,Z^m)]
$$

need not yet be a Gaussian normal form. The variables $Z^1,\ldots,Z^m$ can be nonlinear functions of earlier Gaussian sources and Onsager terms. To obtain an ordinary Gaussian integral, one must unwind them as

$$
(Z^1,\ldots,Z^m)=F(G),
\qquad
G\sim N(0,\Sigma),
$$

and then write

$$
\mathbb E[\Psi(Z^1,\ldots,Z^m)]
=
\int \Psi(F(g))\,N(0,\Sigma)(dg).
$$

This unrolling is possible for a fixed finite program in the denotational sense, but Tensor Programs generally permits the recursive $Z$ representation to remain as the answer.

### 4.3 The symbolic Onsager calculation can be burdensome

The correction $\dot Z^{Wx}$ requires expressing $Z^x$ in terms of the underlying Gaussian source variables, differentiating that expression, and taking another expectation. The Tensor Programs IV supplement explicitly notes that this calculation can balloon quickly and that the general terms have no easy expression.

This is not a defect in mathematical definition. It is the distinction between a well-defined recursive interpreter and a compact, normalized symbolic output.

### 4.4 “Finite-dimensional” is not automatically “batch-dimensional”

For Tensor Programs, a fixed finite computation introduces finitely many Gaussian source variables. Their number can nevertheless grow with depth, training time, number of forward and backward passes, or derivative order.

Therefore the statement

> the answer is a finite-dimensional Gaussian expectation

does not by itself imply that every integral is over only one $B$-dimensional preactivation vector, nor that the dimension is uniformly bounded in depth.

## 5. Intended contribution of mean-field peeling

Mean-field peeling starts from a different input and demands a more normalized output.

### 5.1 Input

The proposed input is a scalar contracted derivative observable constructed from network outputs, losses, hidden feature Grams, preactivations, activations, and a fixed number of parameter or training-trajectory derivatives.

### 5.2 Transformation

The proposed compiler performs, explicitly:

1. derivative expansion by chain and product rules;
2. recursive scalarization of the current maximal layer;
3. grouping by layer;
4. conditional Gaussian integration over the maximal-layer weights;
5. Stein expansion of every weight–preactivation dependence;
6. Wick contraction of the remaining Gaussian weights;
7. enumeration of neuron-index equality partitions;
8. width-power counting and removal of strictly subleading partitions;
9. replacement of surviving row averages by their deterministic mean-field Gaussian moments;
10. propagation of the resulting lower-layer boundary state to the next peel.

### 5.3 Output

The desired output is a finite directed acyclic graph containing only deterministic algebra and Gaussian atoms of the form

$$
\mathcal I_{\ell,F}
=
\int_{\mathbb R^d}
F(g)\,N(0,K^\ell)(dg),
$$

where all of the following are explicitly generated:

- the layer $\ell$;
- the covariance matrix $K^\ell$;
- the dimension $d$;
- the integrand $F$;
- every occurrence of $\phi,\phi',\ldots$;
- every deterministic coefficient;
- every surviving batch-index contraction and equality pattern.

The output should contain no random weights, neuron-index sums, implicit backward vectors, recursively named Tensor Program variables, or unevaluated Onsager terms.

On their common domain, the two calculations should agree. The intended relationship is

$$
\operatorname{Peel}(O)
=
\operatorname{UnrollTP}
\bigl(\operatorname{CompileDerivative}(O)\bigr).
$$

Mean-field peeling can therefore be viewed as a specialized normal-form compiler or layerwise variable-elimination calculus for derivative observables, not as a competing infinite-width semantics.

## 6. Recommended sharp theorem contract

The theorem should first be stated for fully connected MLPs with equal hidden width. Extensions to unequal widths, residual networks, convolutions, attention, normalization, or general Tensor Programs should be separate results.

### 6.1 Network and limit

Fix:

- a batch of $B$ input-label pairs;
- a depth $L$;
- a derivative order $r$;
- a fixed number of gradient steps when training updates are included;
- an MLP with hidden width $n$ and fully declared $\mu$P initialization and optimizer scaling;
- a scalar activation with sufficiently many polynomially bounded derivatives.

Take $n\to\infty$ with $B$, $L$, derivative order, training-step count, and the observable schema fixed. A complexity statement may subsequently compare the symbolic construction across values of $L$, but the probability limit itself is width first at every fixed depth.

### 6.2 Admissible derivative observables

An admissible derivative observable should be defined structurally. It is a scalar expression generated from:

- outputs and losses on the fixed batch;
- preactivations and activations;
- hidden-layer Gram entries;
- parameter derivatives of total order at most $r$;
- finite sums, products, and tensor contractions;

subject to:

1. all neuron and parameter indices are eventually contracted;
2. every width normalization is declared;
3. the local expression schema is independent of width;
4. depth dependence is generated by repeated layer-local templates;
5. the expression is width-balanced under the declared scaling.

The phrase “any observable having a mean-field limit” should not define the class, because that would make the theorem partly circular.

### 6.3 Target theorem

> **Target theorem: Mean-Field Derivative Peeling.**  
> For every admissible scalar derivative observable $O_n$, there is a deterministic syntactic transformation $\operatorname{Peel}$ that recursively eliminates the maximal remaining layer group. Each peel replaces that group by a finite sum of deterministic Gaussian-integral coefficients multiplying admissible lower-group states. The transformation terminates after at most $L$ layer eliminations and emits a finite Gaussian normal-form DAG. Under the stated regularity and uniform-integrability hypotheses,
> $$
> \lim_{n\to\infty}
> \mathbb E_{\theta_0}[O_n]
> =
> \operatorname{Eval}
> \bigl(\operatorname{Peel}(O_n)\bigr).
> $$
> Every integrand, covariance, coefficient, index partition, and activation derivative in the output is effectively constructed from the network specification, fixed data, and observable syntax.

This is the conservative core claim. It asserts a finite explicit construction but does not yet assert that its size is linear in depth.

### 6.4 Finite-state strengthening

The strongest useful extension is:

> For every fixed batch size, derivative order, training-step count, and observable schema, the lower-layer boundary signatures produced by peeling close on a finite set of state types. After identical states are shared, the normal-form DAG has at most
> $$
> C_{B,r,O}\,L
> $$
> nodes, and every Gaussian atom has dimension at most
> $$
> d_{B,r,O},
> $$
> where the effective constants are independent of width and depth.

The constants may grow combinatorially or exponentially with derivative order and training-step count. No polynomial dependence should be claimed without a separate analysis.

This finite-state statement is the sharpest contrast with generic Tensor Program unrolling, but it is also the most important open proof obligation. Until it is proved, the safe statement is “at most $L$ elimination stages,” not “an $O(L)$-size formula.”

### 6.5 Possible batch-dimensional strengthening

A still stronger corollary would assert that every connected Gaussian atom can be reduced to one $B$-dimensional layer-preactivation integral, so that all multiple-row contributions factor into products of such atoms.

That statement may be true for the intended initialization derivative grammar, but it requires a factorization theorem for the equality partitions created by Wick and Stein expansions. The current program should use the safe bound $d_{B,r,O}$ until this is proved.

## 7. Feature-learning-jet corollary

Consider full-batch gradient descent with canonical $\mu$P scaling and master learning rate $\eta$. Fix a number $s$ of gradient steps and a Taylor order $p$.

For sample $a$, let $\mathcal L_a^{(s)}(\eta)$ be its loss after $s$ steps. For layer $\ell$, define the hidden feature Gram

$$
G_{ab}^{\ell,(s)}(\eta)
=
\frac1n
\left\langle
h_a^{\ell,(s)}(\eta),
h_b^{\ell,(s)}(\eta)
\right\rangle.
$$

For each $k\leq p$, the coefficients

$$
[\eta^k]\,
\mathbb E\left[\mathcal L_a^{(s)}(\eta)\right]
$$

and

$$
[\eta^k]\,
\mathbb E\left[G_{ab}^{\ell,(s)}(\eta)\right]
$$

are initialization derivative observables of fixed order. Once their admissibility is proved, the peeling theorem gives explicit Gaussian normal forms for them.

The finite collection of coefficients through order $p$ is the **order-$p$ feature-learning jet**.

This corollary makes a precise claim about every fixed coefficient. It does not imply convergence of the Taylor series, a positive radius of convergence, or correctness of a truncated series at a fixed nonzero learning rate.

## 8. Required nonclaims

The theorem and abstract should state explicitly that the work does not prove:

- convergence of the learning-rate or time Taylor series;
- complete positive-time training dynamics;
- arbitrary or width-dependent training times;
- a uniform-in-depth probability limit;
- elementary closed forms for general activation functions;
- polynomial complexity in derivative order or training-step count;
- self-averaging of every admissible observable;
- general architectural universality;
- exactly $B$-dimensional integration without the additional factorization proof.

Expectation-level exactness and sample-level determinism must remain separate claims. A variance or concentration theorem is required to pass from the former to the latter.

## 9. Reviewer-safe contrast with Tensor Programs

The recommended contrast is:

- **Input.** Tensor Programs takes a straight-line tensor computation; mean-field derivative peeling takes a contracted derivative observable.
- **Output semantics.** Tensor Programs gives recursive limiting coordinate semantics; peeling gives a completely eliminated Gaussian-integral normal form.
- **Intermediate randomness.** Tensor Programs introduces recursively defined $Z$ variables; peeling removes all random intermediate variables from the final representation.
- **Onsager correction.** Tensor Programs defines it through expected symbolic derivatives; peeling executes the Stein branches explicitly during layer elimination.
- **Dimension claim.** In Tensor Programs, “finite-dimensional” means finite for a fixed finite program; peeling seeks a bound depending only on fixed batch/order/schema data.
- **Compression claim.** Generic Tensor Program unrolling does not promise a compact normal form; peeling seeks finite-state closure and a depth-linear shared DAG.

The recommended prose statement is:

> Tensor Programs supplies general recursive limiting semantics for finite neural computations. Mean-field derivative peeling is a normal-form compiler for contracted derivative observables: it eliminates the wide random computation one layer at a time and emits a finite DAG of explicitly specified Gaussian integrals.

The work should not claim that Tensor Programs is nonconstructive. The distinction is between a recursive semantic representation and a normalized symbolic elimination theorem.

## 10. Naming and branding recommendations

### 10.1 Recommended vocabulary

- **Method:** mean-field derivative peeling
- **Short method name:** mean-field peeling
- **Main theorem:** Mean-Field Derivative Peeling Theorem
- **Output representation:** Gaussian normal form
- **Finite local Taylor data:** feature-learning jet
- **Algorithmic structure:** peeling-state DAG or peeling dynamic program

The acronym **MFP** should be avoided because it is already naturally read as “mean-field parameterization.” If an acronym is needed, **MFDP** is less ambiguous, but the full phrase is preferable in exposition.

### 10.2 Recommended paper title

> **Mean-Field Peeling: Explicit Gaussian Normal Forms for Feature-Learning Jets**

This is the preferred title because it combines:

- the memorable method name;
- the concrete output claim;
- the local, fixed-order nature of the feature-learning application.

### 10.3 Alternative titles

1. **Mean-Field Derivative Peeling: An Explicit Gaussian Calculus for Local Feature Learning**
2. **Peeling Wide Neural Networks: Explicit Gaussian Recursions for Feature-Learning Derivatives**
3. **From Derivatives to Gaussian Integrals: Mean-Field Peeling in Feature-Learning Networks**
4. **Feature-Learning Jets at Infinite Width: A Mean-Field Peeling Calculus**

If “jet” is considered too unfamiliar for the target venue, the safest replacement is “Taylor coefficients”:

> **Mean-Field Peeling: Explicit Gaussian Normal Forms for Feature-Learning Taylor Coefficients**

### 10.4 Alternative theorem names

1. **Mean-Field Derivative Peeling Theorem** — recommended canonical name.
2. **Gaussian Normal-Form Peeling Theorem** — best descriptive name for the output result.
3. **Layerwise Gaussian Elimination Theorem for Derivative Observables** — precise but less memorable.
4. **Feature-Learning Jet Representation Theorem** — best reserved for the training corollary, not the core initialization calculus.

## 11. Recommended paper framing

The paper should be framed as a constructive refinement and specialization, not as a replacement for Tensor Programs.

A reviewer-resistant abstract-level framing is:

> Existing infinite-width frameworks provide recursive limiting semantics for broad classes of neural computations. We study a narrower but algebraically difficult class: scalar contractions involving fixed-order derivatives of deep mean-field networks. We introduce mean-field derivative peeling, a layerwise conditional Gaussian elimination calculus that compiles such observables into explicit Gaussian normal forms. The procedure executes all Stein corrections, Wick contractions, equality-partition bookkeeping, and width power counting, leaving no wide random objects or implicit limit variables. For fixed batch size and derivative order, we identify the finite peeling states required by local feature-learning coefficients and derive explicit recursions for their Gaussian-integral representations.

The final sentence should only claim finite-state or depth-linear recursions after those properties have been proved.

## 12. Decisive proof obligations

The highest-leverage unresolved obligations are:

1. **Observable grammar:** define the admissible contracted derivative language without referring circularly to the existence of its limit.
2. **Derivative closure:** prove that chain/product-rule expansion and every peel remain inside a finite extension of that language.
3. **Stein termination:** prove that repeated dependence removal terminates and produces only the declared activation derivatives and lower-group states.
4. **Equality-partition completeness:** prove that all leading neuron-index patterns are enumerated and no apparently subleading pattern can regain order through a lower-layer contraction.
5. **Mean-field replacement:** justify every empirical-average-to-expectation step with the required conditional law of large numbers, uniform integrability, or concentration estimate.
6. **Finite-state closure:** classify the lower-layer boundary signatures at fixed derivative order.
7. **Complexity:** prove the shared-DAG bound and state exactly how its constant depends on derivative order, batch size, training steps, and observable schema.
8. **Gaussian dimension:** determine whether the safe finite bound can be strengthened to one $B$-dimensional atom per connected row component.
9. **Tensor Programs equivalence:** on the overlap class, prove that peeling evaluates to the same limit as the Tensor Program semantics. This converts a possible reviewer objection into a validation theorem.

The single most decisive next step is the finite-state closure theorem. Without it, peeling is an explicit layerwise elimination recipe but not yet the claimed $O(L)$ dynamic program. With it, the method has a precise and substantial distinction from generic symbolic unrolling.

## 13. Primary literature anchors

- Greg Yang and Edward J. Hu, [Tensor Programs IV: Feature Learning in Infinite-Width Neural Networks](https://proceedings.mlr.press/v139/yang21c.html), ICML 2021.
- Greg Yang and Edward J. Hu, [Tensor Programs IV supplementary material](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf), especially Definition G.3, the Master Theorem, Algorithm 1, and the discussion of computational complexity.
- Greg Yang, [Tensor Programs II: Neural Tangent Kernel for Any Architecture](https://arxiv.org/abs/2006.14548), 2020.
- Greg Yang, [Tensor Programs III: Neural Matrix Laws](https://arxiv.org/abs/2009.10685), 2020.
- Jiaoyang Huang and Horng-Tzer Yau, [Dynamics of Deep Neural Networks and Neural Tangent Hierarchy](https://proceedings.mlr.press/v119/huang20l.html), ICML 2020.
- Ethan Dyer and Guy Gur-Ari, [Asymptotics of Wide Networks from Feynman Diagrams](https://arxiv.org/abs/1909.11304), 2019.
- Max Guillen, Philipp Misof, and Jan E. Gerken, [Finite-Width Neural Tangent Kernels from Feynman Diagrams](https://arxiv.org/abs/2508.11522), ICML 2026.

## 14. Current authoritative positioning statement

The strongest defensible current statement is:

> Mean-field peeling is a proposed explicit normal-form calculus for fixed-order contracted derivative observables in wide mean-field MLPs. Tensor Programs already supplies constructive recursive semantics for broad finite neural computations, including $\mu$P feature-learning limits. The prospective distinction is that peeling begins from derivative syntax and performs all layerwise Gaussian elimination, Stein correction, Wick contraction, equality-pattern enumeration, and width power counting explicitly, with the goal of producing a finite Gaussian-integral DAG and a finite-state depth recursion. The existence of this normal form is an open target theorem; the depth-linear finite-state strengthening remains the decisive unproved claim.

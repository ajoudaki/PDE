# The closest new compression claim: Wang et al., ICLR 2026

## Source and reading coverage

[A universal compression theory for lottery ticket hypothesis and neural scaling laws](https://proceedings.iclr.cc/paper_files/paper/2026/hash/bc71544dfef150412977e59d221b6597-Abstract-Conference.html), Hong-Yi Wang, Di Luo, Tomaso Poggio, Isaac L. Chuang, and Liu Ziyin.

Complete 26-page read, including Appendices A–H, of arXiv:2510.00504v2 (2 March 2026). Downloaded the [published proceedings PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/bc71544dfef150412977e59d221b6597-Paper-Conference.pdf) as well: extracted texts differ only on the first page's layout/arXiv stamp. Main theorem and appendix passages are identical. Rendered p. 18 inspected to verify the printed inequality below. Public code is linked by the source, but was not executed or scientifically audited.

This is a direct novelty comparator, not ordinary snapshot pruning. Its abstract and §5 explicitly claim polylogarithmic width while preserving learning dynamics. It must be cited and discussed even though important qualifications and proof problems remain.

## What the construction does

The source's \(d\) counts objects and its \(m\) is the dimension of one object; neither is our paper's corresponding symbol. Here use words for these quantities.

1. A permutation-invariant observable is represented as \(h(\sum_i g(w_i))\). Assumption 1 requires both functions to be independent of the number of objects and analytic. Each object lies in a bounded, fixed-dimensional region.
2. Tchakaloff/Carathéodory moment matching replaces many objects by positively weighted selected objects. Moments through a chosen degree agree.
3. Analyticity converts increasing moment order into a claimed exponentially decreasing local error. Theorem 7 claims a retained support proportional to a power of the logarithm of original size divided by target error. The exponent is the dimension of one object, fixed in that theorem's asymptotics.
4. A prediction after training is a symmetric function of the initialization because training is permutation equivariant. Theorem 5 applies the approximation theorem to this composed function, **assuming it too satisfies Assumption 1**.
5. The practical compressed optimizer divides a retained object's gradient by its multiplicity weight (Appendix C). Thus it is not simply the original optimizer applied to a naively pruned ordinary network. Absorbing weights into output coefficients reproduces the forward function but does not, by itself, establish equality of optimization metrics.

This is a genuinely related analytic-moment mechanism. It is closer to our selected-source compression than an endpoint lottery ticket theorem.

## Decisive scope distinctions, independent of any proof criticism

- **Depth is explicitly unresolved.** Section 5, p. 8, states that extension to deep networks requires scrutiny and leaves the compressed-width scaling open. Treating a neuron as an incoming row/outgoing column gives an object whose dimension grows with neighboring hidden widths. Therefore a fixed-object-dimension logarithmic power cannot be substituted unchanged into an all-wide multilayer network. This is exactly why compressing a quadratic hidden interaction is a meaningful additional problem.
- **Dynamical regularity is assumed.** The same page says the authors do not know whether the trained observable retains Assumption 1 even when the initial observable has it. Their expectation concerns analytic maps and a finite number of steps. Analyticity at each fixed time is not a uniform-in-time analytic radius or stability bound.
- **The displayed dynamical theorem is for a specified map \(T\).** It does not exhibit one width-uniform approximation estimate over all training times and the fitted limit, with the constants needed for that union.
- **No actual dense–dense benchmark is certified.** The target is a chosen absolute observable error. No nondegenerate independent-seed discrepancy and no ratio to it are analyzed.
- **Initialization is bounded-object rather than the present full Gaussian model.** A Gaussian adaptation requires tracking a growing high-probability radius and its effect on constants; it is not automatic from the stated theorem.
- **Efficient implementation is narrower than the optimal theorem.** Appendix D says the strongest error bounds are for greedy smallest-cluster selection. Experiments use a hybrid \(k\)-means/approximate-neighbor implementation for which the same bound is not proved. The optimal increasing moment order is explicitly expensive.

These qualifications alone establish that the paper does not supply the combined guarantee of the present manuscript. They remain valid if its mathematical gaps are repaired.

## What the experiments actually establish

All descriptions here concern reported experiments, not reproduced runs.

- Figure 4: a **one-hidden-layer** ReLU MLP of width 10,000 reduced to 1,000, moment order five, a two-dimensional oscillatory regression task, several optimizers, and common minibatch sequences.
- Figures 4 and 7 plot train/test **MSE against target labels**, not RMS disagreement between dense and compressed prediction vectors. Matching MSE curves alone does not imply matching predictions.
- Appendix F adds a single-layer multi-head attention experiment, 4,000 to 800 heads, fixed per-head dimension, moment order three, 250 Adam updates. This is a meaningful additional architecture but not an all-wide deep MLP result.
- Appendix G does empirically test logarithmic and squared-logarithmic retained supports in dimensions one and two. Its observable is a **static symmetric rational function**, not a trained deep-network trajectory. It would be inaccurate to say the paper never tests polylogarithmic compression; it would also be inaccurate to attribute that experiment to its dynamical claim.

## Mathematical findings

### Confirmed counterexample to the width-uniform local upper bound

A subsequent fresh isolated full-text check found a stronger obstruction than the missing-derivative argument below. For a one-dimensional cluster, set moment order one, so Theorem 3 permits at most two retained points. Take equal numbers of the three values \(-a,0,a\), with \(a>0\) fixed. The symmetric analytic observable

\[
\det\!\left(\sum_i
 \begin{pmatrix}1\\w_i\\w_i^2\end{pmatrix}
 \begin{pmatrix}1&w_i&w_i^2\end{pmatrix}\right)
\]

is proportional to the **cube** of the number of objects. Every weighted two-point approximation has determinant zero by rank, for any chosen weights or locations. Its error therefore cannot obey the theorem's bound proportional to the number of objects times the squared diameter. Both maps in the required deep-set representation are fixed polynomials. The source explicitly treats polynomials as admissible; a rational variant also handles a strict finite-complex-radius reading.

The complete calculation and exact coefficient are in [UNIVERSAL_FRESH_CHECK.md](UNIVERSAL_FRESH_CHECK.md). This disproves Theorem 3's intended width-uniform bound and breaks that step in the supplied proofs of Theorems 4, 7 and 5. It does **not** itself disprove eventual polylogarithmic support, since this example is represented exactly with three points. The distinction between an invalid supplied proof and an impossible final rate is essential.

### Verified false lemma in the optimality lower-bound proof

Appendix B, Lemma 2, eq. (57), claims that for a degree-at-most-\(k\) polynomial normalized to have supremum one on a convex compact set \(D\),

\[
\frac{|\{x\in D:|p(x)|\ge t\}|}{|D|}
\ge 1-(t/2)^{1/k}.
\]

Set \(D=[0,1]\), \(p(x)=x\), \(k=1\), and \(t=1/2\). The left side equals \(1/2\), whereas the asserted lower bound is \(3/4\). Every stated hypothesis holds. This is a counterexample to the printed lemma, not an OCR interpretation.

The proof's eq. (63) substitutes a **lower** bound for a right-hand side that was already at least one; that substitution does not preserve the inequality. Theorem 8 then uses Lemma 2 in eq. (67), so the supplied optimality proof is not valid as written. A corrected Remez argument may yield a useful weaker estimate; this audit does not claim the optimality conclusion is impossible.

A separate step at eq. (67) claims that bounded Voronoi-cell volume forces the number of sample points in a measurable region to be bounded below by a constant times its volume. That is false for arbitrary regions: remove the finite point set from \(D\), retaining full volume but no sample points. For the particular polynomial superlevel sets one would need additional sampling/mesh-resolution reasoning; the displayed argument does not provide it.

The fresh check strengthens this observation to exactly the required type of region: equally spaced points on the horizontal midline of a square have Voronoi cells of area reciprocal to sample count, yet a linear polynomial vanishing on that line has a positive-area superlevel set containing no sample points. Thus the stated quasi-uniformity condition is insufficient even for low-degree polynomial superlevel sets.

### Missing uniform control in the upper-bound proof

Appendix A.3, eq. (34), concludes that the coefficient is \(O(\text{number of objects})\) because \(h\) and \(g\) do not themselves depend on that number. But the argument at which \(h'\) is evaluated is a sum over all objects and grows with their number. Function independence does not imply a uniform derivative bound on that expanding range.

For example, even the fixed analytic function \(h(y)=y^2\) has \(h'(y)=2y\). Evaluating at \(y\) proportional to object count introduces an additional growing factor. The paper itself admits polynomials as analytic examples; an insistence on finite rather than infinite Taylor radius can equally use \(h(y)=y^2+(1+y^2)^{-1}\). This is a gap in the stated justification, not by itself a counterexample to every possible compression of such an observable. The needed condition is uniform control of the composed observable on the relevant domain, not merely independence of its formula from width.

Appendix A.6 also turns an analytic convergence radius into a uniform coefficient majorant while changing expansion centers and degree. Such a majorant needs an appropriate smaller complex neighborhood and a bound there. This is another reason not to read the advertised universal theorem as a black-box uniform all-time neural-network theorem.

### Further issue not used as a settled criticism

Appendix C extends moment representations from unweighted finite configurations to weighted ones and treats that extension as unique and compatible with composed dynamics. Polynomial relations between moments can make off-configuration extensions nonunique. A careful reconstruction would need to specify the extension and prove its composition property. This audit records that obligation but does **not** claim a completed counterexample to their natural weighted SGD construction.

## Recommended use in our paper

Credit prior polylogarithmic analytic-moment compression and initialization-based dynamical compression. Then distinguish the proved handling of deep quadratic interactions, nonlinear stability through convergence, the coupled ordinary dense reference, and the benchmark against actual seed variability.

Do not write “we are the first to compress learning dynamics polylogarithmically.” A safer statement is that existing analytic-moment compression does not establish the present **deep, seed-coupled, complete-trajectory** guarantee. Local proof findings belong in an internal review or a restrained technical note, not a rhetorical attack in the introduction.

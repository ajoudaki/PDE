# Bounded review: first raw metric and controlled kernel

## Scope and verdict

This is an isolated audit of `FIRST_RAW_METRIC_AND_CONTROLLED_KERNEL_COMPACTNESS.md`, read completely (122 lines). The only additional material read was the procedural rigorous-math skill. No other mathematical document, history, experiment, or agent was used. The source was not edited. This review concerns the stated conditional lemma, not any global convergence or proof program.

**Verdict:** the three principal conditional conclusions are correct under the explicit joint-law Wasserstein premise, the exact raw update rule, and the stated antiparallel invariance where applicable. These conclusions are:

1. Quadratic-Wasserstein convergence of the joint laws of raw first-row increments and velocities in the indicated continuous-path/product-L2 topology.
2. Convergence of the first raw kinetic energy with exactly the factor `d/n` and no defect.
3. Strong time-L1 convergence of every entry of the residual-weighted two-by-two kernel, including the off-diagonal entries.

No unweighted reverse-field moment is needed for these conclusions. No actual joint-law convergence, population equation, or GD/GF comparison is proved by them.

The main qualifications concern wording, rather than the coupling proof:

- Under the deterministic premise, the limiting measure and its kernel are deterministic. The statement that the limit “need not be deterministic” must be restricted to an explicitly random version, or clarified as referring to a non-Dirac particle law.
- Compact containment alone does not establish convergence in probability. It needs a further identification/uniqueness or approximation argument if it is to support such a conclusion.
- At the antiparallel endpoint, the ordinary row norm squared is `v^T C^+ v / d`. The displayed energy formulas correctly use the scaled quantity `d |dot W|^2`; the prose calling `v^T C^+ v` the “squared raw norm” should make that scaling explicit.
- The loss-dissipation sentence establishes algebraic consistency with the scaled speed. In particular, it is not an exact nonlinear loss identity for the affine GD interpolation.

The arguments and the precise scope of these qualifications follow.

## 1. Premise, notation, and what is being assumed

Interpret `rho = C_12 = C_21`, as intended by lines 9–10 and 26. Since both input squared norms are `d`,

\[
X^T X=dC,\qquad
C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}.
\]

The input pair, its dimension, and the finite interval `[0,T]` are fixed. Thus all maps used below are independent of width. The case `rho=1` is expressly outside the statement.

Let

\[
\mathcal E=C([0,T];\mathbb R^2)\times L^2([0,T];\mathbb R^2),
\]

with squared distance

\[
\operatorname{dist}_{\mathcal E}((z,v),(z',v'))^2
=\|z-z'\|_\infty^2+\|v-v'\|_2^2.
\]

The substantive compactness premise is convergence `mu_n -> mu` in `W_2( E )`, with `mu` a probability measure of finite second moment. For each width, the empirical measure is over whole trajectories of that width's neurons; the source does not assume a common labeling across widths.

The phrase “follows the exact … rule” is interpreted in its usual GF/GD sense: the trajectories satisfy the integral evolution equation and are absolutely continuous. Raw affine GD interpolation has this property. This is the trajectory regularity used when integrating the row velocity. Merely assigning an almost-everywhere derivative to an arbitrary continuous path would not by itself supply an integral evolution equation.

For `rho=-1`, the sample equalities in lines 35–39 are an explicit additional hypothesis. This review accepts those equalities as the stated exact invariance. The source does not define the full architecture from which one could independently prove them. Odd activation functions and labels by themselves would not establish the same equalities for an arbitrary architecture with, for example, biases. No such additional architectural conclusion is needed for the conditional lemma.

Write `(Z_n,V_n)` and `(Z,V)` for the coordinate pairs under a coupling `pi_n` of `mu_n` and `mu`. The W2 premise permits couplings for which

\[
\varepsilon_n^2
=\mathbb E_{\pi_n}\left[
\|Z_n-Z\|_\infty^2+\|V_n-V\|_2^2\right]\longrightarrow0.
\tag{R1}
\]

Approximate minimizing couplings suffice; no existence claim about an optimal coupling is needed.

In particular, with

\[
M_n^2=\mathbb E_{\mu_n}\|V\|_2^2,\qquad
M^2=\mathbb E_\mu\|V\|_2^2,
\]

the triangle inequality in the coupled L2 space gives

\[
M_n\le M+\varepsilon_n.
\tag{R2}
\]

This verifies the source's assertion that the uniform integrated second-moment bound is redundant under W2 convergence. It does not give a bound uniform in time.

## 2. Exact raw factors and first-row reconstruction

### 2.1 The nondegenerate input pair

For one row, temporarily suppress width, neuron, and time indices. The stipulated update is

\[
\dot W=\frac1d Xd_i,\qquad z=X^T W.
\]

Consequently,

\[
v=X^T\dot W=\frac1d X^TXd_i=Cd_i,
\]

and

\[
|\dot W|^2
=\frac1{d^2}d_i^TX^TXd_i
=\frac1d d_i^TCd_i.
\tag{R3}
\]

Thus equation (1) has the correct factor `d`. There is no extra sample factor or width factor in this individual-row identity.

For `-1<rho<1`, the eigenvalues of `C` are `1+rho` and `1-rho`, both positive. With `D=C^{-1}`,

\[
d_i=Dv,\qquad
\dot W=Av,\qquad
d|\dot W|^2=v^TDv,\qquad A=\frac1d XD.
\tag{R4}
\]

Every formula in (2) follows. Also,

\[
\|D\|_{\mathrm{op}}=\frac1{1-|\rho|},\qquad
A^TA=\frac1d DCD=\frac1d D.
\tag{R5}
\]

The bounded-map estimates are therefore valid for the fixed input pair, and generally are not uniform as the pair approaches a singular endpoint.

### 2.2 The antiparallel case

At `rho=-1`, normalized inputs satisfy `x_2=-x_1`. Here

\[
C=\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad
C^+=\frac14C,
\]

and `C` has eigenvalue `2` on `span{(1,-1)}` and eigenvalue `0` on `span{(1,1)}`. The stated invariance supplies equal deltas and opposite controls, hence

\[
d_i=(b,-b),\qquad v=Cd_i=(2b,-2b),\qquad C^+v=d_i.
\]

The actual row velocity and the energy are

\[
\dot W=\frac{2b}{d}x_1=\frac1d XC^+v,
\]

\[
|\dot W|^2=\frac{4b^2}{d},\qquad
d|\dot W|^2=4b^2=v^TC^+v=\frac{|v|^2}{2}.
\tag{R6}
\]

This verifies the factor and rules out an erroneous doubling of the first-row energy. In particular, `|v|^2` itself would be twice the scaled row energy in this case.

The sentence at lines 41–42 should explicitly say “its squared row norm multiplied by d.” Since the source also says all norms are ordinary, the unscaled row norm cannot literally equal `v^T C^+ v` unless `d=1`. Equation (2), equation (3), and the surrounding reconstruction are correctly normalized.

The invariance is essential for identifying `d_i` from `v`, and therefore for identifying the entire controlled kernel. To see exactly where it enters, omit that invariance and write

\[
d_i=(b,-b)+h(1,1).
\]

Then `v=(2b,-2b)` and the raw row velocity are independent of `h`, but

\[
C\odot(d_i d_i^T)
=\begin{pmatrix}
(b+h)^2&b^2-h^2\\
b^2-h^2&(h-b)^2
\end{pmatrix},
\tag{R7}
\]

where `odot` denotes entrywise multiplication. Its entries depend on `h`. In particular, `d_i=(1,1)` gives zero velocity but a nonzero controlled-kernel matrix equal to `C`.

This is not a counterexample to the draft: its antiparallel hypothesis forces `h=0`. It shows why silently dropping that hypothesis would invalidate (5), even though row reconstruction and the scalar energy could still be recovered using the pseudoinverse.

### 2.3 Increments, full rows, and the limit derivative

In both admitted cases, `dot W=Av` and `v=dot z` in the integral sense. Hence

\[
W(t)-W(0)=A[z(t)-z(0)].
\tag{R8}
\]

For two trajectory pairs,

\[
\|A[(z-z(0))-(z'-z'(0))]\|_\infty
\le 2\|A\|_{\mathrm{op}}\|z-z'\|_\infty,
\]

\[
\|A(v-v')\|_2\le\|A\|_{\mathrm{op}}\|v-v'\|_2.
\]

The pushforward map in line 60 is therefore Lipschitz with constant at most `2 ||A||_op` for the product metric. Pushing forward the couplings in (R1) proves W2 convergence of the asserted joint laws, not merely weak convergence.

This reconstructs labeled trajectories within each width before passing to laws; the couplings need not preserve neuron indices across widths.

Let `P=XD X^T/d`. In both cases, `P` is the orthogonal projection onto the input span: it is symmetric, has that range, and `P^2=P` by `DCD=D`. Thus

\[
W(t)=Az(t)+q,\qquad q=(I-P)W(0),
\tag{R9}
\]

with `q` constant in time. To reconstruct full row laws, one must add this initial perpendicular component jointly with `(z,v)` and assume the corresponding convergence; its separate marginal distribution is not enough to preserve correlations. The source already correctly requests its inclusion in the joint law.

The derivative relation also survives the limit. Define

\[
F(z,v)(t)=z(t)-z(0)-\int_0^t v(s)\,ds.
\]

Then

\[
\|F(z,v)-F(z',v')\|_\infty
\le 2\|z-z'\|_\infty+\sqrt T\|v-v'\|_2.
\]

Since `F(Z_n,V_n)=0`, (R1) implies `E_mu ||F(Z,V)||_infty^2=0`. Thus `Z` is absolutely continuous with derivative `V`, for `mu`-almost every pair. At the antiparallel endpoint, the relations `Z_1+Z_2=0` and `V_1+V_2=0` similarly survive, in C and L2 respectively. There is no hidden loss of the kinematic compatibility needed by reconstruction.

## 3. No defect in the raw first-matrix energy

Define the time-dependent scaled energy density

\[
q_n(t)=\frac d n\|\dot W_n^{(1)}(t)\|_F^2
=\mathbb E_{\mu_n}[V(t)^TDV(t)].
\tag{R10}
\]

This equality uses one sum over the `n` first-layer rows. There is no additional sum over samples beyond the quadratic form already present in (R3).

The candidate limit is the integrable density

\[
q(t)=\mathbb E_\mu[V(t)^TDV(t)].
\]

For the couplings in (R1), symmetry of `D` gives

\[
|u^TDu-w^TDw|
\le\|D\|_{\mathrm{op}}|u-w|(|u|+|w|).
\]

Taking the absolute value outside the coupled expectation, integrating, and applying Cauchy–Schwarz on time times coupling yields

\[
\|q_n-q\|_{L^1(0,T)}
\le\|D\|_{\mathrm{op}}\varepsilon_n(M_n+M)
\longrightarrow0.
\tag{R11}
\]

All factors on the right are justified by (R1)–(R2). The proof establishes the slightly stronger result of convergence of the energy densities in L1. Equation (3) follows by integration. For every measurable time set `B`,

\[
\left|\int_B q_n(t)\,dt-\int_B q(t)\,dt\right|
\le\|q_n-q\|_1.
\]

Thus the source's statement about every fixed measurable time subset is valid. In fact the bound is uniform over such subsets.

The W2 premise is doing more work than bounded second moments. For example, at `C=I`, the empirical laws

\[
\mu_n=(1-1/n)\delta_{(0,0)}
+(1/n)\delta_{(\sqrt n\,t e_1,\sqrt n\,e_1)}
\]

converge weakly to `delta_(0,0)` and have bounded integrated mean squared velocity, but their integrated scaled energy is always `T`, while that of the weak limit is zero. Their W2 distance to the zero law does not tend to zero. This exact example explains why the supplied W2 hypothesis cannot be replaced by a moment bound plus weak convergence. The draft does not make that replacement.

## 4. The full controlled two-by-two kernel

### 4.1 Identification and the L1 estimate

The controls in (4) have sample and time indices, but no neuron index. Therefore they can be brought inside the empirical sum, giving exactly

\[
J_{n,ab}(t)=C_{ab}\mathbb E_{\mu_n}[(DV(t))_a(DV(t))_b].
\tag{R12}
\]

Here `d_i=DV_i` holds because `C` is invertible, or because of the explicitly assumed antiparallel invariance. This is the indispensable identification step.

Put `E_n=DV_n` and `E=DV` in the couplings. For either diagonal or off-diagonal indices,

\[
E_{n,a}E_{n,b}-E_aE_b
=(E_{n,a}-E_a)E_{n,b}+E_a(E_{n,b}-E_b).
\]

Consequently,

\[
\begin{aligned}
\int_0^T\left|
\mathbb E[E_{n,a}E_{n,b}]-\mathbb E[E_aE_b]
\right|dt
&\le\|E_n-E\|_{L^2(dt\,d\pi_n)}
\bigl(\|E_n\|_{L^2(dt\,d\pi_n)}+\|E\|_{L^2(dt\,d\pi_n)}\bigr)\\
&\le\|D\|_{\mathrm{op}}^2\varepsilon_n(M_n+M).
\end{aligned}
\tag{R13}
\]

This verifies the displayed estimate at lines 97–100 with constant one as written there. Multiplication by `C_ab` introduces `|C_ab|<=1`, so each kernel entry converges in L1. For example, for the Frobenius matrix norm,

\[
\int_0^T\|J_n(t)-J(t)\|_F\,dt
\le\sum_{a,b=1}^2\|J_{n,ab}-J_{ab}\|_1
\longrightarrow0.
\tag{R14}
\]

Any other fixed norm on two-by-two matrices gives the same convergence. The proof genuinely identifies the full matrix, not just its trace, its sum of entries, or one residual quadratic form. It uses only the velocity marginal of the W2 premise; the position marginal is needed for the joint reconstruction statement.

No bound on the individual deltas, no control bounded away from zero, and no division by residuals is used. Integrability of the controlled products follows from `d_i=DV_i` and the velocity second moments.

### 4.2 Summation and endpoint factors

For finite width,

\[
\sum_{a,b}J_{n,ab}(t)
=\frac1n\sum_i d_{n,i}(t)^TCd_{n,i}(t)
=\frac d n\|\dot W_n^{(1)}(t)\|_F^2.
\tag{R15}
\]

For the limit, `DCD=D` is an identity on the whole two-dimensional space for either choice of `D`. Hence

\[
\sum_{a,b}J_{ab}(t)
=\mathbb E_\mu[V(t)^TDCDV(t)]
=\mathbb E_\mu[V(t)^TDV(t)]
\quad\text{for almost every }t.
\tag{R16}
\]

The expectation and the empirical averaging must be retained. Lines 104–105 are correct as shorthand for (R15)–(R16), but the limit sum is the expectation of `v^T D v`, not an unaveraged random value.

At the antiparallel endpoint, a single row with `d_i=(b,-b)` contributes

\[
C\odot(d_id_i^T)
=b^2\begin{pmatrix}1&1\\1&1\end{pmatrix}.
\]

The sum of its four entries is `4b^2`, exactly (R6). Equivalently, the limit matrix is

\[
J(t)=\frac14\mathbb E_\mu[V_1(t)^2]
\begin{pmatrix}1&1\\1&1\end{pmatrix},
\]

whose entry sum is `E[V_1^2]=E[|V|^2]/2`. The cross terms are required for this equality; using the trace instead of the sum of all entries would give the wrong factor.

Finally, `c=-2r` gives the exact algebraic equality

\[
\sum_{a,b}J_{n,ab}=c_n^TK_n^{(1)}c_n
=4r_n^TK_n^{(1)}r_n.
\tag{R17}
\]

The factor four is already present through the controls; it must not be inserted again into the raw speed formula.

## 5. Kernel arguments and time topology

### 5.1 What the limit kernel means

The claimed kernel has the two fixed sample indices `a,b` and one time argument. It is the controlled empirical product in (4). Formula (5) identifies an observable of the limiting velocity law. It does not identify an unweighted kernel, a kernel at arbitrary new inputs, or a function of the position law alone.

There is also no identification of a nonlinear population kernel or population force equation. The joint-law premise itself does not state that the limiting velocities are generated by any specified population dynamics. The source's disclaimer on that point is appropriate.

The controls can vanish without harming the argument. In that case the weighted product need not carry information about the corresponding unweighted delta products. Even on a region where controls are nonzero, a further claim of unweighted-kernel convergence would require assumptions sufficient to control and identify the divisions by the width-dependent controls. Such assumptions are absent, and the source makes no such positive claim.

### 5.2 Meaning of `V(t)` under an L2 path law

An L2 element is an equivalence class of functions, so evaluation at a prescribed time is not an intrinsic operation. The safe formulation of (5) is the L1-valued expectation

\[
J=\mathbb E_\mu\bigl[C\odot((DV)(DV)^T)\bigr].
\tag{R18}
\]

The mapping inside this expectation is continuous from L2 to matrix-valued L1 by the product estimate in (R13), and its L1 norm is bounded by a fixed constant times `||D||_op^2 ||V||_2^2`. It is therefore integrable. Formula (5) is a representative of (R18) for almost every time. The same interpretation applies to the energy density. Absolute integrability of the products justifies the time/expectation interchange.

This makes the source's claim at lines 102–103 sound: the proof does not use continuity of time evaluation on L2. It should consistently be read with an almost-everywhere time qualifier.

Neither pointwise convergence at a prescribed time nor uniform-in-time kernel convergence follows. For an exact topological illustration, take `C=I`, an interior time `t_*`, and

\[
V_n(t)=\max\{1-n|t-t_*|,0\}\,e_1,\qquad
Z_n(t)=\int_0^t V_n(s)\,ds.
\]

Then `||V_n||_2 -> 0` and `||Z_n||_infty -> 0`, so the Dirac joint laws converge in the required W2 metric. But `J_{n,11}(t_*)=1` for every `n`, while the limiting kernel is zero. These are even continuous velocity representatives. The stated L1 conclusion holds; a stronger pointwise conclusion does not follow from this topology alone.

### 5.3 GF and affine raw GD use different evaluations

For GF, the exact rule is evaluated at the current state. For raw GD interpolation, `V_n` and the stipulated `d_{n,i}` are generated by the node quantities held fixed on the cell. The source explicitly uses those same node quantities in (4). Thus the algebra `d_i=DV_i` and the proof of (R12) apply in both cases as stated. Cell boundaries form an irrelevant null set for these L2/L1 conclusions.

A recomputed nonlinear kernel at an interior interpolated parameter state is a different quantity. There is no estimate here comparing its deltas or residuals with the node values. Lines 88–89 and 118 correctly leave that difference uncontrolled. The terminology “NODE” should be read as referring to GD; GF has the current-time controlled kernel.

The sentence about loss dissipation at line 106 is valid as an algebraic consistency observation: the kernel entry sum equals the scaled first-block speed. To claim that this speed equals an actual contribution to `-dot L`, one must also specify the loss normalization and the relation between the deltas and its parameter derivatives. Those definitions are not supplied in this isolated note.

Moreover, even with a specified normalized gradient loss, an affine GD cell generally satisfies

\[
\frac{d}{dt}L(\theta(t))
=\nabla L(\theta(t))\cdot\dot\theta_{\mathrm{node}},
\]

which uses the current gradient paired with the frozen node velocity. The node quadratic form uses the node gradient. Their equality throughout the cell requires an additional argument and is not established here. Accordingly, this note proves no exact GD loss-decrement identity. This limitation is consistent with its explicit node/recomputed-kernel distinction.

## 6. Deterministic, subsequential, and probability scope

### 6.1 Deterministic convergence and compactness

The source begins with a deterministic sequence of empirical measures and assumes its W2 convergence. The resulting `mu`, pushforward measure, energy density, and controlled kernel are deterministic objects. A trajectory sampled from `mu` can be random, and `mu` can be non-Dirac, without making the measure or its expected kernel random.

If only W2 relative compactness is assumed, each W2-convergent subsequence has all the conditional consequences above with its own limit. The image laws are correspondingly W2 relatively compact, and the image kernels and energy densities are L1 relatively compact, because the proved maps are continuous. Different subsequences may have different limits. This is not full-sequence convergence and is not randomness of a deterministic limit.

The word “compactness” must retain the W2 topology in this statement. Relative compactness merely for weak convergence, even with a bounded second moment, is insufficient for the no-defect argument, as the example in Section 3 shows.

Thus lines 108–109 are correct with that topology. Line 110 needs the deterministic/random distinction clarified. A suitable replacement is:

> Under the deterministic premise each subsequential limiting measure and its kernel are deterministic, although the limiting particle law can be non-Dirac and different subsequences can give different limits. For explicitly random empirical measures, subsequential limits may themselves be random measures.

### 6.2 What would give convergence in probability

The proof establishes continuous maps from `P_2(E)` to the output W2 space and to matrix-valued L1. Consequently, if random measures satisfy the explicit premise

\[
W_2(\mu_n,\mu)\longrightarrow0\quad\text{in probability},
\tag{R19}
\]

on a specified probability space, then the corresponding outputs converge in probability in their stated metrics. The limit `mu` may then be a random measure. Formula (5) is interpreted for each realization as integration against that realization's measure; it is not automatically an expectation over all external randomness.

One can justify the probability implication directly. From every subsequence of a nonnegative metric error converging to zero in probability, select a further subsequence whose probabilities of errors exceeding `2^{-k}` are at most `2^{-k}`. The probability of any such violation after index `K` is at most the tail of this summable series, so the errors converge almost surely along that further subsequence. Deterministic continuity applies realization by realization. If the output did not converge in probability, a subsequence with a fixed positive probability of a fixed positive error would contradict this almost-sure further-subsequence conclusion. This requires (R19); it is not a probability conclusion from deterministic couplings alone.

The source is therefore right to reject an automatic new probability quantifier. Its phrase “or explicit compact-containment argument” at lines 112–113 is underspecified if intended to describe an alternative sufficient condition. Compact containment alone gives no convergence in probability or unique limit.

For a precise counterexample to that possible reading, take `C=I` and the two admissible trajectory pairs

\[
p_0=(0,0),\qquad p_1=(t e_1,e_1).
\]

Let `B_n` be independent fair Bernoulli variables and let every neuron at width `n` have pair `p_{B_n}`. Then `mu_n=delta_{p_{B_n}}` always belongs to the fixed compact two-point set `{delta_{p_0},delta_{p_1}}`. Nevertheless its controlled kernel has `J_{n,11}(t)=B_n`, and for `n != m`,

\[
\mathbb P\bigl(\|J_{n,11}-J_{m,11}\|_{L^1(0,T)}=T\bigr)=\frac12.
\]

It is not Cauchy in probability. This is an abstract trajectory-law counterexample to a topological implication, not an assertion about the dynamics of a separately specified network.

A compact-containment proof could contribute to a valid probability argument if it also supplied the required approximation, limit identification, or uniqueness. This source supplies no such argument. A precise replacement for the relevant wording is:

> For random arrays these continuous-map consequences inherit an explicitly supplied W2 convergence-in-probability premise. Compact containment by itself yields no convergence in probability; a separate argument identifying and controlling the limit would be required.

Nor do the path-space W2 couplings establish convergence of kernels in expectation over external randomness: (R19), even if supplied, would require additional integrability for such an upgrade.

## 7. Final disposition of the bounded lemma

| Claim in the source | Audit result |
| --- | --- |
| Exact rule implies (1) | Correct, with precisely `d |dot W_i|^2`. |
| Inverse reconstruction (2) for a fixed interior angle | Correct; constants can diverge near singular angles. |
| Antiparallel reconstruction using `C/4` | Correct under the stated invariance; the scaled energy is `|v|^2/2`. |
| Joint raw-increment/velocity law convergence | Correct in W2 for the indicated C-times-L2 metric. Full rows need joint initial perpendicular data. |
| Integrated energy equality (3) and measurable time subsets | Correct; the proof actually gives L1 convergence of energy densities. |
| Entire controlled matrix convergence (5) | Correct in time L1, including cross entries, under the same hypotheses. |
| No unweighted reverse-field moment needed | Correct for these controlled observables. |
| Node versus recomputed GD kernel distinction | Correct and essential; no interpolation-kernel comparison is established. |
| Compatibility with first-block loss dissipation | Algebraically correct as a speed identity; exact loss identification needs the specified gradient/loss normalization and, for GD, further analysis. |
| Only subsequential consequences from W2 compactness | Correct, with potentially different subsequential limits. |
| “Limit need not be deterministic” | Needs qualification under the expressly deterministic premise. |
| Probability scope | Correct refusal to infer probability convergence automatically; compact containment alone is not an alternative sufficient premise. |
| Actual convergence, population equation, uniqueness, other layers, or all-angle conclusions | Not established, and not supplied by this review. |

The principal conditional proof can be retained. The recommended changes are precision edits to norm scaling and deterministic/probability/loss wording, not a replacement of its reconstruction or L1 coupling arguments. The W2 compactness/convergence premise and the antiparallel invariance remain assumptions throughout.

## Source integrity

- Source: `/tmp/l2-two-sample-proof-0ywjpp/FIRST_RAW_METRIC_AND_CONTROLLED_KERNEL_COMPACTNESS.md`.
- Pre-review SHA-256: `a8feb9d53afd3ed712eb1d9949f9ecb770af26f9d34ff08845df67d797471eee`.
- Post-review SHA-256: `a8feb9d53afd3ed712eb1d9949f9ecb770af26f9d34ff08845df67d797471eee`.
- Integrity result: the source hashes before and after writing the review match exactly.
- Only this separate review file was written; the source was not patched.

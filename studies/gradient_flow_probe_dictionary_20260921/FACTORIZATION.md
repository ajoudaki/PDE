# Frozen two-sided factorization from derivative-generated fields

Continuation requested by the user: organize the derived initialized fields into two frozen dictionaries and one small trainable middle matrix, with dictionary cardinality independent of the number of training samples. This is a representation and gradient calculation, not a new training experiment or an approximation theorem.

## Label-free dictionaries

Fix the two literal probes `e1,e2` and a derivative order `N`. All fields in this section are initialized fields from DERIVATION.md; no task labels or future trajectory are used. Write `phi=tanh` and define, for `a,b in {1,2}`,

\[
U_{ab}=H_b^{(2)}\phi'(Z_a^{(2)}),\qquad
Q_{ab}=(W^{(2)}(0))^*U_{ab},
\]
\[
L_{ab}=\phi'(Z_a^{(1)})^2Q_{ab},\qquad
F_{ab}=2vU_{ab}+W^{(2)}(0)L_{ab},\quad
v=E_1[(H_a^{(1)})^2].
\]

An initial pair of generating lists is

\[
\mathcal V_1=\operatorname{span}\{1,H_a^{(1)},Q_{ab},L_{ab}\},
\]
\[
\mathcal V_2=\operatorname{span}\{1,Z_a^{(2)},H_a^{(2)},U_{ab},
 W^{(2)}(0)L_{ab}\}.
\]

The displayed raw lists have 11 and 13 entries, before any exact dependence removal. They retain the first new forward/reverse computation graph, not every higher-order coefficient. For the middle-velocity terms through cubic order, a sufficient enlargement of the upper span additionally includes

\[
\phi'(Z_a^{(2)})\phi'(Z_b^{(2)})F_{bc},\qquad
H_c^{(2)}\phi''(Z_a^{(2)})F_{ab},\quad a,b,c\in\{1,2\}.
\]

These add at most sixteen listed functions, so the first explicit tensor-factor superset has at most 11 lower and 29 upper generators. This is an algebraic containment count for the derived population cubic middle velocity, not a minimal dictionary or a general full-state jet theorem. It uses the exact population diagonal probe Grams. At finite width those empirical Grams have off-diagonal terms, so exact finite-width jet containment would require empirical corrections or a broader product list; evaluating this population-derived list at finite width still defines a valid approximate compressed model. The equal-weight coefficients in DERIVATION.md obey
`V_a=(y_a/4) sum_b y_b L_ab` and
`R_a=(y_a/4) sum_b y_b F_ab`; substitution into its `F` shows the two displayed upper product families and `U_ab tensor L_ac` exhaust its additional tensor factors. The base list contains the lower factors of the latter tensors.

At higher orders, differentiate the canonical equations, separate all symbolic label coefficients, and collect the initialized intermediate fields and rank-one factors on their own populations. Keep arguments AND results of initialized operator calls. This produces a finite sufficient list at each fixed order and fixed probe count. No claim that every factor is linearly independent or that all-order population derivatives exist is needed for the representation at a computed order.

## Finite-width representation and exact normalization

Evaluate the frozen fields on `n` neurons per layer and orthonormalize each independent column span in its empirical population inner product. Denote the resulting tables by

\[
B_1\in\mathbb R^{n\times K_1},\quad
B_2\in\mathbb R^{n\times K_2},\qquad
\frac1nB_\ell^TB_\ell=I.
\]

This exact algebraic statement allows removal of dependent columns; numerical rank tolerance is a separate implementation choice. The tables remain fixed during training. Replace the entire middle block by

\[
\widehat W^{(2)}(t)=\frac1nB_2M(t)B_1^T,
\qquad M(t)\in\mathbb R^{K_2\times K_1}.
\]

For an arbitrary training or test input,

\[
h^{(1)}(t,x)=\tanh(W^{(1)}(t)x/\sqrt2),\quad
a(t,x)=B_1^Th^{(1)}(t,x)/n,
\]
\[
z^{(2)}(t,x)=B_2M(t)a(t,x),\quad
f(t,x)=\frac1n(W^{(3)}(t))^T\tanh(z^{(2)}(t,x)).
\]

The read-in matrix and readout can train as before; only the dense middle block is restricted to these two frozen spans. The original `n by n` matrix need not be materialized during training.

With `P_l=B_l B_l^T/n`, the initialization

\[
M(0)=\frac1nB_2^TW^{(2)}(0)B_1
\]

satisfies `W2hat(0)=P2 W2(0) P1`. For any required forward call whose argument is in the lower span and result in the upper span, this compressed action is exact. Its transpose likewise preserves a reverse call if both ends are retained. In particular, the displayed lists preserve `H_a^(1) -> Z_a^(2)`, `U_ab -> Q_ab`, and `L_ab -> W2(0)L_ab`. Retaining the upper preactivations is material: a finite polynomial of their bounded tanh activations cannot equal those unbounded population preactivations. These statements are local computation-graph facts; full-flow accuracy needs further control.

## Trainable middle equation and metric

For weighted unhalved squared loss, define

\[
d_a=\frac1nB_2^T
 [W^{(3)}\odot\phi'(z_a^{(2)})],\qquad r_a=f_a-y_a.
\]

Variation of the prediction gives `delta f_a=d_a^T (delta M) a_a`, hence

\[
\dot M=-2\sum_{a=1}^m\omega_a r_a d_a a_a^T.
\]

This is ordinary Euclidean gradient flow in `M`, with mobility one. The lift is a Frobenius isometry:

\[
\|B_2(\delta M)B_1^T/n\|_F^2=\|\delta M\|_F^2.
\]

Indeed cyclicity of trace and the two equalities `B_l^TB_l=nI` cancel `n^2`. Therefore the lifted velocity is the orthogonal two-sided projection of the full middle gradient evaluated at the compressed network's current state. No frozen residual or kernel approximation has been inserted. The first and third blocks retain the canonical finite mobilities `n,n`. For general nonorthogonal bases, the induced physical metric has Gram factors; ordinary coordinate gradient flow then defines a different metric unless corrected. Ridge filtering is not exact orthogonal projection.

The population version, with orthonormal feature vectors `b_l`, is

\[
(\widehat W^{(2)}(t)g)(\omega_2)
=b_2(\omega_2)^TM(t)E_1[b_1g].
\]

Its coefficient and adjoint formulas have the same form, with empirical averages replaced by population expectations.

## Sample-count independence and limitations

With two fixed probes and fixed computed derivative order, `K_1,K_2` do not depend on `m`. More samples change the empirical loss sum, not the feature list. For input dimension `d`, a fixed chosen probe set (for example the `d` axes) and fixed derivative order give the same structural independence. Fixed input/output dimension alone does not bound the order needed for a desired accuracy on every possible task.

At equal finite width, the middle block has `K_1 K_2` trainable scalars, the two frozen tables have `n(K_1+K_2)` stored scalars, and retaining the full trainable read-in and scalar readout gives `nd+n+K_1K_2` trainable scalars (thus `3n+K_1K_2` at `d=2`). These counts exclude data/optimizer workspace and do not remove the cost of processing more observations.

The resulting network accepts arbitrary inputs and trains on arbitrary samples. Its fixed-axis dictionary is an approximation for general directions. No universal exact finite span or sample-independent accuracy guarantee has been claimed. The full original Gaussian matrix is used to construct finite-width frozen features and initialize `M`, then can be discarded. A population-only implementation would instead evaluate the corresponding joint initialized Gaussian programs. Higher derivative features can be unbounded, so the established bounded-dictionary convergence theorem is not automatically inherited.

## Checks

Root checked the factorization and current-loss gradient against established C.4.7.9 (H2.1)--(H2.7). Scoped agent `probe_factorization_check` independently checked the normalization, coefficient mobility, trainable count and initial operator-call preservation from a self-contained prompt. Its assignment had no inherited conversation and permitted no scientific retrieval. This is an internal algebra check, not a promotion review or an executed learning comparison. No additional experiment or maintained code/book edit was performed.

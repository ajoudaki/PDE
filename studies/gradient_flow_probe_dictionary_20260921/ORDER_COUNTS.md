# Dictionary counts by literal order in the middle-weight expansion

This continues the user's request to index the new dictionary by powers in `W^(2)(t)`, rather than by polynomial degree or by powers in its velocity. The count below is specifically for the learned increment `W^(2)(t)-W^(2)(0)`, with zero population readout, two fixed axis probes, and symbolic labels. Additional seed and action fields for compressing the initial operator or matching the complete neural state are not included in this increment count.

From DERIVATION.md,

\[
W^{(2)}(t)-W^{(2)}(0)
=\frac{t^2}{2}\mathcal D-\frac{\tau t^3}{2}\mathcal D+O_{HS}(t^4),
\]
\[
\mathcal D(y)=\sum_{a,b=1}^2y_ay_bU_{ab}\otimes H_a^{(1)},
\qquad U_{ab}=H_b^{(2)}\phi'(Z_a^{(2)}).
\]

Thus under literal maximum Taylor power `p`, the minimal universal lower/upper increment spans have dimensions `(0,0)` at `p=1`, `(2,4)` at `p=2`, and again `(2,4)` at `p=3`. Universality here means the frozen spans work for every pair of labels at those fixed probes. Their sample-count and label independence is part of the definition. The order-three proportionality uses the symmetric equal-weight population calculation; its positive `tau` is assured by the nondegenerate initialized Gaussian probes.

The frozen vectors can be chosen as

\[
\psi_{1,2}=(H_1^{(1)},H_2^{(1)})^T,\qquad
\psi_{2,2}=(U_{11},U_{12},U_{21},U_{22})^T.
\]

There are six dictionary functions in total, and an unrestricted matrix between them has shape `4 by 2` and eight entries. This is separate from the four ordered outer-product terms in `D` and its three label monomials `y1^2,y1 y2,y2^2`. For a fixed label pair the resulting operator has rank at most two. Labels must not be absorbed into the frozen dictionary to claim a smaller universal dimension.

In the displayed raw ordering, the coefficient matrix of `D` is

\[
\begin{pmatrix}
y_1^2&0\\
y_1y_2&0\\
0&y_1y_2\\
0&y_2^2
\end{pmatrix}.
\]

## Independence and minimality proof

The two lower fields are independent centered nondegenerate variables, so their Gram is `v I_2` with `v>0`. Their span dimension is two.

Put `s=H_1^(2), t=H_2^(2)`. Their joint law has full support on the open square `(-1,1)^2`. The four upper functions are

\[
s-s^3,\quad t-s^2t,\quad s-st^2,\quad t-t^3.
\]

A linear relation holding almost surely holds everywhere on that square by continuity, hence is a polynomial identity. Each of the four cubic monomials has a unique coefficient in the displayed relation, forcing all four coefficients to vanish. Therefore the upper span has dimension four.

For universal minimality, `D(1,0)=U11 tensor H1^(1)` and `D(0,1)=U22 tensor H2^(1)` require both lower directions and the upper directions `U11,U22`. Also

\[
D(1,1)-D(1,0)-D(0,1)
=U_{12}\otimes H_1^{(1)}+U_{21}\otimes H_2^{(1)}.
\]

Apply this operator to `H1^(1)/v` and `H2^(1)/v` to recover `U12` and `U21`. Every fixed upper span representing all these label choices must contain all four independent functions. This proves the stated minimal support dimensions for the increment family, not minimality for an entire closure architecture.

If orders are instead numbered by their first two potentially nonzero terms, then level one means `t^2` and level two means `t^3`, and both levels have the same `(2,4)` increment dictionary. That is a different indexing convention from literal Taylor degree. The old polynomial-core `p` is a third convention and must not be conflated with either.

## Check status

Root derived the dimensions and minimality proof. Scoped agent `probe_order_count_check` independently checked the supplied coefficient family from a prompt-only assignment, without any other scientific retrieval. It confirmed the distinction between span dimensions, ordered outer products, label monomials and unrestricted trainable entries. No training, numerical experiment, established-source edit or promotion occurred.

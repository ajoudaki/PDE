# Raw-cubic depth-2 Stieltjes audit through order nine

## Bottom line

The Stieltjes conditions do **not** all remain valid after replacing the raw
quadratic activation by raw cubic.  All four moments determined by the
order-nine jet are positive, and the ordinary Hankel matrix \(H_1\) is
positive definite, but the shifted matrix \(H_1^+\) has a strictly negative
exact determinant:

\[
\boxed{
\mu_1\mu_3-\mu_2^2
=-
\frac{
3136318387543181669964663532850762952758515589
}{
36859700346470723980544924489290665938162841796875000
}<0.
}
\]

Thus the four-moment prefix is not a Stieltjes moment prefix.  This is an
exact finite-order counterexample to extending the output-kernel Stieltjes
claim to this raw-cubic architecture; it does not change results proved or
observed for the raw-quadratic model.

## Convention and exact moments

The transformation is

\[
K(y)=F'\!\left(F^{-1}(y)\right)
=305\,775+\mu_0y^2-\mu_1y^4+\mu_2y^6-\mu_3y^8+O(y^{10}).
\]

Exact rational series reversion gives

| moment | exact value | decimal |
|---|---:|---:|
| \(\mu_0\) | \(93960072/114005\) | \(824.175009867988246\) |
| \(\mu_1\) | \(5787193487251/147192610783125\) | \(0.0393171468082586443\) |
| \(\mu_2\) | \(8262390512438071457518/25655582915973781969921875\) | \(3.22050391117549262\times10^{-4}\) |
| \(\mu_3\) | \(2636622646388500249440493088029/5564847635936495462248842835546875000\) | \(4.73799611216990501\times10^{-7}\) |

Consequently, every accessible one-by-one moment condition is strict:

\[
\mu_0,\mu_1,\mu_2,\mu_3>0.
\]

## Complete accessible PSD audit

The size-one matrices pass:

\[
H_0=[\mu_0]\succ0,
\qquad
H_0^+=[\mu_1]\succ0.
\]

For the ordinary matrix,

\[
H_1=
\begin{pmatrix}
\mu_0&\mu_1\\
\mu_1&\mu_2
\end{pmatrix},
\]

the determinant is

\[
\det H_1
=\mu_0\mu_2-\mu_1^2
=\frac{
85757048922094359666566525129
}{
324984970037287890386771484375
}
=0.263880046244153474\ldots>0.
\]

Hence \(H_1\succ0\).  Its approximate eigenvalues are

\[
0.000320174771729853,
\qquad
824.175011743608.
\]

For the shifted matrix,

\[
H_1^+=
\begin{pmatrix}
\mu_1&\mu_2\\
\mu_2&\mu_3
\end{pmatrix},
\]

both diagonal entries are positive, but

\[
\det H_1^+
=-8.50880055470521677\times10^{-8}<0.
\]

Therefore \(H_1^+\) is indefinite, with approximate eigenvalues

\[
-2.16399978779022\times10^{-6},
\qquad
0.0393197846076577.
\]

The sign is not a floating-point ambiguity.  The equivalent exact Schur
complement is

\[
\mu_3-\frac{\mu_2^2}{\mu_1}
=-
\frac{
3136318387543181669964663532850762952758515589
}{
1449218249830611469860822809648457598571642578125000
}<0.
\]

Thus the vector \((-\mu_2/\mu_1,1)\) is an explicit negative quadratic-form
witness for \(H_1^+\).  Numerically,

\[
\frac{\mu_1\mu_3}{\mu_2^2}=0.179609387693335\ldots,
\]

so the failed inequality is separated substantially from equality.

Across \(H_0,H_0^+,H_1,H_1^+\), seven of the eight enumerated nonempty
principal-minor checks are positive and one is negative.  Equivalently, five
of the six unique scalar PSD inequalities pass and the shifted determinant
fails.

For completeness, the remaining distinct accessible \(2\times2\) Hankel
minor is positive:

\[
\mu_0\mu_3-\mu_1\mu_2
=\frac{
9987673202539975224521403702065077961
}{
26434185613955840215569971977771728515625
}>0.
\]

This redundant total-positivity check does not repair the negative principal
minor.

## Validation and exact cutoff

Two exact transformations agree coefficient by coefficient:

1. rational series reversion followed by \(K=F'\circ F^{-1}\);
2. a triangular solve of \(F'(t)=K(F(t))\), without constructing the inverse.

All moment and determinant decisions use exact rational arithmetic.  The
floating eigenvalues above are diagnostics only.  The frozen derivative,
protocol, derivative-engine, and series-transform hashes all passed.

The current jet determines no moment beyond \(\mu_3\):

- \(\mu_4\) and \(H_2\) require \(F^{(11)}(0)\);
- \(\mu_5\) and \(H_2^+\) require \(F^{(13)}(0)\).

Those higher conditions remain uncomputed, but they cannot undo the already
negative \(H_1^+\) principal minor.

The exact audit implementation has SHA-256
`a63e6925ff148b4587c7b8823827bcdb0a71a331ea6252d368f25e55d0e5866d`.

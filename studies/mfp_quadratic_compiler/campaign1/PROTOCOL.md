# Campaign 1: exact relative-metric and hidden-norm extension

## Scope

This directory contains the exact Campaign 1 extension of the accepted
one-input quadratic MFP compiler.  It does **not** alter or supersede the
checked order-eleven compiler.  It validates two structural additions and
records the completed bounded experiment through output order nine and hidden
order eight:

1. a one-parameter relative block metric; and
2. simultaneous jets for the output and hidden squared-RMS norms.

The exact canonical variables are

\[
x_i=u_i^2,
\qquad
z_p=\sum_i B_{pi}x_i,
\qquad
f=\frac1n\sum_p c_pz_p^2,
\]

where the entries of (B) have variance (1/n).  The observables are

\[
Q_1=\frac1n\sum_i x_i,
\qquad
Q_2=\frac1n\sum_p z_p^2.
\]

The default metric line is

\[
D_\lambda=D_a+\lambda(D_u+D_W),
\qquad \lambda\ge0.
\]

This is a relative metric change, not a common rescaling of feature time.
It is also not the already-studied middle-weight-variance homotopy.  At
\(\lambda=0\), only the readout moves and the feature curve is exactly
linear:

\[
F_0'(0)=27,
\qquad
F_0^{(k)}(0)=0\quad(k\ge2).
\]

The normalized variance-homotopy boundary instead equals

\[
36s e^{72s^2},
\]

whose third derivative is (15\,552\).  Thus no nonsingular linear rescaling
of output and feature time identifies the two boundary curves.

## Exact multi-root state

Every canonical decorated forest carries a three-component amplitude

\[
(A_f(\lambda),A_{Q_1}(\lambda),A_{Q_2}(\lambda)),
\]

whose entries are exact integer polynomials.  A readout hit preserves the
polynomial degree; a first-feature or middle-weight hit multiplies it by
\(\lambda\).  If descendants of different roots reach the same canonical
decorated forest, they share its rewrite and Wick-contraction state.

The three roots are

\[
f=\frac1n\sum_{p,i,j}c_pB_{pi}B_{pj}x_ix_j,
\]

\[
Q_1=\frac1n\sum_i x_i,
\]

and

\[
Q_2=\frac1n\sum_{p,i,j}B_{pi}B_{pj}x_ix_j.
\]

The differentiation operator remains the output-generated operator
\(D_\lambda\).  In particular, adding the (Q_2) root does not add
\(\nabla Q_2\) to the training direction.

## Claim ladder

1. **Exact finite construction.**  At every fixed derivative order reached
   by the program, the emitted coefficients equal the leading-width MFP
   Wick expansion for the stated metric line.
2. **Compiler regression.**  Substitution \(\lambda=1\) reproduces the
   accepted canonical output derivatives.
3. **Finite-order Stieltjes test.**  Formal series inversion converts the
   output and (Q_2) jets into finitely many exact moment candidates and
   Hankel determinants.
4. **All-order conjecture.**  Positivity of all such determinants remains
   open.  Passing any finite campaign is evidence only at the tested orders.
5. **Global trajectory identification.**  This remains a separate open
   obligation even if all formal-jet tests pass.

## Mandatory regression gates

Before any Campaign 1 result is interpreted:

1. The tagged children of every reachable low-order state must agree exactly
   with the unmodified parent rewrite engine after the tags are erased.
2. At \(\lambda=1\), the output jet must reproduce

   \[
   F'(0)=111,
   \qquad
   F^{(3)}(0)=1\,685\,184,
   \qquad
   F^{(5)}(0)=77\,400\,633\,120
   \]

   before any higher order is accepted.
3. Parity must hold coefficientwise:

   \[
   D_\lambda^{2r}f=0,
   \qquad
   D_\lambda^{2r+1}Q_1=D_\lambda^{2r+1}Q_2=0
   \]

   after initialization expectation.
4. The exact Euler identity must hold coefficientwise:

   \[
   D_\lambda Q_1=8\lambda f,
   \qquad
   D_\lambda^kQ_1=8\lambda D_\lambda^{k-1}f.
   \]
5. Initial values must be

   \[
   \mathbb E f=0,
   \qquad
   \mathbb E Q_1=1,
   \qquad
   \mathbb E Q_2=3.
   \]

## Precommitted first execution

The smallest discriminatory hidden-norm test is:

1. compute (D_\lambda^kQ_2) through (k=6);
2. combine it with the already checked output jet through order five;
3. form the first three moments of

   \[
   T_2(x;\lambda)
   =\frac{Q_2(F_\lambda^{-1}(\sqrt{x});\lambda)-3}{x};
   \]

4. test the ordinary (2\times2) Hankel determinant over
   \(\lambda\ge0\).

A strictly negative value at any certified \(\lambda\ge0\) falsifies this
hidden-observable Stieltjes extension, but does not falsify the original
output-kernel conjecture.  If the determinant is nonnegative and every
regression gate passes, extend through order eight for the first shifted
Hankel test.  Do not proceed to orders ten or twelve unless that branch is
explicitly authorized after measuring state growth.

## Implementations

`parametric_multiroot_reference.py` is the transparent whole-forest Python
implementation.  It reuses the accepted leading-width Wick evaluator and its
canonical caches, while retaining a separate tagged rewrite routine that is
checked against the parent routine.

`connected_parametric_multiroot.cpp` is the production connected-recursion
implementation.  It includes an accepted tree representation, canonicalizer,
component splitter, and Wick evaluator without changing the accepted source.
The historical dense primary mode is selected by
`CAMPAIGN1_DENSE_PRIMARY_PARENT` and includes
`../component_recursion.cpp`, whose frozen SHA-256 is

```text
ad53d2d786393cafc9d034685638348afa19f08dbb8d5aeb3110f8e24c7847ad
```

The default build instead includes the checked portfolio evaluator in
`../sector_engine_checked.cpp`, whose frozen SHA-256 is

```text
1931b628b25d2a7c018bc20a06d14aee6ee86ca702d8abcbec17e1ec719be260
```

The wrapper replaces only the scalar recurrence value by a dense exact
polynomial in \(\lambda\).  Arithmetic remains the accepted checked 512-bit
unsigned arithmetic: overflow throws rather than wraps.  The executable
refuses orders above \(F^{(9)}\) and \(Q_1^{(8)},Q_2^{(8)}\).

The present low-order reference run, audited through order five, gives

\[
F_\lambda'(0)=27+84\lambda,
\]

\[
F_\lambda^{(3)}(0)
=123\,120\lambda+699\,408\lambda^2+862\,656\lambda^3,
\]

\[
\begin{aligned}
F_\lambda^{(5)}(0)={}&
1\,730\,898\,720\lambda^2
+14\,214\,258\,432\lambda^3\\
&+35\,456\,350\,464\lambda^4
+25\,999\,125\,504\lambda^5,
\end{aligned}
\]

and

\[
Q_{2,\lambda}^{(2)}(0)
=2\,916\lambda+9\,456\lambda^2,
\]

\[
Q_{2,\lambda}^{(4)}(0)
=20\,751\,552\lambda^2
+123\,392\,448\lambda^3
+167\,175\,936\lambda^4.
\]

At \(\lambda=1\), the three displayed output derivatives reproduce the
accepted canonical values exactly.  Through order five, no complete forest
state belongs to two roots.  Connected-component reuse is nevertheless
substantial: at order five the separate roots require respectively
\(261,80,525\) canonical component keys, while their union has only (669).
Thus the shared cache avoids (197) duplicate component evaluations; (133)
component keys occur in at least two roots.

## Completed bounded production run

The first precommitted execution has completed.  The exact command was

```text
prlimit --as=4294967296 -- timeout 600s \
  connected_parametric_multiroot \
  --max-f 7 --max-q2 6 --max-q1 6 \
  --output campaign1_order7_q2_order6.json
```

It completed in under six seconds and used (5\,483) value-cache entries and
\(3\,983) Wick-base entries.  The durable coefficient output is
`results_order7_q2_order6.json`; its SHA-256 is

```text
9919b54fdddc496af5b4b439f525c0215ed0295d7130a0eb247e2416ce62ca18
```

The new highest hidden-norm derivative is

\[
\begin{aligned}
Q_{2,\lambda}^{(6)}(0)={}&
390\,147\,331\,968\lambda^3
+3\,343\,277\,514\,240\lambda^4\\
&+8\,933\,475\,492\,864\lambda^5
+7\,317\,629\,343\,744\lambda^6.
\end{aligned}
\]

At \(\lambda=1\), this equals

\[
19\,984\,529\,682\,816.
\]

The transparent whole-forest implementation was separately run through order
six under a three-GB, five-minute cap.  It reproduced every coefficient of
the production (Q_1^{(6)}) and (Q_2^{(6)}) polynomials exactly.  At this
order the three separate roots expose (862,261,2\,096) connected-component
keys; their union has (2\,554), avoiding (665) duplicate component
evaluations.

## Exact first Hankel certificates

`analyze_hankel.py` performs exact series inversion and composition.  Put

\[
K_\lambda(y)
=F_\lambda'(F_\lambda^{-1}(y))
=F_\lambda'(0)+\mu_0y^2-\mu_1y^4+\mu_2y^6+O(y^8),
\]

and

\[
T_{2,\lambda}(x)
=\frac{Q_{2,\lambda}(F_\lambda^{-1}(\sqrt{x}))-3}{x}
=\nu_0-\nu_1x+\nu_2x^2+O(x^3).
\]

For every \(\lambda\ge0\), exact coefficientwise-positive rational
certificates prove

\[
\mu_0,\mu_1,\mu_2\ge0,
\qquad
\mu_0\mu_2-\mu_1^2\ge0,
\]

and

\[
\nu_0,\nu_1,\nu_2\ge0,
\qquad
\nu_0\nu_2-\nu_1^2\ge0.
\]

All eight quantities are strictly positive for \(\lambda>0\).  At
\(\lambda=0\), the feature blocks are frozen and the displayed moments vanish
through explicit powers of \(\lambda\).  In particular,

\[
\nu_0\nu_2-\nu_1^2
=\frac{16\lambda^4P_6(\lambda)}
{32\,805(28\lambda+9)^{10}},
\]

where

\[
\begin{aligned}
P_6(\lambda)={}&
19\,767\,831\,420\,944\,384\lambda^6
+43\,084\,897\,006\,679\,808\lambda^5\\
&+38\,879\,388\,442\,425\,024\lambda^4
+18\,414\,359\,217\,379\,152\lambda^3\\
&+4\,812\,644\,080\,574\,964\lambda^2
+658\,030\,009\,006\,728\lambda\\
&+36\,821\,353\,160\,601.
\end{aligned}
\]

At the canonical point,

\[
(\nu_0,\nu_1,\nu_2)
=\left(
\frac{2062}{4107},
\frac{678331568}{5616860517},
\frac{2090752728035608}{38408962828626135}
\right).
\]

The compact exact expressions are in
`hankel_certificates_order7_q2_order6.json`.  A second audit directly reverted
and composed the series at \(\lambda=0,1/2,1,2\) in exact rational arithmetic
and reproduced all six moment expressions.

This result does not prove either all-order Stieltjes conjecture.  It proves
that the first ordinary \(2\times2\) output and hidden-norm Hankel tests pass
over an entire nontrivial relative-metric ray, rather than at one numerical
configuration.

## Completed order-nine/order-eight branch

The authorized second branch computed the complete exact polynomial jets
through \(F^{(9)}\) and \(Q_2^{(8)}\).  The durable raw output is
`results_order9_q2_order8.json`.  Its SHA-256 is

```text
02215aa7c18f3550a19f34b89734b6bf5b66a2825e8aa5bc103517767982ee1a
```

The highest new polynomials are

\[
\begin{aligned}
F_\lambda^{(9)}(0)={}&
2\,478\,851\,054\,278\,778\,880\lambda^4\\
&+32\,885\,131\,309\,935\,058\,944\lambda^5\\
&+165\,198\,603\,388\,928\,974\,848\lambda^6\\
&+388\,905\,477\,453\,868\,400\,640\lambda^7\\
&+423\,643\,509\,104\,850\,763\,776\lambda^8\\
&+168\,049\,569\,513\,538\,584\,576\lambda^9,
\end{aligned}
\]

and

\[
\begin{aligned}
Q_{2,\lambda}^{(8)}(0)={}&
14\,150\,574\,369\,616\,896\lambda^4\\
&+157\,936\,407\,142\,173\,696\lambda^5\\
&+627\,373\,095\,171\,618\,816\lambda^6\\
&+1\,040\,967\,770\,404\,737\,024\lambda^7\\
&+601\,355\,932\,032\,393\,216\lambda^8.
\end{aligned}
\]

At \(\lambda=1\), these equal

\[
F^{(9)}(0)=1\,181\,161\,141\,825\,400\,561\,664,
\qquad
Q_2^{(8)}(0)=2\,441\,783\,779\,120\,539\,648.
\]

The primary exact run was rebuilt and rerun under an enforced four-GB address
space cap and a twenty-minute wall cap.  The rebuilt executable was
byte-for-byte identical to the executable used for the original result.  The
fresh run took 717.631 seconds for the output root and 260.327 seconds for the
second-hidden root.  Every exact coefficient, canonical value, cache count,
and recurrence-miss count matched the original run; only wall timings differed.
The full source, binary, command, resource, raw-result, and certificate hashes
are frozen in `order9_q2_order8_provenance.json`.

## Shifted Hankel certificates

For both the output and second-hidden moment sequences, exact series reversal
gives four moments with the forced scaling

\[
m_r(\lambda)=\lambda^{r+1}\bar m_r(\lambda).
\]

Consequently an ordinary size-\(d\) Hankel determinant has the forced factor
\(\lambda^{d^2}\), while a shifted size-\(d\) determinant has the forced
factor \(\lambda^{d(d+1)}\).  This is a diagonal congruence, not merely an
empirical factorization.

The first new shifted output determinant is

\[
\det\!\begin{pmatrix}\mu_1&\mu_2\\\mu_2&\mu_3\end{pmatrix}
=
\frac{256\lambda^6P_{12}(\lambda)}
{93\,002\,175(28\lambda+9)^{16}},
\]

and the first new shifted hidden determinant is

\[
\det\!\begin{pmatrix}\nu_1&\nu_2\\\nu_2&\nu_3\end{pmatrix}
=
\frac{64\lambda^6Q_{10}(\lambda)}
{837\,019\,575(28\lambda+9)^{16}}.
\]

Every coefficient of both \(P_{12}\) and \(Q_{10}\) is a strictly positive
integer.  Therefore both determinants are nonnegative for every
\(\lambda\ge0\), vanish at \(\lambda=0\) only through the forced factor, and
are strictly positive for \(\lambda>0\).  The complete exact polynomials are
in `hankel_certificates_order9_q2_order8.json` and are regenerated by
`parametric_stieltjes_postprocess.py`.

Thus Campaign 1 found no falsification.  It upgrades isolated canonical PSD
checks to exact inequalities over an entire nontrivial relative-metric ray,
for both the output kernel and a new hidden observable.  It remains
finite-order evidence only.

## Independent graded audit and its limit

`graded_sector.cpp` organizes the same recurrence by fixed counts of
middle-weight and readout hits.  A durable unit test reconstructs every
\(\lambda\)-coefficient through \(F^{(7)}\) and \(Q_2^{(6)}\) and matches the
frozen dense results exactly.  In the capped upper run, all 55
\(F^{(9)}\) sectors completed and their canonical sum matched the accepted
value.  Only 24 of 45 \(Q_2^{(8)}\) sectors completed before the global cap.
The runner had not checkpointed those records, so the partials are not safely
reusable.  This incomplete route validates no \(Q_2^{(8)}\) claim; the fresh
dense rerun is the primary certificate.

No \(Q_2^{(10)}\) or higher branch was launched.

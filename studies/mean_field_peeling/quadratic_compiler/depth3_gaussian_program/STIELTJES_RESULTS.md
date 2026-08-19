# Depth-3 Stieltjes audit from the order-nine feature jet

## Bottom line

No Stieltjes Hankel inequality available from the depth-3 derivatives through
(F^{(9)}(0)) is violated.  All four available moments are strictly positive,
and all four accessible ordinary/shifted Hankel matrices are positive
definite.  This is strict finite-order compatibility, not an all-order proof.

## Convention and exact moments

The audit uses

\[
K(y)=F'\!\left(F^{-1}(y)\right)
=14\,175+\mu_0y^2-\mu_1y^4+\mu_2y^6-\mu_3y^8+O(y^{10}).
\]

Exact reversion gives

| moment | exact value | decimal |
|---|---:|---:|
| (\mu_0) | (95641312/275625) | 346.99795736961454 |
| (\mu_1) | (3963629647049188/3230587705078125) | 1.2269066835173064 |
| (\mu_2) | (12164741271894434633792/601040746943206787109375) | 0.020239461856392072 |
| (\mu_3) | (4206861574840394358968837051264/9862678589590839304447174072265625) | 0.00042654351316693563 |

Thus every available scalar moment-sign condition is strict:

\[
\mu_0>0,
\qquad \mu_1>0,
\qquad \mu_2>0,
\qquad \mu_3>0.
\]

## Complete accessible Hankel audit

The one-by-one matrices are

\[
H_0=[\mu_0]\succ0,
\qquad
H_0^+=[\mu_1]\succ0.
\]

The first nontrivial ordinary determinant is

\[
\begin{aligned}
\Delta_1
&=\det H_1
=\mu_0\mu_2-\mu_1^2\\
&=\frac{57587104390258273954913012692208}
{10436696920201946353912353515625}\\
&=5.5177519123688406\ldots>0.
\end{aligned}
\]

Since (\mu_0>0), Sylvester's criterion gives

\[
H_1=
\begin{pmatrix}
\mu_0&\mu_1\\
\mu_1&\mu_2
\end{pmatrix}\succ0.
\]

Its approximate eigenvalues are

\[
0.0159011971442169,
\qquad 347.002295634327.
\]

The first shifted determinant is

\[
\begin{aligned}
\Delta_1^+
&=\det H_1^+
=\mu_1\mu_3-\mu_2^2\\
&=\frac{
18112616071796981590543696523289774449027892736}
{159311240953347141011947883502580225467681884765625}\\
&=0.00011369327087911579\ldots>0.
\end{aligned}
\]

Since (\mu_1>0), again by Sylvester's criterion,

\[
H_1^+=
\begin{pmatrix}
\mu_1&\mu_2\\
\mu_2&\mu_3
\end{pmatrix}\succ0.
\]

Its approximate eigenvalues are

\[
0.0000926413876864984,
\qquad 1.22724058564279.
\]

All eight nonempty principal-minor checks across
(H_0,H_0^+,H_1,H_1^+) are strictly positive.  Equivalently, all six unique
available scalar inequalities

\[
\mu_0,\mu_1,\mu_2,\mu_3,
\Delta_1,\Delta_1^+>0
\]

hold.

## Exact cutoff

The current jet determines no moment beyond (\mu_3):

- (\mu_4) and the ordinary (3\times3) matrix (H_2) require
  (F^{(11)}(0));
- (\mu_5) and the shifted (3\times3) matrix (H_2^+) require
  (F^{(13)}(0)).

Those conditions are **undecided**, not presumed positive.

## Validation and claim level

Two exact transformations agreed:

1. rational series reversion followed by (K=F'\circ F^{-1});
2. a triangular coefficient solve of the independent identity
   (F'(t)=K(F(t))), without constructing (F^{-1}).

Every matrix decision used exact principal minors; floating eigenvalues are
reported only as conditioning diagnostics.  The audit ran in 0.03 seconds
with 15,196 KiB peak resident memory.

This establishes exact-under-assumptions compatibility with all Stieltjes
Hankel conditions accessible from the order-nine formal jet.  It does not
establish the missing higher Hankel conditions, a representing measure for an
unknown full moment sequence, formal-series convergence, or a positive-time
mean-field trajectory.

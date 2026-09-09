# Unit-Gram versus unnormalized-quadratic control

This is a scope correction, not a failed algebra check.

The proposed scalar recurrence has imposed

\[
Q^0=\cdots=Q^H=1,\qquad M_{200000}=\mathbb E[\phi(G)^2]=1.
\]

The canonical activation \(\phi(x)=x^2\) does not belong to that shared
unit-Gram class:

\[
Q^0,Q^1,Q^2,Q^3,Q^4=1,3,27,2187,14348907.
\]

Consequently the accepted unnormalized values, beginning with

\[
(A_2,B_2,C_2)=(111,1685184,77400633120),
\]

cannot be obtained by substituting \(x^2\) moments into a quotient in which
\(M_{200000}\) has already been set to one.  An independent exact evaluation
of the three frozen unit maps gives instead the purely formal quotient
values

\[
\begin{array}{c|rrr}
H&A&B&C\\\hline
2&21&321600&9391605792\\
3&85&128455488&313377512166432\\
4&341&64111733568&17305789745609614368.
\end{array}
\]

These numbers are not the coefficients of the actual unnormalized quadratic
network.  Therefore a correct final report must use two differently labeled
gates:

1. exact expansion of the new unit-Gram recurrence against the frozen unit
   maps; and
2. the already-audited layer-tagged/arbitrary-Gram compiler for the accepted
   unnormalized quadratic controls.

Claiming that the unit recurrence itself reproduces the accepted quadratic
values would be false.  Extending the new compact scalar recurrence to
layer-dependent moments/Grams is a separate obligation.

A genuine exact affine control within the shared unit-Gram class is
\(\phi(x)=3/5+4x/5\), for which
\(\mathbb E\phi(G)^2=1\).  Its unit-map values are recorded by
`exact_controls.py`.

# Full signed-polynomial bridge: hostile audit

## Verdict

The arbitrary-signed theorem is proved for the frozen scalar recursion, but
is **not proved for the same full width-first two-hidden-layer network**.
Two distinct steps used in the nonnegative-coefficient proof fail:

1. deletion of the bottom-layer update is no longer coefficientwise
   monotone;
2. the algebraically largest finite-width sector need not survive Gaussian
   integration and the width limit.

The first failure is not merely the absence of a proof.  For the exactly
RMS-normalized signed quadratic

\[
 \psi(x)=-\frac{11}{9}+\frac{10}{27}x^2,
 \qquad
 \left(-\frac{11}{9}\right)^2
 +2\left(-\frac{11}{9}\right)\frac{10}{27}
 +3\left(\frac{10}{27}\right)^2=1,
\]

the exact chronological width-first Wick DAG gives

\[
 [h^{11}]\{\Delta_1^{\rm full}(h)-
                 \Delta_1^{\rm frozen}(h)\}
 =-\frac{
 50342126934494248177872714327572247743518720000000000
 }{
 375710212613636260325580163599137907799836383538729
 }<0,
\]

where \(\Delta_1(h)=F_2(h)-F_1(2h)\).  Thus the coefficientwise deletion
order used in the positive-semiring proof is actually false after the width
limit.  The exact reproducer is `audit_signed_deletion_failure.py`.

The following exact width-first example disproves the tempting replacement
claim that a positive leading activation coefficient forces a nonzero top
step-size coefficient.

## Exact centered-quadratic calculation

Let

\[
 \psi_K(x)=b_K(x^2-K),\qquad
 b_K=(K^2-2K+3)^{-1/2}.
\]

Then \(\mathbb E\psi_K(G)^2=1\) and the leading coefficient \(b_K\) is
positive.  More generally write \(\psi(x)=a+bx^2\), under the normalization
\(a^2+2ab+3b^2=1\).  In the exact one-step width-first OMFP DAG,

\[
 U_1=U+2bhBU,\qquad B\sim N(0,4b^2),
\]

and hence

\[
 Q_{01}=\mathbb E[\psi(U)\psi(U_1)]
 =1+16b^5(a+3b)h^2.
\]

The reused-adjoint plus learned-matrix response is

\[
 L=h\,\mathbb E[\psi'(U_1)\psi'(U)]+hQ_{01}
   =(1+4b^2)h+16b^5(a+3b)h^3.
\]

With \(Z_0=\xi_0\), \(Z_1=\xi_1+2bLAZ_0\), and
\(A_1=A+h\psi(Z_0)\), the only contribution to order \(h^7\) in
\(F_1(h)=\mathbb E[A_1\psi(Z_1)]\) is

\[
 h\,4b^3L^2\,\mathbb E[\psi(Z_0)Z_0^2].
\]

Since \(\mathbb E[\psi(G)G^2]=a+3b\), this gives the exact identity

\[
 \boxed{[h^7]F_1(h)=1024b^{13}(a+3b)^3.}
\]

For \(a=-3b\), equivalently \(K=3\) and \(b=1/\sqrt6\),

\[
 [h^7]F_1(h)=0.
\]

This is an RMS-normalized, genuinely nonlinear activation with positive top
coefficient.  The calculation is in the width-first Gaussian DAG, not a
finite-width Taylor limit.  Pointwise fixed-\(h\) identification follows
from the fixed finite polynomial-program theorem already used for polynomial
activations.  The exact rational checker
`audit_centered_quadratic_top.py` reproduces the formula before normalization;
normalization changes \((a,b)\) by a common positive factor and therefore
preserves the zero at \(a+3b=0\).

## What the example does and does not show

It refutes all proofs which assert that the maximal \(h\)-sector is always
strictly positive/nonzero merely from \(c_d>0\), or that the positive
joint \((h,\hbox{raw degree})\) finite-width branch automatically survives
the width limit.  It is not a counterexample to the eventual uniform-tail
no-go: lower \(h\)-sectors can and do survive.

Chebyshev extremality controls cancellation among the powers of \(h\) once
one has a quantitatively nonzero coefficient of the **full** width-first
polynomial.  It cannot transfer the already proved frozen coefficient to the
full DAG, and it cannot prove that a finite-width index sector survives
\(n\to\infty\).  Those are the two missing full-network lemmas.  Therefore a
strict universal full-network lower bound for arbitrary signed lower
coefficients remains open under the stated hypotheses.

# Final release audit: quadratic uniform-tail no-go

## Verdict

**PASS**, with the polynomially-smooth finite NETSOR\({}^\top+\)Moment
theorem recorded in
`generic_first_stieltjes/PROBABILISTIC_BRIDGE_AUDIT.md` treated as the
available established theorem specified in the audit contract.

The alternative bridge in `FIXED_H_QUADRATIC_WIDTH_LEMMA.md` exactly maps
the trained network to that theorem and closes the fixed-\((N,h)\) annealed
width limit.  The no-go proof then respects the required order: for each
fixed \(t\), take the two width limits at fixed step sizes; only afterward
send \(t\to\infty\).

## Exact exponent check

For the selected all-quadratic branch, let \(A,Z\in\mathbb N^2\) denote the
raw \((A_0,Z_0)\)-exponent vectors in the selected leading monomials of the
two state coordinates.  One selected update sends

\[
 A\mapsto2Z,
 \qquad Z\mapsto A+Z.
\]

Two updates therefore send

\[
 A\mapsto2A+2Z,
 \qquad Z\mapsto A+3Z.
\]

The selected output monomial is \(qAZ^2\), whose exponent is \(A+2Z\).
After two updates,

\[
 (2A+2Z)+2(A+3Z)=4(A+2Z).
\]

At horizon zero this output exponent is

\[
 A_0^1Z_0^2,
\]

so iteration over \(t\) pairs gives exactly

\[
 (R_{2t},S_{2t})=(4^t,2\cdot4^t).
\]

Both exponents are even for \(t\ge1\).  Taking
\(K=S_{2t}=2\cdot4^t=2m\), hence \(m=4^t\), yields

\[
 \mathbb EG^{S_{2t}}
 =(2m-1)!!\ge m!\ge(m/e)^m
 =\left(\frac{4^t}{e}\right)^{4^t}.
\]

The other even moment is at least one.  Thus the released lower bound

\[
 L_t=q^{3(4^t-1)+1}
 \left(\frac\rho t\right)^{3(4^t-1)}
 \left(\frac{4^t}{e}\right)^{4^t}
\]

is correct for \(q>0\).  Moreover

\[
\begin{aligned}
\frac{log L_t}{4^t}
={}&\left(3-\frac2{4^t}\right)\log q
+\left(3-\frac3{4^t}\right)(\log\rho-\log t)\\
&+t\log4-1
=t\log4-3\log t+O_{q,\rho}(1),
\end{aligned}
\]

which tends to \(+\infty\).

## Remaining bridge and conclusion checks

- Coefficientwise deletion monotonicity is valid before Gaussian
  expectation.
- Gaussian expectation preserves coefficientwise nonnegativity.
- The coarse \(t\)-step scalar polynomial has strictly smaller \(h\)-degree
  than the selected fine \(2t\)-step term, so that term survives subtraction.
- The two orthogonal conjugacies correctly reduce arbitrary signs of
  \((p,q)\) to \((|p|,|q|)\).
- The cubic subtraction is \(O_{p,q}(1/t)\) at \(h=\rho/t\), while
  \(L_t\to\infty\).
- The proposed right side \(Ct^4h^5=C\rho^5/t\) tends to zero.  More
  generally, \(L_t\) dominates every fixed polynomial in \(t\).

Therefore every fixed nonzero quadratic coefficient, however small, rules
out the desired horizon-uniform fifth-order remainder on a step window of
positive total-time size \(\rho/t\).  This is compatible with the exact
local fifth coefficient being only quartic in \(t\): the obstruction occurs
at order \(3(4^t-1)\), which grows with the horizon.


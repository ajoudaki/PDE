# Independent audit of the two oscillatory counterexample claims

## 1. Triangular-phase scalar theorem

The scalar theorem in `SCALAR_COUNTEREXAMPLE.md` is valid with its stated
scope.

For

\[
 \Phi(x)=2+\sqrt{1+x^2}+\lambda\arcsin(\sin x^3),
 \qquad 0<\lambda\le1/\pi,
\]

one has \(\Phi>0\), \(c|x|^2\le|\Phi'(x)|\le D(1+x^2)\) away from the
countable corner set and for sufficiently large \(|x|\).  On the event

\[
 1\le a_0\le2,\qquad K/h\le z_0\le K/h+1,
\]

positivity makes \(a_r\ge1\), while the reverse triangle inequality gives

\[
 |z_{r+1}|\ge \frac c2h|z_r|^2.
\]

Thus the fine \(2t\)-step amplitude has logarithm bounded below by
\(c_1 4^t-O(t^2)\); the \(O(t^2)\) term is exactly the Gaussian cost of
the event \(z_0\asymp t\).  The negative part of the terminal observable
is only \(O(1/h)\), because on \(a_N<0\) monotonicity gives
\(h\Phi(z_r)\le|a_0|\).  For the coarse schedule, the global recursion
\(R_{r+1}\le C R_r^3\) gives logarithmic expectation at most
\(O(t3^t)\).  Since \(4^t\gg t3^t\), the claimed fine/coarse separation
follows without comparing two quantities on the same exponential scale.

The countable corner set causes no missing mass.  On each phase cell the
two-dimensional update is real analytic.  Its Jacobian determinant is

\[
 1+ha\Phi''(z)-h^2\Phi'(z)^2,
\]

which cannot vanish on a two-dimensional open set (for fixed \(z\) it is
affine in \(a\), and the exceptional \(\Phi''=0\) case would also require
the nonconstant function \(|\Phi'|\) to equal \(1/|h|\) on an interval).
Hence each finite iterate is absolutely continuous cell by cell and hits
the corner set with probability zero.

The quantifiers are therefore correct: for every fixed
\(0<\rho\le1/2\), the scalar discrepancy at \(h_t=\rho/t\) beats every
polynomial.  It is not a theorem about a smooth activation and it is not a
theorem about the full two-hidden-layer OMFP DAG.

## 2. Smooth exponential-phase shifted derivative

The analytic claim in `SMOOTH_FIXED_STEP_BREAKDOWN.md` is also valid.  If

\[
 \Phi(x)=3+\sqrt{1+x^2}+\epsilon\sin(e^{cx}),
\]

then every initialization Gaussian moment of every derivative is finite,
because \(|\Phi^{(r)}(x)|\le C_r(1+e^{rcx})\).  Nevertheless, for
independent nondegenerate centered Gaussians \(U,B\), every \(h\ne0\),
and

\[
 U_1=U+hB\phi'(U),
\]

one has \(\mathbb E|\phi'(U_1)|^2=\infty\).  Conditioning on large phase
intervals where \(e^{cU}\) is close to \(2\pi n\) makes
\(\phi'(U)\ge k e^{cU}\).  Integrating over a fixed-sign interval of
\(B\), followed by the substitution \(q=e^{c(U+hB\phi'(U))}\), gives a
conditional lower bound \(\exp(k'e^{cU})\).  Its product with the Gaussian
density of \(U\) is not integrable.  The same argument uses a negative
interval of \(B\) when \(h<0\), so no sign of \(h\) was omitted.

In fact the proof gives the stronger response obstruction

\[
 \mathbb E\bigl|\phi'(U)\phi'(U_1)\bigr|=\infty. \tag{1}
\]

To see this, on the same phase intervals integrate \(|\phi'(U_1)|\), not
its square.  The change of variables gives

\[
 \mathbb E_B[|\phi'(U_1)|\mid U=x]
 \ge \frac{c_0}{|h|\phi'(x)}
 \int_{Y_1}^{Y_2}|\cos q|\,dq-C_0,
\]

and \(\int_{Y_1}^{Y_2}|\cos q|dq\ge c_1Y_2\) once
\(Y_2/Y_1\) is large.  Multiplication by \(\phi'(x)\) and integration in
\(x\) proves (1).  Restricting the \(q\)-integral separately to positive
and negative cosine phases shows that both signs have infinite mass; the
signed response is therefore not a finite Lebesgue expectation.

## 3. What the smooth claim does and does not imply for actual `L=2`

At the first lower update of the established DAG,

\[
 u_1=U+hB\phi'(U),
\]

with \(U\) and \(B\) independent nondegenerate Gaussians.  Hence (1)
shows that the response coefficient

\[
 \rho_{10}=h\,\mathbb E[\phi'(u_1)\phi'(U)]
\]

is not a finite absolutely convergent Gaussian integral.  Thus
initialization Gaussian derivative moments, even all of them, do not
guarantee that the fixed-nonzero-step OMFP operator DAG is well defined.

This still does **not** prove that an actual full-network expected output
\(F_N(h)\) is infinite or fails to have a width-first limit.  Such a claim
would require one of the following additional arguments, neither of which
is contained in the candidate proof:

1. a finite-width lower bound that survives all connector correlations and
   proves non-uniform integrability of the terminal output; or
2. a theorem that the divergent response coefficient cannot be cancelled
   in the exact reused-matrix conditioning identity and forces divergence
   of the terminal expectation.

The rigorous conclusion is therefore an operator-integrability
counterexample, not an `L=2` terminal-output counterexample.

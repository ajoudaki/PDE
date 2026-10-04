# The local profile contrast at the first nonlinear feedback

This is additional evidence for the local hypothesis in DECISIVE_CONDITIONAL_ROUTE.md, not its propagation theorem. Take two tanh layers, one normalized training input, zero initial readout, and the deterministic driver \(b(u)=u\). Use that note's width \(N=2n\), two-block profile \(c_{ij}(s)\), initialized variances \(c_{ij}/N\), and matched edge mobilities \(c_{ij}\), with \(0\le s\le1/2\).

Write the initialized first preactivation as \(a\), and set
\[
h=\tanh a,\quad d=\operatorname{sech}^2a,\quad z=W_0h,\quad
g=\tanh z,\quad \psi(z)=g\odot(1-g^2),\quad T=W_0^\top\psi(z),
\]
\[
q_i=N^{-1}\sum_jc_{ij}h_j^2,\qquad
E_c=N^{-1}\sum_i q_i\psi(z_i)^2
       +N^{-1}\sum_j d_j^2T_j^2.
\]
Let \(q_N(u)=d f_N(u,x_1)/du\), reserving \(q_i\) for the row variances just defined. Exact differentiation of the controlled dense equations at zero readout gives
\[
q_N'(0)=0,\qquad q_N''(0)=4E_c.
\tag{1}
\]

For verification, \(w'(0)=g\), all first hidden velocities vanish,
\(\delta'(0)=\psi(z)\),
\(W''(0)=c\odot(\psi(z)h^\top)/N\), and
\(a''(0)=d\odot T\). Thus
\[
z''(0)=\operatorname{diag}(q_i)\psi(z)+W_0(d^2\odot T),
\quad N^{-1}g^\top g''(0)=E_c.
\]
The controlled tangent coefficient \(q_N\) is the readout feature energy plus the two hidden mobility-weighted gradient energies. The second derivative of the first part is \(2E_c\); those of the initially zero hidden parts sum to another \(2E_c\). This proves (1). Equivalently \(f_N'''(0)=4E_c\) since \(u\) is the residual-free control, not physical time.

Define bounded smooth functions of a variance \(q\in[0,1]\):
\[
\alpha(q)=\mathbb E\psi'(\sqrt q\,G),\qquad
\beta(q)=\mathbb E\psi(\sqrt q\,G)^2,\qquad
\gamma(q)=\mathbb E(\psi^2)''(\sqrt q\,G),
\]
where \(G\) is standard Gaussian. All fixed derivatives needed below are bounded, including at \(q=0\), by Gaussian integration by parts and bounded tanh derivatives.

Conditional on \(a\), different rows of \(W_0\) are independent, and direct Gaussian integration by parts gives
\[
\mathbb E[T_j^2\mid a]
=\frac1N\sum_i c_{ij}\beta(q_i)
 +h_j^2\left\{
\left(\frac1N\sum_i c_{ij}\alpha(q_i)\right)^2
 +\frac1{N^2}\sum_i c_{ij}^2
       [\gamma(q_i)-\alpha(q_i)^2]\right\}.
\tag{2}
\]
Indeed the row mean is \(c_{ij}h_j\alpha(q_i)/N\), and the row second moment is \(c_{ij}\beta(q_i)/N+c_{ij}^2h_j^2\gamma(q_i)/N^2\); summing row cross products gives (2). The order-one response mean is retained.

For block \(A\) or \(B\), define its empirical triple
\[
X_A=(Q_A,V_A,U_A)
=\frac1n\sum_{j\in A}(h_j^2,d_j^2,d_j^2h_j^2),
\]
and likewise \(X_B\). Put
\[
\widetilde Q_A=(1-s)Q_A+sQ_B,\qquad
\widetilde Q_B=sQ_A+(1-s)Q_B,
\]
and abbreviate \(\alpha_A=\alpha(\widetilde Q_A)\), \(\beta_A=\beta(\widetilde Q_A)\), \(C_A=\gamma(\widetilde Q_A)-\alpha_A^2\), and similarly for \(B\). Substituting (2) gives the exact conditional mean
\[
\begin{aligned}
\mathbb E[E_c\mid a]={}&
\tfrac12(\widetilde Q_A\beta_A+\widetilde Q_B\beta_B)\\
&+\tfrac12\{V_A[(1-s)\beta_A+s\beta_B]
              +V_B[s\beta_A+(1-s)\beta_B]\}\\
&+\tfrac12\{U_A[(1-s)\alpha_A+s\alpha_B]^2
              +U_B[s\alpha_A+(1-s)\alpha_B]^2\}\\
&+\frac1N\{U_A[(1-s)^2C_A+s^2C_B]
                  +U_B[s^2C_A+(1-s)^2C_B]\}.
\end{aligned}
\tag{3}
\]

The first three lines are a smooth function \(F_s(X_A,X_B)\); the last is \(N^{-1}G_s(X_A,X_B)\), with bounded derivatives through the orders used below, uniformly in \(s\). Both empirical triples have the same deterministic mean \(x_*=(Q_*,V_*,U_*)\), their centered first moments vanish, and their centered second moments are \(O(1/n)\). At equal means,
\[
F_s(x_*,x_*)=(Q_*+V_*)\beta(Q_*)+U_*\alpha(Q_*)^2,
\]
which is independent of \(s\). Taylor expansion of \(\partial_sF_s\) at \((x_*,x_*)\) has zero constant term, a linear term of zero expectation, and a remainder of expected magnitude \(O(1/n)\). The derivative of \(G_s/N\) is \(O(1/N)\). Consequently
\[
\left|\frac d{ds}\mathbb E q_N''(0)\right|
\le C/N.
\tag{4}
\]
By the exact interpolation identity, this is the second activity-derivative coefficient of the normalized within-block versus cross-block response contrast. The zeroth activity coefficient obeys the same \(O(1/N)\) rate by the initialization calculation in DECISIVE_CONDITIONAL_ROUTE.md; the first coefficient is zero by (1).

Differentiation and expectation interchange at these initial coefficients is justified directly: the formulas contain bounded smooth functions of bounded empirical \(h,d\), and Gaussian polynomial factors with finite moments. This does not assert analytic continuation or sum a time series.

Thus the contrast condition is consistent not only with initial random features but with the first genuine learned-matrix/adjoint feedback. Extending (4) from a coefficient at zero to a full fixed positive activity interval remains open. No trained rate follows from the coefficient calculation alone.

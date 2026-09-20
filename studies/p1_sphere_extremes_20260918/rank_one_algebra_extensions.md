# Explicit ambient stationarity with prescribed effective signs

This bounded follow-up uses only the supplied algebraic setup and the supplied
statement that every sufficiently small triple of prescribed lower vectors can
be realized by a finite odd lower field on the canonical marks. It supplies no
claim about reachability from initialization or about an unspecified rule for
realizing the derivative vectors.

Let \(e_1,e_2,e_3\) denote the standard basis of \(\mathbb R^3\), and
\(f_1,\ldots,f_6\) the standard basis of \(\mathbb R^6\). Fix
\[
p=(1/4,1/4,1/2),\qquad y=(1,1,-1),\qquad
s=(-1,1,-1),\qquad \rho=(-3/8,-1/8,1/4).
\]
For reference, the stipulated residuals satisfy the arithmetic identity
\(\rho_i=p_i(s_i/2-y_i)\). This identity does not assume a readout formula.

## 1. Nonzero common derivative, rank-two middle matrix and lower features

For any \(t>0\) and \(\delta>0\), set
\[
M=t^{-1}(e_1f_1^T+e_3f_2^T),\qquad d_i=\delta e_2\quad(i=1,2,3),
\]
and
\[
a_1=t(-f_1+f_3),\qquad
a_2=t(f_1+f_3),\qquad
a_3=t(-f_1+2f_3).
\]
Then \(Mf_1=t^{-1}e_1\), \(Mf_2=t^{-1}e_3\), and \(Mf_j=0\) for
\(j\geq3\), so
\[
\operatorname{rank}M=2,\qquad Ma_i=s_i e_1,\qquad M^Td_i=0.
\]
The first two lower vectors are independent: if
\(\alpha a_1+\beta a_2=0\), their \(f_1\) and \(f_3\) coordinates give
\(-\alpha+\beta=0\) and \(\alpha+\beta=0\), hence \(\alpha=\beta=0\).
All three belong to \(\operatorname{span}\{f_1,f_3\}\), and
\[
2a_3=3a_1+a_2.
\]
Consequently every \(a_i\ne0\), their joint rank is exactly two, and they are not
all proportional. The residual identity gives
\[
\sum_{i=1}^3\rho_i a_i
=\frac{-3a_1-a_2+2a_3}{8}=0.
\]
Thus both stationarity conditions hold:
\[
\sum_{i=1}^3\rho_i d_i a_i^T
=\delta e_2\left(\sum_{i=1}^3\rho_i a_i\right)^T=0,
\qquad
\rho_iM^Td_i=0\quad(i=1,2,3).
\]
Every summand in middle stationarity is nonzero, since
\(\rho_i\ne0\), \(d_i\ne0\), and \(a_i\ne0\). Cancellation uses the common
left factor and the displayed linear relation, without collinearity of the
lower vectors.

## 2. Full-row-rank middle matrix and independent lower features

For any \(t>0\), set
\[
\widetilde M=t^{-1}(e_1f_1^T+e_2f_2^T+e_3f_3^T),
\]
\[
\widetilde a_1=t(-f_1+f_4),\qquad
\widetilde a_2=t(f_1+f_5),\qquad
\widetilde a_3=t(-f_1+f_6),\qquad
\widetilde d_i=0.
\]
Then \(\operatorname{rank}\widetilde M=3\) and
\(\widetilde M\widetilde a_i=s_i e_1\). If
\(\sum_i c_i\widetilde a_i=0\), its \(f_4,f_5,f_6\) coordinates are
\(tc_1,tc_2,tc_3\), respectively, so every \(c_i=0\). Therefore
\[
\operatorname{rank}[\widetilde a_1\ \widetilde a_2\ \widetilde a_3]=3.
\]
With the same nonzero residuals, both stationarity equations hold because every
\(\widetilde d_i=0\). No cancellation relation among the
\(\rho_i\widetilde a_i\) is needed in this case.

In the first construction \(\max_i\|a_i\|=\sqrt5\,t\); in the second it is
\(\sqrt2\,t\). Choosing \(t\) sufficiently small therefore places either triple
inside any prescribed neighborhood of zero, as required to apply the supplied
lower moment-realization statement. For each fixed \(t>0\) both middle matrices
are finite; their operator norms equal \(t^{-1}\), so this scaling does not give
a bound on those norms uniform as \(t\downarrow0\).

These are ambient algebraic constructions. The first disproves any proposed
algebraic necessity that three active stationary terms have proportional lower
vectors; the second shows that full row rank of the middle matrix and full rank
of the three lower vectors, even together, do not exclude stationarity with the
stipulated nonzero residuals when derivative vectors may vanish. Additional
architectural or dynamical information is needed to exclude these cases.
Neither construction establishes accessibility from an initialized trajectory.

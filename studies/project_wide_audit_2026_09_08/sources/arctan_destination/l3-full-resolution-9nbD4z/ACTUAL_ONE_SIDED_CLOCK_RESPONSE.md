# Every expanding direction is controlled in physical time

Candidate pending independent full-file audit. This refines the two-extreme
exclusion in ACTUAL_CLOCK_RANK_ONE_RESPONSE.md. The physical clock has a
negative semidefinite derivative correction. Therefore no expanding
direction has to be excluded from the all-physical-time squared-log bound.
Only the smallest singular value is excluded from a two-sided version.
This remains logarithmic control, not a width-uniform response-trace bound
or a population continuation theorem.

The canonical model, raw Euclidean coordinates
\(\theta=(z^{(1)},\sqrt n W^{(2)},\sqrt n W^{(3)},W^{(4)})\),
feature field \(b=\nabla_\theta[nf_n]\), and constants \(C_B(M,R)\)
and \(K_b(M,R)\) are as in ACTUAL_SQUARED_LOG_RESPONSE.md:
\[
\|Db\|_{\rm F}\le C_B(M,R)\sqrt n,\qquad
\|b\|_2\le K_b(M,R)\sqrt n.
\]
For specificity, with \(a=\pi/2\), \(K_2=a+M\), \(K_3=a+MK_2\),
\[
C_B=2R(M^2+MK_2^2+K_3^2+M+K_2)+\sqrt2K_3,
\quad
K_b^2=M^4R^2+a^2M^2R^2+a^2R^2+a^2.
\]
No maximum-coordinate bound on a backward field is imposed.

## One-sided logarithmic energy

Let \(V'=D(t)V\), with \(V\) a real \(N\)-by-\(m\) matrix of full
column rank. Set \(G=V^TV>0\), \(Q=VG^{-1/2}\), and
\[
\mathcal E_+(V)=\frac14\operatorname{Tr}[(\log G)_+^2]
             =\sum_{j=1}^m(\log\sigma_j(V))_+^2.
\]
Here the positive part of a symmetric matrix is defined on its
eigenvalues, and \(x_+=\max(x,0)\). The scalar function
\(g(\lambda)=(\log\lambda)_+^2/4\) is continuously differentiable
on \((0,\infty)\), with derivative
\(g'(\lambda)=(\log\lambda)_+/(2\lambda)\), including at \(\lambda=1\).
Consequently the trace differential used for the two-sided energy gives
\[
\mathcal E_+'=\operatorname{Tr}[(\log G)_+Q^TD_{\rm sym}Q].
\tag{1}
\]
Here is an elementary justification at repeated eigenvalues and crossings
of one. On any compact positive spectral interval approximate \(g'\)
uniformly by polynomials \(p_k\), and let \(g_k\) be their primitives
agreeing with \(g\) at one point. Polynomial trace differentiation gives
\(\operatorname{Tr}g_k(G(t))-\operatorname{Tr}g_k(G(t_0))
=\int_{t_0}^t\operatorname{Tr}[p_k(G(u))G'(u)]\,du\).
Uniform convergence of both functions on this spectral interval allows
passage to the limit. The resulting integral has a continuous integrand,
so its derivative is \(\operatorname{Tr}[g'(G)G']\).
Substitution of
\(G'=2G^{1/2}Q^TD_{\rm sym}QG^{1/2}\) proves (1).
This uses only approximation of a continuous scalar function on a
compact interval; no differentiable singular-vector selection is needed.

If \(D_{\rm sym}=A-P\), where \(A\) is symmetric and \(P\succeq0\),
then \(Q(\log G)_+Q^T\succeq0\) and
\[
\mathcal E_+'\le
\operatorname{Tr}[(\log G)_+Q^TAQ]
\le2\sqrt{\mathcal E_+}\,\|A\|_{\rm F}.
\]
The first inequality is justified by
\(\operatorname{Tr}(XY)\ge0\) for positive semidefinite \(X,Y\):
it equals \(\operatorname{Tr}(X^{1/2}YX^{1/2})\).
Integrating the upper differential inequality for
\(\sqrt{\mathcal E_++\varepsilon}\), then sending
\(\varepsilon\downarrow0\), gives
\[
\sqrt{\mathcal E_+(V(t))}
\le\sqrt{\mathcal E_+(V(t_0))}
   +\int_{t_0}^t\|A(u)\|_{\rm F}\,du.
\tag{2}
\]
An upper derivative bound is sufficient; an absolute derivative bound is
not asserted. This distinction permits arbitrarily rapid contraction.

## Physical clock and all expanding singular values

On the canonical high-probability primal event specified in
ACTUAL_CLOCK_RANK_ONE_RESPONSE.md, put \(\alpha(t)=2(1-f_n(t))>0\).
The actual physical Jacobian is exactly
\[
D_{\rm phys}(t)=\alpha(t)Db(\theta(t))-\frac2n b(\theta(t))b(\theta(t))^T.
\tag{3}
\]
Apply (2) with \(A=\alpha Db\), \(P=2bb^T/n\), and initial isometry
\(V(t_0)=E\), \(E^TE=I_m\). Since \(ds=\alpha\,dt\), this yields
\[
\sum_{j=1}^m
(\log\sigma_j(U_{\rm phys}(t,t_0)E))_+^2
\le C_B(M,R)^2n[s(t)-s(t_0)]^2
\le C_B(M,R)^2nS_*^2.
\tag{4}
\]
All \(0\le t_0\le t<\infty\), all \(1\le m\le N\), and all initial
isometries are covered on the same event. The constants \(M,R,S_*\)
are independent of width, and this event has probability tending to one
under the prescribed independent Gaussian initialization, including its
nonzero tiny readout. Neither a fixed clock nor exactly zero readout is
substituted. Formula (4) includes the largest singular value.

For decreasingly ordered singular values, the rank-one interlacing
proved in ACTUAL_CLOCK_RANK_ONE_RESPONSE.md gives
\[
\sigma_j(U_{\rm phys}(t,t_0)E)
\ge \sigma_{j+1}(U_{\rm feat}(s(t),s(t_0))E),\qquad 1\le j<m.
\]
Thus the negative logarithmic energy after excluding only the smallest
singular value is bounded by the full feature logarithmic energy:
\[
\sum_{j=1}^{m-1}
(-\log\sigma_j(U_{\rm phys}(t,t_0)E))_+^2
\le C_B(M,R)^2nS_*^2.
\]
Together with (4),
\[
\frac1n\sum_{j=1}^{m-1}
[\log\sigma_j(U_{\rm phys}(t,t_0)E)]^2
\le2C_B(M,R)^2S_*^2.
\tag{5}
\]
For \(m=1\) the last sum is empty, while (4) remains informative.
For every \(r>0\), (4)--(5) imply, respectively,
\[
\#\{j:\log\sigma_j\ge r\}\le C_B^2nS_*^2/r^2,\qquad
\#\{j:|\log\sigma_j|\ge r\}\le1+2C_B^2nS_*^2/r^2.
\tag{6}
\]
The tail count is about logarithmic distortion, not amplitude moments.

## The transformed first-layer metric

Use the orthonormal representation
\(\eta=(F(z^{(1)})/\sqrt n,W^{(2)},W^{(3)},W^{(4)}/\sqrt n)\),
\(F(z)=z+z^3/3\), and the endpoint factors
\[
H_t=\operatorname{diag}(\operatorname{diag}(1+(z_i^{(1)}(t))^2),
                        I_{n^2},I_{n^2},I_n).
\]
The coordinate derivative identity is
\(U_{\eta,\rm phys}=H_tU_{\rm phys}H_{t_0}^{-1}\).
The initial matrix \(H_{t_0}^{-1}E\) has singular values at most one,
so its positive logarithmic energy is zero. Apply (2) along the raw
physical flow and then to the path \(H_t^rV\), \(0\le r\le1\), with
generator \(\log H_t\). Using
\(\|\log H_t\|_{\rm F}\le2\|z^{(1)}(t)\|_2\) gives
\[
\sqrt{\sum_j(\log\sigma_j(U_{\eta,\rm phys}(t,t_0)E))_+^2}
\le C_B\sqrt n[s(t)-s(t_0)]+2\|z^{(1)}(t)\|_2.
\tag{7}
\]
In particular, on the event of ACTUAL_LOG_RESPONSE_METRIC_TRANSFER.md
with \(\|z^{(1)}(u)\|_2/\sqrt n\le R_1\) for all reached \(u\), the
normalized positive energy is at most \((C_BS_*+2R_1)^2\).

Conjugacy preserves the rank-one clock difference. The transformed
feature response has full two-sided logarithmic energy at most
\(n(C_BS_*+4R_1)^2\), by that dependency. Applying the same negative
interlacing argument as above therefore yields
\[
\frac1n\sum_{j=1}^{m-1}
[\log\sigma_j(U_{\eta,\rm phys}(t,t_0)E)]^2
\le(C_BS_*+2R_1)^2+(C_BS_*+4R_1)^2.
\tag{8}
\]
The actual top-column embedding \(E_i u=(0,0,ue_i^T,0)\) is included.
For its independent Gaussian derivative probe in the original
matrix-column scaling \(g/\sqrt n\), the transformed response is
\(U_{\eta,\rm phys}E_i/\sqrt n\); consequently (7)--(8) apply to
\(\sqrt n\) times that response, or to the logarithms of \(n\) times
its nonzero covariance eigenvalues, with the usual factor four for
covariance squared logarithms. No ambient zero eigenvalue is logged.

The expansion-side bound also covers every singular value of the
trained-increment response. For a column seed write
\[
Z_i=(U_{\rm phys}(t,t_0)-I_N)E_i,\qquad
\widetilde Z_i=n^{-1/2}(U_{\eta,\rm phys}(t,t_0)-I_N)E_i.
\]
These are derivatives of the actual state increments for an auxiliary
independent standard Gaussian probe applied to the column coordinates
at the starting state; the second expression retains their transformed
scaling. The trained column itself is not asserted to be independent
Gaussian at that reached state.
For any full-column-rank \(Y\) and isometry \(E\) of the same size,
\((Y-E)^T(Y-E)\preceq2Y^TY+2I_m\). Ordered eigenvalues and
\(\log(3+2u^2)\le\log5+2(\log u)_+\) imply
\[
\sum_{j=1}^m[\log(1+\sigma_j(Y-E)^2)]^2
\le2m(\log5)^2+8\mathcal E_+(Y).
\]
Using (4) and (7) proves, uniformly over all finite physical segments,
\[
\frac1n\sum_{j=1}^n[\log(1+\sigma_j(Z_i)^2)]^2
\le2(\log5)^2+8C_B^2S_*^2,
\tag{8a}
\]
\[
\frac1n\sum_{j=1}^n[\log(1+n\sigma_j(\widetilde Z_i)^2)]^2
\le2(\log5)^2+8(C_BS_*+2R_1)^2.
\tag{8b}
\]
There is no excluded increment singular value, and zero singular values
are allowed by the regularization \(1+\sigma^2\). No implication for
an unregularized logarithm of a zero covariance eigenvalue is intended.

## A contracting extreme really can become unbounded in logarithm

For the full raw square propagator from zero, autonomy gives
\[
U_{\rm phys}(t,0)b(\theta(0))
=\frac{\alpha(t)}{\alpha(0)}b(\theta(t)).
\tag{9}
\]
Indeed differentiating
\(\Psi_t(\Psi_\varepsilon(\theta(0)))=\Psi_{t+\varepsilon}(\theta(0))\)
at \(\varepsilon=0\) gives
\(U_{\rm phys}\alpha(0)b(\theta(0))=\alpha(t)b(\theta(t))\).
All differentiations are at finite width and finite time.

The primal event gives \(\|b(\theta(0))\|_2/\sqrt n\ge b_0>0\)
from its readout-gradient block \(h^{(3)}(0)\).
READOUT_COERCIVITY.md gives
\(\alpha(t)/\alpha(0)\le e^{-2k_0t}\) with \(k_0=b_0^2/4\).
Using the unit direction \(b(\theta(0))/\|b(\theta(0))\|_2\)
in the minimum singular value characterization proves
\[
\sigma_N(U_{\rm phys}(t,0))
\le (K_b/b_0)e^{-2k_0t}.
\tag{10}
\]
Hence a uniform-in-all-physical-time two-sided logarithmic bound with
no excluded direction is impossible even at each fixed width on this
actual event. This is the expected contraction toward zero residual,
not a counterexample to population flow or convergence.
The estimate is for the full square propagator; it need not hold for a
column restriction whose initial subspace misses this direction.

The new information is a complete expansion-side estimate for the
actual flow, with the correct clock and coordinate metric. It still
allows expanding singular values as large as \(\exp(C\sqrt n)\), so
width-uniform response energy, actual source alignment, the clipped
tail envelope, and the full canonical theorem remain open.

Explicit dependencies: ACTUAL_SQUARED_LOG_RESPONSE.md for the raw
Hessian and primal velocity constants; ACTUAL_CLOCK_RANK_ONE_RESPONSE.md
for rectangular interlacing and its canonical all-time primal event;
ACTUAL_LOG_RESPONSE_METRIC_TRANSFER.md for endpoint factors and the
transformed feature estimate; READOUT_COERCIVITY.md for loss decay,
bounded total feature time, and the event's quantitative constants.

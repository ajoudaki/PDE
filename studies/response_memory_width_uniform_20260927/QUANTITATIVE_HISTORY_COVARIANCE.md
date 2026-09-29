# Quantitative Gaussian coupling for empirical history covariance

28 September 2026. Prompt-only standalone lemma for the current study.
Internally derived; no study history, manuscript, external source, or
experiment was consulted. This note proves the covariance estimate under
bounded or exponentially integrable \(H^1\) norm, and disproves it under
only a fourth \(H^1\) moment.

## Conclusions

Let \(H=L^2([0,1];\mathbb R)\), with its ordinary norm, and let \(X\) be a
strongly measurable random element of \(H^1([0,1];\mathbb R)\). The norm is
\[
 \|X\|_{H^1}^2=\int_0^1(|X(t)|^2+|X'(t)|^2)\,dt.
\]
For independent copies \(X_1,\ldots,X_n\), put
\[
 Q=\mathbb E[X\otimes X],\qquad
 Q_n=\frac1n\sum_{i=1}^n X_i\otimes X_i,\qquad
 (x\otimes x)h=x\langle x,h\rangle_H.
 \tag{1}
\]
These are uncentered second-moment operators; \(X\) need not be centered.
All Gaussian laws below are centered and have the displayed covariance.
The Wasserstein cost uses the squared \(L^2\) distance between functions.

The following statements hold.

1. If \(\|X\|_{H^1}\le R\) almost surely, then
   \[
    \mathbb E\,\mathcal W_2^2(N(0,Q_n),N(0,Q))
      \le\frac{R^2\tau}{n},\qquad
    \tau=1+\sum_{j=1}^{\infty}\frac1{1+\pi^2j^2}
      \le1+\frac2{\pi^2}.
    \tag{2}
   \]
2. If, for some \(c,\alpha,M>0\),
   \[
    \mathbb E\exp(c\|X\|_{H^1}^{\alpha})\le M,
    \tag{3}
   \]
   then
   \[
    \mathbb E\,\mathcal W_2^2(N(0,Q_n),N(0,Q))
       \le C(c,\alpha,M)\,
          \frac{(\log(en))^{2/\alpha}}n.
    \tag{4}
   \]
3. The hypothesis \(\mathbb E\|X\|_{H^1}^4<\infty\) alone does not imply
   \(O(n^{-1}\log^k(en))\) for any fixed \(k\). A fixed law with bounded
   pointwise values and uniformly bounded pointwise derivative fourth
   moments has expected squared Gaussian Wasserstein error
   \(\Theta(n^{-5/6})\).

No relative-coordinate-kurtosis condition occurs in (2) or (4). The proof
uses the entire \(H^1\) ellipsoid, not bounds on individual covariance
eigenvectors. The independence assumption in (1) is substantive: this
lemma does not establish independence of trained neuron histories, nor
does it justify conditioning on adaptively queried histories.
The exponential Sobolev bound and the pointwise sufficient conditions
below are separate hypotheses, not conclusions about network source
histories. In particular, applying an operator bounded on \(L^2\) to a
derivative field does not by itself preserve its higher \(L^p\) bounds;
deeper-layer histories require their own response estimates.

## 1. A finite-dimensional covariance inequality

Let \(B\) be a positive definite \(d\times d\) matrix, let \(A\) be
positive semidefinite, and set \(\Delta=A-B\). In an orthonormal
eigenbasis of \(B\), write its eigenvalues as \(\lambda_i>0\). Then
\[
 \mathcal W_2^2(N(0,A),N(0,B))
 \le 2\sum_{i,j=1}^d
       \frac{|\Delta_{ij}|^2}{\lambda_i+\lambda_j}.
 \tag{5}
\]

Here is a derivation without a Gaussian optimal-transport formula.
For \(0\le s<1\), set \(C_s=(1-s)B+sA\), so \(C_s\succ0\).
On real symmetric matrices, with Frobenius inner product, define
\[
 \mathcal L_C(U)=UC+CU.
\]
This is a positive definite self-adjoint operator when \(C\succ0\).
Let \(U_s=\mathcal L_{C_s}^{-1}(\Delta)\), and solve the linear ODE
\[
 \frac{dY_s}{ds}=U_sY_s,\qquad Y_0\sim N(0,B).
 \tag{6}
\]
On every closed subinterval of \([0,1)\), its coefficients are continuous.
The solution is centered Gaussian. Its covariance solves
\(S_s'=U_sS_s+S_sU_s\). The matrix \(C_s\) solves the same equation and
has the same initial value, because
\(\mathcal L_{C_s}(U_s)=\Delta=C_s'\). Uniqueness for this finite
linear ODE gives \(\operatorname{Cov}(Y_s)=C_s\).

Its squared speed in \(L^2\) of the auxiliary probability space is
\[
 \mathbb E\|Y_s'\|_2^2
 =\operatorname{Tr}(U_sC_sU_s)
 =\frac12\langle\Delta,\mathcal L_{C_s}^{-1}\Delta\rangle_F.
 \tag{7}
\]
Since \(C_s\succeq(1-s)B\), for every symmetric \(U\),
\[
 \langle U,\mathcal L_{C_s}U\rangle_F
 =2\operatorname{Tr}(U^2C_s)
 \ge(1-s)\langle U,\mathcal L_BU\rangle_F.
\]
Consequently
\[
 \langle\Delta,\mathcal L_{C_s}^{-1}\Delta\rangle_F
 \le\frac1{1-s}
       \langle\Delta,\mathcal L_B^{-1}\Delta\rangle_F.
 \tag{8}
\]
One can verify this inverse inequality directly from
\(\langle v,T^{-1}v\rangle
 =\sup_z\{2\langle v,z\rangle-\langle z,Tz\rangle\}\)
for a positive definite self-adjoint operator \(T\).

In the chosen eigenbasis,
\[
 S:=\langle\Delta,\mathcal L_B^{-1}\Delta\rangle_F
   =\sum_{i,j}\frac{|\Delta_{ij}|^2}{\lambda_i+\lambda_j}.
\]
Minkowski's integral inequality and (7)--(8) show
\[
 \|Y_t-Y_s\|_{L^2}
 \le \sqrt{S/2}\int_s^t(1-u)^{-1/2}\,du.
 \tag{9}
\]
The right side tends to zero as \(s,t\uparrow1\), so \(Y_s\) has an
\(L^2\) limit \(Y_1\). Its law is \(N(0,A)\), since its Gaussian
covariances tend to \(A\). The coupling \((Y_0,Y_1)\) has cost at most
\[
 \left(\sqrt{S/2}\int_0^1(1-u)^{-1/2}\,du\right)^2=2S.
\]
This proves (5), including singular \(A\).

## 2. Bounded Sobolev norm gives the \(1/n\) rate

Use the real orthonormal cosine basis
\[
 e_0(t)=1,\qquad e_j(t)=\sqrt2\cos(\pi jt),\quad j\ge1.
\]
Define the positive operator \(D\) by
\[
 De_j=\sqrt{1+\pi^2j^2}\,e_j,\qquad K=D^{-2}.
 \tag{10}
\]
Its domain is \(H^1([0,1])\), and
\[
 \|Df\|_H^2=\|f\|_{H^1}^2,\qquad \operatorname{Tr}K=\tau<\infty.
 \tag{11}
\]
To check the norm identity, integrate by parts against
\(\sqrt2\sin(\pi jt)\): its boundary values vanish and the resulting
derivative coefficient is \(-\pi j\langle f,e_j\rangle\).
Parseval for the cosine basis for \(f\) and the sine basis for \(f'\)
gives (11), first for smooth functions and then by \(H^1\) approximation.
The trace bound in (2) follows from
\(\sum_{j\ge1}j^{-2}\le1+\int_1^\infty u^{-2}du=2\).

Assume \(\|DX\|_H\le R\) almost surely. Since
\(\operatorname{Tr}Q=\mathbb E\|X\|_H^2<\infty\), the positive compact
operator \(Q\) has an orthonormal eigenbasis on its support. Write its
positive eigenvalues and eigenvectors as \((\lambda_i,u_i)\), and set
\(x_i=\langle X,u_i\rangle\). Let \(P_N\) project onto the first \(N\)
positive-eigenvalue eigenvectors. Finite rank is handled by stopping at
its rank. Components in the kernel of \(Q\) vanish almost surely because
their second moments vanish.

Apply (5) to the projected covariance pair. Independence of the samples
gives
\[
 \begin{aligned}
 &\mathbb E\,\mathcal W_2^2
   (N(0,P_NQ_nP_N),N(0,P_NQP_N))\\
 &\qquad\le\frac2n
     \sum_{i,j\le N}
       \frac{\mathbb E[x_i^2x_j^2]}{\lambda_i+\lambda_j}.
 \end{aligned}
 \tag{12}
\]
Indeed each empirical covariance entry has variance
\(n^{-1}(\mathbb E[x_i^2x_j^2]-Q_{ij}^2)\), and dropping the final
nonnegative term gives (12).

The essential estimate is
\[
 \sum_{i,j\le N}
       \frac{\mathbb E[x_i^2x_j^2]}{\lambda_i+\lambda_j}
 \le\frac{R^2}{2}\operatorname{Tr}(KP_N).
 \tag{13}
\]
For \(t\ge0\), define
\(A_t=\sum_{i\le N}e^{-t\lambda_i}u_i\otimes u_i\).
Using the integral of \(e^{-t(\lambda_i+\lambda_j)}\), the left side
of (13) is exactly
\[
 \int_0^\infty\mathbb E\langle X,A_tX\rangle_H^2\,dt.
 \tag{14}
\]
The Sobolev constraint enters through a single Cauchy--Schwarz inequality:
\[
 \begin{aligned}
 \langle X,A_tX\rangle_H^2
 &=\langle DX,D^{-1}A_tX\rangle_H^2\\
 &\le R^2\langle X,A_tKA_tX\rangle_H.
 \end{aligned}
 \tag{15}
\]
This identity is valid even if \(u_i\) do not belong to the domain of
\(D\): \(X\) does, and \(D^{-1}\) is bounded on \(H\). In particular
no regularity of covariance eigenvectors is being assumed.

Taking expectations, cycling the finite-rank trace, and integrating gives
\[
 \begin{aligned}
 \int_0^\infty\mathbb E\langle X,A_tX\rangle_H^2\,dt
 &\le R^2\int_0^\infty\operatorname{Tr}(KA_tQA_t)\,dt\\
 &=R^2\sum_{i\le N}\langle u_i,Ku_i\rangle
           \int_0^\infty\lambda_i e^{-2t\lambda_i}\,dt\\
 &=\frac{R^2}{2}\operatorname{Tr}(KP_N)
 \le\frac{R^2\tau}{2}.
 \end{aligned}
 \tag{16}
\]
Together with (12), this proves (2) for the projected laws.

For completeness, these projected Wasserstein distances converge to the
full distance almost surely. If \(G\) is any centered Gaussian with
trace-class covariance \(C\), the coupling \((G,P_NG)\) gives
\[
 \mathcal W_2^2(N(0,C),N(0,P_NCP_N))
 \le \operatorname{Tr}((I-P_N)C).
 \tag{17}
\]
For \(C=Q\) this trace tends to zero; for \(C=Q_n\) it is
\(n^{-1}\sum_i\|(I-P_N)X_i\|_H^2\), which tends to zero almost surely.
The triangle inequality therefore gives the asserted convergence.
Fatou's lemma passes the uniform upper bound \(R^2\tau/n\) to the full
expected squared distance. This completes the proof of (2).

The same argument works in any separable Hilbert space with an
ellipsoidal constraint \(\|DX\|\le R\), provided \(D^{-1}\) is bounded
and \(\operatorname{Tr}(D^{-2})<\infty\).

## 3. Exponential tails and pointwise sufficient conditions

Write \(Z=\|X\|_{H^1}\), and truncate the entire history by
\[
 X^{[R]}=X\,\mathbf1_{\{Z\le R\}}.
 \tag{18}
\]
Let \(Q^{[R]},Q_n^{[R]}\) be its population and empirical second-moment
operators using the same samples. Because the retained and removed
parts are disjoint,
\[
 Q=Q^{[R]}+Q^{>R},\qquad Q_n=Q_n^{[R]}+Q_n^{>R},
 \tag{19}
\]
with all four summands positive semidefinite. Coupling a Gaussian with
covariance \(Q^{[R]}\) to itself plus an independent Gaussian with
covariance \(Q^{>R}\) shows that the squared coupling cost is at most
\[
 T(R):=\mathbb E[\|X\|_H^2\mathbf1_{\{Z>R\}}]
 \le\mathbb E[Z^2\mathbf1_{\{Z>R\}}].
 \tag{20}
\]
The empirical version has cost \(\operatorname{Tr}Q_n^{>R}\), whose
expectation is \(T(R)\). The triangle inequality, followed by
\((a+b+c)^2\le3(a^2+b^2+c^2)\), and (2) give
\[
 \mathbb E\,\mathcal W_2^2(N(0,Q_n),N(0,Q))
 \le \frac{3R^2\tau}{n}+6T(R).
 \tag{21}
\]

Under (3), put
\[
 B_{c,\alpha}
 =\sup_{z\ge0}z^2e^{-cz^\alpha/2}
 =\left(\frac4{c\alpha e}\right)^{2/\alpha}.
 \tag{22}
\]
For \(z>R\),
\(z^2e^{-cz^\alpha}\le B_{c,\alpha}e^{-cR^\alpha/2}\).
Multiplication by \(e^{cZ^\alpha}\) and expectation yield
\[
 T(R)\le M B_{c,\alpha}e^{-cR^\alpha/2}.
 \tag{23}
\]
Choose \(R=(4\log(en)/c)^{1/\alpha}\). Formula (21) becomes the explicit
bound
\[
 \mathbb E\,\mathcal W_2^2(N(0,Q_n),N(0,Q))
 \le
 \frac{3\tau(4/c)^{2/\alpha}(\log(en))^{2/\alpha}}n
 +\frac{6M B_{c,\alpha}}{e^2n^2},
 \tag{24}
\]
which proves (4).

Uniform pointwise subGaussian bounds on both \(X\) and its weak derivative
are one sufficient way to obtain (3) with \(\alpha=2\). Specifically, if
for almost every \(t\),
\[
 \mathbb E e^{2c|X(t)|^2}\le M,\qquad
 \mathbb E e^{2c|X'(t)|^2}\le M,
 \tag{25}
\]
then Jensen on the unit time interval and
\(e^{a+b}\le(e^{2a}+e^{2b})/2\) give
\[
 \mathbb E e^{c\|X\|_{H^1}^2}
 \le\int_0^1\mathbb E e^{c(|X(t)|^2+|X'(t)|^2)}\,dt
 \le M.
 \tag{26}
\]
No independence between times or between value and derivative is needed.

More generally, suppose that for all \(p\ge2\) and almost every \(t\),
\[
 (\mathbb E|X(t)|^p)^{1/p}\le Bp^{1/\alpha},\qquad
 (\mathbb E|X'(t)|^p)^{1/p}\le Bp^{1/\alpha}.
 \tag{27}
\]
Minkowski's integral inequality with exponent \(p/2\) gives
\[
 (\mathbb E\|X\|_{H^1}^p)^{1/p}
 \le\sqrt2\,B p^{1/\alpha}.
 \tag{28}
\]
This implies (3) for sufficiently small positive \(c\), depending only on
\(B,\alpha\). To check it directly, expand the exponential in powers of
\(Z^\alpha\). For integers \(k\) with \(\alpha k\ge2\), (28) and
\(k!\ge(k/e)^k\) bound its \(k\)-th term by
\[
 \frac{c^k\mathbb EZ^{\alpha k}}{k!}
 \le [c(\sqrt2B)^\alpha\alpha e]^k.
 \tag{29}
\]
Choose the bracket smaller than one. The finitely many remaining terms
are finite by the second moment and the inequality
\(z^q\le1+z^2\) for \(0<q<2\). Thus uniform subWeibull moment growth of
the values and derivatives also suffices, with no temporal independence.
In contrast, one fixed derivative moment, even the fourth, does not.

## 4. A fixed-law counterexample under only a fourth moment

For \(j\ge1\), use \(e_j(t)=\sqrt2\cos(\pi jt)\), and set
\[
 a=\left(\sum_{j=1}^\infty j^{-6}\right)^{-1},\qquad
 p_j=aj^{-6}.
 \tag{30}
\]
Let \(J\) have probabilities \(p_j\), let \(\varepsilon\) be an independent
uniform random sign, and put
\[
 X=\varepsilon e_J.
 \tag{31}
\]
Every realization is smooth and \(X\) is centered. Moreover,
\[
 \mathbb E\|X\|_{H^1}^4
 =a\sum_{j\ge1}j^{-6}(1+\pi^2j^2)^2<\infty,
 \tag{32}
\]
since the summand is \(O(j^{-2})\). Its values satisfy
\(|X(t)|\le\sqrt2\) for every realization and time. Its derivatives obey
\[
 \sup_{t\in[0,1]}\mathbb E|X'(t)|^4
 \le4\pi^4a\sum_{j\ge1}j^{-2}<\infty.
 \tag{33}
\]
Thus bounded values and a uniform pointwise derivative fourth-moment
bound do not rescue the requested rate.

Let \(N_j\) count observations whose frequency is \(j\). The empirical
and population covariance operators are simultaneously diagonal:
\[
 Q=\sum_{j\ge1}p_j e_j\otimes e_j,\qquad
 Q_n=\sum_{j\ge1}\frac{N_j}{n}e_j\otimes e_j.
 \tag{34}
\]
Their exact squared Gaussian Wasserstein distance is
\[
 \mathcal W_2^2(N(0,Q_n),N(0,Q))
 =\sum_{j\ge1}
       \left(\sqrt{N_j/n}-\sqrt{p_j}\right)^2.
 \tag{35}
\]
For a proof, in any coupling each coordinate's covariance is at most
the geometric mean of its variances, by Cauchy--Schwarz. Summing the
resulting coordinate cost lower bounds gives the right side. Equality
is attained by using the same independent standard Gaussians as
coordinates for both laws, scaled respectively by
\(\sqrt{N_j/n}\) and \(\sqrt{p_j}\). These series converge in \(L^2\)
because both covariance traces are one.

If \(p_j\le1/(2n)\), the missing-coordinate event has probability
\[
 \mathbb P(N_j=0)=(1-p_j)^n\ge1-np_j\ge\frac12.
 \tag{36}
\]
On this event its summand in (35) is \(p_j\). With
\(k_n=\lceil(2an)^{1/6}\rceil\), Tonelli therefore gives
\[
 \begin{aligned}
 \mathbb E\,\mathcal W_2^2(N(0,Q_n),N(0,Q))
 &\ge\frac a2\sum_{j\ge k_n}j^{-6}\\
 &\ge\frac a{10}k_n^{-5}
 \ge c_0 n^{-5/6}
 \end{aligned}
 \tag{37}
\]
for an absolute \(c_0>0\). The second inequality integrates \(u^{-6}\)
from \(k_n\) to infinity. The final bound follows because
\(k_n\le2(2an)^{1/6}\) for \(n\ge1\); indeed
\(\sum j^{-6}\le6/5\), so \(a\ge5/6\).

There is a matching upper bound. For a binomial \(N\) with parameters
\(n,p\),
\[
 \mathbb E(\sqrt{N/n}-\sqrt p)^2
 \le 2p,\qquad
 \mathbb E(\sqrt{N/n}-\sqrt p)^2
 \le\frac{\mathbb E(N/n-p)^2}{p}
 =\frac{1-p}{n}\le\frac1n.
 \tag{38}
\]
The first inequality expands the square and drops its nonnegative
cross term; the second uses
\((\sqrt u-\sqrt p)^2=(u-p)^2/(\sqrt u+\sqrt p)^2\).
Splitting the sum at \(\lfloor n^{1/6}\rfloor\) gives
\[
 \mathbb E\,\mathcal W_2^2(N(0,Q_n),N(0,Q))
 \le\sum_{j\ge1}\min(2aj^{-6},n^{-1})
 \le C_0n^{-5/6}.
 \tag{39}
\]
For the tail use
\(\sum_{j>M}j^{-6}\le(5M^5)^{-1}\) and
\(\lfloor n^{1/6}\rfloor\ge n^{1/6}/2\).

This one fixed distribution therefore contradicts an
\(O(n^{-1}\log^k(en))\) bound for every fixed \(k\), even if the bound's
constant were allowed to depend on this entire distribution rather than
only its fourth moment. Multiplying \(X\) by a fixed positive scalar
can enforce any specified positive upper bound on that fourth moment
without changing the rate exponent.

The example does not satisfy (3) for any positive \(\alpha\):
\(\|e_j\|_{H^1}=\sqrt{1+\pi^2j^2}\), and polynomial probabilities
cannot integrate its positive exponential powers. Its derivative is
also not pointwise subGaussian: at \(t=1/2\), odd \(j\) have
\(|e_j'(1/2)|=\sqrt2\pi j\), so
\(\mathbb E e^{b|X'(1/2)|^2}=\infty\) for every \(b>0\).
It therefore leaves the stronger covariance estimate (4), and any
network application satisfying its hypotheses, intact.

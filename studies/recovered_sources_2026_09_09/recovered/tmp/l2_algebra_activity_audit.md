# Independent algebra/activity audit: the (L=2), one-sample arctan construction

## 1. Raw model, scaling, and exact normalized dynamics

For

\[
A_i=W_i^{(1)},\qquad B_{ji}=W_{ji}^{(2)},\qquad c_j=W_j^{(3)},
\]

put

\[
H=\arctan A,\quad S=BH,\quad G=\arctan S,\quad
C=nc,\quad q(x)=(1+x^2)^{-1},
\]

and use \(\langle u,v\rangle_n=n^{-1}u^Tv\). Then

\[
f=\langle C,G\rangle_n,\qquad e=f-1,
\qquad D=C\odot q(S).
\]

The proposed initialization and mobilities are

\[
A_i(0)\sim N(0,1),\quad B_{ji}(0)\sim N(0,n^{-1}),
\quad c_j(0)\sim N(0,n^{-4}),
\]

\[
\lambda_1=n,\qquad \lambda_2=1,\qquad \lambda_3=n^{-1},
\qquad \eta_{0,n}=n^{-2}.
\]

Thus \(C_j(0)\sim N(0,n^{-2})\), where the displayed number is the
variance. Direct differentiation gives

\[
\partial_{A_i}f={1\over n}q(A_i)(B^TD)_i,\qquad
\partial_{B_{ji}}f={1\over n}D_jH_i,\qquad
\partial_{c_j}f=G_j.
\]

Consequently, on the clock \(t=k\eta_{0,n}\), one exact GD step is one
Euler step of

\[
\dot A=-2e\,q(A)\odot B^TD,\qquad
\dot B=-2e\,D\otimes_n H,\qquad
\dot C=-2e\,G,
\tag{1}
\]

where \(u\otimes_n v=uv^T/n\). There is no missing factor of \(n\).
Also \(\eta_{0,n}\lambda_1=n^{-1}\),
\(\eta_{0,n}\lambda_2=n^{-2}\), and
\(\eta_{0,n}\lambda_3=n^{-3}\), so all raw step sizes tend to zero.

The three raw-parameter kernel blocks are exactly

\[
K_1=\|q(A)\odot B^TD\|_n^2,
\quad K_2=\|H\|_n^2\|D\|_n^2,
\quad K_3=\|G\|_n^2.
\tag{2}
\]

Hence

\[
\dot f=-2e(K_1+K_2+K_3),\qquad
\dot L=-4e^2(K_1+K_2+K_3).
\tag{3}
\]

Differentiating \(S=BH\) in (1) yields the exact identity

\[
\dot S=-2e\left[\|H\|_n^2D+B\{q(A)^2\odot B^TD\}\right].
\tag{4}
\]

## 2. Initial Gaussian law and the reused-transpose response

Let

\[
m=\mathbb E[\arctan(Z_1)^2]>0,\qquad Z_1\sim N(0,1).
\]

At initialization, the second preactivation converges to
\(Z\sim N(0,m)\). Define

\[
U(z)={\arctan z\over 1+z^2},\qquad
\nu=\mathbb E[U(Z)^2]>0,\qquad
\kappa=\mathbb E[U'(Z)].
\tag{5}
\]

The exact Gaussian row decomposition proves the required reused-adjoint
law without an appeal to a heuristic cavity rule. Conditional on
\(H\), write \(s_j=b_j^TH\) and

\[
b_j={s_j\over\|H\|_{\mathrm E}^2}H+\widetilde b_j,
\]

where \(\widetilde b_j\), conditional on \(H\), is independent of
\(s_j\) and Gaussian with covariance \(n^{-1}P_H^\perp\). Therefore

\[
B^TU(S)=a_nH+\sqrt{\nu_n}\,P_H^\perp\Gamma,
\quad
a_n={\sum_js_jU(s_j)\over nm_n},
\quad \nu_n={1\over n}\sum_jU(s_j)^2,
\tag{6}
\]

in conditional law, where \(m_n=\|H\|_n^2\) and
\(\Gamma\sim N(0,I_n)\) is independent. The laws of large numbers and
Gaussian integration by parts give

\[
a_n\longrightarrow {\mathbb E[ZU(Z)]\over m}
=\mathbb E[U'(Z)]=\kappa,
\qquad \nu_n\longrightarrow\nu.
\]

Moreover, \(P_H^\perp\Gamma-\Gamma\to0\) in normalized empirical
\(L^2\), because \(\langle H,\Gamma\rangle_n=O_{\mathbb P}(n^{-1/2})\).
Thus the joint empirical limit is

\[
\Xi=B_0^*U=\kappa H+\sqrt\nu\,\Gamma,
\tag{7}
\]

where \(\Gamma\sim N(0,1)\) is independent of the initial
\(A\sim N(0,1)\). This confirms both the innovation and response terms.

Set

\[
d=\mathbb E[q(A)^2\Xi^2]
=\nu\,\mathbb E q(A)^2
+\kappa^2\mathbb E[q(A)^2\arctan(A)^2].
\tag{8}
\]

Since \(\nu>0\) and \(q>0\), \(d>0\), regardless of the sign or
possible vanishing of \(\kappa\). This rules out cancellation in the
first hidden layer.

## 3. Node-by-node small-time expansion of the limiting flow

At time zero the limiting output mark is \(C(0)=0\), hence
\(e(0)=-1\), while \(S(0)=Z\). Put

\[
k_3=\mathbb E[\arctan(Z)^2]>0,
\qquad
\mathcal R=mI+B_0M_{q(A)^2}B_0^*.
\tag{9}
\]

Here \(M_{q(A)^2}\) denotes coordinate multiplication. From (1),

\[
C(t)=2t\arctan Z+O(t^2),\qquad
D(t)=2tU+O(t^2).
\tag{10}
\]

It follows, in the limiting right and left \(L^2\) spaces, that

\[
A(t)=A+2t^2q(A)\Xi+o(t^2),
\tag{11}
\]

\[
B(t)=B_0+2t^2U\otimes H+o_{\mathrm{op}}(t^2),
\tag{12}
\]

and, either from (4) or by differentiating \(BH(A)\) twice,

\[
S(t)=Z+2t^2\mathcal R U+o(t^2).
\tag{13}
\]

All constants and signs in (10)--(13) follow from
\(\dot D(0)=2U\), \(A''(0)=4q(A)B_0^*U\),
\(B''(0)=4U\otimes H\), and

\[
S''(0)=4\{mU+B_0[q(A)^2B_0^*U]\}=4\mathcal RU.
\]

The operator \(\mathcal R\) is positive and

\[
\langle U,\mathcal RU\rangle
=m\nu+\langle B_0^*U,q(A)^2B_0^*U\rangle
=m\nu+d>0.
\tag{14}
\]

Therefore \(\mathcal RU\ne0\). This excludes cancellation in the
second hidden layer.

## 4. Velocities, displacements, kernels, and operator motion

Equations (11)--(13) give

\[
V_1(t)^2=16dt^2+o(t^2),\qquad
V_2(t)^2=16\|\mathcal RU\|_2^2t^2+o(t^2),
\tag{15}
\]

and

\[
\mathbb E|A(t)-A(0)|^2=4dt^4+o(t^4),
\]

\[
\mathbb E|S(t)-S(0)|^2
=4\|\mathcal RU\|_2^2t^4+o(t^4).
\tag{16}
\]

The middle operator has genuine action-scale motion:

\[
\|B(t)-B_0\|_{\mathrm{op}}
=2t^2\sqrt{m\nu}+o(t^2),
\tag{17}
\]

because \(\|U\otimes H\|_{\mathrm{op}}=\|U\|_2\|H\|_2\).

The kernel blocks have the expansions

\[
K_1(t)=4dt^2+o(t^2),\qquad
K_2(t)=4m\nu t^2+o(t^2),
\tag{18}
\]

\[
K_3(t)=k_3+4(m\nu+d)t^2+o(t^2).
\tag{19}
\]

For (19), use
\(\arctan S(t)=\arctan Z+2t^2q(Z)\mathcal RU+o(t^2)\) and
\(U=\arctan(Z)q(Z)\), followed by (14). Hence

\[
K(t)=k_3+8(m\nu+d)t^2+o(t^2).
\tag{20}
\]

The coefficient is strictly positive. Thus, for every sufficiently
small \(T>0\), all three block integrals are finite and strictly
positive, and the total kernel is nonconstant on \([0,T]\).

Finally,

\[
f(t)=2k_3t+o(t),\qquad
L(t)=1-4k_3t+o(t),
\tag{21}
\]

so the loss strictly decreases for every sufficiently small positive
endpoint.

## 5. Variance and nonlinear residual

Initially the two hidden laws are \(N(0,1)\) and \(N(0,m)\), with
strictly positive finite variances. Variance is continuous in
Wasserstein-2, so both remain positive on a sufficiently short common
interval.

For a law \(\mu\) of positive variance, the squared affine-regression
residual of \(g(z)=\arctan z\) equals

\[
\operatorname{Var}_\mu(g)
-{\operatorname{Cov}_\mu(z,g)^2\over\operatorname{Var}_\mu(z)}.
\tag{22}
\]

It is strictly positive at either initial nondegenerate Gaussian law:
otherwise continuity would force \(\arctan z=az+b\) on all of
\(\mathbb R\), which is false. The five moments in (22) are continuous
under \(W_2\) convergence. The only nonbounded one is
\(\mathbb E[Z\arctan Z]\); for an optimal \(W_2\) coupling,

\[
|\mathbb E[X\arctan X-Y\arctan Y]|
\le {\pi\over2}\|X-Y\|_2+\|Y\|_2\|X-Y\|_2.
\]

Thus both nonlinear residuals stay strictly positive on a sufficiently
short interval and have positive time integrals.

## Verdict of this audit

The finite-width algebra, all powers of \(n\), all signs, the
reused-transpose response, and every stated small-time nondegeneracy
coefficient are correct. None of the activity claims can fail through
a cancellation: the independent innovation yields \(d>0\), and the
strictly positive \(mI\) part of \(\mathcal R\) yields
\(\mathcal RU\ne0\).

This audit does **not** by itself prove compact-time action-law
convergence, cutoff removal, uniqueness/restartability, or the joint
exact-GD diagonal limit. Those are separate analytical obligations.
The conclusions above are rigorous once that limiting flow and the
stated \(W_2\)/operator differentiability have independently been
established.

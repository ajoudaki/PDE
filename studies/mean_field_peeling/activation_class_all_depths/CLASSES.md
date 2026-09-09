# Part A. Uniform activation classes and depth-uniform nonaffinity

Fix the three-input separation parameter \(\delta>0\), and set
\[
\lambda=\delta^2/16,\qquad T_0=12/\lambda.
\]
Let
\[
\mathcal B=\left\{\psi\in C_b^2(\mathbb R):
          \max_{k=0,1,2}\|\psi^{(k)}\|_\infty\le1\right\},
\qquad
\phi(z)=a(1+z)+e\psi(z),\quad 0<e\le1.
\]
Here \(C_b^2(\mathbb R)\) consists of twice continuously differentiable real functions with bounded derivatives of orders zero, one, and two, and carries the displayed maximum norm. Throughout, \(e\) is fixed when comparing depths.

The main theorem supplies, for each fixed finite hidden depth \(L\ge2\), its global strong physical trajectory and the estimate
\[
\max_{i,\ 1\le\ell\le L}\sup_{t\ge0}
 \|z_i^\ell(t)-z_i^\ell(0)\|_2
\le d_L,\qquad
d_L=3\sqrt L\left(\frac{32768}{a}\right)^L\frac{T_0^2}{a}.
                                                               \tag{A.1}
\]
Its function-independent dynamical estimates require
\(a\ge10^{12}(1+T_0)\). This appendix proves exactly how one can choose the remaining gain condition uniformly over classes of functions, and when the nonaffinity lower bound can also be uniform over depth. All constants selected below depend only on \(\delta\) and the specified class, and not on \(L\), the dataset, time, or the fixed \(e\in(0,1]\).

## A.1. Elementary regression estimates

For a square-integrable real random variable \(X\), define
\[
\mathcal R_\psi(X)=\inf_{\alpha,\beta\in\mathbb R}
                       E[\psi(X)-\alpha-\beta X]^2.
\]
The infimum is attained. If \(\operatorname{Var}(X)>0\), direct completion of squares gives an optimal slope
\[
\beta_X=\frac{\operatorname{Cov}(X,\psi(X))}
                     {\operatorname{Var}(X)},\qquad
\alpha_X=E\psi(X)-\beta_XEX.
\]
When \(X\) is almost surely constant, choose \(\beta_X=0\) and
\(\alpha_X=\psi(X)\).

For \(\psi\in\mathcal B\), its Lipschitz constant is at most one. If \(X'\) is an independent copy of \(X\), expansion and independence give
\[
\operatorname{Cov}(X,\psi(X))
=\tfrac12E[(X-X')(\psi(X)-\psi(X'))],
\qquad E[(X-X')^2]=2\operatorname{Var}(X).
\]
Consequently \(|\beta_X|\le1\). In particular optimal slopes need not be positive, but they remain in the fixed interval \([-1,1]\).

For two square-integrable variables \(X,Y\) on a common probability space, use the optimal affine fit at \(Y\) as a competitor at \(X\). The triangle inequality and \(|\beta_Y|\le1\) give
\[
\begin{aligned}
\sqrt{\mathcal R_\psi(X)}
&\le\|\psi(X)-\alpha_Y-\beta_YX\|_2\\
&\le\sqrt{\mathcal R_\psi(Y)}
       +\|\psi(X)-\psi(Y)-\beta_Y(X-Y)\|_2\\
&\le\sqrt{\mathcal R_\psi(Y)}+2\|X-Y\|_2.
\end{aligned}
\]
Interchanging \(X,Y\) proves the useful stability estimate
\[
\left|\sqrt{\mathcal R_\psi(X)}
       -\sqrt{\mathcal R_\psi(Y)}\right|
                         \le2\|X-Y\|_2.                 \tag{A.2}
\]

At a fixed \(X\), the corresponding estimate for changing the function is
\[
\left|\sqrt{\mathcal R_\psi(X)}
       -\sqrt{\mathcal R_\chi(X)}\right|
\le\|\psi(X)-\chi(X)\|_2\le\|\psi-\chi\|_\infty.          \tag{A.3}
\]
Indeed test each regression problem with an optimal affine fit for the other and use the triangle inequality. This estimate does not require bounds on the derivatives.

Finally the affine part of \(\phi\) can be absorbed exactly into the free regression coefficients. Since \(e>0\), the substitutions
\(\widetilde\alpha=(\alpha-a)/e\) and
\(\widetilde\beta=(\beta-a)/e\) range over all real pairs. Thus
\[
\inf_{\alpha,\beta}E[\phi(X)-\alpha-\beta X]^2
                              =e^2\mathcal R_\psi(X).    \tag{A.4}
\]

## A.2. Finite-interval margins and a common gain

For \(r\ge1\), put
\[
J_r(\psi)=\inf_{\alpha,\beta}
                   \int_{-r}^r[\psi(x)-\alpha-\beta x]^2\,dx.
\]
The functions \(1,x\) are orthogonal on this interval and have squared norms \(2r,2r^3/3\). Completing squares therefore gives
\[
J_r(\psi)=\int_{-r}^r\psi(x)^2\,dx
 -\frac1{2r}\left(\int_{-r}^r\psi(x)\,dx\right)^2
 -\frac3{2r^3}\left(\int_{-r}^r x\psi(x)\,dx\right)^2.     \tag{A.5}
\]
In particular the infimum is attained. It is zero exactly when
\(\psi\) equals an affine function almost everywhere on \([-r,r]\); continuity then gives equality everywhere on that interval.

Every bounded nonconstant \(\psi\in C^2(\mathbb R)\) has some \(r\ge1\) with \(J_r(\psi)>0\). Otherwise its restrictions to all intervals \([-n,n]\), for positive integers \(n\), would be affine. These affine functions agree on their overlapping intervals, so their two coefficients agree. Thus \(\psi\) would be affine on all of \(\mathbb R\), and boundedness would make it constant, a contradiction.

Fix any such interval, and define
\[
c_\psi=\frac{e^{-r^2/2}J_r(\psi)}{\sqrt{2\pi}}>0.         \tag{A.6}
\]
For \(G\sim N(0,1)\) and \(\sigma\ge1\), its scaled density on \([-r,r]\) obeys
\[
\frac1{\sigma\sqrt{2\pi}}
        e^{-x^2/(2\sigma^2)}
\ge\frac{e^{-r^2/2}}{\sigma\sqrt{2\pi}}.
\]
Applying this pointwise lower bound to every squared affine-regression error and then taking the infimum proves
\[
                    \mathcal R_\psi(\sigma G)
                                  \ge c_\psi/\sigma.    \tag{A.7}
\]

We record the initialized variance bounds used with (A.7). Write
\(z_i^\ell(0)\overset d=\sigma_\ell G\). All samples have the same marginal variance at a fixed layer, and \(\sigma_1=1\). The recursion of the initialized Gaussian program is
\[
\sigma_{\ell+1}=\|\phi(\sigma_\ell G)\|_2.
\]
Integration by parts gives the coefficient of the projection of
\(\phi(\sigma G)\) onto \(G\):
\[
E[G\phi(\sigma G)]
=\sigma E[\phi'(\sigma G)]\ge(a-e)\sigma.
\]
Its absolute value is bounded by the \(L^2\) norm of the feature, because \(\|G\|_2=1\). Thus
\[
\sigma_\ell\ge(a-e)^{\ell-1}
                          \ge(a/2)^{\ell-1}\ge1,         \tag{A.8}
\]
where \(a\ge4\) and \(e\le1\) suffice. For an upper bound, the triangle inequality gives
\[
\sigma_{\ell+1}
\le a\sqrt{1+\sigma_\ell^2}+e
\le a\sigma_\ell+2a.
\]
Dividing by \(a^\ell\), summing this scalar recurrence, and using \(a\ge4\) gives
\[
\frac{\sigma_\ell}{a^{\ell-1}}
\le1+2\sum_{k=0}^{\ell-2}a^{-k}
\le1+\frac2{1-a^{-1}}\le\frac{11}{3}<4.
\]
Hence
\[
                     1\le\sigma_\ell\le4a^{\ell-1}.      \tag{A.9}
\]
The first-layer upper bound also follows directly from \(\sigma_1=1\).

Select
\[
a=\max\left\{10^{12}(1+T_0),
       \left(\frac{2^{36}T_0^2}{\sqrt{c_\psi}}\right)^{2/5}\right\}.
                                                               \tag{A.10}
\]
Here is the arithmetic that makes this one gain work at every fixed depth. Put \(q=32768/\sqrt a=2^{15}/\sqrt a\). The first condition in (A.10) gives \(q<1/2\). For \(L\ge2\), the ratio of consecutive terms of \(\sqrt Lq^{L-2}\) is
\[
q\sqrt{\frac{L+1}{L}}\le\tfrac12\sqrt{\tfrac32}<1.
\]
Therefore \(\sqrt Lq^{L-2}\le\sqrt2\), and (A.1) yields
\[
\begin{aligned}
d_La^{(L-1)/2}
&=\frac{3T_0^2}{a^{3/2}}\sqrt Lq^L\\
&\le\frac{3\sqrt2\,2^{30}T_0^2}{a^{5/2}}\\
&\le\frac{3\sqrt2}{64}\sqrt{c_\psi}
 <\frac{\sqrt{c_\psi}}8.
\end{aligned}                                                   \tag{A.11}
\]
The last strict inequality is \(3\sqrt2<8\).

By (A.7)–(A.9), the initialized regression residual at layer \(\ell\) satisfies
\[
\sqrt{\mathcal R_\psi(z_i^\ell(0))}
                    \ge\frac{\sqrt{c_\psi}}{2a^{(\ell-1)/2}}.
\]
For \(\ell\le L\), (A.11) gives
\[
2d_L\le\frac{\sqrt{c_\psi}}{4a^{(L-1)/2}}
       \le\frac{\sqrt{c_\psi}}{4a^{(\ell-1)/2}}.
\]
Apply (A.2) to the coupling of the initialized and trained fields in (A.1), then use (A.4). This proves, for every sample, layer, and time,
\[
\inf_{\alpha,\beta}
 E[\phi(z_i^\ell(t))-\alpha-\beta z_i^\ell(t)]^2
\ge \frac{e^2c_\psi}{16a^{\ell-1}}
\ge \frac{e^2c_\psi}{16a^{L-1}}.                         \tag{A.12}
\]

Now let \(\mathcal C\subset\mathcal B\) be any class with a common interval \(r\ge1\) and common margin \(j>0\):
\[
                         J_r(\psi)\ge j
                         \quad(\psi\in\mathcal C).
\]
Set \(c_0=e^{-r^2/2}j/\sqrt{2\pi}\), and use (A.10) with \(c_\psi\) replaced by \(c_0\). The density bound, gain arithmetic, and proof of (A.12) then hold for every \(\psi\in\mathcal C\), with this same \(a\) and the common lower bound
\[
\frac{e^2c_0}{16a^{\ell-1}}\ge\frac{e^2c_0}{16a^{L-1}}.
\]
More generally it is enough for each member to have a possibly different interval witnessing \(c_\psi\ge c_0>0\); the argument uses only the common constant \(c_0\).

These interval classes contain open neighborhoods of many shapes. To check this without a compactness assertion about the class, choose a bounded nonconstant \(\psi_*\) with \(\|\psi_*\|_{C_b^2}<1\), and choose \(r\) with \(J_r(\psi_*)>0\). Testing an optimal affine fit for one function in the other interval problem gives
\[
\left|\sqrt{J_r(\psi_*+u)}-\sqrt{J_r(\psi_*)}\right|
                       \le\|u\|_{L^2[-r,r]}
                       \le\sqrt{2r}\|u\|_\infty.
\]
Thus any positive radius \(\rho\) satisfying
\[
\rho\le\frac{1-\|\psi_*\|_{C_b^2}}2,\qquad
\rho\le\frac{\sqrt{J_r(\psi_*)}}{2\sqrt{2r}}
\]
gives \(\psi_*+u\in\mathcal B\) and
\(J_r(\psi_*+u)\ge J_r(\psi_*)/4\) whenever
\(\|u\|_{C_b^2}<\rho\). Section A.4 below verifies explicitly that such neighborhoods have infinitely many independent directions.

## A.3. Why the broad class cannot have a positive depth-uniform margin

Let \(\psi\) be any nonzero compactly supported \(C^2\) function, normalized into \(\mathcal B\). For every \(\sigma>0\), testing the regression problem with the zero affine function gives
\[
0\le\mathcal R_\psi(\sigma G)
\le E[\psi(\sigma G)^2]
\le\frac1{\sigma\sqrt{2\pi}}\int_{\mathbb R}\psi(x)^2\,dx.
                                                               \tag{A.13}
\]
The integral is finite by compact support and continuity. Thus the Gaussian regression residual tends to zero as \(\sigma\to\infty\).

Keep \(a\ge4\) and \(e\in(0,1]\) fixed, and consider networks with increasing depth. Their initialized marginal variances satisfy (A.8), so \(\sigma_\ell\to\infty\). At initialization, (A.4) and (A.13) therefore give
\[
\inf_{\alpha,\beta}
 E[\phi(z_i^\ell(0))-\alpha-\beta z_i^\ell(0)]^2
=e^2\mathcal R_\psi(\sigma_\ell G)\longrightarrow0.
\]
In particular even this single admissible perturbation admits no positive lower bound uniform over all hidden depths and all times: the proposed bound would already fail at \(t=0\). This explains the depth-dependent margin in the broad theorem. It does not assert that the particular numerical lower bound (A.12) is optimal.

## A.4. A stronger class with a positive depth-uniform margin

Suppose instead that a class \(\mathcal C\subset\mathcal B\) satisfies
\[
\inf_{\psi\in\mathcal C}\inf_{\sigma\ge1}
                  \mathcal R_\psi(\sigma G)\ge\eta_0>0.  \tag{A.14}
\]
Choose the common gain
\[
a=\max\left\{10^{12}(1+T_0),
       \left(\frac{2^{36}T_0^2}{\sqrt{\eta_0}}\right)^{2/5}\right\}.
                                                               \tag{A.15}
\]
The arithmetic in (A.11), now with \(\eta_0\), gives
\[
d_La^{(L-1)/2}\le\sqrt{\eta_0}/8,
\qquad d_L\le\sqrt{\eta_0}/8<\sqrt{\eta_0}/4.
\]
Since \(\sigma_\ell\ge1\), (A.14) supplies an initialized square-root residual at least \(\sqrt{\eta_0}\). By (A.1)–(A.2), its trained square-root residual is at least
\(\sqrt{\eta_0}-2d_L\ge\sqrt{\eta_0}/2\). Thus (A.4) proves
\[
\inf_{t\ge0}\inf_{\alpha,\beta}
 E[\phi(z_i^\ell(t))-\alpha-\beta z_i^\ell(t)]^2
                              \ge e^2\eta_0/4            \tag{A.16}
\]
for every fixed \(L\ge2\), every \(1\le\ell\le L\), every sample, and every member of the class. Neither \(\eta_0\) nor the selected \(a\) changes with depth. The same fixed perturbation amplitude \(e\) is used throughout.

We now construct a nonempty infinite-dimensional open \(C_b^2\) ball satisfying (A.14).

First consider any bounded continuous nonconstant function \(\psi\) with distinct limits \(\ell_-,\ell_+\) at negative and positive infinity. For \(\sigma>0\), the functions \(1,G\) are orthonormal in Gaussian \(L^2\), and
\(\operatorname{span}\{1,\sigma G\}=\operatorname{span}\{1,G\}\). Direct completion of squares gives
\[
\mathcal R_\psi(\sigma G)
=E[\psi(\sigma G)^2]
 -(E[\psi(\sigma G)])^2
 -(E[G\psi(\sigma G)])^2.                               \tag{A.17}
\]
This is strictly positive for every fixed \(\sigma>0\). Indeed a zero residual would give \(\psi(\sigma G)=\alpha+\gamma G\) almost surely. The difference of these continuous functions of \(G\) would then vanish everywhere: if it were nonzero at one point, continuity would make it nonzero on an open interval of positive Gaussian probability. Therefore \(\psi(x)=\alpha+(\gamma/\sigma)x\) on all of \(\mathbb R\). Boundedness forces \(\gamma=0\), contradicting nonconstancy.

The residual in (A.17) is continuous in \(\sigma>0\). For any convergent positive scale sequence, continuity of \(\psi\) gives pointwise convergence of the integrands. Boundedness of \(\psi\) bounds the first two integrands by constants and the last by a constant times \(|G|\), which is integrable. Dominated convergence gives the assertion.

Put
\[
m=(\ell_++\ell_-)/2,\qquad b=(\ell_+-\ell_-)/2\ne0.
\]
For every \(G\ne0\), which holds with probability one,
\(\psi(\sigma G)\to m+b\,\operatorname{sgn}(G)\) as
\(\sigma\to\infty\). Boundedness gives convergence in \(L^2\). The limit of (A.17) is consequently
\[
b^2\bigl(1-(E|G|)^2\bigr)=b^2(1-2/\pi)>0.              \tag{A.18}
\]
Here \(E\operatorname{sgn}(G)=0\) by symmetry and
\[
E|G|=\frac2{\sqrt{2\pi}}
       \int_0^\infty x e^{-x^2/2}\,dx=\sqrt{2/\pi}.
\]
Choose a finite \(M\ge1\) such that the residual for every \(\sigma\ge M\) is at least half its positive limit in (A.18). On the compact interval \([1,M]\), the continuous strictly positive residual attains a strictly positive minimum. The smaller of these two positive bounds proves
\[
                       \inf_{\sigma\ge1}
                          \mathcal R_\psi(\sigma G)>0.   \tag{A.19}
\]
This argument proves positivity of an actual numerical constant associated with a fixed function; it does not assume a compactness property for an infinite function class.

Apply it to
\[
\psi_0(x)=\tfrac14\arctan x.
\]
Its derivatives are
\[
\psi_0'(x)=\frac1{4(1+x^2)},\qquad
\psi_0''(x)=-\frac{x}{2(1+x^2)^2}.
\]
Thus
\[
\|\psi_0\|_\infty=\pi/8,\quad
\|\psi_0'\|_\infty=1/4,\quad
\|\psi_0''\|_\infty=3\sqrt3/32,
\qquad \|\psi_0\|_{C_b^2}=\pi/8<1.
\]
For the second derivative maximum, differentiating
\(x/(1+x^2)^2\) on \(x\ge0\) gives derivative
\((1-3x^2)/(1+x^2)^3\); its unique positive critical point is \(x=1/\sqrt3\), which yields the displayed value.
The tail limits are \(-\pi/8,\pi/8\), so (A.18) has the positive value
\(\pi^2(1-2/\pi)/64\). Define
\[
\eta_b=\inf_{\sigma\ge1}\mathcal R_{\psi_0}(\sigma G)>0,
\qquad
\rho=\min\left\{\frac{1-\pi/8}{2},\frac{\sqrt{\eta_b}}2\right\}>0.
\]
Consider the open ball
\[
\mathcal C_\rho
=\{\psi_0+u:\ u\in C_b^2(\mathbb R),\ \|u\|_{C_b^2}<\rho\}.
\]
It is an open \(C_b^2\) ball contained in \(\mathcal B\), hence also open relative to the normalized admissible class. Indeed its members have norm at most
\(\pi/8+\rho<1\). By (A.3), for every \(\sigma\ge1\),
\[
\sqrt{\mathcal R_{\psi_0+u}(\sigma G)}
\ge\sqrt{\eta_b}-\|u\|_\infty
\ge\sqrt{\eta_b}/2.
\]
Thus this entire ball satisfies (A.14) with the single constant
\[
                              \eta_0=\eta_b/4>0.         \tag{A.20}
\]
In particular all its members are nonconstant. This constant depends only on the displayed fixed center and radius, and is independent of \(\delta\); the gain in (A.15) still depends on \(\delta\) through \(T_0\).

For an explicit verification of infinite dimensionality, let
\[
v(x)=c(1-x^2)^3\mathbf1_{\{|x|<1\}},
\]
where \(c>0\) is small enough that \(\|v\|_{C_b^2}\le1\).
The function and its first two derivatives vanish at the endpoints \(\pm1\), so it is a nonzero compactly supported \(C_b^2\) function. The translates \(v_k(x)=v(x-3k)\), \(k\ge1\), have disjoint supports. For every positive integer \(N\) and any real coefficients with \(\max_{k\le N}|s_k|<\rho\),
\[
\left\|\sum_{k=1}^Ns_kv_k\right\|_{C_b^2}
\le\max_{k\le N}|s_k|<\rho.
\]
The translates are linearly independent, since each is nonzero on a support disjoint from all the others. Hence the ball contains parameter families of arbitrarily large finite dimension, proving it has infinitely many independent directions.

Membership in this ball does not require tail limits or oddness. For example a sufficiently small cosine perturbation belongs to the ball and has oscillating tails and breaks oddness. Its common lower bound follows from the uniform norm estimate (A.3), even though the tail-limit proof applies only to the fixed center. The full activation remains strictly increasing because
\(\phi'=a+e\psi'\ge a-e>0\).

## A.5. Scope of the uniform conclusions

For a class with a common finite-interval margin, the same gain and all main-theorem conclusions hold for every fixed member and every fixed finite depth, with the common lower bound (A.12). For a class satisfying (A.14), the same parameter recipe with \(\eta_0\) instead of \(c_\psi\) improves that bound to (A.16), uniform also in hidden depth.

The finite-width convergence statements retain their original quantifiers: the function, dataset, finite depth, and observation horizon are fixed before width tends to infinity. Sharing constants across a class does not by itself assert uniform finite-width convergence over that infinite class, simultaneous width/depth limits, or a positive margin independent of \(e\) as \(e\downarrow0\). The construction uses the original raw metric and the displayed affine-plus-perturbation activation throughout.

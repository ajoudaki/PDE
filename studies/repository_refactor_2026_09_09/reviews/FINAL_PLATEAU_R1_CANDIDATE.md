## Plateau features: protected geometry, confinement and selected path laws

This section concerns exactly two hidden layers and three fixed samples,
with a separate smooth plateau activation. It proves protected first-feature
geometry, continuous-time row confinement under integrable controls, and
selected path-law compactness for supplied strong dissipative flows. It
constructs neither a canonical population solution nor a finite-width limit.

Put \(u_a=x_a/\sqrt d\), \(|u_a|=1\), and
\(G_{ab}=u_a^Tu_b\). Assume \(|G_{ab}|<1-\delta\) for distinct
\(a,b\in\{1,2,3\}\), with \(0<\delta<1\). The labels are binary.
The finite first row is the stored row \(w=(W^{(1)})_{j,:}\), so its
preactivation is \(w^Tu_a\). Finite initialization, when used, has
independent standard Gaussian first rows, middle entries of variance
\(1/n\), and stored readout entries of variance \(n^{-2}\).
Use the half-sum loss \(\mathcal E=\tfrac12\sum_a r_a^2\),
\(r_a=f_a-y_a\), and block mobilities \((n,1,n)\).
The residual-free backward fields follow the notation contract. Consequently

\[
 \dot w=-\sum_a r_a\delta_{a,j}^{(1)}u_a
       =-\sum_a r_a q_{a,j}\phi'(w^Tu_a)u_a,
 \qquad q_a=(W^{(2)})^T\delta_a^{(2)}.
 \tag{P.1}
\]

This follows by differentiating \(f_a=(W^{(3)})^Th_a^{(2)}/n\)
with respect to the first row and multiplying the half-sum gradient by
\(n\). It fixes the storage and physical clock used below. Simultaneous
raw GD uses the same right-hand side at the old state.

For conditional population applications, take probability spaces
\(\Omega_1,\Omega_2\), a given bounded initial action
\(A_0:L^2(\Omega_1)\to L^2(\Omega_2)\), and state
\(w\in L^2(\Omega_1;\mathbb R^d)\),
\(W^{(2)}=A_0+U\), \(U\) Hilbert--Schmidt, and
\(W^{(3)}\in L^2(\Omega_2)\). Define

\[
 Z_a^{(1)}=w^Tu_a,\quad H_a^{(1)}=\phi(Z_a^{(1)}),\quad
 Z_a^{(2)}=W^{(2)}H_a^{(1)},\quad H_a^{(2)}=\phi(Z_a^{(2)}),
 \quad f_a=\mathbb E_2[W^{(3)}H_a^{(2)}],
\]
\[
 \Delta_a^{(2)}=W^{(3)}\phi'(Z_a^{(2)}),\quad
 Q_a=(W^{(2)})^*\Delta_a^{(2)},\quad
 \Delta_a^{(1)}=\phi'(Z_a^{(1)})Q_a.
 \tag{P.2}
\]

A supplied population path satisfies the Bochner integral equations for

\[
 \dot w=-c\sum_a r_a\Delta_a^{(1)}u_a,\qquad
 \dot U=-\sum_a r_a\Delta_a^{(2)}\otimes H_a^{(1)},\qquad
 \dot W^{(3)}=-\sum_a r_a H_a^{(2)},\quad 0\le c(t,\omega)\le1.
 \tag{P.3}
\]

The first cap is one common measurable scalar per row. The true physical
flow has \(c=1\). A rank-one operator is
\(v\otimes h:g\mapsto v\mathbb E_1[hg]\).
Every use below of a population path explicitly assumes that its equations,
products and chain rules hold strongly; existence of such a path is not an
inference from the geometry. Initially \(w\) is a standard Gaussian vector,
\(U=0\), and \(W^{(3)}=0\). This zero population readout is not a reset of
the finite random readout.

### P.1 Activation and conclusions

Put

\[
 \beta(s)=\begin{cases}e^{-1/(1-s^2)},&|s|<1,\\0,&|s|\geq1,\end{cases}
 \qquad I=\int_0^1\beta(s)\,ds,
 \qquad
 \phi(z)=1+\frac{1}{2I}\int_0^z\beta(s)\,ds.
\]

Thus \(\phi=1/2\) on \(( -\infty,-1]\), \(\phi=3/2\) on \([1,\infty)\), and \(\phi'>0\) exactly on \((-1,1)\). In particular its nonlinear amplitude is the fixed coefficient \(1/2\), not a separation-dependent small parameter.

Let \(u_i=x_i/\sqrt d\), so \(\|u_i\|=1\), and assume

\[
 -1+\delta<u_i\cdot u_j<1-\delta\quad(i\ne j),
 \qquad 0<\delta<1.
\]

For a standard Gaussian \(w\in\mathbb R^d\), write

\[
 h(w)=(\phi(w\cdot u_1),\phi(w\cdot u_2),\phi(w\cdot u_3)),
 \qquad
 P=\{w:|w\cdot u_i|\geq1\text{ for all }i\}.
\]

The principal conclusions are

\[
 K_{\rm fr}:=\mathbb E[\mathbf1_P(w)h(w)h(w)^T]
      \succeq \lambda_\delta I_3,
 \qquad \lambda_\delta=\frac1{240}e^{-22/\delta}.
\]

This includes singular, rank-two input Grams. Every initial row in \(P\) is exactly frozen under raw GF and simultaneous raw GD, so this is an invariant part of the first-layer feature Gram. The coefficient is deliberately crude but explicit.

There is also a positive fraction of derivative-active rows: under any raw GF satisfying the locally integrable row-coefficient condition stated below, a row initially outside \(P\) never enters \(P\) in finite time. Consequently the fraction of rows with at least one strictly positive first-layer activation derivative remains at least

\[
 p_{\rm act}=\mathbb P(|G|<1)>0,\qquad G\sim N(0,1).
\]

Derivative activity must not be confused with nonzero feature velocity. That stronger assertion requires information about the physical residuals and return fields.

### P.2 Smoothness and moderate fixed bounds

The zero extension of \(\beta\) is \(C^\infty\). To check the endpoint assertion directly, every derivative inside \((-1,1)\) is a finite sum of powers of \(s\) and \((1-s^2)^{-1}\), multiplied by \(e^{-1/(1-s^2)}\). This follows inductively by differentiating such expressions. If \(x=(1-s^2)^{-1}\to\infty\), every such term is bounded by a constant times \(x^M e^{-x}\), which tends to zero: the exponential series gives \(e^x\geq x^{M+1}/(M+1)!\). All one-sided derivatives therefore match the zero extension. Integration gives the claimed smoothness of \(\phi\).

On \([0,1/2]\), \(\beta\geq e^{-4/3}\); everywhere, \(\beta\leq e^{-1}\). Thus

\[
 \tfrac12e^{-4/3}\leq I\leq e^{-1},
 \qquad 0\leq\phi'\leq e^{1/3},
 \qquad
 \inf_{|z|\leq1/2}\phi'(z)\geq \nu:=\tfrac12e^{-1/3}.
\]

Inside the transition,

\[
 \beta'(z)=-\frac{2z}{(1-z^2)^2}e^{-1/(1-z^2)}.
\]

With \(x=(1-z^2)^{-1}\geq1\), this has absolute value at most \(2x^2e^{-x}\leq8e^{-2}\), since differentiating \(x^2e^{-x}\) places its maximum at \(x=2\). Hence

\[
 \|\phi''\|_\infty\leq8e^{-2/3}.
\]

These fixed, finite bounds suffice for the row uniqueness argument below. No gain changes with \(\delta\).

### P.3 Six plateau balls that detect every coefficient

Let \(S=\operatorname{span}(u_1,u_2,u_3)\). Its dimension \(k\) is either two or three: rank one would force two unit inputs to have inner product \(1\) or \(-1\), contradicting separation. The orthogonal projection of \(w\) onto \(S\) is standard Gaussian in \(S\). This can be seen by completing an orthonormal basis of \(S\) and factoring the standard Gaussian density in those coordinates. Features depend only on this projection. Thus all probability estimates below take place in dimension at most three, regardless of \(d\).

Fix an index \(i\), and call the remaining indices \(j,k\). Set

\[
 a=u_j-(u_j\cdot u_i)u_i,
 \qquad b=u_k-(u_k\cdot u_i)u_i.
\]

Both belong to \(S\cap u_i^\perp\), and

\[
 \|a\|,\|b\|\geq\sqrt{\delta(2-\delta)}\geq\sqrt\delta.
\]

Choose \(\epsilon\in\{-1,1\}\) so that
\(\widehat a\cdot(\epsilon\widehat b)\geq0\), where hats denote unit normalization, and put

\[
 v=\frac{\widehat a+\epsilon\widehat b}
          {\|\widehat a+\epsilon\widehat b\|}.
\]

Writing \(c=\widehat a\cdot(\epsilon\widehat b)\in[0,1]\), direct calculation gives

\[
 v\cdot u_i=0,\quad \|v\|=1,\quad
 |v\cdot u_j|=\|a\|\sqrt{\frac{1+c}{2}}\geq\sqrt{\delta/2},
 \quad
 |v\cdot u_k|\geq\sqrt{\delta/2}.
\]

This works also when \(S\cap u_i^\perp\) is one-dimensional: after choosing \(\epsilon\), the two normalized projections agree.

Define centers in \(S\)

\[
 R=4\sqrt{2/\delta},\qquad w_i^\pm=Rv\pm2u_i,
 \qquad B_i^\pm=\{g\in S:\|g-w_i^\pm\|<1/2\}.
\]

At the two centers the \(i\)-th preactivation is respectively \(+2\) and \(-2\). For \(\ell\in\{j,k\}\),

\[
 |Rv\cdot u_\ell\pm2u_i\cdot u_\ell|
 \geq4-2|u_i\cdot u_\ell|\geq2.
\]

Their signs are the sign of \(v\cdot u_\ell\), independent of the choice \(+\) or \(-\). Moving by less than \(1/2\) changes each unit-input projection by less than \(1/2\). Consequently both balls lie in \(P\), all coordinates have fixed plateau signs on each ball, and only coordinate \(i\) changes sign between the two balls.

Let \(h_i^\pm\in\{1/2,3/2\}^3\) be their respective feature vectors. Exactly,

\[
 h_i^+-h_i^-=e_i.
\]

For fixed \(i\) the two balls are disjoint, since their centers are distance four apart.

The center norms satisfy

\[
 \|w_i^\pm\|^2=32/\delta+4\leq36/\delta.
\]

Thus every point in either ball has norm at most \(6/\sqrt\delta+1/2\leq13/(2\sqrt\delta)\). Integrating the minimum Gaussian density over a radius-\(1/2\) ball gives

\[
 \mathbb P(w_S\in B_i^\pm)
 \geq c_k e^{-169/(8\delta)},
 \quad c_2=\tfrac18,\quad c_3=\frac1{12\sqrt{2\pi}}.
\]

Here the constants follow from the disk area \(\pi/4\) and three-dimensional ball volume \(\pi/6\), multiplied by the respective Gaussian normalizations. Both constants exceed \(1/40\), and \(169/8<22\). Therefore every one of the six balls has probability at least

\[
 p_\delta:=\frac1{40}e^{-22/\delta}.
\]

### P.4 Positive definite invariant feature Gram

For any \(c\in\mathbb R^3\), the disjointness for a fixed \(i\) yields

\[
 c^T K_{\rm fr}c
 \geq p_\delta\big[(c\cdot h_i^+)^2+(c\cdot h_i^-)^2\big]
 \geq\frac{p_\delta}{2}c_i^2.
\]

The last inequality is \(a^2+b^2\geq(a-b)^2/2\), together with \(h_i^+-h_i^-=e_i\). Choose an index with \(c_i^2\geq\|c\|^2/3\). It follows that

\[
 c^TK_{\rm fr}c\geq\frac{p_\delta}{6}\|c\|^2
 =\lambda_\delta\|c\|^2.
\]

No disjointness of balls belonging to different indices is asserted or needed. This avoids overcounting their Gaussian mass. The construction also proves \(\mathbb P(P)\geq2p_\delta\).

### P.5 Exact invariance for the original raw dynamics

For the stored first-layer row in (P.1), the raw GF gives exactly

\[
 \dot w(t)=-\sum_{i=1}^3r_i(t)q_i(t)\phi'(w(t)\cdot u_i)u_i.
 \tag{P.4}
\]

For a population row, \(q_i(t)\) means the value at that row's Gaussian coordinate. For a finite row, it is the corresponding component of the actual \((W^{(2)})^T\delta_i^{(2)}\). No different metric or surrogate return field is used.

**Row lemma.** Suppose a row is absolutely continuous on \([0,T]\), satisfies (P.4) almost everywhere, and

\[
 \int_0^T\sum_i|r_i(t)q_i(t)|\,dt<\infty.
 \tag{P.5}
\]

Then a row starting in \(P\) stays at its initial value. A row starting outside \(P\) stays outside \(P\) throughout \([0,T]\).

**Proof.** Treat the realized coefficients \(a_i(t)=r_i(t)q_i(t)\) as fixed measurable functions and set

\[
 F(t,z)=-\sum_i a_i(t)\phi'(z\cdot u_i)u_i.
\]

The derivative bound above and \(\|u_i\|=1\) imply

\[
 \|F(t,z)-F(t,\widetilde z)\|
 \leq L(t)\|z-\widetilde z\|,
 \qquad L(t)=\|\phi''\|_\infty\sum_i|a_i(t)|\in L^1(0,T).
\]

For every \(\xi\in P\), \(F(t,\xi)=0\). If a solution equals \(\xi\) at a time \(s\), then for later times its distance \(D(t)\) from \(\xi\) obeys
\(D(t)\leq\int_s^tL(v)D(v)\,dv\). To prove it vanishes without invoking a uniqueness theorem, set \(J(t)=\int_s^tL(v)D(v)\,dv\). Then \(J(s)=0\), \(J\geq0\), and \(J'\leq LJ\) almost everywhere. Differentiating \(e^{-\int_s^tL}J(t)\) shows it is nonincreasing and starts at zero. Hence \(J=D=0\). Reversing the time variable proves the same assertion before \(s\). Thus an initial point in \(P\) is constant, while an initial point outside \(P\) cannot reach any \(\xi\in P\) at a later finite time. ∎

For every existing finite GF solution on a compact interval, its continuous finite-dimensional coefficients satisfy (P.5). For a population GF, a sufficient condition is

\[
 \sum_i\int_0^T|r_i(t)|\,\|q_i(t)\|_{L^2(\Omega_1)}\,dt<\infty.
\]

Indeed, integration over the probability space, followed by \(\|q\|_{L^1}\leq\|q\|_{L^2}\), shows that (P.5) holds for almost every row. An absolutely continuous \(L^2\) row path with an integrable \(L^2\) velocity has an almost-everywhere absolutely continuous representative: its Bochner integral formula can be represented pointwise because the integral of the pointwise absolute velocity is finite by the same inequality. Thus the row lemma applies whenever the population equation has this stated pointwise interpretation. This note does not assume that merely naming a strong solution automatically supplies unproved return-field bounds.

Consequently, for each such population flow,

\[
 \mathbb E_1[\mathbf1_{P}(w(0))H_i^{(1)}(t)H_j^{(1)}(t)]
 =(K_{\rm fr})_{ij},
 \qquad
 \big(\mathbb E_1[H_i^{(1)}(t)H_j^{(1)}(t)]\big)_{i,j=1}^3
 \succeq K_{\rm fr}\succeq\lambda_\delta I_3.
\]

For simultaneous raw GD, a row initially in \(P\) has zero update at the first step and, inductively, at every step. This is exact for any step size, in particular the stipulated physical step \(n^{-2}\). The no-entry statement for initially active rows is a continuous-time uniqueness statement; its discrete analogue would need a step-size estimate.

### P.6 Elementary finite-sample version

This section concerns only the invariant initial feature Gram, not the full finite-width bridge. For independent initial rows \(w_a\), define

\[
 K_{{\rm fr},n}=\frac1n\sum_{a=1}^n
 \mathbf1_P(w_a)h(w_a)h(w_a)^T.
\]

It is unchanged along every existing finite GF and every raw GD trajectory. Since \(|h_i h_j|\leq9/4\), independence and expansion of centered squares give

\[
 \mathbb E\|K_{{\rm fr},n}-K_{\rm fr}\|_F^2
 =\sum_{i,j}\operatorname{Var}((K_{{\rm fr},n})_{ij})
 \leq\frac{729}{16n}.
\]

For a nonnegative random variable \(X\), \(\mathbb P(X\geq a)\leq\mathbb E X/a\), because \(X\geq a\mathbf1_{\{X\geq a\}}\). Apply this to the squared Frobenius norm with threshold \(\lambda_\delta^2/4\). Using \(\|M\|_{\rm op}\leq\|M\|_F\), one gets

\[
 \mathbb P\left(K_{{\rm fr},n}\not\succeq
              \tfrac12\lambda_\delta I_3\right)
 \leq\min\left\{1,\frac{729}{4n\lambda_\delta^2}\right\}.
\]

On the complementary event this same lower bound holds for the full first-layer feature Gram at every time for which the finite flow exists, or every GD step. The estimate is very conservative and no practical width claim is attached to it.

### P.7 Quantitative initial nonaffinity

Let \(\rho(g)=(2\pi)^{-1/2}e^{-g^2/2}\), \(Q=\int_1^\infty\rho(g)\,dg\), and \(M=\rho(1)\). A fixed scalar measure of initial nonaffinity is

\[
 \mathcal N=\inf_{a,b\in\mathbb R}
       \mathbb E\big[(\phi(G)-a-bG)^2\big].
\]

Writing \(\psi=\phi-1\), its oddness and Gaussian symmetry give

\[
 \mathbb E[(\phi(G)-a-bG)^2]
 =(1-a)^2+\mathbb E[(\psi(G)-bG)^2].
\]

On the positive tail \(g\geq1\), \(\psi(g)=1/2\). The two tails therefore imply

\[
 \mathcal N\geq\inf_b2\int_1^\infty(1/2-bg)^2\rho(g)\,dg
 =:c_{\rm tail}
 =\frac12\left(Q-\frac{M^2}{Q+M}\right)>0.
\]

For the equality, \(\rho'=-g\rho\) and integration by parts give
\(\int_1^\infty g\rho=M\) and
\(\int_1^\infty g^2\rho=Q+M\); minimizing the resulting quadratic gives the formula. Its positivity also follows directly because a nonconstant interval of positive Gaussian mass cannot satisfy \(1/2=bg\) almost everywhere.

A lower bound with no Gaussian tail integral is

\[
 c_{\rm tail}\geq
 2\rho(2)\inf_b\int_1^2(1/2-bg)^2\,dg
 =\frac{\rho(2)}{56}
 =\frac{e^{-2}}{56\sqrt{2\pi}}>0.
\]

Indeed, the integral is \(1/4-(3/2)b+(7/3)b^2\), with minimum \(1/112\). This documents a fixed quantitative departure from every affine scalar activation.

The same bound holds when comparison is made with arbitrary affine functions of the full initial Gaussian row:

\[
 \inf_{a\in\mathbb R,\,b\in\mathbb R^d}
 \mathbb E[(\phi(w\cdot u_i)-a-b\cdot w)^2]\geq c_{\rm tail}.
\]

To see this, decompose \(b=(b\cdot u_i)u_i+b_\perp\). The independent orthogonal Gaussian component contributes the nonnegative variance \(\|b_\perp\|^2\), while the component along \(u_i\) is the scalar calculation above. Thus a three-coordinate vector of affine Gaussian functions has squared approximation error at least \(3c_{\rm tail}\).

### P.8 What remains active, and what this does not show

Initially the event \(|w\cdot u_1|\leq1/2\) has probability

\[
 \mathbb P(|G|\leq1/2)
 =2\int_0^{1/2}\rho(g)\,dg
 \geq\rho(1/2)>0,
\]

and on this event the first datum has \(\phi'\geq\nu=\tfrac12e^{-1/3}\). Both this derivative bound and its positive fraction are independent of separation and ambient dimension. If activity on all three data is desired initially, the event \(\|w_S\|<1/2\) suffices. Its probability is at least

\[
 \frac{e^{-1/8}}{12\sqrt{2\pi}}>0,
\]

using the two possible dimensions and their ball-density constants from the six-ball construction.

Under the row lemma, membership in \(P\) is unchanged, so for every finite training time

\[
 \mathbb P\left(\max_i\phi'(w(t)\cdot u_i)>0\right)
 =\mathbb P(w(0)\notin P)
 \geq\mathbb P(|G|<1)=p_{\rm act}>0.
\]

The same row labels remain in the active complement at all finite times, assuming (P.5) on all compact intervals. This statement supplies neither a uniform-in-time positive lower bound on those derivatives nor a positive speed. In particular the population initialization in (P.2)–(P.3) has \(W^{(3)}(0)=0\), hence \(Q_i(0)=0\) and \(\dot w(0)=0\), despite the positive fraction of activation derivatives. Establishing actual subsequent feature motion is a separate physical-dynamics question.

Finally, the invariant first-layer Gram is not by itself a lower bound for the full prediction kernel: the other factors in the true kernel blocks, especially \(\Delta_i^{(2)}=\phi'(Z_i^{(2)})W^{(3)}\), still have their actual evolving values. The result settles the proposed plateau geometry and invariance mechanism, including rank-two inputs, while leaving those dynamic obligations open.

### P.9 Statement

Let \(u_1,u_2,u_3\in\mathbb R^d\) be unit vectors with

\[
 |u_i\cdot u_j|<1-\delta\quad(i\ne j),\qquad0<\delta<1.
\]

Let \(g:\mathbb R\to\mathbb R\) be globally Lipschitz and vanish whenever \(|s|\geq1\). The plateau derivative \(g=\phi'\) above satisfies these hypotheses. Its sign and whether it is strictly positive in the interior are immaterial for this confinement result.

Consider any absolutely continuous solution on \([0,T]\) of

\[
 \dot w(t)=\sum_{i=1}^3 a_i(t)g(u_i\cdot w(t))u_i,
 \qquad a_i\in L^1(0,T).
 \tag{P.6}
\]

The controls may depend arbitrarily on the realized solution. Only their integrability on the interval is required; neither their sizes nor the length of the interval enters the bound.

Write \(G=(u_i\cdot u_j)_{i,j=1}^3\) and

\[
 B_\delta=\sqrt{2/\delta},\qquad D_\delta=B_\delta+2.
\]

Then every such solution satisfies the following bounds at all times in its existence interval:

* If \(\operatorname{rank}G=2\),
  \[
  \|w(t)\|\leq\|w(0)\|+D_\delta.
  \]
* If \(\operatorname{rank}G=3\), putting \(\kappa=\lambda_{\min}(G)>0\),
  \[
  \|w(t)\|\leq\|w(0)\|+R_G,
    \qquad R_G=D_\delta+\frac{1+D_\delta}{\sqrt\kappa}.
  \]

These are stronger than a bound of the requested form \(C_G(1+\|w(0)\|)\). They also apply to every subinterval, forwards and backwards. The rank-three constant is not uniform as its Gram approaches singularity; the exactly rank-two case has its separate uniform separation bound.

### P.10 Freezing and a two-dimensional geometric lemma

We first establish two elementary facts that will also handle boundary and last-activation-time cases.

**Freezing fact.** For any subset \(J\) of the indices, a solution driven only by the gates in \(J\) that reaches

\[
 P_J=\{w:|u_i\cdot w|\geq1\text{ for every }i\in J\}
\]

is constant on its entire interval.

To prove this, fix a reached point \(\xi\in P_J\) and regard the realized coefficients as prescribed functions of time. The vector field vanishes at \(\xi\), and its spatial Lipschitz constant is bounded by
\(\operatorname{Lip}(g)\sum_{i\in J}|a_i(t)|\in L^1\). If two solutions agree at time \(s\), their distance obeys
\(D(t)\leq\int_s^t L(v)D(v)\,dv\). For \(J_0(t)=\int_s^tL(v)D(v)\,dv\), multiplication by \(e^{-\int_s^tL}\) shows from \(J_0'\leq LJ_0\) and \(J_0(s)=0\) that \(J_0=D=0\). Reversing time proves equality before \(s\) as well. The constant trajectory \(\xi\) therefore coincides with the given trajectory. This argument remains valid even if the original controls were generated by a coupled system: the comparison uses their realized values.

**Planar lemma.** Suppose finitely many pairwise nonparallel unit vectors \(v_1,\ldots,v_N\) lie in a fixed two-dimensional Euclidean space \(V\). Let \(x(t)\in V\) satisfy an equation of the form (P.6) using only those vectors and their gates. Assume every double-strip intersection

\[
 Q_{ij}=\{x\in V:|v_i\cdot x|\leq1,\ |v_j\cdot x|\leq1\}
\]

is contained in the closed radius-\(B\) ball. Put \(Q=\bigcup_{i<j}Q_{ij}\). Then:

1. If a trajectory visits \(Q\), its whole trajectory on that interval is contained in the radius-\(B+2\) ball.
2. In general,
   \(\sup_t\|x(t)\|\leq\max\{\|x(0)\|,B\}+2\).
3. For \(N=2\), if both closed strips are visited, possibly at different times, then \(Q_{12}\) is visited.

**Proof.** A constant trajectory needs no argument. By the freezing fact, a nonconstant trajectory has at least one strictly active strip \(|v_i\cdot x|<1\) at every time. On any connected time interval avoiding \(Q\), there is at most one closed strip, hence exactly one strictly active strip. Its index is locally constant: the other strip inequalities are strict in the opposite direction and persist under small perturbations of time. It is therefore constant on the interval. Only the corresponding direction \(v_i\) can drive motion there, so

\[
 x(t)-x(s)=\alpha v_i,
 \qquad \alpha=v_i\cdot x(t)-v_i\cdot x(s),
 \qquad |\alpha|\leq2.
 \tag{P.7}
\]

The same displacement bound holds on the closure of that time interval by continuity.

If \(Q\) is visited, each component of its time complement has a boundary time at which \(Q\) is visited, unless the complement is the whole interval. The latter is excluded. Formula (P.7) puts each point outside \(Q\) within distance two of a point in \(Q\). This proves assertion 1, including components adjoining either endpoint. If \(Q\) is never visited, the active index stays fixed on the whole interval and (P.7) bounds displacement from the initial point by two. This proves assertion 2.

For assertion 3, if \(Q_{12}\) were never visited, a nonconstant trajectory would have one fixed strictly active strip and would stay strictly outside the other closed strip. A constant trajectory cannot visit both closed strips without belonging to their intersection. Both alternatives contradict the premise. ∎

The lemma works with two or three gates; no finite bound on the number of switches is needed.

### P.11 The size of every double-strip intersection

For two of our unit vectors with \(\rho=u_i\cdot u_j\), let \(V=\operatorname{span}(u_i,u_j)\), and set
\(z=(u_i\cdot x,u_j\cdot x)\) for \(x\in V\). In the basis \(u_i,u_j\), inversion of the two-by-two Gram gives

\[
 \|x\|^2=z^T\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}^{-1}z
 \leq\frac{z_1^2+z_2^2}{1-|\rho|}.
\]

For completeness, the Gram's orthogonal directions \((1,1)\) and \((1,-1)\) have eigenvalues \(1+\rho\) and \(1-\rho\), so its inverse quadratic form is bounded by \((1-|\rho|)^{-1}\|z\|^2\). When both strip constraints hold,

\[
 \|x\|\leq\sqrt{\frac2{1-|\rho|}}\leq B_\delta.
 \tag{P.8}
\]

In a rank-two input configuration, every pair spans the entire input span, so (P.8) bounds every double-strip intersection in that common plane.

### P.12 Rank-two confinement

Let \(S=\operatorname{span}(u_1,u_2,u_3)\) have dimension two. The component \(w_{S^\perp}\) is constant, since all velocities lie in \(S\). Apply the planar lemma with all three gates to \(w_S\). It gives

\[
 \|w_S(t)\|\leq\max\{\|w_S(0)\|,B_\delta\}+2
 \leq\|w_S(0)\|+D_\delta.
\]

Adding the unchanged orthogonal component does not cost a second copy of the initial norm: by the triangle inequality in two dimensions,

\[
 \sqrt{\|w_{S^\perp}(0)\|^2+(\|w_S(0)\|+D_\delta)^2}
 \leq\|w(0)\|+D_\delta.
\]

This proves the rank-two assertion.

### P.13 Rank-three confinement by last activation times

Now suppose \(S\) has dimension three. As before, work first in \(S\), as its orthogonal component is constant. Fix an arbitrary endpoint \(T\). Define the open-gate time sets

\[
 \mathcal T_i=\{t\in[0,T]:|u_i\cdot w(t)|<1\}.
\]

If one of these sets is empty, that gate contributes zero throughout the interval. The other two gates evolve only the projection onto their span. The planar lemma and (P.8), with the orthogonal component fixed, then give

\[
 \|w(T)\|\leq\|w(0)\|+D_\delta.
 \tag{P.9}
\]

This remains true when another gate is also inactive: it is still a valid two-gate equation.

It remains to handle the case when all three \(\mathcal T_i\) are nonempty. Set

\[
 \tau_i=\sup\mathcal T_i,
\]

and choose \(k\) with minimal \(\tau_k\), breaking ties arbitrarily. Let \(i,j\) be the other two indices and put \(s=\tau_k\). Continuity gives

\[
 |u_\ell\cdot w(\tau_\ell)|\leq1\quad\text{for every }\ell.
 \tag{P.10}
\]

For every \(t>s\), the \(k\)-th gate vanishes. Thus on the suffix \([s,T]\) the equation uses only directions \(u_i,u_j\). A possibly different value at the single endpoint \(s\) has no effect on its integral equation.

Let \(V=\operatorname{span}(u_i,u_j)\), and write

\[
 w_S(t)=v(t)+rn,\qquad v(t)\in V,
\]

where \(n\) is a unit normal to \(V\) inside \(S\). The scalar \(r\) is constant on the suffix. By (P.10), the projected trajectory \(v\) visits both closed strips at the times \(\tau_i,\tau_j\in[s,T]\). The planar lemma, including assertion 3, therefore implies

\[
 \|v(t)\|\leq D_\delta\quad(s\leq t\leq T).
 \tag{P.11}
\]

This reasoning includes tied last-activation times. If \(s=T\), the suffix is a single point and both closed strip inequalities hold there, so (P.11) holds directly.

Set

\[
 \eta_k=|u_k\cdot n|=\operatorname{dist}(u_k,V)>0.
\]

At the suffix start, (P.10) and (P.11) imply

\[
 |r|\eta_k\leq |u_k\cdot w_S(s)|+|u_k\cdot v(s)|
 \leq1+D_\delta.
\]

Consequently

\[
 \|w_S(T)\|\leq D_\delta+\frac{1+D_\delta}{\eta_k}.
 \tag{P.12}
\]

To bound \(\eta_k\) by the full Gram, note that

\[
 \eta_k^2=\inf_{b_i,b_j}
 \|u_k-b_i u_i-b_j u_j\|^2.
\]

Every squared norm on the right is \(c^TG c\) with \(c_k=1\), hence is at least \(\kappa\|c\|^2\geq\kappa\). Thus \(\eta_k\geq\sqrt\kappa\). Formula (P.12) is bounded by \(R_G\).

Restoring the fixed component in \(S^\perp\) yields
\(\|w(T)\|\leq\|w(0)\|+R_G\). Combining this with (P.9) and the arbitrariness of \(T\) proves the result.

The argument also explains why repeated control loops cannot produce an unbounded ratchet. On a suffix driven by two gates, the transverse component is fixed. If both gates participate, their planar component is bounded independently of the controls. The last participation of the third gate bounds the remaining component.


### P.14 Selected population path laws

Assume a family of supplied strong paths (P.2)–(P.3) on a fixed
\([0,T]\), with the same Gaussian law of \(w(0)\),
\(\|A_0\|_{\rm op}\le a_0\), zero learned increment and readout initially,
and the dissipative estimate

\[
 \mathcal E(t)+\int_0^t\left(
 \mathbb E_1|\dot w|^2+\|\dot U\|_{\rm HS}^2+
 \mathbb E_2|\dot W^{(3)}|^2\right)dv\le E_0=3/2.
 \tag{P.13}
\]

The spaces or initial actions may differ between members of the family;
this statement concerns their laws. Write
\(B=3/2\), \(D=e^{1/3}\), \(D_2=8e^{-2/3}\), the activation bounds
already proved, and set

\[
 R=\sqrt{6E_0},\quad c_T=BRT,\quad a_T=a_0+\sqrt{TE_0},
 \quad W_T=RD^2a_Tc_T,\quad U_T=RDBc_T,
\]
\[
 V_T=BU_T+a_TDW_T,\qquad B_T=RBD+D_2c_TV_T.
 \tag{P.14}
\]

Indeed \(\sum_a|r_a|\le\sqrt{3\sum_a r_a^2}\le R\).
The readout equation and its zero initial value imply the pointwise bound
\(|W^{(3)}(t)|\le c_T\). The energy bound and Cauchy–Schwarz give
\(\|U(t)\|_{\rm HS}\le\sqrt{TE_0}\), hence
\(\|W^{(2)}(t)\|_{\rm op}\le a_T\). Thus

\[
 |H_a^{(1)}|,|H_a^{(2)}|\le B,\qquad
 |\Delta_a^{(2)}|\le Dc_T,\qquad
 \|Q_a\|_{L^2(\Omega_1)}\le a_TDc_T.
 \tag{P.15}
\]

Apply the triangle inequality to (P.3), using the unit vectors \(u_a\)
and \(c\le1\). Then, for almost every time,

\[
 \|\dot w\|_{L^2(\Omega_1)}\le W_T,\quad
 \|\dot U\|_{\rm HS}\le U_T,\quad
 \|\dot H_a^{(1)}\|_{L^2(\Omega_1)}\le DW_T,
\]
\[
 \|\dot Z_a^{(2)}\|_{L^2(\Omega_2)}
 \le \|\dot U\|_{\rm op}\|H_a^{(1)}\|_{L^2}
      +\|W^{(2)}\|_{\rm op}\|\dot H_a^{(1)}\|_{L^2}
 \le V_T,
\]
\[
 \|\dot H_a^{(2)}\|_{L^2(\Omega_2)}\le DV_T,\qquad
 \|\dot W^{(3)}\|_{L^2(\Omega_2)}\le RB,\qquad
 \|\dot\Delta_a^{(2)}\|_{L^2(\Omega_2)}\le B_T.
 \tag{P.16}
\]

The last estimate follows by differentiating
\(\Delta_a^{(2)}=W^{(3)}\phi'(Z_a^{(2)})\), using the pointwise
readout bound in the term \(W^{(3)}\phi''(Z_a^{(2)})\dot Z_a^{(2)}\).
The rank-one norm used for \(\dot U\) is exactly
\(\|v\otimes h\|_{\rm HS}=\|v\|_{L^2}\|h\|_{L^2}\), obtained by
summing its squared action on an orthonormal basis.

The row controls \(-c r_a Q_a\) are integrable for almost every row:
(P.15), \(\|Q_a\|_{L^1}\le\|Q_a\|_{L^2}\), and Fubini give a finite
integral of their absolute values. The Bochner integral equation for \(w\)
therefore has pointwise absolutely continuous representatives on one
probability-one event. Apply the preceding confinement theorem on rational
compact intervals. It gives, at all times of each row path,

\[
 |w(t)|\le |w(0)|+K_G,
 \qquad K_G=D_\delta\quad(\operatorname{rank}G=2),
 \qquad K_G=R_G\quad(\operatorname{rank}G=3).
 \tag{P.17}
\]

This envelope uses no bound on the row-control integrals. An almost-everywhere
differential identity without the integral equation or absolute continuity
would not suffice.

Here is the elementary path-law lemma needed to use these estimates. For
random absolutely continuous \(X:[0,T]\to\mathbb R^q\), suppose uniformly
in a family that

\[
 \mathbb E\int_0^T|\dot X|^2dt\le M,
 \qquad
 \lim_{A\to\infty}\sup_X\mathbb E[
 \|X\|_\infty^2\mathbf1_{\{\|X\|_\infty>A\}}]=0.
 \tag{P.18}
\]

Their laws are totally bounded for \(\mathcal W_2\) with the uniform
path metric. To prove this, interpolate a grid of maximum spacing \(h\).
Writing the interpolation error on each cell as a convex combination of
two endpoint increments and applying Cauchy–Schwarz gives
\(\|X-I_hX\|_\infty^2\le h\int_0^T|\dot X|^2dt\).
Project grid values onto the radius-\(A\) ball and round them to a fixed
finite \(\epsilon\)-net, then interpolate. The resulting \(Y\) takes
values in one finite set of paths and satisfies

\[
 \mathbb E\|X-Y\|_\infty^2\le
 3hM+3\mathbb E[\|X\|_\infty^2
          \mathbf1_{\{\|X\|_\infty>A\}}]+3\epsilon^2.
 \tag{P.19}
\]

Choose \(A\) large, then \(h,\epsilon\) small. Laws on that finite set
have finite nets: round their probability masses to a finite simplex grid,
couple common mass identically, and bound the cost of unmatched mass by the
squared diameter times its mass. This proves total boundedness with explicit
couplings; no field-equation compactness theorem is being imported.

Apply the lemma separately in the two populations to

\[
 X_1=(w,(Z_a^{(1)},H_a^{(1)})_{a=1}^3),\qquad
 X_2=(W^{(3)},(H_a^{(2)},\Delta_a^{(2)})_{a=1}^3).
 \tag{P.20}
\]

The derivative condition follows from (P.16) and
\(|\dot Z_a^{(1)}|\le|\dot w|\). The second tuple has a deterministic
supremum bound by (P.15); the first is dominated by a fixed multiple of
\(1+|w(0)|+K_G\). Its fixed Gaussian squared envelope is uniformly
integrable. Thus both families of same-layer joint laws are totally bounded
in \(\mathcal W_2(C([0,T]))\).

Along any convergent subsequence of these two laws, predictions, loss and
the readout and middle kernel blocks converge uniformly. Their formulas are

\[
 f_a=\mathbb E_2[W^{(3)}H_a^{(2)}],\quad
 K^{(3)}_{ab}=\mathbb E_2[H_a^{(2)}H_b^{(2)}],\quad
 K^{(2)}_{ab}=\mathbb E_1[H_a^{(1)}H_b^{(1)}]
                  \mathbb E_2[\Delta_a^{(2)}\Delta_b^{(2)}].
 \tag{P.21}
\]

For example, under any coupling the output difference is at most
\(B\mathbb E\|W^{(3)}-\widetilde W^{(3)}\|_\infty+
 c_T\mathbb E\|H_a^{(2)}-\widetilde H_a^{(2)}\|_\infty\).
The other products have the same estimate, and bounded outputs transfer it
to the half-sum loss. No cross-population coupling is used to take a product
inside an expectation.

Raw second preactivations, incoming fields \(Q_a\), and the first kernel
\(G_{ab}\mathbb E_1[\Delta_a^{(1)}\Delta_b^{(1)}]\) are absent from
(P.20)–(P.21). Their bounded second moments and time derivatives alone give
no uniform integrability of squared spatial amplitudes. These laws also do
not identify the initialized action on a common space, a unique limit,
true limiting velocities, cap removal, or actual finite GF/GD convergence.

### P.15 Protected backward forces and exact learned returns

On any supplied path above, let \(P\) be multiplication by the indicator
of the initially protected rows, and write \(g_a=P H_a^{(1)}(0)\).
Invariance gives \(P H_a^{(1)}(t)=g_a\). Let
\(\mathsf G:\mathbb R^3\to L^2(\Omega_1)\) have columns \(g_a\)
and \(Q=\mathsf G^*\mathsf G\succeq\lambda_\delta I\).
Projection of the exact matrix update gives

\[
 \|\dot U\|_{\rm HS}^2\ge\|\dot U P\|_{\rm HS}^2
 =\sum_{a,b}Q_{ab}r_a r_b
                     \mathbb E_2[\Delta_a^{(2)}\Delta_b^{(2)}]
 \ge\lambda_\delta\sum_a r_a^2\|\Delta_a^{(2)}\|_{L^2}^2.
 \tag{P.22}
\]

To verify the last inequality, expand the three vectors
\(r_a\Delta_a^{(2)}\) in an orthonormal basis and apply
\(Q\succeq\lambda_\delta I\) to each real coefficient triple, then
sum. The first inequality holds because an orthogonal domain projection
cannot increase the Hilbert–Schmidt norm. From (P.13),
\(\int_0^T\sum_a r_a^2\|\Delta_a^{(2)}\|_{L^2}^2dt
\le E_0/\lambda_\delta\).

There is also an exact primitive. Since
\(\mathbb E_1[H_a^{(1)}(t)g_b]=Q_{ab}\),

\[
 J_a(t):=\int_0^t r_a(v)\Delta_a^{(2)}(v)dv
      =-U(t)\mathsf GQ^{-1}e_a.
 \tag{P.23}
\]

Differentiate the right-hand side using (P.3); it is
\(r_a\Delta_a^{(2)}\), and its initial value is zero.
Moreover \(\|\mathsf GQ^{-1}\|_{\rm op}\le\lambda_\delta^{-1/2}\),
because its squared Gram is \(Q^{-1}\). Thus
\(\|J_a(t)-J_a(s)\|_{L^2}\le
\lambda_\delta^{-1/2}\|U(t)-U(s)\|_{\rm HS}\).
If the supplied true flow has the exact energy identity, this is at most
\(\sqrt{(t-s)(\mathcal E(s)-\mathcal E(t))/\lambda_\delta}\).
The estimate for a merely dissipative path follows instead with its
assumed energy drop or with the total bound \(E_0\); (P.13) alone is not
silently strengthened into an arbitrary-subinterval energy identity.

For any bounded activation \(|\phi|\le B\), \(|\phi'|\le D\), an
existing path with exact readout/matrix equations has additional pointwise
bounds. Suppose \(\|W^{(3)}(0)\|_\infty=c_0<\infty\), and put
\(\mathcal R(t)=\int_0^t\sum_a|r_a(v)|dv\). Then

\[
 \|W^{(3)}(t)\|_\infty\le c_0+B\mathcal R(t),\qquad
 \|\Delta_a^{(2)}(t)\|_\infty\le D(c_0+B\mathcal R(t)).
\]

The learned increment has the actual integral kernel

\[
 u_t(\omega_2,\omega_1)=
 -\sum_a\int_0^t r_a(v)\Delta_a^{(2)}(v,\omega_2)
                                  H_a^{(1)}(v,\omega_1)dv.
\]

It is bounded by
\(\mathcal U(t)=BD[c_0\mathcal R(t)+B\mathcal R(t)^2/2]\).
Indeed \(\mathcal R'=
\sum_a|r_a|\) almost everywhere, so integration of
\(BD(c_0+B\mathcal R)\mathcal R'\) gives this expression.
On probability spaces, integrating a bounded kernel against a bounded
field gives

\[
 \|U H_a^{(1)}\|_\infty\le B\mathcal U(t),\qquad
 \|U^*\Delta_a^{(2)}\|_\infty
       \le D(c_0+B\mathcal R(t))\mathcal U(t).
 \tag{P.24}
\]

For the finite normalized model the kernel is \(n U_{ij}\), not
\(U_{ij}\); its matrix update has the explicit factor \(1/n\).
Hence the same bounds follow by normalized finite sums. Finite Gaussian
readout is retained in \(c_0\). It tends to zero in probability under
stored variance \(n^{-2}\), since
\(\mathbb P(c_0>\epsilon)\le2n e^{-n^2\epsilon^2/2}\).
For the three-sample half-sum loss,
\(\mathcal R(t)\le\sqrt{6\mathcal E(0)}t\) on energy-monotone paths.
These are compact-time statements, not a finite total residual-clock claim.
The unknown initial-action returns in
\(Z_a^{(2)}=A_0H_a^{(1)}+UH_a^{(1)}\) and
\(Q_a=A_0^*\Delta_a^{(2)}+U^*\Delta_a^{(2)}\) remain separate.

### P.16 Why the protected Gram is not a fitting theorem

For the plateau activation above, take any fixed \(n\ge3\) and mixed
binary labels. There is a positive-probability initial first-layer event
with a positive protected Gram: the six open balls supply feature vectors
spanning \(\mathbb R^3\), so choose three independent rows in three
linearly independent cells. Independent additional rows cannot decrease
the Gram. Conditional on such a feature matrix, each second-layer
preactivation triple is Gaussian with positive-definite covariance
\((h_a^{(1)})^Th_b^{(1)}/n\). Its density is strictly positive, so the
finite intersection event that every second-layer preactivation exceeds
one has positive conditional probability.

On that event every second-layer gate is zero and each top feature is
\(B=3/2\). Thus both hidden updates vanish. The readout follows its
original equation, while the second-layer preactivations stay fixed.
Writing \(s_n=(\mathbf1^T W^{(3)})/n\), the outputs all equal
\(B s_n\), and
\(\dot s_n=-B\sum_a(Bs_n-y_a)\). Direct solution of this scalar linear
equation gives convergence of every output to
\(\bar y=\tfrac13\sum_a y_a\), with loss tending to
\(\tfrac12\sum_a(y_a-\bar y)^2>0\). The readout kernel is
\(B^2\mathbf1\mathbf1^T\), of rank one, and the other blocks vanish.
No special readout initialization is needed.

This is a positive-probability event at each fixed width, with no claimed
probability lower bound as width grows. It disproves a deterministic
implication from protected first features to fitting; it does not disprove
a typical population fitting or convergence theorem. A single saturated
second-layer row is not similarly protected in general, because its
preactivation still has the term \((W^{(2)}\dot h_a^{(1)})_j\).

A second exact obstruction concerns discarding raw plateau depths. Use the
explicitly different activation
\(\widetilde\phi(z)=2\phi(z/2)-1\), with plateau values zero and two
outside \([-2,2]\), and \(\widetilde\phi(0)=1\).
At width one choose
\(G=\begin{psmallmatrix}1&\rho&0\\\rho&1&0\\0&0&1\end{psmallmatrix}\),
\(0<\rho<1-\delta\). It is realized by
\(u_1=e_1,u_2=\rho e_1+\sqrt{1-\rho^2}e_2,u_3=e_3\).
Set the first preactivation triple to \((2+s,0,3)\), the stored middle
weight to \(1/4\), and the stored readout to two. All \(s>0\) give the
same first features \((2,1,2)\) and the same other parameter blocks.
Positive-definiteness of \(G\) makes each such preactivation triple a
valid raw first row.

Initially \(f_2=2\widetilde\phi(1/4)>2\) and
\(q_2=\tfrac12\widetilde\phi'(1/4)>0\), so \(r_2q_2>0\) for any
binary label. Until the first sample leaves its plateau, the equations are

\[
 \dot z_1=-\rho\widetilde\phi'(z_2)r_2q_2,\quad
 \dot z_2=-\widetilde\phi'(z_2)r_2q_2,\quad \dot z_3=0.
\]

The subsystem for \(z_2,W^{(2)},W^{(3)}\) is independent of \(s\)
on this interval and has a smooth local solution. Continuity supplies a
fixed short interval on which \(-\dot z_1\ge c>0\), and also bounds its
total decrease. Choose one positive \(s\) smaller than that decrease and
another larger than it. The first trajectory crosses \(z_1=2\) with
negative derivative and its feature becomes less than two; the second
remains on the plateau. Their initial feature and remaining-parameter states
agree but their feature paths differ. Every training block follows the raw
half-sum gradient, and the full raw finite ODE is smooth and unique.

Thus the feature-only state loses information needed for autonomous unique
restart on arbitrary finite states with correlated inputs. The constructed
states are not claimed to be reached from canonical Gaussian initialization.
Neither this obstruction nor (P.22)–(P.24) closes the reverse-field or
population-identification gaps.

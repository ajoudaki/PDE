# Fixed smooth plateaus: invariant three-input feature geometry

2026-09-08. This is an independent geometry/invariance result for the exact architecture and raw dynamics in `CONTRACT.md`. It uses a **different fixed activation** from the contract's principal affine–tanh mixture. The activation is fixed once, independently of the inputs, their separation, width, and training time. This note does not prove a global population solution or a finite-width convergence theorem.

## 1. Activation and conclusions

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
 \boxed{\quad K_{\rm fr}:=\mathbb E[\mathbf1_P(w)h(w)h(w)^T]
      \succeq \lambda_\delta I_3,
 \qquad \lambda_\delta=\frac1{240}e^{-22/\delta}.\quad}
\]

This includes singular, rank-two input Grams. Every initial row in \(P\) is exactly frozen under raw GF and simultaneous raw GD, so this is an invariant part of the first-layer feature Gram. The coefficient is deliberately crude but explicit.

There is also a positive fraction of derivative-active rows: under any raw GF satisfying the locally integrable row-coefficient condition stated below, a row initially outside \(P\) never enters \(P\) in finite time. Consequently the fraction of rows with at least one strictly positive first-layer activation derivative remains at least

\[
 p_{\rm act}=\mathbb P(|G|<1)>0,\qquad G\sim N(0,1).
\]

Derivative activity must not be confused with nonzero feature velocity. That stronger assertion requires information about the physical residuals and return fields.

## 2. Smoothness and moderate fixed bounds

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

## 3. Six plateau balls that detect every coefficient

Let \(S=\operatorname{span}(u_1,u_2,u_3)\). Its dimension \(m\) is either two or three: rank one would force two unit inputs to have inner product \(1\) or \(-1\), contradicting separation. The orthogonal projection of \(w\) onto \(S\) is standard Gaussian in \(S\). This can be seen by completing an orthonormal basis of \(S\) and factoring the standard Gaussian density in those coordinates. Features depend only on this projection. Thus all probability estimates below take place in dimension at most three, regardless of \(d\).

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
 \geq c_m e^{-169/(8\delta)},
 \quad c_2=\tfrac18,\quad c_3=\frac1{12\sqrt{2\pi}}.
\]

Here the constants follow from the disk area \(\pi/4\) and three-dimensional ball volume \(\pi/6\), multiplied by the respective Gaussian normalizations. Both constants exceed \(1/40\), and \(169/8<22\). Therefore every one of the six balls has probability at least

\[
 p_\delta:=\frac1{40}e^{-22/\delta}.
\]

## 4. Positive definite invariant feature Gram

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

## 5. Exact invariance for the original raw dynamics

For a first-layer row, use \(w=\sqrt d\,W_{\rm row}\). The contract's raw GF gives exactly

\[
 \dot w(t)=-\sum_{i=1}^3r_i(t)q_i(t)\phi'(w(t)\cdot u_i)u_i.
 \tag{5.1}
\]

For a population row, \(q_i(t)\) means the value at that row's Gaussian coordinate. For a finite row, it is the corresponding component of the actual \(A^Tb_i\). No different metric or surrogate return field is used.

**Row lemma.** Suppose a row is absolutely continuous on \([0,T]\), satisfies (5.1) almost everywhere, and

\[
 \int_0^T\sum_i|r_i(t)q_i(t)|\,dt<\infty.
 \tag{5.2}
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

For every existing finite GF solution on a compact interval, its continuous finite-dimensional coefficients satisfy (5.2). For a population GF, a sufficient condition is

\[
 \sum_i\int_0^T|r_i(t)|\,\|q_i(t)\|_{L^2(\Omega_1)}\,dt<\infty.
\]

Indeed, integration over the probability space, followed by \(\|q\|_{L^1}\leq\|q\|_{L^2}\), shows that (5.2) holds for almost every row. An absolutely continuous \(L^2\) row path with an integrable \(L^2\) velocity has an almost-everywhere absolutely continuous representative: its Bochner integral formula can be represented pointwise because the integral of the pointwise absolute velocity is finite by the same inequality. Thus the row lemma applies whenever the population equation has this stated pointwise interpretation. This note does not assume that merely naming a strong solution automatically supplies unproved return-field bounds.

Consequently, for each such population flow,

\[
 \mathbb E[\mathbf1_{P}(w(0))h_i(t)h_j(t)]
 =(K_{\rm fr})_{ij},
 \qquad
 \big(\langle h_i(t),h_j(t)\rangle\big)_{i,j=1}^3
 \succeq K_{\rm fr}\succeq\lambda_\delta I_3.
\]

For simultaneous raw GD, a row initially in \(P\) has zero update at the first step and, inductively, at every step. This is exact for any step size, in particular the stipulated physical step \(n^{-2}\). The no-entry statement for initially active rows is a continuous-time uniqueness statement; its discrete analogue would need a step-size estimate.

## 6. Elementary finite-sample version

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

## 7. Quantitative initial nonaffinity

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

## 8. What remains active, and what this does not show

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

using the two possible dimensions and their ball-density constants from Section 3.

Under the row lemma, membership in \(P\) is unchanged, so for every finite training time

\[
 \mathbb P\left(\max_i\phi'(w(t)\cdot u_i)>0\right)
 =\mathbb P(w(0)\notin P)
 \geq\mathbb P(|G|<1)=p_{\rm act}>0.
\]

The same row labels remain in the active complement at all finite times, assuming (5.2) on all compact intervals. This statement supplies neither a uniform-in-time positive lower bound on those derivatives nor a positive speed. In particular the contract's population initialization has \(C(0)=0\), hence \(q_i(0)=0\) and \(\dot w(0)=0\), despite the positive fraction of activation derivatives. Establishing actual subsequent feature motion is a separate physical-dynamics question.

Finally, the invariant first-layer Gram is not by itself a lower bound for the full prediction kernel: the other factors in the true kernel blocks, especially \(b_i=\phi'(v_i)C\), still have their actual evolving values. The result settles the proposed plateau geometry and invariance mechanism, including rank-two inputs, while leaving those dynamic obligations open.

# Independent adversarial mathematical review

Candidate: `/tmp/l3-two-sample-Un7kw9/QUARTIC_TWO_DRIVER_REGULARIZED_FRAME.md`

Verified SHA256:

`db2eae51d2b8c7b0ed14d911416117b1de3b2bca75cf4bbcf1eeb7e57eaaa3c0`

**Scoped verdict: PASS.** For fixed \(e>0\) and every finite time horizon, the candidate establishes global existence and uniqueness for the prescribed ODE with arbitrary signed \(L^1\) drivers, joint Fréchet differentiability with respect to both initial coordinates and both drivers, and the asserted operator bound

\[
\|DS(M_0,V_0,p,q)\|
\le C_eR^{12}\exp(C_eR^{4/3}).
\]

Its conclusion about every finite positive moment is valid under its stated square-exponential input-tail hypothesis. This includes Gaussian random elements of the stated Banach input space, as explained below. The proof does not establish sharpness of the response exponent, a bound depending only on the initial state, or a network theorem.

No substantive mathematical correction is necessary. Two precision improvements are recorded at the end: parenthesize the elementary inequality used for the separate tail assumptions, and distinguish optimization of this estimate from optimality of the actual response growth.

This review used only the named candidate and the explicitly requested `solve-math-rigorously` skill at `/etc/codex/skills/solve-math-rigorously/SKILL.md`. No histories, ledgers, other proofs or reviews, external sources, experiments, or agents were used. The candidate was not edited.

## 1. Input space, existence, uniqueness, and state estimates

The natural precise domain is

\[
\mathcal B=\mathbb R^2\times L^1([0,T];\mathbb R)^2,
\qquad
\|x\|_{\mathcal B}=|M_0|+|V_0|+\|p\|_1+\|q\|_1,
\]

with output \(C([0,T];\mathbb R^2)\) in the supremum of the coordinate sum norm. Solutions are absolutely continuous and satisfy the ODE almost everywhere. In particular, changing a driver on a null set does not change the solution.

Write the two coefficient fields as

\[
f(M,V)=(a(M),0),\qquad g(M,V)=(Vb(M),a(M)).
\]

The activation derivatives displayed in the candidate are correct. Both fields are smooth; their first and second derivatives are bounded on each bounded state ball. The elementary bounds \(1\le a\le L\) and \(|b|\le4e\) hold on the entire real line. Consequently, on a fixed state ball the Lipschitz majorant is \(K(|p|+|q|)\), an integrable function. Local contraction therefore needs small integrated driver mass, not bounded driver amplitudes.

The proposed a priori estimates are valid without sign restrictions. Indeed,

\[
|V(t)|\le |V_0|+LQ_t,
\qquad Q_t=\int_0^t|q(s)|\,ds,
\]

and hence

\[
\begin{aligned}
|M(t)|
&\le |M_0|+L\int_0^t|p(s)|\,ds
  +4e\int_0^t(|V_0|+LQ_s)|q(s)|\,ds\\
&\le |M_0|+LP+4e|V_0|Q+2eLQ^2.
\end{aligned}
\]

Here \(Q_t\) is absolutely continuous and \((Q_t^2)'=2Q_t|q(t)|\) almost everywhere. This verifies the coefficient \(2eL\) in (3).

These estimates place the entire trajectory in a bounded state ball determined by \(e\) and the input size. On that ball the velocity has an integrable bound \(K(|p|+|q|)\). A solution approaching a finite endpoint is therefore Cauchy and has a limiting state, from which local existence extends it. The same integrable Lipschitz estimate proves uniqueness. There is no finite-time escape or hidden driver regularity assumption.

In particular,

\[
\sup_t|V(t)|\le LR,\qquad \sup_t|M(t)|\le C_eR^2.
\]

No factor involving \(T\) is needed: every growth estimate integrates \(|p|\) or \(|q|\). This verifies (3), (4), and the claimed independence from the time horizon at fixed driver masses.

## 2. Joint Fréchet differentiability, including \(L^1\) forcing

The differentiability paragraph in the candidate is sufficient. The following explicit remainder calculation checks that it proves a joint Fréchet derivative, rather than only directional derivatives.

Fix a base input \(x\in\mathcal B\). Let its perturbation be \(\delta=(u_0,v_0,r,s)\), with \(\varepsilon=\|\delta\|_{\mathcal B}\le1\), and let \(z\) and \(z+\Delta\) be the base and perturbed state paths. Estimate (3) places every such path in a common bounded, convex state ball. On this ball choose bounds \(K_0,K_1,K_2\) for the fields and their first and second derivatives, in the relevant induced norms.

The integral difference equation gives

\[
|\Delta(t)|_1
\le (1+K_0)\varepsilon
 +K_1\int_0^t(|p|+|q|)|\Delta|_1\,ds.
\]

Iterating this scalar integral inequality, or summing its ordered integral series, yields

\[
\|\Delta\|_\infty
\le (1+K_0)e^{K_1(P+Q)}\varepsilon.
\]

Let \(y=(m,v)\) solve the linear equation

\[
y'=[pDf(z)+qDg(z)]y+f(z)r+g(z)s,
\qquad y(0)=(u_0,v_0).
\]

Its coefficients and forcing are integrable. The same integral estimate gives a bounded linear map \(\delta\mapsto y\) into the output space. Since

\[
Df=\begin{pmatrix}b&0\\0&0\end{pmatrix},
\qquad
Dg=\begin{pmatrix}Vb'&b\\b&0\end{pmatrix},
\]

this is exactly (9), with every initial and forcing direction present.

To check the remainder, set \(\rho=\Delta-y\). Its equation has homogeneous coefficient \(pDf(z)+qDg(z)\), zero initial value, and forcing

\[
\begin{aligned}
N={}&p\,[f(z+\Delta)-f(z)-Df(z)\Delta]\\
&+q\,[g(z+\Delta)-g(z)-Dg(z)\Delta]\\
&+r\,[f(z+\Delta)-f(z)]
 +s\,[g(z+\Delta)-g(z)].
\end{aligned}
\]

Taylor's formula on the common ball implies

\[
\|N\|_1
\le \tfrac12K_2(P+Q)\|\Delta\|_\infty^2
 +K_1(\|r\|_1+\|s\|_1)\|\Delta\|_\infty
\le C_x\varepsilon^2.
\]

Another integral estimate gives \(\|\rho\|_\infty\le C_x\varepsilon^2\). This is uniform over perturbations of the given sum norm and proves Fréchet differentiability. In particular, all cross-effects between perturbed states and perturbed drivers are included in the last line of \(N\). No \(L^\infty\) norm, smoothness, support restriction, or sign condition is imposed on \(r,s\). Concentrated late forcing is covered.

The constants in this local existence-of-derivative argument may depend on the base input. The later moving-frame estimate supplies the stated quantitative dependence.

## 3. Weight bounds and the cancellation at zero

For each fixed \(h\in(0,1]\), \(w_h\) is smooth and strictly positive on the whole real line. Its logarithmic derivative in (5) is correct. In particular,

\[
w_h(0)=h^3,\qquad \ell_h(0)=0,
\qquad b(0)=b'(0)=0.
\]

Every estimate in (6) checks out:

- \(2h|M|\le h^2+M^2\) bounds the first part of \(\ell_h\) by \(3/(2h)\), and \(|M|^3/(1+M^4)\le1\) bounds its second part by \(8\).
- For \(|M|\le1\), \(w_h\le2^{3/2}\). For \(|M|\ge1\), \(w_h\le2^{3/2}|M|^{-5}\le2^{3/2}\).
- For \(|M|\le1\), \(w_h^{-1}\le4h^{-3}\). For \(|M|\ge1\), \(w_h^{-1}\le4|M|^5\). These imply the displayed global bound \(4h^{-3}(1+|M|^5)\).
- The exact identity \(b/w_h=-4eM^3/(h^2+M^2)^{3/2}\) implies \(|b/w_h|\le4e\). Multiplying the separate upper bounds for \(|b|\) and \(w_h\) gives the claimed bound on \(|bw_h|\).

A direct calculation, without dividing by \(b\), gives

\[
b'(M)=-\frac{12eM^2}{(1+M^4)^2}
       +\frac{32eM^6}{(1+M^4)^3},
\]

whereas

\[
\ell_h(M)b(M)
=-\frac{12eM^4}{(h^2+M^2)(1+M^4)^2}
 +\frac{32eM^6}{(1+M^4)^3}.
\]

Subtracting yields

\[
b'-\ell_hb
=-\frac{12eh^2M^2}{(h^2+M^2)(1+M^4)^2}.
\]

This verifies (7) everywhere, including \(M=0\), and proves (8), since both \(M^2/(h^2+M^2)\) and \((1+M^4)^{-2}\) are at most one. The zero-curvature point causes no singularity, jump, or missing crossing term. The calculation is independent of every driver and state sign.

## 4. Moving frame and simultaneous operator bound

For the fixed base path, define \(u=m/w_h(M)\). This is a linear change of variables on the first variation along that path. It is not the derivative of the nonlinear expression \(M/w_h(M)\).

The base path and variation are absolutely continuous. The functions defining the frame and its inverse have bounded derivatives on the compact range of that fixed path. Thus the chain and product rules apply almost everywhere, giving

\[
u'=\frac{m'}{w_h}-\ell_hM'u.
\]

Substituting (1) and (9) produces (10) exactly. In particular, subtracting \(\ell_hM'u\) contributes both \(-a\ell_hp\,u\) and \(-V\ell_hbq\,u\). Neither base driver is omitted.

The homogeneous coefficient matrix is

\[
H_h(t)=
\begin{pmatrix}
(b-a\ell_h)p+V(b'-\ell_hb)q &(b/w_h)q\\
bw_hq &0
\end{pmatrix}.
\]

Its induced one-norm is the maximum of the two absolute column sums:

\[
\|H_h\|_1
=\max\left\{
|(b-a\ell_h)p+V(b'-\ell_hb)q|+|bw_hq|,
|(b/w_h)q|
\right\}.
\]

The verified weight bounds give

\[
\|H_h(t)\|_1
\le C_e\big[(1+h^{-1})|p(t)|
 +(1+h^2|V(t)|)|q(t)|\big].
\]

This proves (11). Absolute column sums accommodate negative drivers, negative states, arbitrarily many sign changes, and noncommuting coefficient matrices.

Since

\[
\int_0^T|V(t)||q(t)|\,dt
\le (|V_0|+LQ)Q=A,
\]

the total coefficient integral is bounded by

\[
E_h=C_e[P+P/h+Q+h^2A].
\]

For completeness, the norm of the \(n\)-th ordered integral in the transition matrix is at most

\[
\frac1{n!}\left(\int_s^t\|H_h(\tau)\|_1\,d\tau\right)^n.
\]

This follows by comparing with the product integrand on the full \(n\)-dimensional integration cube and its ordered simplexes; no matrix commutation is used. Summation bounds every forward transition by \(e^{E_h}\). The coefficients are integrable, so the series also supplies the integral-equation solution and its variation-of-constants formula. This verifies (12) and the asserted control on any subinterval.

The forcing vector in the frame is

\[
\left(\frac{a}{w_h}r+\frac{Vb}{w_h}s,\;as\right).
\]

The necessary uniform coefficient bounds are

\[
\sup_t\frac{a(M(t))}{w_h(M(t))}
\le C_eh^{-3}R^{10},
\qquad
\sup_t\left(\left|\frac{Vb}{w_h}\right|+a\right)
\le C_eR.
\]

The power ten comes from \(\sup|M|\le C_eR^2\) and the fifth power in \(w_h^{-1}\). The transformed initial value satisfies

\[
\left|\left(\frac{u_0}{w_h(M_0)},v_0\right)\right|_1
\le C_eh^{-3}R^{10}(|u_0|+|v_0|).
\]

Variation of constants therefore bounds the framed solution by \(C_eh^{-3}R^{10}e^{E_h}\|\delta\|_{\mathcal B}\). Recovering \(m=w_h(M)u\) costs at most the constant \(\max\{2^{3/2},1\}\). There is no second inverse-weight factor at recovery. This proves (13) with the stated sum norms and covers all four derivative components simultaneously.

## 5. Choice of \(h\), the exponent, and edge cases

The chosen parameter

\[
h=\min\left\{1,\left(\frac{1+P}{1+A}\right)^{1/3}\right\}
\]

lies in \((0,1]\) for every input. If \(P\le A\), then

\[
\frac{P}{h}
=\frac{P}{(1+P)^{1/3}}(1+A)^{1/3}
\le(1+P)^{2/3}(1+A)^{1/3},
\]

and

\[
h^2A
=(1+P)^{2/3}\frac{A}{(1+A)^{2/3}}
\le(1+P)^{2/3}(1+A)^{1/3}.
\]

If \(P>A\), then \(h=1\) and

\[
P+P/h+Q+h^2A=2P+Q+A\le3P+Q.
\]

These verify (15). They include \(P=A\), \(P=0\), \(A=0\), and the zero-driver input without division by a vanishing quantity. Furthermore,

\[
A\le LR^2,\qquad
(1+P)^{2/3}(1+A)^{1/3}\le C_eR^{4/3},
\]

using \(R\ge1\). The linear terms \(P+Q\) are also bounded by \(R^{4/3}\). Finally,

\[
h^{-3}=\max\left\{1,\frac{1+A}{1+P}\right\}
\le1+A\le C_eR^2.
\]

Substitution into (13) gives precisely the polynomial power twelve and the exponential power \(4/3\) in (2).

The parameter is fixed after choosing the base input, while (13) already holds for every fixed admissible parameter. It is legitimate to select a different proof parameter for each base input. Fréchet differentiation never differentiates this selection. In particular, the nonsmoothness of \(P,Q\) as functions of the input, or of the minimum at \(P=A\), does not enter the derivative argument.

There is a distinction between the exponent proved here and a sharp exponent for the ODE. For \(P,A>0\), the unconstrained minimizer of \(P/h+Ah^2\) satisfies \(h^3=P/(2A)\). On \(0<h\le1\), the minimum is

\[
\begin{cases}
3\,2^{-2/3}P^{2/3}A^{1/3},&P\le2A,\\
P+A,&P\ge2A.
\end{cases}
\]

Thus (14) is a regularized choice with the appropriate scaling, rather than the exact minimizer. When \(P,Q\) are both proportional to \(R\), the budget permits \(A\) proportional to \(R^2\); balancing these two terms then gives \(R^{4/3}\). This confirms the claimed upper-bound exponent. It supplies no matching lower bound on the actual solution derivative, and none is needed for the candidate's theorem. When \(P=0\), taking \(h\downarrow0\) would also enlarge the inverse-weight prefactor; the positive regularized choice avoids that issue.

## 6. Random inputs and every finite positive moment

Let \(B_e(R)=C_eR^{12}e^{C_eR^{4/3}}\). For every \(k>0\) and every \(\lambda>0\),

\[
\log\big(R^{12k}e^{kC_eR^{4/3}-\lambda R^2}\big)
=12k\log R+kC_eR^{4/3}-\lambda R^2
\longrightarrow-\infty.
\]

The expression is continuous on \([1,\infty)\) and has a finite supremum there. Consequently,

\[
\mathbb E B_e(R)^k
\le C_{e,k,\lambda}\mathbb E e^{\lambda R^2}<\infty.
\]

This proves the moment implication for every finite positive \(k\), including nonintegers. No comparison of \(\lambda\) with \(e,T\), or \(k\) is required. The resulting moment bound may depend on \(k,\lambda\) and the input law; there is no assertion of a constant uniform over all moment orders.

Measurability does not conceal a defect. The input norm, and hence \(P,Q,R\), is continuous on the Banach input space. The solution map is locally Lipschitz by the difference estimate above. For each fixed direction \(d\),

\[
DS(x)d=\lim_{n\to\infty}n[S(x+d/n)-S(x)]
\]

is Borel measurable in \(x\). The input space is separable, so a countable dense subset \(\{d_j\}\) of its unit sphere satisfies

\[
\|DS(x)\|=\sup_j\|DS(x)d_j\|_\infty.
\]

Thus the derivative norm is measurable as well. This argument avoids any need to assume separability of the whole operator space.

To verify the claim about separate square-exponential moments, set

\[
X_1=|M_0|,\quad X_2=|V_0|,\quad X_3=P,\quad X_4=Q.
\]

Cauchy--Schwarz gives the unambiguous inequality

\[
R^2=(1+X_1+X_2+X_3+X_4)^2
\le5\left(1+\sum_{i=1}^4X_i^2\right).
\]

If \(\mathbb E e^{\lambda_iX_i^2}<\infty\) for some \(\lambda_i>0\), choose \(0<\lambda\le\min_i\lambda_i/20\). Hölder's inequality then yields

\[
\mathbb E e^{\lambda R^2}
\le e^{5\lambda}
\prod_{i=1}^4
\left(\mathbb E e^{20\lambda X_i^2}\right)^{1/4}
<\infty.
\]

No independence is used. Ordinary second moments do not imply this hypothesis. Even all finite polynomial moments do not imply it: a positive lognormal variable has all such moments but no positive square-exponential moment. That observation concerns the input-tail hypothesis; it is not a counterexample to the deterministic response bound.

### Gaussian inputs: precise meaning and a self-contained verification

The candidate states a conditional tail theorem. Its Gaussian specialization is valid when the full input is a measurable Gaussian random element of \(\mathcal B\), including correlated or degenerate Gaussian inputs. Merely expressing a driver as an arbitrary nonlinear function of Gaussian variables does not make that driver Gaussian in \(\mathcal B\), nor establish the required tail hypothesis.

Here is an independent verification of the Gaussian norm fact needed for that specialization. It also makes explicit that finite-dimensional forcing is not required.

Let \(Y\) be a centered Gaussian random element of a separable real Banach space, with \(\|Y\|<\infty\) almost surely. Take an independent copy \(Y'\). Then

\[
U=(Y+Y')/\sqrt2,\qquad W=(Y-Y')/\sqrt2
\]

are independent copies of \(Y\). To justify this for Banach-valued variables, every finite collection of continuous linear evaluations is jointly Gaussian; the two displayed groups have zero cross-covariance and each has the original covariance. These finite-dimensional laws determine the Borel law and independence in a separable Banach space. One way to see the last point is to choose a countable norming family of linear functionals from a dense subset of the unit sphere and Hahn--Banach; the norm, its translates, and therefore the Borel sigma algebra are generated by those functionals.

Choose \(r>0\) such that \(c=\mathbb P(\|Y\|\le r)\ge3/4\), and write \(\psi(t)=\mathbb P(\|Y\|>t)\). On the event \(\|Y\|\le r,\ \|Y'\|>t\), both \(\|U\|\) and \(\|W\|\) exceed \((t-r)/\sqrt2\). Independence therefore gives

\[
c\psi(t)\le\psi((t-r)/\sqrt2)^2.
\]

Set \(t_0=r\) and \(t_{n+1}=\sqrt2t_n+r\). Since \(\psi(t_0)/c\le1/3\), induction yields

\[
\psi(t_n)\le c\,3^{-2^n}.
\]

With \(D=r(1+1/(\sqrt2-1))\), the recurrence gives \(t_n\le D2^{n/2}\). For \(t_n\le t<t_{n+1}\), monotonicity thus implies

\[
\psi(t)\le c\exp\left(-\frac{\log3}{2D^2}t^2\right),
\qquad t\ge r.
\]

For sufficiently small \(\alpha>0\), Tonelli's theorem applied to the nonnegative integrand in

\[
\mathbb E e^{\alpha\|Y\|^2}
=1+\int_0^\infty2\alpha t e^{\alpha t^2}\psi(t)\,dt
\]

now proves finiteness.

This also covers a general, possibly noncentered Gaussian random element \(X\) without assuming its mean in advance. For an independent copy \(X'\), \(X-X'\) is centered Gaussian, so \(\mathbb E e^{\beta\|X-X'\|^2}<\infty\) for some \(\beta>0\). Choose \(r\) with \(c=\mathbb P(\|X'\|\le r)>0\). On that event,

\[
\|X\|^2\le2\|X-X'\|^2+2r^2.
\]

Independence of \(X\) and \(X'\) consequently gives

\[
c\mathbb E e^{(\beta/2)\|X\|^2}
\le e^{\beta r^2}\mathbb E e^{\beta\|X-X'\|^2}<\infty.
\]

Apply this result to the separable space \(\mathcal B\). Since \(R=1+\|X\|_{\mathcal B}\) and \(R^2\le2+2\|X\|_{\mathcal B}^2\), its square-exponential moment is finite for some positive parameter. The candidate's argument therefore gives every finite positive response moment for Gaussian inputs in this precise sense. This reasoning does not assume independence among initial coordinates or drivers.

## 7. Necessary corrections and scope of the verdict

There is no necessary change to equations (1)--(15), the differentiability conclusion, or the conditional moment theorem.

Two wording clarifications would improve precision:

1. Replace “five times the sum of their squares plus one” by the displayed inequality \(R^2\le5(1+\sum_{i=1}^4X_i^2)\). If the original phrase were read as \(R^2\le5\sum_iX_i^2+1\), that literal inequality would be false; for example, all four \(X_i=1/10\) give \(R^2=1.96>1.20\). The intended Cauchy--Schwarz bound, with the constant five also multiplying one, proves the claimed conclusion.
2. Describe \(4/3\) as the exponent obtained by balancing this proof's coefficient bound. No sharpness result for the true derivative, nor optimality of the polynomial factor \(R^{12}\), has been proved or is needed.

The PASS is for the prescribed two-coordinate ODE and the stated input-tail assumption. The proof allows arbitrary signed \(L^1\) drivers and arbitrary signed \(L^1\) derivative directions, retains both base drivers throughout the frame equation, and remains valid at zero crossings. It provides no estimate of the drivers from a population \(L^2\) bound, no higher-order response theorem, and no network continuation or transport theorem. Those are outside this candidate's asserted result.

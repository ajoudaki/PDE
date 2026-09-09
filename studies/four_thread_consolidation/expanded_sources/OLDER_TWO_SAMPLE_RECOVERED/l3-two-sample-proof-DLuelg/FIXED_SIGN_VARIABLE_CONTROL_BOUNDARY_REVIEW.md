# Independent adversarial review

Date: 2026-09-06.

Mathematical input: /tmp/l3-two-sample-proof-DLuelg/FIXED_SIGN_VARIABLE_CONTROL_BOUNDARY.md, read in full, 170 lines, 7310 bytes.

Input SHA-256:

    28ae2496937d65ec80a8e727519f60cac146574fbcabcfec6fbde57f11364c9f

The hash was checked again after the mathematical audit and before writing this review. The candidate was not edited.

Isolation: I read the requested solve-math-rigorously procedural skill at /etc/codex/skills/solve-math-rigorously/SKILL.md myself. The candidate above was the sole mathematical source. I did not consult project files, history, other notes or reviews, agents, experiments, or external mathematical sources. The calculations below are independent analytic checks.

## Verdict

The standalone prescribed-control theorem and the counterexample pass. For the Euclidean induced operator norm, equations (2), (4), (5), and (10) have the stated constants. The proof covers every admissible correlation and coordinate-sign pattern, merely integrable controls, arbitrarily changing component ratios, and vanishing components. The example proves sharpness of the exponent power \(1/3\), and failure of a uniform polynomial bound in control cost, even on a fixed time interval.

There are no required mathematical repairs to these results. The regularity argument is compressed but valid; a complete justification is supplied below.

One contextual sentence cannot be independently certified from the permitted input: lines 160–161 compare (1) to an unspecified first-layer characteristic and refer to “its specified factor 1/2.” The note contains no such characteristic equation or definition of its forcing. This does not affect the theorem for the explicitly displayed equation (1). I give the exact conditional normalization below, without asserting a link to a trained system.

## 1. Setup, normalization, and every sign case

Interpret the unqualified tangent norm as the Euclidean induced operator norm. Take a finite horizon \(T\geq0\), \(u\in L^1([0,T];\mathbb R^2)\), and a prescribed control that is held fixed when differentiating in \(z_0\).

Let
\[
S=\operatorname{diag}(s_1,s_2),\qquad (x,y)^T=Sz,\qquad
r=\rho s_1s_2.
\]
Since \(p\) is even and \(Su=(|u_1|,|u_2|)^T\) almost everywhere,
\[
SC S=C_r=
\begin{pmatrix}1&r\\r&1\end{pmatrix},\qquad
\binom{x'}{y'}=
C_r\binom{\alpha/(1+x^2)}{\beta/(1+y^2)},
\]
where
\[
\alpha=|u_1|/10,\quad \beta=|u_2|/10,\quad
U=\int_0^T(\alpha+\beta)\,dt.
\]
Thus the factors \(1/10\) in the equation and the cost agree exactly. The candidate makes no hidden time change in this reduction.

The reflected flow derivative is \(S(D_{z_0}z(T))S\), so its Euclidean operator norm is unchanged. Also \(|r|=|\rho|=k\) and \(\|(x(0),y(0))\|_1=\|z_0\|_1\).

The cases are exhaustive:

| Original correlation | Chosen coordinate signs | Reflected correlation and proof branch |
| --- | --- | --- |
| \(\rho>0\) | \(s_1s_2=1\) | \(r>0\), monotonicity argument |
| \(\rho>0\) | \(s_1s_2=-1\) | \(r<0\), cubic cost argument |
| \(\rho<0\) | \(s_1s_2=1\) | \(r<0\), cubic cost argument |
| \(\rho<0\) | \(s_1s_2=-1\) | \(r>0\), monotonicity argument |
| \(\rho=0\) | either | \(r=0\), monotonicity argument |

A coordinate control that is identically zero can be assigned either sign. The argument applies to any admissible assignment. Controls that vanish only on subsets of time cause no problem: nothing divides by \(\alpha,\beta,A,B\), or a component ratio.

The assumption \(k<1\) is used essentially for positive definiteness and \(\delta=1-k>0\). No assertion uniform as \(k\uparrow1\) is made.

## 2. Carathéodory existence and initial-state differentiability

The claims at lines 35–45 are valid for \(L^1\) controls. Here is a full verification that does not assume time continuity of the control.

Write \(q(v)=(1+v^2)^{-1}\). Its derivatives satisfy
\[
|q|\leq1,\qquad
|q'|=\frac{2|v|}{(1+v^2)^2}\leq1,\qquad
|q''|=\frac{|6v^2-2|}{(1+v^2)^3}\leq2.
\]
For the reflected vector field \(F(t,X)=C_r(\alpha q(x),\beta q(y))^T\), put
\[
g(t)=(1+k)(\alpha(t)+\beta(t)),\qquad
\Lambda=\int_0^Tg(t)\,dt=(1+k)U.
\]
The spectral norm of \(C_r\) is \(1+k\), and consequently
\[
|F(t,X)|_2\leq g(t),\qquad
\|D_XF(t,X)\|_2\leq g(t),
\]
\[
\|D_XF(t,X)-D_XF(t,Y)\|_2
\leq2g(t)|X-Y|_2
\]
for almost every \(t\). These bounds are global in the state, and \(g\in L^1\).

Partition \([0,T]\) into finitely many intervals on each of which the integral of \(g\) is less than \(1/2\). Such a partition exists by absolute continuity of the integral. On each interval the integral-equation map on continuous paths has contraction constant less than \(1/2\). It maps continuous paths to absolutely continuous paths because its integrand is measurable and dominated by \(g\). Iterating the resulting solutions proves global existence and uniqueness. The speed bound also precludes finite-time escape.

For completeness, the integral estimate used here and below is: if
\[
a(t)\leq a_0+\int_0^t g(s)a(s)\,ds,\qquad g\geq0,
\]
then \(a(t)\leq a_0e^{\int_0^t g}\). Indeed, setting
\(v(t)=a_0+\int_0^tga\) gives \(v'\leq gv\); multiplication by
\(e^{-\int_0^t g}\) and integration proves the claim.

Let \(X(t;a)\) be the solution from \(a\), and let
\(\Delta(t)=X(t;a+h)-X(t;a)\). The preceding estimate gives
\[
\sup_{0\leq t\leq T}|\Delta(t)|_2\leq e^\Lambda|h|_2.
\]
The linear integral equation
\[
J'=D_XF(t,X(t;a))J,\qquad J(0)=I_2
\]
has a unique absolutely continuous solution by the same interval argument. Taylor's formula and the Lipschitz bound on \(D_XF\) give a remainder \(r_h(t)\) satisfying
\[
F(t,X+\Delta)-F(t,X)
=D_XF(t,X)\Delta+r_h(t),\qquad
|r_h(t)|_2\leq g(t)|\Delta(t)|_2^2.
\]
Therefore \(W=\Delta-Jh\) satisfies
\[
W'=D_XF(t,X)W+r_h,\qquad W(0)=0,
\]
and
\[
\sup_{0\leq t\leq T}|W(t)|_2
\leq \Lambda e^{3\Lambda}|h|_2^2.
\]
This proves a Fréchet initial-state derivative, not merely existence of coordinatewise directional derivatives. The same bounds show continuity of \(J\) with respect to the initial state. Thus the candidate's average-derivative and dominated-convergence argument is justified, and all subsequent chain rules are valid almost everywhere along absolutely continuous paths.

These statements concern a frozen prescribed control. Differentiating a control that itself varies with the initial condition would be a different derivative.

## 3. Tangent energy and constants

Set
\[
A=\frac{\alpha}{1+x^2},\quad B=\frac{\beta}{1+y^2},\quad
H(v)=\log(1+v_-^2),\quad f=-H'.
\]
At \(v=0\), both one-sided derivatives of \(H\) equal zero. Hence \(H\) is \(C^1\), and
\[
f(v)=
\begin{cases}2|v|/(1+v^2),&v<0,\\0,&v\geq0,\end{cases}
\qquad 0\leq f\leq1.
\]
The equality \(f(0)=0\) eliminates any difficulty at crossings through zero.

For a tangent vector \(v(t)\), define
\[
E=v^TC_r^{-1}v,\qquad
C_r^{-1}=\frac1{1-r^2}
\begin{pmatrix}1&-r\\-r&1\end{pmatrix}.
\]
Completing the square in both ways gives
\[
E=v_1^2+\frac{(v_2-rv_1)^2}{1-r^2}
=v_2^2+\frac{(v_1-rv_2)^2}{1-r^2}.
\]
Thus \(v_i^2\leq E\), exactly as claimed; no extra factor involving \(k\) is needed at this step.

The variational equation is
\[
v'=C_r Dv,\qquad
D=\operatorname{diag}\left(
-\frac{2\alpha x}{(1+x^2)^2},
-\frac{2\beta y}{(1+y^2)^2}
\right).
\]
Since \(C_r\) and \(D\) are symmetric,
\[
E'=2v^TDv.
\]
For \(x<0\), the first diagonal entry is \(Af(x)\); for \(x\geq0\), it is nonpositive while \(Af(x)=0\). The corresponding statement holds for \(y\). Consequently
\[
E'\leq2\bigl(Af(x)v_1^2+Bf(y)v_2^2\bigr)
\leq2hE,\qquad h=Af(x)+Bf(y).
\]
Here \(0\leq h\leq A+B\leq\alpha+\beta\), so \(h\in L^1\). Applying the absolutely continuous integrating factor yields
\[
E(T)\leq E(0)e^{2I},\qquad
I=\int_0^T h(t)\,dt\leq U.
\]
The eigenvalues of \(C_r\) are \(1+r\) and \(1-r\). Hence
\[
\frac{|v|_2^2}{1+k}\leq E\leq
\frac{|v|_2^2}{1-k}.
\]
It follows that
\[
\|D_{z_0}z(T)\|_2
\leq \sqrt{\frac{1+k}{1-k}}\,e^I.
\]
This verifies all coefficients in (4), including the square root rather than the full condition number, and the absence of an extra factor of two in the exponential for the tangent norm.

## 4. Nonnegative reflected correlation

For \(r\geq0\),
\[
x'=A+rB\geq A,\qquad y'=rA+B\geq B.
\]
The chain rule gives
\[
\frac{d}{dt}\bigl(H(x)+H(y)\bigr)
=-f(x)(A+rB)-f(y)(rA+B)\leq-h.
\]
Because \(H\geq0\),
\[
I\leq H(x(0))+H(y(0)).
\]
In fact \(H(v)\leq v_-\), since \(H(0)=0\) and \(0\leq f\leq1\). Thus
\[
I\leq x(0)_-+y(0)_-\leq\|z_0\|_1=R-1.
\]
The stated \(I\leq2R\) is therefore conservative and correct. Together with \(I\leq U\), it yields the asserted stronger bound with exponent \(\min\{U,2R\}\).

It also implies the general (2) in this branch, since
\[
2R\leq\frac{3(R+U^{1/3})}{\delta}.
\]
This includes \(r=0\). No negative-correlation argument is being implicitly applied at this boundary.

## 5. Negative reflected correlation and cubic control cost

For \(r=-k<0\), with \(\delta=1-k\), define
\[
L=\int_0^T(A+B)\,dt,\qquad w=x+y.
\]
Then \(w'=\delta(A+B)\), so
\[
\delta L=w(T)-w(0),\qquad I\leq L.
\]
Since \(A+B\leq\alpha+\beta\), all these integrals are finite.

The map \(v\mapsto v_+^3\) is \(C^1\), including at zero. Using
\(x'=A-kB\) and \(y'=B-kA\),
\[
\begin{aligned}
\frac{d}{dt}(x_+^3+y_+^3)
&=3x_+^2(A-kB)+3y_+^2(B-kA)\\
&\leq3x_+^2A+3y_+^2B\\
&\leq3(\alpha+\beta).
\end{aligned}
\]
The final inequality uses \(x_+^2/(1+x^2)\leq1\) and its \(y\) counterpart. It remains valid when a coordinate is negative, zero, or moving in either direction. It requires no count of zero crossings.

At time zero,
\[
x_+(0)^3+y_+(0)^3
\leq(|x(0)|+|y(0)|)^3=(R-1)^3\leq R^3.
\]
Integration therefore gives precisely
\[
x_+(T)^3+y_+(T)^3\leq R^3+3U.
\]
For \(a,b\geq0\),
\[
4(a^3+b^3)-(a+b)^3
=3(a-b)^2(a+b)\geq0.
\]
Also \(w(T)\leq x_+(T)+y_+(T)\) and \(-w(0)\leq|w(0)|\leq R\). Thus
\[
\begin{aligned}
\delta L
&\leq x_+(T)+y_+(T)+R\\
&\leq 4^{1/3}(R^3+3U)^{1/3}+R\\
&\leq (1+4^{1/3})R+12^{1/3}U^{1/3}\\
&\leq3(R+U^{1/3}).
\end{aligned}
\]
The penultimate inequality follows from
\((R+(3U)^{1/3})^3\geq R^3+3U\). The last follows separately from
\(1+4^{1/3}<3\) and \(12^{1/3}<3\). Every constant in (5) is valid.

Combining \(I\leq U\), \(I\leq L\), and this estimate proves (2) for negative reflected correlation. The proof imposes no regularity or nondegeneracy of the ratio of the controls.

When \(U=0\), the control vanishes almost everywhere and the exact tangent is the identity. Formula (2) returns the valid, possibly loose upper bound \(\sqrt\kappa\). At \(T=0\) the same conclusion holds. These cases do not require interpreting a ratio or a singular power.

## 6. Exact example and its variational equation

Fix \(0<k<1\), set \(\rho=-k\) and \(d=1-k^2>0\), and use
\[
u_1(t)=20k,\qquad
u_2(t)=10\bigl(1+(2+dt)^2\bigr),\qquad z_0=(-1,2).
\]
The controls are smooth and strictly positive. Their restrictions to every finite interval are integrable, which is the theorem's requirement; integrability on the entire half-line is not required.

Along \(x=-1,\ y=2+dt\),
\[
\alpha=2k,\quad \beta=1+y^2,\quad A=k,\quad B=1.
\]
Therefore
\[
x'=A-kB=0,\qquad y'=B-kA=1-k^2=d,
\]
with the stated initial condition. Existence and uniqueness identify this as the exact solution. The control ratio
\[
\frac{u_2(t)}{u_1(t)}
=\frac{1+(2+dt)^2}{2k}
\]
strictly increases, so this is indeed a changing-ratio example.

The cost calculation is
\[
\begin{aligned}
U(T)
&=\int_0^T\left[2k+1+(2+dt)^2\right]\,dt\\
&=(2k+5)T+2dT^2+\frac{d^2}{3}T^3,
\end{aligned}
\]
which verifies (7), including its quadratic coefficient.

For the initial-state derivative, the prescribed functions \(u_i(t)\) remain fixed. In particular, the equality \(\beta(t)=1+y(t)^2\) holds along the displayed solution but is not a feedback law to differentiate. The state derivative of the first flux is
\[
\left.-\frac{2\alpha x}{(1+x^2)^2}\right|_{x=-1}=k,
\]
and that of the second is
\[
-\frac{2\beta y}{(1+y^2)^2}
=-\frac{2y}{1+y^2}=-b(t).
\]
Multiplication by \(C_{-k}\) gives exactly
\[
\binom{\xi'}{\eta'}=
\begin{pmatrix}k&kb\\-k^2&-b\end{pmatrix}
\binom{\xi}{\eta}.
\]
Since \(y\geq2\), \(b>0\) and in fact \(b\leq4/5<1\). The weaker bound \(b\leq1\) used in the candidate is valid.

## 7. Riccati interval, invariant tangent cone, and growth

For
\[
F_s(t,s)=k^2-(k+b(t))s+kb(t)s^2,
\]
the boundary values are
\[
F_s(t,0)=k^2>0,\qquad
F_s(t,k)=-kb(t)(1-k^2)<0.
\]
The scalar vector field is continuous in time and locally Lipschitz in \(s\). From \(s(0)=0\), its initial derivative is positive. A first exit through either endpoint would have an outward or zero derivative there, contradicting the strict inward derivative. Thus \(0\leq s(t)\leq k\).

On any finite time interval the vector field is bounded on a neighborhood of \([0,k]\). A bounded solution has a limit at a finite proposed maximal endpoint and can be extended by local existence. Therefore no finite maximal endpoint occurs, and the scalar solution exists for all \(t\geq0\). This justifies both the invariance and the global-existence sentence at lines 133–135.

Define
\[
\xi(t)=\exp\left(\int_0^t k[1-b(r)s(r)]\,dr\right),
\qquad \eta(t)=-s(t)\xi(t),
\]
where \(r\) is only the integration variable in this formula.

Then
\[
\xi'=k\xi+kb\eta,
\]
and substitution of the scalar equation gives
\[
\eta'=-s'\xi-s\xi'=(-k^2+bs)\xi
=-k^2\xi-b\eta.
\]
The initial tangent is \((1,0)\), as required.

Equivalently, this tangent remains in the cone
\[
\mathcal K=\{(\xi,\eta):\ \xi\geq0,\ -k\xi\leq\eta\leq0\}.
\]
The matrix equation independently verifies its boundary directions: on \(\eta=0\),
\(\eta'=-k^2\xi\leq0\); on \(\eta+k\xi=0\),
\[
(\eta+k\xi)'=-b(1-k^2)\eta
=kb(1-k^2)\xi\geq0.
\]
The vertex is an equilibrium, and the constructed solution has \(\xi>0\). These directions agree with the scalar invariant interval.

Since \(0\leq bs\leq k\),
\[
\xi(t)\geq e^{k(1-k)t}.
\]
The initial vector \((1,0)\) has Euclidean norm one, and the final tangent has norm at least \(\xi(t)\). Thus
\[
\|D_{z_0}z(T)\|_2\geq e^{k(1-k)T}.
\]
Equation (10) follows from a genuine solution of the nonautonomous variational equation; no instantaneous-eigenvector argument is used.

## 8. Sharpness and fixed-interval rescaling

For \(T\geq1\), set
\[
a_k=\frac{d^2}{3}>0,\qquad
B_k=2k+5+2d+\frac{d^2}{3}.
\]
The explicit polynomial cost satisfies
\[
a_kT^3\leq U(T)\leq B_kT^3.
\]
Writing \(c_k=k(1-k)>0\), the example therefore gives
\[
\|D_{z_0}z(T)\|_2
\geq e^{c_kT}
\geq \exp\left(\frac{c_k}{B_k^{1/3}}U(T)^{1/3}\right).
\]
This is a lower bound on the same cube-root exponent scale as the upper bound, with \(k\) and \(z_0=(-1,2)\), hence \(R=4\), fixed.

For any finite \(C>0\) and \(p\geq0\),
\[
\log\bigl(C(1+U(T))^p\bigr)
\leq \log C+p\log(1+B_kT^3)=O(\log T),
\]
which cannot dominate \(c_kT\). Negative finite \(p\) only decreases the proposed polynomial bound, so it cannot help.

Likewise, for \(0\leq\gamma<1/3\),
\[
C(1+U(T)^\gamma)=O(T^{3\gamma})=o(T).
\]
For \(\gamma<0\), this quantity remains bounded as \(T\to\infty\). Thus every claimed bound of the displayed form
\(\exp(C[1+U^\gamma])\), with finite \(C\) independent of the varying cost, fails when \(\gamma<1/3\). A fixed multiplicative prefactor would not change the conclusion. Constants may depend on the fixed \(k,z_0\); their dependence does not affect either contradiction.

To fix the horizon, use a parameter \(\ell\geq1\), distinguished here from the accumulated flux \(L\) in Section 2 of the candidate, and put
\[
u_\ell(t)=\ell u(\ell t),\qquad 0\leq t\leq1.
\]
For every initial state \(a\), not just the displayed \(z_0\), the function
\(z^u(\ell t;a)\) satisfies
\[
\frac{d}{dt}z^u(\ell t;a)
=C\operatorname{diag}(p(z^u_1),p(z^u_2))\,\ell u(\ell t).
\]
Uniqueness implies equality with the flow driven by \(u_\ell\). Differentiating this identity in \(a\) proves equality of the initial-state tangents at times \(1\) and \(\ell\).

The change of variables \(\tau=\ell t\) gives
\[
\frac1{10}\int_0^1\|u_\ell(t)\|_1\,dt
=\frac1{10}\int_0^\ell\|u(\tau)\|_1\,d\tau
=U(\ell).
\]
The rescaled controls remain smooth, positive, and independent of the perturbed initial state. Their amplitudes need not be uniformly bounded over \(\ell\), and the asserted control class does not require such a bound. Therefore the fixed-interval argument is exact and rules out rescuing a polynomial estimate by allowing constants to depend on the horizon.

## 9. Random initial states, factor 1/2, and exact scope

The Gaussian assertion at lines 102–109 is correct for every finite positive moment order and every Gaussian mean and covariance, including a singular covariance.

For \(\lambda\geq0\),
\[
e^{\lambda\|z_0\|_1}
=\max_{\sigma\in\{-1,1\}^2}e^{\lambda\sigma^Tz_0}
\leq\sum_{\sigma\in\{-1,1\}^2}e^{\lambda\sigma^Tz_0}.
\]
Each \(\sigma^Tz_0\) is a scalar Gaussian with finite exponential moments. For positive variance this follows by completing the square; for zero variance it is a deterministic finite number. Together with the stated \(R\)-dependent bound, this proves the claimed moment conclusion.

There is also a simpler stronger observation for deterministic prescribed \(u\): (4) gives the initial-state-independent bound
\[
\|D_{z_0}z(T)\|_2\leq\sqrt\kappa\,e^U.
\]
Consequently every positive moment is finite for any initial-state distribution in that case. The Gaussian calculation is valid but unnecessary for this particular deterministic-control conclusion.

For random prescribed controls, finite cost almost surely does not itself provide the exponential moments needed to average the displayed bounds. If a control is chosen as a function of \(z_0\), the estimate still describes differentiation of the flow with that realized schedule frozen. It does not bound the derivative of the composite map \(z_0\mapsto z^{u(z_0)}(T;z_0)\), which can contain derivatives of the control. True state feedback would likewise add terms to the variational equation. This distinction is consistent with the note's prescribed-forcing scope.

All calculations above are in the exact normalization of equation (1). If a separate equation were instead
\[
\dot z=\tfrac12 C\operatorname{diag}(p(z))q(t),
\]
then the exact identification would be \(u=q/2\). If
\[
V=\frac1{10}\int_0^T\|q(t)\|_1\,dt,
\]
the candidate's effective cost would be \(U=V/2\), and its estimate would read
\[
\|D_{z_0}z(T)\|_2
\leq\sqrt\kappa\,
\exp\left(\min\left\{\frac V2,\,
\frac{3[R+(V/2)^{1/3}]}{\delta}\right\}\right).
\]
To reproduce example (6) on the same time interval in that half-speed equation, prescribe \(q=2u\). Using the unchanged numerical schedule (6) in an equation with an extra \(1/2\) would not justify the displayed path \(x=-1,\ y=2+dt\). The candidate itself does not make that substitution.

Thus the undefined contextual “factor 1/2” cannot be checked against a training equation from this input, but the conditional conversion is harmless to the exponent scale when done explicitly. There is no factor-of-two defect within (1)–(10).

The example is a prescribed deterministic control schedule at a fixed initial state. It does not establish that training produces the schedule, that trained controls have fixed signs, that a random initialization encounters this growth with positive probability, or that a population quantity diverges. The candidate explicitly disclaims these conclusions. No canonical trained counterexample is necessary for the claim actually proved.

The statement about a constant-control polynomial estimate is supported in the following precise sense: a uniform polynomial-in-total-cost conclusion for arbitrary changing fixed-sign schedules is false, even for smooth schedules on \([0,1]\). This does not rule out applying local estimates on a mesh if the eventual result has different dependence on the control path. No separate constant-control lemma was supplied or needed for this conclusion. Sign-changing controls and actual trained-control continuation are outside this review's mathematical target.

## 10. Required repairs versus optional clarifications

**Required mathematical repairs: none.** The standalone fixed-sign theorem, cubic estimate, differentiability argument, exact example, invariant cone, exponent-scale sharpness, and fixed-interval counterexample are valid as stated under the conventional Euclidean operator-norm interpretation.

Optional clarifications:

1. State explicitly that the tangent norm is the Euclidean induced operator norm. The exact prefactor \(\sqrt\kappa\) was proved for that norm; different norms generally require conversion constants.
2. Replace the phrase “up to its specified factor 1/2” with an explicit conditional normalization such as \(u=q/2\), or omit the contextual comparison. Verifying an actual first-layer equation would require additional mathematical input that this audit was expressly forbidden to consult. This is a scope/normalization clarification, not a repair of (1).
3. In the random-control paragraph, specify that the derivative holds the realized control fixed. The current prescribed-control setup already has this meaning.
4. If more regularity detail is desired, add the integrable derivative bound and the Fréchet remainder argument from Section 2 of this review. The existing compressed argument has no missing hypothesis.
5. Use a different letter for the rescaling parameter than the accumulated flux \(L\). The current local reuse is harmless.

The stronger \(I\leq R-1\) in the nonnegative-correlation branch and the deterministic-control moment simplification are available improvements, not required changes. Neither optimal constants nor a trained-network construction are prerequisites for acceptance of the claims in this note.

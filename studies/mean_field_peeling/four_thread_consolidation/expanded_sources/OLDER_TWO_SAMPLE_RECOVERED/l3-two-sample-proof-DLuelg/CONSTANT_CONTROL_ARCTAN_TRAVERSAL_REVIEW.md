# Independent isolated adversarial audit

The stated global polynomial tangent bound is valid for the fixed two-dimensional control problem. I found no substantive mathematical error and no required repair to equation (1), including its numerical constants. The proof covers zero control, one vanishing component, either effective-correlation sign, every initial state, and both time directions with the stated absolute-time convention. The Gaussian moment estimate (24) is valid under the nonnegative-time convention of (1), and extends to signed time by the same absolute-time substitution.

This verdict concerns the supplied autonomous flow and its derivative with respect to its initial state. It does not identify that flow with an actual-network reverse-query evolution. The sole mathematical input supplies no network/query identification to audit; this limits the network-level conclusion without creating a defect in the lemma's stated scope.

## Provenance and isolation

- Sole mathematical input: `/tmp/l3-two-sample-proof-DLuelg/CONSTANT_CONTROL_ARCTAN_TRAVERSAL.md`.
- Input SHA-256: `8fca2c20127608fc84f04906ecf733b9d4a6e8b65a78c8af9416d52f8b36522c`.
- Input size: 12,401 bytes, 359 lines. The entire input was read. Line references below refer to this snapshot.
- Procedural skill personally read in full: `/etc/codex/skills/solve-math-rigorously/SKILL.md`.
- Procedural-skill SHA-256: `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`.
- Audit metadata timestamp: `2026-09-06T15:44:57Z`.
- No other project files, mathematical sources, history, or pre-existing reviews were read. No agents, experiments, simulations, symbolic-algebra checks, or external searches were used. The work below is a direct analytical reconstruction. Tool use was limited to the permitted reads, provenance/metadata checks, and writing this review with `apply_patch`.
- The candidate was not edited. A final source-hash verification is recorded at the end of this review.

## Required repairs

None for the stated constant-control tangent theorem or its Gaussian-integrability consequence. In particular, no extra positivity assumption on the smaller control component, no lower bound on its ratio to the larger component, and no initial-state restriction are needed.

## Optional presentation changes

1. At candidate lines 320–324, write “a finite time \(t\geq0\)” or use \(\log(1+|t|\|u\|_2)\) in the definition of \(\lambda\). Equation (24) is derived from the explicitly nonnegative-time equation (1), so the current proof is sound with that inherited convention. The local phrase “a finite time” is less precise after the earlier discussion of negative time. The displayed formula must not be read literally with arbitrary negative \(t\) and without the already-announced absolute-time substitution.
2. Define \(S=\tau(a+b)\) before the comparable/small-component split. It is introduced in the comparable branch at line 195 and reused in the small-component branch. Its intended meaning is unambiguous; moving the definition would make each branch easier to read independently.

Neither suggestion changes the substantive claim, proof mechanism, or constants.

## 1. Well-posedness, reflections, and the time factor

Write
\[
F_u(z)=C\operatorname{diag}(p(z_1),p(z_2))u.
\]
The assumptions give \(0<p(v)\leq1/10\) and
\[
|p'(v)|=\frac{2|v|}{10(1+v^2)^2}\leq\frac1{10},
\]
using \(2|v|\leq1+v^2\). Thus, for each fixed finite \(u\),
\[
\|F_u(z)\|_2\leq\frac{1+k}{10}\|u\|_2,
\qquad
\|DF_u(z)\|_{2\to2}\leq\frac{1+k}{10}\|u\|_\infty.
\]
These are global bounds. The elementary ODE fact being used is that a continuously differentiable vector field with a global Lipschitz bound has a unique solution from every initial state; bounded speed rules out finite-time escape, so the local solution continues for every real time. The integral equation is a contraction on sufficiently short time intervals, and iteration supplies this continuation. All hypotheses hold here.

The dependence on the initial state is continuously differentiable and its derivative \(J\) satisfies
\[
\dot J=DF_u(z(t))J,\qquad J(0)=I_2.
\]
For completeness, initial-state difference quotients satisfy this integral equation with the coefficient matrix replaced by the average of \(DF_u\) along the segment between the two solutions. The Lipschitz bound controls the difference of those solutions on every compact time interval. Continuity of \(DF_u\) on the resulting compact set makes the averaged coefficients converge uniformly to \(DF_u(z(t))\); the corresponding linear integral equations then converge by the integrating-factor inequality. This justifies the variational equation, rather than merely formally differentiating a trajectory.

Let \(Q=\operatorname{diag}(\sigma_1,\sigma_2)\), with \(Qu=(a,b)^T\), \(a,b\geq0\). For a zero component either sign is allowed. Define
\[
X(\tau)=(x(\tau),y(\tau))^T=Qz(10\tau;z_0,u).
\]
Evenness of \(p\) gives
\[
X'
=10QF_u(z)
=QCQ\begin{pmatrix}a/(1+x^2)\\b/(1+y^2)\end{pmatrix}
=C_r\begin{pmatrix}A\\B\end{pmatrix},
\qquad r=\rho\sigma_1\sigma_2.
\]
Consequently the normalization is \(\tau=t/10\), not \(10t\). The off-diagonal entry is the effective correlation \(r\), whose sign need not equal the sign of \(\rho\), while \(|r|=k\).

For fixed \(u\), the reflection is independent of \(z_0\), including when a component of \(u\) vanishes. If \(J_X\) denotes the reflected initial-state derivative, then
\[
D_{z_0}z(t;z_0,u)=QJ_X(t/10)Q.
\]
Orthogonal conjugation preserves the Euclidean operator norm. Exchanging the two coordinates also preserves that norm, \(R\), and the matrix form of \(C_r\). There is no derivative of a sign choice to account for: the derivative in question is with respect to \(z_0\), not \(u\).

## 2. The tangent energy and growth integral

The potential
\[
H(v)=\log(1+v_-^2)
\]
is continuously differentiable at zero because both one-sided derivatives equal zero. Its negative derivative is
\[
f(v)=\begin{cases}2|v|/(1+v^2),&v<0,\\0,&v\geq0.\end{cases}
\]
In particular \(0\leq f\leq1\); the chain rule used in the proof needs only this \(C^1\) regularity of \(H\), not a second derivative at zero.

For the reflected tangent vector,
\[
\eta'=C_r D\eta,\qquad
D=\operatorname{diag}\left(-\frac{2ax}{(1+x^2)^2},-\frac{2by}{(1+y^2)^2}\right).
\]
Since \(|r|<1\), \(C_r\) is positive definite. With \(E=\eta^TC_r^{-1}\eta\), symmetry gives the exact cancellation
\[
E'=\eta^T(DC_rC_r^{-1}+C_r^{-1}C_rD)\eta
=2\eta^TD\eta.
\]
The positive parts of the two diagonal entries of \(D\) are precisely \(Af(x)\) and \(Bf(y)\). Furthermore,
\[
E=\eta_1^2+\frac{(\eta_2-r\eta_1)^2}{1-r^2}
=\eta_2^2+\frac{(\eta_1-r\eta_2)^2}{1-r^2},
\]
so \(\eta_i^2\leq E\) with constant exactly one. Therefore
\[
E'\leq2Af(x)\eta_1^2+2Bf(y)\eta_2^2
\leq2hE,
\qquad h=Af(x)+Bf(y).
\]
Multiplication by \(e^{-2I(\tau)}\), where \(I(\tau)=\int_0^\tau h(s)\,ds\), shows
\[
E(\tau)\leq e^{2I(\tau)}E(0).
\]
The eigenvalues of \(C_r\) lie between \(1-k\) and \(1+k\), hence
\[
\|\eta(\tau)\|_2^2
\leq(1+k)E(\tau)
\leq\frac{1+k}{1-k}e^{2I(\tau)}\|\eta(0)\|_2^2.
\]
Taking the supremum over unit initial tangent vectors proves (4), with prefactor \(\sqrt\kappa\). No additional condition-number factor is missing from the energy derivative.

## 3. Nonnegative effective correlation

For \(r\geq0\), \(x'=A+rB\geq A\) and \(y'=B+rA\geq B\). Since \(f\geq0\),
\[
\frac{d}{d\tau}\bigl(H(x)+H(y)\bigr)
=-f(x)(A+rB)-f(y)(B+rA)\leq-h.
\]
Integrating and discarding the nonnegative terminal potential gives
\[
I(\tau)\leq H(x_0)+H(y_0)
\leq2(|x_0|+|y_0|)\leq2R.
\]
For the displayed logarithmic bound, if \(v\geq0\), the function \(2v-\log(1+v^2)\) vanishes at zero and has nonnegative derivative \(2-2v/(1+v^2)\). This verifies the inequality used. The argument includes \(k=0\), either zero component, and \(u=0\), without any threshold involving \(1/k\).

## 4. Negative effective correlation: path geometry

It remains to take \(r=-k\), \(0<k<1\). If \(u=0\), the flow and its initial-state derivative are the identity. Otherwise, after a coordinate exchange, \(0\leq a\leq b\) and \(b>0\). Hence \(B>0\) at every finite state, so every use of \(A/B\) below is legitimate even if \(A=0\).

The equations are
\[
x'=A-kB,\qquad y'=B-kA.
\]
For \(L(\tau)=\int_0^\tau(A+B)\,ds\) and \(w=x+y\),
\[
|x'|,|y'|\leq A+B,
\quad |x-x_0|,|y-y_0|\leq L,
\quad |x|,|y|\leq R+L,
\]
and
\[
w'=\delta(A+B),\qquad w=w_0+\delta L,
\qquad L\leq\tau(a+b)=S.
\]
Here \(L'>0\), so both the reparameterization by \(L\) and strict increase of \(w\) are valid. The portion with \(w<0\), if nonempty, is an initial interval. Since \(h\leq A+B=L'\), its contribution is at most
\[
\frac{(-w_0)_+}{\delta}\leq\frac{R}{\delta}.
\]
If \(w_0\geq0\), the nonnegative portion starts at time zero. Otherwise, if it has started by the observation time, its starting path length is \(L_*=-w_0/\delta\leq R/\delta\). In either case the starting coordinate magnitudes are bounded by
\[
R+\frac R\delta\leq\frac{2R}{\delta}.
\]
At \(w\geq0\) both coordinates cannot be negative. Thus at that starting time
\[
H(x)+H(y)\leq\log\left(1+(2R/\delta)^2\right).
\]
This is a bound at the beginning of the nonnegative portion, not an assertion that all later coordinate magnitudes remain bounded by the same quantity.

Set
\[
L_0=\frac{8R}{k},\qquad M=R+L_0,
\qquad \varepsilon=\frac{k}{4(1+M^2)}.
\]
These are used only when \(k>0\), and \(0<\varepsilon<1\). The two cases \(a/b\geq\varepsilon\) and \(a/b\leq\varepsilon\) cover all ratios, with harmless overlap at equality. Their thresholds depend on the initial state but are never differentiated; this does not affect the initial-state tangent argument or its later pointwise integration.

## 5. Comparable controls: reconstruction of the telescoping estimate

Assume \(\varepsilon\leq a/b\leq1\). Then \(a,b>0\), and \(b/a\geq1\geq\varepsilon\). With \(\mathcal H=H(x)+H(y)\), direct substitution gives
\[
\mathcal H'=-f(x)(A-kB)-f(y)(B-kA),
\]
and therefore
\[
h+2\mathcal H'=f(x)(2kB-A)+f(y)(2kA-B).
\]
Consider any time with \(w\geq0\).

If \(x<0\), then \(y=w+|x|\geq w\geq0\), and \(f(y)=0\). When \(2kB-A\leq0\), the entire right side is nonpositive. In the remaining subcase \(A<2kB\), multiplication by positive denominators gives
\[
1+x^2>\frac{a}{2kb}(1+y^2)
\geq\frac{\varepsilon}{2k}(1+y^2)
\geq\frac{\varepsilon}{2k}(1+w^2).
\]
It follows that
\[
f(x)=\frac{2|x|}{1+x^2}
\leq\frac2{\sqrt{1+x^2}}
\leq\frac{2\sqrt{2k/\varepsilon}}{\sqrt{1+w^2}},
\]
and
\[
f(x)(2kB-A)\leq2kBf(x)
\leq\frac{4k\sqrt{2k/\varepsilon}\,B}{\sqrt{1+w^2}}.
\]

If \(y<0\), then \(x=w+|y|\geq w\geq0\), and \(f(x)=0\). A positive remaining term requires \(B<2kA\), which gives
\[
1+y^2>\frac{b}{2ka}(1+x^2)
\geq\frac{\varepsilon}{2k}(1+w^2).
\]
The same elementary estimate for \(f(y)\) now yields
\[
f(y)(2kA-B)
\leq\frac{4k\sqrt{2k/\varepsilon}\,A}{\sqrt{1+w^2}}.
\]
If the remaining term was nonpositive no estimate was needed. If both coordinates are nonnegative, both terms vanish. Coordinates equal to zero are included because \(f(0)=0\).

These exhaustive cases establish
\[
h\leq-2\mathcal H'
+K\frac{A+B}{\sqrt{1+w^2}},
\qquad K=4k\sqrt{2k/\varepsilon}.
\]
There is no count of turning points or assumption of eventual monotonicity in this argument.

Let the nonnegative portion, when present, start at \(\tau_*\). With \(d=w(\tau)-w(\tau_*)\),
\[
0\leq d=\delta(L(\tau)-L(\tau_*))\leq\delta S\leq S.
\]
Changing variables using \(w'=\delta(A+B)>0\),
\[
\int_{\tau_*}^{\tau}\frac{A+B}{\sqrt{1+w^2}}\,ds
=\frac1\delta\int_{w(\tau_*)}^{w(\tau_*)+d}
\frac{dv}{\sqrt{1+v^2}}
\leq\frac1\delta\int_0^d\frac{dv}{\sqrt{1+v^2}}.
\]
The last inequality follows from the decrease of the integrand on \([0,\infty)\) and \(w(\tau_*)\geq0\). Its antiderivative is \(\operatorname{arsinh}v=\log(v+\sqrt{1+v^2})\), verified by differentiation. Since \(\sqrt{1+d^2}\leq1+d\), the last expression is bounded by \(\delta^{-1}\log(1+2S)\).

Integrating the potential inequality, discarding the nonnegative terminal potential, and including the initial \(w<0\) portion gives
\[
\begin{aligned}
I(\tau)
&\leq\frac R\delta
+2\log\left(1+(2R/\delta)^2\right)
+\frac K\delta\log(1+2S)\\
&\leq\frac{9R}{\delta}+\frac K\delta\log(1+2S).
\end{aligned}
\]
The coefficient \(9\) is \(1+8\): the logarithmic term is at most \(2\cdot2\cdot(2R/\delta)=8R/\delta\). If the trajectory has not reached \(w=0\), the first term alone already bounds \(I\).

Finally,
\[
\begin{aligned}
K&=8\sqrt2\,k\sqrt{1+M^2}\\
&\leq8\sqrt2\,k(1+M)
=8\sqrt2\,[k+(k+8)R]\\
&\leq8\sqrt2\,(2k+8)R
\leq80\sqrt2\,R<120R.
\end{aligned}
\]
Here \(R\geq1\) permits \(k\leq kR\), and \(k<1\). The cancellation of the auxiliary \(1/k\) scale is valid. No direction-dependent or ratio-dependent factor remains in the final estimate.

## 6. Small component: initial segment and entry

Assume \(0\leq a/b\leq\varepsilon\). This branch estimates the entire trajectory from time zero; it does not assume \(w\geq0\) or require entry into that half-plane first. Write \(\theta=A/B\). While \(L\leq L_0\),
\[
\theta=\frac ab\frac{1+y^2}{1+x^2}
\leq\varepsilon(1+M^2)=\frac k4.
\]
Thus
\[
y'=B(1-k\theta)\geq(1-k^2/4)B\geq\frac34B>0.
\]
Over any initial segment ending at or before \(L=L_0\),
\[
\int Af(x)\,ds\leq\int A\,ds
\leq\frac k4\int B\,ds
\leq\frac k4L_0=2R,
\]
while
\[
\int Bf(y)\,ds
\leq\frac43\int f(y)y'\,ds
=\frac43\bigl(H(y_0)-H(y_{\rm end})\bigr)
\leq\frac43\log(1+y_0^2).
\]
This remains true when \(y\) crosses zero: \(H\) is \(C^1\), and \(f\) then becomes zero. No negative-part sign is reversed in this estimate.

If the observation precedes \(L=L_0\), this already bounds \(I\). Otherwise define \(\tau_e\) by \(L(\tau_e)=L_0\). This is a guaranteed interior time in the eventual invariant region, not necessarily the first time that region is entered. Because \(L'>0\), this time, if reached, is unique.

For \(g=x+(k/2)y\), division by \(L'=B(1+\theta)>0\) gives
\[
\frac{dy}{dL}=\frac{1-k\theta}{1+\theta}
\geq\frac{3/4}{5/4}=\frac35.
\]
Also
\[
\frac{dg}{dL}
=\frac{(1-k^2/2)\theta-k/2}{1+\theta}.
\]
The numerator is at most \(\theta-k/2\leq-k/4\), while \(1+\theta\leq5/4\). Because the numerator bound is negative, the correct inequality direction is
\[
\frac{(1-k^2/2)\theta-k/2}{1+\theta}
\leq\frac{-k/4}{1+\theta}
\leq\frac{-k/4}{5/4}=-\frac k5.
\]
This checks the potentially delicate signed division at candidate lines 255–257.

Since \(y_0\geq-R\) and
\[
g_0=x_0+(k/2)y_0
\leq|x_0|+(k/2)|y_0|\leq R,
\]
integration to \(L_0=8R/k\) yields
\[
y(\tau_e)\geq-R+\frac{24R}{5k}>0,
\qquad
g(\tau_e)\leq R-\frac{8R}{5}=-\frac35R<0.
\]
Hence \(X(\tau_e)\) lies strictly inside
\[
\mathcal K=\{y\geq0,\ g\leq0\}.
\]
There is no assumed finite hitting time hidden in this finite-observation argument. One can additionally verify finite attainment of every fixed \(L_0\): if \(L\leq L_0\), then
\[
L'=A+B\geq\frac{a+b}{1+(R+L_0)^2}>0.
\]
Remaining below \(L_0\) indefinitely would contradict this uniform lower bound. This extra observation is not necessary for the candidate's case split.

## 7. Invariance and the logarithmic tail

At every point of \(\mathcal K\), \(x\leq-(k/2)y\leq0\), so \(x^2\geq(k^2/4)y^2\). Therefore
\[
\begin{aligned}
\theta
&\leq\varepsilon\frac{1+y^2}{1+(k^2/4)y^2}
\leq\frac{4\varepsilon}{k^2}\\
&=\frac1{k(1+M^2)}
\leq\frac k{64}<\frac k4.
\end{aligned}
\]
The second inequality uses
\(1+(k^2/4)y^2\geq(k^2/4)(1+y^2)\), since \(k^2/4<1\). The penultimate inequality follows from \(M\geq8R/k\geq8/k\). It does not assume that the earlier condition \(L\leq L_0\) remains valid. This is the independent geometric estimate needed to avoid a circular invariance argument.

Throughout \(\mathcal K\),
\[
y'=B(1-k\theta)>0,
\]
and
\[
g'=B\bigl((1-k^2/2)\theta-k/2\bigr)
\leq B(\theta-k/2)\leq-\frac k4B<0.
\]
Both boundary directions are therefore correct. Starting in the strict interior, a first contact with \(y=0\) from \(y>0\) would require \(y'\leq0\), contradicting the positive derivative at that contact. A first contact with \(g=0\) from \(g<0\) would require \(g'\geq0\), contradicting the negative derivative. A boundary initial state moves into the interior because the same strict derivative inequalities hold there, including at the corner. Global existence excludes an alternative finite-time termination. This proves forward invariance.

For \(\tau\geq\tau_e\), \(y>0\) and \(x<0\), and \(A\leq(k/4)B\) implies
\[
-x'=kB-A\geq3A.
\]
There is no division by \(A\). Thus this inequality remains valid when \(a=0\). The only growth contribution is \(h=Af(x)\), and
\[
\begin{aligned}
\int_{\tau_e}^{\tau}h\,ds
&\leq\frac13\int_{\tau_e}^{\tau}f(x)(-x')\,ds\\
&=\frac13\bigl(H(x(\tau))-H(x(\tau_e))\bigr)\\
&=\frac13\log\frac{1+x(\tau)^2}{1+x(\tau_e)^2}
\leq\frac13\log\bigl(1+(R+S)^2\bigr).
\end{aligned}
\]
The sign is correct: \(x\) is negative and decreasing, so \(H(x)\) increases and \(H'(x)x'=f(x)(-x')\geq0\). The last inequality uses the denominator lower bound one and \(|x(\tau)|\leq R+L(\tau)\leq R+S\).

Combining the initial and tail estimates, or adding the nonnegative tail upper bound when the observation is before \(\tau_e\), gives
\[
I(\tau)\leq2R+\frac43\log(1+y_0^2)
+\frac13\log\bigl(1+(R+S)^2\bigr).
\]
Now
\[
\log(1+y_0^2)\leq2\log(1+R),
\]
and
\[
1+(R+S)^2\leq(1+R+S)^2\leq(1+R)^2(1+S)^2.
\]
Consequently
\[
\begin{aligned}
I(\tau)
&\leq2R+\frac{10}{3}\log(1+R)+\frac23\log(1+S)\\
&\leq\frac{16}{3}R+\frac23\log(1+S)
\leq6R+\frac23\log(1+S).
\end{aligned}
\]
This verifies all constants in (22), including for observation times before entry.

## 8. Explicit vanishing-component check and exhaustive cases

The preceding estimates already include \(a=0\). There is also a direct exact check, independent of the invariant-region construction. When \(a=0<b\), for either effective correlation \(r\),
\[
y'=\frac b{1+y^2},\qquad x'=r y'.
\]
Let \(P(v)=v+v^3/3\), so \(P'(v)=1+v^2>0\). Then
\[
P(y(\tau))=P(y_0)+b\tau,
\qquad x(\tau)=x_0+r(y(\tau)-y_0).
\]
These identities describe the global solution because \(P\) is strictly increasing onto \(\mathbb R\). Its initial-state derivative is
\[
d=\frac{1+y_0^2}{1+y(\tau)^2},
\qquad
J_X(\tau)=\begin{pmatrix}1&r(d-1)\\0&d\end{pmatrix}.
\]
For forward time, \(y\) increases and
\[
I(\tau)=\int_0^\tau Bf(y)\,ds
=H(y_0)-H(y(\tau))\leq H(y_0).
\]
Thus a vanishing component has no singular sensitivity limit and even admits a time-independent forward bound through (4). For \(r=-k\), the off-diagonal tangent entry is \(k(1-d)\), which also checks the sign of the coupling. If the other component vanishes, the coordinate exchange reduces it to this case. If both vanish, \(J_X=I_2\).

The complete case partition is therefore:

| Case | Verified upper bound for \(I(\tau)\) |
| --- | --- |
| \(u=0\) | \(0\) |
| \(r\geq0\), including \(k=0\) | \(2R\) |
| \(r=-k<0\), \(\varepsilon\leq a/b\leq1\) | \(9R/\delta+(120R/\delta)\log(1+2S)\) |
| \(r=-k<0\), \(0\leq a/b\leq\varepsilon\) | \(6R+(2/3)\log(1+S)\) |

Initial states on \(x=0\), \(y=0\), or \(w=0\) cause no exceptional term because the potential is \(C^1\) and \(f(0)=0\). The threshold equality is covered by both branches. Arbitrarily small \(k>0\) is covered with no final \(1/k\) loss; \(k=0\) is handled separately before introducing that threshold. As \(k\uparrow1\), the permitted constants diverge through \(\delta\) and \(\kappa\); the excluded endpoints \(|\rho|=1\) are not being assumed.

## 9. Raw time, uniformity, and reverse time

For \(t\geq0\), let \(T=t\|u\|_2\). The normalization gives
\[
2S=\frac t5(a+b)
\leq\frac{\sqrt2}{5}t\sqrt{a^2+b^2}
=\frac{\sqrt2}{5}T\leq T.
\]
In the comparable branch this replaces \(\log(1+2S)\) by \(\log(1+T)\). In the small branch it also gives \(\log(1+S)\leq\log(1+T)\). Since \(R\geq1\), \(0<\delta\leq1\), and the logarithms are nonnegative, every row of the table is bounded by
\[
I(\tau)\leq\frac{10R}{\delta}
+\frac{120R}{\delta}\log(1+T).
\]
Together with the energy estimate and the orthogonal coordinate changes, this proves precisely
\[
\|D_{z_0}z(t;z_0,u)\|_{2\to2}
\leq\sqrt\kappa\,
\exp\left(\frac{10R}{\delta}\right)
(1+t\|u\|_2)^{120R/\delta}.
\]
Its constants depend only on \(R\) and \(|\rho|\); no dependence on the signs, ratio, or direction of \(u\) remains. At \(t=0\), the derivative is the identity and the displayed right side is at least one. The estimate is pointwise in \(z_0\), and uniform on any initial-state set where \(R\) has a finite upper bound.

For signed time, linearity in the fixed control gives \(F_{-u}=-F_u\). If \(s\geq0\), then the curve \(s\mapsto z(-s;z_0,u)\) solves the initial-value problem with control \(-u\). Uniqueness gives
\[
z(-s;z_0,u)=z(s;z_0,-u),
\]
and differentiation in \(z_0\) gives the same identity for initial-state derivatives. Since \(\|-u\|_2=\|u\|_2\) and \(R\) is unchanged, the theorem holds for every real \(t\) with \(|t|\). This is a direct control-reversal argument; it does not infer a bound on an inverse matrix merely from a forward matrix bound.

## 10. Initial-state dependence and Gaussian moments

For uniform signed-time notation in this reconstruction, set
\[
T=|t|\|u\|_2,\qquad
\lambda=\frac q\delta\bigl(10+120\log(1+T)\bigr)>0,
\]
where \(q>0\), \(u\) is deterministic and constant, and \(t\) is finite. For \(t\geq0\) this is exactly the candidate's definition. Raising the pointwise bound to the power \(q\) gives
\[
\mathbb E\|D_{Z_0}z(t;Z_0,u)\|_{2\to2}^{q}
\leq\kappa^{q/2}e^\lambda
\mathbb E e^{\lambda\|Z_0\|_1}.
\]
For \(\lambda\geq0\),
\[
\|v\|_1=\max_{s\in\{-1,1\}^2}s^Tv,
\qquad
e^{\lambda\|v\|_1}
=\max_s e^{\lambda s^Tv}
\leq\sum_s e^{\lambda s^Tv}.
\]
The four terms, rather than an independence assumption on the coordinates of \(Z_0\), produce the factor four.

For a Gaussian law with finite mean \(m\) and positive-semidefinite covariance \(\Sigma\), including a singular covariance, choose a matrix \(B\) with \(BB^T=\Sigma\) and represent its law by \(Z_0=m+BG\), with \(G\) having two independent standard normal coordinates. Such a \(B\) is obtained by orthogonally diagonalizing the symmetric positive-semidefinite matrix and taking square roots of its nonnegative eigenvalues; zero eigenvalues require no inverse.

For a standard normal scalar and any real \(c\), completing the square gives
\[
\frac1{\sqrt{2\pi}}\int_{\mathbb R}e^{cg-g^2/2}\,dg
=e^{c^2/2}\frac1{\sqrt{2\pi}}
\int_{\mathbb R}e^{-(g-c)^2/2}\,dg
=e^{c^2/2}.
\]
Applying this identity independently to the coordinates of \(G\) yields
\[
\mathbb E e^{\lambda s^TZ_0}
=\exp\left(\lambda s^Tm+\frac{\lambda^2}{2}\|B^Ts\|_2^2\right)
=\exp\left(\lambda s^Tm+\frac{\lambda^2}{2}s^T\Sigma s\right).
\]
This derivation is valid even when \(\Sigma=0\). The estimates
\[
s^Tm\leq\|m\|_1,
\qquad
s^T\Sigma s\leq\|\Sigma\|_{2\to2}\|s\|_2^2
=2\|\Sigma\|_{2\to2}
\]
give
\[
\mathbb E\|D_{Z_0}z(t;Z_0,u)\|_{2\to2}^{q}
\leq4\kappa^{q/2}
\exp\left(\lambda(1+\|m\|_1)
+\lambda^2\|\Sigma\|_{2\to2}\right)<\infty.
\]
Thus all constants in (24) check: the prefactor is \(4\kappa^{q/2}\), the linear exponent includes the additive one in \(R\), and the quadratic coefficient is \(\|\Sigma\|_{2\to2}\), because the factor two from \(\|s\|_2^2\) cancels the Gaussian MGF's factor one-half.

No limit exchange or unproved integrable domination is needed: the pointwise nonnegative bound is followed by a finite sum of explicitly evaluated Gaussian integrals. The initial-state derivative is measurable because the flow is continuously differentiable. Every finite \(q>0\) and finite time are permitted, for every Gaussian mean and covariance. The control is fixed and deterministic as stated; no moment claim about an additional random control is being used.

For fixed \(\rho,q,m,\Sigma\), \(\lambda\) is affine in \(\log(1+T)\), so this calculation supplies an upper bound of the form
\[
\exp\bigl(O((1+\log(1+T))^2)\bigr).
\]
This is an upper bound, not an asymptotic equality or a lower bound precluding a polynomial improvement. In particular, the candidate correctly distinguishes pointwise polynomial control from what its Gaussian-averaged estimate proves.

## 11. Consequence for the stated root objective

The audited result rigorously supplies a global initial-state tangent estimate, including reverse time, for the particular constant-control two-input arctangent characteristic equation written in the candidate. That is a valid supporting lemma for a reverse-query construction if this equation is the independently derived characteristic system of the actual network under consideration.

The candidate itself does not specify an actual network, its query coordinates, or the identity relating a reverse-query evolution to this ODE. Those identifications cannot be verified from the allowed input. I therefore accept the constant-control lemma and its integrability consequence without claiming that the broader actual-network derivation has been completed. A time-dependent-control theorem or a training theorem is not required to repair any claim made here.

## Final provenance verification

After the mathematical review was written, the source and procedural skill were rehashed at `2026-09-06T15:48:37Z`. Both digests matched their recorded input hashes exactly:

- Candidate: `8fca2c20127608fc84f04906ecf733b9d4a6e8b65a78c8af9416d52f8b36522c`.
- Procedural skill: `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`.

The reviewed candidate bytes are unchanged. The only file created or edited by this audit is `/tmp/l3-two-sample-proof-DLuelg/CONSTANT_CONTROL_ARCTAN_TRAVERSAL_REVIEW.md`.

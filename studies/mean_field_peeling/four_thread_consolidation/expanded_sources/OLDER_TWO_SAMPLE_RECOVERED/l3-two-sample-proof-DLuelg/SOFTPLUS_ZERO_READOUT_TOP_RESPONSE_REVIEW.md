# Candidate-only adversarial audit: zero-readout top response

Reviewed candidate: `/tmp/l3-two-sample-proof-DLuelg/SOFTPLUS_ZERO_READOUT_TOP_RESPONSE.md`

Verified SHA256: `b3db63b762556636bb5ec5607acbe04729f23944f055e35e4339c2370ae42566`

Audit date: 2026-09-06.

## Verdict and audit boundary

**CONDITIONAL LEMMA PASS. No required mathematical correction was found in the new scalar argument, inequality (4), or the complete homogeneous two-by-two propagator bound (14). This is NOT a whole-goal PASS, a full network response estimate, or a canonical global-flow theorem.**

The only mathematical input to this audit was the candidate identified above; I also read the procedural `solve-math-rigorously` skill. I did not read its cited source, any other mathematical project file, any previous review, or any project history. The newly written output report was checked for formatting. No experiments or agents were used. The candidate was not edited.

As instructed, I accept conditionally the explicitly imported existing global, uncut, symmetric reference family and its primal, action, coercivity, and common-space/local premise. I do not certify that premise, the cited source's contents, or the existence of such a family. The calculations below independently audit what the candidate adds under that premise. Verification of the external training construction is outside this isolated audit; the normalization of the displayed top equations is checked explicitly below.

The main adversarial questions have the following answers:

| Question | Finding |
| --- | --- |
| Does the switching inequality have the right sign? | Yes. The switching contribution to the active $H$-potential is nonpositive; the contribution to the active gap is nonnegative. Both signs follow from the exact readout equation. |
| Can arbitrarily many or accumulating switches invalidate the argument? | No. Every differentiation and integration is done with smooth functions of $w$; no derivative or total variation of $\operatorname{sign}w$ is used. |
| Does the occupation estimate include $w=0$ and the entire level set $X=L$? | Yes. Zero-readout contributions vanish, and the smooth truncation has derivative exactly one at the level. The order of limits is valid. |
| May $L=\log(1+B_t)$ be chosen separately for each path and endpoint? | Yes. The occupation inequality holds for every fixed nonnegative $L$ on that path. The chosen value is held constant during integration. |
| Are the factors in (4), (12), and (13) consistent? | Yes. In particular, $G_{aa}=2\lambda$, the top Jacobian is $(w/2)GD$, and energy growth $2I_t$ becomes norm growth $I_t$. |
| Does the result control the whole homogeneous two-by-two block? | Yes, including its off-diagonal interactions and the changing Gram metric. |
| Does it supply ordinary moments or close the full response theorem? | No. Those conclusions are not established, and the candidate correctly leaves them open. |

## 1. Actual top equations and their normalization

Write $h_a=H_a^{(2)}$ as vectors in the second-population Hilbert space, so that $z_a=W^{(3)}h_a$ and $G_{ab}=\langle h_a,h_b\rangle$. At the two-sample feature-time normalization used in the candidate, the label-weighted top potential is

\[
\mathcal F=\frac12\,\mathbb E_3\bigl[w(\phi(z_1)-\phi(z_2))\bigr].
\]

Its readout gradient is exactly $w'=(\phi(z_1)-\phi(z_2))/2$. Its third-matrix gradient, evaluated at a fixed third-population coordinate, is the row vector

\[
(W^{(3)})'=\frac w2\bigl(\phi'(z_1)h_1-\phi'(z_2)h_2\bigr).
\]

Consequently the product rule gives

\[
z_a'=\frac w2\bigl[G_{a1}\phi'(z_1)-G_{a2}\phi'(z_2)\bigr]
       +W^{(3)}h_a'.
\]

Substitution of $G=2\lambda\begin{psmallmatrix}1&k\\k&1\end{psmallmatrix}$ produces exactly (1):

\[
z_1'=\lambda w(\phi'_1-k\phi'_2)+b_1,\qquad
z_2'=\lambda w(k\phi'_1-\phi'_2)+b_2.
\]

Thus the sample factor $1/2$ cancels the factor $2$ in $G$; it must not be retained a second time in these two scalar equations. Conversely, it must remain in the matrix expression for the top Jacobian in (12). There is no missing derivative of $\lambda$ or $k$ in the first derivative of $z_a=W^{(3)}h_a$; their time dependence is the current value of the Gram, and lower feature motion is already in $b_a$.

This establishes factor consistency with the feature-time gradient normalization stated by the candidate. It does not independently establish the outside construction or time change from an unread training source.

The asserted Gram bounds are also algebraically consistent. With $u=\mathbb E_2U^2$, $v=\mathbb E_2V^2$, and $\mathbb E_2UV=0$,

\[
G=\begin{pmatrix}u+v&u-v\\u-v&u+v\end{pmatrix},\qquad
\lambda=\frac{u+v}{2},\qquad k=\frac{u-v}{u+v}.
\]

The Gram eigenvalues are $2u$ and $2v$, not $u$ and $v$. Moreover,

\[
\|w'\|_2
=\left\|\frac{\phi(z_1)-\phi(z_2)}2\right\|_2
\le\frac\epsilon2\|z_1-z_2\|_2
\le\epsilon\|W^{(3)}\|_{\rm op}\sqrt v.
\]

The conditional readout coercivity and operator bound therefore give the claimed positive lower bound on $v$. Since $h_a\ge1$, $u-v=\mathbb E_2[h_1h_2]\ge1$, hence $k\ge0$. Upper bounds on $u+v$, together with the lower bound on $v$, give $k\le k_{\max}<1$. Uniformity here has exactly the reference-index scope supplied by the accepted coercivity premise; the candidate expressly mentions sufficiently large reference indices.

The claimed estimates (3) require only the usual norm consequences of the accepted raw-action/primal premise. In detail, the raw derivative norm controls the individual matrix derivative operator norms, feature norms and primal operator norms are bounded, and $|\phi'|\le\epsilon$. Thus

\[
\|(Z^{(2)}_a)'\|_2
\le\|(W^{(2)})'\|_{\rm op}\|H^{(1)}_a\|_2
 +\|W^{(2)}\|_{\rm op}\epsilon\|(Z^{(1)}_a)'\|_2
\le Ca,
\]

\[
\|(h_a)'\|_2\le Ca,\qquad
\|b_a\|_2\le\|W^{(3)}\|_{\rm op}\|(h_a)'\|_2\le Ca.
\]

Differentiating $G_{ab}=\langle h_a,h_b\rangle$ and applying Cauchy--Schwarz gives $\|G'\|_{\rm op}\le Ca$. Likewise $\|z_a\|_2\le\|W^{(3)}\|_{\rm op}\|h_a\|_2$. These calculations do not require a pointwise-in-neuron bound uniform in the reference index or any independence assumption. The needed raw-norm domination is part of the norm interpretation of the accepted premise; it is not a new response bound.

## 2. The two switching signs are correct

Set $\Delta=z_1-z_2$, $f_a=f(z_a)$, and $g_a=1-f_a$. Strict monotonicity gives

\[
w'\Delta=\frac12[\phi(z_1)-\phi(z_2)](z_1-z_2)\ge0,
\]

whereas monotonicity of $H$ in the opposite direction gives

\[
w'[H(z_1)-H(z_2)]
=\frac12[\phi(z_1)-\phi(z_2)][H(z_1)-H(z_2)]\le0.
\]

Multiplication by $S_\delta'(w)\ge0$ or $\alpha_\delta'(w)\ge0$ proves the claimed signs, including at $w=0$. The argument does not use $w[\phi(z_1)-\phi(z_2)]\ge0$; replacing $w'$ by $w$ would be an unjustified and materially different assertion.

Subtracting the two top equations yields

\[
\Delta'=\epsilon\lambda w(1-k)(f_1+f_2)+(b_1-b_2).
\]

Therefore the exact smoothed-gap identity is

\[
X_\delta'
=S_\delta'(w)w'\Delta
 +(1-k)d_\delta(f_1+f_2)+S_\delta(w)(b_1-b_2),
\quad d_\delta=\epsilon\lambda wS_\delta(w).
\]

Dropping the nonnegative first term and using $|S_\delta|\le1$ proves (7) with the displayed factor $1-k$, not $1+k$.

For each $\delta>0$ these are ordinary smooth chain rules. A factor $S_\delta'$ can become large near zeros as $\delta\downarrow0$, but its contribution has the favorable sign and is discarded before taking a limit. The proof never needs a uniform absolute-integrability bound for that derivative term, a finite crossing count, or a bounded-variation assertion for $\operatorname{sign}w$.

## 3. The truncation, zero sets, and level sets

The specified truncation exists, including when $L=0$. For example, choose a smooth nonincreasing $\rho:\mathbb R\to[0,1]$ equal to one on $(-\infty,0]$ and zero on $[1,\infty)$, and set

\[
T_{L,h}(x)=\int_0^x\rho\!\left(\frac{u-L}{h}\right)\,du.
\]

For $L\ge0$, it has $T(0)=0$, $T'(x)=1$ for $x\le L$, $T'(x)=0$ for $x\ge L+h$, and $T(x)\le L+h$ everywhere. It is generally negative when $x<0$, which is harmless: the proof needs an upper bound on $T$, not nonnegativity.

Multiplying (7) by $T'(X_\delta)\ge0$ gives

\[
(1-k_{\max})T'(X_\delta)d_\delta(f_1+f_2)
\le\frac{d}{ds}T(X_\delta)+T'(X_\delta)|b_1-b_2|.
\]

Since $X_\delta(0)=0$, integration proves (8). This is the precise place where the zero-readout initial condition removes the gap boundary term.

For fixed $L,h,t$ and a fixed coordinate path,

\[
X_\delta(s)\longrightarrow X(s)
=\operatorname{sign}(w(s))\Delta(s)
\]

at every time: when $w(s)=0$, both smoothed and limiting gaps are exactly zero. Also

\[
0\le d_\delta\le d,\qquad d_\delta\longrightarrow d,
\qquad
0\le T'(X_\delta)d_\delta(f_1+f_2)\le2d.
\]

The dominating function $2d$ is time-integrable on the fixed reference interval. Continuity of $T'$ therefore permits dominated convergence in the left side of (8), with no omission of times at which $X=L$. In particular,

\[
T'(L)=1
\]

for every $h>0$. After the $\delta$-limit,

\[
\int_{\{X\le L\}}d(f_1+f_2)
\le\int_0^tT'(X)d(f_1+f_2)
\le\frac{L+h+\int_0^t|b_1-b_2|}{1-k_{\max}}.
\]

The leftmost integral is independent of $h$. Taking the infimum over $h>0$ proves (9). No convergence of $T'$ as $h\downarrow0$ is required, so there is no hidden convention about an indicator's value on the level set. This remains valid when the level set has positive measure, and specifically at $L=0$.

At every point of the zero set of $w$, both $d$ and $d_\delta$ vanish. The choice of active label there has no effect. No assumption about the measure, isolation, or number of these zeros is needed.

**Cutoff quantifier:** the proof gives the inequality for every real $L\ge0$ on each fixed path. Thus, for a chosen endpoint $t$, substitution of the number $\log(1+B_t)$ is legitimate even though it depends on the entire path up to $t$. It remains constant in the integration variable. There is no differentiation of this number, stochastic integral, stopping-time requirement, or interchange of a random cutoff with an unproved expectation bound. A moving cutoff $L(s)$ would require a different chain rule, but none is used here.

## 4. Independent derivation of the positive-curvature estimate

Direct differentiation of the smoothed potential gives

\[
L_\delta'
=\alpha_\delta'(w)w'(H_1-H_2)
 -\alpha_\delta g_1z_1'-(1-\alpha_\delta)g_2z_2'.
\]

After substituting (1), the terms containing the direct top dynamics are

\[
-\epsilon\lambda w\bigl[\alpha_\delta f_1g_1
 -(1-\alpha_\delta)f_2g_2\bigr]
+\epsilon\lambda kw\bigl[\alpha_\delta f_2g_1
 -(1-\alpha_\delta)f_1g_2\bigr].
\]

These are exactly $-I_\delta+R_\delta$. The forcing term is
$-\alpha_\delta g_1b_1-(1-\alpha_\delta)g_2b_2\le|b_1|+|b_2|$, and the switching term is nonpositive. Thus the candidate's differential inequality has the correct signs and factors.

The two coefficient approximations are

\[
w\alpha_\delta(w)\to w_+,
\qquad w(1-\alpha_\delta(w))\to\min(w,0),
\]

each with absolute error at most $C\delta$. Since $f'\le1/4$, $0<f,g<1$, and $\lambda,k$ have uniform bounds, both integrands converge to the claimed active-label expressions with an error bounded by $C\delta\lambda_{\max}$. The possibly signed $I_\delta$ and $R_\delta$ do not need to be nonnegative before taking the limit.

Integrating the inequality, discarding the nonpositive term $-L_\delta(t)$, and using $\alpha_\delta(0)=1/2$ gives

\[
I_t\le A_0+Q_t+\int_0^tkd f(z_{\rm other})(1-f(z_{\rm active}))\,ds,
\quad A_0=\frac{H(z_1(0))+H(z_2(0))}{2}.
\]

In particular, the initial boundary value is the average $A_0$. It is not silently replaced by a chosen active label at $w(0)=0$. No terminal limit of $L_\delta(t)$ is needed.

Put $D_t=\int_0^t|b_1-b_2|\le Q_t$. On $X\le L$, the cross term without $k$ satisfies

\[
d f(z_{\rm other})(1-f(z_{\rm active}))
\le d(f_1+f_2),
\]

so (9) bounds its contribution after multiplying by $k$ by $c_k(L+D_t)$. On $X>L$, the exact identity

\[
f(y)(1-f(x))=\frac{e^y}{(1+e^y)(1+e^x)}\le e^{y-x}
\]

gives the bound $k_{\max}e^{-L}B_t$. Consequently the argument actually proves, for every $L\ge0$,

\[
I_t\le A_0+Q_t+c_k(L+D_t)+k_{\max}e^{-L}B_t.
\]

Setting $L=\log(1+B_t)$ and using $D_t\le Q_t$ yields the slightly sharper bound

\[
I_t\le A_0+c_k\log(1+B_t)
 +(1+c_k)Q_t+k_{\max}\frac{B_t}{1+B_t}.
\]

Replacing the last ratio by one proves exactly (4). Also
$\lambda|w|\phi''=\epsilon\lambda|w|f'=df'$, so there is no extra factor of $\epsilon$ in $I_t$.

Boundary checks do not expose a counterexample: at $B_t=0$, $I_t=0$ and the cutoff is $L=0$; at $k_{\max}=0$, the cross term vanishes and the estimate reduces to $I_t\le A_0+Q_t$. The deterioration as $k_{\max}\uparrow1$ is explicit and consistent with the loss of uniform Gram coercivity.

## 5. The entire homogeneous two-by-two Gram-metric bound

Let $D=\operatorname{diag}(\phi''(z_1),-\phi''(z_2))$. With the readout, Gram, and lower-motion path frozen as time-dependent coefficients, the top Jacobian is

\[
A=\frac w2 GD
=\lambda w\begin{pmatrix}
\phi''_1&-k\phi''_2\\k\phi''_1&-\phi''_2
\end{pmatrix}.
\]

For $\eta'=A\eta$ and $E=\eta^TG^{-1}\eta$, matrix differentiation gives

\[
A^TG^{-1}+G^{-1}A=wD,
\]

and hence

\[
E'=w(\phi''_1\eta_1^2-\phi''_2\eta_2^2)
 -\eta^TG^{-1}G'G^{-1}\eta.
\]

This identity includes both off-diagonal entries of $A$. No componentwise stability assumption or commutation of the matrices at different times is needed.

To bound the positive coordinate, write

\[
\eta_a=e_a^TG^{1/2}G^{-1/2}\eta,
\qquad
\eta_a^2\le(e_a^TGe_a)E=2\lambda E.
\]

For $w>0$, only the first curvature term is positive; for $w<0$, only the second is positive. Dropping the other term thus gives

\[
w(\phi''_1\eta_1^2-\phi''_2\eta_2^2)
\le2\lambda|w|\phi''(z_{\rm active})E
=2d f'(z_{\rm active})E.
\]

At $w=0$, the entire curvature term vanishes. The sign selection therefore remains harmless in this calculation as well.

With $v=G^{-1/2}\eta$, the metric term is

\[
-v^T(G^{-1/2}G'G^{-1/2})v\le m(s)|v|^2=m(s)E.
\]

Let uniform Gram eigenvalue bounds be $\gamma_-I\preceq G(s)\preceq\gamma_+I$, where one may take

\[
\gamma_-=2\lambda_{\min}(1-k_{\max}),\qquad
\gamma_+=2\lambda_{\max}(1+k_{\max}).
\]

Then

\[
m(s)\le\gamma_-^{-1}\|G'(s)\|_{\rm op}\le Ca(s),
\qquad
\int_0^tm(s)\,ds\le C\sqrt{S_{\max}},
\]

using $\int a^2\le1$. This is the needed cost of the changing metric. Omitting it would not be justified for a moving Gram; the candidate retains and controls it.

Multiplication of (13) by the scalar integrating factor gives

\[
E(t)\le E(0)\exp\!\left(2I_t+\int_0^tm(s)\,ds\right).
\]

The endpoint metric comparison therefore yields explicitly

\[
\|\Psi(t,0)\|_{\rm op}
\le\sqrt{\frac{\gamma_+}{\gamma_-}}
\exp\!\left(I_t+\frac12\int_0^tm(s)\,ds\right).
\]

The square root is essential: it converts energy growth $2I_t$ to operator-norm growth $I_t$. Absorbing the deterministic metric bound and $e^{k_{\max}}$, and then inserting (4), proves (14) exactly. The constant can depend on the conditional primal/coercivity constants and $S_{\max}$, but not on individual pointwise readout suprema or on the number of sign switches.

One useful clarification is that the same bound using history from zero also bounds $\Psi(t,s)$ for $0\le s\le t$: its curvature integral is $I_t-I_s\le I_t$, and its metric variation is bounded by the same total variation. This does not produce a bound expressed solely in the history after $s$, nor a restartable canonical theorem. For a fresh scalar estimate starting at $s$, the potential and gap boundary terms must be retained.

## 6. What the population bounds establish, and what they do not

From (3) and the action bound,

\[
\|B_S\|_2
\le\epsilon\lambda_{\max}\int_0^S\|w(s)\|_2\,ds\le CS_{\max},
\]

\[
\|Q_S\|_2
\le\int_0^S(\|b_1(s)\|_2+\|b_2(s)\|_2)\,ds
\le C\sqrt{S_{\max}}.
\]

The inequality $H(z)\le\log2+|z|$ gives $\|A_0\|_2\le C$. Since $\log(1+B)\le B$, (4) gives a uniform $L^2$ bound on $I_t$. The right side of (14), after taking $\log^+$ and choosing its constant at least one, is bounded by

\[
\log C+A_0+(1+c_k)Q_t+c_k\log(1+B_t).
\]

It too is uniformly in $L^2$. The nonnegative integrals $I_t,B_t,Q_t$ increase with $t$; substituting their full-horizon values gives the asserted time-supremum conclusions. If the before-fit interval is open at $S$, these statements use the monotone limits as $t\uparrow S$; no differentiability at the endpoint is necessary.

These are logarithmic response bounds, not ordinary response-moment bounds. For any requested $p>0$, raising (14) to the power $p$ produces the unresolved integrability requirement

\[
\mathbb E_3\!\left[
e^{pA_0+p(1+c_k)Q_S}(1+B_S)^{pc_k}
\right]<\infty
\]

with uniform control across the references if a uniform response bound is wanted. Separate factor estimates must have enough margin to control their product, for example through appropriate Hölder exponents; no independence is available. Even the polynomial factor alone can require more than the supplied second moment when $pc_k>2$. In particular, for a second response moment the polynomial factor is already of order $2c_k$.

There are elementary obstructions to inferring the missing estimates from $L^2$ information alone. On $(0,1)$ with uniform measure, $q(x)=x^{-1/4}$ has finite second moment but $\int_0^1e^{cq(x)}dx=\infty$ for every $c>0$. Its bounded truncations have uniformly bounded second moments and unbounded exponential moments. This is an integrability counterexample to the proposed inference from an $L^2$ norm; it is not a claimed counterexample produced by the actual trained reference family.

The canonical Gaussian assertion about the initial factor is correct. For a Gaussian marginal $Z$,

\[
\mathbb E e^{r|Z|}\le\mathbb E e^{rZ}+\mathbb E e^{-rZ}<\infty.
\]

Applying Cauchy--Schwarz to the two initial fields shows that $e^{A_0}$ has every finite moment without requiring their independence. The same conclusion is not uniform for arbitrary bounded approximations that merely converge strongly in $L^2$. For example,

\[
z_{1,n}(x)=z_{2,n}(x)=-n\,\mathbf1_{(0,n^{-4})}(x)
\]

converge to zero in $L^2$, since each squared norm equals $n^{-2}$, but

\[
\mathbb E e^{pA_{0,n}}\ge n^{-4}e^{pn}\longrightarrow\infty
\qquad(p>0).
\]

Again this demonstrates the insufficiency of strong $L^2$ convergence by itself, without asserting that these scalar fields implement the imported training construction. It supports the candidate's explicit distinction between canonical Gaussian initialization and unrestricted approximating fields.

Finally, the full tangent equations include, schematically but with exact direct-top coefficients,

\[
\delta z'=A\delta z+\frac{\delta w}{2}Gq
 +\frac w2\delta G\,q+\delta b,
\qquad q=(\phi'(z_1),-\phi'(z_2))^T,
\]

\[
\delta w'=\tfrac12\bigl(\phi'(z_1)\delta z_1-\phi'(z_2)\delta z_2\bigr).
\]

The terms $\delta b$ and $\delta G$ arise from matrix and lower-layer variations; they need not be independent of the other tangent fields. Estimate (14) controls the homogeneous $A$-block and does not estimate these terms, their coupling, or the needed inhomogeneous response. The primal forcing $b$ has been retained in the scalar argument, but that is not a bound for its variation $\delta b$.

## 7. Required versus optional fixes

### Required for this conditional lemma

**None found.** The switching inequality has the correct sign; the smoothing/truncation procedure covers zero sets and level sets; the pathwise logarithmic cutoff is legal; and the Gram-metric argument proves the entire stated homogeneous two-by-two bound with the claimed exponent. No displayed new implication needs reversal or a missing multiplicative factor under the accepted premise.

The conditional status must be preserved. This audit does not promote the unread global-reference, coercivity, or common-space premise to a proved theorem. Uniform claims must retain the reference-index range on which that premise supplies uniform coercivity.

### Required before any broader theorem claim

These are outstanding proof obligations, not defects in the limited lemma as stated:

1. Control the actual lower-forcing exponential and sufficient joint/higher moments for the desired response norm, or replace (14) with an argument that avoids those costs.
2. Establish the required initial-factor control uniformly for whatever approximation class is used; canonical Gaussian integrability alone does not certify arbitrary bounded approximations.
3. Estimate the readout and lower-layer coupled variations and the inhomogeneous terms, then justify the required limiting response and continuation statements.
4. Supply whatever uniqueness, common-space passage, and restarting argument the canonical global-flow claim requires. The zero-readout history estimate does not itself supply these conclusions.

### Optional improvements to the candidate's presentation

1. Display the domination $0\le T'(X_\delta)d_\delta(f_1+f_2)\le2d$, and say explicitly that the $h$-limit is taken only after the fixed occupation integral has been bounded. This makes the treatment of $X=L$ immediately checkable.
2. Include the intermediate bound $I_t\le A_0+Q_t+c_k(L+D_t)+k_{\max}e^{-L}B_t$. It exposes every coefficient in (4), and optionally retains the sharper final term $k_{\max}B_t/(1+B_t)$.
3. Display the endpoint factor $\sqrt{\gamma_+/\gamma_-}\exp(\frac12\int m)$ before absorbing it into $C$. This makes both the nonnormal two-by-two control and the energy-to-norm factor transparent.
4. State moment requirements relative to a target exponent $p$, rather than only observing that $c_k$ may exceed two. The issue is $pc_k$ even before accounting for products of dependent factors.
5. Clarify that later-time propagators can still use the original zero-time history bound, while a bound using only post-restart history needs new boundary terms. This is a clarification, not a correction of the canonical-flow disclaimer.

**Final classification: the new actual-path curvature and homogeneous top-block lemma passes conditionally. Ordinary response moments, the coupled global response, and the canonical theorem remain unproved by this candidate.**

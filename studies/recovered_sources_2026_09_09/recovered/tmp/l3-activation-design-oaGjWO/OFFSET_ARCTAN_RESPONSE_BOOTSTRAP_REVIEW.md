# Adversarial audit: fixed-offset arctangent response bootstrap

## Identification and review scope

Candidate reviewed in full:
`/tmp/l3-activation-design-oaGjWO/OFFSET_ARCTAN_RESPONSE_BOOTSTRAP.md`

Exact candidate proof SHA256, verified from the file:

```text
65579a94f883f1b9f9240430039f334f5b3b663599cd7ab16bb15c35f7bacc43
```

Explicit dependency:
`/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md`

Dependency SHA256, also verified:

```text
f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4
```

Only dependency lines 211–455 and 730–1055 were inspected for mathematical content. The required `/etc/codex/skills/solve-math-rigorously/SKILL.md` was read completely. No other research files, task history, external sources, simulations, or subagents were used. References below use the files' original one-based line numbers. The candidate was not modified.

The displayed scalar system, its Gaussian source laws, and its frozen-coefficient formal derivative convention are premises of this audit, as requested. This is an audit of a finite scalar response lemma on feature horizon \(S=M\Delta\le3/2\), not a certification of a global mean-field, gradient-flow, or gradient-descent theorem.

## Verdict

| Claim or proposed use | Verdict and exact scope |
| --- | --- |
| \(U_k<9/10\), uniformly in the stated mesh and clipping parameters | **PASS**, under the displayed scalar-system premise. In fact \(U_k\le2482563/2880000<9/10\). |
| \(V_k\le3067/3200<1\), with the same uniformity | **PASS**, under that premise. |
| Candidate equation (1), the Gaussian tail of \(q^{(2)}_k\) beyond \(7/6\) | **PASS**, uniformly for each \(k\le M\), including arbitrarily correlated or singular time-source laws. |
| Physical-horizon implication, candidate lines 255–267 | **PASS, conditional** on the stated constructed uncut feature flow, zero initial readout, actual gradient identity, and the stated continuity of \(f'\). |
| Treating the cited identification theorem as an already proved identification for the offset activation and every clipping map allowed here | **FAIL as an inference from the citation alone.** The dependency is stated for another activation and a more restrictive clipping class. The candidate expressly leaves representation transfer separate, so this is not a failure of its scalar lemma. |
| An unconditional global theorem, cutoff removal, flow construction, or raw-GD transfer | **Not established or certified by this audit; not claimed by this candidate.** |

No fatal gap, circular bootstrap, missing same-time derivative, or incorrect numerical constant was found in the scalar proof. The detailed verification follows. It first isolates the activation-transfer issue, then proves the estimates using only strictly earlier response rows, and finally verifies the separate time change.

## 1. Activation and identification checks

Use \(a=7/6\) throughout. For the candidate's activation and coordinate transformation,

\[
\phi'(z)=\frac1{10(1+z^2)},\qquad
\phi''(z)=-\frac{z}{5(1+z^2)^2},\qquad
F'(z)=10(1+z^2)=\frac1{\phi'(z)}.
\]

The increasing polynomial \(F\) maps \(\mathbb R\) onto \(\mathbb R\). Writing \(z=F^{-1}(x)\) gives

\[
\chi'(x)=\frac{\phi'(z)}{F'(z)}
=\frac1{100(1+z^2)^2}\le\frac1{100}.
\]

Thus the factor \(1/100\) in the bottom response is correct. The elementary bound \(\pi<10/3\) yields \(5/6<\phi<7/6\). Also \(|z|/(1+z^2)^2\le1\), so the candidate's deliberately loose \(|\phi''|\le1/5\) is valid. No old unscaled gate derivative is used in the candidate's estimates.

There is a real activation distinction at the identification boundary. Dependency line 217 explicitly assumes \(\phi=\arctan\), \(F(z)=z+z^3/3\); dependency lines 734–740 use those same maps and a different horizon in its local bootstrap. These are not literally the candidate's maps. Its response identities have the same structural form, but a citation to that specialized statement alone does not prove their identification for \(1+\arctan/10\).

The candidate does correctly use uncentered query second moments. For example, at initialization, if \(G\sim N(0,1)\), symmetry gives

\[
\mathbb E H^{(1)}_0=1,\qquad
\mathbb E(H^{(1)}_0)^2
=1+\frac1{100}\mathbb E(\arctan G)^2.
\]

The variance of \(H^{(1)}_0\) omits the first term (1). Centering the activation before assigning the variance of \(\xi^{(2)}_0\) would therefore change the source law. Candidate lines 73–76 retain the necessary term, consistently with dependency lines 255–260 and 375. Gaussian matrix outputs can be centered while their input queries have nonzero means; it is the uncentered input second moment that determines their variance.

The dependency's general conditioning argument at lines 299–402 is formulated through smooth coordinate maps, not through oddness of the activation. The offset itself consequently presents no visible structural obstruction to adapting it. However, its fixed-mesh application assumes bounded clipping \(|\tau_R|\le2R\) (line 217), which ensures bounded derivatives of the product \(\phi'(z)\tau_R(q)\) at fixed \(R\). The candidate's two displayed clipping assumptions also allow \(\tau_R(q)=q\); for that map the product's derivative in \(z\) is unbounded as \(q\) varies. The dependency's globally Lipschitz coordinate-map theorem therefore does not directly cover the candidate's entire formal clipping class. Such identification would require the appropriate bounded clipping assumption or a further argument. This affects transfer, not the response inequalities below, which need only the two stated bounds on \(\tau_R\).

Candidate lines 14–15 explicitly reserve representation transfer, and lines 269–273 reserve the subsequent global obligations. Accordingly, the activation distinction is a scope limitation, not a hidden use of an inapplicable theorem inside the scalar estimates.

## 2. Causality, singular sources, and time zero

All derivatives below hold deterministic coefficients fixed and treat the named source coordinates as separate formal arguments, even when the Gaussian law is singular. No derivative of a covariance square root is involved. In particular, singularity does not justify setting a formal derivative to zero merely because its source is zero almost surely.

At time zero \(W^{(4)}_0=0\) as a formal expression. Hence \(\delta^{(3)}_0=0\), all its source derivatives vanish, and \(b^{(3)}_{00}=0\). Its covariance formula gives \(\zeta^{(2)}_0=0\) almost surely. The condition \(|\tau_R(u)|\le|u|\) implies \(\tau_R(0)=0\), so \(q^{(2)}_0=\delta^{(2)}_0=0\) almost surely. The relevant formal derivative, evaluated under this law, is

\[
\partial_{\xi^{(2)}_0}\delta^{(2)}_0
=\phi''(Z^{(2)}_0)\tau_R(0)=0.
\]

Consequently \(b^{(2)}_{00}=0\), and the other backward variance and field also vanish. Thus \(U_0=V_0=0\). This base case does not incorrectly discard the generally nonzero formal derivative in the degenerate \(\zeta^{(2)}_0\) direction.

For the induction step fix \(k\ge1\) and assume \(U_r,V_r\le1\) only for \(r<k\). The causal dependencies are:

1. \(H^{(1)}_k\) uses only bottom response rows before \(k\), determining \(a^{(2)}_{k\cdot}\).
2. \(Z^{(2)}_k\) uses only previous \(\delta^{(2)}\). Its derivatives in past \(\zeta^{(2)}\) directions use only \(b^{(3)}\) rows before \(k\), determining \(a^{(3)}_{k\cdot}\).
3. With \(a^{(3)}\) fixed, the top recursion uses its own \(\xi^{(3)}\) group and determines \(\delta^{(3)}_k\), then \(b^{(3)}_{k\cdot}\).
4. The current \(b^{(3)}\) row is therefore available before estimating \(q^{(2)}_k\), \(\delta^{(2)}_k\), and \(b^{(2)}_{k\cdot}\).

Distributional dependence of coefficients on previous population calculations does not add derivative paths under the explicit convention. No current \(U_k\) is used in this construction or in the bounds that follow.

## 3. Bottom and middle derivative estimates

The discrete comparison used here can be checked directly: if \(b\ge0\), \(d_j\ge0\), \(c_r\ge0\), and

\[
d_j\le b+\sum_{r<j}c_r\max_{v\le r}d_v,
\]

then

\[
\max_{v\le j}d_v\le b\prod_{r<j}(1+c_r)
\le b\exp\!\left(\sum_{r<j}c_r\right).
\]

Indeed, the comparison sequence \(y_j=b\prod_{r<j}(1+c_r)\) is nondecreasing and satisfies \(y_j=b+\sum_{r<j}c_ry_r\); induction bounds each \(d_j\) and its running maximum by \(y_j\). This also handles \(b=0\).

For a fixed bottom source \(\zeta^{(1)}_s\), differentiation and the induction hypothesis give candidate lines 103–106. Applying this comparison with forcing \(b=\Delta\), coefficients \(\Delta/100\), and then the bound on \(\chi'\), yields

\[
\left|\partial_{\zeta^{(1)}_s}H^{(1)}_j\right|
\le\frac\Delta{100}e^{S/100}\quad(s<j\le k).
\]

Since \(e^{3/200}<2\),

\[
|a^{(2)}_{js}|\le\Delta\left(\frac{49}{36}+
\frac{e^{S/100}}{100}\right)
<\Delta\left(\frac{49}{36}+\frac1{50}\right)
=\frac{1243}{900}\Delta<\frac32\Delta.
\]

Set \(A=3/2\), \(\overline{\mathcal R}_j=\max_{v\le j}\mathcal R_v\), and \(c_r=|q^{(2)}_r|/5+V_r/100\). The exact chain rule gives

\[
|\partial\delta^{(2)}_r|
\le\frac{|q^{(2)}_r|}{5}|\partial Z^{(2)}_r|
+\frac1{10}|\partial q^{(2)}_r|.
\]

For a \(\xi^{(2)}_s\) derivative,

\[
\partial q^{(2)}_r
=\sum_{v\le r}b^{(3)}_{rv}\phi'(Z^{(2)}_v)
\partial Z^{(2)}_v.
\]

The direct identity term in \(Z^{(2)}_j\) contributes exactly (1) to the derivative row sum, not one for every past time. All derivatives at source times later than a variable's time vanish. Summing absolute values therefore gives

\[
\mathcal R_j\le1+A\Delta\sum_{r<j}c_r\overline{\mathcal R}_r,
\qquad
\overline{\mathcal R}_j\le
\exp\!\left(A\Delta\sum_{r<j}c_r\right)=E_j.
\]

For a fixed \(\zeta^{(2)}_s\) derivative, the expression for \(\partial q^{(2)}_r\) instead contains \(\mathbf1_{r=s}\). Its contribution in \(Z^{(2)}_j\) has magnitude at most \(A\Delta/10\). All other contributions obey the same comparison. Hence

\[
|\partial_{\zeta^{(2)}_s}Z^{(2)}_j|
\le\frac{A\Delta}{10}E_j,\qquad
|\partial_{\zeta^{(2)}_s}H^{(2)}_j|
\le\frac{A\Delta}{100}E_j.
\]

These bounds include the effect of that source in every later equation. The current \(\zeta^{(2)}_j\) has no direct or indirect entry into \(Z^{(2)}_j\). Thus candidate equations (2)–(3) are valid using only the induction hypotheses at times strictly before \(k\).

## 4. Envelope moments and the top forward coefficient

Bounded activation and the readout sum give, without any response bootstrap,

\[
|W^{(4)}_r|\le aS,\quad
|\delta^{(3)}_r|\le aS/10,\quad
\operatorname{Var}(\zeta^{(2)}_r)\le(aS/10)^2
\le\sigma^2,\qquad \sigma=7/40.
\]

For \(r<k\), \(|q^{(2)}_r|\le|\zeta^{(2)}_r|+a\). For a centered Gaussian \(G\) of variance \(v\), including \(v=0\),

\[
\mathbb E e^{\lambda|G|}
\le\mathbb E(e^{\lambda G}+e^{-\lambda G})
=2e^{\lambda^2v/2}\qquad(\lambda\ge0).
\]

For \(j>0\), convexity of the exponential gives precisely the finite Jensen inequality at candidate lines 174–176. Combining these facts proves

\[
\mathbb E E_j^p
\le2\exp\left\{
pAS\left(\frac a5+\frac1{100}\right)
+\frac12\left(\frac{pAS}{5}\right)^2
\left(\frac{aS}{10}\right)^2\right\}
\le2\exp\left\{\frac{219p}{400}+
\frac{3969p^2}{1280000}\right\}.
\]

The constants follow from \(AS\le9/4\), \(a/5+1/100=73/300\), and \(aS/10\le7/40\). In particular, the last quadratic coefficient is

\[
\frac12\left(\frac9{20}\right)^2\left(\frac7{40}\right)^2
=\frac{3969}{1280000}.
\]

No product of expectations and no independence across times are used. Dependence between a source and its bounded shift also causes no problem because that shift has already been bounded pointwise.

For \(p=1,2\), the exponent after taking the \(p\)-th root is at most \(219/400+7938/1280000<3/5\). Consequently

\[
\|E_j\|_1<2e^{3/5}<4,\qquad
\|E_j\|_2<\sqrt2e^{3/5}<2\sqrt2<3.
\]

The separate value \(E_0=1\) obeys the same bounds. The estimates on the exponent do not overlook the prefactor \(2^{1/p}\). The elementary exponential comparison used by the candidate is valid: \(e<3\) and \(3^3<2^5\) imply \(e^{3/5}<2\).

Taking expectations of the individual \(\zeta^{(2)}_s\) response, not replacing them by pointwise deterministic bounds, now gives

\[
|a^{(3)}_{js}|\le\Delta\left(a^2+\frac A{100}\mathbb E E_j\right)
\le\Delta\left(\frac{49}{36}+\frac3{50}\right)
=\frac{1279}{900}\Delta<A\Delta.
\]

All required response expectations at this stage are integrable. This verifies candidate equations (4)–(6).

## 5. Top response, current middle field, and both row bounds

Let \(D_j=\sum_{s\le j}|\partial_{\xi^{(3)}_s}\delta^{(3)}_j|\) and \(\overline T_j=\max_{v\le j}T_v\). Differentiating both factors of \(W^{(4)}_j\phi'(Z^{(3)}_j)\) gives

\[
D_j\le\frac\Delta{100}\sum_{r<j}T_r+\frac{aS}{5}T_j
\le\frac{73}{300}S\overline T_j.
\]

The \(1/100\) term contains one gate derivative from the readout sum and one from the current top gate. The \(aS/5\) term accounts for differentiation of that current gate.

The strictly causal recursion for \(Z^{(3)}_j\) gives

\[
T_j\le1+A\Delta\sum_{r<j}D_r,
\qquad
\overline T_j\le\exp\left(A\frac{73}{300}S^2\right)
\le e^{657/800}<\frac52.
\]

For the final strict inequality, \(657/800<5/6\), \(e<3\), and \(3^5 2^6=15552<15625=5^6\) suffice. Adding the coefficient's learned term yields

\[
\begin{aligned}
V_k
&\le\mathbb E D_k+\Delta\sum_{s<k}
|\mathbb E[\delta^{(3)}_k\delta^{(3)}_s]|\\
&\le\frac{73}{300}S\frac52+\frac{a^2S^3}{100}\\
&\le\frac{73}{80}+\frac{147}{3200}
=\frac{3067}{3200}<1.
\end{aligned}
\]

This obtains the current \(V_k\) before using a bound on the current middle query. Minkowski's inequality, which requires no independence, then gives

\[
\|q^{(2)}_k\|_2
\le\|\zeta^{(2)}_k\|_2+aV_k
\le\frac7{40}+\frac76=\frac{161}{120}=:Q,
\qquad \|\delta^{(2)}_k\|_2\le Q/10.
\]

The earlier rows have the same bound using their already known \(V_r\le1\). In particular, no current \(U_k\) has entered.

For clarity, the same-time derivatives are exactly

\[
b^{(3)}_{kk}=\mathbb E[W^{(4)}_k\phi''(Z^{(3)}_k)],
\]

\[
b^{(2)}_{kk}
=\mathbb E[\phi''(Z^{(2)}_k)\tau_R(q^{(2)}_k)]
+b^{(3)}_{kk}\mathbb E[(\phi'(Z^{(2)}_k))^2
\tau_R'(q^{(2)}_k)].
\]

Here \(\partial_{\xi^{(2)}_k}q^{(2)}_k=b^{(3)}_{kk}\phi'(Z^{(2)}_k)\), whereas all earlier \(H^{(2)}_v\) have zero derivative in that current source. These formulas agree with dependency lines 434–445 after replacing the activation. The candidate's \(V_k/100\) term includes this return; it is not discarded.

More generally the full current derivative row satisfies

\[
\sum_{s\le k}|\partial_{\xi^{(2)}_s}\delta^{(2)}_k|
\le\left(\frac{|q^{(2)}_k|}{5}+\frac{V_k}{100}\right)E_k.
\]

For each coefficient use \(|\mathbb E D|\le\mathbb E|D|\). Cauchy–Schwarz, applied to the possibly dependent \(q^{(2)}_k,E_k\), and also to each learned covariance term, then gives

\[
\begin{aligned}
U_k
&\le\frac15\|q^{(2)}_k\|_2\|E_k\|_2
+\frac{V_k}{100}\|E_k\|_1
+\Delta\sum_{s<k}\|\delta^{(2)}_k\|_2\|\delta^{(2)}_s\|_2\\
&\le\left(\frac Q5+\frac1{100}\right)3+\frac{SQ^2}{100}\\
&\le\frac{167}{200}+\frac{77763}{2880000}
=\frac{2482563}{2880000}<\frac9{10}.
\end{aligned}
\]

In the second line it is legitimate to use \(\|E_k\|_1\le\|E_k\|_2<3\), not just the separate looser \(L^1\) bound (4). The arithmetic has positive margins

\[
1-\frac{3067}{3200}=\frac{133}{3200},\qquad
\frac9{10}-\frac{2482563}{2880000}
=\frac{109437}{2880000}.
\]

Thus ordinary simultaneous induction closes. All uses of \(E_j\) concern past \(V_r\), the current \(V_k\) is proved before the current \(q^{(2)}_k\) estimate, and the current \(U_k\) is the last quantity bounded. Candidate equations (7)–(9) contain no circular current-row assumption. The constants depend only on the fixed numerical horizon and activation bounds, not \(R,M,\Delta\).

## 6. Gaussian tails and their exact meaning

Write \(q^{(2)}_k=\zeta^{(2)}_k+\beta_k\). The proved row bound gives \(|\beta_k|\le aV_k\le a=7/6\) pointwise, and the Gaussian variance is at most \(\sigma^2=(7/40)^2\). Therefore

\[
\{|q^{(2)}_k|>a+x\}\subseteq\{|\zeta^{(2)}_k|>x\}.
\]

For any centered Gaussian \(G\) with variance at most \(\sigma^2\), Markov's inequality and its Gaussian exponential moment give

\[
\mathbb P(G>x)\le\inf_{\lambda>0}
e^{-\lambda x+\lambda^2\sigma^2/2}
=e^{-x^2/(2\sigma^2)}.
\]

Applying this to both signs proves exactly candidate equation (1). Zero variance presents no exception. Independence of \(\beta_k\) and the source is neither asserted nor required.

The positive-part tail assertion can be made explicit. For \(L>a\), let \(u=L-a\). Integrating the bound gives

\[
\begin{aligned}
\mathbb E(|q^{(2)}_k|-L)_+^2
&=2\int_0^\infty t\,\mathbb P(|q^{(2)}_k|>L+t)\,dt\\
&\le4\int_0^\infty t e^{-(u+t)^2/(2\sigma^2)}\,dt\\
&\le4\sigma^2e^{-u^2/(2\sigma^2)}.
\end{aligned}
\]

The ordinary tail second moment also vanishes uniformly. The identity

\[
\mathbb E[Y^2\mathbf1_{Y>L}]
=L^2\mathbb P(Y>L)+\int_L^\infty2y\,\mathbb P(Y>y)\,dy
\]

for \(Y\ge0\), together with

\[
\int_u^\infty e^{-x^2/(2\sigma^2)}\,dx
\le\frac1u\int_u^\infty xe^{-x^2/(2\sigma^2)}\,dx
=\frac{\sigma^2}{u}e^{-u^2/(2\sigma^2)},
\]

gives

\[
\mathbb E[(q^{(2)}_k)^2\mathbf1_{|q^{(2)}_k|>L}]
\le\left(2L^2+4\sigma^2+\frac{4a\sigma^2}{u}\right)
e^{-u^2/(2\sigma^2)}.
\]

These are marginal bounds with constants uniform over \(k\) and all allowed meshes and clippings. They do not assert a mesh-independent Gaussian bound for the maximum over all times. The parameter \(7/40\) bounds the Gaussian source standard deviation; it is not a claimed centered moment-generating-function proxy for the entire query with its random shift. In the usual tail sense the query is uniformly subGaussian, exactly as its displayed shifted tail states.

## 7. Separate conditional physical-horizon implication

Assume the candidate's specified uncut feature flow already exists on \([0,3/2]\), has the zero initial readout \(f(0)=0\), and satisfies its actual gradient identity with nonnegative terms and \(K^{(4)}=\mathbb E[(H^{(3)})^2]\). Assume also the stated continuity of \(f'\). Then

\[
f'(s)\ge\mathbb E[(H^{(3)}(s))^2]\ge m,
\qquad m=25/36.
\]

It follows by integration that \(f\) is strictly increasing and \(f(36/25)\ge1\). Continuity and \(f(0)=0\) give a unique (s_*\in(0,36/25]) with (f(s_*)=1). The strict feature-horizon margin is

\[
\frac32-\frac{36}{25}=\frac3{50}>0.
\]

Since \(f'\) is continuous on the compact interval \([0,s_*]\), its maximum \(B\) is finite and \(B\ge m\). For \(0\le s\le s_*\), the fundamental theorem of calculus gives both estimates

\[
m(s_*-s)\le1-f(s)=\int_s^{s_*}f'(u)\,du
\le B(s_*-s).
\]

One can construct the physical clock without assuming a continuation theorem. Define

\[
t(s)=\int_0^s\frac{du}{2(1-f(u))},\qquad 0\le s<s_*.
\]

The integrand is positive and continuous on every compact subinterval, so \(t(s)\) is finite there and strictly increasing. The upper bound on \(1-f\) gives

\[
t(s)\ge\frac1{2B}\log\frac{s_*}{s_*-s}\longrightarrow\infty
\quad\text{as }s\uparrow s_*.
\]

Thus this clock has an inverse \(s(t)\) for all \(t\ge0\). Differentiating the inverse yields \(s'=2(1-f(s))\), \(s(0)=0\), and separation of variables gives uniqueness while \(s<s_*\). Equivalently, for \(y(t)=s_*-s(t)\),

\[
-2By(t)\le y'(t)\le-2my(t),\qquad
s_*e^{-2Bt}\le y(t)\le s_*e^{-2mt}.
\]

In particular, \(s(t)<s_*\) at every finite physical time, as claimed in candidate lines 265–267. Composing the already assumed uncut feature flow with this clock defines its time-reparametrized physical trajectory for all finite times, under the stated feature/physical-flow relation. This argument supplies no construction of the assumed feature flow and uses no assertion that a clipped auxiliary trajectory is a gradient flow.

The continuity or a comparable local upper bound on \(f'\) matters for the nonattainment argument; the lower bound alone would not supply it. The candidate explicitly includes continuity in the implication, so this is not a missing assumption in the claim being certified.

Finally, the transformed update distinction at candidate lines 272–273 and dependency lines 1042–1051 is correct. If an ordinary bottom-coordinate Euler step were \(z\mapsto z+\varepsilon\), with \(\varepsilon=\Delta\phi'(z)q\), the exact polynomial identity would be

\[
F(z+\varepsilon)-F(z)
=10(1+z^2)\varepsilon+10z\varepsilon^2+
\frac{10}{3}\varepsilon^3
=\Delta q+10z\varepsilon^2+\frac{10}{3}\varepsilon^3.
\]

Consequently it is not exactly the candidate's \(X\mapsto X+\Delta q\) step. No raw-GD identification or transfer is proved by the scalar bounds or by the conditional physical clock argument.

## Final scope statement

**PASS for the fixed-offset scalar response lemma at the exact candidate hash above, conditional on its displayed source representation. PASS for the separately stated physical-horizon implication with its explicit flow and regularity hypotheses.** The claimed uniform numerical bounds, same-time returns, expectation estimates, and Gaussian tails survive adversarial checking. **FAIL only for an attempted inference that the old activation-specific dependency, without adaptation, already supplies offset-activation identification or an unconditional global theorem.** The candidate itself appropriately reserves those further obligations.

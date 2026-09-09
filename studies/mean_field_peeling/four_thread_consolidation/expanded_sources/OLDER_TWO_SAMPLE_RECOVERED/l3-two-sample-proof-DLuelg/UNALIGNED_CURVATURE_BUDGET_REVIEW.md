# Independent adversarial audit of the unaligned curvature budget

Audited source: `/tmp/l3-two-sample-proof-DLuelg/UNALIGNED_CURVATURE_BUDGET.md`.

Source SHA-256:

```text
a1790728bd693e28140407df96f90a82641f3b7858cf2bf2b59489cef8e19bfe
```

This audit uses only the identified note as mathematical input. The requested `solve-math-rigorously/SKILL.md` was read as procedural guidance. No other project mathematics, reviews, history, external sources, agents, or experiments were used. All tests below are analytic.

**Verdict.** The scalar estimate (2) is correct under its stated forced-system hypotheses, including arbitrary continuous forcing and arbitrary readout zero sets. The constants, the sign of the smoothing term, and the correction coefficient $HR^2$ check out. No correction to the scalar statement is required. The averaged calculation is also correct conditional on the raw Hilbert gradient-action identity, a common or uniformly bounded Gram coefficient, and the asserted lower forward-derivative bound. Section 4 does not specify the lower forward equations or the raw parameter spaces sufficiently to verify that last bound from this document alone. Its conditional consequence can be made fully self-contained by stating those analytic hypotheses explicitly; a precise sufficient formulation and proof appear below. Neither an exponential-response estimate nor population existence is needed for this verdict or claimed by the source.

## 1. Setup and quantities that must remain distinct

Take a finite interval $[0,S]$, initially with $S>0$. Let $w,z_1,z_2$ satisfy (1), with the regularity and continuous coefficients stated in the note. The condition $g>|h|$ implies $g>0$ and

\[
0<c=g-h_+\le g,\qquad h_+=\max(h,0),\qquad 0\le H=\max_{[0,S]}h_+<\infty.
\]

Here $c$ and $H$ refer to the Gram coefficients. In the action discussion I denote the population objective by $\mathcal J$, since the note also calls that different object $g$. The two uses of $g$ should not be conflated.

All scalar trajectories and coefficients are bounded on the compact interval. The curvature $\beta$ is continuous, being the maximum of three continuous functions. Although $\mathbf 1_{wF<0}$ need not be continuous, the product in the estimate is

\[
|wF|\mathbf 1_{wF<0}=(-wF)_+,
\]

which is continuous. Consequently the scalar integrals are ordinary finite integrals. No unstated summability condition on crossings is needed.

The proof has three components: an exact selected-gate derivative on each nonzero-sign sector, a monotone smoothing that joins these sectors without a negative crossing cost, and a bounded endpoint range. The population step then averages this deterministic estimate and supplies separate action bounds for its two costs.

## 2. Gate constants and the feature-coordinate comparison

Write $t=e^z/(1+e^z)\in(0,1)$. Direct differentiation gives

\[
p(z)=1+t,\qquad \phi''(z)=t(1-t),\qquad
r(z)=\frac{t(1-t)}{1+t}.
\]

Thus $1<p<2$, $0<\phi''\le1/4$, and $0<\log p<\log2$. For the ratio,

\[
\frac{d}{dt}\frac{t(1-t)}{1+t}
=\frac{1-2t-t^2}{(1+t)^2}.
\]

The numerator changes from positive to negative at $t_* =\sqrt2-1$, the unique root in $(0,1)$. The endpoint limits are zero, so this is the global maximum. Substitution yields

\[
r_{\max}=3-2\sqrt2=R.
\]

The maximizing feature coordinate is $z_*=-\tfrac12\log2$. In particular, $R$ is an attained maximum, despite the strict bounds on $p$.

Because $\phi'=p>0$, the feature coordinate is strictly increasing. For $a<b$,

\[
p(b)-p(a)
=\int_a^b \phi''(u)\,du
=\int_a^b r(u)\phi'(u)\,du
\le R\bigl(\phi(b)-\phi(a)\bigr).
\]

Reversing the endpoints proves

\[
|p(a)-p(b)|\le R|\phi(a)-\phi(b)|.
\]

This verifies the comparison without requiring a differentiability theorem for the inverse feature map. Equality for separated finite endpoints is not needed.

## 3. Exact sector calculation, signs, and the correction coefficient

At a time with $w\ne0$, use the source's convention $q=|w|$, with $z_+$ the first sample for $w>0$ and the second for $w<0$. Substitution into both equations in (1) gives, in either case,

\[
\beta=\frac{q\phi''(z_+)}2,
\qquad
z_+'=\frac q2(gp_+-hp_-)+\ell_+.
\]

In the negative sector there is no sign change on $\ell_+$: it is exactly $\ell_2$. Also,

\[
wF=\frac q2\bigl(\phi(z_+)-\phi(z_-)\bigr).
\]

This last identity establishes precisely which ordering of the selected features is unaligned. It implies that $wF<0$ exactly when $z_+<z_-$, and $wF=0$, with $w\ne0$, exactly when the two feature coordinates coincide.

Set $U_a=\log p(z_a)$. The selected derivative is

\[
U_+'=r_+z_+'
=\left(g-h\frac{p_-}{p_+}\right)\beta+r_+\ell_+
=c\beta+E_h+r_+\ell_+,
\]

where the exact surplus is

\[
E_h=
\begin{cases}
-h\,\dfrac{p_-}{p_+}\,\beta,&h\le0,\\[5pt]
h\,\dfrac{p_+-p_-}{p_+}\,\beta,&h>0.
\end{cases}
\]

For $h\le0$, the surplus is nonnegative irrespective of alignment. For $h>0$, it is nonnegative when $wF\ge0$. On the only adverse sector, $h>0$ and $wF<0$,

\[
\begin{aligned}
-E_h
&=h\frac{\beta}{p_+}|p_+-p_-|\\
&=h\frac{q r_+}{2}|p_+-p_-|\\
&\le h\frac{qR}{2}\bigl(2R|F|\bigr)\\
&=hR^2|wF|.
\end{aligned}
\]

The factor $2$ from the definition of $F$ cancels the $1/2$ in $\beta/p_+$. There is neither a missing factor $2$ nor an extra factor $1/2$. Thus a slightly more precise pointwise estimate is

\[
U_+'\ge c\beta-h_+R^2(-wF)_+-R|\ell_+|.
\]

Using $h_+\le H$ and $|\ell_+|\le|\ell_1|+|\ell_2|$ gives exactly (4).

The constant $R^2$ is sharp for this particular pointwise surplus bound. To see this, choose $w>0$, constant $g>h>0$, $z_1=z_*$, and $z_2=z_*+\delta$ with $\delta>0$. At that state,

\[
\frac{-E_h}{h|wF|}
=r(z_*)\frac{p(z_*+\delta)-p(z_*)}
{\phi(z_*+\delta)-\phi(z_*)}
\longrightarrow R^2
\quad(\delta\downarrow0).
\]

These are admissible local states of the smooth constant-Gram system, including with zero forcing. This sharpness statement concerns the local comparison; it does not assert optimality of every constant in the integrated inequality.

Finally, the interpretation of the correction as backward motion is exact:

\[
(w^2)'=2wF,
\qquad
(-wF)_+=\frac12[-(w^2)']_+.
\]

It measures the decreasing variation of $w^2$, including every excursion, without counting excursions.

## 4. Smoothing, arbitrary zero sets, and the forcing remainder

For each $\varepsilon>0$, choose a nonnegative even smooth density $\rho_\varepsilon$ of total integral one supported inside $[-\varepsilon,\varepsilon]$, and define

\[
\sigma_\varepsilon(x)=2\int_{-\infty}^x\rho_\varepsilon(u)\,du-1,
\qquad
a_\varepsilon=\frac{1+\sigma_\varepsilon(w)}2.
\]

Then $\sigma_\varepsilon$ is smooth, nondecreasing, lies in $[-1,1]$, equals the sign away from the transition interval, and has $\sigma_\varepsilon(0)=0$. The note's smoothed gate is

\[
L_\varepsilon=a_\varepsilon U_1+(1-a_\varepsilon)U_2,
\qquad 0<L_\varepsilon<\log2.
\]

Its exact derivative is

\[
L_\varepsilon'
=a_\varepsilon U_1'+(1-a_\varepsilon)U_2'
+\frac{\sigma_\varepsilon'(w)}2F(U_1-U_2).
\]

Both $\phi$ and $\log p$ are strictly increasing. Therefore

\[
F(U_1-U_2)
=\frac12\bigl(\phi(z_1)-\phi(z_2)\bigr)
\bigl(\log p(z_1)-\log p(z_2)\bigr)\ge0.
\]

Since $\sigma_\varepsilon'\ge0$, the extra derivative term is nonnegative. This is the correct sign. There is no need to bound its magnitude uniformly as $\varepsilon\to0$: it is discarded with its favorable sign for each fixed $\varepsilon$.

Here is an explicit version of the remainder argument, including arbitrary forcing. Define

\[
M=\max_{[0,S]}(|g|+|h|)<\infty.
\]

The two gate derivatives decompose as

\[
\begin{aligned}
U_1'&=D_1+r_1\ell_1,
&D_1&=\frac w2r_1(gp_1-hp_2),\\
U_2'&=D_2+r_2\ell_2,
&D_2&=\frac w2r_2(hp_1-gp_2).
\end{aligned}
\]

The fixed gate bounds imply

\[
|D_1|,|D_2|\le MR|w|,
\qquad
0\le c\beta\le\frac{M|w|}{8}.
\]

The forcing part of the convex combination satisfies, everywhere,

\[
a_\varepsilon r_1\ell_1+(1-a_\varepsilon)r_2\ell_2
\ge-R\bigl(a_\varepsilon|\ell_1|+(1-a_\varepsilon)|\ell_2|\bigr)
\ge-R(|\ell_1|+|\ell_2|).
\]

Consequently, on $|w|<\varepsilon$,

\[
\begin{aligned}
L_\varepsilon'
&\ge-MR\varepsilon-R(|\ell_1|+|\ell_2|)\\
&\ge c\beta-HR^2(-wF)_+-R(|\ell_1|+|\ell_2|)
-M\left(R+\frac18\right)\varepsilon.
\end{aligned}
\]

The second line uses $c\beta\le M\varepsilon/8$ and $HR^2(-wF)_+\ge0$. It does not require $F$, $\ell$, or the measure of $\{|w|<\varepsilon\}$ to become small. In particular, arbitrary forcing must retain its full $L^1$ cost; the source does retain it. It would be incorrect to include that forcing in an $O(\varepsilon)$ drift remainder, but the source does not make that error.

For $|w|\ge\varepsilon$, the convex combination selects exactly the sector gate, and (4) applies. Thus on all of $[0,S]$ one may take the explicit source constant

\[
C_G=M\left(R+\frac18\right)
\]

and obtain

\[
L_\varepsilon'
\ge c\beta-HR^2(-wF)_+-R(|\ell_1|+|\ell_2|)-C_G\varepsilon.
\]

After integration and rearrangement,

\[
\int_0^S c\beta\,ds
\le L_\varepsilon(S)-L_\varepsilon(0)
+HR^2\int_0^S(-wF)_+\,ds
+R\int_0^S(|\ell_1|+|\ell_2|)\,ds
+C_G\varepsilon S.
\]

Using the endpoint range bounds the first difference by $\log2$. Letting $\varepsilon\downarrow0$ proves (2). This limit involves only the numerical error $C_G\varepsilon S$; there is no passage of a derivative through a limit and no need to prove convergence of the favorable smoothing term.

This also proves the statement on every subinterval. One can retain the global $H,M$, or replace them by their maxima on that subinterval. A nonzero initial readout causes no difficulty for this scalar proof.

## 5. Adversarial edge cases

### Readout sign changes and crossing direction

At a transverse crossing $w(t_0)=0$, $F(t_0)=w'(t_0)\ne0$. An upward crossing switches from $U_2$ to $U_1$, and its jump is $U_1-U_2>0$. A downward crossing switches from $U_1$ to $U_2$, and its jump is $U_2-U_1>0$. At a crossing with $F(t_0)=0$, strict monotonicity gives $z_1(t_0)=z_2(t_0)$, hence the two gate values agree. These observations verify the intuitive sign of isolated jumps, but the smoothing proof, rather than a sum of such jumps, handles a general zero set.

Infinitely many crossings are realizable under the stated hypotheses. For example, on $[0,1]$, let

\[
w(s)=s^5\sin(1/s)\quad(s>0),\qquad w(0)=0.
\]

This function is $C^2$, with $w'(0)=w''(0)=0$, since for $s>0$

\[
w'=5s^4\sin(1/s)-s^3\cos(1/s),
\qquad
w''=20s^3\sin(1/s)-8s^2\cos(1/s)-s\sin(1/s).
\]

The activation maps $\mathbb R$ onto $\mathbb R$: its limits are $-\infty$ and $+\infty$, and its derivative is positive. Therefore set

\[
z_2=0,
\qquad z_1=\phi^{-1}\bigl(\phi(0)+2w'\bigr).
\]

Then $z_1\in C^1$ and $F=w'$. Take $g=2$, $h(s)=\sin(2\pi s)$, and define $\ell_1,\ell_2$ by subtracting the displayed drift in (1) from the prescribed $z_1',z_2'$. These forcings are continuous, $g>|h|$ holds, and $w$ changes sign infinitely often near zero. The proof in Section 4 applies directly. This is an analytic stress test, not an assumption that crossings can be enumerated in the proof.

### An identically zero readout, and intervals of zeros

If $w\equiv0$, its equation forces $F\equiv0$, hence $z_1=z_2$. The other equations then require $\ell_1=\ell_2=z_1'$. Thus $\beta\equiv0$, the backward-motion cost is zero, and (2) holds. One cannot simultaneously prescribe $w\equiv0$ and unequal forcing while claiming to satisfy (1). “Arbitrary forcing” means any continuous forcing together with a solution of the system, not incompatible prescriptions of both a path and its forcing.

The same compatibility applies on any interval on which $w=0$. The zero set can have positive measure; its size is irrelevant to the uniform $C_G\varepsilon S$ bound.

### Negative off-diagonal Gram entries

When $h<0$, the source correctly uses $c=g$, not $g-|h|$. The exact surplus is then positive. If $h\le0$ throughout the interval, $H=0$, and the unaligned-excursion cost disappears even if $wF<0$. Negative $h$ makes the selected drift more favorable. This does not conflict with the smaller minimum eigenvalue of the Gram: the estimate uses the specific signed two-sample equations.

### A nonconstant Gram, including sign changes of $h$

No step differentiates $g,h,c$, or $H$. Continuous variation, rapid oscillation, and crossings of $h=0$ are all permitted. The weight $c=g-h_+$ can fail to be differentiable at such crossings without affecting the proof. Continuity on the finite interval supplies the finite maxima used above. The equal diagonal entries and the specified signed equations remain substantive hypotheses.

### Input-dependent or neuron-dependent weights

For each fixed input pair, (2) uses that pair's actual $c(s)$ and $H$. Input dependence itself is harmless. However, these quantities cannot be replaced by constants uniform over inputs without establishing such uniformity.

For one fixed continuous Gram on a compact interval, strict positivity already implies $\min_{[0,S]}c>0$. This minimum can depend on the trajectory and the inputs and can tend to zero across a family. In a population with neuron-dependent Grams, positivity for every neuron also need not give a common positive lower bound. For example, the admissible coefficients $g=\eta>0,h=0$ have $c=\eta$, with no lower bound uniform over $\eta\downarrow0$.

Accordingly the weighted estimate cannot be turned into a uniform unweighted estimate merely by citing strict positivity. At the level of integrals the obstruction is elementary: a quantity $\beta=1/c$ has $c\beta=1$ while $\beta$ can be arbitrarily large. This illustrates why the implication needs a uniform lower bound; it is not presented as a counterexample trajectory to (2).

### Zero time and zero backward motion

For $S=0$, all time integrals vanish, and both (2) and (7) reduce to $0\le\log2$. The maxima defining $H$ and $c$ are evaluated at the sole time. The action consequences have zero left sides; no division by $S$ is required.

When $wF=0$, the correction vanishes continuously. At $w\ne0$ this means $z_1=z_2$, so the $h>0$ surplus is exactly zero. At $w=0$, $\beta=0$, and the smoothing argument supplies the estimate. No convention concerning $\operatorname{sign}(0)$ enters (2).

## 6. Reconstruction of the averaged action consequence

Let $(\Omega,\mu)$ be the neuron probability space. All expectations below are over this space, not automatically over input pairs or random entire trajectories. Write

\[
\mathcal J(\theta)
=\mathbb E\bigl[W^{(4)}(H^{(3)}_1-H^{(3)}_2)/2\bigr].
\]

### The precise action assumption

A sufficient Hilbert setting is an existing absolutely continuous raw-parameter curve, a valid chain rule for $\mathcal J$ along it, and

\[
\theta'=\nabla_{\rm raw}\mathcal J\quad\text{a.e.},
\qquad w(0,\omega)=0\quad\mu\text{-a.e.}
\]

The raw norm must contain the readout $L^2(\mu)$ block with the normalization used in $F=w'$. For example, continuous Fréchet differentiability of $\mathcal J$ on a neighborhood of the curve is a sufficient chain-rule hypothesis. Under these assumptions,

\[
\frac{d}{ds}\mathcal J(\theta(s))
=\langle\nabla_{\rm raw}\mathcal J,\theta'\rangle_{\rm raw}
=\|\theta'\|_{\rm raw}^2.
\]

The zero readout gives $\mathcal J(0)=0$. Therefore, for

\[
A=\int_0^S\|\theta'\|_{\rm raw}^2\,ds,
\qquad
A_w=\mathbb E\int_0^SF^2\,ds,
\]

the note's premise $\mathcal J(S)\le1$ yields

\[
0\le A_w\le A=\mathcal J(S)\le1.
\]

“Zero readout” must mean zero almost surely, not merely zero mean. Also, an arbitrary change of time, a clipped evolution, or a gradient computed using another norm would require a new action calculation. The note explicitly specifies the raw uncut gradient evolution, so no such replacement is justified or needed.

The same action bound gives, for every $s\le S$,

\[
\|\theta(s)-\theta(0)\|_{\rm raw}
\le\int_0^s\|\theta'\|_{\rm raw}\,du
\le\sqrt{s}\left(\int_0^s\|\theta'\|_{\rm raw}^2\,du\right)^{1/2}
\le\sqrt S.
\]

Thus the stated ball is centered at the initial parameter, and its radius controls the displacement. Bounds on parameter norms also use the initial norms.

### Readout second moment and backward-motion cost

For almost every neuron, $w(s)=\int_0^sF(u)\,du$, so Cauchy–Schwarz gives

\[
w(s)^2\le s\int_0^sF(u)^2\,du.
\]

The integrands are nonnegative and measurable. Tonelli's theorem therefore allows interchange of their time and neuron integrals even before finiteness is established. Integrating first in $s$ gives

\[
\begin{aligned}
\mathbb E\int_0^Sw(s)^2\,ds
&\le\mathbb E\int_0^S\left(\int_u^Ss\,ds\right)F(u)^2\,du\\
&=\frac12\mathbb E\int_0^S(S^2-u^2)F(u)^2\,du\\
&\le\frac{S^2}{2}A_w.
\end{aligned}
\]

Both functions are consequently in $L^2([0,S]\times\Omega)$. Cauchy–Schwarz on that product measure gives

\[
\mathbb E\int_0^S(-wF)_+\,ds
\le\left(\mathbb E\int_0^Sw^2\,ds\right)^{1/2}
\left(\mathbb E\int_0^SF^2\,ds\right)^{1/2}
\le\frac S{\sqrt2}A_w
\le\frac S{\sqrt2}.
\]

This proves (6), with its stated constant. The argument does not require a separate action bound for each neuron or any independence assumption.

### What is needed for the actual forcing estimate

The relation $\ell_a=W^{(3)}(H^{(2)}_a)'$ follows from differentiating an actual top preactivation $z_a=W^{(3)}H^{(2)}_a$ and separating the $W^{(3)\prime}H^{(2)}_a$ drift. To verify its magnitude from action, a sufficient precise version of the note's forward-map assertion is the following. Let $\mathcal H_2$ be the lower feature Hilbert space and require, along the existing curve,

\[
W^{(3)}(s):\mathcal H_2\longrightarrow L^2(\mu),
\qquad \|W^{(3)}(s)\|_{\rm op}\le B_S,
\]

and absolute continuity of the two lower features with

\[
\sum_{a=1}^2\|(H^{(2)}_a)'(s)\|_{\mathcal H_2}^2
\le K_S^2\|\theta'(s)\|_{\rm raw}^2
\quad\text{a.e.}
\]

Here $B_S,K_S$ are finite bounds on the initial-centered raw ball, with allowed dependence on the fixed inputs, architecture, and initial norms. Then the complete forcing calculation is

\[
\begin{aligned}
\mathbb E\int_0^S\sum_{a=1}^2|\ell_a|^2\,ds
&=\int_0^S\sum_{a=1}^2
\|W^{(3)}(H^{(2)}_a)'\|_{L^2(\mu)}^2\,ds\\
&\le B_S^2K_S^2\int_0^S\|\theta'\|_{\rm raw}^2\,ds\\
&\le B_S^2K_S^2.
\end{aligned}
\]

Thus $C_S=B_SK_S$ suffices. These are operator bounds, not bounds on every individual neuron's weight or action. For an $L^2$ kernel, the inequality $\|W\|_{\rm op}\le\|W\|_{L^2}$ follows by applying Cauchy–Schwarz to each row and then integrating the row estimate, so raw kernel control is a sufficient way to obtain $B_S$.

The source's references to bounded activation derivative and differentiated forward equations are consistent with obtaining $K_S$ in a usual fixed finite-depth Hilbert feature model. For example, at an operator/activation layer $H=\phi(VX)$, the relevant estimates are

\[
\|H\|_2\le 2\|V\|_{\rm op}\|X\|_2+(\log2)\|1\|_2,
\qquad
\|H'\|_2\le2\bigl(\|V'\|_{\rm op}\|X\|_2+\|V\|_{\rm op}\|X'\|_2\bigr).
\]

They propagate bounds through finitely many specified layers if the raw norm controls the operator blocks and the along-curve derivative formula is valid. On a probability space $\|1\|_2=1$. This explains how to fill in the intended argument; it is not a claim that the missing parameter spaces and lower architecture were supplied in the note. The scalar forced system and action alone do not specify this structure.

Once the $L^2$ forcing bound is available, Cauchy–Schwarz on time, neuron probability, and the two-point sample index gives

\[
\mathbb E\int_0^S(|\ell_1|+|\ell_2|)\,ds
\le\sqrt{2S}
\left(\mathbb E\int_0^S(|\ell_1|^2+|\ell_2|^2)\,ds\right)^{1/2}
\le\sqrt{2S}\,C_S.
\]

The factor $\sqrt{2S}$ is correct.

### Averaging the Gram term correctly

If the Gram is common to all third-layer neurons, its $H$ is a common number for the fixed trajectory. Averaging (2) and applying the two bounds just proved gives

\[
\mathbb E\int_0^Sc(s)\beta(s)\,ds
\le\log2+HR^2\frac S{\sqrt2}+R\sqrt{2S}\,C_S,
\]

which is exactly (7). In the conventional top-layer realization, common Gram entries come from inner products of the same two lower feature vectors, and exchange symmetry supplies their equal diagonal norms. For the isolated statement, the common-Gram interpretation should be explicit.

More generally, if the forced system is applied separately to neuron-dependent Grams, the direct conclusion is

\[
\mathbb E\int_0^Sc_\omega\beta_\omega\,ds
\le\log2+R^2\mathbb E[H_\omega B_\omega]
+R\mathbb E\int_0^S(|\ell_1|+|\ell_2|)\,ds,
\qquad
B_\omega=\int_0^S(-wF)_+\,ds.
\]

A uniform almost-sure upper bound $H_\omega\le\overline H$ recovers (7) with $\overline H$. An average bound on $H_\omega$ alone does not justify pulling $H$ outside the expectation. Indeed, nonnegative random variables $H=B=\varepsilon^{-1}\mathbf1_E$, with $\mu(E)=\varepsilon$, have $\mathbb EH=\mathbb EB=1$ but $\mathbb E(HB)=\varepsilon^{-1}$. This is a counterexample to the potential moment-factorization step, not to (7) under a common Gram.

Similarly, obtaining the source's unweighted conclusion by dividing (7) requires a common lower bound $c\ge c_*>0$ over the time and neuron variables being averaged. Then nonnegativity gives

\[
c_*\,\mathbb E\int_0^S\beta\,ds
\le\mathbb E\int_0^Sc\beta\,ds.
\]

For precision, this lower bound on $c$ is needed for that particular division, not for every possible unweighted estimate under action. The gate bound gives $\beta\le |w|/8$, so the already established readout moment estimate also yields the separate coarse bound

\[
\mathbb E\int_0^S\beta\,ds
\le\frac18\mathbb E\int_0^S|w|\,ds
\le\frac{\sqrt S}{8}
\left(\mathbb E\int_0^Sw^2\,ds\right)^{1/2}
\le\frac{S^{3/2}}{8\sqrt2},
\]

where the middle step uses the product measure of total mass $S$ and the final step uses $A_w\le1$. This does not replace the signed weighted estimate or its subinterval information. It prevents overstating the necessity of a Gram lower bound for coarse unweighted first-moment control in the conditional action setting.

If one also averages over inputs, uniform bounds or suitable joint moment estimates for the input-dependent $H,C_S,c_*$ are additional hypotheses. The fixed-input assertion does not supply them.

For a finite population with normalized empirical averages, the same measure-theoretic calculation applies. The action identity must use the matching empirical raw metric, and the exact equal-diagonal positive Gram remains a premise. No pathwise symmetry of a Gaussian finite system or convergence to an infinite population follows from this calculation.

## 7. Required repairs and limits of certification

1. **Scalar theorem:** none. The reconstruction above supplies an explicit $C_G=M(R+1/8)$ and fully justifies the arbitrary-zero-set argument. Adding that constant to the candidate would improve auditability but does not change its statement or cure a false inference.

2. **Section 4 as a standalone mathematical corollary:** specify the raw Hilbert space/norm and its readout normalization; state sufficient regularity for the chain rule and lower forward differentiation; and either assume or derive the displayed $B_S,K_S$ bounds in the intended architecture. The source asserts these bounds in prose but does not give the lower model needed to check their hypotheses in isolation. This is a missing analytic specification, not a counterexample to the scalar lemma. Under those precise hypotheses the forcing estimate and (7) are proved above.

3. **Uniformity of the averaged constants:** say that $H$ is common to the neuron population, or replace it by a uniform essential upper bound. Specify that any $c_*$ used to remove the weight is uniform over the variables in the expectation. Allow dependence on the fixed inputs in $C_S$ unless input normalization or a uniform input class has been stated. These qualifications prevent unsupported extensions of the corollary.

4. **Notation only:** use a distinct symbol for the population objective and for the diagonal Gram coefficient. In particular, the premise $g(S)\le1$ in Section 4 concerns the objective, not the diagonal Gram entry.

The audit found no counterexample to (2) with the stated equations and hypotheses. Its use of the actual signs, the positive smoothing contribution, and the retained forcing cost resolves the potential zero-crossing obstruction. The averaged bound has the honest strength of a first-moment estimate along an already existing sufficiently regular gradient trajectory, subject to the analytic and uniformity conditions above. It does not furnish a response exponential, population existence or uniqueness, a regularization limit, or a finite-to-population comparison. Those are expressly excluded by the source and are not missing conclusions of the lemma.

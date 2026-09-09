# Isolated adversarial review: all-angle first-layer action

Sole mathematical input: `/tmp/l2-two-sample-proof-0ywjpp/ALL_ANGLE_FIRST_LAYER_ACTION.md`, read completely (266 lines).

Verified input SHA256:

`73117a5c94b38fc949fc2a3662245e3202cf45a42c831fbdd969236ba19894ed`

Scope: the stated finite-width gradient flow, its first-layer moment estimates, and the initialization/UI/compactness consequences. No other project material, contracts, sources, reviews, or history were consulted. The rigorous-math skill was read for procedure only. No experiments, agents, external heavy theorems, or source edits were used. Line references below refer to the supplied source.

## Verdict and corrections

**PASS for the deterministic finite-GF theorem (2)–(4), with all its displayed constants. PASS for Gaussian transfer uniformly in the deterministic input pair, and for the stated UI and path compactness consequences when their uniform initial-moment condition is retained.** There is no missing reverse-field moment, no Gram-invertibility requirement, and no missing regularity hypothesis for these finite-dimensional arguments.

**One required quantifier clarification:** lines 227–229 say “simultaneously for all fixed input angles.” The proof establishes a probability estimate uniform over deterministic normalized input pairs. This does not, by itself, establish one event on which a deterministic fourth-moment bound holds for every normalized input pair in the same realization. That stronger interpretation is false when dimension can grow. Replace the ambiguous phrase with the precise uniform-in-probability statement in Section 5 below, or explicitly specify a restricted family of inputs and prove a simultaneous statement for that family. This is a correction to the probabilistic wording, not to the finite-GF estimates.

**No other required correction under the section's Gaussian-initialization scope.** Two optional clarifications would improve the statement:

- State explicitly the sufficient initial-moment condition used here for deterministic-family path UI and quadratic-Wasserstein compactness: a uniform bound on the initial empirical fourth moment, as provided by the preceding Gaussian events. For random empirical measures, describe the conclusion as containment in a fixed relatively compact set with probability tending to one; the displayed probability estimates alone are not an almost-sure assertion across all widths.
- At lines 32–33, restrict “coordinatewise” to the vector products defining the two deltas. The product defining $q^{(1)}$ is ordinary matrix–vector multiplication, as the rest of the proof correctly uses.

These conclusions concern finite GF only. They do not establish population existence, population identification or uniqueness, or a GD/GF comparison.

## 1. Actual GF and global finite existence

Take $n,d\geq1$ to be finite integers and all initial weights to have finite real entries. Write $w=W^{(3)}$. Directly from the forward map,

\[
\nabla_{W^{(1)}}L=\frac2n\sum_a r_a\delta^{(1)}_a x_a^T,
\qquad
\nabla_{W^{(2)}}L=\frac2n\sum_a r_a\delta^{(2)}_a(h^{(1)}_a)^T,
\qquad
\nabla_wL=\frac2n\sum_a r_a h^{(2)}_a.
\]

Thus (1) is precisely GF with learning-rate factors $n/d,1,n$, respectively. Substitution into the chain rule gives

\[
\dot L=-\frac dn\|\dot W^{(1)}\|_F^2
        -\|\dot W^{(2)}\|_F^2
        -\frac1n\|\dot w\|^2.
\]

Every factor in (5) is correct. This is a weighted Euclidean GF, and the weights are positive for every finite $n,d$.

The assumed $C^2$ activations make the finite-dimensional vector field $C^1$: differentiating its occurrences of $\phi$ or $\phi'$ requires at most $\phi''$. All such derivatives are continuous on finite-dimensional compact sets. Hence the local contraction argument applies.

For completeness, if a maximal solution had a finite terminal time $t_*$, define the norm

\[
\|\Delta W\|_g^2=\frac dn\|\Delta W^{(1)}\|_F^2
                  +\|\Delta W^{(2)}\|_F^2
                  +\frac1n\|\Delta w\|^2.
\]

For $0\leq s<t<t_*$, energy dissipation and Cauchy–Schwarz give

\[
\|W(t)-W(s)\|_g
\leq\sqrt{(t-s)\int_s^t\|\dot W(u)\|_g^2\,du}
\leq\sqrt{(t-s)L(0)}.
\]

The trajectory stays in a finite-dimensional bounded ball and is Cauchy as $t\uparrow t_*$. Its endpoint is a finite state, where the same local existence argument extends the solution. This excludes finite-time breakdown. No uniform-in-width coercivity is needed for this finite-width conclusion, and no bound on $W^{(1)}(0)$ beyond its being a finite matrix is used.

## 2. Audit of the derivative and control constants

All norms in this section have the meanings specified by the source. In particular, a normalized vector bound means its Euclidean norm divided by \(\sqrt n\), not a coordinatewise bound.

At initialization, \(|f_a(0)|\leq B_2b\), so

\[
\|r(0)\|\leq\sqrt2(B_2b+1)=R_0,
\qquad \sum_a|c_a(t)|=2\|r(t)\|_1\leq2\sqrt2R_0=K_c.
\]

The loss identity justifies the residual bound at all times. The readout equation gives the coordinatewise bound

\[
\|w(t)\|_\infty\leq b+B_2K_ct\leq M.
\]

The factor $1/n$ in the second-layer update cancels its two factors of \(\sqrt n\):

\[
\|\dot W^{(2)}(t)\|_{\rm op}
\leq\frac1n\sum_a|c_a|\|\delta^{(2)}_a\|\|h^{(1)}_a\|
\leq B_1P_2K_c(b+B_2K_ct).
\]

Integration gives exactly

\[
A=a+B_1P_2\left(bK_cT+\frac12B_2K_c^2T^2\right).
\]

Consequently \(\|\delta^{(2)}_a\|/\sqrt n\leq P_2M\) and \(\|q^{(1)}_a\|/\sqrt n\leq AP_2M=Q\). Also

\[
\dot z^{(1)}_a=\sum_b C_{ab}c_b\delta^{(1)}_b,
\qquad |C_{ab}|\leq1,
\]

so \(\|\dot z^{(1)}_a\|/\sqrt n\leq K_cP_1Q\), exactly (6). Correlation does not introduce an extra factor of two in this samplewise bound.

The constants in lines 101–104 have the following verified roles:

| Constant | Bound it provides |
| --- | --- |
| \(D_A=K_cP_2MB_1\) | \(\|\dot W^{(2)}\|_{\rm op}\leq D_A\) |
| \(D_w=K_cB_2\) | \(\|\dot w\|_\infty\leq D_w\) |
| \(D_Z=D_AB_1+AK_cP_1^2Q\) | \(\|\dot z^{(2)}_a\|/\sqrt n\leq D_Z\) |
| \(D_\delta=D_wP_2+ML_2D_Z\) | \(\|\dot\delta^{(2)}_a\|/\sqrt n\leq D_\delta\) |
| \(Q_1=D_AP_2M+AD_\delta\) | \(\|\dot q^{(1)}_a\|/\sqrt n\leq Q_1\) |

Indeed,

\[
\frac{\|\dot h^{(1)}_a\|}{\sqrt n}\leq K_cP_1^2Q,
\quad
\dot z^{(2)}_a=\dot W^{(2)}h^{(1)}_a+W^{(2)}\dot h^{(1)}_a,
\]

and, with \(\odot\) denoting coordinatewise multiplication,

\[
\dot\delta^{(2)}_a
=\dot w\odot\phi_2'(z^{(2)}_a)
 +w\odot\phi_2''(z^{(2)}_a)\odot\dot z^{(2)}_a.
\]

The second term is bounded in normalized $L^2$ because **$w$ is bounded coordinatewise**. It would not follow merely from an $L^2$ bound on $w$, but the needed stronger bound was proved. Finally,

\[
\dot q^{(1)}_a=(\dot W^{(2)})^T\delta^{(2)}_a
                  +(W^{(2)})^T\dot\delta^{(2)}_a
\]

uses only spectral matrix bounds and the preceding vector bounds. It never differentiates \(\delta^{(1)}\), so it introduces no uncontrolled product \(q^{(1)}\odot\dot z^{(1)}\). No fourth moment of $q^{(1)}$, independence along the flow, or third derivative of an activation is being assumed. The bound $L_1$ is not needed in the numerical constants; its regularity role in the local vector field is sufficient.

Differentiating $f_a$ along (1) yields exactly the three kernel terms in lines 127–129. For the first term, \(|C_{ab}|\leq1\) and \(\|\delta^{(1)}_a\|/\sqrt n\leq P_1Q\). For the second and third terms, apply Cauchy–Schwarz separately to the normalized inner products. This gives

\[
|K_{ab}|\leq P_1^2Q^2+P_2^2M^2B_1^2+B_2^2=K_*.
\]

For a $2\times2$ matrix, \(\|K\|_{\rm op}\leq\|K\|_F\leq2K_*\). Thus

\[
\dot r=-2Kr,
\quad \|\dot r\|\leq4K_*R_0,
\quad \sum_a|\dot c_a|\leq2\sqrt2\|\dot r\|
                         \leq8\sqrt2K_*R_0=K'_c.
\]

The factors in (7) are correct, including both factors of two from $c=-2r$ and \(\dot r=-2Kr\).

For the envelope $U_i$, the triangle inequality in the normalized Euclidean norm gives

\[
\begin{aligned}
\left(\frac1n\sum_iU_i^2\right)^{1/2}
&\leq\sum_a|c_a(0)|\frac{\|q_a(0)\|}{\sqrt n}
 +\int_0^T\sum_a\left(
 |\dot c_a|\frac{\|q_a\|}{\sqrt n}
 +|c_a|\frac{\|\dot q_a\|}{\sqrt n}\right)dt\\
&\leq K_cQ+T(K'_cQ+K_cQ_1)=V_T.
\end{aligned}
\]

Here $q_a=q^{(1)}_a$. Each component is continuously differentiable on a finite interval, so all variations and integrations by parts below are legitimate. Dependence between neurons is irrelevant to this deterministic estimate.

## 3. Work identity, nonorthogonal inputs, and singular cases

For one row let $p_a=v_{a,i}\phi_1'(z^{(1)}_{a,i})$, and put $p=(p_1,p_2)^T$. This avoids confusing the source's vector $d_i$ with input dimension $d$. Direct substitution gives

\[
\dot w_i=\frac1d\sum_a p_a x_a^T,
\qquad \dot z_i=Cp,
\qquad d\|\dot w_i\|^2=p^TCp.
\]

Also

\[
\sum_a v_{a,i}\dot h^{(1)}_{a,i}
=\sum_a p_a(Cp)_a=p^TCp.
\]

This verifies (9) pointwise, including its sign. With
\(C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\), its eigenvalues are $1+\rho,1-\rho$, both in $[0,2]$. At \(\rho=1\), the work is \((p_1+p_2)^2\); at \(\rho=-1\), it is \((p_1-p_2)^2\). Null directions simply produce zero row velocity. There is no division by $1-\rho^2$, no positivity assumption on the controls, and no requirement that the activation be monotone or odd.

Write \(S(t)=\sum_a|v_{a,i}(t)|\) and \(J=\int_0^T\sum_a|\dot v_{a,i}|\). Then $U_i=S(0)+J$ and $S(T)\leq S(0)+J$. Integration by parts gives

\[
0\leq E_i
=\left[\sum_a v_{a,i}h^{(1)}_{a,i}\right]_0^T
 -\int_0^T\sum_a\dot v_{a,i}h^{(1)}_{a,i}\,dt
\leq B_1(S(T)+S(0)+J)\leq2B_1U_i.
\]

Thus the linear, rather than quadratic, envelope bound in (10) is valid. Its essential assumptions are bounded activation values and the proved time variation of the actual controls.

## 4. Fourth path and cubic velocity constants

The elementary spectral inequality $C^2\preceq2C$ gives

\[
|\dot z_i|^2=p^TC^2p\leq2p^TCp=2d\|\dot w_i\|^2.
\]

Also \(|\dot z_i|\leq2|p|\leq2P_1U_i\). Hence

\[
\int_0^T|\dot z_i|^2\leq2E_i\leq4B_1U_i,
\qquad
\int_0^T|\dot z_i|^3
\leq(2P_1U_i)(4B_1U_i)=8B_1P_1U_i^2.
\]

Averaging and (8) prove (3). The componentwise chain rule gives \(|\dot h_i|\leq P_1|\dot z_i|\); cubing multiplies the preceding constant by $P_1^3$. Thus the power $P_1^4$ and the factor $8$ in (4) are correct.

For paths,

\[
\sup_{t\leq T}|z_i(t)|\leq|z_i(0)|+\sqrt{2TE_i}.
\]

Using \((a+b)^4\leq8(a^4+b^4)\) and $E_i\leq2B_1U_i$,

\[
\begin{aligned}
\sup_{t\leq T}|z_i(t)|^4
&\leq8|z_i(0)|^4+8(2TE_i)^2\\
&=8|z_i(0)|^4+32T^2E_i^2\\
&\leq8|z_i(0)|^4+128B_1^2T^2U_i^2.
\end{aligned}
\]

This verifies (2), including $8,128,T^2,V_T^2$. No maximum of the initial first-layer coordinates is used. A uniform initial fourth moment is needed only when turning its explicit right-hand side into a uniform numerical fourth-path-moment bound.

The unnumbered row-velocity assertion at lines 203–204 is also valid. In fact,

\[
\sqrt d\|\dot w_i\|
=\left\|\sum_a p_a\frac{x_a}{\sqrt d}\right\|
\leq\sum_a|p_a|\leq P_1U_i,
\]

so \(n^{-1}\sum_i\int_0^T(\sqrt d\|\dot w_i\|)^3\,dt\leq2B_1P_1V_T^2\). No such additional estimate is required for (2)–(4).

The degenerate cases $T=0$, $B_1=0$, or $P_1=0$ cause no contradiction. In particular, a zero bound on $\phi_1$ or on $\phi_1'$ makes the first-layer velocity zero. The constants are valid upper bounds; sharpness is not claimed.

## 5. Gaussian initialization and the quantifier issue

The inputs must be fixed independently of the Gaussian first-layer initialization for the stated Gaussian distribution calculation. That is the conventional meaning of “Fix $x_1,x_2$” in line 21. Arbitrary dependence of the trained variables during GF does not affect this initialization calculation.

For one initial row the pair $(Z_1,Z_2)$ has covariance $C$. Using independent standard normals $G,H$, represent it as

\[
(Z_1,Z_2)=(G,\rho G+\sqrt{1-\rho^2}H).
\]

This representation is valid also at the endpoints. It gives
\(\mathbb E Z_1^2Z_2^2=1+2\rho^2\), and hence

\[
\mathbb E|Z|^4=3+3+2(1+2\rho^2)=8+4\rho^2\leq12.
\]

The Chebyshev argument can be made uniform in both dimension and angle. Since each marginal is standard normal,

\[
\mathbb E|Z|^8
=\mathbb E(Z_1^2+Z_2^2)^4
\leq8\mathbb E(Z_1^8+Z_2^8)=1680.
\]

Here \(\mathbb EG^8=7\cdot5\cdot3\cdot1=105\), obtained by repeated integration by parts against the Gaussian density. Independent rows therefore imply

\[
\Pr\left\{\frac1n\sum_i|z_i(0)|^4>13\right\}\leq\frac{1680}{n}.
\]

The bound is allowed to exceed one for small $n$. It is uniform over every deterministic normalized input pair, including sequences with varying $d$ and \(\rho\).

The spectral-net proof and all its numerical constants are correct. A maximal $1/4$-separated subset of the unit sphere is a $1/4$-net. Its disjoint radius-$1/8$ balls lie inside the radius-$9/8$ ball, giving cardinality at most $9^n$. Approximating each of two unit vectors loses at most \(\frac12\|W^{(2)}_0\|_{\rm op}\), so

\[
\|W^{(2)}_0\|_{\rm op}\leq2\max_{u,v\text{ in net}}|u^TW^{(2)}_0v|.
\]

Each fixed bilinear form is centered Gaussian of variance $1/n$. Its two-sided tail at $4$ is at most $2e^{-8n}$, yielding

\[
\Pr\{\|W^{(2)}_0\|_{\rm op}>8\}
\leq2\exp(-(8-2\log9)n).
\]

The exponent coefficient is positive. Likewise, the stated readout variance is $n^{-2}$, not $n^{-1}$, so

\[
\Pr\{\|W^{(3)}_0\|_\infty>1\}\leq2n e^{-n^2/2}.
\]

No independence between these three good events is needed. Define $E_n(x_1,x_2)$ to be their intersection, including the initial fourth-moment bound $13$. A precise valid replacement for lines 227–229 is:

> For every deterministic normalized input pair, take $a=8,b=1$. There is an event $E_n(x_1,x_2)$ on which (2)–(4) have deterministic bounds depending only on $T$ and the activation bounds, and
> \[
> \sup_{\substack{d\geq1;\ x_1,x_2\in\mathbb R^d\\ \|x_1\|^2=\|x_2\|^2=d}}
> \Pr(E_n(x_1,x_2)^c)
> \leq\frac{1680}{n}+2e^{-(8-2\log9)n}+2ne^{-n^2/2}\longrightarrow0.
> \]
> Thus the probability guarantee is uniform in dimension and input angle. For each such pair, its initialization event works for every finite $T$.

For example, the numerical fourth-path bound on this event is
\(104+128B_1^2T^2V_T^2\), with $a=8,b=1$ in $V_T$.

**Counterexample to a universal simultaneous-input event.** Let $d=n\to\infty$, let $g_n$ be the first row of $W^{(1)}_0$, and for each realization with $g_n\ne0$ select

\[
x_1=x_2=\sqrt n\,g_n^T/\|g_n\|.
\]

Then \(\rho=1\) and the first neuron alone contributes

\[
\frac1n\sum_i|z_i(0)|^4
\geq\frac1n\left(2n\|g_n\|^2\right)^2
=4n\|g_n\|^4.
\]

Now \(\mathbb E\|g_n\|^2=1\) and \(\operatorname{Var}(\|g_n\|^2)=2/n\), so this lower bound diverges in probability. A fixed deterministic fourth-moment bound cannot hold simultaneously over all normalized inputs with dimension unrestricted. Selecting a witness after seeing the realization is legitimate for disproving a universal event; it is not a counterexample to the theorem for a fixed input pair.

A simultaneous statement for a specified angle family can still be true. For example, fix orthonormal directions $e,f$, set $x_1=\sqrt d\,e$ and $x_2(\rho)=\sqrt d(\rho e+\sqrt{1-\rho^2}f)$. If $G_i,H_i$ are the corresponding independent standard Gaussian projections, then

\[
\sup_\rho\frac1n\sum_i|z_i(0;\rho)|^4
\leq\frac4n\sum_i(G_i^2+H_i^2)^2.
\]

The right side converges in probability to $32$. This shows why the required correction is to specify the quantifiers/family, not to assert that all simultaneous angle statements are impossible. This family is not specified in the source, and is not needed for its uniform-in-probability result.

## 6. UI, path compactness, and their exact scope

Consider a deterministic family of these flows for which

\[
\frac1n\sum_i|z_i(0)|^4\leq C_0,
\qquad \|W^{(2)}(0)\|_{\rm op}\leq a,
\qquad \|W^{(3)}(0)\|_\infty\leq b
\]

hold with common constants. The Gaussian good realizations above form such a family with $C_0=13,a=8,b=1$. Set

\[
C_4=8C_0+128B_1^2T^2V_T^2,
\qquad C_3=8B_1P_1V_T^2.
\]

The two tail calculations in lines 233–239 follow pointwise from
\(s^2\mathbf1_{s>R}\leq s^4/R^2\) and
\(s^2\mathbf1_{s>R}\leq s^3/R\), respectively. Thus

\[
\frac1n\sum_i\|z_i\|_\infty^2\mathbf1_{\|z_i\|_\infty>R}
\leq\frac{C_4}{R^2},
\qquad
\frac1n\sum_i\int_0^T|\dot z_i|^2\mathbf1_{|\dot z_i|>R}\,dt
\leq\frac{C_3}{R}.
\]

These are uniform integrability statements for the normalized counting measure and its product with time Lebesgue measure. No probability independence is involved. Activation paths satisfy \(\|h_i\|_\infty\leq\sqrt2B_1\), and activation velocities obey (4), giving the corresponding claims directly.

For $s<t$, integrating the derivative and applying Hölder on $[s,t]$ gives

\[
|z_i(t)-z_i(s)|\leq|t-s|^{2/3}
\left(\int_0^T|\dot z_i(u)|^3du\right)^{1/3}.
\]

The exponent $2/3$ and the absence of an extra $T$-factor are correct. If $H_i$ denotes the Hölder $2/3$ seminorm, then \(n^{-1}\sum_iH_i^3\leq C_3\).

Let \(\mu_n=n^{-1}\sum_i\delta_{z_i(\cdot)}\) on \(C([0,T];\mathbb R^2)\), with the uniform Euclidean path norm. For $L>0$, define

\[
K_L=\{\omega:|\omega(0)|\leq L,\ [\omega]_{2/3}\leq L\}.
\]

Every path in $K_L$ is bounded by $L(1+T^{2/3})$, and all share the modulus $L|t-s|^{2/3}$. The finite-grid diagonal argument in lines 250–254 proves compactness: bounded grid values admit a common convergent subsequence on all grids, and the common modulus makes that subsequence uniformly Cauchy; its continuous limit remains in $K_L$. Moreover,

\[
\mu_n(K_L^c)\leq C_0/L^4+C_3/L^3.
\]

This supplies the claimed mass on compact sets, not just a bound on path values.

One can also verify the quadratic-Wasserstein conclusion directly by finite approximations. Cauchy–Schwarz gives

\[
\int_{K_L^c}\|\omega\|_\infty^2d\mu_n
\leq\sqrt{C_4}\sqrt{C_0/L^4+C_3/L^3}.
\]

Cover $K_L$ by a finite \(\varepsilon\)-net, map each path inside $K_L$ to a nearby net point, and map the complement to the zero path. The induced coupling has squared cost at most

\[
\varepsilon^2+\sqrt{C_4}\sqrt{C_0/L^4+C_3/L^3}.
\]

The resulting measures lie on one finite set of paths, whose probability simplex is compact. Taking $L\to\infty$ and \(\varepsilon\downarrow0\) gives uniform finite approximation in $W_2$, which supplies the measure-level compactness behind the source's assertion. To see why limits remain in this path space, choose a subsequence with summable successive $W_2$ distances and corresponding finite-support approximations with summable errors. Couple consecutive finite-support measures by their transport matrices, matching their common marginals. The resulting random paths have summable $L^2$ distances, hence converge both almost surely in the complete uniform path norm and in $L^2$. Their limit law is a $W_2$ limit of the original subsequence. This uses finite couplings and completeness, without an external compactness theorem.

For joint preactivation/activation path laws, the map
\(\omega\mapsto(\omega,\phi_1(\omega))\) is Lipschitz for the corresponding product uniform norm, with constant at most \(\sqrt{1+P_1^2}\). It therefore preserves the compactness and second-moment-tail conclusion. The two samples are already coupled within each $\omega$; no assertion of their independence is required.

For Gaussian initialization, these deterministic statements apply on $E_n(x_1,x_2)$. In particular, for each fixed $T$, there is a fixed relatively compact family in $W_2$ containing the empirical path measure with probability tending to one, uniformly in the deterministic inputs. This does not assert that the same realization satisfies the displayed numerical bounds for every width. Nor do these estimates identify a limiting equation, give a strong limit of velocities, or establish convergence to a unique path law.

**Counterexample if the initial-moment condition is discarded.** Set $d=1$, $x_1=x_2=1$, take both activations to be arctan, and initialize $W^{(2)}=W^{(3)}=0$. The whole flow is stationary since \(h^{(2)}=\arctan(0)=0\) and both reverse fields vanish. Set the first row of $W^{(1)}$ equal to \(\sqrt n\) and all other rows to zero. The empirical path law is then

\[
\mu_n=(1-1/n)\delta_0+(1/n)\delta_{\omega_n},
\qquad \omega_n(t)=(\sqrt n,\sqrt n).
\]

It has second path moment $2$, fourth path moment $4n$, and zero velocity. It converges weakly to \(\delta_0\), but its squared path norms are not uniformly integrable and it has no $W_2$-convergent subsequence. This does not contradict (2), whose initial fourth moment explicitly diverges, or the Gaussian corollary. It establishes exactly why one must retain that corollary's moment scope; it does not establish that a fourth moment is the minimal possible assumption for UI.

## Final scoped assessment

The mechanism is sound: the actual transpose query has a bounded normalized $L^2$ time derivative; the controls therefore have an $L^2$ variation envelope; the rowwise work identity converts that envelope into a linear action bound; and this yields the stated fourth path and cubic velocity estimates at every input angle, including both singular cases.

The sole required correction is to resolve the probabilistic meaning of “simultaneously.” No change is required to (1)–(11), the definitions of their constants, the finite-GF existence argument, or the Gaussian scalar/net estimates. The UI and compactness conclusions pass in the stated Gaussian-event scope, or for deterministic families with uniform initial fourth moments. No broader population or discrete-time theorem is supported or claimed.

The mathematical source was left unchanged. Its SHA256 is the value recorded at the start of this review.

# Isolated adversarial review: finite raw-GD action and moment bounds

Reviewed source: `ALL_ANGLE_RAW_GD_ACTION.md`, all 270 lines.
Verified SHA256: `a153fbd8eb502a7627f863183634f0e2ee9f4810e77e9e94872b6a951ae95bbf`.

The source was the sole mathematical input. Only the procedural rigorous-math skill was consulted; no other project files, reviews, history, experiments, agents, external sources, or heavy external theorems were used. The candidate was not edited. Line references below refer to the verified candidate.

## Verdict and scope

**The deterministic finite-GD estimate passes this audit.** Under the stated initial operator/readout bounds, for all sufficiently large widths, the exact updates have the asserted descent and primal bounds, and the actual raw interpolation satisfies (2)–(4), with the displayed constants. The argument is uniform in dimension, input angle, and label pattern. I found no omitted mixed-Hessian term, unabsorbed width factor, circular descent assumption, or missing activation regularity in that result.

The Gaussian applicability estimates also check out. The qualification is in lines 257–263: the argument directly establishes **empirical uniform integrability in probability and path tightness in probability**. The text should specify these probability and topology conventions. It does not supply control on exceptional initialization events sufficient to infer uniform integrability after averaging over all initialization randomness. That stronger interpretation is not disproved, but it is not proved by the displayed high-probability argument.

There is no required mathematical correction to the main conditional deterministic theorem. There is a required scope clarification for the final probabilistic paragraph, or an additional argument if its intended meaning is the stronger expectation-level claim. No MF/GF comparison, identification, uniqueness, restart, or second-layer tail conclusion is being demanded here.

## 1. Exact updates and scaling — pass

For this review write \(\|u\|_n=\|u\|_2/\sqrt n\); products inside activation derivatives are coordinatewise. Differentiating \(L=\sum_a r_a^2\) gives the Euclidean gradients

\[
\nabla_{W^{(1)}}L=-\frac1n\sum_a c_a\delta_a^{(1)}x_a^T,
\qquad
\nabla_{W^{(2)}}L=-\frac1n\sum_a c_a\delta_a^{(2)}(h_a^{(1)})^T,
\qquad
\nabla_{W^{(3)}}L=-\frac1n\sum_a c_a h_a^{(2)}.
\]

The inverse metric weights are \(n/d,1,n\), respectively. Consequently \(-\eta\operatorname{grad}_{\rm raw}L\) is exactly (1), including the first-layer \(1/d\), second-layer \(1/n\), and readout factor without \(1/n\). The factor two in the loss derivative is exactly accounted for by \(c_a=-2r_a\). All fields on an update's right side are evaluated at its old node; no transformed Euler update has entered the argument.

The normalization \(\|x_a\|=\sqrt d\) implies both \(|C_{ab}|\le1\) and
\(\|V^{(1)}x_a\|_n\le\sqrt{d/n}\|V^{(1)}\|_F\). These remove the dimension factors used later.

## 2. Stopped primal bounds and closed descent — pass

Take \(N=\lceil T/\eta\rceil\) and \(H=T+1\). For \(\eta\le1\), \(N\eta\le H\). If a first exit occurs at a node \(j\le N\), every update producing nodes up to and including \(j\) starts with \(\|r_k\|_2\le R\), hence \(\sum_a|c_{k,a}|\le K\).

Summing readout increments yields \(\|W_k^{(3)}\|_\infty\le M\). Each second-layer increment obeys

\[
\|\Delta W^{(2)}_k\|_{\rm op}
\le\eta\sum_a|c_{k,a}|\,\|\delta_{k,a}^{(2)}\|_n\,\|h_{k,a}^{(1)}\|_n
\le\eta K P_2 M B_1.
\]

Thus the candidate exit endpoint also obeys \(\|W_j^{(2)}\|_{\rm op}\le A\). Convexity extends both parameter bounds over the entire segment into that endpoint. Recomputing the hidden quantities there then gives \(\|\delta_a^{(2)}\|_n\le P_2M\) and \(\|q_a^{(1)}\|_n\le Q\). No residual bound at the new endpoint was used to establish these segment parameter bounds.

The Hessian calculation below gives the segment-uniform prediction gradient bound \(F_*\). At an admissible old node,
\(\|\operatorname{grad}_{\rm raw}L_k\|_{\rm raw}\le K F_*\). Integrating the prediction differential over a fraction \(s\in[0,1]\) of its raw segment gives

\[
\|r(W_k-s\eta\operatorname{grad}_{\rm raw}L_k)\|_2
\le R+\sqrt2\eta K F_*^2.
\]

Choose \(n\) so that the extra term is at most one. The segment loss Hessian is then bounded by \(H_*(n)\) from (8). The integral Taylor remainder is at most
\(\eta^2 H_*(n)\|\operatorname{grad}_{\rm raw}L_k\|_{\rm raw}^2/2\), which proves (9) when \(\eta H_*(n)\le1\).

Induction through the proposed first exit gives \(L_j\le L_0\le R_0^2\), contradicting \(\|r_j\|_2>R_0+1\). This closes the bootstrap. In particular, loss monotonicity was not assumed to obtain its own Taylor-segment hypotheses.

## 3. Raw-metric mixed Hessian, including every term — pass

For unit raw tangents \(U,V\), use the candidate's factors \(\beta_\ell,\alpha_\ell\). In fact \(\sum_\ell\alpha_\ell^2\le1\) and \(\sum_\ell\beta_\ell^2\le1\); bounding each factor separately by one only enlarges constants. Write \(s_a[V]=D_Vz_a^{(2)}\). Then

\[
\|s_a[V]\|_n\le B_1\alpha_2+A P_1\alpha_1\le J,
\qquad
|D_Vf_a|\le B_2\alpha_3+M P_2\|s_a[V]\|_n\le F_*.
\]

The full mixed second derivative of the second preactivation is

\[
\begin{aligned}
D_U D_Vz_a^{(2)}={}&
V^{(2)}[\phi_1'(z_a^{(1)})U^{(1)}x_a]
+U^{(2)}[\phi_1'(z_a^{(1)})V^{(1)}x_a]\\
&+W^{(2)}[\phi_1''(z_a^{(1)})(U^{(1)}x_a)(V^{(1)}x_a)].
\end{aligned}
\]

The first two terms have RMS bounds \(P_1\alpha_2\beta_1\) and \(P_1\beta_2\alpha_1\). The last has RMS bound \(A L_1\sqrt n\alpha_1\beta_1\), using

\[
\|u v\|_n\le\sqrt n\|u\|_n\|v\|_n.
\]

The full prediction Hessian is the sum of the following four terms:

\[
\begin{aligned}
D_U D_V f_a={}&
\frac1n\langle U^{(3)},\phi_2'(z_a^{(2)})s_a[V]\rangle
+\frac1n\langle V^{(3)},\phi_2'(z_a^{(2)})s_a[U]\rangle\\
&+\frac1n\langle W^{(3)},\phi_2''(z_a^{(2)})s_a[U]s_a[V]\rangle\\
&+\frac1n\langle W^{(3)}\phi_2'(z_a^{(2)}),D_U D_Vz_a^{(2)}\rangle.
\end{aligned}
\]

Their bounds, in order, are \(P_2J\), \(P_2J\), \(M L_2J^2\), and
\(M P_2(2P_1+A L_1\sqrt n)\). The top-curvature bound specifically uses

\[
\frac1n\sum_i|W_i^{(3)}|\,|s_a[U]_i s_a[V]_i|
\le M\|s_a[U]\|_n\|s_a[V]\|_n,
\]

so no additional \(\sqrt n\) is lost there. The first-layer curvature is the only displayed source of width growth. The two readout cross terms also contain their respective first-layer and second-layer directions through \(s_a\); those mixed derivatives have not been omitted.

Finally,

\[
|D^2L[U,V]|
\le4F_*^2+2\Big(\sum_a|r_a|\Big)F_{**}(n)
\le4F_*^2+2\sqrt2(R+1)F_{**}(n).
\]

This verifies (7)–(8) as raw-metric operator bounds. Bounded \(C^2\) activation derivatives suffice for this argument; no third derivative, Hessian Lipschitz condition, or bound on \(z^{(1)}\) is required.

## 4. Actual node increments and the variation envelope — pass

Here is an explicit choice of width-independent rate constants that makes the candidate's repeated \(C_T\) transparent:

\[
\begin{aligned}
D_{W2}&=K P_2 M B_1,&D_{W3}&=K B_2,&D_{z1}&=K P_1Q,\\
D_{z2}&=B_1D_{W2}+A P_1D_{z1},\\
D_{\delta2}&=P_2D_{W3}+M L_2D_{z2},\\
D_q&=P_2M D_{W2}+A D_{\delta2},\\
D_c&=4K F_*^2,&D_v&=Q D_c+K D_q.
\end{aligned}
\]

The first-layer rate follows by summing \(\eta c_b\delta_b^{(1)}C_{ba}\) and using \(|C_{ba}|\le1\). The exact product difference with the **new** \(W^{(2)}\) gives the \(D_{z2}\) bound. Likewise,

\[
\Delta\delta_a^{(2)}
=\Delta W^{(3)}\phi_2'(z_{k,a}^{(2)})
+W_{k+1}^{(3)}[\phi_2'(z_{k+1,a}^{(2)})-\phi_2'(z_{k,a}^{(2)})]
\]

gives \(\|\Delta\delta_a^{(2)}\|_n\le\eta D_{\delta2}\). The candidate's actual transpose difference gives \(\|\Delta q_a^{(1)}\|_n\le\eta D_q\). The gradient bound gives \(|\Delta f_a|\le\eta K F_*^2\), hence \(\sum_a|\Delta c_a|\le\eta D_c\).

Using
\(\Delta(c_aq_a)=(\Delta c_a)q_{k,a}+c_{k+1,a}\Delta q_a\), and the now-proved bound on the new residual, yields

\[
\sum_a\|\Delta(c_aq_a)\|_n\le\eta D_v.
\]

Minkowski's inequality therefore proves

\[
\|U\|_n\le KQ+(N-1)\eta D_v\le KQ+H D_v.
\]

Thus \(V_T=KQ+H D_v\) is one valid explicit choice in (10). It is independent of \(n,d,C\), the label pattern, and all first-layer initial values. This reasoning uses only the Euclidean operator bound for the actual transpose; no coordinatewise or higher-\(L^p\) mapping property is being assumed.

The consequences \(\sum_a|v_{k,a,i}|\le U_i\) and \(\max_iU_i\le\sqrt n V_T\) are exact. A width-independent maximum bound on \(U_i\) is neither available nor needed.

## 5. Pointwise discrete work and Taylor absorption — pass

For the coefficient vector \(d_{k,i}=(v_{k,a,i}\phi_1'(z_{k,a,i}^{(1)}))_{a=1,2}\), the raw row update gives

\[
e_{k,i}=d_{k,i}^TCd_{k,i},\qquad
\Delta z_i=\eta C d_{k,i}.
\]

Since \(C\) is positive semidefinite with eigenvalues in \([0,2]\), \(C^2\preceq2C\); consequently \(|\Delta z_i|^2\le2\eta^2e_{k,i}\). This is valid even when \(e_{k,i}=0\).

Scalar Taylor expansion at the old node gives

\[
\sum_a v_{k,a,i}\Delta h_{a,i}
=\eta e_{k,i}+R_{k,i},\qquad
|R_{k,i}|
\le\frac{L_1}{2}\sum_a|v_{k,a,i}|\,|\Delta z_{a,i}|^2
\le L_1\eta^2U_i e_{k,i}.
\]

Thus the signed work sum is bounded below by
\((1-\eta L_1U_i)A_i\). Summation by parts bounds the same sum above by

\[
B_1\left(\sum_a|v_{N-1,a,i}|+\sum_a|v_{0,a,i}|
+\sum_{k=1}^{N-1}\sum_a|v_{k,a,i}-v_{k-1,a,i}|\right)
\le2B_1U_i.
\]

For \(\eta=n^{-2}\),
\(\eta L_1\max_iU_i\le L_1V_T n^{-3/2}\). Hence uniform absorption at level \(1/2\) is legitimate for sufficiently large \(n\), and gives exactly \(A_i\le4B_1U_i\). This is pointwise in the neuron index; it does not silently replace a pointwise estimate by an average estimate. No sign or monotonicity condition on either activation or the coefficients is used.

All small-step requirements can therefore be imposed simultaneously using only fixed constants:

\[
\sqrt2 n^{-2}K F_*^2\le1,\qquad
n^{-2}H_*(n)\le1,\qquad
L_1V_T n^{-3/2}\le\tfrac12.
\]

Since \(H_*(n)=O(1+\sqrt n)\) with the specified parameter dependence, this introduces no hidden width-dependent constant or dependence on the initial first-layer fourth moment.

## 6. Raw interpolation, exact constants, and singular angles — pass

On each raw interpolation cell, \(\dot z_i=Cd_{k,i}\). Hence

\[
|\dot z_i|\le2P_1U_i,\qquad
\int_0^{N\eta}|\dot z_i|^2\,dt\le2A_i,
\]

and

\[
\int_0^{N\eta}|\dot z_i|^3\,dt
\le(2P_1U_i)(2A_i)\le16B_1P_1U_i^2.
\]

The recomputed activation satisfies the ordinary chain rule almost everywhere, so multiplying by \(P_1^3\) gives the constant \(16B_1P_1^4\) in (4). Linear interpolation of activation values is not used.

Also,

\[
\sup_{t\le T}|z_i(t)|\le|z_i(0)|+\sqrt{2H A_i}.
\]

Applying the fourth-power inequality yields an increment contribution
\(8(2H A_i)^2=32H^2A_i^2\le512B_1^2H^2U_i^2\). Averaging proves exactly (2). Restricting the nonnegative integrals to \([0,T]\) handles a partial last cell. Velocities at the finitely many mesh times have no effect.

For \(\rho=C_{12}\in[-1,1]\), the eigenvalues of \(C\) are \(1+\rho\) and \(1-\rho\). Only positivity, \(|C_{ab}|\le1\), and \(\|C\|_{\rm op}\le2\) were used. No inverse, positive lower eigenvalue, or division by an angle-dependent quantity occurs. Both \(\rho=1\) and \(\rho=-1\), including inconsistent labels at coinciding inputs, are covered; no convergence to zero loss is asserted.

For the harmless endpoint \(T=0\), the conclusions hold directly. The summation-by-parts notation containing \(v_{N-1}\) should be used only for \(N\ge1\).

## 7. Gaussian initialization — pass

A maximal \(1/4\)-separated subset of the unit sphere has at most \(9^n\) points by the stated disjoint-ball volume comparison, and maximality makes it a \(1/4\)-net. Approximating both unit test vectors gives

\[
\|W^{(2)}\|_{\rm op}
\le2\max_{u,v\text{ in the net}}|u^TW^{(2)}v|.
\]

For fixed unit \(u,v\), the scalar on the right is centered Gaussian of variance \(1/n\). The event \(\|W^{(2)}\|_{\rm op}>8\) therefore implies a net pair with absolute scalar value greater than four. Applying the scalar exponential bound and summing over at most \(9^{2n}\) pairs gives exactly
\(2\exp[-(8-2\log9)n]\). The exponent is positive. For the readout, variance \(n^{-2}\) gives \(2n\exp(-n^2/2)\) by the same bound and a union over coordinates. These estimates do not require independence of the net test values.

Each first-layer row pair is centered Gaussian with covariance \(C\), independently across rows, including singular \(C\). Direct Gaussian moments give

\[
\mathbb E|z_i(0)|^4
=3+3+2(1+2\rho^2)=8+4\rho^2\le12.
\]

The eighth moment is bounded uniformly in angle and dimension:

\[
\mathbb E|z_i(0)|^8
\le8\big(\mathbb E|z_{1,i}(0)|^8+\mathbb E|z_{2,i}(0)|^8\big)
=1680.
\]

Thus for \(S_{0,n}=n^{-1}\sum_i|z_i(0)|^4\),
\(\Pr(|S_{0,n}-(8+4\rho^2)|>\varepsilon)\le1680/(n\varepsilon^2)\). This justifies the stated convergence in probability for fixed angle and a uniform concentration assertion about the corresponding mean if the angle varies with width. No initial coordinate maximum is required.

## 8. Uniform integrability and compactness: precise supported conclusion

Let \(E_n\) be the event consisting of the two initial norm bounds with \(a=8,b=1\), and put \(G_n=E_n\cap\{S_{0,n}\le13\}\). Then

\[
\Pr(G_n^c)
\le2e^{-(8-2\log9)n}+2n e^{-n^2/2}+\frac{1680}{n}
\longrightarrow0.
\]

For all sufficiently large \(n\), on this single event, define
\(C_{\rm path}=104+512B_1^2H^2V_T^2\) and
\(C_{\rm vel}=16B_1P_1V_T^2\). The candidate proves, simultaneously for every \(R>0\),

\[
\frac1n\sum_i\|z_i\|_\infty^2
\mathbf1_{\{\|z_i\|_\infty>R\}}
\le\frac{C_{\rm path}}{R^2},
\qquad
\frac1n\sum_i\int_0^T|\dot z_i|^2
\mathbf1_{\{|\dot z_i|>R\}}\,dt
\le\frac{C_{\rm vel}}R.
\]

Here \(\|z_i\|_\infty=\sup_{t\le T}|z_i(t)|\). These are amplitude thresholds; the stated powers of \(R\) are correct with this convention. There is an analogous velocity bound for \(h_i\) using (4).

In particular, for either tail functional \(F_n(R)\) just displayed and every \(\varepsilon>0\),

\[
\lim_{R\to\infty}\limsup_{n\to\infty}
\Pr\big(F_n(R)>\varepsilon\big)=0.
\]

This is a precise empirical uniform-integrability-in-probability statement. Deterministically, the same tail inequalities hold along any sequence satisfying the initial norm conditions and a uniform empirical initial fourth-moment bound.

For compactness, set \(\mu_n=n^{-1}\sum_i\delta_{z_i(\cdot)}\) on \(C([0,T];\mathbb R^2)\) with its uniform norm. Integral Holder gives

\[
[z_i]_{2/3}^3
\le\int_0^T|\dot z_i|^3\,dt,
\qquad
\frac1n\sum_i[z_i]_{2/3}^3\le C_{\rm vel}
\quad\text{on }G_n.
\]

For \(L>0\), the set of paths with \(\|z\|_\infty\le L\) and \([z]_{2/3}\le L\) is compact in the uniform norm: bounded values on successively finer finite time grids admit a diagonal subsequence, and the common modulus of continuity makes it uniformly convergent. On \(G_n\), its complement has \(\mu_n\)-mass at most
\(C_{\rm path}/L^4+C_{\rm vel}/L^3\). This establishes the claimed path tightness in probability, together with second-moment tail control. It neither identifies a limiting dynamics nor proves convergence of the whole sequence.

What is missing for a stronger reading of lines 257–263 is a bound on
\(\mathbb E[F_n(R)\mathbf1_{E_n^c}]\). A small value of \(\Pr(E_n^c)\) alone does not bound this expectation. Likewise, convergence in probability of the initial empirical moment does not by itself specify an almost-sure compactness claim for an entire sequence of widths. These are distinctions in quantifiers, not counterexamples to (2)–(4).

## Required and optional fixes

**Required for precision of the full standalone text:** qualify lines 257–263 as empirical uniform integrability and path tightness **in probability**, in the uniform topology on \(C([0,T];\mathbb R^2)\), or state the equivalent deterministic conclusion along sequences with uniformly bounded empirical initial fourth moments. The displayed probability-tail formulation above is a concrete replacement. If unconditional expectation-level uniform integrability is intended, add an exceptional-event moment argument; the present proof does not contain one. No additional activation regularity is implicated by this qualification.

**No required correction to the deterministic estimates:** the exact raw optimizer, stopped bounds, all mixed Hessian terms, residual-on-segment control, node variation, Taylor absorption, and constants in (2)–(4) are mathematically consistent as written.

**Optional improvements:** give one explicit set of increment constants such as those above; display the four prediction-Hessian terms instead of describing them; explicitly separate the trivial \(T=0\) case before using \(v_{N-1}\); and state that Gaussian fourth-moment concentration is about \(8+4\rho_n^2\) when considering width-dependent input angles.

No further first-layer moments, coordinatewise reverse-field bounds, independence after training, input-angle nondegeneracy, or GF/population assertions are needed for the scoped finite-GD result.

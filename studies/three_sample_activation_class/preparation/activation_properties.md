# Activation-property audit and explicit generalization routes

Source inspected: `/home/amir/Codes/PDE/studies/three_sample_self_contained/MANUSCRIPT.md`, including every activation-specific occurrence in Parts F, R, G, V, V.I and N. This is an authoring audit of the activation substitution, not an independent verification of every general Gaussian-program argument in the source. No numerical experiments or other study summaries were used.

## 1. Main finding and an important quantifier distinction

There are two valid extensions.

1. **Literal preservation of Theorem M.1, including an absolute nonlinear margin and constants selected from separation alone:** use a normalized infinite-dimensional class with a uniform Gaussian regression margin. A concrete open perturbation ball around a small multiple of arctangent is given in Section 7 below. Members can be nonodd, nonmonotone, and oscillatory at infinity. All members share one pair of constants depending only on the separation.
2. **A broader shape-dependent extension:** every nonconstant bounded function \(\psi\in C^2(\mathbb R)\) with bounded first and second derivatives works after normalization. Every existence, convergence, initial-motion and changing-kernel conclusion remains valid, and the nonlinear regression error stays bounded away from zero uniformly in physical time. The margin and activation selection can depend on \(\psi\) and \(\delta\). The word “absolute” in M.1(3) must be changed for this broader statement. A compactly supported perturbation does not have a positive Gaussian regression margin uniformly over all Gaussian scales.

The root author's proposed \(C_b^3\) class with bounds through order three is sufficient. The actual proof uses no third derivative of \(\psi\). The regularity floor for the argument as written is \(C^2\), with bounded \(\psi,\psi',\psi''\); no claim of logically minimal necessary regularity is intended.

In what follows normalize
\[
 \|\psi\|_\infty,\ \|\psi'\|_\infty,\ \|\psi''\|_\infty\le1,
 \qquad \psi\text{ nonconstant},\qquad
 \phi(z)=a(1+z)+e\psi(z),\quad a\ge2,\quad0<e\le1.
\]
For a general bounded shape \(u\), take
\(M=\max\{1,\|u\|_\infty,\|u'\|_\infty,\|u''\|_\infty\}\), set \(\psi=u/M\), and replace the permitted amplitude of \(u\) by the normalized cutoff divided by \(M\). Include \(\|u'''\|_\infty\) if retaining the author's more restrictive \(C_b^3\) formulation.

The additional input restriction \(-1+\delta<\Gamma_{ij}<1-\delta\) needs no new geometry argument: it implies the original upper-separation condition. No part of this extension needs the lower restriction or invertibility of \(\Gamma\).

## 2. Properties used by the analytic machinery

Put \(g=\psi'\) and
\[
 D_R(z,q)=aq+eg(z)\tau_R(q).
\]
Then every original numerical upper bound survives:
\[
 |\phi(z)|\le a|z|+a+2,\quad
 |\phi'(z)|\le a+e,\quad |\phi''(z)|\le e,
\]
\[
 |D_R(z,q)|\le(a+e)|q|,\quad
 |\partial_qD_R|\le a+e,\quad
 |\partial_zD_R|\le2eR,
\]
and
\[
 |D_R(z,q)-aq|\le e|q|.
\]
At fixed cap, \(D_R\) is \(C^1\), globally Lipschitz, and has bounded first derivatives. Nonnegativity of \(g\), oddness of \(\psi\), and sign agreement between \(z\) and \(\psi(z)\) are not used in these bounds.

The exact derivative matrices in R.44 become
\[
 G_k=aI+e\operatorname{diag}(\psi'(Z_k)),\qquad
 V_k=aI+e\operatorname{diag}(\psi'(Z_k)\tau_R'(q_k)),
\]
\[
 L_k=e\operatorname{diag}(\psi''(Z_k)\tau_R(q_k)).
\]
They satisfy precisely R.45:
\[
 |G_k|,|V_k|\le a+1,\quad
 |G_k-aI|,|V_k-aI|\le e,\quad |L_k|\le eQ_k.
\]
All of R.46–R.94 uses these inequalities and the finite-program rules, not a special identity of arctangent. In particular the entire explicit chain defining \(\epsilon_*(a,B,S)\) can remain numerically unchanged. It is uniform over the normalized shape class.

F.5–F.7, the weighted scalar Taylor estimates, the strong curve chain rule, and V.I use bounded continuous \(\phi'\) and \(\phi''\). The source identities for the unbounded initial backward products use only their integrable envelopes involving \(1+|H|\) or \(1+|q|\). The velocity-observation argument differentiates \(\phi'(Z)P\) once and uses \(\phi''\), never \(\phi'''\).

For cap removal, the unchanged asymmetric estimate is
\[
 |D_{R'}(z_A,q_A)-D_R(z_B,q_B)|
 \le(a+e)|q_A-q_B|+2eR|z_A-z_B|
       +2e|q_B|\mathbf1_{|q_B|>R}.
\]
Indeed first vary \(q\) using the \((a+e)\)-Lipschitz bound; insert \(g(z_A)\tau_R(q_B)\); use \(|g(z_A)-g(z_B)|\le|z_A-z_B|\) and \(|\tau_R|\le2R\); and bound the cap difference by \(2|q_B|\mathbf1_{|q_B|>R}\). This uses no sign condition on \(g\).

## 3. Initial Gaussian feature coercivity with nonodd/nonmonotone shapes

This is the first genuine replacement for an arctangent-specific argument. For a centered Gaussian triple with common marginal variance \(v>0\), covariance \(Q\), and \(Z=Q^{1/2}G_3\), projection onto constants and Gaussian linear functions gives
\[
 \Pi\phi(Z_i)=\mu_v+b_vZ_i,
 \qquad \mu_v=a+eE\psi(\sqrt vG),
 \qquad b_v=a+eE\psi'(\sqrt vG).
\]
For completeness, Gaussian integration by parts yields
\(E[G_{3,j}\psi(Z_i)]=(Q^{1/2})_{ij}E\psi'(Z_i)\), so this remains valid when \(Q\) is singular. The common marginal law makes \(\mu_v,b_v\) the same for all sample indices. The projection residuals are orthogonal to the constants and to every Gaussian linear coordinate. Their Gram is positive semidefinite. Therefore
\[
 E[\phi(Z)\phi(Z)^T]\succeq\mu_v^2\mathbf1\mathbf1^T+b_v^2Q.
\]
Since \(a\ge2,e\le1\),
\[
 \mu_v,b_v\ge a-1\ge a/2,
 \qquad
 E[\phi(Z)\phi(Z)^T]\succeq\frac{a^2}{4}
                    (\mathbf1\mathbf1^T+Q).
\]
Thus, writing \(Q_0=\Gamma\) and \(c=a^2/4\ge1\),
\[
 Q_3\succeq c^3\Gamma+(c^3+c^2+c)\mathbf1\mathbf1^T
      \succeq \frac{a^6}{64}(\Gamma+\mathbf1\mathbf1^T)
      \succeq\lambda a^6I_3,
 \qquad \lambda=\delta^2/256.
\]
Also \(Q_1,Q_2\succ0\), and all initial preactivation marginal variances are at least one: the variance recursion has
\(v_{\ell+1}=E\phi(\sqrt{v_\ell}G)^2\ge c(1+v_\ell)\), starting at \(v_1=1\).

This replaces both the original zero-mean perturbation in G.3 and the sign argument \(|az+e\arctan z|\ge a|z|\) in G.2. Neither is valid for general \(\psi\); neither is needed after this projection argument.

With this new \(\lambda\), every upper-bound computation G.14–G.28 remains unchanged. The inequalities requiring \(\lambda\le9/16\) still apply because the new \(\lambda\) is smaller.

## 4. Broad-class regression margin and a noncircular gain selection

Define
\[
 \mathcal R_\psi(Z)=\inf_{\alpha,\beta\in\mathbb R}
                          E[\psi(Z)-\alpha-\beta Z]^2.
\]
Because bounded nonconstant \(\psi\) cannot be globally affine, there is an integer \(r_\psi\ge1\) such that
\[
 J_\psi=\inf_{\alpha,\beta}\int_{-r_\psi}^{r_\psi}
                   [\psi(z)-\alpha-\beta z]^2\,dz>0.
\]
The affine functions form a finite-dimensional, hence closed, subspace of the indicated \(L^2\) space. A zero distance would give equality almost everywhere, and continuity would give equality everywhere on that interval. If no such interval existed, nesting would make \(\psi\) globally affine and bounded, hence constant. Explicitly,
\[
 J_\psi=\int_{-r_\psi}^{r_\psi}\psi^2
       -\frac{(\int_{-r_\psi}^{r_\psi}\psi)^2}{2r_\psi}
       -\frac{(\int_{-r_\psi}^{r_\psi}z\psi)^2}{2r_\psi^3/3}.
\]
Set
\[
 c_\psi=\frac{e^{-r_\psi^2/2}}{\sqrt{2\pi}}J_\psi>0.
\]
For \(\sigma\ge1\), the density of \(\sigma G\) on this interval is at least \(e^{-r_\psi^2/2}/(\sqrt{2\pi}\sigma)\). Taking the infimum over affine predictors after applying that pointwise lower bound proves
\[
                       \mathcal R_\psi(\sigma G)\ge c_\psi/\sigma.
\]
The initialized standard deviations satisfy
\[
 \sigma_1=1,\qquad \sigma_2\le3a,\qquad \sigma_3\le5a^2.
\]
Indeed \(\sigma_2=\|\phi(G)\|_2\le\sqrt2a+1\le3a\), and
\(\sigma_3=\|\phi(\sigma_2G)\|_2\le a(1+\sigma_2)+1\le5a^2\) for \(a\ge1\). The equality between a next-layer initial variance and the previous feature second moment is the fresh initialized Gaussian-forward-call rule, not an assertion about arbitrary operators.

Consequently all initial scalar margins are at least
\[
                         \eta_a=c_\psi/(5a^2)>0.
\]
For a coupling with \(\operatorname{sd}(Z_0)\ge1\) and
\(\|Z-Z_0\|_2\le1/2\), one has \(\operatorname{sd}(Z)\ge1/2\). The optimal slope for regressing \(\psi(Z)\) on \(Z\) is at most
\(\sqrt{\operatorname{Var}(\psi(Z))}/\operatorname{sd}(Z)\le2\). Testing this same affine predictor at \(Z_0\) and using \(\|\psi(Z)-\psi(Z_0)\|_2\le\|Z-Z_0\|_2\) gives
\[
 \sqrt{\mathcal R_\psi(Z_0)}
 \le\sqrt{\mathcal R_\psi(Z)}+3\|Z-Z_0\|_2.
\]
Define
\[
 k_\psi=\min\{1/2,\sqrt{c_\psi}/(6\sqrt5)\},\qquad
 t_a=k_\psi/a.
\]
Then \(t_a\le1/2\) and \(3t_a\le\sqrt{\eta_a}/2\), so
\(\|Z-Z_0\|_2\le t_a\) implies \(\mathcal R_\psi(Z)\ge\eta_a/4\).

An explicit selection avoiding a circular dependence of the margin on \(a\) is
\[
 a=\max\left\{2,\frac{2000}{\sqrt\lambda},
            \left(\frac{10^{12}}{\lambda^2k_\psi}\right)^{1/3}\right\},
 \quad S=\frac{12}{\lambda a^6},
\]
\[
 e_\delta=\frac12\min\{1,\epsilon_*(a,12,S),(10^{10}a)^{-1}\}.
\]
The new third-root condition is exactly the original needed condition
\(a^4t_a\ge10^{12}/\lambda^2\). Therefore G.19 holds with \(t_a\), and the same controlled-clock and cap-transfer proof gives, simultaneously in sample, layer and physical time,
\[
 \inf_{t\ge0}\inf_{\alpha,\beta}
 E[\phi(z_i^\ell(t))-\alpha-\beta z_i^\ell(t)]^2
 \ge e^2\eta_a/4=\frac{e^2c_\psi}{20a^2}>0.
\]
The identity used in the last step is exact for any shape: the affine baseline can be absorbed into \(\alpha,\beta\), giving regression error \(e^2\mathcal R_\psi(Z)\).

## 5. Initial backward positivity and motion

The generalized Gaussian projection gives \(Q_1,Q_2\succ0\), hence \(Z^3\) has full support on \(\mathbb R^3\). Also
\[
                         \phi'(z)=a+e\psi'(z)\ge a-1\ge a/2>0.
\]
The full proof of N.11–N.12 works with two replacements:

- The first factor \(F(z)=\sum_i p_i\phi(z_i)\) has no open zero set because every partial derivative \(p_i\phi'(z_i)\) is nonzero.
- After its dense nonzero set forces \(\sum_i v_i\phi'(z_i)\equiv0\), differentiating coordinate \(i\) gives \(ev_i\psi''(z_i)=0\) for every \(z_i\). Boundedness and nonconstancy imply \(\psi''\not\equiv0\): if it vanished identically, \(\psi\) would be bounded affine and therefore constant. Thus every \(v_i=0\) and \(S_3\succ0\).

The derivative-valid initial transpose identities N.13–N.14 remain exactly the same with \(\phi''=e\psi''\). Their truncation justifications in V.I need no sign condition or arctangent formula.

Replace the factors \(a^2\) by \(a^2/4\) in the positivity lower bounds N.15, N.16, N.17 and N.19. Every strict positivity conclusion survives. N.18 is activation independent. Replace lower gate factors \(a\) by \(a/2\) when transferring nonzero preactivation directions to nonzero feature directions.

All affine comparison calculations N.3–N.4 are unchanged because their comparator has \(e=0\). Their label argument \(|\sum_i p_i|\ge1/3\) uses exactly three binary labels and does not concern the activation shape.

**Every numerical bound N.40–N.53 is unchanged.** Those calculations use only
\(|\phi'-a|\le e\), \(|\phi'|\le2a\), \(|\psi|\le2\), initialized operator norms at most 10, normalized first variance one, and \(\sum_i|p_i|=1\). Our normalization improves the third bound to \(|\psi|\le1\). In particular, the common upper-direction error
\[
 \|U_{j,e}^{\ell}-U_{j,0}^{\ell}\|_2\le2\cdot10^8a^7e,
 \qquad\ell=2,3,
\]
and the cutoff \(e\le(10^{10}a)^{-1}\) are valid without modification.

The physical-time coefficient 9 in all initial hidden second derivatives and the kernel coefficient 18 in N.64 are unchanged. Their derivation uses the physical raw metric, \(p=y/3\), \(C(0)=0\), the bounded multiplier lemma and scalar feature-energy differential. It uses no special property of arctangent after positivity has been established.

## 6. What fails if the replacement is only textual

- Nonodd \(\psi\) changes the Gaussian constant projection from \(a\) to \(a+eE\psi\). Omitting this term makes G.3 incorrect.
- Nonmonotone \(\psi\) need not satisfy \(b_v\ge a\), \(\phi'\ge a\), or the original sign inequality used to show variance growth. The \(a/2\) bounds above repair all three.
- Nonconstant bounded \(\psi\) need not have \(\inf_{\sigma\ge1}\mathcal R_\psi(\sigma G)>0\). For example, for nonzero smooth compactly supported \(\psi\), \(E\psi(\sigma G)^2\to0\), and hence \(\mathcal R_\psi(\sigma G)\to0\). Continuity and positivity at every finite scale alone do not prove a positive infimum over an unbounded scale interval.
- Merely choosing a finite-scale margin after selecting \(a\), then citing the old \(a\)-selection rule depending on that margin, is circular. The explicit \(c_\psi/\sigma\) estimate and cubic gain choice above resolve this.
- A constant perturbation is excluded for substantive reasons: the activation is affine, the regression margin vanishes identically, and the strict top backward-Gram argument fails. Nonconstancy is enough within the bounded class; a separate curvature condition is redundant.
- If only \(C_b^2\) or \(C_b^3\) regularity is assumed, replace prose calling the finite field “smooth” by “continuously differentiable and locally Lipschitz.” This is all the finite existence/GD argument requires.

## 7. A concrete infinite-dimensional class preserving an absolute margin

Let
\[
 \eta_{\rm atan}=\inf_{\sigma\ge1}\mathcal R_{\arctan}(\sigma G)>0,
 \quad\psi_0(z)=\tfrac14\arctan z,
 \quad\rho=\min\{1/4,\sqrt{\eta_{\rm atan}}/8\}.
\]
The manuscript itself proves positivity of \(\eta_{\rm atan}\), without an external source. Define
\[
 \mathfrak C=\{\psi_0+u:
       u\in C_b^3(\mathbb R),\ 
       \max_{0\le j\le3}\|u^{(j)}\|_\infty\le\rho\}.
\]
Every member obeys the normalized bounds through order three. For instance,
\(\|\psi_0\|_\infty=\pi/8<1/2\),
\(\|\psi_0'\|_\infty\le1/4\),
\(\|\psi_0''\|_\infty\le1/4\), and
\(\|\psi_0'''\|_\infty\le1/2\); adding at most \(1/4\) keeps each norm below one. The third-derivative bound follows directly from
\(\arctan'''z=(6z^2-2)/(1+z^2)^3\), whose absolute value is at most 2.

For fixed \(\sigma>0\), regression on \(\{1,\sigma G\}\) is orthogonal projection onto the same subspace \(\operatorname{span}\{1,G\}\). Distance to a closed subspace is 1-Lipschitz in its target. Hence
\[
 \sqrt{\mathcal R_\psi(\sigma G)}
 \ge\tfrac14\sqrt{\mathcal R_{\arctan}(\sigma G)}
       -\|u(\sigma G)\|_2
 \ge\frac18\sqrt{\eta_{\rm atan}},\qquad\sigma\ge1.
\]
Thus the entire class shares the absolute margin
\[
                            \bar\eta=\eta_{\rm atan}/64>0.
\]
Choose
\[
 t_* =\min\{1/2,\sqrt{\bar\eta}/6\},\quad
 \lambda=\delta^2/256,\quad
 a_\delta=\max\left\{2,\frac{2000}{\sqrt\lambda},
       \left(\frac{10^{12}}{\lambda^2t_*}\right)^{1/4}\right\},
\]
and take \(S,e_\delta\) from the original rule with this \(a_\delta,\lambda\). The same \(a_\delta,e_\delta\) work for every \(\psi\in\mathfrak C\). All conclusions of M.1 then hold with the absolute constant \(\bar\eta\), including the normalized inequality \(e^2\bar\eta/4\).

This is genuinely infinite dimensional in the mathematical sense: it contains a ball in the function space \(C_b^3\), not just finitely many shape parameters. No parity, monotonicity or saturation limits are imposed. Taking \(u=\varepsilon\sin z\), with \(0<\varepsilon\le\rho\), gives a nonmonotone \(\psi\): its derivative is negative along sufficiently large odd multiples of \(\pi\), because the derivative of the arctangent baseline tends to zero. Taking \(u=\varepsilon\cos z\) breaks oddness and also gives nonmonotonicity. Both have oscillatory tails.

A different easy sufficient subclass consists of bounded nonconstant \(\psi\) with finite distinct one-sided limits \(L_+\ne L_-\). Direct dominated convergence gives
\[
 \mathcal R_\psi(\sigma G)\longrightarrow
        \frac{(L_+-L_-)^2}{4}(1-2/\pi)>0.
\]
Continuity and positive regression error at finite scales imply a positive shape-dependent global margin. This subclass needs no monotonicity or oddness, although a uniform margin over an entire class needs a uniform nondegeneracy condition such as the perturbation ball above.

## 8. Compact replacement ledger

| Location | Required replacement or property |
|---|---|
| M.2, F.1, R.3, V activation setup, N setup | Replace arctangent by fixed normalized \(\psi\); write \(g=\psi'\). |
| F.17, R.4/R.30–R.45, V.3 and cap comparisons | Same numerical upper bounds; only \(\|\psi\|_\infty\le2\), \(\|\psi'\|_\infty,\|\psi''\|_\infty\le1\). |
| R.46–R.94 | Identical equations with \(g=\psi'\), \(g'=\psi''\); same explicit response threshold. |
| G.3–G.5 | General mean \(\mu_v\), slope \(b_v\); lower each by \(a/2\); use \(\lambda=\delta^2/256\). |
| G.2 initial variance argument | Use Gaussian projection variance recursion; original sign identity is unavailable. |
| G.6–G.8, M.21 | General regression formula; stability constant 3; either global margin class or local-interval density bound with explicit cubic gain. |
| G.14–G.28 | Same constants with the newly chosen \(a,\lambda,t_*\) or \(t_a\). |
| V.I | Same identities with bounded \(\phi'',\phi'\); no extra derivative. |
| N.11–N.12 | \(\phi'\ge a/2\), \(\phi''=e\psi''\not\equiv0\). |
| N.15–N.19 | Replace lower \(a^2\) factors by \(a^2/4\); all strict positivity remains. |
| N.20–N.39 | Entirely unchanged affine comparator calculation. |
| N.40–N.53 | Entirely unchanged upper constants and amplitude cutoff. |
| N.54–N.64 | Entirely unchanged time factors, initial acceleration and kernel expansion. |
| M.1 absolute-margin wording | Keep verbatim for Section 7 class; replace by shape/separation-dependent margin for unrestricted bounded nonconstant class. |

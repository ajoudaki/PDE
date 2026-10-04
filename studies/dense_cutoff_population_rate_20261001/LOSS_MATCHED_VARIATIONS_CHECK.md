# Internal reconstruction of the matched-loss assessment

Verdict: **PASS for the exact finite-system identities and the explicitly scoped diagnostic example.** No width theorem, endpoint smoothness theorem for canonical dense training, or slower-than-root construction is established.

Checked candidate: LOSS_MATCHED_VARIATIONS.md, SHA-256
698b3cd6a947a9f01ea28ee45105e5436dcf2a4a8e0edecdd9ddda780cb1d368.
The coordinator read the complete initial candidate and all amendments, and reconstructed the calculations against the current manuscript's dense flow and tangent Gram. The coordinator contributed the signed Hessian expansion and finite-difference transfer before their final reconstruction. This is a collaborative internal check, not an independent promotion review.

## 1. Normalizations and regularity

With unhalved loss \(\mathcal L=r^\top r/m\), the physical gradient is \(g=2J^\top r/m\). Canonical mobility \(D\) gives \(F=-Dg\), \(K=JDJ^\top=m\Gamma\), \(\dot r=-2\Gamma r\), and
\[
a=-\dot{\mathcal L}=g^\top Dg
 =4r^\top Kr/m^2,\qquad
a/\mathcal L=4r^\top\Gamma r/(r^\top r).
\]
All factors agree with the paper. The mobility norm weights first-layer and readout squared norms by \(1/n\), leaving hidden Frobenius norms unscaled.

The candidate correctly restricts first and second classical responses to \(C^2\) and \(C^3\) activations respectively. The broader manuscript \(C^{1,1}\) class does not automatically support the classical second-response calculation. Positive loss and nonzero loss velocity are retained for every hitting-time identity; zero labels are excluded from that parametrization.

## 2. Hitting times, projection, and observable dependence

For \(Q(\varepsilon,t)=\mathcal L_\varepsilon(q_\varepsilon(t))\), implicit differentiation of \(Q(\varepsilon,t_\varepsilon)=\ell\) gives
\[
t'=-Q_\varepsilon/Q_t,\qquad
t''=-\{Q_{\varepsilon\varepsilon}+2Q_{\varepsilon t}t'
                       +Q_{tt}(t')^2\}/Q_t.
\]
Differentiating \(q_\varepsilon(t_\varepsilon)\) twice yields exactly the candidate's equations (7) and (10). The curvature and mixed time terms cannot be omitted.

In increment coordinates, both \(F_\varepsilon(q)=F(\theta_0(\varepsilon)+q)\) and \(\mathcal L_\varepsilon(q)\) depend explicitly on initialization. The first and second partial derivatives in (12) are correct. The query-prediction chain rule (13) includes these explicit terms too.

In physical coordinates \(Q_t=-a\), so the matched first response is
\[
U=PZ_1,\qquad P=I-Dg\,g^\top/a.
\]
Direct multiplication proves \(P^2=P\), \(PF=0\), and self-adjointness in the \(D^{-1}\) metric. Thus the first response norm cannot increase merely by projection. The second response satisfies \(g^\top V+H[U,U]=0\), not \(g^\top V=0\).

## 3. Evolution at fixed log loss

The exact log-loss field is \(G=-\mathcal L Dg/a\). Along a matched first response, \(g^\top U=0\), \(Dg[U]=HU\), and \(Da[U]=2g^\top DHU\). Hence
\[
U_s=-(\mathcal L/a)(I-2Dg\,g^\top/a)DHU.
\]
The parenthesized operator is a reflection in the mobility metric. Its norm identity is valid; it describes the remaining tangent response's derivative, not a denial of the projection improvement above.

Since \(U\) is tangent, the normal correction disappears in its energy pairing:
\[
\tfrac12\partial_s\|U\|_{D^{-1}}^2
 =-(\mathcal L/a)H[U,U].
\]
The decomposition \(H=2J^\top J/m+2\sum_a r_a\nabla^2f_a/m\) proves equation (19), including its dissipative part and surviving residual-weighted prediction Hessian.

For the second response, along the matched family,
\[
a_1=2g^\top DHU,\qquad
a_2=2(HU)^\top D(HU)+2g^\top D(HV+T[U,U]).
\]
Twice applying the quotient rule to \(-\mathcal L Dg/a\), with total first and second loss derivatives zero, reproduces all four terms and signs in (21). Left multiplication by \(P\) gives (22); the candidate correctly does not replace this by the derivative of \(PV\).

## 4. Dense carrier products and the weaker energy target

The first and second product rules for \(\phi'(z)p\) reproduce (24) and (25), including the factor two in the mixed first-response product. The lower carrier derivative in (26) uses the same matrix and its transpose, not independent Gaussian actions.

For an affine physical parameter direction, recursively expanding second forward derivatives gives
\[
D^2f[U,U]=n^{-1}\sum_{\ell,i}
p_i^{(\ell)}\phi_\ell''(z_i^{(\ell)})(Dz_i^{(\ell)}[U])^2
+2n^{-1}\sum_{\ell\ge2}
\delta^{(\ell)\top}\Delta W^{(\ell)}Dh^{(\ell-1)}[U]
+2n^{-1}\Delta w^\top Dh^{(L)}[U].
\]
There is no first-layer matrix cross term because its input is fixed. This proves (28a). In the energy identity these are signed, residual-weighted products. No general moment bound for them is inferred from the algebra.

For one sample, dividing the physical parameter equation by the training-prediction velocity gives \(d\theta/df=D\nabla f/(\nabla f^\top D\nabla f)\). Projecting its first variation yields (29). Fixed-loss training predictions are identical on the same residual-sign branch; unseen predictions need not be.

## 5. Endpoint diagnostic and finite differences

For the rotated two-output linear model, directly diagonalizing its residual equation gives (31). With \(u=e^{-\alpha t}\), \(v=e^{-\beta t}\), the first and second fixed-time derivatives are exactly \((0,c(v-u))\) and \((-2c(v-u),0)\).

At fixed reference loss the first hitting-time derivative vanishes. The second is \(((v/u)^2-1)/\alpha\). Adding its velocity contribution gives matched second first-component derivative \(c(v-u)^2/u\), which diverges when \(\alpha>2\beta\). This example is explicitly outside the canonical all-layer-trained dense model and cannot serve as its negative width construction.

The residual finite-difference lemma uses only
\(\|\dot r\|_2/\sqrt m\le2\Lambda\rho\) and
\(-\dot\rho\ge2\lambda\rho\). Integrating
\(\|dr/d\rho\|_2/\sqrt m\le\Lambda/\lambda\) between the two residual magnitudes proves (34). Since the rotation formula has uniform same-time difference \(O(|\varepsilon|)\), its matched residual difference is also \(O(|\varepsilon|)\), despite the second derivative divergence. This explicitly prevents interpreting a coordinate-regularity failure as a slow finite-difference rate.

## Conclusion and open obligations

The bounded assessment is mathematically consistent in its stated scopes. Pure speed cancels; mixed transverse responses survive; first-response energy offers a weaker signed estimate to target; and second matched-loss smoothness can fail without a prediction-rate failure. General finite mixed-moment bounds, population-bias identification, and strict all-time root width remain unproved. No experiment or formal proof assistant was used.

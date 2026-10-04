# How moving representations select an unseen-input function

Root derivation, 2026-09-30. This concerns only the intrinsic q=1 model in this study. The mechanism was also present as a limiting projection identity in the independently frozen PREDICTOR_ROUTE.md; after that freeze, root supplied the moving-projector law and cubic-onset computation to its author for checking. The provenance is shared, not a blind independent duplication of the complete result. No dense-training comparison or further compression objective is involved.

## 1. The training-visible subspace

Let g_a(t) in R^n be the second-layer population on training input a, and write G(t)=[g_1(t),...,g_m(t)]. The readout satisfies

\[
f_a=\frac{w^Tg_a}{n},\qquad
\dot w=-\frac2m\sum_a(f_a-y_a)g_a.
\tag{1}
\]

Let P(t) be Euclidean orthogonal projection onto the column span S(t) of G(t). On any interval of constant rank, P is differentiable whenever G is differentiable. For full column rank, P=G(G^TG)^{-1}G^T directly proves this; for other constant ranks, select a locally independent column basis. Define w_perp=(I-P)w. Since wdot lies in S(t),

\[
\frac{d}{dt}w_\perp=-\dot P\,w.
\tag{2}
\]

Every current training output is insensitive to w_perp because G^Tw_perp=0. Nevertheless w_perp can affect any query whose g(t,x) has a component in that direction. Equation (2) says that movement of the training-feature subspace is precisely the source of this component. Readout updates alone cannot create it while the span is fixed. A nonzero Pdot need not create it: Pdot w may vanish. Equation (2) is conditional on constant rank locally, not across arbitrary rank changes.

This is a statement about visibility to the **current linear readout**. Changing w_perp can change later hidden-feature evolution, since the hidden equations use w. Thus this is not a dynamically decoupled or unidentifiable state direction. Its invisibility concerns current training predictions, and at an interpolating equilibrium it remains unconstrained by those predictions.

## 2. Exact decomposition of the final function

Suppose the q=1 trajectory converges to a finite interpolating state. Let G_* contain its final training features, and P_* project onto their span. Put

\[
K_*=G_*^TG_*/n,\qquad
k_*(x)=G_*^Tg_*(x)/n.
\]

Since G_*^Tw_*/n=y, elementary orthogonal decomposition gives

\[
w_*=nG_*(G_*^TG_*)^\dagger y+(I-P_*)w_*.
\]

The first term is the unique smallest-Euclidean-norm readout interpolating y with these fixed final features. Proof: it belongs to range(G_*), solves the interpolation equations because y belongs to range(G_*^T), and every other solution differs by a vector orthogonal to that range. Pythagoras then minimizes the norm.

Therefore the entire fitted function has the exact decomposition

\[
f_*(x)=k_*(x)^TK_*^\dagger y
+\frac{g_*(x)^T(I-P_*)w_*}{n}.
\tag{3}
\]

The second term vanishes at every training input. It need not vanish elsewhere. No generic nonzero final value is asserted merely from (3).

If the trajectory has finite total residual activity, integral rho dt<infinity, the bounded-activation equations give finite total variation of w. Integrating (1) and projecting yields

\[
(I-P_*)w_*=-\frac2m\sum_a\int_0^\infty
r_a(s)(I-P_*)[g_a(s)-g_a(*)]ds.
\tag{4}
\]

The same formula at finite t uses P(t), the finite integral, and g_a(t). It follows directly from w(0)=0; subtraction of g_a(*) is legitimate because P_* fixes those vectors. For the limiting formula, absolute integrability follows from ||g_a||<=sqrt(n) and mean|r_a|<=rho.

In particular

\[
\frac{\|(I-P_*)w_*\|}{\sqrt n}
\le2\int_0^\infty\rho(s)
\left[\frac1m\sum_a\frac{\|g_a(s)-g_a(*)\|^2}{n}\right]^{1/2}ds.
\tag{5}
\]

Use the triangle inequality, then Cauchy--Schwarz over samples. This identifies the relevant history: residuals while the representations are still different from their final positions. It does not show that the path-dependent term improves test accuracy.

## 3. This motion occurs in the actual initialized q=1 system

Assume G(0) has full column rank. The q=1 initialization gives w(0)=v_a(0)=0, k_a(0)=h_a(0), so A'(0)=v_a'(0)=k_a'(0)=0 and G'(0)=0. Because rho(0)=1, the finite-dimensional vector field is analytic near zero. Define

\[
b(t)=\frac1m\sum_a y_a g_a(t),\qquad
C(t)=\frac1m\sum_a g_a(t)g_a(t)^T/n.
\]

Equation (1) becomes wdot=2b-2Cw. Here b'(0)=C'(0)=0. Taylor differentiation gives

\[
w(t)=2t b_0-2t^2 C_0b_0+
t^3\left[\frac13 b''_0+\frac43 C_0^2b_0\right]+O(t^4).
\tag{6}
\]

Since P(t)b(t)=b(t), differentiating twice at zero yields P''_0 b_0=(I-P_0)b''_0. Also P'_0=0, because P is a smooth function of G and G'_0=0. The vectors b_0,C_0b_0,C_0^2b_0 all lie in S(0). Multiplying (6) by I-P(t) consequently gives

\[
(I-P(t))w(t)
=-\frac23t^3(I-P_0)b''_0+O(t^4).
\tag{7}
\]

This is a realized-trajectory statement, not a freely chosen rotating-feature example. The coefficient can vanish in a special configuration. The following actual q=1 instance makes it nonzero.

## 4. An explicit two-neuron circle example

Take m=1,n=2,d=2, training input x_*=sqrt(2)(1,0), label y=1, W0=I_2, and A0=diag(a_1,a_2), with a_1,a_2>0. At the training input this diagonal choice would give h_2=0, so instead choose

\[
A_0=\begin{pmatrix}a_1&0\\a_2&1\end{pmatrix},
\qquad 0<a_1<a_2.
\]

Then h_i=tanh(a_i) satisfy 0<h_1<h_2<1, and g_i=tanh(h_i)>0. Denote H=(h_1^2+h_2^2)/2. Direct differentiation of the stated q=1 equations gives

\[
\frac{g_i''(0)}{g_i(0)}
=4(1-g_i(0)^2)^2\left[(1-h_i(0)^2)^2+H\right].
\tag{8}
\]

For completeness, w'_0=2g, d'_0=2g odot(1-g^2), v''_0=4g odot(1-g^2), and

\[
h''_0=4(1-h^2)^2\odot[g\odot(1-g^2)].
\]

The derived mixer B=W0+v k^T/n has B''_0=v''_0 h^T/n. Thus z''_0=h''_0+v''_0 H, and g''_0=(1-g^2) odot z''_0, which proves (8). Holding the common H fixed, the right side is strictly decreasing in h_i in (0,1). Therefore g''_0 is not parallel to g_0, so (I-P_0)b''_0 is nonzero. Equation (7) proves that the actual q=1 readout develops a component invisible on its training example at order t^3.

It affects a concrete unseen circle point. At x=sqrt(2)(0,1), the initial second-layer feature is (0,tanh(tanh(1))). Any nonzero vector perpendicular to g_0, whose first coordinate is positive, has a nonzero second coordinate. Thus its dot product with this query feature is nonzero. By continuity, for sufficiently small positive time the extra term g_t(x)^T(I-P_t)w(t)/n is nonzero, of order t^3. At that same time it vanishes exactly on the training example.

Although the displayed W0 and A0 are deterministic, the strict nonzero coefficients persist on an open neighborhood. Independent nondegenerate Gaussian initializations have positive probability in that neighborhood. This proves a nonexceptional possible mechanism under the stipulated law; no high-probability large-width claim or nonzero final-endpoint claim is inferred from it.

## 5. Scope and interpretation

There are two coupled selection effects. Feature evolution changes the final kernel K_* itself; rotation of the feature span can also leave a history-dependent readout component beyond that kernel's minimum-norm interpolation. Formula (3) separates them. A comparison of final kernels alone can therefore miss a part of the selected whole-input function.

These statements do not supply a unique endpoint from the labels, a max-margin principle, a beneficial generalization theorem, or proof that every multi-sample task fits. They do identify an exact causal mechanism absent from a stationary feature span, and exhibit it in a directly reachable q=1 trajectory. The natural next question is whether this component is systematic or negligible in particular circle tasks, and how its sign and size depend on the memory-driven movement of g. No experiments have been run here.

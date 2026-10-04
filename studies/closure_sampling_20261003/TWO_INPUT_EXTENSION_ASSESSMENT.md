# Bounded assessment of two canonical training inputs

2026-10-03. Scoped theoretical follow-up to the one-input complex-activity
route. Inputs were the supervisor's assignment, the canonical manuscript
model already read, and `COMPLEX_ACTIVITY_ROUTE.md` at SHA-256
`3190cbcef13c3089b2a475c297e9333e98ce3c01f69a686bde217cf87f193fe4`.
No other studies, experiments, or Git operations were used. The canonical
notation/neural reference, rigorous-proof, and adversarial-audit skills were
applied. This is an assessment, not a completed two-input compression theorem.

**Result of this bounded attempt:** for two orthogonal inputs, the same exact
first-layer coordinate change removes the carrier from the Euclidean
Jacobian of each activity vector field. However, the two activity vector
fields do not commute, almost surely at canonical initialization. The actual
state therefore cannot be represented as a path-independent function of the
two accumulated activities satisfying the proposed pair of activity PDEs.
For nonorthogonal, noncollinear inputs, an additional local obstruction
prevents simultaneously straightening the two first-layer gate directions.
These are obstructions to direct extensions of the current proof route, not
impossibility results for finite canonical two-input compression.

## 1. Exact two-input equations

Let the fixed normalized inputs be \(v_a=x_a/\sqrt d\in\mathbb R^d\),
\(a=1,2\), with \(\|v_a\|_2=1\). Define
\[
 a_a=Av_a,\quad h_a=\tanh a_a,\quad z_a=Wh_a,
 \quad g_a=\tanh z_a,\quad
 \delta_a=w\odot\operatorname{sech}^2z_a,
 \quad k_a=W^\top\delta_a,
 \quad f_a=w^\top g_a/n.
\]
The label vector is \((y_1,y_2)\), the loss is
\(\mathcal L=\tfrac12\sum_{a=1}^2(f_a-y_a)^2\), and define the signed
residual coefficients \(c_a=y_a-f_a\). With the canonical mobilities,
the exact physical equations are
\[
 \dot A=\sum_{b=1}^2c_b
       (\operatorname{sech}^2a_b\odot k_b)v_b^\top,
 \quad \dot W=\frac1n\sum_{b=1}^2c_b\delta_bh_b^\top,
 \quad\dot w=\sum_{b=1}^2c_bg_b.                             \tag{1}
\]
Thus, writing \(G_{ab}=v_a^\top v_b\),
\[
 \dot a_a=\sum_{b=1}^2c_bG_{ab}
                    \operatorname{sech}^2a_b\odot k_b.      \tag{2}
\]
These factors include the \(2/m=1\) normalization for two samples.
The quantities \(s_a(t)=\int_0^t c_a(u)\,du\) are signed accumulated
activities. Individual residuals need not retain their signs in a coupled
two-output gradient flow, so these variables must not automatically be
treated as monotone clocks.

## 2. Orthogonal inputs: exact carrier removal survives

Assume \(G=I_2\). Set, componentwise,
\[
 F(\alpha)=\alpha/2+\sinh(2\alpha)/4,
 \quad u_a=F(a_a),\quad h_a=\sigma(u_a),
 \quad\sigma=\tanh\circ F^{-1},\quad H=\sqrt n\,W.
\]
The inverse and its fixed complex strip are proved in the one-input route.
Equation (2) now gives exactly
\[
 d u_a=k_a\,d s_a,
 \qquad dH=\sum_{a=1}^2\frac{\delta_ah_a^\top}{\sqrt n}\,d s_a,
 \qquad dw=\sum_{a=1}^2g_a\,d s_a.                           \tag{3}
\]
Let \(\Theta=(u_1,u_2,H,w)\). For \(a=1,2\), denote by
\(V_a(\Theta)\) the vector field whose \(u_a\) block is \(k_a\), whose
other \(u\) block is zero, and whose \(H,w\) blocks are
\(\delta_ah_a^\top/\sqrt n,g_a\). Then (3) means
\[
 \dot\Theta=c_1(\Theta)V_1(\Theta)
                            +c_2(\Theta)V_2(\Theta).        \tag{4}
\]
On fixed pole-safe strips, with \(\|W\|_{\rm op}\le K\) and bounded
readout maximum, each \(DV_a\) has a width-independent operator bound in
the ordinary product Euclidean/Frobenius norm. To check this, replace the
single \(u\) in Section 3 of the complex route by the active \(u_a\).
The identities
\[
 \Delta z_a=W\Delta h_a+\Delta H\,h_a^c/\sqrt n,
 \qquad
 \|\Delta h_a\|_2\le C\|\Delta u_a\|_2
\]
give exactly the same finite-difference estimates. No diagonal term
\(\operatorname{diag}(k_a)\) appears in \(DV_a\).

This is a useful proved structural fact. It does not by itself remove the
dependence of the controls \(c_a\) on the trained state.

## 3. The two activity fields do not commute

A tempting extension is to seek a holomorphic map \(\Theta(s_1,s_2)\)
on a two-dimensional activity rectangle satisfying
\[
 \partial_{s_1}\Theta=V_1(\Theta),\qquad
 \partial_{s_2}\Theta=V_2(\Theta).                           \tag{5}
\]
Equality of mixed derivatives would require
\(DV_2V_1-DV_1V_2=0\) on its image. This condition fails already at the
canonical initial state.

At \(w_0=0\), \(\delta_{a,0}=k_{a,0}=0\), and
\[
 V_1(\Theta_0)=(0,0,0,g_{1,0}),\qquad
 V_2(\Theta_0)=(0,0,0,g_{2,0}).
\]
Differentiating only in those readout directions gives the commutator
\[
 (DV_2V_1-DV_1V_2)_{u_1}
 =-W_0^\top(g_{2,0}\odot\operatorname{sech}^2z_{1,0}),
\]
\[
 (DV_2V_1-DV_1V_2)_{u_2}
 = W_0^\top(g_{1,0}\odot\operatorname{sech}^2z_{2,0}),
                                                               \tag{6}
\]
\[
 (DV_2V_1-DV_1V_2)_{H}
 =\frac{
 (g_{1,0}\odot\operatorname{sech}^2z_{2,0})h_{2,0}^\top
 -(g_{2,0}\odot\operatorname{sech}^2z_{1,0})h_{1,0}^\top}
 {\sqrt n},
 \qquad (DV_2V_1-DV_1V_2)_w=0.
\]
For canonical square Gaussian \(W_0\), invertibility holds almost surely:
its determinant is a nonzero polynomial of continuously distributed entries,
whose zero set has Lebesgue measure zero. Also \(h_{2,0}\ne0\) almost
surely, hence \(z_{2,0}=W_0h_{2,0}\ne0\) and \(g_{2,0}\ne0\).
The real gate \(\operatorname{sech}^2z_{1,0}\) is strictly positive in
each coordinate. Thus the \(u_1\) block in (6) is nonzero almost surely.

Therefore (5) has no \(C^2\), hence no holomorphic, solution on a
neighborhood of zero with the canonical initial state. Equivalently, applying
a short \(s_1\)-increment and then an \(s_2\)-increment differs at the
mixed second order from reversing them. The endpoints \((s_1,s_2)\) do
not record this ordering.

This does not prevent parameterizing the single actual training curve by
some scalar on a suitable interval. It prevents treating its endpoint
activities as independent commuting flow coordinates. An arbitrary extension
off the actual activity curve need not satisfy (5), but the present equations
then provide no theorem for that extension.

## 4. Why a single residual clock does not immediately repair the proof

One may use the nonnegative clock
\[
 \tau(t)=\int_0^t\rho(u)\,du,
 \qquad\rho=\sqrt{(c_1^2+c_2^2)/2}.
\]
Away from \(\rho=0\), its exact equation is
\[
 \frac{d\Theta}{d\tau}
      =\alpha_1(\Theta)V_1(\Theta)
                    +\alpha_2(\Theta)V_2(\Theta),
 \qquad\alpha_a=c_a/\rho.                                  \tag{7}
\]
The coefficients are bounded on the real trajectory, but their derivatives
contain division by \(\rho\), and the pair \((\alpha_1,\alpha_2)\) is
not generally determined at a zero residual state by cancellation of a common
scalar factor. In the one-input model that factor cancels exactly from the
entire vector field; (7) does not have that property. Real boundedness of the
\(\alpha_a\) is insufficient to assert their holomorphic continuation or
the required width-independent strip through the fitted endpoint.

Alternatively, keep the actual full controls \(c_a(t)\) as external
functions while deleting a neuron. This yields a useful deterministic
comparison, but its cavity depends on the omitted Gaussian direction through
those controls. The independent Gaussian pairings in the one-input proof
then no longer have their asserted conditional Gaussian law. Choosing the
cavity's own residual coefficients restores independence, while introducing
the control discrepancy into the comparison. A correct proof must quantify
that discrepancy; treating either choice as though it had both properties
would be circular.

The physical-time vector field in (4) remains locally width-independently
Lipschitz on the transformed pole-safe region. Indeed
\(\|Df_a\|\le C/\sqrt n\) while \(\|V_a\|\le C\sqrt n\), so
the extra rank-one term \(V_aDc_a\) has bounded norm. A crude Gronwall
bound nevertheless costs \(e^{Ct}\), rather than the small-total-activity
factor used in the one-input argument. At the logarithmically long physical
times needed for an \(n^{-1/2}\) residual, this becomes a power of width.
Recovering the residual-damping structure, or a sufficiently regular final
clock, is a genuine missing step; it is not supplied by (3).

## 5. A precise positive restricted extension

For two orthogonal inputs and fixed deterministic coefficients
\(\nu_1,\nu_2\), consider the auxiliary activity flow
\[
 \Theta'(s)=\nu_1V_1(\Theta(s))+\nu_2V_2(\Theta(s)),
 \qquad w(0)=0.                                             \tag{8}
\]
This is a single autonomous holomorphic vector field with bounded fixed
coefficients. The one-input complex-strip proof extends to (8), with constants
depending on \(|\nu_1|+|\nu_2|\): a deleted first-layer neuron has two
bounded activation controls \(h_{1,i},h_{2,i}\), so the deterministic column
discrepancy remains \(CT\); a deleted second-layer neuron contributes
\(\sum_a\nu_aW_{j,:}^\top\delta_{a,j}\), of norm \(CT\), so the row
state discrepancy remains \(CT^2\). Both references are autonomous and
independent of the omitted Gaussian vector. Gaussian grids require only a
finite union over the two sample indices. Their amplitude and derivative
bounds, the doubled pole-cap comparison, and the \(T^2M\) absorption are
unchanged up to fixed constants. This gives the same
\(c/\sqrt{\log(n/\varepsilon)}\) strip on a fixed short interval for
the auxiliary path (8).

The actual canonical gradient flow is (8) after one scalar reparameterization
only if its residual coefficient vector remains parallel to the fixed vector
\((\nu_1,\nu_2)\). That is an additional invariant-direction claim and
has not been proved; generic finite Gaussian initialization does not supply
it by symmetry. Exchangeability of the initialization distribution is not an
exact symmetry of an individual initialized network. Thus (8) is a positive
restricted lemma, explicitly not a replacement for the intended two-input
canonical training theorem.

## 6. Nonorthogonal inputs: a second obstruction

Suppose \(v_1,v_2\) are noncollinear and
\(\gamma=v_1^\top v_2\ne0\). Applying the separate transform
\(u_a=F(a_a)\) to (2) gives
\[
 \dot u_a=\sum_{b=1}^2c_bG_{ab}
       \frac{\operatorname{sech}^2a_b}
            {\operatorname{sech}^2a_a}\odot k_b.             \tag{9}
\]
The off-diagonal gate ratio is unbounded on real initialized coordinates,
and its derivative reintroduces carrier multipliers. Thus the bounded
Jacobian argument cannot be copied from the orthogonal case.

There is also an exact local reason why a coordinate map cannot simply
straighten both first-layer directions. For one neuron's parameter
\(p\in\operatorname{span}(v_1,v_2)\), define the gate vector fields
\[
 X_b(p)=\operatorname{sech}^2(v_b^\top p)\,v_b.
\]
Their scalar multipliers in training are \(c_bk_{b,i}\). A local
diffeomorphism sending both \(X_1,X_2\) to fixed independent coordinate
vectors would preserve their Lie bracket and would therefore require that
bracket to vanish. Direct differentiation, with \(\phi=\tanh\), gives
\[
 DX_2X_1-DX_1X_2
 =\gamma\big[
     \phi'(v_1^\top p)\phi''(v_2^\top p)v_2
    -\phi'(v_2^\top p)\phi''(v_1^\top p)v_1\big].           \tag{10}
\]
Because \(v_1,v_2\) are independent and \(\phi'\) never vanishes on
the real axis, this bracket vanishes only when both scalar \(\phi''\)
factors vanish, namely when \(v_1^\top p=v_2^\top p=0\).
It is therefore nonzero at a generic, and in particular almost every
Gaussian, initialized parameter. No local simultaneous constant-coordinate
straightening exists there. The orthogonal case \(\gamma=0\) is precisely
where this particular obstruction disappears.

This excludes one proposed type of change of coordinates. It does not
exclude nonconstant transformed coefficients, weighted estimates, another
regularity proof, or another compression construction.

## 7. Status and bottleneck

Proved here are the exact two-input equations; width-independent activity
field Jacobians for orthogonal inputs; noncommutation of the two activity
flows at canonical initialization; the fixed-direction auxiliary extension;
and the nonorthogonal first-layer straightening obstruction.

Still open is an unconditional fitting-to-endpoint complex regularity and
compression theorem for the actual two-input residual-driven canonical
network. The highest-leverage next mathematical obligation in the orthogonal
case is a cavity comparison that simultaneously preserves omitted-Gaussian
independence and controls the differing residual-direction paths on the
whole fitting interval. A proof using the true physical damping or a regular
alternative final clock could meet that obligation. This bounded assessment
does not supply it, and no real-carrier estimate or fixed-control surrogate
has been substituted for it.

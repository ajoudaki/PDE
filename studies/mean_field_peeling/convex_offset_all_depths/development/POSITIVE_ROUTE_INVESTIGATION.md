# Bounded positive-route investigation of the literal convex activation

Date: 2026-09-08. This is a theoretical subtask report, based on the canonical model and proofs in `activation_class_all_depths/MANUSCRIPT.md` and the initialized-conditioning calculation in `convex_offset_all_depths/REPORT.md`. No numerical experiments were performed and no existing manuscript was edited.

## Result and scope

I do **not** obtain the full global theorem for a fixed literal convex activation. I also obtain no counterexample to qualitative convergence at every separately fixed finite depth. The positive results are (i) explicit initialized geometry and nonaffinity for a concrete witness, (ii) an adaptation of the source method yielding a genuine fixed-depth **local** strong population and finite-algorithm theorem without a gain, and (iii) exact identification of the global inputs this adaptation does not supply.

The witness is

\[
 e=\tfrac14,\qquad \psi(z)=\tfrac14\arctan z,\qquad
 \phi(z)=\tfrac34(1+z)+\tfrac1{16}\arctan z.
\]

The target retains the three given inputs, binary labels, original Gaussian initialization, original raw metric, and actual raw GD step \(n^{-2}\). Depth is fixed before the width limit; the activation must remain independent of depth. An initialized kernel bound decreasing with depth is allowed in the qualitative target.

## 1. Strong initialized facts for the concrete witness

Write \(a=3/4\), \(M=13/16\), and let \(\sigma_\ell^2\) be the common initialized preactivation variance. Oddness of \(\arctan\) gives \(E\phi(\sigma G)=a\). The derivative satisfies

\[
 a\le\phi'(z)\le M<1.
\]

For independent copies \(X,X'\) of \(\sigma G\), the pointwise Lipschitz bound and its lower counterpart give

\[
 a^2\sigma^2\le\operatorname{Var}(\phi(\sigma G))
 \le M^2\sigma^2,
\]

using \(2\operatorname{Var}(f(X))=E(f(X)-f(X'))^2\). Consequently

\[
 a^2(1+\sigma_\ell^2)\le\sigma_{\ell+1}^2
 \le a^2+M^2\sigma_\ell^2,
 \qquad 1\le\sigma_\ell^2\le\frac{48}{29}.
\]

The interval claim follows by induction from \(\sigma_1=1\): its lower endpoint maps to at least \(2a^2>1\), and its upper endpoint is the fixed point of the upper affine recursion.

Let \(Q_\ell\) be the raw initialized feature Gram. The constant and linear Gaussian projections used in Part N apply with mean exactly \(a\) and linear coefficient at least \(a\). Thus

\[
 Q_1\succeq a^2(\Gamma+\mathbf1\mathbf1^T),\qquad
 Q_\ell\succeq a^2 Q_{\ell-1},\qquad
 Q_L\succeq\frac{\delta^2}{4}a^{2L}I_3>0.
\]

The upper bound from the existing convex report remains

\[
 \lambda_{\min}(Q_L)\le(1-\Gamma_{ij})M^{2L}.
\]

These bounds are compatible. The features are strictly independent at every fixed finite depth and poorly conditioned over increasing depths.

There is a useful difference from the large-gain setting: **initialized nonaffinity has a positive bound uniform in depth for this witness**. Define

\[
 J=\inf_{b,c}\int_{-1}^1[\psi(z)-b-cz]^2\,dz>0,
 \qquad c_0=\frac{e^{-1/2}J}{\sqrt{2\pi}}.
\]

Strict positivity follows because the arctangent is not affine on this interval. For \(1\le\sigma\le\sqrt{48/29}\), its Gaussian density on \([-1,1]\) is at least \(e^{-1/2}/(\sigma\sqrt{2\pi})\). Restricting each regression integral to this interval gives

\[
 \inf_{b,c}E[\phi(\sigma G)-b-c\sigma G]^2
 =e^2\mathcal R_\psi(\sigma G)
 \ge \frac{e^2c_0}{\sqrt{48/29}}>0.
\]

This is an initialized statement; all-time persistence is a separate obligation.

## 2. A local source theorem really does survive without the gain

This section applies to any normalized shape and \(0<e<1/2\), with \(a=1-e\). It works directly with the **raw** hidden fields, so no output normalization or altered metric occurs.

Use the controlled equations

\[
 C'=\sum_i c_i h_i^L,\quad
 A_\ell'=\sum_i c_i d_i^\ell\otimes h_i^{\ell-1},\quad
 w'=\sum_i c_i d_i^1u_i,\qquad \|c\|_1\le3,
\]

with \(q^L=C\), \(q^\ell=A_{\ell+1}^*d^{\ell+1}\), and

\[
 d=D_R(z,q)=a q+e\psi'(z)\tau_R(q).
\]

The elementary bounds are

\[
 |\phi(z)|\le|z|+1,\quad |\phi'|\le1,\quad
 |D_R|\le|q|,\quad |(D_R)_q|\le1,\quad
 |(D_R)_z|\le e|q|\le|q|,
\]

with \(|(D_R)_z|\le2eR\) at fixed cap. All coordinate hypotheses of Part F hold.

Set

\[
 F=32^L,\qquad S_L=10^{-12}2^{-20L}.
\]

Stop at hidden raw displacement one. The same elementary primal induction as Part S, now with smaller gate bounds, gives

\[
 \|h_i^\ell\|_2,\|z_i^\ell\|_2\le32^\ell,
 \quad \|C(s)\|_2\le3Fs,
 \quad \|q_i^\ell(s)\|_2\le Q_\ell:=3F32^{L-\ell}S_L,
\]

and

\[
 D(s)\le3\sqrt L F^2s^2.
\]

The chosen \(S_L\) makes the displacement much smaller than one and \(\max Q_\ell<1/2\). The usual first-proposed-exit argument applies to positive Euler meshes as well. These bounds precede all source estimates.

The exact local source equations remain

\[
 z=\xi+\mathcal A d,\qquad q=\zeta+\mathcal B h,
\]

with \(\mathcal A\) strict in time and \(\mathcal B\) causal. Write

\[
 h=a z+u,\quad |u|=|a+e\psi(z)|\le1,
 \qquad d=a q+v,\quad |v|\le|q|.
\]

For a local strict density \(\alpha\) and incoming row bound \(b\), put \(r=\alpha S_L b\). If \(r\le1/8\), the exact Gaussian elimination is

\[
 R=(I-a^2\mathcal A\mathcal B)^{-1},\quad
 P=(I-a^2\mathcal B\mathcal A)^{-1},
\]

\[
 z_G=R\xi+aR\mathcal A\zeta,
 \qquad q_G=P\zeta+a\mathcal B R\xi,
\]

\[
 z-z_G=R\mathcal A v+aR\mathcal A\mathcal B u,
 \qquad q-q_G=a\mathcal B R\mathcal A v+P\mathcal B u.
\]

The two Gaussian combinations use the **actual** coefficients and sources. Because \(a\le1\), all row estimates used in S.3 are at least as strong as before. Gaussian moments and absorption give

\[
 \|q\|_p\le20(Q_\ell+b)\sqrt p,\qquad
 \big\|\max_i|q_i|\big\|_p\le60(Q_\ell+b)\sqrt p.
\]

For the source Jacobian the exact equation is

\[
 J=I_\xi+\mathcal A[NJ+V(I_\zeta+\mathcal B GJ)],
 \quad G=\phi'(z),\ V=(D_R)_q,\ N=(D_R)_z.
\]

Here \(|G|,|V|\le1\) and \(|N|\le\max_i|q_i|\). The proof of S.4 therefore gives the same sufficient production inequalities

\[
 \alpha_{\ell+1,\mathrm{new}}\le3F^2+16\alpha_\ell,
 \qquad b_{\ell-1,\mathrm{new}}
 \le512(Q_\ell+b_\ell)+3S_L,
\]

provided \(\alpha_\ell S_Lb_\ell\le10^{-9}\) and
\(\alpha_\ell S_L60(Q_\ell+b_\ell)\le10^{-6}\).

An explicit closed box is

\[
 B_0=4F^2S_L,\qquad
 \alpha_\ell=3F^2 32^\ell,\qquad
 b_\ell=2048^{L-\ell+1}B_0.
\]

Indeed \(Q_\ell\le B_0\le b_\ell/2048\), while

\[
 \alpha_\ell S_L\le3\,2^{15L}S_L,
 \qquad \alpha_\ell S_Lb_\ell
 \le384\,2^{31L}S_L^2.
\]

Our \(S_L\) satisfies the preceding sufficient smallness conditions with strict slack. The production outputs lie strictly inside the next boxes, as in S.6. The chronological forward-then-reverse induction uses only completed coefficient rows; thus this is not an assumption about an unknown current row.

This yields cap- and mesh-uniform subGaussian incoming moments and integrable source-derivative envelopes throughout \([0,S_L]\) in controlled time.

For physical capped residual feedback set
\(v(t)=\int_0^t\|r(s)\|_1ds\). While \(v\le S_L\),

\[
 |f_i|\le\|C\|_2\|h_i^L\|_2\le3F^2S_L,
 \quad \|r\|_1\le3+9F^2S_L<4.
\]

Hence no exit from \(v<S_L\) occurs for \(0\le t\le S_L/4\). Fixed-cap local existence and bounded continuation give the capped paths on this interval.

Finally, the raw one-cap comparison is

\[
 |D_{R'}(z,q)-D_R(\bar z,\bar q)|
 \le |q-\bar q|+2eR|z-\bar z|
       +2e|\bar q|\mathbf1_{|\bar q|>R}.
\]

SubGaussian source tails beat the resulting \(\exp(C_TR)\) comparison factor. The proof of Part V therefore applies on this interval: there is a unique strong uncut population flow, unique continuation among bounded-primal competitors on the interval, and the actual finite GF/GD and all the stated compact-interval kernel, field, velocity and generated-probe observations converge. The finite random readout is retained before taking width to infinity, exactly as in V.3.

For the concrete witness, Part N now has the local strong solution needed to interpret its nonzero initial accelerations and kernel variation. Its assumption \(a>e>0\) holds. This supplies those local motion assertions without any claim of global existence.

## 3. Why the global clock does not follow from this local lemma

For true uncut GF, the exact energy identity is

\[
 \dot{\mathcal L}=-r^TKr=-\|\dot\theta\|_{\rm raw}^2.
\]

On any already-existing interval it gives

\[
 \int_0^T\|\dot\theta\|_{\rm raw}^2dt\le\tfrac32,
 \quad \|\theta(t)-\theta(0)\|_{\rm raw}\le\sqrt{3t/2}.
\]

These are valuable a priori bounds, but they neither construct a strong Hilbert-space extension nor imply an integrable residual clock. The loss has a continuous gradient by F.7; it has not been proved to have a locally Lipschitz gradient on every raw \(L^2\) ball. The problematic curvature multiplier is \(\phi''(z)q\). Bounded \(L^2\) primal norms alone also do not give uniform integrability of capped incoming fields.

Suppose, as an additional hypothesis, that \(Q_L(t)\succeq\mu_LI\) on an uncut path. Then positivity of all true hidden kernel blocks would give

\[
 \|r(t)\|_2\le\sqrt3e^{-\mu_Lt},
 \qquad \int_0^\infty\|r(t)\|_1dt\le3/\mu_L.
\]

Using the initialized lower bound as a proposed \(\mu_L\) makes this control budget grow exponentially with depth. The local source interval above decreases exponentially. No first-exit bootstrap closes from these two statements. This diagnoses the proof mismatch; it is not a lower bound on the actual residual clock and does not show failure of training.

A scalar time change cannot create the needed physical small-motion estimate: it rescales controlled vector fields as well as interval length and leaves their integrated displacements and feedback products unchanged. Normalizing hidden features by \(a^\ell\) with \(a<1\) makes the offset \(a^{1-\ell}\) grow. The fixed-depth transformed equations remain exact, but the old gain-based smallness inequalities do not survive.

The local source proof cannot simply be restarted at every small interval: after the first interval the readout is nonzero and the source transcript contains trained history. The zero-readout start that made all reverse response rows initially zero is gone. Finite source prefixes are well defined, but uniform cap/mesh response and tail bounds over successively longer prefixes remain to be proved.

## 4. Affine-reference and dissipativity routes examined

An exact affine reference must use \(\phi_0(z)=a(1+z)\), not the high-gain reference from the old theorem. Its initialized Gram can be computed explicitly:

\[
 Q_L^{\mathrm{aff}}=a^{2L}\Gamma+
       \left(\sum_{j=1}^L a^{2j}\right)\mathbf1\mathbf1^T.
\]

Thus the affine reference itself has vanishing contrast scales and an order-one common mode. Its full raw training dynamics need an independent global theorem before a nonlinear perturbation comparison could be useful.

The standard homogeneous deep-linear balance is not conserved here. For affine gates and internal layers \(2\le\ell<L\), direct differentiation of the actual raw updates gives

\[
 \frac d{dt}(A_\ell A_\ell^*-A_{\ell+1}^*A_{\ell+1})
 =\sum_i r_i\bigl(b_i^\ell\otimes\mathbf1_\ell
                 +\mathbf1_\ell\otimes b_i^\ell\bigr).
\]

To verify it, substitute
\(A_\ell h_i^{\ell-1}=h_i^\ell/a-\mathbf1_\ell\)
and \(A_{\ell+1}^*b_i^{\ell+1}=b_i^\ell/a\)
into the two derivatives. The terms involving \(h_i^\ell\)
cancel and leave precisely the displayed offset terms.
At the top the corresponding identity is

\[
 \frac d{dt}(A_LA_L^*-C\otimes C)
 =a\left(\sum_i r_i\right)
       (C\otimes\mathbf1_L+\mathbf1_L\otimes C).
\]

The right sides are signed and are not positive-semidefinite bounds. This does not rule out a different affine invariant or dissipativity mechanism. It does rule out silently importing the homogeneous balance identity into this model.

For the arctangent witness the decay of \(\psi''(z)\) is potentially useful. In a local source representation \(q=\zeta+\mathcal B h\), factors \(z\psi''(z)\) are bounded. But the \(\psi''(z)\zeta\) term and trained time-response coefficients remain. No cap-uniform global bound for those coefficients follows just from curvature decay. I did not close this route.

## 5. The remaining obligations, kept separate

1. **Global strong construction and finite-horizon width/GD limit:** extend cap-uniform source tails and response control to every physical horizon, or replace the cap argument by another fully justified strong compactness/uniqueness method. Energy bounds alone are insufficient for the existing proof.
2. **Training convergence:** show persistent trained coercivity, or another inequality that forces \(r(t)\to0\) and provides enough integrated control. Initialized coercivity and increasing kernel in one direction to second order do not establish this.
3. **All-time nonaffinity:** prevent the trained marginal laws from losing the positive affine-regression residual, including at limiting time. The initialized compact variance interval gives a good starting margin but no trained bound.
4. **Fixed activation over depth:** any nonlinear perturbation comparison must use one \(e>0\) for every finite \(L\), with all deterioration tracked explicitly. Choosing \(e=e_L\), normalizing a gain theorem after the fact, or freezing hidden training changes the target.

The highest-leverage unresolved statement is a trained coercivity/dissipativity estimate for this exact offset architecture in its raw metric. The affine reference is a plausible research route, but even its offset-sensitive global argument is absent here. The initialized-conditioning collapse alone cannot decide the qualitative target.

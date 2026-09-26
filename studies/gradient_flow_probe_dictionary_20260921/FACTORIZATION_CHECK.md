# Independent factorization and probe-basis check

## Input scope and status

This was an independent, prompt-only algebra check. The scientific input was the supervisor's assignment: equal hidden width (n); ordinary multiplication by the physical hidden matrix (W_2); normalized vector pairing (u^Tv/n) and outer-product update (uv^T/n); frozen bases (B_\ell^TB_\ell/n=I); compressed matrix (B_2MB_1^T/n); and the two-probe fields and proposed generators reproduced below. The assignment requested verification of initialization, projected gradient flow, coefficient mobility, trainable count, forward/adjoint preservation, and the distinction between cubic tensor-factor inclusion and complete closed-flow jet agreement. A follow-up authorized this report and requested the finite-width/population distinction.

The solve-math-rigorously skill was read. No repository scientific sources, study history, external sources, or other reviewers' findings were read. Thus this report establishes the algebra stated here; it does not certify unstated network mobilities, readout initialization, or jet identities from another document.

## Factorization, initialization, and mobility

Write (W=W_2), (h=h_1), (\delta=c\odot\phi'(Wh)), and suppose the output and loss are

\[
f=\frac1n c^T\phi(Wh),\qquad
\mathcal L=\sum_s\omega_s(f_s-y_s)^2.
\]

Then physical unit-mobility Euclidean gradient flow is

\[
\dot W=-\nabla_W\mathcal L
=-2\sum_s\omega_s r_s\frac{\delta_s h_s^T}{n}.
\]

Set (P_\ell=B_\ell B_\ell^T/n) and (J(M)=B_2MB_1^T/n). The base normalization makes (P_\ell) orthogonal projectors. Moreover,

\[
\langle J(A),J(C)\rangle_F
=\frac1{n^2}\operatorname{tr}
\big(A^TB_2^TB_2CB_1^TB_1\big)
=\operatorname{tr}(A^TC).
\]

Thus (J) is a Frobenius isometry, its adjoint is (J^*(G)=B_2^TGB_1/n), and the orthogonal projected initialization is exactly

\[
M_0=\frac1nB_2^TW_0B_1,\qquad
J(M_0)=P_2W_0P_1.
\]

For (a_s=B_1^Th_s/n) and (d_s=B_2^T\delta_s/n), differentiation through (J) gives

\[
\nabla_M\mathcal L=2\sum_s\omega_s r_s d_sa_s^T.
\]

Consequently,

\[
\dot M=-2\sum_s\omega_s r_s d_sa_s^T,
\qquad
J(\dot M)=-P_2(\nabla_W\mathcal L)P_1.
\]

**The coefficient mobility is 1, not (n).** This is the projection of the physical gradient evaluated at the current compressed network. It does not mean that projecting an independently evolving unrestricted network produces the same closed trajectory.

With a full trainable (W_1\in\mathbb R^{n\times d}) and readout (c\in\mathbb R^n), and no additional parameters, the count is (nd+n+K_1K_2). Frozen basis entries are not trainable parameters. This count does not account for the work or temporary storage used to construct the bases from a dense initializer.

## Exact initial probe identities

For (a,b\in\{1,2\}), the supplied fields are

\[
\begin{aligned}
h_a&=\tanh(g_a/\sqrt2),&Y_a&=W_0h_a,&H_a&=\tanh Y_a,\\
D_a&=1-H_a^2,&U_{ab}&=D_aH_b,&Q_{ab}&=W_0^TU_{ab},\\
L_{ab}&=(1-h_a^2)^2Q_{ab},&&&F_{ab}&=2vU_{ab}+W_0L_{ab},
\end{aligned}
\]

where products and squares of fields are pointwise and (v=\mathbb E h_a^2).

Let the lower span contain (1,h_a,Q_{ab},L_{ab}) and the upper span contain (1,Y_a,H_a,U_{ab},W_0L_{ab}). Their dimensions are at most 11 and 13, respectively, before accounting for dependencies and the cap (n). For (\widehat W_0=P_2W_0P_1), one has exactly

\[
\widehat W_0h_a=Y_a,\qquad
\widehat W_0^TU_{ab}=Q_{ab},\qquad
\widehat W_0L_{ab}=W_0L_{ab}.
\]

For example, the adjoint identity is

\[
P_1W_0^TP_2U_{ab}=P_1Q_{ab}=Q_{ab};
\]

the two forward identities follow by the same two projection steps. Also (F_{ab}) is in the upper span. These operator-call identities are exact finite-dimensional facts and require no population Gram identity.

They do not guarantee arbitrary-input equality. For a new (h(x)), neither (h(x)\in\operatorname{ran}P_1) nor (W_0h(x)\in\operatorname{ran}P_2) is assured. Nor do they preserve every possible initial adjoint: for arbitrary nonzero (c_0), the field (c_0D_a) and its adjoint image need not belong to these spans. The interpretation of (U_{ab}) as the leading adjoint factors normally uses zero initial readout and a readout derivative in the span of the (H_b).

## Cubic velocity: what the extra upper generators establish

Here is the conditional Taylor calculation underlying the proposed extension. Assume zero initial readout and write ordinary Taylor coefficients as

\[
\begin{aligned}
c(t)&=tc_1+t^2c_2+t^3c_3+O(t^4),\\
h_a(t)&=h_a+t^2\ell_a+O(t^3),\\
z_{2,a}(t)&=Y_a+t^2f_a+O(t^3).
\end{aligned}
\]

Suppose the relevant network equations imply (\ell_a\in\operatorname{span}_bL_{ab}), (f_a\in\operatorname{span}_bF_{ab}), and readout flow (\dot c=\sum_b\alpha_b(t)\phi(z_{2,b}(t))), where (\alpha_b=-2\omega_br_b). Writing (\alpha_b(t)=\alpha_{b,0}+t\alpha_{b,1}+t^2\alpha_{b,2}+\cdots) gives

\[
c_1=\sum_b\alpha_{b,0}H_b,\quad
c_2=\frac12\sum_b\alpha_{b,1}H_b,\quad
c_3=\frac13\sum_b\big(\alpha_{b,2}H_b+\alpha_{b,0}D_bf_b\big).
\]

Therefore the adjoint factor has expansion

\[
c(t)\phi'(z_{2,a}(t))
=tD_ac_1+t^2D_ac_2
+t^3\big(D_ac_3+\phi''(Y_a)f_ac_1\big)+O(t^4).
\]

The first two coefficients lie in the span of (U_{ab}). The third lies in the span of those fields and

\[
D_aD_bF_{bc},\qquad H_c\phi''(Y_a)F_{ab},
\qquad a,b,c\in\{1,2\}.
\]

In the full cubic coefficient of

\[
\dot W(t)=\sum_a\alpha_a(t)
\frac{[c(t)\phi'(z_{2,a}(t))]h_a(t)^T}{n},
\]

the lower factor is either (h_a) or (\ell_a), so the lower base already contains it. Thus these 16 extra upper generators suffice for **population-derived tensor-factor inclusion under the stated jet assumptions**, giving (K_1\le11), (K_2\le29), and at most (nd+n+319) trainable parameters.

Tensor-factor inclusion says that orthogonally projecting the true middle-layer velocity coefficients through degree three leaves them unchanged. Agreement with the independently evolving compressed flow additionally requires verifying its lower-order Taylor recursion: the same (c_1,c_2,c_3), (\ell_a), (f_a), and residual coefficients must actually be produced. The initial identities above supply important operator calls for that verification, but the omitted input Gram, first-layer mobility, and readout initialization cannot be reconstructed from the generator list. A middle-layer statement must also compare increments (W(t)-W_0), or projected trajectories; the dense and compressed initial matrices generally differ.

A full-state claim needs further checks. For example, a cubic first-layer velocity can involve (W_0^TR) for one of the new upper fields (R). Exact initial compression of this call requires (W_0^TR) in the lower span, which the 11 generators do not guarantee. Later forward jets can require the pointwise-transformed lower fields and their (W_0)-images as well. The full-state order being claimed must be specified.

## Finite width versus population

The use of (F_{ab}=2vU_{ab}+W_0L_{ab}) as a paired second forward-jet generator depends on the population simplifications and network scalings that produce that coefficient. At finite width, put (C_{ab}=h_a^Th_b/n). Even for independent centered initialized probe fields, their realized Gram matrix need not equal (vI).

For example, an initial middle-layer acceleration term (U_{bc}h_b^T/n), when applied to probe (h_a), contributes (C_{ba}U_{bc}). Population orthogonality removes the terms with (b\ne a) and replaces (C_{aa}) by (v); a finite realization does neither exactly. The initial basis still preserves every (U_{bc}) and (W_0L_{bc}) individually, but the particular 16 product generators above can rely on population coefficient pairings. An exact finite-width cubic claim therefore needs actual empirical second-jet generators, or a larger product dictionary with an independently verified spanning argument. Taking (n) large gives an approximation, not an exact finite-width identity.

## Ridge and orthonormalization

Exact orthonormalization on the nonzero singular subspace preserves the span and all stated identities. Ridge whitening without a subsequent correction generally does not satisfy (B_\ell^TB_\ell/n=I); using the unit-Gram formulas anyway introduces distortion.

For full-column-rank bases, set (S_\ell=B_\ell^TB_\ell/n). The correct orthogonal projectors and coefficient initialization are

\[
P_\ell=\frac1nB_\ell S_\ell^{-1}B_\ell^T,
\qquad
M_0=S_2^{-1}\left(\frac1nB_2^TW_0B_1\right)S_1^{-1}.
\]

The coefficient metric is (\langle A,C\rangle=\operatorname{tr}(A^TS_2CS_1)), so physical projected gradient flow is

\[
\dot M=-S_2^{-1}(\nabla_M\mathcal L)S_1^{-1}.
\]

Thus ridge can be compensated by the actual Gram metric, or avoided by exact rank-revealing orthonormalization. An uncorrected ridge projector shrinks represented directions and does not exactly preserve the probe calls.

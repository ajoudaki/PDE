# Explicit physical fitting for the corrected autonomous compressor

2026-10-04. Coordinator bridge, awaiting separate reconstruction. Inputs:
the complete `closure_sampling_20261003/STORAGE_QUADRATIC_IMPROVEMENT.md`,
`GENERAL_WEIGHTED_COMPARISON.md`, and `ACTIVATION_CLASS_EXTENSION_ROUTE.md`;
the current study's explicit Gaussian initialization theorem. This note
makes the independent real fitting and endpoint constants numerical for
unbounded activation values. It does not estimate Gaussian fluctuations.

## 1. Exact finite autonomous model

Let \(v_a=x_a/\sqrt d\) have unit norm, \(Y=\|y\|_2/\sqrt m\),
\(\gamma=\lambda_{\min}(Q_L)>0\), and \(\lambda=\gamma/m\).
The source-selection construction provides, for each layer, a positive
metric \(M_\ell\), a positive diagonal metric \(\mathsf D_\ell\), and an exact
isometry on the source space, with
\[
\mathsf D_\ell/4\preceq M_\ell\preceq\mathsf D_\ell,\qquad
\|\mathbf1\|_{M_\ell}=1,\quad\|\mathbf1\|_{\mathsf D_\ell}\le2.
\tag{1}
\]
Original first-weight columns and initialized training features and their
paired initialized mixer images belong to those spaces exactly. Therefore
the selected initial first-weight operator is at most eight, the selected
initial hidden operators are at most eight, and the initialized normalized
training Gram is exactly the original one. On the explicit Gaussian event
in `GENERAL_EXPLICIT_FITTING.md`, it is at least \(\lambda I/2\).
These are deterministic consequences of the selection interface.

The moving variables are \((A,B^2,\ldots,B^L,w,c)\), with \(w(0)=0\),
\(c(0)=y\), and the exact selected initial arrays. Forward evaluation is
\[
z^1(v)=Av,\quad z^\ell(v)=B^\ell h^{\ell-1}(v),\quad
h^\ell(v)=\phi_\ell(z^\ell(v)).
\]
Let \(\mathsf H=[h^L(v_a)]_a\), \(Q=\mathsf H^{\mathsf T}M_L\mathsf H\).
The effective readout and actual predictor are
\[
\widehat w=w+\mathsf H Q^{-1}
(y-c-\mathsf H^{\mathsf T}M_Lw),\qquad
f_C(v)=\widehat w^{\mathsf T}M_Lh^L(v).
\tag{2}
\]
Thus \(c_a=y_a-f_C(v_a)\) exactly. Define
\[
k_a^L=\widehat w,\quad
\delta_a^\ell=\phi_\ell'(z_a^\ell)\odot k_a^\ell,\quad
k_a^\ell=(B^{\ell+1})^*\delta_a^{\ell+1},\qquad
(B^{\ell+1})^*=M_\ell^{-1}(B^{\ell+1})^{\mathsf T}M_{\ell+1}.
\]
Use the Gram matrix
\[
K_{ab}=\langle h_a^L,h_b^L\rangle_{M_L}
+\langle\delta_a^1,\delta_b^1\rangle_{M_1}v_a^{\mathsf T}v_b
+\sum_{\ell=2}^L
\langle\delta_a^\ell,\delta_b^\ell\rangle_{M_\ell}
\langle h_a^{\ell-1},h_b^{\ell-1}\rangle_{M_{\ell-1}}.
\tag{3}
\]
The autonomous equations are
\[
\dot A=\frac2m\sum_a c_a\delta_a^1v_a^{\mathsf T},\quad
\dot B^\ell=\frac2m\sum_a c_a\delta_a^\ell
(h_a^{\ell-1})^{\mathsf T}M_{\ell-1},\quad
\dot w=\frac2m\sum_a c_ah_a^L,\quad \dot c=-2Kc/m.
\tag{4}
\]
All hidden arrays train. The backward signals and \(K\) are the specified
optimizer, not gradients in a non-diagonal metric. No trajectory or external
residual is supplied to (2)–(4).

## 2. Numerical label condition and conclusion

Assume real \(C^2\) activations with bounded first two derivatives and put
\(b=\max_\ell|\phi_\ell(0)|\),
\(s=\max(1,\max_\ell\|\phi_\ell'\|_\infty)\).
No activation-value bound is used. Define
\[
H_1=\max(1,2b+16s),\qquad
H_\ell=\max(1,2b+18sH_{\ell-1}),\qquad H=H_L,
\]
\[
D_\ell=2s(18s)^{L-\ell},\quad U_1=D_1,\quad
U_\ell=2HD_\ell\ (\ell\ge2),
\quad F_1=2sU_1,\quad F_\ell=2s(2HU_\ell+9F_{\ell-1}),\quad F=F_L.
\tag{5}
\]
The \(D_\ell\) in (5) are scalar response bounds.

For
\[
\boxed{Y\le\frac{\gamma}{16mH\sqrt F},}
\tag{6}
\]
the model exists uniquely for all time, its raw and effective parameters
converge, and it fits every training label. Put \(R=5Y/\sqrt\lambda\).
On the stated initial event, for all \(t\ge0\),
\[
\rho_C:=\|c\|_2/\sqrt m\le Ye^{-\lambda t/2},\quad
Q/m\succeq\lambda I/4,\quad
\sup_{\|v\|=1,\ell}\|h^\ell(t,v)\|_{M_\ell}<2H,
\]
\[
\|A(t)\|_{\mathbb R^d\to M_1}<9,\quad
\|B^\ell(t)\|_{M_{\ell-1}\to M_\ell}<9,
\quad\|w(t)\|_{M_L}\le2Y/\sqrt\lambda,
\quad\|\widehat w(t)\|_{M_L}\le R.
\tag{7}
\]

## 3. Proof of the independent fitting bound

Metric comparison gives, for real inputs,
\[
\|\phi_\ell(z)\|_{M_\ell}\le2b+2s\|z\|_{M_\ell},\quad
\|\phi_\ell(z)-\phi_\ell(z')\|_{M_\ell}
\le2s\|z-z'\|_{M_\ell},
\]
and every coordinate gate has operator norm at most \(2s\).
Thus (5) bounds all initialized query features by \(H\), and bounds
backward responses by \(D_\ell\|\widehat w\|_{M_L}\) in the stopped
operator tube. The Gaussian feature moment bound implies \(\lambda\le H^2\):
the scalar moment recursion is dominated by (5).

Use the raw parameter norm
\[
\|\theta\|_{\rm par}^2=\operatorname{tr}(A^{\mathsf T}M_1 A)
+\sum_{\ell=2}^L\|M_\ell^{1/2}B^\ell M_{\ell-1}^{-1/2}\|_F^2
+w^{\mathsf T}M_Lw.
\]
Expansion of the velocities, including cross-sample terms, gives exactly
\[
-\frac d{dt}\rho_C^2=4c^{\mathsf T}Kc/m^2
=\|\dot\theta\|_{\rm par}^2.
\tag{8}
\]
Also \(K\succeq Q\), since every term in (3) is a Gram matrix.
Stop at normalized Gram margin \(\lambda/4\), operator caps nine, and
query-feature cap \(2H\). Then \(-\dot\rho_C\ge\lambda\rho_C/2\).
Equation (8) implies
\[
\int_0^t\|\dot\theta\|_{\rm par}\,ds\le2Y/\sqrt\lambda,
\qquad \int_0^t\rho_C\,ds\le2Y/\lambda.
\tag{9}
\]
For the first inequality, pointwise
\(\|\dot\theta\|=\sqrt{2\rho_C(-\dot\rho_C)}
\le2(-\dot\rho_C)/\sqrt\lambda\).

Write \(P=\mathsf H Q^{-1}\mathsf H^{\mathsf T}M_L\), the
\(M_L\)-orthogonal training-feature projector. Formula (2) gives the
orthogonal sum
\(\widehat w=(I-P)w+\mathsf H Q^{-1}(y-c)\).
Its two squared norms are at most \(4Y^2/\lambda\) and
\(16Y^2/\lambda\), respectively. Consequently
\(\|\widehat w\|\le\sqrt{20}Y/\sqrt\lambda<R\).
The hidden block velocities have norm at most \(2\rho_C R U_\ell\).
After integration, all block displacements and sphere feature displacements
are bounded respectively by
\[
20U_\ell Y^2/\lambda^{3/2},\qquad
20F_\ell Y^2/\lambda^{3/2}.
\tag{10}
\]
The feature bound uses the subtraction recurrence with gate constant
\(2s\), matrix bound nine, and query feature bound \(2H\), exactly
as in (5). Under (6), these are at most
\(5\sqrt\lambda/(64H^2)<\sqrt\lambda/8\) and at most \(1/(8H)\).
Thus operators improve below \(8+1/8\), features below \(H+1/8<2H\),
and the normalized top feature matrix's smallest singular value stays
above \((1/\sqrt2-1/8)\sqrt\lambda>\sqrt\lambda/2\).
All stopped margins improve strictly, proving (7).

At fixed selected dimensions, raw bounded parameters, bounded \(c\),
and the positive Gram gap imply continuation. Equation (9) proves raw
parameter convergence; (2) and the retained Gram gap then prove convergence
of the effective readout. The limit fits because \(c\to0\).

## 4. Explicit whole-sphere endpoint tail

Define
\[
G=4H^2+R^2\left[D_1^2+4H^2\sum_{\ell=2}^L D_\ell^2\right],
\qquad B_w=4H+48RFY/\lambda+4G/\sqrt\lambda,
\qquad B_f=2HB_w+2R^2F.
\tag{11}
\]
Then
\[
\boxed{\sup_{\|v\|=1}|f_C(\infty,v)-f_C(t,v)|
\le\frac{2B_fY}{\lambda}e^{-\lambda t/2}.}
\tag{12}
\]
Here is a direct proof with no minimum-weight dependence. Let
\(V=\mathsf H/\sqrt m\), \(q=V^*V\), \(T=Vq^{-1}\),
\(P=TV^*\), \(b_c=(y-c)/\sqrt m\). Then
\(\widehat w=(I-P)w+Tb_c\), \(\|T\|\le2/\sqrt\lambda\),
\(\|\dot V\|\le2RF\rho_C\), \(\|b_c\|\le2Y\).
Differentiating the inverse and collecting the projectors gives
\[
\dot T=(I-P)\dot Vq^{-1}-T\dot V^*T,\quad
\dot P=(I-P)\dot VT^*+T\dot V^*(I-P).
\]
Thus \(\|\dot T\|\le8\|\dot V\|/\lambda\) and
\(\|\dot P\|\le4\|\dot V\|/\sqrt\lambda\).
The actual Gram satisfies \(\|K/m\|\le G\), so
\(\|\dot b_c\|\le2G\rho_C\); also \(\|\dot w\|\le4H\rho_C\).
Substituting these inequalities into the differentiated readout gives
\(\|\dot{\widehat w}\|\le B_w\rho_C\).
For every query, \(\|\dot h^L(v)\|\le2RF\rho_C\) and
\(\|h^L(v)\|\le2H\). Hence \(|\dot f_C(v)|\le B_f\rho_C\).
Integrating (7) proves (12), including uniform convergence on the sphere.

## 5. Relation to the comparison construction

This supplies the numerical runtime label and tail inputs missing from
`UNBOUNDED_COMPRESSOR_BRIDGE.md` §10. Intersect (6) with its source cap and
the dense fitting cap; no extra scientific assumption is introduced.
The common horizon \(32\lambda^{-1}\log(en)\) is more than sufficient
for (12) to be smaller than any prescribed positive multiple of
\(n^{-1/2}\) at sufficiently large width. Quantifying the same-time
source-to-runtime comparison is separate from this fitting calculation.

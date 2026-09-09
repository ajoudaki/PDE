# Two-sample L3: a bounded C2 shape class without oddness

Derived 2026-09-08. This is new analytic work, conditional only on the displayed mathematical source estimates in the existing two-sample power-four proof and its attached Gaussian action/limit construction. Historical review verdicts are not premises. No experiment was performed and no preexisting file was edited.

## 1. Result and precise dependencies

Let

\[
\mathcal B=\{\psi\in C_b^2(\mathbb R):
\max(\|\psi\|_\infty,\|\psi'\|_\infty,\|\psi''\|_\infty)\le1\}.
\]

For each nonconstant \(\psi\in\mathcal B\), the existing two-sample L3 theorem extends to

\[
\phi(z)=az+e\psi(z),\qquad a\in[1/2,1],\qquad
0<e\le c_\psi\delta^4,
\qquad |\rho|\le1-\delta,\quad0<\delta\le1,
\]

with an explicit positive shape-dependent constant given below. Oddness of \(\psi\), monotonicity of \(\psi\), analyticity, saturation, and existence of tail limits are unnecessary. The complete activation is strictly increasing because \(\phi'\ge a-e\ge1/4\).

The initialization, raw metric, three hidden layers, actual finite readout, and raw GD step \(n^{-2}\) are exactly those in `two_sample_odd_activation_theorem/PROOF.md`. The conclusion is the same global autonomous uncut population flow, bounded-primal strong uniqueness against nonsymmetric competitors and restart from reached states, full-sequence GF/raw-GD limits on each fixed finite physical horizon, both action orientations and actual adjoints, all four raw kernels and stipulated same-layer path/velocity laws and moments. The existing nonaffinity and initial-motion certificates also extend, as proved below. The arctan-specific numerical loss rate changes: the elementary lower bound here gives \(\mathcal L(t)\le e^{-\delta t/2048}\); a sharper bound can be retained when \(\psi'\ge0\).

This extension uses the actual displayed proofs in:

- `two_sample_odd_activation_quantitative/AFFINE_POLYNOMIAL_BOUNDS.md` and `PROOF.md`, for the affine balance identities, primal comparison and numerical constants;
- `two_sample_odd_activation_power4/AFFINE_PROPAGATOR.md`, `PRIMAL_L2_RESPONSE.md`, `SECTOR_SUPERSOLUTION.md`, for the polynomial source interfaces and closure;
- `two_sample_odd_activation_power10/NORMALIZED_GATES_AND_PRIMALS.md`, for exact transformed equations and moment differences;
- `two_sample_odd_activation_theorem/SOURCE_AND_LIMIT_BRIDGE.md` and its attached fixed-program/action/velocity sources, for cap removal and width/GD limits;
- `two_sample_odd_activation_theorem/INITIAL_MOTION_AND_NORMALIZATION.md`, with the explicit shape substitutions checked in Section 7 below.

The new pieces are the typed sample conjugation (which removes oddness), a delta-independent upper bound for actual affine marginal variances (which removes arctan-specific tail/Hermite obligations), and the resulting full Cb2 activation class. The old power-four affine/source proof remains a substantive dependency, rather than something established by the activation substitution alone.

## 2. Scalar symmetry without oddness

Absorb \(y_1\) into the readout, an isometry of the raw metric and of its centered Gaussian initialization, and write \(y=(1,\tau)\), \(\tau=y_1y_2\in\{-1,1\}\). Let \(P\) exchange the two sample slots and let \(Q_x\) be the orthogonal input reflection exchanging the normalized inputs. Such a reflection exists because the two inputs have equal norm (their sum and difference are orthogonal).

The raw transformation

\[
(w,A,B,C)\longmapsto(Q_xw,A,B,\tau C)
\]

preserves the scalar feature objective
\(g=\frac12\sum_i y_if_i\) and its raw metric. Indeed it sends forward fields to their exchanged fields, predictions to \(\tau Pf\), and \(\tau Py=y\). It preserves the Gaussian initialization law. At each fixed Euler/cap transcript this is an exact equivariance. Deterministic limiting contractions therefore satisfy \(f_2=\tau f_1\), so \(f_i=y_ig\), without first invoking uniqueness of an unconstructed population flow.

For arbitrary scalar \(\phi\), forward fields transform as \(Pz,Ph\). Backward fields transform as \(\tau Pq,\tau P\delta\). For the auxiliary gate

\[
D_R(z,q)=aq+e\psi'(z)\tau_R(q),
\]

this is still exact because the same scalar \(\psi'\) is used at both samples and the clipping function \(\tau_R\) is odd. Oddness of the *clip*, not of the activation, is used here. Hence the cap feature paths have the same scalar prediction symmetry.

Once the constructed feature path reaches \(g=1\) from below on a bounded interval, the physical clock
\(dt/ds=[2(1-g(s))]^{-1}\) diverges at its first hit because \(g'\) is bounded there. This gives the exact physical flow for every finite physical time. Scalar symmetry by itself supplies neither the bounded feature interval nor the required source-tail/width bridge; those are supplied in Sections 5–6.

## 3. Typed sample bases: exact replacement for odd label folding

Set

\[
Q=\tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix},\quad
Y=\operatorname{diag}(1,\tau),\quad
Q_f=QY,\quad Q_b=Q,\quad
v=(1+\tau\rho)/2.
\]

Use \(Q_f\) for forward sample slots \(z,h,\xi\), and \(Q_b\) for backward slots \(q,\delta,\zeta\). The names forward/backward refer to the type of the sampled neuron field, not the direction in which a coefficient is multiplied. Then

\[
Q_f\Gamma\operatorname{diag}(y/2)Q_b^{-1}
=\operatorname{diag}(v,1-v),
\]

\[
\sum_i(y_i/2)\delta_i\otimes h_i
=\sum_{\alpha=+,-}(Q_b\delta)_\alpha\otimes(Q_fh)_\alpha,
\qquad \tfrac12\sum_i y_i h_i=(Q_fh)_+,
\qquad Q_b(C,C)^T=Ce_+.
\]

The tensor identity follows from \(Q_b^TQ_f=Y/2\), so includes every factor of two. Put \(S=\operatorname{diag}(\sqrt v,\sqrt{1-v})\), \(r=\sqrt v\), and \(\lambda=a^3r\). The exact normalized equations of `NORMALIZED_GATES_AND_PRIMALS.md` hold after replacing its single Q by Qf for forward slots and Qb for backward slots:

\[
z^\ell=a^{\ell-1}Q_f^{-1}Sx^\ell,\quad
h^\ell=a^\ell Q_f^{-1}S\widehat h^\ell,
\]
\[
\delta^\ell=a^{4-\ell}rQ_b^{-1}S^{-1}d^\ell,\quad
q^\ell=a^{3-\ell}rQ_b^{-1}S^{-1}\widehat q^\ell.
\]

With normalized time \(t=\lambda s\), these give exactly

\[
x^2=A\widehat h^1,\quad x^3=B\widehat h^2,
\quad\widehat q^3=Ce_+,\quad
\widehat q^2=B^*d^3,\quad\widehat q^1=A^*d^2,
\]
\[
\partial_t x^1=d^1,\quad
\partial_t A=\sum_\alpha d^2_\alpha\otimes\widehat h^1_\alpha,
\quad\partial_t B=\sum_\alpha d^3_\alpha\otimes\widehat h^2_\alpha,
\quad\partial_t C=\widehat h^3_+.
\]

At \(e=0\), the normalized active four-component affine system, the frozen inactive fields, all positive beta-scaling arguments, and their numerical affine bounds are therefore precisely the old ones.

There is also an exact source-coefficient symmetry. A forward response block \(\mathsf A\), mapping backward named sources to forward fields, and a backward response block \(\mathsf B\), mapping forward sources to backward fields, obey

\[
P\mathsf A=\mathsf A(\tau P),\qquad
(\tau P)\mathsf B=\mathsf BP.
\]

At each fixed source transcript, this follows by the chain rule under the previous exact involution, keeping the deterministic arrays and covariances fixed during each formal derivative. Learned moments obey the same identities: forward learned blocks are forward Gram matrices times \(\operatorname{diag}(y/2)\), and backward blocks are backward Gram matrices times that same diagonal matrix. Full second-moment covariances commute with P. Induction over the source transcript therefore preserves both covariance symmetry and the response intertwiners, including singular Gaussian sources.

Now

\[
Q_fPQ_f^{-1}=Q_b(\tau P)Q_b^{-1}
=\tau\operatorname{diag}(1,-1).
\]

Thus \(Q_f\mathsf A Q_b^{-1}\) and \(Q_b\mathsf BQ_f^{-1}\) commute with \(\operatorname{diag}(1,-1)\), and are diagonal in the two sample sectors. For opposite labels, the original blocks anti-commute with ordinary exchange; treating them as commuting in one common sample basis would be wrong. The two different bases repair exactly that issue.

The current return \(E[D_z]\) has the backward-from-forward type and satisfies the second intertwiner. It is included, not set to zero. Random gates remain full two-by-two maps; only deterministic expected coefficient blocks become sector diagonal.

## 4. New affine variance bound independent of delta

For the affine active system let \(p\) be the normalized active first root and let \(D\) be the sign-adjusted readout. Write \(R=\|D\|^2\). The existing exact balances give

\[
\|p\|^2=1+R,\quad
A^*A=p\otimes p+A_0^*A_0-p_0\otimes p_0,
\quad BB^*=D\otimes D+B_0B_0^*.
\]

Since the initialized action norms are at most ten,

\[
\|Ap\|^2\le(R+101)(R+1),\qquad
\|BAp\|^2\le(R+100)(R+101)(R+1).
\]

The existing affine radial estimate \(F\ge\|D\|^4/\sqrt2\), with \(g=\lambda F\le3/2\) on the reference interval, yields

\[
R\le\sqrt{\frac3{\sqrt2a^3\sqrt v}}
\le\sqrt{12\sqrt2}\,v^{-1/4}<5v^{-1/4}.
\]

The frozen inactive fields and zero active/inactive covariance give the exact marginal formulas

\[
\operatorname{Var}(z_i^1)=v(1+R)+1-v,
\]
\[
\operatorname{Var}(z_i^2)=a^2[v\|Ap\|^2+1-v],\quad
\operatorname{Var}(z_i^3)=a^4[v\|BAp\|^2+1-v].
\]

Because \(vR^k\le5^k\) for \(k=1,2,3\) and \(0<v\le1\), expansion gives

\[
\operatorname{Var}(z_i^1)\le6,\quad
\operatorname{Var}(z_i^2)\le636,\quad
\operatorname{Var}(z_i^3)\le66780<260^2.
\]

For the last two bounds the expansions are
\(1+100v+102vR+vR^2\) and
\(1+10099v+10301vR+202vR^2+vR^3\).

The existing lower bounds require no activation substitution because this reference is affine: \(\|BAp\|\ge1\) by the radial readout inequality, while

\[
\|Ap\|^2\ge\max\{R(1+R),(100+R)^{-1}\}\ge1/101.
\]

Thus every actual affine marginal is centered Gaussian \(\nu G\) with

\[
\boxed{1/\sqrt{404}\le\nu\le260.}
\]

This fixed compact interval is the key new nonaffinity fact. Large initialized/action-space operator envelopes do not force the actual forward marginals to range over arbitrarily large variances as delta shrinks.

## 5. Nonaffinity and a safe explicit coefficient

Define

\[
\mathcal R_\psi(Z)=\inf_{\alpha,\beta}E[\psi(Z)-\alpha-\beta Z]^2,
\quad
\eta_\psi=\min_{1/\sqrt{404}\le\nu\le260}\mathcal R_\psi(\nu G).
\]

For each bounded continuous nonconstant \(\psi\), \(\eta_\psi>0\). Continuity in \(\nu\) follows by dominated convergence for the Gaussian regression formula (the variance stays positive). A zero residual would identify \(\psi\) with an affine function on the full support of a nondegenerate Gaussian. Continuity extends that equality everywhere, and boundedness makes the affine function constant, a contradiction.

An optional entirely explicit witness is any \(b\ge1\) with

\[
J_b(\psi)=\inf_{\alpha,\beta}\int_{-b}^b[\psi(x)-\alpha-\beta x]^2dx>0.
\]

Such b exists for every bounded nonconstant continuous function. Gaussian density on this interval yields

\[
\eta_\psi\ge\frac{e^{-202b^2}}{260\sqrt{2\pi}}J_b(\psi)>0.
\]

No tail-limit condition is used. Compactly supported and oscillatory shapes are included.

For any coupled square-integrable X,Y and a one-Lipschitz shape,

\[
|\sqrt{\mathcal R_\psi(X)}-\sqrt{\mathcal R_\psi(Y)}|
\le2\|X-Y\|_2.
\]

Indeed the optimal regression slope has absolute value at most one by the independent-copy identity
\(\operatorname{Cov}(X,\psi(X))=\frac12E[(X-X')(\psi(X)-\psi(X'))]\). Its residual map \(\psi(x)-\beta x\) is two-Lipschitz. Test one optimizer on the other coupled variable and reverse the roles. Constant variables are covered by choosing slope zero.

Let C0,Cz,Cg,H be the actual numerical constants in the existing power-four proof:

\[
C_0=1296000e^{1404},\quad C_z=1500C_0,\quad C_g=14400C_0,
\]
\[
H=10^{30}(1+C_0+C_z+C_g+e^{1410})^4.
\]

Define

\[
c_{*,\psi}=\min\left\{\frac14,
\frac1{2C_0(8\sqrt2)^3},
\frac1{4C_g(8\sqrt2)^{11/4}},
\frac{\sqrt{\eta_\psi}}{4C_z(8\sqrt2)^{7/2}}\right\},
\]

\[
\boxed{c_\psi=\min\{c_{*,\psi},10^{-70}H^{-400}\}.}
\]

The old pointwise primal forcing estimates remain valid because \(|\psi|\le1<\pi/2\), \(|\psi'|\le1\), \(|\psi''|\le1\). Hence the old raw radius-one comparison and endpoint estimates hold with the same constants. Under \(e\le c_\psi\delta^4\), we have \(e\le c_{*,\psi}\delta^{7/4}\), so the raw tube closes, \(g_{e,R}(S)\ge5/4\), and

\[
\sup_{i,\ell,s\le S}\|z_{i,e,R}^\ell-z_{i,0}^\ell\|_2
\le C_z e(8\sqrt2)^{7/2}\delta^{-7/4}
\le\sqrt{\eta_\psi}/4.
\]

Consequently \(\mathcal R_\psi(z_{i,e,R}^\ell)\ge\eta_\psi/4\). Absorbing az into the regression competitor gives the activation error \(e^2\eta_\psi/4\). Strong cap removal preserves it, and the first-hit clock preserves it for all finite physical times.

These constants are explicit sufficient constants, still extremely small. This extension preserves the polynomial delta dependence; it does not solve the numerical-prefactor problem.

## 6. Every shape-dependent source/limit occurrence

The exact normalized forward and backward maps now are

\[
\mathcal H_\ell(x)=a^{-\ell}S^{-1}Q_f\phi(a^{\ell-1}Q_f^{-1}Sx),
\]
\[
\mathcal D_{\ell,R}(x,q)=a^{\ell-4}r^{-1}SQ_b
D_R(a^{\ell-1}Q_f^{-1}Sx,a^{3-\ell}rQ_b^{-1}S^{-1}q).
\]

Qf and Qb have exactly the old Q operator norms, as do their inverses. The deviations from the affine maps therefore obey the old normalized bounds with \(\varepsilon=64e/\sqrt\delta\): bounded forward error, first-derivative error at most epsilon, backward-value and q-derivative errors at most epsilon times the old factors, and x-derivative at most \(\varepsilon|q|\). The gates are still applied in original sample coordinates. Their random sector matrices are not assumed diagonal.

The source value substitutions are exact with
\(h(Z)=\psi(Z)\) and \(d(Z,q)=\psi'(Z)\tau_R(q)\). They use only \(|h|\le\pi/2\) and \(|d|\le|q|\), both satisfied. In the derivative equations replace the old g and g-prime by \(\psi'\) and \(\psi''\):

\[
G=aI+e\operatorname{diag}(\psi'(Z)),\quad
V=aI+e\operatorname{diag}(\psi'(Z)\tau_R'(q)),\quad
L=e\operatorname{diag}(\psi''(Z)\tau_R(q)).
\]

The typed versions are respectively forward-to-forward, backward-to-backward, and backward-from-forward. Their deviations satisfy exactly \(|G-aI|,|V-aI|\le e\), \(|L|\le eQ\). These are the only activation inputs into the same-array derivative defect identities. Signs of \(\psi'\) or \(\psi''\) do not occur in their estimates; signed actual coefficient arrays are compared in absolute value to the positive *affine* supersolution. The affine beta positivity proof is unchanged because its activation is az.

Thus all power-four interfaces retain the same constants and powers:

\[
\|q^1\|_2\le HM^3,\quad\|q^2\|_2\le HM^2,\quad\|C\|_2\le HM,
\]
\[
\|q^1\|_p\le H^{10}M^{15}\sqrt p,\quad
\|q^2\|_p\le H^{10}M^{13}\sqrt p,\quad
\|C\|_p\le H^{10}M^{11}\sqrt p,
\]

and the complete coefficient forcing \(q_{\rm def}\le H^{30}eM^{19}\) under \(eH^{22}M^{19}\le1\). The sector supersolution requires \(q_{\rm def}\le H^{-16}M^{-12}\). Since \(M^{32}\le24^8\delta^{-4}\) and \(24^8<H\), the displayed choice \(e\le10^{-70}H^{-400}\delta^4\) verifies both inequalities with the same strict slack as the old proof. Amplitude homotopy at each fixed cap/transcript closes the construction. Current returns, both matrix orientations, all learned memories, singular source covariances and the source-time mesh factor remain in this calculation.

At fixed cap, \(\phi\) and DR are C1 coordinate maps with bounded first derivatives:

\[
|\phi'|\le2,\quad |D_q|\le2,\quad |D_z|\le2eR,
\quad|\phi(z)|\le|z|+1.
\]

C2 of psi supplies continuity of those derivatives; no third derivative is used. The asymmetric gate estimate becomes

\[
\|D_{R'}(z_A,q_A)-D_R(z_B,q_B)\|_2
\le2\|q_A-q_B\|_2+2eR\|z_A-z_B\|_2
+2e\||q_B|\mathbf1_{|q_B|>R}\|_2.
\]

It uses the Lipschitz bound on psi-prime from bounded psi-double-prime. The source subGaussian tails therefore defeat the cap amplification, producing the same strong cap removal, physical uniqueness/restart and finite GF/raw-GD comparison. The velocity bridge uses only linear growth, bounded first and second derivatives, product-query truncation, and the ordered removal of cap and reference-velocity truncation. All are unchanged. Existence of finite GF alone is not used to identify any population limit.

## 7. Initial motion and a kernel lower bound without oddness

Every initialized preactivation pair is nondegenerate centered Gaussian: its feature Gram is positive definite because \(\phi'>0\), full Gaussian support, and differentiation of a hypothetical identity \(u_1\phi(s)+u_2\phi(t)\equiv0\) force both coefficients zero. This induction works with nonzero feature means because source covariances are full second moments.

For the elementary initial kernel bound, decompose \(\phi=\phi_o+\phi_e\) into its odd and even parts. If \(m=a-e\ge1/4\), then \(\phi_o'\ge m\). For a centered Gaussian pair (U,V), simultaneous sign reversal makes the odd/even cross terms vanish. Therefore for each sign,

\[
E[\phi(U)\pm\phi(V)]^2
\ge E[\phi_o(U)\pm\phi_o(V)]^2
\ge m^2E[U\pm V]^2.
\]

Layerwise iteration gives \(\kappa(0)\ge m^6\delta/2\ge\delta/8192\). After construction, the radial gradient identity gives \(g_s'\ge\kappa(0)\), and \(\mathcal L=(1-g)^2\) then obeys \(\mathcal L(t)\le\exp[-4\kappa(0)t]\le\exp[-\delta t/2048]\).

The old initial-motion proof uses nonconstant phi-prime only when proving positive definiteness of the top beta Gram. It remains valid: bounded nonconstant C2 psi cannot have psi-double-prime identically zero, since then psi would be an affine bounded function and hence constant. The identity
\([p_1\phi(z_1)+p_2\phi(z_2)][u_1\phi'(z_1)+u_2\phi'(z_2)]=0\)
forces u1=u2=0 by strict monotonicity of the first factor in each coordinate and nonconstant phi-prime. The full reused-transpose covariance and deterministic derivative response formulas require only phi-prime, phi-double-prime, their bounds and Gaussian moments. Their conditional variance lower bounds hold with m replacing a. Thus all hidden parameter blocks have nonzero initial acceleration.

The forward linearization/adjunction identities still give positive aggregate upper-layer acceleration. The same raw swap/readout-sign involution from Section 2 equates the two sample acceleration norms for any scalar phi, so every sample/layer acceleration is nonzero. Since phi-prime is bounded below, feature accelerations are nonzero too. The projected-kernel expansion and its physical-time factors are unchanged.

## 8. Uniform full Cb2 classes and examples

At a fixed law, distance to the closed affine subspace gives

\[
|\sqrt{\mathcal R_\psi(\nu G)}-\sqrt{\mathcal R_\chi(\nu G)}|
\le\|\psi-\chi\|_\infty.
\]

Choose any nonconstant center \(\psi_0\in C_b^2\) with norm strictly below one and \(\eta_0=\eta_{\psi_0}>0\). Every member of the full Cb2 ball

\[
\|\psi-\psi_0\|_{C_b^2}<r_0,
\quad r_0\le\min\{(1-\|\psi_0\|_{C_b^2})/2,\sqrt{\eta_0}/2\}
\]

lies in the normalized class and has \(\eta_\psi\ge\eta_0/4\). Thus the same c(delta)=c(eta0/4) delta^4 works for this infinite-dimensional *nonodd* open class. It contains oscillatory and compact-support perturbations of the center. Choosing a compactly supported nonconstant center also gives a full open neighborhood of compact-support shapes, though arbitrary members of that neighborhood need not themselves have compact support.

Concrete normalized examples are sin(z), tanh(z), (sqrt(pi)/2) erf(z), and z/sqrt(1+z^2); each has function, first derivative and second derivative bounded by one. Any nonzero compactly supported C2 function can be normalized by its Cb2 norm. Nonodd examples include sufficiently scaled cos(z), exp(-z^2), or arbitrary small nonodd Cb2 perturbations of an admissible interior center. The complete activation stays increasing even when its bounded shape oscillates.

For an arbitrary bounded C2 nonconstant shape with finite norm B, apply the result to psi/B and amplitude eB; equivalently require eB<=c_(psi/B) delta^4. The normalization B is an analytic parameter of the shape, independent of the data and horizon.

## 9. Remaining limits of this derivation

No unresolved *activation-specific* obligation remains for normalized bounded nonconstant Cb2 shapes, provided the stated old power-four affine/source proofs are correct. An independent verification should particularly check the two-type covariance/derivative equivariance in Section 3, the exact source coefficient formulas under those bases, and the lower and upper affine variance bounds in Section 4. This note has not independently reconstructed every Gaussian common-action or power-four affine source-probe theorem from scratch.

The result does not establish practical-sized e, a sharp exponent, one activation amplitude valid for all delta>0, or uniform width convergence over all shapes/datasets/horizons. It does not alter the architecture, initialization or affine gain to disguise relative smallness. The broader class with unbounded linearly growing psi is not included in the theorem above; its source-value forcing requires a separate check.

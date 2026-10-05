# Mathematical checks of the polynomial compact comparison

2026-10-05. **PASS, conditional on the declared source, selection, and
independent fitting interfaces.** The current
[COMPACT_POLYNOMIAL_COMPARISON.md](COMPACT_POLYNOMIAL_COMPARISON.md)
has the stated universal constants 10 and 250, with no added label
restriction, source accuracy, width gate, or retained state. Its accuracy
certificate uses \(250^2=62500\). The dependence is polynomial in
\(\beta^L\), not in depth \(L\) itself.

## Provenance and current binding

Two complete internal reconstructions support this conclusion. The fresh
reviewer `compact_frozen_proof_check` read the entire deterministic proof
and the five mathematical inputs below, without prior reports or study
history, and subsequently reread the complete corrected proof. The
`compact_source_bounds` reviewer independently reconstructed the comparison
but authored its supporting source-energy lemmas. That second check is
therefore not independent of every supporting lemma. Both checks are
internal; neither is a promotion review or a new proof of the inherited
stochastic source theorem.

The fresh review's final corrected proof hash was
`8b3646e09583ebe26b5c3a475a97a5acb1b8ec9e17d06b9d192fe23abd141dae`.
The source-energy input hash was
`1ade8b3e9ee3a646d3a5ff65342c0db8b3606f230a21f78aea5d4c4da15b5317`.
The completed fresh and source-author reconstruction reports had hashes
`3d15a06e8d497b404ecf2b553d4127cb5323b9052b8ecf2ea297ca9826cd06e6`
and `0596b4a9e81aa9595574dbf3a43be01c76a8a66402727598596d176563cd9a10`,
respectively. Their mathematical checks are consolidated below, with
repeated material merged and unique coefficient checks retained.

The current integrated files are:

| File | SHA-256 |
|---|---|
| [COMPACT_POLYNOMIAL_COMPARISON.md](COMPACT_POLYNOMIAL_COMPARISON.md) | `893abe1447627438f3530a8b5a83b8214eb680beca7513bd99fee360f7fe336f` |
| [COMPACT_SOURCE_ENERGY.md](COMPACT_SOURCE_ENERGY.md) | `65a99b7f4249e83c5ad9c97fdc81193c5a49ad5eef04fe7e0582d2e376936c89` |

Editorial consolidation preserved all 55 displayed mathematics blocks in
the corrected comparison and all 46 in the support note byte-for-byte.
Only names, links, provenance, and current-scope descriptions changed.
This correspondence check does not claim a new independent review of the
editorial assembly. The support note also retains its separately derived
effective-readout total-variation lemma; the simple-cap proof does not
require that supplemental estimate.

The scientific inputs read completely by the fresh reviewer were:

| Input | SHA-256 at reconstruction |
|---|---|
| [UNBOUNDED_COMPRESSOR_BRIDGE.md](UNBOUNDED_COMPRESSOR_BRIDGE.md) | `03f126264a01e296f79164257df9fa1e706b8e8d5b043edc7c1d6e851f66acff` |
| [EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md](EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md) | `3824d29791fda356a8c048129576e5f42b4e1f44177759c7fcdb38882a6002c2` |
| [GENERAL_EXPLICIT_FITTING.md](GENERAL_EXPLICIT_FITTING.md) | `5c6f12b78847a2b2874c5bc82eb1cea5f4929ee071b114d09b098397c5e2b8d6` |
| [SIMPLE_CONSTANTS_SOURCE_CHECK.md](SIMPLE_CONSTANTS_SOURCE_CHECK.md) | `cc1096f354e38c97b5cab8fe2000323ca21811c9801a4a33a4c5dbaf0a08938a` |
| Provenance snapshot only: `COMPACT_SAMPLE_EXPONENT_REFINEMENT.md` | `c22585135817b085421ee4f86e6149b206ab9b1678e7888f0bd3791038d8909b` |

The source-author reconstruction additionally read the corresponding source,
runtime, and dense-fitting checks. Source isometry, carrier events, and
fitting inequalities are declared interfaces; the unprovided insertion,
selection, and probability dependencies were not reconstructed. Required
proof/process instructions were used. The canonical-notation skill was
permission-inaccessible, so the explicit notation contract in the assignment
was used rather than claiming to have read that skill.

## Setup and Hilbert geometry

Use the comparison's
\(X=\beta^L\ge100\), \(z=Y/\lambda\le X^{-30}\),
\(\alpha=Y/\sqrt\lambda=z\sqrt\lambda\), and
\(\epsilon=n^{-1}\le\min(1,Y,16z)\). The covariance recursion gives
\(\lambda\le X^4\), hence \(\alpha\le X^{-28}\). This permits
\(\lambda>1\); no replacement by a capped gap occurs.

All selected neuron metrics are fixed positive definite matrices. For a
block from layer \(j-1\) to layer \(j\), its squared Hilbert--Schmidt norm
is
\[
\|M_j^{1/2}B M_{j-1}^{-1/2}\|_F^2.
\]
Consequently the rank-one block \(\delta h^{\mathsf T}M_{j-1}\) has
norm \(\|\delta\|_{M_j}\|h\|_{M_{j-1}}\), and pairings of these blocks
factor into response and feature pairings. This verifies the specified
hidden Gram \(\mathcal J_C^*\mathcal J_C\) and comparison (7), including
the normalization by \(\sqrt m\) in the columns. It does not assert that
the specified backward pass is a parameter gradient in these metrics.

Diagonal domination gives, for a diagonal gate \(D\),
\(\|D\|_{M\to M}\le2\max_i|D_{ii}|\). Its metric adjoint need not
equal itself. Every use of an adjoint in the comparison is instead the
actual Hilbert adjoint of the indicated map; no gate self-adjointness is
used. The top map \(V_C\), its Gram \(Q_C=V_C^*V_C\), right inverse
\(T_C=V_CQ_C^{-1}\), and projector \(P_C=T_CV_C^*\) have the claimed
types. Since \(Q_C\succeq\lambda I/4\),
\[
\|T_C\|\le2/\sqrt\lambda,\qquad
P_C=P_C^*=P_C^2,\qquad T_CQ_C=V_C.
\]

The reference mixer arrays are defined by their rank-one integrals, not
by substituting them into a forward network. This distinction makes their
velocity identity exact while leaving the source action defects available
for forward and backward subtraction. Initial arrays agree exactly, both
raw readouts vanish, and both residuals equal the labels. Thus the hidden,
raw-readout, and normalized-residual errors start at zero even though
off-training initialization source approximations need not be exact.

## Energy transfer and subtraction

The dense energy and residual margin imply
\[
\|\dot\theta_n\|_{\rm par}
=\sqrt{2\rho_n(-\dot\rho_n)}
\le 2(-\dot\rho_n)/\sqrt\lambda,
\qquad \int_0^\infty\|\dot\theta_n\|_{\rm par}\le2\alpha.
\]
The statement extends across zero residual by the stationary continuation.
For source-approximating feature columns, full-width error is at most
\(\epsilon\), selected error at most \(2\epsilon\), and source-space
norm is preserved exactly. Normalizing each column by \(\sqrt m\) makes
the Hilbert--Schmidt error at most the same bound, proving
\(\|V_Rb\|\le\|V_nb\|+3\epsilon\|b\|\) without a sample factor.

Integrating the readout equation therefore yields
\[
\|w_R\|\le2\alpha+24z\epsilon\le4\alpha,
\qquad
\int_0^T\|V_Rc_n/\sqrt m\|\le\alpha+12z\epsilon\le2\alpha.
\]
The last absorptions use \(\epsilon/\sqrt\lambda\le\alpha\le X^{-28}\),
not an assumption \(\lambda\le1\). The corresponding dense response
bound is \(2X^2\alpha\). Adding source restriction error costs at most
\(3\epsilon\le3X^2\alpha\), so the comparison's
\(6X^2\alpha\) bound is safe. With compressed response bound
\(5X^3\alpha\), feature bound \(2X^3\), and \(L\le X\), the column
norm calculation gives
\(\|\mathcal J_C\|,\|\mathcal J_R\|\le X^8\alpha\).
Differentiating the actual compressed forward recurrence gives
\(\|\dot V_C\|\le X^{16}\alpha\rho_C\).

Let \(E_h\) be the product Hilbert norm of hidden parameter error,
\(e=(c_C-c_n)/\sqrt m\), \(p=T_Ce\),
\(\zeta=w_C-w_R+p\), and \(E_r=\|p\|+\|\zeta\|\).
The inherited forward recurrence can use \(E_h\): each individual
hidden block error is bounded by this product norm, and the forward
features do not depend on either readout. Thus
\(\|\Delta V\|\le X^9(E_h+\epsilon)\), including the corresponding
whole-sphere feature and preactivation bounds.

Writing \(d_R=V_R^*w_R-(y-c_n)/\sqrt m\), direct substitution into the
corrected readout gives
\[
\widehat w_C-w_R
=(I-P_C)(w_C-w_R)-p-T_C\Delta V^*w_R-T_Cd_R.
\]
Because \((I-P_C)p=0\), its first two terms cost at most \(E_r\).
The other two terms cost at most
\(8X^9z(E_h+\epsilon)\) and
\(32X^4z\epsilon/\sqrt\lambda\), respectively. Comparison (21)
rounds both upward correctly.

For the backward comparison, split the changed gate against the true
selected carrier, whose coordinates are bounded by
\(M=1+16X^{21}z\sqrt{\log(en)}\). Specifically,
\[
\|[\phi_j'(z_C^j)-\phi_j'(z_R^j)]\odot k_R^j\|_{M_j}
\le2\beta M\|z_C^j-z_R^j\|_{M_j}.
\]
The remaining carrier difference splits into the compressed adjoint acting
on the upper response difference, a mixer difference acting on a true
response of norm at most one, and the reverse source-action defect.
Propagation costs \(18s_1\le\beta^3\). Its finite sum is at most
\(2X^3\), and the additive forcing is at most
\(4\beta X^9M(E_h+\epsilon)\). Since \(\beta\le X^{1/2}\), their
product is at most \(8X^{25/2}M(E_h+\epsilon)\le X^{14}M(E_h+\epsilon)\).
The propagated terminal readout coefficient is at most \(X^4\).
This verifies (23) with one carrier factor, without a compressed-coordinate
maximum. Rank-one subtraction then gives (24):
\[
\|\Delta\mathcal J\|
\le X^{10}E_r+X^{20}M(E_h+\epsilon)
                  +X^{15}z\epsilon/\sqrt\lambda.
\]

## Gram forcing and the exact cancellation

The source Gram defect is bounded entrywise before sample normalization.
Its coefficient is at most
\[
X^4+80zX^{12}+256z^2X^{13}\le X^5.
\]
Here \(\epsilon\le S=16z\) is used for response pairing. An
\(m\)-by-\(m\) matrix with entries bounded by this defect, divided by
\(m\), has operator norm bounded by the same defect. There is therefore
no omitted sample factor in (25).

The Gram factorization (26) is exact. In its first term
\(T_CV_C^*=P_C\), and in its second term the factor
\(\|V_Rc_n/\sqrt m\|=\nu\) must be retained. Applying the bounds
above gives exactly the four coefficients in (27). Substituting (24), the
two potentially large forcing factors are
\(8X^{28}z\le1\) and \(8X^{23}z^2\le1\); the other terms round to
(28). This checks the energy-scale gain in the Gram forcing rather than
replacing it by a generic residual bound.

More explicitly, the hidden-direction substitution contributes
\[
8X^{18}z\rho_nE_r,\qquad
8X^{28}zM\rho_n(E_h+\epsilon),\qquad
8X^{23}z^2\epsilon\rho_n/\sqrt\lambda.
\]
The first rounds to the displayed \(X^{19}z\rho_nE_r\); the latter
two use the existing common label cap.

For fixed metrics, differentiation of the inverse gives
\[
\dot T_C=(I-P_C)\dot V_CQ_C^{-1}-T_C\dot V_C^*T_C.
\]
As \(Q_C^{-1}e=T_C^*p\), this implies
\(\|\dot T_Ce\|\le4\|\dot V_C\|\|p\|/\sqrt\lambda
\le X^{17}z\rho_C\|p\|\).

The residual equation gives a term \(-2T_CQ_Ce=-2V_Ce\) in \(\dot p\).
It cancels the \(+2V_Ce\) term in the raw readout difference when
forming \(\dot\zeta\). Pairing the equation for \(p\) with \(p\)
gives \(-2\langle p,V_Ce\rangle=-2\|e\|^2\), because
\(V_C^*p=e\). The hidden Gram does not need a sign in this pairing:
\[
2\|p\|\|T_C\|\|\mathcal J_C\|^2\|e\|
\le8X^{16}z^2\|e\|^2\le\|e\|^2.
\]
Thus it leaves at least one unit of the displayed residual damping.

With the comparison's nonnegative forcing integral \(I(t)\), regularizing
\(\|p\|\) by \(\sqrt{\|p\|^2+\delta^2}\) and then decreasing
\(\delta\) proves
\[
\|p(t)\|+\int_0^t\frac{\|e\|^2}{\|p\|}\le I(t),
\qquad \int_0^t\|e\|\le2I(t)/\sqrt\lambda.
\]
The quotient is zero when \(p=0\), since then \(e=0\); the damping
integrands increase monotonically in this regularization. The second
inequality uses \(\|p\|\le2\|e\|/\sqrt\lambda\).
Integrating the remaining hidden-Gram term in \(\dot\zeta\) costs
\(8X^{16}z^2I(t)\le I(t)\). The hidden velocity's residual-error term
costs \(4X^8zI(t)\le I(t)\). These are precisely (34)--(35).

## Scalar closure, all-time comparison, and constants

Set \(E=E_h+E_r\) and \(G_\lambda=1+\lambda^{-1/2}\).
Combining the preceding bounds gives comparison (36). The complete
coefficient check before its final rounding is:

| Integrand component | Coefficient before final rounding |
|---|---:|
| \(M\rho_n(E_h+\epsilon)\) | \(4X^{10}+2X^9+2X^{20}\le X^{21}\) |
| \((\nu/\sqrt\lambda)(E_h+\epsilon)\) | \(4X^{10}\le X^{21}\) |
| \(\rho_CE_r\) | \(4X^{17}z\le1\) |
| \(\rho_nE_r\) | \(4X^{19}z+2X^{10}\le3X^{10}\) |
| \(\epsilon\rho_n/\sqrt\lambda\) | \(4X^6+2X^{15}z\le X^7\) |

The chosen \(X^{22}\) covers these terms. Keeping both terms in
\(G_\lambda=1+\lambda^{-1/2}\) is necessary when \(\lambda>1\).

The integrated coefficient obeys
\[
B(t)\le4X^{22}z(M+1)
\le2X^{23}z+16X^{44}z^2\sqrt{\log(en)}.
\]
The cap \(z\le X^{-30}\) makes the last coefficients at most
\(2X^{-7}\) and \(16X^{-16}\). It follows that both
\(B(t)\le1+\sqrt{\log(en)}\) and
\(B(t)\le X^{24}z(1+\sqrt{\log(en)})\) hold. Integral Gronwall with
the verified zero initial error gives
\[
E(t)\le\epsilon G_\lambda(e^{B(t)}-1)
\le\epsilon G_\lambda X^{24}z(1+\sqrt{\log(en)})
                         e^{1+\sqrt{\log(en)}}.
\]
Retaining the factor \(B\) through \(e^B-1\le Be^B\) is essential
for retaining the actual label factor in the final bound.

For a sphere query the output difference is the effective-readout error
paired with a compressed feature, plus the reference readout paired with
the feature error, plus the source observation defect. Their coefficients
give (40). In detail, the coefficients on \(E_h+\epsilon\) are
\(X^{14}z+4X^{11}z\), the remaining forcing is
\(X^9z\epsilon/\sqrt\lambda+16X^4z\epsilon\), and the coefficient
on \(E_r\) is \(X^4\). They are all bounded by the expression in
(40). The substitution above and \(1+r\le2e^r\) imply (41), with
substantial slack in \(6X^{40}\). No source approximation is differentiated.

The inherited dense and compact fitting proofs bound instantaneous
sphere-uniform output speeds by an integrable residual multiple. Their
integrated tails therefore bound the motion from \(T\) to every later
time, and uniform convergence includes the fitted endpoint. Using the
comparison's conservative, doubled tail constants gives
\[
z(16\mathcal K+4B_f)e^{-8\log(en)}
\le X^{13}zG_\lambda e^{-8\log(en)}.
\]
This is a same-time comparison with both optimizers continuing to evolve.
Since \(e^{-8\log(en)}\le n^{-1}\), adding this term to (41) is
covered by the numerical coefficient 10 in comparison (1).

For the strict-root consequence, put \(r=\sqrt{\log(en)}\). The
identity \((r-2)^2\ge0\) gives
\(2r\le r^2/2+2\), hence
\(n^{-1}e^{2r}\le e^{5/2}n^{-1/2}\) for every integer \(n\ge1\).
For every positive \(\lambda\),
\(\lambda^{-1}(1+\lambda^{-1/2})\le2(1+\lambda^{-1})^2\).
Since \(20e^{5/2}<250\), comparison (2) follows with its stated numerical
constant and no new width condition. Squaring the sufficient accuracy
condition yields \(250^2=62500\), exactly as in [RESULT.md](RESULT.md).

## Construction gates, storage, and final claim boundary

All constructions still use coordinate tolerance \(1/n\), horizon
\(32\lambda^{-1}\log(en)\), the same four source families, initialized
exact additions, selected metrics, and corrected-readout runtime. All
comparison vectors and maps introduced in this proof are proof objects.
Neither a trained reference trajectory nor an additional moving coordinate
is retained.

For the per-layer budget in [RESULT.md](RESULT.md), the supplied source bound for
\(d\ge2\) has coefficient
\(2^{16}9^d\beta^{(24+2d)L+d}\). Since
\(2^{16}9^d\le\beta^{5+d}\) and
\((24+2d)L+2d+5\le(32+3d)L\), the displayed budget is sufficient.
For \(d=1\), the supplied coefficient
\(263168\beta^{26L+1}\) is also at most \(\beta^{35L}\).
The selection bound \(q_j\le9R\) then gives the stated ceiling formula.
The learned-coordinate count is
\((L-1)q^2+q(d+1)+m\). The separate all-retained formula is exactly
the supplied source inventory and its checked envelope; its actual
fourth power of \(Y/\lambda\) and logarithmic power \(3d+2\) remain.

The source gates have not disappeared. They include
\(\epsilon\le\min(1,Y,S)\), the radius conditions of source (31),
the degree/count conditions of source (34) and the dimension-one
qualification, as well as the inherited eventual stochastic threshold.
In particular the original temporal condition
\[
\log(en)\ge a^2\lambda^2/(16384Y^4U^2)
\]
can still require an exponential reference width. The new comparison
does not claim otherwise and does not hide another comparison gate there.
The fixed-task accuracy asymptotics in [RESULT.md](RESULT.md) are valid because these
existing thresholds are fixed before the requested error tends to zero.
They do not imply a uniform polynomial threshold in all task parameters.

The case \(Y=0\) is separate: zero readout and zero residual give the
stationary zero predictor. One must not insert \(Y=0\) into the source
construction's inverse-label radius or its \(\epsilon\le Y\) condition.
The constants 10, 250, and 62500 and the displayed beta-only size/storage
envelopes belong to the simple label cap. The larger recurrence allowance
is covered separately by [COMPACT_FULL_LABEL_RANGE.md](COMPACT_FULL_LABEL_RANGE.md)
and [COMPACT_FULL_LABEL_RANGE_CHECK.md](COMPACT_FULL_LABEL_RANGE_CHECK.md),
with its own numerical constants and original exact source-storage coefficients.
This check does not extend the simple-cap constants to that additional range.

No unresolved deterministic correctness objection remains within this
conditional scope. The activation maximum covers every layer and both
derivative orders, and \(Q_C\) consistently denotes the normalized
top-feature Gram. The source stochastic machinery, optimality, finite-precision
complexity, and promotion eligibility remain outside this verdict. Checks
used complete source reads, algebraic reconstruction, edge-case analysis,
and SHA-256 checks; no numerical experiment was performed.

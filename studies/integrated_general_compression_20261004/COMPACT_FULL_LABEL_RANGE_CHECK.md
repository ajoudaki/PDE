# Check of the full recurrence-range compact comparison

2026-10-05. **The mathematical result passes, conditional on the inherited
source, selection, and independent fitting event.** The original internal
reconstruction verified the complete recurrence domination, activation/depth
powers, all-time tails, and exact-storage qualification. It identified a
missing source-forcing factor; the corrected proof was subsequently reread
completely and passed. The corrected envelope is part of the current
[COMPACT_FULL_LABEL_RANGE.md](COMPACT_FULL_LABEL_RANGE.md).

## 1. Mathematical-review and editorial provenance

The mathematical calculations below retain the original independent
internal reconstruction of the full-range derivation and its complete
cancellation reduction. The checker was not an author of that derivation,
but authored its source-energy support, now represented by
[COMPACT_SOURCE_ENERGY.md](COMPACT_SOURCE_ENERGY.md). The coordinator also
flagged the forcing-envelope issue; the checker reconstructed its algebra.
This was an internal reconstruction, not a promotion-isolated review of
the entire inherited stochastic dependency package.

The originally checked corrected theorem text had SHA-256
`0f1c4416e82841eaa69bc41715b05deae74f5184c2ff61b7c78c3754ce3f4ee3`.
Its valid cancellation derivations and the corrected full-range proof
are now integrated into a single document. The editorial consolidation
was performed by the full-range proof author. It preserves the reviewed
mathematics, incorporates the corrected forcing throughout, updates local
definitions and links, and removes superseded-status prose. It is not a
new independent mathematical review.

The consolidated proof's editorial binding is SHA-256
`90aeb1a3aba585aab27f0b46cb23ad7391614abbc64272dccf16ab25fb80b071`.
The correspondence checks for this binding concern the retained equations,
correction, theorem scope, and absence of dependencies on removed files.
The original reviewer's PASS is evidence for the mathematical content;
it is not represented as a fresh review of this newly organized file.

Current scientific dependencies are the integrated
[UNBOUNDED_COMPRESSOR_BRIDGE.md](UNBOUNDED_COMPRESSOR_BRIDGE.md),
[EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md](EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md),
[GENERAL_EXPLICIT_FITTING.md](GENERAL_EXPLICIT_FITTING.md), their retained
checks, and
[SIMPLE_CONSTANTS_SOURCE_CHECK.md](SIMPLE_CONSTANTS_SOURCE_CHECK.md).
The common-cap comparison is
[COMPACT_POLYNOMIAL_COMPARISON.md](COMPACT_POLYNOMIAL_COMPARISON.md).
Notation agrees with the consolidated proof, including
\(a_{\rm strip}\) for the source's strip width \(a\).
No new proof research, experiment, stochastic-width claim, or Git mutation
was part of this editorial consolidation.

## 2. Complete source-forcing envelope

Use \(a\) for hidden error, \(b_e\) for the lifted readout error,
\(E=a+b_e\), \(M\ge1\), and write \(l=\lambda^{-1/2}\) in this
paragraph. The backward subtraction supplies
\[
Q=b_e+M(a+\epsilon)+\epsilon l.
\]
After substituting the forcing inequality into the combined error bound,
put
\[
H_B=(2+20z(c+j))B_h,\qquad K_1=12F+H_B+20D_s.
\]
The resulting \(\rho_n\)-weighted source forcing is
\[
\epsilon[12F+H_B(M+l)+20D_sl].
\tag{C1}
\]
The smaller proposed envelope
\(\epsilon K_1M\max(1,l)\) would not cover this. At \(M=1,l=1\),
(C1) exceeds that expression by \(\epsilon H_B>0\). The same coefficient mismatch
persists for \(M\) sufficiently close to one. This is a defect in the
displayed domination, not a counterexample to the network comparison.

The exact sufficient domination is
\[
Q\le M\{E+\epsilon(1+l)\}.
\]
All other integrands in the scalar inequality of the consolidated proof
are also covered by \(E+\epsilon(1+\lambda^{-1/2})\).
Integral Gronwall then gives
\[
E(t)\le\epsilon(1+\lambda^{-1/2})(e^{B(t)}-1)
\le2\epsilon r_\lambda(e^{B(t)}-1),
\qquad r_\lambda=\max(1,\lambda^{-1/2}).
\tag{C2}
\]
This is precisely (D) in
[COMPACT_FULL_LABEL_RANGE.md](COMPACT_FULL_LABEL_RANGE.md).
The formula for \(B(t)\) is unchanged:
\[
B(t)\le400z^2F_c+2zK_1+40zF
                  +32z^2K_1K_{\rm src}\sqrt{\ell_n}.
\tag{C3}
\]
No factor two is required in \(K_1\) or (C3), because the change is
entirely to the constant source forcing in the scalar inequality.

The complete reduction in Sections 2–5 of the consolidated proof is
covered by the original reconstruction. In particular
\(F_c=(d_1^c)^2+4H_c^2\sum_{j\ge2}(d_j^c)^2\) implies
\(\|\mathcal J_C\|\le5\alpha\sqrt{F_c}\). The non-diagonal hidden
Gram costs at most \(200z^2F_cu^2\le25u^2/32\), against the exact
readout dissipation \(2u^2\). The bound on \(\dot T_Ce\) uses only
the derivative of the actual compressed forward pass. Source errors and
reference feature errors are not differentiated. Thus the source forcing
uses (C2), while the energy and cancellation
identities retain their verified coefficients.

## 3. Recurrence bounds through the hidden-direction coefficient

Retain the extension's proof abbreviations
\[
r_0=10s,\quad r=L-1,\quad u_0=H_L^{\rm src},\quad
p_0=P_L^{\rm src},\quad \kappa=(9/5)^r,
\quad A_0=(18s)^r=\kappa r_0^r,
\quad \tau=su_0r_0^r.
\]
The forward and port recurrences give
\(u_0\ge20sr_0^r\), \(p_0\ge3r_0^r\). The induction proving
\(H_c\le2\kappa u_0\) is valid: its first layer is bounded by
twice the source first layer, and each later multiplier is larger by
exactly \(9/5\); the additive term retains the same inequality.

The source minimum gives the sharper available inequality
\[
16z\le(8s\tau^2u_0^2)^{-1/2}.
\tag{C4}
\]
It follows from \(D_0\ge\tau^2\) and \(C_F\ge su_0^2\).
Since \(P_h\le7u_0\), \(P_\delta\le7\tau\), and
\(H_r\le2u_0\), the correction to either initialized action
coefficient 18 is at most
\(14/(8s\tau u_0)<1\). This proves \(A_f,A_b\le19\).

The forward subtraction recurrence unrolls to
\[
F\le A_0\left[2s+\frac{2s}{18s-1}(H_r+A_f)\right]
\le A_0\left[2s+\frac{u_0+22}{8}\right]
\le u_0A_0.
\]
Here \(u_0\ge20s\ge20\) supplies more than the necessary slack.
The maximum preactivation coefficient is at most \(F/(2s)\).

The real response comparison gives
\(d_j^E\le7\kappa u_0\). Consequently
\[
(\max_jd_j^E)zH_c
\le\frac{14\kappa^2}{16\sqrt8\,sr_0^r}\le1.
\]
The last inequality uses \(\kappa^2/r_0^r\le(3.24/10)^r\).
The two additional bounds \(6zF\le1\) and \(32zP_h\le1\) follow
from (C4), \(u_0\ge20sr_0^r\), and \(\tau\ge20\).

For the backward recurrence, the terminal value is at most
\(6s+tF/s\), and every earlier forcing term is at most
\(40s+tF/s\). The geometric sum is therefore bounded by
\[
\max_j B_j\le A_0(9s+2tF/s)
\le3tu_0A_0^2/s.
\]
For the last step, \(9s^2\le tu_0A_0\) follows immediately from
\(u_0\ge20s\), \(A_0\ge18s\), and \(t\ge1\).

Substitution into \(B_h\) yields
\[
B_h\le13\sqrt L\,\kappa^3tu_0^2r_0^{2r}/s.
\]
The inequality \(\sqrt L\,\kappa^3\le r_0^r\) holds first at
\(L=2\), and each increment of \(L\) multiplies its left/right
ratio by at most \(\sqrt{3/2}(5.832/10)<1\). Since
\(p_0^3\ge27r_0^{3r}\) and \(13/(27s)\le1\), this proves
the claimed bound
\[
B_h\le tu_0^2p_0^3.
\tag{C5}
\]

## 4. Gram coefficient and the strong source minimum

The compact allowance implies \(zc\le5/(16H_c)\le5/16\).
Also
\(j\le14\sqrt L\,\kappa u_0^2\), and (C4) gives
\(zj\le14/(16\sqrt8)<1/3\), because
\(\sqrt L(1.8/r_0)^r\le1\). Thus \(z(c+j)<1\).

For \(D_s\), the middle term is bounded by
\[
\frac{7}{\sqrt{8s}\,u_0}
   [1+4(L-1)u_0^2]
\le\frac3{u_0}+10Lu_0,
\]
and the last term is at most \(7L/(8su_0)\le L/u_0\).
Together with \(P_h\le7u_0\), this gives
\(D_s\le15Lu_0\); the final comparison uses \(L\ge2\) and
\(u_0\ge20\). The coefficient totals in \(K_1\) are therefore
bounded by \(12+22+300=334<400\), proving
\[
K_1\le400tu_0^2p_0^3.
\tag{C6}
\]

Every source lower bound used to compare (C6) to the actual allowance
is valid:
\[
D_0\ge2t^2u_0^2p_0^4,\qquad
D_*\ge tp_0^2,\qquad W_{\rm G}\ge u_0^3.
\]
For the last inequality,
\(W_{\rm G}\ge128s^2u_0(H_{L-1}^{\rm src})^2\), while
\(u_0\le(10s+1)H_{L-1}^{\rm src}\le11sH_{L-1}^{\rm src}\).
Its resulting numerical coefficient is \(128/121>1\).

The fourth-root source gate gives
\[
z\le\frac1{16}(8192D_0W_{\rm G}D_*)^{-3/4}.
\]
This follows from \(\eta^{-1}\ge8192D_0W_{\rm G}\) and
\(D_1\mathcal B\ge D_*^3\), with the correct exponent \(3/4\)
on each factor. Combining it with (C6) proves exactly
\[
zK_1\le\frac{25}{2^{21/2}}
           t^{-5/4}u_0^{-7/4}p_0^{-3/2}\le1.
\]

Since the largest source response coefficient is \(\tau\),
\(C_G=32\tau\). Thus
\(K_{\rm src}\le8448D_0\tau\), and the same gate gives
\[
z^2K_1K_{\rm src}
\le\frac{13200}{\sqrt2\,8192^{3/2}}
       \frac{\tau}{t^{3/2}p_0^2u_0^{7/2}}\le1.
\]
The constant 13200 is \(400\cdot8448/256\), so no factor was
lost. Substitute \(\tau=su_0r_0^r\),
\(p_0\ge3r_0^r\), and \(u_0\ge20s\) to verify the last
inequality directly. Finally (C4) and the forward bound prove
\(zF\le\kappa/(16\sqrt8\,su_0)\le1\).

Consequently all three asserted universal products are valid over the
full existing recurrence intersection. The compact allowance gives
\(400z^2F_c\le25/16\), so (C3) has
\[
B(t)\le25/16+2+40+32\sqrt{\ell_n}
\le44+32\sqrt{\ell_n}.
\tag{C7}
\]
This bound uses existing source and fitting gates, with no additional
small-label condition or width-dependent absorption.

## 5. Polynomial powers and output conclusion

Put \(X=\beta^L\ge100\). The unconditional source recurrences give
\(u_0,p_0,H_c\le X^3\). Since \(A_0\le X^3\),
\(F\le X^6\). Also \(F_c\le X^{15}\) and
\(K_{\rm src}\le X^{21}\) are unconditional recurrence envelopes.
Equation (C6), \(t\le\beta\le X^{1/2}\), and
\(400\le X^{3/2}\) yield
\(K_1\le X^{17}\). These powers do not use the smaller common
label cap.

The consolidated proof defines \(X=\beta^L\) locally and defines
its activation envelope before use. These are the same conventions used
by the numerical reconstruction.

Writing \(R=\sqrt{\ell_n}\), the source gate \(z\le1/16\) gives
an explicit useful version of the asserted polynomial estimate:
\[
\frac{B}{z}
\le25X^{15}+2X^{17}+40X^6+2X^{38}R
\le3X^{38}(1+R).
\tag{C8}
\]
The first three terms are at most \(3X^{17}\) for \(X\ge100\).
The scalar bound (C2), (C7), and (C8) give
\[
E\le6X^{38}z\epsilon r_\lambda(1+R)e^{44+32R}.
\tag{C9}
\]

For the output, (E) in the proof implies
\[
|f_C-f_n|\le15X^3E+575X^9z\epsilon r_\lambda.
\tag{C10}
\]
Indeed the coefficient of hidden error is at most
\(6H_CzF+3\alpha F\le15H_c\), using
\(zF\le1\) and \(\sqrt\lambda\le H_c\). The readout-error
coefficient is \(H_C=2H_c\). The direct source forcing is bounded by
\[
z\epsilon r_\lambda
  [15X^9+448X^6+112X^3]
\le575X^9z\epsilon r_\lambda.
\]
Here \(P_h\le7u_0\le7X^3\). This derivation preserves the actual
factor \(z=Y/\lambda\), including in the forcing term.

Substituting (C9) into (C10) gives at most
\(91X^{41}z\epsilon r_\lambda(1+R)e^{44+32R}\), because
\(575X^9\le X^{41}\). Since \(91X^{41}\le X^{42}\), the proof's
finite-horizon conclusion (47) is valid; its unspecified universal constant
can be taken to be one:
\[
\sup_{t\le T,v}|f_C-f_n|
\le X^{42}z r_\lambda\,n^{-1}(1+\sqrt{\ell_n})
                      e^{44+32\sqrt{\ell_n}}.
\tag{C11}
\]
The spare depth power absorbs only numerical constants. No parameter
dependence is hidden in that step.

## 6. All-time tails and an explicit universal root certificate

The claimed tail coefficients follow from the existing runtime formulas:
\[
G_c=4H_c^2+25\alpha^2F_c\le5H_c^2,
\qquad B_w^c\le25H_c^2r_\lambda,
\qquad B_f\le51H_c^3r_\lambda.
\]
For the middle coefficient, its mixed term is
\(240\alpha F_cz\le15/(16H_c)\); the other terms are
\(4H_c\) and at most \(20H_c^2/\sqrt\lambda\). For \(B_f\),
the remaining term \(50\alpha^2F_c\le50/256\) is smaller than
\(H_c^3r_\lambda\).

The source Gram coefficient has
\[
\mathcal K\le u_0^2+\frac{L}{8s}\le2u_0^2.
\]
The first inequality follows from (C4); the second follows from
\(u_0\ge20s(10s)^{L-1}\). Thus the unchanged all-time triangle
comparison adds at most
\[
236zX^9r_\lambda e^{-8\ell_n}.
\tag{C12}
\]
This covers later physical times and the endpoint, using the independent
fitting tails. No selected-source continuation beyond \(T\) is assumed.

For an explicit version of the proof's universal root-width
consequence, use \(1+R\le e^R\) and
\(33R\le R^2/2+1089/2\). Since \(R^2=1+\log n\),
\[
n^{-1}(1+R)e^{44+32R}\le e^{589}n^{-1/2}.
\]
Also \(\lambda^{-1}r_\lambda\le(1+\lambda^{-1})^2\). Equations
(C11)--(C12) consequently imply the sufficient explicit all-time bound
\[
\sup_{t\in[0,\infty],\,\|v\|=1}|f_C-f_n|
\le e^{590}\beta^{42L}Y(1+m/\gamma)^2n^{-1/2}.
\tag{C13}
\]
The numerical constant is intentionally very loose. This is a verified
completion of the proof's unspecified-universal-constant conclusion,
not an optimality assertion. It uses no new width threshold.

The estimates use \(\lambda\le H_c^2\), never \(\lambda\le1\).
Zero labels remain the exact stationary case. All errors in (C2) start
at zero, so using \(e^B-1\) rather than \(e^B\) is justified.

## 7. Storage and final boundary

The proof correctly preserves the exact source/storage formulas on
this larger interval. For \(d\ge2\), the existing leading source rank is
\[
A_n(Y)=\frac{2^{20}9^d}{d!}\frac U{a_{\rm strip}}\,c_q^{-(d-1)}
       (Y/\lambda)^2\ell_n^{3d/2+1},\qquad
c_q=\min\{1/8,a_{\rm strip}/(8V)\},
\]
with the **actual original** source recurrences \(U,V\) evaluated at
\(S=16Y/\lambda\). For \(d=1\), use its existing replacement
\(A_n(Y)=8\cdot514\cdot1024\,(U/a_{\rm strip})(Y/\lambda)^2\ell_n^{5/2}\).
The unchanged inventory is
\[
2040(L+1)A_n(Y)^2+
2040(L+1)(2m+d+1)^2+10m(d+1).
\]
The common-cap simplified storage coefficient
\(\beta^{(64+6d)L}\) is not justified here and is not asserted by
the extension. No retained runtime variable or source family is added by
the comparison. Exact-real preprocessing, precision qualifications, and
all original source construction gates remain in force.

The proof uses (C2) throughout, so no unresolved forcing correction
remains. The inherited stochastic event remains conditional input, and
the complete construction width is not claimed polynomial. This internal
reconstruction supplies no promotion certificate.


## 8. Current theorem correspondence and scope

The proof's two all-time conclusions are
\[
C\beta^{42L}Y\lambda^{-1}\max(1,\lambda^{-1/2})
 n^{-1}(1+\sqrt{\ell_n})e^{32\sqrt{\ell_n}},
\qquad
C\beta^{42L}Y(1+\lambda^{-1})^2n^{-1/2}.
\]
They follow from (C11)–(C13). Absorbing \(e^{44}\) into a universal
numerical constant introduces no structural or gap-dependent exponential.
The first rate is \(n^{-1+o(1)}\), because
\(\sqrt{\log(en)}/\log n\to0\). The uniform tail includes all physical
times and fitted endpoints.

The exact \(U,V\) storage formulas are retained over the full label
interval. No source, state, label, or construction-width requirement is
added. The separate common-cap theorem and its numerical coefficients
remain as stated in its own proof.

The following formula correspondences were also part of the original
mathematical check. They are retained as correspondences between the
checked theorems; this editorial assignment does not assert that the
coordinator's separately edited integrated result or README has received
a new review.

The companion common-cap error coefficients are 10 and 250. The prescribed
accuracy coefficient is \(250^2=62500\), so its displayed sufficient
reference-width certificate follows directly, subject to the expressly
retained construction conditions. No arbitrary-budget error theorem is
inferred from the per-layer size bound.

The displayed neuron budget is a sufficient common-cap envelope for
\(q_j\le9R\), \(R\le A_n(Y)+2m+d+1\). In particular the checked
source coefficient for \(d\ge2\) is bounded by
\(\beta^{(32+3d)L}(d+3)^{d/2}/d!\); its two-point-sphere replacement
at \(d=1\) is also smaller than that envelope. The learned-state count
and the stronger all-retained inventory agree with the existing
construction. The source tolerance remains \(1/n\).

The coefficients 10, 250, 62500, and the displayed beta-only size/storage
envelopes are confined to \(Y\le(\gamma/m)\beta^{-30L}\).
The separate full-recurrence corollary uses a universal numerical constant
and \(\beta^{42L}\), and preserves the original exact source
coefficients for size and storage on the additional label range. This is
exactly the distinction required by the corrected full-range proof.

The all-time norm, fitted endpoints, actual label factors, \(\lambda>1\)
case, zero-label case, fixed-width probability qualification, and
\(n^{-1+o(1)}\) statements are consistent with the checked proofs.
The fixed-task logarithmic size/storage asymptotics follow by choosing an
eligible reference width of order \(\varepsilon^{-2}\); the statement
explicitly permits their constants to depend on the inherited fixed-task
threshold. It does not claim a quantified or polynomial construction
threshold, introduce a comparison threshold, or imply promotion.


No unresolved blocking mathematical finding remains for the corrected
deterministic full-range extension. The conditional stochastic-source
boundary and the disclosed internal-review independence remain in force.
No promotion approval or effective polynomial construction-width theorem
is implied by this check.

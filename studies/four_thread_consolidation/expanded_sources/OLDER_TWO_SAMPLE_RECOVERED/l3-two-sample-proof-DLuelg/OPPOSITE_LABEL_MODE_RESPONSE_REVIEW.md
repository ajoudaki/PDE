# Independent adversarial mathematical audit

## Verdict and immutable input identification

**PASS within the stipulated finite Gaussian law. No required mathematical correction found.** The exact modal system, its symmetry and Gaussian source independence, all first-update coefficient blocks, and the cap-uniform first middle-query estimates (43)–(44) check out. This verdict does not identify the law with a finite-width limit and does not establish opposite-label global continuation.

The two authorized inputs were read in full:

| Input | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| OPPOSITE_LABEL_MODE_RESPONSE.md | 965 | 35162 | 1318581760487566cc467b2952016ce502a4d2da4a2cbf841e15c19e88a9776b |
| TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md | 352 | 14263 | 9305453f933ad30a0e813e4e97942ee9e00490ce726d70142b25c8f67a475170 |

Both inputs are in /tmp/l3-two-sample-proof-DLuelg/. References below to “candidate” mean the first file at this exact hash; references to “bootstrap” mean the second. Equation numbers without another attribution belong to the candidate. Line references identify these snapshots.

No other project, history, review, mathematical source, or referenced dependency was consulted. No experiments or other agents were used. This report is the only file written; neither input was edited. The finite Gaussian law and its frozen-coefficient formal derivative convention are accepted as stipulated. In particular, the bootstrap's external finite-program identification dependency was not read or audited.

## Required versus optional findings

### Required findings

None. I found no erroneous sign, missing factor of two, missing first-update response block, invalid Gaussian independence claim, or unsupported inference in the stated actual-query bounds.

There is also no missing global theorem relative to the candidate's stated scope: it explicitly disclaims such a theorem. Treating this candidate as a proof of global continuation, cut removal, a width limit, or a physical-time comparison would exceed the result proved.

### Optional clarifications

1. **Specify attained-law equality at the singular root endpoint.** At candidate lines 385–387, the assertion \(Z^{(1)}_{k,+}=0\) for \(\rho=-1\) is correct on the Gaussian law. It is not an identity after freely varying the zero-variance formal root coordinate: (20) still gives \(hZ^{(1)}_{k,+}=hG_+\). Adding “on the attained law” would make this as explicit as the discussion of (28). The existing derivative convention already resolves the issue; no calculation needs changing.

2. **Optionally expose the exact squared norm behind (43).** Independence in (33) gives
   \[
   \|q^{(2)}_{1,-}\|_2^2
   =\Delta^2\left(E_3[V^2p_-^2]+\beta_-^2K_2^+\right).
   \]
   Likewise,
   \[
   \|q^{(2)}_{1,+}\|_2^2
   =\Delta^2\left(E_3[V^2p_+^2]+\beta_+^2\kappa_2\right).
   \]
   These identities are slightly sharper than the triangle inequalities used in the candidate. They factor only the stipulated independent Gaussian noise from the initial population-2 pair. They do not factor the same-population products inside the population-3 expectations.

3. **Qualify the meaning of “uncontrolled” in Section 8.** The bootstrap already gives response bounds on feature time \([0,3/2]\). The missing result is a suitable later-time/contrast-sensitive estimate that would support continuation, not the absence of every short-time bound on these expressions. The candidate's opening and closing qualifications are sufficient, but repeating this distinction near (46) would avoid a possible misreading.

These are optional presentation improvements, not conditions of acceptance.

## 1. Modal coordinates, matrix actions, and every normalization

Candidate lines 55–122 and 254–327 agree with the bootstrap's sample-coordinate definitions.

Let
\[
P=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
Y=\operatorname{diag}(1,-1),\qquad
T=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]
Direct multiplication verifies the displayed inverse of \(T\), as well as
\[
TPT^{-1}=\operatorname{diag}(1,-1),\qquad
TYT^{-1}=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Thus the half-sum convention is used consistently; it is not an orthonormal normalization.

For an output pair \(F\) and a source pair \(s\),
\[
D_{s_{\rm mode}}(TF)=T(D_sF)T^{-1}.
\]
Because \(s_1=s_++s_-\) and \(s_2=s_+-s_-\),
\[
\partial_{s_+}=\partial_{s_1}+\partial_{s_2},\qquad
\partial_{s_-}=\partial_{s_1}-\partial_{s_2}.
\]
This proves (4) with no extra half factor. It holds as a coordinate identity before evaluating any Gaussian variables, independently of covariance rank.

For a sample block anticommuting with \(P\),
\[
M=\begin{pmatrix}u&v\\-v&-u\end{pmatrix},\qquad
TMT^{-1}=\begin{pmatrix}0&u-v\\u+v&0\end{pmatrix}.
\]
This verifies (12), including which modal direction receives \(u-v\).

For an ordinary/ordinary moment block
\[
K=\begin{pmatrix}h&c\\c&h\end{pmatrix},
\]
the learned forward coefficient is \((\Delta/2)KY\). Its modal off-diagonal entries are
\[
\frac{\Delta}{2}(h+c)=\Delta E[U_kU_r],\qquad
\frac{\Delta}{2}(h-c)=\Delta E[V_kV_r].
\]
Applying the same computation to backward/backward moments gives the two learned terms in \(B\). Together with the derivative transformation, this proves all four formulas in (13). Their diagonal modal entries vanish. The indicator \(r<k\) in the learned transpose term is essential and is retained correctly: the current block has only a response derivative.

Both learned matrices have the same exact finite-width algebra:
\[
\frac{\Delta}{2}
\left(\delta_1\otimes H_1-\delta_2\otimes H_2\right)
=\Delta\left(d_-\otimes U+d_+\otimes V\right),
\]
where \(\otimes\) includes the stipulated \(1/n\) normalization. Summing this identity gives (14) for each of \(\ell=2,3\).

In the population law its forward modal actions are
\[
\Delta d_{r,-}E[U_rU_k],\qquad
\Delta d_{r,+}E[V_rV_k],
\]
and its transpose modal actions are
\[
\Delta V_rE[d_{r,+}d_{k,+}],\qquad
\Delta U_rE[d_{r,-}d_{k,-}].
\]
These confirm every placement in the table at lines 318–323. These contractions are within the input population of the relevant rank-one operator. They do not identify population-2 neurons with population-3 neurons. At finite width the rank-one identities remain exact, while the empirical mixed moments need not vanish; the candidate makes that distinction correctly.

## 2. Exchange symmetry and Gaussian source independence

Candidate lines 124–252 pass, including the assertions about arbitrary pairs of times.

The transformation is ordinary exchange on the root and forward sources, and signed exchange on the reverse sources:
\[
G\mapsto PG,\quad \xi\mapsto P\xi,\quad \zeta\mapsto-P\zeta.
\]
For an ordinary pair \(F\), formal equivariance implies
\[
D_\zeta F(Sx)=-P(D_\zeta F(x))P.
\]
For a backward pair \(D\), differentiation in an ordinary forward source gives the same transformation rule. This is a statement about the full formal functions, so it does not require derivatives tangent to the Gaussian support.

The coefficient selection is causal. At each time the bottom fields use past reverse queries; the current objects are then selected in the order (8), with the readout already determined by past top features. Assuming the previously selected coefficients have the claimed symmetry, the preceding derivative rule and the moment symmetry give
\[
A_{k,r}=-PA_{k,r}P,\qquad B_{k,r}=-PB_{k,r}P.
\]
The learned terms obey the same rule since \(PY=-YP\). The forward equations, the opposite-label readout update, and oddness of both cuts then preserve (7).

The source extension step is legitimate within the stipulated construction. Each prescribed full time/sample covariance matrix is a matrix of second moments of a finite vector of fields and hence is positive semidefinite. The symmetry holds for cross-time entries as well as variances. A centered Gaussian vector with that covariance is invariant under the stated transformation even when the covariance is singular. This closes the induction without any continuous-flow uniqueness assumption.

The parity table is correct:

| Field type | Even mode | Odd mode |
|---|---|---|
| Ordinary pair, including \(G,\xi,Z,H,\phi'(Z)\) | plus | minus |
| Backward pair, including \(\zeta,q,d\) | minus | plus |
| Readout | — | \(w\) |

Thus every integrable odd field has zero mean. Any even/odd same-population product has zero expectation, including at different times. This proves (10). It also verifies the ordinary/ordinary and backward/backward sample blocks \(\bigl(\begin{smallmatrix}h&c\\c&h\end{smallmatrix}\bigr)\), and the ordinary/backward block \(\bigl(\begin{smallmatrix}u&v\\-v&-u\end{smallmatrix}\bigr)\). Subtracting the corresponding mean products preserves those structures. In particular, the symmetry does not force the even backward modes or the ordinary average features to have zero mean.

The root mode variances are \((1+\rho)/2\) and \((1-\rho)/2\), with zero cross covariance. Transforming each stipulated source covariance gives exactly (11). There is no centering correction involving \(EU\) or \(Ed_-\): the covariance of the centered Gaussian source is prescribed by a nonlinear field's second moment, not its centered covariance.

For each entire Gaussian source group, including all times, the plus/minus cross block is zero. Its characteristic function therefore factors into the two modal characteristic functions. This proves independence of the two whole modal vectors, not independence of time coordinates within either vector. Combining this fact with the stipulated independence of the four original groups and the root gives the claimed ten independent modal Gaussian groups. Degenerate coordinates cause no exception.

None of this proves independence of nonlinear evolved modes. The candidate uses orthogonality, not that stronger statement. In particular \(E_3[wU]=0\), so
\[
f_1=E_3[wV],\qquad f_2=-E_3[wV]
\]
holds for the deterministic predictions of this law. It does not imply a pathwise finite-width residual identity.

## 3. Coupled cuts, the entire Euler law, and formal derivatives

Candidate lines 329–452 pass.

Applying \(T\) to the two samplewise scalar cuts yields exactly (15). Multiplication by the samplewise gates yields (16). In particular the cross terms involving \(p_-\) are necessary and present.

The samplewise bottom update is \((\Delta/2)CYd^{(1)}\). Since
\[
TCYT^{-1}
=\begin{pmatrix}0&1+\rho\\1-\rho&0\end{pmatrix},
\]
its modal coefficients are \(\Delta(1+\rho)/2\) and \(\Delta(1-\rho)/2\), as in (17). The readout becomes \(\Delta\sum_{r<k}V^{(3)}_r\). The remaining forward and reverse lines follow from (13), with strictly historical forward terms and historical plus current reverse terms. No time block is missing.

The feature and gate differentials are
\[
\begin{pmatrix}hU\\hV\end{pmatrix}
=\begin{pmatrix}p_+&p_-\\p_-&p_+\end{pmatrix}
\begin{pmatrix}hZ_+\\hZ_-\end{pmatrix},\qquad
\begin{pmatrix}hp_+\\hp_-\end{pmatrix}
=\begin{pmatrix}c_+&c_-\\c_-&c_+\end{pmatrix}
\begin{pmatrix}hZ_+\\hZ_-\end{pmatrix}.
\]
These verify (18). The cut Jacobian is precisely the matrix in (19); its eigenvalues are the two scalar cut derivatives, each in \([0,1]\). Its mixed entries generally do not vanish.

For clarity, the product rules requested after (19) expand to
\[
\begin{aligned}
hd_+={}&(hp_+)\mathcal T_++(hp_-)\mathcal T_-\\
&+p_+(t_+hq_++t_-hq_-)+p_-(t_-hq_++t_+hq_-),\\
hd_-={}&(hp_+)\mathcal T_-+(hp_-)\mathcal T_+\\
&+p_+(t_-hq_++t_+hq_-)+p_-(t_+hq_++t_-hq_-).
\end{aligned}
\]
Together with the displayed top product rule, these yield exactly (20), with no derivative of any selected coefficient or covariance parameter. Each source injection is into one formal slot. Coincidence of source values at different times does not merge injections.

At fixed finite caps, gates, cut values, and their relevant derivatives are bounded; the readout is bounded at any fixed horizon. Induction through the finite causal formulas gives finite deterministic coefficients and finite derivative expectations. For identity cuts, each query is a Gaussian coordinate plus a bounded-feature shift with finite deterministic coefficients. Repeated product rules admit polynomial bounds in the finite source vector, which have finite Gaussian moments even for a singular law. This justifies the fixed-mesh well-definedness assertion without giving mesh-uniform bounds.

Finally, oddness and one-Lipschitzness give the claimed modal cut bounds:
\[
2\mathcal T_+(b,c)=\tau(b+c)-\tau(c-b),\qquad
2\mathcal T_-(b,c)=\tau(b+c)-\tau(b-c).
\]
Consequently \(|\mathcal T_+|\le |b|\) and \(|\mathcal T_-|\le |c|\). These inequalities do not decouple the cut.

## 4. Exact gate factors and arbitrary-time current blocks

Candidate lines 454–549 pass.

Writing \(z=\tan\alpha,z'=\tan\beta\) gives
\[
\phi'(z)=\gamma\cos^2\alpha,\qquad
\phi(z)-\phi(z')=\gamma(\alpha-\beta).
\]
The identity
\[
\cos^2\alpha-\cos^2\beta
=-\sin(\alpha+\beta)\sin(\alpha-\beta)
\]
proves (21), including its sign. Therefore \(p_-=\lambda V\) with
\[
\lambda=-\sin(\alpha+\beta)\operatorname{sinc}(\alpha-\beta),
\qquad |\lambda|\le1.
\]
On the diagonal this factor has continuous value \(-\sin(2\alpha)\); both differences themselves are zero. There is no division by a possibly vanishing contrast in the displayed construction.

Direct differentiation gives
\[
\frac{\phi'''(z)}{\phi'(z)}
=\frac{6z^2-2}{(1+z^2)^2}.
\]
For \(x=z^2\ge0\), both inequalities
\[
-2(1+x)^2\le 6x-2\le2(1+x)^2
\]
hold. Integrating with respect to the strictly increasing variable \(\phi\) proves the curvature divided-difference bound and \(c_-=\nu V\), \(|\nu|\le2\), including its diagonal extension. Also \(|\phi''/\phi'|\le1\), so \(|c_+|\le\gamma\). These facts verify (22)–(24) and all the stated mixed terms in the uncut matrix-2 products.

For a current source, past features and \(w_k\) are formally constant. Hence in sample coordinates
\[
B^{(3)}_{kk}=\operatorname{diag}(b^{(3)}_k,-b^{(3)}_k),
\quad b^{(3)}_k=E_3[w_k\phi''(Z^{(3)}_{k1})].
\]
The equality \(b^{(3)}_k=E_3[w_kc^{(3)}_{k,-}]\) follows because \(w_kc^{(3)}_{k,+}\) is odd. Conjugating this diagonal sample block gives two equal off-diagonal modal entries.

For matrix 2 the only current-source dependence of the reverse query is
\[
D_{\xi^{(2)}_k}q^{(2)}_k
=B^{(3)}_{kk}\operatorname{diag}(\phi'(Z^{(2)}_k)).
\]
The chain and product rules give exactly (25), including the square of \(\phi'\), the factor \(b^{(3)}_k\), and both cut terms. No other current-time response or learned term is omitted. For the uncut first expectation, the parity cancellation leaves \(E[c_+q_-+c_-q_+]\), as stated.

## 5. Initial Gaussian integrals and singular first-update values

Candidate lines 551–613 and 670–710 pass.

An explicit standard-normal realization confirms that the integrals in (26) are fully determined. For independent standard normals \(s,t\), put
\[
X^{(\ell)}_1=\sqrt{v_\ell^+}\,s+\sqrt{v_\ell^-}\,t,\qquad
X^{(\ell)}_2=\sqrt{v_\ell^+}\,s-\sqrt{v_\ell^-}\,t,
\]
where
\[
(v_1^+,v_1^-)=((1+\rho)/2,(1-\rho)/2),\qquad
(v_\ell^+,v_\ell^-)=(K_{\ell-1}^+,\kappa_{\ell-1})\quad(\ell=2,3).
\]
Expectation means integration against the standard two-dimensional Gaussian density; a zero coefficient simply suppresses one attained coordinate. This reproduces precisely the recursive initial covariances in the candidate without an inverse covariance or a nonsingular-density assumption.

In these variables,
\[
U=1+\frac{\arctan X_1+\arctan X_2}{20},\qquad
V=\frac{\arctan X_1-\arctan X_2}{20}.
\]
Thus \(e_\ell=E[(\phi'(X_1))^2]\), \(f_\ell=E[\phi'(X_1)\phi'(X_2)]\), and
\[
E[p_+^2]=(e_\ell+f_\ell)/2,\qquad
E[p_-^2]=(e_\ell-f_\ell)/2.
\]
The explicit integral for \(t_\ell\) has the correct negative sign and coefficient \(1/100\), since \(V\) contributes \(1/20\) and \(\phi''(X_1)\) contributes \(-X_1/5\). Exchange symmetry also gives \(t_\ell=E[V c_-]\).

At time zero \(w_0\) and \(d^{(3)}_0\) are identically zero formal functions. Hence \(B^{(3)}_{00}=0\) and the attained \(\zeta^{(2)}_0\) is zero. However
\[
\delta^{(2)}_{0a}
=\phi'(\xi^{(2)}_{0a})\tau_{R_2}(\zeta^{(2)}_{0a})
\]
remains a nonconstant formal function. Its forward-source derivative vanishes on the attained law, giving \(B^{(2)}_{00}=0\), while its own reverse-source derivative there equals \(\phi'(X^{(2)}_a)\), because \(\tau'_{R_2}(0)=1\). The bottom zero-valued reverse slots have the analogous nonzero derivatives.

The first Euler update therefore leaves the attained hidden parameters and bottom values unchanged and sets \(w_1=\Delta V^{(3)}_0\). Equality of the lower-layer time-zero and time-one features makes the variance of each \(\xi^{(\ell)}_{1a}-\xi^{(\ell)}_{0a}\) equal to zero. This proves all equalities in (28) as attained-law equalities. It does not justify substituting one formal source for the other.

The two additional Gaussians in (33) have covariance given by the second moments of \(V p_+\) and \(V p_-\). Their cross moment is zero by exchange parity. They are independent of the initial population-2 pair by the stipulated source-group independence. Consequently (34) is a definite Gaussian integral in the initial pair plus two independent Gaussian coordinates, at the stated \(\Delta,R_2,\rho\). Under exchange \(Q_1\mapsto-Q_2\); evenness of \(\tau'\) and oddness of \(\tau\) prove all the accompanying equality/sign statements. No evolved response is left implicit in these definitions.

## 6. All first-update forward and transpose coefficients

Candidate (29)–(36), lines 615–754, pass separately for every historical/current block.

For matrix 2, direct bottom differentiation gives the sample response block
\[
\frac{\Delta}{2}
\begin{pmatrix}e_1&-\rho f_1\\ \rho f_1&-e_1\end{pmatrix}.
\]
Adding the learned term and transforming proves
\[
A^{(2)}_{10,+-}=\Delta K_1^++\frac{\Delta}{2}(e_1+\rho f_1),
\qquad
A^{(2)}_{10,-+}=\Delta\kappa_1+\frac{\Delta}{2}(e_1-\rho f_1).
\]

For matrix 3 the attained response derivative is
\[
D_{\zeta^{(2)}_0}H^{(2)}_1
=\operatorname{diag}(\phi'(X^{(2)}))\,
A^{(2)}_{10}\,
\operatorname{diag}(\phi'(X^{(2)})).
\]
If the two off-diagonal modal entries of \(A^{(2)}_{10}\) are \(a,b\), the corresponding entries of this gate product have expectations
\[
E[p_+^2]a+E[p_-^2]b,\qquad
E[p_-^2]a+E[p_+^2]b.
\]
Adding \(\Delta K_2^+\) and \(\Delta\kappa_2\) respectively gives exactly both lines of (30). Thus the response terms at zero-valued history slots are retained for both forward matrices. Their cap independence follows from the cuts' values and derivatives at zero.

For matrix 3's transpose, historical differentiation acts on \(w_1\), while current differentiation acts on its gate. The separately obtained sample blocks are
\[
B^{(3)}_{10}=\frac{\Delta}{2}
\begin{pmatrix}e_3&-f_3\\f_3&-e_3\end{pmatrix},\qquad
B^{(3)}_{11}=\Delta t_3\operatorname{diag}(1,-1).
\]
Their modal entries are precisely

| Block | \(+,-\) | \(-,+\) |
|---|---|---|
| \(B^{(3)}_{10}\) | \(\Delta(e_3+f_3)/2\) | \(\Delta(e_3-f_3)/2\) |
| \(B^{(3)}_{11}\) | \(\Delta t_3\) | \(\Delta t_3\) |

Combining these blocks only after evaluating the coincident features gives (32)–(33). In particular, the average query multiplies \(V^{(2)}_0\) by \(\beta_+\), while the difference query multiplies \(U^{(2)}_0\) by \(\beta_-\). Neither assignment is interchangeable.

For matrix 2's transpose, \(D_{\xi^{(2)}_0}Z^{(2)}_1=0\) on the attained law, because the intervening derivative of \(\delta^{(2)}_0\) contains \(\tau_{R_2}(0)\). In contrast \(D_{\xi^{(2)}_1}Z^{(2)}_1=I\). The historical derivative is therefore exactly the matrix displayed at candidate lines 726–730. Taking expectations gives
\[
B^{(2)}_{10}=\frac{\Delta}{2}
\begin{pmatrix}e_3a_2&-f_3b_2\\f_3b_2&-e_3a_2\end{pmatrix}.
\]
The current derivative additionally differentiates the gate and uses the current matrix-3 block, yielding
\[
B^{(2)}_{11}=(c_2+\Delta t_3a_2)\operatorname{diag}(1,-1).
\]
Thus all four entries in (35) are correct:

| Block | \(+,-\) | \(-,+\) |
|---|---|---|
| \(B^{(2)}_{10}\) | \(\Delta(e_3a_2+f_3b_2)/2\) | \(\Delta(e_3a_2-f_3b_2)/2\) |
| \(B^{(2)}_{11}\) | \(c_2+\Delta t_3a_2\) | \(c_2+\Delta t_3a_2\) |

All historical learned transpose terms vanish at this step because the historical backward fields have zero attained values. There is never a current learned transpose term. The modal diagonal entries of every block above are zero.

Equation (36) now follows by the attained equality of the bottom features at the two times. Its two Gaussian source modes are independent of each other and of the root. Their covariances are the middle backward second moments exactly as stated, including the genuine coupled middle cut. The bottom cap does not enter these first-query values or any of (29)–(36). The middle cap does enter (34)–(36); no incorrect cap-independence claim is made for those quantities.

## 7. Angle estimates and uncut specializations

Candidate lines 756–837 pass.

With \(\theta=1-\rho\),
\[
E[(G_1-G_2)^2]=2\theta,\qquad
E[(X^{(\ell)}_1-X^{(\ell)}_2)^2]=4\kappa_{\ell-1}\quad(\ell\ge2).
\]
The bound \(|V|\le\gamma|X_1-X_2|/2\) consequently proves
\[
\kappa_1\le\gamma^2\theta/2,\qquad
\kappa_\ell\le\gamma^2\kappa_{\ell-1}
\le\gamma^{2\ell}\theta/2.
\]
The exact gate factors give
\[
0\le(e_\ell-f_\ell)/2=E[p_-^2]\le\kappa_\ell,\qquad
|t_\ell|=|E[V c_-]|\le2\kappa_\ell.
\]
This is (37). The cancellation replacing \(\phi''(X_1)\) by \(c_-\) uses exchange parity, not independence.

The positivity statements in (38) use \(e_\ell\ge f_\ell>0\), obtained from the nonnegative square \(E[(\phi'(X_1)-\phi'(X_2))^2]\) and positivity of the gates. Since \(|\rho|\le1\), \(e_1\pm\rho f_1\ge0\). For the small forward entry,
\[
e_1-\rho f_1=(e_1-f_1)+\theta f_1\le2\gamma^2\theta,
\]
which gives the stated \(3\Delta\gamma^2\theta/2\) bound after adding \(\Delta\kappa_1\).

For matrix 3, the small entry in (30) is bounded by
\[
\Delta\kappa_2+\kappa_2\,\Delta(a^2+\gamma^2)
+\gamma^2\left(\frac32\Delta\gamma^2\theta\right)
\le\Delta\gamma^4\theta\left(2+\frac{a^2+\gamma^2}{2}\right).
\]
This confirms the constant in the third line of (38). Equations (39) follow directly from the two initial gate moments and the bound on \(t_3\). No sign of \(t_3\) is needed or asserted.

With the identity middle cut, \(a_2=e_2,b_2=f_2\). The centered independent noise in \(Q_1\) has zero contribution to \(E[\phi''(X_1)Q_1]\), so
\[
c_2=\Delta(\beta_+t_2+\beta_-s_2).
\]
This proves (40)–(41), including the \(\Delta t_3e_2\) current contribution.

For (42), use
\[
e_3e_2-f_3f_2=e_3(e_2-f_2)+f_2(e_3-f_3),
\]
along with \(|s_2|\le a\gamma\), \(|\beta_+|\le\gamma^2+2\kappa_3\), and \(|\beta_-|\le3\kappa_3\). These give exactly the displayed three bounds. They are uncut statements. In particular, a sign for the cut historical \(-,+\) entry cannot be deduced by silently replacing its weighted integrals \(a_2,b_2\) with \(e_2,f_2\).

For every \(\rho<1\), strict monotonicity and the positive variance of the initial differences also imply \(\kappa_\ell>0\) successively through the three layers. This is consistent with, but does not strengthen, the upper angle estimates into a uniform positive lower bound as \(\rho\uparrow1\).

## 8. Actual first-query bounds, including the Gaussian contribution

Candidate lines 839–897 pass. Equation (43) controls the actual half-difference of the first middle reverse query, not merely its deterministic response coefficients.

From the exact first-query law,
\[
q^{(2)}_{1,-}=\Delta(\eta_-+\beta_-U^{(2)}_0).
\]
The response coefficient satisfies \(|\beta_-|\le3\kappa_3\). For its Gaussian source,
\[
\|\eta_-\|_2^2=E_3[V^2p_-^2]\le E_3[V^4].
\]
The top initial difference \(D=X^{(3)}_1-X^{(3)}_2\) is a centered Gaussian with variance \(4\kappa_2\). The one-dimensional Gaussian fourth-moment identity gives
\[
E[D^4]=3(4\kappa_2)^2,
\]
also valid at zero variance. Therefore
\[
\sqrt{E_3[V^4]}
\le\frac{\gamma^2}{4}\sqrt{E[D^4]}
=\sqrt3\,\gamma^2\kappa_2.
\]
The factor \(1/4\) here is the square of the half-difference normalization; it cancels the factor \(4\) from \(\sqrt{(4\kappa_2)^2}\). This verifies the potentially delicate fourth-moment constant.

Using \(\|U^{(2)}_0\|_2\le a\) now gives
\[
\|q^{(2)}_{1,-}\|_2
\le\Delta(\sqrt3\,\gamma^2\kappa_2+3a\kappa_3)
\le\frac{\Delta\gamma^6}{2}(\sqrt3+3a)(1-\rho).
\]
This proves both inequalities in (43). No product such as \(E[V^2p_-^2]\) was factorized. The fourth moment used is an exact initial Gaussian moment, not a consequence claimed from a general second-moment energy estimate.

Similarly,
\[
\|\eta_+\|_2\le\gamma\sqrt{\kappa_3},\qquad
|\beta_+|\le\gamma^2+2\kappa_3,\qquad
\|V^{(2)}_0\|_2=\sqrt{\kappa_2},
\]
which proves (44). Hence the stated \(O(\Delta\sqrt{1-\rho})\) average-query upper bound and \(O(\Delta(1-\rho))\) difference-query upper bound follow. These are upper bounds, not claims of matching asymptotics.

Both estimates hold for any finite first step \(\Delta>0\) and all allowed finite caps: this query precedes the middle cut, and all its first-update inputs and top coefficients are independent of the cap sizes. They do not require \(M\Delta\le3/2\). This argument does not produce a corresponding later-time estimate or a bottom-query contrast bound.

## 9. Audit of the supplied short-response bootstrap

The bootstrap was also read in full. Its scalar-law response estimates in Sections 2–6 check out on their stated horizon \(S=M\Delta\le3/2\). This is an additional check of the supplied source, not an import of its unaudited finite-width identification dependency.

Its activation bound \(a_{\mathrm b}=7/6\) differs from the candidate's sharper \(a=1+\pi/20\); both are valid and were not interchanged.

The induction is noncircular. Past \(U_r,V_r\le1\) first bound the bottom sensitivities and \(A^{(2)}\), then the middle sensitivities and \(A^{(3)}\), then current \(V_k\), and only then current \(U_k\). The current return is included in the last derivative row.

For a single bottom reverse-source injection, the coefficient is at most \(\Delta/20\) before the output feature gate, and at most \(\Delta/200\) after it. The remaining multiplier is
\[
\Delta\left(\max_a|q^{(1)}_{ra}|/5+U_r/100\right).
\]
The stated discrete product bound therefore gives bootstrap (6). The Gaussian maximum bound
\[
E e^{\lambda\max(|G_1|,|G_2|)}
\le\sum_a E e^{\lambda|G_a|}
\le4e^{\lambda^2v/2}
\]
requires no independence of the two coordinates. Time Jensen requires no independence between times. These justify (8) and hence
\[
|A^{(2)}_{ja,sb}|
<\frac{\Delta}{2}\left(\frac{49}{36}+\frac{3}{50}\right)
<\frac{3\Delta}{4}.
\]

For the middle forward-source derivative row, there is exactly one direct current injection per output sample. Summing the two update samples cancels the \(1/2\) in the coefficient bound, giving the multiplier \(A\Delta\), where \(A=3/2\). The reverse-source feature injection is \(A\Delta/200\). Thus (10)–(11) have the correct factors.

The Gaussian envelope gives
\[
E(E^{(2)}_j)^p
\le4\exp\left(\frac{219p}{400}+\frac{3969p^2}{1280000}\right).
\]
For \(p=2\), taking the square root gives the exponent
\[
\frac{219}{400}+\frac{7938}{1280000},
\]
exactly as in (13). The stated elementary comparisons imply \(EE^{(2)}_j<8\) and \(\|E^{(2)}_j\|_2<7/2\). Consequently
\[
|A^{(3)}_{ja,sb}|
<\frac{\Delta}{2}\left(\frac{49}{36}+\frac{3}{25}\right)
=\frac{\Delta}{2}\frac{1333}{900}
<\frac{3\Delta}{4}.
\]

For the top backward derivative row, the readout derivative contributes at most \(S/100\) times the maximum preactivation derivative row, and the gate derivative contributes \(a_{\mathrm b}S/5\). Their sum is \((73/300)S\), confirming the constant in Section 5. The ensuing exponent is at most \(657/800\), and its bound by \(5/2\) is valid. The learned covariance row contributes \(a_{\mathrm b}^2S^3/100\), including exactly two sample terms. Hence
\[
V_k\le\frac{73}{80}+\frac{147}{3200}
=\frac{3067}{3200}.
\]

The resulting query bound is
\[
Q_*=\frac{7}{40}+\frac76\frac{3067}{3200}
=\frac{24829}{19200}.
\]
The current middle derivative includes
\[
\left(|q^{(2)}_{ka}|/5+V_k/100\right)E^{(2)}_k.
\]
Cauchy–Schwarz, not independence, bounds its expectation. Adding the learned covariance row gives exactly
\[
U_k\le\frac72(Q_*/5+V_*/100)+\frac3{200}Q_*^2
=\frac{71063018523}{73728000000}<\frac{97}{100}.
\]
For example, the two summands have numerators \(69213580800\) and \(1849437723\) over the displayed common denominator, confirming the quoted rational constant.

Finally \(q=\zeta+\beta\), \(|\beta|\le a_{\mathrm b}\), with \(\operatorname{Var}\zeta\le49/1600\), implies
\[
Ee^{q^2/16}
\le e^{49/288}Ee^{\zeta^2/8}
\le e^{49/288}(1-49/6400)^{-1/2}<2.
\]
This uses the elementary inequality \(q^2\le2\zeta^2+2a_{\mathrm b}^2\) and a scalar Gaussian integral; it does not require independence of \(\beta\) and \(\zeta\). Thus the bootstrap's short-time, mesh/cap-uniform query envelopes have no hidden independence assumption.

The bootstrap's common-label clock discussion is expressly conditional on an uncut gradient flow, symmetry, and cut removal. Under those premises its lower readout contribution \(m^2\) and reciprocal time \(1/m^2=36/25\) are consistent. It is not an unconditional existence or clipping-removal proof. Its finite-program identification and eventual physical-time obligations remain outside this audit.

## 10. Later-time terms and limits of the result

Candidate lines 899–965 correctly identify actual terms left for a continuation argument.

Differentiating \(d_-=p_+q_-+p_-q_+\) gives exactly (45). In its last line the two terms of (46) have parities
\[
(\text{odd})(\text{odd})(\text{even}),\qquad
(\text{even})(\text{odd})(\text{odd}),
\]
respectively, since differentiation is in an even forward source. Both products are even. Symmetry therefore does not force either expectation to vanish.

Differentiating the minus preactivation equation in a plus source gives (47). There is no direct injection, but the historical derivatives of \(d_{v,+}\) remain. Even with frozen deterministic coefficients, these are nontrivial, correlated same-population fields. The factor \(c_-=\nu V\) in the first expression does not justify extracting an \(L^2\) contrast norm from an \(L^2\) product; the second expression also needs control of the contrast sensitivity itself.

The quoted putative inequality
\[
\|Vq\|_2\le\|V\|_2\|q\|_2
\]
is not a general product inequality. Available generic inequalities instead require different moments, such as \(\|Vq\|_2\le\|V\|_4\|q\|_4\), or an actual independence statement. The ten independent Gaussian source groups supply neither independence of these evolved fields nor a later-time analogue of the initial Gaussian contrast fourth-moment calculation. With cuts, the mixed derivatives in (19) must remain.

The result has the following precise boundaries:

| Assertion | Audited scope |
|---|---|
| Exact finite modal law, symmetry, coefficient identities, derivative rules | Any fixed finite mesh and allowed finite caps, within the stipulated law |
| Identity-cut formulas and finite derivative expectations | A separately defined fixed finite identity-cut law; not a proved cap-removal limit |
| Exact first-update \(A,B\) values | \(M\ge1\), with historical/current slots kept distinct |
| Actual query bounds (43)–(44) | First middle reverse query, arbitrary finite \(\Delta>0\), uniformly in both caps |
| Bootstrap row bounds and exponential query envelopes | Feature time \(M\Delta\le3/2\), uniformly in mesh/caps, within its stated scalar law |
| Singular endpoint \(\rho=-1\) | Included; attained root plus mode is zero and formal slots remain |
| Approach to \(\rho=1\) | The candidate's upper angle bounds tend to zero; no uniform contrast lower bound is asserted |
| Width identification, continuous-time construction, global continuation, both-cap removal, physical-time/GD comparison | Not established or certified here |

The candidate does not infer energy dissipation for internally clipped propagation from the uncut gradient identity. It does not infer global response tails from a second-moment/action estimate. The external uncut-action source mentioned in Section 8 was not consulted and is not needed for any accepted calculation above.

The finite-law claims and the first-query bound are therefore supported at the stated hashes. The remaining continuation obstacles are acknowledged limitations, not concealed assumptions in the proved finite statements.

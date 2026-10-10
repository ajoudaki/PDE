# Independent audit: arbitrary-depth initialization activity

Date: 2026-10-10.

## Verdict and scope

The backward Gram positivity and joint feature-acceleration arguments are mathematically sound after supplying their conditioning and normalization details. I found no counterexample to the stated compatible-data theorem. The current proof nevertheless needs a substantive repair in Section 7: analyticity of the scalar activations does not establish smoothness of the population vector field on its stated mean-square spaces. The displayed higher-order big-O remainders are not justified by the cited local theorem. Strong initial asymptotics with little-o remainders suffice, and a direct repair is given below.

This audit read the complete frozen candidate `COMPATIBLE_RESULT.md`; the setup in `paper/compact.tex` (and the complete file, without following its input files); the complete `docs/notation.qmd`; `docs/02-gaussian-reuse.qmd` Sections 1–2, 5.4, and A.1–A.4; and `docs/03-local-population.qmd` C.1, C.3, and the complete three-layer feature-activity Section 8. The local flow theorem is used as an established result; its separate mesh-uniform response proof C.2 and the finite-program proof in Chapter 12 were not independently re-audited. The canonical-notation skill, its neural-network reference, and the rigorous-mathematics skill were read. No other study, prior check, or prior verdict was read.

## 1. Conditioning remains valid at arbitrary fixed depth

Fix a layer index \(1\le\ell<L\). At finite width write

\[
 W=W_0^{(\ell+1)},\quad
 H=[h_{0,1}^{(\ell)},\ldots,h_{0,m}^{(\ell)}],\quad
 Z=WH,
\]

and let \(U=[b_1^{(\ell+1)},\ldots,b_m^{(\ell+1)}]\) be the upper response tuple obtained from the candidate's recursion, with lower-case letters denoting finite arrays. All four matrices except \(W\) have \(m\) columns.

Condition on every initialized weight block other than \(W\), and on \(Z=WH\). Then \(H\) is known. Every forward array at layer \(\ell+1\) and above is determined by \(Z\) and the conditioned higher matrices. The top response \(b_a^{(L)}=(\sum_b y_bh_{0,b}^{(L)})\odot\phi_L'(z_{0,a}^{(L)})\) is therefore known, and descending through matrices \(W_0^{(L)},\ldots,W_0^{(\ell+2)}\) determines \(U\). None of those descending steps uses \(W^T\). Thus \(U\) depends on \(W\) only through the recorded forward outputs \(Z\). This proves the conditional-residual independence required here at every fixed depth. It would generally fail for an unspecified trained-time backward vector, but the candidate uses only initialization.

Define the empirical contractions

\[
 Q_n=H^TH/n,\qquad C_n=Z^TU/n,\qquad D_n=U^TU/n,
 \qquad P_H=H(H^TH)^{-1}H^T.
\]

On the event that \(Q_n\) is invertible, Gaussian orthogonal decomposition gives the exact conditional identity

\[
 W^TU
 \overset d=H Q_n^{-1}C_n+(I-P_H)\Xi D_n^{1/2},
 \tag{A1}
\]

where \(\Xi\in\mathbb R^{n\times m}\) has independent standard Gaussian entries and is independent of everything conditioned on. In particular, the innovation covariance is \(D_n\), with no subtraction of a response covariance. At finite width its rows are projected and are not independent. The omitted projection has the explicit bound

\[
 \mathbb E\!\left[
 \frac1n\|P_H\Xi D_n^{1/2}\|_F^2
 \;\middle|\;\text{conditioned data}\right]
 =\frac{\operatorname{rank}(H)}n\operatorname{tr}D_n
 \le\frac mn\operatorname{tr}D_n.
 \tag{A2}
\]

The forward Gram limit is positive definite, so \(Q_n\) is invertible with probability tending to one and its inverse stays bounded in probability. The fixed initialization forward/backward program has convergent same-layer second moments: its coordinate operations are Lipschitz activations, linear combinations, and products of a bounded continuous derivative with an \(L^2\) field. These are precisely the fixed-program operations covered by the established value extension in Chapter 2, A.1. There are finitely many instructions, and the initialized Gaussian actions have bounded operator norms with probability tending to one. Thus \(C_n\to C\), \(D_n\to D^{(\ell+1)}\), and \(\operatorname{tr}D_n\) is bounded in probability. Formula (A2) removes the projection in normalized mean square. Conditional Gaussian averaging then gives the population law

\[
 (W_0^{(\ell+1)})^*B_a^{(\ell+1)}
 =\sum_bH_b^{(\ell)}
   [(Q^{(\ell)})^{-1}C]_{ba}+\Gamma_a,
 \tag{A3}
\]

\[
 C_{ba}=\mathbb E_{\ell+1}[Z_b^{(\ell+1)}B_a^{(\ell+1)}],
 \qquad
 \Gamma\sim N(0,D^{(\ell+1)}),
\]

with \(\Gamma\) independent of the initial lower tuple \(Z^{(\ell)}\). This is a joint law in the lower population; it does not identify coordinates from different neuron populations.

Multiplying (A3) by \(\phi_\ell'(Z_a^{(\ell)})\), the conditional variance of \(\sum_a c_aB_a^{(\ell)}\) is

\[
 \bigl(c\odot\phi_\ell'(Z^{(\ell)})\bigr)^T
 D^{(\ell+1)}
 \bigl(c\odot\phi_\ell'(Z^{(\ell)})\bigr).
\]

The conditional second moment is this variance plus a nonnegative squared conditional mean. This proves candidate inequality (8) exactly at the population level. Every marginal \(Z_a^{(\ell)}\) is nondegenerate Gaussian. The derivative of a nonconstant analytic activation has a discrete zero set unless it is identically zero, so its squared value has positive expectation. Therefore

\[
 c^TD^{(\ell)}c
 \ge\lambda_{\min}(D^{(\ell+1)})
 \sum_a c_a^2\mathbb E_\ell[\phi_\ell'(Z_a^{(\ell)})^2]>0
 \qquad(c\ne0).
\]

At the top layer the candidate's analytic product argument is valid. A nonzero analytic first factor is nonzero on a nonempty open set; the second factor vanishes there and hence everywhere. Varying one coordinate and using the nonconstant derivative forces all coefficients to zero. Combined with (A3), this closes the depth induction.

The first-layer forward Gram argument is also valid: differentiate a putative ridge identity in a direction nonorthogonal to every input, and apply bounded ridge-function independence to the nonconstant bounded derivative. The later forward Gaussian tuples have full support because their covariance Grams are positive definite. No input-Gram invertibility was used.

## 2. Exact normalized adjoint identity

Put \(k=2/m\). The candidate's response satisfies exactly

\[
 \dot\delta_a^{(\ell)}(0)=k b_a^{(\ell)}.
\]

Indeed \(\dot w(0)=k\sum_b y_bh_{0,b}^{(L)}\), every hidden velocity initially vanishes, and the backward recursion differentiates without additional terms. Let \(V_\ell=\ddot W^{(\ell)}(0)\). The exact accelerations are

\[
 V_1=k^2\sum_a y_ab_a^{(1)}v_a^T,
 \qquad
 V_\ell=\frac{k^2}{n}\sum_a y_ab_a^{(\ell)}h_{0,a}^{(\ell-1)T}
 \quad(\ell\ge2).
 \tag{A4}
\]

Use \(\|V_1\|_{\mathrm{mob}}^2=\|V_1\|_F^2/n\) and
\(\|V_\ell\|_{\mathrm{mob}}^2=\|V_\ell\|_F^2\) for \(\ell\ge2\), exactly as required by the paper's Euclidean mobility coordinates. Let \(r_a^{(\ell)}=\ddot z_a^{(\ell)}(0)\) and \(a_a^{(\ell)}=\ddot h_a^{(\ell)}(0)\). Then

\[
 r_a^{(1)}=V_1v_a,\qquad
 r_a^{(\ell)}=V_\ell h_{0,a}^{(\ell-1)}
                  +W_0^{(\ell)}a_a^{(\ell-1)},
 \qquad
 a_a^{(\ell)}=\phi_\ell'(z_{0,a}^{(\ell)})\odot r_a^{(\ell)}.
\]

For the learned-link term at \(\ell\ge2\), (A4) gives

\[
 \sum_a\frac{y_a}{n}(b_a^{(\ell)})^T
        V_\ell h_{0,a}^{(\ell-1)}
 =\frac1{k^2}\|V_\ell\|_F^2.
\]

The propagated term obeys

\[
 \sum_a\frac{y_a}{n}(b_a^{(\ell)})^T
       W_0^{(\ell)}a_a^{(\ell-1)}
 =\sum_a\frac{y_a}{n}(b_a^{(\ell-1)})^T r_a^{(\ell-1)},
\]

by the actual transpose recursion and the activation multiplier in \(a_a^{(\ell-1)}\). At the first layer the learned-link pairing is \(\|V_1\|_F^2/(nk^2)\). Consequently the exact finite-width identity is

\[
 \sum_a\frac{y_a}{n}(b_a^{(\ell)})^T r_a^{(\ell)}
 =\frac{m^2}{4}
   \sum_{j=1}^{\ell}\|\ddot W^{(j)}(0)\|_{\mathrm{mob}}^2.
 \tag{A5}
\]

The same identity holds in the population spaces with normalized finite pairings replaced by \(\mathbb E_\ell\), the first norm replaced by the \(L^2\) norm of its \(\mathbb R^d\)-valued row, and middle norms replaced by Hilbert–Schmidt norms. Initial actions themselves are not being asserted Hilbert–Schmidt.

Thus candidate (15) has the single coefficient \(c_j=m^2/4\) for every block under the stated mobilities. The candidate's entrywise-Gram proof makes each squared norm on the right strictly positive. Therefore the joint preactivation acceleration is nonzero at every layer. Since multiplication by \(\phi_\ell'(Z_a^{(\ell)})\) has zero kernel in \(L^2\), the joint feature acceleration is nonzero as well. This last implication needs no lower bound on the derivative away from zero, only its almost-sure nonvanishing.

## 3. Repairing the passage to positive time

Section 7 should not invoke a smooth population vector field merely from scalar analyticity. For example, even for an analytic bounded-derivative function such as \(\tanh\), the map \(X\mapsto\tanh X\) is not Fréchet differentiable at zero on a nonatomic \(L^2\) space: for \(X_j=c\mathbf1_{E_j}\), with fixed \(c\ne0\) and \(\Pr(E_j)\downarrow0\), the normalized linearization error is the nonzero constant \(|\tanh c-c|/|c|\). The maintained source explicitly distinguishes its valid strong curve chain rule from such a Fréchet claim.

Here only strong initial limits are needed. The local theorem supplies a strong flow, continuity of all fields in \(L^2\), and continuity of learned actions in operator norm. Its integral equations first yield

\[
 w(t)/t\longrightarrow kS,
 \qquad
 \delta_a^{(\ell)}(t)/t\longrightarrow kB_a^{(\ell)}
 \quad\text{in }L^2,
 \tag{A6}
\]

the second limit following downward using bounded continuous activation derivatives and the same initialized actions and adjoints. For completeness, if \(X_j\to X\) in probability, \(U_j\to U\) in \(L^2\), and \(b\) is bounded continuous, then \(b(X_j)U_j\to b(X)U\) in \(L^2\): subtract the varying \(U_j\), then truncate the fixed integrable variable \(|U|^2\). This is exactly the multiplier fact needed at each step.

Substitution into the parameter integral equations gives

\[
 W^{(\ell)}(t)-W_0^{(\ell)}
 =\tfrac12t^2V_\ell+o(t^2),
\]

in the first-row \(L^2\) norm and middle Hilbert–Schmidt norms. For a middle update, the assertion follows from convergence of both factors in each of its finitely many rank-one terms; the Hilbert–Schmidt norm of \(U\otimes V\) is \(\|U\|_2\|V\|_2\). Forward recursion and the strong curve chain rule then give

\[
 H_a^{(\ell)}(t)-H_a^{(\ell)}(0)
 =\tfrac12t^2A_a^{(\ell)}+o_{L^2}(t^2).
\]

Thus the justified population replacement for candidate (17) is

\[
 \sum_a\mathbb E_\ell
   |H_a^{(\ell)}(t)-H_a^{(\ell)}(0)|^2
 =\frac{t^4}{4}\sum_a\|A_a^{(\ell)}\|_{L^2}^2+o(t^4),
 \tag{A7}
\]

whose leading coefficient is strictly positive by (A5). The population formula must use population fields, not the finite-width left side currently displayed in (17). Path-law convergence in \(\mathcal W_2\) then transfers the strict bound to finite width for each fixed sufficiently small positive time. No exchange of a finite-width Taylor remainder with the width limit is necessary.

The cubic separation can be repaired by the same strong limits. Write
\(E=\sum_{\ell=1}^L\|V_\ell\|_{\mathrm{mob}}^2>0\), using population norms. For the tangent kernel \(K(t)\) with prediction equation \(\dot f=-kK(t)(f-y)\), (A6) gives

\[
 y^TK_{\mathrm{hidden}}(t)y=(E/k^2)t^2+o(t^2).
\]

The readout block is the top feature Gram. Applying (A5) at layer \(L\), its change satisfies

\[
 y^T\{K_{\mathrm{readout}}(t)-K(0)\}y
 =t^2\sum_a y_a\mathbb E_L[B_a^{(L)}R_a^{(L)}]+o(t^2)
 =(E/k^2)t^2+o(t^2).
\]

All entries of \(K(t)-K(0)\) are \(O(t^2)\). Subtracting the frozen-kernel equation and applying variation of constants therefore yields

\[
 y^T\{f(t)-f_{\mathrm{NTK}}(t)\}
 =\frac{2E}{3k}t^3+o(t^3)
 =\frac m3Et^3+o(t^3).
 \tag{A8}
\]

In this calculation \(f(t)=O(t)\); replacing the residual by \(-y\) and the fixed propagator by the identity changes the integral only by \(O(t^4)\). This proves the claimed sign without an unproved population smoothness statement. It also confirms the coefficient in candidate (16).

Finally, the positive affine-fit error follows from the explicit continuous formula

\[
 \operatorname{Var}(\phi_\ell(Z_a^{(\ell)}(t)))
 -\frac{\operatorname{Cov}(Z_a^{(\ell)}(t),
                    \phi_\ell(Z_a^{(\ell)}(t)))^2}
        {\operatorname{Var}(Z_a^{(\ell)}(t))}.
\]

The denominator is initially positive and remains so on a short interval. The Lipschitz activation and mean-square continuity make all moments continuous. This supplies the detail implicit in Section 6. Formula (4) should index the sample explicitly, or state that the positive lower bound holds for all finitely many sample marginals.

The required repairs are therefore: insert (A1)–(A3) or equivalent conditioning details; replace the unspecified constants in (15) by the normalized identity (A5); and replace the smooth-vector-field argument and unsupported big-O remainders in Section 7 by the strong little-o expansions (A6)–(A8). These repairs preserve the theorem's stated strict fixed-time conclusions.

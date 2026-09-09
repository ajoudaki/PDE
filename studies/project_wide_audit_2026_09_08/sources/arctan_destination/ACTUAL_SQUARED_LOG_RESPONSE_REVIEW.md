# Independent audit of ACTUAL_SQUARED_LOG_RESPONSE

Verdict: **PASS for the finite-width response lemma in its explicitly stated raw canonical Euclidean metric.** The displayed constants and inequalities (2)–(10), including the fixed-physical-time derivative and the canonical independent top-column probe, are valid. I found no omitted trained Hessian term, missing power of n, eigenvalue-multiplicity obstruction, or unjustified population-limit transfer in these conclusions.

Two scope clarifications are necessary when describing this PASS: the earlier logarithmic comparison uses a different first-layer coordinate, so “strengthens” must not assert an unproved identification of the two response spectra; and the amplitude limitation means absence of a width-uniform normalized amplitude bound, rather than absence of every finite-width bound. These clarifications are made precise below. Neither requires changing the candidate's displayed inequalities.

This is an independent mathematical audit, not an endorsement of the candidate's conclusions by reference. All four permitted mathematical files were read completely. The solve-math-rigorously instructions were read directly. No other mathematical files, ledgers, reviews, or agents' files were inspected; no numerical experiments or external searches were used. References inside the permitted dependencies to further files were not followed.

## Reviewed inputs and SHA256 identities

The abbreviations C, H, R, and L below refer to these exact files. Line references use the reviewed versions.

| ID | File | SHA256 |
| --- | --- | --- |
| C | [ACTUAL_SQUARED_LOG_RESPONSE.md](/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/ACTUAL_SQUARED_LOG_RESPONSE.md) | c213afd849bd9dd012634e91877fac0b801f4f5fed380b52a2b91142ced628fa |
| H | [ACTUAL_HIDDEN_GRAPH_VOLUME.md](/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/ACTUAL_HIDDEN_GRAPH_VOLUME.md) | 7b70789e567d8c17d0f6ad1c7b4ab703fc9d0ed385863bf38bb8f81b80eeff7e |
| R | [READOUT_COERCIVITY.md](/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/READOUT_COERCIVITY.md) | 0bd062da74fbde03d41a125561beee7345915ea6aa0578ed8e7b81d2c9f08c53 |
| L | [LOGARITHMIC_NETWORK_COMPARISON.md](/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/LOGARITHMIC_NETWORK_COMPARISON.md) | adc98d1f9fe2c23560afc649e9107e2125a87aca1c94ee5db9a4f43e7034f480 |

The dependency actually needed for the probabilistic corollary is R's finite-width primal control and initialization estimates. H's relevant Hessian calculation is independently checked below. L is relevant to normalization and to the comparison of scope, not a premise of the new squared-logarithmic differential argument. This review does not certify unrelated assertions in the dependencies whose proofs refer to disallowed files.

## 1. Raw Gaussian coordinates and the exact trained field

Let \(N=2n^2+2n\), \(n\ge1\), and write the full canonical state as
\[
 y=(z^{(1)},A_2,A_3,c),\qquad
 A_2=\sqrt n\,W^{(2)},\quad A_3=\sqrt n\,W^{(3)}.
\]
Here \(A_2,A_3\) are coordinate names in this paragraph, not the mobility matrices appearing in R. The metric is the ordinary Euclidean direct-sum metric, with ordinary Frobenius metrics on the two matrix blocks.

In particular, a variation \((u_1,E_2,E_3,v)\) means
\[
 dz^{(1)}=u_1,\quad dW^{(2)}=E_2/\sqrt n,\quad
 dW^{(3)}=E_3/\sqrt n,\quad dc=v.
\]
Under the initialization in C, the hidden entries \(z^{(1)},A_2,A_3\) are independent standard Gaussians. The readout c is deliberately not whitened: its entries have variance \(n^{-2}\). A theorem in the metric that instead uses nc as its readout coordinate would be a different theorem.

Set \(D_\ell=\operatorname{diag}(\phi'(z^{(\ell)}))\). Direct differentiation of \(\mathcal P=c^Th^{(3)}\) gives
\[
 \nabla\mathcal P=
 \left(
 \delta^{(1)},\
 \frac{\delta^{(2)}(h^{(1)})^T}{\sqrt n},\
 \frac{\delta^{(3)}(h^{(2)})^T}{\sqrt n},\
 h^{(3)}
 \right)=b.
\]
For example,
\[
 d\mathcal P[E_2]
 =(\delta^{(2)})^TE_2h^{(1)}/\sqrt n,
\]
which establishes the matrix gradient with precisely the displayed scaling. R's feature equations have \((W^{(j)})'=\delta^{(j)}(h^{(j-1)})^T/n\); multiplying by \(\sqrt n\) gives exactly these canonical matrix blocks. The first and readout blocks agree with R as well.

Thus \(y'=b=\nabla\mathcal P\) in feature time. Since \(f_n=\mathcal P/n\), the physical field prescribed by R's normalized training metric is \(2(1-f_n)b\). One must not replace it with ordinary Euclidean gradient descent on the loss in y, which would introduce a different overall factor n.

For completeness, R's original parameter norm and the present norm satisfy
\[
 |dy|^2=n\left(
 \frac{|dz^{(1)}|^2}{n}+\|dW^{(2)}\|_F^2+
 \|dW^{(3)}\|_F^2+\frac{|dc|^2}{n}
 \right).
\]
This is a constant global metric rescaling after the linear coordinate change. No nonlinear \(F(z^{(1)})\) is used in C.

**Finding:** C lines 17–53 have the correct powers of n, first-layer variable, readout scaling, and feature-time field.

## 2. Every trained Hessian term

For a hidden variation \(u=(u_1,E_2,E_3)\), the first preactivation variations are exactly
\[
 T_1u=u_1,\quad
 T_2u=E_2h^{(1)}/\sqrt n+W^{(2)}D_1u_1,
\]
\[
 T_3u=E_3h^{(2)}/\sqrt n+W^{(3)}D_2T_2u.
\]
Along the straight parameter line, product differentiation gives
\[
 d^2z^{(2)}[u,u]
 =2E_2D_1u_1/\sqrt n+
 W^{(2)}\bigl(\phi''(z^{(1)})\odot u_1^2\bigr),
\]
\[
 d^2z^{(3)}[u,u]
 =2E_3D_2T_2u/\sqrt n+
 W^{(3)}\left[
 \phi''(z^{(2)})\odot(T_2u)^2+
 D_2d^2z^{(2)}[u,u]\right].
\]
All squares here are coordinatewise. Contracting
\[
 d^2h^{(3)}[u,u]
 =\phi''(z^{(3)})\odot(T_3u)^2+D_3d^2z^{(3)}[u,u]
\]
with c yields the following symmetric operator:
\[
\begin{aligned}
 A={}&T_1^T\operatorname{diag}(\phi''(z^{(1)})\odot q^{(1)})T_1\\
 &+T_2^T\operatorname{diag}(\phi''(z^{(2)})\odot q^{(2)})T_2\\
 &+T_3^T\operatorname{diag}(\phi''(z^{(3)})\odot c)T_3\\
 &+S_2^TD_1T_1+T_1^TD_1S_2\\
 &+S_3^TD_2T_2+T_2^TD_2S_3,
\end{aligned}
\]
where \(S_2u=E_2^T\delta^{(2)}/\sqrt n\) and
\(S_3u=E_3^T\delta^{(3)}/\sqrt n\).

The first three terms account for all three differentiated activation gates. The last two symmetric pairs account for differentiating the two trained weight matrices. In particular, the dependence of the top layer on the variation of the middle layer is inside \(T_3\), and the two matrix variations are not frozen.

There is a separate readout variation. Since \(\mathcal P\) is linear in c and \(J=D_xh^{(3)}=D_3T_3\), the full Hessian is
\[
 B=D^2\mathcal P=
 \begin{pmatrix}A&J^T\\J&0\end{pmatrix}.
\]
Its full quadratic form is \(u^TAu+2v^TJu\), so the trained-readout mixed terms are retained and there is no c–c Hessian term.

An independent first-derivative check of the backward chain gives
\[
 d\delta^{(3)}=D_3v+
 \operatorname{diag}(c\odot\phi''(z^{(3)}))T_3u,
\]
\[
 dq^{(2)}=E_3^T\delta^{(3)}/\sqrt n+(W^{(3)})^Td\delta^{(3)},
\quad
 d\delta^{(2)}=D_2dq^{(2)}
 +\operatorname{diag}(q^{(2)}\odot\phi''(z^{(2)}))T_2u,
\]
\[
 dq^{(1)}=E_2^T\delta^{(2)}/\sqrt n+(W^{(2)})^Td\delta^{(2)},
\quad
 d\delta^{(1)}=D_1dq^{(1)}
 +\operatorname{diag}(q^{(1)}\odot\phi''(z^{(1)}))u_1.
\]
Differentiating the forward factors in the two matrix gradient blocks additionally gives
\(\delta^{(2)}(D_1u_1)^T/\sqrt n\) and
\(\delta^{(3)}(D_2T_2u)^T/\sqrt n\).
These are exactly the same terms encoded by the symmetric Hessian above.

**Finding:** C (6) and its full block completion are correct, including all trained factors. This also independently verifies the relevant identity in H.

## 3. The explicit RMS-only Frobenius constant

Assume the two hidden operator norms are at most \(M\ge0\) and
\(\|c\|_2/\sqrt n\le R\), \(R\ge0\). Since
\[
 |\phi|\le a,\quad \|D_\ell\|_{\rm op}\le1,\quad
 |\phi''(z)|=\frac{2|z|}{(1+z^2)^2}\le2,
\]
the direct-sum variation norm gives
\[
 \|T_1\|_{\rm op}=1,\quad
 \|T_2\|_{\rm op}\le a+M=K_2,\quad
 \|T_3\|_{\rm op}\le a+MK_2=K_3.
\]
These bounds are conservative but valid; for example each of
\(\|u_1\|_2,\|E_2\|_F,\|E_3\|_F\) is at most \(\|u\|_2\).
Also
\[
 \|\delta^{(3)}\|_2\le R\sqrt n,\quad
 \|q^{(2)}\|_2,\|\delta^{(2)}\|_2\le MR\sqrt n,\quad
 \|q^{(1)}\|_2\le M^2R\sqrt n,
\]
\[
 \|S_2\|_{\rm op}\le MR,\qquad \|S_3\|_{\rm op}\le R.
\]

For a diagonal matrix D of either sign,
\[
 \|T^TDT\|_F\le\|T\|_{\rm op}^2\|D\|_F,
\]
by applying the Frobenius ideal inequalities on the left and right.
Consequently the three gate Hessians contribute at most
\[
 2M^2R\sqrt n,\qquad
 2MK_2^2R\sqrt n,\qquad
 2K_3^2R\sqrt n.
\]
The operator \(S_2^TD_1T_1\) factors through \(\mathbb R^n\), so its rank is at most n and its operator norm is at most MR. Hence its Frobenius norm is at most \(MR\sqrt n\); adding its transpose costs at most \(2MR\sqrt n\). The other symmetric cross pair costs at most \(2RK_2\sqrt n\).

Finally, J has rank at most n and operator norm at most \(K_3\). Thus
\[
 \left\|\begin{pmatrix}0&J^T\\J&0\end{pmatrix}\right\|_F
 =\sqrt2\|J\|_F\le\sqrt{2n}K_3.
\]
Adding these six bounds proves precisely
\[
 \|B\|_F\le
 \left[2R(M^2+MK_2^2+K_3^2+M+K_2)+\sqrt2K_3\right]\sqrt n.
\]
This is the stated \(C_B(M,R)\sqrt n\), with no implicit constant.
It is an explicit upper bound, not a claim that the constant is optimal.

No step uses a width-independent \(\|c\|_\infty\), a pointwise bound on either backward query, or a tail estimate. In particular, allowing a readout coordinate as large as \(R\sqrt n\) is consistent with the proof. If \(R=0\), A vanishes at that state, while the off-diagonal J blocks can remain nonzero. The stated constant covers that case too.

**Finding:** C (2), (5), and the complete Frobenius calculation pass exactly.

## 4. Rectangular singular-log energy, repeated eigenvalues, and zero energy

Let \(\mathsf D(t)\) be any continuous real \(N\times N\) matrix on a compact interval \([t_0,t_1]\). Let \(V'=\mathsf D V\) with \(V(t_0)^TV(t_0)=I_m\), \(1\le m\le N\). The square fundamental solution is invertible: its inverse is obtained by solving \(R'=-R\mathsf D\), \(R(t_0)=I_N\), and differentiating the product. Therefore V keeps full column rank.

Set
\[
 G=V^TV>0,\qquad Q=VG^{-1/2},\qquad
 \mathcal E=\frac14\operatorname{Tr}((\log G)^2).
\]
The eigenvalues of G are the squares of all m singular values of V, so
\(\mathcal E=\sum_{j=1}^m(\log\sigma_j(V))^2\).
The \(N-m\) zero eigenvalues of \(VV^T\), when present, are not part of this logarithm.

Here is a trace-differential derivation that does not select differentiable eigenvectors, including at repeated eigenvalues. For a positive definite G,
\[
 \log G=\int_0^\infty
 \left[\frac{I}{1+r}-(G+rI)^{-1}\right]\,dr.
\]
This follows by diagonalizing the single fixed symmetric matrix and integrating the scalar identity. Locally along a positive definite path, its eigenvalues have a positive lower bound. The derivative integrand is bounded at zero and decays as \(r^{-2}\), which justifies differentiating under the integral:
\[
 D\log(G)[H]=\int_0^\infty
 (G+rI)^{-1}H(G+rI)^{-1}\,dr.
\]
By the product rule and cyclicity of trace,
\[
\begin{aligned}
 \mathcal E'
 &=\frac12\operatorname{Tr}\bigl(\log G\,D\log(G)[G']\bigr)\\
 &=\frac12\operatorname{Tr}\left[
 \left(\int_0^\infty(G+rI)^{-1}\log G(G+rI)^{-1}\,dr\right)G'\right]\\
 &=\frac12\operatorname{Tr}((\log G)G^{-1}G').
\end{aligned}
\]
The last equality uses commutation of functions of G and
\(\int_0^\infty(G+rI)^{-2}\,dr=G^{-1}\). No eigenvalue simplicity is needed. This proves the specialization of the trace identity used in C without an additional external theorem.

Writing \(\mathsf D_{\rm sym}=(\mathsf D+\mathsf D^T)/2\), one has
\[
 G'=2V^T\mathsf D_{\rm sym}V
 =2G^{1/2}(Q^T\mathsf D_{\rm sym}Q)G^{1/2}.
\]
Cyclicity and commutation of \(\log G\) with \(G^{1/2}\) now give exactly
\[
 \mathcal E'=\operatorname{Tr}((\log G)Q^T\mathsf D_{\rm sym}Q).
\]
Because Q is an isometry,
\[
 \|Q^T\mathsf D_{\rm sym}Q\|_F\le\|\mathsf D_{\rm sym}\|_F,\qquad
 \|\log G\|_F=2\sqrt{\mathcal E}.
\]
Thus
\[
 |\mathcal E'|\le2\sqrt{\mathcal E}\,\|\mathsf D_{\rm sym}\|_F.
\]

There is no legitimate division by \(\sqrt{\mathcal E}\) at an isometric time, including the initial time. For \(\epsilon>0\), instead,
\[
 \left|\frac d{dt}\sqrt{\mathcal E+\epsilon}\right|
 \le\sqrt{\frac{\mathcal E}{\mathcal E+\epsilon}}\,
 \|\mathsf D_{\rm sym}\|_F
 \le\|\mathsf D_{\rm sym}\|_F.
\]
Integration gives
\[
 \sqrt{\mathcal E(t)+\epsilon}
 \le\sqrt\epsilon+\int_{t_0}^t\|\mathsf D_{\rm sym}(u)\|_F\,du.
\]
Taking \(\epsilon\downarrow0\) proves C (7), including any intervening returns to zero energy.

For feature time, set \(\mathsf D=B=B^T\) and \(V=U(\cdot,s_0)E\). The bound from Section 3 gives C (3). Each counted index in C (4) contributes at least \(r^2\), which proves that count. The proof works for every initial isometry E on the same bounded trajectory. There is no union bound or independence requirement for this pathwise assertion. An E chosen using the trajectory is allowed as a fixed seed map for the variational equation; a time-varying extra seed would require its derivative and is not covered by this argument.

**Finding:** The rectangular argument, its constants, repeated-eigenvalue handling, and the zero-energy passage all pass.

## 5. Derivative at fixed physical time

The physical vector field and its derivative are
\[
 F_{\rm phys}(y)=2(1-\mathcal P(y)/n)b(y),
\]
\[
 DF_{\rm phys}
 =2(1-f_n)B-\frac2n bb^T.
\]
Indeed \(\nabla[2(1-f_n)]=-2b/n\). The negative rank-one term is the derivative of the state-dependent scalar clock factor. Omitting it would give a different response.

The four blocks of b give the exact identity
\[
 \frac{\|b\|_2^2}{n}
 =\frac{\|\delta^{(1)}\|_2^2}{n}
 +\frac{\|\delta^{(2)}\|_2^2\|h^{(1)}\|_2^2}{n^2}
 +\frac{\|\delta^{(3)}\|_2^2\|h^{(2)}\|_2^2}{n^2}
 +\frac{\|h^{(3)}\|_2^2}{n},
\]
and hence
\[
 \|b\|_2^2/n\le M^4R^2+a^2M^2R^2+a^2R^2+a^2=K_b^2.
\]
Also \(|f_n|\le aR\). Since a rank-one \(bb^T\) has Frobenius norm \(\|b\|_2^2\),
\[
 \|B_{\rm phys}\|_F
 \le2(1+aR)C_B\sqrt n+2K_b^2
 \le[2(1+aR)C_B+2K_b^2]\sqrt n.
\]
The final step uses exactly \(n\ge1\). This is C (9).

The derivative of the physical flow at a fixed physical endpoint solves
\(U_{\rm phys}'=B_{\rm phys}U_{\rm phys}\). Applying Section 4 to this equation, rather than to a feature propagator with a clock held fixed, proves the claimed physical-time inequalities. Even at a base state with \(f_n=1\), where the physical trajectory is stationary, its linearization can be \(-2bb^T/n\ne0\); the candidate handles this case correctly.

**Finding:** The sign, factor 2, factor \(1/n\), and all fixed-clock derivative terms pass.

## 6. Actual top-column seed, covariance, and trained increment

Let \(e_i\) select a column of \(W^{(3)}\). In the present coordinates,
\[
 E_i u=(0,0,ue_i^T,0),\qquad E_i^TE_i=I_n.
\]
The corresponding original matrix perturbation is \(ue_i^T/\sqrt n\). Thus the seed is exactly the derivative with respect to the standard Gaussian coordinates of the original initialized top column, with no missing \(\sqrt n\).

For an auxiliary \(g\sim N(0,I_n)\) independent of the base trajectory,
\[
 Y_i=U(s,0)E_i,\qquad
 \operatorname{Cov}_g(Y_ig\mid\text{trajectory})=Y_iY_i^T.
\]
All n singular values of \(Y_i\) are positive. Its covariance has those n nonzero eigenvalues \(\lambda_j=\sigma_j(Y_i)^2\); the exact covariance version of C (3) is
\[
 \sum_{j=1}^n(\log\lambda_j)^2
 =4\sum_{j=1}^n(\log\sigma_j(Y_i))^2
 \le4C_B^2ns^2.
\]
The factor 4 matters when restating the conclusion for covariance eigenvalues. C does not give an incorrect numerical constant for that restatement.

This conditional Gaussian statement is about the independent auxiliary derivative probe. Substituting the actual initialized column itself for g would not preserve independence from the trained trajectory and would not justify that conditional covariance formula.

The derivative of the trained parameter increment is \(Z_i=Y_i-E_i\), with \(Z_i(0)=0\). For every u,
\[
 \|(Y_i-E_i)u\|^2\le2\|Y_iu\|^2+2\|u\|^2,
\]
so \(Z_i^TZ_i\preceq2Y_i^TY_i+2I_n\). The minimum-maximum characterization of ordered eigenvalues implies, for each decreasing index j,
\[
 1+\sigma_j(Z_i)^2\le3+2\sigma_j(Y_i)^2.
\]
One only uses this ordered eigenvalue implication, not an unsupported assertion that the squared matrix logarithm preserves the positive-semidefinite order.

For \(u>0\),
\[
 \log(3+2u^2)\le\log5+2(\log u)_+,
\]
and therefore
\[
 [\log(3+2u^2)]^2
 \le2(\log5)^2+8(\log u)^2.
\]
Summing proves exactly C (10). Zero singular values of \(Z_i\) cause no problem because its scalar function is \(\log(1+\sigma^2)\). The positive constant at \(s=0\) is merely a nonsharp upper bound on zero. The same reasoning applies to the physical propagator with \(C_{\rm phys}\).

### The metric distinction from L

For the original parameter state with raw \(z^{(1)}\) and the normalized norm in Section 1, denote the corresponding seeded response by \(\widetilde Y_i\). Its singular values satisfy
\[
 \sigma_j(\widetilde Y_i)=\sigma_j(Y_i)/\sqrt n,\qquad
 \sigma_j(\widetilde Z_i)=\sigma_j(Z_i)/\sqrt n.
\]
Thus the normalized-raw-metric increment statement would be
\[
 \sum_j[\log(1+n\sigma_j(\widetilde Z_i)^2)]^2
 \le n[2(\log5)^2+8C_B^2s^2].
\]

L instead uses \(X=F(z^{(1)})=z^{(1)}+(z^{(1)})^3/3\), as well as the normalized vector norms. In orthonormal coordinates for L's metric, the derivative of the coordinate change from y is
\[
 \frac1{\sqrt n}H_t,\qquad
 H_t=\operatorname{diag}\bigl(
 \operatorname{diag}(1+(z_i^{(1)}(t))^2),I_{n^2},I_{n^2},I_n\bigr).
\]
Consequently its full propagator is represented by
\[
 U_L(t,t_0)=H_tU_{\rm raw}(t,t_0)H_{t_0}^{-1},
\]
and its top-column maps by
\[
 Y_{L,i}=H_tY_i/\sqrt n,\qquad
 Z_{L,i}=H_tZ_i/\sqrt n.
\]
For the latter identity, \(H_tE_i=E_i\). These are not generally isometric changes in the first-layer block.

Accordingly, C's raw-coordinate conclusion is valid as written, but its introductory comparison with L cannot be read as an automatic squared-log bound with the same constants for L's transformed-coordinate response. Such a transfer would require controlling the displayed endpoint coordinate factors and proving the associated singular-value comparison. The candidate explicitly specifies the raw metric, so this is a restriction on the comparative wording, not a defect in (2)–(10).

**Finding:** The actual seed and increment normalizations pass. Covariance claims are certified in the stated metric and with an independent auxiliary probe.

## 7. A fully explicit high-probability finite-horizon corollary

The candidate's probability assertion can be verified using only the elementary part of R. In particular, one need not assume any population theorem, transfer a zero-readout limit, or even invoke the stronger all-time readout-coercivity conclusion.

Set \(\beta=1/(2a)\), and define the initial event
\[
 \Gamma_n=\left\{
 \|W^{(2)}(0)\|_{\rm op},\|W^{(3)}(0)\|_{\rm op}\le10,\
 \|c(0)\|_2/\sqrt n\le\beta
 \right\}.
\]
For a matrix with independent \(N(0,1/n)\) entries, a Euclidean \(1/4\)-net has at most \(9^n\) points. This cardinality follows by taking a maximal separated set and comparing the volumes of disjoint radius-\(1/8\) balls with the containing radius-\(9/8\) ball. Approximating both unit vectors in a bilinear form shows that the operator norm is at most twice the largest net bilinear form. Each fixed bilinear form is \(N(0,1/n)\), whose two-sided tail at x is at most \(2e^{-nx^2/2}\). Hence
\[
 \Pr(\|W^{(\ell)}(0)\|_{\rm op}>10)
 \le2\,9^{2n}e^{-100n/8}.
\]
Also \(\mathbb E[\|c(0)\|_2^2/n]=n^{-2}\), so Markov's inequality gives
\[
 \Pr(\Gamma_n^c)
 \le4\exp\bigl(n(2\log9-100/8)\bigr)+\frac{4a^2}{n^2}
 \longrightarrow0.
\]
This is an explicit bound for the canonical tiny Gaussian readout, not for an exactly zero substitute.

For any fixed \(T\ge0\), put \(S=3T\). On \(\Gamma_n\),
\(|f_n(0)|\le a\beta=1/2\), so \(e_0=1-f_n(0)\in[1/2,3/2]\).
Along physical flow,
\[
 \dot e=-2\kappa e,\qquad
 \kappa=\|b\|_2^2/n\ge0.
\]
Thus \(0<e(t)\le e_0\) on every finite existence interval, and the physical feature clock satisfies \(0\le s(t)\le2e_0t\le3T\).

R's primal bounds can also be obtained directly, without its later coercivity theorem:
\[
 R(u):=\|c(u)\|_2/\sqrt n\le\beta+au,
\]
\[
 P_3(u):=10+a\beta u+\frac{a^2u^2}{2}
 \ \ge\ \|W^{(3)}(u)\|_{\rm op},
\]
\[
\begin{aligned}
 P_2(u)&:=10+a\int_0^uP_3(v)(\beta+av)\,dv\\
 &=10+10a\beta u+
 \frac{10a^2+a^2\beta^2}{2}u^2+
 \frac{a^3\beta}{2}u^3+\frac{a^4}{8}u^4\\
 &\ge\|W^{(2)}(u)\|_{\rm op}.
\end{aligned}
\]
These follow from the four exact feature velocities and
\(\|uv^T/n\|_{\rm op}\le\|u\|_2\|v\|_2/n\).
The same estimate bounds each matrix's Frobenius increment; the first-layer displacement is bounded by
\[
 \frac{\|z^{(1)}(u)-z^{(1)}(0)\|_2}{\sqrt n}
 \le\int_0^uP_2(v)P_3(v)(\beta+av)\,dv.
\]
All are finite on compact feature intervals. Smooth local solutions therefore extend globally in forward feature time, and the bound \(s(t)\le3T\) prevents finite physical-time escape on \(\Gamma_n\).

Take the deterministic, width-independent constants
\[
 M_T=\max(P_2(3T),P_3(3T)),\qquad R_T=\beta+3aT,
\quad C_T=C_{\rm phys}(M_T,R_T).
\]
On \(\Gamma_n\), for every \(0\le t_0\le t\le T\), every \(1\le m\le N\), and every isometry E,
\[
 \sum_{j=1}^m
 [\log\sigma_j(U_{\rm phys}(t,t_0)E)]^2
 \le C_T^2n(t-t_0)^2.
\]
The associated counts and top-column increment estimates hold on this same event. There is no probability union bound over subspaces, columns, times, or singular directions: their deterministic assertions already hold simultaneously on every bounded path. For any prescribed feature horizon, the same polynomials evaluated at that horizon give the feature-time corollary directly.

This construction proves the probability claim in C lines 275–285 with explicit quantifiers and constants. It uses only permitted information and elementary calculations. It does not infer any expectation bound on the complement of \(\Gamma_n\), any limiting trained-state law, or a response bound uniform as \(T\to\infty\).

**Finding:** The high-probability corollary is legitimate for the actual canonical initialization.

## 8. What the amplitude statement does and does not mean

On a fixed bounded interval, C proves an \(O(n)\) sum of squared singular logarithms. For an n-column response this is a bounded normalized second logarithmic moment. For the full \(N=2n^2+2n\) response, its average per state direction is even \(O(1/n)\). Neither statement bounds the amplitude carried by one exceptionally expanding direction uniformly in width.

Explicitly, on \(\mathbb R^n\), take
\[
 \mathsf D_n=\operatorname{diag}(\sqrt n,0,\ldots,0),\quad
 U_n(s)=\operatorname{diag}(e^{s\sqrt n},1,\ldots,1).
\]
Then
\[
 \|\mathsf D_n\|_F=\sqrt n,\qquad
 \sum_j(\log\sigma_j(U_n(s)))^2=ns^2,
\]
so the matrix inequality is attained with equality. Nevertheless,
\[
 \frac1n\operatorname{Tr}(U_n(s)^TU_n(s))
 =\frac{e^{2s\sqrt n}+n-1}{n}\longrightarrow\infty,
\]
and for the trained increment,
\[
 \frac1n\operatorname{Tr}((U_n(s)-I)^T(U_n(s)-I))
 =\frac{(e^{s\sqrt n}-1)^2}{n}\longrightarrow\infty
\]
for every fixed \(s>0\). The example can be embedded into the candidate's larger ambient dimension while retaining an n-dimensional seed. It is a counterexample to an implication from the displayed spectral estimates alone; it is not asserted to satisfy the canonical network equations.

The sentence in C lines 326–327 that the estimates “do not bound” the trace should therefore be understood as “do not give a width-uniform normalized trace bound.” Taken literally without that qualification it is too strong: C (3) does imply
\[
 \sigma_{\max}(Y_i)\le e^{C_B\sqrt n\,s},\qquad
 \operatorname{Tr}(Z_i^TZ_i)
 \le n(e^{C_B\sqrt n\,s}+1)^2.
\]
These width-dependent exponential bounds are insufficient for the proposed population stability application. The abstract example proves that a width-uniform improvement cannot follow from the logarithmic estimates alone.

The large-r count improves from \(O(n/r)\) to \(O(n/r^2)\) when compared at the level of logarithmic tail control in a fixed metric. It supplies no control of a pruning source's component along a rare expanding direction. In particular, it does not estimate an inhomogeneous response
\(\int U(t,s)f_E(s)\,ds\), justify independence of that source and its propagator, control a projected hidden Jacobian's angle loss, or supply a trace covariance estimate.

## 9. Precise certified scope and wording corrections

The certified result is the following.

For the uncut arctan network with the feature and physical training fields specified above, at each finite width, on every forward interval where the two hidden operator norms and the readout RMS obey (1), the full canonical Hessian has the exact stated \(C_B(M,R)\sqrt n\) Frobenius upper bound. Every initially isometric, full-column-rank homogeneous response obeys the squared-singular-logarithm bound and its tail count. This includes the actual independent Gaussian top-column derivative probe, its nonzero covariance spectrum, and the regularized squared-log spectrum of its trained increment. At fixed physical times the same assertions hold with exactly the displayed \(C_{\rm phys}(M,R)\), including the derivative of the feature clock. The canonical initialization satisfies the required finite-horizon primal event with probability tending to one, without a zero-readout population approximation.

All logarithms are natural; all covariance logarithms concern nonzero eigenvalues; the isometry and singular values use the specified canonical Euclidean metric. The result is valid also for zero readout and at zero singular-log energy. It needs no simple eigenvalues, smooth choice of singular vectors, normality, time commutation, maximum-coordinate readout bound, or backward-query tail assumption.

Two wording improvements would make the certification unambiguous:

1. Replace a literal claim of strengthening L's response spectrum by: “This proves a second logarithmic-moment estimate for actual responses in raw canonical coordinates. The earlier comparison uses a transformed first-layer coordinate, so its response spectrum requires a separate metric comparison.”
2. Replace “The estimates do not bound \(\operatorname{Tr}(Z_i^TZ_i)\)” by: “The estimates do not supply a width-uniform normalized trace or response-amplitude bound.”

There is no mathematical correction required to C (2)–(10). The certified scope is a finite-width homogeneous-response lemma and its stated increment corollary. It is not the full global population theorem, and it does not resolve population existence, uniqueness, width convergence, global pruning stability, canonical source alignment, or response amplitude.

## 10. Final-current-hash complete verdict — 2026-09-05

**Final verdict: PASS for the complete current candidate at SHA256 d416464bf1b5e4a792bb6937f0f7eec0e5d19cd70ca05816d02f011bf64547f0. Both earlier wording clarifications are resolved. No outstanding correction is required for the claimed finite-width response lemma.**

I reread the complete current C, lines 1–347, and rechecked its definitions, inline mathematics, displayed formulas, proof transitions, probability assertion, probe interpretation, and final scope against the independent derivations in Sections 1–8 of this review. The mathematical content of the displayed formulas agrees with that previously verified. The restored inline delimiters preserve the mathematical statements and their meanings.

The candidate's SHA256 was computed directly and matches the hash supplied by the author. The permitted dependencies retain their previously reviewed hashes:

| Input | Final verification SHA256 |
| --- | --- |
| C: complete current candidate | d416464bf1b5e4a792bb6937f0f7eec0e5d19cd70ca05816d02f011bf64547f0 |
| H: ACTUAL_HIDDEN_GRAPH_VOLUME.md | 7b70789e567d8c17d0f6ad1c7b4ab703fc9d0ed385863bf38bb8f81b80eeff7e |
| R: READOUT_COERCIVITY.md | 0bd062da74fbde03d41a125561beee7345915ea6aa0578ed8e7b81d2c9f08c53 |
| L: LOGARITHMIC_NETWORK_COMPARISON.md | adc98d1f9fe2c23560afc649e9107e2125a87aca1c94ee5db9a4f43e7034f480 |

Before this append, the existing review itself still had SHA256 1b6bd4584f0622317e000a98894f893392e17662653a81f511f093b06f863b02, matching the originally written review. Its earlier sections are retained as the historical audit. Their candidate hash and line references refer to the earlier version; this section provides the complete verdict for the current version. In particular, the two wording requests in Section 9 are now closed, not pending objections.

### Verification of the actual revisions

Current C lines 3–10 expressly place the second logarithmic moment in raw canonical coordinates and identify L's transformed first-layer coordinate without equating the response spectra. Current lines 338–341 also explicitly decline a transfer to the nonlinear coordinate. These passages resolve the metric-comparison clarification, including the comparative wording at the end of the note.

Current C lines 327–336 identify the missing conclusion as a width-uniform bound on the normalized trace \(\operatorname{Tr}(Z_i^TZ_i)/n\), and retain the distinction between the abstract amplification example and an actual canonical network trajectory. The opening paragraph now uses the same width-uniform normalized-response-trace qualification. This resolves the amplitude wording clarification without weakening or overstating the actual response estimates.

The source-level delimiter check found exactly 83 matched inline mathematical pairs and 30 matched display pairs, with no unmatched or improperly nested mathematical delimiters. The complete mathematical reread also checked the content inside those delimiters: the coordinate scales, transposes, derivatives, exponents, quantifiers, positivity requirements, clock factors, and normalization of the seed all retain their audited meanings.

### Complete mathematical status of the current candidate

| Component, with current C locations | Final assessment |
| --- | --- |
| Coordinates, initialization metric, and feature field, lines 14–54 and 276–286 | PASS. The hidden variables are \(z^{(1)},\sqrt nW^{(2)},\sqrt nW^{(3)}\); c remains the unwhitened rescaled readout. The matrix gradient blocks have \(1/\sqrt n\), and \(b=\nabla(c^Th^{(3)})\). |
| All trained Hessian terms, lines 105–168 and 185–193 | PASS. The three gate terms and both symmetric trained-matrix cross pairs are present. The full Hessian includes \(J,J^T\) and its zero readout–readout block. |
| Explicit RMS-only Frobenius estimate, lines 56–78 and 120–193 | PASS with exactly \(C_B=2R(M^2+MK_2^2+K_3^2+M+K_2)+\sqrt2K_3\). Neither a readout maximum-coordinate hypothesis nor query tails are used. |
| Rectangular logarithmic differential, repeated eigenvalues, and zero energy, lines 195–243 | PASS. \(G=V^TV\) remains positive definite, the trace differential is valid at repeated eigenvalues, and regularizing \(\sqrt{\mathcal E+\epsilon}\) avoids division by zero. The constant in (7) is unchanged. |
| Fixed physical-time derivative, lines 245–274 | PASS. \(B_{\rm phys}=2(1-f_n)B-(2/n)bb^T\) retains the clock derivative with the correct sign and scaling. The four-block \(K_b^2\) estimate and \(C_{\rm phys}\) are correct. |
| Canonical probability corollary, lines 276–286 and 343–347 | PASS. The unchanged permitted dependency R supplies the required primal bounds. Section 7 above gives an explicit independent finite-horizon event with probability tending to one for the actual tiny Gaussian readout. |
| Actual top-column response and covariance, lines 288–303 | PASS. \(E_iu=(0,0,ue_i^T,0)\) is isometric and means an original top-column perturbation \(u/\sqrt n\). The auxiliary probe is independent of the trajectory. Nonzero covariance eigenvalues are \(\sigma_j(Y_i)^2\), with the factor 4 in their squared-log sum as recorded in Section 6 above. |
| Trained-increment bound, lines 305–325 | PASS. The seed subtraction, positive-matrix inequality, ordered-eigenvalue comparison, and constants \(2(\log5)^2\) and 8 in (10) remain correct. |
| Amplitude limitation and certified scope, lines 3–10 and 327–341 | PASS. The abstract example permits normalized amplitude divergence while satisfying the logarithmic estimates. The note now explicitly claims neither metric transfer nor a width-uniform amplitude bound nor global population continuation. |

The mathematical proof continues to cover exactly zero readout: no division by its norm occurs, and the off-diagonal Hessian blocks may remain nonzero. It also covers repeated singular values, including the initially isometric spectrum, through the Gram-matrix trace argument.

### Final certified scope

For each finite \(n\ge1\), along an actual uncut arctan trajectory on a forward interval obeying (1), all initially isometric homogeneous responses in the stated canonical Euclidean metric satisfy
\[
 \sum_{j=1}^m[\log\sigma_j(U(s,s_0)E)]^2
 \le C_B(M,R)^2 n(s-s_0)^2,
 \qquad E^TE=I_m,\quad 1\le m\le2n^2+2n.
\]
The associated \(r^{-2}\) count holds for every \(r>0\). The fixed-physical-time versions hold with \(C_{\rm phys}(M,R)\) and physical elapsed time, using the full physical Jacobian. These assertions hold simultaneously for all fixed seed isometries on a bounded path, without requiring their independence from that path.

For the actual independent Gaussian top-column probe, the same certification includes the nonzero conditional covariance spectrum and the trained-increment bound (10). The canonical initialization yields these finite-horizon conclusions with probability tending to one and deterministic constants independent of width. No claim is made for logarithms of zero ambient covariance eigenvalues, for a probe identified with a trajectory-dependent initial column, or for a nonlinear change of response metric without an additional comparison.

The complete current candidate therefore passes as a finite-width response lemma. Its formulas do not establish a width-uniform normalized response-amplitude bound, canonical pruning-source alignment, or the desired full global population theorem. No numerical experiment or additional mathematical source was used in this final verification, and neither the candidate nor its dependencies was edited.

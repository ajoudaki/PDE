# Independent adversarial review of the stopped cavity trace approximation

Date: 2026-09-06.

## Verdict and scope

**SCOPED PASS.** I found no required mathematical correction to the finite-width, continuous-time, stopped approximation (9), its cavity-coefficient version (12), or the supporting estimates, under the stated width condition (7). This verdict concerns validity of the calculation as stated; it does not assert a width-uniform response bound, removal of either stop, a limiting equation, or a result for raw gradient descent.

The important dependencies are present: the concentration event concerns only independent cavity kernels; the induced upper-field coordinates are controlled before Taylor expansion; the nonlinear consistency error is small before the stability exponential is applied; and that stability argument needs a maximum bound only at the actual state. The readback retains the learned column and direct contribution with their correct normalizations.

Required findings: **none within scope**. Two optional presentation improvements appear at the end. They are not additional hypotheses or conditions for this verdict.

## Isolation and integrity record

The only mathematical file read was

`/tmp/l2-two-sample-proof-0ywjpp/CAVITY_STOPPED_TRACE_LINEARIZATION_TEST.md`.

It was read in full: 864 lines, 37,052 bytes. The successive reads covered lines 1–240, 241–480, 481–720, and 721–EOF. No named source, other mathematics file, review, history, skill file, or other agent was read or consulted. No experiments, subagents, external references, or heavy imports were used. The review was written using `apply_patch`; the source was not edited.

SHA-256 before reading:

```text
192a22168de5c560c3d8046f297e813dda1ca037065caa323a90eb9dd7a6bedb
```

SHA-256 after the full reading and mathematical audit:

```text
192a22168de5c560c3d8046f297e813dda1ca037065caa323a90eb9dd7a6bedb
```

The hashes agree. A further source hash taken after writing the full review also returned exactly `192a22168de5c560c3d8046f297e813dda1ca037065caa323a90eb9dd7a6bedb`. The source's statement about its author's earlier reading and the hash of that separate source is a provenance assertion, not a mathematical premise verified here; the isolation instruction precludes checking it. All mathematical identities needed for this review were checked directly from the supplied file.

Equation numbers below refer to the audited source.

## 1. Model, raw metric, deterministic bounds, and restoration

### Equations (1)–(3), (13), (17), and (20): normalization

For one sample, direct differentiation gives

\[
 \nabla_{W^{(1)}}f_a=\frac1n(p_a\odot q_a)x_a^T,
 \qquad \nabla_A f_a=\frac1n\delta_a(h_a^{(1)})^T,
 \qquad \nabla_w f_a=\frac1n h_a^{(2)},
\]

where in this review \(p_a=\phi_1'(z_a^{(1)})\). Multiplication by the inverse metric weights \(n/d,1,n\), respectively, and use of \(c_a=-2(f_a-y_a)\), gives exactly (2). Thus (13) has neither a missing factor of two nor a missing power of \(n\).

Multiplying the first equation of (2) by \(x_b\) gives

\[
 \dot z^{(1)}_{b,i}=\sum_a C_{ba}c_a p_{a,i}q_{a,i},
\]

which is (17). There is no surviving factor of \(d\).

Every moving first-row displacement lies in the span of the two inputs. On that span, whose input Gram matrix is \(dC\),

\[
 d\|\Delta W_i^{(1)}\|^2=\Delta z_i^TC^{-1}\Delta z_i.
\]

The input-orthogonal component is constant and irrelevant to the restricted flow. Because \(\rho\in(-1,1)\), \(C\) is positive definite. This verifies the first block of (20). Its dimension is

\[
 2(n-1)+n(n-1)+n=n^2+2n-2.
\]

All dependence on the input geometry is through \(C\); no hidden dependence on \(d\) enters these estimates. Dependence on the fixed \(\rho\) is allowed.

### Equations (13)–(16): global bounds and the learned column

Bounded activation and \(\|w(0)\|_\infty\leq1\) imply bounded initial predictions and loss. Loss decrease bounds both residual coefficients for all subsequent times. Integration of \(\dot w\), using bounded \(\phi_2\), bounds \(\|w(t)\|_\infty\) on a fixed time interval. Consequently \(\|\delta_a\|\leq C_T\sqrt n\). The outer-product update then gives

\[
 \|\dot A\|_F\leq\frac1n\sum_a|c_a|\|\delta_a\|\|h_a^{(1)}\|
 \leq C_T,
\]

and hence bounded matrix spectral norm and \(\|q_a\|\leq C_T\sqrt n\). The three blocks of raw speed are bounded by these same products. These arguments also apply to the cavity, with \(n-1\) lower units and the unchanged denominator \(n\).

Smooth finite-dimensional local flow plus finite raw displacement on every bounded time interval rules out finite-time escape. This justifies defining the actual distinguished path on all of \([0,T]\), even when the estimates will be used only before the stops. No bound on the initial first-layer norm is required.

On the stated event, \(\|A(0)\|_{\rm op}\leq\|B(0)\|_{\rm op}+\|g\|\leq10\). The actual deterministic bounds therefore require only \(\mathcal C_n\) and \(\|g\|\leq2\), not an actual-trajectory stopping event.

Integrating the actual column update gives (15) exactly, including the actual residuals and actual distinguished features. Its norm is \(O(n^{-1/2})\), since each integrand has Euclidean norm \(O(\sqrt n)\) and the prefactor is \(1/n\). This proves both the learned-column estimate and (16). There is no deletion of any trained-column history.

### Equations (18)–(19): exact scalar splitting

The fundamental theorem of calculus applied coordinatewise to \(\phi_2'\) gives

\[
 \delta_a=\delta_a^0+D_a^{\rm dir}(g+\ell)h_a,
 \qquad h_a=h^{(1)}_{a,j}.
\]

Since \(q_{a,j}=(g+\ell)^T\delta_a\), splitting off \(\ell^T\delta_a\) first yields

\[
 q_{a,j}=g^T\widehat\delta_a+
          \ell^T\delta_a+
          h_a g^TD_a^{\rm dir}(g+\ell)+
          g^T(\delta_a^0-\widehat\delta_a).
\]

This is (19). In particular, there is no missing additional \(\ell^TD_a^{\rm dir}\ell\) term: all terms with the learned column on the left are already contained in \(M_a=\ell^T\delta_a\). The bound on \(D_a^{\rm dir}\) follows from bounded \(w\) and \(\phi_2''\), giving the claimed constant bounds on both \(M_a\) and \(S_a\).

## 2. Conditioning, freezing, and the actual distinguished path

The deleted initial column \(g\) is independent of all remaining initialization, including \(\xi\). The cavity deletes that column permanently; the frozen first-layer row contributes no upper input. Its trajectory, initialization event \(\mathcal C_n\), stopping time \(\tau_c\), and frozen extension are consequently measurable with respect to \(\mathcal F_{-j}\).

On \(\mathcal C_n\), continuity ensures that the cavity reverse-field maximum is at most \(R_n\) up to the hitting time, at the hitting time, and after freezing. Initial equality merely makes the cavity stop zero. The operator estimates at the frozen state are therefore valid on the whole deterministic interval.

The response generator after \(\tau_c\) is explicitly the unfrozen vector-field derivative evaluated at the frozen state. This is a valid definition of an independent extension. It is not asserted to be the derivative of the stopped evolution. The approximation equation is used only for \(t<\tau\), where the cavity follows its original equation. Endpoint statements follow by continuity.

The actual stop never enters a kernel used for Gaussian concentration. All concentration is established on deterministic time domains after conditioning only on \(\mathcal F_{-j}\), then restricted pathwise to \(t\leq\tau\). Thus stopping does not incorrectly preserve a Gaussian law by conditioning on a Gaussian-dependent event.

Likewise, \(G_a(t)=g^T\widehat\delta_a(t)\) has the conditional centered Gaussian finite-dimensional laws and covariance (11). This is its law given \(\mathcal F_{-j}\), not its law after further conditioning on the good event or on stop survival.

The actual distinguished path is retained in every occurrence of \(h_a\). It is generally dependent on \(g\). The proof uses its deterministic bound \(|h_a|\leq B_1\); it does not replace it with a conditionally independent path. If the actual initial maximum already exceeds the threshold, the interval reduces to time zero. The exact initial split and the direct concentration estimate still apply there.

## 3. Full derivative audit in raw coordinates

### Equations (20)–(24): directions and prediction derivative

The scaling convention is essential: \(Y=\sqrt n\,\Delta X\). Accordingly the physical increments are

\[
 \Delta z_i=C^{1/2}u_i=\zeta_i,
 \qquad \Delta B=V/\sqrt n,
 \qquad \Delta w=v.
\]

The physical upper input associated with \(E=e/\sqrt n\) is exactly \(e\). Therefore the derivatives of the upper preactivation, reverse field, and bulk reverse field are

\[
 \lambda_a=VH_a/\sqrt n+\widehat B P_a\zeta_a+e_a,
\]

\[
 d\delta_a=V_a v+D_a\lambda_a,
 \qquad dq_a=V^T\widehat\delta_a/\sqrt n+
                       \widehat B^Td\delta_a.
\]

These agree with (23)–(24). In particular \(L_a=n^{-1/2}D_X\delta_a\), rather than \(D_X\delta_a\). The distinction accounts for the absence of an extra \(\sqrt n\) in the eventual readback.

Differentiating the prediction gives

\[
 df_a=\frac1n\left[v^T\phi_2(\widehat z_a^{(2)})+
                              \widehat\delta_a^T\lambda_a\right],
 \qquad dc_a=-2df_a=\chi_a.
\]

Thus the residual derivative contains both the readout increment and the upper-input increment, including the input due to the restored column.

### Equations (25)–(26): all vector-field terms

For reference, the three blocks of \(\sqrt n F\), expressed in physical variables, are

\[
 C^{1/2}(c_a p_{a,i}q_{a,i})_a,
 \qquad \frac1{\sqrt n}\sum_a c_a\delta_a(h_a^{(1)})^T,
 \qquad \sum_a c_a h_a^{(2)}.
\]

Their directional derivatives are exactly the three lines of (25):

| Block | Differentiated factors that must appear | Check |
| --- | --- | --- |
| First roots | gate curvature, reverse field, residual | \(\widehat c\phi_1''\widehat q\zeta\), \(\widehat c p\,dq\), and \(\chi p\widehat q\) all appear |
| Bulk matrix | residual, upper reverse factor, lower feature factor | \(\chi\widehat\delta H^T\), \(\widehat c\,d\delta H^T\), and \(\widehat c\widehat\delta(P\zeta)^T\), all divided by \(\sqrt n\) |
| Readout | residual and upper activation | \(\chi\widehat h^{(2)}+\widehat cV_a\lambda_a\) |

The term \(V^T\widehat\delta/\sqrt n\) also differentiates the trained transpose factor in \(q\); it is not omitted. All coefficients are the trained cavity coefficients. No initial random matrix is substituted for a trained coefficient.

Equivalently, differentiating \(\sqrt n F(\widehat X+\theta Y/\sqrt n,\theta e/\sqrt n)\) at zero gives \(D_XF\,Y+D_EF\,e\). This verifies the two identities in (26) with their stated normalization.

The equation for the actual bulk indeed holds with \(E\) fixed when taking the gradient: the distinguished first-layer row and the restored column are separate actual parameter blocks. Treating their current contribution as an external input reproduces the bulk updates without an extraneous chain rule through their trajectories.

### Equations (27)–(29): operator bounds and time regularity

The feature and reverse-field norms are \(O(\sqrt n)\), cancelling each \(1/\sqrt n\) in the derivative maps. Bounded gates, matrix norm, and readout maximum give bounded \(Z,L,Q\). Also

\[
 |\chi_a|\leq C_T(\|Y\|+\|e\|)/\sqrt n.
\]

Its multiplication by a reverse-field or feature vector of norm \(O(\sqrt n)\) is therefore harmless. Outer-product Frobenius norms give bounded matrix-block derivatives as well. The only derivative term needing a reverse-field maximum is \(\phi_1''\widehat q\zeta\). This proves the \(1+R_n\) Jacobian bound and a width-independent bound on the input derivative \(\mathcal B\).

Integration of the linear differential inequality gives (28). Existence by the convergent iterated-integral series is valid in the finite-dimensional space. The identity \(\partial_sU_c=-U_cJ_c(s)\) follows from uniqueness and the propagator composition law.

The derivative bounds in (29) follow from the exact equations and the RMS reverse-field bound. In particular, \(\dot z^{(2)}=\dot B H+BP\dot z^{(1)}\) is \(O(\sqrt n)\) in Euclidean norm. Differentiation of \(\delta\) and \(q\) preserves that scale. The residual derivative is bounded either directly from \(df\) or from the raw speed and prediction gradient.

The claimed polynomial time moduli are deliberately loose but valid. Differentiating \(D\) requires only \(\phi_2'''\), and differentiating a first-layer gate requires the stated bounded derivatives. No fourth derivative is needed. Freezing yields Lipschitz paths across the stop; differentiability there is unnecessary. These facts justify the uniform kernel moduli used for the grid extension.

## 4. Gaussian and quadratic concentration, uniformly in time

### Equations (30)–(32): scalar tails and constants

For deterministic \(v\), the conditional scalar \(v^Tg\) has variance \(\|v\|^2/n\), giving (30) directly from its Gaussian moment-generating function.

For the quadratic form, only the symmetric part \(S\) contributes, and its trace agrees with that of \(K\). Orthogonal diagonalization reduces the centered form to \(n^{-1}\sum_i\lambda_i(Z_i^2-1)\). Expanding the logarithm of its moment-generating function gives precisely (32):

\[
 \log\mathbb E e^{t(g^TKg-\operatorname{Tr}K/n)}
 \leq\frac{t^2v^2/n^2}{1-2|t|b/n},
 \quad v=\|S\|_F,\quad b=\|S\|_{\rm op}.
\]

For \(v>0\), the chosen positive value \(t=n\sqrt x/(v+2b\sqrt x)\) is within the required domain. At the proposed threshold,

\[
 t\left(\frac{2v\sqrt x}{n}+\frac{2bx}{n}\right)
 -\frac{t^2v^2/n^2}{1-2tb/n}=x.
\]

Applying the same argument to \(-S\) gives the other tail. If \(v=0\), the form is identically zero. Thus (31), including its constants and applicability to nonsymmetric response matrices, is correct.

### Equations (33)–(36): simultaneous event and interpolation

There are \(O(n^2)\) row families: the identity in the bulk space contributes \(m_n=O(n^2)\) rows, and the remaining maps contribute only \(O(n)\) each. There are four response quadratic families and two diagonal quadratic families. This count does not conceal a dependence on \(d\).

The operator bounds imply row norm at most \(H_n\), and the symmetric parts of the quadratic matrices have Frobenius norm at most \(\sqrt nH_n\). A grid with \(O_T(n^8)\) cells produces \(O_T(n^{16})\) pairs and \(O_T(n^{18})\) scalar tests. With \(x=(p_*+25)\log n\), the union-bound cost is at most \(C_Tn^{-p_*-7}\), hence at most \(n^{-p_*}\) after the stated constant lower-width restriction. Independence across coordinates or times is not needed.

The linear threshold is \(C_{p_*}H_na_n\). The quadratic threshold is bounded by \(C_{p_*}H_n(a_n+a_n^2)\). Both fit inside \(H_n^2a_n\), with slack for sums of the finitely many coordinate bounds and with a sufficiently large fixed \(A_*\).

The norm-tail calculation is also correct:

\[
 \Pr(\|g\|>2)\leq e^{-n}2^{n/2}
 =e^{-(1-\log2/2)n}\leq e^{-n/2}.
\]

It is added to, not conditioned into, the scalar concentration probabilities. On its complement, the interpolation errors are bounded by the deterministic operator modulus times \(\|g\|\), or by that modulus times \(\|g\|^2+1\) for a centered quadratic form. The latter extra term correctly accounts for the changing trace.

The mesh spacing is at most \(n^{-8}\), so the interpolation cost is \(C_Tn^{-6}H_n^4\). The width condition implies \(H_n\leq n^{1/40}\), since \(H_n^{20}a_n\leq1/2\) and \(\log n>1\). Consequently the cost is at most \(C_Tn^{-59/10}\), far smaller than \(H_n^2a_n\) for sufficiently large \(n\). Rounding the lower time down and upper time up respects the propagator's triangular domain.

This establishes a single conditional event of probability at least \(1-n^{-p_*}-e^{-n/2}\) supporting the continuous-time suprema. There is no later sampling-mesh dependence.

### Equations (37)–(39): dependence on the actual path

Although \(Y^{\rm lin}\) is generally not Gaussian conditional on the cavity, every row-kernel bound is available before multiplying by \(h_b(s)\). For each required coordinate,

\[
 \left|\sum_b\int_0^t (\text{row kernel}\cdot g)h_b(s)\,ds\right|
 \leq 2TB_1\sup_{s\leq t,b}|\text{row kernel}\cdot g|.
\]

This is a deterministic inequality for every bounded measurable choice of \(h\), including a choice depending on \(g\). It verifies the use of concentration despite the dependence of the distinguished path.

The global norm bound uses the operator norm of the propagator and \(\|g\|\leq2\), not a sum of coordinate estimates. This distinction is necessary: summing \(O(n^2)\) coordinate estimates would not give the claimed bound. The source makes the valid operator-norm argument instead.

The row families supply all required coordinates: identity rows control roots and readout, \(Z\)-rows control the induced upper input, and \(Q\)-rows together with \(\widehat B^TD_ag\) control the linear bulk reverse field. The fixed two-dimensional transformation \(C^{1/2}\) preserves these coordinate scales. The \(L\)-rows are included as well; alternatively, linear \(\delta\) delocalization follows from \(d\delta=V_av+D_a\lambda_a\).

## 5. Coordinate-delocalized quadratic defect

The local lemma (40) is the main nonlinear issue. Its assumptions are sufficient as written. In the following checks set \(r=N(\alpha+N/\sqrt n)\), as in the source. There is no use of a maximum bound for an intermediate reverse field.

### Equations (41)–(43): activation and reverse-field expansions

The physical increments satisfy \(\|\zeta\|,\|v\|,\|\lambda\|\leq CN\). Bounded second and third activation derivatives give pointwise quadratic remainders for both \(\phi_1\) and \(\phi_1'\). The estimate

\[
 \|\zeta^2\|_2\leq\|\zeta\|_\infty\|\zeta\|_2
\]

therefore gives the two \(C\alpha N\) bounds in (41).

Multiplying out the upper preactivation at the perturbed bulk state gives the exact remainder

\[
 \beta_a=\widehat B r_{1a}+(V/\sqrt n)\Delta h_a^{(1)}.
\]

The two contributions are \(O(\alpha N)\) and \(O(N^2/\sqrt n)\), respectively. The second estimate needs a Frobenius bound on the matrix increment, not coordinate delocalization of all its entries.

It would be invalid to infer a small pointwise quadratic remainder solely from \(\|\Delta z^{(2)}\|_2=O(N)\). The source avoids this: expand in the coordinate-small \(\lambda\) and control the remaining displacement \(\beta\) by a Lipschitz estimate. This yields

\[
 \|r_2\|\leq C\|\lambda\|_\infty\|\lambda\|+C\|\beta\|
 \leq Cr.
\]

For \(\delta\), the analogous Taylor expansion uses \(\phi_2'''\). Its additional trained-readout product satisfies

\[
 \|v\odot[\phi_2'(\widehat z^{(2)}+\Delta z^{(2)})
                         -\phi_2'(\widehat z^{(2)})]\|
 \leq C\|v\|_\infty\|\Delta z^{(2)}\|\leq C\alpha N.
\]

Thus both parts of (43) follow. The stated activation families have all the required bounded derivatives; the proof does not rely on a nonexistent third-derivative assumption.

### Equations (44)–(45): transpose and residual remainders

Multiplication of the trained transpose factor yields exactly

\[
 r_q=\widehat B^Tr_\delta+(V/\sqrt n)^T\Delta\delta.
\]

The second term costs \(CN^2/\sqrt n\). Bounded perturbed readout and matrix norms follow from \(\alpha\leq1\) and \(N/\sqrt n\leq1\). They also give \(\|\Delta\delta\|,\|\Delta q\|\leq CN\).

For the prediction, the omitted linear terms are exactly

\[
 r_c=-\frac2n[\widehat w^Tr_2+v^T\Delta h^{(2)}].
\]

The first contribution is \(Cr/\sqrt n\), and the second \(CN^2/n\), which fits in the same bound because \(r\geq N^2/\sqrt n\). The estimate \(|\Delta c|\leq CN/\sqrt n\) follows directly from the prediction product, using \(N\leq\sqrt n\). No unnormalized residual derivative is hidden here.

### Complete product remainder audit for (40)

The first-root product remainder, suppressing sample indices, is precisely

\[
 \widehat c[\widehat p\,r_q+r_p\widehat q+\Delta p\,\Delta q]
 +r_c\widehat p\widehat q
 +\Delta c[\Delta p\widehat q+p'\Delta q].
\]

The bounds are, in that order,

\[
 Cr,\quad CR_n\alpha N,\quad C\alpha N,
 \quad Cr,\quad C\alpha N,\quad CN^2/\sqrt n.
\]

For the fifth term, \(|\Delta c|\leq CN/\sqrt n\) multiplies \(\|\Delta p\widehat q\|\leq C\alpha\sqrt n\). Only the second term uses the cavity maximum. This checks the curvature factor \(1+R_n\) in (40).

The matrix remainders with frozen residual coefficient are exactly

\[
 \frac{\widehat c}{\sqrt n}
       [r_\delta H^T+\widehat\delta r_1^T+
                           \Delta\delta(\Delta h^{(1)})^T],
\]

with Frobenius bounds \(Cr,C\alpha N,CN^2/\sqrt n\). The residual-dependent remainder is

\[
 \frac1{\sqrt n}[r_c\widehat\delta H^T+
    \Delta c(\Delta\delta H^T+\delta'(\Delta h^{(1)})^T)].
\]

Here \(\|\delta'\|\leq C\sqrt n\); the bounds are \(Cr\) and \(CN^2/\sqrt n\). This expansion accounts for both trained factors and their product, including the product involving the changed residual.

The readout remainders are exactly \(\widehat c r_2+r_c\widehat h^{(2)}+\Delta c\Delta h^{(2)}\), with the same bounds. The fixed sample count and \(C^{1/2}\) factor do not change the scale. Therefore (40) follows with \(C_T(1+R_n)r\).

Adversarial conclusion for this lemma: the potentially dangerous upper quadratic term is controlled by the independent \(Z\)-row concentration; neither a first-root-only estimate nor an uncontrolled global Hessian Lipschitz estimate is being used.

## 6. Actual-only-maximum stability and closure

### Equations (46)–(47): approximate trajectory and learned forcing

Differentiating the variation-of-constants formula (37) gives

\[
 \dot Y^{\rm lin}=J_cY^{\rm lin}+\sum_b\mathcal B_bg h_b.
\]

On \(t<\tau\), the derivative of the cavity path is its true vector field. Consequently its contribution cancels from the definition of the approximate trajectory, and (40) supplies exactly the defect in (46). No derivative of \(h\) is needed. For the actual path \(h\) is continuous; bounded measurable inputs would suffice for an almost-everywhere version and the integrated estimates.

The estimates \(N\leq H_n\), \(\alpha\leq H_n^3a_n\), and \(N/\sqrt n\leq1\) follow from (38)–(39) and (7). They also bound the approximate matrix spectral norm and approximate readout maximum. Thus the local lemma applies without an additional approximation stop.

The actual physical input differs from \(e^0\) by \(\ell h\), whose norm is \(O(n^{-1/2})\). In \(E\)-coordinates this is \(O(n^{-1})\). At bounded matrix norm and readout maximum, the \(e\)-terms of (24)–(25) give a bounded \(D_EF\) at every upper input: residual coefficients remain bounded because the output activation is bounded, and the reverse field is needed only in RMS norm. Multiplication by \(\sqrt n\) therefore gives precisely the \(O(n^{-1/2})\) error in (47). A maximum bound along this input segment is unnecessary.

### Equations (48)–(50): comparison with only the actual maximum

For two bulk states at the same physical upper input, with \(W=\sqrt n(X-X')\), bounded endpoint matrix norms and readout maxima suffice to obtain

\[
 \|\Delta z^{(2)}\|+\|\Delta\delta\|+\|\Delta q_I\|
 \leq C_T\|W\|,\qquad |\Delta c|\leq C_T\|W\|/\sqrt n.
\]

For example, \(\Delta B\) has Frobenius norm at most \(\|W\|/\sqrt n\), cancelling the \(\sqrt n\) feature or reverse-field norms in the product differences. The readout contribution to \(\Delta\delta\) has size \(O(\|\Delta w\|)\); the other contribution uses the bounded readout of the other endpoint. These estimates require neither small \(W\) nor an intermediate-state bound.

The placement of the actual reverse field in (49) is decisive:

\[
 cpq-c'p'q'=(c-c')pq+c'(p-p')q+c'p'(q-q').
\]

The first term uses \(|\Delta c|=O(\|W\|/\sqrt n)\) and \(\|q\|=O(\sqrt n)\). The second uses the actual \(\|q_I\|_\infty\leq R_n\) and \(\|p-p'\|=O(\|W\|)\). The last uses (48). Matrix and readout product differences are \(O(\|W\|)\) in their rescaled update norms. Hence (50) follows exactly as claimed.

In this application the two vector fields have the same actual input; the input replacement for the approximate solution was already paid for separately in (47). This avoids confusing an input difference with a state difference. Neither the approximate reverse-field maximum nor a secant maximum is used in the stability constant.

### Equations (51)–(53): propagation and delocalization

The actual and approximate bulk states agree initially. Integrating the differential norm inequality with (46)–(47) gives (51). Its exponential is \(e^{C_T(1+R_n)T}\), with \(C_T\) independent of width. It multiplies the small defect, so no width-uniform stability constant is required.

For the approximate upper field, the linear coordinate is bounded by (39), while \(\|\beta\|_\infty\leq\|\beta\|_2\) is controlled by (42). The approximate \(\delta\) linear term is \(V_av+D_a\lambda_a\), so its maximum is controlled as well. The linear bulk reverse field uses exactly the last quantity in (39), followed by (44) for its remainder.

Passing from the approximate state with input \(e^0\) to the actual state with input \(e\) costs \(C_TH_n^9a_n+C_T/\sqrt n\) in each relevant Euclidean field norm, by (48) and the learned-input estimate. Euclidean bounds also control maxima. This proves the closure in (52), including the upper fields, without assuming the conclusion in advance.

The total scaled bulk displacement is at most \(H_n+H_n^9a_n\leq2H_n\). The associated RMS field and residual estimates give (53). The distinguished first root is correctly omitted from (52); it is not a small perturbation of a trained cavity row.

## 7. Readback, trace, direct and learned terms, and initial data

### Equation (54) and the trace term in (9)

The quantity requiring approximation after the exact split is \(g^T(\delta_a^0-\widehat\delta_a)\), evaluated at zero restored input for its bulk field. At the approximate state, the zero-input linear upper field \(Z_aY^{\rm lin}\) is controlled by the \(Z\)-row family itself (or by subtracting the controlled \(e_a^0\)). Thus the same Taylor lemma applies there. The actual-minus-approximate field error at zero input is controlled by (48) and (51).

Multiplying these errors by \(\|g\|\leq2\) proves (54). This step uses deterministic norm bounds; it makes no unjustified Gaussian assertion about the nonlinear Taylor remainder.

The leading scalar is exactly

\[
 \sum_b\int_0^t h_b(s)\,
       g^TL_a(t)U_c(t,s)\mathcal B_b(s)g\,ds.
\]

The Gaussian vector has dimension \(n\) and covariance \(I_n/n\). The trace factor must therefore be \(1/n\), as in (10), rather than \(1/m_n\) or an additional raw-coordinate scale. Uniform quadratic concentration permits replacing each quadratic form by this trace even for the actual dependent \(h\). The total error is at most \(2B_1T H_n^2a_n\). This verifies (9).

### Equation (55): learned readback

The exact learned term is

\[
 M_a(t)=\frac1n\sum_b\int_0^t
 c_b(s)\delta_b(s)^T\delta_a(t)h_b(s)\,ds.
\]

Changing the residual costs \(O(H_n/\sqrt n)\), since the normalized inner product is bounded. Changing either field also costs \(O(H_n/\sqrt n)\): its difference has norm \(O(H_n)\), the other field has norm \(O(\sqrt n)\), and the prefactor is \(1/n\). The exact two-term inner-product identity in the source handles both changes without omitting a cross term. Integration preserves the scale. Thus (55) contains the residual replacement and the complete learned-column replacement.

### Equations (56)–(57): direct secant and diagonal trace

The secant's argument differs from the cavity upper input by

\[
 z_a^{(2)}-\widehat z_a^{(2)}-(1-\theta)e_a.
\]

Both terms on the right are controlled in maximum norm: the first by (52), the second by \(\|g\|_\infty\) and \(\|\ell\|\). Bounded \(\phi_2'''\) controls the change in \(\phi_2''\), while (52) controls the changed readout. This proves the operator-norm estimate in (56).

The direct replacement has the exact error decomposition

\[
 S_a-d_ah_a=h_a\left[
   g^T(D_a^{\rm dir}-D_a)g+
   \left(g^TD_ag-\operatorname{Tr}D_a/n\right)+
   g^TD_a^{\rm dir}\ell\right].
\]

The three errors are respectively \(O(H_n^{12}a_n)\), at most \(H_n^2a_n\), and \(O(n^{-1/2})\). This establishes (57). No Gaussian concentration is applied directly to the dependent secant \(D_a^{\rm dir}\).

The cavity coefficients are uniformly bounded: \(|d_a|\leq\|D_a\|_{\rm op}\leq C_T\), and \(|m_{ab}|\leq|\widehat c_b|\|\widehat\delta_b\|\|\widehat\delta_a\|/n\leq C_T\). These bounds do not extend to \(\kappa\), and the theorem does not claim that they do.

### Equations (58)–(59): initial root and field mismatch

At time zero the bulk coordinates agree, so \(Y^{\rm lin}(0)=0\). Nevertheless the upper field differs by \(g\phi_1(\xi_a)\), yielding exactly the displayed initial differences of \(\delta\) and \(c\). The residual's linear response to this input appears in \(\chi_a\), including at the initial time.

Since \(\ell(0)=0\), the exact initial reverse field is

\[
 q_{a,j}(0)=G_a(0)+\phi_1(\xi_a)g^TD_a^{\rm dir}(0)g.
\]

Thus the initial direct term is present. There is no spurious claim that the full initial reverse field is a centered Gaussian, or that equality of bulk parameters means equality of all fields. Equations (9) and (12) remain meaningful when the stopped interval is just this time.

## 8. Error exponents and quantifiers

Write \(H=H_n\) and \(a=a_n\) in this section. The condition \(H^{20}a\leq1/2\), with \(H\geq1\), supplies all smallness requirements with substantial slack. A single sufficiently large \(A_*\) can dominate the finitely many fixed constants, the factor \(C_T(1+R_n)\), and the propagator and stability exponentials. This is uniform in \(K\): the dependence on \(K\) enters through \(R_n\), while \(1+R_n\) and its fixed powers are dominated by exponentials in \(1+R_n\).

The following bookkeeping checks the source's exponent allocations:

| Quantity | Bound before extra constant absorption | Source allowance |
| --- | --- | --- |
| Row/quadratic concentration | \(C_{p_*}Ha\) plus negligible interpolation | \(H^2a\) |
| Linear response coordinates | \(C_TH^2a\) | \(H^3a\) |
| Taylor remainder scale \(r\) | \(H(H^3a+H/\sqrt n)\leq2H^4a\) | used in (40) |
| Rescaled vector-field defect | \(C_T(1+R_n)H^4a\) | \(H^6a\) |
| Learned-input defect | \(C_T/\sqrt n\) | kept separately |
| Stability error | \(Te^{C_T(1+R_n)T}(H^6a+C_T/\sqrt n)\) | \(H^9a\) |
| Actual coordinate differences | \(C_T(H^9a+H^4a+n^{-1/2})\) | \(H^{12}a\) |
| Zero-input scalar readback error | \(C_T(H^9a+H^4a)\) | \(O(H^{12}a)\) |
| Learned readback replacement | \(C_TH/\sqrt n\) | (55) |
| Direct readback replacement | \(C_TH^{12}a+C_TH^2a+C_T/\sqrt n\) | \(H^{15}a\) |
| Final sum of errors | finite sum of the preceding readback errors | \(H^{20}a\) |

For example, choose \(H\) large enough that \(C_T(1+R_n)\leq H\) and the stability exponential is at most \(H\). Then the defect is at most \(2H^5a\leq H^6a\). Its integrated stability error is at most a fixed multiple of \(H^7a\), fitting in \(H^9a\). These choices are compatible with the independent direct estimate \(1+\|Y^{\rm lin}\|+\|e^0\|\leq H\), because that estimate has its own fixed exponential coefficient which can also be dominated by the chosen \(A_*\).

Also \(1/\sqrt n\leq a\) for \(n\geq3\). Thus every displayed negative power of \(n\) fits the stated allowance. The restrictions \(\alpha\leq1\), \(N/\sqrt n\leq1\), and \(H^9a\leq H\) follow from the same width condition; they are not independent bootstrap assumptions.

The finitely many constant lower-width restrictions from probability accounting and constant absorption can be enforced by increasing \(A_*\). On any fixed finite set of excluded widths, \(H^{20}a\) can be made larger than \(1/2\), so those widths fail the displayed regime. This does not make the eventual regime empty. For fixed \(T,K,p_*\),

\[
 \log\epsilon_n=-\tfrac12\log n+20A_*K\sqrt{\log n}
              +\tfrac12\log\log n+20A_*.
\]

Dividing by \(\log n\) proves \(\epsilon_n=n^{-1/2+o(1)}\to0\). The theorem is asymptotic for each fixed \(K\); it is not claimed uniformly for a width-dependent \(K\).

## 9. Initialization probability and excluded obligations

The net construction in (60) is valid. Maximal \(1/4\)-separation gives a \(1/4\)-net with at most \(9^k\) points by the stated disjoint-ball volume comparison. Approximating the two unit vectors in a matrix bilinear form loses at most \(\tfrac12\|B\|_{\rm op}\), hence the factor two in recovering the operator norm.

Each fixed bilinear form of \(B(0)\) has variance \(1/n\). The threshold four has two-sided probability at most \(2e^{-8n}\). Multiplication by \(9^n9^{n-1}\leq9^{2n}\) gives (60), with the correct positive exponent \(8-2\log9\).

For \(w_l(0)\) the standard deviation is \(1/n\), not \(1/\sqrt n\). The union bound at the threshold in (61) is \(2n\,n^{-(q_*+2)}=2n^{-(q_*+1)}\), as stated. Combining the two events gives simultaneously for both samples

\[
 \|\widehat q_a(0)\|_\infty\leq\|B(0)\|_{\rm op}
 \|\phi_2'\|_\infty\sqrt n\|w(0)\|_\infty
 \leq8\|\phi_2'\|_\infty
                   \sqrt{2(q_*+2)\log n/n}.
\]

Comparison with \(K\sqrt{\log n}\) gives the exact lower-width threshold displayed in the source. Once the readout threshold is also below one, this proves

\[
 \Pr(\mathcal C_n^c)\leq
 2e^{-(8-2\log9)n}+2n^{-(q_*+1)}.
\]

This is only an initialization assertion. It is not used to infer a positive-time stopping probability.

The response trace bound obtainable from (28) is

\[
 |\kappa_{ab}(t,s)|\leq\|L_a(t)\|\|U_c(t,s)\|\|\mathcal B_b(s)\|
 \leq C_Te^{C_T(1+R_n)T}.
\]

For fixed \(K\) it is subpolynomial in width but need not be bounded. The following are explicitly outside this verdict, as requested:

- Removing the actual or cavity maximum-field stop.
- A width-uniform response trace bound, including a uniform bound on its action on the actual path.
- Any discrete raw-gradient-descent propagator, simultaneous-update analysis, or raw interpolation.
- A mean-field limit or limiting law for the entire decomposition.

Their absence is not a required finding for this stopped gradient-flow statement.

## 10. Required versus optional findings

**Required findings: none.** I did not find a missing derivative term, a wrong raw-coordinate or trace normalization, an invalid conditioning step, an uncontrolled quadratic coordinate, a hidden secant-maximum requirement, or an error exponent exceeding the stated allowance.

**Optional presentation improvement 1: make the scaled direction explicit at its first use.** Immediately before (23), stating \(Y=\sqrt n\,\Delta X\) would make the physical-increment convention faster to verify. The convention is already correctly specified through the listed increments, the identity for \(L_a\), and the subsequent Taylor point. This is an exposition suggestion, not a normalization defect.

**Optional presentation improvement 2: collect the constant-absorption inequalities.** A short table of the principal bounds on \(H_n\), such as the one above, would make the common choice of \(A_*\) and the exponents 6, 9, 12, 15, and 20 easier to audit. The existing estimates already justify that choice; no numerical value for \(A_*\) is required by the existential theorem.

The scoped result is therefore supported: conditional on a cavity initialization in \(\mathcal C_n\), one event of the stated probability yields both decompositions uniformly up to \(\tau_c\wedge\tau_f\), with error at most \(\epsilon_n\).

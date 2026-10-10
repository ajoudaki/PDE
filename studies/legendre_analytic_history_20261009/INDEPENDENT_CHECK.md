# Independent check of fixed temporal response subspaces

Date: 2026-10-09.

## Verdict and scope

**PASS for the new construction and its stated conclusions, conditional on the explicitly imported paper interfaces.** I found no mathematical obstruction in the global polynomial approximation, initialization-only construction, projected-gradient fitting argument, normal-displacement energy identity, all-time comparison, constants, whole-sphere prediction transfer, or moving-state count.

This is a check of the frozen candidate `RESULT.md`, not an independent certification of every probabilistic argument in the paper. In particular, the deep analytic-source/carrier proposition and the positive-time dense-variability proposition are imported results. The new construction does not improve the order of the paper's unchanged residual-clock Legendre ODE, and it does not prove efficient preprocessing or subquadratic total storage. These limitations are accurately stated in the candidate.

The independent assignment, the required rigorous-math skill, and the canonical-notation skill and neural-response-memory reference were read. Scientific access was restricted to the candidate and the five permitted paper files. No other study notes, histories, author verdicts, sibling reports, or `CLOCK_ANALYSIS.md` were consulted. No scientific source was changed.

## Source identities

The hashes below identify the reviewed inputs. The candidate was frozen throughout this check.

| Input | SHA256 |
|---|---|
| `studies/legendre_analytic_history_20261009/RESULT.md` | `f1788c78eb27d271d9cb3b5023696578923028144912a3dc1daeb185963e7e27` |
| `paper/compact.tex` | `47199d5c9e374b80b9eafefd60699c2f4bfe06dde00ebd0a1c53e2805598a0c4` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `paper/compact_foundations.tex` | `6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0` |
| `paper/compact_legendre.tex` | `862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9` |
| `paper/compact_selected.tex` | `3add2b694f38a4d7dbce90e51dafd375a7e8dee2e06d26b2d5af451bddb44885` |

## Imported interfaces and directly checked dependencies

The setup is the network, mobility, initialization, activation, label, and probability convention in `compact.tex`. In particular, all data and problem parameters are fixed separately as width tends to infinity, and \(Y>0\). Write

\[
\lambda=\gamma/m\in(0,1],\qquad z=Y/\lambda,\qquad
X=\beta^L\ge100,\qquad z\le X^{-30}.
\]

The parameter norm is

\[
\|\theta\|_{\mathrm{par}}^2
=\|W^{(1)}\|_F^2/n+\sum_{\ell=2}^L\|W^{(\ell)}\|_F^2
+\|w\|_2^2/n.
\]

In the corresponding Euclidean coordinates, the dense field \(V\) is minus the gradient of \(m^{-1}\sum_a(f(x_a)-y_a)^2\).

The following distinctions matter for the verdict:

1. **Imported probability event and dense fitting:** Lemma `cp:fit`. Its complete statement and proof were read. Its dissipation, finite-length, and deterministic continuation arguments were checked and transferred to the projected flow below. The Gaussian initialization event is taken from that lemma.
2. **Imported analytic and carrier bounds:** Proposition `cp:source`, parts (i) and (ii). The complete proposition was read. Its physical-time rectangle, vector RMS bound, and real dense carrier bound match the candidate exactly. Its long stopped-cavity probability proof is not re-certified here.
3. **Directly checked signed estimate:** The complete signed perturbation lemma in `compact_fitting.tex` and the comparison and coefficient ledger inside the complete Legendre construction proof in `compact_legendre.tex` were read. The relevant pair-of-states argument is re-derived below. It uses no moment equation of the original closure.
4. **Directly checked compiler dependency:** Proposition `cp:jets` and its complete proof in `compact_selected.tex` were read. Its continuation map and finite-jet approximation are checked below; the required analytic-domain hypothesis comes from the imported source proposition.
5. **Imported relative-error denominator:** The complete statement of Proposition `cp:dense-lower` was read. Its lower bound is used only after proving the absolute error. Its probabilistic fluctuation proof is not re-certified here.

Thus the conclusions are stronger than a formal manipulation of the candidate's equations but narrower than a new audit of the whole paper.

## Global physical-time polynomial approximation

Let \(\ell_n=\log(en)\), and use the candidate's

\[
T=32\lambda^{-1}\ell_n,\quad
r_t=\frac{\lambda}{\beta^{30L}Y^2\sqrt{(d+3)\ell_n}},\quad
A=\max\{1,T/r_t\}.
\]

For any one training forward source, define the normalized vector function
\(g(s)=h_D(T(s+1)/2,x_a)/\sqrt n\). It is holomorphic on the required transformed rectangle and bounded there by \(\beta^{3L}\).

Put \(u=1/A\). Then \(0<u\le1\) and \(Tu\le r_t\). The physical-time Bernstein ellipse with parameter \(e^u\) has imaginary half-height \(T\sinh(u)/2<r_t\) and excess real half-width \(T(\cosh(u)-1)/2<r_t\). For example, \(\sinh(u)\le u\sinh(1)<2u\) and \(\cosh(u)-1\le u(\cosh(1)-1)<2u\). Thus both boundary circles in the Laurent argument lie in the holomorphic domain.

The Cauchy estimate is valid in vector Euclidean norm: integration of a vector-valued function of norm at most \(\beta^{3L}\) bounds its coefficient norm by the same scalar quantity. Symmetry under \(w\mapsto w^{-1}\) yields the Chebyshev coefficient bound \(2\beta^{3L}e^{-j/A}\). Consequently the degree-\(q-1\) approximation error is at most

\[
\frac{2\beta^{3L}e^{-q/A}}{1-e^{-1/A}}
\le4\beta^{3L}A e^{-q/A}.
\]

The factor \(4\) uses \(1-e^{-u}\ge u/2\) for \(0<u\le1\). There is no coordinatewise-to-vector loss of \(\sqrt n\).

For the Legendre projection, \(|P_j(s)|\le1\) on the real interval gives

\[
\|\Pi_q g\|_\infty
\le\sum_{j<q}(2j+1)\|g\|_\infty
=q^2\|g\|_\infty.
\]

The usual Legendre integral representation also proves the bound on \(P_j\), and is supplied in the permitted paper's projection proof. Apply \(I-\Pi_q\) to the Chebyshev approximation error, using exactness on degree below \(q\), to obtain candidate (11). Approximating each Legendre coefficient in normalized Euclidean norm to at most this error divided by \(q\) doubles the error, giving exactly

\[
\eta_q=8\beta^{3L}A(1+q^2)e^{-q/A}.
\]

At a fixed width there are finitely many coordinates and coefficients, so the compiler's coordinatewise tolerances can meet these vector tolerances. The approximating polynomial belongs to the span of the approximate coefficient vectors, even if they are nearly dependent. Orthogonal projection onto that span can only reduce its distance from the true source. This proves (13) without a condition-number assumption. Empty spans are harmless.

## Initialization-only provenance

The compiler's hypotheses apply to the finite training-source family with rectangle radius \(r_t\), interval length \(T\), and any sufficient coordinate bound, for example \(M=\beta^{3L}\sqrt n\). Integrals against rescaled Legendre polynomials are among its permitted polynomial time integrals.

For completeness, the compiler proof defines a holomorphic map \(\mathfrak t\) from the unit disk into the source rectangle, with \(\mathfrak t(0)=0\) and \(\mathfrak t(\xi_*)=T\) for some \(0<\xi_*<1\). Its displayed constants give real extrema \(-r_t\) and \(T+r_t\); the logarithm has imaginary part of magnitude less than \(\pi/2\), so the physical imaginary part is less than \(r_t\). The origin condition follows from \(b_1\theta=b_0=\tanh(\pi T/(8r_t))\). Its derivative is nonzero on the real interval.

The Taylor coefficients of \(g\circ\mathfrak t\) are finite linear combinations of derivatives \(g^{(k)}(0)\), and the uniform tail is bounded by \(M\xi_*^{N+1}/(1-\xi_*)\). Therefore some finite \(N\) supplies any prescribed positive tolerance. The source jets are obtained by the displayed formal coefficient recursion for the dense autonomous ODE at initialization. Integration of the resulting uniformly accurate functions gives the finite coefficient list.

This establishes the claimed provenance without access to a later dense state. It is an existence result in real-coordinate arithmetic. When \(T/r_t\) is large, \(\xi_*\) can be extremely close to one, so no favorable jet-order or precision claim follows. The candidate expressly preserves that limitation.

## Projected gradient flow and independent fitting

For each hidden interface take a fixed orthonormal basis \(U\in\mathbb R^{n\times r}\). The map \(C\mapsto CU^\top\) is an isometry because
\(\|CU^\top\|_F^2=\operatorname{tr}(CU^\top UC^\top)=\|C\|_F^2\).
Its ambient orthogonal projection is right multiplication by \(UU^\top\). With the first layer and readout retained in full, the fixed block projector \(P\) therefore gives exactly candidate (14)--(15), with no missing mobility factor.

The flow is autonomous: \(U\), initialized mixers, and data are fixed; current forward features, residuals, and backward responses are evaluated from the reconstructed current network. No source polynomial is supplied as time-dependent forcing.

Let \(\widehat\rho=\|\widehat r\|_2/\sqrt m\). On a stopped real tube,

\[
-\frac{d}{dt}\widehat\rho^2
=\|PV(\widehat\theta)\|_{\mathrm{par}}^2
\ge\frac4{m^2n}\|\widehat{\mathsf H}\widehat r\|_2^2
\ge\lambda\widehat\rho^2.
\]

The final inequality uses precisely the unchanged readout block and the stopped Gram bound \(\widehat{\mathsf H}^\top\widehat{\mathsf H}/(mn)\succeq\lambda I/4\). It requires no source approximation and no lower bound on the rank of \(U\).

For any stopped interval \([t,b]\), weighted Cauchy--Schwarz gives

\[
\left(\int_t^b\|PV(\widehat\theta)\|_{\mathrm{par}}\right)^2
\le
\left(\int_t^b\frac{-\partial_u\widehat\rho^2}{\widehat\rho}\,du\right)
\left(\int_t^b\widehat\rho\,du\right)
\le2\widehat\rho(t)\frac{2\widehat\rho(t)}\lambda.
\]

At a residual zero the whole field vanishes, so division by zero is unnecessary. In particular the readout RMS is at most \(R=2Y/\sqrt\lambda\).

Backward propagation gives \(\|\widehat\delta_a^{(j)}\|_2/\sqrt n\le D_jR\), where \(D_j=s(9s)^{L-j}\). The respective unprojected block speeds are bounded by

\[
2\widehat\rho D_1R,\qquad
4H\widehat\rho D_jR\ (j\ge2),\qquad
4H\widehat\rho.
\]

Projection cannot increase a hidden Frobenius speed. Hence every deterministic displacement estimate in the read fitting proof applies. More explicitly, its coefficients \(U_1=D_1\), \(U_j=2HD_j\), \(F_1=sU_1\), and \(F_j=s(2HU_j+9F_{j-1})\) give parameter displacements \(8U_jY^2/\lambda^{3/2}\) and feature RMS displacements \(8F_jY^2/\lambda^{3/2}\). With \(F=F_L\), the imported elementary coefficient estimate \(8H\sqrt F\le\beta^{5L}\) and the stronger assumed label cap give the same strict tube margins as in the paper. Using a supremum of the activation derivative on the real line instead of the half strip only decreases these coefficients.

The projected flow therefore continues globally, fits, has finite parameter length, and converges. Its predictions converge uniformly on the sphere because the network map is uniformly Lipschitz in parameters on the bounded tube. These conclusions precede the approximation comparison; there is no circular use of approximation to infer fitting.

Squaring and summing the *unprojected* block bounds separately gives exactly

\[
\|V(\widehat\theta)\|_{\mathrm{par}}
\le G\widehat\rho,\qquad
G=2\sqrt{4H^2+R^2(D_1^2+4H^2D_*^2)},\quad
D_*^2=\sum_{j=2}^L D_j^2.
\]

Thus \(\int_0^\infty\|V(\widehat\theta)\|_{\mathrm{par}}dt\le2Gz\). This is not inferred from projected energy dissipation; its independent proof is essential and correct.

## The signed comparison and its constants

The paper's comparison is an algebraic estimate at a pair of states. The only stochastic coordinate bound it needs is the actual dense carrier bound
\(M=32X^{21}z\sqrt{\ell_n}\). On the straight segment from the dense state to another state in the stated operator/readout tube,

\[
\delta_\vartheta-\delta_D
=\phi'(z_\vartheta)\odot(k_\vartheta-k_D)
+[\phi'(z_\vartheta)-\phi'(z_D)]\odot k_D.
\]

The changed-gate term is bounded in neuron RMS by \(t_2 M\) times the preactivation RMS difference. It does not require a coordinate bound on the second state or on an intermediate carrier. Changed mixers act on responses bounded in RMS. This proves the gradient-difference bound
\(\|\nabla f_a(\theta_\vartheta)-\nabla f_a(\theta_D)\|\le K\vartheta\|\theta-\theta_D\|_{\mathrm{par}}\)
with \(K=K_0+K_1M\) as in the paper. No layer multiplies another factor of \(M\).

The numerical ledger is adequate. For example, its quantities satisfy \(Q\le X^2\), \(F_{\rm seg}\le X^4\), \(P\le X^4\), \(d_0\le2X^3\), and \(d_1\le X^8\). The small label cap gives \((L-1)B_\delta\le1\), and \(\sqrt{L+1}\le X\). These imply the stated \(K_0\le X^9\) and \(K_1\le X^{13}\). The candidate's restricted readout bound \(2z\sqrt\lambda\) is smaller than the allowed \(8z\sqrt\lambda\).

For \(d_\theta=\widehat\theta-\theta_D\), put \(R_f=\widehat r-r_D-J_Dd_\theta\), where \(J_D\) is the dense prediction Jacobian and the sample norm is \(\|u\|_m=\|u\|_2/\sqrt m\). Segment integration yields

\[
\|R_f\|_m\le K\|d_\theta\|_{\mathrm{par}}^2/2,\qquad
\|(J_{\widehat\theta}-J_D)d_\theta\|_m
\le K\|d_\theta\|_{\mathrm{par}}^2.
\]

Direct gradient subtraction then gives

\[
\begin{aligned}
\langle d_\theta,V(\widehat\theta)-V(\theta_D)\rangle
={}&-2\|\widehat r-r_D\|_m^2
+2\langle\widehat r-r_D,R_f\rangle_m\\
&-2\langle\widehat r,(J_{\widehat\theta}-J_D)d_\theta\rangle_m\\
\le{}&K(\rho_D+3\widehat\rho)\|d_\theta\|_{\mathrm{par}}^2.
\end{aligned}
\]

This verifies the precise signed interface used by the candidate. It does not assume that the second state follows the old Legendre moment dynamics.

## Normal displacement and the all-time energy identity

Define the dense normal displacement
\(z_D=(I-P)(\theta_D-\theta_0)\). For each hidden layer and \(t\le T\), the normal gradient is

\[
-\frac2{nm}\sum_a r_{D,a}\delta_{D,a}^{(j)}
\big((I-UU^\top)h_{D,a}^{(j-1)}\big)^\top.
\]

Its Frobenius norm is at most \(2D_jR\rho_D\eta_q\). Indeed, the two vector factors contribute \(\sqrt nD_jR\) and \(\sqrt n\eta_q\), exactly cancelling the denominator \(n\), while \(m^{-1}\sum_a|r_{D,a}|\le\rho_D\). Squaring and summing the hidden-block bounds gives \(2D_*R\rho_D\eta_q\), with no missing sample or width factor.

Integration through \(T\), followed by the dense full-parameter tail bound, gives

\[
\sup_{t\in[0,\infty]}\|z_D(t)\|_{\mathrm{par}}
\le4D_*Rz\eta_q+R(en)^{-16}=Z_q,
\]

because \(\rho_D(T)\le Y(en)^{-16}\). This includes the limit by dense parameter convergence.

The decisive identity is exact. The restricted path stays in \(\theta_0+\operatorname{ran}P\), so \((I-P)d_\theta=-z_D\). For \(e=\|d_\theta\|_{\mathrm{par}}\),

\[
\begin{aligned}
\tfrac12\partial_t e^2
&=\langle d_\theta,PV(\widehat\theta)-V(\theta_D)\rangle\\
&=\langle d_\theta,V(\widehat\theta)-V(\theta_D)\rangle
-\langle(I-P)d_\theta,V(\widehat\theta)\rangle\\
&=\langle d_\theta,V(\widehat\theta)-V(\theta_D)\rangle
+\langle z_D,V(\widehat\theta)\rangle.
\end{aligned}
\]

In particular, the sign of the second term in candidate (20) is correct. Bounding it by \(Z_q\|V(\widehat\theta)\|\) uses the separately established unprojected-gradient integral. Both residual integrals are at most \(2z\), so

\[
\int_0^\infty K(\rho_D+3\widehat\rho)dt\le8Kz.
\]

The integrating factor for the squared-error inequality therefore yields

\[
e(t)^2\le2Z_q e^{16Kz}
\int_0^t\|V(\widehat\theta)\|_{\mathrm{par}}du
\le4GzZ_qe^{16Kz},
\]

and hence \(e(t)\le2\sqrt{GzZ_q}e^{8Kz}\). All constants in candidate (19)--(21) check exactly. There is no order-dependent feedback term to absorb and no need to divide by \(e\).

Finally,

\[
8Kz\le8X^9z+256X^{34}z^2\sqrt{\ell_n}
\le1+\sqrt{\ell_n},
\]

since \(8X^{-21}\le1\) and \(256X^{-26}\le1\). The coefficient of \(\sqrt{\ell_n}\) does not hide an exponential dependence on \(m/\gamma\).

## Whole-sphere accuracy, order, and storage

On the straight parameter segment, all operator bounds persist by convexity and the readout RMS is at most \(R\). Linear growth bounds features at every sphere input by the candidate's \(Q\); backward propagation gives RMS \(D_jR\). The output-gradient blocks in mobility coordinates have norms at most

\[
D_1R,\qquad D_jRQ\ (j\ge2),\qquad Q.
\]

Their squared sum is exactly the candidate's
\(B^2=Q^2+R^2(D_1^2+Q^2D_*^2)\).
The fundamental theorem of calculus along the segment gives
\(|f_{\rm restricted}(t,x)-f_n(t,x)|\le Be(t)\), uniformly over the sphere. Thus the expanded error interface (24) is the direct substitution of (12), (19), (21), and (23); no width factor is introduced at prediction transfer.

For \(q=\lceil16A\ell_n\rceil\), fixed problem parameters give \(A=O(\ell_n^{3/2})\), \(q=O(\ell_n^{5/2})\), and
\(8\beta^{3L}A(1+q^2)=O(\ell_n^{13/2})\).
It is therefore eventually at most \((en)^8\), while \(e^{-q/A}\le(en)^{-16}\). This proves \(\eta_q\le(en)^{-8}\). The error is at most a fixed-problem constant times \(e^{\sqrt{\ell_n}}(en)^{-4}\), which is eventually less than \(Y/n\) for each fixed \(Y>0\). Extending to the fitted limit uses the already established parameter convergence.

The displayed mode bound can even use an absolute numerical constant: since \(\ell_n\ge1\),

\[
q\le17\ell_n+
512\beta^{30L}Y^2\lambda^{-2}\sqrt{d+3}\,\ell_n^{5/2}.
\]

Thus a common \(C=512\) suffices for candidate (1). The width threshold required for the accuracy claim still depends on the fixed problem parameters, as expressly allowed. This step does not establish uniformity when labels, sample count, dimension, depth, or gap vary with width.

The retained moving arrays have exactly
\(n(d+1)+n\sum_{j=2}^Lr_{j-1}\) coordinates, and the fixed bases have \(n\sum_{j=2}^Lr_{j-1}\), with \(r_{j-1}\le\min(n,mq)\). The initialized dense hidden mixers add \((L-1)n^2\) fixed coordinates. Products with reconstructed hidden weights can be evaluated as \(W_0h+C(U^\top h)\), and transposed products analogously, so no updated dense weight matrix need be retained. Data storage and activation-evaluator resources follow the paper's separate accounting convention.

This proves the claimed \(n\operatorname{polylog}(n)\) moving-state bound with other parameters fixed. It proves neither subquadratic total storage nor reduced matrix-vector arithmetic cost. The exact basis construction and discarded dense jet scratch are correctly excluded from the persistent moving-state count and correctly disclosed as unbounded preprocessing resources.

On intersection with the imported dense lower-bound event, division of \(Y/n\) by \(cY\sqrt\gamma/(\sqrt n\ell_n^{5/2})\) gives \(c^{-1}\ell_n^{5/2}/\sqrt{\gamma n}\to0\). A union bound needs no independence between the approximation event and the variability event; arbitrary fixed confidence then gives convergence in probability.

## Objections and qualifications

There is no blocking objection to the candidate within this review scope. The decisive qualifications are already stated and should be retained in any later presentation:

- The probabilistic analytic-source/carrier theorem and dense variability lower bound remain imported dependencies; this report does not certify their full proofs.
- The new runtime is a fixed-subspace restricted gradient flow. The result says nothing sharper about the original moving residual-clock Legendre model.
- The initializer is justified by finite jets in exact real arithmetic; there is no bound on their number, precision, time, or working memory, and no finite-precision basis guarantee.
- The \(Y/n\) assertion is eventual for each fixed positive \(Y\) and fixed problem. The unquantified width threshold is essential.
- Fixed dense mixers remain quadratic. The verified improvement is in moving-state dimension.

No correction to the new proof was needed for this verdict.

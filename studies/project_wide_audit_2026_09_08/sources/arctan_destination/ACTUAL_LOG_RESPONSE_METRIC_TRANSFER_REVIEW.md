# Independent adversarial audit of ACTUAL_LOG_RESPONSE_METRIC_TRANSFER.md

Verdict: PASS for the stated canonical finite-width logarithmic spectral estimates in the explicitly defined transformed metric. No correction to this candidate's displayed estimates or their stated scope is required.

The separate verdict on the complete corrected current ACTUAL_CLOCK_RANK_ONE_RESPONSE.md is also PASS. Its current lines 158–169 explicitly define the independent auxiliary probe, identify the n positive covariance eigenvalues, and include the N-n zeros. The earlier clock wording correction and its resolution are preserved as history in the separate clock audit. The present audit uses the corrected clock dependency identified below.

## Inputs and independent scope

I read this complete candidate and used only its three permitted mathematical dependencies, each read in full in this task. In particular, I reread the complete revised ACTUAL_SQUARED_LOG_RESPONSE.md after its update and the complete corrected ACTUAL_CLOCK_RANK_ONE_RESPONSE.md after its correction, and verified their current hashes. No parent history, ledgers, numerical experiments, other mathematical notes, or review files were inspected. Claims below are checked against the mathematical arguments in the permitted files, not against a review status. The solve-math-rigorously skill instructions were read directly earlier in this task. No input file was modified.

All four current SHA-256 hashes below were computed after the clock correction and checked again before finalizing this report; those sets agree. The metric-transfer candidate, squared-log dependency, and primal dependency are unchanged from their complete readings. The corrected clock note was reread in full at the new hash.

| Role | Exact path | SHA-256 |
| --- | --- | --- |
| Metric-transfer candidate | `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/ACTUAL_LOG_RESPONSE_METRIC_TRANSFER.md` | `29304fb9771653257d3d638908ad4a08aca60690ce3ff4a9f2edfe73bf4bca0e` |
| Squared-log dependency | `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/ACTUAL_SQUARED_LOG_RESPONSE.md` | `d416464bf1b5e4a792bb6937f0f7eec0e5d19cd70ca05816d02f011bf64547f0` |
| Clock dependency | `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/ACTUAL_CLOCK_RANK_ONE_RESPONSE.md` | `a3e093852f07d58b474197fd4781dfb69830203a21eda7e788d45af27f28f0bd` |
| Primal dependency | `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/READOUT_COERCIVITY.md` | `0bd062da74fbde03d41a125561beee7345915ea6aa0578ed8e7b81d2c9f08c53` |

Line references below are to these versions. The transformed metric is the one explicitly defined by candidate lines 9–14. No claim about an uninspected note's metric is needed to establish the results audited here.

## 1. Coordinate map and endpoint conjugacy: PASS

The scalar map \(F(z)=z+z^3/3\) has derivative \(1+z^2>0\), tends to opposite infinities at the two ends of the real line, and has a smooth inverse. Applied coordinatewise and combined with the stated linear block scalings, it gives a global smooth change of coordinates \(T:\theta\mapsto\eta\).

The raw coordinates are

\[
\theta=(z^{(1)},\sqrt nW^{(2)},\sqrt nW^{(3)},W^{(4)}),
\]

and the transformed orthonormal coordinates are

\[
\eta=(F(z^{(1)})/\sqrt n,W^{(2)},W^{(3)},W^{(4)}/\sqrt n).
\]

Differentiating every block gives exactly

\[
DT(\theta)=n^{-1/2}H(\theta),\qquad
H(\theta)=\operatorname{diag}(1+(z_i^{(1)})^2,I_{n^2},I_{n^2},I_n),
\]

where the first listed block is diagonal of size n. Its inverse derivative at \(\eta_0\) is \(\sqrt nH_0^{-1}\). For either the fixed-feature-duration or fixed-physical-duration flow, the chain rule for \(T\circ\mathcal F\circ T^{-1}\) therefore gives

\[
U_\eta=n^{-1/2}H_tU_\theta\sqrt nH_0^{-1}
=H_tU_\theta H_0^{-1}.
\]

The scalar cancellation in equation (2) is exact. This is the derivative of the same flow expressed in new coordinates; it does not require the new coordinates to be an isometry or posit a different Euclidean gradient flow in those coordinates.

There is no missing derivative of H in this first-derivative identity. H is the derivative of the endpoint coordinate map, already evaluated at the endpoint. Its own derivative would enter a second-derivative calculation or an equation for the transformed Jacobian, neither of which is used here.

For an isometric seed E in eta coordinates, the actual raw initial variation is \(\sqrt nH_0^{-1}E\). The candidate's auxiliary \(V_0=H_0^{-1}E\) at lines 76–78 is the factor remaining after the two scalar factors in the conjugacy have canceled. Using this auxiliary matrix in the ensuing bounds is correct; no covariance normalization is being inferred from that auxiliary identification.

## 2. Logarithmic energy with arbitrary initial full-rank embeddings: PASS

The mathematical dependency supplies more than its isometrically initialized corollary. For \(V'=DV\), a full-column-rank V, and continuous D on a finite interval, define

\[
G=V^TV>0,\quad Q=VG^{-1/2},\quad
\mathcal E=\tfrac14\operatorname{Tr}[(\log G)^2]=\Lambda(V)^2.
\]

Then \(Q^TQ=I\), regardless of whether the initial V is isometric. Differentiating the trace function gives

\[
G'=2G^{1/2}Q^TD_{\rm sym}QG^{1/2},\qquad
\mathcal E'=\operatorname{Tr}[(\log G)Q^TD_{\rm sym}Q],
\]

where \(D_{\rm sym}=(D+D^T)/2\). The trace formula is valid at repeated eigenvalues: in an eigenbasis of G, the differential of the trace keeps the diagonal terms \(g'(\lambda_j)G'_{jj}\), and \(g'\) is constant on a repeated-eigenvalue block. Equivalently, the differential of log has diagonal entry \(G'_{jj}/\lambda_j\), obtained from its resolvent integral.

Frobenius Cauchy–Schwarz and compression by an isometry yield

\[
|\mathcal E'|\le2\sqrt{\mathcal E}\,\|D_{\rm sym}\|_{\rm F}.
\]

For \(\varepsilon>0\),

\[
\frac{d}{dt}\sqrt{\mathcal E+\varepsilon}
\le\frac{\sqrt{\mathcal E}}{\sqrt{\mathcal E+\varepsilon}}
\|D_{\rm sym}\|_{\rm F}
\le\|D_{\rm sym}\|_{\rm F}.
\]

Integration and \(\varepsilon\downarrow0\) prove the needed generalization:

\[
\Lambda(V(t))\le\Lambda(V(t_0))+
\int_{t_0}^t\|D_{\rm sym}(u)\|_{\rm F}\,du.
\]

No step sets the initial energy to zero. Full column rank persists because the square fundamental solution is invertible. Thus nonisometric initial embeddings, repeated singular values, and zero initial logarithmic energy are all covered.

For symmetric positive definite H, the path \(V_r=H^rV\) is well defined and full rank, and satisfies \(V_r'=(\log H)V_r\). Since \(\log H\) is symmetric, the preceding inequality yields exactly

\[
\Lambda(HV)\le\Lambda(V)+\|\log H\|_{\rm F}.
\]

This verifies candidate equation (3), including its coefficient one. It is an endpoint multiplication bound for rectangular matrices, not a false assertion that logarithms of singular values add individually under multiplication. Applying it to \(H^{-1}\) costs the same amount because \(\log H^{-1}=-\log H\).

## 3. RMS control suffices for the endpoint logarithms: PASS

For \(u>0\),

\[
\frac{d}{du}\bigl(2\sqrt u-\log(1+u)\bigr)
=\frac1{\sqrt u}-\frac1{1+u}>0,
\]

because \(1+u-\sqrt u=(\sqrt u-1/2)^2+3/4>0\). The difference is continuous at zero with value zero. Therefore \(0\le\log(1+u)\le2\sqrt u\) for all \(u\ge0\). Squaring at \(u=z_i^2\) and summing yields

\[
\|\log H\|_{\rm F}^2
=\sum_{i=1}^n[\log(1+z_i^2)]^2
\le4\sum_{i=1}^nz_i^2.
\]

The identity blocks contribute zero, so there is no factor involving the full dimension \(N=2n^2+2n\). The bound applies even if the RMS control permits a single coordinate of size proportional to \(\sqrt n\). No maximum-coordinate, fourth-moment, or sixth-moment estimate is needed. Although F itself is cubic, only the logarithm of its derivative appears in this spectral argument. The candidate does not need a width-uniform second moment of F(z) itself.

## 4. Feature propagator bound and its dependency constant: PASS

The permitted raw dependency uses \(b=\nabla_\theta(nf_n)\), with blocks

\[
\left(\delta^{(1)},\frac{\delta^{(2)}(h^{(1)})^T}{\sqrt n},
\frac{\delta^{(3)}(h^{(2)})^T}{\sqrt n},h^{(3)}\right).
\]

I verified its Hessian calculation in these coordinates. For completeness, with \(K_2=a+M\) and \(K_3=a+MK_2\), its three activation-curvature terms have Frobenius bounds

\[
2M^2R\sqrt n,\quad2MK_2^2R\sqrt n,\quad2K_3^2R\sqrt n.
\]

The two trained-matrix symmetrized cross terms cost at most \(2MR\sqrt n\) and \(2RK_2\sqrt n\); their unsymmetrized factors have rank at most n. The hidden/readout Hessian blocks cost \(\sqrt{2n}K_3\). These add to exactly

\[
\|B\|_{\rm F}\le C_B(M,R)\sqrt n,
\quad
C_B=2R(M^2+MK_2^2+K_3^2+M+K_2)+\sqrt2K_3.
\]

The derivative maps for the two preactivations have operator bounds \(K_2,K_3\), and the backward vectors satisfy \(\|q^{(1)}\|_2\le M^2R\sqrt n\), \(\|q^{(2)}\|_2\le MR\sqrt n\). Thus this estimate does not use an unverified bound on individual backward coordinates. Both trained matrices and all curvature terms are retained.

For a transformed isometry E, equation (3) gives

\[
\Lambda(H_{s_0}^{-1}E)\le\|\log H_{s_0}\|_{\rm F},
\]

since \(\Lambda(E)=0\). The nonzero-initial-energy inequality applied along the actual raw feature flow then gives

\[
\Lambda(U_\theta(s,s_0)H_{s_0}^{-1}E)
\le\|\log H_{s_0}\|_{\rm F}+C_B\sqrt n(s-s_0).
\]

Multiplying by \(H_s\) costs at most \(\|\log H_s\|_{\rm F}\). Using the RMS inequality proves exactly candidate equation (5). Its endpoint coefficients are both 2. At \(s=s_0\), the actual response is E with zero energy, while the upper bound may be positive; this is permitted and explicitly acknowledged.

The revised dependency's restriction to the raw metric is respected. The present proof supplies a new comparison with endpoint costs, rather than assuming equality of spectra between the two metrics.

## 5. Gaussian column seeds, covariance normalization, and increments: PASS

Let \(g\sim N(0,I_n)\) be independent of the full trained trajectory. The physical matrix perturbation is infinitesimally \(\delta W^{(3)}=ge_i^T/\sqrt n\). Its raw seed is \(E_ig\), where \(E_i^TE_i=I_n\). Every H acts as the identity on this seed block, so

\[
H_sE_i=H_{s_0}E_i=H_{s_0}^{-1}E_i=E_i.
\]

For a feature segment starting at zero, set \(Y_i=U_\theta(s,0)E_i\). The actual transformed response to the stated Gaussian seed is

\[
\widetilde Y_i g=\frac1{\sqrt n}H_sY_i g
=\frac1{\sqrt n}U_\eta(s,0)E_i g.
\]

In particular, an isometric seed E_i in eta space and the actual Gaussian column seed are different by the factor \(1/\sqrt n\). The candidate keeps that distinction.

Conditional on the trajectory, the response covariance is

\[
\operatorname{Cov}(\widetilde Y_i g\mid\text{trajectory})
=\frac1nH_sY_iY_i^TH_s.
\]

Its n positive eigenvalues are

\[
\lambda_j=\sigma_j(H_sY_i)^2/n,
\]

with N-n additional ambient zero eigenvalues. Therefore

\[
\Lambda(\sqrt n\,\widetilde Y_i)^2
=\frac14\sum_{j=1}^n[\log(n\lambda_j)]^2.
\]

There is no missing n factor in equation (6). If restated explicitly as a bound on squared covariance logarithms, its squared right-hand side is multiplied by 4. The prose that the logarithms concern n times the positive covariance eigenvalues is correct; it does not assert a conflicting numerical constant for that conversion. At initialization the n positive covariance eigenvalues are exactly 1/n, and the ambient covariance also has zeros. Lines 106–108 concern those positive eigenvalues.

For the trained increment, differentiating \(\eta(s)-\eta(0)\) with respect to this seed gives

\[
\widetilde Z_i
=\frac1{\sqrt n}(H_sY_i-H_0E_i)
=\frac1{\sqrt n}(H_sY_i-E_i).
\]

The subtraction is exact even though F is nonlinear. Only this top-column seed is used; \(H_0E_i=H_sE_i=E_i\) is what makes the initial subtraction so simple. The same identity also follows by applying the current coordinate derivative to the raw increment \((Y_i-E_i)g\) for this particular seed.

Put \(A=H_sY_i\) and \(D=\sqrt n\,\widetilde Z_i=A-E_i\). For every input v,

\[
\|Dv\|_2^2\le2\|Av\|_2^2+2\|v\|_2^2,
\quad D^TD\preceq2A^TA+2I_n.
\]

Ordered eigenvalues thus satisfy \(1+\sigma_j(D)^2\le3+2\sigma_j(A)^2\). Since

\[
\log(3+2u^2)\le\log5+2(\log u)_+,
\]

one obtains

\[
\sum_{j=1}^n[\log(1+n\sigma_j(\widetilde Z_i)^2)]^2
\le2n(\log5)^2+8\Lambda(A)^2.
\]

Equation (6) supplies precisely equation (7)'s right-hand side. The increment matrix may lose rank or vanish at initialization; the \(\log(1+\cdot)\) expression handles zero singular values without an additional rank assumption.

The response distribution is the conditional Gaussian distribution of an independent derivative probe, with the actual trained coefficients. It is not a claim that a finite nonlinear perturbation remains Gaussian, or that the trained column is independent of its trajectory. The candidate explicitly makes this distinction. The same seed and covariance identities apply from any reached starting state after replacing zero by that start.

## 6. Rank-one interlacing survives endpoint conjugation: PASS

For the canonical raw flow, \(\nabla f_n=b/n\) and the physical field is \(2(1-f_n)b\). On every finite segment beginning with positive residual, the smooth state-dependent clock gives

\[
P_\theta-A_\theta=b(\theta_t)D_{\theta_0}s,
\]

where A is the derivative at the fixed feature duration that reaches the same base endpoint and P is the fixed-physical-duration derivative. The feature flow exists on bounded intervals by the permitted polynomial parameter bounds. The scalar residual satisfies \(e'=-2\kappa e\), so it remains positive for finite time. Smooth flow dependence in an open neighborhood of each finite orbit segment justifies the differentiation without changing or differentiating a probabilistic event.

The two maps have the same endpoint at the base state. Accordingly the same endpoint derivative matrices appear on both sides of the coordinate comparison:

\[
P_\eta-A_\eta
=H_t(P_\theta-A_\theta)H_{t_0}^{-1}
=[H_tb(\theta_t)][D_{\theta_0}s\,H_{t_0}^{-1}].
\]

This still has rank at most one. Multiplication by any fixed E preserves that rank upper bound. There is no additional perturbation caused by endpoint factors, because their base evaluations agree for the physical and feature maps. Both rectangular responses have full column rank: the raw finite-time derivative, the endpoint factors, and their inverses are invertible, and E is injective.

For completeness, rank-one rectangular interlacing follows by intersecting the span of right singular vectors k through m with the codimension-at-most-one kernel of the perturbation row. The resulting subspace has dimension at least m-k, giving \(\sigma_{k+1}(P)\le\sigma_k(A)\) by the variational characterization; exchanging A and P gives the reverse interlacing. Hence for \(2\le j\le m-1\),

\[
\sigma_{j+1}(A)\le\sigma_j(P)\le\sigma_{j-1}(A).
\]

Taking positive and negative parts of logarithms and summing their squares yields

\[
\sum_{j=2}^{m-1}(\log\sigma_j(P))^2
\le\sum_{j=1}^m(\log\sigma_j(A))^2.
\]

There is no coefficient two: where the shifted index ranges overlap, the positive and negative parts for that one A singular value have disjoint support. The proof is valid at repeated singular values and requires no tracking of singular vectors in time.

The corrected clock dependency also gives a precise independent-probe covariance interpretation, with n nonzero eigenvalues and N-n zeros. Its correction leaves the rank-one identity and interlacing arguments unchanged. These arguments have been checked mathematically here, without relying on any review verdict.

## 7. Uniform event, constants, reached starts, and small dimensions: PASS

The readout dependency proves positive acceleration \(c''=D_3A_3D_3c\) with a positive semidefinite coefficient, hence convexity of \(\|c\|_2/\sqrt n\) wherever it is nonzero. Its small-readout argument first controls the initial feature displacement, then obtains \(g'(s_0)\ge25b_0/48>b_0/2\), preventing a later readout zero. This yields \(\kappa\ge b_0^2/4\) and the finite feature endpoint \(s_*\le4e_0/b_0^2\). The normalized parameter action and Cauchy–Schwarz give every individual normalized vector displacement or matrix Frobenius displacement at most \(2e_0/b_0\) up to that endpoint. Thus the constants invoked by the current candidate have a valid deterministic basis.

Under the prescribed Gaussian initialization, take the single event with initial hidden operator norms at most 10, top feature RMS at least \(b_0=\sqrt{m_3}/2\), and readout RMS at most the fixed \(\varepsilon_0\) from READOUT_COERCIVITY.md equation (11). Here m_3 is its positive deterministic Gaussian moment. Conditional Gaussian laws for the hidden rows and bounded activation averages give convergence of the top feature empirical second moment to m_3. The Gaussian net bound controls the two hidden operator norms, and the expected squared readout RMS is \(n^{-2}\). Their intersection therefore has probability tending to one.

On that event, the clock note supplies

\[
M=10+2(1+a\varepsilon_0)/b_0,\quad
R=\varepsilon_0+2(1+a\varepsilon_0)/b_0,\quad
S_*=4(1+a\varepsilon_0)/b_0^2.
\]

The present note adds \(\|z^{(1)}(0)\|_2/\sqrt n\le2\). Its probability tends to one by the Gaussian law of large numbers. No independence of this event from the original event is required. On the intersection, the displacement estimate gives

\[
\sup_{s\in[0,s_*]}\frac{\|z^{(1)}(s)\|_2}{\sqrt n}
\le2+2(1+a\varepsilon_0)/b_0=R_1.
\]

This verifies candidate lines 126–137 without silently substituting a coordinatewise bound. All constants are fixed before taking a width limit.

For every pair \(0\le t_0\le t<\infty\), the feature segment from the reached state \(\theta(t_0)\) has length

\[
\Delta s=s(t)-s(t_0)\le S_*.
\]

All intermediate states and both endpoints obey the same bounds. Equation (5) therefore bounds the feature logarithmic energy by

\[
\Lambda(A_\eta E)\le\sqrt n(C_BS_*+4R_1).
\]

Combining with the conjugated rank-one trimmed inequality proves equation (8) exactly, including the normalization 1/n and the constant \((C_BS_*+4R_1)^2\). For a top-column isometry, \(H_{t_0}^{-1}E_i=E_i\) removes the initial endpoint cost, giving the sharper constant \((C_BS_*+2R_1)^2\) claimed in lines 156–159.

More explicitly, with \(\widetilde Y_{i,\rm phys}=n^{-1/2}U_{\eta,\rm phys}(t,t_0)E_i\), the last assertion is

\[
\frac1n\sum_{j=2}^{n-1}
[\log\sigma_j(\sqrt n\,\widetilde Y_{i,\rm phys})]^2
\le(C_BS_*+2R_1)^2.
\]

For its n positive covariance eigenvalues \(\lambda_j\), this is equivalently

\[
\frac1n\sum_{j=2}^{n-1}[\log(n\lambda_j)]^2
\le4(C_BS_*+2R_1)^2.
\]

These assertions hold pathwise for all reached starts and times, all isometric E of all admissible dimensions, and all finitely many column indices. An embedding may be selected using the trained path; it is held fixed in each indicated derivative. No union bound over an uncountable family and no differentiability of an event indicator are needed.

For m=1 or m=2 the stipulated trimmed sum is zero; for m=3 the same interlacing proof bounds the single retained value. Thus n=1 and n=2 column probes have vacuous but correct physical trimmed estimates. The feature estimates and the increment expression remain well defined at those widths. At equal start and end, the unscaled transformed full response is the identity on E, the column covariance has positive eigenvalues 1/n, and the increment vanishes. Nonsharp positive upper bounds at zero duration are not contradictions. All times in the supremum are finite; continuity of the primal feature endpoint is used only for parameter bounds, not to assert differentiability or invertibility of an infinite-time response.

## 8. What this PASS does and does not establish

The note successfully transfers logarithmic spectral estimates for the same canonical flow from the raw coordinates to its specified transformed metric. The transfer costs endpoint logarithmic energy controlled by first-layer RMS. It preserves the distinction between a transformed isometric seed and the actual Gaussian column perturbation, including all n factors, and preserves rank-one interlacing for physical time.

Equation (7) is a feature-time increment estimate using the full, untrimmed feature response bound. The physical-time conclusion stated in the note is the trimmed response estimate; the note does not assert an untrimmed all-time physical increment bound by replacing constants in equation (7). Such an inference would lack control of the excluded extremes.

These conclusions do not give width-uniform normalized trace or source-alignment bounds. A squared-log bound of order n permits exceptional singular values exponential in \(\sqrt n\), and the physical result explicitly excludes up to two extremes. This is a limitation of what the established inequalities imply, not a claim that responses are infinite at fixed width or that the actual canonical response must exhibit that exceptional behavior. No population existence, population uniqueness, or population closure assertion is being certified.

Final verdict for ACTUAL_LOG_RESPONSE_METRIC_TRANSFER.md with SHA-256 `29304fb9771653257d3d638908ad4a08aca60690ce3ff4a9f2edfe73bf4bca0e`, using the corrected clock dependency with SHA-256 `a3e093852f07d58b474197fd4781dfb69830203a21eda7e788d45af27f28f0bd`: PASS. No required corrections remain in this note. The separate current-hash clock verdict is also PASS; its historical wording correction remains documented separately.

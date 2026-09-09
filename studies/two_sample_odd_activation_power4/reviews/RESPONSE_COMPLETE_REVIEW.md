# Complete independent audit of the power-four theorem

Date: 2026-09-07. Verdict: **PASS for the complete stated odd two-input theorem**, at the four final hashes recorded below. This is a mathematical audit of the whole implication, with additional scrutiny of the source response. It is not a response-only conditional approval.

I read all four candidate files in full, inspected the needed original mathematical constructions directly, and verified all four candidate and all 23 dependency SHA-256 hashes. I did not read historical or sibling review files, review-status files, evidence ledgers, or review certificates. I did not edit a candidate or dependency, run a mathematical experiment, create a subagent, or make a commit. Hashing and text inspection were the only computational checks. The rigorous-math skill was applied.

The final mathematical chain has no unresolved obstruction found in this audit. In particular, the raw-L2 step uses the actual capped-program law before source closure; it does not assume the theorem it is meant to prove. The exact backward derivative identity has a single curvature insertion and therefore a single explicit incoming-field factor. Its full-row bound places the terminal-time maximum outside expectation. The final common affine prefactor is \(10^{30}\exp(2100)<H\), which covers its displayed numerical products.

## 1. Exact scope audited

The target is the theorem of `two_sample_odd_activation_theorem/PROOF.md`, with its amplitude selection replaced by

\[
0<e\le c_{\rm poly}\delta^4,\qquad
\phi_{a,e}(z)=az+e\arctan z,\qquad a\in[1/2,1].
\]

It concerns two deterministic inputs of squared norm \(d\), all binary label pairs, and 
\(|\rho|\le1-\delta\), \(0<\delta\le1\). I checked the original finite equations and metric rather than interpreting “the complete theorem” as a scalar ODE statement. The initialization remains independent Gaussian with first-layer variance \(1/d\), middle-matrix variance \(1/n\), and readout variance \(n^{-2}\). The metric is

\[
\frac dn\|dW^1\|_F^2+\|dW^2\|_F^2+\|dW^3\|_F^2+\|dC\|_n^2.
\]

The loss is \(\tfrac12\sum_i(f_i-y_i)^2\); simultaneous raw GD has step \(n^{-2}\), raw linear interpolation, recomputed hidden fields, and the stated right-node/terminal-left velocity convention. All three hidden blocks and the readout are trained.

The result retains the autonomous global strong population trajectory, nonsymmetric bounded-primal uniqueness on its canonical action spaces, reached-state restart, full-width-sequence joint GF/GD convergence on each fixed finite physical interval, the four complete sample kernel matrices, actual initialized/trained actions and adjoints on generated probes, same-layer joint path and velocity laws, second moments and integrated squared speeds, strict activation-regression nonaffinity, and the initial motion certificates.

The quantifiers remain for each fixed dataset and each fixed finite physical horizon. They do not assert a single positive amplitude for all separations tending to zero, uniform width convergence across datasets, a three-input result, or cross-layer coordinate pairing. The excluded incompatible odd-network endpoints are not silently included. This matches the stated odd theorem; the older contract's ultimate all-angle aspiration is broader and is not proved by this candidate.

## 2. Original mathematical sources inspected

The substantive source inspection included the following chains.

* Original odd `PROOF.md`, `AFFINE_CORE.md` (label folding, exchange symmetry, normalization, inactive-field freezing and Gaussianity), `SOURCE_AND_LIMIT_BRIDGE.md`, and `INITIAL_MOTION_AND_NORMALIZATION.md`.
* Quantitative `PROOF.md`, `AFFINE_POLYNOMIAL_BOUNDS.md` and `POLYNOMIAL_RESPONSE_LEMMA.md`, covering the explicit primal/nonaffinity constant, the raw comparison available before source closure, the learned-moment forcing, temporal kernel algebra and same-array source convention.
* Power-ten `AFFINE_SOURCE_CERTIFICATE.md`, including exact sample/time normalization, both answer orientations, independent-root probes, the top backward probe, the backward top resolvent, beta positivity and the three inner beta scales. I also inspected its refined response and the original exact source equations to check which estimates are being replaced.
* Original `sources/TWO_SAMPLE_SOURCE_BASELINE.md`, especially the source equations \(5\)--\(10\), derivative equations \(12\)--\(16\), probe identity \(23\)--\(25\), and common-action/finite-primal explanation.
* Original `sources/L3_LOCAL_COMPLETE_PROOF.md`, generic Gaussian conditioning, source-derivative identification, singular-Gram regularization, feedback identification, common generated actions and adjunction. These generic parts have the appropriate coordinate-map hypotheses; the old special activation's local theorem is not being imported unchanged.
* Original `sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md` and `sources/FIXED_CAP_VELOCITY_BRIDGE.md`, including the actual two-residual comparison, the appended velocity-product queries, product truncation, and the order of cap and velocity-truncation removal.

All 23 files in the dependency manifest were hash-verified. This inventory distinguishes substantive inspection of the needed mathematics from a claim to have reread every line of every historical source compilation. No review outcome supplies a mathematical premise.

## 3. Primal bounds and the absence of circularity

Let \(v=(1+y_1y_2\rho)/2\), \(r=\sqrt v\), \(\lambda=a^3r\), and

\[
M=\left(\frac3{\sqrt2\lambda}\right)^{1/4}>1.
\]

These are the actual dataset scales. In particular

\[
r=\frac3{\sqrt2a^3}M^{-4},\qquad
S\le\frac2\lambda=\frac{2\sqrt2}{3}M^4<M^4,
\qquad M\le24^{1/4}\delta^{-1/8}.
\]

The reference normalization is an isometry for the active first raw component, not a change of optimization metric. Perpendicular first-layer directions are annihilated by the affine objective, including when that objective is evaluated at a nearby nonlinear state. Thus the comparison covers full raw discrepancies and does not restrict the nonlinear trajectory to an active affine subspace.

The old quantitative comparison only differentiates the affine vector field. Its same-state nonlinear forcing uses \(|\arctan|\le\pi/2\), bounded gates and \(|\tau_R(q)|\le|q|\), uniformly in cap. Hence

\[
E_{\rm raw}\le C_0e\lambda^{-3}\le HeM^{12}
\]

is available for actual capped paths independently of any new coefficient bootstrap. The prior condition \(e\le c_*\delta^{7/4}\) is implied by \(e\le c_{\rm poly}\delta^4\), since \(c_{\rm poly}\le c_*\) and \(\delta^4\le\delta^{7/4}\). It supplies a strict raw tube, \(g_{e,R}(S)\ge5/4\), and the regression margin.

On that actual tube, the raw actions and readout are \(O(M)\). Repeatedly applying the actual bounded actions gives

\[
\|C\|_2\le HM,
\quad \|q^2\|_2=\|B^*\delta^3\|_2\le HM^2,
\quad \|q^1\|_2=\|A^*\delta^2\|_2\le HM^3,
\]

because \(\|\delta^\ell\|_2\le(a+e)\|q^\ell\|_2\) and \(\|\delta^3\|_2\le(a+e)\|C\|_2\). The large numerical \(H\) absorbs the fixed raw size and gate constants.

The fixed-program source identification equates the laws of these actual queries with the named-source output laws, already at fixed cap and mesh. Its existence requires only bounded-derivative coordinate maps at that fixed cap, not cap-uniform derivative estimates. Therefore transferring the preceding L2 norms to the source equations is legitimate before the first-exit argument. A bounded L2 operator is used only for an L2 estimate. No Lp or Gaussian-tail preservation property of arbitrary canonical actions is presumed.

The primitive source standard deviations are consequently bounded by \(H\) times \(1,M^2,M,M,M^2\), in the order stated in the candidate. The learned second-moment difference is bounded by a constant times \(M^3E_{\rm raw}+eM^4\), hence \(HeM^{15}\). Multiplication by \(h_j\) and summation over a backward time row costs at most \(HM^4\), producing \(H^2eM^{19}\). These moment errors also predate source closure.

**Status: PASS.**

## 4. Sharpened affine geometry, probes and normalization

With \(z=\|D\|^2\), the balance identities give exactly the claimed bounds on \(K,J,K_B\), \(s_A=\|Ap\|^2\), and \(s_B=\|B^*D\|^2\). I checked the two less immediate gradient estimates:

\[
\|D'\|^2\ge\frac{s_A^2}{1+z}-100s_A
\ge z^3-99z^2-10200z-10100,
\]
\[
\|p'\|^2\ge\|BB^*D\|^2-100s_B
\ge z^3-100z^2-10000z.
\]

The second uses \(BB^*D=zD+K_BD\) with \(K_B\ge0\). The first bounds its positive and negative terms separately; it does not assume monotonicity of the quadratic in \(s_A\). Adding the two matrix-gradient lower bounds produces \(4z^3-197z^2-20200z-10100\), exactly as written.

For \(P(z)=z^4-(197/3)z^3-10100z^2-10100z\),

\[
\frac d{dt}(F^2-P(z))=2F(F'-P'(z))\ge0.
\]

This argument is valid at \(F=z=0\). The old \(F\ge z^2/\sqrt2\) estimate covers \(z\le200\); for \(z\ge200\), the displayed difference \(P(z)-(z^2-100z)^2\) is strictly positive. Thus \(F\ge z^2-100z\) is valid globally on the relevant affine existence interval.

At scale beta this yields

\[
(\log w_\beta)'\ge c_\beta^2-101\beta^2,
\qquad w_\beta^2=\beta^2+c_\beta^2.
\]

Each column of the raw affine Hessian has three blocks, each bounded by the product of two remaining raw factors. Its norm in the component sum norm is at most \(3R_\beta^2\), and on the radius-one tube at most \(3(R_\beta+1)^2\). The nonlinear state need not satisfy affine balances for this tube estimate.

The old radial inequalities imply \(\int c_1\,dt\le1+\sqrt2\). Homogeneity gives the same upper bound for \(\int c_\beta\,dt\) when \(\beta\ge1\). With \(T<2\) and \(\beta\le1.001\),

\[
\int_s^t3R_\beta^2\,du
\le3\log\frac{w_\beta(t)}{w_\beta(s)}+1810,
\qquad \int_0^T R_\beta\,du<31.
\]

The additional tube cost is at most \(6\cdot31+3\cdot2=192\), so 2100 safely covers the total absolute cost. The coefficient of the logarithm remains exactly three. The common enlarged interval gives \(w_\beta(T)\le30M\), hence \(G\le10^5e^{2100}M^3\). The old extension time and beta gaps still apply. Fine-mesh Euler convergence and deterministic integral approximation preserve these bounds with the stated factor-four margin; no minimum step is required.

I checked the link from this propagator to the actual formal source arrays. The original independent-root identity takes width first at fixed nonzero probe amplitude and fixed mesh, pairs the output with that root, and only then sends its amplitude to zero. It identifies frozen formal derivatives, including off-support source directions at singular covariance. It is not an identification of an arbitrary raw tangent with a coupled covariance derivative. The probe locations, later recomputation of updates, and direct identities are retained.

The bottom-transpose and top-forward coefficient probes have product cost one. The middle two have product cost \(O(M^2)\). The needed resolvents, including the top backward resolvent, have product cost \(O(M^2)\); the top backward-to-forward strict transfer costs \(O(M^4)\). The strict pulse retains \(\Delta t_j\), and signed reuse of a single independent root bounds an entire deterministic row. The normalized density orders are therefore \(3,5,3,5\), the resolvent row order is 5, and the top strict-transfer order is 7.

Beta scaling multiplies the initialized-matrix return variances by \(\beta^2\). All active learned contractions and source entries are nonnegative-coefficient polynomials in beta: finite affine ascent expansions have nonnegative polynomial coefficients in the centered Gaussian entries, and Wick contractions contribute nonnegative variance weights. This does not assert positivity of realized Gaussian matrices. The beta derivative bound at the far reference costs two powers of \(M\), giving the normalized \(FL,RF,RFL\) density order 7.

The exact active array factors are

\[
A_2=(r/a)\widehat A_2,
\quad A_3=ar\widehat A_3,
\quad B_3=(ar)^{-1}\widehat B_3,
\quad B_2=(a/r)\widehat B_2.
\]

Strict densities have the extra \(\Delta t_j/h_j=\lambda\). Thus forward densities gain \(r^2\asymp M^{-8}\), backward rows gain \(r^{-1}\asymp M^4\), and diagonal-sector resolvent rows do not change. This produces the active orders \(-5,-3,7,9,5,-1\) used in the candidate. Inactive forward densities remain \(O(1)\), inactive backward arrays vanish, and inactive resolvents are identity. There is no illicit use of \(r\asymp M_\delta^{-4}\) for a uniform envelope replacing the actual \(M\).

The final affine ledger is numerically sufficient: its displayed product is at most

\[
(4\cdot10^{14})(10^3)(3\cdot10^7)(10^4)e^{2100}
=1.2\cdot10^{29}e^{2100}<10^{30}e^{2100}<H.
\]

**Status: PASS.**

## 5. Exact response calculation and its moments

Write the local equations as

\[
Z=\xi+K\delta,\quad q=\zeta+B\phi(Z),\quad
\delta=D_{a,e,R}(Z,q).
\]

Here \(K\) is strict, \(B\) is causal, and sample matrices are kept intact. Put

\[
R=(I-a^2KB)^{-1},\quad U=RK,\quad
L=(I-a^2BK)^{-1}.
\]

Both inverses are finite causal algebraic inverses; arbitrary backward current diagonals cause no same-time inversion problem. The strict transfer \(U\), rather than a large nonperturbative Lipschitz constant, carries every nonlinear derivative feedback.

### 5.1 Value estimates are justified before Hölder

Solving only the affine part of the actual value equations gives the three formulas in `PRIMAL_L2_RESPONSE.md` §2. They retain the same deterministic arrays as the nonlinear program, including the \(a^{-1}\) and \(a^{-2}\) factors. Using the full sample transfer box gives leading/self exponent pairs

\[
(6,13),\quad(6,11),\quad(7,8)
\]

for \(Z^1,Z^2,Z^3\). The p-norm constants are independent of \(p\ge2\). Absorption is valid under the displayed smallness condition and gives incoming p-norm orders \(15,13,11\), with coefficient \(H^{10}\sqrt p\).

Finite-cap, finite-mesh variables already have finite moments, so this absorption does not rearrange an inequality between infinite quantities. Expanding \(\exp(Q^2/L_Q^2)\) in even moments yields subGaussian scales \(H^{11}M^{15},H^{11}M^{13},H^{11}M^{11}\). Temporal correlations and covariance singularities do not enter this argument.

### 5.2 Derivative identities and the number of explicit Q factors

Let \(G=aI+\Delta G\), \(V=aI+\Delta V\), and

\[
L_g=e\operatorname{diag}(g'(Z)\tau_R(q)),\qquad
P=L_g+a\Delta V B+aB\Delta G+\Delta V B\Delta G.
\]

Direct differentiation gives

\[
D\delta=aI^\zeta+\Delta V I^\zeta+a^2BJ+PJ.
\]

Thus, with \(J_{\rm aff}=RI^\xi+aUI^\zeta\),

\[
J-J_{\rm aff}=U(\Delta V I^\zeta+PJ),
\]
\[
D\delta-D\delta_{\rm aff}
=(I+a^2BU)(\Delta V I^\zeta+PJ)
=L(\Delta V I^\zeta+PJ).
\]

These are exact identities, not a first-order Taylor truncation. The final expression contains one \(P\) insertion and one actual \(J\). The only unbounded explicit local factor in \(P\) is \(L_g\), bounded by \(CeQ\). The dependence of \(J\) on other \(Q\)'s is accounted for by its exponential envelope. There is no second unbounded terminal multiplier multiplying \(LPJ\). Forward coefficient outputs multiply by \(G\), which is bounded. The direct transpose injection multiplies by \(\Delta V\), also bounded.

The deterministic \(B\Delta G\) and \(\Delta VB\) terms are essential and are included. Omitting them would incorrectly lower the middle backward defect power from 17 to 12.

### 5.3 Strict chronological envelope and exponential integrability

For a single bottom/middle transpose slot \(j\), \(J_k=0\) for \(k\le j\). The direct forcing has size \(H^3h_j\). For a complete forward-source row the direct bound is \(H^3M^5\), including the current identity. Extend rows by zeros in future slots when comparing row sizes.

Since \(U_{kr}\) is bounded by \(H^3h_r\), \(r<k\), the \(L_gJ\) term costs \(Ce\sum_{r<k}h_rQ_r|J_r|\). The remaining terms cost \(CeM^b\sum_{r<k}h_r\max_{s\le r}|J_s|\), with \(b=9,7,4\). The running-derivative majorant is therefore bounded by a causal product, at most

\[
\mathcal E_k=\exp\left(eH^6\sum_{r<k}h_r(Q_r+M^b)\right).
\]

This running maximum is a pathwise device for the derivatives. It does not replace the individual \(Q_r\)'s by a random maximum over source times. The source-time \(h_j\) factor persists in every later term.

For each fixed \(k\), weighted Jensen with weights \(h_r/S\) bounds the stochastic exponential by a convex combination of one-time exponentials. The largest integrated stochastic order is \(4+15=19\); the others are 17 and 15. The deterministic orders are 13, 11 and 8. The stochastic numerical coefficient before fixed moment factors is \(H^6H H^{11}=H^{18}\). Under \(eH^{22}M^{19}\le1\), the remaining factor \(H^{-4}\) is enough for moments through order eight to be at most two. For an explicit numerical justification, use

\[
uQ\le\tfrac12Q^2/L_Q^2+\tfrac12u^2L_Q^2
\]

and Cauchy--Schwarz on the subGaussian exponential. The resulting factor is at most \(sqrt2\exp(u^2L_Q^2/2)\); the tiny stochastic rate and deterministic contribution keep the product below two. This uses no independence between source times. The same condition implies the earlier value absorption with strict slack.

### 5.4 Raw L2 and complete backward rows

For every pair \(r,k\), the actual-primal estimates now give

\[
\mathbb E[Q_r\mathcal E_k]
\le\|Q_r\|_2\|\mathcal E_k\|_2
\le H^2M^{q_{\rm raw}},\qquad q_{\rm raw}=3,2,1.
\]

Both factors live in the same actual source law. They may be dependent. This is ordinary Cauchy--Schwarz, and neither an improved covariance comparison nor a raw Lp estimate for \(p>2\) is needed.

The forward single-slot estimate has power

\[
4+\max(q_{\rm raw},b)=13\quad\hbox{or}\quad11.
\]

Here the two strict-transfer factors have power zero, the time integral costs four, and the initial factor remains \(h_j\). Bounded terminal feature gates preserve those exponents.

For backward coefficients fix a terminal time \(k\), expand the deterministic \(L\) row, and sum the absolute source-column entries. For example its curvature term is bounded by

\[
Ce\sum_{r\le k}|L_{kr}|
\mathbb E\left[Q_r\sum_{j\le r}|J_{rj}|\right]
\le Ce|L|_r H^3M^5 H^2M^{q_{\rm raw}}.
\]

The other terms insert a deterministic \(B\) row between bounded gates and \(J\); expanding that row and using the uniform envelope moment gives the same expression with \(M^b\). Taking the maximum over deterministic terminal times afterwards yields

\[
\max_k\mathbb E\sum_{j\le k}|(D\delta-D\delta_{\rm aff})_{kj}|
\le H^{19}eM^{10}(M^{q_{\rm raw}}+M^b).
\]

This directly bounds \(max_k\sum_{j\le k}|\mathbb E(D\delta-D\delta_{\rm aff})_{kj}|\), the coefficient norm required by closure. No \(\mathbb E\max_k\) bound is claimed or used. The powers are 17 for \(B_2\) and 14 for \(B_3\).

The original current identities are retained: \(B^3_{kk}\) contains \(\mathbb E L^3_{g,k}\), and \(B^2_{kk}\) contains both \(\mathbb E L^2_{g,k}\) and the \(B^3_{kk}\mathbb E[V^2_kG^2_k]\) return. They are included by \(L_{kk}=I\), \(J_{kk}=I\) for a forward source, and the causal \(B\) rows. Random gates can mix sample sectors; the norm argument uses their full two-by-two action.

Adding learned-moment defects gives exactly

\[
q\le H^{30}eM^{19}.
\]

The polynomial \(H\) budgets are ample: all transfer, envelope, raw-L2, time and gate factors in the displayed products lie below the intermediate \(H^{19}\) or \(H^{21}\) allowances. No hidden exponential in \(M\) remains outside the e-weighted envelope.

**Status: PASS.**

## 6. Sector transfer box and deterministic closure

Exchange equivariance commutes with the sample swap for the actual deterministic coefficient blocks at every finite source program. Therefore these blocks are diagonal in the mean/contrast basis. This is a statement about expected deterministic arrays, not individual gates or physical competitors.

On the active box, the outer backward excess radius is \(r_a=H^{-10}M^{-2}\). Since \(|F_b|_r\le H^2M^{-1}\) and \(|V_b|_r\le H^2M\), the two Neumann ratios are at most \(H^{-8}M^{-3}\) and \(H^{-8}M^{-1}\). The exact resolvent identities preserve the improved active forward densities and the \(M^5\) forward/reverse rows. In particular \(L_2=L_{2b}+L_{2b}J_3V\) controls the reverse row; the argument never assumes a right row multiplier preserves strict density.

The inactive integration rows have size \(O(M^4)\). Their separate radius \(r_i=H^{-10}M^{-5}\) gives a small \(O(H^{-8}M^{-1})\) ratio. The inactive top projection is zero. This is why the larger active radius does not destroy the inactive bounds. The resulting full-sample transfer table used above follows after fixed two-sample norm conversion.

For arbitrary nonnegative causal backward forcing \(J_3,J_2\), including current entries, the proposed supersolution reconstructs \(B_3^*,R^*,W^*,B_2^*\) exactly. The identities

\[
W^*-W_b=a^2L_bJ_3R^*,
\]
\[
F_b(B_2^*-B_{2b})F_b
=F_bJ_2F_b+a^2(F_bL_b)J_3(R^*F_b)
\]

have the correct orientations. The valid sandwich inequality is

\[
|UQV|_d\le S|U|_d|Q|_r|V|_d.
\]

Expanding its indices retains the final \(h_j\) from the strict right factor. This covers row errors concentrated at an arbitrarily small time step and arbitrary current diagonals.

The first term has density \(H^3M^{-6}q\); the second has density \(H^4M^2q\). Dividing by \(F_{kj}\ge H^{-2}M^{-8}h_j\) gives relative error at most \(H^7M^{10}q\). The positive expansion then sums geometrically. The \(VJ_3V\) relative error has order \(H^5M^6q\), and direct forward forcing has relative size at most \(H^2M^8q\). The beta margin is at least \(H^{-1}M^{-2}\), so \(q\le H^{-16}M^{-12}\) leaves strict forward slack.

Backward reconstruction costs \(H^4M^{10}q\le H^{-12}M^{-2}<r_a/2\). The inactive direct construction gives backward rows at most \(3q<r_i/2\), and forward-density increments \(H^3M^4q,H^5M^4q<1/2\). Positive beta derivatives give strict inner-to-outer forward margin \(H^{-3}M^{-10}h_j\) at every strict entry.

Signed deterministic arrays are dominated by the positive affine causal map at their entrywise absolute values. Since the coefficient system is chronologically constructed, this suffices for comparison; an unproved bound on a fully coupled inverse is not being assumed. First exit along the fixed-cap, fixed-mesh amplitude homotopy is impossible because the forcing estimate holds at the proposed exit and the supersolution is strictly interior there.

**Status: PASS.**

## 7. Numerical amplitude and original downstream conclusions

The exact scale relation gives \(M^{32}\le24^8\delta^{-4}\), and \(24^8<H\). Hence the unchanged coefficient

\[
c_{\rm poly}=\min\{1/4,c_*,10^{-70}H^{-400}\}
\]

implies

\[
eM^{32}\le10^{-70}H^{-399},
\quad eH^{22}M^{19}\le10^{-70}H^{-377}<1,
\]
\[
qM^{12}\le H^{30}eM^{31}
\le10^{-70}H^{-369}<H^{-16}.
\]

The response and closure therefore require only 31 powers of \(M\), while the fourth power of delta supplies 32. The old \(c_*\) condition also holds, as checked above. There is no new data-dependent numerical coefficient selection.

The downstream use of the old bridges checks as follows.

* **Canonical actions and cap removal.** The fixed-cap maps have globally bounded first derivatives, so the generic conditioning and singular-query constructions apply. Finite unions of programs, initial operator bounds and exact finite transpose identities construct both actions and true adjoints on common generated L2 spaces. The actual cap-uniform incoming subGaussian fields supply the precise reference-tail premise of asymmetric comparison. Its error is \(C\exp(C(1+eR)S-cR^2)\to0\). Tails of a competing solution are not required.
* **Global physical flow, uniqueness and restart.** Label folding is an exact identity of the finite loss and raw algorithms. Deterministic population exchange symmetry is proved at the capped finite-program level. Every cap feature path and the uncut path start below one and end above one, so their first-hit clocks cover every finite physical time. The capped argument only needs a bounded prediction derivative, not monotonicity of a capped feature field. Physical comparison keeps both residuals and therefore handles nonsymmetric competitors. The same Gaussian-error estimate survives multiplication by a restart Gronwall factor from a reached state.
* **Finite GF and raw GD.** Fixed mesh/cap source laws identify actual residuals and update contractions. Exact rank-one unrolling and initialized operator bounds produce finite primal balls with slack; trained operator-norm convergence across widths is not assumed. Deterministic fixed-cap Euler estimates remove the auxiliary mesh. The uncut finite algorithms are compared with a same-width cap reference. GD contributes \(C_{R,T}n^{-2}\); it is not silently replaced by a different coordinate update. The initialized finite random readout is retained and tends to the zero population readout through fixed-program stability.
* **Velocities and path observables.** Appended velocity queries include their full sources, derivative responses and learned memories. Their unbounded products are smoothly truncated before the bounded-derivative conditioning theorem is used. The fixed-cap velocity proof gives the required laws and reference tails. For cap removal, the uncut population velocity is a continuous L2 path with compact time image; a finite L2 net gives uniform tail removal. Taking the cap limit at fixed velocity truncation, followed by that truncation limit, avoids any cap-dependent higher-moment growth assumption. The analogous ordered finite-width comparison gives uniform-time same-layer velocity laws and second moments. The bound \(\|x-I_hx\|_\infty^2\le4h\int|x'|^2\), together with integrated speed control and finite-grid joint laws, gives the stated W2 path topology.
* **Nonaffinity and initial motion.** The quantitative affine variance bounds are absolute, and the Hermite argument gives the explicit positive \(eta_*\). The square root of the arctangent regression residual is 1-Lipschitz in W2 because an optimal slope lies in \([0,1]\). Thus the old raw/preactivation comparison retains \(e^2\eta_*/4>0\) throughout the bounded feature interval and every finite physical time. The odd-family motion proof uses full forward support, nonconstant \(\phi'\) for every \(e>0\), actual transpose innovations with full second-moment covariance, adjunction, and exchange symmetry. It needs no further small amplitude. It proves each hidden block and each sample/layer acceleration and the projected kernel change with the original physical-time factors.

Every required bridge premise is supplied for the final fourth-power amplitude. No substituted model, exchanged uncontrolled limit, imposed competitor symmetry, discarded current return, or additional amplitude restriction was found.

**Full-theorem status: PASS.** The sufficient exponent is four with the original explicit prefactor. This verdict does not assert sharpness of either the exponent or that very small prefactor.

## 8. Final hash record

SHA-256 was recomputed from file bytes. Every listed digest matched its manifest. The candidate manifest has four entries; the dependency manifest has 23 entries. Dependency paths are relative to `studies/mean_field_peeling`.

Manifest digests:

| Manifest | SHA-256 |
|---|---|
| `CANDIDATE_HASHES.json` | `8439be694a44c71ad06986cdee28e55e20907fe682ead692ff9fe6747567d62d` |
| `DEPENDENCY_HASHES.json` | `1e6427032404b97eeff50bcdabf65350fa9d64680e92639e4c522d8c50464316` |

Candidate digests:

| File | SHA-256 |
|---|---|
| `PROOF.md` | `7e33899649b547e7dcac8a465f2d118518d9db9ef001a3d04d2b9da615aa9485` |
| `AFFINE_PROPAGATOR.md` | `88a1bfbaf6fd1fc6fcfea56b25a4490932663090eb01710e9d96ba04d26fe460` |
| `PRIMAL_L2_RESPONSE.md` | `cf313286d301aa9fe5fb121d0c1fa5351213efbeaa4c087656d205c3156e417a` |
| `SECTOR_SUPERSOLUTION.md` | `e1ce9401b58bcd20384e1b2932d725844fda6904e9c9d70ef4a4f1af0f9ab68d` |

Dependency digests:

| File | SHA-256 |
|---|---|
| `two_sample_odd_activation_theorem/PROOF.md` | `a4d6ed0ee99a1e111b5eba068f2219cf561a2281b1828b26227aca7a0a54a050` |
| `two_sample_odd_activation_theorem/AFFINE_CORE.md` | `634dd3bbc35436e9d1760bee5c11cbf2124b3c42e8920a1bf3a4fcbb15039711` |
| `two_sample_odd_activation_theorem/SOURCE_AND_LIMIT_BRIDGE.md` | `2a140f2a5a39f911b5c2ca51bc79102d20e9209f1450d38005360c88103f6e77` |
| `two_sample_odd_activation_theorem/INITIAL_MOTION_AND_NORMALIZATION.md` | `c96316fdc481ef3f9e6fc402514ca9b45bcff12e199023505fbbb86d4e15bf24` |
| `two_sample_odd_activation_theorem/sources/ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md` | `27b2579f27ec14319dd39a93a4942d7b6463860648462d5ccb31b662c7725b75` |
| `two_sample_odd_activation_theorem/sources/CONTRACT.md` | `e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd` |
| `two_sample_odd_activation_theorem/sources/FIXED_CAP_VELOCITY_BRIDGE.md` | `a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0` |
| `two_sample_odd_activation_theorem/sources/INITIAL_FEATURE_LEARNING.md` | `bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351` |
| `two_sample_odd_activation_theorem/sources/L3_LOCAL_COMPLETE_PROOF.md` | `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4` |
| `two_sample_odd_activation_theorem/sources/NONLINEAR_RESPONSE_PERTURBATION.md` | `ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568` |
| `two_sample_odd_activation_theorem/sources/PREVIOUS_TWO_SAMPLE_PROOF.md` | `2891b892667396d64bd747689bcd59aa7ca3ffd224d3579fc3407bca0b623f9a` |
| `two_sample_odd_activation_theorem/sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md` | `99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066` |
| `two_sample_odd_activation_theorem/sources/SYMMETRY_RADIAL_CLOCK.md` | `40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4` |
| `two_sample_odd_activation_theorem/sources/THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA.md` | `49da0f68047b4f516d3ad3c94b7112259838bcebf68e2296a948364232842789` |
| `two_sample_odd_activation_theorem/sources/TWO_SAMPLE_SOURCE_BASELINE.md` | `a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f` |
| `two_sample_odd_activation_quantitative/PROOF.md` | `0a7dbd32cb9cc291e706813b59c0142394e6f9532244e52c21a5ab5d89ed4d02` |
| `two_sample_odd_activation_quantitative/AFFINE_POLYNOMIAL_BOUNDS.md` | `8387e2f253063c139dacb282ca9f2372478521f54b33a9ef6c8dbd83f2b521ca` |
| `two_sample_odd_activation_quantitative/POLYNOMIAL_RESPONSE_LEMMA.md` | `51b0f717b33ed618219e086d32b16a95ef4253892171597d1805dd9d37a64f7f` |
| `two_sample_odd_activation_quantitative/OLD_THRESHOLD_AND_NONAFFINITY.md` | `c63753a83e832793c886b8ae8c122e30e0c01864b86a1a5dc9bee030852f9210` |
| `two_sample_odd_activation_power10/PROOF.md` | `37b9e8a27135b95b8dffe05fe2b734229fadedc98bc1609259e365dbb2aeba37` |
| `two_sample_odd_activation_power10/AFFINE_SOURCE_CERTIFICATE.md` | `bc55c0f8e25de1f3a4316fe36e86afa25c9486e014192f2eb818358909b048eb` |
| `two_sample_odd_activation_power10/REFINED_RESPONSE.md` | `3622a0f903cd51b712d1d524a140d834471b5eb588611f059535c41f6efd2332` |
| `two_sample_odd_activation_power10/POSITIVE_SUPERSOLUTION.md` | `e2be183521919ce69c7ae41b81f5cd78566c5430a78c2408687f52f1b6d86774` |

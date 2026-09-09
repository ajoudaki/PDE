# Independent hostile audit: prescribed moderate-sine local source theorem

2026-09-08.

**Verdict: PASS for the local theorem and local joint GF/raw-GD scope. No blocking repair found. This is not acceptance of a global theorem.**

Candidate read in full: `/tmp/sine_source_route.md`, SHA-256
`4bfa60f57e8a226ed73ae85c225f28a17562f26b1aa498351e3617069c94be1e`.
No source file was edited. No experiment or numerical approximation was used.

## 1. Accepted statement and proof dependencies actually checked

For the precise moderate activation in the user's request, with its coefficient unchanged, there is the explicit positive feature interval `[0,S0]` from equation (10). On that interval all capped finite source programs have cap- and mesh-independent Gaussian incoming-field tails. Consequently the canonical uncut population flow exists strongly and uniquely on that interval. The symmetric physical clock covers `[0,S0/3]`, on which the original actual finite GF and raw GD with step `n^-2` have the asserted joint limits, including the original finite readout, both matrix orientations, raw kernels, hidden fields/velocities, second moments, and path-space statements supplied by the cited bridges.

This accepts neither a continuation theorem past the constructed interval nor arbitrary reached-state local existence. The activation has not been made smaller to obtain the interval; the short time itself supplies the small quantity.

Mathematical sources inspected for this audit:

- `two_sample_odd_activation_theorem/sources/NONLINEAR_RESPONSE_PERTURBATION.md`: exact source equations (6)--(10), norm conventions, the full formal derivative recursions (24), (26)--(29), the current-coordinate-factor discussion, and stage dependency discussion;
- `two_sample_odd_activation_theorem/sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md`: complete file, distinguishing its generic conditional cap/physical/finite-algorithm bridges from its separate near-affine hypotheses;
- `two_sample_odd_activation_theorem/sources/FIXED_CAP_VELOCITY_BRIDGE.md`: all operative assumptions and Sections 2--8, including the appended-product truncations, both current returns, the actual physical feedback, and finite Euler node conventions;
- the finite-program/common-action source and bounded-derivative hypotheses already read directly in `two_sample_separated_angle_theorem/sources/L3_LOCAL_COMPLETE_PROOF.md`;
- the exact model and metric in `two_sample_activation_design/PROOF.md`, Section 1;
- the symmetry/strong path chain-rule argument in `two_sample_odd_activation_theorem/sources/SYMMETRY_RADIAL_CLOCK.md`.

No old review verdict, root conclusion, or sibling-agent verdict was used as a mathematical premise.

## 2. Raw model, activation, caps, and the primal interval

Writing Phi(z)=alpha z+beta sin(2z) exactly preserves the user coefficient. The lower derivative is

`alpha-2 beta = [1/5-(4/5)exp(-2)]/s0 > 0`.

The crude bounds `|Phi(z)|<=2|z|`, `|Phi'|<=2`, `|Phi''|<=2` all hold. The partial cap

`D_R(z,q)=alpha q+2 beta cos(2z) tau_R(q)`

obeys `|D_R|<=2|q|`, `|D_q|<=2`, `|D_z|<=2|q|`, and has globally bounded continuous first derivatives for each fixed cap. The affine part is not capped; this causes no loss in either its q-Lipschitz bound or the stated source recursion.

On the B=20 primal ball, the six forward/backward induction bounds (3) are valid in either population L2 or finite normalized norm. Each raw block update has norm at most `L^3 B^3`: the first raw block uses `sum|c_a| ||x_a||/sqrt(d)=1`; each middle block uses the product of its two factor norms; the readout uses `sum|c_a|=1`. For the two bottom projections, the maximum absolute sample row sum of `P=Gamma diag(c)` is at most one. Thus summing increments under (4) supplies strict primal slack independent of cap and mesh. No local Lipschitz constant of an uncut field is smuggled into this step.

The finite initialized readout is retained. Its zero population limit is taken only within the fixed-program limit, where the fixed-cap same-initialization Lipschitz comparison makes this legitimate.

I checked the size D in (6), not only its positivity. The largest raw backward norm before adding sample maxima is bounded by `L^6 B^5 S` (the bottom delta); source-pair Gaussian Lp norms acquire at most the stated fixed pair factor. With L=2, `D=2^10 B^5` dominates these, all forward sources, both root projections, and the learned-moment input norms. Correlations and singular covariance cases do not affect marginal Gaussian moment bounds.

## 3. Norm conventions and moment induction

The norm used is essential:

`|T|=max_a sum_b |T_ab|`, and `|T_kbullet|_r=sum_j |T_kj|`.

The second expression is not replaced by `max_a sum_(j,b) |T_ka,jb|`. The derivative recurrences in the source dependency hold in the former stronger time-block norm by submultiplicativity and by padding unavailable source blocks with zeros. All the candidate's moment and envelope estimates remain valid in that stronger norm. Pair-valued random variables use `|| |X|_infinity ||_p`, so the pair maximum has already been accounted for in D and in (12).

The three inequalities in Section 3.1 follow directly from the exact scalar source equations. For example,

`||q2_r||p <= D S sqrt(p)+M3 S max_(v<=r)||H2_v||p`,

and then

`||Z2_k||p <= D sqrt(p)+A2 L sum_(r<k) h_r ||q2_r||p`.

These yield exactly the displayed middle forcing `A2 L D S^2` and feedback coefficient `A2 L^2 M3 S`. No random supremum over Gaussian time is used. The root and top formulas are similarly correct; the top double Volterra sum is bounded by S times the remaining single sum.

Under (10), every exponential and forcing factor in these three moment recurrences is much smaller than the slack allowed by `10D`. The current input bounds (12) are then

`C <=20D S sqrt(p)`,
`q2 <=[D+20D M3]S sqrt(p)<=21D M3 S sqrt(p)`,
`q1 <=21D M2 S sqrt(p)`.

These are applicable on incomplete prefixes exactly when the fields in question have already been constructed. In particular they are not used to bound a current b3 row through a not-yet-constructed current q2.

## 4. Explicit reconstruction of the random envelope

With fixed coefficient arrays, let J denote the source-to-preactivation derivative. The exact recursions give the following coefficient bounds for positive Volterra majorants:

- Bottom transpose source: forcing `L h_j`; coefficient `2|q1_r|+L^2 M2 S`.
- Middle transpose source: forcing `A2 L h_j`; coefficient `2 A2 |q2_r|+A2 L^2 M3 S`.
- Middle full forward-source row: forcing one; the same middle coefficient.
- Top full forward-source row: forcing one; coefficient `2 A3 |C_r|+A3 L^2 S`.
- Top readout row: at most `L S` times the increasing top preactivation envelope.

Since `A=A3=M2 >= A2=M3 >=1`, each of their integrated coefficients is dominated by

`8 A^2 S^2+2 A sum_(r<k) h_r |Q_r|_infinity`.

Thus (14) is a valid common envelope in the appropriate layer probability space. The transpose single-source factor h_j is introduced once, at its actual source time. There is no hidden full-time forcing term and no sum proportional to the number of source columns.

For all three Q groups one may take `K=21 D A S` in `||Q||p<=K sqrt(p)`. The moment-to-MGF calculation in the candidate is valid, using `m! >= (m/e)^m`. Jensen with total weight S, including a leftover zero term if the prefix ends before S, gives

`E E_k^4 <=2 exp[32 A^2 S^2+e (168 D A^2 S^2)^2]`.

The final restriction in (10) gives `D A^2 S^2<=1/10000`. Hence this last exponent is safely smaller than `log(8)`, indeed much smaller than one, and the conclusion `||E_k||4<2` is valid. This bound is independent of cap, mesh, all temporal correlations, and singular covariance rank.

## 5. Current multiplier, current blocks, and literal closure

The candidate correctly retains the current curvature terms. In the top output,

`sum_j |partial_(xi3_j) delta3_k| <=2 |C_k| E_k+L^2 S E_k`.

After expectation and Cauchy--Schwarz this is at most

`4 ||C_k||2+2 L^2 S =2N ||C_k||2+2 L^2 S`,

because N=2. Thus (16), including its constants, is valid. No current |C_k| factor is incorrectly absorbed into the past-time exponential.

Similarly the middle output row is bounded by

`2 |q2_k|_infinity E_k+L^2 M3 S E_k`,

giving (17). The current return through b3 is included. The exact current blocks (18) follow from the causal source equations: C_k has no current xi3 derivative; the current Z2 derivative in xi2 is the identity; differentiating q2's current return gives the second term in b2. There is no current algebraic inverse and no omitted same-time transpose term.

The four-stage order is valid:

1. a2 at k uses bottom derivatives depending only on past b2.
2. a3 at k uses current a2 and past b3.
3. b3 at k uses the now available a3 and past top fields; only after it is bounded is q2_k constructed.
4. b2 at k uses this q2_k and current b3; only after it is bounded is q1_k constructed.

The raw learned moments are independent inputs to this closure: forward density at most D^2 and backward row at most `D^2 S^3`. I checked the strict numerical inequalities. For example the b2 coefficient is at most

`(84 sqrt(2) D M3+8 M3+D^2 S^2)S`,

which is smaller than `(M2/2)S=50 D^2 M3 S` already for D>=100. The b3, a2 and a3 inequalities have larger slack. Initialization gives empty a rows and vanishing b rows, including their current entries, even for singular Gaussian covariance. This closes the full induction rather than a circular simultaneous-current-row bootstrap.

## 6. Strong local population construction and physical-time conversion

The established Lp bounds imply Gaussian L2 tails of C, q2 and q1 uniformly in cap and mesh. Their coefficient-size constants are large but finite and depend on no width. The reference-only cap comparison has a single linear cap factor: at each backward step the new cap multiplies a forward-state difference, while the preceding backward error is multiplied only by a bounded gate slope and action norm. Consequently the cost is `C exp(C R-c R^2)` on this fixed interval. This makes raw states and raw directions Cauchy and constructs the strong uncut feature flow. The same reference comparison supplies uniqueness against bounded-primal strong competitors and restart uniqueness within the already constructed interval.

The feature-path sample symmetry does not require exact symmetry of a finite realization. It follows from equivariance and the deterministic population limit. The pointwise raw bound gives

`|g_R(s)|<= ||C_R(s)||2 max_a ||h3_R,a(s)||2 <= L^6 B^6 S<=1/4`.

Thus the population scalar physical clock has speed between 3/2 and 5/2, so its image covers at least `[0,2S0/5]`; the candidate's `[0,S0/3]` is safely contained. This applies also to fixed-cap references. No fitting theorem or positive global kernel floor is needed for this local clock.

The actual finite physical algorithms cannot use that scalar clock and the candidate does not do so. The cited bridge keeps both finite residuals throughout and compares to the population-clock-defined physical reference on the covered interval.

## 7. Full local GF/GD and velocity scope

The cited fixed-cap velocity bridge uses only the following scalar conditions: linear growth of the activation, bounded continuous first and second derivatives, linear growth and bounded continuous first derivatives of the fixed-cap backward instruction. The prescribed Phi and D_R satisfy all of them. Its other hypotheses are the bounded common-action initialization, the fixed-program theorem with genuine adjoints and finite moment roots, and an existing bounded fixed-cap physical reference. The construction above supplies the last hypothesis on `[0,S0/3]`.

I checked that the bridge does not apply the fixed-program theorem directly to an unbounded-derivative product `Phi'(z)P`. It first truncates P, appends the two forward velocity actions in order, controls their expected source derivatives, and removes nested truncations in the specified order. Only Phi'' enters these derivatives; no unverified third-derivative or higher-moment operator bound is required.

At fixed cap, raw Euler error is controlled on a larger common primal ball with width-independent constants. Fixed-mesh finite-program convergence is taken before mesh removal. The actual step `n^-2` is compared with the same-width fixed-cap flow. The uncut comparison then uses only reference tails and adds the fixed-cap `C_(R,T)n^-2` defect. It requires no width-independent Lipschitz estimate for the finite uncut field.

For uncut hidden velocities, the order is essential and is present in the bridge: obtain uniform strong raw state and direction convergence first; truncate a fixed uncut reference preactivation velocity; let the training cap go to infinity at fixed velocity threshold; then remove the threshold using compactness of one continuous L2 time image. This avoids multiplying the cap-removal error by an uncontrolled cap-dependent fourth-moment constant.

The path-space W2 conclusion uses the explicit interpolation inequality

`||x-I_h x||infinity^2 <=4h integral |x'|^2`,

not merely finite-time marginal convergence. Kernels use converging same-layer L2 contractions; all original raw normalization factors and the right-node/terminal-left raw-GD direction conventions are retained. These arguments are valid on the local physical interval supplied above.

## 8. Exact current sine average and global boundary

The Section 5 conditional Gaussian identity is correct for k>=1 (and the initial current term is zero separately). C_k and the learned part of Z3_k depend only on strictly past top sources at frozen deterministic coefficients. Gaussian regression gives the displayed independent residual and the factor `exp(-2 sigma_k^2)`. The current conditional variance is at most the variance of the increment from the previous same-sample source. The exact covariance rule identifies that variance with the squared L2 increment of the lower feature. On the bounded raw prefix this is O(h^2). Thus importing the initialization factor `exp(-2)` as a uniform current-time damping factor would be invalid.

The local source gains depend explicitly on zero initial readout, O(S) backward fields and O(S) backward rows. Those are not available merely by changing the starting time to a positive reached time. The note correctly refuses to erase old source history or infer uncut Hilbert local existence from gradient continuity. No argument audited here proves that the old source-response rows remain bounded at every finite physical time.

## 9. Nonblocking presentation suggestions

It would aid a reader to restate explicitly in the source note that pair-valued Lp norms use the pointwise sample maximum, and to say `k>=1` next to the previous-source variance inequality (21). Both conventions are clear from the cited exact equations and the proof, so neither is a blocking mathematical repair. Equation (16)'s factor `2N` works because N=2; writing the actual factor 4 would make its origin in Cauchy--Schwarz more transparent. No constant or theorem restriction needs changing.

**Final acceptance:** the local theorem is supported at the specified candidate hash. The requested all-finite-physical-time strong population/GF/GD theorem remains open.

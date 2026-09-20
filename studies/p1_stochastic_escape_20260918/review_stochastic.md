# Independent internal mathematical review

Date: 2026-09-19. Reviewer: isolated agent `/root/review_stochastic`.

**Verdict: PASS for the precise finite-step, ambient-state claims of the frozen candidate.** Equations (1)–(11), the bounded Hilbert Hessian, cubic descent construction, and exact representability are correct. No required correction or unresolved correctness objection was found. This is an internal mathematical check, not a promotion review, a convergence theorem, or a claim about canonical-initialization reachability.

## Assignment, isolation, and complete input coverage

The neutral assignment was to audit canonical physical p=1 consistency; the four-input ambient equilibrium; the actual positive-semidefinite Hilbert Hessian; cubic descent; exact minibatch covariance; first-step loss increase and guaranteed second-step hidden block motion for batch size three; and exact representability. The only scientific inputs were:

| Input | Complete coverage | SHA-256 |
|---|---|---|
| `docs/observable_p1.md` | All 332 lines, including initialized carriers, normalization, odd-sector folding, finite equations, metric, and stated numerical/limit restrictions | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` |
| `docs/NOTATION.md` | All 98 lines | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `studies/p1_stochastic_escape_20260918/four_input_noise_geometry.md` | All 234 lines, all five sections and every displayed equation | `e60c500587923ec3cab3c9ad9353935dce5d7abc7c3971bb3ec19d5567656e01` |

The initial aggregate tool output was truncated. It was repaired by reading `observable_p1.md` in complete line ranges 1–180 and 181–360 and rereading the complete notation contract and candidate. No scientific content remained unread.

Required process inputs read: supplied root instructions, `RESEARCH_WORKFLOW.md`, `solve-math-rigorously/SKILL.md`, `investigate-conjectures/SKILL.md`, and its `references/adversarial-audit.md`. No author README, study history, other studies, previous reviews, external scientific source, or other reviewer's findings was read. Git status was inspected only as coordination metadata. The checkout HEAD at the initial check was `019e3630237e33f58b9636c0aa67a039bebf0182`; the index had no staged paths. Concurrent unrelated modifications were left untouched.

Methods: complete source reading and independent analytic rederivation, including constants, signs, population types, Taylor orders, and Hilbert differentiability. Commands used for evidence were `wc -l`, `sha256sum`, complete `cat`/`sed` reads, and read-only Git metadata checks. No simulation, numerical experiment, code audit, external retrieval, staging, or commit was performed. The established initialized carrier identities are the canonical input contract here; their separately referenced global source-rule proof is outside this assigned review.

## 1. Canonical model, metric, and data

The candidate uses dimension three, two tanh hidden layers, the canonical correlated lower marks and independent upper population, exact expectations, and the canonical nonconstant odd-sector representation. The matrix is the full arbitrary 3-by-6 trainable matrix in that sector, and its actual transpose appears in reverse propagation. No diagonal, rank-one, or fixed-feature restriction is imposed on the dynamics: rank one is the selected ambient state only.

The Hilbert state space is the odd subspace of

\[
L^2(\Omega_1;\mathbb R^3)\oplus L^2(\Omega_2)\oplus
\mathbb R^{3\times6},
\]

with population pairings in the first two blocks and the Frobenius pairing in the last. The affine coordinate `w-g` has the same differential as `w`. The constructed bounded `w` is admissible because the canonical Gaussian `g` is square-integrable. All proposed readouts and perturbations are odd and square-integrable. Omitting constant feature coordinates is justified by the established odd invariant sector, not by modifying the carriers.

For `u_i=x_i/sqrt(3)`, direct differentiation gives

\[
Df_i[h,k,N]=E_2[kH_i]+d_i^TNa_i+
 E_1[\phi'(w\cdot u_i)(b_1^TM^Td_i)(h\cdot u_i)].
\]

Its Riesz representatives give (2), with the factor 2 belonging to the unhalved squared loss. The empirical batch mean in (3) is therefore the exact sample-loss Hilbert gradient, with a single batch shared across integrated population marks. It is neither neuron resampling nor a numerical Heun step.

Every normalized input has norm one and positive first coordinate C. Distinct inputs can therefore be neither parallel nor antipodal. Their rank is three: pair differences span the second and third coordinates, while pair sums span the first. The relation `u_1+u_2=u_3+u_4` verifies both singularity of the four-input Gram and

\[
\sum_i y_i=0,\qquad \sum_i y_i u_i=0.
\]

No excluded positive-definite-Gram assumption has been introduced.

## 2. Equilibrium and actual Hilbert Hessian

Write `B_1=q^Tb_1`. It is a positive multiple of `tanh(G_1)`, so `B_1 e=|B_1|` almost surely and `kappa=E_1|B_1|>0`. At (4), oddness gives

\[
\phi(w_*\cdot u_i)=e\phi(aC),\quad
a_i=\phi(aC)A=:a_*,\quad M_*a_*=z e_1.
\]

Thus all upper features are the same nonzero `H`, all predictions and backward vectors are zero, and only the readout component of each individual loss gradient can be nonzero. Its full-batch average is zero by label balance. The loss is exactly one.

For an arbitrary Hilbert variation `(h,k,N)`, boundedness of the lower marks and `phi''` gives the uniform finite-moment remainder

\[
\left|E_1[b_1\{\phi(w_*\cdot u_i+h\cdot u_i)
-\phi(w_*\cdot u_i)-\phi'(aC)(h\cdot u_i)\}]\right|
\le C_i\|h\|_2^2.
\]

Consequently `v_i` has the stated bounded first derivative. Composition with bounded upper marks yields an L2-valued differentiable map `H_i`, with derivative

\[
DH_i[h,N]=\phi'(zb_{2,1})\,b_2^T
\{Na_*+M_*\phi'(aC)E_1[b_1(h\cdot u_i)]\}.
\]

This does not assume that the unrestricted lower Nemytskii operator is twice Frechet differentiable on L2. At `c_*=0`, the lower gradient's finite coefficient vanishes. The lower gate changes by `O(||h||_2)` in L2, while its finite coefficient changes by `O(||(h,k,N)||)`. Their product has a quadratic remainder. The other gradient blocks are finite moments or smooth upper compositions. Hence the loss gradient has a bounded Frechet derivative at this point: an actual bounded Hilbert Hessian exists.

For a straight-line variation, set `ell=E_2[kH]`. Then `f_i'=ell` and

\[
f_i''=2E_2[k\phi'(zb_{2,1})b_2^T\delta v_i].
\]

The weighted sum `sum_i y_i delta v_i` is zero because its constant part is multiplied by `sum_i y_i`, and its input-linear part by `sum_i y_i u_i`. Therefore

\[
D^2L[(h,k,N)]^2
=\tfrac14\sum_i(2\ell^2-2y_i f_i'')=2\ell^2.
\]

By polarization, the Hessian is exactly `2 U tensor U`, where `U=(0,H,0)`. It is nonzero, rank one, and positive semidefinite; its sole positive eigenvalue is `2||H||_2^2`. This confirms (5) without substituting a directional Hessian for a Frechet Hessian.

## 3. Cubic descending curve

The upper scalar mark has positive density on an open interval containing zero. If `J=beta H` almost surely, continuity makes `t phi'(zt)=beta phi(zt)` on that interval. The linear Taylor coefficient forces `beta=1/z`; the cubic coefficients would then require `-z^2=-z^2/3`, impossible for `z>0`. Thus the orthogonal projection remainder `k` is bounded, odd, nonzero, and satisfies

\[
E_2[kH]=0,\qquad E_2[kJ]=\|k\|_2^2>0.
\]

The function `psi=tanh(G_2)^2-E[tanh(G_2)^2]` is bounded, even, centered, and nonconstant. Its variance is positive. For `h=e psi e_2`, the pair-1 entries in `E_1[b_1h^T]` vanish by centering of `psi`; the other coordinate-pair entries vanish by independence and `E[e]=0`. Hence every first effective-vector derivative is zero. Since `M_*` selects `B_1`, and `phi''(eaC)=e phi''(aC)`,

\[
v_i''(0)=e_1E_1[B_1e\psi^2]\phi''(aC)u_{i,2}^2
=\kappa\phi''(aC)E[\psi^2]u_{i,2}^2e_1.
\]

For `c(t)=tk`, differentiating `f_i(t)=t E_2[kH_i(t)]` gives `f_i'(0)=f_i''(0)=0` and

\[
f_i'''(0)=3\kappa\phi''(aC)E[\psi^2]u_{i,2}^2\|k\|_2^2.
\]

There is no missing factorial: the factor 3 comes from differentiating the explicit readout factor `t`. Using `sum_i(y_i/4)u_{i,2}^2=S^2/2` gives (6). Because `aC>0`, `phi''(aC)<0`; the displayed derivative is positive. Replacing `k` by `-k` makes the leading cubic term negative. Along this bounded curve, bounded tanh derivatives justify expectation differentiation and an ordinary third-order Taylor remainder. Thus arbitrarily nearby lower-loss states exist. No global C3 assertion on the Hilbert state space is needed or established.

## 4. Exact noise and the first two steps

At the equilibrium, (7) follows directly from `c=0`. A sampled label is an unbiased Rademacher variable, so the covariance of a batch mean of B independent draws is `(4/B) U tensor U`, proving (8). Equivalently, this covariance equals `(2/B)` times the Hessian operator. Its range is the positive quadratic readout direction. Since `E_2[kH]=0`, its projection onto `(h,-k,0)` vanishes exactly in the physical Hilbert metric.

The first update leaves both hidden blocks unchanged and gives `c^+=2 eta bar_y H`. Every prediction becomes the common number `f^+=2 eta bar_y ||H||_2^2`. Label balance gives

\[
L(\theta^+)=1+(f^+)^2
=1+4\eta^2\bar y^2\|H\|_2^4.
\]

For B=3 there is no zero label average, so the movement and loss increase are pathwise strict. For arbitrary positive integer B, `E[bar_y^2]=1/B`, giving the expected-loss statement. For even B, a balanced first batch can leave the state unchanged; the candidate correctly limits its pathwise guarantee to B=3.

At the new state, independence and centeredness of upper coordinates 2 and 3 give (10). Its first-coordinate coefficient `nu` is finite and strictly positive because its integrand is positive away from the zero-probability event `b_{2,1}=0`.

For the second batch define

\[
R'=B^{-1}\sum_j(f^+-y_{I_j'})u_{I_j'}.
\]

Then the complete simultaneous hidden-block increments are

\[
\Delta M=-2\eta(f^+-\bar y')d^+a_*^T,
\qquad
\Delta w=-4\eta^2\bar y\nu\phi'(aC)B_1R'.
\]

For B=3 and `0<eta<1/(6||H||_2^2)`, the strict inequality `|f^+|<1/3` holds for every first batch, whereas `|bar_y'|>=1/3` for every second batch. Thus `f^+-bar_y'` is nonzero. The factors `d^+` and `a_*` are nonzero, and `R'_1=C(f^+-bar_y')` is nonzero. Consequently both hidden increments are nonzero. The readout increment in the second step is also `-2 eta(f^+-bar_y')H`, hence nonzero.

The guarantee is pathwise for all ordered first and second batches; it does not depend on a favorable random draw. The strict step bound matters: its endpoint could permit equality and is correctly excluded. Since the data span R3 and tanh is injective, nonzero `Delta w=B_1` times a nonzero vector also changes a lower hidden activation on at least one training input on a set of positive population measure. The candidate's stated two-step conclusion is motion of the two hidden trainable blocks, not a separate quantitative theorem for both upper and lower activation laws after their simultaneous update.

## 5. Exact representability and scope

The suggested `r` produces four positive arguments `Cr_1+S`, `Cr_1-S`, `Cr_1+2S`, and `Cr_1-2S`. They are distinct because S is positive, and their positivity follows from `Cr_1>2S`. Their slopes `z_i=kappa tanh(t_i)` are therefore distinct and positive.

A linear relation among `tanh(z_i b_{2,1})` vanishes as an analytic function on the upper mark's interval. Its coefficients at powers 1, 3, 5, and 7 yield

\[
\sum_i\lambda_i z_i(z_i^2)^j=0,\qquad j=0,1,2,3.
\]

All four tanh Taylor coefficients used are nonzero. The Vandermonde determinant in the distinct `z_i^2` is nonzero, as are all `z_i`; therefore all `lambda_i` vanish. The Gram K is strictly positive definite, and the stated bounded odd readout gives `f_j=(K K^{-1}y)_j=y_j`. No linear-input separability is needed for this nonlinear exact fit.

The construction retains the canonical carriers and physical gradient metric, but selects an ambient state different from canonical initialization. The following stronger claims remain outside its scope and are not justified by it: reachability of the equilibrium from `(0,0,D)`; a one-sided basin of attraction; stochastic eventual fitting; long-time stability or convergence of fixed-step SGD; finite-width neural identification; and accuracy or convergence of the p=1 closure. No proof in the candidate silently depends on any of these bridges.

## Completion record

All assigned scientific lines and proof bodies were read. All candidate equations and central scope statements were checked analytically. A final SHA-256 check reproduced all three input hashes above unchanged. The exact candidate passes the internal check with no required changes. This report writes only the assigned study-owned output; source inputs and unrelated files are untouched. No promotion authorization or promotion-level review is implied.

---

# Separate supplement: local constant-step minibatch fitting

Date: 2026-09-19. Reviewer: the same isolated agent `/root/review_stochastic`, under a separate neutral supplementary assignment. The original frozen review above is preserved unchanged.

**Supplement verdict: PASS for the stated local theorem.** Every compatible finite sphere dataset in the stated dimension range has the explicit finite-norm interpolant constructed here. For every confidence parameter, the displayed radius gives an open local region from which actual fixed-step iid minibatch SGD, for any fixed positive batch size, converges to a finite zero-loss state with the claimed probability and conditional geometric expected-loss bound. No required correction was found. The theorem does not establish canonical entry or global convergence.

## Supplementary input and isolation record

The complete new scientific input was `studies/p1_stochastic_escape_20260918/local_minibatch_fitting.md`, all 251 lines, all five sections, every displayed equation, and the complete killed-process and path-length arguments. SHA-256:

`28ec016758d0cbfbf3316652b00ac2b6e70f504ba5075537ac2a8ce219daebd6`.

The complete established sources previously read remain `docs/observable_p1.md` and `docs/NOTATION.md`; their hashes were rechecked and remain exactly those recorded above. No other route output, author history, study README, external scientific source, or other review report was supplied or read. The original four-input candidate was already known from the preceding assigned review, but is not a dependency of this supplementary theorem or its verification. This is a new-input supplement by the same reviewer, not a claim of a second fresh reviewer.

Actual checks: complete `cat` read of the 251-line candidate, `wc -l`, source `sha256sum`, unchanged HEAD and empty-index metadata, and independent analytic derivations below. No experiments, numerical approximations, or external theorem retrieval were needed. Only this assigned report was edited, by appending the supplement.

## A. Merging inputs and constructing an exact fit

For every admissible state, odd tanh and bias-free composition give `a(-u)=-a(u)`, `H(-u)=-H(u)`, and `f(-u)=-f(u)`. Thus a compatible antipodal observation has exactly the same scalar loss function as its representative. Their gradients agree as derivatives of identical functions. Duplicates also have identical loss functions. Mapping each iid original draw to its equivalence class gives iid merged draws with the summed probabilities, so the entire update-sequence law is preserved. No averaging of unequal labels or replacement of SGD by its mean occurs.

After merging, every vector in the hyperplane list (1) is nonzero. A finite union of proper hyperplanes is closed and has measure zero, so its complement is open and nonempty. Density of rational vectors ensures that the proposed enumeration eventually reaches a valid vector when equality tests are interpreted in exact arithmetic. This is a mathematical construction from the given data, not a finite-precision conditioning guarantee. It yields nonzero `t_i` with `t_i` unequal to both signs of `t_j`. Oddness and strict monotonicity of tanh then give nonzero `z_i` with distinct squares.

The same canonical normalized lower coordinate satisfies `kappa=E|q^Tb_1|>0`. The prescribed bounded odd `w_*=er` and finite rank-one `M_*` yield the claimed `a_i` and `z_i`. The full dynamics are still allowed to change every matrix entry.

For arbitrary sample count, the Taylor recursion is correct. Comparing coefficients of `t^(2n)` in `phi'=1-phi^2` gives

\[
(2n+1)b_n=\sum_{j+k=n-1}b_jb_k,\qquad n\ge1,
\]

with `b_0=1`, hence all coefficients are strictly positive by induction. Tanh is analytic near zero. The upper mark has positive density on an interval containing zero, so an almost-sure linear relation implies a continuous identity there and hence vanishing Taylor coefficients. Its first m odd coefficients give a Vandermonde system in the distinct numbers `z_i^2`, with additional invertible factors `z_i`. This works equally for positive and negative slopes; distinct magnitudes are the necessary property.

Thus K is positive definite for every finite merged dataset. The readout (2) is a finite linear combination of bounded odd functions, so it is bounded, square-integrable, and in the required invariant sector. It fits all representatives, hence all original observations. The displacement `er-g` is square-integrable. Arbitrary finite labels, including zero labels, cause no exception. Conditioning may be poor, but all stated exact quantities remain finite for each fixed dataset.

## B. Verification of every local constant

Canonical nonconstant marks are bounded, so both `B_l` are finite. On the unit ball, `||c||_2<=C` and `||M||_F<=R_M`; normalized inputs have norm one. Pointwise activation bounds give

\[
|a_i|\le B_1,\quad |d_i|\le B_2C,\quad
\|J_{i,w}\|_2\le B_1R_MB_2C,\quad
\|J_{i,c}\|_2\le1,\quad
\|J_{i,M}\|_F\le B_1B_2C.
\]

Squaring and summing these three block estimates proves exactly (3). The finite-moment map is Frechet differentiable on L2 because bounded `phi''` gives an integrated quadratic remainder. Upper composition and pairing with `c` preserve the displayed gradient formula. No problematic C2 assumption on an unrestricted lower L2 Nemytskii map is used.

For two states in the unit ball, write their Hilbert distance as `s`. The inequalities

\[
|a_i-a_i'|\le B_1s,\quad
|Ma_i-M'a_i'|\le B_1(1+R_M)s
\]

imply `||H_i-H_i'||_2<=hs`. Splitting the difference of `d_i` into the readout difference and upper-gate difference, using Cauchy–Schwarz and `|phi''|<=2`, gives

\[
|d_i-d_i'|\le
\{B_2+2B_2^2CB_1(1+R_M)\}s=Ds.
\]

The three lower-gradient terms are bounded respectively by `2B_1R_MB_2C s`, `B_1B_2C s`, and `B_1R_MD s`: these come from changing the lower gate, M, and d. The readout-gradient difference is at most `hs`. The matrix-gradient difference is at most `(B_1D+B_1B_2C)s`. Their sum is the displayed J, proving its claimed Lipschitz bound.

Integration on the segment from the interpolant gives `|f_i-y_i|<=G||theta-theta_*||`. Subtracting `2(f_i-y_i)J_i` between two unit-ball states therefore gives `2(G^2+GJ)s`, proving the sample-gradient bound `K_L` and the same bound for the weighted full gradient.

For the weighted feature map T, Cauchy–Schwarz gives `||T||<=1`, because `sum_i p_i||H_i||_2^2<=1`. The same reasoning bounds `||T-T_*||<=h||theta-theta_*||`. Therefore

\[
\|T^*T-T_*^*T_*\|\le2h\|\theta-\theta_*\|.
\]

The radius in (5) consequently preserves the Gram eigenvalue at least `lambda=lambda_*/2`. In the readout component, putting `v_i=sqrt(p_i)(f_i-y_i)` gives

\[
\|\nabla_cL\|_2^2=4\|Tv\|_2^2\ge4\lambda\|v\|^2
=4\lambda L.
\]

For every batch size, Jensen's inequality yields

\[
E\|\widehat g\|^2
\le E\|g_I\|^2
\le4G^2\sum_i p_i(f_i-y_i)^2=4G^2L.
\]

This proves both parts of (6) without any assertion that the minibatch direction is nondegenerate or that the matrices remain rank one. All constants are strictly positive where division occurs. Also `lambda_*<=1`, since the weighted Gram trace is at most one, and `G^2>=1`. Hence the asserted interval `q in [1/2,1)` follows from the step bound (in fact these bounds give `q>=3/4`).

## C. Stopping, killed loss, and finite path length

Use the filtration generated by batches through time k. On `k<tau`, every sample residual is at most `GR/2`, so every sample gradient has norm at most `G^2R`. Its batch average satisfies the same pathwise bound. Thus the next update has length at most `eta G^2R<=R/4`; both its endpoint and entire segment are within radius `3R/4`, where the required radius-R estimates apply. This includes an update which exits the smaller radius-R/2 ball.

Conditioning on the full past, the fresh batch has mean `nabla L`. Integrating the Lipschitz gradient along the admissible segment gives

\[
E[L_{k+1}\mid\mathcal F_k]
\le L_k-\eta\|\nabla L_k\|^2
 +\tfrac12K_L\eta^2 E[\|\widehat g_k\|^2\mid\mathcal F_k]
\le(1-4\eta\lambda+2K_L\eta^2G^2)L_k
\le qL_k
\]

on `k<tau`. This is (8), with the past filtration making the stopping interpretation explicit. It is not a conditional drift assertion given the future event of never exiting.

The killed-loss recurrence is valid even when a crossing update has large loss: nonnegativity gives

\[
E[V_{k+1}]
\le E[1_{\{\tau>k\}}L_{k+1}]
\le qE[V_k],
\]

and `V_0=L_0`. For travel before stopping, conditional Cauchy–Schwarz and then unconditional Cauchy–Schwarz give

\[
E[1_{\{k<\tau\}}\|\theta_{k+1}-\theta_k\|]
\le2\eta G E[\sqrt{V_k}]
\le2\eta G\sqrt{E[V_k]}.
\]

Summing the geometric series is justified by nonnegativity. Since `1-sqrt(q)=2 eta lambda/(1+sqrt(q))>=eta lambda`, the last constant in (9) is correct. The indexing includes the crossing step: if `tau=n<infinity`, the update at `k=n-1` is present.

The initial distance is less than R/4. Any exit therefore requires cumulative included travel at least R/4. Markov's inequality and `sqrt(L_0)<=G||theta_0-theta_*||` prove (10) with exactly the displayed factor 8. The open initial radius gives strict probability less than delta; no independence of the stopping event is assumed.

The stopped total length has finite expectation and is therefore finite almost surely. Also `sum_k E[V_k]<=L_0/(1-q)<infinity`; by nonnegativity, `sum_k V_k` is finite almost surely. On never exiting, these imply finite total length of the actual unmodified SGD path and `L_k->0`. The invariant odd Hilbert state space is complete and closed, so the path has a finite state limit. It stays within the closed radius-R/2 ball in the limit; continuity of the loss proves exact fitting there.

Finally, with `A={tau=infinity}`, one has `1_A L_k<=V_k` and `P(A)>1-delta`. Consequently

\[
E[L_k\mid A]
=\frac{E[1_A L_k]}{P(A)}
\le\frac{q^kL_0}{1-\delta},
\]

which is (11). Future conditioning creates no bias problem because the estimate uses this domination, not a reapplication of unbiased stochastic gradients under A. As usual, the path convergence statement on A excludes only the null exceptional sets from the two nonnegative-series arguments.

## Supplement completion and limits

The theorem is an exact local convergence statement for the actual iid population SGD recursion. Its success radius is independent of the selected fixed batch size and valid throughout the displayed step interval; its convergence factor depends on the step. It gives no unconditional post-exit loss bound and no deterministic guarantee of staying in the region. Every scientific claim is correctly limited to finite compatible sphere data, the prescribed canonical carrier model, the odd invariant sector, and a data-defined neighborhood of the explicitly constructed fit.

The following remain unproved and are not smuggled into this result: entry from canonical initialization; a global basin; a useful uniform condition number over datasets; convergence of neural finite-width training to these p=1 equations; and convergence of the p=1 approximation to a higher-order or exact network model. The supplement passes independently of those open bridges. No promotion review or approval is supplied by this check.

Final provenance check: all supplementary scientific input hashes were unchanged after the review. The first 168 lines, constituting the original report, retain their exact pre-supplement SHA-256 `b81c70bdf5fd8bb6fe5186f4700b0243bb549031154e89a10eefcc0471e47a91`, verified by hashing that prefix after the append.

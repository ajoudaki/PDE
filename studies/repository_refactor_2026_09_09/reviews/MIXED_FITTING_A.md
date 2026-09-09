# Isolated adversarial audit of proposed Sections 10–11

**Verdict: CLEAN. No required mathematical corrections found.**

The two supplied files support the stated finite-width gradient-flow result: global existence from every finite initialization; on the explicit event E, for n >= n_*, asymptotic interpolation at finite parameter limits with the displayed bounds; and, on E intersect E_S, a time-independent positive lower bound on each sample's first-gate squared mass. The constants, probabilities, continuation arguments, and weighted-residual inequalities check out. Fitting means convergence as physical time tends to infinity; the proof does not establish interpolation at a finite stopping time.

## Inputs, hashes, and complete read coverage

The only mathematical materials consulted were these two files. Locations below refer to their original, one-based line numbers.

| Input | SHA-256 | Complete coverage |
| --- | --- | --- |
| `/tmp/pde-mixed-fitting-audit.GVYPqDG0/PROOF.md` | `36a50c2aa599302db2b2942d0ddb21d5561488ac0eff5e4b34dd7e43e3717a78` | 19,240 bytes; 496 lines; read in consecutive chunks 1–170, 171–340, and 341–496, without truncation |
| `/tmp/pde-mixed-fitting-audit.GVYPqDG0/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` | 5,110 bytes; 98 lines; read in full, lines 1–98, without truncation |

No repository, studies, prior reviews, history, internet, skill documents, other agents, or subagents were consulted. No input edits, experiments, generators, builds, installs, or Git operations were performed. This report is the sole output file, created with apply_patch inside a genuinely new directory returned by mktemp.

Both input hashes were checked again after the report was written and matched the values above exactly.

The audit covers every mathematical assertion in PROOF.md, including the limitation and counterexample paragraphs. The entire notation contract was also checked; its population and GD conventions supply no additional theorem assumptions here. Ordinary finite-dimensional calculus, elementary probability, and smooth ODE existence and uniqueness are sufficient; the relevant hypotheses are verified below.

## 1. Model, raw scaling, metric, and global existence

**Locations:** PROOF 11–90, equations (10.1)–(10.5); NOTATION 8–42, 59–63, 70–88.

The stated input Gram is

\[
G=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},
\]

whose eigenvalues 1+rho and 1-rho are positive. Thus the two inputs are linearly independent and d >= 2. No orthogonality or whitening is assumed. Smoothness and the compact support of the first derivative make P finite; positivity on the interior makes A positive. Oddness and the zero value at the origin imply saturation at exactly +A and -A. The second activation satisfies all three asserted bounds, including its global Lipschitz constant M.

Direct differentiation of the raw predictor gives

\[
\nabla_{W^{(1)}}f_a=\frac{\delta_a^{(1)}x_a^T}{n\sqrt d},\qquad
\nabla_{W^{(2)}}f_a=\frac{\delta_a^{(2)}(h_a^{(1)})^T}{n},\qquad
\nabla_{W^{(3)}}f_a=\frac{h_a^{(2)}}n.
\]

The block mobilities are n, 1, n, as allowed by NOTATION 78–82 and specified concretely by (10.2). Equivalently, the squared metric norm of a parameter velocity is

\[
\|\dot W^{(1)}\|_F^2/n+\|\dot W^{(2)}\|_F^2+
\|\dot W^{(3)}\|^2/n.
\]

Multiplying the sum-loss Euclidean gradients by these mobilities gives precisely (10.2). The residual is absent from each delta, as required by NOTATION 31–40. The mean loss for two samples is half the sum loss, so its velocities are half as large and its physical traversal time doubles.

The mobility-weighted Jacobian Gram gives exactly all three blocks in (10.3). In particular, the first block has denominator n, and the second has two factors with denominator n. The displayed tensor/matrix Gram representations prove positivity even when rho is negative. Consequently r-dot = -2Kr and the energy identity has factor 4, exactly as in (10.4).

The vector field is smooth on the entire finite-dimensional parameter space. On its maximal existence interval the loss is nonnegative and nonincreasing. Integrating (10.4), then applying Cauchy–Schwarz separately to each velocity, proves all three bounds (10.5). If the maximal endpoint T were finite, these bounds would make all parameters Cauchy as t approaches T, with finite limits at fixed n. Smooth local existence at that finite state extends the solution past T. This proves global existence before any success-event or fitting assumption is used.

**Finding:** scaling, physical time, metric, kernel, energy, and unconditional finite-width continuation are correct.

## 2. Saturated rows and coercivity supplied by the middle block

**Locations:** PROOF 92–134, equations (10.6)–(10.8).

If both preactivations of a first row are outside the open interval (-R,R), both first derivatives vanish, including at the endpoints. Fixing that row is compatible with its equation for any evolution of the other parameters. Local uniqueness of the full system, or equivalently uniqueness relative to the reduced system with that row fixed, identifies this invariant evolution with the actual flow. Global existence extends the invariance for all time.

An equal-sign saturated row contributes A^2 times the outer product of (1,1); an opposite-sign row contributes the outer product of (1,-1), with its irrelevant simultaneous sign removed. Summing gives the matrix in (10.6), with eigenvalues 2A^2 N_s/n and 2A^2 N_o/n. Every other row contributes a positive semidefinite matrix.

For each second neuron, congruence gives D_i Q(t) D_i >= gamma D_i^2 >= gamma I, since each diagonal entry of D_i is at least one. Its weight in K^(2) is (W_i^(3))^2/n. Hence K^(2) >= gamma M_3^2 I without assuming any individual readout entry is nonzero. The resulting loss and residual inequalities have coefficients 4 gamma and 2 gamma, respectively. At zero residual the entire vector field vanishes, so constant continuation is valid.

**Finding:** no row is frozen by an additional optimizer rule, and the lower kernel bound is valid for the actual dynamics.

## 3. Centered balance and the noncircular bound on the weighted residual integral

**Locations:** PROOF 136–217, equations (10.9)–(10.13).

The defect is exactly

\[
D(z)=\varepsilon\left[\frac{z}{1+z^2}-\arctan z\right],\qquad
D'(z)=-\frac{2\varepsilon z^2}{(1+z^2)^2}.
\]

Its monotonicity and limits give the claimed supremum norm epsilon*pi/2. The bound on the middle-layer speed follows from

\[
\frac2n\sum_a|r_a|\,\|\delta_a^{(2)}\|\,\|h_a^{(1)}\|
\le 2\sqrt2 MA\,eM_3=CeM_3.
\]

For the centered balance, differentiating M_2^2 produces the factor (W^(2)-W^(2)(0))h_a^(1); differentiating M_3^2 produces h_a^(2). Subtraction gives exactly D(z_a^(2)) minus the displayed initial-matrix term. No derivative of a moving hidden feature belongs in these derivatives of parameter norms. The sign in (10.9) is correct.

The norm of the bracket, divided by sqrt(n), is at most

\[
\varepsilon\pi/2+MB_0A.
\]

Thus the absolute derivative of the centered difference is at most D_0 e M_3. Its initial value is -b_0^2, which explains the +b_0^2 on the left of (10.10). Integration, M_2 <= C S_w, and nonnegativity of b_0^2 give all three inequalities in (10.10). The initial operator norm suffices; no width-dependent initial Frobenius norm has been substituted.

The first predictor estimate in (10.11) follows by applying the operator norm of W^(2) to the two-column first-feature matrix and the readout norm to the resulting second features. Its prefactor is sqrt(2)MA = C/2. Replacing it by C in the second estimate is a harmless weakening.

An actual loss below 2 implies, for every later time,

\[
\|f(t)\|\ge\|y\|-\|r(t)\|\ge\sqrt2-e_0=\nu>0.
\]

When M_3 <= 1, (10.11) and

\[
B_0+1+\sqrt{D_0}\sqrt{S_w}
\le (B_0+1+\sqrt{D_0})(1+\sqrt{S_w})
\]

give M_3 >= c/(1+sqrt(S_w)). When M_3 >= 1, the same conclusion follows from c <= 1. The definition of c therefore handles both regimes, including their boundary.

The delicate clock step is valid directly in physical time:

\[
\begin{aligned}
\frac d{dt}\{e+2\gamma c F(S_w)\}
&\le -2\gamma eM_3^2+
        \frac{2\gamma c\,eM_3}{1+\sqrt{S_w}}\\
&=-2\gamma eM_3\left(M_3-
        \frac{c}{1+\sqrt{S_w}}\right)\le0.
\end{aligned}
\]

Here F'(x)=1/(1+sqrt(x)), including its right derivative at zero. No division by e, M_3, or S_w' occurs. If residual zero is reached, all quantities in this inequality continue constantly. Thus (10.12) also covers that case and does not require a strictly increasing clock.

The integral formula for F is correct. For u >= 0, the maximum of log(1+u)-u/2 is log(2)-1/2, so the stated upper bound log(2) is conservative and valid. It gives F(x) >= sqrt(x)-2log(2). Applying this to (10.12), using e >= 0, yields precisely S_b. The expression being squared is positive. It also bounds S_w(t_0), and monotonicity of S_w extends the bound to times before t_0.

The bounds U and the upper bound on M_3 now follow from (10.10), while the lower bound beta holds after the margin. Integration of e' <= -2 gamma beta^2 e yields both the loss exponent 4 gamma beta^2 and the residual-integral denominator 2 gamma beta^2 in (10.13).

There is no circular use of an already bounded readout or of fitting. Before the margin, (10.5) gives M_3(t) <= b_0+sqrt(t L_Sigma(0)); multiplying by e(t) <= sqrt(L_Sigma(0)) and integrating proves

\[
S_w(t_0)\le\sqrt{\mathcal L_\Sigma(0)}b_0t_0+
\tfrac23\mathcal L_\Sigma(0)t_0^{3/2}.
\]

**Finding:** the centered signs and initial term, both regimes of the readout lower bound, the zero-clock case, all factors, and the closure of the global bounds are correct.

## 4. Finite parameter endpoints

**Locations:** PROOF 218–227, equation (10.14).

The bounds on the first-layer backpropagation are

\[
\|\delta_a^{(1)}\|\le PMU\sqrt n\,M_3.
\]

Inserting these into (10.2), and using the two input norms sqrt(d), gives the first-layer speed bound 2sqrt(2)PMU e M_3 after division by sqrt(n). The other two bounds in (10.14) likewise follow with the displayed C. Consequently the normalized total first-layer length is at most 2sqrt(2)PMU S_b, the middle-layer length is at most C S_b, and the normalized readout length is at most CU times the residual integral in (10.13).

All are finite. At fixed n these are finite lengths in ordinary finite-dimensional parameter spaces, so each parameter converges to a finite limit. The predictor is continuous in these parameters, and the loss tends to zero. The limiting parameters therefore realize both labels exactly. This argument requires no compactness theorem in a growing-width or population space.

**Finding:** the proof establishes convergence of all raw parameter blocks, not just convergence of the loss.

## 5. Explicit Gaussian events and their dependence structure

**Locations:** PROOF 231–311, equations (10.15)–(10.19); NOTATION 70–76.

The three initial variances agree exactly with the stored-readout convention. The normalized first preactivation pairs are independent across rows and have covariance G. Its positive density on open corners proves p_s,p_o > 0. The definitions gamma=A^2 min(p_s,p_o), kappa=gamma/2 are therefore positive, and E_F implies gamma_n >= gamma.

For a Bernoulli count of parameter p, deviation below np/2 has probability at most 4(1-p)/(np). Applying this separately to the two counts gives (10.16); their mutual independence is unnecessary.

Conditional on the first weights, the second-preactivation rows are independent N(0,Q). On E_F, Q-gamma I is positive semidefinite, so the representation U+sqrt(gamma)xi is valid, including when that covariance is singular. Given U, the transformed coordinates are independent. For every real sample-direction vector v, conditional variance and the scalar independent-copy inequality give

\[
\mathbb E[(v^T\phi^{(2)}(Z))^2]
\ge\mathbb E[\operatorname{Var}(v^T\phi^{(2)}(Z)\mid U)]
\ge\gamma\|v\|^2.
\]

This justifies the second-moment matrix lower bound even though conditional means need not vanish. The independent-copy inequality is legitimate since the derivative lower bound implies |phi^(2)(s)-phi^(2)(t)| >= |s-t|, and all required moments are finite by the Lipschitz bound.

Each of the four empirical Gram entries has variance at most 3M^4 A^4/n. Summing gives expected squared Frobenius error at most 12M^4 A^4/n. Markov's inequality at squared threshold gamma^2/4, followed by the operator-norm bound by the Frobenius norm, gives 48M^4 A^4/(n gamma^2) exactly. This establishes (10.17) conditional on first weights in E_F.

For the operator norm event, the volume ratio is ((1+1/8)/(1/8))^n=9^n for each 1/4-net. Approximating both unit test vectors loses at most one half of the operator norm in total, so ||W^(2)(0)||_op > 8 forces a net bilinear form with absolute value > 4. Each has variance 1/n and tail at most 2 exp(-8n). The two-net union bound is therefore 2 exp(-(8-2log(9))n), with positive exponent coefficient.

For the readout, b_0^2=n^(-3) sum_i xi_i^2. The event b_0 > 2/n is sum_i xi_i^2 > 4n. The moment E exp(xi_i^2/4)=sqrt(2) gives exactly exp(-(1-log(2)/2)n), again with positive exponent coefficient.

The failure decomposition is E_F^c, the second-feature failure intersected with E_F, and the two norm failures. Integrating (10.17) only over E_F and using a union bound gives the displayed p_n. In particular, the proof never conditions the independent Gaussian rows on the overlapping operator-norm event. All constants are fixed as n grows, so p_n tends to zero. The max with zero is the correct truncation when a finite-width union bound exceeds one.

**Finding:** the event probabilities, all numerical factors, and all uses of conditional independence are justified.

## 6. Actual loss margin and uniform constants

**Locations:** PROOF 313–387, equations (10.20)–(10.23).

The normalized two-column input matrix has operator norm sqrt(1+|rho|) <= sqrt(2). This and (10.5) give the first feature-displacement estimate in (10.20). Expanding the second preactivation difference exactly as in lines 326–328 gives the second estimate. These estimates use unconditional energy bounds, with no prior fitting or S_w bound.

If L_Sigma(0) <= 4 and t <= tau <= 1/4, then sqrt(t L_Sigma(0)) <= 1. Thus the squared normalized second-feature displacement is bounded by

\[
8M^2t[A+P(B_0+1)]^2\le\kappa/4.
\]

The denominator 32 in tau is exactly sufficient. Initial smallest singular value at least sqrt(kappa) therefore remains at least sqrt(kappa)/2. Squaring gives K^(3)(t) >= kappa I/4, and the factor 4 in the energy identity gives L_Sigma(t) <= L_Sigma(0) exp(-kappa t).

The displayed initial predictor bound is conservative: the first inequality in (10.11), with M_2(0)=0 and b_0 <= 2/n, already gives ||f(0)|| <= CB_0/n, and hence certainly <= 2CB_0/n as used. There is no missing +b_0 term in the bound actually needed.

For n >= n_*, the stated denominator ensures both

\[
\|f(0)\|\le2-\sqrt2,\qquad
\|f(0)\|\le\sqrt2(e^{\kappa\tau/4}-1).
\]

Consequently e(0) <= 2 and e(0) <= sqrt(2) exp(kappa tau/4). Squaring and applying the short-time decay proves L_Sigma(tau) <= 2 exp(-kappa tau/2) < 2. This is an actual strict loss margin at a specified finite physical time, not merely a negative derivative at initialization. The readout throughout is the nonzero Gaussian initialization prescribed in (10.15).

For the uniform version, n >= n_* >= 2 gives b_0 <= 1. The unconditional pre-margin estimate then yields S_w(tau) <= 2tau+(8/3)tau^(3/2). The actual e(tau) is at most e_*, so the actual c is at least c_* > 0. Repeating the physical-time inequality with c_* gives exactly overline S, overline U, and beta_*. The bound on M_3^2 follows using b_0^2 <= 1. The two time integrals and exponential rates in (10.23) have the correct factors.

Every displayed uniform constant is finite and positive where asserted for fixed admissible activation and fixed rho in (-1,1). They may be extremely unfavorable; no quantitative usefulness or uniformity as rho approaches either endpoint is asserted. The uniform fitting and gate conclusions are used for n >= n_*; the explicit final width restriction in Section 11 is essential to their scope.

**Finding:** the initialization really supplies the required margin, and the uniform bounds do not assume their own conclusion.

## 7. Extra strip event, accumulated forcing, and permanent nonexit

**Locations:** PROOF 391–479, equations (11.1)–(11.4).

The first-coordinate equation (11.1) follows from multiplying the first weight equation by x_a/sqrt(d). Its diagonal Gram coefficient is one, and the off-diagonal coefficient is rho. The definition c_a=-2r_a gives the correct sign and factor; q_a^(1) contains no residual. Smooth compact support of the first derivative makes lambda_1 finite. It is strictly positive because that derivative is positive inside and zero outside, so it cannot be constant.

Before any strip or nonexit argument, the Section 10 bounds imply

\[
\|q_a^{(1)}\|/\sqrt n\le M\overline U M_3.
\]

For the nonnegative vector with coordinates sum_a |c_a q_(a,i)^(1)|, its Euclidean norm divided by sqrt(n) is at most 2sqrt(2)M overline U e M_3. The integral triangle inequality on [0,T] therefore bounds the RMS of the accumulated integrals by V_*. Taking T to infinity monotonically gives (11.2). In particular, each V_i is finite at fixed n. This proof does not use any first gate remaining open; it is the required noncircular input to nonexit.

The Gaussian residual z_b(0)-rho z_a(0) has variance 1-rho^2 and covariance zero with z_a(0). Joint Gaussianity implies independence, proving the exact product formula for p_strip. Both factors are strictly positive. For an initial strip row, |z_a(0)| <= R/2 and the residual magnitude at least 3R imply that the other coordinate is strictly exterior.

Up to a first exit from |z_a| < R and |z_b| > R, the b gate vanishes. Equation (11.1) then gives

\[
\dot z_b=\rho\dot z_a,\qquad
\dot z_a=(\phi^{(1)})'(z_a)c_aq_a^{(1)}.
\]

Thus z_b-rho z_a is constant on that interval. Because the first derivative vanishes at both endpoints and is lambda_1-Lipschitz,

\[
0\le(\phi^{(1)})'(z)\le\lambda_1(R-|z|)\quad (|z|<R).
\]

The distance d_a(t)=R-|z_a(t)| is absolutely continuous, including through zeros of z_a. Almost everywhere, d_a' >= -|z_a'| >= -lambda_1 |c_aq_a^(1)| d_a. The integrating factor gives

\[
d_a(t)\ge (R/2)\exp(-\lambda_1V_i)>0.
\]

The conserved residual also gives |z_b(t)| >= 3R-|rho|R > 2R. If the first exit time were finite, continuity would preserve both of these strict margins there, contradicting the definition of the exit. Global existence already proved in Section 10 rules out loss of the solution as an alternative endpoint. The estimates therefore hold for all finite times, and also pass to the parameter limits by continuity.

For V_i <= B_*, the first margin is at least delta_*=(R/2)exp(-lambda_1B_*). Since p_strip > 0 and V_* is finite, B_* is finite and delta_* is strictly positive. Also delta_* <= R/2, so the compact interval defining p_* is strictly inside (-R,R); continuity and strict positivity of the first derivative imply p_* > 0.

The discarded-row calculation is

\[
\frac{\#\{i:V_i>B_*\}}n
\le\frac{V_*^2}{B_*^2}=\frac{p_{\rm strip}}4.
\]

Subtracting this worst-case count from each strip count of at least n p_strip/2 leaves at least n p_strip/4 rows for each sample. The same bad set may be used in both subtractions: no independence or random selection argument is needed. Each retained row contributes at least p_*^2 to the squared gate sum for every time, proving both parts of (11.4). Integer rounding cannot weaken the displayed real lower bound on the integer cardinality.

The sets depend on the full realized trajectory but are fixed sets of indices thereafter. They are only witnesses to a property of the already defined dynamics. No future-dependent choice is inserted into the flow.

Finally, strip indicators are independent across first rows. The two separate Chebyshev bounds are 4(1-p_strip)/(n p_strip) each, giving the stated factor 8. The union with E uses no independence. For n >= n_*, the final probability bound is exactly the one displayed in lines 476–479 and tends to one.

**Finding:** the accumulated-force bound, strip probability, boundary argument, threshold constants, simultaneous counts, and permanent gate-mass estimate are all valid.

## 8. Necessity example and limitations

**Locations:** PROOF 1–7, 354–387, 481–496; NOTATION 90–98.

The two independent inputs make the map from a first row to its two preactivations surjective. Thus the proposed n/2 copies of (2R,2R) and n/2 copies of (2R,-2R) are realizable for even n. With W^(2)(0)=I, their second-feature rows are (phi^(2)(A),phi^(2)(A)) and (phi^(2)(A),-phi^(2)(A)), respectively. Equal counts give K^(3)(0)=phi^(2)(A)^2 I exactly.

The readout choice gives b_0=1/n, and the operator norm of the identity is one. Also p_s,p_o < 1, so both count inequalities have strict slack. Since min(p_s,p_o) <= 1/2, kappa <= A^2/4, whereas phi^(2)(A) > A. The second-feature inequality is therefore strict as well. Every first preactivation is strictly saturated.

Continuity preserves the norm and kernel inequalities on a sufficiently small open neighborhood; the strict saturation preserves the counts and zero first gates. The independent finite Gaussian initialization has a strictly positive density on the entire parameter space, so this neighborhood has positive probability. Hence E alone fails to imply positive gate mass even almost surely at the stated fixed even widths. The example need not have appreciable or width-uniform probability, and the proof does not claim that it does.

The remaining scope statements are justified. Unconditional global existence supplies no unconditional fitting theorem. Positive first-gate mass by itself supplies no positive lower bound for residuals, reverse queries, feature velocities, or their weighted kernels. The displayed normalized readout bound does not bound individual stored readout coordinates uniformly in width. Smooth nonaffinity of the chosen scalar activation does not establish distributional nonaffinity of trained top features. No population limit, raw-GD theorem, or nonlazy feature-motion theorem has been proved or used. The input hypothesis excludes both rho=1 and rho=-1; no endpoint correlation result follows.

## Final disposition

**CLEAN.** No correction is required for the mathematical assertions within their stated finite-GF, fixed-interior-correlation scope. In particular, the loss margin is attained by the actual initialized flow, all continuation and clock steps close without circular assumptions, and the additional strip event supports the claimed simultaneous permanent first-gate mass with exactly the advertised constants and probability bound.

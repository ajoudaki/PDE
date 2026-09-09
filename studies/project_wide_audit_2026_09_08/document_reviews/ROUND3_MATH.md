# Round 3: independent mathematical document review

**Verdict: CLEAN.** No required mathematical correction was found in the reviewed version. This verdict concerns the internal correctness and qualification of the synthesis; it does not certify the proofs of quoted primary results that were unavailable under this review's source restriction.

## Source isolation and complete-read record

- Sole mathematical research input: `/home/amir/Codes/PDE/studies/project_wide_audit_2026_09_08/MASTER_RESEARCH_REPORT.md`.
- SHA256 before reading: `a43b83329277ad724143e1bc0da2bd1efbe7b2ed41989922869d137bb7486910`.
- SHA256 after the complete read and mathematical audit: `a43b83329277ad724143e1bc0da2bd1efbe7b2ed41989922869d137bb7486910`.
- Size: 94,870 bytes; 587 lines. The before/after hashes agree.
- Full-read ranges, inclusive, in order: **1–100, 101–200, 201–300, 301–370, 371–465, 466–530, 531–587**. Every line was returned without truncation and read, including every table row and the final paragraph.
- Operational instructions read: `/etc/codex/skills/solve-math-rigorously/SKILL.md`, all 115 lines, through EOF.
- No linked file, source audit, prior review, other project file, task history, browser source, or other agent's output was opened. References and earlier acceptance claims appearing inside the permitted report were treated as the report's attributions, not as independently inspected evidence.
- No experiment or new proof campaign was undertaken. The calculations below are direct checks of the report's own formulas and deductions. Only this assigned review file was written, using `apply_patch`; the master was not edited.

## Required corrections

None.

## Checks of the central deductions

### 1. Gaussian reuse: both displayed examples are consistent

At lines 74–79, conditioning each Gaussian row on its sum gives mean row $y_i\mathbf1^T/n$ and covariance $P/n$, where $P=I-\mathbf1\mathbf1^T/n$. Conditional row independence therefore gives exactly

\[
\mathbb E[W^Tg(y)\mid y]=\frac1n\sum_i y_i g(y_i)\,\mathbf1,
\qquad
\operatorname{Cov}(W^Tg(y)\mid y)
=\frac1n\sum_i g(y_i)^2P.
\]

The finite-width coefficient is random. Polynomial growth gives the integrability needed for the law of large numbers and Gaussian integration by parts, so its limit is $\mathbb E[Gg(G)]=\mathbb E g'(G)$. The displayed independent-residual representation of the conditioned matrix is valid. The text does not replace a reused matrix by fresh independent randomness.

The three-call generated-action example at lines 421–426 also keeps the requisite response. For a fixed bump scale, write $b=e_\varepsilon/\sqrt{v_\varepsilon}$. Evenness gives $\mathbb E[Yb]=0$, while $\mathbb E b^2=1$. Thus the limiting transpose query is a centered unit Gaussian. In the next forward query, the response coefficient is

\[
\mathbb E[G\tanh G]=\mathbb E\operatorname{sech}^2G=c,
\]

and the innovation variance is $\mathbb E\tanh^2G=\sigma^2$. The resulting law $\sigma G+cb$ is consistent with two-sided Gaussian conditioning; there is no missing subtraction of $c^2$ from the innovation variance. Conditional Jensen gives

\[
\mathbb E|\sigma G+cb|^p\ge c^p\mathbb E|b|^p
\asymp\varepsilon^{1-p/2},
\]

which yields the stated $L^p$ lower-bound exponent. The report correctly takes width first at each fixed scale and does not identify these high-sensitivity queries with actual training queries.

### 2. The finite-GF deduction from every vanishing GD mesh is valid

Lines 250–265 supply the needed argument, rather than equating a fixed-program theorem with a growing program. For the fixed nonnegative mobility $D_n$, square-loss dissipation gives

\[
\int_s^t\|\dot\theta\|^2du
\le\|D_n\|\bigl(\mathcal E_n(s)-\mathcal E_n(t)\bigr)
\le\|D_n\|\mathcal E_n(0).
\]

Consequently,

\[
\|\theta(t)-\theta(s)\|
\le\sqrt{(t-s)\|D_n\|\mathcal E_n(0)}.
\]

At fixed width this rules out finite-time escape, supplies an endpoint at a hypothetical finite maximal time, and permits continuation by the locally Lipschitz finite-dimensional vector field. Zero-mobility coordinates cause no problem. The bound need not be uniform in width.

Fixed-width Euler convergence in a compact tube transfers to the stated observables. With the continuous, piecewise affine Euler interpolation, parameter velocities converge in essential supremum, and continuity of the finite network Jacobian transfers this to hidden velocities in $L^2$ time. The neuron pairing bounds the **squared** path-law $W_2$ distance by the average squared uniform-path error, as the report states.

Almost-sure fixed-width convergence implies convergence in probability and permits a deterministic choice of $\widehat\eta_n<1/n$ with the displayed probability bound. Since the population theorem covers every deterministic vanishing sequence, the triangle inequality transfers its local conclusion to finite GF. This does not establish global population continuation, additional observables, or a common-neuron coupling between arbitrary meshes. The distinct statement for other separable losses is appropriately stopped and qualified.

### 3. The three clipping statements cannot be combined, and the report does not combine them

Lines 363–368 correctly use reverse fields $\delta^{(\ell)}=n\nabla_{z^{(\ell)}}f$, without residual or output averaging factor. The physical clock for full square loss and target one is therefore $ds/dt=2(1-f)$.

For the metric projection at lines 388–403, replacing the complete $\delta^{(2)}$ by $u$ in both lower updates gives

\[
\frac{dz^{(2)}}{ds}
=\left[\frac{\|h^{(1)}\|_2^2}{n}I+
W^{(2)}\operatorname{diag}(\phi'(z^{(1)})^2)(W^{(2)})^T\right]u
=Mu.
\]

Thus the defect relative to the unprojected vector field at the same state is $-e_R$, with $e_R=M(\delta^{(2)}-u_R)$. Box optimality places $e_R$ in the outward normal cone: its nonzero coordinates have the sign of the saturated coordinate of $u_R$. Hence

\[
e_R^Tu_R=R\|e_R\|_1,
\qquad
(\delta^{(2)})^TMu_R
=u_R^TMu_R+R\|e_R\|_1.
\]

These identities explain the positive work contribution and the integrated $L^1$ defect bound. Bounded tests inherit that bound; an $L^2$ defect or squared-observable estimate does not follow. A cap $C_S\sqrt n$ is inactive when the stated coordinate bound holds, and a bounded total fitting feature time allows one such cap for all physical time on the fitting event.

For the different coordinate-query construction, $R_n=o(\log n)$ makes the logarithm of the bound in lines 382–383 equal to $-(1/24)\log n+o(\log n)$, so it tends to zero. This proves comparison of the two varying constructions, not existence of a population limit. Fixed-cap identification, slowly growing coordinate caps, and a $\sqrt n$ metric-projection cap use different rules or scales. The report states each missing bridge explicitly. Its separate treatment of the possibly nonsymmetric capped hidden contribution at line 295 is also correct.

### 4. Formal, analytic, and actual-dynamics no-gos are separated correctly

At lines 154–168, a nonzero initial residual is essential to the residual-clock argument. If the physical formal output were analytic, its clock would be analytic with nonzero derivative and would have an analytic local inverse; composing with that inverse would make the feature series analytic. Thus a divergent feature series transfers the formal analytic obstruction in this case. This argument would fail at a zero initial residual, which the report excludes.

For the explicit counterexample,

\[
g^{(j)}(t)=\mathbb E\left[G^j r^{(j)}(tG)\right],
\qquad r(u)=(1+u^2)^{-1}.
\]

Bounded derivatives of $r$ and finite Gaussian moments justify smoothness. The even Taylor coefficients are indeed $(-1)^k(2k-1)!!$, with zero radius. The autonomous system $(\dot s,\dot q)=(1,g'(s))$ nevertheless has the unique solution $(s,q)=(t,g(t))$ from $(0,1)$. This refutes a smooth-ODE impossibility deduction while leaving an analytic obstruction intact. Formal jets still require identification with the actual trajectory.

The actual quadratic initial-layer claim is expressly withheld because of its reported adaptive bridge and row-estimate defects. Its dependent GD claim inherits that qualification. The frozen-bottom all-mesh statement, the fixed-step positive-polynomial obstruction, the conditional tagged DMFT comparison, and the finite-width ReLU gate example have distinct scopes. None is used to certify canonical full-network nonexistence. Likewise, ambient or generated-space estimates failing do not by themselves prove failure along a Gaussian training trajectory, and failure of ambient local Lipschitzness does not imply nonuniqueness.

## Remaining formula and scope inventory

The following completes the check of the report's other displayed formulas, numerical assertions, and deductions. “Source-qualified” here means that the statement is internally compatible with its declared assumptions and evidence level; it does not mean its unprovided derivation was independently verified.

| Report lines | Audit result |
|---|---|
| 39–68 | The input Gram, RMS norm, layer populations, raw learning-metric kernels, and stored-readout conventions are consistent. Changing first coordinates from $W^{(1)}$ to $V^{(1)}=W^{(1)}/\sqrt d$ changes mobility from $n\kappa_1$ to $n\kappa_1/d$, as stated. Fixed depth, fixed sample size, physical time, and width/step quantifiers remain distinct. |
| 85–106 | In the fixed metric, differentiating $Df=\|\nabla f\|^2$ twice gives $D^3f=2\nabla^3f[g,g,g]+4\|\nabla^2f\,g\|^2$. This is correctly distinguished from the Euler-comparison coefficient $J$, whose cubic term has coefficient one. The fixed-count remainder is not used uniformly in a growing update count; the sharper one-layer claim retains its smaller interval. The general recurrence and its constants remain source-qualified. |
| 110–119 | The activation-stability witness checks directly. The constant perturbation makes the second preactivation of the selected row equal to one; $\psi'(0)=2$ and $\psi'(1)=3/2$ give first updates $4h\mathbf1$ and $3h\mathbf1$. The readout RMS norm and middle operator norm are one. The perturbed prediction tends to zero, so a fixed nonzero physical target preserves the discrepancy. No Gaussian-typical counterexample is inferred. |
| 127–150 | The QQ initial block values sum to $27+36+48=111$. Gaussian raw-square variance propagation for three hidden layers gives block values $2187,2916,3888,5184$, summing to $14175$. The formal inverse has nonzero linear coefficient. Output order 17 supplies eight candidate moments after subtraction and division; integrating the Ward identity can supply hidden order 18 without output order 19. Finite Hankel positivity is never promoted to all-order positivity, determinacy, or trajectory identification. Detailed determinant certificates and upstream coefficients remain explicitly qualified. |
| 174–180 | The quantitative initial-layer and ReLU statements retain their effective-model, auxiliary-model, finite-width, or compactness scopes. Binary occupation satisfies $I^2=I$, so averaging its square gives $\lambda$, not $\lambda^2$. Tightness is not treated as uniqueness. |
| 186–211 | The deep-linear equation has $\dot f=2\eta(y-f)\|C^3\|_{\mathrm{HS}}^2$ by the trace derivative, consistent with the displayed kernel. The trace-norm bound is compatible with the stated rank structure and square-loss dissipation. Exact GD recomputes the residual from the operator state. The explicit spectral measure and width-identification proof remain quoted results. Three-hidden-layer, one-sample identification is not expanded to arbitrary depth/data; finite-contraction closure negatives are compatible with an infinite-dimensional current operator. |
| 217–229 | Direct differentiation gives all six QI/IQ feature-time updates, including the factors $4$, $2$, and $1/n$. No residual is missing under the explicitly stated feature-time convention. Conserved spectra are not treated as sufficient to recover the coordinate-sensitive kernel; the numerical orientation witness remains a quoted finite-algebra result. |
| 235–248, 269–295 | Local existence does not promise activity when rates vanish or activations are affine. The global table keeps initialization, activation, depth, data separation, labels, loss normalization, and mesh restrictions separate. For the bounded one-sample activation, $1\pm\pi/20$ lie within $[5/6,7/6]$; the readout floor is $25/36$, the hit bound is $36/25<3/2$, and full-square-loss decay is $e^{-25t/9}$. The physical clock diverges at the controlled regular hit. The shape constant is positive because a bounded nonconstant continuous shape cannot be affine on every bounded interval. Detailed gain constants and separation exponents are source-qualified. |
| 297–305 | The relative-nonaffinity inequality follows from the independent-copy variance identity: its numerator is at most $e^2\operatorname{Var}Z$, and its denominator is at least $(a-e)^2\operatorname{Var}Z$. Finite variance, nondegeneracy, and $a>e$ are stated. The equal-coefficient odd-gain theorem is correctly excluded from this argument. |
| 309–327 | Order-one and tiny stored readout, local and global population claims, finite optimization, special-angle results, subsequential containment, and stationary zero-label limits remain separate. The equal-label two-sample clock factor four agrees with unhalved sum loss. Initial or local activity is not promoted to activity at every positive time. The numerical tanh kernel and detailed source-specific conclusions remain qualified quotations. |
| 331–351 | Since $q_L$ is common to the diagonal, dividing the absolute eigenvalue estimate by $q_L$ gives the displayed normalized estimate. The large-depth Gaussian expansion $\phi_\theta(z)=z-\theta z^3/3+O(z^5)$ yields residual variance $2\theta^2q^3/3$; with $q\sim1/(2\theta L)$ this gives $1/(12\theta L^3)$ and relative fraction $1/(6L^2)$. The fitting-time lower bound is the reciprocal of the stated unit-ball loss-drop upper bound, using dissipation and first-exit distance one. Existence or a matching upper rate is not inferred. Sharp uniform initialization estimates and the calibrated-sine percentage remain source-qualified. |
| 412–433 | A small $L^2$ gate difference times an $L^2$-bounded field need not be small in $L^2$. The stated tail criterion is compatible with an Osgood modulus of order $u\log(1/u)\log\log(1/u)$, whose reciprocal integral diverges at zero. It is presented only as a sufficient criterion. The RMS-normalized initial kernel is a source-dependent formula; smooth fixed-width square-loss dynamics do have the stated finite-time continuation argument at fixed positive epsilon, without a width-uniform tail conclusion. |
| 439–459 | The residual increment $1/(nL)$ and mobility $\eta nL$ have consistent particle/depth scaling. The nested-tanh example has uniformly controlled effective coefficients and derivatives on bounded state strips. For the depth-averaged initial $W_1$ error, identical layer marginals make its expectation equal to the one-layer expectation, so the convergence implication does not require a maximum over a growing number of layers. The $L^{-1}$ term then vanishes along every joint sequence. No dense-Gaussian, GD, or fitting theorem is inferred. |
| 461–477 | Finite Hermite truncation is not equated with cutoff removal or a dense-network limit. Literature comparisons and imported-proof qualifications do not create additional project theorems. Their primary proofs were not read in this review and are not certified here. |
| 483–517 | Odd/even symmetry fitting obstructions have the correct label qualifications. The bounded-feature contrast estimate is Cauchy–Schwarz and gives the stated readout lower bound. For mean square loss, $\dot f=-2Kr/m$ gives $\dot{\mathcal L}=-4r^TKr/m^2$; residual-direction coercivity yields decay rate $4\kappa/m$. An initial gap is not treated as a trained gap. The prescribed-accuracy probability inclusion is valid and proves neither a uniform-in-time trajectory limit nor endpoint convergence. |

## All-36 task-map consistency

The map has exactly **17 PDE entries plus 19 PDE-2 entries**, with no missing number or extra “Work” task. Every entry was checked against the corresponding discussion and the final correction list.

- PDE 1–5 agree with the bounded global theorem, conditional reconstruction routes, scoped two-sample extensions, clipping/response work, and broad local theorem with its finite-GF corollary.
- PDE 6–12 preserve the original-readout nonlinear open problems, repaired L2 theorem, representation negatives, withheld quadratic initial layer, finite RMS result, conditional broader linear proposal, and partial-quadratic reductions.
- PDE 13–17 preserve activation-specific Stieltjes evidence, formal/conditional no-gos, the incomplete noncommutative transform, retained output order 17 versus hidden order 18, and the missing backward-kernel concentration step.
- PDE-2 1–7 agree with the shape/depth/gain results, explicit no-gain limitations, recovery-only work, local/global activation variants, and separate L3 local and finite-fitting results.
- PDE-2 8–12 retain the sin-plus-cos correction, linear and mesh distinctions, unavailable experiment/attribution evidence, unrecovered nested theorem, and fixed-step MFP scope.
- PDE-2 13–19 preserve the original initialization, failed global bridges, non-independent teaching task, stationary tanh exception, scalar-particle versus dense residual distinction, fixed-order machinery, and incomplete private-history provenance.

These are internal consistency findings. The report's claims about external task identities, private histories, original source hashes, and earlier auditors' read coverage were not independently verified. Their explicit qualifications are not defects in this source-qualified synthesis.

## Optional improvement

At lines 250–257, naming the GD interpolation explicitly as piecewise affine would make the velocity argument easier to read in isolation. The current discussion of piecewise derivatives already indicates that convention, so this is an expository suggestion, not a required correction.

The CLEAN verdict leaves every expressly open mathematical, coefficient-generation, source-recovery, and imported-proof obligation open.

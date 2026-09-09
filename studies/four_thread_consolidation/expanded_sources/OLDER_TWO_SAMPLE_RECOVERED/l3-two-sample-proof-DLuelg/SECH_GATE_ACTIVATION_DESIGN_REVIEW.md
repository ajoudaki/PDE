# Independent adversarial audit of SECH_GATE_ACTIVATION_DESIGN.md

Candidate: `/tmp/l3-two-sample-proof-DLuelg/SECH_GATE_ACTIVATION_DESIGN.md`

Candidate SHA256:

`c0f67365fbe36af74db9708ce8a32018b30d8164e77c50b068f71299045e4f24`

Audit date: 2026-09-06.

## Verdict and audit boundaries

**PASS as the stated supporting theorem. No required mathematical corrections were identified.** The activation bounds, scalar Gaussian nonaffinity, initial forward empirical convergence, and uniform frozen-control tangent estimate are valid under the assumptions actually stated. The proof covers arbitrary integrable controls within one fixed sign quadrant, including zero components and changing component ratios. Its constants are conservative but correct.

This verdict does not extend to controls that change sign, derivatives of feedback systems, or a trained-network limit. The candidate explicitly excludes those conclusions. The initialization conclusions concern the limiting empirical laws; deeper finite-width preactivations are conditionally Gaussian and generally have Gaussian-mixture unconditional laws.

I read the entire candidate, lines 1–231. It was the only mathematical input. I did not inspect project history, other research documents, ledgers, other reviews, or other task conversations. No numerical experiments were performed. No specialized external result was needed: the checks below use elementary calculus, finite-dimensional linear algebra, integral-equation estimates, and elementary probability. The candidate was not edited.

The historical comparison with an unspecified “arctan route” at lines 222–224 cannot be independently checked from this input. Every bound explicitly written here is verified directly, and none of the proofs depends on that comparison.

## Required corrections versus optional improvements

### Required corrections

None for the mathematical supporting theorem or its stated initialization claim, with “empirical laws jointly in probability” understood in the product weak topology for the three separate layer populations, as the surrounding text indicates.

In particular, the following are not missing hypotheses: independence between a random initial point and its control; nonvanishing control components; a bound on changes of component ratios; differentiability of the cutoff; or a finite count of coordinate sign crossings. The proof needs none of them.

### Optional improvements

1. **Make the initialization statement explicit at its first occurrence, lines 75–102.** Define the population modes as `(phi(X) ± phi(Y))/2`, state their limiting squared norms as expectations, and display the covariance recursion and product weak convergence given below. This would prevent a finite-width reading of the Gaussian and lower-bound assertions. The later paragraph already identifies this as a forward limit, so this is a clarification rather than a correction to a false limiting claim.
2. **Remove or define the historical comparator, lines 222–224.** Replace “of the arctan route” with “in (2)” if the file is intended to be fully standalone. No mathematical property of an unnamed comparator can be audited from this document alone.
3. **Specify `q > 0` and fixed deterministic `k < 1` in the random-control corollary, lines 215–220.** This makes the conventional meaning of the moment statement explicit. It is also useful to say that a measurable random control is an `L1`-valued random element, or a jointly measurable process with integrable sample paths.
4. **The exponent can be reduced without a new argument.** Choosing `Q = log(e + U) >= 1` in (10) gives

   `I <= 4 + [4 + 8k/(1-k)] log(e+U)`.

   Indeed, `U/(e+U) <= 1` and `U/(e+U)^2 <= 1`, so the two tail terms sum to at most `2+2k <= 4`. Thus the exponent `4+8k/(1-k)`, or the simpler upper bound `8/(1-k)`, also works with the stated prefactor and `e^4`. The candidate's larger exponent is valid; sharpening it is not required.

## 1. Activation, derivative bounds, and relative-gate inequality

References: lines 8–17 and 36–66.

Write `a = 1/10`. Since `1+sinh^2 z = cosh^2 z` and `cosh z > 0`,

`d/dz atan(sinh z) = cosh z/(1+sinh^2 z) = sech z`.

Consequently `p = phi' = a sech z` is strictly positive at every finite real argument, is even, and is bounded by `a`. The definition contains no width, angle, label, or time parameter. The function `g = phi-1` is odd and strictly increasing.

For the range, the substitution `t=e^{-v}` gives exactly

`integral_0^infinity sech v dv = 2 integral_0^1 1/(1+t^2) dt`.

For `0<t<1`,

`(1-t^2/2)(1+t^2)-1 = t^2(1-t^2)/2 > 0`.

The claimed pointwise strict inequality and its integrated version therefore have the correct direction:

`2 integral_0^1 1/(1+t^2) dt < 2(1-1/6) = 5/3`.

Multiplication by `a`, followed by oddness, proves `5/6 < phi(z) < 7/6` for every real `z`. There is no issue at infinity: the integral gives a bound on the limiting tail amplitude itself. Strictness is justified on an interval of positive measure, not merely at isolated points.

The next derivatives are

`p' = -a sech z tanh z`,

`p'' = a sech z (2 tanh^2 z - 1)`.

In particular, both `|p'| <= a` and `|p''| <= a` hold globally. The second identity also supplies the global Lipschitz bound on the spatial derivative needed later. For all higher derivatives, one can write

`p^(m)(z) = a sech z P_m(tanh z)`,

where `P_0=1` and

`P_(m+1)(t) = (1-t^2) P_m'(t) - t P_m(t)`.

Each `P_m` is a polynomial, hence bounded on `[-1,1]`. This proves the asserted boundedness of each fixed higher derivative; no uniform bound over derivative order is claimed.

The relative-gate inequality has a particularly direct verification. For `z<z'`,

`|p(z')-p(z)| <= integral_z^z' |p'(v)| dv`

`<= integral_z^z' p(v) dv = phi(z')-phi(z)`.

Here `|p'|/p = |tanh| <= 1`, with `p>0` everywhere. Reversing the two arguments proves the stated absolute-value inequality. The candidate's inverse-function argument is also valid: `phi` has a differentiable inverse on its open range, and its derivative is never zero at a finite argument. No extension to the endpoints of that range is needed.

Dividing the inequality by two gives `|p_-| <= |V|` exactly with the normalization in lines 64–65. It has no probabilistic or independence content.

## 2. Strict scalar Gaussian nonaffinity

References: lines 68–73 and 90.

Let `G` have any scalar Gaussian law with strictly positive variance. Boundedness gives `phi(G) in L2`; the variables `1` and `G` also belong to `L2`. If `phi(G)=b+cG` almost surely, continuity and the strictly positive density on every real interval imply `phi(z)=b+cz` for all real `z`. Otherwise the continuous difference would be nonzero on an interval of positive Gaussian probability.

That identity is impossible because `phi'=a sech` is not constant. For example, its value at zero is `a`, while it tends to zero at infinity.

The assertion about strictly positive best-affine squared error also follows, not merely nonattainment of zero by a chosen affine function. The two-dimensional span of `1,G` is closed. Explicitly, writing `m=E G` and `sigma^2=Var(G)>0`,

`E[(b+cG)^2] = (b+cm)^2 + c^2 sigma^2`.

Thus an `L2`-Cauchy sequence of affine functions has Cauchy coefficients and an affine `L2` limit. If the infimum approximation error were zero, closedness would put `phi(G)` in this span, contradicting the preceding argument. This verifies both the closure hypothesis and the strict positivity conclusion.

No positive lower bound uniform over Gaussian means and variances is asserted or proved. In particular, the error can tend to zero as a variance tends to zero. This does not contradict the pointwise nonaffinity statement.

## 3. Initial label modes and population covariance recursion

References: lines 75–90.

Here is the precise limiting interpretation of the candidate's initialization argument. Put

`Sigma_1 = [[1,rho],[rho,1]]`, with `-1 <= rho < 1`,

and, for a centered Gaussian pair `(X_l,Y_l)` with covariance `Sigma_l`, define

`H_l = (phi(X_l), phi(Y_l))`,

`Sigma_(l+1) = E[H_l H_l^T]`.

This is an uncentered second-moment recursion. Centering the features instead would change the argument and, at the initial endpoint `rho=-1`, would give a singular centered feature covariance.

Each centered scalar Gaussian is symmetric, so oddness of `g=phi-1` gives `E phi(X_l)=E phi(Y_l)=1`. Therefore

`E[((phi(X_l)+phi(Y_l))/2)^2] >= 1`.

Initially `Var(X_1-Y_1)=2(1-rho)>0`, including when `rho=-1`. A nondegenerate scalar Gaussian equals zero with probability zero, and strict monotonicity of `phi` gives

`E[((phi(X_1)-phi(Y_1))/2)^2] > 0`.

There is a short verification that these two mode statements imply positive definiteness in this setting. Equal marginal variances and the Gaussian law make `(X_l,Y_l)` exchangeable. Hence its feature second-moment matrix has the form

`M = [[a,b],[b,a]]`.

Its two eigenvalues are

`a+b = (1/2) E[(phi(X_l)+phi(Y_l))^2] >= 2`,

`a-b = (1/2) E[(phi(X_l)-phi(Y_l))^2] > 0`.

This proves positive definiteness whenever the current Gaussian difference has positive variance. Applying it first at `l=1` makes `Sigma_2` positive definite. Its diagonal entries are equal and positive; its Gaussian difference consequently has positive variance. The argument repeats to give `Sigma_3` positive definite and positive norms of both modes at layer three. Each scalar marginal remains nondegenerate, so Section 2 applies at every initial limiting hidden layer.

The candidate's separate proofs of positive definiteness are also sound. At `rho=-1`, `(X_1,Y_1)` has the law of `(G,-G)`, so a homogeneous dependence of the feature pair would read

`(c_1+c_2)+(c_1-c_2)g(G)=0` almost surely.

Taking expectations forces `c_1+c_2=0`, and `E[g(G)^2]>0` then forces `c_1-c_2=0`. For an interior correlation the Gaussian pair has positive density everywhere. A continuous relation `c_1 phi(x)+c_2 phi(y)=0` must then hold everywhere; varying `x` and `y` separately forces both coefficients to vanish.

Endpoint and uniformity checks:

- `rho=-1` is legitimately included in this initialization argument, although the first two-dimensional Gaussian law is singular. The individual scalar laws are nondegenerate, and the next uncentered second-moment matrix is positive definite.
- `rho=1` is correctly excluded: the two initial coordinates and their features coincide, so the opposite mode vanishes and the feature second-moment matrix has rank one.
- Positivity of the opposite mode is for each fixed permitted correlation. There is no asserted uniform lower bound as `rho` approaches one.
- These are population expectations and limiting normalized empirical squared norms. They are not deterministic lower bounds on every finite sample.

## 4. Initial empirical convergence, including jointness and singular covariances

References: lines 92–105.

The conditional Gaussian statement in the candidate is exact under the initialization it specifies: each new independent Gaussian row has independent weights of variance `1/n`, or equivalently standard Gaussian weights with an external factor `1/sqrt(n)`. Conditional on the preceding feature array `H_(l,i) in R^2`, the next preactivation rows are independent with covariance

`Sigma_(l+1,n) = (1/n) sum_i H_(l,i) H_(l,i)^T`.

To verify the limiting statement fully, let `mu_(l,n)` be the empirical measure of the `n` preactivation pairs in population `l`, and let

`mu_l = N(0,Sigma_l)`.

For any fixed bounded continuous `f : R^2 -> R`, conditional independence gives

`E[mu_(l+1,n)(f) | preceding features] = F_f(Sigma_(l+1,n))`,

`Var(mu_(l+1,n)(f) | preceding features) <= ||f||_infinity^2/n`,

where `F_f(S)=E[f(S^(1/2) G)]` for a standard two-dimensional Gaussian `G`. Taking expectations of the conditional variance and applying Chebyshev shows

`mu_(l+1,n)(f) - F_f(Sigma_(l+1,n)) -> 0` in probability.

The same reasoning applies to all four covariance-entry tests

`f_ab(z)=phi(z_a) phi(z_b)`.

They are continuous and bounded by `49/36` in absolute value. A valid conditional variance constant is therefore `(49/36)^2/n`. The `O(1/n)` claim is about conditional sampling variance; it is not a claim that the unconditional law or covariance bias already has that rate.

The asserted square-root continuity is valid even at singular covariances. If positive semidefinite `S_m -> S`, their positive roots `R_m` are bounded because `||R_m||_op^2=||S_m||_op`. Every subsequence has a convergent further subsequence. A limit `R` is positive semidefinite and satisfies `R^2=S`. Such a positive semidefinite root is unique: it commutes with `S`, preserves each eigenspace of `S`, and on an eigenspace with eigenvalue `lambda >= 0` its nonnegative eigenvalues must all be `sqrt(lambda)`. Therefore every subsequential limit is `S^(1/2)`, proving `R_m -> S^(1/2)`.

Under the common coupling by `G`, `S_m^(1/2) G -> S^(1/2) G` pointwise. Bounded continuity of `f` and bounded convergence then prove continuity of `F_f` on the entire positive semidefinite cone. This argument never uses invertibility or Gaussian densities near a singular covariance.

The independent first rows give, by the same variance bound,

`mu_(1,n)(f) -> mu_1(f)` in probability.

In particular, applying this to the covariance-entry tests gives `Sigma_(2,n) -> Sigma_2` in probability. Continuity of `F_f` and the conditional fluctuation estimate then give `mu_(2,n)(f) -> mu_2(f)` in probability. Repeating the covariance-entry argument and the conditional estimate proves the same conclusion for layer three.

This proves the stated joint empirical convergence, with the correct meaning of “joint.” A basic weak neighborhood of a deterministic probability measure is specified by finitely many bounded continuous test integrals. A finite union bound shows that each empirical measure enters every such neighborhood with probability tending to one. A second finite union bound over the three layers yields

`(mu_(1,n), mu_(2,n), mu_(3,n)) -> (mu_1,mu_2,mu_3)`

in probability in the product weak topology. No independence between the three empirical measures is necessary. Applying the continuous feature map `(z_1,z_2) -> (phi(z_1),phi(z_2))` gives the corresponding feature empirical laws and mode squared norms; their required test functions are bounded and continuous.

This does not establish a six-dimensional empirical law obtained by matching a neuron index across all three layers, nor independence of such matched triples. The candidate explicitly says that no such matching is required. It also does not establish Gaussian laws at positive training times or any law involving reused forward and backward matrices. Those restrictions are substantive and correctly stated.

## 5. Existence and initial-state differentiability for L1 controls

References: lines 19–34 and 107–124.

Fix `u in L1([0,T];R^2)` and `k=|rho|<1`. The Euclidean operator norm of `C` is `1+k`. With

`L(t) = (1+k)||u(t)||_1/10`,

the field `F(t,z)=C diag(p(z_1),p(z_2))u(t)` satisfies

`|F(t,z)| <= L(t)`,

`||D_z F(t,z)||_op <= L(t)`,

`||D_z F(t,z)-D_z F(t,z')||_op <= L(t)|z-z'|`.

The third estimate follows from `|p''|<=1/10`, verified above. The field and its derivative are measurable in time; all three coefficients are integrable. The displayed speed and spatial-derivative bounds in the candidate are thus valid in Euclidean norm.

Absolute continuity of the integral of `L` permits a finite partition into intervals on which `integral L < 1`. On each interval the integral-equation map is a contraction on continuous paths with the fixed starting value. It maps that space to itself because the field has the integrable uniform bound `L`. Concatenation gives a unique absolutely continuous solution on the entire interval. In particular,

`|z(t)-z(0)| <= integral_0^t L(s) ds`,

so there is no finite-time escape.

The differentiability assertion is also valid for merely integrable time dependence. Let `Lambda=integral_0^T L=(1+k)U`, let `delta` be an initial increment, and let `Delta(t)` be the difference between its perturbed solution and the original solution. The integral Lipschitz estimate gives

`sup_t |Delta(t)| <= e^Lambda |delta|`.

Let `J` solve `J'=D_zF(t,z(t))J`, `J(0)=Id`. The globally Lipschitz spatial derivative gives the pointwise Taylor remainder bound

`|F(t,z+Delta)-F(t,z)-D_zF(t,z)Delta| <= (L(t)/2)|Delta|^2`.

Consequently another integral estimate gives, for example,

`sup_t |Delta(t)-J(t)delta| <= (Lambda/2)e^(3Lambda)|delta|^2`.

This is a uniform quadratic remainder for every direction of `delta`, so it proves the Fréchet derivative, not merely directional derivatives. It is uniform in time and in the initial point for a fixed control norm. The exponential estimate used here only establishes regularity; the later argument improves the bound on `J` itself.

All time derivatives and variational equations are understood almost everywhere. No derivative of `u` is needed. The derivative keeps `u` fixed throughout, exactly as the candidate stipulates.

## 6. Reflection and tangent energy

References: lines 126–147.

Let `S=diag(s_1,s_2)`. The sign premise gives `Su=|u|` componentwise almost everywhere, including on zero sets. Evenness of `p` and the identity

`S C S = C_r`, where `r=rho s_1s_2`,

give the reflected equation

`x'=A+rB`, `y'=rA+B`,

`A=alpha sech x`, `B=beta sech y`,

`alpha=|u_1|/10`, `beta=|u_2|/10`.

Here `A,B >= 0` and `integral(alpha+beta)=U`. Reflection is orthogonal, so it preserves the Euclidean operator norm of the initial-state derivative.

The tangent equation is

`eta' = C_r diag(-A tanh x,-B tanh y) eta`.

Since `|r|=k<1`, `C_r` is positive definite. For `E=eta^T C_r^(-1) eta`, differentiation along the absolutely continuous tangent gives exactly

`E' = 2[-A tanh x eta_1^2 - B tanh y eta_2^2]`.

The component estimate used in the proof has constant one, with no missing factor of `1/(1-k)`:

`E = eta_1^2 + (eta_2-r eta_1)^2/(1-r^2) >= eta_1^2`,

and the symmetric identity gives `E>=eta_2^2`. Hence, with `f(v)=(-tanh v)_+`,

`E' <= 2[A f(x)+B f(y)]E = 2hE`.

The function `h` is nonnegative and integrable because `h<=A+B<=alpha+beta`. An integrating factor therefore yields `E(T)<=E(0)e^(2I)`, where `I=integral h`.

The eigenvalues of `C_r` are `1+r` and `1-r`, so

`|eta(T)|^2 <= (1+k)E(T)`,

`E(0) <= |eta(0)|^2/(1-k)`.

Taking square roots and then the supremum over unit initial tangents proves (5), with precisely the prefactor `sqrt((1+k)/(1-k))` and exponent `I`. No extra factor of two belongs in the final exponent.

## 7. Truncation, occupation, and all cutoff endpoints

References: lines 149–200.

A permissible continuous cutoff exists, for example the function equal to one up to one, linear from one to zero on `[1,2]`, and zero after two. Smoothness is unnecessary.

For any cutoff as stated, `f_Q` is continuous. It vanishes at and beyond `v=0` on the positive side, and at and below `v=-2Q` on the negative side. At `v=-Q`, the cutoff is exactly one. Consequently `H_Q` is continuously differentiable across `0`, `-Q`, and `-2Q`, with `H_Q'=-f_Q` everywhere. Its derivative is bounded by one, so it is globally Lipschitz. Thus composition with an absolutely continuous coordinate is absolutely continuous and obeys the chain rule almost everywhere. No derivative of `chi` occurs.

The inequalities `0<=H_Q<=2Q` follow from integration of a function between zero and one supported on an interval of length at most `2Q`. In particular, the potential is uniformly bounded even for an initial coordinate arbitrarily far into the negative tail.

Set

`J_Q(t)=A f_Q(x)+B f_Q(y)`,

`K_Q(t)=f_Q(x)B+f_Q(y)A`,

`S_Q(t)=H_Q(x)+H_Q(y)`.

The discarded difference `f-f_Q` is zero for `v>=-Q`. Using

`sech v = 2/(e^v+e^(-v)) <= 2e^(-|v|)`,

one obtains exactly

`integral [h-J_Q] <= 2e^(-Q) integral(alpha+beta) = 2e^(-Q)U`.

This verifies (6), including its factor two and the support endpoint.

If `r>=0`, differentiation gives `S_Q'=-J_Q-rK_Q<=-J_Q`. Since the terminal potential is nonnegative and the initial potential is at most `4Q`,

`integral J_Q <= 4Q`,

and hence `I<=4Q+2e^(-Q)U`. This also covers `r=0`.

If `r=-k<0`, differentiation instead gives `S_Q'=-J_Q+kK_Q`, exactly (7). Let

`D={t: |x(t)|<=2Q and |y(t)|<=2Q}`.

On `D`, `K_Q<=A+B`. Also `w=x+y` is absolutely continuous and

`w'=(1-k)(A+B)>=0` almost everywhere.

Thus `w` is nondecreasing, and `D` is contained in the closed strip `|w|<=4Q`. To justify (8) including the boundary, put `c(w)=max(-4Q,min(w,4Q))`. The composition is absolutely continuous. Its derivative equals `w'` in the open strip and zero outside the closed strip.

On either boundary level set, `w'=0` almost everywhere. In this application there is an elementary proof: a level set of a nondecreasing function is an interval, possibly empty or a singleton; the function is constant on its interior, and endpoints have measure zero. The more general assertion for absolutely continuous functions used by the candidate is also correct. At a differentiability point in a level set, a nonzero derivative would make that point isolated in the level set. Such isolated points form a countable set, while nondifferentiability occurs only on a null set. This also proves the needed general assertion without invoking a specialized result.

It follows that

`integral_D (A+B)`

`<= (1/(1-k)) integral_{|w|<=4Q} w'`

`= [c(w(T))-c(w(0))]/(1-k)`

`<= 8Q/(1-k)`.

This verifies the closed-strip occupation bound and its constant. Nonnegativity of `w'` is essential to the first inequality and is supplied by the dynamics. Repeated entries into the central set and flat portions create no additional term.

Outside `D`, if `f_Q(x)>0`, then necessarily `-2Q<x<0`. The other coordinate must therefore satisfy `|y|>2Q`, so

`f_Q(x)B <= 2 beta e^(-2Q)`.

The corresponding bound for the other summand is `f_Q(y)A<=2 alpha e^(-2Q)`. These inequalities also hold when the respective cutoff factor is zero. Integrating their sum proves (9), with the constant `2e^(-2Q)U`; no extra factor two is missing.

Finally, integrating (7) gives

`integral J_Q = S_Q(0)-S_Q(T)+k integral K_Q`.

Use `S_Q(0)<=4Q`, `S_Q(T)>=0`, the central occupation estimate, the outside estimate, and the discarded-tail estimate. The result is exactly

`I <= [4+8k/(1-k)]Q + 2k e^(-2Q)U + 2e^(-Q)U`.

Thus (10) is valid uniformly over every finite initial point and every permitted control. No monotonicity of either individual coordinate was assumed in the negative-correlation case.

## 8. Final constants, zero cost, and polynomial terminology

References: lines 202–213.

The chosen `Q=2log(e+U)` satisfies `Q>=2`, so it meets the earlier requirement `Q>=1`. The tail factors are

`e^(-Q)U = U/(e+U)^2 <= 1`,

`e^(-2Q)U = U/(e+U)^4 <= U/(e+U)^2 <= 1`.

Therefore the sum of the tail terms in (10) is at most `2+2k<=4`. The coefficient of the logarithm is exactly

`2[4+8k/(1-k)] = 8+16k/(1-k)`.

Moreover,

`8+16k/(1-k) = 16/(1-k)-8 <= 16/(1-k)`.

These calculations verify both inequalities in lines 207–208. In the case `r>=0`, the earlier estimate gives `I<=8log(e+U)+2`, which is also bounded by the same final expression. Substitution into the energy bound yields exactly

`||D_z0 z(T)||_op`

`<= sqrt((1+k)/(1-k)) e^4 (e+U)^(16/(1-k))`.

At `U=0`, both controls vanish almost everywhere, the flow is the identity, and its derivative is the identity. The displayed upper bound is loose but still valid. The same observation covers a zero-length time interval. If only one control component vanishes, all the proof steps continue to apply; none divides by `alpha`, `beta`, `A`, or `B`.

The exponent is finite for each fixed `k<1`. Both it and the norm-comparison prefactor deteriorate as `k` approaches one; no estimate at `|rho|=1` follows from this proof. Inclusion of `rho=-1` in the separate initialization discussion does not extend the characteristic theorem to that endpoint.

For noninteger exponent, the result is a finite-power growth bound. Because `e+U>=1`, replacing the exponent by its ceiling gives an ordinary polynomial upper bound in `U`, as stated. The candidate correctly avoids presenting the original noninteger power as literally a polynomial.

## 9. Random controls and scope of the conclusion

References: lines 215–231 and introductory qualifications.

For fixed `k<1`, let `C_k=sqrt((1+k)/(1-k))e^4`. The pathwise result immediately gives, for every `q>0`,

`E[||D_z0 z(T)||_op^q] <= C_k^q E[(e+U)^(16q/(1-k))]`.

No factor involving the initial point appears. Hence no integrability assumption on that point and no independence between it and the control is needed. Even a sign quadrant selected differently for different realizations is harmless, provided each realization has one constant sign pair throughout time; the estimate depends only on `|rho|`.

The tangent is measurable under the usual meaning of a measurable random control and initial point. The integral equation can be constructed by measurable Picard iterates; alternatively, the same integral estimates show continuity of the solution and its variational matrix in the initial point and in the `L1` control on sets of bounded control norm. Thus the stated moment is well-defined. This does not require differentiating the random control with respect to the initial point.

The distinction between a frozen-control derivative and feedback variation is indispensable. For a state-dependent control, differentiating the coupled equation would introduce a term involving the control derivative. Nothing in this argument bounds it. Likewise, the fixed-sign reflection is a constant coordinate change; the proof does not handle time-varying sign reflections or aggregate bounds over an arbitrary number of control sign changes.

The final list of unproved tasks is accurate. The document neither establishes control moments for a trained network nor proves actual fixed signs of backpropagation controls. It supplies no positive-training-time Gaussian/nonaffinity result, population continuation theorem, exact-gradient-descent/gradient-flow limit, or nontrivial feature-learning theorem. Those omissions do not invalidate a theorem explicitly scoped as supporting activation and prescribed-characteristic analysis.

All internally specified mathematical claims survive this audit. The only unverified assertion is the nonessential historical comparison to an undefined alternative activation; the optional wording change above would remove it.

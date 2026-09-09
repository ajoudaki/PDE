# Independent adversarial review

**Verdict: PASS.** I found no substantive correctness or completeness objection to the assertions proved, or explicitly made conditional, in the supplied report. This verdict does **not** establish the global trained-limit theorem that the report explicitly leaves unresolved.

## Input, coverage, and compliance

- Sole mathematical input: `/tmp/proof-f17d445202e2/REPORT.md`.
- Input SHA256: `cd62425a6d8ae0ca7351bb6e71b31cd0b4eb7266263e53e377f976bab261e037`.
- Complete reading coverage: all 643 lines, including the exact finite model, initialization lemma, every section of Part I, every section of Part II, and the concluding scope limitations. An initially truncated display was followed by complete, numbered reads covering lines 1–210, 211–435, and 436–643.
- I read no skills, other files, project notes, previous versions, previous reviews, or websites. I did not communicate with other reviewers or run experiments. The input was not modified. File inspection, hashing, and creation of this review were the only filesystem operations used.
- The review independently checked the mathematical derivations and constants, with particular attention to the functional analysis and the cap-removal argument.

## Substantive objections

None found.

## Audit of the exact finite model and initialization

The raw metric and all three gradient factors agree. In particular, the first block applies the inverse metric factor (n/d) to a Euclidean prediction derivative (n^{-1}b_i^1x_i^T), producing the stated (d^{-1}) factor. The internal matrix and readout factors likewise give exactly the kernel blocks displayed at lines 70–73.

The finite-width global GF argument is valid. Smoothness gives local existence and uniqueness in a finite-dimensional space with a fixed positive metric. The energy identity bounds the accumulated squared speed, and Cauchy–Schwarz makes a trajectory Cauchy at any finite candidate endpoint. Its endpoint is an ordinary finite parameter state, so local continuation prevents finite-time blowup. This makes no width-uniform claim. The GD statement asserts only that every finite update is defined; it does not incorrectly infer stability or convergence.

The initialization induction correctly conditions on preceding layers. The conditional variance bound (3M^2/n) follows from Gaussian fourth moments, and the bounded-diagonal events have probability tending to one because their limiting diagonals are deterministic and finite. Covariance continuity remains valid for singular matrices using positive square roots and the Lipschitz activation.

The net argument also has the stated constants: a (1/4)-net has at most (9^n) elements, the two-vector approximation loses a factor of at most two, and a fixed pairing exceeds five with probability at most (2e^{-25n/2}). The resulting union bound vanishes. It is needed only for the square hidden matrices. Together with (E\|C(0)\|_n^2=n^{-2}), it gives the claimed (O_{\mathbb P}(n^{-1})) backward norms at each fixed depth. Thus every initial hidden kernel block vanishes and the readout block converges to (Q_L).

The order of limits is explicit and respected: this initialization convergence fixes depth and the other finite-model parameters before taking width to infinity. It does not provide a simultaneous growing-depth width limit.

## Audit of Part I

### Scalar recursion and Hermite representation

Equations (1)–(4) are valid, including their constants. The key reciprocal-variance increment is

\[
q_+^{-1}-q^{-1}=\frac{D(q)}{q q_+}.
\]

The lower bound uses (q_+\le q), and the upper bound uses (q_+\ge q/4). The upper square-sum bound (4/\theta) follows directly by telescoping (q_k-q_{k+1}\ge(\theta/4)q_k^2), rather than by an incorrect endpoint estimate for an integral. The lower sum bound follows from the decreasing-function integral as stated. The interpolation bound involving (5L/(1+\theta L)) holds in both regimes (\theta L\le4) and (\theta L\ge4).

The Gaussian integration-by-parts calculations satisfy their integrability and boundary hypotheses: the functions have at most linear growth, their displayed derivatives are bounded, and the polynomial factors are Gaussian integrable. The Hermite completeness argument is adequate, including the finite signed density, the imaginary-argument (L^2) generating series, and Fourier uniqueness by Gaussian convolution. The covariance identity also covers correlations (\pm1). Parseval applied to the two derivatives yields exactly (8); the finite nonnegative derivative sums justify the endpoint derivatives and their continuity. There is no unsupported exchange of a divergent series and an endpoint derivative.

The activation is odd, so the absence of a constant coefficient and the restriction to positive odd powers are correct. This proves the preservation of absolute pairwise separation in (7), including negative correlations.

### Lower conditioning bound

The residual bound (R(q)\le(5/3)\theta^2q^3) uses (E G^6=15). Dividing by (q c(q)^2\ge q/4) gives the logarithmic coefficient (20/3). Summing then gives the uniform first-chaos product lower bound (e^{-80/3}); it does not silently require a depth-independent lower bound on the variances.

The cubic tensor witnesses are valid even when the original Gram matrix is singular. Each witness annihilates the other two tensor vectors and has inner product at least (s_\delta) with its selected vector. Summing the three resulting scalar bounds gives exactly (C^{\circ3}\succeq s_\delta^2 I/3).

The cubic Hermite coefficient in (11) has the correct sign and normalization. Jensen under the probability measure with density (G^2) yields the bound (1/16), and squaring gives (b_3(q)^2\ge q^3/384). Since (q_+\le q), the claimed lower bound on (w_3) follows. Every omitted integer-power Gram term is positive semidefinite, including at negative off-diagonal correlations. The iteration therefore gives (13) and (14). The numerical lower constant in (A) is consistent with (1152\cdot64=73728).

### Matching upper bound and depth asymptotics

Composition preserves the nonnegative odd-power probability series. The curvature estimate uses

\[
b_k\le16\theta^2q_k^2,
\qquad d_k-1\le b_k/3,
\]

where the second inequality follows termwise from odd nonlinear degrees being at least three. The chain-rule identity for (B_L), and hence the factor (e^{128/3}) in (17), are correct. This estimates the full composed kernel at arbitrary finite depth.

The planar example is strictly admissible throughout (0<\delta\le1/4), including the endpoint. The vector (v=(1,-2c,1)) annihilates the degree-one Gram. Direct differentiation of (E_n(c)) gives the displayed second derivative, and the bound

\[
40n^2-16n+8\le54n(n-1),\qquad n\ge3,
\]

is valid. Taylor's integral remainder and positivity of the tensor Gram justify both sides of the bound on (E_n). Summing against the composed-kernel coefficients and dividing by (\|v\|^2\ge3) gives (20). The final upper constant is (36\cdot80\cdot4=11520), as stated. Thus both sharp comparison claims (A) and (B) hold with their stated quantifiers, and the upper example embeds in every allowed dimension.

The reciprocal-increment limit proves (q_\ell\sim(2\theta\ell)^{-1}) for **fixed** positive (\theta). The global arctangent remainder gives the (L^2) projection expansion with cubic residual (-q^{3/2}H_3/3), hence the coefficient (2/3) in (22). The resulting absolute and relative nonaffinity asymptotics, (1/(12\theta\ell^3)) and (1/(6\ell^2)), are correct. These fixed-(\theta) asymptotics are not used to justify the uniform joint bounds.

The affine obstruction has the claimed scope. The equilateral triple sums to zero, so every bias-free linear network has predictions summing to zero and cannot fit three positive labels. At zero population readout, both the readout and hidden directions vanish. The affine field consists of continuous finite products of bounded actions, vectors, and inner products, and is locally Lipschitz in the specified raw coordinates, so stationarity is unique. This does not imply an obstruction at positive mixture.

## Audit of Part II

### State space and fixed-cap fields

The affine product of (L^2) and Hilbert–Schmidt spaces is complete. Bounded base actions need not themselves be Hilbert–Schmidt: only increments are measured that way. Every matrix direction is a finite sum of rank-one Hilbert–Schmidt operators. The proof correctly uses actual Hilbert adjoints and (\|\Delta A\|_{\mathrm{op}}\le\|\Delta A\|_{\mathrm{HS}}).

A cutoff with the stated properties exists by integrating a smooth even cutoff equal to one on ([-1,1]). It satisfies all subsidiary bounds used on (\tau) and (\tau'). The derivatives in (II.5) are correct, so each finite-cap gate induces a globally Lipschitz map from (L^2\times L^2) to (L^2). Combined with the bounded-action and rank-one operations, this makes each fixed-cap raw field locally Lipschitz. No unjustified infinite-dimensional Peano theorem is being invoked: existence on the target interval is expressly assumed.

### Adaptive caps and the reference-only secant estimate

The inequality ( |\partial_zN_R|\le |q|\,|g'(z)|) is valid for all signs. Evenness in (z) permits integration between the absolute values of the two preactivations, where (g) is monotone. The stated extremum of (|z+u|/(1+z^2)) is correct and gives the final bound (1/s(u)).

Crucially, (II.7) remains valid when clipping at the moved point differs from clipping at the reference point. After changing the incoming field at unit Lipschitz cost, one compares (N_{R'}(z,\bar q)) with (N_{R'}(\bar z,\bar q)). On the reference good event, the latter equals the true value and hence equals the other reference cap. The secant bound costs only (\theta M|z-\bar z|). On the bad event the two nonlinear terms together cost at most (2\theta|\bar q|). This verifies the assertion that only the reference law needs a tail estimate. The same reasoning covers an infinite cap on the moved state.

### Arbitrary-depth field estimates

Forward discrepancies in (II.8) use the raw **sum** distance, so telescoping sums of parameter differences do not require an extra layer factor. The backward size and discrepancy exponents in (II.9) are correct. Substitution through the downward recurrence gives (II.10) with slack: cap factors enter as additive forward errors and never multiply prior backward errors. Thus the dependence on (M) is linear at every fixed depth.

Using the rank-one difference bound in each of the (L+1) blocks gives (II.11). Its deliberately large constant covers the residual, forward, and backward factors: the largest displayed power needed is at most (B^{4L+1}), and the coefficients fit under (100(L+1)^2). Neither a bound on individual pointwise fields nor an unassumed competitor tail is used.

### Variable threshold, direction convergence, and continuation

For (u=d+Ae^{-cR}), the choice (M=c^{-1}\log(A/u)) is indeed within ([1,R]) while (u\le Ae^{-c}). It makes the exponential remainder equal to (u), yielding the asserted logarithmic differential inequality. Norm distances of the reference paths are absolutely continuous on compact intervals, so the scalar integration can be performed almost everywhere, avoiding any issue with a decreasing transformation of an upper Dini derivative. It gives the same displayed bound for (u), and hence for (d). For sufficiently large (R), that bound lies below the stopping threshold, closing the argument.

The resulting error decays exponentially in (R) on every separately fixed time interval, with a time-dependent positive rate. Taking (M=R/2) therefore makes both the linearly amplified state error and the exponential tail error tend to zero uniformly. Raw states and raw directions are Cauchy in complete spaces. Uniform convergence of the continuous directions and the integral identities gives a strong (C^1) limiting path.

The true gate is continuous as an (L^2)-valued map, although it need not be locally Lipschitz there. For the potentially difficult multiplier term, a fixed square-integrable incoming field supplies the integrable dominating function; bounded multiplier convergence in measure gives convergence in (L^2) by the subsequence argument stated in the report. The finite forward/backward induction is therefore valid. Alternatively, the infinite-cap/reference comparison directly identifies the limiting direction, with no tail bound on the limiting state.

Uniqueness against a bounded-primal strong competitor follows from exactly the same reference-only estimate after enlarging (B). For continuation from a reached time, the reference initial discrepancy is exponentially small, rather than zero; its logarithm still grows linearly in (R), so the same scalar integration forces convergence on every later compact interval. No restart tail condition is silently imposed on the reached law. Consistent finite-horizon reference hypotheses and overlap uniqueness yield the global conditional solution. The argument neither interchanges (T\to\infty) with cap removal nor requires a positive rate uniform over all (T).

### Counterexamples and hypothesis separation

The rank-one modification in II.5 is an allowed Hilbert–Schmidt increment and sends the selected feature exactly to the constant one. With (C=U^{-1/3}), the squared (L^2) tail is exactly (3/(\sqrt2u)), so a raw norm bound cannot imply (II.4). The example (Z=Q) correctly shows that (II.4) need not imply ordinary exponential incoming-field tails. Finally, (Q=J=U^{-1/3}) is square integrable while (QJ) is not, and (g'(1)\ne0). The report correctly treats these as state-space or differentiability examples, not as laws proved reachable by training.

## Scope and external-theorem audit

The standard facts used—finite-dimensional local ODE theory, completeness of Hilbert and Hilbert–Schmidt spaces, Gaussian moments and integration by parts, continuity of positive matrix square roots, orthogonal projection, elementary tensor Gram positivity, dominated/monotone convergence, and scalar differential-inequality integration—are applied with valid hypotheses. The report supplies the less immediate Hermite/Fourier and net arguments. It does not rely on a specialized trained-network limit theorem without proof.

The two additional reference hypotheses (II.3)–(II.4) remain assumptions throughout. They are not deduced from initialization, raw norm control, or an assumed property of the desired true solution. The report repeatedly and accurately excludes trained finite-width approximation, velocity observations, all-time trained nonaffinity, and a positive sufficient training threshold from its proved conclusions. The universal initialization constants do not become depth-uniform absolute coercivity constants, and the conditional continuation theorem does not become a construction of the canonical initialized population actions.

**Final assessment:** the supplied report is mathematically sound within this explicitly limited and conditional scope. No substantive correction is required for that scope; its explicitly unresolved research target remains unresolved.

# Informed internal review of the small-label endpoint route

Date: 2026-09-20. Scope: mathematical checking of the frozen `ENDPOINT_ROUTE.md`, including the original GF, weighted loss, eventual closure coercivity, all-time comparison, and hidden activity. This is an informed internal review, not an isolated promotion review or a promotion verdict. The reviewer previously developed `OPERATOR_ROUTE.md` and received the supervisor's filter-order observation. No selection route, other study, or other review was read.

## Reviewed snapshot and complete read coverage

The complete reviewed report has SHA-256:

`430c86712686cf7c0d059d6a7a1032d21e637efa3606255f9628387ded34a17e`

`docs/global_nonlinear.md` has SHA-256:

`81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c`

`docs/NOTATION.md` has SHA-256:

`199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b`

Read completely for this review: `ENDPOINT_ROUTE.md`; C.4.5's statement, margins, and limitations, lines 5270–5474; C.4.5.1, lines 5475–6103; C.4.5.2, lines 6104–6595. Already read completely during the preceding operator assignment, with the same unchanged source hash: `docs/NOTATION.md`; C.4.7.9, lines 12084–12554; C.4.7.10.B–C, lines 13161–14245; C.4.7.10.D.3, lines 15146–15528. These complete prior reads were retained rather than needlessly repeated. No C.4.5.3, numerical code, or finite-width endpoint transfer was used as a premise.

The rigorous-math and investigate-conjectures skills and the latter's research-contract/adversarial-audit references were read in the preceding assignment and remain applicable. No numerical training, quadrature, or experimental evidence was added. The numerical margins below were checked directly by exact arithmetic on the displayed constants, without rerunning the report's Python command.

## Finding

I found no unresolved mathematical objection to the theorem as stated for the two orthogonal training inputs with fixed opposite labels `±alpha`, `0<alpha<=10^-3`, exact canonical initialization and hierarchy, and sufficiently large closure order. The report supplies the missing all-time bridge instead of assuming all-order coercivity. Its constants are conservative but have the required strict margins.

The important scope restrictions are real: this is a small-label two-atom result, not the unit-label endpoint theorem, not a neighborhood of general data laws, not a rate in closure order, and not a neural-width/infinite-time result. The report already states these restrictions. Its activity threshold can depend on the fixed nonzero amplitude, although its fitting threshold `p_0` does not.

## 1. Canonical feature orbit and physical-time factors

The feature equations in C.4.5.1 have fixed signs `(1,-1)` and do not contain the target amplitude. Hence their same solution `(w(s),K(s),c(s))` is available for every `alpha`. The proved population symmetry remains `f_1=b=-f_2`; changing the labels changes the scalar clock, not the orbit.

For the probability-weighted unhalved loss,

\[
 L=\tfrac12[(b-\alpha)^2+(-b+\alpha)^2]=(b-\alpha)^2.
\]

The physical readout velocity is

\[
 c_t=-[(b-\alpha)H_1+(-b+\alpha)H_2]
     =2(\alpha-b)(H_1-H_2)/2.
\]

The row and middle velocities have the same factor relative to the feature equation's one-half coefficients. Thus `ds/dt=2(alpha-b)` is the correct clock for all three blocks. There is no sum-loss/mean-loss time error.

Since `b_s>=m>=1/10`, `b(0)=0`, and `b(s)<=s`, the unique level `b=alpha` occurs at `alpha<=s_alpha<=10alpha`. The divergence of the clock integral at that level uses continuity and boundedness of `b_s` on its compact feature segment, exactly as for the unit reference. Therefore all physical times are covered while the feature trajectory remains in `[0,s_alpha]`.

The residual obeys `e_t=-2b_s e`, giving `e<=alpha exp(-t/5)`. Combining `s_alpha-s(t)<=10e(t)` with the feature path-length identity gives raw endpoint distance at most `sqrt(10)e(t)`. These calculations confirm report (7), including its factor of `alpha`. The gradient norm bound less than two holds on the small convex raw ball: `||c||_2<=sqrt(10)alpha`, `||A||<=2+sqrt(10)alpha`. Integration along a straight segment justifies the whole-circle estimate (8).

The construction is therefore the original canonical nonlinear GF for this law. It does not replace training by fixed features or a linear kernel.

## 2. Initial Gram and the amplitude-independent order threshold

The initialized training Gram is an ordinary, unweighted two-by-two matrix:

\[
 G_p^0[a,b]=\langle H_{p,a}(0),H_{p,b}(0)\rangle.
\]

Strong convergence of `B_p` on the two fixed initial lower features gives `G_p^0 -> v I_2`. The limit follows from the canonical initial forward Gaussian law, whose two source variables are independent with variance `q=E tanh^2 G`. The complete C.4.5.1 certificate provides `v>1/5`. Thus eventual minimum eigenvalue at least `3/20` follows with a strict limit margin.

The dictionary, ridge, action contractions, and these initial features do not depend on `alpha`. Consequently a single `p_0` works for the entire stated amplitude interval. No symmetry of the finite-order dictionary and no common whitening across orders are required. The actual coefficient Frobenius metric is retained, and only the valid inequality `||K_p||_HS<=||M_p-D_p||_F` is used.

## 3. The trapping estimate and its normalization

Within coefficient-metric distance `d` of initialization, `||A_p||<=2+d` and each training feature changes by at most `(3+d)d`. Each Gram entry therefore changes by at most `2(3+d)d`, and its two-by-two operator norm changes by at most `4(3+d)d`.

At radius `delta=1/100`, the exact perturbation bound is

\[
 4(3+\delta)\delta=301/2500,
 \qquad 3/20-301/2500=37/1250>1/40=\gamma.
\]

For residual vector `r=(r_1,r_2)`, the normalization check is decisive:

\[
 L_p=|r|^2/2,\qquad
 c_p'=-(r_1H_{p,1}+r_2H_{p,2}),\qquad
 \|c_p'\|_2^2=r^TG_pr\ge\gamma|r|^2=2\gamma L_p.
\]

Together with `L_p'=-||Theta_p'||_p^2`, this implies
`sqrt(L_p(t))<=alpha exp(-gamma t)` and, while in the ball,

\[
 \int_a^b\|\Theta_p'\|_pdt
 \le\sqrt{2/\gamma}\,[\sqrt{L_p(a)}-\sqrt{L_p(b)}].
\]

There is no factor-of-two error from treating the unweighted Gram as a probability-weighted kernel operator: its eigenvalue enters the velocity expression exactly as displayed above. The total pre-exit length is at most `sqrt(80)alpha`, which is strictly less than `1/100` when `alpha<=1/1000`. A first-exit argument is therefore valid. Fixed-order global existence for every bounded-label law is available from the complete finite-closure well-posedness proof; it does not require the time-40 theorem's particular unit-label data class.

The endpoint is Cauchy in the complete coefficient Hilbert space. Its characteristic-class membership can also be checked explicitly: `||c_p'||_infty<=2sqrt(L_p)` gives

\[
 \sup_t\|c_p(t)\|_\infty\le2\alpha/\gamma=80\alpha.
\]

At fixed order, bounded marks and the bounded matrix then give `||w_p'||_infty<=C_p sqrt(L_p)`, an integrable speed. Thus both row increments and readout converge in their bounded characteristic classes as well. A uniform bound for `C_p` is unnecessary for this existence step.

The prediction gradient norms are bounded by `||A_p||||c_p||_2`, `||c_p||_2`, and one. Their square sum is below four throughout the convex trapping ball. Hence the whole-circle tail `18alpha exp(-t/40)` follows from the coefficient-metric length bound, with slack (`2sqrt(80)<18`).

## 4. Why comparison holds on every finite physical horizon

The report correctly avoids applying the time-40 theorem directly to small labels, which are outside that theorem's stated label class. It checks the hypotheses of the comparison proof instead.

The initialized observable spaces are closed `L2` spaces of the generated sigma fields and reduce the two directions of `A_0`. In the canonical feature Picard construction, the initial roots belong to those spaces, coordinate functions such as `j(X,g)` preserve measurability, bounded gates preserve multiplication on the relevant fixed `L2` fields, and ranks remain in the supported closed HS block. The bound `|j(X,g)-g|<=|X|` supplies integrability. Thus the entire small feature segment stays in the spaces where `Q_{l,p}->I` strongly. This resolves the carrier/invariance premise; no operator-norm approximation of `A_0` is needed.

For each fixed physical `T`, continuity supplies compact target sets for the lower forward field on `[0,T] x S^1`, the two training upper backward fields, and the HS derivative. The strong-compact and finite-rank arguments in (21) consequently give all three omitted sources tending to zero. The use of only two backward fields is sufficient: training velocities only integrate over the two training atoms; passive whole-circle predictions need the forward estimate.

C.4.5.2 (R17)–(R18), read in full, applies to the complete unit-reference feature interval up to `b=1`. It gives a common bounded remainder plus Gaussian source for each of the two actual reverse fields at every deterministic feature time, and a supremum of their individual RMS tails over that interval. The small-label trajectory traverses its subset `0<=s<=s_alpha`, so those constants apply uniformly for every physical `t>=0`. This is neither a claim about a random supremum nor an unproved whole-circle reverse-tail bound.

The one-reference subtraction in (23)–(27) then has all required inputs: common action/raw bounds, bounded target readout, the two vanishing action sources, the HS source, and the two target reverse tails. Approximate-trajectory tails are not required. At fixed `T` the quadratic negative cutoff exponent dominates the positive linear Gronwall exponent. Hence taking order to infinity and then cutoff to infinity proves compact-time raw and whole-circle convergence for every finite `T`.

For uniqueness, the same comparison with zero omitted source applies to another strong raw solution from initialization on a finite common interval. Its ordinary finite-horizon raw/readout bounds are enough; global membership in the small trapping ball is not assumed for that competitor. This identifies the feature-orbit solution within the intended canonical strong class, without claiming uniqueness of arbitrary formal hierarchies.

## 5. Endpoint and uniform-in-time passage

Equation (28) correctly combines compact-time error with two order-uniform tails. For the uniform-in-time claim at `t>=T`, compare both paths with their values at `T`, not just with each other's endpoints: integrating the path lengths from `T` to `t` costs no more than their respective remaining-time tail bounds. The result is bounded by the compact-time error plus `18alpha exp(-T/40)+7alpha exp(-T/5)`.

Taking `p->infinity` at fixed `T`, then `T->infinity`, proves both endpoint convergence and uniform-in-time whole-circle prediction convergence. The construction supplies the required tail estimate; there is no illicit interchange of limits. It gives no quantitative order rate because the initial-Gram threshold and compact-source convergence remain qualitative.

## 6. Hidden motion and thresholds

The time `t=1/4` is independent of amplitude. The clock inequality gives
`alpha(1-exp(-2t))<=s(t)<=2alpha t`, so `alpha/3<s(1/4)<=alpha/2`, safely inside the feature expansion interval `s<=1/100`.

The complete C.4.5.1 bounds (R32)–(R34) then imply paired hidden RMS greater than `alpha^2/1800` in each layer. Tanh's one-Lipschitz property transfers first-layer activation motion into a nonzero first-row displacement.

For the middle increment, the two lower initial features are orthogonal, so the squared HS norm of the leading coefficient is exactly

\[
 \frac{q}{16}(\|U_1\|_2^2+\|U_2\|_2^2)
 >\frac{(39/100)(6/100)}{16}>(1/30)^2.
\]

The remainder `45s^4/32` cannot cancel this coefficient for `s<=1/100`; the stated weaker lower bound `||K(s)||_HS>s^2/100` is valid. The readout is nonzero by `||c(s)||_2>=s sqrt(m)`. Thus all three canonical blocks move, and both paired hidden activations move.

Compact-time raw and paired-feature convergence transfers these strict positive margins to all sufficiently large closure orders for each fixed `alpha>0`. The activity order threshold may depend on `alpha`, because its positive margins shrink like `alpha^2`. This does not contradict the amplitude-independent fitting threshold `p_0`. The report distinguishes these thresholds correctly and does not claim nonvanishing activity uniformly as `alpha` tends to zero.

## Remaining qualifications

No correction is needed for the checked formulas or theorem scope. In a synthesis, preserve the distinction between the amplitude-independent fitting threshold and amplitude-dependent activity threshold, and retain the explicit two-atom/small-label restriction. The proof establishes a rigorous nonlinear example with all-time order convergence; it does not establish rapid stabilization with order, the unit-label endpoint, or comparable behavior for a general training distribution.

The report's elementary autonomous least-squares counterexample also checks out: the positive-parameter equilibria are `(1,-1)`, the zero-parameter trajectory ends at `(1,0)`, the added odd cubic vanishes at the two training inputs, and its passive endpoint gap is `1/sqrt(2)`. It illustrates the logical need for the newly proved uniform trapping estimate without claiming to refute the canonical hierarchy.

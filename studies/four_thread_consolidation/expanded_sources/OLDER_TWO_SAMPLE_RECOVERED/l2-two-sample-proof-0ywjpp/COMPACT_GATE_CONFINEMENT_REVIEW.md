# Isolated adversarial review: compact first-gate confinement

## Scope and verdict

Reviewed the entire 451-line, 36,460-byte candidate `/tmp/l2-two-sample-proof-0ywjpp/COMPACT_GATE_CONFINEMENT_TEST.md`. All line references below are to that file. The candidate was the sole mathematical source. The procedural `solve-math-rigorously` skill was read; no other mathematical documents, project files, history, external sources, experiments, symbolic-computation checks, or agents were used. The source was not edited.

**Verdict: the substantive confinement, sharpness, Gaussian-reservoir, finite-width initial-motion, projection-invariant, energy, pointwise-obstruction, and first-activation nonaffinity arguments pass on their intended domains.** I found one small required domain correction: the division in (17) must explicitly assume positive reservoir occupancy, hence `gamma_n > 0`. I also identify two consequential wording ambiguities, concerning the neighborhood quantifiers and the meaning of the antiparallel “target direction.” Neither invalidates the corresponding carefully scoped argument in the body.

This review does not assert a positive or negative result about a full mean-field model. In particular, it supplies no population-network existence result, nonlinear width limit, persistent nonlazy learning theorem, global learning conclusion, or adverse canonical trajectory.

## Required correction and recommended clarifications

### R1 — Explicitly restrict (17) to `gamma_n > 0`

**Location:** lines 283–292, equation (17).

The phrase “on the empirical event `G_1 >= gamma_n I`” does not supply the needed hypothesis: by (7)–(8), that inequality holds for every initialization, including draws with `gamma_n = 0`. The latter event has positive probability at every finite width in the nondegenerate geometry, and `gamma_n = 0` throughout the physical rank-one endpoint geometries. Division by `4 gamma_n` is undefined there.

Replace the lead-in with, for example:

> On the occupancy event `N_s > 0` and `N_o > 0`, set `gamma_n = (2 A^2/n) min(N_s,N_o) > 0`. Since `G_1(t) >= gamma_n I` throughout the trajectory, …

Then (17) is correct with exactly its stated constant. If `gamma_n = 0`, retain the undivided dissipation identity (16), not (17). The surrounding discussion already intends the positive-occupancy restriction, so this is a local hypothesis correction, not a failure of the reservoir estimate or its derivation.

### C1 — Specify which centers and quantifiers are used for weak-decrease neighborhoods

**Location:** line 374.

There are two correct neighborhood arguments, but the sentence “For each fixed finite M, neighborhoods … [have] arbitrarily weak initial loss decrease” does not distinguish them.

For the tail states with `B=M>0`, define `Q=(1,-1)G_1(1,-1)^T>0`. Their dissipation is

\[
 D_M=-\dot L=\frac{8}{n}M^2g'(\pm M)^2Q>0
\]

at every fixed finite `M`. By continuity, a sufficiently small neighborhood of that particular center has dissipation greater than `D_M/2`. Shrinking a neighborhood about that center alone therefore cannot make the dissipation arbitrarily close to zero.

The precise tail-family statement is:

> For every tolerance `epsilon>0`, choose a finite `M` sufficiently large that `D_M<epsilon/2`; then choose an open neighborhood on which `-dot L<epsilon`, with the desired strict first-layer occupancy conditions preserved.

Alternatively, for the **stationary centers with `w=0`** in the preceding sentence, any fixed finite `M` works: for every `epsilon>0`, continuity gives a neighborhood with `-dot L<epsilon`. This latter reading makes the existing sentence valid as written, but does not by itself give large readout norm near the center. The tail-family reading can preserve large norms of both upper parameter blocks.

**Recommendation:** name the center and state the quantifier order. The claimed pointwise obstruction and positive-probability weak-decrease conclusion are valid; this is not a counterexample to them.

### C2 — Keep the antiparallel first-feature direction distinct from the prediction differential

**Location:** lines 237–241 and the status-table entry at line 441.

At antiparallel inputs, a single first-row perturbation produces a first-feature pair proportional to `(1,-1)`. For fixed upper parameters, however, its prediction differential is

\[
 \delta f=\frac{p(z^1_{j1})}{n}(b_{j1},-b_{j2})^T\,\delta W^1_jx_1.
\]

For arctan, evenness of `g'` gives `b_{j1}=b_{j2}`, so this prediction direction is also the label direction whenever the coefficient is nonzero. For softplus that equality need not hold. For instance, a single nonzero connection/readout at a preactivation `t>0`, with `b=0`, gives the direction `(sigma(t),-sigma(-t))`, which is not proportional to `(1,-1)`.

The body correctly discusses the first-feature direction and separately proves representability by adjusting upper parameters. It does not prove that a generic single-row prediction differential for softplus equals the target direction. Recommended replacement for the table wording:

> At antiparallel inputs the first-feature differential lies in the label direction; the explicit upper-layer construction establishes label representability.

If the table was intended to claim a target-aligned prediction differential for both activations, that stronger interpretation requires correction. The first-feature/representability interpretation is sound.

## Coverage map

| Candidate material | Assessment |
|---|---|
| Setup, fixed bump, exact RawGF reduction, lines 18–56 | Verified, including all normalization factors. |
| Frozen set, finite-time non-entry, arbitrary switching, lines 60–85 | Verified for absolutely continuous paths and finite-interval `L^1` controls. |
| Interior and side-strip sharp classification, lines 87–113 | Verified, including equality at the trapping threshold, inactive support endpoints, and both signs of correlation. |
| General rank-one endpoints and physical endpoint subspaces, lines 115–131 | Verified; touching open intervals cannot be crossed. |
| Frozen rows, Gaussian probabilities, empirical/population Gram bounds, lines 133–201 | Verified; positive empirical coercivity remains an occupancy-conditioned statement. |
| Sample-map ranks, actual initial motion, coexistence, lines 205–247 | Verified at fixed finite width with the stated occupancy and continuation qualifications; see C2 for table wording. |
| Top transport and visible/invisible projection, lines 251–269 | Verified. The invariant can be trivial when there is no invisible subspace. |
| SUM-loss dissipation and finite-horizon estimates, lines 271–316 | Every factor checked. Equation (17) needs R1. |
| Activation derivatives, scalar controls, balance defects, lines 320–355 | Verified for arctan and all fixed real softplus shifts `b,c`. |
| Stationary/tail states and positive-probability neighborhoods, lines 359–374 | Pointwise constructions verified; C1 makes the neighborhood quantifiers explicit. |
| Antiparallel arctan dynamics and softplus identities, lines 378–400 | Verified, including the omitted nonnegative first-layer term. |
| First-activation distributional nonaffinity, lines 404–430 | Verified under the supplied measurable continued-path assumption; no existence or learning conclusion follows. |
| Opening and closing status claims, lines 3–14 and 432–451 | Consistent with the scoped results, subject to R1 and the wording qualifications above. |

## 1. Controlled geometry: hypotheses, switching, sharpness, and endpoints

### Exact reduction and barrier argument

The input normalization gives `x_a^T x_b/d=C_ab`. Multiplying the stated row update by `x_b` therefore yields

\[
 \dot z_b=-2\sum_a C_{ba}p(z_a)r_ab_a
          =\sum_aC_{ba}p(z_a)q_a.
\]

There is no missing `n`, `d`, or factor of two in (2). The control reduction is conditional on the specified finite network trajectory and is also meaningful independently for arbitrary controls in `L^1([0,T])`.

Since `p` is smooth and compactly supported, it has a finite global Lipschitz constant `K_p`. For any frozen point `z_*`,

\[
 |\dot z|\le \|C\|K_p|q|\,|z-z_*|.
\]

Writing `u(t)=|z(t)-z_*|` and `v(t)=integral_0^t K|q(s)|u(s) ds`, one has `u<=v`, `v(0)=0`, and `v'<=K|q|v` almost everywhere. The integrating factor forces `v=0`. Reversing time from a proposed finite frozen-set hitting point gives the same argument with integrable reversed control. Thus a path outside the frozen set cannot reach a point where both gates vanish at finite time.

This uses a scalar integral inequality with verified integrability. It does not require a theorem constructing a network flow or a uniqueness theorem for a population model. Support endpoints belong to the frozen set because smooth compact support forces `p(±R)=0`.

On every excursion with `z_1>R`, the absolutely continuous function `z_1-rho z_2` has derivative zero almost everywhere and is constant. Unless the entire path is frozen, `z_2` stays in `(-R,R)` throughout that excursion. A fresh excursion starts at `z_1=R`, hence contributes at most `2|rho|R` above `R`. An excursion already in progress at time zero contributes at most that amount above `z_1(0)`. The negative side and the other coordinate give (1).

Infinitely many excursions, switching accumulations, and controls without an amplitude bound cause no additional term: the argument applies to the excursion containing the time being estimated. It never sums excursion lengths. A time-zero excursion starting exactly at `z_1(0)=R` uses the same boundary-entry formula; this harmless case could be mentioned explicitly in line 83.

### Sharp classification for `|rho|<1`

All possible initial states are covered: doubly inactive; doubly active; or exactly one inactive coordinate, with equality at `±R` included in “inactive.”

For `rho=0`, each coordinate solves an independent scalar gated equation. An active coordinate cannot reach either endpoint in finite time by the same backward barrier argument, and every interior target is reachable using a path that stays a positive distance from the endpoints. The absolute-value supremum is `R`. An inactive scalar coordinate is constant.

For `0<eta=|rho|<1`, the matrix `C` is invertible. Inside any compact subset of the active square, `diag(p)^{-1}C^{-1}` is bounded, so the proposed inverse-control construction follows any smooth finite-length path there with an integrable control.

To make the sharpness construction explicit, let `tau=sign(rho)` and choose small `delta>0`. Arrange a side exit at

\[
 (z_1,z_2)=(R,-\tau(R-\delta)).
\]

Such an exit can be approached from an interior point on the same line using only control 2; throughout this crossing its gate is positive. Continue with only control 2 until `z_2=tau(R-delta)`. The invariant gives

\[
 z_1=R+2\eta(R-\delta).
\]

Every approximating path has its controlling gate bounded below by a positive constant on that path. Letting `delta` decrease proves the supremum `(1+2 eta)R`, without using one limiting control with infinite integral or claiming an attainable frozen corner. Exchanging coordinates proves the assertion for either coordinate.

For an initially inactive coordinate `a`, let `s=sign(z_a(0))` and `k=s(z_a(0)-rho z_b(0))`. While it remains inactive,

\[
 sz_a=k+s\rho z_b,\qquad -R<z_b<R.
\]

If `k>=(1+eta)R`, the infimum of the signed inactive coordinate is at least `R`. Equality allows only a limiting frozen corner, which cannot be reached at finite time. The coordinate therefore stays in the same side strip for every control; sweeping the other coordinate over its open active interval yields exactly `sup|z_a|=k+eta R` and `sup|z_b|=R`.

If `k<(1+eta)R`, the initial condition also implies `k>(1-eta)R`, because `|z_a(0)|>=R` and `|z_b(0)|<R`. Thus the crossing value determined by `k+s rho z_b=R` lies strictly inside `(-R,R)`. One can cross into the square using only the other gate. Before this entry the inactive coordinate is bounded by `k+eta R<(1+2eta)R`; after entry the previously proved universal bound and sharp construction apply. Therefore the stated common supremum is valid over the whole path, including its initial portion.

Starting at `(0,0)` establishes optimality of the additive constant, including `eta=0`. For a fixed initially far-out coordinate, choose the other initial coordinate near the endpoint opposite the desired motion; its traversal makes the outward increment approach `2eta R`. The candidate correctly distinguishes sharp suprema from finite-time attainment.

### `rho=±1`, arbitrary initial state and physical state

Set `rho=epsilon`, `k=z_1-epsilon z_2`, and `u=z_1`. Then

\[
 \dot u=p(u)q_1+\epsilon p(\epsilon(u-k))q_2.
\]

The two coefficients vanish simultaneously exactly outside the open union in (5). For a smooth path `u(t)` on a finite time interval whose image lies in a compact subinterval of one component, with velocity `v=dot u`, set

\[
 D(u)=p(u)^2+p(\epsilon(u-k))^2,
 \quad q_1=\frac{v p(u)}{D(u)},
 \quad q_2=\frac{v\epsilon p(\epsilon(u-k))}{D(u)}.
\]

Here `D` has a strictly positive minimum on that compact subinterval, and these controls realize `dot u=v` with finite integral. At a missing endpoint, including a touching point when `|k|=2R`, both gates vanish and the barrier excludes crossing. This proves the exact connected-component reachable-set classification, including overlapping intervals, separated intervals, touching intervals, and frozen initial points.

Physical coordinates obey `k=0`, because equality in the input inner-product bound gives `x_2=epsilon x_1`. Their active component is just `(-R,R)`, proving (6) and finite-time gate positivity. At `rho=1`, both predictions coincide for all parameters and the two distinct labels cannot be represented. That endpoint fact does not invalidate any controlled geometric conclusion.

## 2. Frozen Gaussian reservoir and finite occupancy

Frozen coordinate pairs have both first-layer gradient factors equal to zero. Thus the entire corresponding parameter row, not merely its two observed coordinates, is fixed. The reservoir really is selected by the prescribed Gaussian initialization and the activation; it is not a separately imposed freeze.

Each same-sign frozen row contributes `A^2(1,1)(1,1)^T/n`, and each opposite-sign row contributes `A^2(1,-1)(1,-1)^T/n`. This gives (7) and eigenvalues

\[
 \lambda_s=2A^2N_s/n,\qquad \lambda_o=2A^2N_o/n.
\]

All other rows contribute positive semidefinite outer products, proving (8) simultaneously at every continued time. Occupancy of one same-sign and one opposite-sign row suffices; occupancy of all four corners is unnecessary. Positive full-Gram eigenvalues could also come from active rows, so positivity of both counts is required for this **reservoir-certified** bound, not a necessary condition for every possible positive full Gram.

The initialization has covariance exactly `C`: the variances are `||x_a||^2/d=1` and the covariance is `rho`. Its displayed density is normalized correctly and strictly positive when `|rho|<1`. Every open corner therefore has positive probability; global sign reversal pairs the two same-sign corners and separately pairs the opposite-sign corners. No equality of the two aggregated probabilities is assumed.

Taking expectation of the unchanged frozen outer products proves (9). This calculation only needs the specified initial marginal law and measurable trajectories. It neither needs independence of evolved neurons nor constructs a limiting population.

The occupancy bound is a valid union bound. In fact, because the same-sign and opposite-sign events are disjoint for a row, the exact probability is

\[
 \Pr(N_s>0,N_o>0)=1-(1-m_s)^n-(1-m_o)^n+(1-m_s-m_o)^n.
\]

The omitted last term is nonnegative. For each count, applying the squared-deviation bound at deviation `m/2` gives failure probability at most `4(1-m)/(nm)`. The union of the two failures gives exactly (10); on their complement both counts divided by `n` are at least their respective probability halves, hence `gamma_n>=A^2 min(m_s,m_o)`. No independence between the two counts is needed. A negative displayed lower probability is merely uninformative, as the candidate says.

At `rho=-1`, every pair remains `(h,-h)`, so the population and empirical Grams have the stated form `alpha [[1,-1],[-1,1]]`. The frozen mass gives `alpha>=A^2 m_F` in population and `alpha>=A^2 N_F/n` empirically. Its nonzero eigendirection is the label direction. Empirically, the reservoir guarantees strict positivity only when `N_F>0`; without it, the displayed lower bound is zero. The opening phrase “rank one” should be read with that population/occupancy qualification. At `rho=1`, the analogous form has plus signs and its positive direction is `(1,1)`, not the label direction.

For (12), a row increment in the input span is `sum_a c_a x_a^T`, its coordinate increment is `d C c`, and its norm squared is `d c^T C c`. Substitution yields exactly `Delta z^T C^{-1} Delta z/d`. The fixed input-orthogonal component contributes no increment. The deterioration as `|rho|` approaches one is real and correctly separated from the correlation-uniform coordinate estimate.

## 3. Initial ranks, nonzero motion, and persistence qualifications

The compact interior square has strictly positive Gaussian mass, and continuity/positivity of `p` on it gives `p_*>0`. Since `|rho|<1` makes the inputs independent, the two rows of the feature differential have rank two.

Conditional on the hidden weights, the variance of the backpropagation coefficient is

\[
 \operatorname{Var}(b_{ja}\mid W^1,W^2)
 =n^{-2}\sum_i (W^2_{ij})^2g'(z^2_{ia})^2>0
\]

almost surely. Every derivative factor is positive for either activation and a Gaussian column is not identically zero almost surely. Dependence between `W^2` and the preactivations does not undermine this argument: there is no cancellation inside this sum of squares. The claim does not require `b_{j1}` and `b_{j2}` to be independent.

Thus both diagonal coefficients in the prediction differential at lines 217–219 are nonzero almost surely, and composing with the rank-two input map preserves rank two. Conditional on hidden weights, `r_a=n^{-1}w^T h^2_a-y_a` is either a nondegenerate affine Gaussian variable or the nonzero constant `-y_a`. Hence both residuals and both backpropagation coefficients are simultaneously nonzero almost surely at fixed finite width.

For an initially doubly active row, define `c_a=p(z^1_{ja})r_ab_{ja}`. The row velocity is `-(2/d)(c_1 x_1^T+c_2 x_2^T)`, which is nonzero by input independence. Its coordinate velocity is `-2C(c_1,c_2)^T`, and its feature velocity is this vector multiplied by the positive diagonal gate matrix. Both vectors are nonzero. This proves a nonzero **pair velocity**, not that each individual coordinate velocity must be nonzero; cross-coordinate cancellation in one component is possible and is not claimed away.

All assertions hold for all initially active rows simultaneously because there are only finitely many rows and samples. They also hold conditional on any positive-probability first-layer occupancy event: intersecting such an event with a probability-one initialization property preserves its probability.

The three-group coexistence bound is another valid union bound, and `N_A/n` has variance `m_A(1-m_A)/n`. A two-direction frozen reservoir plus a separate active row requires `n>=3`; for smaller widths the stated assumptions cannot all hold, and the probability lower bound is simply vacuous. For a finite classical trajectory the parameter vector and its velocity are continuous. Taking the minimum of finitely many short positive intervals preserves the selected gates and nonzero velocities. There is no width-uniform duration or motion magnitude in this reasoning.

The persistence distinctions are correct. No initially nonfrozen pair can become doubly inactive at finite time; individual gate positivity persists in scalar cases; and the explicit side excursion destroys two-gate positivity at finite time for `0<|rho|<1`. With arbitrary neuron-dependent controls one can route every neuron in a chosen initially doubly active group to a fixed side-strip point in a common finite time. Each individual route stays away from the endpoints of whichever gate drives it, so its own integral is finite. No population-uniform control budget or realization by the coupled network is supplied or needed for this controlled counterexample.

### Antiparallel representability and the polynomial argument

For a nonzero vector `h`, the rows `t h^T/||h||^2` and `-t h^T/||h||^2` realize the required preactivation pairs. Substituting the displayed two readout weights gives exactly `(1,-1)` for every strictly increasing `g`; `g(t)-g(-t)>0` ensures a finite denominator. The `n>=2` condition is stated. With arctan a single row and `w=n/arctan(t)` suffice. This is a parameter construction, not a training argument.

At initialization, let `T_j=r_1b_{j1}-r_2b_{j2}`. Conditional on hidden weights it is a polynomial of degree at most two in `w`. Its degree-one part is exactly

\[
 -\sum_i W^2_{ij}[g'(t_i)+g'(-t_i)]w_i.
\]

At least one of these coefficients is nonzero almost surely. Positivity of the bracket is sufficient; the two derivatives need not be equal. A nonzero linear homogeneous component cannot be canceled identically by the degree-two component.

For completeness, the zero-set argument uses only an elementary induction: write a nonzero multivariate polynomial as a polynomial in the last variable. At least one coefficient polynomial in the other variables is nonzero. Its zero set has measure zero by induction. Outside the exceptional set where all coefficients vanish, the last-variable polynomial has finitely many roots, hence zero probability under a nondegenerate one-dimensional Gaussian. Integrating gives zero probability overall. This applies to the independent Gaussian coordinates of `w` conditional on the hidden weights.

Consequently `T_j` is nonzero almost surely, and the active row's velocity is `-(2/d)p(z^1_{j1})T_j x_1^T`; its first-coordinate and first-feature velocities are respectively `-2p(z^1_{j1})T_j` and `-2p(z^1_{j1})^2T_j`. All are nonzero. The statement is conditional on the existence of such active rows in the finite draw. The population active probability alone does not guarantee a finite draw contains one. If desired, antiparallel frozen/active coexistence can be made explicit as probability `1-m_F^n-(1-m_F)^n` for `n>=1`.

## 4. Top transport, memory, and every energy factor

Differentiating the product `W^2 h^1_a`, including both differentiated factors, gives (13): the weight-update term is `-2w_i G_1 diag(g'(Z_i))r`, and the feature-update term is `B_i`. The factor `n` in `(H^1)^T H^1=nG_1` cancels the `1/n` in the weight update. The transport term cannot be omitted when the active first layer moves.

For the frozen restriction, `dot V` is a sum of matrices whose row vectors lie in the column space of `S`. Hence `dot V(I-P)=0`. Also `(I-P)S=0`, and the corresponding first-layer gates are zero, so this invariant affects neither the two forward predictions nor backpropagation through those frozen first-layer rows. Equation (14) is valid at ranks zero, one, and two. If `|F|=rank(S)`, the invisible subspace is zero-dimensional and the invariant is trivial; no nontrivial invariant dimension is guaranteed by merely having two occupied sign groups.

Multiplication of `dot V` by `S`, followed by transposition, gives `dot U_i=-2w_i G_F diag(g'(Z_i))r`, exactly (15). The derivative depends on total `Z_i`, so this does not form a closed equation for the frozen contribution alone.

For the SUM loss, introduce only for this calculation

\[
 H=\sum_a r_ah^2_a,\qquad
 M_2=\sum_a r_a\delta^2_a(h^1_a)^T,\qquad
 M_1=\sum_a r_a\delta^1_ax_a^T.
\]

The ordinary Euclidean gradients and prescribed velocities are:

| Parameter block | Gradient of `L=sum_a r_a^2` | Prescribed velocity | Contribution to `-dot L` |
|---|---|---|---|
| `w` | `(2/n)H` | `-2H` | `(4/n)||H||^2` |
| `W^2` | `(2/n)M_2` | `-(2/n)M_2` | `(4/n^2)||M_2||_F^2` |
| `W^1` | `(2/n)M_1` | `-(2/d)M_1` | `(4/(nd))||M_1||_F^2` |

This verifies (16), including its raw rate two and the absence of a sample-average or half-loss convention. Substitution of the velocities gives exactly

\[
 -\dot L=\frac{\|\dot w\|^2}{n}
          +\|\dot W^2\|_F^2
          +\frac d n\|\dot W^1\|_F^2.
\]

For row `i` of `M_2`, the squared norm is `v_i^T(H^1)^T H^1v_i=n v_i^TG_1v_i`, with the candidate's `v_i`. Summing over rows proves the claimed factor `4 gamma_n/n`. Under R1, time integration gives (17) with denominator `4 gamma_n`. At the rank-one endpoint the full-dimensional `gamma_n` is zero, so (17) is not an endpoint estimate; the full energy identity still holds.

If `gamma_n>0`, `w!=0`, and `r!=0`, choose a nonzero residual coordinate and a nonzero readout entry. Strict positivity of `g'` makes at least one term in the weighted sum positive. This proves the pointwise strict loss decrease. It gives no uniform lower rate when either readout magnitudes or derivatives may degenerate.

Integrating the velocity identity and applying Cauchy–Schwarz in time gives the two inequalities (18), with exactly `sqrt(t L(0))` and `sqrt(n t L(0))`. Moreover,

\[
 \frac d{dt}\|w\|^2
 =-4\sum_a r_aw^Th^2_a=-4n\langle f-y,f\rangle
 \le 2n,
\]

because `||y||^2=2`. This verifies (19). These are horizon-dependent finite-width estimates. The weighted integral in (17) does not remove the factor `(W^2)^T` from the original controls, and no asserted all-time integrability of those controls follows from it.

## 5. Activation shapes and balance defects

For arctan, `g'=1/(1+s^2)>0` and `2|s|<=1+s^2` give `|s g'|<=1/2`. The activation is bounded by `pi/2`, while its derivative tends to zero in both tails. A bounded feature range alone supplies no positive lower Gram eigenvalue; identical rows with identical two-sample values already give a rank-deficient second-feature matrix.

For every fixed real `b,c`, shifted softplus has derivative `sigma(s+b)` strictly between zero and one, asymptotically zero in the negative tail. Its positive tail behaves as `s+b-c+o(1)`. Vertical or horizontal fixed shifts do not remove these tail properties.

For the scalar arctan control example, `d(z+z^3/3)/dt=q`; the primitive is strictly increasing and onto the real line. The stated constant control therefore reaches `M` in unit time. For softplus, `F'(z)=1+exp(-z-b)=1/g'(z)>0`, and `F` is likewise onto. The stated negative constant control reaches `-M` in unit time. Both controls have finite integral and finite support for each chosen finite target. Neither construction is an unbounded network trajectory.

The balance identity follows from

\[
 \frac d{dt}\|w\|^2=-4\sum_{a,i}r_aw_i g(z^2_{ia}),\quad
 \frac d{dt}\bigl(n\|W^2\|_F^2\bigr)
 =-4\sum_{a,i}r_aw_i z^2_{ia}g'(z^2_{ia}).
\]

Subtracting verifies the sign and coefficient in (20). For arctan the defect has derivative `-2s^2/(1+s^2)^2` and limiting values `±pi/2`, establishing the claimed absolute bound. For softplus, substitute `s=log(u/(1-u))-b` and `log(1+exp(s+b))=-log(1-u)` to obtain exactly `D=c-H(u)-bu`. The entropy bounds yield a finite bound for every fixed `b,c`; centered softplus gives `D=log 2-H(u)>=0`.

Neither defect is identically zero. Its sign does not give a sign for the right side of (20), and the absolute-value bound has exactly the factor `4||D||_infinity ||r||_1 ||w||_1`. Controlling a difference of two nonnegative squared norms would in any case not control both norms separately. No conserved balance is being incorrectly inferred.

## 6. Noncanonical pointwise states and probability scope

Section 7's first-layer configuration is feasible for `|rho|<1` and sufficient width: two frozen rows from independent sign groups, plus a distinct active row, can be chosen with strict inequalities. Rank two of `S` permits any second preactivation pair. Explicitly, for `e_+=(1,1)^T`, choose every frozen-supported second-layer row by

\[
 V_i^T=\pm M S(S^TS)^{-1}e_+.
\]

This produces the desired equal pair. It also lies wholly in the visible subspace, so the large second-layer norm in this example need not be hidden in the invariant `(I-P)` component.

With two readout weights `+B,-B` and the others zero, their sum is zero. Thus `f=0`, `r=(-1,1)`, and `L=2`. Equal sample features cancel the two terms of `dot w`; identical second-layer rows and their common derivative factor make `b_ja` proportional to `sum_i w_i=0`. Therefore `dot W^1=0` at that state. Only the `W^2` term survives in (16), yielding exactly (21).

For `B=M`, the readout squared norm is `2M^2`, and the chosen visible second-layer rows scale linearly with `M`. The first-layer parameters, first Gram, and loss stay fixed. Meanwhile `M^2/(1+M^2)^2` and `M^2 sigma(-M+b)^2` tend to zero. This defeats a pointwise upper-parameter bound or a positive uniform learning rate based solely on those first-layer bounds and bounded loss.

Setting `w=0` instead yields `dot W^1=dot W^2=0`, and equal features still give `dot w=0`. These are exact positive-loss stationary states of the specified finite system. Their existence does not show random initialization reaches them.

The parameter distributions at each fixed finite width have everywhere positive densities. Strict saturation/activity inequalities and positive reservoir bounds persist on sufficiently small open neighborhoods of the constructed first-layer state. Continuity of dissipation then gives the weak-decrease neighborhoods with the quantifiers in C1. Such nonempty open neighborhoods have positive Gaussian probability, however small. Intersecting them with the probability-one initial-motion event preserves that probability, and strict active occupancy supplies actual moving first-layer rows.

The zero-probability exact cancellations and the positive-probability neighborhoods are correctly distinguished. These conclusions neither rule out a high-probability learning statement nor exhibit an unbounded single trajectory. They also do not imply that any one tail center has probability bounded below uniformly in width or in `M`.

## 7. Antiparallel top dynamics

Every second preactivation pair is `(t_i,-t_i)`, so the nonzero equal-pair tail example is unavailable. For arctan, oddness gives `f_2=-f_1`, `r=e(1,-1)` and `L=2e^2`.

One can verify the omitted term in (22) without appealing to an unspecified kernel. Put `p_j=p(z^1_{j1})` and `b_j=sum_i W^2_ij w_i/(1+t_i^2)`. Directly from the raw updates,

\[
 \dot w_i=-4e\arctan(t_i),\qquad
 \dot W^2_i=-\frac{4e}{n}w_i(1+t_i^2)^{-1}h^T,\qquad
 \dot h_j=-4e p_j^2b_j.
\]

Therefore the exact coefficient is

\[
 \kappa=\frac4n\left[
 \sum_i\arctan(t_i)^2
 +\alpha\sum_i w_i^2(1+t_i^2)^{-2}
 +\sum_jp_j^2b_j^2\right]\ge0.
\]

This confirms every factor and the direction of the inequality in (22). On each finite classical interval, `kappa` is continuous and finite; the integrating factor gives `e(t)=e(0)exp(-integral_0^t kappa)`. Thus its sign cannot change and its absolute value cannot increase. “Moves monotonically toward 1” includes stationary motion. Vanishing residual at infinite time would require information about the cumulative coefficient that is not supplied here.

The stationary example `w=0,t_i=0` has all three coefficient terms zero and loss two even with positive first-feature mass. In the tails, by contrast, `arctan(t_i)^2` remains nonzero; the candidate correctly avoids carrying the equal-pair argument into this geometry.

For softplus with `b=0`, the identities follow by factoring `1+exp(t)=exp(t/2)2cosh(t/2)` and its negative-argument counterpart. They give exactly (23). The contrast is linear in the `t_i` for fixed readout weights (and bilinear in the pair of upper parameter blocks); this is the appropriate meaning of “affine in the second preactivations.” It is not a statement that the whole predictor is affine in the original input or in all its parameters. The common channel retains the nonlinear `log cosh` term. A nonzero horizontal shift removes the identity `g(t)-g(-t)=t` in general; it does not repair the derivative tail.

## 8. First-activation distributional nonaffinity supplement

The supplement explicitly assumes measurable continued controlled paths with finite-interval integrable controls for almost every initial neuron. A countable intersection over integer horizons gives a full-probability set on which the pathwise conclusions hold for all finite horizons. No population construction is needed to prove an implication for such supplied paths.

Equation (1) gives, for every fixed sample and finite time,

\[
 |Z|\le |Z(0)|+(1+2|\rho|)R,
\]

so `E Z^2<infinity`. For `|rho|<1`, given any threshold, take the initial sample coordinate above both that threshold and `R`, and the other coordinate in an open saturation interval. The event has positive probability by the strictly positive Gaussian density and is frozen. An analogous negative event has positive probability. At `rho=-1` these two events are furnished by the tails of `(G,-G)`. Thus each current sample coordinate has unbounded essential support in both directions, even if all other paths have changed arbitrarily within the controlled rules.

Suppose `phi_1(Z)=a+bZ` almost surely. If `b!=0`, boundedness `|phi_1|<=A` contradicts the unbounded essential tail of `a+bZ`. If `b=0`, the positive-probability frozen events with activation values `A` and `-A` contradict constancy. This proves the nonaffinity statement without an assumption that an active population is still moving.

The least-squares conclusion is also justified. Both `1` and `Z` are in `L^2`, and their Gram matrix is

\[
 \begin{pmatrix}1&E Z\\E Z&E Z^2\end{pmatrix},
\]

whose determinant is `Var(Z)>0`. The quadratic affine-fitting objective therefore has a unique finite coefficient minimizer obtained from this positive definite matrix. If the minimum squared error were zero, its attained affine fit would equal `phi_1(Z)` almost surely, which has just been excluded. Hence the minimum is strictly positive. No heavy closure theorem is necessary beyond this finite-dimensional calculation.

The supplement's written tail cases cover the stated physical domain through `rho=-1` and `-1<rho<1`. If an explicit extension to `rho=1` is desired, use `(G,G)` in exactly the same frozen-tail argument. Distributional first-activation nonaffinity persists in that geometry even though the identical inputs cannot fit the two labels. There is no contradiction: first-activation nonaffinity is a different assertion from prediction learning or second-layer nonaffinity.

The supplement makes no uniform quantitative lower-error claim, no limiting-network existence claim, and no nonlazy or persistent-moving-mass claim. Its conclusion is valid at each stated finite time under its continuation assumption.

## Optional editorial improvements

1. In the introductory rank-one statement, say “rank one in population, and empirically with positive coefficient whenever the relevant mass is present.” The body already gives the correct occupancy-qualified bounds.
2. Mention a time-zero excursion starting exactly at a support endpoint in the excursion proof. The existing boundary-entry estimate covers it without modification.
3. State the minimum width `n>=3` when simultaneously choosing two frozen sign groups and a distinct active row in Section 7. It is already implicit in that construction's premises.
4. Make the antiparallel finite-draw occupancy qualification explicit alongside its polynomial motion proof. The closing table already includes the intended conditioning.
5. If presenting a completely symmetric endpoint appendix, add the `rho=1` Gram and frozen-tail observations described above. They are not needed for the candidate's excluded-identical-input application.
6. In the status table, describe the population bound as “an expectation bound for any supplied measurable evolved population with the stated Gaussian initial law.” This avoids reading “unconditional population bound” as an existence assertion; the body already excludes that inference.

No change to the confinement constants, sharp classification, raw energy coefficients, Gaussian polynomial argument, stationary constructions, or first-activation nonaffinity proof is required. Preserve the current distinctions between abstract controls and coupled RawGF, between initial finite-width motion and limiting behavior, and between pointwise examples and canonical trajectories.

## Source integrity

- Source SHA-256 before reading:
  `7ea96a3f240363dce497ef214ccc6df4326aeff3dce126707c99e5e6a2091a68`
- Source SHA-256 after completing the review:
  `7ea96a3f240363dce497ef214ccc6df4326aeff3dce126707c99e5e6a2091a68`
- Before/after comparison: identical; source integrity verified.
- Source edits: none. The only newly written mathematical artifact is this requested review.

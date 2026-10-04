# Internal check of the actual-carrier near-cap estimate

2026-10-01. Scoped internal mathematical check, not promotion review.

Scientific inputs read in full: `RESOLUTION_UPPER_ROUTE.md` (including its final equations (21)–(22)), `FITTING_AND_THRESHOLD.md`, `CLIPPED_POPULATION_ROUTE.md`, `CONCENTRATION_ROUTE.md`, and `BIAS_CAVITY_ROUTE.md`. I also read the repository `AGENTS.md` and the required solve-math-rigorously skill. No other study, sibling route report, manuscript, history, experiment, or external scientific source was used. This report is the only file written.

**Verdict: PASS for the near-cap proposition (2) on its stated event, and PASS for the adaptive linear estimate (22).** The detailed estimates below verify the width and activity factors that were compressed in the route. There is one explicit correction to the auxiliary probability claims: the operator cutoff must be sufficiently large. A fully explicit sufficient condition is **K ≥ 6**, with **L ≥ K** when using the common event. Merely K > 1 does not justify the claimed O(1/n) exceptional probability. The two minor domain/activity clarifications below also should be reflected in the route's wording. None requires a new density hypothesis to prove (2).

These passes do not establish the nonlinear remainder (20), a population bias rate, or a density estimate along arbitrary interpolated Gaussian histories.

## 1. Event, activity, and nondegeneracy checks

The column-cavity initialization event is independent of the deleted Gaussian column and of A_{0,j}: the initial rank memories vanish, so neither enters its initial forward features. The cavity flow itself can depend on A_{0,j}; the proof does not need independence at positive time.

The initialization feature difference has ordinary norm at most L **on E_j**, and the initial Gram difference is at most C L/sqrt(n). Thus all values of the first Gaussian coordinate and all columns in the closed radius-L ball have a common fitting tube, once n is large. No first-matrix norm bound is needed for this statement because tanh and its relevant derivatives are bounded. This uniformity is what makes the later entire-line and interval arguments valid.

The route's first sentence in Section 2 says this bound holds “on C_j”; that domain must read “on E_j” or additionally impose the column-norm bound. C_j alone contains no bound on the deleted column.

The bounded exact residual kernels imply |rho'| ≤ C rho whenever rho > 0. Together with fitting this gives

    Y exp(-C t) ≤ rho(t) ≤ Y exp(-lambda t),

and hence activity comparable to Y min(t,1), uniformly over the conditioned roots. This proves positivity at positive finite times and makes the full and cavity activities comparable.

Activity comparability does **not** imply pointwise comparability of their rates. In Section 3.1, use the explicitly allowed sum rho + rho^c in the comparison inequalities. Its integral up to t is at most C s^c(t), which is all Gronwall needs. For the directional estimates below, first use the full flow's activity q(t) = integral_0^t rho; perform integrations with dq = rho dt; only afterward replace q(t) by its comparable cavity activity s^c(t). One should not literally substitute s = s^c into ds = rho dt with rho belonging to the full flow.

The backward norm lower bound (6) is valid for **each** training sample. Indeed,

    ||w^c||_2/sqrt(n) ≥ ||f^c||_m ≥ Y - rho^c
      ≥ Y(1-exp(-lambda t)) ≥ lambda s^c.

The last inequality uses the integrated upper fitting bound. With ||z_a^c||_2/sqrt(n) ≤ D and ||w^c||_infinity ≤ 2s^c, the squared readout mass on |z_a^c| > R is at most 4(s^c)^2 D^2/R^2. Choosing R^2 ≥ 8D^2/lambda^2 leaves at least lambda^2(s^c)^2/2 on the complement, where the gate is at least sech^2(R). Thus sigma = ||d_a^c||_2/sqrt(n) lies between c s^c and 2s^c, with c > 0 independent of width, time, and the conditioned roots. The possibly very small c can be accommodated by a fixed small-label restriction.

## 2. Column removal and the first Gaussian direction

For deletion of a whole lower column, the direct forward difference is gamma h_{aj}, of norm at most L. The direct transpose difference occurs only at lower coordinate j. Its **clipped** difference is bounded by 2, irrespective of the size of the uncut coordinate. All remaining differences use the unchanged bounded operator and the global post-gate clipping inequality.

Use ordinary vector-state distances, sqrt(n) times the clock distance, and R = sqrt(n)||r-r^c||_m. The readout-Gram source from the bounded forward difference is O(1/sqrt(n)) before residual rescaling. A direct hidden-kernel matrix source is also O(1/sqrt(n)): it pairs a vector of norm O(sqrt(n) s) with gamma times one bounded lower coordinate, then divides by n. A direct clipped lower-coordinate source has the same normalization. Therefore the displayed damped comparison system with sources C(rho+rho^c) is justified. Integrating R first gives N + integral R ≤ C s^c.

The forward difference itself is O(1+N); multiplying it by the upper readout bound O(s^c) gives

    ||d_a-d_a^c||_2 ≤ C s^c.

The rank part of the lower carrier is bounded coordinatewise by C(s^c)^3, because |k_{bj}| ≤ 1 and |v_b^T d_a/n| ≤ C(s^c)^3. This proves both parts of (7).

For the first-row scalar xi, the initial ordinary sensitivity of A is 1, that of the keys is bounded, and the others vanish. Rescaled pairwise stability gives bounded total state sensitivity and integral sqrt(n)||partial_xi r||_m ≤ C s^c. The A increment has sensitivity O(s^c), the readout has sensitivity O(s^c), and the forward field has sensitivity O(1). Thus partial_xi d_a has ordinary norm O(s^c). At coordinate j, multiplication by the initialized column costs at most L; differentiating its rank correction contributes only O((s^c)^2) or smaller. Consequently (8) follows, uniformly along the entire xi-line. Every training input is nonzero by the Gram gap, so partial_xi alpha_{aj} remains positive after the fixed activity bound is reduced.

## 3. Explicit audit of (11)–(14)

Fix the cavity and the terminal time used to select its unit vector v. This vector is held fixed when differentiating the full trajectory at all earlier times. Write delta = n^(-1/2) and q = integral rho for the full trajectory in this section. Use the route's ordinary sensitivity norms a,b,c,k and its rescaled scalar sensitivities T,R. Constants absorb the fixed number of samples.

The matrix derivative is

    partial_zeta W_0 = delta v e_j^T,
    ||partial_zeta(B-W_0)||_op ≤ C delta(c+q^2 k).

The latter bound follows by differentiating v_b k_b^T/n, using ||k_b||_2 ≤ sqrt(n) and ||v_b||_2 ≤ Cq^2 sqrt(n). Forward multiplication by h_a cancels the delta in the rank term, whereas the initialized derivative uses only |h_{aj}| ≤ 1. Hence

    Z ≤ C(a+c+q^2 k+delta),    D ≤ b+CqZ.

For a sum over samples the explicit forward source is C delta, rather than a literal coefficient-one delta; this is absorbed by the route's fixed-data constants.

The explicit transpose source is

    (partial_zeta W_0)^T d_a
      = delta e_j(v^T d_a),

whose norm is O(q), not O(q delta). Let E denote the summed ordinary lower-signal sensitivity. The clipping inequality yields

    E ≤ C[a+D+q(c+q^2 k)+q].

Differentiating the four state equations now gives

    a' ≤ C rho E + CqR,
    b' ≤ C rho Z + CR,
    c' ≤ C rho D + CqR,
    k' ≤ C rho(a+k+q^2 T) + Cq^2 R,
    T' ≤ R.

The residual-difference sources in these lines use, respectively, ordinary base norms O(q sqrt(n)), O(sqrt(n)), O(q sqrt(n)), and O(q^2 sqrt(n)). This checks every sqrt(n) cancellation in (12). The final key norm follows from ||h_b-k_b||_2 ≤ Cq^2 sqrt(n); using only the cruder bounded-key estimate would lose the displayed powers of q.

For the residual derivative, the ordinary output derivative in the concentration note equals d_b because the top clip is inactive. Set U = psi(alpha_b) multiplied coordinatewise by ell_a. Then ||U||_2 ≤ Cq sqrt(n), |U_j| ≤ 1, and ||partial_zeta U||_2 ≤ E+Ca. Differentiating the hidden-motion kernel d_b^T B U/n, and multiplying by sqrt(n), gives the following bounds:

| Differentiated factor | Bound after multiplying the scalar kernel derivative by sqrt(n) |
| --- | --- |
| d_b | CqD |
| rank part of B | Cq^2(c+q^2 k) |
| initialized part of B | Cq delta |
| U | Cq(E+a) |

In particular the initialized term is exactly (d_b^T v)U_j/n after rescaling, bounded by Cq/sqrt(n). It does not have an extra sqrt(n) loss.

The readout Gram contributes CZ. The value kernel contributes C[qD+q^2(a+k)]. For the clock-memory kernel, use the stronger base bounds

    |d_b^T v_c/n| ≤ Cq^3,
    |(h_c-k_c)^T h_b/n| ≤ Cq^2.

Its rescaled derivative is bounded by

    C[q^4 D+q^3 c+q^3(a+k)+q^5 T],

which is smaller than the bound used in the route for q ≤ 1. The non-readout terms multiplying the residual sensitivity are O(q^2) or smaller. After absorption into the initial readout coercivity, substitution of Z,D,E yields precisely

    R' ≤ -kappa R
         +C rho[a+c+qb+q^2(k+T)+delta+q^2].

Thus (13) retains both its damping and its actual source scaling.

Here is an explicit closure of the integral estimates. Put U_0 = a+b+c+k+T and I = integral R. Integrating the damped residual inequality first and substituting in the sum of state inequalities gives

    U_0(t) ≤ C integral_0^t rho U_0 + C(q^2+q delta),

so U_0 ≤ C(q^2+q delta). The same initial bound gives I ≤ C(q delta+q^3), since the term q^2 delta is bounded by q delta for q ≤ 1. In the first state equation, the integral of the explicit source rho q is O(q^2), all terms containing U_0 integrate to O(q^3+q^2 delta), and integral qR ≤ qI. Hence a ≤ Cq^2. Substitution into the readout and backward-field bounds gives b+D ≤ C(q delta+q^3); then

    c ≤ C(q^2 delta+q^4),
    k ≤ Cq^3,
    T ≤ C(q delta+q^3).

The k estimate follows by integrating its q^2R term as at most q^2 I and applying Gronwall to its rho k term. These are all the bounds in (14). Replacing q(t) by the comparable cavity activity s^c(t) is legitimate at the end.

For completeness, differentiation of the rank correction at coordinate j is bounded by

    C[q^3 k + delta q c + delta q^2 D],

and therefore by C(q delta+q^3). The initialized part gives sigma + O(q delta) by (7), while the learned d derivative costs at most L D. This proves (10), including the error small relative to sigma after choosing n large and the fixed activity sufficiently small.

The differential computations can be made with difference quotients on the cutoff interval. The vector field is locally Lipschitz, and all the preceding estimates are uniform there. Passing to weak derivatives, or using the almost-everywhere derivatives of the scalar parameter maps, does not require differentiating a clip selector.

## 4. Conditioning and strip crossings

For the xi argument, E_j is independent of xi, so its whole real line is available. On either connected region alpha ≥ 1 or alpha ≤ -1, and for either fixed cap strip, (8) makes the derivative of X have a fixed sign and magnitude at least c_a. Composing X with projection to that strip produces an absolutely continuous function with the same derivative on its preimage and zero derivative outside. Its total change is at most the strip length 2u. Hence that preimage has length at most 2u/c_a. Exact strip endpoints do not create positive-measure exceptions: an absolutely continuous function has derivative zero almost everywhere on a level set, incompatible with the established nonzero derivative there. The bounded standard Gaussian density then gives Cu.

For the zeta argument, condition on the cavity and gamma_perp, **not** on the column-norm cutoff. The remaining scalar keeps its ordinary N(0,1) density, while the cutoff restricts its integration domain to an interval. The cavity direction is measurable without the removed column, so this Gaussian decomposition is valid even though the direction was chosen using the terminal cavity backward field.

On the cap strips with |alpha| ≤ 2, sigma ≥ c s^c and (10) give

    partial_zeta X ≥ psi(2)c s^c
       -C(s^c/sqrt(n)+(s^c)^2+(s^c)^3)
      ≥ c' s^c.

The O((s^c)^2) term is the gate derivative times the bounded carrier p on this gate region. Independently, |X| ≥ 3/4 and p = sigma zeta + O(s^c) imply |zeta| ≥ b/s^c after decreasing the fixed activity ceiling.

A unit interval that contains a contributing point with |alpha| < 1 has |alpha| ≤ 2 on its **intersection with the cutoff interval**, because |partial_zeta alpha| ≤ C(s^c)^2 there. Only this intersection is needed; no derivative estimate outside the cutoff is assumed. The same strip-projection argument gives length at most Cu/s^c on each such interval. Summing the Gaussian density suprema over the intervals meeting |zeta| ≥ b/s^c gives at most C exp(-c/(s^c)^2). Thus the bound is

    (Cu/s^c) exp(-c/(s^c)^2) ≤ C'u,

uniformly at small positive times as well as at late times. This verifies (19) and completes (2). A previously deleted upper row leaves the entire argument in its coordinate-orthogonal subspace; its absent backward coordinate stays zero, so the selected direction belongs to that subspace.

## 5. Explicit cutoff correction and the common event

The Gram comparison and column-length estimates supporting (3) are valid. The Gaussian norm assertion needs a sufficiently large K, as in the assigned concentration note; the statement “K > 1” is insufficient as a stated hypothesis.

An explicit sufficient cutoff can be proved without importing another theorem. Choose 1/4-nets of both unit spheres, each with at most 9^n points, by the usual disjoint-ball volume argument. Approximation of the two vectors in a bilinear form gives

    ||W_0||_op ≤ 2 max_{x,y in the nets}|x^T W_0 y|.

For each fixed pair, x^T W_0 y is N(0,1/n). The scalar Gaussian tail bound and the union bound yield

    P(||W_0||_op > K)
      ≤ 2 exp[n(2 log 9 - K^2/8)].

The exponent is negative for K ≥ 6. Deleting a row or column cannot increase operator norm. This supplies the required O(1/n) bound for all relevant operator events. With the fixed larger Gram margin, (3) and the common-event failure estimate follow for this explicit choice. For the common event take L ≥ K ≥ 6. Its inclusion in every E_j follows deterministically from column norm ≤ K and the uniform O(K/sqrt(n)) Gram comparison; no union bound over the cavities is needed.

This is an explicit correction to the ancillary probability claim, not an additional condition needed for the event-restricted inequality (2), which remains valid for any fixed cutoff for which its event is defined.

## 6. Adaptive linear-response estimate and its limits

Equations (21)–(22) also pass. With the cavity and prescribed scalar histories fixed, the omega = 0 base trajectory is independent of eta. Its tangent coefficient matrix has operator norm at most C rho. The insertion for the term omega eta_b r_b is bounded, measurable in source time, and independent of eta. The output map is the lower activation derivative followed by the appropriate sample projection.

Writing the kernel as output(t) times evolution(t,s) times insertion(s), the evolution norm is bounded by exp(C integral rho), and its terminal-time derivative is bounded by C rho(t) times that constant. The output gate derivative has operator norm at most C rho(t), because each row of the clipped A velocity has norm at most C rho(t). Its integral is bounded. These facts prove (21) without requiring source-time variation of the clip selector.

For any real, possibly nonsymmetric matrix K, Gaussian fourth moments give exactly

    Var(omega^T K omega)
      = [tr(KK^T)+tr(K^2)]/n^2
      ≤ 2||K||_op^2/n.

Apply this at t=s and to the terminal-time derivative, then use the fundamental theorem for the absolutely continuous kernel and Minkowski. The L2 norm of the terminal-time supremum of each centered quadratic kernel is at most C/sqrt(n).

For every measurable eta(omega) within its stated envelope, the absolute supremum in (22) is bounded pathwise by the integral of 2s(s)|r_b(s)| times those kernel suprema. Minkowski gives C/sqrt(n) times the deterministic envelope integral, which is O(S^2). Thus no independence between eta and omega is used or needed.

The subtracted trace expression in (22) is itself random when eta depends on omega. Accordingly, (22) is a root-width approximation to an adaptive trace functional, not concentration around a deterministic mean. Its displayed formula and proof respect that distinction; the phrase “centered concentration” in the claim summary should be read only in this kernel-by-kernel sense.

The actual-carrier density estimate supplies almost-everywhere absence of base-time clip corners on a common good event and hence a legitimate first variational equation. It supplies neither density along arbitrary covariance interpolations nor density for all forced systems with frozen empirical histories. The route explicitly acknowledges that limitation. Neither the first-tangent construction nor (22) controls the nonlinear, left-weighted remainder (20), restores the empirical scalar histories quantitatively, or identifies the adaptive trace/covariance law with the population law. Those remain substantive open obligations.

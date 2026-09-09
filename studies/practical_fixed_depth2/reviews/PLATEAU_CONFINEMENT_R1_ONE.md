# Isolated review of PLATEAU_CONFINEMENT.md

**Verdict: NOT PASS as written.** The deterministic confinement theorem in Sections 1–5 passes this audit. One substantive missing hypothesis remains in the population implication in Section 6.

This review used only the supplied report as its project source, read no linked geometry or contract files or other reviews, and ran no experiments. It assesses the report's explicitly partial theorem, not a population existence theorem or an unstated training limit.

## Substantive objection: almost-everywhere differentiation does not give absolute continuity

Section 1 correctly assumes an absolutely continuous solution. Section 6 instead states its population implication under the conditions that “the row equation is justified almost everywhere” and the coefficients are locally integrable almost surely. If the first condition means that the displayed differential equation holds almost everywhere in time and population sample, these conditions do not suffice. Local absolute continuity of the row paths, or the corresponding integral identity, must also be required. It cannot be deduced merely from the integrability of the right-hand side and existence of the derivative almost everywhere.

Here is a counterexample to the implication with exactly those stated conditions. Take

\[
d=3,\qquad u_i=e_i,\qquad \delta=\tfrac12,\qquad
g(s)=(1-|s|)_+,\qquad a_i(t,\omega)=0.
\]

These vectors satisfy the strict separation condition. Their Gram matrix is the identity, so \(\kappa=1\), \(B_\delta=2\), \(D_\delta=4\), and \(R_\Gamma=9\). Let \(Z\) be a standard Gaussian vector in \(\mathbb R^3\), and let \(C:[0,1]\to[0,1]\) be the Cantor function. It is continuous, satisfies \(C(0)=0\), \(C(1)=1\), and has derivative zero almost everywhere: it is locally constant off the measure-zero Cantor set. Define

\[
w(t,\omega)=Z(\omega)+12C(t)e_1.
\]

For every sample, the derivative is zero almost everywhere in time, so (1.1) holds almost everywhere. The coefficients are locally integrable almost surely, and the initialization is Gaussian. Nevertheless, on the positive-probability event \(\{\|Z\|\leq1\}\),

\[
\|w(1)\|\geq12-\|Z\|\geq11
>10\geq\|w(0)\|+R_\Gamma.
\]

Thus the population envelope is false under an interpretation that requires only the stated almost-everywhere differential identity. These paths are not absolutely continuous, which is precisely the missing condition; this counterexample does not challenge the deterministic theorem.

**Minimal repair.** Require that, for almost every population sample, the row path is locally absolutely continuous on its existence interval, satisfies (1.1) almost everywhere in time, and has locally integrable realized coefficients. Equivalently, require the pathwise integral equation with those coefficients. With that explicit premise, the population implication follows by applying Sections 1–5 on finite subintervals. No uniform coefficient-integral bound is needed. The asserted transfer of finite \(p\)-th moments, \(p\geq1\), then follows from the displayed elementary inequality.

## Audit of the deterministic proof

- **Freezing and solution-dependent controls:** Correct. Fixing the realized coefficients produces a time-dependent vector field with an integrable spatial Lipschitz bound. The integrating-factor argument establishes uniqueness after the meeting time, and time reversal establishes uniqueness before it. The constant path at a point where all relevant gates vanish is therefore the entire realized path. It need not solve the original feedback or coupled system; uniqueness is used only for the auxiliary equation with the coefficients fixed.
- **Nonconstant-path freezing and strip boundaries:** Correct. A nonconstant path can never reach the set where all relevant closed-gate inequalities hold. Outside the union of double closed strips, exactly one open strip is present. The inequalities excluding every other closed strip persist locally, which makes its index constant on each connected component. Motion there is along one unit vector, with signed coordinate displacement at most two. Continuity gives the same estimate at the component endpoints.
- **Planar lemma:** All three assertions follow. A component of the complement of the visited double-strip set has an endpoint in that set, including components adjoining the original time endpoints. Infinite switching causes no difficulty. For two gates, visiting both closed strips while avoiding their intersection contradicts the fixed-index property; constant trajectories are also covered.
- **Double-strip radius and rank two:** Correct. Each pair is linearly independent. The inverse two-by-two Gram estimate gives the stated radius. In rank two every pair spans the same plane, so the planar lemma applies. Restoring the fixed orthogonal component via the displayed triangle inequality preserves the additive constant.
- **Last activation times:** Correct. Nonempty open-gate time sets have last times at which the corresponding closed-strip inequality holds by continuity. After the smallest such last time, that gate vanishes. Its possible value at the suffix's initial endpoint does not affect the integral equation. The remaining two closed strips are visited on the suffix, so the planar lemma bounds its planar projection, including its start. Ties cause no gap; when the suffix is a single point, both closed-strip inequalities hold directly.
- **Rank-three transverse and Gram bounds:** Correct. The transverse component is fixed on the suffix. The third closed-strip inequality at its start bounds that component by \((1+D_\delta)/\eta_k\). In the variational expression for \(\eta_k^2\), every coefficient vector has its \(k\)-th entry equal to one, so its squared norm is at least one and the Gram lower bound gives \(\eta_k\geq\sqrt\kappa\). Restoring the ambient orthogonal component gives the asserted additive envelope. If one gate never opens, the two-gate reduction gives the smaller bound.
- **Subintervals and backward time:** Correct. Restriction and time reversal preserve absolute continuity, the gate form, and integrability of the realized controls.

The report's references to its particular \(\phi\), raw-flow normalization, and external contract identify intended applications. Those external identifications are not independently established by the supplied text and were not imported as premises for this review. Conditional on the row equation actually having the stated form and regularity, they introduce no additional defect in the confinement proof.

The final Euler-step observation is valid whenever the gate is nonzero at a reachable starting coordinate: scaling its control gives an arbitrarily large single step. The allowed degenerate choice \(g\equiv0\) makes all Euler steps zero, so that observation should be understood as the absence of a general discrete guarantee, rather than a claim about every allowed gate. This qualification does not affect the continuous-time theorem or the substantive objection above.

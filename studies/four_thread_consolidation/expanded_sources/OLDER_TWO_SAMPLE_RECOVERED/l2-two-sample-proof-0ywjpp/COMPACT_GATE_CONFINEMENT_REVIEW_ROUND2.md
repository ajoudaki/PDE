# Isolated adversarial referee report — round 2

## Provenance, isolation, and verdict

The sole mathematical source reviewed was `/tmp/l2-two-sample-proof-0ywjpp/COMPACT_GATE_CONFINEMENT_TEST.md`, read in full, including all 451 lines, equations (1)–(23), and the final status table. Its size was 37,728 bytes. The SHA-256 computed from the source bytes was:

```text
bbce988f9082d2137d822491008dc7b60f74091017436a15944797b1ccefd2c3
```

This exactly matches the hash supplied in the review request. A second SHA-256 check after writing the report returned the same source hash. The only additional file consulted was the procedural skill `/etc/codex/skills/solve-math-rigorously/SKILL.md`. No history, other project documents, earlier reviews, agents, experiments, or external mathematical sources were consulted. No source edits were made. The arguments below were checked directly from the displayed definitions and dynamics. References to source lines refer to this exact version. Statements about the author's earlier process or an unprovided original prompt are not independently certified.

**Isolated verdict: PASS as a scoped confinement/reservoir lemma and diagnostic test, with no required mathematical corrections.** The conclusions have the qualifications needed for their proofs: locally integrable abstract controls; continued trajectories; explicit finite occupancy events; fixed, nondegenerate geometry for two-dimensional coercivity; and finite-width, local assertions for actual initialization motion. Section 9 proves first-activation distributional nonaffinity for a supplied measurable controlled population. None of these conclusions is an existence, convergence, persistent-nonlazy, or global mean-field theorem.

Required findings: **none**. In particular, I found no missing SUM-loss factor, invalid sharpness case, unjustified unconditional empirical Gram bound, or illicit inference from nonzero finite-width motion to population-scale motion.

Optional findings:

1. Section 7 could display its fixed-width neighborhood quantifiers and a positive-loss neighborhood condition explicitly. Both follow from its existing argument; this is clarification, not a repair. The precise statement is supplied below.
2. Section 9 can be strengthened to a time-uniform positive lower bound on the population affine-fit error using only the unchanged frozen subset. The derivation below is optional; the stated fixed-time result is already correct.

## 1. Controlled barrier, sharpness, and endpoint geometry

### Activation and reduction to the two-coordinate system

The assumptions on the smooth bump imply that \(p\) and \(p'\) are bounded, \(p(\pm R)=0\), and \(p>0\) exactly on \((-R,R)\). Its integral is odd, bounded by \(A\), strictly increasing in the interior, and constant on each saturation tail. It is not globally affine. Fixing \(p,R\) independently of width and geometry gives precisely the fixed activation described in the source; this alone does not settle any broader activation-design requirement.

Multiplying the stated first-row update by \(x_b\) gives

\[
\dot z_{jb}^1=-2\sum_a C_{ba}r_ap(z_{ja}^1)b_{ja}
=\sum_a C_{ba}p(z_{ja}^1)q_{ja}.
\]

Thus (2) has the correct sign, input normalization, and factor 2. No additional factor of \(n\) belongs in it. For the controlled test, the hypothesis is \(q\in L^1([0,T])\) on each finite interval under consideration, with no common bound on this norm over controls. Finite classical network states give continuous effective controls on compact trajectory intervals. These facts make no global \(L^p(0,\infty)\) assertion about \(q\).

### Frozen set and excursion bound

Fix \(z_*\in\mathcal F\). Global Lipschitz continuity of \(p\) gives

\[
|\dot z(t)|\le K|q(t)|\,|z(t)-z_*|.
\]

If \(z(0)=z_*\), let \(M(t)=\int_0^t K|q(s)|\,|z(s)-z_*|\,ds\). Then \(|z(t)-z_*|\le M(t)\), \(M(0)=0\), and \(M'\le K|q|M\) almost everywhere. Multiplication by the integrating factor proves \(M=0\). Reversing time on a finite interval gives the same conclusion backward from any proposed hit of a frozen point. Therefore a path outside \(\mathcal F\) cannot reach it in finite time. This also covers support endpoints and does not require a separate population uniqueness result.

On a connected component of \(\{t:z_1(t)>R\}\), the equation gives \(z_1-\rho z_2=\text{constant}\). A nonfrozen path has \(z_2\in(-R,R)\) there, since otherwise it would lie in \(\mathcal F\). An excursion entering from the boundary consequently satisfies

\[
z_1(t)\le R+|\rho|\,|z_2(t)-z_2(\text{entry})|
\le R+2|\rho|R.
\]

An excursion already outside at time zero instead has upper bound \(z_1(0)+2|\rho|R\). The same calculation applies to negative excursions and to the other coordinate. This proves both inequalities in (1), including initial equality at a support endpoint. It is a bound on each excursion separately, so infinitely many returns or switches cannot accumulate an additional outward increment. No denominator \(1-|\rho|\) is introduced.

### Complete sharpness classification for \(|\rho|<1\)

All cases at source lines 87–113 check out. The suprema are coordinatewise suprema over controls and finite times, not a claim that both coordinates can simultaneously realize their maximal magnitudes.

For \(\rho=0\), an active coordinate obeys a scalar equation with a Lipschitz gate vanishing at the endpoints. The preceding barrier argument excludes a finite-time hit of either endpoint. Every compact subinterval of the active interval can be traversed with finite-integral control. An inactive coordinate has identically zero velocity. This establishes the stated scalar suprema.

For \(0<\eta=|\rho|<1\), the interior control matrix is invertible. Any smooth path contained in a compact subset of the open square has a finite-integral realizing control \(q=\operatorname{diag}(p(z))^{-1}C^{-1}\dot z\). This does not presume that inversion remains bounded at the square boundary.

Here is an explicit check that sharp side exits avoid that potential problem. By reflecting the second coordinate and its control, it suffices to take \(\rho=\eta>0\). Reach the interior point

\[
(R-\eta\delta/2,-R+\delta/2)
\]

for a small \(\delta>0\). Set \(q_1=0\), and increase \(z_2\) to \(R-\delta\), using \(q_2=\dot z_2/p(z_2)\). The controlling gate is bounded away from zero on this particular path. The invariant \(z_1-\eta z_2\) gives the final first coordinate

\[
R+2\eta R-2\eta\delta.
\]

The path crosses \(z_1=R\) while \(z_2=-R+\delta\) is strictly active. Sending \(\delta\) to zero proves the sharp supremum \((1+2\eta)R\) from every interior initial point. Each approximating control has finite integral; their integrals need not be uniformly bounded. Coordinate interchange and sign reflection give all other cases.

If coordinate \(a\) starts inactive and \(b\) active, set \(s=\operatorname{sign}z_a(0)\) and \(k=s(z_a(0)-\rho z_b(0))\), exactly as in the source. In the initial strip,

\[
sz_a=k+s\rho z_b.
\]

If \(k\ge(1+\eta)R\), the limiting minimum \(k-\eta R\) is at least \(R\); the strip cannot be left. Equality permits contact only at a frozen corner, which is inaccessible in finite time. Traversing compact portions of the active \(b\)-interval establishes the exact suprema \(k+\eta R\) and \(R\) in (4).

If \(k<(1+\eta)R\), the initial condition also gives \(k>(1-\eta)R\). Thus the crossing value \(z_b=s(R-k)/\rho\) lies strictly inside \((-R,R)\). The \(b\)-control carries the path into the square, including when it starts on the side itself. The initial-strip maximum is below \((1+2\eta)R\), and subsequent excursions satisfy that same bound. Interior reachability then gives the claimed sharp supremum for either coordinate.

For the sharpness of the extra \(2\eta R\) when only a far-out initial coordinate is retained, choose the other initial coordinate arbitrarily near the endpoint opposite its intended motion. Traversing almost the full active interval changes the far-out coordinate by almost \(2\eta R\). Starting from \((0,0)\) verifies the sharp additive constant \(1+2\eta\) in the second inequality of (1). There is no missing attainability claim at a frozen endpoint.

### Rank-one endpoints and full first-row motion

For \(\rho=\varepsilon\in\{-1,1\}\), direct subtraction yields the invariant \(k=z_1-\varepsilon z_2\). With \(u=z_1\), the scalar coefficients are \(p(u)\) and \(\varepsilon p(\varepsilon(u-k))\). At least one is nonzero precisely on the open union in (5). On a compact subinterval of a connected component, the sum of their squares has a positive minimum; choosing the controls proportional to these coefficients realizes any prescribed scalar velocity. A gap or a touching point makes both coefficients zero, so the frozen-point barrier prevents crossing it. This proves the exact reachable-component description.

Physical endpoint initial data have \(k=0\), giving (6) and finite-time persistence of an initially active physical neuron. Identical inputs at \(\rho=1\) indeed cannot produce the two different labels.

For nondegenerate inputs, a row increment lies in their span. Writing it as \(\sum_a c_ax_a^T\) gives coordinate increment \(dCc\) and squared row norm \(d c^TCc\), which proves (12). Its dependence on \(C^{-1}\) explains the deterioration near singular geometry. Frozen rows are fixed in all parameter directions because every term in their row update contains a zero first gate. These assertions are stronger than merely freezing their two projections, and are valid for the actual network update.

## 2. Gaussian reservoir and finite occupancy

The initialization scaling and input normalization give covariance \(C\) for each first-coordinate pair. For \(|\rho|<1\), its displayed Gaussian density is positive everywhere. The same-sign and opposite-sign saturation events therefore have strictly positive probabilities \(m_s,m_o\). Central symmetry pairs opposite corners; equality of \(m_s\) and \(m_o\) is not assumed or needed.

Each same-sign frozen row contributes \(A^2\begin{pmatrix}1&1\\1&1\end{pmatrix}\) before division by \(n\), and each opposite-sign row contributes \(A^2\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\). Summation gives (7). Its eigenvalues are exactly \(2A^2N_s/n\) and \(2A^2N_o/n\), establishing (8). The remaining rows contribute a positive semidefinite Gram matrix at every time. Occupancy of one row from each of the two sign classes suffices; occupancy of all four individual corners is unnecessary.

Taking expectations on a supplied measurable evolved initial-neuron space gives (9). The proof uses a fixed initial subset whose feature values do not change; it needs neither independence of evolved neurons nor construction of a population equation.

The union bound at lines 174–178 is valid. In fact, for the two disjoint sign classes the exact probability is

\[
\Pr(N_s>0,N_o>0)
=1-(1-m_s)^n-(1-m_o)^n+(1-m_s-m_o)^n,
\]

which confirms the source's lower bound. No positive lower bound for every finite draw follows. For (10), the two events \(N_s/n\ge m_s/2\) and \(N_o/n\ge m_o/2\) imply \(\gamma_n\ge A^2\min(m_s,m_o)\). The respective failure probabilities are at most \(4(1-m_s)/(nm_s)\) and \(4(1-m_o)/(nm_o)\), by applying Markov's inequality to the squared deviations. This verifies the stated constants. Negative lower bounds are merely vacuous. The event is selected once at initialization, so no union over time is needed. Uniformity as \(\rho\) approaches an endpoint is not asserted.

At \(\rho=-1\), the invariant gives \(z_2=-z_1\), and oddness of \(\phi_1\) gives feature pairs \((h,-h)\). Consequently the entire first Gram, not only its frozen contribution, has the form in (11). Its eigenvalues are \(0,2\alpha(t)\), with \(\alpha(t)\ge A^2m_F\) in the population and \(\alpha(t)\ge A^2N_F/n\) empirically. A positive empirical reservoir contribution requires \(N_F>0\); its probability is \(1-(1-m_F)^n\). Rank two is neither available nor claimed. The positive eigendirection is precisely the label direction.

## 3. Actual initialization motion and its limits

For \(|\rho|<1\), every smaller interior square has positive Gaussian mass, and the minimum of \(p\) on that compact interval is positive. Linear independence of the inputs makes the row-to-feature differential in lines 209–213 surjective onto the two sample coordinates when both gates are positive.

Conditional on \(W^1,W^2\), the backward coefficient \(b_{ja}\) is a linear form in \(w\). Its coefficient vector has entries \(W^2_{ij}g'(z^2_{ia})\). Both proposed activations have strictly positive derivative at every finite state. A Gaussian column of \(W^2\) is not identically zero with probability one, so this coefficient vector is nonzero with probability one. The conditional linear form is a nondegenerate scalar Gaussian even though the variance of \(w_i\) scales as \(n^{-2}\). Hence both \(b_{j1},b_{j2}\) are nonzero almost surely. Independence between these two forms is unnecessary.

The conditional residual is either a nonconstant affine form in \(w\), or the nonzero constant \(-y_a\) if its feature vector vanishes. Thus each \(r_a\ne0\) almost surely as well. Taking a finite union of the corresponding null events proves the assertions simultaneously for all rows and both samples; dependence among the residuals and backward coefficients causes no problem.

For an initially doubly active row, the two nonzero coefficients \(p(z_{ja}^1)r_ab_{ja}\), together with independent inputs, imply a nonzero actual row velocity. Its coordinate-pair velocity is \(-2C\operatorname{diag}(p) (r_1b_{j1},r_2b_{j2})^T\), and its feature-pair velocity is obtained by multiplying by the same positive diagonal gate matrix. Both matrices are invertible, so the feature-pair velocity is nonzero. This does not assert that each component separately must be nonzero. The prediction differential in lines 215–219 has rank two for the same reason.

The three-class coexistence probability is the valid union bound for \(N_s,N_o,N_A>0\). The variance \(m_A(1-m_A)/n\) is correct. Whenever that occupancy event is nonempty, intersecting it with a probability-one motion event preserves its probability. A finite collection of strictly positive gates and nonzero continuous velocities remains so on a sufficiently short common interval. The length and velocity scales can depend on the complete finite realization. None of this yields a width-uniform motion magnitude, duration, or a positive-mass moving population in a limit. The source states these distinctions correctly.

The persistence distinctions are also valid. A pair starting outside the frozen set cannot have both gates shut in finite time. For scalar cases, each initially active physical coordinate remains active. When \(0<|\rho|<1\), the explicit side exit checked above shuts one gate in finite time; unrestricted individual controls can apply this construction to an entire chosen initially active group. That construction is not a realization of the coupled network's endogenous controls. No all-time two-gate floor follows from these observations.

At \(\rho=-1\), let \(t_i=z^2_{i1}=-z^2_{i2}\). The active row velocity is proportional to \(p(z_{j1}^1)(r_1b_{j1}-r_2b_{j2})x_1^T\). Conditional on the hidden weights, the expression in parentheses is a polynomial of degree at most two in \(w\), with linear part

\[
-\sum_i W^2_{ij}[g'(t_i)+g'(-t_i)]w_i.
\]

That coefficient vector is nonzero almost surely. For completeness, a nonzero polynomial has a Lebesgue-null zero set: expand in its last variable, choose one nonzero coefficient polynomial, use induction to exclude the null set where all coefficients vanish, and use the finite root set of a nonzero one-variable polynomial on every other fiber. Integration over fibers finishes the argument. Gaussian absolute continuity then gives the desired probability-zero exceptional set. This proves actual row and first-feature motion for each initially active row and simultaneously for finitely many such rows. Positivity of \(p\) and \(\|x_1\|^2=d\) ensure that a nonzero row coefficient changes the first feature as claimed.

The antiparallel representability construction is exact: choose rows \(t h^T/\|h\|^2\) and \(-t h^T/\|h\|^2\) for any nonzero first-feature vector \(h\). The stated weights \(\pm n/[g(t)-g(-t)]\) give outputs \((1,-1)\). Strict increase makes the denominator positive, and \(n\ge2\) supplies two rows. For arctan one row with weight \(n/\arctan t\) suffices. This is representability, not a training claim. A first-feature differential is antipodal; a prediction differential need not be antipodal for nonodd \(g\). The source does not confuse these assertions.

## 4. Exact upper dynamics and all SUM-loss constants

The following check uses the source's SUM loss \(L=r_1^2+r_2^2\), with neither a factor \(1/2\) nor sample averaging. Introduce, solely for this calculation,

\[
T_0=\sum_a r_ah_a^2,\qquad
T_2=\sum_a r_a\delta_a^2(h_a^1)^T,\qquad
T_1=\sum_a r_a\delta_a^1x_a^T.
\]

The three gradients are \(2T_0/n,2T_2/n,2T_1/n\). The prescribed dynamics multiply their negative gradients by \(n,1,n/d\), respectively. Therefore

\[
-\dot L=\frac4n\|T_0\|^2+\frac4{n^2}\|T_2\|_F^2
+\frac4{nd}\|T_1\|_F^2,
\]

exactly (16). Equivalently,

\[
-\dot L=\|\dot w\|^2/n+\|\dot W^2\|_F^2
+d\|\dot W^1\|_F^2/n.
\]

Integrating and applying Cauchy–Schwarz in time gives both bounds in (18), with exactly the displayed factors \(\sqrt{tL(0)}\) and \(\sqrt{ntL(0)}\). Also,

\[
\frac{d}{dt}\|w\|^2=-4\sum_a r_aw^Th_a^2
=-4n\langle r,f\rangle\le2n,
\]

because \(\|y\|^2=2\) and \(\langle f-y,f\rangle=\|f-y/2\|^2-1/2\). Thus (19) is correct, including its label-dependent constant.

Differentiating \(W^2h_a^1\) yields the direct update contribution

\[
-\frac2n\sum_b r_bw_ig'(z^2_{ib})(h_b^1)^Th_a^1,
\]

which is the first term of (13); the additional contribution is exactly \(B_i\). No transport term is missing. For the frozen columns, \(S^T(I-P)=0\), so \(\dot V(I-P)=0\), proving (14), including rank-one or trivial cases. This invariant contributes zero to \(VS\), and its backward effect through frozen first rows is killed by their zero gates. It is only invisible on the two specified samples. Multiplication of the visible frozen update by \(S\) gives (15), with \(G_F=S^TS/n\); the derivative must be evaluated at the total \(Z_i\), as written.

For the second loss term, the \(i\)-th row of \(T_2\) is \(\sum_a(v_i)_a(h_a^1)^T\), so its squared norm is \(n v_i^TG_1v_i\). Hence (8) gives

\[
-\dot L\ge\frac{4\gamma_n}{n}\sum_{i,a}w_i^2r_a^2g'(z^2_{ia})^2.
\]

Integrating proves exactly (17), with denominator \(4\gamma_n\), on the event \(\gamma_n>0\). No division is made on a zero-occupancy event. For finite states with \(w\ne0\), positive \(g'\), positive \(\gamma_n\), and \(r\ne0\), at least one term is strictly positive. This verifies pointwise strict loss decrease. It does not produce a state-independent rate: the necessary factors \(w_i^2g'(z^2_{ia})^2\) have no uniform positive lower bound here. Nor does (17) remove its weights or control the multiplication by \((W^2)^T\) in the original first-layer controls.

Finally,

\[
n\frac{d}{dt}\|W^2\|_F^2
=-4\sum_{a,i}r_aw_i z^2_{ia}g'(z^2_{ia}),
\]

so subtraction from the readout norm derivative gives exactly (20), with sign \(+4\) and defect \(sg'(s)-g(s)\). This completes the normalization check for all upper identities and estimates.

## 5. Activation shapes, pointwise obstructions, and neighborhood quantifiers

For arctan, the value and derivative bounds are correct; \(|s|/(1+s^2)\le1/2\). Its defect has derivative \(-2s^2/(1+s^2)^2\), vanishes at zero, and tends to \(\mp\pi/2\) at the two infinite endpoints, so the stated absolute bound follows. The second-feature Gram can be singular, for example when the two feature columns coincide.

For shifted softplus, \(g'=\sigma(s+b)\), with positive derivative at every finite argument but infimum zero. Its positive tail is unbounded and asymptotically affine. Writing \(u=\sigma(s+b)\), so \(s=\log(u/(1-u))-b\), gives exactly

\[
sg'(s)-g(s)=c+u\log u+(1-u)\log(1-u)-bu
=c-\mathcal H(u)-bu.
\]

The entropy lies in \([0,\log2]\). Thus the defect is bounded but not identically zero; for \(b=0,c=\log2\) it is nonnegative. The products \(r_aw_i\) have no fixed sign, so the source's absolute-value estimate following (20) is valid and is not a conservation law. Boundedness of the difference of two nonnegative norms would not bound them individually.

The scalar controlled counterexamples also have the correct signs and primitives. For arctan, \(d(z+z^3/3)/dt=q\); the displayed positive constant control reaches \(M\) at time 1. For softplus, \(F'(z)=1+e^{-z-b}=1/g'(z)\), so the displayed negative constant control reaches \(-M\) at time 1. Both trajectories can then remain at their endpoints under zero control. Every such control has finite integral and compact time support. They disprove amplitude-independent scalar confinement, without constructing an unbounded canonical network trajectory.

For Section 7, independent inputs permit first rows realizing strict same-sign saturation, strict opposite-sign saturation, and strict interior activity. This requires \(n\ge3\) for the combined construction, as the source states. Rank two of \(S\) gives a frozen-supported row realizing any prescribed two-component preactivation: a concrete choice is

\[
V_i^T=S(S^TS)^{-1}(m,m)^T,
\]

where \(m=M\) for arctan and \(m=-M\) for softplus. Choose all second rows this way. Their norms grow linearly in \(M\), and this growth is in the visible contribution \(U_i=(m,m)^T\), not merely the invisible invariant.

With readout weights \(+B,-B,0,\ldots,0\), equal feature pairs and zero total readout weight give exactly \(f=0\), \(r=(-1,1)\), and \(L=2\). They also give \(\dot w=0\) and \(b_{ja}=0\) at that state, hence \(\dot W^1=0\). The only loss term left is

\[
-\dot L=\frac4n\|w\|^2g'(m)^2
(1,-1)G_1(1,-1)^T,
\]

which verifies (21). With \(B=M\), both upper norms diverge along this family of states, while \(L,G_1\), and the first parameters remain fixed. The dissipation tends to zero with the stated factors \(M^2/(1+M^2)^2\) and \(M^2\sigma(-M+b)^2\). With \(w=0\), all three updates vanish at the equal-pair center, proving the positive-loss stationary example.

The probability argument is sound and does not require an exact cancellation event to have positive probability. For precision, fix \(n\ge3\), fixed \(|\rho|<1\), one of the two activations, and a strict first-layer center. For every \(\epsilon>0\), there exists a finite parameter center and a nonempty open neighborhood \(U_\epsilon\) such that throughout that neighborhood

\[
N_s,N_o,N_A>0,\qquad 1<L<3,\qquad 0\le-\dot L<\epsilon.
\]

For the tail construction, first choose finite \(M\) making the center's dissipation less than \(\epsilon/2\). Continuity of the smooth finite-dimensional loss dissipation then supplies the neighborhood. Strict gate classifications and positive loss persist after further shrinking it. A stationary center with \(w=0\) supplies the alternative construction for each tolerance and any fixed finite \(M\). Every nonempty open neighborhood of a finite parameter vector has positive probability under the joint Gaussian initialization, since all parameter variances are positive at this fixed width. Intersecting with the probability-one initialization-motion event retains that positive probability. No independence from the motion event is needed.

This explicit quantifier statement is the first optional clarification. The source's existing argument already proves it. The neighborhood, its probability, and its motion magnitudes can all depend on the tolerance and width; there is no single positive-probability event on which the initial dissipation is zero, no lower bound on the probabilities as width grows, and no uniform time interval of weak dissipation supplied by this argument. At the exact centers the loss is 2; in open neighborhoods it is close to 2, not necessarily exactly 2.

The valid obstruction is therefore to pointwise upper-norm bounds and uniformly positive instantaneous learning rates derived only from first-layer confinement, first-Gram coercivity, and bounded loss. These constructions do not disprove high-probability convergence, a bound depending on the full initial upper state, or boundedness along a particular canonical trajectory. The source expressly preserves these distinctions.

## 6. Separate antiparallel upper dynamics

At antiparallel inputs every second pair is \((t_i,-t_i)\), so a nonzero equal-pair tail is unavailable. For arctan, oddness gives \(f_2=-f_1\) and \(r=e(1,-1)\), with \(e=f_1-1\). Let \(p_j=p(z_{j1}^1)\) and \(b_j=b_{j1}=b_{j2}\). Direct differentiation gives

\[
\dot w_i=-4e\arctan(t_i),\qquad
\dot W^2_i=-\frac{4e}{n}\frac{w_i}{1+t_i^2}h^T,
\qquad \dot h_j=-4e p_j^2b_j.
\]

Consequently the full coefficient, including the omitted nonnegative contribution, is

\[
\kappa(t)=\frac4n\left[
\sum_i\arctan(t_i)^2
+\alpha\sum_i\frac{w_i^2}{(1+t_i^2)^2}
+\sum_jp_j^2b_j^2\right].
\]

This proves (22), including its factor 4, and shows explicitly why first-feature transport does not introduce a negative contribution in this special scalar reduction. Along a finite classical trajectory, \(e(t)=e(0)\exp[-\int_0^t\kappa(s)\,ds]\). Thus the error cannot change sign, and its magnitude is nonincreasing. Monotonic motion toward 1 is understood non-strictly, as the source's stationary example requires. The displayed inequality alone does not force \(\int_0^\infty\kappa=\infty\).

The lower bound \(\alpha\ge A^2N_F/n\) follows from the reservoir. Nevertheless \(w=0,t_i=0\) gives a stationary state with \(L=2\), even for \(\alpha>0\). Conversely, a large arctan preactivation contributes a nonzero readout feature, which confirms why Section 7's cancellation construction cannot simply be reused here.

For softplus with \(b=0\),

\[
\log(1+e^t)=t/2+\log(2\cosh(t/2))
\]

implies both identities in (23), including all \(1/n\) and \(2/n\) factors and the vertical shift \(c\). For fixed readout weights the contrast is linear in the second preactivations; the common channel retains the displayed nonlinear term. This is not a claim that the entire network is affine in its input or in all trainable parameters. A nonzero horizontal shift generally destroys the exact contrast identity, while leaving the derivative-tail issue. These scoped conclusions are correct.

## 7. First-activation distributional nonaffinity

Section 9 explicitly supplies the population premise it needs: a measurable family of continued controlled paths with the specified initial Gaussian pair and locally integrable controls almost surely. It does not obtain that family by passing to a width limit.

For a fixed sample, write \(G=Z(0)\). Equation (1) gives

\[
|Z(t)|\le |G|+(1+2|\rho|)R,
\]

so \(Z(t)\in L^2\), in fact with a uniform second-moment bound along the supplied trajectories. For \(|\rho|<1\), each event \(G>K\) with the other initial coordinate outside the gate support has positive probability once \(K\ge R\), and these neurons are frozen. The negative counterparts also have positive probability. Arbitrary smaller thresholds follow by using a larger \(K\). At \(\rho=-1\), the same reasoning uses the frozen event \(|G|\ge R\). Therefore the evolved marginal retains both unbounded tails, on which the activation is respectively \(A\) and \(-A\).

If \(\phi_1(Z)=aZ+b\) almost surely with \(a\ne0\), then \(|aZ+b|\ge |a||Z|-|b|\) exceeds \(A\) on a sufficiently remote frozen tail of positive probability, contradicting boundedness of the activation. If \(a=0\), the two frozen signs require simultaneously \(b=A\) and \(b=-A\), which is impossible. This verifies the claimed nonaffinity.

The Gram matrix of \((1,Z)\) has determinant \(\operatorname{Var}(Z)>0\) and finite entries. Its positive definiteness means that the \(L^2\) norm on the span is equivalent to the Euclidean norm of the two coefficients: every convergent sequence of affine functions has convergent coefficients and an affine limit. The span is therefore closed. Since \(\phi_1(Z)\in L^2\) and is not in that span, its least-squares distance to it is strictly positive. Thus there is no omitted attainment or integrability step in lines 419–425.

Here is the second optional strengthening. Let \(\mathcal F_0\) denote the event that the initial pair is frozen and set

\[
m=\Pr(\mathcal F_0),\qquad
J_1=\mathbb E[|G|\mathbf1_{\mathcal F_0}],\qquad
J_2=\mathbb E[G^2\mathbf1_{\mathcal F_0}].
\]

These are fixed initial-law quantities with \(m,J_2>0\). Joint central symmetry makes \(\mathbb E[G\mathbf1_{\mathcal F_0}]=\mathbb E[\operatorname{sign}(G)\mathbf1_{\mathcal F_0}]=0\). Since the frozen part never changes, for every \(a,b\) and every supplied time,

\[
\begin{aligned}
\mathbb E[(\phi_1(Z(t))-aZ(t)-b)^2]
&\ge\mathbb E[(A\operatorname{sign}(G)-aG-b)^2\mathbf1_{\mathcal F_0}]\\
&=A^2m-2aAJ_1+a^2J_2+b^2m.
\end{aligned}
\]

Minimizing the last expression gives

\[
\inf_{a,b}\mathbb E[(\phi_1(Z(t))-aZ(t)-b)^2]
\ge A^2\left(m-\frac{J_1^2}{J_2}\right)>0.
\]

Strict positivity follows from strict Cauchy–Schwarz: equality \(J_1^2=mJ_2\) would make \(|G|\) constant on the frozen event, whereas its conditional law has unbounded support. The same proof applies at the physical antiparallel endpoint. Thus even a time-uniform positive population affine-fit gap is available. The document only claims the weaker fixed-time consequence, so this is not a required correction.

Both versions concern the full evolved initial-neuron law, not an arbitrary finite empirical affine fit. A finite empirical marginal supported on only two distinct preactivations can admit an exact affine fit. More fundamentally, this nonaffinity is already supplied by frozen neurons and therefore establishes neither moving positive mass nor nonlazy prediction dynamics, second-layer distributional nonaffinity, or existence of a population limit. Section 9 and the status table correctly retain those limits.

## Final disposition

Every substantive mathematical claim in the supplied document, including its final status table, is supported at its stated scope. Equations (1)–(23), the sharp initial-state cases, both rank-one endpoint geometries, the finite occupancy and motion events, and the neighborhood probability quantifiers have been independently checked. There are no required findings. The two optional points above improve explicitness or strength without changing the verdict.

Accept this exact source version as the stated scoped lemma/test. It establishes controlled first-state confinement, an actual frozen Gaussian reservoir, conditional first-Gram coercivity, local finite-width initial motion, exact upper identities and weighted dissipation, pointwise limitations on conclusions from the first Gram alone, and first-activation distributional nonaffinity for a supplied population. It does not establish the broader activation-design or global nonlinear mean-field objectives, and its failure to do so is not a defect in this deliberately scoped submission.

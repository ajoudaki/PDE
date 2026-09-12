# Random-direction source responses — bounded theoretical assessment

The random-direction identity is exact for a fixed finite source program with deterministic frozen coefficients. Weighted directions can make its **contracted** error independent of the number of mesh slots, provided a weighted *random-derivative* energy bound holds. One directional tangent per representative reduces the direct response work to \(O(PJ^2)\). These facts do not establish the corresponding error bound for a generated solver that feeds the same representatives' response estimates back into later coefficients.

This is exploration, not an independent review or a simulation report. Scientific inputs were the self-contained assignment, C.4.7 equations N2–N8, and the specified III.F source-rule material. The earlier spectral route was frozen before this subtask; it is not an input to this report. No experiments were run.

## 1. Fixed-program identity, including singular sources

Let \(\xi\in\mathbb R^J\) have the finite Gaussian source law of one orientation, possibly singular, and let \(F(\xi,g)\) be a scalar node's prescribed smooth formal expression. All scalar feedback values, covariances, contractions, residuals, and response coefficients are held fixed when differentiating. Write

\[
 a_p(\xi,g)=\partial_{\xi_p}F(\xi,g),\qquad b_p=E[a_p].
\]

The named coordinates remain distinct formal arguments even at singular covariance. Assume \(E\|a\|_2^2<\infty\), as holds for each fixed graph under its finite derivative-envelope argument. Let \(\epsilon_p\) be independent Rademacher signs, independent of roots and Gaussian sources. Then

\[
 T=\sum_q\epsilon_q a_q,
 \qquad E_{\epsilon}[\epsilon_pT\mid\xi,g]=a_p,
 \qquad E[\epsilon_pT]=b_p.
\]

The proof is the finite expansion \(E[\epsilon_p\epsilon_q]=\mathbf1_{p=q}\); neither an inverse covariance nor Gaussian integration by parts is used. Correlation or singularity of the Gaussian coordinates therefore does not invalidate this identity. Replacing the formal source direction by a direction in independent Gaussian innovations would estimate a different derivative unless the change of coordinates were explicitly accounted for.

The same construction applies separately to lower-population derivatives \(\partial_\zeta H^{(1)}\) and upper-population derivatives \(\partial_\xi\Delta^{(2)}\). Their Gaussian populations are separate. They are not paired neuron coordinates. A common probe seed across populations is optional coupling of numerical estimates, not a statement that the population Gaussian families coincide.

To get a \(P^{-1}\) variance from \(P\) representatives, sample **independent pairs** \((\xi^{(i)},g^{(i)},\epsilon^{(i)})\). One sign vector shared by all Gaussian representatives does not suffice: as \(P\to\infty\), the estimator converges to \(\epsilon\epsilon^Tb\), whose probe noise generally persists.

## 2. Exact contracted variance

Let \(h=(h_1,\ldots,h_J)^T\) denote the destination population's saved history features. It is independent of the source-population representatives in this section, because the program's scalar coefficients are deterministic. Set

\[
 G=E[hh^T],\quad \widehat b=\frac1P\sum_{i=1}^P
       \epsilon^{(i)}(\epsilon^{(i)T}a^{(i)}),\quad
 C=h^Tb,quad\widehat C=h^T\widehat b.
\]

Here \(G\) is the uncentered history Gram, not a centered covariance of \(h\). For one fixed vector \(a\), direct expansion of four signs gives

\[
 E_\epsilon[(\epsilon\epsilon^Ta-a)(\epsilon\epsilon^Ta-a)^T]
 =\|a\|^2I+aa^T-2\operatorname{diag}(a_p^2).
\]

Indeed, its diagonal entry \(p,p\) is \(\sum_{q\ne p}a_q^2\); its off-diagonal entry \(p,r\) is \(a_pa_r\). Averaging independent representatives and conditioning first on their gradients yields the exact decomposition

\[
\begin{aligned}
 E\|\widehat C-C\|_{L^2(h)}^2
 =\frac1P\bigg\{
 &E\big[\|a\|^2\operatorname{tr}G+a^TGa
          -2\sum_pG_{pp}a_p^2\big]\\
 &+E[a^TGa]-b^TGb\bigg\}.
\end{aligned} \tag{R1}
\]

The first line is extra random-direction variance. The second is the variance of integrating the exact gradient with \(P\) Gaussian representatives. It is necessary to count both.

Saved histories may instead be a fixed finite destination sample, with empirical Gram \(\widehat G\). Conditional on that sample and independent source/probe samples, the same formula holds with \(\widehat G\). This conditional independence is a fixed-program property. It is not automatic after sample-based coefficients couple the two populations.

Formula R1 explains both a benefit and a danger. It controls the synthesized correction rather than the Euclidean error of all its individual coefficients. But its leading term contains \(\operatorname{tr}G\,E\|a\|^2\). An order-one derivative in a single source can produce noise in all the other history coefficients.

## 3. Weighted directions and a mesh-independent sufficient bound

Choose deterministic positive weights \(\omega_p\) on the active historical source slots. Put

\[
 T_\omega=\sum_p\frac{\epsilon_p}{\sqrt{\omega_p}}a_p,
 \qquad \widehat a_p=\sqrt{\omega_p}\epsilon_pT_\omega.
 \tag{R2}
\]

The same sign identity proves \(E_\epsilon\widehat a_p=a_p\). Define the two quantities

\[
 S_\omega=\sum_p\omega_p E[h_p^2],\qquad
 E_\omega=\sum_p\frac{E[a_p^2]}{\omega_p}.
 \tag{R3}
\]

These use random derivatives \(E[a_p^2]\). A bound only on \(\sum_p|b_p|^2/\omega_p\) cannot replace \(E_\omega\): a mean response can be zero while its sampled derivative fluctuates strongly.

For \(P\) independent source/probe pairs, weighted estimation obeys

\[
 E\|h^T(\widehat b-b)\|_2^2
 \leq \frac{3S_\omega E_\omega}{P}. \tag{R4}
\]

The extra probe variance alone is at most \(2S_\omega E_\omega/P\); the exact-gradient Monte Carlo contribution is at most \(S_\omega E_\omega/P\).

**Proof.** Put \(D=\operatorname{diag}(\omega_p^{-1/2})\). Apply the unweighted computation to \(Da\), contracting with \(D^{-1}h\). The exact probe variance for one gradient, averaged over destination history, is

\[
 \Big(\sum_p\omega_pG_{pp}\Big)
 \Big(\sum_p a_p^2/\omega_p\Big)
 +a^TGa-2\sum_pG_{pp}a_p^2. \tag{R5}
\]

For every \(a,h\), weighted Cauchy–Schwarz gives

\[
 (h^Ta)^2\leq
 \Big(\sum_p\omega_ph_p^2\Big)
 \Big(\sum_pa_p^2/\omega_p\Big).
\]

Average independent \(h\) and \(a\) to obtain \(E[a^TGa]\leq S_\omega E_\omega\). Drop the negative term in R5 to bound probe variance by \(2S_\omega E_\omega\). Exact-gradient sampling variance is \(E[a^TGa]-b^TGb\leq S_\omega E_\omega\). Independence of representatives divides the sum by \(P\), proving R4.

If \(\omega_p=m_p=h_sp_b\), if historical derivatives obey \(E[a_p^2]\leq C^2m_p^2\), and if \(E[h_p^2]\leq B^2\), then

\[
 S_\omega\leq B^2\sum_pm_p,
 \qquad E_\omega\leq C^2\sum_pm_p.
\]

The resulting bound depends on total physical time, not the number or balance of time/data slots. Unit directions would instead give the potentially poor factor \(J\sum_pm_p^2\).

Alternatively choose \(\omega_p=|\gamma_p|\), with zero weights skipped in the *historical tangent calculation*. If \(a_p=\gamma_p\widetilde a_p\) and \(E[\widetilde a_p^2]\leq C^2\), then both sums in R3 are bounded by constants times accumulated force \(\sum_p|\gamma_p|\). This is more closely matched to the source equations. Neither choice proves that the envelope constant \(C\) stays useful through time 40.

Zero \(\gamma_p\) does not justify removing the primal Gaussian source or its covariance record. It only permits skipping its old response direction when the causal derivative factorization below proves that its future state influence is zero.

## 4. Application to N7–N8 and exact current subtraction

For the lower population propagate one two-component directional tangent \(\dot w_k\) per representative. Use an independently signed lower direction and define

\[
\begin{aligned}
 \dot H_q&=\phi'(w_{t(q)}\cdot u_q)u_q\cdot\dot w_{t(q)},\\
 \dot Q_{ka}&=\epsilon^{\zeta}_{ka}/\sqrt{\omega_{ka}}
       +\sum_{q\leq k}D_{ka,q}\dot H_q,\\
 \dot w_{k+1}&=\dot w_k+\sum_a\gamma_{ka}u_a
 \{\phi''(w_k\cdot u_a)Q_{ka}(u_a\cdot\dot w_k)
                       +\phi'(w_k\cdot u_a)\dot Q_{ka}\}.
\end{aligned} \tag{R6}
\]

An inactive zero-weight source contributes no direct tangent pulse. All coefficients in R6 are frozen. At node \(ku\), estimate the historical \(\alpha_{ku,p}\) by the representative average of

\[
 \sqrt{\omega_p}\epsilon^\zeta_p
       \phi'(w_k\cdot u)u\cdot\dot w_k.
\]

Current and unavailable lower coefficients are structurally zero and are set to zero, rather than estimated noisily.

For the upper population the one-direction equations are

\[
\begin{aligned}
 \dot c_k&=\sum_{q<k}\gamma_q\phi'(Z_q)\dot Z_q,\\
 \dot Z_{ka}&=\epsilon^\xi_{ka}/\sqrt{\omega_{ka}}
                +\sum_{q<k}F_{ka,q}\dot\Delta_q,\\
 \dot\Delta_{ka}&=\phi'(Z_{ka})\dot c_k
                  +c_k\phi''(Z_{ka})\dot Z_{ka}.
\end{aligned} \tag{R7}
\]

The known current derivative is pointwise

\[
 a_{ka}^{\rm current}=c_k\phi''(Z_{ka}).
\]

Before estimating **any historical** \(\beta_{ka,p}\), form

\[
 T^{\rm old}_{ka}
 =\dot\Delta_{ka}
       -c_k\phi''(Z_{ka})\epsilon^\xi_{ka}/\sqrt{\omega_{ka}}.
 \tag{R8}
\]

Then use

\[
 \widehat\beta_{ka,p}
 =\frac{\sqrt{\omega_p}}P\sum_i
       \epsilon^{\xi,(i)}_p T^{{\rm old},(i)}_{ka},\quad t(p)<k.
\]

Set the current diagonal to the ordinary representative mean of \(c_k\phi''(Z_{ka})\), and every other current formal coefficient to zero. For a passive query use its own distinguished current slot. This remains the rule when inputs are duplicated or the covariance is singular.

If the current weight is zero, its directional injection is omitted; R8 then subtracts zero, while the current diagonal is still evaluated directly. Its primal source is retained. The coefficient and weight used for a new pulse are causal scalar values and are frozen in the tangent calculation.

Subtracting only the **mean** current derivative is insufficient: its centered pointwise fluctuation would still contaminate every historical coefficient. R8 subtracts the whole known direct tangent before sign multiplication. Without this step, a current derivative of size order one enters \(E_\omega\) with factor \(1/\omega_{ka}\), defeating the intended mesh refinement bound.

**Why old pulses carry their training weight.** In N7 the derivative from a lower source is initially zero and first enters through its direct pulse \(\gamma_pu_p\phi'(w\cdot u_p)\). Every subsequent derivative equation is linear in that pulse's tangent with deterministic frozen coefficients. Thus \(\partial_{\zeta_p}H_k=\gamma_p\widetilde a_{k,p}\) for \(t(p)<k\). It follows that the forward coefficient \(F_{k,p}=\alpha_{k,p}+\gamma_pE[H_kH_p]\) also has a factor \(\gamma_p\).

For upper sources, the direct derivative of \(\Delta_p\) at its own node need not have such a factor. To influence a later node, however, it must either enter the readout update through \(\gamma_p\), or leave its source node through a coefficient \(F_{k,p}\), which has the factor just proved. N8 then gives the same factor for every later upper derivative by induction in construction order. Different current input slots have zero direct cross-derivative. This proves the stated historical factorization, including zero-pulse exclusion.

The factorization is exact for each fixed finite graph. It is not a graph-uniform moment bound on the quotients \(\widetilde a_{k,p}\). N7 includes multiplicative random \(Q\) terms, and the assigned fixed-graph envelope argument asserts finite moments but explicitly does not give a bound uniform in instruction count. Establishing a uniform weighted random-tangent bound remains a substantive step.

For numerical evaluation, compute the identical old tangent directly as

\[
 T^{\rm old}_{ka}=\phi'(Z_{ka})\dot c_k
       +c_k\phi''(Z_{ka})\sum_{q<k}F_{ka,q}\dot\Delta_q,
\]

rather than subtracting two potentially large numbers when the current weight is small. The plain current-diagonal sample mean has variance at most \(4E[c_k^2]/P\), since \(|\phi''|\leq2\); its contraction with its one current first-layer history has the same upper bound because \(|H^{(1)}|\leq1\). This residual ordinary sampling error is distinct from the removed leakage across all old slots.

## 5. Cost, storage, and the meaning of \(O(PJ^2)\)

Here \(J\) is the **total number of named scalar source calls** in the retained graph, not merely the number of training inputs per step; \(P\) is the number of independent representatives per population. Two populations change constants but not orders.

At the \(j\)-th call, a value history contraction and its one-direction derivative each require (O\(Pj\)) operations. Forming all \(j\) response coefficients as sign–tangent sample means also costs (O\(Pj\)). Summing over calls gives \(O(PJ^2)\). Store (O\(PJ\)) values, directional tangents, and signs, plus \(O(J^2)\) scalar response/covariance entries. Weighted signs and the current subtraction add only constant work per stored/source entry. They therefore preserve this order.

A full forward derivative array has \(j\) derivative coordinates at step \(j\); naively differentiating its dense history contractions costs \(O(Pj^2)\), hence \(O(PJ^3)\) overall and \(O(PJ^2)\) tangent storage. The random-direction gain concerns this derivative coordinate dimension.

The response cost does not include the separate causal Gaussian source generation/factorization work. Dense covariance factorization, rank handling, data quadrature, time resolution, coefficient precision, and the cost required to choose a sufficient \(P\) must be added to any total solver budget. In particular, an \(O(PJ^2)\) operation formula is not evidence that its required \(P,J\) give feasible time-40 accuracy.

With \(R\) independent directions per fixed Gaussian representative, source-sampling variance is divided by \(P\), whereas extra probe variance is divided by \(PR\). Work becomes \(O(PRJ^2)\). This tradeoff is distinct from drawing \(PR\) independent Gaussian representatives.

## 6. The generated-solver adaptation obstacle

Stop-gradient conventions prevent differentiation **through** scalar feedback. They do not make a coefficient statistically independent of the probes that generated it. Once earlier response estimates influence later values, a reused probe may be correlated with the later frozen-program gradient itself. The sign expectation used in Section 1 can then fail.

An explicit two-source example is enough. Let \(\epsilon_1,\epsilon_2\) be independent signs, let the earlier generated scalar be \(\theta=\epsilon_1\epsilon_2\), and let the later frozen-coefficient expression be

\[
 F_\theta(\xi)=\theta\xi_2.
\]

Its formal derivative in coordinate 1 is zero. Nevertheless its reused-direction estimate is

\[
 \epsilon_1\sum_q\epsilon_q\partial_qF_\theta
 =\epsilon_1\epsilon_2\theta=1.
\]

The coefficient is frozen during differentiation, exactly as prescribed; the bias remains. For a pooled construction let

\[
 s_i=\epsilon_{i1}\epsilon_{i2},\qquad
 \theta=P^{-1}\sum_i s_i.
\]

The pooled estimate of the same zero derivative is \(\theta^2\), whose expectation is \(1/P\). This illustrates a bias that can vanish on a fixed graph as \(P\to\infty\), while invalidating a claim of exact unbiasedness and leaving its accumulation on refined long graphs unproved.

There is a second dependence issue: representative Gaussian histories can themselves be correlated with previously estimated coefficients. Even fresh directions at the current row only restore the conditional identity for the gradients of those *current empirical histories*. They do not automatically turn that average into the exact source expectation for a Gaussian program with the random coefficient transcript held fixed.

Fresh independent directions plus fresh Gaussian replay of the whole current frozen prefix can restore the relevant conditional fixed-program identities. But replaying a dense prefix for every response row has direct cost \(O(PJ^3)\), forfeiting the advertised saving. Merely splitting two probe banks and allowing both banks' outputs to influence later shared coefficients does not maintain permanent independence.

A valid \(O(PJ^2)\) generated solver therefore needs a separate theorem, for example a quantitative comparison to the deterministic source program controlling representative dependence and probe-feedback sensitivity, or an appropriate uniform empirical-process/leave-one-out estimate. Its hypotheses must control weighted random tangents, history synthesis, and covariance generation on the **generated** path. Fixed-program R4 plus stability of the exact flow is not that theorem.

## 7. What paired or symmetrized probes can and cannot fix

* **Antithetic signs \(\epsilon,-\epsilon\):** their response estimates are identical, since both the tangent and the outer sign change sign. There is no variance reduction and the adaptation counterexample is unchanged.
* **Two independent directions on a frozen program:** averaging them halves the extra probe variance at twice the tangent work. It does not reduce the Gaussian-gradient sampling component when the Gaussian representatives are shared. Their later reuse after feedback still needs an adaptation argument.
* **A symmetric finite-difference pair \(F(\xi+\delta v),F(\xi-\delta v)\):** with coefficients held fixed, its central difference approaches the same directional tangent. It adds finite-difference error and does not remove reused-probe dependence. Exact forward differentiation is preferable when available.
* **Common probes for opposite orientations:** these can correlate the two numerical errors, but the two response rules concern different derivatives on separate Gaussian populations. No general adjoint-accuracy or variance cancellation follows from pairing alone. Such a coupling needs its own algebraic identity.
* **A complete orthogonal sign frame:** if its empirical outer product is exactly the identity, averaging over the whole frame recovers a common gradient exactly, even if that gradient depends on the frame. A padded Hadamard frame can be built recursively from \(H_1=(1)\) by \(H_{2m}=\begin{pmatrix}H_m&H_m\\H_m&-H_m\end{pmatrix}\); the identity \(H_{2m}H_{2m}^T=2mI\) follows by block multiplication. But a complete frame requires order \(J\) tangents, restoring the full derivative-scale cost. A small random subset does not supply this exact identity.

Thus ordinary paired symmetrization is a variance option for the frozen program, not a repair of the generated-state bias.

## 8. Singular-support and formal-coordinate audit

The exact source rule is invariant after contraction under admissible changes of formal extension on a singular support. A random finite coordinate sketch need not have that invariance sample by sample, or even in variance.

For example, take \(J\geq3\), deterministic history \(h=(1,\ldots,1)\), and perfectly duplicated sources \(\xi_1=\cdots=\xi_J=G_0\). The formal expression \(F=\xi_1-\xi_2\) is identically zero on the source support and its exact history correction is zero. Its unit-direction contracted estimate is

\[
 \Big(\sum_{p=1}^J\epsilon_p\Big)(\epsilon_1-\epsilon_2)
 =\Big(\sum_{p=3}^J\epsilon_p\Big)(\epsilon_1-\epsilon_2),
\]

which has variance (2\(J-2\)). Independence of the two parenthesized factors gives this value directly. This is not a counterexample to unbiasedness, nor to the weighted bound, nor to the assigned formal derivative convention. It shows why response variance cannot be certified solely from the scalar field's value on a singular support or the size of its exact contracted correction.

Projecting probes onto a covariance-supported subspace could remove such null-direction noise, but introduces covariance factorization/rank information and a new stability/cost analysis. It is not part of the coordinate-sign estimator proved here. No continuity of a pseudoinverse at rank loss is presumed.

## Frozen conclusion

The following pieces are proved: the fixed-program random-direction identity; the exact contracted variance formula; the weighted \(3S_\omega E_\omega/P\) bound; exact current-diagonal subtraction; historical pulse factorization; and the direct \(O(PJ^2)\) response cost. They apply to the actual causal forward/backward source equations with all specified scalar quantities frozen.

The missing bridges are \(i\) a useful time-40 bound on weighted **random** tangent energy, and \(ii\) a generated-solver approximation theorem controlling adaptive sample/probe feedback with the chosen \(P,J\). Known-current subtraction and force-weighted directions are concrete improvements to a candidate. They do not by themselves certify its generated error, convergence under joint refinement, or feasible total cost.

# Independent audit of the tangent trace identification and induction closure

Reviewed input: the complete frozen `MFP_CAVITY_PROOF.md`, revision c2, 566 lines, in this directory. The line numbers below refer to that frozen file unless explicitly labelled `docs`. I did not read the linked audit, blueprint, worker notes, study histories, or another reviewer's findings. Permitted comparison material was `docs/02-gaussian-reuse.qmd:252–1293` and `docs/notation.qmd`. The required mathematical-solution and canonical-notation skills, including the neural response reference, were applied.

**Conclusion:** I found no mathematical defect in the Section 5 trace identification or its use in Sections 6–7. Its induction is well founded, its symbolic tangent identity retains both families of response terms, and it proves the limit of the physical injection Jacobian rather than assuming that it is a formal source derivative. Singular and duplicate source slots do not invalidate the argument. The empirical all-finite-$L^p$ and $\mathcal W_2$ bridges are valid under the moment and cavity estimates established in Sections 2–4. I also inspected those estimates as dependencies and found no conflicting premise. This is a mathematical audit of the stated smooth Gaussian class, not a claim about a lower-regularity extension or formal verification.

The only correction I recommend in this scope is a small expository addition to the finite reverse-differentiation summary, described at the end. It is not a missing argument in the central probabilistic proof.

## 1. The matrix-stage induction really decreases

The relevant quantifier is essential: the induction applies to every fixed batch size, root list and deficit vector (65–68), and a stage contains one matrix name and orientation with all its inputs available before that stage (39–43).

Fix a current stage numbered $\ell$ and an input node $H$ of one of its calls. The primal prefix producing $H$ contains at most $\ell-1$ stages. For an earlier output $q$, introduce an independent root vector $z\sim N(0,I_{N_t})$ on the output type of $q$, and propagate a physical tangent with seed $z$ added to that output. A primal call $Wh$ and its tangent call $W\dot h$ have the same name and orientation; both inputs are available before the original stage. They can therefore be placed in one enlarged batch. The designated addition of $z$ is a coordinate instruction after its batch. No call in that batch needs this addition, because no original input depends on another output in the same batch.

Thus neither tangent propagation nor the final average $n^{-1}z^TT_H$ creates a new stage. Adding a root and increasing a batch size remain within the induction quantifiers. This validates 304–310 and 363–370; the hypothesis is not being applied to a program of the current complexity.

The same argument applies to the retained cavity graph: deleting one or two sites changes only fixed deficits, while all variance and average denominators remain $n$. There is no hidden change of normalization in the probe identity.

## 2. Reconstruction of the formal tangent identity

For each original matrix call $r$, write $\xi_r$ for its formal primal source and $\eta_r$ for the separate source attached to its tangent matrix call. Let $Z$ denote the scalar representative of the added root $z$. On a given type the derivation in 315–324 is

$$
D=\sum_r\eta_r\partial_{\xi_r}
  +\mathbf 1_{\{q\text{ has this output type}\}}Z\partial_{\xi_q}.
$$

The sums contain that type's source slots. The derivation fixes original roots, previous expectations, covariance entries and scalar values. A primal field is a function only of original roots and primal source variables with these coefficients fixed. Therefore $DH$ is linear in the tangent sources and $Z$, with coefficients depending only on primal variables.

The following simultaneous induction is sufficient and is what 326–359 implement:

1. The enlarged evaluator's primal fields equal the original evaluator's fields.
2. Its tangent vector fields equal $D$ of those primal fields.
3. Its tangent scalar values are zero.
4. Every primal/tangent covariance entry within each oriented source group is zero; the resulting Gaussian blocks are independent. All source blocks remain independent of roots, including $Z$.

Coordinate maps satisfy item 2 by the finite chain rule and item 3 for their scalar arguments. For an average, its tangent integrand is conditionally centered given primal variables because it is linear in a centered tangent Gaussian family and $Z$ independent of those variables. Its expectation is consequently zero. Scalar arithmetic propagates zero tangents. The same conditional-centering calculation gives

$$
\mathbb E[H_r\,DH_t]=0.
$$

Hence the new primal/tangent source Gram entries vanish. Within the tangent block the covariance is the ordinary input Gram $\mathbb E[(DH_r)(DH_t)]$, which is positive semidefinite. Appending these blocks causally preserves the earlier laws. Gaussian independence here concerns the sources; tangent output fields can and do share primal-dependent coefficients.

The matrix step is the nontrivial part. For a forward call with primal input $H_r$, let $U_s$ be earlier reverse inputs, and let $\zeta_s,\theta_s$ be the sources for the primal and tangent reverse calls. The source rule of the enlarged tangent program gives exactly the two sums in 342–343:

$$
T_{Y_r}=\eta_r
 +\sum_s U_s\,\mathbb E[\partial_{\zeta_s}(DH_r)]
 +\sum_s DU_s\,\mathbb E[\partial_{\theta_s}(DH_r)].
$$

The first expectation is zero: differentiating a primal variable changes the coefficients of the tangent-linear expression without destroying its centered linearity. Before restriction to the Gaussian support,

$$
\partial_{\theta_s}(DH_r)=\partial_{\zeta_s}H_r.
$$

This holds because the coefficients of $DH_r$ contain no tangent slots and the coefficient of $\theta_s$ is precisely $\partial_{\zeta_s}H_r$. Thus

$$
T_{Y_r}=\eta_r+sum_s DU_s\,\mathbb E[\partial_{\zeta_s}H_r]
       =D\!\left(\xi_r+sum_sU_s\,\mathbb E[\partial_{\zeta_s}H_r]\right).
$$

At $q$ both sides receive the additional $Z$. The original primal call receives no contribution from earlier tangent reverse calls, because its primal input has zero derivative in all tangent slots. The same calculation with endpoint types interchanged treats reverse calls. This accounts for all response terms; no coefficient derivative has been silently dropped. The coefficients are constants in the evaluator, and the enlarged program itself proves that its potentially additional response coefficients vanish.

Since all tangent Gaussian source blocks are independent of $Z$ and primal variables, and $\mathbb E Z^2=1$,

$$
\mathbb E[ZDH^*]=\mathbb E[\partial_{\xi_q}H^*].
$$

This is an algebraic calculation on the evaluator of an already admitted program. It is not differentiation of a covariance, a Gaussian law, or a limiting theorem.

## 3. Why this identifies the physical Jacobian, including scalars

Let $J_n$ be the full finite derivative of $H$ with respect to an additive perturbation of the output $q$. Finite tangent propagation includes every finite scalar-average derivative, so $T_H=J_nz$ exactly (298–313). Conditional on the original initialization,

$$
\mathbb E_z\frac{z^TT_H}{n}
 =\frac{\operatorname{tr}J_n}{n}.
$$

By the earlier-stage induction and the calculation above, the random scalar $A_n=z^TT_H/n$ converges in every finite $L^p$ to $c=\mathbb E[\partial_{\xi_q}H^*]$. Conditional Jensen gives

$$
\mathbb E\left|\frac{\operatorname{tr}J_n}{n}-c\right|^p
\le \mathbb E|A_n-c|^p\longrightarrow0.
$$

Physical scalar feedback has therefore been included and subsequently shown to disappear from this normalized trace limit. It was not frozen in the finite derivative. The optional independent observation in 288–294 is consistent: removing every path containing a scalar tangent edge changes a fixed graph's Jacobian by a finite sum of rank-one maps. In the stated weighted norms each has operator norm $O_*(1)$, so its normalized trace is $O_*(n^{-1})$. The main probe proof does not need this optional observation.

## 4. Explicit small programs

These are exact checks of the mechanisms, not substitutes for the preceding induction.

**Scalar feedback.** Take $y=W\mathbf1$, $s=y^Ty/n$ and $H=sy$, and inject immediately after $y$. At zero deficits,

$$
J_n=sI+\frac2n yy^T,
\qquad
\frac{\operatorname{tr}J_n}{n}=s+\frac{2s}{n}.
$$

The full tangent has $\dot s=2y^Tz/n$ and $T_H=sz+\dot s\,y$. In the evaluator $s^*=1$, $\dot s^*=0$ and $H^*=\xi$, so its formal derivative is one. This matches the physical normalized trace limit and verifies the example at 545–546.

**Singular duplicate calls.** Take an independent standard Gaussian input root $h$, duplicate calls $y_1=Wh$ and $y_2=Wh$, and $u=y_1^2y_2$. The two primal sources satisfy $(\xi_1,\xi_2)=(G,G)$ on their singular support, where $G\sim N(0,1)$. Their distinct formal partials are

$$
\partial_{\xi_1}(\xi_1^2\xi_2)=2\xi_1\xi_2,
\qquad
\partial_{\xi_2}(\xi_1^2\xi_2)=\xi_1^2.
$$

The normalized physical injection traces converge to two and one respectively. A seed at the first output gives limiting tangent $2G^2Z$; a seed at the second gives $G^2Z$. Hence the reverse output has the two responses $2h$ and $h$ separately, as 542–544 state. Computing a derivative after merging the source arguments would not describe either single-output injection.

**Repeated round trips.** Let

$$
y=W\mathbf1,\quad v=W^Ty,\quad a=Wv,\quad b=W^Ta,\quad H=Wb.
$$

Write $\xi_1,\xi_3,\xi_5$ for the forward sources and $\zeta_2,\zeta_4$ for the reverse sources. Direct causal evaluation gives

$$
Y=\xi_1,\quad V=\zeta_2+1,\quad
A=\xi_3+\xi_1,\quad B=\zeta_4+\zeta_2+2,\quad
H^*=\xi_5+\xi_3+2\xi_1.
$$

The injection Jacobian from $y$ to $H$ is $(WW^T)^2$, and the predicted coefficient is $\partial_{\xi_1}H^*=2$. Independently, Gaussian pairings give $\mathbb E\operatorname{tr}((WW^T)^2)/n=2+1/n$. This confirms that repeated response paths are accumulated, not reduced to the most recent transpose. The tangent identity itself gives $DH^*=\eta_5+\eta_3+2\eta_1+2Z$ and therefore the required probe expectation two.

Zero tangent sources in these examples must still be retained as formal slots before restriction. Zero variance causes no division or covariance inverse anywhere in the calculation.

## 5. Closing the probabilistic induction

For the current batch, every covariance entry in 386–389 involves earlier-stage cavity inputs, so the strengthened hypothesis applies to their polynomial product test. Section 5 likewise applies to every nonzero trace in (C). Earlier scalars converge to deterministic limits. There is no need for the source vector to be independent of the traces: the latter converge to constants, which suffices for Slutsky's lemma.

Conditional on retained initialization, the source vector is centered Gaussian with covariance given by the old input Gram. For two deleted sites it has two independent copies of this covariance; their deleted Gaussian root tuples are also independent and independent of the retained initialization (277–286, 394–401). Convergence of covariance matrices to deterministic limits gives joint convergence by the displayed characteristic-function argument, without positive definiteness. Causal processing of the finite approximate recurrence (C) then gives one-site convergence and two-site convergence to independent copies of the source evaluator (403–412).

The adaptive deleted values multiplying quadratic-form errors cause no difficulty. They have uniform moments and hence are tight; a tight factor times an $o_P(1)$ error remains $o_P(1)$ even with dependence (263–266). The source/trace construction only requires finitely many such products.

For a polynomial-growth continuous test $f$, the all-order coordinate moments give uniform integrability of $f(V_1)$, $f(V_1)^2$ and $f(V_1)f(V_2)$. The exchangeability identity in 420–423 therefore proves convergence of the empirical average in $L^2$. Higher uniformly bounded empirical moments follow by Jensen, and interpolation yields every finite $L^p$ (425–428). The factors $N_t/n\to1$ are handled correctly.

Closing coordinate and scalar instructions after the batch (430–443) is also valid. A polynomial mean-value bound and Hölder control the error from replacing converging scalars by their limits. With those scalars fixed, the existing joint empirical law pushes forward under the coordinate map. Compact truncation and higher moments extend bounded continuous tests to polynomial-growth tests. The analogous one- and two-site conclusions, needed as auxiliary induction statements, follow at the same step by joint convergence with scalars tending to constants and the continuous mapping theorem; this is implicit in the paragraph but requires no additional theorem or hypothesis.

## 6. The Wasserstein and finite-derivative conclusions

The argument at 451–473 is a valid elementary bridge. A countable bounded-Lipschitz determining class together with the second-moment test gives a subsequence on which weak convergence and convergence of second moments hold almost surely. Their deterministic implication for $\mathcal W_2$ follows from truncating quadratic tails and matching masses in small cells. Extracting such an almost-sure further subsequence from every subsequence proves convergence in probability. The continuity estimate for empirical arrays also supplies the relevant measurability. No rate or positive-definiteness assumption enters.

Section 7 differentiates finite graphs before applying the primitive probabilistic theorem (475–524). It maintains the distinction between physical derivatives, frozen physical directional seeds, and formal source paths. Its statements about current ambient gradients, represented updates and moving-field second derivatives agree with the maintained finite rules in `docs:762–909`. The proof does not need a common ODE existence interval or analyticity, and does not exchange differentiation with width limits.

One useful expository completion is to add the vector-adjoint propagation at matrix calls to 486–489. In addition to the rank-one matrix-gradient contribution, a forward call $v=Wu$ adds $W^Tb_v$ to $b_u$, and a reverse call $v=W^Tu$ adds $Wb_v$. The complete rules are already cited at 477 and stated in `docs:809–824`; their omission from this summary is not a contradiction or a failure of exact compilation. I found no other actionable issue in the assigned sections.

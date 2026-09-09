# Independent document-only mathematical referee report

## Scope, provenance, and reading coverage

The mathematical input was exclusively:

`/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md`

The observed SHA256 was

`3d22121e563be632d78df5cb8116b124f73e22f89f2367e3c55032e25a61202d`.

It agrees exactly with the supplied frozen hash. I checked it before reading, again after the mathematical audit, and once more after writing this report. The observed file size was 81,710 bytes, with 1,785 lines.

I read the entire document, including the theorem, introductory qualifications, every displayed equation, all explanatory prose, and the final claims. The line-numbered reads covered 1–300, 301–600, 601–900, 901–1200, 1201–1500, and 1501–1785, without gaps or truncated tool output. References below are to those observed line numbers. This was an audit of the full theorem, not just the Gaussian calculation or a continuation lemma.

Complete source-access list:

1. The proof file above: the sole source of mathematical assertions, constructions, and evidence.
2. `/etc/codex/skills/solve-math-rigorously/SKILL.md`: read completely as a procedural instruction. It instructed careful hypothesis checking, complete arguments, and an internal audit. It supplied no mathematical dependency or evidence. Its general suggestion to consult external sources was not used: the user's document-only restriction governed this review.

The requested report is the sole output file created. I also reread this newly generated report to check the output artifact and its formatting; it was not an additional mathematical evidence source. No other project or research file, previous review, audit record, conversation, or agent output was inspected. No agent was contacted. No browsing, simulation, or numerical experiment was performed. File hashing, counting, and line-numbered reading were the only diagnostic operations on the input. All mathematical checks below are analytic checks of the supplied document; no resemblance to an outside research theorem is used as support.

## Assessment

The full stated theorem is proved by the document. I found no false mathematical assertion or missing mathematical step that requires repair. In particular, the proof supplies the specialized Gaussian-program argument it needs, handles singular queries without assuming continuity of inverse Gram matrices, constructs actual bounded operators and their adjoints on fixed spaces, and obtains empirical and whole-path convergence rather than only a representative-coordinate distribution.

There is one local layer-typing ambiguity in the introductory notation of Section 3.1, recorded separately below. It does not invalidate the calculation or leave a theorem obligation undischarged: the needed same-layer formulation and its averaging proof are present in Section 3.2 and are used in the applications. I found no required mathematical repair associated with it.

## 1. Exact statement, normalization, and elementary tools

**Locations: lines 18–256.**

The finite model defines its updates explicitly. Differentiating the predictor with vector squared norms normalized by $1/n$ and ordinary matrix Frobenius squared norms gives exactly the four vector-field components in (1.3). In particular, the matrix gradient is $\delta^{(\ell)}(h^{(\ell-1)})^T/n$, whereas the first-vector and readout gradients are $\delta^{(1)}$ and $h^{(3)}$. The four kernel normalizations in (1.6) agree with their squared gradient norms. The later population Hilbert metric matches these normalizations.

The initial readout vanishes in the relevant vector norm: its expected normalized squared norm is $n^{-2}$. Treating its population initial value as zero is therefore legitimate only together with a stability argument; that argument is provided in Sections 8 and 10, rather than assumed at initialization.

The activation estimates are valid. The bounds $5/6<\phi<7/6$, $0<\phi'\le1/10$, and $|\phi''|\le1/5$ follow from the displayed formula. The first-coordinate change has

\[
F'(z)=10(1+z^2)=1/\phi'(z),\qquad
(F^{-1})'\le1/10,\qquad
(\phi\circ F^{-1})'=(\phi'\circ F^{-1})^2\le1/100.
\]

The non-Lipschitz map $F$ is used as an initial root component with finite moments, not silently inserted into the Lipschitz Gaussian-program class.

The net proof of the initial operator bound has the correct scaling and a decaying union bound: $2\,9^{2n}e^{-100n/8}\to0$. A fixed finite number of uses of either matrix does not require new norm events for that matrix.

The elementary convergence tools have the hypotheses later applications require. Weak convergence plus second-moment convergence gives squared-tail control and hence $\mathcal W_2$ convergence. Continuous quadratic-growth tests are controlled by this tail control. The bounded-multiplier assertion (2.4) is a strong $L^2$ statement with an $L^2$-convergent unbounded factor; it is not an assertion that multiplying weakly convergent fields preserves strong convergence. The curve chain rule uses bounded derivatives and this multiplier result. The discrete and integral Gronwall comparisons are proved in the needed forms.

## 2. Adaptive Gaussian conditioning in both directions

**Locations: lines 258–369, especially (3.1)–(3.4).**

The introductory forward and transpose formulas have the correct covariance. After observing $Wh=y$, the residual matrix is $\widetilde W P_{h^\perp}$. For an input $u$ known without seeing that residual,

\[
W^Tu=h\frac{y^Tu/n}{\|h\|^2/n}
       +\frac{\|u\|}{\sqrt n}P_{h^\perp}g.
\]

Consequently the first reverse source has variance equal to the full second moment of its input. Subtracting the squared response coefficient from that variance would be incorrect; the document does not do so.

For multiple observations, the conditional mean in (3.3) satisfies both constraints. Indeed its product with $V$ is $Y$, while its left product with $U^T$ is

\[
U^TY(V^TV)^{-1}V^T+Q^TP_{V^\perp}
=Q^TP_V+Q^TP_{V^\perp}=Q^T.
\]

The homogeneous matrices satisfying both zero constraints form exactly the subspace represented by $P_{U^\perp}\widetilde W P_{V^\perp}$. Orthogonal projection of the isotropic Gaussian entry vector therefore gives the stated residual law.

Adaptation is handled with the correct filtration. A new input is measurable with respect to the preceding transcript. Observing its answer adds a linear observation of the queried matrix with that input now fixed. Induction over the observations preserves the Gaussian residual description. For two initially independent matrices, each such observation conditions only the residual of the queried matrix, so the two conditional residuals remain independent. Coordinate instructions reveal functions of the existing transcript, not new observations of an unexplored matrix component. This justifies the adaptive use of the conditional law; treating all random constraints as exogenous without this induction would not suffice.

I also checked the reverse counterpart of (3.4), not just the displayed forward formula. With

\[
\gamma_n=(U^TU)^{-1}U^Tu,\qquad u_\perp=u-U\gamma_n,
\]

it is

\[
W^Tu\mid\mathcal F\ \overset d=
Q\gamma_n+
V(V^TV/n)^{-1}(Y^Tu_\perp/n)
+\frac{\|u_\perp\|}{\sqrt n}P_{V^\perp}g.
\]

This follows by transposing (3.3) and using the same compatibility identity. Thus interchanging the orientations does give the asserted rule, with the correct projection and normalization.

The discarded projections have fixed rank for a fixed program. Their normalized squared Gaussian norms have expectation at most that rank divided by $n$. Their multipliers are bounded in probability by the input second moments. This proves that their removal costs $o_{\mathbb P}(1)$ in normalized vector norm; it does not assert that the exact reused answers have independent coordinates.

The empirical averaging argument is sufficient. After this removal, conditional independence of the newly introduced Gaussian coordinates yields the stated $O(1/n)$ conditional test variance. The conditional expectation is an old empirical average with converging deterministic limiting coefficients. For squared norms, both the Gaussian-square fluctuation and its cross term with the known mean vanish with the displayed bounds. Applying the argument to the old tuple augmented by the new answer proves joint empirical convergence and second-moment convergence. The reasoning is not restricted to a randomly selected coordinate.

## 3. Gaussian sources, formal derivatives, and singular queries

**Locations: lines 371–471.**

The source/response rule is derived from the conditional projection formula. In the positive-definite case, $h_\perp$ is $L^2$-orthogonal to all preceding same-direction inputs. The nongeneric part of an old reverse answer is a deterministic linear combination of precisely those inputs. Its pairing with $h_\perp$ therefore vanishes. Gaussian integration by parts on the remaining source gives

\[
\mathbb E[\zeta h_\perp]
=\Gamma_U\left(\mathbb E\nabla_\zeta h
        -\sum_r\alpha_r\mathbb E\nabla_\zeta v_r\right).
\]

The response terms in the old forward answers then cancel the subtraction term, giving (3.5). The same argument applies to the reverse orientation.

The derivative convention is essential and correctly specified: derivatives act on the full explicit coordinate expression, with the already selected deterministic coefficients and covariance parameters fixed. They are not derivatives of a covariance square root, nor derivatives of the map selecting the population coefficients. The oracle construction in Section 4 justifies using this convention for the actual feedback program.

The source covariance calculation is also correct. Adding an independent residual source to the least-squares combination of preceding sources gives covariance $\mathbb E[h v_r]$ and variance $\mathbb E[h^2]$, including input means. New innovations are independent of all preceding groups, and their within-group recombinations use deterministic coefficients. This preserves independence of the distinct oriented source groups and of the initial roots. Integration by parts can be performed after conditioning on the other independent groups. For singular Gaussian laws, the document gives the elementary $\zeta=AG$ reduction; it does not assume a nonexistent full-dimensional density.

The singular-query argument is valid for a fixed finite program:

- A fresh independent input root of size $\epsilon$ is introduced immediately before each query. Its contractions with earlier inputs and the original new input vanish in the empirical limit. Every limiting Gram Schur complement therefore has an additional $\epsilon^2$, and the positive-definite argument applies at fixed $\epsilon>0$.
- Coupling the perturbed and original finite programs using the same matrices gives a $C\epsilon$ error through all finitely many instructions. The initial operator bound and the finitely many noise norms supply a width-independent constant. This is a comparison of complete programs, not an assumption that nearly singular inverse Gram matrices converge.
- The limiting source recursion has no inverse-Gram operation. Causality allows a finite induction bounding its deterministic coefficients and formal derivatives: bounded first derivatives of the primitive maps and bounded previously constructed coefficients bound the next derivatives and their expectations. The coefficients are therefore in a bounded set for this fixed program.
- Covariances converge by second moments. Continuous positive-semidefinite square roots give a coupling of each finite Gaussian source vector, including at rank drops. Continuity of the $C^1$ expressions and boundedness of their formal derivatives justify the $L^2$ and dominated-convergence passages used for the next instruction.

No mesh-uniform constant is needed in this step. The document separately proves the uniform response bound that is needed for mesh refinement.

The null-space observation at lines 465–471 is correct: if $v\in\ker\Gamma_U$, then $\mathbb E[(u^Tv)^2]=0$, so an ambiguity in derivative coefficients in that direction cannot change the contracted response. In particular, a source slot of zero variance is not automatically assigned zero formal derivative. This matters at initialization and is respected later.

## 4. Actual feedback and current-time returns

**Locations: lines 473–615.**

The clipped Euler program is an Euler scheme in $X^{(1)}$ and feature time. It is expressly distinguished from exact raw GD. Its unrolled matrix actions consist of the initial action plus the rank-one learned sums in (4.2), with the correct $1/n$ contractions and strictly earlier update times.

At a fixed number of steps and fixed clipping level, the top readout and both clipped backward products are bounded coordinatewise as required. Smooth extensions outside attained bounds put the oracle program inside the $C^1$, globally Lipschitz class without changing its attained values or derivatives. The root pair includes $F(Z^{(1)}_0)$ separately.

Freezing the finitely many contractions first is legitimate. Their oracle empirical errors vanish by the Gaussian-program result, and the displayed contraction-difference inequality and finite Lipschitz induction propagate this to the actual program. This does not claim a Gaussian induction uniform over the width-dependent number of GD steps.

The causal order in (4.3)–(4.5) is correct. A forward input at step $k$ uses only previously available reverse sources. The reverse input at the same step already contains the current forward answer, so its response sum includes $k$.

In particular, differentiating the complete current middle reverse input gives

\[
\partial_{\xi^{(2)}_k}\delta^{(2)}_k
=\phi''(Z^{(2)}_k)\tau_R(q^{(2)}_k)
+b^{(3)}_{kk}(\phi'(Z^{(2)}_k))^2\tau'_R(q^{(2)}_k).
\]

Here $\partial_{\xi^{(2)}_k}Z^{(2)}_k=1$, and the current term in $q^{(2)}_k$ contributes $b^{(3)}_{kk}\phi'(Z^{(2)}_k)$. Its expectation is exactly (4.6). The return through the other matrix is present. Past-source derivatives are likewise derivatives of the complete expressions, rather than a reduced direct path.

## 5. Fixed spaces and genuine adjoints

**Locations: lines 617–786.**

The construction uses a countable collection of finite programs closed under finite unions and the specified operations. Its finite marginal laws are consistent because every finite union is the limit of the same finite-width computations. The countable measure-extension principle applies to real coordinate slots with their Borel laws and these consistent marginals. It is applied separately to each neuron population, so it does not impose coordinate pairing between populations.

The claimed density of generated coordinate functions in each $L^2$ space is justified. The sigma field is generated by the countable slots. Projection onto increasing finite-slot subspaces approximates $L^2$ functions; truncation and finite-dimensional Borel regularity reduce to bounded continuous functions; the included countable smooth family approximates those on compact sets. These are foundational measure/Hilbert-space facts in precisely the settings stated in the document.

Passing the finite high-probability operator inequality to the limiting second moments yields a deterministic bound for every generated rational linear combination. In particular, an input equal to zero in $L^2$ has output equal to zero in $L^2$. The map is therefore well-defined on equivalence classes and extends continuously to the completed space. Real linearity follows by continuity. The same construction gives the reverse action.

The adjoint identification does not follow merely from having two bounded maps, and the document supplies the additional needed step: finite transpose pairings pass to the two same-layer limiting scalar expectations in (5.2). These pairings are continuous in the $L^2$ inputs and bounded operators, so density extends the identity to all inputs. The reverse action is consequently the Hilbert-space adjoint of the forward action.

The resulting initial operators are deterministic maps between fixed spaces, with their Gaussian finite-program laws. The theorem does not need them to have a Hilbert–Schmidt kernel. Nor does it claim operator-norm convergence between operators acting at different widths. Additional real coefficients and fixed Lipschitz probes can be approximated on these same spaces using the bounded actions and $L^2$ tail control; no new space is needed at a new Euler mesh.

The coarse estimates (5.5) are deliberately loose but valid. They successively bound readout, matrix 3, matrix 2, and the first-coordinate velocity, using bounded activations and $|\tau_R(q)|\le|q|$. For the zero-readout reference, integrating the activation floor and ceiling gives the pointwise bound (5.6).

The stability estimate uses the bounded reference readout in the correct place. In the top gate difference, its pointwise bound multiplies the preactivation difference, while the difference of readouts is controlled in $L^2$. No $L^\infty$ bound on the other readout is required. The middle gate becomes Lipschitz with constant $O(1+R)$ after clipping. These bounds hold with the same normalizations at finite width.

The fixed-clip integral map is a contraction on a closed set of paths with the stated bounds. The pointwise readout constraint is closed under $L^2$ convergence, and the integral map preserves it. The a priori bounds permit continuation over each fixed feature interval. The Euler defect is $O(\Delta^2)$ for fixed clip, giving (5.8). Finite time nets and finite probe stability supply the asserted fixed-clip uniformity.

## 6. Mesh- and clip-uniform response estimate

**Locations: lines 788–974.**

I checked the induction and its constants. It uses only strictly preceding response rows until the current top reverse row has been established.

At initialization, zero readout makes $\delta^{(3)}_0$ and its relevant forward-source derivatives vanish. Then the current middle forward-source derivative vanishes as stated, so $U_0=V_0=0$. This does not erase formal derivatives with respect to a degenerate backward source.

For a fixed bottom reverse source, entering the first-coordinate time sum contributes $\Delta$, and the derivative of $\chi$ contributes $1/100$. The Gronwall bound (6.2) is therefore uniform in the number of steps. It gives $|a^{(2)}_{js}|<A\Delta$, $A=3/2$, without needing a pointwise bound on $q^{(1)}$.

The middle derivative estimates retain both the gate derivative $|q^{(2)}|/5$ and the return derivative $V_r/100$. Summing over forward-source indices contributes exactly one direct derivative at a given forward row. A single backward source first contributes through one time update and has the additional $A\Delta/10$ factor. These are the recursions (6.3) and (6.4).

The random envelope is bounded in moments, not uniformly over neurons. Jensen's inequality over time slots uses only marginal Gaussian exponential moments, so correlations or singular temporal source covariances do not invalidate (6.5). The worst-case exponents are

\[
AS(a/5+1/100)=219/400,\qquad
\tfrac12(AS/5)^2(aS/10)^2=3969/1280000.
\]

They give $\|E_j\|_1<4$ and $\|E_j\|_2<3$, as used. The resulting $a^{(3)}$ coefficient is less than $A\Delta$.

The top derivative includes both the differentiated readout integral and the differentiated top gate. Their sum has coefficient $S(1/100+a/5)=73S/300$. Its Gronwall exponent at $S=3/2$ is $657/800$, and the elementary estimate $e^{657/800}<5/2$ is valid. Including the learned covariance terms gives

\[
V_k\le 73/80+147/3200=3067/3200<1.
\]

Only after obtaining that current bound does the proof use

\[
\|q^{(2)}_k\|_2\le Q=161/120
\]

and close the current middle row by

\[
U_k\le3(Q/5+1/100)+SQ^2/100
=2482563/2880000<9/10.
\]

This order avoids a circular bound on the current $U_k$. The covariance contribution is controlled by Cauchy–Schwarz, and the random derivative envelope by its $L^2$ norm; no unavailable pointwise bound is used.

Thus the actual scalar query has a Gaussian source of variance at most $(7/40)^2$ plus a shift bounded by $7/6$. The exponential-square estimate (6.11) follows even if the shift depends on that source. Its uniformity is marginal in time, which is sufficient for the subsequent comparisons. No Gaussian supremum-over-time estimate is assumed.

## 7. Removal of clipping, existence, uniqueness, and restart

**Locations: lines 976–1105.**

The passage from fixed-clip Euler queries to fixed-clip flow queries is strong $L^2$. Applying Fatou along an almost-everywhere convergent subsequence at each fixed time gives the same deterministic exponential bound at every time and clip. A simultaneous almost-sure convergence event for all times and clips is unnecessary.

The decomposition (7.2) is algebraically exact. It puts the gate-difference multiplier under the reference clip $R$, and the discrepancy between clips is supported outside $|q_B^{(2)}|\le R$. Consequently (7.3) has a stability constant depending on $R$, not on the larger clip or on an uncut competitor's tails.

The continuous function $b_R(q)=(|q|-R/2)_+$ controls this tail discrepancy. The Gaussian exponential-square bound implies (7.4), with decay $e^{-R^2/(16K^2)}$, $K=4$. This decay absorbs every fixed comparison factor $e^{CR}$, and also the additional factor $1+R$ needed for velocity convergence.

The clipped states are therefore Cauchy in the continuous-path Banach norm. More is proved than convergence of states: applying the same asymmetric estimate to the limiting state shows that its actual uncut vector field is the uniform limit of the clipped velocities. Passing the integral equations is consequently legitimate and gives a $C^1$ uncut solution on the full interval $[0,3/2]$. There is no passage of an uncontrolled product under weak convergence.

For any other bounded-primal uncut integral solution, the same comparison needs only its finite primal bounds and the reference solution's tail estimate. Letting $R\to\infty$ proves uniqueness. At a reached feature time, the initial discrepancy from the clipped reference already has Gaussian decay times an exponential in $R$; a further comparison interval multiplies it by another such exponential. It still vanishes. This proves restart uniqueness on the remaining constructed feature interval without assuming local Lipschitz continuity of the uncut vector field on arbitrary $L^2$ neighborhoods.

For the finite-width passage, $b_R^2$ is a continuous quadratic-growth test. Fixed-clip empirical convergence gives its norm at each time, and time-Lipschitz bounds give the uniform convergence (8.1). This is the appropriate replacement for a finite-width exponential-tail assertion, which is neither available nor used.

The small nonzero finite readout is then restored by comparison to the zero-readout reference. Its normalized norm tends to zero, and only the reference needs a pointwise readout bound. Taking width to infinity at fixed clip and then removing the clip proves the finite uncut feature-flow law. The same estimate explicitly controls $\delta^{(2)}$ and then $q^{(1)}$, so the state comparison does not leave those unbounded backward observables unidentified.

## 8. Gradient structure and all finite physical horizons

**Locations: lines 1107–1235.**

Although the initial Gaussian actions need not be Hilbert–Schmidt, their trained increments are integrals of continuous rank-one Hilbert–Schmidt velocities. The rank-one norm and difference estimates hold in Hilbert–Schmidt norm as well as operator norm. Thus the raw trajectory belongs to the claimed affine Hilbert parameter space.

The proof of scalar predictor differentiability is adequate. For a fixed $B\in L^2$, the remainder estimate (9.2) first truncates $B$. The bounded part contributes $O(R\|v\|_2^2)$; the tail contributes $O(\|B1_{|B|>R}\|_2\|v\|_2)$. Taking the small-increment limit before the tail limit proves a scalar $o(\|v\|_2)$ remainder. Top-down expansion applies this to the old readout and old backward factors, each in $L^2$. Terms involving two parameter/activation differences are quadratic because Hilbert–Schmidt norm controls operator norm.

This proves the displayed Fréchet derivative and gradient without asserting Fréchet differentiability of the activation map $L^2\to L^2$. Gradient continuity follows by successive bounded-multiplier continuity and operator continuity. The constructed raw curve has the needed Hilbert-space differentiability for the scalar chain rule.

The feature field is exactly $\nabla f$ in raw coordinates: the inverse-coordinate derivative supplies $(Z^{(1)})'=\phi'(Z^{(1)})q^{(1)}=\delta^{(1)}$. Hence $f_s=\sum_\ell K^{(\ell)}$, with $K^{(4)}\ge25/36$. Starting from $f(0)=0$, the unique level-one point satisfies $0<s_*\le36/25<3/2$.

The inverse physical clock is justified at its potentially problematic endpoint. Boundedness of $f_s$ gives $1-f(s)\le B_*(s_*-s)$, which makes the integral defining $t(s)$ diverge logarithmically. The inverse clock therefore exists for every finite physical time and stays strictly below $s_*$. The physical gradient and loss identities have the correct signs and factors.

Raw-coordinate uniqueness is not simply inferred from uniqueness in the transformed class. For a raw competitor, continuous backward fields and Hilbert–Schmidt increments justify the predictor chain rule and the deficit exponential formula. Coordinatewise absolute continuity and the ordinary scalar chain rule then give (9.8); its right side is $L^2$, establishing the transformed membership that had not initially been assumed. The positive deficit allows reparametrization, and feature uniqueness and scalar-clock uniqueness exclude exit at finite physical time. The same argument starts at any reached state, whose transformed first coordinate is already known to be $L^2$.

The source process is not extra forcing in these equations. It is used to construct and estimate the fixed-space solution; the current four objects and the adjoint operations determine its vector field.

## 9. Exact raw GD and interpolation

**Locations: lines 1237–1386.**

Finite physical GF exists on every finite interval: the deficit identity bounds the residual, and successive readout, matrix, and first-coordinate estimates prevent finite-dimensional escape. On the high-probability initialization event, the finite feature predictor crosses one before $3/2$, since $f_n(0)>-1/24$ and $f_{n,s}\ge25/36$. Uniform feature-predictor convergence and a uniform Lipschitz bound justify the finite physical-clock comparison.

The raw GD argument addresses the actual step size $n^{-2}$ and does not replace it by a fixed Gaussian program. The positive feature increments are defined only before the stopping conditions. The first potentially bad endpoint is included in the estimates: its preceding step is positive and is at most $C\eta_n$, so it still lies within the available feature interval.

The exact cubic identity (10.1) is correct. The quadratic and cubic correction vectors have normalized norms bounded by

\[
C(\alpha_k^2\sqrt n+\alpha_k^3 n).
\]

This follows from the elementary finite-vector inequalities stated there and the bounded normalized $q^{(1)}$ norm. It does not presume empirical fourth or sixth moments. Summing over a positive prefix of bounded total feature time gives

\[
O(\eta_n\sqrt n+\eta_n^2n)=O(n^{-3/2}+n^{-3}),
\]

which vanishes.

The comparison recurrence includes this defect, the clipped Euler defect, the state discrepancy, and the reference tail forcing. The partition can be random: the Riemann-sum estimate (10.4) is pathwise, using the reference forcing's time-Lipschitz property. This justifies the accumulated error estimate without independence assumptions on the adaptive step sizes.

The stopped predictor and clock errors tend to zero. At a putative first bad endpoint, the fixed margin $36/25<147/100$ excludes the feature-time exit, and the deficit margin on $[0,T+1]$ excludes the prediction exit. The extra interval covers the last interpolation node. Thus the stopping construction is closed without assuming in advance what it is meant to prove.

For points inside a raw interpolation step, the fractional version of the same cubic identity controls the difference between transforming the raw interpolant and interpolating transformed nodes. Comparing both GD and finite GF with the same finite clipped reference at their respective converging clocks proves the same-width distance assertion (1.7).

The final order of approximation is consistent: select a clip, select a fixed reference mesh, and then take sufficiently large widths; afterward the deterministic clipping and mesh errors can be made arbitrarily small. The Fatou subsequences used for a moment estimate do not restrict the final width sequence. No infinite-training-time limit is interchanged with width.

## 10. Probes, unbounded factors, velocities, and whole paths

**Locations: lines 1388–1501.**

The observable argument covers the additional fields in the theorem. Lipschitz functions, bounded products, and bounded matrix actions propagate same-width and population comparisons directly. The middle backward field is covered by the asymmetric comparison, and the lower backward query by the bounded reverse action.

For a bounded continuous gate times an unbounded $L^2$ field, the proof first truncates the field. The resulting bounded expression can be approximated by the permitted Lipschitz probes. The discarded norm is controlled by squared tails, uniformly over time because the limiting $L^2$ path has compact image and the empirical laws converge uniformly in $\mathcal W_2$. Subsequent matrix calls multiply this error only by a bounded operator norm. This supplies the missing ingredient that state convergence alone would not give for all unbounded gate-containing expressions.

Predictions and squared backward norms are quadratic-growth measurements. The kernel blocks are the correct products of these scalar expectations. Thus their convergence follows with the claimed normalization and uniformity.

I checked all three preactivation derivatives in (11.1). Differentiating each forward operator action gives its learned rank-one contribution plus the action on the previous layer's feature derivative. For layer 2, the latter is $W^{(2)}[(\phi'(Z^{(1)}))^2q^{(1)}]$; the square of the first gate is necessary and is present. Feature derivatives and the physical multiplier are then correct.

For raw GD, these formulas initially describe node fields, not automatically the velocities of recomputed intermediate features. The document supplies the necessary separate argument. Raw block velocities have bounded normalized norms, and a hidden preactivation changes in coordinate supremum by at most $C\eta_n\sqrt n$ on one step. Bounded $\phi''$ gives the same order for gate changes. In (11.2), contraction and matrix changes are $O(\eta_n)$; the gate multiplier contributes $O(\eta_n\sqrt n)$. The next layer and feature derivatives follow successively. Since $\eta_n\sqrt n=n^{-3/2}\to0$, the actual recomputed velocities have the stated limits, including the terminal-left convention.

Uniform convergence of squared velocity norms gives convergence of their time integrals. Population $L^2$-continuous velocities have jointly measurable versions; integrating them produces absolutely continuous scalar paths with finite expected squared supremum norm. Finally, (11.3) controls path interpolation error by the integrated squared velocity, in both empirical average and population expectation. On a fixed grid, the joint finite-time laws converge; the interpolation map is Lipschitz into $C([0,T])$. The triangle argument with a refining grid proves the claimed path-space $\mathcal W_2$ convergence. Finite-dimensional weak convergence alone is not being used as a substitute for path convergence.

## 11. Nonlinear feature learning and absence of later freezing

**Locations: lines 1503–1785.**

The initial forward variances in (12.1) use full second moments and the oddness of the arctangent under a centered Gaussian law. The constant activation offset is retained.

The first initial transpose law has a source variance $\mathbb E[(B^{(3)})^2]>0$. Its response coefficient $c_3$ is positive for the reason stated: the odd part of the Gaussian expectation cancels, leaving a strictly positive integrand $z\arctan z/(1+z^2)$ off zero. This is not a pointwise positivity claim for $z\phi(z)\phi'(z)$.

For the second transpose, conditioning on the first-layer roots, the second preactivation, and the entire independent third matrix makes the actual reverse input known while leaving the appropriate second-matrix Gaussian residual unexplored. The conditional transpose formula therefore applies. The needed contractions converge empirically, and truncation handles the unbounded gated input. The resulting variance $\sigma_2^2$ and coefficient $c_2$ in (12.4)–(12.5) have the displayed values and strict positivity.

The adjoint identities in (12.6) are correct. In particular, the lower-layer term in $\mathbb E[B^{(2)}V^{(2)}]$ is $\mathbb E[(B^{(1)})^2]$, and the corresponding top pairing is the sum of all three positive hidden gradient contributions. This excludes cancellation in the initial preactivation movement coefficients.

The second-order expansions follow from strong continuity of the readout integral, bounded multipliers, and bounded operator continuity in reverse order. The $L^2$ velocity remainder is integrated explicitly, giving the required $o(s^2)$ state remainder. Matrix increments have the analogous Hilbert–Schmidt expansion. The readout kernel's second-order coefficient is $\Gamma$, so the total feature-time kernel coefficient is $2\Gamma$; using $s(t)=2t+o(t)$ gives precisely the factors $4\Gamma$ and $8\Gamma$ in (12.8). The integrated physical-velocity coefficients $16/3$ are also consistent. These statements prove nonzero initial hidden motion and a nonconstant total kernel at fixed width-independent physical scales.

The later-time nonaffinity argument has the required support control:

- At the top, the correction to the forward Gaussian source is bounded by $63/160$, so both Gaussian lower tails survive without an independence assumption on that correction.
- In the middle, the displayed dominating variable depends only on the backward source group and is independent of the current forward source. Its expectation is at most $483/1600$, giving the stated independent-event bound. The actual correction itself need not be independent.
- At the bottom, the dominating variable is independent of the initial Gaussian root, has expectation $1561/800<2$, and is used with the increasing odd function $F$. This gives the stated lower bound for both signs.

The lower bounds are uniform in mesh, clipping, and time index. The closed-half-line weak-convergence inequality is used in its correct direction: a limit law assigns a closed set at least the limsup of the approximating probabilities. Thus these positive lower tail bounds pass to each reached flow time without assuming atom-free limiting laws.

For a square-integrable nonconstant $Z$, the least-squares affine-error formula (12.12) follows by minimizing first over the intercept and then the slope. If that attained error were zero, boundedness of $\phi$ and the unbounded support just proved would force zero slope; strict monotonicity would then force a constant $Z$, a contradiction. Continuity of all displayed moments along the $L^2$ path, and compactness of a physical time interval, give a strictly positive uniform lower bound. The empirical version follows from the already established uniform second-moment convergence and a denominator bounded away from zero.

Finally, the no-freezing argument is sequential, not circular. Positive readout and a strictly positive gate make $\delta^{(3)}(s)\ne0$. Approximating Gaussian reverse sources then have variance bounded below, and their uniformly bounded response shifts force unbounded support of $q^{(2)}(s)$. This gives $\delta^{(2)}(s)\ne0$; repeating the same reasoning gives $\delta^{(1)}(s)\ne0$. The adjoint pairings (12.13) exclude cancellation of the middle and top preactivation velocities. A strictly positive gate cannot annihilate a nonzero $L^2$ field. The physical clock multiplier remains positive at every finite positive physical time. This proves all the claimed nonzero feature-velocity statements, not just initial movement.

## 12. Theorem invocations and limit-order audit

The specialized arguments required by this theorem are supplied inside the document. In particular, it does not assume an external tensor-program theorem, a general mean-field theorem, a Banach-space existence theorem for merely continuous vector fields, or an external continuation result for the uncut population system.

The foundational facts used have their relevant hypotheses available: finite-moment iid roots for the law of large numbers; finite-dimensional Gaussian linear observations for orthogonal conditioning; bounded formal derivatives and integrable roots for Gaussian integration by parts; consistent Borel finite-coordinate laws for countable extension; sigma-field generation and square integrability for Hilbert projections; bounded continuous rank-one velocities for the operator and Hilbert–Schmidt integrals; and the stated domination, positivity, or strong convergence for Fatou, Fubini, chain rules, and limit passages. Finite-dimensional smooth continuation is supported by actual compact-interval parameter bounds. No unproved heavy research result is needed to bridge the argument.

The approximation orders are compatible throughout:

1. Query perturbations are removed for each fixed finite Gaussian program.
2. Empirical contractions are restored for each fixed finite Euler program.
3. At fixed clip, a fixed mesh is used for the width limit, then refined using dimension-independent stability.
4. The mesh- and clip-uniform response estimate gives reference tails, allowing removal of clipping in the common spaces and in finite-width comparisons.
5. Physical clocks are compared on a fixed finite physical horizon; the separate stopped raw-GD proof treats its width-dependent mesh.
6. Unbounded observable truncations and path-interpolation meshes are removed using the proved uniform tail and velocity controls.

There is no inverse-Gram limit hidden at a singularity, no weak-to-strong product substitution, no unsupported independence of reused coordinates, and no passage from a one-coordinate law to empirical convergence without an averaging argument. Cross-width statements remain empirical/action-law statements. Operator-norm comparisons occur on common population spaces or at the same finite width, as the theorem requires.

## 13. Actual notation ambiguity versus optional style

**N1 — Local layer-typing ambiguity, notation only.** At lines 296–301, the introductory phrase “the empirical joint law of $(h,y,u)$” places an input-side field $h$ in a tuple with output-side fields $y,u$. Equal finite widths make a same-index triple writable, but the theorem explicitly does not supply a coordinate pairing between different neuron populations. Likewise, “that old tuple” at lines 299–300 could misleadingly suggest a population triple on one neuron space.

The precise formulation needed there is: the old input-population tuple containing $h$ has its joint empirical limit, while the output-population pair $(y,u)$ supplies the limiting contraction $\mathbb E[YU]$ and second moment $\mathbb E[U^2]$; the fresh scalar $G$ is independent of the old input-population tuple. This clarifies the typing and preserves exactly the displayed answer $cH+\sigma G$.

Severity: minor notation ambiguity. The clarification does not require a new mathematical argument. The finite conditional formula immediately uses only these same-layer quantities, Section 3.2 proves the requisite general same-layer averaging statement, and Section 12.1 checks the corresponding pairings explicitly. No downstream step relies on a cross-layer empirical coordinate pairing. It is therefore not a defect in the proof of the stated theorem.

I found no other erroneous or consequentially ambiguous notation requiring correction. Reuse of locally defined letters, the context-dependent finite/population notation for the backward fields, and leaving the reverse version of (3.4) to an explicitly stated orientation interchange are not mathematical defects. Further stylistic expansions or different notation would be optional and are not conditions on this verdict.

## Final verdict

**PASS.** The entire stated theorem is proved with no required mathematical repair. There are no outstanding mathematical discharge obligations. The one local notation clarification above does not qualify or weaken this verdict.

Report path: `/tmp/l3-standalone-proof-D6AW4s/ROUND_3_REVIEW_A.md`

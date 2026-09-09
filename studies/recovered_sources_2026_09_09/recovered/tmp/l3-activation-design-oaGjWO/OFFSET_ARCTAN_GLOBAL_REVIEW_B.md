# Independent exact-hash audit of the offset-arctangent global theorem

**Full-theorem status: PASS.**

I find no remaining fatal mathematical gap in this proof package for the fixed activation \(\phi(z)=1+\arctan(z)/10\), with the initialization, raw updates, physical time, and observable interpretation specified in the candidate. This is a proof audit, not numerical evidence. The conclusion is convergence in probability along the full width sequence on each fixed finite physical interval; it does not assert an interchange with infinite training time.

The inherited finite-program argument has been checked as an argument, rather than accepted on provenance. The new numerical bootstrap, its same-time returns, the common operator realization, cutoff removal, arbitrary-competing-solution uniqueness, the actual raw-GD comparison, and the later-time nontriviality claims all close. Details below explain the substantive checks and the scope of this verdict.

## Scope, isolation, and exact inputs

I read /etc/codex/skills/solve-math-rigorously/SKILL.md completely. The mathematical inputs read were exactly these three complete files:

| Alias | File | Verified SHA256 |
| --- | --- | --- |
| G | /tmp/l3-activation-design-oaGjWO/OFFSET_ARCTAN_GLOBAL_THEOREM.md | d50b7708b767f20010437e48a716366ac32b5dd6db6e6e12beb94cd1d15897e5 |
| R | /tmp/l3-activation-design-oaGjWO/OFFSET_ARCTAN_RESPONSE_BOOTSTRAP.md | 65579a94f883f1b9f9240430039f334f5b3b663599cd7ab16bb15c35f7bacc43 |
| L | /tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md | f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4 |

Line references below refer to these exact versions. I read G through line 822, R through line 273, and L through line 2321. I did not inspect any other review, worker note, history, source task, or repository file. I used no agents or simulations and did not change any of the three inputs. References in L to its constituent notes were assessed through the material actually included in L, without opening those other files.

The theorem under review is the changed-activation instance. The arctangent-only local horizon and oddness-based positivity statements in L are not being imported as assertions about the new activation. G replaces those parts explicitly.

## Status by obligation

| Obligation | Status | Main locations |
| --- | --- | --- |
| Prescribed initialization, raw scaling, and normalization | PASS | G 24–109, 466–483 |
| Fixed-program Gaussian identification with both matrices and both transposes | PASS | L 297–451; G 132–202 |
| Singular-Gram removal and empirical feedback | PASS | L 379–447; G 166–190 |
| Common probability spaces, bounded actions, and actual adjoints | PASS | L 470–547; G 204–219 |
| Fixed-clip existence and width/mesh bridge | PASS | L 617–719; G 221–265 |
| Mesh- and cap-uniform numerical response/tail bound | PASS | R 96–253 |
| Cutoff removal and unrestricted bounded-primal competitor uniqueness | PASS | G 267–362 |
| Gradient structure, physical continuation, and raw restart uniqueness | PASS | G 364–444 |
| Actual raw GD, stopping argument, and prescribed interpolation | PASS | G 446–539 |
| Joint measurements, velocities, kernels, and path laws | PASS | G 541–592 |
| Initial feature learning and nonconstant total kernel | PASS | G 594–710 |
| Strict nonlinearity at every finite time and absence of later freezing | PASS | G 712–816 |

There are no remaining gaps requiring a repair or counterexample for the stated theorem. The explanations that follow supply explicit checks at the points where a false shortcut would have changed this verdict.

## 1. Model, gradient normalization, and activation replacement

G 24–69 preserves the four initial variances and the exact specified raw updates. In particular, the readout entries have standard deviation \(n^{-1}\), so their normalized Euclidean norm is \(O_{\mathbb P}(n^{-1})\), not order one. Setting the population initial readout to zero is therefore consistent with this initialization; G 338–362 and 485–539 separately transfer the actual small finite readout.

The finite raw gradient uses normalized Euclidean inner products for the vector blocks and ordinary Frobenius inner products for the matrix blocks. Indeed,
\[
 \partial_{z^{(1)}}f_n=\delta^{(1)}/n,\quad
 \partial_{W^{(\ell)}}f_n=\delta^{(\ell)}(h^{(\ell-1)})^T/n,\quad
 \partial_{W^{(4)}}f_n=h^{(3)}/n.
\]
Taking gradients in those metrics gives exactly (2). The rank-one population operator \(U\otimes V\) corresponds to \(uv^T/n\); its Hilbert–Schmidt norm is \(\|U\|_2\|V\|_2\). Thus the kernel factors in G (4) and (15) have the correct normalization.

For the new activation,
\[
 \phi'(z)=\frac{1}{10(1+z^2)},\qquad
 \phi''(z)=-\frac{z}{5(1+z^2)^2}.
\]
Consequently the bounds \(5/6<\phi<7/6\), \(0<\phi'\le1/10\), and \(|\phi''|\le1/5\) used in G and R are valid conservative bounds. Also
\[
 F'(z)=10(1+z^2)=1/\phi'(z),\qquad
 (F^{-1})'=\phi'\circ F^{-1},\qquad
 \chi'=(\phi'\circ F^{-1})^2.
\]
The inverse and \(\chi\) have Lipschitz constants \(1/10\) and \(1/100\). The cubic root variable \(F(Z_0^{(1)})\) has finite moments of every order. It is supplied as part of the root tuple, so the proof never needs the false assertion that \(F:\mathbb R\to\mathbb R\) is globally Lipschitz.

The constant offset changes second moments and certain initial response coefficients. G 139–160 and 597–650 account for both changes. No centering or oddness premise survives unexamined into the new argument.

## 2. The generic finite-program identification is valid

### Conditional Gaussian step and the two orientations

At a finite transcript, with old constraints \(WV=Y\) and \(W^TU=Q\), L 301–329 gives
\[
 W=Y(V^TV)^{-1}V^T+
 U(U^TU)^{-1}Q^TP_{V^\perp}
 +P_{U^\perp}\widetilde W P_{V^\perp}
\]
in conditional law, when the input Grams are invertible. This conditional mean satisfies both constraints: the compatibility identity \(U^TY=Q^TV\) supplies the first part of the transpose constraint, and the second term supplies its orthogonal remainder.

For \(h_\perp=h-V(V^TV)^{-1}V^Th\), its unexplored answer is a Gaussian with variance \(\|h_\perp\|_2^2/n\), projected away from the old reverse-input span. The removed standard-Gaussian projection has expected normalized squared norm \(\operatorname{rank}(U)/n\). At fixed program length this vanishes; its bounded variance multiplier does not alter the conclusion.

Adaptive interleaving does not invalidate the conditioning. Conditional on the preceding transcript, a new input is known, and its answer adds a linear observation of only the matrix being queried. Induction therefore preserves independence of the two conditional residual matrices. This is the conditional independence required in L 307 and G 162–165; it is not a claim that trained matrix entries remain independent.

The empirical-law induction also has the moments it needs. After removing the finite-rank projection, the fresh Gaussian coordinates are independent conditional on the transcript. Bounded-test conditional fluctuations vanish, and the conditional second-moment calculation has a vanishing cross-term variance controlled by the previous normalized squared norm. Previous joint \(\mathcal W_2\) convergence supplies convergence of the Gram entries and all finite linear-combination moments. Globally Lipschitz instructions preserve this convergence. No coordinatewise iid assertion about reused answers is needed.

### Why the response is the full source derivative

The cancellation in L 333–377 is substantive and correct. Old transpose answers have the form
\[
 q_s=\zeta_s+\sum_r c_{sr}v_r.
\]
Orthogonality of \(h_\perp\) to all old forward inputs gives
\[
 \mathbb E[q_s h_\perp]=\mathbb E[\zeta_s h_\perp].
\]
The source covariance is \(\Gamma_U=(\mathbb E[u_su_t])\). Gaussian integration by parts, with the other source groups and roots fixed, gives
\[
 \mathbb E[\zeta h_\perp]=
 \Gamma_U\,\mathbb E\nabla_\zeta h_\perp.
\]
The coordinate expressions have bounded source derivatives at each fixed instruction, hence the integration-by-parts expectations are legitimate. Substitution in the projection formula cancels the responses already contained in the old forward answers. This yields
\[
 (Wh)_{\rm lim}=\xi_h+\sum_su_s\,\mathbb E\partial_{\zeta_s}h,
 \qquad
 \mathbb E[\xi_h\xi_v]=\mathbb E[hv].
\]
The covariance is an uncentered second moment. In particular the variance of the first forward query is \(\mathbb E[\phi(G)^2]\), not \(\operatorname{Var}(\phi(G))\).

The new source is a deterministic linear combination of old same-orientation sources plus an independent innovation. This proves the source-group independence asserted in the recursion. It does not resample the reverse action independently: the dependence on the original matrix's other orientation is precisely the response term.

### Singular inputs and feedback

L 379–402 removes singular Grams by adding a new independent Gaussian input of size \(\epsilon\) before each call. Its limiting squared distance from the preceding input span is at least \(\epsilon^2\), because the new noise is independent of that span and of the unperturbed new input. Thus the positive-Gram argument applies for each fixed \(\epsilon>0\).

At fixed program length, globally Lipschitz instructions and bounded initial matrix norms give an \(O(\epsilon)\) normalized-vector comparison of the perturbed and original finite programs. On the scalar side the induction is through deterministic response coefficients, covariance entries, and explicit coordinate functions. Previous coefficients and formal derivatives have finite uniform bounds in this fixed induction. Continuity of positive-semidefinite covariance square roots and dominated convergence pass the expected derivatives to the zero-noise recursion. This is a valid removal argument; it does not require pseudoinverse continuity at a rank change.

It is also legitimate to keep formally distinct source arguments when their covariance is singular. Any difference in derivative coefficients in a null covariance direction has zero contraction against the corresponding response-input tuple. L 394–402 verifies this with the equality of the source covariance and the response-input second-moment matrix.

The oracle argument in L 404–430 and G 176–190 freezes only finitely many empirical contractions, causally at their population values. Fixed clipping bounds the middle backward factor; bounded activations bound the readout at every oracle step. The top product can therefore be extended smoothly with bounded first derivatives without changing the calculation. Cauchy–Schwarz controls contraction differences, and finite induction transfers the oracle limit to actual empirical feedback. This avoids differentiating empirical coefficient selections or covariance factorizations.

The actual call order is forward layer 2, forward layer 3, reverse layer 3, reverse layer 2. Thus forward sums are strictly past-time sums and reverse sums include the present index. In particular,
\[
 b^{(3)}_{kk}=\mathbb E[W^{(4)}_k\phi''(Z^{(3)}_k)],
\]
\[
 b^{(2)}_{kk}=
 \mathbb E[\phi''(Z^{(2)}_k)\tau_R(q^{(2)}_k)]
 +b^{(3)}_{kk}\mathbb E[(\phi'(Z^{(2)}_k))^2\tau_R'(q^{(2)}_k)].
\]
The second term is required and is retained. Past-source derivatives use the complete coordinate expressions as well. These checks discharge R's representation premise for the changed activation.

## 3. Common actions and fixed-clipping flows

L 470–547 constructs the spaces from actual joint finite-program limits, not from independent copies of separately computed marginal laws. A finite union of allowed programs is another allowed finite program. Its deterministic limit supplies consistency, including when a query is repeated or inserted in a different finite list. The countable joint-coordinate construction therefore applies separately in each neuron layer.

The operator-norm estimate is sufficient: a \(1/4\)-net of size at most \(9^n\) on each sphere and the scalar Gaussian tail yield
\[
 \mathbb P(\|W_0^{(\ell)}\|_{\rm op}>10)
 \le2\,9^{2n}e^{-100n/8}\longrightarrow0.
\]
Passing the finite norm inequality to joint second moments proves
\[
 \|W_0^{(\ell)}U\|_2\le10\|U\|_2
\]
for every generated rational combination. Equal \(L^2\) inputs consequently have equal outputs, and linearity passes as well. The span is dense: finite-coordinate measurable functions approximate generated \(L^2\) variables, bounded continuous functions approximate finite-coordinate functions in \(L^2\), and the included smooth Lipschitz family approximates on compact sets with clipping controlling tails.

Both orientations extend continuously. For generated \(U,V\), the finite identity
\[
 \langle v,Wu\rangle_n=\langle W^Tv,u\rangle_n
\]
passes to the limit in the joint laws, and density extends it to all inputs. Thus the reverse extension really is the adjoint. This construction can support arbitrarily many fixed probes while retaining bounded operators; it asserts no operator-norm limit between different-width matrices.

For fixed clipping, G 221–265 has a complete Banach-space construction. The readout integral preserves \(|W^{(4)}(s)|\le as\). Bounded gates, \(|\tau_R(q)|\le|q|\), and successive integration bound the readout and both operator norms by (6), independently of \(R\). The same estimates apply to positive-step Euler prefixes.

The important difference estimate uses the reference readout:
\[
 C_A\phi'(Z_A)-C_B\phi'(Z_B)
 =(C_A-C_B)\phi'(Z_A)
 +C_B[\phi'(Z_A)-\phi'(Z_B)].
\]
Only \(C_B\) needs a pointwise bound. This gives G (7). The middle clipped multiplier costs \(O(R)\), leading to the stated \(C_S(1+R)\) Lipschitz constant. Picard iteration is on a closed set of continuous paths with the preserved readout bound, rather than on an unrestricted \(L^2\) ball. The primal bounds allow finitely many restarts on any fixed feature interval.

The bounded velocity and fixed-\(R\) Lipschitz estimate give a local Euler defect \(O_{R,S}(\Delta^2)\) and a global \(O_{R,S}(\Delta)\) error, uniform at finite width on the appropriate initialization event. Combining this with fixed finite-program identification, with width sent to infinity before the mesh is refined, establishes the fixed-clip width limit. The unbounded initial first-coordinate transform causes no difficulty because the estimates use its differences and its finite initial second moment.

## 4. Numerical response bootstrap and uniform tails

The induction in R is closed at the current row, rather than assuming the row to be proved. Let \(A=S=3/2\), \(a=7/6\), and suppose \(U_r,V_r\le1\) for \(r<k\).

The bottom derivative estimate gives
\[
 |\partial_{\zeta^{(1)}_s}H^{(1)}_j|
 \le\Delta e^{S/100}/100,\qquad
 |a^{(2)}_{js}|<A\Delta.
\]
There is one factor of the source-time mesh here, which is essential.

For the middle layer the derivative inequalities are
\[
 |\partial\delta^{(2)}_r|
 \le |q^{(2)}_r|\,|\partial Z^{(2)}_r|/5
      +|\partial q^{(2)}_r|/10,
\]
\[
 |\partial_{\xi^{(2)}}q^{(2)}_r|
 \le\frac1{10}\sum_{v\le r}|b^{(3)}_{rv}|
                         |\partial_{\xi^{(2)}}Z^{(2)}_v|.
\]
They include \(v=r\). Their source-row sums are bounded by the envelope \(E_j\) in R 120–151. A derivative at an individual backward source has a first forcing at most \(A\Delta/10\), so
\[
 |\partial_{\zeta^{(2)}_s}H^{(2)}_j|
 \le A\Delta E_j/100.
\]

For prior rows, \(|q^{(2)}_r|\le|\zeta^{(2)}_r|+a\) and
\(\operatorname{Var}(\zeta^{(2)}_r)\le(7/40)^2\). Jensen's inequality over time uses only these marginal variances. In particular it does not assume independence between source times. Direct substitution gives exactly
\[
 \mathbb E E_j^p\le
 2\exp\!\left(\frac{219p}{400}
             +\frac{3969p^2}{1280000}\right).
\]
For \(p=1,2\) this gives \(\|E_j\|_1<4\) and \(\|E_j\|_2<3\). Hence
\[
 |a^{(3)}_{js}|
 \le\Delta(49/36+3/50)<A\Delta.
\]

The top response then has
\[
 \sum_{s\le j}|\partial_{\xi^{(3)}_s}\delta^{(3)}_j|
 \le(73/300)S\max_{v\le j}T_v,\qquad
 \max_{v\le j}T_v\le e^{657/800}<5/2.
\]
Adding the learned-rank term yields
\[
 V_k\le73/80+147/3200=3067/3200<1.
\]
This is obtained before bounding the current middle query, so using
\[
 \|q^{(2)}_k\|_2\le7/40+7/6=161/120=:Q
\]
is not circular.

Finally the current middle derivative row is bounded by
\[
 \left(|q^{(2)}_k|/5+V_k/100\right)E_k.
\]
The \(V_k/100\) term contains the current return through \(b^{(3)}_{kk}\). Cauchy–Schwarz and the covariance contribution give
\[
 U_k\le3(Q/5+1/100)+SQ^2/100
 =\frac{2482563}{2880000}<9/10.
\]
All constants and fractions in this closure check. Since all previous-row hypotheses are available in the causal order, simultaneous induction proves the bounds for every mesh index. There is no first-row loophole: zero initial readout makes both initial rows and backward variances zero.

Thus the actual identified scalar query is a Gaussian source plus a shift of absolute value at most \(7/6\), with Gaussian variance at most \((7/40)^2\), uniformly in mesh and cap. These bounds imply a common finite \(K\) with \(\mathbb E e^{q^2/K^2}\le2\). Fixed-clip strong Euler convergence and Fatou pass it to every clipped-flow time. Taking a supremum of these expectations over deterministic times does not require a tail estimate for a Gaussian path supremum.

## 5. Cutoff removal, competitors, and restart

The three-term identity in G 294–299 is exact. Its last term is supported on \(|q_B|>R\), and
\[
 |q_B|\mathbf1_{\{|q_B|>R\}}\le2(|q_B|-R/2)_+.
\]
The gate-difference term uses the clipped reference query, so its multiplier is at most \(2R\). Together with G (7) and the rank-one inequalities, this proves (10), with no dependence on the other cutoff \(R'\), even for \(R'=\infty\).

The exponential moment gives the uniform tail estimate
\[
 \|(|q_R|-R/2)_+\|_2
 \le2K e^{-R^2/(16K^2)}=\varepsilon_R.
\]
Consequently the comparison error is at most a constant times
\[
 e^{C(1+R)S}\varepsilon_R.
\]
The Gaussian decay defeats the entire exponential stability cost, including an additional factor \(1+R\). Completeness gives a uniform state limit; (7) identifies its actual backward query; (10) evaluated at that limit gives uniform convergence of the vector fields. Passing the integral equations therefore constructs a \(C^1\) uncut solution on the whole feature interval \([0,3/2]\).

For an arbitrary competing continuous bounded-primal uncut integral solution, the same estimate uses the constructed clipped solution as reference. The competitor need not satisfy an exponential-tail premise or a pointwise bound on its own readout. Its compact-interval bounds merely change the constant \(C\). Gronwall followed by \(R\to\infty\) forces equality.

At a reached feature time \(\sigma\), the initial discrepancy from the clipped reference is already \(O(e^{C_0R}\varepsilon_R)\). Propagating it on the remaining interval adds another factor \(e^{C_1R}\), which still tends to zero after multiplication by \(\varepsilon_R\). This proves restart uniqueness in the class claimed.

The finite-width tail bridge is also sufficient. The positive-part function is 1-Lipschitz, and its squared norm is a continuous quadratic-growth measurement. Fixed-\(R\) \(\mathcal W_2\) convergence gives convergence at fixed times; (6), (7), and the uniform velocity bound give a common time-Lipschitz constant. A finite time net proves G (13). Therefore the proof needs no unproved finite-width exponential moment.

Applying the asymmetric comparison at the same width gives (14) with the correct \(O_{\mathbb P}(n^{-1})\) readout perturbation. Sending width to infinity at fixed \(R\), and only then removing \(R\), proves the full-sequence feature-flow limit.

## 6. Gradient structure and all finite physical times

G 366–393 and L 1776–1865 justify a scalar Fréchet derivative, without incorrectly asserting Fréchet differentiability of the activation as a map \(L^2\to L^2\). For fixed \(B\in L^2\), truncating \(B\) bounds the scalar Taylor remainder by
\[
 C R\|v\|_2^2+
 C\|B\mathbf1_{\{|B|>R\}}\|_2\|v\|_2=o(\|v\|_2).
\]
Successive backwards expansion applies this estimate with fixed original-state backward factors. Mixed matrix/activation changes are quadratic because the Hilbert–Schmidt norm bounds the operator norm. The resulting four gradient entries are exactly those displayed in G 386–389.

Continuity of the gradient follows by the fixed-factor multiplier argument: bounded continuous gates converging in probability act continuously on any fixed \(L^2\) factor. Trained matrix increments lie in the Hilbert–Schmidt class because their continuous rank-one velocities are integrable in that norm. The cutoff limit has the same increments, since rank-one differences converge in Hilbert–Schmidt norm too.

The chain rule along the constructed \(L^2\) curve gives \(dZ^{(1)}/ds=\phi'(Z^{(1)})q^{(1)}\). Thus
\[
 \theta_s=\nabla f,\qquad f_s=\|\nabla f\|^2=\sum_{\ell=1}^4K^{(\ell)}.
\]
All terms are continuous and bounded on \([0,3/2]\). Since \(H^{(3)}>5/6\),
\[
 f_s\ge25/36,\qquad f(0)=0,\qquad
 f(3/2)\ge25/24>1.
\]
There is exactly one root \(f(s_*)=1\), with \(s_*\le36/25<3/2\).

Writing \(B=\sup_{[0,s_*]}f_s<\infty\), the clock
\[
 s_t=2(1-f(s)),\qquad s(0)=0
\]
is a scalar Lipschitz initial-value problem. Since
\[
 1-f(s)\le B(s_*-s),
\]
its distance to the endpoint satisfies
\[
 s_*-s(t)\ge s_*e^{-2Bt}>0.
\]
It remains in the already constructed feature interval for every finite physical time. This discharges global physical continuation without extending the response bound to arbitrarily large feature time.

The raw competitor argument is legitimate as well. A continuous bounded-primal raw integral solution has continuous \(L^2\) backward fields by bounded-gate truncation and bounded operators. Its matrix velocities are continuous in Hilbert–Schmidt norm, so its increments belong to the same affine gradient space, even if this was not imposed separately. The scalar chain rule therefore gives
\[
 (1-f)_t=-2(1-f)\sum_\ell K^{(\ell)}.
\]
The bounded kernel on a compact physical interval prevents a positive \(1-f\) from vanishing there.

For the unbounded transformation \(F\), first take absolutely continuous scalar coordinate versions of the raw integral solution. The pointwise chain rule cancels \(F'\phi'=1\), yielding
\[
 F(Z^{(1)}(t))=F(Z^{(1)}(t_0))
 +\int_{t_0}^t2(1-f(u))q^{(1)}(u)\,du.
\]
The right-hand side is in \(L^2\), which proves membership in the transformed solution class rather than assuming it for the competitor. Feature-time uniqueness and scalar-clock uniqueness then identify the raw solution before any attempted exit. The preceding nonattainment estimate rules out that exit. The argument applies from initialization and from every reached state.

## 7. Exact raw GD and interpolation

G 448–525 uses a valid stopping argument for each fixed \(T\). The population residual has a positive minimum \(\rho\) on \([0,T+1]\), and the feature clock stays at most \(36/25\). The stopping levels \(1-\rho/2\) and \(S_b=147/100\) leave fixed positive margins.

Before stopping, the computational increments \(\alpha_k=2\eta_n(1-f_{n,k})\) are positive and \(O(\eta_n)\). The readout and matrix primal bounds depend only on their accumulated positive feature time. They do not presuppose an exact transformed first-coordinate Euler step. They bound \(q^{(1)}\) in normalized Euclidean norm and keep the first stopping endpoint below \(3/2\).

The cubic identity G (17) is exact:
\[
 F(z+\alpha\phi'(z)q)-F(z)
 =\alpha q+10\alpha^2z(\phi'(z))^2q^2
       +(10/3)\alpha^3(\phi'(z))^3q^3.
\]
Using \(\|q\|_2\le C\sqrt n\),
\[
 \|q^2\|_2/\sqrt n\le C^2\sqrt n,\qquad
 \|q^3\|_2/\sqrt n\le C^3n.
\]
Since \(\sup_z|z|(\phi'(z))^2<\infty\), the summed normalized error is bounded by
\[
 C_S(\eta_n\sqrt n+\eta_n^2n)
 =O(n^{-3/2}+n^{-3}).
\]
Thus the correction vanishes for the actual prescribed step size. No fourth- or sixth-moment estimate for the finite backward coordinates is silently used.

The discrete comparison recurrence includes this correction, the fixed-clip local Euler defect, and the reference tail. The random computational partition causes no independence problem: the tail norm is uniformly Lipschitz in feature time, so its weighted sum differs from its integral by \(O(\max\alpha_k)\) pathwise. Discrete Gronwall proves (19), including the first stopping node.

The predictor is Lipschitz in the bounded state metric. Therefore (19), fixed-clip identification, and cutoff removal give a uniform stopped predictor error against \(f(s_k)\). Scalar Gronwall for the interpolated computational clock then gives (20) up to that same random endpoint. A premature stop contradicts either the \(3/100\) feature-clock margin or the \(\rho/2\) predictor margin. The comparison therefore holds on the whole requested physical interval with probability tending to one.

Applying the same cubic identity to a fractional raw step controls the transform of the specified raw linear interpolant. The remaining parameter blocks are already linear. This proves the claimed interpolation result, not just convergence at mesh nodes.

Finite physical GF is covered by its feature-flow comparison and scalar clock. Its exact lower bound \(df_n/ds\ge25/36\), together with \(f_n(0)\to0\), places the finite root inside the available feature interval with probability tending to one. Comparing both finite algorithms to the same finite clipped reference and using its uniform velocity bound for clock differences proves the stated same-width GD/GF distance convergence. No cross-width operator-norm convergence is needed.

Every approximation step bounds the full finite sequence at fixed auxiliary parameters. The successive removal of these parameters yields convergence in probability along the full sequence, not merely a selected subsequence.

## 8. Measurements, velocities, and path laws

G 541–579 contains the necessary extra step beyond state convergence. The asymmetric comparison first controls the uncut middle backward field; bounded reverse actions then control \(q^{(1)}\). For a bounded gate multiplying an unbounded \(L^2\) field, clip that field at a fixed level, pass the resulting Lipschitz calculation, and remove the clip.

The required tails are uniform in time. A continuous \(L^2\) curve on a compact interval has a compact image and uniformly integrable squared tails. Uniform \(\mathcal W_2\) convergence of the finite laws transfers this tail control in probability. This argument can be iterated through each specified bounded operator call, using its common operator bound to control the input approximation error.

The exact feature-time preactivation velocities are correctly differentiated in G (21):
\[
 Z^{(1)}_s=\phi'(Z^{(1)})q^{(1)},
\]
\[
 Z^{(2)}_s=\mathbb E[(H^{(1)})^2]\delta^{(2)}
       +W^{(2)}[(\phi'(Z^{(1)}))^2q^{(1)}],
\]
\[
 Z^{(3)}_s=\mathbb E[(H^{(2)})^2]\delta^{(3)}
       +W^{(3)}[\phi'(Z^{(2)})Z^{(2)}_s].
\]
They include movement of both trained matrices and of the preceding hidden features. Their products are precisely covered by the truncation argument. The same reasoning gives joint laws and second moments of all four raw kernel blocks.

For GD, raw derivatives are constant within a parameter step, but differentiated hidden quantities have current gates and current matrices. The discrepancy from the node formula is controlled as follows: clip the node velocity coordinates, use the vanishing same-step state and operator changes on the clipped part, and bound the remaining part by the uniformly integrable squared tails already obtained for the node velocity fields. This also controls the terminal-left convention. It does not assume that the interpolated hidden states themselves follow an exact Euler rule.

Uniform convergence of the squared velocity norms gives convergence of their integrals. Jointly measurable \(L^2\) velocities give coordinatewise absolutely continuous versions by integration and Fubini. For those paths,
\[
 \|z-I_\pi z\|_\infty^2
 \le4|\pi|\int_0^T|\dot z(t)|^2\,dt.
\]
After averaging, this bounds the \(\mathcal W_2\) distance from full paths to their finite-grid interpolants. The finite-grid joint laws converge, the averaged energies remain bounded, and then \(|\pi|\to0\) proves the asserted path-space convergence. The same estimate also provides finite second moments of the supremum norm. Applying the Lipschitz activation gives the feature path laws.

Continuous quadratic-growth tests are legitimate consequences of \(\mathcal W_2\) convergence. Uniformity in time follows from the compact time image and the uniform \(\mathcal W_2\) comparison. No pairing between different neuron populations is introduced.

## 9. Nonlinearity and nonlazy behavior

### Initial movement and the changing kernel

G 597–650 correctly replaces the odd-activation initial calculations. The full forward second moments satisfy
\[
 m_\ell=1+\frac1{100}\mathbb E[
 \arctan(\sqrt{m_{\ell-1}}G)^2]>1.
\]
For the first transpose, the innovation variance is the full
\(\mathbb E[(B^{(3)})^2]\), not that quantity minus a response projection. Conditioning leaves a fresh Gaussian acting on the entire transpose input; the removed projection lies in the output coordinate space and has vanishing normalized norm.

The response coefficient is
\[
 c_3=\frac{\mathbb E[Z^{(3)}_0B^{(3)}]}{m_2}
 =\frac1{100m_2}\mathbb E\frac{Z^{(3)}_0\arctan Z^{(3)}_0}
                                      {1+(Z^{(3)}_0)^2}>0.
\]
The offset term vanishes by initial Gaussian symmetry, rather than by an incorrect pointwise sign assertion. Conditioning additionally on the independent third-layer matrix makes \(B^{(2)}\) a permissible input for the second transpose calculation without exposing the residual of the second-layer matrix. This gives exactly the positive \(c_2\) and positive innovation variance displayed in G.

Adjunction gives
\[
 \mathbb E[B^{(2)}V^{(2)}]=\gamma_1+\gamma_2>0,\qquad
 \mathbb E[B^{(3)}V^{(3)}]=\Gamma>0.
\]
Thus all three \(V^{(\ell)}\) are nonzero. Since \(\phi'\) is strictly positive everywhere, the leading feature-velocity variables are nonzero as well. Strong continuity and bounded-gate truncation justify the successive limits \(W^{(4)}(s)/s\to H^{(3)}_0\) and \(\delta^{(\ell)}(s)/s\to B^{(\ell)}\), then all the state and velocity expansions.

Expanding the top feature squared norm yields the coefficient \(\Gamma\), so
\[
 \sum_{\ell=1}^4K^{(\ell)}(s)=m_3+2\Gamma s^2+o(s^2),
\]
and \(s(t)=2t+o(t)\) gives the \(8\Gamma t^2\) coefficient in G (22). The hidden squared-speed integrals have the positive \(16/3\) coefficients stated there. Both trained matrices also have nonzero leading Hilbert–Schmidt increments. Hence this is neither a frozen-hidden-feature limit nor a constant-kernel limit.

### Strict nonlinearity at later times

The lower-tail argument G 712–768 is stronger than a small-time continuity argument and works on the whole constructed feature interval.

At the top,
\[
 |Z^{(3)}_k-\xi^{(3)}_k|\le AaS^2/10=63/160.
\]
The source variance is at least \(m^2\), so both half-line probabilities have the lower bound (23), regardless of dependence between the source and its bounded correction.

In the middle, the correction is dominated by
\[
 R_{2,k}=\frac{A\Delta}{10}\sum_{j<k}(|\zeta^{(2)}_j|+a),
 \qquad \mathbb E R_{2,k}\le483/1600.
\]
This dominating variable, unlike the correction itself, depends only on the independent backward-source group. Consequently its event \(R_{2,k}\le1\), of probability at least \(1117/1600\), can be intersected independently with the required forward-source event. This proves (24).

At the bottom,
\[
 |X^{(1)}_k-F(Z^{(1)}_0)|\le R_{1,k},\qquad
 \mathbb E R_{1,k}\le1561/800<2.
\]
The dominator is independent of the initial root. The event \(R_{1,k}\le4\) has probability at least \(1/2\). Monotonicity and oddness of \(F\), not of the activation, yield (25).

These are uniform lower bounds for closed upper and lower half-lines. Under weak convergence, a closed-set probability is at least the limsup of the approximating probabilities. Thus the direction of Portmanteau used in G 762–768 is correct, and the lower bounds pass through mesh refinement and cutoff removal at every time.

Every hidden preactivation therefore has finite second moment, positive variance, and unbounded support in both directions at every reached time. The affine least-squares minimum in (26) is attained. If it were zero, boundedness of \(\phi\) and unbounded support of \(Z\) would force its slope to vanish; strict monotonicity of \(\phi\) would then force \(Z\) to be constant. This contradiction proves strict positivity.

The moments in this minimum vary continuously along the \(L^2\) path. The variance never vanishes, so both it and the positive minimum have positive lower bounds on each compact physical interval. Uniform joint \(\mathcal W_2\) convergence transfers the latter lower bound, with a smaller positive margin, to the finite empirical least-squares errors with probability tending to one.

### No later hidden freezing

At every \(s>0\), positivity of the activation gives \(W^{(4)}(s)\ge ms\) pointwise. Hence \(\delta^{(3)}(s)\) is nonzero and has strictly positive second moment. Along sufficiently accurate clipped Euler approximations to this time, the variance of \(\zeta^{(2)}_k\) is bounded below by a positive constant. Since
\[
 |q^{(2)}_k-\zeta^{(2)}_k|\le a,
\]
Gaussian lower tails pass by the same closed-set argument and make the uncut \(q^{(2)}(s)\) unbounded in law. Therefore \(\delta^{(2)}(s)=\phi'(Z^{(2)}(s))q^{(2)}(s)\ne0\).

Repeat using convergence of the middle backward second moment, the variance identity for \(\zeta^{(1)}_k\), and \(|q^{(1)}_k-\zeta^{(1)}_k|\le a\). This proves \(\delta^{(1)}(s)\ne0\). This passage can be taken successively with the mesh sent to zero at fixed cutoff and then the cutoff removed; the already proved backward-field convergence supplies the required eventual positive variance bounds.

Finally,
\[
 \mathbb E[\delta^{(2)}Z^{(2)}_s]=K^{(2)}+K^{(1)}>0,\qquad
 \mathbb E[\delta^{(3)}Z^{(3)}_s]=K^{(3)}+K^{(2)}+K^{(1)}>0.
\]
Together with \(Z^{(1)}_s=\delta^{(1)}\), these identities exclude zero \(L^2\) preactivation velocities. Multiplication by the strictly positive activation derivative excludes zero feature velocities. The physical clock derivative is strictly positive at every finite physical time, so this conclusion transfers to every positive finite physical time.

Zero initial hidden velocities are consistent with the vanishing initial population readout; the positive second-order onset is explicitly proved. The theorem requires a nonconstant kernel and moving hidden features, not monotonicity of every kernel block for all time, and the proof establishes the stated requirement.

## Final disposition

**PASS for the complete exact-hash package and its stated changed-activation theorem.**

Remaining fatal gaps: none found. Remaining conditional mathematical premises: none beyond the model and solution/observable classes explicitly stated in G. No repairs are required for this verdict.

The result remains limited to the fixed shifted activation, each fixed finite physical horizon, the generated common action spaces, and the stated empirical/action-law topology. It is not a proof for unshifted arctangent, an infinite-training-time interchange, or an operator-norm limit across widths. These are boundaries already stated by the candidate, not deficiencies in this theorem.

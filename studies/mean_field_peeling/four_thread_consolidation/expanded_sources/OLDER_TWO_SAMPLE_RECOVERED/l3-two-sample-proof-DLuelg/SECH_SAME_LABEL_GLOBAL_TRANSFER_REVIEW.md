# Independent isolated modular audit: same-label sech transfer

Review date: 2026-09-06.

**Verdict: PASS as a modular same-label theorem, at the candidate hash and dependency versions recorded below. No required mathematical correction was found.** The new activation preserves the proof for both equal-label choices and every fixed admissible input correlation rho in [-1,1). The two new numerical inequalities are valid. The inherited construction, comparison, observation, and nontriviality arguments were checked from their mathematical sources; assertions about earlier audits were not accepted as evidence.

This verdict includes global finite-physical-horizon population existence and reached-state restart uniqueness, full-sequence joint exact raw GD / finite GF / population convergence, all four two-by-two raw kernel blocks, both directions of both hidden operators in the specified probe sense, hidden paths and velocities, positive distributional nonaffinity, and nonzero feature motion in all three hidden layers. It does not certify an opposite-label global theorem, a self-contained presentation in the 119-line candidate alone, an infinite-time/width interchange, or existence from arbitrary population initial states.

## 1. Exact hash and read scope

The audited candidate is:

- `/tmp/l3-two-sample-proof-DLuelg/SECH_SAME_LABEL_GLOBAL_TRANSFER.md`
- SHA256: `f7cfaf82de5ba25a7b8429435366a2919c2c82e15cf132d2525e4b260c602302`
- Read in full, lines 1-119. Its hash matches the requested hash.

The following mathematical dependencies were each read completely, including portions not subsequently relied upon. In the rest of this review, D, B, A, N, P, and E denote these exact versions. Line references use the original files.

| ID | Absolute path | Complete read | SHA256 |
| --- | --- | --- | --- |
| D | `/tmp/l3-two-sample-proof-DLuelg/SECH_GATE_ACTIVATION_DESIGN.md` | 1-231 | `c0f67365fbe36af74db9708ce8a32018b30d8164e77c50b068f71299045e4f24` |
| B | `/tmp/l3-two-sample-proof-DLuelg/TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md` | 1-352 | `9305453f933ad30a0e813e4e97942ee9e00490ce726d70142b25c8f67a475170` |
| A | `/tmp/l3-two-sample-proof-DLuelg/SAME_LABEL_GLOBAL_ASSEMBLY.md` | 1-358 | `510fd019c204e0e89e0c6bcb99c031a11de974b05323df1c016c72b263f64a44` |
| N | `/tmp/l3-two-sample-proof-DLuelg/SAME_LABEL_NONTRIVIALITY.md` | 1-288 | `76124a7552d67304a7e43212b4461ca53c9d79a214af80761f6560012bdf48b6` |
| P | `/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md` | 1-1789 | `bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e` |
| E | `/tmp/l3-two-sample-proof-DLuelg/EXACT_TWO_SAMPLE_REDUCTION.md` | 1-376 | `432f98ff185c797901a81f83c72e4217395d0100f0804b0e609b98db83182e60` |

All five hashes printed in the candidate match. E is an explicitly listed transitive dependency: A:10-25 imports it for the model, raw metric, kernel normalization, and symmetry. E is not directly hash-pinned in the candidate; the precise version audited here is recorded above. P's actual location is explicitly given by B:6-8 and A:18-21.

The mathematical-content read scope consists exactly of these seven files, totaling 3,513 lines. No project history, ledger, separate review, cubic-control file, or jet-bridge file was opened. An exact-basename location search for P inspected file locations, not other file contents. References to previous reviews appearing inside A and the candidate were disregarded. The procedural skill `/etc/codex/skills/solve-math-rigorously/SKILL.md` was read as audit guidance, not as a mathematical dependency.

No experiments, simulations, numerical sampling, external mathematical sources, or outside specialized theorems were used. Numerical checks below are algebraic or series inequalities. The candidate and its dependencies were not edited; all seven source hashes were rechecked after review creation and remained unchanged. This review was created with `apply_patch`.

The operative import scope is D's activation eligibility; E's model, metric, and symmetry identities; B's entire two-sample source bootstrap; A's construction and comparison; N's entire nontriviality proof; and P's elementary limiting tools, finite Gaussian-program proof, common operator construction, and explicitly cited elementary tail calculation. Reading all of P and E does not import their separate arctan-specific conclusions wholesale.

## 2. Exact normalization and both equal-label choices

E:11-91 specifies independent Gaussian initialization, normalized inputs, the rescaled readout, loss

\[
L=(f_1-y_1)^2+(f_2-y_2)^2,
\]

and raw metric

\[
\frac d n\|dW^{(1)}\|_F^2+
\|dW^{(2)}\|_F^2+\|dW^{(3)}\|_F^2+
\frac1n\|dW^{(4)}\|_2^2.
\]

Differentiating the forward equations gives exactly the residual-free deltas and gradients stated there. In particular, the first sample-field update is

\[
\Delta z_b^{(1)}=-2\eta_n\sum_a C_{ba}(f_a-y_a)\delta_a^{(1)},
\qquad \eta_n=n^{-2}.
\]

For common label y, the population label-aligned output is

\[
g=\frac y2(f_1+f_2).
\]

Once deterministic limiting sample symmetry is established, f_a=yg and

\[
\dot\theta=4(1-g)\nabla g.
\]

The factors 1/2 in feature time and 4 in the physical clock are consistent with the unaveraged two-sample loss. No one-input factor 2 is carried into this clock.

The isometry exchanging the equal-norm inputs in E:101-128 works for any shared activation. It does not require activation oddness. The simultaneous transformation (y,W^(4)) -> (-y,-W^(4)) preserves all hidden updates and changes the signs of the readout, predictions, and residual-free deltas. It applies to exact finite GD, finite GF, the zero-readout cut programs, and the population construction. Therefore proving the positive-label case proves the negative-label case as well. For y=-1, positive-delta assertions in N's positive-label convention concern y delta, not the negative raw delta itself.

For -1<rho<1 the first-field metric is the C^(-1) metric derived in E:81-89. At rho=-1, the correct state is the subspace Z_2^(1)=-Z_1^(1), with the one-field raw metric in E:90-91. No inversion of singular C is needed. Constants based on equivalent first-field norms may depend on fixed rho, as allowed.

## 3. Activation eligibility and the complete source bootstrap

### 3.1 Activation properties

For epsilon=1/10,

\[
\phi(z)=1+\epsilon\arctan(\sinh z),\qquad
p(z)=\phi'(z)=\epsilon\operatorname{sech}z,
\]

\[
p'(z)=-\epsilon\operatorname{sech}z\tanh z.
\]

Thus p>0 everywhere, p<=1/10, and |phi''|<=1/10<=1/5. Higher fixed derivatives are bounded: differentiation preserves finite linear combinations of products of bounded sech and tanh factors. The activation minus one is odd and strictly increasing.

D:38-61 supplies an elementary range proof. Namely,

\[
\int_0^\infty\operatorname{sech}v\,dv
=2\int_0^1\frac{dt}{1+t^2}<\frac53,
\]

because (1+t^2)^(-1)<1-t^2/2 for 0<t<1. Consequently

\[
\frac56<\phi<\frac76.
\]

All boundedness, smoothness, and Lipschitz hypotheses used below hold with the old conservative constants m=5/6, a=7/6, epsilon=1/10, and |phi''|<=1/5. D also proves the relative-gate inequality through p'/phi'=-tanh, but the same-label construction does not need that additional inequality.

### 3.2 Gaussian program identification, including singular queries

P:258-475 proves the finite-program result used by B, rather than merely naming a matrix-reuse theorem. Its key ingredients remain valid here:

- Conditional on earlier observations WV=Y and W^T U=Q, the remaining Gaussian matrix is the two-sided orthogonal residual in P:319-321. The deterministic part satisfies both constraints by U^T Y=Q^T V. Sequential conditioning justifies adaptive inputs and preserves independence of the two matrices' conditional residuals.
- A new answer is a linear combination of old coordinates plus a fresh Gaussian vector with a fixed-rank projection removed. The removed part has normalized mean-square size O(1/n). Conditional averaging gives empirical convergence and second moments, not independence of trained neuron coordinates.
- Gaussian integration by parts gives the source-response coefficients. The limiting source covariance is the FULL second-moment matrix of its inputs. Forward and reverse source groups are independent; their respective time/sample slots retain their correlations.
- Fresh input perturbations make every finite same-orientation query Gram invertible. Their removal uses a finite Lipschitz/operator comparison and the causal source recursion with continuous covariance square roots. This handles singular Grams without taking a limit of inverse Grams.
- Source derivatives hold the selected deterministic coefficients and covariance parameters fixed. Zero-variance source slots are not deleted.

B:75-108 verifies the hypotheses for the actual two-sample Euler programs. At fixed caps and fixed number of steps, products involving clipped queries are globally Lipschitz after the stated smooth extensions; the top product can be extended outside the attained readout interval. The new phi and gates satisfy the same hypotheses. The empirical rank-one contractions can be restored by finite induction, since their errors are bounded by products of normalized vector norms and discrepancies.

The additional sample index is a finite root tuple/instruction index. P's proof permits arbitrary within-tuple dependence. Thus (G,-G) at rho=-1 is legitimate. Neither a positive-definite input C nor independence between the two samples is required for identification.

### 3.3 Every induction estimate is preserved

I checked B:110-325 with the new p and p'. No rational-arctan identity occurs in this proof. It uses precisely the derivative bounds above, |C_ab|<=1, two-sample row sums, and the cut bounds |tau_R(q)|<=|q| and |tau_R'|<=1.

The zero-time treatment is correct: W^(4)=0 makes the forward-source derivatives of the actual deltas vanish, whereas a reverse-source derivative such as partial delta^(2)/partial zeta^(2) remains positive at its zero source value. The proof keeps this formal derivative.

The order of construction at time k is A^(2), Z^(2), A^(3), Z^(3), delta^(3), B^(3), q^(2), delta^(2), B^(2). Current U_k is not used to prove itself. In particular:

1. The bottom single-source injection into H^(1) is at most Delta/200. Its envelope is

   \[
   E_j^{(1)}=\exp\left\{\Delta\sum_{r<j}
   \left[\frac{\max_a|q_{ra}^{(1)}|}{5}+\frac{U_r}{100}\right]\right\}.
   \]

   For two possibly correlated Gaussian coordinates, the bound on exp(lambda max |G_a|) costs a factor 4. Jensen over time requires no independence in time. With Q_0=161/120, its expected value is bounded by

   \[
   4\exp\left\{\frac{73}{200}+
   \frac9{200}\left(\frac{161}{1200}\right)^2\right\}
   <4e^{2/5}<6.
   \]

   Therefore |A^(2)|<(Delta/2)(49/36+3/50)<(3/2)Delta/2.

2. The middle total forward-source row has exactly one direct unit derivative per output row. The sum over the two update samples cancels the update's 1/2; it does not introduce a second extra factor 2. The resulting envelope obeys

   \[
   \mathbb E(E_j^{(2)})^p\le
   4\exp\left(\frac{219p}{400}+\frac{3969p^2}{1280000}\right).
   \]

   Its first moment is less than 8 and its L2 norm less than 7/2. The latter uses

   \[
   \frac{219}{400}+\frac{7938}{1280000}<\frac59,
   \quad e<\frac{68}{25},
   \quad (68/25)^5<(7/4)^9.
   \]

   The elementary exponential-series bound is sufficient: the series through degree five is 163/60, and its remaining tail is at most 7/4320, giving e<=11743/4320<68/25. Hence

   \[
   |A^{(3)}|<(\Delta/2)(49/36+3/25)
   =(\Delta/2)(1333/900)<(3/2)\Delta/2.
   \]

3. The top total delta-derivative row is bounded by (73/300)S times the maximum top source row. Its envelope is at most exp(657/800)<5/2. Adding the learned covariance row gives

   \[
   V_k\le V_*:=\frac{3067}{3200}<1.
   \]

4. The current middle reverse query then satisfies

   \[
   \|q_{ka}^{(2)}\|_2\le\frac{aS}{10}+aV_*
   =Q_*:=\frac{24829}{19200}.
   \]

   The current return through matrix 3 is included when differentiating delta^(2). Cauchy--Schwarz and the learned covariance term give

   \[
   U_k\le\frac72\left(\frac{Q_*}{5}+\frac{V_*}{100}\right)
   +\frac3{200}Q_*^2
   =\frac{71063018523}{73728000000}<\frac{97}{100}<1.
   \]

This verifies the small numerical margin in the bootstrap as well as its causal structure.

Finally both ACTUAL reverse queries have q=zeta+beta, |beta|<=a, with Gaussian source standard deviations at most 7/40. The shift need not be independent of its source. The deterministic inequality (zeta+beta)^2<=2zeta^2+2beta^2 gives

\[
\mathbb E e^{q^2/16}
\le e^{49/288}(1-49/6400)^{-1/2}<2.
\]

This is a timewise bound uniform in both caps, mesh, labels, and C on S=3/2. It is not a bound on a time supremum of a Gaussian process. Both problematic multipliers are covered.

## 4. Common spaces, cuts, autonomous flow, and restart

### 4.1 Common initial operators and fixed-cap flows

The part of P:621-680 imported by A:32-43 is activation-independent. Consistent finite same-layer program laws define countable probability spaces. Closure under a countable dense family of bounded smooth coordinate functions makes the generated linear span dense in L2. Passing the finite bound ||W_0||_op<=10 to rational linear combinations defines a well-defined bounded initial action; zero L2 input gives zero output. Passing finite transpose pairings and extending by density identifies the actual adjoint.

The finite operator bound itself is proved by the Gaussian bilinear-form/net calculation in P:180-192. Its use requires no arctan input law. The bottom root is replaced by the RAW Gaussian pair, as A expressly specifies; the old cubic root is not retained. The evolving state records each current operator including all its rank-one increments. Responses and Gaussian sources are devices for constructing its law, not additional dynamical variables or a forcing history.

A:81-117 gives cap- and width-independent primal bounds in the correct order: readout, matrix 3, matrix 2, first fields. The estimates use bounded features, gates, and |tau_R(q)|<=|q|. From zero readout, |W^(4)(s)|<=as pointwise.

For fixed cap, the asymmetric top expansion

\[
\delta_A^{(3)}-\delta_B^{(3)}
=(W_A^{(4)}-W_B^{(4)})p(Z_A^{(3)})
+W_B^{(4)}[p(Z_A^{(3)})-p(Z_B^{(3)})]
\]

needs a pointwise bound only on the reference readout. This supplies the local Lipschitz comparison on the closed path constraint used in Picard iteration. That constraint is preserved by the readout integral. Thus the fixed-cut existence proof does not silently assert local Lipschitzness of the uncut field on arbitrary L2 balls.

The fixed-cap Euler error is O(Delta), uniformly in width on the initial norm event. Fixed finite-program limits followed by mesh refinement yield the fixed-cap flow limit. Finite time nets yield uniformity on the fixed feature interval.

### 4.2 The comparison remains linear in the cap

For a state A at cap R'>=R, possibly uncut, and reference B at cap R, the middle product difference can be split exactly as

\[
\begin{aligned}
p_A\tau_{R'}(q_A)-p_B\tau_R(q_B)
={}&p_A[\tau_{R'}(q_A)-\tau_{R'}(q_B)]\\
&+(p_A-p_B)\tau_R(q_B)
+p_A[\tau_{R'}(q_B)-\tau_R(q_B)].
\end{aligned}
\]

The first term costs the query discrepancy; the second costs R times the forward discrepancy; the third costs at most a constant times b_R(q_B)=(|q_B|-R/2)_+. After reverse multiplication, apply the same split at the bottom. There the existing q^(1) discrepancy is multiplied by bounded p_A, not by another R. Only the separate bottom gate discrepancy costs R. Consequently

\[
\|V_{R'}(A)-V_R(B)\|
\le C(1+R)d(A,B)+Ce_R(B),
\]

where e_R is the sum of the two samples' tails at both reverse layers. The constant is independent of the larger cap and there is no tail premise on A. This checks the crucial absence of an R^2 coefficient.

Fixed-cap mesh limits and Fatou transfer the exponential-square bound to every reference flow time. The elementary tail argument in P:1020-1030 gives

\[
\|b_R(q)\|_2\le8e^{-R^2/256},\qquad
e_R(\theta_R(s))\le32e^{-R^2/256}=:\epsilon_R.
\]

Gronwall therefore yields

\[
\sup_{s\le S}d(\theta_{R'}(s),\theta_R(s))
\le CS e^{C(1+R)S}\epsilon_R.
\]

The complete state space gives a uniform limit. The same product comparisons, including the extra factor 1+R, identify its actual uncut deltas, queries, and velocities strongly. Their integral equations give a C1 uncut feature flow on the whole [0,3/2]. Rank-one differences satisfy the same bound in Hilbert--Schmidt norm, so trained increments also lie in the claimed affine raw Hilbert space.

An uncut competitor with bounded primal norms compares to the same reference. Its possibly larger comparison constant still gives e^(CR)epsilon_R -> 0. At a reached feature time, the initial error against the original cut reference already has this same decay, and a further Gronwall factor does not change the conclusion. This proves reached-state uniqueness on the remaining constructed feature interval without assuming competitor tails or a new Gaussian initialization.

## 5. Gradient differentiability and the global physical clock

A:196-235 contains the needed separate gradient and clock arguments. The scalar differentiability estimate for fixed B in L2 is

\[
|\mathbb E B[\phi(Z+v)-\phi(Z)-p(Z)v]|
\le CR\|v\|_2^2+C\|B1_{|B|>R}\|_2\|v\|_2.
\]

It follows by a quadratic Taylor bound on the truncated factor and a linear remainder bound on its tail. Fixing R before sending v to zero, then removing R, proves the scalar remainder is o(||v||_2). Applying this successively from the top down, with old backward factors, proves scalar predictor differentiability. Terms with two parameter changes are quadratic. Adjunction identifies the metric gradient; bounded-gate truncation proves its continuity. This does not assume Frechet differentiability of a nonlinear Nemytskii map L2 -> L2.

The deterministic limiting laws of the exchange-equivariant cut programs give f_1=f_2 and equal sample feature second moments for common labels. These identities survive cut removal. The symmetry argument uses deterministic limits of the full relevant laws; symmetry in distribution of a finite random output is not mistaken for finite pathwise equality.

The uncut feature flow is grad g. Its readout block gives

\[
g'=\|\nabla g\|^2
\ge \mathbb E\left[\left(\frac{H_1^{(3)}+H_2^{(3)}}2\right)^2\right]
\ge m^2=25/36.
\]

Since g(0)=0 and g' is continuous and bounded on [0,S], there is a unique

\[
0<s_*\le36/25<3/2,\qquad g(s_*)=1.
\]

For s<s_*, define

\[
t(s)=\int_0^s\frac{du}{4(1-g(u))}.
\]

If B_* bounds g', then 1-g(s)<=B_*(s_*-s), so this integral diverges as s increases to s_*. Its inverse exists for every finite t and satisfies s'(t)=4(1-g(s(t)))>0. Thus all finite physical horizons stay inside the one constructed feature interval. This justifies the global physical conclusion without long-feature-time continuation.

Physical uniqueness is proved separately against theta_R(s(t)). A competitor need not be symmetric. The difference between that reference's derivative and its own physical cut-loss field is controlled by its two prediction errors relative to the uncut symmetric solution. Those errors are O(e^(CR)epsilon_R). Bounded-state prediction Lipschitzness and the same two-tail comparison give a physical Gronwall estimate. At a reached physical time the initial reference discrepancy has the same decaying form. Removing R proves unique physical restart for every finite remaining horizon. No scalar clock is assigned to a nonsymmetric competitor.

For negative equal labels, yW^(4)>=ms and g=y(f_1+f_2)/2 give precisely the same argument and clock. The hidden trajectories are preserved by the sign transformation described in Section 2 of this review.

## 6. Exact finite GF/GD, including the off-mode residual

A:237-305 compares both actual finite dynamics to the same finite zero-readout cut feature flow evaluated at the deterministic population clock:

\[
B_{n,R}(t)=\theta_{n,R}(s(t)).
\]

At fixed R, the two prediction errors relative to the uncut population reference are uniformly o_P(1)+O(e^(CR)epsilon_R). The finite reference tail measurements are empirical averages of the continuous quadratic-growth function b_R^2; fixed-cap W2 convergence and the reference query time modulus give e_(n,R)<=epsilon_R+o_P(1) uniformly. No finite-width exponential-moment estimate is assumed.

For each sample the residual discrepancy splits into

\[
f_{n,a}^{\rm actual}-f_a
=(f_{n,a}^{\rm actual}-f_{n,R,a})+(f_{n,R,a}-f_a).
\]

The first term is controlled by same-width state distance and the second by the reference limit. This controls the off-mode component as well as the label mode. It is the necessary comparison for finite random data; an exact finite scalar clock is neither true nor used.

The actual small Gaussian initial readout contributes O_P(n^(-1)) in normalized vector norm. The hidden initial blocks are coupled identically. The pointwise bound is required only on the zero-readout reference, so no uniform coordinate bound on the actual Gaussian readout is smuggled into the argument.

Raw GD is exact Euler for the physical vector field in the raw state. The reference's local defect is O(C_(R,T) eta_n^2): its fixed-cut field is Lipschitz, s' is bounded, and s''=-4g'(s)s' is continuous and bounded. Discrete Gronwall yields the stated type of stopped estimate

\[
\sup_k d_k\le e^{C_T(1+R)T}
\left[O_P(n^{-1})+C_{R,T}\eta_n+C_T\epsilon_R
+C_Te^{CR}\epsilon_R+o_P(1)\right].
\]

All o_P(1) terms here are at fixed R. First taking n to infinity and then R to infinity makes the bound vanish. This iterated tolerance argument proves convergence of the full width sequence, not only a diagonal subsequence.

The primal stop is legitimate through its first bad endpoint. Before that step, bounded features/gates and bounded operator/readout norms bound residuals and all raw velocities independently of width. The step into the bad node overshoots by at most C eta_n. Taking the reference bound plus one as the stop threshold makes a discrepancy below one half incompatible with a first exit. GF has the continuous analogue. At fixed width its smooth gradient field exists globally: the loss-energy identity bounds the squared velocity integral, hence the length on a finite time interval, excluding finite-time escape in the finite-dimensional raw metric.

For the prescribed interpolation, normalized vector changes and operator changes inside a step are O(eta_n). Differentiating the recomputed forward equations gives the same order for preactivation changes in normalized L2, hence O(eta_n sqrt(n)) in coordinate supremum. Lipschitz gates and the layer-by-layer product rule then bound the recomputed velocity discrepancy from the node formula by

\[
O(\eta_n\sqrt n)=O(n^{-3/2}).
\]

This covers interior right derivatives and terminal left derivatives. At a terminal mesh node the preceding node is within eta_n; uniform convergence to the continuous population velocity covers that convention as well. No transformed-GD defect calculation or higher empirical moment is needed.

## 7. Full observable and path transfer

The exact kernel blocks verified from E:59-69 have population entries

\[
K^{(1)}_{ab}=C_{ab}\mathbb E[\delta_a^{(1)}\delta_b^{(1)}],
\]

\[
K^{(\ell)}_{ab}
=\mathbb E[\delta_a^{(\ell)}\delta_b^{(\ell)}]
\mathbb E[H_a^{(\ell-1)}H_b^{(\ell-1)}],\quad\ell=2,3,
\]

\[
K^{(4)}_{ab}=\mathbb E[H_a^{(3)}H_b^{(3)}].
\]

There is no missing sample, width, or metric factor. A:307-347 transfers all entries, not only their same-label quadratic form.

Finite Lipschitz probe programs and either direction of either operator are controlled by the state comparison and bounded operator norms. Both uncut backward queries and deltas have the additional two-tail comparisons. For subsequent bounded gates times L2 factors, truncating the factor, passing the bounded product, and then removing the uniformly integrable squared tail proves strong/product convergence. The compact image of a continuous L2 path supplies uniform tail control in time. Applying this through each fixed probe program proves same-layer joint W2 laws with both samples and any finite time list, uniformly over those time arguments.

For clarity, the feature-time hidden preactivation velocities are exactly

\[
(Z_b^{(1)})'=\frac12\sum_a C_{ba}y_a\delta_a^{(1)},
\]

\[
(Z_b^{(2)})'=\frac12\sum_a y_a\delta_a^{(2)}
\mathbb E[H_a^{(1)}H_b^{(1)}]
+W^{(2)}[p(Z_b^{(1)})(Z_b^{(1)})'],
\]

\[
(Z_b^{(3)})'=\frac12\sum_a y_a\delta_a^{(3)}
\mathbb E[H_a^{(2)}H_b^{(2)}]
+W^{(3)}[p(Z_b^{(2)})(Z_b^{(2)})'].
\]

Feature velocities multiply these by the gate at their own layer; physical velocities multiply by s'(t). These are finite programs of the already controlled types. Their joint laws, squared norms, and integrated squared norms therefore transfer. The raw GD interpolation argument in Section 6 supplies the same statement between nodes.

The whole-path argument uses the deterministic inequality

\[
\|z-I_\pi z\|_\infty^2
\le4|\pi|\int_0^T|\dot z|^2dt.
\]

Expectation or empirical averaging bounds the cost of replacing paths by a fixed grid interpolant. Fixed-grid joint W2 convergence, followed by mesh removal, proves W2 convergence on C([0,T]); summing the two component bounds proves the two-sample path version. Lipschitz phi transfers preactivation paths to feature paths.

These are laws and operator-action probes across widths. The proof does not claim operator-norm convergence between different neuron spaces or create a cross-layer pairing of neuron coordinates. Same-width GD/GF state-distance convergence follows by comparison to their common finite reference. Any raw increment norms obtained from rank-one integrals can also be expressed through the corresponding two-time contractions; no additional arctan identity is involved.

## 8. Forward separation and strict distributional nonaffinity

### 8.1 The first new inequality is correct

On Z_1>=1, Z_2<=-1, strict monotonicity and oddness of phi-1 give

\[
\phi(Z_1)-\phi(Z_2)
\ge2\epsilon\arctan(\sinh1)
>2\epsilon\arctan1=\epsilon\pi/2.
\]

The strict inequality follows from sinh1=1+1/3!+1/5!+...>1. Thus the old separation threshold epsilon pi/2 remains valid, with room to spare. No approximate evaluation is needed.

### 8.2 The source events and Grams still follow

N:24-39 bounds the first raw displacement by a variable R_1 depending only on the reverse source group, independent of the Gaussian root pair, with

\[
\mathbb E R_1\le\epsilon S(Q_*/10+a)<1/5.
\]

The event R_1<=1 has probability at least 4/5. For every rho<1, P(G_1>=2,G_2<=-2)>0, including rho=-1 where this becomes P(G>=2)>0. Their intersection gives the same strictly positive separation probability and hence the same lower bound d_1(rho) for the squared feature difference.

Exchange symmetry gives equal feature diagonal second moments. The two eigenvalues of the feature SECOND-MOMENT matrix are one half the expected squared sum and difference. They are bounded below by 2m^2 and d_1/2. This is the appropriate uncentered Gram; replacing it by a centered covariance would lose the constant feature direction at rho=-1.

For layer 2, N:58-80 has an independent reverse-source dominator with mean at most

\[
A\epsilon S(7/40+a)=483/1600<1/3.
\]

The forward source pair has covariance eigenvalues between a fixed positive c_1(rho) and 2a^2. Its Gaussian density on [2,3] x [-3,-2] is bounded below by

\[
\frac1{4\pi a^2}\exp(-\|x\|^2/(2c_1)).
\]

Intersecting with R_2<=1 gives the same separation and a positive second-layer feature Gram. At the top, the correction is deterministically bounded by

\[
B_0=Aa\epsilon S^2=63/160<2/5.
\]

The same rectangle therefore gives separation without requiring independence of the actual correction from its forward source.

These are uniform statements about the actual cut Euler laws. The closed-event direction of the weak-limit inequality used in N:93-98 is correct: the limiting closed-set probability is at least the limsup of the approximating probabilities. Strong/second-moment convergence also passes the feature Gram lower bounds. No simultaneous realization of source paths at all meshes is needed.

### 8.3 Both unbounded tails rule out affine collapse

The root/dominator events, independent middle dominator, and bounded top correction give both unbounded marginal preactivation tails at every constructed time. The marginal Gaussian variances used in layers 2 and 3 are at least m^2. These facts transfer through the same closed-event argument.

For any resulting scalar Z,

\[
\inf_{\alpha,\beta}\mathbb E[\phi(Z)-\alpha Z-\beta]^2
=\operatorname{Var}(\phi(Z))-
\frac{\operatorname{Cov}(Z,\phi(Z))^2}{\operatorname{Var}(Z)}>0.
\]

The variance of Z is positive. If the attained least-squares error were zero, bounded phi and unbounded support of Z would force alpha=0, and strict monotonicity would force Z constant, a contradiction. The formula's moments are continuous along the L2 trajectory. Its strictly positive values and the positive variance thus have positive minima on a compact time interval. Uniform moment convergence transfers smaller bounds to the finite empirical affine errors. The argument is valid for every layer and both samples and does not merely establish Gaussian nonaffinity at initialization.

## 9. Backward Grams, every-positive-time motion, and rho=-1

### 9.1 The second new inequality is correct

Work in N's convention y=+1, so W^(4)(s)>=ms. Fix s_0>0. On the top source rectangle [4,5] x [-1/10,1/10], the bound B_0<2/5 gives

\[
|Z_1^{(3)}|\ge18/5,\qquad |Z_2^{(3)}|\le1/2.
\]

For the new gates,

\[
\frac{\delta_1^{(3)}}{\delta_2^{(3)}}
=\frac{\cosh Z_2^{(3)}}{\cosh Z_1^{(3)}}.
\]

The common positive readout cancels. For cosh(1/2), the first nonconstant series term is 1/8, and each subsequent term has ratio at most 1/48 to its predecessor. Therefore

\[
\cosh(1/2)\le1+\frac{1/8}{1-1/48}
=1+6/47<5/4.
\]

Also

\[
\cosh(18/5)\ge1+\frac{(18/5)^2}{2}=187/25>5.
\]

Evenness and monotonicity of cosh give, in particular,

\[
\frac{\delta_1^{(3)}}{\delta_2^{(3)}}
<\frac{125}{748}<\frac14,
\qquad
\delta_2^{(3)}>\frac45ms_0\epsilon=:b_0>0.
\]

These are the same conservative inequalities used in N:137-149. The swapped rectangle gives the other direction. The rectangle probabilities retain a positive lower bound p(rho), since the preceding feature Gram remains uniformly positive definite.

For every unit v, choose the rectangle where the delta multiplying its larger-magnitude coefficient is the larger delta. The reverse triangle inequality gives |v dot delta|>=3b_0/(4 sqrt(2)). Hence the top delta second-moment matrix has smallest eigenvalue at least 9p(rho)b_0^2/32>0. This remains true after both limits by convergence of second moments.

For y=-1, apply this calculation to the label-aligned deltas y delta. Their Gram is identical to the raw-delta Gram, their ratio is the same, and the sign transformation preserves the hidden states. The assertion needed for motion is therefore proved for both label choices.

### 9.2 The lower backward arguments need no extra gate formula

At fixed positive time, the middle reverse Gaussian source covariance tends to the strictly positive-definite top-delta second-moment matrix. Its response shift is bounded by a. Each of the four signed source rectangles beyond a+1 therefore gives positive probability of the corresponding nonzero query quadrant, regardless of dependence of the actual shift on the source.

Multiplication by p(Z)>0 preserves those signs. No nonzero deterministic linear combination of the two middle deltas can vanish almost surely: choose a quadrant aligned with its nonzero coefficients. This proves positive definiteness of the middle-delta second-moment matrix. The same sequential argument for the bottom source then proves positive definiteness of the bottom-delta matrix. It requires neither a gate bounded away from zero globally nor a sign premise on actual backpropagation controls.

### 9.3 Raw and feature motion cannot cancel

Let K_g^(ell) be the squared norm of the ell-th raw block of grad g. For positive labels,

\[
K_g^{(1)}=\frac14\sum_{a,b}C_{ab}\mathbb E[\delta_a^{(1)}\delta_b^{(1)}],
\]

and for ell=2,3 it is one quarter the trace product of the delta and preceding feature Grams. If D is positive definite and F is positive semidefinite with positive trace, tr(DF)>=lambda_min(D)tr(F)>0. The first case uses F=C, whose trace is 2 even when rho=-1. Thus every hidden raw block has strictly positive velocity norm at s>0; input degeneracy at rho=-1 does not defeat the argument.

Adjunction and differentiated forward equations give N's exact pairing

\[
\frac12\sum_a\mathbb E[\delta_a^{(j)}(Z_a^{(j)})']
=\sum_{\ell\le j}K_g^{(\ell)}>0.
\]

The trained matrix term contributes its own block norm and the propagated term gives the preceding-layer pairing. Thus at least one sample's preactivation velocity is nonzero at each layer. Exchange symmetry of the joint laws, including derivative probes, makes the two norms equal, so both are nonzero. Since p>0 almost surely, both feature velocities are nonzero too. Finally s'(t)>0 at every finite physical time transfers this to every t>0. The claim concerns nonzero L2 velocities, not pointwise motion of every neuron.

## 10. Initial nonlazy scale and the changing kernel

Actual hidden velocities vanish at initialization because W^(4)_0=0. Positive-time backward Grams alone would not justify nonzero leading Taylor coefficients. N:217-281 supplies the needed separate argument, and it transfers.

Set V(alpha)=(H_1^(3)+H_2^(3))/2 in the positive-label convention, let D_0 be the bounded linearized forward map on raw hidden variations, and B=D_0^*V_0. The top pair needed for this coefficient is V_0 p(Z_(a,0)^(3)), not the zero initial actual delta pair. The top forward pair is nondegenerate Gaussian, V_0>=m, and the two gate-ratio rectangles just checked make this coefficient pair's second-moment matrix positive definite.

The initial reverse argument also survives a direct multi-query conditioning check. If H collects the two forward input columns, Z=W_0H, and U collects the two backward coefficient columns, then

\[
W_0^T U=H(H^T H)^{-1}Z^T U+P_{H^\perp}\widetilde W^T U
\]

in conditional law when U is determined without observing the residual. Before the finite-rank projection, the reverse Gaussian rows have covariance U^T U/n. Its limit is the FULL backward second-moment matrix, not a response-subtracted covariance. The first term converges to a bounded linear combination of the two bounded input features; its coefficients are finite because their feature Gram is positive definite. The rank-two projection vanishes in normalized mean square. Conditional averaging supplies joint empirical laws.

For matrix 3, U depends only on its two forward answers, so the residual condition holds. For matrix 2, condition additionally on the entire independent initial matrix 3; its backward input is then determined without observing matrix 2's remaining residual. The unbounded gated reverse input is covered by clipping, its already established Gaussian-plus-bounded law, and the bounded initial operator. Positive gates and the four-quadrant argument give positive-definite middle and bottom coefficient Grams. No positivity of an arctan-specific response mean is needed.

The trace-product argument consequently gives a nonzero component B_ell in each hidden raw block. Put Gamma_ell=||B_ell||^2>0 and Gamma=sum Gamma_ell. Strong continuity of bounded-gate products and operators on the displayed directions gives

\[
W^{(4)}(s)/s\to V_0,\qquad
\alpha'(s)/s\to B,\qquad
\alpha(s)-\alpha(0)=\tfrac12s^2B+o(s^2).
\]

Only directional strong continuity of the bounded linearized maps and their adjoints is needed here; operator-norm differentiability of the nonlinear feature map on all of L2 is not asserted. Along this curve,

\[
V'(s)=sD_0B+o(s),\qquad
\mathbb E[V_0D_0B]=\|B\|^2=\Gamma.
\]

Thus the inherited coefficients are correct:

\[
K_g^{(4)}(s)=\mathbb E[V_0^2]+\Gamma s^2+o(s^2),
\]

\[
\sum_{\ell=1}^3K_g^{(\ell)}(s)=\Gamma s^2+o(s^2),\qquad
\sum_{\ell=1}^4K_g^{(\ell)}(s)=\mathbb E[V_0^2]+2\Gamma s^2+o(s^2).
\]

Each sample/layer leading preactivation velocity T_a^(ell) is nonzero by the initial version of the pairing in Section 9.3 and sample symmetry. The positive gate makes p(Z_(a,0)^(ell))T_a^(ell) nonzero in L2. Since s(t)=4t+o(t),

\[
H_a^{(\ell)}(t)-H_{a,0}^{(\ell)}
=8t^2p(Z_{a,0}^{(\ell)})T_a^{(\ell)}+o(t^2).
\]

The readout-mode kernel change is 16Gamma t^2+o(t^2) and the total-mode change is 32Gamma t^2+o(t^2). A nonconstant fixed quadratic form forces the total two-by-two kernel matrix to be nonconstant. These positive coefficients are configuration-dependent and fixed with respect to width. Their numerical values need not equal the arctan coefficients; the transfer claims preservation of nonvanishing and of the displayed forms.

Joint field/kernel convergence transfers these nonzero changes at sufficiently small fixed positive times to the finite model. The all-positive-time nonfreezing result is supplied separately by Section 9, so the initial expansion is not being overstretched to later times. For negative common labels, the hidden path and these kernel conclusions are unchanged under the exact sign transformation.

## 11. Check for unimported arctan-specific steps

The following distinctions are essential to the passing verdict:

| Potential activation-specific dependency | What is actually used here |
| --- | --- |
| P's cubic F(z)=10(z+z^3/3), inverse-coordinate Lipschitz estimates, and transformed bottom dynamics | A explicitly uses raw Gaussian sample fields and B's raw two-cut induction. None of these F formulas is imported. |
| P's arctan cubic raw-GD defect calculation and its one-input finite scalar clock | A uses direct raw physical Euler comparison, controls both residual components, and uses the population two-sample clock. |
| P's one-input response calculation | B supplies the two-sample calculation, including both backward clips, factor 4 in Gaussian maximum bounds, both sample sums, and the current cross-matrix return. |
| P's arctan-specific initial positive response-mean integrals | N uses positive-definite pairs, full reverse-source covariance, and quadrant events. A sign of the response mean is unnecessary. |
| E's arctan-specific initial contrast constant based on 1/(1+M^2) | The imported model/symmetry identities are general. N establishes the needed same-label nontriviality directly. That opposite-mode quantitative constant is not claimed unchanged. |
| D's fixed-sign prescribed-control tangent theorem | Only activation eligibility is needed for this transfer. Its fixed-sign hypothesis and restriction -1<rho<1 are not invoked for actual feedback dynamics or at rho=-1. |

After excluding these unimported arguments, the two replacements identified in candidate:69-103 are exactly the formula-dependent numerical steps in N. Smoothness, boundedness, strict monotonicity, and positive gates cover its remaining activation uses. I found no concealed use of the old inverse coordinate, rational gate decay, or a special arctan identity in the operative same-label chain.

## 12. Required versus optional findings

### Required findings

**None.** At the versions in Section 1, I found no failed inequality, missing hypothesis, circular construction, false finite scalar-clock assertion, unverified heavy-theorem invocation, omitted equal-label sign case, or unresolved rho=-1 endpoint in the modular theorem being asserted.

This is a substantive proof verdict from the supplied mathematical dependencies. It is not a reassignment of any earlier review's verdict or hash.

### Optional findings

1. **Directly pin the exact reduction dependency.** Candidate:22-34 omits E from its direct hash list, although A:12-14 explicitly imports it. The dependency chain is resolvable and was fully audited, so this is not a mathematical gap. For a reproducible future bundle, directly list E with the hash recorded in Section 1.

2. **Make the positive-label convention explicit beside the gate lower bound.** Candidate:82-103 follows N:9-10's y=+1 convention; for common label -1, raw delta_2^(3) is negative. The existing sign-reversal argument correctly proves the theorem, so no change to the proof is required. Writing the positive lower bound for y delta_2^(3), or adding “in the positive-label convention of N,” would prevent an isolated reading of candidate:96 from suggesting a false sign claim.

3. **Clarify algebraic versus trajectory dependence on the bottom cap.** A:154 says the definition of q^(2) does not depend on the bottom cap. This is correct as a formula evaluated at a fixed state: it does not apply the bottom clipping function. The evolving state, and therefore the value of q^(2) along a flow, generally depends on both caps. B's estimates are uniform in both caps and A evaluates actual cut states, so the proof does not use an incorrect independence claim. A short wording clarification would improve precision.

No candidate or dependency edit was made. The opposite-label global continuation problem remains outside this review's claim. The same-label modular transfer passes for both equal-label choices and every fixed rho in [-1,1), with unchanged conservative clock/bootstrap constants and the full stated convergence and nontriviality scope.

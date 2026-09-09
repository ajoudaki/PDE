# Isolated full-note mathematical audit — round 2

## Scope, provenance, and verdict

The sole mathematical source for this review was
`/tmp/l2-two-sample-proof-0ywjpp/COMPACT_GATE_RAW_GD_AND_GAUSSIAN_PATHS.md`, read in full, lines 1–347. Line references below refer to that exact source. The supplied digest is a SHA-256 digest.

- Requested SHA-256: `4801b9a5608a1332c9f2f278836f680568fdd5117dbf938630cd4d61a6311b1d`.
- Before-read SHA-256: `4801b9a5608a1332c9f2f278836f680568fdd5117dbf938630cd4d61a6311b1d` — exact match.
- After-review SHA-256: `4801b9a5608a1332c9f2f278836f680568fdd5117dbf938630cd4d61a6311b1d` — exact match, checked after the full audit was written.
- Source extent: 347 lines, 16,421 bytes.

No other mathematical files, conversation history, prior reviews, dependencies, agents, or experiments were used. No source edits were made. Only the procedural review skill and its severity rubric were additionally read. The evidence, claim checks, and findings are consolidated into this one requested report; no auxiliary review artifacts were created. No external-model compatibility, provenance, priority, or novelty claim is evaluated.

**Scoped verdict: PASS.** I found no required mathematical correction to the stated finite-width GD/GF estimates, exact freezing and nonentry results, first-layer confinement, probability and exponential-moment bounds, finite-order Wasserstein compact containment on a fixed finite time interval, or frozen first-feature Gram lower bound. The mixed Hessian and candidate-first-exit argument close without using the confinement result they subsequently establish. The compact-containment argument has both ingredients it needs: an average derivative-energy cutoff and uniform tails for the relevant path norms.

This verdict does not certify a mean-field identification, a population continuation theorem, strong compactness of velocities, an unweighted kernel lower bound, a response-kernel estimate, or nonlazy motion. The source does not claim those conclusions. “Actual raw GD” is checked against the precise variables, metric, and updates defined in this note, not against an unprovided outside model.

## 1. Claim coverage

| Source location | Claim checked | Audit result |
| --- | --- | --- |
| 16–35 | Activations, input covariance, centered initialization, output scaling, SUM loss, backward fields | Consistent; all required global activation bounds hold |
| 37–47, 114–125 | Simultaneous updates and raw metric | Exactly metric gradient descent for the displayed SUM loss |
| 96–113 | Bounds through a candidate first exit and along its segment | Valid before descent is established |
| 127–156 | Mixed differentials, raw Hessian bound, and descent at `eta=n^-2` | Valid; no missing factor of `n` or circular small-increment premise |
| 159–167 | Global finite-width GF from arbitrary finite initial parameters | Valid |
| 169–184 | Exact first-pair update, maximum increment, and average squared speed | Valid, with distinct uses of maximum and averaged bounds |
| 188–208 | Frozen rows and nonentry throughout every raw cell | Valid under the stated width condition; freezing itself needs no width or step restriction |
| 210–247 | Discrete and continuous excursion confinement, including scalar cases | Valid; excursions are not accumulated |
| 49–81, 251–269 | Main confinement and Gaussian exponential-moment conclusions | Valid with the stated time, width, and event quantifiers |
| 251–260 | Explicit bad-event probability | Correct for the actual two initialization variances |
| 270–286 | Markov bound and finite-power tails in probability | Valid; no unconditional GD expectation bound on the bad event is inferred |
| 83–92, 288–316 | Joint initial/path/activation laws in finite-order Wasserstein topology | Valid on each fixed `[0,T]` |
| 318–337 | Frozen Gram, count probabilities, and singular-input endpoint | Valid; the full-rank bound is for fixed `|rho|<1` |
| 339–347 | Limits on what is concluded | Consistent with the proofs |

## 2. Model, initialization, scaling, and metric

### 2.1 Activation and input assumptions

Because `p` is smooth and compactly supported, `p` and `p'` are bounded. Its evenness makes `phi_1` odd; nonnegativity and positivity on `(-R,R)` give

\[
\phi_1(z)=B_1\quad(z\ge R),\qquad
\phi_1(z)=-B_1\quad(z\le -R),\qquad B_1>0.
\]

The gates are positive exactly on `(-R,R)` and zero at its boundary and outside. Consequently `P_1` bounds `p`, and `L_1` is a global Lipschitz constant for `p`. The boundedness assertions for `arctan`, its first derivative, and its second derivative also hold. The later estimates use these fixed bounds, never a width-dependent activation or a clipping operation.

The input normalization gives a positive-semidefinite matrix

\[
C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},
\qquad \|C\|_{\rm op}=1+|\rho|\le2.
\]

At `rho=-1`, equality in the input inner-product bound forces `x_2=-x_1`. Thus `z_2=-z_1` at every parameter state, including raw interpolation states. No inverse of `C` is needed anywhere.

### 2.2 Actual centered initialization

The note explicitly uses independent entries with variances `1/d`, `1/n`, and `n^-2` in its three declared blocks. In particular the declared readout has standard deviation `1/n`, not `1/sqrt(n)`. No nonzero readout mean or sign bias is inserted later.

For each first row,

\[
\operatorname{Var}(W^{(1)}_i x_a)=\|x_a\|^2/d=1,
\qquad
\operatorname{Cov}(W^{(1)}_i x_1,W^{(1)}_i x_2)=\rho.
\]

These pairs are independent across rows, including at the degenerate endpoint `rho=-1`. Independence of evolved rows is neither true in general nor used.

The displayed output really includes another factor `1/n` after the readout. For example, conditional on the initialized hidden layers,

\[
\operatorname{Var}(f_a(0)\mid W^{(1)}(0),W^{(2)}(0))
=\frac{\|h^{(2)}_a(0)\|^2}{n^4}
\le\frac{B_2^2}{n^3}.
\]

This checks the consequences of the stated scaling directly; replacing the readout variance or removing the output normalization would be a different model. The proof needs only the coarser deterministic estimate `|f_a(0)| <= B_2 b` on the initial readout bound.

### 2.3 SUM loss and raw gradient

For `L=sum_a r_a^2` and `c_a=-2r_a`, the Euclidean block gradients are

\[
\begin{aligned}
\nabla_{W^{(1)}}L&=-\frac1n\sum_a c_a\delta^{(1)}_a x_a^T,\\
\nabla_{W^{(2)}}L&=-\frac1n\sum_a c_a\delta^{(2)}_a(h^{(1)}_a)^T,\\
\nabla_{W^{(3)}}L&=-\frac1n\sum_a c_a h^{(2)}_a.
\end{aligned}
\]

The constant raw metric weights the blocks by `d/n`, `1`, and `1/n`. Its inverse therefore multiplies these Euclidean gradients by `n/d`, `1`, and `n`, respectively. Negating and multiplying by `eta` gives precisely all three updates in (1), including their signs, factors of two, and width factors.

This is gradient descent in the stated fixed metric. There is no hidden replacement of SUM loss by mean loss, no parameter-dependent metric, and no omitted metric term in subsequent differentiations. Raw first preactivations interpolate affinely because they are linear in `W^(1)`; deeper fields and the loss are recomputed along the raw segment and need not interpolate affinely.

## 3. GD first exit and every mixed Hessian term

### 3.1 The parameter bounds do not presume descent

Initially `sqrt(L_0) <= R_0 < R_*`. If node `m` were the first node with `sqrt(L_m)>R_*`, all updates producing nodes through `m` would use old-node coefficients satisfying

\[
\sum_a|c_a|=2\|r\|_1\le2\sqrt2\|r\|_2\le K.
\]

With `N=ceil(T/eta)` and `eta<=1`, the total elapsed update time is at most `N eta <= T+1=H`. The readout increment obeys

\[
\|\Delta W^{(3)}\|_\infty\le\eta B_2K,
\]

so its bound `M` includes the candidate exit node. At every old node used in this sum,

\[
\|\Delta W^{(2)}\|_{\rm op}
\le \frac\eta n\sum_a|c_a|\,
\|\delta^{(2)}_a\|\,\|h^{(1)}_a\|
\le\eta K P_2 M B_1.
\]

Summation gives `A`, also including that node. Convexity of the two block norms gives these bounds at every point of every intervening raw segment. Bounded activations and gates then give (4) along those segments, without requiring first-preactivation confinement or a bound on the candidate node's loss.

### 3.2 First differentials

For a unit raw tangent `V`, the three normalized block lengths have squared sum one. In particular each is at most one. Using `||x_a||=sqrt(d)` gives

\[
\frac{\|D_Vz^{(1)}_a\|}{\sqrt n}\le\alpha_1,
\qquad
\frac{\|D_Vz^{(2)}_a\|}{\sqrt n}
\le B_1\alpha_2+A P_1\alpha_1\le J.
\]

The readout differential contributes at most `B_2 alpha_3`; the hidden-field differential contributes at most `M P_2 J`. Hence `|D_Vf_a| <= F_*`. The raw gradient at any old node consequently has norm at most `K F_*`.

### 3.3 Second differentials

For unit raw tangents `U,V`, there are exactly three terms in `D_U D_V z^(2)`:

\[
V^{(2)}[p(z^{(1)})U^{(1)}x]
+U^{(2)}[p(z^{(1)})V^{(1)}x]
+W^{(2)}[p'(z^{(1)})(U^{(1)}x)(V^{(1)}x)].
\]

The first two have RMS norm at most `P_1` each. For the third,

\[
\frac{\|uv\|}{\sqrt n}
\le\sqrt n\,
\frac{\|u\|}{\sqrt n}\frac{\|v\|}{\sqrt n}
\]

gives the bound `A L_1 sqrt(n)`. This is the only growing factor needed in this estimate.

The second output differential consists of two readout/hidden cross terms, a top-activation curvature term, and the term containing `D_U D_V z^(2)`. Their respective bounds are

\[
2P_2J,\qquad M L_2J^2,\qquad
M P_2(2P_1+A L_1\sqrt n).
\]

The top curvature estimate correctly uses the coordinate bound `|W_i^(3)|<=M`:

\[
\frac1n\sum_i
|W_i^{(3)}\phi_2''(z_i^{(2)})
(D_Uz_i^{(2)})(D_Vz_i^{(2)})|
\le M L_2J^2.
\]

Thus the displayed `F_**(n)` accounts for all terms. There is no pure second readout derivative because the output is linear in the readout; second derivatives of the affine first preactivation vanish as well. Using the fixed raw metric, this bilinear estimate is the required operator estimate, not just an estimate along a particular update direction.

### 3.4 Candidate-segment residuals and Taylor descent

Integrating the first differential along the candidate segment gives

\[
\|r(\theta)\|_2
\le R_*+\sqrt2\eta K F_*^2.
\]

For sufficiently large `n`, `eta=n^-2` makes the added term at most one. Therefore throughout the segment

\[
\|D^2L\|_{\rm raw}
\le4F_*^2+2\sqrt2(R_*+1)F_{**}(n)=H_*(n).
\]

Here `D^2L=2 sum_a(Df_a tensor Df_a+r_a D^2f_a)` retains the factor two from SUM loss. The integral Taylor formula with `Delta=-eta grad_raw L_k` gives

\[
L_{k+1}\le L_k
-\eta\left(1-\frac{\eta H_*(n)}2\right)
\|\operatorname{grad}_{\rm raw}L_k\|_{\rm raw}^2.
\]

Since `eta H_*(n)=O_T(n^-2+n^-3/2)`, the asserted descent coefficient follows for large `n`. Applying it successively through the candidate exit gives `L_m<=L_0<R_*^2`, a contradiction. No monotonicity of the recomputed loss inside interpolation cells is asserted or needed.

For completeness, all width requirements can be imposed simultaneously:

\[
\sqrt2\,n^{-2}K F_*^2\le1,\qquad
n^{-2}H_*(n)\le1,\qquad
2L_1KQ n^{-3/2}<1,\qquad
2P_1KQ n^{-3/2}\le1.
\]

With `a=8,b=1`, every constant here is independent of the input angle and dimension. This verifies the stated dependence of `n_T`. Its dependence on `T` and the fixed activation bounds is allowed.

## 4. Finite-width GF and first-pair speed bounds

### 4.1 Global GF is established before confinement

At each fixed width and dimension the vector field is smooth in all finite parameter coordinates. The usual local contraction construction applies on a sufficiently small time interval inside a bounded parameter ball. Along such a local solution,

\[
-\dot L=\|\operatorname{grad}_{\rm raw}L\|_{\rm raw}^2.
\]

The residual, readout, and second-block bounds therefore hold by integration on any fixed finite horizon, taking `a,b` to be the finite norms of the actual initial parameters. Moreover,

\[
\|\dot W^{(1)}\|_F
\le K P_1Q\sqrt{n/d}.
\]

Thus the first block is also bounded on that horizon. The second block's operator bound implies a finite Frobenius bound at fixed width, and the readout's infinity bound implies a finite Euclidean bound. Boundedness of the vector field on the resulting parameter ball gives a limit at any proposed finite maximal endpoint; the local construction then extends the solution from that limit. Finite-time escape is excluded.

This argument works for every finite initial parameter tuple. Width-uniform bounds for arbitrary, unbounded families of initial tuples are not being claimed. The extension is in finite-dimensional parameter space and uses neither a limiting distribution nor a population uniqueness theorem.

### 4.2 Exact pair dynamics and the two different speed estimates

Multiplying the first parameter update by `x_a` gives the exact sample covariance factor `x_b^T x_a/d=C_ab`. Hence (5) is exact for the actual old-node fields, with

\[
u_i=(c_1q_{1,i}^{(1)},c_2q_{2,i}^{(1)}),\qquad
|u_i|\le KQ\sqrt n.
\]

Using `||C||<=2` and `p<=P_1` proves (6):

\[
|\Delta z_i|\le2P_1KQ\eta\sqrt n
=2P_1KQ n^{-3/2}=D_n.
\]

For the average estimate one must not insert this maximum-row bound and then average. Directly,

\[
\frac1n\sum_i|u_i|^2
=\sum_a c_a^2\frac{\|q_a^{(1)}\|^2}{n}
\le K^2Q^2.
\]

It follows that

\[
\frac1n\sum_i|\dot z_i|^2\le4P_1^2K^2Q^2.
\]

For GD this holds almost everywhere on each affine first-preactivation cell, with its old-node controls. For GF it holds at each time. Integration over `[0,T]` gives the stated average action bound. No uniform integrability or strong compactness of the squared velocities follows from this step alone, and none is used.

## 5. Whole-cell nonentry, exact freezing, and confinement

### 5.1 The frozen set barrier is valid even though the set is not convex

For fixed `u` and `z_* in F`, the vector field vanishes at `z_*`. Lipschitz continuity of `p` gives

\[
|b_u(z)-b_u(z_*)|
\le2L_1|u|\,|z-z_*|.
\]

The closed, nonempty set `F` has a nearest point to every `z` in this finite-dimensional space. Choosing that point yields (7). Applying the 1-Lipschitz property of distance gives, for every `theta in [0,1]`,

\[
\operatorname{dist}(z+\theta\eta b_u(z),F)
\ge\bigl(1-2\eta L_1|u|\bigr)
\operatorname{dist}(z,F).
\]

The width restriction makes this lower bound strictly positive whenever the old pair is outside `F`. This is a whole-segment statement, not just an endpoint test. It applies to the actual interpolation because the first preactivation is affine along a raw parameter segment. Induction permits different controls at successive nodes.

If the old pair is in `F`, both factors `p(z_a)` vanish, so the entire first-parameter row update is exactly zero. Later changes in other rows, the second layer, or the readout cannot undo these two zero factors. This proves permanent freezing at every width and step size, without a probability event or a descent hypothesis.

### 5.2 Discrete excursions do not accumulate an error per excursion

For a nonfrozen row, every node in a block with `z_1>R` has `|z_2|<R`. On every step whose old node is in this block,

\[
\Delta z_1=\eta\rho p(z_2)u_2,\qquad
\Delta z_2=\eta p(z_2)u_2,
\]

so `Delta(z_1-rho z_2)=0` exactly. Inside that one block the change in `z_2` between its first node and any other node has absolute value at most `2R`.

If the block starts at node zero, its first `z_1` value is the actual initial value. Otherwise the preceding node has `z_1<=R`, and the new block's first value is at most `R+D_n`. Therefore every node in the block is bounded by the relevant starting value plus `2|rho|R`. Repeating the reasoning for negative excursions and for the other sample proves

\[
|z_{a,i}(k\eta)|
\le\max(R,|G_{a,i}|)+2|\rho|R+D_n.
\]

One uses only the block containing the node under consideration. There is no sum over the number of blocks, the number of steps, or the total variation of `z_2`. Initially frozen rows satisfy this bound directly. The absolute value of an affine scalar interpolation is at most the larger endpoint absolute value, so no second `D_n` is needed inside a cell.

Finally,

\[
\max(R,|G|)+2|\rho|R+D_n
\le |G|+3R+D_n\le |G|+3R+1,
\]

which proves the announced GD bound with the stated additional error `O_T(n^-3/2)`.

### 5.3 Scalar cases

At `rho=0`, each coordinate has scalar update `eta p(z_a)u_a`. Distance to the closed complement of `(-R,R)` obeys the scalar version of the same estimate, with Lipschitz coefficient `L_1|u_a|`.

At `rho=-1`, the physical identity `z_2=-z_1` and the evenness of `p` reduce the first update to `eta p(z_1)(u_1-u_2)`. Its coefficient satisfies

\[
|u_1-u_2|\le\sqrt2|u_i|\le\sqrt2KQ\sqrt n.
\]

The already imposed condition with factor `2` covers both scalar cases and the whole raw cell. Thus an initially active coordinate remains strictly active through the specified horizon. These conclusions concern positivity of a gate, not positivity or nonvanishing of a velocity.

### 5.4 GF nonentry and excursions

For any fixed frozen point `z_*`, along the actual finite-width solution,

\[
|\dot z(t)|\le2L_1|u(t)|\,|z(t)-z_*|.
\]

The coefficient is integrable on every finite horizon by the bounds already obtained before using confinement. Forward Gronwall proves constancy if the pair starts at `z_*`. If it reaches `z_*` at a finite time `tau`, integration backward from `tau` and backward Gronwall show it must have been constant on the preceding finite interval. This excludes finite-time entry from outside.

On a connected component of the open set `{t:z_1(t)>R}`, the same invariant has zero derivative and the other coordinate lies in `(-R,R)`. A component starting after time zero starts continuously at `z_1=R`; a component adjoining zero uses the initial value, including its boundary case. This gives the refined bound with `D_n=0`. Infinitely many components cause no difficulty because their contributions are never added.

Together with global finite-width existence, the resulting deterministic bound holds for all `t>=0` for each fixed finite initialization. The scalar GF arguments similarly require no width or step restriction.

## 6. Every probability and exponential-moment statement

### 6.1 The event `E_n`

A maximal `1/4`-separated family on the unit sphere is a `1/4`-net. Disjoint radius-`1/8` balls centered at its points lie in a radius-`9/8` ball, so the net has at most `9^n` points. For a matrix `W`, approximating its two bilinear-form unit vectors by net points gives

\[
\|W\|_{\rm op}\le2\max_{u,v\text{ in the nets}}|u^TWv|.
\]

For the actual initialized `W^(2)`, every fixed unit-vector bilinear form has variance `1/n`. Thus

\[
\Pr(\|W^{(2)}(0)\|_{\rm op}>8)
\le 2\,9^{2n}e^{-8n}
=2e^{-(8-2\log9)n}.
\]

The initialized readout coordinate has variance `n^-2`, so its threshold-one Gaussian tail is at most `2e^{-n^2/2}`. The union bound over the `n` readout coordinates gives the second term in (11). Adding the two failure bounds proves exactly the stated `b_n`, which tends to zero. A bound exceeding one at a small width is merely uninformative there, not an error.

No event on first-layer rows is imposed. Independence between `E_n` and those rows is available from the initialization but is not needed for the displayed moment argument.

### 6.2 Exponential moments, including the GF all-time quantifier

For GD, fix `T` first and then take `n>=n_T`. Put `B=3R+1` and `X_{a,i}=sup_{t<=T}|z_{a,i}(t)|`. On `E_n`,

\[
X_{a,i}\le |G_{a,i}|+B,
\qquad
\mathbf1_{E_n}e^{\alpha X_{a,i}^2}
\le e^{2\alpha B^2}e^{2\alpha G_{a,i}^2}.
\]

For `0<alpha<1/4`, integrating the standard Gaussian density yields

\[
\mathbb E e^{2\alpha G^2}=(1-4\alpha)^{-1/2}.
\]

Linearity of expectation, with no independence assumption about the evolved paths, proves (3). The cutoff `alpha<1/4` is sufficient for this particular inequality; the note does not claim it is an optimal exponential threshold.

For GF, the deterministic confinement holds for arbitrary finite initial parameters, without `E_n`, at every width. It also has the time-independent constant `3R`. Consequently the same Gaussian calculation applies without an event indicator and even with `sup_{t>=0}`. Global existence and continuity make that supremum legitimate; it can also be expressed as a countable supremum over rational times. This all-time moment statement does not supply an all-time raw-GD estimate or a compactness assertion in an unbounded-time uniform metric.

### 6.3 Markov and finite-power tails

Let

\[
C_{\alpha,B}=e^{2\alpha B^2}/\sqrt{1-4\alpha}.
\]

For every positive threshold `M_0`, splitting off `E_n^c` and applying Markov on `E_n` gives

\[
\Pr\left(\frac1n\sum_i e^{\alpha X_{a,i}^2}>M_0\right)
\le b_n+C_{\alpha,B}/M_0,
\]

as claimed. This does not estimate the expectation of the GD exponential moment on `E_n^c`.

For `s>=1`, `alpha>0`, and nonnegative `x,r`, one may take

\[
C_{s,\alpha}=\sup_{x\ge0}x^s e^{-\alpha x^2/2}
=\left(\frac{s}{\alpha e}\right)^{s/2}.
\]

This proves the stated inequality

\[
x^s\mathbf1_{x>r}
\le C_{s,\alpha}e^{\alpha x^2}e^{-\alpha r^2/2}.
\]

When combining it with (3) or (12), choose `alpha` in `(0,1/4)`. In particular, for every `delta>0`, the empirical tail moment satisfies the explicit bound

\[
\Pr\left(\frac1n\sum_i X_{a,i}^s\mathbf1_{X_{a,i}>r}>\delta\right)
\le b_n+
\frac{C_{s,\alpha}C_{\alpha,B}}{\delta}
e^{-\alpha r^2/2}.
\]

Thus the tail is uniformly integrable in the needed asymptotic, in-probability sense: first take `limsup` as `n` grows and then let `r` grow. It also yields moment boundedness in probability. No uniform-in-time statement for one fixed GD width, no almost-sure statement across widths, and no expectation control on the bad event is substituted for this quantifier.

Separate coordinate moments control the joint norm without requiring independence. If `V_i=||z_i||_infinity` for the Euclidean two-coordinate path norm, then

\[
V_i^2\le X_{1,i}^2+X_{2,i}^2,
\qquad
e^{(\alpha/2)V_i^2}
\le\tfrac12\bigl(e^{\alpha X_{1,i}^2}+e^{\alpha X_{2,i}^2}\bigr).
\]

This supplies the asserted decrease in the exponent for a joint exponential-square bound. The initial-pair norm is at most `V_i`; the activation paths are bounded and are a Lipschitz image of the preactivation paths.

## 7. Wasserstein compact containment: explicit quantifier check

The argument in lines 288–316 can be made precise using a deterministic family of laws. This also verifies that the average derivative bound is not being misused as compactness of velocities.

Let `S=C([0,T];R^2)` with its uniform Euclidean norm, and define the extended action

\[
\mathcal A(\gamma)=
\begin{cases}
\int_0^T|\dot\gamma(t)|^2\,dt,&\gamma\text{ absolutely continuous with }\dot\gamma\in L^2,\\
+\infty,&\text{otherwise}.
\end{cases}
\]

For `beta=alpha/2`, `A_T=4T P_1^2K^2Q^2`, and a deterministic cutoff `M`, consider

\[
\mathcal D_{M,A_T}=
\left\{\mu:\int e^{\beta\|\gamma\|_\infty^2}\,d\mu\le M,
\quad\int\mathcal A(\gamma)\,d\mu\le A_T\right\}.
\]

The action is a legitimate extended nonnegative path functional. Its sublevel sets with bounded initial value have compact closure in the uniform topology: the initial bound and action bound imply a uniform bound on path values and the modulus

\[
|\gamma(t)-\gamma(s)|\le\sqrt{|t-s|}\,\mathcal A(\gamma)^{1/2}.
\]

Finite time grids then give total boundedness, and completeness of continuous-path space gives compact closure. Equivalently, lower semicontinuity of the action follows from its partition-energy characterization or from weak compactness of bounded derivatives and uniform convergence of paths. No compactness of derivatives in their strong `L^2` topology is needed.

For laws in `D`, Markov gives

\[
\mu(\mathcal A>E)\le A_T/E,
\qquad
\mu(|\gamma(0)|>L)\le M e^{-\beta L^2}.
\]

Choosing `E,L` large proves tightness uniformly over this deterministic family. Separately, the exponential cutoff gives uniform integrability of `||gamma||_infinity^s` for every fixed finite `s`.

These two properties imply relative `W_s` compactness. A direct verification is to select a compact set `K` with uniformly small outside mass, partition `K` into finitely many small-diameter cells, and map each cell to a representative. For the outside transport cost use

\[
\int_{K^c}\|\gamma\|_\infty^s\,d\mu
\le\int_{\|\gamma\|_\infty>L}\|\gamma\|_\infty^s\,d\mu
+L^s\mu(K^c).
\]

Choose `L` using the uniform moment tail, then choose `K` using tightness. The resulting uniformly accurate finite-support approximations lie in a compact finite-dimensional simplex of laws. This proves total boundedness in `W_s`; completeness yields compactness of the `W_s` closure. This is exactly the norm-tail issue that weak tightness alone would not settle.

For the empirical preactivation-path law, the action cutoff holds on `E_n` for both schemes at the stated widths. The joint exponential inequality above gives

\[
\mathbb E\left[\mathbf1_{E_n}\int e^{\beta\|\gamma\|_\infty^2}\,d\mu_n\right]
\le C_{\alpha,B}.
\]

It follows that

\[
\Pr(\mu_n\in\overline{\mathcal D_{M,A_T}}^{\,W_s})
\ge1-b_n-C_{\alpha,B}/M.
\]

Given `T`, `epsilon>0`, and finite `s>=1`, choose `M` so the last fraction is at most `epsilon`. The set is then deterministic and independent of `n`, and `b_n=o(1)`. This proves exactly `1-epsilon-o(1)` containment. A finite union bound gives simultaneous containment for GF and GD if that reading is desired, after enlarging `M`. The good-event action bound remains part of the definition of the family throughout; it is not dropped after obtaining tightness.

Finally, the graph map

\[
\Psi(\gamma)=(\gamma(0),\gamma,\phi_1\circ\gamma)
\]

lands in the source's product space, applying `phi_1` coordinatewise. For its sum metric,

\[
d(\Psi(\gamma),\Psi(\widetilde\gamma))
\le(2+P_1)\|\gamma-\widetilde\gamma\|_\infty.
\]

It induces a Lipschitz map on finite-order Wasserstein laws. The image of the compact set just constructed is therefore compact and contains precisely the claimed joint empirical initial/preactivation/activation laws on the same event. The initial pair here is the path's value at zero, not an additional unrelated random variable.

The result concerns laws of continuous paths, with fixed finite `T` and fixed finite Wasserstein order. It makes no claim about `W_infinity`, a velocity topology, or identification of any subsequential path law.

## 8. Frozen first-feature Gram and its probability

Each frozen equal-sign row contributes

\[
B_1^2\begin{pmatrix}1&1\\1&1\end{pmatrix}
\]

to the unnormalized first-feature Gram, regardless of whether both signs are positive or negative. Each frozen opposite-sign row contributes

\[
B_1^2\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.
\]

The outer products of all remaining rows are positive semidefinite. Dividing by `n` therefore gives the first inequality in (13). In the orthonormal symmetric and antisymmetric directions, the two eigenvalues of the frozen contribution are exactly

\[
2B_1^2N_s/n,\qquad 2B_1^2N_o/n.
\]

Their minimum is the second displayed lower bound. This is the ordinary empirical first-feature Gram; it does not insert gates, backward fields, or an inverse kernel.

For `|rho|<1`, the first Gaussian pair has positive density on all of `R^2`. Each of the equal-sign and opposite-sign frozen regions contains an open set, so `m_s,m_o>0`. For either group `j`, row independence gives

\[
\mathbb E(N_j/n)=m_j,\qquad
\operatorname{Var}(N_j/n)=m_j(1-m_j)/n.
\]

Chebyshev and a union bound, without assuming independence between the two counts, give

\[
\Pr(N_s\ge nm_s/2,\ N_o\ge nm_o/2)
\ge1-\frac4n\left(\frac{1-m_s}{m_s}+\frac{1-m_o}{m_o}\right).
\]

On this one initialization event, the minimum frozen eigenvalue is at least `B_1^2 min(m_s,m_o)` at every GD node and interpolation time and at every GF time. No further time union bound, no `E_n` restriction, and no large-width descent argument is necessary for preservation of this contribution. If one wants this event jointly with the finite-horizon GD controls, the failures can be combined by another union bound.

The positive constants and count probability are for the specified fixed angle. They are not uniform as the covariance approaches a singular endpoint. At `rho=-1`, `G_2=-G_1`, so `N_s=0`; oddness of `phi_1` places every first-feature vector, not just the frozen ones, in the antisymmetric direction. The note correctly withholds a full-rank lower bound there.

## 9. Required findings versus optional improvements

### Required findings

**None identified.** All displayed equations (1)–(13) and the surrounding scoped conclusions pass the checks above. No fatal, major, or minor mathematical flaw is assigned. In particular, no missing argument forces a change to the stated model, learning rate, metric, confinement estimate, probability quantifier, or path-law topology.

### Optional presentation improvements

- **O1 — Collect the width requirements.** Lines 143–156 and 203 impose several compatible large-width conditions. Listing their conjunction, as in Section 3.4 of this review, would make the angle/dimension independence of `n_T` immediately visible. The current proof already supplies each condition and closes without this edit.
- **O2 — Display a deterministic compact-containment class.** Lines 293–316 correctly retain both cutoffs. An explicit definition such as `D_{M,A_T}` and the bound `1-b_n-C/M` would make the order of choices in the probability statement easier to inspect. This is an exposition improvement, not a missing compactness hypothesis.
- **O3 — Make the absence of a uniform gate margin explicit.** The finite-width barrier keeps the distance positive, but its lower bound can deteriorate with width and elapsed time. Thus it does not itself provide a width-uniform distance from the frozen set or a positive gate value in a limiting law. The source's existing exclusions already prevent the prohibited mean-field or nonlazy inference; this additional sentence would clarify the quantitative limit of the barrier.

These suggestions are optional and do not condition the verdict. No change to the mathematical source was made or is required by this review.

## 10. Final scoped assessment

The note establishes its stated finite-width and first-path results for the specific compactly supported smooth first-layer derivative and the precise centered Gaussian scaling it defines. The GD argument controls the candidate segment before applying descent, the confinement argument uses an exact excursion invariant, and the probability argument preserves the good-event and finite-horizon quantifiers. The joint path-law conclusion is supported in every fixed finite Wasserstein order, and the frozen-feature Gram claim has the correct normalization, count probability, and singular-angle limitation.

Confidence is high for the mathematical claims actually audited above. No external application, dependency, experiment, prior result, mean-field theorem, or strong-velocity conclusion was verified or inferred.

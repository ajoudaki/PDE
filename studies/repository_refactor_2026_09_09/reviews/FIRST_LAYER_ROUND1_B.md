# Independent isolated full-proof audit

## Verdict

**MINOR NOTATION CORRECTIONS REQUIRED; NO SUBSTANTIVE PROOF GAP FOUND.**

I independently checked the deterministic finite dynamics, Gaussian good events, row-work estimates, moment gains, strong velocity translations, measure compactness construction, reconstruction maps, and every asserted kinetic and controlled-kernel limit. The claimed fixed-input, fixed-correlation, first-layer compactness theorem is supported after the two local notation corrections identified below. No change to its dynamics, initialization, hypotheses, normalization, step size, topology, or substantive conclusions is required by this audit.

This is not a literal clean-copy verdict: the permitted text never defines `C_{ab}`, although several theorem formulas and calculations use it, and one continuity statement gives a matrix as the codomain of a path-valued map. I do not silently import definitions for those symbols. The verification below explicitly uses the repair `C_{ab}=G_{ab}`, which direct differentiation forces, and the stated continuous-path codomain.

## Exact evidence and read scope

The complete substantive input consisted of exactly these two files:

| Input | Bytes | Lines read | SHA-256 |
|---|---:|---:|---|
| `/tmp/pde-first-layer-isolated.D13ZM6gP/PROOF.md` | 66,319 | 1–1,596, completely | `d45999fc681e4bf66f95392f04f5940be6d3245d88a9eeea33f066560d665adb` |
| `/tmp/pde-first-layer-isolated.D13ZM6gP/NOTATION.md` | 5,110 | 1–98, completely | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

Both files were read from beginning to end before the audit conclusions were formed. Subsequent targeted searches and numbered rereads were confined to these files. All line references below refer to this exact `PROOF.md`, unless `NOTATION.md` is specified.

Both input SHA-256 digests were checked again after report creation and matched the initial digests above.

No source repository, study, previous review, conversation history, other agent's work, external skill document, or internet source supplied mathematical evidence. No experiments, generators, installations, builds, Git operations, or subagents were used. The input files were not edited. The only authored artifact is this report, created with `apply_patch` in the new directory `/tmp/pde-first-layer-fresh-audit.RvWqzzRA`.

The target audited is the stated deterministic and Gaussian actual-GF/raw-GD compactness theorem for two opposite labels at each fixed realized correlation in `[-1,1)`. Uniqueness, a full-population equation, full-sequence convergence, and equality of GF and GD limits are not part of that target.

## Required corrections: two actual local defects

### 1. Undefined Gram-entry symbol

`G=X^T X/d` is defined at lines 17–20. `NOTATION.md`, line 13, likewise names its entries `G_ab`. Neither permitted file defines `C_{ab}`. Nevertheless it appears at lines **246, 257, 363, 364, 410, 1472, 1474, and 1487**.

Replace `C_{ab}` by `G_{ab}` in those eight locations. This repairs (IV.19), (IV.20), the equation preceding (IV.28), (IV.32), (IV.102), and the explanatory entry bounds. An explicit alias would also resolve the undefined symbol, but replacement directly respects the notation contract.

The required entry is determined without any outside convention:

\[
 \dot z_a^{(1)}
 =\dot W^{(1)}x_a/\sqrt d
 =\sum_b c_b\delta_b^{(1)}\frac{x_b^Tx_a}{d}
 =\sum_b G_{ab}c_b\delta_b^{(1)}.
\]

In particular, `C` cannot be left as an arbitrary matrix: the controlled-kernel speed identity and its agreement with the `G`-based map (IV.103) require these Gram entries. This is a genuine self-containment defect, but the required replacement causes no downstream change of constants or arguments.

### 2. Incorrect codomain of the integral-defect map

At lines **1322–1324**, the text says that the integral-defect map is continuous from `C × L²` “to \(G\).” Here `G` is the fixed two-by-two Gram matrix, not a function space. The codomain must be

\[
 C([0,T];\mathbb R^2).
\]

The immediately following uniform-norm estimate is correct for that codomain. This is a local type error, not a failure of the closed-support argument.

**These are the only required corrections identified.** The remainder records the affirmative verification and its exact scope.

## 1. Model, normalization, metric, and clocks — (IV.1)–(IV.24)

The model agrees with the permitted notation contract: first preactivations are `W^(1)x/√d`, middle preactivations have no additional width factor, predictions contain `1/n`, and the deltas exclude the residual. The stored Gaussian readout has variance `n^(-2)`. All norms used below are ordinary finite norms unless an empirical factor is displayed.

Direct differentiation of one prediction gives

\[
 \nabla_{W^{(1)}}f_a=\frac{\delta_a^{(1)}x_a^T}{n\sqrt d},\qquad
 \nabla_{W^{(2)}}f_a=\frac{\delta_a^{(2)}(h_a^{(1)})^T}{n},\qquad
 \nabla_{W^{(3)}}f_a=\frac{h_a^{(2)}}n.
\]

Multiplication by `2r_a` and summation gives all three Euclidean gradients in (IV.23). The inverse block weights of (IV.22) are `n,1,n`; applying these gives exactly (IV.6) and (IV.7), with `c_a=-2r_a`. These are gradient dynamics in the declared raw metric, consistent with the mobilities in `NOTATION.md`, lines 78–82.

There is no missing or extra `√d`. A first row, regarded as a column, satisfies

\[
 \dot w_i=Xe_i/\sqrt d,\qquad
 v_i=X^T\dot w_i/\sqrt d=Ge_i,\qquad
 |\dot w_i|^2=e_i^TGe_i.
\]

The first-matrix contribution to the raw squared speed is therefore

\[
 \frac1n\|\dot W^{(1)}\|_F^2=\frac1n\sum_i e_i^TGe_i.
\]

It is not divided by an additional `d`. The factors of `d` have already combined in `G=X^TX/d`. The first-matrix metric really is `1/n` times the ordinary Frobenius metric.

The chain rule with the raw gradient gives (IV.24) exactly. For two samples, the declared mean loss is half the declared sum loss. Consequently

\[
 W_{\rm mean}(t)=W_{\Sigma}(t/2)
\]

for common initialization and the same mobilities. Reaching a given sum-flow state takes twice the physical time under mean loss. Equal GD parameter updates require `η_mean=2η_Σ`. The introductory bookkeeping is consistent; there is no unacknowledged half-squared-loss convention.

The norm and Wasserstein definitions in (IV.8)–(IV.9) use the same neuron for all four coordinates and both samples. Both velocity spaces carry strong `L²(dt)` norms, with no time normalization.

## 2. Global GF, primal stability, and actual transpose queries — (IV.25)–(IV.38)

At fixed `n,d` the vector field is smooth on the entire finite parameter space. The local contraction construction applies on a sufficiently small parameter ball. Energy dissipation gives

\[
 \int_0^{t_*}\|\dot W\|_{\rm raw}^2\,dt\le\mathcal L_\Sigma(0),\qquad
 \|W(t)-W(s)\|_{\rm raw}
 \le |t-s|^{1/2}\mathcal L_\Sigma(0)^{1/2}.
\]

Thus a solution at any finite proposed terminal time has a finite endpoint limit in a positive definite finite-dimensional metric. Restarting the local solution at that limit contradicts finite-time termination. This verifies global existence and finite-width uniqueness without needing any bound on the initially unobserved components of first rows.

The constants in (IV.26) follow in the stated order:

\[
 |r(0)|\le\sqrt2(B\beta+1)=R_0,\qquad
 \sum_a|c_a(t)|\le2\sqrt2R_0=K_c^{\rm F},
\]

\[
 \|W^{(3)}(t)\|_\infty\le\beta+BK_c^{\rm F}t,
\]

\[
 \|W^{(2)}(t)\|_{\rm op}
 \le\alpha+B\int_0^tK_c^{\rm F}(\beta+BK_c^{\rm F}s)\,ds.
\]

The last expression is bounded by the stated `A_F`. Each rank-one middle update has norm at most `|c_a|MB`, because its `1/n` cancels the two `√n` vector bounds. With `Q=AM`, the nondifferential estimates in (IV.27) follow directly. For each sample the velocity RMS is at most `K_cQ`; combining the two samples later accounts for the factor `√2` in `K_z`.

The initial fourth-moment hypothesis implies the per-sample RMS bound `b_4^(1/4)`. Integrating the velocity bound proves (IV.28); it does not presume a maximum bound on a first neuron.

All product rules in (IV.30) differentiate the actual fields. In particular the middle reverse derivative uses the coordinate bound on the readout:

\[
 \|\dot\delta_a^{(2)}\|/\sqrt n
 \le D_w+M\|\dot z_a^{(2)}\|/\sqrt n.
\]

Together with

\[
 \|\dot z_a^{(2)}\|/\sqrt n\le D_AB+AK_cQ,
\]

this gives exactly `D_Z`, `D_δ`, and `D_q=D_AM+AD_δ` in (IV.29)–(IV.31). No product of an uncontrolled reverse coordinate and a hidden velocity has been bounded as though both had maximum norms.

The kernel calculation (IV.32), with the first required notation repair, independently yields

\[
 k_{ab}=G_{ab}\frac{(\delta_a^{(1)})^T\delta_b^{(1)}}n
 +\frac{(\delta_a^{(2)})^T\delta_b^{(2)}}n
       \frac{(h_a^{(1)})^Th_b^{(1)}}n
 +\frac{(h_a^{(2)})^Th_b^{(2)}}n.
\]

Hence `ṙ=-2kr`, `ċ=4kr`, each entry has absolute value at most `K_*=Q²+M²B²+B²`, and `||k||op≤2K_*`. It follows that

\[
 \sum_a|\dot c_a|\le8\sqrt2K_*R_0,
\]

as claimed in (IV.33).

For `u_a=c_aq_a`, empirical Minkowski gives (IV.36) with `K_u^F=D_c^FQ_F+K_c^FD_q`. Applying the same inequality to the integral of the coordinatewise absolute derivatives gives (IV.38). The envelope controls a row's entire trajectory, and its empirical squared moment is bounded by `V_F²`. None of these estimates uses the last hypothesis of (IV.10) except the explicitly stated primal bound.

## 3. GF row work and every moment coefficient — (IV.39)–(IV.42)

Let `e_i=φ'(z_i)⊙u_i`. Since `s_i=φ'(z_i)⊙Ge_i`,

\[
 u_i\cdot s_i=e_i^TGe_i=|\dot w_i|^2\ge0.
\]

Integration by parts gives the actual row action, including both endpoint terms:

\[
 \mathcal A_i^{\rm F}
 =[u_i\cdot h_i]_0^T-\int_0^T\dot u_i\cdot h_i\,dt
 \le 2B\upsilon_i.
\]

The last inequality uses `|u_i(T)|_1≤|u_i(0)|_1+TV(u_i)` and `|h_{a,i}|≤B`. It is linear in the envelope, which is the essential improvement over a crude squared-envelope action bound.

The eigenvalues `1±ρ` imply `0≤G≤2I` and `G²≤2G`, also at the singular endpoint. Therefore

\[
 |v_i|^2\le2|\dot w_i|^2,\qquad |v_i|\le2\upsilon_i,
\]

\[
 \int|v_i|^2\le4B\upsilon_i,\qquad
 \int|v_i|^3\le(2\upsilon_i)(4B\upsilon_i)=8B\upsilon_i^2.
\]

Also `|s_i|≤|v_i|`. For the position,

\[
 \|z_i\|_\infty\le|z_i(0)|+\sqrt{2T\mathcal A_i^{\rm F}}.
\]

Using `(a+b)^4≤8(a^4+b^4)` gives

\[
 \|z_i\|_\infty^4
 \le8|z_i(0)|^4+32T^2(\mathcal A_i^{\rm F})^2
 \le8|z_i(0)|^4+128B^2T^2\upsilon_i^2.
\]

Finally `(∫|v_i|²)²≤16B²υ_i²`. Averaging these inequalities verifies every coefficient in (IV.42), including the fourth moment of the whole `L²` velocity norm. No inverse Gram matrix has been used in this moment gain.

## 4. Raw GD descent is closed without circular stability — (IV.43)–(IV.49)

For `T>0`, `η=n^(-2)≤1` and `Nη≤T+1=H`. Before a first candidate residual exit from `|r|≤R`, all old-node controls have the stated bound. Summing the exact readout and middle-matrix increments proves `M_G` and `A_G` through the candidate endpoint. Convexity extends these bounds along the whole raw segment. This argument does not use descent in advance.

For a unit raw tangent, the three numbers `a_1,a_2,a_3` satisfy `a_1²+a_2²+a_3²=1`. Input normalization gives (IV.44), and the first prediction differential is bounded by `F_*=B+M(B+A)`.

The three terms of (IV.45) are the complete mixed derivative of the second preactivation. The first two have RMS at most one each. The last has RMS at most `A√n`, because

\[
 \|u\odot v\|\le|u||v|.
\]

This is a permitted `√n` loss in the second derivative, not a missing `√d` normalization. In the full second prediction derivative, the two readout-tangent terms contribute at most `2J_0`. The term with `φ''(z^(2)) D_ζz^(2)D_ξz^(2)` is bounded by `MJ_0²` using the readout maximum norm and an `L¹` product estimate. The remaining term contributes at most `M(2+A√n)`. These are precisely (IV.46).

The old-node raw gradient has norm at most `K_cF_*`. Integrating the first prediction differential along its actual update segment gives a prediction change at most `ηK_cF_*²` per sample. Thus the first condition of (IV.60) bounds the segment residual by `R+1`, independently of any proposed descent conclusion.

For unit raw tangents the loss Hessian then has norm at most

\[
 4F_*^2+2\sqrt2(R+1)F_{**}(n)=H_*(n).
\]

Taylor's integral formula along the old-node gradient direction proves (IV.48) when `ηH_*(n)≤1`. Since `H_*(n)` is a constant plus a constant times `√n`, this holds eventually for `η=n^(-2)`. The candidate endpoint has residual at most `R_0<R`, so the exit cannot occur. Summing the resulting descent inequality proves (IV.49), including its factor `1/2`.

The width threshold depends on `T,α,β`, and not on `b_4,d,ρ`. The proof does not assert an exact loss-dissipation identity inside an affine GD cell.

## 5. Recomputed GD fields, discrete row work, and moments — (IV.50)–(IV.62)

The raw segment derivatives are held old-node updates. Their first-preactivation RMS, middle-matrix operator norm, and readout maximum norm are bounded as in (IV.50). Applying the genuine product rules to the recomputed nonlinear fields gives all of (IV.51). Continuity across nodes permits integration of those derivative bounds over full cells.

The recomputed control derivative satisfies

\[
 \sum_a|\dot c_a|=2\sum_a|\dot f_a|\le4K_c^{\rm G}F_*^2.
\]

The exact endpoint product identities (IV.52) have the indicated old/new factors, so they agree with the integrated bounds and do not drop mixed increments. Formula (IV.53) follows by integrating the first-preactivation speed through at most `H` units of time.

For the controlled query difference,

\[
 \Delta(c_aq_a)=(\Delta c_a)q_{k,a}+c_{k+1,a}\Delta q_a,
\]

the now-proved node residual bounds justify both endpoint controls. Empirical Minkowski gives (IV.54), with no extra sample factor. The envelope in (IV.55) includes exactly nodes `0,…,N-1`, which generate the cell velocities. Therefore

\[
 \frac1n\sum_i\upsilon_i^2\le V_{\rm G}^2,
 \qquad \max_i\upsilon_i\le\sqrt nV_{\rm G}.
\]

These facts are established before any row-work absorption, so that absorption is not circular.

At a node, `Δz_i=ηGe_{k,i}` and `|Δz_i|²≤2η²a_{k,i}`. The scalar Taylor remainders give exactly

\[
 \sum_a u_{k,a,i}\Delta h_{a,i}=\eta a_{k,i}+r_{k,i}^{\rm Tay},
 \qquad |r_{k,i}^{\rm Tay}|\le\eta^2\upsilon_i a_{k,i}.
\]

There is no division by `a_{k,i}`; zero row speeds are included. The last condition of (IV.60) implies `ηυ_i≤1/2` for every admissible outcome at the width in question. Summation by parts, with the boundary terms using `u_(N-1)h_N` and `u_0h_0`, gives an absolute bound `2Bυ_i`. Consequently

\[
 \tfrac12\sum_k\eta a_{k,i}\le2B\upsilon_i,
 \qquad \mathcal A_i^{\rm G}\le4B\upsilon_i.
\]

On a raw cell, `v_i=Ge_(k,i)` is constant. On that same cell,

\[
 s_i(t)=\phi'(z_i(t))\odot v_i,
\]

with the recomputed, generally nonconstant gate. Thus the bounds `|s_i|≤|v_i|`, `∫|v_i|²≤8Bυ_i`, and `∫|v_i|³≤16Bυ_i²` are all valid. Restricting the final full-cell action to `[0,T]` only decreases it.

The position bound uses `√(2H A_i^G)`. The same fourth-power calculation as for GF now gives `512B²H²υ_i²`, and the fourth moment of the `L²` velocity norm is bounded by `64B²υ_i²`. This verifies all coefficients in (IV.61)–(IV.62).

## 6. Singular antipodes and reconstruction — (IV.63)–(IV.69), (IV.93)–(IV.97)

At `ρ=-1`, input normalization gives `x_2=-x_1` exactly. Since there are no biases and both activations are odd, every raw state satisfies opposite preactivations, activations, and predictions for the two samples. Since `φ'` is even, both second deltas, both transpose queries, and both first deltas are equal. This remains true for an arbitrary, nonzero readout.

Opposite labels then give `r_2=-r_1` and `c_2=-c_1`. Hence the controlled queries and gated controls are antisymmetric. The doubled GF formulas (IV.66), and their exact old-node GD versions, follow. These are identities at all raw states, so no invariance approximation or limiting initialization is needed inside GD cells.

On `E_-={(b,-b)}`, `G` acts as multiplication by two. Thus `v=2e` and `D=G/4` gives `e=Dv` with `||D||op=1/2`. In the interior, the inverse and its norm in (IV.68)–(IV.69) are correct. There is no continuous extension of the interior inverse estimate being presumed at the endpoint.

In both cases `DGD=D`. Therefore

\[
 A_{\rm row}=XD/\sqrt d,\qquad
 A_{\rm row}^TA_{\rm row}=D,\qquad
 \|A_{\rm row}\|_{\rm op}^2=\kappa_\rho,
\]

\[
 \dot w_i=A_{\rm row}v_i,\qquad
 |\dot w_i|^2=v_i^TDv_i,\qquad
 w_i(t)-w_i(0)=A_{\rm row}(z_i(t)-z_i(0)).
\]

For the endpoint check `e=(b,-b)`, the row speed is `2bx_1/√d` and its squared norm is `4b²`. Meanwhile `v=(2b,-2b)` and `v^TDv=4b²`. This is one first-row energy. Neither a second sample-row energy nor a factor of `d` is to be added.

The endpoint symmetry is essential for the individual kernel entries: a general nullspace component of `e` would not be determined by `v=Ge`. Here that component is exactly absent, not estimated away.

Finally `P=XDX^T/d` is symmetric and idempotent, and `PX=X` for the realized inputs in both cases. Its range is their span, so it is the orthogonal projection onto that span. This proves (IV.97). The initial orthogonal component is constant and not contained in the two sample evaluations. Restricting the claimed row-law result to increments and velocities is therefore correct.

## 7. Strong translations at all admissible widths — (IV.70)–(IV.80)

The maxima defining `K_z,K_u,J,A_kin,B_path` correctly combine the preceding GF and GD estimates. In particular the two-sample instantaneous RMS uses `√2K_cQ`, while the cubic and path-norm fourth moments keep their already-derived coefficients.

For a shift `τ`, the GF controlled query difference is obtained by integrating its RMS derivative. For GD, the held controlled query crosses at most `τ/η+1` node increments. This gives the first line of (IV.72). The same argument gives the held-node gate position bound. The actual continuous first preactivation instead integrates its actual velocity and has the sharper `τ`, with no `η`, in the third line of (IV.72). No time extension is needed.

The relative arctan gate estimate is valid because

\[
 |(\log\phi')'(x)|=\frac{2|x|}{1+x^2}\le1,
 \qquad
 \frac{|a-b|}{a+b}=\tanh\!\left(\frac{|\log a-\log b|}{2}\right)
\]

for positive `a,b`. Thus `θ(x,y)≤min(1,|x-y|/2)`. The scalar algebra in (IV.74) follows by inserting `φ'(x)(u-v)` and using

\[
 \phi'(x)|v|\le|\phi'(x)u|+\phi'(x)|u-v|.
\]

Applying the coordinate estimates and then the Euclidean triangle inequality yields the same bound for two-vectors with the maximum coordinate ratio. No residual, control, or vanishing gate is divided out.

For the empirical space-time measure, `0≤θ≤1` implies `∫θ⁶≤∫θ²`. By (IV.72),

\[
 \|\theta\|_6\le(TK_z^2/4)^{1/6}(\tau+\epsilon)^{1/3}.
\]

Also `||e||_3≤κ_ρJ`. Hölder with `1/2=1/6+1/3` proves precisely (IV.75), including the factor two from the sum of shifted and unshifted gated fields. Multiplication by `G`, with norm at most two, and absorption of the linear term on the bounded shift interval give (IV.76).

For `s`, the proof uses the recomputed gate and the exact difference decomposition. Its gate difference is bounded by `min(1,|Δz_i|)`, so the same Hölder calculation with the actual-position shift gives the additional `J(TK_z²)^(1/6)τ^(1/3)` in (IV.77). This correctly treats the different GD gates.

The remaining `η` cannot by itself establish uniform compactness over all widths; the proof supplies the needed additional estimate. When `τ≤η`, a held velocity changes only for starting times crossing an internal node. There are at most `T/η` such nodes, each affecting a set of measure at most `τ`. The empirical squared difference is at most `4K_z²`. Thus (IV.78) and the minimum estimate (IV.79) are valid, including a partial terminal cell.

For `0<τ<min(1,T)`, splitting at `δ=τ^(3/5)` yields

\[
 \eta\le\delta:\quad(\tau+\eta)^{2/3}\le2^{2/3}\tau^{2/5},
 \qquad
 \eta>\delta:\quad\tau/\eta\le\tau^{2/5}.
\]

This proves a uniform `τ^(2/5)` bound for the squared velocity-translation norm. Squaring the estimate for `s` and using `τ^(2/3)≤τ^(2/5)` supplies its part of (IV.80). GF obeys the same weaker exponent. The result covers all outcomes and every admissible GD width; it does not discard finitely many fixed widths or confuse squared norms with norms.

## 8. Strong joint measure compactness — (IV.81)–(IV.86) and lines 1162–1196

For a fixed proof mesh, time averaging is a bounded finite-rank contraction on `L²`, and interpolation through finitely many node values is a bounded finite-rank contraction in the continuous-path supremum norm. Thus `Q_h` has exactly the stated properties on the full tuple space.

Expanding the square on a cell gives

\[
 \int_I|v-P_hv|^2
 =\frac1{2h}\int_I\int_I|v(t)-v(s)|^2\,ds\,dt.
\]

Splitting into the two orders cancels the factor two in the denominator. Enlarging within-cell pairs to all time pairs separated by `τ<h` gives `(1/h)∫_0^h C_1τ^(2/5)dτ=(5C_1/7)h^(2/5)`. This checks the coefficient in (IV.82).

Absolute continuity gives the displayed formula for `z-Π_hz`. Bounding each of its two integral terms by `√h||v||_(L²(I))` yields the `4h` bound for the squared supremum error, and hence (IV.83). The same calculation applies to `h` with derivative `s`. The direct same-atom projection coupling therefore has expected squared error at most

\[
 \varepsilon(h)=8hTK_z^2+(5C_1/7)h^{2/5}\longrightarrow0.
\]

This is an actual bound on `∫||ξ-Q_hξ||²dμ_n`, not merely an abstract upper bound on a Wasserstein infimum. That stronger fact also justifies its later use in Markov's inequality for direct tightness.

The full fourth-moment coefficient is correct. Applying `(a+b+c+d)²≤4(a²+b²+c²+d²)` to the four squared coordinate norms gives

\[
 \int\|\xi\|_{\mathcal E_T}^4d\mu_n
 \le4(B_{\rm path}+2A_{\rm kin}^2+4B^4)=M_4,
\]

because `||h_i||∞≤√2B`. Projection does not increase this moment.

The finite-cover construction proves Wasserstein total boundedness with control of quadratic tails, not only weak tightness. On each fixed finite-dimensional range, moving the part outside radius `R` to zero costs at most `M_4/R²` in squared transport distance. A finite grid for the remaining norm ball then costs at most `δ²`. The resulting probabilities are supported on a fixed finite set. Their masses range over a finite-dimensional simplex, which has finite grids; common mass can be coupled identically and unmatched mass costs at most that mass times the squared support diameter. This gives a finite Wasserstein cover. Combining it with the uniform direct projection bound covers the entire original union.

The proof also constructs the needed measure limits. Every original law is finite empirical. A Cauchy subsequence can be thinned so that adjacent finite transport tables have summable root-mean-square costs. The recursive subdivision of `[0,1]` realizes all successive tables on one probability space, with the correct finite marginals. Countably many interval endpoints can be ignored. By Cauchy–Schwarz, the expected sum of successive distances is finite, so the sum is finite almost surely. Completeness of `C × L² × C × L²` gives a limit point, and the `L²` triangle inequality gives a tail bounded by the sum of the remaining root-mean-square costs. The limit law has finite second moment and the empirical subsequence converges to it in the declared strong Wasserstein metric.

This construction supplies the significant measure-existence step; it does not rely on an omitted compactness or representation theorem. The coupling triangle arguments have the required justification: with a finite intermediate law, condition each coupling on its finitely many atoms and join the corresponding conditional laws. The same construction works when an endpoint law is a limit law. Thus the approximation of arbitrary closure points by empirical laws does not introduce an unresolved gluing step.

Approximating the `j`th point of the closure within `1/j` by a point of the original union proves sequential compactness of the closure. The stated open-cover argument then converts this to compactness: otherwise relative balls with radii tending to zero would fail to lie in any cover member, contradicting a convergent subsequence and openness at its limit. Total boundedness supplies the final finite subcover. This establishes one deterministic compact set for all the required outcomes.

The independent path-space tightness construction is valid as well. The closed set `G` used there is bounded and uniformly approximated by bounded finite-dimensional ranges; hence it is totally bounded and complete, and therefore compact. Its excluded mass is at most

\[
 M_4/R^4+\sum_{j\ge1}2^{2j}\varepsilon(h_j)
 \le a/2+a\sum_{j\ge1}2^{-j-1}=a.
\]

Thus neither tightness nor the quadratic tails are left implicit.

## 9. Gaussian bounds, measurability, and probability versus annealed UI — (IV.87)–(IV.91)

For fixed deterministic normalized inputs, each first row gives a centered Gaussian pair of covariance `G`, independently over rows. The representation `(U,ρU+√(1-ρ²)U')` is correct even at `ρ=-1`. Gaussian integration by parts gives `EU⁴=3` and `EU⁸=105`, while direct expansion gives `E[U²V²]=1+2ρ²`. Consequently

\[
 E|(U,V)|^4=8+4\rho^2\le12,
 \qquad E|(U,V)|^8\le8(EU^8+EV^8)=1680.
\]

The empirical fourth moment has variance at most `1680/n`. Exceeding 13 entails a deviation of more than one from its mean, so (IV.88) follows. There is no assertion that the loose upper bound is less than one at every width.

For the middle matrix, the packing argument gives a deterministic `1/4`-net of size at most `9^n`. Approximating the two unit test vectors costs at most half the operator norm, so norm greater than eight forces a net bilinear form greater than four in absolute value. Each fixed form has variance `1/n`. Its tail at four is at most `2exp(-8n)`, and the two nets have at most `9^(2n)` pairs. This proves exactly

\[
 2\exp(-(8-2\log9)n).
\]

The exponent is strictly positive. The actual stored readout has variance `n^(-2)`, so its maximum tail is at most `2n exp(-n²/2)`. Union of these three failure events gives (IV.13), without any need for independence between the events.

The deterministic compact set applies to every point of `E_n` for both schemes. Thus a common initialization requires only one failure event and has bound `b_n`; separate initializations give the union bound `2b_n`. The event is independent of the horizon, while the compact set and width threshold may depend on each fixed horizon.

The random empirical laws are measurable in the asserted Wasserstein topology. At each fixed width, GD is a finite composition of smooth maps; its raw interpolation and both `L²` derivative coordinates vary continuously with initialization. For GF, the energy bound places solutions from a bounded neighborhood of an initial state in a common finite-dimensional ball through `T`. A Lipschitz constant on that ball gives continuous dependence via the exponential integral-inequality estimate; evaluation of the vector field gives continuous dependence of velocities. Pairing the same finitely many neuron indices converts these facts into Wasserstein continuity.

The two truncations in (IV.91) concern different empirical measures. On `E_n`,

\[
 F_n(R)\le M_4/R^2
\]

truncates the squared norm of an entire tuple. In contrast,

\[
 L_n(R)\le\frac1R\frac1n\sum_i\int|v_i|^3\le J^3/R
\]

truncates velocity values under empirical neuron-time measure; the same holds for `s`. Once either deterministic bound is at most a given `a>0`, the corresponding exceedance probability is at most `P(E_n^c)`, eventually in width. This proves the exact order of limits in (IV.91).

These estimates say nothing about expectations over initialization on `E_n^c`. The proof correctly makes no inference of annealed uniform integrability or convergence of expected kinetic energies. It also does not infer eventual almost-sure goodness at all widths from the nonsummable `1680/n` estimate. Uniform probability constants for each deterministic input pair do not give a simultaneous event for adaptively selected pairs.

## 10. Population compatibility and joint row laws — (IV.15), (IV.17), (IV.92)–(IV.97)

After the codomain correction, the integral-defect map has difference bounded by

\[
 2\|z-z'\|_\infty+\sqrt T\|v-v'\|_2.
\]

The arctan path map is continuous in the uniform norm. The derivative relation is continuous because

\[
 \|\phi'(z_j)\odot v_j-\phi'(z)\odot v\|_2
 \le\|v_j-v\|_2+\|\phi'(z_j)-\phi'(z)\|_\infty\|v\|_2.
\]

Thus the simultaneous integral and chain-rule relations define a closed subset of the full strong tuple space. Every finite atom lies in it, including recomputed GD activation paths. In a coupling whose root-mean-square distance is `ε_n`, the population expectation of truncated distance to this closed set is at most `ε_n`. It vanishes in the limit, proving support on the set. The same closed-set argument preserves the antipodal constraints. This proves all four relations in (IV.15), not just the relation for `z`.

The map taking a tuple to its reconstructed raw increment and velocity has squared Lipschitz constant at most `4||A_row||op²`: subtracting the initial value costs at most a factor two in the position supremum norm, and the velocity map is linear. Pushing the couplings through this map proves the claimed Wasserstein convergence. Retaining the original tuple adds just its original squared coupling cost, so joint convergence is justified as well.

This step only requires a fixed realized pair of inputs in the fixed space `R^d`; it does not compare full-row laws in changing dimensions or reconstruct the missing initial orthogonal component.

## 11. Timewise representatives and strong-L² to L¹ maps — (IV.98)–(IV.106)

The proof does not evaluate an arbitrary `L²` equivalence class at a prescribed time. Uniform cell averages are measurable functions of the path and time: every averaging coefficient is a bounded linear functional on `L²`. They converge in `L²(dt)` for each path by density of interval-step functions and contraction of averaging. Their squared errors are bounded by `4||V||₂²`, which is integrable under a `P₂` law, so they converge in `L²(μ×dt)` as well.

A subsequence with summable `L²(μ×dt)` increments has a jointly measurable almost-everywhere limit. By Fubini, for almost every path this representative agrees almost everywhere in time with that path's `L²` class: the same averages already converge to that class in `L²(dt)`. This supplies the representative and the finite integral in (IV.98). The argument applies to `S` too. Products used below are integrable and do not depend on changes of representative on product-null sets.

For any chosen couplings with expected squared tuple distance at most `ε_n²→0`, set `M_n=(E||v_n||₂²)^(1/2)` and `M=(E||V||₂²)^(1/2)`. The triangle inequality gives `|M_n-M|≤ε_n`. Then

\[
 \|E|v_n(\cdot)|^2-E|V(\cdot)|^2\|_1
 \le E\int |v_n-V|(|v_n|+|V|)
 \le\varepsilon_n(M_n+M).
\]

This is precisely (IV.99). Its application to `s` proves the second speed limit. The quadratic raw form satisfies

\[
 |v^TDv-w^TDw|\le\kappa_\rho|v-w|(|v|+|w|),
\]

which proves (IV.100). Together with the exact finite row-speed identity, this proves all three limits in (IV.18) and the first-matrix action formula (IV.101). Integration over any fixed measurable time subset follows immediately by bounding the restricted integral error by the full `L¹` error. No pointwise-in-time convergence of the full sequence is being used.

For the kernel, common sample controls can be placed inside each empirical sum. With the repaired Gram notation and the specified held-node convention for GD,

\[
 j_{n,ab}^{(1)}=G_{ab}\frac1n\sum_i e_{n,a,i}e_{n,b,i},
 \qquad e_{n,i}=Dv_{n,i}.
\]

Define `H(v)=G⊙[(Dv)(Dv)^T]`. The elementary factorization

\[
 ee^T-ff^T=(e-f)e^T+f(e-f)^T
\]

gives the Frobenius bound `|e-f|(|e|+|f|)`. Entrywise multiplication by `G` is a contraction in Frobenius norm because each entry has absolute value at most one. Time Cauchy–Schwarz therefore gives

\[
 \|\mathcal H(v)-\mathcal H(w)\|_{L^1(F)}
 \le\kappa_\rho^2\|v-w\|_2(\|v\|_2+\|w\|_2),
 \qquad
 \|\mathcal H(v)\|_{L^1(F)}\le\kappa_\rho^2\|v\|_2^2.
\]

The second bound establishes integrability of the population map. The first, applied inside the coupling and followed by Cauchy–Schwarz in the coupling variable, gives exactly (IV.105). Thus the entire matrix, including both off-diagonal entries, converges in matrix-valued `L¹`. This conclusion requires neither separate convergence of the residual controls nor recovery of the unweighted deltas.

Finally,

\[
 \sum_{a,b}\mathcal H(v)_{ab}
 =(Dv)^TG(Dv)=v^TDGDv=v^TDv.
\]

This is the sum of all four entries, not the trace. At the antipodal endpoint a row contributes `b²` to each entry, with total `4b²`, matching its actual row energy. Positive semidefiniteness follows from `diag(Dv)Gdiag(Dv)`, but is not substituted for the entrywise identities.

Equation (IV.106) is the correct GD chain rule: the current raw loss gradient is paired with the held old-node gradient. It need not equal the negative squared held gradient. Accordingly the proof's controlled GD kernel is the node-controlled one. No equality or asymptotic equality with a recomputed interior-cell kernel has been proved or claimed.

The additional compact-containment statement for observables follows from the explicit coupling bounds: the raw-row pushforward, all three speed densities, and the full matrix are continuous maps of a `P₂` law into the displayed Wasserstein and `L¹` spaces. The joint image of the already-proved compact set is compact. All good-outcome observables lie in that one image, so the same failure probability applies without an additional union factor.

## 12. Endpoint cases, quantifiers, and coverage of the theorem

For `T=0`, the two velocity spaces are zero spaces and both raw-row observables vanish. The initial position and its arctan lie in a finite-dimensional space with the required fourth-moment bound. The finite-dimensional covering and measure-limit argument therefore proves compact containment directly; all asserted time-integral identities are vacuous equalities. There is no need to use the positive-time mesh or a nonexistent generating node.

For `d=1`, realized normalized input pairs with `ρ<1` are antipodal; interior correlations simply have no such one-dimensional inputs. This causes no defect in a theorem quantified over realized pairs. For general fixed dimension and interior correlation, the stated inverse has the required rank. Zero controls and zero row actions are included everywhere without division. The point `ρ=1`, varying correlations approaching an endpoint, and growing time horizons are explicitly excluded from the corresponding assertions.

The verified chain covers every substantive obligation:

| Obligation | Proof locations audited | Result after the two notation repairs |
|---|---|---|
| Actual model, sum-loss GF, raw GD, metric, normalization | (IV.1)–(IV.9), (IV.22)–(IV.24) | Correct |
| Global finite GF and uniform primal/query bounds | (IV.25)–(IV.38) | Correct |
| GF row work and stronger moments | (IV.39)–(IV.42) | Correct |
| Closed GD descent, threshold, and action bound | (IV.43)–(IV.49), (IV.60) | Correct; no circular stability premise |
| Actual GD reverse regularity and discrete moment gain | (IV.50)–(IV.62) | Correct; node/recomputed distinction preserved |
| Exact antipodal reduction and inverse on its range | (IV.63)–(IV.69) | Correct for the actual readout |
| Strong translations uniform over all admissible outcomes and widths | (IV.70)–(IV.80) | Correct |
| Strong joint Wasserstein compact set and explicit measure limits | (IV.81)–(IV.86), lines 1162–1196 | Correct; quadratic tails and limit existence supplied |
| Gaussian good-event and joint probability bounds | (IV.12)–(IV.14), (IV.87)–(IV.90) | Correct |
| Measurability and empirical UI in probability | Lines 1267–1307, (IV.91) | Correct; no annealed inference |
| Population compatibility and first-row increment/velocity laws | (IV.15)–(IV.17), (IV.92)–(IV.97) | Correct |
| Three speed densities and every controlled-kernel entry in `L¹` | (IV.18)–(IV.21), (IV.98)–(IV.106) | Correct |
| Compact containment of the joint observables and precise limit scope | Lines 1538–1596 | Correct |

In particular, compactness is established for the union of all admissible deterministic outcomes, not merely one chosen outcome per width. Every convergent subsequence has the stated compatibility and observable limits for its own limiting neuron law. The Gaussian statement is compact containment in probability, and the probability-space expectation in the limiting formulas is over that neuron law. The proof does not identify a unique population evolution or an expectation-level limit over initialization randomness. Those stronger statements are neither required for this theorem nor supplied by this audit.

# Audit plan: beyond-initialization two-layer tanh dynamics

2026-10-07. Bounded experiment-design task only. No simulation, numerical fit, or new global proof was run. SECOND_FORWARD_RESPONSE_STEP.md remains frozen and unreviewed; it is not evidence for this experimental plan.

Complete scientific inputs read for this task:

- CANDIDATE_SYSTEM.md, SHA-256 `a5fa62c596b5816859589be7af686829a5f4f65ddb8406138e15cf4468a45c31`.
- TWO_LAYER_MECHANISM_CHECK.md, SHA-256 `022b11454c281ac647e68f214a23f205de5029989ce88310702e320203b8623d`.

No other scientific source or study was consulted. The source formulas supply initial-time checks, not predictions that every initial sign or ordering persists at later times.

## 1. Question and primary comparison

The primary question is whether the closed feature–response population computation predicts the joint evolution of training outputs, passive outputs, and feature statistics beyond initialization, at a resolved fixed Euler mesh. The mechanism question is which distinct roles are played by:

1. the learned increment of the middle matrix;
2. reciprocal feedback from reusing the same initialized matrix in forward and transpose directions;
3. activation derivative gates;
4. changes in the representation of a passive input.

Prediction accuracy alone cannot separate these mechanisms. In particular, a passive prediction can change when every feature is frozen and only the readout learns.

Use the source panel

\[
v_1=e_1,\qquad v_2=e_2,\qquad
v_3=(2e_1+e_2)/\sqrt5,
\qquad S_{ab}=v_a^\top v_b.
\tag{1}
\]

Only indices 1 and 2 train. Compare $y=(\eta,\eta)$ with $y=(\eta,-\eta)$ for one declared nonzero $\eta$ in the authorized small-label class. Keep this $\eta$ fixed as dense width, population sample size, and timestep change. Do not make the labels width-dependent to obtain a cleaner comparison.

Write $T(z)=\tanh z$ and $g(z)=T'(z)=\operatorname{sech}^2z$. At dense width $n$ the model and physical clock are

\[
\begin{aligned}
z_{1,a}&=Av_a,&h_{1,a}&=T(z_{1,a}),&
z_{2,a}&=Wh_{1,a},&h_{2,a}&=T(z_{2,a}),\\
f_a&=w^\top h_{2,a}/n,&
\delta_{2,a}&=g(z_{2,a})\odot w,&
b_{1,a}&=W^\top\delta_{2,a},&
\delta_{1,a}&=g(z_{1,a})\odot b_{1,a},\\
\dot A&=\sum_{b=1}^2c_b\delta_{1,b}v_b^\top,&
\dot W&=\frac1n\sum_{b=1}^2c_b\delta_{2,b}h_{1,b}^\top,&
\dot w&=\sum_{b=1}^2c_bh_{2,b},&&c_b=y_b-f_b.
\end{aligned}
\tag{2}
\]

The factor $2/m$ is one because $m=2$. Initial $A$ entries have variance one, $G=W(0)$ entries have variance $1/n$, and $w(0)=0$. Use the same initialization within paired label-sign and parameter-freezing comparisons.

The first accuracy comparison should be dense simultaneous Euler updates against the population candidate at exactly the same timestep $\Delta$ and number of steps. All right-hand sides of a dense Euler step must use the old state; updating $w$ and then using its new value in the same step's hidden updates would be a different program.

## 2. Distinct, interpretable controls

The following is the minimum useful control set. “Recompute” means regenerate that control's residuals, covariance laws, tangent fields, and expected responses from its own evolving state.

| Control | Dense meaning | Population implementation | Legitimate interpretation |
|---|---|---|---|
| Full model | Train $A,W,w$ by (2) | Full candidate | Main mechanism and accuracy target |
| Frozen middle matrix | Set $W(t)=G$; train $A,w$ with the actual $G^\top$ backward action | Remove both learned-middle history sums; retain and recompute reciprocal responses | Constrained-gradient counterfactual removing middle-weight learning, not reciprocal reuse |
| Frozen first layer | Set $A(t)=A(0)$; train $W,w$ | Freeze $z_1,h_1$; keep middle writes and readout evolution | Constrained-gradient counterfactual removing lower-feature motion |
| Readout only | Freeze $A,W$; train $w$ | Constant feature kernel | Fixed-feature baseline and integration check |
| Response-off law | No canonical-gradient dense counterpart asserted | Mask all applied $R$ terms; recompute the remaining surrogate law | A mechanistic stress test of the reciprocal correction, not a valid gradient-flow approximation by definition |

Removing only the forward learned-middle term or only the backward one does not freeze $W$: a single learned matrix contributes to both directions. Such a one-sided deletion can be a separately named non-gradient surrogate, but it cannot be presented as the frozen-middle control.

Conversely, freezing $W$ does not justify setting $R=0$. The same fixed $G$ still acts forward and backward on adaptive features and backward signals. The source's nonzero first-layer cross-acceleration already survives when $W$ is frozen: middle learning has not yet had an opportunity to cause that particular acceleration.

At initialization, the source's total upper cross-acceleration splits into the middle-learning contribution and the propagated first-layer-motion contribution. Accordingly the frozen-$A$ and frozen-$W$ controls can check the two initial pieces separately. At later times the controls have different states and deficits. Their trajectory differences are counterfactual effects, not an additive decomposition of the full model's trajectory.

The readout-only dense model has constant empirical top-feature Gram $K^0_{ab}=h_{2,a}(0)^\top h_{2,b}(0)/n$. Its training deficit obeys

\[
\dot c=-K^0_{\mathrm{tr},\mathrm{tr}}c,
\qquad c(t)=e^{-tK^0_{\mathrm{tr},\mathrm{tr}}}y.
\tag{3}
\]

This gives an exact continuous-time benchmark for the chosen finite-width initialization. Its matched Euler recurrence is $c^{k+1}=(I-\Delta K^0_{\mathrm{tr},\mathrm{tr}})c^k$. Neither a physical feature-learning model nor a population solver is needed to check that recurrence.

### Optional dense control for untied initialized feedback

If a direct perturbation of transpose reuse is wanted, write $W=G+L$ and sample another fixed independent Gaussian matrix $B$ with the same entry variance as $G$. Keep the forward map $G+L$ and the learned increment equation from (2), but replace the lower carrier by

\[
b_{1,a}^{\mathrm{untied}}=(B+L)^\top\delta_{2,a}.
\tag{4}
\]

This preserves the learned increment in both directions and changes only the initialized backward operator. It is a fully specified modified vector field, but generally not the gradient of the original tanh network loss. No canonical PSD loss identity should be imposed on it.

Initially, $\dot b_{1,a}=B^\top d_a$ has no tied-$G$ alignment with the lower features, so it removes the source's leading first-layer cross-acceleration in the width limit. That is a useful initial negative control. It is not a proof that this untied model's complete later scalar law equals the candidate with $R=0$. Such a correspondence would need a separate derivation; do not infer it from a similar curve.

## 3. Separate mechanisms along the same full trajectory

Counterfactual training controls should be complemented by exact decompositions evaluated on one unchanged full trajectory. These avoid attributing all later differences to one term after the residuals and features have themselves changed.

### 3.1. Learned-middle memory versus initialized action

Let $L^k=W^k-G$. Simultaneous Euler updates imply the exact finite-width memory identity

\[
L^k=\frac\Delta n\sum_{j<k,b\leq2}
c_b^j\delta_{2,b}^j(h_{1,b}^j)^\top.
\tag{5}
\]

Hence, for any training or passive query $a$,

\[
\begin{aligned}
z_{2,a}^k
 &=Gh_{1,a}^k+L^kh_{1,a}^k,\\
L^kh_{1,a}^k
 &=\Delta\sum_{j<k,b\leq2}
c_b^j C^1_{ab}(k,j)\delta_{2,b}^j,\\
b_{1,a}^k
 &=G^\top\delta_{2,a}^k+(L^k)^\top\delta_{2,a}^k,\\
(L^k)^\top\delta_{2,a}^k
 &=\Delta\sum_{j<k,b\leq2}
c_b^j D^2_{ab}(k,j)h_{1,b}^j.
\end{aligned}
\tag{6}
\]

The Grams in this dense identity are normalized empirical inner products. Compare direct matrix products with reconstructed history sums as a hard implementation check. No asymptotic Gaussian approximation enters (5)–(6).

In the candidate, separately log the corresponding learned-memory fields and the two reciprocal fields

\[
\mathcal R^z_a(k)=\sum_{j<k,b\leq p}R^h_{ab}(k,j)\delta_{2,b}^j,
\qquad
\mathcal R^b_a(k)=\sum_{j\leq k,b\leq p}R^\delta_{ab}(k,j)h_{1,b}^j.
\tag{7}
\]

Report their root-mean-square magnitudes, their signed projections onto relevant feature/backward fields, and their mutual inner products. The squared norm of a sum includes cross terms; separate field norms are not additive “percentages of learning.” Current-time curvature and strict-past response contributions may additionally be displayed separately using the source's diagonal formula for $R^\delta(k,k)$.

For a stronger statistical reciprocal check, take $R$ coefficients computed by the independent population solver and apply the response sums to stored dense histories. Test whether the residual initialized actions have the predicted uncentered Gaussian covariance and selected mixed moments, within sampling and width error. This is a diagnostic of an approximate law, not a finite-width identity. Do not fit $R$ to those same dense residuals and then claim an independent confirmation.

### 3.2. An additive beyond-initialization velocity budget

At each full dense state, compute the exact vector-field identity

\[
\dot z_{2,a}=\dot W h_{1,a}+W\dot h_{1,a}.
\tag{8}
\]

Multiplication by $g(z_{2,a})$ and the product rule give an additive decomposition of $\dot C^2_{ab}(t,t)$ into a middle-weight part and an input-feature-motion part. For example the first part is

\[
\frac1n\left\langle g(z_{2,a})\odot\dot W h_{1,a},h_{2,b}\right\rangle
+\frac1n\left\langle h_{2,a},g(z_{2,b})\odot\dot W h_{1,b}\right\rangle.
\tag{9}
\]

Replacing $\dot W h_1$ by $W\dot h_1$ gives the other part. Their sum must equal the directly differentiated feature Gram at that state. This is meaningful beyond initialization and does not require interpreting a frozen-parameter trajectory difference as an additive term.

For an Euler trajectory, distinguish this instantaneous vector-field budget from the actual finite-step change: nonlinear finite-step increments have additional discretization terms. Integrating the budget by quadrature should approach the observed continuous-time change under timestep refinement, not be asserted exact at a nonzero Euler step.

## 4. Activation sensitivity: first measure it without changing the model

The exact lower-feature velocity is

\[
\dot h_{1,a}
=g(z_{1,a})\odot d_{1,a},\qquad
d_{1,a}=\sum_{b\leq2}c_bS_{ab}\,
g(z_{1,b})\odot b_{1,b}.
\tag{10}
\]

For the orthogonal training panel, this simplifies to

\[
\dot h_{1,a}=c_a g(z_{1,a})^2\odot b_{1,a},\qquad a=1,2.
\tag{11}
\]

Log the distributions of the gates and the gate-weighted velocity flux. A stable scalar diagnostic is

\[
\mathcal S_a
=\frac{\|g(z_{1,a})\odot d_{1,a}\|_{2,n}^2}
       {\|d_{1,a}\|_{2,n}^2}\in[0,1],
\tag{12}
\]

when the denominator is nonzero; report it as undefined at zero rather than add an arbitrary denominator floor. For a training input, one may also report
$\|g(z_{1,a})^2\odot b_{1,a}\|_{2,n}^2/\|b_{1,a}\|_{2,n}^2$.
Use predeclared gate bins or pilot-fixed quantiles, and show the corresponding carrier/drive magnitude. A raw correlation between speed and gate size is otherwise confounded by the carrier. Do not divide individual neuron velocities by very small gates to manufacture an unstable “ungated” estimate.

A snapshot intervention can replace a gate in one evaluated right-hand side while keeping the state, deficit and carrier fixed. This measures an instantaneous force change only; it is not a second trained trajectory or evidence for its eventual behavior.

If a gate-freezing trajectory is nevertheless run, specify precisely what changed:

- Keeping forward tanh but replacing backward gates by their initial values is generally a surrogate-gradient rule, not the gradient of the original loss.
- Replacing backward gates by one while retaining forward tanh is also a surrogate rule. It is not the linear-activation network, which changes both the forward activation and its derivative consistently.
- A gate frozen in physical time remains a function of its initial Gaussian primitives. Its response to an initial primitive probe must still be differentiated through that initialization dependence. Stopping every probe derivative of the frozen gate silently defines a different intervention.

There is no need to include these surrogate trajectories in the minimum experiment. The exact velocity identities, constrained-gradient controls, and source's squared-gate acceleration already give clean sensitivity diagnostics.

## 5. Passive-query diagnostics and invariance checks

Record $f_3$, both passive feature displacements

\[
\|h_{\ell,3}(t)-h_{\ell,3}(0)\|_{2,n}^2,
\qquad \ell=1,2,
\tag{13}
\]

and the passive–training similarities $C^\ell_{31},C^\ell_{32}$ at selected equal-time and two-time arguments. These distinguish moving representations from an output change caused only by readout learning.

Because $w(0)=0$, the exact same-path split

\[
f_3(t)=\frac1n w(t)^\top h_{2,3}(0)
+\frac1n w(t)^\top[h_{2,3}(t)-h_{2,3}(0)]
\tag{14}
\]

separates readout on the initial passive feature from a signed feature-motion correction. It is a descriptive decomposition on the full trained path, not a claim that either summand equals a separately trained model's prediction.

Use two passive implementation checks:

1. Adding or removing input 3 from the declared evaluation panel must not change the dense training updates. This is exact, not a width-limit assertion. In the population code, active laws must agree within its numerical error; bitwise agreement is expected only if its Gaussian sampling construction also preserves the existing active draws.
2. The lower initialization has $X_3=(2X_1+X_2)/\sqrt5$, but the upper initialization does not have $Z_3=(2Z_1+Z_2)/\sqrt5$. Its covariance is the nonlinear first-feature Gram from the source. Validate that full covariance before evolving any dynamics.

No passive target or residual is formed, and passive data are not used to tune labels or population coefficients. The asymmetry $2/\sqrt5$ versus $1/\sqrt5$ makes the opposite-sign passive output slope informative without introducing a validation label.

## 6. Label-sign contrasts and initial checks

For every initialization, pair the same-sign and opposite-sign label cases. Where useful, include all four corners $(\pm\eta,\pm\eta)$ and form the feature-statistic contrast

\[
\mathcal I_C(t)=\frac14\bigl[
C^{++}(t)-C^{+-}(t)-C^{-+}(t)+C^{--}(t)\bigr].
\tag{15}
\]

At initialization the source predicts the signed $y_1y_2$ cross-acceleration. At later times (15) is a finite sign-interaction contrast, not an exact bilinear coefficient or a mixed derivative at zero labels. It can include higher-order label dependence.

The canonical flow has an exact paired-seed global sign symmetry: changing $y$ to $-y$ with $w(0)=0$ leaves $A,W$ and features unchanged and changes the signs of $w,f$ and backward signals. Simultaneous Euler updates preserve this symmetry too. Thus the four-corner feature contrast reduces to half the same-minus-opposite difference, and global sign reversal is a useful implementation test. A corresponding bilinear contrast of the prediction itself vanishes by that symmetry and is not the appropriate feature-interaction statistic.

Before any beyond-initialization interpretation, verify the source checks:

- the first nonzero readout derivative and the correlated first-return covariance;
- zero initial hidden velocities;
- first-layer cross-acceleration with its label-product sign;
- the total top cross-acceleration, including both terms, not only middle learning;
- the passive first-layer acceleration and initial output slope;
- the frozen-$A$ and frozen-$W$ initial components described in Section 2.

Prefer analytic differentiation of the dense initialization equations, and independent Gaussian integration for their population coefficients. Estimating an acceleration by dividing a noisy feature-Gram increment by $t^2$ can amplify width/population noise severely. A fixed number of Euler startup steps also does not reproduce a continuous-time acceleration with its Taylor coefficient: timestep refinement must hold the physical observation time fixed, not keep that step count fixed. These checks validate implementation and normalization; they do not replace the positive-time comparison.

## 7. Population implementation checks specific to this candidate

The population solver needs persistent joint path samples in each population, not independent scalar resampling of each moment.

- Maintain separate lower and upper primitive/root families. Do not identify their particle indices as neuron correspondences or form cross-population coordinate pairings.
- Within a primitive family, preserve the full sample/time covariance. Use full uncentered query Grams, including their off-diagonal sample correlations.
- Build history covariance blocks from compatible stored path samples so the whole matrix is a Gram. Independently estimated entries need not form a positive-semidefinite covariance matrix.
- Zero innovations, including the zero initial reverse field, must stay zero. Any numerical rank threshold, PSD repair, or diagonal jitter must be logged and varied; silently adding noise changes the candidate.
- For response tangents, treat realized primitive coordinates as formal leaves. Hold all population coefficients fixed and do not differentiate through the Gaussian whitening or factorization map. A probe changes one primitive coordinate while other primitive values remain fixed, even though their sampled values are correlated.
- Validate selected tangent fields by small finite differences of the same local circuit with those coefficients and other primitive coordinates held fixed. Vary the probe size to distinguish truncation from floating-point error.
- Check the exact current-step response structure: off-diagonal $R^\delta_{ab}(k,k)$ vanishes, and the diagonal equals the expectation of $w^kT''(z_{2,a}^k)$ within integration error. Differentiating the shared deficit or moment estimates would generally corrupt this check.

If moments are estimated using the evolving particle ensemble, the resulting numerical computation is itself interacting and may have finite-population bias. Neither iid error bars over its particles nor an automatic $P^{-1/2}$ accuracy claim follows simply from the population law. Replication and population-size refinement must assess that approximation.

## 8. Keep three numerical error axes separate

Let $n$ be dense width, $P$ the population integration/sample budget, and $\Delta$ the Euler step. They are different parameters and must not all be increased or decreased together in the main comparison.

### Fixed-mesh population convergence

At a declared mesh and horizon, run successive population budgets, for example $P,2P,4P$, with independent complete-run seeds as well as any planned common-random-number pairing. Track means, run-to-run spread, and changes under refinement for every primary statistic. Hold dense width fixed during this check. Choose the production budget before inspecting the final dense-versus-candidate comparison.

A numerical covariance-rank tolerance is a fourth implementation parameter. Repeat the key calculation with a materially smaller tolerance and report the change and discarded covariance mass. Large negative covariance eigenvalues are a consistency defect, not evidence against the mathematical model.

### Matched fixed-mesh width comparison

At the resolved $P$ and the same fixed $\Delta$, compare several dense widths using independent dense initializations. Pair each initialization across labels and physical controls. Treat a complete initialization/run as the replicate; interacting neurons and successive times are not independent experimental replicates.

Show both the dense ensemble mean minus the candidate mean and the dense path-to-path spread. For a claim about the variability scale, additionally show the candidate discrepancy relative to that measured dense spread, with uncertainty from both ensembles. Matching one dense realization or obtaining a small raw error when labels are small is insufficient.

A finite width trend is descriptive. A fitted slope near $-1/2$ over a short width range does not prove an asymptotic rate, and a fitted intercept near zero does not prove the limiting law. Do not identify the population budget $P$ with the physical width $n$ by default; their errors could then cancel or mask one another.

### Timestep convergence and physical-time interpretation

Repeat at $\Delta,\Delta/2,\Delta/4$ with the same physical horizon and evaluation times, resolving population error at each mesh. This changes the history length and numerical difficulty; it is not covered by merely keeping the same population budget.

The clean primary statement remains agreement between matched Euler programs. Only after timestep refinement can one give an empirical continuous-time interpretation. A high-accuracy dense ODE solve may serve as an additional integration benchmark, but comparing it directly to an unresolved population Euler mesh confounds model and integration error.

The continuous full model and the legitimate frozen-parameter controls have exact PSD gradient-loss identities with only their trained parameter blocks included. The full tangent kernel is $C^2+C^1\circ D^2+S\circ D^1$; frozen $W$ removes the middle block, frozen $A$ removes the first-layer block, and readout-only keeps $C^2$. Check the instantaneous dense identities. Finite Euler steps need not decrease loss at arbitrary $\Delta$, and response-off/untied-feedback/gate-surrogate controls need not satisfy the canonical loss identity at all.

### Declared horizon and uncertainty reporting

Declare the time horizon and primary observation times before the final comparison. A useful clock is the inverse initial population top-feature Gram eigenvalue for the two training inputs; it supplies a fixed learning-time unit without selecting a horizon after looking for favorable agreement. Report the actual physical times as well.

Use paired-run uncertainty for control differences and independent-run uncertainty for the two numerical solvers. If confidence bands are based on resampling, resample whole runs/paths and state the procedure; do not treat pointwise intervals as simultaneous path guarantees. A predeclared finite time-grid maximum error is a transparent additional summary.

No finite horizon, label set, width grid, or numerical confidence band certifies all-time accuracy, arbitrary passive inputs, or every label in the original class. If the mechanisms remain too small compared with resolved numerical/width variability, report that lack of resolution rather than enlarging a contrast after seeing the result.

## 9. Minimum deliverable and decision rules

Use a small, readable set of diagnostics rather than a large ablation leaderboard:

1. Training/passive output curves and training loss: full population versus dense ensembles, with the readout-only baseline.
2. Same/opposite-label cross-feature similarities in both layers, plus passive feature displacement and passive–training similarity.
3. Full, frozen-$W$, and frozen-$A$ comparisons alongside the same-path velocity budget (8)–(9); do not merge these two types of evidence.
4. Reciprocal-response magnitudes and selected initialized-action residual covariance checks; response-off is explicitly marked as a surrogate.
5. Gate-weighted flux diagnostics and the passive signed representation correction in (14).
6. A compact numerical audit showing population, timestep, width, and covariance-tolerance refinements separately.

The full-law comparison is provisionally supported only if its main discrepancies persistently fall within the combined numerical and dense-sampling resolution across the declared positive-time window, and the joint feature/backward diagnostics agree as well as the outputs. A control is mechanistically discriminating when its predeclared affected statistic changes by more than that resolution while the hard implementation identities remain satisfied.

If $R=0$ happens to fit a selected output curve but misses cross-feature, backward-alignment, or passive-representation statistics, that is evidence that the output alone is nondiscriminating, not that reciprocal feedback is absent. If a frozen-middle control retains lower cross-feature motion, that is the expected separation between learned middle memory and tied initialized-map feedback, not a failed ablation. If all representation diagnostics are unresolved but readout predictions fit, the experiment has tested output fitting, not the proposed feature-learning mechanism.

All such conclusions concern the tested numerical regimes. They do not upgrade the frozen, unreviewed local proof or establish the missing global quantitative guarantee.

## Addendum: independent static audit of the dense implementation

The supervisor subsequently supplied the complete 240-line `dense_learning_experiment.py`, frozen for this audit at SHA-256 `58d566adc2898a49389c73d659147dd98d39b4eab0c24aaba444dbc91d8a7942`. This addendum audits that file only. I did not modify it, execute its self-test or simulations, read its imported maintained API, inspect generated results, or audit a resource-budget execution. “Pass” below means an algebraic/static check, not a claimed runtime result.

### Canonical coefficients and integrators: pass

The initializations have the required variances and exactly zero simulation readout. `fields` uses $Av$, $Wh_1$, $w^\top h_2/n$, and the two derivative-gated backward signals. Training slices `:2` exclude the passive input from all forces. The three velocities have exactly the $m=2$ coefficients in (2): no factor of two or missing middle-layer $1/n$ was found.

The Euler branch evaluates every component from the old state and then updates the tuple simultaneously. The RK4 branch evaluates each stage from a complete intermediate state with the same frozen constants, and uses the standard four-stage weighted combination. Its use of RK4 makes the dense curve a numerical ODE trajectory, not an exact match to the candidate's nonzero-step Euler history. Matched Euler runs or demonstrated timestep refinement remain necessary for that comparison.

The block kernel in `observe` is correctly ordered as readout, middle matrix, first matrix. Zeroing its middle block for `frozen_middle`, or its two hidden blocks for `frozen_features`, matches the trained coordinates of those modes.

In particular the line

`loss_derivative = -c @ K_train @ c`

is correct. Since $\mathcal L=(c_1^2+c_2^2)/2$ and $\dot f=Kc$ for $m=2$,

\[
\dot{\mathcal L}=-c^\top Kc.
\tag{16}
\]

An independent equivalent check, useful for extending the self-test, is

\[
\dot{\mathcal L}
=-\|\dot A\|_F^2/n-\|\dot W\|_F^2-\|\dot w\|_2^2/n,
\tag{17}
\]

with the frozen velocity blocks equal to zero. Formula (17) follows from the canonical parameter learning-rate metric; replacing it by the unweighted Euclidean sum would be incorrect. These are instantaneous ODE identities. The recorded quantity is not the exact finite-step RK4 or Euler loss decrement.

### Mode semantics: pass, with one important naming qualification

`frozen_middle` freezes only $W$, leaving the tied $G/G^\top$ uses and the $A,w$ gradients intact. `frozen_features` is the readout-only control: both $A$ and $W$ are frozen. Neither mode freezes or independently redraws the initialized feedback. A frozen-$A$-only complementary control is not implemented in this version; that is an absent diagnostic, not a bug in the implemented modes.

The implemented `affine_gates` mode is **not** the backward-only gate-freezing surrogate discussed in Section 4. It consistently replaces both forward activations by fixed affine maps:

\[
\begin{aligned}
\widetilde h_{1,a}
 &=h_{1,a}(0)+g_{1,a}(0)\odot(Av_a-z_{1,a}(0)),\\
\widetilde h_{2,a}
 &=h_{2,a}(0)+g_{2,a}(0)\odot(W\widetilde h_{1,a}-z_{2,a}(0)).
\end{aligned}
\tag{18}
\]

Their derivatives are the stored $g_{1,a}(0),g_{2,a}(0)$, exactly as used by `rhs`. The offsets and slopes are not mutated. Therefore this is a consistent gradient flow for its own fixed-initialization, input/neuron-specific affine objective. Its PSD block-kernel and loss identity are valid for that objective.

The qualification matters scientifically: this is a different transductive model on the declared panel, not the same shared tanh network with only backward gates frozen. It also is not the global first-order parameter/NTK linearization: the composed model still has products of the evolving $A,W,w$. A contrast with full tanh changes local curvature and the forward extrapolation away from initialization together. It cannot by itself isolate a purely backward-gating causal effect. Reports should call it the “initialization-anchored affine-activation control” or explain that meaning beside the shorter code name.

### Existing checks and quadrature: algebraically sound, coverage limited

The maintained-API comparison supplies raw inputs $\sqrt2\,V$ for $d=2$, consistent with the normalized directions used internally. It deliberately sets a nonzero test readout, making the hidden-layer velocity and kernel comparisons nontrivial. The adjacent comment about explicitly zeroing the readout is inaccurate for this test; actual simulation initialization remains correctly zero.

The Euler memory check stores each pre-update deficit, backward input, and lower feature. Its forward reconstruction is the learned rank-one increment applied to the current lower feature; its backward reconstruction is the transpose of the same increment applied to the current upper backward input. Both $1/17$ factors, history order, and sample indices are correct. Testing both orientations catches more than reconstructing the matrix increment alone. This is an exact Euler identity, not a test of a population approximation.

The Hermite rescaling is correct for standard-normal expectations. The returned constants `b1`, `b2middle`, and `b2` are the source's acceleration coefficients *after division by* $2y_1y_2$; they are not the full accelerations. Both terms in the total top-layer coefficient are present.

The self-test returns quadrature orders 100 and 160 but does not compare them or assert a tolerance. Printing both is useful evidence for a later comparison, not an automatic quadrature-convergence pass. Runtime success of any of these assertions has not been independently checked in this addendum.

Recommended bounded additions before stronger numerical claims are a direct check of (16) against (17) or a centered directional finite difference, mode-specific zero-velocity checks, paired global-label-sign symmetry, the exact readout-only solution/recurrence, and a declared quadrature-order difference tolerance. The current source does not contain those checks.

### What the saved diagnostics do and do not identify

`backward_init_rms` measures the full initialized action $G^\top\delta_2$, not the reciprocal response term alone. `backward_learned_rms` and `forward_learned_rms` correctly measure $(W-G)^\top\delta_2$ and $(W-G)h_1$. Their separate norms are not additive contributions to the total squared magnitude. Cross-inner-products would be needed for that interpretation.

The stored feature Grams, passive outputs, and per-input feature motions support genuine representation diagnostics. Initial-gate quartile motion is a descriptive paired-neuron statistic; carrier differences can still confound a causal gate-only interpretation. `gate_change` covers the first layer, and its vanishing in the affine mode is true by construction. It does not establish that changing gates was the sole cause of a full-versus-affine difference.

The current script is a dense-mechanism experiment. It implements neither the candidate population solver nor response-off or untied-feedback dynamics. Its outputs alone therefore cannot be described as a beyond-initialization numerical validation of the complete inverse-free population system. This limitation is independent of whether all dense comparisons look convincing.

### Provenance and robustness recommendations

The record contains method, mode, labels, width, seed, timestep, horizon, NumPy version, resource observations, and a source hash; output directories are not overwritten. One provenance issue needs procedural care: the source hash is read **after** `simulate` finishes. If the script is edited during a run, that hash could name code different from the version loaded by the running process. Freeze the file for the whole campaign, or record its startup hash and assert/record the final hash as well. This audit did not edit the script.

For small widths or tied gate quantiles, empty quartile bins can produce NaN diagnostics even when all state arrays remain finite. The production width makes this unlikely, but a general-purpose check should record bin counts or handle empty bins explicitly. Positive width/timestep and valid horizon/observation spacing should also be validated rather than relying on incidental downstream exceptions. These are robustness recommendations, not identified failures at the stated width-512 configuration.

Overall verdict: the inspected dense mathematics, mode implementation, loss coefficient, and two-sided memory test are internally consistent. The remaining qualifications concern control interpretation, missing independent numerical checks, and provenance/convergence evidence—not a discovered canonical normalization error.

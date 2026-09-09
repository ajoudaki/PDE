# Independent adversarial audit A

## Verdict and isolation

**PASS for the stated finite-dimensional model and quantifiers.** I found no false mathematical claim, missing premise needed for the stated conclusions, normalization error, or circular estimate. Theorem 1, Lemma 2, Theorem 3, and the uniform bounds follow as written. Required fixes: **none**. Optional improvements are listed separately below.

I read all 564 lines (23,903 bytes) of `/tmp/l2-two-sample-proof-0ywjpp/COMPACT_FIRST_LINEAR_TAIL_TOP_CLOCK.md`. This was the only source read. No dependencies, project files, history, reviews, skills, other agents, experiments, or external sources/imports were consulted. The audit concerns the explicitly defined equations and initialization; the names “canonical” and “RawGF,” novelty, and the opening provenance assertion cannot be independently authenticated from this one source.

Source SHA-256 before audit:

`cb0a9abb96ede054190b54cf883f9bd51081b39c3d7b36689eaa335268301e8b`

Source SHA-256 after audit:

`cb0a9abb96ede054190b54cf883f9bd51081b39c3d7b36689eaa335268301e8b`

The hashes agree. The source was not edited.

## Full mathematical coverage

### 1. Model, frozen rows, and exact loss normalization — (1)–(13)

The activation bounds in (3) follow from the integral definition, bounded derivative, and vanishing value at zero. Smooth compact support gives (p(\pm R)=0); evenness gives saturated values (\pm A). An entire first row with both coordinates saturated solves its row equation by remaining constant, even while the other parameters move. Restricting the smooth vector field to that fixed-row subspace and applying local uniqueness justifies invariance; this is not an assumption that arbitrary other rows freeze.

The eigenvalues of the frozen Gram contribution are exactly (2A^2N_s/n) and (2A^2N_o/n). Adding the other row outer products preserves its lower bound. Thus (7) is correct, including the need for both sign types for this two-dimensional bound.

For the **sum loss** (L=r_1^2+r_2^2), direct differentiation gives

\[
\nabla_{W^1}L=\frac2n\sum_a r_a\delta^1_ax_a^T,\quad
\nabla_{W^2}L=\frac2n\sum_a r_a\delta^2_a(h^1_a)^T,\quad
\nabla_{W^3}L=\frac2n\sum_a r_ah^2_a.
\]

Equation (5) therefore has respective gradient mobilities (n/d,1,n). Their reciprocals give precisely the speed weights (d/n,1,1/n) in (10). Differentiating each prediction gives the three kernels in (9), with factors (C_{ab}/n), (1/n^2), and (1/n); consequently (\dot r=-2Kr) and (-\dot L=4r^TKr). There is no missing sample-average factor or square root of width. Each kernel is a Gram matrix, including (K_1) with the stated Frobenius features.

Integrating the nonnegative squared speeds gives (11). The same estimate on any subinterval gives a uniform square-root modulus up to a finite maximal endpoint. Hence the parameters have finite limits there and smooth local existence extends the solution. Global existence requires neither frozen-Gram positivity nor a loss margin.

For the upper-layer coercivity in (12), the exact identity is

\[
K_2=\frac1n\sum_i(W_i^3)^2D_iG_1D_i.
\]

Congruence first gives (D_iG_1D_i\succeq\gamma D_i^2), and the derivative lower bound gives (D_i^2\succeq I). Summing produces (K_2\succeq\gamma b^2I). This does not rely on signs of correlations or entries. The factors in (13) follow: (\dot L\le-4\gamma b^2L), (\dot s\le-2\gamma b^2s) when (s>0). At zero residual every velocity vanishes.

### 2. Centered balance with moving first features — (14)–(20)

The derivative and limits of (D(z)) in (14) are correct and establish its exact supremum (D_*=\varepsilon\pi/2). The velocity estimate (16) uses (\sum_a|r_a|\le\sqrt2s), giving exactly (C_B=2\sqrt2MA).

Equation (17) differentiates (\|W^2-A_0\|_F^2) and (\|W^3\|_2^2/n), not a product involving a differentiated feature matrix. Substitution of (Bh^1_a=z^2_a-A_0h^1_a) is an identity at the current time. Thus there is **no missing (\dot H^1) term**. In particular,

\[
\|D(z^2_a)\|_2\le D_*\sqrt n,\qquad
\|\phi_2'(z^2_a)\odot A_0h^1_a\|_2\le Ma_0A\sqrt n.
\]

Together with (\|W^3\|_2=\sqrt n b), these give the exact advertised (C_D=4\sqrt2(D_*+Ma_0A)). The initial balance is (-b_0^2), so the sign of (+b_0^2) inside (18) is correct. Both directions of (19) follow; dropping (-b_0^2) in the upper bound for (a^2) is harmless.

The prediction estimate (20) uses a Frobenius bound on (H^2), not an invalid spectral inequality for nonlinear entrywise maps:

\[
\|H^2\|_F\le M\|W^2H^1\|_F
\le M\|W^2\|_{\rm op}A\sqrt{2n}.
\]

This verifies (C_f=\sqrt2MA). Centering avoids charging the initial Frobenius norm; the statement that this norm is typically of order (\sqrt n) follows under (37) from its squared norm being (n^{-1}\chi^2_{n^2}).

### 3. Divergent comparison integral and all-time convergence — (21)–(32)

The achieved margin supplies the persistent lower bound (\|f(t)\|_2\ge\eta=\sqrt2-s_0>0). For (b\le1), (20) gives (23) by bounding the bracket with ((a_0+1+\sqrt{C_D})(1+\sqrt X)); for (b\ge1), (c\le1) gives the same result directly. No positive initial readout lower bound is assumed.

The key integration has the correct sign and power:

\[
\dot s\le-2\gamma b^2s=-2\gamma bX'
\le-2\gamma c\frac{X'}{1+\sqrt X}.
\]

The primitive in (24) is correct, has derivative (1/(1+\sqrt x)) also at zero, and diverges at infinity. Thus (25) bounds (F(X(t))), and hence (X(t)), uniformly in time. It does not divide by (s), (b), or (X') to invert the clock. Zero-residual continuation handles the only nondifferentiability issue for (s=\|r\|). The case (\delta=2), hence (s_0=0), also works.

The logarithm estimate is loose but valid: the actual maximum of (\log(1+u)-u/2) is (\log2-1/2). Consequently (F(x)\ge\sqrt x-2\log2), and the square in (26) is a valid explicit bound, including for (X_0) itself. Monotonicity of (X) covers all times before (t_0). Equations (16), (19), and (23) then give exactly (\overline a,\overline b,U,\beta) in (26)–(27).

The loss rate is (4\gamma\beta^2), whereas the residual-norm rate and its integral use (2\gamma\beta^2); both factors in (28) are correct. Independently, (11) implies (b(t)\le b_0+\sqrt{tL(0)}), which integrates to (29). Thus the construction of the constants does not presuppose a finite infinite-time clock.

For (30), (\|h^2_a\|_2\le MAU\sqrt n) and (\|\delta^1_a\|_2\le PMU\sqrt n b) give the stated speeds, including the (\sqrt{d/n}) first-layer normalization. Their integrals are exactly (31). Finite total variation in these fixed finite-dimensional spaces yields actual parameter limits, not merely boundedness or subsequences. Prediction continuity gives exact interpolation at those limits.

Equation (32) follows from (\|q_{:,a}\|_2/\sqrt n\le2MU|r_a|b\le2MUsb). If the referenced first-coordinate equation is desired explicitly, (5) gives (\dot z^1_{ja}=\sum_b C_{ab}q_{jb}p(z^1_{jb})). No additional confinement theorem is needed for any conclusion here.

### 4. Actual short-time entry below loss 2 — (33)–(36)

The energy estimate and input norms give

\[
\frac{\|H^1(t)-H^1(0)\|_F}{\sqrt n}
\le P\sqrt{\frac{2d}{n}}\|W^1(t)-W^1(0)\|_F
\le\sqrt2P\sqrt{tL(0)}.
\]

The displayed product expansion before (35) includes **both** sources of feature motion and yields (35) with the stated constants. For (t\le\tau), (tL(0)\le1) and

\[
\frac{\|H^2(t)-H^2(0)\|_F^2}{n}
\le2M^2t\overline L[A+P(a_0+1)]^2\le\kappa/4.
\]

The triangle inequality for every unit (v\in\mathbb R^2) then lowers the smallest singular value of (Q=H^2/\sqrt n) from at least (\sqrt\kappa) to at least (\sqrt\kappa/2). Squaring gives (K_3(t)\succeq\kappa I/4), and (10) gives (L(t)\le L(0)e^{-\kappa t}). These estimates need neither (\phi_2'') nor individual readout-weight bounds.

Multiplication by the initial upper bound (2e^{\kappa\tau/2}) proves the actual margin (36). This is a finite-interval argument for the stated trajectory, including initial losses above 2, not a substitution of zero readout or an inference from just the initial derivative.

### 5. Gaussian coercivity, constants, and unconditional probability — (37)–(46)

Each initial first-row preactivation pair has exactly covariance (\left(\begin{smallmatrix}1&\rho\\\rho&1\end{smallmatrix}\right)), independently across rows and independently of both upper layers. Strict positivity of its density for (|\rho|<1) proves (m_s,m_o>0). The reservoir event therefore gives (\gamma_n\ge A^2\min(m_s,m_o)=\gamma). Bernoulli variance and a union bound give precisely (39); the two counts need not be independent.

Conditional on the initial first layer, the second-row pairs are independent (N(0,G)). The lower matrix bound (40) is sound: write (Z=U+\sqrt\gamma\xi). Given (U), the coordinates after activation are independent, and each has variance at least (\gamma), since (\phi_2'\ge1) expands scalar distances. For arbitrary signed (v), the conditional variance of (v^TV) is therefore at least (\gamma\|v\|^2). Adding the nonnegative squared conditional mean proves the second-moment inequality. No matrix-order preservation by entrywise activation, positive correlation, or unjustified independence of the unconditional coordinates is assumed. Finite variances follow from (|\phi_2(z)|\le M|z|).

The Gaussian fourth moment gives (\mathbb E[V_a^2V_b^2\mid H]\le3M^4A^4). Summing the four entry variances of the empirical matrix gives (12M^4A^4/n); the squared deviation threshold ((\gamma/2)^2) gives exactly (48M^4A^4/(n\gamma^2)) in (41), with (\kappa=\gamma/2).

Both Gaussian norm estimates have correct constants. The (1/4)-net volume ratio is (9^n); approximating both bilinear-form arguments costs at most half the operator norm. Threshold 8 thus reduces to threshold 4 for a (N(0,1/n)) scalar. Its tail (2e^{-8n}), union-bounded over (9^{2n}) pairs, gives (42). Also (b_0^2=n^{-3}\sum_i\xi_i^2), so (b_0>2/n) corresponds to (\sum_i\xi_i^2>4n). The exponential moment at (1/4) gives exactly (43). Both exponential constants are positive.

At time zero, (20) gives (\|f(0)\|\le\sqrt2q_0/n), hence (45). The two nontrivial thresholds in (44) respectively impose (q_0/n\le\sqrt2-1) and (q_0/n\le e^{\kappa\tau/4}-1). Thus (L(0)\le4) and (L(0)\le2e^{\kappa\tau/2}), with no claim about the sign of (L(0)-2). The specified Gaussian readout is nonzero almost surely; no step replaces it by zero.

Writing (E_K=\{K_3(0)\succeq\kappa I\}), the relevant failure bound is

\[
\Pr(E^c)\le\Pr(E_F^c)+\Pr(E_F\cap E_K^c)
+\Pr(\|A_0\|_{\rm op}>8)+\Pr(b_0>2/n).
\]

Integrating (41) over first-layer realizations in (E_F) bounds the second term. This proves the unconditional (46) without requiring independence between (E_K) and the operator-norm event. For each fixed correlation and activations, (N_*,\tau,\delta_*) are fixed, positive where appropriate, and independent of (n,d). The resulting per-width success probability tends to one. The result asserts neither success for every finite draw nor an almost-sure simultaneous event over all widths or correlations.

### 6. Uniform constants and precise scope — (47)–(49), section 8

The successful event has (s(\tau)\le s_*), (L(0)\le4), and (b_0\le2/n\le1). Substitution into (29) gives exactly (X_{\rm pre}=2\tau+(8/3)\tau^{3/2}). Using (\eta_*,c_*) in the same clock proof gives (47)–(48), including the (+1) in (b_*^2) and the residual integral (S_*). The normalized total variations inherit these uniform replacements. Equation (49) is simply (\|W^2h^1_a\|/\sqrt n\le U_*A).

These are bounds on the stated operator norms, centered Frobenius displacement, normalized Euclidean norms, and normalized variations. They are not width-independent bounds on the full unnormalized first/readout parameter norms or individual coordinate maxima. Parameter convergence is for each fixed finite network; no interchange of the infinite-width and infinite-time limits is proved.

The separate zero-readout diagnostic is correct: (r(0)=-y), (K_1(0)=K_2(0)=0), and (\dot L(0)=-4y^TK_3(0)y<0). It is not used to discharge the nonzero Gaussian case. Endpoint exclusions are accurate: at (\rho=1), the inputs coincide and the labels conflict; at (\rho=-1), oddness forces opposite feature columns, so this two-dimensional Gram lower bound fails even though the target has the compatible symmetry.

Finally, (\phi_2''(z)=-2\varepsilon z/(1+z^2)^2) is bounded, but (|W_i^3|\le\sqrt n b_*) supplies only a width-dependent curvature-product bound. The source correctly declines to infer a mean-field flow, uniqueness, propagation, persistent moving mass, nonlazy learning, or second-layer distributional nonaffinity. No finite-width optimization estimate is silently promoted to any of those claims.

## Counterexample attempts and their outcomes

1. **Remove the strict loss margin.** Take a positive frozen first Gram but (W^2=W^3=0). All velocities vanish and (L\equiv2). This is a genuine counterexample to replacing the margin by (L\le2), but satisfies neither the theorem's margin nor Lemma 2's initial (K_3\) bound.

2. **Make first features move to break the balance or short-time lemma.** Re-differentiation gives only parameter-norm derivatives in (17); the two feature-motion terms are explicitly present in (35). Thus movement of every nonfrozen first row does not break either argument.

3. **Let the readout decay to zero while upper weights grow, allowing (X\to\infty).** The centered balance and achieved margin force (b\ge c/(1+\sqrt X)). Integrating this lower bound against (X') forces the unbounded function (F(X)) to remain bounded. This rules out the proposed escape mechanism, including clocks with stationary intervals.

4. **Use negative correlations or dependence between the Gaussian events.** Conditional independent Gaussian noise proves (40) for arbitrary covariance sign. The restricted conditional union bound above handles the dependence between (K_3(0)) and (A_0). Neither attempt defeats the probability argument.

5. **Promote high-probability success to fixed-width almost-sure success.** Under the actual Gaussian law, the event that all first rows are same-sign saturated has probability (m_s^n>0). Then (h^1_1=h^1_2) forever, hence (f_1=f_2=u) and (L=2u^2+2\ge2). Thus almost-sure interpolation at any fixed width is actually false for this model, not just unproved by the given argument. This event is outside (E_F), so Theorem 3 is unaffected.

6. **Infer coordinatewise curvature control from the uniform moment bounds.** A concrete family of parameter states disproves that inference. For even (n), choose saturated first features with (H^TH=nA^2I). Let (u>0) solve (\phi_2(u)=1), set the top preactivation rows to (Z_1=(1,1)) and (Z_i=(u,-u)) for (i>1), and take (W^2=ZH^T/(nA^2)), (W_1^3=\sqrt n), (W_i^3=1) otherwise. Then (W^2H=Z), (\|W^2\|_{\rm op}\le\sqrt2/A), (b^2=2-1/n), and the normalized preactivation norms are bounded. Yet

   \[
   L=2/n^2+2\phi_2(1)^2/n\longrightarrow0,\qquad
   |W_1^3\phi_2''(1)|=\varepsilon\sqrt n/2.
   \]

   These are parameter states, not claimed canonical trajectories. They show why even positive first Gram, small loss, and the indicated bounded norms do not by themselves give uniform coordinatewise curvature control. They support the source's exclusion rather than contradicting its trajectory theorem.

## Required fixes

**None.** All numbered formulas (1)–(49), the three named results, parameter convergence, and the stated exclusions were checked. The usual finite-dimensional smooth-ODE existence/uniqueness and completeness facts are used with their hypotheses satisfied. No unstated premise from another file is needed.

## Optional improvements

- Strengthen the fixed-width caveat with the explicit (m_s^n) failure event above: fixed-width almost-sure interpolation is false here.
- Display (\dot z^1_{ja}=\sum_b C_{ab}q_{jb}p(z^1_{jb})) after (32) if the phrase “first-coordinate confinement equation” is intended to be immediately usable without any prior document.
- If discussing width limits elsewhere, explicitly retain the per-width probability quantifier and normalized norms. The (O(1/n)) bound in (46) alone does not establish an almost-sure eventual-success statement across all widths.

# Independent source audit: original canonical L3 local theorem

## Verdict and read certificate

**Verdict: no decisive mathematical gap found in the assembled local theorem, within this bounded source audit. The specialized fixed-program Gaussian/response law is proved internally; it is not accepted on the authority of a tensor-program theorem or of the opening assembled statement.** This supports the stated local, pure-arctangent, three-hidden-layer result. It does not support all-finite-time continuation or a finite-scalar description of the state.

- Audit date: 2026-09-08.
- Sole mathematical source: `/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/expanded_sources/EXPLAIN_PRIMARY/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md`.
- Full read: **all lines 1–2321**, without truncation, in consecutive ranges 1–580, 581–1160, 1161–1740, and 1741–2321. Subsequent targeted checks used only this same file.
- Source size: **2321 lines; 93,788 bytes**.
- Source SHA-256: `f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4`.
- The hash matched before and after the complete source read and targeted checks.
- Operational skill read completely: `/etc/codex/skills/solve-math-rigorously/SKILL.md`. Its external-result discipline informed the distinction between an internally supplied proof and an unsupported import.
- No other mathematical source, audit report, history, or master consolidation was read. No agents, experiments, source edits, or proof campaign were used. The only authored file is this report.

All line references below refer to the sole source above. This is an independent mathematical audit, not a formal verification certificate.

## Exact theorem being supported

The network has one input and target, both equal to one; three hidden layers of equal width $n$; activation $\phi=\arctan$; and predictor $f_n=n^{-1}(W^{(4)})^\top h^{(3)}$. Initialization has independent blocks with first-layer coordinates $N(0,1)$, both hidden matrices with iid $N(0,1/n)$ entries, and readout coordinates $N(0,n^{-2})$ (lines 9–32).

The finite algorithms are exactly the displayed raw updates with $\eta_n=n^{-2}$, physical time $t=k\eta_n$, and the corresponding finite gradient-flow equations. Raw parameters are linearly interpolated, with hidden preactivations and features recomputed from those parameters (lines 34–54). This is not a statement about an arbitrary learning-rate scaling, dataset, activation, or depth.

The population state is the four-object list

$$
(X^{(1)},W^{(2)},W^{(3)},W^{(4)}),\qquad
X^{(1)}=F(Z^{(1)}),\quad F(z)=z+z^3/3.
$$

The vector fields live in three fixed neuron $L^2$ spaces; the two matrices are bounded actions between adjacent spaces with their actual adjoints. Their countable construction retains reused-matrix correlations. The initial population readout is zero. This is an autonomous evolution of fields and operators, not a finite-dimensional scalar ODE, and not a representation of the initial Gaussian matrices by Hilbert–Schmidt kernels (lines 77–120, 470–547, 1776–1812, 1903–1910).

**Time scope:** the uncut feature-time construction is on $0\le s\le S_0$, where

$$
S_0=\min\{1,(2C_2)^{-1},(2C_3)^{-1}\},\qquad
T_0=\tfrac14\min\{S_0,(4a^2)^{-1}\},\quad a=\pi/2.
$$

Here $C_2,C_3$ are the explicit activation-only constants defined at lines 56–69 and derived at lines 900–978; they are not assumed moment or continuation constants. The assembled raw-GD/finite-GF/population theorem is on **$0\le t\le T_0$**. Fixed-cutoff flows exist for every finite feature horizon, but the uniform tail argument used to remove cutoff is local. Restart uniqueness is only along the reached trajectory within the constructed interval. It is not a continuation theorem for another interval of length $S_0$ or $T_0$ (lines 683–725, 1036–1038, 1344–1367, 1618–1694). Global continuation is expressly unproved (lines 4–5, 205–206, 1741–1743, 1912–1914).

## Fixed-program law: internal proof and import audit

The opening assertion that all premises are discharged (lines 177–203) was not treated as evidence by itself. The required proof is actually supplied in the embedded source-identification section, lines 211–451.

1. **Finite conditioning and transpose reuse.** Lines 299–331 give the conditional law after observations $WV=Y$ and $W^\top U=Q$, including the doubly projected residual. The adaptive query is measurable from the preceding transcript; observing its answer constrains only the queried matrix. This explains why the residuals of the two initially independent matrices can still be conditioned separately despite interleaved calls. For positive-definite limiting query Grams, coefficients converge from previously established contractions, and the normalized mean-square cost of the removed finite-rank projection vanishes. Conditional Gaussian averaging then supplies joint empirical weak convergence and convergence of second moments.

2. **The response identity is derived.** Lines 333–377 identify the non-Gaussian correction, rather than merely naming its final law. If $h_\perp=h-\sum_r\alpha_rv_r$, orthogonality to old forward inputs removes the old response part of each transpose output. Consequently

   $$
   E[q h_\perp]=E[\zeta h_\perp]
     =\Gamma_U E\nabla_\zeta h_\perp.
   $$

   Inverting $\Gamma_U$ in the positive-definite case and substituting the old forward decompositions cancels the old-response subtraction. The new response is $\sum_su_sE\partial_{\zeta_s}h$. The new Gaussian innovation has the required covariance with previous forward sources and variance $Eh^2$. Its construction also accounts for independent oriented Gaussian source groups without making the original matrix and its transpose independent.

3. **Singular Grams are addressed without assuming pseudoinverse continuity.** Lines 379–402 perturb each query input by fresh independent Gaussian noise. At fixed perturbation size the limiting new-input squared distance is at least $\epsilon^2$, so the nonsingular argument applies. Fixed-program Lipschitz stability and bounded initial operator norms control the coupled finite-width perturbation error by $C\epsilon$. The source recursion has no Gram inverse in its final derivative form: causal continuity of its coefficients, continuous covariance square roots, and bounded source derivatives permit the perturbation to vanish even at singular covariance. The nullspace/Stein calculation also explains why an off-support derivative choice cannot change its contracted response. These are substantive arguments present in the source, not an assumption of stable rank.

4. **The trained program and feedback match.** Lines 406–432 unroll the learned matrices, retain both forward and transpose rank-one terms, and freeze contractions only in an auxiliary finite oracle. Its population coefficients are causal. The finite contraction inequality and fixed-step Lipschitz comparison then transfer the oracle law back to empirical training feedback. The gate/readout products meet the fixed-program regularity assumptions after harmless extension outside their bounded ranges. The current-step return through the other matrix is explicitly retained in $b^{(2)}_{kk}$ at lines 436–445. Tiny nonzero readout initialization is dealt with at lines 447 and, for actual flows, at lines 1459–1487.

The derivative convention is essential: differentiate the explicit scalar program with deterministic coefficients and covariance parameters held fixed, keeping distinct Gaussian source slots as formal arguments at singular laws (lines 295, 783–786). The later bootstrap uses exactly this convention.

**Imported-proof check:** no indispensable nonclassical proof is left supplied only by an external theorem statement. The cutoff section does explicitly retain a “Representation premise” (lines 1058–1063, 1121–1143, 1741), but the earlier internal conditioning/response proof and common-action realization discharge that premise for this assembled file. The reference to `/tmp/L3_FIXED_MESH_SOURCE_IDENTIFICATION.md` at line 462 points to material embedded at lines 211–451. `TWO_HIDDEN_LAYER_PROOF.md` is mentioned at line 1393 and was not supplied or read; its cited query-noise mechanism is independently given at lines 379–402. Thus that mention is not an indispensable missing proof import. If the cutoff section were used alone, its representation premise would remain a real hypothesis.

The remaining general tools are classical Gaussian conditioning and integration by parts, laws of large numbers, countable probability-space construction and $L^2$ density, bounded-operator extension, Picard iteration, Gronwall, and basic integration/compactness facts. The specialized adaptive Gaussian law is not outsourced to one of these names: its required conditioning and response calculation is displayed.

## The main analytic bridges

| Bridge | Source evidence and assessment |
|---|---|
| Finite laws to common population actions | Lines 472–547 close a countable probe family under finite unions, pass second-moment norm inequalities and exact adjunction identities, and extend from a dense span. The explicit Gaussian net estimate supplies a width-independent operator bound. This gives actions on fixed spaces without asserting operator-norm convergence between different widths. No decisive gap found. |
| Fixed-cutoff flow and width limit | Lines 617–719 give cutoff-independent primal bounds and cutoff-dependent Lipschitz stability, with a closed path class preserving the readout pointwise bound. Euler error is uniform in width for fixed cutoff. Width is sent to infinity at a fixed finite program before the auxiliary Euler mesh tends to zero. No growing-program theorem is assumed here. |
| Mesh- and cutoff-uniform local tail | Lines 808–1034 derive the source-time factor $\Delta$, a Gaussian exponential envelope, the current top response bound, and then the current bottom response bound in causal order. The first-exit argument closes $U_k,V_k\le1/2$ for $S\le S_0$. Jensen uses only marginal Gaussian variances, not independence across times. The resulting $q_2=\zeta_2+\beta_2$ has Gaussian variance at most $a^2S^2$ and deterministically bounded shift. No decisive circularity or omitted current-source term found. |
| Cutoff removal and uniqueness | Lines 1259–1342 use the bounded-readout clipped reference asymmetrically. The vector-field discrepancy is bounded by $C(1+R)d+C\|b_R(q_B^{(2)})\|_2$. Fatou transfers the Euler exponential moment to the clipped flow, giving $\varepsilon_R=2K e^{-R^2/(16K^2)}$. This beats the $e^{CR}$ comparison loss, yields a Cauchy family, permits passage to the uncut vector field, and proves uniqueness without imposing a tail bound on a competing uncut solution. |
| Finite tails and empirical feedback | Lines 1369–1487 pass a continuous quadratic tail measurement through the fixed-cutoff width limit and use time equicontinuity to obtain a uniform reference-tail bound. They do not assume a uniform finite-width exponential moment. The actual nonzero finite readout is compared with the zero-readout clipped reference in normalized $L^2$. |
| Actual raw GD | Lines 1503–1614 explicitly handle the mismatch between Euler in $F(z)$ and transforming raw Euler. The exact cubic identity has accumulated normalized error $O(\eta\sqrt n+\eta^2n)$, which vanishes for $\eta=n^{-2}$. Positive random feature increments satisfy $0<\alpha_k=2\eta(1-f_{n,k})<3\eta$; all required endpoints stay within $7\bar S/8$. A pathwise quadrature estimate covers that random partition, and the fractional-step cubic identity covers the specified raw interpolation. This is an actual-GD bridge, not an identification only of transformed Euler. |
| Physical time and same-width GD/GF comparison | Lines 1618–1668 control clocks by scalar Lipschitz estimates while they remain strictly within the proven feature interval. Both actual algorithms are compared with the same clipped finite reference, yielding the displayed same-width state-distance convergence. No uncut global Lipschitz theorem is assumed. |

The limit order matters: fixed-program convergence alone has constants depending on program size and cutoff (lines 213, 451). The independent bootstrap and analytic comparisons supply the extra uniformity needed later; the proof does not silently apply the fixed-program statement to $O(n^2)$ steps.

## Actual gradient structure

Lines 1748–1910 establish gradient flow for the original squared loss in **raw coordinates**. The parameter metric has ordinary population $L^2$ lengths on $Z^{(1)}$ and $W^{(4)}$, and Hilbert–Schmidt lengths on the trained matrix increments. At finite width these correspond to normalized vector inner products $u^\top v/n$ and ordinary Frobenius matrix inner products. In particular, the matrix gradient is $\delta^{(\ell)}(h^{(\ell-1)})^\top/n$, whereas the normalized vector gradients have no additional $1/n$. This agrees with the raw update scaling.

The initial Gaussian actions are only bounded; they are not required to be Hilbert–Schmidt. Rank-one velocities and their integrated trained changes do belong to the Hilbert–Schmidt class, and the cutoff comparison passes those increments in that norm (lines 1776–1797).

The scalar predictor derivative is justified by the weighted Taylor-remainder estimate at lines 1814–1848, which truncates a fixed $L^2$ backward coefficient. It does not assume that a nonlinear coordinate map is Fréchet differentiable from all of $L^2$ to $L^2$. Its resulting gradient is

$$
\nabla f=(\delta^{(1)},\delta^{(2)}\otimes H^{(1)},
\delta^{(3)}\otimes H^{(2)},H^{(3)}).
$$

The curve chain rule returns from $X^{(1)}$ to $Z^{(1)}$; feature time gives $\theta_s=\nabla f$, and the proven physical clock gives $\theta_t=-2(f-1)\nabla f=-\nabla L$. Thus $\dot L=-4(f-1)^2\kappa$, with all four nonnegative kernel blocks displayed at lines 1892–1900. No decisive gap found in this metric, differentiability, or time-change bridge. The transformed coordinate itself is not being claimed to carry the same flat raw-coordinate metric.

## Exact convergence topology

- **Across widths:** convergence in probability of empirical laws of each specified finite same-layer probe tuple, in $\mathcal W_2$, uniformly for $t\in[0,T_0]$. The probes permit the stated finite compositions, globally Lipschitz coordinate maps, bounded products, both orientations of both current matrices, and finite joint time lists. This includes continuous tests of at most quadratic growth, so prediction, residual, loss, and the four displayed kernel blocks are covered (lines 122–150, 701–719, 1662–1668).
- **Unbounded backward factors and velocities:** these are not simply declared globally Lipschitz. The asymmetric comparison first controls $\delta^{(2)}$ and $q^{(1)}$; auxiliary truncation and uniform integrability then pass bounded gates and further operator calls (lines 1489–1501). Lines 1696–1737 give the GD derivative convention, preactivation velocity identities, and interpolation argument. The treatment is compressed, but the required squared-tail control comes from the established uniform $\mathcal W_2$ convergence and compact $L^2$ population time images. I found no decisive missing moment assumption here.
- **Entire hidden preactivation paths:** each layer's empirical path law converges in $\mathcal W_2(C([0,T_0]))$, including second moments of the supremum norm. Lines 1731–1737 bound piecewise-linear path approximation by $4|\pi|\int|\dot z|^2$, reducing this to finite-grid joint laws and the already controlled integrated speeds. Integrated squared velocities converge as stated.
- **Same width, same initialization:** actual GD and actual finite GF approach each other uniformly in the sum of the normalized $F(z^{(1)})$ difference, two operator-norm differences, and normalized readout difference (lines 152–157, 1652–1660).

There is no asserted coordinatewise coupling across distinct hidden layers, operator-norm convergence across different widths or to operators on different spaces, total-variation convergence, or almost-sure width convergence. The action-law limit and the same-width state comparison must remain distinct in consolidation.

## Nonlazy feature learning

Lines 1919–2320 contain an independent derivation conditional on the previously constructed flow, not just a feature-learning assertion. The multiplier lemma and curve chain rule give strong small-time expansions from the integral equations without requiring operator-norm convergence of the gate multipliers (lines 2035–2099).

The nonzero coefficients are checked using initial transpose conditioning at lines 2101–2177. In particular,

$$
P_2=c_3H^{(2)}_0+\sigma_3G_2^{\mathrm b},\qquad
P_1=c_2H^{(1)}_0+\sigma_2G_1^{\mathrm b},
$$

with $c_2,c_3,\sigma_2^2,\sigma_3^2>0$. The $c_3$ factor in the second return is retained. The innovation variance is the second moment of the transpose input, not that moment minus a response variance. Positivity of the initial forward variances, $\mathcal A^{(2)}_0\succeq m_1I$, $\mathcal A^{(3)}_0\succeq m_2I$, and the zero kernel of multiplication by $d(z)=(1+z^2)^{-1}$ establish nonzero $V_\ell$ and $d(Z^{(\ell)}_0)V_\ell$.

Consequently, for every hidden layer, as $t\downarrow0$,

$$
Z^{(\ell)}(t)-Z^{(\ell)}_0=2t^2V_\ell+o_{L^2}(t^2),\qquad
H^{(\ell)}(t)-H^{(\ell)}_0
=2t^2d(Z^{(\ell)}_0)V_\ell+o_{L^2}(t^2).
$$

The hidden kernel blocks are $4\gamma_\ell t^2+o(t^2)$, with each $\gamma_\ell>0$; hidden preactivation and feature integrated squared speeds have the displayed positive $16T^3/3$ coefficients. The total kernel has expansion $m_3+8(\gamma_1+\gamma_2+\gamma_3)t^2+o(t^2)$, and the best affine-approximation error for arctangent remains positive on a common initial interval (lines 2192–2320). These prove actual local hidden movement and a changing kernel despite zero limiting initial readout. They are small-time statements, not claims of a uniform lower speed or monotone feature displacement throughout training.

## Consolidation disposition

**Accept as source-supported, with no decisive gap found:** the canonical pure-atan L3 local population construction, its uniqueness in the stated bounded-primal class on fixed spaces, actual population gradient structure, the actual raw-GD and finite-GF local limit, the specified measured-law and preactivation-path topologies, and nonzero local learning in every hidden layer.

**Do not promote:** global uncut continuation, all-finite-time training limits, arbitrary-state restart existence, a finite-scalar closure, cross-width operator-norm convergence, or an assertion that the fixed-program theorem alone is uniform over growing training programs. Global continuation is a substantive unresolved extension expressly acknowledged by this source; it is not a hidden premise used to prove the local theorem.

No indispensable imported nonclassical proof was found missing from this assembled source. The surviving filename references and conditional language in individual embedded notes require reading the assembly, but do not by themselves invalidate its internal dependency chain.

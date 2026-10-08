# Does residual filtering preserve the measured learning path?

2026-10-07. Source-only diagnostic for the precommitted numerical repair of
the same m=16 geometry and full causal model. Inputs are
MULTISAMPLE_TRAJECTORY_RESULT.md, CANDIDATE_SYSTEM.md,
causal_filtered_integrator.py, residual_filter_experiment.py, and the frozen
multisample_experiment.py. No scientific run, model change, coefficient fit,
or global theorem is added here.

Use one paired comparison: measure each layer's Gram trajectory at both the
same normalized physical time and the same **raw training loss**, and check
the corresponding allocation of feature displacement between layers.
Monotone loss alone does not establish that a stable discretization follows
the gradient-flow learning path.

## What the numerical filter changes

The network has \(h_{1,a}=\tanh(Av_a)\),
\(h_{2,a}=\tanh(Wh_{1,a})\), and \(f_a=w^\top h_{2,a}/n\).
Only the m training indices \(\mathcal T\) have labels. The raw deficit is
\(c=y-f_{\mathcal T}\), and \(\mathcal L=\|c\|^2/m\).
Normalized physical time is \(\tau=2t/m\); its step is \(h=2\Delta t/m\).
This is a fixed change of units, not a fitted learning clock.

At a current dense state the normalized-time tangent kernel is
\[
K_{ab}=C^2_{ab}+C^1_{ab}D^2_{ab}+S_{ab}D^1_{ab},
\]
where \(C^\ell_{ab}=h_{\ell,a}^\top h_{\ell,b}/n\),
\(D^\ell_{ab}=\delta_{\ell,a}^\top\delta_{\ell,b}/n\),
\(S_{ab}=v_a^\top v_b\),
\(\delta_{2,a}=\tanh'(Wh_{1,a})\odot w\), and
\(\delta_{1,a}=\tanh'(Av_a)\odot W^\top\delta_{2,a}\).
Thus ordinary gradient flow has \(df/d\tau=K_{\cdot\mathcal T}c\).
The population integrator forms the corresponding kernel from its current
feature and backward-response Grams.

The new step solves
\[
\widetilde c^{\,k}=(I+hK^k_{\mathcal T\mathcal T})^{-1}c^k
\tag{1}
\]
and uses this same filtered deficit in every parameter or learned-history
write. The arrays named c contain raw deficits; write_deficit contains
\(\widetilde c\). Loss and fitting-stage definitions must use raw c.
The filter has no passive forcing index.

The distinction between stability and path accuracy is already visible at a
fixed dense state. Its **linearized** next training residual is exactly
\[
c^k-hK^k_{\mathcal T\mathcal T}\widetilde c^{\,k}
=\widetilde c^{\,k}.
\tag{2}
\]
Since this kernel is positive semidefinite, a kernel eigencomponent with
eigenvalue \(\lambda\ge0\) is multiplied by \(1/(1+h\lambda)\).
This contracts the linearized residual. The actual next prediction also
contains nonlinear feature changes, so (2) is not an unconditional
nonlinear loss-stability or trajectory-accuracy guarantee.

Different eigencomponents are damped by different factors. In general
\(\widetilde c\) is not a scalar multiple of c, and the step cannot be
interpreted simply as taking ordinary gradient flow more slowly.
The exact relation \(c-\widetilde c=hK\widetilde c\) identifies this as
an integrator-induced modification of the sample forces. Its off-diagonal
mixing is **not** new evidence of learned sample associations.

## One comparison, evaluated in time and at matched loss

Use the refined ordinary dense gradient-flow reference only on the horizon
where its own RK4 refinement has passed. If the reference remains unresolved,
the path comparison remains unresolved too. For dense comparisons use the
same initialized draw. Let \(\Delta C^\ell=C^\ell-C^\ell(0)\), and report
separately \(\ell=1,2\), off-diagonal TT entries, and all TP entries, where P
is the four-input passive panel. For a block B, define
\(\operatorname{rms}_B(X)=
(|B|^{-1}\sum_{(a,b)\in B}X_{ab}^2)^{1/2}\).

At equal normalized physical times on a common grid, measure
\[
\max_\tau\operatorname{rms}_B\!
\left[\Delta C^\ell_{\rm filtered,h}(\tau)
-\Delta C^\ell_{\rm reference}(\tau)\right].
\tag{3}
\]
Also retain the entrywise maximum, so an average cannot conceal one passive
input or a small collection of pairs. Subtract matrices before taking norms:
agreement only in their change magnitudes does not establish agreement in
the learned geometry.

For each already declared loss fraction \(r\), take the first crossing of
\(\mathcal L/\mathcal L(0)=r\) in each model and measure
\[
\operatorname{rms}_B\!
\left[\Delta C^\ell_{\rm filtered,h}(\tau_h(r))
-\Delta C^\ell_{\rm reference}(\tau_{\rm ref}(r))\right].
\tag{4}
\]
Use the same crossing/interpolation convention throughout and report actual
attained losses if using saved crossings. Do not fit a time warp, choose a
favorable crossing, or extrapolate a missing crossing. Matching loss is a
diagnostic alignment of observed trajectories, not a predictive closure.

At these same times and loss stages report both layer displacements,
separately over training and passive indices:
\[
M_{\ell,\mathcal A}^2=
\frac1{|\mathcal A|}\sum_{a\in\mathcal A}
\left[C^\ell_{aa}(\tau,\tau)+C^\ell_{aa}(0,0)
-2C^\ell_{aa}(\tau,0)\right],
\qquad \mathcal A=\mathcal T,\mathcal P.
\tag{5}
\]
For dense arrays this is the saved mean squared feature motion. Comparing
the pair \((M_{1,\mathcal A},M_{2,\mathcal A})\) detects whether filtering
shifts displacement between layers at the same fitting progress. Such a
shift caused by the integrator must not be described as a newly discovered
physical redistribution mechanism. These quantities are representation
displacements, not a conserved budget.

Apply (3)--(5) first to filtered dense paths versus the ordinary dense
reference, and then to filtered causal versus filtered dense paths on the
same mesh. The latter comparison checks the filtered numerical program;
it establishes gradient-flow fidelity only to the extent that the former
comparison and the causal discretization/particle controls support it.

Interpretation and falsifier:

- Large equal-time errors but small matched-loss errors and similar layer
  displacements are consistent with mainly timing bias for these observables.
  They do not prove a common scalar time reparameterization.
- Small loss but appreciable matched-loss Gram or layer-allocation errors
  indicates a changed representation path at that mesh. If these errors
  exceed the supported numerical/ensemble uncertainty, stable fitting alone
  cannot qualify that mesh as a resolved gradient-flow approximation.
- The desired repair reduces both comparisons under the precommitted step
  refinements. Agreement of filtered dense and causal outputs while both
  depart from the ordinary reference validates only their shared discrete
  program, not the original continuous learning mechanism.

No additional trajectory or step search is required by this diagnostic.

## The exact readout accounting uses filtered deficits

The filtered readout update is
\(w^{k+1}=w^k+h\sum_{b\in\mathcal T}\widetilde c_b^{\,k}h_{2,b}^k\).
With zero initial readout it gives the exact dense or population identity
\[
f_a^k=h\sum_{j<k,b\in\mathcal T}
\widetilde c_b^{\,j} C^2_{ab}(k,j),
\tag{6}
\]
using empirical inner products for dense histories and population inner
products for the causal history. Check (6) with saved write_deficit, not
raw c. The stored final filtered deficit is not used in a prediction at
that same time; the sum is strictly \(j<k\).

If raw c is inserted instead, its reconstruction error relative to (6)
is exactly
\[
h\sum_{j<k,b\in\mathcal T}
(c_b^j-\widetilde c_b^{\,j})C^2_{ab}(k,j).
\tag{7}
\]
This is the numerical force-filter contribution, not a missing reciprocal
term or a failure of the readout-memory mechanism. Formal local primitive
responses in the new source correctly freeze the effective write
coefficients \(\widetilde c\), as well as the other deterministic population
coefficients; they do not differentiate the population filter through an
individual Gaussian probe.

Identity (6) preserves the meaning of a historical training write evaluated
against the current query feature, including passive inputs. It can hold to
roundoff even on an inaccurate trajectory. Its role here is to keep the
mechanism accounting consistent while (3)--(5) test whether the numerically
stabilized path is also faithful to ordinary gradient flow.

# Master report: finite neural-PDE hypothesis, nonlinear explainability, and the remaining convergence gap

**Date:** 25 July 2026  
**Scope:** standard fully dense Euclidean \(\mu\)P residual network; ordered width-first, residual-depth-second limit; output, loss, and hidden-layer Gram observables  
**Status:** consolidated final report through the scalar Hermite experiment  

## Executive conclusion

The study now supports a strong practical result but not the full arbitrary-accuracy theorem.

> A genuine, autonomous, width-independent, nonlinear operator–Liouville PDE with the smallest useful source-Hermite closure (\(P=5\) in the original four-label problem) predicts nonlazy dense-network output, loss, and hidden-Gram dynamics with unexpectedly high accuracy and broad portability.

This success is not explained merely by identity or gain-adjusted linear dynamics:

- in the original activation-continuation study, the nonlinear dense Gram path was \(36.38\%\) from the identity path while the matched PDE was only \(1.09\%\) from the nonlinear dense path;
- a fixed gain-matched linear control reduced that discrepancy to \(3.46\%\), leaving a serious effective-linear loophole at the project’s \(5\%\) tolerance;
- the later scalar sine stress closed that loophole: gain-matched linear dynamics missed the dense Gram path by \(15.95\%\), while the nonlinear PDE matched dense Gram/output paths within \(2.50\%/2.81\%\).

Thus the PDE demonstrably captures nonlinear feature-learning dynamics beyond the tested fixed-gain linear controls.

The fixed low-order PDE also generalized without retuning across 14 configurations involving labels, input geometry, sample count, activations, and crossed stresses. Every observed full-curve error was below \(5\%\); the median/maximal Gram errors were \(1.71\%/4.14\%\).

The unresolved issue is different:

> It has not been shown that increasing the pure source-Hermite order produces a Cauchy sequence converging to the ordered dense limit with arbitrary accuracy.

The earliest apparent evidence against Hermite convergence was partly invalid. Exact parity makes even Hermite shells inert, so the old \(P=5\to15\to35\) comparison used a numerical-null even shell as its denominator. On the corrected odd ladder \(P=5\to35\to126\), the newly outgoing tail contracted by \(17\)–\(34\times\). However, aggregate high-to-low feedback and actual state/observable Cauchy increments did not contract through the tested degrees. In the scalar degree-13 study, a high-order turnover failed to replicate across cubature scrambles.

The final status is therefore:

\[
\boxed{\text{Useful, nonlinear, portable low-order finite PDE: strongly supported.}}
\]

\[
\boxed{\text{Pure-Hermite arbitrary-accuracy convergence: plausible but unresolved.}}
\]

\[
\boxed{\text{Full dense-network all-time theorem: additionally requires limit identification and stability.}}
\]

## 1. Canonical target and what counts as a finite neural PDE

The target is the standard dense Euclidean \(\mu\)P residual network with a fixed finite training set and squared loss. Width is taken to infinity first at fixed physical depth, and residual depth is then taken to infinity. The observables of interest are:

- the finite vector of training outputs \(f(t)\);
- the loss;
- the depth-indexed hidden Gram matrix \(G^h(s,t)\).

An admissible accuracy-dependent neural-PDE family must have:

1. a finite-dimensional source coordinate and finitely many depth fields at each approximation order;
2. no dependence of its mathematical state on network width \(n\), original layer count \(L\), or requested time horizon;
3. no microscopic \(n\times n\) matrices or width-indexed vectors;
4. a fixed architecture-local compiler for initialization, drift, and readouts;
5. no access to positive-time dense trajectories, fitted closure constants, or hidden oracle functions;
6. an autonomous, restartable state;
7. a basis/order fixed before observing positive-time reference data;
8. direct output and Gram readouts from current PDE moments;
9. projection only after the width limit, not a low-rank replacement of the dense finite architecture.

The implemented candidate is an operator–Galerkin conditional Liouville PDE. It expands dependence on the immutable Gaussian neuron label in Hermite coordinates, evolves a conditional law over a finite row-coordinate space, uses the same projected operator for forward and transpose actions, and reads output and Grams directly from current moments.

At each finite order it is a literal PDE rather than a disguised finite network. Its internal audits established:

- exact projected Euclidean-gradient structure;
- a positive-semidefinite tangent kernel and \(\dot f=-\Theta e\);
- correct loss dissipation;
- paired forward/transpose operators;
- autonomy and split/restart agreement;
- no dense-trajectory imports or fitted decoders.

## 2. Up-to-date conjectures

Let \(\mathcal O_\vartheta(t)=(f_\vartheta(t),G^h_\vartheta(\cdot,t))\) denote the ordered dense-limit observables for parameters/data \(\vartheta\) in the allowed class \(\mathcal U\), and define

\[
d_{\mathrm{obs}}(\mathcal O,\widetilde{\mathcal O})
=
\|f-\widetilde f\|_2+
\sup_{s\in[0,1]}\|G^h(s)-\widetilde G^h(s)\|_F.
\]

### 2.1 Broad finite-neural-PDE existence conjecture

There exists one admissible, architecture-local family of finite neural PDEs \(\{\mathsf P_k\}_{k\ge1}\), with unique global solutions and autonomous evolution, such that

\[
\boxed{
\inf_{k\ge1}\;
\sup_{\vartheta\in\mathcal U}\;
\sup_{t\ge0}
d_{\mathrm{obs}}
\bigl(\mathcal O_\vartheta(t),\mathcal O_{\mathsf P_k,\vartheta}(t)\bigr)
=0.}
\]

This is the irreducible project claim: for every accuracy, one predeclared finite PDE achieves it without microscopic state, trajectory playback, or horizon-dependent compilation.

### 2.2 Explicit operator–Hermite witness conjecture

For the complete-degree operator–Liouville family, let

\[
E_r=
\sup_{\vartheta\in\mathcal U}\sup_{t\ge0}
\left[
\|f_\vartheta^{(r)}(t)-f_\vartheta(t)\|_2+
\sup_s\|G_\vartheta^{h,(r)}(s,t)-G_\vartheta^h(s,t)\|_F
\right].
\]

The sharp existence statement inside this explicit family is

\[
\boxed{\inf_{r\ge1}E_r=0.}
\]

The stronger canonical Galerkin statement is

\[
\boxed{\lim_{r\to\infty}E_r=0.}
\]

The second statement says all sufficiently high complete Hermite degrees work, not merely a favorable subsequence. Neither statement is proved.

For the canonical odd-activation, symmetric-Gaussian model, the hierarchy should now be stated in parity-reduced form: only odd Hermite degrees are active. In the original four-label system, the nontrivial ladder is

\[
P=5\to35\to126\to\cdots,
\]

or \(4\to24\to80\to\cdots\) active odd modes after deleting inert coordinates.

Failure of this pure-Hermite witness would not logically refute the broader finite-PDE conjecture. A finite response/history enrichment could still satisfy the project-level statement.

## 3. Direct finite-PDE result

The first complete nonconstant system, \(P=5\), was integrated as a literal width-independent PDE.

Against the pooled \(n=256,L=32\) dense reference:

| Quantity | Result |
|---|---:|
| PDE feature motion | \(0.633801\) |
| Dense feature motion | \(0.639909\) |
| Maximum output gap | \(1.0753\times10^{-2}\) |
| Maximum loss-of-ensemble-mean gap | \(1.8457\times10^{-3}\) |
| Maximum absolute Gram gap | \(1.9408\times10^{-2}\) |
| Maximum Gram-increment surface gap | \(7.2433\times10^{-3}\) |
| Gram-increment gap / PDE feature motion | \(1.1428\%\) |

The discrepancy was statistically distinguishable, so the correct description is “close,” not “exact.”

The same autonomous PDE was continued through \(t=32\). After \(t=8\), output, Gram, tangent-kernel, and residual drift were at roughly \(10^{-13}\) or smaller. This rules out the interpretation that the PDE was merely a local-time Taylor fit. It is operational plateau evidence, not an all-time theorem.

Numerical time-integration error was negligible at the observed dense/PDE discrepancy scale. Depth and cubature errors were smaller than the principal dense/PDE gap but not always negligible.

## 4. Portability beyond the original dataset

The fixed \(P=5\) PDE was tested without fitting or retuning on 14 preregistered configurations:

- four label changes;
- two new input geometries;
- \(m=2,3,4,5\) samples;
- \(\tanh\), normalized erf, and normalized arctangent;
- two crossed stress cases.

| Full-curve metric | Median | Maximum |
|---|---:|---:|
| All-depth Gram increment | \(1.71\%\) | \(4.14\%\) |
| Output increment | \(1.46\%\) | \(1.83\%\) |
| Loss | \(0.63\%\) | \(1.97\%\) |

All cases had active nonlazy feature learning. The PDE/dense feature-motion ratio stayed between \(0.977\) and \(1.023\), so the match was not obtained by predicting static features.

The cleanest anti-tuning result was label transfer: all four label cases passed the numerical and plateau gates, with maximum Gram/output/loss errors of \(1.56\%/1.47\%/1.41\%\). The alternative activations also remained accurate.

Qualifications:

- the deliberately strong simultaneous 95% certification rule was underpowered;
- six harder cases were not fully PDE-resolution-certified;
- four cases missed both strict plateau windows by \(t=32\);
- this establishes broad descriptive portability, not uniformity over an infinite problem class.

## 5. Linear-explainability hypothesis: first iteration

The first explicit loophole test asked whether residual-depth scaling made the system effectively an identity or deep-linear network.

For the confirmatory nonlinear activation case:

| Comparison | Gram distance |
|---|---:|
| Dense nonlinear versus identity | \(36.38\%\) |
| Matched nonlinear PDE versus dense nonlinear | \(1.09\%\) |
| Identity PDE used on nonlinear target | \(35.37\%\) |

The PDE also tracked activation-specific contrasts, and the nonlinear/identity paths remained \(27.14\%\) apart even after reparameterizing time by loss progress. Therefore the result was not merely an activation-dependent training-clock change.

However, the best fixed initialization-Gaussian gain-matched linear control was only \(3.46\%\) from the nonlinear dense Gram curve. The PDE retained a resolved advantage, but this first experiment could not show that nonlinear dynamics were necessary to achieve the project’s \(5\%\) tolerance.

This was the correct intermediate conclusion:

> Exact identity dynamics were decisively rejected; an effective fixed-gain linear approximation remained viable at \(5\%\).

## 6. Proof-obligation program and what was initially left untested

The first five-hour proof-obligation run mostly built and audited infrastructure. Only two \(P=5\) cubature trajectories completed. Consequently it did not test the proposed chain:

\[
\text{ordered limit}
\to\text{depth homogenization}
\to\text{state sufficiency}
\to\text{Hermite consistency}
\to\text{finite-time stability}
\to\text{all-time stability}.
\]

The only new scientific result was close agreement between two \(P=5\) cubature scrambles:

- normalized output difference \(2.85\times10^{-4}\);
- normalized all-depth Gram difference \(3.35\times10^{-4}\);
- absolute loss difference \(4.80\times10^{-5}\).

The framework’s 128 software tests validated implementation properties, not the seven scientific assumptions. No gate was legitimately counted as passed by that run.

## 7. Lean proof-obligation salvage

A later bounded salvage obtained actual evidence on the main mechanisms.

### 7.1 Ordered width/depth trend

Successive width corrections contracted with ratios \(0.462\)–\(0.518\), and the tested depth correction contracted with ratio \(0.578\). This supports an ordered limiting trend but did not resolve the remaining width/depth tail to the target accuracy.

### 7.2 Trained depth homogenization

Centered trained-depth variance scaled almost exactly as \(L^{-1}\):

\[
\alpha_{\rm forward}=-1.00219,\qquad
\alpha_{\rm backward}=-0.99982.
\]

This strongly supports cancellation of centered fast-depth innovations. It did not identify or prove correctness of the conditional/Onsager mean.

### 7.3 State sufficiency attack

A perturbation invisible to retained \(P\le35\) coordinates and current observables produced only a \(0.332\%\) continuation gap in the strongest tested case. No large projectability counterexample was found. This is one-sided evidence, not a proof that the static label is sufficient.

### 7.4 Stability and late time

Short shadow errors were tiny, and both dense and PDE observable drift collapsed by roughly three orders of magnitude between the \([2,4]\) and \([4,8]\) windows. This supports practical finite-time stability and plateau behavior. Worst-direction amplification, state arclength, and literal \(t\to\infty\) control remained untested.

### 7.5 The provisional Hermite warning

The salvage initially reported larger defects for \(15\leftarrow35\) than for \(5\leftarrow15\), with ratios from \(2.54\) to \(26.53\). A held-out rank-five POD basis also cut the Hermite observable defect roughly in half.

These interpretations were later revised:

- the old successive-shell comparison was invalid because the even shell is exactly inert;
- the POD comparison used five active mixtures against four active linear Hermites plus an inert constant, so it was not an equal-active-rank test.

The POD result still suggests possible basis inefficiency, but it is trajectory-fitted and is not an admissible fixed witness.

## 8. Parity correction and the proper Hermite ladder

For odd activation and symmetric Gaussian initialization, exact sign equivariance implies that even-degree Hermite fields vanish dynamically. Hence

\[
P=5\equiv P=15,\qquad P=35\equiv P=70.
\]

With parity-paired cubature, \(P=5\) and \(P=15\) agreed to \(10^{-17}\) at positive time. The earlier adverse ratios were therefore ratios against numerical symmetry leakage.

On the correct odd-degree ladder:

| Time/seed | Outgoing-tail ratio, degree \(5\) shell / degree \(3\) shell |
|---|---:|
| \(t=0.25\), seed 1 | \(0.0290\) |
| \(t=0.25\), seed 2 | \(0.0320\) |
| \(t=0.50\), seed 1 | \(0.0589\) |

This is a replicated \(17\)–\(34\times\) contraction in the newly outgoing tail.

But aggregate high-to-low state feedback grew by \(38.9\%\)–\(46.1\%\) at \(t=0.25\), and observable-generator defects also grew. The cubic shell has 20 modes while the quintic shell has 56; most RMS-per-mode quantities contracted, but the wider shell prevented aggregate contraction.

Actual observable differences remained extremely small, \(0.0021\%\)–\(0.0079\%\) of the fixed scale. Thus parity repair removed the apparent fundamental obstruction while leaving aggregate tail summability open.

The compiler should henceforth use odd modes only and parity-paired cubature.

## 9. High-to-low tail and degree-seven common-reference test

A common degree-seven reference was used to avoid confounding separately evolved low and high systems.

The results were:

- aggregate state commutator ratio: \(1.3257\);
- observable-generator defect ratio: \(1.6174\);
- shell-adjusted state ratio: \(0.9056\);
- RMS-per-mode ratios: \(0.865\) for \(c\), \(0.865\) for \(\dot c\), \(0.903\) for forward fields, and \(0.965\) for adjoints;
- over \(99.998\%\) of each dominant \(B\)-defect remained in its newly added Hermite shell;
- successive dominant defects had weighted cosine \(4.62\times10^{-4}\).

This ruled against a coherent low-mode resonance or a small number of explosive modes. The higher shell consisted of more, individually weaker, almost orthogonal modes. That favors a bridgeable shell-multiplicity explanation.

Nevertheless, aggregate state and observable defects still grew, and the actual trained degree-seven \(\dot c\) norm was \(1.2665\times\) the degree-five norm. Therefore this round did not establish tail summability.

## 10. Compactness versus flow amplification

The final coupled degree \(3,5,7\) run measured actual outgoing tails, low-state shadows, integrated feedback, propagated quotients, and output/Gram Cauchy gaps.

At \(t=0.25\):

| Metric | Degree \(3\to5\) | Degree \(5\to7\) | Ratio |
|---|---:|---:|---:|
| Projective state error | \(1.3116\times10^{-3}\) | \(1.7338\times10^{-3}\) | \(1.3219\) |
| Output/Gram gap | \(2.1913\times10^{-5}\) | \(3.5846\times10^{-5}\) | \(1.6358\) |
| Feedback commutator | \(7.2584\times10^{-3}\) | \(9.6224\times10^{-3}\) | \(1.3257\) |

The realized final-time shadow quotient changed by a factor \(0.9986\). This found no large amplification change in that one realized direction, but it is a secant quotient, not a uniform propagator bound.

The analytic audit produced two important updates:

1. The frozen shared-transpose term can be represented directly by a bounded Riesz adjoint. Separate Malliavin differentiability is not required merely to define the transpose or prove consistency along a fixed compact trajectory.
2. Energy bounds give uniform finite-time bounds and time equicontinuity, but not Hermite compactness. Plain \(L^2\) local Lipschitzness fails because the adjoint boundary contains an unbounded Gaussian coordinate.

The compact-time pure-Hermite theorem therefore reduces to a tight bundle:

- collective source-Hermite tail compactness or uniform weighted Hermite regularity of reachable trajectories;
- uniqueness and cutoff-uniform forced-flow stability in a suitable weaker/coercive topology.

The experiment localized the observed failure primarily to aggregate tail injection rather than visibly increasing realized amplification, but it did not prove either condition.

## 11. Scalar nonlinear stress and the final effective-linear test

The one-input, one-dimensional reduction made high Hermite degrees cheap while retaining a nontrivial depth- and time-dependent scalar Gram

\[
G(s,t)=\mathbb E[h(s,\theta,t)^2].
\]

The theory-selected activation was

\[
\phi(z)=\frac{\sin(2.5z)}{2.5},
\]

which is smooth, odd, bounded, and 1-Lipschitz. At initialization, \(62.14\%\) of its Gaussian \(L^2\) energy lies outside its best linear Hermite component.

### 11.1 Nonlinear dynamics beyond fixed gain

| Comparison | Gram | Output | Loss |
|---|---:|---:|---:|
| Initialization-gain linear control versus degree-11 sine PDE | \(17.70\%\) | \(7.12\%\) | \(7.51\%\) |
| RMS-gain linear control versus degree-11 sine PDE | \(8.68\%\) | \(3.95\%\) | \(4.68\%\) |
| Paired dense linear versus dense sine | \(15.95\%\) | \(6.55\%\) | \(6.95\%\) |
| Degree-11 sine PDE versus dense sine | \(2.50\%\) | \(2.81\%\) | \(5.54\%\) |

Every paired dense seed had a Gram distance well above \(5\%\). This closes the tested fixed-gain linear explanation for the Gram dynamics. The PDE captured the nonlinear Gram/output evolution substantially more accurately.

### 11.2 Role of higher source Hermites

Strong activation nonlinearity did not make high source-label Hermites important:

- degree 1 versus degree 11 at \(y=2\): \(0.339\%\) Gram difference;
- degree 1 versus degree 13 at \(y=4\): \(0.247\%\);
- degree \(11\to13\) Gram effect in the two resolved \(\tanh\) scrambles: \(0.0046\%\) and \(0.0061\%\).

The top projective-state ratio \(E_{11\to13}/E_{9\to11}\) was \(0.958\) in one well-conditioned scramble and \(1.913\) in the independent scramble. The apparent turnover did not replicate.

The conceptual resolution is:

> Every \(P\) evaluates the full nonlinear activation \(\phi\) and \(\phi'\). \(P\) truncates dependence on the immutable Gaussian neuron label; it is not a Taylor or Hermite truncation of the activation itself.

Therefore a degree-one source closure can capture strongly nonlinear activation dynamics. Activation nonlinearity and source-label complexity are distinct.

## 12. Consolidated status of the major claims

| Claim or mechanism | Current status |
|---|---|
| Literal finite, width-independent PDE construction | Established |
| Exact projected-gradient, transpose, autonomy, and dissipation identities | Established for the finite PDE |
| Accurate \(P=5\) prediction on the canonical benchmark | Strongly supported |
| Portability across tested labels, activations, geometries, and \(m=2\)–5 | Strong descriptive support; uniform certification unresolved |
| Nonlazy feature learning | Established in all tested cases |
| Exact identity/deep-linear explanation | Decisively rejected |
| Tested fixed-gain linear explanation in a strongly nonlinear regime | Decisively rejected for Gram; PDE is substantially more accurate |
| Ordered width/depth limiting trend | Favorable finite-grid evidence; not identified rigorously |
| Centered trained-depth homogenization | Strong \(L^{-1}\) variance evidence; Onsager mean unproved |
| Sufficiency of the static source state | No large counterexample found; unproved |
| Old \(P=5\to15\to35\) noncontraction warning | Retracted as a parity-invalid comparison |
| Corrected outgoing odd-Hermite tail contraction | Strongly supported at the first proper rung |
| Aggregate Hermite Cauchy contraction | Not observed through tested degrees |
| Uniform weighted Hermite regularity/compactness | Unproved |
| Cutoff-uniform forced-flow stability and uniqueness | Unproved |
| Arbitrary-accuracy pure-Hermite convergence | Unresolved |
| Arbitrary-accuracy response-enriched finite PDE | Plausible fallback; not implemented as a width-independent PDE |
| All-time dense-limit identification | Unproved |

## 13. What could still trivialize or downgrade the result?

The simple claim that the PDE only reproduces linear dynamics is no longer credible: the scalar sine case produces a \(15.95\%\) dense linear/nonlinear Gram separation while the PDE is only \(2.50\%\) from the nonlinear dense Gram curve.

The serious surviving alternative is subtler:

> The tested observables may lie on an unusually low-complexity nonlinear manifold in the immutable neuron label, so \(P=5\) is an excellent nonlinear moment closure but not the first member of a systematically convergent pure-Hermite hierarchy.

If true, this would not make the current result trivial. The PDE would remain autonomous, nonlinear, width-independent, nonlazy, and portable across the tested configurations. It would, however, downgrade the broad claim from an arbitrary-accuracy neural-PDE theory to a robust low-order surrogate with a possible irreducible error floor.

## 14. Final open obligations, in priority order

### 14.1 Decisive pure-Hermite gap

Prove or decisively establish that the parity-reduced Galerkin trajectories are collectively compact in a source-mode-coercive weighted space and are uniquely, uniformly stable under cutoff forcing. This is what converts Hermite completeness for each fixed regular field into convergence of the trained flows.

The scalar theory makes the conditional implication explicit: if, for some \(s>0\),

\[
\sup_P\sup_{t\le T}\|Y_P(t)\|_{\mathcal H_\gamma^s}<\infty
\]

and the forced flows are cutoff-uniformly stable in a weaker norm, then Hermite projection tails vanish and compact-time Galerkin convergence follows. What is missing is propagation of that bound through the trained nonlinear forward/adjoint system.

### 14.2 Ordered dense-limit identification

Prove deterministic width convergence at fixed depth and then identify the continuous residual-depth operator PDE, including the correct shared-transpose/Onsager mean after trained-depth homogenization.

### 14.3 Compact time to all time

Use loss dissipation, residual arclength, eventual contraction, or another valid mechanism to upgrade compact-time approximation to uniform control over \(t\ge0\).

### 14.4 Fallback if pure Hermites fail

If the static source label is not closed, introduce a finite, architecture-local set of response/history coordinates. Earlier finite-matrix response hierarchies improved by roughly one to two orders of magnitude per response grade, but they retained dense matrices and therefore remain mechanism evidence rather than the required finite PDE.

## Final assessment

The project has crossed an important threshold:

- it has an explicit and internally consistent finite neural PDE;
- the PDE predicts active nonlinear feature learning rather than merely loss;
- it transfers broadly without case-specific fitting;
- it survives a deliberately nonlinear regime in which fixed-gain linear controls fail badly;
- the most alarming early Hermite “divergence” result was corrected by exact parity;
- higher-shell behavior looks like many individually weaker, nearly orthogonal modes rather than a coherent structural resonance.

But the evidence has not crossed the final convergence threshold:

- aggregate state and observable Cauchy increments have not shown a replicated contracting trend;
- the high-order scalar turnover did not replicate;
- uniform weighted regularity/compactness and cutoff-uniform stability remain assumptions rather than consequences of the dynamics;
- the explicit PDE has not been rigorously identified with the ordered dense limit for all time.

The most defensible closing statement is:

> There is strong evidence for a nontrivial, useful, portable low-order neural PDE that captures genuinely nonlinear dense \(\mu\)P feature-learning dynamics. There is favorable but incomplete mechanism evidence for a bridgeable Hermite hierarchy. Arbitrary-accuracy pure-Hermite convergence, and therefore the full all-time dense-network PDE conjecture, remain unproved.

## Source reports consolidated

This report replaces superseded conclusions while retaining the valid evidence from:

1. `FINAL_DENSE_MUP_PDE_CONJECTURE_REPORT(1).md`
2. `PDE_GENERALIZATION_FINAL_REPORT(3).md` (`(2)` is byte-identical)
3. `ACTIVATION_LINEARITY_SMOKING_GUN_REPORT.md`
4. `PDE_PROOF_OBLIGATION_STUDY_FROZEN_REPORT.md`
5. `PDE_LEAN_SALVAGE_REPORT.md`
6. `PDE_BRIDGEABILITY_RESOLUTION_REPORT.md`
7. `PDE_HIGH_TO_LOW_TAIL_ROUND_REPORT.md`
8. `PDE_FINAL_COMPACTNESS_ROUND_REPORT.md`
9. `SCALAR_HERMITE_MINIMAL_EXPERIMENT_REPORT.md`

Earlier foundational reports are incorporated only where their conclusions survive the later direct-PDE construction and audits. The provisional adverse \(P=5\to15\to35\) interpretation and the stronger separate Malliavin-tail requirement are explicitly superseded by the parity correction and Riesz-adjoint analysis above.

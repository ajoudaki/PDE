# Fixed L=2: current result and unresolved theorem

2026-09-08. **Research stopped at the user's request. The requested unconditional global joint-limit theorem has not been proved or disproved.** The complete saved index and final status are in [PERSISTENT_HANDOFF.md](PERSISTENT_HANDOFF.md). The principal activation remains

\[
\phi(z)=\tfrac34(1+z)+\tfrac14\tanh z.
\]

The original Gaussian initialization, raw training metric, three-input geometry (including singular Grams), and actual finite GF/GD targets have not been weakened. The research objective was not achieved. Do not resume research without a new user instruction.

## Result that passed isolated review

[CAPS_MANUSCRIPT.md](CAPS_MANUSCRIPT.md) gives a self-contained analytic theorem on the specified population Hilbert spaces with the bounded initialized action and genuine adjoint as explicit given hypotheses. It constructs global smooth approximations that cap the entire first-row gradient by one common nonnegative scalar, cap the readout velocity, and retain the true trained-matrix update. They satisfy

\[
E_R(t)+\int_0^t\|\dot\Theta_R(s)\|_{\rm raw}^2ds\le E(0),
\qquad
\|\Theta_R(t)-\Theta(0)\|_{\rm raw}\le\sqrt{tE(0)}
\]

uniformly in the cap. This repairs the loss-dissipation problem of the earlier approximation route.

The same manuscript proves a conditional cap-removal theorem. Write

\[
P_R=(\sum_i r_{R,i}^2 q_{R,i}^2)^{1/2},
\qquad g_{C,R}=\sum_i r_{R,i}\phi(v_{R,i}).
\]

If, for every finite T, constants K_T,c_T>0 give

\[
\sup_{R\ge1,\,t\le T}
\left(\|P_R(t)\mathbf1_{P_R(t)>a}\|_2
+\|g_{C,R}(t)\mathbf1_{|g_{C,R}(t)|>a}\|_2\right)
\le K_Te^{-c_Ta},\qquad a\ge1,
\]

then the approximants converge strongly, uniformly on compact time intervals, to a unique global true population flow with restart from reached states and convergence of its true fields and kernel blocks. The proof derives an Osgood comparison from this premise. **It does not prove the premise.** The actual finite Gaussian GF/GD and velocity/path-law identification remains a further required bridge.

After correcting two omitted addition signs and clarifying the real-cap compactness argument, two new independent reviewers received only the corrected entire manuscript. Both returned PASS with no objections. See [review summary](reviews/REVIEW_SUMMARY.md). Their acceptance concerns exactly the unconditional approximation and conditional continuation statements; it is not acceptance of the requested unconditional global training theorem.

## What the other proof attempts established

The development notes retain useful exact mechanisms and their limitations:

- Source covariance contractions and Gaussian primitive-path bounds control only part of the adapted feedback. An exact same-matrix return survives at order one in a tagged neuron's field.
- Orthogonal inputs admit an exact first-layer coordinate cancellation. Distinct bounded activations then give global population flows in that special geometry. General correlated inputs and the full finite-width bridge remain outside that result.
- Ambient energy bounds do not supply the needed convexity, compactness or one-sided stability. The counterexamples used to test those shortcuts are explicitly not claimed to be reached by physical training.
- Gaussian projection regularizes certain multiplier comparisons, giving a cap-independent Osgood estimate for projected returns. The orthogonal component of `C phi'(v)` remains unclosed and can feed a new Gaussian source with its full L2 variance.

These development statements have not all received the isolated review status of CAPS_MANUSCRIPT. The authoritative claim and dependency ledger is [PROJECT_STATE.md](PROJECT_STATE.md).

## New bounded-activation results

A distinct fixed smooth activation with plateaus `1/2` and `3/2`, and a fixed transition interval `[-1,1]`, gives further exact structure. Its nonlinearity is not made small as input separation decreases. The development proofs establish:

- A positive invariant part of the first-layer feature Gram, including singular input geometry. The first rows in that part remain fixed because their actual derivative gates vanish; their learned matrix columns continue to train.
- A control-independent bound on first-row weight amplitudes. The proof treats rank-two and rank-three input spans separately. Two fresh isolated reviewers passed the corrected complete confinement report with no objections. This certifies the confinement result alone.
- A positive readout-kernel floor on each compact interval for already-constructed paths with the stated canonical causal source realization. The proof retains initialized returns and kills them only on a specifically proved dormant-row event.
- Total boundedness of several bounded observable path laws across existing dissipative approximants. It excludes the raw backward fields, the first-layer kernel, and identification on the common canonical Gaussian space.

The details are in [plateau geometry](development/PLATEAU_GEOMETRY.md), [confinement](development/PLATEAU_CONFINEMENT.md), [causal dynamics](development/PLATEAU_DYNAMICS.md), and [path-law compactness](development/PLATEAU_PATH_COMPACTNESS.md). The confinement reviews are [first](reviews/PLATEAU_CONFINEMENT_FINAL_TWO.md) and [second](reviews/PLATEAU_CONFINEMENT_FINAL_THREE.md); its accepted SHA-256 is `e66b09fd0b115113da658cff6a0e7f3da3ddbc5401360b275546cdacb027b5d3`. The other new notes remain development proofs.

The new route has not removed the decisive gap. A sharper Gaussian chaining estimate improves the dormant-row lower bound to polynomial dependence on the residual clock, but its explicit certificate fails the finite-clock criterion even on orthogonal inputs for this moderate activation. A deleted-row cavity has Gaussian source tails; transferring them to the actual row still requires a missing response estimate. Augmenting the comparison with backward fields introduces further uncontrolled products. These failures concern the specified arguments, and do not disprove the physical global theorem.

For a separate fixed bounded sine activation, [BOUNDED_SINE_PICARD.md](development/BOUNDED_SINE_PICARD.md) shows why taking absolute values of all elementary differentials loses essential cancellations: that majorant has exponentially growing moments even for the actually bounded sine feature. It leaves open a nonlinear iteration that keeps the sine intact. Both legal Gaussian-matrix query families are bounded in this variant, so counterexamples that first use an unbounded probe do not settle its physical source question.

The unresolved mathematical obligation is a property of the actual gradient-selected paths: prove that their returned and unprojected fields cannot develop the concentration that defeats the comparison, or find another strong continuation argument preserving those fields. Failure of the tested general estimates does not falsify this physical-path assertion. No completed proof or physical counterexample is available in this report.

The final completed development round is also saved: [canonical response measures](development/BOUNDED_RESPONSE_MEASURE.md), [bounded legal-query audit](development/LEGAL_QUERY_AUDIT.md), and [sine-preserving approximation and capped cavity bounds](development/SINE_RESUMMED_ITERATION.md). These are partial, unreviewed development reports. They respectively leave an uncontrolled response feedback, a state-dependent multiplier outside a proved semilinear class, and a source scale growing exponentially with the cap. None closes the target. Notes from the interrupted averaging branch are preserved separately as unverified work in progress in [INTERRUPTED_AVERAGING_NOTES.md](development/INTERRUPTED_AVERAGING_NOTES.md).

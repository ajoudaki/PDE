# New task: generalization during nonlinear added-data learning

Work in `/home/amir/Codes/PDE`, the single checkout shared by PDE and PDE-2.
Start a new study, `studies/nonlinear_selection_generalization/`, for milestone B.
This task begins after milestone A is approved and incorporated as C.4.9 of
`docs/global_nonlinear.md`. Verify that dependency first. If absent, report the
missing established input; do not fetch its unpromoted study or reconstruct it
from another task.

Read `AGENTS.md`, the required research workflow, `docs/README.md` including its
philosophy and roadmap, and `docs/NOTATION.md`. Use `solve-math-rigorously` and
`investigate-conjectures`, reading their required instructions yourself. Digest
C.4.9 completely and the complete established proofs it needs; read C.4.5–C.4.8
where relevant, preserving their different horizons and limit orders. Research
inputs are this new study and the established book/code only. Keep source and
review records flat inside the study and generated products under
`data/generated/nonlinear_selection_generalization/`.

**Problem.** Establish a quantitative generalization theorem explaining when
the nonlinear prediction selected during an added-data episode learns an
independently specified regression family from finitely many noisy observations.
The result must connect target structure, approximation error, sampling/noise
and training duration. A positive training-atom gain or a fluctuation theorem
alone does not resolve this problem.

Retain exactly C.4.9's bias-free two-hidden-layer tanh model, ordinary independent
Gaussian initialization with stored variances `(1,1/n,1/n^2)`, mobilities
`(n,1,n)`, readout division by `n`, unhalved squared loss, physical GF, full first
rows and reused middle action with its actual adjoint. Retain the actual finite
Gaussian readout. Every physical run starts from that initialization and uses
its fixed training law throughout.

Let the two known anchors retain their exact reference law
\[
 \nu_*=\tfrac12\delta_{(\sqrt2e_1,1)}
       +\tfrac12\delta_{(\sqrt2e_2,-1)}.
\]
For a fixed label bound \(Y\ge1\), let \(\nu\) be a law on
\(\sqrt2 S^1\times[-Y,Y]\). Draw independent added-data observations
\((X_i,Y_i)\sim\nu\), independent of Gaussian initialization, set
\(\widehat\nu_m=m^{-1}\sum_i\delta_{(X_i,Y_i)}\), and train on
\[
 \widehat\mu_{\varepsilon,m}
       =(1-\varepsilon)\nu_*+\varepsilon\widehat\nu_m.
\]
Here \(m\) counts observations from the added distribution; the anchors are
known and weighted exactly. This is not iid sampling from the entire mixture.
If you also analyze that sampling design, account separately for rare-component
counts and random anchor weights.

Choose, justify and freeze a substantive class of laws \(\nu\) before seeking
a favorable learning conclusion. It must have a nonatomic input distribution
on a fixed set of positive arc length, with declared density/regularity bounds,
and genuinely varying regression-function shape with a meaningful complexity
parameter. Its support must not shrink with width, sample size or contamination,
or be chosen merely to inherit the one-atom gain by continuity. Define the class
without using the trained network's answer. Respect the model's oddness and
anchor constraints, or account explicitly for their approximation cost. You
may choose an appropriate basis or another description; no particular one or
proof route is prescribed.

Write \(Y=q(X)+\xi\), with \(\mathbb E[\xi\mid X]=0\), bounded labels and
specified noise bounds. The test input is an independent draw from \(\nu_X\),
and the target error is
\[
 \mathcal E_\nu(f)=\|f-q\|_{L^2(\nu_X)}^2
                 =R_\nu(f)-\mathbb E\xi^2.
\]
Retain whole-circle prediction as an observable; any risk claim concerns its
declared test distribution.

Resolve the following connected obligations as one theorem package:

1. Construct and identify the nonlinear selection for the population and
   empirical added laws on an admitted nonzero slow-time episode. Prove the
   continuation and original-mixture capture needed at \(t=\tau/\varepsilon\).
   Every extension beyond C.4.9's one-atom theorem must be justified.
2. Give an explicit target-approximation, contraction or oracle inequality for
   the population selection. Its dependence on target complexity, mode content
   or regularity must explain what is learned during the episode. Bound all
   terms using declared class parameters and proved reference quantities;
   do not define the approximation term to be the unknown trained risk.
3. Give quantitative finite-sample control with specified probability or
   expectation, separating input sampling and centered label noise. Combine
   it with the approximation bound and a justified stopping time chosen from
   available information. Exhibit a nonempty regime with strict unseen-risk
   improvement over the fitted reference, uniform on a robust task subfamily
   and nonvanishing as contamination and inverse width vanish. Explain how the
   guarantee improves with data or training effort and its approximation floor.
4. Transfer these claims to actual finite GF with explicit limit order and
   probabilities over samples and initialization. Width first at each fixed
   sample and positive \(\varepsilon\), then \(\varepsilon\downarrow0\), then
   increasing sample size is admissible if justified. No simultaneous rate or
   raw-GD extension is required. Preserve nonvanishing paired second-hidden
   activation displacement on a robust subfamily at the learning scale,
   comparing mixture and reference flows on the same initial arrays at the
   same physical time, as in C.4.9.

A quantitative finite-episode learning theorem can complete this target with
an explicit approximation floor; universal consistency or an all-time endpoint
theorem is not required. A thickened-atom witness, unspecified continuity bound,
initial derivative, or restatement of the time-40 sampling theorem is insufficient.
Keep the hidden dynamics nonlinear and evolving. In particular, finite-list
Gram positivity does not prove continuum coercivity, and the existing time-40
sampling result does not automatically apply on the new learning horizon.

Work toward full resolution while allowing diverse approaches. Use fresh
`fork_turns="none"` agents with explicit allowed inputs: prompt-only or selected
established material for creative attempts, and complete frozen inputs for
adversarial review. Do not expose independent attempts to each other's route
before comparison. Separate a failed approach from a false target; if progress
stalls, identify the precise missing estimate and compare genuinely different
routes rather than repeatedly polishing one conditional argument. Follow the
roadmap's conditional GF/GD reassessment only if a persistent specific obstacle
and a concrete benefit justify it; do not silently change the target.

No training experiments or broad computational campaign are authorized. Run
appropriate deterministic checks. Preserve concurrent work, coordinate the
shared Git writer lock and make scoped study commits. If successful, prepare
the smallest self-contained canonical addition, complete the independent
relevance, paired scientific and separate integration reviews, and present the
concrete package for user approval before established files change. If a genuine
gap remains, retain the precise partial results and obstruction; do not label
the milestone complete.

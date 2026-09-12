# Independent assessment: the next target after milestone A

Assessment date: 2026-09-12. This is a strategy assessment, not a scientific
review verdict or a proof of the proposed next theorem. The candidate A is
unpromoted throughout this assessment.

## Input and action scope

I read `docs/README.md`, `docs/NOTATION.md`, and this study's
`CANONICAL_ADDITION_v3.md` completely. In `docs/global_nonlinear.md` I read
C.4.8's model and theorem, and the beginning of C.4.8.1 through its displayed
source derivative recursions (lines 11440–11785 as read). The C.4.8 theorem
statement is the only established sampling conclusion used below. No other
study, study history, review, chat, Git history, code or generated data was
consulted. I read the required investigate-conjectures and
solve-math-rigorously skills, including research-contract and adversarial-audit
instructions. No theorem search, experiment or implementation was performed.

## Recommendation

If A passes its separate complete reviews and promotion decision, make B the
next principal mathematical target. Aim for a **finite-episode regression
theorem on a genuinely distributed, externally specified task family**, with a
teacher approximation bound, quantitative sampling and noise control, and a
justified stopping time. Its behavior should vary meaningfully with task
complexity. This can satisfy the roadmap's B without proving universal
consistency, a global changed-law endpoint, or arbitrarily long slow-time
continuation.

A fixed positive risk gain for a narrow thickening of A's added atom would be
useful intermediate progress but insufficient as the whole next milestone.
The risk guarantee must explain approximation to an independently defined
regression target and improve with information or training effort in a stated
regime. Conversely, demanding consistency for every smooth teacher would add a
major obligation absent from the stated roadmap.

C remains independently valuable, but A gives no concrete compression theorem
that makes C the higher-leverage next step. Its projected equation retains the
entire trained Gaussian action state and its reference history. A two-by-two
projection inverse does not make the rest of that state cheaply computable.
Promoting A would establish a useful determining description at its stated
scope, not an independent finite simulator.

## What A actually contributes

The principal extension mechanism is the source tube measured by accumulated
absolute control mass. Proof unit A is stated for arbitrary finite training
direction lists and uses weighted sums rather than a minimum atom weight. The
long physical horizon is controlled because the reference residual contracts
while the additional force is weighted by epsilon. This is much more relevant
to B than simply having another local derivative at time 40.

For the one-atom law, proof unit C constructs the constrained strong evolution
with the original Gaussian carrier and continued source history, and derives
the slow clock from an exact residual identity. Its anchor projection is
recomputed from current gradients. Proof unit D supplies a width-first bridge
at each separately fixed positive epsilon. Those are substantial ingredients
for a distributed-law extension, but the extension remains to be proved.

The endpoint argument in proof unit B establishes independence for each finite
list of distinct, nonantipodal inputs, including a nonzero middle-gradient
component after anchor projection. This is useful geometry. It is **not** an
integral coercivity estimate over all residual functions on an interval, nor
a quantitative learning rate as task complexity increases.

The present theorem selects one finite nonzero episode and gains risk at one
repeated training atom. Whole-circle reconstruction makes test prediction
available as an observable; it does not make that prediction approximate an
external regression function. C.4.8's influence theorem and mean-square
remainder hold at physical time 40. They cannot be substituted at
`t = tau/epsilon` without new estimates for that regime.

## A concrete, non-vacuous B contract

The following is an admissible target specification, not a compulsory choice
of basis or proof. An equally substantive family and guarantee would serve.

Retain A's exact two-hidden-tanh architecture, ordinary Gaussian initialization,
nonzero actual finite readout, mobilities, unhalved loss and GF. Train from the
original initialization on

\[
 \mu_{\epsilon,m}=(1-\epsilon)\nu_*+\epsilon\nu_m,
 \qquad \nu_m=m^{-1}\sum_{i=1}^m\delta_{(\sqrt2u_{\alpha_i},Y_i)}.
\]

Here the anchor law is known and retained exactly. The sample consists of
independent observations from the added task law. Thus this first contract
does not also require analysis of random anchor counts in an iid sample from
the entire mixture. The two sampling designs must not be conflated.

Use a fixed input arc of positive length independent of all accuracy, sample,
width and contamination parameters, for example
`I = [pi/6, pi/3]`. Admit design densities bounded above and below by specified
positive multiples of normalized arc length. This is a continuum of
nonorthogonal inputs, not a support radius chosen to inherit the atom theorem.
Let

\[
 Y_i=h(\alpha_i)+\xi_i,
 \qquad \mathbb E[\xi_i\mid\alpha_i]=0,
 \quad |\xi_i|\le b,\quad
 \mathbb E[\xi_i^2\mid\alpha_i]\le\sigma^2,
\]

with an explicit uniform bound ensuring labels remain in `[-Y,Y]`.
Risk on this law decomposes as

\[
 R_\nu(f)=\|f-h\|_{L^2(\nu_X)}^2+\mathbb E\xi^2.
\]

The regression function must be specified independently of the trained
network. One natural class is bounded odd trigonometric polynomials with
anchor values `h(0)=1`, `h(pi/2)=-1`, with a degree or smoothness parameter.
For example, independent coordinates can be built from

\[
 h(\alpha)=\cos\alpha-\sin\alpha+
 \sum_{k=0}^{q-1}b_k\sin(2\alpha)
             \cos((2k+1)(\alpha-\pi/4)).
\]

The displayed corrections vanish at both anchors and are odd under the
antipodal transformation. Bounded coefficient sets, and if useful a fixed
positive midpoint signal with controlled higher modes, define the class
without referencing `F_*`, a network trajectory, or a fitted answer. The
coefficient restrictions, degree range and target accuracy regime must be
frozen before proving a favorable learning assertion. Polynomial teachers
are a suggestion, not a result about what this network already learns.

For the corresponding population added law, construct the distributed version
of A's selected evolution and its prediction `P_nu(tau)`. The central result
should give a finite-episode approximation or oracle bound of the schematic
form

\[
 \|P_\nu(\tau)-h\|_{L^2(\nu_X)}^2
 \le {\cal B}(\tau;q,R)+{\cal A}_q(h),
 \qquad 0<\tau\le\tau_{\rm adm}(q,R).
\]

Here `q,R` describe declared target complexity and regularity. The term
`A_q(h)` is an explicit task approximation remainder when teachers outside a
finite-degree class are admitted; it can be zero for the initial exact-class
theorem. The bias term `B` must be bounded from declared task data and proved
reference quantities, not defined as the unknown risk of `P_nu`. A relative
contraction bound against the known reference error is also admissible if it
quantifies the contraction and its complexity dependence. A single fixed
small degree can be the first proved case, but the contract should expose
what changes with degree, smoothness, or mode content rather than append an
irrelevant complexity symbol to its constants.

For the selected evolution trained on the empirical law, require a
high-probability bound of the form

\[
 \|P_{\nu_m}(\widehat\tau)-h\|_{L^2(\nu_X)}
 \le \sqrt{{\cal B}(\widehat\tau;q,R)+{\cal A}_q(h)}
       +{\cal S}(m,\sigma,b,\delta,\widehat\tau,q,R).
\]

Specify and prove the statistical term: it must vanish as information grows
in the stated regime, distinguish input sampling from centered label noise,
and have useful dependence on time and complexity. A generic CLT or existence
of an unspecified continuity modulus alone is insufficient. A deterministic
stopping time chosen from class bounds, sample size and confidence is enough;
an implementable validation-based alternative would require its own proof.
No unknown population risk minimizer can silently serve as the stopping rule.
There should be a nonempty parameter regime in which the combined bound is
strictly better than the reference predictor by a fixed positive margin on
the added test distribution. State any irreducible approximation floor.

The population estimate, empirical estimate, stopping justification and
finite-network bridge are the deliverables of one B theorem. Re-establish
hidden adaptation on a robust subfamily with a directly paired observation;
moving parameters alone should not replace A's hidden-activation criterion.
Whole-circle prediction reconstruction remains an observable, while the
teacher error is measured on the stated test distribution. Claiming teacher
approximation on unsampled portions of the entire circle would require an
additional assumption and argument.

## Limit order and finite-network obligation

A conservative first contract is: for each separately fixed sample size,
realized training sample, admissible stopping time and positive epsilon, take
width to infinity at the finite physical horizon `T = tau/epsilon`; then
take epsilon to zero; then let sample size grow in the proved regression
bound. Probabilities include independent training samples and initialization.
Passing a conditional finite-width statement through the sample law also
needs its measurability and integration argument.

One may prove a different order or uniform estimates if useful, but should not
promise simultaneous width/sample/contamination rates from A. Likewise no
raw-GD conclusion follows here. If a stopped time varies with the sample,
the population empirical bound and finite-GF capture must cover that choice,
for example uniformly over a declared compact slow-time interval. For each
fixed sample the width limit is still taken before that physical horizon is
allowed to diverge through epsilon.

## Plausible leverage and genuine gaps

1. **Distributed construction and singular limit.** Replace the added atomic
   force by its integral, preserve the two-anchor projection and the full
   retained Gaussian action, and prove uniform source control through finite
   approximations of the law. A's control-mass estimates are well matched to
   this obligation. Independence of constants from the number of directions,
   source construction for the limiting law and its original-mixture capture
   must all be verified, not inferred by replacing a sum symbol by an integral.

2. **Teacher approximation is the new central bottleneck.** The relevant
   projected prediction operator at a state has kernel
   `K_theta(u,v) = <Pi_theta g_theta(u), Pi_theta g_theta(v)>`. Its action on
   the actual teacher residual, with features and projector moving, determines
   progress. A viable local route might establish quantitative observability
   on a restricted finite-dimensional endpoint residual family generated by
   `F_*` and the teacher modes, and control its distortion over the finite
   episode. Other routes may be better. Neither finite-list positive
   definiteness nor a formal frozen-kernel evolution proves this estimate.
   The residual leaves the initial finite-dimensional family under nonlinear
   training, so that leakage must be controlled if this route is chosen.

3. **Sampling at the correct learning scale.** A's one-reference comparison
   and accumulated-force bounds suggest stability against empirical force
   errors on bounded slow time. Quantitative concentration along an actual
   population path may suffice; an influence CLT is not essential to B.
   Prove the source-error estimate as well as its propagation. The physical
   time-40 statistical theorem does not settle either assertion at this scale.

4. **Stopping is substantive.** More training can reduce approximation error
   while amplifying empirical deviations or exhausting the proven source
   tube. A nonempty useful interval and a certified choice within it suffice.
   Reaching arbitrary precision by sending slow time to infinity is a stronger
   continuation/optimization campaign and should not be made an implicit
   prerequisite for this finite-episode B.

A proves neither integral coercivity nor a uniform spectral gap on all
`L2` residuals. On a continuum, a regular bounded kernel may have arbitrarily
small spectral values even when every finite Gram is strictly positive.
Complexity-dependent approximation is therefore the honest target. A
restricted-family theorem with a stated bias floor can complete the roadmap's
B if its actual approximation, information and stopping guarantees are
substantive; gain alone plus a sampling limit cannot.

## Why C is not automatically next

A's source cap controls the sum of response magnitudes and passive query
tails. It does not establish decay of response-history modes, compressibility
of the covariance structure, or a representation with bounded total numerical
cost. C would need an independently evolving finite causal approximation,
computable coefficients and initialization, controlled forward and adjoint
reuse, reconstruction and restartability, and an error/resource theorem.
Those are major unsolved obligations in the scoped input. A's long-time
control variable could help later, but it is not such a construction.

If a concrete representation supplies a verified compression mechanism, C
may deserve parallel priority. That decision should follow the proposed
representation and its decisive estimate, not the attractiveness of having a
solver or the small size of the anchor projection. B currently has a clearer
connection from A's new structure to the project's generalization question.

## Concise proposed task prompt

After A is promoted, investigate B for the same nonlinear GF: establish a
quantitative finite-episode generalization theorem for an independently
specified, non-atomic correlated regression family with bounded centered
noise. Seek a teacher approximation or oracle bound with meaningful task
complexity dependence, vanishing sampling error, and a justified stopping
time, retaining actual hidden adaptation and the original-initialization
finite-GF bridge with explicit limit order. Use A's selection and accumulated
control structure where valid; prove the continuum and learning-scale
statistical extensions needed. Do not substitute atom thickening, a
network-defined teacher, a frozen-feature model, or the time-40 CLT. A useful
finite-episode bound may have an explicit approximation floor; universal
consistency and all-time continuation are stronger optional targets. Choose
and freeze the sharp task family and success criterion before proof search.

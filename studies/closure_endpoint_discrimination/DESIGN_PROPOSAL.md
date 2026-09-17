# Distinguishing closure orders by their settled circle predictions

Initially design only, requested on 2026-09-14. The user has now authorized a
progressive numerical search from simple to more complex targets. The active
execution contract is [CAMPAIGN_PLAN.md](CAMPAIGN_PLAN.md), frozen before runs;
it supersedes the design-only restrictions and single-law protocol below.
No numerical experiment has yet been executed at this preparation checkpoint.
The task is to choose a training law that plausibly separates the final radial
outputs of the maintained N=1,3,5 closures while retaining nonlinear feature
learning. This is a new study, using only established docs/code and its own
reasoning. No other study's results, arrays or implementation are inputs.

## Proposed training law

Keep the bias-free, two-hidden-layer tanh model and its small Gaussian readout,
unhalved mean squared loss and physical mobilities (n,1,n). Let
u(theta)=(cos(theta),sin(theta)); physical network inputs are x=sqrt(2)u.

Use 24 equally weighted inputs. In degrees, define six cluster centers

    c = (15, 35, 50, 75, 100, 170)
    offsets = (-4, -4/3, 4/3, 4)
    theta[j,k] = c[j] + offsets[k].

Assign bounded real regression labels from the fixed, globally defined function

    y_star(theta) = 0.40 cos(3(theta - 17 degrees))
                  +0.35 sin(5(theta - 17 degrees))
                  +0.25 cos(7(theta + 11 degrees)).

Convert every angle and phase to radians before numerical evaluation. The
weights sum to one, so |y_star|<=1. All frequencies are odd, hence
y_star(theta+pi)=-y_star(theta), compatible with the model's exact oddness.
There are no antipodal training pairs and no contradictory duplicate inputs.
The labels have a fixed, nonvanishing scale; there is no small-amplitude limit.

The principal evaluation region is

    G = (104,166) degrees union (284,346) degrees.

It contains no training direction or direction antipodal to a training point.
Its two components each have width 62 degrees and are centered at oblique
directions 135 and 315 degrees. Antipodal predictions are redundant by oddness,
so the two components should not be counted as independent evidence.
Retain the whole circle as a secondary evaluation domain. Labels outside the
training support are used only to assess this declared synthetic target, never
to train any model or choose coefficients after seeing the outputs.

## Why this design addresses the actual order distinction

The maintained dictionary retains products of Chebyshev polynomials of total
degree at most N in four bounded first-population initialization marks and two
bounded second-population marks. The first four marks include tanh(g1), tanh(g2)
and bounded reverse-action coordinates; the second two are bounded initial
forward-action coordinates. The current hidden fields and readout evolve
nonlinearly at every order. Actual retained dimensions are (5,3), (35,10),
(128,21); N=5 includes two redundant constant tail words beyond its 126 lower
polynomial features. The positive ridge also changes with N. Thus the proposed
comparison is between the complete maintained schemes, not basis degree alone.

Oblique inputs directly exercise the extra mixed polynomial directions. With
X=tanh(g1), Y=tanh(g2), a=cos(theta), b=sin(theta), the initial first hidden
activation is exactly

    F_theta(X,Y) = tanh(a artanh(X) + b artanh(Y)).

Around (X,Y)=(0,0), substitution of artanh(z)=z+z^3/3+O(z^5) into
tanh(z)=z-z^3/3+O(z^5) gives

    F_theta = aX+bY + (a-a^3)X^3/3 + (b-b^3)Y^3/3
              -a^2 b X^2 Y - a b^2 X Y^2 + O((|X|+|Y|)^5).

The mixed cubic terms are explicit retained polynomial directions at N=3 and
are absent from the N=1 polynomial span. Fifth-degree mixed directions enter
at N=5. At coordinate axes this particular activation reduces exactly to
plus or minus X or Y. Clusters near 35 and 50 degrees exercise mixed-coordinate
dependence; the unseen arc probes how the learned map extends toward 135 degrees.
This local expansion motivates the geometry. It is not a global approximation
bound, a replacement of tanh in the simulation, or a proof of endpoint separation.

In particular, N is NOT an angular Fourier cutoff: even N=1 can produce high
angular harmonics through its full tanh and moving fields. The target's third,
fifth and seventh harmonics create several interacting angular scales; their
indices are not claimed to match exact representability thresholds. Varying
real labels, unequal center spacings and unequal phases reduce the constraints
imposed by simple binary or rotationally symmetric targets. The wide missing
arc leaves room for different extensions even if all models fit their labels.
Adding dense full-circle supervision could instead force the outputs to agree.

## Hypothesis and interpretation

The hypothesis is that the larger mixed-feature dictionaries select visibly
different settled extensions across G, with some higher-order predictions
closer to a wide actual network. Either ordering is possible; monotone benefit
with N is not assumed. Separation among closures and agreement with the network
are separate metrics. Error against y_star is a third, distinct question.

The strongest alternatives are common endpoint selection despite different
hidden states, unequal progress along similar trajectories, numerical
integration error, and differences caused by training-fit quality rather than
off-support selection. The proposed comparison measures all of these explicitly.
Agreement would disfavor this particular design as a separator; it would not
prove that all orders always share the same endpoint. Separation would not prove
convergence of the hierarchy. Finite quadrature remains a separate approximation
axis and cannot be confused with closure order.

## Proposed bounded protocol, conditional on later execution authorization

Before execution, freeze the implementation and exact command/source/input hashes.
Main network: width 8192, seeds 11,29,47, float32 with TF32 disabled. Main closures:
N=1,3,5 with Q=4096 initialization and P=2048 population nodes. Integration
controls repeat each order at Q=8192,P=4096. These are comparison resolutions,
not certified sufficient values; no outcome-dependent enlargement is allowed.
Use the standard initializer and no fitted time rescaling or trajectory input.

Use simultaneous Heun with h=.01, retaining a 1440-angle passive output panel,
training predictions/loss and paired hidden motion. Additional fixed controls:
width 4096 seed11 in float32 and float64; width8192 seed11 with h=.005; N=3 and
N=5 at the main integration resolution with h=.005. Maximum 14 trajectories,
at most two simultaneous network and two closure workers. This is a proposed
maximum menu, not authority to launch it now.

First observe T=100, then extend in common 25-unit blocks, at most to T=300.
Require, for every main realization/order and both integration resolutions,
maximum whole-circle output drift <.005 over each of the last two 25-unit
blocks and absolute loss change <.0005 on those blocks. Then stop at a common
checkpoint and compare the radial functions. A plateau is a finite diagnostic,
not a proof of an infinite-time limit. If the cap is reached without this
criterion, call the endpoint question unresolved; never present an unfinished
trajectory as a settled endpoint. A radial plot at a fixed T alone does not
remove learning-speed effects.

Stop at 15 minutes total scientific wall time, 600 seconds per worker, 6 GiB of
generated outputs or less than 3 GiB free disk, whichever occurs first. Retain
partial results and do not search for a different label pattern, phase, seed,
order or horizon after seeing outcomes. Final-state plotting/verification has
a separate two-minute limit and performs no additional training.

For radial functions rho_N(theta)=R+f_N(theta), use common R=2 when every radius
is positive; otherwise set R=1+max|f| across compared curves and label it. Do not
rescale amplitudes or rotate curves separately. Show the full radial overlay,
the gap shaded as unsupervised, output-versus-angle and a radial difference plot.

Primary discrimination is gap RMS distance

    D_N,M = sqrt(mean_G (f_N - f_M)^2)

for (N,M)=(1,3),(3,5), with uniform angular weighting. Also report full-circle
distances, maximum displacement in G and gap error against the network mean.
Predeclared visible pairwise separation: D_N,M>=.075 AND maximum gap displacement
>=.15. Both adjacent pairs must qualify to call all three orders distinguished.
If D_N,M<.025 and maximum displacement<.05, call that pair practically coincident;
between thresholds is inconclusive. Require every claimed separation to exceed
five times the largest corresponding width/seed, resolution, step or remaining
drift discrepancy. Failure of that gate makes the interpretation unresolved.

Numerical checks must verify the exact equations, initialization, full-state
restart, oddness, input geometry and exclusion of passive labels from training.
For endpoint numerical adequacy require controls to change dense output by
<.01 in maximum norm and training loss by <.001, as well as the five-times margin.
Report time evolution separately if these gates fail transiently. For an
off-support selection claim additionally require all compared training losses
<.005 and training prediction differences <.02 RMS. A settled model with poor
training fit is a distinct approximation failure; an unsettled model is a speed
or convergence ambiguity. Neither should be relabeled as pure off-support bias.
Report paired hidden motion to check that the intended feature-learning regime
has actually been exercised; a nearly frozen run has weaker mechanistic force.

## Sources, checks and scope

Established inputs: docs/NOTATION.md, docs/README.md, code/README.md and complete
code/pde/observable_initialization.py, observable_words.py and observable_solver.py.
Source version inspected: Git HEAD 04b61a12795734cbfc93830bf0a164bab7d101c4.
No claims about another study's results are inputs to this design.

Root synthesized the concrete 24-point law and checked the local cubic expansion.
Fresh scoped agent closure_order_design inspected the maintained initialization
and evolution code and proposed the mixed-feature mechanism; fresh prompt-only
agent endpoint_design_audit examined endpoint identifiability and gap/symmetry
confounds without seeing that route. Their alternative parameter lists were not
executed or searched; the fixed candidate above is the sole selected proposal.
Required investigate-conjectures design/contract guidance was applied.

Status: proposed, untested endpoint-separation hypothesis. The local algebra and
dictionary description have been checked against the established code; no
empirical superiority, equilibrium result or promotion is claimed. All files
remain flat in this study. Future generated products belong only under
data/generated/closure_endpoint_discrimination/. The current user request for
a concrete design is fulfilled; scientific execution awaits a later request.

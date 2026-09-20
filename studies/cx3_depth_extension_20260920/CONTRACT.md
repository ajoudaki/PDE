# C-X3: faithful depth extension of C-H3 and C-H4

Author contract, 2026-09-20. This specifies research to be proved; it is not
a completed depth theorem or promotion proposal. The first complete target
is three hidden layers. The desired strengthening is the identical contract
for every separately fixed finite hidden depth. Partial results retain their
own scope and do not discharge an unproved substantial-training clause.

## 1. What the maintained results require

The baseline is `docs/global_nonlinear.md`, C.4.7.10, read in full, together
with the fixed-depth C.1-C.3 foundation and the opposite-label reference
C.4.5.1. Source locations refer to HEAD
`bcee9782651c34ae1204d37186e5c57e9282b273`.

| Obligation | Maintained source | Consequence for this contract |
|---|---|---|
| Broad target-flow domain | C-H3 A.1, lines 12594-12627 | Every Borel circle law with labels in [-1,1]; no exclusion of repeated, parallel, antiparallel or singular-Gram data for existence. |
| Nonlazy finite-data scope | C.3, lines 3441-3835 | Pairwise nonparallel normalized inputs, positive weights and nonzero labels belong to the strict-activity assertion, not the existence assertion. C.3 itself has two hidden layers. |
| Represented short-time numerics | C-H3 A.1/B/C, lines 12629-14245 | Preserve the full rational two-arc family, including atomic and nonatomic laws with cross-component correlations in [2/5,4/5]. |
| Substantial training | C-H4 D.1-D.3, lines 14246-15528 | Preserve a positive supported neighborhood with equal binary-label masses, atoms and nonatomic laws, risk <=1/4 from initial risk one, and early paired motion. |
| Approximation and implementation | C-H3 C and C-H4 D.3-D.5 | Same population target, whole-input prediction, paired joint observations, own-state restart, separate numerical/order limits and actual finite implementation with accounted costs. |
| Actual training algorithm | C.1, C.4.3, C.4.5 and C-H3/H4 | Distinguish finite GF, actual simultaneous raw GD, and the numerical integrator of the closure. Their conclusions and step restrictions differ. |

C-H3 fixes physical time 1/200. C-H4 fixes physical time 40 and its own
positive radius. At greater depth, new positive onset times, fitting times,
activity margins and radii may depend on depth. Keeping the literal numbers
1/200, 40 or 10^-13 at every depth is not required. Replacing a positive
fixed radius by one tending to zero with width or approximation order is
not allowed.

At L=2 retain the maintained C-H3 interval 1/200 and C-H4 time-40 family,
margins and scope. The depth extension must recover those statements; the
new constants at L>=3 do not rewrite the established two-layer results.

C-H4's perturbed-law statement is through a fixed finite learning horizon.
It is not an all-time perturbed-law theorem. Its orthogonal reference has
the separate global and endpoint results of C.4.5.1.

## 2. Exact model, common to both branches

Fix the hidden depth L, initially L=3. Use tanh in **every** hidden layer,
no biases, common width n, and normalized inputs u=x/sqrt(d) in S^(d-1):

    z1=W1 u,                 h1=tanh(z1),
    zell=Well h(ell-1),      hell=tanh(zell),   2<=ell<=L,
    f_n(u)=c^T hL/n.

All stored entries are independent centered Gaussians at initialization:
first weights have variance 1, every hidden matrix variance 1/n, and the
stored readout variance 1/n^2. Mobilities are (n,1,...,1,n). Train every
block under the unhalved probability-weighted squared loss

    L_mu = integral (f(u)-y)^2 dmu(u,y).

For finite data the positive weights sum to one. Time is physical training
time. Raw GD updates all stored blocks simultaneously from the old state,
with linearly interpolated raw parameters and recomputed hidden fields.
The actual finite random readout is retained; only its population limit
is initially zero. No depth-dependent rescaling of tanh or initialization
is inserted to keep a uniform signal size.

Data laws in the theorem statements are laws of physical inputs (x,y).
In equations written with (u,y), integration is against their pushforward
under u=x/sqrt(d); predictions f(u) abbreviate the prediction at x=sqrt(d)u.
Distances to axes always concern normalized directions. This convention
applies also to the reference and represented circle laws below.

At population level retain the full first-row field w in L2(Omega1;R^d),
the readout c in L2(OmegaL), and L-1 distinct initialized Gaussian actions

    Aell=Aell,0+Kell : L2(Omega(ell-1)) -> L2(Omegaell), 2<=ell<=L.

Each action and its actual adjoint must have their common canonical
realization. Different matrices are independently initialized, but their
reused answers during training are not fresh independent Gaussian calls.
Only each learned increment Kell is Hilbert-Schmidt. The raw squared metric
is the sum of the full-row L2, all increment HS, and readout L2 squares.

For a passive input define H1=tanh(w.u), Zell=Aell H(ell-1),
Hell=tanh(Zell), f=E_L[c HL], and

    DeltaL=c tanh'(ZL),
    Pell=A(ell+1)* Delta(ell+1),
    Deltaell=tanh'(Zell) Pell,                    ell=L-1,...,1.

The target equations, with r=f-y, are

    w'    = -2 integral r Delta1 u dmu,
    Kell' = -2 integral r Deltaell tensor H(ell-1) dmu, 2<=ell<=L,
    c'    = -2 integral r HL dmu.

Here (a tensor b)v=a E[bv], with the expectation on b's population.
Writing these equations is not an existence, uniqueness or finite-network
identification theorem.

## 3. Broad-data positive-time branch

For L=3, and subsequently every separately fixed L>=3, prove:

1. For every Borel law on sqrt(2)S1 x [-1,1], there is a canonical strong
   autonomous population solution on one common [0,T_L^on], T_L^on>0.
   The interval is independent of that law, sample count, atom masses,
   covariance rank, width and numerical resolution. Prove uniqueness in
   the specified raw class, law continuity and unique reached-state
   restart under the same training law for the remaining asserted interval.
   Preserve the actual action/adjoint structure and HS increments.
2. Preserve the broad finite-data setting as well: every separately fixed
   d,m, normalized input list and bounded label list, with arbitrary
   positive probability weights. Coincident inputs and singular Grams do
   not invalidate the existence statement. On a positive common interval
   for the stated bounds, retain the full first row and whole-sphere
   prediction. No growing-dimension theorem is required.
3. For finite normalized datasets with |u_a.u_b|<1 for a!=b and all labels
   nonzero, prove actual early paired activation motion and nonaffinity in
   **every** hidden layer. The activity time/margins may depend on the fixed
   data and depth. Seek the faithful onset statement: nonzero order-t^2
   activation displacement (squared size order t^4) and order-t RMS speed
   at each input/layer. This is a new depth obligation, not an automatic
   invocation of the two-layer C.3. For arbitrary Borel laws, give a
   nontrivial open nonlazy subfamily, including represented nonatomic
   members, rather than claiming universal motion for stationary laws.
4. Identify the target with actual finite GF and simultaneous raw GD for
   every eta_n->0 on this onset interval. Preserve joint second-moment
   observations, predictions uniformly in time and input, and the local
   fixed-data path observations of the maintained C.1 theorem. For the
   circle-law assertion, also prove deterministic data-law and independent
   empirical-sampling limits without a relative sample/width restriction.
5. Construct a determining current observable hierarchy, autonomous finite
   closures, and a reusable numerical implementation converging to this
   same target. Include every finite represented dataset and the entire
   original C-H3 rational two-arc family. Arbitrary Borel integration is
   not supplied as a numerical oracle; mathematical all-Borel existence
   and executable represented-law scope are stated separately.

Thus broad finite-data coverage is not restricted to near-orthogonal data,
two samples, linearly independent input lists, or m<=d. Full higher-dimensional
Borel-law coverage would be an additional strengthening; the required Borel
scope already preserves the complete original circle statement.

## 4. Fixed positive neighborhood through substantial training

Retain the original two-axis geometry in dimension two, independently of
the wider finite-data onset branch. For each admitted depth prove positive
constants rho_L, a_L and finite times 0<t_L^act<=T_L^fit, fixed before width,
sample and approximation limits, with the following conclusions.

The reference is

    nu_* = (1/2) delta_(sqrt(2)e1,+1)
         + (1/2) delta_(sqrt(2)e2,-1).

The admitted target class contains **every** Borel law with half its mass at
each binary label and support within rho_L of the matching normalized axis.
In particular it contains equal-weight perturbed pairs, genuinely nonorthogonal
pairs and supported nonatomic laws. Supply an explicit, finite description
of a positive supported radius and a represented rational-endpoint arc
subfamily, with a convergent input quadrature staying inside the domain.
A nonnumerically-optimized constructive radius is acceptable; a trajectory
oracle or a radius chosen after the approximation limit is not.

For every separately fixed law in this class require:

- The same canonical strong solution, uniqueness and reached-state restart
  under the same law through the entire [0,T_L^fit], with actual finite-network
  capture. No arbitrary ambient-state or switched-law restart is implied.
- Initial population loss one and final loss strictly below 1/4, with
  enough proved slack to transfer loss <=1/4 to actual finite networks
  with probability tending to one. T_L^fit must be justified from a
  fitting estimate, not chosen because a numerical curve appears low.
- At t_L^act, training-averaged squared initial/current activation motion
  at least a_L>0 in every layer, using the same population rows and input.
  Establish visited-law nonaffinity on a stated positive early interval.
  No margin uniform over all depths or at the final fitting time is required.
- The **same closure construction and numerical realization** as in the
  onset branch, with its full convergence proof carried through T_L^fit.
  Continue its own approximate state across the whole interval. Exact
  intermediate target states and resets of approximation error are not inputs.
- Actual finite GF capture for whole-circle prediction and the declared
  paired/joint observations, including deterministic or independent empirical
  laws tending to the fixed target law without relative sample/width growth
  restrictions. Prove a separate actual raw-GD bridge through this horizon
  with an explicit sufficient step condition. The preferred target is
  eta_n->0; any stronger required restriction must be stated as such.

The long-horizon raw-GD bridge is an explicit C-X3 objective. C-H4 part D
itself asserts GF capture; its inherited C.4.5 raw-GD endpoint comparison
uses eta_n sqrt(n)->0 and is not already a raw-GD identification with the
whole perturbed population trajectory. A closure's Heun limit is neither
of those raw-GD statements.

Preserve the separate reference conclusions where the depth proof permits:
global physical reference dynamics, a strong learned reference endpoint,
and uniform whole-circle approximation to that endpoint at a sufficiently
large fixed horizon on a correspondingly small fixed neighborhood. These
are named additional conclusions, not a license to infer a perturbed-law
endpoint or one radius valid for every time. If these inherited reference
conclusions remain unproved at depth three, report that loss of scope
explicitly even if the finite substantial-training branch is completed.

## 5. Common hierarchy, numerical and resource obligations

Use L separately typed observable populations and a distinct initialized
action label for each edge between adjacent layers. A candidate finite
state has complete retained joint marks at each layer, current full-row
values w, current readout values c, and L-1 evolving feature-action matrices
Mell with their fixed initial contractions Dell. Intermediate hidden fields
are recomputed from these current quantities. Both orientations of each
edge use Mell and its transpose, with the correct population weights.

Prove a countable determining initialized-word grammar containing both
orientations of every edge, a dense nested retained family, compatible joint
initialization and a specified positive ridge schedule. No assumed sufficiency
of a finite Gaussian core, empirical rank deletion or independent resampling
of adjacent source groups may replace that construction.

At fixed hierarchy order N, state the exact finite-population equations and
prove existence and own-state restart. Then prove order convergence to the
actual nonlinear target on each branch's fixed domain and horizon. In
addition to whole-circle/whole-sphere prediction, preserve every separately
fixed admitted same-layer observation tuple involving forward and adjoint
actions, with second moments, and initial/current hidden pairs in W2 in
every layer. Prove uniform-time convergence of paired RMS and risks.
Do not invent a cross-layer pairing of neuron indices.

Here the exact finite-feature closure may still contain joint probability
laws and hence is not a finite scalar array. The numerical population rules
must replace those complete joint laws by actual finite arrays. Account for
both levels explicitly; finite feature count alone is not a finite numerical
implementation or a way to hide an infinite-dimensional state.

The finite implementation must construct all coefficients from initialization,
architecture and declared data; it uses no trained trajectory. Compile the
complete joint Gaussian program with matrix identity and orientation retained.
Discard its initialization transcript before evolution. At fixed resolution,
retained state and stage workspace have no width parameter and no growing
list of elapsed steps. Retained feature dimensions, population integration
counts and bit precision are separate axes.

Use the inherited numerical order unless a different order is proved. With
outermost limits written first it is

    lim_N lim_epsilon->0 lim_Q lim_P lim_input-quadrature
          lim_h->0 lim_precision.

Omit input quadrature for exact finite data. Here epsilon regularizes source
covariance, Q determines initialization integration, P replays joint mark
laws, and h discretizes the closure ODE. These quantities are distinct from
neural width n and actual GD step eta_n. Give each intermediate target,
primitive arithmetic consistency and eventual success under adequate finite
resource allowances. Restart must retain the complete joint state and fixed
marks, not draw a new initialization.

Executable finite data must have an explicit finite representation, such as
rational parameters, or consistent computable coordinate/weight/label
evaluators. The mathematical arbitrary-real data domain does not itself
supply such an evaluator.

Supply reusable study-owned code, deterministic checks with independent
algebraic oracles, and bounded operational validation at genuinely enriched
resolutions under a preregistered budget. No training campaign is authorized
by this contract. Require successful feasible computations at several declared
resolutions, exercising initialization, evolution, observations and own-state
restart, with timing, memory and conditioning diagnostics. Record
initialization/evolution work, retained and temporary storage, precision and
exact law-description costs. Qualitative convergence plus this actual finite
implementation and accounted operation is the completion standard.
No hierarchy-order rate, arbitrary simultaneous diagonal, automatic tolerance
selector, per-run accuracy certificate or practical cost-to-accuracy theorem
is required. Numerical refinement agreement is not an accuracy certificate.

## 6. Proof architecture and the decisive new obligation

The maintained all-fixed-depth C.1-C.2 theorem is a genuine starting point:
it supplies finite-data local existence, Gaussian source-tail control,
matrix/adjoint capture and every-vanishing-step raw GD. It does not itself
supply the full-row law completion, numerical hierarchy, or substantial
training. C.3's every-input activity proof is only two-layer and requires
a new depth argument. Maintained all-depth shifted-arctangent one-input
results do not substitute for the present tanh/two-anchor problem.

For the short branch, lift the fixed-depth construction to full rows and HS
increments, complete in the circle training law, and generalize the typed
observable projection/initializer to all L-1 actions. Prove every-layer
activity with actual reused Gaussian responses and exclude cancellation of
the contributions to a given layer; positive total gradient energy alone
does not give motion in every layer.

For the substantial-training branch, establish the three-layer orthogonal
reference and its reached source control before transferring to supported
perturbations. A useful candidate mechanism is depth independent: writing
h=(H_1^L-H_2^L)/2, b=<c,h>, and J for its hidden directional derivative,
the feature equations c_s=h, hidden_s=J* c imply

    b_s=||h||_2^2+||J* c||_hidden^2,
    (||c||_2)_(ss)>=0,              b_s>=m_L:=||h(0)||_2^2>0.

For tanh with orthogonal Gaussian initialization, set q_0=1 and
q_ell=E[tanh(sqrt(q_(ell-1)) G)^2], G~N(0,1). Then m_L=q_L/2>0.
On a strong symmetric continuation the physical clock is ds/dt=2(1-b),
so L_*(t)<=(exp(-4m_L t)). This is a conditional fitting mechanism;
it is not a completed continuation theorem. A horizon log(8)/(4m_L)
would give reference loss <=1/8 and leave perturbation slack if existence
and identification through that horizon are proved.

The two-layer reference continuation uses a first-layer scalar coordinate
change and bounded readout to obtain a Lipschitz clock system. At L=3,
Delta2=tanh'(Z2) A3* Delta3 introduces an intermediate gate multiplying
an unbounded backward field. That bound is not supplied by the old clock
argument. One needs control of the reached responses/tails on both edges,
then stability on a positive supported-law neighborhood through fitting.
Raw energy or norm bounds alone do not establish this continuation.

Three-layer completion means both branches and their common implementation
meet the clauses above. Extend to every fixed L only after identifying a
closed depth induction for the new source, activity and numerical obligations.
Constants may deteriorate with L, but every fixed-depth result must retain
positive times/radii/margins and finite state/cost descriptions. No continuous-
depth or depth-growing-with-width limit is part of this package.

## 7. Check status and boundaries

This is source-grounded author contract assembly. Complete C-H3/C-H4 and
fixed-depth source readings are recorded in the study's scoped assessment
files. They are not fresh full scientific reviews of a future C-X3 theorem.
At this checkpoint no new depth theorem, executable depth closure or empirical
claim has been accepted. Required proof units and checks will be persisted
here before any result is marked internally checked.

Only this study and maintained book/code are scientific inputs. C-X1/C-X2
remain separate unpromoted studies. The contract combines depth with the
original tanh baselines; it does not combine their unpromoted extensions.
Book/code promotion remains on standby and requires its separate gates.

# Thread 3 evidence audit

Read-only reconciliation dated 2026-09-08. This audit introduces no proof, experiment, or change to an original theorem. The research-state/evidence-ledger instructions of `investigate-conjectures` were used. “Checked” below means the saved independent mathematical agent audits; no formal proof-assistant verification is claimed.

## Provenance and authority

Target task: **Find Resume L3 proof thread (3)**, id `01a07ce0-e69d-74d2-868d-c2edc3068c7d`, host `remote-ssh-discovered:black-chatgpt-2`. The coordinator fetched its latest ten turns with the task-reading tool and saved them as [THREAD3_TRANSCRIPT_PAGE1.json](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/THREAD3_TRANSCRIPT_PAGE1.json). That export includes the completed L4, L5/L6/general-depth, three-input L2, and final near-identity general-depth turns. Its older inherited turns are partial; the exact-id local rollouts were also inspected:

- `/home/codex-b/.codex/sessions/2026/09/07/rollout-2026-09-07T19-18-29-01a07ce0-e69d-74d2-868d-c2edc3068c7d.jsonl`.
- `/home/codex-b/.codex/sessions/2026/09/07/rollout-2026-09-07T20-24-57-01a07ce0-e69d-74d2-868d-c2edc3068c7d_01a07d1d-c0eb-7b71-a35d-e7c22a1a4008.jsonl`.
- `/home/codex-b/.codex/sessions/2026/09/08/rollout-2026-09-08T07-44-02-01a07ce0-e69d-74d2-868d-c2edc3068c7d_01a07f8b-7a83-78f1-8236-0bd93e5e07b3.jsonl`.

The task's new work begins with the L3-to-L4 request. The earlier L3 power-ten/power-four results were inspected as inherited mathematical dependencies; their original authorship should not be reassigned to this task merely because they occur in its inherited context.

The last accepted activation constraint is a genuine perturbation of identity. The user explicitly rejected the separately proved overall-gain branch. That branch remains a valid separately scoped mathematical result, and is recorded below, but is not a solution of the accepted near-identity request.

## Model shared by the full population theorems

Throughout, **L counts hidden layers**, hence there are L+1 trainable blocks including the readout and L+1 raw kernel summands. Inputs obey `||x_i||²=d`; `Gamma_ij=x_i^T x_j/d`. The two-sample assumption is `|Gamma_12|<=1-delta`; the three-sample assumption is `|Gamma_ij|<=1-delta` for every distinct pair, with `0<delta<=1`. Binary labels are arbitrary. Three-sample pairwise separation allows singular Gamma; no positive `lambda_min(Gamma)` may be silently added.

The finite model has independent `W1_jk~N(0,1/d)`, `Wl_jk~N(0,1/n)` for 2<=l<=L, and **finite readout** `C_j~N(0,n^-2)`. Features satisfy `z1=W1 x`, `hl=phi(zl)`, `zl=Wl h(l-1)` and `f=<C,hL>_n`, with `<u,v>_n=u^Tv/n`. The loss is half the sum of squared residuals. The raw metric is

`(d/n)||dW1||_F² + sum_(l=2)^L ||dWl||_F² + ||dC||_n²`.

GF uses this metric and GD is simultaneous raw Euler with physical step `n^-2`; raw parameters are interpolated linearly and hidden fields are recomputed. The readout becomes zero only in the population initialization. See [depth56/PROOF.md:86](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth56/PROOF.md:86) and [L2 CONTRACT.md:8](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_depth2/CONTRACT.md:8).

For a “full global theorem” in the table, the exact conclusion is one autonomous global strong C1 population flow on L separate canonical neuron L2 spaces; L−1 bounded initialized adjacent actions with genuine adjoints and Hilbert–Schmidt learned increments; uniqueness against bounded-primal strong competitors on those spaces, including nonsymmetric competitors; and restart from reached states. For **each fixed dataset, fixed finite L, and every fixed finite physical T**, finite GF and the prescribed raw GD converge in probability along the full width sequence. Observables include predictions/loss, all raw kernel terms, both action orientations on fixed finite generated probes, same-layer joint field/true-velocity W2 laws uniformly in time and at finite collections of times, second moments, integrated squared speeds, and same-layer `(z,h)` path W2 laws with the uniform path norm. These are not operator-norm limits across widths, across-layer neuron pairings, growing-depth limits, or width convergence uniform on the infinite time half-line. See [depth56/PROOF.md:121](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth56/PROOF.md:121).

## Main positive results

| Result | Hidden L; samples | Activation and exact coefficient range | Time and conclusion | Status and authoritative source |
|---|---|---|---|---|
| Inherited power ten | L=3; 2 | `phi=az+e atan z`, `1/2<=a<=1`, `0<e<=c_poly delta^10`; convex mixture takes `a=1-theta,e=theta` | Full global theorem, original nonaffinity and initial motion | Three complete PASS reviews; [power10/PROOF.md:7](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_power10/PROOF.md:7). Preserved as an older sufficient interval. |
| Inherited power four | L=3; 2 | Same rectangle, `0<e<=c_poly delta^4`, **same c_poly** | Full global theorem; delta^8 is included | Three complete PASS reviews; [power4/PROOF.md:6](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_power4/PROOF.md:6). Stronger intervals later exist. |
| L4 extension | L=4; 2 | Same rectangle, `0<e<=c_poly delta^10`, **unchanged old pair** | Full global theorem, all five raw kernels, nonaffinity, initial motion; `loss<=exp(-2a^8 delta t)` | Three complete PASS reviews; [depth4/PROOF.md:29](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth4/PROOF.md:29). |
| Stronger L3–L6 bounds | L=3,4,5,6; 2 | Same rectangle; `0<e<=c_poly delta^pL`, with `p3=31/8`, `p4=9/2`, `p5=21/4`, `p6=83/14` | Full global theorem. One coefficient `theta<=c_poly delta^10` works at all four depths | Three complete PASS reviews; [depth56/PROOF.md:50](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth56/PROOF.md:50). |
| Every fixed finite depth | Every fixed L>=3; 2 | Same rectangle; `0<e<=c_L delta^pL`; for L>=6, `pL=9−43/[2(L+1)]`; explicit c_L below | Full global theorem; `loss<=exp(-2a^(2L) delta t)` | Same three complete PASS reviews; [depth56/PROOF.md:8](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth56/PROOF.md:8). Exponent 9 is sufficient for every fixed depth with depth-dependent prefactor. |
| Explicit local population result | L=2; 3 | **Same activation at both hidden layers**, `phi=(1-theta)z+theta atan z`, all `0<theta<=1/2`; no extra smallness versus delta | Canonical strong uncut population solution and bounded-primal uniqueness on **[0,10^-6]**; population C0=0; this appendix does not assert the complete joint GF/GD/observable theorem or general reached-state restart | Derived by source reviewer and separately checked by root; [SOURCE_REVIEW.md:97](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_depth2/reviews/SOURCE_REVIEW.md:97), [REVIEW_STATUS.md:24](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_depth2/REVIEW_STATUS.md:24). |
| Overall-gain theorem, outside accepted activation constraint | Every fixed L>=2; 3 | `phi_delta(z)=a_delta(z+atan z)`, `a_delta=324 pi exp(1) 10^10 delta^-2`, same activation at every depth | Full global theorem; `loss<=(3/2)exp[-lambda a_delta^(2L)t]`, `lambda=delta²/(324 pi exp(1))`; absolute nonaffinity `>=a_delta²/(432 pi exp(1))` for every sample/layer/time | Three complete PASS reviews at unchanged hashes; [gain/PROOF.md:7](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_gain_all_depths/PROOF.md:7). The user's rejection is recorded in [gain/README.md:1](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_gain_all_depths/README.md:1). |

**Cross-task supersession caution:** the coordinator reports a separately audited L3 `c_poly delta²` theorem in `odd_activation_lower_powers_three_inputs`. This audit does not duplicate the other task's verification. Therefore `31/8` is the strongest L3 exponent in the present depth-extension manuscript, not a claim of the strongest exponent across all four tasks. Also `c_L` is a distinct explicitly specified prefactor, substantially different from old `c_poly`; do not conflate improving an exponent with dominating every prefactor/exponent pair.

All local appendix constants are independent of the particular triple, labels, delta, theta in the stated range, cap, and mesh. Its primal stop uses the Gaussian action norm <=2 and population C0=0, then source bounds `alpha=200,beta=1`. The latest report, evidence ledger, review status, and certificate retain the appendix without retraction. The report's global-open claim is compatible with this local result. No later saved correction of this local result was found in this task's final near-identity sources.

## Exact coefficient dependencies and nonaffinity for the two-sample theorem

The unchanged old prefactor is

`C0=1296000 exp(1404), Cz=1500 C0, Cg=14400 C0`,

`eta*=4·404 exp(-1)/(27 pi·405^4)`,

`c*=min{1/2, [2 C0 (8 sqrt2)^3]^-1, [4 Cg (8 sqrt2)^(11/4)]^-1, sqrt(eta*)/[2 Cz (8 sqrt2)^(7/2)]}`,

`H=10^30(1+C0+Cz+Cg+exp(1410))^4`,

`c_poly=min{1/4,c*,10^-70 H^-400}`.

Its saved decimal logarithm is about −1,004,171.5713. It is an explicit sufficient mathematical constant, not a practical-size claim. Exact definitions are together in [depth4/PROOF.md:11](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth4/PROOF.md:11).

For every L>=3, write `b_L=2^(L-1)sqrt((L-1)!)`, `D_L=3·2^(2L-2)sqrt(2(L-1)!)`, `eta_L=4·4^(L-1)exp(-1)/[27 pi(4^(L-1)+1)^4]`, `c_L=H_L^-100 D_L^-2pL`. For 3<=L<=6, H_L=H. For L>=7, put

`rho_L=1/[100(L+1)]`, `B_L=4 sqrt(L(L-1))`,

`mathcalC_L=exp(1/200)b_L[ sqrt(L)arsinh(B_L)+(L/2)log(1+B_L²)+(rho_L pi L/2)] +2L`,

`H_L=max{H,10^100(8L)^L,4/eta_L, exp(mathcalC_L+1000 L² log(10L))}`.

These constants depend **only on L**. Thus an admissible e or theta depends only on delta and the declared depth, not on the realized angle inside the class, labels, d, n, or a physical horizon T. Through L6 the optional old c_poly depends on neither depth nor dataset. Source/affine proof clocks and tube constants may depend on the dataset; they do not make the physical theorem a small-time result. The complete source construction is carried far enough in feature time to cross prediction one, then the physical clock covers all t>=0. See [depth56/PROOF.md:18](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth56/PROOF.md:18) and [depth56/PROOF.md:403](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth56/PROOF.md:403).

The population nonaffinity bound is `inf_(alpha,beta) E[phi(z_i^l)-alpha-beta z_i^l]^2 >= e² eta_L/4` at every finite physical time. For convex mixtures through L6 the old eta* can replace eta_L; also the old weaker loss rate `exp(-delta t/32)` persists there. Every hidden raw block and every sample's preactivation and feature at every layer has nonzero initial second derivative; the projected kernel has a positive second-order change. Perpetual nonzero feature velocity is not asserted. See [depth56/PROOF.md:137](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth56/PROOF.md:137).

## Three-input initialization and necessary fitting results

These are independent proved partial results. Their quantifiers do not include trained-Gram preservation, global population existence, or joint population/GF/GD limits.

1. **Sharp L2 initialized feature Gram.** For all separated triples, all `0<theta<=1/2`, and `a=1-theta`, let `b3=[1−2 E(1+G²)^-1]/sqrt6`. Then

   `Q2(0) >= [a² b3²/3] theta² delta²(2-delta)² I3 >= [81 exp(-1/4)/(230400 pi)]theta² delta² I3`.

   For d>=2 and `0<delta<=1/4`, the infimum over admissible triples is `Theta(theta²delta²)` with absolute comparison constants uniformly for all `0<theta<=1/2`. This includes singular input Grams. The positive initialized features admit a readout fitting every label vector; that is an expressivity witness, not a trained-trajectory result. [L2 REPORT.md:19](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_depth2/REPORT.md:19).

2. **All-depth initialized variance and Gram.** For every integer L>=1 in the exact convex mixture family,

   `1/[1+(5/2)theta L] <= q_L <= 1/[1+theta L/6]`,

   `Q_L(0) >= theta²delta²/[324 pi exp(1)(1+(5/2)theta L)] I3`.

   For `C_L=Q_L/q_L`, `lambda_min(C_(L+1))>=lambda_min(C_L)` and `lambda_max(C_(L+1))<=lambda_max(C_L)`; condition numbers cannot increase after the positive first layer. This is not the matrix-order statement `C_(L+1)>=C_L`, and it is not monotonicity in training time. For fixed positive theta,delta, the depth order 1/L is optimal because `lambda_min(Q_L)<=q_L`. [INITIALIZATION.md:7](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_near_identity_all_depths/INITIALIZATION.md:7).

3. **Initialized absolute regression residual.** For `Z~N(0,q)`, `0<q<=1`, the exact convex mixture satisfies

   `theta²q³/384 <= inf_(alpha,beta) E[phi_theta(Z)-alpha-beta Z]² <= (2/3)theta²q³`.

   At layer L one must use the preactivation variance **q_(L−1)**. At fixed theta the absolute gap is order L^-3, remaining positive at every finite L. [REPORT.md:54](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_near_identity_all_depths/REPORT.md:54).

4. **L2 necessary distance/time.** The triple with `u1+u2+u3=0`, every off-diagonal cosine −1/2, and labels all +1 is admissible for every `0<delta<=1/2`. For every parameter state reaching loss <=3/8 from canonical population initialization,

   `R>=sqrt(9+2/(pi theta))−3`.

   Any true strong GF reaching that loss at time T satisfies

   `T>=(2/3)[sqrt(9+2/(pi theta))−3]²`, and `liminf_(theta->0) theta T>=4/(3 pi)`.

   Infinite fitting time satisfies the inequality. The claim does not assume that a global solution or fitting exists. [L2 REPORT.md:96](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_depth2/REPORT.md:96).

5. **Every fixed depth necessary distance/time.** On that same triple, for L>=2 a successful state satisfies

   `R >= [(pi L theta)^(-1/L)−2]_+`, and `liminf theta^(1/L)R>=sqrt(L) pi^(-1/L)`.

   A true strong GF reaching loss <=3/8 obeys the squared-distance/energy lower bound and, more strongly, whenever `theta<2/[pi(3^L−1)]`,

   `T>=4/[3 pi(3^L−1)theta]`.

   Thus `liminf theta T>=4/[3 pi(3^L−1)]>0` for each fixed L, and for L>2 `liminf theta^(2/L)T=+infinity`. The earlier L2 constant `4/(3pi)` is stronger at L=2. The inverse-theta first-exit bound supersedes only the weaker time exponent 2/L for L>2, retaining the earlier distance estimate. [NECESSARY_FITTING_SCALE.md:8](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_near_identity_all_depths/NECESSARY_FITTING_SCALE.md:8), [first-exit addition:95](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_near_identity_all_depths/NECESSARY_FITTING_SCALE.md:95).

The L2 partial manuscript has three complete partial-scope reviews. The all-depth initialization and necessary-fitting manuscripts have two reports explicitly matching their final hashes; the geometry author independently checked the initialization argument, and the source reviewer independently checked the fitting-time addition contributed by the limits reviewer. These are partial theorem checks, not three independent complete proofs of the open global target.

## Exact negative quantifiers and proof-method limitations

- **Depth-uniform numerical rate is false for the fixed convex mixture.** For every fixed `0<theta<1`, initialized feature variance `q_L~1/(2theta L)`. For two separated samples and `p_i=y_i/2`, `delta q_L/2<=kappa_L(0)<=q_L` and `loss_L'(0)=−4kappa_L(0)->0`. Hence there cannot be a **positive gamma_delta independent of L** with `loss_L(t)<=exp(-gamma_delta t)` for every depth and every t>=0 under this fixed activation. Likewise no positive absolute activation-regression margin can be uniform in depth. This does **not** refute one common activation giving qualitative global results at every fixed L with depth-dependent rates/margins. [DEPTH_UNIFORMITY.md:15](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth4/DEPTH_UNIFORMITY.md:15), [negative implication:92](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth4/DEPTH_UNIFORMITY.md:92).

  The same checked initialization audit proves `q_l±c_l >=(1-theta)^(2l)(1±rho)>0`, preservation of the sign of normalized correlation `r_l=c_l/q_l` with `|r_(l+1)|<=|r_l|<=|rho|`, and initialized regression residual asymptotic `1/(12 theta L³)` at hidden layer L. Its full-second-moment transpose recursion also certifies nonzero formal initial hidden-block and individual sample/layer accelerations at every fixed finite depth for any fixed nontrivial convex mixture; interpreting these as actual trajectory derivatives still requires a constructed regular trajectory. These fixed-initialization facts do not supply that trajectory. See [DEPTH_UNIFORMITY.md:26](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth4/DEPTH_UNIFORMITY.md:26) and [initial motion:109](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth4/DEPTH_UNIFORMITY.md:109).

- **Theta-uniform fitting rate is false on the three-input class.** Fix any `0<delta<=1/2` and L>=2 and use the equilateral all-positive-label example. There cannot be a positive loss rate depending only on delta,L, with a fixed finite theta-independent prefactor, that holds uniformly for **every positive theta below an upper cutoff** and implies uniformly bounded time to loss 3/8. Necessary inverse-theta fitting time contradicts it. With the exact initial loss prefactor at L2, differentiating at zero also forces `kappa<=6||H0||²<=(3pi²/2)theta²(1+2a)²`. This does not exclude a theta-dependent rate or one fixed positive theta selected per delta,L. [L2 REPORT.md:76](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_depth2/REPORT.md:76), [NECESSARY_FITTING_SCALE.md:88](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_near_identity_all_depths/NECESSARY_FITTING_SCALE.md:88).

- **Affine stationarity is a comparator obstruction, not a nonlinear counterexample.** At theta=0 the equilateral triple with all labels +1 has stationary population flow at loss 3/2. For positive theta the initialized Gram is strictly positive. The divergent required parameter excursion rules out uniform closeness to that stationary affine reference through fitting. It does not refute the positive-theta theorem.

- **Frozen-feature reference really does fit globally, but is a different model.** Freeze the nonlinear first features with positive Gram Q, make the second activation affine with slope a, and train its action/readout. The exact invariant `BB*−C tensor C=P_E` implies `Q_out>=a²Q`, global unique reference GF, loss `<=loss(0) exp(-2a² lambda_min(Q)t)`, and factors O(theta^-1/2 delta^-1/2). At equilateral reference states with any fixed prediction j in (0,1), the omitted true bottom physical force tends to a nonzero vector as theta->0, even including true top nonlinearity. Thus a uniformly vanishing-vector-field-defect comparison fails; this is not a proved separation of the actual trajectories or failure of every comparison. [NONLINEAR_REFERENCE.md:5](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_depth2/NONLINEAR_REFERENCE.md:5), [comparator defect:85](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_depth2/NONLINEAR_REFERENCE.md:85).

- **Conditional symmetric clock.** On the equilateral triple, if the true regular nonlinear ascent continues through first prediction one, its physical clock gives `loss(t)<=(3/2)exp[-(2/3)a²b3²theta²delta²(2-delta)²t]`. The continuation premise is open; generic triples also lack that transitive symmetry. [L2 REPORT.md:201](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_depth2/REPORT.md:201).

- **Exact source and energy facts remain valid without solving continuation.** L2 source equations retain forward/reverse expected formal derivatives, learned moments, full temporal/sample covariance, and current return `diag E[phi''(Z)C]`. Bounded primal/coefficient prefixes imply explicit marginal subGaussian and derivative bounds, but the prefix closure on arbitrary physical horizons is missing. Every finite-width true GF is global by its exact finite-dimensional energy argument. An existing strong population GF has compact-time raw length <=sqrt(3T/2) and strong finite endpoints, but these do not create local well-posedness at arbitrary infinite-dimensional endpoints. The multiplier `C phi''(Z)` can be unbounded on an L2 ball; that is an ambient-state obstruction, not a reached-state counterexample. Ordinary backward caps are not the original loss gradient. [SOURCE_AND_CONTINUATION.md:5](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_depth2/SOURCE_AND_CONTINUATION.md:5), [checked scope:71](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_depth2/reviews/SOURCE_REVIEW.md:71).

- **Covariance-weighted source return is exactly controlled in L2.** Under integrable formal source derivatives and justified Gaussian integration by parts, including singular covariance Sigma, `B Sigma=E[d xi^T]` and `||BX||²=||Proj_span(xi)d||²<=||d||²`. Individually smooth near-identity subGaussian features need not control every normalized span element in Lp for p>2: the saved smooth translated-bump construction has diverging Lp/L2 ratio. This is a counterexample to a generic span inference, not to the reachable trained network. [SOURCE_ROUTE.md:5](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_near_identity_all_depths/SOURCE_ROUTE.md:5); separately checked in [SOURCE_PARTIAL_REVIEW.md:117](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_near_identity_all_depths/reviews/SOURCE_PARTIAL_REVIEW.md:117).

- **Offset geometry is a positive initialization result only.** For any nonzero beta and three distinct normalized vectors in the stated separation class, `Gamma+beta²11^T` has smallest eigenvalue at least `8 beta²delta³/[9(1+beta²)²]`; the initialized affine-offset recursion retains this floor. The global affine physical training/response budget needed for a near-identity perturbation transfer remains open in this route. [SOURCE_ROUTE.md:33](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_near_identity_all_depths/SOURCE_ROUTE.md:33); separately checked by the source reviewer at line 125.

- **Unrestricted bounded-control continuation is false in the generic scalar model.** `w=A=sec s,C=tan s` solves the exact identity-activation ascent from `(1,1,0)` and blows up at pi/2 with bounded control 1. This disproves the proposed long-horizon premise for arbitrary controls, not physical squared-loss GF and not the Gaussian three-input model. [SOURCE_ROUTE.md:59](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_near_identity_all_depths/SOURCE_ROUTE.md:59); independently checked by the source reviewer at line 123.

- **Galerkin route is an auxiliary exact construction with an unclosed bridge.** Finite-partition true-gradient approximants have genuine adjoints, global finite-dimensional GF, exact energy, and uniform compact-time raw length bounds. A specified uniform unresolved-coordinate compactness assertion would imply a subsequential global strong population solution. It remains unproved, and even the conditional result alone does not imply uniqueness, full sequence limits, actual finite-width GF/GD identification, or fitting. The saved final certificate does not promote this route note to an independently accepted full theorem; retain it as a checked route/identity record rather than a principal theorem row. [ENERGY_GALERKIN_ROUTE.md:68](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_near_identity_all_depths/ENERGY_GALERKIN_ROUTE.md:68).

The final accepted near-identity request therefore remains open in this task: neither a polynomial theta cutoff nor another valid positive `theta_(delta,L)` for the complete global three-input joint theorem was obtained. This is not a nonexistence result. Excluding exact antipodes removes the elementary oddness obstruction but does not remove three-vector linear dependence, and does not itself supply trained source-tail estimates.

## Hash verification and resolved corrections

Actual file bytes were rehashed against all present candidate/mathematical/dependency/certificate records in the seven principal directories. The full read-only verification output is [THREAD3_HASH_CHECKS.json](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/THREAD3_HASH_CHECKS.json). No mismatch or unresolved path remained.

| Directory | Distinct hash-bound files checked | Main manuscript SHA-256 | Review coverage |
|---|---:|---|---|
| two_sample_odd_activation_power10 | 27 | `37b9e8a27135b95b8dffe05fe2b734229fadedc98bc1609259e365dbb2aeba37` | 3 complete PASS, 4 mathematics, 19 dependencies |
| two_sample_odd_activation_power4 | 31 | `7e33899649b547e7dcac8a465f2d118518d9db9ef001a3d04d2b9da615aa9485` | 3 complete PASS, 4 mathematics, 23 dependencies |
| two_sample_odd_activation_depth4 | 32 | `f91ce73868922220fd7f6621e08b167472639ebe10f8775d6bb632c10e31c585` | 3 complete PASS, 5 mathematics, 23 dependencies |
| two_sample_odd_activation_depth56 | 37 | `366bf83ff0250a42da9f4f2fae7d51f0dd296cfb2ea3c462761423fec09e8d70` | 3 complete PASS, 4 mathematics, 28 dependencies |
| three_sample_odd_activation_depth2 | 22 | `25cfd1e93b619b6c5aabc674cab7170199024ac7a3cb700365a23048e62d341f` | 3 partial-scope reviews, 5 math/contract files, 13 dependencies; local appendix separately root-checked |
| three_sample_near_identity_all_depths | 6 | `98207c46cb44c525ef0fd7e140a97624bd9750939c3e260a1d03d92c3f7614b8` | 2 final reports match both primary partial-proof hashes; scope as above |
| three_sample_odd_gain_all_depths | 11 | `e8088b9554332c2d45250dec5e1b0004badb0252e5cfe63cefde0f8896e59f66` | 3 complete PASS reports each contain every final four-proof-file hash; 6 dependencies |

Near-identity partial proof hashes: `INITIALIZATION.md=f53b4893ae4cacc2180ab1149c2c00a1b8f8b0b941d3319df5a3c0009f531163`; `NECESSARY_FITTING_SCALE.md=98705d5550bb977f26712e273b47592340ba2899cf952025889b386349af1fbd`. Both final reviews explicitly contain both hashes. The L2 local appendix lives in `reviews/SOURCE_REVIEW.md`, whose certificate-matching hash is `7257c876929a9d5e2a33d81bbb0112865e78f5681074e0b49cb86cbc123d54b9`.

Resolved corrections, already included in the reviewed versions:

- Power ten: restored missing printed addition, distinguished local feature h from numerical H, restricted the outer box to forward strict densities and causal row bounds actually used; arbitrary backward row errors need not have bounded strict density.
- Power four: rounded affine source numerical envelope to `10^30 exp(2100)<H`; placed terminal maximum outside expectation for the backward derivative-row bound.
- Depth56: corrected omitted gate-error terms before final assembly; final certified powers are 21/4 and 83/14 at L5/L6, not provisional commentary exponents 6 and 47/7 or a more optimistic omitted-term calculation. Bibliographic edition correction preceded all final reviews.
- L2 partials: replaced the incorrect squared-uniform-integrability inference from an L2 ball with the accurate statement; retained the exact missing L2-tail obligation.
- General-depth near-identity: first-exit inverse-theta time bound was added and independently checked at final hashes; it improves the earlier time exponent at L>2.

No correction found here invalidates the accepted positive theorem versions. Hash agreement establishes version identity, while the saved mathematical reviews supply the proof checking; neither should be represented as machine-checked formal mathematics.

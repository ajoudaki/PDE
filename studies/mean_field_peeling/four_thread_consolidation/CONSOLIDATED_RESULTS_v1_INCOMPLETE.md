# Consolidated verified results from the four Find Resume L3 proof tasks

Consolidated 2026-09-08. This is an evidence and scope reconciliation, not a resumed proof search. It incorporates **Find Resume L3 proof thread**, **Find Resume L3 proof thread (2)**, **(3)** and **(4)**. Original manuscripts and review records were preserved unchanged.

“Verified” here means a proved statement with the saved mathematical checking/review described below, whose accepted version was recovered. It does not mean formal proof-assistant verification. Three separate agents audited the three forked tasks' statements, final reviews, superseding results and file identities; the coordinating agent audited the root results and reconciled their scopes. This consolidation is not a fresh full re-proof of every manuscript.

## Reading the tables

Write L for the number of **hidden layers**, m for the number of samples, u_i=x_i/sqrt(d), and Gamma_ij=<u_i,u_j>. Inputs have ||x_i||^2=d. Except for explicitly stated inherited one-sample baselines, every trained theorem below permits **all binary labels**, y_i in {-1,1}; there is no unproved extension to arbitrary real labels.

- **Global joint:** one autonomous global strong canonical population flow, with the stated bounded-primal uniqueness/restart, and joint full-sequence finite GF and prescribed raw-GD convergence on **every fixed finite physical [0,T]**. The activation is fixed before choosing T.
- **Semi-global joint:** the same existence/limit conclusions on every [0,T] with T<T_* for a specified absolute T_*>0. A local construction on [0,T_*] implies this convention. Restart uniqueness inside that interval is not an all-time continuation theorem.
- **Population only:** construction/uniqueness of a population flow without the complete finite GF/GD limit and observables. Even if its time is universal, this is not the user's semi-global joint result.
- **Initialization only:** properties at t=0, possibly at all depths. This gives neither positive-time population existence nor convergence of training.
- **Conditional:** the implication is proved, but a named premise is not established for the actual initialized system.

The common modern model fully trains width-n hidden layers and readout, with independent W1 entries N(0,1/d), higher W entries N(0,1/n), and **actual finite readout C_j~N(0,n^-2)**. Prediction is <C,h^L>_n; loss is half the sum of squared residuals. The raw metric is (d/n)||dW1||_F^2 + sum_(l>=2)||dWl||_F^2 + ||dC||_n^2. GD is simultaneous raw Euler with physical step n^-2; raw parameters interpolate and hidden fields are recomputed. C0=0 is a population limit, not a replacement made in the actual finite algorithms.

“Joint” includes predictions and loss, all L+1 true kernel blocks, both action orientations and actual adjoints on generated probes, same-layer joint sample field path laws in W2 with the uniform path norm, field/velocity laws, second moments and integrated squared speeds. The exact topology and uniqueness class are in the linked manuscripts. There is no general assertion of cross-width operator-norm convergence or cross-layer pairing of individual neurons.

The two geometry conditions below are genuinely different:

- **One-sided:** Gamma_ij <= 1-delta. Antipodes are allowed.
- **Two-sided:** |Gamma_ij| <= 1-delta. Both near-coincident and near-antipodal inputs are excluded.

The user's strict interval (-1+delta,1-delta) is covered by the corresponding non-strict two-sided theorem. For three samples, either condition permits singular Gamma. No full-rank or quantitative input-eigenvalue assumption is silently imposed.

## Complete global and semi-global joint theorems

Define two shape classes:

- B: nonconstant psi in C^2(R), with max(||psi||_infinity,||psi'||_infinity,||psi''||_infinity)<=1.
- D: psi in C^2(R), with |psi(0)|<=1, ||psi'||_infinity<=1 and ||psi''||_infinity<=1. B is bounded; D may grow linearly and need not be nonaffine.

| ID | Hidden layers; samples | Activation | Inputs and coefficient quantifiers | Result and authority |
|---|---|---|---|---|
| G1 | L=3; m=2 | 1+z+e atan(z) | One-sided; 0<delta<=2; every 0<e<=e_delta, with a constructive positive e_delta depending only on delta | **Global joint**, including antipodes. [Proof](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_separated_angle_theorem/PROOF.md:11). Three complete PASS reviews. |
| G2 | L=3; m=2 | az+e atan(z), 1/2<=a<=1 | Two-sided; 0<delta<=1; every 0<e<=c_poly delta^2, c_poly absolute | **Global joint.** Includes the exact convex mixture (1-theta)z+theta atan(z), theta<=c_poly delta^2. [Exponent-two theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/odd_activation_lower_powers_three_inputs/TWO_INPUT_PROOF.md:27). Three complete PASS reviews. |
| G3 | Every separately fixed L>=3; m=2 | az+e atan(z), 1/2<=a<=1 | Two-sided; 0<delta<=1; every 0<e<=c_L delta^(p_L), with explicit depth-dependent c_L>0 | **Global joint.** p3=31/8, p4=9/2, p5=21/4, p_L=9-43/[2(L+1)] for L>=6. G2 supplies an additional L3 bound with exponent 2. [All-depth statement](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth56/PROOF.md:8). Three complete PASS reviews. |
| G4 | L=3; m=2 | az+e psi(z), psi in D, 1/2<=a<=1 | Two-sided; 0<delta<=1; every 0<e<=c_dyn delta^(31/8); c_dyn absolute and shared across normalized D | **Global joint.** Oddness, monotonicity and boundedness of psi are unnecessary. [Theorem A](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_activation_design/PROOF.md:45). Three complete PASS reviews. |
| S1 | L=3; m=2 | Exact calibrated sine Phi given below; coefficient 2/5, frequency 2 | Two-sided; 0<delta<=1; no coefficient smallness depending on delta, T or width | **Semi-global joint**, with absolute T_*=S0/3>0 independent of delta, inputs, labels, dimension and width. Global continuation remains open. [Local proof](/home/amir/Codes/PDE/studies/mean_field_peeling/moderate_sine_global/LOCAL_SOURCE.md:248). Full local source/bridge PASS and additional observable-bridge PASS. |
| G5 | L=3; m=3 | a_delta(1+z)+e atan(z) | One-sided; 0<delta<=3/2; suitable a_delta>=1 and every 0<e<=e_delta, selected from delta alone | **Global joint**, singular triples included. [Self-contained Theorem M.1](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_self_contained/MANUSCRIPT.md:242). Four fresh whole-manuscript PASS reviews. |
| G6 | L=3; m=3 | a_(delta,psi)(1+z)+e psi(z), psi in B | One-sided, feasible separated triples; explicit suitable a>=2 and every sufficiently small e>0, depending on delta and psi | **Global joint.** [Self-contained manuscript](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_activation_class/MANUSCRIPT.md), [statement](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_activation_class/RESULT.md). Four fresh whole-manuscript PASS reviews. |
| G7 | Every separately fixed L>=2; m=3 | a_(delta,psi)(1+z)+e psi(z), psi in B | One-sided; 0<delta<1; one pair works at all finite depths: explicit a depending only on delta,psi and **any fixed e in (0,1], including e=1** | **Global joint**, same activation independent of L and T. [Theorem and constants](/home/amir/Codes/PDE/studies/mean_field_peeling/activation_class_all_depths/MANUSCRIPT.md:5). Two fresh whole-manuscript PASS reviews. |
| G8 | Every separately fixed L>=2; m=3 | a_delta(z+atan(z)) | Two-sided; 0<delta<=1; a_delta=324 pi exp(1) 10^10 delta^-2, independent of L,T | **Global joint**, no offset. This is a valid theorem with an overall gain, which the user rejected as answering the near-identity request. [Proof](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_gain_all_depths/PROOF.md:7). Three complete PASS reviews. |

All G-rows have activation choices uniform over the specified configurations and labels. The probabilistic width limits are still **for each fixed dataset**: none of these rows asserts a supremum over all datasets inside a convergence-in-probability statement. “Every separately fixed L” does not mean a theorem with L=L(n) growing as width grows. “Global” does not mean convergence uniformly over [0,infinity).

### Coefficients, normalization and quantitative interpretation

For G2, log10(c_poly) is approximately -1,004,171.5713. Its exact definition is retained in [THREAD2_AUDIT.md](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/THREAD2_AUDIT.md). Earlier powers 800, 10 and 4 with this same prefactor are superseded by exponent 2. This proves polynomial dependence on delta, not a practically large sufficient coefficient.

For G3, c_L=H_L^-100 D_L^(-2p_L), with D_L=3*2^(2L-2)*sqrt(2(L-1)!) and H_L explicitly defined from L alone. The exact formula and separate retained c_poly are in [THREAD3_AUDIT.md](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/THREAD3_AUDIT.md). The old same c_poly delta^10 works simultaneously for L=3,4,5,6; no common positive coefficient for every L is proved in this near-identity branch. A smaller exponent alone need not dominate a sufficient bound with a much larger prefactor: G2 and the c_3 formula should both be retained.

G2 also covers the **unit Gaussian-energy** activation

phi_r(z) = [z+r atan(z)] / sqrt(E[(G+r atan(G))^2]), G~N(0,1), 0<r<=c_poly delta^2.

This lies inside the (a,e) rectangle and has unit initialized variance at every hidden layer. It is not literally a convex combination, and it does not preserve trained variance. [Normalization proof](/home/amir/Codes/PDE/studies/mean_field_peeling/odd_activation_lower_powers_three_inputs/TWO_INPUT_PROOF.md:310).

For G4, log10(c_dyn) is approximately -230,954.3591. The existence/limit theorem needs no nonaffinity hypothesis. If psi is globally nonaffine, let

eta_psi = min_(1/sqrt(404)<=sigma<=260) inf_(b,c) E[(psi(sigma G)-b-c sigma G)^2] > 0.

With the additional restriction e<=c_NL(psi)delta^(31/8), where c_NL=sqrt(eta_psi)/[4 C_z(8sqrt(2))^(7/2)], its actual activation regression error stays >=e^2 eta_psi/4 at every time, sample and layer. Globally nonaffine shapes already give nonzero initial hidden acceleration and a changing projected kernel without this extra persistent-margin cutoff. Whole infinite-dimensional neighborhoods admit a common margin and common coefficient. [Addendum and constants](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_activation_design/PROOF.md:90).

For G6/G7, normalized tanh, sine, cosine, Gaussian bumps and nonzero compactly supported C^2 functions are examples **of the perturbation psi**. These rows do not prove the result for such a bounded function used alone as the entire activation. B contains neither arbitrary unnormalized functions nor ReLU. Suitable infinite-dimensional C_b^2 neighborhoods have common coefficient recipes.

G7's explicit selection is lambda=delta^2/16, S_aux=12/lambda and

a=max{10^12(1+S_aux), [2^36 S_aux^2/sqrt(c_psi)]^(2/5)},

where c_psi>0 is supplied by the nonaffine L2 regression error on a fixed compact interval. S_aux is a proof-control time, **not a physical existence cutoff**. The large gain makes e/a small. G8 instead rescales the entire nonlinear activation; its scale is also outside the user's no-gain restriction. Neither should be described as a verified moderate normalized near-identity solution.

G1/G2/G3/G5/G6/G7/G8 include the stated persistent nonaffinity and initial feature-motion conclusions. Initial acceleration or a changing kernel near zero does not assert nonzero velocity at every later instant. G7's positive nonaffinity lower bound may deteriorate with L; uniform activation parameters do not assert uniform nonaffinity margins.

### Exact moderate activation and physical interval

The S1 activation is

Phi(z) = [z+(2/5)(sin(2z)-2 exp(-2)z)] / sqrt(1+(4/25)v),

v=(1-exp(-8))/2-4exp(-4)>0.

It is smooth and strictly increasing. At initialization it has exactly unit variance, and its best-affine residual accounts for the fraction (4v/25)/(1+4v/25), approximately **0.06389055**, of its output variance. This applies to every initialized hidden layer; trained Gaussianity or persistence of that relative fraction is not claimed.

For an exact universal interval, put B=20, D=2^10 B^5 and A=10^4 D^4. Then

T_* = (1/3) min{1, [100*2^3*B^3]^-1, [4*2^6*B^6]^-1, [10000*D*A^2]^-1/2}.

Numerically this particular sufficient T_* is approximately **5.05073*10^-50**. The symbol L=2 in the source's local constant calculation denotes a slope envelope; the network has **three hidden layers**. The result is a fixed moderate-amplitude semi-global theorem in the user's precise sense, but its proved time constant is highly conservative. It is not a verified practically useful duration. [Constant recipe](/home/amir/Codes/PDE/studies/mean_field_peeling/moderate_sine_global/LOCAL_SOURCE.md:43).

## Checked positive results that do not give the full joint theorem

| ID | Depth / samples / activation / assumptions | Proved conclusion and limit of scope |
|---|---|---|
| P1 | L=2; m=3; phi_theta=(1-theta)z+theta atan(z), all 0<theta<=1/2; normalized two-sided separated inputs, all binary labels | Canonical strong population existence and bounded-primal uniqueness on **[0,10^-6]**, with constants independent of theta and geometry. This reviewed appendix does **not** claim the complete joint finite GF/GD and observable theorem. [Appendix](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_depth2/reviews/SOURCE_REVIEW.md:97). |
| P2 | m=3; exact phi_theta, 0<theta<=1/2; two-sided separation, singular input Grams allowed | At L=2 and L=3, worst-case initialized feature conditioning is **Theta(theta^2 delta^2)**, uniformly for d>=2 and 0<delta<=1/4. At general L>=1, Q_L >= theta^2 delta^2/[324 pi exp(1)(1+(5/2)theta L)] I. Labels are irrelevant. This is initialization, not preservation under training. [L2](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_depth2/REPORT.md:19), [L3 sharpness](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_threshold/REPORT.md:17), [all depths](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_near_identity_all_depths/INITIALIZATION.md:7). |
| P3 | Same exact convex mixture; all initialized depths | q_L lies between [1+(5/2)theta L]^-1 and [1+theta L/6]^-1. For normalized C_L=Q_L/q_L, lambda_min is nondecreasing and lambda_max nonincreasing with depth. This is eigenvalue monotonicity at initialization, not Loewner monotonicity and not training-time monotonicity. Initialized regression residual is of order theta^2 q_(L-1)^3. [Initialization](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_near_identity_all_depths/INITIALIZATION.md). |
| P4 | m=3; two-sided separated inputs; depth-dependent calibrated near-identity family phi_L=(z+sqrt(tau/L) chi(z))/sqrt(1+tau/L), fixed tau>0, explicit bounded trigonometric chi | Unit initialized variance; depth-uniform positive initialized feature-Gram floor; nontrivial sequential width-first/depth-second correlation limit. No trained-flow or simultaneous width/depth theorem. Two isolated full-note PASS reviews. [Proof](/home/amir/Codes/PDE/studies/mean_field_peeling/calibrated_near_identity_reviews/manuscript.md). |
| P5 | L=3; m=2; exact moderate Phi; all binary labels | Actual finite GF is global, actual GD satisfies finite-horizon energy/displacement bounds eventually in width, and field paths are **weakly tight**. An existing strong population trajectory has a strong finite endpoint. These do not identify a unique global population/GF limit or prove W2 compactness. [Physical continuation](/home/amir/Codes/PDE/studies/mean_field_peeling/moderate_sine_global/PHYSICAL_CONTINUATION.md). |
| P6 | Same moderate Phi and model, with the additional uniform exponential-tail hypothesis ET | ET implies global strong canonical population existence/uniqueness/restart. ET remains unproved, and the global finite GF/GD/observable reassembly is not completed by this conditional note. [Conditional theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/moderate_sine_global/CONDITIONAL_GLOBAL_AND_OBSTRUCTIONS.md:103). |
| P7 | Practical fixed L=2,m=3 program, initially targeting .75(1+z)+.25 tanh(z) | Global dissipative population approximants and a **conditional** cap-removal theorem are proved. The uniform tail premise and actual finite algorithm bridge are open. A separate plateau activation has a deterministic first-row confinement theorem assuming existing pathwise solutions; this is not population existence. Each of the two manuscripts received two fresh complete PASS reviews. [Cap theorem](/home/amir/Codes/PDE/studies/mean_field_peeling/practical_fixed_depth2/CAPS_MANUSCRIPT.md), [confinement](/home/amir/Codes/PDE/studies/mean_field_peeling/practical_fixed_depth2/development/PLATEAU_CONFINEMENT.md). |

For P4, chi is the L2(Gaussian)-normalization of exp(3/2)sin(2z)/2-sin(z), so E chi(G)=E[G chi(G)]=0 and E chi(G)^2=1. The initialized Gram bound is at least

[p3 delta^2(2-delta)^2/3] [1-(1+tau/L)^(-L)] I
>= [p3 delta^2(2-delta)^2/3] tau/(1+tau) I,

where p3>0 is the explicit cubic Hermite mass in the note. This construction answers an initialization question about accumulation across many near-identity layers, not the user's global trained-limit objective.

## Proved negative results, with their exact targets

1. **Oddness and antipodal equal labels are incompatible with fitting.** In a bias-free network with odd activation, f(-x)=-f(x) at every width and parameter state. Equal labels on an antipodal pair force a positive loss floor and a common raw-kernel null direction. Such a pair is admissible under one-sided separation. This motivates the two-sided geometry for odd activations; it does **not** refute existence of GF or a population limit. [Proof](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_separated_angle_theorem/SHIFT_AND_ENERGY_NORMALIZATION.md:10).

2. **Pairwise separation does not guarantee an input spectral gap.** The equilateral planar triple has cosines -1/2 and a singular Gamma. There are full-rank triples with the same fixed absolute separation and lambda_min(Gamma) tending to zero. Pure affine, zero-readout population flow is stationary on the equilateral triple with all labels +1, at loss 3/2. This invalidates a uniformly successful affine comparator for that label component, not positive-theta nonlinear training. [Geometry](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_threshold/REPORT.md:68), [stationarity](/home/amir/Codes/PDE/studies/mean_field_peeling/odd_activation_lower_powers_three_inputs/THREE_INPUT_ANALYSIS.md:113).

3. **Fitting cannot have theta-independent speed over the entire small-theta family.** For the exact convex mixture on the equilateral all-positive-label triple and each fixed L>=2, any actual strong GF that reaches loss <=3/8 requires T=Omega_L(theta^-1). At L2 the checked sharper bound is T>=(2/3)[sqrt(9+2/(pi theta))-3]^2 and liminf_(theta->0) theta T>=4/(3pi). The successful raw-state excursion also diverges. No fitting or global continuation is assumed in this necessary condition. It rules out theta-uniform fitting rates, not global existence for one fixed theta. [General-depth proof](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_near_identity_all_depths/NECESSARY_FITTING_SCALE.md:95), [L2 bound](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_depth2/REPORT.md:96).

4. **Additional three-sample small-direction bounds are exact.** For L3, Gram-null directions satisfy v^T K v<=256 theta^2 ||v||_1^2(11+R)^6 on a raw ball of radius R, for the sum of all four kernel blocks. Clustered separated triples additionally require R>(10 theta sqrt(delta))^-1/4-11 to reach loss <=3/8. These preclude uniform conditioning or fitting inside fixed balls as the parameters shrink. They do not prove loss failure along the true trajectory. [Kernel bound](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_threshold/routes/NONLINEAR_REFERENCE.md:83), [distance bound](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_odd_activation_threshold/REPORT.md:93).

5. **Fixed convex mixtures cannot have a positive depth-uniform raw rate or absolute nonaffinity floor.** In the two-sample model with phi_theta=(1-theta)z+theta atan(z), fixed 0<theta<1, initialized variance q_L~1/(2theta L); the initial loss-decay slope tends to zero, and initialized absolute nonaffinity decays as L^-3. Consequently a positive exponential rate with the exact initial-loss prefactor cannot be uniform over all depths. This does not rule out a common activation with depth-dependent rates and qualitative global existence at every fixed L. [Proof](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_depth4/DEPTH_UNIFORMITY.md:15).

6. **Literal convex mixtures of the offset affine map have a separate exponential conditioning obstruction.** For phi_epsilon=(1-epsilon)(1+z)+epsilon psi(z), fixed 0<epsilon<1/2 and psi in B, there is kappa<1 with initialized pair feature distances and a kernel eigenvalue <=2(1-Gamma_ij)kappa^(2L). Hence a depth-independent positive initial kernel floor is impossible for this family. Two isolated full-report PASS reviews. This is not a counterexample to qualitative global population existence at each finite L. [Proof](/home/amir/Codes/PDE/studies/mean_field_peeling/convex_offset_all_depths/REPORT.md).

7. **Exact convexity, Gaussian normalization and relative nonlinearity have restrictions.** The literal nontrivial convex mixture of z and atan(z) has E phi(G)^2<1. Gaussian normalization changes the coefficients so they no longer sum to one. Separately, for phi=az+e psi with psi Lipschitz constant D and a>eD, its best-affine variance fraction is at most [eD/(a-eD)]^2 for every nondegenerate finite-variance input law. A large affine slope can therefore conceal a small relative nonlinear fraction despite an order-one absolute nonlinear coefficient. [Normalization](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_odd_activation_theorem/INITIAL_MOTION_AND_NORMALIZATION.md:199), [relative bound](/home/amir/Codes/PDE/studies/mean_field_peeling/two_sample_activation_design/RELATIVE_NONLINEARITY.md:6).

8. **Several proposed proof methods fail without further hypotheses.** The reviewed counterexamples show that bounded raw norms, second moments, or exchangeability alone do not control adaptive Gaussian-transpose square tails; combined covariance-weighted L2 responses do not control named coefficients or higher moments; the moderate sine loss is not weakly lower semicontinuous or locally semiconvex on the whole ambient Hilbert space, and its gradient is not locally Lipschitz there. The exact sine's trained conditional Gaussian damping need not retain its initialized exp(-2) factor. A scalar identity-activation controlled ascent can blow up under bounded arbitrary control, unlike the physical energy argument. None of these examples establishes that an actual initialized neural GF reaches the offending states or fails to have a global limit. [Detailed thread-2 inventory](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/THREAD2_AUDIT.md), [thread-3 inventory](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/THREAD3_AUDIT.md), [thread-4 inventory](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/THREAD4_AUDIT.md).

The component audits additionally preserve the exact checked conditional scalar-clock lemmas, frozen-feature reference theorem and its force-defect obstruction, source-response identities, bounded-activation memory bounds, affine response certificates, coordinate-straightening obstruction, and cutoff/confinement claims. Their premises and exclusions are part of this consolidated record; these auxiliary statements are not silently promoted to the user's full joint theorem.

## Open and excluded claims

- A complete global joint theorem for **three absolutely separated inputs and the exact no-gain convex mixture** remains open, including the L2 target and the general-depth target.
- The L3 three-input file claiming an absolute local time 10^-40 in `three_sample_odd_activation_full_resolution/LOCAL_THEOREM.md` explicitly says it is a candidate pending independent review. It is excluded from the verified inventory.
- The moderate calibrated sine has the full semi-global joint theorem S1. Its unconditional global theorem remains open. Its earlier “initialization only” status is superseded by S1.
- No reviewed theorem completes the practical L2, three-input .75(1+z)+.25 tanh program. Its two accepted partial manuscripts are retained in P7.
- For the no-gain near-identity family, no single positive coefficient is proved to work at **all** depths for the qualitative global joint theorem. Initialization conditioning and rate obstructions do not prove this qualitative question impossible.
- No theorem here treats an arbitrary sample count, arbitrary real labels, growing depth jointly with width, or a uniform-in-time width limit on [0,infinity).
- Explicit sufficient coefficient recipes can be chosen nondecreasing in delta (the polynomial recipes already are). This does not identify an optimal epsilon_*, prove monotonicity in angle of a sharp admissibility boundary, or show microscopic sufficient coefficients are necessary.

## Recovered inherited one-sample baselines

These earlier results are inherited context of the four tasks. They are separated because their exact loss normalization and uniqueness/measurement classes differ from the modern multi-sample contract. Readable primary proofs and reviews were preserved as exact byte copies in [the baseline archive](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/inherited_baselines/COPY_PROVENANCE.json).

| Hidden depth; samples | Activation and assumptions | Established time/limit scope | Review evidence |
|---|---|---|---|
| L=2; m=1 | atan(z) at both layers; input and label both exactly 1; small rescaled Gaussian readout variance n^-2; loss (f-1)^2 | **Global population/GF/raw-GD joint theorem**, including hidden paths, velocities, kernels and their stated measurement class. Allows any steps with eta_n sqrt(n)->0, hence n^-2. Strict feature activity and nonaffinity are proved on an initial interval only; population uniqueness uses its bounded-operator/readout-supremum class. [Delivered proof](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/inherited_baselines/L2_ONE_SAMPLE_ARCTAN_GLOBAL_PROOF.md:3). | Three fresh complete round-two PASS reviews after a measurement-product scope correction. Both reviewed and delivered versions are preserved; the historical record declares only formatting changes between them, without a historical SHA certificate. [Review record](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/inherited_baselines/L2_ONE_SAMPLE_ARCTAN_GLOBAL_REVIEW.md). |
| L=3; m=1 | atan(z) at every layer; input and label both exactly 1; small rescaled Gaussian readout variance n^-2; loss (f-1)^2 | **Semi-global joint theorem**, explicit absolute T0>0 given by equation (4) of the proof, with the complete local population/GF/GD, kernel, field/path and velocity conclusions. No all-finite-time pure-arctangent continuation theorem. [Complete proof](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/inherited_baselines/L3_ONE_SAMPLE_ARCTAN_LOCAL_PROOF.md:7). | Component/combined checks plus a fresh isolated complete-manuscript PASS tied to hash f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4; recovered bytes match. [Review record](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/inherited_baselines/L3_ONE_SAMPLE_ARCTAN_REVIEW_RECORD.md:59). |

There is also a distinct older checked L2 one-sample arctangent theorem with **order-one Gaussian rescaled readout**, arbitrary real scalar label and a Gaussian-envelope population solution class. It proves global population/GF and prediction/kernel/loss limits, including positive scalar multiples of arctangent. Its initialization and displayed observable scope differ; it does not supply the modern small-readout joint raw-GD theorem by substitution. [Older statement](/home/amir/Codes/PDE/studies/mean_field_peeling/nonlinear_activation_operator_ide/ARCTAN_THEOREM_AND_PROOF.md:7), [audit](/home/amir/Codes/PDE/studies/mean_field_peeling/nonlinear_activation_operator_ide/FINAL_AUDIT.md:1).

Historical conversations additionally report an L3 one-sample global theorem for 1+atan(z)/10 and L2 two-sample arctangent global results at orthogonal inputs or antipodal opposite-label inputs. Their apparent primary directories were inaccessible during recovery, and complete proof-plus-review duplicates were not recovered. They are **historically reported, not primary-artifact-verified in this consolidation**. This is an access/evidence limitation, not a retraction or a claim that those results are false.

## Evidence and complete component inventories

- [Root hash check](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/ROOT_HASH_VERIFICATION.json): seven main reviewed root manuscripts match their accepted hashes.
- [Thread (2) detailed inventory](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/THREAD2_AUDIT.md) and [hash check](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/THREAD2_HASH_CHECK.json): 178 certificate/manifest-bound references match.
- [Thread (3) detailed inventory](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/THREAD3_AUDIT.md) and [hash check](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/THREAD3_HASH_CHECKS.json): all checked accepted files match; partial and full review scopes are separately recorded.
- [Thread (4) detailed inventory](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/THREAD4_AUDIT.md) and [hash check](/home/amir/Codes/PDE/studies/mean_field_peeling/four_thread_consolidation/THREAD4_HASH_VERIFICATION.json): 14/14, 40/40 and 19/19 entries match in its three packages.
- [Three-sample self-contained review record](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_self_contained/REVIEW_SUMMARY.md), [activation-class record](/home/amir/Codes/PDE/studies/mean_field_peeling/three_sample_activation_class/REVIEW_SUMMARY.md), [all-depth record](/home/amir/Codes/PDE/studies/mean_field_peeling/activation_class_all_depths/REVIEW_SUMMARY.md), [convex-offset record](/home/amir/Codes/PDE/studies/mean_field_peeling/convex_offset_all_depths/REVIEW_SUMMARY.md), [calibrated initialization record](/home/amir/Codes/PDE/studies/mean_field_peeling/calibrated_near_identity_reviews/REVIEW_SUMMARY.md), [practical L2 partial-scope record](/home/amir/Codes/PDE/studies/mean_field_peeling/practical_fixed_depth2/reviews/REVIEW_SUMMARY.md).

Saved task exports are adjacent to this document. A mathematical manuscript and its scoped accepted review take precedence over conversational shorthand, superseded progress messages, and filenames such as “global” or “full resolution.”

After assembly, the thread-(3) and thread-(4) synthesis agents separately checked this document against their accepted source scopes and found no substantive overclaims. A small range clarification in the convex-mixture depth obstruction was incorporated. This additional check concerns faithful consolidation, not a fresh full mathematical review.

# Source map for the reopened routes

This is a neutral locator supplement, not an assessment. Each row reports an
existing statement and its stated scope; no proof, experiment, significance
rating, or feasibility judgment was added. “Theorem” below describes the source's
claim type, not a new audit. Canonical chapter statements and study-owned
identities/numerical observations remain distinct.

Every locator is relative to this exact frozen root:

`/home/amir/Codes/PDE/data/generated/closure_historical_calibration/primary_packet/frozen/`

The root's manifest is unchanged. Use the frozen files, not newer live editions.
The common two-hidden-tanh convention is normalized input `u=x/√d`, stored
Gaussian variances `(1,1/n,1/n²)`, output `cᵀh²/n`, block mobilities `(n,1,n)`,
and unhalved probability-weighted square loss. Other models/losses below are
identified explicitly. “Global” population existence, fixed-horizon width
capture, convergence to a fitted endpoint, and uniform-in-time width capture
are different source assertions.

## Horizons and global population dynamics

| Exact source location | Existing scoped statement |
|---|---|
| `docs/global_nonlinear.md:32–176` | For one sample `x=y=1`, every separately fixed hidden depth `L≥3`, and `φ=1+arctan/10`, a global autonomous population flow exists and fits with loss at most `exp(−25t/9)`. Actual GF and raw GD with step `n⁻²` converge on each fixed finite horizon, including typed fields, kernels, paths and velocities. This is not a joint growing-depth/width or growing-horizon theorem. |
| `docs/global_nonlinear.md:1903–2011` | B.1 proves global two-hidden-layer dynamics for a fixed finite **orthogonal** input batch. First activation has bounded Lipschitz derivative; upper activation and its derivative are bounded, with Lipschitz derivative. Vanishing readout or a fixed bounded readout law is admitted. Summed square loss and `η_n√n→0` give the stated raw-GD limit. The orthogonality hypothesis is explicit. |
| `docs/global_nonlinear.md:2462–2572`; `:12594–12675` | C.1 gives a local fixed-depth C¹,¹ theorem for fixed general finite data, possibly singular input Gram, and every vanishing raw-GD step. C.4.7.10 A separately gives canonical two-hidden-tanh population GF through `T=1/200` for every Borel law on `√2S¹×[−1,1]`, with finite-GF and input-law identification. Neither statement supplies arbitrary-horizon correlated-data dynamics. |
| `docs/global_nonlinear.md:5270–5338` | The opposite-label orthogonal two-point tanh reference has a unique global population flow and a selected continuous whole-circle endpoint. The source gives risk decay `e^(−2t/5)` and uniform prediction approach at rate bounded by `17√10 e^(−t/5)`. The endpoint is defined by its actual feature flow stopped at its unique fitting feature time; it is not characterized as the unique interpolant. Nearby-law raw-GD robustness is separately fixed at physical time 40. |
| `docs/global_nonlinear.md:7066–7168` | At that fitted reference, actual finite-GF data derivatives are captured on each separately fixed horizon. The population homogeneous propagator is bounded uniformly for all `0≤s≤t`; the forced response bound is linear in horizon for bounded-TV forcing. The constant uses a finite endpoint pseudoinverse and is not numerically evaluated. Uniform homogeneous propagation is not an all-time nonlinear changed-law theorem. |
| `docs/global_nonlinear.md:13982–14059` | C.4.7.10 D extends canonical flow, closure and numerical convergence through time 40 for the specified near-axis family with `ρ=2^(−E10)`, `E0=8192`, `E(j+1)=2^Ej`. The fixed family and risk/activity assertions are explicit. This is a different law family from the resolved nonorthogonal short-time numerical family. |
| `docs/special_data_limits.md:2095–2154`; `:3518–3592,3718–3788`; `:17700–17792` | Other existing correlated-data global families include equal-label three-hidden-layer `1+arctan/10` at every fixed `−1≤ρ<1`; three separated samples at every fixed depth for the specified large-gain `a(1+z)+eψ` construction; and two separated samples with three hidden layers for `φ=az+eψ`, `e≤c_dyn δ^(31/8)`, with the stated shape bounds. Each has its own fitting and GF/GD conclusions. None is a theorem for arbitrary data and unmodified tanh. |
| `docs/linear_dynamics.md:34–148`; `docs/continuous_depth.md:1–40,342–404,2065–2154,2453–2475` | Global results also exist for the one-sample three-hidden **linear** model with order-one readout; a **scalar residual-particle** architecture with joint width/depth convergence; and a coherent dense **W/n kernel** model with fixed bounded endpoints. The sources explicitly distinguish these architectures/initializations from dense Gaussian W/√n feature learning. |

## Energy, Lyapunov identities, and continuation premises

| Exact source location | Existing scoped statement |
|---|---|
| `docs/finite_dynamics.md:21–166,167–227` | For the finite C² network, all mobility-weighted kernel blocks are positive semidefinite and the exact loss derivative is minus squared metric speed. Its integrated energy identity gives global finite-GF existence and compact-time parameter bounds. Under the stated derivative/initialization bounds, RMS/kernel bounds are width independent. The source explicitly says those RMS bounds do not replace population source identification or response stability. |
| `docs/global_nonlinear.md:12310–12377,15067–15108` | Fixed-order closure already has exact dissipation `L_N′=−||w_N′||²−||c_N′||²−||M_N′||F²`, polynomial-in-time raw bounds, and unique own-state restart. The latter passage explicitly proves existence through **every finite time at fixed order**. This is separate from convergence of increasing order to the actual network/population on an enlarged horizon. |
| `docs/finite_optimization_and_controls.md:38–74,202–267` | In the one-sample, three-hidden arctan model, Theorem 3.1 proves a persistent kernel lower bound, exponential physical-loss decay, and a finite parameter endpoint for zero or sufficiently small initial stored readout under its explicit nondegeneracy/norm conditions. These are finite-network conclusions for that model. |
| `docs/finite_optimization_and_controls.md:2002–2027`; `docs/special_data_limits.md:23293–23323,23391–23449` | Conditional continuation implications are already proved from cap-uniform exponential incoming-field tails. The former works on the supplied operator spaces; the latter treats its prescribed affine-plus-sine activation and obtains an Osgood cap-Cauchy bound and a strong population limit. The tail premise is explicitly unproved; the latter text also distinguishes the core population implication from completed finite-algorithm/observable bridges. |
| `docs/special_data_limits.md:23557–23618,23676–23746` | For bounded C² activations, along an existing strong path, readout and learned reverse-memory terms obey explicit bounds in accumulated residual mass. The initial reused-adjoint term remains. A selected-column Gaussian example disproves obtaining uniform tails from bounded query values, operator norm and exchangeability alone. It is explicitly not a counterexample produced by neural training. |
| `docs/special_data_limits.md:25709–25730,25899–25930` | An abstract causal smooth query program shows that the listed temporal H¹ and signed Gaussian-response controls alone do not bound transported ψ₁ norm. Separately, the tangent-energy identity has a negative `||Jv||²` term and a residual-weighted Hessian term; the latter has no raw-ball lower bound in the stated three-layer model. Neither counterexample is claimed canonically reachable. |

## Geometry and limits of metric or compactness arguments

| Exact source location | Existing scoped statement |
|---|---|
| `docs/finite_optimization_and_controls.md:2432–2516,2988–3058,3295–3396` | The three-hidden arctan model has a deterministic zero-readout reachable obstruction to the specified signed-Hessian material-derivative bound. Separately it has full tangent log-volume bounds. The exact hidden projection determinant contains an additional angle factor; full-volume control supplies no lower bound for that factor, projected nonsingularity, entropy, or adaptive Gaussian-response control. |
| `docs/special_data_limits.md:23497–23552` | For the specified affine-plus-sine activation on the ambient raw Hilbert space, the exact loss is not weakly lower semicontinuous, and positivity of the activation derivative does not give a locally Lipschitz or semiconvex raw gradient. These examples are not asserted to lie on initialized trajectories. |
| `docs/special_data_limits.md:24545–24584` | A distinct theorem concerns actual reached positive-time states: three hidden layers, two inputs with `−1≤ρ<1`, activation `1+arctan(sinh z)/10`, and summed loss. At every sufficiently small fixed positive feature time the scalar loss has unbounded second directional derivatives of both signs in raw unit directions. The raw gradient is not locally Lipschitz there, although the constructed local flow is unique. |
| `docs/special_data_limits.md:25027–25055,25979–26054,26230–26289` | For the three-input, three-hidden `φ=(1−e)z+e arctan z` model, ambient nonzero-loss stationary states in one raw ball have unbounded positive GF linearization eigenvalues. No smooth positive full-parameter metric gives one finite differential one-sided-Lipschitz constant on the entire ball. No canonical reachability is claimed. The same section separately excludes an exact common rowwise cancellation metric and the stated separable mirror/Bregman transplant. |
| `docs/special_data_limits.md:23706–23746` | For correlated two-input first-layer controls with positive gate, a C² point-coordinate map that simultaneously makes both arbitrary incoming-control fields constant exists globally only for affine activation (apart from the orthogonal case). This is an obstruction to that exact coordinate reduction, not to the population theorem itself. |
| `docs/finite_optimization_and_controls.md:2356–2409` | Integrated query approximation along a supplied actual path does not itself establish causal measurability of a compressed algorithm's queries, its stability, strong Hilbert compactness, or convergence of derivatives/hidden velocities. The source gives explicit norm and oscillation counterexamples, without claiming they are canonical trajectories. |

## Learned functions, nonlinear selection, and comparison with frozen features

| Exact source location | Existing scoped statement |
|---|---|
| `docs/global_nonlinear.md:17290–17477,17525–17595` | C.4.9 gives an autonomous, current-state constrained nonlinear selection equation after the fitted reference, for its fixed one-added-atom location/label rectangle. Original-initialization mixture GF is identified through physical time `τ0/ε` in width-first/then-contamination order; added-component risk and paired upper-hidden motion improve by positive amounts. The source excludes a final changed-law endpoint, a raw-GD extension and a simultaneous rate. Its control-clock source bound is independent of physical horizon under the stated small integrated perturbation premise. |
| `docs/global_nonlinear.md:19620–19746,20942–21037,21120–21185,21234–21312` | C.4.10 specifies an independent odd Fourier target family, full-circle density bounds and centered bounded noise. It proves finite-mode nonlinear excess-risk contraction toward a stated approximation floor, a class-determined positive stop, sample thresholds and finite-GF risk/paired-motion conclusions. The source does not assert universal consistency, `a_N²/λ_N→0`, arbitrary-accuracy fitting, an all-time endpoint, or superiority over another method. |
| `docs/global_nonlinear.md:21315–21477` | C.5 already proves strictly positive early-time test-risk advantage over frozen initial hidden features **at matched training loss** for the fixed three-point design and uniform-circle `cos(3α)` teacher. An enclosed positive cubic coefficient and actual-flow fourth-order remainder are supplied. The admitted time window/remainder constant are not numerically evaluated; the scope is local and fixed-design. |
| `studies/closure_circle_spectral_mechanism/THEORY.md:90–159,168–247` | Study-owned identities give exact antipodal oddness, arbitrarily high odd harmonics representable at fixed order, conditional N1/N2 equality under matched ridge and exact sign symmetry, the changing PSD three-block kernel, and `f−f_frozen=O(t³)` on a fixed finite query panel. Representability does not establish reachability; the cubic coefficient need not be nonzero. The finite mark span is not generically rotation closed. |
| `studies/closure_circle_spectral_mechanism/INSIGHT.md:65–108,141–149` | The tanh–sine family is a fit to already learned outputs, with held-out directions from those outputs. The report explicitly leaves the dynamics selecting κ unresolved and does not identify an endpoint variational principle or off-training teacher accuracy. Quadrature and rotation-control qualifications remain recorded. |

## Approximation and computation

| Exact source location | Existing scoped statement |
|---|---|
| `docs/global_nonlinear.md:12084–12128,12555–12675,13481–13522` | A finite autonomous population closure already converges on its stated short-time domain in whole-circle/time prediction and designated W₂ observations. The numerical implementation has the ordered limits precision → time mesh → input quadrature → population quadrature → initializer quadrature → source regularization → closure order. No convergence rate, arbitrary diagonal, per-run certificate or tolerance-to-resolution schedule is asserted. |
| `docs/global_nonlinear.md:15109–15151` | The existing closure proof controls both omitted initialized-action directions and the filtered learned-increment source uniformly over compact sets of the actual time-40 trajectory. Those omitted-source quantities are proof errors; none is supplied to the equations, initializer or order-selection rule. |
| `docs/global_nonlinear.md:15553–15628` | The time-40 implementation already retains an exact supported-law descriptor, accounts for finite-precision radius collapse, and has fixed-resolution scalar state count `P1(d1+5)+P2(d2+2)+2d1d2`, plus `4A` law scalars. It carries no raw neuron-by-neuron middle matrix. The supported radius is not promised practically resolvable. |
| `docs/gaussian_calculus.md:1749–1823,3672–3732,4050–4168` | Existing obstructions concern a full same-norm algebra containing an unbounded atom; unrestricted positive coefficientwise derivative-jet norms; and prescribed positive Taylor closures in a raw-square, order-one-readout formal-jet model. Those Taylor losses are not uniformly Cauchy on intervals containing zero. The source explicitly leaves other signed/non-Taylor descriptions untouched and shows that zero Taylor radius alone does not exclude a smooth finite-dimensional ODE. |
| `studies/first_order_dimension_mnist/INITIALIZATION_THEORY.md:1–203`; `studies/first_order_dimension_mnist/MODEL_SCOPE_CHECK.md:55–112` | Study-owned general-d first-order initialized coefficients reduce to scalar/two-dimensional Gaussian quantities; the actual reverse-response term and full evolving M remain. Exact antithetic folding preserves the specified paired rule. Moving-state size is `O(Pd+d²)`; complete retained/cached counts and per-input work are recorded. Finite quadrature, `P=n`, and fixed p=1 do not establish general-d trained-network convergence or uniform savings when d grows with n. |
| `studies/first_order_dimension_mnist/PCA_REPORT.md:44–82,166–187` | Existing computation measurements include crossed-device fixed-T100 benchmarks: PCA closure/PCA network speed ratio 3.75–3.96 and 80.20% less peak live allocated memory. These are finite implementation measurements with the recorded steps and one digit pair; no asymptotic speed factor or high-dimensional convergence theorem is asserted. |
| `studies/wide_network_closure_comparison/LONG_20260914_REPORT.md:1–37,52–64`; `studies/closure_endpoint_discrimination/README.md:104–154` | Existing longer runs reach T640 and a last complete common T1000 comparison, respectively. The former fails 314/416 strict settling checks and retains quadrature uncertainty. None of the latter's 18 trajectories passes its plateau rule; specified numerical thresholds also fail and T1100 is incomplete. These are numerical observations, not endpoint or all-time convergence theorems. |

## Read coverage and remaining scope

This was a targeted statement/limitation search, not a full-book proof review.
Headings were searched in the nine frozen canonical Markdown files; two large
discovery outputs were truncated, and the relied-on statements were reread in
bounded extracts. No inference is based on a missing fragment. Complete frozen
files remain available to the coordinator. No source implementation was run or
new numerical data opened. Substantive extracts inspected for this map were:

- `docs/global_nonlinear.md`: 1–178, 1140–1210, 1750–1798, 1903–2011,
  2462–2572, 5270–5338, 7066–7168, 12084–12128, 12310–12377,
  12555–12675, 13481–13522, 13982–14059, 15067–15151, 15553–15628,
  17290–17492, 17525–17595, 19620–19750, 20942–21037, 21120–21185,
  21234–21312, 21313–21478. The 5475–5595 discovery extract was partially
  truncated and is not a relied-on read-coverage claim.
- `docs/finite_dynamics.md`: 21–227.
- `docs/finite_optimization_and_controls.md`: 38–74, 202–270, 2002–2057,
  2356–2409, 2432–2516, 2988–3058, 3295–3396.
- `docs/special_data_limits.md`: 1–155, 2095–2154, 3518–3592, 3718–3788,
  17700–17792, 23293–23323, 23391–23449, 23497–23552, 23557–23618,
  23676–23746, 24545–24584, 25027–25090, 25709–25730, 25899–25930,
  25979–26054, 26230–26289, 27238–27274 (file EOF).
- `docs/gaussian_calculus.md`: 1749–1823, 3672–3732, 4050–4168.
- `docs/linear_dynamics.md`: 34–148, 139–185.
- `docs/continuous_depth.md`: 1–41, 342–404, 2065–2154, 2453–2475.
- `studies/first_order_dimension_mnist/INITIALIZATION_THEORY.md`: 1–203;
  `MODEL_SCOPE_CHECK.md`: 55–112; `PCA_REPORT.md`: 44–82, 166–187.
- `studies/closure_circle_spectral_mechanism/THEORY.md`: 90–247;
  `INSIGHT.md`: 65–108, 141–149 (file EOF).
- `studies/wide_network_closure_comparison/LONG_20260914_REPORT.md`: 1–37,
  52–64; `studies/closure_endpoint_discrimination/README.md`: 104–154.

Missing input: none needed to locate the statements above. Unread proof bodies,
dependencies and other chapter sections were not freshly audited. This map is
not an exhaustive assertion that no other relevant result exists. Prior/current
assessment, grade, advocacy and debate documents were not opened. Only the
coordinator receives this source map from the curator.

# Practical nonlinearity and global compact-time limits

2026-09-08. This is a research assessment, not a new global training theorem. It incorporates three independent bounded assessments of the existing proof, depth scaling, and residual-network literature. No experiments were run and no existing manuscript was changed.

## Recommendation and target

Prioritize a new compact-time continuation argument at fixed hidden depth L=2 for a prescribed, moderately nonlinear activation, then extend to L=3. Do not make improved separation-dependent perturbation constants the main target. In parallel as a subsequent research direction, distinguish a variance-calibrated Gaussian deep network from a true residual network: their natural accumulation scales differ.

The desired theorem is a single global, autonomous population gradient flow, with uniqueness and continuation from reached states, and identification with the actual finite-width gradient flows on every finite training interval. Preserve the original Gaussian initialization, raw metric, trained blocks, and named joint observables in the fixed-depth route. Constants in estimates can depend on T, L, the activation and dataset. The activation must be chosen once, independently of T and width. A theorem selecting a smaller activation perturbation each time T increases would not answer the question. Exponential fitting, a positive kernel floor for all training times, and a finite total residual clock are additional properties, not requirements for this target.

The initially practical objective should use one explicit activation with fixed coefficients of moderate size. The conjecture is that its compact-time limit theorem may hold without a separation-dependent activation cutoff. This is open; it is not implied by the existing results. Input separation can remain in the contract while testing whether the proof actually needs it.

## What the existing constants mean

The L=3 activation-class proof uses an augmented affine Gram lower bound of order delta squared, converts it into a fitting/residual-clock bound, and then controls perturbations of the entire trained path. The order delta squared is sharp for that particular geometric lower bound. A later source estimate introduces the sufficient cutoff

    e <= [2 K_* exp(K_* S)]^(-1),

with K_* itself obtained through a large chain of bounds. These losses do not show that the desired finite-horizon limit fails at a larger nonlinear amplitude.

Sources: ../three_sample_activation_class/MANUSCRIPT.md, lines 329–342, 1745–1754, 1816–1858, and 2031–2085.

The latest all-depth gain theorem already avoids a tiny absolute e. It permits e=1 and chooses

    T0 = 192/delta^2,
    a = max{10^12(1+T0), (2^36 T0^2/sqrt(c_psi))^(2/5)}.

For fixed shape, a has order delta^(-2) as delta tends to zero. Thus the relative perturbation e/a has polynomial, rather than nested-exponential, asymptotic dependence. The numerical constants remain extremely restrictive: the first gain requirement alone gives e/a < 5.3e-17 at delta=0.1 and < 5.3e-21 at delta=0.001 when e=1. This is a sufficient construction, not an optimality result.

Source: ../activation_class_all_depths/RESULT.md.

An absolute positive nonaffinity margin does not measure substantial relative nonlinearity. Indeed

    inf_{b,c} E[phi(Z)-b-cZ]^2 = e^2 inf_{b,c} E[psi(Z)-b-cZ]^2

for phi(z)=a(1+z)+e psi(z). The affine gain disappears from the numerator. For centered Gaussian Z of standard deviation sigma>=1 and the normalized shape class, the numerator is at most e^2, while the denominator E phi(Z)^2 is at least (a-e)^2 sigma^2, by projection onto Z and Gaussian integration by parts. The relative regression fraction is therefore at most 4e^2/a^2 for a>=2. A nonzero hidden velocity or changing kernel also does not by itself exclude a deep affine explanation.

For a deep construction, the practical test should concern the cumulative input-to-feature map or normalized feature geometry against an affine comparator. Requiring each individual near-identity layer to have an order-one nonlinear fraction would contradict the intended mechanism. Fitting three training values alone does not certify a nonlinear function: three distinct points on a sphere are affinely independent. Function-level tests should use a specified larger input set or probe distribution.

## The highest-leverage fixed-depth obligation

For any existing true finite-width gradient flow of the nonnegative squared loss E_n, the exact raw-metric energy identity gives

    integral_0^T ||dot Theta_n||_raw^2 dt <= E_n(0),
    sup_{t<=T} ||Theta_n(t)-Theta_n(0)||_raw <= sqrt(T E_n(0)).

These estimates need neither separation nor a kernel lower bound. Together with smooth finite-dimensional local existence they rule out finite-time escape at each width. The small random initial readout is retained; E_n(0) tends to 3/2 for the three binary labels.

Passing to the canonical infinite-dimensional flow is the unresolved part. Bounded raw energy does not imply strong compactness. Differentiating a backward gate produces psi''(z)q, with q controlled in L2 but not necessarily in L-infinity, so the true gradient need not be locally Lipschitz on an ambient L2 ball. Neither obstacle is a counterexample for actual reached neural states.

A sufficient first lemma would give cap-independent tails for the actual physical-feedback incoming fields, initially at L=2 and stopped within a fixed raw ball:

    sup_{R,t<=T,i,l} ||q^l_{R,i}(t) 1_{|q^l_{R,i}(t)|>u}||_2
        <= C_{T,M} exp(-c_{T,M} u^2).

Here M is the stopping radius and R the backward cap. The activation remains fixed as T and M vary. This is an unproved sufficient condition, not a necessary form of a successful proof; a direct Cauchy estimate or suitable Osgood stability modulus could replace it.

The existing reference-only cap comparison produces a stability factor exp(C_{T,M} R), which these tails would dominate. The cap error in the true gradient would vanish as well. For a capped direction G_R approximating the true gradient G, the identity

    dE/dt = -<G,G_R> = -||G_R||^2 - <G-G_R,G_R>

would then provide approximate energy control on the stopped ball. Choosing M strictly larger than the resulting compact-time displacement would remove the stop. This explains why a physical, finite-horizon estimate could bypass the old fast-fitting route. The remaining finite-width and observation bridges would still require verification for the chosen activation; this assessment does not declare them proved.

Uniform estimates for arbitrary bounded control signals are not an adequate replacement: the scalar affine ascent system w'=AC, A'=wC, C'=Aw has w=A=sec(s), C=tan(s), which blows up at s=pi/2. It satisfies a bounded prescribed ascent control but not physical squared-loss dissipation. A new proof must retain the actual feedback or otherwise exploit the true gradient structure.

Sources: ../three_sample_near_identity_all_depths/ENERGY_GALERKIN_ROUTE.md; ../three_sample_near_identity_all_depths/SOURCE_ROUTE.md; ../activation_class_all_depths/BRIDGE.md, V.2.

## Why the two depth mechanisms differ

A true residual layer is

    h_{l+1} = h_l + (beta/L) F_l(h_l).

Its Jacobian is I+(beta/L) DF_l; a uniform derivative bound M yields a product norm at most (1+beta M/L)^L <= exp(beta M). Coherent nonlinear terms can accumulate at first order. For the scalar example with every F_l=tanh, the continuous-depth equation dh/ds=beta tanh(h) has solution

    h(1) = asinh(exp(beta) sinh(h(0))).

The formula follows by differentiating sinh(h): its derivative is beta sinh(h). The map is nonaffine for beta>0: its derivative is exp(beta) at zero and tends to one at infinity. The discrete layers converge to it by the elementary Euler estimate for a bounded Lipschitz vector field. This example proves a forward composition mechanism, not a trained-network limit.

The original dense Gaussian layer instead has h_{l+1}=phi_L(W_{l+1}h_l). Its Jacobian is Dphi_L(W_{l+1}h_l)W_{l+1}; making phi_L close to identity leaves the independent Gaussian matrix. It does not give I+O(1/L).

There is a useful exact initialization calculation. Let phi_e(z)=z+e psi(z), where psi and psi' are bounded, and let the centered Gaussian preactivation covariance be Q=qC with C_ii=1. Define

    a(q)=E psi'(sqrt(q)G),
    B_ij=E[psi(Z_i)psi(Z_j)],  b=B_ii.

Gaussian integration by parts gives E[Z_i psi(Z_j)]=Q_ij a(q), including singular covariances by conditioning or Gaussian approximation. Expanding the product therefore gives

    Q^+ = (1+2e a(q))Q + e^2 B,
    C^+ - C = e^2 (B-bC)/q^+.

The first-order term changes only the common scale; normalized geometry changes at second order. For e=beta/L and fixed beta, the required variance bounds follow directly. If ||psi'||_infinity<=1 and e<=1/2, projection onto G gives q^+>=(1-e)^2 q, while sqrt(q^+)<=sqrt(q)+e||psi||_infinity. Over L layers, starting from q=1, these imply

    exp(-4 beta) <= q_l <= (1+beta||psi||_infinity)^2.

Since |B_ij-bC_ij|<=2||psi||_infinity^2, summing the exact normalized increments gives

    max_ij |C_L,ij-Gamma_ij|
       <= 2 beta^2 ||psi||_infinity^2 exp(4 beta)/L.

Thus this 1/L scheme loses its new normalized initialization geometry in the depth limit. This says nothing conclusive about later trained dynamics.

An affine offset illustrates the cancellation without any estimates: phi_L(z)=z+beta b/L gives Q_L=Gamma+(beta^2 b^2/L)11^T under fresh centered Gaussian mixing. The offset does not coherently accumulate to beta b.

## A variance-calibrated candidate within the Gaussian architecture

Second-order accumulation suggests e_L=beta/sqrt(L). A variance correction is essential because the first-order scale drift otherwise accumulates too. An explicit candidate is

    a0 = E[G atan(G)],
    r(z) = atan(z)-a0 z,
    v = E[r(G)^2] > 0,
    e_L = beta/sqrt(L),
    phi_L(z) = [z+e_L r(z)]/sqrt(1+e_L^2 v).

Here E[G r(G)]=0, and v>0 because atan is not a linear function. The activation is near identity in its derivative and on bounded intervals as L grows. The perturbation r has at most linear growth and bounded derivatives; it is NOT a bounded perturbation in value. This is a new depth-dependent activation class, not the earlier literal convex combination or a renormalization of the proved large-gain network.

At initialized variance one, the cross term vanishes, so E phi_L(G)^2=1 exactly. Define R(c)=E[r(G_1)r(G_2)] for standard Gaussians with correlation c. The initialized correlation recursion is exactly

    c^+ = [c+e_L^2 R(c)]/(1+e_L^2 v).

Consequently, with depth fraction s=l/L, the elementary Euler limit is

    dc/ds = beta^2 [R(c)-v c].

For completeness, R is Lipschitz: Gaussian covariance differentiation and bounded r' give |R'(c)|<=||r'||_infinity^2 in the interior, with continuous extension to the endpoints. The recursion differs from the Euler step for the displayed Lipschitz vector field by O(L^(-2)), uniformly on [-1,1]; the product error estimate gives uniform convergence on s in [0,1]. Correlations remain in [-1,1] because every discrete update is a Gaussian feature correlation.

The limiting generator is nonlinear. Oddness gives R(0)=0, covariance differentiation gives R'(0)=(E r'(G))^2=0 because E r'(G)=E[G r(G)]=0, and R(1)=v>0. Therefore R is not an affine function. The cumulative budget beta^2 v can be chosen of order one independently of delta; each layer's perturbation still tends to zero. These are initialization facts only. They do not establish a global trained flow, uniform trained nonlinearity, or a joint width-depth training limit.

This candidate is a more mechanism-matched second direction than simply choosing beta/L in the old Gaussian composition. Start with the width limit at each fixed L. A later trained depth limit must separately analyze training-time scaling, uniform tails, and all requested observables; a family of fixed-L theorems does not imply an L(n) theorem.

## Training and literature boundaries

For a residual branch multiplied by 1/L, the corresponding parameter derivative is of order 1/L under uniform state/sensitivity bounds. With L independently parameterized branches and an unaveraged sum metric, their total kernel contribution is then of order 1/L. A nontrivial branch-training limit generally requires a depth normalization of the metric or learning rate. This must be stated as part of a new architecture, including how the readout is treated. It cannot be silently imported into the original raw training theorem.

The workspace already contains a distinct scalar residual-particle manuscript, ../residual_continuous_depth_gradient_flow/RESNET_MEAN_FIELD_IDE_THEOREM.md. It uses bounded effective parameters, particle averaging 1/(nL), and training multiplier nL. Its claimed theorem concerns that model, not dense Gaussian matrices; it has not been re-audited in this assessment.

One independent reader also read all 65 pages of Ding, Chen, Li and Wright, *Overparameterization of Deep ResNet: Zero Loss and Mean-field Analysis*, JMLR 23(48), 2022: https://jmlr.csail.mit.edu/papers/volume23/21-0669/21-0669.pdf. The relevant methodological ideas are forward/adjoint depth stability and characteristic-flow continuation. Its actual theorem uses residual particle averaging, an accelerated training flow, decaying quadratic regularization, and a regular depth-process initialization. Its finite-horizon probability statement is pointwise at each training time, rather than explicitly a supremum event. It is therefore a methodological reference, not an invocation proving our target. External dependencies were not recursively certified, and no theorem from it is adopted here.

## Claim ledger and next decision

| Claim | Status in this assessment |
|---|---|
| Earlier sufficient amplitude is practically tiny | Supported by exact published local selection rules |
| Latest gain theorem has polynomial separation dependence but huge constants | Exact reading of its selection rule |
| Physical finite-width energy bounds do not require a kernel floor | Exact identity |
| Energy alone gives the canonical population and full-width limit | Not established; compactness/stability gaps remain |
| Fixed moderate activation can satisfy the desired global compact-time theorem | Central open conjecture |
| Coherent scalar residual 1/L layers can accumulate nonlinearity | Elementary forward example above |
| Ordinary Gaussian near-identity 1/L layers automatically do so | False for the initialized normalized geometry under the stated bounded-shape assumptions |
| Calibrated 1/sqrt(L) candidate has a nonlinear initialized depth limit | Elementary calculation above |
| That candidate has the desired global trained theorem | Open |

The next decisive proof attempt should isolate the stopped, physical-feedback compact-time tail/Cauchy estimate at L=2 for one fixed moderate activation. Success would address the central population-limit obstruction without buying it through fast fitting. If architecture changes are preferred, freeze a residual model and its training metric together before beginning a separate proof. Neither branch requires an experiment to state or test its first theoretical obligation.

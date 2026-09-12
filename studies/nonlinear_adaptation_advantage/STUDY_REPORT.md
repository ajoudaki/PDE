# E₀: current verdict and exact unresolved obligation

E₀ is **unresolved**. This study has not proved a common positive nonlinear
advantage, a beneficial component effect beyond scalar speed, or a positive
actual-network comparison. It has not disproved them either. Three fresh
independent approaches produced exact comparison results and concrete
obstructions to several proposed proof methods. A targeted readout/layer-balance
follow-up was also completed and internally checked; it leaves explicit signed
terms uncontrolled. The continuation now supplies an explicit finite-time
kernel-derivative drift bound, removing the initial remainder-modulus gap.
The required actual-neural signs remain open. No training experiment was run.

The decisive missing result concerns the actual reached tanh geometry, not
existence of the selected episode or sampling consistency. The comparison
identities below make that gap explicit; assuming their favorable sign would
rename the desired theorem rather than solve it.

## Exact scope

The study retains C.4.9–C.4.10's bias-free two-hidden-layer tanh model,
stored Gaussian variances (1,1/n,1/n²), block mobilities (n,1,n), output
division by n, unhalved square loss and actual GF. The full first row, reused
Gaussian middle action, actual adjoint and finite random initial readout are
retained. Every actual run starts at its original initialization and trains
throughout on its fixed mixture with exactly weighted known anchors.

The selected population episode starts at the fitted reference only through
the proved singular limit on tau=epsilon t. C.4.10 supplies a common T_c>0
for all bounded added laws. Its actual-network identification is width first
at each fixed contamination and law, contamination second, sample last.
The frozen comparator uses all projected raw tangent directions at this
fitted reference. It has the same starting prediction, data, metric and clock.
It is neither a readout-only learner nor the tangent kernel at initialization.

The exact task contract is [RESEARCH_CONTRACT.md](RESEARCH_CONTRACT.md).
The complete source/read record and executed upstream check are in
[SOURCE_AND_CHECK_RECORD.md](SOURCE_AND_CHECK_RECORD.md).

## Main comparison results

Fix the common prediction space H=L²(p rho), restricted to odd functions
where convenient. Define D_t a=integral a(u)Pi_(theta_t)g_(theta_t)(u)p d rho
and K_t=D_t*D_t. This K_t is a prediction operator, distinct from the raw
middle-layer increment. Let r_t=P_nu(t)-q, r0=F_*-q and
z_t=exp(-2tK_0)r0. The actual selected and full frozen equations give exactly

    r_t'=-2K_t r_t,       z_t'=-2K_0 z_t,
    W_T=integral_0^T exp(-2(T-s)K_0)(K_s-K_0)r_s ds,
    r_T=z_T-2W_T,
    E_nu(F_fr(T))-E_nu(P_nu(T))
        =4<z_T,W_T>_p-4||W_T||_p².                          (S1)

All nonlinear changes and residual interactions remain in W_T. All three
independent routes derived this identity. Its quadratic penalty has an adverse
sign. Neither a nonzero W_T nor a nonproportional K_t proves a benefit.

The reached-curve derivative estimates, including the actual adjoint and
anchor projection, give a finite reference-dependent constant

    J=A_s T_g(1+4L/sqrt(k)),      Gamma=2LJ,

with the constants of C.4.10.2, such that on the already proved episode

    ||K_t-K_s||<=Gamma|t-s|,
    ||P_nu(T)-F_fr(T)||_p<=Gamma||r0||_p T²,
    |E_nu(F_fr(T))-E_nu(P_nu(T))|<=2Gamma||r0||_p² T².        (S2)

These are actual finite-time estimates, with no assumed neural Taylor radius.
They are unsigned. Both learners have identical initial risk derivative
-4||D_0 r0||². For a finite-cap family with endpoint conditioning lambda>0,
the nonlinear learning gain is at least 2lambda||r0||²T when
T<=min(T_c,lambda/(4L^4+Gamma)). Thus any possible advantage obeys

    |advantage| / nonlinear learning achieved <= Gamma T/lambda. (S3)

This discloses the scale of an early-stop argument: shrinking time makes the
possible extra benefit small relative to learning. It supplies no positive
fraction at any stop. The source/conditioning constants remain unevaluated;
the inherited source estimates already contain exp(2880).

Full arguments: [ROUTE_ENERGY.md](ROUTE_ENERGY.md), §§3–4, independently
reconstructed in [ROOT_ROUTE_CHECK.md](ROOT_ROUTE_CHECK.md).

## Structurally ordinary families were fixed, not selected by performance

The routes chose separate families before deriving a favorable sign. None
was shrunk or redesigned in response to a measured advantage. All have
full-circle support and quantitative exclusion of stationary initial residuals.

| Route | Independently varying structure | Declared robustness | Result |
|---|---|---|---|
| G | s=1, N=1; a0,b0 in [R/16,R/8], a1,b1 in [R/48,R/24], R fixed in (0,1/8] | Odd factorized Lipschitz target radius R/2048; density uniform-plus-Lipschitz radius 1/4 about 1 | Active actual fifth/seventh target harmonics and nonstationarity; advantage sign open |
| H | Frequencies 1 and 11 in both swap sectors; two symmetric amplitudes independently in [a,2a], a=1/768, with independent antisymmetric coefficients | Weighted coefficient radius a/64; explicit small density radius relative to a | Two separated active bands with positive normalization denominators; advantage sign open |
| E | Four frequency-1/3 coefficients, with fixed positive fundamental coefficients and opposite third-harmonic signs | Weighted coefficient radius R/256 and explicit relative C1 target radius; density uniform-plus-Lipschitz radius 1/4 | Quantitative finite-space conditioning and total learning; advantage sign open |

G's actual fifth-harmonic coefficients have magnitude at least 15R/1024;
its seventh-harmonic coefficients have magnitude at least 13R/3072, even
after the stated target perturbation. Its initial risk is at least

    (3/4)R²[(5/96)sqrt(3/8)-1/2048]²>0.

The full ranges, topology qualifications, density/noise bounds and proofs
are in the original route reports. These are substantial candidate families,
not proved advantage families. Their robustness of activity and nonstationarity
must not be confused with robustness of an unproved positive comparison.

## What the mechanism analysis establishes and leaves open

The geometric route gives an explicit constrained-curvature cubic C_p(r0),
including derivatives of every parameter block and the anchor projector:

    <r0,K'_0 r0>_p=-4 C_p(r0),
    advantage(T)=-8 C_p(r0)T² + controlled remainder.          (S4)

The complete formula is G12–G13 in
[ROUTE_GEOMETRY.md](ROUTE_GEOMETRY.md). Its readout/hidden cross term,
tanh curvature terms and anchor correction have no certified combined sign
on the ordinary families. The relevant swap symmetry cancels the pure
symmetric cubic; it leaves a mixed antisymmetric–symmetric term whose sign
is also unknown. The nonstationarity proof does not determine it.

The targeted follow-up
[GEOMETRY_SIGN_FOLLOWUP.md](GEOMETRY_SIGN_FOLLOWUP.md) tests whether the
positive hidden-motion square in readout acceleration resolves that sign.
It does not: even in the pure symmetric diagnostic, the exact second
derivative of the readout norm is

    (||c||²)''(0)
      =8[||b||²-(H_mu[b,g_B]+H_B[b,b])/B_s],                (S4a)

where b is the full projected residual force, B_s=||g_B||²>0 is reference
anchor-contrast conditioning, and H_mu and H_B are the signed-residual and
anchor-contrast directional Hessian forms. Both remaining contractions are
uncontrolled and have the same order as the positive square. This diagnostic
is not an admissible replacement of the fixed ordinary target family by a
target defined around F_*.

The follow-up also proves exact tanh saturation balances using a finite
renormalized middle-action increment, preserving the reused initialized
Gaussian action and its actual adjoint. The scalar saturation defect has a
known sign relative to its preactivation, but the balance integrates it against
different correlated fields and a signed control measure. Consequently these
balances supply no risk or component sign. Conditional next-derivative
identities likewise retain a same-order signed curvature term; the needed
extra derivatives and evaluated remainder are not claimed. The complete
internal balance check is [INTERNAL_BALANCE_CHECK_H.md](INTERNAL_BALANCE_CHECK_H.md).

Two independently interpretable controls were supplied:

- G removes the prediction-space projection of K'_0r0 onto K_0r0, the
  one-dimensional scalar-clock direction, and measures coarse/fine target
  error using fixed orthogonal subspaces in L²(p rho). Its finite remainder
  formulas retain all interactions. The continuation now bounds their
  derivative drift modulus explicitly as described below. No favorable
  component sign is proved.
- E provides a finite scalar-clock exclusion criterion, allowing every
  cumulative clock s in a stated budget [0,S], with
  T<=S<=lambda/(8L0^4). Orthogonal projection off the frozen velocity
  leaves an explicit O(T^4) remainder. It would separate a sufficiently
  large transverse effect from scalar timing, but that transverse lower
  bound and its beneficial component sign are unproved.

These controls interpret the matched-clock base comparison. They do not
claim superiority to arbitrarily accelerated frozen learning. Layer attribution
remains to the full nonlinear constrained evolution; the formulas do not
isolate a specifically middle-layer benefit.

The continuation [QUANTITATIVE_CURVATURE_DRIFT.md](QUANTITATIVE_CURVATURE_DRIFT.md)
uses the retained Gaussian source history to prove a fourth-moment bound for
upper directional preactivations generated by full gradient combinations.
This permits scalar-Hessian subtraction on the actual reached flow and gives

    ||K'_t-K'_s||op <= Lambda_1 |t-s|,
    |advantage(T)+8 C_p(r0)T²|
       <=R0_bound² T²[(2Lambda_1+8L²Gamma)T+Gamma²T²],       (S4b)

where R0_bound=sqrt(10)+1 and every constant has a finite formula in the
established source/reference bounds. All projector and residual variations
are included. Two complete internal checks independently reconstructed the
proof. This supersedes the initial report's unevaluated G20 time modulus;
it assumes neither K'' nor a positive Taylor radius. The source constants
themselves remain unevaluated and the resulting bound can be impractical.

A future uniform certificate C_p(r0)<=-c_*<0 would therefore imply a
matched-clock margin 4c_*T² at the explicit stop in Q14. A beneficial
component coefficient must still be separately established; inserting the
new modulus into G24 retains that control's clock and normalization conditions.
The further [reference-specific sign attempt](REFERENCE_SIGN_ATTEMPT.md)
rewrites the actual disputed contractions using the full anchor-fitting
history but supplies neither sign. Its demonstrated failure concerns the
absolute estimates used in that argument, not the actual neural comparison.

## Proof methods ruled out, with their exact scope

1. **Independent ordinary Fourier learning rates.** The full projected
   kernel vanishes at the anchors and is injective on odd residuals. If it
   preserved a single odd sine/cosine plane, its image in that plane would
   vanish at both anchors and hence be zero, contradicting injectivity.
   Ordinary frequencies therefore mix already in the full frozen comparator.

2. **Symmetry, positive semidefiniteness and nonproportional movement alone.**
   H constructs two auxiliary, anchor-preserving, symmetry-respecting
   positive kernel paths K0±tB. For one fixed ordinary multicomponent task
   their finite-time risk differences have opposite signs with an explicit
   cubic remainder. Neither path is claimed to be the neural path.

3. **Kernel enlargement alone.** E gives a complete two-dimensional example
   with moving kernel always at least the original kernel in positive-operator
   order, yet higher finite-time risk. Noncommuting changes move residual
   into slower directions. This defeats a general proof rule, not E₀.

4. **A frozen approximation floor.** The endpoint force is injective on the
   odd prediction space. An elementary dense-range/contraction proof shows
   frozen risk tends to zero on every such task. On compact finite-cap
   target/density classes it does so uniformly as time grows. No practical
   rate is obtained. A possible E₀ advantage must have a finite-clock scope.

These results distinguish failure of a method from failure on a task family
and from an impossibility theorem. No admitted actual-neural family has been
proved to fail, and there is no obstruction to E₀'s existence claim here.

## Sampling and actual-network transfer

[COMPARISON_TRANSFER.md](COMPARISON_TRANSFER.md) proves, using exactly the
same iid added observations and bounded centered noisy labels for both learners,
an explicit high-probability error bound of the form

    empirical population-risk gap
       >= population gap -alpha_m-2B0 beta_m-beta_m²,
    alpha_m=2(c_b+1)L O_T(C_N/sqrt(m)),
    beta_m=L0 C_F/sqrt(m).                                  (S5)

The constants, four failure allowances and their noiseless specialization
are given there. Positivity of empirical frozen covariance makes its raw
error propagator contractive, including repeated samples. The nonlinear
side uses the established source-bearing comparison, with all random forcing
evaluated on its deterministic population path. A union bound needs no
independence between the learners.

If a separate population theorem supplied a>0 at T<=T_c, formula (12) in
that note gives a sample threshold preserving margin 3a/4 at confidence
1-delta. The width-first, contamination-second actual nonlinear GF transfer
then preserves a/2 for each separately fixed member; sample growth is last.
This is a proved **conditional bridge**. There is no positive a to insert
from this study, so it is not an unconditional E₀ sampling theorem.

The exact empirical frozen comparator has a finite Gram representation given
exact fitted-reference kernel queries. A deterministic bound quantifies error
from approximate kernel/reference inputs. A finite Gaussian realization or
efficient computation of those inputs is not asserted. No unproved finite
network endpoint is substituted for theta_dagger.

## Claim status and milestone E

| Required E₀ obligation | Verdict |
|---|---|
| Common nonlinear episode, original initialization and exact model | Available from established C.4.9–C.4.10; preserved |
| Ordinary robust multicomponent candidate family | Supplied, with quantitative activity and stationary exclusions |
| Uniform positive matched-clock population margin | **Open** |
| Beneficial relative component learning beyond scalar gain | **Open** |
| Finite-time derivative drift and interaction remainder | Explicit formulas internally checked; conditioning not numerically enclosed |
| Positive evaluated stop and complete sign/remainder certificate | **Open**: favorable signs and their positive constants missing |
| Shared-sample positive risk margin | Conditional on the missing population theorem |
| Actual finite nonlinear GF advantage | Conditional, with the required iterated order |
| Finite Gaussian frozen comparator approximation | Not claimed; separate obligation |
| Successful canonical promotion package | Not prepared: no successful E₀ theorem |

E₀ remains a useful intermediate question for milestone E, but this study
does not advance E to a proved discovery or resource advantage. B's useful
learning and hidden motion are compatible with an equally capable full
frozen tangent model. The next substantive obligation is a signed property
of the *actual constrained tanh evolution* predicting which ordinary task
components receive beneficial reweighting, with enough finite-time control
to dominate interactions. Increasing a Fourier cap, restating conditioning,
or proving more unsigned continuity does not close it.

The unresolved obligation can be stated without any Taylor expansion: prove
uniformly on a declared ordinary robust family that the actual W_T in (S1)
satisfies <z_T,W_T>_p-||W_T||_p²>=a/4, and separately certify beneficial
relative component recovery after an independently defined scalar-clock
control, with finite interaction bounds. The routes give neither inequality.
This is a failure to resolve the requested existence question after substantive
alternative approaches, not a failed empirical test or an impossibility result.

The continuation changes the technical outlook narrowly: finite-time control
is now available in explicit source/reference constants once signed endpoint
coefficients are known. The unresolved population obstacle is their actual
neural sign and beneficial relative-component interpretation. That distinction
keeps milestone E's discovery/resource questions separate from a regularity
problem that no longer needs to be assumed away.

No initialized-NTK superiority, unknown-structure discovery, trained-shallow
separation or resource-efficiency conclusion follows. No established book or
code was changed. The paired promotion reviews and integration/user-approval
gate would become applicable only to a concrete successful addition; no
permission request is needed to retain these scoped study results.

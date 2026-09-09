# Independent scope audit of the three-input threshold report

2026-09-08. This is an audit of partial results and claim scope, not a certificate for a full three-input population theorem.

## Material inspected

- `studies/mean_field_peeling/three_sample_odd_activation_threshold/REPORT.md`, SHA256 `d52e54a992b0a8637643875d5df139f846d4ee1033f2a58a85ce4403b5019ae4` at initial review.
- Its `CONTRACT.md`.
- `/tmp/three_geometry_sharpness_20260908.md`, SHA256 `08768e8c190e0e428efe978fa751b35b7444d327364c7bd393a2e9af9eee2fa9`.
- `/tmp/three_direct_source_20260908.md`, SHA256 `5581f430670ac95eab6507f1b4b84eb141ffd4275f4ab70e8ae12426d9338664`.
- `/tmp/three_nonlinear_reference_20260908.md`, SHA256 `b97aafbac18a9966ed6cffe1c0d31e108fafef91202dde1b24c1a5c060e40a68`.
- Existing primary geometry and three-input analysis files, the original two-input L3 model/scope, the controlled interval in the offset/large-gain theorem, the original pure-arctangent two-layer theorem and the depth-three activation comparison.

Independence qualification: I authored the nonlinear-reference route. This is an independent audit of the root's assembly and of the other routes' scope and displayed arguments; it is not an independent second proof check of my own route.

## One required correction

REPORT Section 4 initially says: “its time derivative is not a positive semidefinite matrix.” The actual Gaussian-initialized L3 feature Gram was not proved to have an indefinite derivative. What is established is that the exact derivative identity has no manifest positive-semidefinite sign, and readout linearity/zero initialized readout/gradient flow alone do not prove monotonicity. The explicit counterexample in the nonlinear-reference route is a different readout-linear model. It must not be promoted to a counterexample for this architecture.

Replace the sentence by, for example: “The initial feature Gram is positive, but its time-derivative identity supplies no positive-semidefinite sign, and no architecture-specific monotonicity has been established.” The following statement about the unresolved trained coercivity estimate is justified.

Also remove the stray `+` between the two geometry-source links in Section 1. This is editorial and does not affect a mathematical conclusion.

## Verified claim boundaries

1. **No fitting/global-existence conflation.** Section 3 explicitly says the bare global-flow and population-limit contract does not assert eventual zero loss. The excursion/time bounds are correctly conditional on reaching loss at most 3/8; they are used to constrain fitting-based proof methods. The report does not treat their divergence as nonexistence of a global trajectory or as failure of the width limit.
2. **No impossibility claim.** The opening, nonlinear-reference discussion, Gaussian-regression paragraph and conclusion all distinguish an unclosed sufficient proof from failure of a positive activation coefficient to exist. Neither polynomial nor exponential choices are advertised as disproved.
3. **Interval versus witness.** Section 1 correctly distinguishes one successful positive `theta_delta` from the stronger interval `0<theta<=theta_delta`. Neither is currently supplied. A fixed constant witness remains possible.
4. **Small-delta quantifiers.** The sharp infimum statement is restricted to fixed dimension d>=2, 0<delta<=1/4 and 0<theta<=1/2. The lower comparison follows from `delta^2(2-delta)^2>=delta^2`; the planar upper example embeds in every such dimension and obeys the closed pairwise constraint. Constants are absolute. The report does not extend the matching upper bound to delta=1. The statement about `theta asymptotic to delta^p` should be understood for choices remaining in the stated amplitude range (in particular p>0).
5. **Theta=1 scope.** Pure arctangent is considered as a separate possible constant witness, not as covered by the derivative-floor theorem. The available theorem really is one sample/two hidden layers with a different readout initialization and narrower visible convergence scope. The middle-transpose tail requirement at L3 is not supplied by bounded forward output alone. The report correctly refrains from declaring theta=1 sufficient or impossible.
6. **Spatial versus temporal conditioning.** The report does not confuse the three-input initialization Gram with growing time-query covariance matrices. The direct route's inverse-free L2 projection identity is correct under its stated Gaussian integration-by-parts hypotheses; the Walsh example shows why this alone supplies no uniform Lp or source-tail bound.
7. **Raw-ball versus reachable counterexample.** The concentrated near-collinear weight modification stays in a bounded raw L2 ball while giving an arctangent remainder of order at least sqrt(delta). The report labels it a raw-ball counterexample and does not assert that the actual GF reaches those states.
8. **No easier-model substitution.** The offset/large-gain theorem, depth-two contract and pure-arctangent one-sample result are all distinguished from the original three-hidden-layer, three-input task. The full original convergence/uniqueness/nonaffinity scope remains open.

## Check of the displayed new fitting calculation

For c=1-delta and 0<delta<=1/4, c>=3/4 and `2c^2-1` is positive and at most c. Thus all three displayed unit vectors satisfy the closed separation condition. Their null coefficients are `(1,-2c,1)`, whose label projection is `2+2c>=7/2` and squared norm is at most six. Loss at most 3/8 gives residual norm at most sqrt(3)/2, hence the prediction projection is at least `7/2-sqrt(18)/2>1`.

The preactivation differences follow from the actual input map norm and the 1-Lipschitz activation. Adding/subtracting `2 atan z_0` gives the stated `2 sqrt(2delta) P_l+pi delta` bound. The exact null telescoping identity places one factor theta outside all three terms. With `U=11+R`, the linear-in-input term is at most `6 sqrt(2) theta sqrt(delta) U^4`, and the bounded arctangent remainder is at most `(3pi/11)theta sqrt(delta) U^4`. Since `6sqrt(2)+3pi/11<10`, equations (4)-(5) follow. The conditional energy inequality uses population `C_0=0` so L(0)=3/2, and yields equation (6). No sharpness of the resulting joint excursion exponents is claimed.

The nearby nonsingular equilateral perturbation is also correct: its weighted vector sum equals `(0,0,eta)`, the coefficient squared norm is `3+eta^2`, and the positive Gram Rayleigh quotient therefore tends to zero while the absolute cosines remain at most 1/2.

## Initial verdict

PASS for all reviewed partial mathematical conclusions and research-status boundaries **after** the required Gram-derivative wording correction. Before that correction, the report contains one unsupported architecture-specific assertion, although its overall open-status conclusion is unaffected. No sufficient three-input amplitude theorem or impossibility theorem is certified by this review.

## Final revision check

I reread the full revised REPORT with SHA256
`f5c408e8d4d902762999a9ae3a12d262df39518afca36578787df9f6d0b55bc0`.
It corrects the Gram-derivative claim to the precise absence of an established sign/monotonicity argument and removes the stray link character. The mathematical scope remains otherwise as audited above.

**Final verdict: PASS for the report's partial mathematical statements and calibrated open-status conclusion.** There is no remaining blocking scope issue in this revision. This verdict certifies neither a sufficient three-input amplitude nor nonexistence of one.

## Final assembly additions checked

I reread the full REPORT after its final additions, with SHA256
`a3f46f6aa663150064a445c43e7952d26d40a77149d7aa2f6909ff0b32c85cdf`.
I also checked the copied route revisions:

- `routes/NONLINEAR_REFERENCE.md`: `2e0381a184f9802377f96163fd8f68ae336dfb3cbd18a2ea07da6f364b253d2a`;
- `routes/DIRECT_SOURCE.md`: `f2431508bcf36a4b66375a652fe052f72a250f7f4e571ce51709fae04b02b083`.

The explicit `i!=j` in the infimum removes a possible reading of the pairwise condition as applying to the unit diagonal. The added REPORT equation (7) correctly states the all-state upper bound for the sum of all four raw tangent kernels, derived by differentiating the exact Gram-null prediction identity. The report correctly describes this as absence of a theta-independent null-direction margin on a theta-independent raw ball, and explicitly does not exclude a positive theta-dependent margin. The constant 256 is the square of the route's valid derivative bound 16.

The copied direct-source note now limits the energy-based variance statement to queries whose actual inputs are the bounded primal forward/backward fields; it does not extend that conclusion to arbitrary product or derivative probes. The copied nonlinear-reference note now explicitly permits T-dependent constants for a direct compact-physical-time construction while requiring the activation choice to be independent of T. These are correct clarifications, not new sufficient theorems.

**Final-hash limited verdict: PASS.** All earlier claim-boundary qualifications remain in force. This review certifies the displayed partial statements and open-status synthesis at the hash above; it does not certify a full three-input global theorem, a sufficient theta cutoff, or nonexistence of either.

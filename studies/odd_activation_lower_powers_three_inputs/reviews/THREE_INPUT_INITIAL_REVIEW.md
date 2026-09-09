# Independent audit of the three-input mathematical note

Audited 2026-09-07. Final artifact:
`/home/amir/Codes/PDE/studies/mean_field_peeling/odd_activation_lower_powers_three_inputs/THREE_INPUT_ANALYSIS.md`.

SHA-256: `87327edbd36e63fc40043e5e41783fa6a2e75a0be148af0e41d82337a5bbd2f9`.

## Scope and verdict

I independently checked the full note, the exact raw model and initialization in `two_sample_odd_activation_theorem/PROOF.md`, the mathematical derivations in `odd_mixture_separation_quantitative/THREE_INPUT_GEOMETRY.md`, the cited strong/scalar chain rules in Appendix C, Part F, Sections 9–10 of `odd_mixture_separation_quantitative/REPORT.md`, and the relevant old activation and controlled-source hypotheses. No earlier or sibling review, status/evidence ledger, or certificate was consulted. No experiments, proof edits, subagents, or commits were made.

**The final artifact has no remaining substantive mathematical issue found in this bounded audit.** It proves initialization estimates and necessary/conditional trajectory statements; it does not prove the generic three-input global theorem. Its separation of an unsuccessful proof method from a false positive-amplitude theorem is correct.

The original `/tmp/three_input_global.md` had one overbroad sharpness sentence. The root corrected that sentence in the final artifact, and I verified the exact difference and the corrected claim.

## Resolved finding: the sharpness range

The original note stated the worst-case first-feature eigenvalue as `Theta(e^2 delta^2)` without a separation range. This cannot hold for all admissible `delta`: at `delta=1`, a realizable triple has `Gamma=I`, so oddness and independence give `Q_1=qI` with `q=E phi(G)^2 >= a^2 >= 1/4`. Its least eigenvalue does not tend to zero with `e`.

The final line 31 now restricts this assertion to every fixed `d>=2`, `0<delta<=1/4`, and `0<e<=1/2`, exactly the range justified by the cited sharpness construction. This resolves the issue. The initialization lower bounds never had this problem.

## Verified claims

### Initialization geometry and Gaussian projection

For `T_i=u_i^{tensor 3}` and `R_i=u_i tensor v_ij tensor v_ik`, the unit norm, two zero pairings, and diagonal pairing at least `s_delta` are all correct. Summing the three individual Cauchy–Schwarz inequalities gives the factor `s_delta^2/3`, without using an inverse or full input rank.

The Gaussian integration-by-parts identity for the third Hermite coefficient is correct. Strict Jensen gives `m>1/2`, hence `b_3=(1-2m)/sqrt(6)` is nonzero. The conditional Hermite identity is valid at singular correlations as well as in the interior. The residuals `phi(Z_i)-e b_3 P_i` are orthogonal to every `P_j`, so the claimed matrix lower bound follows from their positive semidefinite Gram.

At later initialized layers, Gaussian regression with the common positive variance `q` gives `c_q>=a`; subtracting `c_q Z_i` is orthogonal to all preactivations, even for a singular covariance. Thus each layer contributes the factor `a^2`, and `Q_3(0)>=a^4 Q_1(0)` is correct.

The cited sharpness example has null direction `(1,-2c,1)`, which cancels the linear activation term. Its second difference is bounded in `L^2` by `C_0(1-c)`. The choices `c=1-delta` for the closed class and `c=1-2delta` for the strict class give the asserted matching order in the final stated range.

I also checked the cited algebraic nonzero-initial-motion arguments. Positive reverse covariances and strictly positive gates give the hidden-block and bottom-sample results. The extra forward-query innovations in the two upper layers have strictly positive conditional variance. Their derivative returns are retained, and these innovations cannot be cancelled by terms measurable in the older source variables. The note correctly makes the interpretation as actual trajectory accelerations conditional on strong existence and the chain rule.

### Odd symmetry and affine obstruction

Replacing `(x_i,y_i)` by `(y_i x_i,1)` preserves the loss as a function of every raw parameter state, hence preserves its exact GF and simultaneous raw-GD updates. Absolute correlations are unchanged.

At `e=0`, predictions are linear in the input and therefore belong to `ran Gamma`; consequently `v^T r=-v^T y` for every input-Gram null vector. A nonzero null-label component yields a positive residual lower bound and an infinite residual-length clock on a global affine path.

The equilateral equal-label triple is admissible for the stated closed/strict separation ranges. With population readout initially zero, the zero feature sum makes the readout derivative zero, and every hidden derivative vanishes. Its affine population GF is stationary at loss `3/2`. This is an affine obstruction only: the positive-amplitude initialized feature Gram is strictly positive.

### Required displacement and fitting-time lower bound

The three equations for the null-direction sums follow by substituting `phi(z)=az+e arctan z` and `sum v_i x_i=0`. The bounded arctangent and probability normalization give `||T_l||_2 <= (pi/2)||v||_1`. Cauchy–Schwarz and the operator norm inequalities then give equation (2) with exactly its displayed constants. The argument works with the stated normalized finite-width norms as well.

For the equilateral all-ones direction, either every prediction being at least `1/2`, or loss at most `3/8`, implies `sum f_i>=3/2`. Dividing equation (2) therefore gives equation (3). Under the explicitly imposed canonical conditions `C_0=0` and initial action norms at most 10, raw distance controls the readout norm and each learned Hilbert–Schmidt increment. The displayed polynomial majorization is correct, yielding

`R >= (pi e)^(-1/3)-11`.

The raw gradient energy identity yields `R<=sqrt(T(L(0)-L(T)))<=sqrt(3T/2)`, so the positive-part fitting-time lower bound has the correct constant. These are necessary bounds conditional on reaching the fitting criterion. They do not assert a finite fitting time or global population existence.

### Conditional scalar clock

For the assumed strong ascent trajectory, `J'=||grad_v J||^2+||H||^2` and `C'=H` hold in the specified Hilbert metrics. Continuity gives `C(s)=sH_0+o(s)` and `J(s)=s||H_0||^2+o(s)`. This justifies strict positivity of both `J` and `||C||` before using their quotient.

Differentiating `q=J/||C||` gives exactly the displayed nonnegative quantity. Therefore `q>=||H_0||` and `J'>=||H_0||^2`. Up to the first hit of `J=1`, `s<=||H_0||^-2` and ascent energy gives total raw length at most `||H_0||^-1`.

The strong-endpoint claim is justified even without a locally Lipschitz field: for `u<v` before the hit,

`||Theta(v)-Theta(u)|| <= sqrt((v-u)(J(v)-J(u))) <= sqrt(v-u)`.

Completeness supplies the endpoint. It does not supply a solution starting there; the note explicitly preserves this distinction.

For a symmetric equilateral population trajectory, all equal residuals factor the physical field into `3(1-J) grad J`. The scalar residual equation gives the exponential upper bound in (8), with strict positivity at every finite existing physical time because the continuous gradient is bounded on compact trajectory intervals. The feature clock integral is bounded by the same first-hit certificate. Symmetry and existence remain conditional as stated.

The initial Gram bound for `H_0=(h_1^3+h_2^3+h_3^3)/3` has the factor `1/9` shown. Equation (1) at initialization gives the upper bound linear in `e`. Together these make the certificate `||H_0||^-2` of order `e^-2` at fixed admissible separation and give the `O(e^-1)` path bound. This is a certificate scale, not a claim of a matching actual hitting time.

### Failure of the current source estimate and energy alternatives

The old controlled-source hypothesis requires bounded affine arrays over its prescribed clock and includes the exponential-in-clock small-amplitude restriction quoted in (9). With a certificate clock bounded below by a positive constant times `e^-2`, even a fixed positive lower bound for its coefficient forces the impossible small-`e` requirement `e exp(c/e^2)<=C`. This correctly disproves closure of this particular certificate for all sufficiently small `e`; it does not disprove global learning or exclude a stronger nonlinear source estimate.

For three samples, a transitive permutation symmetry of the folded Gram forces all off-diagonal entries to agree. Folding alone therefore cannot justify the symmetric scalar reduction for a generic triple.

For an existing true GF, energy gives a strong endpoint at every finite maximal endpoint. In finite dimension the smooth vector field extends from that endpoint, proving global GF existence. The same implication is unavailable for a merely continuous infinite-dimensional field.

For blockwise radial gradient clipping with scale factors in `[0,1]`, the inequality `dot L <= -||dot Theta||^2` follows from `alpha>=alpha^2`. It supplies no local Lipschitz property. The displayed cancellation model with unbounded `Q` indeed has arbitrarily large local `L^2` difference quotients while a clip that is the identity near zero remains inactive. Galerkin energy bounds likewise do not themselves imply strong compactness or weak continuity of the nonlinear maps and action products. These are valid limitations, not impossibility results for every energy method.

## Claim boundary

The final conclusion accurately leaves open construction/continuation of the generic uncut strong flow, source bounds needed for cap removal, nonsymmetric uniqueness and restart, trained-law nonaffinity, and the full finite GF/raw-GD observables and path/velocity limits. Neither the positive initial Gram nor the conditional symmetric lemma establishes these requirements. No counterexample to the positive-`e` theorem is established by this note or by this audit.

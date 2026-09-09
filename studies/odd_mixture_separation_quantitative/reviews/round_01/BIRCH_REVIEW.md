# Independent adversarial mathematical review

**Verdict: PASS.** I found no remaining substantive correctness or completeness objection to the claims actually made in the report, and no required mathematical repair. In particular, this verdict does **not** turn the explicitly open full global three-input result for the odd activation into a proved theorem.

## Input identification, isolation, and complete reading coverage

- Sole reading input: `/tmp/report-cdac813f004c/REPORT.md`.
- Input SHA256: `daa5a57856db4edc58e58f5f9efff12fbe6e0b442b503e1ef731eecfd444ae7b`.
- Input size: 302,359 bytes; 5,743 lines.
- I read the entire input in these consecutive, nontruncated line ranges: 1–240, 241–480, 481–720, 721–960, 961–1200, 1201–1440, 1441–1680, 1681–1920, 1921–2160, 2161–2400, 2401–2640, 2641–2880, 2881–3120, 3121–3360, 3361–3600, 3601–3840, 3841–4080, 4081–4320, 4321–4560, 4561–4800, 4801–5040, 5041–5280, 5281–5520, and 5521–5743.
- This covers the main theorem and all six main sections, the entire quantitative chapter, Appendices A and B, the complete three-input initialization chapter, and every part of Appendix C: M, F, R, G, V (including V.I), and N.
- I did not read skills, AGENTS files, directory listings, other project files, source documents, websites, previous reviews, or other agents' work. I did not consult other agents or run numerical experiments. Tools were used only to inspect this exact report, obtain its size/hash, and write this review. The input was not edited.

## Scope and standard of judgment

The report makes three distinct kinds of assertion: a complete global two-input theorem for the odd mixture; unconditional three-input initialization results and conditional initial-trajectory conclusions for that mixture; and a reproduced foundational manuscript whose own global theorem uses a shifted, large-gain activation. I checked the reproduced manuscript as mathematical content, and checked the applicability of its intermediate arguments to the odd mixture separately. I did not assume that its shifted-activation main theorem automatically applies to the odd network.

The full global odd three-input theorem is explicitly open. The identified affine obstruction invalidates a particular comparison route, while the positive nonlinear initialization results do not supply the missing global reference, tails, or nonaffinity argument. The report consistently respects these distinctions.

## Obligation-by-obligation audit

### 1. Model, normalization, and actual training algorithms — satisfied

The raw metric gives precisely the first-layer factor `1/d`, hidden-matrix factor `1/n`, and readout factor one in (T.6)/(M.7). Population rank-one operators have the required Hilbert–Schmidt norm, and finite normalized-space Hilbert–Schmidt norm is the ordinary Frobenius norm. Thus the four blocks (T.8) are the true gradient Gram blocks with the stated normalization.

The finite readout standard deviation is `n^{-1}`, so its normalized RMS is `O_Pr(n^{-1})`. The fixed-program argument compares this actual root with an auxiliary zero root rather than replacing the training initialization. The later same-width comparisons retain the actual initialization in both algorithms.

Raw GD is simultaneous Euler for the stated field; hidden fields are recomputed from interpolated parameters. The velocity proof uses the preceding-node raw direction, including the endpoint convention, rather than incorrectly evaluating the uncut vector field at the interpolated state. The assertions distinguish same-layer coordinate laws from nonexistent pairings between neuron populations or unrelated widths.

### 2. Two-input symmetry and scalar reduction — satisfied

Odd forward fields, even gates, and label folding give equality of the entire finite parameter vector field, not merely equality of objective values. The reflection exchanging the folded inputs exists under the separation assumption and preserves the Gaussian initialization and metric. Deterministic fixed-program limiting contractions, together with exchange invariance, force equal folded predictions. This obtains the scalar identity before uncut uniqueness is invoked and avoids a circular symmetry argument.

The physical reduction is consequently `Theta_dot = 2(1-g) grad g`; the loss is `(1-g)^2`. The analogous capped reduction is valid as a vector-field identity even though the capped feature field need not be a gradient. The report does not impose the deterministic scalar identity on an individual random finite network.

### 3. Affine feature-time reference, continuation, and inactive fields — satisfied

The active/inactive decomposition (A.3)–(A.4) has the correct gain factors and input-variance factor `v_u`. Both variances are at least `delta/2`. The equation `C'' = J J* C` and regularized radial convexity justify the lower bound on `||C'||`, including its initial one-sided slope. Thus `g' >= a^6 v_u >= delta/128` follows.

The energy-length argument makes a finite endpoint below the target strongly Cauchy, so local affine polynomial well-posedness supplies continuation. This proves the hit of `g=3/2`, the duration bound `192/delta`, and displacement `12 sqrt(2/delta)`. The argument correctly stops each reference at its own hit rather than assuming boundedness up to the larger uniform upper bound on the hit time.

The inactive-freezing argument uses the necessary independence. The active finite transcript is independent of the inactive first-layer Gaussian root, and learned increments have bounded ordinary Frobenius norm on fixed prefixes. Conditional expectation then yields the factor `1/n` in (A.10). Applying it both to the first learned action and to the product difference proves the frozen upper inactive fields. Conditional inner-product variance estimates establish orthogonality to the active fields and zero means. Fixed affine scalar programs contain only Gaussian-linear coordinate expressions with deterministic contractions, so their strong Euler limits are centered Gaussian. Together these give variance at least `delta/32` in every affine sample and layer. Bounded population action norms alone would not prove freezing; the report supplies the stronger argument.

### 4. Explicit Gaussian regression margin and transfer — satisfied

The Hermite projection in (Q.1) uses squared norm six. Gaussian integration by parts produces (Q.2) with coefficient `-2 nu^3`. The measure `t exp(-t) dt` has total mass one and mean two; Jensen has the displayed direction because `(1+2 nu^2 t)^(-3/2)` is convex. Squaring yields `2 nu^6/[3(1+4 nu^2)^3]`. Substituting `nu^2=delta/32` gives exactly the denominator `49152` in (Q.4).

The independent-copy covariance identity puts the optimal arctangent regression slope in `[0,1]`. Testing the optimal affine predictor on the other variable then proves the two-sided estimate (Q.5), also covering constant variables with slope zero. This avoids an inverse-variance loss. The restriction `||Z-Z0||_2 <= sqrt(eta_bar)/4` leaves at least half the residual norm, hence one quarter the squared residual. Absorbing the activation's linear part gives the exact factor `e^2`; the final denominator `196608` is correct. Appendix A's weaker transfer estimate is also valid and is explicitly superseded for the quantitative choice.

### 5. Fixed finite Gaussian program and singular queries — satisfied

Appendix C does not leave the specialized Gaussian-program theorem as an unsupported external invocation. The adaptive-conditioning argument maintains independent residual matrix factors after each revealed linear query. The conditional matrix formula (F.6), its compatibility relation, and the forward answer (F.7) are consistent with Gaussian orthogonal projection. The finite-dimensional removed noise projection has normalized expected squared norm `rank/n`, so discarding it in the coordinate limit is justified.

The source-response derivation retains opposite-orientation return terms. Orthogonality of the new residual input to prior forward inputs and Gaussian integration by parts give the cancellation in (F.11)–(F.12). The resulting oriented source covariances are full second moments of the inputs. Independence of source groups is not incorrectly asserted for the complete matrix answers.

For singular limiting query Grams, fresh input perturbations make each successive Schur complement positive. A fixed-instruction finite-array Lipschitz comparison controls removal of this perturbation. Continuity of finite positive-semidefinite square roots, coordinate expressions, and bounded formal first derivatives proves continuity of the scalar recursion without continuity of a pseudoinverse. The formal derivative convention and its contracted invariance on a singular support are stated and justified. These steps cover the hypotheses actually needed later, including causal scalar feedback and independent probes.

### 6. Canonical action spaces and functional analysis — satisfied

The countable generated-language construction has consistent finite marginals. Its closure under coordinate approximation and matrix applications gives a dense span in each generated `L^2` space. Passing the high-probability finite norm bound to deterministic contractions produces bounded initialized actions on that span; completion extends them to the full spaces. Passing finite adjunction identities on the dense span identifies the reverse actions as the actual Hilbert adjoints.

The rank-one identities provide Hilbert–Schmidt increments and their strong integral limits. The bounded-multiplier lemma and curve chain rule are valid under the stated `L^2` convergence. The weighted scalar Taylor estimate (F.41) proves the scalar predictor's Fréchet derivative without making the false stronger claim that a general nonlinear Nemytskii map is Fréchet differentiable from all of `L^2` into `L^2`. Gradient continuity follows by the same multiplier and rank-one estimates. Fixed-cap local existence and Euler comparison therefore have the required functional-analytic support.

### 7. Sharper two-input affine response constants — satisfied

The affine gradient field has degree three in the four primal components. On the stated ball, the component difference bounds and rank-one expansion justify the conservative total Lipschitz constant `9 b_r^2` and hence `F = exp(36 P^2 S)`. The answer-error table is consistent with the exact affected updates: middle-forward forcing reaches the top matrix and readout; middle-reverse forcing reaches the first two hidden blocks; the remaining two answer types have a single update target.

For the four source/output pairs, multiplying the displayed output Lipschitz constants by the forcing constants yields respectively `1`, `24 P^2`, `8 P^2`, and `1`, before the common `S F` factor. A perturbation at one time carries its own `h_j`. The probe argument first takes width at fixed nonzero amplitude, then uses continuity as amplitude tends to zero; it does not interchange differentiation and a width limit. Choosing deterministic signs tests the full absolute derivative row, including separately named singular slots.

The learned-moment terms are bounded by the stated affine query norms and controls. The factor two safely handles conversion to the two-sample block/time-row convention. Thus (T.17), repeated in (Q.15), is a valid replacement for the larger affine starting constants. The finite-array premise is supplied by fixed-mesh field convergence and exact update lengths; (T.18) leaves numerical slack and does not presume operator-norm convergence of trained matrices.

### 8. Offset removal, gain change, and primal comparison — satisfied

The comparator remains `a z` at the same actual gain. Replacing gain factors by one is only an upper estimate for `a <= 1`. Removing the offset does not remove a derivative, source slot, transpose return, or learned-memory term. The shifted gain-one query tables dominate the corresponding zero-offset quantities on `b_r >= 2`. The lower bound on gain is used separately for the affine variance and initial coercivity, not smuggled into the response upper estimates.

The same-state nonlinear/affine bounds in the main text are conservative consequences of bounded arctangent, bounded gates, and rank-one expansion. Combining their total `40 e b^3` with the affine Lipschitz estimate gives (T.21). The chosen cutoff leaves strict primal slack. The forward discrepancies (T.22) and the prediction constant `O` dominate the successive product expansions; the endpoint is therefore at least `5/4`. The sharper finite-array comparison `T0=40 b_r^3 S exp(9 b_r^2 S)` is consistent with this same estimate. The query and learned-moment error constants `D0` and `m0` remain dominated by the retained oversized numerical `q`.

### 9. Source equations and coordinate moment bounds — satisfied

Exact rank unrolling and the proved Gaussian rule yield (R.11)–(R.16), with the correct sample indices and control weights. Forward rows involve past reverse calls; backward rows include current forward calls. The construction order is `A2`, `A3`, `B3`, `B2`. Source covariances are established from raw primal query norms before any coefficient bootstrap, so this part does not assume the response conclusion to establish source variances.

On a bounded coefficient prefix, the deterministic maxima of the `L^p` norms obey the stated discrete Gronwall bounds (R.38)–(R.40). They are not random maxima over time. Gaussian source norms and Minkowski suffice despite correlations. The constants in (R.37) give the claimed `sqrt(p)` moment bounds. The exponential-square estimate with `L_q^2=8 exp(1) K_q^2` follows from the displayed factorial bound and leaves a summable geometric series. These are the incoming-field tails required for cap removal.

### 10. Retained-e envelope and same-array derivative remainders — satisfied

The exact derivative equations retain `L_k J_k`, cap derivatives, and current transpose returns. Their causal recursions yield the envelope with exponent `H s_k + H e sum h_r Q_r`. The terminal incoming field `Q_k` is absent from that time sum and is correctly retained separately in (R.54), (R.65), and (R.66).

Weighted convexity (R.55) requires no independence over time. Keeping `e` gives the exponent `p^2 H^2 e^2 S^2 L_q^2/4` in (Q.11). Under `e <= 1/(H S L_q)`, the `p=2` estimate and Cauchy–Schwarz give both expectations bounded by the displayed `X1`. The numerical prefactor and `exp(HS+1)` safely exceed the direct bounds.

The same-array affine comparison is explicitly distinguished from the actual affine baseline. The forcing expansions (R.59), (R.62), (R.65), and (R.66) account for all gate changes and preserve `h_j` for a single reverse-source perturbation, including unequal meshes. Their expectations use only the two quantities controlled by `X1`. Thus replacing `X0` by `X1` in the same explicit `R0` is valid; no new undetermined remainder constant is necessary.

### 11. Deterministic coefficient stability and chronological closure — satisfied

I checked the four affine derivative recursions (R.69)–(R.73), their majorants, and the product expansions used for (R.79), (R.81), (R.83), (R.85), and (R.87). The direct forcing terms cancel where claimed because mesh and controls are identical. In particular, the current `B3` row in the middle backward output remains present and is used only after it has been bounded. The top affine readout derivative uses past `A3` rows; its nonlinear remainder is available after the current top forward stage.

The constants `D2`, `D3`, `E3`, and `E2` consequently give the individual bounds by `(e+I_k)`. With `K_* = 2 max{1,D2,D3,E2,E3}`, their sum gives `E_k <= K_*(e+I_k)`. The finite telescoping product controls `e+I_k` using completed past rows. The cutoff `1/[2 K_* exp(K_* S)]` puts every new row within one half of its affine bound.

The stage-specific moment and derivative dependencies in R.9 agree with the actual calculation order. Current `q2` is not used to establish the current forward rows; it is defined after `B3`. Current `q1` is defined only after `B2`. At time zero, zero readout makes the relevant responses and reverse covariances vanish even with distinct formal zero-variance slots. Equations (R.93)–(R.94) also independently display the retained current returns. I found no circular bootstrap or hidden mesh-size restriction in this closure.

### 12. Complete coefficient recipe, monotonicity, and asymptotics — satisfied

Every constant used by `E_src` is explicitly defined by a finite elementary chain. `P_delta`, `S_delta`, `b`, `Q`, `J`, and `O` decrease with delta, while the regression margin increases. All source-chain constants are increasing in `P,S`. The apparent numerator in `P/(2T0)` simplifies to `1/[640 P^2 S exp(36 P^2 S)]` for the improved chain, and to the displayed analogous decreasing expression for the literal chain. Likewise `b/(4Q)` is a decreasing reciprocal in the underlying size parameters. Taking the minimum proves the claimed monotonicity. The latter reciprocal tends to zero as delta decreases to zero, proving the limit of the chosen cutoff.

For the asymptotic claim, `P_delta = O(delta^(-5/2))` and `P_delta^2 S_delta = O(delta^(-6))`. The improved primitive response constants are at most singly exponential in `C delta^(-6)`. The moment/envelope and chronological constants are at most doubly exponential; their finite products and sums do not add another exponential level. The final factor `exp(K_* S)` adds the third level. Thus (Q.21) has the correct direction as a lower bound on the displayed sufficient cutoff. The literal envelope adds an extra level and has the stated inner power `17/2`; retaining `e` alone removes that level. These are sufficient scales, with no implied necessity or polynomial cutoff theorem.

### 13. Cap removal, global physical time, and uniqueness — satisfied

The asymmetric gate decomposition is exact. Sequential backward substitution multiplies an incoming discrepancy only by bounded actions and gates; each cap factor multiplies a forward discrepancy already bounded in terms of the raw state. This gives a single linear dependence on `R`, rather than repeated powers. Gaussian reference tails defeat the resulting `exp(C R)` Gronwall loss, both for states and raw directions.

Uniform Cauchy convergence of cap paths and directions supplies a strong `C^1` uncut solution and identifies its field. The uncut feature path has the radial coercivity after construction, so it reaches one before the endpoint. Its bounded derivative ensures divergence of the physical-time integral at the first hit. The same first-hit clock works for cap references without assuming their prediction monotonicity. The uncut physical trajectory exists globally and remains in the controlled feature interval. The decay coefficient is correct: differentiating the squared residual gives rate at least `4(delta/128)=delta/32`.

Comparing an arbitrary bounded-primal uncut strong competitor to the capped reference needs only the reference's tails. The same argument proves uniqueness without symmetry and unique continuation from reached states; an additional `exp(C R)` factor on the already vanishing initial discrepancy is harmless. No unjustified local existence theorem on arbitrary uncut ambient `L^2` states is needed.

### 14. Finite GF/GD, true kernels, velocities, probes, and path laws — satisfied

At fixed cap and mesh the fixed-program theorem applies. Finite operator bounds follow from initial norm bounds and exact finite update lengths. Fixed-cap local defects and stopped Gronwall then remove the auxiliary mesh with width-independent constants. Comparing actual uncut finite GF to the same-width cap flow uses only already established cap reference tails. For raw GD, the extra cap-reference local defect tends to zero with `eta_n`; no Gaussian theorem is applied to a growing training transcript.

Part V supplies the extra observational obligations rather than inferring them from bounded action norms. The nonlinear probe construction yields source coefficient rows at fixed cap; pointwise derivative recursions then establish the required primary moments. Hidden-velocity actions use nested smooth product truncations, expected derivative domination, full source covariances, and genuine current returns. The second action is treated only after the first action's moments and derivative bounds are established. V.I separately supplies derivative-valid initialization transpose formulas. The true backward fields at capped states are appended as observations, distinct from the capped update fields.

The deterministic velocity comparison (V.40)/(T.27) truncates only the reference factor multiplying a gate difference, producing one `M` factor. Population uncut velocity paths have compact continuous `L^2` time images, which give uniform tail decay without controlling growth of cap-dependent higher moments. The specified order—width at fixed cap and `M`, then cap at fixed `M`, then `M`—avoids the problematic multiplication of cap-dependent moments by cap-removal errors.

Joint `L^2` observations give every true kernel entry and uniform-time moment convergence. Concatenation supplies finite-joint-time laws. The interpolation inequality (V.57) supplies the additional uniform path approximation that fixed-time laws alone lack. Bounded integrated RMS speed makes its error vanish and ensures finite path second moments. Generated probes pass through bounded coordinate operations, contractions, and both action orientations using same-width or common-population comparisons. These arguments support all stated compact-time convergence modes.

### 15. Two-input initial motion and kernel expansion — satisfied

Initial forward Grams are positive definite under the two-input separation. For `e>0`, the everywhere-identity argument makes the top beta Gram positive definite; bounded positive gates and the full reverse source covariances propagate strict positivity downward. The parameter-block norm formulas and bottom conditional variance bounds are valid without an input Gram inverse.

For upper samples, adjunction gives a positive sum of directional pairings. The raw isometry combining input exchange with `C -> tau C` preserves the scalar objective and gives equality of the two sample direction norms, so positivity applies to each sample. This works in both label sectors.

Backward multiplier continuity gives the initial hidden velocity divided by feature time, hence the actual right second derivatives. The scalar weighted Taylor/energy argument supports the kernel expansion without an ambient second Fréchet derivative. Physical time has initial slope two and second derivative `-4 kappa0`; therefore the hidden acceleration factor four and total projected-kernel coefficient `8 ||V||^2` are correct. The readout velocity is nonzero, and its physical second derivative has the displayed value.

### 16. Three-input odd initialization, sharp scale, and explicit open boundary — satisfied

The affine prediction-space obstruction follows from linearity in the input and applies even with singular but pairwise separated Grams. The equilateral equal-label example makes the entire affine population flow stationary. These statements diagnose the affine route without claiming a counterexample for positive `e`.

The tensor witnesses in the cubic lifting argument have norm one, annihilate the other two input tensors, and pair with their target by at least `delta(2-delta)`. Summing the three coefficient inequalities proves the stated lower bound on the entrywise-cubed Gram. The normalized Hermite component of arctangent is nonzero by strict Jensen, and its Gram decomposition supplies the first-feature lower bound. First-chaos projection then propagates positivity to the higher initialization Grams.

The planar near-collinear construction has the stated exact kernel vector for the linear inputs. The second-difference and gain-rescaling bounds on arctangent give the Rayleigh upper bound. Both the closed and strict separation choices satisfy all pairwise conditions on the stated interval, including its upper endpoint. Together with the lower bound they prove the worst-case `Theta(e^2 delta^2)` first-initialization eigenvalue scale for every `d>=2`. This is correctly separated from training-cutoff scaling and from binary-label projections.

For every upper sample's initial motion, the extra initialized forward calls retain their reverse response terms. Regressing the new forward source on old sources leaves a variance bounded below by the conditional variance from the preceding fresh reverse source. The latter is positive because `p_j` and the gates are nonzero. The new remainder is independent of the old variables determining the other term in each upper direction, so cancellation is impossible. The finite adaptive-conditioning version confirms the positive innovation after the finite-rank projection. The finite additional calls have the required integrable derivative envelopes under the described truncation.

Conditional on a strong solution with the proved trajectory chain rule, the physical hidden acceleration is `9V` and the projected total-kernel coefficient is `18 ||V||^2`. The algebra and readout acceleration are consistent without scalar residual symmetry. The report expressly leaves global odd three-input existence, uniqueness, uniform nonaffinity, and algorithmic limits open; no missing proof of an asserted global theorem is concealed here.

### 17. Reproduced shifted-activation global and initialization arguments — satisfied

I also checked the contents of Appendix C not directly imported for the odd global theorem. The augmented-Gram argument handles the realizable singular three-input cases. The large-gain controlled length bounds, their discrete no-overshoot version, and the explicit choices in (M.21) leave the claimed slack. The readout Gram's coercivity dominates the possibly nonsymmetric capped hidden contribution by an operator-norm estimate, which is sufficient for residual decay. This yields the bounded residual clock used by that manuscript and verifies its own affine finite-array premise.

The initial shifted upper-sample calculations in Part N have the displayed gain factors. Conditional Gaussian second/fourth moments give (N.26)–(N.28); the independent trace probe and uniform operator moments justify concentration and expectation limits rather than relying only on finite expectation identities. Expanding the listed trace moments gives the quadratic forms and positive lower bounds in (N.30), (N.37), and (N.39). The nonlinear perturbation table, rank-one expansions, and cutoff preserve those bounds. The physical acceleration and scalar feature-energy calculation produce the coefficient in (N.64). Thus the reproduced shifted theorem also has its stated proof obligations covered within the report.

## Adversarial issues tested and disposition

The most plausible failure mechanisms I tested were: silently changing the affine comparator's gain; losing an offset-dependent source term; replacing formal derivative row control with an operator bound; differentiating through a singular covariance inverse; dropping a current transpose return; invoking unknown current rows to prove their own bound; losing the single-step factor on unequal meshes; omitting the terminal incoming factor from the exponential envelope; using cap-dependent fourth moments in the wrong limit order; equating capped update kernels with true gradient kernels; using finite expectation calculations as concentration; and promoting positive initialization geometry to a global three-input theorem. The report provides the needed distinctions and arguments in each case.

## Objections and required repairs

**Substantive correctness objections:** none remaining.

**Substantive completeness objections to claims actually made:** none remaining.

**Required mathematical repairs:** none.

**Final verdict: PASS.**

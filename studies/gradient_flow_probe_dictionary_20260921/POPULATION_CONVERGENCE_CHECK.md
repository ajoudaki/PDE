# Internal mathematical check of the projected population limit

Checked document: `POPULATION_CONVERGENCE_ATTEMPT.md` in this study.

SHA-256 of the complete checked version:

    2f335a9980586f901a9c2c030c1a861a81ce748ef80af67f8e3349994c1c9152

**Verdict: the ridge-limit and projected-flow convergence results are correct under their stated assumptions.** No mathematical correction is required. This is an internal scoped cross-check, not a fresh isolated promotion review. The checker independently derived its own projected-limit result in POPULATION_OBSTRUCTION_ROUTE.md before reading the lead's proof. The supervisor then explicitly authorized reading the complete lead document and writing this check. No other route's draft was read.

## Scope and verified steps

1. **Ridge limit.** Completing the square gives the displayed variational identity even when the raw Gram is singular. The positive ridge guarantees invertibility. Zero-padding a fixed coefficient vector is valid because raw prefixes retain their literal scales. The quadratic-form estimate, contraction bound, dense-span approximation, and vanishing on the perpendicular complement prove Q_l,p->P_l strongly on the full population L2 space. A finite net gives uniform convergence on each compact subset. No conditioning premise is hidden.

2. **Initialized action and adjoint.** The two-sided background converges strongly to B_infinity=P_2W0P_1; adjoint convergence holds because both filter sequences converge strongly and are self-adjoint. The indicated product proof is valid. For complete detail, its varying-argument term can be split as

       (Q_2,p-P_2)W0Q_1,p v
         =(Q_2,p-P_2)W0P_1v
           +(Q_2,p-P_2)W0(Q_1,p-P_1)v.

   The first term uses strong convergence on a fixed vector; the second uses uniform boundedness. The adjoint proof is identical with the layers exchanged.

3. **Limit-flow well-posedness.** The cited single-sample inverse-gate proof applies to arbitrary fixed positive contractions, so it applies to P_l. It does not require bounded raw dictionary columns. Its bounded readout, HS increment, and middle-operator estimates persist, and X=F(g) is initially square-integrable for Gaussian g because F has at most exponential growth. The normalized unit training direction is needed for X_s=sigma W*Delta exactly as written. Its perpendicular row component stays fixed. The y=0 case is properly separated.

4. **Vanishing comparison sources.** The fixed limit feature trajectory supplies compact L2 images for H1(s,u) on the compact feature-time/input domain and for Delta(s,x). Strong action convergence on compact sets therefore proves a_p,b_p->0. The tensor estimate uses

       ||a_p tensor b_p-a tensor b||_HS
          <=||a_p-a||_2 ||b_p||_2 + ||a||_2 ||b_p-b||_2,

   and proves d_p->0. This argument uses the fixed limit trajectory rather than assuming uniform compactness of all p-dependent trajectories.

5. **Nonlinear comparison.** The forward and Delta estimates are correct. Direct subtraction gives exactly the displayed component bounds: the X equation contributes coefficients 2SM^2, 2SM+S, M on the three state errors; the middle equation contributes S+2SM, 2S, 1; the readout equation contributes M, 1, 1. Their respective source terms agree with the proof. The stated L dominates each resulting total coefficient and each source coefficient. Integration yields (4), and the prediction pairing yields (5). Upper derivatives suffice when a norm difference vanishes; this is the convention inherited from the cited comparison proof.

6. **Compact physical time.** The signed training feature prediction has nonnegative derivative because its middle energy is a product of nonnegative quadratic forms of positive filters, and its other two terms are squared norms. The scalar residual remains nonnegative and at most Y. Thus the physical feature clocks remain in [0,YT] on [0,T]. Subtracting them against the monotone limiting signed prediction gives D^+|d|<=E_p. The choice S=YT+1 covers both trajectories. The passive prediction speed J bounds the three readout, middle and row contributions; (1+JT)E_p proves the asserted uniform input-ball convergence.

7. **All-time upgrade.** When q_infinity>0, q_p->q_infinity follows from strong background convergence and tanh continuity. The radial readout argument in the supplied single-sample certificate gives a uniform positive training gradient energy and bounds both feature clocks by S=2Y/q_infinity for all sufficiently large p. Strong monotonicity of the limiting signed feature prediction gives D^+|d|<=-q_infinity|d|+E_p. Hence the all-time estimate (6) is justified without an exchange of p and physical-time limits.

8. **Axis positivity.** For either fixed normalized axis, retained h_a and U_aa imply the exact pairing

       <U_aa,B_infinity h_a>
         = E[Y_a tanh(Y_a)sech^2(Y_a)] > 0.

   The integrand is positive off zero, integrable, and Y_a is nondegenerate Gaussian. Hence B_infinity h_a is nonzero, and tanh's unique zero proves q_infinity>0. This establishes the unconditional all-time statement **to the projected limit** for those two training directions. It does not establish positivity for every other direction, and the document does not claim it does.

9. **Dense identification.** The three action/rank identities in (7) are sufficient: inserting the dense trajectory into the projected equations leaves no source discrepancy, and inverse-gate uniqueness identifies the states. They are correctly described as sufficient rather than necessary for equality of predictions. The document explicitly leaves them unproved for the derivative dictionary, so no density or dense-limit claim is inferred from convergence within the closed spans.

## Limits and optional presentation refinements

The theorem concerns the prescribed population carrier, zero readout, bounded actual Gaussian action, fixed normalized unit training input, and an all-order continuation whose every finite raw list consists of well-defined L2 fields. It does not itself construct or justify every future formal derivative list. It proves no quantitative order rate, no finite-width interchange, and no convergence to the dense population model.

No required correction was found. Two optional wording refinements would remove avoidable ambiguity: insert the fixed-vector split from item 2 explicitly; replace “h_a belongs to V1 already at p1” by “h_a belongs to V1 from the first nonzero increment list,” since this study also records a distinct literal-time-power indexing in which order one has no middle increment. Neither changes the theorem.

## Final-version recheck

The complete final POPULATION_CONVERGENCE_ATTEMPT.md was reread after the two exposition refinements, route-status updates, and final synthesis were added. Its SHA-256 is

    82105fec3c2f9b2e5feac9dbadfbc31e727aa25c7190486c5eed884162fff07d

The original checked hash above is retained. The mathematical theorem and its hypotheses are unchanged; both suggested exposition refinements are incorporated correctly. The verdict remains **correct under the stated assumptions**, with no required mathematical correction.

The final synthesis keeps the conclusion appropriately scoped: finite-stage innovation bounds do not become an all-order non-density result; the analytic example is expressly an obstruction to a general proof principle rather than a counterexample to this network; and the initial-kernel falsifier is not reported as an actual kernel gap. The projected-limit theorem is explicitly distinguished from still-open dense identification, rates, and all-order density. The descriptions of the other routes were checked here for these logical scope distinctions only; their underlying reports were not newly read or independently re-audited in this final recheck.

The closing discussion of Gaussian-innovation cancellation is read as the remaining mechanism in the stated sufficient state/action approximation route. As the preceding section correctly explains, equality of output trajectories might hold without full state/action equality; this final summary does not add a necessity theorem.

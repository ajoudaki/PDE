# Independent full mathematical review A1

Review date: 2026-09-09. Reviewer: isolated agent `/root/nonlinear_complete_review_a`.

## Verdict

I found no blocking mathematical objection to the substantive A–H conclusions, the local and explicitly conditional conclusions in I, or the exact identities and obstructions actually proved in J. This conclusion follows from reading the full proof packet and the full supplied dependency packet, not from accepting their theorem summaries or other reviewers' conclusions.

The assembled text needs two localized containment/scope repairs before it can be called literally self-contained without qualification: G.1 invokes an initialization asymptotic whose proof is absent from the allowed inputs, and the introductory sentence of J advertises fitting lower bounds that J does not contain. These defects do not invalidate the core dynamical constructions. I give exact locations and a self-contained repair for the former below.

The positive verdict has the manuscript's quantifiers: fixed datasets, fixed finite depth and finite observation horizon before width tends to infinity; canonical initialized actions on separate layer spaces; strong uniqueness on those spaces in the displayed bounded-primal class. It is not a global theorem for arbitrary C1,1 activations, a global moderate-sine or tanh theorem, a width/depth limit, a uniform-in-time width limit, or an operator-norm identification across widths.

## Inputs, hashes, and exact read coverage

I personally read `/etc/codex/skills/solve-math-rigorously/SKILL.md` and followed its proof-audit procedure. Mathematical inputs were restricted to the three files below. I did not inspect Git, history, other studies, reviews, source audits, external sources, or implementations. I did not delegate, train a model, or edit the candidate. The only file written is this report.

| Mathematical input | SHA-256 | Complete read range |
|---|---|---|
| `FINAL_NONLINEAR_ADDITION.md` | `88d726339ac16a5f2b43d0085f2f556df2aa8d0bbf4226040dc81dd80495484b` | 1–15597 |
| `reviews/FINAL_NONLINEAR_DEPENDENCIES.md` | `5104e50fdea12bd04b274016750cbd165a916529152137cf247d1d6ccbe8fa6f` | 1–2868 |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` | 1–98 |

The first two paths are relative to `/home/amir/Codes/PDE/studies/repository_refactor_2026_09_09/`; the notation path is relative to `/home/amir/Codes/PDE/`. File sizes were respectively 735323, 182307, and 5110 bytes. The hashes were checked again after the complete read and were unchanged.

There are **no unread mathematical ranges**, including no dependency ranges omitted as irrelevant. In particular, I read dependency III.M 1–269, III.F 270–811, III.S 812–1068, III.G 1069–1476, III.V 1477–1937, III.N 1938–2504, and III.A 2505–2868. Some portions of III.G, III.N, and III.A were unnecessary to the minimal A–J dependency chain, but I read them rather than assuming their irrelevance. Tool output that was truncated was reread in smaller intervals; in particular main lines 15099–15302 were reread explicitly. The final coverage statement does not count truncated output as read.

## Proof-unit inventory and findings

All line ranges in this section refer to the addition.

| Unit and complete range | Result of audit |
|---|---|
| A.1, 34–45 | Continuous at-most-linear value extension is justified by fixed-program approximation and second-moment tails. It does not claim a derivative formula for arbitrary continuous maps. |
| A.2, 46–55 | The fixed neural-product specialization supplies derivative domination separately, with finitely many source variables and finite polynomial envelopes. |
| A.3, 56–75 | Gaussian comparison and Poincare give the action constant two; the finite norm-three event and canonical extension are consistent. |
| A.4, 76–90 | Scalar predictor differentiation and strong trajectory chain rules avoid a false ambient L2 Nemytskii Frechet claim. |
| B.1, 95–645 | The first-activation flow transform gives the stated global two-hidden-layer result. Boundedness of the second activation and the specified readout initialization are used. The affine-first arbitrary-geometry exception is valid. |
| C.1, 654–1115 | Fixed-depth local existence, uniqueness, approximation and observables are supported under the displayed C1,1 and root assumptions. It is a local theorem. |
| C.2, 1116–1632 | The complete weighted source bootstrap retains each time/sample source weight, closes in causal order, and provides mesh-uniform marginal subGaussian tails. |
| C.3, 1633–2027 | The two-hidden-layer strict-activity argument correctly treats full Gaussian support, ridge independence, genuine transpose returns, and independent forward innovations. |
| D.1, 2032–2547 | The separated offset theorem has a coherent positive coefficient recipe, affine endpoint, and full claimed bundle. |
| D.2, 2548–3437 | The source equations, both orientations, current returns and affine independent-root probes are retained. |
| D.3, 3438–4319 | Nonlinear source perturbations close with their actual strict source-slot factors and complete backward row errors. |
| D.4, 4320–5211 | Sample symmetry is proved at the canonical-law level; radial coercivity and the affine continuation/nondegeneracy arguments have the required hypotheses. |
| D.5, 5212–5524 | Raw comparison, cap removal, physical-clock continuation and actual finite algorithms use the contained bridge with verified hypotheses. |
| D.6, 5525–5716 | All claimed initial hidden block/sample motion follows; no perpetual-motion claim is needed. |
| E.1, 5737–6046 | The final sufficient amplitude is the second-power bound, with the stated unmodified constant. |
| E.2, 6047–6152 | Model, loss, raw metric, finite readout and observable conventions are consistent. |
| E.3, 6153–6562 | Exact odd label folding and the active affine core are valid; inactive freezing is justified by conditional finite-width estimates. |
| E.4, 6563–7004 | Balance, coercivity, integrated Hessian and absolute arctangent regression estimates support the primal/nonaffinity threshold. |
| E.5, 7005–7640 | The actual source-probe normalization, enlarged beta family, positivity and numerical prefactors are supplied. |
| E.6, 7641–7823 | The weighted propagator bound has the stated power and fits the common numerical envelope. |
| E.7, 7824–7974 | The exact backward-forcing supersolution is consistent with the actual initialization coefficient and learned moments. |
| E.8, 7975–8236 | Distinct active/inactive boxes and weighted strict-transfer products close without treating arbitrary backward row errors as strict densities. |
| E.9, 8237–8557 | Full random sample-sector gates, current multipliers, second-order insertions and all source powers are accounted for. |
| E.10, 8558–9022 | The cap, clock and actual finite-algorithm bridge preserves the improved final threshold. |
| E.11, 9023–9282 | Motion, excluded odd endpoint obstructions, and Gaussian-energy normalization have their stated restricted meanings. |
| F.1, 9287–9566 | The general-shape theorem permits the displayed linear growth and has sufficient power 31/8. Extra nonaffinity restrictions are separated from dynamical existence. |
| F.2, 9567–9874 | Different forward/backward sample bases correctly handle opposite labels without assuming oddness of the shape. Gaussian margins and initial activity are justified. |
| F.3, 9875–10174 | Linear-growth forcing and moments preserve the numerical constants; the intrinsic-scale argument avoids an invalid inverse inactive-variance estimate. |
| F.4, 10175–10366 | Same-array cancellation and actual-primal L2 estimates yield the stated complete response defect. |
| F.5, 10367–10595 | Positive supersolution and beta margins close with strict source-step factors and the stated power restriction. |
| F.6, 10596–10922 | Exact affine positivity converts actual variances to response row bounds, including the improved FL estimate. Its wider beta interval is expressly conditional on a common primal interval. |
| F.7, 10923–11043 | Coordinate, time and gate normalization factors check out. The global-delta gate bound is not confused with an intrinsic-scale bound. |
| G.1, 11052–11519 | Main all-depth statement is supported by G.2–G.7. The ancillary initialization asymptotic at 11515 needs the containment repair below. |
| G.2, 11520–11775 | General balances, all-radius coercivity, Hessian integration, beta continuation and explicit depth constants support the interface used by G.3. |
| G.3, 11776–12006 | Gaussian-part moment recovery, full deterministic B-gate terms, compressed positive chains and both sector boxes give the displayed depth exponent ledger. |
| G.4, 12007–12110 | Finite-depth cap/observable extension, regression and initial motion are supported; the excluded smaller derivative exponent is correctly identified as invalid. |
| G.5, 12111–12750 | Four-layer derivation independently supplies balances, norm-ratio estimates and actual source probes; its numerical scale is not silently identified with G.2's scale. |
| G.6, 12751–13002 | Initial motion, true kernels, ordered velocity observations, actual GD directions and path laws are justified. |
| G.7, 13003–13182 | The literal four-layer chronological source identities retain every current return and every gate derivative. Its conservative box is distinguished from G.3's improved box. |
| H.1, 13187–13599 | A single odd large-gain activation works at every separately fixed finite depth, with the stated separation-dependent gain. |
| H.2, 13600–13787 | The direct nonlinear source production has strict slack uniformly over finite depth. The inverse layer-scale remainder compensates the curvature factor. |
| H.3, 13788–14101 | Canonical construction, cap removal, nonsymmetric uniqueness and all stated observation/algorithm limits are supported by the contained foundation and detailed bridge. |
| H.4, 14102–14353 | The no-symmetry, every-sample motion induction retains the exact forward return and a positive independent innovation at every upper layer. |
| I.1, 14358–14450 | Relative nonlinearity and the calibrated moderate sine constants are correct. |
| I.2, 14451–14518 | Exact initialized sine correlation map and its strict contraction inside the endpoints are correct. |
| I.3, 14519–14826 | A direct short-time moderate-amplitude construction is proved; current-return averaging is exact and does not imply global phase damping. |
| I.4, 14827–15141 | Finite-width GF/GD bounds, weak path-law tightness, strong conditional endpoints and the non-Lipschitz example are supported. None proves a new endpoint restart theorem. |
| I.5, 15142–15405 | The exponential-tail conditional population continuation argument and the ambient counterexamples are valid within their stated scopes. The observable reassembly remains explicitly conditional/prospective at 15299. |
| J.1, 15410–15597 | Exact bounded learned-memory estimates, adapted Gaussian concentration example, and simultaneous-coordinate obstruction are supported. No new global construction is proved. The preceding scope sentence needs correction. |

I also read every introduction and inter-unit paragraph outside the numbered ranges above.

## Main mathematical audit

### Foundation and dependency containment

Dependency III.F proves the finite-program theorem actually required: a fixed finite number of independent Gaussian matrices, each reused in both orientations, finite-second-moment iid root tuples, bounded continuous first derivatives for primitive coordinate instructions, and causal locally Lipschitz scalar contractions. Its conditional projection argument conditions the named matrix only. The resulting oriented Gaussian source covariance is the full input second-moment Gram. It is not a residual covariance, and repeated queries are not replaced by independent matrices.

The singular-query argument regularizes query inputs, passes finite-dimensional covariance square roots, and removes the perturbation by RMS stability. It does not claim pseudoinverse continuity. Formal derivatives freeze covariances, learned scalar contractions and previously computed deterministic responses while retaining separate named slots. The countable generated language and finite norm/pairing identities construct separate L2 layer spaces and genuine adjoints. Initialized operators are bounded actions; only learned increments carry Hilbert–Schmidt norms.

A.1 and A.2 provide the two extensions actually needed beyond that primitive theorem. Value convergence for continuous linear-growth instructions is kept distinct from derivative-valid neural product convergence. The latter uses clipping plus finite-source polynomial envelopes. III.V.4's probe argument gives absolute rows of expected derivatives before III.V.5 derives pointwise absolute derivative rows; it does not interchange absolute value and expectation. The fixed-cap primary bounds and finite primal events precede these probes, avoiding circular reliance on velocity estimates.

The references to an earlier “certificate,” “power-ten proof,” or “audited” argument are usually stylistically stale, but their mathematical content is present in D–G and III.F/III.V. The two exceptions requiring textual repair are isolated below. In particular H's cubic geometry is reproved in H.1 and H.4; the mention of special-data Section V there is not an indispensable missing premise.

### Raw metric, clocks, initialization and algorithms

The first-layer storage conversion agrees with NOTATION: stored variance 1/d and raw metric d/n correspond to the normalized first weight and input x/sqrt(d). The hidden rank-one tensor is uv^T/n at finite width, with Frobenius norm equal to the product of normalized vector norms. Middle mobilities, endpoint mobilities, readout storage and the predictor's 1/n are retained.

B/C use their stated unhalved weighted squared-loss convention; D–J use the stated half-sum two- or three-sample convention. The factors two in the two-sample physical clock and the factors three, nine and eighteen in three-sample initial motion are consistent with those losses. H's normalized feature objective satisfies grad f=a^L grad F; its residual equation therefore has a^(2L), while the accumulated control clock has a^L. Neither is a metric change.

The small finite Gaussian readout is retained in actual finite GF and GD and removed only through fixed-cap RMS stability. Variance n^-2 gives normalized RMS O_P(n^-1); the supremum assertion in bounded-memory J follows from the same Gaussian initialization. The zero population readout is not substituted into the actual finite algorithms.

B's general nonlinear transform needs its stated eta_n sqrt(n) restriction for the lifted raw-GD discrepancy. With affine first activation that specific curvature error vanishes and the arbitrary-fixed-Gram exception admits the stated vanishing-step improvement. C's local comparison handles its stated vanishing-step class. The later full bundles prove their prescribed simultaneous raw Euler step n^-2 by comparison to fixed-cap same-width references. At no point is a finite-program theorem applied directly to a number of queries increasing with n.

### Quantitative source closure

D's source identities retain the learned moments and the current transpose returns at both middle populations. Its cap-independent primal comparison is established before source comparison. The latter has a single past source factor h_j, complete backward row norms, and a causal forward-then-backward row construction. The same-array affine derivative comparison includes the current curvature multiplier. Its Gronwall constants may be very large, but the stated positive coefficient recipe makes the required inequalities strict.

E's stronger delta^2 conclusion uses more than a renamed coarse estimate. The intrinsic affine scale obeys M^16 <= 24^4 delta^-2. The weighted active transfers preserve both strict sides in the forward error products. The top learned B3 term remains present in FL, RF and the reconstructed backward error. The decisive weighted closure charges M^10(E2+E3)+M J2+M^3 J3 in the active sector and separate inactive terms; in particular the J3 charge is not incorrectly reduced to M^2. E.9 retains random off-diagonal sample-sector gates, every current return, and the two-insertion contributions. The final 8 H^400 e M^16 condition follows with explicit slack from c_poly.

F uses different forward and backward sample transforms for nonodd shapes with opposite labels. This is necessary and is done explicitly. Its direct raw linear-growth comparison avoids treating e/sqrt(delta) as e M^4 for an intrinsic M when the inactive variance can approach zero independently. The four same-state forcing coefficients sum to 375/16, below the retained constant 40. The complete source forcing bound of order K^30 e M^19 is small enough for the K^-16 M^-12 positive supersolution under the displayed e M^31 condition. This yields delta^(31/8), with a separate shape-dependent regression restriction where asserted.

G's improved all-depth argument preserves the deterministic B-gate terms after recovering sharper actual q moments from the same-array Gaussian-part identity. Those terms give Q_j=8L-3-2j for j<L and Q_L=5L-1; the sharper q scale alone would not justify dropping them. Positive affine comparison compresses chains of local resolvents through strict transfers, and the starred construction includes a transfer constraint as well as a backward-row radius. The inactive sector has its own small triangular supersolution. The resulting sufficient exponents are E_3=31, E_4=45, E_5=63, and E_L=18L-25 for L>=6. Dividing by 2(L+1) gives the stated p_L. The constant c_L=H_L^-100 D_L^(-2p_L) closes exactly against M^(L+1)<=D_L delta^-1/2. It proves no common positive small-perturbation prefactor for all depths.

H does prove a common activation by a different calculation. Its normalized nonlinear forward remainder is bounded by pi/(2K_l), while the curvature factor is K_l. At the same actual arrays this yields an incoming Gaussian-part scale controlled by Q_l+b/K_l. The production bounds alpha_new<=3F^2+16alpha and b_new<=512(n_l+b)+3S fit the explicit 32 and 2048 enlargement factors. Current reverse production uses only the already constructed current higher reverse row. The gain condition a>=10^8(1+T) is independent of depth and is satisfied by H.1's selected a and T0. The clipping argument uses an absolute bound for the possibly nonsymmetric hidden prediction contribution, not a false clipped energy identity.

### Numerical checks

I checked the displayed numerical implications as part of the proof read. I also recalculated the following sensitive constants with independent scalar arithmetic; this was an arithmetic check, not a simulation or replacement for a proof:

- The moderate sine nonlinear fraction is 0.0638905503064183, consistent with “approximately 6.4 percent.”
- G's rounded L6 early Hessian integral upper calculation is 5052.9585834, below 5070; the subsequent tail allowance is 22.2109375, leaving the stated 5100 bound. The auxiliary mean-value constants are approximately 12.77298<13 and 3.98944<4.
- b_5=78.38367<79, b_6=350.54244<351, D_5=5320.86009<5400, and D_6=47591.21936<48000. The common-H inequalities have ample logarithmic slack.
- The L4 integrated forcing bound at M=1 is approximately 10299.60<11000; the logarithmic term divided by M cannot defeat the stated bound for M>=1.
- The E closure factor 8 times 10^-70 times 24^4 is 2.654208 times 10^-64, below one.
- H.2's uniform worst-case alpha S b upper bound from its displayed coarse estimate is below 6.255 times 10^-11; multiplying by 61 gives below 3.816 times 10^-9, as required for the random-envelope estimate.
- H's gain prefactor 324 pi exp(1) times 10^10 is about 2.7668738881462 times 10^13.
- I.4's four raw Lipschitz constants sum to 10256<11000. The sqrt(n) is retained, so h=n^-2 gives the stated n^-3/2 smallness condition.
- The G ledger was recomputed for L=3 through 30 and agrees with the formula. I separately checked the algebra bounding the general j>=5 terms and the top term; a finite numerical sweep is not the justification for all L.

### Cap removal, uniqueness, velocities and path scopes

The decisive deterministic comparison first bounds every forward difference by the raw-state error. Backward induction then introduces one truncation factor multiplying that forward error; it does not produce its L-th power. Gaussian tails defeat the resulting exp(CR) amplification. Only the reference requires a tail certificate. This proves uniqueness against nonsymmetric bounded-primal strong competitors and continuation from reached states on the same canonical spaces, without an arbitrary-endpoint L2 local-existence theorem.

III.V supplies the full order of limits needed for observables: fixed finite primary program; fixed outer observation clip while previous inner clips are removed; fixed training cap before the auxiliary mesh limit; then training-cap removal at a fixed velocity-tail threshold; finally removal of that threshold. Ascending velocity queries and descending true-backward observations are separately justified. A bounded Gaussian action is never assumed to map Lp to Lp. The fixed-cap velocity moments come from source formulas and their explicit relevant derivative rows.

The actual hidden derivative of the raw-GD interpolant uses its preceding-node raw direction and its interpolated raw state, with the prescribed right-node/terminal-left convention. The reference-only velocity comparison has one threshold factor. Compactness of the uncut velocity's L2 time image removes its tails without controlling growth of cap-dependent fourth-moment constants. Products of same-layer L2 fields give every true kernel block and squared speeds. The interpolation estimate ||x-I_h x||_infinity^2 <= 4h integral |x'|^2 upgrades finite-grid joint laws to the stated same-layer path W2 laws. It does not create a cross-layer neuron pairing or a continuous-path velocity law.

## Required localized repairs

### R1. Uncontained ancillary initialization asymptotic

**Location:** main 11515–11518, G.1 Section 7.

The text invokes the “previously proved convex initialization asymptotic q_L~1/(2theta L).” No proof of that asymptotic is contained in the three allowed mathematical inputs. Dependency III.A concerns the large-offset class and does not supply this convex-mixture statement. This is a containment defect in an ancillary limitation discussion, not a counterexample to the all-depth theorem.

**Repair:** either remove that invocation or append the following argument, with q_k defined as the initialized marginal second moment for phi_theta(z)=(1-theta)z+theta atan(z), fixed 0<theta<=1, and q_0=1.

The recursion is q_(k+1)=E[phi_theta(sqrt(q_k)G)^2]. For z!=0, 0<|phi_theta(z)|<|z|, so q_k decreases. Dominated convergence and the strict inequality show its limit is zero. The global remainder bound |atan z-z+z^3/3|<=|z|^5/5 follows by integrating t^4/(1+t^2). Gaussian moments therefore give q_(k+1)=q_k-2theta q_k^2+O_theta(q_k^3). Hence 1/q_(k+1)-1/q_k -> 2theta, and averaging these increments yields q_k~1/(2theta k). The absolute activation regression residual is at most its second moment and thus tends to zero. For two samples, the projected initialized kernel is at most q_L by Cauchy–Schwarz, so the initialized loss derivative also tends to zero; this excludes a positive depth-uniform exponential loss bound beginning at time zero. It does not exclude a single activation satisfying a qualitative finite-depth theorem.

This would make the existing conclusion self-contained without changing any main amplitude threshold.

### R2. Orphan fitting-lower-bound scope claim

**Location:** main 15408, introductory paragraph of J.

The sentence advertises “fitting lower bounds” for a “three-input near-identity family.” J.1 contains bounded-memory identities, an adapted Gaussian concentration example, and a two-input coordinate obstruction. It contains no such three-input fitting lower-bound result, and no explicit contained reference discharges that assertion.

**Repair:** delete that sentence or replace it by the actual scopes of J.1. If fitting lower bounds are intended to remain among this packet's claimed partial results, their precise statements and proofs must be supplied. I cannot certify an absent result. This correction does not affect the bounded-memory or Lie-bracket proofs that are present.

## Exact boundary of acceptance

B is global only for its displayed two-hidden-layer transform class and initialization conditions, with its explicit affine-first exception. C is local at arbitrary fixed depth; C.3's activity claim has its own Gaussian, separation, nonconstancy and positive-mobility assumptions. D handles the offset family under one-sided separation, including its permitted antipodal case. E and F require the stated two-sided separation and amplitude restrictions. G supplies fixed-depth extensions with explicit depth-dependent coefficients; its uniform exponent does not imply a uniform coefficient. H supplies one large-gain odd activation chosen from separation for every separately fixed finite depth, with an absolute regression gap rather than a uniform relative nonlinear-energy fraction.

I's moderate coefficient is genuinely retained in its local theorem and exact initialization identities. Its unconditional finite GF/GD energy estimates and its strong endpoint lemma do not establish a global canonical population path. I.5 proves a global strong population implication under (ET) for the stopped capped reference families at each needed horizon/cutoff; (ET) remains unproved for initialized sine training. The text at 15299 does not present the full observable reassembly as an independently completed unconditional theorem. Its focusing, weak-lower-semicontinuity and non-Lipschitz/semiconvexity examples concern ambient states, with no reachability claim.

J's memory estimates are exact on an existing strong path and have the stated finite-readout corrections. Its adapted Gaussian example refutes a generic tail inference, not the actual dynamics. Its coordinate result concerns simultaneous straightening for arbitrary controls at nonzero correlation. It proves no global tanh or bounded-activation population limit.

Subject to R1–R2, I would accept the substantive packet in precisely these scopes. I found no required change to its core source powers, gain or amplitude recipes, Gaussian initialization, raw clocks/metric, cap-removal logic, actual GD comparison, or stated same-layer observables. This is a supported mathematical review, not a formal proof-verification claim and not a certification of the explicitly open extensions.

# Milestone C after A: established interfaces and remaining obligations

Date: 2026-09-12. Status: scoped strategy assessment, not a new theorem or a promotion review.

The strongest defensible conclusion is that A materially improves the *reachable-state regularity and stability interfaces* available to C. It does not supply a finite, numerically manageable representation of the Gaussian population state. In particular, A makes a long physical learning interval controllable by accumulated training force and gives an independently defined nonlinear selection target with positive learning margins. The remaining central issue is to generate, compress, and propagate the Gaussian action and response information from permitted initial data, with computable error and resource bounds.

The previous supplied-path and adaptive-query results should therefore be retained as useful components, rather than treated either as a completed C solver or as evidence that C is impossible. A's new estimates address some of their named analytic gaps on its own reached tanh family. They do not transfer the three-hidden-layer arctangent comparison theorem to the two-hidden-layer tanh model automatically.

## Source coverage and assessment boundary

Read completely:

- `docs/README.md` and `docs/NOTATION.md`.
- `docs/global_nonlinear.md`, C.4.9 in full, currently lines 12994–15322: statement NS1–NS9, all four proof units, the named-coefficient supplement, and completion.
- `docs/gaussian_calculus.md`, the complete “Integrated queries and adaptive Gaussian comparison” package, currently lines 5945–8546: Q2, Q3, Q4, Q5, Q6, Q7, and G, including their proofs and scope boundaries.
- `docs/finite_optimization_and_controls.md`, complete Section 13, currently lines 2167–2409.
- The required `solve-math-rigorously` and `investigate-conjectures` skills, and the latter's research-contract and adversarial-audit references.

Additional established material read for the model, nonatomic-law, and source interfaces:

- C.4's complete initial theorem and scope statement, currently lines 3836–3981.
- C.4.7's complete model/theorem/observation contract, currently lines 8978–9170, and its complete proof units C.4.7.4–C.4.7.5, currently lines 10307–10554.
- C.4.6's complete subsection “Uniform population bounds from the bounded feature segment,” currently lines 8142–8258, containing S40–S45.

One overlong Section 13 read also exposed the beginning of Section 14, through line 2590; no claim below relies on that material. No other study, study history, review, experimental result, or chat was consulted. No computation or experiment was run. The deeper fixed-program/carrier and fitted-reference results cited inside these established sections are treated as established dependencies; this assessment does not claim a new independent audit of all their proofs. Numerical APIs were outside this assignment.

## 1. What A actually changes

A concerns the original two-hidden-layer tanh network, independent Gaussian stored variances `(1,1/n,1/n²)`, mobilities `(n,1,n)`, and unhalved mean-square GF. Its positive slow-time theorem is for a three-atom mixture: the two reference anchors and one added atom whose location and label vary over the compact rectangle NS1. The passive prediction is nevertheless determined on the whole input circle.

The constrained equation NS3 is an exact nonlinear *limiting episode*:

\[
 \dot{\bar\theta}=-2(f_{\bar\theta}(u_\alpha)-y)
                 \Pi_{\bar\theta}g_{\bar\theta}(u_\alpha),
 \qquad \bar\theta(0)=\theta_\dagger.
\]

Here `theta=(w,K,c)`, `A=A0+K`, and every gradient and projector uses the current state and actual adjoint. The small matrix being inverted is only the two-by-two anchor Gram. The fields `w,c`, the Hilbert–Schmidt increment `K`, and the initialized action `A0` remain infinite-dimensional. A two-by-two inverse does not turn this into a two- or three-dimensional dynamical system.

The following additions are useful to C.

**A horizon-independent source budget.** CT4–CT8 control a whole history by its integrated difference from the full reference control. Its total absolute control mass is at most `10+q`. CT7 bounds the entire backward beta row, including its current diagonal and every retained old training slot, and gives

\[
 \sup_{k,u}\tau_R(Q_k(u))\le M e^{-cR^2}.
\]

CT26 bounds the raw state, action norm, and readout supremum in terms of this mass. The constants do not grow simply because physical time becomes `tau0/epsilon`. This is a substantive improvement over a bound whose only horizon parameter is elapsed physical time.

**The complete query, including its predictable response, has controlled tails.** CT27 decomposes `Q=zeta+J` with bounded `J` and bounded Gaussian variance. This is stronger than G.17–G.20 in the arctangent comparison package, which bound the fresh innovation and trained-memory term but leave the predictable response mean uncontrolled. It closes that particular *type* of missing estimate for A's controlled tanh programs. It is not a theorem about G's different adaptive algorithm.

**A reached one-reference stability modulus.** C.4.9, proof unit C, equations (11)–(13), bounds a gradient difference by

\[
 C(1+R)(d+|u-v|)+Ce^{-cR^2},
 \qquad \omega(z)=z\sqrt{\log(e/z)}.
\]

Only the comparison path needs the proved tails. For an actual comparison inequality

\[
 D(t)\le\eta+C\int_0^t\omega(D(s))\,ds,
\]

the established bound is

\[
 D(t)\le e\exp\!\left[-\left(\sqrt{\log(e/\eta)}-Ct/2\right)^2\right]
\]

on its stated small-error interval. This supports uniqueness, approximation by Euler programs, and restart from reached states. It does not assume ambient local Lipschitzness. A compressed algorithm would still need to produce the discrepancy `eta` in this comparison, on a common meaningful realization; the propagation theorem alone does not do that.

**Strong derivatives along the reached curves.** Proof unit C, (23)–(27), proves

\[
 \|Q(v)'\|_2+\|\Delta^{(2)}(v)'\|_2\le C m(t),
 \quad \|G'(t)\|\le Cm(t),\quad \|B'(t)\|\le Cm(t),
\]

where `m(t)` is absolute control density and `B=G(G*G)^{-1}`. The hidden activation derivatives are also strongly controlled. The important row product is handled using the established `L4` bounds. This provides temporal regularity in accumulated control for A's actual reached queries; the long clock itself need not create arbitrarily many distinguishable time slices. It does not imply compactness of all Gaussian coordinates or stability of named source derivatives under an arbitrary compression.

**A meaningful nonlinear accuracy scale.** NS6–NS7 certify positive added-component risk gain `a` and paired second-hidden displacement `j`, independent of contamination size. B.5 expresses them through a positive endpoint-conditioning constant `kappa` and a positive episode length. This gives C scientifically relevant targets: errors should be smaller than the learning and hidden-adaptation margins. The constant `kappa` is defined by a compact minimum and proved positive; it is not given an evaluated numerical lower bound. The text explicitly permits impractical constants.

**A nonlinear reference beyond a response jet.** NS3–NS4 recompute the projector and features throughout a nonzero episode. They can anchor comparisons of whole-circle predictions and paired hidden changes. This is stronger than a first derivative, fixed kernel, or a fitted curve, but its numerical implementation remains open.

## 2. Exact positive content of the query-compression package

These results concern a different architecture: three hidden arctangent layers, one training input, and a feature-time interval. Their normalizations and applicability must remain attached to the bounds.

| Established component | Usable content | What it does not provide |
|---|---|---|
| Finite controls 13.1 | Exact integrated equations retain all trained increments and both orientations of both initialized matrices. The difficult lower transpose is applied to the primitive `b=integral delta2`. | A finite-dimensional population representation, or deletion of trained memory. |
| 13.2 | Under bounded matrix operator norms and readout supremum, all four query arguments have RMS time-Lipschitz constant `C(B)`. At most `1+ceil(CS/tolerance)` supplied arguments per orientation give action error at most `B*tolerance`. | An algorithm that can generate those arguments from only the retained transcript. Each argument is still an `n`-vector. |
| 13.3 | For the lower memory, `eM <= (Bh+S Lh) eb + S Lb eh` and `eR <= S Lb eM + 2S Lb Bh eb`; top memory has the direct rank-product continuity bound 13.12. No convergence of `b'` is needed for these two lower-memory bounds. | Stability of the equation producing `b`, or derivative/kernel convergence. |
| Q2 | For deterministic or independently frozen histories, integrated Gaussian forcing has mean-square maximum at most `T²(B²+sigma²) reff/m`. A Lipschitz history satisfies `reff <= min(K,1+2(K M²T²/sigma²)^(1/3))`. | Conditioning on an adaptive perturbed history while retaining independent Gaussian laws. |
| Q2's specified scaling | For `K` comparable to `m²` and `sigma=m^(-1/4)`, integrated covariance-forcing squared supremum is `O(m^(-1/6))`; raw-query squared maximum is `O(m^(-1/6) log m)`, under all listed boundedness premises. | A corresponding nonlinear trajectory error. |
| Q4–Q5 | A causal matrix martingale and a two-pass argument bound the algorithm's *own* histories: effective ranks `O(n^(11/12) log(e+n)^(4/3))`, actual raw-query RMS error `O(n^(-1/24) log(e+n)^(8/3)+n^(-1/4))`. | A dimension independent of width, or convergence of the uncut nonlinear dynamics. |
| Q6 | Same-seed clipped filtered/unfiltered state error is at most `C(S,M,R)(filter_scale+step+query_error+warmup_error)`, without an exponential inverse-filter penalty. | A cap-uniform constant, register-derivative convergence, or actual physical-GF identification. |
| Q7 | The constant can be bounded by `C(1+R) exp(C(1+R))`. With deterministic `R_n=o(log n)`, the two same-cap processes have mesh-state error `n^(-1/24+o(1))` in probability. | Clipped-to-uncut comparison or existence of a common population limit. |
| G | Exact finite equality in distribution of the entire coupled two-matrix transcript under the replacement oracle; learned memories and non-matrix roots are retained. G.22 transfers bounded Lipschitz observations from the canonical clipped state and middle query. | Preservation of the initialized matrices as jointly observed coordinates, tail indicators, a population limit, or a numerical complexity theorem. |

Q5 and G are genuine causal constructions, so it would be wrong to describe the whole package as frozen-path work. Conversely, the exact displayed construction has length-`n` vectors, learned `n`-by-`n` matrices, `n`-by-`K` Gaussian arrays, and `K`-by-`K` transcript arrays with `K` comparable to `n²`. The last displayed arrays alone have order `n⁴` entries. Streaming or compression could change storage, but no such cost theorem is established here. Thus “the original Gaussian matrix is replaced” is not yet “the population dynamics are computed manageably.”

The exponent `1/24` is also too weak to be read as a practical accuracy claim without constants and measured resources. It is a convergence statement for its stated comparison, not a usable numerical budget for C.

## 3. The outstanding bridges, with their precise scope

**Supplied path versus generated path.** A time net certifies that finitely many points describe an already supplied query curve. A queried point may have depended on discarded earlier calls. A generative solver must compute its next query and the law of its response from its own finite state. Q4–Q5 show how this issue can be addressed in one particular construction; they do not identify a generic way to discard its transcript.

**Value history versus response history.** A bounds weighted beta rows and normalizes old pulses by control mass. CT36–CT45 compare programs with matching named slots and perturbed controls. They do not bound the error made by dropping slots, merging covariance directions, truncating response order, or projecting fields. At zero-variance or duplicated sources, transverse named derivatives remain meaningful; equality of value laws need not determine them. The A-supplement makes this distinction explicit. A small effective rank for query values therefore does not automatically give a small response state.

**Current adjoint.** In A the force uses `Q=(A0+K)*Delta2`; the projector depends on gradients containing this exact quantity. Retaining an initialized forward covariance while replacing its reverse by fresh independent Gaussian noise changes the force and may change selection. Retaining the current gradient at a few inputs without its future action rule also does not define continuation. Every candidate needs a consistent approximation of both action directions and all retained trained-memory contractions.

**Restartability.** A proves unique restart on the same carrier from reached states. Its construction retains the complete reference history; it does not reset source primitives at the endpoint or a splice. A finite solver must specify which finite numerical state, covariance/response information, random seeds, and fixed coefficients are saved, and show that continuing from that saved state reproduces its own continuation and approximates the target continuation. Finite memory may depend on the chosen horizon and accuracy; it may not hide an unbounded function, an unevaluated Gaussian-action oracle, or arbitrary information in infinite-precision real numbers. Exact fixed-dimensional moment closure is not required by C.

**Error production and accumulation.** The useful A stability estimate starts after an admissible discrepancy has been bounded. It does not by itself control Gaussian quadrature error, source deletion, learned-memory truncation, perturbed inner products, projector error, or roundoff. Local errors need a causal bound on their accumulated effect. Errors weighted by control mass may benefit from A's finite mass; an unweighted persistent physical-time forcing can still accumulate through `tau0/epsilon`. Declaring an error “small at each step” does not identify which case holds. A source or Gram error could also move an algorithm out of the protected conditioned region, so its conditioning and tail premises must be secured for the actual approximation.

**Precision and singular Grams.** Q2–G use positive Gram regularization to define finite Cholesky factors; this is a mathematical existence guarantee. They do not give a floating-point perturbation bound for the factors, response coefficients, or downstream states. A's anchor Gram is conditioned on its certified neighborhood, but the Gaussian history covariance may still be singular or nearly singular. These are different matrices. The arithmetic cost and sensitivity of the history representation need their own analysis; increasing precision cannot be left outside the resource count.

**Derivative observations.** Section 13.15 exhibits why uniform primitive error does not control its derivative. Q6–Q7 similarly leave velocity/kernel observables open. A now proves strong derivative identities for its exact reached trajectories, which is useful, but does not establish convergence of derivatives of a compressed solver. C can choose the smallest observation set that identifies its claimed dynamics and restart; if it claims current gradients, hidden velocities, or kernels, their errors must be included explicitly. A prediction-only curve cannot certify the missing state information.

**No broad impossibility conclusion.** Section 13's concentrated-vector counterexample refutes an RMS-only product estimate; its Hilbert example refutes compactness inferred solely from temporal Lipschitzness; its oscillatory example refutes derivative convergence inferred solely from primitive convergence. None is a reached canonical tanh counterexample or a no-go theorem for all admissible finite approximations. Q7's inability to remove caps likewise identifies a theorem boundary, not impossibility of an independent solver.

## 4. Slow-time computation is not a finite-epsilon GF certificate

A distinguishes three objects: original-mixture GF at fixed positive `epsilon`, the constrained episode as `epsilon` tends to zero, and actual finite networks with width taken first. NS5 excludes slow time zero because the original state is not the fitted endpoint. The full reference carrier is an initial condition for the limiting episode, not permission to reset an actual finite run.

Consequently, a numerical approximation of NS3 has at least two separate discrepancies when used to predict original-mixture GF: its numerical error for the constrained equation and the finite-contamination selection bias. A's C.7(37) gives a useful exact interface for the latter, involving the fixed-prefix raw error, reference residual, its square, and `epsilon`; C.7(38) propagates that discrepancy by the Osgood bound. The displayed proof then fixes a prefix, sends `epsilon` to zero, and finally increases the prefix. It supplies no evaluated practical uniform finite-epsilon error or simultaneous width/contamination rate.

Reference initialization can in principle use a finite reference prefix with the explicit raw endpoint estimate `sqrt(10) exp(-b/5)`, followed by certified numerical approximation of that prefix. Its cost and Gaussian-state representation still count. Storing the exact endpoint as an uncomputed infinite object would leave C's computational problem unresolved.

The correct total comparison keeps separately: initialization error; data-law approximation; Gaussian/state/history approximation; time integration; arithmetic; and, only when substituting NS3 for original-mixture GF, finite-epsilon bias. Their combination must follow an actual comparison argument, not an assumed sum of unrelated rates. Finite-width validation is an additional empirical comparison, not a replacement for these population numerical bounds.

## 5. A minimally meaningful contract for C

The original roadmap's core target remains appropriate. A should sharpen its certificate and benchmark, not narrow it to one atom or silently replace physical GF by the singular limit.

1. **Same model and actual target.** Specify the canonical two-hidden tanh population GF, initialization, training metric, represented law, and finite physical horizon. The approximation is generated from the law and prescribed initialization information. The reference endpoint and NS3 can be computed as additional derived targets, with separately reported finite-epsilon bias when they are used to predict original training.

2. **A represented nonatomic family.** The first certificate should at least cover a concretely specified family inside C.4.7's established neighborhood through physical time 40, containing actual nonatomic laws with a computable integration/approximation interface. Restricting to a represented family is legitimate; an arbitrary Borel law without computational access is not a numerical input specification. Replacing such a law by quadrature is legitimate if the law error is counted. C.4.7.NL/NO supply an established continuity interface for this axis.

3. **A meaningful A overlap.** Include A's original-mixture family and its constrained episode as a demanding additional target for the same approximation machinery, whenever certified. An A-scale claim must name a fixed positive epsilon or an explicit epsilon-dependent regime, control the horizon `tau0/epsilon`, and resolve its numerical and selection errors relative to `a` and `j`. A's current theorem does not extend its slow episode to nonatomic added laws. That extension is a distinct obligation, not an assumption needed to begin C on the already established nonatomic time-40 family.

4. **Finite causal numerical state.** State the saved finite variables and reconstruction map, with a verified continuation rule. Permit multiple low-dimensional fields or retained memory if all discretized degrees of freedom, coefficient tables, Gaussian directions, and history costs are counted. Exclude a renamed trained dense network, trajectory playback, and an unevaluated population action. No particular basis, closure, polynomial order, or hierarchy is prescribed by the existing evidence.

5. **Observable and quantitative guarantee.** Specify whole-circle prediction error and the finite internal/action/paired-hidden observations needed to identify the evolution and justify restart. Give the probability mode, finite resource budget, conditioning and precision requirements, and all approximation dependencies. An arbitrary-accuracy existence statement without a useful evaluated resource instance would not establish the roadmap's manageable computation requirement.

6. **Reusable exploratory operation.** Keep the equations usable for larger perturbations, nonorthogonal inputs, and longer training where meaningful. Outside the certificate, report results as exploratory and require independent refinements of time, law quadrature, Gaussian/state resolution, and memory/response truncation, plus increasing-width finite-network comparison. A stable curve at one setting or agreement only on training loss is insufficient. No experiment is authorized by this assessment.

This keeps the two intended roles of C intact: a certified independent computation in a substantive established family, and a reusable route for investigating whether conservative bounds reflect real behavior. It does not require a universal law theorem, all-time accuracy, a universal fixed-dimensional closure, or a chosen numerical hierarchy before there is evidence for one.

## Recommendation

Use A to replace the vague “long histories might be uncontrollable” concern with a precise constructive obligation: identify a finite causal representation whose *own generated* Gaussian and response approximation errors can enter A's reached one-reference comparison, with all initial-history and arithmetic costs counted. The first candidate should be assessed at this interface before extensive implementation. Source production, not another propagation estimate alone, is now the leading gap.

Retain the nonatomic physical-time-40 certificate as the minimum meaningful computational scope and use A's finite nonlinear episode to test and extend that scope. Solving NS3 alone would be a valuable new numerical component, but would not by itself complete C as currently defined.

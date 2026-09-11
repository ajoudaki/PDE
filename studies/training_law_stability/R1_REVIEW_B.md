# Independent complete scientific review B of frozen R1

**Decision: ACCEPT the mathematical theorem as stated in R1. No required correction was identified.** This is a scientific assessment of the frozen packet, not authorization to promote material or a claim of any conclusion beyond its stated local scope.

Reviewer: `/root/research_review_b`, a fresh isolated reviewer distinct from the listed authors/assembler `/root`, `/root/transport`, `/root/population`, `/root/nonlazy`, and from the relevance selector. Review date: 2026-09-11.

## Scope, isolation, and verified inputs

I read the neutral assignment and manifest, all 1,841 lines of `R1_PROOF.md`, and all 1,310 lines of `R1_DEPENDENCIES.md`, including the complete Gaussian-program, continuous-value, neural-response, weighted-response, and finite-dynamics proofs. One combined display was truncated; separate overlapping reads repaired its omitted portions. Effective complete proof coverage was lines 1–400, 401–759, 760–1100, 1101–1450, and 1451–1841. Effective complete dependency coverage was lines 1–215, 216–450, 451–700, 701–920, 921–1120, and 1121–1310. No scientific passage was accepted on the strength of a summary alone.

I also read the required `solve-math-rigorously` and `investigate-conjectures` skills and the latter's complete `research-contract.md` and `adversarial-audit.md` references. I did not access the live study README, author startup/workflow material, study history, prior review verdicts, another reviewer's findings, or live book/source files. Scientific reconstruction used only the frozen packet. The C.1/C.3 references in component prose were treated according to the packet's explicit wrapper: they are provenance references, and the needed existence, identification, and activity arguments must be supplied by this packet itself.

The two input SHA-256 hashes were computed from the files and matched the manifest exactly:

| Input | Verified SHA-256 |
|---|---|
| `R1_PROOF.md` | `b7f2a65252353d0e47af50da9895f7206d4e202dd591ac4342bf6a2696e036c1` |
| `R1_DEPENDENCIES.md` | `606fe87a97b91a8cad31a26d9e545c4b51ebefd582e55a7ba1b2311bfa2f9469` |

I additionally extracted each included proof component between its frozen markers, removed the wrapper's extra boundary blank lines, restored one terminal newline, and verified all five component hashes without opening their live counterparts:

| Included component | Verified SHA-256 |
|---|---|
| `THEOREM.md` | `e900b0a030dcf2ce6900c2f4dc78f49aa8eaf41174fe56e444e6c82d7a33be2d` |
| `TRANSPORT.md` | `482f460f9e611be16a93f0948da89836b44fe2a734f127333b39a8b756dccd51` |
| `POPULATION.md` | `7972d9f3e26d5972c3dae65e1ef5474584f99e01700b86fb4346a305f16e4552` |
| `ALGORITHM_AND_STATISTICS.md` | `088cfe42376671f49d94ab2c99c8b6c558c2644e9021fcf139ad2b169edc715f` |
| `NONLAZY.md` | `1a5ede04ff241efbb7596215d91822185471cc81f86f53891da9570a93b843f4` |

The manifest's hashes of the original whole book files were not independently recomputed: those live files are outside the assignment. The complete required excerpts are present in the hashed dependency packet; I found no missing mathematical input needed by this theorem.

## Contract and component verdicts

The target is the specified two-hidden-layer tanh network with first, middle, and stored-readout initialization variances `1`, `1/n`, and `1/n²`, unhalved mean-square loss, and stored-weight mobilities `(n,1,n)`. The population state retains the full two-coordinate first row, a bounded middle action with its actual adjoint, and the readout. Its topology is the sum of first-row L², middle operator norm, and readout L². The interval is one sufficiently small common positive interval depending on `Y` and the fixed model. Finite-width conclusions concern actual raw GD with linearly interpolated parameters and recomputed features, in probability, with arbitrary relative orders of width, sample size, and vanishing step.

| Component | Verdict | Essential reason |
|---|---|---|
| Gaussian programs, common actions, A.1/A.2 | Accepted | Conditioning, singular-query regularization, value completion, and source derivatives are proved in the needed fixed-program scopes; the reverse action is identified by finite adjunction and density. |
| Weighted C.2 response proof | Accepted | The derivative-row and single-pulse bounds retain weighted time factors and admit noncircular cap selection independent of the number of inputs and mesh points. |
| Full-row transport | Accepted | The estimate uses only individual reference tails, one power of the cutoff, and the correct changing-input factor. |
| Population construction and uniqueness | Accepted | Euler completion and then law completion occur in the full state space; field continuity identifies the strong integral equation, and inherited integrated tails prove uniqueness. |
| Actual GD and simultaneous limits | Accepted | The finite proxy is identified only at fixed reference law/mesh; same-width deterministic stability subsequently handles arbitrary actual data and steps. |
| Replacement and expected gap | Accepted | The replacement cost and ghost exchange prove precisely the displayed order of expectation, absolute value, and time supremum. |
| Positive finite-time activity | Accepted | Actual-flow expansions with checked physical factors and positive adjunction identities yield paired activation displacement in both layers, which transfers to an open family. |

## Gaussian action and response audit

In dependency lines 216–274, the adaptive conditioning argument conditions successively on the transcript. A new query is then a linear observation of just one residual matrix factor. The minimum-Frobenius-norm conditional mean satisfies both forward and transpose constraints; its complement is exactly `P_(U-perp) Wtilde P_(V-perp)`. The removal of the finite-rank projection of fresh noise costs vanishing normalized mean square. This supplies the induction for nonsingular fixed query Grams.

I checked the source-response cancellation in dependency lines 298–335: orthogonality of the new input residual to the old forward inputs removes the deterministic part of old transpose answers; Gaussian integration by parts then yields the derivative coefficient that cancels the old response term. Independent oriented source groups do not make the two operator directions independent.

The singular-query argument in lines 339–382 does not assume continuity of a pseudoinverse. Each new independent perturbation gives a strictly positive limiting innovation variance. At fixed program length, matrix norm and coordinate Lipschitz bounds control the finite perturbation error. Covariance square roots and bounded first source derivatives then permit removal of the perturbation. The contracted derivative convention remains invariant on singular supports.

Two independent algebraic attacks were useful:

1. Let a root-derived input `h` be independent of the middle matrix, with `E h²=v`, and write `z=A_0 h`. The response rule gives `A_0* z=h+ζ`, where `E ζ²=v` and `ζ` is independent of `h`. Thus `||A_0* A_0 h||²=2v`. A further forward call gives a fresh forward source plus `z`, with covariance `v` with the old source, and hence `||A_0 A_0* A_0 h||²=5v`. I independently enumerated Gaussian Wick pairings for normalized traces of `(WᵀW)^k`, `k=1,2,3`, using exact integer index-identification counts. The resulting polynomials were `1`, `2+1/n`, and `5+6/n+4/n²`. Their leading terms agree with these response calculations. Resampling an independent reverse matrix would fail this check.
2. Duplicate the same forward query, so its two named sources coincide almost surely. For a reverse input `b(ξ_1)-b(ξ_2)`, the input is zero, its reverse innovation is zero, and the two expected derivative coefficients cancel against the identical original inputs. This tests the singular formal-source convention rather than relying on individually unique derivative coefficients.

The common generated space construction, dependency lines 402–440 and proof lines 626–701, transfers the high-probability finite operator bound to each named rational probe, identifies zero differences, and uses dense smooth cylinders to complete the action. Passing the finite transpose identity through this dense family gives the actual Hilbert adjoint on the whole generated spaces. Adding law-specific arbitrary operator extensions is unnecessary. A.1 supplies continuous at-most-linear value operations; A.2 separately supplies source derivatives for bounded gates times unbounded fields, using fixed-program polynomial derivative envelopes. These are not being used as uniform growing-program theorems.

For C.2, I reconstructed equations (24)–(32), dependency lines 845–955. A forward derivative row obeys a pathwise Gronwall estimate involving a weighted sum of absolute backward fields. Its exponential moment is bounded by Jensen using individual subGaussian marginals, without independence in time or a Gaussian maximum estimate. A single reverse-source pulse enters with exactly `Delta omega_b`; differentiation of subsequent history preserves that factor. Therefore the constants do not divide by a small atom weight.

The response caps are chosen first in their stated bottom-up and top-down order, then the time is reduced so the exponents improve the caps. The causal construction at lines 995–1023 uses past lower backward fields to construct a current forward coefficient, and already constructed upper backward fields to construct a current lower backward coefficient. I found no dependence on an unconstructed value of the same coefficient. General positive step lengths and a final partial step preserve the total-time and single-pulse estimates. The resulting tail bounds therefore apply to the reference Euler states actually used later.

## Full-state transport, existence, and uniqueness audit

The finite gradients in dependency lines 1121–1159 produce the three terms of (T2), including `1/n` in the finite middle rank-one action and no such factor in the stored readout update. The full first row uses normalized Frobenius norm, while the middle comparison uses operator norm. These normalizations give the stated mobilities and physical factors two.

In proof lines 280–364, forward differences are controlled by full-row error plus input distance. The gate estimate splits only the reference multiplier. Passing backward through the bounded adjoint multiplies its existing error by a state bound; it does not introduce a second cutoff factor. The next gate adds another cutoff term. The explicit term `bar r bar delta^1 (u-u')` correctly accounts for the input vector in the first-row gradient. Rank-one operator differences require only L² factor bounds. Integrating against a coupling leaves precisely the second marginal's weighted individual tails.

The cutoff optimization is valid: the Gaussian remainder `exp(-cR²)` dominates the propagation factor `exp(aR)`, and taking `R` proportional to `sqrt(log(e/q))` gives the claimed modulus. At `q=0`, sending `R` to infinity proves equality. At `q>1`, the proof uses the bounded-state estimate and never evaluates the local logarithm outside its domain.

The essential continuity fact is proved by truncating a fixed multiplier, not by assuming that a nonlinear map is Fréchet differentiable on all of L². Joint continuity in state and input gives compact, separable integrand ranges. Consequently the Banach-valued integrals exist even though the ambient bounded-operator space need not be separable. The middle integrand is also continuous in Hilbert–Schmidt norm with an integrable norm bound, so learned increments really are Hilbert–Schmidt.

Finite-law Euler paths are Cauchy in the complete full-state path topology by (P13a). Their preceding grid states converge uniformly to the limiting path, allowing the continuous field to pass to the strong integral equation. A second full-state Cauchy argument completes the finite laws to every compactly supported observation law. This proves state existence and a strongly C¹ equation, not merely convergence of predictions.

For arbitrary laws, proof lines 941–984 first transfer bounded continuous truncations of the exponential moment, then use monotone convergence and Cauchy–Schwarz in the observation law. The resulting bound is an integrated input-law tail, exactly the hypothesis required by transport. It does not assert a common almost-sure bound over a continuum of inputs or times.

Uniqueness compares any competing strong continuous integral solution against this constructed reference; only the reference needs tails. The first-exit estimate bounds the competing solution. The zero-error bound `C exp(aR-cR²)` then proves uniqueness. The same argument applies to a continuation from a reached state in the stated ball. Restarted Euler approximations are compared against that existing continuation, so Gaussian tail estimates for arbitrary restarted states are not silently assumed.

## Actual algorithm, statistics, and observable audit

The proxy (A3) uses the actual finite initial arrays, including the random readout. Its oracle coefficients are causal deterministic contractions of earlier population Euler nodes, fixed before width tends to infinity. For each fixed reference law and coarse mesh there are only finitely many such nodes. The middle-action and transpose discrepancies are finite sums of vanishing contraction errors times bounded-RMS nodes. Recomputed backward gates use the reference-tail cutoff argument. Hence the assigned proxy velocity has a vanishing defect in the complete same-width comparison norm.

The stored readout has `E[||W_0^(3)||²/n]=n^(-2)`. It is neither deleted from GD nor silently identified with a zero finite vector. Its vanishing RMS is explicitly included when comparing the proxy recomputation with its zero-readout oracle. Tail transfer to the proxy uses continuous cutoff majorants and L² comparison, avoiding a discontinuous-test assumption.

Equation (A7) uses only a fixed proxy's Gaussian tails, while actual GD is controlled deterministically for every law on the initialization event. Fine and coarse preceding states differ from their interpolants by their mesh sizes times a uniform speed bound. This compares simultaneous raw GD updates and recomputed features, not an alternative transformed or blockwise optimizer.

I checked the limit quantifiers: at any desired error one first fixes a sufficiently large cutoff, then a sufficiently close finite reference law and sufficiently small proof mesh, and only then sends the actual width to infinity and actual step to zero. The actual training law enters only through its W1 distance to that fixed reference. Fixed passive-input and time nets give uniform prediction convergence, since the relevant forward maps have uniform state, input, and time moduli. No operator distance across widths or carrier spaces is asserted.

The same comparison and nets retain joint initial/current feature tuples. Their quadratic difference is controlled by joint second moments, yielding (A15); marginal feature convergence or predictor convergence alone is not used to identify displacement.

For random samples, the compact-space cell-mass argument proves W1 convergence in probability without an atomlessness or boundary-zero requirement. The comparison errors outside this W1 term involve only the fixed reference program and initialization, so the union-bound argument gives the unrestricted joint sample/width/step limit. Uniformly Lipschitz bounded squared-loss integrands then prove both risk limits.

For replacement, matching the unchanged observations costs at most `(2+2Y)/m`. I used the direct cutoff substitution offered in proof lines 1382–1384 to verify the stated bound; this does not require monotonicity of the raw displayed expression for every possible enlarged constant. The finitely many smaller sample sizes are covered by the uniform prediction bound. The ghost identity (A12) correctly exchanges `Z_i` and its independent copy and evaluates both algorithms at the original observation. Its uniformly bounded summands establish `sup_t |E gap_t|`. It establishes neither `E|gap_t|` nor an expectation of a time supremum.

## Boundary and nonlazy checks

| Attack | Outcome |
|---|---|
| Atomic laws and arbitrarily small weights | All law integrals remain finite weighted sums; C.2 retains each pulse weight and uses only sums of weights equal to one. |
| Coincident inputs with different labels | Forward/backward fields coincide at that input; integrating the residual uses its conditional mean label. No Gram inverse or inconsistent duplicate state is introduced. |
| Singular input/query Grams | The finite program's perturb-and-remove argument and derivative nullspace contraction apply. Transport and law completion never invert input Grams. |
| Zero conditional label mean | At `(w_0,A_0,0)`, backward fields vanish and the readout velocity is `2 int y H_0^2(x) dmu=0`. The stationary population solution is consistent with uniqueness and with the restricted activity claim. |
| One active direction and a passive first coordinate | For a law supported on `u=e_1`, the second first-row coordinate has exactly zero velocity and remains `g_2`. Keeping that coordinate permits correct passive-input evaluation and law changes. |
| `q=0`, `q>1`, and `m=1` | Zero is handled by the Gaussian cutoff limit; large transport distances and small sample sizes use deterministic bounded predictions. |
| Random finite readout | Its exact RMS variance calculation and explicit proxy term control it without changing the finite initialization. |
| Arbitrary relative limit orders | All Gaussian identifications are at fixed reference complexity; the actual growing dataset and fine history require only deterministic transport. |
| Paired initial/current features | The finite union of probes includes both times; squared displacement is a joint second-moment observable. |

For the activity reference, `G=I_2` and the upper initial sources are independent `N(0,q_0)`, with `q_0=E tanh²(g)>0`. I independently recomputed the factors in (6): `dot c(0)=2S`, `delta_a^2(t)/t -> 2U_a`, and `delta_a^1(t)/t -> 2b(g_a)P_a`. Since `y_0=2p` and `int_0^t s ds=t²/2`, the first representation increment is `2t² C_a+o_L²(t²)`, the learned middle increment is `2t² sum_b p U_b tensor h_b+o_op(t²)`, and the upper representation increment is `2t² E_a+o_L²(t²)`. The operator/field cross increment is of order `t^4`. Bounded-multiplier convergence justifies the activation limits along the existing flow without an unproved higher-order differentiability assumption.

The first adjunction identity is strictly positive because `xi tanh(xi) sech²(xi)>0` for nonzero `xi`; its cross-input term vanishes by independence and oddness. Thus `P_a` and `C_a` are nonzero. The upper positive quadratic identity retains both the moving-matrix contribution and the moving-lower-feature contribution, so cancellation cannot make all upper leading activation coefficients vanish. Consequently both averaged activation RMS displacements are `2c_ell t²+o(t²)` with positive `c_ell`.

The definition of `s_0` uses a downward-closed set of admissible times. Its positive supremum therefore makes the smaller specified `t_0=s_0/4` legitimate even without assuming that the supremum is attained. The positive `j_0`, law-continuity radius, and two-layer finite probability margin then follow. Small arc/label spreads give nonatomic laws in the same W1 neighborhood, and small angular perturbations give nonorthogonal two-input laws. No positive activity is inferred for every admissible law.

## Corrections, limitations, and decision

**Required mathematical corrections: none.** There is no blocking missing input, incorrect normalization, unsupported interchange of limits, or unresolved necessary bridge in the supplied argument. I do not require a presentation change for acceptance.

Actual checks consisted of complete line-by-line mathematical reconstruction, the boundary attacks above, input/component hashing, and exact finite Gaussian pairing enumeration. I ran no training experiment, made no finite-width accuracy claim, and did not use empirical agreement as a substitute for a proof. The Wick check is a limited independent consistency test of reused forward/transpose actions; acceptance rests on the full supplied arguments, not on those low-order moments.

The accepted conclusion remains local in physical time and qualitative in finite-width approximation. It does not establish a finite-width replacement rate, expected absolute generalization gap, excess risk, fitting, useful risk reduction, global well-posedness of the population equation from arbitrary states, or superiority of hidden learning over another model. The activity constants are positive quantities defined from the actual reference flow, not numerical performance guarantees.

**Final decision: ACCEPT R1 as a complete proof of its stated theorem within these limits.**

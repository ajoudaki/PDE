# Independent mathematical review B1

## Verdict

**No required mathematical correction found.** The Gaussian addition proves the stated fixed-map, fixed-scale empirical laws and their higher-moment obstruction. The Galerkin addition proves the stated internal identities for supplied regular solutions of its separately defined operator-transport model. Its parity conclusions retain their uniqueness conditions, and it does not claim a dense-network limit, training-time existence, or source-cutoff convergence.

This verdict uses the ordinary meaning of the “infinite-source comparison” in G.4: the displayed basis is countably infinite and the source projections exhaust that basis. An optional clarification of that notation appears below.

## Inputs and full-read attestation

I personally read the complete text, including every displayed statement and proof, of:

| Input | Lines read | SHA256 |
|---|---:|---|
| `studies/repository_refactor_2026_09_09/FINAL_GAUSSIAN_ACTION_ADDITION.md` | 1–196 | `f0c01e6ecc33433a454d1e00ff36f8221dc418ccee146b497bf5d8c02a4209dd` |
| `studies/repository_refactor_2026_09_09/FINAL_GALERKIN_ADDITION.md` | 1–350 | `1d22cf0feea55f62b148761bfb40136bec26191ae8d331e1f335ccc12f2bcae4` |
| `docs/NOTATION.md` | 1–98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

I also personally read `/etc/codex/skills/solve-math-rigorously/SKILL.md` and applied its proof-checking instructions. The three files above were the only mathematical inputs. I did not inspect other project files, Git or source history, earlier reports, or other reviewers’ verdicts. I did not delegate, run experiments, or edit either candidate. The input hashes were checked again after the mathematical audit and were unchanged.

## Gaussian addition: complete audit

### Setup and first conditioning, lines 8–61

The bump assumptions imply boundedness, smoothness, and a finite Lipschitz constant for each fixed positive scale. Its plateau has positive Gaussian measure, so the normalization `v_epsilon` is strictly positive. The two other constants are finite and strictly positive. No uniform bound on the scale-dependent coordinate derivatives is used.

Each row sum of the matrix has variance one, and different row sums are independent. Conditional on the row sums, the matrix has mean `y 1^T/n` and Gaussian residual obtained by projecting each row onto the orthogonal complement of the constant vector. Conditional on `y`, the vector `e` is fixed, the coordinates of `Z_n^T e` have variance `v_n`, and multiplication by `P_0` yields (A.4). The mean `a_n 1` and covariance `v_n P_0` are correct.

### Second conditioning and the third call, lines 63–95

The compatibility identity `1^T q = y^T e = n a_n` makes `q-a_n 1` orthogonal to the constant vector. Consequently the affine matrix in the first two terms of (A.5) satisfies both observed constraints. Each of those terms pairs to zero with every homogeneous matrix satisfying `M1=0` and `M^T e=0`. The commuting left and right projections in the last term are exactly the Frobenius orthogonal projection onto that homogeneous subspace. Orthogonal coordinates of an isotropic Gaussian are independent, so the displayed conditional covariance and conditional mean follow without treating the transpose as independent.

The exceptional event `v_n=0` is handled correctly. The plateau event is sufficient to force `v_n>0`, giving the stated exponentially decreasing upper bound. On its complementing exceptional event, `e=q=h=T=0`. Auxiliary definitions on that event do not affect the convergence claims.

Given `(y,q)`, the vector `h` is fixed. The first two affine terms applied to `h` produce exactly `m_n y` and `b_n e`. A fresh matrix of entry variance `1/n` applied to `P_0 h` has isotropic row covariance `s_n^2 I`. The remaining left projection therefore gives precisely the Gaussian term in (A.6).

### Empirical convergence, lines 100–148

Evenness of the bump gives `E[Y psi(Y/epsilon)]=0`. The law of large numbers thus gives the stated limits of `a_n` and `v_n`. Inequality (A.7) accounts separately for the scalar mean, variance, and removed constant-direction projection. Each term tends to zero in probability at a fixed scale.

The fixed Lipschitz constant of the map `q -> tanh(q/sqrt(v_epsilon))` transfers the normalized Euclidean error to `h`. Boundedness of `h` and `tanh(g)` then yields the limits of its empirical mean and variance, hence `m_n -> 0` and `s_n^2 -> sigma^2`. The two Cauchy–Schwarz terms displayed at lines 119–121 correctly control the mixed pairing needed for `b_n`. Gaussian integration by parts has a vanishing boundary term, and gives `E[G tanh(G)]=c`, so the coefficient converges to `c/sqrt(v_epsilon)`.

Conditional on the transcript, the removed projection of `g'` has expected squared length one on `v_n>0`; after normalization its expectation is `1/n`. Markov’s inequality and `s_n<=1` make its effect vanish. All four terms in the comparison with `t^0` therefore tend to zero in probability. Independence of the fresh `g'` from the transcript makes the ideal row tuples iid. The ideal column tuples are also iid. Their second moments are finite.

The finite-partition and second-moment-tail argument at lines 141–146 supplies empirical convergence in `W_2`; coupling corresponding coordinates transfers that convergence to the actual tuples. These arguments concern separately the row and column populations and do not require, or assert, a pairing between them. They prove convergence in probability and need no common almost-sure construction across widths. The text correctly avoids inferring empirical higher-moment convergence from `W_2` convergence.

### Moment obstruction and its scope, lines 152–196

Conditioning on `Y`, convexity of the absolute `p`th power removes the independent centered Gaussian noise and gives the first lower bound. The bump support gives `v_epsilon <= 2 gamma_0(0) epsilon`; its plateau gives the stated lower bound for `E psi(Y/epsilon)^p`. The direction of both substitutions in the moment lower bound is correct. Taking the `p`th root gives the exponent `1/p-1/2`, which is negative for every finite `p>2`.

For a fixed scale the shift is bounded, so all finite output moments exist. The input distribution is the same `tanh(G)` at every scale, with essential supremum one and a fixed positive finite `L^p` norm. Independence and centering of the Gaussian innovation eliminate the cross term in the output second moment; the shift contributes exactly `c^2`. Thus the constant second moment and diverging higher moments are compatible.

The common-realization assertion is explicitly conditional on a single actual bounded `L^2` operator, its adjoint, and the stated program laws being present together. Under that condition, the displayed inputs belong to `L^infinity` and to every finite `L^p`, and the diverging output norms disprove every finite operator bound of the two stated types. Countably many scales suffice for this conclusion. The standardized output remainder already exists on the row probability space and has the joint law needed for the Gaussian innovation, so an additional coordinate root is unnecessary. No joint independence between scales is used. Transpose invariance of the initial matrix law permits the same argument in the reverse orientation.

The order of limits remains width first at each fixed scale, then scale tending to zero. The text does not convert this into a shrinking-scale finite-width theorem, a positive-time training claim, or a statement about a family with uniformly controlled coordinate sensitivities.

## Galerkin addition: complete audit

### Model and depth equations, lines 3–118

The source count, continuous residual-depth variable, endpoint fields, row coefficients, Gaussian labels, and conditional row law have compatible types. The input map and half-sum loss are explicitly distinguished from the established network conventions. In particular, the unnormalized sample factor in the input derivative is `x_a^T x_b`, as later used in the kernel.

The uniform polynomial envelopes, together with the finite source family and Gaussian moments, supply integrability for the displayed products and the time/depth differentiations used subsequently. These are hypotheses on supplied paths and variations; the candidate does not present them as an existence theorem or as regularity of an arbitrary `L^2` state.

For the operator in (G.4), Bessel’s inequality for the source coefficients and Cauchy–Schwarz in the row probability space give the stated norm bound. The same estimate applies to the adjoint. Conditional expectation in `epsilon` is an `L^2` contraction, and `tanh` is one-Lipschitz, so the forward depth map has Lipschitz coefficient `gamma ||w(s)||_2`. Its `L^2` norm is bounded by `gamma`. Once the forward field is supplied, the adjoint is a linear equation whose coefficient is bounded by the same quantity, because `|phi'|<=1`.

The integrable-coefficient qualification at lines 97–103 is sufficient for the Picard integral argument. The factorial bound on iterated differences yields convergence and uniqueness, and finite subdivision gives continuation on the depth interval. The earlier uniform domination ensures this coefficient is integrable in the setting of the stated identities. This establishes only depth solvability with the current row state supplied, as the candidate expressly states.

The training equations use only the retained current state and fixed data. Their restart assertion is properly conditioned on uniqueness in a declared class. Autonomy is not used as a substitute for a uniqueness proof.

### Adjoint and transport identities, lines 122–157

Expansion of the finite source sum proves (G.6); all its pairings are between the declared source and target probability spaces. Both operators use the same coefficients. At initialization the coefficients are `sigma_w epsilon`, and the source projections of `u` are deterministic scalars. Integration by parts in each Gaussian coordinate gives `sigma_w^2 H[u]_j E[g']`, producing (G.7). Boundedness of `g` and `g'` justifies the expectation and vanishing boundary term. The formula is correctly restricted to initialization.

For fixed depth and slow label, differentiation of the pushforward test integral follows from the characteristic chain rule. The displayed velocity depends on the Gaussian label through its current row value `w`, with the slow fields supplied; it is therefore a well-defined velocity for the conditional law. The domination hypotheses justify passing the derivative through the Gaussian integral. This gives exactly the distributional conditional continuity equation in (G.8).

### Variation, kernel, loss and clock, lines 159–234

The linearized forward equation contains both required terms: variation of the row coefficient and variation of the projected hidden field. Pairing it with the adjoint and differentiating the slow pairing cancels precisely the latter term. The initial hidden variation is `delta W^{in} dot x_a`, and the terminal adjoint equals `W^{out}`. Differentiating the readout contributes the remaining endpoint term. These facts give all three terms of (G.9), with their displayed signs and factor `gamma`.

The variational statement is restricted to admissible differentiable variations with the required domination. It does not assert Fréchet differentiability on a bare `L^2` neighborhood. Each of the represented derivatives in (G.9) is square-integrable in the corresponding factor of the declared characteristic metric.

Substituting the training velocities into (G.9) produces the two endpoint terms and the row term in (G.10). The row inner product retains the projected pairing `sum_j H_ja H_jb`; replacing it with a full hidden-field inner product would not follow from this model. For every coefficient vector, the three kernel quadratic forms are exactly the three squared norms listed in the proof. The kernel is therefore positive semidefinite, and both equalities in (G.11) follow.

Integrating the nonnegative squared speed gives total path energy at most the initial half-sum loss. Cauchy–Schwarz in training time then gives the stated displacement and increment bounds. For full mean-square loss, `lambda=2/m` is correct: the velocity and output velocity acquire one factor of `lambda`, while loss dissipation and squared speed acquire two. This preserves the stated physical-time convention.

### Parity and source counts, lines 238–298

The generating identity proves the parity of the one-dimensional Hermite polynomials; taking products and normalizing gives the displayed multivariate signs. Under (G.12), change of Gaussian slow variable gives transformed source coefficients `-J H`. Combining this with `w -> Jw` changes the preactivation’s sign. Oddness of `tanh` and evenness of its derivative then give the stated transformations of the forward, adjoint, and row derivative fields. In the adjoint expectation the coefficient is transformed by `-J`; the matching source-polynomial parity gives the required adjoint equation. Predictions, hence residuals for arbitrary labels, remain unchanged. The row and endpoint velocities have exactly the required transformed signs.

The initial endpoint fields and Gaussian row law are fixed by this transformation. The subsequent symmetry assertion explicitly requires uniqueness of the conditional initial-value problem in an invariant class. Under that condition the slow fields are odd, so their even-mode coefficients vanish. The corresponding row velocities are zero, leaving those row coordinates at their centered independent Gaussian initialization.

With the slow fields supplied, the odd-coordinate vector field is locally Lipschitz in its finite-dimensional row variable and has no even-coordinate dependence. Uniqueness of that characteristic ODE therefore makes its solution independent of the even Gaussian coordinates. The product defining `Delta_a` retains this independence. Centering then gives zero even-source adjoint coefficients, as claimed. This argument proves absence of even-source contributions to the displayed forward and adjoint fields; it does not make the operator vanish on arbitrary even test inputs.

Appending an even shell can consequently be realized by appending independent unchanged Gaussian coordinates. The old forward, adjoint, and endpoint fields and the old active row coordinates still solve the enlarged model. With the stated compatible existence and uniqueness assumptions, this gives the claimed equality of the symmetric physical solution. No source-cutoff convergence is inferred.

For four Gaussian slow coordinates, the degree multiplicity is correctly counted by `binom(k+3,3)`. The totals through degrees one to five are `5,15,35,70,126`; the counts of retained odd-degree modes are `4,4,24,24,80`. These are parity-allowed mode counts, not a claim that every such coefficient must be nonzero for every dataset.

### Hilbert comparison and ambient obstruction, lines 302–350

The independent Gaussian coordinates form an orthonormal family in scalar `L^2`. Orthogonality makes the series defining `Iu` Cauchy and gives its isometry identity. Bessel’s inequality gives square summability of the proposed adjoint coefficients. Pairing partial sums with arbitrary `u`, then using `L^2` convergence, identifies the displayed series as the actual Hilbert adjoint. No differentiability of its argument is required.

For a square-integrable Hilbert-valued row `c`, Cauchy–Schwarz makes `E[cv]` a well-defined Bochner expectation and gives the stated norm bound. Pairing with arbitrary unit vectors verifies the learned-row adjoint. Adding the two bounded operators therefore gives a bounded operator and bounded adjoint.

In the infinite-source setting, every finite source projection omits some basis vector. Testing the adjoint on the corresponding unit Gaussian coordinate gives the lower bound one for the tail norm, and the contraction estimates give the matching upper bound. Thus bounded `L^2` energy does not give a uniform tail estimate. For the exhaustive basis projections, a finite net and the projection contraction bound give uniform convergence on a fixed compact set. The infinite-dimensional energy ball is not such a compact set.

Finally, the multiplier map is well defined into `L^2`, because `|phi'|<=1`. The sequence `z_N` approaches zero in `L^2`, with the other argument held fixed at the square-integrable Gaussian `a`. On its support, `|a|>N` and the derivative difference is the fixed nonzero number `sech^2(1)-1`. The norm ratio in lines 340–343 therefore diverges, disproving local Lipschitz continuity at the stated point. The candidate correctly treats this as an ambient obstruction rather than an example of a reached training perturbation.

## Self-containment and scope

The nontrivial Gaussian reuse calculation, source adjoint, variational cancellation, symmetry transformation, compact-set argument, and multiplier counterexample are supplied within the candidates. The uses of basic Gaussian integration by parts, laws of large numbers, Cauchy–Schwarz, Hilbert orthogonality, and elementary integral iteration have their relevant integrability or coefficient hypotheses checked. I found no silent dependence on a specialized matrix-program theorem, transport existence theorem, source convergence theorem, or network-limit theorem.

The notation contract is respected in the substantive matters checked here: transpose versus actual adjoint; separate row and column pairings; finite normalized factors; explicit different initialization and loss; physical training time versus residual depth; and separation of an internally defined operator model from a trained dense-network limit.

## Optional clarity only

These suggestions are not necessary mathematical corrections and do not change the verdict:

1. At Galerkin lines 302–305, explicitly say that `H` is infinite-dimensional, and define `Pi_K` as projection onto the first `K` basis vectors. This spells out the already indicated infinite-source setting and the exhaustion used at lines 325–332. If one instead allowed a finite-dimensional `H` and its identity projection, the stated tail supremum would of course be zero rather than one.
2. In the mode-count table, “Parity-allowed odd modes” would make explicit that special data can leave some odd coefficients zero.
3. In the Gaussian convergence statements, “for the Euclidean metric on the displayed tuple spaces” would explicitly record the conventional metric used by the coordinate couplings. In the Galerkin increment bound, a second training-time symbol such as `tau` would avoid temporarily reusing the residual-depth symbol `s`.

No candidate changes are required for the proved conclusions at their stated scope.

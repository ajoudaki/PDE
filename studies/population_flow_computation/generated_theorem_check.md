# Scoped check of the fixed-graph generated-solver theorem

Frozen internal scientific review, 2026-09-12. This is not a promotion review
and does not assess milestone C or a physical-time-40 resource certificate.

## Outcome

The exact-arithmetic **training** convergence theorem in
`generated_error_proof.md` is valid for each fixed finite graph, positive
source noise, and fixed positive retained probe weights. In particular, its
same-sample coupling handles the actual adaptive response estimates. It does
not mistakenly apply iid concentration to generated rows.

The stated convergence of finite clean passive-query tuples is also valid,
including the implemented upper `D` and lower `Q` query fields, after making
the law-level coupling explicit as below. There is a real distinction between
that assertion and continuity of the code under identical raw query seeds:
the latter is not implied by the proof and is generally false for eigenvector
square-root factors. The original proof's principal-root argument needs this
qualification when it is applied to `paired_hidden_draws`.

The training arithmetic argument is a conditional residual theorem. It is
not a certificate for the existing float32/float64 implementation, its random
number generator, its acceptance gates, or its passive spectral factors.
Uninstantiated but constructively bounded training constants are not a flaw
in the mathematical consistency result. Unverified numerical residuals must
not be described as already instantiated bounds.

## Scope, coverage and provenance

The assignment was to inspect the fixed-positive-noise, fixed-finite-graph
generated algorithm against its deterministic-coefficient finite-program
limit, using only the following complete scientific inputs. Every line was
read; initially truncated combined tool output was repaired by separate
reads.

| File | Complete coverage | SHA-256 |
|---|---:|---|
| `generated_error_proof.md` | 1–473 | `ff905bfe932254478cbab7f88c5c233a087f9527a634ae497160710a04fbaa26` |
| `directional_solver_spec.md` | 1–109 | `a90c39aa17bf32d6649c459582027be442d6a56c2805fd9b5770ef4e3a70e332` |
| `directional_solver.py` | 1–532 | `eef9c3b2d039d1911d036c068ef52708681f921961d21c73e2b5c999fc9dee23` |
| `random_direction_route.md` | 1–277 | `6724036ca77cfa7e99d415ed627b2970e5ae08ae1dcd49eb0f5edfcc5d33bbfa` |

The supporting random-direction note was read as an identity derivation,
not as a prior review. No study README, prior verdict, empirical result,
other study, Git scientific history, or external scientific source was read.
Shared `AGENTS.md`, `RESEARCH_WORKFLOW.md`, the required
`solve-math-rigorously` and `investigate-conjectures` skills, and the latter's
research-contract and adversarial-audit references were read. The parent
received preliminary findings and requested that the passive law/seed
distinction be made explicit; no other reviewer's findings were supplied.

Checks consisted of complete static code/proof inspection, hand derivations
of the bounds and passive coupling, and source hashing. No simulation,
trajectory, execution of the solver, or numerical experiment was performed.
The input hashes were unchanged on recheck before writing this report.
Observed HEAD was `7f5306c9f862e16374704f8ef54dd13e2bfe2c72`; the shared index
was empty. Concurrent workspace changes were preserved. This report is the
only written artifact, and no Git mutation was performed.

The mathematical model under review is the supplied bias-free two-hidden
tanh source recurrence for the physical unhalved-loss clock, with lower
population roots `g ~ N(0,I2)`, `w=g`, and `K=c=0`. The coefficient
`gamma=-2*h*p*(f-y)` in code line 221 matches the supplied physical Euler
convention. The theorem allows a fixed positive-step mesh; the provided
Python configuration implements the constant-step subclass. The noisy
finite comparison program is the target here. Identification with the
unregularized network/adjoint law is explicitly outside the theorem and was
not independently rederived from unavailable book sections.

## 1. Causality, source responses and code correspondence

Replacing averages by expectations defines coefficients in a finite causal
order. At step `k`, lower `H,Hdot` are formed first; their averages define
the forward coefficients. Upper sources, fields and residuals are then
formed; their averages define reverse coefficients. Lower sources and the
simultaneous state update follow. None of these operations requires a
simultaneous unknown fixed point.

For the deterministic program, primal fields depend on Gaussian primitives
and deterministic coefficients, whereas directional tangents are linear in
the population's independent signs. Thus the weighted sign identity applies
to every historical response coefficient. The implementation's lower
`alpha` (line 209) multiplies `Hdot` by the dual probe `omega*Rminus`.
Upper `beta` (lines 223–227) uses the entire old directional tangent after
removing the known direct current pulse pointwise. It computes that old
tangent directly, avoiding a potentially poorly conditioned subtraction.
The current upper response is the ordinary mean of `c*ddphi(Z)`, placed only
on the current diagonal. There is no spurious same-step off-diagonal response.
The formulas in `_prepare_step` implement both state and frozen tangent updates
using the preceding state.

The empirical primal fields can depend on old signs through generated
coefficients. Their finite-sample response estimates therefore need not be
unbiased. The theorem does not claim otherwise. Equation (11), not the
frozen identity alone, controls this dependence. The warning and pooled
counterexample in `random_direction_route.md` are consistent with that
coupling, since their fixed-graph bias tends to zero.

Both covariance orientations are generated separately from the appropriate
opposite-layer saved fields. The Gaussian innovations and probes remain
separate between populations. The code does not equate matched row numbers
with matched neurons or introduce a trainable representative connector.

## 2. Positive covariance floor and training stability

Let `M_k=max_i |c_ki|`. Since `|tanh|<=1`, `sum_a p_a=1`, and
`|f_ka|<=M_k`, the empirical update gives

    M_{k+1} <= M_k + 2 h_k (M_k+Y).

Starting at zero and using `1+2h<=exp(2h)` proves (3). In the deterministic
program the same argument uses a deterministic essential bound. Thus the
entire retained `H` and `D` Gram matrices have diagonals bounded by 1 and
`C_0^2`, respectively. Adding `s^2 I` proves (4).

Every old factor is retained literally and all old input fields are
immutable. Consequently the block extension is the Cholesky factor of the
entire current empirical Gram plus `s^2 I`. For any old/new partition,

    x^T S x = min_y (y,x)^T K (y,x) >= s^2 |x|^2.

This includes singular clean Grams, duplicated data and `P<J`. No hidden
empirical rank hypothesis is needed. The first reverse Gram can be zero
because `c=0`; its noisy covariance is still positive. In particular, fixed
positive noise modifies the zero-readout initial reverse action. This is
allowed by the specified noisy comparison target, not an exact-neural-flow
identity at positive noise.

The Cholesky derivative formula and the bounds
`||L||op<=sqrt(Lambda)`, `||L^{-1}||op<=1/s` give (6). The segment between the
two complete covariance matrices retains both spectral bounds. Using the
same retained training innovations therefore gives the claimed pointwise
source coupling. There is no pseudoinverse or rank-selection discontinuity
inside the training recurrence.

## 3. Polynomial envelopes, ideal concentration and joint laws

At fixed graph size, all non-covariance primal and tangent operations are
finite sums, products and bounded tanh derivatives. The covariance sources
are bounded pointwise by `sqrt(Lambda)` times the norm of the retained
innovation row even when the covariance depends on that row through
feedback. These facts give polynomial envelopes for the empirical program
on the common Gaussian cutoff event. For the ideal program, expectation
coefficients are bounded by the Gaussian moments of the already constructed
envelopes. Polynomial moments can therefore be bounded without knowing or
integrating an inaccessible target trajectory.

The maximum norm on representative arrays makes averaging 1-Lipschitz.
All remaining dimensions are fixed by the graph. The number of vector
instructions, the degree of their polynomial bounds, and the coefficients
in (8) are independent of `P`. Dependence on `J`, `s`, and the smallest
positive `omega` can be very large, as the proof acknowledges.

For each averaging integrand evaluated on the ideal program, the rows are
iid and have a finite second moment. Chebyshev and a union bound yield (10)
without independence between averaging instructions. Decomposition (11)
then yields (12) by causal induction. It covers Gram entries, both response
orientations, residual feedback, old innovations, and scalar coefficients.
It neither conditions generated rows to be iid nor treats stop-gradient as
a statistical independence operation.

With fixed failure probabilities, the primitive cutoff is of order
`sqrt(log P)` and the ideal averaging error is of order `P^{-1/2}`. Any fixed
polynomial in that cutoff times `P^{-1/2}` tends to zero. Allowing arbitrarily
small fixed failure probabilities proves convergence in probability.

The empirical-law estimate (17) has valid constants: the two
clipping/quantization transports together contribute at most
`12 M_4/B^2+12a^2` after the three-leg squared triangle inequality; unmatched
discrete mass contributes at most `6dB^2 sqrt(K/P)`. For the proposed `B,a`,
the final term is of order `P^{-1/4}` up to a fixed dimensional constant,
and the other terms also vanish. Combining this with indexwise coupling
proves joint, not merely marginal, `W2` convergence.

This result covers tuples of the stated generated fields and their finite
polynomially controlled contractions/observables. It should not be read as
a theorem for every arbitrary smooth observable with unrestricted growth.
A square root applied to a squared norm may require its continuity modulus
at zero; convergence survives, but a linear maximum-error bound should not
be silently assigned to that last transformation.

## 4. Passive queries: valid law extension and seed limitation

### The limitation in a literal code coupling

Equation (22) correctly controls the **principal** square root of a positive
semidefinite matrix. `paired_hidden_draws`, however, uses
`eigenvectors * sqrt(eigenvalues)` (lines 318 and 360), together with
`np.unique` column reduction (lines 307 and 347). This is a covariance
factor, not generally the principal square root. Its eigenvectors and
column order need not be continuous.

For example, let

    S_e = [[1,e],[e,1]],   e>0,       S_0=I.

As `e` decreases to zero, ordered eigenvectors of `S_e` remain a rotated
orthonormal basis, while an eigensolver can return the coordinate basis at
`S_0`. Thus corresponding eigenvector factors need not approach one another,
although `S_e` approaches `S_0`. Applying those factors to one identical raw
Gaussian vector can leave an order-one error. A changing unique-column
ordering adds another possible raw-seed discontinuity.

Accordingly, (22) cannot by itself prove that the current code's passive
outputs approach ideal passive outputs using exactly the same raw query
draws. This is a proof/implementation correspondence issue, not a
counterexample to their laws converging.

### Completion for the stated finite-tuple law theorem

The following construction closes that law-level bridge without changing
the empirical algorithm's distribution.

1. Condition on the full saved empirical training state. Write the forward
   query covariance in the full requested coordinate list, before removing
   duplicate fields, as `S_+^P`. The code's reduced Gaussian draw, expanded
   back through `inverse`, is a Gaussian vector with precisely this
   covariance and the stated conditional mean. It has the same conditional
   distribution as `m_i^P + (S_+^P)^{1/2} z_i^+`, where `m_i^P` is that
   conditional mean, with full-coordinate independent
   standard normal vectors `z_i^+`. The assertion also holds when the
   covariance is singular. No continuous eigenbasis is needed.
2. Use these full-coordinate fresh normals in both the empirical-law
   realization and the deterministic comparison. The forward covariance is
   the clean Gram Schur complement in (21). Positivity follows from the
   full Gram plus training-block noise. The inverse has the fixed training
   floor; all its other inputs are finite contractions already controlled
   by the training coupling, with any new ideal query contractions included
   in the concentration list. Equation (22) then controls forward query
   sources, and the smooth gates control `Z`, hidden fields, and upper `D`.
3. Include **all** ensuing ideal upper-query averaging integrands in that
   list: `beta_old`, `beta_diagonal`, `DD`, and the reverse Gram/cross-Gram
   entries. For each fixed draw index, ideal upper rows are iid because
   their training coefficients are deterministic and their new query
   normals are independent. A fixed number of draw indices may instead be
   collected into one row tuple. Dependence between different averages is
   harmless. The integrands have polynomial Gaussian envelopes: `D` is
   bounded by `C_0`, while the old directional quantities have the training
   envelopes. Apply the same decomposition (11) after the forward query
   coupling to control every reverse coefficient.
4. Condition on the empirical training state and the entire forward-query
   array. The code's fresh reverse draw likewise has a full-coordinate
   Gaussian conditional law with covariance `S_-^P`. Its training block
   still has floor `s^2`, and its clean block is the empirical `D` Gram.
   Couple it through the full principal root to the ideal reverse draw,
   using independent full-coordinate `z_i^-`. A second application of
   (22), followed by the finite history/response correction in code line
   363, controls lower `Q`.

The two changes of Gaussian representation preserve the entire sequential
empirical algorithm law, including its subsequent moment feedback. They
are permissible for a convergence-in-probability statement about empirical
laws. The new primitives have fixed dimension per row, so the Gaussian
cutoff and ideal union-bound concentration arguments still apply.

For clarity about rates, let `t_P` be a polynomial in the cutoff times
`P^{-1/2}`, encompassing training errors and the added ideal sampling
residuals. A conservative forward-query row bound is a polynomial in the
cutoff times `t_P^{1/2}`; a reverse-query row bound is a polynomial times
`t_P^{1/4}`. Thus a conservative lower-`Q` rate is a logarithmic polynomial
times `P^{-1/8}`. These bounds tend to zero for fixed graph and finite query
list. The training linear rate is not the passive reverse rate.

The ideal enlarged same-layer row tuples remain iid and have finite fourth
moments. The elementary empirical-law estimate (17) applies with their
enlarged but fixed dimension. This establishes the requested `W2` tuple
result including subsequent `D/Q` feedback. Any fixed number of query draws
is covered; no growing query count or graph-uniform bound is asserted.

Exact repeated initial/current fields at time zero have equal conditional
means and zero variance in their difference. Full-coordinate principal-root
sampling therefore gives identical coordinates, as does the implementation's
deduplication. Independent extra noise on those passive coordinates would
change the target and is correctly excluded.

The marginal fixed-order Gauss–Hermite predictor needs only the scalar
square-root modulus and its finite weighted sum. Its convergence target is
that same quadrature applied to the ideal finite program. No quadrature-bias
certificate follows.

## 5. Finite precision and effectiveness

For the training recurrence, the expanded-operation tube argument is sound
as a conditional statement: exact triangular divisors are bounded below by
`s`, exact Cholesky radicands by `s^2`, and every other static positive
denominator/radicand can be assigned its supplied positive margin. Local
derivative bounds and the recursion then provide a finite amplification
constant. Given certified primitive/input errors and operation residuals
small enough to satisfy (19), induction proves the claimed training
arithmetic error bound.

The argument does not establish that the current Python run satisfies those
conditions. It provides no certified error for the Gaussian generator,
ordinary tanh/library calls, matrix products, triangular solves, or
eigenvalue acceptance checks. A positive computed pivot or small covariance
reconstruction diagnostic is not such a certificate. In particular, the
code's source-floor acceptance gate has its own tolerance and is not
automatically justified by a tube ensuring only positive pivots.

Moreover, the available implementation offers float32 and float64 rather
than an arbitrarily precise certified backend. Existence of a mathematically
sufficient precision does not imply that one of those two choices suffices
for an arbitrary requested accuracy or graph.

The passive query factorization is a separate numerical issue. Its clean
covariance may be singular; eigenvector factors do not have the training
Lipschitz property. A usable passive numerical certificate would need
verified covariance/factor residuals, treatment of any clipped eigenvalues,
and a law-level Gaussian coupling or an explicitly different sampling
implementation. Neither the printed precision label nor (22) supplies those
residuals for the actual spectral code. This part remains uncertified.

These numerical limitations do not refute the exact-arithmetic theorem or
its constructive sample bound. The polynomial moment and Lipschitz recipes
give finite computable upper bounds for fixed computable inputs with the
stated lower margins. They are not oracle constants. They may be enormous,
and no practical sample count, precision, or polynomial resource law has
been established here.

## 6. Missing supporting inputs and final claim boundary

The optional capped estimates in proof lines 118–138 cite C.4.7.N10–N18 and
use constants whose definitions and derivations are not present in the four
allowed files. Those book sections were not supplied within this review's
scientific scope and were not fetched. I therefore do not certify those
specific cap-dependent constants or their claimed uniformity over bounded
noise ranges. The elementary weighted Hilbert variance identity (2) and the
complete supporting sign derivation were checked. The main fixed-graph
theorem uses the direct polynomial-envelope construction and does not need
the optional cap-dependent estimates.

Likewise, the equivalence of the source construction to the original
initialized neural action/actual adjoint is not independently proved by
this scoped review. The theorem deliberately compares to its explicitly
defined noisy deterministic finite program; it does not need that stronger
identification at positive noise.

No false core fixed-graph convergence theorem was found. The required
correspondence clarification is the passive law-level recoupling above,
including its second singular-root stage for `Q`. Same-raw-query-seed
continuity and a concrete passive spectral precision certificate remain
unsupported. Noise removal, mesh refinement, finite-law approximation,
physical-horizon accuracy, and useful resource bounds remain separate
questions, exactly as the theorem's scope requires.

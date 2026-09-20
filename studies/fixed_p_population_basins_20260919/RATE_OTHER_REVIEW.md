# Independent internal review of the existing-rule and refresh rates

2026-09-19. Independent isolated mathematical check, not promotion.
The reviewer read only the neutral assignment, the frozen inputs below,
and the required rigorous-mathematics and adversarial-audit skills. No
other study, rate route, review, author history, or agent summary was read.
The reviewer did not edit any candidate, run a numerical experiment, or
perform a Git operation.

## Verdict

**PASS for the principal mathematical statements of both candidates.**
`RATE_EXISTING_RULE.md` proves a finite explicit instance-dependent
high-probability proposal budget for the held-state fractional-progress
Gaussian algorithm, including its stated fixed-duration flow variant.
`RATE_RESTART_ROUTE.md` proves the polynomial and logarithmic proposal
bounds for its explicitly changed optimizers. No major or fatal gap was
found. The minor effective-input wording qualification identified below
has been corrected and independently rechecked; no correction remains
outstanding for these reviewed claims.

This verdict does not establish a rate for accepting every strict
decrease under the original centered additive proposal law, ordinary
population gradient flow, SGD, a bounded-noise algorithm, or elapsed
computational time. It is an internal check of these frozen statements.

## Frozen inputs and provenance

SHA-256 hashes, checked before substantive reading and rechecked for the
two candidates and canonical book at the end of the audit:

| Input | SHA-256 |
|---|---|
| `RATE_EXISTING_RULE.md` | `1632f66b461f492468aa91d07b564694e1f146ca35187e37bd6862ef3e0c1c50` |
| `RATE_RESTART_ROUTE.md`, initially reviewed | `9f9d1db8445ff4853b907dfcdcb1a20a20d404c371439f6fa6b7dcb1c5c86fd6` |
| `RATE_RESTART_ROUTE.md`, corrected final version | `6a2c8b8d4e962962685e98175a7332d292c7e7676ffc19b622093a0f3c15b923` |
| `NOISE_GLOBAL_PROGRESS.md` | `70fc60f0554f54041c233d0f50f697e1cfab9a0dd834c8293470540818e11288` |
| `NOISE_RECURRENCE.md` | `644b6f9d306f7e8bde06c5fda5732e69bd960de88b9ee5e5ddcea5eaad1845e9` |
| `ESCAPE_AND_LIMITS.md` | `544a5fde3b224cfa30539754c5d27123b900c12ed3fe5df98df00d5a8dd20ac2` |
| `docs/global_nonlinear.md` | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |

Both candidates and all three dependencies were read completely. The
canonical inputs are the complete named B/C.1 span at lines 13161–13786
and D.3 at lines 15146–15528 in this book version. The supervisor's
initial D.3 line numbers were stale; the named section and corrected
range were confirmed with the supervisor. The initially supplied range
began in C.4.8; that accidentally read material was not used.

The existing-rule author discloses an earlier isolation breach. This
review does not erase that provenance issue or reclassify the original
attempt as blind. The present check was isolated from the exposed
material and from other reviewers.

## Canonical model checks

The book supplies the required fixed physical model: the joint laws
`Law(b_1,g)` and `Law(b_2)`, initialization `(g,0,D)`, actual matrix
transpose, and unhalved probability-weighted square loss. At orders
1, 2, 3 the polynomial dictionaries contain the constant and the upper
coordinate `X=tanh(xi_1)`; inverse-Cholesky normalization is invertible.
If the respective raw coordinate unit vectors are `e_0,e_X`, one can
take `l=L_1^T e_0` and `e=L_2^T e_X`. Thus
`b_1^T l=1` and `b_2^T e=X` exactly, without changing normalization.
All dictionary columns are bounded. The lower carrier is nonatomic
because it contains the continuous Gaussian `g_1`; `X` has positive
density throughout `(-1,1)` because `xi_1` is a nondegenerate Gaussian.

Oddness of both tanh layers makes duplicate/antipodal merging exactly
loss-preserving for compatible labels, including when merged masses
are unequal. The positive-definite feature Grams in the candidates
are therefore available for every fixed finite compatible dataset,
without a sample-count restriction. Their analyticity and distinct
absolute-slope argument correctly proves independence.

`ESCAPE_AND_LIMITS.md`, Section 1, correctly extends the fixed-dictionary
flow to every initial state in the stated physical Hilbert space. The
bounded dictionaries make its vector field locally Lipschitz on Hilbert
balls; loss dissipation bounds the readout, then the matrix, then the
row field on every finite interval. Its energy identity has exactly the
metric and factor needed by the candidate's flow-displacement bound.
No neural-width or hierarchy-limit theorem is needed for these rates.

## Existing fractional rule: verified probability and budget argument

1. **Robust centers and geometry.** Equations (4)–(14) produce rescue
   displacements in the fixed space of dimension `1+n+d_1 d_2`.
   The construction adds `Tv` rather than trying to cancel an arbitrary
   infinite-dimensional row field. Its readout correction has squared
   norm at most `n(1+R)^2/kappa`; the matrix correction is bounded by
   `||M_*||_F+R`. The chosen `T` bounds each of the exponential and
   Markov-error terms by `sqrt(a)/(8 C_R)`. The chosen radius then
   yields pointwise residual at most `sqrt(a)/2` and loss at most
   `a/4<a`. These estimates also cover large `a`, `R=0`, and one
   merged direction.

2. **Infinite-dimensional Gaussian mass.** Equations (15)–(20) do not
   misuse finite-dimensional translation formulas. Projection error of
   every center is at most `H D_N<=r/4`, uniformly because the center
   space is finite-dimensional. Trace-tail control gives Gaussian tail
   norm below `r/4` with probability at least `7/8`. The independent
   finite coordinate intervals contribute exactly the density lower
   bounds in (17), and their joint event lies within distance `3r/4`
   of the center. Hence the explicit `q(R,a)>0` is valid even when the
   centers have infinite Cameron–Martin norm. Neither state-ball
   compactness nor a uniform Gaussian translation bound on that ball
   has been assumed.

3. **Accepted draws.** The Gaussian exponential moment in (22) is
   correctly controlled at parameter `1/(4 Lambda)`; monotone
   convergence supplies the infinite-dimensional bound. The first
   accepted proposal has law `nu(· intersect A)/nu(A)`, not the original
   Gaussian law. Equation (24) retains the necessary factor `1/q` in
   its accepted-norm tail. A joint good event for waiting time and
   accepted norm needs only a union bound, not independence.

4. **Overshoot and adaptive stages.** Before accuracy `epsilon` has
   been attained, the actual acceptance threshold exceeds the fixed
   number `a=theta epsilon`. This is the correct direction of the
   inequality even after a preceding stage greatly overshoots its
   threshold. Conditioning on the history at each reached stage,
   the waiting and accepted-norm bounds propagate the deterministic
   radius envelope. A first-bad-stage union bound over at most `J`
   stages has failure probability at most `delta`. This proves (27)
   without assuming global boundedness or independence across stages.

5. **Flow and clock.** Energy dissipation gives displacement at most
   `sqrt(h ell_s)<=sqrt(h theta^s L_0)` on each fixed-duration segment.
   Thus (30) also covers flow-only stages and earlier accuracy hits
   during flow. `B_h+Jh` is valid for the declared clock charging one
   unit per proposal and `h` per flow segment. It does not charge the
   work needed to represent a Gaussian field, evaluate exact integrals,
   or solve an exact population flow.

6. **Effectivity and expectation.** Section 8 explicitly supplies the
   effective information needed to turn the finite spectral recipe
   into certified numbers. Positivity and convergence alone are used
   for the mathematical assertion; a noncomputable arbitrary covariance
   is not silently declared effectively computable. The distinction
   between high-probability budgets and unconditional mean hitting
   times is also correct. The latter remain unproved at later random
   states, despite finite conditional geometric means.

The centers and interpolating correction are proof witnesses. The
actual unchanged fractional algorithm needs only its fixed proposal law
and loss comparisons; it receives no fitted endpoint.

## Refresh and auxiliary search: verified rates and optimizer changes

The powers-of-three masses correctly exclude zero slopes and equal or
opposite sign-row sums. With the displayed `T`, each finite slope is
within `eta/4` of its limiting slope, so none of the needed separations
is lost. The bound `lambda_min(K)>=det(K)/n^(n-1)` follows from positivity
and `tr K<=n`. All this geometry is independent of label values.

For all-block refresh, the listed coordinates are an isometry into the
physical state space. Equation (9) is a valid global bound relative to
the fixed interpolant: splitting the matrix difference with `M_*` keeps
the coefficient independent of the candidate's matrix norm. A ball of
radius `sqrt(epsilon)/A_*` is therefore sufficient. Its Euclidean volume
and the Gaussian density lower bound give exactly `Q_d epsilon^(d/2)`.
Independent refresh selection supplies the factor `rho`; every useful
candidate is accepted before the target is reached. Equations (12)–(13),
including the mean hitting time and integrated expected-loss bound,
follow. The smaller readout family has the claimed dimension `n` and
Lipschitz constant one.

For the raw-coefficient auxiliary algorithm, `Q=K W K` is positive
definite and `V(a)=(a-a_*)^T Q(a-a_*)` exactly. Its favorable Gaussian
event has conditional probability at least
`q_0=e^(-2)/(2 sqrt(2 pi))`, including `n=1`, and has squared norm at
most `4n`. Substitution of the displayed step scale gives decrease at
least `kappa ell/(4n Lambda)`. Rejection controls the complementary
event. This proves the one-step expected contraction and, after
Bernoulli selection, the main-trial factor `1-rho gamma`.

Maintaining the auxiliary chain even when its offer is rejected by a
better incumbent is essential and is explicitly required. It preserves
`L_incumbent<=V(a)` and validates (22)–(23). Summing the geometric tail
after `ceil(log(1/epsilon)/[-log(1-rho gamma)])` gives (24). These are
accuracy bounds for `0<epsilon<1` from canonical initial loss one;
`epsilon>=1` is already satisfied initially. Conservative lower/upper
spectral bounds work in both the step scale and contraction constant.

The optional preconditioned norm identity and
`E||delta c||_2^2<=ell/(16 n kappa_w)` are correct. Removing the condition
number from the proposal count pays for a geometry-dependent inverse
and potentially large physical displacements. The raw algorithm does
not use that inverse or `K^(-1)y`; it uses labels only through actual
loss evaluations. Its proof may use the interpolant without giving
the algorithm an endpoint oracle.

Absolute refreshes and offers from the auxiliary fixed-feature family
are substantial optimizer changes. They can reset incumbent hidden
fields globally; small auxiliary coefficient increments do not make
those full-state jumps local. The logarithmic bound comes entirely
from the auxiliary positive-definite readout quadratic and gives no
credit to hidden-layer flow. The candidate states these limitations
correctly. Arbitrary finite intervening flow preserves the proposal
bounds but supplies no uniform physical-time bound.

## Closed qualification and remaining limits

The initial version of `RATE_RESTART_ROUTE.md`, Section 2, called its
geometry constants “computable,” while permitting arbitrary real-valued
input data and masses and granting exact population expectations. The
review identified this as a **minor** ambiguity between an explicit
mathematical definition and Turing computability. The supervisor changed
only that paragraph to “explicitly determined” and supplied the needed
effective-input and certified integration/spectral qualifications.
The reviewer read the correction and verified, by replacing that paragraph
with its original text and recovering the original SHA-256, that no
other candidate text changed. The supervisor then made the already used
accuracy range `0<epsilon<1` explicit immediately before (23); the
reviewer checked that phrase and likewise verified it was the sole
change from the corrected intermediate hash
`8d7ea7861ffe39930e19e9b547c879c0044a23d53f53198b6f3f96d33042e5a0`.
The final hash is recorded above. These clarifications close the minor
issues without changing any probability inequality or proof.

There is no uniform efficiency conclusion over collapsing input
geometries, increasing sample counts, small covariance eigenvalues,
or initial norms. The first candidate's recursive finite budget can
be enormously large; the refresh rate's exponent grows with dimension;
the auxiliary raw rate carries an explicit condition-number cost.
These are substantive limits already reflected in the formulas, not
unclosed steps in the proofs.

No additional scientific input is required for the stated internal
verdict. Promotion and any user-facing claim about practical training
remain separate decisions under the repository workflow.

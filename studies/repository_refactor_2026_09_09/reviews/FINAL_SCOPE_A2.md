# Independent complete mathematical audit A2

**Verdict: clean within the stated scopes.** I found no required mathematical
correction to candidates A–E. The packet supplies the specialized dependencies
used by these candidates, including the fixed finite Gaussian source theorem,
singular-query removal, common bounded actions with genuine adjoints, and the
two-query local construction needed by E. This verdict does not enlarge any
candidate into an unstated positive-time, global, finite-width, or GD result.

## Isolation, inputs, and full-read attestation

This was a fresh independent review. Its only scientific inputs were the three
files below. I read every line of all three, including the entirety of the
dependency packet, rather than selected sections. One truncated tool display
inside the source-rule proof was explicitly reread without truncation. I did
not consult another review, verdict, project document, study, Git history, or
external scientific source; I did not delegate or run experiments. I read the
required `solve-math-rigorously` skill and checked applicable instruction-file
locations. The only calculation outside the text was bounded deterministic
rational arithmetic. The only file written was this report.

| Scientific input | Lines | SHA-256 |
|---|---:|---|
| `studies/repository_refactor_2026_09_09/FINAL_SCOPE_ADDITION.md` | 1,254 | `48a67ae44c8bf628d9cafe88f6d96a179e9ffca4b12440f3f68820212e76d877` |
| `studies/repository_refactor_2026_09_09/reviews/FINAL_SCOPE_DEPENDENCIES.md` | 4,511 | `ec849bf098b9c48da4b10f3be63b92acc89ba1de3ff25412634948928769ec51` |
| `docs/NOTATION.md` | 98 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

Total scientific input: **5,863 lines**. Hashes and line counts were checked
both before reading and immediately before writing; the inputs were unchanged.
Line references below refer to these exact versions. “Addition” denotes the
first file and “Dependencies” the second.

## Complete dependency coverage

- **Finite model, Dependencies 8–214:** checked the first-row scaling, all
  gradient blocks, four kernel factors, residual-free backpropagation,
  dissipation, finite-endpoint continuation, and width-uniform RMS bounds.
  The substitution `W^(1)=sqrt(d) V^(1)` is an isometry of the stated first
  metric, so the two storage conventions agree. Loss factors remain explicit.
- **Part II.A–B, 219–789:** checked the exchange/sign transformation, its
  distinction from samplewise finite symmetry, the exact feature factor
  `1/2`, learned memory terms and source derivatives, the zero-variance-slot
  base case, and the ascending-forward/descending-reverse induction. No
  unknown current bottom response is used to prove its own bound. Exact
  arithmetic confirms `V*=3067/3200`, `Q*=24829/19200`, and
  `U*=71063018523/73728000000<97/100`. The forward margin is
  `3/2-49/36-3/25=17/900`. The exponential estimates and resulting
  `E exp(q^2/16)<2` are consistent with these constants.
- **Part II.C, 791–1288:** checked common-space construction, fixed-cap
  Picard/Euler comparison, the attained pointwise readout constraint, and
  the asymmetric two-query estimate. Each new gate contributes a cap times
  a forward discrepancy; it does not multiply the preceding query error by
  another cap. The reference tail is at most `32 exp(-R^2/256)`, which beats
  every fixed `exp(CR)` comparison factor. This constructs the uncut strong
  flow and proves uniqueness/reached-state restart without competitor tails.
  Rank-one estimates also give Hilbert–Schmidt convergence. Checked the
  physical comparison without a false finite scalar clock, ordered
  observational truncation, velocity continuity, path interpolation, and
  squared-speed/increment contractions.
- **Part II.D, 1292–1629:** checked separation and nonaffinity, top backward
  covariance positivity, its transfer to lower layers, motion pairings, and
  the initialized source/acceleration calculations. The same-label positivity
  arguments in this part are not prerequisites silently imported into E.
- **Part III.M/F, 1635–2453:** checked all model and topology declarations and
  the complete Gaussian-program foundation. Adaptive conditioning preserves
  the product of residual Gaussian matrix laws. The minimum-norm conditional
  matrix satisfies both constraints. The removed finite-rank noise projection
  has expected normalized square `rank(U)/n`. Gaussian integration by parts
  cancels the regression response and gives full input second moments as
  source covariance. Adding distinct small input noises makes fixed query
  Grams nonsingular; bounded finite-program errors and covariance-square-root
  continuity remove them. The proof does not assume pseudoinverse continuity.
  Checked causal scalar feedback, the countable dense generated language,
  bounded-action extension, exact adjunction, HS norms, multiplier continuity,
  curve chain rules, scalar Fréchet differentiability, and fixed-cap Euler
  errors. These are full internal proofs, not citations to an unavailable
  specialized limit theorem.
- **Remaining Part III.S/G/V/N/A, 2455–4511:** read and checked the controlled
  source bootstrap and its stage order, gain inequalities, augmented-input
  geometry, residual/control clocks, cap removal and full observation bridge,
  initial backward/forward innovations and derivative-valid nested clips,
  acceleration coefficient `18`, and regression/activation-class arguments.
  The large-gain global theorem retains its own activation and clock; it is
  not used to promote B’s formal coefficients or D’s conditional lemma into
  an unrestricted nonlinear flow theorem. No missing specialized dependency
  was needed to establish the five additions.

## Candidate A: verified

**Addition 11–256.** The order-one stored readout is stated explicitly and is
essential: it gives a nonzero initial hidden kernel despite a prediction of
order `n^(-1/2)`. The four terms in (A.1) have the correct raw metric factors.

The initialized closure is justified by successive bounded clips. Centering
of the independent clipped readout kills the first response; the independent
centered clipped reverse innovation kills the next response. Bounded gates,
operator norms and the previously identified squared tails remove both clips.
This yields exactly `s3`, `s2`, `s1` and (A.5), including all four blocks.
Conditioning only on the hidden initialization makes the initial reverse
queries Gaussian linear forms in the readout. Their stated variance bounds
give (A.6) and the coordinate maximum without independence between coordinates.

The signed feature flow has bounded readout and then successive bounded
matrix norms on every compact feature interval. The path-length inequality
(A.7) and rank-one bounds give uniform `O_P(sqrt(s))` forward motion. The
entropy/Jensen calculation (A.8) is valid also at zero multiplier mass.
Every backward gate is paired with its fixed initial multiplier, so the
reverse recursion has one `sqrt(s log(e/s))` rate, without iterated logarithms.
The initialized-column estimate then gives (A.3). The clock
`s(t)=2 integral |r| <=2t|r(0)|` transfers these statements to physical time.

For label zero, `r(0)=O_P(n^(-1/2))` and residual magnitude decreases. Thus
every fixed physical horizon occupies a vanishing feature interval, proving
the stationary limit (A.4). The identities (A.9) differentiate exactly;
their integrated second form and `sech^(-2)=1+2 Phi` give (A.10).
The static concentration example is compatible with those bounds and is
explicitly not a reachable-state assertion. No nonzero-label positive-time
tail theorem, feature-learning theorem, or raw-GD estimate follows here.

## Candidate B: verified as initialization and formal coefficients

**Addition 259–411.** The Gaussian characteristic-function identities (B.1)
give the three initialized Grams and unit diagonals. Tensor-power expansion
and the displayed interpolation polynomials prove strict positivity for
distinct normalized inputs even with singular `G`; repeating in a Gram
realization is legitimate.

Differentiating the actual top input gives `J3`; differentiating the next
gate gives `J2`, with its negative diagonal curvature term. The Gaussian
innovations have the full `R3`, `R2` input covariances. The clipped extension
has integrable first-source-derivative remainders, and bounded actions pass
the finite RMS errors. Strict positivity of `R3` follows from full Gaussian
support and intersecting nonzero sets of the two trigonometric factors.
Innovation covariance plus the tensor-product Gram argument gives strict
positivity of the remaining `R` matrices and `G circ R1`.

With `gamma=2/m`, the first readout coefficient is `gamma h_y`; hidden
acceleration is `gamma^2 J_y^* h_y`. Consequently
`y^T M y=gamma^2 ||J_y^*h_y||^2`. The hidden blocks contribute this quantity
to the quadratic coefficient and the readout block contributes it again,
which checks the factor `2` in (B.6). This is correctly presented as a
formal coefficient identity, with no analytic remainder or newly
constructed trajectory. The finite exponential formula, regression error
`1-2/e`, and rejected all-`p` tail estimate are also correct: the one-step
query has variance `2h^2(1+exp(-8))`, so its Gaussian `L^p/h` norm cannot
be bounded uniformly in `p` after sending `h` to zero.

## Candidate C: verified with its fitting hypotheses

**Addition 414–594.** For arbitrary bounded initialized actions on the given
spaces, (C.1) is a polynomial raw-Hilbert field. Picard contraction gives
local existence; loss dissipation and the strong Cauchy endpoint estimate
give global existence and reached-state restart. With zero readout and
three binary labels the initial loss is `3/2`, matching (C.2).

Checked `Q_l(0)=G+l 11^T` for canonical fresh Gaussian forward actions,
all four kernel terms (C.4), the augmented-Gram lower bound (C.5), and every
offset defect in (C.6). Compressing off the constant removes those defects;
training offset columns instead would change the model. Three distinct
unit inputs have independent augmented vectors, and the stationarity case
split yields only zero, exact-fit, or mean-label constant predictors.
The mixed-label stationary loss is `4/3`; initial decrease alone need not
cross that level.

Under the separately stated positive raw-Gram margin and entry below
`4/3-epsilon0`, (C.7) is the correct residual-length energy identity.
The nonconstant prediction norm is at least
`nu=sqrt(8/3)-sqrt(8/3-2 epsilon0)`. Hence
`||q1||^2 >=nu^2/[12(1+u)]`, and the first kernel block gives
`K >=lambda nu^2 I/[12(1+u)]`. Integrating the nonnegative residual
amplitude proves (C.8), bounded total clock, a strong endpoint, and an
eventual uniform kernel lower bound giving exponential physical fitting.
Pairwise separation supplies neither the raw-Gram margin nor the required
loss entry, and the text does not assert otherwise.

## Candidate D: verified as a conditional same-array lemma

**Addition 597–792.** The deterministic coefficient arrays and their actual
second-moment bounds are hypotheses. Gaussian groups may be correlated.
Both `AB` and `BA` are strictly lower triangular. The running-maximum
majorant proves row bounds `E=exp(a^2 alpha b S)` for both resolvents even
when `B` has concentrated old columns; `U` and `BU` retain the needed
`h_j` density. No false density bound on `AB` is used.

Elimination gives (D.7) at these same coefficient arrays and covariance.
Actual second moments bound the Gaussian parts by `V` and `V_Z` without
independence from their nonlinear remainders. Marginal Gaussian moments
and discrete Gronwall give exactly the displayed sufficient constants
`M` in (D.4) and the bound in (D.5), independently of the minimum step,
node count and cap. The constants need not be small or uniform in horizon.

Also checked the two-coordinate eigenvalue argument, Gaussian projection
at singular covariance, `0<=R<=9I`, initialized fast/slow block estimates,
the moving-coupling derivative in (D.11), and the orthogonal readout
projection (D.12). None proves trained response bounds, a trained Schur
floor, or an autonomous scalar closure. Those remain explicit premises
or separate obligations.

## Candidate E: verified at actual local positive times

**Addition 795–1254.** The new activation has all three numerical bounds
used in II.B and bounded higher derivatives. Thus the same causal source
induction and II.C.1–2 comparison construct its actual local uncut feature
flow for both label modes. No arctangent coordinate transform or same-label
global fitting estimate is needed. Readout variance, summed loss, first-row
metric (including `rho=-1`), true adjoints, and the factor `1/2` in the
feature equations agree with their dependencies.

The exchange/sign argument gives deterministic population predictions
`f_a=y_a g`; it is not used as a finite samplewise identity. Since the
initial top feature Gram is positive definite even at `rho=-1`, the
readout derivative is nonzero for either label pair. Strong continuity
therefore permits one `S0>0` with nonzero top backward variance, positive
first feature Gram, and `|g|<1/2` for all `0<S<=S0`.

The lower-tail argument is complete:

1. Cap-independent primal bounds and the bounded readout give top backward
   increments bounded by `D|t-u|` in `L2`. The actual source covariance
   passes this bound to the finite Gaussian reverse array. Dyadic chaining
   proves its path-maximum second-moment bound using only Gaussian marginal
   tails; orthogonal regression residuals inherit it.
2. Regression on the terminal reverse source divides only by its positive
   scalar variance. Independence of the Gaussian residual gives an event
   of probability at least `c exp(-C(R+1)^2)` with the whole reverse source
   bounded by `C(R+1)` and terminal signed query at least `R+1`.
3. The forward source group is independent of that event. Its scalar
   regression has variance bounded below by `c_-^2` and terminal residual
   exactly zero. For every remaining forward residual realization, the
   terminal preactivation differs from the varied scalar by at most
   `C(R+1)`. Its Lipschitz constant is at most `C exp(C(R+1))`. The
   intermediate value theorem and a Gaussian density lower bound therefore
   place it in a fixed interior subinterval of `I` with the required
   conditional probability. No residual-path bound or measurable choice
   of a root is assumed.
4. A closed interior interval and query threshold `R+1` permit first mesh
   removal at fixed cap, then cap removal, by the closed-set probability
   inequality. Uniform constants preserve the lower bound for the actual
   reached law. Singular full source covariances cause no inverse problem.

For the curvature conclusion, the normalized dual first-layer feature
`B_a` has norm one and isolates one sample. Each direction `v tensor B_a`
is a raw unit HS direction. Choosing `v` as a normalized event indicator
is permitted: each choice is bounded, though their bounds are not uniform.
Its square lies in `L2`, so the middle second variation and adjunction
are valid. The final scalar pairing has a second derivative with only an
`L2` first variation: bounded readout/curvature and strong multiplier
continuity justify the paired difference quotient. No unsupported `L4`
operator estimate is used, and the Taylor cross remainder retains its
necessary factor `|t|`.

The middle multiplier has both unbounded essential signs by (E.1), while
the top curvature term (23) and squared first directional derivatives
are uniformly bounded on these unit directions. Substituting the residual
identity only at the base state gives exactly
`-D^2 L=4(1-g)D^2 g-2 sum_a(D f_a)^2`. Since `1-g>1/2`, the loss has
both unbounded second-directional-derivative signs, contradicting any
finite local Lipschitz constant for its raw gradient.

Finally `ds/dt=4(1-g)` gives deterministic positive physical times with
`S/6<=t(S)<=S/2`. The result asserts neither a finite-width Hessian limit
at fixed positive time nor global opposite-label continuation. Failure of
ambient local Lipschitzness is consistent with the separately constructed
strong local flow and its reached-state uniqueness.

**Required corrections: none.**

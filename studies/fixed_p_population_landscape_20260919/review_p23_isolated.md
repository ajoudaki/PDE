# Isolated internal review: canonical orders two and three

**Verdict: PASS.** The frozen candidate proves that every local minimum has
zero loss for every finite collection of distinct-modulo-sign circle inputs
with positive weights and finite real labels. It also proves attainment and
the exact weighted architectural floor for repeated or antipodal inputs. The
proof covers all current matrix ranks in the stated physical
`L2 × L2 × Frobenius` topology. I found no missing scientific premise or
necessary proof step. This is an internal research verdict, not promotion.

Review date: 2026-09-19. The candidate was read and checked in full, including
all three current-image cases, the interpolation construction and the final
scope limitations. This isolated review used only the neutral assignment,
the required rigorous-math and conjecture-audit skills, the candidate,
`docs/NOTATION.md`, and the three complete assigned source excerpts. No study
README, other study artifact, other review, history, code, or numerical result
was consulted. No experiment or external specialized theorem is needed.

## Frozen inputs

SHA-256 hashes of the complete files:

| Input | SHA-256 |
|---|---|
| `p2_p3_unrestricted_theorem.md` | `1092fbbbebe969eee9286c4ede25a0fb694fe57f4801f9da456270d8c1d6a060` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/global_nonlinear.md` | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |

Only the following scientific sections of `docs/global_nonlinear.md` were
read. Excerpt hashes include the exact bytes of the indicated inclusive line
ranges, preserving line endings:

| Assigned source | Lines | SHA-256 |
|---|---|---|
| C.4.7.10.B | 13161–13430 | `b77fb96abfbf592faa64e401d4456f52c087723737df667abe834f6eea217380` |
| C.4.7.10.C.1 | 13431–13786 | `20c0590f399064f42ee8aa2ec51b72779e4dc889802caab7be6361d1446063ec` |
| C.4.7.10.D.3 | 15146–15528 | `3815d81705fac51fcd5b5489b6f6f961021cba525acf88e74bdc82fe818ae386` |

The candidate hash was checked before reading and again after the proof audit;
it matched the assignment both times. Line references below refer to this
frozen candidate.

## Canonical-model and dependency audit

Lines 14–114 use the actual retained dictionary. Part B explicitly says that
at orders 1, 2 and 3 the initialized-word prefix supplies no extra bounded
word. At orders 2 and 3, codes 0 and 1 are already retained constants and
codes 2 and 3 are the unbounded Gaussian seeds. Thus the complete lower and
upper lists are precisely the total-degree Chebyshev products, of respective
dimensions `(15,6)` and `(35,10)`. This is not a deletion of tail features or
an empirical-rank reduction.

Part B supplies independent upper Gaussians of variance `v>0` and the lower
law `p=zeta+alpha*tanh(g)` with `zeta` independent of `g` and variance
`tau>0`. The joint lower Gaussian conditional density is everywhere positive;
the coordinatewise tanh transformation therefore gives full positive density
on the open four-cube. The upper core has positive density on the open
two-cube. A continuous polynomial that vanishes almost surely consequently
vanishes on the open cube and then identically. Distinct Chebyshev leading
monomials establish a positive definite raw Gram. Invertible Cholesky
normalization preserves this property and the polynomial spans.

The ridge, both Cholesky factors, the right inverse transpose in `D`, and the
actual transpose of the current `M` agree with (H3.N1)–(H3.N2) and
(H40.C5)–(H40.C6). The physical row/readout `L2` metrics and coefficient
Frobenius metric agree with C.1 and D.3. The fixed lower carrier contains
`g`, so its continuous `g_1` marginal provides the required nonatomicity.
The upper coordinate polynomial needed later is in the full upper span.

The ambient loss for arbitrary finite input laws is explicitly defined in
the candidate and is the same algebraic contraction. Its proof does not use
the narrower supported data classes, horizon restrictions, convergence
theorems, or trajectory bounds elsewhere in B, C.1 or D.3. The initializer
`(g,0,D)` is retained but its trajectory is not invoked. Thus no unsupported
extension of a source's gradient-flow theorem is a dependency.

## Proof audit

### Physical lower-field perturbations and the samplewise condition

Lines 118–127 correctly prove ridge independence. The excluded hyperplanes
are proper because each input is nonzero and no two are equal or antipodal.
The resulting projections are nonzero with distinct squares. The tanh
recurrence makes every odd Taylor coefficient nonzero; the coefficient
equations are an ordinary Vandermonde system after factoring the nonzero
projections.

Lines 129–165 use a valid finite-dimensional Taylor expansion. At fixed
`c,M`, bounded marks and bounded tanh derivatives dominate derivatives of
the prediction by a constant times `|c|`; `c in L2` implies `c in L1` on
the probability carrier. This gives the asserted `C2` loss in the finite
moment vector and a uniform quadratic remainder near the current vector.
The derivatives in (4) have the correct factor two, orientation and sample
weights.

If a better pointwise row value exists on positive measure, continuity in
the row value and countability of rational comparison vectors, margins and
row bounds supply one measurable set with uniform strict improvement.
The subprobability measure `P(B intersect {g_1 in ·})` has no atoms because
it is dominated by the continuous `g_1` marginal; its continuous cumulative
distribution supplies subsets of arbitrarily small positive measure.
Replacing `w` on such a subset is measurable and remains in `L2`. Its
squared displacement is `O(epsilon)`, while each moment displacement is
`O(epsilon)`, making the loss remainder `O(epsilon^2)`. Hence the first-order
decrease contradicts physical local minimality.

Lines 167–179 are also valid. Pointwise minimization gives `F(w)<=0`;
stationarity in the actual matrix gives its expectation zero. Integrability
and the sign force `F(w)=0` almost surely. Oddness then forces the whole
pointwise function to vanish. Ridge independence and positive definiteness
of the lower mark Gram give (6), with positive sample weights permitting
samplewise cancellation. No moment-interiority, free sample moments, or
surjectivity of a lower derivative has been assumed.

### Current image and the polynomial pole lemma

Lines 184–216 use only `V_M`, the current matrix image, and each current
preactivation belongs to that space. If `k` is orthogonal to all current
upper features, `c+t*k` leaves every prediction unchanged. For sufficiently
small nonzero `t`, that state lies strictly inside the original minimizing
ball and is a local minimum on a smaller ball. Applying (6) there and at the
original state is legitimate. Since all elements of `V_M` are bounded,
orthogonal decomposition in `L2` gives exactly inclusion (9) for every
nonzero residual. There is no additional matrix direction or rank assumption.

Lines 220–278 establish the polynomial lemma, including its most delicate
point. For nonconstant `P_i`, the choice `h=P_i` belongs to the available
space even if that space contains no constant. Positive density promotes
the asserted `L2` equality to an equality on the cube. A real line through
an interior point with nonzero directional derivative makes its restriction
`Q_i` nonconstant. The infinitely many distinct targets
`sqrt(-1)*pi*(n+1/2)` have polynomial preimages; these preimages cannot all
lie in the finite union of the critical points of the finitely many
nonconstant restricted polynomials.

At a chosen noncritical preimage, `Q_i*sech^2(Q_i)` has a genuine double
pole: the numerator value is nonzero and the denominator zero is simple
before squaring. Each nonconstant `tanh(Q_j)` has at most a simple pole
there, and a constant restriction is real and has no pole. Clearing the
denominators produces an entire identity from a real segment; the
holomorphic identity theorem applies because that segment has an
accumulation point in the complex plane. The resulting meromorphic identity
contradicts the pole orders. This reasoning remains valid for repeated,
opposite, dependent or constant members of the finite list.

For constant `P_i`, a nonconstant `h` in the image restricts to an unbounded
real polynomial on a suitable real line. Its nonzero multiplier
`sech^2(P_i)` cannot equal a finite sum of bounded real tanh terms on that
line. Real analyticity extends the segment identity along the entire real
line because there are no real poles. This also covers `P_i=0`. In
particular, a nonconstant `V_M` with all current sample preactivations
constant or zero is not omitted.

### Constant and zero current images

Lines 282–354 exhaust the complementary cases. If `b_2^T M=v^T`, then
`M^T d_i=v*(E_2 c)*phi'(v·a_i)`. If `v` is nonzero and a residual is
nonzero, (6) and strict positivity of the finite tanh derivative give
`E_2 c=0`. If `v=0`, the upper features vanish regardless of `c`. Thus in
either case every lower-field change preserves zero predictions and the
fixed residual vector `-y`.

Assuming `q=E_2[b_2 c]` is nonzero, matrix stationarity at all nearby
equal-value fields gives the vector identity (13); cancellation is valid
because the matrix derivative is `2*q*S^T`. Bounded truncations approximate
any `L2` row field, so one can first choose a bounded row field strictly
inside the minimizing ball. Along its affine interpolation to any finite
constant row, lower tanh integrands have locally uniform complex
neighborhoods free of poles. Boundedness permits Cauchy/Fubini integration,
and the outer gates have local complex neighborhoods free of poles at every
real interpolation parameter. Hence (13) is real analytic on the connected
real line. Its identity near zero extends to parameter one; this does not
claim local minimality outside the original ball.

The lower mean `a_0` is nonzero because a linear combination of lower marks
is the constant one. Cancelling it yields (14). For every finite real
`kappa`, `h_kappa` is odd, bounded and real analytic, with derivative one at
zero. It therefore has infinitely many nonzero odd Taylor coefficients:
otherwise analytic continuation would identify it with a bounded
nonconstant polynomial. Selecting any required number of those coefficients
gives a generalized Vandermonde system at distinct positive squared
projections. The sparse-polynomial positive-root bound follows by dividing
out the lowest monomial and applying Rolle's theorem inductively; it proves
invertibility without assuming consecutive nonzero coefficients. Positive
weights then force every residual to vanish, contradicting positive loss.
Thus `E_2[b_2 c]=0` is necessary in both degenerate image cases.

For the zero image, an arbitrarily small constant readout perturbation
preserves predictions but changes this necessary mean vector by
`epsilon*E_2 b_2`, which is nonzero because the constant lies in the upper
span. For a nonzero constant image, a small centered nonconstant upper mark
perturbation preserves `E_2 c=0` and all predictions. Its change to the mean
vector has strictly positive pairing with its own coefficient vector,
equal to the variance of that nonconstant mark. Positive core density makes
that variance strictly positive. Both perturbations are bounded and thus
admissible in `L2`. These contradictions cover the zero image and every
nonzero constant image.

### Attainment, duplicates and scope

Lines 358–371 give an actual finite-norm interpolant. The selected constant
row is in `L2`; `a_0` is nonzero; the coordinate `X_{2,1}` is available in
the upper span; and the proposed finite matrix yields exactly
`H_i=tanh(t_i X_{2,1})`. Strict monotonicity of tanh preserves the nonzero,
distinct absolute projections. Positive density and the same Taylor
Vandermonde argument make the upper feature Gram positive definite for
every finite sample count. The displayed finite linear combination is a
bounded readout and interpolates all labels exactly.

Lines 373–390 correctly exploit the architectural oddness, which holds at
every state without any population or training symmetry assumption. The
weighted within-group square decomposition gives exactly (15). Group
weights remain positive and sum to one, and group labels are finite.
Subtracting the constant floor leaves the loss covered by the theorem on
the same parameter space and with the same topology. Interpolation of group
means proves attainment; positivity of all original weights gives the
stated necessary and sufficient condition for a zero floor.

The order-one extension in lines 394–410 follows from the same source
properties. The candidate correctly refrains from extending the proof to
orders whose complete upper tail may cease to be polynomial, to finite
particles, to a stronger local topology, or to convergence, escape rates,
basin sizes or infinite sample count. No such stronger conclusion follows
from this review.

## Required corrections

None. There are no fatal, major or conditional objections within the stated
finite-sample ambient landscape claim. The decisive bridges are supplied:
physical small-set variations give the samplewise condition, actual
readout variations give the current-image inclusion, the polynomial lemma
contradicts it in every nonconstant-image case, and the separate argument
removes the constant and zero images.

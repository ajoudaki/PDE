# Population derivative spans: analyticity, Gaussian tails, and the limit order

Scoped independent analytic route, 2026-09-21. This note does **not** prove or
disprove convergence of the study's actual derivative dictionary. It proves a
specific obstruction to deriving that convergence from pointwise analyticity,
Gaussian source moments, or fixed-width analyticity alone. It also identifies
an exact localization hypothesis under which an analytic argument would work.

The actual target remains the single-sample canonical two-hidden-layer tanh
population GF with zero readout, the symbolic-label derivative factors from
the two fixed normalized axis probes, whole-middle initialization
`Q2,p W0 Q1,p`, and positive ridge `eta_p=1/[1024(p+1)^2]`. The current
factor-only lists retain neither every initialized action argument/result nor
every bounded function of their fields. No background-preserving or
sample-matched replacement is used below.

Scientific repository inputs were confined to the supervisor's eight assigned
study notes and the relevant model, source, and density passages of established
`docs/global_nonlinear.md` C.4.7.8–10. The two required mathematical skills and
their applicable references were read. A general Denjoy–Carleman web query was
made before noticing that the input restriction also excluded that retrieval;
none of its results is used in the arguments below. No other study, numerical
experiment, GPU/training run, or Git operation was used.

## 1. What vanishing ridge proves without any density assumption

Let `H` be a real Hilbert space. Let `R_p:R^{k_p}->H` list finitely many raw
features, preserving every earlier feature and its raw scale. Write

\[
G_p=R_p^*R_p,\qquad
Q_p=R_p(G_p+\eta_p I)^{-1}R_p^*,\qquad
V=\overline{\bigcup_p\operatorname{ran}R_p},
\]

where `eta_p>0` and `eta_p->0`. Then

\[
Q_p\longrightarrow P_V\quad\text{strongly on }H.                 \tag{1}
\]

Here `P_V` is the orthogonal projection onto the actual closed union, which
need not be the whole observable space.

**Proof.** Finite-dimensional diagonalization gives `0<=Q_p<=I`. If
`v=R_m a`, zero-pad `a` in later lists. For every `p>=m`,

\[
(I-Q_p)v=\eta_pR_p(G_p+\eta_p I)^{-1}a,
\qquad
\|(I-Q_p)v\|\le\frac{\sqrt{\eta_p}}2\|a\|,
\]

because `eta sqrt(lambda)/(lambda+eta)<=sqrt(eta)/2` for `lambda>=0`.
Approximation by the union and `||I-Q_p||<=1` prove convergence to the
identity on `V`. On `V^perp`, `R_p^*v=0`, so `Q_pv=0` for every `p`.
These two assertions give (1). Uniform boundedness also makes convergence
uniform on each compact subset, by a finite epsilon-net argument.

For the two populations this implies

\[
Q_{2,p}W_0Q_{1,p}\longrightarrow P_{V_2}W_0P_{V_1}
\quad\text{strongly},                                      \tag{2}
\]

with the analogous assertion for adjoints. To prove (2), subtract the limit,
split at `Q2,p W0 P_V1`, and use the boundedness of `W0` and the filters.
Thus ill-conditioned finite Grams do not by themselves obstruct the strong
limit of the exact-real ridge construction. Identification of the limiting
compressed action with the required action of `W0` is a different assertion.
It requires the relevant inputs and outputs to lie in the two spaces, or
equivalent action approximation statements. The complete word hierarchy has
that density and reduction argument; the derivative-factor hierarchy has not
inherited it merely by using the same ridge formula.

## 2. Zero Taylor radius can coexist with complete derivative approximation

Let `G~N(0,1)` and set `F(s)=tanh(sG)` as a curve in `L2(G)`. This curve is
`C^infinity`: the scalar derivatives of tanh are bounded, and

\[
F^{(n)}(s)=G^n\tanh^{(n)}(sG)
\]

exists in `L2` by dominated difference quotients, since all Gaussian moments
are finite. Its nonzero initial derivatives are nonzero multiples of
`G,G^3,G^5,...`.

These derivatives span densely the odd subspace of `L2(G)`, so every `F(s)`
belongs to their closed span. Here is a self-contained determinacy argument.
If an odd `q in L2(G)` is orthogonal to every odd power, parity makes it
orthogonal to every even power as well. The entire function

\[
L(z)=E[q(G)e^{zG}],\qquad z\in\mathbb C,
\]

is well defined: Cauchy–Schwarz bounds its absolute integrand uniformly on
compact `z` sets by Gaussian exponential moments. The same bound permits
termwise differentiation. All derivatives of `L` at zero vanish, so its
entire Taylor expansion is zero. Thus the finite signed measure
`q(g) exp(-g^2/2)dg/sqrt(2pi)` has zero Fourier transform. To recall the
uniqueness step, convolution with a centered Gaussian has identically zero
density by its explicit Fourier integral and Fubini. Letting that Gaussian
variance tend to zero shows the signed measure integrates every bounded
continuous test to zero, hence is zero. Consequently `q=0` almost surely.

Nevertheless the `L2` Taylor series of `F` has radius zero. If
`tanh z=sum a_n z^n`, its nearest poles are at `+/-i pi/2`, so
`limsup |a_n|^(1/n)=2/pi`. Meanwhile

\[
\|G^n\|_2^{1/n}=((2n-1)!!)^{1/(2n)}\longrightarrow\infty.
\]

For example the last `floor(n/2)` factors of `(2n-1)!!` are at least `n`,
which already proves divergence of the displayed quantity. Along a
subsequence on which `|a_n|^(1/n)` is bounded below, the norm-root of the
`L2` coefficient `a_nG^n` therefore tends to infinity. The Banach-valued
power series has zero convergence radius.

This example separates the two questions: summing the initialized Taylor
series is stronger than approximating the curve by arbitrary linear
combinations of its initialized derivatives. A failure of the former is
not a failure of the latter.

## 3. An explicit Gaussian tanh curve whose initialized derivatives are incomplete

The preceding positive result does not extend to arbitrary polynomial
Gaussian source directions. With the same standard Gaussian `G`, define

\[
F(s)=\tanh(sG^3),\qquad
q(G)=\operatorname{sgn}(G)
 \sin\!\left(\frac{\sqrt3}{2}G^2-\frac{2\pi}{3}\right).
                                                               \tag{3}
\]

The value assigned to `sgn(0)` is immaterial. The test `q` is bounded,
nonzero, and odd. Again `F` is a bounded `C^infinity` curve in `L2(G)`,
because its derivative of order `n` is bounded in absolute value by a finite
constant times `|G|^{3n}`. Every initial derivative is a scalar multiple of
`G^{3n}`. Yet

\[
E[q(G)G^{3n}]=0\quad(n=0,1,2,\ldots),\qquad
\lim_{s\to\infty}E[q(G)F(s)]=-\frac1{\sqrt2}.                \tag{4}
\]

**Proof of the moment identity.** Even `n` are handled by parity. For
`n=2k+1`, the expectation is a positive real constant times the imaginary
part of

\[
e^{-2\pi i/3}\int_0^\infty
g^{6k+3}\exp\!\left[-\frac{1-i\sqrt3}{2}g^2\right]dg.
\]

Put `c=(1-i sqrt(3))/2=exp(-i pi/3)`, whose real part is positive. With
`u=g^2`, repeated integration by parts gives

\[
\int_0^\infty g^{6k+3}e^{-cg^2}dg
=\frac{(3k+1)!}{2c^{3k+2}}.
\]

Boundary terms vanish because `Re c>0`. After multiplication by
`exp(-2pi i/3)`, this number has argument `k pi`, so its imaginary part is
zero. This proves the first half of (4).

For the second half, bounded convergence gives `F(s)->sgn(G)`. The elementary
Gaussian integral, with the square root chosen continuously from positive
real arguments, gives

\[
E e^{i\sqrt3G^2/2}=(1-i\sqrt3)^{-1/2}
=2^{-1/2}e^{i\pi/6}.
\]

Its imaginary part after multiplication by `exp(-2pi i/3)` is
`-1/sqrt(2)`, proving (4).

Let `V` be the closed span of all initial derivatives of this `F`. Since
`q in V^perp`, for every `s>=0`,

\[
\operatorname{dist}(F(s),V)
\ge \frac{|E[qF(s)]|}{\|q\|_2}.                            \tag{5}
\]

In particular the distance is positive for some finite `s`; for all
sufficiently large `s` it is at least `1/(2sqrt(2))`, since `||q||_2<=1`.
Every finite jet dictionary and every ridge filter on it retains the same
obstruction: `Q_pq=0`, hence
`||F(s)-Q_pF(s)||_2>=|E[qF(s)]|/||q||_2` at every order.

The scalar function `s -> E[qF(s)]` has every derivative zero at the
origin but is nonzero arbitrarily close to it on the positive side. To
justify the last claim, it is analytic around each `s0>0`. In the complex
disk `|z-s0|<s0/4`, one has `|Im z|<=|Re z|/3`. Consequently, for every
real `r`, `tanh(zr)` is holomorphic and uniformly bounded: if
`|Re(zr)|<=pi/4`, its imaginary part lies in the pole-free strip
`|Im(zr)|<=pi/12`; otherwise the identity

\[
|\tanh(x+iy)|^2
=\frac{\cosh(2x)-\cos(2y)}{\cosh(2x)+\cos(2y)}
\]

bounds it by `coth(pi/4)^2`. Dominated integration therefore gives a
holomorphic scalar expectation on that disk. If it vanished on any
initial positive interval, analytic continuation along overlapping such
disks would force it to vanish for every `s>0`, contradicting (4).

One can also use `F(s)=tanh(s^2G^3)`. It has zero initial velocity, the
same closed jet span, and the same obstruction. Thus vanishing initial
hidden velocity does not repair this generic implication.

This is a **proof-route counterexample**, not a canonical-GF counterexample.
The direction `G^3` in (3) is explicitly chosen; the study's initialized
reverse/forward dependence and its symbolic-label coefficient families
have not been identified with (3). The result rules out the unrestricted
principle “pointwise analytic dependence on Gaussian sources plus all
`L2` derivatives implies trajectory containment in the initial derivative
span.” Higher polynomial Gaussian fields cannot invoke Gaussian moment
determinacy merely because their underlying roots are Gaussian.

## 4. Fixed-width derivative completeness does not transfer automatically

The very same example exhibits a noncommuting width/order limit. Sample
independent standard Gaussians `G_1,...,G_n` and equip `R^n` with its
normalized Euclidean norm. For

\[
F_n(s)_i=\tanh(sG_i^3),
\]

the first `n` nonzero initialized derivative columns are nonzero multiples
of `G_i^{3(2k+1)}`, `0<=k<n`. Their matrix factors as

\[
\operatorname{diag}(G_1^3,\ldots,G_n^3)
 \big[(G_i^6)^k\big]_{i=1,\ldots,n;\ k=0,\ldots,n-1}.
\]

It is invertible almost surely: no `G_i` is zero and no two `G_i^6` agree,
and the second factor is a Vandermonde matrix. The odd tanh Taylor
coefficients are nonzero. This can be checked without a closed formula:
writing `tanh z=sum_{k>=0}(-1)^k a_k z^{2k+1}`, the equation
`(tanh z)'=1-tanh(z)^2` yields `a_0=1` and

\[
(2k+1)a_k=\sum_{i+j=k-1}a_i a_j>0\quad(k\ge1).
\]

Therefore the finite-width jet span equals all of `R^n` at a finite order.
In particular, its approximation error tends to zero as order tends to
infinity at each fixed `n`.

For each fixed order, however, the empirical Gram and target pairing
converge almost surely to their population values. The strong law applies
to each entry because it is a finite Gaussian moment, or a bounded tanh
factor times a Gaussian polynomial, and hence integrable. The population
Gram of these distinct monomials is positive definite: a nonzero polynomial
cannot vanish on a full-support Gaussian law. Continuity of inversion then
shows convergence of the fixed-order least-squares distance to its
population counterpart.

If `d_{p,n}(s)` and `d_p(s)` denote those distances and `s` is chosen so that
the right side of (5) is positive, then

\[
\lim_{n\to\infty}\lim_{p\to\infty}d_{p,n}(s)=0,
\qquad
\lim_{p\to\infty}\lim_{n\to\infty}d_{p,n}(s)
=\operatorname{dist}(F(s),V)>0.                            \tag{6}
\]

Nested ridge filters with the study's vanishing ridge obey the same two
iterated-limit conclusion for their approximation errors. At finite width
their closed union is all of `R^n`; at population it is `V`; apply (1).
Fixed-order empirical convergence of their finite ridge formulas follows
from the same Gram convergence, with a strictly positive ridge.

Thus finite-dimensional analyticity and even eventual exact finite-width
jet representation cannot establish the needed population statement
without a width-uniform estimate or a separate population density theorem.

## 5. A precise localization criterion that repairs an analytic proof

Here is a sufficient hypothesis stronger than pointwise analyticity. Let
`I` be a connected real interval containing zero, let
`F:I->L2(Omega)` be `C^infinity`, and let `V` be a closed subspace
containing every `F^(n)(0)`. Suppose measurable sets `E_R` increase to full
probability and satisfy both:

1. Multiplication by `1_E_R` maps `V` into `V`.
2. The localized curve `1_E_R F(s)` is real analytic as an `L2`-valued
   curve on `I`.

Then `F(s) in V` for every `s in I`.

**Proof.** For `q in V^perp`, the bounded self-adjoint multiplier
`M_R=1_E_R` gives `M_Rq in V^perp`, because
`<M_Rq,v>=<q,M_Rv>=0` for `v in V`. The scalar analytic function
`<q,M_RF(s)>` has every initial derivative zero. Its local power series is
therefore zero, and overlapping analytic neighborhoods propagate zero
through the connected interval. Thus `M_RF(s)` is orthogonal to every
element of `V^perp`, so belongs to `V`. Finally
`M_RF(s)->F(s)` in `L2` by dominated convergence; closedness finishes the
proof.

Source truncation often supplies a uniform complex-time neighborhood for
a *fixed finite source model*. That establishes only item 2. Item 1 is
essential: arbitrary truncation of an orthogonal test changes its moment
constraints. In example (3), truncating `q` to `|G|<=R` does not preserve
orthogonality to the powers `G^{3n}`. The derivative span there cannot be
invariant under all such cutoffs, since items 1–2 would contradict (5).

Neither cutoff invariance nor an equivalent module/algebra property is
part of the new factor-only specification. Adding cutoff multiples or all
bounded functions of every source would be a materially enriched hierarchy;
it cannot be silently inserted as a proof step. Even after such invariance
were shown, localized analyticity for the actual infinite population flow
would still need proof, since truncating initial roots does not automatically
bound every subsequently generated query.

## 6. Consequences for the actual research target

The route yields four definite conclusions:

- The prescribed ridge converges strongly to the projection onto the actual
  derivative-span closure. Its polynomially decreasing value is adequate for
  that assertion; a smallest-Gram-eigenvalue rate is unnecessary.
- Divergence of an `L2` Taylor series alone does not defeat derivative-span
  approximation. The linear-Gaussian tanh example proves this distinction.
- Gaussian roots, finite moments of all orders, pointwise analyticity, and
  fixed-width derivative completeness do not suffice. Equations (3)–(6)
  provide an explicit bounded-test obstruction, including the failed exchange
  of limits.
- A localization proof becomes valid under the explicit multiplier-invariance
  and localized-analyticity hypotheses above. Neither is proved for the actual
  factor-only hierarchy.

Three model-specific implications remain open. First, the formal all-order
continuation must be identified with actual population time derivatives;
the p5/p7 notes themselves distinguish formal coefficient algebra from that
regularity assertion. Second, the actual closed factor spaces must approximate
the initialized forward/reverse actions and moving factors required by the
single-sample flow. Third, fixed-axis derivative information must reach the
initial and moving test-circle query family; matching just the axis trajectory
would not establish that claim.

`SINGLE_SAMPLE_GLOBAL_BOUND.md` already supplies an all-time stability
certificate once its explicitly listed source defects vanish and initial
training feature energies have a common positive lower bound. This analytic
route does not supply that missing order-dependent source estimate. The
highest-leverage continuation of this route is to prove an actual structural
closure property of the derivative-factor spans—strong enough to justify
localization or identify their relevant Gaussian function spaces—rather than
to extend the finite-width analytic-radius estimate alone.

Status: **partial route completed; actual population hierarchy convergence
remains open.** The cubic-Gaussian example is not a falsifier of the specific
GF construction, and the positive linear-Gaussian example is not its proof.

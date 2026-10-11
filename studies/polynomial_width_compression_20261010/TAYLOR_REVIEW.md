# Independent audit of the capped Taylor route

2026-10-10. Frozen candidate:
`TAYLOR_ROUTE.md`, SHA-256
`d9153aa789ec23d23683b79f9e5e5a6215a4bb884757079ff1b516235504030e`.

## Verdict

**Conditional result only; the full polynomial source-probability theorem is
not yet established by this frozen version.** The blocking issue is the
terminal-grid construction on a common stopping prefix in Section 5,
lines 748–774. The argument does not identify a root-independent family of
Gaussian tests that covers every full-network-dependent prefix. The claimed
failure estimate (37), and hence the unconditional source theorem, still need
that premise.

This is a proof-construction gap, not a counterexample to the proposed
theorem. The cap, panel count, and fixed-exponent common-cavity calculation
survive at their stated deterministic or conditional scope. The passive
response identities and the numerical coefficient/width accounting also
survive, conditional on the missing uniform local event. The approximation,
initialization-only provenance, and storage calculation preserve the stated
logarithmic powers on that source event.

## 1. Scope and complete inputs

I read the complete frozen candidate; `paper/compact.tex`,
`paper/compact_foundations.tex`, and `paper/compact_selected.tex`; and the five
assigned previous proof files listed in Section 7 below. I read and applied
`solve-math-rigorously`, `explain-with-canonical-notation`, and its
neural-response-memory reference. I did not read the study README, study
history, previous review files, other current route outputs, or archived
book material. No previous verdict is used as evidence.

The current foundations module contains the normalized retained equation,
fixed-order nonlinear remainders, passive response observable, trace
calculation, source recurrences, and flaring-domain estimates used here.
Consequently this audit did not fetch the older studies referenced by the
previous proof files. Their standalone jet and insertion reports are not
independently certified by this review; the relevant supplied current
formulas were checked directly. The quantitative independent-dense-run lower
event is outside the supplied candidate's claim and remains unproved here,
as the candidate itself states.

Use the candidate's notation throughout: width \(n\), training count \(m\),
passive count \(p\), \(N=m+p\), confidence order \(u\),

\[
\lambda=\gamma/m\in(0,1],\quad Y=\|y\|_2/\sqrt m>0,\quad
S=16Y/\lambda,\quad \ell=\log(en),\quad q_n=\log(e+\ell).
\]

The network, Gaussian initialization, zero initial readout, loss and physical
mobilities agree with the supplied paper. The normalized backward fields
are divided by \(S\); passive indices enter evaluated observables but never
the \(m\)-sample optimizer or residual averages.

## 2. The unresolved stopping/grid interface

For a deletion set \(I\), condition on its retained initialization and denote
the cavity's own stop level by \(s_I\). Its complete coefficient extension

\[
b_I^{\mathrm{ext}}(z)=b_I(P_{s_I}z)
\]

is measurable in that retained initialization. Testing this coefficient on
a fixed bounding-rectangle grid is legitimate. This is precisely the kind
of extension used by the Gaussian rectangle moments in Section 4. There is
no defect in that use.

The insertion comparison additionally uses the actual omitted-neuron
controls, which are analytic only on the current successful full/cavity
prefix. Write \(s_F\) for the full-network stop level and

\[
s=\min(s_F,s_I).
\]

After conditioning on the cavity, \(s_F\), and therefore \(s\), may depend on
the omitted Gaussian roots. For a fixed rectangle grid point \(\zeta\),
the retracted point \(P_s\zeta\) has the same dependence.

The candidate states that retracting the grid onto a domain prefix changes
its distance bound by at most \(9/8\), then uses analytic terminal
derivatives to interpolate from that grid. This proves a geometric distance
bound. It does not prove the Gaussian tests at the resulting grid points.
There are two different possibilities, neither completed in the text:

1. If the Gaussian tests are at \(P_s\zeta\), their endpoint and reference
   coefficient maps can depend on the omitted roots through \(s_F\).
   A fixed-control Gaussian or centered quadratic-form tail cannot be
   applied to such a coefficient without a prior uniform event over the
   possible prefix levels.
2. If the tests are instead at \(P_{s_I}\zeta\), the endpoints are
   cavity-measurable, but some may lie beyond the full prefix. The actual
   analytic controls and their analytic linearized solution need not be
   defined there. The claimed off-grid argument cannot simply interpolate
   through such endpoints using the derivative bound proved only on the
   common prefix.

Nor does testing unretracted fixed rectangle points by itself bridge these
two alternatives. One must define the linear insertion maps and a justified
terminal modulus for the chosen complete extensions of controls and
coefficients, or provide a root-independent covering of all valid prefixes.
Clipping an analytic control generally destroys holomorphy outside its
original domain. The candidate expressly avoids assuming analytic
continuation of arbitrary two-dimensional controls, correctly, but does not
supply a replacement extension argument here.

This interface is not supplied by the inherited map note.
`INSERTION_MAP_MODULI.md`, lines 338–359, proves the complex derivative
bound for analytic controls on the pre-stop rectangle and discusses each
reference's own cavity-measurable clamping. It does not construct tests
uniformly over a full-network-dependent prefix level. The finite grid in
`FULL_FINITE_SOURCE_PROBABILITY.md`, Section 3, likewise does not add such a
level parameter. The current foundations module gives the qualitative
terminal-mesh assertion but does not close this distinction.

The exact remaining premise is a conditional Gaussian event, measurable
before actual adaptive controls are substituted, that simultaneously
controls the required linear coordinates, Euclidean images, centered
quadratic pairings and probe images for every applicable prefix and every
admissible control restriction on that prefix. It must have the stated
quantitative failure bound after the deletion union and include an explicit
endpoint interpolation argument. Its reference coefficients must remain
independent of the paired root throughout the construction. A further
uniform covering construction may be feasible with the ample exponent
slack, but no such repair has been silently added in this review.

Accordingly, (37) is presently conditional on this missing event. The
subsequent nonlinear closure, no-cavity-first-exit conclusion, singleton
trace error, maximum improvements and budget removal cannot establish the
unconditional probability theorem without it. Merely increasing the width
does not resolve a measurability or coverage premise.

## 3. Deterministic cap and panel count

The current source recurrences support the candidate's envelopes

\[
S\le\beta^{-26L}\le S_*,\quad S^2/\eta_*\le1,\quad
U_{\rm fin}\le\beta^{26L},\quad
\mathcal K\le\beta^{14L},\quad \eta_*^{-1}\le\beta^{25L+4}.
\]

In particular the displayed recurrences for \(J_*\) and \(C_g\) fit within
the common \(\beta^{100L}\) envelope. With
\(B=\beta^{300L}\), the cap gives all four radius gates in (7), strictly.
It also controls the sum of the two propagator exponents:

\[
4\mathcal K r_n\le4\mathcal K/B,\qquad
\frac{2C_g}{\sqrt{\mathcal K}}B_nYr_n
\le\frac{C_g}{8B}.
\]

Here \(Y=\lambda S/16\) is necessary for the second inequality. There is
no hidden inverse-label or exponential-in-gap gate. Replacing the strip
width by \(a_0=\min(a,1)\) is legitimate, with \(a_0^{-1}\le\beta\).

For the vertical propagator, the real anchor generator is real symmetric,
so its imaginary-time propagator is unitary. Integrating its difference
from the actual generator gives the second exponent above. The residual
bound yields exactly

\[
\int_0^{h(t)}Ye^{-\nu t}e^{2\mathcal Kv}\,dv=Yr_n,
\]

and the corresponding double integral is at most

\[
Ye^{-\nu t}
\frac{e^{2\mathcal Kh(t)}-1-2\mathcal Kh(t)}{(2\mathcal K)^2}
\le\frac{Yr_n}{2\mathcal K}.
\]

This verifies the propagator estimate without complex Gram positivity.
Ordered disjoint pieces add their perturbation integrals; the negative
corner has the separately charged \(e^{4\mathcal Kr_n}\) cost. The
operator, activity and improved pole estimates have strict margins.

The domains are nested and their retractions are uniformly Lipschitz and
commute with the real anchor. The disk-containment proof is valid also at
the negative boundary and near \(T\). Since the adaptive radius is
nondecreasing with Lipschitz constant \(d_h/[2(1+d_h)]\), each complete
panel supplies the stated lower contribution to \(\int dt/\varrho(t)\).
Splitting at \(2\mathcal Kr_ne^{\nu t}=1\) verifies (11).

The cap costs

\[
\frac1{\lambda r_n}
\le \frac{1024U_{\rm fin}}{a_0}(Y/\lambda)^2\sqrt\ell
 +B\lambda^{-1}\sqrt{q_n}+BB_n\sqrt{q_n}.
\]

The identity \(S^2=256(Y/\lambda)^2\) and
\(q_n^{3/2}\le4\sqrt\ell\) preserve the label-dependent first term.
Thus (14) follows with an activation/depth-only coefficient, for example
the stated \(\beta^{400L}\). No confidence order appears in the radius
or panel count.

## 4. Complete common-cavity references and moments

On independently stopped paths, the normalized complex-minus-real
coefficient bounds (15) retain a factor \(\lambda\): backward
derivatives use \(Y/S=\lambda/16\), and forward derivatives use

\[
YS=\lambda S^2/16.
\]

The commuting own-cavity retractions preserve these complete coefficient
bounds. They are legitimate deterministic inputs after conditioning on the
cavity. The rectangle supremum lemma and its sample-RMS version apply;
sample independence is not required.

Substitution of \(\overline D\) gives (18). The only potentially
unbounded gap logarithm is controlled by

\[
\min(1,be^{-x})\sqrt x\le\sqrt{\log b}+1
\quad(b\ge1, x\ge0),
\]

with \(b=B_n\) and \(x=\log(1/\lambda)\). This verifies (20)–(21)
uniformly in width and gap, with the stated generous powers of \(\beta\).

Each complete \(A_i\) is a function of the common cavity and just its own
omitted root pair. Cauchy–Schwarz between the real and complex parts of

\[
A_i^2=\exp\{2\eta_*C_{\rm abs}
 (1+\text{four real terms}+\text{four correction terms})\}
\]

requests the real bound at \(4\eta_*\). Hölder over the four complex
terms requests only \(16\eta_*C_{\rm abs}<8\). Hence

\[
\mathbb E(A_i^2\mid\text{cavity})<3,
\qquad \mathbb E\prod_{i\in I}A_i^2\le3^{|I|}.
\]

There is no confidence-order Hölder exponent in this calculation. The
incoming first-layer root has its proper covariance and time-independent
initial pairing; it is not incorrectly treated as covariance \(I/n\).
The absent top outgoing root causes no additional term.

For the singleton/common-cavity correction, both complete paths omit the
paired root. Extending them separately and projecting their entire
difference preserves independence and gives radius
\(v_n=4n^{-49/100}\). Agreement with the actual difference, however,
uses the local comparison event discussed in Section 2 of this review.
Conditional on that event, Cauchy–Schwarz and Hölder give exactly the
exponent in (25): at most four primitive errors per root produce

\[
k n^{-1/40}+4k\mu_n+64k^2v_n^2.
\]

The indicators are removed only after a pathwise domination. This part
does not assume independence between projected errors or between samples.

## 5. Passive estimates and numerical probability accounting

The passive response recurrence (30) follows by differentiation of the
forward pass. Its driver is always a training sample. The omitted upper
port and the direct reverse observable \(C_bC_a^\top\bar q_a\) are both
needed and are both included. The probe images at passive inputs are also
included. The product subtraction (31) and feature-pair subtraction (32)
agree with the current foundations module.

In the first term of (31), changed gates multiply a localized reference
directional feature, giving \(d_0\); matrix changes keep \(n^{-1/2}\).
The second term uses the adjoint-probe subtraction and the bounded forward
Jacobian. This justifies (33). In (34), the reference response cap occurs
only in the additive gate remainder. Homogeneous propagation uses the
bounded perturbed slope and mixer. Consequently the cutoff degree does
not grow with depth. Time differentiation introduces one raw
RMS-to-coordinate factor \(\sqrt n\), rather than a factor at each
layer. These checks support the stated passive map and remainder ledger.

The numerical envelope (35) is sufficient: its displayed factors cost
at most \(100L+160L+600L\) powers of \(\beta\), leaving ample room
for finite sums and numerical factors. The retained control count
\(4u(N+1)^2\) covers the forward, training backward, and \(mN\)
response controls. Nothing inserts \(N\) into a residual average.

The normalized equation (29) is exact. Since the initial readout is zero,
\(\bar F_a=\bar u_w^\top h_a^{(L)}\); differentiation introduces no
inverse \(S\). The complete top prediction offset is retained. The current
foundations module supplies the fixed-order force remainder and learned
ports in precisely these normalized variables. Their coefficients, at
most cubic in the provisional cutoff, fit inside \(\mathcal A\).

The fitting theorem applies without \(m\ge d\), as its proof states. Its
width envelope is dominated by (26), and the current label condition
implies its fitting cap. All-deletion initialization follows from the
deterministic feature difference and the fresh-row coordinate tail (28),
with the declared finite panel replacing the training-only maximum union.
The coordinate localization is performed before conditioning on the fresh
row's operator event. Passive initial and evolved size caps have ample
margin and require no passive exponential budget.

The width (26) implies (36) at every larger individual width. Its logarithmic
proof is valid at the smallest allowed parameters and improves thereafter.
Once the map/grid event is constructed correctly, the following numerical
claims hold:

- Linear and quadratic fixed-control tails at threshold
  \(n^{-1/10}/8\) are at most \(4e^{-n^{0.78}}\); the Gaussian input
  dimension and quadratic Hilbert–Schmidt factor are charged.
- The control entropy is below \(n^{0.627}\), the stated rectangular
  terminal mesh has at most \(n^6\) points, and the deletion union fits
  within the claimed logarithmic cost. Centered quadratic interpolation
  correctly retains the trace contribution.
- The enclosing remainder (38) is at most a constant times
  \(n^{-0.07875}\), strictly below \(n^{-1/25}/2\) at (26).
  The joining-strip gate is also paid. These imply the claimed coordinate
  and Euclidean discrepancies once the uniform event is available.
- The projected error entropy gives \(\mu_n\le n^{-48/100}\), while
  \(u\le n^{1/8000}\), so the premise of (25) is paid.

The stop transfer, four scalar contractions, unchanged \(C_{\rm abs}\),
and maximum/response improvements then follow in the specified order. The
collision argument is correct: repeated factors have cost at most
\(e^{1/100}n^{1/100}\), and partitions with \(j\) identifications are
bounded by \(\binom u2^j/j!\). For \(n\ge4u^3\) the collision factor
is at most \(e\). The choice of \(u\) gives budget failure at most
\(\delta/4\). Initialization, local Gaussian, and maximum-event failures
fit within the total \(\delta\) allocation. This is valid numerical
composition conditional on the missing uniform-prefix Gaussian event;
it does not prove that event.

## 6. Approximation, accuracy, and inventory

On the claimed source event, the selected-model coefficient ledger permits
\(C_{\rm sel}=\beta^{60L}\). In particular, with \(X=\beta^L\),
the supplied recurrences give \(F\le X^6\), \(K_1\le X^{18}\),
\(\mathcal B_n/z\le X^{22}(1+\sqrt\ell)\), and a tail coefficient
below \(X^{30}z(1+\lambda^{-1/2})\), where \(z=Y/\lambda\).
The finite-horizon carrier bound needed here is supplied by the source
event; no additional all-time coordinate-carrier theorem is necessary for
the selected tail estimate, which uses all-time RMS bounds and fitting.

The tolerance (39) makes the finite-horizon error at most \(Y/(2n)\).
The separate gate (40) makes the endpoint tail at most \(Y/(2n)\).
It contains no inverse positive-label factor.

The disks cover the real interval strictly, so a positive closed rectangle
inside their open union exists. The supplied origin-jet compiler therefore
applies with no preprocessing complexity claim. Coefficient errors chosen
in Euclidean norm give coordinate errors; geometric summation and the
initialized operator norm eight establish exact paired-image source
approximation at the requested tolerance.

The panel input-span reduction preserves every declared input inner
product, the first-layer Gaussian law, and the coupled panel trajectory.
Its dimension is \(k\le\min(d,N)\). The exact rank is consequently

\[
R=2m+k+1+2(2m+p)J(K+1).
\]

Gate (42) is sufficient for \(K+1\le8\ell\). Its inverse-label factor is
an explicitly charged simplification gate, separate from probability.
Without it the exact \(K\), including its \(\log(1/Y)\) dependence,
must be retained.

Squaring the rank bound retains

\[
R^2\le C N^2\left[
(Y/\lambda)^4\ell^3+
\lambda^{-2}\ell^2\{\log(e+\ell)\}^2\right].
\]

The supplied inventory is unchanged and absorbs its additional terms into

\[
C(m+p)^2\left[(Ym/\gamma)^4\log(en)^3
+(m/\gamma)^2\log(en)^2\log(e+\log(en))^2\right]+C(m+p)d.
\]

Here \(C\) depends only on activation bounds and depth. In particular the
confidence order affects the source width, not the retained rank
coefficient; no new power of \(\log n\) has appeared. Dense arrays, jets,
coefficient tables and panel schedules are discarded after initialization.
Nonprimitive activation evaluation remains separately charged.

The independent-dense-run lower event at the end of the candidate is an
additional premise. Dividing \(Y/n\) by its stated lower bound gives the
stated ratio. This review supplies neither that event's quantitative width
nor an unconditional polynomial relative-error theorem.

## 7. Frozen-input verification

SHA-256 hashes were checked before reading and again after the substantive
audit. Every value was unchanged. The candidate hash matches the neutral
assignment. Only this report was written; no candidate, paper, shared
instruction, Git index, or other study artifact was modified.

| Input | SHA-256, before = after |
| --- | --- |
| `TAYLOR_ROUTE.md` | `d9153aa789ec23d23683b79f9e5e5a6215a4bb884757079ff1b516235504030e` |
| `paper/compact.tex` | `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` |
| `paper/compact_foundations.tex` | `6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0` |
| `paper/compact_selected.tex` | `3add2b694f38a4d7dbce90e51dafd375a7e8dee2e06d26b2d5af451bddb44885` |
| `unseen_query_decoder_20261005/FULL_FINITE_SOURCE_PROBABILITY.md` | `6ecf89142925ef831b7efbf12ad84eacdfef3dc97f3c5b749bc7547311f9695a` |
| `unseen_query_decoder_20261005/FINITE_COMPLEX_MOMENT_GATE.md` | `6922cc2630f335903352fab360d3b56b72ccdd10d248ea8e49abe73759b48f18` |
| `unseen_query_decoder_20261005/INSERTION_MAP_MODULI.md` | `ea71fbc226d4ac02031661a96650256a44260553550ef2b2fd0e10a68b78c93e` |
| `unseen_query_decoder_20261005/QUANTITATIVE_INSERTION_WIDTH.md` | `40fc026d7e0d18b968ae1526a94792290dc25cd56f97972db526dfd3e8aeb31b` |
| `unseen_query_decoder_20261005/EXPLICIT_FITTING_WIDTH.md` | `62d018c6448b0e6af6085827a856667ba58747810c6b284452dea21ce800919d` |

## 8. Addendum: complete prefix repair and the assembled theorem

2026-10-10. I read the complete additional frozen input
`TAYLOR_PREFIX_REPAIR.md`, SHA-256
`7e9e027676f68fa362cf4016f578ee4ff96cc8cfbaa7ba63d6457417ebcb0c48`.
Its hash was verified before reading and after this audit. The original
candidate and all nine original input hashes remain those in Section 7.
No other review, study history, or route output was read.

**Repaired assembly: PASS for the polynomial-width finite-panel source,
absolute-error, and retained-storage claims.** The replacement supplies the
specific event missing from the original frozen version, for the actual
augmented maps used there. Combining it with Sections 3–6 of this review
leaves no further unproved premise in those three claims. The original
standalone candidate remains conditional as recorded above: the passing
object is that candidate with its Section 5 endpoint/control paragraph
replaced by the complete prefix repair. The separate quantitative
independent-dense-run lower event remains outside this verdict.

### 8.1 The repair covers the same insertion maps

The repair takes
\[
\mathcal C=\beta^{1000L}(1+\lambda^{-1})^2,\qquad
\mathcal A=\mathcal C^4(N+d+u+1)^8,\qquad \kappa=1/4000.
\]
Thus its width and coefficient envelope are exactly the candidate's,
not additional parameter assumptions. Its interfaces (4)–(6) are the
norm, control-difference, analytic terminal-derivative and control-speed
bounds checked in Section 5 of this review.

The definition of the contour maps is sufficiently explicit to verify this
correspondence. Repair (15) contains both forward-port derivatives of the
normalized retained vector field: the adaptive-residual rank-one term and
the residual-weighted response derivative. It also contains the reverse
force derivative. Equation (16) solves their linear forced variational
equation along a contour entirely inside the independently stopped cavity.
Its coefficients depend only on that cavity. At frozen controls the
solution is linear in the omitted roots.

The endpoint recursions (19) retain all forward and scaled-backward fields.
Equation (20) includes the feature-pair variation, changed mixer,
propagated response, gate variation and independent omitted response port.
The direct lower reverse map \(C_bC_a^\top\bar q_a\), lower adjoint probes
and their forward images at every declared input are explicitly retained.
Finally (21) constructs the centered quadratic matrices by the algebraic
transpose. These are precisely the coordinate, vector, probe and pairing
maps used by candidate (35), including its passive-response additions.
There is no substitution of a narrower training-only family.

The possibly enlarged control envelope is also paid. The parameter
variation and the algebraic endpoint recursions are affine in the frozen
scalar controls; probe maps supply any constant part. Their control
modulus therefore extends by scaling to the larger net envelope. For
every net history the repair obtains
\[
\|L\|,\|R\|
\le4\mathcal C^2\sqrt u\,n^\kappa\ell^5
\le\mathcal A\ell^{16}n^\kappa
\le n^{1/800}<n^{1/200}.
\]
Consequently the original fixed-control Gaussian tails remain valid over
the full net, even though its common amplitude cap exceeds some original
per-type stopped caps. Net histories need only be one-dimensional
histories; none is falsely assumed holomorphic.

### 8.2 Endpoint measurability and actual-control coverage

Condition on one cavity with own stop \(\sigma_c\). With
\[
H=128\ell/\lambda,\qquad
\xi=\frac{n^{-2}}{1+\mathcal A\ell^8},
\]
the repair uses deterministic level spacing at most \(\xi/(16H)\),
a deterministic rectangular spatial grid of spacing at most \(\xi/8\),
and test endpoints
\[
z_{j,q,c}=P_{\min(s_j,\sigma_c)}q.
\]
Every endpoint and its canonical contour are fixed under this conditioning.
They remain inside the cavity's own stopped domain. The associated
Gaussian coefficients are therefore independent of the omitted roots.
The optional clipped extension is never used as a holomorphic coefficient
outside that domain.

After the finite uniform event has been formed, let \(D_\sigma\) be any
actual common prefix, possibly chosen from the omitted roots. Selecting
the largest deterministic mesh level \(s_j\le\sigma\) makes the tested
endpoint and its entire canonical contour lie inside \(D_\sigma\).
The actual controls are defined on that whole contour. Restriction to its
arclength parametrization, followed by freezing its endpoint value, gives
a one-dimensional Lipschitz history covered by the deterministic net.
This resolves both alternatives identified in Section 2 of this review.

The geometric bounds are valid:
\[
\sup_{z\in\mathscr R}|P_sz-P_tz|\le3H|s-t|,
\qquad \operatorname{Lip}(P_s)\le9/8.
\]
For \(z\in D_\sigma\), the selected endpoint is consequently within
\[
(3/16+9\sqrt2/64)\xi
\]
of \(z\). Retracting their straight joining segment by \(P_\sigma\)
produces an in-domain path of length less than \(\xi/2\), with both
endpoints fixed.

Only for the actual analytic control functions does the repair use
holomorphic endpoint interpolation. For \(\sigma>0\), the domain's
interior is simply connected and contains the origin. The linear
variational equation with those fixed actual functions has holomorphic
coefficients and forcing there; local existence, continuation on compact
paths, and uniqueness give its single-valued solution. Restriction to the
canonical contour agrees with (16). Its algebraic endpoint maps obey the
candidate's derivative bound. Boundary points follow by continuity from
smaller levels; \(\sigma=0\) is already an explicit grid endpoint.
No planar analytic extension of a clipped control is being presumed.

Control interpolation, including centered traces, costs at most
\[
10\mathcal C u^{3/2}n^{\kappa-1/8}\ell^4
\le10n^{-0.12375}<n^{-1/10}/8.
\]
Endpoint interpolation costs at most
\[
10\mathcal C u^{3/2}n^{\kappa+1/2}\ell^8\xi
\le10n^{-3/2+\kappa}<n^{-1/10}/8.
\]
Together with the net threshold \(n^{-1/10}/8\), these give the same
scalar and quadratic bound required in the original local comparison.
The separately reserved Euclidean-image margin gives \(n^{1/100}\).
The trace remains a frozen-map trace evaluated after control selection;
it is not misidentified as the conditional mean of an adaptive form.

### 8.3 The extra discretization fits the existing probability budget

The one-dimensional control entropy is still at most
\(\mathcal A\ell^8n^{5/8}\le n^{0.627}\). The spatial and level
cardinalities are at most \(n^6\) and \(n^3\), respectively, so the
endpoint family grows to at most \(n^9\). The estimate
\[
H/\xi\le256\mathcal A^{9/8}\ell^9n^2
\le256n^{2.001125}
\]
verifies these cardinalities at the unchanged width.

The fixed-test complex Gaussian and centered quadratic tails retain
\(4e^{-n^{0.78}}\); their constants explicitly account for the
\(2un\)-dimensional Gaussian input and the quadratic
Hilbert–Schmidt bound. The norm event
\(\|g\|\le2\sqrt{2u}\) fails with probability at most \(e^{-un}\).
The Euclidean-image tail has its required extra margin. Summing over
controls, endpoints, map/probe tests, and all deletion choices leaves
logarithmic cost below \(n^{0.65}\), giving
\[
4e^{\,n^{0.65}-n^{0.78}}+uLn^u e^{-un}
\le e^{-n^{0.7}}<\delta/16.
\]
All conditional estimates have deterministic uniform upper bounds, so
integrating over each cavity and taking the deletion union is valid.
Neither independence between cavities nor conditioning on full-network
survival is used.

This is the missing event itself, rather than a new conditional premise.
It supplies the local first-exit argument, cavity-stop transfer, singleton
trace and maximum improvements, and common-cavity probability composition
already checked above. The extra level mesh changes no source radius,
Taylor rank or retained coordinate count.

### 8.4 Exact scope of the assembled conclusion

For \(0<\delta<1/4\), the candidate's confidence order \(u\) and source
width (26) now give the claimed source event with probability at least
\(1-\delta\), at each individual width above the stated threshold.
This threshold is polynomial in the displayed physical parameters and
confidence variables, with no inverse positive-label factor.

On that event, the selected construction with tolerance (39) and the
explicit tail gate (40) has complete-trajectory error at most \(Y/n\),
including the fitted endpoint. The exact rank and inventory are (41) and
the subsequent displayed inventory. With the additionally charged
simplification gate (42), they give (43)–(44), with the original
\(\log(en)^3\) and
\(\log(en)^2\log(e+\log(en))^2\) powers and activation/depth-only
coefficients. Initialization-only provenance, paired images, and the
unchanged selected optimizer are preserved.

This addendum certifies that repaired assembly within the assigned scope.
It does not certify a quantitative lower event for independent dense-run
variability, preprocessing efficiency, finite-precision complexity, or
promotion into the maintained paper.

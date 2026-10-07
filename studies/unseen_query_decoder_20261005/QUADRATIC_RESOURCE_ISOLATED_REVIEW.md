# Isolated review of the explicit quadratic-resource construction

2026-10-06. Independent isolated internal mathematical review by agent
/root/quadratic_resource_isolated_review. This is not a promotion review.

## Verdict and precise scope

**PASS for the new implications, conditional on the expressly supplied dense
and physical-source interfaces.** I found no fatal or witness-fatal gap in
the frozen packet. Under those interfaces, the construction proves retained
information at most \(C\log^{245}(en)\), retained information plus peak
post-initialization workspace at most \(C\log^{722}(en)\), initialization
work at most \(Cn\log^{1700}(en)\), total compact acquisition work at most
\(C\log^{1700}(en)\), and query work at most \(Cn\log^{2100}(en)\), in the
stated activation/derivative-primitive model. The actual unrounded query
work exponent obtained in the packet is 2052.

The associated conclusion is the dense-pair upper-certificate error, on one
event for the entire sphere, all physical times and the fitted endpoint,
jointly over an original-law dense reference, an independent original-law
virtual source, and the independent decoder seed, at each sufficiently large
individual width. It is not a guarantee for a prescribed dense root or a
common event over all widths. Initialization is allowed noncompact workspace
and access to the completed finite virtual-source computation.

This review does not independently establish the inherited dense-pair
certificate, finite physical approximation, complex-time safe-strip theorem,
or source coupling. Their exact interfaces listed in the candidate were
expressly supplied as assumptions in the neutral assignment. In particular,
low information by itself would not imply the physical moment normal form.
This conditional scope is essential to the verdict.

No required scientific correction was identified. Two bookkeeping details
deserve explicit presentation in the final assembly: the concrete failure
allocation in Section 8 below, and the distinction between restricting an
estimate to an observable-transcript event and conditioning the Gaussian
matrix law on a small realized matrix norm. The frozen packet supports both;
the reconstruction below makes them explicit.

## Isolation, input coverage, and checks performed

The neutral assignment authorized only the five candidate files below, the
two optional dependency notes below, the original Nisan paper, and required
process/skill instructions. I read every scientific line of all seven local
files. A combined initial read was truncated; I repaired it using complete
individual reads and sequential line ranges. The moment note was read only
after its author and supervisor announced that its Section 10 addendum was
frozen. I did not read the study README, prior verdicts, cross-check reports,
other studies, archived book material, Git history, or the separately linked
author inputs. No experiment or code benchmark was performed.

| Frozen input | Lines read | SHA-256 |
|---|---:|---|
| QUADRATIC_RESOURCE_RESULT.md | 1–261 | 97afc75b34e57e38a5ceb6a0984d435ee6485fd9218e3313b1dbbb10807ff0d3 |
| EXPLICIT_COMPILER_EXPONENT.md | 1–609 | 93510e4e88f9c632e9c439715b655d4ea6dc1701aae655f0a30d45cbf7f4ba3a |
| QUADRATIC_INITIALIZATION.md | 1–558 | fa97b8cee8bd97c89f098a6776e6b797b0acdbcca9d0470da5e0cceac405f6e8 |
| SHORT_SEED_PRIOR_BLOCKS.md | 1–265 | f63da50dd1e9e9dc0ed0bb4e80eab4abfd27e2fe445b3521b648f1d8417b241f |
| RECALIBRATION_FREE_MOMENTS.md | 1–1305 | 710989a20ec43db01612c5957bcc1ca181249cdbd08db3fea6addc3ec1a081ea |
| DENSE_BUDGET_SELF_NORMALIZED.md | 1–348 | 80de0e2890bc69331f4046ce24f0e1a3dbe00cf52f53e9635f965d22fd34eb36 |
| DENSE_BUDGET_GEOMETRY.md | 1–895 | 50950e2df4d5d9e9eb20201769da7afee39ef2dee389f1ab97744a25ef88df0e |

Required instructions read completely were RESEARCH_WORKFLOW.md, the
investigate-conjectures and solve-math-rigorously skills, and the research
contract and adversarial-audit references. The required custom skill
/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md returned
“Permission denied.” I disclosed this and used the assignment's minimal-symbol
fallback. I did not claim to read that skill or its inaccessible neural
reference.

The external check read the original Nisan paper through the PDF text,
including the finite-state definition, universal-hash calculation, recursive
generator proof, and space-bounded corollary. PDF screenshot retrieval was not
needed for the verdict. Local commands were read-only cat, sed, wc -l,
and sha256sum, followed by creation of this assigned report with
apply_patch. No Git operation or candidate edit was performed.

## 1. Target and dependency boundary

Write \(\ell=\log(en)\). All constants below may depend on the fixed
admissible problem and confidence, but not width. The problem keeps fixed
nonlinear depth, independent Gaussian initialization, zero readout, mean
squared loss and the stated block mobilities; the original spanning training
data, small-label condition, feature-Gram gap and strip-analytic activations
are unchanged. The derivative bound is on the supplied strip, as stated in
the allowed geometry input. It gives the real second-derivative bounds needed
below by Cauchy's formula on a smaller fixed strip.

The inherited finite source has \(R\le C\ell^8\) named fields/calls,
\(P\le CR^2\) scalar summaries, and iid Gaussian row packets
\(Z_i\in\mathbb R^D\), \(D\le CR\). Its ideal noisy summaries obey

\[
 C_r=n^{-1}\sum_iF_r(Z_i;C_{<r})+\eta E_r,
 \qquad |F_r|\le B_F,
\]

with independent standard Gaussian \(E_r\). The supplied physical
interfaces include a predictable finite Gaussian matrix transcript, bounded
conditional mean mixers on observable transcript events, a finite-rank
covariance correction, a sufficiently accurate scalar-source coupling, and
a deterministic dense proof center. These are the scientific inputs being
used, rather than consequences of the resource analysis.

The review's new obligations were whether the actual row marginal can
replace fitted laws, whether prior blocks and one short seed estimate its
moments, whether those estimates retain the physical guarantee, and whether
all new operations obey the displayed numerical degrees.

## 2. Actual marginal, common Grams, and source dependence

For a fixed ideal prefix \(c\), let \(\pi_c\) be its row-array posterior,
\(\nu_c=\pi_c^1\), and \(\mu\) the Gaussian packet prior. The summaries
are invariant under row permutations, so all posterior marginals coincide.
The entropy identity is exact:

\[
 D(\pi_c\Vert\mu^{\otimes n})
 =D(\pi_c\Vert\nu_c^{\otimes n})+nD(\nu_c\Vert\mu).
\]

It follows by expanding the logarithmic density ratio and integrating each
one-row term against its marginal. Both right-hand terms are nonnegative.
No posterior independence is asserted. The bounded Gaussian observation
channel gives information at most
\(H=(P/2)\log(1+B_F^2/\eta^2)\). Convexity of relative entropy makes
the posterior entropy a nonnegative submartingale; the first-crossing
argument bounds it by \(K_*=H/\alpha\) simultaneously at all prefixes,
outside probability \(\alpha\). Consequently

\[
 D(\pi_c\Vert\nu_c^{\otimes n})\le K_*,
 \qquad D(\nu_c\Vert\mu)\le K_*/n.
\]

The same maximal argument for
\(\mathbb E[\sum_rE_r^2\mid C_{\le j}]\) gives the all-prefix bound
\(P/\beta\), outside probability \(\beta\). Conditional expectation of
the acquired moment identity then bounds the difference between each
observed moment and its actual-marginal counterpart. A posterior event of
mass at least \(1-\rho\) simultaneously bounds every realized acquired
noise by \(T_\rho=\sqrt{P/(\beta\rho)}\).

For any numerical prefix \(\widehat c\) within
\(\varepsilon_{\rm hist}\) of \(c\), row-pair sensitivity gives
entrywise posterior and empirical Gram errors at most

\[
 e_G=\eta T_\rho+(1+L_{\rm pair})\varepsilon_{\rm hist}.
\]

An \(r\)-dimensional symmetric entrywise error has operator norm at most
\(re_G\). Therefore, if \(Re_G\le\tau/4\), the observed table plus
\(2\tau I\) dominates both relevant Grams and has floor at least
\(7\tau/4\). The empirical statement is on the single conditional
noise event; the marginal statement is deterministic given the prefix.
Whitening by this same matrix gives both second-moment bounds at most
identity. This remains valid when the unbuffered Grams are singular.

The argument is pointwise in every \(\widehat c\) in the error ball
while keeping \(\nu_c\) fixed. It therefore covers private,
source-dependent numerical acquisition. It neither conditions the posterior
on the selected packets nor requires the numerical prefix to be measurable
from the ideal one. For numerical seed analysis, the full realized source
and its chosen prefixes are instead fixed first; the seed is independent.
Those are two different, compatible uses of conditioning.

The physical coefficient bound also survives the common buffer. If
\(M=TA_0S^T/n\), partial-isometry factorization identifies
\(\|M\|=\|Q_{T,0}^{1/2}A_0Q_{S,0}^{1/2}\|\). The PSD square-root
inequality gives

\[
 \|(Q_T^*)^{1/2}A_0(Q_S^*)^{1/2}\|
 \le\|M\|+2\|A_0\|\sqrt{D(q+D)}.
\]

Here \(D\) bounds each Gram perturbation and \(q\) bounds the empirical
Gram norms. The stated square-root inequality is valid in operator norm even
at zero eigenvalues: order monotonicity implies
\(\sqrt P\preceq\sqrt{Q+dI}\preceq\sqrt Q+\sqrt d I\), and conversely.
The mean represented in whitened coordinates is unchanged because its
whitening factors cancel. The displayed estimate bounds its stable-coordinate
operator norm.

For the conditional variance, the resolvent identity gives

\[
0\le v^T[(\sigma^2I+Q_0)^{-1}-(\sigma^2I+Q^*)^{-1}]v
\le (D/\sigma^2)c_{\rm in}.
\]

This uses the actual joint query/history Gram to obtain
\(v^T(\sigma^2I+Q_0)^{-1}v\le c_{\rm in}\). It is not an inference
from PSD alone without a noise floor. The master-history selection formula
for \(P_{\rm var}\) has norm at most one by direct multiplication with
its transpose.

## 3. Prior blocks estimate the marginal, not a prior expectation

Suppose \(D(\nu\Vert\mu)\le h\), \(\nu(UU^T)\preceq I_r\), and
\(|G|\le B\). Put \(\bar h=\max(h,1/n)\) and
\(s=\lfloor1/(128\bar h)\rfloor\). For sufficiently large width,
\(s\ge1\) and \(s\asymp\bar h^{-1}\).

Under \(\nu^{\otimes s}\), the variance of a coordinate block mean of
\(UG\) is at most \(B^2/s\). Its probability of missing the target
coordinate by more than \(4B/\sqrt s\) is at most \(1/16\).
Product entropy is at most \(sh\le1/128\), so Pinsker's inequality gives
block-law total variation at most \(1/16\). Thus the same coordinate
event fails with probability at most \(1/8\) under the implemented prior
product law. This is a change of law on a whole statistical block.

For completeness, the needed Pinsker form follows by applying the entropy
chain rule to an event attaining total variation: binary relative entropy
is at least twice the squared probability difference, because its second
derivative in the first probability is at least four and it vanishes with
zero first derivative at equality.

For \(J\) independent prior blocks, failure of one coordinate median
requires at least \(J/2\) failed blocks. Its probability is at most
\(2^J(1/8)^{J/2}=2^{-J/2}\). Union over coordinates gives vector error
\(4B\sqrt{r/s}\) with failure at most \(r2^{-J/2}\). For \(G^2\),
replace \(B\) by \(B^2\).

This calculation does not need a prior second-moment bound on \(U\), does
not estimate \(\mu(UG)\), and never evaluates a density of \(\nu\).
It also explains why pairwise-independent rows would not suffice: the
product-law entropy step would then have no justification. The packet does
not make that substitution.

## 4. Physical propagation and the conditioning audit

The self-normalized dependency was checked directly. Its scalar exponential
comparison bounds deviations of an ordinary iid mean on an event controlling
the raw empirical second moment. Applying it to directions of \(UG\) and
a proof-only sphere net gives a sub-Gaussian tail intersected with the raw
Gram event. Integrating that tail and using the entropy inequality transfers
it to the dependent posterior:

\[
 \mathbb E_{\pi_c}\!\left[
 \left\|n^{-1}\sum_iU_iG_i-\nu_c(UG)\right\|^2\mathbf1_E\right]
 \le CB^2(K_*+r+1)/n.
\]

The product comparison law is now \(\nu_c^{\otimes n}\), and the entropy
bound is supplied exactly by Section 2. The Gram event is supplied by the
observed tables and scalar-noise event; its probability is not inferred from
a mere population second-moment bound. The analogous scalar squared-feature
estimate is \(CB^4(K_*+1)/n\).

The physical cap \(B=C\ell^{3/2}\) follows from the inherited complex
safe-strip interface: the first sine Fourier coefficient bounds the physical
time derivative by \(C\ell^{1/2}\), and the interval length is
\(C\ell\). The initial uniform coordinate bound is \(C\sqrt\ell\).
The completed source approximation transfers the cap with a negligible
coordinate error. This argument is used only for the new passive features,
not for arbitrary old Picard/history fields. A fixed twice continuously
differentiable, piecewise-polynomial cap on the output range can supply
bounded first and second derivatives; it
does not require a new integration oracle or a growing stored table.

For covariance removal, a conditional answer covariance
\(\Gamma=\beta I-K\), with \(0\preceq K\preceq\beta I\) and rank at
most \(R\), can be coupled to \(\beta I\) at squared normalized cost
at most \(\beta R/n\). This follows by diagonalization: only the affected
eigen-directions contribute. A passive forward query uses each independent
posterior matrix block once. Higher centered blocks have covariance bounded
by their prior and are independent of the lower-layer incoming difference
conditional on the finite observable transcript. Together with bounded
conditional means and the global activation Lipschitz bounds, layer hybrids
give the stated \(C_LB\sqrt{R/n}\) prediction RMS cost.

The conditioning order matters. The valid proof samples posterior Gaussian
matrices conditional on the finite observable training transcript. Independent
scalar noises may also be fixed there. Mean-operator and Gram restrictions
used inside Gaussian conditional expectations must be measurable from that
transcript and those noises. The inherited observable mean-operator event
has this property. One can then integrate the conditional bounds over that
event. A small realized matrix norm, the dense-center event, or success of
private packet selection must instead be handled as separate posterior
failure probabilities. Conditioning the Gaussian matrix law on any of those
events would invalidate the Gaussian hybrid argument. The candidate's
observable-event hypothesis, parameterwise prefix comparison, and interval
mass argument permit precisely the valid order; they do not require the
invalid conditioning.

For the deterministic common-coordinate matrix, the positive-mass intersection
of the physical event and the Gram event suffices to prove its norm bound:
the matrix depends only on the fixed numerical prefix, and the same bound
is obtained from every array in that intersection. This existence argument
does not replace the conditional law of the matrices by a truncated one.

After covariance removal, integrate a fresh scalar Gaussian before comparing
moments. For a capped activation \(\chi\),

\[
 \partial_v\mathbb E\chi(m+\sqrt v\,g)
 =\tfrac12\mathbb E\chi''(m+\sqrt v\,g)
\]

at positive variance, by two integrations by parts; continuity extends the
bound to zero variance. Thus the Gaussian mean is Lipschitz in variance,
not only in its square root. The upper history-Gram bounds give
\(\|\mathbb E[Vq]\|\le\|q\|_{L^2}\) and
\(\|b\|\le B\). Consequently variance discrepancy is bounded by
\(y+2Bx\), and the packet's two linear recurrences for cross-moment error
\(x\) and second-moment error \(y\) follow. Fixed depth causes only a
fixed polynomial in \(B\), hence a logarithmic factor.

The row-law concentration estimate is applied at deterministic reference
parameters. Empirical or seed-dependent parameters are compared to them
through these recurrences; they are not silently inserted into a fixed-test
entropy bound. Fresh Gaussian row fluctuations add their explicitly bounded
conditional variances. Guards project moments into their correct balls and
clip only infeasible negative residual variances, so they do not enlarge the
relevant errors. The posterior-to-reference RMS error is therefore
\(C\ell^{C_L}/\sqrt n\) on the common Gram event, with its complement
charged separately.

## 5. One seed, finite contexts, and the row/block distinction

For the external theorem I checked [Nisan, *Pseudorandom generators for
space-bounded computation*, Sections 2–4](https://mathweb.ucsd.edu/~sbuss/CourseWeb/Math268_2013W/Nisan_PRG.pdf).
The finite-state definition bounds all information present between random
blocks; it imposes no computational bound inside a block. Lemma 3 supplies
exponentially small error for exponentially many blocks when state bits and
log block count are bounded by a constant times block length. The recursive
generator uses linear-description universal hashes. Enlarging block length
therefore yields seed length
\(O((S+\log N+\log\epsilon^{-1})\log N)\) for \(N\) blocks and
between-block state \(S\), with error \(\epsilon\). The variance calculation
in Lemma 1 and the concatenation induction in Lemma 2 support that
specialization; no repeated-read theorem is needed.

In the candidate, one generator block supplies one whole Gaussian row.
The potentially much larger matrix/row-evaluation scratch is cleared before
the next random row. Only accumulators, completed block means, finite
coefficients, the fixed context, and counters survive. Hence a test has
between-row state at most

\[
 J\times R\times C\ell^{120}\le C\ell^{244}
\]

bits. The row's \(C\ell^{128}\) Gaussian bits fit in a block of length
\(C\ell^{244}\). With at most \(nC\ell^{116}\) rows,
\(\log N=O(\ell)\), so the seed has \(C\ell^{245}\) bits. The actual
generator's retained seed and transient hashing storage are separately
counted; they need not be included as baseline-test state in the theorem.

Fixing the complete source first fixes the ideal/numerical prefixes and all
coefficient tables. Query inputs, patch time, and guarded intermediate
moments have at most \(C\ell^{16}\) coordinates. At context precision
\(C\ell^{100}\), their possible codes have logarithmic cardinality at
most \(C\ell^{116}\). These codes are not enumerated or retained. The
union includes codes reached through earlier seed-dependent estimates, so
no conditional independence of successive integral estimates is needed.

A fixed-context failure test may hardwire a rational approximation to its
inaccessible exact target. Its target coordinates are bounded by \(B\)
or \(B^2\), so precision \(C\ell^{120}\) suffices. Choosing a comparison
radius strictly larger than the baseline statistical radius leaves a
rounding margin. This threshold is proof advice for an arbitrary finite
state test; it is not an input or hidden oracle of the decoder.

Taking \(J=C\ell^{116}\) and an exponentially small enough PRG error
makes the finite-context sum of median and generator failure probabilities
small. Restarting the same seed at another context means another one-pass
test, not a repeated-read execution of a single test. Union bounds do not
require independence between these tests. Thus this is one event for the
repeatable function evaluated at every later adaptive query.

The numerical Gaussian cutoff \(T_G^2=C\ell^{120}\) is also sufficient.
Its tail after summing rows, coordinates and contexts is exponentially small
in \(\ell^{120}\), which dominates the context logarithm. The clipped
quantile's derivative is at most \(C e^{T_G^2/2}\); a sufficiently large
constant in the same \(\ell^{120}\) uniform-bit precision makes its
coupled coordinate error negligible after the capped row Lipschitz factor.
A cutoff of only \(O(\sqrt\ell)\) would not justify this particular union;
the candidate does not use it.

The finite Gaussian calculation needs no uncounted numerical oracle.
Bisection for a quantile uses a polynomial number of CDF evaluations;
integration of the exponential series on the bounded interval, with precision
including its possible cancellation, has polynomial degree far below the
stated row-interpreter allowance. Deterministic context rounding is compared
through the exact capped circuit, then numerical error is added. Continuity
of the median, rounded program, or branch decisions is never assumed.

## 6. Explicit precision and compiler degrees

The compiler enumerates its physical loops and two-orientation Gaussian
conditioning operations. Padding all small matrices to dimension \(CR^2\)
and charging dense products gives at most \(CR^6\) instructions per
conditioning call, hence at most \(CR^7=O(\ell^{56})\) graph nodes in
total. Shared row nodes are cached; no recursive substitution multiplies
the graph size.

With \(X=C_*(2+n+R+\sigma^{-1})\), \(\log X=O(\ell^2)\). Its caps
are amplitudes, not operation counts. A fixed power of \(X\) bounds each
local sensitivity. Topological error propagation through \(CR^7\) nodes
therefore has logarithm \(CR^7\log X=O(\ell^{58})\); sequential scalar
acquisition adds a factor \(P\), giving \(O(\ell^{74})\).

I checked the numerical degree accounting rather than treating a matrix
inverse or root as unit work. Clearing dyadic denominators and computing
cofactors by reduced rational elimination bounds intermediate fractions
by minors. For macro size parameter \(h\), inverse time is at most
\(Ch^{11}\). A positive-matrix Newton root iteration uses \(O(h)\)
steps and an \(O(h^2)\)-bit internal grid. This grid remains sufficient
even without exact commutation of rounded iterates: on a half-gap domain,
the symmetrized Newton map has Lipschitz constant at most a fixed multiple
of \(1+M/a\); \(O(h)\) iterations amplify errors by at most
\(\exp(O(h^2))\). This also preserves the half-gap by induction.
The resulting inverse substeps have \(O(h^3)\)-bit minors, total root time
\(Ch^{15}\), and scratch \(Ch^5\). A final return-grid reset prevents
the larger private precision from becoming the next macro's input size.

The positive-part approximation using \(\sqrt{A^2+v^2I}\), a small
positive diagonal buffer, and a nonnegative downward-rounded radial scale
preserves PSD and the cap. Its artificial inverse-gap logarithm is only
\(O(h)\). Thus it has the same macro degree. At most \(N\) such operations
and graph caching give the complete row bounds

\[
 \mathcal H=2+b+C\ell^{58},\qquad
 T_{\rm row}\le C\mathcal H^{16},\qquad
 S_{\rm row}\le C\mathcal H^6.
\]

The moment note's Section 10 closes the potentially dangerous whitening
extension. With a dyadic \(\overline X\asymp X\), it chooses
\(\tau=\overline X^{-512}\). Raw mean coefficient norm at most
\(\overline X^{102}\) and Gram norm at most \(\overline X^{202}\)
make the buffer norm error at most \(C\overline X^{-53}\). The variance
error is at most \(C\overline X^{-310}\). Fixed-depth propagation is
eventually smaller than one further factor \(\overline X\), so these
are negligible compared with the target root-width error.

The new inverse roots have norm at most \(\overline X^{256}\),
inverse-root Lipschitz factor at most \(\overline X^{768}/2\), and
all new operands and local sensitivities fit in the explicitly enlarged
fixed powers of \(\overline X\). Their node count is only \(CR^4\),
below the existing \(CR^7\). The global sensitivity degrees remain 58
and 74. No factor \(\tau^{-1}\) is charged as an iteration count.

Choosing scalar noise after the ridge, with logarithmic inverse noise
\(O(\ell^{74})\), meets both source perturbation and common-Gram
accuracy. This makes \(H=O(\ell^{90})\), and therefore
\(\bar h=\operatorname{polylog}(n)/n\). History and source-entry
precision \(C\ell^{100}\) dominate all acquisition amplification.
The query precision \(C\ell^{120}\) dominates it as well as Gaussian
discretization. None of these exponents depends on depth; fixed-depth
constants and the eventual width threshold may depend on it.

## 7. Initialization, rational support, and final resource arithmetic

The exact finite real-valued row law simulates the supplied noisy Gaussian
matrix program by independent packets and small empirical reductions. It
does not form dense initialized matrices. The source's extra scalar noise
and numerical arithmetic are separate perturbations covered by coupling;
they are not falsely declared exact Gaussian posterior identities.

For support reduction, the inserted integer columns are
\(b_i=(1,v_i)^T\), where all dyadic moment vectors use a common denominator.
An affinely independent old support acquires at most one dependence when
one point is inserted. The signed null vector has both signs; ratio
elimination deletes a nonzero coordinate of its one-dimensional nullspace,
so the remaining support is independent, including ties. Thus at most
\(P+1\) positive weights remain.

The bit reset is substantive. At prefix length \(k\), an invertible
support minor \(H\) and the integer prefix-sum target \(t\) satisfy
\(H(kp)=t\). Cramer's formula bounds every weight numerator and
denominator by \(C(P+1)(\beta+\log n+\log(P+2))\) bits. Recomputing
these unique weights prevents an accumulation of old denominators.
Determinant expansion is used only as a size bound; actual elimination is
polynomial work. There is no assumed lower bound on selected weights.

Selection is applied to the vector of all rounded row contributions at
the completed numerical source tape. The weighted panel reproduces every
one of these rational means. Reexecuting the deterministic evaluator with
the same rounding and noise marks reproduces the entire numerical prefix
by induction, not merely approximately. Its coupling to the ideal source
still uses the separately counted precision recurrence. A panel selected
from the source need not be iid, and the decoder does not condition on it.

The resulting exponent calculations are:

| Count | Derivation | Bound |
|---|---|---:|
| Source row work | precision 100 times degree 16 | \(C\ell^{1600}\) |
| Source scratch | precision 100 times degree 6 | \(C\ell^{600}\) |
| Source sweeps and vector reconstruction | \(nP\) row evaluations | \(Cn\ell^{1616}\) |
| Rational support reduction | \(nP^8\beta^3\), \(\beta=O(\ell^{100})\) | \(Cn\ell^{428}\) |
| All compact acquisitions | \(P(P+1)\) row evaluations | \(C\ell^{1632}\) |
| Temporary packet array | \(nD\) entries of precision 100 | \(Cn\ell^{108}\) bits |
| Retained description | graph/panel, including rational weights | \(C\ell^{156}\) bits |
| Query row work | precision 120 times degree 16 | \(C\ell^{1920}\) |
| Query row scratch | precision 120 times degree 6 | \(C\ell^{720}\) bits |
| All query rows | \(n\), statistical blocks 116, moment calls 16 | \(Cn\ell^{2052}\) |
| Generator hashing | per row 489, blocks 116, calls 16 | \(Cn\ell^{621}\) |
| Retained seed | between-row degree 244 plus \(\log N\) | \(C\ell^{245}\) bits |

The rational selection workspace has degree at most 148 and is below the
source scratch allowance. Weighted-update rational arithmetic has bounded
polylogarithmic descriptions even under a simple product-denominator sum;
it fits well below the displayed row-work allowance. Block-mean storage,
median sorting, small coefficient matrices, counters, generator scratch,
and source-panel descriptions all fit below the conservative peak degree
722. Initialization's packet storage and scratch are therefore
\(C[n\ell^{108}+\ell^{600}]\), as claimed.

Rounding work exponents up to 1700 and 2100 is valid. For each fixed
admissible problem, \(n\ell^{2100}=o(n^2)\), so these bounds eventually
fit the prescribed dense-work budget. This comparison gives no useful
practical crossover and imposes no feasible numerical width claim.

All these are the prescribed primitive-model bounds. An arbitrary analytic
activation need not have a uniform computable internal bit-cost exponent.
The packet correctly counts its primitive output precision and separately
states the cost of externally supplied precision evaluators. That limitation
cannot be removed by the word “analytic.”

## 8. Exact confidence, sphere/time uniformity, and independent reference

Set \(\gamma=\delta/256\). The dense-pair certificate with failure
\(\gamma\) yields a deterministic proof center by averaging over one
dense trajectory. For each independent original-law trajectory, its distance
to that same center is at most \(b_n(\gamma)\) except with probability
\(\gamma\). The center is neither computed nor stored.

Here is a concrete allocation compatible with the exact argument in the
assembly. Choose \(q_0=1/32\). Put the virtual-source center event, whose
failure is at most \(\delta/256\), into the complete source event
\(\mathcal G\). Allocate at most another \(\delta/256\) in total to
its remaining physical, observable-operator, and acquisition failures,
using their supplied fixed-confidence versions. Then

\[
 \Pr(\mathcal G^c)\le\delta/128=q_0\delta/4.
\]

The posterior bad-source probability is a nonnegative martingale. Extend
the prefix filtration by a terminal reveal of
\(\mathbf1_{\mathcal G^c}\). The maximal inequality then costs at most
\(\delta/4\) and simultaneously ensures that the actual source is good
and all its prefix posteriors assign source failure at most \(q_0\).
The terminal reveal is necessary for the first assertion.

Take entropy and conditional-noise outer failures
\(\alpha=\beta=\delta/8\), and total numerical-seed failure at most
\(\delta/4\), including median, finite-Gaussian, and PRG errors. These
sum with the preceding maximal failure to \(3\delta/4\). The independent
reference-center failure \(\delta/256\) fits the remaining \(\delta/4\),
as do any separately charged finite-source coupling failures not already
included in \(\mathcal G\). The resulting sum can be made at most
\(\delta\) without changing the certificate argument to a smaller,
undisplayed confidence.

For each good prefix, every numerical prefix in its error ball, and every
fixed input/time, the posterior query has a high-mass interval around the
dense center, and another around the deterministic marginal-recursion
value. Choose Gram and RMS conditional thresholds with losses, for example,
bounded by fixed multiples of \(1/32\), so the interval masses sum to
more than one. Their intersection proves a deterministic bound between
the two centers. This inference holds for every input and time on the same
prefix event; it is not a continuum union of random-query couplings.

The finite-context seed event then compares the implemented decoder with
the marginal recursion for all actual input/time/moment contexts. Adding
the independent actual-reference center bound gives

\[
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |f_{\rm compact}(t,x)-f_n^{\rm ref}(t,x)|
 \le 2b_n(\delta/256)+C\ell^{C_L}/\sqrt n.
\]

Completed time patches and the inherited frozen tail include the fitted
endpoint. For fixed nonzero labels, the supplied positive
\(\exp(CY^2\sqrt\ell)\) factor in the certificate eventually dominates
every fixed power of \(\ell\), so the remainder is absorbed into one
more certificate radius. Zero labels use the exact zero predictor.

Independence of the virtual source and the reference is used exactly here:
the source and seed events can be established without seeing the reference
root. The argument does not promise a bound conditional on an arbitrary
exceptional reference realization. It also does not add an unnecessary
reference-to-virtual triangle radius, because both comparisons use the same
deterministic proof center.

## Final assessment

The new block-statistical, numerical, selection, and short-seed arguments
close their stated obligations. The resource and error claims pass this
isolated internal check with the inherited-source dependency boundary above.
No practical speedup, implementation benchmark, matched-root compressor,
polylogarithmic initialization workspace, ordinary small-network gradient
flow, or promotion to established material follows from this verdict.

## Scoped post-review delta check

2026-10-06. At the supervisor's explicit request, I read the complete final
QUADRATIC_RESOURCE_RESULT.md (295 lines) and SHORT_SEED_PRIOR_BLOCKS.md
(274 lines). These were the only new scientific inputs. I did not follow
their added review or author-check links, and did not inspect another
reviewer's findings. The earlier full review and its frozen-input hashes
remain unchanged above; this section covers only the subsequent edits.

**The PASS verdict is preserved, with exactly the same inherited-interface
scope.** The mean-coordinate clarification now correctly separates exact
invariance of the represented mean from the small buffer increase in its
operator-norm bound. The Section 10 link identifies the already-reviewed
whitening extension. The observable-transcript conditioning clarification
and explicit confidence allocation match Sections 4 and 8 of this report.
In particular,
\(1/4+1/8+1/8+1/4+1/256=193/256<1\), with source and finite-sampling
failures placed inside the stated groups. Review status and links do not
change the mathematical hypotheses.

The finite block-size change is valid. Let
\(h_+=\max(h,1/n)\), choose the certified dyadic number
\(h_+\le\widehat h\le2h_+\), and set
\(s=\lfloor1/(128\widehat h)\rfloor\). At sufficiently large width,

\[
 \frac{1}{512h_+}\le s\le\frac{1}{128h_+},
 \qquad
 sD(\nu\Vert\mu)\le sh\le\frac1{128}.
\]

The lower bound uses \(\lfloor u\rfloor\ge u/2\) for \(u\ge2\).
Consequently the same block change of law holds and the statistical radius
\(B\sqrt{R/s}\) remains at most an absolute constant times
\(B\sqrt{Rh_+}\). The number of rows cannot increase. Since \(h_+\ge1/n\),
a certified dyadic enclosure with absolute precision a sufficiently small
constant times \(1/n\) already permits such a factor-two upper estimate;
it requires no realized posterior entropy or exact transcendental floor.
This change does not affect any seed, workspace, work, or probability
exponent.

The newly displayed evaluator overheads also check: the graph has at most
\(C\ell^{56}\) primitive calls per row, source construction uses at most
\(Cn\ell^{16}\) row evaluations, and all compact acquisitions use at most
\(C\ell^{32}\). Their external evaluator costs are therefore bounded by
\(Cn\ell^{72}T(C\ell^{100})\) and
\(C\ell^{88}T(C\ell^{100})\), respectively. Their workspace addition is
the maximum single-call evaluator workspace, not the number of calls times
that workspace. The query overhead \(Cn\ell^{188}T(C\ell^{120})\) is
unchanged. These qualifications preserve the primitive-model theorem.

The final inputs of this delta check have SHA-256 hashes:

| Final input | SHA-256 |
|---|---|
| QUADRATIC_RESOURCE_RESULT.md | e753d74e80bb4061d10c2c7f735e33991382d93f27c6c638a35c80afac695ccd |
| SHORT_SEED_PRIOR_BLOCKS.md | 78e5f21ce787adac48b5ca745f330af92c87330934dd1634132c0b2308c35201 |

Only this scoped addendum was written. No candidate edits, experiments,
additional scientific retrieval, or Git operations were performed.

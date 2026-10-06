# Independent internal audit of the integrated source and Legendre proofs

2026-10-06. Scoped reconstruction from the frozen inputs below. This is an
internal mathematical audit, not a promotion review or approval to change the
maintained book.

**Status: conditional pass for the assembled source/Legendre text.** The
mathematical arguments examined below pass this reconstruction. Two conditions
remain for the assembled artifact: include the all-time extension and its
deterministic width gates as part of the proof, and correct the notation
conflicts listed below. The originally supplied three-file scientific packet
was incomplete for the all-time carrier claim; the subsequently authorized
analytic-tail input resolves that mathematical dependency. No additional label
restriction, order restriction, or effective stochastic width threshold was
obtained or assumed in this audit.

## Frozen inputs and access scope

All listed files were read completely. The scientific input hashes were
unchanged on recheck immediately before writing this report.

| Input | SHA-256 |
|---|---|
| `INTEGRATED_SOURCE_SECTION.md` | `ddef8fdef8232f4a0352353ea1b3670f1af8f3b9fea5d47629924323055e459f` |
| `INTEGRATED_LEGENDRE_SECTION.md` | `3b88db78111172729bbecc5e31f8a7581952b6d3db1b5475300e0661086e69cb` |
| `GENERAL_EXPLICIT_FITTING.md` | `5c6f12b78847a2b2874c5bc82eb1cea5f4929ee071b114d09b098397c5e2b8d6` |
| `ANALYTIC_TAIL_EXTENSION.md` | `70ec072f0e83c74364f068d61f04148bf110771fd06b4b2b874bb3c5d8dfc349` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |

The analytic-tail file was added to the permitted packet after the missing
all-time dependency was reported. Its source-domain continuation and real
carrier extension, §§2–4, were independently checked. Its separate compact
comparison claims in §5 cite scientific inputs outside this assignment; those
claims are not certified here. Their presence does not enter the Legendre
proof.

The complete `solve-math-rigorously` skill and `AGENTS.md` were read. The
requested canonical-notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` returned
`Permission denied`; no accessible copy was found in the available system skill
directories. Its linked neural-network instructions consequently could not be
read. The explicit presentation rules in the assignment and the complete
notation contract were applied, but full compliance with that inaccessible
skill cannot be asserted. No author history, prior reviews, other studies,
archived book material, experiments, or Git writes were used.

## Required assembly and notation corrections

1. The source section establishes its stochastic domain through
   \(T_0=32\lambda^{-1}\log(en)\), where \(\lambda=\gamma/m\). The
   Legendre section uses an all-time dense-carrier maximum. Include the
   analytic-tail proof, especially its explicit gate (9b), before treating
   `Legendre-carrier-event` as proved. Its recurrence yields
   \[
   \max_{a,j}\|k_a^{(j)}(t)-k_a^{(j)}(T_0)\|_\infty
   \le C_{\rm tail}n\|\theta(t)-\theta(T_0)\|_{\rm par}.
   \]
   Dense energy bounds the last parameter distance by
   \(2Y\lambda^{-1/2}(en)^{-16}\). Gate (9b) therefore gives exactly
   \(2K_{\rm src}(16Y/\lambda)\sqrt{\log(en)}\), the factor in the
   Legendre event. This is a deterministic eventual width condition, shared
   by all orders and accuracies.

2. In the source section, \(t\) denotes both physical time and a fixed
   second-derivative bound. Rename the latter consistently to \(t_2\).
   Replace finite RMS shorthand such as \(\|u\|_{2,n}\) by
   \(\|u\|_2/\sqrt n\), as required by the notation contract. In the
   Legendre signed-stability proof, replace plain \(\Delta\) for a
   parameter difference: the contract reserves plain \(\Delta\) for a
   proof mesh. Also expand the newly defined normalized sample pairing
   \(\langle u,v\rangle_m\) if the final artifact is to follow that
   contract's explicit-factor convention throughout. These corrections
   leave the audited coefficients unchanged.

The sections assume that the integrated model statement supplies the analytic
activation class, initialization, covariance recursion and parameter types;
they are sections of that document, not standalone substitutes for its model
statement.

## Dense fitting and deterministic late-time extension

The explicit initialization threshold is sufficient. The two Gaussian matrix
net bounds leave failure below half the budget. Conditional Chebyshev,
covariance-map Lipschitz constant
\(s^2+t_2(b+\sqrt2sH)\), and the stopped covariance recursion give the
remaining half. A query net needs individual squared norms, not all pairwise
query covariances. Its off-grid feature increment is at most \(H/4\).
Neither bounded activation values nor covariance normalization is used.

The normalized parameter energy identity has the correct factor for the stated
loss and mobilities. Weighted Cauchy–Schwarz gives total path length
\(2Y/\sqrt\lambda\). Hidden displacement is quadratic in labels because
the initial readout is zero. The displacement and singular-value margins close
the operator, feature and readout-Gram stops under the displayed label cap.
The whole-sphere endpoint tail and its numerical simplification follow from
the instantaneous feature recurrence. The zero-label case is stationary.

In the analytic extension, the parameter ball has radius of order
\(n^{-1/2}\), whereas the late-time parameter tail is of order
\(n^{-16}\). The explicit gate (7) keeps every late complex-time disk
inside one common ball around the last source time. The derivative recurrence
controls all query preactivations there. Picard continuation and uniqueness
therefore preserve the original time/query radii without a new random event.
The carrier recurrence in (9a) includes the changed matrix, propagated carrier
and changed gate; its two conversions from RMS to a coordinate maximum explain
the conservative factor \(n\) in (9).

## Source reconstruction

The finite-deletion argument was checked with the original width normalization
and deletion of activations rather than replacement by zero preactivations.
Its retained equation has both the forward port and the reverse chain-rule
force. At the top, the prediction offset multiplies both retained forces.
The first layer has no reverse port. These endpoint changes are necessary for
the stated unbounded-activation class and are included.

The mobility-coordinate Hessian has one carrier in each curvature diagonal.
Its remaining factors pass through spaces of dimension at most \(n\).
Augmented preactivation ports make response derivatives Hessian subblocks.
Consequently the normalized Schatten estimates do not introduce the number of
parameters. The real negative-Gram part contracts; the residual-Hessian part
has logarithmic-width exponent \(D_*S^2/\eta\le1/4000\). The eventual
\(n^{1/1000}\) propagator cap thus follows from a prior smallness condition,
not from enlarging width while keeping an excessive exponent.

The Gaussian control-net exponents have strict room: map norms at most
\(n^{1/200}\) give variance at most \(n^{-99/100}\); threshold
\(n^{-1/10}/2\) has squared Gaussian scale \(n^{79/100}\). The
eventual control-net logarithm \(n^{13/20}\) is smaller. Centered quadratic
and independent-root bilinear forms have the same or better scale. The
nonlinear remainder terms \(n^{-8/100}\) and the square of a remainder
stopped at \(n^{-1/25}\), even after propagation and logarithmic factors,
are smaller than that stopping radius. The incoming probe argument controls
the reverse force. Adaptive controls are substituted only after the uniform
Gaussian event is established.

In the trace summation, splitting the \((h+2)\)-power and using
\((h+2)^h/h!\le e^{h+2}\) produces the displayed
\(576e^3D_*^3\mathcal B S^4/\eta^3\) coefficient. The asymmetric
forward trace uses one endpoint in Hilbert–Schmidt norm and the other in
operator norm. Learned-row and learned-column terms retain their actual
feature RMS and backward amplitudes. The evaluated-sample direct trace is
separate from the driving-sample RMS; this explains the individual
\(Z_{a,i}\) term in (S.15).

The feedback coefficient in the sample-RMS inequalities is
\(4D_0C_FS^2\le1/2\), so the stated absorption envelope follows.
The backward activity modulus handles unbounded reference carriers by an
explicit high/low split. Gaussian chaining and Jensen then give exponential
moments for samplewise and sample-RMS references without independence across
samples. The mixed query endpoint recurrences account for the instantaneous
reverse trace, integrated response and learned row; no query-coordinate
exponential budget is introduced.

For budget removal, the deletion number and empirical moment degree are fixed
before width tends to infinity. Distinct roots are independent conditional on
their common cavity; collisions contribute one fewer free neuron index.
Projected common-cavity errors exclude the paired root and have vanishing
fixed moments. The bound
\(\limsup_n\Pr(\text{budget hit})\le mL(16L/\mathcal B)^p\) therefore
permits the subsequent infimum over fixed integers \(p\). It does not
permit a deletion count growing with width and supplies no computable onset
width. The text discloses both limitations.

The explicit source recurrence and power ledger are consistent with
\(S_*^{\rm src}\ge\beta^{-26L}\) and
\(K_{\rm src}\le\beta^{21L}\). In particular the cap
\(Y/\lambda\le\beta^{-30L}\) implies every source-smallness entry.
The coefficients use linear growth and derivative bounds, not globally
bounded or normalized activation values. No cap \(\lambda\le1\) was
inserted.

## Legendre reconstruction

The moment ODEs are exactly the derivatives of moving-interval Legendre
moments, including the initialized forward prefix and zero backward prefix.
The equations have no division by residual magnitude. Differentiation of the
bilinear projection integral yields the product of the two endpoint errors,
with coefficient \(2\widehat\rho/(mn)\). The moving and fixed coordinate
counts match the retained matrices, vectors, moments and scalar clock.

The weighted tail, endpoint derivative tail and growing-interval energy
identities have the stated factors. The endpoint kernel proof bounds the
variation of \(P_k\) by \(36\sqrt k\); the stated constant 64 is
conservative. In all-order fitting the factors depending on order cancel:
the squared backward endpoint factor \((q+1)^2\) is paired with the
weighted projection denominator \(q(q+1)\). This gives the displayed
defect energy, feature recurrence and Gram margin. The sharper endpoint
kernel yields the order-independent pointwise defect with coefficient
\(130\sum_{\ell=2}^LD_\ell\sqrt{C_{\ell-1}}\). Its label allowance
closes residual decay and the path-length/readout stops for every positive
integer order.

The signed stability argument uses the dense carrier maximum only. Backward
subtraction places the changed gate against the dense carrier, so it needs no
carrier maximum for the compressed state or parameter segment. The parameter
energy retains the negative residual-difference square. Its remaining growth
is bounded by \(K(\rho_D+3\widehat\rho)\), whose time integral gives
exactly the coefficient 14 in the stability exponential.

For projection comparison, recording the dense response in the compressed
clock avoids an inverse residual bound: the remaining clock length cancels
the inverse clock speed in weighted derivative energy. Freezing at physical
time \(2\log q/\kappa\) yields the stated logarithmic numerator and
includes \(q=1\). Growing-interval energies bound the integral of the
absolute defect, not just its signed integral. The resulting absorption
threshold is the displayed \(T_n\).

For orders at least \(T_n\), the first full-range error term follows.
For smaller orders, \(U(T_n/q)^4\) dominates the uniform prediction cap
\(U\); therefore the full-range statement has no hidden order gate.
The simple-cap power ledger bounds both the large-order numerator and
\((U/Y)T_n^2\) by its unchanged coefficient \(P_n\). It consequently
covers the small orders as well, without reducing the labels as a function
of requested accuracy. The structural envelope is a valid further weakening.

Both inverse constructions are valid: \(\sqrt{\log(eq)}/q^2\) decreases
strictly for \(q\ge1\); the closed sufficient order leaves the stated
half-error margin when its ratio exceeds one. Allocating half the target to
each full-range summand gives its displayed sufficient inverse. Storage is
affine and increasing in order, so the floor formula is exact for the stated
coordinate budget. The root-width prescription and fixed-problem rates follow
with \(C_n,T_n=n^{o(1)}\). These are sufficient certificate rates, not
lower bounds or claims about bit complexity.

## Probability and final scope

One initialization/source event at each sufficiently large individual width,
augmented by the deterministic late-time width gates, supports every Legendre
order and accuracy. No union over orders is used. The confidence-dependent
source onset remains qualitative; only the dense-fitting threshold and the
additional deterministic inequalities are effective. The inverse interface
correctly certifies order after a reference width is in that range, and does
not promise an effective confidence-certified choice of that width.

This audit found no remaining mathematical blocker in the assigned assembled
source and Legendre claims, subject to the explicitly identified all-time
dependency. It does not certify compact-runtime claims, independent-dense
comparison, promotion readiness, or inaccessible skill instructions.

## Final assembly binding and resolution

2026-10-06. **Final internal mathematical status: PASS for the assigned
source and Legendre claims in `RESULT.md`.** This supersedes the assembly
conditions in the initial conditional verdict. The final assembled document
has SHA-256
`e24e2f519bd597159f1745ce46e9f9ad27c8772e9ef80807907b63557401c562`, verified
directly before this addendum.

The permitted recheck covered the shared setup and qualifications, complete
source section and activation-power ledger, complete Legendre statements and
proofs, and the analytic-extension gates and proof. Anchor-based comparisons
against the previously audited frozen sections show only the intended heading
and notation changes. The coefficient `t` became `t_2` throughout the source
recurrences; vector RMS and empirical higher moments are explicit; the Hessian
Hilbert–Schmidt normalization remains exactly division by `sqrt(n)`; and the
matrix Schatten convention now defines its singular-value sum. The Legendre
parameter difference is `e_theta`, and every changed sample pairing retains
its explicit factor `1/m`. No coefficient, sign or normalization was lost.

The final document includes the deterministic continuation and all-time carrier
proof at `compact-analytic-extension-proof`, with both additional eventual
width gates displayed under `compact-storage-count`. The introductory proof
dependency paragraph explicitly identifies this extension as the source of the
Legendre all-time carrier bound. Thus the previous missing assembly dependency
is resolved within the document. The shared setup supplies the analytic
activation class and model definitions; the all-order event and qualitative
stochastic-width qualifications remain unchanged.

The following extracted-section SHA-256 values were checked again against the
final document and matched the versions inspected during assembly review:

| Reviewed assembled content | SHA-256 |
|---|---|
| Source foundation through its power ledger | `e6cc1821c7e3e2cf015067dfd1a21ee1ff1b8070aafc08bc152f2fdeaa7aefc8` |
| Legendre statements followed by Legendre proofs | `2f4ca0fc6edc72ca92e2b8cce813f12283124ef264de6408c73be9d411a9368d` |
| Analytic-extension proof | `c74a9af5f20db39bc0a3890de94dfb67c5840067e39629e73e2a36ce6e952d51` |
| Construction-width qualification paragraph through the end of its gates | `e4c02a8bb30f86ee4472fb4704655339a731b2549c1970798dcaf480b5bf5f53` |

The skill-access limitation and the original scope exclusions remain in force.
This addendum does not extend the audit to compact comparison, independent
dense comparison, or promotion. The temporary source/Legendre drafts may be
removed after consolidation without changing this final binding; their
previously audited hashes are retained above, and the complete relevant
content is now bound to `RESULT.md`.

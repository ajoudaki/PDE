# Output-kernel Stieltjes conjecture

The sole authoritative scientific narrative is
[CURRENT_RESEARCH_STATE.md](CURRENT_RESEARCH_STATE.md). It directly contains
the canonical conjecture, exact derivatives and moments, all five parametric
campaigns, the completed Campaign-6 stopping decision, theory routes,
counterexamples, numerics, conditional reconstruction, and current open
obligations.  Campaign-local reports and certificates are linked from that
master as lower-level evidence, not as competing research-state reports.

The canonical verdict remains finite-order compatibility without an
all-order proof or counterexample: its first eight moments are exact and pass
every decidable Hankel test, including the newly completed ordinary and
shifted $4\times4$ matrices.  The stronger uniform block-metric extension,
however, is **disproved**.  For \(\beta=1\), an exact width-limit jet through
order thirteen gives a negative shifted \(3\times3\) Hankel determinant for
every \(0\leq\alpha\leq1/100\).  Thus strictly positive metrics
\((\alpha,1)\), \(0<\alpha\leq1/100\), are counterexamples; no layer needs to
be frozen.  On the complete available six-moment \(\beta=1\) slice, that
determinant has a unique positive zero
\(\alpha_*=0.017519225541486\ldots\); all truncated gates pass strictly
above it, but this is not an all-order good-range theorem and no joint
high-order \((\alpha,\beta)\) classification exists.  At the
\(\alpha=0\) boundary, an exact rescaling gives the standard one-hidden-layer
raw-square network, whose formal shifted \(3\times3\) determinant is also
negative.  Its neurons nevertheless have explicit Riccati characteristics:
Stieltjes positivity is not a necessary condition for low-dimensional
characteristic structure, although no closed scalar loss ODE or global
Gaussian population curve follows.  The same recurrence framework first determined canonical
$F^{(13)}(0)$ and was then specialized in two isolated exact implementations
through $F^{(17)}(0)$.  The resulting $\mu_6,\mu_7$ make both $H_3$ and
$H_3^+$ positive definite.  The proof, certificates, and independent audits
are in [resolution_program](resolution_program/), with the high-order
successor in
[canonical_high_order](resolution_program/canonical_high_order/).  These are
finite-order passes only, and no order-nineteen run was attempted.
The same recurrence states were then audited for the two hidden preactivation
norms in
[canonical_hidden_high_order](resolution_program/canonical_hidden_high_order/).
The first hidden squared-RMS response has nine exact moments with
$H_4,H_3^+\succ0$; the independent second-hidden companion has eight exact
moments with $H_3,H_3^+\succ0$.  Every accessible principal minor also passes
for the normalized literal RMS curves.  This is again finite-order evidence:
the first response is inherited from the output conjecture, while the
second-hidden all-order companion remains open.
Separately, the
[generic-activation compiler](../mean_field_peeling/generic_first_stieltjes/README.md)
gives a smooth bounded normalized-sine counterexample with every block
trained at the equal Euclidean metric: already \(\mu_0<0\) and
\(\mu_1<0\).  Hence neither smoothness nor equal learning rates support a
universal-over-activations Stieltjes claim.  This does not alter the
canonical quadratic point.
The original parameter campaigns remain valid at their frozen finite-order
claim levels; Campaign 6 remains historically inconclusive but is superseded
for canonical D13 identification by the exact recurrence.

This study owns the transformation from the quadratic-network feature jet to
the output-coordinate kernel, the Stieltjes moment problem, conditional
rational ODE reconstructions, and numerical falsification attempts. The raw
feature derivatives and their exact decorated-forest compiler live in the
separate [mean-field peeling study](../mean_field_peeling/).

Directory map:

- [theory](theory/) contains exact transformations, Hankel certificates,
  quadratures, homotopy calculations, and total-nonnegativity audits;
- [numerics](numerics/) contains frozen protocols, reports, compact summaries,
  and integrity metadata; raw arrays and bulk logs are intentionally ignored;
- [resolution_program](resolution_program/) contains the target contract,
  exact block-metric counterexample theorem and certificate, checker,
  proof-route audit, and the canonical order-fifteen/order-seventeen
  successor with exact eight-moment output Hankel certificates, together with
  the canonical hidden-norm successor and its squared/literal-RMS all-minor
  certificates, the sharp six-moment metric transition, and the exact
  shallow raw-square reduction/Riccati analysis;
- the five compiler-local parameter-campaign directories in
  [mean-field peeling](../mean_field_peeling/quadratic_compiler/) retain their
  exact jets, compact certificates, source, tests, and a few tiny execution
  logs required by frozen provenance; the adjacent Campaign-6 directory
  preserves the inconclusive D13 audit at its lower claim level;
- [archive](archive/) contains superseded reports and frozen historical
  protocols retained for provenance.

Historical paths embedded in frozen manifests are preserved verbatim. They
record where a computation ran and are not current reproduction paths.

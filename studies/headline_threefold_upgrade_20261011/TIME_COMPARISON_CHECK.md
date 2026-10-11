# Scoped check of the same-time comparison windows

2026-10-11. Checked only `TIME_COMPARISON.md` and the complete
`paper/compact_fitting.tex`, as assigned. The source-width argument,
early-error construction, and endpoint theorem are imported hypotheses and
were not independently audited here. No proof, paper, or Git changes were
made. The rigorous-math and canonical-notation instructions were applied.

**Finding:** the deterministic near-zero and late-window arguments are
correct. Their stated probability applications retain their inherited
qualifications. They do not prove a comparison at every positive time. Two
minor wording/formal clarifications are listed at the end.

## Quantifiers and the sufficient dense hypothesis

The distinction between
\[
\frac{\sup_t E_n(t)}{\sup_t D_n(t)}
\quad\hbox{and}\quad
\sup_t\frac{E_n(t)}{D_n(t)}
\]
is essential and is correctly maintained. The former can be small despite a
small or zero denominator at another time. The proposed dense condition (2)
is sufficient provided the imported upper estimates have the asserted forms
\[
E_{{\rm Leg},n}(t)\le
\frac{CY\min(t,1)}{\sqrt n[\log(en)]^3},\qquad
E_{{\rm sel},n}(t)\le\frac{CY\min(t,1)}n.
\]
Division on the intersected events gives exactly the two ratios written in
the note. The confidence-dependent constant \(c_\delta\) must remain
fixed as width grows. For each fixed ratio tolerance, first take width to
infinity with fixed failure budgets, then let the budgets decrease to zero.
A union bound suffices; independence is unnecessary.

On a training-only fitted panel, both dense endpoint predictions equal the
label vector, so \(D_n(\infty)=0\). Thus hypothesis (2) is indeed false
there. This observation alone does not establish another asymptotic ratio
under a convention that omits or redefines zero denominators; the note
appropriately leaves the separately discussed scope question outside these
sufficient-window lemmas.

## Near-zero analytic estimate

For the Bernstein ellipse of parameter two over \([0,r]\), the center is
\(r/2\), the real semiaxis is \(5r/8\), and the imaginary semiaxis is
\(3r/8\). If \(0\le s\le r/16\), the disk of radius \(r/16\)
about \(s\) lies in
\([-r/16,r/8]\times[-r/16,r/16]\). Throughout that rectangle,
\[
\frac{(\operatorname{Re}z-r/2)^2}{(5r/8)^2}
+\frac{(\operatorname{Im}z)^2}{(3r/8)^2}
\le(9/10)^2+(1/6)^2<1.
\]
The claimed disk containment therefore holds with strict margin. Cauchy's
formula gives
\[
|g''(s)|\le\frac{2!M}{(r/16)^2}=\frac{512M}{r^2}.
\]
For \(0\le t\le r/16\), the integral remainder gives
\[
|g(t)-tg'(0)|\le\frac{256Mt^2}{r^2}.
\]
When \(|g'(0)|\ge a/\sqrt n\) and
\(t\le ar^2/(512M\sqrt n)\), the last quantity is at most
\(at/(2\sqrt n)\). This proves exactly (3), at every time in that
interval. Reality of \(g\) on the real axis is not needed for this
absolute-value argument.

At separately fixed positive problem parameters and confidence, the displayed
substitution (4) has constant \(a,M,u>0\) and
\(r\asymp[\log(en)]^{-1/2}\). Thus its smaller window endpoint is
eventually of order \(1/(\sqrt n\log(en))\), as claimed. On the
imported early-error event, division by \(at/(2\sqrt n)\) gives the
stated ratio bounds.

The values of \(a\) in the initial-derivative event, the rectangle size
in (4), and their confidence/width guarantees were not inputs to this
bounded check. The note explicitly conditions this application on the
source verification in `WIDTH_UPGRADE.md`, which is the correct claim
level. The uniform ellipse bound over all training coordinates would
indeed allow a data-dependent coordinate chosen on the derivative event
without a further union bound. This implication does not itself prove that
the imported event has that uniformity.

## Late-time comparison and the exact fitting constants

The fitting lemma gives, on its initialization event,
\[
\rho(t):=\|r(t)\|_2/\sqrt m\le Ye^{-\gamma t/(2m)},
\qquad
\|f_n(\infty)-f_n(t)\|_\infty
\le C(m/\gamma)\rho(t),
\]
uniformly on the sphere. Therefore the note correctly takes
\(k=\gamma/(2m)\) and \(B=C(m/\gamma)Y\). The same conclusion
holds for the independent initialization on its own fitting event. A union
bound combines the two fitting events with any endpoint lower event.

Writing the dense-run difference as the endpoint difference plus the two
tails proves
\[
D_n(t)\ge D_n(\infty)-2Be^{-kt}
\ge c/\sqrt n-2Be^{-kt}.
\]
This reverse-triangle estimate also holds when the endpoint lower bound
and both tails are supplied at one fixed query in the domain. The threshold
\(t\ge k^{-1}\log(4B\sqrt n/c)\) makes the subtracted tail at most
\(c/(2\sqrt n)\), proving (5)--(6).

At \(t\ge(2m/\gamma)\log(en)\), the tail is at most \(B/(en)\).
An explicit sufficient extra scalar gate is
\[
n\ge\max\{1,[4B/(ec)]^2\}.
\]
This gate validates the note's convenient late window (7). It does not
quantify the probability onset of the imported endpoint event. Dividing
the current global numerator bounds by \(c/(2\sqrt n)\) gives
\(O([\log(en)]^{-3})\) for Legendre and \(O(n^{-1/2})\) for the
selected models, with the stated fixed-problem/confidence coefficients.

The note retains the endpoint input's orthogonal-query geometry, layerwise
nonaffinity, positive problem-dependent constant, and unquantified width.
No conclusion in its late-window application removes those restrictions.
The endpoint input itself was outside this check's reading scope; this
report does not certify its theorem or citation beyond the stated conditional
use.

## Residual scope and minor clarifications

The shrinking near-zero window and the logarithmically late window leave
an uncontrolled interval. Neither analytic continuation nor separate
fixed-time lower bounds fills that interval. The note explicitly says this
and does not claim the full requested upgrade.

For a fully self-contained formal statement, equation (1) should specify what
happens when \(D_n(t)=0\), including \(0/0\) at a fitted training-only
panel. Adopting the paper's failure convention would make that unambiguous.
The proved window events have strictly positive denominators, so their
proofs are unaffected by this clarification.

The phrase “established endpoint-study input” is better read as “imported
endpoint-study result.” The latter avoids suggesting that an unpromoted
study theorem is maintained-book material. This is a status-language
clarification, not a defect in the conditional stitching argument.

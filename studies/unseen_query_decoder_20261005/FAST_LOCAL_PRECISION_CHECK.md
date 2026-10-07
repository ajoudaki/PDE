# Independent check of finite-tape metric replay

2026-10-06. Bounded independent reconstruction of Sections 1–4 of
`FAST_LOCAL_PRECISION_TEST.md`. The remaining sections were read as
supplied context; no full-decoder verdict is given. No experiment, Git
operation, maintained edit, or other-study input. Only this report is
written; the preceding fast-query check remains unchanged.

## Inputs, correction, and verdict

The complete original target was read at SHA-256
`7ddc3ab8ecc94d1ed39e54ae158451432a0293f7db1dea86b6c2fa8a9d6ed705`.
The sole scientific dependency read was the complete
`SANE_METRIC_PACKETS.md`, SHA-256
`1683563689c824593613cb636590ae3180f4cc897913c8ed5acb3c12170adeea`.
Shared instructions and the current required research, rigorous-proof,
and canonical-notation skills, including the neural reference, were
applied. No history, review report, or unassigned scientific source was
opened for this check.

The original had one minor wording error in Section 4: there is no
smallest positive dyadic grid step satisfying an upper bound. Its intended
choice is the coarsest dyadic step satisfying (6), equivalently the
smallest sufficient bit precision. The supervisor changed precisely that
phrase. The corrected passage was read and its hash verified:
`af2a238a3ea1ed73059fd61321ca8408ce487399542156dc44e5e06f5a3e2f91`.
This resolves the finding without changing a proof or resource order.

**Verdict for the corrected target: PASS for the stated finite-tape
replay lemma and its conditional resource consequences.** No unresolved
finding remains in Sections 1–4. In particular, local precision of the
underlying source and evaluator remains an explicit premise, not a
conclusion. The boundary lemma does not supply the later posterior,
physical-source, or whole-decoder transfers.

## Adaptive Gaussian boundary estimate

Let \(f\) be the density of \(a+\eta E\), where
\(E\sim N(0,1)\), and let \(h>0\). Its derivative satisfies

\[
 \int_{\mathbb R}|f'(x)|\,dx
 =\frac{\sqrt{2/\pi}}{\eta}\le\eta^{-1}.
\]

On each interval \([s+kh,s+(k+1)h]\), the fundamental theorem of
calculus bounds its left-endpoint density by the density at any point
plus the integral of \(|f'|\) on that interval. Integrating and
summing gives

\[
 \sum_{k\in\mathbb Z}f(s+kh)
 \le h^{-1}+\eta^{-1}.
\]

For \(v\le h/2\), the boundary neighborhoods are disjoint apart
from endpoints. Integrating the displayed periodic density over
\([-v,v]\), with the half-grid offset, proves (4). The bound is
uniform in the mean \(a\).

For update \(r\), condition on the full finite root array and the
preceding scalar marks. The deterministic evaluator and already rounded
prefix make \(A_r\) measurable, while \(E_r\) remains independent
standard Gaussian by the finite-source hypotheses. Therefore the same
bound applies even though the prior rounded decisions depend arbitrarily
on earlier noise.

With \(P\ge1\),
\(\zeta=\delta_{\rm acq}h/(64P)\) gives
\(4\zeta\le h/2\). Since \(h\le\eta\), each boundary
event has probability at most

\[
 8\zeta(h^{-1}+\eta^{-1})
 \le16\zeta/h=\delta_{\rm acq}/(4P).
\]

Their union costs \(\delta_{\rm acq}/4\). No independence of
different boundary events is needed. The case of no acquisitions is
vacuous and needs neither this choice of \(\zeta\) nor a replay
argument.

## Exact metric identity and source-dependent selection

Let \(V\) be the completed finite field table, including its constant
column. Choose independent columns and an invertible selected row block
\(H\). The coefficient matrix
\(V[:,J]H^{-1}\) reconstructs every column from its selected values;
its selected rows are the identity. Its Gram divided by \(n\) gives
the positive metric \(M\) and the exact identity

\[
 V^TV/n=V[I,:]^T M V[I,:].
\]

The determinant-improvement construction in the supplied metric note
ensures \(|M_{ab}|\le4\). Thus (2) holds for every pair on the
completed source tape. Exact pair products and rational division by
\(n\), as required by the target, are essential to this identity.
There is no assertion that it holds at a different prefix.

For symmetric entrywise rounding error at most \(\epsilon_M\),
the error operator norm is at most \(q\epsilon_M\). Adding
\(q\epsilon_M I\) therefore gives the PSD-safe metric and

\[
 \|\widehat M-M\|_{\rm op}\le2q\epsilon_M,
 \qquad
 |u^T(\widehat M-M)v|
 \le2q^2B^2\epsilon_M\le\zeta.
\]

This bound holds for every selected pair of vectors with the stated cap.
It does not require the metric, its rank, or the selected row indices to
be independent of any scalar noise.

Intersect the boundary event with the sampler coupling event (5).
Their complement has probability at most
\(\delta_{\rm acq}/4+\delta_{\rm acq}/2\).
On this intersection, induction starts at the empty prefix. If prefixes
coincide through update \(r-1\), copying the finite packets and using
the same deterministic evaluator gives bit-for-bit identical selected
field values at update \(r\). Relative to
\(X_r=A_r+\eta E_r\), the source pre-rounding value differs by at
most \(\zeta\). The compact value differs by at most
\(\zeta\) from metric rounding, \(\zeta\) from finite noise,
and an optional \(\zeta\) from arithmetic. Both are within
\(3\zeta\) of a shadow value more than \(4\zeta\) from every
boundary. They occupy the same rounding cell and yield identical scalars.
This closes the induction with probability at least
\(1-3\delta_{\rm acq}/4\ge1-\delta_{\rm acq}\).

The boundary probability was bounded before selecting or conditioning on
the metric. Conditioning on that completed-source metric would generally
destroy the fresh-Gaussian argument; the proof does not do so. It instead
uses a uniform deterministic perturbation bound after the source event
has been defined. No off-tape Lipschitz estimate, accumulated sensitivity,
or smallest-eigenvalue bound is required for the replay conclusion.

## Finite scalar noise can realize the required coupling

The Gaussian sampler reference cited in Section 4 was outside this
assignment and was not fetched. Its needed local conclusion can be
reconstructed directly as follows, so it is not a missing scientific
input to the present lemma.

Put \(\rho=\zeta/\eta\). Generate independent uniform cell indices
using \(b\) unbiased bits per mark. A proof-only independent uniform
position within each cell makes an exact uniform variable \(U\), and
\(E=\Phi^{-1}(U)\) is standard Gaussian. Let \(u\) be the cell
midpoint. The actual sampler evaluates the clipped inverse CDF at \(u\)
to error at most \(\rho/2\), producing a finite dyadic mark.
Conversely, the cell index is a function of \(E\), so this coupling
has exactly the dependence permitted by hypothesis 3. No continuous
Gaussian is an algorithm input.

Choose a finite certified cutoff with
\(T_E^2\ge2\log(8P/\delta_{\rm acq})\), comparable to that
quantity. The union of exact Gaussian tails has probability at most

\[
 2P e^{-T_E^2/2}\le\delta_{\rm acq}/4.
\]

The clipped inverse CDF is globally Lipschitz with constant at most
\(\sqrt{2\pi}e^{T_E^2/2}\); it is constant outside its interior
quantile interval. On \(|E|\le T_E\), midpoint coupling therefore
has error at most
\(\sqrt{2\pi}e^{T_E^2/2}2^{-b}\). Choosing this below
\(\rho/2\), and adding quantile-evaluation error, proves (5) with
failure no larger than \(\delta_{\rm acq}/4\), within its allowance.
Thus

\[
 b=O(T_E^2+\log\rho^{-1}),\qquad
 \log_2\rho^{-1}
 =\log_2(\eta/h)+\log_2(64P/\delta_{\rm acq}).
\]

This verifies the random-bit and stored-mark precision claims separately.
The latter also needs the cutoff's integer-part bits, as the target states.

A finite CDF algorithm needs no quantile table. Integrate the Taylor
polynomial for \(e^{-x^2/2}\) on the bounded interval. Taking
\(O(T_E^2+k)\) terms suffices for absolute CDF error \(2^{-k}\):
the exponential-series remainder is bounded by the first omitted
factorial term once the order is a sufficiently large multiple of
\(T_E^2+k\). The same order of guard bits controls large intermediate
terms. Take \(k=O(T_E^2+\log\rho^{-1})\), so the positive lower
Gaussian density converts CDF uncertainty to coordinate error below
\(\rho\). Certified bisection then terminates without deciding
transcendental equality. Elementary fixed-precision series arithmetic
and bisection give polynomial work and scratch in this word allowance;
in particular an \(O(w_E^4)\)-work, \(O(w_E)\)-scratch scalar
schedule is sufficient for
\(w_E=O(T_E^2+\log\rho^{-1})\).
All \(P\) marks therefore have an additional
\(O(Pw_E^4)\) sampling allowance, part of source generation rather
than the metric-selection work stated in Section 4.

## Precision, retained space, and metric setup

With the corrected coarsest-step rule, one can take

\[
 b_M=\left\lceil
 \log_2\frac{2q^2B^2}{\zeta}\right\rceil.
\]

Expanding \(\zeta\) yields (9) up to a universal additive constant.
The compensation \(q\epsilon_M\) is small under (6), so metric
entry integer parts remain bounded by a constant. No inverse of \(M\)
is executed during replay, and no spectral gap enters \(b_M\).

Multiplying two \(p_f\)-fractional-bit fields and one metric entry,
then summing \(q^2\) terms, requires
\(O(2p_f+b_M+\log(q+2)+\log(B+2))\) bits. The scaled-noise
representation and exact outer grid rounding must use their declared
finite word allowances. In the empirical source, the exact sum and its
denominator \(n\) require another \(O(\log(n+2))\) bits. No
denominator from an earlier acquisition survives through the outer scalar
rounding: every retained scalar is again a multiple of the fixed grid.

The local-precision premise must be read as a complete word allowance,
including actual representations of \(h\), \(\eta\), packets,
field outputs, coefficients, and scalar values. Magnitude bounds on
\(\log h^{-1}\) and \(\log\eta^{-1}\) alone would not bound
the exact description lengths of arbitrary dyadic inputs. The target
already assumes a locally precise finite source and evaluator; its setup
paragraph additionally includes \(\log n\) in the table allowance.
Under these stated premises, all required words are \(O(p_{\rm loc})\).

There are \(qD\) selected packet entries, \(q^2\) metric entries,
\(P\) scalar marks, at most \(P\) current/past scalar values, and
\(O(R^2)\) coefficient/template entries. With
\(q,D=O(R)\), \(P=O(R^2)\), their sum gives
\(O(R^2p_{\rm loc})\) retained bits. Evaluator descriptions and
workspace, query seeds, and median arrays are correctly left as explicit
additional costs.

For the table construction, let
\(b=2+p_f+\lceil\log_2(B+2)\rceil+
\lceil\log_2(n+s+2)\rceil=O(p_{\rm loc})\), where
\(s=O(R)\) is its field count. The supplied metric construction
uses \(O(sb)\)-bit exact minors, \(O(sb)\) determinant-improvement
swaps, and row scans of bounded finite integers. Its established counts
\(O(ns^5b^3)\) work and
\(O(n(s+D)b+s^3b)\) peak bits therefore become

\[
 O(nR^5p_{\rm loc}^3),\qquad
 O(nRp_{\rm loc}+R^3p_{\rm loc}).
\]

The exact metric entries temporarily have \(O(Rp_{\rm loc})\)
bits, and its expanded square arrays account for the cubic scratch term.
Rounding to (9) discards those expanded entries. Source generation,
sampler work, and later decoder storage remain outside this metric-only
setup bound, as stated. Exact bilinear replay itself can be performed in
\(O(q^2p_{\rm loc}^2)\) bit operations per acquisition, in addition
to the supplied row/coefficient evaluations; no unit-cost matrix operation
is needed.

The final \(Z^6\) remark is correct conditional exponent arithmetic:
\(R=O(Z^{5/2})\) and \(p_{\rm loc}=O(Z)\) give
\(R^2p_{\rm loc}=O(Z^6)\). The unassigned scientific derivation of
those envelopes and the full source/decoder precision premise were not
checked. Sections 5–7 identify further transfers, which this report neither
certifies nor uses to infer a complete neural compression theorem.

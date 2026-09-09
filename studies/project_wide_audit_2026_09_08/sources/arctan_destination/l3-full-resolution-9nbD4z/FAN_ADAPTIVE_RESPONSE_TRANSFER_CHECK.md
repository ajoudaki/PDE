# Adaptive Langevin response: exact transfer check, no closure

Status: NO_CANONICAL_PROGRESS. This is a source-mechanism check, not
a new response theorem, a review of the whole paper, or a negative
resolution of the canonical problem. No numerical experiment was performed.

The primary source is Fan, Ko, Loureiro, Lu and Shen,
[arXiv:2504.15556v1](https://arxiv.org/pdf/2504.15556v1), dated
22 April 2025. This check pins that version, rather than an uninspected
later revision. In addition to the displayed model and assumptions,
the argument of Lemma 5.6, equations (159)--(169), was inspected.

## The source step being tested

The source's main particle Jacobian is
\[
J_1=-\beta X^T X+\operatorname{diag}(\partial_\theta s).
\]
Assumption 2.2 bounds the coordinate drift derivatives. Lemma 5.6
uses the block estimates
\[
\|J_1\|_{\rm op},\ \|J_4\|_{\rm F}\le C,\qquad
\|J_2\|_{\rm F}\le C\sqrt d,\qquad
\|J_3\|_{\rm F}\le C/\sqrt d.
\]
Its two response blocks then obey
\[
U'=J_1U+J_2W,\qquad W'=J_3U+J_4W.
\]
The balanced quantity \(\|U\|_{\rm op}+\sqrt d\|W\|_{\rm F}\)
has a closed Gronwall bound. The discrete analogue has a factor
\(1+C\gamma\) per step, giving mesh-uniform control on each finite
horizon. Thus this part of the proof uses coefficient bounds before
passing to the continuous-time response; covariance matching alone
does not supply them. See the proof of (163)--(165), and the derivative
continuity estimate (166). The source's displayed diffusion is noisy;
no noiseless DMFT theorem is inferred here.

## The unchanged canonical term

Use the precise canonical setup in CONTRACT_AND_LEDGER.md, including
the independent Gaussian hidden matrices, readout variance \(n^{-2}\),
and every trained block. In feature time let a dot below mean an
initial-data variation, not a time derivative. Direct differentiation
of
\[
q^{(2)}=(W^{(3)})^T\delta^{(3)},\qquad
\delta^{(2)}=\phi'(z^{(2)})\odot q^{(2)}
\]
gives
\[
\dot q^{(2)}=(\dot W^{(3)})^T\delta^{(3)}
 +(W^{(3)})^T\dot\delta^{(3)},
\]
\[
\dot\delta^{(2)}
=\phi'(z^{(2)})\odot\dot q^{(2)}
 +[\phi''(z^{(2)})\odot q^{(2)}]\odot\dot z^{(2)}.
\tag{1}
\]
The full upper variation and lower forward variation remain present;
none is held fixed. A diagonal multiplication operator on vectors
measured by \(\|v\|_2/\sqrt n\) has operator norm equal to the maximum
absolute diagonal entry: the upper bound follows by summing squares,
and a vector supported on a maximizing coordinate attains equality.
Consequently the coefficient in the last term of (1) has norm
\[
\max_i|\phi''(z_i^{(2)})q_i^{(2)}|.
\tag{2}
\]
The established RMS query bound does not prove a uniform bound for
(2). In the actual transformed-state calculation of
ACTUAL_BULK_GAUSSIAN_TANGENT_ENERGY.md, this is precisely the retained
middle multiplication operator between bounded state maps. The
canonical normalization is already accounted for; balancing blocks
does not establish its missing estimate.

For a fixed smooth clipping, (1) instead has
\(\phi'(z^{(2)})\tau'(q^{(2)})\dot q^{(2)}\) and
\(\phi''(z^{(2)})\tau(q^{(2)})\dot z^{(2)}\).
The bound on the second coefficient grows with its cap. This is not
the cap-independent estimate required for uncut continuation.

The separate signed Gaussian-probe energy remains a legitimate
alternative to a full operator bound, but this source step has not
estimated that energy. No assertion is made that every possible
embedding or extension of the source method is impossible. Reopen
this specific transfer only with a new, actually verified canonical
coefficient or response estimate, not the source's conclusion alone.

## Internal provenance

ACTUAL_BULK_GAUSSIAN_TANGENT_ENERGY.md and
ACTUAL_BACKPROP_PRIMITIVE_RESPONSE.md specify the already established
actual variations and signed-energy gap. The current route registry
has hash 1091aa57ee26642b9eeef86d9d9b041584e477a8742dbb58183b2135673862d6
before this check is recorded. No certified internal proof is changed.

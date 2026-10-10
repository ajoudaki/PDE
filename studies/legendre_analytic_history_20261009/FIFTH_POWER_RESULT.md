# The one-tenth boundary for the unchanged Legendre method

Date: 2026-10-10. Status: proved and internally checked, not promoted.
Root reconstructed the calculation. A fresh scoped full-chain audit,
[FIFTH_POWER_AUDIT.md](FIFTH_POWER_AUDIT.md), passed both the prediction
lower bound and the tight dense upper bound. A separate nonauthor check,
[FIFTH_POWER_TRANSFER_CHECK.md](FIFTH_POWER_TRANSFER_CHECK.md), passed
the prediction transfer; its context was reused and it did not re-audit
the dense upper bound. The scalar component also has the separate
[CROSS_TAIL_CHECK.md](CROSS_TAIL_CHECK.md). Source hashes and exact review
scopes are in those reports. No paper, experiment, or implementation
is changed.

## The question and the precise answer

The user asks whether \(q<n^{1/10}\) suffices for the original Legendre
method at dense-variability accuracy. The method is kept exactly as in
the current paper: residual-RMS clock starting at one, constant forward
prefix, zero backward prefix, original reconstruction, and original
training equations. No data-adapted basis or extra stored coordinates
are introduced.

The previous \(cq^{-10}\) obstruction was not sharp. The refined
analysis gives \(cq^{-5}\) for actual predictions, uniformly in width
and order, on a fixed positive training-time interval. On an admissible
identity-activation problem, this rules out every \(q=o(n^{1/10})\)
for even constant-factor comparison with independent dense variability.
It also rules out \(q=O(n^{1/10})\) for error negligible relative to
that variability.

There is an important literal boundary distinction. An order
\(q=c_0n^{1/10}\) with a small fixed \(c_0>0\) is numerically less
than \(n^{1/10}\), but is not \(o(n^{1/10})\). The present result
does not rule out constant-factor accuracy for such an order, nor prove
its sufficiency. It does rule out a strictly smaller width exponent,
and it rules out that boundary scale for the paper's stronger vanishing
relative-error guarantee.

## Precise statements

Take \(m=d=L=2\), both activations equal to the identity, normalized
training inputs \(v_1=e_1,v_2=e_2\), and fixed nonzero labels satisfying
the paper's original small-label cap. Then the population feature Gram
is \(I_2\), so \(\gamma=1\). Identity activations satisfy the given
strip-analytic assumptions, including bounded derivatives and permitted
unbounded values. This is a counterexample within the full scope, not a
new restriction on a positive theorem.

For this fixed problem, there are constants \(c>0\), \(q_0<\infty\),
and \(0<t_1<t_2<\infty\), independent of \(n,q\), such that on the
common initialization event,

\[
 \sup_{t\in[t_1,t_2]}\max_{a=1,2}
 |f_{\rm Leg}(t,x_a)-f_n(t,x_a)|\ge c q^{-5}
 \qquad(q\ge q_0).
 \tag{1}
\]

The event has probability tending to one and supports all finite orders
simultaneously. The constants may depend strongly on the fixed labels
but do not change as width or order grows. The earlier uniform onset
bound handles the finitely many smaller orders, so decreasing \(c\)
gives \(\|f_{\rm Leg}-f_n\|_*\ge cq^{-5}\) for every \(q\ge1\);
the fixed interval in (1) is only asserted for \(q\ge q_0\).
Here \(\|\cdot\|_*\) means all physical times, including the fitted
endpoint, and the whole input sphere.

For two independent dense initializations on the same fixed problem,

\[
 \|f_n-\widetilde f_n\|_*=O_{\mathbb P}(n^{-1/2}).
 \tag{2}
\]

The precise meaning of (2) is that for every \(\delta>0\), some finite
\(C_\delta\) bounds this discrepancy by \(C_\delta/\sqrt n\) with
probability at least \(1-\delta\), at each sufficiently large
individual width. The width threshold is not asserted explicit or
polynomial. There is no logarithmic factor hidden in (2).

Together, (1)--(2) imply for every deterministic \(q(n)=o(n^{1/10})\)
and every fixed \(K>0\),

\[
 \Pr\!\left\{
 \|f_{\rm Leg}-f_n\|_*
 \le K\|f_n-\widetilde f_n\|_*
 \right\}\longrightarrow0.
 \tag{3}
\]

For the stronger paper contract
\(\|f_{\rm Leg}-f_n\|_*/\|f_n-\widetilde f_n\|_*
\longrightarrow0\) in probability, a necessary condition is

\[
 \frac{q(n)}{n^{1/10}}\longrightarrow\infty.
 \tag{4}
\]

Neither (3) nor (4) asserts a sufficient order. The existing general
sufficient bound remains \(n^{1/4+o(1)}\). The sharp sufficient exponent
between these bounds is not determined here.

## Proof architecture and dependencies

The complete proof of (1) is [SHARPER_OBSTRUCTION_ROUTE.md](SHARPER_OBSTRUCTION_ROUTE.md),
supported by the explicit scalar algebra in
[CROSS_TAIL_IDENTITIES.md](CROSS_TAIL_IDENTITIES.md). It uses the current
paper's initialization/fitting statement and exact Legendre equations,
not the dense complex-time source theorem.

First, the accumulated hidden-weight defect is exactly the pairing of
the discarded backward and forward histories. Near the prefix join,
the backward history begins linearly and the changed forward history
quadratically. The pairing of these two truncated powers has an exact
formula involving two adjacent Legendre moments. Its surviving
oscillation has size \(q^{-5}\). Terms of the same order from higher
jets contribute a smooth background, not that oscillation.

Second, only the dense histories are differentiated. Their high
derivatives are bounded uniformly in width on a fixed short interval,
because the scaled identity-network vector field is polynomial and
the residual stays away from zero there. Uniform Legendre estimates
include the initial shrinking boundary layer. An integral comparison
then transfers the dense-history source estimate to the actual
order-dependent closure without bounding its high derivatives.

Third, the proof follows the induced changes in the first layer,
readout, and clock. At the same physical time, the prediction error is
an explicit \(q^{-5}\) oscillation with nonzero coefficient, plus a
background whose derivative is \(O(q^{-5})\), plus \(o(q^{-5})\).
Two clock values separated by \(O(q^{-1})\) have opposite phases.
The smooth background cannot cancel the oscillation at both, proving
(1) for actual predictions. This is not an inference from a parameter
norm or from the mere lack of history smoothness.

The proof of (2) is [IDENTITY_DENSE_UPPER.md](IDENTITY_DENSE_UPPER.md).
It starts with the same current-paper dense fitting event. On that event
the prediction Hessian in the scaled parameter coordinates is
width-independent. Signed stability and residual damping show that each
prediction velocity has initialization Lipschitz constant at most
\(C(1+t)e^{-t/4}/\sqrt n\). Scalar Lipschitz extensions allow an
unconditioned Gaussian variance estimate. Integrating it over time
proves (2), avoiding a time net and its logarithmic loss. The extension's
joint measurability and the Gaussian inequality are proved in that note.

## Deriving the relative-error conclusions

Fix \(\delta>0\) and intersect the events of (1) and (2). Their
probability has limiting inferior at least \(1-\delta\); no independence
between these two events is needed. On that intersection, whenever the
dense denominator is positive, the ratio is at least

\[
 \frac{c\sqrt n}{C_\delta q(n)^5}.
\]

For \(q(n)=o(n^{1/10})\) this tends to infinity. Thus the probability
in (3) has limiting superior at most \(\delta\), and letting
\(\delta\) be arbitrarily small proves (3). A zero denominator also
cannot satisfy the desired comparison because the numerator is positive.

If (4) fails, some infinite subsequence satisfies
\(q(n)\le Bn^{1/10}\) for a finite fixed \(B>0\). Choose, for example,
\(\delta=1/4\). Along that subsequence the ratio is at least the
positive constant \(c/(C_{1/4}B^5)\) with limiting probability at least
\(3/4\), contradicting convergence to zero in probability. This proves
(4). The constants in this argument are for the one fixed admissible
problem; it does not take labels to zero with width.

For the particular stronger absolute certificate displayed in the
paper,

\[
 \|f_{\rm Leg}-f_n\|_*\le
 \frac{CY}{\sqrt n[\log(en)]^3},
\]

(1) instead gives the more explicit necessary order

\[
 q\ge c_{\rm problem}\,
 n^{1/10}[\log(en)]^{3/5}.
\]

That logarithm belongs to this particular absolute target, not to
the general necessary condition (4).

## Storage and scope

The exact learned-state count in this example is \(3n+1+4nq\), with
an additional fixed \(n^2\) mixer. Therefore a learned-state count
\(o(n^{11/10})\) cannot achieve even constant-factor dense-variability
accuracy for the unchanged method over the full original scope.
For negligible relative error, a necessary count is
\(\omega(n^{11/10})\). These are necessary counts on this example,
not universal sufficient counts or an optimality theorem.

The obstruction is transient. Both fitted predictors in this example
agree on the whole sphere, because they are linear in the input and
fit the two basis inputs with the same labels. It does not refute good
finite-width experiments, endpoint agreement, or a nonlinear-only
theorem restricted to activations such as tanh. The constant can be
extremely small under the sufficient label cap.

The upper-route note [SHARPER_UPPER_ROUTE.md](SHARPER_UPPER_ROUTE.md)
also proves a useful new stability lemma: the supremum of the signed
defect primitive can replace the integral of its absolute magnitude,
with controlled finite-horizon cost and an all-time tail argument. It
does not prove a general sufficient error rate better than the existing
one. Keeping this positive lemma separate from the counterexample avoids
confusing a sharper proof tool with a completed improved compression
guarantee.

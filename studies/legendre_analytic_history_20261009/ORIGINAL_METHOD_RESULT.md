# The unchanged residual-clock Legendre method: a prediction obstruction

The later [FIFTH_POWER_RESULT.md](FIFTH_POWER_RESULT.md) sharpens this
valid \(q^{-10}\) lower bound to \(q^{-5}\) and removes logarithmic
loss from the identity example's dense upper bound. That newer result
is authoritative for the strongest necessary order; this earlier proof
is retained as a valid simpler onset argument and finite-order check.

## Scope and current status

This result concerns exactly the first construction in
`paper/compact_legendre.tex`: the residual-RMS clock starts at one, the
forward history has a constant prefix, the backward history has a zero
prefix, and all original update and reconstruction equations are retained.
No data-adapted space, change of clock, replacement prefix, or tail switch
is allowed. The physical-time construction in `OBLIVIOUS_WINDOWS.md` is a
different method and is not used here.

The onset proof is complete in `ORIGINAL_OUTPUT_ANALYSIS.md` and passed
two separate scoped checks, `ORIGINAL_OUTPUT_REMAINDER_CHECK.md` and
`ORIGINAL_OUTPUT_COEFFICIENT_CHECK.md`. Both reconstructed its coefficient
and uniform remainder; the second also checked the actual dense-variability
implication. These were nonauthor checks with reused contexts, not fresh
isolated promotion reviews. Status: internally checked, not promoted.
The implication for actual independent dense-run variability is proved
below using the current paper's existing upper certificate. The
nonlinear-activation calculation in
`ORIGINAL_POSITIVE_ROUTE.md` has a different, explicitly incomplete status:
its coefficient is computed, but its uniform remainder is not proved.

## Result

The full-scope polylogarithmic claim is false for the unchanged method.
There is an admissible fixed problem with two hidden layers, two training
inputs in dimension two, identity activations, positive population Gram
gap, and fixed nonzero labels satisfying the original small-label cap, for
which the following holds. Let (q\ge1) be the Legendre order and (n)
the dense width. There are positive constants (c,\eta), depending only
on this fixed problem and not on (n,q), such that with probability
tending to one, simultaneously for every finite order,

\[
\sup_{\|x\|=\sqrt2}
 |f_{\rm Leg}(\eta/q^2,x)-f_n(\eta/q^2,x)|\ge c q^{-10}.
\tag{1}
\]

Here the dense reference and the Legendre model have the same realized
initialization. This is a difference between actual trained predictions,
not merely a lower bound on approximating a history. Identity activations
are holomorphic with bounded derivatives on every fixed strip; the paper
does not require nonaffinity or bounded activation values. Thus this
example is within its stated scope, although it is not a tanh example.

Write (\|\cdot\|_*) for the supremum over this input sphere and all
physical times, including the fitted endpoint. Let \(\widetilde f_n\)
be an independent ordinary dense run. For every deterministic
\(q(n)=n^{o(1)}\), and every fixed comparison factor \(K>0\),

\[
\Pr\!\left(
 \|f_{\rm Leg}-f_n\|_*
 \le K\|f_n-\widetilde f_n\|_*
\right)\longrightarrow0.
\tag{2}
\]

In particular, no fixed polylogarithmic order proves even constant-factor
comparison with actual dense-run variability over the original full
scope. This does not claim that the older sufficient order
\(n^{1/4+o(1)}\) is necessary or optimal. The present necessary order
is only \(n^{1/20-o(1)}\) on this example.

## Why the residual clock does not cure this particular onset

At initialization the residual RMS is the fixed positive label scale
\(Y\). Therefore
\(\tau(t)=1+Yt+O(t^2)\): the residual clock is a regular change of time
near zero. It does not smooth the artificial join at \(\tau=1\).
The backward response begins linearly after its zero prefix; the forward
response begins quadratically after its constant prefix. Their first
unmatched derivatives survive that regular change of time.

The exact forcing error in the reconstructed hidden matrix is the product
of the two endpoint projection errors. Consequently it starts at order
\(t^3\), the hidden weight error starts at order \(t^4\), and the
prediction error starts at order \(t^5\), since the readout also starts
at zero. The induced readout error has the same sign as the direct hidden
weight contribution: it does not cancel it.

The endpoint Legendre kernel has absolute value at most \(q^2/\tau\).
On an active interval of physical length proportional to \(q^{-2}\),
its projection cannot remove the leading onset terms. The full proof
controls the actual nonlinear parameter evolution uniformly on that
interval, rather than making a fixed-order Taylor expansion and then
silently allowing the order to grow.

For completeness, in the proof's local normalization put
\(A_0=W_0^{(1)}/\sqrt n\), \(B_0=W_0^{(2)}\), and
\(G=A_0^\top B_0^\top B_0A_0\). For the vector of the two training
predictions the exact estimate is

\[
 f_{\rm Leg}(t)-f_n(t)
 =-\frac3{20}\|y\|_2^2(y^\top Gy)Gy\,t^5+R_q(t),
 \qquad \|R_q(t)\|_2\le Cq^2t^6,
\tag{3}
\]

on \(0\le t\le\min(t_*,q^{-2})\). The constants \(C,t_*\) are
uniform in \(n,q\) on the common initialization/fitting event.
Since \(G\succeq I_2/2\) there with probability tending to one,
the fifth-order coefficient is bounded away from zero. A sufficiently
small fixed \(\eta\) makes the remainder less than half the leading
term at \(t=\eta/q^2\), proving (1). All normalizations, the exact
projection defect, and the uniform remainder are derived in
`ORIGINAL_OUTPUT_ANALYSIS.md`.

## Closing the comparison with actual dense variability

The lower bound on dense variability is not useful for disproving (2).
We instead use the upper certificate in the current paper:
`paper/integrated_appendix.tex`, label
`int:dense-forward-comparison`, with its signed-comparison and Gaussian
concentration proof. Its scope includes this identity-activation example.
The original fixed small-label cap is sufficient for its fitting and
source allowances.

For each fixed failure probability \(0<\delta<1\), that certificate
implies finite constants \(C_\delta,N_\delta\), independent of \(n,q\),
such that for \(n\ge N_\delta\), with probability at least
\(1-\delta\),

\[
 \|f_n-\widetilde f_n\|_*
 \le C_\delta\frac{\log(en)}{\sqrt n}
                 \exp\!\big(C_\delta\sqrt{\log(en)}\big).
\tag{4}
\]

This fixed-problem consequence follows directly from the exact
certificate: its carrier allowance is \(O(\sqrt{\log(en)})\), its
comparison exponent is affine in that allowance, its remaining comparison
coefficient is at most affine, and its input/time covering logarithm is
\(O_\delta(\log(en))\). No claim of a polynomial width threshold or
uniformly growing data is made. The larger constant inside the exponential
is harmless here because (4) is \(n^{-1/2+o(1)}\).

On the intersection of (1) and (4), their ratio is bounded below by

\[
 \frac{c\sqrt n}
 {C_\delta q^{10}\log(en)
       \exp(C_\delta\sqrt{\log(en)})}.
\]

For \(q=n^{o(1)}\) this diverges. Thus the probability in (2) has
limsup at most \(\delta\); since \(\delta\) was arbitrary, (2)
follows. No independence between the compression error and its coupled
dense reference is used. A zero dense denominator cannot make the desired
comparison hold, because the numerator is strictly positive on (1).

Likewise, if comparison within a fixed factor holds on this intersection,
then necessarily

\[
 q\ge c_{\delta,K}\,
 n^{1/20}[\log(en)]^{-1/10}
 \exp\!\big(-C_\delta\sqrt{\log(en)}/10\big)
 =n^{1/20-o(1)}\ \text{up to a fixed positive factor}.
\]

The unchanged method has exactly \(3n+1+4nq\) learned coordinates on
this problem, in addition to its fixed \(n^2\) mixer. Hence this
counterexample also prevents an \(n^{1+o(1)}\) learned-state guarantee
for the unchanged method over the full original scope. It does not exclude
better rates than the paper's existing sufficient bound.

## What this says about the experiments

The experiments can correctly show excellent polylogarithmic orders over
their tested widths and tolerances. They do not settle the uniform
continuous-trajectory, vanishing-tolerance asymptotic assertion above.
The obstruction is high order in both label size and early time, its
witness time shrinks with \(q\), and it is not an endpoint lower bound.
The theorem's label cap can make its coefficient extremely small.
In this particular counterexample both fitted predictors even agree
exactly on the whole sphere: they are linear in the input and fit the two
basis inputs with the same labels. The obstruction is entirely transient.
We have not re-run or audited the experiments in this theoretical task,
and do not claim this mechanism explains any particular plotted curve.

For tanh, `ORIGINAL_POSITIVE_ROUTE.md` computes a nonzero fifth-order
coefficient with a positive-magnitude infinite-width limit. Its remainder
has not been controlled uniformly for growing \(q,n\); that calculation
alone is not a tanh counterexample. Conversely, no polylogarithmic
guarantee for the unchanged tanh method has been proved here.

The previously checked physical-time, zero-prefix construction avoids the
specific prefix join and has a polylogarithmic sufficient order, but it
also changes the clock and tail handling. It remains a separate positive
result, not a proof about the method requested in this continuation.

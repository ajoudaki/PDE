# Relative moving-state complexity without a numerical width law

28 September 2026. Continuation of the same study. This note answers the
common-width comparison question and separates it from optimal complexity
at a prescribed accuracy. It uses the latest near-quadratic theorem, not
the superseded near-first-order envelope in DENSE_VS_CLOSURE_TEST_COMPLEXITY.md.
No manuscript or algorithm is changed.

## 1. A common sufficient width exists

Use exactly the small-label, Gaussian-initialization, zero-readout regime
and the whole-input/all-time prediction norm of
ACTIVATION_NEAR_QUADRATIC_ALLTIME.md. Write D_n for the dense prediction
error and H_n(q) for the actual order-q closure's error against the same
dense population predictor. The current theorem gives, on its common
initialization event,

\[
 D_n\le\eta_n,\qquad
 H_n(q)\le C\omega(q)+\eta_n,\qquad
 \omega(q)=q^{-2}e^{K\sqrt{\log(e+q)}},\qquad
 \eta_n\longrightarrow0\text{ in probability}.
 \tag{1}
\]

Here eta_n may be chosen as C_mu Phi(a_n)+D_n, as in the latest proof.
Its common-event failure probability tends to zero and is included below.
All data, depth, test law and confidence parameters are fixed.

For any epsilon,delta>0 choose q_epsilon so C omega(q_epsilon)<=epsilon/2.
There is N(epsilon,delta) such that, for every n>=N, the common event
and eta_n<=epsilon/2 hold together with probability at least 1-delta.
Both the dense and closure predictors then have error at most epsilon.

This is a common *sufficient* width certificate. It is not a theorem that
the smallest sufficient dense width also controls eta_n: the latter
includes a trained-carrier transfer remainder in addition to D_n.

The order can be chosen as

\[
 q_\varepsilon=\varepsilon^{-1/2}
                \exp[O(\sqrt{\log(1/\varepsilon)})].
 \tag{2}
\]

To see the scaling, put u=log q. The equation for its leading terms is
2u-K sqrt(u)=log(1/epsilon)+O(1); it has
u=(1/2)log(1/epsilon)+O(sqrt(log(1/epsilon))). Increasing its constant
makes (2) a sufficient integer order. No width rate is used in this step.

## 2. The exact relative state count

Exclude the fixed initialized hidden matrices, as specified in the
research contract. The two persistent moving-state counts are

\[
 M_D(n)=(L-1)n^2+n(d+1),\qquad
 M_H(n,q)=2(L-1)mnq+n(d+1)+O(1).
 \tag{3}
\]

Consequently their ratio is exactly, up to the constant-size clock state,

\[
 \frac{M_D(n)}{M_H(n,q)}
 =\frac{(L-1)n+d+1}
        {2(L-1)mq+d+1+O(1/n)}.
 \tag{4}
\]

For fixed m,d,L with L>=2 and q growing, this is asymptotic to n/(2mq).
Thus (1)--(4) give a proved comparison of two accurate implementations
at any common sufficient width. If n_epsilon=F(epsilon) denotes that
width, the gain is

\[
 \frac{F(\varepsilon)}{2m q_\varepsilon}
 =\frac{F(\varepsilon)}{2m}\,
   \varepsilon^{1/2}
   \exp[O(\sqrt{\log(1/\varepsilon)})].
 \tag{5}
\]

The sign and constant of the subpower factor in this asymptotic notation
are determined by the chosen sufficient order; the exact expression is
F/(2m q_epsilon). One factor F cancels, but one remains, because dense
state is quadratic and closure state is linear in width.

For illustration, if a common certificate had F(epsilon)=epsilon^-a+o(1),
then its sufficient state counts and their ratio would be

\[
 M_D=\varepsilon^{-2a+o(1)},\quad
 M_H=\varepsilon^{-(a+1/2)+o(1)},\quad
 M_D/M_H=\varepsilon^{-(a-1/2)+o(1)}.
 \tag{6}
\]

With root-width error, a=2: the costs would be epsilon^-4 and
epsilon^-5/2+o(1), and the gain would be epsilon^-3/2+o(1).
The exponent 5/2 is a closure *cost* exponent, not its improvement factor.
Equation (6) remains a conditional calculation; (4) is unconditional
accounting, combined with the actual common-width accuracy certificate.

No specified epsilon-power improvement follows merely from the existence
of F. A lower growth bound for a particular common sufficient width would
give a lower bound on the ratio of those two implementations. To claim
a gain over the best dense implementation additionally requires a lower
bound on its necessary width or state, not only two sufficient budgets.

It is possible to force any proposed ratio R(epsilon) by choosing
n>=max{N(epsilon,delta), C m q_epsilon R(epsilon)}. Then (1) and (4)
certify both accuracies and that ratio. This is a valid same-width
existence statement, but widening the dense benchmark this way does not
establish an optimal epsilon-complexity advantage.

## 3. A rate-free compression theorem

For every deterministic q_n->infinity with q_n=o(n), (1) proves
H_n(q_n)->0 in probability in the whole-input/all-time norm, while
(3) proves M_H/M_D->0 at fixed m,d,L. This is a genuine compression
theorem that requires no numerical width law. It does not assert that
the two errors have the same actual size at each n, or that the narrowest
accurate implementations attain those state counts.

## 4. What a direct closure width theorem would need

A direct route would establish a quantitative finite-to-population
comparison for the closure itself, rather than transfer the dense
trained-carrier remainder. If it yielded

\[
 \mathcal E(\widehat f_{n,q},f_\infty)
       \le C\omega(q)+\frac{A(q)}{\sqrt n}
 \tag{7}
\]

at fixed confidence uniformly over physical time, for widths including
the choices below, then (2) gives

\[
 n_\varepsilon=O(\varepsilon^{-2}A(q_\varepsilon)^2),\qquad
 M_H=O\bigl(Lm\varepsilon^{-5/2+o(1)}
                         A(q_\varepsilon)^2\bigr).
 \tag{8}
\]

Subpower A(q)=q^o(1) is sufficient for the requested exponent. A bound
holding only separately for each fixed q, with no control of A(q), is
not sufficient. If A(q)=O(q^b), the resulting sufficient moving-state
exponent is 5/2+b, up to subpower corrections.

If (7) is only valid for n>=N_0(q,delta), replace its displayed sufficient
width by max{N_0(q_epsilon,delta), C epsilon^-2 A(q_epsilon)^2}.
The threshold and failure probabilities must therefore also be controlled
along the increasing-order sequence. An unspecified fixed-q threshold
can invalidate the exponent even when A(q) is small.

One may instead first identify a unique fixed-q population predictor
f_infinity,q, prove its width rate, and combine it with the population
order estimate. Uniqueness of the full fixed-q population moment law
is not supplied by the current subsequential predictor-limit result.
The direct theorem must prove the needed identification or bypass it
by comparing directly with the dense population predictor as in (7).

The exact favorable moment-energy structure, and the remaining fixed
random-matrix interactions, are derived separately in
DIRECT_CLOSURE_WIDTH_ROUTE.md. They motivate this direct route without
claiming (7) has already been proved.

## Check and scope

The coordinator checked (1) against the current near-quadratic theorem,
then derived (2)--(8) explicitly. The source result's common-event and
in-probability quantifiers are retained. No numerical width rate,
necessary-width lower bound, optimality result, experiment, manuscript
edit, external search or Git mutation is asserted. The scoped author
of the companion note independently derived the moment-energy identity
and the A(q) accounting before exchanging findings with the coordinator;
this was an author check, not a blind review or promotion.

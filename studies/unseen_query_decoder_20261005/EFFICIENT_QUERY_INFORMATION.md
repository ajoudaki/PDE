# Information in the current prefix and the unresolved query stability estimate

2026-10-06. Scoped theoretical continuation. No experiment, promotion, or
change to the existing decoder theorem.

The low-information premise is correct, and it gives more than a typical-row
expectation estimate: one event controls conditional empirical averages of
every bounded row function at every retained prefix. This includes row
functions chosen using the current state and an arbitrary unseen input.
It does **not** presently give an efficient decoder. The supplied row
representation permits exponentially large moment-to-output sensitivity,
and its large global caps do not provide useful concentration scales for a
population query. A concrete bounded scalar-program example below shows
that low information and concentration of the exact output together do not
remove this obstruction.

## 1. Scope, target, and supplied objects

The target remains the original full-label nonlinear network, the whole
input sphere, every training time and the fitted endpoint, with error on
the inherited dense-versus-dense upper-certificate scale. A successful
decoder must use its present compressed state without dense-root access or
replaying the training scalar updates, and have runtime polynomial in its
polylogarithmic description and requested logarithmic numerical precision.
All retained storage and query workspace must have an absolute
polylogarithmic bound. This note does not weaken those requirements.

Only the following complete scientific inputs were read:

- `CURRENT_STATE_DECODER_CANDIDATE.md`;
- `NOISY_TWO_ORIENTATION_TRANSCRIPT.md`;
- `NOISY_SCALAR_HISTORY_ACQUISITION.md`;
- `PHYSICAL_NOISY_PROGRAM_BRIDGE.md`;
- `CONDITIONAL_PREFIX_CENTER.md`.

Their ideal scalar history has the form

\[
 C_r=\frac1n\sum_{i=1}^n F_r(Z_i;C_{<r})+\eta E_r,
 \qquad 1\le r\le P.                                      \tag{1}
\]

Here the packets \(Z_i\) are independent with common Gaussian law
\(\mu\), the \(E_r\) are independent standard Gaussians independent
of the packets, \(0<\eta\le1\), and \(|F_r|\le B\). The functions
are identical for every row, so the history is invariant under permuting
the packets. We use the source's prefix \(C_{\le j}\), not the selected
private packet panel or its weights, as conditioning information.

The source gives \(P\le C[\log(en)]^{16}\) and absolute-polynomial
bounds in \(\log(en)\) for \(\log B\) and \(\log(1/\eta)\).
The results below concern the ideal continuous history. Stability under
rounding must be proved for a replacement decoder; it is not supplied by
an information bound on that ideal history.

## 2. The information budget and its row consequence

Use natural logarithms and write \(D(\nu\Vert\lambda)\) for relative
entropy, with value infinity if \(\nu\) is not absolutely continuous
with respect to \(\lambda\). Define

\[
 H=\frac P2\log(1+B^2/\eta^2).                              \tag{2}
\]

Then

\[
 I(Z_1,\ldots,Z_n;C_{\le P})\le H.                          \tag{3}
\]

Indeed, conditional on an earlier prefix, the empirical mean in (1) lies
in \([-B,B]\), so the variance of the next noisy observation is at most
\(B^2+\eta^2\). A real variable of variance \(v\) has differential
entropy at most \(\frac12\log(2\pi e v)\): subtract its entropy
from that of the Gaussian with its mean and variance to obtain the
nonnegative relative entropy to that Gaussian. Conditional on all packets
and the preceding history, the remaining randomness of the next summary
is exactly \(\eta E_r\). Thus

\[
 \begin{aligned}
 I(Z_{1:n};C_r\mid C_{<r})
 &=h(C_r\mid C_{<r})-h(C_r\mid Z_{1:n},C_{<r})\\
 &\le\tfrac12\log[(B^2+\eta^2)/\eta^2].
 \end{aligned}
\]

Summing the conditional-information chain rule proves (3).
Consequently \(H\) is absolute-polylogarithmic in the supplied program.
Tiny scalar noise does not produce an inverse power of \(\eta\) in
this information bound.

For a prefix value \(c\), let \(\pi_{j,c}\) be the posterior of
\(Z_{1:n}\), and put

\[
 K_j(c)=D(\pi_{j,c}\Vert\mu^{\otimes n}).                   \tag{4}
\]

The Gaussian likelihood is positive. Its permutation invariance gives an
exchangeable posterior with common one-row marginal \(\pi^1_{j,c}\).
Whenever the entropy in (4) is finite, factoring the density against the
product of its own marginals gives the exact identity

\[
 K_j(c)=D\bigl(\pi_{j,c}\Vert(\pi^1_{j,c})^{\otimes n}\bigr)
          +nD(\pi^1_{j,c}\Vert\mu).
                                                               \tag{5}
\]

It follows, both pointwise and after averaging, that

\[
 D(\pi^1_{j,c}\Vert\mu)\le K_j(c)/n,
 \qquad I(Z_i;C_{\le j})\le H/n.                            \tag{6}
\]

This proves the proposed row-information inequality. Its justification
uses independence of the prior rows as well as posterior exchangeability;
exchangeability alone would not imply it.

## 3. One entropy event for every prefix

The process \(K_j(C_{\le j})\) is a nonnegative submartingale for the
retained-prefix filtration. The posterior at the earlier prefix is the
conditional mixture of the next posterior, and relative entropy is convex
in its first argument. Equivalently, conditional Jensen applied to the
convex function \(u\mapsto u\log u\) of the posterior density proves
the submartingale assertion. Its terminal expectation equals the mutual
information in (3).

For \(0<\alpha<1\), the finite maximal inequality therefore gives

\[
 \Pr\left\{K_j(C_{\le j})\le H/\alpha
                    \text{ for every }j\le P\right\}\ge1-\alpha.
                                                               \tag{7}
\]

For completeness, stop at the first index where the nonnegative process
exceeds \(H/\alpha\). On each first-crossing event, the conditional
expectation of its terminal value is at least its current value. Summing
these disjoint events bounds \((H/\alpha)\) times the crossing
probability by the terminal expectation, which is at most \(H\).
If \(H=0\), every posterior equals the prior almost surely and (7)
has the evident zero-entropy interpretation.

Combining (5)--(7) also controls every one-row test at every prefix. In
particular, with total variation defined as a supremum over events,

\[
 \|\pi^1_{j,C_{\le j}}-\mu\|_{\rm TV}
                  \le\sqrt{H/(2\alpha n)}.                  \tag{8}
\]

The entropy-to-total-variation inequality used here follows by mapping
both laws to a two-set partition attaining their positive density
difference, then using the binary relative-entropy bound
\(D(\operatorname{Bern}(p)\Vert\operatorname{Bern}(q))
\ge2(p-q)^2\). The latter follows because its second derivative in
\(p\) is \(1/[p(1-p)]\ge4\), and its value and first derivative
vanish at \(p=q\).

Equation (8) is uniform over all bounded measurable row tests chosen
after seeing the prefix. No query net is involved. It is still only a
marginal statement; the rows generally remain dependent under the
posterior.

## 4. Conditional empirical averages: a stronger uniform inequality

The full entropy in (4), rather than a two-row covariance estimate, gives
the sharper useful result. Fix a prefix \(c\) with \(K_j(c)<\infty\)
and any measurable \(f_c\) satisfying \(|f_c|\le B_f\). Define its
empirical-minus-prior discrepancy by

\[
 A_c(z_{1:n})=\frac1n\sum_i f_c(z_i)-\int f_c\,d\mu.
\]

Then

\[
 \mathbb E_{\pi_{j,c}}|A_c|
       \le B_f\sqrt{\frac{2[K_j(c)+\log2]}n}.                \tag{9}
\]

To prove it, a variable taking values in an interval of length \(2B_f\)
has centered log moment-generating function at most
\(\lambda^2B_f^2/2\). One elementary proof differentiates that log
moment-generating function twice: the second derivative is a variance
under an exponentially tilted law, still supported in the same interval,
and is at most \(B_f^2\). Integrating twice proves the bound. Independence
under \(\mu^{\otimes n}\) consequently gives

\[
 \mathbb E_{\mu^{\otimes n}}e^{\lambda|A_c|}
                   \le2e^{\lambda^2B_f^2/(2n)}.
\]

For any laws \(\nu\ll\lambda_0\) and integrable \(g\), the entropy
inequality

\[
 \mathbb E_\nu g\le D(\nu\Vert\lambda_0)
                                  +\log\mathbb E_{\lambda_0}e^g
\]

follows by comparing \(\nu\) with the probability law whose density
relative to \(\lambda_0\) is proportional to \(e^g\).
Apply it with \(g=\lambda|A_c|\), divide by \(\lambda>0\), and
minimize in \(\lambda\) to obtain (9).

The corresponding posterior tail bound is, for
\(nt^2/(2B_f^2)>\log2\),

\[
 \pi_{j,c}(|A_c|>t)
 \le\frac{K_j(c)+\log2}{nt^2/(2B_f^2)-\log2}.                \tag{10}
\]

Under the product prior the event has probability at most
\(2e^{-nt^2/(2B_f^2)}\). Mapping the two measures to the event and
its complement, binary relative entropy is at least
\(q\log(1/p)-\log2\), where \(q\) and \(p\) are the posterior
and prior event probabilities. This proves (10).

On the single event (7), (9)--(10) hold with \(K_j(c)\) replaced by
\(H/\alpha\), simultaneously for every prefix and every such test.
The test may depend on the unseen sphere point, time coordinate, and
current prefix. The inequalities are pointwise consequences of the
entropy bound for a probability measure, so there is no uncountable
union of exceptional sets. For a passive query, first discard packet
coordinates belonging to unused future training calls. Relative entropy
cannot increase under this marginalization: the full relative entropy
equals the marginal relative entropy plus a nonnegative average
conditional relative entropy. Appending the query representation's
independent fresh Gaussian coordinates then leaves that marginal relative
entropy unchanged. The same conclusions apply to the augmented row
functions. This argument does not require the passive-query innovations
to be independent of unused future training innovations in a full-tape
coupling.

Thus conditional empirical-versus-prior row averaging is established.
Replacing a nonlinear function of several empirical averages requires a
separate estimate, which (9) does not supply.

## 5. The precise sufficient stability estimate for a population query

Here is a conditional result identifying that estimate. At a fixed
training prefix and query, write the appended scalar query program as

\[
 D_r=\frac1n\sum_i G_r(Z_i;c,D_{<r})+\eta E'_r,
                      \qquad 1\le r\le q,                  \tag{11}
\]

where any fresh row innovations are included in \(Z_i\), and the fresh
scalar noises \(E'_r\) are independent of the retained history and row
packets. Suppose \(|G_r|\le B_q\) and these functions are
\(\Lambda_q\)-Lipschitz in their query-summary prefix, uniformly in
the other arguments. Let the scalar output be
\(\Phi(c,D_{\le q})\), \(L_q\)-Lipschitz in its summary argument.
Include a final empirical readout among (11) if needed.

Define a deterministic population query using the current training
prefix as fixed coefficients:

\[
 d_r=\int G_r(z;c,d_{<r})\,\mu(dz),
 \qquad d(c,x,t)=\Phi(c,d_{\le q}).                          \tag{12}
\]

This definition does not rerun the training updates. It does require
evaluating the displayed row integrals, whose runtime is discussed below.

For \(0<\rho<1\), set

\[
 a=B_q\sqrt{\frac2n\left[
          \log(2q)+\frac{H/\alpha+\log2}{\rho}\right]},
 \qquad A_q=(1+L_q)q(1+\Lambda_q)^q.                         \tag{13}
\]

On event (7), with posterior probability at least \(1-\rho\), all
empirical means of the fixed functions \(G_r(\cdot;c,d_{<r})\)
are within \(a\) of their prior means. To check this, their union
event under the product prior has probability at most
\(2q e^{-na^2/(2B_q^2)}\). Applying the binary-entropy argument
from (10) to that one union event proves the assertion.

On this event and \(\max_r|E'_r|\le T\), put
\(e_r=\max_{s\le r}|D_s-d_s|\). Subtracting (11) and (12) gives

\[
 e_r\le(1+\Lambda_q)e_{r-1}+a+\eta T,
 \qquad
 |\Phi(c,D)-d(c,x,t)|\le A_q(a+\eta T).                     \tag{14}
\]

The independent scalar-noise failure costs at most
\(2q e^{-T^2/2}\) conditional on every prefix. Consequently (14)
is a uniform conditional query estimate, at every prefix on (7), with
failure at most \(\rho+2q e^{-T^2/2}\). The uniformity includes every
sphere point and time for which the same constants apply.

This interfaces directly with the robust-center theorem in the supplied
`CONDITIONAL_PREFIX_CENTER.md`. Suppose its exact posterior query law
has mass at least \(5/8\) in
\([f_0(x,t)-b-\varepsilon,f_0(x,t)+b+\varepsilon]\).
If the failure just specified is less than \(5/8\), that interval and
the posterior interval around the deterministic value (12) must overlap.
Therefore, on the intersection of the two training success events,

\[
 |d(c,x,t)-f_n(t,x)|
       \le2b+\varepsilon+A_q(a+\eta T)                     \tag{15}
\]

simultaneously over all prescribed prefixes, times, and sphere inputs.
The extra training failure is only \(\alpha\).

Thus a sufficient statistical condition for retaining the dense-upper
scale is

\[
 A_q B_q\sqrt{\log(2q)+H}=O(\sqrt n\,b_n),                 \tag{16}
\]

with the specified fixed confidence factors understood. If
\(A_qB_q\), \(q\), and \(H\) were polylogarithmic, their contribution
would be smaller eventually than the inherited
\(n^{-1/2}e^{CY^2\sqrt{\log(en)}}\sqrt{\log(en)}\) allowance for
each fixed admissible problem with \(Y>0\) and its positive certificate
constant. This would preserve an \(O(b_n)\) error, not automatically
the old theorem's exact coefficient \(2b_n+1/n\).

The supplied sources do not prove (16). Their range bounds allow
\(B_q=\exp[\operatorname{polylog}(n)]\), and the coefficient
sensitivities contain powers of
\(\sigma^{-1}=\exp([\log(en)]^2)\). Even one such power in
\(A_q\) overwhelms \(\sqrt n\,b_n\). Composing the current bounds
does not close the estimate. A much better concentration scale than the
global range, and a bound on output sensitivity in the corresponding
moment geometry, could improve (13)--(16); neither follows from (3).

## 6. A counterexample to obtaining stability from information alone

This example concerns the generic bounded scalar-program interface, not
the original trained network. It is not a no-go theorem for that network
or for efficient decoding. It proves that its missing stability estimate
cannot be replaced by an information-budget argument alone, even when
the exact program output is sharply concentrated around zero.

Let \(Z_i\) be standard Gaussian, set
\(X_i=\max(-1,\min(Z_i,1))\), and define

\[
 M=\frac1n\sum_iX_i,
 \quad \sigma=e^{-[\log(en)]^2},\quad \eta=\sigma^2,
 \quad C=M+\eta E,                                        \tag{17}
\]

where \(E\) is an independent standard Gaussian. This is one bounded,
globally Lipschitz scalar-history update, with

\[
 I(Z_{1:n};C)\le\tfrac12\log(1+\eta^{-2})=O(\log^2 n).
                                                               \tag{18}
\]

Append a query mean \(D=M+\eta E'\), with independent standard
Gaussian \(E'\), and output

\[
 U=\tanh((D-C)/\sigma)
                  =\tanh(\sigma(E'-E)).                    \tag{19}
\]

In particular, \(|U|\le\sigma(|E|+|E'|)\); the exact output tends
to zero much faster than the dense-upper scale with arbitrarily high
fixed probability. The output is bounded by one. Its only large scalar
gain is \(\sigma^{-1}\), whose logarithm has exactly the permitted
polylogarithmic size.

The population replacement of the query mean is
\(d=\mathbb E X_i=0\), giving

\[
 u(C)=\tanh(-C/\sigma).                                    \tag{20}
\]

With probability tending to one, \(|u(C)|\ge\tanh(1)\).
Here is an elementary small-ball proof. Put
\(p=\Pr(|Z_1|<1)>0\), and let \(J\) be the first index with
\(|Z_J|<1\). The event that no such index exists has probability
\((1-p)^n\). Conditional on \(J=j\), the variable \(Z_j\) has
the standard Gaussian density restricted to \((-1,1)\), bounded
by \(1/(p\sqrt{2\pi})\). It is independent of the other summands
under this conditioning. Thus \(M\), and also \(M+\eta E\),
has conditional density bounded by \(n/(p\sqrt{2\pi})\).
Summing over \(j\) yields

\[
 \Pr(|C|\le\sigma)
       \le(1-p)^n+\frac{2n\sigma}{p\sqrt{2\pi}}
                         \longrightarrow0.                 \tag{21}
\]

Equations (19)--(21) show an order-one population-substitution error
despite (18), the one-row information bound, and near-deterministic exact
outputs. The error arises because the true second empirical mean agrees
with the retained first one up to tiny noise. Population substitution
breaks this consistency before applying a large scalar gain.

This deliberately redundant example can be simplified by reusing the
stored mean. That observation is consistent with its purpose: a decoder
may exploit exact identities or structural cancellations, but information
alone does not establish those cancellations or their numerical stability.
No claim is made that this artificial scalar gain is realized by the
original physical network.

## 7. Consequence for the efficient-decoder route

The completed part is an all-prefix, all-row-test information estimate,
including a conditional population-query transfer theorem with explicit
constants. It avoids a separate information budget for every unseen query
and avoids a sphere net.

Two substantive obligations remain for this route:

1. Prove a concentration and propagation estimate such as (16) for the
   **actual** passive query, preferably in a geometry that retains the
   exact Gram identities and cancels artificial inverse-noise factors.
   Global entrywise Lipschitz bounds from the current representation are
   insufficient. This includes stability under a rounded retained prefix.
2. Evaluate the population row integrals in (12) deterministically in
   time polynomial in their counted description and logarithmic accuracy.
   Replacing a conditional integral by an unconditional integral does not
   establish this complexity. The row dimension is \(d+O(R)\); tensor
   quadrature can be exponential in it, while ordinary Monte Carlo with
   an absolute accuracy of order \(n^{-1/2}\) has a polynomial-in-\(n\)
   sample cost and does not provide the required deterministic query map.

The existing expensive conditional-Fourier decoder theorem is unchanged.
The low-information route has not produced a polynomial-time decoder or
shown that such a decoder is impossible. The sharp new obstruction is the
need to control the actual moment-to-output map and its row integration,
not a failure of the proposed mutual-information inequality.

## 8. Process and claim status

The research and rigorous-proof skills were read and applied. The required
custom notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` remained
unreadable with `Permission denied`; the supervisor's explicitly authorized
fallback to the supplied notation requirements was used. No other study,
old review, or archived book material was read. Only this assigned note
was written, and no Git index operation was performed.

| Claim | Status | Boundary |
|---|---|---|
| Total prefix information is at most (2) | Proved | Bounded noisy updates (1) |
| One-row information is at most \(H/n\) | Proved | Iid prior and symmetric scalar history |
| One event controls all-prefix conditional empirical averages | Proved | Equations (7), (9), (10) |
| Population passive query transfers through (15) | Proved under displayed bounds | Its explicit error may be useless |
| Information alone prevents large substitution error | Falsified | Counterexample (17)--(21) in the generic row-program class |
| The actual network satisfies (16) | Open | Current bounds do not imply it |
| Population row integrals have the required deterministic runtime | Open | No efficient integration theorem supplied |
| Efficient decoder for the full original contract | Open | Both preceding obligations remain |

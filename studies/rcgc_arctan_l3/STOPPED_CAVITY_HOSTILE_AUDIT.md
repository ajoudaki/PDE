# Hostile audit of the stopped two-sided cavity blueprint

**Provenance:** isolated clean-room referee; no project access and no
communication with the blueprint's designer or other agents.

**Date:** 2026-08-24  
**Verdict:** **reject as written; downstream implication sound, upstream
cavity proof not established.** The proposed empirical tail would indeed
give Osgood stability, but the blueprint hides uncontrolled repeated returns
inside response-trace self-averaging and uses a stop-removal quantifier
stronger than its master moment statement.

## Tail threshold

A sub-Gaussian \(C\sqrt p\) bound for every field is stronger than needed
and is not justified. A macroscopic low-rank response can retain a
\(\chi^2\)-type component with \(L^p\) growth \(Cp\). For a cavity-measurable
quadratic response,

\[
 \left\|\frac{g^*Rg-\operatorname{Tr}R}{n}\right\|_{L^p}
 \lesssim \frac{\sqrt p}{n}\|R\|_{HS}
          +\frac p n\|R\|_{op}.                       \tag{1}
\]

Thus sub-Gaussianity needs a flatness theorem. Fortunately a restartable
empirical \(\psi_1\) bound \(\|Q_2\|_p\lesssim p\) is enough: tail
splitting gives \(Cs\log(C/s)\), still an Osgood modulus. Only the
unbounded multiplier \(Q_2\) needs this certificate.

## Repeated tagged returns are order one

A deleted row may change the bulk normalized \(L^2\) state by
\(n^{-1/2}\) while producing an order-one return through that same row. For

\[
 x_j-x_j^{(a)}=n^{-1/2}g_{aj}h(\xi_a),qquad
 \xi_a=n^{-1/2}g_a^*x^{(a)},
\]

one has \(\|x-x^{(a)}\|_n=O(n^{-1/2})\), but

\[
 n^{-1/2}g_a^*(x-x^{(a)})
 =\frac{\|g_a\|^2}{n}h(\xi_a)\longrightarrow h(\xi_a).
\]

Consequently, subtracting only a cavity-independent first or second
variation does not make the remaining tagged return small. The time-simplex
factor can make an **all-order** causal response series summable, but does
not make orders \(k\ge2\) vanish with width.

## Response-trace self-averaging was the hidden theorem

For \(F=\operatorname{tr}_nR\), Efron--Stein needs a one-row trace change
of \(n^{-1+o(1)}\) in \(L^2\) to obtain vanishing variance. A generic
Lipschitz use of the known bulk influence gives only \(n^{-1/2+o(1)}\),
whose Efron--Stein sum is order one. The missing extra cancellation/locality
is itself a continuous-time adaptive local law. For a tail theorem,
self-averaging is unnecessarily strong; uniform Orlicz control of response
traces and their operator/Hilbert--Schmidt norms may suffice.

## Stop-removal quantifier failure

For fixed \(p\), the cost
\(e^{CT\sqrt{\log n}}=n^{o(1)}\) preserves a cavity power. But a statement
holding for each fixed \(p\) after \(n\to\infty\) does not show that a
global \(L\sqrt{\log n}\) coordinate stop is never hit. A union bound needs
uniform moment estimates through \(p\asymp\log n\). One exceptional
coordinate can be invisible to every fixed empirical moment and still hit
the stop. A soft good/bad-coordinate truncation would require a separate
proof that the bad set is negligible under every response contraction.

The alternative subexponential stop \(L_n\asymp\log n\) makes the crude
Grönwall factor \(e^{CL_nT}=n^{CT}\), potentially erasing the cavity gain.

## Corrected local target

At a restart time \(\tau\), assume the proved \(L^2\)/trace orbit bound
\(M\) and an empirical \(\psi_1\) bound \(K\) for \(Q_2(\tau)\). The
smallest useful theorem is the existence of
\(\delta=\delta(M,K)>0\) such that, for
\(I=[\tau,\tau+\delta]\),

\[
 \sup_{p\ge2}\frac1p
 \limsup_{n\to\infty}\sup_\pi
 \left(
  \mathbb E\frac1n\sum_i\sup_{t\in I}|Q_{2,i}^{n,\pi}(t)|^p
 \right)^{1/p}
 \le K',                                              \tag{2}
\]

for the exact flow and relevant Euler interpolants, with a restart recursion
such as \(K'\le K+C(M)\delta(1+K)\). The order
\(\limsup_n\sup_\pi\) is part of the claim.

Concrete leaves are:

1. direct empirical \(\psi_1\) initialization;
2. an exact nonperturbative one-site row/column Volterra cavity equation
   retaining every repeated tagged return;
3. uniform Orlicz, operator, and Hilbert--Schmidt response bounds sufficient
   for Hanson--Wright-type control;
4. all-order response summability and a genuine remainder theorem, unless
   the Volterra equation closes exactly;
5. noncircular stop removal via moderate deviations through
   \(p\le c\log n\) or a response-stable good/bad-coordinate truncation; and
6. uniform time increments and restart compatibility.

Until leaves 2--5 are proved, the cavity blueprint has not yet reduced the
adaptive problem enough to count as working machinery. It is the best
localized program identified by the probe, not a proof of D3.

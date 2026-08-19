# Amortized multi-observable MFP DAG

This directory extends the audited arbitrary-fixed-depth, one-sample,
unit-Gram order-five feature-ascent graph with observable-specific readout
heads.  The reusable graph is the six-sweep scalar backbone

\[
F1\to R1\to F2\to R2\to F3\to R3,
\]

whose 29 propagated scalar coordinate types determine
\(A_H=F_H'(0)\), \(B_H=F_H^{(3)}(0)\), and \(C_H=F_H^{(5)}(0)\).
Each sweep has exactly \(H\) nearest-neighbour layer transitions.  The
transition template is shared between layers inside a sweep, but the six
sweeps are different jet-grade maps.

The first completed extra head is the hidden-activation squared-RMS jet

\[
Q_\ell(s)=n^{-1}\lVert x^\ell(s)\rVert^2.
\]

After the backbone is available, the missing contraction
\(\Gamma_{04}^\ell\) closes in one additional bottom-up sweep.  The public
recurrence has two dynamic coordinates, \((\gamma04,a41)\), and contains
only rational arithmetic, stored deterministic backbone states, and the
one-dimensional activation moments

\[
M_{\nu_0\ldots\nu_5}
=\mathbb E_{G\sim N(0,1)}
  \prod_{r=0}^{5}\phi^{(r)}(G)^{\nu_r}.
\]

The initially derived third coordinate obeys

\[
a43_\ell=d(1+a43_{\ell-1}),\qquad 1+a43_\ell=\tau_\ell,
\]

and is therefore eliminated exactly.  The two remaining transition
polynomials contain 64 and 17 canonical monomials.  This is the smallest
state found; no minimality claim is made.

The complete formulas and proof are in
[`independent_route_a/INDEPENDENT_DERIVATION.md`](independent_route_a/INDEPENDENT_DERIVATION.md).
The independently frozen second producer, exact layerwise maps, and full
finite-width/partition/transpose ledger are in
[`../../depth_order5_observables/independent/INDEPENDENT_ROUTE_S_REPORT.md`](../../depth_order5_observables/independent/INDEPENDENT_ROUTE_S_REPORT.md).
The hostile contract and audit live in [`audit/`](audit/).

## Observable outputs

With moving activation jets \(X_\ell^{(r)}\), define

\[
\Gamma_{rs}^\ell
=\lim_{n\to\infty}\mathbb E\,n^{-1}
  \langle X_\ell^{(r)},X_\ell^{(s)}\rangle.
\]

The exact product rule gives

\[
Q_\ell^{(k)}(0)
=\sum_{r=0}^{k}\binom{k}{r}\Gamma_{r,k-r}^\ell.
\]

The backbone dictionary is

\[
\Gamma_{11}=w_\ell,qquad
\Gamma_{02}=q02_\ell,qquad
\Gamma_{22}=q22_\ell,qquad
\Gamma_{13}=q13_\ell,
\]

and the new head gives \(\gamma04_\ell=\Gamma_{04}^\ell\).  Hence

\[
Q_\ell''(0)=2(w_\ell+q02_\ell),
\]

\[
Q_\ell^{(4)}(0)
=2\gamma04_\ell+8q13_\ell+6q22_\ell.
\]

For \(R_\ell=\sqrt{Q_\ell}\) under unit Gram,

\[
R_\ell''(0)=w_\ell+q02_\ell,
\]

\[
R_\ell^{(4)}(0)
=\gamma04_\ell+4q13_\ell+3q22_\ell
-3(w_\ell+q02_\ell)^2.
\]

For label-one MSE, \(ds/dt=c(1-F(s))\), \(c=2\eta\).  If
\(q_2=Q_\ell''(0)\) and \(q_4=Q_\ell^{(4)}(0)\), exact composition yields

\[
\begin{aligned}
Q_t''(0)&=c^2q_2,\\
Q_t'''(0)&=-3c^3A_Hq_2,\\
Q_t^{(4)}(0)&=c^4(q_4+7A_H^2q_2),\\
Q_t^{(5)}(0)&=-5c^5\bigl[(3A_H^3+B_H)q_2+2A_Hq_4\bigr].
\end{aligned}
\]

## Claim boundary

The finite-width differentiation identities are exact.  The displayed
moment-only head is algebraically audited at separately fixed depths.  Its
annealed large-width interpretation is a theorem for polynomially smooth
activations—\(C^\infty\), with every derivative polynomially bounded—via
the fixed tensor-program \(L^p\) limit.  Under weaker smoothness, convergence
in probability plus a uniform \(L^{1+\epsilon}\) bound for every retained
Gram is required separately.

No result here is uniform in growing depth, covers positive feature-ascent
time, proves that every observable has a small head, or closes the analogous
preactivation-RMS head.  The order-seven discussion is roadmap-only: no
order-seven state dimension, sweep count, derivative ceiling, or \(O(H)\)
claim is promoted.

## Reproduction

```bash
python -m studies.mean_field_peeling.generic_first_stieltjes.depth_order5_scalar.multi_observable.independent_route_a.run_checks
python -m studies.mean_field_peeling.generic_first_stieltjes.depth_order5_observables.independent.run_checks
```

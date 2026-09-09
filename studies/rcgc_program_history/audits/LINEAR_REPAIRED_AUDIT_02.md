# Linear common-theorem repaired audit 02

**Provenance:** fresh clean-room referee; it received only the proposed
common theorem and proof modules, had no project access, and communicated
with no other agent.

**Date:** 2026-08-24  
**Verdict on the feature-time interpretation:** reject. The Fock source and
local Picard/trace-tail calculus are sound, but the unit feature-gradient
flow blows up in finite feature time for every \(H\ge2\). The compact
**physical-time** theorem remains salvageable and is the theorem retained by
the study.

## Source accepted

For mutually orthogonal creation colors,

\[
 c_\ell=\ell(e_{\ell,+})+\ell(e_{\ell,-})^*
\]

has the correct real-Ginibre first-order transpose moments and scaling;
there is no missing \(1/\sqrt2\). The direct sum
\(\Gamma_\ell=c_\ell\oplus c_\ell\), with the two endpoint roots in
different summands, correctly makes their full cyclic sectors orthogonal
while exposing both to the same matrix sources. Fixed rooted Grams converge
jointly in probability; an \(O(n^{-1})\) variance estimate does not by
itself give almost-sure convergence.

## Exact feature-time obstruction

Let \(m=H+1\). In unit feature time, every parameter-block energy obeys

\[
 \frac d{ds}\frac12\|u\|^2=f,
 \qquad
 \frac d{ds}\frac12\|A\|^2=f,
 \qquad
 \frac d{ds}\frac12\|G_\ell\|_F^2=f,
\]

so the total raw parameter energy satisfies \(E'=mf\). Pairwise
layer-energy differences (and stronger operator-valued balancedness
identities) are conserved, but these balances are not coercive for gradient
ascent.

For the specified Fock source, put

\[
 F(s)=\int_0^sf(r)\,dr=\tfrac12(\|u(s)\|^2-1).
\]

The balances and Cauchy--Schwarz give constants \(B,C>0\) such that, for
positive \(s\),

\[
 f'=K\ge\frac{m f^2}{B+2F},
 \qquad
 f(s)\ge C(B+2F(s))^{m/2}.
\]

Since \(\int^\infty(B+2F)^{-m/2}dF<\infty\) when \(m>2\), the maximal
feature interval has a finite right endpoint and \(f\to+\infty\); time
reversal gives a finite left endpoint with \(f\to-\infty\). Thus global
feature-time well-posedness is false for \(H\ge2\). It remains true for
\(H=1\).

## Why physical time survives

The actual training ODE multiplies the feature vector field by
\(2\eta e\) and includes

\[
 \dot e=-2\eta eK,
 \qquad
 \int_0^T e^2K\,dt\le |e(0)|^2/(4\eta).
\]

For each endpoint block and each rank-one matrix velocity,

\[
 \int_0^T\|\dot\theta_j(t)\|\,dt
 \le |e(0)|\sqrt{\eta T}.
\]

For a matrix block the rank-one Frobenius, Hilbert--Schmidt, and trace norms
agree. Hence all endpoint and trace-class perturbation norms stay bounded on
compact physical time, giving global continuation. This direct physical
argument neither asserts nor needs a global feature clock.

## Picard and nuclear-tail audit

On a common physical-time state ball, the polynomial/rank-one vector field
has a dimension-free local Lipschitz constant. Fixed Picard iterates are
finite algebraic combinations of rooted word vectors and rank-one
operators; every scalar contraction is a continuous function of finitely
many rooted Grams. A finite composition of approximate Picard flow maps,
with joint multi-time compiled signatures, handles later time slabs without
ever subtracting vectors in different widths.

If

\[
 I_\ell(t)=2\eta e(t)b_{\ell+1}(t)\otimes x_\ell(t),
\]

then on a safe slab it is uniformly Lipschitz in trace norm. Its \(N\)-cell
Riemann integral has rank at most \(N+1\) and is within \(C/N\) in trace
norm, uniformly in time and width. This proves the claimed best-rank tail,
provided the fixed-rank bridge includes all cross-time Grams at the mesh
nodes.

## Mandatory disposition

The study records feature-globality as falsified, restricts every
feature-time regression formula to the maximal feature interval, and states
the theorem directly in autonomous physical time. A further isolated audit
must verify that no feature-global premise remains hidden in the slabwise
Picard transfer.

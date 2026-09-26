# Unrestricted circle approximation at different orders

This continues DERIVATION.md's static question. The current read-in, readout
and M may be customized for each target and tolerance, with no common norm
bound. The joint read-in/dictionary law may change while the read-in marginal
remains standard Gaussian. The claim is about uniform approximation.

Let F_1 denote these p=1 outputs and let C_odd(S^1) be the continuous functions
with f(theta+pi)=-f(theta). Then the uniform closure of F_1 is C_odd(S^1).
Every finite-order bias-free tanh closure output is in C_odd(S^1), assuming
integrable readout, bounded fixed dictionary features and read-in finite almost
surely. Therefore no function uniformly approximable at p=2 or p=3 fails to
be uniformly approximable at p=1 under these permissions.

Proof of the upper inclusion: tanh(w dot u_theta) is continuous almost surely,
and the bounded lower dictionary dominates its contraction. Dominated
convergence gives continuity of a(theta). The upper tanh is then continuous
almost surely, and the integrable bound |c| gives continuity of f. Oddness of
both tanh layers gives the half-circle sign change, regardless of mark symmetry.
These properties are preserved by uniform limits.

For the converse, finite odd-frequency trigonometric polynomials are dense in
C_odd. A self-contained proof uses

\[
F_N(t)=\frac1{N+1}\left|\sum_{j=0}^N e^{ijt}\right|^2,
\qquad T_N(\theta)=\frac1{2\pi}\int_{-\pi}^{\pi}F_N(t)f(\theta-t)\,dt.
\]

The finite square expansion makes F_N a nonnegative trigonometric polynomial
with integral 2pi. Thus T_N is a trigonometric polynomial and inherits the
half-circle sign change, so it has only odd-frequency sine and cosine terms.
For 0<delta<pi the finite geometric sum gives

\[
F_N(t)\le\frac1{(N+1)\sin^2(\delta/2)}\quad(\delta\le|t|\le\pi).
\]

Split the integral at |t|=delta. With omega_f the modulus of continuity,
positivity and unit normalized mass give

\[
\|T_N-f\|_\infty\le\omega_f(\delta)+
\frac{2\|f\|_\infty}{(N+1)\sin^2(\delta/2)}.
\]

Choose delta small, then N large, to obtain an odd polynomial T_N within
e/2 of f. DERIVATION.md (16) constructs a p=1 state within
a^2||T_N||_infinity^3/6 of T_N. Choose a nonzero and small enough to make
this <e/2; for T_N=0 choose zero readout. The triangle inequality proves
the assertion for every e>0. The populations, couplings and finite parameters
may depend on f and e, with no uniform cost guarantee.

This does not settle exact representability, fixed populations with only M
varying, bounded parameter norms, finite population integration counts, or
prescribed training dynamics. Higher p could matter under those restrictions.

Separately, the complete established passage "Conditional parity equivalence
of orders one and two" in docs/global_nonlinear.md proves identical canonical
p=1 and p=2 trajectories under exact sign symmetry, matching ridge and matching
integration. Degree-two added features are even in Gaussian marks; the canonical
odd state sector, including its zero inactive matrix blocks, is invariant.
Odd readout alone would not suffice for arbitrary states. The maintained
p-dependent ridge schedule does not meet the matched-ridge condition. Degree
three can add odd active channels without altering the unrestricted density
conclusion proved here.

Inputs were this study's DERIVATION.md and the complete established circle-parity
and conditional p=1/p=2 equivalence passages. No other study was used. Root
authored the argument; fresh prompt-only agent p_order_capacity_check separately
verified the continuity, parity and explicit density bound, and highlighted the
invariant-sector requirement for the optional p=2 statement. This is an internal
mathematical consequence, not a promotion review or an empirical result.

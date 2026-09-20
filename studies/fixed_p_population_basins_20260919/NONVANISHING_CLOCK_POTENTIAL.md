# The fixed-rate variant has an explicit clock potential

2026-09-19. Short extension of NONVANISHING_RATE_RESULTS.md Section 4,
with exactly its data, model, activation and continuation hypotheses.
No new source, experiment, original-GF fitting claim, or promotion.

Fix lambda>0, 0<epsilon<1, and sample V uniformly on (0,1) independently.
The declared activation time and current countdown are

\[
 A_\varepsilon=\lambda^{-1}[\log(1/\varepsilon)+V],
 \qquad a(t)=(A_\varepsilon-t)_+.
\]

The algorithm's full restart state includes a. For a>0 run original GF
and set a'=-1. At a=0 keep a'=0 and run the existing corrected flow at
fixed strength alpha=lambda/4, with tangent noise amplitude epsilon.
Use the same almost-sure regular activation and fitted-absorption
conventions proved in the parent note. The scalar a is a declared
algorithmic countdown, not a future trained endpoint or unknown future
trajectory.

Define the current extended-state functional

\[
 \Psi(S,a)=e^{\lambda a}L(S).
 \tag{1}
\]

It dominates L. Before activation, the original energy identity gives

\[
 \dot\Psi=e^{\lambda a}(\dot L-\lambda L)
 =-e^{\lambda a}\|\nabla L\|^2-\lambda\Psi
 \le-\lambda\Psi.
 \tag{2}
\]

After activation a=0, Psi=L, and the parent theorem gives
dot(Psi)=dot(L)<=-lambda L=-lambda Psi. At activation a and S are
continuous, so Psi is continuous. At a fitted absorbing endpoint L=0
and Psi remains zero. Integrating these piecewise inequalities yields

\[
 L(S_\varepsilon(t))\le\Psi(t)\le e^{-\lambda t}\Psi(0),
 \quad
 \Psi(0)=\frac{e^V}{\varepsilon}L_0.
 \tag{3}
\]

Thus both pathwise and expected all-time bounds are explicit:

\[
 L(S_\varepsilon(t))\le
 L_0\min\{1,(e/\varepsilon)e^{-\lambda t}\}\quad\text{a.s.},
\]
\[
 E L(S_\varepsilon(t))\le
 L_0\min\{1,((e-1)/\varepsilon)e^{-\lambda t}\}.
 \tag{4}
\]

The last expectation uses E exp(V)=e-1, and requires no moment of the
activation Gram inverse. Equation (4) extends the parent note's sharper
late expected bound to every time; it does not contradict its bound.

For fixed t, the initial 1/epsilon potential scale diverges as the
modified process approaches original GF. The potential is a valid
Lyapunov functional of the extended algorithmic state, but its countdown
factor records planned future intervention. It is not a new decaying
hidden-geometry potential for the original autonomous population state
S alone. This construction explains exactly where the slow start is
stored while retaining a nonvanishing exponent.

# Circle tangent route: high angular modes and the trained readout weight

2026-10-11. Second bounded scoped theoretical attempt. Scientific inputs:
`paper/compact.tex`, `paper/compact_fitting.tex`,
`ENDPOINT_TRANSVERSE_ROUTE.md`, and `ENDPOINT_PROBE_NONCANCELLATION.md`.
No experiments, manuscript edits, or Git operations. The same required
proof, research, and canonical-notation skills were applied.

A second bounded attempt tested a different mechanism: differentiate a high
circle mode with respect to hidden parameters, then compare that derivative
with the readout derivative. The following obstruction is exact. It refutes
the proposed inference from Gaussian roots, a nonzero analytic readout, and
a near-identity hidden map alone. It is not a counterexample to the canonical
gradient-flow endpoint, because reachability of the obstructing readout by
that flow is not established.

First state the proposed cancellation test precisely. Let \(u\) denote all
hidden mobility coordinates, \(a=w/\sqrt n\), and

\[
b_\psi(u)=\frac1{2\pi}\int\psi(\theta)
        \frac{h^{(L)}(u,x(\theta))}{\sqrt n}\,d\theta.
\]

For fixed initial hidden coordinates \(u_0\), the fitted functional is
\(X(u_0)=a_\infty(u_0)^\top b_\psi(u_\infty(u_0))\). If the two endpoint
maps are differentiable, the chain rule gives

\[
\nabla_{u_0}X
=(D u_\infty)^\top\nabla_u[a_\infty^\top b_\psi]
 +(D a_\infty)^\top b_\psi,
\tag{17}
\]

where the partial hidden gradient holds \(a_\infty\) fixed. If
\(\sigma_{\min}(D u_\infty)\ge s>0\) and
\(\|D a_\infty\|\le M\), then

\[
\|\nabla_{u_0}X\|
\ge s\|\nabla_u[a_\infty^\top b_\psi]\|-M\|b_\psi\|.
\tag{18}
\]

Thus unbounded hidden-gradient/readout-gradient ratios would prevent
cancellation by this particular bound. Neither endpoint derivative bound is
asserted here for the canonical dynamics. More decisively, nonpolynomial
circle features and a nonzero readout do not themselves force the required
unbounded ratio.

## 1. The unweighted high-mode gain is real

Consider the elementary circle ridge family

\[
\phi(U^\top v(\theta))=\cos(U^\top v(\theta)),\qquad
U\sim N(0,I_2),\qquad
B_\psi(U)=\frac1{2\pi}\int\psi(\theta)
             \cos(U^\top v(\theta))\,d\theta.
\tag{19}
\]

Cosine is real, nonaffine, entire, and has bounded derivatives on every
fixed horizontal strip. For the complex Fourier test
\(\psi(\theta)=e^{-ik\theta}\), write \(B_k=B_\psi\). Complex notation
combines the two corresponding real tests; all norm identities use modulus
squares. The function \(B_k\) has angular character \(k\) as a function of
\(U\). It is orthogonal in Gaussian \(L^2\) to every polynomial of degree
less than \(|k|\): such a polynomial has angular frequencies of absolute
value at most its degree, and the Gaussian angle is uniform. Expanding in
the orthonormal product Hermite polynomials \(H_\alpha\) gives

\[
\mathbb E|B_k|^2=\sum_\alpha|c_\alpha|^2,
\qquad
\mathbb E\|\nabla_U B_k\|^2
=\sum_\alpha |\alpha|\,|c_\alpha|^2
\ge |k|\,\mathbb E|B_k|^2.
\tag{20}
\]

Here the derivative identity follows from
\(\partial_j H_\alpha=\sqrt{\alpha_j}H_{\alpha-e_j}\) and orthogonality;
it extends from finite Hermite sums by Gaussian Sobolev convergence.
The functions in (19) and their first derivatives are bounded, so that
Sobolev identity applies. Every even nonnegative \(k\) gives a nonzero
mode: for \(U=r(\cos\alpha,\sin\alpha)\), its leading Taylor term is
\((-1)^{k/2}r^k e^{-ik\alpha}/(2^k k!)\).

Equation (20) validates the unweighted part of the proposed mechanism.
The trained hidden gradient, however, is weighted by the readout amplitude.

## 2. An everywhere-positive analytic readout reverses the gain

Assign the analytic readout amplitude

\[
w(U)=e^{-\|U\|^2/4}.
\tag{21}
\]

Here \(w(U)\) is the physical scalar readout of a neuron; its normalized
readout coordinate is \(w(U)/\sqrt n\). For this one-neuron ridge
contribution, the feature-kernel quadratic form
is \(\mathbb E|B_\psi|^2\), while the incoming-hidden-weight tangent
quadratic form is \(\mathbb E[w(U)^2\|\nabla_U B_\psi\|^2]\).
These are exactly the population counterparts of the two top-layer
derivative blocks, with the same row normalization on both sides.

Every function \(B=B_\psi\) in (19) satisfies
\(\Delta_U B=-B\), because \(\|v(\theta)\|=1\). Put
\(p(U)=(2\pi)^{-1}e^{-\|U\|^2/2}\). The weight
\(w^2p=(2\pi)^{-1}e^{-\|U\|^2}\) has gradient
\(-2U w^2p\). Integration by parts twice gives

\[
\begin{aligned}
\mathbb E[w^2\|\nabla B\|^2]
&=\int w^2p\,|B|^2
  +\int w^2p\,U^\top\nabla |B|^2\\
&=\mathbb E\left[e^{-\|U\|^2/2}
            (-1+2\|U\|^2)|B|^2\right]\\
&\le\frac4e\,\mathbb E|B|^2.
\end{aligned}
\tag{22}
\]

The last bound uses
\(2r^2e^{-r^2/2}\le4/e\) and discards the negative term. Boundary terms
vanish since \(B\) and all its first two derivatives are bounded by
\((2\pi)^{-1}\int|\psi|\), whereas the weight is Gaussian. The complex
case follows by taking real parts of the integrations by parts.

Thus the weighted hidden tangent is bounded by a fixed multiple of the
feature kernel on the entire spatial test space, despite infinitely many
nonzero circle modes and a readout that is nonzero at every root.

In fact the high-mode ratio tends to zero. For completeness, define

\[
I_k(t)=\sum_{r=0}^{\infty}
       \frac{(t/2)^{k+2r}}{r!(k+r)!},\qquad k\ge0,
\]

the coefficient of \(e^{ik\theta}\) in \(e^{t\cos\theta}\). Expanding
the two exponentials in
\(e^{(t/2)e^{i\theta}}e^{(t/2)e^{-i\theta}}\) proves this coefficient
formula directly. Gaussian characteristic functions give, for even
\(k\ge2\),

\[
\begin{aligned}
\mathbb E|B_k|^2&=e^{-1}I_k(1),\\
\mathbb E[w^2\|\nabla B_k\|^2]
&=\frac{e^{-1/2}}4
       [I_{k-1}(1/2)+I_{k+1}(1/2)].
\end{aligned}
\tag{23}
\]

To check the second line, multiplication by \(w^2\) changes the Gaussian
measure to one half the probability measure \(N(0,I_2/2)\). The
derivative covariance at angle difference \(t\) is therefore
\(\tfrac12 e^{-1/2}\cos(t)\sinh(\tfrac12\cos(t))\); its even Fourier
coefficient is the displayed expression. The first line follows from
\(\mathbb E[\cos(U^\top v)\cos(U^\top v')]
=e^{-1}\cosh(v^\top v')\).

For each fixed positive \(t\), the series gives
\(I_k(t)=(t/2)^k/k!\,[1+O(k^{-1})]\). Indeed the ratio of the sum to its
first term lies between one and
\(\exp(t^2/[4(k+1)])\). Substitution into (23) proves

\[
\frac{\mathbb E[w^2\|\nabla B_k\|^2]}
     {\mathbb E|B_k|^2}
\sim e^{1/2}k\,2^{-k}\longrightarrow0
\qquad(k\to\infty,\ k\text{ even}).
\tag{24}
\]

High-degree angular modes concentrate their Gaussian norm at increasingly
large root radius. Readout decay suppresses precisely that part of the
root distribution. A pointwise nonzero readout, even one bounded away from
zero on every fixed compact root set, cannot prevent this effect.

## 3. Exact scope of the obstruction

Multiplying (21) by any \(\varepsilon>0\) makes both the readout and its
root derivative arbitrarily small, while preserving nonzero analyticity;
(22) then has constant \(4\varepsilon^2/e\). The incoming-root map can be
the identity. Thus near-identity hidden transport and a small bounded
readout derivative do not repair this operator inference. The corresponding
population predictor is even a nonzero constant on the circle,
\(\varepsilon(2/3)e^{-1/3}\), so it fits any finite training panel with
that constant label vector. Choosing \(\varepsilon\) sufficiently small
places those labels under any specified positive cap.

This static construction has not been produced by training from zero
readout. It also treats the incoming top-row derivative only; the other
trained hidden blocks could contribute an additional coercive mechanism.
Accordingly it does not refute (18) for the full canonical endpoint, the
desired dense-copy theorem, or a flow-specific non-domination theorem.
It refutes the proposed shortcut that nonaffine circle modes, Gaussian
rows, and nonzero trained-amplitude values alone establish non-domination.

The precise remaining requirement is a property of the readout actually
created by canonical training that prevents suppression of the Gaussian
regions carrying high circle modes, or a coercive contribution from other
hidden blocks with a separately proved noncancellation bound. Neither is
supplied by the original cap, the absolute displacement tube, or the
qualitative nonzero-readout chart in the authorized sources. Even a proved
operator non-domination statement would still need a width-stable covariance
and anti-concentration argument before giving the endpoint fluctuation
theorem.

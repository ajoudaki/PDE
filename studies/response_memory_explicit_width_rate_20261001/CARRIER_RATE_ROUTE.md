# Direct finite-width carrier route

Status: initial independent route frozen, 2026-10-01. The general nonlinear
finite-width rate remains open. This note proves two reductions and a direct
finite-width result for the linear-activation subclass. The subclass result is
not a substitute for the nonlinear target.

## Contract and inputs

The target is the actual dense gradient flow in `paper/main.tex`, Setting,
under the assumptions of `paper/results.tex`, Theorem `thm:alltime`: fixed
depth/data, independent Gaussian initialization, zero readout, globally bounded
and Lipschitz activation derivatives, a positive initial limiting feature-Gram
gap, and sufficiently small fixed labels. No label threshold may shrink with
width. Every initialized matrix is reused in both orientations throughout
training. No experiment was performed.

Read inputs: the complete `paper/proof_alltime.tex`,
`paper/proof_tracking.tex`, and `paper/results.tex`, and the Setting section of
`paper/main.tex`. No other study or route note was read. The mathematical proof
and conjecture-audit skills were applied.

Write \(\mathcal G_n\) for the paper's initial good event. Carrier quantities
below are set to zero off this event. On it, the dense fitting and tube bounds,
which precede population transfer in the paper, give

\[
 \rho(t)\le Ye^{-\kappa t},\qquad
 \max_{\ell,a}\|k_a^{(\ell)}(t)\|_2/\sqrt n\le B,
 \qquad t\ge0,                                      \tag{1}
\]

with deterministic width-independent \(B\). The carriers are
\(k_a^{(L)}=w\) and
\(k_a^{(\ell)}=(W^{(\ell+1)})^\top\delta_a^{(\ell+1)}\).
Define

\[
 h_{\ell a,n}(M,t)=\frac{\|k_a^{(\ell)}(t)
                    1_{\{|k_a^{(\ell)}(t)|>M\}}\|_2}{\sqrt n},
 \quad H_n(M,t)=\sum_\ell\max_a h_{\ell a,n}(M,t),
 \quad Z_n(M)=\int_0^\infty\rho(t)H_n(M,t)\,dt.         \tag{2}
\]

The desired quantitative replacement is
\(Z_n(M)\le Ce^{-cM^2}+a_n\), simultaneously for integer \(M\ge1\),
with an explicit width rate for \(a_n\). The separate dense-to-population
prediction error is not covered by a carrier estimate alone.

## 1. An annealed Gaussian bound would already improve tracking

Suppose one could prove, directly at finite width, that

\[
 \sup_{n,t,\ell,a,i}
 \mathbb E\big[1_{\mathcal G_n}
                  e^{c_0|k_{a,i}^{(\ell)}(t)|^2}\big]\le C_0. \tag{3}
\]

This is an unproved hypothesis for the stated nonlinear class. It does not
assert independence between neurons or independence from the initialized
matrices. It implies

\[
 \mathbb E Z_n(M)\le C e^{-cM^2}.                    \tag{4}
\]

Indeed, \(x^2 1_{|x|>M}\le C e^{-c_0M^2/2}e^{c_0x^2}\).
Average this estimate over coordinates, take square roots by Jensen, bound the
sample maximum by the sample sum, and use (1) inside the time integral. No time
supremum is put inside an exponential and no temporal independence is needed.

Fix \(0<\delta<1\). A countable union bound and Markov's inequality applied
to (4) give

\[
 \Pr\{\exists M\in\mathbb N_{\ge1}:
       Z_n(M)>C_\delta e^{-cM^2/2}\}\le\delta,
 \quad
 C_\delta=\frac C\delta\sum_{M=1}^{\infty}e^{-cM^2/2}.       \tag{5}
\]

Consequently the deterministic tracking argument in `proof_tracking.tex`
would yield, on \(\mathcal G_n\) and an event of failure probability at most
\(\delta\),

\[
 \sup_{t\ge0}d_n(\widehat\theta_{n,q}(t),\theta_n(t))
 \le C_\delta' q^{-2}\exp\{K\sqrt{\log(e+q)}\},
 \qquad\text{simultaneously for all }q\ge1.               \tag{6}
\]

To verify this implication, insert (5) in the paper's
`eq:at-cutoff-conclusion`; take
\(M=\lceil A\sqrt{\log(e+q)}\rceil\), with fixed \(A\) large enough,
and \(T=C\log(e+q)\). The tail term is then at most
\(C_\delta' q^{-2}e^{K\sqrt{\log(e+q)}}\), and the remaining terms and
the absorption condition are exactly those in the paper. The finite set of
orders below the absorption threshold is covered by the common physical bound.
The exponent constant \(K\) need not depend on \(\delta\).

Thus annealed finite-width sub-Gaussian carrier marginals would suffice for
confidence-dependent tracking with no width remainder. They would not by
themselves give a numerical rate for the paper's particular remainder with
fixed tail constants and event probability tending to one. A quantitative
empirical-tail estimate would give that stronger conclusion.

## 2. A quantitative empirical-tail reduction

Here is one sufficient estimate, weaker than an all-time supremum estimate.
Suppose that for all integer \(M\ge1\), all \(t\ge0\), and each carrier,

\[
 \left\|\big(h_{\ell a,n}(M,t)-C_0e^{-c_0M^2}\big)_+\right\|_{L^2(\Pr)}
 \le\eta_n,\qquad 0<\eta_n\le\tfrac12.                  \tag{7}
\]

Then there is a dense-only \(a_n\ge0\), independent of memory order, such
that simultaneously at all integer cutoffs

\[
 Z_n(M)\le Ce^{-c_0M^2}+a_n,
 \qquad
 \|a_n\|_{L^2(\Pr)}
 \le C\eta_n\{\log(e+1/\eta_n)\}^{1/4}.                 \tag{8}
\]

Proof. Choose an integer
\(J\le C\sqrt{\log(e+1/\eta_n)}\) with
\(C_0e^{-c_0J^2}\le\eta_n\), and set

\[
 U_{\ell a}(t)=\max_{1\le M\le J}
              \big(h_{\ell a,n}(M,t)-C_0e^{-c_0M^2}\big)_+.
\]

Since the square of a maximum of nonnegative numbers is at most the sum of
their squares, \(\|U_{\ell a}(t)\|_2\le\sqrt J\eta_n\).
For \(M>J\), monotonicity gives
\(h_{\ell a,n}(M,t)\le h_{\ell a,n}(J,t)
 \le\eta_n+U_{\ell a}(t)\).
Thus for every integer \(M\),

\[
 H_n(M,t)\le LC_0e^{-c_0M^2}+E_n(t),\qquad
 E_n(t)=L\eta_n+\sum_{\ell,a}U_{\ell a}(t),
 \quad \|E_n(t)\|_2\le C\sqrt J\eta_n.
\]

Take \(a_n=\int_0^\infty Ye^{-\kappa t}E_n(t)\,dt\).
Equations (1) and Minkowski's integral inequality prove (8). This argument
uses marginal-in-time information, not a union bound over a growing time grid.

## 3. A complete direct result for linear activations

Assume in this section only that \(\phi_\ell(z)=s_\ell z\), with fixed
slopes, and retain the other assumptions including the actual Gram gap. The
admissible data for this subclass must actually have that gap; for example
linear activations do not make linearly dependent training inputs independent.
No claim for nonlinear activations follows from this section.

**Proposition.** There are width-independent constants \(c,C>0\) and a
dense-only remainder satisfying

\[
 Z_n(M)\le Ce^{-cM^2}+a_n\quad(M\in\mathbb N_{\ge1}),\qquad
 \|a_n\|_2\le C n^{-1/2}\{\log(e+n)\}^{1/4}.             \tag{9}
\]

In particular, for every fixed confidence parameter \(\delta>0\), the
carrier-induced tracking remainder \(b_n=C\Phi(a_n)\) is
\(n^{-1/2+o(1)}\) with probability at least \(1-\delta\), in addition to
the good-event requirement. This is a bound on the carrier contribution,
not on the full dense-to-population error.

### Orthogonal symmetry survives the complete trained trajectory

For arbitrary deterministic \(O_1,\ldots,O_L\in O(n)\), transform

\[
 W^{(1)}\mapsto O_1W^{(1)},\qquad
 W^{(\ell)}\mapsto O_\ell W^{(\ell)}O_{\ell-1}^{\top},\qquad
 w\mapsto O_Lw.                                        \tag{10}
\]

The independent Gaussian initialization is invariant in law under (10).
Linear coordinate activations commute with every \(O_\ell\), so forward
and backward fields, including carriers, transform by their corresponding
\(O_\ell\). Each dense update equation has exactly the same equivariance.
Uniqueness of the finite-dimensional ODE transfers (10) to every time. The
event \(\mathcal G_n\) is invariant: its Frobenius, operator, sample-vector
norms and sample Gram are unchanged.

Therefore, for fixed \(t,\ell,a\), the carrier set to zero off
\(\mathcal G_n\) has a rotationally invariant distribution and norm at most
\(B\sqrt n\). Conditional on its radius it has uniform direction on the
sphere; at radius zero an independent uniform direction can be adjoined.
This conclusion uses the same initialized matrices in both directions and
throughout training. It does not condition a trained vector to be independent
of its initialized matrix.

### A spherical soft-tail estimate

For \(v\in\mathbb R^n\), define

\[
 F_M(v)=\left\{n^{-1}\sum_{i=1}^n(|v_i|-M)_+^2\right\}^{1/2}.
\]

It is \(n^{-1/2}\)-Lipschitz in Euclidean norm and monotone under an
increase of the absolute coordinates. Also

\[
 \|v1_{|v|>M}\|_2/\sqrt n\le2F_{M/2}(v).                \tag{11}
\]

Let \(G\sim N(0,I_n)\) and \(U=G/\|G\|_2\). For a carrier with uniform
direction and radius at most \(B\sqrt n\), its hard tail is stochastically
bounded by \(2F_{M/2}(B\sqrt nU)\). Put
\(\mu_M=\mathbb EF_{M/2}(BG)\). Gaussian exponential moments and Jensen
give \(\mu_M\le C e^{-cM^2}\), uniformly in \(n,M\).

Gaussian Poincare gives

\[
 \operatorname{Var}(F_{M/2}(BG))\le B^2/n.               \tag{12}
\]

For completeness, the form used is
\(\operatorname{Var}_\gamma f\le\mathbb E_\gamma|\nabla f|^2\).
It follows by taking
\(P_tf(x)=\mathbb E f(e^{-t}x+\sqrt{1-e^{-2t}}G)\), using Gaussian
integration by parts to obtain
\(-\frac d{dt}\mathbb E(P_tf)^2=2\mathbb E|\nabla P_tf|^2\), and
\(\nabla P_tf=e^{-t}P_t\nabla f\). Integrate over \(t\ge0\) and apply
Jensen. Smooth approximation extends this to Lipschitz functions. The
function in (12) has gradient norm at most \(B/\sqrt n\) almost everywhere,
including its zero region, so all hypotheses apply.

The normalization of the Gaussian vector costs only another \(n^{-1/2}\):

\[
 |F_{M/2}(B\sqrt nU)-F_{M/2}(BG)|
 \le B|1-\|G\|_2/\sqrt n|,
\]

\[
 \mathbb E|1-\|G\|_2/\sqrt n|^2
 \le\mathbb E|1-\|G\|_2^2/n|^2=2/n.                    \tag{13}
\]

Combining (11)--(13), and enlarging the deterministic Gaussian-tail
coefficient, proves (7) with \(\eta_n=C/\sqrt n\). Finite small widths are
absorbed by a larger constant. The reduction (8) proves (9).

Finally Chebyshev gives
\(a_n\le C\delta^{-1/2}n^{-1/2}\log(e+n)^{1/4}\)
with failure probability at most \(\delta\). The function
\(\Phi(u)=u\exp\{K\sqrt{\log(e+1/u)}\}\) is increasing on a sufficiently
small interval next to zero, as seen by differentiating. Inserting that bound
therefore gives the stated \(n^{-1/2+o(1)}\) carrier contribution for fixed
\(\delta\) and sufficiently large \(n\).

For linear activations, direct tracking can also exploit the absence of the
changed-gate product. Thus the proposition is primarily a fully justified
finite-width carrier benchmark, not evidence that the nonlinear bottleneck
has been solved.

## 4. The remaining nonlinear cavity estimate

Consider one initialized hidden matrix \(W_0\), with column \(c_i\), and
the backward response \(\delta(t)\) above that link. Run a cavity flow whose
initialized matrix has column \(i\) replaced by zero and whose residual and
all responses are recomputed from that modified initialization. Denote its
upper backward response by \(\delta^{[-i]}(t)\). This cavity is independent
of the removed Gaussian column. The exact identity is

\[
 c_i^\top\delta(t)=
 c_i^\top\delta^{[-i]}(t)+
 c_i^\top\{\delta(t)-\delta^{[-i]}(t)\}.                 \tag{14}
\]

On a cavity event determined without \(c_i\), the first term is conditionally
Gaussian at each time, with variance
\(\|\delta^{[-i]}(t)\|_2^2/n\). A cavity RMS bound therefore handles that
term. The required estimate on the second term is not supplied by the
paper. In particular, it is not legitimate to declare the original
\(\delta(t)\) independent of \(c_i\).

The trained part is an additional exact term. At the link from layer
\(\ell\) to layer \(\ell+1\),

\[
 ((W(t)-W_0)^\top\delta_a^{(\ell+1)}(t))_i
 =-\frac2m\sum_b\int_0^t r_b(s)h_{b,i}^{(\ell)}(s)
       \frac{\langle\delta_b^{(\ell+1)}(s),
                       \delta_a^{(\ell+1)}(t)\rangle}{n}\,ds. \tag{15}
\]

The coefficient in the inner product is bounded by \(CY^2\). Thus finite
width sub-Gaussian forward-coordinate bounds would control (15), and also
the trained readout, by Minkowski and the deterministic residual envelope.
They would not control the second term of (14). Forward initialized-matrix
actions require the corresponding row-deletion estimate.

A sufficient missing lemma is a simultaneous finite-width estimate, uniform
in time and neuron index, of the form

\[
 \|1_{\mathcal G_n}k_{a,i}^{(\ell)}(t)\|_{L^p}
 +\|1_{\mathcal G_n}h_{a,i}^{(\ell)}(t)\|_{L^p}
 \le C\sqrt p,\qquad p\ge2,                             \tag{16}
\]

with fixed \(C\), proved while retaining the dependence in (14). A direct
cavity proof would have to bound that feedback term, or separate its order-one
response correction and control the remaining fluctuation. For the stronger
fixed-constant remainder rate, one additionally needs (7), or a replacement
that controls integrated empirical tails quantitatively.

The elementary estimate
\(|c_i^\top(\delta-\delta^{[-i]})|
 \le\|c_i\|_2\|\delta-\delta^{[-i]}\|_2\)
does not close (16) with the available bounds. The original and cavity
initialized matrices differ by order one in Frobenius norm. Exploiting the
fact that their action is initially localized requires a stronger influence
estimate. Generic RMS comparison encounters exactly the changed-gate product
\([g(z)-g(z^{[-i]})]k^{[-i]}\) and therefore needs carrier control again.
Replacing it by a coordinate maximum produces width-dependent amplification
\(e^{C\sqrt{\log n}}\) even if a Gaussian maximum is already granted;
that amplification alone is not a width-independent sub-Gaussian marginal
bound. This is a failure of this crude estimate, not a no-go theorem for a
more precise cavity argument.

## 5. A concrete check against an invalid independence shortcut

Gaussian initialized matrices, bounded input coordinates and RMS bounds do
not imply Gaussian tails after an adapted transpose action. Let
\(W_{ij}\) be independent \(N(0,1/n)\), let \(J\) be independent uniform on
\(\{1,\ldots,n\}\), and put

\[
 u_i=\tanh(\sqrt nW_{iJ}).
\]

Then \(|u_i|\le1\), but

\[
 (W^\top u)_J
 =\frac1{\sqrt n}\sum_{i=1}^nG_i\tanh(G_i),
 \qquad G_i=\sqrt nW_{iJ}.
\]

The summands are independent, have finite variance and strictly positive
mean \(a=\mathbb E[G\tanh G]>0\). Hence
\((W^\top u)_J/\sqrt n\to a\) in probability, and for each fixed \(M\),

\[
 \|W^\top u\,1_{|W^\top u|>M}\|_2/\sqrt n
 \ge |(W^\top u)_J|/\sqrt n\;1_{|(W^\top u)_J|>M}
 \longrightarrow a\quad\text{from below in probability}.
\]

The normalized input RMS is bounded, the Gaussian matrix operator norm is
bounded with high probability, and randomizing \(J\) makes the output
coordinate-exchangeable. Nevertheless a single adapted coordinate carries
macroscopic tail energy. This is not a reachable neural training trajectory
and the \(\sqrt n\) inside the illustrative coordinate map is not a permitted
fixed activation. Its precise logical force is only that the Gaussian-matrix,
RMS, bounded-coordinate and exchangeability facts do not establish the needed
claim. Reachable-trajectory structure must enter a valid nonlinear proof.

## Frozen conclusion

The general nonlinear direct finite-width route is unresolved. Its leading
missing input is a finite-width, reused-matrix cavity/response estimate for
the adapted term in (14), with enough uniform integrability for (16), and
empirical concentration if a fixed-constant numerical remainder is desired.
Small total activity alone does not provide that estimate through the
available RMS comparison. The reductions (3)--(8) show exactly how such an
estimate would enter the paper, and (9) is a complete direct result for the
linear subclass. Neither proves an explicit width rate for the stated
nonlinear all-time population theorem.

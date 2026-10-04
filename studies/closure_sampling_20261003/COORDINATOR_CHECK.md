# Coordinator reconstruction of the reduced-order result

2026-10-03. Internal mathematical check, not a promotion review.
The coordinator read every scientific line of HISTORY_APPROXIMATION_ROUTE.md
at SHA-256 bfb51ee447eeb2128d5970ba400eff9964987bcdbc47d38bba21f65dc2e2240f.
The coordinator and source author had independently reached the central
weighted-derivative mechanism before exchanging it; this is a collaborative
reconstruction, not a blind check.

**Mathematical verdict: PASS.** The notation correction displays finite
normalization factors explicitly, as required by docs/notation.qmd, and
writes activation derivatives directly. No mathematical repair was needed.
The coordinator subsequently read the entire corrected source at SHA-256
46fc0584660bc45bda7cfeb6e4b6a63151559f79c96005ad3794799048d2477f.
Every vector RMS, squared RMS and history norm has the same normalization;
the derivative substitutions and diagnostic-source clarification change no
premise or conclusion. The PASS applies to that corrected frozen version.

## Inputs actually checked

The manuscript and book startup inputs retain their earlier complete-read
hashes; the exact model, projection/fitting proof and entire tracking proof
were reread for this continuation. The user explicitly authorized the relevant
prior compression proof/check files in dense_cutoff_population_rate_20261001.
The following complete source chains were read, repairing truncated tool output:

- Q_ORDER_RESULT.md and all of Q_ORDER_POSITIVE_ROUTE.md;
- Q_ORDER_INSERTION_CHECK.md and Q_ORDER_POSITIVE_PROBABILITY_CHECK.md;
- NONORTHOGONAL_DIRECT_ROUTE.md and NONORTHOGONAL_CHECK.md;
- FINITE_MIXED_MOMENT_ROUTE.md and FINITE_MIXED_MOMENT_CHECK.md;
- complete quotient and initialization-Gram arguments in Sections 1–2 of
  DATA_QUOTIENT_CLOCK.md and DATA_QUOTIENT_CHECK.md.

The last pair's subsequent inconsistent-label and persistent-clock results
are not dependencies. The previous regularity note is not needed for this
proof: prefix matching follows directly from the equations below.
The old conditional status of NONORTHOGONAL_DIRECT_ROUTE is respected:
its backward-history bound is unconditional on the fitting event; its
formerly missing finite carrier probability input is supplied by the later
Q_ORDER_POSITIVE_ROUTE, not silently inferred from the conditional note.

Verified source anchors include:

- Q_ORDER_POSITIVE_ROUTE.md:
  9026935501ce94886d9eee81c6d318d3f45ac2f526597be5de71b0989a959f27
- FINITE_MIXED_MOMENT_ROUTE.md:
  882fc64d4a0f3e98e630fdf9609ce911b1df21eee31fc9ac058be6058afdd571
- NONORTHOGONAL_DIRECT_ROUTE.md:
  5619965ad3ea85c186385951d07f59f3fe7e01c0f52b5b7710de65ba38896522
- paper/proof_tracking.tex:
  e75f8122ab0ed0bc5f8c0b5f979b7e1a1b779c94440367d62d9a98892d3e53be

No specialized external approximation theorem is needed. The squared
Legendre eigenvalue estimate is proved directly, rather than imported as a
higher-regularity assertion without checking its interface hypotheses.

## 1. The finite initialized object is unchanged

Let \(\phi=\tanh\). The model has two width-\(n\) hidden layers,
\(W^{(1)}\in\mathbb R^{n\times d}\), a reconstructed \(W\), and
readout \(w\), with prediction
\[
 f(t,x)=\frac1n w^\top\phi\bigl(W\phi(W^{(1)}x/\sqrt d)\bigr).
\]
The source retains the original Gaussian laws, zero readout, unhalved
squared loss, mobilities \((n,1,n)\), residual clock
\(\dot\tau=\rho,\ \tau(0)=1\), and both raw moment families.
Its reconstruction coefficient is exactly
\(-2(2j+1)/(mn\tau)\). The forward mode-zero initialization is the
initial feature, and all other memories vanish.

The proposed smaller model simply initializes the same equations at a
smaller predetermined number of modes. It is an autonomous finite ODE.
Neither the dense reference nor the larger closure supplies its future
states, responses or history coefficients. \(W_0\) remains fixed and
is applied together with its actual transpose.

## 2. Weighted second derivative, including the prefix

At a finite current clock endpoint \(A=\tau(t)\), write
\[
 \eta_A(\xi)=\xi(A-\xi),\qquad
 \mathcal L_A h=-\partial_\xi(\eta_A\partial_\xi h).
\]
The normalized Legendre basis obeys
\(\mathcal L_A e_j=j(j+1)e_j\). If \(h,h'\) agree at the prefix
join, two integrations by parts give
\[
 j(j+1)\langle h,e_j\rangle=\langle\mathcal L_Ah,e_j\rangle.
\]
Endpoint terms vanish because \(\eta_A\) vanishes there; the two interface
terms cancel because both the value and first derivative agree.
Consequently,
\[
 \frac{\|(I-\Pi_q^A)h\|_{L^2}}{\sqrt n}
 \le \frac{\|\mathcal L_Ah\|_{L^2}}{\sqrt n\,q(q+1)}.
\]
A jump in the second derivative does not create an interface point mass
in this single application of \(\mathcal L_A\).

For actual closure histories put \(c_a=r_a/\rho\) and
\(k_a=W^\top\delta_a^{(2)}\), where
\(\delta_a^{(2)}=w\odot\phi'(z_a^{(2)})\).
Primes in the following calculation denote its own clock derivative.
The first-layer equation gives
\[
 (z_a^{(1)})'
 =-\frac2m\sum_b G_{ab}c_b\,
      \phi'(z_b^{(1)})\odot k_b.
\]
All backward fields vanish initially because \(w(0)=0\). Thus this
derivative and \(h_a^{(1)\prime}\) equal zero at \(1+\), agreeing with
the constant prefix at \(1-\). This verifies the actual interface
hypothesis, rather than assuming every history is globally smooth.

## 3. The derivative estimate does not differentiate the defect

Let \(K_q=\sup_{t,a}\|k_a(t)\|_\infty\), finite from the existing
all-order RMS bounds. The original fitting theorem gives, before any
approximation argument,
\[
 \|W\|_{\rm op}\le C,\quad
 \frac{\|W_t\|_F}{\rho}\le CY,\quad
 \frac{\|z_{a,t}^{(\ell)}\|_2}{\sqrt n\,\rho}\le CY,\quad
 \frac{\|w_t\|_2}{\sqrt n\,\rho}\le2,\quad
 \|w\|_\infty\le CY.
\]
The last estimate uses bounded tanh in the readout update. Therefore
\[
 \frac{\|\delta_a^{(2)\prime}\|_2+\|k_a'\|_2}{\sqrt n}\le C
\]
by differentiating \(w\odot\phi'(z_a^{(2)})\) and
\(W^\top\delta_a^{(2)}\) once. This uses \(W_t\), whose speed was
already proved, and never \(W_{tt}\) or the derivative of the closure
velocity defect.

The sample residual equation supplies \(\|c_t\|_m\le C\), hence
\(\|c'\|_m\le C/\rho\). Differentiating the first-layer equation and
the activation once more gives
\[
 \frac{\|h_a^{(1)\prime}\|_2}{\sqrt n}\le CY,\qquad
 \frac{\|h_a^{(1)\prime\prime}\|_2}{\sqrt n}
 \le C\left(\frac Y\rho+1+YK_q\right).
\]
Every coordinatewise product here is justified. For example,
\[
 \frac{\|(z_a^{(1)\prime})^2\|_2}{\sqrt n}
 \le\|z_a^{(1)\prime}\|_\infty
       \frac{\|z_a^{(1)\prime}\|_2}{\sqrt n}
 \le CYK_q.
\]
No unproved fourth moment of a response sensitivity is being used.

For \(s\le t\), the residual tail estimate gives
\[
 \eta_A(\tau(s))\le \frac A\kappa\rho(s).
\]
Thus its square cancels the apparent inverse-residual square in the
second derivative. Since \(d\xi=\rho(s)\,ds\),
\[
 \frac1n\|\mathcal L_Ah_a^{(1)}\|_{L^2(0,A)}^2
 \le C\int_0^t
  [Y^2+(1+YK_q)^2\rho(s)^2]\rho(s)\,ds
 \le CY^3(1+YK_q)^2.
\]
This is uniform in the finite terminal time. It assumes no differentiability
at the limiting endpoint \(\tau(\infty)\).

## 4. The absolute source really has a third order

The top backward history \(b_a=(r_a/\rho)\delta_a^{(2)}\) satisfies
\[
 \frac{\|b_a\|_2}{\sqrt n}\le CY,\qquad
 \frac{\|\dot b_a\|_2}{\sqrt n}\le C(Y+\rho).
\]
Freeze after \(T=2\log q/\kappa\), and use the first weighted
Legendre bound and the residual tail. This yields, including \(q=1\),
\[
 \frac{\|(I-\Pi_q^A)b_a\|_{L^2}}{\sqrt n}
 \le CY\,q^{-1}\sqrt{\log(e+q)}.
\]
The history is continuous at both the initial join and the freezing time.
It need not have a second derivative in \(L^2\).

The exact growing-projection-energy identity bounds the time integral of
the norm of the velocity defect by the product of the two history tails.
It is stronger than a bound on only the signed reconstruction discrepancy.
Consequently
\[
 \epsilon_q:=\int_0^\infty\|E_2(t)\|_Fdt
 \le CY^{5/2}(1+YK_q)q^{-3}\sqrt{\log(e+q)}.
\]
Increasing finite terminal times is valid because the left side is
nondecreasing and the right side has a common bound.

## 5. The apparently circular carrier dependence is absorbable

Let \(D_{n,q}\) be the supremum over physical time of the manuscript's
normalized parameter distance to the same initialized dense run.
The all-order fitting bounds first establish that \(D_{n,q}<\infty\).

On the previously proved dense maximum event, its carriers and readout
are bounded by \(M_n=1+C_0Y\sqrt{\log(e+n)}\).
Top response subtraction uses the bounded dense readout coordinates:
\[
 \frac{\|\widehat\delta_a^{(2)}-\delta_{D,a}^{(2)}\|_2}{\sqrt n}
 \le C D_{n,q}.
\]
Carrier subtraction then gives the same RMS bound. Conversion to a
coordinate maximum costs precisely \(\sqrt n\):
\[
 K_q\le M_n+C\sqrt nD_{n,q}.
\]
This is a same-physical-time estimate. No equality of the history clocks
or ratio of the residuals is assumed.

One-reference damping gives \(D_{n,q}\le A_{M_n}\epsilon_q\), where
\(A_{M_n}\le C\exp(K\sqrt{\log(e+n)})\).
The dense carrier tail is exactly zero on the maximum event. Substitution
leaves one linear feedback term with coefficient
\[
 C A_{M_n}Y^{7/2}\sqrt n\,q^{-3}\sqrt{\log(e+q)}.
\]
At \(q_n=\lceil n^{1/6}\exp(a\sqrt{\log(e+n)})\rceil\), \(3a>K\),
this coefficient tends to zero. It can be absorbed because \(D_{n,q}\)
was finite already; no prior smallness of that discrepancy is assumed.
The remaining source is at most \(C/\sqrt n\).
The previous dense maximum theorem supplies the probability event under
the existing assumptions, so it is not an added moment or response hypothesis.

## 6. Original closure, bias, endpoint and count

The function \(q^{-3}\sqrt{\log(e+q)}\) decreases, so the same bound
holds simultaneously for every \(q\ge q_n\). For an original order \(q\),
choose \(p=\min(q,q_n)\). If \(q\le q_n\), the systems are identical.
Otherwise the triangle inequality through the same dense run gives
\[
 \mathcal E_\mu(\widehat f_{n,p},\widehat f_{n,q})
 \le 2C_\mu/\sqrt n.
\]
This is the full realized-model error, not concentration around an
unspecified center. It contains all deterministic truncation bias.
No population target and no independently sampled mixer are introduced.

The manuscript's pointwise forward estimate has factor
\(C(1+\|x\|/\sqrt d)\), so a finite second query moment suffices even
with the time supremum inside the integral. Both closures already converge;
the supremum bound therefore includes their fitted limits. The probabilistic
statement is for each sufficiently large width at fixed confidence, not a
single event across infinitely many independently drawn widths.

The moving count is \(2mnp+n(d+1)+1\le n^{7/6+o(1)}\).
For the previous \(q=n^{1/4+o(1)}\) baseline, this saves a power
\(n^{1/12-o(1)}\) relative to \(n^{5/4}\). Any fixed saving exponent
strictly below \(1/12\) is available for sufficiently large widths.
The exact fixed mixer still costs \(n^2\) storage and dense forward/transpose
applications. Neither wall-clock nor total-storage compression is proved.

## 7. Separate neuron-sampling calculation

The coordinator also read all of NEURON_SAMPLING_ROUTE.md at hash
1a4c715d167ceca5979b56902e57edd18e0c199d22e0567c0d70a471cf1c5a41.
Its Gaussian projections, conditional covariance normalizations,
Horvitz--Thompson variance, retained-row bound, query-coefficient variance
bound, and conditional stratified quadrature calculation reconstruct correctly.

In particular, after conditioning on initialized training fields
\(Z=W_0H\), the unused Gaussian matrix component has covariance
\(P_{\operatorname{col}(H)^\perp}/n\) row by row. Multiplication by
a training-field-measurable response leaves the explicit adjoint variance
claimed there. For its separate unseen-query example, Cauchy--Schwarz and
the positive conditional tanh variance give the \(c/N\) conditional
mean-square error in the sampled initial kernel coefficient.

These are restricted sampling obstructions. A derivative mean-square lower
bound is not an all-time trajectory lower bound, and a strong hidden-vector
obstruction is not automatically a prediction obstruction. The source keeps
both distinctions explicit. Its hypothetical fixed-dimensional stratification
gain is conditional, not used in the positive theorem. The returned positive
construction instead retains all neurons and changes only the number of
history moments.

No training experiment, formal proof assistant, manuscript edit, Git mutation
or external publication was part of this check.

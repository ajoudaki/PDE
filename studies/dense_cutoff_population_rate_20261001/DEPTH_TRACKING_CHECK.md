# Internal reconstruction of the arbitrary-depth deterministic comparison

2026-10-03. Coordinator check. This is an internal study reconstruction,
not a promotion review. Read the complete DEPTH_TRACKING_ROUTE.md at
SHA-256 90b9c19f40def4f2d60f11594789ce28e0e988238082fde53bc0f413aa21c134,
and reconstructed the result against the current manuscript's fitting,
projection, speed, and damping proofs. No experiment or manuscript edit.

**Verdict: PASS as a deterministic implication.** It assumes the stated
actual dense all-layer maximum M. It does not prove that event's
probability. In particular the unconditional arbitrary-depth near-quarter
theorem needs a separate finite-network carrier estimate.

## 1. Exact model and parameter distance

The source keeps the block mobilities (n,1,...,1,n), the canonical initial
Gaussian scaling, zero readout, and the original autonomous Legendre
closure. The closure clock is its own residual RMS, with the unit prefix.
The discrepancy d_n uses first-layer/readout normalization sqrt(n) and
unscaled Frobenius hidden-matrix discrepancy. No dense source is fed into
the actual closure.

The activation assumptions are bounded slopes and globally Lipschitz
derivatives. These are exactly enough for the deterministic physical
bounds and the a.e. derivative estimates; bounded values or third
derivatives are not used in this part.

## 2. Reconstruction of the comparison

The manuscript's exact projection-energy identity gives, for each layer,
the product of the clock-L2 forward and backward projection errors as an
upper bound for the accumulated absolute matrix defect. This is not a
bound merely on signed reconstruction error.

The all-order fitting and speed theorem yields
||dot(hat h)||/sqrt(n)<=CY hat rho. Thus the clock derivative of
the forward history has RMS at most CY, and its physical clock interval
has length CY. The weighted Legendre error is CY^(3/2)/q.

If every dense carrier coordinate is bounded by M, backward subtraction
has bound C(1+M)d_n. The M factors add through fixed depth; they do not
multiply in a power M^L. The residual difference is damped by the closure
Gram, which is already known positive before comparison. Integrating this
damping inequality and subtracting parameter equations gives
\[
 D\le A_M\epsilon,\qquad A_M=Ce^{C_1YM}.
\]
Here D=sup_t d_n, and epsilon is the total absolute closure defect.
Both are finite by the prior all-order physical estimates, so this step
does not bootstrap their existence.

## 3. Dense response recorded in the closure's clock

The proof history is
\[
 \widetilde b_a^{(\ell)}(t)
 =\widehat c_a(t)\delta_{D,a}^{(\ell)}(t),
 \qquad \widehat c_a=\widehat r_a/\widehat\rho.
\]
It has zero prefix because the dense readout starts at zero. It is not
used in the closure update. Dense backward differentiation with the
actual dense maximum gives
||dot delta_D||/sqrt(n)<=C(1+M)rho_D. Thus
||dot tilde b||/sqrt(n)<=C[Y+(1+M)rho_D].

Freeze the proof history at physical time T. Its remaining clock-L2
error is Ce^(-kappa T/2), since the closure's own remaining clock mass
is exponentially small. For terminal clock A=hat tau(t),
\[
 \frac{\widehat\tau(s)[A-\widehat\tau(s)]}
          {\widehat\rho(s)}\le C
\]
for s<=t. This follows from the closure's own residual decay:
A-hat tau(s)<=hat rho(s)/kappa. The inverse clock speed therefore
cancels before any dense derivative enters. In particular no bound on
rho_D/hat rho is assumed.

The frozen weighted derivative energy is at most C[T+(1+M)^2].
Projection gives C[(1+M+sqrt T)/q+e^(-kappa T/2)].
The actual backward history and the proof history have the same hat c,
so their clock-L2 discrepancy is at most C(1+M)D directly.

Combining with the forward factor, then choosing T=2 log(q)/kappa,
gives
\[
 \epsilon\le
 C\frac{1+M+\sqrt{\log(e+q)}}{q^2}
       +\frac{C(1+M)A_M}{q}\epsilon.
\]
The assumed q>=C(1+M)A_M absorbs the last term. This proves the
claimed one-amplification bound. The source's general schedule checks
both the absorption threshold and the numerator logarithm.

## 4. Endpoints, test inputs, and limits

The physical paths converge independently of this comparison, so the
time supremum includes their limits. Forward subtraction with global
slope bounds gives prediction error at x bounded by
C(1+||x||/sqrt(d))D. Hence finite second moment of the test law is
sufficient, with the supremum inside its integral.

For M=c sqrt(log(e+n)), q=ceil(n^(1/4)exp(a sqrt(log(e+n))))
with a>C_1Yc/2 eventually satisfies the absorption threshold and gives
strict C_mu/sqrt(n) error. All constants may depend on fixed depth,
data, activation bounds and the initial Gram. They do not depend on
width, memory order or physical time. A fixed-depth statement does not
mean the constants are uniform as depth increases.

The integrated-envelope refinement is the same calculation with
time-dependent M(t): it changes the integrating factor to
exp(C int rho_D(1+M)), the clock-L2 mismatch coefficient to the
displayed B_2, and derivative energy to T+B_3^2. No averaged-neuron
moment can be substituted into that refinement without a further
product estimate. The source correctly withholds such a substitution.

No mathematical correction was required. The author was asked to repair
stripped inline-math delimiters before the final source freeze. A
formatting-only source version preserves this verdict.

The corrected source has SHA-256
f06f6c1acc75c1841f7898dcccb3a88a1f8b7724c53f8dbbe688f46305162e0c.
The correction restores inline mathematical delimiters without changing
the formulas, quantifiers or proof.

## 5. A simultaneous-in-order corollary

There is also a convenient way to state the eventual finite-width
consequence for every memory order on one event. This is a coordinator
corollary of the checked source, rather than an additional probabilistic
assumption. Suppose its dense carrier envelope is
\(M=c\sqrt{\log(e+n)}\), with fixed \(c\).
Write \(A_M=C e^{K_0M}\) for the source's damping constant and
\(q_0=C_0(1+M)A_M\) for its absorption threshold.
The all-order physical tube supplies \(D_{n,q}\le C\) for every
\(q\ge1\), independently of width and order.

For \(q\ge q_0\), the source proves
\[
 D_{n,q}\le
 C A_M\frac{1+M+\sqrt{\log(e+q)}}{q^2}.
\]
For any fixed \(\varepsilon>0\),
\(1+M\le C_\varepsilon e^{\varepsilon\sqrt{\log(e+n)}}\)
and \(\sqrt{\log(e+q)}\ge1\). Thus this range has a bound of
the form
\[
 D_{n,q}\le C e^{K\sqrt{\log(e+n)}}
                 \frac{\sqrt{\log(e+q)}}{q^2}.
 \tag{C1}
\]
For \(q<q_0\), choose \(K>2K_0c\), increasing it further if
needed. Then
\[
 q_0^2\le C(1+M)^2e^{2K_0M}
          \le C'e^{K\sqrt{\log(e+n)}}.
\]
After increasing the fixed prefactor in (C1), its right side is at
least the physical bound \(C\) throughout this lower-order range.
This proves (C1) for all positive integer orders, with constants
independent of \(n,q,t\). The same event controls all these orders
because both the paper's physical tube and the dense carrier envelope
are independent of the chosen order.

The whole-input prediction estimate in the source transfers (C1) to
the norm with the physical-time supremum inside the query integral,
for every fixed query law with finite second moment. Finally,
\(q_n=\lceil n^{1/4}e^{a\sqrt{\log(e+n)}}\rceil\), with
\(a>K/2\), gives strict \(C_\mu n^{-1/2}\) error: the remaining
factor is bounded by
\(C\sqrt{\log(e+n)}e^{-(2a-K)\sqrt{\log(e+n)}}\).
This corollary still requires the separately proved probability of the
dense carrier event; it does not supply that event.

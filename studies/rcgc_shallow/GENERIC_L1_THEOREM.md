# Generic one-hidden-layer theorem from the calculus

**Status:** proved after independent hostile reconstruction and repair.

## 1. Theorem

Let \(\phi\in\mathcal A_{\rm sh}\):

\[
 \phi\in C^2(\mathbb R),\qquad
 \|\phi'\|_\infty+\|\phi''\|_\infty<\infty,qquad
 |\phi(u)|\le C_\phi(1+|u|).                           \tag{1.1}
\]

For the canonical one-hidden-layer model

\[
 f_n=\frac1n\sum_{i=1}^n A_i\phi(u_i),                 \tag{1.2}
\]

train both blocks in the endpoint normalized Hilbert metric under physical
full-MSE flow with learning-rate coefficient \(\eta\ge0\). On the immutable
mark space

\[
 (\Omega,\gamma_2),\qquad (a_0,u_0)\sim N(0,I_2),      \tag{1.3}
\]

the autonomous limiting IDE/ODE is

\[
\boxed{
\begin{aligned}
 \dot A&=2\eta e\,\phi(U),\\
 \dot U&=2\eta e\,A\phi'(U),\\
 K&=\mathbb E\{\phi(U)^2+A^2\phi'(U)^2\},\\
 \dot e&=-2\eta eK,
\end{aligned}}                                         \tag{1.4}
\]

with \((A,U,e)(0)=(a_0,u_0,y_\star)\). It has a unique global canonical
solution. It is autonomous and restartable from the full marked population
state \((A(\cdot),U(\cdot),e)\), subject to
\(e+\mathbb E[A\phi(U)]=y_\star\), and

\[
 f=\mathbb E[A\phi(U)]=y_\star-e,qquad \mathcal L=e^2.\tag{1.5}
\]

For every finite \(T\),

\[
 \sup_{t\le T}
 (|f_n-f|+|K_n-K|+|e_n-e|+|e_n^2-e^2|)
 \xrightarrow{\mathbb P}0.                            \tag{1.6}
\]

This is one theorem over the activation class (1.1), not an arctangent or
polynomial specialization.

## 2. Exact characteristic compilation

The calculus's `Forward`, `Reverse`, and `Gradient` rules give feature time

\[
 {d\widehat A\over ds}=\phi(\widehat U),\qquad
 {d\widehat U\over ds}=\widehat A\phi'(\widehat U),   \tag{2.1}
\]

independently for every source mark \((a_0,u_0)\). Assumption (1.1) gives

\[
 {d\over ds}(1+|\widehat A|+|\widehat U|)
 \le C_\phi(1+|\widehat A|+|\widehat U|),             \tag{2.2}
\]

so (2.1) has a unique global solution and, on \(|s|\le S\),

\[
 1+|\widehat A_s|+|\widehat U_s|
 \le C_{S,\phi}(1+|a_0|+|u_0|).                       \tag{2.3}
\]

Define

\[
 F(s)=\mathbb E[\widehat A_s\phi(\widehat U_s)].      \tag{2.4}
\]

Differentiation under the expectation is justified by (2.3), Gaussian
moments, and the bounded derivatives in (1.1). It gives the exact calculus
identity

\[
 F'(s)=\mathbb E\{\phi(\widehat U_s)^2+
 \widehat A_s^2\phi'(\widehat U_s)^2\}
 =:K(s)\ge0.                                          \tag{2.5}
\]

Independence and centering of \(a_0\) give \(F(0)=0\), for an arbitrary
admissible activation.

`ScalarLossClock` now emits the scalar equation

\[
 \dot s(t)=2\eta\{y_\star-F(s(t))\},\qquad s(0)=0.    \tag{2.6}
\]

Since \(F\) is nondecreasing, \(s(t)\) cannot cross a root of
\(F(s)=y_\star\). Equivalently, with \(e(t)=y_\star-F(s(t))\),

\[
 e(t)=y_\star\exp\!\left\{-2\eta\int_0^tK(s(\tau))\,d\tau\right\}. \tag{2.6a}
\]

Thus the residual sign is preserved, including when no root exists, and

\[
 |\dot s(t)|\le2\eta|y_\star|,qquad
 |s(t)|\le2\eta|y_\star|t.                            \tag{2.7}
\]

If no root exists in that direction, the same inequality holds forever.
Thus (2.6) is global and unique. Put

\[
 A(t)=\widehat A_{s(t)},\quad U(t)=\widehat U_{s(t)},
 \quad e(t)=y_\star-F(s(t)).                           \tag{2.8}
\]

The chain rule gives (1.4)--(1.5). Conversely every solution of (1.4)
generates the clock \(s(t)=2\eta\int_0^t e\) and, by uniqueness of (2.1),
has the form (2.8). Restarting at time \(\tau\) retains the marked fields
\(\omega\mapsto(A_\tau(\omega),U_\tau(\omega))\), the residual \(e_\tau\),
and the consistency invariant. The scalar tuple \((f,K,e)\) alone is not a
restart state. The clock is proof scaffolding, not hidden final state.

## 3. Uniform characteristic law

For iid marks \((a_i,u_i)\), let
\((\widehat A_{i,s},\widehat U_{i,s})\) solve (2.1), and define

\[
 F_n(s)=\frac1n\sum_i
 \widehat A_{i,s}\phi(\widehat U_{i,s}),              \tag{3.1}
\]

\[
 K_n(s)=\frac1n\sum_i
 \{\phi(\widehat U_{i,s})^2+
 \widehat A_{i,s}^2\phi'(\widehat U_{i,s})^2\}.       \tag{3.2}
\]

### Lemma 3.1

For every finite \(S\),

\[
 \sup_{|s|\le S}\{|F_n(s)-F(s)|+|K_n(s)-K(s)|\}
 \longrightarrow0                                    \tag{3.3}
\]

almost surely.

#### Proof

Equation (2.3) bounds both integrands by
\(C_S(1+|a_0|+|u_0|)^2\), an integrable envelope. Differentiating the first
integrand gives the second. If that second integrand is \(H_s\), then

\[
 H_s'=4A_s\phi(U_s)\phi'(U_s)^2
 +2A_s^3\phi'(U_s)^2\phi''(U_s).
\]

Thus its derivative uses only \(\phi',\phi''\) and (2.1), and is bounded on
\([-S,S]\) by an integrable cubic polynomial in
\(1+|a_0|+|u_0|\). Hence both indexed families are pointwise Lipschitz in
\(s\) with an integrable random Lipschitz constant.

Apply the strong law on a finite rational \(\delta\)-net of ([-S,S]).
The empirical averages of the envelope and Lipschitz constant also converge
by the strong law. Letting \(\delta\downarrow0\) proves uniform convergence
for each family. \(\square\)

This is the shallow instance of the calculus's source-semantic and
uniformization rules: no fixed-order Taylor expansion is used.

## 4. Finite-width physical clock and convergence

The exact finite particle flow has the representation

\[
 A_i(t)=\widehat A_{i,s_n(t)},\qquad
 u_i(t)=\widehat U_{i,s_n(t)},                          \tag{4.1}
\]

where

\[
 \dot s_n=2\eta\{y_\star-F_n(s_n)\},\qquad s_n(0)=0. \tag{4.2}
\]

This includes the random initial output:
\(e_n(0)=y_\star-F_n(0)\).
On the high-probability event

\[
 |F_n(0)|\le1,\qquad
 \sup_{|s|\le S_T}\{|F_n(s)-F(s)|+|K_n(s)-K(s)|\}\le1,
 \quad S_T=2\eta(|y_\star|+1)T+1,                      \tag{4.3}
\]

the scalar vector fields in (2.6) and (4.2) are evaluated inside a common
compact interval. There \(F\) is Lipschitz with constant
\(\sup K<\infty\). Adding and subtracting \(F(s_n)\), Grönwall gives

\[
 \sup_{t\le T}|s_n(t)-s(t)|
 \le C_T\sup_{|s|\le S_T}|F_n(s)-F(s)|\longrightarrow0.\tag{4.4}
\]

The exit assumed in (4.3) cannot occur. Indeed, \(F_n'=K_n\ge0\) exactly,
not merely asymptotically. The scalar flow therefore moves monotonically
toward the (possibly absent) level \(F_n=y_\star\), cannot cross that level,
and

\[
 |y_\star-F_n(s_n(t))|
 \le |y_\star-F_n(0)|\le |y_\star|+1.                 \tag{4.4a}
\]

Consequently \(|s_n(t)|\le2\eta(|y_\star|+1)T<S_T\) for
\(0\le t\le T\). This pathwise monotonicity argument avoids using the
limiting function \(F\) to control an as-yet-unlocalized finite-width clock.

Now

\[
 f_n(t)=F_n(s_n(t)),\qquad K_n(t)=K_n(s_n(t)),          \tag{4.5}
\]

and (3.3)--(4.4), together with uniform continuity of \(F,K\) on the common
compact interval, prove (1.6). Residual and loss follow from
\(e_n=y_\star-f_n\).

Under the nested common-iid coupling the convergence is almost sure. Since
all four limits are deterministic, this implies the intrinsic convergence
in probability asserted in (1.6) for the original width laws.

## 5. Promotion audit

- G0: exact characteristic and raw kernel identities, proved.
- G1: the immutable source is the explicit two-Gaussian mark law, proved.
- G2: global physical solution, uniqueness, and restart, proved.
- G3: every finite time discretization is an iid mark program, proved as a
  special case of the same characteristic semantics.
- G4: Lemma 3.1 and scalar-clock stability are mesh-free uniformization
  certificates, not fixed-grid convergence.
- G5: equation (1.6), proved.

The proof has not used a closed form of any activation. Its only activation
inputs are the declared constants in (1.1). The hostile reconstruction
checked both the finite-clock localization and the integrable Lipschitz
envelope for \(K_s\); it also fixed the precise restart state and the
requirement \(\eta\ge0\).

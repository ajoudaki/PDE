# An initialization-compiled physical-time Legendre variant

Scoped proof-route note, 2026-10-09. This is an internally derived construction,
not a change to the paper and not an independent review. Scientific inputs were
the setup in `paper/compact.tex`, the fitting and signed-stability arguments in
`paper/compact_fitting.tex`, the public source proposition in
`paper/compact_foundations.tex`, the current Legendre construction and comparison
in `paper/compact_legendre.tex`, and the initialization-only coefficient compiler
in `paper/compact_selected.tex`. No other study's findings were consulted.

The conclusion concerns a **modified construction**. It does not establish that
the current residual-clock, two-sided Legendre-memory equations work with
polylogarithmic order.

## A concrete alternative with a direct nonlinear comparison

Keep exactly the paper's network, data, mobilities, activations, label cap and
realized initialization. Put \(\lambda=\gamma/m\),
\(\ell_n=\log(en)\), and \(T=32\ell_n/\lambda\). For every training sample
\(a\) and hidden interface \(j=2,\ldots,L\), compile from initialization a
real vector-valued polynomial

\[
 H_a^{(j-1)}(t)=\sum_{k=0}^{q-1} c_{a,k}^{(j-1)}
                         P_k(2t/T-1),\qquad 0\le t\le T,
\]

whose coefficient vectors belong to \(\mathbb R^n\), and which satisfies

\[
 \max_{a,j}\sup_{0\le t\le T}
 \frac{\|H_a^{(j-1)}(t)-h_{D,a}^{(j-1)}(t)\|_2}{\sqrt n}
 \le \eta.
 \tag{1}
\]

Here the subscript \(D\) identifies the coupled dense trajectory. The
initialization-only compiler in the paper supplies the coefficient vectors
using finitely many dense ODE derivatives at time zero; it does not take a
later dense state as input. Its preprocessing cost is not bounded.

Extend \(H_a^{(j-1)}\) constantly after \(T\). This is a real-time
evaluation rule, not an assertion that the extension is analytic. Retain the
full first-layer matrix \(\widehat W^{(1)}\), full readout
\(\widehat w\), a scalar clock \(\tau\), and only the backward moments
\(\bar\delta_{a,k}^{(j)}\in\mathbb R^n\). Reconstruct hidden matrices by

\[
 \widehat W^{(j)}=W_0^{(j)}-
 \frac{2}{mn}\sum_{a=1}^m\sum_{k=0}^{q-1}
             \bar\delta_{a,k}^{(j)}c_{a,k}^{(j-1)\top}.
 \tag{2}
\]

Use those matrices in the ordinary nonlinear forward and backward passes,
including \(\widehat f=\widehat w^\top\widehat h^{(L)}/n\),
\(\widehat r_a=\widehat f(x_a)-y_a\), and the original residual-free
responses \(\widehat\delta_a^{(j)}\). The loss remains
\(m^{-1}\sum_a\widehat r_a^2\).

For a bounded autonomous clock, initialize \(\tau=0\) and evolve
\(\dot\tau=1-\tau\). Define the locally Lipschitz evaluation map

\[
 s(\tau)=\begin{cases}
 0,&\tau\le0,\\
 -\log(1-\tau),&0<\tau<1-e^{-T},\\
 T,&\tau\ge1-e^{-T}.
 \end{cases}
\]

On the generated trajectory, \(s(\tau(t))=\min(t,T)\). Evolve

\[
 \begin{aligned}
 \dot{\bar\delta}_{a,k}^{(j)}
   &=\widehat r_a\widehat\delta_a^{(j)}
                         P_k(2s(\tau)/T-1),\\
 \dot{\widehat W}^{(1)}
   &=-\frac2m\sum_a\widehat r_a\widehat\delta_a^{(1)}v_a^\top,\\
 \dot{\widehat w}
   &=-\frac2m\sum_a\widehat r_a\widehat h_a^{(L)}.
 \end{aligned}
 \tag{3}
\]

Initially all backward moments and the readout are zero, and
\(\widehat W^{(1)}=W_0^{(1)}\). Equations (2)-(3) give an autonomous,
locally Lipschitz, finite-dimensional system. No residual division occurs.
The clock continues at a zero residual, but all reconstructed physical
parameters remain stationary there.

The exact storage, excluding data, is

\[
 S_{\rm moving}=n(d+1)+1+(L-1)mnq,
 \qquad
 S_{\rm fixed}=(L-1)n^2+(L-1)mnq.
 \tag{4}
\]

The extra fixed coefficient vectors and their initialization-only compilation
are material changes from the original inventory. The construction also
replaces residual-clock histories by physical-time polynomial factors and
removes the evolving forward moments. It retains nonlinear feature evaluation
and nonlinear feedback through residuals and backward responses.

## Fitting does not require a small approximation error

Let \(H=\max_j\sqrt{Q^{(j)}_{11}}\),
\(s=\max\{1,\sup_{j,\mathbb R}|\phi'_j|\}\), and
\(D_j=s(9s)^{L-j}\), as in the paper's real fitting proof. Assume
\(\eta\le H\). The dense fitting lemma and (1) give
\(\|H_a^{(j)}(t)\|/\sqrt n\le3H\) for every real time, including
the constant continuation.

Write \(\rho=\|\widehat r\|_2/\sqrt m\). On the tube with operator
norms at most nine, feature RMS at most \(2H\), and readout RMS at most
\(R=8Y/\sqrt\lambda\), the backward responses have RMS at most
\(D_jR\). Differentiating (2) gives

\[
 \dot{\widehat W}^{(j)}
   =-\frac2{mn}\sum_a\widehat r_a\widehat\delta_a^{(j)}
                                          H_a^{(j-1)}(t)^\top.
 \tag{5}
\]

Let \(\mathcal F\) be the full dense negative-gradient vector field at the
reconstructed parameters, in mobility coordinates
\((W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)\).
Then the exact physical defect is

\[
 \mathcal E_j=\frac2{mn}\sum_a\widehat r_a
 \widehat\delta_a^{(j)}
 [\widehat h_a^{(j-1)}-H_a^{(j-1)}(t)]^\top.
 \tag{6}
\]

With \(B=10H\sum_{j=2}^L D_j\), sample Cauchy-Schwarz and
\(\|\widehat h-H\|/\sqrt n\le5H\) give
\(\|\mathcal E\|_{\rm par}\le BR\rho\). The readout Gram gap
on the stopped tube gives \(\|\mathcal F\|_{\rm par}\ge\sqrt\lambda\rho\).
Because the actual parameter velocity is \(\mathcal F+\mathcal E\),

\[
 -\frac{d}{dt}\rho^2
 =\|\mathcal F\|_{\rm par}^2+\langle\mathcal F,\mathcal E\rangle_{
 \rm par}
 \ge\left(1-\frac{BR}{\sqrt\lambda}\right)
                  \|\mathcal F\|_{\rm par}^2.
 \tag{7}
\]

Here \(B\le\beta^{6L}\): use \(H\le\beta^{2L}\),
\(D_j\le\beta^{2L}\), and \(10L\le\beta^{2L}\). Thus the original
cap \(Y/\lambda\le\beta^{-30L}\) ensures
\(BR/\sqrt\lambda=8B(Y/\lambda)<1/2\). Consequently

\[
 \rho(t)\le Ye^{-\lambda t/4},\qquad
 \int_0^\infty\rho\le4Y/\lambda,\qquad
 \int_0^\infty\|\mathcal F\|_{\rm par}\le4Y/\sqrt\lambda.
 \tag{8}
\]

For the last bound, (7) implies
\(\int\|\mathcal F\|^2/\rho\le4Y\), and Cauchy-Schwarz with
\(\int\rho\le4Y/\lambda\) applies. The readout has no defect, so its
RMS stays below \(R/2\). The direct velocity bounds from (5) give

\[
 \frac{\|\widehat W^{(1)}-W_0^{(1)}\|_F}{\sqrt n}
 \le64D_1\frac{Y^2}{\lambda^{3/2}},\qquad
 \|\widehat W^{(j)}-W_0^{(j)}\|_F
 \le192HD_j\frac{Y^2}{\lambda^{3/2}}.
 \tag{9}
\]

Forward subtraction uses the recursion
\(A_1=64sD_1\) and
\(A_j=s(288H^2D_j+9A_{j-1})\) for the coefficient of
\(Y^2/\lambda^{3/2}\) in the layer-\(j\) feature displacement.
Expanding the recursion and using
\(H\le\beta^{2L}\), \(D_j\le\beta^{2L}\), and
\((9s)^L\le\beta^{2L}\) gives \(A_j\le\beta^{16L}\).
Therefore the feature displacement is at most
\(\beta^{16L}(Y/\lambda)^2\sqrt\lambda<\sqrt\lambda/8\).
The same cap makes every hidden displacement in (9) less than one.
The initialization event has feature RMS at most \(3H/2\) and minimum
training feature singular value at least \(\sqrt{\lambda/2}\), so
these bounds improve all tube boundaries and preserve the Gram gap
\(\lambda/4\). This closes the stop argument with the original label cap.

The bounded coefficient factors \(|P_k|\le1\) and (8) make all moments
convergent. The physical gradient and defect have finite length; hence all
physical parameters converge, the labels are fitted, and the output has a
uniform whole-sphere limit. This fitting argument is uniform in \(q\).

## The dense-source error controls the actual nonlinear runtime

The dense feature-speed estimate in `compact_fitting.tex` gives

\[
 \sup_{t\ge T,a,j}
 \frac{\|h_{D,a}^{(j)}(t)-h_{D,a}^{(j)}(T)\|}{\sqrt n}
 \le C\frac{Y^2}{\lambda^{3/2}}e^{-\lambda T/2}.
\]

Thus the constant continuation in (1) approximates the dense histories at
all times with RMS error at most

\[
 \varepsilon=\eta+C\frac{Y^2}{\lambda^{3/2}}e^{-\lambda T/2}.
 \tag{10}
\]

Let \(e(t)=\|\widehat\theta(t)-\theta_D(t)\|_{\rm par}\).
Forward subtraction on the real tube gives, uniformly in all sphere queries,
\(\|\widehat h^{(j)}-h_D^{(j)}\|/\sqrt n\le C_h e\), with
\(C_h\) depending only on activations and depth. Equation (6) now yields
the sharper, exact-runtime forcing bound

\[
 \|\mathcal E(t)\|_{\rm par}
 \le2R\left(\sum_{j=2}^L D_j\right)\rho(t)
                       [C_h e(t)+\varepsilon].
 \tag{11}
\]

Use the signed comparison from the current Legendre proof. Its Jacobian
coefficient \(K=K_0+K_1M_n\), where
\(M_n=32\beta^{21L}(Y/\lambda)\sqrt{\ell_n}\), applies to any
pair of parameter trajectories in this tube: the derivation uses only the
dense training carrier bound, the endpoint parameter bounds, and the straight
parameter segment. It does not use the moment equations. The differential
inequality proved there, combined with (11), is

\[
 \dot e\le\left[K(\rho_D+3\rho)+
       2RC_h\left(\sum_{j=2}^L D_j\right)\rho\right]e
   +2R\left(\sum_{j=2}^L D_j\right)\rho\varepsilon.
 \tag{12}
\]

At a zero of \(e\), use the same \(\sqrt{e^2+u^2}\) regularization
as in the paper. Since \(\int\rho_D\le2Y/\lambda\) and
\(\int\rho\le4Y/\lambda\), integration of (12), with \(e(0)=0\), gives

\[
 \sup_{t\ge0} e(t)
 \le 8R\frac Y\lambda\left(\sum_{j=2}^L D_j\right)\varepsilon
 \exp\left\{14K\frac Y\lambda+
     8RC_h\frac Y\lambda\sum_{j=2}^L D_j\right\}.
 \tag{13}
\]

The exponent is \(O_{\rm problem}(1+\sqrt{\ell_n})\).
Whole-sphere forward/readout subtraction therefore proves

\[
 \sup_{t\in[0,\infty],\|x\|=\sqrt d}
 |\widehat f(t,x)-f_D(t,x)|
 \le C_{\rm problem}e^{C_{\rm problem}\sqrt{\ell_n}}
 \left[\eta+C_{\rm problem}e^{-16\ell_n}\right].
 \tag{14}
\]

The fitted endpoint is included by the proved limits. This is a genuine
source-to-nonlinear-runtime estimate, rather than a dense projection-tail
estimate. Integrating the differential inequality directly matters: inserting
a signed-stability factor into a later unsigned Gronwall inequality would
produce an unnecessary exponential of that factor.

## A polylogarithmic order supplies the source accuracy

Use the public whole-sphere time strip, whose radius is
\(r_t=\lambda/[\beta^{30L}Y^2\sqrt{(d+3)\ell_n}]\), and put

\[
 \alpha=\min\{1,r_t/(2T)\},\qquad M=\beta^{3L}.
\]

The Bernstein ellipse of parameter \(e^\alpha\) for \([0,T]\) lies
strictly inside that strip rectangle: its imaginary semiaxis is
\((T/2)\sinh\alpha\le T\alpha\le r_t/2\), and its real overshoot
is at most \(T\alpha/2\le r_t/4\). Apply the Joukowski contour
argument from the paper coordinatewise, or directly in the normalized
Euclidean norm. The resulting degree-below-\(q\) Chebyshev truncation has
uniform RMS error at most \(2M e^{-\alpha q}/(1-e^{-\alpha})\).

The degree-below-\(q\) Legendre projector on \([0,T]\) has
\(L^\infty\)-to-\(L^\infty\) norm at most \(q\). Indeed its
reproducing kernel has squared \(L^2(dt/T)\) norm
\(\sum_{k<q}(2k+1)P_k(2t/T-1)^2\le q^2\), so Cauchy-Schwarz
proves this bound. Applying the projector to the Chebyshev remainder gives
Legendre projection error at most

\[
 \frac{4M(1+q)}\alpha e^{-\alpha q}.
\]

For example,

\[
 q=\left\lceil\frac4\alpha
                   \log\frac{16M}{\alpha^2\eta}\right\rceil
 \tag{15}
\]

makes this error at most \(\eta/2\) when \(0<\eta\le1\).
Compile each of the exact Legendre coefficient vectors to normalized
Euclidean accuracy \(\eta/(2q)\). Since \(|P_k|\le1\), the total
coefficient error is at most \(\eta/2\), proving (1).

Take \(\eta=Yn^{-2}\). This is at most \(H\) because
\(Y\le\lambda\le\sqrt\lambda\le H\). Equation (14) is then at
most \(Y/n\) for sufficiently large width for every fixed admissible
problem. Finally

\[
 \alpha^{-1}=O_{\rm problem}(\ell_n^{3/2}),\qquad
 q=O_{\rm problem}(\ell_n^{5/2}).
\]

Consequently (4) has \(O_{\rm problem}(n\log^{5/2}n)\) moving
coordinates and that many extra fixed coefficient coordinates, in addition
to the fixed dense mixers. The original theorem's sharper explicit
sample/gap prefactor is not claimed here. Its same-label, whole-sphere,
all-time, initialization-only scope is retained for this modified model.

## Assessment of the supervisor's projected-gradient variant

The supervisor separately proposed replacing the fixed forward forcing in
(5) by an exact orthogonal projection of the runtime feature. This is the
cleaner fitting mechanism. Let \(U_{j-1}\in\mathbb R^{n\times r_{j-1}}\)
have orthonormal columns spanning all the compiled coefficient vectors
\(c_{a,k}^{(j-1)}\), so \(r_{j-1}\le mq\). Parameterize

\[
 \widehat W^{(j)}=W_0^{(j)}+C_jU_{j-1}^\top,\qquad
 \dot C_j=-\frac2{mn}\sum_a\widehat r_a\widehat\delta_a^{(j)}
                     [U_{j-1}^\top\widehat h_a^{(j-1)}]^\top,
 \qquad C_j(0)=0.
\]

Keep the full first-layer and readout equations. The map
\(C_j\mapsto C_jU_{j-1}^\top\) is an isometry in Frobenius norm,
and right multiplication by \(U_{j-1}U_{j-1}^\top\) is an orthogonal
contraction. This is exactly gradient flow of the same nonlinear network
loss on a fixed affine parameter subspace. Every fitting bound in
`compact_fitting.tex` survives with the **same constants**: exact energy
dissipation uses the restricted gradient, the readout Gram gives the same
coercivity, hidden-block speeds only decrease under projection, and the
same forward subtraction and stop argument apply. In particular the
original label cap suffices, without a new smallness assumption.

Let \(P\) be the resulting orthogonal projector in mobility parameter
coordinates, \(z=(I-P)(\theta_D-\theta_0)\), and
\(e=\widehat\theta-\theta_D\). Because the dense training features
stay within \(\varepsilon\) of these coefficient spans by (10),

\[
 \sup_t\|z(t)\|_{\rm par}
 \le C\frac{Y^2}{\lambda^{3/2}}\varepsilon.
\]

This follows by projecting the dense hidden weight velocity and integrating
\(2\rho_D\|\delta_D^{(j)}\|_{\rm RMS}\varepsilon\); the other
blocks have zero omitted component. For the exact restricted runtime,

\[
 \frac12\frac d{dt}\|e\|_{\rm par}^2
 =\langle e,\mathcal F(\widehat\theta)-\mathcal F(\theta_D)\rangle
  +\langle z,\mathcal F(\widehat\theta)\rangle.
\]

The sign of the last term is positive because \((I-P)e=-z\).
The first term has the signed comparison bound
\(K(\rho_D+3\widehat\rho)\|e\|^2\). The full, unprojected
gradient at the restricted runtime has norm at most
\(C_{\rm problem}\widehat\rho\) on the fitting tube, so its total
norm integral is bounded independently of \(n\). Integration therefore
gives \(\sup_t\|e\|\le C_{\rm problem}
e^{C_{\rm problem}\sqrt{\ell_n}}\sqrt\varepsilon\).
Choosing source tolerance \(\eta=Yn^{-K_*}\) with a fixed sufficiently
large \(K_*\), for example \(K_*=6\), still gives
\(q=O_{\rm problem}(\log^{5/2}n)\) and accuracy below \(Y/n\)
eventually. Whole-sphere and fitted-endpoint transfer are unchanged.

This projected variant removes the auxiliary clock and the non-gradient
forcing. Its moving hidden coordinates are \(n\sum_j r_j\), and its
extra fixed bases occupy the same number. It is a fixed parameter-subspace
method built from Legendre history coefficients, rather than the original
two-sided moving Legendre projection. Subject to an independent audit, this
route is preferable to the one-sided variant above.

### Fewer local modes suffice for the projected variant

The projected variant needs source approximation only for **training forward
histories**. Its whole-sphere conclusion is obtained afterwards by parameter
comparison. It can therefore use the finite-panel source proposition with
the panel consisting only of the training inputs. The deterministic partition
has

\[
 J\le1+\beta^{30L}(Y/\lambda)^2\sqrt{\ell_n}
       +\frac{\beta^{16L}}\lambda
           \log(1+4\ell_n/\log2).
\]

On each interval \([t_b,t_{b+1}]\) of length at most \(r_b/2\),
the parameter-two Bernstein ellipse lies in \(|t-t_b|<r_b\): its
center is \(t_b+h/2\) and its real semiaxis is \(5h/8\), so every
point has distance at most \(9h/8\le9r_b/16\) from \(t_b\).
Its imaginary semiaxis is smaller, and this maximum follows directly from
the ellipse parameterization. Thus degree
\(K=O_{\rm problem}(\log n)\) local Legendre approximants attain
\(\eta=Yn^{-6}\). Equivalently, compile the local Taylor jets supplied by
the paper and convert each degree-\(K\) Taylor polynomial exactly to the
local Legendre basis; this preserves its vector span and approximation error.

Put the coefficient vectors from every interval into the same fixed
\(U_j\). The total local mode count per training curve is

\[
 q_{\rm local}=J(K+1)
 =O_{\rm problem}\!\left(
       \ell_n^{3/2}+\ell_n\log\ell_n\right)
 =O_{\rm problem}(\ell_n^{3/2}).
\]

No patch selector, clock, or transition matching is present at runtime,
because the runtime only retains the common subspace and performs projected
gradient flow. This gives moving and extra fixed storage
\(O_{\rm problem}(n\log^{3/2}n)\). The statement concerns the total
number of local polynomial modes, not the degree of one global Legendre
polynomial, and it still does not establish the original moving-memory
equations at that order.

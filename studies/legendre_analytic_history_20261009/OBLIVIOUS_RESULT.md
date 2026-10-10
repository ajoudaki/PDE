# Oblivious physical-time Legendre memories with a small prefix

Internal derivation, 2026-10-09. This is a modified Legendre construction,
not a proof that the paper's existing residual-clock equations admit the
same improved order. It uses only prescribed temporal Legendre polynomials,
the ordinary online current forward/backward responses, the realized Gaussian
initial weights, and the initialized features. No dense future derivatives,
compiled response coefficients, response-dependent bases, or distilled
directions are inputs.

The proposed runtime is an **autonomous hybrid system**, with one prescribed
clock-triggered switch to readout-only training. It has a unique piecewise
classical, absolutely continuous solution. A globally locally Lipschitz
single-vector-field implementation is not claimed.

## Setup, prescribed order, and retained state

Use exactly the architecture, data, activations, normalizations, initialization,
and label cap in `paper/compact.tex`. Thus
\(v_a=x_a/\sqrt d\), \(\lambda=\gamma/m\le1\),
\(Y=\|y\|_2/\sqrt m>0\), and
\(Y\le\lambda\beta^{-30L}\). All problem parameters stay fixed as
\(n\) grows. Work on the paper's initialization/fitting event and public
analytic-source/carrier event. Their probabilities tend to one in the stated
eventual-confidence sense.

Set

\[
 \ell_n=\log(en),\qquad
 T=\frac{32\ell_n}{\lambda},\qquad
 r_t=\frac{\lambda}
 {\beta^{30L}Y^2\sqrt{(d+3)\ell_n}},
\]
\[
 \varepsilon=\min\{1,r_t/4\}e^{-16\ell_n},\qquad
 \alpha=\min\{1,r_t/[4(T+1)]\},\qquad
 q=\left\lceil32\alpha^{-1}\ell_n\right\rceil.
 \tag{1}
\]

These numbers depend only on declared scalar problem parameters. In particular,

\[
 \alpha^{-1}
 =\max\left\{1,
 \frac{4\beta^{30L}Y^2(T+1)\sqrt{(d+3)\ell_n}}{\lambda}
 \right\},\qquad
 q=O_{\rm problem}(\ell_n^{5/2}).
 \tag{2}
\]

The moving state consists of \(\widehat W^{(1)}\in\mathbb R^{n\times d}\),
\(\widehat w\in\mathbb R^n\), one scalar \(A\), and
\(\bar h_{a,j}^{(k-1)},\bar\delta_{a,j}^{(k)}\in\mathbb R^n\)
for \(k=2,\ldots,L\), \(a=1,\ldots,m\), and
\(j=0,\ldots,q-1\). The fixed matrices are exactly the initialized dense
mixers \(W_0^{(k)}\), \(k\ge2\).

Reconstruct each current hidden matrix as

\[
 \widehat W^{(k)}
 =W_0^{(k)}-
 \frac{2}{mnA}\sum_{a=1}^m\sum_{j=0}^{q-1}(2j+1)
       \bar\delta_{a,j}^{(k)}\bar h_{a,j}^{(k-1)\top}.
 \tag{3}
\]

Use those matrices in the ordinary forward pass
\(\widehat z^{(1)}=\widehat W^{(1)}v\),
\(\widehat z^{(k)}=\widehat W^{(k)}\widehat h^{(k-1)}\),
\(\widehat h^{(k)}=\phi_k(\widehat z^{(k)})\),
and \(\widehat f=\widehat w^\top\widehat h^{(L)}/n\).
The training residuals and loss are
\(\widehat r_a=\widehat f(x_a)-y_a\) and
\(m^{-1}\sum_a\widehat r_a^2\). The backward responses are the
paper's residual-free responses:

\[
 \widehat\delta_a^{(L)}
  =\widehat w\odot\phi_L'(\widehat z_a^{(L)}),\qquad
 \widehat\delta_a^{(k)}
  =\phi_k'(\widehat z_a^{(k)})\odot
                   \widehat W^{(k+1)\top}\widehat\delta_a^{(k+1)}.
\]

Let \(\chi(A)=1\) for \(A<\varepsilon+T\), and
\(\chi(A)=0\) for \(A\ge\varepsilon+T\). The autonomous equations are

\[
 \begin{aligned}
 \dot A&=\chi(A),\\
 \dot{\widehat W}^{(1)}
   &=-\chi(A)\frac2m\sum_a
                  \widehat r_a\widehat\delta_a^{(1)}v_a^\top,\\
 \dot{\widehat w}
   &=-\frac2m\sum_a\widehat r_a\widehat h_a^{(L)},\\
 \dot{\bar h}_{a,j}^{(k-1)}
   &=\chi(A)\left[\widehat h_a^{(k-1)}-
       \frac1A\left(j\bar h_{a,j}^{(k-1)}+
              \sum_{i<j}(2i+1)\bar h_{a,i}^{(k-1)}\right)\right],\\
 \dot{\bar\delta}_{a,j}^{(k)}
   &=\chi(A)\left[\widehat r_a\widehat\delta_a^{(k)}-
       \frac1A\left(j\bar\delta_{a,j}^{(k)}+
              \sum_{i<j}(2i+1)\bar\delta_{a,i}^{(k)}\right)\right].
 \end{aligned}
 \tag{4}
\]

Initialize

\[
 A(0)=\varepsilon,\quad
 \widehat W^{(1)}(0)=W_0^{(1)},\quad \widehat w(0)=0,\quad
 \bar h_{a,0}^{(k-1)}(0)=\varepsilon h_{0,a}^{(k-1)},
\]

with every higher forward moment and every backward moment zero. Thus
\(A(t)=\varepsilon+\min(t,T)\). Before the switch the vector field is
locally Lipschitz because \(A\ge\varepsilon>0\). After the switch,
all hidden parameters and histories are frozen and the readout follows an
ordinary linear gradient flow. The value \(\chi=0\) at the boundary
specifies the unique stationary clock continuation.

The exact persistent coordinate counts, excluding data, are

\[
 S_{\rm moving}=n(d+1)+1+2(L-1)mnq,
 \qquad S_{\rm fixed}=(L-1)n^2.
 \tag{5}
\]

Known scalar coefficients and the prescribed mode recurrence require no dense
response arrays. The count is therefore
\(O_{\rm problem}(n\log^{5/2}n)\) moving coordinates. There is no
claim about finite precision or numerical conditioning: the small positive
prefix produces large but finite coefficients \(1/A\) near initialization.

## Exact moment identity and physical defect before the switch

For \(A\le\varepsilon+T\), let
\(p_j^A(\xi)=P_j(2\xi/A-1)\) and let \(\Pi_q^A\) be the
\(L^2([0,A])\) projector onto degree below \(q\).
Define the proof histories

\[
 h_a^{(k)}(\xi)=
 \begin{cases}h_{0,a}^{(k)},&0\le\xi\le\varepsilon,\\
 \widehat h_a^{(k)}(\xi-\varepsilon),&\varepsilon<\xi\le A,
 \end{cases}
\]
\[
 b_a^{(k)}(\xi)=
 \begin{cases}0,&0\le\xi\le\varepsilon,\\
 \widehat r_a(\xi-\varepsilon)
       \widehat\delta_a^{(k)}(\xi-\varepsilon),&\varepsilon<\xi\le A.
 \end{cases}
\]

Both histories are continuous at the prefix join: the first by initialization,
the second because the initialized readout is zero. Differentiating their
Legendre moments proves that (4) stores exactly
\(\bar h_{a,j}^{(k)}=\int_0^A p_j^Ah_a^{(k)}\) and
\(\bar\delta_{a,j}^{(k)}=\int_0^A p_j^Ab_a^{(k)}\).

Set \(e_h=h(A)-(\Pi_q^Ah)(A)\) and
\(e_b=b(A)-(\Pi_q^Ab)(A)\), with layer/sample indices as needed.
The growing-interval projection identity in `compact_legendre.tex` gives,
for \(0<t<T\),

\[
 \dot{\widehat W}^{(k)}
 =-\frac2{mn}\sum_a\widehat r_a\widehat\delta_a^{(k)}
                          \widehat h_a^{(k-1)\top}+\mathcal E_k,
 \qquad
 \mathcal E_k=\frac2{mn}\sum_a e_{b,a}^{(k)}e_{h,a}^{(k-1)\top}.
 \tag{6}
\]

There is no residual-clock prefactor in (6). Its useful feature is that
the defect is the **product of two endpoint projection errors**. This
construction is not claimed to fit at every finite order without switching.

## Analytic dense histories have uniformly tiny endpoint errors

Use a subscript \(D\) for the coupled dense trajectory. Form the same
constant-prefix histories from \(h_D\) and \(b_D=r_D\delta_D\).
The public source theorem gives a holomorphic extension of \(h_D\) and
\(\delta_D\) to
\([-r_t,T+r_t]+i[-r_t,r_t]\), uniformly for real sphere queries.
It also bounds their normalized Euclidean norms there by fixed-problem
constants. The residual is holomorphic because
\(r_{D,a}=w_D^\top h_{D,a}^{(L)}/n-y_a\). Its modulus is bounded
there using the source bounds on \(w_D=k_D^{(L)}\) and
\(h_D^{(L)}\). Consequently both \(h_D\) and
\(b_D=r_D\delta_D\) have normalized Euclidean norm at most a
constant \(B_{\rm problem}\) throughout the rectangle. This constant
does not depend on width.

For any \(A\in[\varepsilon,\varepsilon+T]\), compare a dense
prefixed history with its genuinely analytic extension
\(g(\xi)=h_D(\xi-\varepsilon)\), or
\(g(\xi)=b_D(\xi-\varepsilon)\). A disk of radius \(r_t/2\)
around any point of \([-\varepsilon,0]\) stays in the source rectangle.
Cauchy's formula bounds the normalized derivative by
\(2B_{\rm problem}/r_t\). Since \(h_D(0)=h_0\) and
\(b_D(0)=0\), the constant-prefix modification differs from the analytic
extension in uniform normalized Euclidean norm by at most

\[
 2B_{\rm problem}\varepsilon/r_t.
 \tag{7}
\]

The parameter-\(e^\alpha\) Bernstein ellipse for \([0,A]\),
after shifting by \(-\varepsilon\), lies inside the source rectangle.
Indeed its imaginary semiaxis is at most \(A\alpha\le r_t/4\),
its real overshoot is at most \(A\alpha/2\le r_t/8\), and
\(\varepsilon\le r_t/4\). The Joukowski contour argument gives a
degree-below-\(q\) polynomial approximating the analytic history uniformly
in normalized Euclidean norm with error at most

\[
 \frac{2B_{\rm problem}e^{-\alpha q}}{1-e^{-\alpha}}
 \le4B_{\rm problem}\alpha^{-1}e^{-\alpha q}.
\]

The endpoint projection operator satisfies
\(\|(\Pi_q^Au)(A)\|\le64\sqrt q\|u\|_{L^\infty}\),
as proved in the paper. Since the projector reproduces the approximating
polynomial, (7) proves that every dense prefixed endpoint error, divided
by \(\sqrt n\), is at most

\[
 \eta_n=C_{\rm problem}(1+64\sqrt q)
       [\alpha^{-1}e^{-\alpha q}+\varepsilon/r_t].
 \tag{8}
\]

The same bound holds uniformly in sample, relevant layer, and growing horizon.
By (1), \(\alpha q\ge32\ell_n\) and
\(\varepsilon/r_t\le e^{-16\ell_n}/4\). Since \(q\) and
\(\alpha^{-1}\) grow only polylogarithmically, at sufficiently large
width for each fixed problem,

\[
 \eta_n\le n^{-8}.
 \tag{9}
\]

This calculation does not assert analyticity of the constant-prefixed history.
Its nonanalytic part has explicitly bounded amplitude on the short prefix.

## Quadratic signed bootstrap for the actual online model

Use the Euclidean mobility norm

\[
 \|\theta\|_{\rm par}^2
  =\|W^{(1)}\|_F^2/n+
       \sum_{k=2}^L\|W^{(k)}\|_F^2+\|w\|_2^2/n.
\]

Let
\(D(t)=\sup_{0\le u\le t}\|\widehat\theta(u)-\theta_D(u)\|_{\rm par}\).
Stop the pre-switch evolution at \(T\) or its first discrepancy
\(D=n^{-3}\). On this stopped interval, dense fitting and ordinary
forward subtraction place the compressed physical parameters in the same
real operator/feature tube used by the paper's signed comparison, for
sufficiently large width. The dense trajectory has strict margins from
its proof: initialized operators at most eight, hidden displacements less
than \(1/8\), and feature/singular-value improvements strictly within
the displayed bounds. The readout remains within
\(8Y/\sqrt\lambda\), since the dense readout is at most
\(2Y/\sqrt\lambda\) and \(n^{-3}\to0\).

Forward subtraction, uniformly over the sphere, gives
\(\|\widehat h^{(k)}-h_D^{(k)}\|/\sqrt n\le C_{\rm problem}D\).
For backward subtraction use the dense carrier decomposition from the paper:

\[
 \widehat\delta-\delta_D
 =\phi'(\widehat z)\odot(\widehat k-k_D)
   +[\phi'(\widehat z)-\phi'(z_D)]\odot k_D.
\]

Only the actual dense carrier requires a coordinate bound, supplied as
\(\max|k_D|\le32\beta^{21L}(Y/\lambda)\sqrt{\ell_n}\).
The backward recursion therefore bounds normalized response discrepancy by
\(C_{\rm problem}(1+\sqrt{\ell_n})D\).
The bounded real tube also bounds every current residual, and forward/readout
subtraction bounds residual discrepancies by \(C_{\rm problem}D\).
Thus

\[
 \frac{\|\widehat r_a\widehat\delta_a^{(k)}
                  -r_{D,a}\delta_{D,a}^{(k)}\|}{\sqrt n}
 \le C_{\rm problem}(1+\sqrt{\ell_n})D.
\]

The two systems have identical prefixes. Applying the endpoint operator to
the history differences, and then (8)-(9), gives bounds for the **runtime**
endpoint errors of the form

\[
 \frac{\|e_h\|}{\sqrt n},\quad
 \frac{\|e_b\|}{\sqrt n}
 \le\eta_n+B_nD(t),\qquad
 B_n=C_{\rm problem}(1+64\sqrt q)(1+\sqrt{\ell_n}).
 \tag{10}
\]

Here \(B_n\) is polylogarithmic in width. Sample Cauchy-Schwarz in
(6) consequently yields

\[
 \sum_{k=2}^L\|\mathcal E_k(t)\|_F
 \le2(L-1)[\eta_n+B_nD(t)]^2.
 \tag{11}
\]

This is the nonlinear feedback estimate needed for the construction.

The signed Jacobian estimate from the current Legendre comparison applies on
this real tube and straight parameter segments. Its coefficient is
\(K_n=K_0+K_1M_n=O_{\rm problem}(1+\sqrt{\ell_n})\), where
\(M_n\) is the actual dense carrier bound. That estimate depends on the
network and tube, not on the residual-clock moment equations.

Write \(\rho_D=\|r_D\|_2/\sqrt m\) and
\(\widehat\rho=\|\widehat r\|_2/\sqrt m\). On the stopped interval,

\[
 \int_0^t\widehat\rho\le
 \int_0^t\rho_D+C_{\rm problem}TD(t)
 \le2Y/\lambda+C_{\rm problem}Tn^{-3}
 \le3Y/\lambda
\]

eventually. The paper's signed perturbation lemma and (11) now give

\[
 D(t)\le C\mathcal A_n T[\eta_n+B_nD(t)]^2,
 \qquad
 \mathcal A_n\le\exp\{C_{\rm problem}(1+\sqrt{\ell_n})\}.
 \tag{12}
\]

The right side of (12), evaluated at \(D=n^{-3}\), is
\(n^{-6+o(1)}<n^{-3}\). Thus no discrepancy stop occurs. Bounded
physical parameters imply bounded histories on each finite stopped horizon;
their exact moment integral formulas bound all stored coordinates. Since
\(A\ge\varepsilon>0\), this also rules out a finite-time continuation
failure before \(T\).

For the sharper final estimate, use
\((\eta+B D)^2\le2\eta^2+2B^2D^2\) in (12). Because
\(D\le n^{-3}\) and
\(2C\mathcal A_nTB_n^2n^{-3}\to0\), the quadratic term can be
absorbed, giving

\[
 \sup_{0\le t\le T}
 \|\widehat\theta(t)-\theta_D(t)\|_{\rm par}
 \le4C\mathcal A_nT\eta_n^2=n^{-16+o(1)}.
 \tag{13}
\]

The assertion \(n^{-16+o(1)}\) concerns a deterministic fixed-problem
bound on the stated source event. Uniform whole-sphere output subtraction
has a width-independent constant on the real tube, so the same rate holds
for the prediction discrepancy on \([0,T]\). No extra label restriction
was introduced: the existing cap supplies dense fitting, and every additional
smallness condition above is obtained by increasing width for the same
fixed positive \(Y\).

## The prescribed switch gives exact fitting and the entire endpoint

At \(T\), freeze \(A\), every moment, and \(\widehat W^{(1)}\),
as specified by (4). This freezes every hidden feature. Only the readout
continues to move. The frozen training feature matrix
\(\widehat{\mathsf H}_T=[\widehat h_a^{(L)}(T)]_{a=1}^m\)
has normalized Gram at least \(\lambda I/4\), after using the strict
dense singular-value margin and (13). Hence

\[
 \dot{\widehat r}
 =-\frac2{mn}\widehat{\mathsf H}_T^\top
                         \widehat{\mathsf H}_T\widehat r,
 \qquad
 \widehat\rho(t)\le\widehat\rho(T)
                       e^{-\lambda(t-T)/2}\quad(t\ge T).
\]

The readout converges and the labels are fitted exactly. Since
\(\|\widehat h^{(L)}(T,x)\|/\sqrt n\le2H\) on the sphere,
\(\|\dot{\widehat w}\|/\sqrt n\le4H\widehat\rho\), giving

\[
 \sup_{t\ge T,\|x\|=\sqrt d}
 |\widehat f(t,x)-\widehat f(T,x)|
 \le\frac{16H^2}{\lambda}\widehat\rho(T).
 \tag{14}
\]

The dense tail estimate applies to all sphere queries, and
\(\rho_D(T)\le Ye^{-16\ell_n}\). Furthermore
\(\widehat\rho(T)\le\rho_D(T)+C_{\rm problem}D(T)\).
Combining (13)-(14), the dense output tail, and the discrepancy at \(T\)
therefore proves

\[
 \sup_{t\in[0,\infty],\|x\|=\sqrt d}
 |\widehat f(t,x)-f_D(t,x)|
 \le C_{\rm problem}[\mathcal A_nT\eta_n^2+Ye^{-16\ell_n}]
 =n^{-16+o(1)}.
 \tag{15}
\]

All limits in (15) exist: every non-readout coordinate is fixed after \(T\)
and the readout converges exponentially in its training-feature component.
Thus (15) includes the fitted endpoint, and in particular is at most \(Y/n\)
for every fixed admissible problem at sufficiently large width. It is also
negligible compared with the paper's dense-variability scale.

## Scope of the result

The basis is oblivious: every temporal polynomial, order, prefix length and
switch time is prescribed before observing any response direction. Its
coefficients are not initialized with dense future information. All moments
are written online from current nonlinear responses. Fixed storage remains
the initialized dense mixers, and (5) gives the moving inventory.

The changes from the published-in-this-checkout construction are the physical
clock, an \(n\)-dependent small constant prefix, and a deterministic
readout-only tail. The proof relies on the quadratic endpoint defect and a
finite-horizon signed bootstrap, rather than the original order-independent
all-time Legendre fitting argument. It establishes an autonomous hybrid
construction; requiring one globally locally Lipschitz autonomous vector
field with no switching would leave an additional implementation/proof
obligation. This note is an internal proof route awaiting independent audit.

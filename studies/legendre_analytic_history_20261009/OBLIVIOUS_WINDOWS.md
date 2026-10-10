# Oblivious physical-time Legendre compression

The final section gives the simplest version: **one growing interval and
one order `q`**, with no prefix or panel restarts. Its order is
`O(log(en)^(5/2))` with the problem fixed, and its learned state is at most
`n(d+1)+2(L-1)mnq+1`. The multi-panel construction first proves the same
mechanism locally; it is not necessary to introduce a second tunable order
in the final method. Both versions use only online responses of the compressed
model, never a data-adapted response basis, dense source coefficients, or
dense initialization jets.

This is a bounded candidate within this study, not a promoted result. It uses
only the setup, fitting lemma, signed perturbation lemma, analytic-source
proposition, and projection identities in `paper/compact*.tex`. It does not
use a fitted response subspace or a dense-trajectory source compiler. The
argument below closes the nonlinear comparison on a finite deterministic
horizon, then obtains fitting by an explicit readout-only continuation.

## Setup and conclusion

Use exactly the network, initialization, block mobilities, activation
assumptions, and small-label condition of `paper/compact.tex`. Thus

\[
z^{(1)}=W^{(1)}v,\quad z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\quad
h^{(\ell)}=\phi_\ell(z^{(\ell)}),\quad
f=\frac{w^\top h^{(L)}}n,\quad r_a=f(x_a)-y_a,
\qquad v=x/\sqrt d.
\]

The residual-free responses are
\(\delta_a^{(L)}=w\odot\phi_L'(z_a^{(L)})\) and
\(\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot
W^{(\ell+1)\top}\delta_a^{(\ell+1)}\). Hats will identify the new
online model; unhatted quantities identify dense gradient flow.

Put

\[
\lambda=\gamma/m\le1,\quad z=Y/\lambda,\quad
T=32\log(en)/\lambda,\quad
r_t=\frac{\lambda}{\beta^{30L}Y^2\sqrt{(d+3)\log(en)}},\quad
q=\left\lceil\frac{4\log(en)}{\log2}\right\rceil.
\]

The letter \(z\) without a layer/sample index is only the scalar \(Y/\lambda\)
in this note. Let \(J=\lceil2T/r_t\rceil\) and
\(t_b=bT/J\), \(0\le b\le J\). Every panel has length at most
\(r_t/2\), and

\[
J\le1+64\beta^{30L}z^2\sqrt{d+3}\,\log(en)^{3/2}.
\]

The basis and schedule depend only on the qualification parameters listed
above. The following construction has total learned storage, including
completed frozen panels,

\[
n(d+1)+2(L-1)mnqJ+O(1)
=O\!\left(nd+mn\log(en)+
mn\beta^{30L}z^2\sqrt{d+3}\,\log(en)^{5/2}\right).
\tag{1}
\]

The constants in the last big-O can depend on depth. The fixed initialized
mixers cost another \((L-1)n^2\); training data and activation evaluators
are additional, as in the source convention. For each fixed admissible
problem, eventually at each fixed confidence, the construction fits the
labels, has limits, and satisfies

\[
\sup_{t\in[0,\infty],\ \|x\|=\sqrt d}
|\widehat f(t,x)-f_n(t,x)|
\le\frac{Y}{\sqrt n\,\log(en)^3}.
\tag{2}
\]

The proof yields a stronger finite-horizon error of
\(n^{-8+o(1)}\), with constants depending on the fixed problem. As in the
paper, this statement is eventual for a fixed positive \(Y\), not uniform
as \(Y\downarrow0\), and it does not assert a practical width threshold.

## Online state and reconstruction

For each hidden interface \(\ell=2,\ldots,L\), sample \(a\), panel
\(b\), and mode \(j<q\), store vectors
\(\bar h_{a,b,j}^{(\ell-1)},\bar\delta_{a,b,j}^{(\ell)}\in\mathbb R^n\).
On the active panel \([s,t_{b+1}]\), where \(s=t_b\), write \(A=t-s\).
The intended moments for \(A>0\) are

\[
\begin{aligned}
\bar h_{a,b,j}^{(\ell-1)}(t)
 &=\int_s^tP_j\!\left(2\frac{u-s}{A}-1\right)
                  \widehat h_a^{(\ell-1)}(u)\,du,\\
\bar\delta_{a,b,j}^{(\ell)}(t)
 &=\int_s^tP_j\!\left(2\frac{u-s}{A}-1\right)
          \widehat r_a(u)\widehat\delta_a^{(\ell)}(u)\,du.
\end{aligned}
\tag{3}
\]

The backward moment therefore includes the physical residual, with no
division by a residual and no residual-dependent clock. Set every new
panel's moments to zero at its left endpoint. Completed moments and their
panel lengths are frozen. The moments of panels not yet started are zero.

For any nonzero active or completed length \(A_b(t)\), reconstruct

\[
\widehat W^{(\ell)}(t)=W_0^{(\ell)}-
\frac2{mn}\sum_{b:A_b(t)>0}\frac1{A_b(t)}
\sum_{a=1}^m\sum_{j<q}(2j+1)
\bar\delta_{a,b,j}^{(\ell)}(t)
\bar h_{a,b,j}^{(\ell-1)}(t)^\top.
\tag{4}
\]

At zero panel length its contribution is defined to be zero. Evaluating
the ordinary current forward and backward recursions using (4) supplies
all updates. Matrix-vector products can apply the rank-one sums directly;
the reconstructed dense matrices need not be retained.

The active moments satisfy, for \(A>0\),

\[
\begin{aligned}
\dot{\bar h}_{a,b,j}^{(\ell-1)}
 &=\widehat h_a^{(\ell-1)}-
 \frac1A\left(j\bar h_{a,b,j}^{(\ell-1)}+
       \sum_{i<j}(2i+1)\bar h_{a,b,i}^{(\ell-1)}\right),\\
\dot{\bar\delta}_{a,b,j}^{(\ell)}
 &=\widehat r_a\widehat\delta_a^{(\ell)}-
 \frac1A\left(j\bar\delta_{a,b,j}^{(\ell)}+
       \sum_{i<j}(2i+1)\bar\delta_{a,b,i}^{(\ell)}\right).
\end{aligned}
\tag{5}
\]

The remaining moving state is \(\widehat W^{(1)},\widehat w\), with
the original physical-time updates

\[
\dot{\widehat W}^{(1)}=-\frac2m\sum_a
\widehat r_a\widehat\delta_a^{(1)}v_a^\top,
\qquad
\dot{\widehat w}=-\frac2m\sum_a\widehat r_a\widehat h_a^{(L)}.
\tag{6}
\]

Their initial values are the realized initialized first layer and zero
readout. No artificial history prefix or labeled-future derivative is
used. A physical-time clock and panel index make this a deterministic
hybrid evolution. Completed frozen moments are still charged as learned
information in (1).

## A genuine solution at zero panel length

The singular notation in (5) is not treated by starting at a positive
epsilon. Here is a local definition and existence proof at every restart.
For a continuous trial parameter path \(\vartheta\) on \([s,s+a]\),
with prescribed value \(\vartheta(s)=\widehat\theta(s)\), evaluate its
current fields and write (3) as

\[
\bar h_j(s+A)=A\int_0^1P_j(2u-1)h_\vartheta(s+Au)\,du,
\quad
\bar\delta_j(s+A)=A\int_0^1P_j(2u-1)
                  (r\delta)_\vartheta(s+Au)\,du.
\tag{7}
\]

Let \(\Pi_q\) be the fixed degree-below-\(q\) projection on \([0,1]\).
The active hidden increment in (4) is exactly

\[
-\frac{2A}{mn}\sum_a\int_0^1
\Pi_q[(r_a\delta_a)_\vartheta(s+A\,\cdot)](u)
\Pi_q[h_{a,\vartheta}(s+A\,\cdot)](u)^\top\,du.
\tag{8}
\]

Define a map on trial paths by (8) added to the hidden matrices at time
\(s\), and by integrating (6) for the first layer and readout. On a fixed
finite-dimensional parameter ball, the fields and their first derivatives
are bounded. Projection contraction in \(L^2([0,1])\), followed by
Cauchy--Schwarz for each outer product, bounds the difference between (8)
for two trial paths by
\(a C\|\vartheta-\widetilde\vartheta\|_{C^0}\). It also bounds the
increment by \(aC\). The integral equations for (6) have the same two
bounds. These constants can be taken independent of \(q\), although
only their finiteness is needed for local existence.

Choose \(a>0\) so that this map preserves the ball and \(aC<1\).
The contraction theorem gives a unique continuous path, hence the moments
(7). For \(A>0\), differentiation gives (5); its finite-dimensional
vector field is smooth there. As \(A\downarrow0\),
\(\bar h_0/A\to h(s)\), \(\bar\delta_0/A\to(r\delta)(s)\), and
all higher normalized moments tend to zero. The active hidden increment
is \(-2A\sum_a(r_a\delta_a)(s)h_a(s)^\top/(mn)+o(A)\).
Thus the physical path has the correct right derivative at the restart.
The construction specifies the regular branch uniquely; merely imposing
zero initial moments on the singular differential notation would not
have supplied this argument.

Away from a restart, the moment ODE continues whenever its state remains
bounded. Identity (3) bounds every moment on a finite panel whenever the
physical parameters stay in a bounded region. The discrepancy estimate
below guarantees this through \(T\). Physical parameters are continuous
across panel boundaries; their derivatives can have a finite jump.

## Exact defect and analytic reference approximation

For a history \(g\) on the active interval, let
\(e_g(t)=g(t)-(\Pi_q^{[s,t]}g)(t)\) be its endpoint projection error.
Use the actual online histories \(\widehat h\) and
\(\widehat b_a^{(\ell)}=\widehat r_a\widehat\delta_a^{(\ell)}\).
Differentiation of the projected bilinear pairing gives

\[
\dot{\widehat W}^{(\ell)}=
-\frac2{mn}\sum_a\widehat r_a\widehat\delta_a^{(\ell)}
                              \widehat h_a^{(\ell-1)\top}
+\mathcal E_\ell,
\qquad
\mathcal E_\ell=\frac2{mn}\sum_a
e_{\widehat b_a}^{(\ell)}e_{\widehat h_a}^{(\ell-1)\top}.
\tag{9}
\]

Indeed the derivative of the full-history pairing is its endpoint
product, and the derivative of the pairing of the two orthogonal
remainders is the product of their endpoint remainders. The interior
derivative terms vanish by orthogonality. Frozen earlier panels
contribute zero derivative.

Work on the joint source and fitting event of the paper. The aggregate
Hilbert norm of a training-history family \(g=(g_a)_{a=1}^m\) is
\(\|g\|_{mn}^2=\sum_a\|g_a\|_2^2/(mn)\). On each complex disk
\(|t-s|\le r_t\), the dense source proposition supplies

\[
\|h^{(\ell)}\|_{mn}\le\beta^{3L},\qquad
\max_a\|\delta_a^{(\ell)}\|_2/\sqrt n
\le16\beta^{4L}z.
\]

The dense readout obeys the latter bound too, so
\(|f(t,x_a)|\le16\beta^{7L}z\). Consequently

\[
\|b^{(\ell)}\|_{mn}
\le16\beta^{4L}z(16\beta^{7L}z+Y)
\le272\beta^{11L}z^2,
\qquad b_a^{(\ell)}=r_a\delta_a^{(\ell)}.
\tag{10}
\]

Here \(Y\le z\) uses \(\lambda\le1\). Products of holomorphic
fields are holomorphic, so these bounds apply to the backward history
actually used in physical time.

For a Hilbert-valued function holomorphic on a neighborhood of a disk of
radius \(r_t\), bounded there by \(B\), Cauchy's integral formula gives
Taylor coefficients bounded by \(B r_t^{-k}\). On every growing interval
of length \(A\le r_t/2\), its degree-below-\(q\) Taylor remainder
therefore has uniform norm at most \(2B2^{-q}\). The endpoint projection
bound from the paper, applied after subtracting this Taylor polynomial,
gives

\[
\|e_g(t)\|\le2(1+64\sqrt q)B2^{-q}.
\tag{11}
\]

The Taylor polynomial is a proof object: none of its coefficients are
computed or stored by the online construction.

## Closing the nonlinear flow

Use the paper's Euclidean mobility coordinates
\((W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)\), with norm
\(\|\cdot\|_{\rm par}\). Define

\[
D(t)=\sup_{0\le u\le t}\|\widehat\theta(u)-\theta(u)\|_{\rm par},
\qquad \varepsilon=2^{-q}\le(en)^{-4}.
\]

Stop while \(D\le\varepsilon\). Dense fitting and \(\varepsilon\le1\)
place the two paths and the segment between them in a bounded real
operator/readout region; all forward RMS bounds there depend only on
activations and depth. Forward subtraction gives, for all sphere queries,

\[
\frac{\|\widehat h^{(\ell)}-h^{(\ell)}\|}{\sqrt n}
+|\widehat f-f_n|\le C D(t).
\tag{12}
\]

To check backward subtraction without a dimension factor, use

\[
\widehat\delta-\delta
=\phi'(\widehat z)\odot(\widehat k-k)
+[\phi'(\widehat z)-\phi'(z)]\odot k.
\]

The second term uses only the dense training carrier bound
\(M_n=32\beta^{21L}z\sqrt{\log(en)}\). The first term propagates the
response discrepancy and a changed matrix acting on a bounded dense
response. Induction through the fixed depth gives
\(\max_a\|\widehat\delta_a-\delta_a\|/\sqrt n
\le C(1+M_n)D(t)\).
Splitting
\(\widehat r_a\widehat\delta_a-r_a\delta_a
=\widehat r_a(\widehat\delta_a-\delta_a)
+(\widehat r_a-r_a)\delta_a\), then using the sample RMS residual
and (12), yields

\[
\|\widehat b-b\|_{mn}\le C_0(1+\sqrt{\log(en)})D(t).
\tag{13}
\]

In this subsection \(C_0,C_1,\ldots\) may depend on the fixed problem,
but never on \(n\). This convention is only for the proof's eventual
comparison and does not hide a width dependence in the storage formula.

Apply (11) to the dense histories and the endpoint operator bound to
their differences from the online histories. Cauchy--Schwarz in samples
in (9) gives, uniformly on stopped intervals,

\[
\sum_{\ell=2}^L\|\mathcal E_\ell(t)\|_F
\le C_1q(1+\sqrt{\log(en)})[\varepsilon+D(t)]^2.
\tag{14}
\]

This estimate uses analytic dense histories only as reference functions.
It makes no analyticity assertion about the online closed flow. The
quadratic dependence is essential: replacing either endpoint error by a
crude nonvanishing bound would lose the argument.

The same backward subtraction on every point of the segment from dense
parameters to online parameters gives

\[
\|\nabla f_a(\theta+u(\widehat\theta-\theta))-
       \nabla f_a(\theta)\|_{\rm par}
\le K_nu\|\widehat\theta-\theta\|_{\rm par},
\quad K_n\le C_2(1+\sqrt{\log(en)}),\quad 0\le u\le1.
\tag{15}
\]

For verification, the gradient blocks are
\(\delta_a^{(1)}v_a^\top/\sqrt n\),
\(\delta_a^{(\ell)}h_a^{(\ell-1)\top}/n\), and
\(h_a^{(L)}/\sqrt n\). Subtract a hidden product by changing its
backward factor and then its forward factor. Equations (12)--(13)'s
response argument bound each resulting product; there are only \(L+1\)
blocks. Segment integration of (15) verifies both Taylor-remainder
hypotheses of the paper's signed perturbation lemma with coefficient
\(K_n\).

Dense fitting gives \(\int_0^T\rho\le2z\), and (12) implies
\(\int_0^T\widehat\rho\le2z+CT\varepsilon\le3z\) eventually,
where \(\rho=\|r\|_2/\sqrt m\) and
\(\widehat\rho=\|\widehat r\|_2/\sqrt m\).
The signed lemma, applied piecewise and integrated across the finitely
many continuous panel joins, therefore yields

\[
D(t)\le A_n\int_0^t\sum_{\ell=2}^L\|\mathcal E_\ell(u)\|_F\,du,
\qquad A_n=\exp(11zK_n)=\exp(O(\sqrt{\log(en)}))=n^{o(1)}.
\tag{16}
\]

Combining (14)--(16) under the stop condition gives

\[
D(t)\le4A_n C_1Tq(1+\sqrt{\log(en)})\varepsilon^2
=n^{-8+o(1)}.
\tag{17}
\]

Eventually the coefficient times \(4\varepsilon\) is below \(1/2\),
so (17) improves the stop to \(D(t)<\varepsilon/2\). Continuity, local
existence at restarts, and bounded-moment continuation exclude a first
stop before \(T\). Thus (17) holds on the entire deterministic training
horizon. It gives (2) for \(t\le T\) by (12).

## Fitted continuation and the complete time axis

At the predetermined time \(T\), freeze all moments and the first layer.
Continue only the readout equation in (6), using the resulting fixed
hidden features. This switch is part of the method's definition and does
not depend on its observed residual.

Let \(\widehat{\mathsf H}\) contain its fixed top training features.
Dense fitting gives the least singular value of
\(\mathsf H(T)/\sqrt{mn}\) at least \(\sqrt\lambda/2\).
Equation (12) bounds the operator norm difference from
\(\widehat{\mathsf H}/\sqrt{mn}\) by \(CD(T)\). Eventually,

\[
\frac{\widehat{\mathsf H}^{\top}\widehat{\mathsf H}}{mn}
\succeq\frac\lambda8I_m.
\]

The tail residual satisfies the exact linear equation

\[
\dot{\widehat r}
=-\frac{2\widehat{\mathsf H}^{\top}\widehat{\mathsf H}}{mn}
\widehat r,
\qquad
\widehat\rho(t)\le\widehat\rho(T)e^{-\lambda(t-T)/4}.
\]

The fixed feature RMS bound gives
\(\|\dot{\widehat w}\|/\sqrt n\le C\widehat\rho\).
Its integrable tail proves a parameter limit, exact fitting, and

\[
\sup_{t\ge T,\ \|x\|=\sqrt d}
|\widehat f(t,x)-\widehat f(T,x)|
\le\frac C\lambda\widehat\rho(T).
\]

Since \(\rho(T)\le Y(en)^{-16}\) and
\(\widehat\rho(T)\le\rho(T)+CD(T)\), this bound, the dense output-tail
lemma, and the discrepancy at \(T\) give

\[
\sup_{t\ge T,\ \|x\|=\sqrt d}
|\widehat f(t,x)-f_n(t,x)|
\le C_3[D(T)+Y(en)^{-16}]
=n^{-8+o(1)}.
\]

The same inequality includes fitted limits. It eventually implies (2)
for each fixed positive \(Y\). No new label-size restriction has been
introduced.

The method's persistent learned information consists solely of the online
first layer/readout and Legendre moments collected from its own current
training responses. Its temporal basis and freeze times are predetermined.
The dense trajectory, dense analytic coefficients, and source disks appear
only in the proof. No response subspace, dense source coefficient array, or
initialization jet of a labeled future is retained or produced.

## Simplest final construction: one growing physical-time interval

The preceding local-existence and signed-defect arguments do not depend
on using multiple intervals. Set `J=1`, keep the same deterministic `T`,
and use (3)--(9) with `s=0` for the entire interval `0<t<=T`. All moment
vectors start at zero. The continuous branch at zero is defined uniquely
by (7)--(8), so there is no artificial prefix, division by a vanishing
residual, or finite positive startup step. The quantities represented by
`1/t` in the moment equations are interpreted through this branch. This is
an exact mathematical initialization, not a claim that a naive explicit
Euler method handles that removable initial singularity accurately.

Only the analytic approximation argument changes. In this paragraph put

\[
A=\max\{1,T/r_t\}
=\max\left\{1,32\beta^{30L}Y^2
\left(\frac m\gamma\right)^2\sqrt{d+3}
[\log(en)]^{3/2}\right\},\qquad
q=\lceil16A\log(en)\rceil.
\tag{18}
\]

For every growing interval `[0,t]` with `t<=T`, its Bernstein ellipse
of parameter `exp(1/A)` has imaginary half-height
`t sinh(1/A)/2 < r_t` and excess real half-width
`t(cosh(1/A)-1)/2 < r_t`. Therefore it lies in the dense source rectangle
`[-r_t,T+r_t]+i[-r_t,r_t]`. The forward histories and physical backward
histories `b=r delta` have precisely the complex Hilbert bounds in (10).
Substitute `s=(w+w^(-1))/2` into any normalized vector history, expand
its holomorphic Laurent series, and use Cauchy's integral on the circles
`|w|=exp(±1/A)`. Symmetric coefficient pairing supplies a degree-below-`q`
Chebyshev polynomial with uniform error at most

\[
\frac{2B e^{-q/A}}{1-e^{-1/A}}
\le4BAe^{-q/A},
\]

where `B` is the corresponding bound in (10). The Legendre projector
is exact on this polynomial, so the dense endpoint error on **every**
growing interval is at most

\[
4(1+64\sqrt q)BAe^{-q/A}.
\tag{19}
\]

These polynomials are proof witnesses only. No coefficient is computed
from the dense solution; the actual method integrates (5) using its own
current activations and residual-weighted responses.

With (18), `e^(-q/A)<=(en)^(-16)` and `A,q` are polylogarithmic for
each fixed problem. Thus (19) is at most `(en)^(-8)` eventually for
all layers and both histories. Repeat the comparison (12)--(17) with
`epsilon=(en)^(-8)`, stopping at `D<=epsilon`. In (14), the dense part
is now bounded by `epsilon`, while the online-minus-dense part is bounded
by `(1+64 sqrt(q))` times (12)--(13). Hence its right side can again be
enlarged to

\[
C_1q(1+\sqrt{\log(en)})[\varepsilon+D(t)]^2.
\tag{20}
\]

The signed stability factor remains `n^(o(1))`, so the resulting bound is
`D(T)<=n^(-16+o(1))`, strictly improving the stopping condition. All
constants here are independent of width. The real tube is inherited from
dense fitting because this discrepancy tends to zero; in particular the
readout bound required by the signed comparison holds eventually for
each fixed positive `Y`. More precisely, the dense fitting proof supplies
the uniform operator margin `8+1/8<9`, and its readout RMS is at most
`2(Y m/gamma) sqrt(gamma/m)`; the vanishing stopped discrepancy therefore
preserves operators below nine and the larger readout margin used by the
paper's signed-comparison ledger. There is no new label condition or assumption
about the rank, positions, labels, or response directions of the data.

If desired, the subpolynomial gain can be bounded with a universal
coefficient of `sqrt(log(en))`, rather than a dataset-dependent exponent.
Use the explicit constants of the paper's signed comparison:
`X=beta^L`, `z=Y m/gamma`, `M=32 X^21 z sqrt(log(en))`,
`K<=X^9+X^13 M`. On the stopped path the residual integrals are at most
`2z` and `3z`, as above. Thus its exponent is at most

\[
11Kz\le11X^9z+352X^{34}z^2\sqrt{\log(en)}
\le1+\sqrt{\log(en)},
\tag{21}
\]

by the original cap `z<=X^(-30)` and `X>=100`. This is exactly the
same use of the label cap for stability as in the paper; no sample/gap
dependence in the displayed order or storage is removed using that cap.

Freeze the moment arrays, their interval length, and the first layer at
the prescribed `T`; keep training the readout by (6). The fitted-tail
argument above applies unchanged and gives, including the fitted limit,

\[
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |\widehat f(t,x)-f_n(t,x)|\le\frac Yn
\tag{22}
\]

eventually at each fixed confidence. The threshold may depend on every
fixed problem parameter and remains unquantified. The stronger statement
(22) follows because `n^(-16+o(1))<=Y/n` eventually for fixed `Y>0`.
As with the paper, no uniform growing-data or vanishing-label limit is
asserted. Dividing (22) by the imported actual dense-variability lower
bound gives a ratio tending to zero in probability.

The exact retained learned state (including arrays frozen after `T`) is

\[
n(d+1)+2(L-1)mnq+1,
\tag{23}
\]

where the last coordinate is the clamped physical clock. Combining (18)
and (23) gives the explicit bound

\[
C n\left[d+1+Lm\log(en)+
Lm\beta^{30L}Y^2\left(\frac m\gamma\right)^2\sqrt{d+3}
[\log(en)]^{5/2}\right]
=n^{1+o(1)}
\tag{24}
\]

for fixed, separately chosen problem parameters; `C` may be absolute.
The fixed initialized mixers still use `(L-1)n^2` coordinates. No fixed
learned response basis, source coefficient table, hidden updated dense
matrix, or history sample list is omitted from (23). Data storage,
activation evaluators, and transient forward/backward scratch retain the
same exclusions as in the original paper's state count.

The resulting method is an oblivious **temporal** compression: the Legendre
basis, order and freeze schedule use only the qualification parameters;
its stored vectors are its own online moments exactly as in the original
method. It is not dataset-oblivious training, since the usual gradients
necessarily use training data. It changes the original method's clock,
removes its artificial prefix, and specifies a readout-only tail; it does
not assert that merely lowering `q` in the unchanged residual-clock ODE
has this guarantee.

Finally, this is a uniquely defined finite-state evolution with a regular
Volterra initialization branch and a deterministic hybrid switch at `T`.
It is not claimed to be one globally locally-Lipschitz vector field on
all clock states. Its physical parameters are continuous, are classical
away from the prescribed switch, and have a fitted limit. There is no
claim here about an optimal numerical integrator, step size, improved
training/query time, or subquadratic **total** memory.

## Internal check status

The complete candidate, frozen at SHA-256
`7cd8051dda86a6bc7bee09cd46ab51ddce1fb8d21f7891f97148e34cc6137298`,
passed the separate checks in `OBLIVIOUS_RUNTIME_CHECK.md` and
`OBLIVIOUS_SOURCE_CHECK.md`. Both reconstructed the new deterministic
arguments against the stated paper interfaces; neither re-certified the
whole imported probabilistic cavity proof. The reviewers did not author
this construction or use one another's reports, but reused their contexts
from the earlier different-candidate checks rather than starting fresh.
Root also reconstructed the initialization, exact defect, signed bootstrap,
tail and state inventory. After review, only this status, placement of the
probability qualifier, and the explicit already-proved dense operator
margin were added. There are no unresolved mathematical objections within
this scoped check. This is an internally checked study result, not a
promotion; the paper remains unchanged.

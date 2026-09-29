# Local activation modulus: conditional all-time tracking theorem

Scoped proof dependency, 28 September 2026. This note uses only the
coordinator's explicit supplied lemmas, `docs/notation.qmd`, and the complete
`SMALL_LABEL_SPECTRAL_SLACK.md` and `SMALL_LABEL_ENERGY.md`. The
`solve-math-rigorously` skill was applied. No other study, manuscript, code,
experiment, or archived book was read. The supplied small-label existence,
activity, tube, and fitting lemmas are **coordinator-supplied inputs to be
verified elsewhere**. This note proves the implication from those inputs
to consistency and tracking for the broader activation class. It does not
independently establish those inputs or any probabilistic initialization
claim, and it is an internal dependency rather than a promotion review.

## 1. Precise conditional statement

Fix finite depth \(L\), finite data, and canonical mobilities and squared
loss \(m^{-1}\sum_a r_a^2\), where \(r_a=f_a-y_a\). The activations may
depend on the layer and satisfy

\[
 \phi^{(\ell)}\in C^{1,1}_{\mathrm{loc}}(\mathbb R),\qquad
 \max_\ell\| (\phi^{(\ell)})'\|_\infty\le M<\infty,
 \qquad \max_\ell|\phi^{(\ell)}(0)|\le A_0<\infty.
 \tag{1}
\]

Thus \(|\phi^{(\ell)}(u)|\le A_0+M|u|\); no boundedness of the activations
or global Lipschitz constant of their derivatives is assumed. Put

\[
 Y=\left(m^{-1}\sum_a y_a^2\right)^{1/2},\qquad
 B_0=\|w_0\|_2/\sqrt n\le Y\le Y_*\le1.
 \tag{2}
\]

Consider the original autonomous old-clock closure \(\widehat\theta\)
of order \(P\ge1\) and dense flow \(\theta_D\), with identical initial
parameters. All following uniform bounds are supplied by the coordinator.
They hold globally for both paths, with constants independent of \(n,P,Y\):

\[
 \|W_\ell\|_{\mathrm{op}}\le D\quad(2\le\ell\le L),\qquad
 \max_{\ell,a}\frac{\|z_{\ell,a}\|_2+\|h_{\ell,a}\|_2}{\sqrt n}\le R,
 \tag{3}
\]
\[
 \frac{\|w\|_2}{\sqrt n},\quad
 \max_{\ell,a}\frac{\|\delta_{\ell,a}\|_2}{\sqrt n}\le CY,
 \qquad \Gamma_w\succeq\lambda_0 I_m/2,
 \tag{4}
\]
\[
 \int_0^\infty\rho(t)\,dt\le CY,\qquad
 \rho(t)\le CY e^{-\kappa t},\qquad
 \int_t^\infty\rho(s)\,ds\le\rho(t)/\kappa,
 \tag{5}
\]
\[
 \max_{\ell,a}\frac{\|\dot z_{\ell,a}\|_2+
                  \|\dot h_{\ell,a}\|_2}{\sqrt n}\le CY\rho,
 \qquad \frac{\|\dot w\|_2}{\sqrt n}\le C\rho.
 \tag{6}
\]

Here \(\rho=\|r\|_m\) is always the residual of the path being considered.
For the closure, the exact physical equation and supplied relative defect
bound are

\[
 \dot{\widehat\theta}=F(\widehat\theta)+E,\qquad E_1=E_w=0,
 \qquad e_E:=\sum_{\ell=2}^L\|E_\ell\|_F
                       \le CY^{5/2}\widehat\rho.
 \tag{7}
\]

The last part of (5) is an essential input, stronger than merely its
exponential envelope. It follows in the coordinator's source lemma from
\(\dot\rho\le-\kappa\rho\), uniformly from every starting time. It also
follows directly from (3)--(4), (7), and a sufficiently small fixed
\(Y_*\), as checked below. Constants may depend on depth, data, \(M,A_0\),
the fixed initialized operator and RMS bounds underlying (3), and the
fixed Gram margin, but not on the values of local derivative moduli.

Define

\[
 \ell_n=\max_{1\le\ell\le L}
   \operatorname{Lip}\big((\phi^{(\ell)})';[-R\sqrt n,R\sqrt n]\big),
 \qquad \zeta_n=\ell_n\sqrt n\,Y^2.
 \tag{8}
\]

The assignment's scalar \(z_n\) is denoted here by \(\zeta_n\) to
distinguish it from network preactivations. Each \(\ell_n\) is finite
by local Lipschitz regularity; it is permitted to be zero. The conclusion is

\[
 \varepsilon_{n,P}:=\int_0^\infty e_E(t)\,dt
 \le C\left[
 \frac{B_0Y^{3/2}}{P^{3/2}}+
 \frac{Y^{5/2}\sqrt{1+\zeta_n^2+\log(e+P)}}{P^2}\right],
 \tag{9}
\]
\[
 \sup_{t\ge0}d_n(\widehat\theta(t),\theta_D(t))
 \le C e^{CY+C_s\zeta_n}\left[
 \frac{B_0Y^{3/2}}{P^{3/2}}+
 \frac{Y^{5/2}\sqrt{1+\zeta_n^2+\log(e+P)}}{P^2}\right].
 \tag{10}
\]

The distance in (10) is the canonical mobility Hilbert distance:

\[
 d_n^2=\frac{\|\widehat W_1-W_{1,D}\|_F^2}{n}
 +\sum_{\ell=2}^L\|\widehat W_\ell-W_{\ell,D}\|_F^2
 +\frac{\|\widehat w-w_D\|_2^2}{n}.
 \tag{11}
\]

For a constant \(a\ge\max(1,C_s)\), (10) implies a common bound \(C/P\)
on every pair \((n,P)\) satisfying

\[
 P\ge e^{2a\zeta_n}.
 \tag{12}
\]

When \(B_0=0\), the sufficient condition improves to

\[
 P\ge(1+\zeta_n)e^{a\zeta_n}.
 \tag{13}
\]

These are conditions on simultaneous width and memory order. They do not
give a width-uniform bound for every order independently of width. At
\(Y=0\), the assumed \(B_0=0\) makes both paths stationary. The same is
true when their common initial residual is zero. We treat the remaining
case below.

The proof first obtains actual backward-history regularity using the local
modulus and full carrier RMS. A terminal cutoff then gives a backward
projection tail, which pairs with the forward tail to yield (9). Finally
the prediction discrepancy is damped before the parameter discrepancy is
estimated; its activity integral produces the exponential in (10).

## 2. Local chain rule and actual source regularity

For a scalar absolutely continuous path \(u:[0,T]\to I\) and a
Lipschitz function \(g:I\to\mathbb R\) with constant \(K\), the composition
is absolutely continuous and satisfies

\[
 |(g\circ u)'(t)|\le K|u'(t)|\quad\text{for almost every }t.
 \tag{14}
\]

Indeed the Lipschitz inequality transfers the defining disjoint-interval
criterion for absolute continuity from \(u\) to \(g\circ u\); at points
where both derivatives exist, taking difference quotients proves the
bound. This argument needs no choice of \(g'\) at a nondifferentiability
point. The fundamental theorem for absolutely continuous functions then
applies. In our application every coordinate of \(z_{\ell,a}\) lies in
\([-R\sqrt n,R\sqrt n]\) by (3), so (14) with
\(g=(\phi^{(\ell)})'\) gives

\[
 \left|\frac{d}{dt}(\phi^{(\ell)})'(z_{\ell,a,i}(t))\right|
       \le\ell_n|\dot z_{\ell,a,i}(t)|\quad\text{a.e.}
 \tag{15}
\]

There are finitely many coordinates at each width, so the product and
backward recursions hold outside one null set on each finite interval.
No classical second derivative of an activation is required.

The exact hidden-block flow is

\[
 F_\ell=-\frac2m\sum_a r_a\,
                 \frac{\delta_{\ell,a}h_{\ell-1,a}^T}{n}
 \quad(2\le\ell\le L),
 \tag{16}
\]

with first block \(-2m^{-1}\sum_a r_a\delta_{1,a}x_a^T/\sqrt d\)
and readout \(-2m^{-1}\sum_a r_a h_{L,a}\). Since
\(\|uv^T/n\|_F=(\|u\|_2/\sqrt n)(\|v\|_2/\sqrt n)\), (3)--(4)
and sample Cauchy--Schwarz give, using (7) and \(Y\le1\),

\[
 \frac{\|\dot W_1\|_F}{\sqrt n}
       +\sum_{\ell=2}^L\|\dot W_\ell\|_F\le CY\rho.
 \tag{17}
\]

Introduce the full carrier immediately before each backward gate:

\[
 k_{L,a}=w,\qquad k_{\ell,a}=W_{\ell+1}^T\delta_{\ell+1,a}
                         \quad(\ell<L),\qquad
 \delta_{\ell,a}=(\phi^{(\ell)})'(z_{\ell,a})\odot k_{\ell,a}.
 \tag{18}
\]

It obeys

\[
 \frac{\|k_{\ell,a}\|_2}{\sqrt n}\le CY,
 \qquad \|k_{\ell,a}\|_\infty\le\|k_{\ell,a}\|_2\le C\sqrt nY.
 \tag{19}
\]

This estimate includes the learned part of the carrier and requires no
coordinate bound on a feature. By (6), (15), and (19), the RMS of a
gate-derivative term is at most

\[
 \ell_n\|k_{\ell,a}\|_\infty
                   \frac{\|\dot z_{\ell,a}\|_2}{\sqrt n}
             \le C\zeta_n\rho.
 \tag{20}
\]

At the top layer the other term is bounded by \(MC\rho\), using the
readout velocity in (6). At lower layers,
\(\dot k_\ell=\dot W_{\ell+1}^T\delta_{\ell+1}
+W_{\ell+1}^T\dot\delta_{\ell+1}\). The first term has RMS at most
\(CY^2\rho\le C\rho\) by (17), and the second propagates the next
backward derivative with coefficient at most \(D\). Induction through
fixed depth proves

\[
 \max_{\ell,a}\frac{\|\dot\delta_{\ell,a}\|_2}{\sqrt n}
                     \le C(1+\zeta_n)\rho\quad\text{a.e.}
 \tag{21}
\]

For completeness the tangent Gram is

\[
 \Gamma_{ab}=\frac1m\left[
 \frac{h_{L,a}^Th_{L,b}}n+
 \frac{\delta_{1,a}^T\delta_{1,b}}n\frac{x_a^Tx_b}d+
 \sum_{\ell=2}^L\frac{\delta_{\ell,a}^T\delta_{\ell,b}}n
                         \frac{h_{\ell-1,a}^Th_{\ell-1,b}}n\right].
 \tag{22}
\]

It is positive semidefinite and has operator norm at most \(C\), by
(3)--(4) and fixed data. The prediction differential of the defect has

\[
 (JE)_a=\sum_{\ell=2}^L
             \delta_{\ell,a}^TE_\ell h_{\ell-1,a}/n,
 \qquad \|JE\|_m\le CY e_E.
 \tag{23}
\]

The exact residual equation \(\dot r=-2\Gamma r+JE\) thus gives
\(\|\dot r\|_m\le C\rho\). In addition, for the closure,
\(\dot\rho\le-(\lambda_0-CY^{7/2})\rho\), and
\(\dot\rho\ge-C\rho\). Reducing the fixed threshold \(Y_*\) to make
\(CY_*^{7/2}\le\lambda_0/2\) proves the relative decay and tail bound
in (5) with \(\kappa=\lambda_0/2\), and prevents a positive residual
from reaching zero at finite time. The same statements hold for the dense
flow with \(E=0\).

On the closure let \(c=r/\rho\); hence \(\|c\|_m=1\) and
\(|c_a|\le\sqrt m\). Differentiating gives

\[
 \dot c=(\dot r-c\dot\rho)/\rho,\qquad \|\dot c\|_m\le C.
 \tag{24}
\]

The backward history is \(b_{\ell,a}=c_a\delta_{\ell,a}\).
Equations (4), (21), and (24) imply

\[
 \left(\frac1m\sum_a\frac{\|\dot b_{\ell,a}\|_2^2}{n}\right)^{1/2}
             \le C\{Y+(1+\zeta_n)\rho\},
 \tag{25}
\]
\[
 \frac1m\sum_a\int_0^T\frac{\|\dot b_{\ell,a}\|_2^2}{n}\,dt
              \le CY^2(T+1+\zeta_n^2).
 \tag{26}
\]

To obtain (26), square (25), use \((1+\zeta_n)^2\le2(1+\zeta_n^2)\),
and integrate \(\rho^2\le C Y^2e^{-2\kappa t}\). No terminal limit
of \(c\), or integrability of \(\dot c\) over infinite time, is asserted.

## 3. Projection tails and the absolute defect

Use the closure's own clock
\(\tau(t)=1+\int_0^t\widehat\rho(s)\,ds\), so
\(1\le\tau(t)\le A:=1+CY\). Histories have a constant forward prefix
on \([0,1]\) and zero backward prefix there. At the single join point
their chosen value is immaterial for integrals. Let \(\Pi_P^\tau\)
be orthogonal projection onto polynomials of degree below \(P\) on
\([0,\tau]\), acting coordinatewise.

We use the elementary weighted Legendre inequality, in any Hilbert space,

\[
 \int_0^\tau\|q-\Pi_P^\tau q\|^2\,d\xi
 \le\frac1{P(P+1)}
      \int_0^\tau\xi(\tau-\xi)\|q'(\xi)\|^2\,d\xi
 \quad(q\in H^1(0,\tau)).
 \tag{27}
\]

Here the Hilbert norm may be ordinary Euclidean norm divided by
\(\sqrt n\), or the sample direct sum with squared norm
\(m^{-1}\sum_a\|q_a\|_2^2/n\). To verify (27), let \(e_j\) be the
orthonormal shifted Legendre basis. The equation
\(-[\xi(\tau-\xi)e_j']'=j(j+1)e_j\) and integration by parts show
that the \(q\)-coefficient times \(\sqrt{j(j+1)}\) is the ordinary
\(L^2\) pairing of \(\sqrt{\xi(\tau-\xi)}q'\) with
\(\sqrt{\xi(\tau-\xi)}e_j'/\sqrt{j(j+1)}\). The latter functions,
for \(j\ge1\), form an orthonormal family in unweighted \(L^2\),
again by integration by parts. Bessel's inequality yields
\(\sum_{j\ge1}j(j+1)\|\langle q,e_j\rangle\|^2
\le\int\xi(\tau-\xi)\|q'\|^2\). Summing the coefficient squares
over \(j\ge P\) proves (27). Smooth approximation proves the same
calculation for \(H^1\) functions. Hilbert-valued versions follow by
orthonormal-coordinate expansion and nonnegative summation.

Equation (6) gives \(\|\partial_\xi h\|_2/\sqrt n\le CY\) on the
active part of length at most \(CY\); this derivative is zero on the
prefix. Therefore its integrated square is at most \(CY^3\). Applying
(27) and \(\xi(\tau-\xi)\le A^2/4\) proves, uniformly in terminal time,

\[
 \left(\frac1m\sum_a\int_0^{\tau(t)}
       \frac{\|(I-\Pi_P^{\tau(t)})h_{\ell,a}\|_2^2}{n}\,d\xi\right)^{1/2}
                              \le\frac{CY^{3/2}}P.
 \tag{28}
\]

For the backward history collect all samples at one layer in the direct
sum Hilbert space just described. Let \(b_0=b(1+)\). Its norm is at most
\(CB_0\): the initial backward recurrence involves only bounded initial
operators, slopes, and the initial readout, while \(\|c(0)\|_m=1\).
Write, on the entire finite clock interval,

\[
 \widetilde b(\xi)=b(\xi)-b_0\mathbf1_{[1,\tau(\infty))}(\xi).
 \tag{29}
\]

This is continuous at the prefix join, has norm at most \(CY\), and has
the same physical derivative as \(b\) for positive times. For a finite
\(T\), define \(q_T\) to agree with \(\widetilde b\) until \(\tau(T)\)
and to be constant thereafter. On every finite clock interval it belongs
to \(H^1\): the positive residual has a positive lower bound on each
bounded physical interval, so the change of variables and (26) give a
finite derivative integral there. If \(a(s)=\int_s^\infty\rho\), then
on any terminal interval \([0,\tau(t)]\),

\[
 \begin{split}
 \int_0^{\tau(t)}\xi(\tau(t)-\xi)\|q_T'(\xi)\|^2\,d\xi
 &\le\int_0^T\tau(s)a(s)\frac{\|\dot b(s)\|^2}{\rho(s)}\,ds\\
 &\le\frac A\kappa\int_0^T\|\dot b(s)\|^2\,ds
 \le CY^2(T+1+\zeta_n^2).
 \end{split}
 \tag{30}
\]

When \(t<T\), the nonzero integral only reaches \(t\) and extension to
\(T\) increases its bound. When \(t>T\), the derivative is zero after
\(T\). The difference \(\widetilde b-q_T\) is bounded by \(CY\)
and supported in a clock interval of length at most
\(a(T)\le CYe^{-\kappa T}\). Thus

\[
 \|\widetilde b-q_T\|_{L^2(0,\tau(t))}
                   \le CY^{3/2}e^{-\kappa T/2}.
 \tag{31}
\]

Projection contraction, (27), and (30)--(31) give

\[
 \|(I-\Pi_P^{\tau(t)})\widetilde b\|_{L^2}
 \le \frac{CY\sqrt{T+1+\zeta_n^2}}P
                            +CY^{3/2}e^{-\kappa T/2}.
 \tag{32}
\]

The scalar step in (29) has projection tail at most \(C\sqrt{\tau/P}\).
One direct proof for \(P\ge2\) replaces its jump by a linear ramp of
length \(\tau/P\) on a side of the join with at least that much room;
one side always has length at least \(\tau/2\). The replacement has
\(L^2\) error at most \(\sqrt{\tau/P}\) and derivative norm
\(\sqrt{P/\tau}\). Formula (27), with the weight bounded by
\(\tau^2/4\), gives the same tail bound for the ramp. For \(P=1\),
projection contraction suffices. Multiplication by \(b_0\) gives a
contribution at most \(CB_0/\sqrt P\), since \(\tau\le A\le C\).
Choosing \(T=2\kappa^{-1}\log(e+P)\) in (32) proves

\[
 \left(\frac1m\sum_a\int_0^{\tau(t)}
       \frac{\|(I-\Pi_P^{\tau(t)})b_{\ell,a}\|_2^2}{n}\,d\xi\right)^{1/2}
 \le C\left[\frac{B_0}{\sqrt P}
       +\frac{Y\sqrt{1+\zeta_n^2+\log(e+P)}}P\right].
 \tag{33}
\]

To convert tails into absolute velocity defect, retain the exact closure
identity from the allowed source, which is activation-independent:

\[
 E_\ell(t)=\frac{2\rho(t)}m\sum_a
       \frac{(b_{\ell,a}-b_{\ell,a}^*)
                   (h_{\ell-1,a}-h_{\ell-1,a}^*)^T}{n},
 \tag{34}
\]

where a star means projection evaluated at the current right endpoint.
For a fixed history \(q\), its projection-error energy satisfies

\[
 \frac d{d\tau}\int_0^\tau
               \|q(\xi)-\Pi_P^\tau q(\xi)\|^2\,d\xi
       =\|q(\tau)-(\Pi_P^\tau q)(\tau)\|^2
       \quad\text{a.e.}
 \tag{35}
\]

Indeed the derivative of the fitted polynomial is again a polynomial of
degree below \(P\), so its inner product with the projection error is
zero. Its coefficients are absolutely continuous on compact positive
terminal intervals by the invertible polynomial Gram matrix and
absolutely continuous history moments. This proves differentiation even
for the backward history with its prefix jump. Both energies are zero
at \(\tau=1\), since the backward prefix is zero and the forward prefix
is constant. Change variables \(d\tau=\rho\,dt\) in (34), apply the
rank-one Frobenius identity, and apply Cauchy--Schwarz using (35).
It gives

\[
 \int_0^t\|E_\ell(s)\|_F\,ds
 \le\frac2m\sum_a
 \left(\int_0^{\tau(t)}\frac{\|(I-\Pi_P)b_{\ell,a}\|_2^2}{n}\right)^{1/2}
 \left(\int_0^{\tau(t)}\frac{\|(I-\Pi_P)h_{\ell-1,a}\|_2^2}{n}\right)^{1/2}.
 \tag{36}
\]

The omitted differentials in (36) are \(d\xi\), and both projections
use the single final interval \([0,\tau(t)]\). Sample Cauchy--Schwarz,
(28), and (33) prove (9) first on a finite horizon and then on the whole
half-line by monotone convergence of its nonnegative left side. This
is an absolute-defect estimate, not a signed cancellation estimate.

## 4. Stability using full carriers and RMS features

Let \(x\) be the sum of first-block normalized Frobenius discrepancy
and all hidden-block Frobenius discrepancies, let
\(\eta=\|\widehat w-w_D\|_2/\sqrt n\), and put \(d=x+\eta\).
Then \(d_n\le d\le\sqrt{L+1}\,d_n\). Throughout this section the
unadorned residual measure in time integrals is the dense
\(\rho_D(t)\,dt\).

Forward subtraction gives, with constants independent of the local
modulus,

\[
 \max_{\ell,a}\frac{\|\widehat z_{\ell,a}-z_{\ell,a,D}\|_2
                    +\|\widehat h_{\ell,a}-h_{\ell,a,D}\|_2}{\sqrt n}
                                                        \le Cx.
 \tag{37}
\]

At the first layer this uses the normalized input bound. At later layers
write \(\widehat W\widehat h-W_Dh_D
=(\widehat W-W_D)h_D+\widehat W(\widehat h-h_D)\).
The first term's RMS is at most \(R\|\widehat W-W_D\|_F\);
the second has coefficient \(D\). Apply the global slope bound \(M\)
afterwards. This proves (37) by induction without pointwise bounded
features.

For the dense reference full carrier in (18), let
\(G_\ell=\operatorname{diag}((\phi^{(\ell)})'(z_{\ell,a}))\), with
the sample index understood. Equation (19), the Lipschitz bound in (8),
and (37) give

\[
 \frac{\|(\widehat G_\ell-G_{\ell,D})k_{\ell,a,D}\|_2}{\sqrt n}
              \le C\ell_n\sqrt nY\,x.
 \tag{38}
\]

Write \(b_\ell=\max_a\|\widehat\delta_{\ell,a}
-\delta_{\ell,a,D}\|_2/\sqrt n\) and
\(\chi_n=\ell_n\sqrt nY\). At the top,
\(b_L\le M\eta+C\chi_nx\). At lower layers the exact difference is

\[
 \begin{split}
 \widehat\delta_\ell-\delta_{\ell,D}
 ={}&\widehat G_\ell\widehat W_{\ell+1}^T
                 (\widehat\delta_{\ell+1}-\delta_{\ell+1,D})\\
 &+\widehat G_\ell(\widehat W_{\ell+1}-W_{\ell+1,D})^T
                    \delta_{\ell+1,D}
 +(\widehat G_\ell-G_{\ell,D})k_{\ell,a,D}.
 \end{split}
 \tag{39}
\]

The three terms have RMS at most \(MD b_{\ell+1}\), \(CYx\), and
\(C\chi_nx\), respectively. Downward induction proves

\[
 \max_\ell b_\ell\le C[\eta+(Y+\chi_n)x].
 \tag{40}
\]

No carrier is split into initialized and learned parts here. In particular,
the bounded-activation learned-coordinate estimate from
`SMALL_LABEL_ENERGY.md` is not used or asserted.

Let \(q=f_{\widehat\theta}-f_{\theta_D}\), \(v=\|q\|_m\), and
\(Q(t)=\int_0^t v(s)\,ds\). The exact discrepancy equation is

\[
 \dot q=-2\widehat\Gamma q
       -2(\widehat\Gamma-\Gamma_D)r_D+\widehat JE.
 \tag{41}
\]

In (22), the difference of a forward normalized pairing is bounded by
\(CRx\), and that of a backward normalized pairing is bounded by
\(CY b_\ell\), by (3)--(4), (37), and Cauchy--Schwarz. Subtracting
products of these pairings and using (40) gives

\[
 \|\widehat\Gamma-\Gamma_D\|_{\mathrm{op}}
                     \le C[x+Y\eta+Y\chi_n x].
 \tag{42}
\]

For this passage, a sample matrix with entries bounded by \(K/m\) has
operator norm at most \(K\), as follows from its maximum absolute row
and column sums. Equation (23) holds also with hats. Taking the norm
derivative in (41), using \(2\widehat\Gamma\succeq\lambda_0 I\),
and integrating gives

\[
 Q(t)\le C\int_0^t\rho_D(s)
                      [x+Y\eta+Y\chi_nx](s)\,ds
                         +CY\varepsilon(t),
 \qquad\varepsilon(t)=\int_0^t e_E(s)\,ds.
 \tag{43}
\]

Specifically the differential bound is
\(D^+v\le-\lambda_0v+C\rho_D[x+Y\eta+Y\chi_nx]+CY e_E\).
The integrated version follows by regularizing the norm as
\(\sqrt{v^2+\epsilon^2}\), integrating on a finite interval, and
letting \(\epsilon\downarrow0\); \(v(0)=0\) and the terminal \(v\)
can be discarded. Thus there is no unweighted infinite physical-time
integral of parameter error.

Subtracting readout equations using
\(\widehat r\widehat h-r_Dh_D=q\widehat h+r_D(\widehat h-h_D)\)
gives

\[
 \eta(t)\le C Q(t)+C\int_0^t\rho_D(s)x(s)\,ds.
 \tag{44}
\]

In the hidden equations, the corresponding three terms are
\(q\widehat\delta\widehat h^T\),
\(r_D(\widehat\delta-\delta_D)\widehat h^T\), and
\(r_D\delta_D(\widehat h-h_D)^T\). Their canonical Frobenius bounds
are \(CYv\), \(C\rho_D b_\ell\), and \(CY\rho_Dx\), respectively,
using RMS features throughout. The first block has the same bounds with
its fixed input. Include \(E\), sum blocks, and use (40):

\[
 x(t)\le CYQ(t)+C\int_0^t\rho_D(s)
                       [\eta+(Y+\chi_n)x](s)\,ds+\varepsilon(t).
 \tag{45}
\]

Insert (43) into (44)--(45) and use \(Y\le1\). This yields

\[
 d(t)\le C\varepsilon(t)
       +C(1+\chi_n)\int_0^t\rho_D(s)d(s)\,ds.
 \tag{46}
\]

For a fixed terminal time replace the nondecreasing inhomogeneous term
\(C\varepsilon(s)\) by \(C\varepsilon(t)\) on its interval.
Differentiating the resulting integral majorant proves

\[
 \sup_{0\le s\le t}d(s)
 \le C\varepsilon(t)
       \exp\left(C(1+\chi_n)\int_0^t\rho_D(s)\,ds\right)
 \le C\varepsilon_{n,P}e^{CY+C_s\zeta_n},
 \tag{47}
\]

because \(\chi_nY=\zeta_n\). Letting \(t\uparrow\infty\) and using
(9) proves (10). Equations (6), (17), and finite activity also give
finite parameter limits, so their distance satisfies the same bound.

## 5. Algebra of the joint order conditions and scope

Choose \(a\ge\max(1,C_s)\). Under (12),

\[
 e^{C_s\zeta_n}P^{-1/2}\le1,\qquad
 \zeta_n\le\frac{\log P}{2a},\qquad
 e^{C_s\zeta_n}P^{-1}
          \sqrt{1+\zeta_n^2+\log(e+P)}
 \le C_a P^{-1/2}[1+\log(e+P)]\le C_a.
 \tag{48}
\]

After multiplying (10) by \(P\), its first term is bounded using the
first inequality and \(B_0Y^{3/2}\le Y^{5/2}\le1\); its second term
is bounded using the final inequality. The factor \(e^{CY}\) is uniformly
bounded. This proves the \(C/P\) assertion under (12), including \(P=1\)
when \(\zeta_n=0\).

If \(B_0=0\), put \(P_0=(1+\zeta_n)e^{a\zeta_n}\). For fixed
\(\zeta_n\ge0\), the function

\[
 p\longmapsto \frac{\sqrt{1+\zeta_n^2+\log(e+p)}}p
 \tag{49}
\]

is decreasing for \(p\ge1\): the derivative of its logarithm is
\(1/[2(e+p)(1+\zeta_n^2+\log(e+p))]-1/p<0\).
At \(p=P_0\),

\[
 \log(e+P_0)\le\log(e+1)+\log(1+\zeta_n)+a\zeta_n,
 \tag{50}
\]

so \(\sqrt{1+\zeta_n^2+\log(e+P_0)}\le C_a(1+\zeta_n)\).
For every \(P\ge P_0\), (49)--(50) therefore give

\[
 \frac{e^{C_s\zeta_n}
        \sqrt{1+\zeta_n^2+\log(e+P)}}P
 \le C_a e^{(C_s-a)\zeta_n}\le C_a.
 \tag{51}
\]

This proves the zero-readout improvement (13) without losing an extra
factor of two in its exponential constant.

There is exactly one explicit spatial loss: conversion of carrier RMS
to a coordinate maximum in (19). Its local-modulus multiple enters (20)
and (38), producing \(\zeta_n\) in both consistency and stability.
Unbounded activation values are handled solely through (3), RMS product
bounds, and the slope bound; no second factor of \(\sqrt n\) enters.
If all gates are constant on the attained preactivation intervals, then
\(\ell_n=\zeta_n=0\), so both terms disappear without division by the
modulus or any artificial width loss. In particular this covers affine
activations, including unbounded ones.

The result remains conditional on the coordinator's width/order-uniform
source lemmas (3)--(7) and their initialization assumptions. This proof
does not turn those inputs into Gaussian initialization claims, does not
establish an arbitrary-order width-uniform theorem, and does not claim
that the exponential order thresholds are necessary or optimal.

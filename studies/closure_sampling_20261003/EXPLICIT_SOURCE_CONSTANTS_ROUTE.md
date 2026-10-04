# Explicit source constants: independent bounded derivation

2026-10-04. Independent route, frozen before exchanging scientific findings.
This is an internal conditional derivation, not a promotion review. No
experiment, Git operation, runtime edit, or maintained-book edit was made.

The conclusion below quantifies the source prefactor **conditional on an
explicit sufficiently small activity allowance and the inherited local
insertion interface**. The local interface's remainder and net constants
need not be quantified to quantify this prefactor: they enter the eventual
width threshold. The activity smallness conditions that do persist are
listed explicitly. The separate label route must enforce them; this note
does not assert an explicit label theorem by itself.

## 1. Inputs and normalization

Complete current-study inputs read: `DEPTH_INDEPENDENT_EXPONENT.md`,
`DEPTH_INDEPENDENT_EXPONENT_CHECK.md`, `INPUT_DEPTH_REFINEMENT.md`,
`WHOLE_QUERY_RESPONSE_SOURCE.md`, `GENERAL_ANALYTIC_COMPRESSION.md`,
`DEEP_COMPLEX_SOURCE.md`, `DEEP_ACTIVATION_EXTENSION.md`,
`DATASET_SOURCE_CONSTANTS.md`, and `LABEL_SEPARATE_BUDGETS.md`.
The supervisor subsequently authorized the three exact prior-study inputs
`../dense_cutoff_population_rate_20261001/DEPTH_CAVITY_ROUTE.md`,
`DEPTH_INSERTION_CHECK.md`, and `DEPTH_CAVITY_PROBABILITY_CHECK.md` in that
same directory. All three were read completely; their further references
were not followed. In particular the explicit Hessian used below is
equation (11) of that first prior input.

Let hidden depth be \(L\ge2\), input dimension \(d\ge2\), width \(n\),
and sample count \(m\). Inputs \(v_a\) have norm one. Use the canonical
forward pass, with independent Gaussian initialization and zero readout,

\[
 z^{(1)}=Av,\quad z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\quad
 h^{(\ell)}=\phi_\ell(z^{(\ell)}),\quad f=w^\top h^{(L)}/n.
\]

With residuals \(r_a=f(v_a)-y_a\), the mobilities are

\[
 \dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\quad
 \dot W^{(\ell)}=-\frac2{mn}\sum_a
 r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},\quad
 \dot w=-\frac2m\sum_a r_a h_a^{(L)}.
\]

Here \(k_a^{(L)}=w\), \(\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})
\odot k_a^{(\ell)}\), and \(k_a^{(\ell)}=W^{(\ell+1)\top}
\delta_a^{(\ell+1)}\). Write

\[
 \lambda=\min(1,\gamma/m),\quad Y=\|y\|_2/\sqrt m,
 \quad \ell_n=\log(en),\quad
 d\mu=\frac2m\sum_a|r_a|\,|dt|.
\]

Suppose all activations are real on the real axis and bounded by \(B_\phi\)
on \(|\Im z|<b\). Put

\[
 B=\max(1,B_\phi),\qquad
 D_1=\max(1,4B_\phi/b),\qquad
 D_2=\max(1,2B_\phi(4/b)^2),\qquad
 \beta=\max(8,B,D_1,D_2,16/b).
\tag{1}
\]

Cauchy's formula supplies these derivative bounds on the safe strip
\(|\Im z|\le b/2\). \(B\) in this note is the activation bound;
the exponential carrier budget is denoted \(\mathcal B\).

The physical inputs to this route are the following, with strict margins
for the full model and every fixed-size cavity:

\[
 \|W_0^{(\ell)}\|_{\rm op}\le3,\quad
 \|W^{(\ell)}\|_{\rm op}\le4,\quad
 \|A\|_{\rm op}/\sqrt n\le3,\quad
 \mu(\hbox{each real-plus-short-complex contour})\le S\le1,
 \quad Y\le1,\quad \rho\le2Y.
\tag{2}
\]

The real fitting rate needed for the horizon below is \(\kappa\ge\lambda/2\).
For example, if the real theorem supplies that rate, setting \(S=8Y/\lambda\)
leaves a factor-two margin above real absolute activity
\(2\int\rho\le4Y/\lambda\). Short complex pieces use the remaining
margin at sufficiently large width. Gaussian initialization gives the
initialized bounds in (2) at sufficiently large width for each fixed \(d,L\).
The label route must justify the dynamic tube and fitting inputs.

## 2. Sphere geometry introduces no hidden chart count

Use the single periodic trigonometric parameterization from the source
theorem, with \(d-1\) angles. It is a product of plane rotations applied
to a fixed unit vector. A complex plane rotation has operator norm at most
\(e^{|\Im\theta|}\). Its derivatives of every fixed order have the same
bound. Thus when \(r\le1/(8d)\),

\[
 \|v(\theta)\|_2\le2,\qquad
 \|\partial_{\theta_j}v(\theta)\|_2\le2.
\tag{3}
\]

The same bound holds for the second derivatives used in a polynomial
grid argument. The map covers the entire real sphere. It needs no chart
partition, Jacobian integration weight, or additional chart multiplier.
The only geometric count is \(d-1\) angular Fourier indices, and summing
their imaginary displacements costs \(d-1\).

## 3. Explicit deterministic layer recurrences

All constants in this section are finite expressions in \(L,B,D_1,D_2\).
Define forward derivative bounds \(u_\ell,f_\ell\), backward RMS
coefficients \(k_\ell,t_\ell\), and angular RMS coefficients
\(j_\ell,b_\ell\) by

\[
 u_1=2,\quad u_\ell=B+4f_{\ell-1},\quad f_\ell=D_1u_\ell,
\]
\[
 k_\ell=B(4D_1)^{L-\ell},\quad t_\ell=D_1k_\ell,
 \qquad j_\ell=6(4D_1)^{\ell-1},\quad b_\ell=D_1j_\ell.
\tag{4}
\]

Then in mobility coordinates
\(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\),

\[
 \|D_\Theta z^{(\ell)}\|_{\rm op}\le u_\ell,\quad
 \|D_\Theta h^{(\ell)}\|_{\rm op}\le f_\ell,\quad
 \|k^{(\ell)}\|_{2,n}\le Sk_\ell,\quad
 \|\delta^{(\ell)}\|_{2,n}\le St_\ell,\quad
 \|\partial_{\theta_j}z^{(\ell)}\|_{2,n}\le j_\ell.
\tag{5}
\]

Here \(\|a\|_{2,n}=\|a\|_2/\sqrt n\). The forward recurrence bounds
the direct map \(U_Hh/\sqrt n\) by \(B\|U_H\|_F\), then propagates
lower variations. The backward recurrence starts from
\(\|w\|_\infty\le BS\), obtained by integrating the readout equation.
The angular recurrence starts from (2)-(3).

For \(F_a=nf(v_a)\), the hidden part of \(\nabla F_a\) has Euclidean
norm at most \(Sg\sqrt n\), where

\[
 g=t_1+B\sum_{\ell=2}^L t_\ell,\quad
 r_\ell=u_\ell g,\quad q_\ell=f_\ell g.
\tag{6}
\]

Consequently the residual-free forward responses \(R_a^{(\ell)}=
D_\Theta z^{(\ell)}\nabla F_a\) and \(Q_a^{(\ell)}=
D_\Theta h^{(\ell)}\nabla F_a\) have RMS bounds \(Sr_\ell,Sq_\ell\).

The explicit Hessian formula gives the following coefficients:

\[
 h_0=2f_L+2\sum_{\ell=2}^L t_\ell f_{\ell-1},\qquad
 h_2=h_0+D_2\sum_{\ell=1}^L u_\ell^2k_\ell.
\tag{7}
\]

Its two readout terms each have rank at most \(n\) and operator norm
\(f_L\). Each mixed hidden-weight term has rank at most \(n\), operator
norm at most \(St_\ell f_{\ell-1}\), and occurs twice. Each curvature
term is a bounded-map contraction of
\(\operatorname{diag}(\phi_\ell''k_a^{(\ell)})\). Therefore
\(\|D^2F_a\|_{2,n}\le h_2\), with no coordinate maximum.

Let \(0<\eta\le B^{-1}\) be the coefficient in the separate exponential
budgets, stopped at \(2\mathcal B\). Put

\[
 h_1=\eta^{-1}D_2\sum_{\ell=1}^L u_\ell^2.
\]

The deterministic exponential-moment inequality then gives, for every
\(p\ge2\),

\[
 \|D^2F_a\|_{p,n}\le h_0+Sh_1p(2\mathcal B)^{1/p}.
\tag{8}
\]

This also holds for the normalized residual mixture by triangle
inequality. No count of parameters enters (7)-(8).

The mixed second derivative of the forward pass, evaluated on the hidden
gradient argument, has normalized Hilbert--Schmidt bound \(Se_\ell\),
where

\[
 e_1=D_2r_1u_1,\qquad
 e_\ell=D_2r_\ell u_\ell+
 D_1(q_{\ell-1}+t_\ell Bf_{\ell-1}+4e_{\ell-1}).
\tag{9}
\]

The four terms are respectively gate curvature, the matrix-coordinate
Hilbert--Schmidt identity for \(U_HQ/\sqrt n\), the mixed rank-one
weight-gradient term, and propagation of the previous mixed derivative.
Thus \(\|D_\Theta Q_a^{(\ell)}\|_{2,n}\le f_\ell h_2+e_\ell\).
For an angular feature derivative the corresponding recurrence is

\[
 a_1=D_2j_1u_1+2D_1,\qquad
 a_\ell=D_2j_\ell u_\ell+D_1(b_{\ell-1}+4a_{\ell-1}).
\tag{10}
\]

Define

\[
 f_* =\max_\ell f_\ell,\quad
 E_Q=\max_\ell(f_\ell h_2+e_\ell),\quad E_J=\max_\ell a_\ell.
\]

The asymmetric Dyson trace is bounded by

\[
 T_Q=8f_*E_Q\quad\hbox{or}\quad T_J=8f_*E_J,
\tag{11}
\]

provided the activity allowance satisfies the explicit conditions

\[
 Sh_0\le\tfrac14,\qquad
 16eS^2h_1\sqrt{2\mathcal B}\le1.
\tag{12}
\]

Indeed, the term with \(h\ge1\) insertions is bounded by
\(2f_*E\,S^h[h_0+2Sh_1h(2\mathcal B)^{1/(2h)}]^h/h!\).
The factor two bounds the product of base propagators on their total
short non-real contour, at sufficiently large width. Splitting the power
gives the series \(e^{2Sh_0}-1\) and
\(\sqrt{2\mathcal B}\sum_{h\ge1}(4eS^2h_1)^h\), each bounded by one
under (12). The zero-insertion term is at most \(2f_*E\). This proves
(11) with room to spare. These conditions persist in the label threshold;
they cannot be moved into \(n_0\).

## 4. Gaussian coefficients and an explicit complex radius

Set

\[
 K_* =32\max(1,\max_\ell k_\ell,\max_\ell t_\ell),\qquad
 G_d=8\sqrt{d+3}.
\tag{13}
\]

The training carrier maximum can be stopped at
\(M_n=K_*S\sqrt{\ell_n}\). For a single omitted Gaussian root, the
conditional variance of its cavity response pairing is at most
\(S^2\max t_\ell^2\). A mesh of spacing \(n^{-2}\) on the two real
time coordinates, with \(T\le n\), has at most a fixed multiple of
\(n^5\) points. Including neurons, samples, and layers costs at most
\(n^7\) eventually. For a complex Gaussian pairing with variance bound
\(\sigma^2\), splitting real and imaginary parts gives tail
\(4\exp[-u^2/(4\sigma^2)]\). Taking \(u=8\max t_\ell S\sqrt{\ell_n}\)
dominates this grid. Stopped derivatives give an off-grid error
\(n^{-3/2}\operatorname{polylog}(n)\). The finite singleton shift
\(C S(1+S^2\mathcal B)\) is eventually smaller than another such Gaussian
bound. Hence it affects \(n_0\), not (13).

For the query forward/angular Gaussian terms there are \(2d\) real
time/angle coordinates. The same mesh has at most \(n^{4d+1}\) points
eventually; the fixed sample/layer/angle multiplicities and neurons can
be bounded by two more powers. Their RMS coefficients are \(Sq_\ell\)
and \(b_\ell\). The multiplier \(G_d\) in (13) dominates the resulting
tail union. Time and angle derivatives of these stopped sources have
coordinate bounds \(\sqrt n\operatorname{polylog}(n)\), by the exact
response recursions and their first derivatives. Thus the same mesh
suffices. Constants in those derivative bounds affect \(n_0\) only.

Define coordinate-response coefficients

\[
 U_1=4D_1K_*,\qquad
 U_\ell=2\{D_1K_*(B^2+f_{\ell-1}^2+T_Q+Bq_{\ell-1})
                      +G_dq_{\ell-1}+1\},\quad\ell\ge2,
\]
\[
 V_1=2(2G_d+2D_1K_*+1),\qquad
 V_\ell=2\{G_db_{\ell-1}+D_1K_*(T_J+Bb_{\ell-1})+1\},
 \quad\ell\ge2.
\tag{14}
\]

The exact row-insertion identity gives these coefficients term by term:
the direct feature pairing contributes \(D_1M_nB^2\), its direct
reverse trace contributes \(D_1M_nf_{\ell-1}^2\), the same-root integral
contributes \(SD_1M_nT_Q\), and the learned-row correction contributes
\(S^2D_1M_nBq_{\ell-1}\). The centered Gaussian term has coefficient
\(G_dSq_{\ell-1}\). For an angular source there is no direct reverse
observable term; its two corrections are \(SD_1M_nT_J\) and
\(SD_1M_nBb_{\ell-1}\). Using \(S\le1\), these are bounded by (14).
The factor two and the added one give strict margins for vanishing
insertion remainders. Consequently

\[
 \max|R_a^{(\ell)}|\le U_\ell S\sqrt{\ell_n},\qquad
 \max|\partial_{\theta_j}z^{(\ell)}|\le V_\ell\sqrt{\ell_n}.
\tag{15}
\]

Put \(U_* =\max U_\ell\), \(V_* =\max V_\ell\), and define

\[
 c_{d,L,\phi}=
 \min\left\{\frac1{8d},\frac{b}{32[4U_*+(d-1)V_*]}\right\}.
\tag{16}
\]

Then the source radius is explicitly

\[
 r_n=c_{d,L,\phi}\ell_n^{-1/2},\qquad
 T=8\lambda^{-1}\ell_n.
\tag{17}
\]

Along time and angular imaginary segments, the preactivation displacement
is at most
\(r_n[4YSU_*+(d-1)V_*]\sqrt{\ell_n}\le b/32\).
This proves the required strict pole margin. The inherited stopped
insertion/budget argument and deterministic product interpolation remove
the stops exactly as in `DEPTH_INDEPENDENT_EXPONENT.md`. Its complex
Gaussian correction still tends to zero; its now explicit but fixed
derivative coefficients change only the width from which it is small.

For readers preferring one envelope to the recurrence, (4)-(16) imply

\[
 c_{d,L,\phi}^{-1}\le\beta^{40L}(d+3)^{3/2}.
\tag{18}
\]

Here is sufficient exponent accounting, deliberately loose: \(u_\ell,
k_\ell,t_\ell,j_\ell\le\beta^{2L}\), \(f_\ell,b_\ell,g\le\beta^{3L}\),
\(r_\ell\le\beta^{5L}\), \(q_\ell\le\beta^{6L}\),
\(h_2\le\beta^{9L}\), \(e_\ell\le\beta^{11L}\),
\(E_Q\le\beta^{13L}\), \(E_J\le\beta^{8L}\),
\(T_Q\le\beta^{17L}\), \(T_J\le\beta^{12L}\),
\(K_*\le\beta^{3L}\), and
\(U_*,V_*\le\beta^{25L}\sqrt{d+3}\).
Each line follows by substituting the previous lines into its displayed
finite sum or recurrence, using \(L\le\beta^{L-1}\) and \(L\ge2\).
Substitution in (16), with \(b^{-1}\le\beta/16\), proves (18).
This is an envelope of specified expressions, not an assignment of a
guessed exponent to an opaque source constant.

## 5. Magnitude, Fourier factors, and coefficient count

All four whole-query source families are bounded coordinatewise by

\[
 M_n=M_0\sqrt n,\qquad M_0=3\max(B,\max_\ell t_\ell)
                                      \le\beta^{3L}.
\tag{19}
\]

For backward sources use (5) and \(S\le1\); for the initialized
matrix images use their operator bound three. This bound is used only
for approximation, never as the training carrier bound.

The complete approximation calculation can avoid an unspecified
Bernstein-ellipse constant. Set \(c=c_{d,L,\phi}\),
\(\alpha=r_n/(4T)\), and substitute \(t=T(1+\cos u)/2\).
For \(|\Im u|\le\alpha\), this map lies inside the source time
rectangle. The resulting function is even and periodic in \(u\), and
periodic in its \(d-1\) angles. Contour translation in each variable
bounds a Fourier coefficient of multi-index \(k\) by

\[
 M_n\exp[-\alpha|k_0|-r_n\textstyle\sum_{j=1}^{d-1}|k_j|].
\]

For \(0<a\le1\), the sum of \(e^{-a|k|}\) is at most \(3/a\), and
the tail beyond degree \(N\) is at most \(4a^{-1}e^{-aN}\).
Thus, with tolerance \(\epsilon=n^{-1}\), it suffices to put

\[
 P=(3/\alpha)(3/r_n)^{d-1},\quad
 H_n=\log(8d M_nP/\epsilon),\quad
 p=\lceil H_n/\alpha\rceil,\quad J=\lceil H_n/r_n\rceil.
\tag{20}
\]

The Fourier truncation error is at most \(\epsilon/4\). Tensor discrete
Fourier interpolation at \(2p+1\) time-angle nodes and \(2J+1\) nodes
per original angle has at most twice that error: every outside Fourier
coefficient aliases to one retained coefficient, so its additional
coefficient-sum error is bounded by the same outside tail. Evenness in
\(u\) leaves \(p+1\) real temporal cosine coefficients, equivalent to a
degree-\(p\) polynomial in \(t\). There are precisely at most
\((p+1)(2J+1)^{d-1}\) real coefficient vectors per real source family.
Approximating the finitely many nodes from initial jets to a further
accuracy \(\epsilon/[2(2p+1)(2J+1)^{d-1}]\) controls the remaining
interpolation error. This affects temporary precision, not retention.
Identical scalar operations on each initialized-matrix pair preserve
the exact pairing interface.

In (20),

\[
 H_n=\tfrac32\log n+
 \log(256dM_0 3^d\lambda^{-1}c^{-d})
 +\tfrac{d+2}{2}\log\ell_n.
\tag{21}
\]

Increase the already unquantified threshold so that
\(\log(256dM_0 3^d\lambda^{-1}c^{-d})\le\ell_n\) and
\((d+2)\log\ell_n/2\le\ell_n\). Then \(H_n\le4\ell_n\), and

\[
 p+1\le130c^{-1}\lambda^{-1}\ell_n^{5/2},\quad
 2J+1\le11c^{-1}\ell_n^{3/2}.
\]

Four families per layer plus exact initialized additions therefore give

\[
 R\le4(130/c)^d\lambda^{-1}\ell_n^{3d/2+1}+2m+d
 \le[4(130/c)^d+2B^2+d]\lambda^{-1}\ell_n^{3d/2+1}.
\tag{22}
\]

The last step uses the exact trace constraint \(m\lambda\le B^2\).
Optional feature-motion certificate vectors were not requested or counted.
Using (18), a convenient coarser version is

\[
 R\le\beta^{45Ld}(d+3)^{3d/2}
                   \lambda^{-1}\ell_n^{3d/2+1}.
\tag{23}
\]

Consequently an explicit quadratic runtime count multiplies the square of
(23), preserving the requested width power \(3d+2\). Its own layer,
first-weight, metric, data, and residual counts belong to the runtime
route and are not silently absorbed here.

## 6. What remains a condition or a threshold

Actual persistent requirements are the explicit physical input (2), the
rate \(\kappa\ge\lambda/2\), the trace conditions (12), and the
separate-budget/local-insertion smallness conditions needed to prove the
source event. A full explicit label result must choose \(\eta,
\mathcal B,S\) to enforce these, including its singleton moment shift.

The following affect only \(n_0\): Gaussian initialization confidence;
fixed-moment insertion remainder constants and control-net prefactors;
the bounded singleton shift relative to \(S\sqrt{\ell_n}\); complex
base propagation over \(O(r_n)\); the vanishing complex Gaussian
correction; derivative-grid constants; and the logarithmic conditions
under (21). The finite original-width initial-jet work is outside retained
storage by the inherited representation contract.

In particular a constant multiplying a strict negative power of \(n\),
or a fixed coefficient inside a logarithm such as (21), may move into
the eventual threshold. A coefficient in the pole margin cannot: it is
explicitly retained in (16), and subsequently in (22)-(23). The proof
does not turn an unknown \(C_L\) into a claimed \(\exp(L^q)\) envelope.

## 7. Post-exchange reconciliation and independent label audit

2026-10-04. The independent source content above was frozen at SHA-256
b2d6cc7b4423967646699fc12f6b53568079f229fcded71d26749da85279c506.
Restoring stripped inline mathematical delimiters without changing the
science gave 959d325966a88496fd3050295d853c068b16f57e6c0e14ce23fcdb49043e9860.
The supervisor then authorized exchange. I read the complete
EXPLICIT_LABEL_CONSTANTS_ROUTE.md at
0fa619fde5966b55287eaaef6d3c59cc11e3d858964d989741556e173aadcb94
and EXPLICIT_RUNTIME_CONSTANTS_ROUTE.md at
775ed6756af7de018c961173b850ad69930a71e4273c669bfe71c93182987bcd.
The following conventions supersede Sections 1--6's numerical tube,
activity, and horizon choices.

Use the label route's activation constants
\[
 B=\max(1,B_\phi),\quad s=\max(1,4B/a),\quad
 t=\max(1,32B/a^2),\quad \beta=\max(10,B,s,t,16/a).
 \tag{24}
\]
The initialized, real, and complex hidden-operator caps are \(8,9,10\).
The real residual rate is \(\lambda/4\). Take
\[
 S=16Y/\lambda,\qquad T=32\lambda^{-1}\ell_n.
 \tag{25}
\]
Real absolute residual activity is at most \(S/2\), and each extended
contour has activity at most \(S\) for sufficiently large width. Complex
residual RMS is at most \(2Y\); readout maximum is at most \(BS\).
One may use \(\|A\|_{\rm op}/\sqrt n\le10\). For the initialized
first matrix, the label route's Gaussian net proof gives failure at most
\(2\exp[-8n+(n+d)\log9]\) for cap eight, tending to zero at fixed \(d\).
Normalized first-weight displacement is at most \(sK_1S^2<1\), as
verified below, and the short complex extension keeps a strict margin.

### 7.1 Independent check of the exponential budget

Let \(P_\ell,K_\ell,A_H,D_H,H,H_2,D,G,\mathcal M,\mathcal M_c,
\mathcal B,S_*\) denote exactly the explicit quantities in equations
(6)--(21) of the label route. I reconstructed the closure directly.

Each mixed Hessian term factors through a width-dimensional space. Each
curvature term contains one carrier diagonal. The top diagonal has
coordinate bound \(K_LS\) and is explicitly included in \(A_H\).
The others obey the exponential-budget moment bound. Consequently
\[
 \|D^2F_a\|_{p,n}\le A_H+SD_Hp(2\mathcal B)^{1/p},
 \qquad \|D^2F_a\|_{2,n}\le H_2.
 \tag{26}
\]
These estimates also hold for the augmented Hessian and its response
endpoint blocks.

Splitting the \(h+2\) factors in the singleton Dyson trace gives first
sum \(4H^2(e^{2HS}-1)\) and budget-dependent sum
\[
 8e^2H^2S^2\mathcal B
       \sum_{h\ge1}(2eHS^2)^h(h+2)^2.
 \tag{27}
\]
For \(q\le1/2\), \(\sum_{h\ge1}q^h(h+2)^2\le36q\): after division
by \(q\), the series has nonnegative coefficients and value \(36\) at
\(q=1/2\). Thus (27) is at most \(576e^3H^3\mathcal BS^4\).
Adding \(2H_2^2\), the direct external trace and the learned-column
term proves the stated shift \(DS(1+S^2\mathcal B)+o(1)\), with no
sample or deletion-count factor.

For the real activity modulus, the cutoff
\(R_c=4\log(8\sqrt{2\mathcal B}/v)\) makes the high-carrier gate term
at most \(sSv\). This follows from \(x^2e^{-x/2}\le16\), the budget,
and the gate-difference bound \(2s\). The low-carrier term is
\(tV_\ell S^3R_cv\). Using
\[
 R_c\le10\log(e+\mathcal B)+4\log(1/v),\qquad
 v\log(1/v)\le2\sqrt v/e
\]
gives the exact coefficient \(14tV_\ell\). The changed-matrix term
is \(Bs^3K_{\ell+1}^2S^3v\), and the top gate term is
\(2BtV_LS^3v\). These account for every term in its \(G_\ell\)
recurrence.

The dyadic Gaussian threshold allocation has total failure
\(4e^{-4}(1-4e^{-4})^{-1}e^{-z^2}<e^{-z^2}\); its threshold sum is
below \(32G(1+z)\). Integrating that tail gives
\[
 \mathbb E e^{qZ}\le e^{32qG}
 \left[1+32qG\int_0^\infty e^{32qGz-z^2}\,dz\right]
 \le\mathcal M(q).
 \tag{28}
\]
Completing the square gives the exponent \(256q^2G^2\). The vanishing
complex correction has second exponential moment at most two eventually,
so Cauchy--Schwarz gives \(\mathcal M_c=\sqrt{2\mathcal M(2)}\).
This is a single-sample calculation on a cavity-measurable path.

Finally \(\mathcal B=2L+8(L-1)\mathcal M_ce^D\) and
\(DS^2\mathcal B\le\log2\) give moment ratio at most \(1/4\).
Collision tuples have finite fixed-multiplicity moments by (28) and
vanish after normalization. At each fixed \(p\), the limiting hit
probability is at most \(m4^{-p}\); taking the width limit first and then
the infimum over \(p\) removes the stop. I found no numerical defect in
this closure.

The sharper source trace conditions (12) are automatic:
\[
 D\ge4(e^2-1)H^2\ge24H^2,\quad \mathcal B\ge8e^D,\quad
 S\le\mathcal B^{-1/2},\quad A_H,D_H\le H.
\]
Therefore
\[
 SA_H\le H e^{-12H^2}/\sqrt8<1/4,\qquad
 16eS^2D_H\sqrt{2\mathcal B}\le8eH e^{-12H^2}<1.
 \tag{29}
\]
The trace bound \(8f_*E\) thus holds with
\((h_0,h_1,h_2)=(A_H,D_H,H_2)\) and carrier exponent one, without a
new label restriction. Also \(H_2\ge2s+4K_1\) and \(D\ge2H_2^2\);
hence \(D\) dominates \(sK_1\), proving \(sK_1S^2\le sK_1/\mathcal B<1\).

### 7.2 Reconciled source recurrences

In (4)--(16), substitute exactly
\[
 u_\ell=P_\ell,\quad f_\ell=sP_\ell,\quad
 k_\ell=K_\ell,\quad t_\ell=sK_\ell,\quad
 j_\ell=20(10s)^{\ell-1},\quad b_\ell=sj_\ell,
 \tag{30}
\]
replace propagation multiplier \(4\) by \(10\) in (9)--(10),
replace \(D_1,D_2\) by \(s,t\), and put
\((h_0,h_1,h_2)=(A_H,D_H,H_2)\). Keep the formulas for
\(g,r_\ell,q_\ell,E_Q,E_J,T_Q,T_J,U_\ell,V_\ell\). The Gaussian
grid multipliers need no change. Put
\[
 K_{\rm src}=32\max(1,\max_\ell K_\ell,\max_\ell sK_\ell).
 \tag{31}
\]
Then \(\max|k|\le K_{\rm src}S\sqrt{\ell_n}\) on the source horizon.
This coefficient has no input-dimension factor: the carrier grid has
only the two real time coordinates.

With \(U_*=\max U_\ell,V_*=\max V_\ell\), take
\[
 c=\min\{(8d)^{-1},a/[32(4U_*+(d-1)V_*)]\},\quad
 r_n=c\ell_n^{-1/2},\quad
 M_0=8\max(B,\max_\ell sK_\ell).
 \tag{32}
\]
All four source families have coordinate magnitude at most \(M_0\sqrt n\).
Use \(\alpha=r_n/(4T)\) in (20), with horizon (25). Its logarithm is now
\[
 H_n=\tfrac32\log n+
 \log(1024dM_0\,3^d\lambda^{-1}c^{-d})
       +\tfrac{d+2}{2}\log\ell_n.
 \tag{33}
\]
The same eventual logarithmic conditions give \(H_n\le4\ell_n\), hence
\[
 p+1\le514c^{-1}\lambda^{-1}\ell_n^{5/2},\qquad
 2J+1\le11c^{-1}\ell_n^{3/2}.
 \tag{34}
\]
For \(d\ge2\), include the constant vector in addition to exact initialized
features, their images, and the first columns:
\[
 R\le4(520/c)^d\lambda^{-1}\ell_n^{3d/2+1}+2m+d+1.
 \tag{35}
\]
The trace constraint \(m\lambda\le B^2\) absorbs these additions.

For \(d=1\), the sphere is the two-point set \(\{-1,+1\}\).
Use both separate time-only query families, rather than one empty-angle
parameterization. There are at most eight families per layer, and
\[
 R\le8(p+1)+2m+2
 \le8(520/c)\lambda^{-1}\ell_n^{5/2}+2m+2.
 \tag{36}
\]
The same source radius works (there are no angular segments), and the
envelope below absorbs the factor two. This supplies the \(d=1\) case
without incorrectly identifying its two queries.

### 7.3 Runtime normalization and activation-only envelopes

One exact wording repair is needed in the frozen runtime interface.
Its item 3 defines carrier scale as the actual activity
\(\int_0^T\rho_n(t)\,dt\). The source proves a bound normalized by the
allowance \(16Y/\lambda\); no reverse inequality between these scales
was supplied. The runtime proof only uses
\[
 M\le1+4K(Y/\lambda)\sqrt{\ell_n}.
 \tag{37}
\]
Require (37) directly and choose \(K=8+4K_{\rm src}\). This supplies
the initialized operator cap and the approximation-error multiplier too.
Every subsequent runtime estimate is unchanged. Its coefficient \(K\)
is independent of input dimension.

Here is sufficient exponent accounting for the label route:
\[
\begin{array}{c|c@{\quad}c|c}
 C_*&\beta^{6L}&P_\ell&\beta^{3L}\\
 K_\ell&\beta^{2L}&H,H_2&\beta^{10L}\\
 T_0&\beta^{22L}&T_1&\beta^{34L}\\
 E&\beta^{7L}&D&\beta^{36L}\\
 V_\ell&\beta^{6L}&G&\beta^{12L}\\
 \log\mathcal M_c&\beta^{26L}&\log\mathcal B&\beta^{38L}
\end{array}
 \tag{38}
\]
The symbols in this table are the label route's constants. Use
\(10s\le\beta^2\), \(L\le\beta^{L-1}\), and substitute in its finite
sums. In the modulus recurrence its inhomogeneous part is at most
\(\beta^{9L}\); propagation through at most \(L\) layers gives
\(G\le\beta^{12L}\). Moreover
\[
 \log\mathcal M(2)
 \le64G+\log(1+64G\sqrt\pi)+1024G^2\le1216G^2.
\]
Thus \(\log\mathcal M_c\le609G^2\le\beta^{26L}\), and
\(\mathcal B\le10L\mathcal M_ce^D\) gives the final table entry.
The logarithm of the reciprocal of each entry in \(S_*\)'s defining
minimum is at most \(\beta^{38L}\); for its last entry use
\[
 \tfrac12(\log D+\log\mathcal B-\log\log2)\le\beta^{38L}.
\]
Absorbing the factor \(16\) and the real fitting minimum gives the
certified lower bound on the evaluated sufficient coefficient
\[
 c_{L,\phi}\ge\exp[-\beta^{40L}].
 \tag{39}
\]
In particular \(Y/\lambda\le\exp[-\beta^{50L}]\) is a simpler sufficient
label restriction with slack.

For the substituted source recurrence, sufficient bounds are
\[
\begin{array}{c|c@{\quad}c|c}
 f_\ell,g&\beta^{4L}&r_\ell,q_\ell&\beta^{7L},\ \beta^{8L}\\
 e_\ell&\beta^{14L}&E_Q,E_J&\beta^{15L},\ \beta^{9L}\\
 T_Q,T_J&\beta^{20L},\ \beta^{14L}&K_{\rm src}&\beta^{4L}\\
 U_*,V_*&\beta^{30L}\sqrt{d+3}&M_0&\beta^{4L}
\end{array}
 \tag{40}
\]
For example (9)'s inhomogeneous part is bounded by a multiple of
\(\beta^{10L+1}\); propagation by \(10s\le\beta^2\) and summation over
at most \(L\) terms gives \(\beta^{14L}\). The other entries follow
by substitution into (10)--(14). Equations (32), (35)--(36) imply,
for every \(d\ge1\),
\[
 c^{-1}\le\beta^{40L}(d+3)^{3/2},\quad
 R\le\beta^{50Ld}(d+3)^{3d/2}\lambda^{-1}\ell_n^{3d/2+1},
 \quad K=8+4K_{\rm src}\le\beta^{5L}.
 \tag{41}
\]
In the \(d=1\) count, the factor \(8\cdot520\) in (36) is absorbed by
the gap between \(\beta^{40L}\) and \(\beta^{50L}\), already for
\(\beta=10,L=2\). The exact initialized additions are smaller still.

For compatibility with the runtime envelope, its real activation norm
\(B_{\rm rt}\) is at most \(\beta\), so
\[
 X=64B_{\rm rt}(K+1)\le\beta^{7L},\quad
 Q=X^{16L+48}\le\beta^{280L^2},\quad 40Q^2\le\beta^{600L^2}.
 \tag{42}
\]
For \(L\ge2,\beta\ge10\), \(\exp[-\beta^{50L}]\le Q^{-1}\).
Thus the simple source label cap also enforces the runtime's optional
explicit cap. These statements check substitution into the runtime
envelope, rather than independently reconstructing its full cancellation.

The exponential-budget closure passes this independent reconstruction.
The only interface issue found is the actual-activity wording repaired
by (37). The final stochastic width threshold remains unquantified with
the original fixed-data and positive-label qualifications.

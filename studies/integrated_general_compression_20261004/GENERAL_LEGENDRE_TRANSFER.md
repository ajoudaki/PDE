# General Legendre transfer and the numerical small-label interface

2026-10-04. Scoped continuation in the new integrated study. This note reuses
only the explicitly authorized prior-study sources named at the end. It is an
internal derivation, not an independent promotion review. No maintained source
or earlier study was changed.

The general same-width theorem transfers to the requested strip-holomorphic
activation class, including unbounded activation values. It supplies one event
per width for every memory order, physical-time and whole-sphere suprema, and
fitted endpoints. The explicit order below makes its error little-o of
`n^(-1/2)`. Consequently an explicit positive eventual error prefactor does
not require evaluating the inherited comparison constants. The unresolved
numerical inheritance is the label threshold for the finite-width carrier
estimate. The proposed `beta_partial^(-62L)` activity threshold is not a
numerical consequence of the old theorem without an additional bound described
in Section 5.

## 1. Model, activation class, and Gram normalization

Fix the hidden depth \(L\ge2\), input dimension \(d\), sample count \(m\),
and training inputs \(x_a\in\mathbb R^d\), \(\|x_a\|=\sqrt d\), independently
of width. Write \(v_a=x_a/\sqrt d\). The dense network is
\[
 z_a^{(1)}=W^{(1)}v_a,\qquad
 z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
 h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),\qquad
 f_a=\frac{w^\top h_a^{(L)}}n.
\]
Here \(W^{(1)}\in\mathbb R^{n\times d}\), the other hidden matrices are
\(n\times n\), and \(w\in\mathbb R^n\). All initialized blocks are independent:
first-layer entries are standard Gaussian, later hidden entries have variance
\(1/n\), and \(w(0)=0\). Let
\[
 r_a=f_a-y_a,\quad \rho=\left(\frac1m\sum_a r_a^2\right)^{1/2},
 \quad Y=\left(\frac1m\sum_a y_a^2\right)^{1/2},\quad \mathcal L=\rho^2.
\]
The block mobilities are \((n,1,\ldots,1,n)\). In terms of the backward
responses
\[
 k_a^{(L)}=w,\quad
 k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)},\quad
 \delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)},
\]
the dense updates are
\[
 \dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,
 \quad \dot W^{(\ell)}=-\frac2{mn}\sum_a
 r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},\quad
 \dot w=-\frac2m\sum_a r_a h_a^{(L)}.                     \tag{1}
\]

The limiting initialized feature covariance is defined recursively by
\[
 (Q_0)_{ab}=v_a^\top v_b,\qquad
 (Q_\ell)_{ab}=\mathbb E[\phi_\ell(G_a)\phi_\ell(G_b)],
 \quad G\sim N(0,Q_{\ell-1}).
\]
The user's gap is the **unweighted** gap
\(\gamma=\lambda_{\min}(Q_L)>0\). Put \(\lambda=\gamma/m\) only as a
proof shorthand: the mean-loss readout Gram tends to \(Q_L/m\).
No raw-input Gram gap, orthogonality, or automatic nonaffinity criterion is
needed. Exact data quotients require their own weighted convention; this
principal statement uses the supplied positive unweighted gap directly.

Assume each \(\phi_\ell\) is real on the real axis and holomorphic on
\(\{z:|\operatorname{Im}z|<a\}\), with bounded first derivative there.
Cauchy's formula applied to \(\phi_\ell'\) implies bounded second and third
derivatives on the half-strip. Thus the finite quantity
\[
 \beta_\partial=\max\left\{10,
 1+\max_\ell|\phi_\ell(0)|,\frac{16}{a},
 \max_{\ell,\ 1\le j\le3}
 \sup_{|\operatorname{Im}z|<a/2}|\phi_\ell^{(j)}(z)|\right\}
                                                               \tag{2}
\]
controls all real derivative bounds used in the inherited theorem. Its
activation hypothesis is only real \(C^3\) with bounded first three
derivatives. Values need not be bounded, because
\[
 |\phi_\ell(u)|\le |\phi_\ell(0)|+
                   \|\phi_\ell'\|_\infty|u|.
\]
The strip assumption is stronger than what this particular transfer needs.

## 2. The original autonomous closure

For each reconstructed layer \(\ell=2,\ldots,L\), sample \(a\), and mode
\(j=0,\ldots,q-1\), the closure stores two \(n\)-vector histories
\(\bar h_{a,j}^{(\ell-1)}\) and \(\bar\delta_{a,j}^{(\ell)}\), along with
its first matrix, readout, and scalar clock. Its own forward pass and residual
are evaluated using
\[
 \widehat W^{(\ell)}=W_0^{(\ell)}-
 \frac2{mn\tau}\sum_{a=1}^m\sum_{j=0}^{q-1}(2j+1)
 \bar\delta_{a,j}^{(\ell)}\bar h_{a,j}^{(\ell-1)\top}.       \tag{3}
\]
The physical-time equations are
\[
 \dot\tau=\widehat\rho,\qquad \tau(0)=1,
\]
\[
 \dot{\bar h}_{a,j}^{(\ell-1)}=
 \widehat\rho\widehat h_a^{(\ell-1)}-
 \frac{\widehat\rho}{\tau}
 \left(j\bar h_{a,j}^{(\ell-1)}+
             \sum_{i<j}(2i+1)\bar h_{a,i}^{(\ell-1)}\right),
\]
\[
 \dot{\bar\delta}_{a,j}^{(\ell)}=
 \widehat r_a\widehat\delta_a^{(\ell)}-
 \frac{\widehat\rho}{\tau}
 \left(j\bar\delta_{a,j}^{(\ell)}+
             \sum_{i<j}(2i+1)\bar\delta_{a,i}^{(\ell)}\right).  \tag{4}
\]
The first matrix and readout use (1) at the reconstructed state. The forward
zeroth modes start at the initialized features; the other forward modes and
all backward modes start at zero. These are a constant unit forward prefix
and zero backward prefix. Formulas (3)–(4) are regular at zero residual.
The auxiliary dense histories introduced below are proof objects only.

## 3. What the inherited theorem proves

There is a fixed positive threshold \(Y_*\), depending on the fixed
activation, data, and depth, such that every fixed \(0<Y\le Y_*\) has the
following conclusion. Both dense training and every order of (3)–(4) exist
for all physical times, fit the training labels, and converge in their
physical parameters. There are fixed \(C_0,K_0<\infty\) and events
\(\Omega_n\), \(\mathbb P(\Omega_n)\to1\), on which, simultaneously for all
positive integers \(q\),
\[
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |\widehat f_{n,q}(t,x)-f_{n,D}(t,x)|
 \le C_0e^{K_0\sqrt{\log(e+n)}}
                     \frac{\sqrt{\log(e+q)}}{q^2}.          \tag{5}
\]
The bracket \([0,\infty]\) includes the physical limits at infinity.
The same right side, with another fixed prefactor, bounds the normalized
physical parameter distance
\[
 D_{n,q}=\sup_{t\in[0,\infty]}\left[
 \frac{\|\widehat W^{(1)}-W_D^{(1)}\|_F}{\sqrt n}
 +\sum_{\ell=2}^L\|\widehat W^{(\ell)}-W_D^{(\ell)}\|_F
 +\frac{\|\widehat w-w_D\|_2}{\sqrt n}\right].             \tag{6}
\]
Forward subtraction through bounded slopes and physical operator bounds
makes the prediction discrepancy at any \(x\) at most
\(C(1+\|x\|/\sqrt d)D_{n,q}\); hence a whole-sphere supremum, rather than
only a sphere integral, is legitimate.

The event in (5) comes from one actual dense carrier envelope and a
physical fitting tube independent of \(q\). Large orders use the projection
absorption inequality; smaller orders use the all-order physical tube and
an enlarged exponent \(K_0\). There is no union bound over orders.
For each fixed confidence \(1-\delta\), every sufficiently large individual
width has probability at least \(1-\delta\). The sources do not claim one
event for an infinite family of independently initialized widths.

For \(Y=0\), both systems are stationary and coincide. There is no
population approximation or width-bias remainder in this theorem.

## 4. A specified order and any positive eventual prefactor

Set \(s_n=\log(e+n)\) and
\[
 q_n=\left\lceil n^{1/4}\exp(s_n^{3/4})\right\rceil.        \tag{7}
\]
Since \(q_n\le2n^{1/4}e^{s_n^{3/4}}\) and \(s_n\ge1\),
\(\log(e+q_n)\le4s_n\). The right side of (5) is therefore at most
\[
 \frac{2C_0}{\sqrt n}\sqrt{s_n}
       \exp(K_0\sqrt{s_n}-2s_n^{3/4})=o(n^{-1/2}).          \tag{8}
\]
This strengthens the immediate \(C_0/\sqrt n\) consequence: for **any
specified positive** \(C_{\rm target}\), (8) is at most
\(C_{\rm target}/\sqrt n\) at all sufficiently large widths. A sufficient
additional condition, still involving the source's unknown constants, is
\[
 s_n\ge\max\left\{1,K_0^4,
       [2\log_+(2C_0/C_{\rm target})]^{4/3}\right\},       \tag{9}
\]
where \(\log_+(u)=\max(0,\log u)\). Indeed the first two bounds turn
(8)'s multiplier into \(2C_0\sqrt s e^{-s^{3/4}}\), and
\(\log s\le s^{3/4}\) for \(s\ge1\) makes this at most
\(2C_0e^{-s^{3/4}/2}\). Differentiation shows
\(q^{-2}\sqrt{\log(e+q)}\) decreases for \(q\ge1\), so the same event
and target prefactor apply to every integer \(q\ge q_n\).

In particular, for fixed \(Y>0\), one may choose
\[
 C_{\rm target}=\beta_\partial^{124L}Y(m/\gamma)^{3/2}.     \tag{10}
\]
This statement is valid under the inherited condition \(Y\le Y_*\).
It does **not** establish that
\[
 Y\le (\gamma/m)\beta_\partial^{-62L}                     \tag{11}
\]
implies that condition. Nor does (9) give a numerical width prescription
until \(C_0,K_0\), and the confidence threshold are evaluated. An explicit
eventual prefactor and an explicit sufficient-width threshold are different
claims.

The logarithm of (7) divided by \(\log n\) tends to \(1/4\), while
\(\log(q_n/n)=-3\log n/4+o(\log n)\to-\infty\). Thus
\(q_n=n^{1/4+o(1)}=o(n)\). More generally,
\(q_n=\lceil n^{1/4}e^{\sqrt{s_n}g(s_n)}\rceil\) works for any prescribed
function with \(g(s)\to\infty\) and \(g(s)=o(\sqrt s)\), provided
\(\log(e+q_n)=O(s_n)\). The concrete choice (7) needs no unknown coefficient.

The moving state has exactly
\[
 2(L-1)mnq+n(d+1)+1                                     \tag{12}
\]
real coordinates. The initialized hidden mixers require an additional
\((L-1)n^2\) fixed coefficients in the explicit-matrix representation.
At (7), moving storage is \(n^{5/4+o(1)}\); total storage remains
\(\Theta(n^2)\). A strict eventual root-width target gives sufficient
moving storage \(\epsilon^{-5/2+o(1)}\) and total storage
\(\Theta(\epsilon^{-4})\), for fixed problem and confidence. These are
representation costs, not lower bounds for alternative models.

## 5. The exact numerical carrier bridge still required

The inherited proof uses residual decay \(\rho\le Ye^{-\kappa t}\) and
sets \(S=2Y/\kappa\). For each neuron it controls the running maxima
\[
 Z_i^{(\ell)}=\max_a\sup_t|z_{a,i}^{(\ell)}(t)|,
 \quad K_i^{(\ell)}=\max_a\sup_t|k_{a,i}^{(\ell)}(t)|
\]
through the stopped joint budget
\[
 \frac1n\sum_{\ell,i}
    e^{\eta(Z_i^{(\ell)}+K_i^{(\ell)}/S)}\le B.           \tag{13}
\]
Rectangular neuron deletion retains both its forward forcing and reverse
force; at the top it also retains the omitted prediction offset multiplying
both forces. The complete local sources prove the following two scalar
inequalities, with \(u_i=K_i/S\):
\[
 u_i\le G_{\delta,i}/S+C_1(1+S^2B)(1+Z_i)+o(1),
 \quad
 Z_i\le G_{h,i}+C_2S^2(1+S^2\sqrt B)u_i+o(1).            \tag{14}
\]
Here \(G_h,G_\delta\) are the independently stopped cavity Gaussian-path
suprema. The coefficients \(C_1,C_2\) depend on the fixed problem and on
choices in the proof. They are not given numerical activation/data/depth
bounds in the old sources. Their explicit absorption conditions include
\[
 S^2B\le1,\qquad 8C_1C_2S^2\le1.                         \tag{15}
\]
The first and last layer have corresponding one-sided absorptions.

Three further quantitative requirements precede the final carrier theorem:

1. The cavity variational propagator uses the Hessian decomposition into a
   negative Gram part and a residual Hessian. If \(C_H\) denotes the
   coefficient in its operator estimate, the source needs
   \[
    \|J(t,s)\|_{\rm op}\le
       \exp\{C_H S(1+M_n)\}\le n^{1/1000},\qquad
    M_n=(2S/\eta)\log(e+n)                               \tag{16}
   \]
   for all sufficiently large widths. A sufficient strict coefficient
   condition is \(2C_HS^2/\eta<1/1000\). The source's normalized Schatten
   trace series also needs its numerical geometric-series ratio below one.
   Both requirements appear as unspecified sufficiently-small choices.

2. Singleton insertion and (14) give
   \[
    Z_i+K_i/S\le C_{\rm abs}(1+G_{h,i}+G_{\delta,i}/S)+o(1).
   \]
   The fixed-block moment argument has an order-independent base
   \(D_\eta(B,S)\). It must satisfy
   \[
     L D_\eta(B,S)<B,\qquad
     \sum_{\ell=1}^L
       \mathbb E e^{\eta\max_a|(G_{\ell-1})_a|}<B/2,
     \quad G_{\ell-1}\sim N(0,Q_{\ell-1}).                \tag{17}
   \]
   The second condition is the initialized joint-budget margin. The old
   proof establishes \(D_\eta(B,S)=B^{o(1)}\), or a stronger budget-independent
   bound after another smallness restriction. It does not evaluate this
   base in terms of (2), \(m,d,L,\gamma\). In particular its maximum over
   training examples has a fixed-data Gaussian supremum constant.

3. Choose the budget first, then the label threshold satisfying (15)–(16),
   the trace-series convergence, and the response-modulus smallness. The
   empirical moment limit is taken at fixed moment degree; only afterward
   is the degree sent to infinity. These choices may not depend on moment
   degree. A selected finite width or a growing-deletion argument does not
   replace this condition.

Together those conditions imply, on events of probability tending to one,
\[
 \sup_{t\ge0}\max_{a,\ell,i}|k_{D,a,i}^{(\ell)}(t)|
       \le C_{\rm car}S\sqrt{\log(e+n)}.                 \tag{18}
\]
The all-time extension is already checked: use the physical tube after
\(T_n=c\log(e+n)\), with \(c\kappa>1\), to bound the remaining coordinate
carrier movement by \(CSn e^{-\kappa T_n}=o(S)\).

Therefore the precise missing implication for the benchmark is that (11)
permits choices \(\eta,B\) satisfying (15)–(17) and the trace-series
conditions with numerical coefficients derived from the proposed physical
tube. An explicit fitting inequality alone does not supply that implication.
This is a missing quantitative refinement of a proved fixed-problem theorem,
not an unidentified qualitative probability assumption.

Two possible refinements deserve distinction from established inputs. One
can choose \(\eta\) small to keep Gaussian exponential moments moderate,
but then (16) worsens through \(1/\eta\). Also, retaining the sharper
backward scale \(Y/\sqrt\lambda\) separately from residual activity
\(Y/\lambda\) may improve this tradeoff; the inherited proof collapses both
into \(S\). Neither refinement has numerical bounds in the borrowed source.

## 6. An explicit deterministic tracking interface

The following fresh calculation makes the deterministic comparison concrete
without claiming to solve Section 5. It uses no strip estimate. Assume dense
and all closure orders already satisfy, with known constants,
\[
 \rho_j(t)\le Ye^{-\kappa t},\quad
 \int_t^\infty\rho_j\le\rho_j(t)/\kappa,\quad
 \|W_j^{(\ell)}\|_{\rm op}\le9\ (\ell\ge2),\quad
 \|h_{j,a}^{(\ell)}\|_2/\sqrt n\le2H,\quad
 \|w_j\|_2/\sqrt n\le R,
\]
and their full physical tangent Grams have gap at least \(\kappa/2\).
Here \(j\in\{D,q\}\), \(H\ge1\). In the coordinator's proposed tube,
\(\kappa=\lambda/2\) and \(R=2Y/\sqrt\lambda\).
Assume also the two explicit closure outputs
\[
 \max_{a,\ell}\|\dot{\widehat h}_a^{(\ell)}\|_2/\sqrt n
       \le V_h\widehat\rho,
 \qquad \|\dot{\widehat c}\|_m\le C_c,
 \quad \widehat c_a=\widehat r_a/\widehat\rho,             \tag{19}
\]
where \(\|u\|_m^2=m^{-1}\sum_a u_a^2\). For \(Y>0\), residuals are
positive at finite times, as in the source fitting theorem. These are
precisely the additional outputs needed from a quantitative fitting proof.

Put \(s=\max(1,\max_\ell\|\phi_\ell'\|_\infty)\),
\(t_2=\max_\ell\|\phi_\ell''\|_\infty\), and define
\[
 T=9s,\quad F=2HT^{L-1},\quad B_\delta=sT^{L-1}R,
 \quad P=1+2H(L-1),\quad G=PB_\delta+2H.
\]
If the actual dense carrier maximum is at most \(M\), define
\[
 B_{\rm diff}(M)=sT^{L-1}(1+B_\delta)
                       +Lt_2FT^{L-1}M,
\]
\[
 J_{\rm diff}(M)=P B_{\rm diff}(M)
                      +[1+(L-1)B_\delta]sF.             \tag{20}
\]
Forward subtraction gives normalized preactivation discrepancy at most
\(Fd_n\). Backward subtraction multiplies a gate difference by a dense
carrier at most \(M\), and propagates existing differences by \(T\).
The readout, changed-hidden-matrix, and gate terms then give respectively
the three contributions in \(B_{\rm diff}\). Thus the response discrepancy
is at most \(B_{\rm diff}(M)d_n\).

For the normalized physical coordinates
\((W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)\), the sample output
gradient has blocks
\[
 g_a=\left(\delta_a^{(1)}v_a^\top/\sqrt n,
      (\delta_a^{(\ell)}h_a^{(\ell-1)\top}/n)_{\ell=2}^L,
      h_a^{(L)}/\sqrt n\right).
\]
Its sum of block norms is at most \(G\); that of its difference is at
most \(J_{\rm diff}(M)d_n\). Consequently the mean tangent Gram difference
has operator norm at most \(2GJ_{\rm diff}(M)d_n\).

Let \(E_\ell\) be the physical closure defect and
\(\epsilon=\int_0^\infty\sum_{\ell=2}^L\|E_\ell\|_Fdt\). Its residual
forcing has norm at most \(2HB_\delta\sum_\ell\|E_\ell\|_F\). Damped
residual subtraction followed by parameter subtraction and Gronwall gives
\[
 D_{n,q}\le A(M)\epsilon,
\]
\[
 A(M)=\left(1+\frac{4GHB_\delta}{\kappa}\right)
 \exp\left\{2J_{\rm diff}(M)
       \left(1+\frac{4G^2}{\kappa}\right)\frac Y\kappa\right\}. \tag{21}
\]
For verification, the integrated residual difference is bounded by
\(4GJ_{\rm diff}\kappa^{-1}\int\rho_Dd_n+
 2HB_\delta\kappa^{-1}\epsilon\). Multiplying it by the parameter
velocity coefficient \(2G\) gives exactly (21).

The dense normalized preactivation speed is at most \(V_z\rho_D\), and
its response speed at most \(V_\delta(M)\rho_D\), where the explicit
recursive bounds are
\[
 V_z=2FB_\delta P,\qquad
 V_\delta(M)=T^{L-1}
 [4sH+4sH(L-1)B_\delta^2+Lt_2MV_z].                     \tag{22}
\]
Let \(a_0=Y/\kappa\), so the closure clock has endpoint at most \(1+a_0\).
The weighted Legendre inequality and (19), using the constant prefix, give
\[
 \max_{a,\ell}
 \frac{\|(I-\Pi_q)\widehat h_a^{(\ell)}\|_{L^2}}{\sqrt n}
 \le\frac{F_h}{q},\qquad
 F_h=V_h a_0\sqrt{(1+a_0)/2}.                            \tag{23}
\]
Indeed \(\int_1^A\xi(A-\xi)d\xi\le A(A-1)^2/2\).

Record the dense response in the closure clock as
\(\widetilde b_a=\widehat c_a\delta_{D,a}\), with zero prefix, and freeze it
after physical time \(u\). Its sample-averaged normalized derivative is at
most \(C_cB_\delta+V_\delta(M)\rho_D\). In the weighted derivative energy,
\(A-\widehat\tau(t)\le\widehat\rho(t)/\kappa\) cancels the inverse closure
clock speed. Freezing costs at most \(2B_\delta\sqrt{a_0}e^{-\kappa u/2}\).
Take \(u=2\log q/\kappa\), including zero when \(q=1\), and set
\[
 B_q(M)=\frac{2\sqrt{1+a_0}}\kappa C_cB_\delta\sqrt{\log q}
       +\frac{\sqrt{1+a_0}Y}\kappa V_\delta(M)
       +2B_\delta\sqrt{a_0}.                            \tag{24}
\]
The sample-averaged backward projection error is at most
\(B_q(M)/q+B_{\rm diff}(M)\sqrt{a_0}D_{n,q}\). No factor \(\sqrt m\)
is needed: the residual direction has \(\|\widehat c\|_m=1\), and one
uses Cauchy–Schwarz in the sample average in the exact defect identity.

That identity is the product of forward and backward projection errors,
with coefficient \(2/m\) per hidden layer. Equations (23)–(24) imply
\[
 \epsilon\le2(L-1)F_h\left[
 \frac{B_q(M)}{q^2}+
 \frac{B_{\rm diff}(M)\sqrt{a_0}D_{n,q}}q\right].          \tag{25}
\]
Therefore the fully numerical sufficient absorption condition and bound are
\[
 q\ge4(L-1)F_hB_{\rm diff}(M)\sqrt{a_0}A(M)
 \quad\Longrightarrow\quad
 D_{n,q}\le\frac{4(L-1)A(M)F_hB_q(M)}{q^2}.              \tag{26}
\]
Every quantity in (26) is explicit in the physical inputs (19) and the dense
carrier envelope. This proves the deterministic interface independently of
the unnamed constants in the borrowed tracking calculation.

For a numerical whole-sphere Lipschitz factor, suppose additionally
\(\|W_j^{(1)}\|_{\rm op}/\sqrt n\le R_1\). Put
\(b=\max_\ell|\phi_\ell(0)|\), \(Q_1=b+sR_1\),
\(Q_\ell=b+9sQ_{\ell-1}\), and \(Q=\max(1,Q_1,\ldots,Q_L)\).
Forward subtraction on the sphere and readout expansion give
\[
 \sup_{t,x:\|x\|=\sqrt d}|\widehat f-f_D|
       \le[Q+RsQT^{L-1}]D_{n,q}.                         \tag{27}
\]
Physical convergence supplies the same bound at the fitted endpoint.
The numerical coefficient in (26) is not a replacement for the independent
probability and label-admissibility requirement (18).

## 7. Source record and status

The complete following authorized files were read, including their corrections:

- `dense_cutoff_population_rate_20261001/DEPTH_EXTENSION_RESULT.md`;
- `DEPTH_TRACKING_ROUTE.md` and `DEPTH_TRACKING_CHECK.md`;
- `DEPTH_RESPONSE_MODULUS.md` and `DEPTH_RESPONSE_MODULUS_CHECK.md`;
- `DEPTH_CAVITY_ROUTE.md`, `DEPTH_CAVITY_PROBABILITY_CHECK.md`, and
  `DEPTH_INSERTION_CHECK.md`;
- `UNBOUNDED_ACTIVATION_CANDIDATE.md`, `UNBOUNDED_INSERTION_CHECK.md`, and
  `UNBOUNDED_ACTIVATION_CHECK.md`;
- `closure_sampling_20261003/INTEGRATED_LEGENDRE_REUSE.md` and its check.

The first directory prefix applies to its following unqualified filenames.
The source model and explicit positive gap suffice here, so no automatic
activation-gap classification or other study result was invoked. Required
canonical notation, neural response-memory conventions, and rigorous proof
instructions were applied.

The inherited source proves the general qualitative small-label theorem.
Equations (7)–(10) establish the explicit schedule and eventual prefactor.
Equations (19)–(27) give a new numerical deterministic interface. Completing
(11) as a sufficient label condition requires the coefficient bounds in
Section 5; none is silently supplied by an internal PASS verdict.

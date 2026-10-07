# Certified restarted dense Taylor continuation for Harmonic setup

2026-10-06. Author-derived scoped candidate, frozen before receiving another
current route's findings. This note is not an independent review or promotion.
The initial freeze had SHA-256
`be877b71714c06490b02725e384b0bb6696ff1dd4ab38b2f06c8ca98565f1ea8`.
The supervisor's subsequent audit corrected the inherited late complex-strip
margin from a quarter-strip to three eighths and halved the corresponding
parameter-tube allowance; inline mathematical delimiters were also repaired.

The user now permits reconstruction of the dense reference during setup when
its certified arithmetic cost is near quadratic in width. Under that clarified
contract, local Taylor continuation supplies the paired Harmonic source values
in \(n^{2+o(1)}\) non-activation arithmetic at fixed structural parameters and
polynomial accuracy. It uses \(O((\log(en))^{3/2})\) numerical panels and Taylor
degree \(O(\log(en))\). The panels cover a physical training horizon
\(T=O(\log(en))\); physical time is not an operation count.

The activation backend is stated separately, exactly as in `RESULT.md`.
Arbitrary strip analyticity by itself does not assert computability or a
unit-cost high-order derivative oracle. The near-quadratic total-arithmetic
claim holds when the specified scalar jet backend costs a polynomial in its
degree. Without such a backend hypothesis, the fully general result is a
near-quadratic arithmetic bound plus the explicitly counted scalar jet costs.
The last section records this precise remaining computational qualification.

The scientific inputs are `RESULT.md`, `POLYNOMIAL_SETUP_ODE_ROUTE.md`,
`POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md`, and `docs/notation.qmd`. In particular,
the source probability event and its complex extension are imported, not
reproved. The older statements in the two route notes excluding complete dense
path reconstruction are superseded by the user's present cost-based permission.
No other study or historical research input was read. The required canonical
notation skill again returned an operating-system permission error; the
previously authorized fallback uses the accessible rigorous-math skill, the
book notation contract, and the user's explicit notation rules.

## 1. Model, imported event, and claimed output

Write \(v=x/\sqrt d\), so the query sphere is \(\|v\|_2=1\). The
network, its backward fields, and the normalized parameter coordinates are

\[
z^{(1)}=Av,\qquad z^{(j)}=W^{(j)}h^{(j-1)},\qquad
h^{(j)}=\phi_j(z^{(j)}),\qquad f_n=w^Th^{(L)}/n,
\]
\[
k^{(L)}=w,\qquad
\delta^{(j)}=\phi_j'(z^{(j)})\odot k^{(j)},\qquad
k^{(j)}=(W^{(j+1)})^T\delta^{(j+1)},
\]
\[
\theta=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)
\in\mathbb R^P,\qquad P=nd+(L-1)n^2+n.
\tag{1}
\]

Let \(r_a=f_n(v_a)-y_a\), \(\rho=\|r\|_2/\sqrt m\),
\(Y=\|y\|_2/\sqrt m\), \(\lambda=\gamma/m\), and
\(S=16Y/\lambda\). With \(\xi_a=\nabla_\theta f_n(v_a)\), the
mean-square-loss flow with the prescribed mobilities is

\[
\dot\theta=F(\theta),\qquad
F(\theta)=-\frac2m\sum_a r_a\xi_a(\theta).
\tag{2}
\]

The complex extension of this equation uses the algebraic transpose and no
complex conjugations. Norm bounds below are ordinary complex Euclidean or
Frobenius bounds; they do not use positivity of a complex Gram matrix.

Assume \(Y>0\), the full original common label interval, and the original
source and analytic-extension width gates. All activations are the original
strip-holomorphic activations, with possibly unbounded values. Let
\(b=\max_j|\phi_j(0)|\), and let \(s\ge1,t_2\ge1\) bound their
first and second derivatives on \( |\operatorname{Im}z|\le a/2\).
The imported event gives, on the real trajectory,

\[
\|A\|_{\rm op}/\sqrt n<9,\quad
\|W^{(j)}\|_{\rm op}<9,\quad
\|w\|_2/\sqrt n\le2Y/\sqrt\lambda,
\]
\[
\rho(t)\le Ye^{-\lambda t/2},\quad
\int_0^\infty\rho(t)\,dt\le2Y/\lambda,
\quad \max_{a,j,i,t\ge0}|k_{a,i}^{(j)}(t)|
 \le2K_{\rm src}S\sqrt{\log(en)}.
\tag{3}
\]

For every finite source horizon, the exact trajectory is holomorphic on the
source time neighborhood with radius \(r_t=c_t/\sqrt{\log(en)}\),
including its endpoint neighborhoods. Its joint passive-query extension has
preactivation imaginary parts at most \(3a/8\), operator caps ten, feature RMS
bounds \(H_j^{\rm src}\), and readout RMS at most \(SH_L^{\rm src}\).
Along every complex disk of radius \(r_t/2\) centered on a nonnegative real
time, its residual RMS is at most \(2Y\). These are the source-domain and
late-extension conclusions of `RESULT.md`.

The task of this note is to supply at any finite list of real time/query nodes
all four families

\[
h^{(j)},\quad W_0^{(j)}h^{(j-1)},\quad
\delta^{(j)},\quad W_0^{(j+1)T}\delta^{(j+1)},
\tag{4}
\]

with the existing boundary-layer omissions, with coordinate error at most a
given \(\delta_{\rm node}>0\), and with exact initialized-matrix pairing.
For the certified quadrature route one uses

\[
\delta_{\rm node}=\frac{\eta}{64N A_d\mathcal Y_J^2}\quad(d\ge2),
\qquad \delta_{\rm node}=\frac{\eta}{64N_1}\quad(d=1).
\tag{5}
\]

Here \(N,N_1,A_d,\mathcal Y_J\) are exactly the quantities defined in
`POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md`. In its fixed-parameter polynomial
accuracy regime, \(\log(1/\delta_{\rm node})=O(\log(en))\).

## 2. Complex endpoint estimates with explicit coefficients

The constants in this section apply to complex parameters with operator caps
eleven, readout RMS at most
\(R=1+SH_L^{\rm src}\), and preactivations in the safe half-strip.
The extra margin is used only for the numerical restart proof. Define

\[
H_1=\max(1,b+11s),\qquad
H_j=\max(1,b+11sH_{j-1}),
\]
\[
B_j=Rs(11s)^{L-j},\qquad
P_1=1,\quad P_j=H_{j-1}+11sP_{j-1},\quad P_* =\max_jP_j.
\tag{6}
\]

For \(M\ge0\), define

\[
\kappa_L(M)=1,\qquad
\kappa_j(M)=11s\kappa_{j+1}(M)
           +11t_2MP_{j+1}+B_{j+1},
\]
\[
D_j(M)=s\kappa_j(M)+t_2MP_j,\qquad
\kappa_*(M)=\max_j\kappa_j(M),
\]
\[
G=H_L+B_1+\sum_{j=2}^LB_jH_{j-1},
\]
\[
J(M)=sP_L+D_1(M)+
\sum_{j=2}^L\{H_{j-1}D_j(M)+B_jsP_{j-1}\}.
\tag{7}
\]

Every coefficient is explicit, and \(\kappa_*,D_j,J\) are bounded by
affine functions of \(M\), with fixed structural coefficients.

Let \(u,v\) be two such states, \(E=\|u-v\|_2\), and suppose only
the carriers at \(v\) have coordinate bound \(M\). Subtracting the
forward recursion gives

\[
\frac{\|z^{(j)}(u)-z^{(j)}(v)\|_2}{\sqrt n}\le P_jE,
\qquad
\frac{\|h^{(j)}(u)-h^{(j)}(v)\|_2}{\sqrt n}\le sP_jE.
\tag{8}
\]

For the first layer this uses \(\|\Delta A\|_F/\sqrt n\le E\).
For a later layer use

\[
z^{(j)}(u)-z^{(j)}(v)
=W^{(j)}(u)\Delta h^{(j-1)}+\Delta W^{(j)}h^{(j-1)}(v),
\]

whose two normalized bounds are \(11sP_{j-1}E\) and \(H_{j-1}E\).
The straight scalar segment between each pair of preactivations remains in
the half-strip, justifying the complex derivative bound used here.

For the backward subtraction use the carrier at \(v\):

\[
\Delta\delta^{(j)}
=\phi_j'(z^{(j)}(u))\odot\Delta k^{(j)}
 +[\phi_j'(z^{(j)}(u))-\phi_j'(z^{(j)}(v))]\odot k^{(j)}(v).
\]

The second term has RMS at most \(t_2MP_jE\). For \(j<L\),

\[
\Delta k^{(j)}
=(W^{(j+1)}(u))^T\Delta\delta^{(j+1)}
 +(\Delta W^{(j+1)})^T\delta^{(j+1)}(v).
\]

The two costs are \(11D_{j+1}(M)E\) and \(B_{j+1}E\), while
the top readout cost is \(E\). Induction proves

\[
\frac{\|\Delta k^{(j)}\|_2}{\sqrt n}\le\kappa_j(M)E,
\qquad
\frac{\|\Delta\delta^{(j)}\|_2}{\sqrt n}\le D_j(M)E.
\tag{9}
\]

The gradient blocks are

\[
\xi_a=\left(\delta_a^{(1)}v_a^T/\sqrt n,
 (\delta_a^{(j)}h_a^{(j-1)T}/n)_{j=2}^L,h_a^{(L)}/\sqrt n\right).
\]

Their norms are bounded by \(B_1,B_jH_{j-1},H_L\). In a hidden
block the difference splits into
\(\Delta\delta\,h(u)^T+\delta(v)\Delta h^T\); (8)--(9) then give

\[
\|\xi_a(u)\|_2\le G,\qquad
\|\xi_a(u)-\xi_a(v)\|_2\le J(M)E.
\tag{10}
\]

If the parameter segment from \(v\) to \(u\) is in the same admissible
domain, integration of the first gradient bound also gives
\(|f_a(u)-f_a(v)|\le GE\). Consequently

\[
\|F(u)-F(v)\|_2
\le [2G^2+2\rho(v)J(M)]\|u-v\|_2.
\tag{11}
\]

Indeed subtract (2) as
\(-2m^{-1}\sum_a[(r_a(u)-r_a(v))\xi_a(u)
+r_a(v)(\xi_a(u)-\xi_a(v))]\), and apply sample Cauchy--Schwarz
to both sums. Equations (8)--(11) require a carrier bound at one endpoint,
not a hypothesized bound on an unknown numerical trajectory.

## 3. Uniform complex carriers for the true reference

The early source event supplies the complex carrier maximum

\[
M_0=K_{\rm src}S\sqrt{\log(en)}
\]

through \(T_0=32\lambda^{-1}\log(en)\), including the short complex
time pieces. The late-extension proof puts every later complex disk in the
fixed safe parameter ball about \(\theta(T_0)\) and gives

\[
\|\theta(\zeta)-\theta(T_0)\|_2\le Z_n,
\quad
Z_n=\left(\frac{2Y}{\sqrt\lambda}
       +8Y\sqrt{\mathcal K}\,r_t\right)(en)^{-16}.
\tag{12}
\]

Here \(\mathcal K\) is the explicit source Gram bound in `RESULT.md`.
The existing extension gate makes this distance less than half the radius
of that ball. Its straight parameter segments are in the safe half-strip.
Use (9), anchored at \(\theta(T_0)\), and convert RMS to a coordinate
bound. Thus at every real anchor's disk of radius \(r_t/2\), for all
training carriers,

\[
\max_{a,j,i}|k_{a,i}^{(j)}(\zeta)|\le M_c,
\qquad M_c=M_0+\sqrt n\,\kappa_*(M_0)Z_n.
\tag{13}
\]

At fixed positive admissible labels and other structural parameters,
\(M_c=O(\sqrt{\log(en)})\). This derivation fills the possible
late-complex-carrier gap without another stochastic event or another label
restriction. It does not assert that arbitrary points in the full late
parameter ball have that maximum.

## 4. A complex restart disk from a nearby real anchor

Define the parameter tube radius, Lipschitz coefficient, disk radius, and
velocity bound by

\[
b_n=\min\left\{\frac14,\frac{a}{16\sqrt nP_*},
                    \frac1{\sqrt n\kappa_*(M_c)}\right\},
\]
\[
L_n=2G^2+2(2Y+G)J(M_c+1),\qquad
R_n=\min\{r_t/2,(4L_n)^{-1}\},\qquad V=2G(2Y+G).
\tag{14}
\]

The use of \(b_n\) here is local to this note; it is not the differently
defined late-extension radius in `RESULT.md`. At fixed parameters,

\[
b_n^{-1}=O(\sqrt{n\log(en)}),\quad
L_n=O(\sqrt{\log(en)}),\quad
R_n^{-1}=O(\sqrt{\log(en)}).
\tag{15}
\]

Fix a real time \(t\ge0\). On \( |\zeta|\le R_n\), consider the
moving parameter balls centered at \(\theta(t+\zeta)\) with radius
\(b_n\). Every such ball lies in the activation domain. To prove this,
follow a straight parameter segment from its center, stopped at first
half-strip exit. The forward bounds (8) apply before that exit, and each
coordinate changes by at most
\(\sqrt nP_*b_n\le a/16\). Its center has imaginary parts at most
\(3a/8\), so the result stays below \(7a/16<a/2\) and the alleged first exit cannot occur. Operator caps eleven and
readout cap \(R\) also hold since the change is at most \(1/4\).

Equation (9) and (13) show that every state in each moving ball has carrier
maximum at most
\(M_c+\sqrt n\kappa_*(M_c)b_n\le M_c+1\).
The segment between any two states in the ball remains in it. Their residual
RMS is at most \(2Y+Gb_n\le2Y+G\). Hence (11) proves the uniform,
genuine pairwise Lipschitz bound \(L_n\) throughout each ball. This is
where control at the exact complex endpoint is converted into a usable
neighborhood for numerical restarts.

Let the real restart value \(u_0\) satisfy

\[
\|u_0-\theta(t)\|_2\le b_n/4.
\tag{16}
\]

On the Banach space of vector functions continuous on the closed disk and
holomorphic inside it, with supremum norm at most \(b_n\), define

\[
(\mathcal Te)(\zeta)=u_0-\theta(t)
 +\int_0^\zeta
 [F(\theta(t+z)+e(z))-F(\theta(t+z))]\,dz.
\tag{17}
\]

The integrand is holomorphic, so its integral is independent of path in the
disk; bounding it along the straight radius gives

\[
\|\mathcal Te\|_\infty\le b_n/4+L_nR_nb_n\le b_n/2,
\quad
\|\mathcal Te-\mathcal T\widetilde e\|_\infty
\le\tfrac14\|e-\widetilde e\|_\infty.
\]

Iteration is Cauchy, converges uniformly on the disk, and its limit remains
holomorphic by uniform convergence on every smaller circle and the Cauchy
integral formula. Passing to the integral equation proves existence of its
fixed point; the same contraction inequality proves uniqueness. Consequently
\(v_t(\zeta)=\theta(t+\zeta)+e(\zeta)\) solves (2) and starts at
\(u_0\). Moreover,

\[
\|v_t-\theta(t+\cdot)\|_\infty
\le\frac43\|u_0-\theta(t)\|_2\le b_n/3,
\qquad \|v_t'\|_\infty\le V.
\tag{18}
\]

This proof establishes the complex restart disk directly; it does not assume
that analyticity about the exact anchor automatically transfers to a perturbed
anchor. Conjugating the equation and using uniqueness shows \(v_t\) is real
on the real diameter. The exact reference is only a proof device: the algorithm
below computes coefficients from \(u_0\) and the initialized data.

## 5. Taylor tail, continuous defect, and global error budget

Let \(p_t\) be the degree-\(K\) Taylor polynomial of \(v_t\) about zero.
Since \(\|v_t(\zeta)-u_0\|_2\le VR_n\), its coefficients obey
\(\|[\zeta^k]v_t\|_2\le VR_n^{1-k}\) for \(k\ge1\), by the
vector-valued Cauchy integral formula. On \(0\le h\le R_n/2\), summing
the resulting geometric series and its derivative gives

\[
\|p_t(h)-v_t(h)\|_2\le VR_n2^{-K},
\quad
\|p_t'(h)-v_t'(h)\|_2\le V(2K+4)2^{-K}.
\tag{19}
\]

If \(VR_n2^{-K}\le b_n/3\), the polynomial and the exact restarted
solution stay in the same moving ball, so (11) applies to them. Since
\(L_nR_n\le1/4\), their continuous ODE defect satisfies

\[
\|p_t'(h)-F(p_t(h))\|_2
\le V(2K+5)2^{-K}.
\tag{20}
\]

For clarity, the real defect-stability constants imported from
`POLYNOMIAL_SETUP_ODE_ROUTE.md` are reproduced here with a superscript
\({\rm r}\) so they are not confused with (6)--(7). Put

\[
H_1^{\rm r}=\max(1,b+10s),\quad
H_j^{\rm r}=\max(1,b+10sH_{j-1}^{\rm r}),\quad H^{\rm r}=H_L^{\rm r},
\]
\[
R^{\rm r}=1+2Y/\sqrt\lambda,\quad
B^{\rm r}=R^{\rm r}s(10s)^{L-1},\quad
F_z^{\rm r}=H^{\rm r}(10s)^{L-1},\quad
P^{\rm r}_{\rm layer}=1+(L-1)H^{\rm r},
\]
\[
D^{\rm r}(M)=(10s)^{L-1}\{s(1+B^{\rm r})+Lt_2F_z^{\rm r}M\},
\]
\[
J^{\rm r}(M)=\sqrt{L+1}\{P^{\rm r}_{\rm layer}D^{\rm r}(M)
 +[1+(L-1)B^{\rm r}]sF_z^{\rm r}\},
\]
\[
C^{\rm r}(M)=sF_z^{\rm r}\sqrt L+LB^{\rm r}sF_z^{\rm r}
 +\tfrac12L^2t_2(F_z^{\rm r})^2M.
\tag{21}
\]

Use \(M=2K_{\rm src}S\sqrt{\log(en)}\), and abbreviate the last two
values by \(J^{\rm r},C^{\rm r}\). Define

\[
A_n=4J^{\rm r}Y/\lambda,\qquad K_q=R^{\rm r}(10s)^{L-1},
\]
\[
C_{\rm src}=8\sqrt{L+1}\max\{sF_z^{\rm r},
(10s)^{L-1}[s(1+B^{\rm r})+Lt_2F_z^{\rm r}K_q]\}.
\tag{22}
\]

The real lemma states: for an absolutely continuous numerical path \(u\),
let \(d=u'-F(u)\) and
\(E_0=\|u(0)-\theta(0)\|_2+\int_0^T\|d\|_2dt\). If

\[
E_0\le e^{-A_n}/4,\qquad
8(C^{\rm r}+J^{\rm r})^2T e^{2A_n}E_0^2\le1,
\tag{23}
\]

then \(\sup_{[0,T]}\|u-\theta\|_2\le2e^{A_n}E_0\). Its proof keeps
the negative sample prediction-error square before applying the scalar energy
inequality; it is not the exponential of a worst-case Jacobian times \(T\).
The same note proves each coordinate of (4), including initialized images,
has error at most \(C_{\rm src}n\|u-\theta\|_2\) on the whole real
query sphere. This uses only deterministic query RMS bounds, and hence does
not need passive-query carrier maxima.

For \(T>0\), choose the following total allowed defect:

\[
\varepsilon_d=e^{-A_n}\min\left\{
\frac14,\ \frac1{\sqrt8(C^{\rm r}+J^{\rm r})\sqrt T},\
\frac{\delta_{\rm node}}{2C_{\rm src}n},\ \frac{b_n}{8}\right\}.
\tag{24}
\]

Choose the explicit integer

\[
K=\max\left\{8,
\left\lceil2\log_2\max\{1,4TV/\varepsilon_d\}\right\rceil,
\left\lceil\log_2\max\{1,3VR_n/b_n\}\right\rceil\right\}.
\tag{25}
\]

For \(K\ge8\), \(2K+5\le4\,2^{K/2}\): it holds at eight, and the
ratio of the left side at \(K+1\) to its value at \(K\) is less than
\(\sqrt2\). Thus (25) ensures both

\[
TV(2K+5)2^{-K}\le\varepsilon_d,
\qquad VR_n2^{-K}\le b_n/3.
\tag{26}
\]

Set \(N_{\rm step}=\lceil2T/R_n\rceil\), and divide \([0,T]\) into
that many equal panels. Initialize \(u(0)=\theta(0)\). On each panel compute
the degree-\(K\) Taylor polynomial from its already computed initial value,
and take its endpoint as the next initial value. This creates a continuous,
piecewise polynomial, absolutely continuous real path.

This procedure is well defined through the whole horizon. Inductively, all
already constructed panels have defect bounded by (20), so their total defect
is at most \(\varepsilon_d\). The real stability lemma, applied to that
prefix with the conservative full-horizon constants in (23)--(24), gives

\[
\|u(t)-\theta(t)\|_2\le2e^{A_n}\varepsilon_d\le b_n/4
\tag{27}
\]

at its final endpoint. Thus the next panel satisfies the restart hypothesis
(16), and (19)--(20) give the same defect bound for that panel. The initial
case is exact. Finite induction constructs every panel; no assumption about
the yet-uncomputed numerical path has been used. Applying the same estimate
on the completed interval proves

\[
\sup_{0\le t\le T}\|u(t)-\theta(t)\|_2
\le\frac{\delta_{\rm node}}{C_{\rm src}n}.
\tag{28}
\]

For polynomial nodal accuracy and \(T=O(\log(en))\), (15), (21)--(24)
give

\[
\log(1/\varepsilon_d)=O(\log(en)),\qquad
K=O(\log(en)),\qquad
N_{\rm step}=O((\log(en))^{3/2}).
\tag{29}
\]

The full dependence on depth, sample count, gap, labels, strip width and
activation bounds remains in the displayed constants. No additional smallness
condition on the labels was imposed. The \(Y=0\) case has stationary zero
readout and zero predictor and uses the original exact zero-label branch.

## 6. Computable Taylor coefficients and paired source values

On a panel write \(u(h)=\sum_{k=0}^K u_kh^k\). Compute successively

\[
u_{k+1}=\frac{[h^k]F(\sum_{i=0}^ku_ih^i)}{k+1},
\qquad 0\le k<K.
\tag{30}
\]

At stage \(k\), every input coefficient on the right side has already been
computed. The forward pass, backward pass and rank-one updates in (1)--(2)
give its coefficient by finite additions, scalar multiplications and truncated
series compositions. Induction identifies these coefficients with the Taylor
coefficients of the unique local solution proved above. The algorithm needs
neither exact anchors nor samples of the unknown exact path.

At a requested real time node, evaluate the current panel polynomial by
Horner's rule and perform the ordinary dense forward/backward pass at each
requested passive query. Form every paired image by multiplying that computed
base vector by its initialized matrix. For example, define

\[
\widetilde h^{(j)}=h^{(j)}(u(t),v),\qquad
\widetilde{W_0^{(j)}h^{(j-1)}}
=W_0^{(j)}\widetilde h^{(j-1)},
\tag{31}
\]

and do the same for the reverse image of \(\widetilde\delta\). Equations
(22), (28) give the required separate coordinate error
\(\delta_{\rm node}\) for every family. Pairing is an exact algebraic
identity. Applying identical scalar quadrature, cosine normalization and mode
restriction to both members preserves it. Passive-query Taylor jets are not
needed.

The numerical path need not itself be globally analytic across restart points.
Quadrature accuracy is proved for the exact source function, and its finite
sum is then perturbed by the nodal error (5). Therefore the piecewise
representation does not invalidate the analytic coefficient-quadrature proof.

## 7. Arithmetic, memory, and the exact activation qualification

Let \(\mathcal A_\phi(K)\) and \(\mathcal B_\phi(K)\) bound the arithmetic
and workspace of one scalar **online** degree-\(K\) series composition with
both \(\phi\) and \(\phi'\), including obtaining their required scalar
derivatives at the real constant term. Take maxima over the finitely many
activations and over the real anchor arguments encountered. This definition
counts a specified implementation; analyticity alone gives no bound on these
computational functions.

All matrix/vector and rank-one series operations can be accumulated online.
For each scalar product, the coefficient of degree \(k\) needs \(k+1\)
products of already available coefficients. Summing over \(k<K\) costs
\(O(K^2)\). Each dense vector-field coefficient pass has \(O(mP)\) such
entries; forward and reverse passes have the same order. Consequently all
training panels cost

\[
O\!\left(N_{\rm step}
  [mPK^2+Lmn\mathcal A_\phi(K)]\right),
\tag{32}
\]

with a sufficient current-panel memory bound

\[
O\!\left(PK+Lmn[K+\mathcal B_\phi(K)]\right).
\tag{33}
\]

The \(n\)-scaled mobility coordinates in (1) require only scalar rescaling
and do not change these counts. The computation trains all dense blocks; it
does not assume low rank of the trained increments or lazy feature dynamics.

Let \(N_t,N_x\) be the quadrature's numbers of time and spatial nodes. Supply
their values in increasing physical time. Evaluating panel polynomials at all
time nodes costs \(O(PKN_t)\). Ordinary query forward/backward passes and
the initialized-matrix image actions cost \(O(PN_tN_x)\), plus
\(O(LnN_tN_x)\) scalar activation and first-derivative calls. Thus the
value-oracle interface in the quadrature route has the explicit bound

\[
\begin{split}
\mathcal T_{\rm val}=O\!\big(&N_{\rm step}mPK^2+PKN_t+PN_tN_x\\
&+N_{\rm step}Lmn\mathcal A_\phi(K)\big),
\end{split}
\tag{34}
\]

plus the separately counted query scalar calls. Additional streamed memory is
bounded by (33) and \(O(Ln)\) query buffers. If a consumer insists on spatial
nodes outside time nodes, retaining all panel coefficients costs
\(O(PKN_{\rm step})\), or retaining all requested dense states costs
\(O(PN_t)\); both are still near quadratic at fixed parameters. Alternatively
the coefficient accumulator may consume time-major values directly.

For the original \(T=T_0,\eta=1/n\) specialization, and more generally the
quadrature route's polynomial-accuracy regime,

\[
N_t=O((\log(en))^{5/2}),\qquad
N_tN_x=O_d((\log(en))^{3d/2+1}),\qquad P=O(Ln^2+nd).
\]

Inserting these and (29) in (34) gives \(n^{2+o(1)}\) non-activation
arithmetic and near-quadratic peak setup memory. The quadrature, source
orthogonalization, selection and assembly terms already displayed in the
quadrature route also remain \(n^{2+o(1)}\), since their ranks and degrees are
polylogarithmic at fixed \(d\). None of these width-asymptotic statements
claims modest constants when \(d,L,m,1/\gamma\), or activation bounds vary.
The final retained Harmonic model is unchanged; panel coefficients and dense
setup arrays are discarded.

If \(\mathcal A_\phi(K),\mathcal B_\phi(K)\) are polynomial in \(K\),
and scalar query evaluations have bounded or polynomial-logarithmic cost at
the requested accuracy, the **total** exact-arithmetic setup is
\(n^{2+o(1)}\). Formula (34) remains the valid general interface without
that backend assumption. An arbitrary holomorphic function can have no
specified computational representation, so an unconditional algorithmic cost
claim for its derivative oracle cannot be inferred from the mathematical
activation hypotheses. Constructing activation approximants from a specified
scalar value oracle could remove the high-order derivative requirement, but
that additional backend construction is not assumed proved in this frozen
candidate.

The present result certifies exact-real arithmetic and source-coordinate
accuracy. It does not assert floating-point stability of high-order jets,
well-conditioned coordinate selection, or bit complexity. It also does not
by itself prove a wall-clock advantage over every dense training solver:
such a comparison needs that solver's numerical accuracy and step convention.
It proves that the permitted full nonlinear reference reconstruction can be
done within the stated near-quadratic arithmetic envelope rather than costing
a width-polynomial number of first-order training steps.

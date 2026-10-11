# Generic sphere inputs admit bad basins after choosing mixed labels

2026-10-10. Candidate theorem from the scoped negative-label route;
internally derived, awaiting independent checking, not promoted.
Scientific inputs were the supervisor's model and the complete
TANH_NECESSARY_GEOMETRY.md and TANH_REPLICATION_CLASS.md in this study.
After the independent moment derivation, the supervisor supplied the
all-amplitude capture mechanism; TANH_LARGE_RESIDUAL_CAPTURE.md was then
read completely and checked. TANH_BAD_BASIN.md was not read or used.
No experiments or external scientific sources were used. Required proof,
research, and canonical-notation instructions were applied.

Sections 1--6 prove small-label capture for generic fixed sphere inputs
when \(m\ge d^2+3d+3\). Section 7 adds one moment and proves capture at
every positive amplitude when \(m\ge d^2+3d+4\). Both conclusions give
open zero-readout basins with full-rank initial features and finite
positive-loss limits. Neither gives a failure-probability lower bound
uniform in width or covers every input configuration.

## 1. Model and small-label theorem

Let \(d\ge2\), let \(X=[x_1,\ldots,x_m]\in\mathbb R^{d\times m}\)
have unit columns, and let \(n\ge m\). Define
\[
U=\tanh(AX),\qquad H=\tanh(WU),\qquad
f=H^\top w/n,\qquad r=f-y,\qquad \mathcal L=\|r\|^2/m,
\]
where \(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\),
and \(w\in\mathbb R^n\). Physical gradient flow is
\[
\dot A=-n\nabla_A\mathcal L,\qquad
\dot W=-\nabla_W\mathcal L,\qquad
\dot w=-n\nabla_w\mathcal L,\qquad w(0)=0.                 \tag{1}
\]

**Candidate theorem.** Put \(N(d)=d^2+3d+3\). For \(m\ge N(d)\),
there is an open dense subset of \((S^{d-1})^m\), consisting of distinct
nonantipodal columns, with this property. Each configuration in that set
admits fixed mixed-sign labels \(y\), with \(0<\|y\|_\infty\le1\), and
a number \(\ell_*>0\), such that for every \(n\ge m\) there is a
nonempty open set of hidden starts on the exact slice \(w(0)=0\) satisfying
\[
\operatorname{rank}U(0)=\operatorname{rank}H(0)=m,\qquad
\lim_{t\to\infty}\mathcal L(t)=\ell_* .                  \tag{2}
\]
These trajectories converge to finite critical points. Labels and limiting
loss are independent of width. The global minimum loss is zero. The
specified Gaussian hidden initialization therefore assigns positive
probability to this behavior at each fixed width, without a width-uniform
lower bound. The sufficient label scale in this theorem can be small
and depends on the fixed dataset; Section 7 removes that restriction
with one additional sample and moment.

The proof prescribes a strict reduced minimum using linear residual
moments, establishes zero-readout capture, and lifts the attracting
trajectory to an open basin in the full dense network.

## 2. Independence of the moment functions

Fix \(a>0\), \(q>0\), and \(p=a e_1\), where \(e_1\) is the first
coordinate vector. For \(x\in S^{d-1}\), put
\[
\begin{aligned}
t&=p^\top x,&u&=\tanh t,&\chi&=1-u^2,&\tau&=-2u\chi,\\
h&=\tanh(qu),&\psi&=1-h^2,&\sigma&=-2h\psi,\\
T&=\psi\tau,&C&=q^2\sigma\chi^2+q\psi\tau,&
D&=q\sigma u\chi+\psi\chi .
\end{aligned}                                                   \tag{3}
\]
Here \(T,C,D\) are scalar functions, not parameter blocks. Consider
\[
h,\quad \psi u,\quad \psi\chi x,\quad
\sigma u^2,\quad Txx^\top,\quad Cxx^\top,\quad Dx,          \tag{4}
\]
using one scalar coordinate per vector entry and per upper-triangular
symmetric-matrix entry. Their number is
\(2+d+1+d(d+1)+d=N(d)\).

**Lemma 1.** The functions (4) are linearly independent on the sphere.

First, if \(F_0,\ldots,F_K\) are analytic near zero and
\[
\sum_{k=0}^K t^kF_k(e^{-2t})=0
\quad\hbox{for all sufficiently large }t,                 \tag{5}
\]
then every \(F_k\) vanishes near zero. Otherwise choose the smallest
Taylor order \(j\) occurring in any nonzero \(F_k\). Division by
\(e^{-2jt}\) gives a nonzero polynomial equal to
\(O(t^K e^{-2t})\), impossible as \(t\to\infty\).

All scalar functions in (3) are analytic for real \(t\), and analytic
in \(z=e^{-2t}\) near zero, since \(u=(1-z)/(1+z)\) and
\(\tanh(qu)\) is analytic near \(u=1\). An identity on an open
\(t\)-interval extends to all real \(t\) by the real-analytic identity
principle. Equation (5) therefore separates its distinct powers of \(t\).

The following three groups are independent:
\[
\{h,\psi u,\sigma u^2,T,C\},\qquad
\{\psi\chi,D\},\qquad \{T,C\}.                             \tag{6}
\]
For the first group, divide a relation with coefficients
\(b_0,\ldots,b_4\) by \(\psi>0\) and multiply by \(\cosh(qu)\):
\[
b_0\sinh(qu)\cosh^2(qu)+P(u)\cosh(qu)+Q(u)\sinh(qu)=0,      \tag{7}
\]
where
\[
P(u)=b_1u-2(b_3+qb_4)u(1-u^2),\qquad
Q(u)=-2b_2u^2-2q^2b_4(1-u^2)^2.
\]
This identity extends from \((-1,1)\) to all real \(u\). Using
\(\sinh z\cosh^2z=(\sinh(3z)+\sinh z)/4\) and sending \(u\to+\infty\)
gives \(b_0=0\): a polynomial times \(e^{qu}\) cannot cancel a nonzero
\(e^{3qu}\) term. The remaining identity is
\((P+Q)e^{qu}+(P-Q)e^{-qu}=0\). Exponential versus polynomial growth
gives \(P+Q=0\), then \(P-Q=0\). Thus \(P=Q=0\). Comparing the
fourth-, second-, third-, and first-degree coefficients gives
\(b_4=b_2=b_3=b_1=0\).

For the second group, the ratio
\(D/(\psi\chi)=1-2qu\tanh(qu)\) is nonconstant on \((-1,1)\).
For the last group, division by \(-2\psi\chi\) reduces a relation to
\[
(b+cq)u+cq^2\tanh(qu)(1-u^2)=0 .
\]
The limit \(u\to1\) gives \(b+cq=0\), and any \(u\in(0,1)\) then
gives \(c=b=0\). This proves (6). Together with (5), it proves
independence of the nine functions
\[
h,\psi u,\sigma u^2,T,C,\quad
t\psi\chi,tD,\quad t^2T,t^2C,                             \tag{8}
\]
and the four functions
\[
\psi\chi,D,tT,tC.                                        \tag{9}
\]

For the spherical step write
\(x=(t/a,\rho z)\), where \(\rho=\sqrt{1-t^2/a^2}\),
\(z\in S^{d-2}\), and \(|t|<a\). A relation among (4) has the form
\[
\beta_0h+\beta_1\psi u+\psi\chi b^\top x+
\beta_2\sigma u^2+T x^\top Bx+C x^\top Ex+D c^\top x=0,    \tag{10}
\]
with fixed vectors \(b,c\) and symmetric matrices \(B,E\).
Separate its constant, linear, and trace-free quadratic dependence on
\(z\). Subtracting the relation at \(-z\) isolates the linear part;
a quadratic form constant on the sphere is a scalar multiple of the
identity, which separates the remaining parts.

The trace-free quadratic coefficient is
\(\rho^2(TB_0+CE_0)\). Independence of \(\{T,C\}\) gives
\(B_0=E_0=0\). For \(d=2\), transverse blocks have dimension one and
their trace-free parts are already zero. The linear coefficient is
\[
\rho\left[\psi\chi b_\perp+D c_\perp+
\frac{2t}{a}(T B_{1\perp}+C E_{1\perp})\right].
\]
Equation (9) annuls its four vector coefficients. The constant part now
reduces to (8), because transverse scalar blocks multiply
\(1-t^2/a^2\), and first diagonal entries multiply \(t^2/a^2\).
Independence (8) annuls every remaining coefficient. This proves Lemma 1.

Let \(M(X)\in\mathbb R^{N(d)\times m}\) evaluate (4) on the inputs.
Independence gives \(N(d)\) evaluation points with an invertible square
evaluation matrix: otherwise all evaluation vectors would span a proper
subspace, producing a relation among the functions. Thus the determinant
from the first \(N(d)\) columns is a nonzero analytic function on
\((S^{d-1})^m\). This analytic manifold is connected for \(d\ge2\).
The identity principle on overlapping coordinate neighborhoods along
paths shows that a nonzero analytic function has zero set with empty
interior. Hence the nonzero determinant set is open dense. Intersect it
with the open dense set of distinct nonantipodal columns, and call the
result \(\mathcal G\). For \(X\in\mathcal G\), the map
\(M(X):\mathbb R^m\to\mathbb R^{N(d)}\) is onto.

## 3. Strict minimum from prescribed moments

For fixed \(X\in\mathcal G\), surjectivity supplies \(r^0\in\mathbb R^m\)
such that
\[
\begin{gathered}
\sum_a r_a^0h_a=0,\qquad
\sum_a r_a^0\psi_a u_a=0,\qquad
\sum_a r_a^0\psi_a\chi_a x_a=0,\\
\sum_a r_a^0\sigma_a u_a^2=1,\qquad
\sum_a r_a^0T_a x_ax_a^\top=I_d,\qquad
\sum_a r_a^0C_a x_ax_a^\top=I_d,\qquad
\sum_a r_a^0D_a x_a=0 .
\end{gathered}                                                   \tag{11}
\]
Fix \(s,\gamma>0\), and set
\[
\bar y=sh-\gamma r^0 .                                   \tag{12}
\]
Define the reduced loss
\[
J(p',q',c)=\frac1m\sum_a
[c\tanh(q'\tanh(p'^\top x_a))-\bar y_a]^2.                 \tag{13}
\]
At \((p,q,s)\), the residual is \(\gamma r^0\). The first three
moments in (11) give stationarity. For a direction \((v,b,c')\), the
first prediction derivative is
\(\delta f_a=h_a c'+s\psi_a(u_ab+q\chi_a x_a^\top v)\).
The second derivative, contracted with the residual, has no
readout/hidden term by the zero moments in (11). Its remaining moments
give exactly
\[
D^2J[(v,b,c'),(v,b,c')]
=\frac2m\left[\sum_a(\delta f_a)^2+
s\gamma(\|v\|^2+b^2)\right].                              \tag{14}
\]
This is positive definite: if \(v=b=0\), its remaining term is
\(2(c')^2\|h\|^2/m\), and \(h\ne0\) by the fourth moment in (11).

At width \(n\), take the profile
\[
A_{j,:}=p^\top,\qquad W_{ij}=q/n,\qquad w_i=s.             \tag{15}
\]
For a variation let \(a_j=\delta A_{j,:}^\top\),
\(b_i=\sum_j\delta W_{ij}\), \(c_i=\delta w_i\), with bars denoting
neuron averages. The exact rank-one identity from equations (7)--(13)
of TANH_REPLICATION_CLASS.md gives
\[
\begin{aligned}
D^2\mathcal L[\delta\theta,\delta\theta]
={}&D^2J[(\bar a,\bar b,\bar c),(\bar a,\bar b,\bar c)]\\
&+\frac{2s\gamma}{mn}\left[
\sum_i(b_i-\bar b)^2+q\sum_j\|a_j-\bar a\|^2\right].
\end{aligned}                                                   \tag{16}
\]
Its hypotheses are precisely (11): the top splitting moment is
\(\gamma\), the lower splitting matrix is \(\gamma I_d\), and mixed
splitting moments vanish. Direct differentiation also yields (16):
the mixed \(\delta W\,\delta A\) terms contract with the third zero
moment in (11).

The Hessian is positive definite transverse to the affine critical set
\[
\mathcal M_n=\{A_{j,:}=p^\top\ \forall j,\quad
W\mathbf1=q\mathbf1,\quad \mathbf1^\top w/n=s\}.           \tag{17}
\]
Every point on this set has prediction \(sh\) and vanishing gradients
by the first three moments in (11). Its tangent space is exactly the
kernel of (16).

These facts give an open attracting neighborhood at fixed width.
In fixed normal/tangent coordinates \((\xi,\eta)\), the loss excess
\(E=\mathcal L-\mathcal L_*\) is comparable to \(\|\xi\|^2\), and
the gradient norm is bounded below by a positive multiple of
\(\|\xi\|\). With the positive constant mobility metric, the speed
is therefore at least \(c\sqrt E\) and \(\dot E\) is minus its square.
Integration bounds remaining path length by \(2\sqrt{E(t)}/c\).
An inner starting neighborhood makes this less than the distance to the
outer boundary, preventing exit. The path is Cauchy and its limit lies
on (17). This is also the local trapping proof in Section 5 of the
replication note. Neighborhood sizes may depend on width.

Choose \(\gamma\) to make \(\bar y\) mixed-sign. If \(h\) has both
signs, sufficiently small \(\gamma>0\) works. Otherwise its nonzero
entries have one sign. Then \((r^0)^\top h=0\) and the fourth moment
in (11) force \(r^0\) to have both signs among indices with \(h_a\ne0\).
Sufficiently large \(\gamma\) makes (12) mixed-sign. In either case
all strict inequalities above remain valid.

Scaling labels and readout together by any \(\varepsilon>0\) preserves
stationarity and strict transverse stability; the residual becomes
\(\varepsilon\gamma r^0\), and the constant loss is
\[
\ell_*=\varepsilon^2\gamma^2\|r^0\|^2/m>0.                \tag{18}
\]
This is an all-amplitude existence result. The next section proves
capture for small \(\varepsilon\); Section 7 obtains all-amplitude
capture for a separately chosen label direction.

## 4. Small-label capture and the full zero-readout basin

For labels \(\varepsilon\bar y\), write the physical common readout
as \(\varepsilon c\). The exact reduced physical flow is
\[
\dot p'=-\varepsilon^2\nabla_{p'}J,\qquad
\dot q'=-\varepsilon^2\partial_{q'}J,\qquad
\dot c=-\partial_cJ,                                      \tag{19}
\]
starting from \((p,q,0)\). At \(\varepsilon=0\), hidden coordinates
freeze and readout stationarity gives
\[
c(t)=s(1-e^{-\kappa t}),\qquad
\kappa=2\|h\|^2/m>0.                                     \tag{20}
\]
Choose a closed ball around the strict minimum \((p,q,s)\) on which
\(D^2J\succeq\mu I\). Its boundary has loss at least \(J_*+b\),
for some \(b>0\), by the supporting quadratic inequality. At a finite
time \(T\), the path (20) is inside the ball with loss below \(J_*+b/2\).
Smooth finite-time dependence on \(\varepsilon^2\), from a local
Lipschitz bound and Gronwall's inequality on a compact tube, puts the
positive-\(\varepsilon\) path inside with loss below \(J_*+b\), for
all sufficiently small \(\varepsilon>0\).

Loss decreases, so boundary exit is impossible. Strong convexity gives
\(\|\nabla J\|^2\ge2\mu(J-J_*)\), and therefore
\[
\frac{d}{dt}(J-J_*)\le
-2\mu\min\{\varepsilon^2,1\}(J-J_*).                      \tag{21}
\]
The quadratic lower bound yields convergence to \((p,q,s)\).
The threshold \(\varepsilon_0>0\) depends only on the reduced problem.
Fix \(0<\varepsilon<\min\{\varepsilon_0,1/\|\bar y\|_\infty\}\).
The labels are mixed-sign, bounded by one, and fixed independently of width.

The symmetric family (15) is invariant under (1), by permutation
symmetry and uniqueness. Its restricted inverse-mobility metric is
\[
n^{-1}\|\delta A\|_F^2+\|\delta W\|_F^2+
n^{-1}\|\delta w\|^2
=\|\delta p\|^2+\delta q^2+\delta s_{\rm phys}^2 .
\]
Thus its exact physical flow is (19) at every width. Its zero-readout
path enters the full attracting neighborhood of the scaled (17) at
some finite time. The preimage of that neighborhood under the finite-time
flow, restricted to \(w=0\), is a nonempty open hidden-parameter set.
Every such start converges to the same constant-loss manifold.

## 5. Full-rank starts, interpolation, and Gaussian probability

For distinct nonantipodal nonzero columns, the ridge vectors
\((\tanh(v^\top x_a))_{a=1}^m\) span \(\mathbb R^m\).
To prove this, choose a direction with nonzero projections of distinct
absolute values by avoiding finitely many proper hyperplanes. A putative
annihilating relation restricts to a relation among
\(\tanh(tb_a)\), for distinct \(0<b_1<\cdots<b_m\), after absorbing
signs into the coefficients. The limit \(t\to\infty\) gives zero sum
of the coefficients. Subtract that constant relation and use
\(\tanh(tb)-1=-2e^{-2bt}(1+o(1))\); dividing by \(e^{-2b_1t}\)
annuls the first coefficient. Iteration annuls all of them.

Choose \(m\) first-layer rows making \(U\) have column rank \(m\).
A left inverse of \(U\) allows choosing \(W\) so that the first \(m\)
rows of \(WU\) are \(\delta I_m\), for \(\delta\ne0\), and remaining
rows are zero. Then \(H\) also has column rank \(m\).
Consequently
\[
P(A,W)=\det(U^\top U)\det(H^\top H)
\]
is a nonzero real-analytic function on connected hidden-parameter space.
Its nonzero set is open dense by the identity principle. Intersecting
it with the open zero-readout basin gives a nonempty open basin with
both initial features full rank. Full-rank \(H\) also permits solving
\(H^\top w/n=y\), so the global minimum is zero.

The independent law \(A_{jk}\sim N(0,1)\), \(W_{ij}\sim N(0,1/n)\)
has strictly positive density everywhere at each fixed width. It
assigns positive probability to this open basin, but these probabilities
may vanish as width increases.

## 6. Scope before the stronger amplitude result

The small-label theorem assumes \(m\ge d^2+3d+3>d\), so it does not
contradict the full-column-rank-input classification in
TANH_NECESSARY_GEOMETRY.md. The constructed failure is convergence to
finite attracting critical manifolds, not parameter escape. The limiting
feature matrices have rank one, despite full-rank initial features.

Labels depend on the fixed inputs, not width or a realized Gaussian draw.
The sufficient small capture scale can be very small for an ill-conditioned
dataset. Strict minima exist at every multiplier of those labels, but
Sections 1--5 prove capture only at small multipliers. Section 7 instead
chooses a large residual coefficient and an extra zero-sum moment,
yielding a direction with capture at every amplitude.

Intermediate sample counts and exceptional dependent geometries remain
unresolved. For full-column-rank inputs, absence of bad finite local
minima is still not an all-time fitting theorem; boundedness, escape,
and saddle avoidance on the exact zero-readout slice are separate questions.

## 7. One additional moment gives capture at every amplitude

**Stronger candidate theorem.** If \(d\ge2\) and
\(m\ge d^2+3d+4\), there is an open dense class of distinct nonantipodal
sphere-input configurations with the following property. For each fixed
configuration there is a fixed mixed-sign label vector \(y^\circ\), with
\(\|y^\circ\|_\infty=1\), such that, for every amplitude \(s>0\) and
every width \(n\ge m\), labels \(y=s y^\circ\) admit a nonempty open
set of hidden initializations on the exact slice \(w(0)=0\) whose initial
feature matrices both have rank \(m\), and whose trajectories converge
to a finite positive-loss critical manifold. The limiting loss is
\(s^2\ell^\circ\) for a fixed \(\ell^\circ>0\), independent of width.
The open set may depend on \(s,n\). Its Gaussian probability is positive
at every fixed \(s,n\), without a width-uniform probability bound.
Moreover, for any prescribed \(0<\eta<1\), the direction can be chosen
so that every trajectory in each of these basins satisfies
\(\mathcal L(\infty)/\mathcal L(0)>1-\eta\), simultaneously at every
amplitude and width.

First append the constant function \(1\) to the functions (4). Every
function in (4) is odd under \(x\mapsto-x\). A relation involving the
constant, evaluated at \(x\) and \(-x\) and added, therefore makes its
constant coefficient zero; Lemma 1 annuls the remaining coefficients.
The enlarged \(N(d)+1\) functions are independent. The same analytic
determinant argument consequently gives an open dense set of datasets
on which the equations (11) can be solved together with

\[
\sum_a r_a^0=0.
\tag{23}
\]

The moment \(\sum_a r_a^0\sigma_a u_a^2=1\) makes \(r^0\ne0\), so
(23) implies that \(r^0\) has both signs.

Write \(\theta=(p',q')\in\mathbb R^{d+1}\),
\(\theta_*=(p,q)\), and now regard

\[
h_a(\theta)=\tanh(q'\tanh(p'^\top x_a)),\qquad
h_*=h(\theta_*),\qquad F(\theta)=(r^0)^\top h(\theta)
\tag{24}
\]

as functions of the hidden reduced parameters. The prescribed moments
give exactly

\[
F(\theta_*)=0,\qquad \nabla F(\theta_*)=0,
\qquad D^2F(\theta_*)=I_{d+1},\qquad h_*\ne0.
\tag{25}
\]

Indeed the \(p'p'\), \(p'q'\), and \(q'q'\) blocks of \(D^2F\)
are respectively the \(C\)-matrix moment, the \(D\)-vector moment,
and the \(\sigma u^2\) moment in (11).

We prove a capture lemma directly from (25). For a number \(M>0\) to
be chosen, use labels

\[
y=s(h_*-M r^0),\qquad s>0,
\tag{26}
\]

and physical reduced readout \(s b\). Define

\[
V(\theta,b)=\|b h(\theta)-h_*\|^2+2MbF(\theta).
\tag{27}
\]

Because \((r^0)^\top h_*=0\), the actual reduced loss is
\(s^2[V+M^2\|r^0\|^2]/m\). Its exact physical flow, starting at
\((\theta_*,0)\), is

\[
\begin{aligned}
\dot\theta
&=-\frac{s^2}{m}\nabla_\theta V
 =-\frac{2s^2b}{m}
 \left[Dh(\theta)^\top(bh(\theta)-h_*)+M\nabla F(\theta)\right],\\
\dot b
&=-\frac1m\partial_b V
 =-\frac2m\left[b\|h(\theta)\|^2-h(\theta)^\top h_*+MF(\theta)\right].
\end{aligned}
\tag{28}
\]

Here \(Dh\) is the \(m\)-by-\((d+1)\) derivative matrix. The factors
in (28) retain the original physical time and all dependence on \(s\).

Choose a fixed ball around \(\theta_*\) on which

\[
cI\preceq D^2F\preceq CI,\qquad
\|h\|^2\ge A>0,
\tag{29}
\]

for constants \(c,C,A>0\). Smoothness gives a bound

\[
\|Dh(\theta)^\top(bh(\theta)-h_*)\|\le G
\quad\text{on that ball for }0\le b\le2.
\]

Choose \(K>G/c\), and then choose \(M\) sufficiently large that
the cylinder

\[
\mathcal C_M=\{\|\theta-\theta_*\|\le K/M,\quad0\le b\le2\}
\tag{30}
\]

lies in the chosen ball. These choices do not involve \(s\).
Writing \(e=\theta-\theta_*\), the bracket in the first equation of
(28) has radial inner product at least

\[
-G\|e\|+Mc\|e\|^2.
\]

It is strictly positive when \(\|e\|=K/M\), so the hidden velocity
points inward there whenever \(b>0\). At \(b=0\) that velocity is zero.
Taylor's integral formula and (25), (29) give
\(0\le F(\theta)\le C\|e\|^2/2\). Uniformly on (30), therefore,

\[
MF=O(M^{-1}),\qquad
\|h\|^2=\|h_*\|^2+O(M^{-1}),\qquad
h^\top h_*=\|h_*\|^2+O(M^{-1}).
\tag{31}
\]

For sufficiently large \(M\), the \(b\) velocity in (28) is positive
at \(b=0\), negative at \(b=2\), and bounded below by a fixed positive
constant whenever \(0\le b\le1/2\). A first-exit argument now keeps the
trajectory in (30): it leaves \(b=0\) immediately, and each potential
subsequent boundary exit has strict inward velocity. It reaches
\(b=1/2\) in finite time and thereafter stays in the smaller cylinder

\[
\mathcal C_M^+=\{\|\theta-\theta_*\|\le K/M,\quad1/2\le b\le2\}.
\tag{32}
\]

We next check full strong convexity of \(V\) on (32), rather than
assuming that separate convexity suffices. Its second derivatives are

\[
\begin{aligned}
D^2_{\theta\theta}V
 &=2b^2Dh^\top Dh
   +2b\sum_a(bh_a-h_{*,a})D^2h_a+2MbD^2F,\\
D^2_{\theta b}V
 &=2Dh^\top(2bh-h_*)+2M\nabla F,\\
\partial_b^2V&=2\|h\|^2.
\end{aligned}
\tag{33}
\]

The first two terms in the first line are uniformly bounded. Thus that
block is bounded below by \((Mc-R)I\) for a constant \(R\).
The middle block is uniformly bounded, say by \(B\), because
\(M\|\nabla F\|\le CK\). The last block is at least \(2A\).
Choosing \(M\) still larger, so that \(Mc-R>2B^2/A\), makes the full
Hessian positive definite by

\[
2B\|v\||z|
\le\tfrac12(Mc-R)\|v\|^2
       +\frac{2B^2}{Mc-R}|z|^2.
\]

Hence \(D^2V\succeq\mu I\) on (32), for some \(\mu>0\).
The point \((\theta_*,1)\) is stationary and has \(V=0\).
The cylinder is convex, so the supporting quadratic inequalities give

\[
V\ge\frac\mu2\| (\theta,b)-(\theta_*,1)\|^2,
\qquad \|\nabla V\|^2\ge2\mu V.
\]

Using (28), after the trajectory enters (32),

\[
\dot V
\le-\frac{\min\{s^2,1\}}m\|\nabla V\|^2
\le-\frac{2\mu\min\{s^2,1\}}m V.
\tag{34}
\]

Thus \((\theta,b)\to(\theta_*,1)\) for every \(s>0\), with the same
choice of \(M\). This proves all-amplitude zero-readout capture. Large
\(s\) can change the speed, but none of the invariant-region or convexity
conditions depends on \(s\).

Since \(r^0\) has both signs, increase \(M\), if necessary, so that
\(h_*-M r^0\) has both signs. This preserves all preceding sufficiently
large-\(M\) conclusions. At the final profile the residual is \(sM r^0\).
The same strict Hessian and splitting calculations as in Section 3 apply
with \(\gamma=sM\), and the readout is \(s>0\), so the limiting manifold
has a full open attracting neighborhood at every width. Exact replication,
pullback to \(w=0\), full-rank density, and positive fixed-width Gaussian
mass then follow exactly as in Sections 4--5.

Finally let \(Q=\|h_*-M r^0\|_\infty>0\) and define

\[
y^\circ=(h_*-M r^0)/Q,
\qquad
\ell^\circ=\frac{M^2\|r^0\|^2}{mQ^2}>0.
\]

Apply the all-amplitude result with its physical readout amplitude equal
to \(s/Q\). Labels are then exactly \(s y^\circ\), and the loss limit
is \(s^2\ell^\circ\), proving the stronger theorem. This resolves the
amplitude restriction for this generic class with the additional sample
and moment; it does not upgrade the Gaussian probability statement.

The quantitative retained-loss claim follows from \(h_*^\top r^0=0\):
\[
\frac{\mathcal L(\infty)}{\mathcal L(0)}
=\frac{M^2\|r^0\|^2}{\|h_*\|^2+M^2\|r^0\|^2}.
\tag{35}
\]
This identity holds for every trajectory in the constructed basin.
Every start has \(w(0)=0\) and hence \(f(0)=0\), so all have the same
initial loss; every endpoint lies on the same constant-loss manifold.
Increase \(M\) once more to make (35) exceed \(1-\eta\). All capture
conditions hold for all sufficiently large \(M\), so this changes none
of their quantifiers. The final direction may depend on \(\eta\), but
not on amplitude, width, or a realized Gaussian draw.

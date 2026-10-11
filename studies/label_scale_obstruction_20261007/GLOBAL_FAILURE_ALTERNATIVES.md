# Exact failure alternatives and a positive-loss escape example

This is a scoped theoretical contribution to
`label_scale_obstruction_20261007`, prepared from the supervisor's prompt alone.
No other study, book material, external scientific source, or experiment was
used. The mathematical and process skills required by the repository were read.
The statements below have complete direct arguments; they are author-checked
and await the supervisor's check. They do not classify all bad local minima or
prove almost-sure fitting.

## Model and exact flow

Let \(m,n,d\geq1\), with \(n\geq m\). The fixed input matrix

\[
X=[x_1,\ldots,x_m]\in\mathbb R^{d\times m}
\]

has unit columns, and \(y\in\mathbb R^m\) is the fixed target vector. The
global-existence, energy, kernel, and finite-accumulation results hold for
arbitrary finite \(X\). The initialization rank lemma uses distinct,
nonantipodal unit inputs; the escape example specifies its own admissible
four-sample input geometry.
The parameters and forward pass are

\[
\begin{aligned}
A&\in\mathbb R^{n\times d},&
W&\in\mathbb R^{n\times n},&
w&\in\mathbb R^n,\\
U&=\tanh(AX),&
H&=\tanh(WU),&
f&=\frac1nH^\top w,\\
r&=f-y,&
\mathcal L&=\frac1m\|r\|^2.
\end{aligned}
\]

The nonlinearities act entrywise. We use physical training time, initial
readout \(w(0)=0\), and mobilities \((n,1,n)\) in the parameter order

\[
\dot A=-n\nabla_A\mathcal L,\qquad
\dot W=-\nabla_W\mathcal L,\qquad
\dot w=-n\nabla_w\mathcal L.
\]

Define the entrywise derivative matrices

\[
S=\mathbf1-U\odot U,\qquad D=\mathbf1-H\odot H.
\]

Every entry of \(S,D\) is strictly positive at finite parameters. The chain
rule gives

\[
\begin{aligned}
\dot w&=-\frac2mHr,\\
\dot W&=-\frac{2}{mn}\bigl[(wr^\top)\odot D\bigr]U^\top,\\
\dot A&=-\frac2m
\left\{W^\top\bigl[(wr^\top)\odot D\bigr]\odot S\right\}X^\top.
\end{aligned}
\tag{1}
\]

For example, a variation of \(W\) changes \(H\) by

\[
\delta H=D\odot(\delta W\,U),
\]

so

\[
\delta_W\mathcal L
=\frac{2}{mn}\left\langle
[(wr^\top)\odot D]U^\top,\delta W
\right\rangle_F.
\]

The \(A\) equation follows by additionally substituting

\[
\delta U=S\odot(\delta A\,X).
\]

## Global existence and finite energy

Write \(\theta=(A,W,w)\) and equip parameter increments with the fixed metric

\[
\|\delta\theta\|_{M^{-1}}^2
=\frac1n\|\delta A\|_F^2+
\|\delta W\|_F^2+
\frac1n\|\delta w\|^2.
\]

Here \(M\) is the diagonal mobility operator with blocks \(nI,I,nI\).
Along every local solution of (1),

\[
\frac{d\mathcal L}{dt}
=-n\|\nabla_A\mathcal L\|_F^2
-\|\nabla_W\mathcal L\|_F^2
-n\|\nabla_w\mathcal L\|^2
=-\|\dot\theta\|_{M^{-1}}^2.
\tag{2}
\]

Consequently, for \(0\leq s<t\) in the interval of existence,

\[
\begin{aligned}
\int_s^t\|\dot\theta(u)\|_{M^{-1}}^2\,du
&=\mathcal L(s)-\mathcal L(t),\\
\|\theta(t)-\theta(s)\|_{M^{-1}}
&\leq\sqrt{(t-s)[\mathcal L(s)-\mathcal L(t)]}
\leq\sqrt{(t-s)\mathcal L(0)}.
\end{aligned}
\tag{3}
\]

The second inequality is the integral triangle inequality followed by
Cauchy--Schwarz. If the maximal forward interval had finite endpoint \(T\),
(3) would make \(\theta(t)\) Cauchy as \(t\uparrow T\), with a finite limit.
The right side of (1) is smooth on the entire finite-dimensional parameter
space, so a local solution from that limit extends the trajectory past \(T\),
a contradiction. Thus the solution is unique and exists for all \(t\geq0\).

The loss has a limit \(\mathcal L_\infty\geq0\), and

\[
\int_0^\infty\|\dot\theta(t)\|_{M^{-1}}^2\,dt
=\mathcal L(0)-\mathcal L_\infty,
\qquad
\|\theta(t)-\theta(0)\|_{M^{-1}}
\leq\sqrt{t\mathcal L(0)}.
\tag{4}
\]

These estimates exclude finite-time parameter blow-up. They do not establish
bounded parameters, integrable speed, or parameter convergence as \(t\to\infty\).

## Exact residual kernel and a sufficient fitting condition

Let \(u_a,h_a\in\mathbb R^n\) be the \(a\)-th columns of \(U,H\), and define

\[
s_a=\mathbf1-u_a\odot u_a,\qquad
d_a=\mathbf1-h_a\odot h_a.
\]

Differentiating the scalar prediction \(f_a\) gives

\[
\begin{aligned}
\nabla_w f_a&=\frac1n h_a,\\
\nabla_W f_a&=\frac1n(w\odot d_a)u_a^\top,\\
\nabla_A f_a&=\frac1n
\bigl[W^\top(w\odot d_a)\odot s_a\bigr]x_a^\top.
\end{aligned}
\]

Define the symmetric matrix \(K(\theta)\in\mathbb R^{m\times m}\) by the
mobility-weighted Gram formula

\[
\begin{aligned}
K_{ab}
={}&\frac1n h_a^\top h_b\\
&+\frac1{n^2}
[(w\odot d_a)^\top(w\odot d_b)](u_a^\top u_b)\\
&+\frac1n
\left[W^\top(w\odot d_a)\odot s_a\right]^\top
\left[W^\top(w\odot d_b)\odot s_b\right]
(x_a^\top x_b).
\end{aligned}
\tag{5}
\]

Equivalently, if \(J\) is the Jacobian of \(\theta\mapsto f\), then

\[
K=JMJ^\top\succeq\frac1nH^\top H\succeq0.
\]

Since \(\dot\theta=-(2/m)MJ^\top r\),

\[
\dot r=-\frac2mKr,\qquad
\dot{\mathcal L}=-\frac4{m^2}r^\top Kr.
\tag{6}
\]

Suppose \(\mathcal L(0)>0\). The loss remains positive at every finite time:
on each compact time interval \(K(t)\) is bounded and

\[
\dot{\mathcal L}
\geq-\frac4m\|K(t)\|_{\mathrm{op}}\mathcal L.
\]

Multiplication by the integrating factor yields a strictly positive lower
bound. Dividing (6) by \(\mathcal L=\|r\|^2/m\) and integrating is therefore
legitimate:

\[
\mathcal L(t)=\mathcal L(0)
\exp\left[-\frac4m\int_0^t
\frac{r(s)^\top K(s)r(s)}{\|r(s)\|^2}\,ds\right].
\tag{7}
\]

Equation (7) is an exact identity, not an independent criterion computable from
initial data. It says that fitting is equivalent to divergence of its actual
residual Rayleigh-quotient integral.

A stronger but nonnecessary sufficient condition is

\[
\int_0^\infty\lambda_{\min}(K(t))\,dt=\infty.
\tag{8}
\]

In particular, writing \(\sigma_{\min}(H)\) for the smallest of its \(m\)
singular values,

\[
\int_0^\infty\sigma_{\min}(H(t))^2\,dt=\infty
\quad\Longrightarrow\quad\mathcal L(t)\longrightarrow0.
\tag{9}
\]

Indeed, \(r^\top Kr/\|r\|^2\geq\sigma_{\min}(H)^2/n\). A uniform lower
bound \(\sigma_{\min}(H(t))\geq c>0\) for all \(t\geq T\) gives the explicit
estimate

\[
\mathcal L(t)\leq\mathcal L(T)
\exp[-4c^2(t-T)/(mn)],\qquad t\geq T.
\]

Full column rank at \(t=0\) gives a positive lower bound only on some initial
time interval by continuity. It does not prove (9). Even pointwise positive
smallest eigenvalues would not alone make their integral diverge.

## Every finite accumulation point is stationary

This claim does not require the entire trajectory to be bounded. Suppose

\[
t_k\longrightarrow\infty,\qquad\theta(t_k)\longrightarrow\theta_*.
\]

Then \(\mathcal L(\theta_*)=\mathcal L_\infty\) by continuity. To prove
stationarity, suppose instead that

\[
q(\theta_*)>0,\qquad
q(\theta)=\|\dot\theta\|_{M^{-1}}^2
=\|M^{1/2}\nabla\mathcal L(\theta)\|^2.
\]

Choose a closed metric ball \(B_\rho(\theta_*)\) on which \(q\geq c>0\).
The continuous vector field has a finite speed bound \(C>0\) on that ball.
For all sufficiently large \(k\), \(\theta(t_k)\in B_{\rho/2}(\theta_*)\).
For at least

\[
\delta=\rho/(2C)
\]

units of subsequent time it stays in \(B_\rho(\theta_*)\): an earlier first
exit would require travelling metric distance at least \(\rho/2\), despite
speed at most \(C\). Equation (2) therefore implies

\[
\mathcal L(t_k)-\mathcal L(t_k+\delta)\geq c\delta.
\]

Both loss values converge to \(\mathcal L_\infty\), a contradiction. Hence

\[
\nabla\mathcal L(\theta_*)=0.
\tag{10}
\]

At any stationary point, (6) or the Gram representation gives

\[
J^\top r=0,\qquad Kr=0,\qquad Hr=0.
\tag{11}
\]

Consequently, a finite accumulation point with \(\operatorname{rank}H_*=m\)
forces \(r_*=0\), and thus \(\mathcal L_\infty=0\).

If the trajectory is bounded, it has at least one finite accumulation point
by finite-dimensional compactness. The argument establishes stationary
accumulation points, not convergence to a unique point. No analytic-gradient
convergence theorem is imported or needed here.

## A stronger first-layer criterion for zero-readout initialization

At a stationary point the \(j\)-th row of the \(W\) gradient is

\[
\nabla_{W_j}\mathcal L
=\frac{2w_j}{mn}
\left[U\operatorname{diag}(D_{j1},\ldots,D_{jm})r\right]^\top.
\tag{12}
\]

Suppose \(U\) has full column rank and \(r\ne0\). Every diagonal entry in
(12) is positive; hence

\[
\operatorname{diag}(D_{j1},\ldots,D_{jm})r\ne0,
\qquad
U\operatorname{diag}(D_{j1},\ldots,D_{jm})r\ne0.
\]

Equation (12) then forces \(w_j=0\) for every \(j\). Thus:

> Every finite, positive-loss stationary point with first-layer feature rank
> \(m\) has \(w=0\), \(f=0\), and loss \(\|y\|^2/m\).

Such a stationary point is moreover a strict saddle. To see this, let \(h_j\)
be the transpose of row \(j\) of \(H\), let

\[
D_j=\operatorname{diag}(D_{j1},\ldots,D_{jm}),\qquad q=UD_jy\ne0,
\]

and perturb only

\[
w=s e_j,\qquad W_j\mapsto W_j+tq^\top.
\]

Here \(e_j\in\mathbb R^n\) is the \(j\)-th coordinate vector, and \(A\) is
fixed. At the stationary point \(w=0\), stationarity in \(w\) means

\[
h_j^\top y=0.
\]

The degree-two part of the loss change in \((s,t)\) is

\[
\frac{s^2}{mn^2}\|h_j\|^2
-\frac{2st}{mn}\,q^\top UD_jy
=\frac{s^2}{mn^2}\|h_j\|^2
-\frac{2st}{mn}\|q\|^2.
\tag{13}
\]

There is no \(t^2\) term because with \(w=0\) the prediction remains zero for
every \(W\). The symmetric matrix of this quadratic form has negative
determinant, so the loss Hessian has both a negative and a positive direction.

Now return to the stipulated initialization \(w(0)=0\). At that instant

\[
\dot A(0)=0,\qquad\dot W(0)=0,\qquad
\dot w(0)=\frac2mH(0)y,
\]

and

\[
\dot{\mathcal L}(0)
=-\frac4{nm^2}\|H(0)y\|^2.
\tag{14}
\]

If \(H(0)y=0\), all velocities vanish and uniqueness makes the trajectory
stationary. If \(H(0)y\ne0\), (14) and continuity imply that for some \(t_1>0\),

\[
\mathcal L_\infty\leq\mathcal L(t_1)
<\mathcal L(0)=\frac1m\|y\|^2.
\tag{15}
\]

Combining (10), (12), and (15) proves the stronger criterion:

> If \(w(0)=0\), \(H(0)y\ne0\), and the trajectory has any finite accumulation
> point at which \(\operatorname{rank}U_*=m\), then
> \(\mathcal L(t)\to0\).

Equivalently, a positive-loss trajectory that leaves the zero-readout
initialization can have only finite accumulation points satisfying

\[
\nabla\mathcal L(\theta_*)=0,\qquad
w_*\ne0,\qquad
\operatorname{rank}U_*<m,\qquad
\operatorname{rank}H_*<m.
\tag{16}
\]

For example, boundedness of the trajectory together with

\[
\limsup_{t\to\infty}\sigma_{\min}(U(t))>0
\]

implies fitting, provided \(H(0)y\ne0\): choose times with smallest singular
value uniformly positive, take a convergent parameter subsequence, and apply
the criterion. This requires only recurrent first-layer nondegeneracy, not a
uniform lower bound for all times.

## What Gaussian initialization actually supplies

Assume the unit inputs are distinct and no pair is antipodal. The functions

\[
a\longmapsto\tanh(a^\top x_b),\qquad b=1,\ldots,m,
\]

are linearly independent on \(\mathbb R^d\). Here is a direct proof.

Choose \(v\in\mathbb R^d\) outside the finitely many hyperplanes

\[
v^\top x_b=0,\qquad v^\top(x_a-x_b)=0,\qquad
v^\top(x_a+x_b)=0\quad(a\ne b).
\]

Each hyperplane is proper under the assumptions. Thus the numbers

\[
c_b=v^\top x_b
\]

are nonzero with pairwise distinct absolute values. If

\[
\sum_{b=1}^m\alpha_b\tanh(tc_b)=0\quad\hbox{for all }t,
\]

put \(\beta_b=\alpha_b\operatorname{sign}(c_b)\) and \(q_b=|c_b|>0\),
and order the \(q_b\) increasingly. Taking \(t\to\infty\) yields

\[
\sum_b\beta_b=0.
\]

Because

\[
\tanh(tq_b)-1=-2e^{-2tq_b}+O(e^{-4tq_b}),
\]

subtracting the constant relation and multiplying by \(e^{2tq_1}\) gives

\[
0=-2\beta_1+o(1).
\]

Thus \(\beta_1=0\). Repeating with the remaining terms gives every

\[
\alpha_b=0.
\]

The evaluation vectors

\[
(\tanh(a^\top x_1),\ldots,\tanh(a^\top x_m))\in\mathbb R^m
\]

therefore span \(\mathbb R^m\): otherwise a nonzero vector orthogonal to their
span would contradict independence. Select \(m\) evaluations forming a basis
and use their arguments as the first \(m\) rows of \(A\). This constructs an

\[
U=\tanh(AX)
\]

whose first \(m\) rows form an invertible matrix.

That \(m\times m\) determinant is real analytic in the entries of \(A\) and is
not identically zero. A nonzero real-analytic function on \(\mathbb R^N\) has a
Lebesgue-null zero set. For completeness, prove this by induction on \(N\).
For \(N=1\), zeros are isolated. For \(N>1\), choose a real number \(t_0\) such
that \(g(z)=F(z,t_0)\) is not identically zero. Its zero set is null by the
induction hypothesis. For every other \(z\), the one-variable function

\[
t\longmapsto F(z,t)
\]

is not identically zero, since its value at \(t_0\) is nonzero, and has a null
zero set. Applying Fubini on bounded boxes and then taking their countable
union proves the assertion.

It follows that an \(A\) with an absolutely continuous law has

\[
\operatorname{rank}U=m
\]

almost surely. There is likewise a nonzero analytic \(m\times m\) minor of

\[
H=\tanh(W\tanh(AX))
\]

as a function of the joint entries of \(A,W\). To construct a witness, fix the
full-rank \(U\) above and let \(Z\in\mathbb R^{n\times m}\) have first \(m\)
rows equal to \(cI_m\), \(c\ne0\), and remaining rows zero. The choice

\[
W=Z(U^\top U)^{-1}U^\top
\]

satisfies \(WU=Z\). Then the first \(m\) rows of \(H\) are

\[
\tanh(c)I_m,
\]

which are invertible. The analytic-null-set argument proves that any jointly
absolutely continuous initialization of \((A,W)\), including a nondegenerate
Gaussian law, gives

\[
\operatorname{rank}U(0)=\operatorname{rank}H(0)=m
\]

almost surely. For fixed \(y\ne0\), this implies \(H(0)y\ne0\), so the loss
starts decreasing.

This proves initial nondegeneracy and departure from the zero-readout slice.
It does not prove preservation of feature rank at accumulation points,
boundedness of parameters, (8), or (9). Also, the full initialization law on

\[
(A,W,w)
\]

is supported on the lower-dimensional set \(w=0\). An avoidance assertion
proved for a density on the full parameter space cannot be applied to this
law without a separate argument about its intersection with the relevant
stable sets. A specific null counterexample below does not establish a
positive Gaussian failure probability.

## Stationary strict-saddle counterexample on the zero-readout slice

Fix \(y\ne0\), let \(A_0\) satisfy \(U_0y\ne0\), and initialize

\[
W_0=0,\qquad w_0=0.
\]

Then \(H_0=0\), and every right side of (1) vanishes. Thus the exact trajectory
is constant with

\[
\mathcal L(t)=\frac1m\|y\|^2>0.
\]

It is a strict saddle. Choose any unit vector \(v\in\mathbb R^n\), set

\[
B=v(U_0y)^\top\in\mathbb R^{n\times n},
\]

and perturb \(w=\varepsilon v\), \(W=\pm\varepsilon B\), \(A=A_0\). Taylor
expansion of \(\tanh\) at zero gives

\[
\begin{aligned}
H&=\pm\varepsilon BU_0+O(\varepsilon^3),\\
f&=\pm\frac{\varepsilon^2}{n}U_0^\top B^\top v
+O(\varepsilon^4),\\
\mathcal L
&=\frac1m\|y\|^2
\mp\frac{2\varepsilon^2}{mn}\|U_0y\|^2
+O(\varepsilon^4).
\end{aligned}
\]

Both signs of quadratic loss change occur. Hence the point is not a local
minimum and has a negative Hessian direction. Such an \(A_0\) is available for
every admissible input set by the full-rank construction above. A particularly
explicit instance is \(d=m\), \(X=I_m\), and \(A_0\) whose first \(m\) rows are

\[
aI_m,\qquad a\ne0,
\]

with remaining rows zero.

This refutes a deterministic assertion that every zero-readout configuration
outside bad stable minima fits. It does not refute a statement restricted to

\[
\operatorname{rank}H(0)=m
\]

or an almost-sure statement under a nondegenerate Gaussian hidden-weight
initialization. Its first-layer features can have full rank, but its
second-layer features are exactly zero.

## A higher-order stalled saddle

Take \(m=n=d=1\), \(x_1=y_1=1\), and scalar parameters \(A,W,w\). Then

\[
f=w\tanh(W\tanh A),\qquad\mathcal L=(f-1)^2.
\]

At \(A=W=w=0\), all velocities vanish and \(\mathcal L=1\). The prediction
has no Taylor terms below total degree three, with leading term \(wWA\), so
the loss Hessian at the origin is zero. Nevertheless, for every sufficiently
small \(\varepsilon>0\), choosing

\[
A=W=w=\varepsilon
\]

gives \(0<f<1\), hence \(\mathcal L<1\). Keeping \(A=W=\varepsilon\) and
choosing \(w=-\varepsilon\) gives \(f<0\), hence \(\mathcal L>1\).
Thus this stationary point is neither a local minimum nor a strict saddle in
the negative-Hessian-eigenvalue sense. The example shows why ruling out only
strict saddles would not yield an every-configuration fitting theorem.

## A moving, positive-loss trajectory escaping to infinity

The following construction was proposed by the supervisor and independently
checked in this scoped route. It gives an actual unbounded nonfitting
trajectory, with both hidden layers trained, for correlated admissible inputs.
It uses a special rank-one hidden initialization; it does not assert failure
with positive probability under Gaussian initialization.

Take \(d=2\), \(m=4\), and any \(n\geq4\). Choose

\[
\frac34<s_1<s_2<1,
\qquad
x_{k,\pm}=(s_k,\ \pm\sqrt{1-s_k^2})^\top,
\quad k=1,2.
\]

Assign labels \(\alpha\) to the two \(k=1\) samples and \(\beta\) to the two
\(k=2\) samples, where \(\alpha>\beta>0\).

All four inputs have unit norm, are distinct, and are nonantipodal because
their first coordinates are positive. They are also pairwise positively
correlated. Indeed, write \(s_k=\cos\vartheta_k\), with

\[
0<\vartheta_2<\vartheta_1<\arccos(3/4).
\]

Their polar angles are \(\pm\vartheta_1,\pm\vartheta_2\), so every angular
separation is less than \(2\arccos(3/4)<\pi/2\), and every pairwise inner
product is strictly greater than

\[
\cos(2\arccos(3/4))=\frac18.
\]

Initialize in the symmetric family

\[
A_i=p e_1^\top\quad(1\leq i\leq n),\qquad
W_{ij}=\frac qn\quad(1\leq i,j\leq n),\qquad
w_i=v\quad(1\leq i\leq n),
\tag{17}
\]

where \(e_1=(1,0)^\top\in\mathbb R^2\), \(p(0),q(0)>0\), and \(v(0)=0\).
The letter \(v\) denotes the scalar common readout coordinate here; the network
readout is still the vector \(w=v\mathbf1\in\mathbb R^n\).

For the two sample types define

\[
u_k=\tanh(ps_k),\qquad
h_k=\tanh(qu_k),\qquad
r_1=vh_1-\alpha,\qquad r_2=vh_2-\beta.
\]

The network predicts \(vh_k\) on both signs of sample type \(k\). Hence

\[
\mathcal L=\frac12(r_1^2+r_2^2).
\tag{18}
\]

The family (17) is invariant under the full flow. To verify this directly,
substitute it into (1). All readout velocities agree. All \(W_{ij}\) velocities
agree, and their common value is \(\dot q/n\). All \(A_i\) velocities agree;
their second input coordinate vanishes because the two signs of each sample
have equal forward states and residuals, while their second input coordinates
are opposite. Their common first coordinate is \(\dot p\). The resulting
scalar equations, including all width and sample-count factors, are

\[
\begin{aligned}
\dot v&=-\sum_{k=1}^2r_kh_k,\\
\dot q&=-v\sum_{k=1}^2r_ku_k(1-h_k^2),\\
\dot p&=-vq\sum_{k=1}^2
r_ks_k(1-u_k^2)(1-h_k^2).
\end{aligned}
\tag{19}
\]

In particular, (19) is exactly Euclidean gradient flow of (18) in

\[
(p,q,v)\in\mathbb R^3.
\]

The induced parameter metric confirms the normalization:

\[
\frac1n\|\delta A\|_F^2+
\|\delta W\|_F^2+
\frac1n\|\delta w\|^2
=\delta p^2+\delta q^2+\delta v^2.
\tag{20}
\]

Consequently,

\[
\dot{\mathcal L}=-(\dot p^2+\dot q^2+\dot v^2).
\]

All three scalar parameters are strictly positive for \(t>0\). First,

\[
\dot v(0)=\alpha h_1(0)+\beta h_2(0)>0,
\]

so they are positive on a sufficiently short interval after zero. On the
three faces of the nonnegative octant, the corresponding inward velocities
are

\[
\begin{aligned}
\dot v\big|_{v=0}
&=\alpha h_1+\beta h_2\geq0,\\
\dot q\big|_{q=0}
&=v(\alpha\tanh(ps_1)+\beta\tanh(ps_2))\geq0,\\
\dot p\big|_{p=0}
&=vq(\alpha s_1+\beta s_2)\geq0.
\end{aligned}
\]

For a direct strict-positivity argument, suppose there is a first finite
boundary time after a time when all coordinates are positive. On the compact
nonnegative box containing the preceding trajectory and its coordinate-face
projections, the smooth vector field is Lipschitz with some constant \(C\).
Each coordinate \(z=p,q,v\) therefore satisfies

\[
\dot z\geq-Cz
\]

before that boundary time: compare its velocity with the nonnegative velocity
at the point obtained by setting only that coordinate to zero. Gronwall's
inequality gives a strictly positive value at the proposed first boundary
time, a contradiction. Finite-time compactness is available from (3).

Since \(p,q,v>0\) and \(s_1<s_2\),

\[
0<vh_1<vh_2\qquad(t>0).
\]

The labels have the opposite strict order. Writing the two predictions as

\[
f_1=vh_1,\qquad f_2=vh_2,
\]

the exact identity

\[
\mathcal L
=\frac14\left[
(f_1+f_2-\alpha-\beta)^2+
(f_1-f_2-\alpha+\beta)^2\right]
\]

implies

\[
\mathcal L(t)\geq\frac{(\alpha-\beta)^2}{4}>0
\quad\text{for every }t\geq0.
\tag{21}
\]

For \(t>0\) the inequality is strict, since \(f_1-f_2<0\). In particular, the
limit satisfies the same positive lower bound.

There is no stationary point of (19) in the positive octant. At such a point,

\[
r_1h_1+r_2h_2=0
\]

from the readout equation. Solving for \(v\) then gives

\[
\begin{aligned}
v&=\frac{\alpha h_1+\beta h_2}{h_1^2+h_2^2},\\
(r_1,r_2)&=c(-h_2,h_1),\qquad
c=\frac{\alpha h_2-\beta h_1}{h_1^2+h_2^2}>0.
\end{aligned}
\]

Let \(h_{k,q}=\partial h_k/\partial q=u_k(1-h_k^2)\). Then

\[
\sum_{k=1}^2r_kh_{k,q}
=c h_1h_2
\left(\frac{h_{2,q}}{h_2}-\frac{h_{1,q}}{h_1}\right).
\]

For fixed \(q>0\),

\[
\frac{h_{k,q}}{h_k}
=\frac{2u_k}{\sinh(2qu_k)}
\]

is strictly decreasing as a function of \(u_k>0\). Indeed, its derivative
has the sign of

\[
\sinh z-z\cosh z<0,\qquad z=2qu_k>0,
\]

because \(z\cosh z-\sinh z\) vanishes at zero and has derivative

\[
z\sinh z>0.
\]

Since \(0<u_1<u_2\), it follows that

\[
\sum_{k=1}^2r_kh_{k,q}<0,\qquad
\dot q=-v\sum_{k=1}^2r_kh_{k,q}>0,
\]

contradicting stationarity.

There are also no finite boundary accumulation points. The trajectory has

\[
\mathcal L(0)=\frac{\alpha^2+\beta^2}{2},\qquad
\dot{\mathcal L}(0)
=-[\alpha h_1(0)+\beta h_2(0)]^2<0,
\]

so \(\mathcal L_\infty<\mathcal L(0)\). At any finite nonnegative boundary
point, at least one of \(p,q,v\) vanishes; then both predictions vanish, and
the loss equals \(\mathcal L(0)\), which excludes accumulation there.

The invariant parameter family is closed. Any finite accumulation point of
the full trajectory would therefore correspond to a finite nonnegative
limit of \((p,q,v)\). A positive limit would be stationary by (10), which was
just ruled out; a boundary limit was ruled out by its loss value. There is no
finite accumulation point. If the scalar norm did not tend to infinity,
there would be a sequence of times tending to infinity on which \((p,q,v)\)
was bounded; a convergent subsequence would produce a finite accumulation
point. Therefore

\[
p(t)^2+q(t)^2+v(t)^2\longrightarrow\infty,
\qquad
\mathcal L_\infty\geq\frac{(\alpha-\beta)^2}{4}>0.
\tag{22}
\]

Both hidden layers do move immediately after initialization. Their first
velocities vanish exactly at \(t=0\), as every zero-readout initialization
requires. With

\[
c_v=\alpha h_1(0)+\beta h_2(0)>0,
\]

their second derivatives are

\[
\begin{aligned}
\ddot q(0)
&=c_v\left[
\alpha u_1(0)(1-h_1(0)^2)+
\beta u_2(0)(1-h_2(0)^2)\right]>0,\\
\ddot p(0)
&=c_v q(0)\left[
\alpha s_1(1-u_1(0)^2)(1-h_1(0)^2)+
\beta s_2(1-u_2(0)^2)(1-h_2(0)^2)\right]>0.
\end{aligned}
\]

Thus (22) describes the actual trained
two-hidden-layer flow, not a frozen-feature or readout-only substitute.
Its initial \(U\) and \(H\) each have rank one, so it remains outside an
initial-full-rank assertion. The exact symmetry also defines a null set for
a nondegenerate Gaussian hidden-weight initialization.

## Exact alternative and remaining obligations

For every initial finite parameter vector the flow is global and the loss has
a limit. If \(w(0)=0\), \(y\ne0\), and \(H(0)y\ne0\), then either:

1. \(\mathcal L(t)\to0\); or
2. \(\mathcal L_\infty>0\), in which case every finite accumulation point obeys
   (16), and the parameter trajectory may also be unbounded.

For a bounded trajectory the second case necessarily has finite stationary
accumulation points. For an unbounded trajectory the proof neither forces

\[
\|\theta(t)\|\longrightarrow\infty
\]

nor excludes finite accumulation subsequences. These possibilities must not be
collapsed into an unsupported dichotomy between convergence to a finite local
minimum and uniform escape to infinity.

The stalled saddles and the moving escape construction disprove an unrestricted
claim that all configurations outside bad stable equilibria fit. To obtain such
a conclusion for a restricted initialization class, one still needs arguments
excluding convergence or accumulation at unstable and degenerate stationary
points from that class, and excluding positive-loss parameter escape within
that class. For a Gaussian statement, any avoidance argument must apply to the
actual zero-readout initialization slice. The calculations here establish
neither exclusion for Gaussian or initially full-rank hidden configurations.
No complete classification or almost-sure convergence claim is made.

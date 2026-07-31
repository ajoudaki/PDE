# Independent reconstruction and implementation audit of the proposed dense continuous-depth PDE

## Executive verdict

The object called \((\mathrm{PDE}\text{-}K,J,N)\) in
`dense_euclidean_continuous_depth_pde_conjecture.md` is a formally useful
**schema**, but it is not an emitted, numerically implementable PDE.  In
particular, the note does not give even one concrete value of \(J_*\), one
enumerated tag table, one historical-coefficient table, the finite Gaussian
kernel \(\Gamma_{K,J,N}\), or the resulting characteristic drift.  Thus the
first claimed model
\[
(\mathrm{PDE}\text{-}1,J_*,N)
\]
cannot be coded from the note without making new closure choices.  Such
choices would define a new PDE, not simulate the displayed one.

The exact finite-width \(q/r\) response system in the reproducibility bundle
is not a counterexample to this conclusion: it carries every
\(W_\ell\in\mathbb R^{n\times n}\).  It is a finite-matrix response
projection, not a width-independent law PDE.

There is, however, a substantially more explicit and promising alternative.
After the iid-depth homogenization, project each *row operator* onto a fixed
Hermite basis of the static neuron label
\(\theta=(B_i(0),a_i(0))\), and transport the conditional law of its finitely
many row coefficients.  This gives an autonomous, width-independent
McKean--Vlasov transport PDE with an exact forward/backward adjoint pair and
an exact positive-semidefinite tangent kernel.  It can be simulated by
characteristics without storing any matrix with two neuron indices.

That alternative is an honest PDE candidate, but not yet a theorem for the
canonical dense network.  Its central unresolved lemma is a trained
iid-depth homogenization statement: the zero-mean fresh *column* cavity
innovation in \(W_\ell^\top\beta_\ell\) must average away as
\(L^{-1/2}\), while its nonzero Onsager mean must converge to the adjoint
term retained by the PDE.  This is true at initialization and is the natural
conditional law-of-large-numbers prediction under depth propagation of
chaos; it is not proved in either supplied note.

The best immediate path to a genuine PDE experiment is therefore:

1. implement the Hermite--Young row-law PDE below;
2. verify its internal adjoint, Onsager, tangent-kernel, and refinement
   identities;
3. compare it against dense networks along separate \(n\)- and \(L\)-ladders;
4. describe the result as evidence for the homogenized PDE, not as a
   simulation of the presently unspecified \(K/J/N\) compiler.

---

## 1. Locked canonical model and exact finite-network algebra

For samples \(x_1,\ldots,x_m\), put \(\Delta=L^{-1}\) and
\[
h_r^0=Bx_r,\qquad z_r^\ell=W_\ell h_r^\ell,\qquad
h_r^{\ell+1}=h_r^\ell+\gamma\Delta\tanh z_r^\ell,
\]
\[
f_r=\frac1n a^\top h_r^L,\qquad
\mathcal L=\frac12\|f-y\|_2^2,\qquad e=f-y.
\]
The independent initialization and Euclidean \(\mu\)P multipliers are
\[
(W_\ell)_{ij}\sim N(0,\sigma_w^2/n),\quad
B_{ij}\sim N(0,1),\quad a_i\sim N(0,A^2),
\]
\[
\eta_{W_\ell}=L,\qquad \eta_B=n,\qquad\eta_a=n.
\]
With
\[
p_r^L=a,\qquad
D_r^\ell=\operatorname{diag}\sech^2(z_r^\ell),\qquad
\beta_r^\ell=D_r^\ell p_r^{\ell+1},
\]
the exact equations are
\[
p_r^\ell=(I+\gamma\Delta W_\ell^\top D_r^\ell)p_r^{\ell+1},
\]
\[
\dot W_\ell=-\frac{\gamma}{n}\sum_qe_q\beta_q^\ell
(h_q^\ell)^\top,\qquad
\dot a=-\sum_qe_qh_q^L,\qquad
\dot B=-\sum_qe_qp_q^0x_q^\top.
\]
The target order of limits is
\[
n\to\infty\quad\hbox{at fixed }L,\qquad L\to\infty\quad\hbox{second}.
\]
The second step is a homogenized iid-layer/Young-measure limit, not a
classical limit of a smooth matrix path \(W(s)\).

---

## 2. What the proposed \(K/J/N\) PDE is supposed to be

### 2.1 Budgets

The final note actually has three budgets
\[
(K,J,N),
\]
not a separately defined \(H\)-budget:

| symbol | intended meaning |
|---|---|
| \(K\) | maximum oriented chronological dense-response grade |
| \(J\) | maximum nonlinear expression-DAG complexity |
| \(N\) | number of slow-field depth degrees of freedom |

The quadrature size is prescribed as
\[
Q_{K,J,N}=2(K+J+N)+3.
\]
Slow depth fields are represented by one boundary value plus \(N-1\)
Legendre coefficients of their depth derivative.  Fast iid-layer tags are
represented only through a conditional Young kernel on the \(Q\) quadrature
nodes.

### 2.2 Formal first-response state

Before automatic chain-rule augmentation, the \(K=1\) slow seed list is
\[
a,\quad h_r,\quad p_r,\quad
q^0_{r\leftarrow q},q^1_{r\leftarrow q},\quad
r^0_{r\leftarrow q},r^1_{r\leftarrow q}.
\]
For \(m\) samples this is
\[
2m+4m^2
\]
depth fields plus the depthless readout coordinate.  Thus even the seed
law has dimension at least
\[
D_{\rm seed}=1+N(2m+4m^2).
\]
For the central \(m=3\) instance, \(D_{\rm seed}=1+42N\).  This is only a
lower bound: the compiler says that chain-rule tags and conditioning
records are to be appended, but does not enumerate them.

The forward response equations are
\[
\partial_s q^0_{r\leftarrow q}
=-\gamma^2D_r\beta_qG^h_{qr},\qquad
q^0_{r\leftarrow q}(0)=-Q^x_{qr}p_q(0),
\]
\[
\partial_s q^1_{r\leftarrow q}
=\gamma D_rWq^0_{r\leftarrow q},\qquad
q^1_{r\leftarrow q}(0)=0,
\]
\[
\partial_t h_r=\sum_qe_q(q^0_{r\leftarrow q}
+q^1_{r\leftarrow q}).
\]
Writing \(v^{[1]}_{r\leftarrow q}=q^0_{r\leftarrow q}
+q^1_{r\leftarrow q}\), the label-separated preactivation velocity is
\[
(\partial_tz_r)_{\leftarrow q}
=-\gamma\beta_qG^h_{qr}+Wv^{[1]}_{r\leftarrow q}.
\]
Consequently the exact, pre-closure source in the backward response is
\[
\begin{aligned}
S_{r\leftarrow q}
:={}&((\partial_tA_r)_{\leftarrow q})^\top p_r\\
={}&\gamma W^\top\!\left[
p_r\odot\tanh''(z_r)\odot
\left(-\gamma\beta_qG^h_{qr}
+Wv^{[1]}_{r\leftarrow q}\right)
\right]
-\gamma^2h_qG^\beta_{qr},
\end{aligned}
\]
where \(A_r=\gamma D_rW\).  The backward block is then
\[
-\partial_sr^0_{r\leftarrow q}=S_{r\leftarrow q},\qquad
r^0_{r\leftarrow q}(1)=-h_q(1),
\]
\[
-\partial_sr^1_{r\leftarrow q}
=\gamma W^\top D_rr^0_{r\leftarrow q},\qquad
r^1_{r\leftarrow q}(1)=0,
\]
\[
\partial_tp_r=\sum_qe_q(r^0_{r\leftarrow q}
+r^1_{r\leftarrow q}).
\]
At grade one, terms in \(S\) containing two new oriented dense actions must
be projected to zero.  The note does not supply the concrete parsed DAG
that decides these cases.

### 2.3 Formal law equation

If \(\xi\) contained every retained slow coefficient and
\(\kappa\) every retained deterministic historical coefficient, the
proposed law equation would be
\[
\partial_t\rho+
\nabla_\xi\cdot\left[
\rho\sum_qe_q[\rho]V^{(q)}_{K,J,N}
(\xi;\mathcal M[\rho],\kappa)
\right]=0,
\]
\[
\dot\kappa_\alpha
=\sum_qe_q[\rho]B_\alpha^{(q)}
(\mathcal M[\rho],\kappa).
\]
The formal characteristic drift is
\[
V^{(q)}_{K,J,N}
=\mathsf P^{\rm depth}_{K,J,N}
\int
\mathsf C_{K,J}\mathscr D_{K,J}^{(q)}
(\iota_N\xi,\zeta;\mathcal M,\kappa)
\,
\Gamma_{K,J,N}(d\zeta\mid\xi,\mathcal M,\kappa).
\]
Outputs and hidden Grams would be
\[
f_r=\int ah_r(1)\,d\rho,\qquad
G^h_{rq}(s)=\int h_r(s)h_q(s)\,d\rho.
\]
The tangent kernel is reconstructed with positive depth quadrature:
\[
\widehat\Theta_{rq}
=\widehat G^h_{rq}(1)
+Q^x_{rq}\widehat G^p_{rq}(0)
+\gamma^2\sum_{\nu=1}^Qw_\nu
\widehat G^h_{rq}(s_\nu)\widehat G^\beta_{rq}(s_\nu).
\]
This is the full extent to which the finite PDE can be reconstructed from
the note.

---

## 3. Why \((\mathrm{PDE}\text{-}1,J_*,N)\) cannot honestly be implemented

The following are mathematical data required by a PDE solver, not optional
proof details.

### 3.1 \(J_*\) is not computable from the stated grammar

\(J_*\) is defined as the least complexity that contains everything needed
for “one expansion,” but the expansion is never emitted.  More basically,
the complexity recursion does not assign complexity to several explicitly
required primitive fast tags:
\[
z=Wh,\qquad Wq^k,\qquad W^\top r^k.
\]
The displayed constructors
\(\operatorname{diag}(\tanh^{(j)}z)Wu\) and
\(W^\top\operatorname{diag}(\tanh^{(j)}z)u\) do not generate a bare
\(Wu\) or \(W^\top u\).  Therefore neither \(c(z)\), \(c(Wq)\), nor
\(c(W^\top r)\) is defined by the rules given.  The minimum \(J_*\) is
literally undefined.

### 3.2 No finite tag or moment table is present

The phrases “every budget-admissible chain-rule child,” “the coefficient
dictated by conditioning,” and “canonical DAG” are not formal rewrite rules.
There is no list of:

- retained particle tags;
- moment functions \(\phi_\alpha\);
- their grade and complexity;
- algebraic dependencies;
- zeroed outgoing children;
- or the resulting dimension \(D_{K,J,N}\).

Consequently two reasonable implementers will emit different states and
different vector fields.

### 3.3 The historical state \(\kappa\) is semantic, not constructed

The note requires every retained action of \(W(t)-W^0\) to be recoverable
from finitely many historical coefficients and says that algebraic
strongly-connected components are promoted to ODE coordinates.  It gives
neither the coefficients, their initial values, nor the functions
\(B_\alpha^{(q)}\).  Differentiating a promoted moment can generate new
moments, so termination is not a consequence of merely saying “promote the
SCC.”  There is also no independent history/age cutoff.  Thus hidden
two-training-time memory has not actually been Markovized.

### 3.4 The fast kernel \(\Gamma_{K,J,N}\) is not defined

The note displays the finite-\(n\) vectorized Gaussian conditioning identity
for
\[
W^0u,\qquad (W^0)^\top v,
\]
and states that a finite Woodbury reduction exists.  It does not give the
width-limit scalar/vector formulas, innovation variables, covariance
factors, or the endogenous-query Onsager coefficients.  In particular:

- the covariance cross-block \(\sigma_w^2vu^\top/n\) is still an
  \(n\times n\) object in the semantic derivation;
- the finite reduction that is claimed to remove it is absent;
- queries such as \(u=h,q^k\) and \(v=\beta,r^k\) depend on previous
  answers from the same matrix;
- one special Stein/Onsager check does not define the joint law for the full
  query list.

Therefore
\[
\Gamma_{K,J,N}(d\zeta\mid\xi,\mathcal M,\kappa)
\]
is a name, not a probability kernel that can be sampled or integrated.

### 3.5 The characteristic drift is missing

The displayed equations give \(\partial_th\) and \(\partial_tp\), but
\(\rho\) also carries \(q^0,q^1,r^0,r^1\).  Their training-time velocities
must be obtained by differentiating the depth equations.  Those velocities
are not displayed, and their chain rules are precisely where higher
nonlinear tags and high-to-low Gaussian contractions appear.  Referring to
\(\mathscr D_{K,J}^{(q)}\) does not supply them.

### 3.6 The initial law is missing

“A finite-dimensional Gaussian pushforward” is a valid *type* of initial
law, but no pushforward map is given.  The initial joint law must include
all depth coefficients of \(h,p,q,r\), their correlations with \(a\), and
all fast row/column answers.  This cannot be reconstructed from
\(\rho(0)=\text{Gaussian pushforward}\) alone.

### 3.7 The older audit explicitly leaves the needed target open

`dense_euclidean_continuous_depth_npde_audit.md` correctly classifies the
fixed-depth causal DMFT, the iid-depth homogenization, reciprocal Onsager
responses, and the finite compiler as conjectural.  It defines what an
admissible compiler would have to certify; it does not derive one.  The
newer note replaces that existential interface by a symbolic
least-fixed-point story, but does not fill the missing dynamic-cavity
algebra.

### 3.8 Consequence

It would be scientifically invalid to choose an ad hoc \(J\), invent a
\(\kappa\) list, use independent forward/backward Gaussian tags, and label
the result “the first PDE from the note.”  That would test a new closure.
The only code presently in the bundle uses all dense finite-width matrices,
and the bundle itself correctly reports zero compiled Liouville-PDE runs.

---

## 4. A concrete alternative: the Hermite--Young row-law PDE

This section audits the alternative suggested by the parent task.  It is
not an instantiation of the incomplete \(K/J/N\) compiler.  It is a
different, explicit Galerkin compiler whose only closure axis is a Hermite
row-query budget \(H\), optionally followed by numerical depth and
cubature refinements.

### 4.1 Static neuron label and basis

Let
\[
\theta=(b^0,a^0)\in\mathbb R^{d+1},\qquad
\mu(d\theta)=N(0,I_d)(db^0)\,N(0,A^2)(da^0).
\]
The label \(\theta\) remains static.  Current input-row and readout
coordinates are functions
\[
b_t(\theta)\in\mathbb R^d,\qquad a_t(\theta)\in\mathbb R.
\]
Fix, before training, an orthonormal Hermite basis
\(\{\phi_j\}_{j\ge1}\) of \(L^2(\mu)\), with the \(a^0\) coordinate
standardized by \(A\).  Let \(P_H\) be projection onto the first \(H\)
basis functions.

For every physical depth \(s\), training time \(t\), and row label
\(\theta\), let
\[
\rho_{s,t}^{\theta}(dw),\qquad w=(w_1,\ldots,w_H)\in\mathbb R^H,
\]
be the conditional law of the total retained row coefficients of the
current dense layer.  The initialization part and the learned part need not
be stored separately:
\[
w_j=\sigma_w\epsilon_j+c_j,\qquad
\epsilon_j\stackrel{\rm iid}{\sim}N(0,1).
\]

### 4.2 Finite-width projection derivation and scaling

At finite width define the empirical row projection
\[
w_{\ell i j}:=\sum_{k=1}^n(W_\ell)_{ik}\phi_j(\theta_k).
\]
If the empirical basis is asymptotically orthonormal, then at initialization
\[
(w_{\ell i1},\ldots,w_{\ell iH})
\Longrightarrow N(0,\sigma_w^2I_H).
\]
For
\[
H_{rj}^{n,\ell}:=\frac1n\sum_k
\phi_j(\theta_k)h_{r,k}^\ell,
\]
the projected row action is
\[
(W_{\ell,H}h_r^\ell)_i
=\sum_{j=1}^Hw_{\ell i j}H_{rj}^{n,\ell}.
\]
Most importantly, the Euclidean \(\mu\)P update gives exactly
\[
\begin{aligned}
\dot w_{\ell i j}
&=\sum_k\dot W_{\ell,ik}\phi_j(\theta_k)\\
&=-\gamma\sum_qe_q\beta_{q,i}^\ell
\left(\frac1n\sum_kh_{q,k}^\ell\phi_j(\theta_k)\right).
\end{aligned}
\]
Thus the continuum coefficient velocity is
\[
\boxed{
\dot w_j=-\gamma\sum_qe_q\beta_qH_{qj}.
}
\]
There is no missing \(n\), \(L\), \(H\), or \(\sigma_w\) factor.
\(\sigma_w\) appears only in the initial law of \(w\).

At fixed \(H\), the reconstructed finite-width operator has entries
\[
(W_{\ell,H})_{ik}
=\frac1n\sum_{j=1}^Hw_{\ell i j}\phi_j(\theta_k)
\]
and rank at most \(H\).  Therefore this is not an approximation to the
full fixed-\(L\) matrix in operator norm.  It is a candidate Galerkin
approximation to the *homogenized slow observable dynamics*, for which only
finitely many row queries and the depth-averaged transpose action are
needed.

### 4.3 Closed forward/backward fields

Define
\[
H_{rj}(s,t)
:=\int\phi_j(\theta)h_r(s,\theta,t)\,\mu(d\theta),
\]
\[
z_r(s,\theta,w,t)
:=\sum_{j=1}^Hw_jH_{rj}(s,t),
\]
\[
d_r:=\sech^2(z_r),\qquad
\beta_r(s,\theta,w,t):=d_r\,p_r(s,\theta,t).
\]
The forward equation is
\[
\boxed{
\partial_sh_r(s,\theta,t)
=\gamma\int\tanh(z_r(s,\theta,w,t))
\rho_{s,t}^{\theta}(dw),
}
\]
\[
h_r(0,\theta,t)=b_t(\theta)^\top x_r.
\]
Define the transpose moments
\[
M_{rj}(s,t)
:=\int\mu(d\theta')\int\rho_{s,t}^{\theta'}(dw)\,
w_j\beta_r(s,\theta',w,t).
\]
The backward equation is
\[
\boxed{
-\partial_sp_r(s,\theta,t)
=\gamma\sum_{j=1}^H\phi_j(\theta)M_{rj}(s,t),
}
\]
\[
p_r(1,\theta,t)=a_t(\theta).
\]

### 4.4 The genuine transport PDE

The conditional coefficient law obeys
\[
\boxed{
\partial_t\rho_{s,t}^{\theta}
+\nabla_w\cdot\left(\rho_{s,t}^{\theta}
V_H(s,\theta,w,t)\right)=0,
}
\]
where
\[
\boxed{
(V_H)_j
=-\gamma\sum_{q=1}^me_q(t)
\beta_q(s,\theta,w,t)H_{qj}(s,t).
}
\]
The remaining trained coordinates obey
\[
\boxed{
\dot b_t(\theta)
=-\sum_qe_q(t)p_q(0,\theta,t)x_q,
\qquad
\dot a_t(\theta)
=-\sum_qe_q(t)h_q(1,\theta,t).
}
\]
Equivalently, if only the sample projections
\(u_r=b^\top x_r\) are stored,
\[
\dot u_r(\theta)
=-\sum_qe_qQ^x_{rq}p_q(0,\theta).
\]
The output and residual are
\[
\boxed{
f_r(t)=\int a_t(\theta)h_r(1,\theta,t)\,\mu(d\theta),
\qquad e=f-y.
}
\]

Initialization is completely explicit:
\[
b_0(\theta)=b^0,\qquad a_0(\theta)=a^0,
\]
\[
\boxed{
\rho_{s,0}^{\theta}=N(0,\sigma_w^2I_H)
\quad\text{for every }(s,\theta).
}
\]
Because this law is centered and \(\tanh\) is odd,
\[
h_r(s,\theta,0)=(b^0)^\top x_r.
\]
For the centered independent readout initialization, the transpose moments
vanish and
\[
p_r(s,\theta,0)=a^0.
\]

This is an autonomous McKean--Vlasov transport PDE coupled to one forward
and one backward depth equation.  Its physical source variables are
\[
(s,\theta,w)\in[0,1]\times\mathbb R^{d+1}\times\mathbb R^H.
\]
Its dimension depends on \(H,m,d\), but not on \(n\), the original \(L\),
or the requested training horizon.

### 4.5 Exact transpose identity

For a slow input \(u(\theta)\), define the retained row action
\[
(T_Hu)(\theta,w)
=\sum_{j=1}^Hw_j
\int\phi_j(\theta')u(\theta')\,\mu(d\theta').
\]
For a fast row function \(v(\theta,w)\), define
\[
(T_H^\dagger v)(\theta)
=\sum_{j=1}^H\phi_j(\theta)
\int\mu(d\theta')\int\rho^{\theta'}(dw)\,w_jv(\theta',w).
\]
Then, exactly,
\[
\int\mu(d\theta)\int\rho^\theta(dw)\,
v(\theta,w)(T_Hu)(\theta,w)
=\int\mu(d\theta)\,u(\theta)(T_H^\dagger v)(\theta).
\]
The backward equation above is therefore the exact adjoint of the retained
forward operator.  It does not replace \(W^\top\) by an independent
Gaussian draw.

### 4.6 Onsager/Stein audit

At initialization, take \(w\sim N(0,\sigma_w^2I_H)\) and
\[
Z=w\cdot H[u].
\]
For smooth bounded \(\varphi\), Gaussian integration by parts gives
\[
\mathbb E[w_j\varphi(Z)]
=\sigma_w^2H_j[u]\,\mathbb E[\varphi'(Z)].
\]
Consequently,
\[
\boxed{
T_H^\dagger\varphi(T_Hu)
=\sigma_w^2(P_Hu)\,\mathbb E[\varphi'(Z)].
}
\]
This is exactly the projected Onsager identity.  If \(u\) lies in the
retained span, it is the full identity; as \(H\to\infty\), it converges to
the full identity whenever \(P_Hu\to u\) in the needed norm.

There is an important qualification.  At fixed finite depth, the original
\((W^0)^\top v\) contains a fresh, zero-mean column Gaussian innovation of
variance \(O(1)\).  The adjoint above gives its conditional **mean**, not
that innovation.  This is acceptable for the proposed continuous-depth
closure only if
\[
\frac1L\sum_{\ell=0}^{L-1}
\left[
(W_\ell^0)^\top v_\ell
-\mathbb E((W_\ell^0)^\top v_\ell\mid\text{slow state})
\right]
\longrightarrow0.
\]
With conditionally independent layers and bounded second moments, the RMS
is \(O(L^{-1/2})\).  Proving the corresponding statement under trained
global feedback is the central homogenization lemma.  Without that lemma,
the PDE is a strong candidate, not an established canonical limit.

### 4.7 Exact tangent-kernel identity for the truncated PDE

Define
\[
G^h_{rq}(s)=\int h_r(s,\theta)h_q(s,\theta)\,\mu(d\theta),
\]
\[
G^p_{rq}(0)=\int p_r(0,\theta)p_q(0,\theta)\,\mu(d\theta),
\]
\[
G^\beta_{rq}(s)
=\int\mu(d\theta)\int\rho_s^\theta(dw)\,
\beta_r(s,\theta,w)\beta_q(s,\theta,w),
\]
\[
G^{h,H}_{rq}(s)
:=\sum_{j=1}^HH_{rj}(s)H_{qj}(s)
=\langle P_Hh_r,P_Hh_q\rangle_{L^2(\mu)}.
\]
The output of the truncated system obeys the exact identity
\[
\boxed{
\dot f=-\Theta_H e,
}
\]
with
\[
\boxed{
(\Theta_H)_{rq}
=G^h_{rq}(1)
+Q^x_{rq}G^p_{rq}(0)
+\gamma^2\int_0^1
G^{h,H}_{rq}(s)G^\beta_{rq}(s)\,ds.
}
\]
Every term is positive semidefinite, so
\[
\dot{\mathcal L}=-e^\top\Theta_He\le0.
\]
This is a mandatory implementation test.  At finite \(H\), replacing
\(G^{h,H}\) by the full \(G^h\) would not be the tangent kernel of the
simulated PDE.  Parseval gives
\[
G^{h,H}_{rq}\to G^h_{rq}
\]
as \(H\to\infty\), subject to the required Hermite-tail control.

---

## 5. Is the Hermite candidate a genuine PDE or disguised matrix dynamics?

It is a genuine width-independent PDE if implemented as follows:

- evolve the conditional law \(\rho_{s,t}^{\theta}\) by characteristics in
  \(w\in\mathbb R^H\);
- compute all interactions through the displayed population moments;
- never allocate or evolve an array with two neuron/particle indices
  representing a learned \(W\);
- regard particle count and quadrature count solely as numerical resolution
  of \(\rho\), \(\mu\), and the physical depth coordinate.

A characteristic particle has only \(H\) weight coordinates, plus its
static \(\theta\) and scalar/vector fields.  Increasing the number of
particles improves integration of one fixed PDE.  This is categorically
different from the existing \(q/r\) code, whose characteristic state
contains all \(n^2L\) entries of the finite network.

For numerical work, one may use:

1. \(M_\theta\) fixed Gaussian cubature or Monte Carlo labels
   \(\theta_a\);
2. \(M_w\) conditional \(w\)-particles for each \((s_\nu,\theta_a)\);
3. \(N_s\) positive depth quadrature/collocation nodes;
4. the exact characteristic velocity above.

The storage is \(O(N_sM_\theta M_wH)\), not a learned
\(M_\theta\times M_\theta\) matrix.  Conditional replication in \(w\) for
each \(\theta_a\) is important; an unconditional row law loses the
\(\theta\)--weight correlations created by training.

---

## 6. Concrete first budgets and experiment

For the central \(d=m=3\) case, enumerate multivariate Hermites by total
degree in the four standardized variables
\[
(b_1^0,b_2^0,b_3^0,a^0/A).
\]
Natural budgets are:

| maximum Hermite degree | number \(H\) of modes |
|---:|---:|
| \(1\) | \(5\) |
| \(2\) | \(15\) |
| \(3\) | \(35\) |

The degree-one \(H=5\) system is the first nontrivial PDE.  It contains the
constant and every base linear coordinate, represents the initial hidden
features exactly, and passes the initialization covariance/Onsager tests.
The \(H=15\) system is the first useful nonlinear refinement; \(H=35\)
provides a serious convergence check.

Recommended preregistered numerical ladder:

- \(H\in\{5,15,35\}\);
- \(N_s\in\{16,32,64\}\);
- two independent \(M_\theta,M_w\) refinements;
- \(dt\in\{0.02,0.01,0.005\}\);
- the same \(T=32\) plateau rule as the finite-matrix bundle;
- dense-network comparisons on separate \(n\)- and \(L\)-ladders.

Mandatory audits:

1. numerical transpose duality for random retained \(u,v\);
2. the initialization Stein identity;
3. \(\dot f+\Theta_He=0\) at random positive-time states;
4. nonincreasing loss and nonnegative eigenvalues of \(\Theta_H\);
5. \(H,N_s,M_\theta,M_w,dt\) refinement separately;
6. no dense learned matrix in memory or code;
7. empirical \(L^{-1/2}\) decay of the discarded depth-column innovation;
8. restart from the full current PDE state
   \((b,a,\rho)\), not from a replay clock;
9. compare full hidden-Gram motion to rule out a lazy match;
10. report the projected hidden tail
    \(\|h_r-P_Hh_r\|_{L^2(\mu)}\) whenever estimable.

---

## 7. Exact limitations of the explicit candidate

The Hermite--Young PDE is non-oracular and internally closed, but the
following claims remain conjectural:

1. **Depth propagation of chaos.**  A single trained iid layer must have
   vanishing influence on the slow depth state, despite coupling through
   the global residual.
2. **Sufficiency of the static neuron label.**  After homogenization,
   \(h_r(s)\) and \(p_r(s)\) must be measurable functions of
   \(\theta=(B_i(0),a_i(0))\); no persistent local depth-disorder path may
   survive in the slow state.
3. **Column-innovation cancellation.**  The centered part of
   \(W_\ell^\top\beta_\ell\) must average away in depth, while the Onsager
   mean above survives.
4. **Hermite closure.**  Relevant \(h,p\), row-response functions, and their
   nonlinear feedback must be approximable by \(P_H\), with no uncontrolled
   high-to-low return.
5. **All-time stability.**  Finite-time convergence does not itself prove a
   horizon-independent \(H\).

At fixed \(H\), the model is the gradient flow of a projected row-operator
system.  It is not the full dense fixed-\(L\) network and should not be
advertised as such.  The scientific claim tested by simulation is:
\[
\lim_{H\to\infty}
\mathcal O_H(t)
\stackrel{?}{=}
\lim_{L\to\infty}\lim_{n\to\infty}
\mathcal O_{n,L}(t),
\]
uniformly on the tested time interval (and ultimately, conjecturally,
uniformly for \(t\ge0\)).

---

## 8. Final recommendation

There is currently no honest way to “implement
\((\mathrm{PDE}\text{-}1,J_*,N)\)” from the supplied conjecture note.  A
purported implementation would necessarily fill in undefined mathematical
objects and would need to be presented as a newly proposed closure.

The Hermite--Young row-law system in Section 4 is the strongest
non-oracular repair available from the same architecture:

- it uses the exact standard dense Euclidean \(\mu\)P scaling;
- it has a completely explicit state, drift, initialization, and readout;
- it preserves the retained forward/transpose duality and the projected
  Onsager identity;
- it has an exact PSD tangent kernel and loss-dissipation identity;
- it is genuinely width-independent and admits a standard particle
  solution of a transport PDE;
- and its only architecture-identification gap is sharply exposed as a
  trained iid-depth homogenization/Hermite-tail theorem.

Simulating this PDE and obtaining stable convergence in
\((H,N_s,M_\theta,M_w,dt)\), followed by agreement with increasing
\((n,L)\), would be the first actual numerical evidence for a
width-independent neural PDE in the canonical model.  Failure would also be
informative: it would localize the obstruction to depth homogenization,
transpose innovation, or Hermite high-to-low feedback rather than to the
already successful finite-matrix \(q/r\) truncation.

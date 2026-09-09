# Two-sample symmetry, radial coercivity, and the affine baseline

This is a bounded sidecar to CONTRACT.md, not a full two-sample population,
GF, or exact-GD theorem. It establishes symmetry at finite clipped Euler
level, inheritance by constructed limits, a strong Hilbert-space radial
lemma, initial projected kernels, pre-target energy and clock bounds,
and the requested affine baseline variance lemma. The main argument
retains nonlinear response estimates, cutoff removal, nonlinear
continuation, state comparison, and the finite-width/GD bridges.

The skill /etc/codex/skills/solve-math-rigorously/SKILL.md and the contract
were read in full. Only relevant finite-program/action-space,
singular-Gram, and gradient/clock passages were inspected in:

- /tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md,
  whose SHA-256 was verified as
  f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4;
- /tmp/l3-activation-design-oaGjWO/OFFSET_ARCTAN_GLOBAL_THEOREM.md.

No numerical experiment or agent was used.

## 1. Normalization and scalar reduction

Write
\[
G_{ab}=x_a^Tx_b/d,\qquad
G=\begin{pmatrix}1&\rho\\ \rho&1\end{pmatrix},\quad -1\le\rho<1,
\qquad y_1=\sigma,\quad y_2=\sigma\tau,
\]
where \(\sigma\in\{-1,1\}\) and \(\tau=y_1y_2\in\{-1,1\}\).
Let \(\pi\) interchange the samples. Same labels mean \(\tau=1\);
opposite labels mean \(\tau=-1\).

Use three separate population spaces
\(\mathcal H_\ell=L^2(\Omega_\ell)\), a first weight field
\(w\in L^2(\Omega_1;\mathbb R^d)\), bounded actions
\(A:\mathcal H_1\to\mathcal H_2\),
\(B:\mathcal H_2\to\mathcal H_3\), and readout \(C\in\mathcal H_3\).
Set
\[
z_a^{(1)}=w\cdot x_a,\quad h_a^{(1)}=\phi(z_a^{(1)}),\quad
z_a^{(2)}=Ah_a^{(1)},\quad h_a^{(2)}=\phi(z_a^{(2)}),
\]
\[
z_a^{(3)}=Bh_a^{(2)},\quad h_a^{(3)}=\phi(z_a^{(3)}),\qquad
f_a=\langle C,h_a^{(3)}\rangle_3.
\]
The projected feature and scalar objective are
\[
H=\frac{y_1h_1^{(3)}+y_2h_2^{(3)}}2,\qquad
g=\langle C,H\rangle_3=\frac{y_1f_1+y_2f_2}2.                 \tag{1}
\]
We prove below that the constructed symmetric population path obeys
\(f_a=y_ag\). On that path the contract's normalization gives
\[
L=\frac{(f_1-y_1)^2+(f_2-y_2)^2}{2}=(1-g)^2,\qquad
\dot\Theta=-\sum_a(f_a-y_a)\nabla f_a=2(1-g)\nabla g.        \tag{2}
\]
Our feature-time convention is therefore
\[
\Theta'=\nabla g,\qquad ds/dt=2(1-g).                       \tag{3}
\]
The projected kernel in this convention is \(y^TKy/4\).

## 2. Symmetry before uncut uniqueness

### Finite clipped Euler

Because the inputs have identical norm, the orthogonal involution
\[
u=\frac{x_1-x_2}{\|x_1-x_2\|},\qquad Q=I-2uu^T
\]
satisfies
\[
Qx_1=x_2,\quad Qx_2=x_1.                                  \tag{4}
\]
Indeed, \(\|x_1-x_2\|^2=2d(1-\rho)\) and
\((x_1-x_2)^Tx_1=d(1-\rho)\). The formula includes \(\rho=-1\).

At finite width define
\[
\mathcal T(W^{(1)},A,B,C)=(W^{(1)}Q,A,B,\tau C).
\]
With the dataset and labels held fixed,
\[
h_a^{(\ell)}(\mathcal T\Theta)=h_{\pi a}^{(\ell)}(\Theta),
\quad f_a(\mathcal T\Theta)=\tau f_{\pi a}(\Theta),
\]
\[
r_a(\mathcal T\Theta)=\tau r_{\pi a}(\Theta),\qquad
\delta_a^{(\ell)}(\mathcal T\Theta)
   =\tau\delta_{\pi a}^{(\ell)}(\Theta).                   \tag{5}
\]
Here \(y_{\pi a}=\tau y_a\), and the backward fields are linear in
the readout. No oddness of the activation is needed.

In each hidden update the signs in \(r_a\delta_a\) cancel.
For the first block also use \(x_{\pi a}^T=x_a^TQ\).
The readout update acquires the sign \(\tau\). Thus the raw
vector field is equivariant under \(\mathcal T\).

The scalar objective (1) is itself invariant under \(\mathcal T\),
since \(y_{\pi a}=\tau y_a\). This transformation is an isometry
of the raw parameter metric, so its scalar gradient is equivariant
as well. The Euler and limit arguments below therefore apply both
to physical loss updates and to auxiliary scalar feature updates,
using the corresponding equivariant clips.

The same calculation applies to finite clipped Euler provided:

- both samples use identical deterministic coordinate instructions;
- clips of sign-changing slots in (5) are odd, including any clipped
  readout, residual, or backward factor;
- additional norm cutoffs are invariant under \(\mathcal T\).

For example, to obtain a globally Lipschitz finite coordinate program,
cap preactivation arguments identically for both samples and cap
unbounded scalar factors before multiplication. Bottom updates remain
sums of scalar factors times the fixed input vectors; do not clip
the weight vector componentwise in a basis that breaks \(Q\)-equivariance.
For the smooth activations considered here this supplies suitable
fixed finite programs. Uniform removability of those auxiliary clips
is a separate issue.

For the resulting one-step map \(E_{R,\Delta}\),
\[
E_{R,\Delta}\mathcal T=\mathcal T E_{R,\Delta}.              \tag{6}
\]
Gaussian initialization is invariant under \(W^{(1)}\mapsto W^{(1)}Q\),
independently of the other blocks. The zero readout is invariant under
its sign change. Induction in (6) proves the joint path-law identity
\[
(\Theta_0,\ldots,\Theta_N)\overset{\rm law}=
(\mathcal T\Theta_0,\ldots,\mathcal T\Theta_N).              \tag{7}
\]
The small independent centered Gaussian finite readout in the contract
also satisfies (7); its population limit is zero.

Equation (7) generally does not give \(f_2=\tau f_1\) in one finite
realization. With exactly zero initial readout, one raw physical Euler
step leaves the hidden state unchanged and gives
\[
C_1=\Delta\sigma(h_{1,0}^{(3)}+\tau h_{2,0}^{(3)}),
\]
\[
f_{1,1}-\tau f_{2,1}
=\Delta\sigma\left(\|h_{1,0}^{(3)}\|_n^2
                        -\|h_{2,0}^{(3)}\|_n^2\right),
\qquad \|v\|_n^2=n^{-1}\sum_i v_i^2.                      \tag{8}
\]
Those empirical diagonal norms need not agree. An exactly invariant
finite realization or an imposed pairing would be an additional
initialization condition. Even at \(\rho=-1\), the exact identity
\(z_2^{(1)}=-z_1^{(1)}\) does not equate shifted top feature norms.

### Deterministic population laws

The fixed-program input from the cited local proof is the following:
a fixed finite transcript of calls to independent Gaussian matrices
in both orientations, suitable Lipschitz coordinate instructions with
bounded derivatives, and iid finite-moment root tuples has deterministic
limiting same-layer joint empirical laws, including second moments.
Empirical scalar feedback is handled by causal freezing of already
constructed limiting contractions and finite induction. Singular query
Grams are treated at fixed transcript length.

In the present application, the root tuple contains either the entire
first weight row \(N(0,I_d/d)\), or its two projections with covariance
\(G\). It has all moments; the two hidden matrices have the required
independent Gaussian laws; and the auxiliary clips give the required
coordinate instructions. Adding a second sample adds finitely many
queries to the same matrices. In particular, singularity at \(\rho=-1\)
does not require a Gram inverse. This invokes only the finite-program
dependency, not a two-sample mesh-uniform estimate or uncut theorem.

Pass (7) to a deterministic limiting joint law of sample and time
slots. That law is invariant under the simultaneous transformations
(5). Second-moment convergence gives deterministic contractions
\[
f_{a,k}=\tau f_{\pi a,k},\qquad f_{a,k}=y_ag_k.              \tag{9}
\]
More explicitly, if \(F_n\) has a law invariant under \(F\mapsto\tau PF\)
and converges in probability to deterministic \(F\), its limiting
laws are both \(\delta_F\) and \(\delta_{\tau PF}\), forcing equality.
A random limit would not give that conclusion.

One may realize this symmetry exactly on the canonical population
spaces. Close the countable action/probe collection under the root
transformation and sample exchange. Its invariant joint law defines
measure-preserving involutions and composition operators \(U_\ell\)
on \(\mathcal H_\ell\). They are unitary involutions and commute
with pointwise coordinate functions. With \(w\) written as a column
field, initially
\[
U_1w_0=Qw_0,\qquad U_2A_0=A_0U_1,\qquad
U_3B_0=B_0U_2,\qquad C_0=0.                               \tag{10}
\]
The action identities first hold on paired matrix-query nodes and
extend to all generated \(L^2\) vectors by boundedness of the actions.

Direct induction in the population Euler updates preserves
\[
U_1w=Qw,\quad U_2A=AU_1,\quad U_3B=BU_2,\quad U_3C=\tau C,
\]
\[
U_\ell h_a^{(\ell)}=h_{\pi a}^{(\ell)},\qquad
U_\ell\delta_a^{(\ell)}=\tau\delta_{\pi a}^{(\ell)}.         \tag{11}
\]
For instance, conjugating a hidden update
\(\sum_a r_a\delta_a\otimes h_a\) gives
\(\sum_a r_a\tau\delta_{\pi a}\otimes h_{\pi a}\), the original
update because \(r_{\pi a}=\tau r_a\). The first/readout blocks
follow from the same substitutions used in (6). The prediction
identity follows from
\(\langle C,U_3h_a\rangle=\langle U_3C,h_a\rangle\).
This is an induction from the initial state, not a uniqueness argument.

Every strong fixed-clip mesh limit, and every subsequently constructed
strong uncut limit, inherits these identities. Joint-law symmetry
passes under weak convergence; contractions additionally require their
moment convergence. Thus the claim applies to limits of the symmetric
approximations on their constructed intervals. Extending it to every
arbitrary uncut solution requires a separate selection or uniqueness
result.

In this realization, \(C,H\) lie in the \(\tau\)-eigenspace of \(U_3\);
the other feature sector is orthogonal to \(C\). This does not equate
the two hidden sample fields or pair neurons from different layers.
The scalar objective still uses the full paired hidden state.

## 3. Strong Hilbert radial coercivity

Let \(\mathcal X,\mathcal Y\) be real Hilbert spaces, and let
\(g(\vartheta,C)=\langle C,H(\vartheta)\rangle_{\mathcal Y}\).
Assume along a strong solution that bounded linear maps
\(J_s:\mathcal X\to\mathcal Y\) give
\[
C'=H(\vartheta),\qquad \vartheta'=J_s^*C,\qquad
\frac d{ds}H(\vartheta(s))=J_s\vartheta'(s),\qquad C(0)=0.   \tag{12}
\]
Then
\[
C''=J_sJ_s^*C,\qquad
\langle C,C''\rangle=\|J_s^*C\|_{\mathcal X}^2\ge0.         \tag{13}
\]
Sufficient strong regularity is that both curves are \(C^1\), the
feature chain rule holds strongly, and its right-hand side is
continuous. A Fréchet \(C^1\) feature map suffices but is not necessary.

The radial conclusion itself needs only
\[
C\in C^1([0,S);\mathcal Y),\quad
C'\in AC_{\rm loc}((0,S);\mathcal Y),\quad
\langle C,C''\rangle\ge0\quad\hbox{a.e.}                  \tag{14}
\]
Absolute continuity is strong/Bochner absolute continuity. Under (14),
with \(h_0=\|C'(0)\|=\|H(\vartheta_0)\|\),
\[
\|C(s)\|\ge sh_0,\qquad \|C'(s)\|\ge h_0
\quad(0\le s<S).                                         \tag{15}
\]

Proof: set \(r_\epsilon=(\|C\|^2+\epsilon^2)^{1/2}\). On compact
subintervals of \((0,S)\), strong Hilbert differentiation and
Cauchy--Schwarz give, almost everywhere,
\[
r_\epsilon''
=\frac{\|C'\|^2+\langle C,C''\rangle}{r_\epsilon}
 -\frac{\langle C,C'\rangle^2}{r_\epsilon^3}
\ge\frac{\epsilon^2\|C'\|^2}{r_\epsilon^3}
   +\frac{\langle C,C''\rangle}{r_\epsilon}\ge0.             \tag{16}
\]
Thus \(r_\epsilon\) is convex. Uniform convergence to \(r=\|C\|\),
then continuity at zero, makes \(r\) convex on \([0,S)\).
Since \(C(s)=sC'(0)+o(s)\), \(r'_+(0)=h_0\).
Convexity gives \(r(s)\ge sh_0\). For \(h_0>0\), \(r(s)>0\) for
\(s>0\), so
\[
h_0\le r'(s)=\frac{\langle C,C'\rangle}{\|C\|}
             \le\|C'(s)\|.
\]
For \(h_0=0\), (15) is immediate. This proves the claim, including
zeros of \(C\), without finite-dimensional compactness or coordinate
summation.

For (12), the scalar chain rule also yields
\[
g'=\|H\|^2+\|J_s^*C\|^2=\|\Theta'\|^2\ge h_0^2.           \tag{17}
\]
Alternatively \(g=\langle C,C'\rangle=rr'\ge sh_0^2\).
The conclusion is a uniform lower bound on feature speed/norm; it
does not assert that \(\|C'\|\) itself is monotone or that features
are pointwise positive.

The clipped backward equation need not be a gradient equation, and
explicit Euler need not preserve (13), (16), or (17). The symmetry
argument operates at clipped Euler level; this lemma operates on a
constructed strong uncut gradient path, or on finite uncut GF.

## 4. Application in the raw population metric

The affine hidden Hilbert space has coordinates
\[
\vartheta=(w-w_0,A-A_0,B-B_0),\qquad
\|\dot\vartheta\|_{\mathcal X}^2
=d\,\mathbb E_1\|\dot w\|_{\mathbb R^d}^2
 +\|\dot A\|_{\rm HS}^2+\|\dot B\|_{\rm HS}^2.              \tag{18}
\]
Add \(\|\dot C\|_3^2\) for the full state. This matches the contract.
The initial actions need only be bounded. Trained rank-one increments
are Hilbert--Schmidt since
\(\|u\otimes v\|_{\rm HS}=\|u\|\|v\|\), including for their Bochner
integrals.

It suffices for the following regularity argument that
\(\phi\in C^1(\mathbb R)\) have bounded continuous derivative.
It has at most linear growth; the features are therefore in \(L^2\)
at every affine Hilbert state. Forward propagation is locally
Lipschitz in (18), using bounded current actions,
\(\|M\|_{\rm op}\le\|M\|_{\rm HS}\), and the Lipschitz activation.
Features and their bounded linearizations are bounded on bounded
affine state balls.

Here is the strong chain rule actually needed. If \(z(s)\) is
\(L^2\)-valued \(C^1\), \(v=z'(s)\), and
\[
a_h=\int_0^1\phi'(z(s)+u[z(s+h)-z(s)])\,du,
\]
then
\[
\frac{\phi(z(s+h))-\phi(z(s))}{h}
   =a_h\frac{z(s+h)-z(s)}h.
\]
The multipliers are uniformly bounded and converge in probability
to \(\phi'(z(s))\). Split the difference from \(\phi'(z(s))v\)
into \(a_h[(z(s+h)-z(s))/h-v]\) and
\([a_h-\phi'(z(s))]v\).
The first tends to zero in \(L^2\) by strong differentiability.
For the second, truncate the fixed \(L^2\) vector \(v\), pass to
the limit with bounded multipliers, and then remove its \(L^2\) tail.
This also proves continuity of the resulting derivative. Bounded
bilinear operator actions obey the strong product rule.

For a hidden variation \((v,M_2,M_3)\), the notation \(J=DH\) means
the following bounded directional linearization with this path
chain rule:
\[
\dot z_a^{(1)}=v\cdot x_a,\quad
\dot h_a^{(1)}=\phi'(z_a^{(1)})\dot z_a^{(1)},
\]
\[
\dot z_a^{(2)}=M_2h_a^{(1)}+A\dot h_a^{(1)},\quad
\dot h_a^{(2)}=\phi'(z_a^{(2)})\dot z_a^{(2)},
\]
\[
\dot z_a^{(3)}=M_3h_a^{(2)}+B\dot h_a^{(2)},\quad
J(v,M_2,M_3)=\frac12\sum_a y_a\phi'(z_a^{(3)})\dot z_a^{(3)}.
                                                               \tag{19}
\]
This does not claim Fréchet differentiability of a nonlinear
Nemytskii map on all of \(L^2\).

Set
\[
\delta_a^{(3)}=C\phi'(z_a^{(3)}),\quad
\delta_a^{(2)}=\phi'(z_a^{(2)})B^*\delta_a^{(3)},\quad
\delta_a^{(1)}=\phi'(z_a^{(1)})A^*\delta_a^{(2)}.
\]
Taking adjoints in (19) gives
\[
J^*C=\left(
 \frac1{2d}\sum_a y_a\delta_a^{(1)}x_a,\quad
 \frac12\sum_a y_a\delta_a^{(2)}\otimes h_a^{(1)},\quad
 \frac12\sum_a y_a\delta_a^{(3)}\otimes h_a^{(2)}
\right).                                                    \tag{20}
\]
In particular,
\[
(z_a^{(1)})'=\frac12\sum_bG_{ab}y_b\delta_b^{(1)}.          \tag{21}
\]
The off-diagonal coupling is retained. At \(\rho=-1\) this preserves
\(z_2^{(1)}=-z_1^{(1)}\) and requires no Gram inverse.

The scalar \(g\) is \(C^1\) in the affine Hilbert norm. Formulae
(19)--(20) first give its directional gradient \((J^*C,H)\).
This gradient is norm continuous: use the fixed-factor truncation
argument for bounded gates, successively backwards, and the
rank-one difference inequality in HS norm. Integrating the
directional derivative along a line segment then gives
\[
g(\Theta+v)-g(\Theta)-\langle\nabla g(\Theta),v\rangle
=\int_0^1\langle\nabla g(\Theta+uv)-\nabla g(\Theta),v\rangle\,du
=o(\|v\|).
\]
This proves scalar Fréchet differentiability without the stronger,
generally false \(L^2\)-feature assertion. For a constructed strong
solution of (20), the forward chain rule makes \(C\) strongly \(C^2\)
and proves (13), (17). It does not require an uncut uniqueness theorem.

The raw sample-kernel blocks are
\[
K^{(1)}_{ab}=G_{ab}
       \langle\delta_a^{(1)},\delta_b^{(1)}\rangle_1,
\]
\[
K^{(2)}_{ab}=\langle\delta_a^{(2)},\delta_b^{(2)}\rangle_2
               \langle h_a^{(1)},h_b^{(1)}\rangle_1,
\]
\[
K^{(3)}_{ab}=\langle\delta_a^{(3)},\delta_b^{(3)}\rangle_3
               \langle h_a^{(2)},h_b^{(2)}\rangle_2,\qquad
K^{(4)}_{ab}=\langle h_a^{(3)},h_b^{(3)}\rangle_3.
\]
Each is a Gram matrix in its parameter block, hence positive
semidefinite, including at \(\rho=-1\). Define
\[
\kappa_\ell=\frac14y^TK^{(\ell)}y,\qquad
\kappa=\sum_{\ell=1}^4\kappa_\ell
      =\|J^*C\|^2+\|H\|^2=g'.                             \tag{22}
\]
For example,
\[
\kappa_1\big|_{\rho=-1}
=\frac14\|y_1\delta_1^{(1)}-y_2\delta_2^{(1)}\|_1^2.
\]
Population symmetry gives equal diagonal entries in every block, so
\(y\) is its sum or difference eigenvector. Radial coercivity gives
\[
\kappa_4(s)=\|H(s)\|^2\ge\|H(0)\|^2=:\kappa_0.            \tag{23}
\]
At zero initial readout all hidden backward fields and hidden kernel
blocks vanish. Thus the initial total projected kernel equals
\(\kappa_0\).

## 5. Initial projected kernels

Initial Gaussian propagation uses uncentered second moments, including
the constant activation shift. Let
\[
q_\ell=\mathbb E(h_{a,0}^{(\ell)})^2,\qquad
c_\ell=\mathbb E h_{1,0}^{(\ell)}h_{2,0}^{(\ell)},\qquad
q_0=1,\quad c_0=\rho.
\]
At each layer the initial preactivation pair is centered Gaussian
with diagonal \(q_{\ell-1}\) and off-diagonal \(c_{\ell-1}\).

For the affine comparator \(\phi_0(z)=1+z\),
\(q_\ell=1+q_{\ell-1}=\ell+1\) and
\(c_\ell=1+c_{\ell-1}=\ell+\rho\). Therefore
\[
K^{(4)}(0)=\begin{pmatrix}4&3+\rho\\3+\rho&4\end{pmatrix},
\qquad
\kappa_0=
\begin{cases}
(7+\rho)/2,&\tau=1,\\
(1-\rho)/2,&\tau=-1.
\end{cases}                                                \tag{24}
\]
These are \(3\) and \(1\) at \(\rho=-1\). The unprojected
eigenvalues are \(7+\rho\) and \(1-\rho\); (24) is half of those.
The affine model is a comparator, not an admissible nonlinear
resolution of the main contract.

For \(\phi_e=1+\psi_e\), \(\psi_e(z)=z+e\arctan z\), take any
fixed finite real \(e\). The function \(\psi_e\) is odd, continuous,
nonconstant, and of at most linear growth. If \((U,V)\) is centered
Gaussian with common variance \(q>0\), covariance \(c\), the new
moments satisfy
\[
\widetilde q-\widetilde c
 =\frac12\mathbb E[\psi_e(U)-\psi_e(V)]^2,\qquad
\widetilde q+\widetilde c
 =2+\frac12\mathbb E[\psi_e(U)+\psi_e(V)]^2\ge2.             \tag{25}
\]
For \(-q<c<q\), the pair has positive density on every open rectangle.
Continuity and nonconstancy give an open rectangle where the two
function values differ, proving positivity of the first expression.
For \(c=-q\), \(V=-U\) almost surely, and that expression is
\(2\mathbb E\psi_e(U)^2>0\). A nonconstant odd continuous function
cannot vanish almost everywhere under a Gaussian with positive
variance.

Starting at \(q_0=1,c_0=\rho<1\), (25) thus gives positive contrast
at the first layer, even at \(\rho=-1\). Also \(q_\ell+c_\ell>0\),
so subsequent preactivation pairs satisfy
\(-q_\ell<c_\ell<q_\ell\). Induction through all three layers yields
\[
\kappa_0^{\rm opp}=(q_3-c_3)/2>0,\qquad
\kappa_0^{\rm same}=(q_3+c_3)/2\ge1.                        \tag{26}
\]
In particular any universally fixed \(e>0\) has strictly positive
initial contrast for every \(\rho<1\), including \(-1\).

For \(e\ge0\), \(\psi_e'\ge1\) and oddness give
\[
|\psi_e(u)-\psi_e(v)|\ge|u-v|,\qquad
|\psi_e(u)+\psi_e(v)|\ge|u+v|.
\]
Thus \(q_\ell-c_\ell\ge q_{\ell-1}-c_{\ell-1}\) and
\(q_\ell+c_\ell\ge2+q_{\ell-1}+c_{\ell-1}\), so
\[
\kappa_0^{\rm opp}\ge(1-\rho)/2,\qquad
\kappa_0^{\rm same}\ge(7+\rho)/2.                          \tag{27}
\]
These are initial-kernel calculations, not a nonlinear response
estimate or a separation bound uniform as \(\rho\uparrow1\).

## 6. Pre-target feature budget, energy, and physical clock

On any constructed strong uncut feature path with \(\kappa_0>0\),
\[
g'(s)\ge\kappa_0,\quad g(s)\ge\kappa_0s,\quad
g(s)<1\ \Longrightarrow\ s<S_0:=1/\kappa_0.                \tag{28}
\]
For \(e\ge0\), sufficient deterministic pre-target budgets are
\[
S_0\le
\begin{cases}
2/(7+\rho),&\text{same labels},\\
2/(1-\rho),&\text{opposite labels}.
\end{cases}                                                \tag{29}
\]
The entire pre-target feature interval is therefore bounded in terms
of the fixed pair. No arbitrary extra interval after the target is
needed to define the physical clock.

For \(0\le u<v\) before the target, the exact gradient identity gives
\[
\int_u^v\|\Theta'(s)\|^2\,ds=g(v)-g(u),\qquad
\|\Theta(v)-\Theta(u)\|
\le\sqrt{(v-u)[g(v)-g(u)]}\le\sqrt{v-u},                    \tag{30}
\]
and in particular
\[
\|\Theta(s)-\Theta(0)\|\le\sqrt{s\,g(s)}\le\sqrt{S_0}.       \tag{31}
\]
Hence a pre-target branch approaching a finite endpoint is strongly
Cauchy and has finite energy and length. Completeness gives a finite
affine Hilbert limit: first field/readout in \(L^2\), trained matrix
increments in HS norm and therefore operator norm, and every forward
feature in \(L^2\). This rules out state-norm blow-up and loss of
strong convergence along this single path. No compactness of bounded
Hilbert balls is asserted.

The gradient is bounded on the ball (31), by bounded gates, bounded
actions, and bounded forward \(L^2\) norms in (20). Its norm
continuity gives a finite limiting velocity at the endpoint, so the
path extends to the endpoint itself as a strong solution.

The continuation claim has a precise additional hypothesis. If local
existence is available at every such reached state, a maximal
pre-target endpoint with limiting \(g<1\) can be extended, and a first
hit \(s_*\le S_0\) follows. This uses local existence, not uniqueness.
For a smooth finite-dimensional scalar feature equation, local
Lipschitzness gives that existence. A continuous vector field on an
infinite Hilbert space does not by itself have a general Peano
existence theorem; the nonlinear population argument must supply its
own reached-state construction and control of its solution class.
The energy bound does not replace that work or apply automatically
to clipped Euler.

Suppose now that the symmetric feature path has been constructed
through a finite state with \(g(s_*)=1\). Its continuous kernel is
bounded on \([0,s_*]\), say \(\kappa_0\le g'\le M<\infty\).
Define
\[
t(s)=\int_0^s\frac{du}{2[1-g(u)]},\qquad 0\le s<s_*.
                                                               \tag{32}
\]
Since \(1-g(s)=\int_s^{s_*}g'(u)\,du\le M(s_*-s)\), this integral
diverges as \(s\uparrow s_*\). Its inverse is a global physical
clock with \(s(t)<s_*\) for every finite \(t\). Along that path,
\[
1-g(t)=\exp\!\left[-2\int_0^t\kappa(s(v))\,dv\right]
 \le e^{-2\kappa_0t},\qquad L(t)\le e^{-4\kappa_0t}.        \tag{33}
\]
The scalar clock is unique on this given feature path because its
right-hand side is \(C^1\). This is not a uniqueness or width-limit
claim for the full two-sample system.

## 7. Affine baseline: positive hidden variances through a target margin

This section concerns the scalar feature ascent of (1) with
\(\phi_0(z)=1+z\). Finite auxiliary systems used in its proof also
ascend this scalar \(g\); they are not asserted to equal finite-width
two-sample loss training. The latter distinction is necessary because
(8) generally prevents an exact finite-width scalar loss reduction.

### Existence on a compact interval through \(g=1+\gamma\)

In the affine model, \(H\) is a finite sum of continuous multilinear
expressions in the hidden Hilbert variables. For example these include
\(B{\bf1}\), \(BA{\bf1}\), and \(BA(w\cdot x_a)\), with bounded
initial actions plus HS variations. Thus \(g\) is a continuous
polynomial on the affine Hilbert space, and its gradient is locally
Lipschitz with bounded derivatives on bounded balls.

This gives local strong existence and uniqueness in infinite dimension:
on a closed ball around the initial state, let the vector field have
bound \(M\) and Lipschitz constant \(L\). For a time interval of length
less than the radius divided by \(M\), and less than \(1/L\), the
integral map on continuous curves in that ball maps it into itself and
is a contraction. Its fixed point solves the ODE. This construction
also applies at any finite reached state.

Fix any finite \(b=1+\gamma>1\), independent of width or \(e\).
While \(g<b\), the radial and energy arguments give
\[
s<b/\kappa_0,\qquad
\int_0^s\|\Theta'\|^2=g(s)<b,\qquad
\|\Theta(s)-\Theta(0)\|\le b/\sqrt{\kappa_0}.               \tag{34}
\]
If a maximal branch stopped before hitting \(b\), (30), with \(b\)
in place of \(1\), would give a finite strong endpoint; the preceding
local construction would extend it. A branch staying below \(b\)
for arbitrarily large feature time contradicts \(g(s)\ge\kappa_0s\).
Hence there is a unique first hit
\[
S_b\le b/\kappa_0,\qquad g(S_b)=b,
\]
and a strong bounded affine baseline on \([0,S_b]\). Its local
existence/uniqueness has now been justified, rather than imported
from an unconstructed nonlinear equation. Finite Euler convergence
on this interval follows from the same bounded-ball Lipschitz
estimate and the integral equation.

### Common and contrast coordinates

To avoid confusing dimension \(d\) with a contrast vector, write
\[
m=(x_1+x_2)/2,\qquad v=(x_1-x_2)/2,\qquad m\cdot v=0,
\]
\[
v_M=\|m\|^2/d=(1+\rho)/2,\qquad
v_D=\|v\|^2/d=(1-\rho)/2>0.
\]
Define the common and contrast preactivations
\[
M_\ell=(z_1^{(\ell)}+z_2^{(\ell)})/2,\qquad
D_\ell=(z_1^{(\ell)}-z_2^{(\ell)})/2.
\]
For the affine network they satisfy the exact identities
\[
M_1=w\cdot m,\quad D_1=w\cdot v,\quad
M_2=A({\bf1}+M_1),\quad D_2=AD_1,
\]
\[
M_3=B({\bf1}+M_2),\quad D_3=BD_2,\qquad
z_a^{(\ell)}=M_\ell+(-1)^{a-1}D_\ell.                     \tag{35}
\]
Initially \(M_1,D_1\) are independent Gaussian fields of variances
\(v_M,v_D\); \(v_M=0\) is permitted. Initial forward Gaussian
propagation gives
\[
\mathbb E D_{\ell,0}=0,\qquad \|D_{\ell,0}\|_\ell^2=v_D
\quad(\ell=1,2,3).                                       \tag{36}
\]

### Opposite labels

Now \(H=\sigma D_3\) and
\[
g=\sigma\langle C,BAD_1\rangle.
\]
The feature equations reduce exactly to
\[
C'=\sigma D_3,\quad
B'=\sigma C\otimes D_2,\quad
A'=\sigma B^*C\otimes D_1,\quad
D_1'=\sigma v_D A^*B^*C,\quad M_1'=0.                     \tag{37}
\]
These are a deep linear scalar feature objective, with bottom
metric factor \(v_D\). The constants cancel in the objective, but
remain in the common preactivations (35).

The transformation \(D_{1,0}\mapsto-D_{1,0}\) preserves initialization.
In (37) it sends \(D_\ell,C\) to their negatives and leaves \(A,B,M_1\)
unchanged. This is already an exact finite Euler equivariance;
it passes to the constructed affine flow. The common fields in
(35) are unchanged by that transformation. Consequently each
deterministic population joint law satisfies
\[
\mathbb E D_\ell(s)=0,\qquad
\mathbb E[M_\ell(s)D_\ell(s)]=0.
\]
Thus
\[
\operatorname{Var}(z_a^{(\ell)}(s))
=\operatorname{Var}(M_\ell(s))+\|D_\ell(s)\|_\ell^2.        \tag{38}
\]

By (24), \(g'(s)\ge\kappa_0=v_D\), hence \(g(s)>0\) for every
\(s>0\). If any of \(D_1,D_2,D_3\) were zero in its Hilbert space,
the bounded-action identities in (35) would give \(D_3=0\), hence
\(g=0\), a contradiction. All three contrast norms are therefore
positive for \(s>0\); they are positive at zero by (36).
Strong continuity and compactness of the time interval imply
\[
b_D:=\min_{\ell=1,2,3}\ \min_{0\le s\le S_b}
               \|D_\ell(s)\|_\ell>0.
\]
Together with (38),
\[
\inf_{a,\ell,\,0\le s\le S_b}
     \operatorname{Var}(z_a^{(\ell)}(s))\ge b_D^2>0.       \tag{39}
\]
This includes \(\rho=-1\), where \(v_D=1\) and \(M_1=0\).
The bound may depend on the fixed pair and on \(b\).

### Same labels

Here
\[
H=\sigma({\bf1}+M_3),\qquad
g=\sigma\langle C,{\bf1}+B[{\bf1}+A({\bf1}+M_1)]\rangle.
\]
The scalar objective and its training equations depend only on
\(M_1,A,B,C\). Explicitly,
\[
C'=\sigma({\bf1}+M_3),\quad
B'=\sigma C\otimes({\bf1}+M_2),\quad
A'=\sigma B^*C\otimes({\bf1}+M_1),
\]
\[
M_1'=\sigma v_M A^*B^*C,\qquad D_1'=0.                    \tag{40}
\]
Thus the contrast root is frozen and independent of the information
that drives this scalar training. Independence at the root alone
does not assert independence of trained matrices from their own
initial disorder. The following conditional fixed-Euler argument
handles that dependence before taking a continuous-time limit.

Let
\(\mathscr F_n=\sigma(M_{1,0},A_0,B_0)\), with the readout initially
zero. Every step of the finite scalar affine Euler prefix
\(M_1,A,B,C\) is measurable with respect to \(\mathscr F_n\).
Meanwhile \(D_0=D_{1,0}\) is an independent
\(N(0,v_DI_n)\) vector. For every \(\mathscr F_n\)-measurable matrix
\(T_n\),
\[
\mathbb E[\|T_nD_0\|_n^2\mid\mathscr F_n]
       =\frac{v_D}{n}\|T_n\|_F^2.                        \tag{41}
\]
This is the exact normalization: a bounded ordinary Frobenius
increment has conditional squared RMS action \(O(n^{-1})\), not
an asserted \(O(n^{-1})\) Frobenius norm.

On a fixed finite Euler prefix, bounded initial operator norms and
bounded \(\|M_{1,0}\|_n\) give bounds on all field norms and
on the ordinary Frobenius norms of the learned increments by
finite induction in (40). Each matrix increment has Frobenius norm
equal to the product of its two factors' RMS norms times its step
size. These bounds can depend on the fixed prefix; no mesh-uniform
response estimate is used. The energy bound gives corresponding
bounds for an exact scalar gradient path on a bounded target interval.
In particular \(\|A_s-A_0\|_F,\|B_s-B_0\|_F\) and current operator
norms are bounded at each Euler node \(s\). Therefore
\[
\|B_sA_s-B_0A_0\|_F
\le\|B_s-B_0\|_F\|A_s\|_{\rm op}
  +\|B_0\|_{\rm op}\|A_s-A_0\|_F
\]
is bounded as well. Applying (41) to the two difference matrices gives
\[
\|(A_s-A_0)D_0\|_n\longrightarrow0,\qquad
\|(B_sA_s-B_0A_0)D_0\|_n\longrightarrow0                 \tag{42}
\]
in probability, on the usual bounded-initial-operator events.
These events and the scalar-training bounds can be taken
\(\mathscr F_n\)-measurable, so conditioning is legitimate.
Pass these identities through the deterministic fixed-program law.
They state exact zero action of each learned difference on the
contrast root in the population Euler program.

At initialization \(D_0,A_0D_0,B_0A_0D_0\) have deterministic
same-layer Gaussian limits of variance \(v_D\). For example,
conditional on \(D_0\), the coordinates of \(A_0D_0\) are independent
centered Gaussians of variance \(\|D_0\|_n^2\); this variance converges
to \(v_D\). Conditional on \(A_0D_0\), the same argument applies to
the independent \(B_0\). Combining with (42), the contrast field in
each layer equals its initial field in every population Euler prefix.
Strong Euler convergence on the affine interval, already justified
by its polynomial gradient, preserves that equality at every time.
In particular its variance remains \(v_D\).

One must also check covariance with the common field. For
\(\mathscr F_n\)-measurable \(q_n\), \(P_n\), with bounded
\(\|q_n\|_n\) and \(\|P_n\|_{\rm op}\),
\[
\mathbb E[\langle q_n,P_nD_0\rangle_n\mid\mathscr F_n]=0,
\]
\[
\mathbb E[\langle q_n,P_nD_0\rangle_n^2\mid\mathscr F_n]
=\frac{v_D}{n^2}\|P_n^Tq_n\|_2^2
\le\frac{v_D}{n}\|P_n\|_{\rm op}^2\|q_n\|_n^2.            \tag{43}
\]
Take \(P_n=I,A_s,B_sA_s\), and \(q_n={\bf1}\) or the
corresponding \(M_\ell(s)\). Fixed-program convergence proves zero
contrast mean and zero common--contrast covariance at every
population Euler node. Strong Euler convergence and continuity of
inner products preserve them on the full affine interval. Therefore
\[
\operatorname{Var}(z_a^{(\ell)}(s))
=\operatorname{Var}(M_\ell(s))+v_D\ge v_D
=\frac{1-\rho}{2}>0                                     \tag{44}
\]
on the whole affine interval.

In particular, the proposed same-label argument is sound after
specifying scalar training, conditional independence, and the
normalization (41). HS boundedness without that independence would
not suffice: a learned rank-one operator built from the contrast
itself could have a nonvanishing action on it. No assertion here
makes the Gaussian initial actions independent of the training path.

### Gaussianity and the arctangent affine-approximation error

Positive variance by itself would not ensure positive best affine
approximation error: a two-point law would be a counterexample.
The affine baseline also has Gaussian preactivation laws, as can
be justified at the finite-program level.

At each finite population Euler prefix for the affine model, every
forward, backward, or evolving vector field is an affine function
of finitely many jointly Gaussian source coordinates in its layer.
To see the induction, all
coordinate activation and gate operations are affine or constant.
After unrolling a trained matrix into its initial action plus
rank-one updates, each learned contribution is a previous coordinate
times a deterministic population contraction. A new initial-matrix
call, by the finite Gaussian-conditioning dependency, is a Gaussian
innovation plus response terms that are linear combinations of
previous coordinates with deterministic coefficients. No product
of two varying same-neuron coordinates is needed outside a scalar
population contraction. This proves the induction, allowing
singular Gaussian source covariances.

Bounded-interval strong Euler convergence for the polynomial affine
gradient passes these joint Gaussian laws and their second moments
to the exact affine path. A strong \(L^2\) limit of Gaussian vectors
is Gaussian: its means and covariances converge, and their Gaussian
characteristic functions converge to that of the limiting vector.
Thus each \(z_a^{(\ell)}(s)\) is Gaussian. Equations (39) and (44)
make its variance uniformly positive on \([0,S_b]\).

For a square-integrable real variable \(Z\) of positive variance,
define
\[
\mathcal R(Z)=\inf_{\alpha,\beta\in\mathbb R}
 \mathbb E[\arctan Z-\alpha-\beta Z]^2
=\operatorname{Var}(\arctan Z)
 -\frac{\operatorname{Cov}(Z,\arctan Z)^2}{\operatorname{Var}(Z)}.
                                                               \tag{45}
\]
The equality follows by first minimizing over the intercept to center
both variables, then minimizing the quadratic in the slope.
For a nondegenerate Gaussian \(Z\), \(\mathcal R(Z)>0\):
a zero minimum would say that \(\arctan z\) equals one affine
function Gaussian-almost everywhere. Positive density and continuity
would extend that identity to every real \(z\), contrary to the
nonconstant derivative \(1/(1+z^2)\).

The variance and covariance in (45) are continuous under strong
\(L^2\) convergence; here \(\arctan\) is bounded and Lipschitz.
The denominators are bounded below by (39) or (44).
Strong time continuity and compactness therefore give
\[
\eta_b:=\min_{a,\ell,\,0\le s\le S_b}
                 \mathcal R(z_{a,\mathrm{aff}}^{(\ell)}(s))>0,
                                                               \tag{46}
\]
Here \(z_{a,\mathrm{aff}}^{(\ell)}\) denotes the affine baseline.

This supplies the baseline needed for a separately proved \(O(e)\)
comparison. Precisely, if the main argument constructs a nonlinear
path on this same interval and proves
\[
\sup_{a,\ell,s\le S_b}
 \|z_{a,e}^{(\ell)}(s)-z_{a,\mathrm{aff}}^{(\ell)}(s)\|_2\le K|e|,
                                                               \tag{47}
\]
then all second moments remain bounded. Standard deviation is
1-Lipschitz under \(L^2\) distance, because it is the norm of the
orthogonal projection onto the mean-zero subspace. Thus (47)
preserves a positive variance lower bound for sufficiently small
fixed \(|e|\). Boundedness and Lipschitzness of arctangent give
\(O(|e|)\) changes in each variance and covariance in (45);
its denominator stays bounded away from zero. Consequently
\[
\inf_{a,\ell,s\le S_b}\mathcal R(z_{a,e}^{(\ell)}(s))
\ge\eta_b/2
\]
for sufficiently small fixed \(|e|\). Also
\[
\inf_{\alpha,\beta}
 \mathbb E[\phi_e(Z)-\alpha-\beta Z]^2
=e^2\mathcal R(Z),                                       \tag{48}
\]
by absorbing \(1+Z\) into the free affine coefficients and rescaling
them (the equality is also valid at \(e=0\)).

Equations (46)--(48) are a conditional transfer statement. They
neither prove the nonlinear state comparison (47) nor control its
response recursion. Likewise a separately proved \(O(e)\) output
comparison at \(S_b\) would preserve a positive margin above \(g=1\).
The fixed affine interval through \(1+\gamma\), its positive hidden
variances, and its positive arctangent approximation error have been
established here.

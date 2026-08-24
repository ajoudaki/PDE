# Three-hidden-layer arctangent: exact operator IDE and theorem reduction

Status: exact C0--C2 and fixed-mesh C4; the unconditional C3--C6 theorem is
not asserted in this document.  The remaining probabilistic lemma is isolated
in Section 8.  The reconciled multi-route verdict is in
[`FINAL_CONVERGENCE_AUDIT.md`](FINAL_CONVERGENCE_AUDIT.md).

## 1. Natural coordinate and finite equations

Write

\[
 \Theta(u)=u+u^3/3,\qquad r=\Theta(u),\qquad
 \iota(r)=2\sinh\!\left\{\tfrac13\operatorname{arsinh}(3r/2)\right\},
\]

and set

\[
 \Psi(r)=\arctan\iota(r),\qquad c(r)=(1+\iota(r)^2)^{-1},
 \qquad d(z)=(1+z^2)^{-1}.
\]

Then \(\Psi'(r)=c(r)^2\).  On the normalized spaces
\(H_{j,n}=(\mathbb R^n,n^{-1}x^{\mathsf T}y)\), define

\[
\begin{aligned}
 X_1&=\Psi(r),& Z_2&=G_1X_1,&X_2&=\arctan Z_2,\\
 Z_3&=G_2X_2,&X_3&=\arctan Z_3,&f_n&=\langle A,X_3\rangle_n,\\
 B_3&=A d(Z_3),&R_2&=G_2^*B_3,&B_2&=d(Z_2)R_2,\\
 Q_1&=G_1^*B_2.&&&&
\end{aligned}                                                    \tag{1.1}
\]

With \((b\otimes x)v=b\langle x,v\rangle_n=n^{-1}bx^{\mathsf T}v\),
feature ascent is exactly

\[
 \boxed{A'=X_3,\quad r'=Q_1,\quad
 G_1'=B_2\otimes X_1,\quad G_2'=B_3\otimes X_2.}       \tag{1.2}
\]

The transformed equation is not Euclidean gradient ascent in \(r\): it is
the exact change of variables from \(u'=c(r)Q_1\), since
\(\Theta'(u)=1/c(r)\).

Direct differentiation gives

\[
 \boxed{
 K_n=f_n'
 =\|X_3\|_2^2+\|B_3\|_2^2\|X_2\|_2^2
  +\|B_2\|_2^2\|X_1\|_2^2+\|c(r)Q_1\|_2^2.}          \tag{1.3}
\]

All four terms are squared parameter-gradient norms in the declared mixed
metric.  The identities are also checked by the finite central-difference
test in `test_finite_identities.py`.

## 2. Immutable joint source

Use three probability Hilbert spaces \(H_j=L^2(\Omega_j)\), the endpoint
marks

\[
 a_0\in H_3,\qquad r_0=u_0+u_0^3/3\in H_1,
\]

and two independent pointed Gaussian actions

\[
 \Gamma_1:H_1\to H_2,\qquad \Gamma_2:H_2\to H_3.       \tag{2.1}
\]

The source is the deterministic master law of every fixed finite,
three-sorted program built from \(a_0,r_0,\Gamma_1,\Gamma_1^*,\Gamma_2,\Gamma_2^*\),
coordinatewise pseudo-Lipschitz maps, and normalized moments.  Simultaneous
projective realization on a countable program language gives genuine bounded
Hilbert operators with

\[
 \|\Gamma_1\|_{\rm op},\|\Gamma_2\|_{\rm op}\le2,
 \qquad \Gamma_j^\dagger=\Gamma_j^*.                  \tag{2.2}
\]

The adjoints are part of the same realized source; neither transpose is
replaced by a fresh Gaussian action.  The usual spectral-norm theorem is
needed in addition to empirical program convergence to extend the actions
from the dense program domains to all of \(H_j\).

## 3. Exact autonomous IDE

The current state is

\[
 (A,r,P_1,P_2)\in H_3\times H_1\times
 \mathfrak S_1(H_1,H_2)\times\mathfrak S_1(H_2,H_3).   \tag{3.1}
\]

Put \(G_j=\Gamma_j+P_j\), form all fields by (1.1), and solve

\[
 \boxed{
 \begin{aligned}
 A'&=X_3,&r'&=Q_1,\\
 P_1'&=B_2\otimes X_1,&P_2'&=B_3\otimes X_2.
 \end{aligned}}                                       \tag{3.2}
\]

Equivalently, \(P_j\) is the trace-norm Bochner integral of its displayed
current rank-one velocity.  There are two current vectors and two current
operators, regardless of elapsed time or requested accuracy.  The integral
is stored extensionally as the present operator; its rank-one creation times
are not accessible to the future vector field.

The system has one time coordinate, is autonomous, and restarts from the
present quadruple with the same immutable source.  It contains no response
kernel, covariance kernel, second time, path measure, or growing collection
of state species.

## 4. Direct physical-time system

Adjoin the residual \(e\) and multiply the four feature velocities by
\(2\eta e\):

\[
 \boxed{
 \begin{aligned}
 \dot A&=2\eta eX_3,&\dot r&=2\eta eQ_1,\\
 \dot P_1&=2\eta eB_2\otimes X_1,&
 \dot P_2&=2\eta eB_3\otimes X_2,\\
 \dot e&=-2\eta eK.
 \end{aligned}}                                       \tag{4.1}
\]

The present-state readouts are

\[
 f=\langle A,X_3\rangle,\qquad K\text{ from (1.3)},
 \qquad \mathcal L=e^2.                               \tag{4.2}
\]

At the canonical independent centered initialization, \(f(0)=0\), so
\(e(0)=y_\star\).  Along any solution, \(f+e=y_\star\) and

\[
 \dot{\mathcal L}=-4\eta K\mathcal L.                 \tag{4.3}
\]

## 5. Dimension-free compact-time bounds

Let \(a=\pi/2\) and use \(S=|s|\).  Since every activation is bounded and
\(|B_3|\le|A|\),

\[
 \|A(s)\|_2\le \|a_0\|_2+aS,                         \tag{5.1}
\]

\[
 \|P_2(s)\|_1\le
 a\left(\|a_0\|_2S+\tfrac a2S^2\right).              \tag{5.2}
\]

Writing \(L_2(S)=\|\Gamma_2\|_{\rm op}+\sup_{|s|\le S}\|P_2(s)\|_1\),

\[
 \|B_2(s)\|_2\le L_2(S)(\|a_0\|_2+aS),              \tag{5.3}
\]

and therefore

\[
 \|P_1(s)\|_1\le
 a\int_0^S L_2(\sigma)(\|a_0\|_2+a\sigma)\,d\sigma. \tag{5.4}
\]

If \(L_1(S)=\|\Gamma_1\|_{\rm op}+\sup\|P_1\|_1\), then

\[
 \|Q_1(s)\|_2\le L_1(S)L_2(S)(\|a_0\|_2+aS),        \tag{5.5}
\]

which also bounds \(r\).  Finally,

\[
 0\le K\le a^2+a^2\|A\|_2^2+a^2L_2^2\|A\|_2^2
                 +L_1^2L_2^2\|A\|_2^2.              \tag{5.6}
\]

The same inequalities hold at finite width.  They exclude state escape and
make the feature velocity uniformly bounded in its natural Hilbert/trace
metric.  They do **not** by themselves exclude coordinate concentration.

## 6. Fixed meshes are finite source programs

At Euler step \(k\), exact elimination gives, for every current query \(v,w\),

\[
\begin{aligned}
G_1^kv&=\Gamma_1v+\sum_{m<k}hB_2^m\langle X_1^m,v\rangle,&
(G_1^k)^*w&=\Gamma_1^*w+\sum_{m<k}hX_1^m\langle B_2^m,w\rangle,\\
G_2^kv&=\Gamma_2v+\sum_{m<k}hB_3^m\langle X_2^m,v\rangle,&
(G_2^k)^*w&=\Gamma_2^*w+\sum_{m<k}hX_2^m\langle B_3^m,w\rangle.
\end{aligned}                                         \tag{6.1}
\]

Thus every fixed mesh is one finite, two-matrix, transpose-reusing source
program.  The master theorem identifies its full joint empirical laws and
all fixed polynomial moments.  This proves the width limit before mesh
removal; it does not authorize an increasing number of program steps.

## 7. Why bare \(L^2\) and finite lifts fail

The critical difference term is

\[
 d(Z_2)R_2-d(\widetilde Z_2)\widetilde R_2
 =d(Z_2)(R_2-\widetilde R_2)
 +\{d(Z_2)-d(\widetilde Z_2)\}\widetilde R_2.          \tag{7.1}
\]

Multiplication by an arbitrary \(L^2\) field is not continuous from \(L^2\)
to \(L^2\), so the second term is not locally Lipschitz on bare \(L^2\)
balls.  This is a real obstruction: a bounded-norm Householder construction
has \(K_n'(0)\asymp-\sqrt n\) and an order-one kernel change on an
\(n^{-1/2}\) interval.

Evolving \(B_2\), a log momentum, or the present Jacobian does not give a
finite bare-\(L^2\) repair.  The exact cotangent lift contains a term of the
form \(\kappa(Z_2)B_2^2\), while its Jacobian satisfies

\[
 \dot J=M_{\kappa(Z_3)\dot Z_3}J+\text{rank one}
       +J M_{\kappa(Z_2)\dot Z_2}.                    \tag{7.2}
\]

An \(L^2\) multiplier need not preserve Hilbert--Schmidt class.  Adding a
finite list of product fields only raises the highest multiplication word.

## 8. Exact remaining lemma

For \(X\) on a probability space, write

\[
 \|X\|_{\psi_1}=\inf\{C>0:\mathbb E e^{|X|/C}\le2\}.
\]

The following is the theorem-strength dependency left by all completed
routes.

### Middle-adjoint delocalization lemma

For every compact feature horizon \(S\), uniformly over the canonical
finite systems, their readout cutoffs, and the comparison Euler meshes,

\[
 \sup_{|s|\le S}\|R_{2,n}(s)\|_{\psi_1,n}=O_{\mathbb P,S}(1),            \tag{8.1}
\]

with the analogous bound in the pointed-action limit.  It is enough to
replace (8.1) by a moderate estimate

\[
 \|R_{2,n}(s)\|_{p,n}\le C_Sp
 \quad(2\le p\le c_S\log n),                            \tag{8.2}
\]

provided the associated exact-versus-mesh stability and limit uniqueness
are proved in the same reachable class.

The learned part is already safe:

\[
 P_2(s)^*B_3(s)=
 \int_0^s X_2(\sigma)
 \langle B_3(\sigma),B_3(s)\rangle\,d\sigma,            \tag{8.3}
\]

so only \(\Gamma_2^*B_3\) is difficult.  Removing one initial middle
column reduces it to a conditional Gaussian cavity term plus the signed
quadratic response

\[
 \int_0^1 n^{-1}g_j^{\mathsf T}R_{j,s}^{\lambda}g_j\,d\lambda.           \tag{8.4}
\]

Energy and spectral-norm estimates do not control (8.4); one Gaussian
integration by parts creates a directional Malliavin tangent with the same
multiplier and no remaining factor \(n^{-1/2}\).

### Conditional closure theorem

If (8.1), including its cutoff/mesh stability form, holds, then (3.2) is
globally well posed in the corresponding restart-stable reachable class and,
for every finite physical horizon \(T\),

\[
 \sup_{t\le T}\{|f_n-f|+|K_n-K|+|e_n-e|+|\mathcal L_n-\mathcal L|\}
 \xrightarrow{\mathbb P}0.                              \tag{8.5}
\]

Indeed \(\|R\|_{2p}\lesssim p\) and bounded interpolation give

\[
 \|R\{d(z)-d(\widetilde z)\}\|_2
 \le C\delta\log(e/\delta),                            \tag{8.6}
\]

where \(\delta=\|z-\widetilde z\|_2\).  This is an Osgood modulus.
Bihari's inequality supplies uniqueness, mesh removal, and cutoff stability.
Fixed-mesh program convergence then passes every derived field strongly in
\(L^2\), hence passes all four raw squared terms in (1.3).  Finally
\(|e|\) is nonincreasing and \(|s(t)|\le2\eta|y_\star|t\), so the scalar
clock transfers compact feature-time convergence to physical time.

The conditional theorem is a reduction, not a proof of (8.1).

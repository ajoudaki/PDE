# Exact discrete Abel collapse for the layer-3 predictor

## 1. Setup and hypotheses

Fix Euler indices \(k=0,\ldots,m\).  All products below are the normalized
Hilbert-space products used by the network.  Put

\[
 W_k:=\Gamma _2+P_2^k,\qquad x_k:=X_2^k,\qquad
 z_k:=Z_3^k=W_kx_k,
\]
\[
 a_k:=A^k,\qquad d_k:=d(z_k),\qquad b_k:=B_3^k=a_kd_k,
\]

where products involving \(a_k,d_k\) are componentwise.  Let

\[
 D_k:=Dd(z_k,z_{k+1}),\qquad M_k:=\operatorname{diag}(a_kD_k).
\]

The Euler updates used in the calculation are

\[
 W_{k+1}=W_k+h\,b_k\otimes x_k,\qquad
 a_{k+1}=a_k+hX_3^k,
\]

and \(hV_2^k=x_{k+1}-x_k\).  Define

\[
 \rho_k:=\langle x_k,x_{k+1}\rangle .
\]

Then the rank-one update gives the exact identity

\[
 W_kx_{k+1}=z_{k+1}-h\rho_kb_k,                     \tag{1}
\]

and hence

\[
 hW_kV_2^k=z_{k+1}-z_k-h\rho_kb_k.                  \tag{2}
\]

Let \(\mathcal G_k\) be the row-space Gaussian first-chaos subspace generated
by the canonical forward innovations through time \(k\), let
\(\mathcal X_k\) be its paired feature-history space, and let
\(U_k:\mathcal G_k\to\mathcal X_k\) be the canonical isometry.  Write

\[
 T_k:=U_k\Pi_{\mathcal G_k}.
\]

The only structural property needed for the telescoping argument is extension
consistency on old backward histories:

\[
 T_{k+1}v=T_kv\quad\text{for every }v\in\mathcal H_k^B,       \tag{EC}
\]

where \(\mathcal H_k^B=\operatorname{span}\{b_0,\ldots,b_k\}\) is the old
backward-history space.  In particular, \((T_{k+1}-T_k)b_k=0\).

For the canonical construction, (EC) is not an estimate.  Let
\(\gamma_1,\ldots,\gamma_r\) be the old orthonormal Gaussian innovations and
\(e_1,\ldots,e_r\) their paired orthonormal feature directions, so that
\(U_k\gamma_\ell=e_\ell\).  The new two-sided Gaussian residual is constructed
in \((\mathcal H_k^B)^\perp\); hence its normalized direction
\(\gamma_{r+1}\) satisfies

\[
 \langle\gamma_{r+1},v\rangle=0
 \quad(v\in\mathcal H_k^B).                          \tag{EC1}
\]

Adjoining the new pair preserves \(U_k\gamma_\ell=e_\ell\) for
\(\ell\le r\) and only defines
\(U_{k+1}\gamma_{r+1}=e_{r+1}\).  Therefore, for
\(v\in\mathcal H_k^B\), (EC1) gives

\[
 U_{k+1}\Pi_{\mathcal G_{k+1}}v
 =U_k\Pi_{\mathcal G_k}v,
\]

which is (EC).  If the new residual is zero, the first-chaos space does not
increase and the same identity is immediate from the Moore--Penrose/canonical
definition.

## 2. Direct collapse of the curvature block

For any scalar \(a,b\), with \(d(s)=(1+s^2)^{-1}\),

\[
 Dd(a,b)= -\frac{a+b}{(1+a^2)(1+b^2)},              \tag{3}
\]

with the same value at \(a=b\) by continuity.  The proof below needs only the
divided-difference identity

\[
 Dd(a,b)(b-a)=d(b)-d(a).                             \tag{4}
\]

Using (2) and (4), componentwise,

\[
 \begin{aligned}
 hM_kW_kV_2^k
 &=a_kD_k(z_{k+1}-z_k-h\rho_kb_k)\\
 &=a_k(d_{k+1}-d_k)-h\rho_k a_kD_kb_k.              \tag{5}
 \end{aligned}
\]

The last term in (5) cancels exactly with the \(+\rho_kb_k\) term in the
stated formula for \(F_3^k\).  Adding the source caused by the update of
\(A\) gives

\[
 \begin{aligned}
 hF_3^k
 &=hX_3^kd_{k+1}+a_k(d_{k+1}-d_k)\\
 &=(a_k+hX_3^k)d_{k+1}-a_kd_k\\
 &=b_{k+1}-b_k.                                      \tag{6}
 \end{aligned}
\]

Thus the factor containing \(W_kV_2^k\), including every covariance/rank-one
correction, leaves no predictor-amplitude remainder at all.

## 3. Abel form and cancellation of transfer variation

For completeness, Abel summation applied before the cancellation reads

\[
 S_{\rm open}:=\sum_{k=0}^{m-1}T_{k+1}M_kW_k(x_{k+1}-x_k).
\]

Using (1) at both endpoints of each summand gives exactly

\[
\begin{aligned}
S_{\rm open}
={}&T_mM_{m-1}z_m-T_1M_0z_0\\
&-\sum_{k=1}^{m-1}(T_{k+1}M_k-T_kM_{k-1})z_k\\
&-\sum_{k=0}^{m-1}h\rho_kT_{k+1}M_kb_k.             \tag{7}
\end{aligned}
\]

The final line is precisely the negative of the explicit \(\rho_kb_k\)
curvature contribution.  Adding that contribution and the source term is
equivalently, by (6),

\[
 \begin{aligned}
 \sum_{k=0}^{m-1}T_{k+1}(b_{k+1}-b_k)
 ={}&T_mb_m-T_1b_0\\
 &-\sum_{k=1}^{m-1}(T_{k+1}-T_k)b_k.                \tag{8}
 \end{aligned}
\]

Every term in the last sum vanishes by (EC).  Consequently

\[
 \sum_{k=0}^{m-1}hT_{k+1}F_3^k=T_mb_m-T_1b_0.       \tag{9}
\]

Equivalently, if \(P_{\rm stat}^k=T_kb_k\), then

\[
 P_{\rm stat}^{k+1}-P_{\rm stat}^k=hT_{k+1}F_3^k,
\]

and (9) is its exact telescoping form.

## 4. What this proves, and what it does not

There is no need to prove that
\(T_{k+1}M_kW_k\) has bounded variation.  In fact such a statement is false
in general: extension consistency controls \(T_{k+1}-T_k\) only on the old
backward-history space.  A new residual of size \(h\) costs only order
\(h^2/h=h\) in the Euler energy while its normalized canonical direction may
change by order one.  Hence energy alone cannot control the off-history total
variation of \(T_k\).

The exact cancellation avoids that false estimate.  It leaves the genuine
problem

\[
 P_{\rm stat}^m=T_mb_m.                              \tag{10}
\]

The isometric/canonical construction and Bessel give the a priori normalized
\(L^2\) bound for (10), but they do not by themselves give a coordinatewise
\(\psi_1\) bound.  Such a bound must use the conditional Gaussian law and
causal square-function/BMO control of the successive new canonical directions
along the actual Euler orbit.  It cannot follow from deterministic total
variation of \(T\).

## 5. First obstruction to an energy-only response square function

The exact Abel collapse does not imply that a Malliavin/response square
function is controlled by the base-orbit energy.  The first term that obstructs
that inference occurs one layer lower and is an off-diagonal commutator, not
the diagonal arctangent curvature.

To display it in continuous notation, suppress only the inessential insertion
map in the first layer and set

\[
 D_1:=\operatorname{diag}d(u),\qquad
 D_2:=\operatorname{diag}d(z_2),\qquad
 W_1:=\Gamma_1+P_1.
\]

The stated updates give

\[
 \dot z_2=K D_2R_2,\qquad
 K:=\rho_1I+W_1D_1W_1^*,                            \tag{11}
\]

where \(\rho_1=\langle X_1,X_1\rangle\).  Let \(\delta z_2\) be a response
and put \(\eta_i:=\delta z_{2,i}/d_i\).  Differentiating (11), using
\(\delta z_i=d_i\eta_i\), and subtracting
\(d_i'\dot z_i\eta_i\) from the left side gives

\[
\begin{aligned}
\dot\eta_i={}&(D_2^{-1}\delta K D_2R_2)_i
 +(D_2^{-1}KD_2\delta R_2)_i\\
&+\sum_{j\ne i}K_{ij}\frac{d_j}{d_i}R_{2,j}
       (d_j'\eta_j-d_i'\eta_i).                     \tag{12}
\end{aligned}
\]

Indeed, before cancellation the curvature part is

\[
 \frac1{d_i}\sum_jK_{ij}R_{2,j}d_j'd_j\eta_j
 -\frac{d_i'}{d_i^2}\Big(\sum_jK_{ij}d_jR_{2,j}\Big)d_i\eta_i.
\]

The \(j=i\) summands cancel exactly.  Combining the remaining summands yields
the last line of (12).  Therefore scalar characteristic dressing removes the
entire diagonal multiplier, but it does not remove the off-diagonal
commutator.  Since \(R_2\) contains the layer-2 predictable response, (12) is
the first algebraic location where its amplitude survives as a multiplier.

This obstruction is reachable by the exact state equations and can be large
while the base velocity is small.  For example, take a two-dimensional second
layer and a one-dimensional first layer.  Fix a vector \(z=(1,2)^*\), let
\(X_1=\varepsilon\), and choose \(W_1=z/\varepsilon\), so that
\(W_1X_1=z\).  Up to the harmless positive scalar \(d(u)\),

\[
 K=\varepsilon^2I+\varepsilon^{-2}zz^*.
\]

Let \(q=(2,-1)^*\), so \(z^*q=0\), and prescribe
\(D_2R_2=Lq\), \(\varepsilon=L^{-1}\).  Then

\[
 \dot z_2=KD_2R_2=L^{-1}q,
\]

while \(W_1^*D_2R_2=0\), and
\(\dot W_1=D_2R_2\otimes X_1=q\) is order one.  Thus neither the state
velocity nor the parameter energy sees a large quantity.  On the other hand,
for a response with \(\eta=(1,0)^*\), the rank-one part of the last line in
(12) has magnitude comparable to \(L^3\), because \(d'(1)\ne0\).  The same
statement holds on an open neighborhood of these data.  Ginibre matrices and
the Gaussian top endpoint have full support, so such finite-dimensional states
and response directions are reachable with positive probability along a
finite Euler history.

This example does **not** disprove a \(\psi_1\) bound for the bounded endpoint
transfer (10).  It proves the narrower but decisive point that its BMO square
function cannot be bounded using only the base energy and the size \(h\) of
the Euler increments.  A successful proof must find an additional signed
cancellation of (12) after taking the actual canonical trace/projection, or
use conditional Gaussian averaging of its off-diagonal part.  Taking an
operator norm or absolute total variation at (12) necessarily loses the
desired tail class.

## 6. A conditional random-bracket continuation lemma

The following lemma records exactly what remains sufficient for an
arbitrary-time \(\psi_1\) continuation.  It deliberately uses a random
quadratic-variation bound; an essential-supremum BMO bound is unnecessary and
would be false in the presence of the Gaussian endpoint.

**Lemma.**  Let \((M_k,\mathcal F_k)_{k\le m}\) be a real martingale and let
\(V_m=\sum_{k<m}\Delta V_k\), with each \(\Delta V_k\ge0\) predictable.  Assume

\[
 \mathbf E[\exp(\lambda\Delta M_k)\mid\mathcal F_k]
 \le \exp(\lambda^2\Delta V_k/2)                    \tag{13}
\]

for both signs of every real \(\lambda\).  Suppose also that, for some
nonnegative \(G\),

\[
 V_m\le C_T(1+G),\qquad
 \mathbf E e^{sG}<\infty\quad\hbox{for every }s>0.  \tag{14}
\]

Then \(M_m-M_0\in\psi_1\).  More precisely, for every fixed \(\lambda>0\),

\[
 \mathbf E e^{\lambda|M_m-M_0|}
 \le 2\{\mathbf E e^{2\lambda^2V_m}\}^{1/2}<\infty. \tag{15}
\]

If in addition a predictable finite-variation term \(D_m\) satisfies
\(|D_m|\le C_T(1+G)\), then \(M_m+D_m\in\psi_1\) as well.

*Proof.*  Iterating (13) shows that

\[
 \mathbf E\exp\{\theta(M_m-M_0)-\theta^2V_m/2\}\le1
\]

for every real \(\theta\).  With \(\theta=2\lambda\), Cauchy--Schwarz gives

\[
\begin{aligned}
 \mathbf E e^{\lambda(M_m-M_0)}
 &=\mathbf E\left[
   e^{\lambda(M_m-M_0)-\lambda^2V_m}
   e^{\lambda^2V_m}\right]\\
 &\le
 \{\mathbf E e^{2\lambda(M_m-M_0)-2\lambda^2V_m}\}^{1/2}
 \{\mathbf E e^{2\lambda^2V_m}\}^{1/2}\\
 &\le \{\mathbf E e^{2\lambda^2V_m}\}^{1/2}.
\end{aligned}
\]

Apply the same calculation to \(-M\) and use
\(e^{\lambda|x|}\le e^{\lambda x}+e^{-\lambda x}\).  Assumption (14) makes
the last expectation finite and proves (15).  The assertion about \(D_m\)
follows from \(|M_m+D_m|\le|M_m|+C_T(1+G)\) and one more
Cauchy--Schwarz inequality.  This proves the lemma.

For the network, the natural candidate is

\[
 G=\|A^0\|+T,
\]

whose normalized Gaussian norm has exponential moments of every linear
order, uniformly in the width.  The continuous signed energy identity is

\[
\begin{aligned}
 \frac{d}{dt}\langle A,X_3\rangle
 ={}&\|X_3\|^2+\rho_2\|B_3\|^2
       +\rho_1\|B_2\|^2+\langle Q_1,D_1Q_1\rangle . \tag{16}
\end{aligned}
\]

To verify (16), differentiate the output.  The \(A\)-update gives
\(\|X_3\|^2\).  Next,

\[
 \langle B_3,\dot Z_3\rangle
 =\rho_2\|B_3\|^2+\langle R_2,\dot X_2\rangle.
\]

Since \(\dot X_2=D_2\dot Z_2\) and \(B_2=D_2R_2\),

\[
 \langle R_2,\dot X_2\rangle
 =\langle B_2,\dot Z_2\rangle
 =\rho_1\|B_2\|^2+\langle Q_1,D_1Q_1\rangle.
\]

This proves (16).  Because \(X_3\) is bounded and
\(A(t)=A^0+\int_0^tX_3(s)\,ds\), integration yields

\[
 \int_0^T\!\left(
 \rho_2\|B_3\|^2+\rho_1\|B_2\|^2+
 \langle Q_1,D_1Q_1\rangle\right)dt
 \le C_T(1+\|A^0\|).                               \tag{17}
\]

Consequently, an exact canonical decomposition satisfying (13) with
\(V_m\) bounded by the discrete analogue of the left side of (17), plus an
\(h\)-summable remainder obeying the same bound, would prove the desired
arbitrary-time \(\psi_1\) estimate immediately by the lemma.  Establishing
that canonical bracket inequality for the *signed trace/projection* is the
remaining network-specific obligation.  Formula (12) shows why it cannot be
replaced by an operator-response or absolute-variation bound.

# Coupled even-channel estimates at a fixed finite angle

Status: new conditional actual-network identities and a priori estimates;
the universal population/GF/exact-GD theorem remains open. The primal
even-channel estimate below closes on every already constructed symmetric
physical-time branch. The linear-response estimate has three explicitly
identified, unclosed, gate-weighted product residuals. Neither statement
constructs the uncut population branch by assuming its existence.

I read solve-math-rigorously at `/etc/codex/skills/solve-math-rigorously/SKILL.md`
in full, and read CONTRACT.md, DATA_DEPENDENT_CONSTANTS_CLARIFICATION.md,
TANGENT_EVEN_CHANNEL_FOLLOWUP.md, UNIVERSAL_ANGLE_ROUTE.md, and
QUARTIC_FLAT_GATE_RESPONSE.md in full. This note uses no experiments,
agents, or external theorem beyond the elementary differential and
integral arguments supplied below. Only this new file is written.

The route is to retain the finite angle, use physical loss dissipation,
and split the trained operators by exchange parity. This exposes a
contribution of order e squared from the trained even operators to the incoming common
adjoints. A separate quartic identity cancels the top signed curvature
work against a weighted readout energy. Finally, differentiating the
whole network isolates the remaining response products without freezing
either operator orientation.

## 1. Fixed activation, scope, and physical normalization

Use the single activation
\[
 \phi(z)=1+z+e\mathcal A(z),\qquad
 \mathcal A(z)=\int_0^z\frac{dr}{1+r^4},\qquad e=1/10,
 \qquad L=1+e.
 \tag{1}
\]
No parameter in (1) depends on the data or any horizon or approximation.
For bookkeeping the formulas retain the symbol e. We use
\(|\mathcal A|\le4/3\), \(1\le\phi'\le L\), and
\(|\phi''|\le4e\). The first bound follows by integrating 1 on
[0,1] and r^{-4} on [1,infinity); the other two follow directly from
\(\phi'=1+e/(1+z^4)\) and
\(\phi''=-4ez^3/(1+z^4)^2\). This smooth activation is nonaffine
on every open interval. No layer is replaced by its affine part.

Fix opposite labels, taking their order to be (1,-1), and
\[
 \delta=\sqrt{(1-\rho)/2}\in(0,1],\qquad
 \mu=\sqrt{1-\delta^2}.
\]
The same-label case and the full nonlazy conclusion are not proved here.
Let \(\mathscr H_\ell=L^2(\Omega_\ell)\), with probability measures on three
separate populations, and let the exchange involutions give the
orthogonal decompositions
\(\mathscr H_\ell=\mathscr H_{\ell,e}\oplus\mathscr H_{\ell,o}\).
All norms of fields below are in these probability-normalized spaces.
For vectors f,g, \((f\otimes g)v=f\langle g,v\rangle\), and its
Hilbert-Schmidt norm is \(\|f\|_2\|g\|_2\).

Work on an already constructed strong symmetric branch with bounded
operators A,B, Hilbert-Schmidt trained increments, and the chain rule
and loss identity below. Its current operators intertwine the
involutions, so write \(A=A_e\oplus A_o\), \(B=B_e\oplus B_o\).
The common fields are even; normalized contrasts and C are odd.
This is the population symmetry of the specified initialization, not
an assertion of exact symmetry for an independently sampled finite
network. In particular, C(0)=0 is the prescribed population readout
limit; no finite-width initialization is changed.

Use coordinates U,V_1 for the first input plane, with
\(M_1=\mu U\). Omit U at \(\mu=0\). Their metric is
\(\|dU\|_2^2+\|dV_1\|_2^2\); both initial retained coordinates
have norm 1. With E_A=A-A_0 and E_B=B-B_0, the parameter displacement
metric is
\[
 \|d\Theta\|^2=\|dU\|_2^2+\|dV_1\|_2^2+
 \|dE_A\|_{\rm HS}^2+\|dE_B\|_{\rm HS}^2+\|dC\|_2^2.
 \tag{2}
\]
Frozen first-layer directions orthogonal to the input plane are omitted.

Define the exact finite-angle activation maps and gates by
\[
 h(M,V)=\frac{\phi(M+\delta V)+\phi(M-\delta V)}2,
 \quad k(M,V)=\frac{\phi(M+\delta V)-\phi(M-\delta V)}{2\delta},
\]
\[
 a(M,V)=\frac{\phi'(M+\delta V)+\phi'(M-\delta V)}2,
 \quad b(M,V)=\frac{\phi'(M+\delta V)-\phi'(M-\delta V)}{2\delta}.
 \tag{3}
\]
Subscripts denote layers, never paired neurons across layers. The
forward network is exactly
\[
 (M_2,V_2)=(A_eh_1,A_ok_1),\qquad
 (M_3,V_3)=(B_eh_2,B_ok_2),\qquad G=\langle C,k_3\rangle.
 \tag{4}
\]
Set \(g=\delta G\). On the symmetric branch, the two predictions are
(g,-g) and the contract's loss is \(\mathcal L=(1-g)^2\). Hence the
specified optimizer, in physical time, is
\[
 \dot\Theta=\lambda\nabla G,\qquad
 \lambda=2\delta(1-g).
 \tag{5}
\]
This factor, including its 2, follows by differentiating
\((1-\delta G)^2\) in metric (2).

On any interval where this branch exists,
\(\dot g=2\delta^2(1-g)\|\nabla G\|^2\). Solving this scalar
linear equation for 1-g, initially 1, shows
\(0\le g\le1\) and \(0\le\lambda\le2\delta\). Also
\[
 \frac{d\mathcal L}{dt}=-\|\dot\Theta\|^2,\qquad
 \int_0^t\|\dot\Theta\|^2dr\le1,\qquad
 \|\Theta(t)-\Theta(0)\|\le\sqrt t.
 \tag{6}
\]
The last inequality is the integral Cauchy-Schwarz inequality. Thus it
does not require a data-dependent smallness assumption on e.

## 2. Exact backward split and the bounded finite-angle gate

The differential of (3) is
\[
 dh=a\,dM+\delta^2b\,dV,\qquad dk=b\,dM+a\,dV.
\]
For incoming activation adjoints p,q define preactivation adjoints
\[
 P=ap+bq,\qquad Q=\delta^2bp+aq.
 \tag{7}
\]
These P,Q are adjoints, not the forward maps named P_delta,Q_delta in
UNIVERSAL_ANGLE_ROUTE.md. Their exact backward recursion is
\[
 p_3=0,\quad q_3=C,\quad P_3=b_3C,\quad Q_3=a_3C,
\]
\[
 p_2=B_e^*P_3,\quad q_2=B_o^*Q_3,\qquad
 p_1=A_e^*P_2,\quad q_1=A_o^*Q_2.
 \tag{8}
\]
Thus p,P are even, q,Q are odd. Differentiation in the raw parameters
gives the actual updates
\[
 \dot U=\lambda\mu P_1,\qquad \dot V_1=\lambda Q_1,
\]
\[
 \dot A_e=\lambda P_2\otimes h_1,\quad
 \dot A_o=\lambda Q_2\otimes k_1,\qquad
 \dot B_e=\lambda P_3\otimes h_2,\quad
 \dot B_o=\lambda Q_3\otimes k_2,\quad
 \dot C=\lambda k_3.
 \tag{9}
\]
The even and odd rank-one terms are orthogonal in the operator metric:
their Hilbert-Schmidt inner product is
\(\langle P,Q\rangle\langle h,k\rangle=0\).

The useful finite-angle observation is
\[
 1\le a\le L,\qquad |b|\le\beta:=\frac e{2\delta},\qquad
 \left\|\begin{pmatrix}a&\delta b\\\delta b&a\end{pmatrix}
 \right\|_{\mathbb R^2\to\mathbb R^2}\le L.
 \tag{10}
\]
Indeed the two eigenvalues are the two original activation derivatives.
The bound on b follows because each derivative lies in [1,1+e].
In particular, bq is an L2 field for every L2 q at fixed delta; no
product of q with an uncontrolled V is needed for this primal bound.

Fix T and assume \(\|A_0\|_{\rm op},\|B_0\|_{\rm op}\le K_0\),
where K_0>=1. Write
\[
 K=K_0+\sqrt T,\qquad
 H_1=1+\mu(1+\sqrt T)+4e/3,\qquad
 H_2=1+KH_1+4e/3.
 \tag{11}
\]
Equations (3),(4),(6) imply, throughout [0,T],
\[
 \|A\|_{\rm op},\|B\|_{\rm op}\le K,\quad
 \|C(t)\|_2\le\sqrt t,\quad \|h_1\|_2\le H_1,
 \quad\|h_2\|_2\le H_2,
\]
\[
 \|k_1\|_2\le L(1+\sqrt T),\qquad
 \|k_2\|_2\le KL^2(1+\sqrt T).
 \tag{12}
\]
Here h=1+M+e times a field bounded by 4/3, and
\(|k|\le L|V|\), which proves the two kinds of forward bounds.

Applying (10) to the pair (delta p,q), and then applying each block
operator, yields
\[
 \|Q_3\|_2\le L\|C\|_2,\quad
 \|q_2\|_2\le KL\|C\|_2,\quad
 \|Q_2\|_2\le KL^2\|C\|_2,\quad
 \|q_1\|_2\le K^2L^2\|C\|_2.
\]
Using (7),(8) again, now retaining the factor beta, gives
\[
 \|P_3\|_2\le\beta\|C\|_2,\quad
 \|p_2\|_2\le\beta K\|C\|_2,\quad
 \|P_2\|_2\le2\beta LK\|C\|_2,
\]
\[
 \|p_1\|_2\le2\beta LK^2\|C\|_2,\qquad
 \|P_1\|_2\le3\beta L^2K^2\|C\|_2.
 \tag{13}
\]
For example P_2 has the two terms a_2 B_e^*(b_3 C) and
b_2 B_o^*(a_3 C), each bounded by beta L K times the readout norm.
The next backward layer adds the third such contribution. All actions
in this calculation use the current, trained operators.

## 3. Integrated even energy and the frozen affine baseline

Let \(E_{A,e}=A_e-A_{0,e}\), \(E_{B,e}=B_e-B_{0,e}\).
Since \(\lambda\beta\le e\), (9),(12),(13) prove
\[
 \|\dot U\|_2\le3e\mu L^2K^2\sqrt t,\quad
 \|\dot E_{A,e}\|_{\rm HS}\le2eLKH_1\sqrt t,\quad
 \|\dot E_{B,e}\|_{\rm HS}\le eH_2\sqrt t.
 \tag{14}
\]
Thus the apparent inverse-angle gate coefficient cancels in physical
time. Define
\[
 S=9\mu^2L^4K^4+4L^2K^2H_1^2+H_2^2,
\]
\[
 Z_e(t)^2=\|U(t)-U_0\|_2^2+
 \|E_{A,e}(t)\|_{\rm HS}^2+\|E_{B,e}(t)\|_{\rm HS}^2,
\]
omitting the U term when mu=0. Integration of (14) gives
\[
 \int_0^T\big(\|\dot U\|_2^2+
 \|\dot E_{A,e}\|_{\rm HS}^2+
 \|\dot E_{B,e}\|_{\rm HS}^2\big)dt
 \le\min\{1,e^2ST^2/2\},
\]
\[
 \sup_{t\le T}Z_e(t)\le
 \min\{\sqrt T,(2/3)e\sqrt S\,T^{3/2}\}.
 \tag{15}
\]
The first alternative in each minimum follows from (6) and the
orthogonal parity decomposition. The second alternatives follow by
integrating t and sqrt(t), respectively. Individually, at t<=T,
\[
 \|E_{B,e}(t)\|_{\rm HS}\le(2/3)eH_2t^{3/2},\quad
 \|E_{A,e}(t)\|_{\rm HS}\le(4/3)eLKH_1t^{3/2},
\]
\[
 \|U(t)-U_0\|_2\le2e\mu L^2K^2t^{3/2}.
 \tag{16}
\]
These estimates are finite for the fixed choice e=.1 at every finite T.
They do not require e times a function of T to be small. Large bounds
do not justify a perturbative approximation; finiteness is the claim.

There is a corresponding comparison with the *frozen common fields*
of the affine baseline using the same initial operators:
\[
 M_1^{\rm aff}=\mu U_0,\quad
 M_2^{\rm aff}=A_{0,e}(1+M_1^{\rm aff}),\quad
 M_3^{\rm aff}=B_{0,e}(1+M_2^{\rm aff}).
\]
To see freezing directly, set e=0 in (7)--(9): p_3=P_3=0 propagates
to every p,P, so U,A_e,B_e are constant. No comparison of odd paths
is needed. For the nonlinear path write h_l=1+M_l+e j_l, with
\(|j_l|\le4/3\). Exact algebra, with current h_l, gives
\[
 M_2-M_2^{\rm aff}=E_{A,e}h_1+
 A_{0,e}(M_1-M_1^{\rm aff}+e j_1),
\]
\[
 M_3-M_3^{\rm aff}=E_{B,e}h_2+
 B_{0,e}(M_2-M_2^{\rm aff}+e j_2).
 \tag{17}
\]
Consequently, if \(d_l=\|M_l-M_l^{\rm aff}\|_2\),
\[
 d_1\le\mu\|U-U_0\|_2,\quad
 d_2\le H_1\|E_{A,e}\|_{\rm HS}+K_0(d_1+4e/3),\quad
 d_3\le H_2\|E_{B,e}\|_{\rm HS}+K_0(d_2+4e/3).
 \tag{18}
\]
The e terms include the nonlinear initial forward pass. They must not
be dropped by identifying the nonlinear and affine initial hidden
fields. Equations (16),(18) bound their full difference by e times an
explicit finite horizon-dependent expression.

## 4. Trained-even return is second order in e in physical time

Integrating the *actual* even update in (9), then taking its adjoint
against the current P, yields the causal identities
\[
 p_2(t)=B_{0,e}^*P_3(t)+
 \int_0^t\lambda(s)h_2(s)\langle P_3(s),P_3(t)\rangle ds,
\]
\[
 p_1(t)=A_{0,e}^*P_2(t)+
 \int_0^t\lambda(s)h_1(s)\langle P_2(s),P_2(t)\rangle ds.
 \tag{19}
\]
The integrals are Bochner integrals: (12),(13) bound the norms of
their integrands on a finite horizon. In particular these p's are
not arbitrary incoming common drivers. The scalar kernels
\(\sqrt{\lambda(s)\lambda(t)}\langle P_l(s),P_l(t)\rangle\)
are positive semidefinite: a finite quadratic form is the squared
norm of \(\sum_i c_i\sqrt{\lambda(t_i)}P_l(t_i)\).
This fact gives no pointwise sign for (19), because h_l varies.

Call the two integral terms p_2^{tr},p_1^{tr}. From their exact forms
\(p_2^{tr}=E_{B,e}^*P_3\), \(p_1^{tr}=E_{A,e}^*P_2\),
(13),(16) give
\[
 \lambda(t)\|p_2^{tr}(t)\|_2
 \le e\sqrt t\,\|E_{B,e}(t)\|_{\rm HS}
 \le(2/3)e^2H_2t^2,
\]
\[
 \lambda(t)\|p_1^{tr}(t)\|_2
 \le2eLK\sqrt t\,\|E_{A,e}(t)\|_{\rm HS}
 \le(8/3)e^2L^2K^2H_1t^2.
 \tag{20}
\]
Thus, in particular,
\[
 \int_0^T\lambda\|p_2^{tr}\|_2dt\le(2/9)e^2H_2T^3,
 \qquad
 \int_0^T\lambda\|p_1^{tr}\|_2dt
 \le(8/9)e^2L^2K^2H_1T^3.
 \tag{21}
\]
The complete incoming adjoints, including initialized-operator returns,
satisfy
\[
 \lambda\|p_2\|_2\le eK\sqrt t,\qquad
 \lambda\|p_1\|_2\le2eLK^2\sqrt t,
\]
\[
 \int_0^T\lambda^2\|p_2\|_2^2dt\le e^2K^2T^2/2,
 \quad
 \int_0^T\lambda^2\|p_1\|_2^2dt\le2e^2L^2K^4T^2.
 \tag{22}
\]
For p_1, the first return in (19) itself contains B_e inside P_2.
One can expose that additional trained even operator too. Keep every
gate, C, and the odd operator B_o at their actual current values, and set
\[
 p_1^{(0)}=A_{0,e}^*\left[
 a_2B_{0,e}^*(b_3C)+b_2B_o^*(a_3C)\right].
\]
Substituting P_2=a_2p_2+b_2q_2 gives the exact further decomposition
\[
 p_1-p_1^{(0)}=A_{0,e}^*(a_2p_2^{tr})+p_1^{tr}.
\]
Consequently the return through either explicitly trained even operator
satisfies the integrated bound
\[
 \int_0^T\lambda\|p_1-p_1^{(0)}\|_2dt
 \le\frac{2e^2T^3}{9}
 \left(K_0LH_2+4L^2K^2H_1\right).
 \tag{22a}
\]
This follows by multiplying (21)'s first bound by K_0 L and adding
its second bound. In this decomposition only the even operator actions
are replaced by their initialized actions. The field p_1^{(0)} is
evaluated on the nonlinear trajectory, so (22a) makes no assertion
that gate-selection feedback or its derivative has been controlled.
Both trained operator orientations remain in the actual equations.

## 5. All forward and backward operator-transport terms

The upper preactivations are not isolated local gate flows. Applying
(9) to their defining operator actions, and using h perpendicular to k,
gives the exact physical velocities
\[
 \dot M_1=\lambda\mu^2P_1,\qquad \dot V_1=\lambda Q_1,
\]
\[
 \dot M_2=\lambda\|h_1\|_2^2P_2+
 A_e(a_1\dot M_1+\delta^2b_1\dot V_1),
\]
\[
 \dot V_2=\lambda\|k_1\|_2^2Q_2+
 A_o(b_1\dot M_1+a_1\dot V_1),
\]
\[
 \dot M_3=\lambda\|h_2\|_2^2P_3+
 B_e(a_2\dot M_2+\delta^2b_2\dot V_2),
\]
\[
 \dot V_3=\lambda\|k_2\|_2^2Q_3+
 B_o(b_2\dot M_2+a_2\dot V_2).
 \tag{23}
\]
For example, the first term in dot M_2 is dot A_e h_1; it is
present even if the lower preactivation is momentarily stationary.

Differentiating (8) gives the backward counterparts
\[
 \dot p_2=\lambda h_2\|P_3\|_2^2+B_e^*\dot P_3,
 \qquad \dot q_2=\lambda k_2\|Q_3\|_2^2+B_o^*\dot Q_3,
\]
\[
 \dot p_1=\lambda h_1\|P_2\|_2^2+A_e^*\dot P_2,
 \qquad \dot q_1=\lambda k_1\|Q_2\|_2^2+A_o^*\dot Q_2.
 \tag{24}
\]
Here
\[
 \dot P_l=a_l\dot p_l+b_l\dot q_l+\dot a_l p_l+\dot b_l q_l,
 \quad
 \dot Q_l=\delta^2b_l\dot p_l+a_l\dot q_l+
 \delta^2\dot b_l p_l+\dot a_l q_l.
 \tag{25}
\]
At the top, \(\dot p_3=0\) and \(\dot q_3=\dot C\).
Identities involving differentiated gates are asserted where their
products are defined, as in finite dimension or under the response
integrability conditions below. The undifferentiated estimates
(13)--(22) do not require those additional products.

## 6. Quartic cancellation in a nonnegative top-even energy

There is also a cancellation specific to the finite-angle quartic
structure. Put D=delta V and define the smooth secant
\[
 s(M,D)=\frac12\int_{-1}^1\phi'(M+rD)dr\in[1,L].
\]
Thus k(M,V)=s(M,D)V, including V=0. Direct subtraction of the two
quartic gates gives
\[
 b(M,V)=-\frac{4eMV(M^2+D^2)}
 {[1+(M+D)^4][1+(M-D)^4]}.
\]
Define, with no division by M or V,
\[
 \omega(M,D)=\frac{4eM^2(M^2+D^2)}
 {[1+(M+D)^4][1+(M-D)^4]s(M,D)}.
 \tag{26}
\]
It satisfies the exact identity
\[
 M b(M,V)=-\omega(M,\delta V)k(M,V),\qquad
 0\le\omega\le2e.
 \tag{27}
\]
For the upper bound put x=M+D, y=M-D. Then
\(4M^2(M^2+D^2)=(x+y)^2(x^2+y^2)/2\), which is at most
\((x^2+y^2)^2\le2(x^4+y^4)\). The denominator without s is
at least x^4+y^4, and s>=1. The zero numerator case is included.

The first derivatives of omega are globally bounded. Indeed its
rational numerator divided by the two quartic denominators is a sum
of products \(x^i/(1+x^4)\,y^{4-i}/(1+y^4)\), 0<=i<=4.
Each factor and its first derivative is bounded, by inspection at
infinity and continuity on compact intervals. The integral formula
for s bounds its first derivatives using |phi''|<=4e; s>=1 permits
differentiation of 1/s. In particular the deterministic constant
\[
 c_e=\sup_{M,D}(|\partial_M\omega|+|\partial_D\omega|)<\infty
\]
is available for this fixed activation, independent of delta.

On the actual network define the nonnegative modulated energy
\[
 \mathcal E_B(t)=\|E_{B,e}(t)\|_{\rm HS}^2+
 \mathbb E_{\Omega_3}[\omega(M_3,\delta V_3)C^2].
 \tag{28}
\]
Where the time differentiation is integrable, (9) and
E_{B,e}h_2=M_3-B_{0,e}h_2 give
\[
 \frac d{dt}\|E_{B,e}\|_{\rm HS}^2
 =2\lambda\langle b_3C,M_3-B_{0,e}h_2\rangle
 =-2\langle\omega_3 C,\dot C\rangle
   -2\lambda\langle b_3C,B_{0,e}h_2\rangle.
\]
Differentiating the second term in (28) cancels the first displayed
term exactly. Therefore
\[
 \mathcal E_B(t)=
 -2\int_0^t\lambda\langle b_3C,B_{0,e}h_2\rangle dr
 +\int_0^t\mathbb E\left[
 C^2(\omega_M\dot M_3+\delta\omega_D\dot V_3)\right]dr.
 \tag{29}
\]
The initial energy is zero. No sign of C V_3 is assumed. No inverse
power of M occurs, and crossings of M_3=0 cause no singularity.
The remaining initialized-operator work is bounded in absolute value by
\[
 2eK_0H_2\int_0^t\sqrt r\,dr
 =(4/3)eK_0H_2t^{3/2}.
 \tag{30}
\]

The second integral in (29) is a genuine transport residual, with
dot M_3 and dot V_3 given by **all** the terms in (23). For example it
contains the contribution
\[
 \lambda\,\mathbb E\left[C^2\left(
 \omega_M\|h_2\|_2^2 b_3 C+
 \delta\omega_D\|k_2\|_2^2 a_3 C\right)\right]
\]
from training B itself, in addition to transport through the lower
layer and B. This contribution is not dropped or declared restoring.

One sufficient condition making (29) rigorous is
\(C\in L^4([0,T]\times\Omega_3)\). To see this, the forward
differential bounds in the next section give
\(\|\dot M_3\|_2+\|\dot V_3\|_2\le N_3\|\dot\Theta\|\).
Hölder in the population variable, then Cauchy-Schwarz in time and (6),
give the explicit residual estimate
\[
 \int_0^T\left|\mathbb E[C^2\dot\omega_3]\right|dt
 \le c_eN_3\left(\int_0^T\|C(t)\|_4^4dt\right)^{1/2}.
 \tag{31}
\]
Also \(\int|\mathbb E[\omega C\dot C]|\) is finite from bounded
omega and C,dot C in time-space L2. Pointwise absolute continuity,
these integrable derivatives, and Fubini justify integrating the
product rule in (29). This fourth-moment input is not proved by (6).
Identity (29) is an additional structural cancellation, not a stronger
unconditional bound than (15), and not by itself a response theorem.

## 7. Whole-network linear response with three explicit residual pairs

This section retains variations of both operator orientations. It
also permits variations that break exchange symmetry. All differential
identities hold in finite dimension; on a population branch they apply
to variations for which the displayed differentiations and products
exist. Establishing these hypotheses for the limiting source response
is part of the unclosed work.

Let \(\eta=(\eta_U,\eta_{V_1},\eta_A,\eta_B,\eta_C)\) be a
parameter variation in metric (2), and let xi_Ml,xi_Vl be the induced
preactivation variations. For l=1,
\(\xi_{M_1}=\mu\eta_U\), \(\xi_{V_1}=\eta_{V_1}\). Use full
operators for these possibly nonsymmetric variations:
\[
 \xi_{M_2}=\eta_Ah_1+A\,dh_1,\qquad
 \xi_{V_2}=\eta_Ak_1+A\,dk_1,
\]
\[
 \xi_{M_3}=\eta_Bh_2+B\,dh_2,\qquad
 \xi_{V_3}=\eta_Bk_2+B\,dk_2,
\]
\[
 dh_l=a_l\xi_{M_l}+\delta^2b_l\xi_{V_l},\qquad
 dk_l=b_l\xi_{M_l}+a_l\xi_{V_l}.
 \tag{32}
\]
Here dh,dk denote variation, not time differentiation. Both eta_A
and eta_B terms are necessary trained-operator response terms.

For explicit deterministic constants set
\[
 J=L+\beta,\quad N_1=2,\quad
 S_1=H_1+L(1+\sqrt T),\quad S_2=H_2+KL^2(1+\sqrt T),
\]
\[
 N_2=S_1+KJN_1,\qquad N_3=S_2+KJN_2.
 \tag{33}
\]
The two column sums of the absolute differential matrix in (3) are
at most J. Applying (32) inductively proves
\[
 \|\xi_{M_l}\|_2+\|\xi_{V_l}\|_2\le N_l\|\eta\|,
 \qquad \|dh_l\|_2+\|dk_l\|_2\le JN_l\|\eta\|.
 \tag{34}
\]
Taking eta=dot Theta also proves the velocity bound used in (31).

Set
\[
 c_l=\frac{\phi''(M_l+\delta V_l)+\phi''(M_l-\delta V_l)}2,
 \quad d_l^{\rm gate}=\frac{\phi''(M_l+\delta V_l)-\phi''(M_l-\delta V_l)}{2\delta}.
\]
The gate variations, with every delta factor retained, are
\[
 \alpha_l:=da_l=c_l\xi_{M_l}+\delta^2d_l^{\rm gate}\xi_{V_l},\qquad
 \gamma_l:=db_l=d_l^{\rm gate}\xi_{M_l}+c_l\xi_{V_l}.
\]
There are exactly three local residual pairs, one for each layer:
\[
 R^P_l=\alpha_l p_l+\gamma_l q_l,\qquad
 R^Q_l=\delta^2\gamma_l p_l+\alpha_l q_l.
 \tag{35}
\]
Their norms need not be controlled by the primal L2 energy. In
particular, with \(Z_l=|\xi_{M_l}|+\delta|\xi_{V_l}|\),
\[
 \|R^P_l\|_2+\|R^Q_l\|_2
 \le4e(1+\delta)\left\|
 Z_l\big(|p_l|+|q_l|/\delta\big)\right\|_2.
 \tag{36}
\]
Indeed |alpha|<=4e Z and |gamma|<=4e Z/delta, and the bounds for
R^P and R^Q differ by the factor delta. One can retain the exact
quartic coefficients \(c_l,d_l^{\rm gate}\) in (35) instead of using the coarser (36).

To expose the operator returns as well, the differentiated backward
recursion is, without suppressing any operator variation,
\[
 \widehat P_l=a_l\widehat p_l+b_l\widehat q_l+R^P_l,
 \quad
 \widehat Q_l=\delta^2b_l\widehat p_l+a_l\widehat q_l+R^Q_l,
 \quad \widehat p_3=0,\quad\widehat q_3=\eta_C,
\]
\[
 \widehat p_2=\eta_B^*P_3+B^*\widehat P_3,\quad
 \widehat q_2=\eta_B^*Q_3+B^*\widehat Q_3,
\]
\[
 \widehat p_1=\eta_A^*P_2+A^*\widehat P_2,\quad
 \widehat q_1=\eta_A^*Q_2+A^*\widehat Q_2.
 \tag{37}
\]
In particular, the contribution of the even feedback to its first
variation is obtained from
\[
 D(P_l\otimes h_{l-1})[\eta]
 =\widehat P_l\otimes h_{l-1}+P_l\otimes dh_{l-1}.
 \tag{38}
\]
For a nonsymmetric variation take the even output/input projections
in (38) when computing the even-to-even block. Differentiating the
odd rank-one term contributes zero to that block at the symmetric
base: its unchanged input or its unchanged output is odd. Bounds
(12),(13),(34),(37) control (38) by a finite constant times
\(\|\eta\|+\sum_l(\|R^P_l\|_2+\|R^Q_l\|_2)\).
The scalar loss-factor variation must also be included for a physical
velocity; it is included next.

Here is an integrated estimate for the full response, rather than only
the even component. Extend the definitions of h,k,G to nearby states
without imposing parity, and put F=<C,h_3>. Exactly
\[
 f_1=F+\delta G,\quad f_2=F-\delta G,\quad
 \mathcal L=F^2+(\delta G-1)^2.
\]
At the symmetric base F=0. For a source-forced linear response with
forcing j(t) in parameter metric (2), differentiation of the actual
loss flow gives
\[
 \dot\eta=\lambda D^2G\,\eta
 -2\delta^2\nabla G\,DG[\eta]-2\nabla F\,DF[\eta]+j.
 \tag{39}
\]
Both negative terms are retained, including the second one for a
symmetry-breaking source. The variation of lambda is
\(-2\delta^2DG[\eta]\).

Repeatedly differentiating the forward equations gives the exact
quadratic Hessian identity
\[
 D^2G[\eta,\eta]=2\langle\eta_C,dk_3\rangle
 +2\sum_{l=1}^2\left(
 \langle P_{l+1},\eta_{W_l}dh_l\rangle+
 \langle Q_{l+1},\eta_{W_l}dk_l\rangle\right)
\]
\[
 \hspace{25mm}
 +\sum_{l=1}^3\left(
 \langle\xi_{M_l},R^P_l\rangle+
 \langle\xi_{V_l},R^Q_l\rangle\right),
 \qquad W_1=A,\ W_2=B.
 \tag{40}
\]
For verification, the second differential of W h is
2 eta_W dh+W d^2h. Move the last term backward using W^* and
repeat at the preceding layer. At each activation the remaining
second differential paired with p,q is exactly the last line of
(40), by differentiating (7) with p,q held fixed. The first-layer
preactivation has zero second differential. This accounts for every
term, including all matrix transport; no Hessian term has been
discarded into an unspecified operator coefficient.

Write
\[
 D_2=K(2\beta L+L^2)\sqrt T,\qquad
 D_3=(\beta+L)\sqrt T,
 \quad H=2J(N_3+D_2N_1+D_3N_2),
\]
\[
 \mathcal R(t)=\sum_{l=1}^3N_l
 (\|R^P_l(t)\|_2+\|R^Q_l(t)\|_2).
 \tag{41}
\]
Equations (12),(13),(34) bound the absolute value of the first two
terms of (40) by H||eta||^2: for example
\(|\langle P_{l+1},\eta_{W_l}dh_l\rangle|
 \le\|P_{l+1}\|_2\|\eta_{W_l}\|_{\rm HS}\|dh_l\|_2\).
The last line is at most ||eta|| times mathcal R. Taking the inner
product of (39) with eta therefore proves
\[
 \frac12\frac d{dt}\|\eta\|^2
 +2\delta^2(DG[\eta])^2+2(DF[\eta])^2
 \le\lambda H\|\eta\|^2+
 \|\eta\|(\lambda\mathcal R+\|j\|).
 \tag{42}
\]
If \(\lambda\mathcal R\) and ||j|| are integrable, then
\[
 \sup_{t\le T}\|\eta(t)\|
 \le\exp(2\delta HT)\left[
 \|\eta(0)\|+\int_0^T(\lambda\mathcal R+\|j\|)dt\right].
 \tag{43}
\]
To justify the scalar step even when eta vanishes, use
\(r_\varepsilon=(\|\eta\|^2+\varepsilon^2)^{1/2}\) in (42).
It satisfies \(\dot r_\varepsilon\le\lambda H r_\varepsilon+
\lambda\mathcal R+\|j\|\). Multiply by
\(\exp(-H\int_0^t\lambda)\), integrate, use lambda<=2 delta,
and let epsilon decrease to zero. This proves (43) with the
stated hypotheses. It does not assume a driver-uniform propagator
bound or confuse a late source injection with an initial variation.

## 8. What is established, and what still has to close

The new unconditional a priori information *on a constructed symmetric
branch* is (15)--(22): integrated physical even energy, controlled
departure from the frozen affine common fields, and an explicit
part of the p-return of order e squared through trained even operators. These estimates
need only second moments, bounded initialized L2 operators, the fixed
finite angle, and physical loss dissipation. The trained odd blocks
can move freely within the energy bound. No optimizer or initialization
has been redesigned, and no all-layer motion conclusion is inferred
merely from allowing that motion.

The new quartic cancellation (29) is exact on integrable branches.
Its residual is the transport of the smooth bounded weight omega,
with all terms in (23) included. A single space-time fourth moment of
the actual readout suffices for its estimate (31). That moment is an
unclosed input; the ordinary energy does not establish it.

The whole-network response estimate (42),(43) leaves precisely the
three local gate-weighted response pairs (35). All differentiated
forward and backward matrix actions, the loss-factor variation, and
the response to a symmetry-breaking common prediction are present.
To close (43), one sufficient new estimate would be, on the actual
Gaussian population construction and its approximations,
\[
 \lambda(t)\mathcal R(t)\le a_{D,T}(t)\|\eta(t)\|+b(t),
 \qquad a_{D,T}\in L^1[0,T],
 \tag{44}
\]
with controlled source term b and constants uniform in the relevant
mesh, width, and auxiliary caps. In that event the same integrating
factor argument closes (43). No bound (44), no required source
moment theorem, and no population differentiability theorem is
claimed here. The p bounds (22) alone do not bound the products of
p,q with xi in (35). The exact quartic weights in (35) are available
for a stronger actual-network argument.

The estimates here have no cap or mesh parameter. They therefore
provide useful a priori inputs when a construction preserves their
equations and energy identity; they do not automatically apply to
an arbitrary clipping scheme, which may change those identities.
For exact GD, (6) is not an identity: one still needs a discrete
descent/remainder bound, and uniform source-response control for
passing the mesh limit. Finite-width asymmetry and the small nonzero
finite-width initial readout also need quantitative error estimates;
the symmetric population algebra is not substituted for those errors.

Constructing and continuing the uncut joint population flow, removing
all required caps/meshes, proving the full raw-kernel and restart
observables, and proving genuine nonlinear hidden motion remain open.
The same-label extension remains outside this calculation. These
unclosed implications are not a failure of the universal-activation
goal. In particular, no step here requires choosing e depending on
the dataset or the time horizon.

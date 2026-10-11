# Finite-time energy route for the unchanged Legendre closure

11 October 2026. Scoped author derivation. Inputs: the canonical setup in
`paper/compact.tex`, the actual construction and projection identities in
`paper/compact_legendre.tex`, `AUTONOMOUS_ONE_SAMPLE.md`, `AUTONOMOUS_SCOPE.md`,
and `ACTIVATION_UNIT_LABEL_FINITE_TIME.md` in the explicitly authorized earlier
study, and `docs/notation.qmd`. The canonical-notation and rigorous-mathematics
skills were read and applied. No experiments, external literature, other
studies, Git operations, or manuscript changes were used. The supervisor
supplied the exact readout identity in Section 3 during this derivation; its
algebra is verified below. This is an author result, not an independent review.

The direct energy argument proves something beyond the supplied joint-order
theorem: for arbitrary fixed labels and possibly unbounded activations, the
actual closure exists on every fixed finite horizon at a sufficient order
independent of width. Its accumulated absolute velocity defect is O(1/q), and
its total positive loss variation is O(1/q), on a single Gaussian event
independent of q. These statements do not establish width-uniform tracking of
dense predictions. The precise remaining stability and second-tail gaps are
identified below.

## 1. Setup and the unchanged construction

There are m normalized training inputs v_a=x_a/sqrt(d), with ||v_a||_2=1,
arbitrary labels y_a, width n, and L>=2 hidden layers. Write
Y=(m^{-1} sum_a y_a^2)^{1/2}. For every sphere query v=x/sqrt(d), ||v||_2=1,
the forward and backward recursions are

\[
 z^{(1)}(x)=W^{(1)}v,\qquad
 z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),\qquad
 h^{(\ell)}(x)=\phi_\ell(z^{(\ell)}(x)),\qquad
 f(x)=w^\top h^{(L)}(x)/n,
\]
\[
 r_a=f(x_a)-y_a,\qquad \rho^2=m^{-1}\sum_a r_a^2,
 \qquad k_a^{(L)}=w,
 \qquad k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)},
 \qquad\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)}.
\]

Each activation is real on the real axis, holomorphic in a fixed strip,
and has bounded first derivative there. Only the following weaker consequences
are needed for Sections 2--5:

\[
 b_\ell=|\phi_\ell(0)|<\infty,\qquad
 s_\ell=\sup_{u\in\mathbb R}|\phi_\ell'(u)|<\infty,
 \qquad \phi_\ell'\text{ is locally Lipschitz}.
\]

The canonical dense velocity F has blocks

\[
 F^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\qquad
 F^{(\ell)}=-\frac2{mn}\sum_a r_a\delta_a^{(\ell)}
                         h_a^{(\ell-1)\top}\quad(2\le\ell\le L),
 \qquad F_w=-\frac2m\sum_a r_a h_a^{(L)}.
 \tag{1}
\]

The zero-readout initialization is shared. For an increment U, its mobility
norm is defined by

\[
 \|U\|_{\rm par}^2=
 \frac{\|U^{(1)}\|_F^2}{n}
 +\sum_{\ell=2}^L\|U^{(\ell)}\|_F^2
 +\frac{\|U_w\|_2^2}{n}.
 \tag{2}
\]

The closure has the original clock tau(0)=1, dot(tau)=hat(rho), and the
original raw moments. For j=0,...,q-1,

\[
\begin{aligned}
 \dot{\bar h}_{a,j}^{(\ell-1)}
 &=\widehat\rho\,\widehat h_a^{(\ell-1)}
 -\frac{\widehat\rho}{\tau}
 \left[j\bar h_{a,j}^{(\ell-1)}+
       \sum_{i<j}(2i+1)\bar h_{a,i}^{(\ell-1)}\right],\\
 \dot{\bar\delta}_{a,j}^{(\ell)}
 &=\widehat r_a\widehat\delta_a^{(\ell)}
 -\frac{\widehat\rho}{\tau}
 \left[j\bar\delta_{a,j}^{(\ell)}+
       \sum_{i<j}(2i+1)\bar\delta_{a,i}^{(\ell)}\right],\\
 \widehat W^{(\ell)}
 &=W_0^{(\ell)}-
 \frac2{mn\tau}\sum_{a=1}^m\sum_{j<q}(2j+1)
       \bar\delta_{a,j}^{(\ell)}\bar h_{a,j}^{(\ell-1)\top}.
\end{aligned}\tag{3}
\]

The closure first matrix and readout follow (1), evaluated in its own
reconstructed network. Initially bar(h)_{a,0}^{(ell-1)}=h_{0,a}^{(ell-1)},
and all other moments vanish. No part of (3) uses the dense trajectory.

For the proof only, the forward history equals its initial value on [0,1]
and its closure value at subsequent clock times. The backward history is
zero on [0,1] and equals

\[
 b_a^{(\ell)}(\tau(t))
   =\frac{\widehat r_a(t)}{\widehat\rho(t)}
       \widehat\delta_a^{(\ell)}(t).
 \tag{4}
\]

The backward history is continuous at 1 because w(0)=0. The sample norm of
r/rho is one: m^{-1} sum_a(r_a/rho)^2=1; an individual ratio need not be
bounded by one. All aggregate estimates below retain this normalization.

The raw finite-dimensional ODE is locally Lipschitz on tau>0. If Y=0, every
velocity initially vanishes and both systems are stationary. Otherwise a
regular solution cannot reach rho=0 at a finite interior time: that state is
an equilibrium of the entire raw ODE, and backward uniqueness would make
the preceding solution stationary. Clock division in the proof is therefore
legitimate on each compact regular interval. The algorithm never divides by
rho.

## 2. Exact history identities

Let Pi_q^A denote the orthogonal projection in L2([0,A]) onto degree below q,
acting componentwise, and put e_g(A)=g(A)-(Pi_q^A g)(A). Differentiating (3)
and its moment integrals gives

\[
 \dot{\widehat\theta}=F(\widehat\theta)+\mathcal E,
 \qquad \mathcal E^{(1)}=\mathcal E_w=0,
 \qquad
 \mathcal E_\ell=\frac{2\widehat\rho}{mn}\sum_a
          e_{b,a}^{(\ell)}e_{h,a}^{(\ell-1)\top}.
 \tag{5}
\]

For an aggregate history g=(g_a), define its normalized squared tail by

\[
 D_g(A)=\frac1{mn}\sum_a\int_0^A
                   \|g_a-\Pi_q^A g_a\|_2^2\,d\xi.
\]

Orthogonality gives the exact growing-interval identity

\[
 \frac{dD_g(A)}{dA}=\frac1{mn}\sum_a\|e_{g,a}(A)\|_2^2.
 \tag{6}
\]

Indeed the derivative of the approximating polynomial still has degree below
q, so its pairing with the projection error is zero. At A=1 both history
tails vanish. The shifted Legendre eigenvalue identity then yields, for H1
histories,

\[
 D_g(A)\le\frac{A^2}{4q(q+1)}
          \frac1{mn}\sum_a\int_0^A\|g_a'(\xi)\|_2^2\,d\xi.
 \tag{7}
\]

For clarity, the eigenvalue identity is
-[xi(A-xi)(p_j^A)']'=j(j+1)p_j^A. Integration by parts and Bessel's
inequality put q(q+1) times the squared projection tail below the weighted
derivative energy; xi(A-xi)<=A^2/4 proves (7).

The rank-one identity ||uv^top/n||_F=(||u||_2/sqrt(n))
(||v||_2/sqrt(n)), followed by sample and clock Cauchy--Schwarz in (5), gives

\[
 \int_0^t\|\mathcal E_\ell(s)\|_F\,ds
       \le2\sqrt{D_{b^{(\ell)}}(\tau(t))
                         D_{h^{(\ell-1)}}(\tau(t))}.
 \tag{8}
\]

These statements refer to the closure's own histories and exact physical
defect. They do not replace the algorithm with an externally driven model.

## 3. A priori readout and dense estimates

The readout equation is exact in either model. With
<u,v>_m=m^{-1} sum_a u_a v_a, it gives

\[
\begin{aligned}
 \frac d{dt}\frac{\|w\|_2^2}{n}
 &=-4\langle r,f\rangle_m\\
 &=2Y^2-2\rho^2-2\|f\|_m^2\\
 &=Y^2-4\|f-y/2\|_m^2\le Y^2.
\end{aligned}\tag{9}
\]

The second equality uses r=f-y and expands both squared norms. Integrating
from the zero readout proves, without bounded activation values,

\[
 \frac{\|w(t)\|_2}{\sqrt n}\le Y\sqrt t,
 \qquad \int_0^t\rho(s)^2\,ds\le Y^2t,
 \qquad \int_0^t\rho(s)\,ds\le Yt.
 \tag{10}
\]

For dense gradient flow the loss is rho^2 and

\[
 \frac d{dt}\rho_D^2=-\|F(\theta_D)\|_{\rm par}^2,
 \qquad
 \|\theta_D(t)-\theta_0\|_{\rm par}\le Y\sqrt t.
 \tag{11}
\]

The latter is Cauchy--Schwarz in physical time. At fixed finite n it also
proves dense global continuation because every physical parameter remains
bounded on finite intervals.

## 4. Width-independent continuation and absolute defect

Assume deterministic initialization bounds

\[
 \|W_0^{(1)}\|_F/\sqrt n\le A_0,
 \qquad \max_{2\le\ell\le L}\|W_0^{(\ell)}\|_{\rm op}\le K_0,
 \qquad w_0=0.
 \tag{12}
\]

Fix T>0 and Y>0. Define R=Y sqrt(T)+1 and stop the closure at its first
mobility displacement R from initialization or its maximal existence time.
On this stopped interval the hidden operator norms are at most K_R=K_0+R,
the first-matrix RMS is at most A_0+R, and the readout RMS is at most
B_w=Y sqrt(T), by (10). Set

\[
 H_1=b_1+s_1(A_0+R),\qquad
 H_\ell=b_\ell+s_\ell K_RH_{\ell-1},
\]
\[
 B_L=s_LB_w,\qquad B_\ell=s_\ell K_R B_{\ell+1},
 \qquad \rho_* =Y+B_wH_L,
 \qquad S=YT,\qquad A_c=1+S.
 \tag{13}
\]

Forward induction using |phi_l(u)|<=b_l+s_l|u| bounds every sphere-query
feature RMS by H_l. Backward induction bounds every training response RMS
by B_l. Hence rho<=rho_*, and (10) bounds tau<=A_c. All constants in (13)
are independent of n and q.

Define the forward clock energies, including their constant prefixes, by

\[
 Z_\ell(t)=\frac1{mn}\sum_a\int_0^{\tau(t)}
                  \|(h_a^{(\ell)})'(\xi)\|_2^2\,d\xi.
\]

They obey Z_l(t)<=Z_l^*, where the following finite recursion suffices:

\[
 Z_1^*=4S s_1^2B_1^2,
\]
\[
 Z_\ell^*=3s_\ell^2\left[
       4S B_\ell^2H_{\ell-1}^4+
       (K_R^2+2A_c^2B_\ell^2H_{\ell-1}^2)Z_{\ell-1}^*\right]
       \quad(\ell\ge2).
 \tag{14}
\]

Here is the full closure of this recursion. In clock time,
|| (W^(1))' ||_F/sqrt(n)<=2B_1, by sample Cauchy--Schwarz in (1), so the
first line follows. Backward history RMS is at most B_l. Evaluation of a
degree-below-q polynomial at A has L2 norm q/sqrt(A), because
sum_{j<q}(2j+1)/A=q^2/A. Consequently backward endpoint-error RMS is at most
(q+1)B_l. Equations (5)--(7) then imply

\[
 \int_1^{\tau(t)}\|\mathcal E_\ell/\widehat\rho\|_F^2\,d\xi
 \le4(q+1)^2B_\ell^2D_{h^{(\ell-1)}}
 \le2A_c^2B_\ell^2Z_{\ell-1}(t).
 \tag{15}
\]

The factor (q+1)/q is at most two. Differentiate
h_l=phi_l(W_l h_{l-1}). The three terms are the canonical weight velocity,
the defect, and propagation of h_{l-1}'. Their squared sum is bounded by
three times their squared norms. Their respective integrated bounds are
4S B_l^2 H_{l-1}^4, H_{l-1}^2 times (15), and K_R^2 Z_{l-1}. Multiplication
by s_l^2 gives (14). This proof does not differentiate a backward gate.

Since the backward history vanishes on [0,1], contraction gives
D_b<=S B_l^2. Equations (7), (8), and (14) yield

\[
 \int_0^t\sum_{\ell=2}^L\|\mathcal E_\ell(s)\|_F\,ds
 \le\frac{C_E}{\sqrt{q(q+1)}}\le\frac{C_E}{q},
 \qquad
 C_E=A_c\sqrt S\sum_{\ell=2}^L B_\ell\sqrt{Z_{\ell-1}^*}.
 \tag{16}
\]

To close the stop, define

\[
 M=2\rho_*\left[
 B_1^2+\sum_{\ell=2}^L B_\ell^2H_{\ell-1}^2+H_L^2
 \right]^{1/2}.
 \tag{17}
\]

Equation (1) and sample Cauchy--Schwarz give ||F||_par<=M throughout the
stopped region. Since F is minus the loss gradient in mobility coordinates,
the exact closure loss identity is

\[
 \frac d{dt}\widehat\rho^2
 =-\|F(\widehat\theta)\|_{\rm par}^2
  -\langle F(\widehat\theta),\mathcal E\rangle_{\rm par}.
 \tag{18}
\]

Integrating and discarding the nonnegative final loss gives

\[
 \int_0^t\|F(\widehat\theta)\|_{\rm par}^2\,ds
 \le Y^2+MC_E/q.
 \tag{19}
\]

The integral equation (5), physical-time Cauchy--Schwarz, and (16) therefore
bound the displacement by

\[
 \|\widehat\theta(t)-\theta_0\|_{\rm par}
 \le\sqrt{T(Y^2+MC_E/q)}+C_E/q
 \le Y\sqrt T+\sqrt{TMC_E/q}+C_E/q.
 \tag{20}
\]

For every integer

\[
 q\ge q_0:=\left\lceil\max\{1,16TMC_E,4C_E\}\right\rceil,
 \tag{21}
\]

the last two terms total at most 1/2, so the stopped radius R cannot be
reached. At each fixed n,q, the physical parameters and tau are bounded,
and each raw moment is an integral of a bounded finite-dimensional history
against |p_j|<=1. Thus the full raw state remains bounded with tau>=1; its
locally Lipschitz ODE extends past every proposed finite maximal endpoint.
This proves existence and (13)--(20) throughout [0,T]. The case C_E=0 is
included: then the defect is zero and q_0=1.

There is also the quantitative loss statement

\[
 \int_0^T\left(\frac d{dt}\widehat\rho^2\right)_+dt
 \le MC_E/q.
 \tag{22}
\]

Indeed the positive part in (18) is at most
||F||_par ||E||_par, and ||E||_par<=sum_l||E_l||_F. This measures the
closure's violation of loss monotonicity. It is not a comparison of its loss
with dense loss.

## 5. The Gaussian confidence event has no width remainder

Fix 0<delta<1. First-layer entries are independent N(0,1), hidden entries
are independent N(0,1/n), and the matrices are mutually independent, as in
the canonical initialization. For every n>=1 the first-layer Gaussian law gives
E[||W_0^(1)||_F^2/n]=d. Markov's inequality therefore gives the bound in
(12) with A_0=sqrt(2d/delta), at failure probability at most delta/2.

For a Gaussian hidden matrix with entry variance 1/n, two Euclidean
1/4-nets, each of cardinality at most 9^n, give

\[
 \Pr\{\|W_0^{(\ell)}\|_{\rm op}>K_0\}
 \le2\exp\{n(2\log9-K_0^2/8)\}.
 \tag{23}
\]

To verify the constants, its operator norm is at most twice the largest
absolute bilinear form on the two nets. Each fixed bilinear form is
N(0,1/n), and the scalar Gaussian tail at K_0/2 is at most
2 exp(-n K_0^2/8). A union bound proves (23). Choose

\[
 K_0=\sqrt{8\left[2\log9+
                    \log\frac{4(L-1)}\delta\right]}.
 \tag{24}
\]

At every n>=1 each hidden failure is at most delta/[2(L-1)]. Intersecting
these L events yields probability at least 1-delta. On this event one common
set of constants and q_0 in (13)--(21) works simultaneously for every
q>=q_0 at that width. The constants contain no n-dependent remainder,
threshold, or maximum initialized entry. No common realization across
infinitely many independently sampled widths is claimed.

## 6. What is still required for prediction tracking

The energy proof supplies exact perturbed gradient flow with a vanishing
L1-in-time defect. For each fixed width ordinary finite-dimensional
continuous dependence then proves tracking as q tends to infinity. That
continuity constant need not be uniform in width. The following two missing
estimates are distinct.

First, upgrading (16) to O(q^-2) by paired history tails requires a uniform
backward clock derivative estimate. At each layer,

\[
 \dot\delta_a^{(\ell)}=
 \phi_\ell'(z_a^{(\ell)})\odot\dot k_a^{(\ell)}
 +\phi_\ell''(z_a^{(\ell)})\odot k_a^{(\ell)}
                                      \odot\dot z_a^{(\ell)}.
 \tag{25}
\]

Strip analyticity bounds phi_l'', but operator/RMS bounds on k and dot(z)
do not bound the RMS of their coordinatewise product. For example the
vectors u=v=sqrt(n)e_1 each have RMS one, whereas u odot v has RMS sqrt(n).
This elementary example diagnoses the estimate; it is not a trajectory or
Gaussian counterexample. The same issue occurs for the unbounded readout
multiplier at the top layer when activation values are not bounded.

Second, comparison of the two actual vector fields encounters

\[
 \widehat\delta_a^{(\ell)}-\delta_a^{(\ell)}
 =\phi_\ell'(\widehat z_a^{(\ell)})\odot
                  (\widehat k_a^{(\ell)}-k_a^{(\ell)})
 +[\phi_\ell'(\widehat z_a^{(\ell)})-
                \phi_\ell'(z_a^{(\ell)})]\odot k_a^{(\ell)}.
 \tag{26}
\]

The second product again has no uniform L2 Lipschitz estimate from the
available RMS bounds. Replacing its carrier sup norm by its Euclidean norm
introduces sqrt(n), exactly as in the supplied joint-order theorem. The
signed gradient-flow comparison also contains the corresponding weighted
quadratic form; the dissipative Jacobian Gram does not remove every residual
times Hessian contribution.

The known one-input coordinate cancellation does not directly repair (26)
for correlated data. For one first-layer row a in R^d, the coefficient
vector fields are X_b(a)=phi'(v_b^top a)v_b. Their bracket is

\[
 [X_a,X_b]
 =(v_a^\top v_b)
 \left[\phi'(z_a)\phi''(z_b)v_b-
       \phi'(z_b)\phi''(z_a)v_a\right].
 \tag{27}
\]

It is generally nonzero, so a single smooth change of coordinates cannot
make all these fields constant. This excludes that particular simultaneous
straightening argument, not all geometric metrics or Gaussian stability.

A Gaussian tail estimate might resolve the stability gap through an Osgood
modulus, without a uniform carrier maximum. For example, if the actual dense
carriers had uniform aggregate L2 tail bounded by C exp(-cM^2), then splitting
(26) at magnitude M would bound its troublesome term by
C M e+C exp(-cM^2), where e is parameter discrepancy. Choosing
M proportional to sqrt(log(1/e)) would yield the modulus
C e sqrt(log(1/e)), whose reciprocal has a divergent integral at zero.
This is a conditional mechanism only: the required evolving Gaussian tail
bound is not a consequence of initialization tails and the energy estimates
proved here. Nor does this mechanism, by itself, supply the backward
derivative bound in (25).

## 7. A genuine special-case tracking consequence

For layerwise affine activations phi_l(u)=a_l u+c_l, arbitrary depth and
arbitrary finite data, the same argument does yield width-uniform O(q^-2)
tracking on every finite horizon, including all sphere predictions. This
special case permits unbounded activation values and arbitrary labels, but
does not settle nonlinear activations.

Here is why both missing steps close in that case. On the bounded parameter
region obtained above, forward and backward subtraction involve only bounded
operators, matrix increments controlled by their Frobenius norms, and
constant gates. Rank-one subtraction in (1) therefore gives a finite
width-independent constant C_F with

\[
 \|F(\theta)-F(\vartheta)\|_{\rm par}
 \le C_F\|\theta-\vartheta\|_{\rm par}.
 \tag{28}
\]

The same finite layer recursions bound the derivative of each training
prediction by C_f times the parameter increment norm. To control the closure
velocity pointwise uniformly in q, use the endpoint bounds from the actual
Legendre construction,

\[
 \|e_h\|_{\mathrm{RMS}}
    \le\sqrt{A_c/(3q)}\sqrt{Z_{\ell-1}^*},\qquad
 \|e_b\|_{\mathrm{RMS}}\le65\sqrt q B_\ell.
\]

Thus ||E_l||_F<=130 rho B_l sqrt(A_c Z_{l-1}^*/3), and
||dot(theta)||_par<=C rho. This bound in fact holds also for the nonlinear
case. It implies ||dot(r)||_m<=C rho, hence

\[
 Y e^{-CT}\le\rho(t)\le Y e^{CT},
 \qquad\|\partial_t(r/\rho)\|_m\le2C.
 \tag{29}
\]

For affine activations the backward recursion has constant gates, so its
time derivative has RMS at most C rho; all matrix velocities are bounded
by C rho. Consequently (4), (29), and dxi=rho dt give

\[
 \frac1{mn}\sum_a\int_0^{\tau(T)}
                      \|(b_a^{(\ell)})'(\xi)\|_2^2d\xi
 \le C_{T,Y}<\infty.
 \tag{30}
\]

In detail, the physical derivative of b has aggregate RMS at most
C+C rho, and its clock derivative energy is the physical integral of this
squared quantity divided by rho. The positive lower bound in (29) makes
that integral finite, independently of n,q. The fixed positive Y is allowed
in this constant; Y=0 is stationary. The backward prefix is continuous and
zero, so (7) applies without a jump term. Pairing (30) with (14) in (8)
improves (16) to C/q^2. Gronwall using (28) now gives

\[
 \sup_{t\le T}\|\widehat\theta(t)-\theta_D(t)\|_{\rm par}
 \le C_{T,Y}q^{-2}.
 \tag{31}
\]

Both paths lie in the same bounded region, by (11) and the energy
continuation. The forward difference recursion on their straight parameter
segment, uniformly over ||v||=1, gives

\[
 \sup_{t\le T,\ \|x\|_2=\sqrt d}
          |\widehat f(t,x)-f_D(t,x)|\le C_{T,Y}q^{-2}.
 \tag{32}
\]

The constants in (28)--(32) also depend on the fixed layer coefficients,
depth, initialization bounds, and data, but not n,q. The Gaussian event of
Section 5 supplies the advertised fixed confidence.

For the full nonlinear strip-analytic class, this route establishes
width-independent finite-time existence, boundedness, O(q^-1) absolute
consistency, and O(q^-1) positive loss variation. It establishes neither
O(q^-2) prediction tracking nor any explicit weaker prediction rate under
the requested unrestricted Gaussian assumptions. The deterministic
multiplier obstruction is not a disproof of such a Gaussian theorem.

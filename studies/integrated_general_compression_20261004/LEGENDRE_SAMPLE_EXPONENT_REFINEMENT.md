# Legendre comparison with polynomial sample dependence

**Interface correspondence (2026-10-05).** [RESULT.md](RESULT.md),
(Legendre error) and (Legendre order), expand (2)–(3) below using
`lambda=gamma/m`, `z=Ym/gamma`, and `B=beta^(100L)`. Its `q` is this
note's memory order. For a requested error, choosing the least admissible
integer satisfying the existing error inequality is a certificate
selection, not a change to the closure or its proof. The event remains
simultaneous in order; the original root-width prescription (4) is retained.

2026-10-04. Scoped continuation of the integrated study. This note replaces
the unsigned stability estimate in `EXPLICIT_LEGENDRE_COMPARISON.md` by a
parameter energy estimate. It then uses convexity of the exponential, retaining
the actual label amplitude, to remove inverse-gap factors from the exponential
width dependence. The new stability calculation and its numerical assembly
are internal derivations; the source event and fitting results are inherited
from the current study. No statement about larger labels is made.

## 1. Statement and conventions

Fix hidden depth \(L\ge2\), width \(n\), input dimension \(d\), and
training inputs \(x_a\in\mathbb R^d\), \(\|x_a\|=\sqrt d\),
\(a=1,\ldots,m\). Write \(v=x/\sqrt d\). The dense forward pass is
\[
 z^{(1)}=Av,\qquad z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\qquad
 h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad
 f=w^\top h^{(L)}/n.
\]
Here \(A\in\mathbb R^{n\times d}\), \(W^{(\ell)}\in\mathbb R^{n\times n}\)
for \(2\le\ell\le L\), and \(w\in\mathbb R^n\). The first block has
independent standard Gaussian initial entries; the later hidden entries
are independent \(N(0,1/n)\); all blocks are independent and \(w(0)=0\).
The loss is \(m^{-1}\sum_a(f_a-y_a)^2\), with mobilities
\((n,1,\ldots,1,n)\). The order-\(q\) comparison is the original closure
in `GENERAL_LEGENDRE_TRANSFER.md` §2: its clock satisfies
\(\dot\tau=\widehat\rho\), \(\tau(0)=1\), and it uses the constant unit
forward prefix and zero backward prefix. It retains the same initialized
hidden mixers and the same physical time as the dense flow.

Each activation is real on the real axis, holomorphic on the strip
\(|\operatorname{Im}z|<a\), and has bounded first derivative there.
Activation values need not be bounded. Define
\[
 b=\max_\ell|\phi_\ell(0)|,\quad
 s=\max\{1,\max_\ell\sup_{|\operatorname{Im}z|\le a/2}|\phi_\ell'(z)|\},
 \quad t_2=\max_\ell\sup_{|\operatorname{Im}z|\le a/2}|\phi_\ell''(z)|,
\]
\[
 \beta=\max\{10,1+b,16/a,s,\max(1,t_2)\}.
\]
The covariance recursion and its gap are
\[
 Q^{(0)}_{ab}=x_a^\top x_b/d,\qquad
 Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
 \quad Z\sim N(0,Q^{(\ell-1)}),\qquad
 \gamma=\lambda_{\min}(Q^{(L)})>0.
\]
Thus \(\gamma\) is the unweighted gap. Put
\[
 \lambda=\gamma/m,\qquad Y=\|y\|_2/\sqrt m,\qquad z=Y/\lambda,
 \qquad 0<z\le\beta^{-30L}.                                      \tag{1}
\]
The scalar \(z\), without a layer index, denotes the actual label-to-gap
ratio only in this note; the vectors \(z^{(\ell)}\) remain preactivations.

The following explicit width factor has no data-dependent exponential
coefficient:
\[
 B=\beta^{100L},\qquad u_n=\sqrt{\log(en)},\qquad
 F_n=(1+Bzu_n)\,[1+Bz^2(e^{u_n}-1)],
\]
\[
 P_n=3Bz^2(1+\lambda^{-1})F_n.                              \tag{2}
\]
On the same initialization and dense-carrier event used in the existing
comparison, simultaneously for every integer \(q\ge\max\{1,P_n\}\),
\[
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |\widehat f_{n,q}(t,x)-f_n(t,x)|
 \le YP_n\frac{\sqrt{\log(eq)}}{q^2}.                     \tag{3}
\]
In particular the completely specified order
\[
 Q_n=\max\{3,P_n,n^{1/4}\sqrt{P_n}\},\qquad
 q_n=\left\lceil4Q_n[\log(e+Q_n)]^{1/4}\right\rceil        \tag{4}
\]
satisfies
\[
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |\widehat f_{n,q_n}(t,x)-f_n(t,x)|\le\frac{Y}{8\sqrt n}
 \le\frac{Y}{\sqrt n}.                                  \tag{5}
\]
All appearances of \(Y\) in (2) are its actual value. In particular
\(P_n=O((Y/\lambda)^2)\) as \(Y\to0\) at fixed other quantities.
Every inverse-gap factor outside the elementary order inversion is
polynomial. The only exponential width factor in (2) is \(e^{u_n}\),
whose coefficient is independent of \(m,\gamma,Y\).

The event has probability tending to one at each individual width.
The inherited source theorem's sufficient stochastic width is still
implicit; (2)--(5) introduce no further eventual-width restriction.
For fixed nonzero labels and other problem parameters,
\(q_n=n^{1/4+o(1)}\). The moving and fixed counts are respectively
\[
 2(L-1)mnq_n+n(d+1)+1=n^{5/4+o(1)},\qquad (L-1)n^2.
                                                               \tag{6}
\]
For \(Y=0\), both predictors are identically zero and any positive order
gives exact agreement.

The proof first retains the positive semidefinite training-residual term
in the parameter discrepancy energy. The resulting exponent is an
activation-dependent multiple of \(z+z^2u_n\). A convexity inequality
then preserves the actual \(z,z^2\) as polynomial factors. Finally the
existing projection-error product is absorbed with explicit constants.

## 2. Inherited event and physical estimates

Define
\[
 q_0=1,\qquad q_\ell=\mathbb E\phi_\ell(\sqrt{q_{\ell-1}}Z)^2,
 \quad Z\sim N(0,1),\qquad
 H=\max\{1,\sqrt{q_1},\ldots,\sqrt{q_L}\}.
\]
`GENERAL_EXPLICIT_FITTING.md` and
`GENERAL_EXPLICIT_CLOSURE_FITTING.md`, including their complete checks,
give the following consequences on their initialization event for every
order, with \(\kappa=\lambda/4\), \(R=8Y/\sqrt\lambda\):
\[
 \|A\|_{\rm op}/\sqrt n,\quad
 \max_{\ell\ge2}\|W^{(\ell)}\|_{\rm op}\le9,\qquad
 \sup_{\|x\|=\sqrt d,\ell}\|h^{(\ell)}(x)\|_2/\sqrt n\le2H,
 \qquad \|w\|_2/\sqrt n\le R.                            \tag{7}
\]
Both dense and closure satisfy (7), converge in physical parameters,
and fit the labels. Their residual RMS norms satisfy
\[
 \int_0^\infty\rho_D(t)\,dt\le2z,\qquad
 \int_0^\infty\widehat\rho(t)\,dt\le4z.                 \tag{8}
\]
Write
\[
 k_a^{(L)}=w,\qquad
 k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)},\qquad
 \delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)}.
\]
The source recurrence and `SIMPLE_CONSTANTS_SOURCE_CHECK.md` give
\[
 S_*^{\rm src}\ge\beta^{-26L},\qquad K_{\rm src}\le\beta^{21L}.
\]
Since \(16z\le\beta^{-26L}\), its hypothesis holds. On the same
all-time event as in the numerical Legendre comparison,
\[
 \max_{a,\ell,i}\sup_{t\ge0}|k_{D,a,i}^{(\ell)}(t)|
 \le M:=32K_{\rm src}zu_n.                               \tag{9}
\]
This is a training-input carrier bound only; the proof does not require
one at every query. The factor two relative to the finite-horizon source
bound is the already checked physical-tail enlargement. No carrier
bound on the closure or on a segment between trajectories is assumed.

## 3. A one-reference gradient bound along parameter segments

Use the Euclidean physical coordinates
\[
 \theta=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n).
\]
Their ordinary Hilbert gradient generates the prescribed mobilities.
Let \(\Delta=\widehat\theta-\theta_D\), \(e=\|\Delta\|\), and let
\(d_1\) be the sum of these \(L+1\) block norms. Then
\(d_1\le\sqrt{L+1}\,e\). All norms of vector features and responses
in this section are divided by \(\sqrt n\).

For \(0\le v\le1\), set \(\theta_v=\theta_D+v\Delta\).
The operator and readout bounds in (7) persist by convexity. Define the
deterministic feature envelope
\[
 Q_1=b+9s,\qquad Q_\ell=b+9sQ_{\ell-1},\qquad
 Q=\max\{1,Q_1,\ldots,Q_L\}.
\]
The bound \(|\phi_\ell(t)|\le b+s|t|\) gives feature RMS at most
\(Q\) throughout this segment, for every sphere query. With
\[
 T=9s,\qquad F_{\rm seg}=QT^{L-1},\qquad
 B_\delta=sT^{L-1}R,
\]
forward subtraction from the dense reference gives
\[
 \max_\ell\|z_v^{(\ell)}-z_D^{(\ell)}\|_2/\sqrt n
 \le F_{\rm seg}v d_1,\qquad
 \max_\ell\|h_v^{(\ell)}-h_D^{(\ell)}\|_2/\sqrt n
 \le sF_{\rm seg}v d_1.                                 \tag{10}
\]
Indeed the first preactivation difference is bounded by the first
parameter-block difference, and each later difference obeys
\(\Delta z_\ell\le9s\Delta z_{\ell-1}+Q\Delta W_\ell\).

For the backward difference use exactly the asymmetric identity
\[
 \delta_v-\delta_D
 =\phi'(z_v)\odot(k_v-k_D)
   +[\phi'(z_v)-\phi'(z_D)]\odot k_D.
\]
Thus only the dense coordinate maximum in (9) enters the second term.
The first term propagates through matrices of operator norm at most nine;
the matrix-difference term uses the dense response RMS, at most
\(B_\delta\). Iterating over at most \(L\) layers therefore gives
\[
 \max_\ell\|\delta_v^{(\ell)}-\delta_D^{(\ell)}\|_2/\sqrt n
 \le(d_0+d_1^{\rm coef}M)v d_1,
\]
\[
 d_0=sT^{L-1}(1+B_\delta),\qquad
 d_1^{\rm coef}=Lt_2F_{\rm seg}T^{L-1}.                  \tag{11}
\]
Here \(d_1^{\rm coef}\) is a scalar coefficient, distinct from the
block-sum parameter distance \(d_1\).

For a training output the gradient blocks in these coordinates are
\[
 g_{a,A}=\delta_a^{(1)}v_a^\top/\sqrt n,\qquad
 g_{a,\ell}=\delta_a^{(\ell)}h_a^{(\ell-1)\top}/n,
 \qquad g_{a,w}=h_a^{(L)}/\sqrt n.
\]
Subtract hidden gradients as
\((\delta_v-\delta_D)h_v^\top+\delta_D(h_v-h_D)^\top\).
Equations (10)--(11) then prove
\[
 \|g_a(\theta_v)-g_a(\theta_D)\|
 \le (j_0+j_1M)v d_1\le(K_0+K_1M)v e,                 \tag{12}
\]
where all coefficients are explicit:
\[
 p=1+Q(L-1),\quad
 j_0=pd_0+[1+(L-1)B_\delta]sF_{\rm seg},\quad
 j_1=pd_1^{\rm coef},\qquad K_i=\sqrt{L+1}\,j_i.
\]
Write \(K(M)=K_0+K_1M\). Integrating (12) along the segment proves
the Taylor remainder estimate
\[
 |f_a(\widehat\theta)-f_a(\theta_D)-g_a(\theta_D)\cdot\Delta|
 \le\tfrac12K(M)e^2.                                  \tag{13}
\]
The segment is used only for this scalar Taylor formula. No claim that it
is a training trajectory, or has a uniformly bounded carrier, is needed.

## 4. Signed discrepancy energy

Let \(J_D,J_{\widehat\theta}\) be the training-output Jacobians, and use
the sample inner product \(\langle r,s\rangle_m=m^{-1}\sum_a r_as_a\).
The adjoints below use this inner product and the parameter Hilbert norm.
Differentiating the exact Legendre reconstruction gives
\[
 \dot\theta_D=-2J_D^*r_D,\qquad
 \dot{\widehat\theta}=-2J_{\widehat\theta}^*\widehat r+\mathcal E,
                                                               \tag{14}
\]
where \(\mathcal E\) has only hidden-matrix blocks. In clock coordinates,
those blocks are the products of the forward and backward endpoint
projection errors, as proved in the closure-fitting check.

Put \(v_r=\widehat r-r_D\). From (13),
\[
 v_r=J_D\Delta+\mathcal R,\qquad
 \|\mathcal R\|_m\le\tfrac12K(M)e^2,
 \qquad\|(J_{\widehat\theta}-J_D)\Delta\|_m\le K(M)e^2.
\]
Subtract (14) and take its scalar product with \(\Delta\):
\[
 \begin{aligned}
 \tfrac12\frac d{dt}e^2
 &=-2\|v_r\|_m^2+2\langle v_r,\mathcal R\rangle_m
   -2\langle\widehat r,(J_{\widehat\theta}-J_D)\Delta\rangle_m
   +\langle\Delta,\mathcal E\rangle\\
 &\le K(M)(\rho_D+3\widehat\rho)e^2+e\|\mathcal E\|.
 \end{aligned}                                                    \tag{15}
\]
The first equality retains the negative training-output discrepancy
square. In particular no inverse training Gram is used to integrate an
unsigned residual discrepancy. Applying the differential inequality to
\(\sqrt{e^2+\varepsilon^2}\) and sending \(\varepsilon\downarrow0\)
justifies division at \(e=0\). Since the initial states agree, (8) gives,
on every finite physical horizon,
\[
 \sup_t d_1(t)\le\mathcal A_{\rm new}\,\epsilon,
 \quad \epsilon=\int\sum_{\ell=2}^L\|\mathcal E_\ell(t)\|_F\,dt,
 \quad
 \mathcal A_{\rm new}=\sqrt{L+1}\,e^{14K(M)z}.            \tag{16}
\]
The integral defining \(\epsilon\) is over that horizon. The exponent
before any label-cap simplification is exactly bounded by
\[
 14K(M)z=14K_0(R)z+448K_1K_{\rm src}z^2u_n.             \tag{17}
\]
This is the energy improvement: the earlier comparison had an additional
inverse-gap multiplier inside its stability exponent.

## 5. Numerical envelope and actual-label interpolation

For the algebra write \(X=\beta^L\ge100\) and
\(\chi=1+\lambda^{-1}\). These are proof notation only. The checked
fitting recurrences imply
\[
 H\le X^2,\quad \lambda\le H^2\le X^4,\quad
 D_\ell=s(9s)^{L-\ell}\le X^2,\quad \sqrt{C_\ell}\le X^8,
\]
\[
 C_1=4s^2D_1^2,\qquad
 C_\ell=3s^2(64H^4D_\ell^2+82C_{\ell-1}).
                                                               \tag{18}
\]
The covariance inequality follows from
\(\lambda\le\operatorname{tr}(Q^{(L)})/m=q_L\).
Condition (1) gives
\[
 R=8z\sqrt\lambda\le X^{-27},\qquad
 8z\le1,\qquad a_0:=4z\le1,
 \qquad B_\delta\le X^3R\le1.
\]
Also \(Q\le X^2\): the affine recurrence defining \(Q_\ell\) is
bounded inductively by \((10\beta)^\ell\le\beta^{2\ell}\).
Since \(T^{L-1}\le X^2\), the quantities in (11)--(12) satisfy
\[
 F_{\rm seg}\le X^4,\quad d_0\le2X^3,\quad
 d_1^{\rm coef}\le LX^7\le X^8,\quad p\le X^4,
\]
\[
 j_0\le2X^7+(L+1)X^5\le X^8,
 \quad j_1\le X^{12},\quad K_0\le X^9,\quad K_1\le X^{13}.
\]
Using (9) and \(K_{\rm src}\le X^{21}\), (17) yields
\[
 14K(M)z\le X^{10}z+X^{36}z^2u_n.                       \tag{19}
\]
The numerical constants are covered by \(14\le X\) and \(448\le X^2\).

For \(0\le a\le1\), convexity gives \(e^a\le1+2a\). For
\(0\le\vartheta\le1\) and \(u\ge0\), it gives
\[
 e^{\vartheta u}\le1+\vartheta(e^u-1).
\]
Here \(X^{10}z\le X^{-20}\) and
\(X^{36}z^2\le X^{-24}\). Therefore
\[
 \mathcal A_{\rm new}
 \le\sqrt{L+1}(1+2X^{10}z)
            [1+X^{36}z^2(e^{u_n}-1)]
 \le X\,\Xi_n,                                        \tag{20}
\]
\[
 \Xi_n=(1+Bz)[1+Bz^2(e^{u_n}-1)],\qquad B=X^{100}.
\]
The cap is used to verify the interpolation ranges. The coefficients
\(z\) and \(z^2\) have not been replaced by that cap. This is stronger
in label dependence than the uniform bound obtained by simply setting
\(z=\beta^{-30L}\) in (19), and is still explicitly conditional on
the same small-label regime. Lifting that regime would require another
stability argument or another interpolation envelope.

## 6. Projection absorption and its polynomial prefactor

The projection estimates in `EXPLICIT_LEGENDRE_COMPARISON.md` do not use
the old stability argument. Their exact constants, with its symbol \(B\)
renamed \(B_\delta\), are
\[
 T_0=9s,\quad F_z=2HT_0^{L-1},\quad P_0=1+2H(L-1),
\]
\[
 B_d=sT_0^{L-1}(1+B_\delta)+Lt_2F_zT_0^{L-1}M,
 \quad V_z=2F_zB_\delta P_0,
\]
\[
 V_\delta=T_0^{L-1}
 [4sH+4sH(L-1)B_\delta^2+Lt_2MV_z],
 \quad F_h=V_h a_0\sqrt{(1+a_0)/2},
\]
\[
 b_1=\frac{2\sqrt{1+a_0}}\kappa C_cB_\delta,
 \quad b_0=\frac{\sqrt{1+a_0}Y}\kappa V_\delta+2B_\delta\sqrt{a_0},
 \quad C_f=2H+RsF_z.                                   \tag{21}
\]
For completeness the two closure-speed outputs are numerical recurrences:
\[
 T_1=2D_1R,\qquad
 T_\ell=4HD_\ell R+130D_\ell\sqrt{8zC_{\ell-1}}R^2,
\]
\[
 V_1=sT_1,\qquad V_\ell=s(2HT_\ell+9V_{\ell-1}),
 \quad V_h=\max_\ell V_\ell,
\]
\[
 C_c=4\left(4H^2+D_1^2R^2+
             4H^2R^2\sum_{\ell=2}^LD_\ell^2\right)+\lambda/2.
                                                               \tag{22}
\]
Their checked power bounds are \(V_h\le X^{20}R\) and
\(C_c\le X^{11}\). They follow directly by summing the nonnegative
recurrences (18), (22), as recorded in
`SIMPLE_CONSTANTS_LEGENDRE_CHECK.md` §3.

For a finite horizon let \(D=\sup_t d_1(t)\). The forward projection
error is at most \(F_h/q\); the backward projection error is at most
\((b_0+b_1\sqrt{\log q})/q+B_d\sqrt{a_0}D\). Consequently
\[
 \epsilon\le2(L-1)F_h\left[
  \frac{b_0+b_1\sqrt{\log q}}{q^2}
  +\frac{B_d\sqrt{a_0}D}{q}\right].                     \tag{23}
\]
Here \(\epsilon\) is the integral of the norm of the physical defect
in (16), not the norm of its signed integral. To verify this distinction,
let \(\Pi_q^A\) denote orthogonal projection onto polynomials of degree
below \(q\) on the growing clock interval \([0,A]\). For either fixed
history \(g\), with the aggregate sample/neuron Hilbert norm, define
\[
 E_g(A)=\int_0^A\|g(\xi)-\Pi_q^A g(\xi)\|^2\,d\xi.
\]
Differentiating gives
\[
 E_g'(A)=\|g(A)-\Pi_q^A g(A)\|^2.
\]
Indeed the interior derivative pairs the projection residual with
\(\partial_A\Pi_q^A g\), a polynomial of degree below \(q\), so
orthogonality makes that pairing zero. Both prefix energies vanish at
\(A=1\), since the forward prefix is constant and the backward prefix
is zero. The exact reconstruction derivative is
\[
 \mathcal E_\ell(t)=\frac{2\widehat\rho(t)}{mn}
 \sum_a e_{b,a}^{(\ell)}(\tau(t))
             e_{h,a}^{(\ell-1)}(\tau(t))^\top,
\]
where \(b_a=\widehat r_a\widehat\delta_a/\widehat\rho\) is the
backward history before a residual zero and \(e_b,e_h\) are endpoint
projection errors. Cauchy--Schwarz first over samples and then over
\(dA=\widehat\rho\,dt\) therefore gives
\[
 \int_0^T\|\mathcal E_\ell(t)\|_F\,dt
 \le2\sqrt{E_b(\tau(T))}\sqrt{E_h(\tau(T))}.
\]
The history norm is \((m^{-1}n^{-1}\sum_a\|g_a\|_2^2)^{1/2}\).
Insert the two terminal tail-norm bounds just stated and sum over the
\(L-1\) reconstructed layers to obtain (23). For positive labels the
fitting theorem excludes a finite first residual zero; the stationary
zero-label case needs no division. The identity also follows by the
corresponding stopped-interval limit whenever a history is represented
only almost everywhere.

Insert (16). For
\[
 q\ge q_{\rm abs}^{\rm new}
 :=4(L-1)F_hB_d\sqrt{a_0}\,\mathcal A_{\rm new},         \tag{24}
\]
the second term is absorbed, and sphere forward subtraction gives
\[
 \|\widehat f_{n,q}-f_n\|_*
 \le\frac{4(L-1)C_f\mathcal A_{\rm new}F_h}{q^2}
                    (b_0+b_1\sqrt{\log q}).             \tag{25}
\]
The norm denotes the two suprema in (3). First prove the estimate on
finite horizons with the same constants; then pass to all finite times
and the existing physical limits to include \(t=\infty\).

The following bounds keep the powers of the actual \(z\), instead of
discarding them using the label cap:
\[
 F_z\le X^5,\quad P_0\le X^4,\quad
 F_h\le X^{24}z^2,\qquad F_h/Y\le X^{22}z\sqrt\chi,
\]
\[
 B_d\le X^{33}(1+zu_n),\qquad
 V_z\le2X^{12}R,\qquad V_\delta\le X^{40}(1+zu_n),
\]
\[
 b_1\le X^{16}z\sqrt\chi,\qquad
 b_0\le X^{42}z(1+zu_n),\qquad C_f\le X^7.             \tag{26}
\]
Here are the substitutions accounting for the label factors. From (22),
\(F_h\le4X^{20}Rz=32X^{20}z^2\sqrt\lambda\), and dividing by
\(Y=\lambda z\) gives
\(F_h/Y\le32X^{20}z/\sqrt\lambda\). In \(B_d\), its first term is
at most \(2X^3\) and its carrier term at most
\(32LX^{29}zu_n\). For \(V_\delta\), the terms without \(M\)
are at most \(4LX^5\), while the carrier term is at most
\(64LX^{36}Rzu_n\). Using \(R\le1\) proves its bound in (26).
The definition of \(b_1\) gives
\(b_1\le96X^{14}z/\sqrt\lambda\). The two terms of \(b_0\) are
at most \(6X^{40}z(1+zu_n)\) and
\(32X^5z^{3/2}\), respectively. Since \(z\le1\), they have the
stated sum. The loose powers of \(X\ge100\) cover every displayed
numerical constant and the factor \(L\le X\).

In particular, for \(q\ge1\),
\[
 b_0+b_1\sqrt{\log q}
 \le X^{43}z\sqrt\chi(1+zu_n)\sqrt{\log(eq)}.
\]
Using \(4(L-1)\le X^2\), \(\sqrt{a_0}\le1\), and (20),
equations (24)--(26) give
\[
 q_{\rm abs}^{\rm new}\le X^{60}z^2(1+zu_n)\Xi_n,
\]
\[
 \frac{4(L-1)C_f\mathcal A_{\rm new}F_h}{Y}
       (b_0+b_1\sqrt{\log q})
 \le X^{75}z^2\chi(1+zu_n)\Xi_n\sqrt{\log(eq)}.        \tag{27}
\]
Thus both are bounded by the corresponding expressions with
\(Bz^2\chi(1+zu_n)\Xi_n\). Finally, for \(B\ge1\),
\(u_n\ge1\), \(0\le z\le1\),
\[
 (1+zu_n)(1+Bz)
 =1+zu_n+Bz+Bz^2u_n\le1+3Bzu_n\le3(1+Bzu_n).
\]
Equations (2), (27) prove (3), including its absorption condition.

## 7. Order inversion, topology, and scope

For \(Q\ge3\), put \(a_Q=\log(e+Q)>1\) and
\(q=\lceil4Qa_Q^{1/4}\rceil\). Then
\[
 4Qa_Q^{1/4}\le q\le5Qa_Q^{1/4},\qquad
 \log(eq)\le\log(5e)+\log Q+\tfrac14\log a_Q\le4a_Q.
\]
For the last step, \(\log(5e)\le2a_Q\),
\(\log Q\le a_Q\), and \(\log a_Q\le a_Q\).
Consequently the choice (4) gives
\[
 \frac{P_n\sqrt{\log(eq_n)}}{q_n^2}
 \le\frac{2P_n\sqrt{a_{Q_n}}}{16Q_n^2\sqrt{a_{Q_n}}}
 =\frac{P_n}{8Q_n^2}\le\frac1{8\sqrt n}.
\]
Also \(q_n\ge Q_n\ge P_n\), so (3) applies. This proves (5)
for every width on the inherited event, without a new deterministic
width threshold. For fixed positive \(z\), the expression (2) has
\(\log P_n=O(\sqrt{\log n}+\log\log n)\). Hence eventually
\(Q_n=n^{1/4}\sqrt{P_n}\) and (6) follows.

The comparison uses one source event for every order at a given width;
there is no union bound over orders. Both predictions use the same
initialization and unchanged physical time. The all-query estimate comes
from forward subtraction under (7), so no carrier event over the sphere
is required. Their physical parameter convergence includes both fitted
endpoints in the supremum. No simultaneous event over infinitely many
independently initialized widths is asserted.

The current study's fitting checks, source-power check, and numerical
Legendre projection comparison are the dependencies. This note changes
only the deterministic stability step and its algebraic envelope. The
implicit probability threshold of the source theorem remains implicit.
The removal of sample dependence from the exponential uses the existing
small-label cap through a convexity interpolation, while retaining all
actual-label factors. It is not an assertion of sample-uniform stability
outside that cap.

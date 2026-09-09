# Appendix A. Two-input symmetry and the affine core

This note proves the symmetry, initial-kernel, affine-reference, and
nonaffinity ingredients for the genuinely unshifted family
\[
\phi_{a,e}(z)=a z+e\arctan z,\qquad \tfrac12\le a\le1,\quad e\ge0.
\]
The source and limit arguments for this gate are verified in the main text and quantitative chapter.

Fix \(0<\delta\le1\), \(\|x_1\|^2=\|x_2\|^2=d\), and
\(|\rho|\le1-\delta\), where \(\rho=x_1^Tx_2/d\). Write
\(y_1=\sigma,y_2=\sigma\tau\), with \(\sigma,\tau\in\{-1,1\}\).
All raw metrics, initialization laws, forward actions, and backward
adjoints have the normalizations in Theorem T.1.
The population readout initially vanishes; the finite raw model's
small random readout is retained.

## 1. Exact label folding and population scalar reduction

Every odd differentiable activation has even derivative. At any parameter
state, induction through the forward and backward equations gives
\[
z^\ell(-x)=-z^\ell(x),\quad h^\ell(-x)=-h^\ell(x),\quad
f(-x)=-f(x),\quad b^\ell(-x)=b^\ell(x).
\]
Replace the dataset by
\(\widetilde x_j=y_jx_j,\widetilde y_j=1\). Then
\(\widetilde h_j^\ell=y_jh_j^\ell\),
\(\widetilde f_j=y_jf_j\),
\(\widetilde r_j=y_jr_j\), and
\(\widetilde b_j^\ell=b_j^\ell\). Consequently
\[
\widetilde r_j\widetilde b_j^1\widetilde x_j^T
=r_jb_j^1x_j^T,\qquad
\widetilde r_j\widetilde b_j^\ell
(\widetilde h_j^{\ell-1})^T=r_jb_j^\ell(h_j^{\ell-1})^T,\qquad
\widetilde r_j\widetilde h_j^3=r_jh_j^3.
\]
Thus finite raw GF and simultaneous raw Euler/GD have exactly the same
parameter trajectory after label folding, including the original finite
readout. The folded correlation is \(\widetilde\rho=\tau\rho\).

Let \(R\) be the orthogonal reflection exchanging the folded inputs:
\[
v=\widetilde x_1-\widetilde x_2,\qquad
R=I-2vv^T/\|v\|^2.
\]
The angle condition ensures \(v\ne0\). Acting by \(R\) on the first
weight field exchanges both folded samples through all hidden layers.
The scalar objective
\[
g(\Theta)=\tfrac12\sum_j y_j f_j
         =\tfrac12\sum_j\widetilde f_j
\]
and physical loss are invariant. The reflection is an isometry of the
raw metric, so both gradient vector fields are equivariant. Identical
sample clips and odd clips on sign-changing slots preserve this fact
at fixed-cap finite Euler level. Gaussian initialization is invariant.

The limiting fixed-program predictions are deterministic contractions.
Since their approximating laws are sample-exchange invariant, those
deterministic predictions must be invariant:
\(\widetilde f_1=\widetilde f_2=g\). Explicitly, an exchange-invariant
random pair converging in probability to a deterministic pair forces
that pair to equal its exchange. Canonical population action spaces
closed under the paired queries realize the invariance by
measure-preserving involutions. Euler induction and strong limits
preserve it exactly on the constructed path, as follows from the finite-program construction in Appendix C, Part F. This uses no uniqueness of an unconstructed uncut flow.

Undoing the fold gives \(f_j=y_jg\) and \(\mathcal L=(1-g)^2\)
for both uncut and capped constructed paths. For the uncut gradient
fields it yields
\[
f_j=y_jg,\qquad \mathcal L=(1-g)^2,\qquad
\dot\Theta=2(1-g)\nabla g.
\]
The feature equation is \(\Theta'=\nabla g\), with
\(ds/dt=2(1-g)\) and \(g'=y^TKy/4\). A finite realization generally
does not satisfy this population scalar prediction identity.
For a cap, the feature equation is instead \(\Theta'=V_R\) and the
physical equation is \(\dot\Theta=2(1-g)V_R\); the scalar clock is the
same but the gradient and kernel-derivative identities are not asserted.

## 2. Initial kernels for the odd family

Let \(q_0=1,c_0=\rho\), and let \(q_\ell,c_\ell\) be the initial
diagonal and off-diagonal feature second moments. Gaussian propagation
gives a centered preactivation pair \((U,V)\) with diagonal
\(q_{\ell-1}\) and covariance \(c_{\ell-1}\). Oddness gives
\[
q_\ell\pm c_\ell
=\tfrac12\mathbb E[\phi_{a,e}(U)\pm\phi_{a,e}(V)]^2.
\]
Since \(\phi_{a,e}'\ge a\),
\[
|\phi_{a,e}(u)-\phi_{a,e}(v)|\ge a|u-v|,\qquad
|\phi_{a,e}(u)+\phi_{a,e}(v)|\ge a|u+v|,
\]
the second inequality following by replacing \(v\) by \(-v\).
Therefore
\[
q_\ell\pm c_\ell\ge a^2(q_{\ell-1}\pm c_{\ell-1}),\qquad
q_3\pm c_3\ge a^6(1\pm\rho)>0.
\]
All hidden kernel blocks initially vanish because \(C(0)=0\). Hence
\[
\kappa_{a,e}(0)=\tfrac14y^TK^4(0)y
=\frac{q_3+\tau c_3}{2}
\ge a^6\frac{1+\tau\rho}{2}\ge\frac{\delta}{128}. \tag{A.1}
\]
The two strict moment eigenvalues also verify nonsingularity of every
initial preactivation pair. For \(e=0\) these recursions are exact:
\[
q_\ell=a^{2\ell},\qquad c_\ell=a^{2\ell}\rho,\qquad
\kappa_{a,0}(0)=a^6(1+\tau\rho)/2. \tag{A.2}
\]
Equal labels activate \(a^6(1+\rho)\); opposite labels activate
\(a^6(1-\rho)\). The absolute-angle condition treats both without an
offset: at antipodal inputs an odd network cannot fit equal nonzero
labels, and at identical inputs it cannot fit opposite labels.

## 3. Affine active and inactive equations

Define
\[
u=(x_1+\tau x_2)/2,\quad v=(x_1-\tau x_2)/2,\quad
v_u=(1+\tau\rho)/2,\quad v_v=(1-\tau\rho)/2.
\]
Then \(u\cdot v=0\), \(\|u\|^2/d=v_u\),
\(\|v\|^2/d=v_v\), and \(v_u,v_v\ge\delta/2\).
For the affine activation \(az\), put
\[
P_\ell=(z_1^\ell+\tau z_2^\ell)/2,\qquad
Q_\ell=(z_1^\ell-\tau z_2^\ell)/2.
\]
Their forward identities are
\[
P_1=w\cdot u,\ Q_1=w\cdot v,\quad
P_2=aAP_1,\ Q_2=aAQ_1,\quad
P_3=aBP_2,\ Q_3=aBQ_2. \tag{A.3}
\]
Thus \(H=\frac12\sum_j y_jh_j^3=\sigma aP_3\) and
\(g=\sigma a^3\langle C,BAP_1\rangle\). Taking its gradient in the
raw metric gives exactly
\[
\begin{aligned}
C'&=\sigma aP_3,\\
B'&=\sigma a^2C\otimes P_2=\sigma a^3C\otimes(AP_1),\\
A'&=\sigma a^3B^*C\otimes P_1,\\
P_1'&=\sigma v_u a^3A^*B^*C,\qquad Q_1'=0.
\end{aligned} \tag{A.4}
\]
Indeed \(w'=(\sigma a^3/d)(A^*B^*C)u\); contraction with \(u\)
produces \(v_u\), and contraction with \(v\) vanishes. These equations
depend only on \((P_1,A,B,C)\), never on the inactive root \(Q_1(0)\).

Both label sectors are explicit:

* If \(y_1=y_2\), \(P_\ell\) is the common field and \(Q_\ell\) the
  contrast; \(v_u=(1+\rho)/2,v_v=(1-\rho)/2\).
* If \(y_1=-y_2\), \(P_\ell\) is the contrast and \(Q_\ell\) the common
  field; \(v_u=(1-\rho)/2,v_v=(1+\rho)/2\).

## 4. Uniform affine interval through \(g=3/2\)

The affine objective is a continuous polynomial on the affine raw
Hilbert space. Its gradient is locally Lipschitz, with bounded
derivatives on bounded balls uniformly for \(a\in[1/2,1]\).
Picard contraction on such a ball supplies strong local existence and
uniqueness, including at every finite reached state.

Write the hidden state as \(\vartheta\), and \(J_s\) for the bounded
linearization of \(H\). The gradient equations are
\(C'=H,\vartheta'=J_s^*C\), and the strong chain rule gives
\[
C''=J_sJ_s^*C,\qquad \langle C,C''\rangle=\|J_s^*C\|^2\ge0,
\qquad g'=\|C'\|^2+\|J_s^*C\|^2=\|\Theta'\|_{\rm raw}^2.
\]
Twice differentiating \((\|C\|^2+\epsilon^2)^{1/2}\), using
Cauchy--Schwarz and \(\langle C,C''\rangle\ge0\), proves convexity.
Letting \(\epsilon\downarrow0\) gives convexity of \(\|C\|\).
Its initial right slope is \(\|H(0)\|\), because
\(C(0)=0,C'(0)=H(0)\). Thus \(\|C'(s)\|\ge\|H(0)\|\) and
\[
g'\ge\kappa_0,\qquad
\int_0^s\|\Theta'(r)\|_{\rm raw}^2\,dr=g(s),\qquad
\kappa_0=a^6v_u\ge\delta/128. \tag{A.5}
\]

The first hit \(S\) of \(g=3/2\) exists. Before that hit,
\(s\le3/(2\kappa_0)\), and the energy is at most \(3/2\).
A finite maximal endpoint below the target has a strong limit since
\[
\|\Theta(v)-\Theta(u)\|_{\rm raw}
\le\sqrt{(v-u)[g(v)-g(u)]}\le\sqrt{\tfrac32(v-u)}.
\]
Local existence at that reached state extends the branch. An
arbitrarily long branch below the target contradicts \(g(s)\ge\kappa_0s\).
Cauchy--Schwarz then gives, on the entire closed interval \([0,S]\),
\[
S\le S_\delta:=192/\delta,\qquad
\|\Theta(s)-\Theta(0)\|_{\rm raw}
\le\frac3{2\sqrt{\kappa_0}}
\le R_\delta:=12\sqrt2/\sqrt\delta. \tag{A.6}
\]
Set
\[
U=11+R_\delta. \tag{A.7}
\]
Initial first-layer projected norms are one, action norms are at most
ten, and the readout vanishes. Raw displacement controls each projected
change by \(\|\Delta w\cdot x_j\|_2\le\sqrt d\|\Delta w\|_2\),
and operator changes by Hilbert--Schmidt norms. Consequently
\[
\max_j\|z_j^1(s)\|_2,\ \|A(s)\|_{\rm op},\
\|B(s)\|_{\rm op},\ \|C(s)\|_2\le U. \tag{A.8}
\]
The full initial \(\sqrt d\|w_0\|_2\) need not be dimension-independent;
only its projections and raw displacement enter these constants.
Each reference path stops at its own hit \(S\), never being extended
to the uniform duration upper bound \(S_\delta\).

## 5. Active lower bounds and frozen inactive Gaussian fields

Since \(C'=\sigma aP_3\), the radial bound implies
\(a^2\|P_3\|^2\ge a^6v_u\). Using (A.3) and (A.8) backwards gives
\[
\|P_3\|^2\ge a^4v_u,\qquad
\|P_2\|^2\ge a^2v_u/U^2,\qquad
\|P_1\|^2\ge v_u/U^4. \tag{A.9}
\]
Every active hidden field therefore remains nonzero.

A stronger variance bound comes from exact population freezing of the
inactive fields. This requires independence, not merely bounded learned
Hilbert--Schmidt increments. In a fixed finite affine scalar-Euler
prefix with zero initial readout, let
\(\mathscr F_n=\sigma(P_{1,0},A_0,B_0)\). Equations (A.4) make all
active training fields \(\mathscr F_n\)-measurable. Orthogonality of the
Gaussian input projections makes \(Q_0=Q_{1,0}\) an independent
\(N(0,v_vI_n)\) vector. For an \(\mathscr F_n\)-measurable matrix \(T_n\),
\[
\mathbb E[\|T_nQ_0\|_n^2\mid\mathscr F_n]
=\frac{v_v}{n}\|T_n\|_F^2. \tag{A.10}
\]
On bounded-initial-operator events, each fixed Euler prefix has bounded
field norms and ordinary Frobenius norms of its learned increments.
The normalization is
\(\|\Delta s\,p q^T/n\|_F=\Delta s\|p\|_n\|q\|_n\). Moreover
\[
\|B_sA_s-B_0A_0\|_F
\le\|B_s-B_0\|_F\|A_s\|_{\rm op}
+\|B_0\|_{\rm op}\|A_s-A_0\|_F.
\]
Apply (A.10) to \(A_s-A_0\) and \(B_sA_s-B_0A_0\).
Their normalized actions on \(Q_0\) tend to zero in probability.
The deterministic joint fixed-program limit therefore gives exact
Hilbert-space identities at population Euler nodes:
\[
Q_1(s)=Q_0,\qquad Q_2(s)=aA_0Q_0,\qquad
Q_3(s)=a^2B_0A_0Q_0. \tag{A.11}
\]
Strong bounded-interval Euler convergence for the affine polynomial
field preserves (A.11) at every \(s\in[0,S]\). Initial Gaussian matrix
propagation then gives
\[
Q_\ell(s)\sim N(0,a^{2(\ell-1)}v_v). \tag{A.12}
\]

For \(\mathscr F_n\)-measurable \(p_n,T_n\), conditional Gaussianity gives
\[
\mathbb E[\langle p_n,T_nQ_0\rangle_n\mid\mathscr F_n]=0,\qquad
\mathbb E[\langle p_n,T_nQ_0\rangle_n^2\mid\mathscr F_n]
\le\frac{v_v}{n}\|T_n\|_{\rm op}^2\|p_n\|_n^2. \tag{A.13}
\]
Use \(T_n=I,aA_s,a^2B_sA_s\) and \(p_n=P_\ell(s)\), and also
\(p_n=\mathbf1\). Fixed-program convergence and then strong affine
Euler convergence give
\[
\mathbb E Q_\ell(s)=0,\qquad
\mathbb E[P_\ell(s)Q_\ell(s)]=0. \tag{A.14}
\]
As \(z_1^\ell=P_\ell+Q_\ell\) and
\(z_2^\ell=\tau(P_\ell-Q_\ell)\), one obtains
\[
\operatorname{Var}(z_j^\ell(s))
=\operatorname{Var}(P_\ell(s))+a^{2(\ell-1)}v_v
\ge\delta/32,\qquad j=1,2. \tag{A.15}
\]
Here \(a^4\ge1/16\) and \(v_v\ge\delta/2\). The frozen field is the
contrast for equal labels and the common field for opposite labels.

All affine preactivations are Gaussian, not merely of positive
variance. In a finite affine population Euler prefix, every forward,
reverse, and evolving field is linear in finitely many joint Gaussian
source coordinates in its layer. Inductively, the gate \(a\) is
constant, the activation is linear, unrolled rank-one memories multiply
previous fields only by deterministic scalar contractions, and each
new initialized matrix call is a Gaussian innovation plus linear
Gaussian-conditioning response terms. No product of varying neuron
coordinates occurs outside a scalar contraction. Strong Euler
convergence passes their means, covariances, and Gaussian
characteristic functions to the exact affine path.

Their means vanish: changing \(P_{1,0}\) to its negative sends
\(P_\ell,C\) to their negatives and leaves \(A,B\) fixed in (A.4).
The invariant initialization and deterministic limiting laws force
zero active means; (A.14) supplies zero inactive means. Finally,
\[
\|z_j^1\|_2\le U,\qquad
\|z_j^2\|_2\le aU^2\le U^2,\qquad
\|z_j^3\|_2\le a^2U^3\le U^3. \tag{A.16}
\]
Thus every affine marginal has form \(\nu G\), \(G\sim N(0,1)\), with
\[
m:=\sqrt{\delta/32}\le\nu\le L:=U^3. \tag{A.17}
\]

## 6. Uniform Gaussian nonaffinity and perturbative transfer

For a square-integrable real variable \(Z\) with positive variance, put
\[
\mathcal R(Z)=\inf_{\alpha,\beta}\mathbb E[
\arctan Z-\alpha-\beta Z]^2
=\operatorname{Var}(\arctan Z)
-\frac{\operatorname{Cov}(Z,\arctan Z)^2}{\operatorname{Var}(Z)}.
\]
Define a constant depending only on \(\delta\):
\[
\eta_\delta=\min_{m\le\nu\le L}\mathcal R(\nu G)>0. \tag{A.18}
\]
Coupling by the same \(G\), boundedness and Lipschitzness of arctangent,
and the denominator bound \(m^2\) show continuity on this compact
interval. Zero residual would identify arctangent with an affine
function Gaussian-almost everywhere. Positive density and continuity
would then extend the identity to all of \(\mathbb R\), contradicting
the nonconstant derivative. Thus the minimum is positive and
\[
\inf_{a\in[1/2,1]}\ \inf_{j,\ell,s\le S}
\mathcal R(z_{j,a,0}^\ell(s))\ge\eta_\delta. \tag{A.19}
\]
The endpoint \(S\) in each term is that affine reference's own endpoint.

The transfer estimate needs no Gaussianity of the perturbed variable.
Suppose \(\|Z-Z_0\|_2\le t\),
\(\operatorname{sd}(Z_0)\ge m\), and
\(\mathcal R(Z_0)\ge\eta_\delta\). Then
\[
t\le t_\delta:=
\min\left\{m/2,\frac{\sqrt{\eta_\delta}}{2(1+\pi/m)}\right\}
\quad\Longrightarrow\quad \mathcal R(Z)\ge\eta_\delta/4. \tag{A.20}
\]
Indeed centering is an orthogonal projection, so standard deviation is
1-Lipschitz and \(\operatorname{sd}(Z)\ge m/2\). The optimal slope for
regressing \(\arctan Z\) on \(Z\) has absolute value at most
\(\operatorname{sd}(\arctan Z)/\operatorname{sd}(Z)\le\pi/m\).
Using its intercept and slope as a competitor for \(Z_0\) gives
\[
\sqrt{\mathcal R(Z_0)}
\le\sqrt{\mathcal R(Z)}+(1+\pi/m)t,
\]
proving (A.20). Absorbing \(aZ\) into the free affine approximant gives
the exact identity
\[
\inf_{\alpha,\beta}\mathbb E[
\phi_{a,e}(Z)-\alpha-\beta Z]^2=e^2\mathcal R(Z). \tag{A.21}
\]
Consequently a separately proved comparison
\(\|z_{j,a,e}^\ell-z_{j,a,0}^\ell\|_2\le Je\), uniform on these
reference intervals with \(J\) depending only on \(\delta\), gives
the uniform positive activation-regression margin
\(e^2\eta_\delta/4\) whenever \(0<e\le t_\delta/J\).
The constants in (A.6), (A.7), (A.17), (A.18), and (A.20) precede the slope,
dataset, labels, dimension, width, and physical horizon.


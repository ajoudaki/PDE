# Explicit fitting for every original-clock Legendre order

2026-10-04. New deterministic bridge, awaiting a separate check. This extends
the numerical dense fitting interface to every order of the manuscript's
actual autonomous closure. It uses the complete projection/fitting argument
in `paper/proof_alltime.tex`, with numerical constants, and the initialization
event proved in `GENERAL_EXPLICIT_FITTING.md`. It changes neither algorithm.

## 1. Setup and explicit constants

Use the canonical model, mean-loss mobilities, initialization, sphere data,
and original RMS-clock Legendre equations in `GENERAL_LEGENDRE_TRANSFER.md`
§§1–2. In particular the hidden matrices are reconstructed from moments,
not independently learned. Let

\[
Y=\|y\|_2/\sqrt m,\qquad \lambda=\gamma/m,
\quad \gamma=\lambda_{\min}(Q_L)>0.
\]

For the layerwise activations put
\[
b=\max_\ell|\phi_\ell(0)|,\quad
s=\max(1,\max_\ell\|\phi_\ell'\|_\infty),\quad
H=\max(1,\sqrt{q_1},\ldots,\sqrt{q_L}),
\]
where \(q_0=1\) and
\(q_\ell=\mathbb E\phi_\ell(\sqrt{q_{\ell-1}}Z)^2\),
\(Z\sim N(0,1)\). Thus \(\lambda\le H^2/m\le H^2\).
The real argument needs bounded slope and locally Lipschitz derivative;
the explicit Gaussian initialization event additionally uses the bounded
second derivative in the dense note. Activation values may be unbounded.

Define the finite recurrences
\[
D_\ell=s(9s)^{L-\ell},\quad D=D_1,
\quad C_1=4s^2D_1^2,
\]
\[
C_\ell=3s^2(64H^4D_\ell^2+82C_{\ell-1}),\quad
C=\sqrt{C_L},\quad
E=130\sum_{\ell=2}^L D_\ell\sqrt{C_{\ell-1}}.
\tag{1}
\]
All these quantities are positive; \(C_\ell\) is increasing. Set
\[
S_* =\min\left\{1,\frac1{64H^2D},
\frac1{\sqrt{8C}},
\left(\frac1{8H^2DE}\right)^{2/7}\right\}.
\tag{2}
\]

Suppose that initialization satisfies
\[
\|A_0\|_{\rm op}/\sqrt n\le8,\quad
\max_{\ell\ge2}\|W_0^\ell\|_{\rm op}\le8,\quad
\sup_{\|v\|=1,\ell}\|h_0^\ell(v)\|_2/\sqrt n\le3H/2,
\quad H_{L,0}^{\mathsf T}H_{L,0}/(mn)\succeq\lambda I/2.
\tag{3}
\]
The explicit \(N_{\rm fit}(\delta)\) in the dense note proves (3) with
probability at least \(1-\delta\) for every \(n\ge N_{\rm fit}(\delta)\).

**Claim.** If
\[
\boxed{Y\le\frac{\gamma}{8m}S_*,}
\tag{4}
\]
then, on (3), simultaneously for every positive integer order \(q\), the
original autonomous closure exists uniquely for all time, fits, and has
convergent physical parameters. If \(Y=0\) it is stationary. For \(Y>0\), set
\[
S=8Y/\lambda,\quad R=8Y/\sqrt\lambda=S\sqrt\lambda,
\quad\kappa=\lambda/4.
\tag{5}
\]
The bounds are
\[
\rho(t)\le Ye^{-\kappa t},\quad
\int_t^\infty\rho\le\rho(t)/\kappa,\quad
\|w(t)\|_2/\sqrt n\le R/2,
\tag{6}
\]
\[
\|A(t)\|_{\rm op}/\sqrt n<9,\quad
\max_{\ell\ge2}\|\widehat W^\ell(t)\|_{\rm op}<9,\quad
\sup_{\|v\|=1,\ell}\|\widehat h^\ell(t,v)\|_2/\sqrt n<2H,
\quad \widehat\Gamma_w(t)\succeq\lambda I/4.
\tag{7}
\]
The bounds use (5), even though the realized total activity is at most
\(S/2\). They are independent of order and width.

## 2. Numerical projection bounds

For shifted Legendre projection \(\Pi_q^A\), the manuscript proves
\[
\|(I-\Pi_q^A)u\|_{L^2}^2
\le\frac1{q(q+1)}\int_0^A\xi(A-\xi)\|u'\|^2d\xi,
\]
\[
\|u(A)-(\Pi_q^Au)(A)\|
\le\sqrt{A/(3q)}\,\|u'\|_{L^2}.
\tag{8}
\]
The second bound follows from the exact multiplier
\((p_q+p_{q-1})/2\), whose squared norm is
\(A[(2q+1)^{-1}+(2q-1)^{-1}]/4\le A/(3q)\).
One may take the following conservative numerical endpoint norm:
\[
\| (\Pi_q^A b)(A)\|\le64\sqrt q\,\|b\|_{L^\infty}.
\tag{9}
\]
Here is a numerical verification. For the ordinary Legendre polynomial,
\(v(\theta)=\sqrt{\sin\theta}P_k(\cos\theta)\), the energy
\(v^2+(v')^2/[(k+1/2)^2+(4\sin^2\theta)^{-1}]\) increases on
\((0,\pi/2)\). Its central-binomial endpoint formulas bound that energy
by \(4/k\) for \(k\ge1\). On \([1/k,\pi/2]\) this gives
\[
|\partial_\theta P_k(\cos\theta)|
\le 3\sqrt k(\sin\theta)^{-1/2}
       +2k^{-1/2}(\sin\theta)^{-3/2}.
\]
Using \(\sin\theta\ge2\theta/\pi\), the integral of the first term
is at most \(3\pi\sqrt k\); that of the second is at most
\(4(\pi/2)^{3/2}\le8\). The interval \([0,1/k]\) contributes at
most \((k+1)/(4k)\le1/2\), by \(|P_k'|\le k(k+1)/2\).
Reflection thus gives \({\rm Var}(P_k)\le36\sqrt k\).
The endpoint kernel is \((p_q'+p_{q-1}')/2\), so its \(L^1\) norm
is at most \(36\sqrt q\); (9) follows. The cases \(k=1,q=1\)
also satisfy the bounds directly. These arguments apply to Hilbert-valued
histories by integrating the scalar kernel against the vector.

## 3. Closed bootstrap

Stop at activity \(S\), readout norm \(R\), any operator boundary in
(7), or any sphere-feature boundary \(2H\). Before the stop,
\(\|\delta_a^\ell\|/\sqrt n\le D_\ell R\).
Projection contraction in the reconstruction gives
\[
\|\widehat W^\ell-W_0^\ell\|_F
\le4HD_\ell R\sqrt{(1+S)S},\quad
\|A-A_0\|_F/\sqrt n\le2DRS.
\tag{10}
\]
The first and second bounds are strictly below one under (2), since
\(\sqrt\lambda\le H\). Thus the operator boundaries cannot be reached.

Let \(Z_\ell\) be the supremum, over all sphere queries, of the normalized
clock derivative energy of the layer's forward history, including its
constant unit prefix. The exact defect is
\[
E_\ell(t)=\frac{2\rho}{mn}\sum_a
(b_a^\ell-b_a^{\ell,*})(h_a^{\ell-1}-h_a^{\ell-1,*})^{\mathsf T},
\quad b_a^\ell=(r_a/\rho)\delta_a^\ell.
\tag{11}
\]
The same symbol \(E\) without a subscript denotes the scalar in (1).
Endpoint polynomial evaluation and the growing projection-error identity
give
\[
\int_0^t\rho\|E_\ell/\rho\|_F^2du
\le2(1+S)^2D_\ell^2R^2 Z_{\ell-1}.
\tag{12}
\]
Indeed the backward endpoint error in sample RMS is at most
\((q+1)D_\ell R\); the integrated squared forward endpoint error is
its final projection error, at most
\((1+S)^2 Z_{\ell-1}/[4q(q+1)]\). Cauchy–Schwarz in the sample average
and \((q+1)/q\le2\) prove (12). This works equally for the supremum
over query energies; the backward history in (11) uses only training data.

The first-layer chain rule and the later-layer three-term square inequality
now give
\[
Z_1\le4Ss^2D_1^2R^2,
\]
\[
Z_\ell\le3s^2\{64SH^4D_\ell^2R^2+
[81+32H^2D_\ell^2R^2]Z_{\ell-1}\}
\le C_\ell S R^2.
\tag{13}
\]
For the last inequality use
\(32H^2D_\ell^2R^2\le32H^4D^2S^2<1\), by (2).
Consequently every sphere feature moves at most
\(\sqrt{S Z_\ell}\le CSR=CS^2\sqrt\lambda\).
This is at most \(\sqrt\lambda/8\), and at most \(H/8\).
It excludes the feature boundary and changes the top training feature
matrix, normalized by \(\sqrt{mn}\), by at most \(\sqrt\lambda/8\).
The smallest singular value is therefore at least
\((1/\sqrt2-1/8)\sqrt\lambda>\sqrt\lambda/2\), proving the gap in (7).

Combining (8), (9), and (13) in (11), with sample Cauchy–Schwarz, yields
\[
e_E(t):=\sum_{\ell=2}^L\|E_\ell(t)\|_F
\le E\sqrt S R^2\rho(t).
\tag{14}
\]
The factor 130 bounds \(2\cdot65\sqrt{2/3}\). No coordinate maximum,
bound on activation values, or factor \(\sqrt m\) is used here.
The ordinary prediction Jacobian satisfies
\[
\|JE\|_m\le2HDR e_E
\le 2HDE S^{7/2}\lambda^{3/2}\rho
\le\lambda\rho/4.
\tag{15}
\]
Thus \(\dot r=-2\Gamma r+JE\), \(\Gamma\succeq\Gamma_w\), gives
\(\dot\rho\le-\lambda\rho/4\). In particular activity is at most
\(4Y/\lambda=S/2\), with the tail inequality in (6).

To close the readout boundary, use the genuine dense gradient field \(F\)
evaluated at the reconstructed state. In the parameter norm
\[
\|U\|_{\rm par}^2=\|U_A\|_F^2/n+
\sum_{\ell\ge2}\|U_{W^\ell}\|_F^2+\|U_w\|_2^2/n,
\]
its energy identity is
\[
-\frac d{dt}\rho^2=\|F\|_{\rm par}^2-2\langle r,JE\rangle_m
\ge\tfrac12\|F\|_{\rm par}^2.
\tag{16}
\]
Indeed \(\|F\|_{\rm par}^2=4\langle r,\Gamma r\rangle_m
\ge\lambda\rho^2\), whereas the last term has magnitude at most
\(\lambda\rho^2/2\). Weighted integration with \(e^{\kappa t}\),
using \(\rho\le Ye^{-\kappa t}\), gives
\(\int e^{\kappa t}\|F\|_{\rm par}^2dt\le4Y^2\).
Weighted Cauchy–Schwarz then gives
\[
\int_0^\infty\|F\|_{\rm par}dt\le2Y/\sqrt\kappa
=4Y/\sqrt\lambda=R/2.
\tag{17}
\]
The readout equation has no defect, so (17) excludes its boundary.
All stops have strict margins. Local uniqueness excludes finite arrival
at a zero-residual equilibrium for a nonstationary solution. The moment
integral formulas and \(1\le\tau\le1+S\) give continuation at fixed
\(n,q\). Finally (14), (17) show finite physical path length and hence
convergent parameters and predictors. Exponential residual decay makes
the endpoint interpolating.

## 4. Explicit outputs for the comparison interface

Define
\[
T_1=2DR,\qquad
T_\ell=4HD_\ell R+130D_\ell\sqrt{C_{\ell-1}S}\,R^2
\quad(\ell\ge2),
\]
\[
V_1=sT_1,\qquad V_\ell=s(2HT_\ell+9V_{\ell-1}).
\tag{18}
\]
Then \(\|\dot W^\ell\|_F\le T_\ell\rho\), with the first block
normalized by \(\sqrt n\), and all query feature speeds are at most
\(V_\ell\rho\) in normalized Euclidean norm. Therefore the comparison
input \(V_h\) can be taken as \(\max_\ell V_\ell\).
Put
\[
G=(2H)^2+D_1^2R^2+4H^2R^2\sum_{\ell=2}^L D_\ell^2.
\]
Since the mean tangent Gram has operator norm at most its trace \(G\),
\(\|\dot r\|_m\le(2G+\lambda/4)\rho\) and hence
\[
\|\dot c\|_m\le 4G+\lambda/2,
\quad c=r/\rho.
\tag{19}
\]
These constants close the previously numerical physical-tube interface
in `GENERAL_LEGENDRE_TRANSFER.md` §6. They do not by themselves prove the
probabilistic trained-carrier bound needed for the near-quarter order.

## 5. Relation to the proposed activation envelope

Use exactly the fully defined strip envelope \(\beta_\partial\ge10\)
in the dense fitting note. It satisfies \(b,s\le\beta_\partial\), and
\(H\le(2\beta_\partial)^L\le\beta_\partial^{3L/2}\).
The deliberately loose bounds
\[
D\le\beta_\partial^{2L},\quad C\le\beta_\partial^{8L},\quad
E\le\beta_\partial^{12L}
\]
follow from (1): \(246s^2\le\beta_\partial^5\), and the resulting
geometric recurrence has at most \(L\) terms, with \(L\le\beta_\partial^L\).
Substitution into every term of (2), for \(L\ge2\), gives
\(S_*\ge\beta_\partial^{-8L}\). Consequently the simple sufficient cap
\[
\boxed{Y\le\frac\gamma m\,\beta_\partial^{-10L}}
\tag{20}
\]
implies (4). This numerical cap is only for physical fitting and the
deterministic comparison interface. The full probabilistic source proof
can require a smaller explicit cap; (20) does not settle that separate
obligation.

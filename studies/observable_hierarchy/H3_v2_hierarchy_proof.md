# A dense closure with a small polynomial core

This is a proof candidate for the exact bias-free tanh model of C.4.7.8.
Its finite numerical realization is treated separately. Set T=1/200 and fix
one represented two-arc law from the short-time proposition. The proposition
constructs its canonical population GF (w,K,c), with A=A0+K, by finite common
Gaussian programs, proves its individual reverse-query tails and identifies
it with the actual finite-network GF retaining its random initial readout.
No finite-network approximation is used to run the closure.

The bounded initialized-word grammar consists of the constants on both
populations, first-population Gaussian seeds g1,g2, rational linear
combinations, sin/cos/tanh of permitted words, products of bounded words on
one population, and A0 or its actual adjoint on bounded operands. The
population type determines the orientation. Let the natural-number coding
be exactly C.4.7.9's coding: 0,1 are the two constants; 2,3 are g1,g2; for
n=4+8k+j, j=0,1,2,3 applies sin,cos,tanh,action to code k; for j=4,5,7,
unpair k by Cantor pairing and use addition, bounded product, addition;
for j=6, the first unpaired integer specifies a rational coefficient and the
second its operand. Type-invalid expressions are rejected. If the rational
index unpairs as (a,b), its numerator is 0 for a=0, (a+1)/2 for odd a,
and -a/2 for even positive a, and its denominator is b+1. This enumerates
every permitted finite word. Envelopes are exact rational metadata, never
rounded to float to decide boundedness. Literal syntax duplicates are shared;
no numerical or algebraic rank deletion is used.

Use h_i=tanh(g_i), xi_i=A0 h_i, H_i=tanh(xi_i), p_i=A0* H_i, for i=1,2.
With G a standard scalar Gaussian, set

\[
 v=E\tanh^2G,\quad \alpha=E[1-\tanh^2(\sqrt vG)],
 \quad \tau_0=E\tanh^2(\sqrt vG).
\]

All three constants are strictly positive. Oddness and independence give
E[h_i h_j]=v delta_ij. The complete finite-source rule of C.4.7.8 therefore
realizes the forward sources as independent N(0,v) variables and gives

\[
 p_i=\zeta_i+\alpha\tanh g_i,
 \qquad (\zeta_1,\zeta_2)\sim N(0,\tau_0 I_2),
\]

independently of g. Here E[partial_(xi_j)H_i]=alpha delta_ij; this is the
response term from the same reused action. The two population measures are
separate, and their quadrature indices are not paired across populations.

Put X1=(tanh g1,tanh g2,tanh p1,tanh p2) and X2=(tanh xi1,tanh xi2).
For order N>=1 retain all products of Chebyshev polynomials

\[
 \prod_{j=1}^{d_\ell}T_{a_j}(X_{\ell,j}),\quad
 a_j\ge0,\quad\sum_j a_j\le N,\qquad d_1=4,\ d_2=2,
\]

and append every bounded valid code through N not already present literally.
Use total degree followed by descending lexicographic exponent order for the
polynomial list, then increasing code order. Compiling a dependency does not
make it a retained feature. The recurrence T0=1,T1=x,T_(k+1)=2xT_k-T_(k-1)
expresses each polynomial as a bounded word. The identity T_k(cos theta)=
cos(k theta), obtained by induction from the cosine addition formula, proves
its absolute bound one on [-1,1].

The conditional Gaussian density of (g,p) is positive everywhere on R4.
The coordinatewise tanh diffeomorphism gives X1 a positive density on the
open four-cube; X2 similarly has a positive density on the open two-cube.
A polynomial zero almost surely is zero on that cube by continuity, and
is the zero polynomial by successively applying the one-variable root
property to every variable. The listed products have distinct leading
monomials and span all polynomials of total degree at most N. Their exact
span dimensions are binomial(N+4,4) and binomial(N+2,2). At N=1,2,3 the
appended code prefix contributes no new bounded word. The dimensions are
therefore (5,3), (15,6), (35,10), with strict enrichment in both populations.

Strict raw-span enrichment alone need not add a direction used by a particular
trajectory. For example, the new quadratic core features are even under the
joint core sign reversal, whereas the initialized hidden fields are odd.
Operational comparisons can therefore use the odd degrees N=1,3,5. Their
full retained counts are (5,3), (35,10), (128,21): the last first-population
list has 126 polynomial features and also the two syntactically distinct
constant tail words sin(1),cos(1). Those harmless duplicate functions are
retained according to the declared rule, rather than deleted by rank.

These odd degrees add initialized action information beyond the previous
upper span. To verify this exactly, let H=tanh(xi_1) and, for k=3 or 5,
let P_k be the monic degree-k polynomial orthogonal to lower-degree
polynomials for the law of H. The positive density on (-1,1) makes its
moment Gram positive definite, so it exists uniquely. Symmetry makes P_k
odd. It has k distinct roots in (-1,1): otherwise multiply it by the
product of its fewer-than-k sign-changing interior roots. The resulting
function has a fixed nonzero sign off finitely many points, contradicting
orthogonality to that lower-degree product. Interpolate artanh at those
k roots by a polynomial L of degree at most k-1. Repeated Rolle's theorem
gives, at every other x in (-1,1),

\[
 P_k(x)[\operatorname{artanh}(x)-L(x)]
 =\frac{\operatorname{artanh}^{(k)}(\xi_x)}{k!}P_k(x)^2>0,
\]

because for odd k,
artanh^(k)(x)=(k-1)![(1-x)^(-k)+(1+x)^(-k)]/2>0.
The product is integrable, since artanh(H)=xi_1 is Gaussian and P_k is
bounded. Orthogonality to L therefore gives E[P_k(H)xi_1]>0. Independence
of H1,H2 also makes P_k(H1) orthogonal to every previous upper polynomial
of total degree at most k-2. Nevertheless

\[
 E_2[P_k(H_1)A_0h_1]=E[P_k(H_1)\xi_1]>0.
\]

The same quantity is E1[(A0*P_k(H1))h1] by actual adjunction. Thus the
newly retained directions carry nonzero action information in the very
coupling used by the closure. This is a structural enrichment claim; it
does not assert an accuracy ordering between two finite degrees.

For polynomial-core features F(X1),B(X2), all initialized action contractions
reduce to bounded integrals in four and two independent scalar Gaussians:

\[
 E_2[B A_0F]=\sum_{i=1}^2
 E_1[Fh_i]E_2[\partial_{\xi_i}B]
 +\sum_{i=1}^2 E_1[\partial_{\zeta_i}F]E_2[BH_i].       \tag{H3.1}
\]

Indeed append A0F after the two reverse probes. Its source response is
sum_i E1[partial_(zeta_i)F]H_i, and its centered source has covariance
E1[Fh_i] with xi_i. Subtracting sum_i(E1[Fh_i]/v)xi_i leaves a centered
Gaussian independent of the old forward pair, including when its variance
is zero. Its product with B has expectation zero. Finally Gaussian
integration by parts gives E[B xi_i]=v E[partial_(xi_i)B]: the Gaussian
density derivative is -xi_i/v, the bounded B makes the boundary term zero,
and its derivative is bounded at fixed degree. Fubini applies. These steps
prove (H3.1). An innovation is integrated out of this contraction, not
deleted from a joint action law. The formula also applies to a retained
bounded smooth tail depending only on the same core coordinates. A new
action requires the full finite-source compiler, as in the numerical proof.

Let psi_l,N be the entire raw feature column, G_l,N=E[psi psi^T], and set
eta_N=1/[1024(N+1)^2]. Define lower Cholesky L_l,N by
G_l,N+eta_N I=L_l,N L_l,N^T, and b_l,N=L_l,N^-1 psi_l,N. If U_l,N
maps a coefficient vector to b_l,N^T times that vector, then

\[
 U_{\ell,N}^*U_{\ell,N}
 =I-\eta_N L_{\ell,N}^{-1}L_{\ell,N}^{-T}\le I,
 \qquad
 Q_{\ell,N}=U_{\ell,N}U_{\ell,N}^*
 =S_{\ell,N}(G_{\ell,N}+\eta_NI)^{-1}S_{\ell,N}^*,      \tag{H3.2}
\]

where S maps raw coefficients to psi^T times the vector. In particular Q is
a positive contraction. Its raw spans are nested and dense in the initialized
observable spaces: every bounded code eventually appears, and the rational
word/Fourier-cylinder density argument of C.4.7.9 applies without alteration.
For completeness the only filter estimate needed is, for a fixed raw-span
vector S a embedded at all later orders,

\[
 \|(I-Q_N)S_N a\|^2
 =\sum_j\frac{\eta_N^2\lambda_j}{(\lambda_j+\eta_N)^2}|a_j|^2
 \le\frac{\eta_N}{4}|a|^2.
\]

Here diagonalize the positive raw Gram and use
lambda/(lambda+eta)^2<=1/(4eta). Approximate any initialized observable-space
vector by a fixed raw-span vector and use ||I-Q_N||<=1. This proves Q_N→I
strongly. The initialized observable spaces contain the exact trajectory:
C.4.7.9 proves invariance by finite Euler word approximation followed by its
strong completion. The short-time proposition supplies exactly that strong
completion and tails for the present fixed family, so the same argument
applies on [0,T]. No assumption that the finite Gaussian core alone generates
the full spaces is made.

Set D_N=U_2,N* A0 U_1,N. The raw contraction C from (H3.1) or the full
source program gives D_N=L_2,N^-1 C L_1,N^-T; the right transpose is required.
Use the complete nonlinear equations of C.4.7.9 with these features and D_N.
This inverse-Cholesky choice is equivalent to symmetric whitening: if
R=G+eta I and O=L^-1 R^(1/2), then OO^T=I and b=O b^s. Transform
M=O2 M^s O1^T, a=O1 a^s, d=O2 d^s. Predictions, both action orientations,
row/readout equations and the Frobenius middle gradient all agree.

Here is the compatibility with the identical population GF, including the
change in dictionary and ridge. Lift the exact finite-order equations to the
fixed canonical carrier and put

\[
 B_N=Q_{2,N}A_0Q_{1,N},\qquad
 K_N=U_{2,N}(M_N-D_N)U_{1,N}^*.
\]

Their current action is B_N+K_N. The middle equation is exactly the rank
equation with Q2 and Q1 on its two factors. Energy differentiation uses the
same population pairings as the dynamics, so the unhalved loss is at most
one, ||c_N||_infty<=2t, ||M_N-D_N||_F<=2t^2, and ||K_N||_HS<=2t^2.
The operator bound on A0 and (H3.2) give ||B_N||<=2, uniformly in N.

Both B_N and its adjoint converge strongly to A0 and its adjoint. For example,
subtract Q2 A0(Q1 v-v)+(Q2-I)A0v and use boundedness and strong convergence.
Strong convergence of uniformly bounded operators is uniform on a compact
set, by a finite epsilon-net and the triangle inequality. Applied to the
continuous exact trajectory's compact (t,u) images h1 and delta2, this gives
the first two vanishing terms in

\[
 \epsilon_N=\sup_{t,u}\|(B_N-A_0)h^1(t,u)\|_2
 +\sup_{t,u}\|(B_N^*-A_0^*)\delta^2(t,u)\|_2
 +\sup_t\|Q_{2,N}\dot K(t)Q_{1,N}-\dot K(t)\|_{\rm HS}\to0. \tag{H3.3}
\]

For the last term approximate each HS operator by a finite sum of rank-one
operators. Strong convergence handles their finitely many factors; contractions
bound the discarded HS remainder. The same finite-net argument makes this
uniform on the compact image of the continuous exact derivative dot K.

Let e_N be the sum of row L2, middle HS and readout L2 distances. The
one-reference comparison in C.4.7.9 applies: its derivation uses precisely
the uniform bounds just checked, both strong action directions, and the
HS projection source in (H3.3). Splitting the exact reference reverse query
at magnitude s controls its multiplier, giving

\[
 D^+e_N(t)\le C(1+s)(e_N(t)+\epsilon_N)+C\tau(s),\qquad e_N(0)=0,
\]

where C is independent of N,s and the short-time proposition gives
tau(s)<=C0 exp[-c0(s-D0)^2]. This is the same estimate proved there for the
filtered closure; no tail bound on numerical or projected trajectories is
inserted as an assumption. Integrating the scalar inequality yields
sup_t e_N<=CT exp[C(1+s)T]((1+s)epsilon_N+tau(s)). First N→infinity at
fixed s and then s→infinity proves raw convergence, since a negative
quadratic dominates the positive linear exponent.

Direct subtraction of f=E[c tanh(A tanh(w·u))], using the action/row/readout
bounds and |tanh'|<=1, now proves sup_(t,u)|f_N-f_mu|→0. The same
subtraction for the initial and current hidden activations gives uniform
(t,u) L2 convergence in each population; initial upper activations use
B_N tanh(g·u) and converge by compact-target strong convergence. Keeping
initial and current values on the same carrier gives joint-pair W2 convergence.
Integrating against the fixed training law preserves it. RMS displacement
converges because it is the L2 norm of the difference of the two paired
activations and the reverse triangle inequality bounds changes of that norm.
The supported family and T have remained fixed throughout all limits.

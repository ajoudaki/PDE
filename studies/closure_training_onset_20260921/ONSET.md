# What canonical training initially learns

## 1. Model, initialization and what is selected

Use the book's fixed-order two-hidden-tanh population closure. Inputs are
u=(cos theta,sin theta), with the normalization u=x/sqrt(2). Let nu be the
input marginal of a probability training law and m(u)=E[y|u], with |y|<=Y.
All gradients of squared loss depend on the labels through m. The loss is
the unhalved expectation E[(f(u)-y)^2]. Each hidden population has its own
expectation; the read-in/readout metric is population L2 and the M metric
is ordinary Frobenius.

At each fixed p the bounded feature columns b_1,b_2 are frozen functions of
the initialized Gaussian marks. Their joint laws, including their relation
with the initial read-in G, are retained. For raw features psi_l define

\[
L_lL_l^T=E_l[\psi_l\psi_l^T]+\eta_p I,\quad b_l=L_l^{-1}\psi_l,
\quad \eta_p=\frac1{1024(p+1)^2},
\quad D_p=L_2^{-1}C_pL_1^{-T},
\quad C_p=E_2[\psi_2(A_0\psi_1)^T].
\tag{1}
\]

The canonical initial state is w(0)=G,c(0)=0,M(0)=D_p. In particular, M is
not chosen to fit a target. Its deterministic entries are specified Gaussian
initialization contractions. At p<=3 the polynomial-core source/response
formula (H3.1) evaluates them, including both orientations of the same
initialized action A_0. At higher orders a retained word requiring a new
action uses the full finite-source rule of Section 3, not H3.1 alone.

For comparison, deliberately coupling a lower feature h_1 to an upper
polynomial P has raw coefficient matrix K=t r_P e_{h_1}^T, where
psi_2^T r_P=P, and normalized matrix M=L_2^T K L_1. That is a selected static
matrix direction. It is not D_p and supplies no claim of training selection.

At a current state set

\[
h(u)=\tanh(w\cdot u),\ a(u)=E_1[b_1h(u)],\ Z(u)=b_2^TMa(u),
\ H(u)=\tanh Z(u),\ f(u)=E_2[cH(u)],
\]
\[
d(u)=E_2[b_2c(1-H(u)^2)],\quad q(u)=b_1^TM^Td(u).
\]

The actual gradient-flow equations, in physical time, are

\[
\dot c=2\int(m-f)H\,d\nu,\quad
\dot M=2\int(m-f)d\,a^T\,d\nu,\quad
\dot w=2\int(m-f)(1-h^2)q\,u\,d\nu.
\tag{2}
\]

## 2. The first selected function

Subscript zero denotes evaluation at (G,0,D_p). Define

\[
S=\int m(v)H_0(v)\,d\nu(v),\qquad
\mathcal K(u,v)=E_2[H_0(u)H_0(v)],\quad
(\mathcal Km)(u)=\int\mathcal K(u,v)m(v)\,d\nu(v).
\]

Because c_0=0, one has d_0=q_0=0. Substitution in (2) gives

\[
\dot c_0=2S,\qquad \dot w_0=0,\qquad \dot M_0=0,
\qquad \dot f_0(u)=2(\mathcal Km)(u).
\tag{3}
\]

For finite data (u_a,y_a) of weights omega_a, the selected first function is
2 sum_a omega_a y_a E[H_0(u)H_0(u_a)]. This is a whole-circle function,
not a choice of readout or M made after specifying a desired waveform.
The kernel is the closure's own initialized kernel; it is generally not the
full dense Gaussian network's kernel. It is exactly the entire initial
tangent kernel because the other two trainable blocks initially have zero
prediction derivatives when c=0.

The initial loss slope is -4<m,mathcal K m>_{L2(nu)}=-4E_2 S^2. This supplies
an exact task-dependent comparison between orders, not a presumed ordering
of their slopes. Both kernels and targets are necessary for that comparison.

## 3. First hidden motion and the cubic prediction correction

Put s(u)=1-h_0(u)^2, g(u)=1-H_0(u)^2 and

\[
B(u)=E_2[b_2Sg(u)].
\]

Differentiating d at zero gives dot d_0(u)=2B(u). Differentiating (2), terms
containing d_0 or q_0 vanish, leaving the accelerations

\[
N:=\ddot M_0=4\int m(v)B(v)a_0(v)^T\,d\nu(v),
\]
\[
W:=\ddot w_0=4\int m(v)s(v)
[b_1^TD_p^TB(v)]v\,d\nu(v).
\tag{4}
\]

These are fixed Gaussian initialization contractions and data integrals.
In particular, on finite data they are finite sums of initialization-based
activation, gate and dictionary expressions. No moving-state oracle enters.

Define

\[
a_2(u)=E_1[b_1s(u)(W\cdot u)],\qquad
J(u):=\ddot H_0(u)=g(u)b_2^T[Na_0(u)+D_pa_2(u)],
\]
\[
\mathcal R(u,v)=E_2[J(u)H_0(v)].
\tag{5}
\]

There are no squared first-velocity terms in (5), because dot w_0=dot M_0=0.
The adjoint R* below is with respect to the same input measure nu.
Differentiating the readout equation gives

\[
\ddot c_0=-4\int(\mathcal Km)(v)H_0(v)\,d\nu(v),
\]
\[
c_0^{(3)}=8\int(\mathcal K^2m)(v)H_0(v)\,d\nu(v)
 +2\int m(v)J(v)\,d\nu(v).
\]

The product derivative of E[cH] now gives

\[
f_t=2t\mathcal Km-2t^2\mathcal K^2m
 +t^3\left[\frac43\mathcal K^3m+
 \mathcal Rm+\frac13\mathcal R^*m\right]+O(t^4).
\tag{6}
\]

All remainders here are uniform on the circle at fixed p and fixed bounded
training law. One justification is the smooth ODE on the Banach space of
bounded increments w-G, bounded c and finite M. Fixed feature bounds, bounded
input/labels and bounded tanh derivatives give bounded Frechet derivatives
of every required fixed order on a local state ball. Picard existence and
ordinary finite-order Taylor remainders therefore apply. This is a local
finite-order result; no infinite temporal Taylor series is asserted.

The readout-only comparator with w=G,M=D_p has
f_frozen=(I-exp(-2t mathcal K))m. Its cubic coefficient is only
(4/3)mathcal K^3m. Thus the first possible feature-learning prediction term
is t^3(R+R*/3)m. Hidden and middle parameters can first move at order t^2;
their linear terms vanish. These coefficients may vanish for particular data.

There is an exact check on its sign in training loss. Directly from (4),(5),

\[
\langle m,\mathcal Rm\rangle
=\frac14\bigl(\|W\|_{L^2(\Omega_1)}^2+\|N\|_F^2\bigr).
\tag{7}
\]

For the N part substitute B=E[b_2 Sg] into E[SJ] and integrate against m:
the matrix pairing is <N,integral m B a_0^T>=||N||^2/4. For the W part,
substitute a_2=E[b_1s(W dot u)] and reverse the finite/integrable pairings;
the result is E[W dot integral m s(b_1^TD^TB)u]=||W||^2/4.
Since <m,R*m>=<m,Rm>, the loss difference is

\[
\mathcal L_{\rm full}(t)-\mathcal L_{\rm frozen}(t)
=-\frac23\bigl(\|W\|_2^2+\|N\|_F^2\bigr)t^3+O(t^4).
\tag{8}
\]

This compares each closure with its own frozen-feature counterpart. It does
not compare different p or a closure with a matched dense network. If both
accelerations vanish, no strict cubic improvement is implied.

## 4. Explicit p=1 initialization on the circle

Use the exact core h_i=tanh G_i, H_i=tanh Xi_i, Xi_i~N(0,v), and
k_i=tanh(sqrt(tau) Z_i+alpha h_i), with tau=E H_i^2, alpha=1-tau.
Let s_k=E k_i^2, beta=E h_i k_i, gamma=1-s_k, and
Sigma=[[v,beta],[beta,s_k]]. Define

\[
A(\rho)=E[\tanh X\tanh Y],\quad
B_0(\rho)=E[j(X)\tanh Y],\quad
j(x)=E_Z\tanh(\sqrt\tau Z+\alpha\tanh x),
\]

where X,Y are standard Gaussians with correlation rho. These expectations
can be evaluated by Gaussian derivative contractions. More explicitly,
with d_r=E[tanh^{(r)}G] and e_r=E[j^{(r)}G],
A(rho)=sum_{r odd}d_r^2 rho^r/r! and
B_0(rho)=sum_{r odd}e_r d_r rho^r/r!. Repeated Gaussian integration by
parts identifies the Hermite coefficients. Parseval and Cauchy–Schwarz give
absolute uniform convergence on [-1,1], since sum d_r^2/r!=v and
sum |e_r d_r|/r!<=sqrt(v E j(G)^2). The correlated-Hermite identity follows
by expanding the joint Gaussian exponential generating function; this is
not an assertion about convergence of a temporal Taylor series.

For eta=eta_1, put

\[
\Lambda(\rho)=\frac1{\tau+\eta}
(\alpha v,\alpha\beta+\tau\gamma)
(\Sigma+\eta I)^{-1}
\begin{pmatrix}A(\rho)\\B_0(\rho)\end{pmatrix}.
\tag{9}
\]

The book's exact p=1 initialization gives

\[
Z_{0,1}(\theta)=H_1\Lambda(\cos\theta)+H_2\Lambda(\sin\theta),
\quad H_{0,1}(\theta)=\tanh Z_{0,1}(\theta),
\]
\[
\mathcal K_1(\theta,\varphi)
=E[H_{0,1}(\theta)H_{0,1}(\varphi)].
\tag{10}
\]

Indeed the raw initialized action is
(G_2+eta I)^{-1} C (G_1+eta I)^{-1}; C has rows
(alpha v,alpha beta+tau gamma) on each coordinate pair, and upper Gram
tau I. This proves (9) including the reverse-response term tau gamma.
Equations (3),(9),(10) are an exact whole-circle onset predictor for any
specified data, requiring only fixed-dimensional Gaussian expectations.

## 5. Canonical middle ranks and what changes at p=3

For the polynomial-core dictionaries at p<=3 set

\[
A_i=E_1[\psi_1h_i],\quad V_i=E_1[\partial_{\zeta_i}\psi_1],
\quad U_i=E_2[\partial_{\Xi_i}\psi_2],\quad
B_i=E_2[\psi_2H_i],\quad \zeta_i=\sqrt\tau Z_i.
\]

The book's source/response contraction is exactly

\[
C_p=\sum_{i=1}^2[U_iA_i^T+B_iV_i^T].
\tag{11}
\]

Hence rank(C_p)<=4, and ridge coordinate changes preserve its rank.
At p=1 the explicit nonzero two coordinate-diagonal rows have rank two.
At p=2 the added features are even in the Gaussian marks and contribute
zero new rows/columns to C_p, so its rank is also two.

At p=3 the rank is exactly four. To prove this, first the four lower columns
[A_1,A_2,V_1,V_2] are independent: testing a linear combination at the h_j
row gives v times its A_j coefficient, while the k_j row then gives gamma
times its V_j coefficient. Both constants are strictly positive.

For the upper columns [U_1,U_2,B_1,B_2], let
P_3(H)=H^3-(EH^4/EH^2)H. It is orthogonal to H, has mean zero, and is an
available upper degree-three polynomial. Testing against P_3(H_j) kills
all but U_j; the surviving pairing is
E[P_3(H_j)Xi_j]/v>0. Here is a direct proof of strict positivity. Weight the
law of H by H^2/EH^2. The pairing E[P_3(H)atanh H] equals EH^2 times the
covariance of H^2 and atanh(H)/H under that law. Both functions are strictly
increasing in |H| on (0,1): atanh(x)/x=integral_0^1 (1-t^2 x^2)^{-1}dt.
Thus the covariance is strictly positive by the
independent-copy covariance identity. It is integrable because atanh(H)=Xi
is Gaussian. Independence eliminates cross-coordinate pairings. After the
U coefficients vanish, testing against H_j gives tau times the B_j
coefficient. Thus both rectangular factors in (11) have full column rank
four, proving rank(C_3)=rank(D_3)=4.

| p | Shape of M | Canonical initial rank |
|---|---|---|
| 1 | 3 by 5 | 2 |
| 2 | 6 by 15 | 2 |
| 3 | 10 by 35 | 4 |

These are action ranks, not ranks of the nonlinear circle kernel or Fourier
bandwidths. The outer tanh can generate infinitely many angular components.
The canonical M is fixed by (1),(11), not arbitrarily selected to expose P_3.

With exact sign symmetry and a common ridge, p=1 and p=2 canonical flows
coincide: their added even features stay inactive in the invariant odd block.
The maintained eta_1=1/4096 and eta_2=1/9216 differ, so their actual default
flows need not coincide even at the exact population level. The distinction
is normalization, not activation of the new even channels. At p=3 there
are genuinely new odd action directions, whose contribution to its initial
kernel is specified by (1),(11). Rank four is a statement about the full
retained dictionary; a particular dataset need not excite all four directions.
Neither (11) nor nested raw spans proves a positive-semidefinite ordering
between K_3 and K_1 after nonlinear activation and ridge normalization.

## 6. A cubic readout component actually appears at p=1

This is a selection calculation, not a proposed performance benchmark.
Take the balanced antipodal data u=e_1,y=1 and u=-e_1,y=-1. Equation (3)
gives dot c_0=2H_{0,1}(e_1). Since A(1)=v, B_0(1)=beta and A(0)=B_0(0)=0,

\[
H_{0,1}(e_1)=\tanh(aH_1),\qquad a=\Lambda(1)>0.
\]

For positivity note beta>0: conditional expectation of k given G is odd,
strictly increasing and has the sign of h. Also
(Sigma+eta I)^{-1}(v,beta)^T has entries
[v(s_k+eta)-beta^2,beta eta]/det(Sigma+eta I), both positive.
The row in (9) is positive, proving a>0.

Use the same initialized orthogonal polynomial P_3 as above. Under the
H^2-weighted probability law,

\[
E[P_3(H)\tanh(aH)]
=EH^2\,\operatorname{Cov}\left(H^2,\frac{\tanh(aH)}H\right)<0.
\tag{12}
\]

The ratio is extended continuously at zero. It strictly decreases with |H|:
for z>0, tanh(z)-z sech^2(z)>0, since its derivative is
2z sech^2(z)tanh(z)>0 and its value at zero is zero. The covariance sign
then follows by multiplying differences for independent copies. Thus
E[P_3(H_1)dot c_0] is nonzero at p=1. In particular training does not
keep the moving readout in the degree-one dictionary span.

For general labels the coefficient is instead
2 integral m(u) E[P_3(H_1)H_0(u)] dnu(u); it can vanish by label alignment
or symmetry. No universal emergence of that particular component is claimed.

## 7. Angular prediction and scope

On the uniform circle one may compute the Fourier matrix
Khat_mn=integral integral exp(-im theta)K(theta,phi)exp(in phi)
dtheta dphi/(2pi)^2. Equation (3) becomes
dot fhat_m(0)=2 sum_n Khat_mn mhat_n. Even input modes vanish by antipodal
oddness. One must not replace this matrix by a diagonal list of Fourier
eigenvalues without proving rotation stationarity for the finite closure.
The book explicitly does not assert that stationarity. Thus a cos(3 theta)
target need not produce a pure cos(3 theta) onset at fixed p.

The exact predictors are (3) for the leading function and (4)–(6) for the
first hidden-learning correction. They are all initialization-based Gaussian
and data contractions. They do not predict a final trained endpoint or an
order-dependent accuracy advantage without evaluating the task-specific
coefficients and controlling the relevant time interval. No numerical study
or training run is part of these conclusions.

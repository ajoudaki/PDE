# Quadratic source-space storage with an autonomous corrected readout

2026-10-04. **Internally checked deterministic source-to-runtime result.**
The independent internal reconstruction in
[STORAGE_QUADRATIC_CHECK.md](STORAGE_QUADRATIC_CHECK.md) passed at report
SHA-256 `b373ee9212997c6e60002b2cf0ad613b6b58865ab82cc9589bc70931603724d9`.
Its complete reviewed source had SHA-256
`b376b2f04da5d80ffaac2c56a1bbbd378f498bc657369cbdd834b5fafcc8993c`.
This revised version incorporates that report's exact-pair clarification,
current inherited label regime, and explicit dimension-independent tail
proof. The original candidate was frozen before exchanging conclusions.
This is a study check, not an independent promotion review or established
book result.
The construction below has total retained storage O(R²), compared with
O(R⁴) for the existing dense positive-cubature construction. It changes
the compressed training rule: the smaller network has an internal residual
state and an algebraically corrected readout, and does not follow ordinary
gradient flow. The original canonical Gaussian model is unchanged.

The construction uses the existing source theorem as an input, not as a
newly proved result. Its repository inputs are the complete
GENERAL_ANALYTIC_COMPRESSION.md, GENERAL_WEIGHTED_COMPARISON.md,
DATASET_DEPENDENCE.md, and DATASET_NORMALIZATION_ASSESSMENT.md.
No other current route was read before freezing this candidate. The only
new external theorem is the general-vector spectral sparsification theorem
specified below. No experiment or promoted-book change is involved.

## 1. Scope and input theorem

Fix the original width-n canonical model, finite compatible sphere data,
analytic bounded activations, zero initialized readout, and labels in the
existing source theorem's small-label regime. Write m for sample count,
d for input dimension, L for hidden depth, v_a=x_a/sqrt(d),
Y=||y||₂/sqrt(m), ell_n=log(en), and lambda for the capped smallest
initialized limiting top-feature eigenvalue after division by m. Constants
C below are structural unless a data dependence is written explicitly.
We retain physical training time.

Explicitly, the reference hidden layers have width n and
\(z_n^{(1)}(x)=A_nv\),
\(h_n^{(l)}(x)=\phi_l(z_n^{(l)}(x))\),
\(z_n^{(l)}(x)=W_n^{(l)}h_n^{(l-1)}(x)\), and
\(f_n(x)=w_n^\top h_n^{(L)}(x)/n\). Initialization entries of A_n are
independent N(0,1), entries of W_n^(l) are independent N(0,1/n), all
arrays are independent, and w_n(0)=0. With c_{n,a}=y_a-f_n(x_a),
its fixed reference dynamics are

\[
 \dot A_n=\frac2m\sum_a c_{n,a}\delta_{n,a}^{(1)}v_a^\top,
 \quad\dot W_n^{(l)}=\frac2{mn}\sum_a
       c_{n,a}\delta_{n,a}^{(l)}h_{n,a}^{(l-1)\top},
 \quad\dot w_n=\frac2m\sum_a c_{n,a}h_{n,a}^{(L)}.
\]

Here k_{n,a}^(L)=w_n, delta_{n,a}^(l)=phi_l'(z_{n,a}^(l)) multiplied
coordinatewise by k_{n,a}^(l), and
k_{n,a}^(l)=W_n^(l+1)ᵀ delta_{n,a}^(l+1). These are the squared-mean-loss
equations with the canonical mobilities (n,1,...,1,n).

The source theorem supplies, from initialization alone, spaces
S_l contained in R^n with dimensions at most R, approximating to coordinate
error epsilon the actual reference features h^(l)(t,x), backward responses
delta_a^(l)(t), and their paired W_0 forward and transpose images, through
T=C lambda^-1 ell_n, uniformly on the query sphere. Every member of a
paired approximation has its own coordinate error bound. Include initial
training features, their forward images, and the columns of A_0 exactly,
as in the existing theorem. Add the constant vector to each S_l.

We use the source accuracy epsilon=n^-1. The existing dimensional bound is

\[
 R\le C\{\lambda^{-1}(\ell_n^a+m\ell_n^b)+d\},\qquad
 a=d(L+5)+1,\quad b=L+6.                                      \tag{1}
\]

On the same event the reference residual RMS rho_n(t) obeys
rho_n(t)<=Y exp(-c lambda t), its total activity is at most
S=C Y/lambda, its layer operator norms and parameter RMS norms are bounded,
and its coordinate carrier maximum on [0,T] obeys

\[
 M:=\max\{1,\max_{a,l,i,t\le T}|k_{a,i}^{(l)}(t)|\}
       \le 1+CS\sqrt{\ell_n}.                               \tag{2}
\]

The source assumptions already imply S is bounded by a sufficiently small
structural constant. The current internally checked inherited sufficient
regime is

\[
                         0<Y\le c\lambda,
\]

from [LABEL_SEPARATE_BUDGETS.md](LABEL_SEPARATE_BUDGETS.md), independently
reconstructed in
[LABEL_SEPARATE_BUDGETS_CHECK.md](LABEL_SEPARATE_BUDGETS_CHECK.md), report
SHA-256 `96f9766dc398b08b229581e64eb6590298b4ff95aaa4a7a7fac492cf29c2e059`.
It supersedes the extra exp(-C sqrt(log(em))) factor of
DATASET_MAXIMUM_REFINEMENT.md. The deterministic runtime requires the
same structural condition and introduces no additional label penalty.
Any separately verified enlargement of the source regime passes through
this bridge unchanged. Y=0 has the exact constant-zero representation.

## 2. O(R) selected coordinates with exact source inner products

Choose U_l with columns spanning S_l and U_l^T U_l/n=I. We first discuss
one layer and suppress l. Let r=dim S. Apply the following specialization
of Batson--Spielman--Srivastava's general-vector theorem: if
sum_i q_i q_i^T=I_r, nonnegative coefficients s_i exist, with at most 9r
positive coefficients, such that

\[
 I_r\preceq\sum_i s_iq_iq_i^\top\preceq4I_r.
\]

This is Theorem 3.1 with its sparsity parameter equal to 9 in
[the authors' paper](https://www.cs.cmu.edu/~odonnell/hits09/batson-spielman-srivastava-twice-ramanujan-sparsifiers.pdf).
Its hypotheses hold with q_i=U_{i,:}^T/sqrt(n). Retain its positive support
I and set N=|I|<=9r, P=U_I, and D=diag(s_i/n) on that support. Thus
G=P^TDP has spectrum in [1,4]. Since the constant vector belongs to S,
1<=1^TD1<=4. The theorem is constructive; its preprocessing cost is outside
the existing exact-real resource contract.

The complete proof of Theorem 3.1 was inspected, including the
Sherman--Morrison preliminary, both barrier-shift lemmas, the averaging
lemma, its Cauchy--Schwarz subclaim, and the final barrier parameter choice
(Sections 2.3 and 3.2, printed pages 5 and 9--15). In the specialization
used here the parameters are lower shift 1, upper shift 2, lower potential
1/3, upper potential 1/6, and initial barriers -3r and 6r. The averaging
condition is 1/2+1/6=1-1/3. After 9r rank-one steps the barriers are 6r
and 24r; scaling by 1/(6r) gives precisely I<=G<=4I. Thus the imported
statement and its constructive parameter regime have both been checked.

Put Z=D^(1/2)P and define the fixed N-by-N metric

\[
 H=D^{1/2}\bigl[ZG^{-2}Z^\top+I-ZG^{-1}Z^\top\bigr]D^{1/2}.
                                                               \tag{3}
\]

The matrix ZG^-1 Z^T is the orthogonal projector onto range(Z).
On this range, ZG^-2 Z^T has eigenvalues equal to those of G^-1;
on its orthogonal complement the bracket in (3) is the identity.
Consequently

\[
 \tfrac14D\preceq H\preceq D,\qquad P^\top HP=I.          \tag{4}
\]

The second identity follows by multiplication:
P^T H P=G G^-2 G+G-G G^-1 G=I. Hence restriction S->R^N is an exact
isometry from the empirical norm to ||u||_H²=u^THu. Coordinate errors
remain controlled: if ||e||_infty<=epsilon then
||e_I||_H<=||e_I||_D<=2epsilon. Every diagonal multiplication operator has
H-operator norm at most twice its largest diagonal magnitude. In
particular bounded pointwise activations and their first derivatives
remain bounded and Lipschitz in this metric, independently of N and the
smallest selected diagonal weight.

For adjacent layers set

\[
 B_0^{(l)}=P_l\frac{U_l^\top W_0^{(l)}U_{l-1}}n
                     P_{l-1}^\top H_{l-1},\qquad
 B^{(l)*}=H_{l-1}^{-1}B^{(l)\top}H_l.                    \tag{5}
\]

Its operator norm is at most ||W_0^(l)|| because P_l are isometries.
If s belongs to S_(l-1) and W_0^(l)s belongs to S_l as an exact paired
approximant, then (5) gives

\[
 B_0^{(l)}s_{I_{l-1}}=(W_0^{(l)}s)_{I_l}.
\]

The corresponding exact transpose identity holds for each exact paired
reverse approximant. Each member of a pair must separately approximate
its true source to coordinate error epsilon. These exact actions do not
assert exact mapping of the actual moving source: its action has the
C epsilon defect proved in the comparison. Initial training features
and the top Gram
are preserved exactly. The full U_l, selected P_l, and middle matrix in
(5) are discarded after H_l and B_0^(l) are formed.

## 3. Why a different training rule is required

Under a diagonal metric the pointwise gate diag(phi_l'(z)) is self-adjoint.
For general H_l its true adjoint is
H_l^-1 diag(phi_l'(z)) H_l. Therefore merely replacing diagonal cubature
weights by H_l in the former gradient-flow construction would invalidate
its backpropagation identity. Nor would constant spectral distortion alone
supply root-width source accuracy.

The next construction explicitly repairs the residual dynamics instead.
Its loss decreases exactly, although its parameter vector field is not
asserted to be the gradient of that loss. This distinction is part of the
result, not an omitted proof obligation.

## 4. Stored state, forward pass, and autonomous equations

The moving state is (A_C,B_C^(2),...,B_C^(L),w_C,c_C), where c_C is an
m-vector initialized at y and w_C is a raw readout initialized at zero.
Initialize A_C=A_{0,I_1} and B_C by (5). H_l are fixed positive matrices.
The hidden forward pass uses the original pointwise activations:

\[
 z_C^{(1)}(x)=A_Cv,\quad
 z_C^{(l)}(x)=B_C^{(l)}h_C^{(l-1)}(x),\quad
 h_C^{(l)}(x)=\phi_l(z_C^{(l)}(x)).                       \tag{6}
\]

Let F_C=[h_{C,1}^(L),...,h_{C,m}^(L)] be the current N_L-by-m matrix
of top training features and let Q_C=F_C^T H_L F_C. While Q_C is positive
definite define the effective readout

\[
 \widehat w_C=w_C+F_CQ_C^{-1}
                   (y-c_C-F_C^\top H_Lw_C),\qquad
 f_C(x)=\widehat w_C^\top H_Lh_C^{(L)}(x).                \tag{7}
\]

Substitution gives the exact identity

\[
                       y-f_C(x_1,\ldots,x_m)=c_C.        \tag{8}
\]

Thus the internal state is the model's own residual, not a reference
residual supplied from outside. Computing (7) uses only current neural
features, current state, and the retained training labels. The correction
is an ordinary linear readout combination of current hidden features.

Define the model's backward signals by

\[
 k_{C,a}^{(L)}=\widehat w_C,\quad
 \delta_{C,a}^{(l)}=\phi_l'(z_{C,a}^{(l)})\odot k_{C,a}^{(l)},\quad
 k_{C,a}^{(l)}=B_C^{(l+1)*}\delta_{C,a}^{(l+1)}.
                                                               \tag{9}
\]

These are explicitly defined training signals; for non-diagonal H they
are not claimed to equal derivatives of the network output. Form the
symmetric matrix

\[
 \begin{aligned}
 K_{C,ab}={}&\langle h_{C,a}^{(L)},h_{C,b}^{(L)}\rangle_{H_L}\\
 &+\sum_{l=2}^L
    \langle\delta_{C,a}^{(l)},\delta_{C,b}^{(l)}\rangle_{H_l}
    \langle h_{C,a}^{(l-1)},h_{C,b}^{(l-1)}\rangle_{H_{l-1}}\\
 &+\langle\delta_{C,a}^{(1)},\delta_{C,b}^{(1)}\rangle_{H_1}
      v_a^\top v_b .
 \end{aligned}                                               \tag{10}
\]

Each term is a Gram matrix (use tensor products for the product terms),
so K_C is positive semidefinite and K_C>=Q_C. The full autonomous flow is

\[
 \begin{aligned}
 \dot A_C&=\frac2m\sum_a c_{C,a}\delta_{C,a}^{(1)}v_a^\top,\\
 \dot B_C^{(l)}&=\frac2m\sum_a c_{C,a}\delta_{C,a}^{(l)}
                          h_{C,a}^{(l-1)\top}H_{l-1},\\
 \dot w_C&=\frac2m\sum_a c_{C,a}h_{C,a}^{(L)},\\
 \dot c_C&=-\frac2m K_Cc_C .
 \end{aligned}                                               \tag{11}
\]

All hidden matrices are trained. No physical-time function, clock-driven
source interpolation, initial Taylor series, or reference state is an
argument of (6)--(11). In particular the internally evolved residual
trajectory is generated by this changing network. By (8), the squared
mean loss is ||c_C||_m², and its exact derivative is
-4 c_C^T K_C c_C/m²<=0. On Q_C/m>=gI it decays at rate at least 2g
in residual norm. Local existence and uniqueness hold on this open set,
because the activations are smooth and inversion is smooth on invertible
matrices. The following energy argument proves that this set is never left.

The coordinator identified a stronger energy argument after the independent
candidate was frozen. Let theta_C denote only (A_C,B_C,w_C), with the
parameter norm defined explicitly by

\[
 \|(A,B,w)\|_{\rm par}^2=
 \operatorname{tr}(A^\top H_1A)
 +\sum_{l=2}^L\|H_l^{1/2}B^{(l)}H_{l-1}^{-1/2}\|_F^2
 +w^\top H_Lw.
\]

Expanding the
squared velocities in (11), including all cross-sample terms, gives

\[
 -\frac{d}{dt}\rho_C^2
 =\frac4{m^2}c_C^\top K_Cc_C
 =\|\dot\theta_C\|_{\rm par}^2,\qquad
 \rho_C=\|c_C\|_m.                                      \tag{11a}
\]

This identity does not require the vector field to be a gradient: (10)
is exactly the Gram of the directions appearing in the raw parameter
velocities. On a stopped tube Q_C/m>=gI, with g=c lambda, it implies
-rho_C'>=2g rho_C and
||theta_C'||²=2rho_C(-rho_C'). Therefore
||theta_C'||<=(-rho_C')/sqrt(g), including its continuous zero-residual
interpretation, and integration gives

\[
 \int_0^t\|\dot\theta_C\|_{\rm par}\,ds\le CY/\sqrt\lambda,
 \qquad \|w_C(t)\|_{H_L}\le CY/\sqrt\lambda.              \tag{11b}
\]

The operator P_C=F_CQ_C^-1 F_C^T H_L is the H_L-orthogonal projector
onto range(F_C). Rewriting (7) as
widehat w_C=(I-P_C)w_C+F_CQ_C^-1(y-c_C), its two terms are orthogonal.
Since ||y-c_C||_m<=2Y, (11b) and the inverse-Gram bound prove
||widehat w_C||_{H_L}<=CY/sqrt(lambda). Bounded gates and mixers give
the same bound on all backward RMS norms. Consequently all hidden
parameter displacements, and hence every training-feature displacement,
are at most

\[
 C\frac{Y}{\sqrt\lambda}\int_0^t\rho_C(s)ds
                    \le CY^2/\lambda^{3/2}.             \tag{11c}
\]

The initial normalized feature matrix H_L^(1/2)F_C/sqrt(m) has smallest
singular value comparable to sqrt(lambda). Its operator perturbation is
bounded by the RMS of the individual feature perturbations in (11c).
For Y<=c lambda the perturbation is at most a small fixed fraction of
sqrt(lambda). Hidden operator bounds close at the same time, since their
Hilbert--Schmidt displacements satisfy (11c). The first-exit argument
therefore preserves the initialized Gram margin globally. This proves
independent fitting of the autonomous model throughout the real-label
range required by the existing source theorem, with no extra label loss.

## 5. Same-time comparison through the source horizon

For proof only, use the selected reference state A_R=A_I, w_R=w_I and

\[
 B_R^{(l)}(t)=B_0^{(l)}+\frac2m\sum_a\int_0^t c_{n,a}(s)
 \delta_{n,a}^{(l)}(s)_{I_l}
 h_{n,a}^{(l-1)}(s)_{I_{l-1}}^\top H_{l-1}\,ds.          \tag{12}
\]

Use the H first-weight/readout norms and the induced Hilbert--Schmidt
matrix norms. Let d(t) be the sum of their distances between the
compressed state and (12), and u(t)=||c_C(t)-c_n(t)||_m.

The previous pairing proof applies with (4): source pairings have error
C epsilon, readout pairings have the same bound by the integral formula,
and forward/reverse actions of (12) have errors C epsilon. No claim about
a metric adjoint of the activation is used in these steps. Layerwise
forward subtraction, using the bounded diagonal-multiplier estimate
following (4), gives

\[
 \|h_C^{(l)}(t,x)-h_n^{(l)}(t,x)_{I_l}\|_{H_l}
                         \le C(d(t)+\epsilon).           \tag{13}
\]

Initially d=u=0 and the selected top Gram equals the original one.
Stop the comparison if the bounded-operator tube is left, or if the
compressed normalized top Gram loses a fixed fraction of the reference
lower margin c lambda. Within this tube,

\[
 \|F_CQ_C^{-1}r\|_{H_L}^2=r^\top Q_C^{-1}r
                           \le C\lambda^{-1}\|r\|_m^2.
\]

In (7), r=y-c_C-F_C^T H_Lw_C. Adding and subtracting the actual
reference prediction and applying (13) shows
||r||_m<=u+C(d+epsilon). Hence

\[
 \|\widehat w_C-w_{n,I_L}\|_{H_L}
                 \le C\lambda^{-1/2}(d+u+\epsilon).      \tag{14}
\]

For backward subtraction, multiply every changed gate by the actual
selected reference carrier, exactly as in the previous comparison note.
The bounded diagonal-multiplier norm supplies only a structural factor;
its coordinate maximum supplies M. The other term uses the bounded
mixer and the already controlled upper response difference. Descending
through fixed depth therefore proves

\[
 \max_{a,l}\|\delta_{C,a}^{(l)}-delta_{n,a,I_l}^{(l)}\|_{H_l}
        \le C\lambda^{-1/2}(1+M)(d+u+\epsilon).           \tag{15}
\]

Here and below the response RMS norms themselves stay bounded in the
stopped tube. Pairing (15), (13), and the source pairing errors in (10)
gives, using ||E/m||_op<=max_ab|E_ab|,

\[
 \|(K_C-K_n)/m\|_{\rm op}
        \le C\lambda^{-1/2}(1+M)(d+u+\epsilon).           \tag{16}
\]

K_n is the original model's actual tangent Gram. Both residual equations
are exact: the original equation comes from its gradient flow, while
the compressed equation comes from (11) and is its actual residual
equation by (8). Subtract them and use K_C/m>=c lambda I:

\[
 D^+u\le-c\lambda u
    +C\lambda^{-1/2}(1+M)\rho_n(d+u+\epsilon).            \tag{17}
\]

Regularizing the norm at u=0 justifies the same inequality there.
Integrating and dropping the nonnegative terminal value yields

\[
 \int_0^t u(s)ds\le
 C\lambda^{-3/2}(1+M)\int_0^t\rho_n(s)(d+u+\epsilon)(s)ds. \tag{18}
\]

Dropping the damping term in (17) also bounds u(t) by the same integral
with coefficient C lambda^-1/2(1+M). Subtract the first three equations
in (11) from the exact reference velocities defining (12). A residual
difference costs Cu; response and feature differences cost the
right-hand side of (15) times rho_n. Thus

\[
 d(t)\le C\int_0^t u(s)ds+
 C\lambda^{-1/2}(1+M)\int_0^t\rho_n(s)(d+u+\epsilon)(s)ds. \tag{19}
\]

No differentiated observation defect or activation-metric commutator
occurs. Combining (18)--(19) with the pointwise bound for u, and putting
E=d+u, gives

\[
 E(t)\le C\lambda^{-3/2}(1+M)
                   \int_0^t\rho_n(s)(E(s)+\epsilon)ds.
\]

The integral Gronwall inequality (or direct differentiation of its
integral majorant) now yields

\[
 \sup_{t\le T}(E(t)+\epsilon)
 \le\epsilon\exp[C\lambda^{-3/2}(1+M)S].                 \tag{20}
\]

For each fixed dataset this tends to zero at epsilon=n^-1 and
M=O(sqrt(ell_n)). It is eventually smaller than the fixed stopped-tube
margins. Equations (13) and the exact source pairings preserve the
compressed Gram lower margin, so the first-exit argument closes through
T. The bound is independent of elapsed time except through the known
carrier event; no T factor appears.

Equation (14) and bounded sphere features give the same-time output bound

\[
 \sup_{t\le T,x}|f_C(t,x)-f_n(t,x)|
 \le C\lambda^{-1/2}\epsilon
                \exp[C\lambda^{-3/2}(1+M)S].             \tag{21}
\]

For example (2) gives the explicit sufficient estimate

\[
 C\lambda^{-1/2}e^{CY/\lambda^{5/2}}n^{-1}
                  e^{(CY^2/\lambda^{7/2})\sqrt{\ell_n}}.
                                                               \tag{22}
\]

The additional width condition ell_n>=C(1+Y^4/lambda^7) bounds the last
exponential by sqrt(n), up to a harmless structural constant. Thus the
finite-horizon error is at most C_data/sqrt(n), where one may retain
C_data=C lambda^-1/2 exp(CY/lambda^(5/2)). This is a worse explicit
conditioning dependence than the earlier dense construction; it does not
change storage. This step only absorbs the subpolynomial stability
amplification and does not discard any m-dependent storage term.

## 6. Global existence, fitting, and the endpoint

The independent energy argument in Section 4 supplies global bounded
parameters, Q_C/m>=gI with g=c lambda, and exponential residual decay.
Its finite path length makes every raw parameter converge. The following
tail estimate controls the algebraically reconstructed readout with
constants independent of selected widths and minimum weights.

Regard the normalized training feature matrix
V=F_C/sqrt(m) as an operator from Euclidean sample space to the H_L
neuron space. Its adjoint is V*=V^T H_L. Define

\[
 q=Q_C/m=V^*V,\qquad b=(y-c_C)/\sqrt m,\qquad
 T_V=Vq^{-1},\quad P_V=T_VV^*,\quad
 \widehat w_C=(I-P_V)w_C+T_Vb.                            \tag{23a}
\]

These quantities are computed from current state; T_V is unrelated to
the source horizon T. Bounded features give ||V||<=C; q>=gI gives
||T_V||<=g^-1/2 because T_V* T_V=q^-1; and P_V is an orthogonal
projection, so ||P_V||<=1. Forward differentiation through the actual
neural layers and the bounded diagonal-multiplier estimate (4) give

\[
 \|\dot V\|\le C\|\dot\theta_{C,\mathrm{hidden}}\|_{\rm par}
                 \le C(Y/\sqrt\lambda)\rho_C.            \tag{23b}
\]

In the first inequality, the operator norm of the normalized training
feature derivative is bounded by the RMS of its individual feature
derivatives. Thus no sample-count factor is introduced. Differentiation
gives dot q=dot V* V+V* dot V and
dot(q^-1)=-q^-1 dot q q^-1. Applying the product rule to T_V and P_V
therefore proves

\[
 \|\dot q\|\le2\|V\|\|\dot V\|,\qquad
 \|\dot T_V\|+\|\dot P_V\|
                   \le C(g^{-1}+g^{-2})\|\dot V\|.       \tag{23c}
\]

The feature/response Gram formula (10) gives ||K_C/m||<=C, hence
||dot c_C||_m<=C rho_C. Also ||dot w_C||_(H_L)<=C rho_C,
||w_C||_(H_L)<=CY/sqrt(lambda), and ||b||_2<=2Y. Differentiating
(23a) and using the contraction of I-P_V yields

\[
 \begin{aligned}
 \|\dot{\widehat w}_C\|_{H_L}
 &\le \|\dot w_C\|_{H_L}
       +\|\dot P_V\|\|w_C\|_{H_L}
       +\|\dot T_V\|\|b\|_2
       +\|T_V\|\|\dot c_C\|_m\\
 &\le C_{\rm data}\rho_C .
 \end{aligned}                                               \tag{23d}
\]

Only fixed data and gap parameters enter C_data. All displayed operator
norms use the normalized sample and H neuron norms; no Euclidean
coordinate estimate with a minimum-weight dependence is used.

For every sphere query, its feature norm is bounded by C and its feature
derivative by C(Y/sqrt(lambda))rho_C, by the same forward calculation.
Differentiating f_C=widehat w_C^T H_L h_C and using (23d) gives

\[
 \sup_x|\partial_t f_C(t,x)|\le C_{\rm data}\rho_C(t),
 \qquad
 \sup_x|f_C(\infty,x)-f_C(t,x)|
            \le C_{\rm data}(Y/\lambda)e^{-c\lambda t}. \tag{23e}
\]

This proves sphere-uniform convergence. The limiting Gram remains
positive definite, so the effective readout converges; (8) and c_C->0
give exact interpolation. No source approximation is required after T.
The original reference has its supplied analogous tail. With the
structural horizon constant in T=C lambda^-1 ell_n chosen large, both
tails are O(C_data n^-1). For t>=T compare each flow to its value at T;
the difference from that value is bounded by twice its endpoint tail.
Combining with (21) proves

\[
 \sup_{t\in[0,\infty]}\sup_{x\in\sqrt d S^{d-1}}
             |f_C(t,x)-f_n(t,x)|\le C_{\rm data}/\sqrt n,  \tag{23}
\]

including t=infinity. Both flows continue autonomously after T; no switch,
trajectory freezing, or supplied endpoint is used.

## 7. Complete retained storage and the original two-term source count

The moving parameters A_C, B_C, w_C, c_C require

\[
 dN_1+\sum_{l=2}^L N_lN_{l-1}+N_L+m
\]

real coordinates. The fixed H_l and optional inverse/copies require
O(sum_l N_l²) more. Training data cost m(d+1). The working Q_C and training
feature matrices also cost at most O(R²): exact preservation of the
full-rank m-sample initial top Gram forces m<=N_L<=9R. Thus counting all
retained coefficients and even these caches gives

\[
 \mathrm{size}\le C(R^2+dR)+Cm(d+1)
 \le C\lambda^{-2}(\ell_n^{2a}+m^2\ell_n^{2b})+Cm(d+1).   \tag{24}
\]

Neither U_l, original-width coefficient vectors, nor original-width
initialized matrices remain after setup. The readout correction contains
no stored reference trajectory or time-dependent coefficient table.
Its cost is an m-by-m linear solve, whose computational work is not a
resource guaranteed by this existence result.

When lambda=gamma/m, (24) is

\[
 C\gamma^{-2}(m^2\ell_n^{2a}+m^4\ell_n^{2b})+Cm(d+1).    \tag{25}
\]

This calculation removes one full squaring from the original storage
construction. With the training-only source bound (1), it does not by
itself give a pure m² prefactor: the contribution m ell_n^b survives
inside R. Assuming ell_n^(a-b)>=m would make the first term dominate,
but that additional-width simplification is not used here. Equations
(24)--(25) retain this original two-term calculation for provenance;
Section 9 uses the separately checked source refinement to remove the
second term, without hiding it inside a width threshold.

## 8. Contract audit and checked status

The reference initialization, labels, data, physical clock and activation
functions are unchanged. Runtime hidden features use genuine moving neural
matrices. The output is a linear readout of their current top activations;
its trainable effective readout is algebraically reconstructed from current
state. All residuals equal labels minus this same network's predictions.
Its residual matrix is computed from the network's own changing features
and responses. Thus there is neither trajectory playback nor an external
residual oracle.

The substantive extension is a different autonomous optimizer, including
m extra residual coordinates and an algebraic readout constraint. Formula
(10) is a surrogate Gram, not the actual parameter-gradient tangent Gram.
If the representation contract additionally insists that the smaller
network use ordinary squared-loss gradient flow with the old mobilities,
then this construction is outside that narrower contract and (24) is not
a solution to that stronger demand. The non-diagonal gate-adjoint issue
in Section 3 remains a precise obstruction to the simple metric replacement
under that demand; it is not an impossibility theorem for other methods.

The conditional source-to-runtime theorem has passed the complete
independent internal check named at the beginning. Its source theorem
and the general-vector sparsification theorem remain explicit inputs.
All hidden updates are present; this does not assert nonzero motion of
every hidden layer for every possible admissible label/activation pair.
No promotion into established material has occurred.

## 9. Separately checked whole-query sources give the quadratic sample bound

[WHOLE_QUERY_RESPONSE_SOURCE.md](WHOLE_QUERY_RESPONSE_SOURCE.md) replaces
the m training-only backward source families by a fixed number of jointly
analytic whole-query backward families. Their C sqrt(n) coordinate
magnitudes affect only approximation-degree constants. The independent
reconstruction in
[WHOLE_QUERY_RESPONSE_CHECK.md](WHOLE_QUERY_RESPONSE_CHECK.md), report
SHA-256 `dfefa67af9a7d8b7a9b1d7a279169b5cc8d6efe7b29ad4092853f121907524ce`,
checks the holomorphy, both exact paired-approximant interfaces,
initialization-only coefficients and unchanged training-carrier input.
It supplies, including the exact initialization additions,

\[
 R\le C\lambda^{-1}\ell_n^a,\qquad a=d(L+5)+1.           \tag{26}
\]

Substituting (26) into the first inequality of (24) gives

\[
 \mathrm{size}\le C\lambda^{-2}\ell_n^{2a}+Cm(d+1).
                                                               \tag{27}
\]

When lambda=gamma/m this is
C gamma^-2 m² ell_n^(2a)+Cm(d+1). Thus the former pure-quadratic-sample
gap is resolved conditional on this separately checked source theorem
and the original source probability inputs. The runtime and its same-time
error proof are unchanged. There is no additional condition
ell_n^(a-b)>=m. The whole-query source note also retains the optional
explicit logarithmic gap factor when log(e/lambda) has not yet been
absorbed into the standard sufficiently-large-width condition.

The complete runtime, whole-query source, and separate-budget checks were
read before this revision. Their combination gives (27) under Y<=c lambda
with the original fixed-dataset quantifiers. These are internally checked
study results; this update does not promote them into established material.

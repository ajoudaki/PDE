# Stopped independent-cavity trace linearization: gradient flow

Author calculation, 2026-09-06. This note proves a finite-width,
continuous-time stopped approximation. It does not prove that the stop
is unlikely, that the response trace stays bounded as width grows, or
that a mean-field limit exists. No assertion about raw GD is made.

The sole source inspected was the entire 946-line original candidate
SINGLE_FIRST_NEURON_CAVITY_TEST.md, SHA-256
a94813d504e4e9bc9a7c7e2c66472f41b76d66dfc20e9c120ddabca1add558bc.
Its identities and bounds used here are derived below. Subsequent
revisions and reviews were not consulted. No agents, experiments, or
external concentration theorem are used.

The key point is to construct the linear response at the independent
cavity, prove simultaneous Gaussian bounds for its coordinate kernels,
and evaluate its nonlinear consistency defect. A deterministic stability
estimate, whose exponential is allowed to be subpolynomial in width,
then transfers that approximation to the actual trajectory. This closes
the coordinate bootstrap without needing a maximum bound at intermediate
points on a parameter secant.

## 1. Exact model, scope, and quantitative statement

There are two samples, two hidden layers of the same width \(n\), and
input dimension \(d\geq2\). Fix deterministic inputs and labels with
\[
 \|x_a\|^2=d,\qquad x_1^Tx_2/d=\rho\in(-1,1),\qquad
 C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\qquad y=(1,-1).
\]
The dimension \(d\) can depend on \(n\); constants below do not depend on
\(d\). Norms are unnormalized Euclidean, Frobenius, or spectral norms,
as indicated. Define
\[
\begin{split}
 z^{(1)}_a&=W^{(1)}x_a,& h^{(1)}_a&=\phi_1(z^{(1)}_a),\\
 z^{(2)}_a&=Ah^{(1)}_a,& h^{(2)}_a&=\phi_2(z^{(2)}_a),\\
 f_a&=n^{-1}w^Th^{(2)}_a,&c_a&=-2(f_a-y_a),\\
 \delta_a&=w\odot\phi_2'(z^{(2)}_a),&q_a&=A^T\delta_a.
\end{split}                                                     \tag{1}
\]
Here \(q_a=q^{(1)}_a\), and \(\delta_a=\delta^{(2)}_a\). The exact raw
gradient flow is
\[
 \dot W^{(1)}={1\over d}\sum_a c_a
       [\phi_1'(z^{(1)}_a)\odot q_a]x_a^T,\quad
 \dot A={1\over n}\sum_a c_a\delta_a(h^{(1)}_a)^T,\quad
 \dot w=\sum_a c_a h^{(2)}_a.                               \tag{2}
\]
Initialization is independent, with entries distributed as
\[
 W^{(1)}_{il}(0)\sim N(0,1/d),\quad
 A_{li}(0)\sim N(0,1/n),\quad w_l(0)\sim N(0,n^{-2}).        \tag{3}
\]
Take \(\phi_2=\arctan\). The first activation is either \(\arctan\),
or \(\phi_1(s)=\int_0^s p(u)\,du\) for a fixed smooth compactly supported
function \(p\) that is not identically zero. In particular both
activations and their derivatives of orders one through three have
finite, width-independent bounds. The third derivative is used in
this note's quadratic Taylor estimates: the candidate's displayed
bounds through order two alone would not supply them. Both specified
activation families satisfy this regularity. Put
\(B_1=\|\phi_1\|_\infty\).

Fix \(T<\infty\), \(K>0\), and a deterministic deleted index \(j\).
Write \(I=\{1,\ldots,n\}\setminus\{j\}\), \(B(t)=A(t)_{:,I}\), and
\[
 g=A(0)_{:,j}\sim N(0,I_n/n),\qquad
 \xi_a=z^{(1)}_{a,j}(0),\qquad R_n=K\sqrt{\log n}.
\]
The sigma-field \(\mathcal F_{-j}\) contains all initialization except
\(g\), including \(\xi\sim N(0,C)\). It is independent of \(g\).

Delete column \(j\) permanently, freeze the first row \(j\), and train
all remaining parameters by (2), with denominator \(n\) unchanged.
This is the cavity. Its first features are indexed by \(I\); its upper
width remains \(n\). Put
\[
 \mathcal C_n=\{\|B(0)\|_{\rm op}\leq8,\ \|w(0)\|_\infty\leq1,\quad
             \max_{i\in I,a}|\widehat q_{a,i}(0)|\leq R_n\}.
                                                               \tag{4}
\]
This event is \(\mathcal F_{-j}\)-measurable. Stop the cavity at
\[
 \tau_c=T\wedge\inf\{t\geq0:
              \max_{i\in I,a}|\widehat q_{a,i}(t)|\geq R_n\}, \tag{5}
\]
and freeze its parameters thereafter. Throughout the note a hat means
this frozen extension to \([0,T]\). On \(\mathcal C_n\) its first reverse
fields are bounded by \(R_n\) everywhere. Define the actual stop
\[
 \tau_f=T\wedge\inf\{t\geq0:\max_{i,a}|q_{a,i}(t)|\geq R_n\},
 \qquad \tau=\tau_c\wedge\tau_f.                            \tag{6}
\]
The actual stop includes \(j\). If an initial actual field already
exceeds \(R_n\), use \(\tau_f=0\). All statements at that single time
remain valid. An additional stop on other backward fields would only
shorten the interval and does not affect the assertion.

Here is the result, with a finite-width error formulation. For every
fixed probability exponent \(p_*>0\), there is a finite constant \(A_*\),
depending only on \(T,\rho,p_*\) and the fixed activation bounds, for
which the following holds. Set
\[
 H_n=\exp\{A_*(1+R_n)\},\qquad
 a_n=\sqrt{\log n/n},\qquad \epsilon_n=H_n^{20}a_n.          \tag{7}
\]
Require \(n\geq3\) and \(\epsilon_n\leq1/2\). Increasing \(A_*\) absorbs
the finitely many constant lower-width restrictions in the proof; thus
these displayed conditions specify the width regime. For fixed
\(T,K,p_*\), they hold for all sufficiently large \(n\), and
\[
 \epsilon_n=n^{-1/2+o(1)}\longrightarrow0.                  \tag{8}
\]
For almost every cavity initialization in \(\mathcal C_n\), there is a
conditional event of probability at least \(1-n^{-p_*}-e^{-n/2}\) on
which, simultaneously for \(a=1,2\) and \(0\leq t\leq\tau\),
\[
\begin{split}
 q_{a,j}(t)={}&G_a(t)+M_a(t)+S_a(t)\\
 &+\sum_{b=1}^2\int_0^t
       \kappa_{ab}(t,s)h^{(1)}_{b,j}(s)\,ds+e_a^{\rm err}(t),
 \qquad \sup_{t\leq\tau,a}|e_a^{\rm err}(t)|\leq\epsilon_n.
\end{split}                                                     \tag{9}
\]
The objects are specified, without any fitted kernel, as follows:
\[
\begin{split}
 G_a(t)&=g^T\widehat\delta_a(t),\\
 \ell(t)&={1\over n}\sum_b\int_0^t
       c_b(s)\delta_b(s)h^{(1)}_{b,j}(s)\,ds,\\
 M_a(t)&=\ell(t)^T\delta_a(t),\\
 S_a(t)&=h^{(1)}_{a,j}(t)g^TD_a^{\rm dir}(t)(g+\ell(t)),\\
 \kappa_{ab}(t,s)&={1\over n}\operatorname{Tr}
       [L_a(t)U_c(t,s)\mathcal B_b(s)].
\end{split}                                                     \tag{10}
\]
Here \(D_a^{\rm dir}\) is the exact direct secant in (18) below, while
\(L_a,U_c,\mathcal B_b\) are derivatives and a propagator evaluated
entirely at the stopped cavity, defined in (23)--(27). The matrix inside
the trace is independent of \(g\). Conditional on \(\mathcal F_{-j}\),
\(G\) is a centered Gaussian process with covariance
\[
 \mathbb E[G_a(t)G_b(s)\mid\mathcal F_{-j}]
       ={1\over n}\widehat\delta_a(t)^T\widehat\delta_b(s). \tag{11}
\]
The terms \(M_a,S_a\) are bounded by a constant depending only on \(T\),
\(\rho\), and the activations on the event in this statement. There is
also a version of (9) in which these terms have cavity coefficients:
\[
\begin{split}
 q_{a,j}(t)={}&G_a(t)+d_a(t)h^{(1)}_{a,j}(t)\\
 &+\sum_b\int_0^t
       [m_{ab}(t,s)+\kappa_{ab}(t,s)]h^{(1)}_{b,j}(s)\,ds
       +\widetilde e_a^{\rm err}(t),\\
 d_a(t)&={1\over n}\operatorname{Tr}
     \operatorname{diag}(\widehat w\odot\phi_2''(\widehat z^{(2)}_a)),\\
 m_{ab}(t,s)&={\widehat c_b(s)\over n}
                    \widehat\delta_b(s)^T\widehat\delta_a(t),
 \qquad
 \sup_{t\leq\tau,a}|\widetilde e_a^{\rm err}(t)|\leq\epsilon_n.
\end{split}                                                     \tag{12}
\]
The constant in (7) covers both errors. The functions \(d_a,m_{ab}\)
are bounded uniformly in \(n\). Only a subpolynomial bound is proved
for \(\kappa_{ab}\). No width-uniform bound on that trace, and no
assertion that \(\tau=T\) with high probability, is part of the result.
All time suprema are continuous-time suprema; the probability bound
does not depend on a mesh on which one later samples these functions.

## 2. Uniform deterministic bounds and exact restoration

The raw metric is
\[
 \|V\|_{\rm raw}^2={d\over n}\|V^{(1)}\|_F^2
                       +\|V^{(2)}\|_F^2+n^{-1}\|V^{(3)}\|^2.
\]
Direct differentiation of \(L=\sum_a(f_a-y_a)^2\), using (1), verifies
that (2) is its negative gradient in this metric and that
\[
 -\dot L=\|\dot W\|_{\rm raw}^2.                           \tag{13}
\]
If initially \(\|A(0)\|_{\rm op}\leq10\) and
\(\|w(0)\|_\infty\leq1\), then \(|f_a(0)|\leq\|\phi_2\|_\infty\).
Loss decrease bounds \(\sum|c_a|\). Integrating \(\dot w\) gives a
constant bound on \(\|w\|_\infty\). Finally
\[
 \|\dot A\|_{\rm op}\leq\|\dot A\|_F
 \leq {1\over n}\sum_a|c_a|\|\delta_a\|\|h^{(1)}_a\|
 \leq C_T
\]
gives a constant bound on \(\|A\|_{\rm op}\). Consequently
\[
 \sum_a|c_a|+\|w\|_\infty+\|A\|_{\rm op}\leq C_T,\qquad
 \|\delta_a\|+\|q_a\|\leq C_T\sqrt n,\qquad
 \|\dot X\|\leq C_T,                                      \tag{14}
\]
where \(X\) is the bulk raw coordinate introduced below. The same proof
applies to the cavity with normalization \(n\). Local existence follows
from local Lipschitz continuity of (2). Formula (13) bounds finite-time
raw displacement, and the displayed bounds also bound raw speed.
Thus no finite-time escape occurs. Freezing preserves these bounds.

On \(\mathcal C_n\cap\{\|g\|\leq2\}\),
\(\|A(0)\|_{\rm op}\leq\|B(0)\|_{\rm op}+\|g\|\leq10\).
Thus (14) is available without conditioning on an actual stopping
event. Integrating exactly the column \(j\) equation in (2) gives
\[
 A_{:,j}=g+\ell,\qquad \|\ell\|\leq C_T/\sqrt n,\qquad
 z^{(2)}_a=B h^{(1)}_{a,I}+(g+\ell)h^{(1)}_{a,j}.           \tag{15}
\]
The learned readback obeys
\[
 |M_a(t)|\leq {1\over n}\sum_b\int_0^t |c_b(s)|B_1
                      \|\delta_b(s)\|\|\delta_a(t)\|\,ds\leq C_T.
                                                               \tag{16}
\]

Write \(z_i=(z^{(1)}_{1,i},z^{(1)}_{2,i})^T\). Its exact equation is
\[
 \dot z_i=C(c_a\phi_1'(z^{(1)}_{a,i})q_{a,i})_{a=1,2}.     \tag{17}
\]
The cavity has the same equation for \(i\in I\), with cavity fields.
For \(i=j\), (17) and \(z_j(0)=\xi\) specify the actual distinguished
root. Its path is never replaced by the frozen root. Only
\(|h^{(1)}_{a,j}|\leq B_1\) is used in the estimates.

Let \(\delta_a^0=w\odot\phi_2'(Bh^{(1)}_{a,I})\), evaluated at actual
bulk parameters, and \(e_a=(g+\ell)h^{(1)}_{a,j}\). The fundamental
theorem of calculus gives
\[
 \delta_a=\delta_a^0+D_a^{\rm dir}e_a,\qquad
 D_a^{\rm dir}=\operatorname{diag}\left(
 w_l\int_0^1\phi_2''((Bh^{(1)}_{a,I})_l+\theta e_{a,l})d\theta
                                     \right).             \tag{18}
\]
Hence the exact split is
\[
 q_{a,j}=G_a+M_a+S_a+g^T(\delta_a^0-\widehat\delta_a),\qquad
 \|D_a^{\rm dir}\|_{\rm op}\leq C_T,\qquad
 |S_a|\leq C_T\|g\|(\|g\|+n^{-1/2}).                       \tag{19}
\]
Thus it remains to approximate the last scalar. This split retains the
complete learned column and the direct nonlinear dependence on it.

## 3. Cavity derivatives, including all residual and trained-rank terms

Use the Euclidean bulk coordinates
\[
 X=\left((C^{-1/2}z_i/\sqrt n)_{i\in I},\ B,\ w/\sqrt n\right)
       \in\mathbb R^{m_n},\qquad m_n=n^2+2n-2.             \tag{20}
\]
For moving first rows, \(d\|\Delta W^{(1)}_i\|^2
=\Delta z_i^TC^{-1}\Delta z_i\): write the row displacement in the
span of \(x_1,x_2\), multiply it by the inputs, and use their Gram matrix
\(dC\). The input-orthogonal part never moves. Thus (20) is exactly
the restricted raw metric.

For an independent argument \(E\in\mathbb R^{2n}\), set
\[
 f_a(X,E)={1\over n}w^T\phi_2(B\phi_1(z^{(1)}_{a,I})+\sqrt n E_a),
 \qquad F(X,E)=-\nabla_X\sum_a(f_a(X,E)-y_a)^2.            \tag{21}
\]
Derivatives here hold \(E\) fixed. The exact actual bulk equation is
\(\dot X=F(X,e/\sqrt n)\); before \(\tau_c\) the cavity equation is
\(\dot{\widehat X}=F(\widehat X,0)\). This equality does not differentiate
the actual path \(e\) with respect to bulk parameters.

At a cavity point write
\[
 H_a=\phi_1(\widehat z^{(1)}_{a,I}),\quad
 P_a=\operatorname{diag}\phi_1'(\widehat z^{(1)}_{a,I}),\quad
 V_a=\operatorname{diag}\phi_2'(\widehat z^{(2)}_a),\quad
 D_a=\operatorname{diag}(\widehat w\odot\phi_2''(\widehat z^{(2)}_a)).
                                                               \tag{22}
\]
For \(Y=(u,V,v)\in\mathbb R^{m_n}\), its physical parameter increments
are \(\zeta_i=C^{1/2}u_i\), \(\Delta B=V/\sqrt n\), \(\Delta w=v\).
Define the cavity linear maps
\[
 \begin{split}
 Z_aY&=V H_a/\sqrt n+\widehat B P_a\zeta_a,\\
 L_aY&=V_a v+D_a Z_aY,\\
 Q_aY&=V^T\widehat\delta_a/\sqrt n+\widehat B^TL_aY.
 \end{split}                                                   \tag{23}
\]
Here \(\zeta_a=(\zeta_{a,i})_{i\in I}\), \(Z_a,L_a\) map to
\(\mathbb R^n\), and \(Q_a\) maps to \(\mathbb R^{n-1}\).
In particular \(L_a=n^{-1/2}D_X\delta_a(X,0)|_{X=\widehat X}\).

For an upper input \(e=(e_1,e_2)\) put
\[
 \lambda_a=Z_aY+e_a,\quad
 d\delta_a=L_aY+D_a e_a,\quad
 dq_a=Q_aY+\widehat B^TD_a e_a,\quad
 \chi_a=-{2\over n}\left[v^T\phi_2(\widehat z^{(2)}_a)
                              +\widehat\delta_a^T\lambda_a\right].
                                                               \tag{24}
\]
The exact first derivative of the rescaled bulk vector field is the
linear map \(\mathscr L(Y,e)=J_cY+\sum_b\mathcal B_b e_b\) given by
\[
\begin{split}
 (\mathscr L_u)_i
 &=C^{1/2}\left(
     \widehat c_a\phi_1''(\widehat z^{(1)}_{a,i})\widehat q_{a,i}\zeta_{a,i}
    +\widehat c_a\phi_1'(\widehat z^{(1)}_{a,i})dq_{a,i}
    +\chi_a\phi_1'(\widehat z^{(1)}_{a,i})\widehat q_{a,i}
                  \right)_{a=1,2},\\
 \mathscr L_V
 &={1\over\sqrt n}\sum_a
    [\chi_a\widehat\delta_a H_a^T
       +\widehat c_a d\delta_a H_a^T
       +\widehat c_a\widehat\delta_a(P_a\zeta_a)^T],\\
 \mathscr L_v
 &=\sum_a[\chi_a\phi_2(\widehat z^{(2)}_a)
                    +\widehat c_a V_a\lambda_a].
\end{split}                                                     \tag{25}
\]
These follow by differentiating, respectively, (17), the bulk-column
equation, and the readout equation. They show that
\[
 J_c=D_XF(\widehat X,0),\qquad
 \mathcal B_b=D_{E_b}F(\widehat X,0).                       \tag{26}
\]
In particular \(\chi_a\), including its dependence on \(e_a\), is present
in every required place. Both differentiated factors of each trained
outer product are present, as are the trained cavity \(B,w,c\).

Define
\[
 \partial_tU_c(t,s)=J_c(t)U_c(t,s),\quad U_c(s,s)=I_{m_n},
 \qquad K_{ab}(t,s)=L_a(t)U_c(t,s)\mathcal B_b(s).          \tag{27}
\]
Thus \(K_{ab}\in\mathbb R^{n\times n}\). The generator is the derivative
evaluated at the frozen cavity state also after \(\tau_c\); it is not
multiplied by an actual stopping indicator. Its extension after
\(\tau_c\) is only for defining independent continuous kernels.

Directly from (14), (23)--(25),
\[
 \|Z_a\|+\|L_a\|+\|Q_a\|+\|\mathcal B\|\leq C_T,\quad
 \|J_c\|\leq C_T(1+R_n),\quad
 \|U_c(t,s)\|\leq e^{C_T(1+R_n)(t-s)}.                     \tag{28}
\]
Indeed \(\|H_a\|,\|\widehat\delta_a\|,\|\widehat q_a\|
\leq C_T\sqrt n\), so the factors \(1/\sqrt n\) in (23) give bounded
maps. Equation (24) gives
\(|\chi_a|\leq C_T(\|Y\|+\|e\|)/\sqrt n\). In the first line of (25)
it multiplies a vector of norm \(C_T\sqrt n\). The first term of that
line is the sole term requiring a maximum first reverse field; its
norm is at most \(C_TR_n\|Y\|\). A rank-one matrix has Frobenius norm
equal to the product of the two vector norms, so the second and third
lines of (25) are bounded by \(C_T(\|Y\|+\|e\|)\).
Differentiating \(\|U_c(t,s)v\|^2\) and integrating proves the last
inequality of (28). Successive integration, bounded by the exponential
series, constructs this propagator.

We will also use polynomial time moduli. Before freezing,
\[
 \|\dot{\widehat z}^{(1)}\|\leq C_T\sqrt n,\quad
 \|\dot{\widehat z}^{(1)}\|_\infty\leq C_TR_n,\quad
 \|\dot{\widehat B}\|_F+\|\dot{\widehat w}\|_\infty\leq C_T,
\]
\[
 \|\dot{\widehat z}^{(2)}\|+
 \|\dot{\widehat\delta}\|+\|\dot{\widehat q}\|\leq C_T\sqrt n,
 \qquad \sum_a|\dot{\widehat c}_a|\leq C_T.                \tag{29}
\]
The first line uses (17), the RMS bound on \(q\), and the stop. For the
second, differentiate \(z^{(2)}=Bh^{(1)}\), then
\(\delta=w\odot\phi_2'(z^{(2)})\), then \(q=B^T\delta\).
The raw norm of the differential of \(c\) is bounded by the same
products as (23)--(24), and the raw speed is bounded by (14).
Freezing preserves the resulting Lipschitz bounds across the stop.
Differentiating (22)--(25) gives the loose but sufficient operator
Lipschitz bound \(C_Tn^2(1+R_n)^2\) for \(Z,L,Q,\mathcal B,D\).
For example \(\dot D_a\) costs
\(C_T(1+\|\dot{\widehat z}^{(2)}_a\|_\infty)\leq C_T(1+\sqrt n)\);
a differentiated factor \(\phi_1'\) costs \(C_TR_n\);
the vectors \(\widehat q,\dot{\widehat q}\), of norm \(C_T\sqrt n\),
retain the \(1/\sqrt n\) normalization in residual terms.
Together with \(\partial_sU_c=-U_cJ_c(s)\), these bounds supply the
time moduli used next. No regularity of \(h_j\) is needed for that step.

## 4. Uniform Gaussian linear bounds and a proved quadratic bound

Condition on a cavity initialization in \(\mathcal C_n\). All matrices
in (22)--(29) are now deterministic. Completing the square in the
Gaussian density and applying exponential Markov gives
\[
 \Pr\{|v^Tg|>\|v\|\sqrt{2x/n}\}\leq2e^{-x}.                \tag{30}
\]
This requires neither independence of different rows nor independence
between different times.

Here is the quadratic bound needed, including its proof. For a real
matrix \(K\in\mathbb R^{n\times n}\), put \(S=(K+K^T)/2\),
\(b=\|S\|_{\rm op}\), and \(v=\|S\|_F\). For \(x>0\),
\[
 \Pr\left\{\left|g^TKg-{\operatorname{Tr}K\over n}\right|
       >{2v\sqrt x\over n}+{2b x\over n}\right\}\leq2e^{-x}.
                                                               \tag{31}
\]
The antisymmetric part has zero quadratic form and zero trace.
Diagonalize \(S\) orthogonally. The standard Gaussian density is
invariant under orthogonal transformations, so the centered quadratic
form becomes \(n^{-1}\sum_i\lambda_i(Z_i^2-1)\) for independent
\(N(0,1)\) variables. The one-dimensional Gaussian integral gives
\(\mathbb E e^{uZ_i^2}=(1-2u)^{-1/2}\) for \(2u<1\). For \(2|t|b<n\),
\[
 \log\mathbb E\exp\left\{{t\over n}\sum_i\lambda_i(Z_i^2-1)\right\}
 =\sum_i[-t\lambda_i/n-\tfrac12\log(1-2t\lambda_i/n)]
 \leq {t^2v^2/n^2\over1-2|t|b/n}.                         \tag{32}
\]
To check the inequality, expand
\(-\log(1-u)-u=\sum_{k\geq2}u^k/k\), whose absolute value is at most
\(u^2/[2(1-|u|)]\) when \(|u|<1\). Apply exponential Markov with
\(t=n\sqrt x/(v+2b\sqrt x)\). At the threshold in (31), subtracting the
right side of (32) from \(t\) times that threshold gives exactly \(x\).
Use \(-S\) for the other tail. If \(v=0\), then \(S=0\) and the
centered quadratic form is identically zero.
This proves (31), including for nonsymmetric \(K\).

Apply (30) to every row of
\[
 O(t)U_c(t,s)\mathcal B_b(s),\quad
 O\in\{I_{m_n},Z_1,Z_2,L_1,L_2,Q_1,Q_2\},\quad b=1,2,     \tag{33}
\]
and also to the rows of \(I_n\) and \(\widehat B^TD_a(t)\).
Apply (31) to \(K_{ab}(t,s)\) and \(D_a(t)\). There are \(O(n^2)\)
row families and six quadratic families. Their operator norms are at
most \(H_n\), after increasing \(A_*\). The symmetric part of each
quadratic family has Frobenius norm at most \(\sqrt nH_n\).
Their joint time Lipschitz constants are at most \(n^2H_n^4\).

Use the uniform grid with \(\max(1,\lceil Tn^8\rceil)\) cells in
\([0,T]\), and all grid pairs \(s\leq t\). There are at most
\(C_Tn^{16}\) pairs and \(C_Tn^{18}\) scalar tests in total. Use
\(x=(p_*+25)\log n\) in (30)--(31). Their exceptional probabilities
sum to at most \(n^{-p_*}\) in the width regime (7), after increasing
\(A_*\). The Gaussian integral also gives
\[
 \Pr(\|g\|>2)
 \leq e^{-n}\mathbb E e^{n\|g\|^2/4}
 =e^{-n}2^{n/2}\leq e^{-n/2}.                             \tag{34}
\]
On \(\|g\|\leq2\), moving a row test to a neighboring grid point costs
at most \(C_Tn^{-6}H_n^4\). Moving a centered quadratic test costs at
most \(C_Tn^{-6}H_n^4(\|g\|^2+1)\), because
\(|\operatorname{Tr}(K-K')|/n\leq\|K-K'\|_{\rm op}\).
Round \(s\) down and \(t\) up to preserve \(s\leq t\).
Condition (7) makes these interpolation costs smaller than the
bounds below. Thus on one conditional event of probability at least
\(1-n^{-p_*}-e^{-n/2}\),
\[
 \sup_{s\leq t}\max_{\text{rows in (33)}}|\text{row}\cdot g|
       \leq H_n^2a_n,\qquad
 \|g\|_\infty+\sup_{t,a}\|\widehat B^TD_a(t)g\|_\infty
       \leq H_n^2a_n,                                    \tag{35}
\]
\[
 \sup_{s\leq t,a,b}
 \left|g^TK_{ab}(t,s)g-{\operatorname{Tr}K_{ab}(t,s)\over n}\right|
 \leq H_n^2a_n,\qquad
 \sup_{t,a}|g^TD_a(t)g-\operatorname{Tr}D_a(t)/n|
 \leq H_n^2a_n.                                          \tag{36}
\]
Constants in these displays are absorbed into \(A_*\). This proves
continuous supremum bounds; the grid is not a dynamical discretization.

Let \(h_b(t)=h^{(1)}_{b,j}(t)\) be the actual path and define
\[
 Y^{\rm lin}(t)=\sum_b\int_0^tU_c(t,s)\mathcal B_b(s)g h_b(s)\,ds,
 \qquad e_b^0(t)=g h_b(t).                               \tag{37}
\]
This vector is generally not conditionally Gaussian: \(h\) depends on
\(g\). Nevertheless (35) bounds the integrand before multiplication by
\(h\), simultaneously over all \(s,t\). Thus \(|h_b|\leq B_1\) gives
\[
 \sup_t(1+\|Y^{\rm lin}(t)\|+\|e^0(t)\|)\leq H_n,          \tag{38}
\]
\[
 \sup_t\max_a\{
  \|\zeta_a(Y^{\rm lin})\|_\infty,\ \|v^{\rm lin}\|_\infty,\quad
  \|Z_aY^{\rm lin}+e_a^0\|_\infty,\quad
  \|Q_aY^{\rm lin}+\widehat B^TD_ae_a^0\|_\infty\}
 \leq H_n^3a_n.                                          \tag{39}
\]
The norm bound in (38) follows directly from (28), \(\|g\|\leq2\),
and the integral (37). Equation (35) also bounds every individual
coordinate of \(Y^{\rm lin}\), including its matrix block.
Only the types in (39) are needed below. These estimates hold for
every bounded measurable \(h\) at once; no conditional law for \(h\)
was used.

## 5. A quadratic-defect estimate with the necessary coordinates

Fix a cavity point with (14) and \(\max|\widehat q|\leq R_n\).
For \(Y=(u,V,v)\) and an input \(e\), use (23)--(24), and put
\[
 N=1+\|Y\|+\|e\|,\qquad
 \alpha=\max_a\{\|\zeta_a\|_\infty,\|v\|_\infty,
                                      \|\lambda_a\|_\infty\}.
\]
Assume \(\alpha\leq1\) and \(N/\sqrt n\leq1\). At
\(X'=\widehat X+Y/\sqrt n\), the physical increments are those
following (22). We claim
\[
 \left\|\sqrt n[F(X',e/\sqrt n)-F(\widehat X,0)]
                       -\mathscr L(Y,e)\right\|
 \leq C_T(1+R_n)N(\alpha+N/\sqrt n).                     \tag{40}
\]
We verify the products rather than invoking a global Hessian
Lipschitz constant.

Taylor's integral formula and bounded third derivatives give
\[
 \Delta h^{(1)}_a=P_a\zeta_a+r_{1a},\quad
 \|r_{1a}\|\leq C\alpha N,\qquad
 \Delta\phi_1'=\phi_1''(\widehat z^{(1)})\odot\zeta+r_{pa},
 \quad \|r_{pa}\|\leq C\alpha N.                          \tag{41}
\]
Indeed each remainder is bounded pointwise by a constant times
\(|\zeta_i|^2\), and
\(\|\zeta^2\|_2\leq\|\zeta\|_\infty\|\zeta\|_2\).
The exact upper increment is
\[
 \Delta z^{(2)}_a=\lambda_a+\beta_a,\qquad
 \beta_a=\widehat B r_{1a}+(V/\sqrt n)\Delta h^{(1)}_a,
 \qquad \|\beta_a\|\leq Cr,\quad r=N(\alpha+N/\sqrt n).
                                                               \tag{42}
\]
The second term costs \(CN^2/\sqrt n\), using Frobenius norm for \(V\).
Because \(\alpha,N/\sqrt n\leq1\),
\(\|\Delta z^{(2)}_a\|\leq CN\). Expand first in \(\lambda_a\), then
use the Lipschitz bound for the displacement \(\beta_a\). This gives
\[
 \Delta h^{(2)}_a=V_a\lambda_a+r_{2a},\quad
 \Delta\delta_a=d\delta_a+r_{\delta a},\qquad
 \|r_{2a}\|+\|r_{\delta a}\|\leq Cr.                       \tag{43}
\]
The first bound is
\(C\|\lambda_a\|_\infty\|\lambda_a\|+C\|\beta_a\|\).
For the second the additional product is
\(v\odot[\phi_2'(\widehat z^{(2)}+\Delta z^{(2)})-
\phi_2'(\widehat z^{(2)})]\), bounded by \(C\alpha N\).
This explains why delocalization of the induced upper field, as well
as of the first roots and readout, is needed.

Expand \(q'=(\widehat B+V/\sqrt n)^T
(\widehat\delta+\Delta\delta)\). Then
\[
 \Delta q_a=dq_a+r_{qa},\quad
 r_{qa}=\widehat B^Tr_{\delta a}+(V/\sqrt n)^T\Delta\delta_a,
 \qquad \|r_{qa}\|\leq Cr.                                \tag{44}
\]
The prediction product gives
\[
 \Delta c_a=\chi_a+r_{ca},\quad
 r_{ca}=-{2\over n}
           [\widehat w^Tr_{2a}+v^T\Delta h^{(2)}_a],
 \qquad |r_{ca}|\leq Cr/\sqrt n.                          \tag{45}
\]
Also \(\|dq_a\|,\|d\delta_a\|,\|\Delta\delta_a\|,\|\Delta q_a\|
\leq CN\), and \(|\chi_a|,|\Delta c_a|\leq CN/\sqrt n\).

Insert these expansions into the bulk updates. In the first-root
update write its perturbed gate as \(p'=\widehat p+\Delta p\), with
Taylor remainder \(r_p\) as in (41). After subtracting (25), the terms with coefficient
\(\widehat c\) are
\[
 \widehat c[\widehat p\,r_q+r_p\widehat q
                                      +\Delta p\,\Delta q].
\]
Their norms are at most \(Cr\), \(CR_n\alpha N\), and \(C\alpha N\),
respectively, because \(\|\Delta p\|_\infty\leq C\alpha\).
The residual remainders can be written
\[
 r_c\widehat p\widehat q
       +\Delta c[\Delta p\,\widehat q+p'\Delta q].
\]
The first costs \(Cr\) by \(\|\widehat q\|\leq C\sqrt n\).
The other two cost \(CN\alpha\) and \(CN^2/\sqrt n\), using
\(\|\Delta p\widehat q\|\leq C\alpha\sqrt n\).
This verifies the first-root part of (40), including its curvature.

For the matrix update use
\(n^{-1/2}c\delta(h^{(1)})^T\) in \(Y\)-coordinates. Its remainders
with coefficient \(\widehat c\) are
\[
 {\widehat c\over\sqrt n}
 [r_\delta H^T+\widehat\delta r_1^T
                               +\Delta\delta(\Delta h^{(1)})^T].
\]
Their Frobenius norms are bounded by \(Cr\), \(C\alpha N\), and
\(CN^2/\sqrt n\). The residual remainders are
\[
 {1\over\sqrt n}
 [r_c\widehat\delta H^T+
       \Delta c(\Delta\delta H^T+\delta'(\Delta h^{(1)})^T)],
\]
where \(\delta'=\widehat\delta+\Delta\delta\) has norm \(C\sqrt n\).
They cost \(Cr\) and \(CN^2/\sqrt n\). In the readout update the
remainders are
\(\widehat c r_2+r_c\widehat h^{(2)}+\Delta c\Delta h^{(2)}\);
their norms have the same bounds. There are two samples, so summing
proves (40).

This calculation contains every trained rank term and every residual
term. A first-root-only coordinate estimate would have left
\(\|\lambda_a^2\|_2\) in (43) uncontrolled at the necessary scale.
The rows \(Z_a(t)U_c(t,s)\mathcal B_b(s)\) in (33) supply precisely
that estimate.

## 6. Transfer to the actual trajectory and closure of delocalization

Define \(X^{\rm app}=\widehat X+Y^{\rm lin}/\sqrt n\).
Equations (38)--(39) give \(\alpha\leq H_n^3a_n\leq1\),
\(N\leq H_n\), and \(N/\sqrt n\leq1\). The approximate readout is
bounded coordinatewise by \(C_T+1\) and its bulk matrix has spectral
norm at most \(C_T+1\). Equation (40) gives
\[
 \left\|\sqrt n[\dot X^{\rm app}
                        -F(X^{\rm app},e^0/\sqrt n)]\right\|
       \leq H_n^6a_n\qquad(t<\tau).                      \tag{46}
\]
Indeed (37) satisfies
\(\dot Y^{\rm lin}=J_cY^{\rm lin}+\sum_b\mathcal B_bg h_b\), and
the cavity satisfies its true equation before \(\tau_c\).

The actual input differs from \(e^0\) by \(\ell h_j\), of norm
\(C_T/\sqrt n\). At any bulk point with bounded matrix norm and
coordinatewise readout, \(D_EF\) has norm \(C_T\). To see this use the
\(e\)-terms in (24)--(25), whose bound uses the RMS reverse field, not
its maximum. The same calculation applies at any upper input, with
the corresponding fields. Integrating this derivative in \(E\) gives
\[
 \sqrt n\|F(X^{\rm app},e/\sqrt n)
                  -F(X^{\rm app},e^0/\sqrt n)\|
       \leq C_T/\sqrt n.                                 \tag{47}
\]

We spell out the stability estimate to avoid a hypothesis on secant
maxima. Compare two bulk states with the same upper input \(e\),
bounded matrix and readout norms, and write \(W=\sqrt n(X-X')\).
Exact product differences in (1) give
\[
 \|\Delta z^{(2)}\|+\|\Delta\delta\|+\|\Delta q_I\|
       \leq C_T\|W\|,\qquad
 |\Delta c|\leq C_T\|W\|/\sqrt n.                          \tag{48}
\]
For example
\(\Delta z^{(2)}=\Delta B h^{(1)}+B'\Delta h^{(1)}\) and
\(\Delta q_I=\Delta B^T\delta+(B')^T\Delta\delta\);
the \(\sqrt n\) from bounded features or backward fields cancels
the \(1/\sqrt n\) in \(\Delta B\). The readout bound makes the
derivative of \(\delta\) bounded in these physical coordinates.
For \(c\), the inner products have the additional \(1/n\).

Suppose the first state is actual and \(\max|q_I|\leq R_n\).
In the first-root update use the exact split
\[
 cpq-c'p'q'=(c-c')pq+c'(p-p')q+c'p'(q-q').                 \tag{49}
\]
The first term uses the RMS norm of \(q\), the second uses only the
actual maximum \(R_n\), and the third uses (48). Matrix and readout
updates are bounded by their product differences. Therefore
\[
 \sqrt n\|F(X,e/\sqrt n)-F(X',e/\sqrt n)\|
       \leq C_T(1+R_n)\|W\|.                             \tag{50}
\]
There is no assumption that \(q'\), or a secant reverse field, has
maximum below \(R_n\).

Apply (50) to actual \(X\) and \(X^{\rm app}\), with their common
actual input. They agree initially. Equations (46)--(47) and the
scalar integrating-factor inequality give
\[
 \sup_{t\leq\tau}
 \|\sqrt n(X(t)-\widehat X(t))-Y^{\rm lin}(t)\|
 \leq T e^{C_T(1+R_n)T}[H_n^6a_n+C_T/\sqrt n]
 \leq H_n^9a_n.                                          \tag{51}
\]
The estimates first hold for \(t<\tau\) and extend to its endpoint by
continuity. If \(\tau=0\), (51) holds because both bulk differences
are initially zero. The allowed maximum-based exponential here
multiplies an already vanishing nonlinear defect. It is not being
used to bound the leading scalar response.

Equations (41)--(44), (48), and (51) imply
\[
 \sup_{t\leq\tau}\max_a\{
 \|z^{(1)}_{a,I}-\widehat z^{(1)}_{a,I}\|_\infty,\quad
 \|w-\widehat w\|_\infty,\quad
 \|z^{(2)}_a-\widehat z^{(2)}_a\|_\infty,\quad
 \|\delta_a-\widehat\delta_a\|_\infty,\quad
 \|q_{a,I}-\widehat q_{a,I}\|_\infty\}
       \leq H_n^{12}a_n.                                 \tag{52}
\]
Explicitly, at the approximate state the upper increment is
\(\lambda_a+\beta_a\), with
\(\|\lambda_a\|_\infty\leq H_n^3a_n\) and
\(\|\beta_a\|_2\leq C_TH_n(H_n^3a_n+H_n/\sqrt n)\).
The actual-minus-approximate increment has Euclidean norm at most
\(C_TH_n^9a_n+C_T/\sqrt n\). These also bound the maximum.
For \(q_I\), use the linear \(dq_a\) bound in (39), the remainder
(44), and (48). The same argument applies to \(\delta\).
First-root and readout coordinates follow from (39) and (51).
Thus the upper-field and first-root delocalization estimates close
without a new stopping hypothesis on a difference. Also
\[
 \sup_{t\leq\tau}\|\sqrt n(X-\widehat X)\|\leq2H_n,\quad
 \|\delta_a-\widehat\delta_a\|\leq C_TH_n,\quad
 |c_a-\widehat c_a|\leq C_TH_n/\sqrt n.                    \tag{53}
\]
The distinguished root \(z_j\) is intentionally absent from (52):
it can differ substantially from \(\xi\).

## 7. Readback, traces, learned terms, and the initial root

At \(X^{\rm app}\) with zero upper input, apply (43). Its upper
linear coordinate \(Z_aY^{\rm lin}\) is covered by (35), or by
subtracting \(e_a^0\) in (39). This gives
\[
 \|\delta_a(X^{\rm app},0)-\widehat\delta_a-L_aY^{\rm lin}\|
       \leq C_TH_n(H_n^3a_n+H_n/\sqrt n).
\]
The actual-minus-approximate field difference at the same zero input
is at most \(C_TH_n^9a_n\), by (48) and (51). Since \(\|g\|\leq2\),
\[
 g^T(\delta_a^0-\widehat\delta_a)
       =g^TL_a(t)Y^{\rm lin}(t)+O(H_n^{12}a_n),            \tag{54}
\]
uniformly up to \(\tau\). The leading term is
\[
 g^TL_a(t)Y^{\rm lin}(t)
   =\sum_b\int_0^t h_b(s)\,g^TK_{ab}(t,s)g\,ds.
\]
Using (36) under this integral costs at most \(2B_1T H_n^2a_n\),
even though \(h_b(s)\) depends on \(g\). Equations (19) and (54)
prove (9). The trace normalization is \(1/n\), because the deleted
column has covariance \(I_n/n\), not \(1/m_n\).

For (12), compare the exact learned readback with its cavity
version. Equation (53) and
\[
 \delta_b(s)^T\delta_a(t)-\widehat\delta_b(s)^T\widehat\delta_a(t)
 =(\delta_b(s)-\widehat\delta_b(s))^T\delta_a(t)
       +\widehat\delta_b(s)^T(\delta_a(t)-\widehat\delta_a(t))
\]
give
\[
 \sup_{t\leq\tau,a}
 \left|M_a(t)-\sum_b\int_0^t m_{ab}(t,s)h_b(s)ds\right|
       \leq C_TH_n/\sqrt n.                             \tag{55}
\]
This includes the actual residual and the complete learned-column
history: their replacement errors have been estimated.

By (52), bounded third derivative of \(\phi_2\), and
\(\|e_a\|_\infty\leq B_1(\|g\|_\infty+\|\ell\|)\),
\[
 \sup_{t\leq\tau,a}\|D_a^{\rm dir}(t)-D_a(t)\|_{\rm op}
       \leq C_TH_n^{12}a_n.                             \tag{56}
\]
Its base input \(Bh^{(1)}_{a,I}\) differs from
\(\widehat z^{(2)}_a\) by the actual upper increment minus \(e_a\),
both already controlled in maximum norm. In \(S_a\), the term
with \(\ell\) costs \(C_T/\sqrt n\). Thus (36) and (56) yield
\[
 \sup_{t\leq\tau,a}|S_a(t)-d_a(t)h_a(t)|
       \leq H_n^{15}a_n.                                \tag{57}
\]
All errors (54)--(57) fit within \(H_n^{20}a_n\), by the choice of
\(A_*\). Definitions and (14) give
\(\sup|d_a|+\sup|m_{ab}|\leq C_T\), proving (12).

At time zero the bulk parameters agree, but the fields do not:
\[
 z^{(2)}_a(0)-\widehat z^{(2)}_a(0)=g\phi_1(\xi_a),
\]
\[
 \delta_a(0)-\widehat\delta_a(0)
 =w(0)\odot[\phi_2'(\widehat z^{(2)}_a(0)+g\phi_1(\xi_a))
                      -\phi_2'(\widehat z^{(2)}_a(0))],
\]
\[
 c_a(0)-\widehat c_a(0)
 =-{2\over n}w(0)^T[
 \phi_2(\widehat z^{(2)}_a(0)+g\phi_1(\xi_a))
                  -\phi_2(\widehat z^{(2)}_a(0))].         \tag{58}
\]
Thus \(Y^{\rm lin}(0)=0\) is correct: the initial field mismatch is
the nonzero input \(e_a^0(0)=g\phi_1(\xi_a)\). Its linear residual
effect is precisely the \(e_a\) term in \(\chi_a\) in (24).
The exact initial scalar is
\[
 q_{a,j}(0)=G_a(0)+\phi_1(\xi_a)g^TD_a^{\rm dir}(0)g.       \tag{59}
\]
The initial local first root is included in (9) and in the direct
trace approximation (12); it is not absorbed into an independent
Gaussian. At positive times its role is played by the actual path
from (17), not by a path independently sampled from it.

## 8. Conditioning, initialization, and remaining obligations

All probability estimates above are conditional only on
\(\mathcal F_{-j}\), on its measurable event \(\mathcal C_n\).
Gaussian and quadratic estimates were established on the whole
deterministic square/triangle of times, using the cavity's own
frozen extension. The actual stop is used afterwards, by pathwise
restriction and deterministic comparison on \(t\leq\tau\).
Neither \(\tau_f\) nor an actual-trajectory event was inserted into
a kernel before applying a Gaussian estimate. In particular the
theorem does not state a Gaussian law conditional on \(\tau_f=T\).

The initialization restriction has a high-probability bound without
a dynamical assertion. A \(1/4\)-net on the unit sphere in
\(\mathbb R^k\) has at most \(9^k\) points: take a maximal separated
set and compare volumes of its disjoint balls of radius \(1/8\)
with the ball of radius \(9/8\). Approximating both vectors in a
bilinear form bounds a matrix norm by twice its maximum form on
the two nets. For \(B(0)\in\mathbb R^{n\times(n-1)}\), each form
has Gaussian variance \(1/n\). Using (30) at threshold \(4\),
\[
 \Pr(\|B(0)\|_{\rm op}>8)
       \leq2\exp[-(8-2\log9)n].                          \tag{60}
\]
For any fixed \(q_*>0\), the scalar Gaussian bound gives
\[
 \Pr\{\|w(0)\|_\infty>
              \sqrt{2(q_*+2)\log n}/n\}\leq2n^{-(q_*+1)}. \tag{61}
\]
On these complementary events,
\[
 \max_{i,a}|\widehat q_{a,i}(0)|
       \leq8\|\phi_2'\|_\infty\sqrt{2(q_*+2)\log n/n}.
\]
This is below \(R_n\) whenever
\(n>[8\|\phi_2'\|_\infty\sqrt{2(q_*+2)}/K]^2\); (61)'s
threshold is also below \(1\) for sufficiently large \(n\).
Hence (4) is a natural high-probability initialization event.
This supplies no bound on a positive-time stopping probability.

The leading response in this calculation is the independent cavity
trace, and its nonlinear approximation error is \(n^{-1/2+o(1)}\).
The potentially missing coordinate estimate, for
\(Z_a(t)U_c(t,s)\mathcal B_b(s)g\), has bounded row variance by (28)
and is controlled uniformly by (35). It controls the quadratic
upper-gate remainder in (43). The first-root curvature remainder
is controlled separately by (41), with the allowed factor \(R_n\).
No unresolved coordinate estimate remains in this gradient-flow
stopped approximation.

Two distinct obligations remain outside it: a width-uniform bound
on the trace response acting on the actual bounded path, and a
proof that the actual and cavity maximum-field stops can be removed.
In particular (28) only gives
\(|\kappa_{ab}|\leq C_Te^{C_T(1+R_n)T}\), which need not be bounded
as \(n\to\infty\). This does not deny a weaker fixed-neuron scalar
tail obtainable by other arguments. Exact raw GD, including its
simultaneous-update propagator and raw interpolation, is not
proved by this continuous-time calculation.

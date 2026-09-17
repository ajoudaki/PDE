# Three correlated inputs in three coordinates: an explicit alternative

2026-09-16. Frozen analytic candidate. This is a **d=3 extension**, using the
exact general-dimensional p=1 coefficients of `docs/observable_p1.md`.
It is not a solution of the original d=2 three-input circle problem, nor an
identification with a trained-network limit. No experiment is used. Nothing
is promoted to `docs/` or `code/`.

Scientific inputs were `docs/NOTATION.md`, the complete
`docs/observable_p1.md`, the state/dynamics/existence sections of
`docs/global_nonlinear.md` C.4.7.9 and C.4.7.10 B/C.1/D.3, this study's
`scalar_margin_extension.md` and `all_angles_result.md`, and, following an
explicit scope extension, Sections 1–4 of `arbitrary_pair_local.md` and its
initialization audit. The population existence argument below is supplied
directly in three coordinates; no d=2 network theorem is extended silently.

The proof establishes the full metric gradient, exact permutation symmetry,
rank-three initialization, a normalized-readout bound, and an exponentially
decaying mixed potential. All constants are determined by initialized
Gaussian expectations and the prescribed inputs. The endpoint and auxiliary
clock are proof objects only.

## 1. Statement and scope

Choose real a,b with

\[
 a^2+2b^2=1,\qquad a\ne b,
\]

and put

\[
 v_1=(a,b,b),\quad v_2=(b,a,b),\quad v_3=(b,b,a),
 \qquad (u_1,u_2,u_3)=(v_1,v_2,-v_3).
\]

The physical inputs are x_i=sqrt(3) u_i, labels are (1,1,-1), and all
three data weights are 1/3. Use the exact correlated Gaussian p=1 marks,
the prescribed eta=1/4096 Cholesky normalization, the full 4-by-7 evolving
matrix M with its actual transpose, and initial (w,c,M)=(g,0,D).

Write H_i=H^2(v_i) and define from the current state

\[
 U=\frac{H_1+H_2+H_3}{3},\qquad
 F=E_2[cU],\qquad q=E_2[c^2],\qquad C=E_2[U^2],
 \qquad C_0=E_2[U_0^2].                                      \tag{1}
\]

The exact initialized upper-field Gram of the three original inputs has
rank three. In particular C_0>0. The unique initialized characteristic
solution exists for all physical times and has

\[
 f(u_1)=f(u_2)=-f(u_3)=F,\qquad 0\le F<1\quad(t<\infty),
 \qquad \mathcal L=(1-F)^2.
\]

A nonsingular current-state mixed potential is

\[
 \Psi=\frac{1+q}{C_0+F^2},\qquad
 \Phi=\mathcal L\left(1+C_0\Psi\right).                  \tag{2}
\]

Along this initialized full flow,

\[
 \mathcal L\le\Phi\le2\mathcal L,\qquad
 \dot\Phi\le-4C_0\Phi,\qquad \Phi(0)=2,                 \tag{3}
\]

so the requested bound holds with lambda=4C_0 and h(z)=z. Also

\[
 \mathcal L(t)\le e^{-4C_0t},\qquad C(t)\ge C_0,
 \qquad q(t)\le\frac{F(t)^2}{C_0}\le\frac1{C_0}.          \tag{4}
\]

In the physical population-L2/Frobenius metric specified below,

\[
 \int_t^\infty\|\dot X(r)\|\,dr
 \le\sqrt{\mathcal L(t)/C_0}.                            \tag{5}
\]

Consequently the full state converges strongly to a fitting state. In
addition w-g and c converge in their population essential-supremum norms,
M converges in Frobenius norm, and the complete joint population laws
converge in W2 using their ordinary Euclidean coordinate metrics.

These conclusions concern the initialized symmetry class. They assert
neither a coercive Lyapunov inequality on every ambient state nor uniqueness
of the fitting state. All entries of the middle matrix are evolved by the
full equation; its initialization pattern is not imposed as a constraint.

The family contains genuinely correlated examples. For a=2/sqrt(6),
b=1/sqrt(6), the label-absorbed off-diagonal input inner products equal
5/6. The original input inner products are 5/6,-5/6,-5/6. The three input
vectors in this example are linearly independent. For the entire stated
family the three initialized hidden constraints are independent, even
when the input vectors themselves have a linear relation. No pair of
these inputs is an antipodal duplicate.

## 2. Exact initialization and physical gradient

Use independent lower coordinates G_i~N(0,1), zeta_i~N(0,tau), i=1,2,3,
and independent upper coordinates Xi_i~N(0,v). The two populations are
separate. Set

\[
 v=E\tanh^2G,\quad \tau=E\tanh^2(\sqrt vG),\quad
 \alpha=1-\tau,\quad h_i=\tanh G_i,
 \quad k_i=\tanh(\zeta_i+\alpha h_i),\quad Z_i=\tanh\Xi_i,
\]
\[
 \beta=E[h_i k_i],\quad \sigma=E[k_i^2],\quad
 \gamma=1-\sigma,\quad \eta=1/4096,
\]
\[
 R_h=\sqrt{v+\eta},\quad
 R_k=\sqrt{\sigma+\eta-\beta^2/(v+\eta)},\quad
 R_Z=\sqrt{\tau+\eta}.
\]

The construction below is specified entirely by finite initialized
coefficients; it needs no operational uncompressed-action query.

The actual normalized feature columns are

\[
 b_1=\left((1+\eta)^{-1/2},\ h/R_h,
                 (k-\beta h/(v+\eta))/R_k\right)^T,
 \qquad
 b_2=\left((1+\eta)^{-1/2},\ Z/R_Z\right)^T.             \tag{6}
\]

The frozen initialized D has zero constant row/column and exactly

\[
 D_{Z_i,h_i}=\frac{\alpha v}{R_hR_Z},\qquad
 D_{Z_i,k_i}
 =\frac{\alpha\beta\eta/(v+\eta)+\tau\gamma}{R_kR_Z}.   \tag{7}
\]

In particular the reverse-response term tau gamma is retained. Positivity
of the denominators follows from v,tau,sigma>0 and beta^2<=v sigma.
The joint lower correlation between G_i and k_i is retained exactly.

The formulas (6) are the inverse lower-Cholesky normalization of the raw
columns (1,h_1,h_2,h_3,k_1,k_2,k_3) and (1,Z_1,Z_2,Z_3).
If U_l maps a coefficient vector z to b_l^T z, then

\[
 U_l^*U_l=E_l[b_l b_l^T]
       =I-\eta L_l^{-1}L_l^{-T}\le I.                    \tag{8}
\]

Thus both feature maps and their adjoints are contractions. Their finite
supremum envelopes B_l=ess sup |b_l| are finite. Set d_0=||D||op<infinity;
no unproved general-dimensional bound on an uncompressed action is needed.

For a current characteristic state X=(w,c,M), and any unit u, put

\[
 H^1(u)=\tanh(w\cdot u),\quad a(u)=E_1[b_1H^1(u)],
 \quad Z^2(u)=b_2^TMa(u),\quad H^2(u)=\tanh Z^2(u),
\]
\[
 d(u)=E_2[b_2c\,\operatorname{sech}^2Z^2(u)],\qquad
 Q(u)=b_1^TM^Td(u),\qquad f(u)=E_2[cH^2(u)].            \tag{9}
\]

The constant physical metric is

\[
 \|\delta X\|^2
 =E_1|\delta w|^2+E_2|\delta c|^2+\|\delta M\|_F^2.     \tag{10}
\]

Differentiating (9) gives its full gradient in this metric:

\[
 \nabla_c f(u)=H^2(u),\qquad
 \nabla_M f(u)=d(u)a(u)^T,\qquad
 \nabla_w f(u)=\operatorname{sech}^2(w\cdot u)Q(u)u.     \tag{11}
\]

For example, delta f=d(u)^T(delta M)a(u) in the middle block.
In the row block delta a=E_1[b_1 sech^2(w dot u)(delta w dot u)];
contracting this with M^T d yields the last expression. This verifies
both the actual transpose and all metric factors. All relevant integrands
have bounded features and gates and integrable row/readout factors, so
the variations and chain rules follow by dominated convergence. The
remainder in the row variation is bounded by a constant times
E_1|delta w|^2; the resulting Hilbert gradients are valid at the
characteristic states used below.

For the unhalved weighted loss, the full equations are

\[
 \dot X=-\nabla\mathcal L
       =-\frac23\sum_{i=1}^3(f(u_i)-y_i)\nabla f(u_i).   \tag{12}
\]

Equations (11)–(12) are exactly the general-d p=1 closure equations.
In particular

\[
 \dot{\mathcal L}=-\|\dot X\|^2.                       \tag{13}
\]

## 3. Population existence and restart in d=3

Work on the frozen joint mark probability spaces in the Banach space

\[
 (w-g,c,M)\in L^\infty(\Omega_1;\mathbb R^3)
            \times L^\infty(\Omega_2)
            \times\mathbb R^{4\times7}.                \tag{14}
\]

The unbounded Gaussian g remains fixed. On each bounded set in (14),
the vector field (12) is locally Lipschitz: subtract its finite products,
use the finite B_l, |u_i|=1, |tanh'|<=1 and Lip(sech^2)<=2, and contract
against probability measures. The fixed g occurs only inside bounded
gates and does not enter a Lipschitz constant for w-g differences.

For completeness, integrate the vector field on continuous paths in a
closed ball about the initial state. A sufficiently short time interval
makes its integrated speed smaller than the ball radius and its Lipschitz
constant times the interval smaller than one. Successive iterations
therefore converge in this complete path space; the integral identity
gives a solution, and the same contraction gives local uniqueness.
This proves the needed local characteristic result without appealing to
a higher-dimensional network-existence theorem.

Here is finite-time continuation, independently of the symmetry argument.
Equation (13) and mathcal L(0)=1 give sum_i |r_i|/3<=1. By (8),
|a(u)|<=1 and |d(u)|<=||c||_2. Hence

\[
 \|c(t)\|_\infty\le2t,\qquad
 \|M(t)-D\|_F\le2t^2,\qquad
 \|M(t)\|_{\rm op}\le d_0+2t^2.                       \tag{15}
\]

The lower speed satisfies

\[
 \|\dot w(t)\|_\infty
 \le4B_1t(d_0+2t^2),\qquad
 \|w(t)-g\|_\infty\le B_1(2d_0t^2+2t^4).             \tag{16}
\]

Indeed |Q(u)|<=B_1||M||op |d(u)|. These bounds prevent finite-time escape
from (14). On each finite interval the speeds are bounded as well, so a
putative finite maximal endpoint has a Cauchy limit in (14), to which the
local contraction applies. This proves global characteristic existence
and uniqueness for the initialized physical flow.

The same local argument starts from any reached saved joint law and finite
matrix; the saved law includes all current correlations of b,g,w or b,c.
The next velocities depend only on those laws and M. No extra elapsed-time
coordinate or past trajectory is required at restart. The theorem concerns
this characteristic solution class, not arbitrary uncontrolled weak
solutions of a formal continuity equation.

## 4. The exact permutation symmetry and full-block scalar reduction

At every state, oddness in the input gives H^2(-u)=-H^2(u) and
f(-u)=-f(u). Therefore, as functions of the entire ambient state,

\[
 \mathcal L(X)=\frac13\sum_{i=1}^3(f(v_i)-1)^2.          \tag{17}
\]

This is exact absorption of the negative label, not a deletion of a
constraint. The fields for these three inputs will have full rank at
initialization.

Let P be any 3-by-3 coordinate permutation matrix. Permuting each full
lower coordinate pair by S_1(G,zeta)=(PG,Pzeta), and the upper marks by
S_2 Xi=P Xi, preserves the two Gaussian laws. By the explicit features,

\[
 b_1\circ S_1=Q_1b_1,\qquad b_2\circ S_2=Q_2b_2,
 \qquad Q_1=\operatorname{diag}(1,P,P),\quad
 Q_2=\operatorname{diag}(1,P).                          \tag{18}
\]

Both Q_l are orthogonal. The block scalar Cholesky factors in (6) commute
with these Q_l; thus (18) is the action on the normalized dictionary, not
an assumption about unnormalized features. Formula (7) also gives

\[
 Q_2^TDQ_1=D.                                         \tag{19}
\]

Define a transformation of the full state by

\[
 T_P(w,c,M)=
    (P^Tw\circ S_1,\ c\circ S_2,\ Q_2^TMQ_1).          \tag{20}
\]

It fixes (g,0,D), preserves (14), and is an isometry for (10), because
the mark maps preserve probability and the three finite matrices acting
on coordinates are orthogonal. Substitution and a change of variables give

\[
 a_{T_PX}(u)=Q_1^Ta_X(Pu),\qquad
 H^2_{T_PX}(u)=H^2_X(Pu)\circ S_2,
 \qquad f_{T_PX}(u)=f_X(Pu).                           \tag{21}
\]

For example b_2^TQ_2^TMQ_1Q_1^Ta_X(Pu)
equals (b_2 composed with S_2)^TM a_X(Pu), proving the upper identity.
The reverse uses the transpose of that same transformed M. Consequently
this is an isometry of the complete action and gradient, not merely a
symmetry of the three initialized predictions.

The set {v_1,v_2,v_3} is permuted transitively by P, so both mathcal L
in (17) and F=(f(v_1)+f(v_2)+f(v_3))/3 are invariant under T_P.
For an invariant differentiable function J and an isometry T_P,
the chain rule gives grad J(T_P X)=T_P grad J(X) on tangent vectors:
pair either side with T_P delta X and use preservation of the metric.
Thus the transformed solution solves the same ODE from the same initial
state. Uniqueness yields T_P X(t)=X(t) for every permutation and time.
Equation (21) then implies f(v_1)=f(v_2)=f(v_3)=F.

At such a state, differentiating the ambient loss, rather than just its
restriction to the invariant set, gives

\[
 \nabla\mathcal L
 =\frac23\sum_i(F-1)\nabla f(v_i)
 =2(F-1)\nabla F.
\]

Hence the exact full-block physical flow is

\[
 \dot X=2(1-F)\nabla F.                               \tag{22}
\]

In particular the three gradients remain averaged; no equality of their
individual row, matrix, or readout components was assumed.

## 5. Exact initialized scalar map and rank three

This section gives the dimension transfer and the essential analytic
initialization details explicitly. Introduce fixed scalar coefficients
(A,B), distinct from the input coordinates (a,b), by

\[
 (A,B)=(\alpha v,\alpha\beta+\tau\gamma)
 \begin{pmatrix}v+\eta&\beta\\\beta&\sigma+\eta\end{pmatrix}^{-1}.
\]

The normal equations give

\[
 B=\frac{\alpha\beta\eta/(v+\eta)+\tau\gamma}
          {\sigma+\eta-\beta^2/(v+\eta)}>0,\qquad
 A=\frac{\alpha v-B\beta}{v+\eta}.                     \tag{23}
\]

Define m(x)=E_zeta tanh(zeta+alpha x), j(g)=A tanh g+B m(tanh g), and

\[
 \kappa(t)=\frac1{\tau+\eta}
    E[j(G)\tanh(tG+\sqrt{1-t^2}\,Z)],\qquad -1\le t\le1,
                                                                  \tag{24}
\]

where G,Z are independent standard Gaussians. Then the exact initialization
for every u in S^2 is

\[
 Z^2_0(u)=\sum_{i=1}^3 Z_i\kappa(u_i),\qquad
 H^2_0(u)=\tanh\left(\sum_i Z_i\kappa(u_i)\right).      \tag{25}
\]

Indeed eliminating the Cholesky factors in b_2^TD E_1[b_1 tanh(g dot u)]
gives exactly

\[
 \psi_2^T(G_2+\eta I)^{-1}C_{\rm raw}
           (G_1+\eta I)^{-1}E_1[\psi_1\tanh(g\cdot u)].
\]

The constant terms vanish, the lower independent coordinate blocks give
(23), and the upper odd block contributes 1/(tau+eta). Conditional
averaging over each coordinate's own independent reverse noise gives j.
Finally (g_i,g dot u) is a centered Gaussian pair of unit variances and
correlation u_i, irrespective of dimension; the sum of the other two
Gaussian coordinates is an independent Gaussian with variance 1-u_i^2.
This proves (24)–(25), including u_i=+/-1. It uses no rotation of the
feature dictionary.

Here is a direct monotonicity verification, retaining the possibility
A<0 in (23). Set

\[
 b_*(x)=E_\zeta\operatorname{sech}^2(\zeta+\alpha x),
 \quad b_*=b_*(0),\quad q_*=529/1024.
\]

The inequality tanh^2 z>=z^2/(1+z^2) follows from sinh^2 z>=z^2.
For V~N(0,s), Cauchy–Schwarz gives

\[
 E\frac{V^2}{1+V^2}\ge\frac{(EV^2)^2}{E[V^2+V^4]}
 =\frac{s}{1+3s}.
\]

Applying this first at s=1 and then at s=v gives v>=1/4, tau>=1/7,
and 0<alpha<=6/7. Gaussian convolution of sech^2 is maximal at zero:
its level sets are centered intervals, and a centered Gaussian assigns
no more mass to any translated interval than to its centered translate.
The latter assertion follows by differentiating the interval probability;
the Gaussian density decreases with absolute argument. Integrating the
nonnegative level-set probabilities proves b_*(x)<=b_*.

Pairing zeta and -zeta in the sech-squared addition formula gives

\[
 b_*(x)\ge b_*\operatorname{sech}^2(\alpha x).
\]

Explicitly the paired integrand, divided by sech^2(zeta) sech^2(alpha x),
is (1+tanh^2(zeta)tanh^2(alpha x)) divided by
(1-tanh^2(zeta)tanh^2(alpha x))^2, which is at least one.
For 0<=z<=6/7, the coefficient bound (2n)!>=2*12^(n-1) gives

\[
 \cosh z\le1+\frac{z^2/2}{1-z^2/12}\le32/23.
\]

Consequently

\[
 q_*b_*\le b_*(x)\le b_*\qquad(|x|\le1).              \tag{26}
\]

Conditional Gaussian integration by parts, whose bounded factors make
the boundary terms zero, gives
Cov(zeta,tanh(zeta+alpha x))=tau b_*(x). Conditional Cauchy–Schwarz
therefore bounds its variance below by tau b_*(x)^2. Averaging and
using E m(h)^2>=beta^2/v gives

\[
 \sigma+\eta-\frac{\beta^2}{v+\eta}
 \ge\tau E b_*(h)^2+\eta\ge\tau\gamma^2+\eta.           \tag{27}
\]

As m'(x)=alpha b_*(x), one has 0<beta<=alpha v, and (23)–(27) imply

\[
 0<B\le\frac{\tau\gamma+\eta/\gamma}{\tau\gamma^2+\eta}
 =\frac1\gamma\le\frac1{q_*b_*}.                       \tag{28}
\]

For the numerator inequality, alpha beta eta/(v+eta)<=eta<=eta/gamma.
Also beta<=alpha b_*v. Put R_eta=v/(v+eta), for which
1024/1025<=R_eta<1 and R_eta>q_*. The exact derivative obeys

\[
 \begin{aligned}
 \frac d{dx}(Ax+Bm(x))
 &=\alpha R_\eta+B\left(\alpha b_*(x)-\frac\beta{v+\eta}\right)\\
 &\ge\alpha R_\eta-B\alpha b_*(R_\eta-q_*)\\
 &\ge\alpha[1-R_\eta(q_*^{-1}-1)]
 \ge\alpha(2-q_*^{-1})=\frac{34\alpha}{529}>0.
 \end{aligned}                                                   \tag{29}
\]

Thus j is odd and j'(g)>=34alpha sech^2(g)/529. Differentiating (24)
for -1<t<1 and integrating by parts in G and Z cancels the second-gate
derivative terms, giving

\[
 \kappa'(t)=\frac1{\tau+\eta}
 E[j'(G)\operatorname{sech}^2(tG+\sqrt{1-t^2}Z)]>0.     \tag{30}
\]

For example the differentiated Gaussian factors are G-tZ/sqrt(1-t^2);
the G integration produces E[j' sech^2]+t E[j tanh''], and the Z
integration cancels the latter summand. Bounded derivatives and Gaussian
moments justify both operations on interior compact intervals. The
right side is bounded and continuous up to t=+/-1 by dominated
convergence, and (24) is continuous there. Integrating the derivative
to the endpoints proves strict increase on [-1,1]. Gaussian symmetry
also gives kappa(-t)=-kappa(t). This completes the needed scalar result
without a numerical sign test or an assumed sign for A.

Set p=kappa(a), z=kappa(b). Since a!=b, one has p!=z. The three
coefficient vectors in (25) are the rows of

\[
 V=(p-z)I_3+z\mathbf1\mathbf1^T.                        \tag{31}
\]

The law of the raw upper mark Z=(Z_1,Z_2,Z_3) has positive density on
(-1,1)^3. Suppose sum_i t_i H^2_0(v_i)=0 in upper L2. Continuity and
this positive density extend the identity to the entire open cube.
Differentiating it at Z=0 gives V^T t=0.

If p+2z!=0, the eigenvalues p-z,p-z,p+2z of V are all nonzero, so
t=0. If p+2z=0, the first two eigenvalues remain nonzero and hence
t=t_0(1,1,1). Here z!=0, since otherwise p=z=0. Restricting to
Z=(r,0,0) and differentiating three times at r=0 gives

\[
 0=-2t_0(p^3+2z^3)=12t_0z^3,
\]

because p=-2z and tanh'''(0)=-2. Again t=0. Thus the three fields
are linearly independent in every admitted case. The original third
field is their third field times -1; this diagonal sign change preserves
Gram rank. In particular

\[
 C_0=\frac19E_2(H^2_0(v_1)+H^2_0(v_2)+H^2_0(v_3))^2>0.  \tag{32}
\]

This also distinguishes the construction from an antipodal one-feature
reduction. For example v_1=-v_2 would force b=0 from their third
coordinates and then a=0 from their first two, contradicting unit norm.
The other pairs are treated by permutation; v_i=v_j would force a=b.
Changing the sign of v_3 cannot create a coincident or antipodal pair.

## 6. Autonomous gradient curve and noncollapse

Consider X_s=grad F from the same initialized state. This auxiliary
autonomous curve uses the same current-state F as (1); it is used only
to prove statements about physical time. By (11) its full equations are

\[
 c_s=U,\qquad
 M_s=\frac13\sum_i d(v_i)a(v_i)^T,\qquad
 w_s=\frac13\sum_i\operatorname{sech}^2(w\cdot v_i)Q(v_i)v_i.
                                                               \tag{33}
\]

The same local Lipschitz proof applies, and all finite feature times exist:

\[
 \|c(s)\|_\infty\le s,\qquad
 \|M(s)\|_{\rm op}\le d_0+s^2/2,
\]
\[
 \|w(s)-g\|_\infty
 \le B_1(d_0s^2/2+s^4/8).                              \tag{34}
\]

These follow successively from |U|<=1, ||M_s||F<=||c||2<=s, and
||w_s||infinity<=B_1(d_0+s^2/2)s. Bounded speeds give Cauchy endpoints
and continuation exactly as in Section 3. The same permutation isometries
preserve F, so uniqueness keeps (33) in their fixed-point set as well.

Write h=(w,M) and

\[
 K=\|\nabla F\|^2=C+\|\nabla_hF\|^2.
\]

Linearity of F=<c,U(h)> in c gives the exact identities

\[
 F_s=K,\qquad q_s=2F.                                  \tag{35}
\]

At s=0 the hidden gradient vanishes because c=0, while c_s(0)=U_0.
Continuity of the vector field therefore gives

\[
 c(s)=sU_0+o(s),\quad F(s)=C_0s+o(s),\quad
 q(s)=C_0s^2+o(s^2).                                   \tag{36}
\]

Since C_0>0, F>0 initially; F_s=K>=0 keeps F positive for all s>0.
Then q>0 as well. Cauchy–Schwarz gives F^2<=qC<=qK. Consequently

\[
 \left(\frac q{F^2}\right)_s
 =-\frac{2(qK-F^2)}{F^3}\le0,\qquad
 \lim_{s\downarrow0}\frac q{F^2}=\frac1{C_0}.           \tag{37}
\]

Integrate first on [r,s] with r>0 and then let r decrease to zero.
This justifies the singular one-sided limit and yields

\[
 q\le F^2/C_0,\qquad C\ge F^2/q\ge C_0,
 \qquad K\ge C_0.                                     \tag{38}
\]

There is no assumed persistent full-Gram coercivity here: the proof uses
only the actual residual symmetry and the scalar feature U. The complete
initial Gram is rank three, but no claim about its smallest eigenvalue
at every later time is needed.

The nonsingular function Psi in (2) satisfies its full derivative

\[
 \Psi_s
 =-\frac{2F[(qK-F^2)+(K-C_0)]}{(C_0+F^2)^2}\le0.        \tag{39}
\]

The exact deficit decomposes as

\[
 qK-F^2=(qC-F^2)+q\|\nabla_hF\|^2\ge0.                 \tag{40}
\]

It measures current readout/feature misalignment and current hidden
gradient activity. Neither term contains the past trajectory or an
unknown fitting endpoint. The feature norm C itself is not asserted
to be monotone.

## 7. Physical time, the mixed potential, and the full-state limit

Since F_s>=C_0 and F(0)=0, continuity and strict increase give a unique
s_* in (0,1/C_0] with F(s_*)=1. On the compact interval [0,s_*], K is
continuous, finite, and at least C_0. Solve

\[
 \dot s=2(1-F(s)),\qquad s(0)=0.
\]

The scalar right side is Lipschitz on this interval. Its residual
e(t)=1-F(s(t)) satisfies

\[
 \dot e=-2K(s(t))e,\qquad
 e(t)=\exp\left(-2\int_0^tK(s(r))\,dr\right)>0.         \tag{41}
\]

Boundedness of K on [0,s_*] prevents reaching s_* at finite t. Also
e<=exp(-2C_0t), which forces s(t) to increase to s_*. By (22)–(33),
the composed curve X(s(t)) solves every physical block equation from
the prescribed initialization. Uniqueness identifies it with the global
solution of Section 3. This is a proof reparametrization of that solution,
not a different optimizer or a time input supplied to the closure.

Equations (38)–(41) give (4) and the physical derivative

\[
 \dot\Psi
 =-\frac{4eF[(qK-F^2)+(K-C_0)]}{(C_0+F^2)^2}\le0.        \tag{42}
\]

The nonsingular potential Phi is defined even at initialization. Along
the whole initialized path, (38) implies 0<C_0 Psi<=1, and therefore
mathcal L<=Phi<=2 mathcal L. Moreover mathcal L_dot=-4K mathcal L, so

\[
 \begin{aligned}
 \dot\Phi
 &=-4K\mathcal L(1+C_0\Psi)+C_0\mathcal L\dot\Psi\\
 &=-4K\Phi
 -\frac{4C_0e^3F[(qK-F^2)+(K-C_0)]}{(C_0+F^2)^2}\\
 &\le-4C_0\Phi.
 \end{aligned}                                                   \tag{43}
\]

This includes the derivative of the readout-dependent factor; the
physical metric itself remains (10). At initialization C_0 Psi=1,
so Phi(0)=2. Equations (3) and the exponential potential bound follow.

Finally ||X_dot||=2e sqrt(K), whereas -e_dot=2eK. By K>=C_0,

\[
 \|\dot X\|\le-\dot e/\sqrt{C_0}.
\]

Integrating from t to infinity proves (5). Completeness of the physical
Hilbert space gives strong full-state convergence, and continuity of
the finite-feature-time curve identifies its limit as X(s_*). Bounds
(34) and their bounded speeds on [0,s_*] give convergence also in
(14), not merely in the physical norm. The limit fits all three original
labels, since F tends to one and the signed-prediction identities persist.

For the saved laws Gamma_1=Law(b_1,g,w), Gamma_2=Law(b_2,c), couple the
complete frozen marks identically at time t and the endpoint. The squared
Euclidean W2 transportation costs are bounded respectively by
E_1|w(t)-w_*|^2 and E_2|c(t)-c_*|^2. They vanish. Frozen b is bounded,
g has finite Gaussian second moment, and the moving increments are
bounded, so these are actual finite-second-moment laws. No joint law
across the two separate populations is introduced.

## 8. What this settles, and what it does not

This is an exact all-time theorem for the stated correlated three-input,
three-coordinate p=1 closure and prescribed initialization. It supplies
a present-state mixed potential with exponential decay, explicit loss
control, positive initialized rank three, and a fitting full-state limit.
The exact symmetry forces one signed residual direction along this
particular initialized flow; the three independent input constraints
have not been replaced by duplicated data.

The theorem exploits the S3 symmetry of this particular dictionary and
data family. It does not establish generic three-input convergence,
generic label convergence, arbitrary rotational invariance, monotone
hidden-feature norm, or strict hidden-feature improvement. The bound
C(t)>=C_0 is proved; a strict endpoint increase is not asserted here.
No d=3 network-identification or closure-order-accuracy statement has
been added. The original d=2 circle question remains a separate target.

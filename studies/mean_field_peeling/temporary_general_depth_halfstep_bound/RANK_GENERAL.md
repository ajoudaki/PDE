# General-depth two-time ranks

This note proves the rank part of the width-first comparison

\[
 \Delta_L(h)=F_{2,L}(h)-F_{1,L}(2h)
\]

for a network with \(L\ge2\) hidden layers.  It uses only the inverse-free
Gaussian operator DAG obtained after the fixed-\(h\) width limit.  In
particular, it does not Taylor-expand a finite-width network and does not
invoke an initialization/dynamics intertwining identity.

For \(L=1\), both collections (3)--(4) below are empty: there is no reused
hidden matrix and hence no conditioning-rank obligation.  One may set the
rank radius to \(1/2\).  Thus the nontrivial rank induction starts at
\(L=2\).

Throughout, \(G\sim N(0,1)\),

\[
 \mathbb E\phi(G)^2=1,
 \qquad
 M_\phi=
 \max\left\{1,
 \sup_x\frac{|\phi(x)|}{1+|x|},
 \max_{1\le j\le12}\|\phi^{(j)}\|_\infty\right\}<\infty .       \tag{1}
\]

The notation for a hidden layer is

\[
 Z_{a,s}=\hbox{preactivation},\quad
 X_{a,s}=\phi(Z_{a,s}),\quad
 \Delta_{a,s}=R_{a,s}\phi'(Z_{a,s}),
 \qquad 1\le a\le L.                                      \tag{2}
\]

Here \(R_{L,s}\) is the readout weight and, for \(a<L\), \(R_{a,s}\)
is the full back-propagated carrier entering layer \(a\).  Define the
two-time population Grams

\[
 Q^{a,[1]}(h)=
 \bigl(\mathbb E[X_{a,r}X_{a,t}]\bigr)_{0\le r,t\le1},
 \qquad 1\le a\le L-1,                                    \tag{3}
\]

\[
 K^{a,[1]}(h)=
 \bigl(\mathbb E[\Delta_{a,r}\Delta_{a,t}]\bigr)_{0\le r,t\le1},
 \qquad 2\le a\le L.                                     \tag{4}
\]

These are exactly the \(2(L-1)\) nonterminal Grams inverted by the
adaptive conditioning proof for two recomputed steps.  No three-time Gram
is included.

## 1. Exact rank theorem

Put, with \(g=\phi(G)\), \(p=\phi'(G)\), \(q=\phi''(G)\), and
\(t=\phi'''(G)\),

\[
\begin{array}{lll}
 d=\mathbb Ep^2,&u=\mathbb Ep^4,&v=\mathbb E[gq],\\
 m=\mathbb E[gp^2q],&r=\mathbb E[pt],&s=\mathbb Eq^2,\\
 e=\mathbb E[p^2q^2],&&\ell=\mathbb E[g^2p^2].
\end{array}                                                  \tag{5}
\]

Assume first that \(d>0\).  Define

\[
 \Theta_0=1,
 \qquad
 \Theta_a=1+d\Theta_{a-1}=\sum_{j=0}^{a}d^j,               \tag{6}
\]

\[
 b_a=d^{L-a},
 \qquad
 \pi_a=db_a=d^{L-a+1}.                                    \tag{7}
\]

The number \(b_a\) is the initialization variance of \(R_{a,0}\), and
\(\pi_a\) is the initialization variance of \(\Delta_{a,0}\).

Define the forward tangent variances by

\[
 V_0=0,
 \qquad
 V_1=b_1u,                                                   \tag{8}
\]

and, for \(2\le a\le L\),

\[
 V_a=dV_{a-1}+\Theta_{a-1}^2b_au.                           \tag{9}
\]

Define the reverse tangent quantities from top to bottom by

\[
 \beta_{L+1}=0,
 \qquad
 \gamma_{L+1}=1,                                           \tag{10}
\]

and, for \(a=L,L-1,\ldots,1\),

\[
\boxed{
\begin{aligned}
 \beta_a={}&b_aV_{a-1}s
 +3\Theta_{a-1}^2b_a^2e+d\beta_{a+1}
 +\gamma_{a+1}^2\ell\\
 &+2\Theta_{a-1}\gamma_{a+1}b_am,
\end{aligned}}                                               \tag{11}
\]

\[
\boxed{
 \gamma_a
 =\pi_a+\Theta_{a-1}b_a(r+s)
  +\gamma_{a+1}(v+d).}                                      \tag{12}
\]

Then the exact quadratic rank coefficients are

\[
\boxed{
 \lim_{h\to0}\frac{\det Q^{a,[1]}(h)}{h^2}=V_a,
 \qquad 1\le a\le L-1,}                                  \tag{13}
\]

\[
\boxed{
 \lim_{h\to0}\frac{\det K^{a,[1]}(h)}{h^2}=\pi_a\beta_a,
 \qquad 2\le a\le L.}                                    \tag{14}
\]

Every coefficient in (13)--(14) is strictly positive.  Moreover, define

\[
 \widehat s=
 \begin{cases}
  s,&s>0,\\
  1,&s=0,
 \end{cases}
 \qquad
 \lambda_\phi=\min\{1,d,u,\ell,\widehat s\}.             \tag{15}
\]

Then \(\lambda_\phi>0\), depends only on the activation, and every one of
the \(2(L-1)\) coefficients \(a_{G,L}\) in (13)--(14) obeys the single
depth-explicit estimate

\[
\boxed{a_{G,L}\ge \lambda_\phi^{\,4L}.}                    \tag{16}
\]

The proof occupies Sections 2--7.  Section 8 constructs a finite,
activation-envelope rank radius.

If \(d=0\), continuity and full Gaussian support imply
\(\phi'\equiv0\); (1) then gives \(\phi\equiv\pm1\).  All hidden gradients
vanish and \(F_{k,L}(h)=kh\) exactly.  Thus
\(\Delta_L\equiv0\), and no rank inversion is required.  All remaining
sections concern \(d>0\).

## 2. A signed Gaussian-source lemma

The following lemma is the only fact needed to differentiate a Gaussian
source at a covariance which loses rank at \(h=0\).

**Lemma 2.1.**  Let \(Y_0\in L^2\), \(\|Y_0\|_2^2=c>0\), and suppose

\[
 Y_1(h)=Y_0+hP+o_{L^2}(h),
 \qquad
 \langle Y_0,P\rangle=0.                                  \tag{17}
\]

Let \((\zeta_0,\zeta_1(h))\) be centered Gaussian with covariance
\(\operatorname{Gram}(Y_0,Y_1(h))\).  It has a realization, for both
signs of \(h\), such that

\[
 \zeta_1(h)=\zeta_0+h\sqrt{\|P\|_2^2}\,E+o_{L^p}(h)        \tag{18}
\]

for every finite \(p\), where \(E\sim N(0,1)\) is independent of
\(\zeta_0\sim N(0,c)\).  Also

\[
 \det\operatorname{Gram}(Y_0,Y_1(h))
 =c\|P\|_2^2h^2+o(h^2).                                   \tag{19}
\]

**Proof.**  Put

\[
 q_{01}(h)=\langle Y_0,Y_1(h)\rangle,
 \qquad q_{11}(h)=\|Y_1(h)\|_2^2.
\]

Equation (17) gives \(q_{01}=c+o(h)\) and

\[
 q_{11}-q_{01}^2/c=\|P\|_2^2h^2+o(h^2).                   \tag{20}
\]

For \(h\ne0\), let

\[
 \alpha(h)=q_{01}(h)/c,
 \qquad
 \nu(h)=\frac{q_{11}(h)-q_{01}(h)^2/c}{h^2}\ge0
\]

and set

\[
 \zeta_1(h)=\alpha(h)\zeta_0+h\sqrt{\nu(h)}E.             \tag{21}
\]

The factor in (21) is the signed \(h\), not \(|h|\).  This pair has the
required covariance.  We have
\((\alpha(h)-1)/h\to0\) and
\(\nu(h)\to\|P\|_2^2\), proving (18).  Multiplying (20) by \(c\) proves
(19).  \(\square\)

The \(L^2\) expansions below are legitimate derivatives of the already
width-limited inverse-free DAG.  Indeed, at fixed \(L\) it is a finite
composition of sums, products, \(\phi\), and Gaussian expectations.  The
signed realization (21), the linear-growth bound on \(\phi\), and bounded
\(\phi'\), \(\phi''\) give a common polynomial Gaussian envelope.  The
mean-value theorem and dominated convergence therefore propagate each
\(o_{L^2}(h)\) remainder through every node used below.  No covariance
inverse enters this argument.

## 3. Initialization and local representatives

At \(h=0\), every forward preactivation is standard Gaussian.  The
initial reverse variances follow from top to bottom:

\[
 R_{L,0}=A\sim N(0,1),
 \qquad
 \mathbb E\Delta_{a,0}^2
 =d\,\mathbb ER_{a,0}^2,
 \qquad
 \mathbb ER_{a-1,0}^2=\mathbb E\Delta_{a,0}^2.             \tag{22}
\]

Thus (7) holds.  At each local Gaussian-operator call one may use the
representative

\[
 Z_a\sim N(0,1),
 \qquad R_a\sim N(0,b_a),                                  \tag{23}
\]

with \(Z_a\) and \(R_a\) independent.  Fresh forward and reverse
innovations introduced below are independent of both.  This is not an
extra independence assertion about a trained finite-width network: it is
the primitive-block independence in the fixed-\(h\), inverse-free Gaussian
DAG, specialized to its coalesced \(h=0\) node.

For reference, the complete time-zero/time-one slice of that DAG is as
follows.  At the first layer,

\[
 Z_{1,0}=U,\qquad Z_{1,1}=U+h\Delta_{1,0}.                  \tag{23a}
\]

For \(2\le a\le L\), let
\((\xi^a_0,\xi^a_1)\) have covariance \(Q^{a-1,[1]}\), and set

\[
 Z_{a,0}=\xi^a_0,\qquad
 Z_{a,1}=\xi^a_1+
 \bigl(\rho^a_{10}+hQ^{a-1}_{01}\bigr)\Delta_{a,0},         \tag{23b}
\]

\[
 \rho^a_{10}
 =\mathbb E[\partial_{\chi^a_0}X_{a-1,1}].                 \tag{23c}
\]

At the top,

\[
 R_{L,0}=A,\qquad R_{L,1}=A+hX_{L,0}.                      \tag{23d}
\]

For \(1\le a<L\), let
\((\chi^{a+1}_0,\chi^{a+1}_1)\) have covariance
\(K^{a+1,[1]}\), and set

\[
\begin{aligned}
 R_{a,0}&=\chi^{a+1}_0,\\
 R_{a,1}&=\chi^{a+1}_1+
 \sigma^{a+1}_{10}X_{a,0}
 +\sigma^{a+1}_{11}X_{a,1}
 +hK^{a+1}_{01}X_{a,0},
\end{aligned}                                               \tag{23e}
\]

\[
 \sigma^a_{1r}
 =\mathbb E[\partial_{\xi^a_r}\Delta_{a,1}],
 \qquad r=0,1.                                              \tag{23f}
\]

The forward primitive blocks \(\xi^a\), transpose primitive blocks
\(\chi^a\), and \(A,U\) are independent except for the displayed
within-block covariances.  Equations (2) and (23a)--(23f), evaluated in
the order bottom-up, top-down, are the inverse-free one-step program used
in the proof.  They display both response coefficients created by every
reused matrix.

## 4. Forward tangent induction

Let

\[
 P_a=\left.\frac{d}{dh}X_{a,1}(h)\right|_{h=0}
\]

as an \(L^2\) derivative of the operator DAG.  We prove simultaneously

\[
 \mathbb E[X_{a,0}P_a]=0,
 \qquad
 \mathbb EP_a^2=V_a.                                      \tag{24}
\]

At the first layer, the exact update is

\[
 Z_{1,1}=Z_1+hR_1p(Z_1),
\]

so

\[
 P_1=R_1p(Z_1)^2.                                         \tag{25}
\]

Since \(R_1\) is centered and independent of \(Z_1\),

\[
 \mathbb E[g(Z_1)P_1]=0,
 \qquad
 \mathbb EP_1^2=b_1u=V_1.                                \tag{26}
\]

Suppose (24) holds at layer \(a-1\).  Lemma 2.1 applied to the feature
Gram \(Q^{a-1,[1]}\) says that the derivative of the time-one raw forward
source at layer \(a\) is

\[
 \sqrt{V_{a-1}}E_a,
 \qquad E_a\sim N(0,1)\ \hbox{fresh}.                     \tag{27}
\]

The full preactivation also contains a learned rank-one term and the
reused-matrix response.  Their combined first derivative is

\[
 \Theta_{a-1}R_ap(Z_a).                                   \tag{28}
\]

Here is the complete induction for its coefficient.  The learned term is
\(hQ^{a-1}_{01}\Delta_{a,0}\), and hence contributes \(1\), because
\(Q^{a-1}_{00}=1\).  The response is
\(\rho^a_{10}=\mathbb E[\partial_{\chi_{a,0}}X_{a-1,1}]\), where
\(\chi_{a,0}\) is the coalesced transpose source entering layer \(a-1\).
At zero its value is \(0\).  Differentiating (25) for \(a=2\), or the
inductive tangent below for \(a>2\), gives

\[
 (\rho^a_{10})'(0)
 =\Theta_{a-2}\mathbb Ep^2=d\Theta_{a-2}.                 \tag{29}
\]

Thus the full coefficient is
\(1+d\Theta_{a-2}=\Theta_{a-1}\), proving (28) without dropping the
reused-column response.

Consequently the exact local tangent representation is

\[
 \dot Z_{a,1}
 =\sqrt{V_{a-1}}E_a+\Theta_{a-1}R_ap(Z_a),
 \qquad
 P_a=p(Z_a)\dot Z_{a,1}.                                  \tag{30}
\]

Every summand contains a centered independent \(E_a\) or \(R_a\), so
\(\mathbb E[g(Z_a)P_a]=0\).  Squaring (30) gives

\[
 \mathbb EP_a^2=dV_{a-1}+\Theta_{a-1}^2b_au=V_a,          \tag{31}
\]

which proves (24), (8), and (9) for every layer.

## 5. Reverse tangent induction and every response term

Put

\[
 T_a=\left.\frac{d}{dh}\Delta_{a,1}(h)\right|_{h=0}.
\]

We prove, downward in \(a\), that the derivative \(D_a\) of the carrier
\(R_{a,1}\) has the local representation

\[
 D_a=\sqrt{\beta_{a+1}}B_a+\gamma_{a+1}g(Z_a),             \tag{32}
\]

where \(B_a\sim N(0,1)\) is fresh.  At the top,
\(R_{L,1}=A+hX_{L,0}\), so (32) holds with the initialization (10).

Combining (30) and (32) gives

\[
\begin{aligned}
 T_a={}&p(Z_a)D_a+R_aq(Z_a)\dot Z_{a,1}\\
 ={}&\sqrt{\beta_{a+1}}B_ap
   +\gamma_{a+1}gp
   +\sqrt{V_{a-1}}R_aE_aq
   +\Theta_{a-1}R_a^2pq .
\end{aligned}                                               \tag{33}
\]

All functions \(g,p,q\) in (33) are evaluated at the same \(Z_a\).
The four primitive variables \(Z_a,R_a,E_a,B_a\) are independent, except
that \(R_a\) has variance \(b_a\).

First,

\[
 \mathbb E[\Delta_{a,0}T_a]=0.                            \tag{34}
\]

Indeed, after multiplication by \(R_ap\), the first two terms in (33)
contain one centered \(R_a\), the third contains centered \(E_a\), and the
fourth contains the odd moment \(\mathbb ER_a^3=0\).

The \(B_a\)-term and the \(R_aE_a\)-term are orthogonal to every other
term.  Among the remaining two terms only their mutual cross term
survives.  Therefore

\[
\begin{aligned}
 \mathbb ET_a^2={}&d\beta_{a+1}+\gamma_{a+1}^2\ell
 +b_aV_{a-1}s+3\Theta_{a-1}^2b_a^2e\\
 &+2\Theta_{a-1}\gamma_{a+1}b_am,
\end{aligned}                                               \tag{35}
\]

which is precisely (11).  In particular,

\[
 \beta_a=\|T_a\|_2^2.                                     \tag{36}
\]

It remains to prove (12), including the reused-matrix response.  Lemma
2.1 applied to (34)--(36) gives a fresh derivative
\(\sqrt{\beta_a}B_{a-1}\) for the raw transpose source of the matrix below
layer \(a\).  The full carrier also contains

\[
 \sigma^a_{10}X_{a-1,0}+\sigma^a_{11}X_{a-1,1}
 +hK^a_{01}X_{a-1,0}.                                     \tag{37}
\]

At \(h=0\), the two source coordinates coalesce,
\(\sigma^a_{10}+\sigma^a_{11}=0\), and the first derivatives of both
the feature and cotangent covariances vanish by (24) and (34).  Therefore
differentiation of the canonical sum of the two responses gives

\[
 \left.\frac d{dh}(\sigma^a_{10}+\sigma^a_{11})\right|_{0}
 =\mathbb E[\partial_{Z_a}T_a].                            \tag{38}
\]

For completeness, (38) is independent of a choice of coordinates at the
singular covariance.  Realize the two coalesced forward sources by (21),
differentiate the sum
\(\mathbb E[(\partial_{\xi_0}+\partial_{\xi_1})\Delta_{a,1}]\), and use
dominated convergence.  The innovation derivative has mean zero, while
the common-source derivative is \(\partial_{Z_a}T_a\).  This gives (38)
directly and uses no inverse covariance.

Differentiating the four terms of (33) with respect to \(Z_a\) gives

\[
 \mathbb E[\partial_{Z_a}T_a]
 =\gamma_{a+1}(v+d)+\Theta_{a-1}b_a(r+s).                  \tag{39}
\]

The terms containing \(B_a\) or \(R_aE_a\) average to zero;
\((gp)'=p^2+gq\) and \((pq)'=q^2+pt\).  Finally, differentiating the last
term in (37) contributes \(K^a_{00}=\pi_a\).  The derivative of
\(R_{a-1,1}\) is thus

\[
 \sqrt{\beta_a}B_{a-1}+\gamma_ag(Z_{a-1}),
\]

with \(\gamma_a\) exactly as in (12).  This closes the downward induction.

## 6. Gram coefficients

For a feature Gram, (24) and Lemma 2.1 with
\(\|X_{a,0}\|_2^2=1\) give

\[
 \det Q^{a,[1]}(h)=V_ah^2+o(h^2),                          \tag{40}
\]

which proves (13).  For a cotangent Gram, (34), (36), and
\(\|\Delta_{a,0}\|_2^2=\pi_a\) give

\[
 \det K^{a,[1]}(h)=\pi_a\beta_ah^2+o(h^2),                \tag{41}
\]

which proves (14).  These expansions are used only to identify the exact
second derivatives at the inverse-free \(h=0\) DAG.  Section 8 replaces
their remainders by explicit activation-envelope bounds before any rank
claim at nonzero \(h\) is made.

## 7. Strict positivity and a depth-uniform lower base

Since \(d>0\), also \(u>0\).  Equations (8)--(9) give \(V_a>0\) for every
\(a\).

Although the last term of (11) can have either sign, positivity must not
be inferred termwise from that polynomial.  It follows from the stochastic
square (33).  At the top layer, if \(s>0\), the component

\[
 \sqrt{V_{L-1}}\,R_LE_Lq(Z_L)
\]

is orthogonal to the other three components and has squared norm
\(V_{L-1}s>0\).  Hence \(\beta_L>0\).  If \(s=0\), continuity and full
Gaussian support give \(\phi''\equiv0\).  Then \(\phi\) is a nonconstant
affine function and (33) at the top reduces to
\(T_L=\phi(Z_L)\phi'(Z_L)\); consequently

\[
 \beta_L=\ell=d>0.                                        \tag{42}
\]

For \(a<L\), the fresh \(B_a\)-component in (33) is orthogonal to all
others, so

\[
 \beta_a\ge d\beta_{a+1}>0.                               \tag{43}
\]

This proves strict positivity, including the affine case.

We now prove (16).  The number \(\ell\) in (5) is positive: if
\(\phi\phi'=0\) everywhere, then \((\phi^2)'=0\), so continuity on the
connected line makes \(\phi\) constant in modulus; this contradicts
\(d>0\).  Hence every entry in the minimum (15) is positive.

Because \(0<\lambda_\phi\le1\), (8)--(9) imply, for
\(1\le a\le L-1\),

\[
 V_a\ge d^{a-1}V_1=d^{L+a-2}u
 \ge\lambda_\phi^{L+a-1}
 \ge\lambda_\phi^{2L}.                                   \tag{44}
\]

If \(s>0\), (44) gives

\[
 \beta_L\ge V_{L-1}s
 \ge\lambda_\phi^{2L-1}.                                  \tag{45}
\]

If \(s=0\), (42) and \(\lambda_\phi\le1\) give the same weaker lower
bound.  From (43), for every \(2\le a\le L\),

\[
 \beta_a\ge d^{L-a}\beta_L
 \ge\lambda_\phi^{3L-a-1}
 \ge\lambda_\phi^{3L}.                                    \tag{46}
\]

Also

\[
 \pi_a=d^{L-a+1}\ge\lambda_\phi^L,
 \qquad 2\le a\le L.                                     \tag{47}
\]

Thus every feature coefficient is at least
\(\lambda_\phi^{2L}\ge\lambda_\phi^{4L}\), and every cotangent
coefficient is at least
\(\lambda_\phi^{3L}\lambda_\phi^L=\lambda_\phi^{4L}\).
This proves (16).

## 8. A finite activation-envelope rank radius

This section turns the coefficients above into a nonexistential interval
of positive definiteness.  It deliberately constructs constants from
activation envelopes, rather than from a continuity modulus of a trained
output.

### 8.1 Envelope and singular Price recursion

An envelope is a pair \((A,p)\in[0,\infty)\times\mathbb N\), denoting

\[
 |f(x)|\le A(1+\|x\|)^p.
\]

Use the exact rules

\[
 (A,p)\oplus(B,q)=(A+B,\max\{p,q\}),
 \qquad
 (A,p)\odot(B,q)=(AB,p+q),                                \tag{48}
\]

and initialize

\[
 {\cal E}(1)={\cal E}(h)=(1,0),
 \quad {\cal E}(x_i)=(1,1),
\]

\[
 {\cal E}(\phi(f))=(M_\phi(1+A),p)
 \quad\hbox{if }{\cal E}(f)=(A,p),
 \qquad
 {\cal E}(\phi^{(j)}(f))=(M_\phi,0),\quad1\le j\le12.    \tag{49}
\]

Generate formal derivatives by the product and chain rules, including all
integer multiplicities.

For a Gaussian block of dimension \(D\le4\), a covariance
\(\Sigma(h)\), and a local integrand \(\psi(h,x)\), define

\[
 N(h)=\mathbb E_{N(0,\Sigma(h))}\psi(h,X).
\]

Suppose already constructed numbers \(\bar c_j\) satisfy

\[
 \sum_{r,t}|\Sigma_{rt}^{(j)}(h)|\le\bar c_j,
 \qquad 0\le j\le4,\quad |h|\le1.                         \tag{50}
\]

For ordered spatial derivative strings, let \(R^{(0)}_{j,k}\) be the
\(\oplus\)-sum of the envelopes of every
\(\partial_h^j\partial_x^\alpha\psi\) with \(|\alpha|=k\) and
\(j+\lceil k/2\rceil\le4\).  Recursively set

\[
 R^{(q+1)}_{j,k}=R^{(q)}_{j+1,k}
 \oplus
 \bigoplus_{i=0}^{j}
 \left[
  \left(\frac12{j\choose i}\bar c_{i+1},0\right)
  \odot R^{(q)}_{j-i,k+2}
 \right]                                                   \tag{51}
\]

whenever \(q+j+\lceil k/2\rceil<4\).  If
\(R^{(q)}_{0,0}=(A_q,p_q)\), put

\[
 \overline{\mathcal J}_q(N)
 =A_q\sum_{j=0}^{p_q}{p_q\choose j}
   \bar c_0^{j/2}2^{j/2}
   \frac{\Gamma((D+j)/2)}{\Gamma(D/2)}.                   \tag{52}
\]

Repeated Price differentiation gives

\[
 |N^{(q)}(h)|\le\overline{\mathcal J}_q(N),
 \qquad 0\le q\le4,\quad |h|\le1.                        \tag{53}
\]

This remains valid at singular covariance.  To see this without an
inverse, first prove

\[
 \frac d{dh}\mathbb E\psi(h,X_h)
 =\mathbb E\left[
   \partial_h\psi+\frac12\Sigma'(h):D_x^2\psi
  \right]                                                  \tag{54}
\]

for Schwartz \(\psi\) by differentiating the Gaussian characteristic
function.  Cutoff and mollification extend (54) to (49); (52) supplies a
uniform Gaussian polynomial moment bound.  Iterating (54) gives exactly
(51), proves (53), and verifies all domination hypotheses.

### 8.2 Chronological termination

Apply (48)--(54) to the exact local expressions in (2), in this order:

1. the bottom time-one feature call, producing \(Q^{1,[1]}\) and
   \(\rho^2_{10}\);
2. the time-one forward calls \(a=2,\ldots,L-1\), each producing
   \(Q^{a,[1]}\) and \(\rho^{a+1}_{10}\);
3. the top time-one call, producing \(K^{L,[1]}\) and
   \(\sigma^L_{10},\sigma^L_{11}\);
4. the backward calls \(a=L-1,\ldots,2\), each producing
   \(K^{a,[1]}\) and \(\sigma^a_{10},\sigma^a_{11}\).

At each call, every earlier scalar Gram or response and each of its first
four derivative bounds is inserted as a scalar token.  A new covariance
majorant is the entrywise sum

\[
 \bar c_j^{\rm new}
 =\sum_{r,t}\overline{\mathcal J}_j(\text{required earlier Gram}_{rt})
   +\mathbf1_{j=0}(\text{required base variances}).        \tag{55}
\]

For a full learned-plus-response coefficient \(S+hQ\), use

\[
 \overline{(S+hQ)}_j
 =\bar S_j+\bar Q_j+j\bar Q_{j-1},
 \qquad \bar Q_{-1}=0.                                    \tag{56}
\]

This is a completely specified finite recursion: it has
\(2L-2\) calls; every Gaussian block has dimension at most four; every
index set in (51) is finite; and formal spatial differentiation reaches
order at most eight.  A response integrand begins with at most
\(\phi''\), while the restriction
\(j+\lceil|\alpha|/2\rceil\le4\) implies
\(j+|\alpha|\le8\).  Thus no activation derivative above order ten is
needed, and (1) is more than sufficient.  The call order is acyclic, hence the
recursion terminates and returns finite numbers depending only on \(L\),
\(M_\phi\), the base moments (5), and the explicit Gaussian moments in
(52).  It contains no output derivative, trained-trajectory supremum, or
unspecified continuity modulus.

Write the resulting bounds as

\[
 \bar Q^a_{rt,j}\ge
 \sup_{|h|\le1}|(Q^a_{rt})^{(j)}(h)|,
 \qquad
 \bar K^a_{rt,j}\ge
 \sup_{|h|\le1}|(K^a_{rt})^{(j)}(h)|.                     \tag{57}
\]

### 8.3 Radius

The general operator DAG has the sign symmetry

\[
 h\mapsto-h,\qquad A\mapsto-A,\qquad
 \hbox{every primitive transpose source }\chi^a_s\mapsto-\chi^a_s.
                                                                    \tag{58}
\]

Forward sources are unchanged.  Induction first over time and then over
layers shows that every \(Z_{a,s},X_{a,s}\) is unchanged and every
\(R_{a,s},\Delta_{a,s}\) changes sign.  Hence every Gram in (3)--(4) and
its determinant is even in \(h\).

For \(1\le a\le L-1\), define

\[
 D_{Q^a}=\bar Q^a_{11,4}
 +\sum_{j=0}^{4}{4\choose j}
   \bar Q^a_{01,j}\bar Q^a_{01,4-j},                       \tag{59}
\]

and, for \(2\le a\le L\),

\[
 D_{K^a}=\pi_a\bar K^a_{11,4}
 +\sum_{j=0}^{4}{4\choose j}
   \bar K^a_{01,j}\bar K^a_{01,4-j}.                       \tag{60}
\]

These bound the fourth derivatives of the corresponding determinants,
because \(Q^a_{00}=1\) and \(K^a_{00}=\pi_a\) are constant in \(h\).
For \(c>0,D\ge0\), put

\[
 R(c,D)=\min\left\{1,\sqrt{\frac{12c}{1+D}}\right\}.      \tag{61}
\]

The finite recursive rank radius is

\[
\boxed{
 h^{\rm rank}_{\phi,L}
 =\min\left\{
 \frac12,
 \min_{1\le a\le L-1}R(V_a,D_{Q^a}),
 \min_{2\le a\le L}R(\pi_a\beta_a,D_{K^a})
 \right\}.}                                                \tag{62}
\]

It is positive and is computed only from the activation and \(L\).
Indeed, evenness, (13)--(14), and Taylor's theorem give, for any one Gram
with coefficient \(c\) and fourth-derivative bound \(D\),

\[
 |\det G(h)-ch^2|\le\frac D{24}|h|^4.                      \tag{63}
\]

For \(0<|h|\le R(c,D)\), the right side is at most
\(ch^2/2\), so \(\det G(h)\ge ch^2/2>0\).  This proves positive
definiteness of all \(2(L-1)\) Grams on the punctured interval in (62).

Finally, if

\[
 D_L=\max\left\{
 \max_{1\le a\le L-1}D_{Q^a},
 \max_{2\le a\le L}D_{K^a}
 \right\},                                                  \tag{64}
\]

then (16) yields the explicitly depth-separated lower estimate

\[
\boxed{
 h^{\rm rank}_{\phi,L}
 \ge
 \min\left\{\frac12,
 \sqrt{\frac{12\lambda_\phi^{4L}}{1+D_L}}
 \right\}.}                                                \tag{65}
\]

Any general-depth fifth-order compiler bound on \(D_L\) can therefore be
inserted into (65) directly.  The rank argument itself does not assume or
claim the separate fixed-\(h\) finite-width/DAG identification; it supplies
the activation-defined positive-definiteness interval required by that
identification.

# Covariance-supported response in the exact finite L=2 Gaussian program

2026-09-06. Bounded theoretical result; no experiments or agents.

The full-history first-chaos contraction is valid, including singular
Grams, with explicit defects recording the means and the independent
bottom root. Bounded outputs give a quantitative strict defect on each
fixed finite covariance support. Its constant depends on the smallest
positive attained Gram eigenvalues; no mesh-uniform gap is inferred.

There is also a bound that avoids those eigenvalues: on a feature-time
horizon, every row of the **complete learned kernels** A and B has a
uniform bound on covariance-supported inputs. This bounds the expected
source responses of the actual fields, with every learned memory retained.
The output norm here is the ordinary coordinate or time-weighted Euclidean
norm. An attained two-update example shows why one cannot automatically
upgrade this to a contraction between the two history covariance norms:
learned forward memory can leave the destination covariance support.

## 1. Dependency, scope, and exact law

The sole mathematical dependency read, in full, was

`/tmp/l2-two-sample-proof-0ywjpp/HARMONIC_FULL_RESPONSE_TEST.md`

SHA256:
`6a6a49cd1e5c25c4e6884de8dca7d933f54cb3e2d67c8fcd8833b50b87480ae7`.

No files named inside that dependency, reviews, history, project files,
or external mathematical sources were consulted. Procedural skills used:
`/etc/codex/skills/investigate-conjectures/SKILL.md`, its research-contract,
evidence-ledger, and adversarial-audit references, and
`/etc/codex/skills/solve-math-rigorously/SKILL.md`. Their role was to keep
finite identities, uniform estimates, and unresolved continuation claims
separate. Only this mathematical deliverable is written.

Fix a finite prefix k=0,...,N, a mesh lambda>0, and

\[
 C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\quad
 -1\le\rho<1,\quad Y=\operatorname{diag}(1,-1),\quad y=(1,-1).
\]

The default activations are

\[
 \ell(z)=1+\tfrac1{10}\arctan z,\quad
 h(z)=\varepsilon(\sin z+\cos z),\quad
 p=h',\quad \varepsilon=1/20,\quad b=\sqrt2\varepsilon.
\]

Thus |h|,|p|<=b, p'=-h, and |ell|<=L with
L=1+pi/20. The projection and finite-horizon bounds below also apply to
the dependency's bounded smooth alternatives ell=sin and ell=arctan,
using their corresponding bound L. The support obstruction in Section 7
uses the default ell.

Population 1 has independent centered Gaussian groups G and zeta, with
Cov(G)=C. Population 2 has a centered Gaussian history xi, independent
of those groups. Put i=(k,a), j=(r,b), and j<i when r<k. Flattening the
two samples and all N+1 times gives n=2(N+1) coordinates. The exact law is

\[
\begin{aligned}
 Z^1_{ka}&=G_a+\lambda\sum_{r<k,b}C_{ab}y_b
                  \ell'(Z^1_{rb})q_{rb},& F_i&=\ell(Z^1_i),\\
 Z_i&=\xi_i+\sum_{j<i}A_{ij}\delta_j,& H_i&=1+h(Z_i),\\
 w_k&=\lambda\sum_{r<k,b}y_bH_{rb},&\delta_i&=w_kp(Z_i),\\
 q_i&=\zeta_i+\sum_{r\le k,b}B_{i,rb}F_{rb}.&&
\end{aligned}                                                    \tag{1}
\]

The initial readout is the attained deterministic value w_*=0. Define

\[
 \Gamma=E_1[FF^T]=\operatorname{Cov}(\xi),\qquad
 \Sigma=E_2[\delta\delta^T]=\operatorname{Cov}(\zeta),
                                                                    \tag{2}
\]
\[
 S=E_1\partial_\zeta F,\qquad D=E_2\partial_\xi\delta,
 \qquad
 A=S+M_A,\quad B=D+M_B,
                                                                    \tag{3}
\]
\[
 (M_A)_{ij}=\lambda\mathbf1_{r<k}\Gamma_{ij}y_b,
 \qquad
 (M_B)_{ij}=\lambda\mathbf1_{r<k}\Sigma_{ij}y_b.          \tag{4}
\]

S and A are strictly lower in time; D and B are lower in time, including
their complete current blocks. All selected coefficients and covariance
parameters are frozen during differentiation. Every formal slot remains
present, including zero-variance zeta_0, duplicate xi slots, and the
formal readout root. These are not derivatives of the statistical
selection map.

Since the constants in H cancel against the labels,

\[
 |w_k|\le2b\lambda k,\qquad
 |\delta_{ka}|\le2b^2\lambda k.                         \tag{5}
\]

For each finite prefix, the smooth causal recursion gives integrable
source derivatives: the bottom derivatives are bounded by polynomials
in finitely many Gaussian coordinates, with finite deterministic
coefficients, and the top recursion has bounded gates and readout.
This suffices for every integration by parts below. No uniform derivative
moment assumption is being added.

Crucially, (2) uses **uncentered second moments of F and delta**.
The Gaussian sources are centered; the features and backward fields need
not be. Replacing (2) by Cov(F) and Cov(delta) would change the law.

## 2. Exact projection identities, including means and roots

Here is the finite Gaussian argument, including degeneracy. If
X=L_0 g with g standard Gaussian and V=L_0L_0^T, then
one-dimensional integration by parts against the
Gaussian density gives

\[
 E[U(X)X^T]=E[\partial_X U]V.                            \tag{6}
\]

Indeed E[U g^T]=E[partial_g U] and partial_g U=(partial_X U)L_0.
An independent auxiliary Gaussian group can first be conditioned on and
then integrated out. Polynomial derivative bounds justify the integration
and vanishing boundary terms. No inverse of V is involved. Moreover,
E[partial_X U]X is the orthogonal projection of U onto the span of the
coordinates of X: (6) makes its residual orthogonal to each coordinate.
This describes an uncentered U projected onto centered linear functions.

Let

\[
 m_F=E_1F,\quad m_\delta=E_2\delta,\quad
 R=E_1\partial_G F,
\]
\[
 U_F=F-m_F-RG-S\zeta,\qquad
 U_\delta=\delta-m_\delta-D\xi.                         \tag{7}
\]

Because G and zeta are independent Gaussian groups, their linear spans
are orthogonal. Equation (6) gives exactly

\[
 \Gamma=m_Fm_F^T+RCR^T+S\Sigma S^T+E_1[U_FU_F^T],
                                                                    \tag{8}
\]
\[
 \Sigma=m_\delta m_\delta^T+D\Gamma D^T
                         +E_2[U_\delta U_\delta^T].       \tag{9}
\]

Each residual has zero mean and is orthogonal to all the Gaussian
coordinates displayed in its population. These are the full constant,
linear, and remaining components; no diagonal-in-time approximation is
present. In particular,

\[
 D\Gamma D^T\preceq\Sigma,\qquad
 S\Sigma S^T\preceq\Gamma.                              \tag{10}
\]

Initial independence is used only to justify the separate RCR^T term
in (8). It does not assert that evolved F is independent of zeta or G.
The deterministic zero readout root contributes no Gaussian component
to (9); its formal derivative is not bounded by giving that root a
zero covariance norm.

The mean issue is already visible at the first update. With
K=E[ell(G)ell(G)^T], sigma^2=K_11 and chi=K_11-K_12>0, one has
xi_0=xi_1=X~N(0,K) and

\[
 E\delta_{11}
 =\lambda\varepsilon^2
       \left(e^{-2\sigma^2}-e^{-(\sigma^2+K_{12})}\right),
 \qquad E\delta_{12}=-E\delta_{11}.                       \tag{11}
\]

To verify this, delta_11=lambda(h(X_1)-h(X_2))p(X_1),
E[h(X_1)p(X_1)]=epsilon^2 exp(-2 sigma^2), and
E[h(X_2)p(X_1)]=epsilon^2 exp(-(sigma^2+K_12)), by expanding into
sin(X_2-X_1) and cos(X_1+X_2). Thus centering delta without accounting
for m_delta would already remove a nonzero rank-one contribution.

## 3. The covariance norms and exact composite defect

For a positive semidefinite matrix V write

\[
 \mathcal H_V=\operatorname{Ran}V,\qquad
 \|v\|_V=(v^TV^\dagger v)^{1/2}\quad(v\in\mathcal H_V).   \tag{12}
\]

This norm is used **only on its support**. Applying the pseudoinverse
formula to an arbitrary vector would silently discard its component
outside the support.

If TVT^T<=W, every vector in ker W is orthogonal to Ran(TV^{1/2}); hence
T maps H_V into H_W. Also
W^{dagger/2}TV^{1/2} has operator norm at most one, proving

\[
 \|Dv\|_\Sigma\le\|v\|_\Gamma,\qquad
 \|Su\|_\Gamma\le\|u\|_\Sigma.                          \tag{13}
\]

Thus DS is a contraction on H_Sigma and SD on H_Gamma. Define the exact
positive defects

\[
 R_F=\Gamma-S\Sigma S^T,
 \qquad R_\delta=\Sigma-D\Gamma D^T.
\]

The complete two-stage identity is

\[
 \Sigma-DS\Sigma S^TD^T=R_\delta+D R_FD^T.               \tag{14}
\]

The analogous identity for SD is
Gamma-SD Gamma D^T S^T=R_F+S R_delta S^T. Equations (8)-(9) specify
every term in these defects, including the independent first root.

Causality also gives (DS)^{N+1}=(SD)^{N+1}=0: each multiplication by
DS advances time at least once. Consequently, on the corresponding
supports,

\[
 (I-DS)^{-1}=\sum_{j=0}^{N}(DS)^j,\qquad
 \|(I-DS)^{-1}\|_{\Sigma\to\Sigma}\le N+1.               \tag{15}
\]

This is an exact finite-prefix statement about the derivative-only
composition DS. It is not a bound for BA, and N+1 is not uniform under
mesh refinement at fixed positive time.

Zero-variance columns of S and directions distinguishing duplicate xi
slots are not individually controlled by (10). Their products with the
source covariance are controlled. This distinction is essential in
Sections 7 and 8.

## 4. Quantitative strictness on a fixed finite support

A general elementary lemma supplies an explicit, but possibly very
small, constant. Let V=E[HH^T] be nonzero, let |H_i|<=L_i, and let PH be
its orthogonal projection onto any centered Gaussian linear span. Set

\[
 B_V=\frac{(\sum_i L_i^2)^{1/2}}{
                     \sqrt{\lambda_{\min}^{+}(V)}},\qquad
 a=\sqrt2B_V,
\]
\[
 \eta(B_V)=\int_a^\infty(z-a)^2\varphi(z)\,dz
          =(1+a^2)\overline\Phi(a)-a\varphi(a)>0,         \tag{16}
\]

where phi is the standard Gaussian density and barPhi its upper tail.
Then

\[
 E[(PH)(PH)^T]\preceq(1-\eta(B_V))V.                    \tag{17}
\]

Proof. Take c in H_V with c^TVc=1. Then ||c||_2<=1/sqrt(lambda_min^+(V))
and |c^TH|<=B_V. The centered Gaussian L_c=c^TPH has variance v<=1,
and projection orthogonality gives

\[
 1-v=E(c^TH-L_c)^2
       \ge E\bigl(|L_c|-B_V\bigr)_+^2.
\]

If v>=1/2, the last expression is at least
E(|g|/sqrt(2)-B_V)_+^2=eta(B_V). If v<1/2, then 1-v>1/2>=eta(B_V).
For c in ker V, c^TH=0 almost surely, so its projection also vanishes.
Decomposing a general c into the support and kernel proves (17).
The integral in (16) is positive and at most 1/2; integration of
z phi(z) and z^2 phi(z) gives its displayed closed expression.

Apply this to F projected onto zeta and delta projected onto xi. With
t_k=lambda k, use

\[
 B_\Gamma=\frac{L\sqrt{2(N+1)}}{
                           \sqrt{\lambda_{\min}^{+}(\Gamma)}},
 \qquad
 B_\Sigma=\frac{2b^2\sqrt{2\sum_{k=0}^{N}t_k^2}}{
                           \sqrt{\lambda_{\min}^{+}(\Sigma)}}.
                                                                    \tag{18}
\]

Whenever the respective Gram is nonzero,

\[
 S\Sigma S^T\preceq(1-\eta(B_\Gamma))\Gamma,
 \qquad
 D\Gamma D^T\preceq(1-\eta(B_\Sigma))\Sigma.             \tag{19}
\]

In particular, if both supports are nonzero, the norm of DS is at most

\[
 r=\sqrt{(1-\eta(B_\Gamma))(1-\eta(B_\Sigma))}<1,
 \qquad
 \|(I-DS)^{-1}\|\le\sum_{j=0}^{N}r^j.                  \tag{20}
\]

If a Gram is zero, the corresponding supported map is zero and no
positive-eigenvalue expression for that Gram is needed.

This proves strictness for the actual finite histories, not just for
individual nonlinear gates. It does **not** give a gap depending only
on T=lambda N and the activation bounds. Nearly dependent histories
can make lambda_min^+ small, and the bound on a covariance-normalized
linear combination can grow with N. Boundedness then gives an extremely
small tail defect. No lower bound on those attained eigenvalues, or
alternative uniform control of normalized history combinations, has
been proved here. The possibility that such combinations approach
first chaos remains unresolved as the prefix varies.

## 5. Full learned kernels: a bound without Gram eigenvalues

Put

\[
 f_i=\sqrt{\Gamma_{ii}}\le L,\qquad
 d_i=\sqrt{\Sigma_{ii}}\le2b^2t_k,
 \qquad
 s_k=\lambda\sum_{r<k,b}f_{rb}d_{rb}.
\]

The exact time sum and its horizon bound are

\[
 s_k\le2Lb^2\lambda^2 k(k-1)\le2Lb^2t_k^2.             \tag{21}
\]

For every u in H_Sigma and v in H_Gamma, the complete coefficients
obey

\[
 |(Au)_i|\le f_i(1+s_k)\|u\|_\Sigma,
 \qquad
 |(Bv)_i|\le d_i(1+s_k)\|v\|_\Gamma.                   \tag{22}
\]

Proof. Covariance Cauchy-Schwarz gives |u_j|<=d_j||u||_Sigma and
|v_j|<=f_j||v||_Gamma. Projection gives
|(Su)_i|<=f_i||u||_Sigma and |(Dv)_i|<=d_i||v||_Gamma. Meanwhile,

\[
\begin{aligned}
 |(M_Au)_i|
 &\le\lambda\sum_{j<i}|\Gamma_{ij}|\,|u_j|
 \le f_i\lambda\sum_{j<i} f_jd_j\|u\|_\Sigma,\\
 |(M_Bv)_i|
 &\le\lambda\sum_{j<i}|\Sigma_{ij}|\,|v_j|
 \le d_i\lambda\sum_{j<i} f_jd_j\|v\|_\Gamma.
\end{aligned}
\]

Adding the complete learned pieces proves (22). No learned term was
deleted or replaced by a diagonal, and every historical slot is summed.

For example, on T=lambda N with the history output norm

\[
 \|z\|_{\lambda,2}^2=\lambda\sum_{k=0}^{N}\sum_{a=1}^2|z_{ka}|^2,
\]

equation (22) gives the explicit operator bounds

\[
 \|Au\|_{\lambda,2}
 \le L(1+2Lb^2T^2)\sqrt{2(T+\lambda)}\,\|u\|_\Sigma,
                                                                    \tag{23}
\]
\[
 \|Bv\|_{\lambda,2}
 \le2b^2T(1+2Lb^2T^2)\sqrt{2(T+\lambda)}\,\|v\|_\Gamma.
                                                                    \tag{24}
\]

These constants are uniform along lambda=T/N for N>=1 and fixed T.
They control all output coordinates; no projection of the output back
onto its Gaussian covariance support is made. This is why they remain
valid when that output leaves the support.

## 6. Consequences for the actual attained fields and mean responses

First, (22) is equivalently a row bound on A Sigma^{1/2} and
B Gamma^{1/2}. Since the attained delta and F have exactly these raw
second moments,

\[
 \|(A\delta)_i\|_{L^2(E_2)}\le f_i(1+s_k),\qquad
 \|(BF)_i\|_{L^2(E_1)}\le d_i(1+s_k).
\]

Minkowski's inequality in (1), with no independence assertion between
the two summands, therefore gives

\[
 \|Z_i\|_2\le f_i(2+s_k)\le L(2+2Lb^2t_k^2),
                                                                    \tag{25}
\]
\[
 \|q_i\|_2\le d_i(2+s_k)\le2b^2t_k(2+2Lb^2t_k^2).      \tag{26}
\]

These are finite-horizon moment bounds for the exact, uncut law.

Next, fix a deterministic supported top-source direction v in H_Gamma,
with all other root/source directions zero. Let P=partial_v Z and
T_delta=partial_v delta be the actual pathwise variations from the
frozen-coefficient causal equations. Taking their expectations yields

\[
 E_2T_\delta=Dv,\qquad E_2P=v+ADv.                     \tag{27}
\]

Because Dv belongs to H_Sigma, (13) and (22) give

\[
 |(E_2P)_i|\le f_i(2+s_k)\|v\|_\Gamma,
 \qquad \|E_2T_\delta\|_\Sigma\le\|v\|_\Gamma.          \tag{28}
\]

Similarly, for a supported reverse-source direction u in H_Sigma with
zero bottom-root variation,

\[
 E_1\partial_uF=Su,\qquad
 E_1\partial_uq=u+BSu,
\]
\[
 |(E_1\partial_uq)_i|\le d_i(2+s_k)\|u\|_\Sigma.        \tag{29}
\]

The independent bottom root can also be retained. By (8), the map
(g,u) -> Rg+Su is a contraction from
H_C direct-sum H_Sigma to H_Gamma. For g in H_C and u in H_Sigma set
J^2=||g||_C^2+||u||_Sigma^2. Then

\[
 \|E_1\partial_{(g,u)}F\|_\Gamma\le J,
 \qquad
 |E_1\partial_{(g,u)}q_i|\le d_i(2+s_k)J.                \tag{30}
\]

Indeed partial q has mean u+B(Rg+Su), and both terms have the stated
bounds. This includes rho=-1 with singular C. A nonzero formal variation
of the deterministic readout root is outside this covariance-supported
statement and is not assigned zero cost.

Equations (28)-(30) concern **expected** formal Jacobians, which are the
response objects S and D of the specified law. They do not bound
E|partial_v Z|^2, E|partial_v delta|^2, or the response of the selected
statistics themselves. In particular, bounding q in L^2 does not bound
its product with a correlated bottom sensitivity. The curvature and
mixed-response products in the dependency's storage identity remain
uncontrolled by these estimates alone.

## 7. An attained support obstruction from learned forward memory

The failure to obtain a covariance-norm contraction for A is not merely
an abstract concern about triangular truncation. Use the default ell,
rho=-1, and exactly the prefix k=0,1,2, at any lambda>0. Let
e_+=(1,1)^T/sqrt(2), e_-=(1,-1)^T/sqrt(2).

Since the rows of C sum to zero and G_1+G_2=0 almost surely,
Z^1_{k1}+Z^1_{k2}=0 at every time. The shifted odd activation implies

\[
 F_{k1}+F_{k2}=2\quad\hbox{almost surely for every }k.    \tag{31}
\]

Therefore every x in H_Gamma satisfies

\[
 e_+^Tx_0=e_+^Tx_1=e_+^Tx_2.                            \tag{32}
\]

For example, the coefficient vector testing the difference of two such
sample averages annihilates F almost surely and hence lies in ker Gamma.
Also, differentiating (31) in any reverse-source slot gives
e_+^TS_{k,r}=0. This remains true off the zeta support while G is held
at its attained value: the bottom update always preserves the zero sum.

We now construct an actually supported u, rather than prescribing
independent temporal slots. On the first update, write

\[
 G=(g,-g),\quad U=\tfrac1{10}\arctan g,\quad \nu=EU^2>0,
\]

so K=E[F_0F_0^T] has diagonal 1+nu and off-diagonal 1-nu.
For the initial top pair X, the variables
x=(X_1+X_2)/2 and d=(X_1-X_2)/2 are independent Gaussians of
variances 1 and nu. Since delta_1=lambda(h(X_1)-h(X_2))p(X),

\[
 e_-^T\delta_1
   =-2\sqrt2\lambda\varepsilon^2\sin^2(d)\cos(2x).
                                                                    \tag{33}
\]

Its second moment a_-=E(e_-^T delta_1)^2 is strictly positive. Sample
exchange makes Sigma_11 commute with exchange, so
Sigma_11 e_-=a_-e_-. Define a history vector c by c_1=e_-/a_- and
c_0=c_2=0, and put

\[
 u=\Sigma c\in\mathcal H_\Sigma.
\]

Then u_0=0, u_1=e_-, and u_2 is whatever the actual covariance selects.
There is no assumption that u_2 can be independently set to zero.

Strict causality gives (Au)_0=(Au)_1=0. In row 2, the response part has
zero sample average, whereas the **full** learned part gives

\[
\begin{aligned}
 e_+^T(Au)_2
 &=\lambda e_+^T\Gamma_{21}Y e_-\\
 &=\lambda E_1[(e_+^TF_2)(F_1^Te_+)]
 =2\lambda.
\end{aligned}                                                       \tag{34}
\]

Thus Au does not belong to H_Gamma. Both learned pieces remain in the
underlying causal law; no earlier coefficient, source covariance, or
attained field was modified. The reverse learned memory at later rows
cannot change the conserved identity (31) or this causal calculation.

Consequently, A:H_Sigma -> H_Gamma is not even a well-defined
support-preserving map for all allowed finite programs. A covariance
contraction or a small-gain bound for BA cannot be obtained by treating
A and B as if they were S and D. Projecting Au back onto H_Gamma removes
a nonzero temporal sample-average contrast of the actual output, as
detected in (34); it need not set its whole time-two average to zero.
A norm or storage with
additional components might control it; this example does not exclude
that possibility. Bounds (22)-(30) do control the full vector in their
stated output norms.

## 8. First-prefix supported source constant in time: the sign calculation

For a two-sample history v through time index N, the sign functional
in this section is defined by the UNWEIGHTED label-paired quadratic form

\[
 \mathcal Q_B(v)=\sum_{k=0}^N v_k^T Y(Bv)_k
        =\sum_{k=0}^N\sum_{r\le k}v_k^T YB_{kr}v_r.
\]

There is no extra time weight in this definition. Multiplying it by
lambda gives the time-weighted variant and multiplies its value below
by lambda without changing its sign. The ordinary pairing without Y
is a different functional and is not the nonpositivity claim tested.

For the default ell and any allowed rho, let
K=E[F_0F_0^T], chi=K_11-K_12=E(F_{01}-F_{02})^2/2>0, and c=exp(-chi).
On k=0,1, the forward covariance is

\[
 \Gamma=\begin{pmatrix}K&K\\K&K\end{pmatrix},\qquad
 \xi_0=\xi_1=X.
\]

To avoid a collision with the history Gram Gamma, write the initial
gate Gram as

\[
 J_p=E[p(X)p(X)^T]
      =\varepsilon^2\begin{pmatrix}1&c\\c&1\end{pmatrix},
 \qquad\kappa=\varepsilon^2(1-c).
\]

The complete blocks on this prefix are
B_00=0, B_10=lambda J_pY, B_11=-lambda kappa Y; the learned reverse
term is zero here because delta_0=0. The source

\[
 v_0=v_1=e_-
\]

is in H_Gamma: K e_-=chi e_-, so it is Gamma times the history vector
whose two blocks both equal e_-/(2chi). Its squared covariance norm is
1/chi. Direct calculation gives

\[
\begin{aligned}
 \mathcal Q_B(v)
 &=e_-^T\{\lambda YJ_pY-\lambda\kappa I\}e_-\\
 &=\lambda\{\varepsilon^2(1+c)-\varepsilon^2(1-c)\}
 =2\lambda\varepsilon^2e^{-\chi}>0.                    \tag{35}
\end{aligned}
\]

This is exact, with no small-mesh remainder. It refutes nonpositivity
of this specified label-paired functional on the full covariance-supported
source class. It includes a variation
of the initial top source xi_0; if that source is fixed, then support
forces v_1=v_0=0 on this prefix and this test is unavailable. All other
initial roots and the readout root are fixed. The earlier arbitrary-slot
test from the dependency is not being asserted to be supported.

In fact S vanishes on H_Sigma on this first prefix, since F_0=F_1=ell(G)
and the only potentially used reverse slot is zeta_0=0. Thus DS=0 on
the support here, fully consistent with (35). Neither the first-chaos
contraction nor a richer storage inequality asserts the nonpositivity
tested in (35).

## 9. Exact boundary of the result

| Claim | Status and precise scope |
|---|---|
| Mean/root-resolved full-history identities (8)-(10), (14) | Proved in every attained finite law, including singular Grams |
| Strict first-chaos defect (19) | Proved with explicit attained-eigenvalue-dependent constants |
| Complete learned-kernel bounds (22)-(24) | Proved for supported inputs; full coordinate/time-weighted outputs; uniform at fixed feature horizon |
| Actual field L2 and expected-source-response bounds (25)-(30) | Proved with all memories; not second moments of pathwise sensitivities |
| A preserves the two history covariance supports | Falsified by the attained two-update construction (31)-(34) |
| Supported-source nonpositivity alone | Falsified by the exact first-prefix calculation (35) |
| A strict DS gap uniform in mesh/history from the fixed activations and T alone | Open; (18) supplies no uniform constant |
| A response/storage norm closing learned feedback and sensitivity products uniformly on a horizon | Open; no estimate for the missing correlated products is asserted |
| Global continuation, limiting GD/GF/MF identification, or a Catalan/Bessel response bound | Not established or upgraded |

For a uniform strict-gap route, the missing premise is quantitative
separation of covariance-normalized **attained history combinations**
from the relevant Gaussian linear span, or a corresponding lower bound
on the composite defect R_delta+D R_F D^T relative to Sigma. Individual
gate nonlinearity does not supply that premise. For the full learned
feedback, such a gap would additionally need a norm or storage that
retains the component exhibited in (34) and controls the actual
curvature/sensitivity products. These are separate obligations.

The bounded result therefore provides a strict finite-prefix projection
estimate and useful mesh-uniform bounds in a specified weaker output
norm, while leaving the stronger feedback/storage question explicit.
No global theorem or unattained forcing is used to cross that boundary.

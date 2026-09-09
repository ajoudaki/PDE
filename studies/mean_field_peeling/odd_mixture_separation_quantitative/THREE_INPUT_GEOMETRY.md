# Three-input initialization geometry and remaining global question

In this chapter use the raw model of Appendix C, Part M, with activation phi(z)=a z+e arctan(z), a=1-e and 0<e<=1/2. The lemmas also hold for independent a>=1/2 and e>0 where indicated.

The geometric assumptions are \(u_i=x_i/\sqrt d\), \(\|u_i\|=1\), and
\(|\Gamma_{ij}|\le1-\delta\), where \(\Gamma_{ij}=u_i\cdot u_j\).
Open separation in the requested statement implies these weak inequalities.
All assertions below also hold for independent \(a\ge1/2,e>0\).

## What this establishes, and what it does not

Pairwise absolute separation removes all antipodal/duplicate initialization
obstructions for three inputs, even when their Gram matrix is singular.
There is an explicit strictly positive lower bound on the initialized
nonlinear feature Gram, with matching worst-case scale \(e^2\delta^2\).
The algebraically defined initial acceleration directions are nonzero in
every hidden parameter block and for every individual sample in every
hidden layer. Conditional on a canonical strong solution with the trajectory
chain rule, they are its nonzero physical accelerations, and its projected
total kernel has precisely the coefficient \(18\|V\|^2\). The upper
sample assertion has a direct fresh-Gaussian-innovation proof, requiring
neither permutation symmetry nor a nonzero affine comparison direction.
These conditional trajectory conclusions do not assert existence of the
flow, which remains part of the unresolved complete theorem below.

However, the complete all-time three-input theorem is not established by
these facts. Its existing affine-clock proof has a genuine obstruction:
admissible rank-two triples may have a target component outside the affine
network's output space. The affine residual clock is then infinite. In the
equilateral, equal-label case the entire affine population trajectory is
stationary. This invalidates that proof route; it is not a counterexample
to the positive-\(e\) theorem.

The only imported population machinery in the initial-motion statements is
the fixed finite Gaussian program/action theorem and its derivative-valid
initial transpose observation in Appendix C, Parts F and V.I. Those hypotheses are
checked below for the additional forward queries. The finite Gaussian
conditioning argument for their crucial positive innovation is also given.
No assertion about arbitrary bounded initialized operators is substituted
for the canonical Gaussian initialization.

## 1. Exact odd symmetry and the singular affine obstruction

For every finite parameter state a bias-free odd network satisfies
\(h^\ell(-x)=-h^\ell(x)\) and \(f(-x)=-f(x)\). Its gates are even.
Replacing \((x_i,y_i)\) by \((y_i x_i,1)\) therefore leaves the squared loss,
as a function of all raw parameters, exactly unchanged. GF and GD have
identical parameter trajectories under this label folding. The input Gram
changes to \(D_y\Gamma D_y\), which preserves absolute pairwise separation.

Unlike two folded inputs, three folded inputs need not have an orthogonal
symmetry acting transitively on their indices. A permutation can be induced
by an input isometry only if it preserves their Gram matrix. A transitive
permutation group on three vertices forces all three off-diagonal Gram
entries to coincide. Thus generic folded triples have no symmetry forcing
all predictions or residuals to be equal.

For the affine network \(\phi(z)=az\), the predictor is linear in its input
at every parameter state. Hence its prediction vector belongs to
\(\operatorname{ran}\Gamma\). If \(v\in\ker\Gamma\), then

\[
v^Tf(t)=0,\qquad v^Tr(t)=-v^Ty
\]

at every time and for both algorithms. If \(v^Ty\ne0\),
\(\|r(t)\|_2\ge |v^Ty|/\|v\|_2>0\). In particular any residual clock
\(\int_0^\infty\|r(t)\|_1dt\) diverges. Absolute pairwise separation does
not exclude this case.

For an especially sharp example, take three unit planar vectors with
pairwise inner products \(-1/2\), and labels \(y=(1,1,1)\). This is allowed
whenever \(0<\delta<1/2\) for the requested strict separation. They obey
\(u_1+u_2+u_3=0\). All affine hidden feature sums vanish for every parameter
state. Starting at population \(C=0\), the readout derivative is zero;
the hidden derivatives have a factor \(C\) and are zero. Thus the affine
population solution is stationary with loss \(3/2\).

More generally, \(\Gamma y=0\) with \(y_i\in\{-1,1\}\) is equivalent to
the folded inputs being an equilateral triple: if
\(v_i=y_i u_i\), then \(v_1+v_2+v_3=0\), and
\(\|v_i+v_j\|^2=\|v_k\|^2=1\) gives \(v_i\cdot v_j=-1/2\).
The converse is immediate. A rank-two Gram can also have a kernel vector
with unequal coefficient magnitudes, creating an incompatible affine
target without complete stationarity.

## 2. Cubic lifting is uniformly positive for three separated lines

Let \(T_i=u_i^{\otimes3}\) in the Hilbert tensor product. Their Gram matrix
is \(\Gamma^{\circ3}\), the entrywise cube. Set
\(s_\delta=\delta(2-\delta)\). For each \(i\) and each \(j\ne i\), define

\[
v_{ij}=\frac{u_i-\Gamma_{ij}u_j}{\sqrt{1-\Gamma_{ij}^2}}.
\]

Then \(\|v_{ij}\|=1\), \(v_{ij}\perp u_j\), and
\(u_i\cdot v_{ij}=\sqrt{1-\Gamma_{ij}^2}\ge\sqrt{s_\delta}\).
If \(\{i,j,k\}=\{1,2,3\}\), put
\(R_i=u_i\otimes v_{ij}\otimes v_{ik}\). Its norm is one, and

\[
\langle T_l,R_i\rangle=0\ (l\ne i),\qquad
\langle T_i,R_i\rangle\ge s_\delta.
\]

For \(T=\sum_l c_lT_l\), Cauchy--Schwarz gives
\(|c_i|s_\delta\le\|T\|\). Summing its square over three indices proves

\[
\boxed{\quad\Gamma^{\circ3}\succeq
\frac{\delta^2(2-\delta)^2}{3}I_3.\quad}                 \tag{1}
\]

This proof permits singular \(\Gamma\), uses no covariance inverse, and
works in the actual input dimension. It proves that the cubic ridge
functions corresponding to the three inputs are linearly independent.

## 3. Explicit nonlinear feature-Gram lower bound

Let \(G\sim N(0,1)\), \(H_3(z)=z^3-3z\), and

\[
m=E(1+G^2)^{-1},\qquad b_3=(1-2m)/\sqrt6.
\]

Strict Jensen for the strictly convex function \(t\mapsto(1+t)^{-1}\)
gives \(m>1/2\), so \(b_3\ne0\). Integration by parts once yields

\[
E[\arctan(G)H_3(G)]
=E[(G^2-1)/(1+G^2)]=1-2m.
\]

Write \(Z_i=u_i\cdot g\) for the initialized first Gaussian projections
and \(P_i=H_3(Z_i)/\sqrt6\). Gaussian conditioning gives
\(E[H_3(Z_i)\mid Z_j]=\Gamma_{ij}^3H_3(Z_j)\), obtained directly by
expanding \(Z_i=\Gamma_{ij}Z_j+\sqrt{1-\Gamma_{ij}^2}G'\).
Consequently

\[
E[P_iP_j]=\Gamma_{ij}^3,\qquad
E[\phi(Z_i)P_j]=e b_3\Gamma_{ij}^3.
\]

Thus each residual \(\phi(Z_i)-e b_3P_i\) is orthogonal to every \(P_j\).
Their Gram decomposition and (1) prove

\[
Q_1:=(E[h_i^1h_j^1])_{ij}
\succeq e^2b_3^2\Gamma^{\circ3}
\succeq e^2b_3^2\frac{\delta^2(2-\delta)^2}{3}I_3.       \tag{2}
\]

There is also a direct first-chaos propagation bound. If a centered
Gaussian tuple has common variance \(q>0\) and covariance \(Q\), let
\(c=E[\phi(\sqrt qG)G]/\sqrt q\). Since
\(z\arctan z\ge0\), \(c\ge a\). Conditional Gaussian expectation shows
that \(\phi(Z_i)-cZ_i\) is orthogonal to every \(Z_j\). Therefore its
feature Gram is \(c^2Q\) plus a positive semidefinite matrix, and is at
least \(a^2Q\). The initialized scalar variances agree across samples,
so this applies at each following layer:

\[
Q_2\succeq a^2Q_1\succ0,\qquad Q_3\succeq a^2Q_2\succ0. \tag{3}
\]

For \(p=y/3\) and \(H=\sum_i p_i h_i^3\),

\[
\|H\|^2=p^TQ_3p\ge
a^4e^2b_3^2\delta^2(2-\delta)^2/9>0.                   \tag{4}
\]

This explicitly disproves a proposed exact three-point cancellation for
the positive mixture. In particular the equilateral affine obstruction
is removed already at initialization when \(e>0\).

### 3.1. Matching sharpness of the worst-case initialization scale

The \(e^2\delta^2\) scale in (2) cannot be improved uniformly over the
admissible three-input geometry, up to absolute constant factors. This is
an assertion about the smallest eigenvalue of the first initialized feature
Gram, not a necessary or sufficient bound on the training cutoff
\(e_\delta\).

For \(0<c<1\), order the planar unit inputs as

\[
u_+=(c,\sqrt{1-c^2}),\qquad u_0=(1,0),\qquad
u_-=(c,-\sqrt{1-c^2}).
\]

Their three pairwise inner products are \(c,c,2c^2-1\), and
\(v=(1,-2c,1)^T\) is a Gram-kernel vector because
\(u_+-2cu_0+u_-=0\). For independent standard normals \(G_1,G_2\), let
\(Z_0=G_1\), \(Z_\pm=cG_1\pm\sqrt{1-c^2}G_2\), and write
\(F=\arctan\). The linear part of the activation cancels exactly:

\[
\begin{split}
\sum_i v_i\phi(Z_i)
&=e\{F(Z_+)+F(Z_-)-2cF(G_1)\}\\
&=e\{F(cG_1+h)+F(cG_1-h)-2F(cG_1)\\
&\hspace{34mm}+2[F(cG_1)-cF(G_1)]\},\qquad
h=\sqrt{1-c^2}G_2.
\end{split}
\]

The bounds \(\|F'\|_\infty\le1\), \(\|F\|_\infty\le\pi/2\), and
\(\|F''\|_\infty\le1\) suffice. For the last bound,
\(2|z|/(1+z^2)^2\le1\) follows from \(2|z|\le1+z^2\).
Taylor's formula with integral remainder in both signs gives

\[
|F(x+h)+F(x-h)-2F(x)|\le h^2.
\]

Also
\(|F(cG_1)-cF(G_1)|\le(1-c)(|G_1|+\pi/2)\).
Since \(\|G_2^2\|_2=\sqrt3\) and \(\|G_1\|_2=1\), Minkowski gives

\[
\begin{split}
\|F(Z_+)+F(Z_-)-2cF(G_1)\|_2
&\le(1-c^2)\sqrt3+2(1-c)(1+\pi/2)\\
&\le(1-c)C_0,\qquad C_0=2\sqrt3+2+\pi.
\end{split}
\]

Taking the Rayleigh quotient in direction \(v\), whose squared norm is
\(2+4c^2\), proves

\[
\lambda_{\min}(Q_1)
\le \frac{e^2(1-c)^2C_0^2}{2+4c^2}.                    \tag{4a}
\]

For the closed class \(|\Gamma_{ij}|\le1-\delta\), choose
\(c=1-\delta\), \(0<\delta\le1/4\). The center-to-side inner products
equal \(1-\delta\). The side-to-side inner product is
\(r=1-4\delta+2\delta^2>0\), and
\((1-\delta)-r=\delta(3-2\delta)>0\). Hence all three absolute
pairwise inequalities hold, and

\[
\lambda_{\min}(Q_1)
\le \frac{e^2\delta^2C_0^2}{2+4(1-\delta)^2}.           \tag{4b}
\]

For the requested strict class
\(-1+\delta<\Gamma_{ij}<1-\delta\), choose instead
\(c=1-2\delta\), again with \(0<\delta\le1/4\). The two center-to-side
inner products lie strictly inside the interval since
\((1-\delta)-c=\delta>0\) and \(c-(-1+\delta)=2-3\delta>0\).
For the side-to-side inner product \(r=1-8\delta+8\delta^2\), both
strict inequalities follow from

\[
(1-\delta)-r=\delta(7-8\delta)>0,
\]

\[
r-(-1+\delta)
=2-9\delta+8\delta^2
=(1-4\delta)(2-2\delta)+\delta>0.
\]

Thus this example is strictly admissible and satisfies

\[
\lambda_{\min}(Q_1)
\le \frac{4e^2\delta^2C_0^2}{2+4(1-2\delta)^2}
\le\frac43 C_0^2e^2\delta^2.                           \tag{4c}
\]

These unit vectors can be embedded in every fixed \(d\ge2\); multiplying
them by \(\sqrt d\) gives the model's exact input normalization. Let
\(\Lambda_1(e,\delta;d)\) denote the infimum of \(\lambda_{\min}(Q_1)\)
over all strictly admissible triples in that dimension for
\(\phi(z)=(1-e)z+e\arctan z\). Combining (2) and (4c) gives, for every
\(d\ge2\), \(0<e\le1/2\), and \(0<\delta\le1/4\),

\[
\frac{b_3^2}{3}e^2\delta^2
\le\Lambda_1(e,\delta;d)
\le\frac43 C_0^2e^2\delta^2.                           \tag{4d}
\]

The constants are absolute and independent of dimension, labels, \(e\),
and \(\delta\). This is the precise worst-case
\(\Theta(e^2\delta^2)\) initialization statement. The kernel vector used
in its Rayleigh quotient need not be a binary-label vector; the claim is
about the least eigenvalue, not every binary-label projection of the Gram.
It yields no all-time training, flow-existence, or cutoff sharpness claim.

## 4. Backward positivity and bottom-layer motion

Use the exact initialization notation

\[
D_i^\ell=\phi'(Z_i^\ell),\quad
\beta_i^3=HD_i^3,\quad q_i^2=B_0^*\beta_i^3,
\quad\beta_i^2=D_i^2q_i^2,
\quad q_i^1=A_0^*\beta_i^2,\quad\beta_i^1=D_i^1q_i^1,
\]

and \(S_\ell=(E[\beta_i^\ell\beta_j^\ell])_{ij}\).
By (3), \(Z^3\) is a nondegenerate Gaussian triple. If \(v^TS_3v=0\),
positive density and continuity imply the everywhere identity

\[
\left(\sum_i p_i\phi(z_i)\right)
\left(\sum_i v_i\phi'(z_i)\right)=0.
\]

The first factor has no open zero set, because each of its coordinate
derivatives is \(p_i\phi'(z_i)\ne0\). The second therefore vanishes
everywhere. Its derivative in coordinate \(i\) is
\(v_i\phi''(z_i)=0\). As \(\phi''\) is not identically zero, \(v_i=0\).
Hence \(S_3\succ0\).

Appendix C, Part V.I's exact transpose identities are

\[
q_i^2=\zeta_i^2+\sum_k T_{ik}h_k^2,\qquad
q_i^1=\zeta_i^1+\sum_k R_{ik}h_k^1,                    \tag{5}
\]

where \(T,R\) are deterministic derivative responses,
\(\operatorname{Cov}\zeta^2=S_3\), and
\(\operatorname{Cov}\zeta^1=S_2\). Each reverse group is independent
of all forward groups and roots. The covariances are the full second
moments of the corresponding reverse inputs. The deterministic responses
must not be discarded. Conditioning successively gives

\[
S_2\succeq a^2\lambda_{\min}(S_3)I_3\succ0,\qquad
\operatorname{Cov}(\beta^1\mid Z^1)
\succeq a^2\lambda_{\min}(S_2)I_3.                    \tag{6}
\]

Define the hidden directions exactly as in Appendix C, Part N,

\[
V^1=d^{-1}\sum_i p_i\beta_i^1x_i,\quad
V^2=\sum_i p_i\beta_i^2\otimes h_i^1,\quad
V^3=\sum_i p_i\beta_i^3\otimes h_i^2.
\]

Equations (2), (3), and (6) imply

\[
dE\|V^1\|^2\ge a^2\lambda_{\min}(S_2)\sum_i p_i^2>0,
\]

\[
\|V^\ell\|_{\rm HS}^2
=\operatorname{tr}(\operatorname{diag}(p)S_\ell
                   \operatorname{diag}(p)Q_{\ell-1})>0
\quad(\ell=2,3).
\]

For each sample,
\(U_j^1=\sum_i\Gamma_{ji}p_i\beta_i^1\) satisfies

\[
\|U_j^1\|^2\ge a^2\lambda_{\min}(S_2)p_j^2>0.          \tag{7}
\]

No rank assumption on the first Gaussian triple enters these inequalities.

## 5. A direct proof of every upper sample's initial motion

This is the new part of the argument. Set

\[
t_j=D_j^1U_j^1,\qquad
c_{ji}=p_i\{(Q_1)_{ij}+\Gamma_{ji}E[D_j^1D_i^1]\}.
\]

The explicit dependence in (5) gives
\(\partial_{\zeta_i^1}t_j=D_j^1\Gamma_{ji}p_iD_i^1\).
The initialized forward return rule therefore yields

\[
A_0t_j=\xi_{t_j}+\sum_i\beta_i^2\Gamma_{ji}p_iE[D_j^1D_i^1],
\]

and hence the exact forward linearization is

\[
U_j^2=V^2h_j^1+A_0t_j
=\xi_{t_j}+\sum_i c_{ji}\beta_i^2.                     \tag{8}
\]

The new source \(\xi_{t_j}\) belongs to the A-forward Gaussian group.
Regress it on that group's three initialized sources \(Z^2\). Its
independent Gaussian remainder has variance

\[
\sigma_{2,j}^2
=\inf_{b\in\mathbb R^3}\left\|t_j-\sum_i b_i h_i^1\right\|_2^2
\ge E\operatorname{Var}(t_j\mid Z^1)
\ge a^4\lambda_{\min}(S_2)p_j^2>0.                    \tag{9}
\]

The last inequality uses (6) and both factors \(D_j^1,D_i^1\ge a\).
The remainder is independent of \(Z^2\) and of the independent B-reverse
group \(\zeta^2\). Since \(\beta^2\) depends only on those old variables,
(8) has an uncancelled Gaussian component of variance \(\sigma_{2,j}^2\).
Thus \(U_j^2\ne0\) for every \(j\).

For the final layer put \(s_j=D_j^2U_j^2\). From (8),
\(\partial_{\zeta_i^2}s_j=D_j^2c_{ji}D_i^2\), since every A-forward
named source is a separate independent source group. The B-forward
return rule gives

\[
U_j^3=V^3h_j^2+B_0s_j
=\xi_{s_j}+
\sum_i\beta_i^3\{p_i(Q_2)_{ij}+c_{ji}E[D_j^2D_i^2]\}.   \tag{10}
\]

After regressing \(\xi_{s_j}\) on the initial B-forward sources \(Z^3\),
its independent Gaussian remainder has variance

\[
\begin{split}
\sigma_{3,j}^2
&=\inf_b\left\|s_j-\sum_i b_i h_i^2\right\|_2^2\\
&\ge E\operatorname{Var}(s_j\mid Z^2,\zeta^2)
=E[(D_j^2)^2]\sigma_{2,j}^2
\ge a^2\sigma_{2,j}^2>0.
\end{split}                                             \tag{11}
\]

Here (9)'s remainder is independent of \((Z^2,\zeta^2)\), and all the
features \(h_i^2\) are measurable with respect to that tuple. In (10),
\(\beta^3\) is a function of the initialized \(Z^3\) alone. The new
remainder cannot cancel it, proving \(U_j^3\ne0\). Finally the feature
directions \(D_j^\ell U_j^\ell\) are nonzero because \(D_j^\ell\ge a\).

### Why the extra source calls are legitimate

All initialization variables in (5), (8), and (10) are bounded smooth
multipliers times finite sums of Gaussian sources and linear-growth smooth
functions of Gaussian sources. They have every finite moment. The added
inputs \(t_j,s_j\) are not globally bounded-derivative maps of their named
sources, but this is resolved by the same finite-transcript truncation as
Appendix C, Part V.I: truncate every unbounded incoming Gaussian-linear factor with a
smooth clip, apply the fixed-program theorem, and then remove the clips in
the actual action answers using bounded operator norms. The gate and its
derivatives are bounded; the factors appearing in the displayed source
derivatives either are bounded or have a fixed integrable Gaussian-linear
envelope. Dominated convergence therefore passes those response coefficients.
Source Gram convergence and continuous positive-semidefinite square roots
give the joint Gaussian-source limits. This uses finitely many calls only.

One can prove the needed positive innovation without the derivative
formula. Condition the finite initialized matrix A on all previous calls
\(AV=Y\) and \(A^TU=Q\), where the columns of V are the three \(h_i^1\)
and the columns of U are the three \(\beta_i^2\). For the next input
\(t_j\), exact Gaussian conditioning gives an independent new noise term

\[
\|(I-P_V)t_j\|_n\,P_{U^\perp}g_n,
\]

besides transcript-measurable terms. The expected normalized squared
length removed by \(P_U\) is \(\operatorname{rank}U/n\le3/n\).
The residual input norm converges to the positive quantity in (9), because
\(Q_1\succ0\) and all required contractions have fixed-transcript limits.
Therefore the limiting new scalar noise is an independent normal with
strictly positive variance. The B call with input \(s_j\) gives (11) by
the identical argument, now using \(Q_2\succ0\). This also verifies that
reuse of the same matrices cannot silently remove the innovations.

## 6. Physical acceleration and kernel variation need no scalar clock

On any canonical strong solution with the trajectory chain rule,
\(C(0)=0\), \(r(0)=-y\), and \(\dot C(0)=3H\). Thus
\(b_i^\ell(t)=3t\beta_i^\ell+o_{L^2}(t)\) and

\[
\theta_h(t)=\theta_h(0)+\frac92t^2V+o_{\rm raw}(t^2),
\qquad z_j^\ell(t)=Z_j^\ell+\frac92t^2U_j^\ell+o_{L^2}(t^2).
\]

The derivatives of the vector fields, obtained by the same backward
multiplier limits, give the actual right second derivatives
\(9V\), \(9U_j^\ell\), and \(9D_j^\ell U_j^\ell\), respectively.
All are nonzero by the preceding sections. The initial hidden first
derivatives are zero, as dictated by the population-zero readout.

Let \(J\) be the hidden directional linearization of
\(H(\theta_h)=\sum_i p_i h_i^3(\theta_h)\). Adjunction gives
\(V=J^*H\). Consequently

\[
p^TK^4(t)p=\|H(t)\|^2
=\|H\|^2+9t^2\|V\|_{\rm hidden}^2+o(t^2),
\]

while the projected sum of the three hidden kernel blocks is
\(9t^2\|V\|_{\rm hidden}^2+o(t^2)\). Therefore

\[
p^TK(t)p=p^TK(0)p+18t^2\|V\|_{\rm hidden}^2+o(t^2).    \tag{12}
\]

Neither equal predictions nor a feature-time reparameterization was used.
If readout acceleration is also required,
\(\ddot C(0)=-\sum_i(Q_3y)_i h_i^3\ne0\), since \(Q_3\succ0\).

## 7. Remaining analytic bridge

At initialization every scalar preactivation is a centered Gaussian of
positive variance, so its arctangent regression error is positive. For the
convex mixture with \(a\ge1/2\), the three initial standard deviations lie
between \(1/4\) and \(1\). Compactness and continuity give a uniform
strictly positive initial regression gap; continuity in \(L^2\) preserves
it for a sufficiently short interval along any regular solution.
This does not prove a gap at every later physical time.

The complete requested theorem still requires a single positive choice
\(e_\delta\), independent of physical horizon and of the potentially
singular Gram, together with all of the following:

1. A global canonical uncut strong flow and source-tail control sufficient
   to remove backward caps on every compact physical interval.
2. Uniqueness against all bounded-primal strong competitors and unique
   continuation from reached states.
3. A mechanism preventing the sample activation laws from losing their
   affine-regression gap over the whole physical trajectory.
4. The finite-width GF/raw-GD, velocity, path, kernel, and generated-probe
   identifications through those cap-independent reference estimates.

The existing fixed-program and compact-reference limit machinery can be
used once the required reference and tail estimates are supplied. It does
not supply them merely from the positive initial Gram (2).

Two exact diagnostics locate the failure of a direct two-input transplant:

* A generic three-input folded Gram has no transitive symmetry, so a single
  scalar residual and its exact one-dimensional time conversion are absent.
* Even a symmetric equilateral triple has zero affine signal. Its nonlinear
  initial projected kernel is positive but can be of order \(e^2\), whereas
  the affine perturbation bounds require a bounded reference clock independent
  of \(e\). An \(O(e^{-2})\) clock and growing reference bounds cannot be
  inserted into the affine small-\(e\) threshold without a new estimate.

A direct nonlinear source/continuation theorem valid on arbitrary bounded
physical intervals, plus a trained-law nondegeneracy mechanism, would bridge
these gaps. Alternatively a nonlinear reference that retains the cubic
signal in singular directions could replace the affine reference, but
its uniform source estimates and nonaffinity control must be proved.
The present note gives no counterexample to those possible conclusions.

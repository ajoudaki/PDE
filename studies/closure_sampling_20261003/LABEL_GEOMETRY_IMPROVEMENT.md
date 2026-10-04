# Sample cancellation, Gaussian derivative geometry, and the remaining fitting gap

2026-10-04. Scoped internal investigation in `closure_sampling_20261003`.
The complete assigned inputs were `DATASET_LABEL_DEPENDENCE.md`,
`DATASET_SOURCE_CONSTANTS.md`, `DATASET_MAXIMUM_REFINEMENT.md`,
`GENERAL_WEIGHTED_COMPARISON.md`, and `GENERAL_ANALYTIC_COMPRESSION.md`.
No other study, experiment, or manuscript source was used. This note is
not a promotion review or an improved unconditional fitting theorem.

The independent candidate, recorded before exchange, was to retain the
signed feature synthesis of the residual in hidden-gradient estimates,
instead of replacing it by the residual RMS. The exact missing estimate
is identified below. A complete initialized Gaussian derivative estimate
does retain those cancellations and has only a logarithmic relative loss.
The learned readout factor prevents directly substituting that estimate
into the actual training argument. In particular, this investigation has
not proved the requested sufficient scale
`gamma times a subpolynomial penalty in m`.

## 1. Exact dynamics and where the current sample-count loss occurs

Let \(v_a=x_a/\sqrt d\in S^{d-1}\), \(a=1,\ldots,m\), and let all
hidden widths be \(n\). The model, loss, and physical gradient flow are

\[
 z_a^{(1)}=Av_a,\qquad
 z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
 h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),\qquad
 f_a=\frac{w^\top h_a^{(L)}}n,
\]
\[
 c_a=y_a-f_a,\qquad \rho^2=\mathcal L=\frac1m\sum_a c_a^2,
 \qquad Y^2=\frac1m\sum_a y_a^2,
\]
\[
 k_a^{(L)}=w,\qquad
 \delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)},
 \qquad k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)},
\]
\[
 \dot A=\frac2m\sum_a c_a\delta_a^{(1)}v_a^\top,\qquad
 \dot W^{(\ell)}=\frac2{mn}\sum_a c_a\delta_a^{(\ell)}
                                      h_a^{(\ell-1)\top},\qquad
 \dot w=\frac2m\sum_a c_a h_a^{(L)},\qquad w(0)=0.
 \tag{1}
\]

Put \(\|u\|_n=\|u\|_2/\sqrt n\), let \(H_L\) have columns
\(h_a^{(L)}\), and put \(G=H_L^\top H_L/n\). A finite initialized
gap \(G(0)\succeq m\lambda I_m\) gives the normalized gap
\(\lambda\). In the limiting Gaussian statement of the assigned
sources, \(\lambda\) is a fixed fraction of \(\gamma/m\), where
\(\gamma=\lambda_{\min}(Q^{(L)})\).

Define the mobility norm by

\[
 \|\dot\theta\|_{\rm mob}^2
 =\frac{\|\dot A\|_F^2}{n}
  +\sum_{\ell=2}^L\|\dot W^{(\ell)}\|_F^2
  +\|\dot w\|_n^2.
\]

The exact loss identity and the readout part of the tangent Gram give,
as long as \(G(t)/m\succeq\lambda I_m/4\),

\[
 -\frac d{dt}\rho^2=\|\dot\theta\|_{\rm mob}^2,
 \qquad -\dot\rho\ge\frac\lambda2\rho,
 \qquad
 P(t):=\int_0^t\|\dot\theta(s)\|_{\rm mob}\,ds
       \le\frac{2(Y-\rho(t))}{\sqrt\lambda}.
 \tag{2}
\]

In particular \(\|w(t)\|_n\le P(t)\). The existing proof bounds
each hidden speed by \(C\rho\|w\|_n\), obtains total hidden
displacement \(CY^2/\lambda^{3/2}\), and compares this with the
feature singular value \(\sqrt\lambda\). The resulting sufficient
condition is \(Y\le c\lambda\). No algebraic change of the
physical clock removes that loss.

The following simple exact calculation is a useful restriction on
possible repairs. Freeze the initialized features and take a label vector
in an eigenspace of \(G(0)\) with eigenvalue \(\gamma\). The actual
mean-loss readout flow then satisfies

\[
 c(t)=e^{-2\gamma t/m}y,\qquad
 \rho(t)=Ye^{-2\gamma t/m},\qquad
 \int_0^\infty\rho(t)\,dt=\frac{mY}{2\gamma}.
 \tag{3}
\]

This is an obstruction to replacing residual activity by
\(CY/\gamma\) in the existing argument. It is not an obstruction to
fitting: the frozen-feature model fits exactly. Changing the clock in
(3) changes all the update coefficients by the inverse factor, leaving
the integrated physical displacement unchanged. Equation (3) is a
diagnostic calculation, not a replacement of the all-layer model (1).

## 2. A precise stronger estimate that would improve real fitting

Here is a deterministic implication isolating the required geometry. All
constants in this section depend only on a real activation bound \(B\ge1\),
a slope bound \(s\ge1\), initial hidden-operator bound \(K\ge1\),
and depth \(L\). They have no hidden dependence on \(m,n\), or the
input arrangement. Assume bounded second derivatives for local uniqueness.

Write

\[
 V_h(t)^2=\frac{\|\dot A(t)\|_F^2}{n}
                +\sum_{\ell=2}^L\|\dot W^{(\ell)}(t)\|_F^2.
\]

Suppose a number \(\beta\ge1\) bounds the following **additional,
unproved-for-the-general-network** quantity on the interval before a
hidden operator reaches \(K+1\) or the normalized feature gap reaches
\(\lambda/4\):

\[
             V_h(t)\le \beta\|w(t)\|_n\|\dot w(t)\|_n.
 \tag{4}
\]

The inequality is interpreted directly when one factor vanishes; there
is no division by the zero initial readout. At a zero residual every
velocity vanishes.

**Conditional fitting proposition.** There is an explicit structural
constant \(C_0\ge1\), defined below, such that (4) and

\[
                 Y\le\frac{\lambda^{3/4}}{\sqrt{8C_0\beta}}
 \tag{5}
\]

imply global fitting and convergence, with
\(G(t)/m\succeq9\lambda I_m/16\). The residual and total-path
bounds of (2) then hold for all time. This implication is not claimed
as an unconditional improvement: proving (4) is its substantive premise.

To specify \(C_0\), let \(R=K+1\), and for a hidden velocity vector
of block norms

\[
 a_1=\|\dot A\|_F/\sqrt n,\qquad
 a_\ell=\|\dot W^{(\ell)}\|_F\quad(2\le\ell\le L),
\]

define the nonnegative linear forms

\[
 q_1(a)=s a_1,\qquad
 q_\ell(a)=s\{B a_\ell+R q_{\ell-1}(a)\}.
\]

Let \(C_H\) be the Euclidean norm of the coefficient vector of \(q_L\),
and set \(C_0=\max\{1,B,C_H\}\). Differentiating the forward pass
shows, uniformly over sphere inputs,

\[
 \|\dot h^{(L)}(t,v)\|_n\le C_H V_h(t).
 \tag{6}
\]

Indeed the first layer costs \(sa_1\); each later layer costs
\(s(Ba_\ell+R\|\dot h^{(\ell-1)}\|_n)\). This gives exactly
the displayed recursion and Cauchy--Schwarz in the block index.

By (2), (4), \(\|w\|_n\le P\), and
\(\|\dot w\|_n\le\dot P\),

\[
 \int_0^tV_h(s)\,ds
 \le\beta\int_0^tP(s)\dot P(s)\,ds
 =\frac\beta2P(t)^2\le\frac{2\beta Y^2}{\lambda}.
 \tag{7}
\]

Thus (5) bounds the hidden path by
\(\sqrt\lambda/(4C_0)\). Since bounded activations give
\(\lambda\le B^2/m\le B^2\), every hidden operator moves by
at most \(1/4\). Also (6) bounds

\[
 \left\|\frac{H_L(t)-H_L(0)}{\sqrt{mn}}\right\|_{\rm op}
 \le\left\|\frac{H_L(t)-H_L(0)}{\sqrt{mn}}\right\|_F
 \le\frac{\sqrt\lambda}{4}.
\]

The initialized smallest feature singular value is at least
\(\sqrt\lambda\), so the current one is at least
\(3\sqrt\lambda/4\). Both proposed exits have strict margins.
The finite path bound (2), local uniqueness, and extension from a finite
limiting state exclude a finite maximal time. Residual decay then gives
interpolation and parameter convergence. This proves the proposition.

The comparison between (5) and the previous bound is informative:
if one can prove (4) with \(\beta\ll\lambda^{-1/2}\), it is a real
improvement. Substituting the generic bound
\(\beta=C\lambda^{-1/2}\) gives exactly the previous scale
\(Y\le c\lambda\). Therefore (4) identifies a concrete estimate
that must improve, rather than relabeling the normalized gap.

## 3. A proved Gaussian derivative estimate with no input restrictions

Let \(u_1,\ldots,u_m\in\mathbb R^p\) satisfy
\(\|u_a\|_2\le R_u\), where the Gaussian dimension \(p\) can be
arbitrary. Let \(g\sim N(0,I_p)\), and let \(\phi\) be real on
the real axis, holomorphic on \(|\operatorname{Im}z|<b\), and
bounded there by \(B\ge1\). Define the feature and derivative Grams

\[
 Q_{ab}=\mathbb E[\phi(g^\top u_a)\phi(g^\top u_b)],
\]
\[
 D_{ab}=(u_a^\top u_b)
       \mathbb E[\phi'(g^\top u_a)\phi'(g^\top u_b)].
 \tag{8}
\]

**Gaussian derivative proposition.** If \(Q\succeq\gamma I_m\)
for \(\gamma>0\), then

\[
       D\preceq C\left[\log\left(\frac{eB^2m}{\gamma}\right)
                  \right]^2 Q,
 \tag{9}
\]

where \(C\) depends only on \(b,R_u\). In particular, it does not
depend on \(m,p\), pairwise input separations, or any intermediate
covariance gap. No sphere separation or nonproportionality assumption
is used beyond the stated positive final Gram.

Here is a proof including the tail estimate that produces the logarithm.
For a coefficient vector \(c\in\mathbb R^m\), put

\[
 F(g)=\sum_a c_a\phi(g^\top u_a),\qquad
 E=\mathbb E[F(g)^2],\qquad M=B\sum_a|c_a|.
\]

Then \(c^\top Qc=E\), \(c^\top Dc=\mathbb E\|\nabla F\|_2^2\),
and \(0<E\le M^2\) for \(c\ne0\). Cauchy's formula on a
circle of radius \(b/2\) gives, for every integer \(k\ge0\),

\[
 \mathbb E\|\nabla^kF\|_{\rm HS}^2
 \le M^2(k!)^2 a^{2k},\qquad
 a=\max\{1,2R_u/b\}.
 \tag{10}
\]

The norm of \(u_a^{\otimes k}\) is \(\|u_a\|^k\); the triangle
inequality therefore proves (10) without a factor depending on \(p\).

Expand \(F\) in the orthonormal multivariate Gaussian Hermite basis,
and let \(E_j\) be the squared norm of its component of total degree
\(j\). Orthogonality and the derivative rule for normalized Hermite
polynomials give

\[
 E=\sum_{j\ge0}E_j,\qquad
 \mathbb E\|\nabla^kF\|_{\rm HS}^2
       =\sum_{j\ge k}(j)_kE_j,
 \tag{11}
\]

where \((j)_k=j(j-1)\cdots(j-k+1)\). To see the tensor factor,
sum squared derivatives over all ordered \(k\)-tuples of coordinate
indices: for a Hermite multi-index of total degree \(j\), the sum of
the corresponding falling factorials is exactly \((j)_k\).
The bounded derivatives in (10) place \(F\) in every Gaussian Sobolev
space, so the polynomial identities extend to \(F\) by orthogonal
truncation; Gaussian integration by parts identifies its weak derivative
coefficients with the displayed Hermite derivatives.

For \(J\) large enough, choose
\(k=\lfloor\sqrt J/(4a)\rfloor\), so \(1\le k\le J/2\).
Equations (10)--(11), \((j)_k\ge(J/2)^k\) for \(j\ge J\),
and \(k!\le k^k\) imply

\[
 \sum_{j\ge J}E_j
 \le M^2\left(\frac{2a^2k^2}{J}\right)^k
 \le M^2 8^{-k}
 \le C M^2e^{-c\sqrt J}.
 \tag{12}
\]

Enlarging \(C\) proves the last bound for all integer \(J\ge1\).
The constants depend only on \(a\). Since

\[
 \sum_{j\ge1}jE_j=\sum_{J\ge1}\sum_{j\ge J}E_j,
\]

split this sum at
\(J_0=\lceil C_1\log^2(eM^2/E)\rceil\). The terms through
\(J_0\) total at most \(J_0E\). Comparing the tail of (12) with
the integral after the substitution \(u=\sqrt J\) bounds the remaining
terms by

\[
 C M^2(1+\sqrt{J_0})e^{-c\sqrt{J_0}}\le CE
\]

when the structural constant \(C_1\) is sufficiently large. Hence

\[
 \mathbb E\|\nabla F\|_2^2
 \le CE\log^2(eM^2/E).
 \tag{13}
\]

Finally \(M^2\le B^2m\|c\|_2^2\) and
\(E\ge\gamma\|c\|_2^2\). Substitution into (13) proves (9).
The zero coefficient vector is immediate.

At initialization of the actual deep network, condition on the previous
layer and set
\(u_a=h_a^{(\ell-1)}(0)/\sqrt n\) for \(\ell\ge2\).
Then \(\|u_a\|\le B\), and the rows of
\(\sqrt n W_0^{(\ell)}\) are independent standard Gaussians.
Thus (8)--(9) apply conditionally, whenever that conditional feature
Gram has the specified gap. The first layer uses \(u_a=v_a\).
For fixed \(m\), empirical versions converge entrywise: feature products
and derivative products are uniformly bounded, so their conditional
variances are \(O(1/n)\). A union bound over \(m^2\) entries and
\(\|E\|_{\rm op}\le m\|E\|_{\max}\) transfer (9), with fixed
slack, to the empirical matrices at sufficiently large width. This
statement concerns initialized layers only.

## 4. Why the initialized proposition does not close all-layer training

The distinction is visible already at the last hidden matrix. At a real
time \(t\), define

\[
 (D_w)_{ab}=
 \langle h_a^{(L-1)},h_b^{(L-1)}\rangle_n
 \frac1n\sum_{i=1}^n
 w_i^2\phi_L'(z_{a,i}^{(L)})\phi_L'(z_{b,i}^{(L)}).
 \tag{14}
\]

Directly expanding (1) gives the exact identities

\[
 \|\dot W^{(L)}\|_F^2=\frac4{m^2}c^\top D_wc,
 \qquad
 \|\dot w\|_n^2=\frac4{m^2}c^\top Gc.
 \tag{15}
\]

The unweighted version of (14) has \(w_i^2\) replaced by one; call
it \(D_1\). Equation (9) concerns that unweighted matrix at
initialization. The matrix required by (4) is instead \(D_w\), and
the readout is learned from precisely the same rows and feature values.
Replacing \(w_i^2\) by its neuron average would assert an independence
that is absent even in the first nonzero time derivative of training.
The valid elementary bound is only

\[
                D_w\preceq\|w\|_\infty^2D_1.
 \tag{16}
\]

The source proof bounds \(\|w\|_\infty\) by residual activity.
Consequently (16) does not yield (4) with a useful coefficient from
(9). Earlier layers have additional correlated backward factors, and
after initialization the conditional Gaussian row structure itself
must be replaced by a proved transport or cavity comparison. Neither
step is supplied by the initialized derivative proposition.

This is not merely a technical possibility of large Gaussian moments.
Consider the one-dimensional family

\[
 \phi_R(x)=e^{-(x-R)^2/2},\qquad g\sim N(0,1).
\]

For any fixed strip width \(b\), all these activations are bounded
there by \(e^{b^2/2}\), uniformly in the real translation \(R\).
Taking a readout profile proportional to the feature itself gives

\[
 Q_R=\mathbb E[\phi_R(g)^2]=\frac1{\sqrt3}e^{-R^2/3},
\]
\[
 \mathbb E[\phi_R(g)^2\phi_R'(g)^2]
 =\frac1{\sqrt5}\left(\frac15+\frac{R^2}{25}\right)e^{-2R^2/5}.
 \tag{17}
\]

Completing the square in each Gaussian integral proves these formulas:
the second tilted Gaussian has mean \(4R/5\) and variance \(1/5\),
so its mean squared distance from \(R\) is \(R^2/25+1/5\).
Thus the mixed derivative ratio is

\[
 \frac{\mathbb E[\phi_R^2\phi_R'^2]}{Q_R^2}
 =\frac3{\sqrt5}\left(\frac15+\frac{R^2}{25}\right)e^{4R^2/15}.
 \tag{18}
\]

It cannot be bounded by a constant depending only on the common strip
width and bound, or by a power of \(\log(1/Q_R)\). This is an
actual Gaussian analytic feature calculation. Its readout profile is
also the initial readout-velocity profile for one sample, up to the
label factor. It does not disprove the desired label theorem: for
\(m=1\) there is no sample-count improvement to make. It disproves
one tempting missing step, namely that unweighted Gaussian derivative
domination automatically extends to learned feature-correlated weights
with only logarithmic loss.

## 5. Scope of the result and consequences for the source theorem

The complete unconditional result established here is (9), an initialized
Gaussian feature/derivative comparison with all \(m\)-dependence
displayed. The complete dynamical result is the conditional implication
(4)--(5), identifying the weighted derivative estimate that would
strictly improve the old real fitting bootstrap. Equations (14)--(18)
show why the initialized result does not establish its hypothesis.

The existing analytic compression proof separately requires

\[
 S=C\frac{mY}{\gamma},\qquad
 S^2B_{\rm car}\le c,\qquad
 B_{\rm car}=C\exp\{C\sqrt{\log(em)}\}.
\]

Even an improvement of real fitting alone would not change this source
condition while the same activity-normalized insertion budget is used.
Equation (3) rules out improving the activity estimate itself uniformly
by a factor \(m\). A successful proof at the requested label scale must
therefore also exploit cancellation or the distribution of learned
responses inside the carrier and insertion estimates. It cannot follow
by replacing \(\lambda\) by \(\gamma\) in their existing formulas.

No necessity statement for the factor \(m\), no counterexample to
all-layer Gaussian fitting, and no improved full-compression threshold
have been proved in this note. The useful new information is the exact
relative-derivative estimate available at initialization and the precise
mixed-moment and trajectory-control estimates still required to turn it
into a label theorem.

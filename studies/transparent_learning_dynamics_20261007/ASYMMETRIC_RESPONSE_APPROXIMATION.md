# Unequal labels: a closed approximation with ordered feature writes

2026-10-07. Scoped analytical continuation of the causal two-hidden-layer
candidate. Scientific inputs: CANDIDATE_SYSTEM.md,
ANALYTICAL_LEARNING_PROFILES.md, and RESIDUAL_CLOCK_CHECK.md in this study.
No experiment, fitted trajectory coefficient, or global approximation proof
is included.

The unequal-label case admits a five-scalar approximation for both training
outputs and the passive output, or a six-scalar implementation that evolves
the outputs directly. Its fixed coefficients are initial Gaussian
expectations. Four scalars suffice for training alone. A two-scalar cubic
potential is also correct through cubic order in small labels, but omits the
first response to a rotating residual direction. The distinction matters:
control degree and small-label order are not the same once the controls are
determined by the evolving predictions.

## Setup and the retained orders

Use the canonical normalization with two training samples,

\[
v_1=e_1,\quad v_2=e_2,\quad v_3=(2e_1+e_2)/\sqrt5,
\qquad y=(0.6,-0.3).
\]

Sample 3 is passive. Write \(T=\tanh\), \(g=T'=\operatorname{sech}^2\), and
\(S_{ab}=v_a^\top v_b\). The source network has

\[
z_{1,a}=Av_a,\quad h_{1,a}=T(z_{1,a}),\quad
z_{2,a}=Wh_{1,a},\quad h_{2,a}=T(z_{2,a}),\qquad
f_a=n^{-1}w^\top h_{2,a},\qquad
\mathcal L=\tfrac12\sum_{a=1}^2(y_a-f_a)^2.
\]

Here \(A\in\mathbb R^{n\times2}\), \(W\in\mathbb R^{n\times n}\), and
\(w\in\mathbb R^n\). Initially \(A\) has independent \(N(0,1)\) entries,
\(W\) has independent \(N(0,1/n)\) entries, these matrices are independent,
and \(w=0\). The physical factor \(2/m\) is one. Set
\(c_a=y_a-f_a\), \(\delta_{2,a}=g(z_{2,a})\odot w\), and
\(\delta_{1,a}=g(z_{1,a})\odot W^\top\delta_{2,a}\), where \(\odot\)
denotes entrywise multiplication. The physical velocities are

\[
\dot A=\sum_{a\le2}c_a\delta_{1,a}v_a^\top,\qquad
\dot W=\frac1n\sum_{a\le2}c_a\delta_{2,a}h_{1,a}^\top,\qquad
\dot w=\sum_{a\le2}c_a h_{2,a}.
\]

Each hidden velocity multiplies a residual by a backward field proportional
to the current readout.

First regard \(c_1,c_2\) as prescribed controls. Define their accumulated
deficits and ordered integrals by

\[
u_a(t)=\int_0^t c_a(s)\,ds,\qquad
I_{ab}(t)=\int_0^t c_a(s)u_b(s)\,ds,\qquad a,b\le2.
\tag{1}
\]

The first index in \(I_{ab}\) is the current hidden write; the second is
the earlier readout write supplying its backward signal. The exact identities

\[
I_{11}=\tfrac12u_1^2,\quad I_{22}=\tfrac12u_2^2,\quad
I_{12}+I_{21}=u_1u_2
\]

leave one independent signed area,

\[
\mathcal A=I_{12}-I_{21},\qquad
\dot{\mathcal A}=c_1u_2-c_2u_1,
\qquad I_{12,21}=\tfrac12(u_1u_2\pm\mathcal A).
\tag{2}
\]

Scaling the prescribed control by a common small factor assigns degree one
to \(u\), degree two to \(I\) and \(\mathcal A\), degree two to the leading
hidden displacement, and degree three to the first output correction. The
approximation below keeps precisely these hidden and output terms before
closing the control by \(c=y-f\). Oddness under simultaneous control and
readout sign reversal removes the intervening degrees. Remainders here are
formal population coefficients, or ordinary local finite-width expansions
followed by limits of their coefficients. No uniform population remainder
is claimed.

## Coefficients evaluated only at initialization

Let \(X_1,X_2\) be independent standard Gaussians,
\(X_3=(2X_1+X_2)/\sqrt5\), and \(H_a=T(X_a)\). Define

\[
C^{1,0}_{ab}=\mathbb E[H_aH_b],\qquad
Z\sim N(0,C^{1,0}),\qquad K_a=T(Z_a),\qquad
C^{2,0}_{ab}=\mathbb E[K_aK_b].
\tag{3}
\]

The lower and upper expectations in the formulas below are separate
population expectations. In particular \(Z_3\) is not the same linear
combination of \(Z_1,Z_2\) as \(X_3\) is of \(X_1,X_2\).

Put

\[
\begin{aligned}
\sigma^2&=\mathbb E[T(X)^2],&q_X&=\mathbb E[g(X)^2],&
\tau_X&=\mathbb E[T(X)^2g(X)^2],\quad X\sim N(0,1),\\
\nu&=\mathbb E[T(Z)^2],&\alpha&=\mathbb E[g(Z)],&
\beta&=\mathbb E[g(Z)^2],\quad Z\sim N(0,\sigma^2),\\
\tau&=\mathbb E[T(Z)^2g(Z)^2],&&
r_0&=3\beta-2\alpha.
\end{aligned}
\tag{4}
\]

For training indices \(j,b\), the initial reverse input and its derivatives
are

\[
d_{jb}(Z)=g(Z_j)K_b,\qquad
R_{jb,c}=\mathbb E[\partial_{Z_c}d_{jb}(Z)].
\]

Only the following derivative entries are nonzero:

\[
R_{jj,j}=r_0,\qquad R_{jb,b}=\alpha^2\quad(j\ne b).
\tag{5}
\]

The corresponding lower return is

\[
B_{jb}=\zeta_{jb}+\sum_{c=1}^2R_{jb,c}H_c,\qquad
\mathbb E[\zeta_{jb}\zeta_{kd}]
=\mathbb E[d_{jb}(Z)d_{kd}(Z)].
\tag{6}
\]

The centered Gaussian family \(\zeta\) is independent of the lower roots.
Its covariance is the full displayed uncentered pairing; the reaction term
in (6) is not subtracted from that covariance.

To make every observable implementable without propagating these random
fields, define fixed tensors \(M^\ell_{aq;jb}\), for panel indices
\(a,q\le3\) and training indices \(j,b\le2\). They are the pairing of the
coefficient of \(I_{jb}\) in the layer-\(\ell\) feature with sample \(q\)'s
initial feature. At the first layer their formula is

\[
M^1_{aq;jb}
=S_{aj}\sum_{c=1}^2 R_{jb,c}
\mathbb E[g(X_a)g(X_j)H_qH_c].
\tag{7}
\]

For the second layer set

\[
\begin{aligned}
\psi_{aq}(Z)&=g(Z_a)K_q,\\
U_{aq,d}&=\mathbb E[\partial_{Z_d}\psi_{aq}(Z)]\\
&=\mathbf1_{d=a}\mathbb E[T''(Z_a)K_q]
 +\mathbf1_{d=q}\mathbb E[g(Z_a)g(Z_q)].
\end{aligned}
\]

Then

\[
\begin{aligned}
M^2_{aq;jb}
={}&\left(C^{1,0}_{aj}
 +S_{aj}\mathbb E[g(X_a)g(X_j)]\right)
 \mathbb E[\psi_{aq}(Z)d_{jb}(Z)]\\
&+S_{aj}\sum_{c=1}^2\sum_{d=1}^3
 R_{jb,c}U_{aq,d}
 \mathbb E[g(X_a)g(X_j)H_cH_d].
\end{aligned}
\tag{8}
\]

These are two- and three-dimensional Gaussian integrals. The term with
\(C^{1,0}\) is middle-matrix learning. The next term is the correlated
forward/transpose Gaussian return. The final term is its reaction alignment.
They are exactly the ordered, label-independent coefficients obtained by
expanding equations (14)--(15) of ANALYTICAL_LEARNING_PROFILES.md before
contracting with the two label factors. No new return-law hypothesis has
been inserted.

For example, the lower feature displacement itself is

\[
h_{1,a}-H_a
\simeq\sum_{j,b\le2}I_{jb}S_{aj}g(X_a)g(X_j)B_{jb}.
\tag{9}
\]

The factor \(S_{aj}\) selects which training write reaches a passive input,
and both derivative gates select which neurons respond. Equations (7)--(8)
are the contractions of this displacement and its upper-layer propagation.

## Six evolving scalars, including the passive prediction

The quadratic approximation to either same-time feature Gram is

\[
C^\ell_{aq}(t,t)
\simeq C^{\ell,0}_{aq}
 +\sum_{j,b\le2}I_{jb}
       (M^\ell_{aq;jb}+M^\ell_{qa;jb}).
\tag{10}
\]

The top two-time Gram keeps the order of its two evaluations:

\[
C^2_{aq}(t,s)
\simeq C^{2,0}_{aq}
 +\sum_{j,b\le2}\left[I_{jb}(t)M^2_{aq;jb}
                         +I_{jb}(s)M^2_{qa;jb}\right].
\tag{11}
\]

Substitution into the exact readout integral gives the cubic output
functional

\[
\begin{aligned}
f_a(t)\simeq{}&\sum_{q\le2}C^{2,0}_{aq}u_q(t)
 +\sum_{q,j,b\le2}u_q(t)I_{jb}(t)M^2_{aq;jb}\\
&+\sum_{q,j,b\le2}M^2_{qa;jb}
                    \int_0^t c_q(s)I_{jb}(s)\,ds.
\end{aligned}
\tag{12}
\]

The last integral is a third-order memory. It cannot in general be
reconstructed from \(u\) and \(\mathcal A\) at the final time. Instead of
storing all eight ordered third integrals, evolve the three outputs directly.
Differentiating (12) gives the following closed approximation:

\[
\begin{aligned}
c_a&=y_a-f_a\quad(a=1,2),\\
\dot u_a&=c_a\quad(a=1,2),\\
\dot{\mathcal A}&=c_1u_2-c_2u_1,\\
\dot f_a&=\sum_{q=1}^2\mathcal K_{aq}(u,I)c_q\quad(a=1,2,3),
\end{aligned}
\tag{13}
\]

where \(I\) is reconstructed from (2) and

\[
\mathcal K_{aq}(u,I)
=C^{2,0}_{aq}
 +\sum_{j,b\le2}I_{jb}(M^2_{aq;jb}+M^2_{qa;jb})
 +\sum_{d,b\le2}u_du_bM^2_{ad;qb}.
\tag{14}
\]

All six state variables \((u_1,u_2,\mathcal A,f_1,f_2,f_3)\) start at zero.
There is no \(c_3\), and neither \(f_3\) nor a passive coefficient affects
the training subsystem. This is directly implementable by a six-dimensional
ODE solver and a one-time coefficient calculation. Fixed coefficient storage
is at most 36 numbers per \(M^\ell\), in addition to the initial Grams;
many entries vanish. Those stored numbers are separate from the six moving
coordinates. No learned inter-neuron matrix is evolved.

The \(I\)-weighted terms in (14) come from the changing same-time top
features. The last sum comes from moving the current query while it is paired
with the existing readout. Keeping only (10) as an evolving kernel would
miss that last term.

For an explicit passive formula use \(k_q=C^{2,0}_{3q}\) and

\[
\dot f_3=\sum_{q\le2}c_q\left[
k_q+\sum_{j,b\le2}I_{jb}(M^2_{3q;jb}+M^2_{q3;jb})
       +\sum_{d,b\le2}u_du_bM^2_{3d;qb}\right].
\tag{15}
\]

The unequal geometry enters (7)--(8) through
\(S_{31}=2/\sqrt5\) and \(S_{32}=1/\sqrt5\), as well as through the
initial Gaussian covariances. Formula (15) retains any signed-area
contraction instead of assuming a passive exchange symmetry that this
geometry does not have. Its value, including the possibility that a
particular contraction vanishes, is decided by those explicit integrals.

## The training equations simplify considerably

Define the positive constants

\[
\lambda=(\sigma^2+q_X)\tau+r_0^2\tau_X,
\qquad
\mu=(\sigma^2+q_X)\nu\beta+\sigma^2q_X\alpha^4.
\tag{16}
\]

On the training panel the only nonzero top tensor entries are

\[
M^2_{11;11}=M^2_{22;22}=\lambda,
\qquad
M^2_{12;12}=M^2_{21;21}=\mu.
\tag{17}
\]

To verify this, \(S_{aj}=\delta_{aj}\) and
\(C^{1,0}_{aj}=\sigma^2\delta_{aj}\) force \(j=a\). Independent symmetric
training roots then force \(b=q\). The self contraction has Gaussian part
\((\sigma^2+q_X)\tau\) and reaction part \(r_0^2\tau_X\); the cross
contraction has Gaussian part \((\sigma^2+q_X)\nu\beta\) and reaction part
\(\alpha^4q_X\sigma^2\).

Consequently

\[
\begin{aligned}
C^2_{11}&\simeq\nu+\lambda u_1^2,&
C^2_{22}&\simeq\nu+\lambda u_2^2,&
C^2_{12}&\simeq\mu u_1u_2,\\
C^1_{11}&\simeq\sigma^2+r_0\tau_Xu_1^2,&
C^1_{22}&\simeq\sigma^2+r_0\tau_Xu_2^2,&
C^1_{12}&\simeq\sigma^2q_X\alpha^2u_1u_2.
\end{aligned}
\tag{18}
\]

Their signed-area dependence cancels. The training kernel likewise reduces
to

\[
\mathcal K_{\mathrm{tr}}(u)=
\begin{pmatrix}
\nu+2\lambda u_1^2+\mu u_2^2&\mu u_1u_2\\
\mu u_1u_2&\nu+\mu u_1^2+2\lambda u_2^2
\end{pmatrix}.
\tag{19}
\]

Thus training needs only
\(\dot u=y-f\), \(\dot f=\mathcal K_{\mathrm{tr}}(u)(y-f)\),
with \(u,f\in\mathbb R^2\). The four-state training subsystem is autonomous.
Its kernel is symmetric and positive definite: the correction to \(\nu I\)
is \(2\lambda\operatorname{diag}(u_1^2,u_2^2)
+\mu(u_2,u_1)(u_2,u_1)^\top\). This is an algebraic consistency check of
the approximation, not an error guarantee for the source system.

## What the area records, and what a cubic potential omits

Area is present in the quadratic feature law. For example (9)
contains

\[
h_{1,1}-H_1
\simeq g(X_1)^2\left[
\tfrac12u_1^2B_{11}
+\tfrac12(u_1u_2+\mathcal A)B_{12}\right].
\tag{20}
\]

The coefficient of \(\mathcal A\) is nonzero:
\(B_{12}=\zeta_{12}+\alpha^2H_2\), with
\(\mathbb E\zeta_{12}^2=\beta\nu>0\). Writing sample 2 into the readout
before applying sample 1's hidden update differs from doing those operations
in the opposite order. A final vector \(u\) cannot record that ordering.

The cancellation in the training same-time Grams is therefore a cancellation
of observables, not disappearance of the memory. Even their two-time cross
Gram retains it:

\[
C^2_{12}(t,s)\simeq\mu[I_{12}(t)+I_{21}(s)]
=\frac\mu2\left[u_1(t)u_2(t)+u_1(s)u_2(s)
                  +\mathcal A(t)-\mathcal A(s)\right].
\tag{21}
\]

This is precisely the type of pairing the readout integral uses.

A natural two-coordinate alternative is the radial cubic formula

\[
F_a(u)=\nu u_a+\frac23\left(\lambda u_a^3
                         +\mu u_au_b^2\right),\qquad b\ne a,
\quad \dot u=y-F(u).
\tag{22}
\]

It is the gradient of
\(\nu|u|^2/2+\lambda(u_1^4+u_2^4)/6+\mu u_1^2u_2^2/3\).
Along a fixed ray it has the correct cubic output. In particular
\(u_2=su_1\), \(s=\pm1\), gives the audited symmetric coefficient
\(\kappa=2(\lambda+\mu)/3\).

However the controlled response (19) is not the Jacobian of any output map
depending on \(u\) alone:

\[
\partial_{u_2}\mathcal K_{11}=2\mu u_2
\ne\partial_{u_1}\mathcal K_{12}=\mu u_2.
\]

More precisely,

\[
\mathcal K_{\mathrm{tr}}(u)-DF(u)
=\frac\mu3
\begin{pmatrix}u_2\\-u_1\end{pmatrix}
\begin{pmatrix}u_2&-u_1\end{pmatrix},
\qquad
\frac d{dt}[f-F(u)]
=\frac\mu3\begin{pmatrix}u_2\\-u_1\end{pmatrix}
                         \dot{\mathcal A}.
\tag{23}
\]

The potential approximation captures motion along the accumulated deficit
and misses a positive transverse response when the deficit direction rotates.
The integrated correction depends on
\(\int u_2\,d\mathcal A\) and \(-\int u_1\,d\mathcal A\), not just the
final area. Thus adding one area scalar to an algebraic output map is not
in general sufficient either. Evolving the outputs in (13) stores the
required contractions of that third-order history without a larger tensor
of moving integrals.

This statement concerns general control paths, not a claim that the particular
fixed-label trajectory can make arbitrary loops. For fixed labels it identifies
exactly the term omitted by (22), which can be diagnosed within the predictive
closure itself.

### An algebraically equivalent five-state closure

Two scalar third-order histories suffice for every passive query:

\[
V_a(t)=\int_0^t c_a(s)\mathcal A(s)\,ds,\qquad a=1,2.
\]

Set \(\varepsilon_{12}=1\), \(\varepsilon_{21}=-1\), and
\(\varepsilon_{11}=\varepsilon_{22}=0\). Every third integral appearing in
(12) has the exact identity

\[
\begin{aligned}
\int_0^t c_q I_{jb}\,ds
={}&\frac{u_qu_ju_b}{6}
+\frac{\mathcal A}{6}
       (\varepsilon_{jb}u_q+2\varepsilon_{qj}u_b)\\
&+\frac13(\varepsilon_{jb}V_q-\varepsilon_{qj}V_b).
\end{aligned}
\tag{24}
\]

All quantities on the right are evaluated at \(t\). Differentiate the
right side using \(\dot u=c\), \(\dot V=c\mathcal A\), and (2); its
derivative is \(c_qI_{jb}\), and both sides start at zero. This verifies
the identity without an additional closure assumption.

For training, integrating (23) gives the particularly simple reconstruction

\[
f_1=F_1(u)+\frac\mu3(u_2\mathcal A-V_2),\qquad
f_2=F_2(u)+\frac\mu3(-u_1\mathcal A+V_1).
\tag{25}
\]

Here and in the remainder of this subsection, equality means equality
inside the defined truncated model. Reconstruct \(f_3\) by (12), replacing
its integrals with (24). Evolve only

\[
\dot u_a=y_a-f_a,\qquad
\dot{\mathcal A}=(y_1-f_1)u_2-(y_2-f_2)u_1,\qquad
\dot V_a=(y_a-f_a)\mathcal A,
\tag{26}
\]

with five zero initial coordinates \((u_1,u_2,\mathcal A,V_1,V_2)\).
Equations (24)--(26), together with the initial coefficients (3)--(8),
are the smaller closed implementation. Additional passive queries add
fixed coefficient rows but no evolving state. The six-state version
(13) avoids the reconstruction identity and is often easier to code;
the two versions implement exactly the same cubic control functional.

For completeness, the third histories cannot generally be discarded.
The concatenated control path in the \(u\)-plane

\[
(0,0)\to(1,0)\to(1,1)\to(0,1)\to(0,0)
\to(-1,0)\to(-1,1)\to(0,1)\to(0,0)
\]

ends with \(u=0\), \(\mathcal A=0\), but \((V_1,V_2)=(3,0)\).
Equation (25) then gives \(f=(0,\mu)\), whereas the stationary path gives
zero. Scaling both rectangles scales this cubic discrepancy by the cube
of their size. This is an obstruction for controlled response functions,
not a proposed trajectory of the fixed-label training problem.

## Why the smaller potential remains a valid small-label approximation

Write \(y=Y(1,-1/2)\), with the requested example at \(Y=0.6\).
Since the initial training Gram is \(\nu I\), on a regular finite-time
small-label branch

\[
c_a=Y\ell_a e^{-\nu t}+O(Y^3),\qquad
u_a=Y\ell_a\frac{1-e^{-\nu t}}\nu+O(Y^3),
\qquad \ell=(1,-1/2).
\tag{27}
\]

The degree-two term in \(\dot{\mathcal A}\) cancels. Therefore

\[
\mathcal A=O(Y^4),\qquad f-F(u)=O(Y^5)
\tag{28}
\]

on the same fixed finite time interval. Consequently no area variable is
required to obtain the correct quadratic-in-label features and cubic-in-label
predictions for this constant-label example. Unequal labels alone do not
justify claiming an order-\(Y^2\) area effect. At the requested moderate
amplitude, (13) and (22) are different testable resumptions of the same
low-order label expansion; neither has a certified error there.

The passive counterpart of the smaller two-state model is also explicit.
Define the homogeneous cubic polynomial

\[
P_a(u)=\sum_{q,j,b\le2}u_qu_ju_b
          \left(\tfrac12M^2_{aq;jb}+\tfrac16M^2_{qa;jb}\right).
\tag{29}
\]

Then use (22) for training and

\[
f_3\simeq k_1u_1+k_2u_2+P_3(u),\qquad
C^\ell_{aq}\simeq C^{\ell,0}_{aq}
 +\tfrac12\sum_{j,b\le2}u_ju_b
             (M^\ell_{aq;jb}+M^\ell_{qa;jb}).
\tag{30}
\]

For training, \(P_a=F_a-\nu u_a\). The unequal factors \(1/2\) and
\(1/6\) in (29) respectively describe the moving current query and the
earlier feature written to the readout. They must not be replaced by a
single symmetric coefficient. Equations (29)--(30) reproduce the source's
finite-time cubic passive expansion after residual feedback is included.

The useful comparison is therefore concrete: the two-state potential model
tests the radial small-label mechanism, while the five-state closure retains
the first ordered-write and transverse-response corrections during nonlinear
residual evolution. Both are initialized from (3)--(8); their predictions
require no future trajectory data. The larger model still omits the other
fourth-degree hidden and fifth-degree output terms, so retaining these memory
effects does not make it a complete fifth-order approximation.

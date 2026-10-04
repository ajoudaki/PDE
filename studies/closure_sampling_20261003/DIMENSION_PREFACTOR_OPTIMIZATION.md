# Anisotropic source radii and weighted-degree truncation

2026-10-04. Scoped source-representation derivation in the existing study.
This is an internal proof refinement, conditional on the inherited local
insertion and real-fitting interfaces. It is not a promotion review.
The supervisor proposed separate time/angle radii and a weighted-degree
index set. The proof below reconstructs that proposal; no new label-route
or runtime-route findings were used before this document was completed.
No experiment, trained-trajectory query, Git operation, or maintained-file
edit was made.

Provenance of the first freeze: the complete main text was written before
the supervisor's subsequent messages reporting other routes' proposed
label and runtime constants arrived. Those numerical conclusions were
then visible before the final notation audit and hash. They were not used
in this source proof, and no new proof file from either route was opened.
This parent-proposed derivation is not a blind independent attempt.

Complete scientific inputs read: EXPLICIT_SOURCE_CONSTANTS_ROUTE.md,
including its reconciled Section 7; DEPTH_INDEPENDENT_EXPONENT.md and
DEPTH_INDEPENDENT_EXPONENT_CHECK.md; GENERAL_ANALYTIC_COMPRESSION.md;
and the exact current-study dependencies DEEP_COMPLEX_SOURCE.md,
DEEP_ACTIVATION_EXTENSION.md, and TWO_INPUT_STABLE_GEOMETRY.md.
Prior-study sources linked by those inputs were not opened.

The construction improves the source-space estimate to
\[
 R\le \beta^{36Ld}\frac{(d+3)^{3d/2-1}}{d!}\,
       \lambda^{-1}\ell_n^{3d/2+1},\qquad \ell_n=\log(en),
 \tag{1}
\]
for every fixed integer dimension \(d\ge1\), at sufficiently large width.
In particular the supervisor's proposed exponent \(52Ld\) is valid with
slack. Every retained coefficient is obtained from finitely many initial
time derivatives, and paired initialized matrix actions remain exact.
The approximation tolerance stays \(n^{-1}\). The dense reference,
whole-sphere domain, physical time, and all-time root-width output norm
are unchanged. The squared dimension factor supplied to the inherited
quadratic runtime is \((d+3)^{3d-2}/(d!)^2\), which admits an
activation-only exponential times \((d+3)^d\) as a coarse envelope.

## 1. Model and inherited quantitative source inputs

Fix hidden depth \(L\ge2\), sample count \(m\), and unit training
vectors \(v_a\in S^{d-1}\). The canonical width-\(n\) network is
\[
 z^{(1)}(v)=Av,\qquad
 z^{(j)}(v)=W^{(j)}h^{(j-1)}(v),\qquad
 h^{(j)}(v)=\phi_j(z^{(j)}(v)),\qquad
 f_n(v)=w^\top h^{(L)}(v)/n.
 \tag{2}
\]
The middle recurrence is for \(j\ge2\). Initialization has independent
standard Gaussian entries in \(A_0\), independent \(N(0,1/n)\)
entries in the hidden matrices, and \(w_0=0\). With
\(r_a=f_n(v_a)-y_a\), define
\[
 k_a^{(L)}=w,\qquad
 \delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot k_a^{(j)},\qquad
 k_a^{(j)}=W^{(j+1)\top}\delta_a^{(j+1)}.
\]
The loss is \(m^{-1}\sum_a r_a^2\), the mobilities are
\((n,1,\ldots,1,n)\), and physical-time training is
\[
 \dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,
 \quad
 \dot W^{(j)}=-\frac2{mn}\sum_a r_a\delta_a^{(j)}
                                      h_a^{(j-1)\top},
 \quad
 \dot w=-\frac2m\sum_a r_a h_a^{(L)}.
 \tag{3}
\]

Assume each activation is real on the real axis, holomorphic on
\(|\Im z|<a\), and bounded there by \(B_\phi\). Use precisely the
reconciled constants
\[
 B=\max(1,B_\phi),\quad s=\max(1,4B/a),\quad
 t_\phi=\max(1,32B/a^2),\quad
 \beta=\max(10,B,s,t_\phi,16/a).
 \tag{4}
\]
Here \(t_\phi\) is the constant called \(t\) in equation (24) of
EXPLICIT_SOURCE_CONSTANTS_ROUTE.md; physical time remains \(t\).
Let \(\gamma>0\) be the initialized limiting top-feature Gram gap and
put
\[
 \lambda=\min(1,\gamma/m),\quad Y=\|y\|_2/\sqrt m,\quad
 S=16Y/\lambda,\quad T=32\lambda^{-1}\ell_n.
 \tag{5}
\]
Keep the source input's actual label restriction and stopped physical
tube. In particular \(S\le1\), \(Y\le1\), complex residual RMS is
at most \(2Y\), the real fitting rate is at least \(\lambda/4\),
and all real-plus-short-complex contours have activity at most \(S\).
The initialized/real/complex hidden-operator caps are \(8,9,10\).

The explicitly defined response constants \(U_*\) and \(V_*\)
from equations (14), (30)--(31) of that source satisfy, on its stopped
domains,
\[
 \max_{a,j,i}|R_{a,i}^{(j)}|\le U_*S\sqrt{\ell_n},\qquad
 \max_{q,j,i}|\partial_{\theta_q}z_i^{(j)}|
                                  \le V_*\sqrt{\ell_n},
 \qquad U_*,V_*\le\beta^{30L}\sqrt{d+3}.
 \tag{6}
\]
Here \(R_a^{(j)}=D_\Theta z^{(j)}\nabla_\Theta(nf_n(v_a))\),
with \(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\).
Thus \(R_a\) is a residual-free response, and
\(\dot z^{(j)}=-(2/m)\sum_a r_aR_a^{(j)}\).
The four whole-query source families are
\[
 h^{(j)}(t,v),\quad W_0^{(j)}h^{(j-1)}(t,v),\quad
 \delta^{(j)}(t,v),\quad
 W_0^{(j+1)\top}\delta^{(j+1)}(t,v),
 \tag{7}
\]
with their natural layer ranges. The passive-query backward recursion in
(7) uses the actual current parameters and adds no training force.
Their sufficient coordinate magnitude bound is
\(M_n=M_0\sqrt n\), with \(M_0\le\beta^{4L}\).

## 2. Different time and angular radii satisfy the same source proof

For \(d\ge2\), set
\[
 c_t=\min\{1/8,a/(512U_*)\},\qquad
 c_a=\min\{1/(8d),a/[128(d-1)V_*]\},
 \qquad r_t=c_t/\sqrt{\ell_n},\quad r_\theta=c_a/\sqrt{\ell_n}.
 \tag{8}
\]
Use the time rectangle
\(-r_t\le\Re t\le T+r_t\), \(|\Im t|\le r_t\), and
\(|\Im\theta_q|\le r_\theta\) for all \(d-1\) periodic sphere angles.
For \(d=1\), retain \(c_t,r_t\), omit \(c_a,r_\theta\), and use both
queries \(v=-1,+1\).

The sphere parameterization is a product of plane rotations, hence
\(\|v(\theta)\|_2\) and each first or second angular derivative
are bounded by \(\exp(\sum_q|\Im\theta_q|)\le e^{1/8}<2\).
These are the same geometric bounds used to derive (6).
From (3) and complex residual RMS at most \(2Y\),
\[
 \max|\partial_tz^{(j)}|\le4YU_*S\sqrt{\ell_n}.
\]
Anchor the complex time at its nearest point in \([0,T]\), move first
along the real direction if necessary and then vertically; the two short
segments have total length at most \(2r_t\). Then change each angle
vertically. The absolute preactivation displacement from the real
anchor is at most
\[
 8c_tYSU_*+(d-1)c_aV_*
 \le a/64+a/128=3a/128<a/32.
 \tag{9}
\]
For \(d=1\) only the first term occurs. This retains a strict pole
margin even with both short time pieces explicitly counted.

To justify the enlarged domain, repeat the stopped-domain proof, rather
than claiming that it is a subset of the previous equal-radius domain.
Scale \(r_t\) and \(r_\theta\) by one common continuation parameter.
Every local insertion control still lives on a one-dimensional time
contour. Its short non-real/backwards length is at most \(2r_t\),
so the product of negative-Gram base propagators costs
\(\exp(Cr_t)=1+o(1)\). The same control nets and augmented Taylor
remainders retain their strict powers of \(n\). The query grid still
has \(2d\) real coordinates and the same polynomial cardinality;
the constants in (6) use only the displayed geometric bound of two.
Changing fixed side lengths affects net prefactors, not their powers.

Training carriers depend only on time. Their deterministic interpolated
derivative estimate remains
\[
 \|\dot\delta_a^{(j)}\|_2/\sqrt n
 \le C\rho[1+S^2\log(e+\ell_n)].
\]
Consequently their normalized short-complex-contour correction is still
at most \(C r_t\log(e+\ell_n)\). Its Gaussian supremum bound is
\(O(\ell_n^{-1/2}[\log(e+\ell_n)]^{3/2})=o(1)\), with the
same fixed-exponent moment argument. Angular width never enters this
training-carrier moment calculation. All cavity pole/response comparisons
use the same coordinate-small insertion errors. Thus the original order
of removing the carrier maximum, response, pole, and budget stops works,
using (9) at the pole step. It introduces no new persistent small-label
condition. The resulting high-probability event supplies joint
holomorphy of (7), with magnitude \(M_n\), on a neighborhood of this
anisotropic closed domain.

The explicit inverse-radius estimates are
\[
 c_t^{-1}\le\beta^{32L}(d+3)^{1/2},\qquad
 c_a^{-1}\le\beta^{32L}(d+3)^{3/2}.
 \tag{10}
\]
Indeed \(a^{-1}\le\beta/16\) makes the nongeometric terms at most
\(32\beta^{30L+1}\sqrt{d+3}\) and
\(8\beta^{30L+1}(d-1)\sqrt{d+3}\), respectively. Since
\(L\ge2\), \(\beta\ge10\), these and the caps \(8,8d\) are
bounded by (10). In particular
\[
 c_t^{-1}c_a^{-(d-1)}
 \le\beta^{32Ld}(d+3)^{3d/2-1}.
 \tag{11}
\]
The time factor has only one square root of dimension; it no longer
pays for the sum of all angular displacements.

## 3. Weighted-degree Fourier truncation

For any coordinate \(g(t,\theta)\) of a source (7), define the
transformed source \(G(u,\theta)=g(T(1+\cos u)/2,\theta)\) and put
\[
 \alpha=\frac{r_t}{4T}
       =\frac{c_t\lambda}{128\ell_n^{3/2}},
 \qquad r=r_\theta.
 \tag{12}
\]
For \(|\Im u|\le\alpha\), the imaginary part of the mapped time
is at most \((T/2)\sinh\alpha\le T\alpha=r_t/4\).
Its real excursion beyond \([0,T]\) is at most
\((T/2)(\cosh\alpha-1)\le T\alpha^2/2\le r_t\).
Thus the transformed source is holomorphic, bounded by \(M_n\),
periodic in all \(d\) variables, and even in \(u\). Contour
translation in each variable yields Fourier coefficients satisfying
\[
 |\widehat G(k_0,k')|
 \le M_n\exp[-\alpha|k_0|-r\|k'\|_1],
 \qquad (k_0,k')\in\mathbb Z\times\mathbb Z^{d-1}.
 \tag{13}
\]
For \(d=1\), use the same formula without \(k'\) and \(r\).

Put \(\epsilon=n^{-1}\) and define
\[
 P=\frac{6^d}{\alpha r^{d-1}},\qquad
 H=2\log\frac{16M_nP}{\epsilon},\qquad
 \Lambda=\{(k_0,k'):\alpha|k_0|+r\|k'\|_1\le H\}.
 \tag{14}
\]
Missing angular factors in this and subsequent formulas are one when
\(d=1\). For \(0<b\le1\),
\(\sum_{k\in\mathbb Z}e^{-b|k|}=1+2/(e^b-1)\le3/b\).
Split each omitted exponential into two equal factors. Equations
(13)--(14) then give the full coefficient tail
\[
 \sum_{k\notin\Lambda}|\widehat G(k)|
 \le M_ne^{-H/2}\sum_{k\in\mathbb Z^d}
       e^{-(\alpha|k_0|+r\|k'\|_1)/2}
 \le M_ne^{-H/2}P=\epsilon/16.
 \tag{15}
\]
This bounds uniform coordinate error on the entire real time/sphere
domain, without a measure or an average over queries.

Evenness in \(u\) converts nonnegative temporal modes to cosines,
or equivalently to Chebyshev polynomials in \(2t/T-1\). Define
\[
 N=\#\{(j_0,j')\in\mathbb Z_{\ge0}\times\mathbb Z^{d-1}:
                        \alpha j_0+r\|j'\|_1\le H\}.
\]
There are exactly at most \(N\) real coefficient vectors: for each
\(j_0\), the symmetric angular set has one real constant and two
real sine/cosine coefficients per nonzero pair \(j',-j'\).
The temporal cosine coefficient absorbs both signed temporal modes.

For the count, first replace each angular integer by its absolute value.
This gives at most \(2^{d-1}\) sign choices per nonnegative lattice
point. The disjoint unit cubes based at these nonnegative lattice points
lie in the simplex with weighted radius
\(H+\alpha+(d-1)r\). Its volume, by the substitutions
\(y_0=\alpha x_0\), \(y_q=rx_q\), is
\((H+\alpha+(d-1)r)^d/(d!\alpha r^{d-1})\). Hence
\[
 N\le\frac{2^{d-1}[H+\alpha+(d-1)r]^d}
                    {d!\alpha r^{d-1}}.
 \tag{16}
\]
This is where the factorial gain enters. No tensor-box coefficient count
is retained.

The logarithm in (14) is completely explicit:
\[
 H=2\left\{\tfrac32\log n+
 \log\bigl(2048M_0\,6^d\lambda^{-1}
                         c_t^{-1}c_a^{-(d-1)}\bigr)
                 +\tfrac{d+2}{2}\log\ell_n\right\}.
 \tag{17}
\]
At fixed data, increase the width threshold until the second and third
terms inside braces are each at most \(\ell_n\). Then \(H\le7\ell_n\).
Moreover \(\alpha+(d-1)r<1/4\) by (8) and (12), independently of
dimension. Using the loose bound \(H+\alpha+(d-1)r\le9\ell_n\)
in (16) proves
\[
 N\le64\,18^d\,
       \frac{c_t^{-1}c_a^{-(d-1)}}{d!}\,
                 \lambda^{-1}\ell_n^{3d/2+1}.
 \tag{18}
\]
Both the logarithmic conditions in (17) and the retained inverse-radius
factors are visible. No polynomial or exponential dimension factor in
(18) has been discarded into the width threshold.

## 4. Finite initial jets and exact paired actions

The Fourier coefficients in (13) are used for an error estimate, not as
an oracle for trained values. Choose a finite tensor sampling grid with
odd sizes \(2p+1\), \(2J+1\) in time angle and each sphere angle,
where \(p=\lceil H/\alpha\rceil\), \(J=\lceil H/r\rceil\).
Apply its normalized discrete Fourier transform and retain only
\(\Lambda\). Distinct indices in \(\Lambda\) have distinct grid
residues, since the grid's entire frequency box contains \(\Lambda\).
For exact source nodal values, every alias contributing to a retained
coefficient comes from outside that box, hence outside \(\Lambda\).
The total alias error is therefore at most the tail (15). Evenness and
reality of the nodal array persist under the transform and the symmetric
restriction to \(\Lambda\). The retained array consequently has at
most the \(N\) real coefficient vectors just counted. The tensor grid
is temporary preprocessing workspace only.

For completeness, all nodal values can be computed to arbitrary accuracy
from finitely many initial time derivatives by the following map. Put
\[
 q=\frac{\pi T}{8r_t},\quad b_0=\tanh q,\quad
 b_1=\tanh(q+\pi/4),\quad \eta=b_0/b_1,\quad
 \psi(\xi)=\frac{\xi-\eta}{1-\eta\xi},
\]
\[
 z(\xi)=\frac T2+\frac{2r_t}{\pi}
                \log\frac{1+b_1\psi(\xi)}{1-b_1\psi(\xi)}.
 \tag{19}
\]
The disk automorphism \(\psi\) and the analytic logarithm map the
unit disk into the time rectangle, and \(z(0)=0\). The inverse maps
\([0,T]\) into \([0,\xi_*]\), where
\(\xi_*=2\eta/(1+\eta^2)<1\). For each fixed grid angle \(\theta\),
the Taylor coefficients of the composed source are
\[
 A_j(\theta)=\sum_{k=0}^j
       \frac{\partial_t^kg(0,\theta)}{k!}
                                    [\xi^j]z(\xi)^k.
 \tag{20}
\]
Here \(g(t,\theta)\) is the original source coordinate, before
the cosine substitution. Its derivative values are obtained by finite
formal differentiation of (3), using initialized parameters and labels.
Cauchy's coefficient estimate is \(|A_j|\le M_n\). Writing
\(d_*=1-\xi_*>0\), a degree-\(K\) Taylor sum has nodal error at most
\[
 M_n\xi_*^{K+1}/d_*
                 \le M_ne^{-d_*(K+1)}/d_*.
\]
Take this below \(\delta=\epsilon/(32N)\) by choosing any finite
\(K+1\ge d_*^{-1}\log[M_n/(d_*\delta)]\). A normalized DFT changes
each coefficient by at most \(\delta\). Since
\(|\Lambda|\le2N\), the total reconstruction error from inexact
nodes is at most \(2N\delta=\epsilon/16\). Together with (15) and
the alias bound, the error is at most \(3\epsilon/16<\epsilon\).
The same \(K\), grid, and linear coefficient operations can be used
for all sources and all coordinates.

For an initialized matrix \(W_0\), every initial derivative of its
image is exactly \(\partial_t^k(W_0g)=W_0\partial_t^kg\).
Equations (19)--(20), the DFT, the selection of \(\Lambda\), and
the conversion to real coefficients are all fixed scalar linear
operations. Applying identical operations therefore gives exact pairs
\(u,W_0u\), or \(v,W_0^\top v\), at the retained coefficient level.
Each member independently has the coordinate approximation estimate
just proved. No operator-norm conversion of one member's coordinate
error is used. All initial derivatives, tensor-grid values, discarded
coefficients, and original-width work arrays are discarded after setup.

## 5. Layer dimension and consequences for retained storage

At each layer, span the real coefficients of the four sources (7), add
the exact initialized training features and their initialized forward
images, add the constant vector, and at the first layer add the \(d\)
columns of \(A_0\). For \(d\ge2\) this gives
\[
 R\le4N+2m+d+1.
 \tag{21}
\]
For \(d=1\), use both time-only query families, giving instead
\(R\le8N+2m+2\). The universal upper bound
\(8N+2m+d+1\) is valid in both cases. This accounts for the two
points of \(S^0\) explicitly.

Define, only to simplify the count in this paragraph,
\(F_d=(d+3)^{3d/2-1}/d!\). For \(d\ge2\),
\(d!\le(d+3)^{d-1}\) gives \(F_d\ge(d+3)^{d/2}\ge d+3\);
also \(F_1=2\). The exact Gram trace constraint
\(m\lambda\le B^2\) therefore bounds the additions in (21) by
\(3\beta^2F_d\lambda^{-1}\ell_n^{3d/2+1}\).
Equations (11), (18), and (21) now give
\[
 R\le\left[512\,18^d\beta^{32Ld}+3\beta^2\right]
             F_d\lambda^{-1}\ell_n^{3d/2+1}.
 \tag{22}
\]
Since \(512\,18^d\le9216^d\le10^{4d}\le\beta^{2Ld}\)
and \(3\beta^2\le\beta^{2Ld}\), the bracket is at most
\(2\beta^{34Ld}\le\beta^{35Ld}\), and the slightly looser
\(\beta^{36Ld}\) proves (1). All constants are explicit expressions
or bounds inherited from the named reconciled source; no opaque
depth-dependent constant has been assigned an exponential envelope.

Squaring the actual source bound supplies
\[
 R^2\le\beta^{72Ld}
      \frac{(d+3)^{3d-2}}{(d!)^2}
             \lambda^{-2}\ell_n^{3d+2}.
 \tag{23}
\]
For a simpler dimension dependence, integrate \(\log x\) over
\([1,d]\) to obtain \(d!\ge(d/e)^d\). Thus
\[
 \frac{(d+3)^{3d-2}}{(d!)^2}
 \le e^{2d}(1+3/d)^{2d}(d+3)^{d-2}
 \le e^{2d+6}(d+3)^{d-2}
 \le\beta^{2Ld}(d+3)^d.
 \tag{24}
\]
The last step uses \(e^{2d+6}\le e^{8d}\le10^{4d}\le\beta^{2Ld}\).
Consequently \(R^2\le\beta^{74Ld}(d+3)^d
\lambda^{-2}\ell_n^{3d+2}\).

These are source and source-square bounds. Every fixed metric, dense
learned matrix, first-weight array, label, training input, and moving
auxiliary array required by the existing corrected-readout runtime must
still be counted by that runtime's explicit inventory. This note makes
no new runtime reduction and does not replace its coefficient by one.
In particular the older quartic-storage weighted model in
GENERAL_ANALYTIC_COMPRESSION.md is not being substituted for the
quadratic corrected-readout interface inherited by
DEPTH_INDEPENDENT_EXPONENT.md.

The latter interface uses precisely the coordinate source tolerance,
exact paired actions, initial-feature additions, and finite initial-jet
provenance established above. It therefore receives the same hypotheses
at the smaller \(R\). Its own-residual optimizer, trained hidden
matrices, physical clock, and all-time whole-sphere root-width comparison
transfer unchanged. Its stability amplification is still a fixed-data
multiple of \(n^{-1}\exp(C\sqrt{\ell_n})\), eventually at most a
fixed-data multiple of \(n^{-1/2}\); both physical fitting tails use
the same horizon (5). No trained dense trajectory becomes a runtime
input.

The width threshold remains unquantified for the inherited stochastic
source theorem. Additional thresholds here are only the explicit fixed
logarithmic conditions in (17). The factorial improvement is an actual
coefficient-count improvement, and (11) retains the actual dimension cost
of the pole barrier. This is a fixed-dimension, fixed-depth theorem;
it proves neither optimal dimension dependence nor efficient or
bounded-precision preprocessing.

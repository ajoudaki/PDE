<!-- Integration provenance (scientific imports only):
Setup-S: POLYNOMIAL_SETUP_ODE_ROUTE.md, "Deterministic setup" through
  the end of the polynomial-accuracy argument; excludes global coefficient solve.
Setup-Q: POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md, sections 1--6 through
  geometry/basis costs (30)--(31), plus section 7; excludes value-oracle
  accounting and the obsolete remaining-gap paragraph.
Setup-C: LOCAL_CONTINUATION_SETUP.md, sections 1--6; generic derivative-oracle
  cost section is replaced by the real-value activation backend.
Setup-A: LOCAL_ACTIVATION_BACKEND.md, complete scientific sections.
Setup-E: LOCAL_CONTINUATION_ASSEMBLY.md, scientific sections 1--5.
Setup-B: LOCAL_TAYLOR_ASSEMBLY_BRIDGE.md, all scientific sections.
Setup-G: IMPLICIT_GAUSSIAN_SAMPLER.md, all scientific sections.
Setup-I: IMPLICIT_HARMONIC_EXECUTION.md, scientific sections 1--7.
Orders: IMPLICIT_SETUP_ORDERS.md, scientific sections 1--9; its repeated source,
  fitting and inherited-gate recurrences are replaced by exact internal
  references and notation correspondences to the existing RESULT proofs.
No scientific input is taken from another study. Component equation tags and
prose references are namespaced; spherical cutoff J is renamed ell_* in Setup-Q.
Workflow/status metadata and unused routes are not part of these imports.
-->
<a id="harmonic-efficient-setup-proofs"></a>
<a id="efficient-setup-proofs"></a>
### Proofs of the efficient Harmonic initializers

The explicit initializer constructs source coefficients by certified local
continuation through the full source horizon. The implicit initializer executes
that same finite calculation through exact adaptive Gaussian actions. The
argument proceeds from signed defect stability and positive quadrature to
local numerical continuation, activation replacement, source assembly, and
finally the joint-law coupling and its operation count. The legacy
[initialization-jet construction](#harmonic-initial-jet-proof) remains a
separate valid alternative.

All notation referring to the dense model retains its original meaning:
\(A=W^{(1)}\), \(w=W^{(L+1)}\), \(v=x/\sqrt d\), and
\(\phi_j=\phi^{(j)}\). The parameter vector
\(\theta=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)\)
uses ordinary Euclidean/Frobenius norms and the original mean-square loss and
mobilities. This is the normalized coordinate form of the same dense flow.
The positive-label analytic branch has \(L\ge2\), \(Y>0\),
\(T\ge32(m/\gamma)\log(en)\), and
\(0<\eta\le\min(1,Y,16Ym/\gamma)\), with the full original label and
width/source qualifications. Zero labels and full-width retention keep their
separate definitions.

Each proof component scopes its auxiliary coefficient names locally. In the
quadrature component, \(a=\alpha_T/2\) is the temporal angular strip radius
and \(\ell_*\) the largest spherical degree; the continuation components use \(a\)
for the original activation strip width, and the assembly/execution components
use \(J\) for the number of time panels and \(\ell_*\) for spherical degree.
Their exact correspondence to the single order interface is given in
[the deterministic prescription](#setup-orders). In the sampler component,
\(Y,R,U,V,p,q\) are stored matrices and query-span dimensions, not network
labels, source budgets or selected widths.

The source recurrences, source event, source expansion, exact selector and
runtime comparison are proved elsewhere in this same document. Every new
deterministic and probabilistic execution argument needed for the two
initializers is included below. No source-event test or new failure allowance
is introduced. Exact joint-law equality refers to the explicit local finite
initializer with the same scalar routines and deterministic conventions; it
does not assert equality with the alternative origin-jet coefficient program.

<a id="setup-stability"></a>
#### Signed defect stability

<a id="setup-stability-1"></a>
##### Deterministic setup

Let \(v=x/\sqrt d\), so \(\|v\|_2=1\), and retain the dense network

\[
z^{(1)}=Av,\qquad z^{(j)}=W^{(j)}h^{(j-1)},\qquad
h^{(j)}=\phi_j(z^{(j)}),\qquad f_n=w^Th^{(L)}/n.
\]

Its parameter coordinates with Euclidean mobility metric are

\[
\theta=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n).
\]

Write \(r_a=f_n(v_a)-y_a\), \(\rho=\|r\|_2/\sqrt m\),
\(Y=\|y\|_2/\sqrt m\), and \(\lambda=\gamma/m\). With
\(\xi_a(\theta)=\nabla_\theta f_n(v_a)\), the exact vector field is

<a id="eq-setup-s-1"></a>
\[
F(\theta)=-\frac2m\sum_{a=1}^m r_a\xi_a(\theta),\qquad
\dot\theta=F(\theta).
\tag{Setup-S.1}
\]

The initial readout is zero. All blocks train with the loss and mobilities of
[the preceding Harmonic construction](#harmonic-construction); no frozen-feature model replaces [(Setup-S.1)](#eq-setup-s-1).

Condition on the existing real-fitting and source event, including the stated
analytic-extension gates when all-time carrier control is used. The complete
original common label allowance is unchanged. The imported deterministic
conclusions needed here are

\[
\|A(t)\|_{\rm op}/\sqrt n<9,\qquad
\|W^{(j)}(t)\|_{\rm op}<9,\qquad
\|w(t)\|_2/\sqrt n\le 2Y/\sqrt\lambda,
\]
\[
\rho(t)\le Ye^{-\lambda t/2},\qquad
\int_0^\infty\rho(t)\,dt\le 2Y/\lambda,
\]
<a id="eq-setup-s-2"></a>
\[
\max_{a,j,i,t\ge0}|k_{a,i}^{(j)}(t)|\le M_n,
\qquad M_n=2K_{\rm src}S\sqrt{\log(en)},\qquad S=16Y/\lambda.
\tag{Setup-S.2}
\]

Here \(k^{(L)}=w\) and
\(k^{(j)}=(W^{(j+1)})^T\delta^{(j+1)}\), with
\(\delta^{(j)}=\phi_j'(z^{(j)})\odot k^{(j)}\).
The carrier maximum in [(Setup-S.2)](#eq-setup-s-2) concerns only the true training trajectory. No
carrier maximum for perturbed trajectories or parameter segments is assumed.

Take \(b=\max_j|\phi_j(0)|\), and let \(s\ge1\), \(t_2\ge1\)
bound the first and second activation derivatives on the safe strip, as in the
source recurrences. Define explicit deterministic coefficients

\[
H_1=\max(1,b+10s),\qquad H_j=\max(1,b+10sH_{j-1}),\qquad H=H_L,
\]
\[
R=1+2Y/\sqrt\lambda,\quad B=Rs(10s)^{L-1},\quad
F_z=H(10s)^{L-1},\quad P_{\rm layer}=1+(L-1)H,\quad
G=H+P_{\rm layer}B,
\]
\[
D(M)=(10s)^{L-1}\{s(1+B)+Lt_2F_zM\},
\]
\[
J(M)=\sqrt{L+1}\{P_{\rm layer}D(M)+[1+(L-1)B]sF_z\},
\]
<a id="eq-setup-s-3"></a>
\[
C(M)=sF_z\sqrt L+LBsF_z+\frac12L^2t_2F_z^2M.
\tag{Setup-S.3}
\]

These constants expose dependence on depth, activation bounds and
\(Y/\sqrt\lambda\); \(\lambda=\gamma/m\) exposes the sample/gap
dependence. The parameter norm and these bounds are independent of input
dimension once the input norm is one. The original source event still has its
stated problem-dependent eventual-width qualification.

Every real state \(u\) within Euclidean distance one of \(\theta(t)\)
has mixer and normalized first-matrix operator caps ten and readout RMS at most
\(R\). Linear activation growth therefore gives feature RMS at most \(H\)
on the entire input sphere. These statements do not require bounded activation
values.

<a id="setup-stability-2"></a>
##### Endpoint estimates with only one controlled carrier endpoint

Let \(e=u-\theta\), \(E=\|e\|_2\le1\), and let
\(D_h\) be the sum of the first normalized Frobenius discrepancy and
the hidden-matrix Frobenius discrepancies; let \(D_w\) be the readout
RMS discrepancy. Then
\(D_h\le\sqrt L E\) and \(D_h+D_w\le\sqrt{L+1}E\).
Forward subtraction through matrices with operator norm at most ten gives

<a id="eq-setup-s-4"></a>
\[
\sup_{v,j}\frac{\|z^{(j)}(u,v)-z^{(j)}(\theta,v)\|_2}{\sqrt n}
 \le F_zD_h,
\qquad
\sup_{v,j}\frac{\|h^{(j)}(u,v)-h^{(j)}(\theta,v)\|_2}{\sqrt n}
 \le sF_zD_h.
\tag{Setup-S.4}
\]

Indeed the first direct coefficient is one; every later direct coefficient is
at most \(H\), and each propagation contributes \(10s\). The sum of
the parameter block discrepancies is already in \(D_h\).

For a training sample, split the backward difference using the true carrier:

\[
\delta^{(j)}(u)-\delta^{(j)}(\theta)
=\phi_j'(z^{(j)}(u))\odot[k^{(j)}(u)-k^{(j)}(\theta)]
+[\phi_j'(z^{(j)}(u))-\phi_j'(z^{(j)}(\theta))]\odot k^{(j)}(\theta).
\]

The second term in RMS is bounded by \(t_2M_nF_zD_h\).
The first propagates with factor \(10s\), and changed mixers cost at
most \(sB\|\Delta W\|_F\). The top readout difference costs
\(sD_w\). Summing the resulting finite geometric recursion gives

\[
\frac{\|\delta_a^{(j)}(u)-\delta_a^{(j)}(\theta)\|_2}{\sqrt n}
\le D(M_n)(D_h+D_w).
\]

The exact gradient blocks are

\[
\xi_a=
\left(\frac{\delta_a^{(1)}v_a^T}{\sqrt n},
 \left(\frac{\delta_a^{(j)}h_a^{(j-1)T}}n\right)_{j=2}^L,
 \frac{h_a^{(L)}}{\sqrt n}\right).
\]

Bounding and subtracting these blocks gives

<a id="eq-setup-s-5"></a>
\[
\|\xi_a(u)\|_2,\|\xi_a(\theta)\|_2\le G,\qquad
\|\xi_a(u)-\xi_a(\theta)\|_2\le J(M_n)E.
\tag{Setup-S.5}
\]

There is also a Taylor remainder anchored at the true state:

<a id="eq-setup-s-6"></a>
\[
|f_n(u,v_a)-f_n(\theta,v_a)-\langle\xi_a(\theta),e\rangle|
\le C(M_n)E^2.
\tag{Setup-S.6}
\]

For completeness set \(\Delta h=h(u)-h(\theta)\),
\(\Delta z=z(u)-z(\theta)\), and
\(a^{(j)}=\Delta h^{(j)}-\phi_j'(z^{(j)}(\theta))\odot\Delta z^{(j)}\).
Scalar Taylor's formula gives
\(|a_i^{(j)}|\le t_2|\Delta z_i^{(j)}|^2/2\). Expanding the
network discrepancy by forward differentiation and then backward substitution
expresses its scalar remainder as

\[
\frac1n\sum_j k_a^{(j)}(\theta)^Ta_a^{(j)}
+\frac1n\sum_{j=2}^L\delta_a^{(j)}(\theta)^T
             \Delta W^{(j)}\Delta h_a^{(j-1)}
+\frac1n\Delta w^T\Delta h_a^{(L)}.
\]

The three absolute bounds are respectively
\(L^2t_2M_nF_z^2E^2/2\), \(LBsF_zE^2\), and
\(sF_z\sqrt L E^2\), proving [(Setup-S.6)](#eq-setup-s-6). No Hessian bound on an
uncontrolled interpolating state has been inserted.

<a id="setup-stability-3"></a>
##### Defect stability lemma

Let \(u:[0,T]\to\mathbb R^P\) be an absolutely continuous approximate
parameter path, where \(P=(L-1)n^2+n(d+1)\). Its additive ODE defect is

\[
d(t)=\dot u(t)-F(u(t)),\qquad
E_0=\|u(0)-\theta(0)\|_2+\int_0^T\|d(t)\|_2\,dt.
\]

Write \(J=J(M_n)\), \(C=C(M_n)\), and
\(A_n=4JY/\lambda\). Suppose

<a id="eq-setup-s-7"></a>
\[
E_0\le e^{-A_n}/4,\qquad
8(C+J)^2T e^{2A_n}E_0^2\le1.
\tag{Setup-S.7}
\]

Then

<a id="eq-setup-s-8"></a>
\[
\sup_{0\le t\le T}\|u(t)-\theta(t)\|_2\le 2e^{A_n}E_0.
\tag{Setup-S.8}
\]

**Proof.** Stop at discrepancy one. Put
\(e_{f,a}=f_n(u,v_a)-f_n(\theta,v_a)\), so the perturbed residual is
\(r_a+e_{f,a}\). The exact vector-field subtraction in [(Setup-S.1)](#eq-setup-s-1) gives

\[
\frac12\frac d{dt}E^2
=-\frac2m\sum_a e_{f,a}\langle e,\xi_a(\theta)\rangle
 -\frac2m\sum_a(r_a+e_{f,a})
                  \langle e,\xi_a(u)-\xi_a(\theta)\rangle
 +\langle e,d\rangle.
\]

Using [(Setup-S.5)](#eq-setup-s-5)--[(Setup-S.6)](#eq-setup-s-6) and the ordinary sample RMS gives

\[
\frac12\frac d{dt}E^2
\le-2\frac{\|e_f\|_2^2}{m}
 +2(C+J)\frac{\|e_f\|_2}{\sqrt m}E^2
 +2J\rho E^2+E\|d\|_2.
\]

Maximizing the first two terms over their nonnegative scalar argument bounds
them by \((C+J)^2E^4/2\). Consequently, in the upper-derivative sense,

<a id="eq-setup-s-9"></a>
\[
E'\le 2J\rho E+\frac12(C+J)^2E^3+\|d\|_2.
\tag{Setup-S.9}
\]

At zero discrepancy use \((E^2+\varepsilon^2)^{1/2}\) and pass to
zero \(\varepsilon\); all coefficients and the defect are integrable.
Let \(a(t)=2J\int_0^t\rho(s)\,ds\le A_n\) and
\(z(t)=e^{-a(t)}E(t)\). As long as \(z\le2E_0\), integration
of [(Setup-S.9)](#eq-setup-s-9) gives

\[
z(t)\le E_0+4(C+J)^2T e^{2A_n}E_0^3\le\frac32E_0.
\]

Thus a first crossing of \(2E_0\) is impossible. The first condition
in [(Setup-S.7)](#eq-setup-s-7) also keeps \(E\le1/2\), so the geometric stop cannot occur.
The case \(E_0=0\) follows by uniqueness or the same regularization.
This proves [(Setup-S.8)](#eq-setup-s-8).

At fixed admissible \(m,d,L,\gamma,Y\) and activations, [(Setup-S.3)](#eq-setup-s-3) is affine
in \(M_n\), hence

\[
A_n=a_0+a_1\sqrt{\log(en)}
\]

for explicitly defined nonnegative coefficients \(a_0,a_1\).
The amplification is therefore subpolynomial in width. Its exponent has no
factor \(T\): the training residual is integrable and the negative
prediction-error square was retained before estimating it.

This is a finite-horizon defect theorem. It does not assert that an arbitrary
perturbed flow fits labels, nor that a persistent nonzero defect is harmless
over an infinite horizon. The original Harmonic endpoint theorem is unchanged.

<a id="setup-stability-4"></a>
##### Polynomial precision for all source coordinates

The source families contain backward fields at every passive query. Their
carrier maxima are not supplied by [(Setup-S.2)](#eq-setup-s-2). A deterministic RMS-to-coordinate
conversion is sufficient for this precision estimate.

Set

\[
K_q=R(10s)^{L-1},\qquad
C_{\rm src}=8\sqrt{L+1}\max\left\{
sF_z,\ (10s)^{L-1}[s(1+B)+Lt_2F_zK_q]\right\}.
\]

Every query carrier has RMS at most \(K_q\), hence maximum at most
\(\sqrt nK_q\). Repeat the backward subtraction above with that
maximum. A final RMS-to-coordinate conversion and \(\sqrt n\le n\)
show that each feature or response family differs between \(u(t)\) and
\(\theta(t)\) in coordinate norm by at most \(C_{\rm src}nE(t)\).
The factor eight also includes its initialized forward/reverse image because
\(\|W_0\|_{\rm op}\le8\). Consequently source accuracy \(\eta\)
is guaranteed if, in addition to [(Setup-S.7)](#eq-setup-s-7),

<a id="eq-setup-s-10"></a>
\[
E_0\le \frac{\eta e^{-A_n}}{2C_{\rm src}n}.
\tag{Setup-S.10}
\]

For \(\eta=n^{-a}\), fixed \(a>0\), and
\(T=O((m/\gamma)\log n)\), the logarithm of the required inverse
defect tolerance is \(O(\log n+\sqrt{\log n})\), with the explicit
coefficients above. Thus polynomial precision suffices at the original
\(\eta=1/n\) specialization. This is a statement about the required
numerical tolerance, not the bit complexity of an activation evaluation or
the condition number of coordinate selection.

The source coefficient construction must still apply identical scalar linear
operations to both members of every initialized-mixer pair. Approximate ODE
solutions do not by themselves preserve that algebraic identity. Forming the
image from the computed base coefficient preserves it exactly in the same
exact-real operation model as [the preceding Harmonic construction](#harmonic-construction); finite precision needs its own
roundoff allowance.

<a id="setup-quadrature"></a>
#### Positive coefficient quadrature

<a id="setup-quadrature-1"></a>
##### Precise input and conclusion

Fix a permitted width and source event in [the preceding Harmonic construction](#harmonic-construction), a finite source horizon
\(T\ge T_0=32(m/\gamma)\log(en)\), and source-coordinate tolerance
\(0<\eta\le\eta_0=\min(1,Y,16Ym/\gamma)\). These are the existing
Harmonic source qualifications; in particular the retained set below is
nonempty. At hidden layer
\(j\), the existing source families are

\[
h_n^{(j)}(t,v),\qquad
W_0^{(j)}h_n^{(j-1)}(t,v),\qquad
\delta_n^{(j)}(t,v),\qquad
W_0^{(j+1)T}\delta_n^{(j+1)}(t,v),
\]

with the same omissions at the first and last layers as in [the preceding Harmonic construction](#harmonic-construction).
Here \(v=x/\sqrt d\in S^{d-1}\), \(W_0\) is an initialized
dense mixer, and \(\delta_n\) is the existing passive-query backward
field. Consider one scalar coordinate \(g(t,v)\) of any of these
families. Put

<a id="eq-setup-q-1"></a>
\[
G(u,v)=g\bigl(T(1+\cos u)/2,v\bigr),\qquad
\alpha=\alpha_T=\frac{r_t}{4T},\qquad a=\alpha/2.
\tag{Setup-Q.1}
\]

The source theorem supplies holomorphy on a neighborhood of
\(\{|\operatorname{Im}u|\le\alpha\}\times\mathcal Q_{r_q}\)
and the uniform coordinate bound \(|G|\le M_n\), where

<a id="eq-setup-q-2"></a>
\[
\mathcal Q_r=
\{z\in\mathbb C^d:z^Tz=1,\ \|\operatorname{Im}z\|_2\le\sinh r\},
\qquad M_n=10\max(H_L^{\rm src},\tau)\sqrt n.
\tag{Setup-Q.2}
\]

As in the original source proof, \(\alpha\le1\). The choice of the
smaller strip \(a\) merely leaves an analytic margin. All bounds below
are deterministic on that same source event.

For \(d\ge2\), use the real orthonormal spherical harmonics
\(Y_{\ell,b}\) under probability-sphere measure \(\sigma\). Their
degrees are denoted \(\ell\), to distinguish them from hidden layers.
Write

<a id="eq-setup-q-3"></a>
\[
h_\ell={\ell+d-1\choose d-1}-{\ell+d-3\choose d-1},\qquad
\mathcal Y_{\ell_*}=\max_{0\le\ell\le \ell_*}\sqrt{h_\ell},\qquad
H=\sum_{\ell=0}^{\ell_*} h_\ell.
\tag{Setup-Q.3}
\]

Impossible binomials are zero. Retain **exactly** the original joint set

<a id="eq-setup-q-4"></a>
\[
\Lambda=\{(k,\ell,b):k\ge0,\ \alpha k+r_q\ell\le H(T,\eta),
\ 1\le b\le h_\ell\},
\quad N=|\Lambda|=N(T,\eta),
\tag{Setup-Q.4}
\]

and put \(p=\max_\Lambda k\), \(\ell_*=\max_\Lambda\ell\).
The exact retained cosine coefficients are

<a id="eq-setup-q-5"></a>
\[
c_{k\ell b}
=\gamma_k\int_0^{2\pi}\int_{S^{d-1}}
G(u,v)\cos(ku)Y_{\ell,b}(v)\,d\sigma(v)\frac{du}{2\pi},
\quad \gamma_0=1,\quad\gamma_k=2\ (k\ge1).
\tag{Setup-Q.5}
\]

Thus the factor two for positive modes is part of the definition and of
every error estimate below. The original expansion proof gives coordinate
error at most \(\eta/16\) for the omitted modes.

Define the target error for each retained coefficient by

<a id="eq-setup-q-6"></a>
\[
\epsilon_c=\frac{\eta}{16N\mathcal Y_{\ell_*}}.
\tag{Setup-Q.6}
\]

The explicit rule constructed below gives exact-value quadrature error
at most \(\epsilon_c/2\). If supplied nodal values have the common
coordinate accuracy in [(Setup-Q.24)](#eq-setup-q-24), their contribution is at most
\(\epsilon_c/2\). Consequently every retained coefficient has error
at most \(\epsilon_c\), and its finite reconstruction has error at
most

<a id="eq-setup-q-7"></a>
\[
\frac{\eta}{16}+N\mathcal Y_{\ell_*}\epsilon_c=\frac{\eta}{8}<\eta.
\tag{Setup-Q.7}
\]

The first term is the original truncation tail. Every member of every
source pair is treated with its own coordinate guarantee.

<a id="setup-quadrature-2"></a>
##### Sphere coordinates and their complex neighborhood

For \(d\ge3\), use the usual successive polar angles
\(\theta_1,\ldots,\theta_{d-2}\in[0,\pi]\) and final azimuth
\(\varphi\in[0,2\pi]\):

<a id="eq-setup-q-8"></a>
\[
v=(\cos\theta_1,\ \sin\theta_1\cos\theta_2,\ldots,
\ \textstyle\prod_{i=1}^{d-2}\sin\theta_i\cos\varphi,
\ \textstyle\prod_{i=1}^{d-2}\sin\theta_i\sin\varphi).
\tag{Setup-Q.8}
\]

The intermediate coordinates follow the same displayed pattern. For
\(d=2\), use only \(v=(\cos\varphi,\sin\varphi)\).
Introduce

<a id="eq-setup-q-9"></a>
\[
I_b=\int_0^\pi\sin^b\theta\,d\theta,\qquad
I_0=\pi,\quad I_1=2,\quad
I_b=\frac{b-1}{b}I_{b-2}\ (b\ge2).
\tag{Setup-Q.9}
\]

The recurrence follows by integration by parts. Differentiating [(Setup-Q.8)](#eq-setup-q-8) gives
orthogonal coordinate tangent vectors: the vector for each successive
angle has length equal to the product of the preceding polar sines.
Multiplying these lengths gives the Jacobian
\(\prod_{i=1}^{d-2}\sin^{d-1-i}\theta_i\). Its successive
integrals are the factors \(I_{d-1-i}\), so normalization proves that
probability-sphere integration becomes product integration under the uniform measures
\(d\theta_i/\pi\) and \(d\varphi/(2\pi)\), with the multiplier

<a id="eq-setup-q-10"></a>
\[
W(\theta)=\prod_{i=1}^{d-2}
\frac{\pi}{I_{d-1-i}}\sin^{d-1-i}\theta_i.
\tag{Setup-Q.10}
\]

Empty products are one. In particular this formula includes \(d=2\).
Write

<a id="eq-setup-q-11"></a>
\[
A_d=\prod_{b=1}^{d-2}\frac{\pi}{I_b},\qquad
D_d^{\rm ang}=\frac{(d-2)(d-1)}2,\qquad
h=\frac{r_q}{2(d-1)},\qquad
\sigma=\operatorname{arsinh}(2h/\pi).
\tag{Setup-Q.11}
\]

These constants expose the dependence on dimension. The angular multiplier
satisfies \(0\le W\le A_d\) on real angles and

<a id="eq-setup-q-12"></a>
\[
|W(\theta)|\le A_d(\cosh h)^{D_d^{\rm ang}}
\quad\text{if all }|\operatorname{Im}\theta_i|\le h.
\tag{Setup-Q.12}
\]

Indeed \(|\sin(x+iy)|^2=\sin^2x+\sinh^2y\le\cosh^2y\).

To check the source domain, represent [(Setup-Q.8)](#eq-setup-q-8) as successive coordinate-plane
rotations applied to a real unit vector. Real rotations preserve
\(z^Tz=1\) and \(\|\operatorname{Im}z\|_2\). For
\(z=b+ic\) on that quadric there is \(s\ge0\) with
\(\|b\|_2=\cosh s\), \(\|c\|_2=\sinh s\). Applying a
coordinate-plane rotation of imaginary angle \(iy\) gives

<a id="eq-setup-q-13"></a>
\[
\|\operatorname{Im}(R(iy)z)\|_2
\le \sinh|y|\,\|b\|_2+\cosh|y|\,\|c\|_2
=\sinh(s+|y|).
\tag{Setup-Q.13}
\]

For the unchanged coordinates the real part of this rotation is the
identity, whose norm is at most \(\cosh|y|\); its imaginary part
has norm at most \(\sinh|y|\), which proves the inequality.
Decompose each complex angle into its commuting real and imaginary
rotations and apply [(Setup-Q.13)](#eq-setup-q-13) successively. If all \(d-1\) angles have
imaginary parts of magnitude at most \(h\), the resulting point lies
in \(\mathcal Q_{(d-1)h}=\mathcal Q_{r_q/2}\). Real parts may
lie outside the fundamental angle boxes without changing this argument.

The angular composition of a degree-\(\ell\) harmonic polynomial
is a trigonometric polynomial of degree at most \(\ell\) separately
in every angle. If a trigonometric polynomial \(P\) has degrees
between \(-\ell\) and \(\ell\) and satisfies \(|P|\le C\)
on the real axis, then

<a id="eq-setup-q-14"></a>
\[
|P(x+iy)|\le C e^{\ell|y|}.
\tag{Setup-Q.14}
\]

For \(y\ge0\), multiply its Laurent polynomial by \(z^\ell\),
apply the maximum modulus principle inside \(|z|\le1\), and set
\(z=e^{i(x+iy)}\). For \(y\le0\), use the reversed Laurent
polynomial. Iterating this argument over the angles, starting from
the real-sphere bound \(|Y_{\ell,b}|\le\sqrt{h_\ell}\), gives

<a id="eq-setup-q-15"></a>
\[
|Y_{\ell,b}(v)|\le\mathcal Y_{\ell_*} e^{\ell_*(d-1)h}
\quad(\ell\le \ell_*).
\tag{Setup-Q.15}
\]

Finally \(|\cos(ku)|\le e^{ka}\) in the time strip. Every
coefficient integrand, including \(\gamma_k\), is therefore
holomorphic on the product domain just described and bounded there by

<a id="eq-setup-q-16"></a>
\[
B_{\rm int}=
2M_n\mathcal Y_{\ell_*} A_d
\exp\{ap+\ell_*(d-1)h\}(\cosh h)^{D_d^{\rm ang}}.
\tag{Setup-Q.16}
\]

This is an integrand bound, not an additional source or rank parameter.

<a id="setup-quadrature-3"></a>
##### Explicit positive quadrature and its error

###### Periodic variables

For a \(2\pi\)-periodic function \(F\), use
\(Q_NF=N^{-1}\sum_{r=0}^{N-1}F(2\pi r/N)\).
If \(F\) is holomorphic near \(|\operatorname{Im}z|\le b\)
and bounded there by \(B\), contour translation gives Fourier
coefficient bound \(|\widehat F_k|\le Be^{-b|k|}\). Absolute
convergence permits termwise quadrature. The discrete average of
\(e^{ikz}\) is one when \(N\) divides \(k\), zero otherwise;
therefore

<a id="eq-setup-q-17"></a>
\[
\left|\int_0^{2\pi}F(u)\frac{du}{2\pi}-Q_NF\right|
\le2B\sum_{r=1}^{\infty}e^{-brN}
=\frac{2B}{e^{bN}-1}.
\tag{Setup-Q.17}
\]

Use this rule for time with \(b=a\), and for azimuth with \(b=h\).
Both rules have positive weights summing to one.

###### Polar variables

The following construction supplies the nodes and weights; no Gaussian
quadrature construction is assumed. For an integer \(M\ge1\), let

\[
\omega_r=\frac{(2r+1)\pi}{2M},\quad x_r=\cos\omega_r,
\quad r=0,\ldots,M-1,
\]
<a id="eq-setup-q-18"></a>
\[
w_r=\frac1M\left[
1-2\sum_{k=1}^{\lfloor(M-1)/2\rfloor}
\frac{\cos(2k\omega_r)}{4k^2-1}\right].
\tag{Setup-Q.18}
\]

These are Fejér's first interpolatory weights for the normalized integral
\(\frac12\int_{-1}^1\). The discrete cosine identities at these
nodes give the interpolant

<a id="eq-setup-q-19"></a>
\[
I_{M-1}F(x)=
\frac1M\sum_r F(x_r)
\left[1+2\sum_{k=1}^{M-1}\cos(k\omega_r)T_k(x)\right].
\tag{Setup-Q.19}
\]

To verify the identity, sum the elementary geometric series for
\(e^{ij\omega_r}\), or use
\(2\cos j\omega\cos k\omega=\cos((j-k)\omega)+
\cos((j+k)\omega)\). The constant mode has squared discrete norm
\(M\); all nonconstant modes through \(M-1\) have squared norm
\(M/2\), and unequal modes are orthogonal. Evaluating [(Setup-Q.19)](#eq-setup-q-19) at
the nodes then gives their prescribed values. Substitution
\(x=\cos\omega\) in the elementary integral gives

\[
\frac12\int_{-1}^1 T_k(x)\,dx=
\begin{cases}
1,&k=0,\\
0,&k\text{ odd},\\
-1/(k^2-1),&k\ge2\text{ even}.
\end{cases}
\]

Integrating [(Setup-Q.19)](#eq-setup-q-19) proves [(Setup-Q.18)](#eq-setup-q-18) and exactness for every polynomial of
degree at most \(M-1\). Moreover

\[
2\sum_{k=1}^K\frac1{4k^2-1}=1-\frac1{2K+1}<1
\]

for finite \(K\), by telescoping. Thus every \(w_r>0\), including
the empty-sum case, and exactness for constants gives \(\sum_rw_r=1\).

Suppose \(F\) is holomorphic near the filled Bernstein ellipse
\(x=(z+z^{-1})/2\), \(|z|=e^\sigma\), and bounded there by
\(B\). Its Laurent expansion in \(z\) is symmetric under
\(z\mapsto z^{-1}\). Cauchy's coefficient formula therefore gives
Chebyshev coefficients of magnitude at most \(2Be^{-k\sigma}\)
for \(k\ge1\). The truncated degree-\(M-1\) series has uniform
real-interval error at most
\(2Be^{-M\sigma}/(1-e^{-\sigma})\). Both the exact normalized
integral and the positive quadrature have operator norm one on real
continuous functions. Subtracting that polynomial from each proves

<a id="eq-setup-q-20"></a>
\[
\left|\frac12\int_{-1}^1 F(x)\,dx-\sum_rw_rF(x_r)\right|
\le\frac{4Be^{-M\sigma}}{1-e^{-\sigma}}.
\tag{Setup-Q.20}
\]

Apply this rule to \(\theta=\pi(1+x)/2\). The ellipse has
\(|\operatorname{Im}\theta|\le(\pi/2)\sinh\sigma=h\),
by [(Setup-Q.11)](#eq-setup-q-11). It is therefore inside the previously verified angular
domain. The normalization becomes \(d\theta/\pi\), as required
in [(Setup-Q.10)](#eq-setup-q-10).

###### Tensor rule and explicit sufficient sizes

Each univariate exact integral and quadrature is a contraction in the
supremum norm. Write their product difference as a telescoping sum,
changing one factor at a time. Apply [(Setup-Q.17)](#eq-setup-q-17) or [(Setup-Q.20)](#eq-setup-q-20) to that factor while
the remaining variables are real, and then apply the other contraction
operators. There are \(d\) variables in total: time, azimuth and
\(d-2\) polar variables. This gives

<a id="eq-setup-q-21"></a>
\[
|c_{k\ell b}-Q c_{k\ell b}|
\le B_{\rm int}\left[
\frac2{e^{aN_t}-1}+\frac2{e^{hN_\varphi}-1}
+\frac{4(d-2)e^{-\sigma N_\theta}}{1-e^{-\sigma}}
\right].
\tag{Setup-Q.21}
\]

Here \(Q c_{k\ell b}\) denotes application of the tensor rule to
the integrand of [(Setup-Q.5)](#eq-setup-q-5) after the angular change of variables. The signs
of the harmonic and cosine do not affect positivity of the underlying
integration rule.

Choose

\[
N_t=\max\left\{1,
\left\lceil\frac1a\log\left(1+\frac{4dB_{\rm int}}{\epsilon_c}\right)
\right\rceil\right\},
\]
\[
N_\varphi=\max\left\{1,
\left\lceil\frac1h\log\left(1+\frac{4dB_{\rm int}}{\epsilon_c}\right)
\right\rceil\right\},
\]
<a id="eq-setup-q-22"></a>
\[
N_\theta=\max\left\{1,
\left\lceil\frac1\sigma
\log\left(\frac{8dB_{\rm int}}
{\epsilon_c(1-e^{-\sigma})}\right)\right\rceil\right\}
\quad(d\ge3).
\tag{Setup-Q.22}
\]

Each of the \(d\) contributions in [(Setup-Q.21)](#eq-setup-q-21) is then at most
\(\epsilon_c/(2d)\). The total spatial node count is

<a id="eq-setup-q-23"></a>
\[
N_x=N_\varphi N_\theta^{d-2}\quad(d\ge3),
\qquad N_x=N_\varphi\quad(d=2).
\tag{Setup-Q.23}
\]

The dependence on \(d\), \(\alpha\), \(r_q\), \(p\),
\(\ell_*\), \(M_n\), \(N\), and \(\eta\) is explicit in
[(Setup-Q.3)](#eq-setup-q-3), [(Setup-Q.6)](#eq-setup-q-6), [(Setup-Q.9)](#eq-setup-q-9), [(Setup-Q.11)](#eq-setup-q-11), [(Setup-Q.16)](#eq-setup-q-16), and [(Setup-Q.22)](#eq-setup-q-22). In particular no equality
\(N_x=H\) or \(N_t=p+1\) is assumed.

<a id="setup-quadrature-4"></a>
##### Inexact nodal values and exact source pairing

At every time/spatial node, suppose an initialization-based procedure
supplies all needed vector sources with coordinate error at most

<a id="eq-setup-q-24"></a>
\[
\delta_{\rm node}=
\frac{\epsilon_c}{4A_d\mathcal Y_{\ell_*}}.
\tag{Setup-Q.24}
\]

All quadrature weights before the multiplier \(W\) are positive
and have total mass one. On real nodes \(W\le A_d\),
\(|Y_{\ell,b}|\le\mathcal Y_{\ell_*}\), \(|\cos ku|\le1\), and
\(\gamma_k\le2\). Therefore the coefficient error caused by
these nodal errors is at most

<a id="eq-setup-q-25"></a>
\[
2A_d\mathcal Y_{\ell_*}\delta_{\rm node}=\epsilon_c/2.
\tag{Setup-Q.25}
\]

This supplies the second half of the error allocation in [(Setup-Q.7)](#eq-setup-q-7).
It does not assume holomorphy of the numerical nodal approximation;
the quadrature analysis applies to the exact analytic source, followed
by the separate finite-sum perturbation estimate [(Setup-Q.25)](#eq-setup-q-25).

For exact preservation of initialized-matrix pairing, more than separate
numerical accuracy is required. In the following pairing identities only,
let \(g\) denote the full \(\mathbb R^n\)-valued source, so the
preceding coordinate estimates apply to each of its entries. Let \(A\)
be the fixed initialized
matrix in one pair: either \(W_0^{(j)}\) or
\(W_0^{(j+1)T}\). The two input families are \(g\) and
\(Ag\). Require their nodal approximants to have the exact algebraic
form

<a id="eq-setup-q-26"></a>
\[
\widetilde{Ag}(u_r,v_s)=A\widetilde g(u_r,v_s),
\tag{Setup-Q.26}
\]

while **each side separately** has coordinate error at most
\(\delta_{\rm node}\) relative to its own exact source. Applying
identical real quadrature, cosine normalization and retained-mode
restriction to both sides gives, in exact arithmetic,

<a id="eq-setup-q-27"></a>
\[
\widetilde c^{\,Ag}_{k\ell b}
=\sum_{r,s}\beta_{k\ell b,rs}A\widetilde g(u_r,v_s)
=A\sum_{r,s}\beta_{k\ell b,rs}\widetilde g(u_r,v_s)
=A\widetilde c^{\,g}_{k\ell b}.
\tag{Setup-Q.27}
\]

The scalar coefficients \(\beta\) are the same in both sums.
The reconstructed approximants consequently satisfy
\(p_{Ag}=Ap_g\) at every real time/query, exactly. The source-space
membership and action identities used in [the preceding Harmonic construction](#harmonic-construction) are unchanged.

Exact source evaluation satisfies [(Setup-Q.26)](#eq-setup-q-26). The original common finite
initial-jet reconstruction also satisfies it: differentiation, scalar
continuation, truncation and this quadrature all commute with a fixed
matrix. Its sufficiently large common jet cutoff can certify the
required coordinate errors separately for every member, because each
member has the same source bound. This establishes finite realizability
without establishing an efficient cutoff. Independently computed
approximate nodal values do not automatically satisfy [(Setup-Q.26)](#eq-setup-q-26), even when
they are each accurate. Deriving the image's error from the feature's
coordinate error through a dimension-dependent matrix norm is not used.

No quadrature node is a generator of \(E_j\). The generators remain
the coefficient vectors indexed by \(\Lambda\), plus the original
exact initialized vectors. Thus

<a id="eq-setup-q-28"></a>
\[
\dim E_j\le R=2m+d+1+4N,
\tag{Setup-Q.28}
\]

with the existing boundary-layer improvements. This is exactly the old
dimension certificate. The original budget prescription proves its own
bound \(9R\le q\); replacing the quadrature does not enlarge it.
For a supplied alternative mode set, the existing actual-rank test
\(9r\le q\), \(r=\max_j\dim E_j\), is still the applicable
selector guarantee. Numerical perturbations can change actual rank, so the
safe argument uses [(Setup-Q.28)](#eq-setup-q-28), not an assertion that an old accidental rank
deficiency persists. The selected runtime, its learned and fixed storage,
and the dense-comparison certificate therefore retain their existing
bounds whenever the original count certificate applies.
The exact initialized training vectors, first-weight columns and constant
are still inserted by their original exact construction. Baseline-only,
zero-label and full-width exact-retention branches need no quadrature and
are unaffected.

<a id="setup-quadrature-5"></a>
##### Dimensions one and two

For \(d=2\), equations [(Setup-Q.3)](#eq-setup-q-3)--[(Setup-Q.28)](#eq-setup-q-28) apply with no polar angles,
\(A_2=1\), \(D_2^{\rm ang}=0\), and \(h=r_q/2\).
The basis is \(1,\sqrt2\cos(\ell\varphi),
\sqrt2\sin(\ell\varphi)\). Hence \(\mathcal Y_{\ell_*}=\sqrt2\)
if \(\ell_*\ge1\), and \(\mathcal Y_0=1\). The spatial rule is
just the positive circle trapezoid, with \(N_x=N_\varphi\).

For \(d=1\), the source domain has precisely the two inputs
\(v=-1,1\). Perform their cosine expansions separately, with
\(N_1=N_1(T,\eta)\), \(p=N_1-1\), and

<a id="eq-setup-q-29"></a>
\[
\epsilon_c=\frac{\eta}{16N_1},\qquad
B_{\rm int}=2M_ne^{ap},\qquad
N_t=\max\left\{1,
\left\lceil\frac1a\log\left(1+\frac{4B_{\rm int}}{\epsilon_c}\right)
\right\rceil\right\}.
\tag{Setup-Q.29}
\]

Use the time trapezoid only. Its coefficient error is at most
\(\epsilon_c/2\). The common nodal tolerance is
\(\delta_{\rm node}=\epsilon_c/4\), which gives the other half
because \(\gamma_k\le2\). The original separate time tails are
at most \(\eta/16\), so the same reconstruction bound [(Setup-Q.7)](#eq-setup-q-7) holds
at both inputs. There are \(N_x=2\) spatial evaluations, not an
angular grid. The rank certificate remains
\(R=2m+d+1+8N_1\), and the same exact linear pairing proof applies.

<a id="setup-quadrature-6"></a>
##### Node generation, arithmetic and peak setup memory

All counts below use the exact-real arithmetic contract of [the preceding Harmonic construction](#harmonic-construction).
Elementary trigonometric and inverse/hyperbolic scalar evaluations are
reported as scalar calls; their bit complexity is not claimed to be
constant. The needed one-dimensional rule orders are part of the input
to the following execution, determined by the explicit certificates above.

For \(d\ge3\), build the \(N_\theta\) nodes and weights in
[(Setup-Q.18)](#eq-setup-q-18). At each node use angle-addition recurrences to evaluate the
\(O(N_\theta)\) cosine terms in its weight. This costs
\(O(N_\theta^2)\) arithmetic and \(O(N_\theta)\) words.
The same normalized unweighted rule is reused in every polar coordinate;
only the Jacobian power changes. Computing the constants [(Setup-Q.9)](#eq-setup-q-9) and the
normalizations [(Setup-Q.10)](#eq-setup-q-10) costs \(O(d)\) arithmetic. The time and azimuth
rules cost \(O(N_t+N_\varphi)\) arithmetic and words if cached.
Enumerating the spatial tensor product and mapping each point to the
sphere costs \(O(dN_x)\). Powers in [(Setup-Q.10)](#eq-setup-q-10) can be computed using
\(O(d)\) multiplications per node after powers of each cached
one-dimensional sine through \(d-2\) are prepared, or directly in
\(O(d^2)\) per node. Use the former execution and charge
\(O(dN_\theta)\) preparation and storage.

Consequently a sufficient rule-only bound is

\[
\mathcal G_{\rm rule,time}
=O\bigl(N_\theta^2+dN_\theta+N_t+N_\varphi+dN_x+d\bigr),
\]
<a id="eq-setup-q-30"></a>
\[
\mathcal G_{\rm rule,memory}
=O(dN_\theta+N_t+N_\varphi+d),\qquad d\ge3.
\tag{Setup-Q.30}
\]

There are \(O(N_\theta+N_t+N_\varphi)\) elementary scalar
trigonometric calls with direct one-dimensional tables. The orders in
[(Setup-Q.22)](#eq-setup-q-22) require a fixed number of further elementary calls. For \(d=2\)
delete all polar terms and use \(O(N_t+N_x)\) time and cached words;
for \(d=1\) use \(O(N_t)\). Streaming the periodic tables can
reduce their memory, but the displayed cached implementation is enough.

At each spatial node, the separated harmonic basis from the complete
geometric-basis argument in [the preceding Harmonic construction](#harmonic-construction) can still be used. In addition
to [(Setup-Q.30)](#eq-setup-q-30), charge

\[
\mathcal G_{\rm basis,time}=
\begin{cases}
0,&d=1,\\
O(N_x(\ell_*+1)),&d=2,\\
O\bigl(d(\ell_*+1)^2+dN_x[(\ell_*+1)^2+H]\bigr),&d\ge3,
\end{cases}
\]
<a id="eq-setup-q-31"></a>
\[
\mathcal G_{\rm basis,memory}=
\begin{cases}
O(1),&d=1,\\
O(\ell_*+1),&d=2,\\
O\bigl(d[(\ell_*+1)^2+H]\bigr),&d\ge3.
\end{cases}
\tag{Setup-Q.31}
\]

That recurrence includes scalar normalization generation; this route does
not assume a precomputed dense table of harmonics at all spatial nodes.
Let \(\mathcal G_{\rm time},\mathcal G_{\rm memory}\) be the
sums of the rule and basis bounds.

<a id="setup-quadrature-7"></a>
##### Polylogarithmic quadrature regime and claim boundary

The explicit estimates hold for every finite permitted \(T,\eta\).
The following asymptotic statement has additional stated conditions:
fix \(d,L,m\), activation/source coefficients and a positive allowed
label size, and let

<a id="eq-setup-q-34"></a>
\[
T=O(\log(en)),\qquad \log(1/\eta)=O(\log(en)),\qquad
r_t^{-1},r_q^{-1}=O(\sqrt{\log(en)}).
\tag{Setup-Q.34}
\]

These conditions cover the original \((T_0,1/n)\) specialization
and the existing polynomial-accuracy inverse prescriptions whenever
their analytic compressed branch is used. They do not cover every
arbitrarily large supplied budget under an unchanged claim of
polylogarithmic horizon.

Then \(\alpha^{-1}=O(\log(en)^{3/2})\),
\(H(T,\eta)=O(\log(en))\), and the unchanged cutoffs satisfy

<a id="eq-setup-q-35"></a>
\[
p=O(\log(en)^{5/2}),\qquad
\ell_*=O(\log(en)^{3/2}),\qquad
N=O(\log(en)^{3d/2+1}).
\tag{Setup-Q.35}
\]

The logarithm of \(M_n\) is \(O(\log(en))\), that of
\(\mathcal Y_{\ell_*}\) is \(O_d(\log\log(en))\), and
\(ap+\ell_*(d-1)h=O(\log(en))\). It follows directly from [(Setup-Q.6)](#eq-setup-q-6),
[(Setup-Q.11)](#eq-setup-q-11), and [(Setup-Q.16)](#eq-setup-q-16) that
\(\log(B_{\rm int}/\epsilon_c)=O_d(\log(en))\).
Since \(\sigma\) is comparable to \(h\) for the current
bounded radii, [(Setup-Q.22)](#eq-setup-q-22) gives

<a id="eq-setup-q-36"></a>
\[
N_t=O_d(\log(en)^{5/2}),\qquad
N_\varphi,N_\theta=O_d(\log(en)^{3/2}),\qquad
N_x=O_d(\log(en)^{3(d-1)/2})\quad(d\ge2).
\tag{Setup-Q.36}
\]

For \(d=1\), [(Setup-Q.29)](#eq-setup-q-29) gives \(N_t=O(\log(en)^{5/2})\) and
\(N_x=2\). Thus even the **total** number of real time/query
pairs is polylogarithmic for fixed dimension:

<a id="eq-setup-q-37"></a>
\[
N_tN_x=O_d(\log(en)^{3d/2+1}).
\tag{Setup-Q.37}
\]

Node generation and harmonic evaluation have the explicit costs [(Setup-Q.30)](#eq-setup-q-30)--[(Setup-Q.31)](#eq-setup-q-31).
The continuation, source projection, selection and assembly costs are proved
below in [the complete source-jet bridge](#setup-bridge). All quadrature and
dense setup arrays are discarded under the original retained-storage convention.

For the arbitrary supplied-budget construction in [the preceding Harmonic construction](#harmonic-construction), substitute
its actual
\(T=T_0+4mu/\gamma\), \(\eta=\eta_0e^{-u}\) into [(Setup-Q.22)](#eq-setup-q-22).
If \(u\) grows faster than \(\log n\), the claim [(Setup-Q.36)](#eq-setup-q-36) need not
hold. The finite quantitative rule and preservation of that budget's
rank/error certificate still hold. There is no silent restriction of the
forward theorem to polynomial target accuracies.

<a id="setup-core"></a>
#### Local Taylor continuation from computed anchors

<a id="setup-core-1"></a>
##### Model, imported event, and claimed output

Write \(v=x/\sqrt d\), so the query sphere is \(\|v\|_2=1\). The
network, its backward fields, and the normalized parameter coordinates are

\[
z^{(1)}=Av,\qquad z^{(j)}=W^{(j)}h^{(j-1)},\qquad
h^{(j)}=\phi_j(z^{(j)}),\qquad f_n=w^Th^{(L)}/n,
\]
\[
k^{(L)}=w,\qquad
\delta^{(j)}=\phi_j'(z^{(j)})\odot k^{(j)},\qquad
k^{(j)}=(W^{(j+1)})^T\delta^{(j+1)},
\]
<a id="eq-setup-c-1"></a>
\[
\theta=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)
\in\mathbb R^P,\qquad P=nd+(L-1)n^2+n.
\tag{Setup-C.1}
\]

Let \(r_a=f_n(v_a)-y_a\), \(\rho=\|r\|_2/\sqrt m\),
\(Y=\|y\|_2/\sqrt m\), \(\lambda=\gamma/m\), and
\(S=16Y/\lambda\). With \(\xi_a=\nabla_\theta f_n(v_a)\), the
mean-square-loss flow with the prescribed mobilities is

<a id="eq-setup-c-2"></a>
\[
\dot\theta=F(\theta),\qquad
F(\theta)=-\frac2m\sum_a r_a\xi_a(\theta).
\tag{Setup-C.2}
\]

The complex extension of this equation uses the algebraic transpose and no
complex conjugations. Norm bounds below are ordinary complex Euclidean or
Frobenius bounds; they do not use positivity of a complex Gram matrix.

Assume \(Y>0\), the full original common label interval, and the original
source and analytic-extension width gates. All activations are the original
strip-holomorphic activations, with possibly unbounded values. Let
\(b=\max_j|\phi_j(0)|\), and let \(s\ge1,t_2\ge1\) bound their
first and second derivatives on \( |\operatorname{Im}z|\le a/2\).
The imported event gives, on the real trajectory,

\[
\|A\|_{\rm op}/\sqrt n<9,\quad
\|W^{(j)}\|_{\rm op}<9,\quad
\|w\|_2/\sqrt n\le2Y/\sqrt\lambda,
\]
<a id="eq-setup-c-3"></a>
\[
\rho(t)\le Ye^{-\lambda t/2},\quad
\int_0^\infty\rho(t)\,dt\le2Y/\lambda,
\quad \max_{a,j,i,t\ge0}|k_{a,i}^{(j)}(t)|
 \le2K_{\rm src}S\sqrt{\log(en)}.
\tag{Setup-C.3}
\]

For every finite source horizon, the exact trajectory is holomorphic on the
source time neighborhood with radius \(r_t=c_t/\sqrt{\log(en)}\),
including its endpoint neighborhoods. Its joint passive-query extension has
preactivation imaginary parts at most \(3a/8\), operator caps ten, feature RMS
bounds \(H_j^{\rm src}\), and readout RMS at most \(SH_L^{\rm src}\).
Along every complex disk of radius \(r_t/2\) centered on a nonnegative real
time, its residual RMS is at most \(2Y\). These are the source-domain and
late-extension conclusions of [the preceding Harmonic construction](#harmonic-construction).

The task of this component is to supply at any finite list of real time/query nodes
all four families

<a id="eq-setup-c-4"></a>
\[
h^{(j)},\quad W_0^{(j)}h^{(j-1)},\quad
\delta^{(j)},\quad W_0^{(j+1)T}\delta^{(j+1)},
\tag{Setup-C.4}
\]

with the existing boundary-layer omissions, with coordinate error at most a
given \(\delta_{\rm node}>0\), and with exact initialized-matrix pairing.
For the certified quadrature route one uses

<a id="eq-setup-c-5"></a>
\[
\delta_{\rm node}=\frac{\eta}{64N A_d\mathcal Y_{\ell_*}^2}\quad(d\ge2),
\qquad \delta_{\rm node}=\frac{\eta}{64N_1}\quad(d=1).
\tag{Setup-C.5}
\]

Here \(N,N_1,A_d,\mathcal Y_{\ell_*}\) are exactly the quantities defined in
[positive coefficient quadrature](#setup-quadrature). In its fixed-parameter polynomial
accuracy regime, \(\log(1/\delta_{\rm node})=O(\log(en))\).

<a id="setup-core-2"></a>
##### Complex endpoint estimates with explicit coefficients

The constants in this section apply to complex parameters with operator caps
eleven, readout RMS at most
\(R=1+SH_L^{\rm src}\), and preactivations in the safe half-strip.
The extra margin is used only for the numerical restart proof. Define

\[
H_1=\max(1,b+11s),\qquad
H_j=\max(1,b+11sH_{j-1}),
\]
<a id="eq-setup-c-6"></a>
\[
B_j=Rs(11s)^{L-j},\qquad
P_1=1,\quad P_j=H_{j-1}+11sP_{j-1},\quad P_* =\max_jP_j.
\tag{Setup-C.6}
\]

For \(M\ge0\), define

\[
\kappa_L(M)=1,\qquad
\kappa_j(M)=11s\kappa_{j+1}(M)
           +11t_2MP_{j+1}+B_{j+1},
\]
\[
D_j(M)=s\kappa_j(M)+t_2MP_j,\qquad
\kappa_*(M)=\max_j\kappa_j(M),
\]
\[
G=H_L+B_1+\sum_{j=2}^LB_jH_{j-1},
\]
<a id="eq-setup-c-7"></a>
\[
J(M)=sP_L+D_1(M)+
\sum_{j=2}^L\{H_{j-1}D_j(M)+B_jsP_{j-1}\}.
\tag{Setup-C.7}
\]

Every coefficient is explicit, and \(\kappa_*,D_j,J\) are bounded by
affine functions of \(M\), with fixed structural coefficients.

Let \(u,v\) be two such states, \(E=\|u-v\|_2\), and suppose only
the carriers at \(v\) have coordinate bound \(M\). Subtracting the
forward recursion gives

<a id="eq-setup-c-8"></a>
\[
\frac{\|z^{(j)}(u)-z^{(j)}(v)\|_2}{\sqrt n}\le P_jE,
\qquad
\frac{\|h^{(j)}(u)-h^{(j)}(v)\|_2}{\sqrt n}\le sP_jE.
\tag{Setup-C.8}
\]

For the first layer this uses \(\|\Delta A\|_F/\sqrt n\le E\).
For a later layer use

\[
z^{(j)}(u)-z^{(j)}(v)
=W^{(j)}(u)\Delta h^{(j-1)}+\Delta W^{(j)}h^{(j-1)}(v),
\]

whose two normalized bounds are \(11sP_{j-1}E\) and \(H_{j-1}E\).
The straight scalar segment between each pair of preactivations remains in
the half-strip, justifying the complex derivative bound used here.

For the backward subtraction use the carrier at \(v\):

\[
\Delta\delta^{(j)}
=\phi_j'(z^{(j)}(u))\odot\Delta k^{(j)}
 +[\phi_j'(z^{(j)}(u))-\phi_j'(z^{(j)}(v))]\odot k^{(j)}(v).
\]

The second term has RMS at most \(t_2MP_jE\). For \(j<L\),

\[
\Delta k^{(j)}
=(W^{(j+1)}(u))^T\Delta\delta^{(j+1)}
 +(\Delta W^{(j+1)})^T\delta^{(j+1)}(v).
\]

The two costs are \(11D_{j+1}(M)E\) and \(B_{j+1}E\), while
the top readout cost is \(E\). Induction proves

<a id="eq-setup-c-9"></a>
\[
\frac{\|\Delta k^{(j)}\|_2}{\sqrt n}\le\kappa_j(M)E,
\qquad
\frac{\|\Delta\delta^{(j)}\|_2}{\sqrt n}\le D_j(M)E.
\tag{Setup-C.9}
\]

The gradient blocks are

\[
\xi_a=\left(\delta_a^{(1)}v_a^T/\sqrt n,
 (\delta_a^{(j)}h_a^{(j-1)T}/n)_{j=2}^L,h_a^{(L)}/\sqrt n\right).
\]

Their norms are bounded by \(B_1,B_jH_{j-1},H_L\). In a hidden
block the difference splits into
\(\Delta\delta\,h(u)^T+\delta(v)\Delta h^T\); [(Setup-C.8)](#eq-setup-c-8)--[(Setup-C.9)](#eq-setup-c-9) then give

<a id="eq-setup-c-10"></a>
\[
\|\xi_a(u)\|_2\le G,\qquad
\|\xi_a(u)-\xi_a(v)\|_2\le J(M)E.
\tag{Setup-C.10}
\]

If the parameter segment from \(v\) to \(u\) is in the same admissible
domain, integration of the first gradient bound also gives
\(|f_a(u)-f_a(v)|\le GE\). Consequently

<a id="eq-setup-c-11"></a>
\[
\|F(u)-F(v)\|_2
\le [2G^2+2\rho(v)J(M)]\|u-v\|_2.
\tag{Setup-C.11}
\]

Indeed subtract [(Setup-C.2)](#eq-setup-c-2) as
\(-2m^{-1}\sum_a[(r_a(u)-r_a(v))\xi_a(u)
+r_a(v)(\xi_a(u)-\xi_a(v))]\), and apply sample Cauchy--Schwarz
to both sums. Equations [(Setup-C.8)](#eq-setup-c-8)--[(Setup-C.11)](#eq-setup-c-11) require a carrier bound at one endpoint,
not a hypothesized bound on an unknown numerical trajectory.

<a id="setup-core-3"></a>
##### Uniform complex carriers for the true reference

The early source event supplies the complex carrier maximum

\[
M_0=K_{\rm src}S\sqrt{\log(en)}
\]

through \(T_0=32\lambda^{-1}\log(en)\), including the short complex
time pieces. The late-extension proof puts every later complex disk in the
fixed safe parameter ball about \(\theta(T_0)\) and gives

<a id="eq-setup-c-12"></a>
\[
\|\theta(\zeta)-\theta(T_0)\|_2\le Z_n,
\quad
Z_n=\left(\frac{2Y}{\sqrt\lambda}
       +8Y\sqrt{\mathcal K}\,r_t\right)(en)^{-16}.
\tag{Setup-C.12}
\]

Here \(\mathcal K\) is the explicit source Gram bound in [the preceding Harmonic construction](#harmonic-construction).
The existing extension gate makes this distance less than half the radius
of that ball. Its straight parameter segments are in the safe half-strip.
Use [(Setup-C.9)](#eq-setup-c-9), anchored at \(\theta(T_0)\), and convert RMS to a coordinate
bound. Thus at every real anchor's disk of radius \(r_t/2\), for all
training carriers,

<a id="eq-setup-c-13"></a>
\[
\max_{a,j,i}|k_{a,i}^{(j)}(\zeta)|\le M_c,
\qquad M_c=M_0+\sqrt n\,\kappa_*(M_0)Z_n.
\tag{Setup-C.13}
\]

At fixed positive admissible labels and other structural parameters,
\(M_c=O(\sqrt{\log(en)})\). This derivation fills the possible
late-complex-carrier gap without another stochastic event or another label
restriction. It does not assert that arbitrary points in the full late
parameter ball have that maximum.

<a id="setup-core-4"></a>
##### A complex restart disk from a nearby real anchor

Define the parameter tube radius, Lipschitz coefficient, disk radius, and
velocity bound by

\[
b_n=\min\left\{\frac14,\frac{a}{16\sqrt nP_*},
                    \frac1{\sqrt n\kappa_*(M_c)}\right\},
\]
<a id="eq-setup-c-14"></a>
\[
L_n=2G^2+2(2Y+G)J(M_c+1),\qquad
R_n=\min\{r_t/2,(4L_n)^{-1}\},\qquad V=2G(2Y+G).
\tag{Setup-C.14}
\]

The use of \(b_n\) here is local to this component; it is not the differently
defined late-extension radius in [the preceding Harmonic construction](#harmonic-construction). At fixed parameters,

<a id="eq-setup-c-15"></a>
\[
b_n^{-1}=O(\sqrt{n\log(en)}),\quad
L_n=O(\sqrt{\log(en)}),\quad
R_n^{-1}=O(\sqrt{\log(en)}).
\tag{Setup-C.15}
\]

Fix a real time \(t\ge0\). On \( |\zeta|\le R_n\), consider the
moving parameter balls centered at \(\theta(t+\zeta)\) with radius
\(b_n\). Every such ball lies in the activation domain. To prove this,
follow a straight parameter segment from its center, stopped at first
half-strip exit. The forward bounds [(Setup-C.8)](#eq-setup-c-8) apply before that exit, and each
coordinate changes by at most
\(\sqrt nP_*b_n\le a/16\). Its center has imaginary parts at most
\(3a/8\), so the result stays below \(7a/16<a/2\) and the alleged first exit cannot occur. Operator caps eleven and
readout cap \(R\) also hold since the change is at most \(1/4\).

Equation [(Setup-C.9)](#eq-setup-c-9) and [(Setup-C.13)](#eq-setup-c-13) show that every state in each moving ball has carrier
maximum at most
\(M_c+\sqrt n\kappa_*(M_c)b_n\le M_c+1\).
The segment between any two states in the ball remains in it. Their residual
RMS is at most \(2Y+Gb_n\le2Y+G\). Hence [(Setup-C.11)](#eq-setup-c-11) proves the uniform,
genuine pairwise Lipschitz bound \(L_n\) throughout each ball. This is
where control at the exact complex endpoint is converted into a usable
neighborhood for numerical restarts.

Let the real restart value \(u_0\) satisfy

<a id="eq-setup-c-16"></a>
\[
\|u_0-\theta(t)\|_2\le b_n/4.
\tag{Setup-C.16}
\]

On the Banach space of vector functions continuous on the closed disk and
holomorphic inside it, with supremum norm at most \(b_n\), define

<a id="eq-setup-c-17"></a>
\[
(\mathcal Te)(\zeta)=u_0-\theta(t)
 +\int_0^\zeta
 [F(\theta(t+z)+e(z))-F(\theta(t+z))]\,dz.
\tag{Setup-C.17}
\]

The integrand is holomorphic, so its integral is independent of path in the
disk; bounding it along the straight radius gives

\[
\|\mathcal Te\|_\infty\le b_n/4+L_nR_nb_n\le b_n/2,
\quad
\|\mathcal Te-\mathcal T\widetilde e\|_\infty
\le\tfrac14\|e-\widetilde e\|_\infty.
\]

Iteration is Cauchy, converges uniformly on the disk, and its limit remains
holomorphic by uniform convergence on every smaller circle and the Cauchy
integral formula. Passing to the integral equation proves existence of its
fixed point; the same contraction inequality proves uniqueness. Consequently
\(v_t(\zeta)=\theta(t+\zeta)+e(\zeta)\) solves [(Setup-C.2)](#eq-setup-c-2) and starts at
\(u_0\). Moreover,

<a id="eq-setup-c-18"></a>
\[
\|v_t-\theta(t+\cdot)\|_\infty
\le\frac43\|u_0-\theta(t)\|_2\le b_n/3,
\qquad \|v_t'\|_\infty\le V.
\tag{Setup-C.18}
\]

This proof establishes the complex restart disk directly; it does not assume
that analyticity about the exact anchor automatically transfers to a perturbed
anchor. Conjugating the equation and using uniqueness shows \(v_t\) is real
on the real diameter. The exact reference is only a proof device: the algorithm
below computes coefficients from \(u_0\) and the initialized data.

<a id="setup-core-5"></a>
##### Taylor tail, continuous defect, and global error budget

Let \(p_t\) be the degree-\(K\) Taylor polynomial of \(v_t\) about zero.
Since \(\|v_t(\zeta)-u_0\|_2\le VR_n\), its coefficients obey
\(\|[\zeta^k]v_t\|_2\le VR_n^{1-k}\) for \(k\ge1\), by the
vector-valued Cauchy integral formula. On \(0\le h\le R_n/2\), summing
the resulting geometric series and its derivative gives

<a id="eq-setup-c-19"></a>
\[
\|p_t(h)-v_t(h)\|_2\le VR_n2^{-K},
\quad
\|p_t'(h)-v_t'(h)\|_2\le V(2K+4)2^{-K}.
\tag{Setup-C.19}
\]

If \(VR_n2^{-K}\le b_n/3\), the polynomial and the exact restarted
solution stay in the same moving ball, so [(Setup-C.11)](#eq-setup-c-11) applies to them. Since
\(L_nR_n\le1/4\), their continuous ODE defect satisfies

<a id="eq-setup-c-20"></a>
\[
\|p_t'(h)-F(p_t(h))\|_2
\le V(2K+5)2^{-K}.
\tag{Setup-C.20}
\]

For clarity, the real defect-stability constants imported from
[signed defect stability](#setup-stability) are reproduced here with a superscript
\({\rm r}\) so they are not confused with [(Setup-C.6)](#eq-setup-c-6)--[(Setup-C.7)](#eq-setup-c-7). Put

\[
H_1^{\rm r}=\max(1,b+10s),\quad
H_j^{\rm r}=\max(1,b+10sH_{j-1}^{\rm r}),\quad H^{\rm r}=H_L^{\rm r},
\]
\[
R^{\rm r}=1+2Y/\sqrt\lambda,\quad
B^{\rm r}=R^{\rm r}s(10s)^{L-1},\quad
F_z^{\rm r}=H^{\rm r}(10s)^{L-1},\quad
P^{\rm r}_{\rm layer}=1+(L-1)H^{\rm r},
\]
\[
D^{\rm r}(M)=(10s)^{L-1}\{s(1+B^{\rm r})+Lt_2F_z^{\rm r}M\},
\]
\[
J^{\rm r}(M)=\sqrt{L+1}\{P^{\rm r}_{\rm layer}D^{\rm r}(M)
 +[1+(L-1)B^{\rm r}]sF_z^{\rm r}\},
\]
<a id="eq-setup-c-21"></a>
\[
C^{\rm r}(M)=sF_z^{\rm r}\sqrt L+LB^{\rm r}sF_z^{\rm r}
 +\tfrac12L^2t_2(F_z^{\rm r})^2M.
\tag{Setup-C.21}
\]

Use \(M=2K_{\rm src}S\sqrt{\log(en)}\), and abbreviate the last two
values by \(J^{\rm r},C^{\rm r}\). Define

\[
A_n=4J^{\rm r}Y/\lambda,\qquad K_q=R^{\rm r}(10s)^{L-1},
\]
<a id="eq-setup-c-22"></a>
\[
C_{\rm src}=8\sqrt{L+1}\max\{sF_z^{\rm r},
(10s)^{L-1}[s(1+B^{\rm r})+Lt_2F_z^{\rm r}K_q]\}.
\tag{Setup-C.22}
\]

The real lemma states: for an absolutely continuous numerical path \(u\),
let \(d=u'-F(u)\) and
\(E_0=\|u(0)-\theta(0)\|_2+\int_0^T\|d\|_2dt\). If

<a id="eq-setup-c-23"></a>
\[
E_0\le e^{-A_n}/4,\qquad
8(C^{\rm r}+J^{\rm r})^2T e^{2A_n}E_0^2\le1,
\tag{Setup-C.23}
\]

then \(\sup_{[0,T]}\|u-\theta\|_2\le2e^{A_n}E_0\). Its proof keeps
the negative sample prediction-error square before applying the scalar energy
inequality; it is not the exponential of a worst-case Jacobian times \(T\).
The signed-stability proof above proves each coordinate of [(Setup-C.4)](#eq-setup-c-4), including initialized images,
has error at most \(C_{\rm src}n\|u-\theta\|_2\) on the whole real
query sphere. This uses only deterministic query RMS bounds, and hence does
not need passive-query carrier maxima.

For \(T>0\), choose the following total allowed defect:

<a id="eq-setup-c-24"></a>
\[
\varepsilon_d=e^{-A_n}\min\left\{
\frac14,\ \frac1{\sqrt8(C^{\rm r}+J^{\rm r})\sqrt T},
\frac{\delta_{\rm node}}{2C_{\rm src}n},\ \frac{b_n}{8}\right\}.
\tag{Setup-C.24}
\]

Choose the explicit integer

<a id="eq-setup-c-25"></a>
\[
K=\max\left\{8,
\left\lceil2\log_2\max\{1,4TV/\varepsilon_d\}\right\rceil,
\left\lceil\log_2\max\{1,3VR_n/b_n\}\right\rceil\right\}.
\tag{Setup-C.25}
\]

For \(K\ge8\), \(2K+5\le4\,2^{K/2}\): it holds at eight, and the
ratio of the left side at \(K+1\) to its value at \(K\) is less than
\(\sqrt2\). Thus [(Setup-C.25)](#eq-setup-c-25) ensures both

<a id="eq-setup-c-26"></a>
\[
TV(2K+5)2^{-K}\le\varepsilon_d,
\qquad VR_n2^{-K}\le b_n/3.
\tag{Setup-C.26}
\]

Set \(N_{\rm step}=\lceil2T/R_n\rceil\), and divide \([0,T]\) into
that many equal panels. Initialize \(u(0)=\theta(0)\). On each panel compute
the degree-\(K\) Taylor polynomial from its already computed initial value,
and take its endpoint as the next initial value. This creates a continuous,
piecewise polynomial, absolutely continuous real path.

This procedure is well defined through the whole horizon. Inductively, all
already constructed panels have defect bounded by [(Setup-C.20)](#eq-setup-c-20), so their total defect
is at most \(\varepsilon_d\). The real stability lemma, applied to that
prefix with the conservative full-horizon constants in [(Setup-C.23)](#eq-setup-c-23)--[(Setup-C.24)](#eq-setup-c-24), gives

<a id="eq-setup-c-27"></a>
\[
\|u(t)-\theta(t)\|_2\le2e^{A_n}\varepsilon_d\le b_n/4
\tag{Setup-C.27}
\]

at its final endpoint. Thus the next panel satisfies the restart hypothesis
[(Setup-C.16)](#eq-setup-c-16), and [(Setup-C.19)](#eq-setup-c-19)--[(Setup-C.20)](#eq-setup-c-20) give the same defect bound for that panel. The initial
case is exact. Finite induction constructs every panel; no assumption about
the yet-uncomputed numerical path has been used. Applying the same estimate
on the completed interval proves

<a id="eq-setup-c-28"></a>
\[
\sup_{0\le t\le T}\|u(t)-\theta(t)\|_2
\le\frac{\delta_{\rm node}}{C_{\rm src}n}.
\tag{Setup-C.28}
\]

For polynomial nodal accuracy and \(T=O(\log(en))\), [(Setup-C.15)](#eq-setup-c-15), [(Setup-C.21)](#eq-setup-c-21)--[(Setup-C.24)](#eq-setup-c-24)
give

<a id="eq-setup-c-29"></a>
\[
\log(1/\varepsilon_d)=O(\log(en)),\qquad
K=O(\log(en)),\qquad
N_{\rm step}=O((\log(en))^{3/2}).
\tag{Setup-C.29}
\]

The full dependence on depth, sample count, gap, labels, strip width and
activation bounds remains in the displayed constants. No additional smallness
condition on the labels was imposed. The \(Y=0\) case has stationary zero
readout and zero predictor and uses the original exact zero-label branch.

<a id="setup-core-6"></a>
##### Computable Taylor coefficients and paired source values

On a panel write \(u(h)=\sum_{k=0}^K u_kh^k\). Compute successively

<a id="eq-setup-c-30"></a>
\[
u_{k+1}=\frac{[h^k]F(\sum_{i=0}^ku_ih^i)}{k+1},
\qquad 0\le k<K.
\tag{Setup-C.30}
\]

At stage \(k\), every input coefficient on the right side has already been
computed. The forward pass, backward pass and rank-one updates in [(Setup-C.1)](#eq-setup-c-1)--[(Setup-C.2)](#eq-setup-c-2)
give its coefficient by finite additions, scalar multiplications and truncated
series compositions. Induction identifies these coefficients with the Taylor
coefficients of the unique local solution proved above. The algorithm needs
neither exact anchors nor samples of the unknown exact path.

At a requested real time node, evaluate the current panel polynomial by
Horner's rule and perform the ordinary dense forward/backward pass at each
requested passive query. Form every paired image by multiplying that computed
base vector by its initialized matrix. For example, define

<a id="eq-setup-c-31"></a>
\[
\widetilde h^{(j)}=h^{(j)}(u(t),v),\qquad
\widetilde{W_0^{(j)}h^{(j-1)}}
=W_0^{(j)}\widetilde h^{(j-1)},
\tag{Setup-C.31}
\]

and do the same for the reverse image of \(\widetilde\delta\). Equations
[(Setup-C.22)](#eq-setup-c-22), [(Setup-C.28)](#eq-setup-c-28) give the required separate coordinate error
\(\delta_{\rm node}\) for every family. Pairing is an exact algebraic
identity. Applying identical scalar quadrature, cosine normalization and mode
restriction to both members preserves it. Passive-query Taylor jets are not
needed.

The numerical path need not itself be globally analytic across restart points.
Quadrature accuracy is proved for the exact source function, and its finite
sum is then perturbed by the nodal error [(Setup-C.5)](#eq-setup-c-5). Therefore the piecewise
representation does not invalidate the analytic coefficient-quadrature proof.

<a id="setup-activation"></a>
#### Real-value activation backend

<a id="setup-activation-1"></a>
##### Domain to be approximated

Use \(P_*,G,L_n,b_n,V,M_c,Z_n\) from equations
[(Setup-C.6)](#eq-setup-c-6)--[(Setup-C.14)](#eq-setup-c-14) of [the local-continuation proof](#setup-core), with the
\(b_n\le a/(16\sqrt nP_*)\). Thus the exact network throughout every moving
parameter ball has preactivation imaginary parts at most \(7a/16\).

We need a bound on preactivation real parts for every real query, including
when the parameters are on a complex time disk. Let
\(H_{\max}^{\rm src}=\max_jH_j^{\rm src}\),
\(G_d=16\sqrt{d+3}\), and let \(U\) be the explicit source coefficient in
(S.25) of [the preceding Harmonic construction](#harmonic-construction). One sufficient bound at the exact disk centers is

<a id="eq-setup-a-1"></a>
\[
Z_*=(K_{\rm src}+G_dH_{\max}^{\rm src}+1+US^2)\sqrt{\log(en)}
       +a/8+\sqrt nP_*Z_n.
\tag{Setup-A.1}
\]

Indeed the initial whole-sphere coordinate bound is
\((G_dH_{\max}^{\rm src}+1)\sqrt{\log(en)}\). The real velocity bound
\(|\partial_tz_i^{(j)}|\le2\rho SU\sqrt{\log(en)}\), integrated using the
source activity bound \(\int2\rho\,dt\le S/2\), adds at most
\(US^2\sqrt{\log(en)}\). The short complex time pieces add at most
\(8YSUr_t\sqrt{\log(en)}=a/8\). After \(T_0\), compare with
\(\theta(T_0)\) in the late safe ball; the forward endpoint estimate adds
at most \(\sqrt nP_*Z_n\). The extra \(K_{\rm src}\sqrt{\log(en)}\) in [(Setup-A.1)](#eq-setup-a-1)
also covers the early training-coordinate maximum. Only real query
vectors are needed here; no polynomial is evaluated on a complex query sphere.

Every original preactivation at a state in one of the moving balls therefore
satisfies

<a id="eq-setup-a-2"></a>
\[
|\operatorname{Re}z|\le Z_*+a/16,\qquad
|\operatorname{Im}z|\le7a/16.
\tag{Setup-A.2}
\]

At fixed structural parameters, \(Z_*=O(\sqrt{\log(en)})\). Define

<a id="eq-setup-a-3"></a>
\[
B=8(Z_*+a+1),\qquad
\tau_o=\operatorname{arsinh}\frac{31a}{64B},\qquad
\tau_i=\operatorname{arsinh}\frac{29a}{64B},\qquad
\Delta=\tau_o-\tau_i.
\tag{Setup-A.3}
\]

For \(\tau>0\), write \(\mathcal E_\tau\) for the filled ellipse with boundary
\(z=B(w+w^{-1})/2,\ |w|=e^\tau\). Its semiaxes are \(B\cosh\tau\)
and \(B\sinh\tau\). The outer ellipse is strictly inside the activation
half-strip because its imaginary semiaxis is \(31a/64<a/2\).
Moreover \(B\ge8a\), so

<a id="eq-setup-a-4"></a>
\[
0<\Delta<1,\qquad \Delta\ge\frac{a}{64B},\qquad \tau_o<1.
\tag{Setup-A.4}
\]

For the lower bound, integrate the derivative of \(\operatorname{arsinh}x\)
between \(29a/(64B)\) and \(31a/(64B)\); it is at least \(1/2\)
on that interval.

The inner ellipse contains every disk of radius \(a/512\) around every point
at distance at most \(a/512\) from a point of [(Setup-A.2)](#eq-setup-a-2). Its real coordinate
divided by its real semiaxis is at most \(1/8\), while its imaginary
coordinate divided by the imaginary semiaxis is at most
\((7/16+2/512)/(29/64)=226/232\). Their squared sum is less than one.
This verifies the domain for activation substitution and derivative
estimation below, with strict margin.

<a id="setup-activation-2"></a>
##### Explicit real-node Chebyshev construction

Let \(b=\max_j|\phi_j(0)|\) and let \(s\) be the original first-derivative
bound on the half-strip. On \(\mathcal E_{\tau_o}\),

<a id="eq-setup-a-5"></a>
\[
|\phi_j(z)|\le M_\phi,\qquad M_\phi=b+s(B+a).
\tag{Setup-A.5}
\]

Integrate the bounded derivative on the segment from zero to \(z\), which
lies in the half-strip, and use \(|z|\le B\cosh\tau_o\le B+a\).

Fix a desired value/first/second derivative accuracy \(\epsilon>0\), and put

\[
C_a=\max\{1,512/a,2(512/a)^2\},\qquad
\epsilon_p=\epsilon/C_a,
\]
<a id="eq-setup-a-6"></a>
\[
D=\max\left\{1,\left\lceil
 \Delta^{-1}\log\max\{e,24M_\phi/(\epsilon_p\Delta)\}
 \right\rceil\right\},\qquad N_\phi=4(D+1).
\tag{Setup-A.6}
\]

At the real nodes \(x_r=B\cos(2\pi r/N_\phi)\), evaluate the original
activation. Define

\[
\widetilde c_0=\frac1{N_\phi}\sum_{r=0}^{N_\phi-1}\phi_j(x_r),
\qquad
\widetilde c_k=\frac2{N_\phi}\sum_{r=0}^{N_\phi-1}
       \phi_j(x_r)\cos(2\pi kr/N_\phi),\quad 1\le k\le D,
\]
<a id="eq-setup-a-7"></a>
\[
\psi_j(z)=\sum_{k=0}^D\widetilde c_k T_k(z/B),
\tag{Setup-A.7}
\]

where \(T_k(\cos u)=\cos(ku)\). Thus \(\psi_j\) has real coefficients
and is computed from \(N_\phi\) real calls to \(\phi_j\).

Here is the error estimate, including the finite coefficient rule.
For \(g(u)=\phi_j(B\cos u)\), shifting a Fourier contour within
\(|\operatorname{Im}u|\le\tau_o\) gives
\(|\widehat g_k|\le M_\phi e^{-|k|\tau_o}\). The function is even.
Its Chebyshev coefficients are \(c_0=\widehat g_0\) and
\(c_k=2\widehat g_k\) for \(k\ge1\). Also
\(|T_k(z/B)|\le e^{k\tau_i}\) on \(\mathcal E_{\tau_i}\), by its
Laurent formula on the ellipse boundary and the maximum modulus principle.
Consequently the degree-\(D\) exact coefficient tail is at most

<a id="eq-setup-a-8"></a>
\[
\frac{2M_\phi e^{-(D+1)\Delta}}{1-e^{-\Delta}}
\le \frac{4M_\phi}{\Delta}e^{-(D+1)\Delta}.
\tag{Setup-A.8}
\]

Absolute Fourier convergence permits interchange with the finite sum. The
discrete Fourier coefficient is
\(\sum_{q\in\mathbb Z}\widehat g_{k+qN_\phi}\), since the discrete sum of
\(e^{i\ell u}\) vanishes unless \(N_\phi\) divides \(\ell\). For
\(0\le k\le D<N_\phi/2\), this gives

\[
|\widetilde c_k-c_k|
\le\frac{4M_\phi e^{-(N_\phi-D)\tau_o}}
           {1-e^{-N_\phi\tau_o}}.
\]

The factor four safely includes the constant coefficient. Since
\((D+1)\Delta\ge1\), the denominator is at least \(1/2\). Summing the
coefficient error on the inner ellipse and using \(N_\phi=4(D+1)\) yields

<a id="eq-setup-a-9"></a>
\[
\left|\sum_{k=0}^D(\widetilde c_k-c_k)T_k(z/B)\right|
\le8M_\phi(D+1)e^{-2(D+1)\tau_o}
\le\frac{8M_\phi}{\Delta}e^{-(D+1)\Delta}.
\tag{Setup-A.9}
\]

For the last inequality use \(x e^{-x}\le1\) with
\(x=(D+1)\tau_o\), and \(\tau_o\ge\Delta\).
Equations [(Setup-A.6)](#eq-setup-a-6), [(Setup-A.8)](#eq-setup-a-8)--[(Setup-A.9)](#eq-setup-a-9) show that
\(\sup_{\mathcal E_{\tau_i}}|\psi_j-\phi_j|\le\epsilon_p/2\).

The reserved half also permits inexact real value calls: if each value in
[(Setup-A.7)](#eq-setup-a-7) has absolute error at most

<a id="eq-setup-a-10"></a>
\[
\epsilon_{\rm eval}=
\frac{\epsilon_p}{4(D+1)e^{D\tau_i}},
\tag{Setup-A.10}
\]

the resulting extra polynomial error on the inner ellipse is at most
\(\epsilon_p/2\). Bound every coefficient perturbation
by \(2\epsilon_{\rm eval}\) and sum \(D+1\) terms.

Cauchy's integral formula on the disks checked after [(Setup-A.4)](#eq-setup-a-4) gives, at every
point at distance at most \(a/512\) from the rectangle [(Setup-A.2)](#eq-setup-a-2),

<a id="eq-setup-a-11"></a>
\[
|\psi_j-\phi_j|\le\epsilon,\qquad
|\psi_j'-\phi_j'|\le\epsilon,\qquad
|\psi_j''-\phi_j''|\le\epsilon.
\tag{Setup-A.11}
\]

The derivative factors are \(512/a\) and \(2(512/a)^2\), precisely those
included in \(C_a\). Exact calls make [(Setup-A.10)](#eq-setup-a-10) unnecessary; finite-accuracy calls
only require polynomially small error in the regime analyzed below.

<a id="setup-activation-3"></a>
##### Error in the training vector field

Replace every activation by \(\psi_j\) only in a disposable setup network,
and call its gradient-flow vector field \(\widetilde F\). We compare this
polynomial field to \(F\) at the same parameter value \(u\) in a moving
ball of [the local-continuation proof](#setup-core). Use the core coefficients \(H_j,B_j\), and define

<a id="eq-setup-a-12"></a>
\[
U_0=0,\qquad U_j=1+11sU_{j-1},\qquad U_*=\max_jU_j,
\qquad K_j=R(11s)^{L-j}.
\tag{Setup-A.12}
\]

Superscripts \(0\) and \(p\) below distinguish the original and polynomial
activation evaluations at this one parameter state. If

<a id="eq-setup-a-13"></a>
\[
\epsilon\le\min\left\{1,U_*^{-1},
       \frac{a}{5632\sqrt nU_*}\right\},
\tag{Setup-A.13}
\]

then induction over the layers gives

<a id="eq-setup-a-14"></a>
\[
\frac{\|h^{p,(j)}-h^{0,(j)}\|_2}{\sqrt n}\le U_j\epsilon,
\qquad
\frac{\|z^{p,(j)}-z^{0,(j)}\|_2}{\sqrt n}
 \le11U_{j-1}\epsilon.
\tag{Setup-A.14}
\]

The first preactivations agree. At the next layer the unchanged matrix costs
eleven, and the activation difference splits into its error at the polynomial
argument plus the original activation's \(s\)-Lipschitz change. Every
preactivation coordinate discrepancy is at most
\(11\sqrt nU_*\epsilon\le a/512\), so [(Setup-A.11)](#eq-setup-a-11) applies at every induction
step. Also \(\|h^{p,(j)}\|_2/\sqrt n\le H_j+1\).

For \(M\ge0\), define backward error coefficients by descending recursion:

<a id="eq-setup-a-15"></a>
\[
Q_{L+1}(M)=0,\qquad
Q_j(M)=11(s+1)Q_{j+1}(M)+K_j+11t_2M U_{j-1}.
\tag{Setup-A.15}
\]

If the original carriers at \(u\) have maximum \(M\), then

<a id="eq-setup-a-16"></a>
\[
\frac{\|\delta^{p,(j)}-\delta^{0,(j)}\|_2}{\sqrt n}
\le Q_j(M)\epsilon.
\tag{Setup-A.16}
\]

The changed carrier costs \(11Q_{j+1}\epsilon\) at \(j<L\), while
at \(j=L\) it is zero. The polynomial gate has modulus at most \(s+1\).
The gate discrepancy multiplied by the original carrier contributes
\(\epsilon K_j+t_2M(11U_{j-1}\epsilon)\), by [(Setup-A.11)](#eq-setup-a-11) and [(Setup-A.14)](#eq-setup-a-14).
These are exactly the terms in [(Setup-A.15)](#eq-setup-a-15).

For the training vector field take \(M=M_c+1\). Set

\[
Q_\xi=U_L+Q_1(M)+
\sum_{j=2}^L\{Q_j(M)(H_{j-1}+1)+B_jU_{j-1}\},
\qquad Q_f=RU_L,
\]
<a id="eq-setup-a-17"></a>
\[
C_F=2Q_f(G+1)+2(2Y+G)Q_\xi.
\tag{Setup-A.17}
\]

Subtracting the gradient blocks gives
\(\|\widetilde\xi_a-\xi_a\|_2\le Q_\xi\epsilon\).
Subtracting the predictions gives
\(|\widetilde f_a-f_a|\le Q_f\epsilon\).
If also \(Q_\xi\epsilon\le1\), the polynomial gradient norm is at most
\(G+1\). Splitting the factors in the residual-gradient product in [(Setup-C.2)](#eq-setup-c-2)
of [the local-continuation proof](#setup-core), and using the original residual bound \(2Y+G\), proves

<a id="eq-setup-a-18"></a>
\[
\sup_{\text{moving ball}}\|\widetilde F-F\|_2
\le C_F\epsilon.
\tag{Setup-A.18}
\]

All training constants in [(Setup-A.15)](#eq-setup-a-15)--[(Setup-A.18)](#eq-setup-a-18) grow at most like
\(O(\sqrt{\log(en)})\) at fixed structural parameters.

<a id="setup-activation-4"></a>
##### Modified restart and a combined defect budget

Keep the real signed-stability constants \(A_n,C^{\rm r},J^{\rm r}\)
and \(C_{\rm src}\) from [the local-continuation proof](#setup-core). For a positive source horizon \(T\)
and target nodal error \(\delta_{\rm node}\), define

\[
e_d=e^{-A_n}\min\left\{\frac14,
 \frac1{\sqrt8(C^{\rm r}+J^{\rm r})\sqrt T},
 \frac{\delta_{\rm node}}{4C_{\rm src}n},\frac{b_n}{16}\right\},
\]
<a id="eq-setup-a-19"></a>
\[
\zeta_F=\min\{e_d/(2T),b_nL_n/4,V/2\},\qquad
\widehat R_n=\min\{r_t/2,(8L_n)^{-1}\}.
\tag{Setup-A.19}
\]

Choose \(\epsilon\) satisfying [(Setup-A.13)](#eq-setup-a-13), \(Q_\xi\epsilon\le1\), and
\(C_F\epsilon\le\zeta_F\). A further source-output requirement is imposed in
the next section. Construct the activation polynomials once using [(Setup-A.6)](#eq-setup-a-6)--[(Setup-A.7)](#eq-setup-a-7).

There is a uniform derivative bound for the field perturbation in each ball
of radius \(b_n/2\) about the exact complex reference:

<a id="eq-setup-a-20"></a>
\[
\|D(\widetilde F-F)\|_{\rm op}\le2\zeta_F/b_n.
\tag{Setup-A.20}
\]

For a unit complex parameter direction, the disk of radius \(b_n/2\)
about any such state remains in the original ball of radius \(b_n\).
Apply the vector-valued Cauchy integral formula to
\(\widetilde F-F\), using [(Setup-A.18)](#eq-setup-a-18). This proves [(Setup-A.20)](#eq-setup-a-20) without a
dimension-dependent conversion of coordinate derivatives.
The polynomial field is therefore \(2L_n\)-Lipschitz on that smaller ball.

The exact restarted solution of \(\dot v=\widetilde F(v)\) exists on the
complex disk of radius \(\widehat R_n\) whenever its real initial anchor
has distance at most \(b_n/8\) from the true original trajectory.
Repeat the core Picard map for the error, now with integrand
\(\widetilde F(\theta+e)-F(\theta)\) and error ball of radius \(b_n/2\).
Its contraction factor is at most \(2L_n\widehat R_n\le1/4\).
Its forcing at \(e=0\) is at most \(\zeta_F\). The map sends that ball
to radius at most

\[
b_n/8+\widehat R_n\zeta_F+(1/4)(b_n/2)
\le9b_n/32<b_n/2.
\]

The fixed point has error at most
\((b_n/8+b_n/32)/(1-1/4)=5b_n/24<b_n/4\).
Its velocity is at most \(V+\zeta_F\le2V\).
Thus its degree-\(K\) Taylor polynomial, on a half-radius real panel, has
tail at most \(2V\widehat R_n2^{-K}\). If this is at most \(b_n/4\),
the polynomial remains inside the smaller ball. Its defect against the
polynomial field is at most \(2V(2K+5)2^{-K}\), by the same differentiated
geometric series as the core proof. Its defect against the original field is
therefore at most

<a id="eq-setup-a-21"></a>
\[
2V(2K+5)2^{-K}+\zeta_F.
\tag{Setup-A.21}
\]

Choose

<a id="eq-setup-a-22"></a>
\[
K=\max\left\{8,
\left\lceil2\log_2\max\{1,16TV/e_d\}\right\rceil,
\left\lceil\log_2\max\{1,8V\widehat R_n/b_n\}\right\rceil\right\}.
\tag{Setup-A.22}
\]

The first error term in [(Setup-A.21)](#eq-setup-a-21), integrated over the horizon, is at most
\(e_d/2\), because \(2K+5\le4\,2^{K/2}\) for \(K\ge8\).
The second term contributes at most \(e_d/2\) by [(Setup-A.19)](#eq-setup-a-19).
Use \(N_{\rm step}=\lceil2T/\widehat R_n\rceil\) panels and the
explicit coefficient recurrence [(Setup-C.30)](#eq-setup-c-30) of [the local-continuation proof](#setup-core), with
\(\widetilde F\) in place of \(F\).

The prefix induction from the core proof now gives
<a id="eq-setup-a-23"></a>
\[
\sup_{[0,T]}\|u(t)-\theta(t)\|_2
\le2e^{A_n}e_d
\le\min\{b_n/8,\delta_{\rm node}/(2C_{\rm src}n)\}.
\tag{Setup-A.23}
\]
It justifies every successive restart and reserves half
the nodal error for evaluating sources with the activation polynomials.

<a id="setup-activation-5"></a>
##### Source values without derivative calls to the original activations

The original passive-query carrier RMS is at most \(K_j\) throughout the
operator/readout tube. Hence its coordinate maximum is at most
\[
M_q=\sqrt n\max_jK_j.
\]
Use [(Setup-A.15)](#eq-setup-a-15) with \(M=M_q\), and define
<a id="eq-setup-a-24"></a>
\[
C_p=8\sqrt n\max\{U_*,\max_jQ_j(M_q)\}.
\tag{Setup-A.24}
\]
Choose, finally, the single sufficient scalar tolerance
<a id="eq-setup-a-25"></a>
\[
\epsilon=\min\left\{1,U_*^{-1},
\frac{a}{5632\sqrt nU_*},Q_\xi^{-1},
\frac{\zeta_F}{C_F},\frac{\delta_{\rm node}}{2C_p}\right\}.
\tag{Setup-A.25}
\]
All denominators are positive; \(Q_\xi,C_F\) in this expression are
the training constants from [(Setup-A.17)](#eq-setup-a-17).

At each time/query node evaluate the network at \(u(t)\), using
\(\psi_j,\psi_j'\). Equations [(Setup-A.14)](#eq-setup-a-14), [(Setup-A.16)](#eq-setup-a-16), and RMS-to-coordinate
conversion show that the coordinate error from replacing the activations is
at most \(\sqrt n\max(U_*,\max_jQ_j(M_q))\epsilon\). Initialized
image actions cost at most eight in Euclidean norm, so every family, including
each image, has error at most \(C_p\epsilon\le\delta_{\rm node}/2\).
The original-activation source at \(u(t)\) differs from its true source at
\(\theta(t)\) by at most the other half, by [(Setup-A.23)](#eq-setup-a-23) and the core source
comparison. Every family has the required total coordinate tolerance.

Form initialized images directly from their computed base vectors. Pairing
therefore remains exact, and identical scalar coefficient quadrature preserves
it. The approximated training field and passive evaluations do
not introduce independent approximations to members of a pair.

The exact initialized additions to the source spaces are a separate operation:
evaluate their features with the original \(\phi_j\), and form their original
matrix images exactly in the same exact-real model as [the preceding Harmonic construction](#harmonic-construction). These take
\(O(Lmn)\) real activation-value calls and \(O(mP)\) arithmetic. Initial
backward fields vanish because the readout is zero. No derivative call to the
original activation is required by this setup backend. The final compressed
network still evaluates the original activation and derivative during its
specified runtime; the polynomials are discarded after setup.

<a id="setup-activation-6"></a>
##### Degree, cost, and the ordinary Euler comparison

Fix the full admissible structural parameters, take
\(T=O(\log(en))\), and let \(\log(1/\delta_{\rm node})=O(\log(en))\).
Then [(Setup-A.19)](#eq-setup-a-19), [(Setup-A.24)](#eq-setup-a-24)--[(Setup-A.25)](#eq-setup-a-25) imply
\(\log(1/\epsilon)=O(\log(en))\): \(C_p=O(n)\), the training error
coefficients are \(O(\sqrt{\log(en)})\), and
\(e^{A_n}=\exp(O(\sqrt{\log(en)}))\). Equations [(Setup-A.3)](#eq-setup-a-3)--[(Setup-A.6)](#eq-setup-a-6) give
<a id="eq-setup-a-26"></a>
\[
D=O(\log(en)^{3/2}),\quad N_\phi=O(\log(en)^{3/2}),\quad
K=O(\log(en)),\quad N_{\rm step}=O(\log(en)^{3/2}).
\tag{Setup-A.26}
\]
Also \(D\tau_i=O(\log(en))\), so the sufficient value-call accuracy
[(Setup-A.10)](#eq-setup-a-10) is polynomially small in \(n\). This is a precision requirement,
not a proof about a particular floating-point library.

Computing the coefficients in [(Setup-A.7)](#eq-setup-a-7) by cosine recurrences costs \(O(LD^2)\)
arithmetic and \(O(LD)\) retained coefficient words. It uses
\(O(LD)\) scalar activation calls and trigonometric calls at real arguments.
No complex activation values or high derivatives are requested.

Convert each Chebyshev polynomial to ordinary polynomial coefficients, or
evaluate its truncated series by the three-term Chebyshev recurrence.
Both give \(O(DK^2)\) arithmetic for one online degree-\(K\) scalar
composition, and \(O(DK)\) sufficient workspace. Each of the
\(D\) recurrence products is a convolution; accumulating its successive
coefficients through \(K\) costs \(\sum_{k\le K}O(k)=O(K^2)\).
The derivative polynomial can be prepared in \(O(D^2)\) arithmetic and
evaluated with the same bound.

Let \(N_t,N_x\) be the certified time/spatial quadrature node counts.
Including polynomial passive-query evaluations, a sufficient source-value
arithmetic bound is
<a id="eq-setup-a-27"></a>
\[
O\!\left(
LD^2+N_{\rm step}[mPK^2+LmnDK^2]
+PKN_t+PN_tN_x+LnDN_tN_x+mP
\right).
\tag{Setup-A.27}
\]
In addition, there are \(O(LD+Lmn)\) original scalar activation-value
calls and \(O(LD)\) elementary trigonometric calls. A sufficient streamed
memory bound, before adding the unchanged source coefficient/selection arrays,
is
<a id="eq-setup-a-28"></a>
\[
O(PK+LmnDK+LD+Ln).
\tag{Setup-A.28}
\]
At fixed parameters all arithmetic and call counts in [(Setup-A.27)](#eq-setup-a-27)--[(Setup-A.28)](#eq-setup-a-28),
and the certified quadrature/selection/assembly costs, are
\(n^{2+o(1)}\). If scalar activation values are unit-cost primitives,
this is the total arithmetic bound. If a concrete value routine is supplied,
add its explicitly requested costs at the arguments and tolerances above.
Nothing assumes an arbitrary analytic activation has an efficient
representation merely because it satisfies a strip bound.

For the specified Euler comparison, ordinary explicit Euler with numerical step
\(h\) over physical horizon \(T\) takes
\(\Theta(mPT/h)\) arithmetic before query/source processing, up to its
activation costs. If its accuracy requirement calls for \(h=n^{-1/2}\)
at fixed structural parameters, that work is \(n^{5/2+o(1)}\);
the present high-order setup has \(n^{2+o(1)}\) work. This is a conditional
comparison using the stated Euler step requirement. The theorem does not
claim that every dense solver must use such a step, or prove a lower bound
against high-order dense solvers. It shows that covering the full physical
source horizon need not carry the width-dependent first-order time-step cost.

<a id="setup-assembly"></a>
#### Streamed explicit assembly

<a id="setup-assembly-1"></a>
##### Conditional input and unchanged output

Let $L,m,d,n$ denote hidden depth, training sample count, input dimension and
hidden width. Inputs are $v=x/\sqrt d\in S^{d-1}$. Retain the exact dense
architecture, loss, mobilities, zero initial readout and full original label
allowance from [the preceding Harmonic construction](#harmonic-construction). Thus, with $A=W^{(1)}$ and $w=W^{(L+1)}$,

\[
z^{(1)}=Av,\quad z^{(j)}=W^{(j)}h^{(j-1)},\quad
h^{(j)}=\phi_j(z^{(j)}),\quad f_n=w^Th^{(L)}/n,
\]
\[
\delta^{(L)}=w\odot\phi_L'(z^{(L)}),\qquad
\delta^{(j)}=\phi_j'(z^{(j)})\odot
                  W^{(j+1)T}\delta^{(j+1)}.
\]

A passive query uses the current trained parameters and does not enter the
training residuals or parameter updates. Write

\[
P=(L-1)n^2+n(d+1)
\]

for the dense parameter count. We use the existing cost convention
$n\ge\max(m,d)$, numerical big-O constants, and exact-real arithmetic.
Activation and Gaussian-generation costs are accounted for separately.

Take a permitted source horizon $T\ge T_0>0$ and tolerance
$0<\eta\le\eta_0$. To avoid a collision with the number of panels, let
$\ell_*$ denote the largest retained spherical degree, and put

\[
h_\ell={\ell+d-1\choose d-1}-{\ell+d-3\choose d-1},\qquad
H_{\rm sph}=\sum_{\ell=0}^{\ell_*}h_\ell,\qquad
\mathcal Y=\max_{\ell\le\ell_*}\sqrt{h_\ell}
\]

when $d\ge2$. The original weighted simplex is retained exactly:

<a id="eq-setup-e-1"></a>
\[
\Lambda=\{(k,\ell,b):k\ge0,\ \alpha_Tk+r_q\ell\le H(T,\eta),
                   \ 1\le b\le h_\ell\},
\quad N=|\Lambda|,\quad p=\max_\Lambda k.
\tag{Setup-E.1}
\]

The source-generator bound, actual rank and selected-width condition remain

<a id="eq-setup-e-2"></a>
\[
R=2m+d+1+4N,\qquad r=\max_j\dim E_j\le\min(n,R),
\qquad 9r\le q<n.
\tag{Setup-E.2}
\]

The original sufficient budget uses $9R\le q$. For $d=1$, use the
two separate queries $v=\pm1$, $N_x=2$, $H_{\rm sph}=2$,
$p+1=N_1$, and $R=2m+d+1+8N_1$; below $N$ in rectangular
work bounds may be replaced by $2N_1$. No angular quadrature is needed then.

The positive time/sphere rule of [the quadrature proof](#setup-quadrature) has $N_t$ time nodes
$u_a=2\pi a/N_t$, physical times $t_a=T(1+\cos u_a)/2$, and $N_x$
spatial nodes $v_s$. Its spatial weights, including the real angular
Jacobian, are denoted $\omega_s$. They are positive and satisfy

<a id="eq-setup-e-3"></a>
\[
\sum_s\omega_s\le A_d,
\qquad
\epsilon_c=\frac{\eta}{16N\mathcal Y},\qquad
\delta_{\rm node}=\frac{\epsilon_c}{4A_d\mathcal Y}.
\tag{Setup-E.3}
\]

Here $A_d$ is the explicit product of polar normalization factors in the
[quadrature proof](#setup-quadrature); it equals one in dimension two. In dimension one the existing
separate-point definitions are $\epsilon_c=\eta/(16N_1)$ and
$\delta_{\rm node}=\epsilon_c/4$. Exact-value quadrature already has
coefficient error at most $\epsilon_c/2$, and the exact source tail is
at most $\eta/16$.

The conditional integrator supplies consecutive real panels

\[
0=\tau_0<\tau_1<\cdots<\tau_J=T,
\qquad \Delta_b=\tau_{b+1}-\tau_b,
\]

and an approximate dense anchor at each panel's left endpoint. The following
are the precise required properties.

1. At panel $b$, normalized training Taylor coefficients through degree
   $K\ge1$, generated from that anchor using the actual dense ODE, are
   available or can be generated by the recursion counted below. The same
   coefficients advance the anchor to the next panel. Only one anchor and its
   current panel data need remain resident.
2. For every needed passive query, the corresponding forward and backward
   source polynomials can be generated from those shared training jets:
   <a id="eq-setup-e-4"></a>
\[
   \widetilde g_b(t,v_s)=\sum_{c=0}^K G_{b,c}(v_s)
                 ((t-\tau_b)/\Delta_b)^c,
   \quad g\in\{h^{(j)},\delta^{(j)}\}.
   \tag{Setup-E.4}
   \]
   At each assigned quadrature node they satisfy
   <a id="eq-setup-e-5"></a>
\[
   \|\widetilde g_b(t_a,v_s)-g(t_a,v_s)\|_2
                         \le\delta_{\rm node}/8.
   \tag{Setup-E.5}
   \]
   This error includes anchor error, local-series truncation, and any
   approximation by the activation backend. A sufficient coordinatewise
   interface is $\delta_{\rm node}/(8\sqrt n)$ for every coordinate
   of each base source.
3. Panel construction, local error certification and any corrective work not
   included in the explicit recursions have total work $C_{\rm cert}$ and
   additional peak workspace $M_{\rm cert}$. They must be proved small;
   neither implicit solves nor rejected panels are free.

Only the finite node set requires [(Setup-E.5)](#eq-setup-e-5). A uniform local source estimate is a
stronger sufficient input. The local-continuation and activation proofs above
provide the numerical path; [the source-jet bridge](#setup-bridge) below proves
this stronger Euclidean source interface for its polynomial-activation jets.
Thus this conditional assembly lemma applies after that explicit interface
replacement, with no extra numerical-path hypothesis.

<a id="setup-assembly-2"></a>
##### Exact pairing with the initialized mixers

At a learned anchor the degree-zero mixer is $W_b^{(j)}$, whereas source
pairing requires $W_0^{(j)}$. In general

\[
W_b^{(j)}G_{b,c}\ne W_0^{(j)}G_{b,c}.
\]

Consequently the saved dense forward action in the local recursion cannot be
relabelled as an initialized-mixer image. This is the key difference from a
single Taylor recursion at time zero.

Compute global coefficients only for the base fields $h^{(j)}$ and
$\delta^{(j)}$. After all panels have been summed, set

<a id="eq-setup-e-6"></a>
\[
\widetilde c_{k\ell b}^{\,W_0^{(j)}h^{(j-1)}}
       =W_0^{(j)}\widetilde c_{k\ell b}^{\,h^{(j-1)}},\qquad
\widetilde c_{k\ell b}^{\,W_0^{(j+1)T}\delta^{(j+1)}}
       =W_0^{(j+1)T}\widetilde c_{k\ell b}^{\,\delta^{(j+1)}}.
\tag{Setup-E.6}
\]

Every coefficient is a finite scalar linear combination of nodal polynomial
values. Thus [(Setup-E.6)](#eq-setup-e-6) is exactly what would be obtained by applying $W_0$ or its
transpose to every base nodal polynomial before quadrature. This proves exact
coefficient and reconstructed-source pairing without storing image jets or
performing initialized-mixer actions at every node.

Accuracy for the image remains a separate requirement. On the inherited event
$\|W_0^{(j)}\|_{\rm op}\le8$, [(Setup-E.5)](#eq-setup-e-5) gives

<a id="eq-setup-e-7"></a>
\[
\|W_0(\widetilde g-g)\|_\infty
 \le\|W_0\|_{\rm op}\|\widetilde g-g\|_2
 \le\delta_{\rm node}.
\tag{Setup-E.7}
\]

The base source also has coordinate error at most $\delta_{\rm node}$. Apply the
[quadrature proof](#setup-quadrature)'s positive-weight perturbation estimate separately to each
family, using its own exact analytic source. Its coefficient error is at most
$\epsilon_c/2$ from nodal approximation and $\epsilon_c/2$ from quadrature. The source
reconstruction error is therefore at most

<a id="eq-setup-e-8"></a>
\[
\eta/16+N\mathcal Y\epsilon_c=\eta/8<\eta.
\tag{Setup-E.8}
\]

This deliberately pays a factor $\sqrt n$ if the available source estimate is only
coordinatewise. It avoids an invalid dimension-free inference from coordinate
accuracy to image accuracy. At polynomial target accuracy this additional
factor changes the constant multiplying $\log n$ in the precision/degree
requirement, not its order. Alternatively one can certify both polynomial
families directly, but their exact relationship must still be imposed.

There are at most $2(L-1)N$ image columns, so [(Setup-E.6)](#eq-setup-e-6) costs

<a id="eq-setup-e-9"></a>
\[
O(Ln^2N)
\tag{Setup-E.9}
\]

arithmetic. Applying initialized mixers instead to every local source jet would
cost $O(JLn^2N_xK)$. Either bound is legitimate; [(Setup-E.9)](#eq-setup-e-9) avoids that work during
continuation and is convenient for streaming. No claim that [(Setup-E.9)](#eq-setup-e-9) is always
smaller is required.

<a id="setup-assembly-3"></a>
##### Panel-major streaming and the local-to-global transform

Partition the time-node indices into disjoint sets $I_b$, assigning each
$t_a$ to exactly one panel. Repeated physical times from the cosine map may
remain separate quadrature nodes. Their scalar weights are simply both counted.
Sort the nodes in $O(N_t\log(2+N_t))$ work if needed; the monotonic halves of
the cosine grid also allow a linear merge. The continuation proceeds in
increasing physical time, regardless of the original quadrature ordering.

For each panel form the scalar moment table

<a id="eq-setup-e-10"></a>
\[
B^{(b)}_{kc}=\frac{\gamma_k}{N_t}\sum_{a\in I_b}
      \cos(ku_a)((t_a-\tau_b)/\Delta_b)^c,
\qquad \gamma_0=1,\quad \gamma_k=2\ (k\ge1).
\tag{Setup-E.10}
\]

For one base source the global coefficient is exactly

<a id="eq-setup-e-11"></a>
\[
\widetilde c_{k\ell b'}^{\,g}
 =\sum_{b=0}^{J-1}\sum_{s=1}^{N_x}\omega_sY_{\ell,b'}(v_s)
                    \sum_{c=0}^K B^{(b)}_{kc}G_{b,c}^{\,g}(v_s).
\tag{Setup-E.11}
\]

Only $\lambda=(k,\ell,b')\in\Lambda$ is accumulated. In particular, the $J$ local
polynomial descriptions are not added as $J$ new source-space families.
They are integrated into the original global coefficients, so they do not
multiply the rank bound.

The execution order is: generate training jets for one panel; process all
spatial nodes against those jets; add that panel's contribution to [(Setup-E.11)](#eq-setup-e-11);
advance the dense anchor once; discard the panel jets. This requires one dense
continuation pass. Spatial-node-major execution without storing all panels
would repeat the dense training computation $N_x$ times; it is not the
execution costed here.

Powers in [(Setup-E.10)](#eq-setup-e-10) and cosine values can be generated by scalar recurrences. A
safe total moment-table cost, including clearing every panel table, is

<a id="eq-setup-e-12"></a>
\[
T_{\rm moments}=O((N_t+J)(p+1)K),\qquad
M_{\rm moments}=O((p+1)K+N_t+J).
\tag{Setup-E.12}
\]

No conformal-map power composition or $JK^2(p+1)$ term is needed: the
local polynomials are evaluated directly in the local affine coordinate.
Panels containing no quadrature nodes require no passive queries or transform,
although their training continuation still has to be performed.

There are two useful orders for the sums in [(Setup-E.11)](#eq-setup-e-11).

**Temporal first.** For a streamed spatial query, transform its $K+1$ jets
to all $p+1$ temporal modes, then update just the retained coefficients. Over
all panels the work is

<a id="eq-setup-e-13"></a>
\[
T_{\rm proj,t}=O\bigl(LnJN_x[(p+1)K+N]\bigr).
\tag{Setup-E.13}
\]

Beyond the jets and final coefficient arrays, the vector buffer is
$O(Ln(p+1))$, which fits within $O(LnR)$.

**Spatial first.** For the current panel accumulate spherical coefficients of
each local jet,

\[
S_{c\ell b'}^{\,g}=\sum_s\omega_sY_{\ell,b'}(v_s)G_{b,c}^{\,g}(v_s).
\]

Then transform only the final retained pairs using [(Setup-E.10)](#eq-setup-e-10). The work and extra
vector buffer are

<a id="eq-setup-e-14"></a>
\[
T_{\rm proj,x}=O\bigl(LnJK[N_xH_{\rm sph}+N]\bigr),\qquad
M_{\rm proj,x}=O(LnKH_{\rm sph}).
\tag{Setup-E.14}
\]

These are alternative implementations, with the displayed memory attached to
the chosen one. They are not simultaneous minima. Degree-dependent temporal
cutoffs are used when applying the final transform. Both methods produce the
same finite coefficients in exact arithmetic. In dimension one, transform the
two point families separately; [(Setup-E.13)](#eq-setup-e-13)--[(Setup-E.14)](#eq-setup-e-14) remain valid as upper bounds under
the conventions following [(Setup-E.2)](#eq-setup-e-2).

The positive-rule construction and separated harmonic recurrences are exactly
those in [the quadrature proof](#setup-quadrature). Let $G_{\rm rule},G_{\rm basis}$ denote its
time bounds [(Setup-Q.30)](#eq-setup-q-30)--[(Setup-Q.31)](#eq-setup-q-31), with spherical cutoff $\ell_*$. Scalar basis values may be recomputed on each panel for work
$G_{\rm rule}+JG_{\rm basis}$ and the original geometry workspace, or
cached once for work $G_{\rm rule}+G_{\rm basis}$ and additional storage
$O(N_x(H_{\rm sph}+d))$. Either choice avoids dense-path storage and is
polynomial in the displayed orders. Time-node sorting, panel moment tables,
and their workspace are charged separately in [(Setup-E.12)](#eq-setup-e-12).

<a id="setup-assembly-4"></a>
##### Dense local jets and anchor advancement

The factorization used at time zero remains algebraically valid at an arbitrary
anchor; zero readout is not required. Temporarily use unscaled normalized
Taylor coefficients $[\cdot]_c$ with respect to $t-\tau_b$, and set
$u_a^{(j)}=r_a\delta_a^{(j)}$. For $s\ge1$, the dense ODE gives

\[
[A]_s=-\frac2{ms}\sum_a[u_a^{(1)}]_{s-1}v_a^T,
\]
<a id="eq-setup-e-15"></a>
\[
[W^{(j)}]_s=-\frac2{mns}\sum_a\sum_{i+k=s-1}
              [u_a^{(j)}]_i[h_a^{(j-1)}]_k^T.
\tag{Setup-E.15}
\]

The constant mixer in this identity is the current $W_b^{(j)}$. Training
jets shared by every passive query therefore determine all higher parameter
jets without storing $K$ dense matrices. The scalar change to coefficients
in [(Setup-E.4)](#eq-setup-e-4) costs only a multiplication by $\Delta_b^c$ for each coefficient.

For a query series $X$, let $U_i,H_k$ be the $n$-by-$m$ training
coefficient matrices. The increment action of degree $s$ is

<a id="eq-setup-e-16"></a>
\[
-\frac2{mn}\sum_{i+k+c=s-1}
                   \frac{U_i(H_k^TX_c)}{i+k+1}.
\tag{Setup-E.16}
\]

Caching all $H_k^TX_c$ first gives the same causal operation bound as the
initial-jet construction. Only lower orders occur in an order-$s$ increment.
Training uses a batch of $m$ vectors once per panel, and passive queries use
one vector at a time. Transpose actions interchange the two training factors.
The resulting non-activation work is

\[
T_{\rm train}
=O\bigl(J[PmK+Lm^2K^2(n+K)]\bigr),
\]
<a id="eq-setup-e-17"></a>
\[
T_{\rm passive}
=O\bigl(JN_x[PK+LmK^2(n+K)]\bigr).
\tag{Setup-E.17}
\]

The live jets/contraction caches need

<a id="eq-setup-e-18"></a>
\[
O(P+LmnK+Lm^2K^2)
\tag{Setup-E.18}
\]

words, including a dense anchor and the resident initial arrays up to a
numerical constant. The $P$ term cannot be dropped merely because the
retained runtime model is small. At most one spatial query's jets are live.

Advancing the dense anchor also has to be charged. Its hidden-matrix endpoint
increment can be grouped as

<a id="eq-setup-e-19"></a>
\[
\Delta W^{(j)}=-\frac2{mn}\sum_{i=0}^{K-1}U_iV_i^T,
\qquad
V_i=\sum_{k=0}^{K-1-i}
              \frac{\Delta_b^{\,i+k+1}}{i+k+1}H_k.
\tag{Setup-E.19}
\]

Forming the $V_i$ costs $O(nmK^2)$ per layer. Applying the $K$
rank-at-most-$m$ outer products to the dense anchor costs $O(n^2mK)$.
First-matrix and readout updates fit the bound

<a id="eq-setup-e-20"></a>
\[
T_{\rm advance}=O\bigl(J[PmK+LnmK^2]\bigr).
\tag{Setup-E.20}
\]

This is absorbed by [(Setup-E.17)](#eq-setup-e-17), but [(Setup-E.19)](#eq-setup-e-19) shows why it does not require an omitted
$O(Jn^2mK^2)$ materialization. One can form one $V_i$, update the
anchor, and discard it after the panel's source processing is complete.

A simpler materialized implementation is also valid: generate all dense
parameter jets and use ordinary series convolutions for training and passive
queries. Its non-activation bound is

<a id="eq-setup-e-21"></a>
\[
O(JP(m+N_x)K^2),\qquad O(PK+LmnK)
\tag{Setup-E.21}
\]

for time and live jet memory, with anchor evaluation included. Formula [(Setup-E.17)](#eq-setup-e-17)
is the more economical construction used below; [(Setup-E.21)](#eq-setup-e-21) is not needed to establish
its validity.

Let $a_{\rm on}(K),b_{\rm on}(K)$ be time and workspace for one scalar
activation/derivative in sequential training-jet generation, and
$a_{\rm off}(K),b_{\rm off}(K)$ the corresponding passive-query series
costs, including scalar derivative generation. The separate activation terms
are

\[
T_{\rm act}=JLn[ma_{\rm on}(K)+N_xa_{\rm off}(K)],
\]
<a id="eq-setup-e-22"></a>
\[
M_{\rm act}=Lmn b_{\rm on}(K)+b_{\rm off}(K).
\tag{Setup-E.22}
\]

Maxima over layer-specific backends suffice. Fixed-size differential
recurrences, such as tanh, permit quadratic series arithmetic and linear
workspace. General analytic regularity does not imply a fast derivative
oracle. A cubic composition algorithm with supplied scalar derivatives still
leaves derivative generation separately charged through [(Setup-E.22)](#eq-setup-e-22).

<a id="setup-assembly-5"></a>
##### Selection, final initialization, total work and memory

Save the exact initialized training features and their initialized forward
images during the first training pass at $\tau_0=0$. Include the constant vector
and initial first-weight columns. These additions are exact; later approximate
anchors cannot replace them. Their direct work is at most $O(mP)$, absorbed
by the training term in [(Setup-E.17)](#eq-setup-e-17), plus the already charged scalar activations.
These initial values use the inherited exact-real activation primitives;
finite-precision exact initialization is a separate issue.

After computing [(Setup-E.11)](#eq-setup-e-11) and [(Setup-E.6)](#eq-setup-e-6), discard dense continuation anchors and panel
workspace. Orthogonalize the complete source-generator list, select coordinates,
and assemble the original source metrics and initial compressed matrices. The
existing costs are

<a id="eq-setup-e-23"></a>
\[
T_{\rm select+assemble}
=O(LnRr+Lnr^3+Ln^2r+Lq^2r).
\tag{Setup-E.23}
\]

The $Ln^2r$ term compresses $W_0$ on the complete source bases. The
paired image coefficients do not generally give its action on every basis
vector, so this term remains even after [(Setup-E.9)](#eq-setup-e-9). The final model starts at the
original $A_0,W_0,w_0=0$, with the original exact training Gram and optimizer.
The last continuation anchor is not its initialization.

Let $T_{\rm proj}$ and $M_{\rm proj}$ denote either [(Setup-E.13)](#eq-setup-e-13) with buffer
$O(Ln(p+1))$, or [(Setup-E.14)](#eq-setup-e-14). Let $G_{\rm time},G_{\rm memory}$ denote one of
the explicit geometry choices after [(Setup-E.14)](#eq-setup-e-14). A sufficient complete envelope is

<a id="eq-setup-e-24"></a>
\[
\begin{split}
T_{\rm setup}=O\bigl(&P
 +J\{P(m+N_x)K+Lm(m+N_x)K^2(n+K)\}\\
&+(N_t+J)(p+1)K+T_{\rm proj}+Ln^2N\\
&+LnRr+Lnr^3+Ln^2r+Lq^2r\\
&+T_{\rm act}+G_{\rm time}+N_t\log(2+N_t)+C_{\rm cert}\bigr),
\tag{Setup-E.24}
\end{split}
\]

<a id="eq-setup-e-25"></a>
\[
\begin{split}
M_{\rm setup}=O\bigl(&P+LmnK+Lm^2K^2+LnR+Lq^2\\
&+(p+1)K+N_t+J+M_{\rm proj}+m(d+1)\\
&+M_{\rm act}+G_{\rm memory}+M_{\rm cert}\bigr).
\tag{Setup-E.25}
\end{split}
\]

These bounds do not store $JP$ anchors, $JPK$ dense jets, or $N_tN_x$
dense source arrays. Their source coefficients require $O(LnR)$ words,
which are discarded after assembly. The formula is a safe peak upper bound;
freeing stage-specific buffers can lower it. Fresh initialization additionally
requires exactly $nd+(L-1)n^2$ Gaussian draws and the sampler's cost/scratch.

By [(Setup-E.6)](#eq-setup-e-6)--[(Setup-E.8)](#eq-setup-e-8), the spaces meet the original approximation and pairing assumptions
with the original rank bound [(Setup-E.2)](#eq-setup-e-2). Therefore the selected neural dynamics,
learned-state count

\[
(L-1)q^2+q(d+1)+m,
\]

and retained inventory bound

<a id="eq-setup-e-26"></a>
\[
1020(L+1)R^2+10m(d+1)
\tag{Setup-E.26}
\]

remain valid with the same qualifications as in [the preceding Harmonic construction](#harmonic-construction). The original
all-time prediction-error certificate is unchanged because every source error
is below its original allowance. Neither quadrature nodes nor local panel
degrees become runtime state. Baseline-only, zero-label and full-width branches
retain their separate existing constructions.

<a id="setup-bridge"></a>
#### Source-jet compatibility and complete explicit costs

<a id="setup-bridge-1"></a>
##### Precision and source-jet compatibility

Let \(\delta_{\rm node}>0\) be the global quadrature's coordinate-error
allowance. It is defined in assembly equation [(Setup-E.3)](#eq-setup-e-3), with its separate
dimension-one convention. Run the polynomial-activation backend with the
stricter requested nodal tolerance

<a id="eq-setup-b-1"></a>
\[
\tau=\frac{\delta_{\rm node}}{32\sqrt n}.
\tag{Setup-B.1}
\]

All its scalar approximation and global defect budgets use this \(\tau\)
in place of its local symbol \(\delta_{\rm node}\). Let
\(\widehat R_n,V,C_{\rm src}\) be the explicit radius, velocity and
original-source comparison coefficient of that backend and [the local-continuation proof](#setup-core).
Set

<a id="eq-setup-b-2"></a>
\[
C_g=\max_j\{H_j+1,B_j+1\},
\tag{Setup-B.2}
\]

where \(H_j,B_j\) are the core's complex forward-feature and backward
response RMS bounds. Increase the backend's training Taylor degree, if
necessary, to the maximum of its equation [(Setup-A.22)](#eq-setup-a-22) and

<a id="eq-setup-b-3"></a>
\[
\left\lceil\log_2\max\left\{1,
 \frac{128V\widehat R_n C_{\rm src}n^{3/2}}{\delta_{\rm node}}
 \right\}\right\rceil,
\qquad
\left\lceil\log_2\max\left\{1,
 \frac{64\sqrt n C_g}{\delta_{\rm node}}
 \right\}\right\rceil.
\tag{Setup-B.3}
\]

Use that same degree \(K\) for training and passive sources. Increasing it
preserves the previous tail/defect inequalities. All additional inverse
tolerances have logarithm \(O(\log(en))\) in the polynomial-accuracy
regime, so \(K=O(\log(en))\) is unchanged.

To verify the assembly's Euclidean error interface, consider one panel and
one passive real unit query. Write \(v\) for the exact local solution of
the polynomial-activation setup field, \(p\) for its computed degree-\(K\)
parameter Taylor polynomial, and \(g_K\) for the degree-\(K\) Taylor
polynomial of a base source \(h^{(j)}\) or \(\delta^{(j)}\) along
\(v\), using the setup activations. Denote original and setup activation
evaluation by \(g^0\) and \(g^p\), respectively. The desired source is
\(g^0(\theta(t))\), on the original dense trajectory.

On the local complex disk, both original feature and response RMS are
bounded by \(H_j,B_j\). The activation replacement estimate applies
there at each fixed real query: every original carrier has RMS bounded by
the core coefficient, hence coordinate maximum at most \(\sqrt n\)
times that coefficient, exactly as used in backend equations [(Setup-A.15)](#eq-setup-a-15), [(Setup-A.24)](#eq-setup-a-24).
Equation [(Setup-A.25)](#eq-setup-a-25) with [(Setup-B.1)](#eq-setup-b-1) makes the additional source RMS smaller than one.
Thus \(\|g^p(v)\|_2\le\sqrt n C_g\) throughout the complex disk.
Vector-valued Cauchy and the half-radius panel give

<a id="eq-setup-b-4"></a>
\[
\|g_K-g^p(v)\|_2\le\sqrt n C_g2^{-K}
                         \le\delta_{\rm node}/64.
\tag{Setup-B.4}
\]

The remaining differences are split before estimating:

<a id="eq-setup-b-5"></a>
\[
g_K-g^0(\theta)
=[g_K-g^p(v)]+[g^p(v)-g^0(v)]
 +[g^0(v)-g^0(p)]+[g^0(p)-g^0(\theta)].
\tag{Setup-B.5}
\]

The second term has each coordinate at most \(\tau/2\), by backend
[(Setup-A.24)](#eq-setup-a-24)--[(Setup-A.25)](#eq-setup-a-25); its Euclidean norm is therefore at most
\(\sqrt n\tau/2=\delta_{\rm node}/64\).

For the third term the original-source comparison gives a coordinate
bound \(C_{\rm src}n\|v-p\|_2\). It applies to these two real states:
both remain within the core's real operator/readout neighborhood, and its
passive-query proof uses only those caps and the RMS-to-coordinate estimate,
not a probabilistic maximum for the perturbed state. The Taylor tail gives
\(\|v-p\|_2\le2V\widehat R_n2^{-K}\). Conversion to Euclidean norm
and [(Setup-B.3)](#eq-setup-b-3) thus give at most \(\delta_{\rm node}/64\).

For the fourth term the backend's global estimate [(Setup-A.23)](#eq-setup-a-23), with tolerance
\(\tau\), gives original-source coordinate error at most \(\tau/2\).
Its Euclidean norm is again at most \(\delta_{\rm node}/64\).
Combining the four terms proves

<a id="eq-setup-b-6"></a>
\[
\|g_K-g^0(\theta)\|_2\le\delta_{\rm node}/16
                              <\delta_{\rm node}/8.
\tag{Setup-B.6}
\]

This is precisely the stronger nodal interface needed for assembly [(Setup-E.5)](#eq-setup-e-5).
It permits forming initialized-matrix image coefficients only after global
accumulation: their coordinate error is bounded by eight times the base
Euclidean error. The two computed members satisfy the exact pairing by
linearity, while their error is measured against their own original analytic
source functions. The unchanged quadrature and source-tail allocation then
gives source-coordinate approximation below the original tolerance \(\eta\).

<a id="setup-bridge-2"></a>
##### Why the factored execution still applies

The assembly's original statement names Taylor jets of the actual dense
field \(F\). Here they are jets of the certified disposable field
\(\widetilde F\), with activations \(\psi_j\). This is an explicit
interface replacement, justified by [(Setup-B.6)](#eq-setup-b-6) and the following exact identity.

The polynomial-activation system has the same rank-one gradient equations,
loss normalization and mobilities; only its scalar activation functions are
different. Coefficient comparison therefore gives the identical equations
[(Setup-E.15)](#eq-setup-e-15)--[(Setup-E.20)](#eq-setup-e-20) of [the assembly proof](#setup-assembly), using its actual residuals, responses and
features. The cached action formula and grouped dense-anchor advancement
remain exact for those jets. The proof of their arithmetic count uses only
these finite sums, not a special activation or zero readout at a restart.
There is no extra dense matrix factor hidden in changing \(F\) to
\(\widetilde F\).

For one scalar degree-\(D\) polynomial \(\psi\), the Chebyshev
recurrence is linear in a product by the scalar input series. At time order
\(k\), computing every recurrence index in increasing polynomial degree
uses already known lower time coefficients and the just computed order-\(k\)
coefficients at the preceding recurrence indices. Each product costs
\(O(k+1)\); there are \(O(D)\) such indices. Summing over
\(0\le k\le K\) gives \(O(DK^2)\) work and \(O(DK)\)
sufficient persistent words. Preparing \(\psi'\) costs \(O(D^2)\)
once and its series composition has the same bound. Thus both online
training and offline passive-query backend costs satisfy

<a id="eq-setup-b-7"></a>
\[
a_{\rm on}(K),a_{\rm off}(K)=O(DK^2),\qquad
b_{\rm on}(K),b_{\rm off}(K)=O(DK).
\tag{Setup-B.7}
\]

The exact original initialized features and their images must be computed
separately using \(\phi_j\), as prescribed by the backend. They must not
be replaced by the constant-order \(\psi_j\) features. This costs
\(O(mP)\) arithmetic and \(O(Lmn)\) original value calls and restores
the exact initialized Gram and action conditions. The final compressed
network uses the original activations and optimizer at original time zero;
neither the last dense anchor nor the setup polynomials survive as runtime
state.

<a id="setup-bridge-3"></a>
##### Complete costs and headline specialization

Use the supplied internal counts and geometry from [the assembly proof](#setup-assembly).
Let \(J\) be the number of local panels in this section. Its complete
time envelope [(Setup-E.24)](#eq-setup-e-24) and memory envelope [(Setup-E.25)](#eq-setup-e-25) apply after the substitutions
[(Setup-B.7)](#eq-setup-b-7), with the following explicit additions and qualifications:

- Add \(O(LD^2+mP)\) arithmetic for the polynomial backend and exact
  original initialized features, and \(O(LD)\) polynomial coefficient words.
- Add \(O(LD+Lmn)\) original real activation-value calls. There are no
  high derivative, original first-derivative, complex activation or
  trained-reference oracles. The activation-value precision allowed by
  backend [(Setup-A.10)](#eq-setup-a-10) is polynomially small in width in this regime.
- Panel counts, degrees and tolerances are explicit scalar formulas in
  the backend and [(Setup-B.1)](#eq-setup-b-1)--[(Setup-B.3)](#eq-setup-b-3). Their evaluation fits its displayed scalar
  preprocessing. There are no adaptive rejections, implicit nonlinear
  solves or uncharged certification runs; take the assembly's
  \(C_{\rm cert},M_{\rm cert}\) to be this elementary scalar overhead.
- Fresh initialization adds the original Gaussian draws and sampler costs.
  All arithmetic counts otherwise have numerical, implementation-only
  big-O constants. Finite precision, numerical rank reliability and bit
  complexity are not implied by these exact-real counts.

In particular, with spatial-first projection, a sufficient complete
non-activation bound is

<a id="eq-setup-b-8"></a>
\[
\begin{split}
O\big(&P+LD^2+mP
 +JP(m+N_x)K+JLm(m+N_x)K^2(n+K)\\
 &+JLn(m+N_x)DK^2+(N_t+J)(p+1)K\\
 &+LnJK(N_xH_{\rm sph}+N)+Ln^2N\\
 &+LnRr+Lnr^3+Ln^2r+Lq^2r
 +G_{\rm time}+N_t\log(2+N_t)\big),
\end{split}
\tag{Setup-B.8}
\]

where \(P=(L-1)n^2+n(d+1)\). A sufficient peak count in real words is

<a id="eq-setup-b-9"></a>
\[
\begin{split}
O\big(&P+LmnDK+Lm^2K^2+LnR+Lq^2+LnKH_{\rm sph}+LD\\
 &+(p+1)K+N_t+J+m(d+1)+G_{\rm memory}\big).
\end{split}
\tag{Setup-B.9}
\]

The quadrature geometry terms in these formulas are the explicitly specified
recomputed-per-panel or cached choice in [the assembly proof](#setup-assembly); the chosen time
and memory versions must be used together. No source or dense trajectory
array is retained after selection.

For each separately fixed admissible dataset, depth, activation, positive
label size and confidence, at the original source tolerance \(1/n\) and
horizon \(32(m/\gamma)\log(en)\), the certified choices satisfy

\[
D=O(\log(en)^{3/2}),\quad K=O(\log(en)),\quad
J=O(\log(en)^{3/2}),
\]
<a id="eq-setup-b-10"></a>
\[
N_t,p+1=O(\log(en)^{5/2}),\quad
N_x,H_{\rm sph}=O(\log(en)^{3(d-1)/2}),\quad
N,R,r=O(\log(en)^{3d/2+1}).
\tag{Setup-B.10}
\]

Use the assembly's two-point conventions at \(d=1\). With actual selected
width \(q=O(R)\), every term of [(Setup-B.8)](#eq-setup-b-8) is bounded by

<a id="eq-setup-b-11"></a>
\[
O\!\left(n^2\log(en)^{3d/2+1}
             +n\log(en)^{9d/2+3}+\operatorname{polylog}(n)\right).
\tag{Setup-B.11}
\]

For example the new activation arithmetic is at most
\(n\log(en)^{3d/2+7/2}\), which is bounded by the second term for
every fixed integer \(d\ge1\). The \(n^2\) terms include source-image
formation and initialized mixer assembly, not merely the dense integrator.
The \(n\)-proportional terms are eventually smaller than the displayed
quadratic term, giving the convenient headline

<a id="eq-setup-b-12"></a>
\[
\text{setup work}=O\!\left(n^2\log(en)^{3d/2+1}\right),\qquad
\text{peak setup memory}=O(n^2).
\tag{Setup-B.12}
\]

Both statements are at fixed admissible structural parameters. The explicit
separate \(m,d,L\), order and source-radius dependence is in [(Setup-B.8)](#eq-setup-b-8)--[(Setup-B.10)](#eq-setup-b-10)
and the backend's degree/step formulas; it has not been identified or
discarded. Bounded-cost scalar evaluations and Gaussian sampling, or a
supplied initialization for the latter, are required to include those
costs inside the work shorthand in [(Setup-B.12)](#eq-setup-b-12); otherwise add their exposed costs.
At \(d=1\), [(Setup-B.12)](#eq-setup-b-12) has logarithmic exponent \(5/2\).

The original whole-sphere/all-time error and retained inventory are unchanged:
source approximation is below \(1/n\), so the original comparison gives
\(n^{-1+o(1)}\) error and \(O(\log(en)^{3d+2})\) retained words.
No statement of optimality among all setup algorithms or finite-precision
implementations follows from these sufficient bounds.

For ordinary dense Euler at physical step \(h\), full source horizon
\(T=32(m/\gamma)\log(en)\), and the same scalar-cost convention, the
work is \(\Theta(mPT/h)\). At fixed parameters the setup/Euler ratio is
therefore at most

<a id="eq-setup-b-13"></a>
\[
O\!\left(h\log(en)^{3d/2}\right).
\tag{Setup-B.13}
\]

In particular \(h=n^{-1/2}\) gives a ratio tending to zero, and the
same holds for every fixed inverse-polynomial step. This comparison does
not assert that such an Euler step is necessary or sufficient for a
particular numerical accuracy. The construction may cost more than a dense
solver using the same high-order continuation, which omits source sampling
and compression assembly. It provides the stated Euler comparison,
not a lower-bound separation from all dense training methods.

<a id="setup-sampler"></a>
#### Exact adaptive Gaussian sampling

<a id="setup-sampler-1"></a>
##### Statement and computational model

Fix an integer width $n\geq1$, a finite set of layer indices
$\mathcal I$, and deterministic nonnegative query budgets
$k_\ell$, $\ell\in\mathcal I$. In the dense reference model,

\[
 W^{(\ell)}\in\mathbb R^{n\times n},\qquad
 W^{(\ell)}_{ij}\ \text{are jointly independent }N(0,1/n)
 \quad(\ell\in\mathcal I, 1\leq i,j\leq n).
\]

Let $\xi$ denote all independent randomness used by the querying algorithm;
it is independent of these matrices. At each step the algorithm either stops
or chooses, measurably from $\xi$ and the global past transcript, a layer,
a direction of multiplication, and a finite vector in $\mathbb R^n$. The
reply is $W^{(\ell)}v$ for a forward query or
$(W^{(\ell)})^T u$ for a transpose query. The transcript includes query
choices and replies. There are at most $k_\ell$ queries to layer $\ell$,
including zero, repeated, and linearly dependent queries. The stopping time is
at most $\sum_\ell k_\ell$. No observation of a reference matrix outside this
interface is allowed.

The sampler below receives the queries, draws fresh standard Gaussian scalar
variables as needed, and returns replies. Its Gaussian draws are independent
of $\xi$; its private random tape is not an extra observation made available
to the querying algorithm.

**Theorem.** For every such querying algorithm, the sampler has exactly the
same joint law of $\xi$, queries, replies, stopping time, and every measurable
quantity computed from them as the dense reference model. On an extension of
the sampler's probability space, matrices $\widehat W^{(\ell)}$ can be
defined so that:

1. Their entries are jointly independent $N(0,1/n)$, independently of
   $\xi$.
2. Every reply actually returned by the sampler equals the corresponding
   product with $\widehat W^{(\ell)}$, simultaneously and almost surely.
3. The joint law including these matrices is the dense reference joint law.

This completion is only a proof coupling. The sampler does not initialize a
dense reference matrix or evaluate the dense Gaussian remainder in that
coupling. Its stored matrix information consists only of query bases and their
answers, as described below.

For a layer receiving $k\geq0$ queries, the following bounds hold. Here a
scalar addition, subtraction, multiplication, division, or square root costs
one arithmetic operation; generating one exact standard Gaussian scalar costs
one Gaussian draw. One exact real scalar or integer/address occupies one word.
These are idealized real-arithmetic and Gaussian-generation primitives, not
claims about finite-bit implementations.

\[
\begin{aligned}
\text{arithmetic operations}
 &\leq 4nk^2+6nk+2,\\
\text{Gaussian draws}
 &\leq n\min\{k,2n-1\}\leq nk,\\
\text{sampler words}
 &\leq 2n\min\{k,2n\}+8n+5\min\{k,2n\}+64.
\end{aligned}
\]

There are at most $k$ zero tests and $k$ further rank comparisons. These bounds exclude the querying algorithm's
own work and storage, including any transcript it elects to retain. They include
one current query/reply workspace. For $k\geq1$, they are $O(nk^2)$ arithmetic
and $O(nk)$ words. The two initialization arithmetic operations can be shared
between all layers of the same width. In particular, globally the arithmetic
bound is

\[
 2+\sum_{\ell\in\mathcal I}(4n k_\ell^2+6n k_\ell),
\]

and the Gaussian-draw bounds add across layers. A sum of the displayed per-layer
memory bounds is a valid global bound; the vector workspace can also be shared.
When all query budgets are zero the sampler need not allocate vector workspace.

The budgets may depend arbitrarily on $n$. There is no asymptotic assertion
and no assumption that the input vectors are well conditioned.

The proof maintains the conditional Gaussian law after every query. An
orthogonal split isolates the newly observed Gaussian vector from the
unobserved matrix remainder. This proves the answer kernels, preserves the
conditional product law across layers, and supplies the stopped completion
coupling.

<a id="setup-sampler-2"></a>
##### Stored state and the online algorithm

Suppress the layer superscript while describing one layer. The sampler stores
four matrices, initially with zero columns:

\[
 V,Y\in\mathbb R^{n\times p},\qquad
 U,R\in\mathbb R^{n\times q}.
\]

The columns of $V$ form an orthonormal basis of the span of the forward
query vectors seen so far; the columns of $U$ form an orthonormal basis of
the span of the transpose query vectors seen so far. The stored answers have
the meaning $Y=WV$, $R=W^T U$. This meaning will be supplied by the
coupling proof; an actual $W$ is not an input to the algorithm. The state
always satisfies

<a id="eq-setup-g-1"></a>
\[
 V^T V=I_p,\qquad U^T U=I_q,\qquad U^T Y=R^T V.
\tag{Setup-G.1}
\]

Empty matrix products are zero. Precompute $\sigma=1/\sqrt n$. Every
normalization and every zero test below is exact. In particular, a small
positive norm is not rounded to zero.

###### Forward query $v\in\mathbb R^n$

Using the old state, compute

\[
 a=V^T v,\qquad v_\perp=v-Va,\qquad
 \alpha=\sqrt{v_\perp^T v_\perp}.
\]

If $\alpha=0$, return $Ya$, leave the state unchanged, and draw no
randomness. Otherwise compute

\[
 e=v_\perp/\alpha,\qquad b=R^T e.
\]

If $q<n$, draw $g\in\mathbb R^n$ with independent $N(0,1)$ coordinates
and set

<a id="eq-setup-g-2"></a>
\[
 h=Ub+\sigma\{g-U(U^Tg)\}.
\tag{Setup-G.2}
\]

If $q=n$, set $h=Ub$ without drawing $g$. Return

<a id="eq-setup-g-3"></a>
\[
 Ya+\alpha h,
\tag{Setup-G.3}
\]

then append the column pair $(e,h)$ to $(V,Y)$. The returned expression
uses the old $V,Y$ and old coefficient $a$. The order of appending and
returning can be reversed in an implementation that preserves those values.

###### Transpose query $u\in\mathbb R^n$

Using the old state, compute

\[
 b=U^T u,\qquad u_\perp=u-Ub,\qquad
 \beta=\sqrt{u_\perp^T u_\perp}.
\]

If $\beta=0$, return $Rb$, leave the state unchanged, and draw no
randomness. Otherwise compute

\[
 f=u_\perp/\beta,\qquad a=Y^T f.
\]

If $p<n$, draw fresh $g\in\mathbb R^n$ with independent $N(0,1)$
coordinates and set

<a id="eq-setup-g-4"></a>
\[
 h=Va+\sigma\{g-V(V^Tg)\}.
\tag{Setup-G.4}
\]

If $p=n$, set $h=Va$ without drawing $g$. Return

<a id="eq-setup-g-5"></a>
\[
 Rb+\beta h,
\tag{Setup-G.5}
\]

then append $(f,h)$ to $(U,R)$.

For multiple layers, retain a separate quadruple $(V,Y,U,R)$ per layer and
apply the corresponding rule to the chosen layer. All fresh $g$'s, across
all times and layers, are independent. The algorithm forms only matrix-vector
products with the stored columns. In particular, neither an $n\times n$
projector nor the conditional-mean matrix used in the proof is formed.

<a id="setup-sampler-3"></a>
##### Elementary Gaussian splitting used in the proof

The needed Gaussian fact can be verified directly. If
$Z\in\mathbb R^d$ has independent $N(0,\tau^2)$ coordinates and
$A,B$ are deterministic linear maps with $AB^T=0$, then $AZ$ and
$BZ$ are independent centered Gaussian vectors. Indeed their joint
characteristic function at $(s,t)$ is

\[
 \mathbb E e^{i(s^TAZ+t^TBZ)}
 =\exp\!\left(-\frac{\tau^2}{2}
       \|A^T s+B^Tt\|_2^2\right).
\]

The cross term is $2s^TAB^Tt=0$, so this factors as the product of the
two marginal characteristic functions. This proves independence even when
either covariance is singular. Applying this to the vector of matrix entries
justifies every orthogonal Gaussian split below. No nonsingular covariance or
matrix inverse is needed.

For fixed state satisfying [(Setup-G.1)](#eq-setup-g-1), define, for proof purposes only,

<a id="eq-setup-g-6"></a>
\[
 P=VV^T,\qquad Q=UU^T,\qquad
 M=YV^T+UR^T(I-P).
\tag{Setup-G.6}
\]

The compatibility identity in [(Setup-G.1)](#eq-setup-g-1) implies

<a id="eq-setup-g-7"></a>
\[
 MV=Y,\qquad
 M^TU=VY^TU+(I-P)R=PR+(I-P)R=R.
\tag{Setup-G.7}
\]

The matrices preserving homogeneous versions of these observations are
exactly

<a id="eq-setup-g-8"></a>
\[
 \{A:AV=0, A^TU=0\}
 =\{(I-Q)B(I-P):B\in\mathbb R^{n\times n}\}.
\tag{Setup-G.8}
\]

For the forward inclusion, $AV=0$ implies $AP=0$, and $A^TU=0$
implies $QA=0$. For the reverse inclusion use $(I-P)V=0$ and
$(I-Q)U=0$. Each summand of $M$ in [(Setup-G.6)](#eq-setup-g-6) is Frobenius-orthogonal to
the space in [(Setup-G.8)](#eq-setup-g-8): the first has right support in $\operatorname{span}(V)$,
and the second has left support in $\operatorname{span}(U)$.

Thus the candidate conditional matrix law at this state is

<a id="eq-setup-g-9"></a>
\[
 W=M+(I-Q)G(I-P),
 \qquad G_{ij}\ \text{independent }N(0,1/n).
\tag{Setup-G.9}
\]

The induction below proves [(Setup-G.9)](#eq-setup-g-9) as a conditional-law identity after adaptive
queries. It does not infer adaptive conditioning merely by treating random
query directions as fixed in an unconditional formula.

<a id="setup-sampler-4"></a>
##### One query updates the conditional law exactly

Assume [(Setup-G.9)](#eq-setup-g-9) holds conditional on the full past. Once that past and the
independent querying randomness are conditioned on, the next query direction
and selected layer are fixed.

For a forward query, the algorithm's orthogonal decomposition is
$v=Va+\alpha e$ when $\alpha>0$. If $\alpha=0$, [(Setup-G.7)](#eq-setup-g-7) gives the
deterministic answer $Ya$; receiving that answer conveys no additional
information. If $\alpha>0$, then $\|e\|_2=1$, $Pe=0$, and

<a id="eq-setup-g-10"></a>
\[
 We=UR^T e+(I-Q)Ge.
\tag{Setup-G.10}
\]

The coordinates of $Ge$ are independent $N(0,1/n)$: distinct coordinates
use independent rows of $G$, and the variance in each row is
$\|e\|_2^2/n=1/n$. Consequently [(Setup-G.2)](#eq-setup-g-2) has exactly the conditional law of
$We$, and [(Setup-G.3)](#eq-setup-g-3) has that of $Wv$. If $q=n$, $Q=I$, so the random
term is identically zero and skipping it preserves the law.

It remains to verify that the remaining randomness has the claimed form
after the new answer. Let

\[
 P'=P+ee^T,\qquad
 E=(I-Q)Ge,\qquad
 D=(I-Q)G(I-P').
\]

The remainder in [(Setup-G.9)](#eq-setup-g-9) splits as

<a id="eq-setup-g-11"></a>
\[
 (I-Q)G(I-P)=Ee^T+D.
\tag{Setup-G.11}
\]

The random vector $E$ and matrix $D$ are independent. One direct
covariance calculation is

\[
 \operatorname{Cov}(E_i,D_{ab})
 =\frac1n(I-Q)_{ia}\bigl[e^T(I-P')\bigr]_b=0,
\]

because $P'e=e$. They are jointly Gaussian linear functions of the entries
of $G$, so the characteristic-function argument in [the exact adaptive gaussian sampling subsection 3](#setup-sampler-3) proves the
asserted independence, including all singular cases. The covariance and mean
of $D$ are those of $(I-Q)G'(I-P')$ for fresh iid
$G'_{ij}\sim N(0,1/n)$.

Observing the reply is equivalent to observing $h=We$, since
$h=(Wv-Ya)/\alpha$ and $\alpha>0$. By [(Setup-G.10)](#eq-setup-g-10) this specifies
$E=h-UR^T e$ while leaving $D$ independent and unchanged in law.
The new stored columns satisfy $U^Th=R^Te$, since the noise is annihilated
by $U^T$. Hence [(Setup-G.1)](#eq-setup-g-1) remains valid. The new mean computed by [(Setup-G.6)](#eq-setup-g-6) is

\[
\begin{aligned}
 M'&=YV^T+he^T+UR^T(I-P-ee^T)\\
   &=M+(h-UR^Te)e^T=M+Ee^T.
\end{aligned}
\]

Together with [(Setup-G.11)](#eq-setup-g-11), this is exactly the updated kernel
$M'+(I-Q)G'(I-P')$.

For a transpose query with $\beta=0$, [(Setup-G.7)](#eq-setup-g-7) gives the deterministic answer
$Rb$. With $\beta>0$, $Qf=0$ and $\|f\|_2=1$, so

<a id="eq-setup-g-12"></a>
\[
 W^Tf=VY^Tf+(I-P)G^Tf.
\tag{Setup-G.12}
\]

Thus [(Setup-G.4)](#eq-setup-g-4) is its conditional law. Put

\[
 Q'=Q+ff^T,\qquad
 E=(I-P)G^Tf,\qquad D=(I-Q')G(I-P).
\]

Then $(I-Q)G(I-P)=fE^T+D$, and

\[
 \operatorname{Cov}(E_i,D_{ab})
 =\frac1n(I-P)_{ib}\bigl[f^T(I-Q')\bigr]_a=0.
\]

The same characteristic-function argument shows that $E$ and $D$ are
independent. The observed column $h=W^Tf$ specifies
$E=h-VY^Tf$, while $D$ keeps the law of
$(I-Q')G'(I-P)$. Compatibility is preserved because $V^Th=Y^Tf$.
Expanding the new formula [(Setup-G.6)](#eq-setup-g-6), with $U'=[U\ f]$, $R'=[R\ h]$, gives

\[
 M'=M+fh^T(I-P).
\]

Compatibility yields $Ph=VY^Tf$, so
$h^T(I-P)=(h-VY^Tf)^T=E^T$. Therefore $M'=M+fE^T$, precisely
the updated conditional mean. When $p=n$, $P=I$ and the random term
in [(Setup-G.12)](#eq-setup-g-12) vanishes. This completes the one-query proof in both directions.

<a id="setup-sampler-5"></a>
##### Arbitrary interleaving, stopping, and completion

Let the full past sigma-field include $\xi$ and all queries and replies
up to the current global step. The induction invariant in the dense model is:
conditional on this sigma-field, the matrices in different layers are
independent, with layer $\ell$ having kernel

<a id="eq-setup-g-13"></a>
\[
 M_\ell+(I-Q_\ell)G_\ell(I-P_\ell),
\tag{Setup-G.13}
\]

where the $G_\ell$'s in this conditional representation are mutually
independent iid Gaussian matrices. At time zero, all stored lists are empty,
$M_\ell=P_\ell=Q_\ell=0$, and [(Setup-G.13)](#eq-setup-g-13) is the assumed initialization law.

At a subsequent step, the query choice is measurable from the conditioned
past. It therefore reveals no extra information once that past is fixed.
Only the selected matrix determines the next answer. The one-query calculation
in [the exact adaptive gaussian sampling subsection 4](#setup-sampler-4) gives its answer law and posterior kernel. The conditional
product structure in [(Setup-G.13)](#eq-setup-g-13) implies that all other matrix kernels are unchanged:
the joint conditional law before the answer is the product of the selected
matrix/answer law and the other matrix laws. Conditioning that product on the
answer changes only the selected factor. This proves the induction invariant.

These calculations can equivalently be read as conditional-expectation
identities for bounded measurable test functions; they do not require giving
positive probability to any particular real-valued transcript.

The sampler uses exactly the answer transition kernel just derived, at every
history. Its initial independent randomness $\xi$ has the same law as in
the dense model. Induction over the finite maximal number of queries therefore
gives equality of the complete transcript laws. Querying another layer using
an earlier reply causes no difficulty: conditional on the global past the new
query is already determined. It is the remaining matrices that are
conditionally independent; the outputs themselves need not be independent.

Stopping adds no further conditioning beyond the transcript: whether the
algorithm stops at the current step is measurable from that transcript and
$\xi$. Formally, for a bounded stopping time $T$, partition by the finitely
many events $\{T=t\}$. On each such event the fixed-time conditional identity
already proved applies, with the state at time $t$. Summing those identities
proves [(Setup-G.13)](#eq-setup-g-13) at time $T$. Alternatively, make stopping absorbing and pad the
remaining global steps with no observations.

To construct the stated coupling, run the sampler through its stopping time,
then on an extended probability space take independent matrices
$G_\ell$, independent also of the entire sampler run, with iid
$N(0,1/n)$ entries. Define mathematically

<a id="eq-setup-g-14"></a>
\[
 \widehat W^{(\ell)}
 =M_\ell+(I-Q_\ell)G_\ell(I-P_\ell)
\tag{Setup-G.14}
\]

using the final stored states. The conditional law in [(Setup-G.14)](#eq-setup-g-14) is exactly the
dense model's conditional law given the same stopped transcript and $\xi$.
Integrating this kernel against the identical transcript laws shows equality
of the full joint laws, including $\xi$ and all completed matrices. In
particular, their unconditional entries are jointly independent
$N(0,1/n)$, and the completed matrices are independent of $\xi$.

Equation [(Setup-G.7)](#eq-setup-g-7) and the projected remainder imply
$\widehat W^{(\ell)}V_\ell=Y_\ell$ and
$(\widehat W^{(\ell)})^TU_\ell=R_\ell$. Every earlier forward query is
in the span of the final $V_\ell$, with its returned reply equal to the same
linear combination of stored columns of $Y_\ell$; the new independent
column is appended when that query is processed. Later appends preserve all
previous columns and relations. The transpose argument uses $U_\ell,R_\ell$.
Thus all earlier replies are simultaneously products with the single completed
matrix for their layer. This is pathwise equality on the constructed coupling,
not only a separate marginal-law assertion for each answer.

Construction [(Setup-G.14)](#eq-setup-g-14) is not part of the online algorithm or its operation count.
Even if the algorithm later resumes querying, it can continue from the stored
quadruples with fresh Gaussian vectors: the same conditional kernel gives the
correct continuation law. One must not first realize an independent completion
and then claim that unrelated fresh sampler draws reproduce that particular
completion; pathwise agreement requires the joint coupling just established.

<a id="setup-sampler-6"></a>
##### Cost calculation

At a local query to one layer, let $p,q$ be the old basis sizes. A length-
$n$ dot product costs at most $2n$ arithmetic operations. Therefore a
product by an $n\times p$ matrix or its transpose costs at most $2np$.
The following count assumes a new forward direction and allows all displayed
operations even when an empty or full span would permit skipping some.

| Computation | Arithmetic bound |
| --- | ---: |
| $a=V^Tv,\ v_\perp=v-Va$ | $4np+n$ |
| $\alpha=\sqrt{v_\perp^Tv_\perp}$ | $2n+1$ |
| $e=v_\perp/\alpha$ | $n$ |
| $b=R^Te$ | $2nq$ |
| $g-U(U^Tg)$ | $4nq+n$ |
| $h=Ub+\sigma\{g-U(U^Tg)\}$ after the projected vector is ready | $2nq+2n$ |
| reply $Ya+\alpha h$ | $2np+2n$ |

The sum is $6np+8nq+9n+1\leq8n(p+q)+10n$, since $n\geq1$.
A dependent forward query costs at most $6np+3n+1$, which is smaller.
The transpose bound exchanges $p$ and $q$ and has the same upper bound
$8n(p+q)+10n$. There is one zero test per query and at most one further
rank comparison. Vector copying and
bookkeeping take $O(n+p+q)$ word accesses per query, so also preserve the
stated asymptotic work bound if word accesses are charged separately.

Before the $j$-th local query, $p+q\leq j-1$. Summing gives

\[
 \sum_{j=1}^k \{8n(j-1)+10n\}
 =4nk(k-1)+10nk=4nk^2+6nk.
\]

Computing $\sigma=1/\sqrt n$ uses one square root and one division. This
proves the claimed arithmetic bound. No inverse, linear solve, Gram-matrix
eigenvalue bound, or condition-number assumption occurs in this calculation.

Every nonzero new query direction increases exactly one of $p,q$ by one.
Both remain at most $n$. Gaussian vectors are needed only until one of the
two ranks first reaches $n$; thereafter queries enlarging the other side
have deterministic new columns. Immediately before that first full rank, both
ranks are at most $n-1$, so at most $2n-1$ enlargements can draw a Gaussian
vector. If neither rank reaches $n$, there are at most $2n-2$ enlargements.
There are also at most $k$ enlargements in total. Each drawing enlargement
uses $n$ scalar draws, proving $n\min\{k,2n-1\}$.

The four stored matrices contain $2n(p+q)$ scalar words. Store their columns
as linked lists of separate vectors with $2(p+q)$ next-column addresses;
this allows append
without holding a second full copy of the state. Eight length-$n$ scratch
vectors and $3(p+q)$ coefficient words are a conservative workspace bound:
one needs only the current vector/residual, a Gaussian vector, a new answer,
an output, temporary matrix-vector storage, and the three coefficient lists
$a,b,U^Tg$ (or their transpose counterparts). Sixty-four additional scalar or
integer/address words suffice for the scale, norms, loop indices, dimensions,
and list roots in an ordinary implementation. Newly retained column vectors
are charged to the stored matrices. Thus

\[
 2n(p+q)+8n+5(p+q)+64
 \leq 2n\min\{k,2n\}+8n+5\min\{k,2n\}+64.
\]

This is a bound for the sampler state, not for arbitrary client-side storage
or for the imaginary dense matrices in the proof. When $k$ is comparable to
$n$, the bound is itself quadratic in $n$; the theorem makes no stronger
compression claim in that regime. For example, querying all $n$ standard
basis vectors forwards returns the entire matrix, and the retained $Y$ then
equals that matrix. Thus “implicit” specifies how reference randomness is
generated and queried; it cannot mean that an unrestricted oracle transcript
never reveals the whole matrix. A requirement of subquadratic storage must
also constrain the query budget, for example $k=o(n)$.

<a id="setup-sampler-7"></a>
##### Exact scope and limitations

The construction samples a new reference matrix implicitly with the correct
joint iid law. It does not receive a previously realized concrete matrix or
the seed of a specified dense-entry generator, and it does not reproduce
products for such a supplied realization. Equality in law and the existence
of the coupling [(Setup-G.14)](#eq-setup-g-14) do not supply that additional service. To serve a fixed
matrix or a prescribed seed-to-matrix map would require a separate input model
and algorithm; no complexity bound for it follows here.

The theorem does permit exact finite-$n$ distributional reasoning for any
algorithm using the specified oracle, including nonlinear or discontinuous
adaptive choices and data-dependent stopping within the budgets. It preserves
the forward/transpose response terms, the dependence between reused products,
and independence of the *unconditional* layer matrices. It makes no claim of
coordinate independence for reused outputs.

Exact zero tests and normalizations are part of the mathematical algorithm.
Near-dependent directions can cause finite-precision difficulties. Replacing
zero tests by tolerances or ordinary orthogonalization by an approximate
implementation requires a separate error analysis. Likewise, exact real words
and exact Gaussian draws are primitives of the stated cost model, not hidden
claims that infinitely precise numbers fit in fixed-bit machine words.

Finally, this sampler result by itself proves no stability, training-time,
width-limit, mean-field, state-evolution, or approximation theorem. Such uses
must supply their own query budgets and additional mathematical arguments.

<a id="setup-implicit"></a>
#### Exact implicit execution and full costs

<a id="setup-implicit-1"></a>
##### Inputs, notation, and precise sampler dependency

Let \(L\ge2\) and \(m,d,n\ge1\) be hidden depth, sample count, input dimension
and hidden width, with \(n\ge\max(m,d)\). Training inputs are

\[
v_a=x_a/\sqrt d\in S^{d-1},\qquad 1\le a\le m.
\]

The first matrix \(W^{(1)}\in\mathbb R^{n\times d}\) has independent
standard normal entries. For \(2\le j\le L\), the initialized hidden matrix

<a id="eq-setup-i-1"></a>
\[
W_0^{(j)}\in\mathbb R^{n\times n},\qquad
(W_0^{(j)})_{uv}\sim N(0,1/n)
\tag{Setup-I.1}
\]

has independent entries, independently across layers and of \(W_0^{(1)}\).
The stored readout \(w=W^{(L+1)}\in\mathbb R^n\) is initially zero.
This is the zero-readout convention of the [dense model](#dense-model-and-certificates).
The ordinary forward and backward coordinates are

\[
z^{(1)}=W^{(1)}v,\quad
z^{(j)}=W^{(j)}h^{(j-1)},\quad
h^{(j)}=\phi_j(z^{(j)}),\quad f_n=w^Th^{(L)}/n,
\]
<a id="eq-setup-i-2"></a>
\[
\delta^{(L)}=w\odot\phi_L'(z^{(L)}),\qquad
\delta^{(j)}=\phi_j'(z^{(j)})\odot W^{(j+1)T}\delta^{(j+1)}.
\tag{Setup-I.2}
\]

Residuals are \(r_a=f_n(v_a)-y_a\). The loss is

\[
\mathcal L_n=m^{-1}\sum_a r_a^2.
\]

The prescribed mobilities give the rank-one equations

<a id="eq-setup-i-3"></a>
\[
\dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^T,
\quad
\dot W^{(j)}=-\frac2{mn}\sum_a r_a\delta_a^{(j)}h_a^{(j-1)T},
\quad
\dot w=-\frac2m\sum_a r_ah_a^{(L)}.
\tag{Setup-I.3}
\]

The setup replaces each \(\phi_j\) in [(Setup-I.2)](#eq-setup-i-2)--[(Setup-I.3)](#eq-setup-i-3) by its computed degree-
\(D\ge1\) polynomial \(\psi_j\), but does not replace the exact initial
source additions or the final runtime activations.

Supply a finite panel partition

\[
0=\tau_0<\tau_1<\cdots<\tau_J=T,\qquad
\Delta_b=\tau_{b+1}-\tau_b,
\]

with \(J\ge1\), a common Taylor degree \(K\ge1\), temporal degree
\(p\ge0\), largest spherical degree \(\ell_*\), a finite retained mode set
\(\Lambda\), and its cardinality \(N=|\Lambda|\). For \(d\ge2\), set

<a id="eq-setup-i-4"></a>
\[
h_\ell={\ell+d-1\choose d-1}-{\ell+d-3\choose d-1},\qquad
H_{\rm sph}=\sum_{\ell=0}^{\ell_*}h_\ell,
\quad R=2m+d+1+4N.
\tag{Setup-I.4}
\]

Impossible binomials are zero. The original weighted simplex is one allowed
\(\Lambda\); its actual supplied cutoffs, rather than a rectangular enlargement,
are used in every retained coefficient. There are \(N_t\ge1\) temporal nodes
and \(N_x\ge1\) spatial nodes. For the positive angular rule of [the quadrature proof](#setup-quadrature), \(N_x=N_\varphi N_\theta^{d-2}\) when \(d\ge3\), and
\(N_x=N_\varphi\) when \(d=2\).

For \(d=1\), use two point families, \(N_x=H_{\rm sph}=2\),
\(N=2(p+1)=2N_1\), and the same formula \(R=2m+d+1+4N\).
This is exactly \(2m+d+1+8N_1\); there is no angular quadrature.

Let \(r_j=\dim E_j\) be the actual source-space ranks after coefficient
construction, and let \(q_j\) be the actual selected support sizes. Put

<a id="eq-setup-i-5"></a>
\[
r=\max_jr_j\le\min(n,R),\qquad q=\max_jq_j.
\tag{Setup-I.5}
\]

The deterministic selector gives \(r_j\le q_j\le9r_j\), hence
\(r\le q\le9r\). A supplied budget \(Q\) is sufficient when
\(9r\le Q\); the original safe count uses \(9R\le Q<n\).
Unused budget is not padded with extra coordinates. All occurrences of
\(q\) in the costs below mean the actual retained maximum, not unused capacity.
The constant source ensures \(r_j\ge1\).

**Sampler contract.** For each matrix [(Setup-I.1)](#eq-setup-i-1), a stateful procedure accepts a finite
adaptive sequence of requests \(W_0^{(j)}x\) and \(W_0^{(j)T}y\), with
\(x,y\in\mathbb R^n\). Queries may depend on all previous responses, the
data, and the other layers' transcripts. Its joint responses admit a coupling
with mutually independent matrices [(Setup-I.1)](#eq-setup-i-1), under which every response is the
corresponding exact action. The action procedure must handle both directions
of one matrix consistently, including dependent and zero queries. For at most
\(k\) vector requests at a layer, assume numerical upper bounds

<a id="eq-setup-i-6"></a>
\[
O(nk^2)\ \text{arithmetic},\qquad O(nk)\ \text{words},\qquad
\text{at most }nk\ \text{independent standard normal draws}.
\tag{Setup-I.6}
\]

It suffices to draw at most \(n\) normals for each newly exposed independent
direction and none for dependent requests. Square roots used by normalization
are accounted for separately below. The coupling must apply to globally
interleaved adaptive requests, not just predetermined query vectors. The [adaptive Gaussian theorem proved above](#setup-sampler) supplies this
contract, including its deterministic bounded-stopping and global-interleaving
hypotheses.

All arithmetic is exact real arithmetic, with exact zero/rank comparisons and
the explicitly counted scalar primitives. Gaussian variates are ideal real
normal samples. Activation evaluation costs and Gaussian-generation costs are
not inferred from analyticity or hidden in arithmetic big-O constants.

<a id="setup-implicit-2"></a>
##### Exact low-rank anchors and current-panel coefficients

At panel \(b\), use normalized Taylor coefficients in the unscaled local
variable \(t-\tau_b\). Write

\[
U_i^{(j)}=
\bigl([r_a\delta_a^{(j)}]_i\bigr)_{a=1}^m\in\mathbb R^{n\times m},
\qquad
H_k^{(j-1)}=
\bigl([h_a^{(j-1)}]_k\bigr)_{a=1}^m\in\mathbb R^{n\times m}.
\]

Here the residuals and fields use the polynomial activations. Comparing
coefficients in [(Setup-I.3)](#eq-setup-i-3), for \(1\le s\le K\), gives

<a id="eq-setup-i-7"></a>
\[
[W^{(j)}]_s=-\frac2{mns}
\sum_{i+k=s-1}U_i^{(j)}H_k^{(j-1)T}.
\tag{Setup-I.7}
\]

The degree-zero term is the current anchor \(W_b^{(j)}\). Its endpoint update
is exactly

<a id="eq-setup-i-8"></a>
\[
W_{b+1}^{(j)}-W_b^{(j)}
=-\frac2{mn}\sum_{i=0}^{K-1}U_i^{(j)}V_i^{(j-1)T},\qquad
V_i^{(j-1)}=\sum_{k=0}^{K-1-i}
\frac{\Delta_b^{i+k+1}}{i+k+1}H_k^{(j-1)}.
\tag{Setup-I.8}
\]

For each panel append the \(mK\) columns of the \(U_i^{(j)}\), with the
factor \(-2/(mn)\), to a factor \(A_b^{(j)}\), and the corresponding
\(V_i^{(j-1)}\) columns to \(B_b^{(j)}\). These factor symbols are not
the first weight matrix. They have shapes \(n\times bmK\), and

<a id="eq-setup-i-9"></a>
\[
W_b^{(j)}=W_0^{(j)}+A_b^{(j)}B_b^{(j)T},\qquad
\operatorname{rank}(W_b^{(j)}-W_0^{(j)})\le bmK.
\tag{Setup-I.9}
\]

No independence, smallness, or low-rank property of the initialized matrix is
used in [(Setup-I.9)](#eq-setup-i-9). The rank bound holds for the finite numerical anchor increment
because its endpoint is the specified degree-\(K\) polynomial. It is not a
rank bound for an exact continuous trained increment.

For a current-panel query series \(X(t)=\sum_{c=0}^KX_c(t-\tau_b)^c\),
each coefficient of the constant-anchor action is computed as

<a id="eq-setup-i-10"></a>
\[
W_b^{(j)}X_c
=\operatorname{Action}_j(X_c)+A_b^{(j)}(B_b^{(j)T}X_c).
\tag{Setup-I.10}
\]

The transpose uses

<a id="eq-setup-i-11"></a>
\[
W_b^{(j)T}X_c
=\operatorname{TransposeAction}_j(X_c)
 +B_b^{(j)}(A_b^{(j)T}X_c).
\tag{Setup-I.11}
\]

The higher-parameter-jet contribution to the coefficient of order \(s\ge1\)
is still the finite sum

<a id="eq-setup-i-12"></a>
\[
-\frac2{mn}\sum_{i+k+c=s-1}
\frac{U_i^{(j)}(H_k^{(j-1)T}X_c)}{i+k+1}.
\tag{Setup-I.12}
\]

The cached-contraction implementation in [the assembly proof](#setup-assembly) computes [(Setup-I.12)](#eq-setup-i-12)
exactly. All its factors at order \(s\) have lower orders than \(s\), so
it remains causal during training-jet generation. Equations [(Setup-I.10)](#eq-setup-i-10)--[(Setup-I.12)](#eq-setup-i-12) give
precisely the same local coefficient as multiplication by a materialized
anchor and materialized parameter jets. Polynomial Chebyshev composition is
also a finite exact recurrence. Induction over coefficient order, then over
layers in the forward/backward passes, identifies every computed training and
passive coefficient with its counterpart in the explicit algorithm.

The first matrix is stored explicitly in \(nd\) words. It does not require
\(ndK\) persistent coefficient words. With
\(V=(v_a)_{a=1}^m\in\mathbb R^{d\times m}\), its higher coefficients act by

<a id="eq-setup-i-13"></a>
\[
[W^{(1)}]_sx=-\frac2{ms}U_{s-1}^{(1)}(V^Tx).
\tag{Setup-I.13}
\]

Precompute \(V^TV\) for training and compute \(V^Tx\) for each streamed
passive query. To advance its anchor first sum
\(\sum_{i<K}\Delta_b^{i+1}U_i^{(1)}/(i+1)\), then multiply by
\(-2V^T/m\). Readout coefficients and endpoint updates are ordinary vectors
obtained from \(\dot w=-2\sum_a r_ah_a^{(L)}/m\). Both calculations are
exact rearrangements of the same finite sums.

<a id="setup-implicit-3"></a>
##### Exhaustive matrix-access inventory and output coupling

Fix generator ordering, Gram--Schmidt sign conventions, deterministic selector
tie-breaking, and all scalar quadrature/backend formulas. These choices select
one concrete version of the explicit finite construction. Its only accesses
to a hidden initialized matrix are the following.

1. **Exact original initialization.** Compute all training features at time
   zero with the original \(\phi_j\), saving the forward images
   \(W_0^{(j)}h_0^{(j-1)}(v_a)\). This uses \(m\) forward actions at each
   hidden mixer. The backward fields are zero because \(w_0=0\); no original
   derivative calls are required. Insert these exact feature/image vectors,
   the first-weight columns at layer one, and the constant vector into the
   source spaces. The degree-zero \(\psi_j\) features cannot replace them.
2. **Every panel's forward/backward coefficients.** For each coefficient
   through \(K\), the training batch uses at most \(m\) forward and \(m\)
   transpose actions per mixer through [(Setup-I.10)](#eq-setup-i-10)--[(Setup-I.11)](#eq-setup-i-11). Each passive query uses at
   most one of each. All current-anchor corrections and nonconstant parameter
   coefficients use retained factors and finite contractions, not new matrix
   entries. Panels with no assigned time nodes can omit passive queries, but
   the bound below permits all \(N_x\) queries on all \(J\) panels.
3. **Initialized images of completed global coefficients.** Accumulate only
   the base coefficient vectors for \(h^{(j)}\) and \(\delta^{(j)}\).
   For each retained mode form
   \(W_0^{(j)}\widetilde c^{\,h^{(j-1)}}\) and
   \(W_0^{(j)T}\widetilde c^{\,\delta^{(j)}}\).
   This uses at most \(N\) forward and \(N\) transpose actions per mixer.
   It is exact because all preceding projection operations are scalar finite
   sums shared by each source/image pair.
4. **Final basis-to-basis mixer.** Having constructed bases
   \(U_j\in\mathbb R^{n\times r_j}\), with \(U_j^TU_j/n=I\), request
   \(W_0^{(j)}U_{j-1}\) column by column. This uses at most
   \(r_{j-1}\le r\) further forward actions. Paired source-image information
   is not assumed to cover these basis columns. Form
   \(U_j^TW_0^{(j)}U_{j-1}/n\) from these returned vectors.

Consequently a sufficient number of vector requests per hidden mixer is

<a id="eq-setup-i-14"></a>
\[
k_* = m+2J(m+N_x)(K+1)+2N+r.
\tag{Setup-I.14}
\]

The random realized rank in this pathwise cost bound is not a deterministic
stopping budget. To invoke the sampler theorem, use the deterministic bound
\(m+2J(m+N_x)(K+1)+2N+\min(n,R)\) at each layer, since
\(r\le\min(n,R)\). Its online operation count may still be evaluated at
the smaller actual request count and bounded by [(Setup-I.14)](#eq-setup-i-14).

This counts requests even when their vectors vanish, repeat, or lie in a
previously queried span. The adaptive sampler can save work in those cases;
the sufficient envelope does not require such savings. Scalar data geometry,
orthogonalization, selection, and metric formation do not access \(W_0\)
except through the four listed uses. In particular there is no request for its
entries, Frobenius norm, singular values, or full operator norm.

To prove coupling of the full outputs, take a joint realization supplied by
the sampler contract. Materialize its completed matrices only in the proof and
run the explicit finite algorithm with those matrices. The original initialized
features agree by induction over layers. Assume current anchors, stored jets,
and accumulated global coefficients agree before one computation step. If the
step requests a matrix action, [(Setup-I.6)](#eq-setup-i-6), [(Setup-I.10)](#eq-setup-i-10), and [(Setup-I.11)](#eq-setup-i-11) give the exact explicit
answer. If it performs a scalar operation, polynomial composition, contraction,
or endpoint update, the operands and the operation are the same exact real
quantities, with [(Setup-I.8)](#eq-setup-i-8), [(Setup-I.12)](#eq-setup-i-12), and [(Setup-I.13)](#eq-setup-i-13) justifying any change in grouping. Thus the
next state agrees. Finite induction over all panels proves equality of the
completed base coefficients, then the image coefficients in item 3.

The source generators and their order therefore agree. Exact orthogonalization
returns the same ranks and bases. The selector sees the same row vectors and
barrier comparisons, so the prescribed tie-breaking gives the same selected
indices and weights. Item 4 then gives the same final compressed mixers. The
metric formula and first-weight restriction also agree. In detail, with
\(P_j=(U_j)_{I_j}\), the initialized output is exactly

\[
W_C^{(1)}(0)=(W_0^{(1)})_{I_1},\quad w_C(0)=0,\quad c_C(0)=y,
\]
<a id="eq-setup-i-15"></a>
\[
B_C^{(j)}(0)
=P_j\frac{U_j^TW_0^{(j)}U_{j-1}}nP_{j-1}^TM_{j-1}.
\tag{Setup-I.15}
\]

Any deterministic scalar failure branch in the explicit execution is reproduced
as well. The algebraic statement holds for all finite supplied orders; source
accuracy additionally requires the certified degree, panel, and quadrature
certificates. This argument is equality under a coupling, not merely equality
of marginal output laws. It preserves the original all-time comparison event
and its probability without an additional failure budget.

The fresh-reference contract matters. This proof does not reproduce a previously
materialized matrix, or a previously specified entrywise pseudorandom stream,
without paying that reference's access costs. It supplies a fresh reference with
the prescribed independent Gaussian law.

<a id="setup-implicit-4"></a>
##### Scalar certificates and what is not tested

The finite construction takes admissible numeric structural certificates as
inputs: a positive population gap \(\gamma\), activation strip/derivative
bounds, and the fitting/source constants required by the proved continuation.
Non-elementary population moments used in the exact label allowance are also
supplied if that allowance is to be evaluated exactly. An arbitrary analytic
activation does not provide an algorithm for its Gaussian moment integrals.
Obtaining such external certificates is not charged as free arithmetic here.

Given those quantities, the source constants (S.5)--(S.10), (S.22)--(S.25),
the fitting/comparison recurrences, the restart constants, and the backend
formulas are finite scalar recurrences. Their layer-indexed arrays have length
\(O(L)\); integer powers/factorials for the dimension use \(O(d)\)
multiplications. The label RMS costs \(O(m)\) arithmetic and one square root.
Thus their scalar preparation and deterministic gate comparisons cost
\(O(L+d+m+1)\) arithmetic, elementary calls, and words as a safe common bound.
Angular basis and mode enumeration costs are separately charged below.

The explicit width, radius, count, and analytic-extension gates are comparisons
of these scalars and \(n\). Their evaluation never tests a sampled hidden
matrix's norm. Likewise the local Taylor construction selects its panels and
degree from the explicit bounds; it does not form an \(n^2\)-coordinate defect
vector, solve an implicit equation, test membership in a complex parameter
ball, or reject and recompute panels. Those norms and domains occur in the
proof of its deterministic error bound. The underlying source probability event
is an inherited theorem hypothesis, not a computable acceptance test, and its
width threshold remains partly unquantified. There is no rejection sampling
conditioned on that event.

If desired, the exact initial top feature Gram can be formed and factored in
\(O(nm^2+m^3)\) arithmetic and \(O(m^2)\) additional words. This is also
a sufficient charge for preparing the final initial readout solve cache: exact
source isometry makes the selected initial Gram the same Gram. It does not
require querying any further initialized-matrix directions. The formulas below
include this charge, even if a particular output omits that cache.

<a id="setup-implicit-5"></a>
##### Complete supplied-order arithmetic and peak storage

All big-O constants in this section are numerical and implementation-dependent
only. They hide no dependence on \(L,m,d,n,J,K,D,p,\ell_*,N_t,N_x,N,R,r,q\),
structural certificate values, confidence, activation cost, Gaussian cost, or
precision. A bound is an operation count for this specified execution; it is
not an optimality statement. Write \(k_*\) only for the explicit expression
[(Setup-I.14)](#eq-setup-i-14).

First account for the two terms introduced by implicit execution. The Gaussian
action work is

<a id="eq-setup-i-16"></a>
\[
O((L-1)n k_*^2),\qquad O((L-1)n k_*)\ \text{words}.
\tag{Setup-I.16}
\]

At panel \(b\), each forward/transposed application of the accumulated
increment has cost \(O(nbmK)\) per vector. There are at most
\(2(m+N_x)(K+1)\) such vectors per mixer. Since
\(\sum_{b=0}^{J-1}b=J(J-1)/2\), their total work is

<a id="eq-setup-i-17"></a>
\[
O((L-1)n m(m+N_x)J(J-1)K(K+1)).
\tag{Setup-I.17}
\]

Retaining both rank factors uses \(O((L-1)nJmK)\) words. Forming the
grouped factors [(Setup-I.8)](#eq-setup-i-8) costs \(O(J(L-1)nmK^2)\). No dense rank-one
outer-product update is executed.

The first matrix, its actions [(Setup-I.13)](#eq-setup-i-13), and data pairings cost, sufficiently,

<a id="eq-setup-i-18"></a>
\[
O\bigl(nd(1+m)+m^2d
 +J\{nd(m+N_x)+dmN_x+nm(m+N_x)(K+1)\}\bigr).
\tag{Setup-I.18}
\]

Here \(nd\) creates the first matrix, \(ndm\) evaluates its original
initialized training actions, and \(m^2d\) prepares the training input Gram.
Each panel charges its direct first-matrix actions, passive input inner products,
and all higher first-matrix coefficients. Its endpoint advancement fits the same
bound. Spatial input inner products are recomputed per panel to avoid storing
an \(m\)-by-\(N_x\) table.

The current-panel contractions [(Setup-I.12)](#eq-setup-i-12), readout/residual series arithmetic,
backward gate multiplication, and grouped factor formation are bounded by

<a id="eq-setup-i-19"></a>
\[
O\bigl(JL m(m+N_x)(K+1)^2(n+K+1)\bigr).
\tag{Setup-I.19}
\]

For [(Setup-I.12)](#eq-setup-i-12), caching all \(H_k^TX_c\) costs \(O(nmb(K+1)^2)\) for
a batch of \(b\) columns; their scalar weighted sums cost
\(O(mb(K+1)^3)\), and the final vector combinations cost
\(O(nmb(K+1)^2)\). Take \(b=m\) for training and \(b=1\) for
each passive query. The first-layer higher-coefficient term in [(Setup-I.18)](#eq-setup-i-18) is absorbed
by [(Setup-I.19)](#eq-setup-i-19). Its separate display explains where it is paid.

The degree-\(D\) polynomial activation backend costs

<a id="eq-setup-i-20"></a>
\[
O\bigl(L(D+1)^2+JLn(m+N_x)(D+1)(K+1)^2\bigr)
\tag{Setup-I.20}
\]

arithmetic, including coefficient construction and preparation of derivative
polynomials. Online training composition needs
\(O(Lmn(D+1)(K+1))\) words. One offline scalar composition may reuse
\(O((D+1)(K+1))\) scratch. No original derivative calls occur.

Use spatial-first projection. On panel \(b\), with time-node set \(I_b\),
form

<a id="eq-setup-i-21"></a>
\[
\mathcal B_{kc}^{(b)}
=\frac{\gamma_k}{N_t}\sum_{a\in I_b}
\cos(ku_a)((t_a-\tau_b)/\Delta_b)^c,
\quad \gamma_0=1,\quad\gamma_k=2\ (k>0).
\tag{Setup-I.21}
\]

These scalar tables cost \(O((N_t+J)(p+1)(K+1))\) arithmetic and
\(O((p+1)(K+1)+N_t+J)\) words. For every spatial query accumulate the
spherical coefficient of each local source coefficient, then transform only
the retained mode pairs. Here the local source coefficients must first be
converted from the unscaled convention in [the exact implicit execution and full costs subsection 2](#setup-implicit-2) to the affine coordinate
used by [(Setup-I.21)](#eq-setup-i-21): for a base field \(g\), define

\[
G_{b,c}^{\,g}(v_s)=\Delta_b^c[g(\tau_b+\cdot,v_s)]_c,
\qquad
\widetilde g_b(t,v_s)=\sum_{c=0}^K G_{b,c}^{\,g}(v_s)
                 ((t-\tau_b)/\Delta_b)^c.
\]

Consequently [(Setup-I.21)](#eq-setup-i-21) acts on \(G_{b,c}^{\,g}\), not on the raw Taylor
coefficients. Generate the powers of \(\Delta_b\) once per panel and
rescale before spatial accumulation. This costs
\(O(JLnN_x(K+1))\) arithmetic, absorbed by the following projection bound
because \(H_{\rm sph}\ge1\), and requires no additional vector buffer.
The full projection therefore costs

<a id="eq-setup-i-22"></a>
\[
O\bigl(LnJ(K+1)(N_xH_{\rm sph}+N)\bigr),\qquad
O(Ln(K+1)H_{\rm sph})\ \text{extra words}.
\tag{Setup-I.22}
\]

The completed global coefficient blocks use \(O(LnR)\) words. They are
not multiplied by the number of panels. Exact initialized-image actions have
already been paid in [(Setup-I.14)](#eq-setup-i-14)--[(Setup-I.16)](#eq-setup-i-16), including their answer vectors. The optional
sorting of time nodes costs \(O(N_t\log(2+N_t))\); a merge of the two
cosine-grid halves can improve it.

For clarity, the following geometry choice recomputes spherical values on each
panel. With the polar/azimuth orders defined after [(Setup-I.4)](#eq-setup-i-4), take

<a id="eq-setup-i-23"></a>
\[
G_{\rm time}=
\begin{cases}
N_t+J, & d=1,\\
N_t+N_x+JN_x(\ell_*+1), & d=2,\\
N_\theta^2+dN_\theta+N_t+N_\varphi+d
+d(\ell_*+1)^2
+JdN_x[1+(\ell_*+1)^2+H_{\rm sph}], & d\ge3,
\end{cases}
\tag{Setup-I.23}
\]

<a id="eq-setup-i-24"></a>
\[
G_{\rm memory}=
\begin{cases}
N_t+1, & d=1,\\
N_t+N_x+\ell_*+1, & d=2,\\
dN_\theta+N_t+N_\varphi
+d[1+(\ell_*+1)^2+H_{\rm sph}], & d\ge3.
\end{cases}
\tag{Setup-I.24}
\]

The rule and separated harmonic recurrences have numerical bounds
\(O(G_{\rm time})\), \(O(G_{\rm memory})\). The term
\(JdN_x\) includes repeated spatial coordinate/weight generation; it
is not charged only on the first panel. The normalization constants are
prepared once. The first case merely evaluates the two fixed points.
If a different geometry implementation is chosen, its matched time and memory
bounds must replace both [(Setup-I.23)](#eq-setup-i-23) and [(Setup-I.24)](#eq-setup-i-24).

Source orthogonalization, the conservative deterministic barrier selector,
small basis contractions, and retained metric/matrix formation cost

<a id="eq-setup-i-25"></a>
\[
O\bigl(LnRr+Lnr^3+(L-1)nr^2
       +L(qr^2+r^3+q^2r)+qd\bigr).
\tag{Setup-I.25}
\]

For orthogonalization, process each of at most \(R\) columns against at
most \(r\) basis columns. At each of \(9r_j\) selector steps, compute
the shifted \(r_j\)-dimensional inverses in \(O(r_j^3)\) and scan all
\(n\) row vectors in \(O(nr_j^2)\). Since \(r_j\le n\), their
sum is \(O(nr_j^3)\). This proves the selector term, with no assumed
fast spectral-selection routine. After item 4 of the inventory, multiplying
the returned basis images by \(U_j^T/n\) costs \(O(nr^2)\) per mixer.

For the metric, with selected rows \(P\), diagonal weights \(\mathsf D\),
and \(G=P^T\mathsf DP\), use

<a id="eq-setup-i-26"></a>
\[
M=\mathsf D+\mathsf DP(G^{-2}-G^{-1})P^T\mathsf D,\qquad
M^{-1}=\mathsf D^{-1}+P(I-G^{-1})P^T,
\quad P^TM=G^{-1}P^T\mathsf D.
\tag{Setup-I.26}
\]

All inverses in [(Setup-I.26)](#eq-setup-i-26) are on the \(r_j\)-dimensional positive Gram.
The displayed matrix products give \(O(qr^2+r^3+q^2r)\) work for
each layer and its retained caches; final mixer multiplication has the same
bound. Because \(q\ge r\), this term is at most \(O(Lq^2r)\),
but [(Setup-I.25)](#eq-setup-i-25) records its sources explicitly. First-weight restriction costs
\(O(qd)\). No initialized-matrix entry is needed in this stage.

Combining [(Setup-I.16)](#eq-setup-i-16)--[(Setup-I.25)](#eq-setup-i-25), one complete non-sampling, non-original-activation
arithmetic envelope is

<a id="eq-setup-i-27"></a>
\[
\begin{split}
T_{\rm setup}=O\bigl(&
nd(1+m)+m^2d+nm^2+m^3+L+d+m+1+L(D+1)^2\\
&+(L-1)nk_*^2
 +(L-1)nm(m+N_x)J(J-1)K(K+1)\\
&+J[nd(m+N_x)+dmN_x]
 +JLm(m+N_x)(K+1)^2(n+K+1)\\
&+JLn(m+N_x)(D+1)(K+1)^2\\
&+(N_t+J)(p+1)(K+1)
 +LnJ(K+1)(N_xH_{\rm sph}+N)\\
&+LnRr+Lnr^3+(L-1)nr^2
 +L(qr^2+r^3+q^2r)+qd\\
&+G_{\rm time}+N_t\log(2+N_t)\bigr).
\end{split}
\tag{Setup-I.27}
\]

For peak resident real words, including phase-specific buffers safely by their
sum, the matched sufficient envelope is

<a id="eq-setup-i-28"></a>
\[
\begin{split}
M_{\rm setup}=O\bigl(&
nd+(L-1)n[k_*+JmK]+Lmn(D+1)(K+1)\\
&+Lm^2(K+1)^2+LnR+Ln(K+1)H_{\rm sph}\\
&+Lq^2+q(d+Lm+1)+m^2+m(d+1)\\
&+L(D+1)+(p+1)(K+1)+N_t+J\\
&+G_{\rm memory}+L+d+m+1\bigr).
\end{split}
\tag{Setup-I.28}
\]

The \(qLm\) term permits final training feature/backward caches. They can
also be initialized directly by restriction of exact source features, with
zero backward fields. Copying/zeroing their arrays costs \(O(Lqm)\),
which fits \(LnRr\) because \(q\le9r\), \(m\le R\).
Other final state arrays fit [(Setup-I.25)](#eq-setup-i-25); initial readout-Gram construction is already
included in the first line of [(Setup-I.27)](#eq-setup-i-27). The \(Lmn(D+1)(K+1)\) term includes
ordinary training jets, and \(Lm^2(K+1)^2\) includes contraction caches.
One passive query's vector jets fit the same envelope because \(m,D\ge1\).
Small basis/selector arrays fit \(LnR\) and \(Lq^2\).

Unlike an explicit dense execution, [(Setup-I.27)](#eq-setup-i-27)--[(Setup-I.28)](#eq-setup-i-28) contain no mandatory hidden
matrix initialization, anchor materialization, source-image multiplication, or
final basis-image charge proportional to \(n^2\). All four are replaced by
the explicitly charged transcript operations. This is not a uniform promise
of subquadratic work at arbitrary orders: if \(k_*\), \(r\), or \(q\)
are large, the displayed bounds can exceed \(n^2\). A branch returning full
dense matrices necessarily has a quadratic output inventory. The present
claim concerns the analytic selected construction under the fresh implicit
reference contract.

<a id="setup-implicit-6"></a>
##### Primitive calls and supplementary costs

The explicit first matrix requires exactly \(nd\) independent standard
normal draws. By the sampler contract, the remaining draws are bounded by

<a id="eq-setup-i-29"></a>
\[
N_{\rm Gaussian}\le nd+n\sum_{j=2}^Lk_j
                 \le nd+(L-1)nk_*.
\tag{Setup-I.29}
\]

The count can be smaller than this because repeated/dependent directions need
no fresh innovation. There are no Gaussian readout draws and no need to draw
the as-yet unexposed part of any matrix. Sampling that part is only a possible
mathematical completion used to define the coupled reference.

The activation backend uses \(4(D+1)\) real scalar value calls per layer.
Exact original initialized features use \(nm\) value calls per layer.
Thus a sufficient original-activation call count is

<a id="eq-setup-i-30"></a>
\[
N_\phi=4L(D+1)+Lnm.
\tag{Setup-I.30}
\]

Add at most \(L\) calls if values \(\phi_j(0)\) needed to compute a
declared envelope have not been supplied. No high derivative, original
first-derivative, complex-activation, or trained-reference calls occur.
The backend's approximate value calls may use its specified accuracy; the
original initialized features use exact real values in the current model.
The equality proof requires the implicit and explicit executions to use the
same value oracle or the same supplied approximate backend samples.

For a reproducible separation of elementary evaluations from additions,
multiplications, divisions, and comparisons, define the angular table count

\[
A_{\rm elem}=
\begin{cases}
0,&d=1,\\
N_x,&d=2,\\
N_\theta+N_\varphi+d(\ell_*+1)^2,&d\ge3.
\end{cases}
\]

A sufficient total count of square roots, trigonometric and fixed
logarithmic/exponential/inverse-hyperbolic evaluations is

<a id="eq-setup-i-31"></a>
\[
N_{\rm elem}
=O\bigl(L+d+m+1+L(D+1)+N_t+A_{\rm elem}
             +(L-1)k_*+Lr\bigr).
\tag{Setup-I.31}
\]

The terms respectively cover scalar certificates, backend real cosine nodes,
time nodes, angular tables and normalization square roots, query-basis
normalizations in the sampler, and source orthogonalization. A Cholesky
factorization of the initial \(m\)-by-\(m\) Gram uses at most \(m\)
additional square roots, already covered. Shifted selector inverses and the
metric inverse can use elimination without spectral decompositions or further
special functions. Integer rounding/floor operations used to choose the orders
and enumerate the degree-dependent temporal cutoffs add
\(O(L+\ell_*+1)\) scalar operations; their arithmetic/memory fits the
geometry and mode inventory. The angular Gegenbauer normalizations are prepared
once, and the cosine/harmonic recurrences do not call trigonometric functions
anew at each coefficient or panel. Gaussian primitives themselves are counted
only in [(Setup-I.29)](#eq-setup-i-29); an implementation of the normal generator may add its own
elementary calls.

If each class of scalar primitive has respective maximum work costs
\(c_{\rm G},c_\phi,c_{\rm e}\) over the actual requested arguments and
accuracies, add

<a id="eq-setup-i-32"></a>
\[
c_{\rm G}N_{\rm Gaussian}+c_\phi N_\phi+c_{\rm e}N_{\rm elem}
\tag{Setup-I.32}
\]

to arithmetic work, with the optional \(L\) activation calls just described.
Add the maximum simultaneous scratch required by these routines to [(Setup-I.28)](#eq-setup-i-28).
One may instead sum the actual per-call costs. The usual bounded-cost primitive
model makes [(Setup-I.32)](#eq-setup-i-32) an operation-count shorthand, not a computability theorem for
arbitrary analytic functions or a bit-complexity result.

<a id="setup-implicit-7"></a>
##### Fixed-parameter specialization, proved from the full counts

Only in this section fix \(L,m,d,\gamma,Y>0\), admissible activation/source
bounds and confidence. At the certified original specialization
\(T=32(m/\gamma)\log(en)\), \(\eta=1/n\), the backend and bridge
give

\[
J=O(\log(en)^{3/2}),\qquad K=O(\log(en)),\qquad
D=O(\log(en)^{3/2}),
\]
\[
N_t,p+1=O(\log(en)^{5/2}),\quad
N_x,H_{\rm sph}=O(\log(en)^{3(d-1)/2}),
\]
<a id="eq-setup-i-33"></a>
\[
N,R,r,q=O(\log(en)^{3d/2+1}).
\tag{Setup-I.33}
\]

For \(d=1\), use the fixed two-point convention in place of angular growth;
it gives the same last exponent \(5/2\). The constants in [(Setup-I.33)](#eq-setup-i-33) may now depend
on the fixed admissible structural parameters. They were not hidden in [(Setup-I.27)](#eq-setup-i-27).

Substitution into [(Setup-I.14)](#eq-setup-i-14) first gives

<a id="eq-setup-i-34"></a>
\[
k_*=O(\log(en)^{3d/2+1}),\qquad JmK=O(\log(en)^{5/2}).
\tag{Setup-I.34}
\]

The two new width-dependent terms are therefore, respectively,

<a id="eq-setup-i-35"></a>
\[
nk_*^2=O(n\log(en)^{3d+2}),
\quad
nm(m+N_x)J(J-1)K(K+1)
=O(n\log(en)^{3d/2+7/2}).
\tag{Setup-I.35}
\]

The activation term has the second exponent in [(Setup-I.35)](#eq-setup-i-35). The local contraction
term proportional to \(n\) has exponent at most \(3d/2+2\).
The spatial-first projection terms have exponents at most
\(3d-1/2\) and \(3d/2+7/2\). Orthogonalization and small basis
contractions have exponents at most \(3d+2\). Finally,

<a id="eq-setup-i-36"></a>
\[
nr^3=O(n\log(en)^{9d/2+3}).
\tag{Setup-I.36}
\]

For every fixed integer \(d\ge1\),
\(3d+2\le9d/2+3\),
\(3d/2+7/2\le9d/2+3\), and
\(3d-1/2\le9d/2+3\). Thus every width-proportional term in [(Setup-I.27)](#eq-setup-i-27)
is bounded by [(Setup-I.36)](#eq-setup-i-36). The remaining terms, including final \(q^2r\)
assembly and geometry, are fixed powers of \(\log(en)\), hence also
bounded by [(Setup-I.36)](#eq-setup-i-36) for sufficiently large \(n\). This proves, with bounded-cost
scalar primitives,

<a id="eq-setup-i-37"></a>
\[
T_{\rm setup}=O(n\log(en)^{9d/2+3}).
\tag{Setup-I.37}
\]

For memory, the transcript and global coefficients are
\(O(n\log(en)^{3d/2+1})\). Rank-history and online activation storage
are \(O(n\log(en)^{5/2})\), which fit that bound because \(d\ge1\).
The spatial-first vector buffer is
\(O(n\log(en)^{3d/2-1/2})\). All remaining terms in [(Setup-I.28)](#eq-setup-i-28) are either
\(O(n)\) at fixed parameters or fixed powers of \(\log(en)\). Therefore

<a id="eq-setup-i-38"></a>
\[
M_{\rm setup}=O(n\log(en)^{3d/2+1}).
\tag{Setup-I.38}
\]

The primitive inventories specialize to
\(N_{\rm Gaussian}=O(n\log(en)^{3d/2+1})\),
\(N_\phi=O(n+\log(en)^{3/2})\), and a fixed power of \(\log(en)\)
for [(Setup-I.31)](#eq-setup-i-31). Additional costs from nonunit scalar backends remain governed by
[(Setup-I.32)](#eq-setup-i-32), not automatically by [(Setup-I.37)](#eq-setup-i-37).

The exact retained Harmonic state, metric, initial-matrix, and cache inventory
is unchanged, including its bound
\(1020(L+1)R^2+10m(d+1)\), hence
\(O(\log(en)^{3d+2})\) at [(Setup-I.33)](#eq-setup-i-33). The Gaussian transcripts, rank histories,
first matrix, source coefficients, bases, and local backend arrays are all
discarded after [(Setup-I.15)](#eq-setup-i-15) and the final caches are formed. The reference is a
coupled mathematical Gaussian network after disposal; the retained model does
not include an oracle or hidden reference access.

The proved source approximation and original all-time comparison then give
the same \(n^{-1+o(1)}\) prediction error under the same event and label
allowance. This component changes execution, not that error coefficient. For an
arbitrary supplied budget whose actual horizon or required accuracy grows
faster than in [(Setup-I.33)](#eq-setup-i-33), only the finite bounds [(Setup-I.14)](#eq-setup-i-14), [(Setup-I.27)](#eq-setup-i-27)--[(Setup-I.32)](#eq-setup-i-32) are asserted.
They do not imply the logarithmic specializations [(Setup-I.37)](#eq-setup-i-37)--[(Setup-I.38)](#eq-setup-i-38).

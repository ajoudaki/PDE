# From initialized onset fluctuations to nonlinear trajectory lower bounds

2026-10-04. Scoped continuation of the integrated study. This note proves
a lower bound in the same all-time, whole-sphere prediction norm as the
upper comparisons. It uses the initialized covariance CLT and the proved
complex-time source event. It does not take an infinitesimal-label limit,
assume a trained central limit theorem, or estimate a nonlinear remainder
by a width-independent \(O(Y^3)\) quantity.

Complete scientific inputs: EARLY_VARIABILITY_AND_STORAGE.md, in
particular its initialized CLT and exact onset formula; the complex
rectangle, RMS bounds and probability statement in
UNBOUNDED_COMPRESSOR_BRIDGE.md; and the power bounds in
SIMPLE_CONSTANTS_SOURCE_CHECK.md. These are current-study inputs. The
initialized CLT and source event remain inherited component results.
The derivative-to-real-supremum argument below is proved here.

## 1. Model, assumptions, and the observable

Fix \(L\ge2\), \(m,d\ge1\), unit training vectors
\(v_a=x_a/\sqrt d\), and a deterministic nonzero label vector \(y\).
Use two independent canonical width-\(n\) Gaussian initializations,
zero readout, mean squared loss, and block mobilities
\((n,1,\ldots,1,n)\). Every hidden layer trains. Denote the two actual
nonlinear predictors by \(f_n\) and \(\widetilde f_n\).

Activations may depend on the layer, are real on the real line, are
holomorphic on the common strip \(|\operatorname{Im}w|<a\), and have
bounded first derivative there. Their values need not be bounded. Put
\[
\beta=\max\left\{10,\ 1+\max_j|\phi_j(0)|,\ 16/a,\
\max_{j,k=1,2}\sup_{|\operatorname{Im}w|\le a/2}
                    |\phi_j^{(k)}(w)|\right\}.
\tag{1}
\]
Let \(Q^{(L)}\) be the initialized population training-feature covariance,
as defined below, and assume
\[
\gamma=\lambda_{\min}(Q^{(L)})>0,\qquad
\lambda=\gamma/m,\qquad Y=\|y\|_2/\sqrt m,\qquad
0<Y\le\lambda\beta^{-30L}.
\tag{2}
\]
The label condition is the existing sufficient condition for the source
event and all-time fitting. This note does not remove it.

The full prediction discrepancy is
\[
\mathcal D_n=
\sup_{t\in[0,\infty]}\sup_{\|v\|_2=1}
             |f_n(t,v)-\widetilde f_n(t,v)|.
\tag{3}
\]
The fitted endpoints exist on the inherited fitting event. Including
them in the supremum does not mean that the lower bound is attained at
the endpoint.

Fix a further unit query \(v_0\). All limits below keep the activation
functions, \(L,m,d\), data, and nonzero labels fixed while \(n\to\infty\).
The explicit dependence on \(m\) in later formulas is not a uniform
growing-\(m\) central limit theorem.

## 2. The inherited onset variance, defined explicitly

For indices \(0,\ldots,m\), define the augmented covariance recursion
\[
Q^{(0)}_{ab}=v_a^\top v_b,\qquad
Q^{(j)}_{ab}=\mathbb E[\phi_j(Z_a)\phi_j(Z_b)],
\quad Z\sim N(0,Q^{(j-1)}).
\tag{4}
\]
The training block of the final matrix in (4) is the matrix used in (2).
Let \(B_j\) be the covariance of the symmetric random matrix
\(\phi_j(Z)\phi_j(Z)^\top\), where \(Z\) has the covariance in (4).
For a symmetric perturbation \(E\), define
\[
\begin{aligned}
(T_jE)_{ab}={}&
\tfrac12E_{aa}\mathbb E[\phi_j''(Z_a)\phi_j(Z_b)]
 +E_{ab}\mathbb E[\phi_j'(Z_a)\phi_j'(Z_b)]\\
&+\tfrac12E_{bb}\mathbb E[\phi_j(Z_a)\phi_j''(Z_b)].
\end{aligned}
\tag{5}
\]
Use upper triangular coordinates on symmetric matrices, and set
\[
C_0=0,\qquad C_j=T_jC_{j-1}T_j^\top+B_j,\qquad
\sigma^2=\frac8{m^2}\sum_{a,b=1}^m y_a C_{L,0a,0b}y_b.
\tag{6}
\]
These are finite-dimensional Gaussian integrals. The inherited
initialized CLT allows singular intermediate covariances.

At zero readout, all hidden initial velocities vanish and
\[
\dot f_n(0,v_0)=\frac2m\sum_{a=1}^m
y_a\,\frac{\langle h_0^{(L)}(v_0),h_0^{(L)}(v_a)\rangle}{n}.
\tag{7}
\]
Consequently the initialized CLT gives, for independent copies,
\[
\sqrt n\,[\dot f_n(0,v_0)-\dot{\widetilde f}_n(0,v_0)]
\ \Longrightarrow\ N(0,\sigma^2).
\tag{8}
\]
This note assumes \(\sigma>0\) for its general conditional conclusion.
Section 6 gives a concrete broad subclass where this nondegeneracy is
proved for every nonzero label direction.

## 3. An elementary analytic derivative-to-supremum inequality

Let \(r>0\), and let \(g\) be holomorphic on a neighborhood of the closed
filled Bernstein ellipse of parameter 2 for the interval \([0,r]\). Its boundary
is the image of \(|w|=2\) under
\[
t=\frac r2\left(1+\frac{w+w^{-1}}2\right).
\]
Suppose \(|g|\le M\) on that ellipse. Then for every integer \(N\ge1\),
\[
\boxed{\sup_{0\le t\le r}|g(t)|
\ \ge\ \frac r{2N^2}|g'(0)|-24M\,2^{-N}.}
\tag{9}
\]

Here is a complete proof. Set \(F(x)=g(r(1+x)/2)\). The Laurent
expansion of \(F((w+w^{-1})/2)\) on the annulus containing
\(1/2\le|w|\le2\) is invariant under \(w\mapsto w^{-1}\).
Cauchy's coefficient estimate therefore gives its Chebyshev expansion
\[
F(x)=a_0+\sum_{k=1}^\infty a_kT_k(x),\qquad
|a_k|\le2M\,2^{-k}\quad(k\ge1).
\]
For the degree-\(N\) partial sum \(P_N\),
\[
\|F-P_N\|_{[-1,1]}\le2M\,2^{-N}.
\tag{10}
\]
Also \(T_k'(-1)\) has absolute value \(k^2\), so absolute convergence
of the derivative series and
\[
\sum_{k>N}k^2\,2^{-k}=2^{-N}(N^2+4N+6)
\]
give, after returning to physical time,
\[
\left|g'(0)-\frac2rP_N'(-1)\right|
\le\frac{4M}{r}\,2^{-N}(N^2+4N+6).
\tag{11}
\]

For completeness the required endpoint polynomial inequality needs no
unstated approximation theorem. Take the nodes
\(x_j=\cos(j\pi/N)\), \(0\le j\le N\), and their Lagrange polynomials
\(\ell_j\). The sign of \(\ell_j'(1)\) is \((-1)^j\): for \(j\ge1\)
this follows from the factors in its product formula, and
\(\ell_0'(1)=\sum_{j=1}^N(1-x_j)^{-1}>0\). Since
\(T_N(x_j)=(-1)^j\),
\[
\sum_{j=0}^N|\ell_j'(1)|
=\sum_{j=0}^N(-1)^j\ell_j'(1)=T_N'(1)=N^2.
\]
Interpolation proves
\(|P_N'(1)|\le N^2\|P_N\|_{[-1,1]}\); reflection proves the same at
\(-1\). This argument also works for complex polynomial coefficients.
Combining it with (10)--(11) yields
\[
|g'(0)|\le\frac{2N^2}{r}\|g\|_{[0,r]}
 +\frac{4M}{r}2^{-N}(2N^2+4N+6).
\]
Since \(2N^2+4N+6\le12N^2\) for \(N\ge1\), rearrangement gives (9).

## 4. Application on the proved complex-time event

Write \(\ell_n=\log(en)\), and use the explicit positive coefficient
\[
\vartheta=
\min\left\{1,\frac{a\lambda}
{1024Y^2\beta^{26L}\sqrt{d+3}}\right\},
\qquad r_n=\vartheta/\sqrt{\ell_n}.
\tag{12}
\]
This coefficient depends only on fixed problem parameters and is not
assumed to be a universal constant.

The source event proves holomorphy on a neighborhood of the time
rectangle with real range \([-r_t,T_n+r_t]\) and imaginary range
\([-r_t,r_t]\), where
\[
T_n=32\lambda^{-1}\ell_n,\qquad
r_t=\frac{c_t}{\sqrt{\ell_n}},\qquad
c_t=\frac{a\lambda}{1024Y^2U}.
\tag{13}
\]
Its numerical source bound \(U\le\beta^{26L}\sqrt{d+3}\) implies
\(r_n\le r_t\). Its width gates imply \(r_t\le1/\lambda\), hence
\(T_n\ge r_n\). The parameter-2 ellipse for \([0,r_n]\) has real range
\([-r_n/8,9r_n/8]\) and imaginary range
\([-3r_n/8,3r_n/8]\). It is therefore contained strictly inside the
proved rectangle.

On this complex domain the source RMS bounds give
\(\|h^{(L)}\|_{2,n}\le H_L\) and \(\|w\|_{2,n}\le S H_L\), with
\(S=16Y/\lambda\). Cauchy--Schwarz for the complex bilinear readout
gives
\[
|f_n(t,v_0)|\le S H_L^2.
\]
The checked power bound \(H_L\le\beta^{3L}\) shows that, for the
difference \(g_n(t)=f_n(t,v_0)-\widetilde f_n(t,v_0)\), one can take
\[
M=32\beta^{6L}Y/\lambda.
\tag{14}
\]
This bound is independent of width. It does not rely on individual
coordinate bounds of size \(\sqrt n\).

Let \(E_n\) be the event that the fitting/source conclusions hold for
both copies. The fixed finite union of their failure probabilities tends
to zero, so \(\Pr(E_n)\to1\). No independence between this event and
the onset observable is required.

Choose
\[
N_n=\left\lceil\frac{2\ell_n}{\log2}\right\rceil.
\]
Then \(N_n\le4\ell_n\) and \(2^{-N_n}\le n^{-2}\). Applying (9) gives
the deterministic inequality on \(E_n\)
\[
\boxed{
\sup_{0\le t\le r_n}|g_n(t)|
\ge\frac{\vartheta}{32\ell_n^{5/2}}|g_n'(0)|
 -\frac{768\beta^{6L}Y}{\lambda n^2}.}
\tag{15}
\]
Both terms concern the actual nonlinear trajectories. There is no
expansion in the label amplitude in (15).

## 5. General nondegenerate-onset lower theorem

Let \(\Phi\) be the standard normal distribution function. Under
(1)--(2), if the explicit variance (6) is positive, then for every
fixed \(u>0\),
\[
\boxed{
\liminf_{n\to\infty}
\Pr\left\{\mathcal D_n\ge
\frac{\vartheta\,u\sigma}
{64\sqrt n\,\log(en)^{5/2}}\right\}
\ge2[1-\Phi(u)].}
\tag{16}
\]
The same conclusion holds if \(\mathcal D_n\) on the left is replaced
by the supremum over the single query \(v_0\) and times
\(0\le t\le r_n\).

To prove this, the event \(|g_n'(0)|>u\sigma/\sqrt n\) has limiting
probability \(2[1-\Phi(u)]\) by (8). For sufficiently large widths,
\[
n^{3/2}\ge
\frac{49152\beta^{6L}Y}{\lambda\vartheta u\sigma}\,
\ell_n^{5/2};
\tag{17}
\]
all coefficients are fixed, so this numerical inequality eventually
holds. On its intersection with \(E_n\), (15) then gives the lower
threshold in (16). Subtracting \(\Pr(E_n^c)=o(1)\) proves (16).
This argument needs no joint CLT involving trained parameters.

For an ordinary confidence formulation, fix \(0<\delta<1\) and choose
\[
u_\delta=\Phi^{-1}(1/2+\delta/4)>0.
\tag{18}
\]
The right side of (16) is then \(1-\delta/2\). Thus there exists a
finite, not presently quantified width threshold such that the lower
bound in (16), with \(u=u_\delta\), holds with probability at least
\(1-\delta\) at each larger individual width. Its coefficient depends
on the requested confidence; a fixed positive Gaussian quantile does
not give probability tending to one.

This is an actual-prediction near-root lower bound in the common full
norm. It does not prove a strict constant-times-\(n^{-1/2}\) lower bound,
because of its logarithmic loss. The witnessing positive time may depend
on the realization and on \(n\); it lies in a shrinking initial interval.

## 6. Orthogonal data: every odd activation, every label direction

There is a concrete family with explicit \(m\), gap, and dimension
dependence. Take \(d=m+1\), training inputs \(v_a=e_a\),
\(1\le a\le m\), and query \(v_0=e_{m+1}\). The original inputs are
\(x_a=\sqrt d\,e_a\). Suppose each layer activation is odd and belongs
to the class in Section 1. Define the scalar moments
\[
q_0=1,\qquad
q_j=\mathbb E[\phi_j(\sqrt{q_{j-1}}Z)^2],\qquad
\alpha_j=\mathbb E[\phi_j'(\sqrt{q_{j-1}}Z)],
\quad Z\sim N(0,1).
\tag{19}
\]
Assume \(q_L>0\). Independence of the Gaussian coordinates and oddness
give \(Q^{(j)}=q_jI_{m+1}\). Hence the training covariance gap is exactly
\(\gamma=q_L>0\).

For the off-diagonal entries in the query row, the two diagonal terms
in (5) vanish, because the activation has zero Gaussian mean.
The remaining map is
\((T_jE)_{0a}=\alpha_j^2E_{0a}\).
For the new Gaussian innovation, independence and zero mean give
\[
B_{j,0a,0b}=q_j^2\,\mathbf1_{\{a=b\}}.
\]
Define
\[
\omega_0=0,\qquad \omega_j=\alpha_j^4\omega_{j-1}+q_j^2.
\tag{20}
\]
The covariance recursion (6) now gives
\[
C_{L,0a,0b}=\omega_L\mathbf1_{\{a=b\}},\qquad
\boxed{\sigma^2=8\omega_LY^2/m,\qquad \omega_L\ge q_L^2=\gamma^2.}
\tag{21}
\]
Thus every nonzero label direction has strictly positive onset variance.
No positive-label or label-alignment hypothesis has been introduced.

For this geometry the explicit time coefficient in (12) equals one.
Indeed Gaussian linear growth gives \(q_L\le\beta^{3L}\).
Using \(Y/\lambda\le\beta^{-30L}\), \(d=m+1\), and \(a\ge16/\beta\),
the second entry in the minimum (12) is at least
\[
\frac{\beta^{34L-1}m}{64\gamma\sqrt{m+4}}
\ge\frac{\beta^{31L-1}}{64\sqrt5}>1.
\tag{22}
\]
Here \(m/\sqrt{m+4}\ge1/\sqrt5\) for \(m\ge1\).

Combining (16), (21), and (22) gives the convenient explicit lower bound
\[
\boxed{
\liminf_{n\to\infty}
\Pr\left\{
\mathcal D_n\ge
\frac{u\gamma Y}{32\sqrt{mn}\,\log(en)^{5/2}}
\right\}\ge2[1-\Phi(u)]\qquad(u>0).}
\tag{23}
\]
We used the harmless weakening
\(\sqrt8/64\ge1/32\). For \(u=1\), the limiting lower probability is
approximately \(0.3173\). Taking (18) instead gives confidence
\(1-\delta\) for sufficiently large individual widths. The lower
coefficient retains the actual label RMS \(Y\).

For the canonical choice \(\phi_j=\tanh\), every \(q_j\) is positive,
and \(\alpha_j=1-q_j\). Therefore
\[
q_j=\mathbb E\tanh^2(\sqrt{q_{j-1}}Z),\qquad
\omega_j=(1-q_j)^4\omega_{j-1}+q_j^2.
\tag{24}
\]
One can use \(a=1/2\) and \(\beta=32\) in (1). To verify the strip
bounds directly, for \(w=x+iy\),
\[
|\cosh w|^2=\sinh^2x+\cos^2y,\qquad
|\tanh w|^2=
\frac{\sinh^2x+\sin^2y}{\sinh^2x+\cos^2y}.
\]
On the full strip \(|y|<1/2\), the derivative is bounded by
\(\sec^2(1/2)<2\). On the half strip, \(|\tanh w|\le1\), so its
second derivative is bounded by \(2\sec^2(1/4)<3\).
All hypotheses therefore hold at every fixed depth; the sufficient
label condition is \(0<Y\le(\gamma/m)32^{-30L}\).

## 7. What this proves and what remains excluded

The result is a lower bound for differences of actual nonlinear
predictions, at the same physical times and in the same full sphere norm
used by the upper comparisons. It repairs the derivative-to-trajectory
gap identified in EARLY_VARIABILITY_AND_STORAGE.md for strip-holomorphic
activations under the existing source event. It does not promote the
initialized derivative itself to a prediction observable without proof.

There is no universal positive lower bound over the entire allowed
activation class using only \(n,m,d,\gamma,Y\). For example, with \(m=1\)
and constant last activation \(\phi_L\equiv c\ne0\), the gap is \(c^2\)
but every initialization gives exactly
\(f_n(t,v)=y(1-e^{-2c^2t})\). Zero labels also give zero discrepancy.
For general activations, the label direction and the query geometry enter
the actual variance (6); \(\gamma>0\) alone does not replace its
nondegeneracy condition.

There is also no fitted-endpoint lower claim. At every fitted training
query both predictors converge to the same prescribed label. Even for
the untrained query in Section 6, this argument establishes a transient
discrepancy and does not determine its endpoint value. It proves neither
a trained or endpoint central limit theorem nor a necessary storage
lower bound against arbitrary representations.

Finally the initialized CLT and source probability limits have no
quantitative joint remainder in the inherited inputs. Consequently the
confidence-dependent sufficient width here is not effective. All
asymptotics are for fixed problem parameters; no simultaneous guarantee
over infinitely many independent widths or a growing sample dimension
has been asserted.

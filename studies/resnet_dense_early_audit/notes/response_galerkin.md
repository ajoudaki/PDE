# Response/Dyson, Galerkin, nonlinear-stability, and long-time audit

## Scope and verdict

This report addresses constructive roles 3--7 for the canonical dense
Euclidean continuous-depth \(\mu\)P model.  I read all five supplied project
notes.  Their most relevant lesson is that one must separate:

1. approximation of a *known bounded causal response problem*;
2. stability of the full training feedback loop under that approximation; and
3. conversion of that conditional approximation into a genuinely
   width-independent finite macroscopic compiler.

For the bounded residual-\(\tanh\) model, item 1 has a strong, elementary,
nonperturbative answer: a chronological (Dyson/Volterra) truncation has a
factorial tail in **depth**, even for noncommuting and nonnormal dense
generators.  This is fundamentally different from the divergent
initialization-time Wick--Taylor expansion in the earlier quadratic model.

Items 2 and 3 are not automatic.  A complete finite-time theorem is highly
plausible once the exact width-limit causal state has been constructed in a
norm in which its local contractions are continuous.  An all-training-time
theorem with approximation order independent of the horizon requires a
uniform coercivity/finite-arclength mechanism and a uniform response envelope.
Neither follows from squared loss and positive semidefiniteness alone in the
standard dense Euclidean model.  Thus:

> **Audited verdict.**  Finite-time response-Galerkin approximation is
> supported by a rigorous theorem skeleton and explicit, non-oracular
> residuals.  Uniform-\(t\geq0\), horizon-independent approximation is a
> credible but genuinely stronger conjecture.  Its decisive missing lemmas
> are uniform finite feature arclength (or an equivalent input-output
> stability estimate), uniform response-generator control, and a
> width-limit state-space tail theorem.  A factorial Dyson tail by itself
> does not prove any of these.

There is also a sharp negative finding:

> The full \(n\times n\) response \(J\) has no width-independent
> low-matrix-rank approximation, even at initialization.  Any admissible
> finite compiler must approximate scalar/macroscopic response contractions,
> a causal DMFT response kernel, or the action of \(J\) on the finitely many
> physically generated source directions.  Keeping finitely many depth modes
> whose coefficients are still \(n\times n\) matrices is not a
> width-independent neural PDE.

## 1. Audited response equations and normalized bounds

Write

\[
g_r=f_r-y_r,\qquad
D_r(s,t)=\operatorname{diag}\phi'(W(s,t)h_r(s,t)),
\]

and use the unit-output adjoint normalization

\[
q_r(1,t)=a(t),\qquad
-\partial_s q_r=W^\top D_rq_r.
\]

Thus

\[
\beta_r=D_rq_r,\qquad
A_r=D_rW.
\]

The forward causal response is

\[
\partial_sJ_r(s,u,t)=A_r(s,t)J_r(s,u,t),\qquad
J_r(u,u,t)=I ,
\tag{1}
\]

and

\[
q_r(u,t)=J_r(1,u,t)^\top a(t).
\tag{2}
\]

With \(G^h_{qr}=n^{-1}h_q^\top h_r\), Euclidean training gives

\[
\partial_tW(s,t)
=-\frac1n\sum_q g_q(t)\,\beta_q(s,t)h_q(s,t)^\top.
\tag{3}
\]

If \(v_r=\partial_t h_r\), then

\[
\partial_sv_r
=A_rv_r-\sum_qg_qD_r\beta_qG^h_{qr}.
\tag{4}
\]

The input condition is also residual-gated:

\[
v_r(0)
=-\sum_qg_q\,(x_q^\top x_r)\,
\operatorname{diag}\chi'(Bx_r)
\operatorname{diag}\chi'(Bx_q)q_q(0).
\tag{5}
\]

Consequently,

\[
\begin{aligned}
v_r(s)
={}&J_r(s,0)v_r(0)\\
&-\sum_qg_q\int_0^sJ_r(s,u)D_r(u)\beta_q(u)
G^h_{qr}(u)\,du .
\end{aligned}
\tag{6}
\]

This displays precisely why one-depth Grams do not close and why the
two-depth response is the correct next object.

For the finite-depth network, put \(\Delta=L^{-1}\) and

\[
A_{r,\ell}=D_{r,\ell}W_\ell,\qquad
J_r^{\ell,k}=
\prod_{j=k}^{\ell-1}(I+\Delta A_{r,j}),
\tag{7}
\]

with later-depth factors on the left.  Define the integrated generator size

\[
C_{r,L}(t)=
\Delta\sum_{\ell=0}^{L-1}\|A_{r,\ell}(t)\|_{\rm op}.
\tag{8}
\]

For \(\phi=\tanh\), \(\|D_{r,\ell}\|_{\rm op}\leq1\), hence

\[
C_{r,L}(t)\leq
\Delta\sum_\ell\|W_\ell(t)\|_{\rm op}.
\tag{9}
\]

This is the right control quantity.  A supremum over all layers is
unnecessarily strong and behaves badly when \(L\) independent Gaussian
matrices are used.  The averaged/integrated norm in (8) is exactly what the
chronological expansion needs.

### Finite-time a priori envelope from loss dissipation

The scaled Euclidean gradient flow has the exact energy identity

\[
-\dot{\mathcal L}
=\frac{\|\dot a\|^2}{n}
+\frac{\|\dot B\|_F^2}{n}
+\frac1L\sum_{\ell=0}^{L-1}\|\dot W_\ell\|_F^2.
\tag{10}
\]

Therefore, for \(0\leq t\leq T\),

\[
\frac1L\sum_\ell
\|W_\ell(t)-W_\ell(0)\|_{\rm op}
\leq
\sqrt{T\mathcal L(0)},
\tag{11}
\]

and

\[
\frac{\|a(t)-a(0)\|}{\sqrt n}
\leq\sqrt{T\mathcal L(0)}.
\tag{12}
\]

Since \(h_r(0)=\tanh(Bx_r)\) and each residual branch has magnitude at most
one coordinatewise,

\[
\sup_{r,s,t}\frac{\|h_r(s,t)\|}{\sqrt n}\leq2.
\tag{13}
\]

Combining (2), (8), and (12),

\[
\frac{\|q_r(s,t)\|}{\sqrt n}
\leq
\left(
\frac{\|a(0)\|}{\sqrt n}+\sqrt{T\mathcal L(0)}
\right)e^{C_{r,L}(t)}
\quad (t\leq T).
\tag{14}
\]

Thus on every fixed \(T\), the response, adjoint, and all normalized source
terms have width- and depth-uniform high-probability envelopes, provided the
initial averaged Gaussian operator norm is controlled.  At initialization
this average tends to the usual \(O(1)\) Gaussian operator-norm constant.

Equations (10)--(14) are useful positive evidence, but they grow at least
like \(\sqrt T\) in the available a priori estimate.  They do **not** yield
an all-time response envelope.

## 2. Dyson expansion: exact noncommutative tail theorem

For measurable \(A\) with

\[
C(s,u)=\int_u^s\|A(v)\|_{\rm op}\,dv<\infty,
\]

the chronological expansion is

\[
J(s,u)=I+\sum_{k\geq1}J^{[k]}(s,u),
\tag{15}
\]

\[
J^{[k]}(s,u)
=
\int_{u<s_1<\cdots<s_k<s}
A(s_k)\cdots A(s_1)\,ds_1\cdots ds_k .
\tag{16}
\]

No commutativity is used.  Directly,

\[
\|J^{[k]}(s,u)\|_{\rm op}
\leq\frac{C(s,u)^k}{k!},
\tag{17}
\]

and hence

\[
\boxed{
\left\|J-\sum_{k=0}^MJ^{[k]}\right\|_{\rm op}
\leq
R_M(C):=\sum_{k>M}\frac{C^k}{k!}
\leq e^C\frac{C^{M+1}}{(M+1)!}.
}
\tag{18}
\]

The same estimate holds before the depth limit.  Expanding (7) by ordered
subsets and using the elementary-symmetric-polynomial bound gives

\[
\left\|J_r^{\ell,k}-
\sum_{p=0}^MJ_{r,L}^{[p],\ell,k}\right\|_{\rm op}
\leq
\sum_{p>M}\frac{C_{r,L}(t)^p}{p!}.
\tag{19}
\]

This bound is uniform in \(n\), \(L\), matrix commutators, and matrix
dimension.  It is a real-axis depth estimate, not a training-time Taylor
estimate.  The zero-radius Wick--Taylor result in the project notes therefore
does not transfer to (18).

### Nonnormality audit

Nonnormality invalidates arguments based only on eigenvalues or spectral
abscissa.  For example,

\[
A=\begin{pmatrix}-\alpha&K\\0&-\alpha\end{pmatrix}
\]

has both eigenvalues \(-\alpha\), while

\[
e^{A\delta}
=e^{-\alpha\delta}
\begin{pmatrix}1&K\delta\\0&1\end{pmatrix}
\]

has transient amplification of order \(K\delta\).  Large Jordan blocks make
the same point more strongly.

This does **not** invalidate (18): the operator norm of the generator, or
more sharply its logarithmic norm, already accounts for nonnormal
amplification.  A hostile nonnormal example defeats only a tail estimate
that replaces \(C\) by an eigenvalue bound.  The correct alternatives are

\[
\|J(s,u)\|\leq
\exp\!\left(\int_u^s\|A(v)\|\,dv\right)
\]

or

\[
\|J(s,u)\|_2\leq
\exp\!\left(\int_u^s
\lambda_{\max}\frac{A(v)+A(v)^\top}{2}\,dv\right).
\tag{20}
\]

### A finite recursive response system

The Dyson terms themselves solve local causal equations:

\[
Z_0(s,u)=I,\qquad
\partial_sZ_k=A(s)Z_{k-1},\qquad
Z_k(u,u)=0,\quad k\geq1.
\tag{21}
\]

Then \(J_{\leq M}=\sum_{k=0}^MZ_k\) obeys the computable local residual

\[
\partial_sJ_{\leq M}-AJ_{\leq M}=-AZ_M,
\qquad
J_{\leq M}(u,u)=I.
\tag{22}
\]

Thus a non-oracular depth-response certificate is

\[
\rho^{\rm Dyson}_M(C_*)
=R_M(C_*),
\tag{23}
\]

where \(C_*\) is an a priori envelope obtained from the model class, not from
the exact positive-time response.

One can avoid storing \(J\) by applying the Volterra recursion only to the
finitely many forcing directions in (6).  This is computationally valuable,
but at finite width the resulting fields are still \(n\)-vectors.  It is not
by itself a width-independent macroscopic closure.

## 3. What Dyson truncation does not prove

Every Dyson word in (16) still contains products of full dense matrices.  A
finite number of word-length fields is therefore not yet a finite neural PDE
in the user's sense.  One still needs either:

1. a width-limit causal DMFT whose response objects are scalar kernels and
   finitely indexed contractions;
2. a path-law state with a proved finite chaos/cubature approximation; or
3. a theorem that only finitely many response actions generated by (6) are
   needed and that their joint law has a certified finite approximation.

The factorial bound controls the *chronological length* of the response.  It
does not control the number of Wick/Onsager contractions needed to evaluate a
word after the width limit, nor the complexity of the depth dependence of
\(A\).

This distinction is the main place where an apparently constructive proof
can accidentally retain the entire \(n\times n\) state.

### Matrix-rank obstruction

At zero depth separation \(J(u,u)=I_n\).  Hence, for every rank
\(R<n\),

\[
\inf_{\operatorname{rank}\widetilde J\leq R}
\|I_n-\widetilde J\|_{\rm op}=1,
\qquad
\inf_{\operatorname{rank}\widetilde J\leq R}
\frac{\|I_n-\widetilde J\|_F}{\sqrt n}
=\sqrt{1-\frac Rn}.
\tag{24}
\]

For small positive separation, all \(n\) singular values of \(J\) remain
near one under an \(O(1)\) generator bound.  Therefore a response
approximation that is low rank in neuron coordinates cannot have rank
independent of \(n\).  Low rank may be used in the two *depth* variables or
among finitely many sample-indexed scalar kernels, but not as a surrogate for
the dense neuron-space response.

## 4. Causal Galerkin approximations on the depth triangle

Let

\[
\Delta_2=\{(s,u):0\leq u\leq s\leq1\}.
\]

A convenient boundary-conforming representation is

\[
J_N(s,u)=I+(s-u)
\sum_{i+j\leq N}c_{ij}
P_i(2u-1)
P_j\!\left(2\frac{s-u}{1-u}-1\right),
\tag{25}
\]

with the corner \(u=1\) treated by the limiting value.  Piecewise-polynomial
finite elements on \(\Delta_2\) are an equally sound and often safer choice.
The factor \(s-u\) enforces \(J_N(u,u)=I\) exactly.

For an approximate generator \(A_N\), define

\[
r_{J,N}=\partial_sJ_N-A_NJ_N,
\qquad
b_{J,N}(u)=J_N(u,u)-I.
\tag{26}
\]

Duhamel's formula gives the a posteriori estimate

\[
\sup_{u\leq s}
\|J(A_N;s,u)-J_N(s,u)\|
\leq
e^{C_N}
\left(
\sup_u\|b_{J,N}(u)\|
+\sup_u\int_u^1\|r_{J,N}(s,u)\|\,ds
\right),
\tag{27}
\]

where \(C_N=\int_0^1\|A_N(s)\|\,ds\).

If \(A\) is the true generator,

\[
\|J(A)-J(A_N)\|
\leq
e^{C+C_N}\int_0^1\|A-A_N\|\,ds.
\tag{28}
\]

The first residual in (27) is fully computable from the approximate state.
The last term in (28) is not computable without the exact state unless it is
absorbed into the residual of the *full nonlinear macroscopic system*.  A
legitimate compiler should therefore certify an outgoing full-state
residual, not write \(\|A-A_N\|\) as an assumed small quantity.

### Approximation rates

If the scalar/macroscopic response kernels have a uniform
\(H^p(\Delta_2)\) bound, standard triangular finite elements or tensor
polynomials give an algebraic approximation rate.  With \(N\) modes in each
depth coordinate and \(O(N^2)\) total coefficients, a representative Jackson
rate is

\[
\|J-J_N\|_{L^2(\Delta_2)}
\lesssim N^{-p}
\asymp (\#\text{coefficients})^{-p/2}.
\tag{29}
\]

If the kernels extend analytically to a uniform complex neighborhood of the
triangle, an \(hp\) or spectral scheme can instead achieve

\[
\|J-J_N\|\lesssim e^{-cN}
=e^{-c\sqrt{\#\text{coefficients}}}.
\tag{30}
\]

Neither regularity statement follows merely from bounded \(\|A\|_{L^1}\).
The unit ball of \(L^1\) or \(L^2\) is not precompact in the relevant
topology, so its Kolmogorov widths do not tend to zero uniformly.

This matters for the canonical finite-depth initialization: the \(W_\ell\)
are independent across depth.  A piecewise interpolation need not converge
to a smooth matrix field as \(L\to\infty\).  The correct limit may be a Young
measure or an averaged depth-disorder state rather than a classical smooth
\(W(s)\).  A spectral Galerkin theorem cannot simply assume depth regularity
of this iid interpolation.  It must first derive the exact continuous-depth
macroscopic object and show that the scalar covariance/response kernels,
rather than the raw weights, possess the required regularity.

### Why observed singular-value decay must be interpreted carefully

Extend the causal kernel to the square by multiplying by
\(\mathbf1_{\{u\leq s\}}\).  Even with \(A=0\), the response action contains
the Volterra integration operator

\[
(Vb)(s)=\int_0^s b(u)\,du.
\]

Its singular values are exactly

\[
\sigma_k(V)=\frac{2}{(2k-1)\pi}.
\tag{31}
\]

Therefore the best rank-\(R\) error is only \(O(R^{-1})\) in operator norm
and \(O(R^{-1/2})\) in Hilbert--Schmidt norm.  Exponential singular-value
decay of the full square-extended causal kernel is impossible even in the
trivial response problem.

The correct numerical and analytic strategy is to retain the causal
Volterra/Heaviside primitive exactly and approximate only the smooth
amplitude \(J(s,u)-I\), the generator \(A\), or boundary-conforming fields on
the triangle.  Reported low-rank plots should subtract or factor the known
causal primitive; otherwise they mostly measure (31).

Generic Sobolev regularity in two variables also permits only algebraic
Kolmogorov-width decay such as (29).  Fast empirical decay is useful
evidence, but a universal exponential claim needs a uniform analyticity or
other structural theorem.

## 5. Positive-semidefinite tangent-kernel reconstruction

With the unit-output adjoint normalization, the exact continuum tangent
kernel is

\[
\Theta_{rq}
=G^h_{rq}(1)
+(x_r^\top x_q)G^\gamma_{rq}
+\int_0^1G^h_{rq}(s)G^\beta_{rq}(s)\,ds,
\tag{32}
\]

where

\[
\gamma_r=\operatorname{diag}\chi'(Bx_r)q_r(0),
\qquad
G^\gamma_{rq}=\frac1n\gamma_r^\top\gamma_q .
\]

Each matrix \(G^h(s)\), \(G^\beta(s)\), and \(G^\gamma\) is positive
semidefinite.  The data Gram is positive semidefinite, and the Schur product
theorem shows that every term in (32) is positive semidefinite.

An admissible approximation should preserve this factorization.  With
positive depth quadrature weights \(w_j\), set

\[
\boxed{
\Theta_M
=G^h_M(1)
+G^x\circ G^\gamma_M
+\sum_jw_j
\bigl(G^h_M(s_j)\circ G^\beta_M(s_j)\bigr).
}
\tag{33}
\]

If the approximate Grams are themselves built from finite feature factors or
positive cubature laws, then \(\Theta_M\succeq0\) exactly.

An even safer implementation is **discretize then adjoint**: construct the
finite forward Galerkin model, differentiate that same finite model, and
define \(\Theta_M\) as the Gram matrix of its approximate parameter
sensitivities.  This prevents a mismatch between the forward and adjoint
discretizations.

Entrywise projection of \(\Theta\), independent truncation of its moments, or
spectral quadrature with negative weights can create a spurious indefinite
kernel.  Clipping negative eigenvalues is a possible numerical repair, but
the factor construction (33) is structural and gives a cleaner theorem.

Positive semidefiniteness is not coercivity.  Adding an artificial ridge to
\(\Theta_M\) would change the optimizer and is disallowed.  If the true
kernel has a proved lower bound \(\Theta\succeq\lambda I\) and
\(\|\Theta-\Theta_M\|_{\rm op}\leq\lambda/2\), then the approximate kernel
inherits coercivity.  The lower bound itself must be proved from the standard
model; it cannot be inserted as a compiler feature.

## 6. Full nonlinear feedback stability

The response estimate must be propagated around the loop

\[
\text{response}\to
\text{feature/adjoint}\to
\text{kernel}\to
\text{training velocity}\to
\text{new response}.
\]

A useful abstract form of the exact macroscopic dynamics is

\[
\dot g=-\Theta(Z)g,\qquad
\dot Z=V(Z)g.
\tag{34}
\]

Here \(Z\) contains the forward, adjoint, response, and law/covariance state.
The second equation is linear in the residual vector because all Euclidean
parameter velocities, and hence the induced time derivatives of \(h,q,J\),
are linear in \(g\).  This residual-gated form is the correct replacement for
a generic \(\dot Z=F(Z)\) estimate.

Suppose on a restartable invariant tube:

\[
\Theta(Z)\succeq\lambda I,\qquad
\widehat\Theta(\widehat Z)\succeq\lambda/2\,I,
\tag{35}
\]

\[
\|\Theta(Z)-\Theta(\widetilde Z)\|
\leq L_\Theta\|Z-\widetilde Z\|,
\qquad
\|V(Z)-V(\widetilde Z)\|
\leq L_V\|Z-\widetilde Z\|,
\tag{36}
\]

and \(\|V(Z)\|\leq V_0\).  Let a finite compiler obey

\[
\dot{\widehat g}
=-\widehat\Theta(\widehat Z)\widehat g,
\]

\[
\dot{\widehat Z}
=\widehat V(\widehat Z)\widehat g+r_Z,
\qquad
\|r_Z(t)\|\leq\rho\,\|\widehat g(t)\|,
\tag{37}
\]

with

\[
\|\widehat\Theta(Z)-\Theta(Z)\|\leq\beta_\Theta,
\qquad
\|\widehat V(Z)-V(Z)\|\leq\beta_V .
\tag{38}
\]

Then

\[
I_g:=\int_0^\infty\|\widehat g(t)\|\,dt
\leq\frac{2\|\widehat g(0)\|}{\lambda}.
\tag{39}
\]

Writing \(E_Z=\|Z-\widehat Z\|\) and \(E_g=\|g-\widehat g\|\), variation of
constants and Gronwall give the explicit all-time bound

\[
\boxed{
\begin{aligned}
\sup_{t\geq0}E_Z(t)
\leq{}&
\bigg[
E_Z(0)+\frac{V_0}{\lambda}E_g(0)\\
&\quad+
\left(
\beta_V+\rho+\frac{V_0\beta_\Theta}{\lambda}
\right)I_g
\bigg]\\
&\times
\exp\!\left[
\left(L_V+\frac{V_0L_\Theta}{\lambda}\right)I_g
\right].
\end{aligned}
}
\tag{40}
\]

Moreover,

\[
\sup_{t\geq0}E_g(t)
\leq
E_g(0)+
\bigl(L_\Theta\sup_tE_Z(t)+\beta_\Theta\bigr)I_g.
\tag{41}
\]

Any Lipschitz output or Gram readout inherits the same uniform estimate.

This theorem closes the full high-to-low feedback loop.  The response tail
cannot return as an \(O(1)\) low-mode error when it is measured in a norm
that controls all contractions and when (35)--(38) hold.  By contrast, a
small coefficient tail in a norm under which the Gram/kernel contraction is
unbounded gives no such conclusion; this is precisely the high-to-low
failure mode identified in the earlier project audits.

For a Galerkin projection \(P_M\), the outgoing residual has the form

\[
r_{Z,M}
=(I-P_M)V(R_Mz_M)\,\widehat g,
\tag{42}
\]

so residual compatibility in (37) is automatic if the projection and
reconstruction are stable.

### Finite-time version

On \([0,T]\), uniform coercivity is not necessary.  Local boundedness and
Lipschitz continuity give the ordinary a posteriori estimate

\[
\sup_{t\leq T}\|Y(t)-Y_M(t)\|
\leq
e^{L_TT}
\left(
\|Y(0)-Y_M(0)\|
+\int_0^T\|r_M(t)\|\,dt
\right).
\tag{43}
\]

Equations (10)--(14) provide finite-\(T\) envelopes from the standard model.
The constant may be very poor and may grow quickly with \(T\), but this is a
real theorem route that does not assume horizon-independent compression.

## 7. A non-oracular residual/tail certificate

Let \(X\) be the exact causal macroscopic state space, once it has been
derived, and let

\[
\dot Y=\mathcal F(Y)
\tag{44}
\]

denote its local restartable evolution.  Let \(P_M:X\to X_M\) and
\(R_M:X_M\to X\) be a prescribed Galerkin projection/reconstruction, and let

\[
\dot y_M=P_M\mathcal F(R_My_M)
\tag{45}
\]

be the finite system.  Its reconstructed residual is

\[
\mathfrak r_M(t)
=\partial_t(R_My_M)-\mathcal F(R_My_M)
=-(I-R_MP_M)\mathcal F(R_My_M).
\tag{46}
\]

This is evaluated on the **approximate** trajectory, using the displayed
local equations.  It never queries the exact positive-time solution.

For an all-time residual-gated theorem, decompose the state as in (34) and
write

\[
\mathfrak r_{Z,M}(t)=E_M(t)\widehat g(t).
\]

A concrete proof-carrying certificate is

\[
\boxed{
\begin{aligned}
\rho_M={}&
\|R_My_M(0)-Y_0\|_X
+\sup_{t\geq0}\|E_M(t)\|\\
&+\sup_{t\geq0}
\|\Theta_M(t)-\Theta(R_My_M(t))\|_{\rm op}\\
&+\rho_M^{\rm Dyson}(C_*)
+\rho_M^{\rm depth}
+\rho_M^{\rm law}.
\end{aligned}
}
\tag{47}
\]

Here:

- \(\rho_M^{\rm Dyson}\) is the explicit tail (23);
- \(\rho_M^{\rm depth}\) is the boundary/local residual in (27), bounded by
  finite basis calculations or interval arithmetic;
- \(\rho_M^{\rm law}\) is the outgoing chaos/cubature/DMFT contraction
  residual, which lies outside the response calculation but is indispensable
  for width independence.

Every term is generated from the architecture, initialization law, local
causal equations, and the approximate solution.  No coefficient may be a
sample of the exact loss, exact response, or exact target time.

For a purely finite-time theorem, replace the suprema in (47) by the
corresponding \([0,T]\) norms and use (43).  For the all-time theorem, the
compiler must also output certified constants

\[
C_*,\quad\lambda,\quad
L_\Theta,\quad L_V,\quad V_0,
\tag{48}
\]

valid on a restartable tube and independent of the requested horizon.  Then
(40)--(41) convert \(\rho_M\to0\) into the requested observable error.

The anti-oracle condition becomes mathematically testable by requiring the
same compiler and constants uniformly over a compact neighborhood of
datasets, labels, initialization laws, and admissible restart states.  A
single canonical trajectory alone can always be hidden in arbitrary real
coefficients.

## 8. Long-time analysis: what squared loss does and does not give

The exact loss identity is

\[
\dot{\mathcal L}=-g^\top\Theta g,\qquad \Theta\succeq0.
\tag{49}
\]

This proves monotone loss and an \(L^2\)-in-time metric-speed bound.  It does
not prove:

\[
\int_0^\infty\|g(t)\|\,dt<\infty,
\tag{50}
\]

finite parameter/feature arclength, uniform kernel coercivity, or a uniform
bound on \(\int_0^1\|A(s,t)\|ds\).

The distinction is essential.  A simple residual-gated abstract system

\[
\dot g=-e^{-z}g,\qquad \dot z=g,\qquad g(0)=1,\ z(0)=0
\]

has

\[
g(t)=\frac1{1+t},\qquad z(t)=\log(1+t).
\]

Its kernel is nonnegative and its squared loss decreases, but
\(\int_0^\infty g\,dt=\infty\).  Thus positivity and loss convergence alone
cannot establish the effective finite training-time budget needed for hidden
Gram stability.

The earlier project stability result concerned a scalar loss after a known
kernel/profile defect was already small.  It did not prove stability of all
hidden Grams or the full response state.  Hidden directions are neutral at
zero residual.  For the present multi-sample problem, an all-time theorem for
every depthwise Gram therefore needs one of:

1. a uniform tangent-kernel gap \(\Theta(t)\succeq\lambda I\);
2. a directly proved uniform bound on total feature arclength;
3. a more general input-output stability estimate with an integrable
   propagator and an integrable residual budget.

### A legitimate small-residual bootstrap

There is one limited regime in which coercivity need not be assumed.  Suppose
the initial kernel satisfies \(\Theta(0)\succeq\lambda_0I\), and in a
normalized metric ball the kernel is \(L_\Theta\)-Lipschitz and bounded above
by \(\Lambda I\).  If

\[
\|g(0)\|
\leq
\frac{\lambda_0^2}{4L_\Theta\sqrt\Lambda},
\tag{51}
\]

then a bootstrap gives

\[
\Theta(t)\succeq\lambda_0/2\,I,\qquad
\int_0^\infty\|\dot\theta(t)\|_{\rm metric}\,dt
\leq
\frac{2\sqrt\Lambda}{\lambda_0}\|g(0)\|.
\tag{52}
\]

Indeed, the assumed gap gives exponential residual decay, (52) bounds the
distance traveled, and (51) prevents the kernel from losing half its initial
gap.  This is a possible rigorous all-time laboratory for sufficiently small
labels/residuals, provided the width-uniform Lipschitz constants are proved.
It should not be advertised as resolving the central \(O(1)\) feature-learning
regime without checking that the allowed class still exhibits nontrivial
Gram motion.

### Why horizon-independent \(M\) is presently conjectural

If one has uniform constants \(C_*\) and \(\lambda\), then:

- the Dyson order needed for response error \(\varepsilon\) depends only on
  \(C_*\) and \(\varepsilon\);
- \(\int_0^\infty\|g\|dt\) is finite;
- the response/Gram trajectory has finite arclength and converges;
- the compactified time orbit is precompact;
- (40) converts the outgoing residual to a uniform observable error.

In that case a horizon-independent \(M(\varepsilon)\) is mathematically
plausible.

Without those constants, the only audited a priori bound is
\(C_T=C_0+O(\sqrt T)\).  The required Dyson order can then grow with \(T\),
and the Galerkin family over \(t\in[0,T]\) need not be uniformly precompact as
\(T\to\infty\).  Numerical stabilization of rank/order is evidence for the
missing long-time lemma, not a proof of it.

## 9. Approximation-theory conclusions

1. **Dyson word length.**  Under an integrated operator envelope \(C_*\), the
   tail is factorial and completely insensitive to noncommutativity.

2. **Depth resolution.**  Word-length control does not control arbitrary
   depth oscillations.  Uniform \(H^p\), bounded-variation, analytic, or
   derived Young-measure regularity is needed for a quantitative finite
   depth basis.

3. **Causal low rank.**  The known Volterra factor has only \(1/k\) singular
   values.  Factor it exactly before assessing low-rank decay.

4. **Neuron-coordinate rank.**  Width-independent low rank is impossible by
   (24).  Approximate contractions, not \(J\) as an \(n\times n\) matrix.

5. **Kolmogorov widths.**  A uniform bounded set in \(L^2(\Delta_2)\) need not
   have widths tending to zero.  A uniformly \(H^p\) response family has
   algebraic widths; a uniformly analytic family can have spectral widths.
   The regularity class must be part of the conjecture and must be derived
   from the canonical initialization/dynamics.

6. **High-to-low feedback.**  An operator-norm response tail controls every
   normalized contraction by Cauchy--Schwarz.  A raw chaos-degree or
   coefficient tail may not, because high modes can contract into low Gram
   observables.  The residual norm in (47) must make the Gram and kernel
   readouts continuous.

## 10. Ranked remaining lemmas

### Tier 1: indispensable

1. **Exact restartable width-limit state.**  Construct the dense Euclidean
   causal DMFT/path-law state in a norm \(X\) that includes the response and
   makes every local Onsager/contraction rule and the Gram/kernel readout
   continuous.

2. **Uniform long-time response envelope.**  Prove
   \[
   \sup_{t\geq0}\int_0^1\|D_r(s,t)W(s,t)\|_{\rm op}\,ds\leq C_*
   \]
   or an equivalent logarithmic-norm bound, uniformly on the stated compact
   problem/restart class.

3. **Finite residual budget.**  Prove a uniform tangent-kernel gap, finite
   feature arclength, or an equivalent stable propagator estimate strong
   enough to replace (35) and (39).  PSD alone is insufficient.

4. **Outgoing residual theorem.**  Exhibit prescribed projections for the
   full DMFT/response state and compute
   \(\rho_M^{\rm law}+\rho_M^{\rm depth}\to0\) in the same norm.  It is not
   enough to assume the exact-state tail is small.

### Tier 2: needed for a quantitative compiler

5. **Depth regularity/Young-measure lemma.**  Resolve the iid-across-layer
   initialization issue and prove the scalar macroscopic response family has
   uniform approximability in the chosen causal basis.

6. **Nonlinear tube stability.**  Verify width-independent versions of
   \(L_\Theta,L_V,V_0\) and prove the abstract estimate (40) for the actual
   macroscopic equations, including response-to-adjoint and adjoint-to-kernel
   feedback.

7. **PSD-consistent discretize-adjoint theorem.**  Show that the finite
   Galerkin/cubature forward model and its discrete adjoint produce (33) and
   that its kernel defect is bounded by the same residual certificate.

8. **Uniform restart class.**  Define a compact neighborhood of positive-time
   states on which all constants and residual estimates remain valid.  This
   is required to exclude single-trajectory oracle playback.

### Tier 3: rate improvements, not logical prerequisites

9. Prove Sobolev or analytic regularity yielding an explicit algebraic or
   spectral mode count.

10. Prove singular-value/Kolmogorov-width decay after factoring the exact
    causal Volterra primitive.

11. Derive sharper logarithmic-norm estimates that reduce the pessimism of
    the operator-norm Dyson bound in nonnormal regimes.

## 11. Recommended numerical falsification targets

The response experiments should distinguish four ranks/orders:

1. Dyson word order;
2. depth finite-element/spectral order after factoring the Volterra kernel;
3. rank of scalar sample-indexed response contractions;
4. forbidden neuron-coordinate rank of the full \(J\).

For each training restart, measure:

\[
C(t)=\sup_r\int_0^1\|A_r(s,t)\|_{\rm op}\,ds,
\]

the actual Dyson error versus \(R_M(C(t))\), the outgoing Galerkin residual
in (26)/(46), the smallest eigenvalue of the factorized kernel (33), and the
training-time integral \(\int_0^T\|g(t)\|dt\).  The key all-time diagnostic is
whether \(C(t)\), the required mode count, and this residual integral
stabilize as \(T\) increases.

Strongly nonnormal tests should compare the observed amplification with the
operator/logarithmic-norm bound, not with generator eigenvalues.  Singular
values should be plotted both before and after removing the known causal
Volterra factor.  Any claimed horizon-independent compression should be
retested from positive-time restarts and nearby labels/data so that a
single-trajectory fitted basis cannot pass.

## Final classification

### Proved at the response-analysis level

- The discrete and continuum dense response has the noncommutative factorial
  Dyson tail (18)--(19) under an integrated operator envelope.
- Nonnormality does not invalidate that tail; it invalidates spectral-only
  estimates.
- Finite-time parameter-energy bounds give finite-\(T\), width/depth-uniform
  response envelopes.
- Boundary-conforming Galerkin residuals imply the a posteriori response
  estimate (27).
- The tangent kernel can and should be reconstructed PSD by (33).
- Under explicit coercivity, Lipschitz, and residual-gating hypotheses, the
  full feedback loop has the horizon-independent error bound (40)--(41).
- Width-independent low rank of the full neuron-space response is impossible.

### Strongly supported but conditional

- A finite-time finite response-Galerkin approximation of the exact dense
  width-limit causal state.
- Horizon-independent approximation in a sufficiently small,
  uniformly-coercive residual basin.

### Genuinely conjectural

- Uniform-\(t\geq0\) finite response-PDE approximation for an \(O(1)\)
  compact label/data class under ordinary dense Euclidean \(\mu\)P training.
- Stabilization of approximation order with training horizon.
- Uniform singular-value/Kolmogorov-width decay of the full response family.

### Falsified

- The claim that a formal Dyson truncation alone closes the nonlinear
  training dynamics.
- Any proof based only on eigenvalue stability in the nonnormal case.
- Any width-independent neuron-coordinate low-rank approximation of \(J\).
- Any claim that PSD of the tangent kernel alone supplies all-time
  coercivity or finite feature arclength.
- Any unqualified claim of exponential causal-kernel singular-value decay
  without first factoring the Volterra/Heaviside primitive.

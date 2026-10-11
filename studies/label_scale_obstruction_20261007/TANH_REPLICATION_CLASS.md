# Exact replication tests for two-hidden-layer tanh minima

2026-10-10. Internal continuation of the same study, written in the reused
`two_layer_persistence` context. This is a derivation, not an independent
promotion review or promoted book material. Scientific inputs are the
canonical model, `TANH_BAD_BASIN.md`, `TANH_GEOMETRY.md`, and the explicitly
scoped replication and robustness calculations reproduced below. No
experiment or other-study input is used.

Source SHA-256 values at writing: `TANH_BAD_BASIN.md`,
`f975c3bd44d9ad97ca22102908e69a181ac1bd4de491781497e9ce65d3d55a53`;
`TANH_GEOMETRY.md`,
`3ac627b10bfe44001724359a0917b201577238a8312df907f79f7031e1e00cd0`.

The results classify the Hessian at a specified replicated critical profile;
they do not classify all neural-network minima. Rank one admits exact,
data-dependent criticality and second-order tests, with robust attracting
minima when all normal curvatures are strict. Equal replication of an
arbitrary width-`k` profile has an exact Hessian decomposition and necessary
and sufficient positive-semidefiniteness conditions. The multi-prototype
conditions below are checkable hypotheses: no satisfying example with
`k>1` is constructed here.

The proof first separates average motions from neuron-splitting motions.
It then identifies every splitting coordinate that has no square term:
its mixed Hessian coefficients must vanish for a minimum to be possible.
Strict positivity in the remaining normal directions gives an actual
attracting critical manifold. Reaching that manifold from zero readout is
a separate, explicitly conditional step.

## 1. Canonical network, residuals, and physical time

Let `m` samples have normalized inputs `xbar_a=x_a/sqrt(d)` in `R^d` and
labels `y_a` in `R`. Sphere inputs have `||xbar_a||=1`; the algebra below
also holds without that restriction. At hidden width `n`, put
\[
\begin{aligned}
U_{ja}&=\tanh(A_{j:}\bar x_a),&
Z_{ia}&=\sum_jW_{ij}U_{ja},& H_{ia}&=\tanh Z_{ia},\\
f_a&=\frac1n\sum_iw_iH_{ia},& r_a&=f_a-y_a,&
\mathcal L&=\frac1m\sum_ar_a^2.
\end{aligned}
\tag{1}
\]
Here `A` is `n by d`, `W` is `n by n`, and `w` is in `R^n`. Residuals
always mean actual, unrescaled residuals `f-y`. The mobilities are
`(n,1,n)` and dots denote physical-time derivatives:
\[
\dot A=-n\nabla_A\mathcal L,\qquad
\dot W=-\nabla_W\mathcal L,\qquad
\dot w=-n\nabla_w\mathcal L.
\tag{2}
\]
The inverse-mobility metric is
\[
\|\delta\theta\|_{M_n^{-1}}^2
=\frac1n\|\delta A\|_F^2+\|\delta W\|_F^2
+\frac1n\|\delta w\|^2.
\tag{3}
\]
Thus `dot L=-||dot theta||^2_{M_n^{-1}}`. On any finite interval `[s,t]`,
the displacement in this metric is at most
`sqrt((t-s)(L(s)-L(t)))`. Smooth local solutions cannot escape to infinity in
finite time, so (2) has global forward solutions. Indeed, a finite maximal
time would give a Cauchy parameter path by this same estimate, a finite
limit, and continuation by smooth local existence.

For any straight parameter variation `delta theta`, let `delta f` and
`delta^2 f` denote the first and second derivatives of the prediction
along that parameter line. The exact loss Hessian is
\[
D^2\mathcal L[\delta\theta,\delta\theta]
=\frac2m\sum_a\bigl[(\delta f_a)^2+r_a\delta^2f_a\bigr].
\tag{4}
\]
The metric does not change whether this quadratic form has a negative
direction. The metric matters for dynamics and rates, which are handled
separately below.

## 2. Rank-one profiles: arbitrary-data criticality and Hessian tests

Fix `p in R^d` and `q,s in R`, and consider the symmetric width-`n` state
\[
A_{j:}=p^\top,\qquad W_{ij}=q/n,\qquad w_i=s.
\tag{5}
\]
For each sample define
\[
\begin{aligned}
t_a&=p^\top\bar x_a,&u_a&=\tanh t_a,&\chi_a&=\tanh'(t_a),&
\tau_a&=\tanh''(t_a),\\
z_a&=q u_a,&h_a&=\tanh z_a,&\psi_a&=\tanh'(z_a),&
\sigma_a&=\tanh''(z_a).
\end{aligned}
\]
Its prediction is `s h_a`, residual is `r_a=s h_a-y_a`, and reduced loss is
\[
J(p,q,s)=\frac1m\sum_a(s h_a-y_a)^2.
\tag{6}
\]
The restriction of (3) to (5) is exactly
`||delta p||^2+delta q^2+delta s^2`. The symmetric subspace is invariant
under (2): it is fixed by arbitrary permutations of the first-layer
neurons and, independently, of the top-layer neurons, and both the loss
and the metric have these symmetries. Uniqueness preserves this fixed
subspace. Hence its physical dynamics is ordinary Euclidean gradient
flow of `J`, independent of `n`.

Assume throughout this section that `s q != 0`. The following three
identities are necessary and sufficient for reduced criticality and,
equivalently, full criticality at (5):
\[
\sum_a r_a h_a=0,\qquad
\sum_a r_a\psi_a u_a=0,\qquad
\sum_a r_a\psi_a\chi_a\bar x_a=0.
\tag{7}
\]
The last equality is an equality in `R^d`. To verify this, the reduced
gradients are respectively `2/m` times the first expression,
`2s/m` times the second, and `2sq/m` times the third. Direct full-network
differentiation gives the same moments, with only neuron-dependent
prefactors. The condition `sq!=0` permits the two cancellations; no claim
that (7) is necessary is made when either factor vanishes.

Define the scalar and symmetric matrix
\[
\alpha=\sum_a r_a\sigma_a u_a^2,\qquad
B=\sum_a r_a\psi_a\tau_a\bar x_a\bar x_a^\top\in\mathbb R^{d\times d}.
\tag{8}
\]
All the tests in (7)--(8) use the actual data, labels, and candidate
profile; they impose no pair symmetry or engineered moment construction.

For an arbitrary full-network variation define
\[
a_j=\delta A_{j:}^\top,\qquad
b_i=\sum_j\delta W_{ij},\qquad c_i=\delta w_i,
\quad
\bar a=\frac1n\sum_ja_j,\quad
\bar b=\frac1n\sum_ib_i,\quad
\bar c=\frac1n\sum_ic_i.
\]
At a critical profile satisfying (7), the exact variance decomposition is
\[
\begin{aligned}
D^2\mathcal L[\delta\theta,\delta\theta]
={}&D^2J[(\bar a,\bar b,\bar c),(\bar a,\bar b,\bar c)]\\
&+\frac{2}{mn}\left[
s\alpha\sum_i(b_i-\bar b)^2
+sq\sum_j(a_j-\bar a)^\top B(a_j-\bar a)
\right].
\end{aligned}
\tag{9}
\]
The proof is the `k=1` specialization of the all-variation calculation in
Section 4. A direct verification is also short: the top-preactivation
variation is
`delta Z_ia=u_a b_i+q chi_a xbar_a^T bara`; the residual-weighted mixed
readout/splitting term vanishes by the second identity in (7), and the
mixed `delta W,delta A` splitting term vanishes by its third identity.
The two activation-second-derivative terms left over are precisely (8).

For completeness, the reduced Hessian in (9) can be evaluated without any
implicit network derivatives. For a reduced direction
`(delta p,delta q,delta s)`, put
\[
\begin{aligned}
\delta z_a&=u_a\delta q+q\chi_a\bar x_a^\top\delta p,\\
\delta^2z_a&=2\chi_a\delta q\,\bar x_a^\top\delta p
+q\tau_a(\bar x_a^\top\delta p)^2,\\
\delta f_a&=h_a\delta s+s\psi_a\delta z_a,\\
\delta^2f_a&=2\delta s\,\psi_a\delta z_a
+s\bigl[\sigma_a(\delta z_a)^2+\psi_a\delta^2z_a\bigr].
\end{aligned}
\tag{10}
\]
Insert these in (4) to obtain `D^2J`.

**Rank-one second-order test.** At a critical profile with `sq!=0`, and
for any `n>=2`, the full Hessian is positive semidefinite if and only if
\[
D^2J\succeq0,\qquad s\alpha\ge0,\qquad sqB\succeq0.
\tag{11}
\]
Indeed coherent variations realize every reduced direction. Opposite
variations in two row sums realize any zero-mean `b` direction; opposite
first-layer variations in two neurons realize any zero-mean `a`
direction. These can be chosen independently, as shown more generally
in Section 4. Formula (9) proves sufficiency and these independent
directions prove necessity. For `n=1` only the reduced-Hessian condition
is needed because there are no splitting directions.

These are necessary second-order conditions for a local minimum, not
sufficient conditions in the semidefinite boundary cases. A zero
eigenvalue can require higher-order analysis.

Every point of the affine set
\[
\mathcal M_n(p,q,s)=
\left\{A_{j:}=p^\top\ \forall j,\quad
W\mathbf1=q\mathbf1,\quad
\frac1n\mathbf1^\top w=s\right\}
\tag{12}
\]
has the same predictions and is critical. The top derivatives use the
first two identities in (7). The first-layer derivative for neuron `j`
is a scalar multiple of the zero vector in the third identity, even
when `sum_i w_i W_ij` varies with `j`. This proves exact criticality,
not just a Hessian-kernel statement.

For `n>=2`, the full Hessian is positive definite normal to (12), with
kernel exactly its tangent space, if and only if
\[
D^2J\succ0,\qquad s\alpha>0,\qquad sqB\succ0.
\tag{13}
\]
Under these conditions, (9) forces every zero quadratic direction to
have `a_j=0`, `b_i=0`, and `barc=0`, precisely the tangent equations of
(12). Conversely, a failed strict inequality in (13), while (11)
holds, produces an additional non-tangent zero direction by the same
independent variations. Section 5 proves that (13) gives an open
attracting neighborhood. Positive residual norm gives a positive-loss
minimum; calling it nonglobal additionally requires a lower-loss witness.

## 3. Equal replication of an arbitrary width-k network

Use (1) now at a fixed seed width `k>=1`, with seed parameters `(A,W,w)`.
First-layer prototype indices are `j=1,...,k` and top-layer prototype
indices are `i=1,...,k`. Define sample-dependent quantities at this seed:
\[
\begin{aligned}
t_{ja}&=A_{j:}\bar x_a,& u_{ja}&=\tanh t_{ja},&
\chi_{ja}&=\tanh'(t_{ja}),&\tau_{ja}&=\tanh''(t_{ja}),\\
z_{ia}&=\sum_jW_{ij}u_{ja},&h_{ia}&=\tanh z_{ia},&
\psi_{ia}&=\tanh'(z_{ia}),&\sigma_{ia}&=\tanh''(z_{ia}).
\end{aligned}
\]
Write `u_a=(u_ja)_{j=1}^k`,
`f_a=k^{-1} sum_i w_i h_ia`, and `r_a=f_a-y_a`. Define
\[
\begin{aligned}
p_i&=\sum_a r_a\psi_{ia}u_a\in\mathbb R^k,\\
T_i&=\sum_a r_a\sigma_{ia}u_au_a^\top\in\mathbb R^{k\times k},\\
v_{ij}&=\sum_a r_aw_i\psi_{ia}\chi_{ja}\bar x_a\in\mathbb R^d,\\
B_j&=\sum_a r_a\tau_{ja}
\left(\sum_iw_iW_{ij}\psi_{ia}\right)
\bar x_a\bar x_a^\top\in\mathbb R^{d\times d}.
\end{aligned}
\tag{14}
\]
The vector `p_i` in this section is not the rank-one input parameter `p`
of Section 2. Formula (14) defines it as a residual-feature moment.
The matrices `T_i,B_j` are symmetric, with no assumed sign.

The seed is critical if and only if
\[
\sum_a r_a h_{ia}=0\quad\forall i,\qquad
w_i p_i=0\quad\forall i,\qquad
\sum_iW_{ij}v_{ij}=0\quad\forall j.
\tag{15}
\]
These follow by differentiating the three parameter blocks; every
gradient has the common factor `2/(mk)`. In particular, stationarity
does not in general give `p_i=0` when `w_i=0`, or `v_ij=0` separately
for each pair.

Let the replication multiplicity be an integer `ell>=1`, and let
`n=k ell`. Copies of prototype `j` are indexed by `beta=1,...,ell`, and
copies of prototype `i` by `alpha=1,...,ell`. Define the lifted state
\[
\widetilde A_{j\beta,:}=A_{j:},\qquad
\widetilde W_{i\alpha,j\beta}=W_{ij}/\ell,\qquad
\widetilde w_{i\alpha}=w_i.
\tag{16}
\]
Every first-layer copy has feature `u_ja`, every top copy has
preactivation `z_ia`, and the prediction is unchanged because the
readout sum and its width normalization are both multiplied by `ell`.

**Exact lifting.** Replication preserves the loss, takes critical points
to critical points, and takes every physical seed trajectory with
mobilities `(k,1,k)` to a physical width-`n` trajectory with mobilities
`(n,1,n)`.

To verify the last assertion, direct differentiation gives
\[
\nabla_{\widetilde A_{j\beta,:}}\mathcal L_n
=\frac1\ell\nabla_{A_{j:}}\mathcal L_k,\quad
\partial_{\widetilde W_{i\alpha,j\beta}}\mathcal L_n
=\frac1\ell\partial_{W_{ij}}\mathcal L_k,\quad
\partial_{\widetilde w_{i\alpha}}\mathcal L_n
=\frac1\ell\partial_{w_i}\mathcal L_k.
\tag{17}
\]
Multiplying the first and third identities by `n=k ell` gives exactly
the replicated seed velocities; the middle identity gives
`dot Wtilde=dot W/ell`. The restriction of the width-`n` metric also
agrees exactly with the seed metric:
\[
\frac1n\|\delta\widetilde A\|_F^2
+\|\delta\widetilde W\|_F^2
+\frac1n\|\delta\widetilde w\|^2
=\frac1k\|\delta A\|_F^2+\|\delta W\|_F^2
+\frac1k\|\delta w\|^2.
\tag{18}
\]
This is an exact invariant family of the original dense model, not a
change of optimizer or inner-layer scaling.

## 4. All variations and the exact lifted Hessian

Consider an arbitrary variation of the lifted parameters, not necessarily
one that preserves (16). Define its first-layer and readout variations,
and its sums over each first-layer copy group, by
\[
a_{j\beta}=\delta\widetilde A_{j\beta,:}^\top,\qquad
c_{i\alpha}=\delta\widetilde w_{i\alpha},\qquad
b_{i\alpha,j}=\sum_\beta\delta\widetilde W_{i\alpha,j\beta}.
\]
Their averages and zero-mean parts are
\[
\begin{aligned}
\bar a_j&=\frac1\ell\sum_\beta a_{j\beta},&
\widehat a_{j\beta}&=a_{j\beta}-\bar a_j,\\
\bar B_{ij}&=\frac1\ell\sum_\alpha b_{i\alpha,j},&
\widehat b_{i\alpha,j}&=b_{i\alpha,j}-\bar B_{ij},\\
\bar c_i&=\frac1\ell\sum_\alpha c_{i\alpha},&
\widehat c_{i\alpha}&=c_{i\alpha}-\bar c_i.
\end{aligned}
\tag{19}
\]
Here `barB` is an averaged parameter variation, not the curvature matrix
`B_j` in (14). Let `hatb_iα` denote the vector with components
`hatb_iα,j`. The remaining column-group sums needed by the Hessian are
\[
d_{ij\beta}=\sum_\alpha\delta\widetilde W_{i\alpha,j\beta}
-\bar B_{ij},\qquad \sum_\beta d_{ij\beta}=0.
\tag{20}
\]
The coherent seed variation is
`delta theta_0=(delta A_{j:}=bara_j^T, delta W=barB, delta w=barc)`.

**Independent realization of these variables.** The coherent variables
and all hatted and `d` variables can be prescribed independently subject
only to their displayed zero-sum constraints. Set
\[
\begin{aligned}
\delta\widetilde A_{j\beta,:}&=(\bar a_j+\widehat a_{j\beta})^\top,\\
\delta\widetilde w_{i\alpha}&=\bar c_i+\widehat c_{i\alpha},\\
\delta\widetilde W_{i\alpha,j\beta}
&=\frac{\bar B_{ij}+\widehat b_{i\alpha,j}+d_{ij\beta}}\ell
+E_{i\alpha,j\beta},
\end{aligned}
\tag{21}
\]
where each `ell by ell` block `E_{i:,j:}` has zero row sums and zero
column sums. Summing (21) over `beta` and then over `alpha` recovers
(19)--(20). Conversely, subtract the first term on its last line from
any `delta Wtilde`; the remainder has precisely those zero row and
column sums. Thus (21) represents every variation, and none of the
splitting coordinates in the next formula are fictitiously independent.

**Exact Hessian identity.** At the lifted profile (16),
\[
\begin{aligned}
D^2\mathcal L_n[\delta\widetilde\theta,\delta\widetilde\theta]
={}&D^2\mathcal L_k[\delta\theta_0,\delta\theta_0]\\
&+\frac{2}{mk\ell}\sum_{i,\alpha}
\left[w_i\widehat b_{i\alpha}^\top T_i\widehat b_{i\alpha}
+2\widehat c_{i\alpha}p_i^\top\widehat b_{i\alpha}\right]\\
&+\frac{2}{mk\ell}\sum_{j,\beta}
\left[\widehat a_{j\beta}^\top B_j\widehat a_{j\beta}
+2\sum_i d_{ij\beta}v_{ij}^\top\widehat a_{j\beta}\right].
\end{aligned}
\tag{22}
\]
This identity itself does not require the seed to be critical. In
particular, the doubly centered blocks `E` are invisible to the Hessian
at the replicated profile.

**Derivation.** Write
\[
\zeta_{ia}=\sum_j\bar B_{ij}u_{ja}
+\sum_jW_{ij}\chi_{ja}\bar x_a^\top\bar a_j.
\]
Differentiating the top preactivation gives
\[
\delta\widetilde Z_{i\alpha,a}
=\zeta_{ia}+\widehat b_{i\alpha}^\top u_a,
\tag{23}
\]
and its second derivative is
\[
\delta^2\widetilde Z_{i\alpha,a}
=2\sum_{j,\beta}\delta\widetilde W_{i\alpha,j\beta}
\chi_{ja}\bar x_a^\top a_{j\beta}
+\sum_j\frac{W_{ij}}\ell\tau_{ja}
\sum_\beta(\bar x_a^\top a_{j\beta})^2.
\tag{24}
\]
Averaging the first prediction variation over top copies cancels every
hat term. Consequently `delta f` is exactly the seed prediction
variation induced by `delta theta_0`, so its squared part in (4) is
the seed squared part.

The full second prediction variation is
\[
\delta^2f_a=\frac1{k\ell}\sum_{i,\alpha}
\left[2c_{i\alpha}\psi_{ia}\delta\widetilde Z_{i\alpha,a}
+w_i\left\{\sigma_{ia}
(\delta\widetilde Z_{i\alpha,a})^2
+\psi_{ia}\delta^2\widetilde Z_{i\alpha,a}\right\}\right].
\tag{25}
\]
In the first term of (25), averaging leaves the coherent term plus
`2 hatc_iα psi_ia (hatb_iα^T u_a)`. Contracting against `r_a` gives
the `p_i` term in (22). In the square term, averaging (23) eliminates
its mean/fluctuation cross term and leaves
`wi sigma_ia (hatb_iα^T u_a)^2`, giving `wi T_i`.

For the first term of (24), use the identity
\[
\sum_{\alpha,\beta}
\delta\widetilde W_{i\alpha,j\beta}a_{j\beta}
=\ell\bar B_{ij}\bar a_j
+\sum_\beta d_{ij\beta}\widehat a_{j\beta}.
\tag{26}
\]
It follows by first summing over `alpha` in (20) and then using both
zero-mean conditions. Its first summand gives the coherent mixed
derivative; its second gives the `d v` term in (22). Finally,
\[
\frac1\ell\sum_\beta(\bar x_a^\top a_{j\beta})^2
=(\bar x_a^\top\bar a_j)^2
+\frac1\ell\sum_\beta(\bar x_a^\top\widehat a_{j\beta})^2.
\]
The second term gives `B_j`. Substituting in (4) proves (22), including
the factor `2/(mk ell)`.

**Lifted second-order criterion.** Suppose the seed is critical and
`ell>=2`. Its lifted Hessian is positive semidefinite if and only if
\[
\begin{gathered}
D^2\mathcal L_k\succeq0,\\
p_i=0,\quad w_iT_i\succeq0\quad\text{for every }i,\\
v_{ij}=0\quad\text{for every }i,j,\qquad
B_j\succeq0\quad\text{for every }j.
\end{gathered}
\tag{27}
\]
These are in particular necessary for the lift to be a local minimum.
They are sufficient for Hessian semidefiniteness, not by themselves for
a local minimum.

To prove necessity, first suppress all fluctuations in (21); this tests
every coherent seed direction. For a fixed top prototype `i`, prescribe
`hatb_i1=v`, `hatb_i2=-v` and
`hatc_i1=t`, `hatc_i2=-t`, with other variables zero. The splitting
form, up to a positive factor, is
`wi v^T T_i v+2t p_i^T v`. There is no `t^2` term. If `p_i!=0`, choose
`v=p_i` and choose the sign and sufficiently large magnitude of `t` to
make it negative. Thus `p_i=0`. Taking `t=0` then forces `wi T_i>=0`.

For fixed `i,j`, prescribe
`hata_j1=a`, `hata_j2=-a`,
`d_ij1=t`, `d_ij2=-t`, with other variables zero. The corresponding
form is, again up to a positive factor,
`a^T B_j a+2t v_ij^T a`. A nonzero `v_ij` yields a negative direction
by choosing `a=v_ij` and a suitable `t`, so all `v_ij` must vanish.
Setting `t=0` then forces `B_j>=0`. Formula (21) verifies that these
tests create no unintended coherent or other splitting variables.
Conversely, (27) makes every summand of (22) nonnegative.

The equality requirements in (27) are substantive. Ordinary seed
criticality supplies only the weighted sums in (15). In particular,
replication of an arbitrary strict seed minimum need not remain a local
minimum: a nonzero pairwise `v_ij` creates a strict negative direction.

## 5. Strict conditions, an exact critical manifold, and trapping

Assume a critical seed satisfies
\[
\begin{gathered}
D^2\mathcal L_k\succ0,\qquad p_i=0\quad\forall i,
\qquad v_{ij}=0\quad\forall i,j,\\
w_iT_i\succ0\quad\forall i,\qquad
B_j\succ0\quad\forall j.
\end{gathered}
\tag{28}
\]
These are sufficient conditions, not an existence assertion. The strict
matrix inequality implies `wi!=0` for every `i`. Consequently
\[
\sum_a r_a\psi_{ia}\chi_{ja}\bar x_a=v_{ij}/w_i=0
\quad\text{for every }i,j.
\tag{29}
\]

The following affine set consists entirely of critical points with the
seed predictions and seed loss:
\[
\mathcal M_{k,\ell}=
\left\{
\begin{array}{ll}
\widetilde A_{j\beta,:}=A_{j:}&\text{for every }j,\beta,\\
\displaystyle\sum_\beta\widetilde W_{i\alpha,j\beta}=W_{ij}
&\text{for every }i,\alpha,j,\\
\displaystyle\frac1\ell\sum_\alpha\widetilde w_{i\alpha}=w_i
&\text{for every }i.
\end{array}\right\}.
\tag{30}
\]
Indeed all first features are fixed, each top copy still has the seed
preactivation, and averaging the readouts preserves the prediction.
The readout gradient vanishes by (15). Each top-weight gradient is
proportional to a component of `p_i=0`. Each first-weight gradient is a
sum over `i,alpha` of scalar weight products times the zero vector in
(29). Thus all gradients vanish even away from the exactly equal-copy
center, as long as (30) holds.

At the equal-copy center, (22) and (28) show that the Hessian kernel is
exactly
\[
\delta\widetilde A=0,\qquad
\sum_\beta\delta\widetilde W_{i\alpha,j\beta}=0,
\qquad \sum_\alpha\delta\widetilde w_{i\alpha}=0.
\tag{31}
\]
To see this, vanishing of the coherent positive form forces
`bara=barB=barc=0`, and the other strict forms force `hata=hatb=0`.
The unrestricted `d`, `E`, and zero-mean `hatc` are precisely the
tangent variables in (31). Conversely those tangent directions make
every term vanish. Hence the Hessian is positive definite on a
complement of the tangent space of (30).

Here is the local attraction argument with the required hypotheses
explicit. It applies equally to the rank-one manifold (12) under (13).
Choose fixed linear coordinates `(xi,eta)` centered at the replicated
point, with `xi` normal and `eta` tangent to the affine critical
manifold; locally that manifold is `xi=0`. For every nearby `eta`,
the loss at `(0,eta)` equals the constant `L_*` and its full gradient
vanishes. The normal Hessian is positive definite at the center.
Continuity therefore gives a small convex product neighborhood and
constants `0<c<C<infinity` on which
\[
c I\preceq\partial_\xi^2\mathcal L\preceq C I.
\]
Taylor's integral formula along `(t xi,eta)` gives
\[
\frac c2\|\xi\|^2\le E:=\mathcal L-\mathcal L_*
\le\frac C2\|\xi\|^2,\qquad
\|\partial_\xi\mathcal L\|\ge c\|\xi\|.
\tag{32}
\]
The second inequality follows by taking the scalar product of
`partial_xi L` with `xi` and integrating the positive normal Hessian.
The fixed coordinate change and positive metric (3) imply, for a
constant `c_0>0`,
\[
\|\dot\theta\|_{M_n^{-1}}=\|\nabla\mathcal L\|_{M_n}
\ge c_0\sqrt E.
\tag{33}
\]
As long as the path stays in this neighborhood, loss dissipation gives
`dot E<=-c_0^2 E`. If `E>0`, it also gives
\[
\int_{t_0}^{t}\|\dot\theta\|_{M_n^{-1}}\,ds
\le\frac2{c_0}\bigl(\sqrt{E(t_0)}-\sqrt{E(t)}\bigr).
\tag{34}
\]
This follows by writing the speed as `-dot E/speed` and using (33).
If `E=0`, (32) puts the point on the critical manifold and the speed
is zero. Choose the initial point in a sufficiently small inner
neighborhood so the upper bound `2 sqrt(E(t0))/c0` is less than its
distance to the outer boundary. A first-exit contradiction proves it
never leaves. Formula (34) makes the path Cauchy at infinity, and (32)
places its limit on the critical manifold. This proves an open
attracting neighborhood at every fixed width.

The radii and constants in this full-space trapping proof may depend
on `k,ell`, the dataset, and the seed. No width-uniform lower bound on
their size is asserted. A positive seed loss stays positive on (30).
Nonglobality requires an attainable smaller loss, established for the
full-rank setting in Section 7.

For perspective, `D^2 L_k>0` already forces the seed first-feature and
top-feature matrices to have row rank `k`. Otherwise a nonzero top
weight direction `delta W_i:=v^T` with `v^T U=0`, or a nonzero readout
direction with `H^T delta w=0`, would leave the prediction constant
along an entire parameter line and contradict positive definiteness.
Thus a satisfying seed with `k>1` would genuinely have more than one
feature prototype. No such seed is supplied by this note.

## 6. Robustness of the strict rank-one case

Let the finite dataset, including labels, be denoted by
`D=(xbar_1,...,xbar_m,y_1,...,y_m)`. Suppose that at a dataset `D_0`, a
rank-one critical point `(p_*,q_*,s_*)` has `s_*q_*!=0`, positive loss,
and satisfies (13). Then there is one neighborhood of `D_0`, independent
of `n`, on which a nearby strict rank-one critical profile exists and
satisfies all the same strict inequalities.

Here and below, input perturbations may be arbitrary in `R^d`; for the
sphere model take the intersection with the product of unit spheres,
giving a relatively open data neighborhood. No pairing or symmetry
of the perturbed samples is imposed.

To prove the assertion, the function `J_D(p,q,s)` is jointly smooth in
its finite data and parameters. The derivative in `(p,q,s)` of its
gradient at the base point is the invertible matrix `D^2J_{D_0}`.
The finite-dimensional implicit-function theorem, in the form that a
smooth equation `F(theta,D)=0` with invertible `D_theta F` has a unique
nearby smooth solution `theta(D)`, therefore supplies
\[
(p_D,q_D,s_D),\qquad \nabla J_D(p_D,q_D,s_D)=0.
\]
Continuity preserves nonzero `s_D q_D`, positive residual norm, positive
definiteness of `D^2J_D`, and both strict inequalities involving (8).
All of these tests are on the same `d+2` reduced coordinates and do not
contain the width. Formula (9) and Section 5 then give an attracting
critical manifold at every `n>=2`, with possibly width-dependent
full-space neighborhoods.

This proves robustness of existence and local attraction. It does not
on its own prove that a trajectory starting at zero readout enters
the attracting neighborhood.

There is also a width-independent robustness statement for reachability
when a seed path is known. Assume that for `D_0` the reduced physical
trajectory beginning at some fixed `(p_0,q_0,0)` converges to
`(p_*,q_*,s_*)`. Then, after shrinking the same data neighborhood, the
reduced trajectory from that same initial point converges to
`(p_D,q_D,s_D)` for every nearby dataset. This conclusion holds in the
physical reduced coordinates without taking a small-label limit.

Here are the trapping and continuity details. Choose a closed ball
around the base minimum, small enough that the base reduced Hessian
is uniformly positive definite throughout. On that ball, uniform
continuity after a small data perturbation gives
`D^2 J_D >= lambda I` for a fixed `lambda>0`, and the continued minimum
lies in the inner quarter-ball. Strong convexity gives a uniform
strict gap between its loss and every boundary loss: the boundary
distance from the moving minimum is at least three quarters of the
radius, and its excess is at least `lambda/2` times the squared
distance.

The known base trajectory enters a smaller interior sublevel at a
finite time `T`. The smooth finite-dimensional ODE and its initial
condition have continuous dependence on `D` over `[0,T]`: on a compact
tube around the base path the vector fields have a common local
Lipschitz bound, and the integral equations plus Gronwall's inequality
bound the path difference by a constant times the data perturbation.
Thus the same perturbed trajectory enters below the uniform boundary
gap at that same `T`. Monotonicity traps it in the ball. Strong
convexity gives
\[
\|\nabla J_D\|^2\ge2\lambda(J_D-J_D(p_D,q_D,s_D)),
\]
by applying its supporting quadratic inequality at the current point
and completing the square. Therefore the loss excess decays
exponentially, and the quadratic lower bound forces convergence to
the moving minimum. All steps concern the width-independent reduced
flow, so the data neighborhood and `T` are independent of `n`.

At each width, Section 7 then pulls back its full attracting
neighborhood to an open zero-readout basin. Its size need not be
uniform in width or data. The explicit seed path in
`TANH_BAD_BASIN.md`, Section 4, verifies the extra reachability premise
for that constructed example after one sufficiently small positive
label scale is fixed independently of width. Its strict inequalities
are precisely (13), as its displayed Hessian and residual moments
show. Consequently its bad-basin existence extends to a genuine open
set of input/label datasets, not merely to perturbations preserving
the nine residual moments.

The same automatic robustness assertion is not available from (28)
for a general multi-prototype seed. The pairwise equalities `v_ij=0`
are stronger than seed criticality (15). An implicit-function
continuation of a strict seed minimum guarantees (15), not those
extra equalities. A small nonzero `v_ij` gives a negative direction
after replication by the necessity proof of (27).

## 7. Conditional zero-readout reachability and Gaussian consequences

Suppose a seed width-`k` trajectory with initial readout exactly zero
is known to converge to a critical seed satisfying (28). For every
integer `ell>=2`, its exact replicated trajectory, by (17), converges
to the center (16) of the full attracting manifold (30). At each
fixed width choose a finite time at which that reference trajectory
enters the open attracting neighborhood of Section 5. The preimage
of that neighborhood under the finite-time flow, restricted to the
initial slice `w=0`, is a nonempty open set of hidden parameters
containing the replicated seed start. Every such start converges to
the same positive-loss critical manifold if the seed loss is positive.

Only continuity of the forward finite-time map is needed for this
pullback; it need not be onto or injective on the zero-readout slice.
The same argument applies at every `n>=2` to a rank-one seed satisfying
(13) with a known zero-readout trajectory, including the robust
rank-one trajectories in Section 6. No zero-readout trajectory is
constructed by the general replication criterion itself.

For completeness, full-rank starts and nonglobality can be guaranteed
under a separate elementary data condition. Suppose the normalized
inputs are nonzero, pairwise distinct and nonantipodal unit vectors,
and `n>=m`. The functions
`g -> tanh(g^T xbar_a)` are linearly independent. Indeed choose `b`
avoiding the finitely many proper hyperplanes defined by
`b^T xbar_a=0` and `b^T(xbar_a +/- xbar_c)=0`. The nonzero absolute
projections are distinct. In a putative relation, restrict `g=t b`
and absorb projection signs into its coefficients to get
`sum_a c_a tanh(t b_a)=0` with `0<b_1<...<b_m`. Sending `t` to
infinity first gives `sum c_a=0`. Subtract that constant relation,
multiply by `exp(2b_1 t)`, and use
`tanh(bt)-1=-2 exp(-2bt)(1+o(1))` to deduce `c_1=0`. Induction
annuls every coefficient.

Thus evaluation vectors span `R^m`, and `m` first-layer rows can be
chosen to make `U` have column rank `m`; pad with rows if necessary.
Given such `U`, prescribe the first `m` rows of `WU` to be
`delta I_m`, with `delta!=0`, and the remaining rows to be zero.
This is realizable because `U` has the left inverse
`U^+=(U^T U)^{-1}U^T`, satisfying `U^+ U=I_m`, and one may set
`W=Z U^+`. The resulting
first `m` rows of `H` form the invertible matrix `tanh(delta) I_m`.

Consequently the real-analytic function on the connected hidden
parameter space
\[
P(A,W)=\det(U^\top U)\det(H^\top H)
\tag{35}
\]
is not identically zero. Its nonzero set is open and dense. Density
can be justified without a measure-zero theorem: vanishing on any
open ball would imply vanishing on every line from its center by the
one-variable real-analytic identity principle, hence everywhere.
Every nonempty open hidden basin therefore intersects the open set
where both feature matrices have column rank `m`, and that intersection
is nonempty and open. This rank conclusion is conditional on first
having the open zero-readout basin from a known seed trajectory.

For any fixed finite label vector, a full-rank `H` also permits solving
`H^T w/n=y`. Thus the global minimum loss is zero under this data and
width condition. Any positive-loss critical manifold considered here
is then genuinely nonglobal.

Under the canonical initialization, the entries of `A` are independent
`N(0,1)`, the entries of `W` are independent `N(0,1/n)`, these blocks
are independent, and `w=0` exactly. At every fixed width the hidden
law has strictly positive density everywhere. Each nonempty open
hidden basin, including its full-rank intersection, therefore has
strictly positive probability. This argument supplies no lower bound
uniform in width: those probabilities may go to zero. It supplies no
Gaussian failure conclusion at all if zero-readout reachability has
not first been proved.

## 8. Exact scope and unresolved implications

The claim levels are as follows.

| Statement | Status and required scope |
|---|---|
| Replication preserves predictions, criticality, and physical trajectories | Exact, every `k>=1`, `ell>=1`, and finite dataset |
| All-variation Hessian identity (22) | Exact, no criticality needed |
| Positive-semidefinite lifted Hessian iff (27) | Exact at a critical seed, `ell>=2` |
| Attracting critical manifold from (28) | Proved conditional sufficiency, each fixed width |
| Rank-one tests (7), (11), and strict-normal test (13) | Exact for `sq!=0`, with splitting tests for `n>=2` |
| Robust strict rank-one minima under arbitrary small data/label perturbations | Proved; one data neighborhood independent of width |
| Robust zero-readout capture in that data neighborhood | Proved only when a convergent reference zero-readout seed path is known |
| Positive fixed-width Gaussian mass and full-rank starts | Conditional on open zero-readout capture; full rank additionally uses the data/width condition in Section 7 |
| Existence of a strict multi-prototype seed satisfying (28) with `k>1` | Not constructed here |

No statement here says that all local minima are replicated profiles,
that Hessian semidefiniteness settles higher-order flat directions, or
that fitting follows outside this class. The general lift concerns
widths `n=k ell`; rank one covers every width. The results do not
control escape to infinite parameters, Gaussian probabilities as
`n` grows, avoidance of saddle stable sets on the exact zero-readout
slice, or uniform all-time fitting. They also do not establish an
incompressibility claim. These are distinct obligations, not consequences
of the exact finite-dimensional splitting calculation.

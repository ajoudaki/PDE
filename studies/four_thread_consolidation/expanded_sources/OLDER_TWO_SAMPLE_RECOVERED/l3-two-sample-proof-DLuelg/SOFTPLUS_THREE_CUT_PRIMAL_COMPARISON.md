# Short finite reference bounds and asymmetric three-cut comparison

Auxiliary reference result, 2026-09-06. This note proves the short primal
estimates and the local vector-field comparison suggested in
`SOFTPLUS_LOCAL_BOOTSTRAP_PLAN.md`. It does not identify a Gaussian program,
construct a mean-field limit, or assert global gradient-flow continuation.

The plan does not specify a loss derivative multiplying the two sample
contributions. We make the label-average normalization explicit below:
the coefficients are \(y_+=1,y_-=-1\), and each sum has weight \(1/2\).
The short bounds also hold for any sample coefficients of absolute value
at most one. The precise extension of the comparison to state-dependent
coefficients is given at the end. An unspecified, unbounded loss derivative
is not implicitly included in the numerical constants.

The proof first closes a primal box using the contraction of each cut,
then uses exact Euler product identities to control forward increments.
For comparison, it always puts a gate difference next to an **old** cut
field. This yields a sum of cap contributions, with no products of caps.

## 1. Norms, inputs, activation, and the three cuts

Fix a finite width \(n\geq1\). On \(E_n=\mathbb R^n\) use the ordinary
Euclidean norm divided by \(\sqrt n\), and its associated inner product:

\[
 \|v\|_n=\frac{\|v\|_{\mathrm{Euclidean}}}{\sqrt n},
 \qquad \langle u,v\rangle_n=\frac1n\sum_{i=1}^n u_iv_i.
\]

For raw first-layer coordinates \(\Theta\in\mathbb R^{n\times2}\), set

\[
 \|\Theta\|_{n,2}
   =\frac1{\sqrt n}\left(\sum_{i=1}^n\sum_{j=1}^2\Theta_{ij}^2\right)^{1/2}.
\]

An effective middle operator \(W:E_n\to E_n\) acts by ordinary matrix
multiplication. Its operator norm is the ordinary Euclidean operator
norm. Its Hilbert--Schmidt norm as an operator on \(E_n\) is

\[
 \|W\|_{\mathrm{HS}}=\left(\sum_{i,j}W_{ij}^2\right)^{1/2}.
\]

In particular, there is no extra \(n^{-1/2}\) in this operator HS norm.
For \(u,v\in E_n\), write

\[
 (u\otimes_n v)f=u\langle v,f\rangle_n,
 \qquad u\otimes_n v=\frac{uv^{\mathsf T}}n.
\]

Directly from this formula,

\[
 \|u\otimes_n v\|_{\mathrm{HS}}
 =\|u\|_n\|v\|_n,
 \qquad \|W\|_{\mathrm{op}}\leq\|W\|_{\mathrm{HS}}.
 \tag{1}
\]

The first equality follows by summing \(u_i^2v_j^2/n^2\); the second follows
by applying Cauchy--Schwarz to each matrix row. Adjoint means \(W^*=W^{\mathsf T}\),
with respect to the displayed RMS inner products.

For every \(-1\leq\rho\leq1\), put

\[
 a=\sqrt{(1+\rho)/2},\qquad b=\sqrt{(1-\rho)/2},
 \qquad x_+=(a,b),\quad x_-=(a,-b).
\]

These two vectors have norm one and Gram matrix

\[
 C_{cd}=x_c\cdot x_d,
 \qquad C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}.
 \tag{2}
\]

This is an exact coordinate description of RMS-normalized canonical
inputs, not a change of their normalization. If the original inputs in
R^d are X_c with ||X_c||^2/d=1, represent X_c/sqrt(d) in an orthonormal
basis of their span by x_c as above, using the nonzero coordinate only
at a rank-one endpoint. If Q is that orthonormal basis matrix, the
corresponding trainable first coordinates are Theta=sqrt(d) W^(1)Q.
Their RMS Frobenius squared norm is exactly the canonical raw metric
d||dW^(1)||_F^2/n on increments in this span. Directions perpendicular
to the input span are frozen and can be retained unchanged. Unused
coordinates in the two-column presentation are set to zero if the
span has dimension one; no extra random seed is introduced. Independent
N(0,1/d) first-weight entries give the required Gaussian preactivation
pair with covariance C. Equations (9) and (13) are therefore precisely
the canonical first-weight and first-preactivation feature updates.

Here and below \(c,d\in\{+,-\}\). No inverse of \(C\) is used, so the
rank-one cases \(\rho=\pm1\) are included. Define

\[
 \phi(x)=1+0.1\log(1+e^x),\qquad
 g(x)=\phi'(x)=\frac{0.1}{1+e^{-x}}.
\]

The elementary inequalities

\[
 0\leq g\leq0.1,\qquad |g'|\leq0.025,\qquad
 0<\phi(x)\leq a_0+0.1|x|\leq2+0.1|x|,
 \quad a_0=1+0.1\log2<2
 \tag{3}
\]

follow from \(\log(1+e^x)\leq\log2+|x|\) and

\[
 g'(x)=0.1\sigma(x)(1-\sigma(x))\leq0.025,
 \qquad \sigma(x)=(1+e^{-x})^{-1}.
\]

Consequently \(\phi\) is \(0.1\)-Lipschitz and \(g\) is
\(0.025\)-Lipschitz, both pointwise and in RMS norm.

A cut is a scalar map \(\tau:\mathbb R\to\mathbb R\), applied
coordinatewise, satisfying

\[
 |\tau(x)|\leq|x|,\qquad |\tau(x)-\tau(z)|\leq|x-z|.
 \tag{4}
\]

The stated derivative condition \(|\tau'|\leq1\) implies the second
inequality for differentiable cuts, and also for absolutely continuous
cuts with the derivative bound almost everywhere. This permits hard
clipping. The primal result uses only (4). To say that a cut has an
output cap \(r<\infty\) means, additionally,

\[
 \sup_x|\tau_r(x)|\leq r.
 \tag{5}
\]

For comparison of different caps, two useful defect conventions are
distinguished in Section 5. Ordinary hard clips are an explicit example:

\[
 \tau_r(x)=\max(-r,\min(x,r)),\qquad
 \tau_0=0,\quad \tau_\infty(x)=x.
 \tag{6}
\]

Smooth cuts may instead be used; their actual output ceilings, and any
nesting property used for their defects, must be stated. For example, a
cut with identity radius \(r\) and output ceiling \(2r\) has output cap
\(2r\) in (5).

An explicit continuously differentiable, nested family satisfying the
derivative condition everywhere is also available. Define an odd function
\(\psi\) by, for \(t\geq0\),

\[
 \psi(t)=
 \begin{cases}
 t,&0\leq t\leq1/2,\\
 t-\tfrac12(t-\tfrac12)^2,&1/2\leq t\leq3/2,\\
 1,&t\geq3/2,
 \end{cases}
 \qquad \tau_r(x)=r\psi(x/r)\quad(r>0).
 \tag{6a}
\]

The values and first derivatives match at the junctions, and
\(0\leq\psi'\leq1\); also \(0\leq\psi(t)\leq\min(t,1)\) for \(t\geq0\).
Hence (4)--(5) hold, with identity on \([-r/2,r/2]\). On the positive
half-line \(\psi'\) is nonincreasing, so
\(\psi(t)=\int_0^t\psi'(s)\,ds\geq t\psi'(t)\). Therefore
\[
 \frac{\partial}{\partial r}\bigl[r\psi(x/r)\bigr]
   =\psi(x/r)-(x/r)\psi'(x/r)\geq0\qquad(x\geq0).
\]
It follows that \(0\leq\tau_r(x)\leq\tau_s(x)\leq x\) for \(x\geq0\)
and \(r\leq s\). Oddness gives (36) for all real \(x\). The definitions
\(\tau_0=0,\tau_\infty(x)=x\) extend this ordering to both endpoints.
Thus the old-tail version below can use either (6) or the everywhere
differentiable cuts (6a), without assuming the existence of an unspecified
compatible cut family.

## 2. Self-contained reference field and exact Euler equations

The raw state is

\[
 U=(\Theta,W_2,W_3,w).
\]

Its forward fields and, optionally, predictions are

\[
 z_1^c=\Theta x_c,\quad h_1^c=\phi(z_1^c),\qquad
 z_2^c=W_2h_1^c,\quad h_2^c=\phi(z_2^c),\qquad
 z_3^c=W_3h_2^c,\quad h_3^c=\phi(z_3^c),\qquad
 f_c=\langle w,h_3^c\rangle_n.
 \tag{7}
\]

For three possibly different cuts, define the backward fields in this
order:

\[
 \begin{aligned}
 \delta_3^c&=\tau_{r_w}(w)\,g(z_3^c),
 &q_2^c&=W_3^*\delta_3^c,\\
 \delta_2^c&=\tau_{r_2}(q_2^c)\,g(z_2^c),
 &q_1^c&=W_2^*\delta_2^c,\\
 \delta_1^c&=\tau_{r_1}(q_1^c)\,g(z_1^c).
 \end{aligned}
 \tag{8}
\]

Products of two vectors in (8) are coordinatewise. In particular, the
cut of \(w\) occurs **only** in \(\delta_3\). Define the four components
of the reference vector field by

\[
 \begin{aligned}
 F_\Theta(U)&=\frac12\sum_c y_c\delta_1^c x_c^{\mathsf T},\\
 F_2(U)&=\frac12\sum_c y_c\delta_2^c\otimes_n h_1^c,\\
 F_3(U)&=\frac12\sum_c y_c\delta_3^c\otimes_n h_2^c,\\
 F_w(U)&=\frac12\sum_c y_c h_3^c
         =\frac12(h_3^+-h_3^-).
 \end{aligned}
 \tag{9}
\]

Changing the common ascent/descent sign does not affect any estimate.
For any mesh \(0=t_0<t_1<\cdots<t_N\), let
\(\Delta_k=t_{k+1}-t_k\). Explicit Euler means exactly

\[
 \begin{aligned}
 \Theta_{k+1}&=\Theta_k+\Delta_k F_\Theta(U_k),\\
 W_{2,k+1}&=W_{2,k}+\frac{\Delta_k}{2}
               \sum_c y_c\delta_{2,k}^c\otimes_n h_{1,k}^c,\\
 W_{3,k+1}&=W_{3,k}+\frac{\Delta_k}{2}
               \sum_c y_c\delta_{3,k}^c\otimes_n h_{2,k}^c,\\
 w_{k+1}&=w_k+\frac{\Delta_k}{2}(h_{3,k}^+-h_{3,k}^-).
 \end{aligned}
 \tag{10}
\]

Thus the readout increment is exact and uncut. Both matrix updates are
part of the state, not merely their actions on the two current features.
The matrices W_2,W_3 themselves are the canonical raw hidden matrices;
their coordinate increments in (10) include the factor 1/n from
the tensor convention (1). No rescaling of either hidden matrix is used.

The first raw coordinates are explicit as well. Writing
\(\Theta=(u,v)\),

\[
 u_{k+1}-u_k=\frac{a\Delta_k}{2}(\delta_{1,k}^+-\delta_{1,k}^-),
 \qquad
 v_{k+1}-v_k=\frac{b\Delta_k}{2}(\delta_{1,k}^++\delta_{1,k}^-).
 \tag{12}
\]

Multiplying by \(x_c\) gives the exact first-field update

\[
 z_{1,k+1}^c-z_{1,k}^c
     =\frac{\Delta_k}{2}\sum_d y_d C_{cd}\delta_{1,k}^d.
 \tag{13}
\]

Write \(\Delta h_{\ell,k}^c=h_{\ell,k+1}^c-h_{\ell,k}^c\), and similarly
for \(z_\ell\). The exact forward product identities are

\[
 \begin{aligned}
 \Delta z_{2,k}^c
 &=W_{2,k+1}\Delta h_{1,k}^c
    +\frac{\Delta_k}{2}\sum_d y_d\delta_{2,k}^d
                      \langle h_{1,k}^d,h_{1,k}^c\rangle_n,\\
 \Delta z_{3,k}^c
 &=W_{3,k+1}\Delta h_{2,k}^c
    +\frac{\Delta_k}{2}\sum_d y_d\delta_{3,k}^d
                      \langle h_{2,k}^d,h_{2,k}^c\rangle_n.
 \end{aligned}
 \tag{14}
\]

Indeed, \(W'h'-Wh=W'(h'-h)+(W'-W)h\); substituting (10) proves (14).
The operator multiplying the feature increment is the **next** operator.
The resulting cross term is included exactly. There is no discarded
\(\Delta_k^2\) remainder. If an entirely algebraic gate representation
is desired, define the diagonal matrix

\[
 D_{\ell,k}^c(i,i)=\int_0^1
       g\bigl(z_{\ell,k}^c(i)+s\Delta z_{\ell,k}^c(i)\bigr)\,ds.
\]

The fundamental theorem of calculus gives

\[
 \Delta h_{\ell,k}^c=D_{\ell,k}^c\Delta z_{\ell,k}^c,
 \qquad \|D_{\ell,k}^c\|_{\mathrm{op}}\leq0.1.
 \tag{15}
\]

For completeness the prediction product identity is

\[
 f_{c,k+1}-f_{c,k}
  =\langle w_{k+1},\Delta h_{3,k}^c\rangle_n
   +\frac{\Delta_k}{2}\sum_d y_d
                       \langle h_{3,k}^d,h_{3,k}^c\rangle_n.
 \tag{16}
\]

## 3. Cap-uniform short primal theorem

Assume

\[
 w_0=0,\qquad \max_c\|z_{1,0}^c\|_n\leq2,\qquad
 \|W_{2,0}\|_{\mathrm{op}},\|W_{3,0}\|_{\mathrm{op}}\leq10.
 \tag{17}
\]

For every width, every \(\rho\in[-1,1]\), every choice of cuts satisfying
(4), and every mesh with \(t_N\leq0.1\), all iterates satisfy

\[
 \begin{aligned}
 \|w_k\|_n&\leq7t_k,\\
 \|\Theta_k-\Theta_0\|_{n,2}
   &\leq0.4235t_k^2,\\
 \max_c\|z_{1,k}^c\|_n&\leq2+0.4235t_k^2<3,\\
 \|W_{2,k}-W_{2,0}\|_{\mathrm{HS}}
   &\leq0.8855t_k^2,\\
 \|W_{3,k}-W_{3,0}\|_{\mathrm{HS}}
   &\leq1.5855t_k^2.
 \end{aligned}
 \tag{18}
\]

In particular both middle operator norms are less than 11, and
the readout RMS is less than 1. No initial HS bound is required.
The raw first-coordinate displacement is controlled even if a component
invisible to the inputs was large initially.

**Proof.** Use the closed provisional box

\[
 \max_c\|z_1^c\|_n\leq3,\qquad
 \|W_2\|_{\mathrm{op}},\|W_3\|_{\mathrm{op}}\leq11,
 \qquad \|w\|_n\leq1.
 \tag{19}
\]

By (3) and (7), at a state in this box,

\[
 \begin{array}{c|ccc}
       &\ell=1&\ell=2&\ell=3\\ \hline
 \|z_\ell^c\|_n&3&25.3&49.83\\
 \|h_\ell^c\|_n&2.3&4.53&6.983<7
 \end{array}
 \tag{20}
\]

The entries mean upper bounds. For example,
\(\|z_2^c\|_n\leq11(2.3)=25.3\) and
\(\|h_2^c\|_n\leq2+0.1(25.3)=4.53\). The same two steps give the third
column. Put \(\omega=\|w\|_n\). Equations (4) and (8) give successively

\[
 \begin{aligned}
 \|\delta_3^c\|_n&\leq0.1\omega,
 &\|q_2^c\|_n&\leq1.1\omega,\\
 \|\delta_2^c\|_n&\leq0.11\omega,
 &\|q_1^c\|_n&\leq1.21\omega,\\
 \|\delta_1^c\|_n&\leq0.121\omega.
 \end{aligned}
 \tag{21}
\]

The \(1/2\) sample average, \(|y_c|=\|x_c\|=1\), and (1) now imply

\[
 \begin{aligned}
 \|F_w\|_n&\leq7,\\
 \|F_\Theta\|_{n,2},\quad
 \max_c\left\|\tfrac12\sum_d y_d C_{cd}\delta_1^d\right\|_n
     &\leq0.121\omega,\\
 \|F_2\|_{\mathrm{HS}}&\leq(0.11)(2.3)\omega=0.253\omega,\\
 \|F_3\|_{\mathrm{HS}}&\leq(0.1)(4.53)\omega=0.453\omega.
 \end{aligned}
 \tag{22}
\]

For the first line in the second row, specifically,
\(\|\delta_1^c x_c^{\mathsf T}\|_{n,2}=\|\delta_1^c\|_n\).
For the other line use \(|C_{cd}|\leq1\).

Assuming all preceding nodes are in the box, sum the Euler increments.
The readout bound gives \(\omega_j\leq7t_j\). Also the exact identity

\[
 \sum_{j<k}\Delta_jt_j
       =\frac12\left(t_k^2-\sum_{j<k}\Delta_j^2\right)
       \leq\frac12t_k^2
 \tag{23}
\]

follows by summing
\(t_{j+1}^2-t_j^2=2\Delta_jt_j+\Delta_j^2\).
Thus (22) gives every bound in (18), since

\[
 0.121\cdot7/2=0.4235,\qquad
 0.253\cdot7/2=0.8855,\qquad
 0.453\cdot7/2=1.5855.
\]

At \(t_k\leq0.1\), the resulting bounds in (19) are at most

\[
 2.004235,
 \qquad10.008855,
 \qquad10.015855,
 \qquad0.7,
\]

respectively. They strictly improve the box. Starting from (17), ordinary
induction on \(k\) therefore proves the box and all the estimates without
assuming anything about a next-step operator in advance. This proof uses
neither an energy identity nor a gradient interpretation of the cuts.

In particular, all the backward quantities have cap-independent linear
time bounds:

\[
 \begin{aligned}
 \|\delta_{3,k}^c\|_n&\leq0.7t_k,&
 \|q_{2,k}^c\|_n&\leq7.7t_k,\\
 \|\delta_{2,k}^c\|_n&\leq0.77t_k,&
 \|q_{1,k}^c\|_n&\leq8.47t_k,\\
 \|\delta_{1,k}^c\|_n&\leq0.847t_k.
 \end{aligned}
 \tag{24}
\]

## 4. Exact-increment forward bounds and time-L2 metrics

Because Section 3 has already bounded the next-step operators, (13)--(15)
give the following inequalities for every step and sample, with
\(\omega_k=\|w_k\|_n\):

\[
 \begin{aligned}
 \|\Delta z_{1,k}^c\|_n&\leq0.121\Delta_k\omega_k,
 &\|\Delta h_{1,k}^c\|_n&\leq0.0121\Delta_k\omega_k,\\
 \|\Delta z_{2,k}^c\|_n&\leq0.715\Delta_k\omega_k,
 &\|\Delta h_{2,k}^c\|_n&\leq0.0715\Delta_k\omega_k,\\
 \|\Delta z_{3,k}^c\|_n&\leq2.83859\Delta_k\omega_k,
 &\|\Delta h_{3,k}^c\|_n&\leq0.283859\Delta_k\omega_k.
 \end{aligned}
 \tag{25}
\]

Here both forward constants are exact sums of the displayed decimal
bounds, not downward roundings:

\[
 \begin{aligned}
 11(0.0121)+0.253(2.3)&=0.1331+0.5819=0.715,\\
 11(0.0715)+0.453(4.53)&=0.7865+2.05209=2.83859.
 \end{aligned}
 \tag{26}
\]

For example the two summands in the first line bound respectively
\(W_{2,k+1}\Delta h_{1,k}^c\) and
\((W_{2,k+1}-W_{2,k})h_{1,k}^c\).

Linearly interpolate the nodal arrays \(h_{\ell,k}^c\), and denote these
interpolants by \(H_\ell^c(t)\). If \(0\leq u\leq t\leq S\leq0.1\),
the piecewise derivative bound from (25), using \(\omega_k\leq7t_k\leq7v\)
on the \(k\)-th interval, gives

\[
 \begin{aligned}
 \|H_1^c(t)-H_1^c(u)\|_n
   &\leq0.04235(t^2-u^2)
    \leq0.0847S|t-u|,\\
 \|H_2^c(t)-H_2^c(u)\|_n
   &\leq0.25025(t^2-u^2)
    \leq0.5005S|t-u|,\\
 \|H_3^c(t)-H_3^c(u)\|_n
   &\leq0.9935065(t^2-u^2)
    \leq1.987013S|t-u|.
 \end{aligned}
 \tag{27}
\]

To justify the integral step, split \([u,t]\) at its mesh points, bound
the norm of each increment by the integral of its slope norm, and sum.
Each interpolated feature also retains its corresponding bound in (20)
by the triangle inequality for convex combinations.

The same constants apply if one instead linearly interpolates the raw
state and recomputes the physical features using (7). Indeed, the raw
interpolants remain in (19), and on the \(k\)-th interval their derivatives
are the frozen increments \(F(U_k)\). Thus

\[
 \begin{aligned}
 \dot z_2^c(t)&=F_2(U_k)h_1^c(t)
                  +W_2(t)\bigl[g(z_1^c(t))\dot z_1^c(t)\bigr],\\
 \dot z_3^c(t)&=F_3(U_k)h_2^c(t)
                  +W_3(t)\bigl[g(z_2^c(t))\dot z_2^c(t)\bigr].
 \end{aligned}
 \tag{28}
\]

Using (20) and (22) in (28) gives exactly (26) times \(\omega_k\).
This proves (27) for those physical features as well. Nodal feature
interpolation and physical feature recomputation need not coincide.

Here is the precise Gaussian-metric consequence, without any program
identification assumption. For deterministic feature paths as above,
let \(G_i^{(2)},G_i^{(3)}\) be independent standard normal variables and put

\[
 \xi_{2,c}(t)=\frac1{\sqrt n}\sum_iG_i^{(2)}H_{1,i}^c(t),
 \qquad
 \xi_{3,c}(t)=\frac1{\sqrt n}\sum_iG_i^{(3)}H_{2,i}^c(t).
 \tag{29}
\]

The same Gaussian array is used for both samples in each source group.
Independence and \(\mathbb EG_iG_j=\mathbf1_{i=j}\) give

\[
 \mathbb E\xi_{\ell,c}(t)\xi_{\ell,d}(u)
      =\langle H_{\ell-1}^c(t),H_{\ell-1}^d(u)\rangle_n,
 \quad \ell=2,3.
 \tag{30}
\]

Consequently the canonical L2 increment metrics obey

\[
 \begin{aligned}
 \bigl(\mathbb E|\xi_{2,c}(t)-\xi_{2,c}(u)|^2\bigr)^{1/2}
   &\leq0.0847S|t-u|,\\
 \bigl(\mathbb E|\xi_{3,c}(t)-\xi_{3,c}(u)|^2\bigr)^{1/2}
   &\leq0.5005S|t-u|.
 \end{aligned}
 \tag{31}
\]

The variances are bounded by \(2.3^2\) and \(4.53^2\) at all times.
At time zero the sharper bounds \(2.2^2\) and \(4.2^2\) follow from (17).
For random finite feature paths, (29)--(31) can be read conditionally on
the entire frozen path, with fresh independent auxiliary Gaussians.
This does not assert that these auxiliary variables are the original
network's Gaussian sources. If a separate construction specifies a
Gaussian source covariance as the expectation of the Gram kernel (30),
taking expectation in the squared pathwise bounds proves (31) for that
covariance too. No independence of evolved neurons is used.

## 5. Local asymmetric L2/HS comparison

Consider an old state \(U=(\Theta,W_2,W_3,w)\) with old cuts
\(\tau^{o}_w,\tau^{o}_2,\tau^{o}_1\), and a new state
\(\widetilde U=(\widetilde\Theta,\widetilde W_2,
\widetilde W_3,\widetilde w)\) with new cuts
\(\tau^{n}_w,\tau^{n}_2,\tau^{n}_1\). Both states are in (19), with the
same \(n,\rho,x_c,y_c\). Each forward and backward field is computed
from its own state and its own cuts via (7)--(8). Assume the three old
output caps obey

\[
 r_w,r_2,r_1\leq R<\infty.
 \tag{32}
\]

The new cuts need only satisfy (4) for the first comparison below; their
output ceilings never enter its coefficient. Define the raw state distance

\[
 \begin{aligned}
 d_\theta&=\|\widetilde\Theta-\Theta\|_{n,2},&
 d_2&=\|\widetilde W_2-W_2\|_{\mathrm{HS}},\\
 d_3&=\|\widetilde W_3-W_3\|_{\mathrm{HS}},&
 d_w&=\|\widetilde w-w\|_n,\\
 D&=d_\theta+d_2+d_3+d_w.
 \end{aligned}
 \tag{33}
\]

In the same order, the norm of a vector-field difference is the sum of
its raw first-coordinate RMS, its two operator HS norms, and its readout
RMS norm. Define **exact old-state cut-mismatch defects** by

\[
 \begin{aligned}
 E_w&=\|\tau_w^n(w)-\tau_w^o(w)\|_n,\\
 E_2&=\max_c\|\tau_2^n(q_2^c)-\tau_2^o(q_2^c)\|_n,\\
 E_1&=\max_c\|\tau_1^n(q_1^c)-\tau_1^o(q_1^c)\|_n.
 \end{aligned}
 \tag{34}
\]

Every \(w,q_2^c,q_1^c\) on the right is an actual field of the **old cut
reference**. Then

\[
 \begin{aligned}
 \|F^{n}(\widetilde U)-F^{o}(U)\|_{L^2/\mathrm{HS}}
 &\leq(1.359+1.1570775R)D
        +0.827E_w+0.34E_2+0.1E_1\\
 &\leq2(1+R)D+E_w+E_2+E_1.
 \end{aligned}
 \tag{35}
\]

Thus, in particular, the coefficient is \(C(1+R)\). It has no
\(R^2\), \(r_wr_2\), \(r_wr_1\), or \(r_2r_1\) term.

For a nested cut family, suppose its ordering is explicitly

\[
 |\tau_s(x)-\tau_r(x)|\leq|x-\tau_r(x)|
       \quad(0\leq r\leq s\leq\infty).
 \tag{36}
\]

Hard clipping (6) satisfies (36): for \(x\geq0\),
\(\min(x,r)\leq\min(x,s)\leq x\), and the negative case follows by
oddness. If each new cap is at least \(R\), define the **old actual
truncation defects**

\[
 T_w=\|w-\tau_{r_w}(w)\|_n,\qquad
 T_2=\max_c\|q_2^c-\tau_{r_2}(q_2^c)\|_n,\qquad
 T_1=\max_c\|q_1^c-\tau_{r_1}(q_1^c)\|_n.
 \tag{37}
\]

Equation (36) gives \(E_j\leq T_j\), so (35) holds with \(T_j\) in
place of \(E_j\). For hard clipping these are exactly

\[
 T_w=\|(|w|-r_w)_+\|_n,\qquad
 T_j=\max_c\|(|q_j^c|-r_j)_+\|_n,\quad j=1,2.
 \tag{38}
\]

These are old actual tails, not tails of a new reference, an uncut
trajectory, or a substituted envelope. If old cuts are identity on
\([-\alpha r_j,\alpha r_j]\), then the always-valid rough bound

\[
 |x-\tau_{r_j}(x)|
    \leq2|x|\mathbf1_{\{|x|>\alpha r_j\}}
 \tag{39}
\]

follows from (4). For sign-preserving cuts the factor 2 improves to 1.

The distinction between (34) and (37) is necessary. Inequalities (4)
alone, even with output ceilings, do not imply cross-cap nesting. For
example, assign the old cut to be hard clipping at \(r=1\) and the new
cut to be zero with an advertised ceiling \(s=2\). At \(x=1/2\) the old
truncation defect is zero and the cut mismatch is \(1/2\). Both maps
satisfy (4) and their ceiling bounds. Thus a conclusion involving only
old truncation defects requires (36), or another explicitly verified
comparison of the actual chosen cuts. With arbitrary cuts the exact
old-state mismatch statement (35) remains valid.

### Proof of (35)

Use a tilde for all new fields, and take a maximum over \(c\) whenever a
field has a sample index. First, forward features satisfy

\[
 \begin{aligned}
 A_1:=\max_c\|\widetilde z_1^c-z_1^c\|_n&\leq d_\theta,\\
 A_2:=\max_c\|\widetilde z_2^c-z_2^c\|_n
    &\leq1.1d_\theta+2.3d_2\leq2.3D,\\
 A_3:=\max_c\|\widetilde z_3^c-z_3^c\|_n
    &\leq1.21d_\theta+2.53d_2+4.53d_3\leq4.53D,\\
 \max_c\|\widetilde h_\ell^c-h_\ell^c\|_n&\leq0.1A_\ell.
 \end{aligned}
 \tag{40}
\]

To verify the second row, split

\[
 \widetilde W_2\widetilde h_1^c-W_2h_1^c
 =\widetilde W_2(\widetilde h_1^c-h_1^c)
       +(\widetilde W_2-W_2)h_1^c
\]

and use \(\|\widetilde W_2\|_{\mathrm{op}}\leq11\), (1), and
\(\|h_1^c\|_n\leq2.3\). The third row follows by the same displayed
identity with \(W_3,h_2\), giving \(A_3\leq1.1A_2+4.53d_3\).

For any one of the cuts, any old scalar fields \(v,z\), and new fields
\(\widetilde v,\widetilde z\), the essential splitting is

\[
 \begin{aligned}
 &\tau^n(\widetilde v)g(\widetilde z)-\tau^o(v)g(z)\\
 &\quad=
 [\tau^n(\widetilde v)-\tau^o(v)]g(\widetilde z)
       +\tau^o(v)[g(\widetilde z)-g(z)].
 \end{aligned}
 \tag{41}
\]

If the old output cap is \(r\), (3)--(5) imply

\[
 \|\tau^n(\widetilde v)g(\widetilde z)-\tau^o(v)g(z)\|_n
 \leq0.1\|\widetilde v-v\|_n
      +0.1\|\tau^n(v)-\tau^o(v)\|_n
      +0.025r\|\widetilde z-z\|_n.
 \tag{42}
\]

Indeed, insert \(\tau^n(v)\) into the first bracket in (41) and use
its Lipschitz constant one. In the second bracket only the **old** cut
is used in the uniform norm. No product of two uncontrolled L2 fields
occurs in this inequality.

Put

\[
 B_\ell=\max_c\|\widetilde\delta_\ell^c-\delta_\ell^c\|_n,
 \qquad Q_j=\max_c\|\widetilde q_j^c-q_j^c\|_n.
\]

The exact adjoint product splits are

\[
 \begin{aligned}
 \widetilde q_2^c-q_2^c
 &=\widetilde W_3^*(\widetilde\delta_3^c-\delta_3^c)
       +(\widetilde W_3-W_3)^*\delta_3^c,\\
 \widetilde q_1^c-q_1^c
 &=\widetilde W_2^*(\widetilde\delta_2^c-\delta_2^c)
       +(\widetilde W_2-W_2)^*\delta_2^c.
 \end{aligned}
 \tag{43}
\]

Use (21) with \(\|w\|_n\leq1\), (40), and (42)--(43), in the indicated
top-to-bottom order. This yields all five comparison inequalities:

\[
 \begin{aligned}
 B_3
 &\leq0.1d_w+0.025r_w A_3+0.1E_w\\
 &\leq(0.1+0.11325R)D+0.1E_w,\\
 Q_2
 &\leq11B_3+0.1d_3\\
 &\leq(1.2+1.24575R)D+1.1E_w,\\
 B_2
 &\leq0.1Q_2+0.025r_2 A_2+0.1E_2\\
 &\leq(0.12+0.182075R)D+0.11E_w+0.1E_2,\\
 Q_1
 &\leq11B_2+0.11d_2\\
 &\leq(1.43+2.002825R)D+1.21E_w+1.1E_2,\\
 B_1
 &\leq0.1Q_1+0.025r_1 A_1+0.1E_1\\
 &\leq(0.143+0.2252825R)D+0.121E_w+0.11E_2+0.1E_1.
 \end{aligned}
 \tag{44}
\]

For example the cap contribution in \(B_2\) is the **sum**
\(0.124575R+0.0575R\). No cap is multiplied by \(Q_2\): its coefficient
in (42) is \(0.1\), regardless of either cap. The same fact holds at the
first layer.

It remains to compare every raw velocity, including both matrices.
The first-coordinate update (9) gives directly

\[
 \|F_\Theta^n(\widetilde U)-F_\Theta^o(U)\|_{n,2}\leq B_1.
 \tag{45}
\]

This proves a bound on the full pair of raw coordinates, not just on
the two projected first fields; it is uniform even when \(C\) is singular.
For the middle matrices, the exact rank-one split is

\[
 \widetilde\delta\otimes_n\widetilde h-\delta\otimes_n h
   =(\widetilde\delta-\delta)\otimes_n\widetilde h
       +\delta\otimes_n(\widetilde h-h).
 \tag{46}
\]

Using (1), the new feature RMS bounds, the old delta RMS bounds, and
the \(1/2\) sample average in (9), gives

\[
 \begin{aligned}
 \|F_2^n(\widetilde U)-F_2^o(U)\|_{\mathrm{HS}}
 &\leq2.3B_2+0.11(0.1A_1)\\
 &\leq(0.287+0.4187725R)D+0.253E_w+0.23E_2,\\
 \|F_3^n(\widetilde U)-F_3^o(U)\|_{\mathrm{HS}}
 &\leq4.53B_3+0.1(0.1A_2)\\
 &\leq(0.476+0.5130225R)D+0.453E_w,\\
 \|F_w^n(\widetilde U)-F_w^o(U)\|_n
 &\leq0.1A_3\leq0.453D.
 \end{aligned}
 \tag{47}
\]

The last row uses the exact uncut readout update. Features in the matrix
updates require only their bounded RMS norms, not coordinatewise ceilings.
Substituting the last row of (44) into (45) and adding (47) proves the first inequality
in (35); each coefficient is displayed so its sum can be checked.
The second follows because
\(1.359+1.1570775R\leq2(1+R)\) for \(R\geq0\), and all three defect
coefficients are at most one.

In particular, for the same cuts on both states, all \(E_j=0\), proving
local L2/HS Lipschitz continuity at every fixed finite triple of caps.
For ordered old/new caps, (36)--(38) give exactly the asserted asymmetric
old-tail comparison, including a new cut equal to the identity.

The same assertion holds on any other fixed primal ball, with a constant
depending on that ball. For precision, suppose both states satisfy
\(\max_c\|z_1^c\|_n\leq m_1\),
\(\|W_2\|_{\mathrm{op}}\leq\beta_2\),
\(\|W_3\|_{\mathrm{op}}\leq\beta_3\), and \(\|w\|_n\leq m_w\).
Put

\[
 H_1=2+0.1m_1,\quad H_2=2+0.1\beta_2H_1,\quad
 H_3=2+0.1\beta_3H_2,\qquad
 L_2=0.1\beta_2+H_1,\quad L_3=0.1\beta_3L_2+H_2.
\]

The forward split (40) gives \(A_1\leq D,A_2\leq L_2D,A_3\leq L_3D\).
The same backward splits (42)--(43), now using
\(\|\delta_3^c\|_n\leq0.1m_w\) and
\(\|\delta_2^c\|_n\leq0.01\beta_3m_w\), give

\[
 \begin{aligned}
 B_3&\leq(0.1+0.025RL_3)D+0.1E_w,\\
 B_2&\leq0.1\beta_3B_3
              +(0.01m_w+0.025RL_2)D+0.1E_2,\\
 B_1&\leq0.1\beta_2B_2
              +(0.001\beta_3m_w+0.025R)D+0.1E_1.
 \end{aligned}
 \tag{47a}
\]

Finally, (45)--(47) bound the full velocity difference by

\[
 B_1+H_1B_2+H_2B_3+
      (0.001\beta_3m_w+0.01m_wL_2+0.1L_3)D.
 \tag{47b}
\]

Successive substitution of the first row of (47a) into the second and
then the third yields a constant depending only on
\((m_1,m_w,\beta_2,\beta_3)\), denoted \(C_{\rm ball}\), such that

\[
 \|F^n(\widetilde U)-F^o(U)\|_{L^2/\mathrm{HS}}
 \leq C_{\rm ball}\bigl[(1+R)D+E_w+E_2+E_1\bigr].
 \tag{47c}
\]

All multipliers of a previous \(B_\ell\) in (47a) are independent of
the caps, which proves the asserted linear dependence without hiding
a cap product in \(C_{\rm ball}\). Ordered cuts again allow the old
actual defects \(T_j\) in place of \(E_j\).

## 6. State, feature, and Euler comparison consequences

The preceding proof includes the bridges between state and fields:
(40) controls every forward field and feature, while (44) controls
both reverse queries and all three deltas. For the predictions in (7),
one additionally has

\[
 \begin{aligned}
 |\widetilde f_c-f_c|
 &\leq\|\widetilde w-w\|_n\|\widetilde h_3^c\|_n
       +\|w\|_n\|\widetilde h_3^c-h_3^c\|_n\\
 &\leq7d_w+0.453D\leq7.453D.
 \end{aligned}
 \tag{48}
\]

For two Euler references on the same mesh, remaining in the box (19),
let \(D_k\) be (33), and let \(T_{j,k}\) be the old actual defects (37)
for a family satisfying (36). Equations (10) and (35), with the triangle
inequality in each state component, give

\[
 D_{k+1}\leq[1+2(1+R)\Delta_k]D_k
       +\Delta_k(T_{w,k}+T_{2,k}+T_{1,k}).
 \tag{49}
\]

Iterating this scalar inequality and using \(1+x\leq e^x\) for \(x\geq0\)
gives the explicit bound

\[
 \begin{aligned}
 D_k\leq{}&e^{2(1+R)t_k}D_0\\
 &+\sum_{j<k}\Delta_j
     e^{2(1+R)(t_k-t_{j+1})}
        (T_{w,j}+T_{2,j}+T_{1,j}).
 \end{aligned}
 \tag{50}
\]

To see the exponent for a forcing term, the term inserted at step \(j\)
is multiplied only by
\(\prod_{j<\ell<k}(1+2(1+R)\Delta_\ell)\), whose time increments sum to
\(t_k-t_{j+1}\). With arbitrary cuts replace \(T\) by \(E\).
This is a comparison estimate, not a claim that its defects vanish.

For any differentiable finite reference solution satisfying
\(\dot U=F(U)\), the same primal and time-metric proofs work with
integrals in place of left-node sums. For two such solutions in the
box, the integrated version of (35) similarly yields

\[
 D(t)\leq e^{2(1+R)t}D(0)
   +\int_0^t e^{2(1+R)(t-s)}[T_w(s)+T_2(s)+T_1(s)]\,ds.
 \tag{51}
\]

For example, this integral inequality follows by first bounding the
state difference by its initial norm plus the integral of (35), then
using the integrating factor on that scalar upper bound. No existence
claim for an uncut population flow is needed in any of these arguments.

## 7. Conditional population-space form and sample-weight normalization

The same algebra and constants hold on explicitly supplied probability
spaces. Here are the needed operators and adjoints, so that this assertion
does not conceal an ill-defined population transpose. Let

\[
 E_\ell=L^2(\Omega_\ell,\mu_\ell),\quad \mu_\ell(\Omega_\ell)=1,
 \qquad \Theta\in L^2(\Omega_1;\mathbb R^2),\quad w\in E_3.
\]

Take fixed bounded operators
\(A_2:E_1\to E_2\) and \(A_3:E_2\to E_3\), and write

\[
 W_2=A_2+K_2,\qquad W_3=A_3+K_3,
\]

where \(K_\ell\) has a square-integrable kernel on
\(\Omega_\ell\times\Omega_{\ell-1}\). Its action, HS norm, and adjoint are

\[
 \begin{aligned}
 (K_\ell f)(y)&=\int_{\Omega_{\ell-1}}K_\ell(y,x)f(x)\,d\mu_{\ell-1}(x),\\
 \|K_\ell\|_{\mathrm{HS}}^2
   &=\int_{\Omega_\ell}\int_{\Omega_{\ell-1}}
                    |K_\ell(y,x)|^2\,d\mu_{\ell-1}(x)d\mu_\ell(y),\\
 (K_\ell^*g)(x)&=\int_{\Omega_\ell}K_\ell(y,x)g(y)\,d\mu_\ell(y),\\
 W_\ell^*&=A_\ell^*+K_\ell^*,\qquad
 \langle A_\ell f,g\rangle_{E_\ell}
       =\langle f,A_\ell^*g\rangle_{E_{\ell-1}}.
 \end{aligned}
 \tag{52}
\]

These formulas are for real spaces. Cauchy--Schwarz in \(x\), followed by
integration in \(y\), proves
\(\|K_\ell f\|_2\leq\|K_\ell\|_{\mathrm{HS}}\|f\|_2\).
The adjoint identity for the kernel follows by interchanging its absolutely
integrable bilinear pairing; absolute integrability follows from
Cauchy--Schwarz on the product probability space. Thus all adjoint
products used in (8) and (43) are well-defined.

Replace every finite RMS inner product by its \(L^2(\mu_\ell)\) inner
product. The rank-one update has kernel \(\delta(y)h(x)\), whose HS norm
is \(\|\delta\|_2\|h\|_2\), by the product integral of
\(|\delta(y)|^2|h(x)|^2\). Equations (7)--(10), including both kernel
updates and the raw first-coordinate update, therefore define the same
reference field on these spaces. In comparison the fixed \(A_\ell\)
are common, so
\(\widetilde W_\ell-W_\ell=\widetilde K_\ell-K_\ell\) is HS even when
\(A_\ell\) itself is not HS. No HS bound on a fixed base operator is
asserted or used.

On the ball (19), (3) ensures that every feature is in \(L^2\), bounded
gates and (4) ensure that every backward field is in \(L^2\), and the
rank-one formula ensures that both matrix velocities are HS. All
inequalities proved above consequently hold, with those norms, for
these supplied operators and reference states. In particular (35) is a
local population-space vector-field inequality. This is conditional on
the specified bounded base operators; it neither constructs Gaussian
base operators nor identifies any population model with a finite-width
limit.

Finally, suppose the two coefficients \(y_c\) in (9)--(10) are instead
specified scalars \(b_c(U)\). If \(|b_c(U)|\leq1\) on (19), the entire
short primal proof and the exact product identities hold, with \(b_c(U_k)\)
in place of \(y_c\) at each step. If in addition

\[
 \max_c|b_c(\widetilde U)-b_c(U)|\leq L_bD,
 \tag{53}
\]

the comparison receives only the additional term \(7.827L_bD\). To
verify it, split each weighted sample difference as new coefficient
times the field difference plus coefficient difference times the old
field. The four old sample-field norms are bounded respectively by

\[
 0.121,\qquad0.253,\qquad0.453,\qquad7,
\]

whose sum is \(7.827\). The \(1/2\) average does not increase this sum.
Thus (35) becomes

\[
 \|F^n(\widetilde U)-F^o(U)\|_{L^2/\mathrm{HS}}
 \leq[2(1+R)+7.827L_b]D+E_w+E_2+E_1,
 \tag{54}
\]

and ordered cuts again allow \(E_j\leq T_j\). For the explicitly
stated label-average field, \(L_b=0\). This extension requires neither
cap products nor a clipped gradient-energy identity.

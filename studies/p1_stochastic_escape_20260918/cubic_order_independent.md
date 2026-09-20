# Cubic descent is not universal: an exact collapsed-state criterion

2026-09-19. Independent scoped derivation, frozen before receiving the
supervisor's candidate. Scientific inputs, read completely: `docs/observable_p1.md`,
`docs/NOTATION.md`, and this study's `four_input_noise_geometry.md` and
`sgd_geometry.md`. No other study, current parallel route, external source,
implementation, or experiment was consulted. The required mathematical and
research skills and applicable shared process instructions were read.

Source HEAD: `019e3630237e33f58b9636c0aa67a039bebf0182`. Input SHA-256 values:

- `docs/observable_p1.md`: `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba`.
- `docs/NOTATION.md`: `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b`.
- `four_input_noise_geometry.md`: `e60c500587923ec3cab3c9ad9353935dce5d7abc7c3971bb3ec19d5567656e01`.
- `sgd_geometry.md`: `619f6c0f3148b72f764a8bacaf92aa434801e94323af0b343a3e1904e01cdf0e`.

## Statement and scope

The previously specified three-point and rank-one four-point examples do have
their displayed leading cubic descent directions. That does not extend to every
positive-loss equilibrium of the same p=1 model. At the fully collapsed state
`(w,c,M)=(0,0,0)`, cubic descent exists **if and only if**

\[
                         s_1:=\sum_a\mu_a y_a u_a\ne0.
\tag{1}
\]

The four binary-labeled inputs already present in the permitted source have
`s_1=0`. At their fully collapsed state there is no nonzero cubic coefficient
in any state direction, yet there is an explicit leading fifth-order descent
line. These inputs are normalized, pairwise nonparallel and nonantipodal, and
exactly representable using the canonical carriers and odd trainable fields.
Thus this is a counterexample to the ambient universal cubic-descent claim,
including when one restricts it to positive-semidefinite Hessian equilibria.

Everything below concerns exact population p=1, its physical L2/L2/Frobenius
metric, the unhalved weighted squared loss, and the odd invariant sector.
There is no approximation, numerical limit, or stochastic-limit argument.
The state here is the absolute triple `(w,c,M)`, not `(w-g,c,M)`.
The canonical initialization remains `(g,0,D)`. No reachability from that
initialization, attraction, or global fitting theorem is asserted.

## 1. The precise meaning of a cubic descent direction

At an equilibrium theta_* a leading cubic descent line is a fixed direction
v and a constant a>0 such that

\[
       L(\theta_*+tv)=L(\theta_*)-a t^3+o(t^3),\qquad t\downarrow0.
\tag{2}
\]

For a three-times differentiable scalar restriction of the loss, this requires
both zero quadratic coefficient and negative cubic coefficient. When the
Hessian is positive semidefinite, zero quadratic coefficient is precisely
the Hessian-null requirement. Indeed positivity of the quadratic polynomial
`H[v+sz,v+sz]` for every real s implies `H[v,z]=0` whenever `H[v,v]=0`.
By contrast, `H[v,v]>0` makes both orientations of the line increase the loss
for sufficiently small nonzero t, irrespective of a nonzero cubic coefficient.

In the counterexample the Hessian itself is zero. Moreover a uniform
fourth-order bound below excludes (2) along every differentiable state curve
with displacement O(t), not only along bounded straight-line perturbations.
We use a cubic Taylor coefficient rather than assuming that the full L2
Nemytskii map is C3 on a neighborhood.

## 2. Exact cubic criterion at complete collapse

Remove the inactive constants as in the odd invariant representation. The
canonical features `b_1` in R^(2d) and `b_2` in R^d are bounded, and

\[
 a_a(w)=E_1[b_1\tanh(w\cdot u_a)],\qquad
 f_a(w,c,M)=E_2[c\tanh(b_2^TMa_a(w))],\qquad
 L=\sum_a\mu_a(f_a-y_a)^2.
\tag{3}
\]

Let `rho` be the physical norm of `(w,c,M)`, and define the finite objects

\[
                 W=E_1[b_1w^T],\qquad v_c=E_2[b_2c].
\]

All estimates in this section hold uniformly for rho<=1, with constants
depending only on the fixed finite dataset and bounded canonical features.
The elementary global bounds

\[
 |\tanh z|\le |z|,\quad
 |\tanh z-z|\le C|z|^2,\quad
 |\tanh z-z|\le C|z|^3
\]

follow from Taylor's formula on |z|<=1 and linear growth outside that interval.
Use the quadratic bound for the lower population, since only w in L2 is
assumed. It gives

\[
 \|a_a(w)-Wu_a\|\le C\|w\|_2^2,
 \qquad \|a_a(w)\|\le C\|w\|_2.
\tag{4}
\]

The upper argument is uniformly bounded by `C||M||_F||w||_2`. Using the
cubic bound there and `E_2|c|<=||c||_2` yields

\[
 f_a=v_c^TMWu_a+R_a,\qquad
 |R_a|\le C\|c\|_2\|M\|_F\|w\|_2^2
       +C\|c\|_2\|M\|_F^3\|w\|_2^3
       \le C\rho^4.
\tag{5}
\]

Also `|f_a|<=C rho^3`. Expanding the square in (3) therefore gives the
uniform cubic Taylor expansion

\[
 L(w,c,M)=L(0)-2v_c^TMWs_1+O(\rho^4).
\tag{6}
\]

In particular the first and second coefficients vanish, and the cubic
coefficient along `(w,c,M)=t(h,k,N)` is

\[
        -2\big(E_2[b_2k]\big)^TN\big(E_1[b_1h^T]\big)s_1.
\tag{7}
\]

The origin is an actual equilibrium and has an actual zero Hilbert Hessian.
For completeness, in the source's physical gradient, the readout component
is O(rho^2), the matrix component is O(rho^2), and the lower component is
O(rho^2), uniformly on the ball. At zero all components vanish, and the
gradient divided by rho tends to zero. This proves differentiability of
the gradient at zero with derivative zero. Every sample gradient also
vanishes separately, so every minibatch is motionless at this state.

If s_1=0, equation (6) is `L-L(0)=O(rho^4)`. Along any curve with
rho=O(|t|) its loss difference is O(t^4); in particular it cannot have a
nonzero cubic coefficient or satisfy (2). This argument covers arbitrary
L2 directions and does not rely on interchanging an unbounded third moment
with differentiation.

Conversely suppose s_1 is nonzero. Let q select the first h-coordinate
of b_1, and let e=sign(G_1) on the lower population. Set

\[
 A=E_1[b_1e],\qquad
 \kappa=q^TA=\frac{E|\tanh G_1|}{\sqrt{v+1/4096}}>0.
\]

On the upper population put `B=b_{2,1}` and
`sigma^2=E_2[B^2]=tau/(tau+1/4096)>0`. By independent centered upper
coordinates, `E_2[b_2B]=sigma^2 e_1`. Choose

\[
                 h=e s_1,\qquad k=B,\qquad N=e_1q^T.
\]

These are bounded admissible odd fields. Substituting them into (7) gives
the strictly negative coefficient `-2 kappa sigma^2 ||s_1||^2`.
Their Hessian coefficient is zero, so they satisfy (2). This proves the
if-and-only-if criterion (1).

## 3. A mixed-binary, nonparallel counterexample with fifth-order descent

Fix C,S>0 with C^2+S^2=1. Take uniform weights and

\[
 \begin{array}{c|c}
 u_1=(C,S,0),\ u_2=(C,-S,0)&y_1=y_2=+1\\
 u_3=(C,0,S),\ u_4=(C,0,-S)&y_3=y_4=-1.
 \end{array}
\tag{8}
\]

The physical inputs are `x_a=sqrt(3)u_a`. All have the required normalized
Gram diagonal one. The u_a are distinct unit vectors with the same positive
first coordinate, so no two are parallel or antipodal. Their signed first
moment is zero because `u_1+u_2=u_3+u_4=(2C,0,0)`.

At `(0,0,0)` their loss is exactly one, every sample gradient is zero,
the Hessian is zero, and every cubic coefficient vanishes by Section 2.
This alone disproves universal cubic descent. To identify an actual higher
order descent, retain A, kappa, B and sigma^2 from Section 2 and put

\[
 w_t=t e(e_1+e_2),\qquad c_t=-tB,\qquad M_t=t e_1q^T,
 \qquad K=\kappa\sigma^2>0.
\tag{9}
\]

Write `z_a=(e_1+e_2) dot u_a`, so
`(z_1,z_2,z_3,z_4)=(C+S,C-S,C,C)`. The sign identity for e gives
exactly `a_a=A tanh(t z_a)`, and hence

\[
 f_a(t)=-tE_2[B\tanh(\kappa tB\tanh(tz_a))]
       =-Kz_at^3+\frac K3 z_a^3t^5+O(t^7).
\tag{10}
\]

All fields and marks in (9) are bounded, so Taylor's formula has an
integrable uniform remainder. The upper tanh cubic term first contributes
at order seven, because its argument is O(t^2) and the readout adds t.
The signed linear and cubic scalar moments are respectively

\[
 \frac14\sum_a y_a z_a=0,\qquad
 \frac14\sum_a y_a z_a^3
  =\frac{(C+S)^3+(C-S)^3-2C^3}{4}
  =\frac32 CS^2>0.
\]

Since `(1/4)sum z_a^2=C^2+S^2/2`, substituting (10) into the exact square
loss gives

\[
 L(w_t,c_t,M_t)
   =1-KCS^2t^5+K^2(C^2+S^2/2)t^6+O(t^7)<1
\tag{11}
\]

for all sufficiently small positive t. This is a leading fifth-order
descent line through a state with identically zero cubic Taylor polynomial.
It does not assert a fifth-order uniform Taylor expansion on an L2 ball.

## 4. Exact representability in the same canonical carrier

The following direct argument verifies that representability is not being
inferred merely from the absence of parallel or antipodal conflicts.
Let `r=(3S/C,1,2)`, choose `w=e r` and `M=e_1q^T`, and keep the same
canonical frozen features. The four positive distinct numbers `r dot u_a`
are `(4S,2S,5S,S)`. Therefore

\[
 Ma_a=z_a^{\rm fit}e_1,\qquad
 z_a^{\rm fit}=\kappa\tanh(r\cdot u_a)>0
\]

are distinct. Define the four odd bounded upper functions
`psi_a(B)=tanh(z_a^{fit}B)`. Their Gram `Q_ab=E_2[psi_a psi_b]` is
positive definite. Indeed, `q^TQq=0` would make the continuous function
`sum_a q_a tanh(z_a^{fit}x)` vanish on the open support interval of B.
Otherwise a nonzero value would give an open interval with positive squared
integral, because the transformed Gaussian law of B assigns positive mass
to every nonempty subinterval. Comparing the first four odd Taylor terms,
whose coefficients are `1,-1/3,2/15,-17/315`, gives

\[
                 \sum_a q_a(z_a^{\rm fit})^{2j+1}=0,
                    \qquad j=0,1,2,3.
\]

After absorbing the positive factors `z_a^{fit}` into q_a, this is the
Vandermonde system for the four distinct numbers `(z_a^{fit})^2`.
Its determinant is the nonzero product of their pairwise differences, so
q=0. Thus Q is invertible. The bounded odd readout

\[
                   c=\sum_a(Q^{-1}y)_a\psi_a
\]

satisfies `f_b=sum_a Q_ba(Q^{-1}y)_a=y_b` for every b. Both hidden
trainable blocks and the readout belong to the same permitted odd state
class. This is an exact fit of all four mixed binary labels by the same
p=1 system.

## 5. Consequences and check record

- The two particular cubic examples in the input sources retain their
  positive results. A quantified claim over all ambient bad equilibria is
  false: the same four-point data have a different, fully collapsed bad
  equilibrium with no cubic term.
- A nonzero third-order coefficient is insufficient when a positive
  quadratic term is present. The constructed counterexample is stronger:
  both Hessian and cubic polynomial vanish, yet (11) supplies descent.
- The origin is absorbing for every sample gradient and every minibatch.
  The existence of (11) does not give stochastic excitation there.
- None of these ambient facts proves or disproves fitting from `(g,0,D)`.
  Reachability and long-time behavior from that initialization remain
  separate questions.

Author check: the uniform remainder estimates use only bounded canonical
marks and L2 state fields; the explicit fifth-order line uses bounded fields.
The signs and constants in (10)--(11), data normalization, pairwise geometry,
odd parity, and the four-function Gram argument were checked directly.
No numerical calculation, simulation, code test, or specialized external
theorem is used. This report is a frozen independent candidate for supervisor
comparison; it is not promoted established material or an isolated review.

# Bounded continuation and an open family of perturbation directions

Informed post-freeze addendum, 2026-09-18. The lead suggested both
strengthenings below after `input_perturb_persist.md` was independently
frozen at SHA256
`641204a025374966da3114bd153f10956d0d9d704d4e6420cd9659ea6cd30dae`.
This note checks those suggestions; they are not claimed as part of the
independent pre-comparison result. The frozen report is left unchanged.
Only its complete proof and the original assigned scientific inputs are
used. No experiment or new scientific source was consulted. Status:
internally checked candidate, not independently reviewed or promoted.

The strengthenings are valid. Along the reflection-symmetric seed path,
the equilibria can have one fixed matrix and readout and converge in the
physical Hilbert space to a bounded, two-amplitude axial equilibrium of
the original data. Separately, an open set of independent spherical
perturbation directions admits loss-48/49 PSD equilibria for every
sufficiently small amplitude, with a threshold allowed to depend on the
direction. Uniform state bounds are proved for the seed continuation and
suitably shrinking neighborhoods of that path, not for the whole open
direction family.

## 1. Fixed coordinates for the symmetric interpolation problem

Use all notation from the frozen report. In particular
`delta=epsilon^(1/3)`, `t_* = arctanh(1/sqrt(3))`, and t_0 is the
positive root of `2t_0 tanh(t_0)=1`. Let the seven critical points be
ordered as the plane point near t_*, the two reflected pairs near t_*,
and the reflected pair near t_0. Let V_epsilon be their input-feature
matrix, and put

\[
                         \beta_\epsilon=V_\epsilon^{-1}{\bf1}.
\tag{1}
\]

Both input values and critical-point columns carry reflection
involutions. They satisfy `R V_epsilon=V_epsilon S`, while
`R 1=1`. Invertibility therefore implies `S beta_epsilon=beta_epsilon`:
the coefficients of the two members of each reflected pair are equal.
Thus the inverse applied to 1 lies entirely in the even subspace.

Replace each pair of feature columns by its mean. If b_epsilon is the
four-vector of coefficients of the plane column and these three means,
then its plane coefficient is the corresponding beta entry and each
mean coefficient is twice the corresponding individual beta entry.
In particular

\[
                 \|\beta_\epsilon\|_1=\|b_\epsilon\|_1.
\tag{2}
\]

The even input-value space is fixed: one coordinate for the positive
angle-zero point and one for each of the three reflected input pairs.
Write xi for the vector of their **unperturbed** cosines. Its four
distinct entries are `1,-1/2,1/sqrt(2),-1/sqrt(2)`. Let e_0 be the
vector equal to one at the single angle-zero input and zero elsewhere.
The four vectors `1,xi,xi^2,e_0` form a basis: a quadratic vanishing
on the three paired cosine values and also taking zero at the single
point is zero; also `rho dot e_0=-8/49!=0`, while rho annihilates
`1,xi,xi^2`.

For an even input-value vector v define its first three coordinates
`ell_0(v),ell_1(v),ell_2(v)` as its coefficients along `1,xi,xi^2`
in this basis, and its fourth coordinate as `rho dot v`. This is one
fixed invertible linear coordinate map, independent of epsilon, and
the constant right-hand side has coordinates `(1,0,0,0)` exactly.

Let A_epsilon be the four-by-four matrix of the mean feature columns
in these coordinates, with its rows divided respectively by

\[
                         1,\quad\delta,\quad\delta^2,\quad\epsilon.
\tag{3}
\]

The scaled right-hand side remains `(1,0,0,0)`. This fact is essential:
a small determinant of the unscaled interpolation matrix alone would
not give a bounded inverse on this particular right-hand side.

## 2. An explicit invertible limit

Set `h_j=phi^(j)(t_*)`, `phi=tanh`, so `h_1=2/3`,
`h_2=-4/(3 sqrt(3))!=0`. Write

\[
 F_j=x_j^2-y_j^2={2\over3}x_j^2+{a\over3x_j},
                    \qquad j=0,-,+,
\]

for the three limiting even critical-point types near t_*. All quantities
are those of (18)--(19) of the frozen report. Taylor expansion in the
fixed coordinate map just defined gives

\[
 A_\epsilon\longrightarrow A_*=
 \begin{pmatrix}
 \phi(t_*)&\phi(t_*)&\phi(t_*)&\phi(t_0)\\
 h_1x_0&h_1x_-&h_1x_+&0\\
 \frac12h_2F_0&\frac12h_2F_-&\frac12h_2F_+&0\\
 q(t_*)&q(t_*)&q(t_*)&q(t_0)
 \end{pmatrix},
 \qquad q(t)=lt\phi'(t),\quad l<0.
\tag{4}
\]

Here is why the chosen fixed coordinates do not alter that limit.
Near t_* the leading feature terms are a constant, a multiple of
`delta x_j xi`, and a multiple of
`delta^2 (x_j^2-y_j^2)xi^2`. Axial shifts change the constant and
terms of lower degree, but vanish after the respective row scalings
in (3) when they could affect the displayed coefficients. Data-angle
changes are O(epsilon); their effects on linear and quadratic
transverse terms are higher order than delta and delta squared.
The O(epsilon) change of the single input's axial argument lies in
the e_0 direction, so does not contaminate these first three coordinates.
The fourth coordinate is exactly Q at each critical point and is
`epsilon q(t_*)+O(epsilon delta)` there. At the t_0 pair the linear
and quadratic nonconstant coordinates are O(epsilon), and its Q value
is `epsilon q(t_0)+o(epsilon)`. These are precisely the remainders
verified in the frozen report's even determinant calculation.

The first three columns in the first three rows have nonzero determinant:
the second divided difference of F at `x_0,x_-,x_+` is

\[
                 {2\over3}+{x_0^2\over3x_-x_+}>0.
\]

After eliminating the first three entries of the last column, its last
entry is

\[
                  q(t_0)-{\phi(t_0)\over\phi(t_*)}q(t_*)\ne0.
\tag{5}
\]

Indeed `q(t)/phi(t)=2lt/sinh(2t)` is strictly monotone on positive t,
and `t_0>t_*`. Thus A_* is invertible. Continuity of inversion at an
invertible finite matrix now gives

\[
 b_\epsilon=A_\epsilon^{-1}(1,0,0,0)^T\longrightarrow
 b_*=A_*^{-1}(1,0,0,0)^T.
\tag{6}
\]

Splitting the three mean coefficients equally among their paired columns
gives `beta_epsilon -> beta_*` in R7. In particular this specific
interpolant is uniformly bounded even though `det V_epsilon -> 0`.

## 3. One matrix and readout, and convergence on the same carrier

Choose epsilon_0 sufficiently small that the preceding branches and
invertibility statements hold. By (6), a finite B bounds
`||beta_epsilon||_1` for `0<epsilon<=epsilon_0` and the limit.
Fix once and for all `lambda>0` with `lambda B<1/2`, and set

\[
 \alpha_{j,\epsilon}=\lambda\beta_{j,\epsilon},\qquad
 p_{j,\epsilon}=|\alpha_{j,\epsilon}|
                  +{1-\sum_k|\alpha_{k,\epsilon}|\over7}.
\tag{7}
\]

These probabilities sum to one, exceed `|alpha_j|` by at least 1/14,
and depend continuously on epsilon including zero. Assign the fourteen
outcomes `(j,sigma)` probabilities

\[
               \pi_{j,\sigma,\epsilon}
                    ={p_{j,\epsilon}+\sigma\alpha_{j,\epsilon}\over2}.
\tag{8}
\]

Use one fixed order of these outcomes and consecutive intervals in the
uniform random variable obtained from the distribution function of
`|G_2|`. Their finitely many interval endpoints vary continuously.
The selected outcome therefore converges almost surely as epsilon tends
to zero, except on the finite set of limiting boundaries, which has
probability zero. The seven critical values remain uniformly bounded and
converge. Consequently

\[
 w_\epsilon=\operatorname{sign}(G_1)\sigma_\epsilon
                        s_{J_\epsilon,\epsilon}
             \longrightarrow w_*\quad\hbox{in }L^2.
\tag{9}
\]

For completeness, almost-sure convergence follows because a uniform
coordinate separated from every limiting endpoint eventually remains
in the same interval. The bound `|w_epsilon-w_*|^2<=4R^2` for a fixed
R then gives L2 convergence by dominated convergence.

Keep exactly the fixed matrix `M=e_1q^T` from the frozen carrier
construction. Every lower moment equals `lambda A`, so the common
effective upper vector is always `z e_1`, with
`z=lambda kappa>0` independent of epsilon. The projected readout

\[
 c={F\over\|H-P_EH\|_2^2}(H-P_EH),\quad
 H=\phi(zB),\quad
 E=\operatorname{span}\{B\phi'(zB),B^2\phi''(zB),\phi''(zB)\}
\tag{10}
\]

is therefore also independent of epsilon. It is one bounded odd
function, not merely a family bounded separately at each epsilon.
The states `(w_epsilon-g,c,M)` converge in the physical Hilbert norm.
Their actual lower fields, readouts, matrix norms, and Hilbert norms
are uniformly bounded.

At the limit the lower field takes values in

\[
 \{\pm(t_*/C)e_1,\quad\pm(t_0/C)e_1\}.
\tag{11}
\]

Both magnitudes have strictly positive total probability by the strict
slack in (7)--(8). The first row of (4)--(6) gives the exact limiting
constant-feature interpolation, so the lower moments remain `lambda A`.
For the original data, every axial value s obeys
`grad Q(s)=phi'(Cs_1) sum_i rho_i u_i=0`. Equations (9)--(11) of the
frozen report therefore verify directly that the limiting state is an
equilibrium with loss 48/49 and the same rank-one PSD Hilbert Hessian.

This limit is different from every old state whose lower field has one
fixed magnitude a. If P_* and P_0 are its positive total masses at the
two magnitudes, the reverse triangle inequality gives, for any field
with pointwise magnitude a,

\[
 \|w_*-w_{\rm old}\|_2^2
 \ge P_*\big(t_*/C-a\big)^2+P_0\big(t_0/C-a\big)^2
 \ge P_*P_0\big((t_0-t_*)/C\big)^2>0.
\tag{12}
\]

Thus bounded continuation does not contradict a local exclusion theorem
near a fixed two-point lower field. The old data have a different PSD
equilibrium at which these branches accumulate.

At each positive seed epsilon, continuity with respect to freely
perturbed data allows an open neighborhood on which the same fixed
lambda still gives `sum |alpha_j|<1`. Shrink these neighborhoods so
the roots and interpolation coefficients differ from their seed values
by at most epsilon. The fixed matrix and readout then work on all those
neighborhoods; their associated states remain uniformly bounded and
converge to (11) along any sequence through the shrinking neighborhoods.
This is an additional open-set existence statement; it imposes no
uniform lower bound on neighborhood size.

## 4. An open set of fixed free perturbation directions

The following second strengthening does not use uniform boundedness of
`V^{-1}1` away from the symmetric path. Let

\[
 \mathcal T=\prod_{i=1}^7T_{u_i^0}S^2\cong\mathbb R^{14},\qquad
 u_i(\epsilon,\xi)
       ={u_i^0+\epsilon\xi_i\over\sqrt{1+\epsilon^2|\xi_i|^2}},
                  \quad\xi\in\mathcal T.
\tag{13}
\]

These are independent normalized affine spherical paths, real analytic
in epsilon and xi near any fixed finite velocity. Take xi^0 to be the
velocity of the symmetric seed path in the frozen report. The path
(13) has the same first derivative but may have different acceleration.
This does not change any decisive leading coefficient:

* Both critical-point blowups use only the first data derivative.
  Second data changes are O(epsilon squared), giving higher-order terms
  after the stated divisions by epsilon or epsilon^(3/2).
* At xi^0 the normalized path preserves reflection. Its six paired
  first coordinates change only by O(epsilon squared), which is higher
  order than the O(epsilon) odd determinant coefficient. Its changed
  angle-zero first coordinate agrees to first order with the seed.
* The even determinant uses the first Q perturbation q and transverse
  terms of orders delta and delta squared; the odd determinant uses
  first Q perturbations and the limiting critical roots. All are
  unchanged by the acceleration difference.

Set `tau=epsilon^(1/6)`. At t_* use the substitutions
`t=t_*+tau^2 T`, `X=tau^2 x`, `Y=tau^2 y`, and divide all three
critical equations by tau^6. At t_0 use
`t=t_0+tau^3 T`, `X=tau^3 x`, `Y=tau^3 y`, dividing the transverse
equations by tau^6 and the axial equation by tau^9. The divided maps
extend real analytically jointly in `(tau,xi,T,x,y)` to tau=0.

To check the axial division at t_0 for unrestricted xi, the first
data variation on the axis always has the form
`q_xi(t)=l_xi t phi'(t)`, with `l_xi=sum_i rho_i xi_{i,1}/C`.
Thus `q_xi'(t_0)=0` for every xi. The leading divided axial equation
is

\[
 q_\xi''(t_0)T+K_3'(t_0)P_3(x,y)
                    +B_\xi'(t_0)\cdot(x,y)=0,
\]

where B_xi is the two-component first transverse data derivative.
The transverse equations have limit

\[
 3K_3(x^2-y^2)+(B_\xi)_1=0,\qquad
 -6K_3xy+(B_\xi)_2=0.
\]

At xi^0 the seven limiting critical zeros have the invertible
Jacobians verified in the frozen report. The real-analytic implicit
function theorem therefore provides seven critical-point branches
real analytic jointly in `(tau,xi)` on one neighborhood of
`(0,xi^0)`. For small positive tau the points are nondegenerate and
distinct, after shrinking that neighborhood as necessary. The theorem
requires a real-analytic map and an invertible derivative with respect
to the unknowns; the preceding divisions verify the first hypothesis,
and the frozen critical-point calculations verify the second.

Form their seven-by-seven feature matrix V(tau,xi). Its determinant
D(tau,xi) is real analytic. At xi^0 its leading order is

\[
                       D(\tau,\xi^0)=c\tau^{27}+o(\tau^{27}),
                            \qquad c\ne0.
\tag{14}
\]

The order is obtained from the frozen proof without another expansion:
the even determinant has order `delta^3 epsilon=tau^12`; the
normalized odd determinant has order `delta^4=tau^8`; restoring
its three feature-difference normalizations multiplies by the three
nonzero Y scales `delta,delta,sqrt(epsilon)`, of product tau^7.
Thus the odd determinant has order tau^15 and the full determinant
order tau^27. Every leading factor was proved nonzero there.

Consequently the coefficient

\[
 C_{27}(\xi)={1\over27!}\partial_\tau^{27}D(0,\xi)
\]

is continuous and nonzero at xi^0. On some open neighborhood W of
xi^0 it remains nonzero. For every fixed xi in W, D as a function
of tau is therefore not identically zero. Its convergent Taylor series
has a first nonzero coefficient of order at most 27, so there is a
direction-dependent `tau_xi>0` for which

\[
                         D(\tau,\xi)\ne0
                    \quad\text{for }0<\tau<\tau_\xi.
\tag{15}
\]

This last step uses only the definition of a real-analytic function:
factor its first nonzero power of tau; the remaining analytic factor
has a nonzero value at zero and stays nonzero nearby. Lower Taylor
coefficients can become nonzero as xi changes, so a uniform threshold
is neither needed nor asserted.

The critical-point interpolation criterion of the frozen report now
constructs an exact loss-48/49 rank-one-PSD equilibrium for every
`xi in W` and every `0<epsilon<tau_xi^6`. For each fixed positive
amplitude it uses the unchanged canonical carrier and full state space.
Its lambda and readout may depend on `(epsilon,xi)` off the seed path.
No uniform bounds over W are inferred from this analytic determinant
argument.

Rescaling a velocity only reparametrizes (13):
`u(epsilon,a xi)=u(a epsilon,xi)` for positive a. Thus W yields an
open patch of unit directions with the same eventual-survival property.
This strengthens the open-data-set conclusion to a positive-volume
family of fixed independent noise directions. It contradicts a global
almost-every-direction claim that all positive-loss PSD equilibria are
removed by every sufficiently small nonzero noise amplitude. It still
does not settle a local claim restricted to a specified old equilibrium
or the probability of convergence to any surviving equilibrium.

## 5. Attainable zero loss for every data set in the construction

This corollary was also suggested by the lead after the independent
report was frozen. It verifies directly, using only V invertibility,
that 48/49 is strictly above an attainable loss of zero for all data
sets treated here.

Replace the constant interpolation target in (1) by
`r=(1,2,3,4,5,6,7)^T`. Choose a sufficiently small positive lambda
so `alpha=lambda V^{-1}r` has l1 norm below one. The same exact
canonical partition construction then gives

\[
 a_i=\lambda i A,\qquad Ma_i=\lambda\kappa i e_1,
 \qquad H_i(B)=\tanh(\lambda\kappa i B).
\]

These seven upper functions are linearly independent. An almost-sure
linear identity extends from the open upper-mark support interval to
the real line by continuity and analyticity. Its limit at positive
infinity forces the sum of its coefficients to vanish. If a coefficient
is nonzero, take the smallest positive slope with a nonzero coefficient;
after subtracting the constant limit and multiplying by the exponential
of twice that slope times B, the identity tends to minus twice that
coefficient, a contradiction. Thus the exact Gram
`K_ij=E_2[H_i H_j]` is positive definite. The bounded odd readout

\[
                         c=\sum_i(K^{-1}y)_iH_i
\]

has predictions y and loss zero. This expressivity check uses the same
data and canonical architecture; it makes no claim that training from
a prescribed initial state reaches the fitted state.

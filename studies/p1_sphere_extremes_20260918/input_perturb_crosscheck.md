# Informed analytical cross-check of the persistence construction

2026-09-18. This is an explicitly informed cross-check performed after my
independent input-perturbation candidate was frozen. It is not a fresh
isolated review and is not a promotion decision. No numerical experiment,
external source, or other study was used. The only newly read scientific
input was the complete `input_perturb_persist.md`, whose SHA256 was verified
as

`641204a025374966da3114bd153f10956d0d9d704d4e6420cd9659ea6cd30dae`.

The remaining scientific dependencies were the already allowed complete
`docs/observable_p1.md`, `FINITE_BASIN_EXTENSION.md`,
`finite_basin_geometry.md`, and `finite_basin_tail.md`. In particular I did
not fetch the two additional reports listed in the candidate's provenance;
the necessary carrier and Hessian arguments can be checked from the
presently allowed material and the explicit candidate. The research and
rigorous-math skills remained in effect. This is the only file written in
this cross-check; neither frozen candidate was edited.

**Verdict:** the stated open-data existence conclusion is supported by the
analytical construction. I found no substantive gap in the seven critical
points, their nondegeneracy, the invertible feature matrix, or its exact
population realization. The decisive determinant coefficients have the
claimed nonzero signs. One minor typesetting error appears in equation
(30): the comma after `epsilon` should be a multiplication space.

The validated scope is nonempty open surviving-data sets arbitrarily near
the original inputs, and therefore positive survival probability for a
noise law having strictly positive density throughout such a neighborhood.
It does not establish survival with probability one, a uniform probability
bound, convergence of these states to a fixed original equilibrium, a
local minimum, or a positive-probability attraction basin.

## 1. The first perturbation coefficients are correct

I use the candidate's notation in this report. Its `a<0,b>0` denote
coefficients of the scaled critical-point polynomial, not the positive
amplitude of the earlier two-point lower field.

For the triangle, the residual-weighted third transverse moment is
`-6 P_3/49`. The square's third moment vanishes. At fourth order the
triangle contributes `-9(X^2+Y^2)^2/49`; the square contributes
`9(X^2+Y^2)^2/49-3P_4/49`. Dividing these moments by `3!` and `4!`
gives exactly

\[
Q_0(t,X,Y)=-\frac{\phi'''(t)}{49}P_3(X,Y)
 -\frac{\phi''''(t)}{392}P_4(X,Y)+O((|X|+|Y|)^5).
\tag{1}
\]

The finite sum of smooth tanh terms gives the stated differentiated
remainder bounds uniformly on a compact `t` interval.

For the changed positive input, differentiating its square-root second
coordinate gives `dot u_2=-Cd/S`. The rotated negative pair contributes
`-12 omega/(49 sqrt(2))` to the candidate's `v`, so a finite `omega`
indeed imposes `v=2l`. No sphere constraint obstructs this choice.

The axial first data variation and its transverse derivative are

\[
q(t)=l t\phi'(t),\qquad
B(t)=v\phi'(t)+lt\phi''(t)
=\phi'(t)[v-2lt\phi(t)].\tag{2}
\]

For the cross term in the second identity, only the positive angle-zero
input changes its first coordinate, so
`sum rho_i dot u_(i,1) cos(theta_i)=L_1`. This verifies the otherwise
potentially important geometric cross term.

At `t_*=arctanh(1/sqrt(3))`, direct differentiation gives

\[
\phi'(t_*)=2/3=:h_1,\quad
\phi'''(t_*)=0,\quad
\phi''''(t_*)=16/(3\sqrt3)=:h_4>0.
\]

The strict inequality `2t_*/sqrt(3)<1` follows from
`arctanh(x)<x/(1-x^2)`. Thus with `K=-h_4/49`,

\[
a=-q'(t_*)/K<0,\qquad b=B(t_*)/K>0,
\qquad 0<-a<b.
\tag{3}
\]

The scaling `epsilon=delta^3`, `t=t_*+delta T`, `X=delta x`,
`Y=delta y` therefore gives the candidate's limiting polynomial

\[
\mathcal P=T(x^3-3xy^2)+\tfrac18(x^4-6x^2y^2+y^4)-aT+bx.
\tag{4}
\]

All three original critical equations begin at order `delta^3`.
Their quotients by `K delta^3` extend smoothly to `delta=0`, with
the gradients of (4) as their limits. The next terms are `O(delta)`
uniformly near each proposed finite limiting solution.

## 2. The five roots and their nondegeneracy

The critical equations of (4) are

\[
x^3-3xy^2=a,
\]
\[
3T(x^2-y^2)+\tfrac12(x^3-3xy^2)+b=0,
\]
\[
y[-6Tx+\tfrac12y^2-\tfrac32x^2]=0.
\tag{5}
\]

The plane solution is `x_0=a^(1/3)<0`, `y_0=0`, with
`T_0=-(a/2+b)/(3x_0^2)`. Its Hessian has a `(T,x)` block with
zero top-left entry and nonzero off-diagonal entry `3x_0^2`, and its
uncoupled `yy` entry is `(2b-a/2)/x_0!=0`. Hence this root is
nondegenerate.

At a solution with `y!=0`, the last equation solves
`T=(y^2-3x^2)/(12x)` once `x!=0`. The first equation excludes `x=0`
because `a!=0`. Substituting this value of `T` into the second equation
and multiplying by `4x` gives the particularly useful exact identity

\[
4bx-(x^2+y^2)^2=0.\tag{6}
\]

Thus `x>0`. With `kappa=2sqrt(b)` and `q=x^(3/2)`, equations (5)--(6)
become

\[
y^2=\kappa\sqrt{x}-x^2,\qquad
4q^2-3\kappa q=a.
\tag{7}
\]

The roots are exactly
`q_±=(3kappa±sqrt(9kappa^2+16a))/8`. Since `-b<a<0`, their
discriminant lies strictly between `5kappa^2` and `9kappa^2`.
They are positive, distinct, and each is less than `kappa`, giving
strictly positive `y^2` and two signs of `y` at each root.

Nondegeneracy also follows rigorously from these eliminations. Dividing
the third equation of (5) by `y` is a locally invertible row operation;
its `T` coefficient is `-6x!=0`. At fixed positive `x`, equation (6)
solves for the positive radius `x^2+y^2`, and `y!=0` makes that a local
coordinate. Finally the remaining scalar equation has derivative
`8q-3kappa!=0` at both quadratic roots. Thus the full three-variable
Jacobian is invertible at all four off-axis roots.

The finite-dimensional implicit-function theorem applies at each of the
five roots. Its exact hypotheses are smooth parameter dependence and an
invertible derivative in the three unknowns; both have been checked.
For each sufficiently small positive `delta`, it gives an actual critical
point and an invertible Jacobian of the divided equations. In original
coordinates this derivative is `(K delta^2)^(-1)` times the Hessian of
`Q_epsilon`, so the actual critical points are nondegenerate as claimed.

## 3. The two further roots at the other special axial value

The equation `2t_0 tanh(t_0)=1` has a unique positive root because its
left side increases strictly from zero to infinity. The inequality in
Section 1 gives `t_0>t_*`, so `phi'''(t_0)>0`. With `l<0`,

\[
q'(t_0)=0,\qquad
q''(t_0)=l\phi'(t_0)[-2\phi(t_0)-2t_0\phi'(t_0)]\ne0,
\]

\[
B_0=\phi'(t_0)(v-l)=\phi'(t_0)l<0,
\qquad K_3=-\phi'''(t_0)/49<0.
\tag{8}
\]

Under `r=sqrt(epsilon)`, `X=rx`, `Y=ry`, `t=t_0+rT`, the two
transverse gradient components begin at `r^2`, while the axial component
begins at `r^3` because `q'(t_0)=0`. Their smooth quotient limits are

\[
3K_3(x^2-y^2)+B_0=0,\qquad -6K_3xy=0,
\]

\[
q''(t_0)T+K_3'(t_0)(x^3-3xy^2)+B'(t_0)x=0.
\tag{9}
\]

At `x=T=0`, `y=±sqrt(B_0/(3K_3))`, the transverse Jacobian has
off-diagonal entries `-6K_3y` and determinant `-36K_3^2y^2!=0`.
The remaining diagonal derivative is `q''(t_0)!=0`. The same theorem
therefore gives two nondegenerate actual critical points. Its `O(r)`
corrections in scaled variables yield `X=O(epsilon)`,
`Y=±sqrt(epsilon)sqrt(B_0/(3K_3))+O(epsilon)`, and
`t=t_0+O(epsilon)`, exactly the orders used later.

The five earlier points and these two are pairwise distinct, and have
positive axial coordinates separated from those of their negatives.

## 4. The feature determinant: even block

Reflection gives a fixed decomposition of the seven-dimensional input
value space into dimensions four and three. Pair averages and differences
of the critical-point feature columns respect this decomposition. The
required change of columns is invertible since the paired points are
distinct.

In the even block, let `xi_i=cos(theta_i)` at the original data. The four
distinct values are `1,-1/2,1/sqrt(2),-1/sqrt(2)`. The vectors
`1,xi,xi^2` are independent, and the nonzero functional `rho` annihilates
all three. They therefore admit coordinates consisting of these three
polynomial coefficients and the `rho` pairing. The use of a fixed
unperturbed even basis is legitimate: the reflection itself is preserved,
and basis corrections from the changed angles enter above the required
leading orders.

For the three columns near `t_*`, their leading first-three-coordinate
matrix has rows proportional to

\[
1,\qquad \delta x_j,\qquad
\delta^2 A_j,\qquad A_j=x_j^2-y_j^2.
\tag{10}
\]

The proportionality constants are `phi(t_*)`, `h_1`, and
`phi''(t_*)/2`, all nonzero. Axial shifts only affect higher orders or
the already lower-degree rows. Input-height changes contribute
`O(epsilon)=O(delta^3)`, also above the last displayed row's order.

At all three limiting points `j=0,-,+`,

\[
A_j=\frac23 x_j^2+\frac{a}{3x_j}.\tag{11}
\]

The second divided difference at the three distinct nonzero `x_j` is

\[
\frac23+\frac{a}{3x_0x_-x_+}
=\frac23+\frac{x_0^2}{3x_-x_+}>0.
\tag{12}
\]

Thus the first three rows of these columns have determinant equal to a
nonzero constant times `delta^3+o(delta^3)`.

Their fourth coordinate is the exact critical value of `Q_epsilon`,
namely `epsilon q(t_*)+O(epsilon delta)`. For the fourth even column
near `t_0`, its first three coordinates are
`(phi(t_0)+O(epsilon),O(epsilon),O(epsilon))`, and its fourth coordinate
is `epsilon q(t_0)+o(epsilon)`.

The elimination coefficients using the first three columns are bounded:
after row division by `1,delta,delta^2`, their right-hand side remains
bounded and the coefficient matrix has a nonsingular limit. Their sum
tends to `phi(t_0)/phi(t_*)`. The final scalar Schur complement is
therefore

\[
\epsilon\left[q(t_0)-\frac{\phi(t_0)}{\phi(t_*)}q(t_*)\right]
+o(\epsilon).\tag{13}
\]

This bracket is nonzero since
`q(t)/phi(t)=2lt/sinh(2t)` is strictly monotone for positive `t` and
`t_0!=t_*`. The derivative numerator is
`sinh(2t)-2t cosh(2t)<0`, as its derivative is `-4t sinh(2t)<0`
and its value at zero is zero. The even determinant is consequently
nonzero for all sufficiently small positive epsilon.

## 5. The feature determinant: odd block

The three reflected input pairs have cosines
`-1/2,+1/sqrt(2),-1/sqrt(2)` and nonzero sines. The three vectors
`sin(theta)`, `xi sin(theta)`, `xi^2 sin(theta)` form an odd-space
basis. Their coefficients may be taken at the perturbed paired angles;
the associated cubic reduction is the original identity

\[
\xi^3=-\tfrac12\xi^2+\tfrac12\xi+\tfrac14
\tag{14}
\]

plus coefficient errors `O(epsilon)`. The six paired points have exactly
the same first coordinate `C` along the chosen data path, so no hidden
axial perturbation enters the following odd calculation.

For one critical pair, divide the feature difference by
`2Y phi'(t)`, which is nonzero. Taylor expansion gives the third
coordinate in the odd basis as

\[
\frac{\phi'''(t)}{6\phi'(t)}(3X^2-Y^2)
-\frac{\phi''''(t)}{12\phi'(t)}X(X^2-Y^2)
\ +\hbox{higher terms}.
\tag{15}
\]

To check (15), before reducing cubic powers the relevant expression is

\[
\frac{\phi'''(t)}{6\phi'(t)}
 [3X^2\xi^2\sin\theta+Y^2\sin^3\theta]
+\frac{\phi''''(t)}{6\phi'(t)}
 [X^3\xi^3\sin\theta+XY^2\xi\sin^3\theta].
\]

Substitute `sin^3(theta)=(1-xi^2)sin(theta)` and (14). Near `t_*`,
`phi'''(t)=delta h_4 T+O(delta^2)`, so (15) becomes

\[
\delta^3\frac{h_4}{6h_1}
\left[T(3x^2-y^2)-\tfrac12x(x^2-y^2)\right]+o(\delta^3).
\tag{16}
\]

The first two coordinates are `1+O(delta^3)` and
`delta [phi''(t_*)/h_1]x+O(delta^2)`. Any harmless normalization
changing the first error to `O(delta^2)` still gives the same determinant
limit. Corrections to (14) multiply cubic-order terms and cannot affect
the order in (16).

I independently reduced the bracket `E` in (16). On an off-axis solution,
use `y^2=x^2/3-a/(3x)` and `T=-(3x^2-y^2)/(12x)` to obtain

\[
E=-\frac{25}{27}x^3-\frac{17}{54}a-\frac{a^2}{108x^3}.
\]

Equation (6) gives
`a^2/x^3=36b-16x^3+8a`. Substitution yields exactly

\[
E=-\frac79x^3-\frac7{18}a-\frac13b.\tag{17}
\]

For the pair near `t_0`, the third coordinate in (15) is

\[
-\frac{\phi'''(t_0)}{6\phi'(t_0)}Y^2+o(\epsilon)
=\epsilon\frac{49B_0}{18\phi'(t_0)}+o(\epsilon).
\tag{18}
\]

Its first coordinate tends to one, and its second is `O(epsilon)`.
Using `v=2l` and the definitions of `a,b` shows

\[
\frac{49B_0}{18\phi'(t_0)}
=\frac{h_4}{6h_1}\left[-\frac{a+b}{3}\right].\tag{19}
\]

Thus after dividing the second and third rows of the odd determinant
by `delta` and `delta^3`, respectively, and removing nonzero fixed
constants, its limit is the affine-plane determinant of the three points

\[
(x_-,E_-),\quad (x_+,E_+),\quad (0,-(a+b)/3).
\]

By (17), the first two points' line has intercept exceeding the third
point's height by

\[
-\frac{a}{18}+\frac79x_-x_+(x_-+x_+)>0.\tag{20}
\]

This is strict because `a<0` and both `x_-,x_+` are positive and
distinct. Hence the odd determinant has a nonzero leading coefficient.
Restoring the feature-difference column factors is safe since every
`Y` is nonzero and `phi'(t)>0`. Both reflection blocks, and therefore
the complete seven-by-seven feature matrix, are invertible for every
sufficiently small positive epsilon.

## 6. Population realization, all blocks of the Hessian, and openness

The final realization does not require any unproved independence of the
trained lower field and its canonical marks. Choose
`alpha=lambda V^(-1)1` with `sum |alpha_j|<1`, and realize these signed
weights by an even partition of `|G_2|`. With
`w=sign(G_1) sigma s_J`, coordinate-one mark expectations factor against
the partition, while all other coordinate-pair contributions vanish
because their remaining independent factor has mean `E sign(G_1)=0`.
Thus `a_i=lambda A` is exact for every input. Odd parity is preserved,
and the actual lower field is bounded. The lower displacement is in
physical `L^2`.

The readout projection onto the orthogonal complement of
`span{B phi'(zB),B^2 phi''(zB),phi''(zB)}` is valid. The span is
finite-dimensional and closed. Its members tend to zero in their real
analytic extensions as `B` tends to positive infinity, while
`H=tanh(zB)` tends to one; hence `H` is not in the span. The resulting
readout is bounded and odd for each fixed positive `z`, even if its
norm deteriorates as `z` tends to zero.

The three orthogonality conditions kill both the entire first upper
derivative vector `d` and the entire second derivative matrix `C_c`:
the longitudinal diagonal uses `B^2 phi''`, transverse diagonals use
`phi''` and coordinate independence, and off-diagonals use a centered
independent upper coordinate. Thus no transverse matrix direction was
omitted.

Every selected lower field value is a signed critical point of `Q`, so
`grad Q(w)=0` almost surely. For every physical direction, the residual
sum of first effective-vector variations is consequently zero. The
second prediction variation has exactly the three terms displayed in
the candidate: a readout/effective-vector mixed term, the `C_c` quadratic
term, and the `d` times second effective-vector term. All their residual
sums vanish. The remaining Hessian is precisely

\[
D^2L[(h,k,N),(h,k,N)]=2\langle k,H\rangle^2.
\tag{21}
\]

This is an actual Hilbert Hessian. Each lower critical coefficient is
zero; bounded marks make the finite moment coefficients locally
`C^(1,1)` on `L^2`, while the lower gate maps are bounded and Lipschitz
into `L^2`. Expanding their product about a zero coefficient gives a
Frechet linearization with an `O(r)`-Lipschitz remainder on radius-`r`
balls, exactly as in the allowed geometry source. No isolated second
Frechet derivative of the lower nonlinear activation map is assumed.

Finally, fix one sufficiently small positive epsilon. The seven ordinary
finite-dimensional critical points have invertible Hessians and the
feature matrix has nonzero determinant. The same implicit-function
theorem, now with all fourteen spherical data coordinates as parameters,
continues all seven points in a full open neighborhood of that data set.
Invertibility of the feature matrix persists by continuity. The exact
population criterion therefore works on this full open neighborhood,
including changes breaking reflection. Choosing epsilon small places
such an open surviving set inside any prescribed neighborhood of the
original data.

## 7. Consequence and remaining distinctions

The candidate establishes the claimed sub-loss-one PSD equilibrium on
open sets of arbitrarily small freely perturbed data, with the exact
canonical marks and full physical tangent space. A probability law
strictly positive in density throughout a small data neighborhood gives
positive probability to a sufficiently close one of these open sets.
It is therefore enough to refute global almost-sure elimination of all
such equilibria under that fixed-neighborhood noise interpretation.

The proof does not establish a positive-measure set of fixed tangent
directions for which survival holds at every sufficiently small amplitude;
that would need a parameter-uniform or directionwise continuation
argument beyond the open-set statement reviewed here. This quantifier
distinction does not weaken the candidate's actual stated theorem.

There is no conflict with the previously checked local exclusion near a
specified original state. The constructed lower support converges toward
the two exceptional axial values `t_*` and `t_0`, exactly where that local
exclusion proof's coefficients `phi'''(t)` and
`phi'(t)+t phi''(t)` vanish. It also need not have a bounded readout or
matrix continuation as the perturbation vanishes. The global existence
and local exclusion statements concern different sets of states.

No attraction or basin-size conclusion follows from the PSD rank-one
Hessian alone. Those dynamical claims remain open.

# Tiny free input perturbations: robust positive-loss PSD states away from a fixed endpoint

Independent analytical route, frozen 2026-09-18 before comparison with any
other current route. Internally checked candidate; not independently reviewed
or promoted. No experiment, numerical premise, or external scientific source
was used. Scientific inputs were exactly the complete
`docs/observable_p1.md`, `FINITE_BASIN_EXTENSION.md`,
`finite_basin_geometry.md`, `finite_basin_tail.md`,
`dependent_basin_functional.md`, and `dependent_finite_fitting.md`.
The investigate-conjectures and solve-math-rigorously skills, research-contract
and adversarial-audit instructions were applied. This is the only file written.

## 1. Precise conclusion

Fix the seven-input triangle/square construction with square angles
`pi/4,3pi/4,5pi/4,7pi/4`, equal weights, three positive labels and four
negative labels. For every neighborhood of this data set in `(S^2)^7`,
there is a nonempty open subset of data sets for which the exact canonical
p=1 population system admits an equilibrium with

\[
             L=48/49,\qquad
 D^2L[(h,k,N),(h,k,N)]=2\langle k,H\rangle_2^2.
\tag{1}
\]

The Hessian is the actual physical Hilbert Fréchet Hessian, PSD of rank
one. All three blocks remain trainable, and the full canonical correlated
marks and odd sector are retained. The open subsets admit arbitrary
independent input changes, not only symmetry-preserving changes.

The construction does **not** assert convergence of these states to the
specific two-point lower state of the earlier example. Its lower field
uses seven critical-point pairs; its readout or matrix size can deteriorate
as the data perturbation shrinks. Consequently this result is compatible
with exclusion of PSD equilibria in a sufficiently small state neighborhood
of one fixed old equilibrium. It does refute a global claim that sufficiently
small generic input noise eliminates every sub-loss-one PSD equilibrium.
For any noise law with strictly positive density throughout a small data
neighborhood, the surviving-data event has positive probability. No uniform
lower probability bound, almost-sure survival, local minimum, or positive
basin probability is asserted.

The proof constructs seven nondegenerate critical points of one scalar
function, proves their feature evaluation matrix invertible, realizes its
interpolant on the unchanged population carrier, and chooses a readout with
vanishing first and second upper derivatives.

## 2. A sufficient critical-point interpolation criterion

Write `phi=tanh`, `F=-1/7`, and

\[
 \rho_i=(F-y_i)/7=
 \begin{cases}-8/49&i\text{ positive},\\6/49&i\text{ negative},\end{cases}
 \qquad Q(s)=\sum_{i=1}^7\rho_i\phi(s\cdot u_i).
\tag{2}
\]

Suppose Q has seven critical points `s_1,...,s_7` for which

\[
                     V_{ij}=\phi(s_j\cdot u_i)
\tag{3}
\]

is invertible. The critical points and their negatives are permitted to
be used as actual lower-field values. Then (1) has an exact realization.

Here are all details of that realization. On the canonical dimension-three
lower carrier let `epsilon=sign(G_1)`,
`A=E_1[b_1 epsilon]`, and let q select the normalized `tanh(G_1)`
coordinate. Thus `kappa=q dot A=E|q dot b_1|>0`. The vector A is supported
on the two coordinate-one mark entries. Coordinate-pair independence is
used here; no independence of g from b_1 is imposed.

Choose `lambda>0` sufficiently small that the vector

\[
                    \alpha=\lambda V^{-1}{\bf1}
                    \quad\hbox{satisfies}\quad
                    \sum_j|\alpha_j|<1.
\tag{4}
\]

The nonatomic even random variable `|G_2|` can be partitioned into finitely
many events that assign a pair `(J,sigma)`, with `J in {1,...,7}` and
`sigma in {-1,1}`, such that `E[sigma 1_{J=j}]=alpha_j`. Explicitly,
choose `p_j>=|alpha_j|` summing to one and assign probabilities
`(p_j+alpha_j)/2` and `(p_j-alpha_j)/2` to `(j,+1)` and `(j,-1)`;
quantile intervals of `|G_2|` realize these probabilities exactly. Put

\[
        w=\epsilon\sigma s_J,\qquad M=e_1q^T.
\tag{5}
\]

This w is bounded and odd under simultaneous canonical mark negation.
For coordinate-one mark entries, independence from `|G_2|` factors the
expectation; for every other mark entry, the independent factor
`E epsilon=0` makes its expectation zero. Consequently

\[
 a_i=E_1[b_1\phi(w\cdot u_i)]
       =A\sum_j\alpha_j\phi(s_j\cdot u_i)=\lambda A,
 \quad Ma_i=z e_1,\quad z=\lambda\kappa>0.
\tag{6}
\]

Moreover `grad Q(w)=0` pointwise outside a null set: Q is odd, so its
gradient is even, and each `s_j` is critical. The actual displacement
`w-g` is in the physical odd L2 space, though it is not essentially bounded.

On the upper carrier let `B=b_{2,1}` and `H=phi(zB)`. Let E be the
finite-dimensional span of the three bounded odd functions

\[
 J_1=B\phi'(zB),\qquad J_2=B^2\phi''(zB),\qquad
 J_0=\phi''(zB).
\]

The function H is not in E. An almost-sure linear identity would hold
on the open support interval by continuity, and then on the real line
by real analyticity. As B tends to positive infinity H tends to one,
whereas every member of E tends to zero. Thus, with orthogonal projection
in the exact upper L2 law,

\[
 U=H-P_EH\ne0,\qquad c={F\over\|U\|_2^2}U
\tag{7}
\]

is a bounded odd readout satisfying

\[
 E[cH]=F,\quad E[cJ_1]=E[cJ_2]=E[cJ_0]=0.
\tag{8}
\]

Independence and centering of the other upper coordinates give, at the
common effective vector `z e_1`,

\[
 d=E_2[b_2c\phi'(zB)]=0,\qquad
 C_c=E_2[c\phi''(zB)b_2b_2^T]=0.
\tag{9}
\]

For C_c, its `(1,1)` entry is killed by J_2, its transverse diagonal
entries by J_0, and every off-diagonal entry by a centered independent
coordinate. This checks the complete upper second derivative, not just
its longitudinal entry.

The lower and matrix gradients vanish individually by d=0. The readout
gradient vanishes because every feature is H and `sum_i rho_i=0`.
Every prediction is F, yielding `L=48/49`.

For an arbitrary physical direction `(h,k,N)`, put

\[
 \delta z_i=N a_i+M E_1[b_1\phi'(w\cdot u_i)(h\cdot u_i)].
\]

The common lower moments and critical-point support give

\[
 \sum_i\rho_i\delta z_i
 =N\lambda A\sum_i\rho_i
    +M E_1[b_1 h^T\nabla Q(w)]=0.
\tag{10}
\]

Since d=0, `Df_i=E_2[kH]`. The residual second prediction variation
has the three terms

\[
 D^2f_i=2E_2[k\phi'(zB)b_2]\cdot\delta z_i
             +\delta z_i^TC_c\delta z_i+d\cdot\delta^2z_i.
\tag{11}
\]

Equations (9)--(10) kill their full residual-weighted sum, proving (1).
Bounded marks and activation derivatives justify the second directional
calculation for every h in L2. It is also the genuine Hilbert Hessian:
each lower critical coefficient `T_i=rho_i M^Td_i` is zero; the lower
gradient is a sum `G_i(w)T_i`, with G_i bounded and Lipschitz into lower
L2 and T_i locally C^(1,1). Subtraction of the linearization leaves an
O(r)-Lipschitz remainder on radius-r Hilbert balls, by the explicit
estimates (13)--(16) in the assigned functional report. The other two
blocks are locally C^(1,1) through finite moments. No lower second
Fréchet derivative in isolation is presumed.

Thus the remaining task is entirely finite: produce the seven critical
points and the invertible matrix (3), robustly under free input changes.

## 3. An explicit small spherical perturbation

Fix `C,S>0`, `C^2+S^2=1`. At zero perturbation the directions are

\[
 u_i=(C,S\cos\theta_i,S\sin\theta_i),
\]

with positive angles `0,+2pi/3,-2pi/3` and negative angles
`+pi/4,-pi/4,+3pi/4,-3pi/4`. Reflecting the third coordinate preserves
both the points and their labels.

Use a small positive perturbation parameter epsilon. Change only the
first coordinate of the positive angle-zero point at first order by a
fixed `d>0`, keeping that point on the sphere and in the reflection plane:

\[
 u_0(\epsilon)=(C+\epsilon d,\sqrt{1-(C+\epsilon d)^2},0).
\tag{12}
\]

Also rotate the negative pair `+pi/4,-pi/4` by opposite angle velocities
`+omega,-omega`, preserving the reflection. Keep the other four points
fixed. Denote first data derivatives by `dot u_i`, and set

\[
 L_1=\sum_i\rho_i\dot u_{i,1}=-8d/49,
 \quad l=L_1/C<0,\quad
 v={1\over S}\sum_i\rho_i\dot u_{i,2}.
\]

The angle pair contributes `-12 omega/(49 sqrt(2))` to v, so omega
can and will be selected to impose

\[
                            v=2l.
\tag{13}
\]

This is an exact smooth spherical path for sufficiently small epsilon.
There are no first-coordinate changes at the six paired points. Also
`sum_i rho_i dot u_{i,1} cos(theta_i)=L_1`, because only the angle-zero
point changes first coordinate.

For lower-field coordinates use

\[
 t=Cs_1,\qquad X=Ss_2,\qquad Y=Ss_3,
 \quad P_3(X,Y)=X^3-3XY^2,\quad
 P_4(X,Y)=X^4-6X^2Y^2+Y^4.
\]

Criticality in these scaled coordinates is equivalent to ordinary
criticality because C,S are positive. Direct finite trigonometric sums
give, for the unperturbed Q,

\[
 Q_0(t,X,Y)=-{\phi'''(t)\over49}P_3(X,Y)
            -{\phi''''(t)\over392}P_4(X,Y)
            +O((|X|+|Y|)^5).
\tag{14}
\]

The zeroth, first, and second transverse moments vanish. The cubic
moment is `-6 P_3/49`; the fourth is `-3 P_4/49`, proving the
displayed coefficients. The remainder is smooth with the differentiated
bounds needed below on every fixed bounded t interval.

On the axial line the first data derivative and its first transverse
derivative are

\[
 q(t)=\partial_\epsilon Q_\epsilon(t,0,0)|_0
           =l t\phi'(t),
 \quad B(t)=\partial_\epsilon\partial_X Q_\epsilon(t,0,0)|_0
           =\phi'(t)[v-2t\phi(t)l].
\tag{15}
\]

Reflection makes the corresponding Y derivative zero. These formulas
follow by differentiating each argument `s dot u_i`; their axial
and transverse cross term uses the last identity after (13).

## 4. Five nondegenerate critical points near a special axial value

Put

\[
 t_* =\operatorname{arctanh}(1/\sqrt3),\quad
 h_1=\phi'(t_*)=2/3,\quad
 h_4=\phi''''(t_*)=16/(3\sqrt3),\quad K=-h_4/49<0,
\]
\[
 \kappa_*=2t_*/\sqrt3<1,\qquad \eta=1-\kappa_*>0.
\]

For the strict inequality, the integral for arctanh gives
`arctanh(x)<x/(1-x^2)` for `0<x<1`; apply this at `x=1/sqrt(3)`.
At t_* the third derivative vanishes. Set `delta=epsilon^(1/3)` and

\[
 t=t_*+\delta T,\quad X=\delta x,\quad Y=\delta y.
\]

After dividing the critical equations by `K delta^3`, their limit is
the gradient of

\[
 \mathcal P(T,x,y)=T P_3(x,y)+\tfrac18P_4(x,y)-aT+bx,
\tag{16}
\]

where

\[
 a=-q'(t_*)/K=-h_1\eta l/K<0,
 \quad b=B(t_*)/K=h_1(v-\kappa_*l)/K>0,
 \quad 0<-a<b.
\tag{17}
\]

The final inequality follows from `v=2l`:
`(-a)/b=eta/(2-kappa_*)<1`. Analyticity shows the divided equations
extend smoothly to delta=0; their errors are O(delta).

Here is the complete solution of the limiting critical equations. One
solution has

\[
 x_0=a^{1/3}<0,\quad y_0=0,\quad
 T_0=-((1/2)a+b)/(3x_0^2).
\tag{18}
\]

For the other solutions put `kappa=2 sqrt(b)` and

\[
 q_\pm={3\kappa\pm\sqrt{9\kappa^2+16a}\over8},
 \quad x_\pm=q_\pm^{2/3}>0,
 \quad y_\pm^2=\kappa\sqrt{x_\pm}-x_\pm^2>0,
\]
\[
 T_\pm=-{3x_\pm^2-y_\pm^2\over12x_\pm}.
\tag{19}
\]

Each sign of y gives a solution. Indeed the equations are
`P_3=a` and, in complex notation `zeta=x+iy`,
`3T conjugate(zeta)^2+(1/2)conjugate(zeta)^3+b=0`.
For y nonzero their imaginary part after multiplication by zeta squared
gives `(x^2+y^2)^2=4bx`. Substitution into `P_3=a` gives
`4q^2-3 kappa q=a` with `q=x^(3/2)`, proving (19).
Since `-b<a<0`, its discriminant is strictly positive, both roots are
positive and distinct, and both are below kappa. This also proves the
strict positivity of the displayed y squared.

All five solutions are nondegenerate. At (18), the `(T,x)` Hessian
block has off-diagonal entry `3x_0^2` and zero `(T,T)` entry, hence
nonzero determinant; the remaining `(y,y)` entry is
`(2b-a/2)/x_0`, nonzero. At each off-axis solution, the eliminations
just performed are invertible local changes: `x>0`, `y!=0`, the
imaginary equation solves the positive radius, and the remaining
quadratic has derivative `8q-3 kappa!=0`. The T equation is linear
with a nonzero coefficient. Their full Jacobian is therefore invertible.

The finite-dimensional implicit function theorem now supplies five
nondegenerate critical points of Q_epsilon for every sufficiently small
positive epsilon, converging in the displayed scaled coordinates to
(18)--(19). The theorem is used in its elementary local form: a smooth
map of parameters and unknowns with invertible unknown derivative at a
zero has a unique nearby smooth zero branch. Smoothness and invertibility
have both been verified. The four off-axis points occur as two reflected
pairs; the fifth lies in the reflection plane.

## 5. Two additional nondegenerate critical points

There is a unique `t_0>0` such that

\[
                         2t_0\tanh(t_0)=1.
\tag{20}
\]

The left side increases strictly from zero to infinity. The inequality
in Section 4 gives `t_0>t_*`, so `phi'''(t_0)>0`. Also
`q'(t_0)=0`, `q''(t_0)!=0`, and

\[
 B_0=B(t_0)=\phi'(t_0)(v-l)<0,\qquad
 K_3=-\phi'''(t_0)/49<0.
\]

Put `r=sqrt(epsilon)`, `X=rx`, `Y=ry`, `t=t_0+rT`.
Divide the X,Y critical equations by r squared and the t equation by
r cubed. They extend smoothly to r=0. Their leading equations are

\[
 3K_3(x^2-y^2)+B_0=0,\quad -6K_3xy=0,
 \quad q''(t_0)T+K_3'(t_0)P_3(x,y)+B'(t_0)x=0.
\]

They have two zeros

\[
 x=0,\qquad y=\pm\sqrt{B_0/(3K_3)},\qquad T=0.
\tag{21}
\]

The transverse two-by-two Jacobian is invertible because y is nonzero;
the remaining T derivative is `q''(t_0)!=0`. The same verified implicit
function theorem gives two nondegenerate critical points, with

\[
 X=O(\epsilon),\quad
 Y=\pm\sqrt\epsilon\sqrt{B_0/(3K_3)}+O(\epsilon),\quad
 t=t_0+O(\epsilon).
\tag{22}
\]

These seven points are distinct, as are their negatives for small epsilon.

## 6. The seven feature vectors are independent

Reflection decomposes the seven-dimensional input-value space into an
even four-dimensional space and an odd three-dimensional space. Take
the sums and differences of feature columns in each reflected critical
pair. There are four even columns (the plane point, the two pairs near
t_*, and the pair near t_0), and three odd columns (the three pairs).
We prove both block determinants nonzero by their leading coefficients.

### 6.1. The even block

At zero perturbation let `xi_i=cos(theta_i)`. Its four distinct values
are `1,-1/2,1/sqrt(2),-1/sqrt(2)`. In the even space the three vectors
`1,xi,xi^2` are independent. The linear functional with coefficients
rho annihilates these three vectors and is nonzero, so it supplies the
fourth coordinate independently of those three.

For each of the three even columns near t_*, the leading coefficients
on these first three vectors are proportional to

\[
                        (1,\delta x,\delta^2(x^2-y^2)).
\tag{23}
\]

Their nonzero fixed multipliers are `phi(t_*)`, `phi'(t_*)`, and
`phi''(t_*)/2`; axial shifts add constant and lower-degree terms and
do not change the determinant coefficient. At all three limiting points
`x=x_0,x_-,x_+`, respectively, the third coordinate in (23) is

\[
                         x^2-y^2={2\over3}x^2+{a\over3x}.
\tag{24}
\]

For the plane point this uses `a=x_0^3`; for the other two it follows
from `P_3=a`. The second divided difference of the right side at the
three distinct nonzero x values is

\[
 {2\over3}+{a\over3x_0x_-x_+}
       ={2\over3}+{x_0^2\over3x_-x_+}>0.
\]

Thus the first three coordinates of these columns have determinant of
order delta cubed with nonzero coefficient. Their rho pairings, namely
their Q values, are
`epsilon q(t_*)+O(epsilon delta)`. The fourth column near t_0 has
constant leading value `phi(t_0)` and rho pairing
`epsilon q(t_0)+o(epsilon)`. Eliminating its first three coordinates
using the other columns leaves rho pairing

\[
 \epsilon\left[q(t_0)-{\phi(t_0)\over\phi(t_*)}q(t_*)\right]
                         +o(\epsilon).
\tag{25}
\]

The elimination coefficients remain bounded: the fourth column's linear
and quadratic transverse coordinates are O(epsilon), smaller than the
delta and delta squared scales in (23). The bracket in (25) is nonzero.
Indeed `q(t)/phi(t)=2lt/sinh(2t)` is strictly monotone for positive t
when `l!=0`; differentiating gives the nonzero sign of
`sinh(2t)-2t cosh(2t)<0`. Since `t_0!=t_*`, the two ratios differ.
This proves the even block invertible.

### 6.2. The odd block

On the three reflected input pairs the cosines at epsilon=0 are
`-1/2,+1/sqrt(2),-1/sqrt(2)`. Their nonzero sines give an odd-space
basis `sin(theta), xi sin(theta), xi^2 sin(theta)`. With the perturbed
angles this remains a basis. On the unperturbed three cosine values,

\[
                    \xi^3=-\tfrac12\xi^2+\tfrac12\xi+\tfrac14.
\tag{26}
\]

The changed angle-zero point contributes zero to every odd column.
The other six inputs have their original first coordinate C exactly,
so only their angles change; the coefficients in (26) change by
O(epsilon), which affects none of the leading coefficients below.

For a reflected critical pair with coordinates `(t,X,+Y)` and
`(t,X,-Y)`, divide its feature difference by `2Y phi'(t)`. For a pair
near t_* its coordinates in this odd basis are

\[
 \left(1+O(\delta^3),\quad
       \delta {\phi''(t_*)\over h_1}x+O(\delta^2),\quad
       \delta^3{h_4\over6h_1}E(x,y,T)+o(\delta^3)\right),
\tag{27}
\]

where possible O(delta squared) changes in the first coordinate can
equivalently be absorbed by normalization, and

\[
 E=T(3x^2-y^2)-\tfrac12x(x^2-y^2).
\tag{28}
\]

To verify the decisive third coefficient, expand the difference before
normalization. Its terms are
`phi'(t) sin(theta)+phi''(t)X xi sin(theta)` and

\[
 {\phi'''(t)\over6}[3X^2\xi^2\sin\theta+Y^2\sin^3\theta]
 +{\phi''''(t)\over6}[X^3\xi^3\sin\theta
                         +XY^2\xi\sin^3\theta].
\]

Use `phi'''(t)=delta h_4 T+O(delta^2)`,
`sin^3(theta)=(1-xi^2)sin(theta)`, and (26). The result is exactly
the third coefficient in (27). The limiting equations (19) reduce (28)
at the two off-axis x values to

\[
                  E_j=-{7\over9}x_j^3-{7a\over18}-{b\over3},
                       \qquad j=-,+.
\tag{29}
\]

For the pair near t_0, the first coordinate is `1+O(epsilon)`, the
second is O(epsilon), and the third coefficient is

\[
 \epsilon\,{49B_0\over18\phi'(t_0)}+o(\epsilon)
 =\delta^3{h_4\over6h_1}\left[-{a+b\over3}\right]+o(\delta^3).
\tag{30}
\]

Here (22) gives the first expression, while (15)--(17) give the second.
After factoring the nonzero fixed constants and powers of delta, the
odd determinant is nonzero exactly when the point
`(0,-(a+b)/3)` is not on the line through `(x_-,E_-)` and `(x_+,E_+)`.
The intercept of this line minus `-(a+b)/3` is

\[
                    -{a\over18}
                       +{7\over9}x_-x_+(x_-+x_+)>0.
\tag{31}
\]

This follows by taking the intercept of `x^3` through two positive
x values, which is `-x_-x_+(x_-+x_+)`, in (29). All factors are
nonzero, `a<0`, and both x values are positive and distinct. Thus the
odd block is invertible. Together with Section 6.1 this proves (3)
invertible for every sufficiently small positive epsilon.

## 7. Free perturbations, scope, and adverse checks

For each sufficiently small epsilon the seven critical points are
nondegenerate and the feature determinant is nonzero. Apply the same
finite-dimensional implicit function theorem with all fourteen local
spherical data coordinates as parameters. Each critical point persists;
the determinant remains nonzero by continuity. Thus the criterion in
Section 2 applies on a full open neighborhood of this perturbed data set,
including data without reflection, common latitude, or matched moments.
The neighborhoods can be taken arbitrarily close to the original seven
inputs because (12)--(13) tend to them.

The reflection was used to prove existence and determinant nonvanishing
at one point inside each open set. It is not a required property of the
final surviving data sets. The critical-point support, collapsed lower
moments, and vanishing readout derivatives are adjusted with the data.
The canonical carrier is unchanged; its continuous population supplies
the exact finite mixture through the explicit even partition in Section 2.

The theorem is an existence statement about allowed population states.
Near-singularity of V as epsilon tends to zero can force lambda to zero;
then the readout in (7) need not remain bounded uniformly. Alternatively
one can hold the effective z fixed by increasing M. There is no claim
of a bounded or continuous extension of the full equilibrium to the
chosen old state at epsilon=0, nor a claim about canonical training or
the size of any attraction basin. Local generic exclusion near that
fixed endpoint remains a logically separate question.

For perspective, a weaker all-data construction is `w=c=M=0`, an exact
equilibrium with zero Hessian and loss one: output begins at third order
in simultaneous block perturbations. That observation alone does not
answer the sub-loss-one question; the construction above does.

| Claim | Status in this route | Evidence / boundary |
|---|---|---|
| Open sets of arbitrarily small free data perturbations admit PSD equilibria at loss 48/49 | Internally proved candidate | Sections 2--7 |
| The full physical Hessian exists and is PSD, with arbitrary matrix/readout/lower directions | Internally proved candidate | Equations (9)--(11), zero lower critical coefficients |
| The carrier realization retains canonical correlations and odd parity | Explicitly verified | Equations (4)--(6), coordinate-pair independence only |
| Such equilibria persist near every fixed old two-point state | Not established | Seven critical values and possibly large readout/matrix; no state-neighborhood claim |
| Almost every small input perturbation admits such a state | Not established | Nonempty open surviving sets suffice for positive probability, not full measure |
| A surviving state has a positive-probability basin | Open here | PSD linearization alone does not control nonlinear central dynamics |


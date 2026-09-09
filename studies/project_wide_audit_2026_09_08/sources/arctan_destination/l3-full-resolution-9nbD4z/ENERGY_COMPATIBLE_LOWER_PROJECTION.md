# Energy-compatible lower-field projection

Status: CANDIDATE, not independently audited. This is a new auxiliary
clipping family for the unchanged canonical network, not the requested
uncut population theorem. The result below is a finite-width theorem:
on an explicit initial event of probability tending to one, every
member is globally defined in feature time with bounds independent of
its clipping cap. Its prediction is increasing, and its canonical
physical clock has bounded total feature time. No population limit,
uncut removal, or new full-query tail is claimed.

The mechanism is to project the lower backward field using the metric
induced jointly by the first vector and the second matrix. A Euclidean
coordinate clipping need not preserve that energy. We prove the
projection inequality, obtain cap-independent energy and operator
bounds, prevent the first-layer activation from collapsing, and then
continue the finite-dimensional ODE. The same inequalities control
the physical clock.

## 1. Model and the auxiliary modification

For width n, let phi(z)=arctan(z), c=pi/2, and
h^(ell)=phi(z^(ell)) coordinatewise. The forward equations are exact:
z^(2)=W^(2)h^(1), z^(3)=W^(3)h^(2), and
f=(W^(4))^T h^(3)/n. W^(4) is the rescaled output vector.
All finite vector norms below are ordinary Euclidean norms, with
normalizing factors displayed. Matrix norms are operator or Frobenius
norms as specified. All transposes are finite T.

The independent initialization is exactly
z^(1)_(0,i)~N(0,1), W^(2)_(0,ij),W^(3)_(0,ij)~N(0,1/n),
and W^(4)_(0,i)~N(0,n^(-2)).
Define the full, UNCLIPPED backward quantities at every current state:
\[
 \delta^{(3)}=W^{(4)}\odot\phi'(z^{(3)}),\qquad
 q^{(2)}=(W^{(3)})^T\delta^{(3)},\qquad
 \delta^{(2)}=\phi'(z^{(2)})\odot q^{(2)}.
 \tag{1}
\]
No residual is included. Put
\[
 c_1=\|h^{(1)}\|_2^2/n,\qquad
 M=c_1 I_n+
 W^{(2)}\operatorname{diag}(\phi'(z^{(1)})^2)(W^{(2)})^T .
 \tag{2}
\]
Whenever c_1>0 and R>0, let u_R be the unique minimizer
\[
 u_R=\mathop{\rm argmin}_{|u_i|\le R}
       \frac12(u-\delta^{(2)})^T M(u-\delta^{(2)}).
 \tag{3}
\]
Only the lower two parameter updates are changed:
\[
 \begin{aligned}
 (z^{(1)})'&=\phi'(z^{(1)})\odot(W^{(2)})^T u_R,&
 (W^{(2)})'&=u_R(h^{(1)})^T/n,\\
 (W^{(3)})'&=\delta^{(3)}(h^{(2)})^T/n,&
 (W^{(4)})'&=h^{(3)} .
 \end{aligned}                                                   \tag{4}
\]
Primes here denote feature time s, not activation derivatives.
In particular both hidden matrices, their exact forward actions and
the tiny readout are retained. If delta^(2) lies in the box, then
u_R=delta^(2), and (4) is exactly the canonical feature flow. This
pointwise agreement does not prove a limit as R increases.

## 2. Projection and local existence

A positive definite quadratic form is strictly convex and continuous;
the box in (3) is compact and convex. Thus its minimizer exists, is
unique, and satisfies
\[
 (v-u_R)^T M(u_R-\delta^{(2)})\ge0
 \quad\hbox{for every }v\hbox{ in the box}.
 \tag{5}
\]
Indeed the right derivative of the objective on the segment to v is
nonnegative. Conversely, expanding the objective at u_R and using
(5) proves optimality. Taking v=0 gives
\[
 (\delta^{(2)})^T M u_R\ge u_R^T M u_R\ge c_1\|u_R\|_2^2.
 \tag{6}
\]
Cauchy--Schwarz in the positive form M also gives
\[
 (u_R^T M u_R)^{1/2}
 \le ((\delta^{(2)})^T M\delta^{(2)})^{1/2}.              \tag{7}
\]
This remains true when u_R=0, without division.

For completeness, the projection is locally Lipschitz in its finite
matrix and vector arguments on positive definite matrices. If
u=P_M(d), v=P_N(e), and M,N have eigenvalues at least a>0, adding
their inequalities (5) gives
\[
 a\|u-v\|_2
 \le \|M\|_{\rm op}\|d-e\|_2
       +\|M-N\|_{\rm op}\|v-e\|_2.                       \tag{8}
\]
For u=v the assertion is immediate; otherwise divide the corresponding
quadratic inequality by ||u-v||_2. One obtains the latter inequality
by expanding M(u-v) and using
(u-v)^T[M(u-d)-N(v-e)]<=0. On any finite bounded argument set the last
factor in (8) is bounded (also ||v||_2<=R sqrt(n)).
All other maps in (1)--(4) are smooth. The vector field is therefore
locally Lipschitz on the open finite-dimensional set c_1>0.
The ordinary local ODE theorem applies: on a closed small ball inside
this set the vector field is bounded and Lipschitz, its integral map
is a contraction for a sufficiently short time, and iteration gives
a unique maximal solution. A finite endpoint in a compact subset of
this open set permits continuation by the same construction.

No dimension-uniform Lipschitz claim for the COMPOSITION in (3) is
made. In particular (8) does not bound the change of delta^(2) from
a change of its middle gate by an RMS bound on q^(2).

## 3. Exact energy and preliminary uniform bounds

Differentiating f through its full exact forward network and using
(4), including both lower blocks, gives
\[
 \begin{split}
 f'
 &=\frac{(\delta^{(2)})^T M u_R}{n}
   +\frac{\|\delta^{(3)}\|_2^2}{n}
      \frac{\|h^{(2)}\|_2^2}{n}
   +\frac{\|h^{(3)}\|_2^2}{n}\\
 &\ge
 \frac{\|(z^{(1)})'\|_2^2}{n}
 +\|(W^{(2)})'\|_{\rm F}^2
 +\|(W^{(3)})'\|_{\rm F}^2
 +\frac{\|(W^{(4)})'\|_2^2}{n}\ge0 .
 \end{split}                                                     \tag{9}
\]
The first two squared speeds sum exactly to u_R^T M u_R/n.
The third and fourth terms in the first line are exactly the upper
matrix and readout squared speeds. Thus there is no missing learned
term or normalization in (9). The possibly strict excess is
(\delta^(2)-u_R)^T M u_R/n>=0. It is not asserted to vanish as R grows.

Suppose initially
\[
 \|W_0^{(2)}\|_{\rm op},\|W_0^{(3)}\|_{\rm op}\le M_0,\quad
 \|z_0^{(1)}\|_2/\sqrt n\le2,\quad
 \|W_0^{(4)}\|_\infty\le1 .                              \tag{10}
\]
For a fixed S>0, define deterministic constants
\[
 B(S)=1+cS,\quad D(S)=cB(S)+c,\quad
 A_2(S)=M_0+\sqrt{S D(S)},\quad
 A_3(S)=M_0+cB(S)S.                                    \tag{11}
\]
These constants are independent of R,n and of the realized initial
point satisfying (10). On the portion of a solution with s<=S,
bounded activation and (4) imply
\[
 \|W^{(4)}(s)\|_\infty\le B(S),\quad
 \|\delta^{(3)}(s)\|_2/\sqrt n\le B(S),\quad
 \|W^{(3)}(s)\|_{\rm op}\le A_3(S),\quad |f(s)|\le cB(S).
 \tag{12}
\]
Since f(0)>=-c, integrating (9) bounds the integral of each squared
speed, and of their sum, by D(S). Consequently
\[
 \begin{split}
 \|W^{(2)}(s)-W_0^{(2)}\|_{\rm F}&\le\sqrt{sD(S)},\\
 \|z^{(1)}(s)-z_0^{(1)}\|_2/\sqrt n&\le\sqrt{sD(S)},\\
 \|W^{(2)}(s)\|_{\rm op}&\le A_2(S).
 \end{split}                                                     \tag{13}
\]
These estimates hold up to any possible endpoint with c_1>0. They
do not assume a lower bound for c_1 or a bound for u_R in advance.

## 4. Uniform initial interval and noncollapse

Assume in addition, for fixed kappa_1,kappa_3>0, that
\[
 \|h_0^{(1)}\|_2^2/n\ge\kappa_1,\qquad
 \|h_0^{(3)}\|_2^2/n\ge\kappa_3,\qquad
 \|W_0^{(4)}\|_2/\sqrt n\le2/n .
 \tag{14}
\]
Take the constants (11) at S=1. Since phi is 1-Lipschitz,
(12)--(13) and the exact two forward products give, for s<=1,
\[
 \begin{split}
 \|h^{(1)}(s)-h_0^{(1)}\|_2/\sqrt n&\le\sqrt{sD(1)},\\
 \|h^{(2)}(s)-h_0^{(2)}\|_2/\sqrt n
     &\le[A_2(1)+c]\sqrt{sD(1)},\\
 \|h^{(3)}(s)-h_0^{(3)}\|_2/\sqrt n
     &\le A_3(1)[A_2(1)+c]\sqrt{sD(1)}+c^2B(1)s
      \le L\sqrt s ,
 \end{split}                                                     \tag{15}
\]
where L=A_3(1)[A_2(1)+c]sqrt(D(1))+c^2B(1).
Choose once and for all
\[
 a=\min\{1,\kappa_1/[16D(1)],\kappa_3/(16L^2)\}>0,\qquad
 f_*=\kappa_3 a/8 .
 \tag{16}
\]
On [0,a] the first and third activation norms are at least half
their stated initial lower bounds, so c_1>=kappa_1/4 and
||h^(3)||_2^2/n>=kappa_3/4. Bounded parameters and this strict
c_1 bound rule out a maximal endpoint before a. Also
|f(0)|<=2c/n. For n>=16c/(kappa_3 a), (9) implies
\[
 f(a)\ge f_* >0,\qquad f(s)\ge f_*\quad(s\ge a)
 \tag{17}
\]
as long as the solution exists.

For S>=a and a<=s<=S, use phi(0)=0 and its Lipschitz constant:
\[
 f_*\le f(s)
 \le B(S)\|h^{(3)}(s)\|_2/\sqrt n
 \le B(S)A_3(S)A_2(S)\|h^{(1)}(s)\|_2/\sqrt n .
 \tag{18}
\]
Hence throughout [0,S],
\[
 c_1(s)\ge
 b(S):=\min\left\{\kappa_1/4,
     [f_*/(B(S)A_3(S)A_2(S))]^2\right\}>0 .             \tag{19}
\]
For S<a the initial bound suffices. For any proposed finite maximal
endpoint, choose S at least a and larger than that endpoint.
Equations (12)--(13),(19) bound all parameters in a finite-dimensional
compact subset of c_1>0. Local continuation contradicts maximality.
Thus (4) exists uniquely for all feature times, for every R>0.

Equation (7), M>=b(S)I and ||M||op<=c^2+A_2(S)^2 now give
\[
 \|u_R(s)\|_2/\sqrt n
 \le U(S):=
 \sqrt{\frac{c^2+A_2(S)^2}{b(S)}}\,A_3(S)B(S) .
 \tag{20}
\]
The right side is cap independent. In particular all parameter
velocities in their preceding normalized/Frobenius norms are
bounded on finite feature horizons, independently of R and n.
For example ||(z^(1))'||_2/sqrt(n)<=A_2 U and
||(W^(2))'||F<=cU; the upper bounds are cB and c.

These imply cap-independent time-Lipschitz bounds for hidden
preactivations and for the FULL query q^(2), not merely its projection.
Explicitly,
\[
 \begin{split}
 \|(z^{(2)})'\|_2/\sqrt n&\le(c^2+A_2^2)U,\\
 \|(z^{(3)})'\|_2/\sqrt n&\le c^2B+A_3(c^2+A_2^2)U,\\
 \|(q^{(2)})'\|_2/\sqrt n
 &\le cB^2+A_3\{c+2B[c^2B+A_3(c^2+A_2^2)U]\}.
 \end{split}                                                     \tag{21}
\]
Here constants are evaluated at S. The last line differentiates
q^(2)=(W^(3))^T delta^(3) and uses
(delta^(3))'=h^(3) odot phi'(z^(3))
 +W^(4) odot phi''(z^(3)) odot (z^(3))',
with |phi''|<=2. No derivative of the nonsmooth projection is used.

## 5. The canonical physical clock

Put v(s)=||W^(4)(s)||_2^2/n. Exactly v'=2f, and Cauchy--Schwarz
together with (9) gives f'>=||h^(3)||_2^2/n>=f^2/v wherever v>0.
For s>=a, f>0 and therefore v>0. Direct differentiation shows
\[
 (f^2/v)'=\frac{2f}{v}\left(f'-\frac{f^2}{v}\right)\ge0.
 \tag{22}
\]
It follows that
\[
 f'(s)\ge k:=f_*^2/B(1)^2>0\quad(s\ge a).
 \tag{23}
\]
Assume also n>2c, so f(0)<1. Since f is continuous, nondecreasing,
and eventually grows at least linearly, it first reaches 1 at some
s_dagger<=a+1/k=:S_dagger. If this occurs before a the same bound
holds. There is only one first crossing.

The scalar clock sdot=2(1-f(s)), s(0)=0 has a unique solution for
all physical t>=0 and 0<=s(t)<s_dagger, with s(t) increasing to
s_dagger. Indeed f is continuously differentiable and f' is bounded
on [0,S_dagger] by (9), (12), (20) and Cauchy--Schwarz in M.
Before the first root the clock is positive; local uniqueness prevents
hitting that root at a finite time, since the constant root trajectory
is also a solution. The bounded clock state gives continuation. A
limit strictly below the root would have a strictly positive clock
speed, which is impossible.

Along this physical reparametrization,
\[
 \frac{d}{dt}(f-1)^2=-4(f-1)^2 f'(s(t))\le0 .
 \tag{24}
\]
This is the canonical clock applied to the AUXILIARY parameter field,
not an assertion of canonical exact GD or of its discretization.
The total feature time S_dagger is uniform in R,n on the initial event.

## 6. Probability of the initial event

Let G be a standard normal scalar. Define deterministic positive numbers
\[
 v_1=\mathbb E\phi(G)^2,\quad
 v_2=\mathbb E\phi(\sqrt{v_1}G)^2,\quad
 v_3=\mathbb E\phi(\sqrt{v_2}G)^2 .
 \tag{25}
\]
Each is positive because its nondegenerate normal input is nonzero
with probability one, and is finite because |phi|<=c.
Take kappa_1=v_1/2 and kappa_3=v_3/2.

The initial first activation average converges in probability to v_1
by variance of the average of independent bounded variables.
Conditioned on h_0^(1), the rows of W_0^(2) are independent, so the
z_0^(2) coordinates are conditionally independent normals with common
variance ||h_0^(1)||_2^2/n. The conditional variance of the average
of phi(z_0^(2))^2 is at most c^4/n. The function
x->E phi(sqrt(x)G)^2 is continuous on [0,c^2] by bounded convergence.
Thus the second activation average converges in probability to v_2.
Conditioning next on h_0^(2), which is independent of W_0^(3),
gives the identical argument and convergence of the third average to
v_3. This establishes the two lower bounds in (14) with probability
tending to one. It is an initialization calculation, not an assertion
of coordinate independence after any reuse of a matrix.

For the remaining event choose M_0=8. A 1/4-net of each unit sphere
has at most 9^n points; approximation of both vectors in a bilinear
form bounds the operator norm by twice the maximum net bilinear form.
Each such form in W_0^(ell) is N(0,1/n), so
P(||W_0^(ell)||op>8)<=2 exp[-(8-2 log 9)n].
A union bound covers both matrices. The normalized squared norm of
z_0^(1) tends to 1 by its variance 2/n. Writing W_0^(4)=G^(4)/n,
the same argument gives ||W_0^(4)||_2/sqrt(n)<=2/n with probability
tending to one. Finally P(||W_0^(4)||infty>1)<=2n exp(-n^2/2).
No independence among these final events is required for their union
bound. Their intersection, (10),(14), has probability tending to one.
It is the SAME initial event for all R>0, since every subsequent
estimate was deterministic and cap independent.

## 7. Exact scope

This proves cap-independent global finite-width energy, primal,
coercivity and clock bounds for a new canonically initialized auxiliary
family. It also exhibits its nonnegative work excess in (9).

It does not prove dimension-uniform state stability of the projection
rule, convergence at fixed R to a population flow, vanishing projection
work excess, uncut removal, or uniqueness of an uncut population limit.
RMS regularity in (21) is not a coordinate tail estimate. Existing
theorems for coordinatewise clipping of q^(2) cannot silently be
applied to the nonseparable metric projection (3). A counterexample
to an ambient projection stability shortcut would not contradict
the dynamical theorem here or the original canonical global theorem.

No numerical experiment, source-task operation, or repository change
was used. This proof has no dependency on the local complete theorem,
the filtered Gaussian law, or an external distribution theorem.


## 8. Vanishing middle-equation defect against bounded tests

There is a quantitative source estimate in addition to the preceding
primal bounds. Define the vector
\[
 e_R=M(\delta^{(2)}-u_R).
 \tag{26}
\]
Coordinate variations in (5) give
\[
 e_{R,i}=0\ \hbox{if }|u_{R,i}|<R,\qquad
 e_{R,i}\ge0\ \hbox{if }u_{R,i}=R,\qquad
 e_{R,i}\le0\ \hbox{if }u_{R,i}=-R .
 \tag{27}
\]
For example at the upper face one may decrease u_i slightly in (5);
this implies [M(u_R-delta^(2))]_i<=0. At an interior coordinate
both perturbation signs are admissible, so this component is zero.
Consequently the exact work excess in (9) is
\[
 \frac{(\delta^{(2)}-u_R)^T M u_R}{n}
       =\frac{R}{n}\sum_i |e_{R,i}| .
 \tag{28}
\]
Combining (9),(28) and integrating, without discarding any negative
term, proves for every S>0
\[
 \int_0^S\frac1n\sum_i |e_{R,i}(s)|\,ds
       \le \frac{D(S)}R .                               \tag{29}
\]
For S<a one may use D(S) directly in this inequality; no coercivity
constant from (19) is needed for it.

The exact differentiated second forward equation is
\[
 (z^{(2)})'=c_1 u_R+
 W^{(2)}\operatorname{diag}(\phi'(z^{(1)})^2)(W^{(2)})^T u_R
 =M\delta^{(2)}-e_R .                                   \tag{30}
\]
The term M delta^(2) is the canonical second-preactivation velocity
evaluated at the CURRENT auxiliary state. Thus (29) is an actual
small defect for one canonical equation, not an estimate of an oracle
or of an externally supplied path.

For every measurable vector test a(s) with |a_i(s)|<=1, including a
test depending on this trajectory, (29) implies
\[
 \left|\int_0^S\frac1n a(s)^T
              [(z^{(2)})'(s)-M(s)\delta^{(2)}(s)]\,ds\right|
 \le D(S)/R .                                           \tag{31}
\]
No independence hypothesis is involved. In particular, for any C^1
scalar function chi with ||chi'||infty<=1, the chain rule gives
\[
 \left|\frac1n\sum_i[\chi(z_i^{(2)}(S))-\chi(z_i^{(2)}(0))]
  -\int_0^S\frac1n\sum_i
       \chi'(z_i^{(2)}(s))[M(s)\delta^{(2)}(s)]_i\,ds\right|
 \le D(S)/R .                                           \tag{32}
\]
For the physical reparametrization in Section 5, replace the velocity
in (31) by its physical counterpart and M delta^(2) by
2(1-f) M delta^(2). The absolute integrated source on any physical
interval [0,T] is at most D(S_dagger)/R: substitution
ds=2(1-f)dt in (29) is legitimate since the clock is positive there.

For clarity about the weaker topology, (20),(27) imply that the
support of e_R at each time lies in a set of at most
n U(S)^2/R^2 coordinates. But neither that support bound nor (29)
shows ||e_R||_2/sqrt(n) tends to zero. Concentration on a decreasing
set can retain its entire squared norm. The lower-parameter velocity
defects involve delta^(2)-u_R=M^(-1)e_R; an operator-norm bound on
M^(-1) supplies no vanishing L2 bound from (29). The excess work
in (28) can remain order one. Tests with unbounded derivative or
with the unbounded middle query as a weight are not covered.
In particular no hidden-velocity RMS, raw-kernel, prediction-energy
identity, population uniqueness, or uncut path comparison is inferred.


## 9. Eventual exactness at each fixed finite width

There is also a precise finite-width consistency statement. Fix
S>=a. On the same initial event, (12),(19),(20) imply for every R
and every s<=S
\[
 \|\delta^{(2)}(s)\|_\infty
 \le \|\delta^{(2)}(s)\|_2
 \le \sqrt n\,A_3(S)B(S).                               \tag{33}
\]
If R>=sqrt(n) A_3(S)B(S), the entire full backward vector is feasible
in (3) for the entire interval. The strictly convex objective is then
minimized by u_R=delta^(2). Consequently the whole auxiliary path on
[0,S] solves the canonical finite-width feature ODE exactly, with the
same prescribed initialization. Its local uniqueness follows from
the smooth raw canonical vector field, so different such caps give
the same path. This is actual interval consistency, not just
pointwise agreement at a supplied state.

In particular use S=S_dagger from Section 5. Such a cap produces
exactly the canonical finite-width physical flow for every physical
time: its feature clock remains below its first f=1 point in
[0,S_dagger]. Thus at each fixed n the projection family is eventually
identical to the canonical physical flow, not merely formally similar.

The sufficient cap in (33) grows as sqrt(n). Nothing here allows a
width-independent cap, a cap o(log n), or interchange of width and
cap limits. This finite-width consistency does not supply any of the
missing population, full-sequence, tail or restart conclusions.

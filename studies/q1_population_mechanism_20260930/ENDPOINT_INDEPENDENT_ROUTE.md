# An actual fitted endpoint outside the final training-feature span

## Scope and conclusion

This is a prompt-only independent theory route. Its only scientific input was
the supervisor's assignment containing the exact finite-dimensional equations
below. I did not read study artifacts, the paper, maintained scientific book or
code, archived material, other studies, or another route's findings. Process
inputs were the root `AGENTS.md`, `RESEARCH_WORKFLOW.md` (Part 1, with part of the
promotion instructions also displayed), the `solve-math-rigorously` and
`investigate-conjectures` skills, and the latter's research-contract and
adversarial-audit references. No experiments or external scientific retrieval
were performed. The initial metadata check found HEAD
`7fce699a7decf2239dc3eb50486eca661783b535` and no staged paths. This report is the
route's sole output; it does not edit the study README or Git index.

**Conclusion within the supplied model.** There is a nonempty open set of
finite initial pairs `(A_0,W_0)` for which the actual physical-time q1 flow is
global, tends to a finite fitted parameter endpoint, and has a nonzero endpoint
readout component perpendicular to its final training feature. That component
changes the prediction at the unseen query `sqrt(2) e_2`, and therefore on a
nonempty open arc of the input circle. Consequently the event has positive
probability under any nondegenerate joint Gaussian law for the free entries of
`(A_0,W_0)` with full support. This is an existence result, not a useful lower
bound on that probability.

The proof uses one route: positive dynamics, one strongly saturated row, and a
small positive second row. The saturated limiting system motivates an explicit
finite choice `M=10`; finite estimates below certify that choice. The remaining
small parameter is chosen in a nonempty interval guaranteed by a strictly
positive first derivative. This is a complete candidate proof for the supplied
equations, with an author audit only; reconciliation against the full model and
independent checking remain the supervisor's responsibility.

## Model and statement

All vectors have two coordinates. There is one training datum

\[
x_{\rm tr}=\sqrt2 e_1,\qquad y=1.
\]

At any input `x`, set

\[
h(x)=\tanh(Ax/\sqrt2),\qquad
B=W_0+\frac12 vk^T,\qquad
g(x)=\tanh(Bh(x)),\qquad
f(x)=\frac12 w^Tg(x),
\]

where the hyperbolic tangent acts coordinatewise. Write `h,g,f` without an
argument for their training values and set
`d=w odot (1-g^2)`. The supplied physical-time dynamics are

\[
\begin{split}
\dot w&=2(1-f)g,&\dot v&=2(1-f)d,\\
\dot A&=2(1-f)\big[(1-h^2)\odot B^Td\big]e_1^T,\\
\dot k&=|1-f|(h-k)/\tau,&\dot\tau&=|1-f|.
\end{split}
\]

Initialization is `w=v=0`, `k=h(0)`, and `tau=1`. The matrix `W_0` is fixed
throughout the flow. A finite fitted endpoint means convergence of all these
parameters as physical time tends to infinity, with final training value one.

Choose

\[
q=\frac12,\qquad r=\frac14,\qquad
A_0=\begin{pmatrix}
\operatorname{arctanh}q&\operatorname{arctanh}r\\
\operatorname{arctanh}q&\operatorname{arctanh}r
\end{pmatrix},\qquad
W_0=\begin{pmatrix}10&10\\\varepsilon&\varepsilon\end{pmatrix}.
\tag{1}
\]

There exists `epsilon_0>0` such that every sufficiently small
`0<epsilon<epsilon_0` in (1) has the claimed endpoint. Denote its final training
feature by `g_*` and define

\[
w_{\perp,*}=w_*-\frac{w_*^Tg_*}{\|g_*\|^2}g_*.
\]

The two strict conclusions are

\[
w_{\perp,*}\ne0,\qquad
\frac12 w_{\perp,*}^Tg_*(\sqrt2e_2)>0.
\tag{2}
\]

## 1. A finite feature clock gives the physical-time endpoint

As long as `f<1`, introduce

\[
s(t)=2\int_0^t(1-f(u))\,du.
\]

Then `ds/dt=2(1-f)>0`, `tau=1+s/2`, and primes denoting derivatives in `s`
give the exact equations

\[
w'=g,\quad v'=d,\quad
A'=\big[(1-h^2)\odot B^Td\big]e_1^T,\quad
k'=\frac{h-k}{s+2}.
\tag{3}
\]

We may solve the smooth system (3) for all finite `s>=0` as an auxiliary
extension and stop it at its first fitted value. Values after that stopping
point are not being identified with the physical dynamics.

For any fixed finite initialization, (3) has no finite-`s` blowup. Indeed,
componentwise `|w_i(s)|<=s` and `|v_i(s)|<=s^2/2`. Also

\[
k(s)=\frac{2h(0)+\int_0^s h(u)\,du}{s+2},
\tag{4}
\]

so `|k_i|<=1`. Thus `B` grows at most quadratically on finite `s` intervals,
and `A'` has a polynomial bound because `|d_i|<=|w_i|`. The right-hand side is
smooth for `s>=0`, so local existence and uniqueness plus these bounds extend
the solution through every finite `s`. The same bounds on a compact set of
initializations give smooth dependence on the initial entries on any fixed
finite interval. The ODE facts used here are the following elementary
specialization: a continuously differentiable vector field is locally
Lipschitz and has a unique local solution; a solution contained in a bounded
region on a finite interval extends past its endpoint; its solution and
parameter derivatives depend continuously on initial parameters while the
vector field and their derivatives remain bounded there. All three
hypotheses hold here by the bounds just given and `s+2>=2`.

Suppose the entries of `W_0` and of the initial training preactivation
`A_0 e_1` are strictly positive. Nonnegativity is invariant for `w,v,h,k`:
`B` has positive entries, `g>0`, `w'=g>0`, and
`v'=w odot (1-g^2)>=0`. Moreover,

\[
h'=(1-h^2)^2\odot B^Td\ge0.
\]

Equation (4) and monotonicity of `h` imply `h(0)<=k(s)<=h(s)`, hence `k'>=0`.
It follows that `B'=(d k^T+v k'^T)/2>=0`, so `g'>=0`. These statements also
hold for the limiting witness `epsilon=0` below, with its second output row
identically zero. In either case the first training feature is strictly
positive. Consequently

\[
f'(s)=\tfrac12\big(\|g(s)\|^2+w(s)^Tg'(s)\big)
\ge\tfrac12\|g(0)\|^2>0,
\quad
f(s)\ge\tfrac{s}{2}\|g(0)\|^2.
\tag{5}
\]

There is exactly one `s_*>0` at which `f(s_*)=1`, and
`s_*<=2/||g(0)||^2`. All parameters are finite there. To recover physical
time, set

\[
t(s)=\int_0^s\frac{du}{2(1-f(u))},\qquad 0\le s<s_*.
\tag{6}
\]

This function is finite before `s_*`. Since `f'` is continuous on the compact
interval `[0,s_*]`, it has a finite upper bound `C`, and
`1-f(s)<=C(s_*-s)`. Equation (6) therefore diverges to infinity at `s_*`.
Its inverse exists for every finite physical time, and substitution into (3)
recovers exactly the supplied dynamics, including their absolute values since
`f<1`. Thus the physical solution tends to the finite feature-clock endpoint
as `t` tends to infinity. Local uniqueness of the physical vector field
(`tau>0`, and the absolute-value map is Lipschitz) identifies this solution
with the actual initialized flow.

## 2. Exact symmetric reduction

Temporarily replace `10` in (1) by `M>0`. Equal rows of the training
preactivation and equal columns of `W_0` are preserved. Write the scalar
training hidden value as `H(s)` and the common key coordinate as `K(s)`. Set

\[
b_1=M+\tfrac12Kv_1,\qquad
b_2=\varepsilon+\tfrac12Kv_2.
\]

Then `B` has row `i` equal to `(b_i,b_i)`, and (3) reduces exactly to

\[
\begin{split}
g_i&=\tanh(2b_iH),&
w_i'&=g_i,&
v_i'&=w_i\operatorname{sech}^2(2b_iH),\\
H'&=(1-H^2)^2\sum_{i=1}^2 b_iw_i
          \operatorname{sech}^2(2b_iH),&
K'&=(H-K)/(s+2),
\end{split}
\tag{7}
\]

with `H(0)=K(0)=q`. The second column of `A` remains its initialized value,
because `A'` in (3) has only a first column. For nonnegative `epsilon`, all the
positivity and fitting conclusions above apply.

At `epsilon=0`, uniqueness makes
`w_2=v_2=g_2=b_2=0` identically. Subscripts `M` on this base solution will be
suppressed when unambiguous. Let `s_M` be its fitted clock value.

## 3. The small second row leaves a nonparallel readout at fitting

Let

\[
p(s)=\left.\partial_\varepsilon w_2(s)\right|_{\varepsilon=0},\qquad
R(s)=\left.\partial_\varepsilon v_2(s)\right|_{\varepsilon=0}.
\]

These derivatives exist on finite intervals by smooth dependence. Under
`epsilon -> -epsilon`, changing the signs of `w_2,v_2,b_2,g_2` leaves
`H,K,w_1,v_1` unchanged in (7), with the same initial data. Uniqueness therefore
makes the latter variables even in `epsilon`. Differentiating the second-row
equations at zero gives the exact linear variational problem

\[
p'=2H+HKR,\qquad R'=p,\qquad p(0)=R(0)=0,
\tag{8}
\]

and `partial_epsilon g_2|_0=p'`.

Set `D(s,epsilon)=w_1g_2-w_2g_1=det(w,g)`. At zero, `D(s,0)=0` for every `s`.
Because `f'(s_M)>0`, the implicit-function theorem gives a smooth fitted root
`s_*(epsilon)` near zero. The theorem used is precisely that a smooth scalar
equation `F(s,epsilon)=0` with nonzero partial derivative in `s` determines a
unique smooth local root; here `F=f-1`, and (5) verifies its hypothesis.
Thus

\[
\left.\frac{d}{d\varepsilon}
 D(s_*(\varepsilon),\varepsilon)\right|_{\varepsilon=0}
=w_1(s_M)p'(s_M)-p(s_M)g_1(s_M)=:C_M.
\tag{9}
\]

There is no omitted moving-endpoint term: `partial_s D(s,0)=0` identically.
We next prove `C_10>0` using finite bounds.

### A finite saturation estimate

Take `M=10`, `q=1/2`, `0<=s<=3`, and

\[
\delta=\operatorname{sech}^2(10)<10^{-8}.
\]

The stated numerical inequality can, for example, be certified from
`sech^2(10)<4e^{-20}`, `e>2.7`, and `2.7^{20}>4*10^8`; no numerical integration
is involved. Since `H>=1/2`, `K>=1/2`, and `b_1>=10`, one has
`2b_1H>=10`. Equations (7) give

\[
0\le w_1\le s,\quad
0\le v_1\le\tfrac12s^2\delta,\quad
10\le b_1\le10+\tfrac94\delta,
\]

and hence

\[
0\le K-\tfrac12\le H-\tfrac12
\le (10+\tfrac94\delta)\tfrac92\delta
<\eta:=5\cdot10^{-7}.
\tag{10}
\]

Also

\[
0\le1-g_1\le\delta,\qquad
0\le s-w_1\le3\delta.
\tag{11}
\]

The first inequality uses
`1-tanh(10)<=sech^2(10)`. In particular,

\[
2\le s_M\le\frac{2}{\tanh^2(10)}
=\frac{2}{1-\delta}<3.
\tag{12}
\]

The lower bound follows from `f=w_1g_1/2<=s/2`; the upper bound follows
from (5).

If `H=K=1/2` exactly, (8) has the explicit solution

\[
p_0(s)=2\sinh(s/2),\qquad
R_0(s)=4(\cosh(s/2)-1),\qquad
p_0'(s)=\cosh(s/2).
\tag{13}
\]

We use (13) only as a comparison for (8), not as a replacement dynamics.
Write `u=p-p_0` and `z=R-R_0`. Their exact equations are

\[
u'=HKz+a(s),\quad z'=u,\qquad
a(s)=2(H-\tfrac12)+(HK-\tfrac14)R_0.
\]

On `[0,3]`, the elementary bounds `e<3`, `p_0<6`, and `R_0<10` hold. From
(10), `0<=HK-1/4<=3 eta/2`, so `0<=a(s)<=17 eta`. Both `u,z` are nonnegative:
their initial values are zero and their equations cannot cross out of the
nonnegative quadrant. As `HK<=1`, their sum satisfies

\[
(u+z)'\le u+z+17\eta,
\]

and multiplying by `e^{-s}` and integrating proves

\[
0\le u,z\le17\eta(e^s-1)<442\eta,
\qquad 0\le u'\le459\eta.
\tag{14}
\]

Here `e^3<27`. Equations (13)--(14) also imply `p'<4` on `[0,3]`.
For `s=s_M`, (11) and (14) now give

\[
\begin{split}
\big|C_M-[s p_0'(s)-p_0(s)]\big|
&\le |w_1-s|p'+s|p'-p_0'|
       +|p-p_0|g_1+p_0|1-g_1|\\
&\le18\delta+1819\eta<10^{-3}.
\end{split}
\tag{15}
\]

The comparison expression is strictly increasing for `s>0`, since

\[
\frac{d}{ds}\{s\cosh(s/2)-2\sinh(s/2)\}
=\frac{s}{2}\sinh(s/2)>0.
\]

Using `s_M>=2`, its value is at least
`2 cosh(1)-2 sinh(1)=2/e>2/3`. Therefore (15) proves

\[
C_{10}>2/3-10^{-3}>0.66.
\tag{16}
\]

By differentiability at zero, (9) and (16) imply

\[
D(s_*(\varepsilon),\varepsilon)>0
\]

for all sufficiently small positive `epsilon`. This is a statement at the
actual fitted endpoint, not at a short training time. Since `g_*!=0`, a
positive determinant is equivalent to `w_perp,*!=0`, proving the first part
of (2). Notice that the coefficient is certified at finite `M=10`; no
interchange of physical infinite time with a saturation limit is required.

## 4. The perpendicular component is visible at an unseen circle query

At `x_q=sqrt(2)e_2`, the hidden feature remains `(r,r)` with `r=1/4`, because
the second column of `A` is constant. Hence the endpoint training and query
features are

\[
g_*=(\tanh(2b_1H_*),\tanh(2b_2H_*)),\qquad
\widetilde g_*=(\tanh(2b_1r),\tanh(2b_2r)).
\tag{17}
\]

For sufficiently small positive `epsilon`, continuity from zero and positivity
give `0<b_2<b_1`, while `H_*>=1/2>r`. For fixed `0<b_2<b_1`, define

\[
\rho(z)=\frac{\tanh(b_2z)}{\tanh(b_1z)},\qquad z>0.
\]

Its logarithmic derivative is

\[
\frac{\rho'(z)}{\rho(z)}
=\frac{2b_2}{\sinh(2b_2z)}-
 \frac{2b_1}{\sinh(2b_1z)}>0.
\]

To check the last strict inequality, `x/sinh(x)` is strictly decreasing for
positive `x`, since the numerator of its derivative is
`sinh(x)-x cosh(x)<0`; the negative of that numerator vanishes at zero and
has derivative `x sinh(x)>0`. Thus (17) gives

\[
\det(g_*,\widetilde g_*)<0.
\tag{18}
\]

For arbitrary vectors `w,g,z` in two dimensions with `g!=0`, direct expansion
of the orthogonal projection gives

\[
\left(w-\frac{w^Tg}{\|g\|^2}g\right)^Tz
=-\frac{\det(w,g)\det(g,z)}{\|g\|^2}.
\tag{19}
\]

The positive determinant from Section 3 and the negative determinant (18),
substituted into (19), prove the second part of (2). Continuity of the final
network in its input makes the same strict inequality hold on a nonempty
open arc around `sqrt(2)e_2`. In particular, under the uniform probability
measure `mu` on the circle of radius `sqrt(2)`,

\[
\int\left|\tfrac12w_{\perp,*}^Tg_*(x)\right|^2\,d\mu(x)>0.
\]

The same conclusion holds for any circle measure that gives positive mass
to every nonempty open arc. This proves population visibility of the
perpendicular component. It does not by itself compare population risks
against another training method or a target regression function.

## 5. Openness and Gaussian probability

Fix one sufficiently small positive `epsilon` for which all strict conclusions
above hold. Both matrices in (1) have strictly positive entries. In an open
neighborhood of this pair the entries of `W_0` and `A_0 e_1` remain positive.
The argument in Section 1, which did not require the row symmetry, therefore
gives a unique finite fitted clock value and a finite physical-time endpoint
for every initialization in this neighborhood.

On a compact `s` interval extending beyond the witness's fitting value, the
solution depends continuously on `(A_0,W_0)`. Since its fitted crossing is
transverse by (5), the fitted clock value and all endpoint parameters are
continuous functions of those initial entries. The endpoint training feature
stays nonzero. Thus `w_perp,*` and its contribution at the fixed query
`sqrt(2)e_2` are continuous too. The strict inequalities (2) persist on a
smaller nonempty open neighborhood. This step removes the apparent
measure-zero problem caused by using exactly equal rows and columns to derive
the witness.

A nondegenerate Gaussian law on the free finite-dimensional coordinates of
`(A_0,W_0)` has a strictly positive density everywhere. Every nonempty open
neighborhood contains a ball of positive Lebesgue volume on which that density
is positive, so the neighborhood just constructed has strictly positive
probability. This conclusion presumes full support for those free entries;
it does not claim the same for an unspecified degenerate Gaussian law with
support constrained to another subspace. `w_0,v_0,k_0,tau_0` remain initialized
exactly as prescribed, with `k_0=h(A_0,x_tr)` throughout this open set.

## Audit and precise claim boundary

- **Actual dynamics:** The proof uses both learned hidden features and the
  evolving key `K`; neither is frozen in (7) or (8). The frozen values in (13)
  are only a comparison whose finite error is bounded in (10)--(15).
- **All time:** Fitting at a finite `s_*` is explicitly converted to an
  infinite physical-time limit in (6), with all endpoint parameters bounded.
- **Endpoint cancellation:** Equation (9) differentiates the determinant at
  the fitted root. Its positive derivative is certified by (16), rather than
  inferred from a transient Taylor coefficient.
- **Final span:** The projection in (2) uses the actual final training feature,
  not the initial feature or a feature from a comparison system.
- **Visibility:** The fixed unseen query and the open-arc argument concern the
  actual endpoint network. No target-dependent choice of query is needed.
- **Positive-probability bridge:** The symmetric construction is only the
  center of an open set; the Gaussian conclusion is not assigned to the
  symmetric, measure-zero family itself.
- **Scope limits:** The result is a finite-width, one-training-point existence
  statement for the equations supplied in the assignment. It does not establish
  a large-width limit, a generic lower probability bound, a comparison of
  population risks, or equivalence to equations not supplied to this route.
  Full-model reconciliation and independent proof review have not been done by
  this scoped author.

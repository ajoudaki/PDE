# Internal check of the fitted endpoint history theorem

Checker: scoped subagent `/root/endpoint_check`, 2026-09-30.
Status: **PASS for the exact finite-dimensional system stated in equation (1).**
No substantive mathematical correction is required. This is an internal
adversarial check, not a promotion review or a verification against the external
manuscript. The single optional exposition improvement is recorded below.

## Input scope, versions and complete read coverage

The supervisor assigned a bounded check of the complete candidate, with its
physical equations taken as the scientific starting point. The assigned attacks
were constants, feature-time reconstruction, positivity and global existence,
the endpoint determinant, query visibility, classifier disagreement, endpoint
continuity on an open neighborhood, and positive Gaussian probability. No
experiments were requested; scalar arithmetic was permitted. The candidate and
README remained the supervisor's files. This report is the only file I wrote.

I read all 364 lines of `ENDPOINT_HISTORY_SELECTION.md`, including its theorem,
equations (1)--(20), every proof paragraph, limitations and source declaration.
Its SHA-256 is

```text
808d4af77af6fb7e14938cd976a26dcf4f2b92ca6784e460cb0f5d9a866df7e6
```

Required process inputs were read completely:

| Input | SHA-256 |
| --- | --- |
| `AGENTS.md` | `3a0b50283fc25b700fbe5c38bbacc38428490a0dad4f0ccce170dcc16179e75f` |
| `RESEARCH_WORKFLOW.md` | `459143719de664d1d6669c615b499d5b2f2505c5d7bad0c22dd7657e9ac41dd1` |
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |

The initial batched display truncated process-file output; subsequent separate
reads supplied the complete skill and workflow. The candidate was displayed
completely. I did not read the paper, established book, other notes in this study,
other studies, history, another reviewer's findings, or external scientific
sources. Scientific conclusions below are therefore about the equations
actually supplied, not independent certification of their manuscript mapping.
No missing scientific input is needed to check that conditional mathematical
claim.

Before editing, metadata-only checks found HEAD
`7fce699a7decf2239dc3eb50486eca661783b535`, an empty staged index, and untracked
study directories. Their contents were not inspected. No staging, commit,
checkout, worktree, or shared-file edit was performed.

## 1. Clock conversion and existence: pass

With residual `e=1-f>0`, the stated physical equations give
`ds/dt=2e` and `d tau/ds=1/2`. The initialized clock is consequently
`tau=1+s/2`. Dividing each physical derivative by `2e` gives exactly

\[
w'=g,\quad v'=d,\quad a'=(1-h^2)\odot B^Td,
\qquad k'=\frac{h-k}{2+s}.
\]

In particular, the key denominator is `2+s`, not `1+s`; the factors 2 and
the rank-one reconstruction `B=W_0+vk^T/2` are retained. The auxiliary
continuation beyond its fitting crossing does not purport to satisfy the
physical equations with positive residual there.

For the general-`n` auxiliary lemma, the claimed region is invariant.
At a face `w_i=0`, `w_i'=g_i>=0`; at `v_i=0`,
`v_i'=w_i(1-g_i^2)>=0`. Nonnegative `W_0,v,k` give nonnegative `B`, so
`a'>=0` and `h'>=0`. At `h_i=k_i`, the derivative of their difference is
`h_i'>=0`; at `k_i=h_i(0)`, the key derivative is nonnegative.
The integrating-factor identity is also exact:

\[
((2+s)k)'=h,\qquad
k(s)=\frac{2h(0)+\int_0^s h(u)\,du}{2+s}.
\]

Thus `h,k,w,v` are nondecreasing, and so are `B`, `Bh` and `g`.
The hypotheses allow the diagonal witness, including its zero off-diagonal
entries: its initial `a` and its initial two coordinates of `g` are strictly
positive.

The bounds in (7) do not hide any uncontrolled matrix coordinate. Namely,
`w_i<=s`, `d_i<=s` and `v_i<=s^2/2`; hence

\[
a_i'
\le s\sum_j(W_0)_{ji}
 +\frac{k_i}{n}\sum_jv_jd_j
\le s\sum_j(W_0)_{ji}+\frac{s^3}{2}.
\]

On each bounded feature-time interval this bounds every `a_i`, while
`0<k_i<=h_i<1`. The auxiliary vector field is smooth on `s>-2` and all
finite-dimensional state coordinates stay bounded on each such forward
interval. Local ODE existence and uniqueness therefore continue the solution
to all finite `s>=0`; no finite escape remains possible.

Because `g` is positive and nondecreasing and `w>=0`,

\[
F'=\frac{\|g\|^2+w^Tg'}{n}\ge c_0>0.
\]

Also `F(0)=0` and `F<=s`, since each `w_i<=s` and `g_i<=1`.
Integrating the derivative bound gives `F>=c_0s`. The unique fitting crossing
therefore lies in `[1,1/c_0]` and is transverse.

The scalar physical reconstruction cannot reach the crossing in finite time.
For example, smoothness on the compact feature-time segment gives a finite
upper bound `M` for `F'`; along the reconstructed solution,

\[
\dot e=-2F'e,\qquad
e(t)=\exp\!\left(-2\int_0^t F'(s(u))\,du\right)
\ge e^{-2Mt}>0
\]

for every finite `t`. Its increasing feature time tends to the crossing,
because any smaller limiting feature time would leave `ds/dt` bounded away
from zero. The lower derivative bound gives the claimed squared-residual
estimate `L(t)=e(t)^2<=exp(-4c_0t)`.

All physical states, including `tau`, converge to finite endpoint values.
The physical vector field is locally Lipschitz when `tau>0` (absolute residual
is locally Lipschitz), and this trajectory has `tau>=1`. Thus the reconstruction
is the unique initialized physical trajectory, not only a formal reparametrized
curve. The mathematical general-`n` lemma is used here only for the specified
`n=2` physical system.

## 2. Strict endpoint determinant and constants: pass

I checked (10)--(13) directly at the finite initialized trajectory. The
determinant is exactly the integral of past features against the final feature.
Since `0<g_1<=1`, `g_{2,*}<=1` and `g_2(u)>=1-epsilon`, its integrand is at most

\[
g_1(u)-(1-\varepsilon)g_{1,*}
\le -(g_{1,*}-g_1(u))+\varepsilon.
\]

This justifies (11), including the sign of the small positive correction.

For `s<=1`, the first column of `W_0` has sum 1, so integrating (7) yields
`a_1<=1/2+s^2/2+s^4/8<=9/8`. Also `k^Th/2<=1` and `v_1<=s^2/2`, giving
`z_1=h_1+v_1k^Th/2<=3/2`. Differentiating the first reconstructed preactivation
retains only nonnegative terms, hence `z_1'>=h_1'`. More specifically,

\[
h_1'=(1-h_1^2)^2
\left(d_1+\frac{k_1v^Td}{2}\right)
\ge(1-h_1^2)^2w_1(1-g_1^2).
\]

Multiplication by the outer derivative `1-g_1^2`, together with
`w_1>=s gamma`, produces exactly the two squared derivative factors in (12):

\[
g_1'\ge s\gamma(1-h_1^2)^2(1-g_1^2)^2
\ge s\gamma\operatorname{sech}^4(9/8)
               \operatorname{sech}^4(3/2)=Cs.
\]

The needed interval `[0,1]` is contained in `[0,s_*]`. Interchanging the
integrals in the continuous nonnegative function gives

\[
\int_0^{s_*}\int_u^{s_*}g_1'(v)\,dv\,du
=\int_0^{s_*}v g_1'(v)\,dv\ge C/3.
\]

Every coarse constant in (14) can be established by elementary strict
inequalities. For completeness, the exponential series gives

\[
e>\sum_{j=0}^4\frac1{j!}=\frac{65}{24}>\frac83,
\qquad
e<\frac{65}{24}+\frac1{120}\sum_{j=0}^{\infty}6^{-j}
=\frac{65}{24}+\frac1{100}<\frac{11}{4}.
\]

The first bound gives `tanh(1/2)>2/5`, `tanh 1>3/4`, and
`e^15>(8/3)^15>2,000,000`. Since
`exp(4/5)>1+4/5+(4/5)^2/2>2`, one obtains `gamma>1/3`.
For `0<u<1`, comparison of the exponential and geometric series gives
`exp(u)<1/(1-u)`. Thus

\[
\cosh(9/8)<\cosh(6/5)
<\frac{55/16+1/2}{2}=\frac{63}{32}<2,
\]

where `exp(-6/5)<1/2` follows already from `exp(6/5)>1+6/5>2`.
The inequality `sqrt(e)<5/3` and `exp(-3/2)<1` also give
`cosh(3/2)<(55/12+1)/2=67/24<3`. Hence

\[
C>\frac1{3\cdot16\cdot81}=\frac1{3888}.
\]

Writing `z=10 tanh 1>15/2`, the exact formulas

\[
1-\tanh z=\frac{2e^{-2z}}{1+e^{-2z}},\qquad
\operatorname{sech}^2z=\frac{4e^{-2z}}{(1+e^{-2z})^2}
\]

give `epsilon<10^(-6)` and `delta<2*10^(-6)`. Also
`eta>tanh 1>3/4`, so `s_*<=2/eta^2<32/9<4`.
The certified determinant margin is therefore

\[
D<-\frac1{11664}+\frac4{10^6}
=-\frac{931}{11390625}<0.
\]

This is a strict finite-parameter estimate. It does not set the second
neuron's derivative to zero, invoke a saturation limit, or infer an endpoint
claim from a short-time expansion. Formula (16) is the correct signed
two-dimensional orthogonal projection: its coefficient is
`w_* dot (g_{2,*},-g_{1,*})=D`.

## 3. Query visibility and classifier disagreement: pass

At the specified query, `h(x_q)=(tanh 1,0)`. The reconstruction of `B` gives
the exact first query preactivation `(1+v_1k_1/2)tanh 1` and second query
preactivation `v_2k_1 tanh 1/2`. Consequently the two bounds in (17) hold.
For its strict first bound, `tanh 1>3/4` and
`exp(3/2)>1+3/2+(3/2)^2/2>3` imply
`tanh(tanh 1)>tanh(3/4)>1/2`.

The training second preactivation is always at least `10 tanh 1`.
Thus `v_2'<=s delta`, `v_{2,*}<8delta`, and
`g_2(x_q)<=v_{2,*}/2<4delta<8*10^(-6)`.
Together with `g_{2,*}>3/4` and `g_{1,*}<1`, this proves

\[
g_1(x_q)g_{2,*}-g_2(x_q)g_{1,*}
>\frac38-\frac8{10^6}=\frac{23437}{62500}>0.
\]

The projection coefficient `D` is negative, so the extra query prediction is
strictly negative with the sign claimed in (4). Its denominator is positive.

Since fitting gives `g_*^Tw_*=2`, the Euclidean orthogonal projection onto
`span(g_*)` is `2g_*/||g_*||^2`, the unique minimum-norm solution of the
single linear interpolation constraint. This verifies (19) with both readouts
evaluated using the same endpoint feature map. No comparison between features
trained by different trajectories is being made.

The determinant calculations in (20) are exact: `beta=(1,0)` is fixed, so
`det A_*=-a_{2,*}<0`; the mixed rank-one terms cancel in `det B_*`, leaving
`10+5v_{1,*}k_{1,*}+v_{2,*}k_{2,*}/2>0`.
For the implied two-layer feature map

\[
g_*(x)=\tanh\!\left(B_*\tanh(A_*x/\sqrt2)\right),
\]

invertibility of both matrices and the fact that scalar tanh vanishes only
at zero prove `g_*(x)!=0` whenever `x!=0`.

The actual and minimum-norm readouts are nonparallel because `D!=0`.
Their null lines intersect only at zero, so their scalar circle functions
cannot have a common zero. Both functions are real analytic and odd in the
input. The actual function is 1 at the training input and -1 at its antipode.
It is therefore not identically zero. The elementary real-analytic zero
property applies on local circle charts: if a nonzero analytic function had
an accumulating sequence of zeros, its Taylor expansion at an accumulation
point could not have a first nonzero coefficient, forcing local and then
connected-circle identically zero behavior. Thus its zeros are isolated and,
by compactness of the circle, finite.

Along a circle path between the training input and its antipode, opposite
endpoint signs and finitely many zeros force at least one sign-changing zero.
At that zero the minimum-norm function is nonzero and has fixed sign on a
neighborhood. On one side the actual function has the opposite sign. The
resulting open arc has positive uniform-circle measure, independent of how a
classifier assigns labels at exact zeros. This proves disagreement, not
improvement under an unspecified truth or test distribution.

## 4. Open neighborhood and Gaussian probability: pass

This is the critical extension beyond the boundary of the nonnegative-matrix
cone. A direct appeal to physical finite-time continuity would be insufficient;
the supplied finite feature-time argument avoids that mistake.

Choose any finite `S>s_*`. The reference auxiliary solution exists through
`S`, has `F(S)>1` and `F'>=c_0` throughout `[0,S]`. On a compact tube around
its graph, the smooth vector field and its state and parameter derivatives
are bounded. Its initial state also varies smoothly with the eight entries
`p=(A_0,W_0)`, including `k(0)=tanh a(0)` and the constant query column beta.
Subtracting integral equations and using the derivative bound gives, up to
first tube exit, the stated Gronwall bound with a constant depending on the
chosen tube and `S`. A sufficiently small parameter ball makes that bound
smaller than the tube radius and excludes a first exit. It also supplies
existence throughout `[0,S]`.

The formula for `F'` is a smooth function of the state, parameters and time;
therefore uniform state continuity controls both `F` and `F'`. The perturbed
paths satisfy `F'>=c_0/2`, `F(0)=0` and `F(S)>1` after shrinking the ball.
Each has a unique first crossing in `(0,S)`. The mean-value inequality yields
the stated crossing displacement bound `2 epsilon/c_0` for a uniform
perturbation `epsilon` in `F`. Composing these crossings with continuous
finite-time states proves endpoint continuity. No infinite-time continuity
theorem is assumed.

For every parameter in this ball, the physical clock reconstruction uses only
the segment below its crossing. Its residual is positive at finite physical
times and tends to zero; boundedness of `F'` excludes finite-time arrival,
and the positive lower slope gives
`L(t)<=exp(-2c_0 t)` in terms of the reference `c_0`. Endpoint states and
`tau` are finite. This argument remains valid when perturbed `W_0` has
negative entries and coordinatewise cooperation no longer applies.

The determinant `D`, the query bracket, and both matrix determinants are
continuous functions of these endpoint states and initialization. Their
strict witness signs persist on a smaller ball. The nonzero feature argument,
nonparallel readouts, oddness and analytic classification proof consequently
apply there as well; the nearby beta column need not equal `(1,0)`.

The joint independent Gaussian law on the eight entries has a continuous,
strictly positive density everywhere. The neighborhood contains a closed
ball of positive radius; on that compact ball the density has a positive
minimum. Its probability is therefore positive. This proves the stated
existence of positive probability without quantifying it or asserting
typicality. If one additionally wants strictly positive off-diagonal entries,
one can move the center slightly into that quadrant and take a still smaller
ball contained in the already proved neighborhood. A ball centered exactly
at the original zero off-diagonal entries would not have that property, but
the candidate does not require that center to remain fixed.

## 5. Executed arithmetic verification and limitations

In `/home/amir/Codes/PDE`, I executed the following scalar-only command,
which exited with status 0. The rational assertions are exact; the printed
floating values are supplementary sanity checks, not proof premises. No ODE
integration or training experiment was performed.

```sh
python - <<'PY'
from fractions import Fraction
from math import tanh,cosh,exp
from pathlib import Path
p=Path('studies/q1_population_mechanism_20260930/ENDPOINT_HISTORY_SELECTION.md')
print('candidate_lines',len(p.read_text().splitlines()))
lo=Fraction(65,24)
hi=lo+Fraction(1,100)
assert lo>Fraction(8,3)
assert hi<Fraction(11,4)
assert Fraction(8,3)**15>2_000_000
assert Fraction(63,32)<2
assert Fraction(67,24)<3
margin=-Fraction(1,11664)+Fraction(4,1_000_000)
assert margin<0
assert Fraction(3,8)-Fraction(8,1_000_000)>0
print('rational_exp15_lower',Fraction(8,3)**15)
print('strict_D_upper',margin,float(margin))
print('strict_query_bracket_lower',Fraction(3,8)-Fraction(8,1_000_000))
gamma=tanh(tanh(.5)); eta=tanh(10*tanh(1)); delta=1/cosh(10*tanh(1))**2
C=gamma/cosh(9/8)**4/cosh(3/2)**4
print('gamma',gamma,'eta',eta,'epsilon',1-eta,'delta',delta)
print('C',C,'C_lower',1/3888,'sstar_upper',2/(gamma**2+eta**2))
print('scalar_checks','PASS')
PY
```

Observed output:

```text
candidate_lines 364
rational_exp15_lower 35184372088832/14348907
strict_D_upper -931/11390625 -8.173388203017833e-05
strict_query_bracket_lower 23437/62500
gamma 0.4318081805950961 eta 0.9999995148152939 epsilon 4.851847060782788e-07 delta 9.703691768362962e-07
C 0.0016786388652200368 C_lower 0.000257201646090535 sstar_upper 1.6856906202285216
scalar_checks PASS
```

**Required corrections or unresolved mathematical objections: none** for
the supplied physical system and claimed finite-width theorem.

**Optional exposition improvement:** explicitly write the arbitrary-input
feature formula `g_s(x)=tanh(B_s tanh(A_s x/sqrt(2)))` before the classifier
argument. It is already implied by the architecture and the training/query
specializations, so this is not a missing dynamical hypothesis or a condition
of this pass.

**Scope limits:** this check does not verify the mapping from the manuscript
to (1), manuscript/book compatibility, a multiple-training-direction theorem,
a quantitative Gaussian probability, typical-width behavior, test-risk
improvement, or a causal claim that memory alone is necessary. The candidate
properly refrains from those stronger conclusions. Its reference to a prior
transient result and its source-history statements were read but not
independently certified; none is a premise of the endpoint proof checked here.

The strict endpoint result and its open-set robustness pass without any
activation limit, frozen neuron, formal Taylor trajectory, empirical premise,
or unverified specialized theorem dependency. Promotion status is unchanged.

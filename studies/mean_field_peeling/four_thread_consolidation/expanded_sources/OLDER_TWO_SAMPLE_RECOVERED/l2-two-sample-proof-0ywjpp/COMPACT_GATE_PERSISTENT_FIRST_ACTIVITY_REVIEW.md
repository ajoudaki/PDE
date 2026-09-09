# Independent adversarial audit: persistent first-gate activity

Audit date: 2026-09-06.

Source: `/tmp/l2-two-sample-proof-0ywjpp/COMPACT_GATE_PERSISTENT_FIRST_ACTIVITY.md`.

Scope: the entire source, lines 1–594, 24,818 bytes. This was a fresh,
isolated analytic audit. Only the specified source was read as audit
input. Its dependencies, project files, history, previous reviews, and
external sources were not inspected. No experiments, simulations,
subagents, external imports, or source edits were used. The source's
provenance descriptions were read as text, not followed as references.
This review was written using `apply_patch`.

Source SHA256 before reading:

```text
8cf3fb3270f1f4b81b068f7ed749bf1cea90a3b5a122e1d6b5b36502d4af916c
```

Source SHA256 after the full analytic audit:

```text
8cf3fb3270f1f4b81b068f7ed749bf1cea90a3b5a122e1d6b5b36502d4af916c
```

The hashes agree. Source line references below refer to this version.

## 1. Verdict and complete coverage

**Verdict: the stated finite-width, finite-horizon, separate-sample
first-gate lower bound passes this audit. No required mathematical fix
was identified.** The document supplies the estimates needed for its
proof without requiring the three notes listed in its provenance section.

The certified scope is the explicitly displayed model, its stated
Gaussian initialization, actual finite gradient flow, and exact
simultaneous raw GD with step size `eta=n^-2` and linear raw-parameter
interpolation. The result is conditional on `A_n(rho)`, with the stated
probability estimate. GD also requires the sufficient width conditions.

This verdict does not establish nonzero motion, nonlazy behavior, a
reverse-field-weighted kernel lower bound, a mean-field limit, or a
comparison between GF and GD. It does not audit the provenance notes or
verify historical claims about what their author read or proved.

| Source coverage | Independent check | Assessment |
| --- | --- | --- |
| Section 1, lines 13–60 | Activation assumptions, Gaussian variances, forward normalization, loss factor, raw metric and simultaneous clock | Internally consistent |
| Section 1, lines 62–133 | Separate strips, antiparallel center set, event, theorem quantifiers, exceptional realizations | Correct within the stated scope |
| Section 2, lines 141–181 | Finite GF existence, dissipation, readout and second-layer bounds | Closes without a limiting argument |
| Section 2, lines 183–234 | Candidate-exit endpoint bounds, segment derivatives, raw Hessian, actual GD descent | No first-exit circularity found |
| Section 3, lines 238–323 | GF variation, exact GD differences, empirical row envelope and maximum-row step bound | No independence assumption needed |
| Section 4, lines 327–362 | Scalar distance estimates, sign changes, nondifferentiability at zero, full GD cells | Correct |
| Section 5, lines 366–426 | Physical pair equations, conditional invariant, joint first exit and cell induction for either ordered pair | Correct separately for each sample |
| Section 6, lines 430–448 | Singular antiparallel identity and effective-control factor | Correct without inverting the Gram matrix |
| Section 7, lines 452–535 | Gaussian occupancy, both norm tails, deterministic removal, fixed retained subsets, final lower bound | Correct |
| Section 8, lines 539–594 | Limits of the conclusion and use of provenance | Scope limitations are appropriate; provenance itself is not independently verified |

The derivations below explain the checks, including the potentially
fragile factors of `n`, first-exit logic, and angle dependence.

## 2. Model normalization and exact gradient structure

Write `W_1,W_2,W_3` for the three displayed raw parameter blocks. The
source defines

```text
f_a = W_3^T phi_2(W_2 phi_1(W_1 x_a)) / n,
L = sum_a r_a^2,       c_a = -2 r_a.
```

For this exact forward map the ordinary Euclidean derivatives are

```text
partial_(W_1) f_a = delta_a^(1) x_a^T / n,
partial_(W_2) f_a = delta_a^(2) (h_a^(1))^T / n,
partial_(W_3) f_a = h_a^(2) / n.
```

In particular, the source's reverse fields omit the output factor `1/n`
by definition; that factor appears in the derivatives above. Because
`2r_a=-c_a`, the negative Euclidean loss gradient has these three
expressions multiplied by `c_a` and summed over samples.

The metric in lines 156–159 has block multipliers `d/n,1,1/n`.
Applying its inverse to the Euclidean loss gradient multiplies the three
blocks by `n/d,1,n`. Therefore

```text
-grad_raw L = (
    (1/d) sum_a c_a delta_a^(1) x_a^T,
    (1/n) sum_a c_a delta_a^(2) (h_a^(1))^T,
           sum_a c_a h_a^(2)
).
```

These are exactly the source's GF velocities and its simultaneous GD
increments divided by `eta`. There is no missing sample-average factor,
readout factor, or factor of two. The clock is `t_k=k eta`.

The initialization is also used consistently as a variance convention:
`W_3,i(0)` has variance `n^-2`, hence standard deviation `n^-1`.
For clarity, if the effective output coefficient is denoted by
`w_out=W_3/n`, the displayed model has

```text
f_a = w_out^T h_a^(2),
Var(w_out,i(0)) = n^-4.
```

In these alternative coordinates the metric's last block is
`n ||V_out||^2`, and the Euclidean block learning-rate multipliers are
`n/d,1,1/n`. This is simply the dictionary induced by the source's
definitions. Conditional on the initial hidden layers,

```text
Var(f_a(0) | W_1(0),W_2(0))
    = n^-4 sum_i h_a,i^(2)(0)^2
    <= B_2^2 n^-3.
```

Thus the displayed readout normalization must be preserved literally.
An agreement with some different, unstated convention for a
"canonical" network cannot be certified in this isolated audit. The
explicit normalization here is fully defined and internally consistent.

The activation assumptions suffice: smooth compact support makes `p`
and `p'` bounded, continuity gives `p(+-R)=0`, and
`phi_1'=p`, `phi_1''=p'`. Evenness of `p` makes `phi_1` odd. The stated
`arctan` bounds are valid; in particular
`|phi_2''(z)|=2|z|/(1+z^2)^2<=2`. No later estimate requires monotonicity
of `p` on either half of its support.

## 3. Actual finite GF and the primal bounds

For fixed positive integer dimensions the raw metric is a fixed positive
definite metric. Its gradient flow satisfies

```text
dL/dt = -||grad_raw L||_raw^2,
integral_0^t ||dot W(s)||_raw^2 ds <= L(0).
```

The vector field is smooth and locally Lipschitz. To see the continuation
argument explicitly, suppose a maximal solution had finite endpoint
`tau`. For every `t<tau`, Cauchy–Schwarz gives

```text
||W(t)-W(0)||_raw <= sqrt(t L(0)) <= sqrt(tau L(0)).
```

This is a compact ball in the finite-dimensional parameter space. The
vector field is bounded on it, so `W(t)` is uniformly Lipschitz near
`tau` and has a limit there. Local existence from that limit extends
the trajectory, contradicting maximality. If `L(0)=0`, the same energy
identity gives zero speed. This establishes global finite-width GF
without an initialization tail bound on `W_1`.

On `E_n`, bounded activations imply `|f_a(0)|<=B_2`; consequently
`||r(0)||<=R_0=sqrt(2)(B_2+1)`. Set, as in the source,

```text
H = T+1,             R_* = R_0+1,
K = 2sqrt(2)R_*,     W_* = 1+B_2 K H,
A = 8+H K P_2 W_* B_1,
Q = A P_2 W_*.
```

Dissipation gives `||r(t)||<=R_0<R_*`, hence

```text
sum_a |c_a| = 2 ||r||_1 <= 2sqrt(2)||r|| <= K.
```

For `t<=H`, integration of the readout equation gives
`||W_3(t)||_infinity<=1+t K B_2<=W_*`. With the normalized vector norm
`||v||_n=||v||/sqrt(n)`, it follows that
`||delta_a^(2)||_n<=P_2 W_*`. Each rank-one term in the second-layer
velocity satisfies

```text
||(1/n) delta_a^(2) (h_a^(1))^T||_op
    = ||delta_a^(2)||_n ||h_a^(1)||_n
    <= P_2 W_* B_1.
```

Integration gives `||W_2(t)||_op<=A` and therefore
`||q_a(t)||_n<=A P_2 W_*=Q`. These reproduce every bound in (11), with
constants independent of width, input dimension, and angle.

## 4. Simultaneous GD: candidate exit, derivatives, and descent

### 4.1 The candidate exit is included in the endpoint estimates

Let `N=max(1,ceil(T/eta))`. For `eta=n^-2<=1`, `N eta<=T+1=H`.
Suppose `j<=N` is the first node with `||r_j||>R_*`. All old nodes
`k<j` have `sum_a |c_(k,a)|<=K`. Summing their readout increments bounds
`W_3` through node `j` by `W_*`. The second-layer increments require
only old readout bounds and bounded activations, so their sum bounds
`W_2` through node `j` by `A` as well.

Thus neither endpoint bound assumes that the candidate node itself has
small residual. Norm convexity gives the same bounds on each raw segment
up to that node. Recomputed hidden fields on those segments satisfy the
reverse RMS bounds because the activation derivatives are globally
bounded. This supplies the segment estimates before descent is invoked.

### 4.2 First and second differentials in the correct metric

For a raw unit tangent `V`, define

```text
alpha_1 = sqrt(d/n)||V_1||_F,
alpha_2 = ||V_2||_F,
alpha_3 = ||V_3||/sqrt(n).
```

Their squares sum to one. Input normalization gives
`||V_1 x_a||_n<=alpha_1`, and differentiation of the hidden fields gives

```text
||D_V z_a^(2)||_n
    <= B_1 alpha_2 + A P_1 alpha_1 <= J,
J = B_1 + A P_1,
|D_V f_a| <= B_2 alpha_3 + W_* P_2 J <= F,
F = B_2 + W_* P_2 J.
```

For two raw unit tangents `U,V`, the complete second differential is

```text
D_U D_V z_a^(2)
    = V_2 [p(z_a^(1)) U_1 x_a]
      + U_2 [p(z_a^(1)) V_1 x_a]
      + W_2 [p'(z_a^(1)) (U_1 x_a)(V_1 x_a)].
```

For arbitrary vectors `u,v`,

```text
||uv||_n <= ||u||_infinity ||v||_n
          <= sqrt(n) ||u||_n ||v||_n.
```

Therefore the first two terms have RMS norm at most `P_1` each,
and the third at most `A L_1 sqrt(n)`. The complete output differential is

```text
D_U D_V f_a
 = (1/n) [
     V_3^T (phi_2'(z_a^(2)) D_U z_a^(2))
   + U_3^T (phi_2'(z_a^(2)) D_V z_a^(2))
   + W_3^T (phi_2''(z_a^(2))
             (D_U z_a^(2))(D_V z_a^(2)))
   + W_3^T (phi_2'(z_a^(2)) D_U D_V z_a^(2))
   ].
```

The readout cross terms contribute at most `2P_2 J`. For the top
curvature term, the coordinatewise bound on `W_3` gives

```text
(1/n) sum_i |W_3,i| L_2 |D_U z_a,i^(2)| |D_V z_a,i^(2)|
    <= W_* L_2 ||D_U z_a^(2)||_n ||D_V z_a^(2)||_n
    <= W_* L_2 J^2.
```

This term has no additional `sqrt(n)` loss. The final pairing is bounded
by `W_* P_2(2P_1+A L_1 sqrt(n))`. The source's resulting expression

```text
F_2(n) = 2P_2 J + W_* L_2 J^2
                   + W_* P_2(2P_1+A L_1 sqrt(n))
```

is therefore valid for all pairs of raw unit tangents. This check also
shows why only the displayed `sqrt(n)` growth enters the Hessian bound.

### 4.3 Residual control on the segment and the contradiction

At an old node, `g_k=grad_raw L_k` obeys
`||g_k||_raw<=sum_a |c_(k,a)| F<=K F`. The raw segment has length at
most `eta K F`, so the vector of its two predictions changes by norm at
most `sqrt(2) eta K F^2`. Thus throughout the segment

```text
||r|| <= R_* + sqrt(2) eta K F^2 <= R_*+1
```

under the first condition in (12). The raw Hessian then satisfies

```text
|D_U D_V L|
 <= 2 sum_a |D_U f_a| |D_V f_a|
       + 2 sum_a |r_a| |D_U D_V f_a|
 <= 4F^2 + 2sqrt(2)(R_*+1) F_2(n)
 = H_2(n).
```

Taylor's formula on the actual raw segment gives

```text
L(W_k-eta g_k)
 <= L_k - eta ||g_k||_raw^2
              + (eta^2 H_2(n)/2)||g_k||_raw^2
 <= L_k - (eta/2)||g_k||_raw^2
```

when `eta H_2(n)<=1`. Applying this through node `j` gives
`L_j<=L_0<=R_0^2`, contradicting `L_j>R_*^2`. After this rules out an
exit, the same argument applies to every segment through `N`.

This proves descent for the actual simultaneous iterates. It uses the
first-order step in the raw parameters and all mixed differential
terms in the predictions. It neither assumes that GD follows GF nor
requires the interpolated loss to be monotone. Segment residuals only
need the larger bound `R_*+1`.

## 5. Variation of the actual row controls

### 5.1 GF bounds

Multiplication of the first raw velocity by `x_a` gives

```text
dot z_a^(1) = sum_b C_ab c_b p(z_b^(1)) q_b.
```

Since `|C_ab|<=1`,

```text
||dot z_a^(1)||_n <= K P_1 Q,
||dot h_a^(1)||_n <= K P_1^2 Q.
```

The following are precisely the source's constants:

```text
D_A = K P_2 W_* B_1,
D_w = K B_2,
D_Z = D_A B_1 + A K P_1^2 Q,
D_delta = D_w P_2 + W_* L_2 D_Z,
Q_1 = D_A P_2 W_* + A D_delta,
D_c = 4K F^2.
```

The product rule now gives, in order,

```text
||dot W_2||_op <= D_A,       ||dot W_3||_infinity <= D_w,
||dot z_a^(2)||_n
    <= ||dot W_2||_op B_1 + A ||dot h_a^(1)||_n <= D_Z,
||dot delta_a^(2)||_n
    <= D_w P_2 + W_* L_2 ||dot z_a^(2)||_n <= D_delta,
||dot q_a||_n
    <= D_A ||delta_a^(2)||_n + A ||dot delta_a^(2)||_n
    <= Q_1.
```

The only coordinatewise multiplier used on a varying hidden field here
is `W_3`, which has a proved infinity-norm bound. In particular, these
steps do not treat the RMS bound on `q_a` as a bound on its multiplication
operator.

Finally `||dot W||_raw<=K F` and `||grad_raw f_a||_raw<=F` imply
`|dot f_a|<=K F^2`. Since there are two samples and `c_a=-2r_a`,
`sum_a |dot c_a|<=4K F^2=D_c`. This verifies the residual-variation
constant, including its factor of four.

### 5.2 GD bounds, with all finite-difference cross terms retained

The old-node update gives `||Delta z_a^(1)||_n<=eta K P_1 Q` and hence
`||Delta h_a^(1)||_n<=eta K P_1^2 Q`. The identities

```text
Delta z_a^(2)
    = Delta W_2 h_(k,a)^(1) + W_(k+1,2) Delta h_a^(1),
Delta delta_a^(2)
    = Delta W_3 phi_2'(z_(k,a)^(2))
      + W_(k+1,3)[phi_2'(z_(k+1,a)^(2))-phi_2'(z_(k,a)^(2))],
Delta q_a
    = (Delta W_2)^T delta_(k,a)^(2)
      + W_(k+1,2)^T Delta delta_a^(2)
```

are exact. Using the new endpoint in the second term includes the
products of increments that would be lost in an unjustified
linearization. The previously proved endpoint bounds and Lipschitz
constants give

```text
||Delta z_a^(2)||_n <= eta D_Z,
||Delta delta_a^(2)||_n <= eta D_delta,
||Delta q_a||_n <= eta Q_1.
```

Integration of `Df_a` along the raw segment also gives
`sum_a |Delta c_a|<=eta D_c`. All these estimates apply to the actual
node values under the original simultaneous update.

### 5.3 The pathwise empirical envelope

Set `v_(a,i)=c_a q_(a,i)`. For GF the source defines the sum of the two
initial absolute controls plus their coordinatewise total variations
through `T`; for GD it uses total variation through old node `N-1`.
Call the resulting nonnegative row quantity `U_i` in either scheme.
The fundamental theorem of calculus, or the telescoping finite sum,
gives `sum_a |v_(a,i)|<=U_i` at every relevant control evaluation.

The triangle inequality in normalized Euclidean norm gives

```text
||sum_a |v_a(0)||_n <= sum_a |c_a(0)| ||q_a(0)||_n <= K Q.
```

For GF, differentiate `v_a=c_a q_a`. The normalized norm of the sum
of the absolute derivatives is bounded by

```text
sum_a |dot c_a| ||q_a||_n + sum_a |c_a| ||dot q_a||_n
    <= D_c Q + K Q_1.
```

Integrating, and using `T<=H`, proves

```text
||U||_n <= KQ + H(D_c Q + K Q_1) = V_T.
```

For GD use the exact identity

```text
v_(k+1,a)-v_(k,a)
    = (c_(k+1,a)-c_(k,a)) q_(k,a)
      + c_(k+1,a)(q_(k+1,a)-q_(k,a)).
```

Both endpoint residuals are now controlled. Each variation term has
normalized norm at most `eta(D_c Q+K Q_1)`, and there are `N-1` such
terms. Their total duration is at most `H`. Thus both envelopes satisfy

```text
(1/n) sum_i U_i^2 <= V_T^2,
max_i U_i <= sqrt(sum_i U_i^2) <= sqrt(n) V_T.
```

No random-row independence enters any of these estimates. They hold
deterministically on the primal-control event, although the envelope can
depend on every weight and the entire trajectory. For GD, controls at
node `N` are unnecessary: the last cell uses old node `N-1`.

## 6. Scalar barriers and protection of full GD cells

For `|x|<R`, let `d(x)=R-|x|`. Choose the nearest endpoint of `[-R,R]`.
Since `p` vanishes there and is `L_1`-Lipschitz,

```text
0 <= p(x) <= L_1 d(x).
```

For a scalar GF equation `dot x=p(x)v(t)` with `|v(t)|<=U`, the
Lipschitz chain inequality gives, almost everywhere before exit,

```text
(d(x(t)))' >= -|dot x(t)| >= -L_1 U d(x(t)).
```

Multiplication by `exp(L_1 U t)` yields
`d(x(t))>=d(x(0)) exp(-L_1 U t)`. If the initial distance is positive,
its lower bound stays positive at any finite proposed first hitting
time. Thus neither boundary is reached. The absolute value at zero
causes no difficulty: an absolutely continuous path composed with a
Lipschitz function is absolutely continuous and obeys this derivative
inequality almost everywhere. The control can change sign arbitrarily.

For an exact scalar GD cell,

```text
x_(k+theta) = x_k + theta eta p(x_k)v_k,     0<=theta<=1,
s = eta L_1 U <= 1/2,
```

the triangle inequality gives

```text
d(x_(k+theta)) >= d(x_k)-theta eta p(x_k)|v_k|
                >= (1-theta s)d(x_k) > 0.
```

Hence every point in the cell is interior. Iterating the endpoint
inequality and then the partial-cell inequality gives

```text
d(x_(k+theta)) >= d(x_0)(1-s)^k(1-theta s).
```

For `0<=u<=1/2`, the function `log(1-u)+2u` is zero at zero and has
derivative `(1-2u)/(1-u)>=0`. Applying its nonnegativity to `s` and
`theta s` gives

```text
d(x_(k+theta)) >= d(x_0) exp(-2L_1 U (k+theta)eta).
```

This proof concerns the exact affine raw first preactivation. It does
not replace the old-node gate by a nonlinear interpolated gate.

The admissible row parameter is the actual `U_i`. The envelope gives

```text
eta L_1 U_i <= L_1 V_T n^-3/2 <= 1/2
```

under (17), for every row. Later substituting `U_i<=M` in the exponent
does not require `eta L_1 M<=1/2`: the small-step hypothesis has already
been verified for `U_i`. This distinction is essential to the
angle-independent width claim and is handled correctly in the source.

## 7. Protected strips: closing the scalar reduction

For either specified ordered pair `a,b`, multiplying the physical first
update by the two inputs gives

```text
dot z_a = p(z_a)v_a + rho p(z_b)v_b,
dot z_b = rho p(z_a)v_a + p(z_b)v_b.
```

The exact GD increments are `eta` times these expressions evaluated
at the old node. The input normalization accounts for both diagonal
coefficients being one and the off-diagonal coefficient being `rho`.

Before making any inactivity assumption, the difference
`e=z_b-rho z_a` satisfies

```text
dot e = (1-rho^2) p(z_b)v_b,
Delta e = eta(1-rho^2) p(z_(k,b))v_(k,b).
```

It is therefore a conditional invariant, not an invariant of arbitrary
two-sample trajectories. The source correctly closes the condition.

For a row in `S_a`, `|z_a(0)|<=R/2` and `|e(0)|>=3R`, so
`|z_b(0)|>=3R-|rho|R/2>R`. On any GF interval before the first exit
from `|z_a|<R, |z_b|>R`, the other sample's gate is zero, `e=e(0)`, and
`dot z_a=p(z_a)v_a`. The scalar bound gives

```text
R-|z_a(t)| >= (R/2) exp(-L_1 U_i t),
|z_b(t)| = |e(0)+rho z_a(t)|
          >= 3R-|rho|R > 2R.
```

At a finite proposed exit, continuity preserves the positive first
margin and the strict second margin. Neither boundary of the stopping
region can be reached. This excludes the exit, including a proposed
exit at the horizon endpoint.

For GD, suppose the same region and invariant hold at node `k`.
Because `p(z_(k,b))=0`, the exact raw cell satisfies

```text
z_(k+theta,a) = z_(k,a)+theta eta p(z_(k,a))v_(k,a),
z_(k+theta,b)-rho z_(k+theta,a) = e(0).
```

The row step condition protects `a` at every `theta`. The second
identity then protects `b` at every `theta`, with the same exterior
margin as above. The endpoint renews the induction hypothesis for the
next cell. This proves

```text
R-|z_a(t)| >= (R/2) exp(-2L_1 U_i t),   0<=t<=N eta.
```

Although the other sample's first gate is zero on this row, it may still
affect residuals and upper-layer parameters. The proof accommodates that
through the actual control envelope. It does not remove that sample
from network training.

The reasoning applies with `a=1,b=2` and with `a=2,b=1`. Thus it produces
two separate pathwise statements. In fact the two initial strips are
disjoint: a row in `S_a` has the other coordinate outside `[-R,R]`,
whereas membership in `S_b` requires that coordinate in `[-R/2,R/2]`.
Their disjointness presents no counting obstruction and makes especially
clear why each sample needs its own occupancy argument.

## 8. The antiparallel case and its control factor

At `rho=-1`, input normalization gives
`||x_1+x_2||^2=2d+2rho d=0`. Thus `x_2=-x_1` and
`z_2^(1)=-z_1^(1)` at every raw state, including all interpolated states.
Evenness of `p` reduces the first pair to

```text
dot z = p(z)(v_1-v_2),
Delta z = eta p(z_k)(v_(k,1)-v_(k,2)).
```

The effective control is bounded by
`|v_1-v_2|<=|v_1|+|v_2|<=U_i`. The source's envelope already contains
both samples, so no additional factor of two belongs in the scalar
step condition.

As an independent consistency check using the displayed odd
activations and opposite labels, this case also has
`h_2^(ell)=-h_1^(ell)`, `f_2=-f_1`, `c_2=-c_1`. Since `phi_2'` is even,
`q_2=q_1`, hence `v_2=-v_1`. The effective control is then `2v_1`,
while its absolute value is exactly `|v_1|+|v_2|`. This confirms the
factor accounting; these extra identities are not needed by the proof.

For rows in `S_0`, the initial scalar distance is at least `R/2`.
The GF and GD scalar estimates apply directly and give the same
distance for both samples because their absolute preactivations agree.
There is no Gaussian innovation with positive variance to use at this
angle, and no inverse of the singular Gram matrix is taken.

## 9. Gaussian occupancy, norm tails, and deterministic count removal

### 9.1 Separate occupancy events

For each first-layer row, direct computation from variance `1/d` gives

```text
Var(G_a) = ||x_a||^2/d = 1,
Cov(G_1,G_2) = x_1^T x_2/d = rho.
```

The pair is jointly Gaussian, and different rows are independent. For
`-1<rho<1`, define `E=G_b-rho G_a`. Then

```text
Cov(G_a,E)=rho-rho=0,
Var(E)=1+rho^2-2rho^2=1-rho^2.
```

The joint characteristic function is
`exp(-(s^2+(1-rho^2)t^2)/2)`, which factors into the two marginal
characteristic functions. Thus `G_a` and `E` are independent, and

```text
P(i in S_a)
 = [2Phi(R/2)-1] * 2[1-Phi(3R/sqrt(1-rho^2))]
 = m_rho > 0.
```

At `rho=-1`, `S_0` instead has mass `m_0=2Phi(R/2)-1>0`.
These positivity statements hold for every fixed `R>0` and every
angle in the specified cases, regardless of how small the mass is.

For each individual strip or center set, its normalized count has
mean `m` and variance `m(1-m)/n`. Consequently

```text
P(|S|/n < m/2)
 <= P(abs(|S|/n-m) >= m/2)
 <= 4(1-m)/(n m).
```

Union bound over the two ordered strips gives `8(1-m)/(n m)` in the
interior case. Only one count is required at the antiparallel angle,
giving `4(1-m_0)/(n m_0)`. The two strip counts are not assumed
independent, and no evolved row variables enter this probability step.

### 9.2 Norm-event probabilities

For completeness, the source's elementary norm calculation checks out.
Take a maximal `1/4`-separated subset of the unit sphere. The radius
`1/8` balls about its points have disjoint interiors and lie inside
the radius `9/8` ball, giving at most `9^n` points. Maximality gives a
`1/4`-net. For unit `u,v` and net approximations `u_0,v_0`,

```text
u^T W v - u_0^T W v_0
    = (u-u_0)^T W v + u_0^T W(v-v_0).
```

Its absolute value is at most `||W||_op/2`. Taking the supremum gives
`||W||_op<=2 max_(u_0,v_0) |u_0^T W v_0|`.

For `W=W_2(0)`, each fixed tested form is Gaussian with variance
`(1/n)sum_(i,j)u_0,i^2 v_0,j^2=1/n`. Completing the square in the
Gaussian integral gives `E exp(lambda Z)=exp(lambda^2 sigma^2/2)`.
Exponential Markov with `lambda=s/sigma^2`, and then the two-sided
union bound, gives `P(|Z|>=s)<=2exp(-s^2/(2sigma^2))`. At `s=4`,
union over at most `9^(2n)` tested pairs therefore yields

```text
P(||W_2(0)||_op>8) <= 2exp(-(8-2log 9)n).
```

The same tail bound at threshold one for variance `n^-2` gives

```text
P(||W_3(0)||_infinity>1) <= 2n exp(-n^2/2).
```

Adding these errors to the occupancy errors proves exactly (8).
Independence between blocks and counts is unnecessary for this union
bound. A negative numerical lower bound for very small `n` is simply
uninformative, not inconsistent.

### 9.3 Removing large envelopes from each strip

On the event `A_n(rho)`, fix one of the two actual schemes and let
`M=2V_T/sqrt(m)`. The empirical square bound gives deterministically

```text
# {i: U_i>M} / n
    <= (1/(n M^2)) sum_i U_i^2
    <= V_T^2/M^2 = m/4.
```

For either sample separately,

```text
I_a = S_a intersect {i:U_i<=M},
|I_a|/n >= |S_a|/n - # {i:U_i>M}/n >= m/2-m/4=m/4.
```

This remains valid if every large-envelope row lies in the very strip
being considered. The same global removal bound can be used in each
of the two inequalities; it is not a probabilistic allocation of bad
rows between samples. At `rho=-1` the same subtraction is made from
`S_0`, and `I_0` serves both samples.

The sets depend on the full relevant trajectory, but once defined they
are fixed throughout the horizon. They are not changing collections of
rows chosen separately at each time. Integer rounding creates no gap:
an integer cardinality satisfying `|I|>=nm/4` has the required meaning
even when the right side is not an integer.

### 9.4 Final gate lower bound

For a retained row, GF has distance at least
`(R/2)exp(-L_1 M T)`. For GD all `N` full cells have distance at least
`(R/2)exp(-2L_1 M H)`, since `N eta<=H`. Thus the source's common choice

```text
delta = (R/2)exp(-2L_1 M H)
```

works for both. It is strictly positive and at most `R/2`. Continuity
and strict interior positivity of `p` give

```text
p_delta = min_(|z|<=R-delta) p(z) > 0.
```

This compact minimum is the correct construction for nonmonotone `p`;
no comparison with just one endpoint value is used. At every time in
the horizon, for each specified sample,

```text
(1/n) sum_i p(z_a,i^(1)(t))^2
    >= (|I_a|/n) p_delta^2 >= (m/4)p_delta^2.
```

The common event gives this conclusion for both GF and GD, although
their envelopes and retained sets may differ. No additional union of
probability errors is required to cover the two schemes: each is a
deterministic implication of the same event. The proof does not claim a
single common retained subset of size `nm/4` for both schemes.

## 10. Width, angle, dimension, and time quantifiers

All primal and envelope constants depend only on the fixed activation
bounds and the horizon. In particular they have no dependence on
`rho` or `d`. The only width dependence in the Hessian is explicit.
To make the sufficient width threshold completely concrete, write

```text
f20 = 2P_2 J + W_* L_2 J^2 + 2W_* P_2 P_1,
f21 = W_* P_2 A L_1,
h0 = 4F^2 + 2sqrt(2)(R_*+1) f20,
h1 = 2sqrt(2)(R_*+1) f21.
```

Then `H_2(n)=h0+h1 sqrt(n)`. One admissible integer threshold is

```text
n_T = ceil(max{
    1,
    (sqrt(2) K F^2)^(1/2),
    (2h0)^(1/2),
    (2h1)^(2/3),
    (2L_1 V_T)^(2/3)
}).
```

For every `n>=n_T`, the first nontrivial entry ensures the segment
residual condition. The next two give
`h0 n^-2<=1/2` and `h1 n^-3/2<=1/2`, hence the Hessian step condition.
The last gives the row barrier condition. This exhibits an
angle-independent and dimension-independent sufficient GD threshold.

The conclusions have several distinct quantifiers:

1. **Deterministic GD step threshold.** `n_T` can be chosen independently
   of `rho,d` for the displayed normalized inputs and fixed activations.
2. **Positive gate constant.** `m=m_rho`, `M`, `delta`, `p_delta`, and
   `kappa_(T,rho)` are angle dependent. They are positive at each fixed
   permitted angle, with no positive lower bound over all interior
   angles asserted.
3. **Probability at a prescribed confidence.** The error contains
   `1/(n m_rho)`. A width sufficient to make that error small generally
   depends on the angle, even though the deterministic step threshold
   does not. For example, making the interior occupancy error at most
   `epsilon/2` is ensured by
   `n>=16(1-m_rho)/(epsilon m_rho)`.
4. **Fixed versus varying angle.** As an interior angle tends to either
   endpoint, `m_rho` tends to zero. The fixed-angle convergence in
   probability need not hold with the same confidence along arbitrary
   angle sequences depending on width. At exactly `rho=-1`, the proof
   uses the different, positive center mass `m_0`; the jump between
   constructions is legitimate.
5. **Finite versus unbounded time.** On `A_n`, finite GF exists globally
   and the deterministic argument can be applied to every finite `T`.
   The retained set and positive constant can depend on `T`. GD's
   sufficient threshold is chosen after `T`, so the theorem gives no
   all-time guarantee at a single fixed finite GD width.
6. **Input pair quantifier.** The probability calculation holds for
   each fixed input pair selected independently of initialization. It
   does not establish a simultaneous event over all possible pairs or
   permit selecting inputs after observing the weights.

The source states these distinctions correctly. At `T=0`, its
`N=max(1,ceil(T/eta))` convention still gives one protected GD cell and
`N eta<=1=H`; the GF envelope has no variation integral. There is no
zero-horizon exception. The endpoint `rho=1` is excluded and has not
been silently supplied by a limit argument.

## 11. Adversarial checks and analytic counterexamples to stronger claims

These checks were analytic; no numerical experiments were run.

- **Finite-width failure without the initialization event.** For an
  interior angle the joint Gaussian density is positive on, for
  example, a rectangle with both coordinates strictly larger than
  `R`. Hence a single row has positive probability of both gates being
  zero. Independence across rows makes the event that every row has
  both gates zero have positive probability at every finite width.
  At the antiparallel angle use `|G|>R` instead. On these events the
  first-layer update is identically zero in GD. For GF, keeping the
  first layer fixed gives the same zero first-layer vector field, and
  uniqueness preserves it. Both gate-square averages remain zero.
  This validates the source's warning against an exception-free claim.

- **Large GD jumps without a step restriction.** In the scalar
  equation, start at `x_0=0`. Since `p(0)>0`, a control satisfying
  `eta p(0)|v_0|>R` sends the next node outside the active interval.
  This is an obstruction to an unrestricted scalar Euler claim. The
  actual-network envelope and (17) exclude it on the proved event at
  the admitted widths.

- **Other-sample reentry.** The quantity `z_b-rho z_a` is not generally
  conserved; its derivative contains `(1-rho^2)p(z_b)v_b`. A proof that
  used it without maintaining inactivity would fail. Here the closed
  stopping argument and the exact cell identity maintain the strict
  exterior margin, so this counterexample route is blocked.

- **Highly concentrated, trajectory-dependent controls.** The empirical
  envelope permits some `U_i` of order `sqrt(n)`. It also permits all
  large-envelope rows to concentrate in one initial strip. The
  maximum-row step estimate handles the first possibility, and the
  deterministic subtraction handles the second. Independence or a
  uniform `O(1)` coordinate bound would be unjustified, but neither is
  used.

- **Misusing the angle-dependent cutoff as a step bound.** Near an
  endpoint, `M=2V_T/sqrt(m_rho)` can be arbitrarily large. A requirement
  `eta L_1 M<=1/2` would introduce an angle-dependent sufficient width.
  The actual proof uses `U_i<=sqrt(n)V_T` for the step and uses `M`
  only afterward for the distance exponent.

- **Losing a sample through a summed bound.** A lower bound on the sum
  of the two samples' gate averages would allow one sample to have
  zero average. The proof instead establishes an occupied, protected,
  retained set for each ordered sample separately. This route to a
  false individual conclusion is not present.

- **Antiparallel singularity and a hidden factor of two.** The Gaussian
  innovation argument is unavailable at `rho=-1`; the source replaces
  it by a physical identity and a center count. The effective scalar
  control may equal twice a one-sample control, but the envelope
  already sums both absolute controls, as checked above.

- **Nonmonotone or very flat gates.** Smooth positive interior bumps
  can approach zero very rapidly near the boundary and need not be
  monotone. The Lipschitz upper bound and compact interior minimum
  remain valid. The resulting lower constant may be extremely small;
  that is compatible with the theorem's strict positivity claim.

- **Positive gates with exactly zero motion.** Take the antiparallel
  case and the deterministic raw state `W_1=W_2=W_3=0`. Then all
  first gates equal `p(0)>0`, every row belongs to `S_0`, and `E_n`
  holds. Odd activations give both hidden layers zero output;
  `delta^(2)=q=0`; all three parameter updates are zero. Thus this
  state has positive gate averages and a stationary trajectory despite
  nonzero residuals. It is a measure-zero state under the continuous
  Gaussian initialization, but it directly demonstrates why a gate
  lower bound alone is not a deterministic force or motion lower
  bound. The theorem does not make that stronger claim.

None of these checks produced a counterexample to the theorem with
its actual event, width conditions, and finite-horizon quantifiers.

## 12. Required fixes, optional clarifications, and scoped disposition

### Required mathematical fixes

**None identified.** In particular, the audit did not find a missing
normalization factor, an unclosed first-exit step, a discarded GD
cross term, an unproved independence assumption, an interpolation gap,
an antiparallel factor error, or an angle-dependent quantity hidden in
the claimed deterministic width threshold.

No dependency lookup is required to complete the proof as written.
Elementary finite-dimensional ODE continuation, calculus, norm
inequalities, Gaussian characteristic functions, and Gaussian tail
bounds suffice; their application is given in the source and expanded
in this review.

### Optional clarifications

1. **Readout dictionary, lines 34–55.** If readers will compare the
   result with another normalization, explicitly add
   `w_out=W_3/n`, `Var(w_out,i(0))=n^-4`. This would clarify the word
   "rescaled". It does not require changing the displayed model or
   repairing any estimate.
2. **Two meanings of a sufficient width, lines 87–126 and 316–323.**
   An additional sentence could explicitly distinguish the
   angle-independent deterministic step threshold from the
   angle-dependent width needed for a prescribed high probability.
   The current quantifiers and error formula are already correct.
3. **A closed-form sufficient threshold.** The formula in review
   Section 10 could replace or accompany the conditions (12) and
   (17). The existing conditions already prove existence of a finite
   threshold for every larger width.
4. **Terminology, lines 539–548.** The source defines "trainable" to
   mean an unsaturated gate and immediately disclaims motion and
   kernel conclusions. Using "unsaturated" consistently would make
   this distinction harder to miss; there is no mathematical scope
   error in the current qualified usage.

### Scoped disposition

Accept the displayed theorem as a self-contained proof of persistent
positive empirical first-gate square, separately for each of the two
fixed samples, for actual finite GF and sufficiently wide simultaneous
raw GD, including the full GD cells covering each fixed finite horizon.
The event and its probability estimate, the separate retained subsets,
the antiparallel treatment, and the angle-independent deterministic
step threshold are supported by the derivations above.

This disposition applies only to the source with the recorded SHA256.
It does not certify its unread provenance notes, any alternate model
normalization, an angle-uniform probability claim, nonlazy dynamics,
nonzero motion, or a mean-field conclusion.

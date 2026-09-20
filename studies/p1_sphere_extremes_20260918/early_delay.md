# Independent early-delay derivation for initialized canonical p=1 in d=3

Status: internally derived theorem, not promoted material. This file was written
without reading another study, another agent's findings, or study history.
No numerical experiment, coefficient quadrature, or population approximation
was run. The exponent below is a lower-bound exponent; a matching upper bound
is not claimed.

## Contract and sources

The object is the exact population p=1 closure in dimension three, with the
joint Gaussian initialization, ridge `eta=1/4096`, both physical population-L2
metrics, the physical Frobenius middle metric, and the complete evolving
`3 x 6` matrix. The data lie on `sqrt(3) S2`; write `u=x/sqrt(3)`.
The loss is the unhalved weighted square loss. Initially `w=g`, `c=0`, `M=D`.
The two population spaces remain independent, and every lower `(b1,g)` pair
retains its full joint law. Removing the constant features uses the exact
invariant sign class; it changes neither the equations nor their metric.

Scientific sources used:

1. `docs/observable_p1.md`, complete: exact general-dimensional initialized
   coefficients, joint Gaussian marks, sign reduction, equations, and metric.
2. `docs/global_nonlinear.md`, C.4.7.9.3--4: characteristic equations,
   bounded-feature local existence, continuation, and energy argument.
3. `docs/global_nonlinear.md`, C.4.7.10.D.3, dictionary/state/equations and
   energy/existence portions: the same population/Frobenius metric and
   contraction representation. Its separate d=2 network-identification domain
   is not extended to the present data.

The required investigate-conjectures skill, its research-contract and
adversarial-audit references, and solve-math-rigorously skill were read. This
is an exact closure theorem, not a general-d trained-network limit theorem.

## The family and conclusions

For `0 < epsilon <= 1/2`, set

\[
 u_+=(\sqrt{1-\varepsilon^2-\varepsilon^4},\varepsilon,\varepsilon^2),
 \qquad
 u_-=(\sqrt{1-\varepsilon^2-\varepsilon^4},-\varepsilon,\varepsilon^2),
 \qquad u_0=e_1.
\]

Give `u_+,u_-` label `+1` and masses `1/4,1/4`, and `u_0` label `-1`
and mass `1/2`. Each vector has unit length. The determinant of the matrix
with these three rows is `2 epsilon^3`, so every positive member has three
distinct linearly independent inputs. The label masses are exactly balanced.

Let `L_epsilon` be its exact initialized loss, so `L_epsilon(0)=1`. There
is a finite constant `C>0`, depending only on the fixed canonical p=1
coefficients and not on epsilon, with the following properties:

* For `0 <= t <= 1/(C epsilon^2)`, the raw displacement `R(t)` defined below
  obeys `R(t) <= C epsilon^2 t`, and
  `0 <= 1-L_epsilon(t) <= C^2 epsilon^4 t`.
* For every fixed `delta in (0,1)`, if
  `T_delta(epsilon)=inf{t: L_epsilon(t)<=1-delta}` (infinity if never), then
  for all sufficiently small epsilon,
  `T_delta(epsilon) >= 1/(C epsilon^2)`.
* The exact initial loss slope is of order epsilon to the fourth:
  `-L_epsilon'(0)=4 ||V||_2^2 epsilon^4+o(epsilon^4)`, where the fixed
  upper-population field `V` is explicitly defined below and is nonzero.

Thus the delay is a statement about the true evolving system, not an inference
from the initial slope or a frozen-feature surrogate. It rules out every
geometry-uniform loss envelope tending to zero, in particular an estimate
`L_epsilon(t)<=A exp(-lambda t)` with fixed finite `A` and fixed positive
`lambda`. It does not rule out a data-dependent exponential rate or fast
terminal convergence after a delay.

## Exact equations, contractions, and existence

Use the source's active feature columns `b1 in R6`, `b2 in R3`, and write

\[
 a(u)=E_1[b_1\tanh(w\cdot u)],\quad
 z(u)=b_2^TMa(u),\quad H(u)=\tanh z(u),\quad f(u)=E_2[cH(u)],
\]
\[
 d(u)=E_2[b_2c\operatorname{sech}^2z(u)],\quad
 Q(u)=b_1^TM^Td(u).
\]

For `r_a=f(u_a)-y_a`, the exact physical equations are

\[
 \dot w=-2\sum_a\mu_a r_a\operatorname{sech}^2(w\cdot u_a)Q(u_a)u_a,
 \quad \dot c=-2\sum_a\mu_a r_aH(u_a),
 \quad \dot M=-2\sum_a\mu_a r_a d(u_a)a(u_a)^T.
 \tag{1}
\]

All entries of `M` evolve. The reverse uses this same matrix's actual
transpose. For the physical product Hilbert norm,

\[
 \|(v,N,q)\|_{\rm raw}^2=\|v\|_{L^2(\Omega_1;\mathbb R^3)}^2
      +\|N\|_F^2+\|q\|_{L^2(\Omega_2)}^2,
\]

direct loss differentiation gives

\[
 \mathcal L'(t)=-\|\dot w\|_2^2-\|\dot M\|_F^2-\|\dot c\|_2^2,
 \qquad
 \mathcal L(t)+\int_0^t\|\dot\theta(s)\|_{\rm raw}^2ds=1.
 \tag{2}
\]

For clarity, no unweighted population metric is substituted here: the
population expectations are the weights in the first and third norm terms.

Let `U_l v=b_l^T v`. Ridge normalization gives

\[
 E[b_lb_l^T]=I-\eta L_l^{-1}L_l^{-T}\preceq I,
 \qquad \|U_l\|_{\rm op}\le1.
 \tag{3}
\]

The active feature block has the same property after deleting the inactive
constant. Define the finite envelopes `K_l=ess sup |b_l|`. Local existence
holds for bounded `w-g,c` and finite `M`: the gates are Lipschitz, the
features are bounded, and every population contraction is a bounded
operation there. The contraction proof in the source is dimension-independent
and therefore applies to the present fixed finite dimensions.

There is no finite-time obstruction. From (2), `sum mu |r|<=1`;
thus `||c||_infinity<=2t`, `|a|<=1`, `|d|<=||c||_2<=2t`, and
`||M-D||_F<=2t^2`. Also

\[
 \|\dot w\|_\infty\le 2K_1\|M\|_{\rm op}\|c\|_2
              \le4tK_1(\|D\|_{\rm op}+2t^2).
\]

These bounds keep the local-existence variables bounded on each finite
interval; bounded velocities yield an endpoint and local continuation.
This proves unique existence through every finite time for this closure.

## A uniform second-difference estimate on each fixed state ball

For a current state define

\[
 R=\bigl(\|w-g\|_2^2+\|M-D\|_F^2+\|c\|_2^2\bigr)^{1/2},
 \qquad W=\|w\|_2,\qquad B=\|M\|_{\rm op}.
\]

The map `u -> a(u)` is twice continuously differentiable as a map into
`R6`, even when only `w in L2`: its second derivative is dominated by
`2 K1 |w|^2`, an integrable function. For a unit direction `v`, (3) and
the bounded tanh derivatives give

\[
 |\partial_va|\le W,\qquad
 |\partial_v^2a|\le2K_1W^2.
\]

Consequently, uniformly in all `u in R3`,

\[
 \|\partial_vH(u)\|_2\le BW,
 \qquad
 \|\partial_v^2H(u)\|_2
       \le 2BW^2(K_1+K_2B).
 \tag{4}
\]

For the second bound, `partial_v z` has L2 norm at most `BW` and
supremum norm at most `K2 BW`. Therefore
`||phi''(z)(partial_v z)^2||_2<=2K2 B^2 W^2`; the remaining term is at
most `2 K1 B W^2`. This avoids an unjustified L2-algebra or L4 assumption.

Let `v_epsilon=(sqrt(1-epsilon^2-epsilon^4),0,epsilon^2)` and define the
signed upper feature

\[
 m_\varepsilon(\theta)
   =\sum_a\mu_a y_a H(u_a)
   =\tfrac14\{H(u_+)+H(u_-)-2H(u_0)\}.
\]

For `epsilon<=1/2`, `|v_epsilon-u0|<=2 epsilon^2`. The integral form of
the centered second difference and (4) imply

\[
 \begin{split}
 \|m_\varepsilon(\theta)\|_2
 &\le\frac{\varepsilon^2}{4}\sup_u\|\partial_{e_2}^2H(u)\|_2
       +\frac12\sup_u\|\nabla H(u)\|\,|v_\varepsilon-u_0|\\
 &\le\varepsilon^2
       \left[BW+\tfrac12 BW^2(K_1+K_2B)\right].
 \tag{5}
 \end{split}
\]

The gradient norm in the middle line is the operator norm from `R3` to
upper L2, bounded by `BW`.

On `R<=1`, use `W<=sqrt(3)+1=:W_*` and
`B<=||D||_op+1=:B_*`. Set explicitly

\[
 K=B_*W_*+\tfrac12B_*W_*^2(K_1+K_2B_*),\qquad C=2K.
 \tag{6}
\]

These are positive finite constants determined by the exact initialized
coefficients. If desired, the source formulas give the elementary envelopes

\[
 K_1^2\le\frac3{a^2}+\frac{3(1+\beta/(v+\eta))^2}{b^2},
 \qquad K_2^2\le\frac3{\tau+\eta}.
\]

No numerical value or certificate for these constants is needed.

## The energy barrier proves a hitting-time delay

Expansion of the loss at an arbitrary state gives the exact identity

\[
 1-\mathcal L
    =2\langle c,m_\varepsilon(\theta)\rangle_2
       -\sum_a\mu_a f(u_a)^2.
 \tag{7}
\]

On a reached state with `R<=1`, (5)--(7) and loss monotonicity give

\[
 0\le1-\mathcal L(t)\le C\varepsilon^2\|c(t)\|_2
                         \le C\varepsilon^2R(t).
 \tag{8}
\]

On the other hand, the Hilbert-space Cauchy--Schwarz inequality and (2) give,
without any bound on intermediate state displacements,

\[
 R(t)^2=\left\|\int_0^t\dot\theta(s)ds\right\|_{\rm raw}^2
       \le t\int_0^t\|\dot\theta(s)\|_{\rm raw}^2ds
       =t[1-\mathcal L(t)].
 \tag{9}
\]

Whenever `R(t)<=1`, combining (8)--(9) yields

\[
 R(t)\le C\varepsilon^2t,\qquad
 1-\mathcal L(t)\le C^2\varepsilon^4t.
 \tag{10}
\]

The zero-displacement case satisfies these directly; otherwise divide by R.
If a first exit `R(t_*)=1` occurs, (9) and (8) at that exit give
`t_*>=1/(C epsilon^2)`. Continuity therefore validates (10) throughout
`0<=t<=1/(C epsilon^2)`.

For fixed `delta>0` and `C epsilon^2<delta`, (8) shows that reaching
`L<=1-delta` is impossible while `R<=1`. The threshold must follow an exit,
which proves the asserted hitting-time lower bound. If the threshold is
never reached, the same assertion holds with hitting time infinity.

This proof uses the increase in all parameter blocks that would be needed
to defeat cancellation. No stability estimate with an exponentially growing
Gronwall constant, frozen middle layer, or frozen row population is used.

## The initial slope is genuinely of order epsilon^4

This section verifies that the family is not accidentally stationary at
positive epsilon. Use the scalar constants in the source, and denote the
two nonzero bands of D by `d_h>0,d_k>0`. Their positivity follows from
the displayed source formulas: `v,tau,alpha,gamma>0` and `beta>0`.
For the last fact, conditioning on G makes `E[k|G]` odd and strictly
increasing in `tanh G`, so `tanh G E[k|G]>0` off zero.

Put

\[
 \bar k(s)=E_Z\tanh(\sqrt\tau Z+\alpha\tanh s),\quad
 F(s)=A\tanh s+B\bar k(s),
\]
\[
 A=\frac{d_h}{a}-\frac{d_k\beta}{b(v+\eta)},\qquad
 B=\frac{d_k}{b}>0.
 \tag{11}
\]

Conditioning the exact lower joint law on its Gaussian coordinates gives
the initialized upper preactivation exactly as

\[
 z_0(u)=\sum_{i=1}^3 b_{2i}v_i(u),\qquad
 v_i(u)=E[F(G_i)\tanh(G\cdot u)].
 \tag{12}
\]

This conditional expectation is only a proof calculation; it does not
resample or decouple the lower feature and Gaussian mark.

Write `q(s)=sech^2 s` and define

\[
 v_*=E[F(G)\tanh G],\qquad
 \kappa=E[q(G)]E[F'(G)],\qquad
 \rho=E[q(G)F'(G)].
\]

At `u=e1`, independence and oddness in each Gaussian coordinate give

\[
 z_0=v_*b_{21},\qquad \partial_2z_0=\kappa b_{22},\qquad
 \partial_3z_0=\kappa b_{23},\qquad
 (\partial_{22}-\partial_1)z_0=-\rho b_{21}.
 \tag{13}
\]

For example `E[G F(G)]=E[F'(G)]` follows by integrating the Gaussian
density derivative; the boundary term vanishes because F is bounded.
For the last identity,
`E[F(G)(phi''(G)-G phi'(G))]=-E[F'(G)phi'(G)]`, by the same integration
by parts. All other coordinate terms vanish by independence and oddness.

The initial feature map is C2 into upper L2, with all required Gaussian
moments finite. Since
`u_+-e1=epsilon e2+epsilon^2(e3-e1/2)+o(epsilon^2)` and the analogous
formula holds with the opposite sign for `u_-`, its Taylor expansion gives

\[
 m_\varepsilon(\theta_0)=\varepsilon^2 V+o_{L^2}(\varepsilon^2),
 \tag{14}
\]
\[
 V=\frac\kappa2\phi'(v_*b_{21})b_{23}
      -\frac\rho4\phi'(v_*b_{21})b_{21}
      +\frac{\kappa^2}{4}\phi''(v_*b_{21})b_{22}^2,
 \qquad \phi=\tanh.
 \tag{15}
\]

Here `V` is nonzero, as the following argument verifies without numerical
coefficient inequalities. If `kappa!=0`, its component odd in `b23` is
`(kappa/2) phi'(v_*b21) b23`, which has strictly positive L2 norm and
cannot cancel the other two terms.

Suppose instead that `kappa=0`. Define

\[
 J(s)=E_Z\operatorname{sech}^2(\sqrt\tau Z+\alpha\tanh s).
\]

Then `F'(s)=q(s)[A+B alpha J(s)]`. Both q and J are even and strictly
decreasing in `|s|` on the positive half-line. For J, the Gaussian convolution
`j(r)=E sech^2(sqrt(tau)Z+r)` is even and, for `r>0`,

\[
 j'(r)=\int_0^\infty(\operatorname{sech}^2)'(z)
             [\varphi_\tau(z-r)-\varphi_\tau(z+r)]\,dz<0.
\]

The derivative factor is negative and the density difference is positive;
composition with the strictly increasing `alpha tanh s` proves the claim.

Let nu be the probability law with density `q(G)/E q(G)` relative to
the standard Gaussian. Since `E F'=0` in the present case,

\[
 A=-B\alpha E_\nu J,\qquad
 \rho=B\alpha E[q(G)]\operatorname{Cov}_\nu(q,J)>0.
 \tag{16}
\]

The strict covariance sign follows by writing it as one half of
`E[(q(G)-q(G'))(J(G)-J(G'))]` for independent nu draws: the integrand is
positive whenever the two absolute values differ, an event of probability
one. Thus when `kappa=0`, (15) reduces to the nonzero field
`-(rho/4)phi'(v_*b21)b21`. In either case `||V||_2>0`.

At initialization `d(u)=0`, so `dot w(0)=0` and `dot M(0)=0` exactly,
whereas `dot c(0)=2 m_epsilon(theta0)`. Substitution into (2) proves

\[
 -\mathcal L_\varepsilon'(0)
       =4\|m_\varepsilon(\theta_0)\|_2^2
       =4\|V\|_2^2\varepsilon^4+o(\varepsilon^4).
 \tag{17}
\]

In particular, for every sufficiently small positive epsilon the initialized
flow immediately lowers the loss, despite the diverging fixed-threshold
delay.

## Claim boundary and excluded mechanisms

Proved:

* Every positive epsilon in the geometric family is genuinely admissible;
  balanced labels and positive masses are retained.
* The exact initialized initial slope has order epsilon^4.
* A fixed loss reduction takes at least order epsilon^-2 physical time.
* For times `o(epsilon^-2)`, the complete raw state displacement tends to
  zero, and the loss stays near one; all moving blocks are included.
* A geometry-uniform exponential loss bound, or any geometry-uniform
  vanishing loss envelope, is impossible.
* Exact initialized stationarity is excluded for all sufficiently small
  positive members, by (17). The coincident epsilon=0 limit is stationary
  at loss one, but is not an admissible three-independent-input example.

Not proved or inferred:

* A positive asymptotic loss floor at any positive epsilon.
* Failure of data-dependent exponential terminal convergence.
* A matching upper bound on the hitting time, or epsilon^-4 as a hitting-time
  lower bound. The initial slope alone does not imply the latter.
* Convergence to an actual trained-network limit in general dimension.
* A certified practical numerical size for the prefactor in (6).

The main surviving alternative is eventual full fitting after a long delay.
The proof leaves it fully viable. Its negative result concerns uniformity
over genuine three-input geometries, not terminal failure at fixed data.

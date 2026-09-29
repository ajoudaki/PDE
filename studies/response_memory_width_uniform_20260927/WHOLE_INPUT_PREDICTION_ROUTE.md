# Whole-input prediction: what the norm estimate transfers, and what it does not

28 September 2026. Scoped internal continuation. This report concerns prediction
and test RMSE, with exactly zero initial readout, fixed positive small label RMS
`Y`, tanh, fixed finite depth/data, canonical Gaussian initialization, and the
positive initial readout-feature Gram of the assigned sources. It neither
constructs nor assumes without notice a population closure limit. It proves
deterministic observation inequalities that can be applied to a valid population
comparison, and records separately the unconditional finite-array consequence.

The assigned scientific inputs read completely were
`SLOW_ORDER_UNIFORM_BOUND.md`, `SLOW_ORDER_GAUSSIAN_ROUTE.md`,
`SMALL_LABEL_GAUSSIAN.md`, `GENERAL_AUTONOMOUS_SYNTHESIS.md`, and
`docs/notation.qmd`. No other study, archived book, external source, experiment,
or further agent was used. Required process inputs were the
`investigate-conjectures` skill and its research-contract, evidence-ledger and
adversarial-audit references, and `solve-math-rigorously`.

## 1. Current conclusion and the population qualification

Write `f_D(t,x)` for the dense population predictor and `f_q(t,x)` for a
population closure predictor **when that object has independently been
constructed and has the comparison bounds below**. Let

\[
 D_q=\sup_{t\ge0}d(\theta_q(t),\theta_D(t)),\qquad
 r(x)=\|x\|_2/\sqrt d.
 \tag{1}
\]

Here `d` is the assigned sum norm: first-row `L2(R^d)`, learned hidden
Hilbert--Schmidt differences, and readout `L2`. For two such trajectories on
the common small-label physical ball, there are constants `C,B`, independent
of `q,t,x`, with `B<=C_0Y`, such that

\[
 \sup_{t\ge0}|f_q(t,x)-f_D(t,x)|
       \le \min\{2B,\; C r(x)D_q\}.                         \tag{2}
\]

The factor `1+r(x)` can be replaced by `r(x)` because the prescribed network
has no biases and tanh vanishes at zero. In particular both predictors are
exactly zero at the origin.

Thus every fixed compact input set `K` obeys the all-time supremum estimate
`sup_(t>=0,x in K)|f_q-f_D|<=min(2B,C R_K D_q)`, where
`R_K=sup_(x in K)||x||/sqrt(d)`. The constant is allowed to depend on that
fixed set; this is not a supremum estimate uniform as `R_K` tends to infinity.

For any fixed test probability measure `mu` on the entire `R^d`, define

\[
 \Psi_\mu(s)=
 \left[\int_{\mathbb R^d}
           \min\{4B^2,C^2r(x)^2s^2\}\,\mu(dx)\right]^{1/2}.
 \tag{3}
\]

Then

\[
 \sup_{t\ge0}\|f_q(t,\cdot)-f_D(t,\cdot)\|_{L^2(\mu)}
       \le\Psi_\mu(D_q),\qquad \Psi_\mu(s)\longrightarrow0
       \quad(s\downarrow0).                              \tag{4}
\]

No moment assumption on `mu` is needed for convergence in (4). A numerical
rate in terms of `s` requires information about that fixed law's tails. For
finite second moment, (4) simplifies to

\[
 \sup_{t\ge0}\|f_q-f_D\|_{L^2(\mu)}
 \le C\left(\frac{\mathbb E_\mu\|X\|_2^2}{d}\right)^{1/2}D_q.
 \tag{5}
\]

Consequently a legitimate all-time population comparison

\[
 D_q\le A_q:=\frac{C_1}{q}
       \exp\!\bigl(K\sqrt{\log(e+q)}\bigr)                 \tag{6}
\]

would give exactly the same near-one order envelope for test prediction in
`L2(mu)` for every finite-second-moment test distribution, including laws with
unbounded support. For every fixed `0<gamma<1`, the error is then at most
`C_(mu,gamma) q^-gamma`. This conclusion is an observation theorem conditional
only on the population objects and comparison (6); the finite-width result
alone must not be renamed a theorem constructing those objects.

An unweighted `sup_(x in R^d)` vanishing bound is stronger than (4)--(5).
The assigned estimates do not currently prove it. Section 5 gives a sufficient
trained-first-row anti-concentration condition and its optimal feature-level
exponent. Section 6 shows exactly why Gaussian initialization and small `L2`
first-row motion do not by themselves verify that condition. That example
invalidates an implication between a priori bounds; it is not a counterexample
to actual dense or closure trajectories.

## 2. Proof of the pointwise envelope

The following argument is deterministic and applies equally to a common
population realization and to two same-width networks sharing initialization.
In the latter case every `L2` field norm is the ordinary vector norm divided
by `sqrt(n)`, as in the notation contract.

Let `H_ell(x)` and `Hhat_ell(x)` be the population features of two states. Assume
that all hidden operator norms are at most `R`, all first-row vector-valued
`L2` norms are at most `F`, and all readout `L2` norms are at most `B`. These
bounds are provided by the small-label physical estimates, with fixed
`F,R`. Set

\[
 a_1=\|\widehat W_1-W_1\|_{L^2(\mathbb R^d)},\quad
 a_\ell=\|\widehat W_\ell-W_\ell\|_{\rm HS}\;(2\le\ell\le L),
 \quad a_w=\|\widehat w-w\|_2,
 \quad d_*=a_1+\sum_{\ell=2}^L a_\ell+a_w.
 \tag{7}
\]

Because `|tanh(v)|<=min(1,|v|)`,

\[
 \|H_1(x)\|_2\le Fr(x),\qquad
 \|H_\ell(x)\|_2\le R^{\ell-1}Fr(x),\qquad
 \|H_\ell(x)\|_2\le1,                                    \tag{8}
\]

and the same bounds hold for the hatted state. Tanh is one-Lipschitz, so

\[
 \|\widehat H_1(x)-H_1(x)\|_2\le r(x)a_1.                 \tag{9}
\]

For each later layer, subtract the two linear preactivations as

\[
 \widehat W_\ell\widehat H_{\ell-1}-W_\ell H_{\ell-1}
 =\widehat W_\ell(\widehat H_{\ell-1}-H_{\ell-1})
       +(\widehat W_\ell-W_\ell)H_{\ell-1}.
\]

The operator norm is bounded by the Hilbert--Schmidt norm for the difference
operator. Therefore

\[
 \|\widehat H_\ell-H_\ell\|_2
 \le R\|\widehat H_{\ell-1}-H_{\ell-1}\|_2
       +a_\ell R^{\ell-2}Fr(x).
 \tag{10}
\]

Induction yields `||Hhat_L-H_L||_2<=C_(F,R,L) r(x)
(a_1+...+a_L)`. Split the readout pairing into the changed readout and changed
feature. Cauchy--Schwarz and (8) give

\[
 |\widehat f(x)-f(x)|
 \le a_w\|\widehat H_L(x)\|_2+B\|\widehat H_L(x)-H_L(x)\|_2
 \le C r(x)d_* .                                          \tag{11}
\]

Every feature has `L2` norm at most one, so both predictions have magnitude
at most `B`, giving the other bound `2B` in (2). The proof is uniform in
physical time whenever the physical bounds are.

The label scaling of `B` also has a direct pointwise proof. From zero initial
readout,

\[
 w(t)=-\frac2m\sum_a\int_0^t r_a(s)H_{L,a}(s)\,ds.
\]

Since each feature has absolute value at most one and
`m^-1 sum_a |r_a|<=rho`, one has `|w(t,omega)|<=2 int_0^t rho` for almost
every coordinate. The common all-time activity bound gives `||w||_infinity
<=CY`, for both paths whenever their activity bounds hold. In particular
the required readout `L2` and prediction bounds have `B<=CY`.

## 3. Test laws, weighted suprema, and RMSE

Squaring the pointwise inequality (2), integrating, and then taking the time
supremum proves (4). The integrand in (3) tends pointwise to zero as `s` tends
to zero and is bounded by the integrable constant `4B^2`, which proves the
convergence by bounded dominated integration.

For each `0<p<=2`, the elementary inequality
`min(u^2,v^2)<=u^(2-p)v^p` for nonnegative `u,v` gives

\[
 \Psi_\mu(s)
 \le (2B)^{1-p/2}(Cs)^{p/2}
       \left(\mathbb E_\mu r(X)^p\right)^{1/2}.             \tag{12}
\]

Thus finite `p`th moment, for `p<2`, supplies an exponent `p/2` of the parameter
envelope. At `p=2` it is (5). Higher moments do not improve the linear
observation estimate (5), although they can be useful for other arguments.

Without a moment assumption, every radius `R_0>0` gives the explicit tail
bound

\[
 \Psi_\mu(s)^2\le
 C^2s^2\int_{r(x)\le R_0}r(x)^2\,\mu(dx)
       +4B^2\mu\{r(X)>R_0\}.                              \tag{13}
\]

One can minimize (13) over `R_0`, or retain the sharper envelope (3). The
result is for one fixed test law; it is not a rate uniform over every
probability law. The bounded envelope alone allows a test law to put its
mass at radii beyond `1/s`, so its supremum over all laws need not vanish.

Equation (11) also proves the whole-space weighted bounds

\[
 \sup_{t\ge0,\;x\ne0}
       \frac{|f_q(t,x)-f_D(t,x)|}{r(x)}\le CD_q,
 \qquad
 \sup_{t\ge0,x}
       \frac{|f_q(t,x)-f_D(t,x)|}{1+r(x)}\le CD_q.           \tag{14}
\]

The first uses the natural zero value at the origin; the second is a bounded
weight formulation that does not require division by zero. Neither is an
unweighted supremum over all inputs.

For any fixed target `g in L2(mu)`, let
`RMSE_mu(f,g)=||f-g||_(L2(mu))`. The reverse triangle inequality gives, for
every `t`,

\[
 |\operatorname{RMSE}_\mu(f_q(t),g)
          -\operatorname{RMSE}_\mu(f_D(t),g)|
 \le\|f_q(t)-f_D(t)\|_{L^2(\mu)}.                         \tag{15}
\]

Combining with (4), (5), or (12) proves the corresponding all-time difference
of test RMSEs. The same proof applies to a joint test distribution `(X,Z)`
with square-integrable target `Z`. This compares the two risks; it does not
bound either risk by a small number independently of the target.

## 4. What is unconditional from the supplied finite-width theorem

The provided slow-order theorem establishes, on events of probability tending
to one, simultaneously for all positive integer orders,

\[
 E_n(q)=\sup_{t\ge0}d_n(\widehat\theta_{n,q},\theta_n^D)
       \le A_q+b_n,\qquad b_n\longrightarrow0
           \quad\hbox{in probability}.                    \tag{16}
\]

Here `A_q` has the form (6), and `b_n` depends only on dense trajectories and
initialized arrays. Intersect these events with a fixed Gaussian first-row
RMS bound if that bound was not already included; this still has probability
tending to one, and first-row total variation preserves a fixed `F` above.
The deterministic proof above immediately yields

\[
 \sup_{t\ge0}\|\widehat f_{n,q}(t)-f_n^D(t)\|_{L^2(\mu)}
       \le\Psi_\mu(A_q+b_n).                              \tag{17}
\]

The function `Psi_mu` is increasing. It is also subadditive: pointwise
`min(2B,C r(s+t))<=min(2B,Crs)+min(2B,Crt)`, and the `L2` triangle inequality
then gives `Psi_mu(s+t)<=Psi_mu(s)+Psi_mu(t)`. Thus the right side of (17)
is at most `Psi_mu(A_q)+Psi_mu(b_n)`, with `Psi_mu(b_n)->0` in probability.
For second-moment laws this is the explicit decomposition
`C_mu A_q+C_mu b_n`.

There is also an all-time dense-to-population test error

\[
 s_{n,\mu}=\sup_{t\ge0}
       \|f_n^D(t)-f_D(t)\|_{L^2(\mu)}\longrightarrow0
           \quad\hbox{in probability}                    \tag{18}
\]

for every fixed probability law `mu`. To see the all-time and unbounded-input
steps without asserting uniform unweighted input convergence, first fix a
finite input ball and finite physical horizon. The supplied dense population
construction and the finite-input-net argument in
`GENERAL_AUTONOMOUS_SYNTHESIS.md` give uniform convergence there. The common
bounded prediction magnitude controls the complement of the input ball by
`2B sqrt(mu{r>R_0})`. For the time tail, dense total variation after time `T`
is at most `C exp(-lambda T)` in the physical sum norm, both at finite width
on the good event and in the population. Applying (2) separately to the two
dense times bounds each dense time tail in `L2(mu)` by
`Psi_mu(C exp(-lambda T))`. This tends to zero as `T` grows. Choose the input
ball and `T` first for a desired error, then let width grow in the fixed
compact comparison. This proves (18).

Consequently the construction-free population-reference consequence is

\[
 \sup_{t\ge0}\|\widehat f_{n,q}(t)-f_D(t)\|_{L^2(\mu)}
       \le\Psi_\mu(A_q+b_n)+s_{n,\mu}.                    \tag{19}
\]

In particular every deterministic sequence `q_n->infinity` makes (19) tend
to zero in probability. This remains a finite closure compared with a dense
population. A fixed-order population closure or its uniqueness does not
follow from (16)--(19). If a population closure is independently shown to be
a suitable fixed-order limit, (19) passes the corresponding prediction
envelope to that limit; the existence/identification step must be stated.

## 5. Optional diagnostic: conditional unweighted whole-space transfer

Let `A(t,omega) in R^d` be the **trained dense first row**. Define its uniform
hyperplane concentration function

\[
 \mathcal A(s)=\sup_{t\ge0}\sup_{u\in\mathbb S^{d-1}}
       \Pr\{|A(t)\mathbin{\cdot}u|\le s\},\qquad s>0.
 \tag{20}
\]

This is a distributional property of the actual reference row after training,
not of its initialization. Let `a_1(t)` be the first-row `L2` discrepancy.
For every `s>0`,

\[
 \sup_{t\ge0,x}\|H_{1,q}(t,x)-H_{1,D}(t,x)\|_2
       \le C\left\{\sqrt{\mathcal A(s)}+D_q/s\right\}.
 \tag{21}
\]

Here and below the feature norm is over the population coordinate and the
input supremum is outside that norm. This is the correct orientation for the
subsequent forward operator bounds.

To prove (21), first note the scalar inequality, valid for all real `a,b` and
all `v>=0`,

\[
 |\tanh(v(a+b))-\tanh(va)|
       \le C\min\{1,|b|/|a|\}\quad(a\ne0).               \tag{22}
\]

If `|b|>=|a|/2`, boundedness of tanh proves (22), enlarging `C` to at least
four. Otherwise every point between `a` and `a+b` has magnitude at least
`|a|/2` and has the same sign. The mean value theorem gives an upper bound
`v|b| sech^2(v|a|/2)`. Since `sup_(z>=0) z sech^2(z/2)` is finite, this is
at most `C|b|/|a|`. This proves (22), including `v=0`.

For a nonzero test input write `x/sqrt(d)=v u`. Substitute
`a=A(t) dot u`, `b=(W_(1,q)(t)-A(t)) dot u` into (22). On `|a|<=s` use the
bound two; on the complement use `C|b|/s`. Squaring and integrating gives

\[
 \|H_{1,q}(t,x)-H_{1,D}(t,x)\|_2^2
       \le4\mathcal A(s)+C a_1(t)^2/s^2.                  \tag{23}
\]

Taking square roots and suprema proves (21). Higher features now satisfy
the same recurrence (10), but use their bound one in its second term. The
readout split therefore gives

\[
 \sup_{t\ge0,x}|f_q(t,x)-f_D(t,x)|
 \le C\left[D_q+B\inf_{s>0}
          \left\{\sqrt{\mathcal A(s)}+D_q/s\right\}\right].
 \tag{24}
\]

The first `D_q` controls readout and hidden-operator differences. Constants
can absorb fixed `B`, but keeping it displayed explains the small-label
amplitude. If `mathcal A(s)->0`, (24) is a qualitative vanishing unweighted
supremum bound: first fix a small `s`, then let `D_q` tend to zero.

If the stronger uniform slab estimate

\[
 \mathcal A(s)\le A_0s^\alpha\quad(0<s\le1),\qquad\alpha>0,
 \tag{25}
\]

is independently available, choose `s=D_q^(2/(alpha+2))` for `0<D_q<=1`.
Then (24) yields

\[
 \sup_{t\ge0,x}|f_q(t,x)-f_D(t,x)|
       \le C D_q^{\alpha/(\alpha+2)}.                     \tag{26}
\]

For a uniform bounded density of every unit projection, `alpha=1`. Combining
with (6) would give

\[
 \sup_{t\ge0,x}|f_q-f_D|
 \le Cq^{-1/3}\exp\!\left(\frac K3\sqrt{\log(e+q)}\right)
       \le C_\gamma q^{-\gamma}\quad(0<\gamma<1/3).        \tag{27}
\]

This is conditional: (25) for trained first rows has not been proved by the
assigned scientific inputs. It would imply the same rate for every test
probability law simultaneously, with no moments, by bounding `L2` by the
unweighted supremum.

The exponent one-third is optimal for (21) given only bounded reference
projection density and `L2` perturbation size. For `G~N(0,1)`, put
`b_h=-2G 1_(|G|<=h)`. As `h` tends to zero,

\[
 \|b_h\|_2^2=4\mathbb E[G^2\mathbf1_{|G|\le h}]
                  \asymp h^3,
\]

whereas, by bounded dominated convergence as `v->infinity`,

\[
 \|\tanh(v(G+b_h))-\tanh(vG)\|_2^2
       \longrightarrow4\Pr\{|G|\le h\}\asymp h.
 \tag{28}
\]

Thus first-feature error can be of order `||b_h||_2^(1/3)`. This is sharpness
of the feature observation lemma, not an optimality theorem for actual
closure prediction rates. Extra structure of readout, Gaussian actions,
the discrepancy, or the reachable trajectories might improve prediction.

## 6. Why small Gaussian first-row movement is insufficient

The assigned small-label bounds give

\[
 \sup_{t\ge0}\|A(t)-G\|_{L^2(\mathbb R^d)}\le\varepsilon,
       \qquad\varepsilon\le CY^2,
 \tag{29}
\]

with `G~N(0,I_d)`. For every `h>0`, a union bound and the scalar Gaussian
density bound give

\[
 \mathcal A(s)
 \le \sqrt{2/\pi}(s+h)+\varepsilon^2/h^2.                 \tag{30}
\]

Indeed, if `|A dot u|<=s` and `|(A-G) dot u|<=h`, then
`|G dot u|<=s+h`. The complement has probability at most
`epsilon^2/h^2` by the elementary second-moment bound. Setting
`h=epsilon^(2/3)` when `epsilon<=1` gives only

\[
 \mathcal A(s)\le C\{s+\varepsilon^{2/3}\}.              \tag{31}
\]

Putting this in (24) and choosing `s=D_q^(2/3)` yields a bound with a fixed
label-dependent floor, of size at most
`C[D_q+B D_q^(1/3)+B epsilon^(1/3)]`. Since `Y` is fixed and positive,
that floor does not vanish as `q` increases. Sending `Y` to zero would change
the user's fixed-label problem.

The failure to remove the floor is real for the ambient assumptions. In one
dimension fix a small `h>0` and define

\[
 A=G\mathbf1_{|G|>h},\qquad
 A_\eta=A+\eta\operatorname{sgn}(G)\mathbf1_{|G|\le h}.
 \tag{32}
\]

Then `||A-G||_2` is of order `h^(3/2)`, so `A` is arbitrarily close in `L2`
to a Gaussian row, but it has an atom of mass `p_h=Pr{|G|<=h}` at zero.
Also `||A_eta-A||_2=eta sqrt(p_h)->0`. Nevertheless

\[
 \lim_{v\to\infty}
 \|\tanh(vA_\eta)-\tanh(vA)\|_2=\sqrt{p_h}
       \quad\hbox{for every }\eta>0.                      \tag{33}
\]

Even a bounded readout can turn this into prediction error. Choose the same
readout `w=Y sgn(G)` for both one-hidden-layer feature maps. The contributions
off the slab agree, and on the slab

\[
 \lim_{v\to\infty}
  \mathbb E\bigl[w\{\tanh(vA_\eta)-\tanh(vA)\}\bigr]
       =Yp_h>0.                                          \tag{34}
\]

Both predictions are uniformly bounded by `Y`, their first-row distance
tends to zero, and their reference first row can obey an arbitrarily small
Gaussian-motion bound. Their unweighted prediction supremum does not tend
to zero. This example is deliberately an ambient feature/readout construction;
it is not claimed to solve the canonical training equations or the old-clock
closure, and it does not replace the fixed-depth canonical model by a
counterexample in a different model. It proves that the currently stated
physical bounds alone cannot justify the missing anti-concentration step.

At radius `v->infinity`, tanh approaches the sign function except at zero.
This is why bounded tanh is not enough to make the whole-space observation map
uniformly continuous in the physical `L2` first-row norm. The missing input
is a property of trained hyperplanes, not a larger compact-input Lipschitz
constant. Smoothness or absolute continuity at each fixed finite time, if
proved, would still need a bound uniform through the terminal time and over
all directions for (25).

## 7. Claim record and remaining obligation

| Claim | Status in this report | Exact scope |
|---|---|---|
| Bounded pointwise envelope (2) | Proved | Any compared states on the common physical ball |
| All-time `L2(mu)` and RMSE transfer (4)--(15) | Proved | Any fixed test law; rates depend on its moments/tails |
| Finite closure to dense population (19) | Proved relative to assigned inputs | No fixed-order population closure construction asserted |
| Population `q^-1 exp(K sqrt(log q))` test rate | Conditional | Requires a valid global population closure and comparison (6) |
| Unweighted whole-space rate (26)--(27) | Conditional | Also requires trained dense first-row slab control (25) |
| Gaussian initialization plus small `L2` motion implies slab control | Falsified as an ambient implication | Explicit collapse construction (32) |
| Actual canonical unweighted whole-space prediction convergence | Open in the assigned inputs | Ambient counterexample does not decide actual dynamics |

For the requested test RMSE under a specified finite-second-moment law, no
trained-first-row anti-concentration theorem is needed: establishing the
population comparison is the only extra bridge. For a supremum over every
input, or one error bound uniform over every possible test law, a quantitative
trained-hyperplane estimate or another dynamical observation argument remains
necessary. No exact all-time `C/q` endpoint, explicit width concentration
rate, or fixed-order population-closure uniqueness is claimed here.

# All-time test prediction against the dense population, and the fixed-order gap

28 September 2026. Scoped analytic continuation; no experiment, external
search, additional delegation, or maintained-book change. This note uses the
unchanged autonomous old-clock closure with exactly zero initial readout.
The mathematical-proof and conjecture-audit skills were applied.

**Conclusion.** The supplied all-time finite-network estimate gives an
all-time, whole-compact-input approximation of the unique dense population
predictor, with order envelope
`q^-1 exp(K sqrt(log(e+q)))` and a vanishing dense-only width floor.
There are also bounds for every fixed test probability law, and a weighted
supremum bound over the whole input space. Neither the supplied results nor
the arguments below construct a unique population old-clock closure at each
fixed order. A population-versus-population assertion is therefore stated
conditionally, separately from the proved finite-closure/population-target
theorem. Subsequence limits of predictor laws exist, but they are not thereby
identified with a population closure equation.

## 1. Model, imported statements, and observables

Fix the data, input dimension `d`, sample count `m`, depth `L`, tanh,
canonical Gaussian initialization, mobilities `(n,1,...,1,n)`, unhalved
mean squared loss, and exactly zero stored readout. There are no biases.
Assume the positive initial readout-feature Gram gap and the common
small-label hypotheses of `SMALL_LABEL_GAUSSIAN.md` and
`SLOW_ORDER_UNIFORM_BOUND.md`. The label RMS `0<Y<=Y_*` is fixed as width
and order vary. All same-width paths share their actual initialized arrays.

Write `f_n^D(t,x)` for the finite dense predictor, `f_D(t,x)` for the
unique global strong dense population predictor, and `fhat_(n,q)(t,x)`
for the actual finite autonomous old-clock predictor. The order `q>=1`
is the number of retained moments, called `P` in the older notes.

Let `G_n` be the initialization event of the slow-order theorem,
intersected with a fixed sufficiently large bound on
`||W_(0,1)||_F/sqrt(n)`. The extra event has probability tending to one,
because `d` is fixed and the first rows are Gaussian. No concentration
rate is needed. The symbol `G_n` below denotes this intersection.

The following are the precise supplied inputs.

1. On `G_n`, all dense and closure paths have common all-time hidden
   operator bounds, a common first-row RMS bound, and a readout RMS bound
   `B<=C Y`. In particular all their predictions are bounded by `B`,
   uniformly over every input. The population has the same bounds after
   enlarging the constants. The first-row bound follows also by adding
   its bounded total variation to the imposed initial RMS bound.
2. `SMALL_LABEL_GAUSSIAN.md`, Sections 2--4, constructs the unique global
   dense population and identifies the finite dense flow on every fixed
   compact physical interval, with passive forward probes available by
   the maintained C.1 fixed-program construction.
3. For the normalized parameter distance from
   `SLOW_ORDER_UNIFORM_BOUND.md`, simultaneously for every `q` on `G_n`,

   \[
   E_n(q):=\sup_{t\ge0}d_n(\widehat\theta_{n,q}(t),\theta_n^D(t))
       \le A(q)+b_n,\qquad
   A(q)=\frac Cq\exp\!\left(K\sqrt{\log(e+q)}\right),
   \tag{1}
   \]

   where `b_n>=0` tends to zero in probability and is constructed from
   dense empirical carrier tails only. Its value may be set to zero
   outside `G_n`. For each `gamma<1`, `A(q)<=C_gamma q^-gamma`.
4. For finite dense paths on `G_n` and for the population dense path,

   \[
   \int_T^\infty\|\dot\theta_D(s)\|_{\rm sum}\,ds
       \le C e^{-\lambda T},\qquad T\ge0.
   \tag{2}
   \]

   At finite width the norm is the maintained normalized parameter
   norm; at population it is row `L2`, hidden increment Hilbert--Schmidt,
   and readout `L2`. Equation (2) follows from the uniform velocity bound
   `||F||_sum<=V rho_D` and the dense exponential residual decay.

Constants can depend on the fixed data, depth, Gram gap, initialization
bounds and fixed small-label regime. They do not depend on `n,q,t`.
No norm between a finite array and a population operator is defined.
All cross-width comparisons below are comparisons of scalar predictions.

For a test law `mu` and `1<=p<infinity`, the particularly strong test error
used below is

\[
 \mathcal D_{\mu,p}(g,h)
 =\left(\int\sup_{t\ge0}|g(t,x)-h(t,x)|^p\,d\mu(x)\right)^{1/p}.
 \tag{3}
\]

This controls `sup_t ||g(t,.)-h(t,.)||_(L^p(mu))`. Supremum measurability
follows by taking rational times, since all prediction paths are continuous.
The test law is fixed as `n,q` vary and is not chosen after seeing the
initialization.

## 2. Direct forward comparison, including the origin

Put `r(x)=||x||/sqrt(d)`. On the common physical ball, zero biases and
`tanh(0)=0` give, for both finite states being compared,

\[
 \|h_\ell(x)\|_2/\sqrt n\le\min\{1,C_\ell r(x)\}.
 \tag{4}
\]

For the first layer use `|tanh u|<=min(1,|u|)` and the full first-row
RMS bound. At each later layer multiply the preceding RMS bound by
the hidden operator norm, and retain separately the coordinate bound
`|h_ell|<=1`. The same reasoning works in each population `L2` space.

For two same-array finite physical states let `d` denote their normalized
parameter distance and put `e_ell=||hhat_ell(x)-h_ell(x)||_2/sqrt(n)`.
The Lipschitz tanh inequality, followed by splitting the matrix product,
gives

\[
 e_1\le r(x)\|\widehat W_1-W_1\|_F/\sqrt n,
 \qquad
 e_\ell\le K_\ell e_{\ell-1}
     +\|\widehat W_\ell-W_\ell\|_F
                         \|h_{\ell-1}(x)\|_2/\sqrt n.
 \tag{5}
\]

Consequently `e_L<=C r(x)d`. At the readout, the exact split and
Cauchy--Schwarz give

\[
 \begin{split}
 |\widehat f(x)-f(x)|
 &\le \|\widehat w-w\|_2/\sqrt n\,
                      \|\widehat h_L(x)\|_2/\sqrt n+B e_L\\
 &\le C r(x)d.
 \end{split}
\]

The separate output bound gives the useful clipped form

\[
 \sup_{t\ge0}|\widehat f_{n,q}(t,x)-f_n^D(t,x)|
 \le\min\{2B,C r(x)E_n(q)\}.
 \tag{6}
\]

In particular there is no constant error at `x=0`: both predictors are
exactly zero there. This sharper spatial factor was also identified by
the coordinator during this scoped continuation. It improves the test
moment dependence, without improving the order exponent in (1).

For one path, the same forward estimate bounds prediction increments by
`C r(x)` times the parameter increment. Also, comparing two inputs in
one state gives

\[
 |f(t,x)-f(t,z)|\le C\|x-z\|/\sqrt d.
 \tag{7}
\]

The constants in (6)--(7) hold for every input, without a sampled test
net or a test backward-carrier tail assertion.

## 3. Dense finite-to-population convergence is uniform for all time

**Proposition.** For every finite `R`, with `K_R={x:r(x)<=R}`,

\[
 s_{n,R}:=\sup_{t\ge0,x\in K_R}|f_n^D(t,x)-f_D(t,x)|
       \longrightarrow0\quad\hbox{in probability on }G_n.
 \tag{8}
\]

For precise unrestricted random variables define `s_(n,R)=0` outside
`G_n`; all inequalities involving it are asserted on `G_n`.

*Proof.* At any fixed finite set of test inputs, append passive forward
queries to the finite Gaussian programs in maintained C.1 and the global
construction of `SMALL_LABEL_GAUSSIAN.md`. Use the full first-row root,
so all training and test inputs use the same weights. These queries do
not enter the residual or updates. Fixed-program joint moment convergence,
and the forward estimate against the same-array proxy, identify their
predictions uniformly on any fixed `[0,T]`. This is the passive-probe
argument already recorded in `GENERAL_AUTONOMOUS_SYNTHESIS.md`, Section 3.

Choose a finite `epsilon`-net of `K_R`. Equation (7) bounds the difference
between the prediction error at any input and at its nearest net point
by `2C epsilon`. Convergence on the finite net and a union bound therefore
give

\[
 \sup_{t\le T,x\in K_R}|f_n^D(t,x)-f_D(t,x)|
       \longrightarrow0\quad\hbox{in probability}.
 \tag{9}
\]

For `t>=T`, apply (2) and the one-path version of (5)--(6) to each dense
path between `T` and `t`. Thus, on `G_n`,

\[
 \begin{split}
 \sup_{t\ge0,x\in K_R}|f_n^D(t,x)-f_D(t,x)|
 &\le\sup_{t\le T,x\in K_R}|f_n^D(t,x)-f_D(t,x)|
          +C_R e^{-\lambda T}.
 \end{split}
 \tag{10}
\]

First choose `T` to make the last term small; next use (9) at that fixed
`T`. Finally `Pr(G_n^c)->0` removes the initialization restriction in
the convergence-in-probability statement. No growing-horizon application
of the compact-time theorem has occurred. This proves (8). The same
argument includes the dense terminal predictions because both dense
parameter paths have strong endpoints by finite total variation. `QED`.

The statement only requires uniform vanishing of the tails in (2).
Finite total activity separately for each width, with no uniform tail
modulus, would not justify (10) with a common small remainder.

## 4. The population-target test theorem

Combining (1), (6), and (8), on `G_n` and simultaneously for all `q>=1`,

\[
 \sup_{t\ge0,x\in K_R}
       |\widehat f_{n,q}(t,x)-f_D(t,x)|
 \le C R A(q)+\underbrace{C R b_n+s_{n,R}}_{\beta_{n,R}},
 \qquad \beta_{n,R}\longrightarrow0\quad\hbox{in probability}.
 \tag{11}
\]

The floor `beta_(n,R)` depends only on dense paths, initialization, and
the deterministic dense population target. It is independent of closure
order and of all closure trajectories. No rate in width has been proved.

In particular every deterministic `q_n->infinity` satisfies

\[
 \sup_{t\ge0,x\in K_R}
       |\widehat f_{n,q_n}(t,x)-f_D(t,x)|
             \longrightarrow0\quad\hbox{in probability}.
 \tag{12}
\]

This is a statement about the full continuum of inputs in `K_R` and all
physical times. It is not restricted to the training set. Every fixed
`gamma<1` can replace `A(q)` in (11) by `C_gamma q^-gamma`, with the
same qualitative width floor. The sharper compact-time exponents below
two in `GENERAL_AUTONOMOUS_SYNTHESIS.md` do not replace this all-time
envelope; their constants have not been bounded uniformly as `T` grows.

### A weighted whole-input theorem

Define `w(x)=1+r(x)` and

\[
 s_{n,w}=\sup_{t\ge0,x\in\mathbb R^d}
          \frac{|f_n^D(t,x)-f_D(t,x)|}{w(x)}
 \quad\hbox{on }G_n,
 \tag{13}
\]

and set it to zero outside `G_n`. On `r(x)>R` the quotient is at most
`2B/(1+R)`, whereas on `K_R` it is at most `s_(n,R)`. Choosing `R`
large, then using (8), proves `s_(n,w)->0` in probability. Since
`r/(1+r)<=1`, (1) and (6) imply

\[
 \sup_{t\ge0,x\in\mathbb R^d}
 \frac{|\widehat f_{n,q}(t,x)-f_D(t,x)|}{1+\|x\|/\sqrt d}
 \le C A(q)+\underbrace{C b_n+s_{n,w}}_{\beta_{n,w}},
 \qquad\beta_{n,w}\longrightarrow0.
 \tag{14}
\]

This is a weighted whole-space supremum. An unweighted supremum over
unbounded `R^d` has not been obtained. Compact convergence, uniform output
bounds, and uniform input Lipschitz constants alone do not imply it:
`tanh(epsilon x)` converges to zero locally uniformly, with uniform boundedness
and Lipschitz bounds, but has whole-line supremum one. This is a diagnostic
of that implication, not a counterexample to the present Gaussian dynamics.
On a compact input domain, (11) is already an unweighted whole-domain bound.

## 5. Test laws, input moments, test probabilities, and risk

Fix any Borel probability measure `mu` on `R^d` and `1<=p<infinity`.
The dense-only error

\[
 s_{n,\mu,p}=\mathcal D_{\mu,p}(f_n^D,f_D)
 \quad\hbox{on }G_n
 \tag{15}
\]

is set to zero outside `G_n` and tends to zero in probability. Indeed

\[
 s_{n,\mu,p}^p\le s_{n,R}^p+(2B)^p\mu\{r>R\}.
 \tag{16}
\]

Every probability measure on `R^d` has `mu{r>R}->0`. Choose `R` first,
then use (8). No input moment is needed for this conclusion.

Define the explicit, law-dependent modulus

\[
 \Psi_{\mu,p}(u)
 =\left(\int\min\{2B,C r(x)u\}^p\,d\mu(x)\right)^{1/p},
 \qquad u\ge0.
 \tag{17}
\]

It is increasing, vanishes at zero, and tends to zero as `u` tends to zero
by bounded convergence. Also
`min(a,c(u+v))<=min(a,cu)+min(a,cv)`; Minkowski consequently makes
`Psi` subadditive for `p>=1`. The pointwise all-time bound (6), the
triangle inequality in (3), and (1) prove

\[
 \begin{split}
 \mathcal D_{\mu,p}(\widehat f_{n,q},f_D)
 &\le\Psi_{\mu,p}(A(q))+
       \underbrace{\Psi_{\mu,p}(b_n)+s_{n,\mu,p}}_{\beta_{n,\mu,p}},\\
 &\hspace{16mm}\beta_{n,\mu,p}\longrightarrow0
                              \quad\hbox{in probability}.
 \end{split}
 \tag{18}
\]

Once again the same floor works for every order. Thus (12) has an
all-time `L^p(mu)` version for every fixed test law, without moments.

If `M_p=(int r^p dmu)^(1/p)<infinity`, then
`Psi_(mu,p)(u)<=C M_p u`. Hence (18) has the explicit deterministic
order term `C M_p A(q)`, including every power below one. If only a
moment of order `0<nu<=p` is finite, use
`min(a,b)^p<=a^(p-nu)b^nu` to obtain

\[
 \Psi_{\mu,p}(u)
 \le (2B)^{1-\nu/p}(C u)^{\nu/p}
            \left(\int r^\nu\,d\mu\right)^{1/p}.
 \tag{19}
\]

For test `L2`, a finite second input moment retains the order envelope;
a finite `nu`th moment with `0<nu<2` gives its `nu/2` power. These are
upper bounds, not asserted sharpness results for the neural dynamics.

For test probability, condition on any initialization in `G_n`. Markov's
inequality applied to (3) gives, simultaneously for all `q`,

\[
 \mu\!\left\{x:\sup_{t\ge0}
       |\widehat f_{n,q}(t,x)-f_D(t,x)|>\epsilon\right\}
 \le \min\!\left\{1,
  \frac{[\Psi_{\mu,p}(A(q))+\beta_{n,\mu,p}]^p}{\epsilon^p}
                                                \right\}.
 \tag{20}
\]

If an independent test input has law `mu`, then for every fixed `eta>0`
its joint initialization/test failure probability is at most

\[
 \Pr(G_n^c)+\Pr\{\beta_{n,\mu,p}>\eta\}
 +\min\!\left\{1,
  \frac{[\Psi_{\mu,p}(A(q))+\eta]^p}{\epsilon^p}\right\}.
 \tag{21}
\]

The first two terms vanish as width grows at fixed `eta`. Along any
`q_n->infinity`, (20) also converges to zero in initialization probability.
Its event is simultaneous over physical time for one test input.

For a fixed target function `g in L2(mu)`, set
`RMSE_g(f(t))=||f(t,.)-g||_(L2(mu))`. The norm triangle inequality gives

\[
 \sup_{t\ge0}|\operatorname{RMSE}_g(\widehat f_{n,q}(t))
                   -\operatorname{RMSE}_g(f_D(t))|
 \le\mathcal D_{\mu,2}(\widehat f_{n,q},f_D).
 \tag{22}
\]

The squared risks differ by at most
`2(B+||g||_(L2(mu)))` times the right side. The bounds compare predictors
and their risks; they do not assert small dense test risk against an
unknown target. Nor do convergence-in-probability bounds on `G_n` give
unconditional initialization expectations without controlling the
complement. Input moments and initialization moments are distinct issues.

## 6. What can be called a population closure

### The intended fixed-order population equations

Replacing finite normalized pairings by within-layer expectations gives a
candidate equation on the canonical initialized action spaces. Besides
the first-row field and readout, its state has `tau` and the `q` forward
and backward moment fields for each link and sample. In population notation,

\[
 \begin{split}
 \dot M_k^h&=\rho H-\frac\rho\tau
           \left(kM_k^h+\sum_{j<k}(2j+1)M_j^h\right),\\
 \dot M_k^b&=r\Delta-\frac\rho\tau
           \left(kM_k^b+\sum_{j<k}(2j+1)M_j^b\right),\\
 W^{(\ell)}&=W_0^{(\ell)}-rac2{m\tau}
          \sum_{a,k}(2k+1)M^b_{\ell,a,k}
                              \otimes M^h_{\ell-1,a,k},
 \qquad\dot\tau=\rho.
 \end{split}
 \tag{23}
\]

Here all responses, residuals and moments belong to the candidate's own
state. The outer equations are its own canonical GF equations, and the
initial forward zeroth moment is the initial feature, with all other
moments and the readout initialized as prescribed. Expectations contract
only fields in the same population. Every initialized action retains its
true adjoint. Formula (23) is an unambiguous formal candidate and preserves
the original dynamics; it is not yet an existence theorem.

A fixed number of `L2` fields is still an infinite-dimensional state.
In particular a typical nonlinear difference contains

\[
 [\tanh'(Z)-\tanh'(\widetilde Z)]
                    (W_0^{(\ell+1)})^*\widetilde\Delta.
 \tag{24}
\]

An operator bound and `L2` bounds alone do not make multiplication by
the final carrier Lipschitz in the `L2` difference of the gates. Bounded
gate products give continuity, as in maintained C.1, but continuity of
an infinite-dimensional vector field does not supply the Picard contraction
used for a locally Lipschitz ODE. The finite numerical closure theorem
in maintained `docs/08-autonomous-computation.qmd`, C.4.7.10, concerns a
different finite bounded-mark hierarchy for a two-hidden-layer model; its
own locally Lipschitz proof does not identify (23).

### The available construction attempt stops at a precise missing input

For any fixed `q`, mesh, and finite horizon, the Euler program for (23)
is a legal finite Gaussian computation. It can be placed on common action
spaces by the same countable-union construction as maintained C.1.
The remaining mesh limit requires a mesh-uniform reference-carrier tail
estimate, or another stability/compactness argument strong enough to
control (24). Fixed-program convergence does not supply this uniformity.

The dense C.2 lemma does not literally apply to these programs. Its
assumed hidden update is the current rank-one increment
`-2 h r Delta tensor H`. Equation (23) instead reconstructs the hidden
matrix from evolving projected moment products; differentiating it
produces additional moment-coupling terms. C.2's permission to replace
the scalar residual coefficients or the step lengths does not replace
that hidden update. Extending its response proof would require checking
new causal response recurrences and mesh-uniform bounds, including the
effect of fixed `q` and continuation through finite total activity.
That extension is not proved in any supplied input and is not proved here.

The already-proved closeness to the dense trajectory does not remove this
problem at fixed `q`: it gives a positive error radius `A(q)`, not a radius
that vanishes as width or the closure's Euler mesh is refined. A cutoff
tail transfer from that dense reference retains a positive error floor at
fixed `q`. Such a floor cannot be sent to zero to establish uniqueness
of the closure mesh limit. Nor does being in a small Hilbert-space ball
around a fixed dense trajectory imply strong compactness of all state
paths in that ball.

Thus fixed-order population existence, uniqueness, identification of
actual finite closures with that solution, and a population own-state
restart theorem remain separate open claims in this scoped derivation.
This is a gap in the present proof, not a no-go theorem for the model.

### What output compactness does prove

The actual finite closures do have subsequential *predictor-law* limits
at any fixed order. To make this precise, let
`X=C_loc([0,infinity) x R^d)` with metric

\[
 d_X(g,h)=\sum_{j\ge1}2^{-j}
   \min\{1,\sup_{t\le j,\,r(x)\le j}|g(t,x)-h(t,x)|\}.
 \tag{25}
\]

This is a complete separable metric space. The compact-horizon squared
velocity-defect bound in `GENERAL_AUTONOMOUS_SYNTHESIS.md`, Section 2,
and the bounded dense-form velocity on the common physical ball give

\[
 \int_0^T\|\dot{\widehat\theta}_{n,q}(t)\|_{\rm sum}^2dt
       \le C_T
 \quad\hbox{on }G_n,
 \tag{26}
\]

uniformly in width and order. For any input ball, (5), Cauchy--Schwarz
in time, and (26) give a common one-half Hölder modulus in time.
Equation (7) gives a common input Lipschitz modulus, and `|fhat|<=B`.
On every compact cylinder these are uniform boundedness and
equicontinuity. The Arzela--Ascoli theorem therefore makes their closure
compact there; taking a diagonal subsequence across integer cylinders
makes the corresponding set compact in (25).

For complete control of the rare bad event, define the modified output
to equal zero off `G_n`. Its laws are supported in that common compact
set (including the zero path), so the compact-space probability-measure
subsequence theorem gives a weakly convergent subsequence. The original
and modified laws differ on an event of probability tending to zero,
so they have the same weak subsequential limits. No actual algorithm
has been changed by this auxiliary definition.

Every such limit law is supported on predictions satisfying

\[
 \sup_{t\ge0,x\in\mathbb R^d}
 \frac{|f_q(t,x)-f_D(t,x)|}{1+r(x)}\le C A(q).
 \tag{27}
\]

For a direct justification, fix a finite time/input cylinder and a
positive tolerance `eta`. The probability that its weighted discrepancy
exceeds `C A(q)+eta` tends to zero by (14). The strict-superlevel set
is open for (25); the open-set inequality for weak convergence implies
that the limiting probability of this set is zero. Then intersect the
result over integer cylinders and rational positive tolerances.

This is a limit of scalar predictor laws. It does not prove convergence
of the moment fields, passage to (23), determinism of the limit law,
uniqueness of subsequential limits, or all-time convergence at fixed
`q`. These distinctions prevent a width-first limsup estimate from
being renamed a unique population model.

### Conditional population-versus-population corollary

Suppose a separate argument constructs the intended population old-clock
solution at each fixed `q` and proves that its predictor `f_q` is a
local-uniform probability limit of the actual finite closure predictors.
Then (11), restricted first to finite time/input cylinders and passed to
the limit, gives for every `R`

\[
 \sup_{t\ge0,x\in K_R}|f_q(t,x)-f_D(t,x)|\le C R A(q).
 \tag{28}
\]

The same limit argument, with (6) and (8), yields the sharper pointwise
bound `sup_t |f_q(t,x)-f_D(t,x)|<=min(2B,C r(x)A(q))`, and hence

\[
 \mathcal D_{\mu,p}(f_q,f_D)\le\Psi_{\mu,p}(A(q)).
 \tag{29}
\]

Countably many rational times and rational inputs suffice to pass these
inequalities, after which continuity extends them to all times and
inputs. Thus the all-time error estimate itself needs no additional
all-time convergence hypothesis once fixed-order local identification
has been proved. That identification, and a unique state solving (23),
are the unproved antecedents; (28)--(29) are not asserted unconditionally.

## 7. Direct output comparison and the remaining rate boundary

The direct readout identity used in Section 2 avoids all test backward
carrier multipliers. It is sharper than an undifferentiated parameter
bound in its `r(x)` factor, bounded-output clipping, and test moment
requirements. It introduces no change of dynamics, frozen feature,
supplied trajectory, or new clock. It does not improve the order exponent.

Indeed the unchanged readout equation gives exactly

\[
 \widehat w(t)-w_D(t)
 =-\frac2m\sum_a\int_0^t
 \left[(\widehat r_a-r_{D,a})\widehat h_{L,a}
                 +r_{D,a}(\widehat h_{L,a}-h_{L,a}^D)\right]ds.
 \tag{30}
\]

Estimating (30) uses the residual-discrepancy integral and the dense
activity-weighted feature discrepancy already controlled by the
all-time damping comparison. Nothing in (30) produces a further factor
`q^-1`, a sign cancellation in the projection defect, or a bound on a
dense history divided by the closure residual at its terminal clock.
Replacing the physical comparison by a test-kernel differential also
introduces test Jacobian differences; the supplied Gram gap controls
the training residual, not contraction of every test prediction.

Therefore no exact `C/q`, all-time exponent above one, or floor-free
finite-width rate follows from this direct output argument. Compact-time
signed reconstruction estimates are valid extra information, but their
closure-residual floors vanish as the physical horizon grows. The
dense-own-clock endpoint regularity in `SMALL_LABEL_GAUSSIAN.md`, Section
5, explicitly leaves this clock-alignment issue unresolved.

## 8. Claim audit and input scope

| Claim | Status in this note | Main reason |
|---|---|---|
| Dense finite-to-population prediction, all time and each compact input set | Proved from supplied inputs | Compact-time identification plus uniform dense tail activity |
| Finite autonomous closure to dense population target, all time | Proved from supplied inputs | Equation (11), independent dense-only width floor |
| Whole `R^d` weighted supremum | Proved from supplied inputs | Equation (14), bounded outputs control spatial tails |
| Every fixed test law, all-time `Lp` discrepancy | Proved from supplied inputs | Clipped modulus (17), no input moments required for convergence |
| Explicit test rate from input moments | Proved from supplied inputs | Equations (18)--(19) |
| Fixed-order subsequential predictor laws | Proved from supplied inputs | Local equicontinuity and compactness, equation (27) |
| Unique fixed-order population old-clock solution and width identification | Open here | No closure-specific mesh-uniform carrier/stability theorem |
| Population-versus-population all-time near-first-order rate | Conditional | Equations (28)--(29) require that fixed-order identification |
| Unweighted supremum on all unbounded input space | Not obtained | Spatial compactness or an additional large-input estimate is needed |
| Numerical width rate, exact `C/q`, or improved all-time order exponent | Not obtained | Neither the dense floor nor needed signed terminal-clock control is quantified |

Scientific inputs were exactly the five complete assigned study files
listed below, `docs/notation.qmd`, maintained C.1--C.2 in
`docs/03-local-population.qmd`, and the introductory statement/A.1 and
C.3 of C.4.7.10 in `docs/08-autonomous-computation.qmd`. Book headings
were inspected to locate these proof units. Other cited study files
appearing inside the assigned sources were not opened. No `old_docs`,
other study, code, data, or external source was used.

| Complete study input | SHA-256 at this reading |
|---|---|
| `SLOW_ORDER_UNIFORM_BOUND.md` | `eee609f0cdc64fb7cdb748c1f4bae49632ca38f8e896931b92a468057f0a2bb9` |
| `SLOW_ORDER_GAUSSIAN_ROUTE.md` | `8e14b5ec751161d9116de49576e40ff242346fa5e5ebad0d7d7fd73795bf1544` |
| `SMALL_LABEL_GAUSSIAN.md` | `1d7cecbf36bea7c5ced2caf1d336d9d70d12db14ffb7a61bde44b580f998becb` |
| `GENERAL_AUTONOMOUS_SYNTHESIS.md` | `8ea4888e9874250e8386f32c492781dbc111fceda17ad5afc4e77a1b6980e735` |
| `GENERAL_REFERENCE_PROJECTION.md` | `db29db73c99b309d77f8233c4e0e1b3060ba8905588a7a893ddc9ccbf177801c` |

This is an internal derivation from the specified study inputs. It is not
an independent promotion review, and it makes no change to established
theory. The single decisive missing bridge for a literal two-population
theorem is the construction and finite-width identification of (23) at
fixed `q`; the test-observation passage itself is now explicit.

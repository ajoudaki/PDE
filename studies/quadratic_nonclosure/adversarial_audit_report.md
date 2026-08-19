# Adversarial audit of the pure-mean-field approximate-closure claim

> **Corrected scope.**  The zero-radius and positive-compiler statements in
> this report concern the exact **formal annealed** fixed-order jet.  They do
> not supply concentration or identify an actual positive-time mean-field
> trajectory.  The \(L^2\), Banach-algebra, frozen-tail, and analytic
> obstructions apply only to their displayed topologies or realization
> classes; the noncommutative continuation argument remains conditional on
> freeness/faithfulness and branch separation.

## Verdict

The phrase

> for every accuracy there is a finite-dimensional, one-source, O(1),
> constructively derived PDE that predicts the full mean-field loss curve

does not yet specify one mathematical proposition.  Under the unrestricted
existential reading it is a theorem for **every** continuous scalar curve and
is therefore vacuous.  Under the natural non-oracle, local-compiler reading,
none of the proposed Taylor, Galerkin, particle, or minimizing-movement
arguments proves it for the fully trained quadratic Gaussian model.  The
prescribed formal annealed Taylor compiler is rigorously false; the other
compilers require a model-specific real-axis well-posedness and tail estimate that has not been
proved and is not routine.

The strongest determinate formulation is a proof-carrying Galerkin/local-
compiler conjecture stated below.  The abstract implication from its
hypotheses to a globally accurate loss is true.  Its decisive hypotheses are
currently open for the full Gaussian model.  In a frozen-first-layer submodel,
the most obvious Gaussian truncation/particle strategy is rigorously false.

Thus an unconditional affirmative full-model theorem cannot honestly be
certified from the current material.  Nor is there yet a full-model no-go
theorem for every non-Taylor compiler.  There is, however, a complete logical
dichotomy that prevents the broad wording from being reported as a solved
nontrivial conjecture.

## Exact model and purely mean-field target

There is one fixed input, so it is suppressed.  Both hidden layers have width
`n`, the activation is `phi(u)=u^2/2`, and the canonical notation is

\[
 h_i^{(1)}=\phi(z_i^{(1)}),
\]

\[
 z_j^{(2)}=\sum_iW_{ji}^{(2)}h_i^{(1)},
 \qquad
 h_j^{(2)}=\phi(z_j^{(2)}),
\]

\[
 f_n=\frac1n\sum_ja_jh_j^{(2)},
 \qquad
 \mathcal L_n=(1-f_n)^2.
\]

Initialization is independent Gaussian:

\[
 z_i^{(1)}\sim N(0,1),\qquad
 W_{ji}^{(2)}\sim N(0,\gamma/n),\qquad
 a_j\sim N(0,1).
\]

Here (a_j) is the rescaled readout coordinate; the corresponding raw
forward weight is (a_j/n).

The `muP` squared-loss flow is

\[
 \dot z^{(1)}=-n\nabla_{z^{(1)}}\mathcal L_n,
 \qquad
 \dot W^{(2)}=-\nabla_{W^{(2)}}\mathcal L_n,
 \qquad
 \dot a=-n\nabla_a\mathcal L_n.
\]

The approximation question itself is asked **after** the mean-field limit.
If the intended deterministic target exists, write `F(tau)` for its readout
along mean-field gradient ascent on `f`, and write `kappa=F'>=0` for its
tangent kernel.  Squared-loss flow is
the same feature orbit with a different clock:

\[
 \dot\tau=2(1-F(\tau)),\qquad
 f(t)=F(\tau(t)),\qquad
 \mathcal L(t)=(1-f(t))^2.
\]

There is no width or probability in the desired conclusion.  The requested
statement is that, for every \(\varepsilon>0\), a finite source model derived
from the mean-field law should produce \(\mathcal L_M\) with

\[
 \sup_{t\ge0}|\mathcal L_M(t)-\mathcal L(t)|\le\varepsilon.
\]

For the structural calculations only, abbreviate

\[
 z=z^{(2)},\qquad h=h^{(1)},
\]

and define

\[
 q=\frac1n\sum_i h_i^2,
 \qquad
 K=W^{(2)}\operatorname{diag}(h)(W^{(2)})^\top.
\]

Along readout ascent the exact composite equations contain

\[
 a'=\frac12z^{\odot2},
 \qquad
 z'=q(a\odot z)+2K(a\odot z).
\]

The first term in the second equation is the positive scalar branch used in
the no-go proofs.  The `K` term is positive only after taking the quadratic
form `(a odot z)^T K(a odot z)`; it has no componentwise sign.

### Established zero-radius input

Let \(D_{+,n}\) denote the finite-width readout-ascent derivation and define
the formal annealed coefficients by

\[
 c_k=\lim_{n\to\infty}
 \mathbb E\!\left[\frac{D_{+,n}^k f_n(0)}{k!}\right],
\]

where the exact special quadratic forest compiler supplies the fixed-order
annealed limit.  For odd `k`, with `m=(k+3)/2`, the audited scalar-branch
argument gives

\[
 c_k\ge
 m!\,b_\gamma^m
 \left(\frac34\right)^{k+1}{k+2\choose2},
 \qquad
 b_\gamma=\frac12\min\{1,\gamma/2\}>0.
\]

The proof repeatedly selects only

\[
 a'=z^2/2,\qquad z'=qaz.
\]

On the invariant ray `z=sqrt(2q)a`, this becomes `a'=qa^2`, whose responses
grow factorially.  Gaussian even moments contribute another factorial
factor.  In the independent primitive coordinates the readout and ascent
vector field have nonnegative polynomial coefficients; every surviving Wick
monomial is nonnegative, so no omitted derivative history can cancel the
selected branch.  Stirling's formula therefore yields

\[
 \limsup_{k\to\infty}c_k^{1/k}=+\infty.
\]

This is a statement about the formal annealed fixed-order coefficient
sequence. It is not concentration of the random derivatives, a finite-width
error estimate, or identification with derivatives of a positive-time
limiting curve.

## 1. Why unrestricted finite one-source existence is tautological

Let `f:[0,infinity)->[f_0,1]` be any continuous scalar output with
`f(t)->1`.  Put

\[
 q(t)=\frac{t}{1+t}
\]

and extend

\[
 g(q)=f\!\left(\frac{q}{1-q}\right),\qquad g(1)=1,
\]

continuously to `[0,1]`.  Let `p_M` be the Bernstein polynomial of `g`.
Then

\[
 \|p_M-g\|_{L^\infty(0,1)}\longrightarrow0.
\]

If `f` is increasing, `p_M` is increasing, takes values in `[f_0,1]`, and
has the correct endpoints.

This approximation can be realized by a one-field, one-source PDE with an
exactly invariant **two-state** affine ansatz.  Set

\[
 \partial_tU_M(t,s)
 =\bigl(1-\partial_sU_M(t,0)\bigr)^2
 \left[p_M'\!\left(\partial_sU_M(t,0)\right)+s\right],
 \qquad U_M(0,s)=f_0.
\]

Writing `U_M(t,s)=u_M(t)+q_M(t)s` gives

\[
 \dot q_M=(1-q_M)^2,\qquad
 \dot u_M=(1-q_M)^2p_M'(q_M),
\]

so `q_M=t/(1+t)` and `u_M=p_M(q_M)`.  Hence

\[
 \sup_{t\ge0}|u_M(t)-f(t)|\to0,
 \qquad
 \sup_{t\ge0}|(1-u_M(t))^2-(1-f(t))^2|\to0.
\]

This uses one source and two states, even independently of requested
accuracy.  All accuracy dependence has merely been moved into the degree and
coefficients of `p_M`.  Those coefficients contain samples of the unknown
future curve.  This is precisely the oracle loophole.

A version closer to the proposed transport PDE is equally immediate.  If the
exact feature-time profile `F` is known on its target interval, its Bernstein
polynomials are monotone finite source profiles, and the residual-clock
transport equation globally shadows the exact loss.  Again, the coefficients
are exact future samples of `F`.

Consequently, neither “finite-dimensional” nor “one source” prevents hiding.
Indeed every finite ODE `x'=G(x)` can be packed into one source by

\[
 U(t,s)=\sum_{j=0}^{d-1}x_j(t)s^j,
 \qquad
 U_t=\sum_{j=0}^{d-1}G_j(J_dU(t,0))s^j.
\]

Unless a uniform local source grammar is imposed, “one source” is only a
coordinate encoding and has no closure content.

## 2. What O(1) must mean in a pure mean-field problem

There is no width parameter after the mean-field limit, so `O(1)` is
meaningless until its reference parameters are declared.  The defensible
meaning is:

* for every `epsilon>0`, the closure has a finite number `d(epsilon)` of
  states;
* `d(epsilon)` is independent of the physical time horizon;
* `d(epsilon)` may grow as `epsilon` decreases;
* the number of source coordinates and fields is fixed;
* the description length/local operator complexity must also be specified,
  otherwise the two-state construction above makes state dimension vacuous.

If state dimension is required to be fixed even as `epsilon->0` while the
vector-field degree and real constants are unrestricted, the oracle
construction still uses only two states.  Thus bounding states alone is never
enough.

## 3. A nontrivial and determinate conjecture

The strongest broad formulation that is both useful and auditable is the
following proof-carrying local-compiler statement.

First one must exhibit a deterministic mean-field state space `X`, an exact
feature-time equation

\[
 Y'=G(Y),\qquad F'=K(Y)\ge0,
\]

and a target buffer `[0,T]` on which:

1. the Gaussian initial state belongs to `X`;
2. the equation has a unique classical solution through `T`;
3. `G` is continuously stable in the chosen topology on a tube around that
   solution;
4. the readout/kernel functional `K` is continuous there;
5. `F` reaches one and has the strict monotonicity needed by the residual
   clock.

An admissible order-`M` closure must then be produced by a **uniform finite
compiler** from only the architecture, Gaussian law, and local mean-field
attachment/contraction rules.  It may not query `F`, the exact target time, or
any exact positive-time hierarchy state.  It must output a finite system and
an a priori, independently checkable residual bound

\[
 \rho_M\longrightarrow0
\]

in the fixed state-space norm.  It must reconstruct a nonnegative approximate
kernel, so that the approximate profile is monotone and reaches the target.
The finite system may then be represented by a genuine uniform source PDE, or
packed into one source if mere syntactic one-source existence is all that is
required.

For a single fixed initialization law, “does not query the answer” is a
syntactic/computability restriction rather than an ordinary extensional
property: the architecture already determines the one target curve, so that
curve can always be hidden in real constants.  A robust alternative is to
require the same compiler and error theorem uniformly for a specified
neighborhood of initialization laws, labels, or variance parameters.  Another
is to require the displayed a priori hierarchy residual.  At least one of
these devices is necessary to make non-oracularity mathematically testable.

Under a locally Lipschitz Banach-space realization with uniformly bounded
finite-rank projections `P_M->I`, the standard Galerkin proof is complete:

\[
 Y_M'=P_MG(Y_M),\qquad Y_M(0)=P_MY(0)
\]

converges uniformly on `[0,T]`.  Compactness of `G(Y([0,T]))` makes
`(I-P_M)G(Y)` uniformly small.  A Lipschitz kernel then gives
\(\|F_M-F\|_\infty\to0\), and the already-proved squared-loss clock comparison
upgrades this to

\[
 \sup_{t\ge0}|\mathcal L_M(t)-\mathcal L(t)|\to0.
\]

This is a correct abstract theorem.  It is not yet a theorem about the stated
Gaussian network until `X,G,K,P_M` and their estimates are actually supplied.

### Strongest model-specific formulation that survives the known no-go results

The Gaussian zero-radius theorem rules out requiring a bounded analytic
generator on one Banach space.  The following residual formulation is broad
enough to allow an unbounded generator or a scale of spaces, while remaining
non-oracular and falsifiable.

> **Certified local real-axis closure conjecture.**  For the deterministic
> full Gaussian quadratic mean-field hierarchy there are a real-axis state
> evolution `Y'=G(Y)`, a nonnegative kernel observable `K`, and trajectory,
> initial-data, and forcing norms on a target buffer `[0,T]` such that:
>
> 1. the hierarchy has a unique target-reaching solution `Y` and its loss is
>    the squared-loss residual-clock time change of
>    `F'=K(Y)`;
> 2. an a posteriori observable-stability estimate holds on a fixed tube:
>    
>    \[
>    \|K(\widetilde Y)-K(Y)\|_{L^1(0,T)}
>    \le C_T\left(
>    \|\widetilde Y(0)-Y(0)\|_{\rm init}
>    +\|\widetilde Y'-G(\widetilde Y)\|_{\rm force}
>    \right);
>    \]
> 3. one uniform finite local compiler, given `M`, uses only the architecture,
>    Gaussian Wick rules, and finitely many local generator operations to
>    produce a finite ODE `y_M'=G_M(y_M)`, a reconstruction `R_My_M`, and a
>    nonnegative finite kernel `K_M`; it never queries `Y`, `F`, or the exact
>    target time at positive feature time;
> 4. the compiler also produces checkable bounds
>    
>    \[
>    \eta_M\ge\|R_My_M(0)-Y(0)\|_{\rm init},\qquad
>    \rho_M\ge\|(R_My_M)'-G(R_My_M)\|_{\rm force},
>    \]
>    
>    and a kernel-reconstruction bound `beta_M`, with
>    `eta_M+rho_M+beta_M -> 0`;
> 5. finite, certified real-axis integration of `K_M` followed by positive
>    polynomial compression produces `P_M`, and the fixed transport PDE
>    
>    \[
>    U_t=2(1-U(t,0))U_s,\qquad U(0,s)=P_M(s)
>    \]
>    has loss error tending to zero uniformly for all physical time.

For every requested accuracy the ODE and polynomial degrees are finite and
independent of physical time.  They may grow with accuracy.  The transport
operator is fixed; only its finitely generated source profile changes.

Items 1--4 are the substantive conjecture.  Item 5 follows from them and the
proved clock comparison.  This statement cannot be satisfied by exact-curve
Bernstein samples, arbitrary real constants encoding the answer, or an
uncertified finite ODE packing.

The conditional continuation-capacity argument does not refute this
conjecture: besides its still-open freeness/faithfulness and branch-separation
lemmas, the finite dimension may grow and the error here is measured only in
an observable trajectory norm rather than exact branchwise future semantics.
The zero-
radius theorem refutes initialization Taylor truncation and the one-Banach
analytic realization, but not an unbounded/scale-space real-axis method.  The
frozen tail theorem refutes naive Gaussian cutoff convergence, but its
componentwise comparison does not survive the full `K` message.  A definitive
negative proof would need a quantitative noncompactness result--for example a
nonvanishing lower bound on every admissible finite residual or on the
Kolmogorov widths of the target orbit in the observable-stability norm.  No
such estimate is presently established.

There is a second reason initialization data alone cannot finish the job.
Once analyticity has failed, even the **complete** formal Wick jet does not
uniquely determine a real-axis function in the class of smooth functions.
Borel extension and nonzero flat functions give different positive-time
profiles with identical derivatives at zero.  Thus Padé, Borel, or another
jet resummation is a choice of continuation until a quasianalyticity,
summability, or independent real-axis well-posedness theorem proves that it is
the continuation selected by the network.

## 4. Why the current Gaussian model does not satisfy the abstract theorem
by inspection

### 4.1 The target mean-field flow itself has not been constructed

The attached work supplies fixed-order Wick coefficients and an infinite
message hierarchy.  It does not supply a Banach/Hilbert realization in which
the full positive-time hierarchy is well posed.  A formal hierarchy with a
zero-radius initialization series is not a classical mean-field trajectory.
Before approximating the loss, existence, uniqueness, and continuity of the
target observable must be established.

### 4.2 Ordinary Gaussian L2 is not a valid closure topology

Polynomial multiplication is not locally bounded from ordinary `L2` to
`L2`.  More concretely, on a nonatomic probability space choose a set `A_R`
of mass `R^{-3}` and set

\[
 a_R=z_R=R\,1_{A_R}.
\]

Then

\[
 \|a_R\|_2^2+\|z_R\|_2^2=\frac2R\to0,
 \qquad
 E[a_Rz_R^2]=1.
\]

Thus the cubic readout is discontinuous under vanishing `L2` perturbations.
The tangent kernel contains still higher powers.  The exact quadratic balance
laws therefore do not exclude an order-one loss change caused by a vanishing
tail mass.

This ambient rare-set witness is not shown to lie on the canonical network's
reachable-state manifold.  It nevertheless defeats an unqualified
physical-time minimizing-movement argument that relies on `L2` control alone.
In the `L2` metric one can change the readout by order one with arbitrarily
small metric cost, so squared loss is not continuous or weakly lower
semicontinuous in the topology controlled by the balance law.  A proximal
step can have a collapsed infimum or select a relaxed, instantaneously
condensed dynamics.  A stronger higher-moment/Orlicz topology and compactness
theorem are indispensable.

No single ordinary `L^p` closes the degree-six polynomial vector field: a
degree-six map consumes higher integrability than it returns.  `L^infinity`
is an algebra but excludes Gaussian initialization.  A scale of weighted
spaces might work, but constructing it and proving target-time bounds is the
missing theorem, not a routine application of Galerkin convergence.

There is also a simple general obstruction to the most common proposed fix.
Suppose `X` is a Banach space of random variables, the embedding `X->L1` is
continuous, and ordinary multiplication is a bounded bilinear operation on
`X`.  Then

\[
 \|x^m\|_1\le C_1 C_2^{m-1}\|x\|_X^m.
\]

Taking `m`-th roots and sending `m` to infinity shows

\[
 \|x\|_\infty\le C_2\|x\|_X.
\]

Thus every such Banach function algebra is contained in `L^infinity` and
cannot contain a nondegenerate Gaussian coordinate.  A successful Gaussian
theory therefore has to use a **scale** of spaces, a restricted nonlinear
domain, or a nonstandard renormalized product.  It cannot simply assume one
Banach algebra in which all local polynomial rules are Lipschitz.

The already-proved formal zero Taylor radius yields a sharper no-go for one
specific realization class. Assume there were a Banach space `X`, an initial
state `Y_0 in X`, and an exact realization of the formal annealed jet

\[
 Y'=G(Y),\qquad F'=K(Y),
\]

on which `G` and `K` were analytic near `Y_0`.  This includes every
realization in which the network's polynomial attachment/contraction rules
are represented by bounded multilinear maps on one Banach space.  The
analytic ODE theorem would make `Y(tau)` and `F(tau)` analytic for some
positive radius.  Cauchy estimates would give

\[
 \frac{|F^{(k)}(0)|}{k!}\le C R^{-k}.
\]

If the realization is exact, its derivatives at zero must equal the fixed-
order Wick coefficients `c_k`.  This contradicts
`limsup |c_k|^(1/k)=infinity`.

Therefore no exact one-space bounded analytic realization can reproduce every
coefficient of this formal annealed jet.  This does not exclude an
accuracy-indexed sequence of analytic approximants, an unbounded generator, a
domain/scale with loss of regularity, or a nonanalytic real-axis resummation.
Such scale-space Galerkin approximations can in principle converge even when
the initial state is not an analytic vector.

Positivity gives a stronger result that also excludes many unbounded or
scale-space proposals.  Let `A` be the reachable mean-field diagram algebra,
`A_+` its primitive nonnegative-coefficient cone, and `Lambda` the Wick
valuation.  Algebraically,

\[
 f\in A_+,\qquad DA_+\subseteq A_+,\qquad
 \Lambda(p)\ge0\quad(p\in A_+).
\]

Suppose an ordered Banach completion, or one member of a scale of spaces,
carried a positive strongly continuous semigroup `S(tau)` whose generator
extends `D` on every `D^k f`, and suppose `Lambda` extended to a continuous
positive functional.  The semigroup Taylor formula with integral remainder
would give, for every finite `M`,

\[
 S(\tau)f
 =\sum_{k=0}^M\frac{\tau^k}{k!}D^kf
 +\int_0^\tau\frac{(\tau-r)^M}{M!}
 S(r)D^{M+1}f\,dr.
\]

The remainder is positive.  Applying `Lambda` gives

\[
 \Lambda(S(\tau)f)
 \ge\sum_{k=0}^Mc_k\tau^k.
\]

The right side tends to `+infinity` for every `tau>0`.  Hence there is no
finite-valued positive classical semigroup completion that simultaneously
preserves the primitive diagram cone, realizes all local derivatives, and
makes the Wick readout continuous.  Merely naming an `L^p`, Orlicz, Fock, or
Kondratiev scale does not evade the obstruction.  A surviving scale-space
construction must lose at least one hypothesis--for example by using a mild
state that is not in every generator domain, a discontinuous/renormalized
readout, or essential signed nonlocal cancellation--and must then prove that
the altered object is still the actual mean-field trajectory.

### 4.3 Worst-case numerical stability is not width/tail uniform

The scaled Hessian already has row blocks of norm proportional to an extreme
Gaussian second-layer preactivation.  Their maximum grows like
`sqrt(log n)`.  Hence a uniform operator-norm Lipschitz estimate cannot justify
a real-axis Euler/Wick diagonal limit.  Fixed-step Wick convergence does not
permit sending the number of steps to infinity.

In fact the particular **explicit symbolic Euler followed by Wick** compiler
can be refuted, rather than merely left conditional.  There is a short
operator proof.

Let `D` be the exact readout-ascent derivation and let `E_h` be pullback by one
explicit Euler state update:

\[
 E_hp=p\circ(I+hX),
\]

where `X` is the polynomial ascent vector field.  Because both the readout
and `X` have nonnegative coefficients in the independent primitive
coordinates, multinomial expansion gives

\[
 E_h=I+hD+\sum_{\ell\ge2}h^\ell A_\ell,
\]

where every `A_ell` preserves the cone of coefficientwise-nonnegative
polynomials.  Centered Gaussian Wick expectation is nonnegative on that cone:
odd monomials vanish and even monomials are positive.

In `E_h^N f`, choose the `hD` term in exactly `k` of the `N` factors and the
identity in the others.  All other choices have nonnegative Wick expectation.
Therefore

\[
 \mathbb E[E_h^Nf]
 \ge {N\choose k}h^k\mathbb E[D^kf].
\]

Take `h=tau/N` and then the fixed-program mean-field Wick limit, reusing the
formal annealed coefficients \(c_k\) defined above. The deterministic
Euler/Wick profile obeys

\[
 F_N(\tau)
 \ge
 \tau^k\frac{(N)_k}{N^k}c_k,
\]

where `(N)_k=N(N-1)...(N-k+1)`.  For each fixed `k`, the middle factor tends
to one.  Since the proved zero-radius bound says

\[
 \limsup_{k\to\infty}c_k^{1/k}=\infty,
\]

given any `tau>0` and any `A>0`, one can first choose `k` with
`c_k tau^k>2A`, and then choose `N` so large that `(N)_k/N^k>1/2`.
Consequently

\[
 F_N(\tau)\longrightarrow+\infty
 \qquad(\tau>0).
\]

The same estimate holds for the safer implementation that integrates the
Euler kernel rather than evaluating the Euler readout.  Since `kappa=Df`,
selecting `k-1` copies of `D` in the `m`-th kernel checkpoint and using

\[
 \sum_{m=k-1}^{N-1}{m\choose k-1}={N\choose k}
\]

produces exactly the same lower bound.

Hence fixed-program Wick limits followed by mesh refinement do **not**
converge.  Their source target times collapse to zero, and the residual-clock
losses converge pointwise to the discontinuous step that equals one at zero
and zero at every positive physical time.  They cannot converge uniformly.

The proof applies more generally to every Wick-positive consistent polynomial
one-step compiler

\[
 E_h=I+hD+\sum_{\ell\ge2}h^\ell A_\ell
\]

whose remainder operators preserve the positive polynomial/Wick cone.  This
includes explicit Euler and positive-stage Picard or SSP-type polynomial
schemes.  Variable positive steps do not help: the binomial coefficient is
replaced by an elementary symmetric sum with the same consistent limit.

This is a full-network formal-jet no-go for the stated Wick-positive compiler
class. It does not cover a method that introduces genuine cancellation or
resummation, an implicit/tamed
nonpolynomial rule, or a scale-space Galerkin projection with a separately
certified real-axis residual.

The underlying no-go is scheme-independent.  If finite polynomial source
profiles

\[
 P_M(s)=\sum_k\beta_{M,k}s^k
\]

have `beta_(M,k)>=0` and recover every fixed Wick coefficient,
`beta_(M,k)->c_k`, then for every `s>0` they diverge to `+infinity`.  Indeed,
for any `A` choose a fixed `k` with `c_k s^k>2A`, and then choose `M` so that
`beta_(M,k)>c_k/2`.  Thus no coefficientwise-positive, all-fixed-orders-
consistent polynomial compiler can converge.  Euler is important because
the pullback argument proves that a broad local compiler class necessarily
has exactly these two fatal properties.

There is a second, purely semantic obstruction to any compiler that reads
only initialization derivatives.  Once analyticity has failed, even the
complete infinite jet does not determine a real-axis function: adding a flat
term such as `exp(-1/tau^2)` for `tau>0` changes the positive-time curve while
leaving every derivative at zero unchanged.  Thus Pad\'e, Borel, or another
jet resummation selects a continuation; it becomes a theorem about this
network only after a quasianalyticity, summability, or independent real-axis
well-posedness result proves that the selected continuation is the mean-field
trajectory.

### 4.4 Gaussian tail truncation can be dynamically singular

In the frozen-first-layer mean field, after rescaling, a particle satisfies

\[
 u'=qv^2,\qquad v'=quv,
\]

and contributes `quv^2` to the readout.  For the centered Gaussian law
conditioned to `[-R,R]^2`, positive-corner comparison with the invariant ray
`u=v` shows that the mean readout diverges before feature time `1/(qR)`.
Every fixed subtarget `y<1` is therefore reached before that time.  The
squared-loss physical hitting time obeys

\[
 t_R(y)\le\frac{1}{2qR(1-y)}\to0.
\]

Hence the truncated losses equal one at zero but tend to zero at every fixed
positive physical time.  They are not uniformly Cauchy on any interval
containing zero.  Initial Wasserstein or moment convergence of the truncated
Gaussian laws does not imply dynamic convergence.

This is a rigorous theorem for the frozen subsystem.  It is not automatically
a theorem for the fully trained model because the additional `K(a odot z)`
message has no componentwise sign.  It does, however, refute every proof that
claims Gaussian quadrature/truncation is harmless merely from initial tail
bounds.

## 5. Audit of the positive identities

Conditional on a classical target-fitting mean-field solution with finite
moments, the following parts of the earlier argument survive audit:

* squared-loss flow is the readout-ascent orbit under the clock
  `tau'=2(1-F(tau))`;
* `F'=kappa>=0`;
* with `C=E[a^2]`, Cauchy--Schwarz gives `F^2<=C kappa` and
  `C'=2F` in feature time (equivalently `Cdot=4f(1-f)` in physical time);
* after any positive output level, `C/F^2` is nonincreasing and the kernel is
  bounded below, so the target is reached in finite feature time;
* a known small monotone profile/kernel defect gives a uniform all-physical-
  time loss defect by scalar clock contraction.

These are stability implications.  They neither construct the classical
mean-field state nor make a hierarchy tail small.  Passing the identities
from finite systems to mean field also requires the same uniform integrability
that tail condensation threatens.

### Required audit for any proposed full-`K` scale-space proof

Such a proof must provide all of the following, rather than only name a
weighted chaos or Fock space:

1. explicit diagram/message indices and weights, with a proof that the
   Gaussian initial state has finite norm;
2. a closed domain for the full generator, including matrix reuse,
   attachments, Wick contractions, and contractions from high grade back to
   low observable grade;
3. quantitative maps between a scale of spaces, or a closable unbounded
   generator and a mild-solution theorem, through a certified target buffer;
4. derivative estimates compatible with the lower growth
   `F^(k)(0) >= k!(k/2)! times exponential factors`; any ordinary analytic
   Cauchy bound is impossible;
5. continuity of the readout and tangent kernel in the same forcing/stability
   topology--weights cannot simply suppress the positive scalar branch while
   still extracting it as a bounded observable;
6. stable finite projections and a **computed** outgoing residual tending to
   zero, not an exact-orbit tail written as an assumption;
7. a structure-preserving kernel reconstruction, since a raw moment
   projection may create a negative kernel;
8. a dynamic Gaussian-tail/uniform-integrability estimate excluding mass
   escape or condensation;
9. no componentwise inference from `K>=0`: positive semidefiniteness gives
   `v^TKv>=0`, but individual coordinates of `Kv` have either sign;
10. a non-oracular target-buffer certificate and the final residual-clock
    comparison.

A chaos-degree projection is especially delicate: Wick contractions can send
high-grade intermediates back into low-grade observables, so smallness of the
raw high-grade coefficient tail does not by itself imply small observable
residual.

## 6. Audit outcomes for proposed constructions

| Construction | Audited status |
|---|---|
| Exact-curve Bernstein/source polynomial | Always works, but is oracle curve fitting |
| Initialization Wick--Taylor jet | False: factorial coefficient lower bound and zero radius |
| Any coefficientwise-positive, fixed-order-consistent polynomial compiler | False: zero-radius coefficients force divergence at every positive source value |
| Explicit symbolic Euler or positive-stage polynomial Wick integrator | False by the pullback/binomial lower bound |
| Exact one-Banach bounded analytic realization of the formal jet | Impossible: it would force a positive Taylor radius |
| Implicit/tamed/Picard or scale-space time stepping | Not resolved; requires a real-axis stability and tail theorem |
| Weighted message Galerkin | Correct conditional theorem; no state space or residual tail theorem supplied |
| Deterministic particles/Gaussian quadrature | Correct for globally Lipschitz McKean--Vlasov equations; hypotheses fail/unproved here |
| Gaussian compact truncation | Dynamically singular in the frozen subsystem |
| Physical-time Galerkin | Still needs higher-moment continuity and compactness; L2 balances are insufficient |
| L2 minimizing movements | Ambient L2 control alone is insufficient because the readout is L2-discontinuous; higher-moment/reachable-set control may repair the route |
| Padé/Borel resummation | No summability, positivity, or real-axis error theorem supplied |
| One-source packing of an arbitrary finite ODE | Syntactically valid but makes the one-source condition vacuous |

## 7. Exact final conclusion

There are three distinct statements.

1. **Unrestricted scalar existence:** true for every continuous fitting loss,
   by the explicit two-state one-source construction above.  This says
   nothing about mean-field closure.
2. **The prescribed formal Wick--Taylor compiler:** false at the formal
   annealed mean-field level.
3. **A non-oracular real-axis local compiler for the fully trained Gaussian
   hierarchy:** a well-posed conjecture only after the hierarchy space,
   admissible compiler, and residual norm are fixed.  No audited constructive
   proof presently verifies its decisive hypotheses, and no theorem yet rules
   out every such non-Taylor compiler.

Therefore the definitive answer to the sentence originally called the
"final conjecture" is:

> It is not one well-formed nontrivial proposition.  Under its literal
> existential meaning it is true for every continuous scalar loss and says
> nothing about closure.  Under the concrete local positive-Wick meanings
> proposed in this project it is false.  The broadest meaningful
> non-oracular version is the separately stated certified local real-axis
> closure conjecture; its truth is an additional mathematical question, not
> something determined by the phrase "some finite one-source PDE."

This is not a report of an unsuccessful proof attempt.  It is a proof that
the original wording conflates inequivalent mathematical claims with
different truth values.  Calling that wording "completely proved" or
"completely disproved" would be logically false.  Any future affirmative
claim about the certified version must pass the state-space, tail,
non-oracle, source-locality, and global-clock audits listed above; any future
negative claim must give a quantitative noncompactness or residual lower
bound covering signed and nonanalytic compilers.

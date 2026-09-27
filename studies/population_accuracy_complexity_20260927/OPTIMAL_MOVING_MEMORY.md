# Optimizing moving memory at prescribed population-prediction error

This continues `ANALYSIS.md` for the user's optimization question. The target,
initialization, feature-learning scaling, test measure Q, and horizon [0,T]
are identical for every method. Error means whole-test-distribution prediction
RMSE, uniformly in time, with the same probabilistic convention throughout.

We optimize the error/cost models identified in that analysis. These are
optimal resource allocations for specified representations and sufficient
error bounds, not lower bounds on all possible algorithms in a framework.
The population square-root-width law and width-uniform closure estimates are
conditional predictions; their algebraic optimization does not prove them.

## Accounting and constants

Moving memory means persistent scalar state updated while computing training.
Exclude genuinely fixed initialization matrices and initial coefficient tables,
including W0 for response memory and the top fixed tensor for truncated NTH.
Include the evolving kernels while a DMFT solver computes them: they cannot
be declared fixed merely because a completed run later freezes them.
Do not count an archive of all predictions or temporary forward activations
as model state. Arbitrarily precomputing the solution and calling it a fixed
coefficient is outside the comparison.

H is hidden depth, m training sample count, and d fixed input dimension.
Constants below depend on `(m,H,T)` and on the fixed task, initialization law,
and test measure. They are independent of tunable width/order only under the
population-scale assumptions in `ANALYSIS.md`. This notation does not assert
that the displayed explicit m,H factors exhaust their dependence. Current
theory supplies no universal polynomial law in m,H,T for those constants.

Use the working error laws

\[
E_{dense}\le A n^{-1/2},\qquad
E_q\le A n^{-1/2}+B_qP^{-q},\quad q=1,2,
\]

with `A=A(m,H,T)`, `B_1=B_old(m,H,T)`, and `B_2=B_joint(m,H,T)`.
Positive generic constants and sufficiently small epsilon are understood;
zero-error and stationary special cases need less memory. The rates remain
equivalent if P is replaced by the exact `sqrt(P(P+1))` factors.

## Dense

The moving parameter count is

\[
M_{dense}(n)=(H-1)n^2+(d+1)n.
\]

It increases with n. The minimum width satisfying the error budget is
`n=ceil((A/epsilon)^2)`. Consequently

\[
M_{dense}^*(\epsilon)
\asymp (H-1)A^4\epsilon^{-4}+(d+1)A^2\epsilon^{-2}.
\tag{1}
\]

The dominant term is proportional to epsilon^-4. This is optimal for this
bound/cost model, not a proved lower bound for actual errors on every task.

## Both response-memory clocks

The dominant moving state is `2(H-1)mnP`. The input matrix and readout add
`(d+1)n`. The joint clock also adds its P-by-P Gram matrix. Matching initial
prefix fields are fixed data and excluded from moving memory.

Let `u=A/sqrt(n)` and `v=B_q/P^q`. At a continuous optimum the full budget is
used: `u+v=epsilon`. Then

\[
nP=A^2B_q^{1/q}u^{-2}v^{-1/q}.
\]

Differentiating its logarithm with respect to u gives

\[
-\frac2u+\frac{1/q}{\epsilon-u}=0.
\]

The logarithm has positive second derivative, and diverges at both endpoints,
so this is the unique minimum. Therefore

\[
u_*={2q\over2q+1}\epsilon,\qquad
v_*={1\over2q+1}\epsilon,
\]
\[
n_* =\left({(2q+1)A\over2q\epsilon}\right)^2,
\qquad
P_* =\left({(2q+1)B_q\over\epsilon}\right)^{1/q}.
\tag{2}
\]

Rounding upward produces a feasible integer choice with the same asymptotic
cost. This is the leading-state optimization; lower-order outer-weight and
Gram terms perturb its exact finite-epsilon allocation but not its asymptotic
exponent or leading optimizer as epsilon tends to zero at fixed task.

For the old clock:

\[
n_*={9A^2\over4\epsilon^2},\quad P_*={3B_1\over\epsilon},\quad
M_{old}^*\sim {27\over2}(H-1)m A^2B_1\epsilon^{-3}.
\tag{3}
\]

Two thirds of the error budget go to width and one third to compression.

For the joint clock:

\[
n_*={25A^2\over16\epsilon^2},\quad P_*=
\sqrt{{5B_2\over\epsilon}},\quad
M_{joint}^*\sim {25\sqrt5\over8}(H-1)m A^2\sqrt{B_2}\epsilon^{-5/2}.
\tag{4}
\]

Four fifths of the error budget go to width and one fifth to compression.
Its Gram matrix adds `5B_2/epsilon` entries at this allocation, and outer
weights add order `(d+1)A^2/epsilon^2`; both are lower order.

The factor m matters. Up to constants, moving-state compression beats dense
storage when `m B_1 epsilon << A^2` for the old clock, or
`m sqrt(B_2) epsilon^(3/2) << A^2` for the joint clock. This is not an
improvement in total storage while dense W0 is retained.

More generally, if a future width estimate is `A n^-alpha`, the same calculation
allocates `q/(q+alpha)` of epsilon to width, and gives dense exponent
`2/alpha` versus closure exponent `1/alpha+1/q`. This records exactly where
the square-root-width hypothesis enters the optimized exponents.

## NTH: exclude its fixed top tensor consistently

For truncation through tensor order p, `dot(K^(p))=0`. Hence the direct moving
state is predictions plus tensors of orders 2 through p-1:

\[
M_{NTH}(m,p)=\sum_{j=1}^{p-1}m^j
=\frac{m^p-m}{m-1},\qquad m\ge2.
\tag{5}
\]

This lies between `m^(p-1)` and `2m^(p-1)`. The top tensor's m^p coefficients
are fixed and must be reported separately. The source of this accounting is
Huang--Yau equation (2.7), inspected in the previously retrieved full PDF.
Equation (17) of `ANALYSIS.md` gives an equivalent residual-integral
representation of the whole test function with the same direct state order,
provided the initial mixed-kernel functions can be evaluated.

If all depth contributions have been combined into these output kernels,
there is no extra H factor in (5). Depth enters the initial functions and the
error constants/order needed for accuracy. This distinction is material.

Let `eta_p(m,H,T)` be a valid same-regime, whole-test-function truncation bound.
The general answer is

\[
p_\epsilon=\min\{p\ge2:\eta_p(m,H,T)\le\epsilon\},\qquad
M_{NTH}^*=\sum_{j=1}^{p_\epsilon-1}m^j.
\tag{6}
\]

Population initial coefficients are assumed in (6). If the initial tensors
are estimated at finite width, sufficiently accurate coefficients are an
additional requirement. Width does not appear in the moving tensor count;
memory-only optimization therefore has no finite interior optimum in that
width: more accurate precomputation costs fixed resources and time. It is not
legitimate to add an n^2 moving-state charge to NTH while excluding fixed W0
from the response-memory count. Conversely its precomputation is not free in
total-resource comparisons.

The original NTH theorem's n^-p/2 rate cannot supply eta_p for our different
feature-learning scaling. Our preceding matched derivation gives one useful
sufficient regime: if exact kernels satisfy

\[
|K^{(j)}|\le U V^{j-2}(j-2)!,\qquad
q=2RVT<1,
\]

with R a residual bound and constants uniform in width, then

\[
\eta_p\le D\frac{q^p}{p},\qquad
D={U\over V}\exp\left({2UT\over1-q}\right).
\tag{7}
\]

All U,V,R,D,q can depend on m,H,T. Let `lambda=log(1/q)>0` and let W be the
positive real Lambert W function, defined by `W(z)exp(W(z))=z`. Solving (7)
for p gives the exact continuous threshold and its integer version:

\[
p_\epsilon=\max\left\{2,
\left\lceil{W(\lambda D/\epsilon)\over\lambda}\right\rceil\right\}.
\tag{8}
\]

Indeed `(D/p)exp(-lambda p)<=epsilon` is equivalent to
`(lambda p)exp(lambda p)>=lambda D/epsilon`. Equations (5),(8) give explicit
m dependence without losing the rounding factors. For fixed m>=2 and fixed
positive constants, with `alpha=log(m)/lambda`,

\[
M_{NTH}^*\asymp
\left({D\over\epsilon\log(D/\epsilon)}\right)^\alpha.
\tag{9}
\]

The constants in this asymptotic depend on m,lambda; use (5),(8) if those
dependencies matter. Ignoring logarithms the epsilon exponent is
`alpha=log(m)/log(1/q)`. Under the looser geometric bound `D q^p`, simply use
`p= max(2,ceil(log(D/epsilon)/lambda))`, dropping the logarithmic improvement.

This is conditional, not a general NTH convergence theorem for rich tanh
training on every finite horizon. When q>=1, this certificate gives no
vanishing bound as p grows. It does not prove that NTH fails. Additional
kernel-growth information is needed to determine p_epsilon there.

For m=1, the direct hierarchy count is p-1, but an equivalent implementation
can do better. There is one control u(t); its iterated integrals are
`I_k=s(t)^k/k!`, with `s'=u`, `s(0)=0`. Equation (17) of `ANALYSIS.md` thus
represents the truncated predictor by one evolving scalar s and fixed initial
kernel coefficients. This illustrates why the direct tensor counts are not
universal lower bounds. Other algebraic reductions may also be possible.

## TP/DMFT: optimize the sampled full-time-grid solver

Use the same limiting process with a consistent numerical solver. Let S be
sampled representative paths, K the number of time steps, `h=T/K`, and r the
fixed order of the time discretization/quadrature. Assume the matched error
bound

\[
E\le A_D S^{-1/2}+B_D(T/K)^r+\eta.
\tag{10}
\]

Here A_D and B_D depend on m,H,T and include the relevant stability constants;
eta is the output-level solver tolerance. The uniform-in-grid sampling and
stability hypotheses are not established by the cited general papers.

The full-grid algorithm can stream one sampled path and its response Jacobian
at a time, accumulating kernel averages. Its moving storage is

\[
M_{D}(K)\asymp Hm^2(K+1)^2,
\tag{11}
\]

independent of S. Increasing S and tightening eta costs work, not this leading
memory. Therefore a memory-only optimization has a boundary infimum:

\[
K_{inf}=T(B_D/\epsilon)^{1/r},\qquad
M_D^{inf}\asymp Hm^2T^2 B_D^{2/r}\epsilon^{-2/r}.
\tag{12}
\]

For an actual finite feasible choice, reserve any fixed fraction beta in (0,1)
of epsilon for sampling/iteration and use

\[
K=\left\lceil T\left({B_D\over(1-\beta)\epsilon}\right)^{1/r}\right\rceil,
\quad
S\ge\left({2A_D\over\beta\epsilon}\right)^2,
\quad \eta\le\beta\epsilon/2.
\tag{13}
\]

This attains (12) up to a constant. Letting beta approach zero makes the
constant approach the continuous infimum, with diverging sampling/iteration
work. It is incorrect to call a finite S a unique optimum for memory alone.

Euler gives `Hm^2 T^2 B_D^2 epsilon^-2`; an r=2 solver, if its assumed error
estimate holds, gives `Hm^2 T^2 B_D epsilon^-1`. These are numerical
time-resolution orders, not response-memory orders P. The paper's practical
full-grid representation has a K^2 history cost, but no fixed epsilon exponent
is intrinsic to TP or DMFT as a mathematical framework.

If arbitrary numerical order is also to be optimized, further regularity and
order-dependent constants/costs must be supplied. For example, an available
stable analytic temporal approximation with error `D exp(-cK/T)` would give
`Hm^2 (T/c)^2 log^2(D/epsilon)` history storage. Such an approximation theorem
is not established for the general nonlinear process considered here. Raising
integrator order for free, with no extra stages and no constants, is invalid.

The distinction between GD and GF becomes essential here. If the target were
instead a fixed K-step population GD trajectory, streamed sampling could
reduce epsilon at fixed history memory by increasing S. For a continuous-time
target, temporal discretization must also tend to zero. We keep that same
continuous-time target throughout (1)--(13).

## Interpretation

Under the common conditional population error laws, the optimized leading
moving-state exponents for dense, old-clock, and joint-clock models are
4, 3, and 5/2 respectively. The old/new optimal width errors consume 2/3 and
4/5 of the budget; an equal split is feasible but not the exact optimizer.

NTH has an exponent determined by higher-kernel growth and sample count, with
the direct state count (5) and the conditional analytic solution (8). TP/DMFT
has the streamed numerical optimum (12), whose exponent depends on time
approximation order. Neither admits a universal best epsilon exponent from the
present matched theory alone. Their potentially smaller moving states can
coexist with expensive fixed coefficients, precomputation, or runtime.

The explicit factors m,H,T above must be read together with their error
constants. In particular, no claim is made that long-time accuracy has only
polynomial T cost: feedback amplification can enter those constants
exponentially. Unbounded labels, arbitrary conditioning, or different
initialization laws cannot be covered by a single universal function of
epsilon,m,H,T alone.

Verification: the allocation equations follow from the strictly convex
log-cost calculation; the NTH threshold is verified by substitution into
Lambert W's defining equation; the DMFT construction (13) sums to epsilon.
Source definitions were rechecked in the locally retained full NTH and DMFT
papers. No agents, new literature search, simulation campaign, paper edits,
or claims of new unconditional population theorems were involved.

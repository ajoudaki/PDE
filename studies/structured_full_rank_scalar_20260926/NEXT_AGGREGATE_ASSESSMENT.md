# The constructive route survives; the current economical cutoff does not

2026-09-27. Continuation after the J2 stress screen. This report separates
the mathematical existence question, the current cutoff's defect, and the
still-unresolved requirement of a practically useful accuracy/size tradeoff.
All new proofs are internal study derivations with separate technical
cross-checks, not promoted results in the maintained book.

## Decision

Continue the constructive route, but discontinue output-only J refinement as
the proposed convergence mechanism. There is now a mathematical obstruction
to convergence of some of that family's retained aggregates, and a different
aggregate family with a compact-time convergence guarantee for the actual
Gaussian **block** population over the whole circle. The general assertion
that all scalar aggregate approximations must fail is therefore too strong
for this fixed-block target.

The stronger engineering request is not resolved: no small aggregate ODE
with a convincingly good accuracy/size tradeoff has been produced. The new
first-level repair fits rapidly but still predicts the wrong circle function.
A formal polynomial construction below has severe dimension and time
dependence. It must not be sold as the efficient replacement the user asked
for. No theorem here identifies a fixed-k block population with the canonical
dense iid-Gaussian network; that is a separate initialization-replacement gap.

## 1. A permanent defect in the old order parameter

The current cutoff adds descendants of output moments as J grows. Its
feedback moments receive only a fixed number of derivative generations.
Differentiation of an output tree never removes its existing second-layer
vertex. It therefore cannot supply a missing moment supported solely on a
first-layer vertex, regardless of J.

This is more than a formal nonclosure observation. For one unit training
input, one nonzero label y, P=1, and canonical Gaussian initialization, use
the bounded current coordinates x=h1, beta=B0/L, alpha=A0/L^2, zeta=c/(2L).
Write brackets for the normalized population average. The retained moment
q=<beta^2 x^4> has an exact evolution term

    eta(t)=32 L^4 R tau <beta^3 x^3 (1-x^2)^2>,
    R=2<zeta h2>-y/L,   tau=<alpha zeta (1-h2^2)>.

The three monomials in this term are absent for every output depth J. On
the actual canonical orbit,

    eta(t)/t^3 -> 32 y^4 kappa mu > 0,
    kappa=<h2(0)^2 (1-h2(0)^2)^2>,
    mu=E[tanh(Z)^6 (1-tanh(Z)^2)^2],  Z~N(0,1).

The rest of this row depends on eleven retained moments and L, independently
of J once J>=2. Integrating the missing positive source and using the fixed
row's Lipschitz bound proves a positive, J-independent error floor for that
finite set on a sufficiently small fixed interval. The full statement and
proof are in [NEXT_OBSTRUCTION_ROUTE.md](NEXT_OBSTRUCTION_ROUTE.md), checked
separately in [NEXT_OBSTRUCTION_AUDIT.md](NEXT_OBSTRUCTION_AUDIT.md).

This result concerns those retained moments. A lower bound for the output
alone would require tracing their effect through the other equations and
excluding cancellations; that has not been established. It is also not a
lower bound against a different cutoff which expands the missing feedback.

There is a separate direct output certificate for each measured alias gap:
if the core and passive decoder give p and z at the same time and input,
then for any single-valued target f,

    max(|p-f|, |z-f|) >= |p-z|/2.

For the saved close-pair J2 gap 0.52853, at least one of those two prediction
errors is at least about 0.26426. This needs neither a finite-width reference
nor a fitted-endpoint comparison. It does not tell which decoder is closer.

## 2. A concrete repair was implemented and tested

Start from every output and feedback constituent, including every term in
dot-s. Expand all their derivative dependencies, not just output children.
The resulting complete dependency family has a bounded-mark finite-horizon
convergence argument. Its first level is smaller than the old J2 model.

The two new tests used the matched n=1024 initial pool, k=4, P=1, seed 1,
64 passive circle points and two passive training-input copies. All scalar
and reused reference endpoints below reached training MSE 0.001.

| Task | Scalar-block circle RMS | Scalar-dense-Gaussian circle RMS | Training seconds |
| --- | ---: | ---: | ---: |
| Opposite-label pair, 60 degrees | 0.252472 | 0.251199 | 0.716 |
| Orthogonal cosine pair | 0.081729 | 0.085372 | 0.687 |

Each model has 69,501 scalars for the full probe panel, versus 188,367 for
J2. The orthogonal case's prior fitted J2 scalar-block error was 0.050058,
so the reduction in state did not improve its accuracy. The opposite-label
case agrees with the block reference's training outputs to RMS 0.002615,
while differing by 0.252472 around the circle. This is a fully fitted
off-training failure. The old J2 endpoint on that task was unfinished and
is not treated as a matched-fit comparison.

No clipping was activated in either new run. Common initial moments match
the old runs bit for bit, and separate checks recomputed saved outputs,
reference comparisons, initialization, and source/data hashes. Total new
training was 1.403 seconds. No larger-order rescue or fresh reference run
was performed. These results reject practical success for this first-level
repair; they do not disprove convergence at increasing complete depth.

See [NEXT_DEPENDENCY_RESULTS.md](NEXT_DEPENDENCY_RESULTS.md) and its linked
protocol, code and independent saved-artifact audit for all details.

## 3. Gaussian blocks and the whole circle now have an existence theorem

The target here is the fixed-k, fixed-P Gaussian-block population closure
with zero initial readout, fixed bounded training labels and tanh activation.
It is not an assertion about replacing a dense iid-Gaussian middle matrix.

First project each Gaussian initialization block radially to norm at most R.
This preserves its rank and only changes blocks outside that ball. Tail mass
alone would not bound the eventual error, because changed blocks alter the
shared feedback. A comparison of the two full population flows instead gives

    e' <= C_T[(1+s^2)e + M exp(-a s^2)],   1<=s<=R.

Here e measures coupled block-state and clock differences in a bounded
metric. Two matrix factors are the worst dependence in the good-block
stability estimate. Optimizing s in terms of e gives an Osgood inequality
e' <= C_T e(1+log(M/e)), with a small cutoff source. Its integrated form
controls the trained output difference by C_T exp(-c_T R^2), including
the changed feedback.

Second, retain separate passive-input moment families sharing only their
training moments. A passive derivative never creates a different passive
input, so M probe families cost M times the one-query count rather than
increasing the base of an exponential count. The true circle output has a
finite, cutoff-uniform Lipschitz constant K_T. Periodic interpolation of M
evolving output aggregates therefore costs at most pi K_T/M. This is a grid
of requested input observables, not a grid of neuron states or a density.

Together with bounded-moment propagation through degree D, the error obeys

    sup_(t<=T,theta)|fhat_(D,R,M)-f|
       <= C_T exp(-c_T R^2) + pi K_T/M
          + exp[C_T(1+R)^2] exp{-D exp[-C_T(1+R)^2]}.

One can choose R and M from D alone so this converges for every finite T,
with no growing state during a run. The proof also has a width-uniform
conditional form for finite empirical block laws with a common exponential
seed-moment bound. Gaussian sampling supplies such an envelope with a
width-independent high-probability constant, for each width; it is not an
unconditional bound on every possible Gaussian realization.

The complete derivation, scope and initialization conditions are in
[NEXT_GAUSSIAN_ROUTE.md](NEXT_GAUSSIAN_ROUTE.md). This proof resolves the
earlier Gaussian-cutoff and full-circle existence gaps. Its initial tree
count gives an extremely poor error/size rate.

## 4. A formal polynomial bound still carries a severe dimension cost

There is also a way to obtain an algebraic bound in scalar state count at
fixed k,m,P. Expand only the ordinary current-coordinate monomials generated
from outputs and feedback by differentiation, with the within-block indices
explicit. Different graph expressions can then use the same finite list of
coordinate products. This does not evolve a population or reconstruct its
density. The ambient monomial count is an upper bound on the generated set,
not an instruction to enumerate the entire joint-law basis.

For training plus one passive input the local coordinate count is

    d=k^2+k(2m+3+2mP),

and degree-D monomials number at most binomial(D+d,d). Evolve O(log D)
independent bounded-mark aggregate hierarchies with R_j=sqrt(j), each with
its own residuals and memory clock. Add one physical-time clock. A prescribed
continuous decoder selects between nearby cutoffs using a computable
stability envelope from the equations, not reference data. This keeps all
ODE sizes fixed during training while choosing a certifiable cutoff at each
time. With D passive circle nodes, the resulting family satisfies

    N_D <= C_d D^(d+1) log D,
    sup_(t<=T,theta)|fhat_D-f| <= A_T D^(-eta_T)
                               <= A'_T N_D^(-eta_T/(d+2)),
    eta_T>0.

The family is independent of a chosen terminal horizon. Its error constants
and positive exponent depend on T and the fixed structural parameters.
The proof is [NEXT_POLYNOMIAL_ROUTE.md](NEXT_POLYNOMIAL_ROUTE.md).

This formal polynomial statement is **not a claim of useful compression**.
For k=4,m=2,P=1, d=60. The degree-nine ambient count is 56,672,074,888;
this is an upper bound, not a measured reachable-state count, but it exposes
the weakness of the certificate. The exponent also deteriorates with time.
No small reachable set or practical implementation of this theoretical
family has been demonstrated. A high-dimensional moment basis must not be
presented as an effective solution merely because its fixed-parameter
asymptotic count is polynomial.

Initialization need not fall back to an exponentially expensive Lipschitz
grid. [A further derivation](NEXT_POLYNOMIAL_INITIALIZATION.md) splits the
Gaussian matrix radial integral exactly at the clipping radius, and then
uses analytic tensor quadrature for the two smooth pieces. It computes the
required exp(-D) initial-moment accuracy with polynomial work in D at fixed
k,m,P. All quadrature seeds are discarded. Its exponent contains the
k^2+2k seed dimension, so this is again a formal complexity result, not a
cheap initializer. A polynomial bound for numerical integration of the ODE
at the certified output accuracy has not been proved.

Separate complete-read technical checks are recorded in the
[state-count audit](NEXT_POLYNOMIAL_ROUTE_AUDIT.md) and
[initialization audit](NEXT_POLYNOMIAL_INITIALIZATION_AUDIT.md). They found
no material mathematical gap in the stated fixed-parameter claims. They do
not certify numerical usefulness or substitute for promotion review.

## 5. What is resolved, and what remains

Resolved within the stated fixed-block model: the old output-depth family
has a permanent feedback defect; an admissible aggregate hierarchy can
approximate the population output over the whole circle on every finite
interval; and a formal fixed-parameter algebraic state-count guarantee can
be constructed. These conclusions prevent the observed failures from
supporting a universal scalar-impossibility claim.

Unresolved: an aggregate representation with a useful exponent and modest
state counts on the actual tasks, a convincing measured accuracy/order
curve, a full efficient numerical-integration guarantee, and convergence of
the block-initialized target to the canonical dense-Gaussian fitted function.
The new inexpensive feedback repair did not solve those problems.

The research decision is therefore constructive, with a narrower practical
claim: stop interpreting J-only refinement as convergent, and require a
new low-cost representation to preserve the relevant feedback and pass
matched population-output tests. The broad mathematical obstruction route
is unsupported; the requested effective compression has not been completed.

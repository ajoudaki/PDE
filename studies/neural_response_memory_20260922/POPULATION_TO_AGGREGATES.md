# Reducing the chronological population closure to global scalar observables

2026-09-25. Continuation explicitly directed to this study. The target is the
existing fixed-P Legendre population closure, including its actual initialized
operators and their adjoints. This note supersedes the choice to test a direct
dense-network derivative hierarchy as an answer to the population-compression
question. That separate experiment is archived on
`codex/experimental-direct-dense-scalar-20260925`.

The constructive result here is an exact starting aggregate map, its first
evolution equations, and a systematic scalar contraction hierarchy derived
from the population equations. An explicit finite truncation and its precise
error source can be specified. A useful small truncation, an unconditional
refinement-convergence theorem, and efficient width-independent initialization
have not been established. The zero-tail truncation below is a reference
construction exposing the approximation, not an endorsed accurate solver.

## 1. What is being compressed

Fix the history order P and the number M of training examples. Write the
existing autonomous collective state as m'=F_P(m). It includes neuron fields,
their retained history moments, the outer weights and the activity clock.
The initial internal operators are fixed parameters of this system.

The proposed second reduction has a state q in R^N consisting of global
averages or contractions. N may depend on P, M, input dimension, chosen test
observables, accuracy and horizon, but should not depend on neuron width or
the number of elapsed steps. It may contain many scalar equations. It must
not contain a hidden neuron ensemble, a density function, a growing history,
or an initialized matrix requiring unrepresented neuron vectors at runtime.

For finite-width initialization, one-time evaluation of the chosen scalar
contractions using the initialized network is permitted and must be counted
as preprocessing. A deterministic population-limit initialization formula
is a separate claim. No trained dense or population trajectory supplies
coefficients to the reduced evolution.

The scientific order of comparison is now

    dense dynamics -> fixed-P population closure -> scalar aggregates.

This study already has evidence about the first arrow. The second arrow
has a new error source and needs its own validation.

## 2. An explicit finite starting aggregate state

Use the three-hidden-layer construction in DEEP_CIRCLE_DERIVATION.md; the
two-hidden-layer version follows by removing one internal link. H_{ell,a}
and Delta_{ell,a} are its current activation and residual-free backward
fields. A_{ell,k,a} and B_{ell,k,a} are its backward and forward history
moments, respectively. Their layers differ: A_ell belongs to layer ell and
B_ell to layer ell-1. E_ell contracts only fields in layer ell.

At finite width E_ell[UV] means u^T v/n. These are exact empirical identities,
without an independence assumption. At an infinite population the same
formulas require an existing solution and enough integrability to justify
the products, operator actions and differentiation.

Take the within-layer second moments of the following finite field lists:

    layer 1: 1, first-weight columns, H1,q, Delta1,q, B2,k,a;
    layer 2: 1, H2,q, Delta2,q, A2,k,a, B3,k,a;
    layer 3: 1, c, H3,q, Delta3,q, A3,k,a.

Here a ranges over training examples and q over training plus a fixed finite
list of passive query inputs. Include the activity length L and residual RMS
rho. The constant field includes means among these second moments. The
backward fields are a redundant exact lift, not independent random variables.

For J training-plus-query inputs the list lengths are
1+d+2J+MP, 1+2J+2MP and 2+2J+MP. Thus the number of these scalar averages is
independent of width. This is an observable map, not yet a closed ODE.

In particular it contains the current outputs f_q=E_3[c H3,q], all history
Grams and their same-layer cross moments. The history Grams have exact
transport equations involving mixed current/history pairings. Those equations
are derived explicitly in POPULATION_AGGREGATE_EQUATIONS_CHECK.md, (9)--(10).
The important question is the evolution of the whole list, not whether its
entries are scalar or whether some subset has a closed first derivative.

## 3. Output velocity follows directly from the population closure

Let r_a=f_a-y_a, rho^2=M^(-1)sum_a r_a^2, L'=rho, and define the history
endpoint reconstructions

    Abar_{ell,a}=L^(-1)sum_{k<P}(2k+1)A_{ell,k,a},
    Bbar_{ell,a}=L^(-1)sum_{k<P}(2k+1)B_{ell,k,a}.

The bar denotes a history projection endpoint, not a population mean.
Differentiating the closure's reconstructed operator and using its exact
Legendre transport gives

    W_ell' = -(2/M)sum_a [
        r_a Delta_{ell,a} tensor Bbar_{ell,a}
        + rho Abar_{ell,a} tensor (H_{ell-1,a}-Bbar_{ell,a})].

Here U tensor V acts on z as U E[Vz]. This is the fixed-P closure's velocity;
replacing it by the dense gradient velocity would remove its history defect
and change the target being reduced.

Define scalar contractions

    C_ell(q,a)=E_ell[H_{ell,q}H_{ell,a}],
    R_ell(q,a)=E_ell[Delta_{ell,q}Delta_{ell,a}],
    S_ell(a,q)=E_{ell-1}[Bbar_{ell,a}H_{ell-1,q}],
    T_ell(q,a)=E_ell[Delta_{ell,q}Abar_{ell,a}],
    G_qa=x_q^T x_a/d.

The chain rule, the actual adjoints and the exact outer-weight equations yield

    f_q' = -(2/M)sum_a r_a [C_3(q,a)+G_qa R_1(q,a)]
           -(2/M)sum_{ell=2,3; a} [
               r_a R_ell(q,a)S_ell(a,q)
               +rho T_ell(q,a)(C_{ell-1}(a,q)-S_ell(a,q))].

Every quantity on the right is in the starting scalar list. This identity
holds for training and passive-query outputs, with no query labels or query
contribution to training. The loss derivative is exactly

    loss'=(2/M)sum_a r_a f_a'.

Thus the output and loss can be read and their first velocities computed
without identifying any individual neuron. This positive result does not
yet determine the future values of all the contractions on the right.

## 4. Which new variables appear

For example, let V_{k,a;b}=E_1[B_{2,k,a}H_{1,b}]. Its exact derivative is

    V_{k,a;b}' = rho C_1(a,b)
        -(rho/L)[k V_{k,a;b}+sum_{j<k}(2j+1)V_{j,a;b}]
        -(2/M)sum_c r_c G_bc
                     E_1[B_{2,k,a}(1-H_{1,b}^2)Delta_{1,c}].

The last expectation contains the fourth mixed moment
E_1[B_{2,k,a}H_{1,b}^2 Delta_{1,c}], in addition to an existing second
moment. At the next layer, the same operation produces terms such as

    E_2[B_{3,k,a}(1-H_{2,b}^2)
            W_{2,0}((1-H_{1,b}^2)Delta_{1,c})].

This is still one scalar. It carries a specific correlation between both
populations and the initialized operator. A product of separate means cannot
replace it exactly without a proved factorization relation. Gaussian initial
matrix entries do not justify refreshing that operator independently after
its repeated use in training and backpropagation.

These calculations give a systematic rule: differentiate each retained
observable with F_P, simplify identities, and add the unresolved contractions
needed by its derivative. The moment transport, activation gates and actual
operator actions dictate the new variables. There is no choice of a new
dense-network Taylor model in this step.

## 5. Exact finite closure versus a finite approximation

For an aggregate map A(m), an exact autonomous law q'=g(q) requires

    DA(m)F_P(m)=g(A(m))

on a declared admissible restart family. Equivalently, two states with the
same retained aggregates must have the same aggregate velocities. The forward
implication follows by substitution; for the reverse, define g at an aggregate
value using any state attaining it. Equal velocities make this definition
single-valued. Suitable regularity and uniqueness of g are additionally needed
for a uniquely restartable ODE.

A useful sufficient algebraic condition is that the algebra generated by the
retained observables is invariant under differentiation with F_P and contains
the desired outputs. Then every derivative is already a function of retained
scalars. This condition allows nonlinear scalar equations; an invariant finite
linear span would be stronger than necessary.

An example of sufficient extra structure is a fixed finite-dimensional
within-layer field algebra, closed under multiplication, containing the
initial fields, and preserved by both directions of the initialized operators.
All response and moment equations then remain in those algebras. Coefficients
can be recovered through a finite set of global pairings with dual basis
fields. Its dimension and stored coefficients must be independent of width;
one basis vector per neuron would merely rename the original system. Such
structure has not been established for the present Gaussian/tanh model.

The supplied sources therefore do not prove an exact small finite scalar
reduction. They also do not prove that every richer finite reduction fails.
In particular, the finite mean/Gram counterexample in
POPULATION_FINITE_CLOSURE_CHECK.md excludes its stated primitive-field list
on a broad finite restart class; it does not exclude the list augmented with
backward fields above or a narrower Gaussian population reachable family.

## 6. A specified scalar hierarchy and the exact approximation step

The response lift is particularly useful here: tanh gates are exactly 1-H^2
on its invariant manifold. One can compile the fixed-P vector field into
typed scalar contraction diagrams: vertex decorations are local response,
weight or history fields, and edges represent the actual W20 or W30 actions.
Every neuron index is summed. There is no open neuron index in a scalar
coordinate.

POPULATION_SCALAR_CONSTRUCTION_CHECK.md specifies this compiler completely.
At finite n it uses C_ell=n W_{ell,0} on an edge and one factor 1/n for each
summed vertex. For example,

    n^(-2)sum_{i,j} u_i C_ell(i,j)v_j = u^T W_{ell,0}v/n.

Forward and transpose contractions share these same edges. Disconnected
diagrams factor exactly into products of their connected components because
all summation indices are independently summed, with collisions included.
Repeated differentiation consequently gives exact equations for a countable
list of connected scalar contractions. This is an identity hierarchy along
each existing fixed-P trajectory. Abstract infinite-system uniqueness and
population identification do not follow from writing these identities.

For a finite cutoff K, retain connected diagrams with at most K total
vertices, edges and decorations. There are finitely many types independent
of n, for fixed sample count, P and query set. One explicit reference closure
deletes a generator monomial if any of its connected factors is omitted.
All remaining coefficients and factors are kept exactly. Keep

    rho(q)=sqrt(M^(-1)sum_a(f_a(q)-y_a)^2),    L'=rho(q).

This supplies a finite locally Lipschitz autonomous ODE on L>0, using only
scalar coordinates and coefficients after initialization. It is closed by
construction. It is not thereby an exact reduction or a convergent
approximation. The deleted contractions can be large, and the resulting
moments need not stay realizable or produce decreasing loss. We have not
selected this zero-tail rule as the next practical solver.

More generally, if the exact retained equations are

    q'=F(q,u),

where u lists the specific unresolved contractions, a finite reconstruction
u=C_K(q) defines the closed approximation

    qhat'=F(qhat,C_K(qhat)).

Its sole extra approximation relative to the fixed-P population model is
this replacement, and its exact velocity defect on the target trajectory is

    eta_K(t)=F(q_P(t),u_P(t))-F(q_P(t),C_K(q_P(t))).

For the reference deletion rule, eta_K is precisely the sum of the deleted
generator monomials, enumerated in the construction note. In a practical
model C_K and all its coefficients must be specified from admissible
information; writing an unknown conditional expectation would not finish
the construction. Neither u_P nor eta_K is a forcing supplied to the solver.

If both paths exist in a common region where the reduced vector field is
Lambda_K-Lipschitz, subtraction of their equations and the integrating-factor
inequality give, for matching initialization,

    ||qhat(t)-q_P(t)||
      <= integral_0^t exp(Lambda_K(t-s)) ||eta_K(s)|| ds.

A norm controlling the requested outputs transfers this bound to them.
Convergence follows if that full propagated error tends to zero, with the
necessary containment and readout bounds. We do not currently have a derived
tail estimate and stability control proving this limit for the diagram
truncation. Increasing moment order alone does not make it a small parameter.
Finite type count also does not ensure cheap preprocessing: brute-force
evaluation of a diagram with v vertices can require n^v operations.

There is a concrete additional limit issue with retaining all graph types.
The undecorated two-vertex diagram with two parallel initialized edges has
value ||W0||_F^2. For independent N(0,1/n) entries its mean is n and its
variance is 2: there are n^2 squared entries, each with mean 1/n and variance
2/n^2. Thus this raw scalar diverges with width, even at initialization.
The complete all-graph dictionary as normalized above has no finite
coordinatewise population limit. Restricting to a sufficient family actually
generated by the requested observables, or choosing suitable renormalizations,
requires further justification. This does not invalidate the finite-n
identities or rule out a useful scalar output reduction; it prevents treating
the reference dictionary itself as an already constructed population limit.

## 7. Full-circle output and meaningful validation

A scalar readout can define a function at every angle. One concrete choice
is to add passive response observables at a fixed circle grid and interpolate
their scalar outputs periodically. The query response equations use the same
population weight velocities; they never enter the training residual or
history source sums. Their contraction derivatives are compiled in the same
way. No neuron forward pass is needed at query time after compression.

If the target fixed-P circle function has angular Lipschitz constant B on a
given time interval, a nearest-grid readout with grid covering radius h has
uniform error at most the maximum scalar query error plus B h. Its circle
RMS error has the same upper bound. Thus finite angular representation is
a separate explicit approximation, not silently an exact every-angle oracle.

At matched training-loss thresholds, denote each model's resulting circle
function by f_scalar, f_P and f_dense. The exact triangle inequality is

    RMS_circle(f_scalar-f_dense)
      <= RMS_circle(f_scalar-f_P) + RMS_circle(f_P-f_dense).

Every endpoint must first pass its training-loss and numerical validity
criteria. Different models may reach that threshold at different physical
times. The compact-time velocity estimate above does not itself prove control
of those stopping times or of infinite-time fitted endpoints.

The immediate diagnostic for a proposed C_K is its specified aggregate
velocity defect against the population closure at the same population state,
followed by an independently evolved scalar-versus-population comparison.
Defect measurements are validation, not a source of runtime refreshes or
undisclosed fitted forcing. Dense comparison then measures the first and
second reductions separately. No new training campaign was run here.

## 8. Checks and current claim levels

The complete source construction and its Legendre correction were read, as
were the complete three scoped derivations named above. The exact first
aggregate equations were checked against the existing population engine,
both by direct chain rule and by automatic directional differentiation of an
independently written reconstructed-network map. All 198 comparisons passed,
with maximum normalized discrepancy 3.33e-16; tolerance was 2e-11. These CPU
checks used width 7 only as a bounded algebra test, P=1,2,3, initialization
and nonzero-history algebraic states, and two passive queries. They are not
small-width training experiments or evidence for population approximation.

Source: check_population_aggregate_equations.py. Evidence:
data/generated/neural_response_memory_20260922/population_aggregate_algebra01/results.json.
The graph truncation is a mathematical construction, not an implemented or
empirically validated scalar solver. The supporting notes state their exact
input scopes and distinguish author checks from promotion reviews.

Established here are the finite-width aggregate identities, an explicit
starting observable map, the exact closure criterion, and a reference scalar
truncation with an identified remainder. Conditional results include finite
invariant-algebra reduction and the defect-propagation estimate. Open are
useful scalar-tail control, stable efficient finite closure, width-uniform
initialization and accuracy, and any exact population or all-time limit for
the new reduction. The abandoned direct-dense experiment answers none of
these questions.

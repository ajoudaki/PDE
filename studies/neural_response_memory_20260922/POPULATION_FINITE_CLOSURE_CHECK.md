# Scalar contraction hierarchy: exactness, finite closure, and its limits

Scoped mathematical check, 2026-09-25. Inputs read completely:
`MOMENT_CONSTRUCTION.md`, `DEEP_CIRCLE_DERIVATION.md`, and
`docs/NOTATION.md`. Process inputs: the investigate-conjectures and
solve-math-rigorously skills, and the former's research-contract and
adversarial-audit references. No other study, experimental result, training
run, implementation, or Git state was used. This is a bounded theory input,
not a promotion review.

The strongest unconditional conclusion from these inputs is an exact
observable identity hierarchy along each existing finite-width, fixed-P
surrogate trajectory. A finite neuron-free closure, uniqueness of an
autonomous infinite hierarchy, population identification, and convergence of
finite graph truncations require additional statements.

## 1. What can be called exact

Let V be the fixed-P response-lift vector field in the derivation, on its
consistent manifold with rho>0 and L>0. An observable expression is built
from the retained fields, scalar coordinates, fixed data, componentwise
products, the actual initialized forward and transpose actions, and
same-layer normalized pairings. Each scalar expression can be represented
by a finite typed contraction graph. Include disconnected graphs to cover
products of scalar contractions; scalar means also require the constant
field 1. Graph expressions must preserve the finite action and normalization
conventions, rather than treating an n^(-1/2)-scaled initialized matrix as an
ordinary bounded graphon kernel.

For each such observable O, define the Lie derivative

    D_V O = DO[V].

The product rule, linearity of each fixed initialized action, and the
explicit rational vector field express D_V O as a finite combination of
the same kind of scalar expressions. Thus, after closure under this operation,

    q_O(t) = O(state(t)),       qdot_O = (D_V O)(state(t))

is exact along the original fixed-P surrogate. This exactness does not remove
its previously identified Legendre approximation relative to the dense flow.

Polynomialization is optional: adjoin a=1/L and b=1/rho and set

    adot = -rho a^2,
    bdot = -b^3 S,     S = M^(-1) sum_sample r_sample fdot_sample.

Together with rhodot=b S these preserve aL=brho=1. Including all scalar
monomials then makes a formally linear, countable Carleman system possible.
The chart ends at rho=0; the absorbing compatible boundary in the original
construction must be handled separately. Adding b does not regularize it.

At finite width every finite expression is defined. At population level,
this assertion is conditional on the corresponding expressions being
defined, integrable, differentiable in a topology allowing the contractions,
and on the initialized operator and its adjoint having the requisite
domains. A bounded L2 operator alone does not ensure that repeated products
and alternating actions are defined: L2 is not closed under multiplication.
Nor need a bounded Gaussian population action have a pointwise kernel.
Operator-expression graphs remain meaningful under suitable domain estimates;
kernel-integral graphs need their own representation theorem.

There are three different meanings of exact here:

1. Every finite observable identity is exact along an existing state solution.
2. The sequence of these observables solves the written countable equations.
3. Those equations, with admissible initial data, independently have a unique
   solution that reproduces the required population outputs.

The algebra proves the first two once expressions exist. It does not prove
the third. A topology, growth or tail class, realizability constraints and
uniqueness are needed. For perspective, the countable equations
qdot_k=q_(k+1) have nonzero smooth solutions with all initial coordinates zero:
take q_k to be the kth derivative of exp(-1/t^2), extended by zero at t=0.
This is an illustration of the missing uniqueness premise, not a proof that
this study's fully constrained hierarchy is nonunique.

All initial graph values must also be specified. Supplying every contraction
of the realized initialized matrices is infinite instance information, even
if their entries no longer appear in the dynamic RHS. Gaussian initialization
can replace this only after a theorem computes the relevant limiting
contractions and validates the evolution. Training creates dependencies
between those matrices and their forward/backward arguments. Replacing
either direction by a new independent Gaussian map changes the system.

## 2. A finite autonomous closure criterion

Let S be the declared admissible restart family, and q:S -> R^D be a regular
map consisting of permitted scalar global observables. A sufficient exact
closure criterion is

    Dq(x)V(x) = B(q(x))    for every x in S,
    required_output(x) = H(q(x)),

where B is locally Lipschitz and the coefficients, q(x(0)), and H are
computable from permitted initial information. Then the ordinary chain rule
and uniqueness give qdot=B(q), and H(q(t)) is the exact output. D and the
description of B,H must obey the intended width-independent complexity bound.
The family S must be invariant for the claimed horizon, or the criterion
must hold on every visited state. Restricting S to one observed trajectory
would conceal the required restart and provenance problem.

The fiber test is necessary: if q(x)=q(y), then Dq(x)V(x) and Dq(y)V(y) must
agree. A useful algebraic sufficient version is that a finitely generated
observable algebra R[q_1,...,q_D] is invariant under D_V and contains the
outputs. A rational version uses a localized algebra on the stated
denominator chart. Finite generation is the relevant condition; requiring
a finite-dimensional invariant linear span would impose a stronger, often
unnecessary linear-closure requirement.

A concrete structural sufficient condition is available. At each layer take
a fixed finite-dimensional algebra of fields containing 1 and every initial
dynamic field. Require it to be closed under pointwise products, and require
each initialized forward action and its true adjoint to map the corresponding
layer algebras into one another. The finite-P RHS then stays in these algebras.
Coordinates can be recovered by a finite list of scalar pairings with fixed
dual test fields, yielding an exact finite scalar ODE. The algebra dimensions,
operator-action coefficients and their initialization descriptions must be
bounded independently of width. Fixed finite partitions with invariant
cell-constant actions are one example. This is a sufficient special structure,
not a property established for the Gaussian initialized model. Allowing one
partition cell per neuron would simply restore the original state.

## 3. A clean means-and-Grams obstruction in the actual finite lift

Consider one sample, d=1, n=2, U=1, y=1, and any P>=1. Fix

    W1 = w(1,1)^T,       q=tanh(w),       p=tanh(q),
    W20 = I,            W30 = [[1,-1],[0,0]].

Compare c_A=epsilon(1,0)^T and c_B=epsilon(0,1)^T, with epsilon nonzero.
Both compatible initial states have

    h1=q(1,1)^T,   h2=p(1,1)^T,   h3=0,
    A2=A3=0,      B2,0=h1,       B3,0=h2,

with all higher B coordinates zero and L=rho=1. Therefore all same-layer
means and pairwise normalized products of the retained primitive fields
W1,c,h1,h2,h3,A2,B2,A3,B3 agree. In particular f=0 agrees. The initialized
matrices are exactly the same in the two states.

Write d1=1-q^2 and d2=1-p^2. The backward fields satisfy

    delta2_A = epsilon d2 (1,-1)^T,     delta2_B = 0,
    delta1_A = epsilon d1 d2 (1,-1)^T, delta1_B = 0.

At initialization both closure defects vanish for every P, so the physical
velocities equal the dense gradient velocities. For this one-sample model,

    fdot = -2r [ ||delta1||^2/n
                  + ||delta2||^2 ||h1||^2/n^2
                  + ||delta3||^2 ||h2||^2/n^2
                  + ||h3||^2/n ].

The last two terms agree between the two states. Since r=-1 and n=2,

    fdot_A - fdot_B
      = 2 epsilon^2 (1-p^2)^2 [ (1-q^2)^2 + q^2 ] > 0.

The output f itself is one retained-field Gram entry. Its derivative is
therefore not a function of all those means and Grams. The missing
information is alignment with initialized operator actions, even before
considering higher nonlinear moments.

This is a forward-compatible, correctly moment-initialized example in the
finite Gaussian initialization support: the stipulated Gaussian joint law
has full support in all finite parameter entries. Although these particular
points have probability zero, a closure identity jointly continuous in the
initial parameters and the aggregate coordinates, and valid almost surely
under that law, would hold everywhere in its support by continuity,
contradicting this pair. Thus it also rules out such a jointly continuous
almost-sure identity over the full finite initialization class. If the
coefficient prescription is merely measurable in the initialized matrices,
this support argument alone does not establish an almost-sure obstruction.

Scope matters: the example is not the one prescribed seeded realization;
it is not a counterexample to a separately proved Gaussian population
reachable-state closure; and it does not defeat larger lists containing
operator-decorated contractions. In particular, the population limiting
initial readout is zero, so this finite-state example cannot silently be
used as a nonzero population initialization.

## 4. A sufficient finite-approximation estimate

An approximate finite closure requires a small closure defect and stable
propagation. For permitted scalar observables q_N and a computable finite
vector field B_N, suppose along the target trajectory on [0,T]

    d/dt q_N(x(t)) = B_N(q_N(x(t))) + e_N(t),
    ||e_N(t)|| <= epsilon_N.

Assume B_N is Lipschitz with constant K_N on a common region containing the
target observable path and approximate path z_N, and initialize z_N with
error at most delta_N. Integrating the difference inequality gives

    sup_[0,T] ||q_N(x(t))-z_N(t)||
       <= exp(K_N T) delta_N
          + epsilon_N (exp(K_N T)-1)/K_N,

where the final quotient is T when K_N=0. If the output reconstruction H_N
has Lipschitz constant C_N and error at most eta_N on the target state, add
eta_N and multiply the displayed bound by C_N. Convergence follows when
that full bound tends to zero. Merely having epsilon_N -> 0 is insufficient
when the propagation or reconstruction constants grow uncontrolled.

For a useful graph truncation theorem, the substantive missing estimate is
the residual epsilon_N from omitted contractions on the actual reachable
family. The Legendre error estimate controls P, a different truncation
axis; it supplies no decay in graph size, population polynomial degree, or
initialized-operator word length. Finite-width estimates must be uniform
in n, including their probability/tail statements, before they can justify
a width-independent approximation. Population identification additionally
requires convergence and uniform integrability for the relevant graph
observables. A claim uniform over all physical time needs separate decay or
long-time stability; this compact-time estimate does not provide it.

The productive conditional statement is therefore: at fixed P and fixed
physical horizon, find a permitted finite graph family whose omitted
generator terms are small in a specified norm and whose finite evolution is
stable in that norm, with all constants and initialization control uniform
in the intended population or width class. Neither that condition nor a
finite invariant observable algebra is established by the two source notes.

## 5. Collaborative audit of the frozen scalar candidate

Additional explicitly assigned input, read completely:
`POPULATION_SCALAR_CONSTRUCTION_CHECK.md`, SHA256
`a0800aa99d03d6d21a6dd89a9facd34636a6e17ac66ab56308d4459414bc848c`.
This is a collaborative check of that frozen version, not an independent
promotion review. No new scientific input, code execution, training, or Git
operation was used. Zero-tail deletion is assessed as an explicit reference
truncation, not as an endorsed accurate practical model.

### Finite-width algebra and construction

The normalization C=nW0 is correct. Every initialized action becomes
(1/n) sum C times its argument, so adding one summed vertex to a rooted
expression adds exactly the required factor 1/n. The outer normalized
contraction supplies the root factor. Repeated index assignments are
included, so graph collisions cause no missing correction. The source's
transpose actions use the same edge values with the original layer roles.

For disjoint H1,H2, the assignments to the two vertex sets are independent
summation variables, even though some assignments take equal numerical
indices. Thus the two finite sums factor exactly and
q_(H1 disjoint-union H2)=q_H1 q_H2. This is an algebraic factorization of
sums, not probabilistic independence. Factoring disconnected components
therefore loses no information at finite width.

The finite type-count claim is valid: the numbers of vertices, edges and
decorations are bounded by K, the layer/edge/species alphabets are finite,
and relabeling leaves finitely many graph types. The count is independent of
n. Static contractions must count toward storage as the candidate explicitly
requires; coefficients cannot additionally conceal per-neuron arrays.

The compiler rules are consistent with the source equations. Each primitive
field velocity is a finite rooted expression involving componentwise
products, fixed initialized actions, global pairings, rho, residuals and
inverse powers of L. The only 1/rho in the source is in the optional
rhodot equation; it does not enter the primitive field velocities.
Consequently diagram differentiation has exactly the rational-in-L,
polynomial-in-rho-and-residuals coefficient structure stated. A finite
maximum size increment Delta exists because differentiating one decoration
substitutes one member of a finite rooted-expression list. Delta bounds each
connected boundary component, even when the replacement creates multiple
disconnected factors.

Deleting a whole monomial when any factor is omitted is a definite finite
autonomous closure. Replacing only that factor by the number 1 would be a
different method; the candidate correctly uses zero. Exact initialization
of its retained scalar list uses permitted finite-width preprocessing only.
After preprocessing, its RHS needs neither evolving neuron fields nor
initialized matrix actions. Its dimension and coefficient-table length at
fixed K are independent of width. No accuracy or preprocessing-cost claim
follows from this fact, and the candidate does not rely on one.

Zero-residual stationarity survives this deletion: every primitive source
term contains at least one factor r_a or rho. The reconstructed matrix
velocities and response chain rules preserve that factor property.
Product-rule differentiation and disjoint-component factorization do not
remove those factors. Hence each expanded monomial, including each retained
one, vanishes when all r_a=rho=0. With rho the norm of the residual vector,
the finite RHS is locally Lipschitz on L>0; Ldot=rho>=0 preserves L>=1.
This proves local well-posedness, including the zero-residual state, but not
global existence, moment realizability, or stability. The optional rational
rho equation is equivalent only on the positive-rho chart, exactly as stated.

The conditional error theorem is valid. For the exact target's retained
coordinates, deletion separates its derivative into F_K plus the explicit
boundary remainder. Subtracting the finite ODE and applying the assumed
common-region Lipschitz bound gives the stated integral estimate. Exact
initial values remove the initial-error term. Output convergence follows
under its stated C_K-weighted remainder-and-propagation condition. That
condition has not been proved and is not implied by rationality, by finite
type count, or by Legendre refinement. The theorem consequently gives no
unsupported unconditional convergence conclusion.

### Required qualification: finite width versus population

The candidate fixes n and defines each q_H by a finite matrix sum. Its
proved target should consistently be called X_(n,P), the finite-width
fixed-P closure. In particular, the sentence saying that identities exact
for every finite n prove that the intended population trajectory provides
an infinite solution needs this qualification. The latter conclusion for
an infinite population requires the separate domain, integrability and
limit statements that the candidate itself recognizes.

There is also a concrete obstruction to a direct population limit of its
entire all-connected-graph state. Let H have two vertices in adjacent layers,
two parallel initialized edges, and no dynamic decorations. Its size is
four, so it is retained for every K>=4. The candidate's exact normalization
gives

    q_H = n^(-2) sum_(i,j) (n W0,ij)^2 = ||W0||_F^2.

For the specified independent Gaussian entries W0,ij~N(0,1/n),

    E q_H = n,          Var(q_H) = 2.

Indeed there are n^2 independent squared entries, each with mean 1/n and
variance 2/n^2. Thus E|q_H/n-1|^2=2/n^2, and q_H diverges in probability.
This retained coordinate has no finite real-valued population limit even
at initialization. Its divergence does not invalidate finite-width scalar
storage, since one ordinary scalar can hold its finite value for every n,
and it does not invalidate the conditional finite-width error estimate.
It does prevent treating the complete fixed-K list as an already defined
finite-coordinate population state with this normalization.

Possible repairs include selecting only a suitably controlled family of
graphs reached from the required observables by the generator, changing
normalization graph by graph while recompiling the generator, or supplying
another specified representation and topology. None is established here.
In particular, the divergence of this overcomplete coordinate is not a
no-go theorem for finite scalar approximations of the outputs. It identifies
a necessary correction to the population interpretation of this candidate.

Subject to that qualification, the frozen candidate honestly supplies a
finite-width finite scalar reference system, an exact named deletion
remainder, and a correct conditional compact-time error theorem. It supplies
neither an accurate practical cutoff nor a convergent population hierarchy.

## 6. Corrected candidate and root synthesis: final collaborative check

The supervisor explicitly extended the input scope to the complete root
synthesis `POPULATION_TO_AGGREGATES.md`. I read it completely, then reread
the complete corrected synthesis and scalar candidate after the corrections
above. The final checked SHA256 values are:

| Artifact | SHA256 |
|---|---|
| `POPULATION_TO_AGGREGATES.md` | `99cf7504e058e076d68ecd4e61c1493e7ce1d2c11dcf94f544012d507b529ebb` |
| `POPULATION_SCALAR_CONSTRUCTION_CHECK.md` | `8a2e44ad6d50995ef626a65402babed19b761f9685d9ef91fb63de7633944383` |

The corrected candidate consistently states its proved target as the
finite-width X_(n,P), labels zero-tail deletion a reference construction,
and explicitly proves the parallel-edge divergence. It preserves the exact
finite-width generator identities and conditional error theorem without
promoting either into a population or unconditional convergence theorem.
These changes resolve the two qualifications raised in section 5 for the
earlier frozen version. Graph-family restriction and renormalization remain
possible directions, not declared successful repairs.

The root synthesis's starting aggregate list is correctly typed and counted.
In particular, A_ell belongs to layer ell while B_ell belongs to layer
ell-1, and the backward-field-augmented list is larger than the primitive
list in the counterexample above. The synthesis expressly preserves that
scope distinction.

Its reconstructed operator velocity follows from the source defect identity:
expand the dense velocity plus
(r Delta-rho Abar) tensor (H-Bbar), cancel the r Delta tensor H terms,
and obtain

    W_ell' = -(2/M) sum_a [
        r_a Delta_(ell,a) tensor Bbar_(ell,a)
        + rho Abar_(ell,a) tensor (H_(ell-1,a)-Bbar_(ell,a)) ].

Pairing each link velocity with the query backward and preceding forward
fields produces its stated output-velocity formula. The outer readout term
is -(2/M) sum_a r_a C3(q,a); the first-weight term is
-(2/M) sum_a r_a G_qa R1(q,a). This verifies every contribution, including
normalization and the passive-query interpretation. Differentiating the
mixed B2/H1 contraction gives the fourth-moment term stated in section 4.
These checks establish the first aggregate identities; they do not close
the entire retained list.

The synthesis correctly distinguishes projectability on an admissible restart
family, sufficient invariant-algebra structure, exact countable identities,
finite zero-tail closure, and its conditional defect-propagation estimate.
The diagram-size parameter, Legendre order, neuron width and angular grid
remain separate approximation axes. The query-grid bound is the direct
triangle inequality between a grid prediction and the target value, using
the assumed target angular Lipschitz bound. Its endpoint triangle inequality
does not identify stopping times or turn compact-time control into an
all-time conclusion, and the synthesis explicitly says so.

The synthesis also records the concrete parallel-edge divergence and limits
its established claims to finite-width identities and a reference scalar
construction. No remaining mathematical correction was identified within
this scoped check. The reported 198 numerical comparisons, checker code,
result files, archived-experiment status and other historical statements
were not independently verified by this audit: their underlying artifacts
were outside my assigned scope. This verdict is a collaborative mathematical
check, not a promotion review or verification of those numerical records.

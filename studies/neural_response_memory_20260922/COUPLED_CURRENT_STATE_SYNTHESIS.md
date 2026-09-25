# Coupled current-state compression with the initialized mixing operator retained

2026-09-22. This note follows the user's correction: the hypothetical states
are collectively sufficient. Individual neuron trajectories are not assumed
autonomous. The actual initialized middle matrix W0 and its transpose remain
present, and all omitted history must be represented by the current collective
state. No external research or computation is used.

## 1. Canonical one-sample identities

Equal hidden widths n; one fixed sample (x,y), x in R^d; phi has as many
continuous derivatives as a displayed finite-width formula requires.
Use normalized inner products <u,v>=u^T v/n, and the unhalved squared loss
with physical block mobilities (W1,W2,c)=(n,1,n). Define

    z1=W1 x/sqrt(d),              h1=phi(z1),
    z2=W2 h1,                    h2=phi(z2),
    f=<c,h2>,                    r=f-y,
    delta2=c .* phi'(z2),         b1=W2^T delta2,
    delta1=phi'(z1) .* b1.

The symbol .* means componentwise multiplication. Let chi=||x||^2/d.
The exact gradient flow is

    W1'=-2r delta1 x^T/sqrt(d),
    c'=-2r h2,
    W2'=-2r delta2 h1^T/n.                                  (1)

Write W2=W0+DeltaW, with DeltaW(0)=0. The following arguments hold at finite
width on regular time intervals. Replacing empirical averages by limiting
population laws requires appropriate limits and joint distributions; no new
such limit theorem is claimed.

## 2. Three kinds of current interaction quantities

For a current first-layer vector q and second-layer vector p, define

    G2[q]=W0 q,           G1[p]=W0^T p,                      (2)
    A[q]=DeltaW q,        B[p]=DeltaW^T p.                   (3)

G2 and G1 are initialized-matrix fields. They are receiver-indexed vectors,
not shared scalar averages. A and B are the learned-action fields. Equation
(3) defines the target quantities; a compressed realization must compute
them from its current retained states, not multiply by an unavailable DeltaW.

Ordinary collective moments have forms such as

    <h1,q>, <delta2,p>, <q1,q2>, <p1,p2>,

and expectations of other specified functions of current local states and
fields. Their values are common population quantities; they differ in type
from receiver-dependent G and learned-action fields.

The basic forward/reverse signals are exactly

    z2=G2[h1]+A[h1],
    b1=G1[delta2]+B[delta2].                                (4)

No particle independence is used. Every field is computed from the same
jointly evolving indexed populations and the same retained W0.

## 3. Exact evolution of the learned-action fields

For arbitrary differentiable current vector paths q(t),p(t), the product
rule and (1) give

    d/dt A[q(t)] = -2r delta2 <h1,q> + A[q'(t)],
    d/dt B[p(t)] = -2r h1 <delta2,p> + B[p'(t)].              (5)

For example, d(DeltaW q)/dt=DeltaW' q+DeltaW q', and
DeltaW' q=-2r delta2(h1^T q/n). This proves the first identity;
transposition proves the second. For the fixed initialized operator,

    d/dt G2[q(t)]=G2[q'(t)],
    d/dt G1[p(t)]=G1[p'(t)].                                (6)

These statements do not require q_j to be a function of a_j alone. Its
total derivative must include dependencies on all shared moments, initialized
fields, learned fields, and any explicit time variables. If q_j=q(a_j,Q),
then q_j'=partial_a q dot a_j'+partial_Q q dot Q'. If local fields enter
separately, their derivative contributions also belong here.

Equations (5)–(6) are an exact, collectively coupled observable/action
hierarchy. Successive differentiation generates new source vectors and their
actions. A proposed finite compression closes the needed actions through
current states and aggregate quantities. It does not need to restrict the
rank of DeltaW. Closure of only the actions relevant to the specified
dynamics can also be weaker than reconstructing every matrix entry.

## 4. The first explicit motion equations

The physical sample-dependent coordinates obey

    z1'=-2r chi delta1,
    h1'=phi'(z1) .* z1',
    c'=-2r h2,                                              (7)

    z2'=G2[h1']+A[h1']-2r delta2 <h1,h1>,                   (8)

    delta2'=c' .* phi'(z2)+c .* phi''(z2) .* z2',            (9)

    b1'=G1[delta2']+B[delta2']-2r h1 <delta2,delta2>.         (10)

For (8), differentiate z2=(W0+DeltaW)h1 and insert (1). For
(10), differentiate b1=(W0+DeltaW)^T delta2. The order of evaluation is
z1',h1', then z2',c', then delta2', then b1', provided the indicated
learned-action readouts are available from the retained state.

The equations visibly include all three types of interaction: actual W0
and transpose mixing, learned actions on current velocity channels, and
ordinary population moments. They also generate interactions within a layer:
substituting (8) into (9) and then (10) produces, among other terms,

    W0^T diag(c .* phi''(z2)) W0 h1'.

No claim that neurons evolve independently is compatible with these terms.

As an exact macroscopic consequence,

    r'=-2r [ <h2,h2>
              +<h1,h1><delta2,delta2>
              +chi <delta1,delta1> ].                       (11)

Proof: f'=<c',h2>+<delta2,z2'>. The c term gives the first
summand. The W2' h1 term gives the product of the middle two moments. The
W2 h1' term is <W2^T delta2,h1'>=<b1,h1'>, which by (7) is
-2r chi<delta1,delta1>. Equation (11) controls the scalar residual but
does not close the evolution of the moments appearing in it.

## 5. Correct form of a finite coupled particle law

Let m1_j,m2_i contain the specified local coordinates and auxiliary action,
derivative and history variables. Let Q be a specified collection of current
population statistics. A closure's local components have the schematic form

    m1_j'=F1(m1_j, {G1[p_beta]_j}, {B[p_beta]_j}, Q),
    m2_i'=F2(m2_i, {G2[q_alpha]_i}, {A[q_alpha]_i}, Q).        (12)

Here the source vectors q_alpha,p_beta are readouts of the current collective
state. Receiver fields may instead already be coordinates of m; either
convention is legitimate if all dependencies are included exactly once.
The initial matrix is implicit only through the explicitly displayed G
operations, never through a fresh independent copy.

For a simple aggregate Q_gamma=n^{-1}sum_j q_gamma(m1_j),

    Q_gamma'=n^{-1}sum_j grad(q_gamma)(m1_j) dot m1_j'.        (13)

Mixed-population and operator-weighted aggregates have analogous product
rules. These identities prescribe how aggregates evolve; they do not imply
that a chosen finite list closes. For an autonomous restartable model, Q and
all fields must be available from the retained current state and the fixed
operator. They cannot be functions read from a dense trajectory afterward.

When its flow is invertible, the full retained configuration, not one particle
in isolation, is the state that reconstructs the joint past. A global reversible
flow generally does not induce a reversible map a_j(0)->a_j(t) independent
of the other particles and their environments.

## 6. Correction to a universal pair readout and its generator

Suppose an admissible reconstruction can be written as

    DeltaW_ij = K(t,m2_i,m1_j,Q)/n,                          (14)

where any necessary local initialized fields are included in the states or
listed as further arguments. This is an additional reconstruction property,
not a consequence of collective Markovianity alone. Q can be finite-dimensional
for a candidate finite closure; a measure- or field-valued Q must be counted
as such and differentiated functionally.

Along the actual coupled flow, the required consistency equation is

    partial_t K + partial_b K dot m2_i'
                + partial_a K dot m1_j'
                + D_Q K[Q']
       = -2r delta2_i h1_j.                                (15)

For finite-dimensional Q, the last term is a sum of ordinary partial
derivatives times Q_alpha'. If additional local fields are explicit arguments,
their chain-rule terms must also appear. Treating them as constants discards
the very population mixing the user wants to retain.

There are two representations that must not be mixed:

* A universal K(t,b,a,Q) evaluated on the current environment has (15).
* A path-conditioned field k_t(b,a)=K(t,b,a,Q_t) has
  partial_t k=partial_t K+D_Q K[Q_t']; its transport PDE already
  contains this contribution inside its time derivative.

The earlier pair-transport identity is valid conditionally on a specified
common environment path when the assumed single-state characteristic fields
exist. It did not establish that autonomous fields F_l(t,a) or two marginal
laws alone encode the actual collectively coupled initialized dynamics.
Adding D_Q K a second time to a path-conditioned k_t equation would also
be incorrect. The current note makes the dependency explicit instead.

## 7. Population description and Gaussian mixing

Normalized empirical contractions in (5), (11), and (13) have ordinary
population-expectation counterparts. W0 has Gaussian entries with variance
of order 1/n and acts by a sum, giving receiver-dependent random fields.
For independent queries with bounded normalized second moment these fields
have bounded second moment. Adaptive queries need additional control; row
alignment can amplify a selected receiver field. This mixing is not an
ordinary average that can be replaced by its zero mean.

For q,v jointly independent of W0, the covariance of two initialized
fields is the input overlap: E[(W0q)_i(W0v)_i |q,v]=<q,v> for
unit initialization variance. This illustrative calculation does not assert
independence for trained queries. Repeated W0/transpose uses must retain
their joint coupling; Gaussian source-response calculus or explicit retained
operator actions can accomplish this. The present construction chooses the
latter, as authorized.

An unmarked one-neuron marginal may lose the relation between its local state
and incoming initialized fields. A legitimate macroscopic state therefore
retains the necessary joint marked distributions or equivalent coupled
operator-state realization. Receiver-dependent fields, ordinary scalar
moments, and learned actions should not be conflated under one unspecified
average. No new propagation-of-chaos or Gaussian-independence claim is made.

## Status and provenance

Exact finite-width identities: (1)–(11), (13) for specified differentiable
observables, and the chain rule (15) conditional on reconstruction (14).
These derive the canonical mixing operations and the action hierarchy.

Assumed/open: an efficient finite selection of states and source channels
closing (12), sufficient finite macro statistics, a reconstructing K if
full weight readout is desired, and population/approximation error limits.
No time Taylor series, finite-rank hypothesis, or replacement of the original
gradient law is used. No experiment, GPU work, web research, or Git write.

Root used this study's canonical identities and current user constraints,
plus required skills. Established notation files were hash-checked unchanged.
Fresh prompt-scoped routes own COUPLED_STATE_GENERATOR_ROUTE.md and
ONE_SAMPLE_ACTION_HIERARCHY.md; they used only their neutral assignments and
required skills, with no other scientific source retrieval.

Root read both complete frozen route reports. The action route checked
sections 1–4; the generator route checked sections 5–7. Both confirmed the
equations within these scopes. Their precision corrections concerning block
ordering, regularity, conditional invertibility and adaptive Gaussian fields
are incorporated. These are internal algebraic checks, not promotion reviews
or a proof of finite closure.

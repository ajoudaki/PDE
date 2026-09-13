# Coordinator numerical route, frozen before comparison

2026-09-13. Candidate design, not yet a theorem or implementation. Inputs:
complete maintained H1/H2 and seven matching frozen dependency excerpts;
maintained prototype/tests/guide; required H3 assessments and their short-time
stability source. No other fresh route candidate has been read. The scope
agent has disclosed its proposed direct all-law short-time extension, still
under construction; no assumption of its validity is made here.

## Finite Gaussian integration without tensor growth

Use deterministic Halton points (distinct prime bases) followed by pairwise
Box–Muller, retaining the entire same-population source tuple on each point.
For every new oriented source, recompute the **full** uncentered Gram of that
orientation's operands on the other current population rule. Add a positive
numerical covariance regularizer tau I and factor by Cholesky. Reevaluate
earlier source expressions using this enlarged covariance; retain their
previously computed deterministic response coefficients. Every named source
and its formal derivative remains present. This avoids discontinuous numerical
rank decisions or pseudoinverses. At finite resolution it is an approximation
to the initialization program, not an exact canonical action.

With exact Gaussian integration, finite causal induction and continuity of
Gaussian laws in their covariance show convergence to H6 as tau decreases to
zero. For fixed positive tau, full-Gram assembly and Cholesky are continuous;
increasing the integration point count gives that exact regularized program.
The change in an earlier marginal after a finite-rule Gram refresh vanishes
in this limit. Frozen expected named derivatives are evaluated on the same
joint tuple; independent substitution for coordinates is prohibited.

A contained Halton consistency proof is available. A base-b digit cylinder
corresponds to one residue class modulo b^k. Chinese remaindering combines
distinct primes, so joint cylinder frequencies converge to their volumes.
Finite box partitions then prove equidistribution. For one coordinate, each
block of b^k radical inverses contains one point in every length-b^-k cell;
digit decomposition gives discrepancy O_b(log M/M), and the smallest of the
first M positive points is at least 1/(bM). Layer-cake integration therefore
controls the tail of -log(u) by its uniform-integral tail plus
O_b((log M)^2/M). Box–Muller has squared pair norm -2log(u), so empirical
second moments are uniformly integrable. Weak convergence and second moments
give W2 convergence of the joint Gaussian rule, also for singular linear
images. These details still require a full persisted proof.

## Coordinates and arithmetic

For raw dictionary Gram G and eta>0, factor G+eta I=L L^T and use
b=L^-1 psi. This gives exactly Q=S(G+eta I)^-1 S* from H2. Symmetric and
Cholesky-normalized features differ by an orthogonal coefficient change;
Euclidean coefficient GF is invariant under it. Replace eta=2^-N by
eta=(N+1)^-2. H2's density proof uses only eta>0 and eta tending to zero.

Add a practical nested trigonometric pilot to an exhaustive H2 code prefix.
One choice starts from h_i=tanh(g_i), z_i=A0 h_i, H_i=tanh(z_i),
p_i=A0*H_i and t_i=tanh(p_i), with both constants. Add sin(k g_i),
cos(k g_i), sin(k z_i), cos(k z_i), 1<=k<=N. Retain every distinct syntactic
bounded output and the code prefix through N, without empirical rank deletion.
N=1,2,3 enrich both feature spans; density comes from the exhaustive prefix,
not from a claim that the pilot alone is dense.

Implement the same contractions and characteristic evolution in float64 and
arbitrary decimal precision. Python Decimal supplies correctly rounded exp,
ln and sqrt (verified from the installed primitive docstrings); sin/cos can
use Machin pi, range reduction and Taylor summation with precision refinement.
Cholesky and triangular solves require only these primitives and ordinary
arithmetic. No permanently fixed float64 ceiling enters the convergence
statement. Unresolved positive pivots raise a numerical failure at a finite
precision instead of removing coordinates.

## Numerical limit and state

One valid fixed-N iterated refinement, read from innermost to outermost, is:
arithmetic precision to infinity; time step to zero; input midpoint count to
infinity; population Halton count to infinity; initialization Halton count to
infinity; covariance regularizer tau to zero. Then N tends to infinity.
This is an iterated multi-index J, not an arbitrary diagonal schedule.

At fixed N, bounded feature marks and bounded readout give locally Lipschitz
characteristics and uniform finite-horizon bounds under nearby mark laws.
Couple the joint marks in W2 and subtract all contractions to obtain solution
continuity. This supplies population/input integration consistency and
convergence of the frozen/current activation pairs. Root g is unbounded but
enters only Lipschitz gates and its L2 initial coordinate, whereas w-g has a
bounded drift at fixed N. These claims require full proofs in the candidate.

Working state: b1,g,w,p1,b2,c,p2,M,D, numerical metadata and represented input
law. The initializer's source tape is discarded after marks and D are built.
Time evolution uses a fixed-stage explicit integrator and fixed input blocks;
observations recompute paired frozen/current values using D and M. No history
or target trajectory is saved. Runtime scales with point counts and feature
counts, rather than a tensor node count. Full timing and storage evidence
remain to be produced under the separate preregistration.

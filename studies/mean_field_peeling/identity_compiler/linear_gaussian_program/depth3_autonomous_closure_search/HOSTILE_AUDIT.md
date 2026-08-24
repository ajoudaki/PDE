# Hostile audit: depth-three autonomous closure search

## 1. Central claim under attack

The target is H1 in PROTOCOL.md: existence of a fixed finite collection of
scalar current-time fields on one explicit finite-dimensional classical
initialization source, with direct prediction/loss readouts and compact-time
width-limit identification.

The present search has not proved H1 and has not disproved it.

## 2. Hidden-operator loophole

One can make (4.1) look continuum-sized by writing a kernel
\(Q(\lambda,\mu,s)\).  This is not sufficient.  Its initial condition must
represent the Haar bridge \(H_n\) in (4.4).  The following substitutions are
contract violations:

- retain \(H_n\) as an \(n\)-dependent kernel;
- call its limiting noncommutative operator one field value;
- encode an infinite orthogonal matrix in a real number or path;
- use a field indexed by all alternating words;
- integrate out the bridge into a two-time covariance/response kernel.

An ordinary deterministic pointwise kernel is not a repair: the bridge
entries tend to zero while the operator remains an isometry.

Severity: fatal to R2 as currently formulated; not fatal to H1.

## 3. Marginal spectra do not encode noncommutative order

The insufficiency is visible without asymptotics.  Let

\[
A=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
B_\theta=R_\theta A R_\theta^T.
\]

Every \(B_\theta\) has the same spectrum as \(A\), but

\[
\frac12\operatorname{Tr}(AB_\theta)=\cos(2\theta),\qquad
\frac12\operatorname{Tr}(AB_\theta AB_\theta)=\cos(4\theta).
\]

At \(\theta=\pi/4\), the second ordered moment is \(-1\).  A classical joint
eigenvalue measure for commuting variables with eigenvalues \(\pm1\) would
instead give \(\int\lambda^2\mu^2\,d\chi=1\).  Thus marginal measures, or a
commuting joint spectral measure, cannot reproduce the ordered bridge
contractions.

This example does not rule out a richer finite-dimensional source carrying
genuine orientation data.

## 4. Gauge-degree warning

The finite-width variables \((x,D,B,y)\) have dimension
\(2n^2+2n\).  Hidden-layer basis changes form \(O(n)^3\), of dimension
\(3n(n-1)/2\).  A generic orbit quotient therefore still has

\[
\frac12n^2+\frac72n
\]

degrees of freedom.  The \(O(n^2)\) remainder is represented concretely by
the relative Haar bridge.  By contrast, the depth-two quotient is only
\(O(n)\), consistent with a one-dimensional spectral source.

This is a structural warning, not a nonexistence proof: a typical Gaussian
width limit can self-average many finite-width degrees of freedom.

## 5. Strongest surviving affirmative alternative

The strongest surviving alternative is that the asymptotic Haar bridge
admits a previously unidentified finite collection of classical
analytic transforms whose current-time PDE closes and is restartable.  Such
a transform would have to:

1. distinguish arbitrary ordered alternating contractions;
2. evolve under the nonlinear rank-one update in (3.2);
3. use no matrix-size parameter or word index;
4. give direct vector-state readouts, not merely normalized traces;
5. admit a source-convergence and compact-time stability proof.

No contradiction to such a construction has been derived.

## 6. Claim-level audit

- Exact invariants do not imply a continuum closure.
- A formal noncommutative operator ODE is not admissible.
- Agreement with finitely many Taylor coefficients, had it been tested,
  would not imply positive-time identification.
- Failure of R1--R4 is witness-level evidence only.
- No derivative artifact was opened and no coefficient comparison was run
  because no candidate was frozen; hence there is no new coefficient-selection
  or post-fit issue.
- Well-posedness of a hypothetical IDE and its compact-time width-limit
  identification remain separate open rungs.

## 7. Final decision

No admissible closure has survived construction, so the correct status is
**open**.  The exact identities and Haar-bridge reduction are retained as
proved progress.  Reporting the cyclic operator ODE, a DMFT system, or the
finite-width kernel (4.1) as the requested answer would violate the frozen
contract.

# Independent source and temporal-approximation check

Verdict: **PASS within the assigned scope.** No mathematical correction is
required for the analytic approximation, initialization provenance, order
selection, or retained-coordinate accounting in the frozen candidate. This
is a check of the new construction against the paper's stated interfaces,
not an independent reproof of the probabilistic cavity argument establishing
the imported analytic-source proposition. It is not a promotion review.

## Frozen inputs and scope

The candidate was read completely. Scientific inputs were limited to that
candidate and the five paper files below. The setup and fitting file were
read completely; the source proposition's full statement and the passages
establishing its public domain and norm bounds were checked; the complete
initialization-jet compiler statement and proof and the complete Legendre
file were checked. No other study artifacts, prior reviews, or research
history were consulted. The required rigorous-mathematics and canonical
notation instructions, including the neural-response reference, were read.

SHA-256 hashes of the input versions checked:

| Input | SHA-256 |
| --- | --- |
| `RESULT.md` | `f1788c78eb27d271d9cb3b5023696578923028144912a3dc1daeb185963e7e27` |
| `paper/compact.tex` | `47199d5c9e374b80b9eafefd60699c2f4bfe06dde00ebd0a1c53e2805598a0c4` |
| `paper/compact_foundations.tex` | `6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0` |
| `paper/compact_selected.tex` | `3add2b694f38a4d7dbce90e51dafd375a7e8dee2e06d26b2d5af451bddb44885` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `paper/compact_legendre.tex` | `862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9` |

## Source theorem and polynomial approximation

Proposition `cp:source(i)` explicitly includes the vector fields
\(h^{(j)}\), with their complex Euclidean norms divided by \(\sqrt n\)
bounded by \(\beta^{3L}\). It is not only a scalar prediction theorem.
Fixing a real training input in its whole-sphere domain gives exactly the
physical-time rectangle and vector bound used in candidate (6). Every
source needed for hidden layer \(\ell\) is
\(h_D^{(\ell-1)}(t,x_a)\), so the claimed interface covers all required
histories without passive-query coefficients or backward-history
approximation. The candidate correctly uses `cp:source(ii)` separately for
the dense pre-gated backward carrier bound.

For \(A=\max(1,T/r_t)\), the Bernstein ellipse with parameter
\(\exp(1/A)\) has physical imaginary half-height
\(T\sinh(1/A)/2<r_t\) and real excess
\(T[\cosh(1/A)-1]/2<r_t\). Indeed, for \(0<u\le1\),
\(\sinh u\le u\sinh1<2u\) and
\(\cosh u-1\le u(\cosh1-1)<2u\), while
\(T/A\le r_t\). Thus Cauchy's integral applies with the paper's
vector norm bound. Pairing the Laurent coefficients gives the Chebyshev
tail in (10); the estimate
\(1-e^{-1/A}\ge1/(2A)\) justifies its stated constant.

The vector supremum norm of the Legendre projector is at most
\(\sum_{j<q}(2j+1)=q^2\), by \(|P_j|\le1\) and the triangle
inequality for the coefficient integrals. Applying it to the Chebyshev
approximation error proves (11) with the factor \(1+q^2\).
Approximating each of the \(q\) coefficient vectors to the right side
of (11) divided by \(q\), in normalized Euclidean norm, adds at most
one further copy of that error. This proves (12), including its factor
eight. Orthogonal projection onto the span of the approximate coefficients
then proves (13), regardless of rank or conditioning. Empty and
rank-deficient spans cause no exception in this exact-real-coordinate
argument.

## Initial jets and autonomy

Proposition `cp:jets` covers a finite list of source integrals against
polynomial time bases, with arbitrarily small positive accuracy. Here
the number of coordinates and coefficients is finite at every individual
width, and the Legendre coefficient integral is such an integral after
the affine time change. The proposition's required analytic rectangle and
coordinate bound follow from `cp:source(i)`; for these forward sources one
may take coordinate bound \(\sqrt n\,\beta^{3L}\).

The compiler proof constructs the continued source approximations from
the dense ODE's derivatives at time zero, then uses finite quadrature of
those approximations. Its conformal time map sends zero to zero and a
strictly interior real disk point to \(T\), so it does not assume that
an ordinary Taylor disk at zero already reaches the full interval. No
later dense state or trajectory samples are required. Approximate
coefficients may be chosen real because the real sources, origin jets,
time maps, and real-interval quadrature are real. Exact rank selection and
orthonormalization are consistent with the candidate's explicit exclusion
of finite-precision guarantees.

After construction, only the bases survive. The restricted flow evaluates
the original forward and backward recursions at its own current weights.
For example, the hidden forward multiplication is
\[
W^{(\ell)}h
=W_0^{(\ell)}h+C^{(\ell)}(U_{\ell-1}^{\top}h),
\]
and the backward multiplication is its transpose. Neither uses a stored
future source function or time-dependent forcing. The bases encode
information obtained from the initial derivatives, but the output itself
is produced by an autonomous nonlinear gradient flow. This is consistent
with the candidate's stated initialization-only model.

The compiler and activation derivative evaluator have no controlled time,
scratch, precision, or jet-order complexity here. The candidate discloses
this both before the headline and in its final limitations. The retained
state estimate must not be interpreted as an initialization-space bound.

## Order, counts, and statement qualifications

Writing \(u=\log(en)\) only in this paragraph, the explicit choice gives
\[
q\le1+16u+
512\beta^{30L}Y^2\lambda^{-2}\sqrt{d+3}\,u^{5/2}.
\]
Since \(u\ge1\), candidate (1) holds, for example, with the absolute
constant \(C=512\). For every fixed admissible problem,
\(A=O(u^{3/2})\), so the prefactor in (12) grows only as a fixed
power of \(u\). The eventual bound \(\eta_q\le(en)^{-8}\)
therefore follows from \(q\ge16Au\). Its width threshold can depend
on all fixed problem parameters. The candidate correctly limits its
subsequent comparison with \(Y/n\) to fixed \(Y>0\); it does not
claim uniformity as labels vanish or data grow with width.

There are \(n(d+1)+n\sum_{\ell=2}^L r_{\ell-1}\) retained moving
coordinates and \(n\sum_{\ell=2}^L r_{\ell-1}\) retained fixed basis
coordinates, with \(r_{\ell-1}\le\min(n,mq)\). Together with the
\((L-1)n^2\) fixed dense mixers, these reproduce (3)--(4). Updated
full hidden matrices need not be stored. As in the inherited paper setup,
training-data storage and a nonprimitive activation evaluator's description
and scratch are additional. The candidate's count concerns evolving state,
not all working arrays or total storage.

The imported signed-Jacobian comparison in the Legendre file is algebraic
at a pair of parameter states. Its proof uses the operator/readout bounds
on their segment and the carrier bound only at the dense endpoint. It
does not depend on the second state satisfying the old moment equations.
Consequently importing that interface for the restricted flow does not
silently reuse an order condition from the original Legendre method.

The candidate expressly changes the construction: Legendre polynomials
are used during initialization to choose fixed right subspaces, and
hidden increments then evolve by restricted exact gradient flow. The
stated result is therefore an improved moving-coordinate bound for this
modified model, with no sharper-order claim for the unchanged online
residual-clock equations. Its all-time and unseen-query claims use the
separate parameter comparison and sphere output-gradient bound, rather
than incorrectly extending a training-history approximation directly to
unseen inputs. The dense-run lower bound cited in the final ratio has
the correct \(Y\sqrt\gamma/(\sqrt n\log(en)^{5/2})\) scale.

No corrective edits are requested within this review's scope. Retain the
existing exclusions of efficient preprocessing, finite precision,
subquadratic total storage, and an improved order for the original online
Legendre ODE when communicating the result.

# Tensor Program fixed-mesh interface audit

**Audit date:** 2026-08-24  
**Claim level:** theorem invocation checked against the full authoritative text  
**Scope:** a fixed finite Euler mesh only

## 1. Result that is actually available

The relevant source is Greg Yang, *Tensor Programs III: Neural Matrix
Laws*, arXiv:2009.10685v3. The older transpose theorem is not the right
interface: the paper itself explains that the earlier master theorems either
forbid simultaneous use of a matrix and its transpose or allow it only under
restrictions that exclude even \(A^{\mathsf T}Av\). TP III states that its
Master Theorem is unrestricted over Tensor Programs.

For the present calculus the precise convenient statement is Appendix E,
Theorem E.15:

- fix one finite NETSOR\({}^{\mathsf T+}\) program;
- initialize its matrices, vectors, and scalar parameters according to
  Setup E.2;
- require every coordinate nonlinearity (and every nontrivial
  scalar-parameter use) to satisfy the pseudo-Lipschitz hypotheses of
  Assumption E.6;
- then empirical averages of every pseudo-Lipschitz test of finitely many
  program vectors converge almost surely to the recursively defined
  population expectation, and every program scalar converges almost surely.

Unlike Theorem E.5, Theorem E.15 does **not** assume rank stability. The
price is that the test function is pseudo-Lipschitz rather than merely
polynomially bounded. Definition E.4 also records that pseudo-Lipschitz
maps are polynomially bounded and are closed under finite composition
(with increasing degree).

Setup E.2 requires:

1. every initial program scalar to have a deterministic limit;
2. every initial matrix entry to be independent Gaussian with variance
   \(\sigma_W^2/n\); and
3. the coordinates of the finite family of initial vectors to be iid copies
   of a joint Gaussian vector.

The language itself contains coordinatewise nonlinearities depending on
previous scalar parameters, normalized empirical moments, and both
\(Wx\) and \(W^{\mathsf T}x\).

Authoritative full text:
[Tensor Programs III](https://arxiv.org/pdf/2009.10685).

## 2. Exact compilation of a fixed Euler mesh

Freeze a mesh \(\Pi=\{0=s_0<\cdots<s_m=S\}\), all source/readout cutoffs
used by the proof, and the hidden depth. At step \(k\), eliminate every
trained effective matrix by the exact identity

\[
 G_\ell^k
 =G_\ell^0+\sum_{r<k}(s_{r+1}-s_r)
   B_\ell^r\otimes_n X_{\ell-1}^r .
\]

Thus a query to the trained matrix is compiled as

\[
 G_\ell^k V
 =G_\ell^0V+
 \sum_{r<k}(s_{r+1}-s_r)B_\ell^r
       \langle X_{\ell-1}^r,V\rangle_n ,
\]

and similarly for the genuine transpose. Every mesh line is therefore a
finite composition of:

- a forward or transpose query to the immutable \(G_\ell^0\);
- a coordinate map;
- a normalized empirical moment; and
- a scalar-linear combination of already generated vectors.

These are NETSOR\({}^{\mathsf T+}\) operations. The trained matrix is
**not** supplied as a random initial matrix, so the source paper's warning
that it makes no general claim about trained weights is not violated.
Training has been algebraically compiled into a finite program over the
initial Gaussian source.

For arctangent and its derivative, products, polynomial natural
coordinates, fixed Lipschitz cutoffs, and the polynomial tests needed for
the named first and second empirical moments, the resulting finite
coordinate maps/tests are pseudo-Lipschitz of some finite degree.
Theorem E.15 therefore proves the joint full-sequence, almost-sure
population semantics of every *fixed* compiled program. In particular it
retains the nonzero forward/transpose regression correction; treating the
transpose as an independent matrix would give the wrong law.

## 3. What this invocation does not prove

The theorem fixes the entire finite program before width tends to infinity.
It provides no constants uniform in:

- the number \(m\) of Euler lines;
- the mesh size \(|\Pi|\);
- a source or coordinate cutoff sent to infinity;
- a growing family of time-labelled tests; or
- the response/sensitivity order.

It therefore proves only gate G3 (fixed-mesh identification). It does not
prove:

1. that exact finite-width flow is uniformly close to its Euler program;
2. that the limiting Euler programs converge as \(|\Pi|\downarrow0\);
3. uniform integrability for an unbounded raw tangent-kernel square after
   cutoff removal;
4. compact-time well-posedness or uniqueness of the limiting IDE; or
5. the depth-three two-channel susceptibility/traffic estimates.

Changing “fix a program” into a triangular sequence of programs whose
length tends to infinity is not an invocation of Theorem E.15.

## 4. Audit verdict

The unrestricted TP III theorem is a rigorous and correctly matched
backend for the calculus's NonlinearFiniteProgramSource rule at every fixed
finite mesh. It is stronger and safer here than the older BP-like transpose
theorem because no rank-stability or gradient-independence shortcut is
needed.

Promotion is strictly limited to G3. Any G4/G5 claim must be supplied by a
separate mesh-uniform stability, envelope, and raw-moment argument.


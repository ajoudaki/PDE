# Isolated review of the projected-Gaussian scalar and innovation lemmas

2026-10-11. Internal mathematical review; not a promotion review.

## Frozen inputs and scope

I read both assigned inputs completely and reconstructed their arguments.
The source hashes at the beginning and end of the initial audit phase
were identical:

- `GELU_SILU_PROJECTED_SCALAR.md`, 456 lines:
  `1b13eca163923713ab2bab3c60c018726f32597684dd285f9eeaf34c65e79721`.
- `GELU_SILU_PROJECTED_INNOVATION.md`, 400 lines:
  `59a507395b324f44a26692b99fec163d34c5637b48a2db59ed8627014f5476b6`.

The only other inputs were the assignment and required rigorous-math and
canonical-notation skills, including the neural-network reference. I did
not read the study README, manuscript, earlier routes, other reviews, or
other agents' findings. No numerical experiments or external scientific
sources were needed. All line references below refer to these frozen inputs.

**Verdict:** the central covariance lower bound, Gaussian approximation,
and fixed-depth innovation arguments pass mathematical reconstruction with
their intended hypotheses. The scalar theorem as literally stated needs
the sign correction in Finding 1 before an unconditional PASS. Finding 2
should be made explicit before using the final fourth-moment corollary as
a uniform result. Neither finding requires changing the proof mechanism.
This verdict does not establish the oracle representation, an endpoint
approximation, or an endpoint theorem.
The final correction recheck and superseding verdict appear at the end.

## Findings requiring a statement correction or clarification

### 1. Require a nonnegative bias bound in the scalar theorem

Location: scalar lines 42–55, 67–75, and 202–205.

The assumptions state only \(B<\infty\) and
\(\|b\|^2/n\le B^2\), but the truncation radius is
\(R=\max\{1,4B\sqrt{M_4}/E^2\}\). The proof needs \(B\ge0\).
For negative \(B\), the stated result is false, not merely unproved.

To see this, take \(E=1\), \(M_4=1\), \(\sigma_-=
\sigma_+=1\), \(P=I_n\), \(w_i=1\), and \(b_i=-T\),
with \(B=-T\) for a fixed positive \(T\). All displayed assumptions
hold. The rank defect is zero, so condition (5) holds at every width for
every allowed \(\tau\). Nevertheless \(R=1\), so the claimed lower
bound is the positive constant \(d_1/16\), independent of \(T\),
whereas independence gives

\[
\operatorname{Var}F=\operatorname{Var}\phi(-T+G)
\longrightarrow0\qquad(T\longrightarrow\infty).
\]

For either named activation, this convergence follows by dominated
convergence: \(\phi(-T+x)\to0\), and for \(T\ge0\) its absolute
value is bounded by \(1+x_+\). Choose a sufficiently large fixed
\(T\) to contradict (6).

Repair: state \(0\le B<\infty\), or use \(|B|\) in the definition
of \(R\). The first option matches the usual convention for a norm
bound. With this repair, the large-bias readout energy estimate is exactly
\(\sqrt{M_4}B/R\le E^2/4\), as required.

### 2. State uniform constants in the fourth-moment corollary

Location: innovation lines 346–392, especially (20) and the
width-independent conclusion following (22).

The calculation in (20)–(22) is correct provided \(c>0\) and
\(K_*<\infty\) are fixed uniformly in width and in the conditioning
under consideration. These quantifiers are not expressly stated when
the constants first appear. If \(c=c_n\to0\) is allowed, the
displayed lower probability bound can tend to zero; (20) alone then
does not yield the stated width-independent conclusion.

Repair: introduce (20) with “for fixed constants \(c>0\) and
\(K_*<\infty\), independent of width and of the admissible
conditioning.” If different conditioning events are intended, specify
the event on which the same constants apply. No algebraic repair is
needed.

### 3. Specify a rank envelope when asserting asymptotic uniformity

Location: scalar lines 94–96 and 380–389; innovation lines 139–150
and 204–221.

The finite-width estimates are uniform as written. Their asymptotic
use is uniform over objects obeying a common deterministic rank envelope
\(r_n=o(n)\), and similarly for the second projection where present.
There is no uniform onset width over the class of all sequences that
individually satisfy \(r_n=o(n)\): any one sequence may have an
arbitrarily late exceptional width. This is a quantifier clarification,
not an obstruction to the stated finite-width estimates or an ordinary
fixed-sequence application. In an assembled theorem, fix the envelope
before taking the uniform limit.

## Independent reconstruction of the scalar argument

Here \(P\) denotes the high-rank projection in the scalar source;
this differs from the innovation source's notation, where \(I-P\)
is the high-rank projection. Assume the sign repair \(B\ge0\).

Write \(Q=I-P\), \(q_i=Q_{ii}\), and
\(I=\{i:q_i\le\tau\}\), \(J=I^c\). Since \(Q\) is an
orthogonal projection, \(\sum_iq_i=r\) and \(|J|\le r/\tau\).
The normalized correlation matrix of \((Pg)_I\) has entries
\(C_{ij}=P_{ij}/\sqrt{P_{ii}P_{jj}}\). For \(i\in I\),

\[
\sum_{j\in I,\ j\ne i}|C_{ij}|^2
\le \frac{q_i}{1-\tau}
\le\frac{\tau}{(1-\tau)^2}<\frac12.
\]

The source's bound is slightly weaker than the first inequality and
valid. Because \(|C_{ij}|\le1\), the same row-sum bound holds for
every entrywise power \(C^{\circ k}\), \(k\ge2\). The quadratic
form estimate using \(2|u_iu_j|\le u_i^2+u_j^2\) therefore gives
\(C^{\circ k}\succeq I/2\).

The normalized Hermite expansion has covariance
\(\sum_{k\ge1}\operatorname{diag}(a_{k,i})C^{\circ k}
\operatorname{diag}(a_{k,i})\). Each summand is positive semidefinite:
\(C\) is a Gram matrix and its entrywise powers are Gram matrices
of tensor powers. Gaussian square integrability and finiteness of the
number of coordinates justify the expansion and its quadratic forms.
For a continuous nonaffine activation, zero Hermite mass above degree
one would force the activation to be affine on the whole real line.
Continuity in Gaussian \(L^2\) makes the minimum \(d_R\) strictly
positive on its compact rectangle with positive scale.

This yields (13), including the large-bias coordinates on its left
side. Thus their potentially nontrivial correlations are not silently
discarded. Cauchy–Schwarz gives, for every coordinate set \(A\),

\[
\frac1n\sum_{i\in A}w_i^2
\le\sqrt{M_4}\sqrt{|A|/n}.
\]

The large-bias energy is at most \(E^2/4\), and the energy on
\(J\) is at most \(\alpha\le E^2/4\). Consequently the retained
bounded-bias energy is at least \(E^2/2\), yielding
\(\operatorname{Var}F_I\ge d_RE^2/4\).
Gaussian Poincare gives
\(\operatorname{Var}F_J\le s^2\sigma_+^2\alpha
\le d_RE^2/16\). The reverse triangle inequality for centered
random variables then gives exactly
\(\operatorname{Var}F\ge d_RE^2/16\). This controls all
cross-cancellation with \(J\).

The upper variance bound follows from
\(\operatorname{Lip}(F)\le s\sigma_+\|w\|/\sqrt n\) and
\(\|w\|^2/n\le\sqrt{M_4}\). For a fixed rank envelope
\(r_n=o(n)\), the proposed \(\tau_n=\sqrt{(r_n+1)/n}\)
tends to zero, and \(r_n/(n\tau_n)\to0\), including when
\(r_n=0\). Thus (5) eventually holds without any stronger rank
restriction.

## Independent reconstruction of the Gaussian approximation

For the centered smooth scalar \(f\), let \(A\) bound its gradient
norm and \(D\) its Hessian operator norm. The Ornstein–Uhlenbeck
resolvent \(Rf=\int_0^\infty P_tf\,dt\) converges by the coupling
bound given in the source. Differentiation under this integral gives
\(\|\nabla Rf\|\le A\), \(\|D^2Rf\|_{\rm op}\le D/2\),
and \(-LRf=f\). These operations are justified by the stated global
derivative bounds and Gaussian integrability.

For \(\Gamma=\nabla f^\top\nabla Rf\), integration by parts gives
\(\mathbb E[f\psi(f)]=\mathbb E[\psi'(f)\Gamma]\),
\(\mathbb E\Gamma=v\), and
\(\|\nabla\Gamma\|\le3AD/2\). Poincare therefore gives
\(\mathbb E|\Gamma-v|\le3AD/2\).

The indicator Stein solution displayed in (24) has the correct signs
and satisfies \(\|\psi_a'\|_\infty\le1\). Besides the normal
tail inequality, the branch checks use \(x\le a\Rightarrow
1-\Phi(a)\le1-\Phi(x)\) and
\(x>a\Rightarrow\Phi(a)\le\Phi(x)\). Rescaling to variance
\(v\) gives the derivative bound \(1/v\), not \(1/\sqrt v\).
It follows that the Kolmogorov error is at most \(3AD/(2v)\).

The atom caveat is handled correctly. One may choose smooth decreasing
approximations that equal one on \(( -\infty,z]\) and decrease to
zero on \([z,z+\varepsilon]\). The Stein bound holds for each
approximation by mixtures of indicator solutions, and dominated
convergence recovers the inclusive distribution function even if
\(f(g)\) has an atom at \(z\). A left limit at the lower interval
endpoint then proves the inclusive small-ball bound (8).

Finally, the exact gradient and Hessian in (25) give
\(A\le s\sigma_+M_4^{1/4}\) and
\(D\le t\sigma_+^2M_4^{1/4}n^{-1/4}\). This verifies the full
constant in (7). No independence among \(b,w,P\) is needed once
they are fixed under conditioning and the remaining Gaussian is fresh.

## Independent reconstruction of innovation and fourth moments

For the innovation source's one-layer lemma, at least \(n/2\)
coordinates have both \(|b_i|\le2B+1\) and \(P_{ii}\le1/2\)
when \(k\le n/8\). Their marginal variances are at least \(v\),
so \(\operatorname{tr}\operatorname{Cov}(h)\ge vn/2\).
Poincare gives \(\operatorname{Cov}(h)\preceq K^2I\).
Removing a rank-\(k'\) subspace therefore leaves
\(\mathbb EN^2\ge vn/2-k'K^2\ge vn/4\), including any feature
mean. Since \(N\) is \(K\)-Lipschitz,
\((\mathbb EN)^2\ge vn/8\) under (3). Chebyshev at
\(N^2<vn/32\) gives exactly \(32K^2/(vn)\). No covariance
lower bound on the entire feature space is used. The analogous scalar
source Section 4 is also valid.

Given representation (9), exposure through layer \(j-1\) fixes
\(b_j\) and \(\sigma_j\); the remaining rows of \(G_j\) give
the conditional standard Gaussian vector in (12). The induction excludes
\(\sigma_j=0\) before using its normalized representation. The
compact variance intervals are nonempty because
\(\kappa_j\le H_{j-1}^2/8<H_j^2\). For the first layer, both
activations equal \(z/2\) plus an even function, so Gaussian
orthogonality gives variance at least \(1/4\). The initial
Chebyshev constant \(256/n\), the Gaussian norm constant
\(2/(9n)\), and all subsequent constants in (14) check out.
Conditional failure probabilities can be summed without assuming
independence of the good events.

The source's use of a transcript-measurable operator bound in lines
276–305 is valid as a conditional argument: the initialized operator
event is used only to bound its probability, not as extra conditioning
on the unused Gaussian. The operator and update probability estimates
themselves are explicitly external inputs and were not audited here.

For any \(K_F\)-Lipschitz Gaussian scalar, Poincare applied to its
centered square gives
\(\mathbb E(F-\mathbb EF)^4\le5K_F^4\). Under (20), with the
uniform constants specified in Finding 2, this yields

\[
\mathbb ED^4\le
8\max\{1,5K_*^4/c^2\}(\mathbb ED^2)^2,
\qquad D=F-\widetilde F.
\]

The displayed second-moment argument then gives exactly the probability
constant in (22), for arbitrary conditional means. This establishes
positive-probability separation; that corollary alone does not establish
separation with every prescribed probability \(1-\delta\). The
scalar Gaussian approximation supplies the stronger small-ball statement
when its hypotheses hold.

## Boundaries of the verdict

The exact conditional Gaussian law is indispensable. Low rank alone
does not replace freshness: if a rank-one projection is selected after
seeing a feature vector, it can project onto that vector and erase its
innovation. Likewise, allowing the scalar high-rank projection to be
\(I-gg^\top/\|g\|^2\) after seeing \(g\) kills the Gaussian term
despite rank defect one. The sources expressly exclude these choices.

The empirical fourth-moment constant must be bounded independently of
width, as stated. For example, a readout supported on one discarded
coordinate with magnitude \(\sqrt n\) has fixed normalized energy
but empirical fourth moment \(n\); its prediction can be deterministic.
The fourth-moment hypothesis prevents precisely this concentration.

The independent-run small-ball implication in scalar Section 5 is valid
if its stated good events hold with probability tending to one, the
freshness survives the stated conditioning, and the approximation errors
are \(o_{\mathbb P}(n^{-1/2})\) for both runs. Existence of such a
transcript and approximation is outside these frozen inputs. No claim
about those obligations is included in this review.

## Final correction recheck and scoped verdict

The author made the two requested statement corrections and the optional
rank-envelope clarification. I read the changed passages and performed
an exact read-only content comparison: reversing only the corrections
listed below reproduced both original SHA-256 hashes above. Thus no
other source content changed between the reviewed versions and the
versions certified here.

- Scalar line 44 now states \(0\le B<\infty\), resolving Finding 1.
- Scalar lines 97–100 now fix deterministic sublinear rank envelopes
  for asymptotic uniformity, resolving Finding 3 for that source. The
  innovation induction already uses the fixed envelope \(r_n\) in
  its representation and finite-width thresholds.
- Innovation lines 347–349 now require fixed \(c>0\) and
  \(K_*<\infty\), uniform in width and admissible conditioning,
  resolving Finding 2.

The final reviewed source hashes are:

- `GELU_SILU_PROJECTED_SCALAR.md`:
  `eb6c0b39570216a6dda3d9ba7ad96fd12493da20bfd393f87af2d12fc1b44a29`.
- `GELU_SILU_PROJECTED_INNOVATION.md`:
  `fac32d132b76e002ef9a956a426d1a182a2aa1bece4eb04c51a7095c135fdb2b`.

**Final verdict: PASS within the stated conditional scope.** The scalar
variance bounds, uniform Gaussian approximation and small-ball estimate,
one-layer innovation estimate, fixed-depth innovation propagation under
the exact representation (9), and fourth-moment implication (22) are
supported by the complete proofs after these corrections. No unresolved
mathematical gap was found in those claims. Construction of the exact
conditional Gaussian representation, endpoint approximation error, and
the assembled endpoint theorem remain unaudited external obligations.
This internal PASS does not establish or authorize book promotion.

# Independent reconstruction of the integrated-collocation source lemma

2026-10-06. Bounded isolated internal reconstruction, not a promotion review.
Reviewer: fresh scoped agent `check_integrated_collocation`. The candidate
was frozen before this reconstruction; the reviewer did not author it and
did not read its author's conversation, the study README, or previous check
reports. Only this report was written. No experiment was run.

**Verdict:** the degree-independent integral-operator estimate, the stated
causal collocation error bounds, and the parameter-explicit source count
are correct under the supplied source interfaces. No correctness objection
remains to that conditional lemma. A compact autonomous decoder, its
all-time unseen-query guarantee, and its final resource bound remain
unproved by this candidate.

## 1. Scope, coverage, and frozen inputs

The neutral assignment was to reconstruct every implication concerning the
integrated interpolation constant, Banach dualization, quadrature
normalization, contraction/global error, all-time handoff, explicit
parameter substitution, and operation count, using only the candidate and
the following full dependencies. The assignment expressly excluded other
scientific retrieval and prior review findings.

All scientific lines in all five files below were read, including the
complete dependency bodies and qualifications. An initially truncated
batched display was repaired by complete separate reads of
`SHORT_CAUSAL_TRAINING_PROGRAM.md` and `PHYSICAL_PARAMETER_ACCOUNTING.md`.

| Input | Lines read | SHA256 |
|---|---:|---|
| `SANE_INTEGRATED_COLLOCATION.md` | 1–255 | `8e92214a0ab090b2d32636d4fdf7e31f3b479092fac29e71c62d0b2c9bd8c60e` |
| `SHORT_CAUSAL_TRAINING_PROGRAM.md` | 1–359 | `0fbffab2a0782cb34987f49c944491fb50f920c4c4acbd888548947131be35a5` |
| `PHYSICAL_PARAMETER_ACCOUNTING.md` | 1–512 | `395301fcca55af8937281f22b56c3ffe366d8e46fe7b4b12aeec35e5ca462279` |
| `COST_INTERFACE_PANEL.md` | 1–302 | `36eeedf00b30800e8dc8bf45dc60ac653570127dcc4e685eec59d5cec69a6ba8` |
| `docs/notation.qmd` | 1–98 | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |

The first four paths are in `studies/unseen_query_decoder_20261005/`.
Required process instructions and the complete `solve-math-rigorously`
skill were read. The prescribed canonical-notation skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`
was permission-denied both normally and with an escalated read. No readable
copy was found in the available skill roots. The lead confirmed the
unavailable-skill fallback; the explicit repository presentation rules and
the fully read maintained notation contract were applied. Its linked
neural-network reference could not be discovered through that inaccessible
file. This is a process limitation, not a substituted scientific input.

The upstream fitting event, activation recurrences, complex-time extension,
original label allowance, and stochastic width threshold are supplied
interfaces of this bounded packet. Their original proofs were not fetched
or independently re-audited. In particular, no source from another study,
`old_docs/`, `COST_CONTRACT.md`, or an existing `*_CHECK.md` was read.
Parameter definitions needed here are reproduced in the allowed dependencies.

## 2. Integrated interpolation, including complex and Banach data

Let \(s_j=(1+\cos\theta_j)/2\),
\(\theta_j=(j+1/2)\pi/K\), and let \(p=I_Kb\) have degree below
\(K\). For every integer \(1\le q<2K\),

\[
\frac1K\sum_{j=0}^{K-1}\cos(q\theta_j)
=\frac{\sin(q\pi)}{2K\sin(q\pi/(2K))}=0.
\]

The denominator is nonzero in this range. With
\(w(u)=1/(\pi\sqrt{u(1-u)})\), the substitution
\(u=(1+\cos\theta)/2\) gives
\(w(u)|du|=d\theta/\pi\). Thus integration against \(w\) and the
equal-weight node average agree on every polynomial of degree at most
\(2K-1\). When \(p\) has complex coefficients,
\(|p(u)|^2=p(u)\overline{p(u)}\), for real \(u\), is still a
polynomial in \(u\) of degree at most \(2K-2\). Consequently

\[
\int_0^1|p|^2w=\frac1K\sum_j|b_j|^2.
\]

Weighted Cauchy–Schwarz and
\(\int_0^1\sqrt{u(1-u)}\,du=\pi/8\) now give

\[
\left|\int_0^s p(u)\,du\right|
\le \left(\frac1K\sum_j|b_j|^2\right)^{1/2}
     \left(\int_0^s\pi\sqrt{u(1-u)}\,du\right)^{1/2}
\le\frac\pi{2\sqrt2}\max_j|b_j|.
\]

For vector data in the finite-dimensional normed space \(X\), apply
this scalar result to \(\lambda(b_j)\) for every continuous linear
functional \(\lambda\in X^*\) of norm at most one. Interpolation and
integration commute with \(\lambda\), and
\(\|v\|=\sup_{\|\lambda\|\le1}|\lambda(v)|\) in both the real and
complex cases. Taking that supremum proves exactly the same constant.
There is no use of a dimension-dependent equivalence with a Euclidean
norm. The Banach-valued step is therefore valid.

If \(p\) approximates \(g\) within \(e\), polynomial exactness yields

\[
\left\|\int_0^s(g-I_Kg)\right\|
\le e+\frac\pi{2\sqrt2}e<3e.
\]

Rescaling an interval of length \(h_i\) multiplies both integral bounds
by \(h_i\). A holomorphic function bounded by \(M\) on the disk of
radius \(2h_i\) about its midpoint has, on the interval, Taylor
remainder at most
\((4/3)M4^{-K}<2M2^{-K}\). Cauchy coefficient bounds establish this
also for the finite-dimensional vector norm by dualization. The candidate's
looser integrated defect \(6Mh_i2^{-K}\) is valid. Its choice
\(h_i\le r/4\) supplies the required disk from the inherited radius;
the shortened final interval only improves the inclusion. Analyticity is
used solely for \(g(t)=u'(t)\), not for the clipped extension away from
the true trajectory.

## 3. Quadrature, iteration, and global accuracy

The coefficient formula in the allowed short-program dependency, together
with
\(\int_0^1T_{2q}(2s-1)\,ds=1/(1-4q^2)\) and vanishing odd
integrals, gives the candidate's endpoint weights exactly. If
\(a=\lfloor(K-1)/2\rfloor\), then

\[
\sum_{q=1}^{a}\frac2{4q^2-1}=1-\frac1{2a+1}.
\]

Thus each bracket defining \(\omega_j\) is at least
\(1/(2a+1)>0\); at \(K=2\) the sum is empty and the weights are
\(1/2\). Constant-polynomial exactness gives \(\sum_j\omega_j=1\).
No extra physical factor is hidden: the endpoint rule is
\(h_i\sum_j\omega_jF(U_j)\).

For a patch of actual length \(h_i\le h\), the node map has Lipschitz
constant at most \(2h_i\Lambda\le1/4\). The full node space is
complete, and the globally bounded, globally Lipschitz real extension
defines the map everywhere. Its unique fixed point is therefore valid
without an invariant-domain hypothesis or an implicit-solve oracle.

Write \(e\) for the initial error, \(V\) for true node values, and
\(\eta=6M2^{-K}\). The residual of \(V\) in the numerical fixed-point
equation is at most \(e+h_i\eta\), so

\[
\|U^*-V\|_{\max}\le\frac{e+h_i\eta}{1-1/4}
\le2(e+h_i\eta).
\]

Boundedness of \(F\) gives
\(\|U^*-(b,\ldots,b)\|_{\max}\le2h_iM\). Starting at the constant
array \(b\), exactly \(J\) iterations therefore leave error
\(\zeta_i\le2h_iM4^{-J}\). The additional final field evaluation
uses \(F(U^{(J)})\) to define both the polynomial patch path and its
committed endpoint. It must be counted, and the candidate does count it.

Positivity and normalization of the endpoint weights give

\[
e_{\rm next}\le(1+2h_i\Lambda)e
 +h_i\eta(1+2h_i\Lambda)+h_i\Lambda\zeta_i.
\]

For \(J=K\ge2\) and \(h_i\Lambda\le1/8\), the two forcing terms
are at most

\[
\left(\frac{15}{2}+\frac1{16}\right)Mh_i2^{-K}
<8Mh_i2^{-K}.
\]

For a partition whose lengths sum to \(T\), iterating this recurrence
from zero initial error yields
\(8MT e^{2\Lambda T}2^{-K}\); the variable final step needs no
separate estimate. At an interior time the integrated operator replaces
the positive endpoint rule, producing

\[
(1+4h_i\Lambda)e
 +(1+4h_i\Lambda)h_i\eta+2h_i\Lambda\zeta_i.
\]

Using \(h_i\le1/8\), its first term is at most
\(12MT e^{2\Lambda T}2^{-K}\), and its remaining terms are below
\(2M2^{-K}\). This proves the stated, more generous envelope
\(32M(T+1)e^{2\Lambda T}2^{-K}\).

For the candidate's degree choice, multiplying this envelope by the
observation sensitivity \(B\) gives the explicit estimate

\[
\sup_{t\le T,\,\|v\|=1}
 |f(u(t),v)-f(\widetilde u(t),v)|
\le\frac{32BM(T+1)}{1+128BM(T+1)/\varepsilon}
<\frac\varepsilon4.
\]

Thus the proposed degree suffices, with slack, for the stated
\(\varepsilon\) target. No stability cost has been moved into an
unspecified lower bound on width. Rounding to a power of two increases
the degree by less than a factor two, except for the harmless explicit
lower bound two.

## 4. Parameter substitution and all-time prediction handoff

Here \(r=m/\gamma\), distinct from the abstract analytic radius in
Section 3 of the candidate; the latter is now \(r_\tau\). Retain
\(\ell=\log(en)\), \(B=\beta^{100L}\), and
\(Z=(a_0+1)\ell+\log(e+B(1+r))\). The allowed accounting dependency
supplies

\[
M\le B(1+r),\quad\Lambda\le B(1+r)\sqrt\ell,
\quad r_\tau^{-1}\le B\sqrt\ell,
\]

and sensitivity at most \(B\) for normalized prediction versus
normalized displacement. One may use the displayed upper bound for
\(\Lambda\), which is at least one.

Choose the stated upper horizon
\(T=2[a_0\log n+\log(1+66Br)]\), or the inherited horizon involving
the smaller fitting constant \(H^2\). An arbitrary smaller horizon is
not justified merely by the phrase “no larger than”; the chosen horizon
must still meet the inherited tail requirement. With either of these
two stated choices, \(T\le CZ\), and the supplied normalized tail is

\[
\frac{65}{4}H^2r e^{-T/2}
\le \frac{65Br}{4(1+66Br)}n^{-a_0}
<\frac14n^{-a_0}.
\]

The formula with the smaller fitting constant has the same inequality
with \(B\) replaced by \(H^2\). Taking
\(\varepsilon=n^{-a_0}/2\) gives numerical prediction error at most
\(n^{-a_0}/8\). Freezing the numerical endpoint after \(T\), the
triangle inequality therefore gives normalized prediction error less
than \(3n^{-a_0}/8\) for all later times, including the limiting
endpoint. Before \(T\) the finite-horizon bound applies. Multiplying
by \(Y\) returns physical predictions. This conclusion is uniform on
the real sphere under the supplied observation bound; it does not need
a spatial net. It asserts neither exact fitting by the numerical program
nor analyticity of the clipped numerical field.

Let \(H\) now denote the number of patches, as in the cost formula.
Then

\[
H=\lceil T/h\rceil
\le1+T\max\{4r_\tau^{-1},8\Lambda\}
\le CB(1+r)Z\sqrt\ell.
\]

The logarithm in the degree formula is bounded by a numerical multiple
of \(Z\): its parameter contributions are at most
\(2\log B+\log(1+r)+\log(T+1)+a_0\log n+O(1)\).
Together with \(\Lambda T\le CB(1+r)Z\sqrt\ell\), this proves
\(K=J\le CB(1+r)Z\sqrt\ell\). Therefore

\[
N_F=HK(J+1)\le CB^3(1+r)^3Z^3\ell^{3/2},
\]

and the \(O(mL)\) initialized matrix calls and principal fields per
evaluation, plus \(d\) first-layer root coordinates, give exactly

\[
C\left[d+mL\beta^{300L}(1+m/\gamma)^3Z^3\ell^{3/2}\right]
\le C\left[d+mL\beta^{300L}(1+m/\gamma)^3Z^{9/2}\right].
\]

The last step uses \(\ell\le Z\). Label normalization removes inverse
powers of \(Y\) from this expression; it does not change the inherited
label allowance, input-description costs, or deterministic/stochastic
width qualifications. The gap dependence is cubic in \(m/\gamma\);
the whole expression is not cubic in \(m\) when \(\gamma\) is held
fixed because of the leading \(m\).

## 5. Operations, storage, and the exact boundary of the result

Put \(D=Ln^2+dn\), an upper bound up to a universal factor for the
dense parameter dimension including readout. One field evaluation costs
\(O(mD)\) scalar arithmetic with the supplied exact-real activation
and square-root primitives. For each state coordinate and each Picard
iteration, the allowed coordinate schedule uses \(O(K^2)\) work to
form cosine coefficients and evaluate their integrated polynomial, with
\(O(K)\) scratch. Hence

\[
O(HJK^2D)+O(N_FmD)+O(HK^2D)
\le C N_FD(m+K).
\]

The last term covers the final path coefficients. Two generations of
dense node arrays, the current endpoint, initialized matrices, and
reusable scalar scratch occupy \(O(DK)\) real coordinates. The
antiderivative identities in `COST_INTERFACE_PANEL.md` integrate the
degree-zero and degree-one terms correctly and give the degree-at-most-
\(K\) polynomial for the remaining terms; no \(K^2\) integration
array is needed. Its power-of-two node construction uses arithmetic and
positive square roots. These exact-real facts imply no finite-precision
stability claim.

The live-stage bound concerns source generation. Retaining every dense
patch polynomial for arbitrary later access would add output/history
storage; streaming specified sample times in chronological order can
reuse patch storage. The candidate expressly excludes output coefficient
arrays from its displayed live-stage count. Primitive descriptions,
workspace and non-unit primitive costs remain chargeable as in the full
allowed interface note.

The exact conditional lemma checked here is a finite causal dense source
solver with the displayed uniform prediction accuracy and smaller count
of initialized matrix actions. Its vectors still have width \(n\), and
its implementation still accesses initialized dense matrices.

The following stronger handoffs remain unresolved, consistently with the
candidate's express limitations:

- The normalized prediction schedule with fixed \(a_0=10\) is not itself
  a certificate for the passive-source target
  \(Y\beta^{-200L}/((Q+1)n^3)\) in Section 6 of the parameter-accounting
  dependency. That target concerns feature/backward coefficients with
  additional sensitivity. The integrated lemma can be rerun with that
  explicit state target, but its source-sampling/tail and coefficient
  budget must be stated and checked. The current candidate does not claim
  this completed replacement.
- The noisy-row compiler, all retained scalar summaries, history
  conditioning, selection precision, and query perturbation propagation
  must be checked for the revised chronological program. A lower number
  of dense calls does not perform those checks.
- Storing every pair of the named history fields would square their
  count, producing a loose logarithmic power nine from this bound. This
  is a warning about that construction's accounting, not a lower bound
  excluding a better representation.
- No autonomous compact state, cheap late query theorem, final small
  memory exponent, or bit-cost guarantee follows from this lemma. The
  inherited stochastic success threshold is still unevaluated.

## 6. Checks actually performed and completion

The checks were complete algebraic reconstruction, including the complex
polynomial exactness range, dimension-independent dual norm step, the
\(K=2\) empty quadrature sum, the last shortened patch, the final extra
field evaluation, and the label/time normalization. No numerical trial,
training run, compiler execution, or stochastic reproduction was used or
claimed. No external theorem or web source was needed.

Operational commands included full `cat` reads, the repaired separate
dependency reads, `sha256sum` on the five inputs, `wc -l` for coverage,
and metadata-only `git rev-parse HEAD`, `git status --short`, and
`git diff --cached --name-only`. HEAD at the pre-write check was
`e0d0908797a63512b8f91ce234c4597249f8a2ec`; the index was empty and
unrelated concurrent working-tree changes were preserved. No Git write
was performed. Final input hashes were rechecked after report creation.

There is no unresolved correctness objection within the bounded
conditional source lemma. The unavailable notation skill and unaudited
upstream scientific interfaces are disclosed above. All stronger decoder
and precision claims remain at their prior, unproved level. This report
is complete for its assigned input scope and does not certify promotion.

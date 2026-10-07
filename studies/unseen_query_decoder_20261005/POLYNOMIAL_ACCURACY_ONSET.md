# Polynomial accuracy onset: what additional sampling can and cannot prove

2026-10-07. Bounded author route in the current study. Proof-only; no
experiment, implementation, Git mutation, or promotion. The new elementary
arguments below have been checked by their author. They are not an
independent reconstruction of the imported neural interfaces.

**Outcome.** Optimizing or repeating the existing prior-block estimator
does not remove its eventual-width absorption condition. There are two
separate obstacles: the posterior/prior sampling comparison and the
passive-population-to-dense comparison. The first has a sharp generic
counterexample under the supplied entropy/moment assumptions; the second
survives an exact evaluation of all passive posterior moments. Neither
result proves a neural lower bound or rules out another compact decoder.
No polynomial-width theorem for the complete current model is proved here.

## 1. Contract and the two errors that must be distinguished

Keep width \(n\), depth \(L\ge2\), \(m\ge d\) spanning training
inputs of norm \(\sqrt d\), the original Gaussian first/hidden weights,
zero initial readout, mean squared loss, and block mobilities
\((n,1,\ldots,1,n)\). All hidden layers continue to learn. Keep the
strip-analytic activations, positive population feature-Gram gap
\(\gamma\), and the full inherited label intersection. In particular,
\(16Ym/\gamma\le1\), where \(Y=\|y\|_2/\sqrt m\), is only a
consequence of that intersection. The assigned notes do not spell out
the full intersection; it remains an imported scientific interface.
The case \(Y=0\) has the separate exact zero predictor.

The observable is the scalar network prediction, simultaneously for
every sphere input, every physical training time, and the fitted endpoint.
An unseen query uses only the current compact state. Its training scalar
recursion is not replayed. The reference is an independent dense run of
the same width. The allowed preprocessing is the existing completed-source
construction. Retained random bits and peak query scratch are charged.

Let \(\beta,Z,R,p,\mathcal B,\mathcal C,\mathcal P,K_*\) have the
meanings in the assigned current notes. In particular,

\[
 Z=\log(en)+\log\left(e+
 \frac{(m+d+2)\beta^{100L}(1+m/\gamma)}{\delta}\right),
\]
\[
 R\le C\beta^{201L}(m+d+2)(1+m/\gamma)Z^{5/2},\qquad
 p\le C\beta^{110L}Z.
 \tag{1}
\]

These are the prescribed sufficient choices of
GAP_REFINED_PHASE_COSTS.md, not arbitrary smaller values. At a fixed
good current scalar prefix \(c\), write \(\mu\) for the actual finite
packet prior and \(\nu_c\) for the proof-only one-row posterior.
For the complete pair count \(P\asymp R^2\), scalar noise \(\eta\),
bounded pair-test cap \(B_F\), and confidence share \(\alpha=c\delta\),

\[
 K_* =\max\left\{1,\frac{P}{2\alpha}
             \log(1+B_F^2/\eta^2)\right\},\qquad
 D(\nu_c\Vert\mu)\le K_*/n,
 \qquad K_*\asymp R^2p/\alpha.
 \tag{2}
\]

The second relation is a sufficient information certificate, not a lower
bound on actual information. A passive cross moment has the form
\(\nu_c(VG)\), where \(V\in\mathbb R^r\), \(r\le CR\),
\(\nu_c(VV^\top)\preceq I_r\), and \(|G|\le\mathcal B\).
The passive Gaussian moment recursion and its normalized final value
\(d_{\nu_c}(c;t,x)\) are exactly those of FAST_FINITE_PASSIVE.md (26).
Its fixed-depth propagation allowance is

\[
 \mathcal P=(1+\mathcal C)
 [C(1+\mathcal B)^2(1+\mathcal C)(1+\beta)^2]^{L+2},
 \tag{3}
\]

with the \(\mathcal B,\mathcal C\) bounds of the current synthesis.

At a fixed allocated confidence share, distinguish the three positive
inherited constants in the benchmark by writing

\[
 b_n=\frac{c_0Y}{\sqrt n}
 e^{c_1Y^2\sqrt{\log(en)}}
 \sqrt{8\log\frac{8(n+1)(1+2n)^d}{\delta_0}}
 +\frac{c_2Y}{n},\qquad
 \rho_n=\frac{\sqrt n\,b_n}{Y}.
 \tag{4}
\]

No uniform polynomial dependence of \(c_0,c_1,c_2\) on the problem
parameters is supplied by these inputs. The constants in (1) and the
internal resource counts below have the different, universal meaning.
The benchmark in (4) is not enlarged in this note.

FAST_FINITE_PASSIVE.md separates two conclusions. Its population value
obeys

\[
 |Yd_{\nu_c}(c;t,x)-f_{0,n}(t,x)|
 \le b_n+CY\mathcal P\sqrt{(K_*+R+1)/n}+CYn^{-10}.
 \tag{5}
\]

Here \(f_{0,n}\) denotes the proof-only deterministic center at this
width. The added subscript asserts no new dependence; it avoids assuming
a center common to different widths. The finite implemented prior-block
decoder instead has the full comparison

\[
 \sup_{t,x}|\widehat f_n(t,x)-f_n^{\rm independent}(t,x)|
 \le2b_n+CY\mathcal P
       \sqrt{(R+1)(K_*+1)/n}+CYn^{-10}.
 \tag{6}
\]

All-time and whole-sphere events in (5)--(6) are inherited from that
note's two-filtration comparison and physical external grid. Neither is
reproved by a fixed-context sampling lemma.

## 2. Optimizing the existing block proof

The following calculation is exact for the stated certification method.
It is not an error lower bound for its neural implementation.

Fix a local tolerance \(a>0\) for \(\nu_c(VG)\). Under
\(\nu_c^{\otimes s}\), each coordinate block mean has variance at most
\(\mathcal B^2/s\). Chebyshev gives probability at most \(1/16\)
of coordinate error exceeding \(4\mathcal B/\sqrt s\). Its transfer
to prior blocks uses

\[
 \|\nu_c^{\otimes s}-\mu^{\otimes s}\|_{\rm TV}
 \le\sqrt{sK_*/(2n)}.
 \tag{7}
\]

With a dyadic certificate \(K_*\le\widehat K_*\le2K_*\), the
existing choice requires

\[
 s\le \frac{n}{128\widehat K_*}.
 \tag{8}
\]

Indeed (7) is then at most \(1/16\). Each prior block fails with
probability at most \(1/8\). For odd \(J\), coordinate medians have
Euclidean error at most \(4\mathcal B\sqrt{r/s}\), except on an
event of probability at most \(r2^{-J/2}\). This last bound follows by
summing over the subsets of at least \(J/2\) failed blocks:
\(2^J(1/8)^{J/2}=2^{-J/2}\).

Consequently a sufficient local radius \(a\) can be certified by this
argument only if the chosen block size also satisfies

\[
 s\ge\frac{16\mathcal B^2r}{a^2}.
 \tag{9}
\]

The continuous versions of (8)--(9) have a common solution exactly when

\[
 a^2\ge\frac{2048\mathcal B^2r\widehat K_*}{n}.
 \tag{10}
\]

Integer rounding changes only a factor of two when the upper endpoint
in (8) is at least two. A smaller block raises the certified radius.
A larger \(J\) raises confidence but does not change (10). Replacing
the constants \(1/16,1/8\) by other fixed successful block probabilities
changes constants in (10), not its dependence on \(r,K_*,n\).

After fixed-depth propagation, the same calculation is the bound-level
condition

\[
 C\mathcal P\sqrt{(R+1)(K_*+1)}+Cn^{-19/2}\le\rho_n
 \tag{11}
\]

for advertising \(3b_n\) from (6). This is the old absorption test,
now obtained by optimizing all admissible block sizes. There is no
unused choice of block count that makes its left side divide by
\(\sqrt J\).

Even granting an exact oracle for every moment of \(\nu_c\) would
only delete the sampling term, leaving from (5)

\[
 2b_n+CY\mathcal P\sqrt{(K_*+R+1)/n}+CYn^{-10}
 \tag{12}
\]

as the currently proved dense-reference bound. Thus a new estimator
alone cannot establish the desired conclusion through the existing
population comparison. The bounds in (11)--(12) are upper certificates;
their failure to fit \(b_n\) is not evidence that the true errors are
that large.

## 3. Why arbitrary repetition cannot remove posterior/prior bias

Here is a sharp scalar counterexample to a stronger inference from just
the entropy and moment interface. It uses finite packets, as the source
does, but does not assert a reachable neural history.

Let \(0<h\le1\), let \(\mu\) assign probability \(1/2\) to each
of \(-1,+1\), set \(\theta=\sqrt h/2\), and define

\[
 \nu\{+1\}=\frac{1+\theta}{2},\qquad
 \nu\{-1\}=\frac{1-\theta}{2},\qquad V(z)=1,\quad G(z)=z.
 \tag{13}
\]

Then \(\nu(V^2)=1\), \(|G|=1\), and \(\nu(VG)=\theta\).
Writing the relative entropy as \(g(\theta)\), direct differentiation
gives

\[
 g(0)=g'(0)=0,\qquad g''(u)=\frac1{1-u^2}.
\]

Because \(0\le\theta\le1/2\), integration twice gives
\(D(\nu\Vert\mu)=g(\theta)\le(2/3)\theta^2\le h\).

For every block length and every odd repetition count, a coordinate
median of prior block means changes sign when all its sampled packets
change sign. Its distribution under \(\mu\) is therefore symmetric
around zero. A symmetric random variable lies in
\((\theta-a,\theta+a)\subset(0,\infty)\) with probability at most
\(1/2\), for every \(0<a<\theta\). No number of independent
repetitions of these prior medians can give confidence greater than
\(1/2\) at such a radius. Averaging independent copies of the median
is still sign-symmetric and has the same obstruction. A generator that
fools the corresponding finite success test to error \(\zeta\) changes
that upper bound to at most \(1/2+\zeta\).

Taking \(h=K_*/n\le1\) exhibits a discrepancy of order
\(\sqrt{K_*/n}\) that unlimited prior sampling does not remove.
The example concerns the estimator and hypotheses (2), not all ways of
using the source. The actual source determines \(\nu_c\) through its
known likelihood, and its acquired moments can provide controls. No
claim is made that (13), with otherwise arbitrary stored marks, is a
posterior of the current neural source. In particular this example
neither proves the factor \(\sqrt R\) optimal nor rules out a sharper
neural-specific information or generalization theorem.

## 4. Extra repetitions can be stored compactly, with their work charged

The statistical limitation is not a memory excuse. Let \(Q\le C(L+1)\)
be the number of passive stages, let \(J\) be any prescribed odd
repetition count at least the physical-code confidence requirement, and
let \(N=Js\) be its stream length. Here \(N\) counts query samples;
it is not a new dense width. Put

\[
 E=1+\lceil\log_2(N+2)\rceil,\qquad
 F=C\{(d+1)p+\log(Q(R+1)/\delta+2)\},
\]
\[
 A=C\{Rp+F+E\}.
 \tag{14}
\]

The imported one-pass generator uses \(CAE\) stored seed bits per
stage, \(CA^2E\) work per packet, and \(CA\) scratch. Its tests
retain the fixed current query context, one coordinate block sum,
threshold counters, and a counter of \(E\) bits. For full-vector tests
one may use \(CRp\) running-sum bits; both fit (14). The passive stage
seeds remain mutually independent and independent of the source. They
are reused across codes exactly as in the reachable-context proof.

At local word length \(p\), a simultaneous-vector implementation
therefore has the modular bounds

\[
 \begin{split}
 S_{\rm peak}&\le C\{R^2p+JRp+QAE\},\\
 W_{\rm query}&\le CQ\{Js(Rp^4+R^2p^2+A^2E)
                +R^5p^2+R^4p^3+RJp\log(J+2)\}.
 \end{split}
 \tag{15}
\]

The row terms are, respectively, finite Gaussian generation, finite row
arithmetic, and generator work. The last terms count a conservative
uncached coefficient preparation and actual median sorting. Evaluator
work, its live workspace, and the original input/certificate interfaces
are added as in the assigned sources. No new unit-cost primitive is used.
The usual implementation, \(J=O((d+1)p)\), \(E=O(p)\),
\(A=O(Rp)\), recovers
\(C[R^2p+(L+d+2)Rp^2]\) retained/peak bits.

If \(J\) is much larger, the \(JRp\) array need not be retained.
For each output coordinate, find its exact dyadic median by binary search
over the \(p\)-bit output range. At each threshold, regenerate the same
stream, retain a block sum and a count of block means below the threshold,
and then choose the next threshold. There are at most \(p+O(1)\)
passes per coordinate. Retain the completed coordinate medians and apply
the moment guard only after all coordinates have been computed. The
incoming context and prepared coefficients stay fixed during these passes.

This schedule computes exactly the median from (15). Hence its accuracy
is still certified by the original one-pass failure tests; it makes no
new claim that the generator fools arbitrary repeated-read programs.
Its peak bits and conservative work are

\[
 S_{\rm peak}\le C\{R^2p+QAE+Rp+E\},
\]
\[
 W_{\rm query}\le CQ\{Rp\,Js(Rp^4+R^2p^2+A^2E)
                         +R^5p^2+R^4p^3\}.
 \tag{16}
\]

If \(Js\) is polynomial in \(n\) and the explicit problem parameters,
\(E\) still fits the existing precision certificate up to a fixed
factor. Thus arbitrary polynomial repetition can retain the same order
of compact seed/scratch storage, with its extra work fully present in
(16). Equations (10)--(13) nevertheless continue to apply. Increasing
\(J\) is useful for confidence, not for eliminating the stated bias.

## 5. Exact requirements for a useful control variate

Let \(X=VG\in\mathbb R^r\). Suppose the query computes a control
\(C_0\) and a vector \(m_0\) satisfying

\[
 \|m_0-\nu_c C_0\|_2\le e_{\rm ctrl},\qquad
 \sum_{i=1}^r\nu_c[(X_i-C_{0,i})^2]\le V^2.
 \tag{17}
\]

The inherited control lemma gives local error
\(e_{\rm ctrl}+4V/\sqrt s\). With the maximal allowed block
length, achieving local tolerance \(a>e_{\rm ctrl}\) by this proof
requires, up to the explicitly harmless integer factor,

\[
 V^2\le\frac{n(a-e_{\rm ctrl})^2}{2048\widehat K_*}.
 \tag{18}
\]

If the local tolerance allocated after all later propagation is
\(a=c\rho_n/(\mathcal P\sqrt n)\), a sufficient route would
therefore need

\[
 e_{\rm ctrl}\le a/2,\qquad
 V^2\le\frac{c'\rho_n^2}{\mathcal P^2\widehat K_*}.
 \tag{19}
\]

These are uniform posterior bounds over all good prefixes and reachable
query contexts. All computation/storage for \(C_0,m_0\), their
coefficients, and their precision must be added. For a linear combination
of acquired pair tests, its known mean has error at most the scalar
pair error times the coefficient \(\ell^1\) norm; an unknown
projection condition number cannot be omitted.

The supplied analytic assumptions and fresh-Gaussian averaging do not
prove (19). For example, if \(Z,g\) are independent standard normals
and \(a\ne0,v>0\) are fixed, then

\[
 X=\sin(aZ+\sqrt v\,g),\quad
 \mathbb E[X\mid Z]=e^{-v/2}\sin(aZ),\quad
 \operatorname{Var}(\mathbb E[X\mid Z])
 =\frac{e^{-v}}2(1-e^{-2a^2})>0.
 \tag{20}
\]

Integrating the last Gaussian removes only its conditional variance.
This example is elementary and its total mean is exactly known; it is
not an integration-hardness example. A useful neural-specific control
could still exist. Even proving (19) leaves the population comparison
(5) as a separate obligation.

## 6. Direct posterior sampling and a larger source

### Direct posterior sampling

Exact independent samples from \(\nu_c\) would remove the product-TV
restriction (8). For instance, vector block Chebyshev at local tolerance
\(a\) would then allow \(s\ge16\mathcal B^2r/a^2\), with no
upper restriction proportional to \(n/K_*\). However, the assigned
packet supplies no such sampler with polynomial work and compact memory.
Moreover its output would still target the population object in (5), so
the remaining bridge (12) would survive.

A bare instruction to reject prior arrays according to their transcript
likelihood is insufficient to give a polynomial sampler. To see the
general problem without claiming a neural lower bound, consider a prior
array with \(n\) even and \(P\) independent Rademacher columns, and
condition on zero sum in each column. Rejection of an entire prior array
accepts with probability

\[
 a_n^P,\qquad a_n=2^{-n}\binom n{n/2}\le(n+1)^{-1/2}.
 \tag{21}
\]

For completeness, with \(n=2k\),
\(a_{2(k+1)}/a_{2k}=(2k+1)/(2k+2)\). Induction from \(a_0=1\)
proves the inequality in (21), because
\((2k+1)(2k+3)\le(2k+2)^2\).
The expected number of attempts is at least \((n+1)^{P/2}\).
This particular conditional law has efficient specialized samplers;
(21) disproves only a general polynomial guarantee for this rejection
proposal. It does not prove that conditional sampling is hard.

The unchanged current-source likelihood may have additional usable
structure. A proof exploiting it must specify the actual sampler,
restartable randomness, numerical likelihood evaluation, failure bound,
and peak scratch. None can be supplied merely by the entropy bound (2).
To bypass (5) as well, an algorithm would need to approximate the exact
conditional physical-output law or provide a new population comparison,
not just sample its passive moment approximation more accurately.

### A larger virtual dense width

Replacing the source width by \(N>n\) would reduce its passive error
to \(CY\mathcal P_N\sqrt{(R_N+1)(K_{*,N}+1)/N}\). The current
proof then compares its answer to \(f_{0,N}\), not automatically to
\(f_{0,n}\). A valid transfer to the width-\(n\) reference would need
the additional term

\[
 \sup_{t,x}|f_{0,N}(t,x)-f_{0,n}(t,x)|.
 \tag{22}
\]

No assigned current-study input bounds (22). Same-width pair
concentration cannot imply that bound: deterministic scalar sequences
\(f_n\equiv a_n\), with arbitrary \(a_n\), have zero same-width
pair discrepancy and unrestricted cross-width centers. This is a
logical counterexample to that inference, not a neural example.

If a common-center or quantitative cross-width theorem is supplied, the
larger source becomes a legitimate candidate provided all costs are
changed: initialization includes \(CN R_N^5p_N^3\), temporary
initialization bits include \(CN R_Np_N\), and query stream work has
its factor \(N\), with \(R_N,p_N\) built from \(\log(eN)\).
The smaller retained count does not make this larger width free. Its
scientific width gates and the benchmark constants also remain to be
controlled. This note has not used (22) as an assumption.

## 7. An existing slower decoder has a different absorption problem

RESULT.md reports the earlier compact Fourier decoder at
\(2b_n+1/n\), at its own stated confidence allocation. If that imported
theorem is granted and the same allocation is used in the benchmark,
then, since the square-root logarithm in (4) exceeds one,

\[
 b_n\ge c_0Y/\sqrt n,\qquad
 n\ge(c_0Y)^{-2}\quad\Longrightarrow\quad 1/n\le b_n.
 \tag{23}
\]

Its particular additive-error absorption therefore does not require
the factor \(\exp(c_1Y^2\sqrt{\log(en)})\). This observation is
conditional on the reported Fourier theorem: its full proof and resource
dependencies were not among this route's assigned inputs. It does not
establish polynomial total work, a polynomial scientific/source width
threshold, or polynomial dependence of \(1/c_0\). RESULT.md explicitly
permits enormous Fourier evaluation work. Equation (23) is useful because
it separates the fast passive method's limitation from a purported
universal obstruction to compact storage.

## 8. Checked claims, missing bridges, and provenance

| Claim | Status and precise boundary |
|---|---|
| Optimizing current TV-transferred block sizes leaves (10)--(11) | Elementary author proof; obstruction to this certificate only |
| Arbitrary prior-median repetitions can have a bias of order \(\sqrt{K_*/n}\) | Elementary finite-law example (13); no neural-reachability claim |
| Polynomially many additional samples can retain compact seed/scratch storage | Conditional counted schedules (15)--(16), using the assigned generator/row interfaces |
| Exact posterior passive moments remove all absorption terms | False for the existing argument; (5) still leaves (12) |
| A uniform posterior control satisfying (19) is available for the full model | Open in assigned inputs |
| Naive conditional rejection always has polynomial work | False for that proposal; (21) is a finite-product counterexample |
| Oversized source can be compared to target width without an extra theorem | Unsupported; missing (22), with all larger-width costs separately charged |
| Reported Fourier remainder has polynomial absorption in \(1/(c_0Y)\) | Elementary implication (23), conditional on the imported reported theorem |
| Full broad neural decoder has polynomial scientific and accuracy onset | Not established here |

The highest-leverage missing bridge for this fast route is a
neural-specific estimate that controls the exact current-prefix
conditional physical output at the unchanged benchmark, together with
a counted way to evaluate that law. Improving only the number of prior
blocks cannot provide that bridge. A uniformly effective control (19)
and a sharper version of (5) are a different concrete pair of obligations.

All scientific lines of the following eight assigned current-study files
were read. No linked companion proof or other study was fetched. The
supervisor supplied scope/route feedback, so this is an author route,
not a blinded review. A proposed cross-width retrieval was not used; the
missing-premise statement above rests solely on the assigned inputs.
Required research/proof and canonical-notation skills, including the neural
reference, were read. Author checks were symbolic derivations of
(7)--(13), (18), (21), and (23), and term-by-term accounting of
(14)--(16); no numerical experiment was used.

| Input | SHA-256 |
|---|---|
| GAP_REFINED_PHASE_COSTS.md | `817617951efb926d2729cd7f20eaccf7cb5c4e25e17eb531502c8b2618e017bc` |
| FAST_FINITE_PASSIVE.md | `7f298bc637afffc207375692ee725290e752cdeb818b42f82563646f74416777` |
| FAST_LOCAL_COMPOSITION.md | `7d101fd08dd5e612963263bb5dd565b146d4ca3b330adb074bd5673b77f40bb2` |
| FAST_UNIFORM_QUERY.md | `e59f805980ddc664794eee8c0f310f51667e94592d4ee502978663e77c64bcd9` |
| FAST_FINITE_POSTERIOR.md | `f3cc565c52e848611d576d877ca893964cf45a74fb35f86c0494fbe8b09413db` |
| FAST_PHYSICAL_QUERY_GRID.md | `bd275d6163f54e0668d55be576c789bdeedae2e447a3dffe0881c4cc7defaa0a` |
| RESULT.md | `ca3a6dd0afd9b64c607a8daf00552e84ff7018a12cab1a92aad4649cfbe702cc` |
| HIDDEN_DEPENDENCY_AUDIT.md | `cffc32a3f1c64cdcd75b8cdf1f5486cd8166d6451b0a6a29c67fde418d608077` |

Metadata before this edit: HEAD
`e0d0908797a63512b8f91ce234c4597249f8a2ec`; index empty; existing unrelated
working-tree changes preserved. Only this assigned note was written.

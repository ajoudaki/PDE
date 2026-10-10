# Independent check of oblivious temporal sources and state

Check status: **PASS within the assigned source, approximation, provenance,
and accounting scope.** The final single-interval construction has the
claimed analytic endpoint approximation and polylogarithmic order. Its
runtime uses its own online moments and does not require dense source
coefficients, an adapted response basis, or future trajectory samples.
No mathematical correction is requested in this scope. One wording
clarification concerning the probability qualifier is recommended below.

The result concerns the explicitly modified method: a growing physical-time
interval, a regular initial branch, and a deterministic readout-only tail.
It does not prove the same order for the unchanged residual-clock method.
This distinction, and the exclusion of a globally locally-Lipschitz vector
field on all clock states, are substantive qualifications already stated
by the candidate.

## Scope and frozen sources

The complete candidate was read, with the final single-global-interval
section treated as the primary construction. Scientific inputs were limited
to that candidate and the five allowed paper files. The source proposition,
fitting and signed-comparison interfaces, Legendre projection estimates,
and dense-variability normalization were checked against those files.
Previously read unchanged source and required skill instructions were
reused. This is not an independent reproof of the full probabilistic source
proposition, nor a promotion review. No other study artifacts or review
findings were consulted for this check.

| Frozen input | SHA-256 |
| --- | --- |
| `OBLIVIOUS_WINDOWS.md` | `7cd8051dda86a6bc7bee09cd46ab51ddce1fb8d21f7891f97148e34cc6137298` |
| `paper/compact.tex` | `47199d5c9e374b80b9eafefd60699c2f4bfe06dde00ebd0a1c53e2805598a0c4` |
| `paper/compact_foundations.tex` | `6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0` |
| `paper/compact_selected.tex` | `3add2b694f38a4d7dbce90e51dafd375a7e8dee2e06d26b2d5af451bddb44885` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `paper/compact_legendre.tex` | `862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9` |

## Physical backward histories have the required source bound

The physical backward history is
\(b_a^{(\ell)}(t)=r_a(t)\delta_a^{(\ell)}(t)\), with no residual
normalization. Proposition `cp:source(i)` bounds the dense forward vectors
and residual-free backward vectors on the whole complex time rectangle.
It includes the readout through the pre-gated response \(k^{(L)}=w\).
Consequently the dense predictions obey
\[
|f(t,x_a)|
\le \frac{\|w(t)\|_2}{\sqrt n}
     \frac{\|h^{(L)}(t,x_a)\|_2}{\sqrt n}
\le16\beta^{7L}z,
\qquad z=Y/\lambda,\quad \lambda=\gamma/m.
\]
The norm here is the complex Euclidean norm; the network's bilinear
readout remains holomorphic. The sample residual RMS on the complex
rectangle is at most \(16\beta^{7L}z+Y\). Thus
\[
\left(\frac1{mn}\sum_a\|r_a\delta_a^{(\ell)}\|_2^2\right)^{1/2}
\le \max_a\frac{\|\delta_a^{(\ell)}\|_2}{\sqrt n}
     \left(\frac1m\sum_a|r_a|^2\right)^{1/2}
\le272\beta^{11L}z^2.
\]
The last step uses \(Y\le z\), because \(\lambda\le1\).
There is no missing \(\sqrt m\): the argument requires the residual
RMS, not a false bound \(\max_a|y_a|\le Y\). Products of the
holomorphic fields are holomorphic, so candidate (10) is a valid bound
for the exact physical backward history being compressed.

## Uniform approximation on every growing interval

Use the candidate's deterministic horizon \(T\), source radius
\(r_t\), and \(A=\max(1,T/r_t)\). For every \(0<t\le T\), the
ellipse for \([0,t]\) with parameter \(e^{1/A}\) lies strictly
inside the source rectangle. Its imaginary half-height is
\(t\sinh(1/A)/2<r_t\), and its real excess is
\(t[\cosh(1/A)-1]/2<r_t\). These inequalities are uniform in
\(t\); shrinking the interval does not worsen the approximation.

Cauchy's integral in the Joukowski variable bounds the degree-below-
\(q\) Chebyshev tail of either aggregate Hilbert-valued history by
\(4BAe^{-q/A}\), where \(B\) is its complex norm bound. The
paper's endpoint operator bound
\(\|(\Pi_q g)(t)\|\le64\sqrt q\|g\|_\infty\) is invariant
under affine interval rescaling. Subtracting the Chebyshev polynomial,
on which the Legendre projection is exact, therefore gives exactly
candidate (19):
\[
\|g(t)-(\Pi_q^{[0,t]}g)(t)\|
\le4(1+64\sqrt q)BAe^{-q/A}.
\]
The same Hilbert norm permits aggregation over training examples before
the estimate is applied. No analyticity of the online compressed path is
needed: analyticity is used only for the dense reference histories, and
the endpoint operator bound controls their difference from online
histories.

With \(q=\lceil16A\log(en)\rceil\), the exponential is at most
\((en)^{-16}\), whereas \(A\), \(q\), and the remaining
prefactor grow as fixed powers of \(\log(en)\) for each fixed problem.
The uniform endpoint error is consequently at most \((en)^{-8}\)
eventually. This is one deterministic statement on the same source event
for all growing intervals and all used orders; no continuum or
order-dependent probability union is required.

For completeness, the product-defect use of these estimates has the right
order. The forward endpoint error is bounded by a constant times
\(\sqrt q[\varepsilon+D(t)]\); the physical backward endpoint error
is bounded by a constant times
\(\sqrt q(1+\sqrt{\log(en)})[\varepsilon+D(t)]\).
Cauchy--Schwarz across samples therefore gives (20), with one factor
\(1+\sqrt{\log(en)}\), rather than requiring its square. Together
with the cited signed stability estimate this is consistent with the
claimed \(n^{-16+o(1)}\) finite-horizon error. The global tail also
contains the separately bounded dense residual \(Y(en)^{-16}\).

## No future-source input and an honest initial branch

Equations (3)--(6) store only moments of the model's own current forward
activations and residual-weighted backward responses. The Legendre
polynomials and deterministic horizon are specified using the qualification
parameters. The dense-source Taylor and Chebyshev polynomials are proof
witnesses; neither their coefficients nor dense initialization jets are
arguments of the online update equations.

The Volterra formula (7)--(8) is causal: at time \(s+A\), it only
uses the trial path over \([s,s+A]\). Its contraction proof defines a
local solution, not an oracle giving future dense states. The factors of
\(A\) cancel the apparent zero-length division in the reconstructed
increment. Projection contraction in \(L^2([0,1])\) supplies a finite
local Lipschitz constant, and the prescribed limit of the normalized
moments selects the regular branch. Away from zero, differentiation
recovers the displayed finite-state moment ODE. This is adequate for the
exact mathematical construction, but is not a finite-step startup
algorithm or a globally locally-Lipschitz extension at arbitrary zero-clock
states. The candidate explicitly states both limitations.

At \(T\), freezing the moments, their denominator, and the first layer
while continuing the readout is a material, deterministic change to the
training rule. It needs no additional stored dense state. The proof uses
closeness at \(T\) to preserve a positive training-feature Gram gap, so
the readout-only tail fits and converges on the same eventual good event.
The tail also supplies the all-time comparison; finite-horizon estimates
alone would not have established that claim.

## Explicit order, storage, and qualifications

Writing \(u=\log(en)\), candidate (18) implies
\[
q\le1+16u+
512\beta^{30L}Y^2\left(\frac m\gamma\right)^2
\sqrt{d+3}\,u^{5/2}.
\]
This retains the displayed label, sample, gap, and input-dimension
dependence; the label cap is not needed to simplify it. The exact array
inventory is
\[
n(d+1)+2(L-1)mnq+1,
\]
including the arrays frozen after \(T\) and one clamped physical clock.
The single-interval implementation has no panel index, learned response
basis, extra history samples, or hidden dense parameter copy. Rank-one
products can evaluate the reconstruction directly. The stated absolute
constant in (24) is valid; for example, \(C=1024\) absorbs the above
ceiling, both moment families, and the clock for \(n\ge1\).

The retained fixed dense mixers still cost \((L-1)n^2\). Training
data, activation evaluators, and transient evaluation scratch are excluded
in the same way as in the paper's moving-state count and are explicitly
disclosed. The theorem does not imply subquadratic total memory, faster
training or querying, controlled numerical precision, or a practical
width threshold. Using \(\gamma\), \(Y\), and \(\beta\) in the
schedule is consistent with the stated qualification-parameter notion of
obliviousness; it is not independence from all training data.

The absolute \(Y/n\) conclusion is eventual for fixed \(Y>0\),
with all other problem parameters fixed separately. Its ratio to the
imported dense lower bound is at most a fixed-confidence multiple of
\(\log(en)^{5/2}/\sqrt{\gamma n}\), tending to zero. The source
event covers full forward vectors; the arbitrary-sphere output comparison
is supplied separately by parameter-to-output bounds. No unproved
analytic approximation of unseen-query histories is being substituted.

The optional numerical exponent (21) also has the advertised form under
the stated cap. Applying the paper's explicit signed-comparison constants
requires operators below nine and the specified readout bound. The fitting
proof provides a quantitative dense operator margin (in fact below
\(8+1/8\)); the vanishing stopped discrepancy preserves that margin.
For fixed positive \(Y\), it likewise eventually preserves the readout
margin. Thus this use is justified by the full fitting interface, not
merely by an unsupported claim that arbitrary perturbations preserve a
strict inequality.

## Recommended wording clarification

The early “Setup and conclusion” paragraph says that, for each fixed
problem, “the construction fits the labels, has limits, and eventually at
each fixed confidence satisfies” (2). Read literally, this could detach
fitting and existence from the eventual probability qualification. The
proof establishes these properties on the same sufficiently-wide good
event. A more precise sentence is:

> For each fixed admissible problem, eventually at each fixed confidence,
> the construction fits the labels, has limits, and satisfies (2).

The final section already presents its accuracy theorem with the correct
eventual qualification. This is a wording clarification, not a defect in
the final analytic or state-count argument.

No other corrective edits are requested within this review's scope.

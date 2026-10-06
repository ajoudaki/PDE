# Dense, Legendre and Harmonic models: integrated statements and proofs

<!-- method-names:start -->
The two methods are named **Legendre compression** and **Harmonic
compression**. Harmonic compression is the method called “compact” in
earlier proof and audit records; only its name has changed.
<!-- method-names:end -->

2026-10-06. This is the current integrated research document. It contains
the headline interfaces, the unsuppressed numerical statements, and the
proofs in one place. The only generic \(C\)'s occur in the explicitly
labelled headline layer. They are not definitions of the exact
certificates. The detailed layer gives finite formulas for every
deterministic error/storage coefficient and additional width gate.

An inherited quantitative limitation of the theorems is stated at
the outset: the stochastic sufficient-width threshold is existential,
not numerically evaluated. Restating the result cannot manufacture an
effective \(n(\delta)\). Each fixed confidence is reached at each
sufficiently large individual width. Nothing below claims simultaneous
success over infinitely many independently initialized widths.

**Navigation.**

- [I. Headline results](#headline-results): the canonical forward and inverse interfaces.
- [II. Detailed statements](#detailed-statements): exact coefficients, storage, qualifications and [computational costs](#computational-costs).
- [III. Proofs](#integrated-proofs): initialization, source estimates, dense comparison and variability, both compressions and [cost derivations](#computational-cost-proofs).
- [IV. Audit and provenance](#integrated-audit): checks, source versions and remaining limitations.

This is an internal research consolidation, not promotion to the maintained
book or paper. Its audit status and any unresolved objections are recorded
in Part IV; the word “integrated” alone is not an independent verification.

<a id="headline-results"></a>
## I. Headline results

### Shared setup, notation and qualifications

The structural parameters remain separate: dense width \(n\), sample count
\(m\), input dimension \(d\), and hidden depth \(L\ge2\). Inputs satisfy
\(\|x_a\|_2=\sqrt d\), and labels are arbitrary fixed real numbers.
The only compressed-model size/order symbol is \(q\): Legendre memory
order or Harmonic per-layer neuron budget. The remaining global numerical
symbols are label RMS \(Y\), feature gap \(\gamma\), activation envelope
\(\beta\), failure probability \(\delta\), target accuracy \(\varepsilon\),
and a generic numerical constant \(C\). Different occurrences of \(C\)
may denote different universal constants; they never conceal structural
dependence. The detailed statements and proofs use locally defined coefficients, not extra model orders.

The dense forward pass is
\[
z^{(1)}=Ax/\sqrt d,\qquad
z^{(j)}=W^{(j)}h^{(j-1)},\qquad h^{(j)}=\phi_j(z^{(j)}),
\qquad f_n=w^\top h^{(L)}/n.
\]
The first weights have independent \(N(0,1)\) entries; hidden mixers have
independent \(N(0,1/n)\) entries; blocks are independent; \(w(0)=0\).
Training minimizes mean squared loss with mobilities \((n,1,\ldots,1,n)\).
The dense copy \(\widetilde f_n\) is independently initialized. Compressed
predictors use their realized reference initialization and the same physical time.

Each activation is real on the real axis, holomorphic on a common strip
\(|\operatorname{Im}z|<a\), with bounded first derivative there. Activation
values may be unbounded. Set
\[
\beta=\max\left\{10,1+\max_j|\phi_j(0)|,\frac{16}{a},
\max_{j,\,k\in\{1,2\}}\sup_{|\operatorname{Im}z|\le a/2}
|\phi_j^{(k)}(z)|\right\},\qquad Y=\frac{\|y\|_2}{\sqrt m}.
\]
The covariance recursion and unweighted gap are
\[
Q^{(0)}_{ab}=x_a^\top x_b/d,\qquad
Q^{(j)}_{ab}=\mathbb E[\phi_j(Z_a)\phi_j(Z_b)],\quad
Z\sim N(0,Q^{(j-1)}),\qquad
\gamma=\lambda_{\min}(Q^{(L)})>0.
\]
The gap is not divided by \(m\). No orthogonality, centering, sign pattern,
clipping, or input-rank assumption is imposed.

**Labels.** The clean dense/Legendre envelopes below use the unchanged
sufficient cap
\[
0<Y\le\frac\gamma m\beta^{-30L}.
\tag{labels}
\]
The larger original recurrence allowance is retained explicitly at the
start of [Part II](#detailed-statements). The Harmonic forward theorem and its new beta-only storage envelope
hold on that entire larger range. Zero labels give the stationary zero
predictor and exact constant-zero compression separately.

**Error.** All comparisons use
\[
\|f-g\|_*=
\sup_{t\in[0,\infty]}\sup_{\|x\|_2=\sqrt d}|f(t,x)-g(t,x)|.
\tag{norm}
\]
This includes fitted limits and the whole sphere, a circle only when
\(d=2\). It measures function fidelity, not unknown-label test risk.

**Probability and width.** Fix \(0<\delta<1\). For each fixed admissible
problem there is a finite width threshold, depending on all its parameters
and \(\delta\), above which the stated comparisons hold jointly with
probability at least \(1-\delta\). It includes inherited source/initialization
gates, the lower theorem's eventual threshold when used, and the explicit
[analytic-tail and construction gates](#harmonic-storage-count). Its stochastic part
remains unquantified. This concerns each individual width, not one event
over infinitely many independent initializations. Split failure budgets
for joint statements. The same event works for every permitted order/budget
at that width; there is no additional tolerance-, horizon-, or order-dependent
stochastic threshold. Fixed-confidence logarithms in upper bounds are
absorbed by this eventual-width convention, not by a claimed numerical
failure-rate formula. Multiplying storage by a fixed constant is not
claimed to produce exponential confidence amplification.

**Model domains.** Legendre permits every integer \(q\ge1\), with no
separate accuracy-order condition. The Harmonic family permits every
integer budget \(q\ge18(2m+d+9)\), abbreviated \(q\ge C(m+d)\)
in the headline counts only. This is exact-initialization overhead:
positive training Gram forces top width at least \(m\), and exact
first-weight columns force first width at least \(d\) when \(n\ge d\).
For \(q\ge n\), the full selected space gives exact agreement with dense.

### Forward interface: supplied size/order gives storage and error

Storage counts real coordinates, not bits. The separate
[computational-cost section](#computational-costs) reports initialization,
per-stage training and single-query costs; storage alone is not a runtime bound.
For \(n\ge d\), the clean counts are:

| Model | Learned state | All retained model storage |
|---|---:|---:|
| Dense | \(O(Ln^2)\) | \(O(Ln^2)\) |
| Legendre | \(O(n[d+Lmq])\) | \(O(Ln^2+Lmnq)\) |
| Harmonic | \(O(Lq^2)\) | \(O(Lq^2)\) |

Before simplification, the exact dense moving count is
\((L-1)n^2+n(d+1)\), the Legendre count is
\(n(d+1)+1+2(L-1)mnq\), and Harmonic has at most
\((L-1)q^2+q(d+1)+m\). Legendre additionally retains
\((L-1)n^2\) fixed mixers; reconstructed matrices are evaluation objects.
Harmonic includes metrics, fixed copies, residual coordinates, data and
solve caches. Original-width source arrays and jets are discarded.
Ordinary data storage is additional for the dense/Legendre model-state
counts if retained.

Legendre uses its original residual-RMS clock and prefixes. Harmonic uses
the corrected-readout autonomous optimizer, not ordinary gradient flow
on an arbitrary smaller network. All hidden arrays train. Neither has
a second independent runtime approximation order.

#### Dense versus an independent dense copy

A simplified polynomial upper envelope is
\[
\|f_n-\widetilde f_n\|_*
\le C\beta^{CL}Y\left(1+\frac m\gamma\right)^5
\sqrt{\frac dn}\,\log(en)e^{\sqrt{\log(en)}}.
\tag{dense upper}
\]
The exact, sharper actual-label coefficient and confidence logarithm
remain in [the exact dense certificate](#dense-forward-comparison).
The sample/gap powers in this upper envelope are not claimed sharp.

For \(m\ge2\),
\[
\|f_n-\widetilde f_n\|_*
\ge c_{\phi,L,\delta}\frac{Y\sqrt\gamma}
{\sqrt n\,\log(en)^{5/2}}.
\tag{dense lower}
\]
The positive coefficient depends only on activations, depth and confidence;
its formula is in [the exact lower theorem](#dense-trajectory-lower).
It cannot be replaced by a confidence-independent universal constant.
The actual-prediction witness occurs at a positive early time, possibly
shrinking with width; this is not an endpoint lower bound. Deterministic
exceptions prevent the general assertion at \(m=1\).

#### Legendre versus its realized dense reference

For every integer \(q\ge1\),
\[
\|f_{\mathrm{Leg},n,q}-f_n\|_*
\le C\beta^{CL}Y\left(1+\frac m\gamma\right)^6
\frac{\sqrt{\log(en)\log(eq)}}{q^2}
e^{\sqrt{\log(en)}}.
\tag{Legendre forward}
\]
The stronger exact actual-label coefficient is unchanged:
[the exact all-order statement](#legendre-forward-certificates).
Above the actual absorption threshold use the signed comparison;
below it use the all-order fitting/predictor bound. Retaining the small
label powers shows that the same coefficient covers both regions.
No second error term or accuracy-order gate is needed on the explicit cap.

#### Harmonic versus its realized dense reference

For every Harmonic budget in the shared model domain,
\[
\begin{split}
\|f_{\mathrm{Harm},n,q}-f_n\|_*
\le{}&C\beta^{CL}Y\frac m\gamma
\left(1+\sqrt{\frac m\gamma}\right)n e^{C\sqrt{\log(en)}}\\
&\times\exp\left[-\frac{\sqrt d}{C\beta^{CL}}
\left(\frac{q}{(Ym/\gamma)^2\log(en)^{d/2}}\right)^{1/(d+1)}\right].
\end{split}
\tag{Harmonic forward}
\]
This is a genuine decreasing certificate in supplied \(q\). The construction
takes \(n,q\) as inputs; its internal source tolerance and horizon are
determined by the budget and discarded after setup. There is no fixed
error floor. For \(q\ge n\), exact retention improves the bound to zero.
The growing comparison exponential has only numerical coefficient \(C\);
structural factors in the negative exponential specify approximation
efficiency, not unstable amplification.

The power \(1/(d+1)\) comes from approximating the sphere and a horizon
that grows with required accuracy. It is a construction rate, not an
optimality lower bound. An initialization-only selected model covers
smaller budgets within the shared domain using independent fitting;
there is no hidden extra accuracy-dependent budget test.

The original construction at source tolerance \(1/n\) remains valid with
its sharper error
\(C\beta^{CL}Y(m/\gamma)(1+\sqrt{m/\gamma})
n^{-1}e^{C\sqrt{\log(en)}}\)
and original \(O(\log(en)^{3d+2})\) all-retained storage.
The supplied-budget family preserves that specialization as a separate available construction.

### Inverse interface: supplied accuracy determines size/order

The common target is
\[
\mathbb P\{\|f_{\rm model}-f_n\|_*\le\varepsilon\}\ge1-\delta.
\tag{target}
\]
For each certificate choose the smallest permitted integer size/order
whose right side is at most \(\varepsilon\), with the common width gates enforced. This minimizes the increasing
storage-budget bound within that certificate, not compression among all
possible models. Exact scalar inversions, including loose targets and
the full-width fallback, are in Part II.

The following simpler prescriptions describe polynomial accuracy
\(\varepsilon=n^{-\Theta(1)}\), with structural parameters and confidence
fixed and \(n\) sufficiently large: the accuracy may lie between two
different fixed negative powers of \(n\), not necessarily \(1/n\).
This does not identify or order \(m,d,L,1/\gamma\).
The common eventual convention absorbs fixed coefficients inside logarithms.
For the user's large-parameter simplification use \(m/\gamma\ge1\);
otherwise replace that ratio by \(1+m/\gamma\) in the dense/Legendre
prescriptions.

#### Dense: choose width before initialization

A sufficient eventual choice is
\[
n=\left\lceil
\frac{C\beta^{CL}Y^2d}{\varepsilon^2}
\left(1+\frac m\gamma\right)^{10}
\log(e/\varepsilon)^2
e^{C\sqrt{\log(e/\varepsilon)}}\right\rceil,
\qquad \text{storage}=O(Ln^2).
\tag{dense inverse}
\]
Its all-retained model storage has the explicit sufficient envelope
\[
\operatorname{storage}(\widetilde f_n)\le
CL\beta^{CL}Y^4d^2\left(1+\frac m\gamma\right)^{20}
\varepsilon^{-4}\log(e/\varepsilon)^4
e^{C\sqrt{\log(e/\varepsilon)}}.
\tag{dense inverse storage}
\]
This is eventual as \(\varepsilon\downarrow0\): the selected width must
exceed the common threshold. It is not a fully effective confidence-certified
width, because the stochastic source threshold is unquantified. It selects
a reference before initialization, not a replacement for an already
prescribed reference.

#### Legendre: choose order for the given reference

The inverse of the forward bound has sufficient eventual form
\[
q=\left\lceil C\beta^{CL}\left(\frac m\gamma\right)^3
\sqrt{\frac Y\varepsilon}\,
[\log(en)\log(en/\varepsilon)]^{1/4}
e^{\frac12\sqrt{\log(en)}}\right\rceil.
\tag{Legendre inverse}
\]
Consequently
\[
\text{learned storage}\le Cnd+
C\beta^{CL}Lmn\left(\frac m\gamma\right)^3
\sqrt{\frac Y\varepsilon}\,
[\log(en)\log(en/\varepsilon)]^{1/4}
e^{\frac12\sqrt{\log(en)}}.
\tag{Legendre inverse storage}
\]
Fixed mixers remain additional. There is no separate order-admissibility
test even before taking this eventual simplification.
Keeping the two logarithms also keeps the coefficient uniform in the
fixed polynomial accuracy exponent; replacing them by \(\log(en)^2\)
would hide a constant depending on that exponent.

#### Harmonic: choose width budget for the given reference

Inverting its stretched-exponential certificate gives
\[
q=\left\lceil C(m+d)+
\frac{\beta^{C(d+1)L}}{d^{(d+1)/2}}
\left(\frac{Ym}{\gamma}\right)^2
\log(en)^{d/2}\log(en/\varepsilon)^{d+1}\right\rceil.
\tag{Harmonic inverse}
\]
The corresponding all-retained bound, hence also the learned-state bound, is
\[
\operatorname{storage}(f_{\mathrm{Harm},n,q})
\le CL(m+d)^2+
\frac{L\beta^{C(d+1)L}}{d^{d+1}}
\left(\frac{Ym}{\gamma}\right)^4
\log(en)^d\log(en/\varepsilon)^{2d+2}.
\tag{Harmonic inverse storage}
\]
There is no factorial ratio: Stirling bounds
\((d+3)^d/(d!)^2\) by \(C^{d+1}/d^{d+1}\), and numerical powers are
absorbed in the displayed activation-depth envelope.
At polynomial accuracy this is \(O(\log(en)^{3d+2})\) for fixed structural
parameters, preserving the previous qualitative storage order.

For an arbitrary target outside that regime, keep the unshortened
logarithm from the forward certificate: replace
\(\log(en/\varepsilon)\) in the sufficient budget by
\[
\log(en)+\log\left(e+
\frac{C\beta^{CL}Y(m/\gamma)(1+\sqrt{m/\gamma})}{\varepsilon}\right).
\tag{Harmonic inverse logarithm}
\]
Enlarging numerical constants absorbs \(\sqrt{\log(en)}\).
If the sufficient budget exceeds \(n\), the exact full-width branch
suffices instead. The exact inverse in the proof also handles targets
already met by the initialization-only model. These are internal choices
of one width budget, not extra runtime orders.

<a id="cost-inverse-interface"></a>
#### Costs at the prescribed inverse widths/orders

In the next table, \(n\) and \(q\) mean the corresponding prescribed
inverse choices above (or their exact Part II versions), not new
optimized quantities. Write \(P=(L-1)n^2+n(d+1)\) only as a
cost-count abbreviation. The explicit Harmonic warmup envelopes
\(\mathcal T_{\rm H},\mathcal M_{\rm H}\) are defined in
[Part II](#harmonic-warmup-cost); evaluate them at that \(n,q\)
and at supplied, accuracy-certified \(K,p,J,N_x,N_t\).
No choice of those internal resolutions, or efficient bound on them,
is inferred merely from the inverse choice of \(q\).

The table counts classical arithmetic, with scalar activation work
and Gaussian sampling charged as specified in the
[cost contract](#computational-costs). Training is one full-batch
vector-field stage, or one fixed-stage explicit step up to its fixed
stage multiplier. Warmup/training memory is total peak resident
memory; query memory is additional peak workspace for an already
loaded, inference-ready model.

| Model and operation | Arithmetic work after the indicated inverse substitution | Peak memory |
|---|---:|---:|
| Dense warmup | \(O(P)\), plus Gaussian draws | \(O(P+m(d+1))\) |
| Dense training stage | \(O(mP)\) | \(O(P+Lmn+m(d+1))\) |
| Dense query | \(O(P)\) | \(O(n)\) additional |
| Legendre warmup | \(O(mP+Lmnq)\), plus Gaussian draws | \(O(P+Lmnq+m(d+1))\) |
| Legendre training stage | \(O(mP+Lnm^2q+Lnmq)\) | \(O(P+Lnmq+m(d+1))\) |
| Legendre query | \(O(P+Lnmq)\) | \(O(n)\) additional |
| Harmonic warmup | \(O(\mathcal T_{\rm H})\), plus Gaussian draws | \(O(\mathcal M_{\rm H})\) |
| Harmonic training stage | \(O(Lmq^2+m^3)\) | \(O(Lq^2)\) |
| Harmonic query | \(O(Lq^2)\) | \(O(q)\) additional |

The full-width exact fallback uses the dense row. Legendre rows use
streamed correction factors and cumulative moment prefixes. Harmonic
rows use fixed metric inverse caches, the necessary moving
feature-Gram solve and a refreshed effective-readout cache. Cache
refresh is charged to training/model preparation, not hidden in the
single-query bound. These are sufficient implementation costs, not
time-optimal algorithms or numerical-step accuracy guarantees.

<a id="main-compression-consequences"></a>
### Common accuracy-to-storage and computational-cost corollary

Fix data, activations, \(m,d,L,Y,\gamma\), and confidence. Choose the dense
reference before initialization to meet its own target:
\(n(\varepsilon)=\varepsilon^{-2+o(1)}\) suffices.
Apply the two inverse orders at this same reference width:

| Model | Learned storage at error \(\varepsilon\) | All retained model storage |
|---|---:|---:|
| Independent dense | \(\varepsilon^{-4+o(1)}\) | \(\varepsilon^{-4+o(1)}\) |
| Legendre | \(\varepsilon^{-5/2+o(1)}\) | \(\varepsilon^{-4+o(1)}\), including fixed mixers |
| Harmonic | \(O(\log(1/\varepsilon)^{3d+2})\) | \(O(\log(1/\varepsilon)^{3d+2})\) |

These powers do not suppress growing structural parameters in the explicit
bounds above. They are sufficient counts, not minimax storage lower bounds
or a growing-data theorem. For comparison against an independent dense run,
split accuracy and failure budgets between dense variability and compression;
the triangle inequality gives the same exponents without event independence.

<a id="cost-common-consequences"></a>
At these same choices, the cost comparison is:

| Model and operation | Work | Peak memory |
|---|---:|---:|
| Dense warmup | \(\varepsilon^{-4+o(1)}\) | \(\varepsilon^{-4+o(1)}\) |
| Dense training stage | \(\varepsilon^{-4+o(1)}\) | \(\varepsilon^{-4+o(1)}\) |
| Dense query | \(\varepsilon^{-4+o(1)}\) | \(\varepsilon^{-2+o(1)}\) additional |
| Legendre warmup | \(\varepsilon^{-4+o(1)}\) | \(\varepsilon^{-4+o(1)}\) |
| Legendre training stage | \(\varepsilon^{-4+o(1)}\) | \(\varepsilon^{-4+o(1)}\) |
| Legendre query | \(\varepsilon^{-4+o(1)}\) | \(\varepsilon^{-2+o(1)}\) additional |
| Harmonic warmup | \(O(\mathcal T_{\rm H})\), with all setup orders retained | \(O(\mathcal M_{\rm H})\), with all setup orders retained |
| Harmonic training stage | \(O(\log(1/\varepsilon)^{3d+2})\) | \(O(\log(1/\varepsilon)^{3d+2})\) |
| Harmonic query | \(O(\log(1/\varepsilon)^{3d+2})\) | \(O(\log(1/\varepsilon)^{3d/2+1})\) additional |

Here the warmup envelopes are evaluated at
\(n=\varepsilon^{-2+o(1)}\) and the Harmonic inverse width
\(q=O(\log(1/\varepsilon)^{3d/2+1})\), with its other setup
resolutions still explicit. No epsilon-only warmup rate has been
established. In the stated resident-dense implementation, warmup
already holds \(P=\varepsilon^{-4+o(1)}\) dense coordinates;
it is not polylogarithmic merely because the retained model is.
All asymptotic rows fix the dataset, depth, dimension, activations
and confidence and use unit-cost scalar evaluation/sampling.
The more general arithmetic-plus-oracle-call qualification is in
Part II. There is no bound here on numerical precision or the number
of training steps. Legendre's smaller learned state does not eliminate
its fixed dense-mixer work; Harmonic's small runtime state does not
bound the cost of constructing it.

For \(m\ge2\) and nonzero labels, canonical independent-dense accuracy
with fixed failure probability below one half requires, eventually,
\[
n\log(en)^5\gtrsim_{\phi,L,\delta}\frac{Y^2\gamma}{\varepsilon^2}.
\]
Thus its parameter count is
\(\Omega(\varepsilon^{-4}/\log(1/\varepsilon)^{10})\) at fixed problem.
This is not a lower bound against arbitrary compressed representations.

### Width scaling and actual dense variability

At root-width target \(\varepsilon=Y/\sqrt n\), Legendre has order
\(n^{1/4+o(1)}\), moving state \(n^{5/4+o(1)}\), and quadratic fixed
mixers. Harmonic has width \(O(\log(en)^{3d/2+1})\) and all-retained
storage \(O(\log(en)^{3d+2})\).
At fixed positive error, Legendre moving storage is instead \(n^{1+o(1)}\).

Harmonic can target \(n^{-1}\), or use its original \(n^{-1+o(1)}\)
specialization, with the same polylogarithmic storage order.
For Legendre, enlarge the root-target order by \(\log(en)^{3/2}\);
its error is then at most \(CY/[\sqrt n\log(en)^3]\) eventually,
without changing the moving-state exponent. For \(m\ge2\), the general
dense lower bound gives for these choices
\[
\frac{\|f_{\rm model}-f_n\|_*}
{\|f_n-\widetilde f_n\|_*}\xrightarrow{\mathbb P}0.
\]
This compares complete trajectory norms, not endpoint errors or
pointwise-in-time ratios. Confidence dependence of the lower coefficient
is retained in this probability argument.



<a id="detailed-statements"></a>
## II. Detailed statements: exact certificates and qualified computational costs

The global quantities are exactly those defined in Part I. The error
and storage formulas in this part, rather than any choice of a headline
constant, are the numerical certificates. Finite recurrence coefficients
are defined locally where they are used; none is an independently
adjustable parameter. The separate cost subsection exposes internal
setup resolutions and qualifies its arithmetic big-O bounds explicitly;
it is not an exact floating-point operation or bit-complexity certificate.
The same physical-time model and the same whole-sphere, all-time norm
apply throughout. Where a proof writes \(v=x/\sqrt d\), its unit-sphere
supremum is exactly the original input-sphere supremum.

### One common label allowance

The complete original allowance is
\[
0<Y\le\frac\gamma m\min\left\{
\frac1{8H_D\sqrt{F_D}},\quad\frac{S_*^{\rm Leg}}8,\quad
\frac1{16H_c\sqrt{F_c}},\quad\frac{S_*^{\rm src}}{16}
\right\}.
\tag{common-exact-labels}
\]
The four entries are fully defined in this document:

| Entry | Exact definitions and proof |
|---|---|
| Dense fitting, \(H_D,F_D\) | [Dense fitting coefficients](#dense-fitting) |
| Every-order Legendre fitting, \(S_*^{\rm Leg}\) | [Legendre coefficients](#legendre-labels) |
| Corrected Harmonic fitting, \(H_c,F_c\) | [Harmonic fitting coefficients](#harmonic-fitting-coefficients) |
| Analytic source control, \(S_*^{\rm src}\) | [Source recurrences](#source-explicit-recurrences) |

The common sufficient specialization is exactly
\(0<Y\le(\gamma/m)\beta^{-30L}\). Its implication of all four
entries is proved in the numerical coefficient ledgers, not assumed.
The simpler dense/Legendre activation-power certificates use this smaller
cap. Their full recurrence certificates retain the entire displayed
interval. Harmonic's explicit full-range certificate and supplied-budget
theorem use the entire interval. No target-dependent label assumption is
introduced. If \(Y=0\), all three predictors stay identically zero;
the positive-label formulas are replaced by that exact stationary case.

### One width and confidence convention

Each detailed statement is written at its individual confidence input
\(0<\delta<1\). For a joint assertion of dense upper, dense lower,
Legendre and Harmonic, use confidence input \(\delta/4\) in each
statement, and take a width satisfying the union of their stated gates.
The union bound gives joint success at least \(1-\delta\), without
independence between compressed constructions. The lower assertion is
included only for \(m\ge2\) and \(Y>0\). A conservative common
explicit initialization requirement is
\(n\ge N_{\rm fit}(\delta/32)\), whose numerical formula appears
below. Also take \(n\ge d\) for the simplified storage counts.

The remaining common gates have exactly these origins:

1. The source's high-probability finite-deletion/moment event, proved in
   [source foundations](#source-foundations). Its sufficient width is
   existential and depends on the fixed problem and confidence.
2. The explicit source complex-radius and counting inequalities and
   [the analytic-tail gates](#harmonic-storage-count), including the
   dimension-one temporal count. These are finite formulas independent
   of the supplied model budget and requested tolerance.
3. When the lower bound is included, the eventual initialized-CLT and
   derivative-to-prediction thresholds in [the lower theorem](#dense-trajectory-lower).

These finitely many eventual conditions have a common finite threshold
for every fixed admissible problem and confidence. This assertion does
not give a numerical value for its stochastic portion, or prove that
the threshold is polynomial in sample count, gap or depth. The exact
deterministic gates are listed and derived below; none is silently put
inside an error constant. At a width satisfying these gates, the same
event covers every permitted Legendre order and Harmonic budget. The
arbitrary-accuracy Harmonic construction introduces no extra stochastic
event depending on its internal horizon or source tolerance.

When \(\varepsilon,\delta\) are inputs to an inverse statement,
its numerical order or storage prescription is effective **conditional
on the reference width satisfying this convention**. The dense inverse
must likewise meet the implicit source threshold. The eventual
\(\varepsilon\downarrow0\) powers in Part I do not quantify it.

### Construction domains and what storage means

Legendre order is every integer \(q\ge1\). The Harmonic construction
below covers every integer \(q\ge18(2m+d+9)\); its baseline is
exact-initialization overhead, not an error floor. Full-coordinate
selection at \(q\ge n\) agrees exactly with dense. In eventual
statements one may include \(n\ge18(2m+d+9)\) in the common width
threshold so these domains overlap directly. At smaller widths the
full-coordinate branch still exists but is not a compression claim.

All storage counts are numbers of real coordinates. For dense and
Legendre, state counts are distinguished from data and evaluation
working memory. For Harmonic, the stated all-retained bound also includes
fixed metrics/copies, data and prescribed solve caches. Setup jets and
original-width arrays are discarded after construction. The separate
[cost analysis](#computational-costs) supplies arithmetic and peak-memory
implementation bounds, not bit complexity or storage optimality over all
possible representations. “Least certified order”
means the least integer satisfying the particular displayed sufficient
error bound; it is not an observed or minimax optimum.

<a id="dense-model-and-certificates"></a>
### Dense model, scope, and numerical certificates

This section uses width \(n\), sample count \(m\), input dimension \(d\),
and hidden depth \(L\ge2\). Set \(v_a=x_a/\sqrt d\), so that
\(\|v_a\|_2=1\), and keep the labels \(y_a\) unchanged. The network is
\[
z^{(1)}(v)=Av,\qquad
z^{(j)}(v)=W^{(j)}h^{(j-1)}(v),\qquad
h^{(j)}(v)=\phi_j(z^{(j)}(v)),\qquad
f_n(v)=\frac{w^Th^{(L)}(v)}n.
\]
Here \(A\) is \(n\times d\), the \(L-1\) hidden mixers are
\(n\times n\), and \(w\in\mathbb R^n\). Initial entries of \(A\) are
independent \(N(0,1)\); mixer entries are independent \(N(0,1/n)\);
all blocks are independent; and \(w(0)=0\). The loss is
\(m^{-1}\sum_a r_a^2\), where \(r_a=f_n(v_a)-y_a\), with mobilities
\((n,1,\ldots,1,n)\). Define
\[
k_a^{(L)}=w,\qquad
\delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot k_a^{(j)},\qquad
k_a^{(j)}=(W^{(j+1)})^T\delta_a^{(j+1)}.
\]
The resulting physical-time flow is exactly
\[
\dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^T,\qquad
\dot W^{(j)}=-\frac2{mn}\sum_a r_a\delta_a^{(j)}(h_a^{(j-1)})^T,
\qquad \dot w=-\frac2m\sum_a r_ah_a^{(L)}.
\]
Every hidden array trains. The two independent dense runs use these same
labels and the same physical time.

Activations are real on the real line and holomorphic on the common strip
\(|\operatorname{Im}z|<a\), with bounded first derivative on that strip.
Values need not be bounded. Write
\[
b=\max_j|\phi_j(0)|,\quad
s=\max\left\{1,\max_j\sup_{|\operatorname{Im}z|\le a/2}|\phi_j'(z)|\right\},
\quad t_2=\max_j\sup_{|\operatorname{Im}z|\le a/2}|\phi_j''(z)|,
\]
\[
\beta=\max\{10,1+b,16/a,s,t_2\},\qquad
Y=\|y\|_2/\sqrt m.
\]
Cauchy's integral formula applied to the full-strip first derivative
bounds the higher derivatives on every smaller strip. Thus these
quantities are finite. In particular \(|\phi_j(z)|\le b+s|z|\) on
the half-strip, by integrating the first derivative along the segment
from zero to \(z\).

The initial population covariance and unweighted gap are
\[
Q^{(0)}_{ab}=v_a^Tv_b,\qquad
Q^{(j)}_{ab}=\mathbb E[\phi_j(Z_a)\phi_j(Z_b)],\quad
Z\sim N(0,Q^{(j-1)}),\qquad
\gamma=\lambda_{\min}(Q^{(L)})>0.
\]
There is no orthogonality, centering, sign, input-rank, or intermediate
covariance nonsingularity assumption. The proof abbreviation
\(\lambda=\gamma/m\) is the normalized gap; it is not a redefinition
of the global \(\gamma\). For a standard real Gaussian \(G\), define
\[
\mu_{2,0}=1,\qquad
\mu_{2,j}=\mathbb E\phi_j(\sqrt{\mu_{2,j-1}}G)^2,\qquad
H_D=\max(1,\sqrt{\mu_{2,1}},\ldots,\sqrt{\mu_{2,L}}).
\]
These are the scalar moments called \(q_j\) in the component notes;
the notation here keeps \(q\) available for a compressed model's order.
Equal input norms imply \(Q^{(j)}_{aa}=\mu_{2,j}\). Consequently
\(\lambda\le H_D^2/m\le H_D^2\).

The dense comparisons concern the single norm
\[
\|f-g\|_*=
\sup_{t\in[0,\infty]}\sup_{\|x\|_2=\sqrt d}|f(t,x)-g(t,x)|.
\]
The extra point \(t=\infty\) denotes the fitted limit constructed
below. An upper bound in this norm also bounds endpoints; the lower
bound below has a positive-time witness and makes no endpoint claim.

The exact number of dense parameter coordinates per run is
\[
S_D(n)=(L-1)n^2+n(d+1).
\]
All these coordinates are learned and retained. This counts real
coordinates, not bits or preprocessing work. If data are retained,
their ordinary \(m(d+1)\) coordinates are additional. Two independent
runs require twice the per-run model storage.

<a id="dense-fitting"></a>
### Quantitative initialization and all-time dense fitting

Define the finite activation/depth coefficients
\[
D_j^D=s(9s)^{L-j},\qquad U_1^D=D_1^D,\qquad
U_j^D=2H_DD_j^D\quad(j\ge2),
\]
\[
F_1^D=sU_1^D,\qquad
F_j^D=s(2H_DU_j^D+9F_{j-1}^D),\qquad F_D=F_L^D.
\]
Unrolling the last recurrence gives the exact expression
\[
F_D=s^2\left[(9s)^{2L-2}
       +4H_D^2\sum_{j=0}^{L-2}(9s)^{2j}\right].
\]
All coefficients are positive, and
\(F_D\ge\max(1,U_1^D,\ldots,U_L^D,F_1^D,\ldots,F_L^D)\).

For a confidence argument \(0<\alpha<1\), set
\[
A_D=s^2+t_2(b+\sqrt2sH_D),\quad
T_D=\sum_{j=0}^{L-1}A_D^j,\quad
e_D=\min\{1/4,\gamma/(2m)\},\quad
M_D=8b^4+96s^4H_D^4,
\]
\[
h_D=\min\{1/2,H_D/[4(8s)^L]\},\qquad P_D=(1+2/h_D)^d,
\]
\[
N_{\rm fit}(\alpha)=\left\lceil\max\left\{
1,\frac{\log(8L/\alpha)}{8-2\log9},
\frac{d\log9+\log(8/\alpha)}{8-\log9},
\frac{2L(m^2+P_D)M_DT_D^2}{\alpha e_D^2}
\right\}\right\rceil.
\]
The denominators are positive. At every \(n\ge N_{\rm fit}(\alpha)\),
with probability at least \(1-\alpha\),
\[
\|A_0\|_{\rm op}/\sqrt n\le8,\qquad
\max_{j\ge2}\|W_0^{(j)}\|_{\rm op}\le8,\qquad
\sup_{\|v\|_2=1,j}\|h_0^{(j)}(v)\|_2/\sqrt n\le3H_D/2,
\]
\[
\lambda_{\min}\!\left(\frac{\mathsf H_0^T\mathsf H_0}{mn}\right)
\ge\lambda/2,\qquad
\mathsf H_0=[h_0^{(L)}(v_1),\ldots,h_0^{(L)}(v_m)].
\]
On this initialization event, the sole real-fitting label restriction is
\[
0<Y\le\frac{\lambda}{8H_D\sqrt{F_D}}.
\]
Under it the flow exists for all time, every parameter converges, and
every training label is fitted. Simultaneously for all \(t\ge0\),
\[
\|A(t)\|_{\rm op}/\sqrt n<9,\quad
\max_{j\ge2}\|W^{(j)}(t)\|_{\rm op}<9,\quad
\sup_{\|v\|_2=1,j}\|h^{(j)}(t,v)\|_2/\sqrt n<2H_D,
\]
\[
\lambda_{\min}\!\left(\frac{\mathsf H(t)^T\mathsf H(t)}{mn}\right)
\ge\lambda/4,\qquad
\rho(t):=\|r(t)\|_2/\sqrt m\le Ye^{-\lambda t/2},\qquad
\int_0^\infty\rho(t)\,dt\le2Y/\lambda.
\]
In the parameter norm
\[
\|\theta\|_{\rm par}^2=
\|A\|_F^2/n+\sum_{j=2}^L\|W^{(j)}\|_F^2+\|w\|_2^2/n,
\]
the path length and displacements satisfy
\[
\int_0^\infty\|\dot\theta\|_{\rm par}\,dt\le2Y/\sqrt\lambda,
\qquad \|w(t)\|_2/\sqrt n\le2Y/\sqrt\lambda,
\]
\[
\frac{\|A(t)-A_0\|_F}{\sqrt n}\le\frac{8U_1^DY^2}{\lambda^{3/2}},
\qquad
\|W^{(j)}(t)-W_0^{(j)}\|_F\le\frac{8U_j^DY^2}{\lambda^{3/2}},
\]
\[
\sup_{\|v\|_2=1}
\frac{\|h^{(j)}(t,v)-h_0^{(j)}(v)\|_2}{\sqrt n}
\le\frac{8F_j^DY^2}{\lambda^{3/2}}.
\]
The uniform endpoint tail is
\[
\sup_{\|v\|_2=1}|f_n(\infty,v)-f_n(t,v)|
\le16\left(H_D^2+\frac{F_DY^2}{\lambda}\right)
\frac Y\lambda e^{-\lambda t/2}
\le\frac{65}{4}H_D^2\frac Y\lambda e^{-\lambda t/2}.
\]
For \(Y=0\), all velocities vanish at initialization and the predictor
remains identically zero. No division by \(Y\) is used in that case.

<a id="dense-forward-comparison"></a>
### Explicit independent-dense upper certificates

The [source foundation](#source-foundations) supplies activation/depth
constants \(S_*^{\rm src},K_{\rm src}>0\) and an eventual probability
event for the actual trained carriers. The full dense allowance is
\[
0<Y\le\lambda\min\left\{
\frac1{8H_D\sqrt{F_D}},\frac{S_*^{\rm src}}{16}\right\}.
\]
When dense is compared jointly with compressed models, intersect this
allowance with their stated fitting allowances. This intersection is the
full common recurrence scope; none of the arguments here shrinks it to
the beta-only cap below.

Put \(S=16Y/\lambda\), \(\kappa=\lambda/2\),
\(R=2Y/\sqrt\lambda\), and \(u_n=\sqrt{\log(en)}\).
The source event, including its deterministic post-horizon tail, gives
\[
\max_{a,j,i,t\ge0}|k_{a,i}^{(j)}(t)|\le M_n,
\qquad M_n=2K_{\rm src}S u_n.
\]
The factor two supplies the all-time tail margin. This bound concerns
training carriers; no carrier maximum on an interpolating parameter
state or on every passive query is assumed.

Define the following local comparison coefficients:
\[
T=9s,\quad F_z=2H_DT^{L-1},\quad B_\delta=sT^{L-1}R,
\quad P=1+2H_D(L-1),\quad G_*=PB_\delta+2H_D,
\]
\[
D_\delta(M)=sT^{L-1}(1+B_\delta)+Lt_2F_zT^{L-1}M,
\]
\[
J(M)=P D_\delta(M)+[1+(L-1)B_\delta]sF_z,
\]
\[
T_{\mathrm{rem}}(M)=sF_z\sqrt L+LB_\delta sF_z+\tfrac12L^2t_2F_z^2M,
\]
\[
E_{\mathrm{en}}(M)=2[2T_{\mathrm{rem}}(M)+\sqrt{L+1}J(M)]Y/\kappa,
\]
\[
C_Y(M)=\frac{2H_D}{\kappa}
\left(\frac{16H_DG_*J(M)}{\kappa}+2sF_z\right)
+\frac{2sF_z}{\sqrt\lambda},
\qquad
\mathcal L_n=\frac{\sqrt{L+1}YC_Y(M_n)}{\sqrt n}e^{E_{\mathrm{en}}(M_n)},
\]
\[
K_t=\frac{8(H_D^2+F_DY^2/\lambda)Y}{\kappa},\qquad
K_x=RT^L,\qquad N_n=(n+1)(1+2n)^d.
\]
For each fixed \(0<\delta<1\), the full-range certificate is
\[
\|f_n-\widetilde f_n\|_*
\le E_D(n,\delta):=
2\mathcal L_n\sqrt{\log(4N_n/\delta)}+
\frac{2(K_t+K_x)}n.
\]
It holds with probability at least \(1-\delta\) once
\(n\ge N_{\rm fit}(\delta/8)\) and the source failure, including
its all-time tail gate, is at most \(\delta/8\) for each path.
The latter sufficient width is not quantified. All coefficients in
the displayed deterministic bound are finite recurrences; the unknown
width must not be interpreted as an explicit confidence-certified
initialization rule.

For completeness, the original full-range unsigned comparison is also
retained. It gives the same certificate with \(\mathcal L_n\) replaced by
\[
\mathcal L_n^{\rm old}=
\frac{(2H_D+RsF_z)\sqrt L}{\sqrt n}
\exp\left\{2J(M_n)(1+4G_*^2/\kappa)Y/\kappa\right\}.
\]
The signed-energy proof below also applies on the full recurrence range
and retains an explicit factor \(Y\) in the newer prefactor.

On the unchanged simpler sufficient cap
\[
0<Y\le\frac\gamma m\beta^{-30L},
\]
let \(B_D=\beta^{100L}\). A shorter fully numerical upper bound is
\[
\begin{split}
\|f_n-\widetilde f_n\|_*\le{}&
B_DY\left(1+\frac m\gamma\right)^2
\left[1+B_D\frac{Ym}{\gamma}\sqrt{\log(en)}\right]\\
&\times\left[1+B_D\left(\frac{Ym}{\gamma}\right)^2
\left(e^{\sqrt{\log(en)}}-1\right)\right]
\sqrt{\frac{\log[8(n+1)(1+2n)^d/\delta]}n}.
\end{split}
\]
This keeps the actual label amplitude in every bracket. It is an
\(n^{-1/2+o(1)}\) upper bound at fixed problem parameters, not a
constant-times-\(n^{-1/2}\) theorem. The source probability qualification
is exactly the same as for the full-range certificate.

<a id="dense-inverse-storage"></a>
### Accuracy inversion and dense storage

For the full recurrence certificate, the exact scalar prescription is the
smallest integer \(n\) meeting its fitting/source width requirements and
\(E_D(n,\delta)\le\varepsilon\). Its storage is exactly
\((L-1)n^2+n(d+1)\). The source threshold remains a specified
unquantified requirement, so this prescription is not a fully effective
confidence-certified width algorithm.
The admissible set is nonempty: at fixed problem parameters \(M_n\)
is proportional to \(\sqrt{\log(en)}\), the coefficients \(J,C_Y\)
are affine in \(M_n\), and \(E_{\mathrm{en}}\) is affine in \(M_n\).
Thus \(E_D(n,\delta)=n^{-1/2+o(1)}\to0\).

Here is an explicit inversion of the simpler cap's numerical expression,
separate from that stochastic qualification. Put
\[
D_{d,\delta}=d+1+\log(16\,3^d/\delta),\qquad
A_{D,\delta}=B_DY(1+m/\gamma)^2
(1+B_DYm/\gamma)(1+B_D(Ym/\gamma)^2)\sqrt{D_{d,\delta}}.
\]
For every \(n\ge1\), the beta certificate is at most
\[
A_{D,\delta}\frac{\log(en)e^{\sqrt{\log(en)}}}{\sqrt n}.
\]
For \(Y>0\), define
\[
a_\varepsilon=\max\{1,A_{D,\delta}/\varepsilon\},\qquad
v_\varepsilon=\log(e+a_\varepsilon),\qquad
\bar n_\varepsilon=
\left\lceil a_\varepsilon^2v_\varepsilon^2
e^{8\sqrt{v_\varepsilon}+16}\right\rceil.
\]
Every \(n\ge\bar n_\varepsilon\) makes the preceding envelope at
most \(\varepsilon\). Thus one may take the maximum of \(\bar n_\varepsilon\),
\(N_{\rm fit}(\delta/8)\), and the same eventual source threshold.
At fixed nonzero labels and fixed problem parameters this gives
\(n=\varepsilon^{-2+o(1)}\) and dense storage
\(\varepsilon^{-4+o(1)}\) as \(\varepsilon\downarrow0\).
These are sufficient parameter counts for choosing the reference before
initialization; they do not replace an already prescribed dense reference.

<a id="dense-initialized-gram-clt"></a>
### Initialized Gram fluctuations, including singular covariances

This initialization statement needs only real \(C^2\) activations with
bounded first two derivatives and linear growth. Fix any finite query
list, allowing duplicates, and index covariance coordinates by pairs
\((a,b),(c,e)\).
Let
\[
K_{n,ab}^{(j)}=n^{-1}(h_0^{(j)}(v_a))^Th_0^{(j)}(v_b),
\qquad Q^{(j)}=\Psi_j(Q^{(j-1)}).
\]
Here \(\Psi_j(C)_{ab}=\mathbb E[\phi_j(Z_a)\phi_j(Z_b)]\) for
\(Z\sim N(0,C)\), and \(Q^{(0)}\) is the input Gram on this query list.
Identify symmetric matrices with their upper triangular coordinates.
For \(Z\sim N(0,Q^{(j-1)})\), define the innovation covariance
\[
(B_j)_{ab,ce}=
\mathbb E[\phi_j(Z_a)\phi_j(Z_b)\phi_j(Z_c)\phi_j(Z_e)]
-Q^{(j)}_{ab}Q^{(j)}_{ce},
\]
and define the linear map on symmetric perturbations by
\[
(T_jE)_{ab}=
\tfrac12E_{aa}\mathbb E[\phi_j''(Z_a)\phi_j(Z_b)]
+E_{ab}\mathbb E[\phi_j'(Z_a)\phi_j'(Z_b)]
+\tfrac12E_{bb}\mathbb E[\phi_j(Z_a)\phi_j''(Z_b)].
\]
All these Gaussian integrals are finite, including at singular
covariances. The joint limit at fixed depth and fixed query list is
\[
\sqrt n(K_n^{(j)}-Q^{(j)})\ \Longrightarrow\ \Xi_j,
\qquad \Xi_0=0,\qquad \Xi_j=T_j\Xi_{j-1}+G_j,
\]
where the \(G_j\) are independent centered Gaussian symmetric matrices
with covariances \(B_j\). In particular, with \(C_j\) the covariance
of \(\Xi_j\),
\[
C_0=0,\qquad C_j=T_jC_{j-1}T_j^T+B_j.
\]
The transpose here is that of the finite-dimensional coordinate map
on symmetric matrices. This is a theorem about initialized features,
not an independence assertion for trained neurons.

<a id="dense-innovation-lower"></a>
### Positive feature rank forces a last-layer innovation

Assume now \(m\ge2\) and \(Y>0\). Let
\[
Z\sim N(0,Q^{(L-1)}),\qquad H_a=\phi_L(Z_a),\qquad
Q=\mathbb E HH^T=Q^{(L)},\qquad S_y=y^TH,
\]
\[
\mu_4=\mathbb E\phi_L(\sqrt{\mu_{2,L-1}}G)^4.
\]
Both \(\mu_{2,L}\) and \(\mu_4\) are positive and finite. Linear
growth gives explicitly
\(\mu_4\le8|\phi_L(0)|^4+
24\|\phi_L'\|_\infty^4\mu_{2,L-1}^2\).
If \(\mu_{2,L-1}=0\), every coordinate of \(H\) would be the same
deterministic constant, contradicting \(Q\succ0\) for \(m\ge2\).
Thus the final preactivation marginal variance is positive as well.

The distribution-free moment inequality needed here is
\[
\operatorname{tr}\operatorname{Cov}(HS_y)
\ge\frac{(m-1)\gamma^3(m\mu_{2,L}-\gamma)}{4m^2\mu_4}
\|y\|_2^2
\ge\frac{(m-1)^2\gamma^3\mu_{2,L}}{4m^2\mu_4}\|y\|_2^2
\ge\frac{\gamma^3\mu_{2,L}}{16\mu_4}\|y\|_2^2.
\]
No independence between the \(m\) coordinates is used.

<a id="dense-finite-query-source"></a>
### Finite-query complex time and its exact recurrence scope

This subsection invokes the local insertion interface in
[the source foundation](#source-foundations), with the same claim level
and eventual-width qualification as that interface. It records the
finite-query modification required by the lower theorem; a whole-sphere
complex-time radius cannot simply be replaced by a larger radius without
this argument.

Write \(H_j^{\rm src},f_j^{\rm src},q_j^{\rm src},T_Q^{\rm src}\)
for exactly the source coefficients called \(H_j,f_j,q_j,T_Q\) in
that foundation. The superscript distinguishes its RMS and response
coefficients from \(H_D\), the Gaussian marginal moments, and the
global compression order \(q\). For activity \(S=16Y/\lambda\), define
\[
U_1^{\rm fin}(S)=4sK_{\rm src},
\]
\[
U_j^{\rm fin}(S)=2\left\{
sK_{\rm src}\left[(H_{j-1}^{\rm src})^2+(f_{j-1}^{\rm src})^2
+S T_Q^{\rm src}+S^2H_{j-1}^{\rm src}q_{j-1}^{\rm src}\right]
+64q_{j-1}^{\rm src}+1\right\}\quad(j\ge2),
\]
\[
U_{\rm fin}(S)=\max_jU_j^{\rm fin}(S),\qquad
\chi(S)=\min\left\{1,\frac{a}{4S^2U_{\rm fin}(S)}\right\},
\]
\[
\chi_{\rm act}=\min\left\{1,
\frac{a}{4(S_*^{\rm src})^2U_{\rm fin}(S_*^{\rm src})}\right\}>0.
\]
Every coefficient in these polynomials is nonnegative, so
\(\chi(S)\ge\chi_{\rm act}\) throughout the original source
allowance \(S\le S_*^{\rm src}\). The latter coefficient depends
only on the fixed activations and depth.

Let \(T_n=32\lambda^{-1}\log(en)\), and choose
\[
0<c\le\frac{a}{64YSU_{\rm fin}(S)}
=\frac{a}{4\lambda S^2U_{\rm fin}(S)},\qquad r_n=c/\sqrt{\log(en)}.
\]
For explicit domain gates, use the source's backward RMS coefficients
\(\tau_j^{\rm src}\), and define
\[
\mathcal K=(H_L^{\rm src})^2+
S^2\left[(\tau_1^{\rm src})^2+
\sum_{j=2}^L(\tau_j^{\rm src})^2(H_{j-1}^{\rm src})^2\right],
\]
\[
D_W=\max\{\tau_1^{\rm src},
\max_{j\ge2}\tau_j^{\rm src}H_{j-1}^{\rm src}\}.
\]
The sufficient numerical gates are
\[
n^{-1}\le Y,\qquad
\sqrt{\log(en)}\ge c\max\{8,\lambda,4\mathcal K/\log2,32YSD_W\}.
\]
There are localized source events with probability tending to one
on which the predictions at every query in the fixed finite collection
are holomorphic on a neighborhood of
\[
[-r_n,T_n+r_n]+i[-r_n,r_n].
\]
The forward RMS is at most \(H_j^{\rm src}\) and the readout RMS
at most \(SH_L^{\rm src}\). At any one of these queries \(v\), put
\(g_n(t)=f_n(t,v)-\widetilde f_n(t,v)\). On both copies' events,
\[
|g_n(t)|\le2S(H_L^{\rm src})^2
\le32\beta^{6L}Y/\lambda
\]
throughout this rectangle. The last inequality uses
\(H_L^{\rm src}\le\beta^{3L}\), independently of the smaller
beta-only label cap. All these localized probability conclusions retain
the source interface's unquantified sufficient width.

<a id="dense-trajectory-lower"></a>
### Actual-trajectory lower bound and its confidence coefficient

For every fixed admissible problem with \(m\ge2\), nonzero labels,
and \(0<\delta<1\), at every sufficiently large individual width,
\[
\mathbb P\left\{\|f_n-\widetilde f_n\|_*
\ge c_{\phi,L,\delta}\,
\frac{Y\sqrt\gamma}{\sqrt n\,[\log(en)]^{5/2}}\right\}
\ge1-\delta,
\]
where on the full recurrence range one can take
\[
c_{\phi,L,\delta}=
\frac{\chi_{\rm act}}{128}
\Phi^{-1}(1/2+\delta/4)\sqrt{\frac{\mu_{2,L}}{\mu_4}}.
\]
Here \(\Phi\) is the standard normal distribution function. On the
unchanged cap \(Y\le(\gamma/m)\beta^{-30L}\), one may replace
\(\chi_{\rm act}\) by one. A sharper fixed-label version replaces
it by \(\chi(S)\). These are positive coefficients; neither a
confidence-independent numerical constant nor a quantified success width
is asserted.

The witness is the deterministic training query \(v_{a_*}\) selected
by the innovation inequality and some strictly positive time
\[
0<t\le\frac{\chi(S)m}{\gamma\sqrt{\log(en)}}
\le\frac m{\gamma\sqrt{\log(en)}}.
\]
The witnessing time may depend on width and initialization. At that
training query the fitted endpoints agree exactly with the prescribed
label, so this theorem is not an endpoint lower bound.

#### Necessary storage within the independent dense family

For a nondegenerate fixed task with \(m\ge2\), fix
\(0<\delta<1/2\). Once the lower theorem's sufficient width is met,
the accuracy condition
\(\Pr\{\|f_n-\widetilde f_n\|_*\le\varepsilon\}\ge1-\delta\)
necessarily implies
\[
n[\log(en)]^5\ge
\frac{c_{\phi,L,\delta}^2Y^2\gamma}{\varepsilon^2},
\qquad
S_D(n)\ge
\frac{(L-1)c_{\phi,L,\delta}^4Y^4\gamma^2}
{\varepsilon^4[\log(en)]^{10}}.
\]
The proof below establishes the resulting fixed-task storage order
\(\varepsilon^{-4}/\log(1/\varepsilon)^{10}\) up to a positive
fixed-task coefficient. This is a statement about independent canonical
dense runs, not arbitrary alternative representations.

<a id="dense-dependency-boundary"></a>
### Dependency and width boundary of the dense section

The quantitative fitting theorem, parameter comparison, Gaussian
concentration, initialized Gram CLT, innovation inequality, confidence
conversion, and scalar accuracy inversion have complete proofs below.
The initialized CLT is qualitative in width; no Berry--Esseen constant
or explicit CLT success threshold is available in these inputs.

The trained carrier event and finite-query holomorphic event depend on
the shared source foundation's local Gaussian insertion theorem and
its complex extension. Their finite activation/depth coefficients are
the displayed source recurrences, not unspecified comparison constants.
Their eventual stochastic width, coordinate-remainder constants,
control-uniform stopping bounds, and higher-derivative probability
constants are not quantified by the dense inputs. Any unresolved proof
obligation for that source interface is inherited by the dense upper
and actual-trajectory lower claims; the deterministic downstream proofs
do not remove it. The concrete numerical initialization threshold and
the displayed domain/remainder gates must remain distinct from that
unquantified source success threshold.

The same statements concern each sufficiently large individual width.
They do not provide one event over infinitely many independently
initialized widths, a joint growing-data/depth limit, strict root-width
upper concentration, or a general fitted-endpoint variability lower
bound. A finite union of model comparisons uses split failure budgets;
no independence of their good events is required.


<a id="legendre-compression"></a>
### Legendre compression: every order, both label ranges, and accuracy inversion

This section uses the dense model, Gaussian initialization, activation
assumptions and covariance gap already specified in this document. In
particular, \(n,m,d\ge1\), \(L\ge2\),
\(\|x_a\|_2=\sqrt d\), \(Y=\|y\|_2/\sqrt m\), and
\(\gamma=\lambda_{\min}(Q^{(L)})>0\). The loss is
\(m^{-1}\sum_a(f_n(x_a)-y_a)^2\), the mobilities are
\((n,1,\ldots,1,n)\), and the initial readout is zero. The
Legendre model shares the realized initialization and the physical time
\(t\) of its dense reference. Its order \(q\) is any positive integer.

The deterministic proofs below apply on the explicitly stated
initialization and dense-carrier event. Its probability is supplied by the
[shared source argument](#source-foundations), including its local
Gaussian insertion proof. The source's sufficient stochastic width remains
implicit. The initialization event itself has the effective threshold
proved in [dense fitting](#dense-fitting).

<a id="legendre-runtime"></a>
#### The stored state and its autonomous equations

Write \(v_a=x_a/\sqrt d\). Superscripts indicate layers, including
the stored readout \(W^{(L+1)}\in\mathbb R^n\). For the dense model,
and separately for the reconstructed model with hats, define
\[
z^{(1)}(x)=W^{(1)}x/\sqrt d,\qquad
z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x),\qquad
h^{(\ell)}(x)=\phi_\ell(z^{(\ell)}(x)),\qquad
f_n(x)=\frac{(W^{(L+1)})^Th^{(L)}(x)}n.
\]
The dense backward carriers and responses on training sample \(a\) are
\[
k_a^{(L)}=W^{(L+1)},\qquad
k_a^{(\ell)}=(W^{(\ell+1)})^T\delta_a^{(\ell+1)},\qquad
\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)}.
\]
The symbol \(\delta_a^{(\ell)}\) is a backward response; the
unsubscripted \(\delta\in(0,1)\) remains the failure probability.
The residual is \(r_a=f_n(x_a)-y_a\), and
\(\rho=\|r\|_2/\sqrt m\). The dense physical equations are
\[
\dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^T,
\quad
\dot W^{(\ell)}=-\frac2{mn}\sum_a
r_a\delta_a^{(\ell)}(h_a^{(\ell-1)})^T,
\quad
\dot W^{(L+1)}=-\frac2m\sum_a r_ah_a^{(L)}.
\tag{Legendre-dense-flow}
\]
The middle equation applies to \(2\le\ell\le L\).

For each such interface, training sample \(a\), and
\(j=0,\ldots,q-1\), store two vectors in \(\mathbb R^n\),
\(\bar h_{a,j}^{(\ell-1)}\) and
\(\bar\delta_{a,j}^{(\ell)}\). Together with
\(\widehat W^{(1)},\widehat W^{(L+1)}\) and one scalar \(\tau\),
these are the complete moving state. Reconstruct the remaining matrices by
\[
\widehat W^{(\ell)}
=W_0^{(\ell)}-
\frac2{mn\tau}\sum_{a=1}^m\sum_{j=0}^{q-1}(2j+1)
\bar\delta_{a,j}^{(\ell)}
(\bar h_{a,j}^{(\ell-1)})^T.
\tag{Legendre-reconstruction}
\]
Compute its forward pass, backward responses, residuals and
\(\widehat\rho=\|\widehat r\|_2/\sqrt m\) from these matrices.
Its first matrix and readout obey (Legendre-dense-flow) evaluated at the
reconstructed state. Its remaining equations are
\[
\dot\tau=\widehat\rho,\qquad \tau(0)=1,
\]
\[
\dot{\bar h}_{a,j}^{(\ell-1)}
=\widehat\rho\widehat h_a^{(\ell-1)}
-\frac{\widehat\rho}{\tau}
\left(j\bar h_{a,j}^{(\ell-1)}
+\sum_{i<j}(2i+1)\bar h_{a,i}^{(\ell-1)}\right),
\]
\[
\dot{\bar\delta}_{a,j}^{(\ell)}
=\widehat r_a\widehat\delta_a^{(\ell)}
-\frac{\widehat\rho}{\tau}
\left(j\bar\delta_{a,j}^{(\ell)}
+\sum_{i<j}(2i+1)\bar\delta_{a,i}^{(\ell)}\right).
\tag{Legendre-moment-flow}
\]
Initially \(\bar h_{a,0}^{(\ell-1)}=h_{0,a}^{(\ell-1)}\);
all other moments are zero. Thus the forward histories have their constant
initialized values on \([0,1]\), while the backward histories are zero
there. The runtime equations involve no division by a residual and are
locally Lipschitz even at \(\widehat\rho=0\). They then have zero
velocity. The histories used in the proof are not additional stored arrays.

The exact counts in real coordinates are
\[
S_{\rm moving}(n,q)=n(d+1)+1+2(L-1)mnq,
\qquad S_{\rm fixed}(n)=(L-1)n^2,
\]
\[
S_{\rm model}(n,q)=(L-1)n^2+n(d+1)+1+2(L-1)mnq.
\tag{Legendre-storage}
\]
These are retained model-state counts; storing the input data and labels
adds \(m(d+1)\). Reconstructed dense matrices can be evaluated from the
displayed state and are not counted as independently retained parameters.
These inventory counts alone concern exact real coordinates, not bit
precision or execution cost. The separate
[cost interface](#computational-costs) includes preprocessing, runtime
and the specified working-memory caches.

<a id="legendre-labels"></a>
#### Label allowances and the event used by the error certificates

The following coefficients are local to this section. Define
\[
b=\max_\ell|\phi_\ell(0)|,\qquad
s=\max\{1,\max_\ell\sup_{|\operatorname{Im}z|\le a/2}
|\phi_\ell'(z)|\},\qquad
t_2=\max_\ell\sup_{|\operatorname{Im}z|\le a/2}|\phi_\ell''(z)|.
\]
The shared envelope is
\(\beta=\max\{10,1+b,16/a,s,\max(1,t_2)\}\).
Set \(\sigma_0=1\) and
\[
\sigma_\ell^2=\mathbb E\phi_\ell(\sigma_{\ell-1}G)^2,
\quad G\sim N(0,1),\qquad
H=\max\{1,\sigma_1,\ldots,\sigma_L\}.
\]
These scalar moments exist by \(|\phi_\ell(u)|\le b+s|u|\).
Every diagonal of \(Q^{(\ell)}\) is \(\sigma_\ell^2\), so
\(\gamma/m\le H^2\). Define
\[
D_\ell=s(9s)^{L-\ell},\qquad
F=s^2\left[(9s)^{2L-2}
+4H^2\sum_{j=0}^{L-2}(9s)^{2j}\right],
\]
\[
C_1=4s^2D_1^2,\qquad
C_\ell=3s^2(64H^4D_\ell^2+82C_{\ell-1}),\qquad
E=130\sum_{\ell=2}^LD_\ell\sqrt{C_{\ell-1}},
\]
\[
S_*^{\rm Leg}=\min\left\{1,\frac1{64H^2D_1},
\frac1{\sqrt{8\sqrt{C_L}}},
\left(\frac1{8H^2D_1E}\right)^{2/7}\right\}.
\tag{Legendre-fitting-coefficients}
\]
There is no unspecified constant in these recurrences. The source
coefficients \(S_*^{\rm src},K_{\rm src}\) are exactly the finite
recurrences defined and estimated in [source foundations](#source-foundations).

The larger label allowance needed by the Legendre comparison is
\[
0<Y\le\frac\gamma m
\min\left\{\frac1{8H\sqrt F},\frac{S_*^{\rm Leg}}8,
\frac{S_*^{\rm src}}{16}\right\}.
\tag{Legendre-full-labels}
\]
In particular this holds throughout the original common allowance, whose
additional Harmonic-fitting term only restricts the common range. The
smaller, sufficient cap is exactly
\[
0<Y\le\frac\gamma m\beta^{-30L}.
\tag{Legendre-simple-labels}
\]
Neither label range is replaced by an error-dependent restriction.

The deterministic initialization event is
\[
\frac{\|W_0^{(1)}\|_{\rm op}}{\sqrt n}\le8,\quad
\max_{2\le\ell\le L}\|W_0^{(\ell)}\|_{\rm op}\le8,\quad
\sup_{\|x\|_2=\sqrt d,\ell}
\frac{\|h_0^{(\ell)}(x)\|_2}{\sqrt n}\le\frac{3H}2,
\]
\[
\frac{\mathsf H_0^T\mathsf H_0}{mn}
\succeq\frac\gamma{2m}I_m,
\qquad \mathsf H_0=[h_{0,a}^{(L)}]_{a=1}^m.
\tag{Legendre-initialization-event}
\]
On this event dense fitting and the proof below give, for all orders,
all sphere queries and all times, normalized first-matrix operator norm
and hidden-matrix operator norms below nine, feature RMS below \(2H\),
and
\[
\rho_D(t)\le Ye^{-\gamma t/(2m)},\qquad
\widehat\rho(t)\le Ye^{-\gamma t/(4m)},
\]
\[
\frac{\|W_D^{(L+1)}(t)\|_2}{\sqrt n}
\le2Y\sqrt{m/\gamma},\qquad
\frac{\|\widehat W^{(L+1)}(t)\|_2}{\sqrt n}
\le4Y\sqrt{m/\gamma}.
\tag{Legendre-physical-bounds}
\]
Both systems converge in physical parameters and fit the training labels.
The additional source event used for approximation is precisely
\[
\max_{a,\ell,i}\sup_{t\ge0}|k_{D,a,i}^{(\ell)}(t)|
\le M_n:=32K_{\rm src}\frac{Ym}\gamma\sqrt{\log(en)}.
\tag{Legendre-carrier-event}
\]
This involves training inputs only. The source argument supplies the
all-time factor two relative to its finite-horizon carrier estimate.
For every fixed \(\delta\in(0,1)\), split the failure budget between
initialization and source events. Their intersection has probability at
least \(1-\delta\) for
each sufficiently large individual width. The source part of the width
threshold remains implicit. One such event works for every order at that
width and for every requested accuracy; no order or tolerance union bound
is required.

<a id="legendre-forward-certificates"></a>
#### Error from a supplied order

For any two predictors use the whole-trajectory, whole-sphere distance
\[
\|f-g\|_*=\sup_{t\in[0,\infty]}
\sup_{\|x\|_2=\sqrt d}|f(t,x)-g(t,x)|.
\]
The fitted endpoints are included. This is a function-fidelity statement,
not a claim about unknown test labels.

On (Legendre-simple-labels), define the exact actual-label coefficient
\[
\begin{split}
P_n={}&3\beta^{100L}\left(\frac{Ym}\gamma\right)^2
\left(1+\frac m\gamma\right)
\left[1+\beta^{100L}\frac{Ym}\gamma\sqrt{\log(en)}\right]\\
&\quad\times
\left[1+\beta^{100L}\left(\frac{Ym}\gamma\right)^2
\left(e^{\sqrt{\log(en)}}-1\right)\right].
\end{split}
\tag{Legendre-simple-coefficient}
\]
Simultaneously for every integer \(q\ge1\),
\[
\|f_{{\rm Leg},n,q}-f_n\|_*
\le YP_n\frac{\sqrt{\log(eq)}}{q^2}.
\tag{Legendre-simple-forward}
\]
An explicit, weaker structural envelope, if a shorter expression is
preferred, is
\[
\|f_{{\rm Leg},n,q}-f_n\|_*
\le12\beta^{300L}Y\left(1+\frac m\gamma\right)^6
e^{\sqrt{\log(en)}}
\frac{\sqrt{\log(en)\log(eq)}}{q^2}.
\tag{Legendre-structural-forward}
\]

For the full range (Legendre-full-labels), use the following exact finite
assembly instead. In these coefficient definitions only, put
\[
\kappa=\frac\gamma{4m},\quad
R=8Y\sqrt{m/\gamma},\quad S=\frac{8Ym}\gamma,
\quad a_0=\frac{4Ym}\gamma,\quad T_0=9s,
\quad B_\delta=sT_0^{L-1}R,\quad F_z=2HT_0^{L-1},
\]
\[
P_0=1+2H(L-1),\qquad
B_d=sT_0^{L-1}(1+B_\delta)+Lt_2F_zT_0^{L-1}M_n,
\]
\[
V_z=2F_zB_\delta P_0,\qquad
V_\delta=T_0^{L-1}
[4sH+4sH(L-1)B_\delta^2+Lt_2M_nV_z],
\]
\[
T_1=2D_1R,\qquad
T_\ell=4HD_\ell R+130D_\ell\sqrt{SC_{\ell-1}}R^2,
\]
\[
V_1=sT_1,\qquad V_\ell=s(2HT_\ell+9V_{\ell-1}),
\qquad V_h=\max_{1\le\ell\le L}V_\ell,
\]
\[
C_c=4\left(4H^2+D_1^2R^2
+4H^2R^2\sum_{\ell=2}^LD_\ell^2\right)+\frac\gamma{2m},
\]
\[
F_h=V_ha_0\sqrt{(1+a_0)/2},\qquad
b_1=\frac{2\sqrt{1+a_0}}\kappa C_cB_\delta,
\]
\[
b_0=\frac{\sqrt{1+a_0}Y}\kappa V_\delta
+2B_\delta\sqrt{a_0},\qquad C_f=2H+RsF_z.
\tag{Legendre-projection-coefficients}
\]
Define segment feature and gradient coefficients by
\[
Q_1=b+9s,\qquad Q_\ell=b+9sQ_{\ell-1},\qquad
Q=\max\{1,Q_1,\ldots,Q_L\},\qquad F_{\rm seg}=QT_0^{L-1},
\]
\[
d_0=sT_0^{L-1}(1+B_\delta),\qquad
d_1=Lt_2F_{\rm seg}T_0^{L-1},\qquad p=1+Q(L-1),
\]
\[
K_0=\sqrt{L+1}\{pd_0+[1+(L-1)B_\delta]sF_{\rm seg}\},
\qquad K_1=\sqrt{L+1}\,pd_1,
\]
\[
\mathcal A_n=\sqrt{L+1}
\exp\left\{14(K_0+K_1M_n)\frac{Ym}\gamma\right\}.
\tag{Legendre-stability-coefficients}
\]
The local scalar \(d_1\) here is a gradient coefficient, not the input
dimension \(d\). Finally set
\[
T_n=4(L-1)F_hB_d\sqrt{a_0}\,\mathcal A_n,
\qquad C_n=4(L-1)C_f\mathcal A_nF_h(b_0+b_1),
\qquad U=12HY\sqrt{m/\gamma}.
\tag{Legendre-full-coefficients}
\]
Then, simultaneously for every integer \(q\ge1\),
\[
\|f_{{\rm Leg},n,q}-f_n\|_*
\le C_n\frac{\sqrt{\log(eq)}}{q^2}
+U\left(\frac{T_n}{q}\right)^4.
\tag{Legendre-full-forward}
\]
The order-independent bound \(\|f_{{\rm Leg},n,q}-f_n\|_*\le U\)
also holds. The simple-cap coefficient is not extended to larger labels;
the displayed recurrence certificate preserves that larger range.

<a id="legendre-inverse-certificates"></a>
#### Accuracy and failure probability as inputs

Fix a permitted problem, \(\varepsilon>0\),
\(0<\delta<1\), and a reference width in the event's sufficient-width
range. The width condition is the same one already stated above; no new
accuracy-dependent stochastic threshold is introduced. The inverse below
is therefore a deterministic order certificate with success probability
at least \(1-\delta\), not an effective
confidence-certified choice of reference width.

Under the simple cap and \(Y>0\), the least positive integer certified
by (Legendre-simple-forward) is exactly
\[
q_{\min}(n,\varepsilon)=
\min\left\{q\in\mathbb N:\ q\ge1,\quad
\frac{YP_n}{\varepsilon}\sqrt{\log(eq)}\le q^2\right\}.
\tag{Legendre-simple-inverse}
\]
This minimizes the increasing storage formula within this certificate;
it is not a minimum over all representations or the actual dynamics.
The minimum exists and every larger integer works. For a closed sufficient choice put
\(r=YP_n/\varepsilon\) only in this inversion formula and take
\[
q_{\rm suff}=
\begin{cases}
1,&r\le1,\\
\left\lceil2\sqrt r[\log(e+r)]^{1/4}\right\rceil,&r>1.
\end{cases}
\tag{Legendre-simple-sufficient-order}
\]
The second branch gives error at most \(\varepsilon/2\).

A sufficient inverse using only the structural envelope is the same
two-branch formula with the explicit ratio
\[
r=\frac{12\beta^{300L}Y}{\varepsilon}
\left(1+\frac m\gamma\right)^6
\sqrt{\log(en)}e^{\sqrt{\log(en)}}.
\tag{Legendre-structural-inverse-ratio}
\]
Equivalently, when this ratio exceeds one, its order is
\[
\left\lceil4\sqrt3\,\beta^{150L}
\left(1+\frac m\gamma\right)^3\sqrt{\frac Y\varepsilon}
\bigl[\log(en)\log(e+r)\bigr]^{1/4}
e^{\frac12\sqrt{\log(en)}}\right\rceil.
\tag{Legendre-structural-sufficient-order}
\]
The scalar \(r\) is only the fully displayed ratio above. Order one
suffices when it is at most one; no asymptotic logarithm replacement is
needed for these formulas.

For the full label allowance, define the exact least integer inverse
\[
q_{\min}^{\rm full}(n,\varepsilon)=
\min\left\{q\ge1:\
C_n\frac{\sqrt{\log(eq)}}{q^2}
+U\left(\frac{T_n}{q}\right)^4\le\varepsilon\right\}.
\tag{Legendre-full-inverse}
\]
The braces here range over integers; this minimum exists.
It equals one whenever \(C_n+UT_n^4\le\varepsilon\).
For a direct sufficient formula apply (Legendre-simple-sufficient-order)
with \(r=2C_n/\varepsilon\), call the resulting integer \(q_1\),
and choose
\[
q=\max\left\{q_1,1,
\left\lceil T_n(2U/\varepsilon)^{1/4}\right\rceil\right\}.
\tag{Legendre-full-sufficient-order}
\]
Both summands are then at most \(\varepsilon/2\). The second entry is an accuracy allocation, not an absorption
gate; before rounding it is below \(T_n\) when
\(\varepsilon>2U\). If using the additional uniform cap is desired,
\(\varepsilon\ge U\) already permits \(q=1\) in either range.
This optional improvement is separate from the least integer inverse of
the displayed decreasing envelope.

In all cases substitute the chosen order into (Legendre-storage).
Conversely, a supplied moving-coordinate budget \(S_{\rm budget}\)
admits the largest order
\[
q_{\rm budget}=\left\lfloor
\frac{S_{\rm budget}-n(d+1)-1}{2(L-1)mn}\right\rfloor.
\tag{Legendre-storage-inverse}
\]
If this is below one, the budget does not hold an order-one instance of
the stipulated representation. Otherwise evaluate the applicable forward
certificate at that order. For a total model-state budget first subtract
\((L-1)n^2\), and also subtract \(m(d+1)\) if data storage is
included. Counts grow strictly with \(q\), so this is the best
certified decreasing error under that coordinate budget.

If \(Y=0\), all moment velocities, parameter velocities and predictions
are zero. Every order is exact; the constant-zero predictor alone is an
exact compression if only predictor fidelity is requested. No expression
dividing by \(Y\) is used. If \(\varepsilon=0\) and \(Y>0\),
the positive finite-order upper envelopes certify no finite order; this
does not assert that a particular network cannot agree exactly. Negative
accuracy or \(\delta\notin(0,1)\) is outside the stated interface.
There is no exactness claim at \(q=n\) for this temporal Legendre
representation, and no need to constrain \(q\) by \(n\).

The retained simple-cap prescription for a strict root-width target is
\[
Q_n=\max\{3,n^{1/4}\sqrt{P_n}\},\qquad
q_n=\left\lceil4Q_n[\log(e+Q_n)]^{1/4}\right\rceil,
\qquad
\|f_{{\rm Leg},n,q_n}-f_n\|_*\le\frac{Y}{8\sqrt n}.
\tag{Legendre-root-width-order}
\]
Here \(Q_n\) is only an auxiliary expression for selecting the one
runtime order \(q_n\), not a second approximation order.

At fixed admissible positive labels and other structural parameters,
\(M_n\) is proportional to \(\sqrt{\log(en)}\), and
\(\log C_n,\log T_n=o(\log n)\). For a polynomial target
\(\varepsilon=Yn^{-\alpha}\) with fixed \(\alpha>0\), the
sufficient orders are \(n^{\alpha/2+o(1)}\) in both label ranges;
the second full-range entry is only \(n^{\alpha/4+o(1)}\).
In particular \(\varepsilon=Y/\sqrt n\) gives
\(q=n^{1/4+o(1)}\) and moving state \(n^{5/4+o(1)}\), while
the retained initialized mixers still have \((L-1)n^2\) entries.
These are sufficient fixed-problem storage rates, with the probability
and exact-real qualifications already stated.


<a id="compact-construction"></a>
<a id="harmonic-construction"></a>
### Harmonic neural dynamics with a supplied neuron budget

<!-- method-names:start -->
The proof-local subscript \(C\) continues to denote the compressed
Harmonic model; its coefficient labels are unchanged.
<!-- method-names:end -->

The Harmonic model has its own evolving first weights, hidden mixers, raw
readout, and label deficit. Its effective readout is reconstructed from its
current features. The construction below approximates the realized dense
trajectory at the same physical times, on the whole input sphere, including
the fitted limit. Its only size parameter is the integer neuron budget
\(q\). Source tolerances, approximation degrees, quadratures and initial
jets are setup objects and are discarded.

The dense architecture, Gaussian initialization with zero readout, loss,
mobilities, activation strip and unweighted gap \(\gamma\) are the shared
ones. In particular the residual convention remains \(r=f-y\). The
Harmonic state variable \(c=y-f=-r\) is called the label deficit below.
This section uses the source event and finite coefficients in
[the source foundations](#source-foundations). It does not convert an
eventual stochastic width into an effective confidence bound. The
deterministic harmonic approximation, coordinate selection, metric,
initialization, runtime, and comparison arguments are supplied here.

For coefficient formulas and proofs only, write
\(\lambda=\gamma/m\), \(z=Y/\lambda\),
\(\alpha=Y/\sqrt\lambda\), and \(S=16Y/\lambda\).
These are explicit arithmetic expressions, not new parameters or a
capped gap. Write \(b=\max_j|\phi_j(0)|\), and let \(s\ge1\) and
\(t_2\ge1\) be the first and second derivative bounds on the safe
half-strip. Thus \(\beta=\max(10,1+b,16/a,s,t_2)\).
Superscript \({\rm src}\) distinguishes the source coefficients from
the Harmonic coefficients defined next.

<a id="compact-fitting-coefficients"></a>
<a id="harmonic-fitting-coefficients"></a>
#### Exact label interval and runtime coefficients

Let \(H_d,F_d\) denote the dense fitting coefficients: if
\(v_0=1\) and
\(v_j=\mathbb E\phi_j(\sqrt{v_{j-1}}Z)^2\), \(Z\sim N(0,1)\), then
\[
H_d=\max(1,\sqrt{v_1},\ldots,\sqrt{v_L}),\qquad
F_d=s^2\left[(9s)^{2L-2}
       +4H_d^2\sum_{k=0}^{L-2}(9s)^{2k}\right].
\tag{Harmonic dense coefficients}
\]
For the Harmonic runtime define
\[
H_1^c=2b+16s,\qquad H_j^c=2b+18sH_{j-1}^c,\qquad H_c=H_L^c,
\]
\[
d_j^c=2s(18s)^{L-j},\quad U_1^c=d_1^c,\quad
U_j^c=2H_cd_j^c\ (j\ge2),\quad
F_1^c=2sU_1^c,\quad F_j^c=2s(2H_cU_j^c+9F_{j-1}^c),
\]
\[
F_c=F_L^c=(d_1^c)^2+4H_c^2\sum_{j=2}^L(d_j^c)^2.
\tag{Harmonic fitting coefficients}
\]
The omitted maxima with one in these recurrences are inactive because
\(s\ge1\). The full Harmonic label interval is
\[
0<Y\le\frac\gamma m
\min\left\{\frac1{8H_d\sqrt{F_d}},
             \frac1{16H_c\sqrt{F_c}},\frac{S_*^{\rm src}}{16}\right\}.
\tag{Harmonic full label interval}
\]
Every conclusion below holds on this entire interval. An additional
Legendre allowance in a joint theorem can be intersected with this
interval; no smaller Harmonic label cap is required. The scalar Gaussian
moment recursion gives \(\sqrt\lambda\le H_c\). In particular
\(S\le1\), \(z\le1/16\), and
\(\alpha\le1/(16\sqrt{F_c})\le1/16\).

For later tail estimates define the following explicit functions of the
same coefficients:
\[
R_c=5\alpha,\qquad G_c=4H_c^2+R_c^2F_c,
\]
\[
B_w^c=4H_c+48R_cF_cz+4G_c/\sqrt\lambda,\qquad
B_f^c=2H_cB_w^c+2R_c^2F_c,
\]
\[
\mathcal K=(H_L^{\rm src})^2+
 S^2\left[(\tau_1^{\rm src})^2+
 \sum_{j=2}^L(\tau_j^{\rm src})^2(H_{j-1}^{\rm src})^2\right],
\qquad \mathcal D=z(16\mathcal K+4B_f^c).
\tag{Harmonic tail coefficient}
\]

<a id="compact-runtime-definition"></a>
<a id="harmonic-runtime-definition"></a>
#### Selected architecture, exact initialization and optimizer

Fix a source horizon \(T\) and coordinate tolerance \(\eta\), chosen
from the supplied budget in the theorem below. At layer \(j\), define
the source space \(E_j\subset\mathbb R^n\) using the empirical pairing
\(u^Tv/n\). The four possible vector-valued source families, indexed by
\((t,v)\in[0,T]\times S^{d-1}\), are
\[
h_n^{(j)}(t,v),\qquad
W_0^{(j)}h_n^{(j-1)}(t,v)\ (j\ge2),\qquad
\delta_n^{(j)}(t,v),\qquad
W_0^{(j+1)T}\delta_n^{(j+1)}(t,v)\ (j<L).
\tag{Harmonic source families}
\]
Here \(W_0^{(j)}\) is the initialized dense mixer. The forward-image
family is absent at layer one, and the reverse-image family is absent
at layer \(L\). For a passive query the dense backward fields are
\[
k_n^{(L)}(t,v)=w_n(t),\quad
\delta_n^{(j)}(t,v)=\phi_j'(z_n^{(j)}(t,v))\odot k_n^{(j)}(t,v),\quad
k_n^{(j)}(t,v)=W_n^{(j+1)}(t)^T\delta_n^{(j+1)}(t,v)\ (j<L).
\]
A passive query is evaluated using the trained parameters but contributes
no update force.

The space \(E_j\) is the real span of the coefficient vectors actually
computed by the finite cosine–spherical-harmonic construction below for
these families, together with the exact initialized vectors
\[
\mathbf1_n,\quad
\{h_n^{(j)}(0,v_a):1\le a\le m\},\quad
\{W_0^{(j)}h_n^{(j-1)}(0,v_a):1\le a\le m\}\ (j\ge2),
\]
and the \(d\) columns of \(A_0\) when \(j=1\).
It uses finite initial-jet/quadrature coefficients, not unavailable
exact integrals of a trained reference. The exact additions number
at most \(m+d+1\) at the first layer and \(2m+1\) at each later
layer. Thus \(B=2m+d+1\) bounds their dimension uniformly.
The construction's counts give
\(\dim E_j\le B+4N(T,\eta)\) for \(d\ge2\).
For \(d=1\) the separate temporal expansions at \(v=-1,1\) give
\(\dim E_j\le B+8N_1(T,\eta)\). The functions \(N,N_1\)
are defined explicitly in the supplied-budget statement.

Use identical cutoff, quadrature and initial-jet operations in every
feature/image pair and response/reverse-image pair. These scalar
operations commute exactly with each initialized mixer. Consequently
the computed approximants obey
\[
p_h^{(j-1)}\in E_{j-1},\quad W_0^{(j)}p_h^{(j-1)}\in E_j,\qquad
p_\delta^{(j+1)}\in E_{j+1},\quad
W_0^{(j+1)T}p_\delta^{(j+1)}\in E_j,
\tag{Harmonic paired source membership}
\]
with a separate coordinate-error bound \(\eta\) for each member of
each pair. These are the paired actions used in the comparison proof;
no further source family or stored runtime order is being introduced.

At layer \(j\), selection supplies \(q_j\) coordinates and a positive
metric \(M_j\), with a positive diagonal comparison metric \(\mathsf D_j\):
\[
\mathsf D_j/4\preceq M_j\preceq\mathsf D_j,
\qquad \mathbf1^TM_j\mathbf1=1,\qquad
\mathbf1^T\mathsf D_j\mathbf1\le4.
\tag{Harmonic metric conditions}
\]
Write \(\langle u,v\rangle_{M_j}=u^TM_jv\).
The moving state is
\[
(A_C,B_C^{(2)},\ldots,B_C^{(L)},w_C,c_C),
\quad A_C\in\mathbb R^{q_1\times d},\quad
B_C^{(j)}\in\mathbb R^{q_j\times q_{j-1}},\quad
w_C\in\mathbb R^{q_L},\quad c_C\in\mathbb R^m.
\tag{Harmonic state}
\]
For \(v=x/\sqrt d\), set
\[
z_C^{(1)}(v)=A_Cv,\qquad
z_C^{(j)}(v)=B_C^{(j)}h_C^{(j-1)}(v),\qquad
h_C^{(j)}(v)=\phi_j(z_C^{(j)}(v)).
\]
Let \(V_C\) have columns \(h_C^{(L)}(v_a)/\sqrt m\), let
\(V_C^*=V_C^TM_L\), and put \(Q_C=V_C^*V_C\). The effective
readout and predictor are
\[
\widehat w_C=w_C+V_CQ_C^{-1}
       \left[(y-c_C)/\sqrt m-V_C^*w_C\right],\qquad
f_C(v)=\langle\widehat w_C,h_C^{(L)}(v)\rangle_{M_L}.
\tag{Harmonic corrected readout}
\]
Multiplication by \(V_C^*\) gives
\(f_C(v_a)=y_a-c_{C,a}\) exactly.
For the specified training signals use
\[
k_{C,a}^{(L)}=\widehat w_C,\qquad
\delta_{C,a}^{(j)}=\phi_j'(z_{C,a}^{(j)})\odot k_{C,a}^{(j)},\qquad
k_{C,a}^{(j)}=(B_C^{(j+1)})^*\delta_{C,a}^{(j+1)},
\]
where \((B_C^{(j+1)})^*=M_j^{-1}(B_C^{(j+1)})^TM_{j+1}\).
Define the unnormalized sample Gram by
\[
\begin{split}
K_{C,ab}={}&\langle h_{C,a}^{(L)},h_{C,b}^{(L)}\rangle_{M_L}
 +\langle\delta_{C,a}^{(1)},\delta_{C,b}^{(1)}\rangle_{M_1}v_a^Tv_b\\
&+\sum_{j=2}^L\langle\delta_{C,a}^{(j)},\delta_{C,b}^{(j)}\rangle_{M_j}
                 \langle h_{C,a}^{(j-1)},h_{C,b}^{(j-1)}\rangle_{M_{j-1}}.
\end{split}
\tag{Harmonic update Gram}
\]
The autonomous equations are
\[
\dot A_C=\frac2m\sum_a c_{C,a}\delta_{C,a}^{(1)}v_a^T,
\quad
\dot B_C^{(j)}=\frac2m\sum_a c_{C,a}\delta_{C,a}^{(j)}
                         h_{C,a}^{(j-1)T}M_{j-1},
\]
\[
\dot w_C=\frac2m\sum_a c_{C,a}h_{C,a}^{(L)},\qquad
\dot c_C=-2K_Cc_C/m.
\tag{Harmonic autonomous optimizer}
\]
These directions are specified by the optimizer. A coordinate gate need
not be self-adjoint in \(M_j\), so they are not asserted to be gradients
of the corrected predictor.

To specify the initialized matrices, choose a basis matrix \(U_j\) of
the source space with \(U_j^TU_j/n=I\), let \(I_j\) be the selected
indices, and write \(P_j=(U_j)_{I_j}\). Initialize
\[
A_C(0)=(A_0)_{I_1},\qquad w_C(0)=0,\qquad c_C(0)=y,
\]
\[
B_C^{(j)}(0)=P_j\frac{U_j^TW_0^{(j)}U_{j-1}}nP_{j-1}^TM_{j-1}.
\tag{Harmonic exact initialization}
\]
The source spaces include every initialized training feature and its
initialized forward image, all first-weight columns, and the constant.
Consequently this initialized forward pass and its training Gram equal
the corresponding selected dense ones exactly. The initialized operator
norms are at most eight. The basis matrices and dense arrays in this
formula are discarded after setup.

<a id="compact-explicit-comparison-certificate"></a>
<a id="harmonic-explicit-comparison-certificate"></a>
#### Explicit full-range comparison coefficient

Here are finite recurrences for the comparison certificate. They use only
the already defined source and fitting coefficients, and contain no
unspecified numerical constant. Put
\[
u_0=H_L^{\rm src},\quad \tau=\max_j\tau_j^{\rm src},\quad
H_r=u_0+3,\quad H_C=2H_c,\quad P_h=6u_0+9,\quad P_\delta=6\tau+9,
\]
\[
A_f=18+S^2(\tau+3)P_h,\qquad A_b=18+S^2H_rP_\delta,
\]
\[
F_1^z=1,\quad F_1^h=2s,\quad
F_j^z=9F_{j-1}^h+H_r+A_f,\quad F_j^h=2sF_j^z,
\qquad F=\max_jF_j^h.
\tag{Harmonic forward subtraction coefficients}
\]
Define
\[
d_j^E=2s(9s)^{L-j}+3H_c,\qquad
J_C=5\sqrt{F_c},\qquad
J_R=\left[(d_1^E)^2+H_r^2\sum_{j=2}^L(d_j^E)^2\right]^{1/2},
\]
\[
D_s=P_h+16zP_\delta[1+(L-1)H_r^2]
                 +(L-1)(16z)^2\tau^2P_h,
\]
\[
B_L=2s(1+6zF+32zP_h)+2t_2F_L^z,
\quad
B_j=18sB_{j+1}+2s(d_{j+1}^EzH_c+A_b)+2t_2F_j^z,
\]
\[
B_h=\sqrt L\left[H_C\max_jB_j+(\max_jd_j^E)zH_cF\right],
\qquad K_1=12F+2B_h+20z(J_C+J_R)B_h+20D_s.
\tag{Harmonic backward subtraction coefficients}
\]
The symbols \(J_C,J_R\) in this display are scalar norm coefficients;
the velocity maps in the proof are written \(\mathcal J_C,\mathcal J_R\).
Set
\[
\mathcal B_n=400z^2F_c+2zK_1+40zF
                 +64z^2K_1K_{\rm src}\sqrt{\log(en)},
\]
\[
\begin{split}
\mathcal A_n={}&[H_C(1+6zF)+3\alpha F]
 (1+\lambda^{-1/2})(e^{\mathcal B_n}-1)\\
&+6H_CzF+32H_CzP_h/\sqrt\lambda+3\alpha F+16zP_h.
\end{split}
\tag{Harmonic exact error coefficient}
\]
For any finite source horizon \(T\ge32(m/\gamma)\log(en)\) and any
source coordinate tolerance \(0<\eta\le\min(1,Y,16Ym/\gamma)\), the
constructed runtime satisfies
\[
\sup_{0\le t\le T,\ \|x\|=\sqrt d}|f_C-f_n|\le\mathcal A_n\eta,
\qquad
\|f_C-f_n\|_*\le\mathcal A_n\eta+\mathcal D e^{-\gamma T/(4m)}.
\tag{Harmonic horizon and tolerance certificate}
\]
The same construction also satisfies the fitting bound
\[
\|f_C-f_n\|_*\le(10H_c+4H_d)Y\sqrt{m/\gamma}.
\tag{Harmonic baseline certificate}
\]
All three bounds include the limiting predictors. The factor 64 in
\(\mathcal B_n\) covers the all-time carrier extension. At the original
horizon, before that extension is used, it can be replaced by 32.

<a id="compact-variable-budget-theorem"></a>
<a id="harmonic-variable-budget-theorem"></a>
#### Every supplied budget and its exact inverse

The following coefficient definitions expose all rounding and finite-width
terms. Use the original source radii
\[
c_t=\frac{a}{64YSU},\quad c_q=\min\{1/8,a/(8V)\},\quad
r_t=\frac{c_t}{\sqrt{\log(en)}},\quad
r_q=\frac{c_q}{\sqrt{\log(en)}},\quad
T_0=32\frac m\gamma\log(en),\quad \eta_0=\min(1,Y,S).
\]
For \(T\ge T_0\), let \(\alpha_T=r_t/(4T)\), and in every
dimension put \(M_n=10\max(H_L^{\rm src},\tau)\sqrt n\).
If \(d\ge2\), set
\[
b_d=2d-2,\quad D_d=2^{d+1}d^{d-2},\quad
P_T=\frac{18D_db_d!2^{b_d+1}}{\alpha_T r_q^{b_d+1}},
\]
\[
H(T,\eta)=2\log\frac{16M_nP_T}{\eta},\quad
N(T,\eta)=\sum_{j=0}^{\lfloor H(T,\eta)/r_q\rfloor}
\left[{j+d-1\choose d-1}-{j+d-3\choose d-1}\right]
\left[1+\left\lfloor\frac{H(T,\eta)-r_qj}{\alpha_T}\right\rfloor\right].
\tag{Harmonic exact coefficient count}
\]
An impossible binomial coefficient is zero. Define
\[
h_0=\max\{8\log(en),H(T_0,\eta_0)+\alpha_{T_0}+(d-1)r_q\}
\quad(d\ge2).
\]
For \(d=1\), use the two queries \(-1,1\) and instead define
\[
H_1(T,\eta)=\log\frac{64M_n}{\alpha_T\eta},\quad
N_1(T,\eta)=1+\lfloor H_1(T,\eta)/\alpha_T\rfloor,
\quad h_0=\max\{8\log(en),H_1(T_0,\eta_0)\}.
\tag{Harmonic dimension one coefficient count}
\]
In both cases set
\[
B=2m+d+1,\quad B_*=2m+d+9,\qquad
\mathcal C_d=\frac{2^{17}(9/4)^d}{d!}\frac Ua\,
 c_q^{-(d-1)}\left(\frac{Ym}{\gamma}\right)^2\log(en)^{d/2},
\]
\[
\mathcal E_0=(10H_c+4H_d)Y\sqrt{m/\gamma},\quad
\mathcal E_1=\mathcal A_n\eta_0+\mathcal D e^{-8\log(en)},\quad
\mathcal E=\max(\mathcal E_0,\mathcal E_1).
\tag{Harmonic budget coefficients}
\]
All coefficients are evaluated at the actual label size \(Y\).

For every integer \(q<n\) with \(q\ge9B\), a Harmonic model with
\(q_j\le q\) exists. Its certificate is the baseline
\(\mathcal E_0\) when
\((\max(q/9-B_*,0)/\mathcal C_d)^{1/(d+1)}<h_0\). Otherwise choose
\[
u=\left(\frac{q/9-B_*}{\mathcal C_d}\right)^{1/(d+1)}-h_0,
\qquad T=T_0+4mu/\gamma,\qquad \eta=\eta_0e^{-u}.
\tag{Harmonic construction from supplied budget}
\]
The resulting error is at most \(\mathcal E_1e^{-u}\), as well as
\(\mathcal E_0\). In particular the uniform convenient certificate is
\[
\|f_C-f_n\|_*\le
\mathcal E\min\left\{1,
 \exp\left[h_0-
  \left(\frac{\max(q/9-B_*,0)}{\mathcal C_d}\right)^{1/(d+1)}\right]
\right\}.
\tag{Harmonic exact budget certificate}
\]
For \(q\ge n\), retain every dense coordinate and take \(M_j=I_n/n\);
then the error is exactly zero. Thus the full-width branch remains
available even if \(n<9B\). If \(Y=0\), the predictor is identically
zero, and no formula dividing by \(Y\) is needed.

For the simpler domain \(18B_*\le q<n\), the certificate implies
\[
\|f_C-f_n\|_*\le\mathcal E
 \min\left\{1,e^{h_0-(q/(18\mathcal C_d))^{1/(d+1)}}\right\}.
\tag{Harmonic simplified exact budget certificate}
\]
With the deterministic logarithmic gates below, a completely numerical
activation-envelope version is
\[
\begin{split}
\|f_C-f_n\|_*\le{}&4096e^{45}\beta^{42L}\frac{Ym}{\gamma}
 \left(1+\sqrt{\frac m\gamma}\right)n e^{65\sqrt{\log(en)}}\\
&\times\exp\left[-\frac{\sqrt d}{294912\beta^{32L}}
 \left(\frac{q}{(Ym/\gamma)^2\log(en)^{d/2}}\right)^{1/(d+1)}\right].
\end{split}
\tag{Harmonic numerical budget certificate}
\]
The numerical coefficient is conservative. The exact recurrence
certificate is usually substantially smaller.

Here is an exact scalar inverse in the headline domain
\(q\ge18B_*\), including loose targets and the full-width fallback.
For a target \(\varepsilon>0\), if \(\varepsilon\ge\mathcal E_0\),
choose \(q=\min(n,18B_*)\). Otherwise put
\[
u_\varepsilon=\max\{0,\log(\mathcal E_1/\varepsilon)\},\qquad
q=\min\left\{n,\max\left\{18B_*,
 \left\lceil9[B_*+\mathcal C_d(h_0+u_\varepsilon)^{d+1}]\right\rceil
\right\}\right\}.
\tag{Harmonic exact inverse prescription}
\]
If the minimum chooses \(n\), use exact retention. Otherwise use the
analytic construction with \(T=T_0+4mu_\varepsilon/\gamma\) and
\(\eta=\eta_0e^{-u_\varepsilon}\). A sharper integer prescription
replaces the ceiling in this formula by \(9[B+4N(T,\eta)]\) when
\(d\ge2\), or \(9[B+8N_1(T,\eta)]\) when \(d=1\).
These prescriptions invert explicit sufficient certificates. They do
not assert optimal compression over other models or constructions.
If one uses the sharper full construction domain \(q\ge9B\), the
loose-target branch may instead use \(\min(n,9B)\), and the maximum
with \(18B_*\) may be omitted in the analytic branch. These are
explicitly different domain choices. A selected full-width model uses
width \(n\) even when it is below the headline baseline.

<a id="compact-original-tolerance-specialization"></a>
<a id="harmonic-original-tolerance-specialization"></a>
For the original source tolerance \(1/n\) and horizon \(T_0\), replace
64 by 32 in \(\mathcal B_n\) and consequently in \(\mathcal A_n\);
call the resulting explicit coefficient \(\mathcal A_n^{(0)}\).
Then
\[
\|f_C-f_n\|_*\le\frac{\mathcal A_n^{(0)}}n
                    +\mathcal D e^{-8\log(en)}.
\tag{Harmonic original tolerance specialization}
\]
It needs the original source domain, without the analytic-extension
gates. For \(d\ge2\) its source rank is at most \(B\) plus
\[
\frac{2^{20}9^d}{d!}\frac Ua c_q^{-(d-1)}
            (Ym/\gamma)^2\log(en)^{3d/2+1};
\]
for \(d=1\), replace this expression by
\(8\cdot514\cdot1024(U/a)(Ym/\gamma)^2\log(en)^{5/2}\).
Substitution in the retained inventory preserves the original
\(\log(en)^{3d+2}\) storage order, including the exact initialization
term. On the optional smaller cap \(Y\le(\gamma/m)\beta^{-30L}\),
the same original construction also retains the numerical refinements
\[
\|f_C-f_n\|_*\le10\beta^{40L}\frac{Ym}{\gamma}
  \left(1+\sqrt{\frac m\gamma}\right)\frac{e^{2\sqrt{\log(en)}}}{n}
 \le250\beta^{40L}Y(1+m/\gamma)^2n^{-1/2}.
\tag{Harmonic optional small cap refinement}
\]

<a id="compact-storage-count"></a>
<a id="harmonic-storage-count"></a>
#### Learned coordinates, fixed storage and gates

For the actual selected dimensions, the exact moving-state count is
\[
dq_1+\sum_{j=2}^Lq_jq_{j-1}+q_L+m
\le(L-1)q^2+q(d+1)+m.
\tag{Harmonic exact learned count}
\]
The effective readout is computed from this state and is not a second
independent learned vector. The fixed symmetric metrics require
\(\sum_jq_j(q_j+1)/2\) real entries if packed; retaining diagonal
comparison metrics uses another \(\sum_jq_j\). Data cost \(m(d+1)\).
Optional metric inverses, initial copies, training feature/backward arrays
and current Gram/solve caches are included in the following explicit
upper inventory for an integer source-dimension bound \(R\):
\[
\operatorname{storage}\le1020(L+1)R^2+10m(d+1).
\tag{Harmonic all retained inventory}
\]
This is an upper bound on the named inventory, not an exact equality for
every possible cache layout. In the analytic branches one can take
\(R=B+4N(T,\eta)\) or \(R=B+8N_1(T,\eta)\), respectively. Whenever
the actual integer rank is at most \(q/9\), the same inventory is at
most \(13(L+1)q^2+10m(d+1)\). Original-width coefficients, quadrature
arrays, jets, bases and initialized dense arrays are absent from retained
storage. Counts concern real coordinates, not bit precision, setup work,
linear-solve work or a numerical ODE solver's chosen work space.

The width qualifications consist of the shared dense initialization and
source probability event, the original deterministic source gates, and
the following explicit additions. In particular retain
\(n^{-1}\le\eta_0\), the source gate
\[
\sqrt{\log(en)}\ge c_t\max\{8,\lambda,
              4\mathcal K/\log2,32YSD_W\},\quad
D_W=\max\{\tau_1^{\rm src},\max_{j\ge2}\tau_j^{\rm src}H_{j-1}^{\rm src}\}.
\tag{Harmonic original radius gate}
\]
For \(d\ge2\), write
\[
C_d^*=16\cdot128\cdot18M_0D_db_d!2^{b_d+1}
          \lambda^{-1}c_t^{-1}c_q^{-(b_d+1)},\qquad M_0=M_n/\sqrt n,
\]
and retain
\[
\log C_d^*\le\log(en),\quad
(d+1)\log\log(en)\le\log(en),\quad
(d-1)c_q/\sqrt{\log(en)}\le1,\quad \alpha_{T_0}\le1.
\tag{Harmonic original counting gates}
\]
For \(d=1\), retain the temporal gate \(\alpha_{T_0}\le1\) and use
\[
\log\frac{8192M_0}{c_t\lambda}\le\log(en).
\tag{Harmonic dimension one gate}
\]
Finally put
\[
b_n=\min\left\{\frac14,\frac{SH_L^{\rm src}}4,
                 \frac{a}{8\sqrt n\max_jP_j^{\rm src}}\right\},
\]
\[
C_L^k=1,\qquad C_j^k=S\tau_{j+1}^{\rm src}+10sC_{j+1}^k
           +10t_2SP_{j+1}^{\rm src}k_{j+1}^{\rm src},\qquad
C_{\rm carrier}=\max_jC_j^k,
\]
and impose
\[
\left(2Y/\sqrt\lambda+8Y\sqrt{\mathcal K}\,r_t\right)(en)^{-16}
          <b_n/2,
\qquad
\frac{2C_{\rm carrier}Y}{\sqrt\lambda}\,n(en)^{-16}
          \le K_{\rm src}S\sqrt{\log(en)}.
\tag{Harmonic analytic extension gates}
\]
These inequalities are eventual at every fixed admissible problem. They
are independent of \(q\), \(T\), and target accuracy. Thus one event
at a fixed width supports all the Harmonic budgets and tolerances above;
there is no union over new horizon-dependent Gaussian events.



<a id="computational-costs"></a>
### Computational costs at supplied orders

This section distinguishes three operations. **Warmup** is all one-off
work needed to create the model, including generation of its dense
reference when not supplied. **Training** is one full-batch evaluation
of the autonomous vector field, or a fixed-stage explicit numerical
step, after the warmup-only arrays have been discarded. **Query** is
one new passive input at a fixed, inference-ready model state. Warmup
and training memory mean **total peak resident memory**; query memory
means **additional peak workspace**, excluding the resident model and
the supplied input. These definitions apply to every cost table.

#### Arithmetic, activation and numerical qualifications

The bounds count classical dense scalar arithmetic, with scalar square
root and the fixed elementary functions used in the continuation and
geometric recurrences treated as unit primitives. They are upper bounds
for the specified implementations, not optimal complexity or wall-clock
measurements. Every big-O constant in this section is numerical and
implementation-dependent only: it hides no dependence on
\(n,m,d,L,q,K,p,J,N_x,N_t,\gamma,Y,\beta,\delta\), activation
evaluation cost, solver stage count or working precision.

General activations are not unit-cost oracles by implication of
analyticity. The tables count non-activation arithmetic; add the
explicit activation calls and jet-composition costs stated below.
Generating a fresh reference also requires exactly
\(nd+(L-1)n^2\) independent Gaussian draws. The displayed arithmetic
bounds include allocation/filling, but the sampling implementation's
time and scratch memory must be added. In the customary unit-cost
sampling model this adds \(O((L-1)n^2+nd)\) work and \(O(1)\)
sampler scratch. If the reference is supplied, omit generation work
but not its resident memory.

A numerical step with \(s\) vector-field stages has \(s\) times the
per-stage work, plus state updates and any cache refresh. Only when
\(s\) is fixed can it be absorbed in big-O; a fixed-stage method uses
a fixed number of state-sized work arrays. Implicit solves, adaptive
rejections, the number of steps, roundoff and the accuracy of numerical
integration are not bounded here. In particular the trajectory-error
theorems concern the continuous flows; this section does not promote
them to finite-step error theorems. Feature-Gram solves are evaluated
where the stated positive-gap conditions hold. Exact rank detection
and exact arithmetic in coordinate selection are part of the operation
model, not floating-point stability assertions.

For the clean common table take \(n\ge\max(m,d)\), allowed by the shared
eventual-width convention. Retain the existing Harmonic compressed
domain \(q\ge18(2m+d+9)\) when simplifying its runtime counts.
No comparison between \(n\) and any internal setup order is assumed.
Define, locally throughout this cost section,
\[
P=(L-1)n^2+n(d+1).
\tag{cost-dense-size}
\]

<a id="cost-forward-table"></a>
#### Common forward cost table: supplied \(n,q\)

The Harmonic warmup envelopes \(\mathcal T_{\rm H},\mathcal M_{\rm H}\)
are defined completely below and retain all supplied setup orders and
activation costs. No inverse or optimized order is used in this table.

| Model and operation | Arithmetic work | Peak memory in real words |
|---|---:|---:|
| Dense warmup | \(O(P)\), plus Gaussian draws | \(O(P+m(d+1))\) |
| Dense training stage | \(O(mP)\) | \(O(P+Lmn+m(d+1))\) |
| Dense single query | \(O(P)\) | \(O(n)\) additional |
| Legendre warmup | \(O(P+mnd+(L-2)mn^2+(L-1)mn+Lmnq)\), plus Gaussian draws | \(O(P+Lmnq+m(d+1))\) |
| Legendre training stage | \(O(mP+Lnm^2q+Lnmq)\) | \(O(P+Lnmq+m(d+1))\) |
| Legendre single query, factor representation | \(O(P+Lnmq)\) | \(O(n)\) additional |
| Harmonic warmup | \(O(\mathcal T_{\rm H})\), plus Gaussian draws | \(O(\mathcal M_{\rm H})\) |
| Harmonic training stage, including inference-cache refresh when required | \(O(Lmq^2+m^3)\) | \(O(Lq^2)\) |
| Harmonic single query, refreshed readout cache | \(O(Lq^2)\) | \(O(q)\) additional |

Dense and Legendre training add at most a fixed numerical multiple of
\(Lmn\) calls each to activation values and first derivatives. Their
queries add \(Ln\) activation-value calls and no activation-derivative
calls. Legendre warmup adds \((L-1)mn\) activation-value calls; it need
only compute initial features through layer \(L-1\), so at \(L=2\)
the displayed warmup feature calculation contains no dense-mixer
application. Harmonic training adds \(m\sum_jq_j\le Lmq\) calls each
to values and first derivatives per vector-field evaluation, and a
refresh adds a comparable number of value calls. Its query adds
\(\sum_jq_j\le Lq\) value calls. Add the chosen routines' work and
peak scratch for these calls; analyticity alone gives no uniform
arithmetic bound on those routines.

Legendre applies its fixed mixers plus the \(mq\) correction factors
without materializing reconstructed dense matrices. Moment-prefix sums
are accumulated once, not recomputed for every prefix. Factor products
can be streamed, avoiding an \(m^2q\)-word temporary.
An optional fixed-snapshot cache of reconstructed dense mixers costs
\(O((L-1)n^2mq)\) work to refresh and \(O((L-1)n^2)\) additional
resident memory; afterward queries cost \(O(P)\), with \(O(n)\)
additional workspace. Refresh whenever moments or the clock change.
It is not one-off initialization if training continues.

The Harmonic inference-ready cache is the vector
\(M_L\widehat w_C\), so a query is an ordinary hidden forward pass
and a final dot product. Refresh it after any relevant model-state
change. A refresh uses the current training features and feature-Gram
solve and has at most the order of one training-stage cost. An
implementation can charge a final refresh to training/model preparation;
it cannot both omit refresh and claim an \(m\)-independent query cost.
At initialization the cache is exactly zero.

#### Unsimplified Harmonic runtime and peak workspace

For the actual layer widths \(q_j\le q\), the training arithmetic is
\[
O\!\left(
m\left[q_1d+\sum_{j=2}^Lq_jq_{j-1}+\sum_{j=1}^Lq_j^2\right]
 +q_Lm^2+m^3\right).
\tag{cost-harmonic-training}
\]
Its total peak memory after discarding warmup-only arrays is
\[
O\!\left(
q_1d+\sum_{j=2}^Lq_jq_{j-1}+\sum_{j=1}^Lq_j^2
 +m\sum_{j=1}^Lq_j+m^2+m(d+1)\right).
\tag{cost-harmonic-training-memory}
\]
This includes model parameters, fixed metrics and inverse caches,
data, feature/backward arrays, parameter directions and the moving
feature-Gram factorization. It does not include any dense-reference
array, jet, coefficient block or source basis. The \(m^3\) term is
the ordinary factorization of the current \(m\)-by-\(m\) feature Gram;
it is not a hidden repeated inversion of the fixed layer metrics.
Although \(m^3\le mq^2\) in the compressed domain, it remains visible.

For a single inference-ready query, arithmetic and additional peak
workspace are respectively
\[
O\!\left(q_1d+\sum_{j=2}^Lq_jq_{j-1}+q_L\right),
\qquad O\!\left(\max_jq_j\right).
\tag{cost-harmonic-query}
\]
Use rolling feature buffers; normalize the first preactivation after
multiplication by the supplied input, avoiding a separate normalized
input copy. Fixed metrics are applied to batch vectors before
forming weight directions. Their inverse caches are created during
warmup, so there is no \(Lq^3\) per-stage cost. The
[cost proof](#computational-cost-proofs) gives an exact matrix-free
formula for the update-Gram action; it is not differentiation of the
corrected predictor.

<a id="harmonic-warmup-cost"></a>
#### Harmonic warmup with all internal orders exposed

The independent supplied setup resolutions are:

| Symbol | Supplied meaning |
|---|---|
| \(K\ge1\) | Highest initial time-derivative order computed |
| \(p\ge0\) | Highest retained temporal Chebyshev degree |
| \(J\ge0\) | Highest retained spherical-harmonic degree |
| \(N_x\ge1\) | Total number of spatial quadrature nodes |
| \(N_t\ge1\) | Number of temporal quadrature nodes |

The source horizon \(T\), continuation map, quadrature nodes/weights
and retained joint mode set must also be specified. The default costed
rule is the elementary angular Riemann rule used in the source proof;
the additional construction and node/weight storage of a different
rule must be charged separately. These are not
additional runtime state after initialization. On the analytic branch
of the forward theorem, the supplied \(q\) prescribes a horizon and
source tolerance; a valid implementation must choose the setup
resolutions to meet that tolerance. This cost analysis does not
identify \(K,p,J,N_x,N_t\) with \(q\), or choose any of them.
In particular \(N_x=H\), \(N_t=p+1\), and \(p\le K\) are not
asserted: the last relation need not hold after continuation in the
nonlinear time coordinate.

For \(d\ge2\), put
\[
h_j={j+d-1\choose d-1}-{j+d-3\choose d-1},\qquad
H=\sum_{j=0}^Jh_j
 ={J+d-1\choose d-1}+{J+d-2\choose d-1},
\tag{cost-harmonic-mode-count}
\]
with impossible binomials zero. If the temporal cutoff at spherical
degree \(j\) is \(p_j\le p\), count all \(h_j\) basis functions there.
A sufficient source-generator count per layer is
\[
R=2m+d+1+4\sum_{j=0}^J(p_j+1)h_j
 \le2m+d+1+4(p+1)H.
\tag{cost-source-generator-count}
\]
Use the actual smaller number of present source families at boundary
layers when available. For \(d=1\), there are two input points,
no nontrivial angular degree, and the corresponding bound is
\(R=2m+d+1+8(p+1)\); one can use \(H=2\) in the rectangular
cost bounds. The actual largest source rank is \(r\le\min(n,R)\).
The deterministic selector guarantees the requested budget when
\(9r\le q<n\); \(9R\le q\) is a stronger sufficient test, not a
necessary rank condition. No successful compressed construction is
asserted for an arbitrary incompatible combination of supplied orders.

The following counts assume all initial dense matrices are resident,
training jets are shared, and spatial nodes are streamed. Here and
below using \(K\) instead of \(K+1\) in big-O is valid because
\(K\ge1\).

| Jet representation | Arithmetic, excluding scalar activation composition | Jet-stage peak memory |
|---|---:|---:|
| Materialized dense parameter coefficients | \(O(P(m+N_x)K^2)\) | \(O(PK+LmnK)\) |
| Factored gradient increments, no contraction cache | \(O(P(m+N_x)K+Lnm(m+N_x)K^3)\) | \(O(P+LmnK)\) |
| Factored increments with contraction caches | \(O(P(m+N_x)K+Lm(m+N_x)K^2(n+K))\) | \(O(P+LmnK+Lm^2K^2)\) |

These are alternative executions of the same coefficient recursion.
Choose an implementation for the available memory; no row is claimed
uniformly fastest. No parameter-Hessian tensor is materialized.
The \(N_x\) query jets reuse the actual empirical-training jets;
designed query points do not replace training samples in the gradients.
Warmup is initialization-only but data- and label-dependent.

For arbitrary activations, define the following **implementation costs**,
not approximation parameters. Let \(a_{\rm on}(K),b_{\rm on}(K)\)
bound arithmetic and peak workspace for one scalar activation and
its derivative in the sequential training-jet recursion, including
persistent series state and derivative-generation scratch; let
\(a_{\rm off}(K),b_{\rm off}(K)\) bound full-series composition and
scratch for a passive query. Each includes the chosen activation's
scalar-derivative generation algorithm. Then add
\[
\mathcal A_{\rm time}
=Ln[ma_{\rm on}(K)+N_xa_{\rm off}(K)],\qquad
\mathcal A_{\rm memory}
=Lmn b_{\rm on}(K)+b_{\rm off}(K).
\tag{cost-activation-backend}
\]
Take maxima over the finitely many layer activations if their
implementations differ. A fixed-size differential recurrence, such
as for tanh, permits \(a_{\rm on},a_{\rm off}=O(K^2)\) and
\(b_{\rm on},b_{\rm off}=O(K)\). For a general analytic activation
with its scalar Taylor coefficients supplied, a direct online power
triangle costs \(O(K^3)\) time and \(O(K^2)\) persistent words;
offline truncated Horner composition costs \(O(K^3)\) time and
\(O(K)\) scratch. Scalar derivative generation is additional to
these latter composition bounds. The theorem's analytic envelope
does not bound that algorithmic cost.

Scalar geometry can be implemented without expanding all harmonics
in Cartesian monomials. The recursive separated orthonormal basis
in the cost proof gives the following sufficient overhead envelopes.
They include the source proof's elementary Riemann nodes/weights,
generated from supplied grid indices in \(O(d)\) work per spatial
node and \(O(1)\) per temporal node. They do not bound construction
of an arbitrary quadrature rule:
\[
\mathcal B_{\rm time}=
\begin{cases}
N_t+N_x,&d=1,\\
N_x(J+1)+N_t,&d=2,\\
d(J+1)^2+dN_x[(J+1)^2+H]+N_t,&d\ge3,
\end{cases}
\quad
\mathcal B_{\rm memory}=
\begin{cases}
1,&d=1,\\
J+1,&d=2,\\
d[(J+1)^2+H],&d\ge3.
\end{cases}
\tag{cost-scalar-geometry}
\]
The \(d=1\) case uses the two sphere points, not an angular grid.
The geometry envelopes are retained explicitly rather than hidden
inside an activation or data constant.

For cached factored jets and temporal-first streamed projection,
define the complete arithmetic and peak-memory envelopes
\[
\begin{split}
\mathcal T_{\rm H}={}&
P+P(m+N_x)K+Lm(m+N_x)K^2(n+K)\\
&+(p+1)K(N_t+K)
 +LnN_x(p+1)(K+H)\\
&+LnRr+Lnr^3+Ln^2r+Lq^2r
 +\mathcal A_{\rm time}+\mathcal B_{\rm time},
\end{split}
\tag{cost-harmonic-warmup-time}
\]
\[
\begin{split}
\mathcal M_{\rm H}={}&
P+LmnK+Lm^2K^2+LnR+Lq^2+(p+1)K+m(d+1)\\
&+\mathcal A_{\rm memory}+\mathcal B_{\rm memory}.
\end{split}
\tag{cost-harmonic-warmup-memory}
\]
All quantities on the right have been defined. The actual work and
peak words are \(O(\mathcal T_{\rm H})\) and
\(O(\mathcal M_{\rm H})\), plus the separately specified Gaussian
sampling cost/scratch. These envelopes include creation of the dense
reference, source construction, selection, model assembly and fixed
metric inverse caches. They are not bounds solely in \(q\).

The universal temporal map costs \(O((p+1)K(N_t+K))\) once,
not once per neuron. Projection then costs
\(O(LnN_x(p+1)(K+H))\). Orthogonalization must process all \(R\)
generators, costing \(O(LnRr)\); the proof's deterministic selector
costs \(O(Lnr^3)\). Dense basis-to-basis mixer compression costs
\(O(Ln^2r)\) in general even though some paired actions can be
reused. Metric and retained-matrix assembly costs \(O(Lq^2r)\).
The \(LnR\) memory term retains all source-coefficient blocks and
therefore introduces no unreported query recomputation.

**Alternative executions.** Replace the cached-jet contributions by
either other row of the jet table when advantageous. Spatial-first
projection costs \(O(LnK[N_xH+(p+1)H])\), with \(O(LnKH)\)
intermediate words instead of temporal-first projection. Coefficient
blocks of size \(b\) can replace \(LnR\) storage by \(Ln(r+b)\);
without stored nodal jets this requires up to
\(\lceil R/b\rceil\) passes over the passive-query jet and temporal
projection calculations, together with streamed node/basis evaluation
unless separately cached, not repeated training-jet construction.
On a uniform circle grid supporting the retained modes, FFT angular
projection takes \(O(Ln(p+1)N_x\log(eN_x))\) work after temporal
projection; a direct batched implementation additionally stores
\(O(Ln(p+1)N_x)\) nodal values. These are explicit time-memory
tradeoffs, not unproved simultaneous minima.

The initialization-only baseline branch can skip source expansions
that it does not use. The full-width exact branch can simply retain
the dense network and use the dense costs. The formulas above concern
the genuine analytic compressed branch and are upper bounds, not
necessary work for every special dataset.

#### Accuracy inversion does not determine an efficient warmup

Insert the inverse interface's prescribed \(n\) or \(q\) into the
forward cost table; no other substitution is licensed automatically.
For Harmonic, the setup orders must additionally satisfy the
time/spatial-tail, initial-jet and quadrature accuracy conditions in
the source construction, and the resulting source rank must fit the
budget. The note proves finite suitable jets and quadrature but does
not derive an efficient joint choice for \(K,N_x,N_t\). Consequently
the warmup entries in the inverse and fixed-problem tables retain
\(\mathcal T_{\rm H},\mathcal M_{\rm H}\) with those arguments
exposed; they are not renamed polylogarithmic setup bounds.

Nor do arithmetic bounds certify finite-precision execution.
Continuation coefficients, source rank tests and small positive
selection weights can require additional precision. No sufficient
bit precision, overall integration step count, or end-to-end
wall-clock efficiency follows from the retained-storage theorem.
The new analysis changes no activation class, label cap, probability
event or trajectory-error certificate.

<a id="integrated-proofs"></a>
## III. Proofs

The proofs are grouped by dependency, with every specialized construction
used above included here. The dense initialization/fitting argument uses
only finite-dimensional Gaussian estimates and deterministic energy.
The source proof adds finite deletion, conditional Gaussian comparison,
moment-budget removal and complex continuation. The later dense upper
and lower proofs, and both compressed-model proofs, use that shared source.

The dependency order is not circular: dense fitting does not use source
analyticity; the source starts from dense fitting; the deterministic
late-time extension uses the source only through its original finite
horizon. The Legendre comparison uses that extension's real carrier bound,
and Harmonic's variable-horizon construction uses its full analytic domain.
The complete extension is in
[the Harmonic proof](#harmonic-analytic-extension-proof) and its explicit
gates are in [the common construction inventory](#harmonic-storage-count).

<a id="source-foundations"></a>
### Source foundations: explicit coefficients and the probabilistic bridge

The coefficients in this section are local proof coefficients, not extra
model parameters or adjustable approximation orders. The scalar
\(\lambda=\gamma/m\) is never capped at one. The activation bounds are
\(b=\max_j|\phi_j(0)|\),
\(s=\max\{1,\sup_{j,|\operatorname{Im}z|\le a/2}|\phi_j'(z)|\}\), and
\(t_2=\max\{1,\sup_{j,|\operatorname{Im}z|\le a/2}|\phi_j''(z)|\}\).
They obey \(1+b,s,t_2,16/a\le\beta\). In numbered form the definitions are
\[
b=\max_j|\phi_j(0)|,\quad
s=\max\{1,\sup_{j,|\operatorname{Im}z|\le a/2}|\phi_j'(z)|\},\quad
t_2=\max\{1,\sup_{j,|\operatorname{Im}z|\le a/2}|\phi_j''(z)|\}.
\tag{S.2}
\]

There is an unavoidable distinction between an explicit error coefficient
and an effective probability threshold. The original source argument
proves probability tending to one by sending width to infinity at each
fixed empirical moment degree and only then taking the infimum over those
degrees. It does **not** specify a numerical sufficient width as a function
of confidence. None is asserted here. The deterministic source coefficients,
label allowance, radii and additional width inequalities below are explicit.
The finite-deletion argument uses eventual domination of fixed logarithmic
factors; it is the source of the remaining qualitative width quantifier.

<a id="source-local-insertion"></a>
#### Finite deletion and its local comparison

Here is the local probabilistic argument used by the source estimates.
It is included to replace the former import of a specialized insertion
theorem. Fix a number \(p\) of deleted neurons in one layer; it is fixed
before width tends to infinity. Delete the activations themselves, leaving
rectangular retained matrices and the original normalization \(n\).
Setting their preactivations to zero is not the same operation, because
\(\phi_j(0)\) need not vanish. Each cavity is initialized, stopped and
continued from its own retained initialization. A reference whose own
initialization fails its prescribed event is assigned the zero coefficient
path. This is done before conditioning on any omitted Gaussian variable.

Use mobility coordinates
\(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\) and
\(F_a=nf_a\). At an interior deleted layer \(j\), write the incoming
initialized row transposes as \(y_i\) and the outgoing columns as \(x_i\).
Conditional on the retained initialization these vectors are independent
\(N(0,I/n)\). The exact retained equation, with a forward source \(e_a\)
at layer \(j+1\) and a reverse source \(q_a^{\rm rev}\) at layer \(j-1\), is
\[
\dot\Theta=-\frac2m\sum_a r_a
 \left[\nabla_\Theta F_a(\Theta,e)
 +(D_\Theta h_a^{(j-1)})^\top q_a^{\rm rev}\right],
\qquad r_a=F_a(\Theta,e)/n-y_a.
\]
The actual sources are
\[
e_a=\sum_{i\in I}W^{(j+1)}_{:,i}h_{a,i}^{(j)},\qquad
q_a^{\rm rev}=\sum_{i\in I}W^{(j)\top}_{i,:}\delta_{a,i}^{(j)}.
\]
Indeed differentiating the retained forward prediction misses exactly
the paths through a deleted activation; their chain-rule contribution is
the second term displayed above. The reverse source is not an artificial
addition to the forward prediction or its residual.

On the stopped source domain, a deleted activation and response are
bounded by a fixed polynomial in \(\log(en)\); their coordinate speeds
are bounded by \(\sqrt n\) times such a polynomial. Integrating their
rank-one updates shows that the learned part of each deleted row or
column, multiplied by its control, has Euclidean norm bounded by
\(n^{-1/2}\) times a fixed polynomial in \(\log(en)\).
The same assertion holds on the short complex segments: their total
residual activity is bounded. These adaptive remainders are estimated
pathwise and are never treated as independent Gaussian variables.

For completeness, the derivative structure that prevents a hidden
parameter-dimension factor is as follows. For a parameter variation \(U\),
write \(Z_a^{(j)}U=D_\Theta z_a^{(j)}[U]\). Its recurrence is
\[
Z_a^{(1)}U=U_Av_a,\qquad
Z_a^{(j)}U=(U_j/\sqrt n)h_a^{(j-1)}
 +W^{(j)}\operatorname{diag}(\phi_{j-1}')Z_a^{(j-1)}U.
\]
The operator coefficients are bounded by the forward RMS recurrences
given below. The exact Hessian is
\[
\begin{split}
D^2F_a[U,V]={}&U_w^\top\operatorname{diag}(\phi_L')Z_a^{(L)}V
 +V_w^\top\operatorname{diag}(\phi_L')Z_a^{(L)}U\\
&+\sum_{j=1}^L(Z_a^{(j)}U)^\top
 \operatorname{diag}(k_a^{(j)}\phi_j'')Z_a^{(j)}V\\
&+\sum_{j=2}^L\frac{\delta_a^{(j)\top}}{\sqrt n}
 \left[U_j\operatorname{diag}(\phi_{j-1}')Z_a^{(j-1)}V
       +V_j\operatorname{diag}(\phi_{j-1}')Z_a^{(j-1)}U\right].
\end{split}
\]
There is one carrier in each curvature diagonal, not a product of
carriers. All non-diagonal factors have bounded operator norm and factor
through a hidden space of dimension at most \(n\). Adding preactivation
ports makes \(D_\Theta\delta_a^{(j)}\) a subblock of this same Hessian.
The normalized Schatten estimates below therefore apply to both
endpoints of a response trace.

Along the zero-source cavity the exact variational generator is
\[
-\frac2{mn}\sum_a\nabla F_a\nabla F_a^\top
-\frac2m\sum_a r_aD^2F_a.
\]
The first term has a contractive real-time propagator. On the short
non-real or backwards pieces its norm cost is bounded by the explicit
complex Gram estimate below. The second term is controlled by the
stopped carrier budget and total residual activity. The specified source
allowance gives propagator norm at most \(n^{1/1000}\) eventually; in
particular the coefficient multiplying \(\log n\) is small before width
is enlarged. Increasing width alone is not used to absorb that coefficient.

If \(d_a=\delta_a^{(j+1)}\), the three linear source maps are exactly
\[
-\frac2{mn}\nabla F_a d_a^\top,\qquad
-\frac2m r_a(D_\Theta d_a)^\top,\qquad
-\frac2m r_a(D_\Theta h_a^{(j-1)})^\top.
\]
Variation of constants applies these maps to \(x_i\) times its forward
control and \(y_i\) times its reverse control. For each deterministic
choice of controls the resulting linear maps, and the finite forward,
backward and passive-query derivative graphs, have operator norm at most
\(n^{1/200}\) eventually. This follows by multiplying the preceding
\(n^{1/1000}\) bound by the finite logarithmic factors in these recurrences.
The number of layers, samples and deleted roots is fixed here.

Each scalar Gaussian coordinate consequently has variance at most
\(n^{-99/100}\) eventually. The elementary Gaussian bound at threshold
\(n^{-1/10}/2\) then has exponent a positive fixed multiple of
\(n^{79/100}\). Centered quadratic forms obey the same scale. To verify
this assertion, diagonalize the real symmetric part of a matrix \(R\).
For \(g\sim N(0,I)\) and \(|2u\lambda_i(R)|<1\),
\[
\mathbb E\exp\{u(g^\top Rg-\operatorname{tr}R)\}
 =\prod_i e^{-u\lambda_i(R)}(1-2u\lambda_i(R))^{-1/2}.
\]
Using \(-\log(1-v)-v\le v^2/[2(1-|v|)]\), followed by the
exponential Markov bound and optimization over \(u\), controls the
tail by the smaller of the squared-threshold/HS-norm and
threshold/operator-norm scales. Divide \(g\) by \(\sqrt n\).
The HS norm is at most \(\sqrt n\|R\|_{\rm op}\). An independent-root
bilinear form uses the symmetric off-diagonal block matrix
\(\bigl(\begin{smallmatrix}0&R/2\\R^\top/2&0\end{smallmatrix}\bigr)\).
Real and imaginary parts give the complex estimates. These steps are
conditional on the cavity, not on the full-network survival event.

Approximate scalar controls uniformly to accuracy \(n^{-1/8}\): sample
time at that accuracy divided by the coordinate Lipschitz bound and
round the sampled values. The logarithm of the number of controls is
at most \(n^{5/8}\) times a fixed polynomial in \(\log(en)\).
It is at most \(n^{13/20}\) eventually, while the Gaussian exponent
is at least \(n^{39/50}\) eventually. The interpolation error has
size at most \(n^{-1/8+1/200}\) times a fixed Gaussian-root norm,
which is smaller than \(n^{-1/10}/2\) eventually. Polynomially fine
terminal-time and query-frame grids add only a fixed multiple of
\(\log n\) to log cardinality. Their off-grid control follows from
the same finite derivative graph. A union bound, including all sets of
\(p\) deleted neurons, therefore leaves failure at most
\(e^{-n^{7/10}}\) eventually. On this event every needed linear
vector has Euclidean norm at most \(n^{1/100}\), and every needed
linear coordinate has magnitude at most \(n^{-1/10}\). The Euclidean
bound also follows directly from the map norm and the norm of the
fixed number of Gaussian roots. Only after this uniform event has
been established are the actual adaptive controls substituted.

Here is the nonlinear remainder check. Write the full parameter increment
as its linear response plus a remainder of norm \(u\le n^{-1/25}\).
The two basic vector remainders are
\[
n^{-9/100}+n^{-1/10}u+u^2,
\qquad
n^{-1/2}(n^{2/100}+n^{1/100}u+u^2).
\]
The first follows from
\(\|v\odot v\|_2\le\|v\|_\infty\|v\|_2\), with the
linear coordinate bound just proved; mixed terms use
\(\|v\odot U\|_2\le\|v\|_\infty\|U\|_2\).
The second is the matrix cross term, which retains the factor
\(1/\sqrt n\) from mobility coordinates. A reference feature multiplying
a changed matrix is controlled by its RMS; bounded activation values
are never used. Induction through the forward recursion and then the
backward recursion preserves these bounds up to fixed logarithmic factors.
The changed gate always multiplies the reference carrier or the already
small linear carrier, not an uncontrolled changed carrier.

For the reverse source one may check this separately with
\(\psi_y(\Theta)=y^\top h_a^{(j-1)}(\Theta)\).
Its reference probe carriers have Euclidean norm bounded independently
of width and coordinate size at most \(n^{-1/10}\). Along the joining
parameter segment, subtracting the probe recursion bounds their change
by fixed logarithmic factors times
\[
n^{-1/10}(n^{1/100}+u)+n^{-1/2}(n^{1/100}+u).
\]
Its Hessian applied to the parameter increment therefore contributes
\(n^{-8/100}+n^{-9/100}u+n^{-1/10}u^2\), times the residual and fixed
logarithmic factors. Residual adaptation contributes the unweighted
matrix-cross scale above: its scalar Taylor remainder is a Hessian
quadratic form divided by \(n\), while the reference gradient has norm
of order \(\sqrt n\). Thus the largest integrated forcing powers are
\(n^{-8/100}\) and \(u^2\). Integration over a logarithmic horizon
and propagation by \(n^{1/1000}\) leave a quantity
\(o(n^{-1/25})\). A first-exit argument closes the assumed remainder
bound. The resulting retained coordinate differences are at most
\(n^{-1/30}\) eventually; relevant whole-vector differences are at
most \(n^{1/100}\) times a fixed constant. Joining scalar segments
remain inside the safe strip because their coordinate increments vanish.

At the first layer there is no reverse source. At the top there is no
outgoing Gaussian root. Instead, if
\(d_a=n^{-1}\sum_{i\in I}w_i h_{a,i}^{(L)}\), the retained equation is
\[
-\frac2m\sum_a(r_a^0+d_a)
 \left[\nabla F_a^0+(D h_a^{(L-1)})^\top q_a^{\rm rev}\right].
\]
The offset multiplies both terms. Its gradient contribution is
\(n^{-1/2}\) times a fixed logarithmic polynomial; its reverse contribution
is smaller. Both fit the same remainder bound. The exact top readout
equation and the incoming-root forward trace then replace the missing
outgoing-root calculation.

Every entire singleton/common-cavity difference excludes the root against
which it is paired. Project that entire difference onto its deterministic
Euclidean ball of radius a fixed constant times \(n^{1/100}\), before
restricting to the successful common prefix. Projection is nonexpansive
and preserves independence. Its Gaussian pairing radius is a fixed
constant times \(n^{-49/100}\). The activity modulus and short complex
segment estimates below imply that its supremum and every fixed
exponential moment correction vanish. This is why conditioning on
root-dependent full survival is unnecessary.

This proof gives eventual bounds for each fixed deletion count. It does
not quantify their onset and does not allow the deletion count to grow
with width. The next argument takes the width limit first at each fixed
moment degree, which is exactly the quantifier this local result supplies.

<a id="source-explicit-recurrences"></a>
#### Explicit source recurrences, budget removal and analytic domain
In this source section only, \(H_j,P_j,k_j,f_j,q_j\) are the source
recurrence coefficients. They are denoted \(H_j^{\rm src},P_j^{\rm src},
k_j^{\rm src},f_j^{\rm src},q_j^{\rm src}\) elsewhere in this document.
In particular \(q_j\) here is not the supplied compression order \(q\).

The dense rank-one equations, with \(v_a=x_a/\sqrt d\), are
\[
\dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\quad
\dot W^{(j)}=-\frac2{mn}\sum_a r_a\delta_a^{(j)}
                         h_a^{(j-1)\top},\quad
\dot w=-\frac2m\sum_a r_ah_a^{(L)}. \tag{S.1}
\]
The independently proved dense-fitting theorem supplies the physical
operator caps below nine and, conservatively,
\[
\rho(t)=\|r(t)\|_2/\sqrt m\le Ye^{-\lambda t/4}.\tag{S.3}
\]
Put
\[
S=16Y/\lambda,\qquad
T=32\lambda^{-1}\log(en),\qquad d\nu=2\rho\,|dz|. \tag{S.4}
\]
Here \(d\nu\) is a contour integration measure, not a new training clock.
Its real mass is at most \(S/2\). The source-domain proof uses this \(T\);
the later analytic-tail lemma extends this domain without changing its
radii or introducing an order-dependent stochastic event.

Linear growth is the exact bound \(|\phi_j(z)|\le b+s|z|\) on the safe
half-strip. If
\(s_{\rm full}=\max\{1,\sup_{j,|\operatorname{Im}z|<a}|\phi'_j(z)|\}\),
Cauchy's formula gives the bound
\((h-1)!s_{\rm full}(4/a)^{h-1}\) for derivatives of order \(h\ge2\)
on that half-strip. Those higher-derivative coefficients occur only in
the qualitative local-width threshold; the explicit recurrences use
\(b,s,t_2,a\).

##### S.2. Explicit RMS, derivative, and trace coefficients

Use the complex operator caps ten and query input norm at most two.
Define the forward feature RMS bounds
\[
H_1=\max(1,b+20s),\qquad H_j=\max(1,b+10sH_{j-1})\quad(j\ge2).
                                                               \tag{S.5}
\]
Indeed \(\|Av\|_2/\sqrt n\le20\), and linear growth followed by the
operator bound proves \(\|h^{(j)}\|_2/\sqrt n\le H_j\). Integrating the readout equation
over a contour of \(\nu\)-mass at most \(S\) gives
\(\|w\|_2/\sqrt n\le SH_L\). Define
\[
k_L=H_L,\quad k_j=10s k_{j+1},\quad \tau_j=sk_j,
\qquad P_1=3,\quad P_j=H_{j-1}+10sP_{j-1}+1,
\qquad f_j=sP_j.                                      \tag{S.6}
\]
Thus carrier and response RMS bounds are \(Sk_j,S\tau_j\).
The derivative numbers \(P_j\) also cover additive preactivation ports
at every layer: augment the mobility coordinates
\(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\)
by vectors \(e^{(j)}\) entering additively in \(z^{(j)}\), and
evaluate derivatives at \(e=0\). The direct first map has norm at
most \(2+1\); every later direct map contributes
\(H_{j-1}+1\). The recurrence proves the claimed augmented derivative
bound. These ports are proof variables and are never retained at runtime.

For \(F_a=nf_n(v_a)\), define
\[
A_*=2sP_L+2s^2\sum_{j=2}^Lk_jP_{j-1},\qquad
D_*=t_2\sum_{j=1}^LP_j^2,\qquad
H_*=A_*+t_2\sum_{j=1}^LP_j^2k_j.                     \tag{S.7}
\]
There are two readout cross terms of rank at most \(n\), two mixed
terms per hidden matrix, and curvature terms
\(Dz_a^{(j)\top}\operatorname{diag}(\phi_j''k_a^{(j)})Dz_a^{(j)}\).
The rank-normalized Schatten bounds consequently use (S.7), as shown in
§S.3 below. Crucially, \(D_\Theta\delta_a^{(j)}\) is a subblock of
this augmented Hessian, since \(\partial_{e^{(j)}}F_a=\delta_a^{(j)}\).
The same constants therefore cover both endpoints of the carrier trace;
no additional unproved endpoint estimate is needed.

Let \(f_* =\max_j f_j\), \(k_* =\max_jk_j\), and
\(H_{\max}=\max_jH_j\). Define
\[
E=t_2\sum_{j=1}^L(10s)^{2(j-1)}k_j,
\quad T_0=2H_*^2+4A_*^2(e^2-1),
\]
\[
D_0=(1+b+s)(1+T_0+E+s^2k_*^2),\qquad
D_1=576e^3(1+b+s)D_*^3,
\qquad C_F=s(8f_*^2+H_{\max}^2+1),
\qquad C_{\rm abs}=8(D_0+1).                       \tag{S.8}
\]
The subscript in the last constant means the scalar absorption coefficient.
It is unrelated to the initial first-weight matrix. All quantities in
(S.5)--(S.8) depend only on depth and activation bounds.

For the real activity moduli, set
\[
V_1=\tau_1,\qquad
V_j=\tau_jH_{j-1}^2+10sV_{j-1},
\]
\[
G_L=sH_L+14t_2V_L+s,\qquad
G_j=10sG_{j+1}+s^3k_{j+1}^2H_j+14t_2V_j+s,
\]
\[
W_{\rm G}=128\{1+H_{\max}+s\max_jV_j+\max_jG_j\}.
                                                               \tag{S.9}
\]
Their interpretation and derivation are in §S.5 below. Finally choose in
the stated order
\[
\eta=\min\{1,(1024C_{\rm abs}W_{\rm G})^{-1}\},\qquad
\mathcal B=1024e^2L,\qquad
\Lambda=\log(e+\mathcal B)+\log(1/\eta),
\]
\[
\begin{split}
S_*^{\rm src}=\min\bigg\{&1,\ (4A_*)^{-1},\
\sqrt{\eta/(4000D_*)},\
\sqrt{\eta/[16eD_*\sqrt{2\mathcal B}]},\
\sqrt{\eta/\Lambda},\
(\eta^3/(D_1\mathcal B))^{1/4},\
(8D_0C_F)^{-1/2}\bigg\}.                         \tag{S.10}
\end{split}
\]
Every denominator is strictly positive by (S.2), (S.5)--(S.9). The sufficient
source condition is \(S\le S_*^{\rm src}\), or
\(Y/\lambda\le S_*^{\rm src}/16\), together with the separate
real-fitting condition. This is a finite evaluable recurrence, independent
of \(m,d,\gamma,Y,n\), confidence, and empirical moment degree.

##### S.3. Separate joint budgets retain samplewise Schatten control

For each training sample separately let
\[
Z_{a,i}^{(j)}=\sup_z|z_{a,i}^{(j)}(z)|,\qquad
K_{a,i}^{(j)}=\sup_z|k_{a,i}^{(j)}(z)|,
\qquad
\mathcal H_a=\frac1n\sum_{j=1}^L\sum_i
 e^{\eta(Z_{a,i}^{(j)}+K_{a,i}^{(j)}/S)}.             \tag{S.11}
\]
The suprema are over each current stopped time rectangle. Stop every
\(\mathcal H_a\) at \(\mathcal B\), and each independently defined
cavity budget at \(2\mathcal B\). This includes the top carrier
\(k^{(L)}=w\). There is no maximum over samples inside an exponential.
The sample RMS running amplitudes at a neuron are
\[
Z_i^{(j)}=\left(m^{-1}\sum_a(Z_{a,i}^{(j)})^2\right)^{1/2},
\qquad U_i^{(j)}=\left(m^{-1}\sum_a(K_{a,i}^{(j)}/S)^2\right)^{1/2}.
                                                               \tag{S.12}
\]
These RMS quantities are not themselves the stopping budget. A single
RMS budget would not automatically control each sample's Schatten norms;
retaining (S.11) is essential.

For every sample, layer, and real \(p\ge2\), the elementary inequality
\(x^p\le(p/e)^pe^x\) yields
\[
\left(\frac1n\sum_i|k_{a,i}^{(j)}|^p\right)^{1/p}
\le (S/\eta)p(2\mathcal B)^{1/p},\qquad
\|k_a^{(j)}\|_\infty\le(S/\eta)\log(2n\mathcal B).
\]
The augmented Hessian decomposition and (S.7) then prove
\[
\|D^2F_a\|_{p,n}\le A_*+(SD_*/\eta)p(2\mathcal B)^{1/p},
\quad \|D^2F_a\|_{\rm HS}/\sqrt n\le H_*,
\]
\[
\|D^2F_a\|_{\rm op}\le A_*+(SD_*/\eta)\log(2n\mathcal B).
                                                               \tag{S.13}
\]
Here \(\|M\|_{p,n}=n^{-1/p}\|M\|_{S_p}\), also for rectangular
maps, where \(\|M\|_{S_p}=(\sum_i\sigma_i(M)^p)^{1/p}\) and
\(\sigma_i(M)\) are the singular values. The mixed blocks use the RMS of reference features; their action
is \(U_Hh/\sqrt n\), which is bounded by
\(H_j\|U_H\|_F\). Only the carrier diagonals need exponential
moments. Normalized residual mixtures retain (S.13), since
\(\sum_a|r_a|/(m\rho)\le1\).

The negative-Gram variational base contracts along the real solution.
All short complex/backwards pieces together have norm cost at most two,
after the explicit width condition in §S.8 below. The full propagator is
therefore bounded by
\[
2\exp\{SA_*+(D_*S^2/\eta)\log(2n\mathcal B)\}.
\]
Condition (S.10) gives \(D_*S^2/\eta\le1/4000\), leaving the inherited
\(n^{1/1000}\) variational cap at sufficiently large width. This
coefficient of \(\log n\) has not been moved into a width threshold.

The local graph proved in [finite deletion](#source-local-insertion) uses only polynomial logarithmic coordinate caps. Every
samplewise cap in (S.11) gives such a cap without a factor \(m\).
Deleted forward amplitudes now have size \(b+sZ_{a,i}\); learned
columns and rows satisfy the inherited \(n^{-1/2}\operatorname{polylog}n\)
source bounds. The exact top residual offset multiplies both the retained
gradient and reverse force. Their norms are respectively
\(n^{-1/2}\operatorname{polylog}n\) and
\(n^{-1}\operatorname{polylog}n\). Thus the complete unbounded local
proof, including its uniform control net and nonlinear remainders, applies
on this stronger collection of stops. Its strict powers of width do not
change. This invokes the local theorem above in its actual form;
it does not assume independence after conditioning on full survival.

##### S.4. Actual-amplitude traces close in sample RMS

At an interior omitted neuron, the incoming row and outgoing column are
independent \(N(0,I/n)\) roots conditional on retained initialization.
Let \(G_{h,a,i}\) and \(G_{\delta,a,i}\) be the suprema of their
forward-feature and backward-response cavity pairings. Divide the latter
by \(S\) below. First establish the trace bounds for deterministic
control paths; the control-uniform Gaussian event above is uniform over those paths.

In the backward trace, the two endpoints and \(h\) Hessian factors use
Schatten exponent \(h+2\). The zero-insertion term is at most
\(2H_*^2\). For \(h\ge1\), the integrated bound is
\[
\frac{2S^h}{h!}
 [A_*+(SD_*/\eta)(h+2)(2\mathcal B)^{1/(h+2)}]^{h+2}.
\]
Split the power into its bounded and carrier parts. Their sums are bounded
by \(4A_*^2(e^{2SA_*}-1)\) and
\[
\frac{8e^2D_*^2S^2\mathcal B}{\eta^2}
\sum_{h\ge1}(2eD_*S^2/\eta)^h(h+2)^2
\le\frac{576e^3D_*^3\mathcal B S^4}{\eta^3}.
\]
The last inequality uses \(\sum_{h\ge1}q^h(h+2)^2\le36q\) for
\(q\le1/2\), and follows by summing the geometric series and its first
two derivatives. Conditions (S.10) imply this restriction and \(SA_*\le1\).
The direct external trace is at most \(ES\): its curvature contraction
at layer \(j\) has nuclear norm per width at most
\(t_2(10s)^{2(j-1)}Sk_j\). The learned outgoing column adds at most
\(s^2k_*^2S^3\) times its actual forward amplitude. These are exactly
the terms in (S.8).

The substantive new point is to retain the sum over driving samples.
For each evaluated sample \(a\), each endpoint trace coefficient is
bounded by the same number, uniformly in driving sample \(b\). Hence
\[
\frac1m\sum_b|r_b|\,|h_{b,i}|\le
\rho\,(b+sZ_i),\qquad
\frac1m\sum_b|r_b|\,|\delta_{b,i}|\le\rho sS U_i.       \tag{S.14}
\]
These inequalities follow from Cauchy--Schwarz and the normalized sample
RMS in (S.12). They do not replace the time supremum by an instantaneous
quantity: the running amplitudes dominate every past integrand.

For the forward reverse-force trace the two forward endpoints have
operator and normalized Hilbert--Schmidt bound \(f_*\). In every term
with \(h\ge1\) insertions, give one endpoint exponent two, the other
infinity, and each Hessian exponent \(2h\). Its split series is bounded
by \(e^{2SA_*}-1\) and
\(\sqrt{2\mathcal B}\sum_{h\ge1}(4eD_*S^2/\eta)^h\).
Under (S.10) each is at most one. Including the zero term gives the
normalized trace bound \(8f_*^2\). Its learned incoming row has
norm at most \(sS^2U_iH_{j-1}/\sqrt n\); pairing against a retained
feature costs at most \(sS^2U_iH_{j-1}^2\). The first layer's direct
update costs at most \(sS^2U_i\). Thus \(C_F\) bounds all forward
feedback coefficients.

The uniform insertion expansion, (S.8), and (S.14) now give, sample by sample,
\[
K_{a,i}/S\le G_{\delta,a,i}/S+
 [D_0+D_1\mathcal B S^4/\eta^3](1+Z_{a,i}+Z_i)+o(1),
\qquad
Z_{a,i}\le G_{h,a,i}+C_FS^2U_i+o(1).                \tag{S.15}
\]
Independent incoming/outgoing cross forms are centered and their uniform
fluctuations are already in the insertion event. The direct external
trace at the evaluated sample multiplies its own current control
\(h_{a,i}\), not an average over driving samples. Its coefficient
\(ES\) costs \(ES(b+sZ_{a,i})\), explaining the separate
\(Z_{a,i}\) term. Only the integrated trace and learned-column terms
use (S.14)'s driving-sample RMS. This distinction is essential.

At the first layer, \(G_{h,a,i}\) is the initialized Gaussian row
paired with \(v_a\). At the top there is no outgoing root and
\(\sup|w_i|/S\le b+sZ_i\) by (S.14); take
\(G_{\delta,a,i}=0\). Thus both endpoints admit the same scalar
argument when their direct terms are assigned as specified below.

Taking sample RMS in (S.15), set
\(\overline G_h=(m^{-1}\sum_aG_{h,a,i}^2)^{1/2}\) and
\(\overline G_\delta=(m^{-1}\sum_a(G_{\delta,a,i}/S)^2)^{1/2}\).
Condition (S.10) gives backward coefficient at most \(2D_0\), and
forward coefficient \(D=C_FS^2\le1/(8D_0)\). Taking sample RMS
keeps both forward amplitudes and gives
\[
U_i\le\overline G_\delta+2D_0(1+2Z_i)+o(1),\qquad
Z_i\le\overline G_h+DU_i+o(1).
\]
The feedback product is \(4D_0D\le1/2\). Consequently
\[
U_i\le2\overline G_\delta+4D_0+8D_0\overline G_h+o(1),\qquad
Z_i\le\tfrac12+2\overline G_h+
                      \overline G_\delta/(4D_0)+o(1).
\]
For an individual sample,
\(Z_{a,i}\le G_{h,a,i}+\tfrac12+\overline G_h+
\overline G_\delta/(4D_0)+o(1)\). Substitution into its backward
inequality gives coefficients at most \(4D_0\) for the constant,
\(2D_0\) for \(G_{h,a,i}\), \(6D_0\) for
\(\overline G_h\), and one for \(\overline G_\delta\).
Adding the forward estimate proves the convenient envelope
\[
Z_{a,i}+K_{a,i}/S\le C_{\rm abs}
(1+G_{h,a,i}+G_{\delta,a,i}/S+
                  \overline G_h+\overline G_\delta)+o(1).          \tag{S.16}
\]
The constants in (S.8) include the direct evaluated-sample term. The coefficient is independent of
sample count and deletion count. The smallness choice precedes the
empirical moment degree.

##### S.5. Sample-uniform Gaussian moments, with no assumed moment law

Parameterize a real cavity by its own activity
\(u=\nu([0,t])/S\in[0,1]\), freezing after its endpoint. With
\(v=|u-u'|\), direct integration of (S.1) and (S.5)--(S.6) gives
\[
\|\Delta w\|_2/\sqrt n\le H_LSv,\quad
\|\Delta A\|_F/\sqrt n\le\tau_1S^2v,\quad
\|\Delta W^{(j)}\|_F\le\tau_jH_{j-1}S^2v,
\]
\[
\|\Delta z_a^{(j)}\|_2/\sqrt n\le V_jS^2v,\qquad
\|\Delta h_a^{(j)}\|_2/\sqrt n\le sV_jS^2v.             \tag{S.17}
\]
For a changed backward gate, split the reference carrier at \(SR\).
The high part is bounded by
\[
\|k\mathbf1_{|k|>SR}\|_2/\sqrt n
 \le(4S/\eta)\sqrt{2\mathcal B}\,e^{-\eta R/4},
\]
using \(x^2e^{-x/2}\le16\) and (S.11). Choose
\(R=(4/\eta)\log[8\sqrt{2\mathcal B}/(\eta v)]\) for \(v>0\).
The high changed-gate contribution is at most \(sSv\). The low
part is at most \(t_2V_jS^3Rv\). Since
\(R\le\eta^{-1}[10\Lambda+4\log(1/v)]\), the condition
\(S^2\Lambda/\eta\le1\), together with
\(v\log(1/v)\le2\sqrt v/e\), bounds that part by
\(14t_2V_jS\sqrt v\). The top carrier is treated by this same split;
it does not require a coordinate bound on the readout.

At the top, the other contribution is \(sH_LSv\). At a lower
layer, the changed mixer costs
\(s^3k_{j+1}^2H_jS^3v\), and propagation costs ten times the gate
bound \(s\). This proves the recurrence (S.9) and
\[
\|\delta_a^{(j)}(u)-\delta_a^{(j)}(u')\|_2/(S\sqrt n)
\le G_j\sqrt{|u-u'|}.                              \tag{S.18}
\]
All constants are independent of \(\eta,\mathcal B,m\) after the
explicit smallness restriction; the displayed recurrences already
include the top-carrier repair.

Condition on any autonomous cavity. For either of its scalar Gaussian
references, its initial variance and its square-root activity modulus
are bounded by (S.5), (S.9), (S.17)--(S.18). Dyadic grids of spacing \(4^{-q}\)
give at most \(2\cdot4^q\) increments of standard deviation bounded
by \(2G2^{-q}\). Gaussian tails with thresholds proportional to
\(2^{-q}\sqrt{z^2+4(q+1)}\), summed over all levels and with the
initial Gaussian value added, give
\[
\Pr\{X>W_{\rm G}(1+z)\mid\text{cavity}\}\le4e^{-z^2}.
                                                               \tag{S.19}
\]
Here \(X\) can be \(G_{h,a,i}\) or \(G_{\delta,a,i}/S\).
The coefficient 128 in (S.9) exceeds the sum of these dyadic thresholds
and the initial-value threshold. Integrating (S.19), or dominating the
positive excess by a variable with that tail, gives
\[
\mathbb E[e^{X^2/(16W_{\rm G}^2)}\mid\text{cavity}]<2.           \tag{S.20}
\]
For example, use \((1+z)^2\le2(1+z^2)\) and
\(\mathbb E e^{Z^2/8}\le1+4/7\) for a tail at most
\(4e^{-z^2}\); the resulting \(e^{1/8}(1+4/7)\) is below two.

For any collection of possibly dependent samplewise references,
\(\overline X^2=m^{-1}\sum_aX_a^2\). Convexity of the exponential
therefore gives the pointwise inequality
\[
e^{\overline X^2/(16W_{\rm G}^2)}
\le m^{-1}\sum_a e^{X_a^2/(16W_{\rm G}^2)}.
\]
Equation (S.20) thus holds for both RMS references in (S.16), with the same
constant and no independence between samples. Completing the square gives
\(\mathbb E e^{qX}\le2e^{4q^2W_{\rm G}^2}\) for each of the four
references. Hölder for their sum and (S.16) imply a moment bound
\[
\mathbb E e^{q(Z_{a,i}+K_{a,i}/S)}
\le 2\exp\{qC_{\rm abs}+64q^2C_{\rm abs}^2W_{\rm G}^2\}+o(1).
                                                               \tag{S.21}
\]
For \(q\le8\eta\), the right side is below four eventually by (S.10).
All higher fixed \(q\) also have finite moments. This is a consequence
of the stopped equations and Gaussian roots, not a premise concerning
trained coordinates.

Initial budgets are valid independently: at zero readout only forward
preactivations appear. On bounded preceding covariance sets, their
conditional second exponential moments are finite and their conditional
means continuous. Conditional Chebyshev gives convergence in probability
of each empirical layer budget. Its limiting mean is at most
\(2e^{\eta^2H_{\max}^2/2}<3\), so every initial sample budget is
below \(\mathcal B/2\) with probability tending to one. A fixed
sample union is allowed here. The preceding coordinate-small deletion
comparison transfers this margin to every fixed-size cavity. It does
not union-bound an \(O(1/n)\) estimate over deletion subsets.

##### S.6. Maximum, mixed endpoints, and explicit query coefficients

Impose training-coordinate maximum stops in addition to (S.11). Define
\[
C_G=32\max(1,H_{\max},\max_j\tau_j),\qquad
K_{\rm src}=16C_{\rm abs}(1+C_G).                    \tag{S.22}
\]
For cavity Gaussian references on a time rectangle of bounded width,
a mesh of size \(n^{-2}\) has a fixed multiple of \(n^5\) points.
Neurons, layers and the fixed sample count increase this to at most
\(n^7\) eventually. Complex Gaussian splitting gives tail
\(4e^{-u^2/(4\sigma^2)}\). The RMS coefficients are at most
\(H_{\max}\) and \(S\max\tau_j\), so (S.22) supplies strict
Gaussian margins of order \(\sqrt{\log(en)}\). Stopped derivatives
are polynomial logarithmic in normalized norm; the corresponding raw
coordinate derivatives are at most \(\sqrt n\operatorname{polylog}n\),
making the off-grid error vanish. The scalar inequalities (S.15)--(S.16)
therefore improve the full stops to
\[
\max_{a,j,i}|z_{a,i}^{(j)}|\le K_{\rm src}\sqrt{\log(en)},\qquad
\max_{a,j,i}|k_{a,i}^{(j)}|\le K_{\rm src}S\sqrt{\log(en)}.        \tag{S.23}
\]
This uses a polynomial Gaussian grid, not Gaussian supremum moments or
budget removal. Hence it precedes the complex moment argument.

For a complex great circle \(q(z)=u\cos z+v\sin z\), with real
orthonormal \(u,v\), define
\[
R_a^{(j)}=D_\Theta z^{(j)}(q)\nabla_\Theta F_a,
\qquad Q_a^{(j)}=\phi_j'(z^{(j)}(q))\odot R_a^{(j)},
\qquad J^{(j)}=\partial_z z^{(j)}(q(z)).
\]
These are residual-free response vectors, not physical velocities.
For \(|\operatorname{Im}z|\le1/8\), the input and every fixed
input derivative have norm below two. Put
\[
g=\tau_1+\sum_{j=2}^L\tau_jH_{j-1},\quad
r_j=P_jg,\quad q_j=f_jg,\quad j_j=20(10s)^{j-1},\quad b_j=sj_j,
\]
\[
e_1=t_2r_1P_1,\qquad
e_j=t_2r_jP_j+s(q_{j-1}+\tau_jH_{j-1}f_{j-1}+10e_{j-1}),
\]
\[
a_1=t_2j_1P_1+2s,\qquad
a_j=t_2j_jP_j+s(b_{j-1}+10a_{j-1}),
\]
\[
T_Q=8f_*\max_j(f_jH_*+e_j),\qquad T_J=8f_*\max_ja_j.          \tag{S.24}
\]
Here the layer coefficients \(r_j\) have a layer index, while the
physical residual \(r_a\) has a sample index. RMS bounds on
\(R,Q,J\) are \(Sr_j,Sq_j,j_j\). To derive the mixed endpoint,
differentiate \(Q=Dh\nabla F\): the first term uses \(DhD^2F\)
and (S.13); the second term uses the curvature diagonal
\(\operatorname{diag}(\phi''R)Dz\), the map
\(U_HQ/\sqrt n\), and a rank-one weight-gradient term. Their normalized
Hilbert--Schmidt coefficients are exactly the three forcing terms and
propagation in \(e_j\). The angular endpoint substitutes \(J\) for
\(R\); its first-layer additional map is \(U_Aq'\), whose
normalized Hilbert--Schmidt norm is at most two. This gives \(a_j\).
Neither endpoint uses a lower-layer coordinate maximum. Applying the
asymmetric trace from §S.4 with endpoint Hilbert--Schmidt norm
\(\max(f_jH_*+e_j)\) or \(\max a_j\) proves (S.24).

Set \(G_d=16\sqrt{d+3}\), and define
\[
U_1=4sK_{\rm src},
\]
\[
U_j=2\{sK_{\rm src}[H_{j-1}^2+f_{j-1}^2+ST_Q
                  +S^2H_{j-1}q_{j-1}]+G_dq_{j-1}+1\},\quad j\ge2,
\]
\[
V_1^{\rm qry}=2(2G_d+2sK_{\rm src}S^2+1),
\]
\[
V_j^{\rm qry}=2\{G_db_{j-1}+sK_{\rm src}S^2
                            (T_J+H_{j-1}b_{j-1})+1\},\quad j\ge2,
\qquad U=\max_jU_j,\quad V=\max_jV_j^{\rm qry}.       \tag{S.25}
\]
The four deterministic forward-response terms are, in order, the direct
feature pairing, direct reverse observable trace, exterior residual
integral, and learned-row correction. Their normalized coefficients are
the four terms inside the bracket. The centered Gaussian pairing gives
\(G_dq_{j-1}\). For the angular derivative both corrections have one
activity factor and one training carrier, hence \(S^2\). These are
the exact row-insertion terms from the endpoint insertion proof above with each
bounded activation value replaced by its actual layer RMS (S.5).

Frames \((u,v)\) form a bounded subset of \(\mathbb R^{2d}\).
A frame mesh and the three real time/tube coordinates have at most
\(n^{4d+10}\) points eventually. The multiplier \(G_d\) dominates
the complex Gaussian tail union. Nearby frames are joined by polar
normalization of their linear interpolation; its derivative is bounded
near the orthonormal-frame manifold. Thus the same off-grid estimates
apply without chart multiplication. The local graph above, with a
temporary passive-query preactivation cap
\(2[G_dH_{\max}+1+US^2+a][\log(en)]^2\), has only
polynomial logarithmic deleted controls. Query forward-control terms are
centered independent-root forms; the only nonzero same-root query trace
uses the training reverse control. The forward source enters only centered independent-root pairings; the reverse source uses the training root twice and gives the trace. This verifies the distinction directly. Consequently the improved coordinate estimates are
\[
\max|R_a^{(j)}|\le US\sqrt{\log(en)},\qquad
\max|J^{(j)}|\le V\sqrt{\log(en)}.                    \tag{S.26}
\]
The initial whole-sphere preactivation maximum is at most
\((G_dH_{\max}+1)\sqrt{\log(en)}\) eventually with probability tending
to one, by fresh-row Gaussian tails on a polynomial sphere mesh:
the conditional row variance is at most \(H_{\max}^2\), the factor
\(G_d=16\sqrt{d+3}\) covers the mesh union, and its off-grid error is
eventually at most one. Real-time
integration of (S.26) adds at most \(US^2\sqrt{\log(en)}\), so the
temporary passive-query size cap is strictly improved. No additional
query-coordinate exponential budget is needed.

##### S.7. Sharp complex derivative and joint-budget removal

Equation (S.1) and (S.24)--(S.26) give
\[
\|\dot z_a^{(j)}\|_2/\sqrt n\le2\rho Sr_j,\qquad
\|\dot z_a^{(j)}\|_\infty\le2\rho SU_j\sqrt{\log(en)}.
\]
Let \(N_* =\max_j(r_j,U_j)\), and take any real \(p\ge4\).
Interpolate the velocity to exponent \(2p/(p-2)\), then apply
Hölder with the carrier \(p\)-norm from (S.11). This yields
\[
\|k_a^{(j)}\odot\dot z_a^{(j)}\|_2/\sqrt n
\le (2\rho S^2N_*/\eta)p(2\mathcal B\log(en))^{1/p}.
\]
For \(\log(en)\ge\max(e^2,2\mathcal B)\), take
\(p=\max(4,\log(2\mathcal B\log(en)))\). The last exponential factor
is at most \(e\), and \(p\le2\log(e+\log(en))\). This is a
deterministic consequence of the stopped exponential budget at a growing
real exponent; it does not require growing deletion sets.

Define
\[
J_L^{\rm time}=2sH_L+4et_2N_*,\qquad
J_j^{\rm time}=10sJ_{j+1}^{\rm time}
                    +2s^3k_{j+1}^2H_j+4et_2N_*,\qquad
J_*^{\rm time}=\max_jJ_j^{\rm time}.
\]
Differentiating the backward recursion gives respectively the readout,
changed mixer, and changed gate contributions in this recurrence. Therefore
\[
\|\dot\delta_a^{(j)}\|_2/\sqrt n
\le J_*^{\rm time}\rho
       [1+(S^2/\eta)\log(e+\log(en))].                 \tag{S.27}
\]
The forward derivative is at most \(2\rho S\max q_j\). Thus, on
any time rectangle whose half-width is \(c_t/\sqrt{\log(en)}\) with
fixed \(c_t>0\), both normalized complex-minus-real Gaussian coefficient
radii tend to zero. For the backward coefficient divided by \(S\),
the explicit bound is
\[
D_n=(\lambda c_tJ_*^{\rm time}/4)[\log(en)]^{-1/2}
                     [1+(S^2/\eta)\log(e+\log(en))].     \tag{S.28}
\]
The two time-parameter Lipschitz coefficients have the same bracket times
fixed constants. Their parameter interval has length \(O(\log(en))\).
Dyadic Gaussian nets therefore have mean
\(O([\log(en)]^{-1/2}[\log(e+\log(en))]^{3/2})\) and tail scale
\(O([\log(en)]^{-1/2}\log(e+\log(en)))\). Both vanish. Their exponential
moments at every fixed order tend to one, as do fixed squared-exponential
moments; the latter also transfer to RMS sample corrections by the Jensen
argument of §S.5.

Each cavity is frozen or clamped on its own domain and assigned zero
reference paths on failed own initialization. All Gaussian laws are then
conditional on retained initialization alone. Common-cavity path
differences are projected onto deterministic Euclidean balls of radius
\(n^{1/90}\), which dominates the fixed-deletion Euclidean error
eventually. Projection is nonexpansive and preserves independence
from the omitted root. Its Gaussian radius is \(n^{-22/45}\),
so the real activity moduli and the complex nets give vanishing moments
at every fixed order. No full-network survival event is used as a Gaussian
conditioning event.

For a fixed sample and a fixed layer, expand the \(p\)th empirical
moment at fixed integer \(p\). Distinct neurons have independent root
pairs conditional on their common same-layer cavity. Equations (S.16),
(S.21), and the vanishing corrections give a main moment base below sixteen.
A fixed Hölder split handles projected errors at orders proportional to
\(p\); these moments tend to one at each fixed \(p\). Collision tuples
have \(O_p(n^{p-1})\) choices and finite higher fixed moments, hence
vanishing normalized contribution. The local exceptional probabilities
are superpolynomial and the stopped budgets are bounded.

The coordinate comparison transfers each individual joint budget:
\[
\mathcal H_a^{\rm cavity}\le
 e^{\eta o(1)(1+1/S)}\mathcal H_a+O_p(1/n)<2\mathcal B.
\]
Remove full-event indicators only after bounding by the nonnegative,
cavity-measurable Gaussian references. If any budget is hit, some sample
and layer has empirical budget at least \(\mathcal B/L\). Thus
\[
\limsup_{n\to\infty}\Pr\{\hbox{a joint budget is hit}\}
\le mL(16L/\mathcal B)^p.                            \tag{S.29}
\]
Take the width limit for each fixed \(p\), then its infimum over
positive integers. Since \(16L/\mathcal B<1\), the right side tends
to zero. This removes all joint budgets. Sample count affects a fixed
union and eventual width, not the source allowance in (S.10).

##### S.8. Label-sensitive time radius and the whole-sphere domain

Take
\[
c_t=\frac a{64YSU},\qquad
c_q=\min\{1/8,a/(8V)\},\qquad
r_t=c_t/\sqrt{\log(en)},\qquad r_q=c_q/\sqrt{\log(en)}.   \tag{S.30}
\]
For \(d\ge2\), the intrinsic query tube consists of
\(u\cosh h+i v\sinh h\), with real orthonormal \(u,v\) and
\(|h|\le r_q\). It is exactly the complex quadric neighborhood
\(q^\top q=1\), \(\|\operatorname{Im}q\|_2\le\sinh r_q\).
For \(d=1\), retain the two queries \(\pm1\) separately.

Set
\[
\mathcal K=H_L^2+S^2[\tau_1^2+
                    \sum_{j=2}^L\tau_j^2H_{j-1}^2],\qquad
D_W=\max\{\tau_1,\max_{j\ge2}\tau_jH_{j-1}\}.
\]
The actual algebraic residual Gram divided by \(m\), and the
negative-Gram variational generator divided by its factor two, have
operator norm at most \(\mathcal K\). This follows by summing the
squared normalized gradient-block norms, not by complex positivity.
Impose the explicit eventual width conditions
\[
n^{-1}\le Y,\qquad
\sqrt{\log(en)}\ge c_t\max\{8,\lambda,
                             4\mathcal K/\log2,32YSD_W\}.       \tag{S.31}
\]
Follow the real solution to the nearest real anchor in \([0,T]\),
then at most two short pieces of total length \(2r_t\). Their residual
growth and base-propagator cost are at most \(e^{4\mathcal Kr_t}\le2\).
The extra \(\nu\)-activity is at most \(8Yr_t\le S/2\).
The first-weight normalized and hidden-mixer increments are at most
\(8YSD_Wr_t\le1/4\), preserving strict margins inside cap ten.
No long horizontal complex contour is used.

The exact physical derivative is
\(\partial_tz^{(j)}=-(2/m)\sum_ar_aR_a^{(j)}\). On the short
pieces, \(\rho\le2Y\), so (S.26) bounds its coordinate magnitude
by \(4YSU\sqrt{\log(en)}\). The short time pieces and one intrinsic
query segment therefore have total preactivation displacement at most
\[
8c_tYSU+c_qV\le a/8+a/8=a/4.                         \tag{S.32}
\]
Full pole stops at \(3a/8\) and cavity stops at \(7a/16\) have
strict separation inside the derivative strip \(a/2\). Equation (S.32)
improves the full stop, and the coordinate comparison transfers its prefix
to all fixed-size cavity stops. The passive-query size stop improves by
§S.6. The logical order is local transfer, maximum improvement,
mixed endpoint and response improvement, query size/pole improvement,
complex Gaussian moments, and only then (S.29). Holomorphy holds on a
neighborhood of the closed rectangle times the closed query tube.

The radius coefficient \(c_t\) need not be at most one: its actual
radius shrinks at each fixed \(Y>0\). Condition (S.31) explicitly includes
\[
\log(en)\ge64c_t^2
 =a^2\lambda^2/(16384Y^4U^2).
\]
Thus the label-sensitive statement is not uniform as \(Y\downarrow0\).
No large fixed radius coefficient is used at an unchanged width.


<a id="source-power-ledger"></a>
#### Exact activation-power ledger on the explicit sufficient label cap

This subsection proves the numerical envelope; it does not replace the
larger recurrence allowance. Here only put \(z=Y/\lambda\) and suppose
\(z\le\beta^{-30L}\). Then \(S=16z\le\beta^{-26L}\).
The references labelled S are the explicit recurrences above; the
references labelled SP are the power inequalities in this subsection.

##### SP.1. Elementary absorptions and source base recurrences

All bounds below use \(b\le\beta-1\), \(s,t_2\le\beta\),
\(10s\le\beta^2\), and
\[
L\le\beta^{L-1},\qquad L+1\le\beta^{L-1},\qquad
4j\le\beta^j\quad(j\ge1),\qquad
\sum_{j=1}^L\beta^{rj}\le
\frac{\beta^{rL}}{1-\beta^{-r}}\quad(r>0).
\tag{SP.3}
\]
The first two inequalities follow by induction from \(L=2\);
the third follows by induction from \(j=1\). Also
\(\log\beta\le\beta\), and \(30\le\beta^2\).

For the source forward recurrence, unrolling the affine map gives
\[
H_j\le22\beta(10\beta)^{j-1}\le3\beta^{2j}.
\]
For example its first value is at most \(21\beta\), and the subsequent
additive contributions sum to at most
\(\beta(10\beta)^{j-1}/(10\beta-1)\). Unrolling the augmented-port
derivative recurrence similarly gives
\[
P_j\le4j(10\beta)^{j-1}\le\beta^{3j-2}.
\]
Consequently, for \(1\le j\le L\),
\[
\boxed{H_j\le3\beta^{2j},\quad
k_j\le3\beta^{4L-2j},\quad
\tau_j\le3\beta^{4L-2j+1},\quad
P_j\le\beta^{3j-2},\quad f_j\le\beta^{3j-1}.}
\tag{SP.4}
\]
These bounds use the actual source RMS recurrence and no global bound on
the activation values.

##### SP.2. Trace constants and the numerical source allowance

Direct substitution of (SP.4) into source (S.7)--(S.8), using the geometric sum
in (SP.3), gives the following ledger:

| Source constant | Intermediate bound | Power bound |
|---|---:|---:|
| \(A_*\) | \(7\beta^{5L-3}\) | \(\beta^{5L-2}\) |
| \(D_*\) | \(2\beta^{6L-3}\) | \(\beta^{6L-2}\) |
| \(H_*\) | \(4\beta^{8L-3}\) | \(\beta^{8L-2}\) |
| \(E\) | \(4\beta^{6L-3}\) | \(\beta^{6L-2}\) |
| \(T_0\) | \(3\beta^{16L-4}\) | \(\beta^{16L-3}\) |
| \(D_0\) | \(8\beta^{16L-3}\) | \(\beta^{16L-2}\) |
| \(D_1\) | \(9216e^3\beta^{18L-8}\) | \(\beta^{18L-2}\) |
| \(C_F\) | \(9\beta^{6L-1}\) | \(\beta^{6L}\) |
| \(C_{\rm abs}\) | \(65\beta^{16L-3}\) | \(\beta^{16L-1}\) |

Here are the exponent checks for the terms that could otherwise be
hidden by this table. The mixed summand in \(A_*\) is at most
\(6\beta^{4L+j-3}\); the curvature summand in \(H_*\) is at most
\(3\beta^{4L+4j-3}\). The summand in \(E\) is at most
\(3\beta^{4L+2j-3}\). In \(D_0\), its outer factor is at most
\(2\beta\), and its inner sum is at most
\[
1+3\beta^{16L-4}+4\beta^{6L-3}+9\beta^{8L-2}
\le4\beta^{16L-4}.
\]
For \(D_1\), the coefficient \(9216e^3<200000\le\beta^6\).
In \(C_F\), the inner expression is at most
\(8\beta^{6L-2}+9\beta^{4L}+1\le9\beta^{6L-2}\).
All displayed comparisons hold already at \(L=2,\beta=10\), and the
ratios of the smaller powers decrease when either variable increases.

To check the real activity moduli of source (S.9), unroll both recurrences.
The first one gives
\[
V_j\le27j\beta^{4L+2j-3},\qquad
\max_jV_j\le\beta^{7L-2}.
\tag{SP.5}
\]
Indeed every propagated forcing term has exponent \(4L+2j-3\).
For the reverse recurrence, its terminal value satisfies
\(G_L\le380L\beta^{6L-2}\). The propagated terminal contribution,
mixed-weight contributions, and curvature contributions at level \(j\)
are bounded respectively by
\[
380L\beta^{8L-2j-2},\quad
27L\beta^{8L-2j-1},\quad
379L\beta^{8L-2j-6}.
\]
The remaining constant contributions total at most
\(2\beta^{2L-2j-1}\). Hence
\[
G_j\le66L\beta^{8L-2j-1},\qquad
\max_jG_j\le\beta^{9L-2},\qquad W_{\rm G}\le\beta^{9L+1}.
\tag{SP.6}
\]
For the last bound, the braces in the definition of \(W_{\rm G}\) are
at most \(2\beta^{9L-2}\), and \(256\le\beta^3\).

The source choices of \(\eta,\mathcal B,\Lambda\) therefore obey
\[
\eta^{-1}\le\beta^{25L+4},\qquad
\mathcal B=1024e^2L\le\beta^{L+3},\qquad
\Lambda\le(26L+8)\log\beta\le\beta^{2L}.
\tag{SP.7}
\]
The first inequality uses \(1024\le\beta^4\); the second uses
\(1024e^2<7600\le\beta^4\). For the last one,
\((26L+8)\log\beta\le30L\log\beta\le\beta^{L+2}\le\beta^{2L}\).

Each nontrivial entry in the minimum defining \(S_*^{\rm src}\) is
at least \(\beta^{-p}\), with the following exponents:

| Entry in source (S.10) | \(p\) |
|---|---:|
| \((4A_*)^{-1}\) | \(5L-1\) |
| \(\sqrt{\eta/(4000D_*)}\) | \((31L+6)/2\) |
| \(\sqrt{\eta/(16eD_*\sqrt{2\mathcal B})}\) | \((63L+12)/4\) |
| \(\sqrt{\eta/\Lambda}\) | \((27L+4)/2\) |
| \((\eta^3/(D_1\mathcal B))^{1/4}\) | \((94L+13)/4\) |
| \((8D_0C_F)^{-1/2}\) | \((22L-1)/2\) |

These use \(4000\le\beta^4\), \(16e\le\beta^2\), and
\(\sqrt{2\mathcal B}\le\beta^{(L+4)/2}\). Every listed exponent
is at most \(26L\) for \(L\ge2\). We have proved
\[
\boxed{S_*^{\rm src}\ge\beta^{-26L}.}
\tag{SP.8}
\]
In particular the sufficient source label allowance is at least
\(\lambda\beta^{-26L}/16\), and the common cap \(Y/\lambda\le\beta^{-30L}\) satisfies it.

##### SP.3. Carrier and query coefficients

source (S.22) and (SP.4) give
\[
C_G\le96\beta^{4L-1},\qquad
K_{\rm src}\le1552\beta^{20L-2}
\le\beta^{20L+2}\le\beta^{21L}.
\tag{SP.9}
\]
For source (S.24), direct substitution and geometric summation give
\[
g\le9L\beta^{4L-1}\le\beta^{5L-1},\quad
r_j\le\beta^{5L+3j-3},\quad q_j\le\beta^{5L+3j-2},
\]
\[
j_j\le2\beta^{2j-1},\quad b_j\le2\beta^{2j},\quad
e_j\le2\beta^{5L+6j-4},\quad a_j\le3\beta^{5j-2},
\]
\[
\boxed{T_Q\le\beta^{14L-3},\qquad T_J\le\beta^{8L-1}.}
\tag{SP.10}
\]
For clarity, the three forcing terms in the recurrence for \(e_j\)
are at most
\(\beta^{5L+6j-4}\), \(\beta^{5L+3j-4}\), and
\(9\beta^{4L+3j-4}\); its propagation factor is at most
\(\beta^2\). The leading exponents grow by six per layer, so their
propagated sum is bounded by the factor two in (SP.10). The angular
recurrence has leading forcing \(2\beta^{5j-2}\), lower forcing
\(2\beta^{2j-1}\), and propagation factor \(\beta^2\); factor
three suffices, including \(a_1\le62\beta\). Finally
\(f_*H_*\le\beta^{11L-3}\), and
\(8f_*\max(f_jH_*+e_j)\le\beta^{14L-3}\);
\(24\le\beta^2\) proves the stated \(T_J\) bound.

Under \(S\le\beta^{-26L}\), both \(ST_Q\) and every
\(S^2H_{j-1}q_{j-1}\) are at most one. The braces multiplying
\(sK_{\rm src}\) in source (S.25) are at most
\(11\beta^{6L-8}\). Using the sharper bound
\(K_{\rm src}\le\beta^{20L+2}\) from (SP.9), we obtain for \(j\ge2\)
\[
U_j\le22\beta^{26L-5}
 +32\sqrt{d+3}\,\beta^{8L-5}+2.
\]
Also \(U_1\le4\beta^{20L+3}\). These imply
\[
\boxed{U\le\beta^{26L}\sqrt{d+3}.}
\tag{SP.11}
\]
For the query coefficient, the term
\(sK_{\rm src}S^2(T_J+H_{j-1}b_{j-1})\) is at most
\(2\beta^{-24L+2}\le1\). Thus
\[
V_j^{\rm qry}\le64\sqrt{d+3}\,\beta^{2L-2}+4
\le\beta^{2L}\sqrt{d+3}\quad(j\ge2).
\]
The first-layer bound is at most \(67\sqrt{d+3}\), and obeys the
same envelope. Therefore
\[
\boxed{V\le\beta^{2L}\sqrt{d+3},\qquad
c_q^{-1}=\max\{8,8V/a\}\le\beta^{2L+1}\sqrt{d+3}.}
\tag{SP.12}
\]

<a id="dense-proofs"></a>
### Dense proofs

The initialization event first gives a global fitting tube and a uniform
endpoint tail. On the trained source event, endpoint subtraction and
signed parameter energy then give Gaussian concentration in the complete
trajectory norm. Independently, the initialized Gram CLT and a
distribution-free innovation inequality identify a fluctuating training
derivative. The finite-query complex extension and polynomial derivative
inequality convert that derivative into an actual positive-time witness.

#### Proof of the initialization event

A maximal \(r\)-separated set of a Euclidean unit sphere is an
\(r\)-net of size at most \((1+2/r)^k\) in ambient dimension \(k\):
the disjoint radius-\(r/2\) balls about its points lie in the ball of
radius \(1+r/2\), and comparison of volumes gives that count.
For two \(1/4\)-nets, approximating a maximizing pair of unit vectors
in a bilinear form gives
\(\|M\|_{\rm op}\le2\max_{u,v\text{ in nets}}|u^TMv|\).
For a hidden initialized mixer each pairing has law \(N(0,1/n)\);
for \(A_0/\sqrt n\) it has the same law. The elementary Gaussian
tail bound \(\Pr\{|G|>z\}\le2e^{-z^2/2}\), followed by the net
union, therefore gives
\[
\Pr\{\|W_0^{(j)}\|_{\rm op}>8\}
\le2e^{-(8-2\log9)n},\qquad
\Pr\{\|A_0\|_{\rm op}/\sqrt n>8\}
\le2e^{-(8-\log9)n+d\log9}.
\]
The scalar tail itself follows by applying Markov's inequality to
\(e^{zG}\) and \(e^{-zG}\), using \(\mathbb Ee^{zG}=e^{z^2/2}\).
The displayed width terms make their combined loss smaller than
\(\alpha/2\).

For a positive semidefinite covariance \(C\), let
\(\Psi_j(C)_{ab}=\mathbb E\phi_j(Z_a)\phi_j(Z_b)\), where
\(Z\sim N(0,C)\). Along a symmetric covariance direction \(E\),
differentiating the nonsingular Gaussian density and integrating twice
by parts yields
\[
(D\Psi_j(C)[E])_{ab}=
\tfrac12E_{aa}\mathbb E[\phi_j''(Z_a)\phi_j(Z_b)]
+E_{ab}\mathbb E[\phi_j'(Z_a)\phi_j'(Z_b)]
+\tfrac12E_{bb}\mathbb E[\phi_j(Z_a)\phi_j''(Z_b)].
\]
This is the Gaussian identity
\(D\mathbb E F(Z)[E]=\frac12\sum_{u,v}E_{uv}
\mathbb E\partial_{uv}F(Z)\) for
\(F(z)=\phi_j(z_a)\phi_j(z_b)\). Linear growth and bounded first
two derivatives make the boundary terms vanish and dominate the
differentiated integrands by integrable Gaussian polynomials. For
singular endpoints, add \(\eta I\) to the covariance segment,
integrate the identity on that segment, and let \(\eta\downarrow0\).
The continuous positive square-root coupling and Gaussian moment
domination give the same integrated identity on the closed positive
semidefinite cone. For a diagonal entry it reads
\(E_{aa}\mathbb E[(\phi_j')^2+\phi_j\phi_j'']\).

If both covariance diagonals are at most \(2H_D^2\), then
\(\mathbb E|\phi_j(Z_a)|\le b+\sqrt2sH_D\). Integrating along the
segment thus gives
\[
\|\Psi_j(C)-\Psi_j(C')\|_{\max}
\le A_D\|C-C'\|_{\max}.
\]
Also \((u+v)^4\le8(u^4+v^4)\) and
\(\mathbb E Z_a^4\le12H_D^4\) imply
\(\mathbb E|\phi_j(Z_a)|^4\le M_D\). Cauchy--Schwarz bounds the
variance of each product \(\phi_j(Z_a)\phi_j(Z_b)\) by \(M_D\).

Conditionally on the preceding initialized layers, the next layer has
\(n\) independent Gaussian rows with covariance equal to the preceding
empirical feature Gram. For each of its \(m^2\) training entries and
the squared norm at each of the \(P_D\) query-net points, conditional
Chebyshev at tolerance \(e_D/T_D\) has failure at most
\(M_DT_D^2/(ne_D^2)\). At the first layer the input covariance is
deterministic and the same calculation is unconditional. If all preceding
tests passed, the covariance error after layer \(j\) is at most
\[
\frac{e_D}{T_D}\sum_{i=0}^{j-1}A_D^i\le e_D.
\]
Its input diagonal is at most \(H_D^2+e_D<2H_D^2\), so the conditional
variance condition closes inductively. A stopped union bound over the
\(L\) layers has failure at most
\[
\frac{L(m^2+P_D)M_DT_D^2}{ne_D^2}\le\alpha/2.
\]
The top training covariance error has operator norm at most
\(me_D\le\gamma/2\), proving the initial Gram gap after division
by \(m\). On the matrix event, the initialized layer-\(j\) feature
map, measured in RMS, is \((8s)^j\)-Lipschitz in \(v\).
A net-query feature norm is at most
\(\sqrt{H_D^2+e_D}\le\sqrt{5/4}H_D\); the off-net addition is
at most \((8s)^Lh_D\le H_D/4\).
Since \(\sqrt{5/4}+1/4<3/2\), this proves the sphere bound and
finishes the initialization probability calculation.

#### Proof of global fitting and the uniform tail

Stop at the first failure of mixer cap nine, sphere feature cap
\(2H_D\), or normalized readout-Gram gap \(\lambda/4\).
Backward propagation in this tube gives
\(\|\delta_a^{(j)}\|_2/\sqrt n\le D_j^D\|w\|_2/\sqrt n\).
Cauchy--Schwarz in the sample index bounds each hidden block's
normalized Frobenius velocity by
\(2\rho U_j^D\|w\|_2/\sqrt n\).

In normalized parameter coordinates the flow is minus the gradient of
\(\rho^2\). Therefore
\[
-\frac{d}{dt}\rho^2=\|\dot\theta\|_{\rm par}^2.
\]
The readout block alone contributes at least
\(4(\lambda/4)\rho^2=\lambda\rho^2\), proving the residual
decay on the stopped interval. While \(\rho>0\),
\[
\left(\int\|\dot\theta\|_{\rm par}\,dt\right)^2
\le\left(\int\frac{\|\dot\theta\|_{\rm par}^2}{\rho}\,dt\right)
\left(\int\rho\,dt\right)
\le(2Y)(2Y/\lambda).
\]
The first factor is \(-2\int d\rho\le2Y\). If the residual reaches
zero, every velocity becomes zero, so the estimates continue without
dividing by zero. Since \(w_0=0\), the path-length bound controls
its RMS by \(2Y/\sqrt\lambda\). Integrating the hidden velocities
then yields the displayed hidden displacement bounds.

For an arbitrary unit query, forward subtraction gives the first-layer
feature error at most \(s\|A-A_0\|_F/\sqrt n\), and at a later layer
at most
\[
s\left[2H_D\|W^{(j)}-W_0^{(j)}\|_F+
9\|h^{(j-1)}-h_0^{(j-1)}\|_2/\sqrt n\right].
\]
This is precisely the recurrence defining \(F_j^D\). The label
allowance gives
\[
\frac{8F_DY^2}{\lambda^{3/2}}
\le\frac{\sqrt\lambda}{8H_D^2}\le\frac1{8H_D}.
\]
The matrix cap thus improves to at most \(8+1/8\); the feature cap
improves to at most \(3H_D/2+H_D/8\). The training feature matrix
divided by \(\sqrt{mn}\) changes in operator norm by at most
\(\sqrt\lambda/(8H_D^2)\le\sqrt\lambda/8\). Its smallest singular
value stays above
\(\sqrt\lambda(1/\sqrt2-1/8)>\sqrt\lambda/2\), improving the
stopped Gram bound strictly. Hence no finite first exit exists.

At fixed \(n\), bounded parameter norm on every finite interval and
local Lipschitz continuity of the vector field give global continuation.
The finite total path length makes the parameters Cauchy as
\(t\to\infty\); the residual decay proves fitting. Finally,
\[
\|\dot w\|_2/\sqrt n\le4H_D\rho,\qquad
\|\dot h^{(L)}(v)\|_2/\sqrt n
\le2\rho F_D\|w\|_2/\sqrt n,
\]
so
\[
|\dot f_n(t,v)|\le
8\left(H_D^2+F_DY^2/\lambda\right)\rho(t).
\]
Integration gives the first endpoint tail. The second follows from
\(F_DY^2/\lambda\le\lambda/(64H_D^2)\le1/64\) and \(H_D\ge1\).
All estimates are uniform on the sphere.

The simpler sufficient real-fitting cap is
\(Y\le\lambda\beta^{-5L}\). Indeed
\(H_D\le(2\beta)^L\), the geometric sum gives
\(F_D\le(21/20)H_D^2s^2(9s)^{2L-2}\), and hence
\[
8H_D\sqrt{F_D}\le H_D^2(9s)^L
\le36^L\beta^{3L}\le\beta^{5L}.
\]
This sufficient cap does not replace the larger recurrence allowance.

#### Endpoint subtraction and the signed parameter energy

Use Euclidean/Frobenius normalized coordinates
\(\theta=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)\).
For two actual good states, write \(e_\theta=\theta-\theta'\),
\(d_\theta=\|e_\theta\|_2\), and
\[
D_h=\|A-A'\|_F/\sqrt n+
\sum_{j=2}^L\|W^{(j)}-W'^{(j)}\|_F,
\qquad D_w=\|w-w'\|_2/\sqrt n.
\]
Cauchy--Schwarz gives \(D_h\le\sqrt Ld_\theta\) and
\(D_h+D_w\le\sqrt{L+1}d_\theta\).
Forward subtraction first gives \(\|\Delta z^{(1)}\|_2/\sqrt n\le D_h\).
At each later layer use
\(\Delta z^{(j)}=W^{(j)}\Delta h^{(j-1)}+
\Delta W^{(j)}h'^{(j-1)}\).
The operator caps, feature RMS bounds, and \(s\)-Lipschitz activations
then give, uniformly on the query sphere,
\[
\|\Delta z^{(j)}\|_2/\sqrt n\le F_zD_h,\qquad
\|\Delta h^{(j)}\|_2/\sqrt n\le sF_zD_h.
\]
The coefficient \(F_z=2H_DT^{L-1}\) dominates every propagated
block coefficient because \(T\ge9\), \(H_D\ge1\), and the block
increments are summed in \(D_h\).

For a training sample, the gate difference in backward subtraction is
bounded by \(t_2M_nF_zD_h\), using the carrier of one actual endpoint.
The remaining terms are a changed readout, or a changed mixer multiplying
a reference backward vector, followed by propagation with factor \(T\).
To make the recursion explicit, put
\(b_j^{\rm err}=\|\delta_a^{(j)}-\delta_a'^{(j)}\|_2/\sqrt n\).
It obeys
\[
b_L^{\rm err}\le sD_w+t_2M_nF_zD_h,\qquad
b_j^{\rm err}\le Tb_{j+1}^{\rm err}
+sB_\delta\|\Delta W^{(j+1)}\|_F+t_2M_nF_zD_h.
\]
Unrolling it gives
\[
b_j^{\rm err}\le sT^{L-j}D_w
+sB_\delta\sum_{i=j+1}^LT^{i-j-1}\|\Delta W^{(i)}\|_F
+t_2M_nF_z\sum_{r=0}^{L-j}T^rD_h.
\]
The three coefficients are at most \(sT^{L-1}\),
\(sB_\delta T^{L-1}\), and \(Lt_2M_nF_zT^{L-1}\), respectively.
Thus
\[
\|\delta_a^{(j)}-\delta_a'^{(j)}\|_2/\sqrt n
\le D_\delta(M_n)(D_h+D_w).
\]
The gradient of one prediction has the exact block form
\[
\xi_a:=\nabla_\theta f_n(v_a)=
\left(\frac{\delta_a^{(1)}v_a^T}{\sqrt n},
\left(\frac{\delta_a^{(j)}(h_a^{(j-1)})^T}{n}\right)_{j=2}^L,
\frac{h_a^{(L)}}{\sqrt n}\right).
\]
Its block norms sum to at most \(G_*\). Subtracting each block gives
one first-layer backward difference, \(L-1\) hidden products each
bounded by \(2H_DD_\delta(D_h+D_w)+B_\delta sF_zD_h\), and a
readout feature difference \(sF_zD_h\). Thus
\[
\|\xi_a\|_2\le G_*,\qquad
\|\xi_a-\xi_a'\|_2
\le J(M_n)(D_h+D_w)
\le\sqrt{L+1}J(M_n)d_\theta.
\]

The Taylor remainder can also be evaluated entirely at actual endpoints.
Anchor derivatives and carriers at the unprimed endpoint, and define
\[
a^{(j)}=\Delta h^{(j)}-
\operatorname{diag}(\phi_j'(z^{(j)}))\Delta z^{(j)},\qquad
e^{(j)}=\Delta h^{(j)}-D_\theta h^{(j)}[e_\theta].
\]
Scalar Taylor's formula gives
\(|a_i^{(j)}|\le(t_2/2)|\Delta z_i^{(j)}|^2\). Direct differentiation
and subtraction yield
\[
e^{(1)}=a^{(1)},\qquad
e^{(j)}=\operatorname{diag}(\phi_j'(z^{(j)}))
[W^{(j)}e^{(j-1)}-\Delta W^{(j)}\Delta h^{(j-1)}]+a^{(j)}.
\]
Expanding this recurrence backward from the readout gives exactly
\[
\begin{split}
f_n(\theta,v_a)-f_n(\theta',v_a)-\langle\xi_a(\theta),e_\theta\rangle
={}&\frac1n\sum_{j=1}^L(k_a^{(j)})^Ta_a^{(j)}\\
&-\frac1n\sum_{j=2}^L(\delta_a^{(j)})^T
\Delta W^{(j)}\Delta h_a^{(j-1)}
-\frac1n\Delta w^T\Delta h_a^{(L)}.
\end{split}
\]
The last term is bounded by \(sF_zD_wD_h\le sF_z\sqrt Ld_\theta^2\).
The middle sum is at most \(B_\delta sF_zD_h^2\le LB_\delta sF_zd_\theta^2\).
The first sum is at most
\((Lt_2M_n/2)F_z^2D_h^2\le(L^2t_2F_z^2M_n/2)d_\theta^2\).
This proves the remainder bound \(T_{\mathrm{rem}}(M_n)d_\theta^2\).

Let \(v_a^{\rm err}=r_a-r_a'\) and
\(\|v^{\rm err}\|_m^2=m^{-1}\sum_a|v_a^{\rm err}|^2\).
Since \(\dot\theta=-(2/m)\sum_a r_a\xi_a\),
\[
\tfrac12\frac d{dt}d_\theta^2
=-\frac2m\sum_a v_a^{\rm err}\langle e_\theta,\xi_a\rangle
-\frac2m\sum_a r_a'\langle e_\theta,\xi_a-\xi_a'\rangle.
\]
Insert the remainder identity into the first pairing and use
\(\|v^{\rm err}\|_m\le\rho+\rho'\). The result is
\[
\tfrac12\frac d{dt}d_\theta^2
\le-2\|v^{\rm err}\|_m^2+
2\{T_{\mathrm{rem}}(M_n)(\rho+\rho')+
\sqrt{L+1}J(M_n)\rho'\}d_\theta^2.
\]
The negative prediction-difference square is retained before applying
Gronwall. Both residual integrals are at most \(Y/\kappa\), hence
\[
\sup_{t\ge0}d_\theta(t)\le d_\theta(0)e^{E_{\mathrm{en}}(M_n)}.
\]
At a vanishing discrepancy this follows by the regularized norm or by
uniqueness; no division by a zero discrepancy is needed.

#### Residual damping and the readout factor

The tangent Gram is \(K_{ab}=\langle\xi_a,\xi_b\rangle\).
Its normalized gap is at least \(\lambda/4\), because its readout
block is the top feature Gram and its other blocks are positive
semidefinite. The preceding endpoint estimates give
\[
\|(K-K')/m\|_{\rm op}\le2G_*J(M_n)(D_h+D_w).
\]
Indeed each entry is bounded by that quantity, and the operator norm
of an \(m\times m\) matrix divided by \(m\) is at most its maximum
entry magnitude. Subtract the exact equations
\(\dot r=-(2/m)Kr\). The homogeneous propagator contracts at rate
\(\kappa\), and the initial residual difference is zero. Variation
of constants and Tonelli therefore give
\[
\int_0^\infty\|r-r'\|_2/\sqrt m\,dt
\le\frac{4G_*J(M_n)}{\kappa}
\int_0^\infty\rho(D_h+D_w)\,dt,
\]
with \(\rho\) chosen from the path multiplying the kernel difference.
The exact readout subtraction, with equal zero initial readouts, gives
\[
D_w(t)\le4H_D\int_0^t\|r-r'\|_2/\sqrt m\,ds
+2sF_z\int_0^t\rho D_h\,ds.
\]
Combining these with the already closed energy estimate proves
\[
\sup_tD_w(t)\le\sqrt{L+1}
\left(\frac{16H_DG_*J(M_n)}\kappa+2sF_z\right)
\frac Y\kappa d_\theta(0)e^{E_{\mathrm{en}}(M_n)}.
\]
The sphere prediction difference is at most
\(2H_DD_w+RsF_zD_h\). Substitution yields
\[
\|f-f'\|_*\le
\sqrt{L+1}YC_Y(M_n)d_\theta(0)e^{E_{\mathrm{en}}(M_n)}.
\]
This derivation uses the reciprocal gap only after energy stability is
closed; it is not fed back into the Gronwall exponent.

To recover the original unsigned certificate, put \(D=D_h+D_w\).
Blockwise parameter subtraction gives
\[
D(t)\le D(0)+2G_*\int_0^t\|r-r'\|_2/\sqrt m\,ds
+2J(M_n)\int_0^t\rho D\,ds.
\]
Insert the damped residual integral above and apply Gronwall to obtain
\(\sup_tD(t)\le D(0)\exp\{2J(M_n)(1+4G_*^2/\kappa)Y/\kappa\}\).
Prediction subtraction costs at most \((2H_D+RsF_z)D\), proving the
stated older full-range coefficient.

<a id="dense-gaussian-concentration"></a>
#### Gaussian extension, exact confidence, and the all-time sphere norm

Let \(\mathsf G=(A_0,\sqrt nW_0^{(2)},\ldots,\sqrt nW_0^{(L)})\)
be the vector of independent standard Gaussian initialization coordinates.
Both readouts initially vanish, so
\(d_\theta(0)=\|\mathsf G-\mathsf G'\|_2/\sqrt n\).
The preceding estimate proves a pairwise Lipschitz bound on the actual
good set, with constant \(\mathcal L_n\), for every scalar prediction
at a fixed time and query. Its McShane extension is
\[
F_{t,v}(g)=\inf_{h\text{ in the good set}}
\{f_n(h;t,v)+\mathcal L_n\|g-h\|_2\}.
\]
The triangle inequality proves that this is globally
\(\mathcal L_n\)-Lipschitz, and the pairwise bound proves equality
with the actual prediction on the good set. Truncation to
\([-2H_DR,2H_DR]\) preserves both properties and bounds the extension.

Here is the Gaussian concentration fact and its needed proof. If \(F\)
is globally \(a_F\)-Lipschitz on standard Gaussian Euclidean space with
\(a_F>0\), then for \(z>0\),
\[
\mathbb P\{|F-\mathbb EF|>z\}\le2e^{-z^2/(2a_F^2)}.
\]
For a smooth function \(h\) bounded above and away from zero, define the
Ornstein--Uhlenbeck averaging operator
\(P_th(x)=\mathbb Eh(e^{-t}x+\sqrt{1-e^{-2t}}G)\).
Its Gaussian entropy is
\(\operatorname{Ent}(h)=\mathbb E[h\log h]
-(\mathbb Eh)\log(\mathbb Eh)\).
Differentiation, Gaussian integration by parts, and invariance of the
Gaussian law give
\[
\operatorname{Ent}(h)=
\int_0^\infty\mathbb E\frac{\|\nabla P_th\|_2^2}{P_th}\,dt.
\]
To verify the identity, differentiate
\(\mathbb E[(P_th)\log(P_th)]\), use generator
\(\Delta-x\cdot\nabla\), integrate by parts, and integrate from
\(t=0\) to \(\infty\), where \(P_th\to\mathbb Eh\).
The commutation \(\nabla P_th=e^{-t}P_t\nabla h\), followed by
weighted Cauchy--Schwarz, bounds the integrand by
\(e^{-2t}\mathbb EP_t(\|\nabla h\|_2^2/h)\).
Integration and Gaussian invariance prove
\(\operatorname{Ent}(h)\le\tfrac12\mathbb E(\|\nabla h\|_2^2/h)\).
Apply this to \(h=e^{zF}\) and integrate the resulting inequality
for \(z^{-1}\log\mathbb Ee^{zF}\). It gives
\(\mathbb Ee^{z(F-\mathbb EF)}\le e^{z^2a_F^2/2}\).
Markov's inequality optimized at \(z=u/a_F^2\), and the same argument
for \(-F\), give the displayed two-sided tail. Smooth approximation
and truncation extend it to every Lipschitz \(F\); Gaussian exponential
integrability of its linear growth justifies the limits.
If \(a_F=0\), the function is constant and the tail assertion is trivial.

For two independent roots, the difference of the identical scalar
extensions has mean zero and Lipschitz constant
\(\sqrt2\mathcal L_n\) on the product Gaussian space. Thus its
two-sided tail at level \(z\) is at most
\(2e^{-z^2/(4\mathcal L_n^2)}\). This argument does not condition
the Gaussian law on the good event or differentiate its indicator.

Use the proof coordinate \(u=1-e^{-\kappa t}\), including \(u=1\)
for the fitted limit. The fitting speed bound gives time modulus
\(K_t|u-u'|\). The actual matrix caps give a feature-map Lipschitz
coefficient at most \(T^L\) in feature RMS on the entire input space,
so prediction increments on the sphere are at most
\(K_x\|v-v'\|_2\). A time grid of \(n+1\) points and sphere
\(1/n\)-net of size at most \((1+2n)^d\) have at most \(N_n\)
joint points. At threshold
\(2\mathcal L_n\sqrt{\log(4N_n/\delta)}\), the Gaussian union costs
at most \(\delta/2\). The two actual paths' off-grid errors total at
most \(2(K_t+K_x)/n\).

For each path, take fitting failure at most \(\delta/8\) using its
explicit width, and source failure at most \(\delta/8\) using the
source's eventual width. The two path failures total at most
\(\delta/2\). Adding this to the net failure proves exactly the
displayed probability \(1-\delta\). The proof coordinate is only
used for a covering argument; neither training clock is changed.
Uniform fitting tails pass the estimate to \(t=\infty\).

#### The beta-only envelope and its actual-label factors

For this paragraph only, put \(z=Y/\lambda\) and \(h=1+1/\lambda\).
The source power ledger in the shared foundation gives
\(S_*^{\rm src}\ge\beta^{-26L}\) and
\(K_{\rm src}\le\beta^{21L}\). The sufficient cap
\(z\le\beta^{-30L}\) implies \(S=16z\le\beta^{-29L}\), so both
source and real-fitting allowances hold. Linear growth gives
\[
H_D\le(2\beta)^L\le\beta^{3L/2},\quad
\lambda\le\beta^{3L},\quad F_D\le\beta^{7L},\quad
F_z\le\beta^{4L},\quad M_n\le\beta^{22L}zu_n.
\]
The geometric sum for \(F_D\) and \(T\le\beta^2\) prove its
stated power. The elementary inequalities
\(L\le\beta^{L-1}\), \(2,8,32\le\beta^L\), and
\(128\le\beta^{2L}\), valid for \(L\ge2,\beta\ge10\), then give
\[
R\le\beta^{-28L},\quad B_\delta\le1,\quad
P,G_*\le\beta^{3L},\quad
D_\delta(M_n)\le\beta^{8L}(1+M_n),\quad
J(M_n)\le\beta^{12L}(1+M_n).
\]
For example, the two terms of \(D_\delta\) are bounded by
\(\beta^{3L}\) and \(\beta^{7L}M_n\); in \(J\), its second
term is at most \(\beta^{5L}\). The three Taylor-remainder terms
are dominated by \(\beta^{11L}(1+M_n)\). Substitution therefore gives
\[
E_{\mathrm{en}}(M_n)\le\beta^{14L}z(1+M_n)
\le\beta^{14L}z+\beta^{36L}z^2u_n.
\]
For the prefactor, expand it without suppressing gap powers:
\[
C_Y(M_n)=\frac{128H_D^2G_*J(M_n)}{\lambda^2}
+\frac{8H_DsF_z}{\lambda}+\frac{2sF_z}{\sqrt\lambda}
\le\beta^{21L}h^2(1+M_n).
\]
The three terms are bounded respectively by
\(\beta^{20L}h^2(1+M_n)\), \(\beta^{8L}h\), and
\(\beta^{6L}\sqrt h\), which proves the last inequality.

The actual coefficients satisfy \(\beta^{14L}z\le1\) and
\(\beta^{36L}z^2\le1\). Convexity gives
\(e^x\le1+2x\) on \([0,1]\) and
\(e^{\vartheta u}\le1+\vartheta(e^u-1)\) for
\(0\le\vartheta\le1\). Consequently
\[
e^{E_{\mathrm{en}}(M_n)}\le
(1+2\beta^{14L}z)
[1+\beta^{36L}z^2(e^{u_n}-1)].
\]
Since \(u_n\ge1\) and \(z\le1\), expansion proves
\[
(1+M_n)(1+2\beta^{14L}z)
\le1+\beta^{38L}zu_n.
\]
Indeed the three added coefficients are at most
\(\beta^{22L}+2\beta^{14L}+2\beta^{36L}\le\beta^{38L}\),
after using \(z^2\le z\). Thus
\[
2\mathcal L_n\le\frac{\beta^{23L}Yh^2}{\sqrt n}
(1+\beta^{38L}zu_n)
[1+\beta^{36L}z^2(e^{u_n}-1)].
\]
The physical coefficients satisfy
\(2(K_t+K_x)\le\beta^{5L}hY\), by
\(F_DY^2/\lambda\le1\) and the displayed bounds on \(H_D,T,R\).
Since every bracket and the logarithmic square root is at least one,
and \(n^{-1}\le n^{-1/2}\), this term is absorbed by enlarging the
leading exponent from \(23L\) to \(24L\). Finally replace the three
powers \(\beta^{24L},\beta^{38L},\beta^{36L}\) by
\(B_D=\beta^{100L}\), and \(4N_n\) by \(8N_n\). This proves
the stated beta-only certificate without hiding numerical constants.

#### Proof of the numerical accuracy inversion

To verify this, use \(N_n\le2\,3^dn^{d+1}\), hence
\(\log(8N_n/\delta)\le D_{d,\delta}\log(en)\), and
\[
1+B_D(Ym/\gamma)u_n\le(1+B_DYm/\gamma)u_n,
\quad
1+B_D(Ym/\gamma)^2(e^{u_n}-1)
\le(1+B_D(Ym/\gamma)^2)e^{u_n}.
\]
In fact \(v_\varepsilon\ge1\),
\(\log v_\varepsilon\le\sqrt{v_\varepsilon}\), and the ceiling
is at most twice its argument. Therefore
\[
\log(e\bar n_\varepsilon)
\le2v_\varepsilon+10\sqrt{v_\varepsilon}+18
\le\min\{(\sqrt{2v_\varepsilon}+5)^2,30v_\varepsilon\}.
\]
The lower bound for the same ceiling gives the ratio of the envelope
to \(\varepsilon\) at most
\(30e^{-2\sqrt{v_\varepsilon}-3}\le30e^{-5}<1\).
Finally \(\ell e^{\sqrt\ell}e^{-(\ell-1)/2}\) is decreasing for
\(\ell\ge4\), because its logarithmic derivative is
\(1/\ell+1/(2\sqrt\ell)-1/2\le0\); the chosen width is already
in that range. This proves the assertion for all larger widths.

#### Proof of the initialized Gram central limit theorem

To prove it, condition on the preceding initialized layers. The next
Gram is the average of \(n\) independent matrices
\(\phi_j(Z_i)\phi_j(Z_i)^T\), with Gaussian covariance
\(K_n^{(j-1)}\), and conditional mean
\(\Psi_j(K_n^{(j-1)})\). On bounded covariance sets, linear growth
gives uniform moments of every fixed order. Conditional Chebyshev first
proves \(K_n^{(j)}\to Q^{(j)}\) in probability by induction.

For a fixed linear functional \(u\) on symmetric matrices, center one
conditional summand and call its contraction \(X\). Taylor's integral
remainder for the scalar exponential gives
\[
\left|\mathbb E[e^{iX/\sqrt n}\mid\mathcal F_{j-1}]
-1+\frac{\mathbb E[X^2\mid\mathcal F_{j-1}]}{2n}\right|
\le\frac{\mathbb E[|X|^3\mid\mathcal F_{j-1}]}{6n^{3/2}}.
\]
The right side is uniformly of order \(n^{-3/2}\) on each bounded
covariance set. Raising the characteristic function to its \(n\)th
power therefore gives the Gaussian innovation characteristic function
with covariance \(B_j\), in probability. Both characteristic functions
have magnitude at most one, so convergence also holds in \(L^1\).
Multiplication by any bounded characteristic function of the preceding
fluctuations proves joint convergence with an independent new innovation.

It remains to linearize the conditional mean. The integrated Gaussian
identity proved in [dense fitting](#dense-fitting), regularized by
adding \(\eta I\) to the entire covariance segment, gives the displayed
map \(T_j\). Its coefficient expectations are continuous at singular
covariances: use their continuous positive square roots to couple the
Gaussians, and dominate by a fixed Gaussian polynomial using linear
growth and bounded derivatives. Integration on a feasible segment then
gives
\[
\Psi_j(Q+E)-\Psi_j(Q)-T_j(Q)E=o(\|E\|)
\]
as \(E\to0\) with \(Q+E\succeq0\). Applied to the preceding tight
\(n^{-1/2}\) fluctuation, its remainder is \(o_{\mathbb P}(n^{-1/2})\).
Combining with the independent conditional innovation proves the recursion
and completes the induction. This proof does not need an invertible
intermediate covariance or a quantitative central-limit error bound.

#### Proof of the innovation inequality and onset variance

Here is its complete proof for a random vector with finite fourth moment
and \(Q=\mathbb E HH^T\succ0\). Set
\(c=Qy\ne0\), \(A=\|c\|_2\), \(T_Q=\operatorname{tr}Q\),
\(M_4=\mathbb E\|H\|_2^4\), and
\(D=T_Q-c^TQc/A^2>0\). The squared area satisfies pointwise
\[
J(H):=A^2\|H\|_2^2-(c^TH)^2
=\|HS_y-c\|_2^2\|H\|_2^2-[(HS_y-c)^TH]^2
\le\|HS_y-c\|_2^2\|H\|_2^2.
\]
Also \(0\le J(H)\le A^2\|H\|_2^2\) and
\(\mathbb EJ(H)=A^2D\). For any \(R_0>0\), the contribution from
\(\|H\|_2>R_0\) is at most \(A^2M_4/R_0^2\), whereas the other
part is at most \(R_0^2V\), where
\(V=\mathbb E\|HS_y-c\|_2^2\). Therefore
\[
R_0^2V\ge A^2(D-M_4/R_0^2).
\]
Choosing \(R_0^2=2M_4/D\) gives
\[
V\ge\frac{A^2D^2}{4M_4}
=\frac{[y^TQ^2(T_QI-Q)y]^2}{4M_4\|Qy\|_2^2}.
\]
All denominators are positive. In the current model,
\(M_4\le m^2\mu_4\) by Cauchy--Schwarz and
\(T_Q=m\mu_{2,L}\). Every eigenvalue \(x\) of \(Q\) lies in
\([\gamma,T_Q-(m-1)\gamma]\subset[\gamma,T_Q-\gamma]\).
Consequently, if \(N=y^TQ^2(T_QI-Q)y\), then
\[
N\ge(m-1)\gamma\|Qy\|_2^2.
\]
For a second bound, the identity
\(x(T_Q-x)-\gamma(T_Q-\gamma)
=(x-\gamma)(T_Q-\gamma-x)\ge0\), followed by multiplication by
\(x\ge\gamma\), gives
\(N\ge\gamma^2(T_Q-\gamma)\|y\|_2^2\).
Multiplying these two positive lower bounds and substituting into the
moment inequality yields its first displayed version. Finally
\(\gamma\le\mu_{2,L}\) and
\(m\mu_{2,L}-\gamma\ge(m-1)\mu_{2,L}\) give the remaining
versions. The weaker bound
\[
V\ge\frac{(m-1)^2\gamma^4}{4m^2\mu_4}\|y\|_2^2
\]
also follows directly from \(D\ge(m-1)\gamma\) and
\(\|Qy\|_2\ge\gamma\|y\|_2\).

For the optional bounded-value subclass \(|H_a|\le K\), the same
area inequality can be integrated without truncation, since
\(\|H\|_2^2\le mK^2\). It gives
\[
V\ge\frac{\gamma^2(m\mu_{2,L}-\gamma)}{mK^2}\|y\|_2^2,
\qquad
\max_a\operatorname{Var}(H_aS_y)
\ge\frac{m-1}{m}\frac{\gamma^2\mu_{2,L}}{K^2}Y^2.
\]
Boundedness is used only in this optional improvement.

The qualitative obstruction has a short exact form. If \(V=0\),
then \(HS_y=Qy\) almost surely. Pairing with \(y\) makes
\(S_y^2=y^TQy>0\) deterministic; hence \(H=(Qy)/S_y\) lies in
one fixed line almost surely. Its second-moment matrix would have rank
at most one, contradicting \(m\ge2\) and \(Q\succ0\).

At least one deterministic training index \(a_*\), chosen from the
fixed data and labels, now satisfies
\[
\operatorname{Var}(H_{a_*}S_y)
\ge\frac{\gamma^3\mu_{2,L}}{16\mu_4}Y^2.
\]
At zero readout every hidden initial velocity vanishes, so exactly
\[
\dot f_n(0,v_a)=\frac2m\sum_b K_{n,ab}^{(L)}y_b.
\]
The initialized Gram central limit theorem and independent second run
therefore imply
\[
\sqrt n[\dot f_n(0,v_{a_*})-
\dot{\widetilde f}_n(0,v_{a_*})]
\Longrightarrow N(0,\sigma_{a_*}^2),
\]
\[
\sigma_{a_*}^2=\frac8{m^2}\sum_{b,c}y_b(C_L)_{a_*b,a_*c}y_c
\ge\frac8{m^2}\operatorname{Var}(H_{a_*}S_y)
\ge\frac{\gamma^3\mu_{2,L}Y^2}{2m^2\mu_4}.
\]
The factor eight is \((2/m)^2\) times the two independent
fluctuation variances. The inequality follows from
\(C_L=T_LC_{L-1}T_L^T+B_L\succeq B_L\); earlier layers cannot
cancel the final innovation. Duplicate query coordinates and singular
augmented Gaussian covariances are covered by the CLT proof above.

#### Proof of the finite-query source localization and label simplification

For a fixed finite collection of real unit queries, including the
training inputs and the selected witness, replace only the passive
frame-mesh union in the source construction. The training sample
budgets, independently stopped cavities, actual-amplitude traces, and
activity cap are unchanged. In the residual-free response recurrence,
the sphere coefficient \(16\sqrt{d+3}\) came from the frame mesh;
for this finite collection it is replaced by 64, producing precisely
\(U_j^{\rm fin}\) above. There are no angular derivatives or complex
query segments.

For clarity, the response at a query is
\[
R_a^{(j)}(v)=D_\Theta z^{(j)}(v)\nabla_\Theta(nf_n(v_a)),
\qquad
\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w).
\]
The source's endpoint and insertion identities require only query norm
at most two, so they still apply. A mesh of spacing \(n^{-2}\) on
the time rectangle has at most \(n^5\) points eventually; its length
is proportional to \(\log(en)\) and its width is bounded. Including
root/neuron indices and the fixed layer, sample, and finite-query
indices leaves at most \(n^{10}\) points eventually. The normalized
centered complex Gaussian tail is at most \(4e^{-u^2/4}\), so the
union at \(u=64\sqrt{\log(en)}\) is bounded by
\[
4n^{10}e^{-1024\log(en)}\longrightarrow0.
\]
The unchanged stopped derivative bounds are
\(\sqrt n\) times a fixed power of \(\log(en)\); hence the
\(n^{-2}\) off-grid error vanishes. Fixed queries have no spatial
off-grid term. Their initialized maxima have the same fresh-row
Gaussian bounds. The source's passive-query size stop improves by
the real increment \(U_{\rm fin}S^2\sqrt{\log(en)}\). There is no
union over deletion subsets and no new exponential query budget.
Conditional on the shared insertion interface this proves, with
probability tending to one,
\[
\max_{v,a,j}\|R_a^{(j)}(v)\|_\infty
\le S U_{\rm fin}(S)\sqrt{\log(en)}.
\]

Following the real path to its nearest anchor and then at most two
short pieces of combined length \(2r_n\), these gates give residual
growth at most two, additional activity at most \(S/2\), and hidden
parameter increments at most \(1/4\). The exact velocity identity
\(\partial_tz^{(j)}=-(2/m)\sum_a r_aR_a^{(j)}\), with
\(\rho\le2Y\) on these pieces, bounds total preactivation
displacement by \(8cYSU_{\rm fin}\le a/8\). There is no angular
displacement. Thus the pole stops retain strict margins inside the
half-strip.

The complex-minus-real Gaussian coefficient radii from the shared source
proof tend to zero for each fixed \(c\). Its empirical moment argument,
with \(\mathcal B=1024e^2L\), has the unchanged estimate
\[
\limsup_{n\to\infty}\Pr\{\text{a training budget is hit}\}
\le mL(16L/\mathcal B)^p
\]
for each fixed positive integer \(p\). First taking the width limit,
then the infimum over \(p\), makes this zero. One may take \(c=\chi(S)/\lambda\) on the full recurrence range.
On the simpler cap \(Y/\lambda\le\beta^{-30L}\), the source power
ledger specializes to
\[
U_1^{\rm fin}\le4\beta^{20L+3},\qquad
U_j^{\rm fin}\le22\beta^{26L-5}+128\beta^{8L-5}+2
\le\beta^{26L}.
\]
The first quantity is also at most \(\beta^{26L}\), since
\(4\beta^{-6L+3}\le4\cdot10^{-9}\). For the second, division by
\(\beta^{26L}\) gives at most
\(22\cdot10^{-5}+128\cdot10^{-41}+2\cdot10^{-52}<1\).
Using \(a\ge16/\beta\) and the actual activity cap yields
\[
\frac{a}{4S^2U_{\rm fin}(S)}
=\frac{a\lambda^2}{1024Y^2U_{\rm fin}(S)}
\ge\frac{\beta^{34L-1}}{64}>1.
\]
Thus \(\chi(S)=1\) on that cap and
\(r_n=m/[\gamma\sqrt{\log(en)}]\). This simplification is not
imposed on the full recurrence range.

#### The deterministic derivative-to-trajectory inequality

Suppose a function \(g\) is holomorphic on a neighborhood of the filled
parameter-two Bernstein ellipse for \([0,r]\), and \(|g|\le M\)
there. For every integer \(N\ge1\),
\[
\sup_{0\le t\le r}|g(t)|
\ge\frac r{2N^2}|g'(0)|-24M2^{-N}.
\]
To prove it, send \([0,r]\) to \([-1,1]\) by
\(t=r(x+1)/2\). Under the Joukowski map
\(x=(z+z^{-1})/2\), holomorphy on the ellipse gives a Laurent
expansion on an annulus containing \(1/2\le|z|\le2\).
Cauchy's coefficient bound gives Chebyshev coefficients
\(|a_k|\le2M2^{-k}\). The degree-\(N\) truncation has uniform
tail at most \(2M2^{-N}\), since \(|T_k(x)|\le1\) on \([-1,1]\).
At the physical endpoint \(t=0\), its derivative tail is at most
\[
\frac{4M}{r}\sum_{k>N}k^22^{-k}
=\frac{4M}{r}2^{-N}(N^2+4N+6).
\]
The identity follows by writing \(k=N+j\) and using
\(\sum_{j\ge1}2^{-j}=1\),
\(\sum_{j\ge1}j2^{-j}=2\), and
\(\sum_{j\ge1}j^22^{-j}=6\).

For completeness, the endpoint polynomial inequality
\(|P'(-1)|\le N^2\sup_{[-1,1]}|P|\) also holds for complex
coefficients. Interpolate at the Chebyshev extrema
\(x_j=\cos(j\pi/N)\), \(0\le j\le N\). The derivative weights
\(\ell_j'(-1)\) of the Lagrange basis have alternating signs, with
\(\ell_j'(-1)(-1)^j\) all of the same sign; this follows by counting
the signs in their products, including
\(\ell_N'(-1)=\sum_{j<N}(-1-x_j)^{-1}<0\).
Since \(T_N(x_j)=(-1)^j\), their absolute sum is
\(\left|\sum_j\ell_j'(-1)(-1)^j\right|
=|T_N'(-1)|=N^2\).
The last equality follows by differentiating
\(T_N(\cos\theta)=\cos(N\theta)\) and taking the endpoint limit.
The triangle inequality now proves the claimed polynomial bound.

Apply it to the truncated series, multiply by \(2/r\) for the
physical derivative, and add the two tails. After rearrangement, the
error coefficient is
\(4+8/N+12/N^2\le24\), giving the stated inequality.

#### Applying the inequality to the actual nonlinear predictions

Take \(g_n(t)=f_n(t,v_{a_*})-\widetilde f_n(t,v_{a_*})\).
The parameter-two ellipse for \([0,r_n]\) has real projection
\([-r_n/8,9r_n/8]\) and imaginary projection
\([-3r_n/8,3r_n/8]\). The finite-query rectangle contains it:
the numerical source gates give \(r_n\le1/\lambda\), whereas
\(T_n=32\log(en)/\lambda\). Choose
\[
N_n^{\rm Ch}=\left\lceil\frac{2\log(en)}{\log2}\right\rceil
\le4\log(en),\qquad 2^{-N_n^{\rm Ch}}\le n^{-2}.
\]
On the two localized source events the preceding deterministic inequality
therefore gives
\[
\|f_n-\widetilde f_n\|_*
\ge\frac{c}{32\log(en)^{5/2}}|g_n'(0)|
-\frac{768\beta^{6L}Y}{\lambda n^2}.
\]
This estimate concerns the actual nonlinear trajectories with the original
labels. It has no fixed nonzero Taylor remainder that could dominate
the \(n^{-1/2}\) fluctuation.

Write \(\sigma=\sigma_{a_*}>0\). For a fixed \(u>0\), the explicit
deterministic gate
\[
n^{3/2}\ge
\frac{49152\beta^{6L}Y}{\lambda c\,u\sigma}\log(en)^{5/2}
\]
makes the remainder at most half the leading term whenever
\(|g_n'(0)|\ge u\sigma/\sqrt n\). The initialized CLT has no atom
at either threshold \(\pm u\sigma\), and both source failures tend
to zero. Thus, without requiring independence of these events,
\[
\liminf_{n\to\infty}
\mathbb P\left\{\|f_n-\widetilde f_n\|_*
\ge\frac{uc\sigma}{64\sqrt n\,\log(en)^{5/2}}\right\}
\ge2[1-\Phi(u)].
\]
Take \(c=\chi(S)/\lambda\), insert
\(\sigma\ge\gamma^{3/2}Y\sqrt{\mu_{2,L}/\mu_4}/(\sqrt2m)\),
and use \(1/(64\sqrt2)\ge1/128\). This gives the displayed
coefficient, with \(\chi(S)\ge\chi_{\rm act}\). Finally choose
\(u=\Phi^{-1}(1/2+\delta/4)\). The limit lower probability is
\(1-\delta/2\), leaving a strict margin for the source failures
and CLT convergence. Hence the probability is at least \(1-\delta\)
at every sufficiently large individual width. The width is not
effective because neither the insertion probability nor the CLT
remainder is quantified. Since \(g_n(0)=0\), a positive lower threshold
is attained only at a strictly positive time in the compact witness
interval.

#### Exact exceptions and the dense storage consequence

For \(Y=0\), both predictors are identically zero. For \(m=1\),
the last innovation is
\[
y_1^2\left[\mu_4-\mu_{2,L}^2\right]
=y_1^2\operatorname{Var}
\big(\phi_L(\sqrt{\mu_{2,L-1}}G)^2\big).
\]
If \(\mu_{2,L-1}>0\), continuity and full Gaussian support make
this variance zero exactly when \(\phi_L^2\) is constant on the
real line. A continuous real function with positive constant square
must itself be constant, because the real line is connected. If
\(\mu_{2,L-1}=0\), the feature is also deterministic. These cases
are permitted by a positive one-sample uncentered gap. In particular,
for \(\phi_L\equiv c\ne0\), every hidden gradient vanishes and
\[
f_n(t,v)=y_1(1-e^{-2c^2t})
\]
for every width, initialization, and query. Thus the general lower
theorem cannot include \(m=1\).

The zero-preactivation-variance exception is deterministic as well.
Starting from \(\mu_{2,0}=1\), take the last transition from a positive
moment to zero before layer \(L\). Gaussian full support forces that
activation to be identically zero. All subsequent moments up to
\(\mu_{2,L-1}\) are zero, so the intervening activations vanish at
zero. The final feature is the constant \(\phi_L(0)\), and the same
deterministic formula applies. Outside these effective-constant cases,
the scalar innovation is positive, but no coefficient uniform in the
gap and \(\beta\) alone follows: with identity earlier activations
and \(\phi_L(t)=\sqrt{1-\eta^2}+\eta t\), \(0<\eta<1\), one has
\(\mu_{2,L-1}=\mu_{2,L}=\gamma=1\), a common \(\beta=10\), and
\(\mu_4-\mu_{2,L}^2=4\eta^2-2\eta^4\to0\).

Fix \(0<\delta<1/2\) and a nondegenerate \(m\ge2\) task. If an
independent dense pair at a sufficiently large width satisfies
\(\Pr\{\|f_n-\widetilde f_n\|_*\le\varepsilon\}\ge1-\delta\),
then its accuracy event intersects the lower event, since their failure
probabilities sum to less than one. Therefore necessarily
\[
n[\log(en)]^5\ge
\frac{c_{\phi,L,\delta}^2Y^2\gamma}{\varepsilon^2},
\]
and its per-run dense parameter count obeys the explicit implicit bound
\[
S_D(n)\ge(L-1)n^2\ge
\frac{(L-1)c_{\phi,L,\delta}^4Y^4\gamma^2}
{\varepsilon^4[\log(en)]^{10}}.
\]
At a fixed task this implies the necessary order
\(\varepsilon^{-4}/\log(1/\varepsilon)^{10}\) up to a positive
fixed-task coefficient: if \(n\le\varepsilon^{-4}\) and
\(\varepsilon\le e^{-1}\), then
\(\log(en)\le5\log(1/\varepsilon)\); if
\(n>\varepsilon^{-4}\), its quadratic storage is already larger
than that order for all sufficiently small \(\varepsilon\).
This is a restriction on the canonical independent dense family,
not a storage or bit-complexity lower bound against arbitrary
compressed representations.

<a id="legendre-proofs"></a>
### Legendre proofs

The proof first establishes the polynomial projection identities and
all-order physical fitting. It then controls the reconstruction defect by
signed parameter energy, proves both forward certificates, and justifies
the scalar accuracy inverses.

<a id="legendre-projection-proof"></a>
#### Projection identities, with the numerical endpoint bounds

Let \(P_j\) be the Legendre polynomial defined by Rodrigues' formula
\(P_j(x)=(2^jj!)^{-1}(d/dx)^j(x^2-1)^j\). On \([0,A]\),
write \(p_j^A(\xi)=P_j(2\xi/A-1)\), and let
\(\Pi_q^A\) be orthogonal projection in Lebesgue \(L^2([0,A])\)
onto polynomials of degree below \(q\). Integration by parts in
Rodrigues' formula gives
\[
\int_0^Ap_i^Ap_j^A\,d\xi=\frac A{2j+1}\mathbf1_{i=j},
\qquad
-\frac d{d\xi}\left[\xi(A-\xi)(p_j^A)'\right]
=j(j+1)p_j^A.
\]
The normalized derivative polynomials are orthogonal in the weighted
derivative inner product. Bessel's inequality there, followed by the
ordinary orthogonal expansion of \(u\), proves
\[
\|(I-\Pi_q^A)u\|_{L^2}^2
\le\frac1{q(q+1)}
\int_0^A\xi(A-\xi)\|u'(\xi)\|^2d\xi.
\tag{Legendre-weighted-tail}
\]
One first applies this calculation to finite polynomial expansions;
polynomial density and the weighted derivative Bessel inequality give
the displayed bound for absolutely continuous histories with the finite
energy appearing on its right. It also holds for Hilbert-valued histories
by applying the scalar argument to finitely many orthogonal coordinates
and passing to their increasing squared norms.

The derivative identity
\(P_j'=\sum_{i<j,\ j-i\ \mathrm{odd}}(2i+1)P_i\), obtained by
integration by parts against the orthogonal polynomials, telescopes to
the endpoint projection kernel
\[
K_q^A(A,\xi)=\frac1A\sum_{j=0}^{q-1}(2j+1)p_j^A(\xi)
=\frac{(p_q^A)'(\xi)+(p_{q-1}^A)'(\xi)}2.
\]
Its integral is one. Integrating by parts, using
\(p_q^A(0)+p_{q-1}^A(0)=0\), proves
\[
u(A)-(\Pi_q^Au)(A)
=\frac12\int_0^A[p_q^A(\xi)+p_{q-1}^A(\xi)]u'(\xi)d\xi.
\]
The squared norm of this scalar multiplier is
\(A[(2q+1)^{-1}+(2q-1)^{-1}]/4\le A/(3q)\). Thus
\[
\|u(A)-(\Pi_q^Au)(A)\|
\le\sqrt{A/(3q)}\,\|u'\|_{L^2}.
\tag{Legendre-endpoint-tail}
\]

Here is a direct proof of the additional bound
\[
\|(\Pi_q^Au)(A)\|\le64\sqrt q\,\|u\|_{L^\infty}.
\tag{Legendre-endpoint-kernel}
\]
For \(k\ge1\), put
\(v(\theta)=\sqrt{\sin\theta}P_k(\cos\theta)\) and
\(a_k(\theta)=(k+1/2)^2+(4\sin^2\theta)^{-1}\).
The Legendre differential equation gives \(v''+a_kv=0\). Therefore
\[
\frac d{d\theta}\left(v^2+\frac{(v')^2}{a_k}\right)
=-\frac{a_k'}{a_k^2}(v')^2\ge0
\quad(0<\theta<\pi/2).
\]
At the center, \(P_{2j}(0)=(-1)^j{2j\choose j}/4^j\) and
\(P_{2j+1}'(0)=(2j+1)P_{2j}(0)\). The elementary induction
\(({2j\choose j}/4^j)^2\le1/(j+1)\) bounds the central energy
by \(2/k\), and hence by \(4/k\). Taking square roots and
differentiating \(P_k=v/\sqrt{\sin\theta}\) gives
\[
|\partial_\theta P_k(\cos\theta)|
\le3\sqrt k(\sin\theta)^{-1/2}
+2k^{-1/2}(\sin\theta)^{-3/2}.
\]
On \([1/k,\pi/2]\), the two integrals are at most
\(3\pi\sqrt k\) and \(4(\pi/2)^{3/2}<8\), respectively,
using \(\sin\theta\ge2\theta/\pi\). On \([0,1/k]\),
\(|P_k'(x)|\le k(k+1)/2\) gives an integral at most
\((k+1)/(4k)\le1/2\). To verify that derivative bound, use the
derivative expansion above and \(|P_i(x)|\le1\) on \([-1,1]\).
The latter follows, for example, from
\[
P_j(\cos\theta)=\frac1\pi\int_0^\pi
(\cos\theta+\mathrm i\sin\theta\cos\psi)^j\,d\psi;
\]
the identity follows by comparing its geometric-series generating
function with \((1-2tx+t^2)^{-1/2}\), and the integrand has modulus
at most one. Reflection around \(\pi/2\) now proves
\({\rm Var}_{[-1,1]}P_k\le36\sqrt k\). The endpoint kernel formula
has \(L^1\) norm at most \(36\sqrt q\), which is below the stated
64. The case \(q=1\) is the constant averaging kernel. This proves
(Legendre-endpoint-kernel), including vector-valued histories.

For a fixed history \(g\), let
\(E_g(A)=\int_0^A\|g-\Pi_q^Ag\|^2d\xi\). Orthogonality to
\(\partial_A\Pi_q^Ag\), which is still a polynomial of degree
below \(q\), gives the exact growing-interval identity
\[
E_g'(A)=\|g(A)-\Pi_q^Ag(A)\|^2.
\tag{Legendre-growing-energy}
\]
In clock coordinates define
\(h_a(\tau(t))=\widehat h_a(t)\) and
\(b_a(\tau(t))=(\widehat r_a/\widehat\rho)
\widehat\delta_a(t)\), with their specified prefixes. Since
\(\widehat W^{(L+1)}(0)=0\), the backward history is continuous
at the prefix junction. The moments in (Legendre-moment-flow) equal
\(\int_0^{\tau(t)}p_j^{\tau(t)}h_a\) and
\(\int_0^{\tau(t)}p_j^{\tau(t)}b_a\). Differentiating those
integrals proves the stated ODEs, using the derivative expansion already
proved. By orthogonality, reconstruction subtracts
\(2/(mn)\sum_a\int(\Pi_qb_a)(\Pi_qh_a)^T\).
Differentiating this bilinear projection integral gives its full endpoint
product minus the product of its two endpoint errors. Hence the exact
physical defect is
\[
\dot{\widehat W}^{(\ell)}
=-\frac2{mn}\sum_a\widehat r_a\widehat\delta_a^{(\ell)}
(\widehat h_a^{(\ell-1)})^T+\mathcal E_\ell,
\qquad
\mathcal E_\ell=
\frac{2\widehat\rho}{mn}\sum_a e_{b,a}^{(\ell)}
(e_{h,a}^{(\ell-1)})^T.
\tag{Legendre-exact-defect}
\]
Here \(e_g=g(\tau)-\Pi_q^\tau g(\tau)\). These identities first
hold before a residual zero, with ordinary clock differentiation; the
runtime is continuous at zero, and its stationary continuation gives the
corresponding stopped limits.

<a id="legendre-fitting-proof"></a>
#### All-order fitting and the physical bounds

For this proof only set \(\lambda=\gamma/m\),
\(S=8Y/\lambda\), \(R=S\sqrt\lambda\), and
\(\kappa=\lambda/4\). Assume (Legendre-initialization-event) and
\(S\le S_*^{\rm Leg}\). Stop at total clock activity \(S\),
readout RMS \(R\), any operator norm nine, or sphere feature RMS
\(2H\). Before that stop, backward propagation gives
\(\|\widehat\delta_a^{(\ell)}\|_2/\sqrt n\le D_\ell R\).
Projection contraction in the reconstruction, sample Cauchy--Schwarz,
and the zero backward prefix imply
\[
\|\widehat W^{(\ell)}-W_0^{(\ell)}\|_F
\le4HD_\ell R\sqrt{(1+S)S},\qquad
\frac{\|\widehat W^{(1)}-W_0^{(1)}\|_F}{\sqrt n}
\le2D_1RS.
\]
For the first bound the forward history norm is at most
\(2H\sqrt{1+S}\), and the aggregate backward norm at most
\(D_\ell R\sqrt S\), both with neuron RMS and sample RMS
normalizations. Since \(\sqrt\lambda\le H\), \(S\le1\),
and \(64H^2D_1S\le1\), both increments are strictly less than
one. Thus no operator boundary is reached.

For each layer let \(Z_\ell\) be the supremum over sphere queries of
\(n^{-1}\int_1^{\tau(t)}\|\partial_\xi h^{(\ell)}(\xi,x)\|_2^2d\xi\),
also taking the supremum over the current stopped time interval. The
endpoint evaluation norm on polynomial \(L^2([0,A])\) is
\(q/\sqrt A\), because \(K_q^A(A,A)=q^2/A\). Consequently
the aggregate backward endpoint error is at most
\((q+1)D_\ell R\). Integrate the square of
(Legendre-exact-defect), use (Legendre-growing-energy), and apply
(Legendre-weighted-tail) with \(\xi(A-\xi)\le A^2/4\). The
prefix error is zero, and \((q+1)/q\le2\), giving
\[
\int_0^t\widehat\rho
\|\mathcal E_\ell/\widehat\rho\|_F^2du
\le2(1+S)^2D_\ell^2R^2Z_{\ell-1}.
\tag{Legendre-defect-energy}
\]
The first-layer chain rule gives \(Z_1\le4Ss^2D_1^2R^2\).
At each later layer the three contributions to its preactivation
derivative are the dense gradient term, the defect term and the previous
feature derivative. Their squared integrals are bounded respectively by
\(64SH^4D_\ell^2R^2\),
\(32H^2D_\ell^2R^2Z_{\ell-1}\), and \(81Z_{\ell-1}\).
Using \(\|u+v+w\|^2\le3(\|u\|^2+\|v\|^2+\|w\|^2)\)
therefore gives
\[
Z_\ell\le3s^2\{64SH^4D_\ell^2R^2+
[81+32H^2D_\ell^2R^2]Z_{\ell-1}\}
\le C_\ell SR^2.
\tag{Legendre-feature-energy}
\]
The last inequality uses
\(32H^2D_\ell^2R^2\le32H^4D_1^2S^2<1\).
The recurrence \(C_\ell\) increases with \(\ell\). Thus every
sphere feature moves by at most
\(\sqrt{SZ_\ell}\le\sqrt{C_L}S^2\sqrt\lambda\le\sqrt\lambda/8\),
by the third entry in \(S_*^{\rm Leg}\). This is also at most
\(H/8\), excluding the feature boundary. The normalized top training
feature matrix moves in operator norm by at most \(\sqrt\lambda/8\).
Its minimum singular value stays above
\((1/\sqrt2-1/8)\sqrt\lambda>\sqrt\lambda/2\), proving the
mean readout-Gram gap \(\lambda/4\).

For a pointwise defect estimate use the sharper endpoint kernel:
the backward endpoint error is at most \(65\sqrt qD_\ell R\),
while the forward endpoint error is at most
\(\sqrt{(1+S)/(3q)}\sqrt{Z_{\ell-1}}\), with the same RMS
normalizations. Since \(S\le1\), (Legendre-exact-defect) gives
\[
e_{\mathcal E}(t):=\sum_{\ell=2}^L\|\mathcal E_\ell(t)\|_F
\le E\sqrt S R^2\widehat\rho(t).
\tag{Legendre-pointwise-defect}
\]
Indeed \(2\cdot65\sqrt{2/3}<130\).
The prediction Jacobian applied to hidden-matrix defects has sample
RMS at most \(2HD_1R e_{\mathcal E}\). The fourth entry in
\(S_*^{\rm Leg}\) gives
\[
\|J\mathcal E\|_2/\sqrt m
\le2HD_1E S^{7/2}\lambda^{3/2}\widehat\rho
\le\lambda\widehat\rho/4.
\]
The residual equation is
\(\dot{\widehat r}=-2\Gamma\widehat r+J\mathcal E\), where
\(\Gamma\) is the mean full tangent Gram and
\(\Gamma\succeq\lambda I/4\). It follows that
\(\dot{\widehat\rho}\le-\kappa\widehat\rho\).
Thus \(\widehat\rho(t)\le Ye^{-\kappa t}\) and
\(\int_t^\infty\widehat\rho\le\widehat\rho(t)/\kappa\);
before any stopped endpoint the same statement holds with the integral
only up to that endpoint. In particular the activity never exceeds
\(Y/\kappa=S/2\).

Let \(\mathcal F\) be the dense gradient field evaluated at the
reconstructed parameters, in the physical Hilbert norm
\[
\|U\|_{\rm par}^2=
\|U^{(1)}\|_F^2/n+
\sum_{\ell=2}^L\|U^{(\ell)}\|_F^2+
\|U^{(L+1)}\|_2^2/n.
\]
Its squared norm is \(4\widehat r^T\Gamma\widehat r/m
\ge\lambda\widehat\rho^2\). Therefore
\[
-\frac d{dt}\widehat\rho^2
=\|\mathcal F\|_{\rm par}^2
-2\widehat r^TJ\mathcal E/m
\ge\tfrac12\|\mathcal F\|_{\rm par}^2.
\]
Multiplication by \(e^{\kappa t}\) and integration by parts show
\(\int e^{\kappa t}\|\mathcal F\|_{\rm par}^2dt\le4Y^2\).
Weighted Cauchy--Schwarz then yields
\(\int\|\mathcal F\|_{\rm par}dt\le2Y/\sqrt\kappa
=4Y/\sqrt\lambda=R/2\). The readout has no defect, so this
excludes its boundary. All stops have strict margins. At fixed finite
\(n,q\), the moment integral formulas and \(1\le\tau\le1+S\)
bound every stored coordinate on finite intervals, proving global
continuation. Local uniqueness excludes a finite first residual zero
when \(Y>0\), because zero residual is an equilibrium of the entire
stored-state ODE. The finite path lengths of \(\mathcal F\) and
\(\mathcal E\) give convergent physical parameters, and the moment
ODEs also have integrable velocities. Residual decay proves interpolation.
This establishes (Legendre-physical-bounds) for every order on one event.

Finally (Legendre-pointwise-defect) and the gradient velocities give the
coefficients \(T_\ell,V_\ell\) in
(Legendre-projection-coefficients). In particular
\(\|\dot{\widehat h}^{(\ell)}(x)\|_2/\sqrt n
\le V_h\widehat\rho\). The tangent Gram's trace is at most
\(4H^2+D_1^2R^2+4H^2R^2\sum_{\ell=2}^LD_\ell^2\).
Differentiating \(\widehat c=\widehat r/\widehat\rho\), using
the residual equation and the triangle inequality, proves
\(\|\dot{\widehat c}\|_2/\sqrt m\le C_c\), with exactly
the displayed coefficient.

<a id="legendre-stability-proof"></a>
#### Signed stability and the projection comparison

Use Euclidean physical coordinates
\(\theta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},
W^{(L+1)}/\sqrt n)\). Let
\(e_\theta=\widehat\theta-\theta_D\), \(e=\|e_\theta\|\), and
let \(D(t)\) be the sum of the \(L+1\) block norms of \(e_\theta(t)\).
Then \(D(t)\le\sqrt{L+1}e(t)\).

On the parameter segment \(\theta_v=\theta_D+ve_\theta\),
\(0\le v\le1\), convexity preserves the matrix and readout bounds.
Linear growth of the activation gives feature RMS at most \(Q\).
Subtracting forward passes recursively gives
\[
\max_\ell\frac{\|z_v^{(\ell)}-z_D^{(\ell)}\|_2}{\sqrt n}
\le F_{\rm seg}vD(t),\qquad
\max_\ell\frac{\|h_v^{(\ell)}-h_D^{(\ell)}\|_2}{\sqrt n}
\le sF_{\rm seg}vD(t).
\]
The first bound starts with the first parameter block; each later layer
has recurrence \(\Delta z_\ell\le9s\Delta z_{\ell-1}
+Q\Delta W_\ell\). For backward subtraction use
\[
\delta_v-\delta_D
=\phi'(z_v)\odot(k_v-k_D)
+[\phi'(z_v)-\phi'(z_D)]\odot k_D.
\]
Only the dense carrier maximum \(M_n\) is used. Propagation by
\(9s\), the changed matrix acting on a dense response of RMS at
most \(B_\delta\), and at most \(L\) changed gates give
\[
\max_\ell\frac{\|\delta_v^{(\ell)}-\delta_D^{(\ell)}\|_2}{\sqrt n}
\le(d_0+d_1M_n)vD(t).
\]
There is no carrier assumption on the segment or the closure.
The gradient of one training output has blocks
\[
g_{a,1}=\delta_a^{(1)}v_a^T/\sqrt n,\qquad
g_{a,\ell}=\delta_a^{(\ell)}(h_a^{(\ell-1)})^T/n,
\qquad g_{a,L+1}=h_a^{(L)}/\sqrt n.
\]
Subtracting each hidden product in the order
\((\delta_v-\delta_D)h_v^T+\delta_D(h_v-h_D)^T\) proves
\[
\|g_a(\theta_v)-g_a(\theta_D)\|
\le(K_0+K_1M_n)ve.
\]
Thus, with \(K=K_0+K_1M_n\), segment integration yields
\[
\widehat r-r_D=J_De_\theta+\mathcal R,\qquad
\|\mathcal R\|_2/\sqrt m\le Ke^2/2,
\quad
\|(J_{\widehat\theta}-J_D)e_\theta\|_2/\sqrt m\le Ke^2.
\]
The physical equations are
\(\dot\theta_D=-2J_D^*r_D\) and
\(\dot{\widehat\theta}=-2J_{\widehat\theta}^*\widehat r
+\mathcal E\), with adjoints using the sample inner product.
Putting \(v_r=\widehat r-r_D\) gives the exact signed energy identity
\[
\frac12\frac d{dt}e^2
=-2\|v_r\|_2^2/m+2v_r^T\mathcal R/m
-2\widehat r^T(J_{\widehat\theta}-J_D)e_\theta/m
+\langle e_\theta,\mathcal E\rangle
\]
\[
\le K(\rho_D+3\widehat\rho)e^2+e\|\mathcal E\|.
\]
Regularize \(e\) by \(\sqrt{e^2+\eta^2}\) and then let
\(\eta\downarrow0\) to justify the scalar inequality at zero.
The integrated residual bounds are \(2Ym/\gamma\) and
\(4Ym/\gamma\). Gronwall and the common initial state imply, on
every finite horizon \([0,T]\),
\[
\sup_{t\le T}D(t)\le\mathcal A_n\mathcal D_T,
\qquad
\mathcal D_T=\int_0^T\sum_{\ell=2}^L\|\mathcal E_\ell(t)\|_Fdt.
\tag{Legendre-signed-stability}
\]
The coefficient is exactly (Legendre-stability-coefficients).

The forward history has clock derivative RMS at most \(V_h\).
Since \(\tau\le1+a_0\) and
\(\int_1^A\xi(A-\xi)d\xi\le A(A-1)^2/2\), the weighted
projection bound gives forward tail norm at most \(F_h/q\).
For the backward history record the dense response in the closure clock,
\(\widetilde b_a(\tau(t))=\widehat c_a(t)\delta_{D,a}(t)\),
with zero prefix. Its physical derivative has aggregate RMS at most
\(C_cB_\delta+V_\delta\rho_D\). The dense speed constants
\(V_z,V_\delta\) in (Legendre-projection-coefficients) follow by
differentiating forward and backward recursions: the backward terms are
the readout speed, changed hidden matrices and changed gates, respectively.
The changed-gate term uses only \(M_n\).

Freeze \(\widetilde b\) after physical time
\(u=2\log q/\kappa\), or after \(T\) if earlier. For
\(A=\tau(T)\), the residual tail estimate gives
\(A-\tau(t)\le\widehat\rho(t)/\kappa\). In the weighted
clock derivative energy this cancels the inverse clock speed, so
\[
\int_0^A\xi(A-\xi)\|\partial_\xi\widetilde b^{\rm frozen}\|^2d\xi
\le\frac{1+a_0}\kappa
\left[2uC_c^2B_\delta^2+
2V_\delta^2\int_0^u\rho_D(t)^2dt\right].
\]
The aggregate norm here is
\((mn)^{-1/2}(\sum_a\|\cdot\|_2^2)^{1/2}\).
Since \(\int\rho_D^2\le Y^2/(2\kappa)\), its projected tail
is at most the first two terms of
\((b_0+b_1\sqrt{\log q})/q\). The freezing remainder has
norm at most
\(2B_\delta\sqrt{a_0}e^{-\kappa u/2}
=2B_\delta\sqrt{a_0}/q\). This includes \(q=1\), when
\(u=0\) and the frozen response is zero.

Forward and backward subtraction directly between the two trajectories
uses \(2H\) instead of \(Q\), giving response difference RMS
at most \(B_dD(t)\). Multiplication by \(\widehat c\), whose
sample RMS is one, and integration over a clock interval of length at
most \(a_0\) give an additional history error
\(B_d\sqrt{a_0}\sup_{t\le T}D(t)\).

To control the integral of the absolute defect, not merely its signed
integral, apply sample Cauchy--Schwarz to (Legendre-exact-defect) and
then Cauchy--Schwarz in \(dA=\widehat\rho dt\). Both prefix
energies vanish. Equation (Legendre-growing-energy) yields for each
interface
\(\int_0^T\|\mathcal E_\ell\|_Fdt
\le2\sqrt{E_b(\tau(T))E_h(\tau(T))}\). Consequently
\[
\mathcal D_T\le2(L-1)F_h\left[
\frac{b_0+b_1\sqrt{\log q}}{q^2}
+\frac{B_d\sqrt{a_0}\sup_{t\le T}D(t)}q\right].
\tag{Legendre-absorption-inequality}
\]
If \(q\ge T_n\), substituting (Legendre-signed-stability)
absorbs the last term with factor at most one half. Whole-sphere forward
and readout subtraction give prediction discrepancy at most \(C_fD\).
Thus
\[
\|f_{{\rm Leg},n,q}-f_n\|_*
\le\frac{4(L-1)C_f\mathcal A_nF_h}{q^2}
(b_0+b_1\sqrt{\log q})
\le C_n\frac{\sqrt{\log(eq)}}{q^2}
\quad(q\ge T_n).
\tag{Legendre-large-order}
\]
The finite-horizon constants are independent of \(T\); taking its
increasing supremum and then the physical limits proves the stated norm.
For every order, (Legendre-physical-bounds) and Cauchy--Schwarz give
\(\|f_{{\rm Leg},n,q}-f_n\|_*\le U\). When \(q<T_n\),
the second term in (Legendre-full-forward) exceeds \(U\); when
\(q\ge T_n\), its first term suffices by (Legendre-large-order).
This proves the full-range all-order certificate without an order gate.

<a id="legendre-simple-cap-proof"></a>
#### The unchanged simple-cap coefficient also covers small orders

Only in this algebraic proof, write
\(X=\beta^L\ge100\), \(z=Ym/\gamma\),
\(\chi=1+m/\gamma\), and \(u=\sqrt{\log(en)}\ge1\).
Here \(z\) is a scalar proof abbreviation, never a preactivation.
The simple cap says \(z\le X^{-30}\).

First the cap implies the full fitting and source restrictions. The
Gaussian recursion gives \(H\le(2\beta)^L\le\beta^{3L/2}\).
The geometric sum for \(F\) gives
\(8H\sqrt F\le\beta^{5L}\). Moreover
\(D_\ell\le\beta^{2L}\), \(\sqrt{C_\ell}\le\beta^{8L}\),
and \(E\le\beta^{12L}\). For the middle bound, unroll
\(C_\ell=192s^2H^4D_\ell^2+246s^2C_{\ell-1}\), use
\(192s^2,246s^2\le\beta^5\),
\(H^4D_\ell^2\le\beta^{10L}\), and sum at most \(L\)
terms; the result is below \(\beta^{16L}\). For \(E\), use
\(130L\le(\beta^L)^2\). Substitution in every entry of
\(S_*^{\rm Leg}\) gives \(S_*^{\rm Leg}\ge\beta^{-8L}\).
Thus \(8z\le S_*^{\rm Leg}\). The shared source power proof
gives \(S_*^{\rm src}\ge\beta^{-26L}\) and
\(K_{\rm src}\le\beta^{21L}\); hence
\(16z\le S_*^{\rm src}\). No extra label restriction has entered.

For the remaining algebra use the weaker \(H\le X^2\),
\(\gamma/m\le X^4\), \(D_\ell\le X^2\), and
\(\sqrt{C_\ell}\le X^8\). The cap gives
\(R\le X^{-27}\), \(S\le1\), \(a_0\le1\), and
\(B_\delta\le X^3R\le1\). The affine segment recurrence gives
\(Q\le X^2\), whence
\[
F_{\rm seg}\le X^4,\quad d_0\le2X^3,\quad
d_1\le LX^7\le X^8,\quad p\le X^4,
\quad K_0\le X^9,\quad K_1\le X^{13}.
\]
Using \(M_n\le32X^{21}zu\), \(14\le X\) and
\(448\le X^2\), the exact stability exponent obeys
\[
14(K_0+K_1M_n)z\le X^{10}z+X^{36}z^2u.
\tag{Legendre-simple-exponent}
\]
Both \(X^{10}z\le X^{-20}\) and \(X^{36}z^2\le X^{-24}\)
are at most one. The elementary convexity inequalities
\(e^v\le1+2v\) for \(0\le v\le1\), and
\(e^{\vartheta u}\le1+\vartheta(e^u-1)\) for
\(0\le\vartheta\le1\), therefore show
\[
\mathcal A_n\le X\Xi_n,\qquad
\Xi_n=(1+X^{100}z)[1+X^{100}z^2(e^u-1)].
\tag{Legendre-exponential-interpolation}
\]

For explicit verification of the remaining coefficient assembly, the
speed recurrence has \(T_1\le X^3R\),
\(T_\ell\le(4X^4+130X^{10})R\le X^{12}R\),
forcing at most \(2X^{15}R\), and total propagation at most
\((9s)^L\le X^2\). Summing at most \(L\) terms proves
\(V_h\le X^{20}R\). The displayed tangent trace gives
\(C_c\le X^{11}\). Direct substitution then gives
\[
F_z\le X^5,\quad P_0\le X^4,\quad
F_h\le X^{24}z^2,\quad F_h/Y\le X^{22}z\sqrt\chi,
\]
\[
B_d\le X^{33}(1+zu),\quad
V_z\le2X^{12}R,\quad V_\delta\le X^{40}(1+zu),
\]
\[
b_1\le X^{16}z\sqrt\chi,\quad
b_0\le X^{42}z(1+zu),\qquad C_f\le X^7.
\tag{Legendre-simple-power-ledger}
\]
For the label-sensitive terms, the explicit substitutions are
\(F_h\le32X^{20}z^2\sqrt{\gamma/m}\) and
\(F_h/Y\le32X^{20}z\sqrt{m/\gamma}\).
The two terms of \(B_d\) are at most
\(2X^3\) and \(32LX^{29}zu\). The non-carrier and carrier
parts of \(V_\delta\) are at most \(4LX^5\) and
\(64LX^{36}Rzu\). Finally
\(b_1\le96X^{14}z\sqrt{m/\gamma}\); the two terms of
\(b_0\) are at most \(6X^{40}z(1+zu)\) and
\(32X^5z^{3/2}\). Since \(z\le1\), \(L\le X\), and
\(X\ge100\), these imply each entry of the ledger without
discarding the actual label factors.

In particular
\(b_0+b_1\sqrt{\log q}
\le X^{43}z\sqrt\chi(1+zu)\sqrt{\log(eq)}\).
Combining the ledger with \(4(L-1)\le X^2\) and
(Legendre-exponential-interpolation) shows that the numerator of
(Legendre-large-order), divided by \(Y\), is at most
\[
X^{75}z^2\chi(1+zu)\Xi_n\sqrt{\log(eq)}.
\]
Since
\((1+zu)(1+X^{100}z)\le3(1+X^{100}zu)\), this is at most
\(P_n\sqrt{\log(eq)}\). Thus the unchanged coefficient works
whenever \(q\ge T_n\).

It remains to cover \(1\le q<T_n\) with this same coefficient.
Retain the factor \(\sqrt{a_0}=2\sqrt z\) in the exact threshold:
\[
T_n\le2X^{60}z^{5/2}(1+zu)
\exp\{X^{10}z+X^{36}z^2u\}.
\]
Put \(\alpha=X^{10}z\) and \(\vartheta=X^{36}z^2\).
Then \(e^{2\alpha}\le2\), \(2\vartheta\le1/2\), and,
for \(u\ge1\), the exponential series gives
\(u^2e^{u/2}\le16(e^u-1)\). Consequently
\[
(1+zu)^2e^{2\alpha+2\vartheta u}
\le4+(8\vartheta+64z^2)(e^u-1)
\le4[1+X^{100}z^2(e^u-1)].
\]
Indeed expand \((1+zu)^2\le2+2z^2u^2\), apply convexity to
\(e^{2\vartheta u}\), and use \(18X^{36}\le X^{100}\).
Since \(12H\sqrt{m/\gamma}\le X^3\sqrt\chi\), this proves
\[
12H\sqrt{m/\gamma}\,T_n^2
\le16X^{123}z^5\sqrt\chi[1+X^{100}z^2(e^u-1)]
\le P_n.
\]
The final comparison is exactly
\(16X^{23}z^3\le16X^{-67}\le3\le
3\sqrt\chi(1+X^{100}zu)\). Therefore, if \(q<T_n\),
\[
\|f_{{\rm Leg},n,q}-f_n\|_*
\le U\le YP_n/T_n^2
\le YP_n\sqrt{\log(eq)}/q^2.
\]
If \(T_n<1\), the already proved large-order case covers every
admissible integer. This completes (Legendre-simple-forward).

For (Legendre-structural-forward), the cap and \(\gamma/m\le X^4\)
give \(Y\le X^{-26}\le1\), so \(z\le m/\gamma\le\chi\).
Thus the two bracket factors in \(P_n\) are at most
\(2X^{100}\chi u\) and \(2X^{100}\chi^2e^u\).
Together with \(z^2\le\chi^2\), this gives
\(P_n\le12X^{300}\chi^5ue^u\le12X^{300}\chi^6ue^u\),
as asserted.

<a id="legendre-inverse-proof"></a>
#### Proof of the scalar inverses and their storage rates

For \(g(q)=\sqrt{\log(eq)}/q^2\),
\(g'/g=[2q\log(eq)]^{-1}-2/q<0\) on \([1,\infty)\),
and \(g(q)\to0\). Hence the minimum exists and every larger
integer works.

For \(r>1\), let \(\ell=\log(e+r)>1\). The chosen order lies
between \(2\sqrt r\ell^{1/4}\) and \(3\sqrt r\ell^{1/4}\),
and \(\log(eq_{\rm suff})\le4\ell\). The latter follows from
\(\log(3e)\le2\log(e+1)\le2\ell\),
\(\log r\le\ell\), and \(\log\ell\le\ell\).
Therefore \(r\sqrt{\log(eq_{\rm suff})}/q_{\rm suff}^2\le1/2\).
In particular this formula even leaves half of the error budget unused.


In the full-range certificate the other summand is \(UT_n^4/q^4\),
which is decreasing and tends to zero. Thus its sum with \(C_ng(q)\)
has a finite least integer inverse. Allocating \(\varepsilon/2\) to
each summand gives (Legendre-full-sufficient-order) directly, including
ratios at most one. Storage is affine and strictly increasing in \(q\),
so the floor in (Legendre-storage-inverse) is the largest feasible order.
At fixed positive labels, all finite recurrence coefficients except
\(M_n\) and \(\mathcal A_n\) are bounded by polynomials in
\(\sqrt{\log(en)}\), and \(\log\mathcal A_n\) is affine in
that quantity. Therefore \(C_n,T_n=n^{o(1)}\). Substitution in the
two sufficient inverse branches gives the stated polynomial-accuracy
orders and the exact storage formula gives their moving-state powers.

For (Legendre-root-width-order), put \(a=\log(e+Q_n)>1\).
Then \(4Q_na^{1/4}\le q_n\le5Q_na^{1/4}\) and
\(\log(eq_n)\le4a\), since \(Q_n\ge3\),
\(\log(5e)\le2a\), \(\log Q_n\le a\), and
\(\log a\le a\). The forward certificate is therefore at most
\(YP_n/(8Q_n^2)\le Y/(8\sqrt n)\), as stated.

<a id="compact-proofs"></a>
<a id="harmonic-proofs"></a>
### Harmonic proofs

<a id="compact-harmonic-proof"></a>
<a id="harmonic-expansion-proof"></a>
#### Proof of the source expansion and finite coefficient count

The argument first obtains decay in spherical degree from holomorphy on
the intrinsic tube. Temporal Fourier decay then produces a weighted
simplex of coefficients. This proves a finite-dimensional approximation
without evaluating any trained trajectory during runtime.

For \(d\ge2\), the intrinsic complex sphere tube of radius \(r\) is
\[
\mathcal Q_r=\{u\cosh h+i v\sinh h:
       u,v\in\mathbb R^d,\ \|u\|=\|v\|=1,\ u^Tv=0,\ |h|\le r\}.
\]
It equals \(\{z:z^Tz=1,\ \|\operatorname{Im}z\|\le\sinh r\}\):
write \(z=b+ic\), use \(b^Tc=0\) and
\(\|b\|^2-\|c\|^2=1\), and put
\(h=\operatorname{arsinh}\|c\|\). The case \(c=0\) permits any
unit tangent vector. This gives all intrinsic imaginary directions.

Let \(F\) be scalar, holomorphic near \(\mathcal Q_r\), and bounded
there by \(M\). Use normalized real-sphere measure. Harmonic
polynomials of degree \(j\), restricted to the sphere, form a space
\(\mathcal H_j\) of dimension
\[
h_j={j+d-1\choose d-1}-{j+d-3\choose d-1}
                  \le2{j+d-2\choose d-2}.
\]
Indeed every homogeneous polynomial decomposes uniquely into terms
\(\|x\|^{2k}H_{j-2k}(x)\) with harmonic \(H_{j-2k}\): induction
uses
\(\Delta(\|x\|^{2k}H_l)=2k(2l+2k+d-2)\|x\|^{2k-2}H_l\).
The coefficients are nonzero for \(k\ge1\); dimension counting gives
the formula. The polar Laplacian gives eigenvalue \(-j(j+d-2)\), so
integration by parts makes different degrees orthogonal.

Let \(P_j\) be the orthogonal projection onto \(\mathcal H_j\).
For a real orthonormal basis \(Y_{j,b}\), rotational invariance and
the trace of its reproducing kernel give
\(\sum_bY_{j,b}(x)^2=h_j\). Consequently
\[
\|P_jg\|_\infty\le h_j\|g\|_\infty,\qquad
|Y_{j,b}(x)|\le\sqrt{h_j}.
\tag{Harmonic projector bounds}
\]
To extract exponential decay, average over tangent directions:
\[
(A_\zeta F)(x)=\int_{v\perp x,\ \|v\|=1}
            F(x\cos\zeta+v\sin\zeta)\,d\sigma_x(v).
\]
This is holomorphic and bounded by \(M\) for
\(|\operatorname{Im}\zeta|\le r\). For \(d\ge3\), put
\(\nu=(d-2)/2\) and define \(C_j^\nu(t)\) by the generating
function \((1-2tw+w^2)^{-\nu}\). Differentiation of that generating
function gives
\[
(1-t^2)(C_j^\nu)''-(d-1)t(C_j^\nu)'
                +j(j+d-2)C_j^\nu=0,
\quad C_j^\nu(1)=(2\nu)_j/j!,
\]
where \((b)_j=b(b+1)\cdots(b+j-1)\) and \((b)_0=1\).
Averaging a degree-\(j\) harmonic over rotations fixing \(x\) gives
the unique zonal harmonic with its value at \(x\): write an invariant
homogeneous polynomial in powers of \(x^Ty\) and
\(\|y-(x^Ty)x\|^2\); its harmonic equation determines every
coefficient from the leading one. The resulting sphere equation is the
displayed differential equation. Hence on \(\mathcal H_j\),
\(A_\zeta\) acts by \(C_j^\nu(\cos\zeta)/C_j^\nu(1)\).

For real \(\zeta\), the joint law of \((x,x\cos\zeta+v\sin\zeta)\)
is symmetric, since it is the rotationally invariant law on pairs with
the specified inner product. Thus \(A_\zeta\) is self-adjoint.
Apply this identity to each harmonic coefficient, and continue the scalar
analytic identity to \(\zeta=ir\), to obtain
\[
P_jA_{ir}F=\frac{C_j^\nu(\cosh r)}{C_j^\nu(1)}P_jF.
\]
No harmonic expansion at complex points was used here. Factoring the
generating function into
\((1-e^rw)^{-\nu}(1-e^{-r}w)^{-\nu}\) and retaining one positive
term gives \(C_j^\nu(\cosh r)\ge e^{rj}(\nu)_j/j!\).
Moreover
\[
\frac{(2\nu)_j}{(\nu)_j}
 =2\prod_{k=1}^{j-1}\left(1+\frac\nu{\nu+k}\right)
 \le2\exp\left(\nu\int_0^{j-1}\frac{dx}{\nu+x}\right)
 \le2^d(j+1)^d.
\]
The first equality applies for \(j\ge1\); the last bound also holds
at zero. Together with the projector bound and
\(h_j\le2d^{d-2}(j+1)^{d-2}\), this proves
\[
\|P_jF\|_\infty\le MD_d(j+1)^{b_d}e^{-rj}.
\tag{Harmonic decay}
\]
For \(d=2\), averaging the two tangent directions has multiplier
\(\cosh(jr)\ge e^{jr}/2\); the same inequality holds with
\(D_2=8,b_2=2\). The bound makes the real-sphere harmonic series
absolutely uniformly convergent. Its sum equals \(F\): restrictions
of polynomials contain constants and separate points and are dense by
the real Stone--Weierstrass theorem; harmonic decomposition then makes
a continuous function with all harmonic coefficients zero vanish.

For a coordinate of any source family, substitute
\(t=T(1+\cos u)/2\). The resulting function is even and periodic in
\(u\). If \(|\operatorname{Im}u|\le\alpha_T\le1\), its imaginary
time displacement is at most \(T\alpha_T=r_t/4\) and its real
overshoot is at most \(T\alpha_T^2/2\le r_t\). Fourier contour
translation, first in time and then the proved harmonic estimate, gives
\[
\|P_jG_k\|_\infty\le
 M_nD_d(j+1)^{b_d}e^{-\alpha_T|k|-r_qj}.
\]
For \(0<r\le1\), comparison with the integral over successive unit
intervals proves
\[
\sum_{j\ge0}(j+1)^{b_d}e^{-rj/2}
 \le e^r b_d!(2/r)^{b_d+1}\le3b_d!(2/r)^{b_d+1},
\]
and \(\sum_{k\in\mathbb Z}e^{-\alpha_T|k|/2}\le6/\alpha_T\).
Split the omitted exponential into two halves. Outside
\(\alpha_T|k|+r_qj\le H(T,\eta)\), the total tail is at most
\(M_nP_Te^{-H(T,\eta)/2}=\eta/16\).

Evenness leaves one real cosine coefficient for each \(k\ge0\), and
each spherical degree has exactly \(h_j\) real coefficients. This is
the count in [the coefficient formula](#harmonic-variable-budget-theorem).
Using \(h_j\le2{j+d-2\choose d-2}\), the count is at most twice
the number of nonnegative integer \(d\)-tuples satisfying
\(\alpha_Tk+r_q\sum_{i=1}^{d-1}b_i\le H(T,\eta)\).
The disjoint unit cubes based at these tuples lie in the weighted
simplex enlarged by \(\alpha_T+(d-1)r_q\). Its volume yields
\[
N(T,\eta)\le
 \frac{2[H(T,\eta)+\alpha_T+(d-1)r_q]^d}
       {d!\alpha_T r_q^{d-1}}.
\tag{Harmonic simplex count}
\]
For \(d=1\), positive cosine coefficients are bounded by
\(2M_ne^{-\alpha_Tk}\). Since
\(1-e^{-\alpha_T}\ge\alpha_T/2\), omission above
\(H_1(T,\eta)/\alpha_T\) costs at most
\(4M_n\alpha_T^{-1}e^{-H_1(T,\eta)}=\eta/16\).
The two points of the sphere require two temporal families, so the
dimension bound is \(B+8N_1\); it is \(B+4N\) when \(d\ge2\).

<a id="compact-initial-jet-proof"></a>
<a id="harmonic-initial-jet-proof"></a>
#### Finite setup from the initialized network

The exact integral coefficients used above serve to prove the error
bound. Their finite approximations can be computed from initial
derivatives. The following explicit map supplies this fact for every
finite \(T\), even when the needed setup work is very large.
For this paragraph only put
\[
\chi=\frac{\pi T}{8r_t},\quad b_0=\tanh\chi,\quad
b_1=\tanh(\chi+\pi/4),\quad \vartheta=b_0/b_1,
\quad \psi(\xi)=\frac{\xi-\vartheta}{1-\vartheta\xi},
\]
\[
\mathfrak t(\xi)=\frac T2+\frac{2r_t}{\pi}
             \log\frac{1+b_1\psi(\xi)}{1-b_1\psi(\xi)}.
\tag{Harmonic initial jet map}
\]
The logarithm is the analytic branch zero when its fraction is one.
The disk automorphism has \(|\psi|<1\). For \(|w|<b_1\), the real
part of \(\log((1+w)/(1-w))\) has magnitude less than
\(2\operatorname{arctanh}b_1=2\chi+\pi/2\), and its imaginary
part has magnitude less than \(\pi/2\). Thus the map lies inside
the source rectangle, has \(\mathfrak t(0)=0\), and maps the real
interval \([0,\xi_*]\) onto \([0,T]\), where
\(\xi_*=2\vartheta/(1+\vartheta^2)<1\).

For a fixed real query and any source coordinate \(g\), its composed
Taylor coefficients are
\[
a_j=\sum_{k=0}^j\frac{\partial_t^kg(0)}{k!}
                         [\xi^j]\mathfrak t(\xi)^k.
\tag{Harmonic finite initial jet coefficients}
\]
They depend on only finitely many initial derivatives. Those derivatives
are obtained by finite differentiation of the dense ODE and passive
backward recursion, using the initial matrices and labels. Cauchy's
bound gives \(|a_j|\le M_n\). A degree-\(K\) Taylor sum therefore
has error at most \(M_n\xi_*^{K+1}/(1-\xi_*)\) at every required
real time. This tends to zero and has an explicit finite cutoff for any
positive nodal tolerance.

Choose each real harmonic basis by harmonic decomposition and
Gram--Schmidt of monomials. Its polynomial coefficients and sphere
integrals are fixed, finite data. Each retained coefficient is an
integral against a cosine and a harmonic polynomial. Finite Riemann
quadrature in the time angle and the ordinary real sphere angles
approximates it to arbitrary accuracy. This can be certified by Cauchy
derivative bounds in the time strip and along great circles, together
with the known polynomial derivatives and sphere Jacobian on compact
angle boxes. Finitely many coefficients permit one common quadrature
mesh and one common initial-jet cutoff.

If \(J=\lfloor H(T,\eta)/r_q\rfloor\), the real basis functions
have magnitude at most \(\max_{j\le J}\sqrt{h_j}\). Choosing each
coefficient error at most
\(\eta/[16N(T,\eta)\max_{j\le J}\sqrt{h_j}]\) makes their
total reconstruction error at most \(\eta/16\), including the
factor two converting positive Fourier modes to cosines in the
coefficient tolerance. Add the tail \(\eta/16\); there is ample
slack to obtain the asserted coordinate error \(\eta\).
The dimension-one case omits the harmonic factor.

For a paired initialized image, differentiation gives exactly
\(\partial_t^k(W_0g)=W_0\partial_t^kg\), and the same holds for
\(W_0^T\). Apply identical scalar linear operations in the Taylor
formula, quadrature and coefficient truncation to both members. Their
coefficient vectors then satisfy the image identity exactly. Each
member separately satisfies its coordinate error bound, since the
common nodal accuracy can be chosen for all members. No operator-norm
conversion of one member's coordinate error is used. This proves the
initialization-only paired-source construction, with finite real setup.

<a id="compact-selection-proof"></a>
<a id="harmonic-selection-proof"></a>
#### Coordinate selection and the exact source metric

The finite selection fact needed here is: if vectors \(v_i\in\mathbb R^r\)
satisfy \(\sum_i v_iv_i^T=I_r\), then there are nonnegative weights,
at most \(9r\) of them positive, for which
\(I_r\preceq\sum_i s_iv_iv_i^T\preceq4I_r\).
It is the sparsity-nine specialization of
[Batson, Spielman and Srivastava, Theorem 3.1](https://www.cs.cmu.edu/~odonnell/hits09/batson-spielman-srivastava-twice-ramanujan-sparsifiers.pdf).
For completeness the required specialization has the following direct
barrier proof.

Starting at \(A=0\), lower barrier \(l=-3r\), and upper barrier
\(u=6r\), maintain
\[
lI\prec A\prec uI,\qquad
\Phi_l(A)=\operatorname{tr}(A-lI)^{-1}\le1/3,\qquad
\Phi^u(A)=\operatorname{tr}(uI-A)^{-1}\le1/6.
\]
The barriers are moved by one and two, respectively, at each step.
For \(l'=l+1\), \(u'=u+2\), define
\[
U(v)=\frac{v^T(u'I-A)^{-2}v}{\Phi^u(A)-\Phi^{u'}(A)}
                         +v^T(u'I-A)^{-1}v,
\]
\[
L(v)=\frac{v^T(A-l'I)^{-2}v}{\Phi_{l'}(A)-\Phi_l(A)}
                         -v^T(A-l'I)^{-1}v.
\]
Both denominators are positive. Also \(A-l'I\) is positive:
\(\Phi_l\le1/3\) forces every eigenvalue's distance above \(l\)
to be at least three. The elementary rank-one inverse identity
\[
(B+\theta vv^T)^{-1}
 =B^{-1}-\frac{B^{-1}vv^TB^{-1}}{\theta^{-1}+v^TB^{-1}v}
\]
is verified by multiplication. Applied with either sign, it shows that
\(U(v)\le\theta^{-1}\le L(v)\), \(\theta>0\), preserves both
potential bounds at the shifted barriers. The upper denominator is
strictly positive because the first term in \(U(v)\) is positive for
nonzero \(v\); hence the upper spectral barrier is preserved as well.
The lower barrier is preserved by positivity of the rank-one addition.

Such a vector and step size always exist. Summing over \(i\) uses
\(\sum_i v_iv_i^T=I\). In the upper sum, each eigenvalue \(a_j\)
satisfies
\[
\frac1{u-a_j}-\frac1{u'-a_j}
       =\frac2{(u-a_j)(u'-a_j)}\ge\frac2{(u'-a_j)^2}.
\]
Thus \(\sum_iU(v_i)\le1/2+\Phi^{u'}(A)\le2/3\).
For the lower sum put \(a_j'=1/(a_j-l')\) and
\(b_j'=1/(a_j-l)=a_j'/(1+a_j')\), and let
\(D=\Phi_{l'}-\Phi_l=\sum_j a_j'b_j'\).
Weighted Cauchy--Schwarz and \(\sum b_j'\le1/3\le1\) give
\[
D^2\le\left(\sum_j(a_j')^2b_j'\right)\sum_jb_j'
 \le\sum_j(a_j')^2b_j'
 =\sum_j(a_j')^2-D.
\]
It follows that
\(\sum_iL(v_i)=\sum_j(a_j')^2/D-\Phi_{l'}
 \ge1-\Phi_l\ge2/3\).
Hence some nonzero \(v_i\) has \(L(v_i)\ge U(v_i)>0\).
Choose a positive \(\theta\) with reciprocal in that interval and
update \(A\) by \(\theta v_iv_i^T\). After \(9r\) steps the
barriers are \(6r\) and \(24r\). Dividing all accumulated weights
by \(6r\) proves the desired selection fact. Repeated choices only
reduce the final support size.

Apply this fact at a layer with \(v_i=(U_j)_{i,:}^T/\sqrt n\).
Its hypothesis is exactly \(U_j^TU_j/n=I\). Let \(P=(U_j)_{I_j}\)
and \(\mathsf D=\operatorname{diag}(s_i/n)\) on the positive
support. Then \(G=P^T\mathsf DP\) has spectrum in \([1,4]\).
Set \(Z=\mathsf D^{1/2}P\), and define
\[
M=\mathsf D^{1/2}
 [ZG^{-2}Z^T+I-ZG^{-1}Z^T]\mathsf D^{1/2}.
\tag{Harmonic source metric formula}
\]
The last two terms give the orthogonal projector on
\(\operatorname{ran}Z^\perp\); on \(\operatorname{ran}Z\) the
first term has the eigenvalues of \(G^{-1}\). Therefore
\(\mathsf D/4\preceq M\preceq\mathsf D\). Multiplication gives
\(P^TMP=GG^{-2}G+G-GG^{-1}G=I\). This is exact source isometry.
Since the constant is a source member, its empirical squared norm is
one, giving \(\mathbf1^TM\mathbf1=1\) and
\(\mathbf1^T\mathsf D\mathbf1\le4\).

If \(D\) is any coordinate multiplication operator, the diagonal
metric and the two metric comparisons imply
\(\|D\|_{M\to M}\le2\|D\|_{\infty\to\infty}\).
Thus activations are \(2s\)-Lipschitz in this metric, and
\(\|\phi_j(z)\|_M\le2b+2s\|z\|_M\). These estimates have no
minimum-weight factor. The metric adjoint of \(D\) is
\(M^{-1}DM\), which need not equal \(D\).

The initialized mixer in [the initialization formula](#harmonic-runtime-definition)
is the compression of \(W_0^{(j)}\) between two isometric source
spaces, so its norm is at most \(\|W_0^{(j)}\|\). If
\(g\in E_{j-1}\) and \(W_0^{(j)}g\in E_j\), direct substitution
gives its exact forward action on \(g_{I_{j-1}}\). Its metric
adjoint gives the exact reverse action whenever
\(d\in E_j\), \(W_0^{(j)T}d\in E_{j-1}\). The initial additions
therefore preserve the training forward pass by induction over layers,
and exact top isometry preserves its Gram. First-weight columns give
the first operator bound. This establishes every metric and initialization
property used by the Harmonic runtime.

<a id="compact-fitting-proof"></a>
<a id="harmonic-fitting-proof"></a>
#### Independent fitting and endpoint control

Work until the first exit from operator caps nine, sphere feature cap
\(2H_c\), or normalized Gram margin \(Q_C\succeq\lambda I/4\).
The local vector field is smooth on this open Gram-positive set.
Give raw parameter tuples the squared norm
\[
\|\theta_C\|_{\rm par}^2=
 \operatorname{tr}(A_C^TM_1A_C)
 +\sum_{j=2}^L\|M_j^{1/2}B_C^{(j)}M_{j-1}^{-1/2}\|_F^2
 +w_C^TM_Lw_C.
\]
Every term of \(K_C\) is a Gram matrix, using tensor products for
the hidden terms. Expanding the raw velocities, including all
cross-sample products, gives
\[
-\frac d{dt}\rho_C^2=4c_C^TK_Cc_C/m^2
       =\|\dot\theta_C\|_{\rm par}^2,
\qquad \rho_C=\|c_C\|_2/\sqrt m,
\qquad K_C/m\succeq Q_C.
\tag{Harmonic exact energy identity}
\]
This identity is algebraic and does not require gradient backpropagation.
The stopped gap implies \(-\dot\rho_C\ge\lambda\rho_C/2\).
Since \(\|\dot\theta_C\|^2=2\rho_C(-\dot\rho_C)\),
\(\|\dot\theta_C\|\le2(-\dot\rho_C)/\sqrt\lambda\). Hence
\[
\rho_C(t)\le Ye^{-\lambda t/2},\qquad
\int_0^t\rho_C\le2z,\qquad
\int_0^t\|\dot\theta_C\|\le2\alpha,\qquad
\|w_C(t)\|\le2\alpha.
\tag{Harmonic fitting energy bounds}
\]
If a zero deficit is reached, all velocities vanish, so the same bounds
continue with the constant solution.

Let \(P_C=V_CQ_C^{-1}V_C^*\), the orthogonal projector in the top
metric. The corrected readout is the orthogonal sum
\((I-P_C)w_C+V_CQ_C^{-1}(y-c_C)/\sqrt m\).
The two squared norms are at most \(4\alpha^2\) and
\(16\alpha^2\), respectively, proving
\(\|\widehat w_C\|\le\sqrt{20}\alpha<5\alpha\).
The gate and mixer bounds then give
\(\|\delta_{C,a}^{(j)}\|\le d_j^cR_c\).
Each hidden block velocity is at most \(2\rho_CR_cU_j^c\).
Its integral is at most \(20U_j^cY^2/\lambda^{3/2}\).
Subtracting the initialized forward pass propagates with factor
\(18s\), and the direct matrix term costs \(2s(2H_c)\);
these are exactly the recurrence defining \(F_j^c\). Therefore every
feature displacement is at most \(20F_j^cY^2/\lambda^{3/2}\).

The full label interval makes these bounds at most
\(5\sqrt\lambda/(64H_c^2)\), hence less than
\(1/(8H_c)\). Initialized features were bounded by \(H_c\), and
operators by eight, so both stopped caps improve strictly. The normalized
training-feature matrix changes in operator norm by less than
\(\sqrt\lambda/8\). Its initial smallest singular value is at least
\(\sqrt{\lambda/2}\), so it remains above
\((1/\sqrt2-1/8)\sqrt\lambda>\sqrt\lambda/2\).
The stopped Gram margin also improves. No finite first exit exists.
Bounded raw parameters and a strict Gram margin permit continuation at
every finite time. Finite total path length gives parameter convergence;
the readout formula gives effective-readout convergence; and
\(c_C\to0\) gives exact fitting.

For the endpoint coefficient set \(T_C=V_CQ_C^{-1}\) and
\(b_C=(y-c_C)/\sqrt m\). Differentiating the inverse and collecting
projectors yields
\[
\dot T_C=(I-P_C)\dot V_CQ_C^{-1}-T_C\dot V_C^*T_C,
\qquad
\dot P_C=(I-P_C)\dot V_CT_C^*+T_C\dot V_C^*(I-P_C).
\tag{Harmonic right inverse derivatives}
\]
The bounds are \(\|T_C\|\le2/\sqrt\lambda\),
\(\|\dot T_C\|\le8\|\dot V_C\|/\lambda\),
\(\|\dot P_C\|\le4\|\dot V_C\|/\sqrt\lambda\), and
\(\|\dot V_C\|\le2R_cF_c\rho_C\).
The Gram formula gives \(\|K_C/m\|\le G_c\), hence
\(\|\dot b_C\|\le2G_c\rho_C\), while
\(\|b_C\|\le2Y\), \(\|\dot w_C\|\le4H_c\rho_C\).
Differentiate \(\widehat w_C=(I-P_C)w_C+T_Cb_C\) to obtain
\(\|\dot{\widehat w}_C\|\le B_w^c\rho_C\).
For every unit query,
\(\|\dot h_C^{(L)}\|\le2R_cF_c\rho_C\), so
\(|\dot f_C(v)|\le B_f^c\rho_C\). Integration proves
\[
\sup_{\|v\|=1}|f_C(\infty,v)-f_C(t,v)|
        \le2B_f^cz e^{-\lambda t/2}.
\tag{Harmonic endpoint tail}
\]
Together with the dense source bound \(|\dot f_n(v)|\le2\mathcal K\rho_n\)
and its fitting tail, comparing the two flows to their values at \(T\)
costs at most \(\mathcal D e^{-\lambda T/4}\). Neither flow is frozen.
Finally \(\|\widehat w_C\|\le5\alpha\),
\(\|h_C\|\le2H_c\), \(\|w_n\|_2/\sqrt n\le2\alpha\),
and \(\|h_n\|_2/\sqrt n\le2H_d\) prove the baseline certificate.

<a id="compact-source-energy-proof"></a>
<a id="harmonic-source-energy-proof"></a>
#### Source metric estimates and reference energy

Fix a source horizon and coordinate tolerance \(\eta\le\eta_0\).
All norms of selected vectors in this proof use their layer metric;
dense vector norms always mean the explicitly normalized Euclidean
quantity \(\|u\|_2/\sqrt n\). If a vector \(u\) has an approximant
\(p\) in the source space with \(\|u-p\|_\infty\le e\), then
\[
\frac{\|u-p\|_2}{\sqrt n}\le e,\qquad
\|(u-p)_I\|_M\le2e,\qquad
\|u_I\|_M\le\frac{\|u\|_2}{\sqrt n}+3e.
\tag{Harmonic source norm transfer}
\]
The first two statements use the unit empirical mass and the diagonal
mass at most four; the last uses exact isometry of \(p\).
For two vectors with approximation errors \(e_u,e_v\) and dense RMS
bounds \(U,V\), insertion of their approximants in both pairings gives
\[
|\langle u_I,v_I\rangle_M-u^Tv/n|
          \le3(e_uV+e_vU)+9e_ue_v.
\tag{Harmonic source pairing transfer}
\]
For example the dense pairing error is at most
\(e_uV+e_vU+e_ue_v\), and the selected error at most
\(2e_uV+2e_vU+8e_ue_v\). Thus feature pairings cost at most
\(P_h\eta\), and response pairings at most \(SP_\delta\eta\),
using \(\eta\le1\) and \(\eta\le S\), respectively.

For proof only, define \(A_R=(A_n)_{I_1}\), \(w_R=(w_n)_{I_L}\),
and
\[
B_R^{(j)}(t)=B_C^{(j)}(0)+
 \int_0^t\frac2m\sum_a c_{n,a}(s)
       \delta_{n,a,I_j}^{(j)}(s)
       h_{n,a,I_{j-1}}^{(j-1)}(s)^TM_{j-1}\,ds.
\tag{Harmonic proof reference matrices}
\]
The true restricted features and responses need not be the forward and
backward pass through these matrices. The initial paired actions have
defect at most \((8\cdot2+2)\eta=18\eta\).
The exact dense rank-one integral and the pairing estimate show that the
learned forward defect is at most
\(S^2(\tau+3)P_h\eta\), and the learned reverse defect at most
\(S^2H_rP_\delta\eta\). Their total bounds are therefore
\(A_f\eta,A_b\eta\). Integrating the top-feature pairing defect
in the raw readout equation gives the observation bound
\[
\sup_{\|v\|=1}|\langle w_R,h_{n,I_L}^{(L)}(v)\rangle_{M_L}-f_n(v)|
                       \le16zP_h\eta.
\tag{Harmonic source action and observation defects}
\]
This estimate also applies to the normalized vector of training
observations, with no sample-count factor.

Let \(V_n\) have columns \(h_{n,a}^{(L)}/\sqrt m\), acting into
the dense RMS space, and let \(V_R\) have the restricted columns in
the selected space. The normalized column-error Hilbert--Schmidt norms
are at most \(\eta\) and \(2\eta\). Thus, for every sample vector,
\[
\|V_R\xi\|\le\|V_n\xi\|+3\eta\|\xi\|_2.
\]
Set \(\nu(t)=\|V_Rc_n/\sqrt m\|\).
The dense path length and \(\dot w_n=2V_nc_n/\sqrt m\) give
\(\int_0^T\nu\le\alpha+6\eta z\).
Integrating the existing top-feature approximants against
\(2c_{n,a}/m\) gives a vector in the fixed source space within
coordinate error \(4\eta z\) of \(w_n\). Finite Riemann sums and
closedness of the finite-dimensional source space justify this integral.
The norm transfer therefore gives
\(\|w_R\|\le2\alpha+12\eta z\).
Because \(\eta\le Y\) and
\(\eta/\sqrt\lambda\le\alpha\le1/16\), these imply
\[
\int_0^T\nu\le2\alpha,\qquad \|w_R\|\le3\alpha.
\tag{Harmonic selected readout energy}
\]
The same transfer applied to true dense responses gives
\[
\|\delta_{n,a,I_j}^{(j)}\|
 \le2s(9s)^{L-j}\alpha+3\eta\le d_j^E\alpha.
\tag{Harmonic selected response energy}
\]
Here \(\eta\le Y=\sqrt\lambda\alpha\le H_c\alpha\).
This step is why no assumption \(\lambda\le1\) is needed. No source
error was differentiated in any of these arguments.

<a id="compact-cancellation-proof"></a>
<a id="harmonic-cancellation-proof"></a>
#### Full-range readout and deficit cancellation

Let \(\mathcal J_C\) map sample space into the direct sum of hidden
parameter Hilbert spaces, with columns divided by \(\sqrt m\) equal to
\[
\left(\delta_{C,a}^{(1)}v_a^T,
 \bigl(\delta_{C,a}^{(j)}h_{C,a}^{(j-1)T}M_{j-1}\bigr)_{j=2}^L\right).
\]
Define \(\mathcal J_R\) using the true restricted dense features and
responses. A rank-one map \(u v^TM\) has Hilbert--Schmidt norm
\(\|u\|\|v\|\), so the definitions give exactly
\[
\dot\theta_{h,C}=2\mathcal J_Cc_C/\sqrt m,\quad
\dot\theta_{h,R}=2\mathcal J_Rc_n/\sqrt m,\quad
K_C/m=V_C^*V_C+\mathcal J_C^*\mathcal J_C,
\]
\[
\|\mathcal J_C\|\le J_C\alpha=5\alpha\sqrt{F_c},\qquad
\|\mathcal J_R\|\le J_R\alpha.
\tag{Harmonic hidden velocity identities}
\]
The norm bounds use the normalized sum of squared column norms, which
dominates the operator norm and introduces no factor \(\sqrt m\).

Write
\[
a_h=\|\theta_{h,C}-\theta_{h,R}\|,\quad
e=(c_C-c_n)/\sqrt m,\quad u=\|e\|_2,\quad
z_w=w_C-w_R,\quad T_C=V_CQ_C^{-1},\quad P_C=T_CV_C^*,
\]
\[
p=T_Ce,\qquad \zeta=z_w+p,\qquad
b_e=\|p\|+\|\zeta\|,\qquad E=a_h+b_e.
\]
These are proof variables and are initially zero. The right inverse
satisfies \(T_C^*T_C=Q_C^{-1}\), \(V_C^*T_C=I\),
\(T_CV_C^*=P_C\), and \(\|T_C\|\le2/\sqrt\lambda\).
Forward subtraction with the paired action defect gives
\[
\sup_{j,v}\|h_C^{(j)}(v)-h_{n,I_j}^{(j)}(v)\|\le F(a_h+\eta),
\qquad \|V_C-V_R\|\le F(a_h+\eta).
\tag{Harmonic forward difference}
\]
Layer one costs \(a_h\) in preactivation; later layers cost
\(9\) times the lower feature difference, \(H_ra_h\) for the
changed mixer, and \(A_f\eta\) for the action defect. Multiplication
by the gate bound \(2s\) proves the defining recurrences for
\(F_j^z,F_j^h\), and hence this inequality.

Let \(\Delta V=V_C-V_R\) and
\(d_R=V_R^*w_R-(y-c_n)/\sqrt m\). Substitution in the corrected
readout gives the exact identity
\[
\widehat w_C-w_R=(I-P_C)z_w-p-T_C\Delta V^*w_R-T_Cd_R.
\]
Since \((I-P_C)p=0\), the preceding energy and observation bounds yield
\[
\|\widehat w_C-w_R\|
       \le b_e+6zF(a_h+\eta)+32zP_h\eta/\sqrt\lambda.
\tag{Harmonic effective readout difference}
\]
In particular, for every query,
\[
|f_C-f_n|\le
 H_C\|\widehat w_C-w_R\|+3\alpha F(a_h+\eta)+16zP_h\eta.
\tag{Harmonic query output difference}
\]

The source Gram defect
\(D=V_R^*V_R+\mathcal J_R^*\mathcal J_R-K_n/m\) obeys
\(\|D\|\le D_s\eta\). To see every term, feature pairings cost
\(P_h\eta\), response pairings cost \(SP_\delta\eta\), and the
hidden products are split as
\(a_Rb_R-ab=(a_R-a)b_R+a(b_R-b)\).
Their bounds are \(SP_\delta H_r^2\eta\) and
\(S^2\tau^2P_h\eta\). The first-layer input pairing is at most
one. Summing gives exactly \(D_s\). A matrix whose entries have
magnitude at most \(d\) has operator norm at most \(md\); the
normalization by \(m\) removes this factor.
Writing \(\Delta\mathcal J=\mathcal J_C-\mathcal J_R\), the exact
factorization is
\[
\Delta\mathcal K:=K_C/m-K_n/m
 =V_C^*\Delta V+\Delta V^*V_R
   +\mathcal J_C^*\Delta\mathcal J
   +\Delta\mathcal J^*\mathcal J_R+D.
\tag{Harmonic factored Gram difference}
\]
Its second feature term will be controlled by the actual selected
readout velocity \(\nu\), retaining its energy scale.

Subtracting the exact deficit and raw-readout equations gives
\[
\dot e=-2(Q_C+\mathcal J_C^*\mathcal J_C)e
                -2\Delta\mathcal Kc_n/\sqrt m,
\qquad \dot z_w=2V_Ce+2\Delta Vc_n/\sqrt m.
\]
Using \(T_CQ_C=V_C\), the terms \(2V_Ce\) cancel after lifting
the deficit error:
\[
\dot\zeta=2\Delta Vc_n/\sqrt m+\dot T_Ce
       -2T_C\mathcal J_C^*\mathcal J_Ce
       -2T_C\Delta\mathcal Kc_n/\sqrt m.
\tag{Harmonic exact readout cancellation}
\]
Only the actual Harmonic feature map is differentiated. The derivative
identity already proved and \(Q_C^{-1}e=T_C^*p\) imply
\[
\|\dot T_Ce\|\le40zF_c\rho_C\|p\|.
\]
In the equation for \(p=T_Ce\), pairing with \(p\) gives the
negative term \(-2\langle p,V_Ce\rangle=-2u^2\).
The hidden Gram need not be dissipative in this lifted metric. Its
absolute contribution is bounded by
\[
2\|p\|\|T_C\|\|\mathcal J_C\|^2u
 \le8\|\mathcal J_C\|^2u^2/\lambda
 \le200z^2F_cu^2\le\frac{25}{32H_c^2}u^2.
\tag{Harmonic hidden Gram absorption}
\]
At least \(39u^2/32\) remains dissipative. Thus this absorption uses
precisely the full runtime label allowance.

Put \(\mathcal F=2\|T_C\Delta\mathcal Kc_n/\sqrt m\|\) and
\[
I(t)=\int_0^t[40zF_c\rho_Cb_e+\mathcal F]\,ds.
\]
Replace \(\|p\|\) by \((\|p\|^2+\vartheta^2)^{1/2}\) in the
norm calculation, integrate, and let \(\vartheta\downarrow0\).
The nonnegative damping integrands increase to \(u^2/\|p\|\),
defined as zero when \(p=0\), since then \(e=V_C^*p=0\).
Monotone convergence proves
\[
\|p(t)\|+\int_0^t\frac{u^2}{\|p\|}\,ds\le I(t),\qquad
\int_0^tu\,ds\le\frac2{\sqrt\lambda}I(t).
\tag{Harmonic lifted error integrals}
\]
The second inequality uses \(\|p\|\le2u/\sqrt\lambda\).
In the equation for \(\zeta\), the integrated hidden-Gram term
therefore costs at most \(200z^2F_cI\le25I/32\). Consequently
\[
b_e(t)\le2F\int_0^t\rho_n(a_h+\eta)\,ds+3I(t).
\tag{Harmonic readout error integral}
\]

Let \(M=1+32zK_{\rm src}\sqrt{\log(en)}\); the all-time carrier
extension proved below bounds every actual dense training carrier by
\(M\). Subtract backward responses by the exact identity
\[
\delta_C^{(j)}-\delta_R^{(j)}
 =\phi_j'(z_C^{(j)})\odot(k_C^{(j)}-k_R^{(j)})
 +[\phi_j'(z_C^{(j)})-\phi_j'(z_R^{(j)})]\odot k_R^{(j)}.
\]
The second term costs at most
\(2t_2MF_j^z(a_h+\eta)\). The first term propagates the upper
response difference with coefficient \(18s\), adds the changed mixer
times a true response of norm at most \(d_{j+1}^E\alpha\), and
adds \(2sA_b\eta\). At the top use the effective-readout estimate.
These terms are exactly the recurrence for \(B_j\). Subtracting each
rank-one hidden direction next gives
\[
\|\Delta\mathcal J\|
 \le B_h[b_e+M(a_h+\eta)+\eta/\sqrt\lambda].
\tag{Harmonic hidden direction difference}
\]
The factor \(M\) is added in the gate forcing, so it appears once,
rather than being multiplied at every layer.

Apply the factored Gram difference in its displayed order. The projector
identity \(T_CV_C^*=P_C\) handles the first feature term, and the
second term uses \(\nu\). The result is
\[
\begin{split}
\mathcal F\le{}&2F\rho_n(a_h+\eta)
 +4F\nu(a_h+\eta)/\sqrt\lambda\\
&+4z(J_C+J_R)B_h\rho_n
        [b_e+M(a_h+\eta)+\eta/\sqrt\lambda]
 +4D_s\eta\rho_n/\sqrt\lambda.
\end{split}
\tag{Harmonic factored forcing bound}
\]
The hidden-parameter equation and the lifted-error integral give
\[
a_h(t)\le\frac54I(t)+2B_h\int_0^t\rho_n
       [b_e+M(a_h+\eta)+\eta/\sqrt\lambda]\,ds,
\]
because \(4zJ_C=20z\sqrt{F_c}\le5/(4H_c)\le5/4\).
Adding the two error bounds and enlarging \(17I/4\) to \(5I\)
gives
\[
E(t)\le\int_0^t
 [200zF_c\rho_C+K_1M\rho_n+20F\nu/\sqrt\lambda]
              [E+\eta(1+\lambda^{-1/2})]\,ds.
\tag{Harmonic scalar comparison}
\]
Here
\(b_e+M(a_h+\eta)+\eta/\sqrt\lambda
 \le M[E+\eta(1+\lambda^{-1/2})]\).
Both source-error terms are required; replacing their sum by a maximum
without a factor would be incorrect.
For a nonnegative coefficient \(b(t)\), the integral inequality
\(E\le\int b(E+c)\), with \(E(0)=0\), is bounded by the
solution \(c(e^{\int b}-1)\): differentiate its integral majorant
and apply the integrating factor \(e^{-\int b}\).
Using \(\int\rho_C,\int\rho_n\le2z\) and
\(\int\nu\le2\alpha\) therefore proves
\[
E(t)\le\eta(1+\lambda^{-1/2})(e^{\mathcal B_n}-1).
\tag{Harmonic scalar comparison conclusion}
\]
Insert this bound into the query-output inequality. Its coefficients
are precisely \(\mathcal A_n\), proving the finite-horizon error
certificate. The separately proved endpoint tails give the all-time
certificate, including the limiting predictors.

<a id="compact-full-range-domination-proof"></a>
<a id="harmonic-full-range-domination-proof"></a>
#### Why the comparison exponent has numerical coefficients

This verification retains the existing source and runtime label caps.
Only in this calculation put \(r=L-1\), \(r_0=10s\),
\(u_0=H_L^{\rm src}\), \(p_0=P_L^{\rm src}\),
\(\kappa=(9/5)^r\), and \(A_0=(18s)^r=\kappa r_0^r\).
The positive source recurrences give
\[
u_0\ge20sr_0^r,\quad p_0\ge3r_0^r,\quad
\tau=su_0r_0^r,\quad H_c\le2\kappa u_0.
\]
The last comparison is an induction from
\(2b+16s\le2(b+20s)\) and \(18s=(9/5)10s\).
The last entry of the source allowance implies
\[
z\le\frac1{16\sqrt{8D_0C_F}}
  \le\frac1{16\sqrt8\,\tau u_0\sqrt s}.
\tag{Harmonic source smallness consequence}
\]
Here the source definitions give \(D_0\ge\tau^2\) and
\(C_F\ge su_0^2\). Since \(P_h\le7u_0\),
\(P_\delta\le7\tau\), \(H_r\le2u_0\), the corrections to
18 in \(A_f,A_b\) are at most
\(14\tau u_0/(8s\tau^2u_0^2)<1\). Thus \(A_f,A_b\le19\).

Unroll the forward subtraction recurrence and use
\(2s/(18s-1)\le1/8\) to get
\[
F\le A_0\left[2s+(H_r+A_f)/8\right]\le u_0A_0,
\qquad \max_jF_j^z\le F/(2s).
\]
The last step uses \(H_r+A_f\le u_0+22\) and \(u_0\ge20s\ge20\).
Also \(d_j^E\le7\kappa u_0\), so the same smallness bound gives
\[
(\max_jd_j^E)zH_c\le1,\qquad 6zF\le1,\qquad32zP_h\le1.
\]
For the first inequality it suffices to use
\(14\kappa^2/(16\sqrt8\,s r_0^r)\le1\), since
\(\kappa^2/r_0^r\le(3.24/10)^r\). The other two have the
additional factors \(u_0,\tau\ge20\) in their denominators.
The backward recurrence now has terminal value at most
\(6s+t_2F/s\) and forcing at most \(40s+t_2F/s\). Its geometric
sum therefore gives
\[
\max_jB_j\le A_0(9s+2t_2F/s)
                      \le3t_2u_0A_0^2/s.
\]
Here \(9sA_0\le t_2u_0A_0^2/s\), because
\(u_0\ge20s\), \(A_0\ge18s\), and \(t_2\ge1\).
Substituting in \(B_h\), with \(H_C\le4\kappa u_0\), gives
\[
B_h\le13\sqrt L\,\kappa^3t_2u_0^2r_0^{2r}/s
                    \le t_2u_0^2p_0^3.
\]
For the last inequality,
\(\sqrt L\kappa^3\le r_0^r\): the ratio at \(L=2\) is
\(\sqrt2(5.832/10)<1\), and each next step multiplies it by at
most \(\sqrt{3/2}(5.832/10)<1\). Now use
\(p_0\ge3r_0^r\) and \(13/(27s)\le1\).

The runtime allowance gives \(zJ_C\le5/(16H_c)\le5/16\).
Moreover \(J_R\le14\sqrt L\kappa u_0^2\), whence
\(zJ_R\le14/(16\sqrt8)<1/3\), using
\(\sqrt L(1.8/r_0)^r\le1\). Therefore
\(z(J_C+J_R)<1\).
Substitute the sharper smallness bound, including \(\sqrt s\), in
the three terms defining \(D_s\). They are bounded by
\(7u_0\), \(10Lu_0\), and \((3+L)/u_0\), respectively; the
last term alone is at most \(7L/(8su_0)\).
Thus \(D_s\le15Lu_0\), and
\[
K_1\le400t_2u_0^2p_0^3.
\tag{Harmonic polynomial coefficient bound}
\]
Indeed the coefficients of the terms bounded by
\(t_2u_0^2p_0^3\) total at most \(12+22+300=334<400\).

The stronger source entry also gives
\[
D_0\ge2t_2^2u_0^2p_0^4,\qquad D_*\ge t_2p_0^2,
\qquad W_{\rm G}\ge u_0^3.
\]
The first two use the top terms of the source trace recurrences.
For the third,
\(W_{\rm G}\ge128sV_L\ge128s^2u_0(H_{L-1}^{\rm src})^2\)
and \(u_0\le(10s+1)H_{L-1}^{\rm src}\le11sH_{L-1}^{\rm src}\),
so the lower bound is at least \((128/121)u_0^3\).
Write \(\eta_{\rm src}\) for the exponential-budget coefficient
in the source allowance. Its definition implies
\(\eta_{\rm src}^{-1}\ge8192D_0W_{\rm G}\), and
\(D_1\mathcal B\ge D_*^3\). The fourth-root source entry yields
\[
z\le\frac1{16}(8192D_0W_{\rm G}D_*)^{-3/4}.
\]
Combining these inequalities proves
\[
zK_1\le\frac{25}{2^{21/2}}
                t_2^{-5/4}u_0^{-7/4}p_0^{-3/2}\le1.
\]
Also \(C_G=32\tau\),
\(C_{\rm abs}=8(D_0+1)\le16D_0\), and \(\tau\ge1\), so
\(K_{\rm src}\le8448D_0\tau\). Consequently
\[
\begin{split}
z^2K_1K_{\rm src}
&\le\frac{13200}{8192^{3/2}}
 \frac{t_2u_0^2p_0^3\tau}{\sqrt{D_0}W_{\rm G}^{3/2}D_*^{3/2}}\\
&\le\frac{13200}{\sqrt2\,8192^{3/2}}
               \frac{\tau}{t_2^{3/2}p_0^2u_0^{7/2}}\le1.
\end{split}
\]
The last step substitutes \(\tau=su_0r_0^r\),
\(p_0\ge3r_0^r\), \(u_0\ge20s\); the remaining numerical
coefficient is less than one. Finally the first smallness bound and
\(F\le u_0A_0\) give
\(zF\le\kappa/(16\sqrt8\,su_0)\le1\). We have proved
\[
zK_1\le1,\qquad zF\le1,\qquad z^2K_1K_{\rm src}\le1.
\tag{Harmonic full range absorptions}
\]
Together with \(400z^2F_c\le25/(16H_c^2)\), these imply
\[
\mathcal B_n\le44+64\sqrt{\log(en)}.
\tag{Harmonic numerical exponential bound}
\]
No structural factor has been moved into a width threshold.

For explicit power envelopes put \(X=\beta^L\ge100\) only in
this calculation. Unrolling the positive source recurrences gives
\[
H_j^{\rm src}\le3\beta^{2j},\quad
P_j^{\rm src}\le\beta^{3j-2},\quad
k_j^{\rm src}\le3\beta^{4L-2j},\quad
\tau_j^{\rm src}\le3\beta^{4L-2j+1}.
\]
For example the feature affine recurrence is bounded by
\(22\beta(10\beta)^{j-1}\); the derivative recurrence is bounded
by \(4j(10\beta)^{j-1}\). Use \(10s\le\beta^2\) and
\(4j\le\beta^j\). Substitution in the trace recurrences gives
\(A_*\le\beta^{5L-2}\), \(D_*\le\beta^{6L-2}\),
\(H_*\le\beta^{8L-2}\), \(E\le\beta^{6L-2}\), and
\(D_0\le\beta^{16L-2}\). These follow by summing geometric powers
with ratio at most \(\beta^{-1}\); the outer factor in \(D_0\)
is at most \(2\beta\), and its inner sum is at most
\(4\beta^{16L-4}\). Thus \(C_{\rm abs}\le\beta^{16L-1}\)
and \(C_G\le96\beta^{4L-1}\), proving
\(K_{\rm src}\le1552\beta^{20L-2}\le X^{21}\).
The runtime recurrence gives \(H_c\le X^3\) and \(F_c\le X^{15}\).
The preceding comparison bounds give
\[
u_0,p_0,H_c\le X^3,\quad F\le X^6,\quad
K_1\le X^{17},\quad K_{\rm src}\le X^{21}.
\]
For \(K_1\), use
\(400t_2u_0^2p_0^3\le400X^{31/2}\le X^{17}\), since
\(t_2\le\beta\le X^{1/2}\) and \(X\ge100\).
The explicit formula for \(\mathcal B_n\) now gives
\[
\mathcal B_n/z\le71X^{38}(1+\sqrt{\log(en)}).
\]
Indeed its four coefficients are bounded by
\(25X^{15},2X^{17},40X^6,4X^{38}\sqrt{\log(en)}\).
The coefficient of \((e^{\mathcal B_n}-1)(1+\lambda^{-1/2})\)
in \(\mathcal A_n\) is at most \(17X^3\); its remaining terms
total at most \(575zX^9(1+\lambda^{-1/2})\).
Using \(e^b-1\le be^b\) proves
\[
\mathcal A_n\le2000e^{44}\beta^{42L}\frac{Ym}{\gamma}
 \left(1+\sqrt{\frac m\gamma}\right)
 (1+\sqrt{\log(en)})e^{64\sqrt{\log(en)}}.
\tag{Harmonic numerical prefactor bound}
\]
For the tails, the runtime cap gives
\(G_c\le5H_c^2\),
\(B_w^c\le25H_c^2\max(1,\lambda^{-1/2})\), and
\(B_f^c\le51H_c^3\max(1,\lambda^{-1/2})\).
For example \(48R_cF_cz\le15/(16H_c)\), and
\(2R_c^2F_c\le50/256\), which verify the latter two bounds
term by term. The source smallness bound gives
\(\mathcal K\le2u_0^2\): its hidden sum is at most
\(LS^2\tau^2u_0^2\le L/(8s)\le u_0^2\).
Therefore
\[
\mathcal D\le236\beta^{9L}\frac{Ym}{\gamma}
                        \left(1+\sqrt{\frac m\gamma}\right).
\tag{Harmonic numerical tail bound}
\]

The optional original-tolerance refinement follows from the same
coefficients. On \(z\le X^{-30}\), let \(\mathcal B_n^{(0)}\)
have coefficient 32 in its last term. The preceding powers give
\[
\mathcal B_n^{(0)}\le1+\sqrt{\log(en)},\qquad
\mathcal B_n^{(0)}/z\le X^{18}(1+\sqrt{\log(en)}).
\]
For the first inequality the four terms are at most
\(400X^{-45},2X^{-13},40X^{-24},32X^{-22}\sqrt{\log(en)}\).
For the second they are at most
\(400X^{-15},2X^{17},40X^6,32X^8\sqrt{\log(en)}\).
These sums have the displayed bounds already at \(X=100\).
The exact output coefficient is therefore at most
\[
\mathcal A_n^{(0)}\le
 [17eX^{21}+575X^9]z(1+\lambda^{-1/2})e^{2\sqrt{\log(en)}}
 \le X^{22}z(1+\lambda^{-1/2})e^{2\sqrt{\log(en)}}.
\]
The tail coefficient is at most \(236X^9z(1+\lambda^{-1/2})\),
and \(e^{-8\log(en)}\le1/n\). These inequalities imply the
displayed coefficient \(10X^{40}\), with considerable slack.
Finally, for \(r=\sqrt{\log(en)}\),
\(2r\le r^2/2+2\), so
\(n^{-1}e^{2r}\le e^{5/2}n^{-1/2}\).
Use \(\lambda^{-1}(1+\lambda^{-1/2})
\le2(1+\lambda^{-1})^2\) and \(20e^{5/2}<250\) to obtain the
stated numerical root-width bound. This specialization does not impose
its smaller cap on the full-range Harmonic theorem.

<a id="compact-analytic-extension-proof"></a>
<a id="harmonic-analytic-extension-proof"></a>
#### All finite source horizons on the same event

The original source event supplies joint time/query holomorphy through
\(T_0\), with the radii \(r_t,r_q\), and preactivation imaginary
parts at most \(a/4\). We extend this domain deterministically using
the dense late-time path length. Use the dense parameter norm
\[
\|\theta\|_{\rm par}^2=\|A\|_F^2/n+
                  \sum_{j=2}^L\|W^{(j)}\|_F^2+\|w\|_2^2/n,
\]
with its usual complex Euclidean extension. The dense energy identity
and gap imply, for every real \(t\),
\[
\int_t^\infty\|\dot\theta(s)\|_{\rm par}\,ds
       \le2\rho_n(t)/\sqrt\lambda
       \le2\alpha e^{-\lambda t/2}.
\tag{Harmonic late dense parameter tail}
\]
This is the same pointwise bound
\(\|\dot\theta\|\le2(-\dot\rho_n)/\sqrt\lambda\) used in fitting.

Consider the complex parameter ball of radius \(b_n\) around
\(\theta(T_0)\). The dense real operator bounds improve below
\(8+1/8\), so the ball stays inside cap ten. The real readout is
at most \(2\alpha\le SH_L^{\rm src}/8\), and the ball keeps it
below \(SH_L^{\rm src}\). On a straight parameter segment stopped
at a first query-strip exit, the source forward derivative recurrence
bounds preactivation RMS differentials by
\(P_j^{\rm src}\|d\theta\|_{\rm par}\): the first direct map
costs at most two, later direct maps at most \(H_{j-1}^{\rm src}\),
and propagation at most \(10s\). Coordinate differentials are
bounded by \(\sqrt nP_j^{\rm src}\|d\theta\|_{\rm par}\).
The radius definition limits the change to \(a/8\), so all query
preactivations stay below imaginary part \(3a/8\). This strictly
improves the stopped boundary. Linear growth now gives the original
complex RMS source bounds throughout the ball.

On that ball the complex algebraic residual Gram has norm at most
\(\mathcal K\), and
\(\|\dot\theta\|_{\rm par}\le2\sqrt{\mathcal K}\rho_n\).
These estimates use absolute Cauchy--Schwarz, not positivity of a complex
Gram. Fix any real anchor \(t\ge T_0\), and continue its finite
analytic ODE along a complex segment of length at most \(2r_t\),
stopped in this same ball. The deficit equation gives
\[
\rho_n(\zeta)\le\rho_n(t)e^{2\mathcal K|\zeta-t|}
                     \le2\rho_n(t),\qquad
\|\theta(\zeta)-\theta(t)\|_{\rm par}
                     \le8r_t\sqrt{\mathcal K}\rho_n(t).
\]
The original radius gate supplies \(4\mathcal Kr_t\le\log2\).
The late-time parameter tail and the first analytic-extension gate
therefore keep this solution strictly within half of the fixed ball
around \(\theta(T_0)\).

For clarity, local holomorphic existence here follows by Picard
iteration on a smaller closed parameter ball: the holomorphic vector
field has bounded derivative there, so its integral map is a contraction
on a sufficiently small complex time disk. The strict interior bound
allows repeated continuation to the whole disk of radius \(2r_t\).
A finite-radius obstruction would have a bounded state a positive
distance from the boundary, where the same local argument extends it.
Uniqueness glues overlapping germs. The disks at all real anchors cover
every late source rectangle with strict slack, and the parameter ball
leaves strict margin below the activation half-strip. The earlier source
domain already has a holomorphic neighborhood. Compactness of each
finite closed time/query domain gives such a neighborhood for every
finite \(T\), without reducing either radius. All anchors use one
fixed ball, so no accumulated continuation error or new stochastic event
is involved. The four source families retain coordinate bound \(M_n\).

The comparison requires a coordinate maximum only for the actual real
training carriers. Between two real states in the operator tube, forward
subtraction bounds preactivation RMS changes by
\(P_j^{\rm src}\|\Delta\theta\|_{\rm par}\). Converting this to
a coordinate maximum costs \(\sqrt n\). In the backward recursion,
the changed mixer costs \(S\tau_{j+1}^{\rm src}\|\Delta\theta\|\),
the propagated carrier difference costs \(10s\), and the changed
gate costs
\(10t_2SP_{j+1}^{\rm src}k_{j+1}^{\rm src}\sqrt n\|\Delta\theta\|\).
The top carrier is just the readout. Induction gives exactly the
recurrence for \(C_j^k\), and a final RMS-to-coordinate conversion
proves
\[
\max_{a,j}\|k_{n,a}^{(j)}(t)-k_{n,a}^{(j)}(T_0)\|_\infty
                  \le C_{\rm carrier}n\|\theta(t)-\theta(T_0)\|_{\rm par}.
\]
The second extension gate and the late parameter tail make this at
most \(K_{\rm src}S\sqrt{\log(en)}\). Adding the source maximum
at \(T_0\) gives, simultaneously for all real times,
\[
\max_{a,j,i}|k_{n,a,i}^{(j)}(t)|
                 \le2K_{\rm src}S\sqrt{\log(en)}.
\tag{Harmonic all time carrier bound}
\]
This proves the value of \(M\) used in the comparison. The first
extension gate is eventual because its left side is a fixed multiple
of \(n^{-16}\), whereas \(b_n\) is bounded below by a fixed
positive multiple of \(n^{-1/2}\). The second is eventual by the
same comparison of powers. Neither changes the label interval.

<a id="compact-budget-inversion-proof"></a>
<a id="harmonic-budget-inversion-proof"></a>
#### Budget count, inversion and boundary cases

The simplex count and
\(\lambda^{-1}c_t^{-1}=1024(U/a)z^2\) give, for \(d\ge2\),
\[
\dim E_j\le B+
 \frac{2^{15}}{d!}\frac Ua z^2(\lambda T)c_q^{-(d-1)}
 \log(en)^{d/2}[H(T,\eta)+\alpha_T+(d-1)r_q]^d.
\tag{Harmonic variable rank bound}
\]
The factor four counts the four source families. In dimension one,
\[
\dim E_j\le B+8+
 2^{15}(U/a)z^2(\lambda T)\sqrt{\log(en)}H_1(T,\eta).
\tag{Harmonic variable rank bound in dimension one}
\]
The extra eight retain all temporal zero modes.

Set \(T(u)=T_0+4u/\lambda\), \(\eta(u)=\eta_0e^{-u}\),
for \(u\ge0\). Since \(P_T\) is proportional to \(T\),
\[
H(T(u),\eta(u))=H(T_0,\eta_0)+2u+
             2\log(1+u/[8\log(en)])
               \le H(T_0,\eta_0)+9u/4.
\]
Also \(\alpha_{T(u)}\le\alpha_{T_0}\) and
\(\lambda T(u)=32\log(en)+4u\le4(h_0+u)\).
The variable rank bound therefore gives
\[
\dim E_j\le B_*+\mathcal C_d(h_0+u)^{d+1}.
\tag{Harmonic one parameter rank bound}
\]
For \(d=1\),
\(H_1(T(u),\eta(u))\le H_1(T_0,\eta_0)+9u/8\), so the
same bound holds with slack in the factor \(9/4\). The error
certificate gives
\(\mathcal A_n\eta(u)+\mathcal De^{-\lambda T(u)/4}
=\mathcal E_1e^{-u}\).

For a supplied \(q\), the nonnegative value of \(u\) in the
construction formula makes this rank bound at most \(q/9\).
Since actual dimension is an integer, it is at most \(\lfloor q/9\rfloor\)
without first rounding the real upper bound upward. The selection theorem
then uses at most \(q\) coordinates. When that formula would give
negative \(u\), retain only the exact initialization additions; they
have rank at most \(B\), fit independently, and obey the baseline.
This proves the piecewise certificate. For \(q\ge18B_*\), the
weaker choice \(u=(q/(18\mathcal C_d))^{1/(d+1)}-h_0\), when
nonnegative, gives \(B_*+q/18\le q/9\). It proves the simpler
certificate. The inverse prescription is the same calculation with
\(u\) chosen to make \(\mathcal E_1e^{-u}\le\varepsilon\),
followed by the final integer ceiling. The exact coefficient counts
give the stated sharper discrete alternative.

For this activation-only calculation set \(X=\beta^L\).
The source recurrences imply
\[
H_{\max}^{\rm src},\max_j(sP_j^{\rm src})\le X^3,\quad
K_{\rm src}\le X^{21},\quad T_Q\le X^{14},\quad T_J\le X^8,
\quad\max_jq_j^{\rm src}\le X^8,\quad
\max_jb_j^{\rm ang}\le X^3.
\]
Here \(q_j^{\rm src}\) and \(b_j^{\rm ang}\) are the response
and angular coefficients in the source recurrence, not selected widths.
To check these last powers, its formulas give
\(g\le\beta^{5L-1}\),
\(q_j^{\rm src}\le\beta^{5L+3j-2}\),
\(b_j^{\rm ang}\le2\beta^{2j}\),
\(e_j\le2\beta^{5L+6j-4}\), and
\(a_j\le3\beta^{5j-2}\). The leading forcing grows by six powers
per layer in \(e_j\), and by five in \(a_j\), while propagation
is at most \(\beta^2\); geometric summation gives the stated factors
two and three. Substitution into the source definitions of \(T_Q,T_J\)
gives \(T_Q\le\beta^{14L-3}\), \(T_J\le\beta^{8L-1}\),
which imply the displayed bounds.
Using only \(S\le1\), the bracket in \(U_j\) is at most
\(2X^{14}\). Its full higher-layer expression is then bounded by
\(4X^{36}+32\sqrt{d+3}X^8+2\), and the corresponding query
expression by \(32\sqrt{d+3}X^3+4X^{30}+2\).
The first-layer expressions are smaller. Since \(X\ge100\),
\[
U\le X^{37}\sqrt{d+3},\quad V\le X^{31}\sqrt{d+3},\quad
U/a\le X^{38}\sqrt{d+3},\quad c_q^{-1}\le X^{32}\sqrt{d+3}.
\]
Consequently
\[
\mathcal C_d\le\frac{2^{17}(9/4)^d}{d!}
 \beta^{(32d+6)L}(d+3)^{d/2}
                (Ym/\gamma)^2\log(en)^{d/2}.
\tag{Harmonic full range rank envelope}
\]
Integrating \(\log x\) over \([1,d]\) gives \(d!\ge(d/e)^d\).
Together with \(d+3\le4d\), \(d^{1/(d+1)}\le2\), and
\(2\sqrt2e<8\), this implies
\[
\frac{(d!)^{1/(d+1)}}{(d+3)^{d/(2d+2)}}\ge\frac{\sqrt d}{8}.
\]
Use also \((18\cdot2^{17})^{1/(d+1)}\le1536\),
\((9/4)^{d/(d+1)}\le9/4\), and
\((32d+6)/(d+1)\le32\). The resulting numerical rate is
\[
\left(\frac q{18\mathcal C_d}\right)^{1/(d+1)}
\ge\frac{\sqrt d}{32768\beta^{32L}}
   \left(\frac q{(Ym/\gamma)^2\log(en)^{d/2}}\right)^{1/(d+1)}.
\tag{Harmonic explicit negative exponential rate}
\]
The original counting gates and \(\eta_0\ge1/n\) give
\(H(T_0,\eta_0)\le7\log(en)\), hence \(h_0\le9\log(en)\),
for \(d\ge2\). In dimension one, the stated temporal gate gives
\(H_1(T_0,\eta_0)\le(7/2)\log(en)\), since
\((3/2)\log\log(en)\le\log(en)\); hence \(h_0=8\log(en)\).

For \(D=(q/(18\mathcal C_d))^{1/(d+1)}\),
\[
\min\{1,e^{9\log(en)-D}\}\le e^{\log(en)-D/9}.
\]
If \(D\le9\log(en)\), the right side is at least one; otherwise
compare its exponent with \(9\log(en)-D\). Thus the simplified
certificate is at most \(en\mathcal E e^{-D/9}\).
The numerical prefactor and tail bounds, \(\eta_0\le1\),
\(H_d\le X^2\), \(\sqrt\lambda\le H_c\le X^3\), and
\(1+\sqrt{\log(en)}\le e^{\sqrt{\log(en)}}\) give
\[
\mathcal E\le4096e^{44}\beta^{42L}\frac{Ym}{\gamma}
 \left(1+\sqrt{\frac m\gamma}\right)e^{65\sqrt{\log(en)}}.
\]
Combine this with the negative exponential rate divided by nine to
obtain the numerical budget certificate, including its constant 294912.

If \(q\ge n\), take the full source space and \(M_j=I_n/n\),
and retain the original dense matrices. Along the dense trajectory,
\(w_C=w_n\), \(c_C=y-f_n\), and the readout correction is zero.
Metric adjoints are ordinary transposes; the hidden rank-one update has
exactly the factor \(1/n\) supplied by \(M_{j-1}\). Every Harmonic
equation therefore equals its dense counterpart. The positive Gram
margin and local uniqueness identify the trajectories for all time and
at the limit. This branch needs only fitting and exact full retention.

The learned count follows by counting the entries of the moving arrays.
The fixed metric and data counts follow by their matrix dimensions.
For the upper inventory, put
\(P=dq_1+\sum_{j=2}^Lq_jq_{j-1}\) only in this count. Two copies
of these blocks, at most three full metric-related matrices per layer,
four training arrays per layer, four top-layer vectors, four sample
Gram/solve matrices and two sample vectors use at most
\[
2P+3\sum_jq_j^2+4m\sum_jq_j+4q_L+4m^2+2m+m(d+1)
\]
real coordinates. This is a conservative upper count for the named
copies and caches, not a compulsory cache layout. Since each selected
dimension is at most \(9R\), while \(m,d\le R\) on the exact
initialization event when \(n\ge d\), this is bounded by
\((441L-102)R^2+m(d+1)\), and hence by
\(1020(L+1)R^2+10m(d+1)\). Diagonal comparison matrices may be
stored within the allowance of three full metric-related matrices.
In particular the factor
\(1020/81<13\) proves the supplied-budget inventory. The exact
positive top Gram forces \(q_L\ge m\); exact first-weight columns
force \(q_1\ge\operatorname{rank}A_0=\min(n,d)\) almost surely.
No conclusion for budgets below these ranks is inferred.

<a id="compact-source-provenance"></a>
<a id="harmonic-source-provenance"></a>
#### Read scope and claim boundary

This section consolidates the current study's source bridge, runtime
fitting, source energy, common-cap and full-range comparisons, analytic
tail extension, variable-source count and numerical power ledger. The
explicitly authorized dependency reads were the complete
`STORAGE_QUADRATIC_IMPROVEMENT.md`, `GENERAL_WEIGHTED_COMPARISON.md`,
`SPHERICAL_SOURCE_DIMENSION_ROUTE.md`, and
`DIMENSION_PREFACTOR_OPTIMIZATION.md` in `closure_sampling_20261003`.
Only their cited selection, metric, harmonic and finite-initial-jet
arguments are imported; their older bounded-activation assumptions,
capped gaps and older source counts are not substituted into this theorem.
The maintained notation contract and the rigorous-math instructions
were read. The separately required canonical-notation skill path was
unreadable; the accessible skill roots contained no replacement.

The resulting deterministic Harmonic implication is complete relative to
the shared source and dense initialization/fitting theorems. Its success
width still includes the source theorem's unquantified stochastic
threshold. The approximation measures predictor fidelity on known inputs,
not test risk for unknown labels. No claim of optimal rate, bounded-precision
compression, efficient setup, or ordinary-gradient Harmonic training follows.


<a id="headline-corollary-proofs"></a>
### Derivation of the headline inverses and storage corollaries

All finite-width certificates are the exact formulas in Part II.
This subsection explains the simplifications, without replacing a
deterministic coefficient by an unspecified constant.

For dense, use the numerical scalar prescription in
[the exact inverse](#dense-inverse-storage) and its proof below the
concentration argument. The selected width must also exceed the source
and, when used, lower-bound onset. For fixed problem and confidence, its
logarithm is
\(2\log(1/\varepsilon)+o(\log(1/\varepsilon))\).
The exact learned count \((L-1)n^2+n(d+1)\) therefore has exponent
\(4+o(1)\) in \(1/\varepsilon\).

For Legendre, the function
\(\sqrt{\log(eq)}/q^2\) is decreasing on \([1,\infty)\).
The exact simple-cap and full-range inverses in
[the inverse statement](#legendre-inverse-certificates) allocate error
explicitly and then round upwards. Substitution in
\(n(d+1)+1+2(L-1)mnq\) is the complete finite-width storage
certificate. The structural sufficient-order formula there retains
\([\log(en)\log(en/\varepsilon)]^{1/4}\); no identification of
these two logarithms is needed. At
\(n=\varepsilon^{-2+o(1)}\), that order is
\(\varepsilon^{-1/2+o(1)}\), so the moving count is
\(\varepsilon^{-5/2+o(1)}\). The fixed mixers still have
\((L-1)n^2=\varepsilon^{-4+o(1)}\) coordinates.

For Harmonic, its exact inverse and exact inventory provide the
unsuppressed storage formula
\[
13(L+1)
\left[
\max\left\{18(2m+d+9),
\left\lceil9\left[2m+d+9+
\mathcal C_d(h_0+u_\varepsilon)^{d+1}\right]\right\rceil
\right\}\right]^2+10m(d+1)
\tag{corollary-exact-harmonic-storage}
\]
whenever the analytic branch is used. The definitions of
\(\mathcal C_d,h_0,u_\varepsilon\) are exactly those in
[the supplied-budget statement](#harmonic-variable-budget-theorem).
For the loose-target branch use its initialization-only budget instead;
for the full-width branch use the exact retained dense arrays rather
than forcing a selected-rank estimate. Both branches are already
explicitly constructed in the Harmonic theorem.

For polynomial accuracy at fixed problem,
\(h_0=O(\log(en))\) and
\(u_\varepsilon=O(\log(en/\varepsilon))\).
The numerical rank envelope proved above gives
\(\mathcal C_d\) proportional to \(\log(en)^{d/2}\);
hence the sufficient Harmonic budget is
\(O(\log(en)^{3d/2+1})\). The inventory is quadratic in that budget,
giving \(O(\log(en)^{3d+2})\).
The separate \(m,d,L,\gamma\) factors in the headline follow by
squaring the exact rank envelope and using
\[
d!\ge(d/e)^d,\qquad
\frac{(d+3)^d}{(d!)^2}
\le \frac{(4e^2)^d}{d^d}
\le\frac{(8e^2)^d}{d^{d+1}}\quad(d\ge1).
\tag{corollary-factorial-elimination}
\]
The last step uses \(d\le2^d\); it does not set the structural
parameters equal. Numerical powers are absorbed only in the headline
activation-depth exponent. Taking
\(n=\varepsilon^{-2+o(1)}\) then gives the stated Harmonic
\(O(\log(1/\varepsilon)^{3d+2})\) storage.

For the dense necessary-storage statement, choose lower confidence
strictly below one half, and use the positive coefficient in
[the actual-trajectory theorem](#dense-trajectory-lower).
If \(n\log(en)^5\) is below its displayed necessary bound, the
success event at accuracy \(\varepsilon\) and the strict lower event
are disjoint while their probabilities sum to more than one.
This gives the scalar necessity. To obtain the storage consequence,
split into \(n\ge\varepsilon^{-2}\), where the claim is immediate,
and \(n<\varepsilon^{-2}\), where
\(\log(en)\le1+2\log(1/\varepsilon)\).
Thus \(n^2\) is bounded below by a positive fixed-problem multiple
of \(\varepsilon^{-4}/\log(1/\varepsilon)^{10}\) eventually.
This argument applies only inside the independently initialized dense
family.

Finally fix an arbitrary failure tolerance. Apply the dense lower theorem
at half that tolerance and the compression upper theorem at the other
half. Harmonic's original \(n^{-1+o(1)}\) specialization divided by
\(n^{-1/2}\log(en)^{-5/2}\) tends to zero. For Legendre use the strict
root-width order in (Legendre-root-width-order), multiplied by
\(\log(en)^{3/2}\) and rounded up. Its squared denominator gains
\(\log(en)^3\); the ratio of the new to old logarithmic numerator
tends to one, since \(\log q=(1/4+o(1))\log n\).
Its ratio to the dense lower bound is therefore bounded by a
fixed-problem, fixed-confidence multiple of \(\log(en)^{-1/2}\),
which tends to zero. The union bound proves a limsup probability at
most the arbitrary failure tolerance for every positive ratio threshold.
Letting that tolerance tend to zero proves convergence in probability.
This step uses neither event independence nor a confidence-uniform
lower coefficient, and makes no fitted-endpoint lower claim.


<a id="computational-cost-proofs"></a>
### Proof of the computational-cost bounds

The cost contract and local symbols are those of
[Part II](#computational-costs). This proof counts explicit executions,
not all possible algorithms. Matrices use classical multiplication:
an \(a\)-by-\(b\) matrix acting on \(c\) vectors costs \(O(abc)\)
arithmetic. Rectangular factors and nodes can be streamed as specified.
All comparisons here concern arithmetic identities of the defined
models, not a new numerical approximation theorem.

#### Dense and Legendre execution

Drawing/filling the \(P\) dense coordinates has the stated arithmetic
and sampling counts. A forward/backward pass over \(m\) inputs and
the outer-product updates cost \(O(mP)\), plus the listed activation
calls. Save \(O(Lmn)\) features and signals, along with parameters,
directions and data. A query uses two width-\(n\) buffers, with
\(O(P)\) arithmetic; normalization of the first preactivation can
follow multiplication by the supplied input.

For Legendre, initialize only the \(L-1\) feature layers used as
zeroth moments. This takes \(mnd+(L-2)mn^2\) matrix arithmetic,
\((L-1)mn\) nonlinear evaluations, and the associated scalar
operations. Write the other \(2(L-1)mnq\) moment entries, including
zeros; their allocation/filling cost is not omitted.

Each reconstructed hidden mixer is its fixed dense matrix plus
\(mq\) outer-product corrections. For a batch of \(m\) columns,
first take their inner products with one stored feature vector,
then accumulate the scaled response vector. Across all factors
this costs \(O(nm^2q)\) per interface. Streaming those operations
does not require an \(m^2q\)-word intermediate. The transpose action
has the same count. All sums
\(\sum_{i<j}(2i+1)\bar h_{a,i}\) and their response analogues
are formed with one running prefix per sample and interface;
there are \(O(Lnmq)\), not \(O(Lnmq^2)\), operations. The
first-layer/readout updates and residual calculation fit \(O(mP)\).
Moment storage dominates \(Lmn\) because \(q\ge1,L\ge2\).

At one query, each correction contributes one scalar inner product
times one stored vector. Accumulate directly into the next layer's
feature buffer, costing \(O(Lnmq)\) work and \(O(n)\) extra
words. Explicitly summing all outer products to cache reconstructed
matrices costs \(O((L-1)n^2mq)\) and creates the stated dense
cache. It must be refreshed after its defining state changes.

#### Exact factored initial-jet execution

For this paragraph, \([g]_s=\partial_t^sg(0)/s!\) denotes a normalized
Taylor coefficient. Put \(u_a^{(j)}=r_a\delta_a^{(j)}\), where the
residual and backward response are the actual dense-training ones.
Coefficient comparison in the dense ODE gives, for \(s\ge1\),
\[
[A]_s=-\frac2{ms}\sum_a[u_a^{(1)}]_{s-1}v_a^T,\qquad
[W^{(j)}]_s=-\frac2{mns}
 \sum_a\sum_{b+c=s-1}[u_a^{(j)}]_b[h_a^{(j-1)}]_c^T.
\tag{cost-factored-weight-jets}
\]
Thus initial matrices and \(O(LmnK)\) training coefficients
determine all parameter jets without retaining \(K\) dense mixers.
For a batch \(X(t)\) of \(b\) query vectors, write \(U_i,H_j\)
for the \(n\)-by-\(m\) weighted-response and feature coefficients.
The increment's coefficient of degree \(s\) is
\[
-\frac2{mn}\sum_{i+j+k=s-1}
 \frac{U_i(H_j^TX_k)}{i+j+1}.
\tag{cost-factored-query-action}
\]
Directly contracting every triple costs \(O(nmbK^3)\). Alternatively,
cache \(H_j^TX_k\): all these inner products cost \(O(nmbK^2)\);
their weighted sums for each outer index cost \(O(mbK^3)\);
the final vector combinations cost \(O(nmbK^2)\). Initialized
matrix actions cost \(O(n^2bK)\). The transpose calculation
interchanges the two training factors and has identical counts.
Every increment at order \(s\) uses lower orders \(i,j,k<s\),
so this cached calculation is causal during the training recursion.
New order-\(s\) contractions are saved for later orders.

Use \(b=m\) once for the shared training calculation and \(b=1\)
for each streamed spatial query. Training contractions occupy
\(O(Lm^2K^2)\) words, and a query can reuse \(O(mK^2)\)
scratch layerwise. First-layer coefficients can be formed one at
a time and discarded, or applied through the training input inner
products; their cost fits the stated envelopes when \(n\ge m,d\).
Pointwise residual/response convolutions and readout operations fit
the same bounds. Saving the initialized-matrix contributions already
computed in forward/backward propagation also supplies the paired
source images. The materialized alternative stores all parameter
coefficients and performs ordinary two-index convolutions, yielding
the \(P(m+N_x)K^2\) count. None of these recursions advances physical
training time.

For a general activation, composition with a scalar Taylor series
can be executed online by a triangular table of power coefficients:
there are \(O(K^2)\) entries, each updated by at most \(O(K)\)
terms. This gives the stated \(K^3\) work and \(K^2\) persistent
words. With the full query series available, truncated Horner
composition uses \(O(K)\) scratch and \(O(K^3)\) work.
Fixed-size differential identities, when available for the chosen
activation, instead use \(O(K^2)\) convolution work and \(O(K)\)
words. These statements account for composition only; the backend
cost definition separately includes scalar derivative generation.

#### Compiling the temporal map and accumulating spatial coefficients

For the actual continuation map in the initial-jet proof, write locally
\[
\mathfrak t(\xi)=c[\log(1+u\xi)-\log(1-v\xi)],\quad
c=2r_t/\pi,\quad
u=\frac{b_1-\vartheta}{1-b_0},\quad
v=\frac{b_1+\vartheta}{1+b_0}.
\]
The constant logarithm cancels because \(\mathfrak t(0)=0\).
The source quantities \(b_0,b_1,\vartheta\) were defined in the
[initial-jet proof](#harmonic-initial-jet-proof). This form gives
\[
[1+(u-v)\xi-uv\xi^2](\mathfrak t^k)'
 =kc(u+v)\mathfrak t^{k-1}.
\]
Writing \(A_{jk}=[\xi^j]\mathfrak t(\xi)^k\), coefficient comparison
yields
\[
(j+1)A_{j+1,k}
 =kc(u+v)A_{j,k-1}-(u-v)jA_{jk}
   +uv(j-1)A_{j-1,k}.
\tag{cost-continuation-power-recurrence}
\]
Use \(A_{00}=1\), zero other entries in column zero and row zero,
and zero negative-index entries. Generate each column from the
preceding one, using \(O(K)\) scratch and \(O(K^2)\) total work.

For temporal quadrature nodes, let \(\xi_\ell\) be their coordinates
under the inverse map and let \(\omega_{a\ell}\) include quadrature
weight, temporal cosine and its normalization. Form
\[
E_{aj}=\sum_{\ell=1}^{N_t}\omega_{a\ell}\xi_\ell^j,\qquad
B_{ak}=\sum_{j=0}^KE_{aj}A_{jk},
\quad 0\le a\le p.
\tag{cost-compiled-temporal-map}
\]
Form \(E\) in \(O(N_t(p+1)K)\) work. As each column of \(A\)
is generated, multiply it by \(E\) and discard it. This adds
\(O((p+1)K^2)\) work and uses \(O((p+1)K)\) words for \(E,B\)
and the streamed columns. A source at a spatial node then has
temporal coefficient \(\sum_k B_{ak}[g]_k\). This is exactly
the chosen finite initial-jet reconstruction followed by the chosen
quadrature, not a replacement approximation.

Apply that transform to the source coordinates at one spatial node,
then accumulate the angular coefficients. This proves temporal-first
work \(O(LnN_x(p+1)(K+H))\) and \(O(LnR)\) coefficient
storage. Reversing the two finite sums proves the spatial-first
alternative and its \(LnKH\) intermediate. The same scalar maps
are used for paired initialized-matrix images, so their exact
linear identities are preserved. Blocking complete coefficient
columns and recomputing nodal jets proves the stated alternative
peak memory and pass count.

#### Geometric basis overhead

The circle basis is \(1,\sqrt2\cos(j\theta),\sqrt2\sin(j\theta)\);
angle-addition recurrences evaluate all degrees through \(J\) in
\(O(J+1)\) arithmetic. In higher dimension split
\(v=(\cos\theta,\sin\theta\,u)\), \(u\in S^{d-2}\).
From a degree-\(\ell\) harmonic on \(S^{d-2}\), use
\[
(\sin\theta)^\ell
C_{j-\ell}^{\,\ell+(d-2)/2}(\cos\theta)\,Y_{\ell,b}(u),
\qquad 0\le\ell\le j,
\tag{cost-separated-harmonics}
\]
with its scalar normalization. Substitution into the separated
sphere Laplacian shows eigenvalue \(-j(j+d-2)\). Orthogonality
in \(u\) separates unequal lower modes; for equal lower modes
the angular integral is the Gegenbauer inner product with weight
\((1-z^2)^{\ell+(d-3)/2}\). Dimension counting by the harmonic
decomposition already proved above makes this a complete basis.
The three-term Gegenbauer recurrence, obtained by differentiating
its generating function, is
\[
(s+1)C_{s+1}^{\lambda}(z)
 =2(s+\lambda)zC_s^\lambda(z)
  -(s+2\lambda-1)C_{s-1}^\lambda(z).
\]
For each intermediate dimension there are \(O((J+1)^2)\)
degree/lower-degree pairs. Their polynomial values and normalization
ratios can be generated recursively, without a gamma-function oracle.
For the probability-sphere angular measure, denote the squared norm
of the angular factor locally by \(N_{\ell,s}\), where
\(\lambda=\ell+(d-2)/2\). The beta integral and the displayed
Gegenbauer recurrence give
\[
N_{0,0}=1,\qquad
\frac{N_{\ell+1,0}}{N_{\ell,0}}
 =\frac{2\ell+d-1}{2\ell+d},\qquad
\frac{N_{\ell,s+1}}{N_{\ell,s}}
 =\frac{(s+2\lambda)(s+\lambda)}
 {(s+1)(s+\lambda+1)}.
\]
Inverse square roots supply the normalization constants. Combining
with the lower-dimensional basis costs at most \(O(H)\) additional
products per dimension and node. This proves
(cost-scalar-geometry), including \(O(d(J+1)^2)\) reusable scalar
data and \(O(dN_x)\) node generation. The case \(d=1\) is the
two-point sphere. No numerical conditioning of these recurrences
is inferred from their arithmetic count.

#### Source selection and assembly

Process the \(R\) generators by rank-aware orthogonalization against
at most \(r\) current basis columns, costing \(O(nRr)\) per layer.
Exact arithmetic distinguishes dependence; a numerical rank tolerance
would require its own error allowance.
Each of the selector's \(9r\) barrier iterations can form its shifted
\(r\)-by-\(r\) inverses in \(O(r^3)\), then test \(n\) row vectors
by \(O(r^2)\) quadratic forms each. Thus the work is
\(O(nr^3+r^4)=O(nr^3)\), since \(r\le n\).

Using the proof's selected basis matrix \(P_j\) and diagonal weights
\(\mathsf D_j\), locally suppress the layer index and put
\(G=P^T\mathsf DP\). The prescribed metric and its inverse satisfy
\[
M=\mathsf D+\mathsf DP(G^{-2}-G^{-1})P^T\mathsf D,\qquad
M^{-1}=\mathsf D^{-1}+P(I-G^{-1})P^T,\qquad
P^TM=G^{-1}P^T\mathsf D.
\tag{cost-metric-factor-identities}
\]
For verification, put \(Z=\mathsf D^{1/2}P\), decompose into
\(\operatorname{ran}Z\) and its orthogonal complement, and use
\(Z^TZ=G\); multiplication gives each identity. Form the
\(r\)-dimensional Gram/inverse and materialize both metric caches
in \(O(qr^2+r^3+q^2r)=O(q^2r)\) work.

The core initialized map \(U_j^TW_0^{(j)}U_{j-1}/n\) costs
\(O(n^2r+nr^2)\) in general. Paired source actions may save
some matrix calls, but do not cover the initialized mixer on the
entire source space. Its remaining assembly through selected bases
and the last metric identity costs \(O(q^2r+qr^2)\). These
counts give the assembly terms of \(\mathcal T_{\rm H}\).
Source bases fit inside the \(LnR\) envelope and the final arrays
inside \(Lq^2\). Adding the live training jets/caches, scalar
transform, data and geometry bounds proves
\(\mathcal M_{\rm H}\). Freeing phase-specific work arrays can
reduce this safe peak upper bound.

#### Harmonic training without cubic hidden-matrix operations

Let \(H_j,\Delta_j\) have training-feature and backward-response
columns, and let \(X\) have normalized training inputs as columns.
The prescribed directions can be evaluated as
\[
\dot A_C=\frac2m(\Delta_1\operatorname{diag}c_C)X^T,\qquad
\dot B_C^{(j)}
=\frac2m(\Delta_j\operatorname{diag}c_C)(M_{j-1}H_{j-1})^T,
\qquad \dot w_C=\frac2mH_Lc_C.
\]
Apply metrics to the batch arrays first. Multiplying an already
formed \(q\)-by-\(q\) update by a dense metric would introduce an
unnecessary \(q^3\) cost. Backward propagation similarly applies
\(M_{j+1}\), then \(B_C^{(j+1)T}\), then the cached \(M_j^{-1}\)
to the batch, rather than constructing dense metric adjoints.

The feature Gram is \(Q_C=H_L^TM_LH_L/m\); its construction costs
\(O(mq_L^2+q_Lm^2)\), and an ordinary fresh factorization costs
\(O(m^3)\). Its positivity is inherited from the fitting theorem.
This moving solve is distinct from the fixed metric inverse caches.

The update Gram need not be formed. Direct expansion of the
directions above gives, sample by sample,
\[
\begin{split}
\frac2m(K_Cc_C)_a={}&
h_{C,a}^{(L)T}M_L\dot w_C
 +\delta_{C,a}^{(1)T}M_1\dot A_Cv_a\\
&+\sum_{j=2}^L
\delta_{C,a}^{(j)T}M_j\dot B_C^{(j)}
                         h_{C,a}^{(j-1)}.
\end{split}
\tag{cost-update-gram-action}
\]
For example, expansion of the \(j\)-th hidden term produces
\((2/m)\sum_b c_{C,b}
\langle\delta_{C,a}^{(j)},\delta_{C,b}^{(j)}\rangle_{M_j}
\langle h_{C,a}^{(j-1)},h_{C,b}^{(j-1)}\rangle_{M_{j-1}}\),
exactly that term of \(2K_Cc_C/m\). Set \(\dot c_C\) to the
negative of these contractions. This is an algebraic identity, not
an assertion that the optimizer is a gradient or that the formula
is a Jacobian-vector product of the corrected predictor.

Forward passes, these ordered backward/update operations, the
feature-Gram solve and state directions give
(cost-harmonic-training) and its peak-memory count. A final
post-update readout refresh repeats no more than the forward pass
and top Gram solve, so it has the same order and the stated
activation calls. With \(M_L\widehat w_C\) resident, query
evaluation is the ordinary forward pass with rolling buffers,
which proves (cost-harmonic-query).

#### Cost consequences of the existing inverse choices

Substitution of an inverse width/order is arithmetic only; it
does not provide a numerical-integration or roundoff bound.
For fixed data/activations/confidence and
\(n=\varepsilon^{-2+o(1)}\), dense \(P\) is
\(\varepsilon^{-4+o(1)}\). The Legendre inverse has
\(q=\varepsilon^{-1/2+o(1)}\), so its \(Lnmq\) storage/action
terms are \(\varepsilon^{-5/2+o(1)}\) and the fixed dense
mixers dominate the total warmup, training and query arithmetic
envelopes. Its additional query workspace remains
\(\varepsilon^{-2+o(1)}\).
The Harmonic inverse has
\(q=O(\log(1/\varepsilon)^{3d/2+1})\) for fixed structural
parameters. Its runtime arithmetic and training peak memory are
therefore \(O(\log(1/\varepsilon)^{3d+2})\), and its query
workspace is \(O(\log(1/\varepsilon)^{3d/2+1})\), under the
separate scalar-evaluation convention. No such substitution
eliminates \(K,N_x,N_t\), activation-series costs or precision
requirements from Harmonic warmup. This proves exactly the
qualified cost tables, not a polylogarithmic initialization theorem.

<a id="integrated-audit"></a>
## IV. Audit, provenance and remaining limitations

This is one results-and-proof document. Earlier within-study derivations
remain provenance and review inputs, not additional instructions a reader
must combine with this theorem. No maintained-book or paper promotion is
asserted.

The assembly contains the entire specialized source insertion argument,
the explicit source recurrences and moment-budget removal; dense
initialization, fitting, signed comparison, Gaussian concentration and
initialized-Gram fluctuation proofs; the Legendre endpoint projection,
all-order fitting and signed comparison proofs; and Harmonic coordinate
selection, metric/action, harmonic expansion, finite initial-jet setup,
independent fitting, source energy, readout/deficit cancellation,
all-time continuation, arbitrary-budget inversion and storage proofs.
The subsequent computational-cost addition derives initialization,
per-stage and single-query bounds from these same constructions, exposing
the Harmonic setup resolutions and activation backend separately.
Ordinary finite-dimensional calculus, the spectral theorem, compactness
and the standard elementary limiting theorems used with their stated
hypotheses are not new model assumptions.

### Internal review status

The dense and source/Legendre sections received fresh, separately scoped
reconstructions against frozen full inputs. Their reports distinguish
local algebra from the source dependency. The source/Legendre report
required the all-time extension and notation corrections; the extension
and its two explicit gates are included above, and the source derivative
bound is now \(t_2\), finite vector RMS factors are written explicitly,
and parameter differences use typed notation.

The Harmonic audit identified a missing definition of its four source
families and the spaces they generate. The explicit definition, endpoint
omissions, exact initialization additions and synchronized coefficient
operations are now in the runtime statement; the reviewer inspected
the addition and confirmed that it resolves the gap without changing
the rank count. The final interface audit also requested an explicit
vector empirical moment and a locally scoped activation-power
abbreviation. Both corrections are included.

The separately scoped internal audits found no remaining mathematical
objection in their combined assigned scope. Dense and Harmonic local
verdicts are conditional on the shared source theorem; that theorem and
the Legendre/all-time bridge were reconstructed in the separate source
audit. No local verdict is presented as an independent proof of a
dependency it did not inspect. The final assembly audit checks
interfaces, not a second reconstruction of every local proof.

| Scope | Recorded audit |
|---|---|
| Dense fitting, upper, lower, confidence and inversion | [Dense audit](INTEGRATED_DENSE_AUDIT.md) |
| Source, all-order Legendre and all-time bridge | [Source/Legendre audit](INTEGRATED_SOURCE_LEGENDRE_AUDIT.md) |
| Harmonic construction, comparison, budgets and storage | [Harmonic audit](INTEGRATED_COMPACT_AUDIT.md) |
| Headline/exact/proof interfaces and final assembly | [Assembly audit](INTEGRATED_ASSEMBLY_AUDIT.md) |

The reports record frozen-input hashes and final-assembly bindings.
Temporary section drafts were assembly inputs, not separate current
results interfaces. Internal review is not a promotion review, formal
verification, or approval to change the maintained book.

<!-- method-names:start -->
The user subsequently selected the names Legendre compression and
Harmonic compression. Original audit reports and historical filenames
are preserved verbatim; their hashes identify the pre-rename version.
The [terminology-only check](TERMINOLOGY_UPDATE_CHECK.md) records the
rename-only snapshot's correspondence to that audited text. That editorial
step changed no numerical coefficient, assumption, construction or proof
claim. Current
fragment links use the new name, while former fragment identifiers remain
as compatibility aliases.
<!-- method-names:end -->

The later computational-cost sections and inverse/consequence tables
are new execution analyses, not part of the frozen original audits.
Their scoped derivation, subsequent reviews, exact version binding and
reproducible algebra checks are recorded in
[COMPUTATIONAL_COST_CHECK.md](COMPUTATIONAL_COST_CHECK.md).
The accompanying [check script](cost_algebra_check.py) tests the jet
contractions, temporal compilation, selected-metric identities, Legendre
prefix/factor execution, matrix-free update-Gram action and inference
cache. Numerical identity checks support the execution derivations;
they do not verify the analytic approximation theorem, optimality,
conditioning or wall-clock complexity.

Mechanical checks cover control characters, paired math delimiters,
unique equation tags and explicit anchors, resolved local links, and
scoped whitespace validation. Bounded scalar arithmetic checks accompany
the written coefficient arguments; no numerical training experiment was
needed. No full Markdown/TeX render was run: the available environment
has neither Quarto/Pandoc nor the checked JavaScript math renderers.

The required canonical-notation skill at
/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md
was inaccessible with permission denied, including a scoped reviewer's
escalated attempt. The supplied user instructions, maintained notation
contract, rigorous-math workflow and research-audit workflow were applied;
compliance with the unreadable additional skill cannot be claimed.

### Source scope

The author used this study's current artifacts and the maintained
notation/setup, plus only the specific cited dependency proofs the user
authorized for this consolidation:

- In the study dense_cutoff_population_rate_20261001:
  UNBOUNDED_ACTIVATION_CANDIDATE, UNBOUNDED_INSERTION_CHECK,
  DEPTH_CAVITY_ROUTE and DEPTH_INSERTION_CHECK.
- In the study closure_sampling_20261003:
  ACTIVATION_CLASS_EXTENSION_ROUTE, STORAGE_QUADRATIC_IMPROVEMENT,
  GENERAL_WEIGHTED_COMPARISON, SPHERICAL_SOURCE_DIMENSION_ROUTE
  and DIMENSION_PREFACTOR_OPTIMIZATION.

These are the cited Markdown dependency proofs, not permission to import
other research from those studies. Their specialized arguments have been
included above. Older
bounded-activation assumptions, normalized gaps, older compression counts,
and specialized endpoint examples were not substituted into the current
general theorem.

The consolidation changes neither the activation class nor the shared
label interval. It adds no model order, confidence-dependent stored
trajectory, or fitted-reference oracle. It does not promise efficient
accuracy-certified preprocessing, numerical integrator complexity, bit
complexity, or ordinary gradient training of an arbitrary smaller network.
The cost addition uses this integrated construction, not further research
from another study; its arithmetic envelopes keep the unoptimized setup
orders, sampling and activation costs explicit. In particular small
retained Harmonic storage is not a claim of small initialization peak
memory or work.

### What remains unresolved

The finite-deletion moment argument and the initialized central limit
theorem give only eventual stochastic widths, not a computable
\(n(\delta)\). All deterministic coefficients and extra width gates
are explicit, but the full sufficient width is not effective. This is
a limitation of the theorem, not notation to be suppressed.

The general lower bound certifies the width exponent up to logarithms,
not the upper bound's powers of \(m/\gamma\), dimension or depth.
It is a transient all-trajectory lower bound, not a general fitted-endpoint
lower bound. Optimal compression among arbitrary representations and
sharp growing-data dependence remain open. Fixed-problem exponents are
not uniform theorems for simultaneously growing structural parameters.

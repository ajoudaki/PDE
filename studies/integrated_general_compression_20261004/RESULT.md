# Dense, Legendre and compact models: accuracy and storage

2026-10-05. This is the single integrated results statement. It includes
the sharpened compact comparison on the full original label range, alongside
the dense upper and lower bounds, Legendre comparison, width conditions,
and accuracy-to-storage consequences. Complete current proofs are linked
in §7. These are internally checked research results, not promoted
manuscript or book results.

## 1. Shared setup, notation and qualifications

Fix input dimension \(d\ge1\), sample count \(m\ge1\), hidden depth
\(L\ge2\), inputs \(x_i\in\mathbb R^d\) with
\(\|x_i\|_2=\sqrt d\), and real labels \(y_i\). The dense width is
\(n\). The only compressed-model size/order symbol is \(q\): Legendre
memory order, or compact per-layer neuron budget. These are different
resources, not equal-sized models.

The other numerical parameters used throughout are label RMS \(Y\),
feature-Gram gap \(\gamma\), activation envelope \(\beta\), failure
probability \(0<\delta<1\), and requested error \(\varepsilon>0\).
Their definitions and all shared assumptions follow before the results.
One indexed family \(E\), with model subscripts
\(\mathrm{dense},\mathrm{Leg},\mathrm{compact}\), denotes the explicit
**error certificates** in §3, not the actual discrepancies.
Their displayed arguments vary width and order; the shared task parameters
and confidence are held fixed.

The dense model has \(A\in\mathbb R^{n\times d}\),
\(W^{(\ell)}\in\mathbb R^{n\times n}\) for \(2\le\ell\le L\),
and \(w\in\mathbb R^n\), with forward pass
\[
z^{(1)}=Ax/\sqrt d,\qquad
z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\qquad
h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad
f_n=w^\top h^{(L)}/n.
\]
First-weight entries are independent \(N(0,1)\), hidden-mixer entries
are independent \(N(0,1/n)\), all blocks are independent, and \(w(0)=0\).
Training minimizes \(m^{-1}\sum_i(f_n(x_i)-y_i)^2\) by the study's
gradient flow with block mobilities
\((n,1,\ldots,1,n)\). Write \(\widetilde f_n\) for an independent
dense copy trained on the same data; \(f_{\rm Leg,n,q}\) and
\(f_{\rm compact,n}\) use the initialization of their reference \(f_n\).

Each \(\phi_\ell\) is real on the real axis, holomorphic on a common
strip \(|\operatorname{Im}z|<a\), and has bounded first derivative
there. Activation **values may be unbounded**. Define
\[
\beta=\max\left\{10,\ 1+\max_\ell|\phi_\ell(0)|,\ \frac{16}{a},\
\max_{1\le\ell\le L,\,j\in\{1,2\}}\sup_{|\operatorname{Im}z|\le a/2}
|\phi_\ell^{(j)}(z)|\right\},\qquad Y=\frac{\|y\|_2}{\sqrt m}.
\]
To define the gap, use the finite covariance recursion
\[
Q^{(0)}_{ij}=x_i^\top x_j/d,\qquad
Q^{(\ell)}_{ij}=\mathbb E[\phi_\ell(Z_i)\phi_\ell(Z_j)],
\quad Z\sim N(0,Q^{(\ell-1)}),\qquad
\gamma=\lambda_{\min}(Q^{(L)})>0.
\]
The gap is **unweighted**: it is not divided by \(m\). No orthogonality,
centering, input-rank condition, label-sign pattern or clipping is assumed.

The explicit envelopes below share the sufficient label condition
\[
\boxed{\quad 0<Y\le\frac{\gamma}{m}\,\beta^{-30L}.\quad}
\tag{labels}
\]
This explicit specialization does not replace the larger original
allowance, stated in §6. The sharpened compact comparison holds throughout
that larger range as well, with universal numerical constants; the
coefficients 10 and 250 below use the displayed simpler cap. The
beta-only size/storage envelopes and the displayed dense/Legendre
envelopes use this simpler cap. If
\(Y=0\), all predictions are exactly zero and a constant-zero compact
representation is exact.

Every error uses the same physical time and the same norm:
\[
\boxed{\quad
\|f-g\|_*:=\sup_{t\in[0,\infty]}
                  \sup_{\|x\|_2=\sqrt d}|f(t,x)-g(t,x)|.
\quad}
\tag{error norm}
\]
This is the whole sphere (the circle when \(d=2\)) and the entire
training trajectory, **including fitted limits**. It measures function
fidelity, not unknown-label test risk or error against a population limit.

All upper certificates require \(n\ge N_0(\delta)\), where this finite
threshold may depend on every fixed problem parameter. It includes the
source-construction gates; its stochastic part is **unquantified**. The
probability is at least \(1-\delta\) at each individual eligible width,
not on one event for infinitely many independent widths. Joint comparisons
use a split failure budget and the corresponding thresholds. The lower
bound has its own eventual, also unquantified, width threshold.

On the fitting events, all three models interpolate and converge. Their
training RMS residuals are at most \(Y e^{-\gamma t/(2m)}\) for dense
and compact, and \(Y e^{-\gamma t/(4m)}\) for every Legendre order
\(q\ge1\). Accuracy, unlike fitting, imposes the extra order condition
in §3.

## 2. Model size and storage: before choosing accuracy

Storage counts real coordinates, not bits or computation time. A learned
coordinate is part of the evolving optimizer state; recomputable caches
and fixed coefficients are listed separately.

| Model | Meaning of its size/order | Learned state | Additional retained storage |
|---|---|---|---|
| Dense | \(n\) neurons per hidden layer | \((L-1)n^2+n(d+1)\) | No fixed mixer separate from the learned weights |
| Legendre | \(q\) memory modes; still width \(n\) | \(n(d+1)+1+2(L-1)mnq\) | \((L-1)n^2\) fixed initialized mixer entries |
| Compact | At most \(q\) neurons per hidden layer | At most \((L-1)q^2+q(d+1)+m\) | \(O(Lq^2+qd+Lmq+m^2+m(d+1))\) for metrics, fixed copies, data and caches |

Thus the principal learned-state sizes are \(Ln^2+dn\), \(Lmnq+dn\),
and \(Lq^2+dq+m\). **The compact quadratic term includes depth.** For
actual selected layer widths \(q_1,\ldots,q_L\le q\), its exact moving
count is \(dq_1+\sum_{\ell=2}^Lq_\ell q_{\ell-1}+q_L+m\).
The dense and Legendre entries count model state, as in the original
results; ordinary storage of the training data is additional if retained.
The compact theorem below gives a stronger, fully inclusive inventory.
Its displayed \(q\) is an enlarged upper budget, so the rough learned-state
bound obtained by inserting that budget can exceed the sharper direct
bound on all retained coordinates; neither is asserted to be an equality.

Legendre uses the original residual-RMS clock with unit forward prefix
and zero backward prefix. Its reconstructed dense matrices are evaluation
objects, not additional learned state. Compact uses the existing
**corrected-readout autonomous optimizer**, not ordinary gradient flow
on an arbitrary smaller network. Its \(m\) internal residual coordinates
are included above. No original-width matrices or trajectory table are
retained after compact preprocessing. Neither model has an additional
independent runtime approximation order.

## 3. Accuracy certificates and their admissible sizes

### Dense versus an independent dense copy

The existing upper certificate, with every coefficient expanded, is
\[
\begin{aligned}
E_{\rm dense}(n):={}&
\beta^{100L}Y\left(1+\frac m\gamma\right)^2
\left(1+\beta^{100L}\frac{Ym}{\gamma}\sqrt{\log(en)}\right)\\
&\times\left[1+\beta^{100L}\left(\frac{Ym}{\gamma}\right)^2
                  \left(e^{\sqrt{\log(en)}}-1\right)\right]
\sqrt{\frac{\log[8(n+1)(1+2n)^d/\delta]}{n}},\\
\|f_n-\widetilde f_n\|_*\le{}&E_{\rm dense}(n).
\end{aligned}
\tag{dense upper}
\]
For \(m\ge2\), the general lower result also gives, with probability
at least \(1-\delta\) at every sufficiently large individual width,
\[
\boxed{\quad
\|f_n-\widetilde f_n\|_*
\ge c_{\phi,L,\delta}\frac{Y\sqrt\gamma}
             {\sqrt n\,[\log(en)]^{5/2}}.
\quad}
\tag{dense lower}
\]
The positive coefficient depends only on activations, depth and confidence;
its exact Gaussian-moment formula and full-label-range adjustment are in
[the lower theorem, §1](GENERAL_VARIABILITY_LOWER_RESULT.md#1-setting-and-conclusion).
The witness is an actual nonlinear prediction at a positive early time,
which may shrink with \(n\); this is **not an endpoint lower bound**.
For \(m=1\), deterministic exceptions prevent this general lower claim.

At fixed task, the upper is \(n^{-1/2+o(1)}\), not a proved strict
\(n^{-1/2}\) upper bound. The lower calibrates the width exponent, not
the upper bound's powers of \(m/\gamma\).

### Legendre versus its realized dense reference

The certificate is
\[
\begin{aligned}
E_{\rm Leg}(n,q):={}&
\frac{3\beta^{100L}Y}{q^2}
\left(\frac{Ym}{\gamma}\right)^2\left(1+\frac m\gamma\right)
\left(1+\beta^{100L}\frac{Ym}{\gamma}\sqrt{\log(en)}\right)\\
&\times\left[1+\beta^{100L}\left(\frac{Ym}{\gamma}\right)^2
                  \left(e^{\sqrt{\log(en)}}-1\right)\right]
\sqrt{\log(eq)},\\
\|f_{\rm Leg,n,q}-f_n\|_*\le{}&E_{\rm Leg}(n,q).
\end{aligned}
\tag{Legendre error}
\]
It holds on **one event simultaneously** for all integer \(q\ge1\)
satisfying
\[
\begin{aligned}
q\ge{}&3\beta^{100L}\left(\frac{Ym}{\gamma}\right)^2
\left(1+\frac m\gamma\right)
\left(1+\beta^{100L}\frac{Ym}{\gamma}\sqrt{\log(en)}\right)\\
&\times\left[1+\beta^{100L}\left(\frac{Ym}{\gamma}\right)^2
                  \left(e^{\sqrt{\log(en)}}-1\right)\right].
\end{aligned}
\tag{Legendre order}
\]
There is no additional order-dependent stochastic threshold. In particular,
the [explicit order prescription, (4)](LEGENDRE_SAMPLE_EXPONENT_REFINEMENT.md)
has \(q=n^{1/4+o(1)}\) and certifies error at most \(Y/\sqrt n\).
Section 4 below specifies the smallest order certified for any requested
\(\varepsilon\), rather than introducing a second order parameter.

### Compact versus its realized dense reference

The current construction fixes source-coordinate tolerance to \(1/n\).
An explicit sufficient **per-layer budget**, using the existing selection
and coefficient bounds, is
\[
\boxed{\quad
q=\left\lceil9\left[
\beta^{(32+3d)L}\frac{(d+3)^{d/2}}{d!}
\left(\frac{Ym}{\gamma}\right)^2[\log(en)]^{3d/2+1}
+2m+d+1\right]\right\rceil.
\quad}
\tag{compact size}
\]
The selected layer widths need only be **at most** this budget. The same
constructed model satisfies the sharpened certificate
\[
\boxed{\quad
\|f_{\rm compact,n}-f_n\|_*\le E_{\rm compact}(n):=
10\beta^{40L}Y\frac m\gamma
\left(1+\sqrt{\frac m\gamma}\right)
\frac{e^{2\sqrt{\log(en)}}}{n}.
\quad}
\tag{compact error}
\]
There is no sample, gap, activation or depth multiplier inside the
exponential. At fixed task the rate is \(n^{-1+o(1)}\). At every
eligible width, without an additional comparison threshold,
\[
\boxed{\quad
\|f_{\rm compact,n}-f_n\|_*
\le\frac{250\beta^{40L}Y(1+m/\gamma)^2}{\sqrt n}.
\quad}
\tag{compact root certificate}
\]
This second bound is convenient for prescribing accuracy; the first has
the sharper width rate. The same improvement holds on the full original
label range in §6. The source tolerance, selected spaces, optimizer and
storage are unchanged.
The **all-retained** numerical storage bound is unchanged:
\[
\begin{aligned}
\operatorname{storage}(f_{\rm compact,n})\le{}&
\beta^{(64+6d)L}\frac{(d+3)^d}{(d!)^2}
\left(\frac{Ym}{\gamma}\right)^4[\log(en)]^{3d+2}\\
&+2040(L+1)(2m+d+1)^2+10m(d+1).
\end{aligned}
\tag{compact storage}
\]
The log exponent is independent of depth; its coefficient is not.

The proof couples readout and residual discrepancies through the current
feature right inverse. Their leading feature-Gram terms cancel; residual
dissipation controls the remainder. Dense energy supplies the selected
readout scale \(Y\sqrt{m/\gamma}\). These arguments require feature
RMS control, not bounded activation values. The existing label allowance
then absorbs the activation powers in the stability exponent. All these
comparison variables are proof objects, not additional learned state.

**Scope of the size choice.** There is no additional runtime order, but
the assembled compact theorem does not supply an error law for arbitrary
\(q\). It certifies the construction above, jointly in its size and
error. A larger budget accommodates that construction; the current result
does not certify a smaller error just by increasing that budget. Inverting
an upper bound on the selected width would not establish such a theorem.

## 4. One accuracy-to-learned-state interface at prescribed width

Fix a dense reference width \(n\) satisfying the applicable thresholds.
The common target is
\[
\boxed{\qquad
\mathbb P\{\|f_{\rm model}-f_n\|_*\le\varepsilon\}\ge1-\delta.
\qquad}
\tag{accuracy target}
\]
Here \(f_{\rm model}\) is respectively an independent dense copy, the
Legendre closure, or the constructed compact model. We minimize learned
state over the choices actually covered by each certificate; compact
currently supplies only the stated construction. This is not a claim of
globally optimal compression.

| Model | Choice giving the target | Certified learned state |
|---|---|---|
| Independent dense | No \(q\) to choose; require \(E_{\rm dense}(n)\le\varepsilon\) | \((L-1)n^2+n(d+1)\) |
| Legendre | Choose the smallest integer \(q\) satisfying (Legendre order) and \(E_{\rm Leg}(n,q)\le\varepsilon\) | \(n(d+1)+1+2(L-1)mnq\) |
| Compact | Use (compact size); require \(E_{\rm compact}(n)\le\varepsilon\), or use (compact accuracy width) below | At most \((L-1)q^2+q(d+1)+m\); full inventory is (compact storage) |

The Legendre prescription is well-defined for every \(\varepsilon>0\),
because its error certificate decreases to zero with \(q\). Since its
moving count increases with \(q\), this is precisely the least moving
count certified by that bound. The error and admissibility formulas above
make this an explicit integer selection, with no extra free parameter.
Fixed Legendre mixers remain additional.

For compact, this table is a **feasibility certificate for the existing
construction**, not a minimization over arbitrary compact widths. If its
certificate exceeds \(\varepsilon\), no arbitrary-tolerance retuning at
this same prescribed \(n\) is supplied by the assembled result. Likewise,
a dense bound exceeding \(\varepsilon\) means no certificate from that
bound, not an assertion that the actual discrepancy exceeds the target.
Increasing \(n\) changes the reference network and belongs to the next
corollary, not this fixed-reference comparison.

In particular, a sufficient width for compact accuracy is
\[
\boxed{\quad
n\ge\left\lceil\max\left\{1,N_0(\delta),
62500\beta^{80L}Y^2\left(1+\frac m\gamma\right)^4
\varepsilon^{-2}\right\}\right\rceil.
\quad}
\tag{compact accuracy width}
\]
Only the extra accuracy requirement is polynomial. The inherited
\(N_0(\delta)\) includes source selection, fitting and construction;
its stochastic part remains unquantified. For clarity, its existing
deterministic conditions include
\[
n\ge\max\left\{1,\frac1Y,\frac{\gamma}{16mY}\right\},\qquad
\log(en)\ge\frac{a^2(\gamma/m)^2}{16384Y^4U^2}.
\tag{inherited width gates}
\]
Here \(U\) is only a local source coefficient: it is the explicit
output of [source recurrences (22)–(25)](UNBOUNDED_COMPRESSOR_BRIDGE.md),
evaluated at source activity \(16Ym/\gamma\). The remaining
radius/degree conditions are source (31), (34). They are not replaced by
these two displayed gates. Thus a polynomial **total construction width**
has not been proved. The improvement does not hide a bad error coefficient
inside a newly enlarged threshold.

For a relative target \(\varepsilon=\eta Y\), the accuracy term is
\(62500\beta^{80L}(1+m/\gamma)^4\eta^{-2}\); \(\eta>0\) is
local to this sentence, and the inherited threshold still depends on
actual \(Y\). In the size/storage formulas, choosing the least integer
allowed by (compact accuracy width) permits replacing \(\log(en)\)
by
\[
\log\!\left(2e\max\left\{1,N_0(\delta),
62500\beta^{80L}Y^2(1+m/\gamma)^4\varepsilon^{-2}\right\}\right).
\]
This is an explicit sufficient accuracy-to-storage substitution, including
confidence, not a bound on preprocessing work or bit complexity.

## 5. Compression corollary: dependence on dense width and on accuracy

Fix the dataset, activations, \(m,d,L,Y,\gamma\), and confidence.
Only the displayed dependence on \(n\) or \(\varepsilon\) varies;
All \(O\), \(\Theta\), \(\Omega\) and \(o(1)\) statements below
refer to this fixed-task regime; their implicit constants may depend on
these fixed parameters and confidence.

For a fixed tolerance \(\varepsilon>0\), as the prescribed dense width
increases, §4 gives sufficient learned-state counts
\[
\text{dense: }\Theta(n^2),\qquad
\text{Legendre: }n^{1+o(1)},\qquad
\text{compact: }O([\log(en)]^{3d+2}).
\]
These apply eventually, after the relevant certificates meet the tolerance.
In particular, the familiar Legendre exponent \(5/4\) below concerns
shrinking error of order \(n^{-1/2}\), not fixed error.

At each sufficiently large prescribed width, using the existing root-width
choices for the compressed models gives:

| Model compared with dense | Certified error | Size/order choice | Learned state | All retained model storage |
|---|---|---|---|---|
| Independent dense | \(n^{-1/2+o(1)}\) | Width \(n\) | \(\Theta(n^2)\) | \(\Theta(n^2)\) |
| Legendre | At most \(Y/\sqrt n\) | \(q=n^{1/4+o(1)}\) | \(n^{5/4+o(1)}\) | \(\Theta(n^2)\), including fixed mixers |
| Compact | \(n^{-1+o(1)}\), hence at most \(Y/\sqrt n\) eventually | Budget \(q=O([\log(en)]^{3d/2+1})\) | \(O([\log(en)]^{3d+2})\) | \(O([\log(en)]^{3d+2})\) |

If the dense width may be chosen **before initialization as a function
of accuracy**, select an eligible \(n=n(\varepsilon)\) with
\(E_{\rm dense}(n)\le\varepsilon\) and
\(Y/\sqrt n\le\varepsilon\), also satisfying (compact accuracy width).
The existing results permit
\(n(\varepsilon)=\varepsilon^{-2+o(1)}\). Each comparison then meets
the same (accuracy target), and sufficient storage is

| Model | Learned state at error \(\varepsilon\) | All retained model storage |
|---|---|---|
| Independent dense | \(\varepsilon^{-4+o(1)}\) | \(\varepsilon^{-4+o(1)}\) |
| Legendre | \(\varepsilon^{-5/2+o(1)}\) | \(\varepsilon^{-4+o(1)}\), including fixed mixers |
| Compact | \(O([\log(1/\varepsilon)]^{3d+2})\) | \(O([\log(1/\varepsilon)]^{3d+2})\) |

These are asymptotic sufficient counts, not effective numerical choices
of a confidence-certified width. They do not replace an already prescribed
dense network by a different-width one. If a compressed model must instead
be close to an **independent** dense run, use error budgets
\(\varepsilon/2\) and failure budgets \(\delta/2\) for the dense-copy
and compression comparisons. The triangle inequality gives the same
storage powers; no independence of the comparison events is needed.

For \(m\ge2\), the existing lower result also implies that canonical
independent-dense accuracy with fixed failure probability below \(1/2\)
requires, in the large-width regime,
\[
n[\log(en)]^5\gtrsim_{\phi,L,\delta}\frac{Y^2\gamma}{\varepsilon^2},
\qquad
\text{dense parameters}
=\Omega\!\left(
\frac{\varepsilon^{-4}}{[\log(1/\varepsilon)]^{10}}\right).
\]
This is not a lower bound against arbitrary compressed representations.

Finally, compact's sharper error is already smaller than the dense lower
scale. For Legendre, enlarge the existing root-width order by
\([\log(en)]^{3/2}\), rounding up. Its error is then at most
\(2Y/[\sqrt n\,\log(en)^3]\) eventually, while its learned-state
exponent remains \(5/4+o(1)\). For compact and Legendre with these
choices, when \(m\ge2\),
\[
\frac{\|f_{\rm model}-f_n\|_*}
     {\|f_n-\widetilde f_n\|_*}
\xrightarrow{\mathbb P}0.
\]
The ratio can be defined arbitrarily when the denominator is zero;
the lower theorem makes the probability of that event tend to zero.
This compares complete trajectory norms, not pointwise-in-time ratios or
endpoint errors. Strict-root dense upper bounds, sharp sample/gap/dimension
dependence, a general endpoint lower bound, and an arbitrary-\(q\) compact
accuracy theorem remain outside the established result.

## 6. Full original label range

This section retains the larger, recurrence-based allowance; it is not
an additional restriction on the explicit results above. The numerical
objects in the next table are **local activation/depth coefficients**,
not extra global parameters or hidden dataset constants. Their exact
definitions are the indicated finite recurrences or Gaussian integrals.

| Required component | Maximum allowed \(Ym/\gamma\) | Exact coefficient definitions |
|---|---|---|
| Dense fitting | \(1/(8H_D\sqrt{F_D})\) | [Dense fitting](GENERAL_EXPLICIT_FITTING.md), (2), (4) |
| All-order Legendre fitting | \(S_*^{\rm Leg}/8\) | [Closure fitting](GENERAL_EXPLICIT_CLOSURE_FITTING.md), (1)–(2) |
| Compact fitting | \(1/(16H_C\sqrt{F_C})\) | [Runtime fitting](EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md), (5) |
| Analytic source construction | \(S_*^{\rm src}/16\) | [Source bridge](UNBOUNDED_COMPRESSOR_BRIDGE.md), (5)–(10) |

The full common label condition is
\[
\boxed{\quad
0<Y\le\frac\gamma m\min\left\{
\frac1{8H_D\sqrt{F_D}},\frac{S_*^{\rm Leg}}8,
\frac1{16H_C\sqrt{F_C}},\frac{S_*^{\rm src}}{16}\right\}.
\quad}
\tag{full labels}
\]
The simpler (labels) implies this condition. The compact-versus-dense
theorem itself needs only the dense, compact and source rows; the extra
Legendre row is needed only for a common three-model statement.

On this **entire original range**, with the same source-eligible widths,
the same construction and the same probability qualification,
\[
\boxed{\quad
\|f_{\rm compact,n}-f_n\|_*
\le C\beta^{42L}Y\frac m\gamma
\max\!\left\{1,\sqrt{\frac m\gamma}\right\}
\frac{(1+\sqrt{\log(en)})e^{32\sqrt{\log(en)}}}{n}.
\quad}
\tag{full-range compact error}
\]
Here and in the next display, \(C\) is a universal numerical constant,
independent of all problem parameters; it can be enlarged to be the same
in both inequalities. In particular,
\[
\|f_{\rm compact,n}-f_n\|_*
\le\frac{C\beta^{42L}Y(1+m/\gamma)^2}{\sqrt n},\qquad
n\ge\max\{N_0(\delta),C^2\beta^{84L}Y^2(1+m/\gamma)^4
\varepsilon^{-2}\}
\ \Longrightarrow\ \|f_{\rm compact,n}-f_n\|_*\le\varepsilon.
\tag{full-range accuracy}
\]
The second implication holds on the same probability event. No activation
or sample/gap coefficient occurs inside the exponential, and no new label
or comparison-width gate is imposed. The proof gives finite numerical
constants; their conservatism is distinct from parameter dependence.

For size/storage on this larger range, use the **actual original source
coefficients**, not the beta-only envelopes of §3. Locally, let \(U,V\)
be source (22)–(25), evaluated at \(16Ym/\gamma\), and define the
source-rank budget
\[
A_n=\begin{cases}
\displaystyle
\frac{2^{20}9^d}{d!}\frac Ua
\left[\min\!\left\{\frac18,\frac a{8V}\right\}\right]^{-(d-1)}
\left(\frac{Ym}{\gamma}\right)^2[\log(en)]^{3d/2+1},&d\ge2,\\[6pt]
\displaystyle
8\cdot514\cdot1024\frac Ua
\left(\frac{Ym}{\gamma}\right)^2[\log(en)]^{5/2},&d=1.
\end{cases}
\]
Then the same constructed compact model has
\[
q=\lceil9(A_n+2m+d+1)\rceil,\qquad
\operatorname{storage}(f_{\rm compact,n})
\le2040(L+1)A_n^2+2040(L+1)(2m+d+1)^2+10m(d+1).
\tag{full-range size and storage}
\]
These are source (35)–(37), including the dimension-one case. No extra
coordinate is added by the sharper comparison. The logarithmic powers
and all fixed-task compression conclusions in §5 therefore persist.

For the other models on (full labels), use their recurrence-form
certificates: [dense comparison, (37)–(44)](GENERAL_DENSE_COMPARISON.md)
gives the same \(n^{-1/2+o(1)}\) rate, and
[Legendre comparison, (1)–(6)](EXPLICIT_LEGENDRE_COMPARISON.md) gives
the simultaneous-in-order error, admissibility condition and explicit
\(q=n^{1/4+o(1)}\) schedule for error \(Y/\sqrt n\). These are
fully specified coefficients, not the beta-only envelopes of §3 extended
beyond their proved range. The interface in §4 is unchanged: insert those
certificates and select an admissible order. Fixed-epsilon Legendre order
is still \(n^{o(1)}\). Their proofs and exact coefficients remain current
supporting derivations, not alternative results summaries.

The dense lower bound also holds on (full labels). To make its constant
explicit under (labels), define locally
\(q_0=1\), \(q_j=\mathbb E\phi_j(\sqrt{q_{j-1}}Z)^2\), and
\(\mu_4=\mathbb E\phi_L(\sqrt{q_{L-1}}Z)^4\), with \(Z\sim N(0,1)\).
One may take
\[
c_{\phi,L,\delta}=
\frac{\Phi^{-1}(1/2+\delta/4)}{128}\sqrt{\frac{q_L}{\mu_4}},
\]
where \(\Phi\) is the standard normal distribution function. On the
larger range multiply this by the positive activation/depth-only
coefficient in [the trajectory bridge, (18)](GENERAL_TRAJECTORY_LOWER_BRIDGE.md).
The witnessing positive time is at most
\(m/[\gamma\sqrt{\log(en)}]\) under (labels); on the larger range
multiply this time bound by the same coefficient in bridge (18).
There is no claim that it is bounded away from zero. Positive feature rank
for \(m\ge2\) rules out
deterministic label-weighted initialized features; a fourth-moment bound
and time analyticity turn the initial derivative fluctuation into this
actual-prediction lower bound. No specialized endpoint example is used.

## 7. Current proof map and claim boundary

The supporting proofs use local notation: their normalized gap
\(\lambda\), or \(g\) in the dense refinement, is \(\gamma/m\).
In the dense/Legendre refinements, \(B=\beta^{100L}\) and the activity
abbreviation \(z\) or \(s\) is \(Ym/\gamma\). Local source ranks,
moment indices and comparison variables are not additional model orders.

| Component | Complete derivation |
|---|---|
| Dense upper | [Signed-energy refinement](DENSE_SAMPLE_EXPONENT_REFINEMENT.md); [general comparison](GENERAL_DENSE_COMPARISON.md) |
| Dense lower | [General lower theorem](GENERAL_VARIABILITY_LOWER_RESULT.md), with its innovation, onset and trajectory proofs |
| Legendre error/order | [Signed-energy refinement](LEGENDRE_SAMPLE_EXPONENT_REFINEMENT.md); [full-range coefficients](EXPLICIT_LEGENDRE_COMPARISON.md) |
| Compact sharpened comparison | [Polynomial comparison](COMPACT_POLYNOMIAL_COMPARISON.md); [full-label-range proof](COMPACT_FULL_LABEL_RANGE.md); [source-energy lemmas](COMPACT_SOURCE_ENERGY.md) |
| Compact construction/storage | [Source bridge](UNBOUNDED_COMPRESSOR_BRIDGE.md), (30)–(37); [source constant ledger](SIMPLE_CONSTANTS_SOURCE_CHECK.md), (14)–(15) |
| Exact compact optimizer/fitting/endpoints | [Corrected-runtime equations and proof](EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md) |
| Current compact proof checks | [Polynomial comparison check](COMPACT_POLYNOMIAL_CHECK.md); [full-range check](COMPACT_FULL_LABEL_RANGE_CHECK.md) |

The compact size budget is not an arbitrary-width approximation theorem.
Its \(n^{-1+o(1)}\) certificate implies error \(Y/\sqrt n\)
eventually, not with coefficient \(Y\) at every source-eligible width.
The dense upper remains near-root; its strict-root replacement, sharp
sample/gap/dimension dependence, a general endpoint lower bound, and a
fully effective stochastic source width remain open. Storage counts real
coordinates; preprocessing work, bit precision and runtime complexity
are not claimed to improve. Internal reconstruction is not independent
promotion review, and this integration does not modify the maintained
book or paper.

# Explicit evaluator, input, and output costs

2026-10-06. Scoped author continuation of the same resource analysis.
This note expands compiler (33), records the computational interfaces
needed to turn its primitive counts into charged bit costs, and makes the
small-label normalization cost explicit. It adds no accuracy theorem or
statistical sufficient-width result. The three assigned scientific inputs
were read completely: `PARAMETER_EXPLICIT_RESOURCES.md`,
`COMPILER_PARAMETER_ACCOUNTING.md`, and `EXPLICIT_COMPILER_EXPONENT.md`.
The supervisor additionally supplied the definition of the activation
envelope below, identifying finite-panel RESULT (1) and the physical
parameter note (2) as its sources. No other scientific inputs were read.

## 1. Parameters and finite computation

Use dense width \(n\), training count \(m\), input dimension \(d\),
hidden depth \(L\ge2\), initial Gram gap \(\gamma>0\), label RMS
\(Y=\|y\|_2/\sqrt m\), and failure probability \(0<\delta<1\).
Training inputs have norm \(\sqrt d\) and span the input space, so
\(d\le m\). Preserve the original full intersection of label
allowances, which in particular supply \(16Ym/\gamma\le1\) and
\(Y\le\beta^{3L}\). This note treats \(Y>0\); the supplied exactly-zero-label
branch returns zero. Deciding whether arbitrary precision-access real
labels are all exactly zero is not a free input operation.

If the activations \(\phi_j\), \(1\le j\le L\), are analytic on
the common strip \(|\operatorname{Im}z|<a\), the supplied envelope is

\[
 \beta=\max\left\{10,
  1+\max_{j\le L}|\phi_j(0)|,\ \frac{16}{a},
  \max_{\substack{j\le L\\k=1,2}}
       \sup_{|\operatorname{Im}z|\le a/2}|\phi_j^{(k)}(z)|
                    \right\}.
 \tag{1}
\]

This is the mathematical activation dependence. It does not bound the
length or running time of a supplied program evaluating \(\phi_j\).
Set

\[
 A=m+d+2,\qquad r=m/\gamma,\qquad
 Z=\log(en)+\log\!\left(e+
       \frac{A\beta^{100L}(1+r)}{\delta}\right).
 \tag{2}
\]

Here \(\log\) is natural; precision and encoding lengths use base two.
Fix the normalized deterministic accuracy exponent at the universal value
\(a_0=10\) for this cost interface; it is not a free accuracy parameter.
The logarithm in compiler (34) differs from (2) by at most a numerical
factor depending on this fixed choice: for
\(K=A\beta^{100L}(1+r)/\delta\ge1\),
\(\log K\le\log(e+K)\le\log K+\log(e+1)\).
Thus using (2) does not absorb a scientific parameter into a constant.

The composed numerical bounds supplied by compiler Section 8 are

\[
 M\le C\beta^{301L}A(1+r)^3Z^6,\qquad
 \Theta\le C\beta^{200L}(1+r)Z^2,\qquad \chi\le\Theta.
 \tag{3}
\]

\(M\) is the counted program-size bound, and \(\Theta,\chi\) are
logarithmic numerical certificates, with the definitions in compiler
(3) and (30). They are substitution variables here, not additional free
scientific parameters. All occurrences of \(C\) below mean numerical
compiler-template constants, with no dependence on
\(n,m,d,\gamma,Y,L,\phi,\delta\), data encodings, or evaluator programs.
The supplied sources do not assign literal numerical values to these
universal constants. This note does not claim to do so.

## 2. Expanded call counts and numerical arguments

Let \(K_{\rm init},K_{\rm upd},K_{\rm query}\) denote upper bounds
on the primitive invocations in complete initialization, all compact
acquisition updates, and one unseen-input query. A primitive is an
activation/first-derivative evaluation or a requested data-literal access.
It is safe to use each bound for either family separately. Compiler (33),
including its additional coefficient-preparation allowance, gives

| Phase | Number of primitive invocations |
|---|---:|
| Complete initialization | \(K_{\rm init}=C n\beta^{2709L}A^9(1+r)^{27}Z^{54}\) |
| All acquisition updates | \(K_{\rm upd}=C\beta^{3311L}A^{11}(1+r)^{33}Z^{66}\) |
| One complete query | \(K_{\rm query}=C n\beta^{6220L}A^{20}(1+r)^{61}Z^{122}\) |

Sufficient requested precision bounds are

\[
 \begin{split}
 b_a&=\left\lceil C\beta^{2909L}
                   A^9(1+r)^{28}Z^{56}\right\rceil,
       &&\text{initialization and updates},\\
 b_q&=\left\lceil C\beta^{3511L}
                   A^{11}(1+r)^{34}Z^{68}\right\rceil,
       &&\text{query row evaluation and preparation},\\
 h&=\left\lceil C\beta^{200L}(1+r)Z^2\right\rceil,
       &&\text{argument integer/magnitude bits}.
 \end{split}
 \tag{4}
\]

The constants are selected to satisfy the compiler's local arithmetic
and half-gap margins; larger precision is allowed. One uniform choice
\(b=b_q\) covers every call, after increasing its numerical constant.
A primitive receives a dyadic argument of magnitude at most \(2^h\),
with at most \(b_a+h+O(1)\) or \(b_q+h+O(1)\) ordinary argument bits,
and is asked for absolute output error at most \(2^{-b_a}\) or
\(2^{-b_q}\). The compiler already accounts for amplification of
argument-rounding and primitive-output error. Matrix macros can use
larger private integer buffers; those are in the nonprimitive row bound,
not additional activation argument precision.

The unseen query-coordinate request itself needs only the context
precision \(p_{\rm ctx}\le b_a\). This request is for all \(d\)
coordinates. Its access cost must be charged even though the rounded
\(d\)-word working buffer fits the core memory bound.

To check every exponent, a monomial \(M^u\Theta^v\) contributes

\[
 \beta^{(301u+200v)L}A^u(1+r)^{3u+v}Z^{6u+2v}.
 \tag{5}
\]

The call counts use \((u,v)=(9,0),(11,0),(20,1)\).
The two precisions use \((9,1),(11,1)\); hence their activation
exponents are \(2709+200=2909\) and \(3311+200=3511\).
The query coefficient-preparation calls are at most \(CM^{11}\),
which are covered by \(CnM^{20}\Theta\) for \(n\ge1,M\ge2,\Theta\ge2\).
Finally the logarithm of the certified operand bound is at most \(\chi\),
so (3) proves the argument bound \(h\). These are direct substitutions;
none trades a parameter factor against a larger width threshold.

## 3. Label normalization and the retained output scale

The internal graph accesses \(y_i/Y\), whose magnitude is at most
\(\sqrt m\). Suppose the original label interface instead returns
\(\widetilde y_i\) with absolute error at most \(\varepsilon\).
The RMS norm is 1-Lipschitz in the maximum coordinate norm, because

\[
 \left|\frac{\|\widetilde y\|_2}{\sqrt m}-Y\right|
 \le\frac{\|\widetilde y-y\|_2}{\sqrt m}\le\varepsilon.
 \tag{6}
\]

Compute that approximate RMS to an additional absolute error at most
\(\varepsilon\), obtaining \(\widehat Y\). Then
\(|\widehat Y-Y|\le2\varepsilon\). If \(\varepsilon\le Y/4\),
\(\widehat Y\ge Y/2\), and \(|y_i|\le\sqrt mY\) gives

\[
 \left|\frac{\widetilde y_i}{\widehat Y}-\frac{y_i}{Y}\right|
 \le\frac{2\varepsilon}{Y}
       +\frac{4\sqrt m\,\varepsilon}{Y}
 \le\frac{6\sqrt m\,\varepsilon}{Y}.
 \tag{7}
\]

Consequently, to produce normalized labels to absolute error \(2^{-b}\),
the sufficient raw-label accuracy is

\[
 b_Y=b+\left\lceil\log_2(16\sqrt m)\right\rceil
         +\left\lceil\log_2\max\{1,Y^{-1}\}\right\rceil.
 \tag{8}
\]

Take \(\varepsilon=2^{-b_Y}\). Formula (7) uses less than half the
requested budget; final division/rounding can use the remainder.
Thus there is no inverse power of \(Y\) in (3)--(4), but an
absolute-precision label interface pays the explicit
\(\log^+(1/Y)\) access overhead (8). Its cost cannot be dropped.
Selecting this precision requires a certified magnitude estimate for
the nonzero scale. Such an estimate may be supplied or obtained by
refining label intervals until their RMS has a positive lower bound;
the actual refinement calls and their work belong to input acquisition.
No zero-test or lower bound for arbitrary real labels is assumed free.

For example, if \(T_y(w)\) is the maximum cost of obtaining one raw
label to absolute error \(2^{-w}\), a direct normalization batch costs

\[
 mT_y(b_Y)+C(m+1)
    [b_Y+h+\lceil\log_2(m+2)\rceil]^3.
 \tag{9}
\]

This elementary implementation reads all labels, sums their squared
dyadic values, divides by \(m\), computes a scalar square root by
bisection, then divides the labels by its positive approximation.
Writing \(v=b_Y+h+\lceil\log_2(m+2)\rceil\), squared dyadic sums
and divisions use \(O(v)\)-bit integers and schoolbook \(O(v^2)\)
arithmetic; \(O(v)\) bisection steps suffice. Thus (9) is a safe upper
bound. Its extra workspace is at most \(C(m+1)v\) bits plus the
largest input-provider workspace. Alternatively, stream the labels twice:
the first pass accumulates their squared sum and computes \(\widehat Y\);
the second obtains each label again and immediately stores its normalized
value. The second-pass approximation need not equal the first: each has
the same absolute error bound, so (7) still applies. This uses at most

\[
 2mT_y(b_Y)+Cm v^3\quad\text{work},\qquad
 C(mb+v)+S_y(b_Y)\quad\text{extra peak bits},
 \tag{9a}
\]

where \(S_y\) is the single raw-label-provider workspace. Normalized
integer parts require \(O(\log(m+2))\) bits per coordinate, already
covered because \(b\) is one of (4). For these same choices
\(h\le Cb\le Cb_Y\), so \(v\le C[b_Y+\log_2(m+2)]\).
The squared-sum accumulator and scalar arithmetic need \(O(v)\) live
bits, while the completed normalized-label cache needs \(O(mb)\).
The scale magnitude certificate used to select \(b_Y\), or its
acquisition, is still charged separately as explained above. A cached
normalized-data interface pays the selected batch cost once at the
maximum required precision. An uncached interface may pay it on every
requested normalized-label access; the formulas below allow either
declared implementation.

Returning a numerical physical prediction also requires the scale \(Y\).
Write \(Y=2^{e_Y}s_Y\), where \(e_Y=\lfloor\log_2Y\rfloor\) and
\(1\le s_Y<2\). A signed binary exponent needs

\[
 E_Y=2+\left\lceil\log_2(2+|e_Y|)\right\rceil
 \tag{10}
\]

bits up to a numerical coding factor. This uses \(e_Y\) only to bound
encoding length: an implementation can use the exponent of a certified
positive approximation, differing from \(e_Y\) by at most one, and a
mantissa in \([1/2,2]\). It need not decide exact equality with a power
of two. A relative-precision scale with
\(b_s\) mantissa bits therefore costs \(C(b_s+E_Y)\) retained bits.
One may use \(b_s\le Cb_q\): if the normalized output is bounded by
\(2^h\), relative scale error at most \(2^{-(b+h+2)}\) contributes
at most \(Y2^{-b}/4\) to the final error. This is already within the
precision schedule (4), with its constant enlarged. It is numerical
error bookkeeping, not a new scientific accuracy estimate.

The \(b_s\) mantissa fits the existing core bound. Before applying a
source-width restriction, the exponent \(E_Y\) is not uniformly bounded
as positive \(Y\) tends to zero and is therefore kept explicit. On an
inherited domain with \(n^{-1}\le Y\), its size can instead be dominated
by the existing logarithmic width factors; the additional charge is
conservative, not a disproof of the source's bound on that domain.
If outputs use fixed-point dyadics instead,
relative scale accuracy additionally needs
\(\lceil\log_2^+(1/Y)\rceil\) fractional positions, where
\(\log_2^+u=\max\{0,\log_2u\}\). Alternatively a
factored output can retain a description of the exact scale and the
normalized prediction, but that is a declared output representation with
its scale-description/access cost; it is not a free ordinary numerical
prediction. Denote the actual supplied scale-description length by
\(B_Y\), including it in the input descriptions below without double
counting when it is already represented by the original labels.

## 4. Additive computational contract

Specify finite programs or encodings for the following interfaces.

* \(B_\phi\) counts the entire activation/derivative evaluator description.
  \(T_\phi(b,h)\) and \(S_\phi(b,h)\) are the maximum work and
  additional live workspace for one call to any \(\phi_j\) or
  \(\phi'_j\), on the dyadic arguments and tolerances in Section 2.
* \(B_{\rm data}\) counts the data and scale providers/encodings.
  \(T_{\rm data}(b,h)\) and \(S_{\rm data}(b,h)\) are the maximum
  work and additional workspace for one requested normalized training
  literal or other input literal. They include the actual normalization
  implementation, for example (8)--(9), and any divisions or scale access.
  Declaring a primitive directly for \(y/Y\) is permitted only if its
  description, acquisition, and evaluation costs are charged here.
* \(B_{\rm cert}\) is the finite numerical-certificate description.
  \(T_{\rm cert},S_{\rm cert}\) are its generation/verification work
  and extra workspace. They vanish only for operations already completed
  and outside the declared execution being counted. Analytic certificate
  formulas do not supply a cost bound for verifying an arbitrary input
  activation program or an original nonlinear-flow event.
* \(T_x(b_a),S_x(b_a)\) include acquiring the complete new query's
  \(d\) coordinates and the requested time to context precision. For
  querying the model's internal clock, that time-access cost is already
  counted by its clock representation. An externally supplied time has
  its own encoding and precision-access cost, included here. The original description
  length \(B_x\) is charged when it is supplied; it is part of this
  input work and live workspace unless already counted separately.
* \(T_{\rm input},S_{\rm input}\) count initial acquisition/parsing and
  preparation not charged in the preceding calls, including any scale
  magnitude search, normalization cache, or output-scale construction.
  \(T_{\rm out},S_{\rm out}\) count conversion to the declared physical
  output format when not included in the core arithmetic. A relative
  floating output charges exponent operations in \(E_Y\); an ordinary
  fixed-point output charges all of its actually emitted bits.

Let \(B_{\rm in}=B_\phi+B_{\rm data}+B_{\rm cert}\), including
\(B_Y\) once. Disjoint accounting is intended: the same input read or
normalization batch is charged once, at the point where it is performed.
Define \(W^0_{\rm init},W^0_{\rm upd},W^0_{\rm query}\) and
\(S^0_{\rm ret},S^0_{\rm peak},S^0_{\rm init}\) by the following
nonprimitive upper bounds, each multiplied by \(C\beta^{65000L}\):

| Resource | Core bound before that common factor |
|---|---:|
| \(W^0_{\rm init}\) | \(nA^{146}(1+r)^{454}Z^{908}\) |
| \(W^0_{\rm upd}\) | \(A^{148}(1+r)^{460}Z^{920}\) |
| \(W^0_{\rm query}\) | \(nA^{189}(1+r)^{584}Z^{1168}\) |
| \(S^0_{\rm ret}\) | \(A^{23}(1+r)^{72}Z^{144}\) |
| \(S^0_{\rm peak}\) | \(A^{66}(1+r)^{204}Z^{408}\) |
| \(S^0_{\rm init}\) | \(nA^{10}(1+r)^{31}Z^{62}+A^{54}(1+r)^{168}Z^{336}\) |

For the source's primitive-access implementation the fully charged work
contract is

\[
 \begin{split}
 W_{\rm init}\le{}&W^0_{\rm init}+T_{\rm input}+T_{\rm cert}
       +K_{\rm init}[T_\phi(b_a,h)+T_{\rm data}(b_a,h)],\\
 W_{\rm upd}\le{}&W^0_{\rm upd}
       +K_{\rm upd}[T_\phi(b_a,h)+T_{\rm data}(b_a,h)],\\
 W_{\rm query}\le{}&W^0_{\rm query}+T_x(b_a)+T_{\rm out}
       +K_{\rm query}[T_\phi(b_q,h)+T_{\rm data}(b_q,h)].
 \end{split}
 \tag{11}
\]

All call counts and all numerical arguments to the external cost
functions are explicit in (2)--(4). These cost functions denote actual
computational interfaces; none is an unnamed scientific constant.
Reading retained descriptions on each restart must also be charged if
the chosen execution model requires it. Ordinary input loading costs at
least the number of description bits actually read.

With the conservative choice to retain the supplied descriptions and a
numerical floating scale, memory satisfies

\[
 \begin{split}
 S_{\rm ret}\le{}&S^0_{\rm ret}+B_{\rm in}+CE_Y,\\
 S_{\rm init}\le{}&S^0_{\rm init}+B_{\rm in}+CE_Y
       +S_{\rm input}+S_{\rm cert}
       +S_\phi(b_a,h)+S_{\rm data}(b_a,h),\\
 S_{\rm upd}\le{}&S^0_{\rm peak}+B_{\rm in}+CE_Y
       +S_\phi(b_a,h)+S_{\rm data}(b_a,h),\\
 S_{\rm query}\le{}&S^0_{\rm peak}+B_{\rm in}+CE_Y+S_x(b_a)+S_{\rm out}
       +S_\phi(b_q,h)+S_{\rm data}(b_q,h).
 \end{split}
 \tag{12}
\]

Sequential invocation needs only single-call workspaces, not their
product with the number of calls. The sums in (12) are safe even when
some areas can be reused. A cached data interface must count its retained
cache; the rounded training coordinates and normalized labels at (4)
fit the displayed core bits, since there are \(m(d+1)\le A^2\)
entries. Unrounded originals, provider code, scale encoding and additional
provider workspace remain the separate terms above.

## 5. What this closes and what it does not

Equations (3)--(5) close the substitution from compiler (33) to explicit
scientific-parameter call counts, precision and argument magnitudes.
Equations (6)--(10) show exactly where normalization and numerical scale
storage reintroduce dependence on small \(Y\). Equations (11)--(12)
give a complete additive accounting contract once the actual input,
certificate and evaluator implementations are specified.

There is no universal replacement of those implementations by a function
of the analytic envelope alone. For example
\(\phi(x)=x+c\), \(0<c<1\), has uniformly bounded analytic envelope
on a fixed strip, while a noncomputable \(c\) admits no precision
evaluator. Even within computable inputs, a supplied data/evaluator
description can have arbitrarily large length or evaluation cost without
changing \(n,m,d,\gamma,Y,L,\beta,\delta\). A uniform fully charged
polynomial needs an additional computational input hypothesis, with its
degree and constants stated. Merely calling a primitive fixed does not
make its description and evaluations free in (11)--(12).

The explicit sampler condition \(n\ge512\max(K_*,1)\), the original
physical/source probability events, and the statistical comparison to
the dense-pair certificate retain their existing status. Numerical
certificate generation is separate from establishing those scientific
events. This note neither supplies a parameter-uniform statistical
sufficient width nor uses its very large numerical circuit propagation
bound as a statistical error estimate. It also does not establish a
finite-bit accuracy theorem for the older exact-real panel ODE or a
number of numerical ODE steps sufficient for training it.

Author checks on 2026-10-06: the exponent substitutions (5) were checked
numerically for all three call counts, both precision bounds, and all
seven monomials in the core resource table. The normalization argument
(6)--(9), the near-power-of-two scale representation, and the additive
workspace conventions were reread against the complete assigned inputs.
There was no experiment or implementation benchmark. The checked input
SHA-256 digests were:

| Assigned input | SHA-256 |
|---|---|
| `PARAMETER_EXPLICIT_RESOURCES.md` | `e445d45042311d567df35a86c2c48b69f20c5450a25b215d75096e358a0e4ed9` |
| `COMPILER_PARAMETER_ACCOUNTING.md` | `00c017e1b39e96de79ca062b207514cef5cb045507f7cef4ed4975b69fa07c6e` |
| `EXPLICIT_COMPILER_EXPONENT.md` | `93510e4e88f9c632e9c439715b655d4ea6dc1701aae655f0a30d45cbf7f4ba3a` |

Process limitation: `solve-math-rigorously` and `investigate-conjectures`
and its relevant references were read. The required canonical-notation
skill at `/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`
remained permission denied, as already reported to the supervisor. The
explicit repository notation requirements and the assigned sources'
notation were used; the inaccessible skill and its neural-network
reference are not claimed as read. This is an author derivation, not an
independent review or promotion.

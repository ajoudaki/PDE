# Bounded mathematical check of the causal Taylor source

2026-10-06. Verdict: **PASS for the stated conditional source-call result**,
with one nonblocking precision clarification below. This is a separate
internal mathematical check, not a blind promotion review or a compact
decoder theorem.

The reviewed candidate is `SANE_TAYLOR_SOURCE.md`, SHA-256
`f61d9635fea24cc72a4d80b315ee1736017091bde410708644afc0df7b0fedce`.
The assignment initially named a different hash; the mismatch was reported,
and the supervisor explicitly confirmed this replacement hash before the
substantive review continued. The confirmed hash was checked again before
this report was written.

## 1. Exact claim checked

The reference is the nonlinear width-\(n\) network with \(L\ge2\) hidden
layers, \(m\) training samples, \(d\) input coordinates, exactly zero initial
stored readout, mean squared loss, and block mobilities
\((n,1,\ldots,1,n)\). All hidden matrices continue to train. Retain the
original intersection of the fitting and source label allowances.

Write \(Y=\|y\|_2/\sqrt m>0\), \(\lambda=\gamma/m\),
\(r=\lambda^{-1}\), \(S=16Yr\le1\), \(\ell=\log(en)\), and
\(B=\beta^{100L}\), where \(\beta\) is the stated activation envelope.
For \(1\le a_0\le12\), define

\[
 Z=(a_0+1)\ell+\log(e+B(1+r)).
\]

On the inherited dense fitting and finite-query complex source event,
with the inherited width requirements and the candidate's additional
explicit horizon gate, the source program has at most

\[
 C\{d+mL\beta^{200L}(1+r)^2Z^2\sqrt\ell\}
\]

initialized matrix calls and principal coefficient fields. Its numerical
prediction, frozen after its final source time, differs from the true
prediction by less than \(Y n^{-a_0}\), uniformly over all real unit
queries and all physical times, including the true fitted endpoint.
Zero labels give the stationary zero predictor separately.

This count retains width-\(n\) vectors and the initialized matrices.
It does not bound total scalar instructions, all temporary coordinate
arrays, complete stored coefficients, or total bit complexity. Smaller
parameter tolerances within the same finite horizon are available by
increasing the Taylor degree; the displayed all-time accuracy statement
has the explicitly stated range \(1\le a_0\le12\).

## 2. Complex source event and the thin parameter neighborhood

The required training carrier maximum is already a complex-time maximum.
In `UNBOUNDED_COMPRESSOR_BRIDGE.md`, the running amplitudes in (11) use
suprema over the stopped complex rectangle, and (23) improves the
preactivation and carrier maxima on that rectangle. Sections 2–3 of
`GENERAL_TRAJECTORY_LOWER_BRIDGE.md` keep the training budgets and carrier
argument while localizing the passive queries. Thus the candidate does
not replace a real carrier bound by an unproved complex carrier bound.
No additional Gaussian event is introduced here.

Use the candidate's displacement sum norm

\[
 \|u\|=\frac{\|A-A_0\|_F}{\sqrt n}
 +\sum_{j=2}^L\|W^{(j)}-W_0^{(j)}\|_F
 +\frac{\|w\|_2}{\sqrt n},
 \qquad \bar u(\tau)=u(\tau/\lambda)/Y.
\]

The proposed normalized radius is

\[
 d_n=\frac{\beta^{-200L}q(T)}{(1+r)^2\sqrt n},
 \qquad q(\tau)=2^{-\lfloor\tau/4\rfloor}.
\]

Its physical radius is \(Yd_n\). A stopped parameter segment of this
length has forward coordinate displacement at most
\(\sqrt n\,\beta^{4L}Yd_n\). The fitting inequalities
\(Y\le\beta^{3L}\), \(r^{-1}\le\beta^{6L}\), together with
\(a\ge16/\beta\), make this strictly smaller than \(a/16\).
Consequently the segment stays inside the activation half-strip and
the operator caps can be enlarged from ten to eleven deterministically.

For backward subtraction, the changed gate multiplies the reference
carrier, whose maximum is \(K_{\rm src}S\sqrt\ell\). Subsequent
backward layers propagate the resulting difference linearly. They do
not introduce another carrier maximum at each layer. The candidate's
loose \(\beta^{50L}(1+S\sqrt\ell)Yd_n\) RMS bound consequently
has sufficient exponent slack. After converting RMS to coordinates,
the relative carrier increase is bounded by

\[
 \frac{\beta^{-150L}q(T)}{16r(1+r)^2}
              (\ell^{-1/2}+S)<1.
\]

This also verifies that small labels cause no hidden inverse-label
restriction: \(Y/S=1/(16r)\), and the remaining inverse gap is explicitly
controlled. The nearby readout RMS and forward/backward RMS bounds have
the stated slack.

At patch anchor \(\tau_j\), the source residual equation on a short
radial contour gives residual RMS at most \(2Y e^{-\tau_j/4}\).
Prediction subtraction contributes at most \(\beta^{8L}Yd_n\),
so the entire nearby neighborhood has residual RMS at most \(3Yq_j\),
where \(q_j=q(\tau_j)\). Splitting every gradient difference into
its residual, backward, and forward factors therefore yields

\[
 \|D\overline F\|\le
 \Lambda_j=B(1+r)(1+q_j\sqrt\ell).
\]

Normalizing state and time multiplies the physical field Lipschitz
constant by \(r\), not by \(r/Y\). The complex field uses algebraic
transposes and holomorphic activations. The real-valued norm and its
conjugates do not appear in the field formula. Holomorphy is therefore
valid on the stated neighborhood without extending a clipped field.

## 3. Approximate anchors and Taylor stability

For the candidate's patch lengths,
\(4h_j\Lambda_j\le1/8\) and the disk of radius \(4h_j\) lies
inside the original source domain. With exact anchor \(a\), approximate
real anchor \(b\), and \(e=\|b-a\|\le d_n/8\), the difference
Picard map acts on holomorphic functions with supremum norm at most
\(d_n/2\). Its Lipschitz constant is at most \(1/8\), and it maps
that ball strictly into itself. Uniform convergence on smaller closed
disks gives a holomorphic nearby flow; uniqueness joins these disks.
Radial integration then proves

\[
 \|X_b(z)-X_a(z)\|\le e e^{\Lambda_j|z|}<2e.
\]

Applying Cauchy's formula to this difference on the radius-\(2h_j\)
circle is the key stability step. At \(0\le s\le h_j\), its Taylor
tail is at most \(2e2^{-K}\). The reference derivative bound \(M\)
gives reference state tail at most \(2Mh_j2^{-K}\). Thus the endpoint
error obeys

\[
 e_{j+1}\le(1+2h_j\Lambda_j+2\,2^{-K})e_j
                         +2Mh_j2^{-K}.
\]

There is no fixed factor two per patch. Since \(\int_0^\infty q=8\)
and the excess of the left sums telescopes to at most \(h\),

\[
 \sum_jh_j\Lambda_j\le E=B(1+r)(T+9\sqrt\ell).
\]

The explicit degree (22) pays for both \(2E\) and \(H2^{-K}\) in
the multiplier product. Iteration gives (23), including interior times.
Its error is below \(d_n/64\), closing the anchor hypothesis by
induction. Because \(\log(d_n^{-1})\le CZ\), this bootstrap costs
only \(K\le CB(1+r)Z\). No dimension-dependent analytic theorem or
unproved stability of a truncated polynomial flow is needed.

## 4. Horizon and all-time prediction

The explicit gate
\(n\ge\max\{1,e^{-1}\sqrt{1+66Br}\}\) implies
\(\log(1+66Br)\le2\ell\). Hence

\[
 T=2\{a_0\log n+\log(1+66Br)\}
       \le(2a_0+4)\ell\le28\ell<32\ell.
\]

The source disks therefore stay within the originally available complex
rectangle, including its padding at time zero. The argument does not
use an extension of the late-time complex carrier maximum.

The all-time fitting bound (11) in `GENERAL_EXPLICIT_FITTING.md`,
with \(H^2\le B\), makes the normalized endpoint tail at \(T\)
smaller than \(n^{-a_0}/4\). The real parameter-to-output sensitivity
is at most \(B\) uniformly over the whole input sphere. Combining
these facts with (23) proves the claimed all-time error after freezing
the numerical endpoint. This is an approximation of the original flow,
not a claim of exact numerical interpolation or a new physical optimizer.

## 5. Matrix chronology, rank summands, and scalar work

Recurrence (25) is causal: coefficient \(k+1\) uses only state
coefficients through \(k\). Increasing forward-layer order, followed
by decreasing backward-layer order, evaluates the coefficient passes.
Each initialized term in (26) requires one action for the relevant
coefficient. Learned terms use previously represented rank-one factors
and scalar pairings. The first layer uses its \(d\) initialized columns.

For each hidden layer and patch, (27) has \(O(mK^2)\) rank-one
summands but only \(O(mK)\) distinct residual-weighted backward factors
and \(O(mK)\) distinct forward factors. A committed endpoint appends
these factors and their scalar coefficients; it need not expand them
recursively into new source vectors. Consequently

\[
 H\le CB(1+r)Z\sqrt\ell,\qquad
 \#\text{initialized calls}\le C(d+mLHK)
       \le C\{d+mLB^2(1+r)^2Z^2\sqrt\ell\}.
\]

The separate direct scalar coefficient description can contain
\(O(mLHK^2)\) weights. Activation composition can require
\(O(K^3)\) scalar work and \(O(K^2)\) scratch per coordinate series.
These costs do not invalidate the matrix-call bound, but must be charged
when compiling the source or claiming storage. The candidate explicitly
keeps them separate.

The coefficient bounds for forward/backward training fields follow
from Cauchy's formula on \(|\xi|=2\). Raw initialized images inherit
an RMS bound from the operator event; converting it to a coordinate
bound may cost \(\sqrt n\). The note correctly does not claim a new
polylogarithmic coordinate maximum for every such answer. A late passive
query also adds its own forward initialized actions. Neither issue is
silently hidden inside the principal-field count.

## 6. Finite jets and the precision qualification

For \(q\ge1\), repeated integration of a forward difference gives

\[
 \eta^{-q}\Delta_\eta^q\phi(x)
 =\int_{[0,1]^q}\phi^{(q)}(x+\eta\textstyle\sum_i t_i)\,dt.
\]

Cauchy's formula for \(\phi'\) on a radius-\(a/4\) circle gives
\(\sup_{\mathbb R}|\phi^{(q+1)}|\le q!\beta D^q\), with
\(D=\max\{1,4/a\}\). These facts prove (31). The value-error
amplification is exactly bounded by \(2^q/(q!\eta^q)\), so (33)
controls every jet in the requested finite list. Multiplying a normalized
jet by \(q+1\) to obtain a coefficient of \(\phi'\) requires the
additional tolerance factor identified in the candidate.

The whole finite coefficient program has a deterministic finite error
amplification bound obtained recursively from operand magnitudes and
derivative bounds. Initial matrix entries are bounded on the operator
event; the coordinate conversion may use \(\sqrt n\). Jet derivatives
are bounded uniformly on the real line, and activation values have
linear growth. Thus the precision can be chosen before executing the
program, with no future trajectory input or additional initialized call.
The conversion to normalized state error includes \(1/Y\); the
inherited gate \(Y\ge n^{-1}\) makes that dependence explicit.

This argument establishes finite approximation conditional on a value
evaluator at the charged precision. It does not make arbitrary analytic
activations computable, and it proves no useful polynomial bit bound.
The candidate states both limitations.

**Nonblocking clarification.** Equation (34)'s upper bound on value
precision requires choosing \(\eta\) equal to, or within a fixed factor
of, the largest value allowed by (32) and \(\eta\le1\). The inequality
\(\eta\le\cdots\) alone also permits arbitrarily smaller spacings
and arbitrarily larger precision. Choosing the largest admissible dyadic
spacing makes (34) valid with a numerical change in its constant. This
does not affect the source-call theorem or finite-jet existence.

## 7. Scope, independence, and remaining claims

No blocking defect was found in this source-solver argument. The supplied
source event remains an inherited research dependency with unquantified
stochastic success width. The complete noisy Gaussian compiler, source
selection, uniform unseen-query replacement, total retained and peak
decoder memory, and useful bit/work bounds remain unproved by this note.
In particular, squaring the call count is not a decoder storage proof.

The complete assigned candidate and these allowed dependencies were read:
`PHYSICAL_PARAMETER_ACCOUNTING.md`, `SANE_ADAPTIVE_TIME.md`,
`SHORT_CAUSAL_TRAINING_PROGRAM.md`, and the integrated-study
`UNBOUNDED_COMPRESSOR_BRIDGE.md`, `GENERAL_TRAJECTORY_LOWER_BRIDGE.md`,
`GENERAL_EXPLICIT_FITTING.md`, and `ANALYTIC_TAIL_EXTENSION.md`.
Links to additional scientific artifacts were not followed. No study
README, history, other review report, or unauthorized scientific source
was read.

The rigorous-math and conjecture-audit skills and their relevant references
were applied. The custom canonical-notation skill was permission-inaccessible;
the supervisor's explicitly authorized fallback was the repository's
notation instructions and the complete `docs/notation.qmd` contract.

After this reviewer had independently sent the supervisor its no-blocker
reconstruction summary covering the tube, Taylor stability, counts, and
finite jets, the supervisor sent a brief preliminary assessment of the
same argument. Its receipt is disclosed here: this report is therefore
a bounded internal check, not a blind review. The conclusions above rest
on the reconstruction and assigned sources, not that assessment.
No experiment or Git operation was performed. Only this assigned report
was written.

## 8. Bounded correction check and current resolution

2026-10-06. The nonblocking precision clarification in Section 6 is
**resolved** in the current candidate, SHA-256
`24b8d368da31e9d8bf00bb1c7fc85f75cb0efcc30a9cbc8409ac9c520bb916af`.
The original review above is preserved. This follow-up checked only the
reported spacing correction, the integral punctuation correction, and
the introductory replacement of fixed-parameter big-O notation by its
equivalent logarithmic-power statement; it did not expand the scientific
scope.

The revised passage specifies \(0<\varepsilon_{\rm jet}\le1\) and
chooses \(\eta=2^{-b}\), with integer \(b\ge0\), as the largest
such power of two allowed by (32). In particular, if

\[
 U=\frac{\varepsilon_{\rm jet}}
             {2(K+1)\beta D^{K+1}},
\]

then \(U<1\) and \(U/2<\eta\le U\). Therefore (33) gives

\[
 \log(\xi^{-1})
 \le\log(2/\varepsilon_{\rm jet})
 +(K+1)\left[
  \log\frac{8(K+1)\beta}{\varepsilon_{\rm jet}}
  +(K+1)\log D\right],
\]

which proves the upper bound in (34). The intermediate wording
"largest dyadic number" was clarified to a power of two so that the
maximization is over a discrete set, not all dyadic rationals.

The corrected integral now has its differential outside the bracket,
and the introductory wording preserves the same fixed-parameter
\(\log(en)^{5/2}\) claim. Neither changes the mathematical argument.
The conditional source-call **PASS** remains in force, with no unresolved
correction from this review. The decoder, noise-compiler, and bit/work
limitations recorded above remain unchanged.

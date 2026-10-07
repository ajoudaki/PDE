# Internal audit of the actual-variability decoder refinement

2026-10-07. Scoped internal mathematical audit, not an independent promotion
review. No paper, RESULT, maintained-book, code, or Git edits were made.

**Verdict: PASS for the proposed replacement, with the stated numerical
remainder and eventual-width qualification.** I found no substantive gap in
the restricted-center argument, probability accounting, scalar transcript
transfer, extension to the full query domain, or eventual factor-three
consequence. This verdict concerns the refinement's use of its inherited
source and finite-decoder interfaces; it is not a new independent
certification of the entire source theorem or initialized CLT.

The checked candidate was
`VARIABILITY_DECODER_REFINEMENT.md`, SHA-256
`783ce30306b7db97429ff0d6d0b2d044b682ae921d043215195527ccda453224`.
The finite construction and backend hashes were respectively
`921c33fb51aabbb4d4d12feeac024b1e25a99fbce0003fc39640e9f9f6472a2d`
and
`77f6261860ee8604405e0acb78ed2ed09468bf2b123233ae413d1a666c1d1686`.

## Inputs and audit boundary

I read the complete frozen candidate, the complete
`DECODER_FINITE_CONSTRUCTION.md` (FC), and
`DECODER_WORD_BACKEND.md` (WB) Sections A and F. I used my own
`VARIABILITY_METRIC_LEMMA.md` as an elementary comparison, not as a
substitute for checking the physical center and finite-program assumptions.
The inspected RESULT passages were its explicit Logarithmic decoder
statement and gates; sharper initialization statement (IC.58); the finite
source conclusion and reference bridge (IC.83)--(IC.90); global fitting and
uniform-tail proof; actual-trajectory lower theorem; derivative-to-trajectory
application; and exact constant-feature exceptions. The other parts of
the source insertion proof, the initialized CLT proof, and numerical backend
Sections B--E remain inherited dependencies.

No other studies, historical reviews, earlier verdicts, external papers, or
paper files were read. The required canonical-notation skill and its neural
reference, and the rigorous-math skill, were applied.

## The actual quantile and physically admissible center

Let \(F,F'\) be independent ordinary dense trajectories, let
\(\alpha=\delta/32\), and write \(b=b_n(\delta)\). The candidate assigns
distance \(+\infty\) to an invalid trajectory pair rather than conditioning
the initialization law on source success. On the reference good event,
the cited fitting estimates give

\[
 \|w(t)\|_2/\sqrt n\le 2Y/\sqrt\lambda,\qquad
 \sup_{t,x}\|h^{(L)}(t,x)\|_2/\sqrt n\le2H_D.
\]

Their product bounds the prediction by \(4YH_D/\sqrt\lambda\).
Thus the two-run distance is at most \(8YH_D/\sqrt\lambda\)
with probability at least \(1-2\rho_{\rm ref}\), where
\(\rho_{\rm ref}=2^{-20}\delta\). Since
\(2\rho_{\rm ref}=2^{-19}\delta<\delta/32=\alpha\), the quantile
is finite. Continuity of probability under decreasing radii yields
\(\Pr(\|F-F'\|_*>b)\le\alpha\), including \(b=0\).
This step uses an amplitude envelope to prove finiteness, not an analytic
upper rate as the variability benchmark.

For \(a(f)=\Pr(\|F-f\|_*>b)\), independence gives
\(\mathbb E[a(F')]\le\alpha\). The intersection estimate is

\[
 \Pr\{F'\in E_{\rm ref},\ a(F')\le2\alpha\}
 \ge1-\rho_{\rm ref}-\tfrac12
 =\tfrac12-\rho_{\rm ref}>0.
\]

A fixed realization \(f_{\rm c}\) in this intersection is therefore
available. It has both ball failure at most \(\delta/16\) and the
physical sphere/time moduli required by FC.57--FC.58. Those real moduli
depend on the shared physical bounds, not on the reference source order
\(p_{\rm ref}\), so they agree with the coefficients in the member's
external grid. The reference tail is also uniform over the sphere.

There is no additional random-center failure to add after this deterministic
selection. Nor must one later intersect the independent target with
\(E_{\rm ref}\): its ball event already includes every required valid-path
condition, since invalid paths have infinite distance from the valid center.
The center is an analysis object and introduces no stored values or
computational dependence on \(b\).

## Fixed-code transfer and exact failure budget

FC Sections 3--5 and 7 provide the needed fixed-code interface: an iid
finite source stopped at the acquired training prefix, with the reserved
passive calls appended, couples to an ordinary Gaussian dense initialization.
The local prediction error is an allocated multiple of \(Yn^{-10}\).
FC.39--FC.41 use a complete-call augmentation, and FC Section 7 explicitly
excludes future training answers and the private metric from the Gaussian
posterior filtration. FC.54--FC.55 compute actual empirical contractions.
The refinement does not strengthen this interface into a joint coupling
over external codes.

For one fixed code \(c\), the dense ball event implies that the coupled
dense scalar lies within \(b\) of \(f_{\rm c}(c)\), except with probability
\(\delta/16\). A triangle inequality enlarges this interval by
\(e_{\rm loc}\). WB Section A then transfers its scalar-transcript event
under the inner generator with loss \(1/64\).

FC Section 6 separately proves selected-metric replay after the inner
replacement. It conditions on the packet array and preceding scalar marks;
the next mark remains fresh and independent. Its argument does not assume
independence among packets and does not condition on the private metric.
The replay loss is \(2^{-12}\). Thus the five auxiliary losses used in
VD.3 match the cited construction exactly:

| Failure source | Bound |
| --- | ---: |
| Physical member source | \(2^{-20}\) |
| Raw-noise RMS | \(2^{-20}\) |
| Chronological Gaussian coupling | \(2^{-26}\) |
| Finite Gaussian sampler | \(2^{-29}\) |
| Selected-metric replay | \(2^{-12}\) |

Their sum is \(0.0002460647374391556<1/1024\). For
\(0<\delta<1/4\), the complete one-member interval-failure probability is
strictly smaller than

\[
 \frac1{64}+\frac1{64}+\frac1{1024}
 =\frac{33}{1024}<\frac1{16}.
\]

All these losses belong inside the complete member experiment and can be
amplified. They are not multiplied by the number of members as failures of
an unamplified common event.

The finite scalar alphabet permits the interval with real endpoints to be
a fixed Boolean test. WB.1 allows arbitrary deterministic within-block
computation. The test is quantified over by the generator theorem; it is
not part of the implemented decoder and does not require a center oracle.
The final transcript inventory in FC gives the claimed \(O(R^2w)\)
transcript and verifier sizes also for the appended query.

## Amplification, sphere, all times, and endpoint

For independent complete members, a bad median requires at least
\((J+1)/2\) bad members. The elementary subset union bound gives

\[
 \Pr(\text{bad median at }c)
 \le 2^J(1/16)^{J/2}
 =2^{-J}
 \le\frac{\delta}{16N_{\rm ext}}.
\]

The fixed-code bad-member counter is exactly the outer test permitted in
WB Section A. The same bound applies to the counter event that contains
median failure. Its outer-generator loss adds another
\(\delta/(16N_{\rm ext})\). The union over codes therefore costs
\(\delta/8\), even though the final generated members are dependent.
Independence is used only for the ideal complete-member experiment before
this outer transfer.

FC.59--FC.60 enumerate a deterministic finite family of sphere/time codes,
including panel labels, both boundary endpoints, and the frozen tail.
The code family is independent of \(f_{\rm c}\) and is not stored.
Every actual query returns one qualifying coded scalar value. Consequently,
the off-grid comparison requires regularity only of \(f_{\rm c}\);
no continuity or Lipschitz property of the finite decoder is used.
The deterministic error decomposition is

\[
 |f_{\rm Log,n}(t,x)-f_{\rm c}(t,x)|
 \le b+e_{\rm loc}+e_{\rm mesh}+e_{\rm tail}
 \le b+A_{\rm num}Yn^{-10}.
\]

The inherited tail bound in FC Section 8 is
\(CYH_D^2\lambda^{-1}e^{-T/2}\le Yn^{-10}/4\). It handles
arbitrarily late times and the endpoint. Either allowed panel at a boundary
is included in the code event. Since the code event is simultaneous before
a query is selected, model-dependent and adaptively selected queries
require no further union bound.

Finally, the ordinary independent target lies within \(b\) of the same
fixed center with failure at most \(\delta/16\). Hence the checked
finite-width conclusion is precisely

\[
 \Pr\!\left\{
 \|f_{\rm Log,n}-f_n^{\rm ind}\|_*
 >2b_n(\delta)+A_{\rm num}Yn^{-10}
 \right\}
 \le\frac{\delta}{8}+\frac{\delta}{16}
 =\frac{3\delta}{16}.
\]

No additional reference-source loss, whole-path coupling, or infinite-query
total-variation statement is needed.

## Numerical remainder and the eventual factor-three statement

The refinement correctly rejects the old inequality \(b_n\ge32Y/n\)
after changing \(b_n\) from an analytic certificate to an actual quantile.
For \(m=d=1\), constant activations \(\phi_j\equiv1\), and a sufficiently
small nonzero label, the uncentered feature matrix is \(Q^{(L)}=[1]\).
All hidden gradients vanish and the stated normalization gives

\[
 \dot w_i=-2(f_n-y),\qquad
 \dot f_n=-2(f_n-y),\qquad
 f_n(t)=y(1-e^{-2t}).
\]

Every Gaussian initialization gives this same trajectory, so the actual
variability quantile is zero. For a fixed retained model the finite time
codes have a finite scalar range, which cannot reproduce this nonconstant
continuous path for every time. The example therefore rules out a
zero-remainder multiplicative guarantee for this prescribed decoder over
the full admissible class. It does not assert an obstruction for every
conceivable alternative decoder.

For completeness, the eventual lower-to-quantile step can be made explicit.
Fix a problem with \(m\ge2\), \(Y>0\), and \(\gamma>0\).
Apply RESULT's actual-trajectory lower theorem at failure \(1/2\).
For all sufficiently large individual widths it gives

\[
 \Pr\{D_n\ge L_n\}\ge\tfrac12,\qquad
 L_n=c_{\phi,L,1/2}
 \frac{Y\sqrt\gamma}{\sqrt n[\log(en)]^{5/2}},
 \qquad D_n=\|f_n-\widetilde f_n\|_*.
\]

The quantile event \(\{D_n\le b_n(\delta)\}\) has probability at
least \(1-\delta/32\). Since
\(1/2+1-\delta/32>1\), these two events intersect with positive
probability, forcing \(b_n(\delta)\ge L_n\). The coefficient is
positive on the original full label allowance, using the lower theorem's
\(\chi_{\rm act}\) factor. Moreover,

\[
 \frac{L_n}{A_{\rm num}Yn^{-10}}
 =\frac{c_{\phi,L,1/2}\sqrt\gamma}{A_{\rm num}}
   \frac{n^{19/2}}{[\log(en)]^{5/2}}
 \longrightarrow\infty.
\]

Thus \(b_n(\delta)\ge A_{\rm num}Yn^{-10}\) eventually, and
the proven finite-width error bound becomes \(3b_n(\delta)\).
This argument inherits the lower theorem's unquantified sufficient width.
It does not turn the explicit finite decoder gate into an effective
factor-three gate, does not cover the constant-feature \(m=1\) case,
and does not provide a single event over all independently initialized
widths.

## Resources and minor integration clarifications

The replacement changes only the interval in the proof tests and the
probability budget. The implementation orders and confidence margins remain
within FC.26, FC.47, FC.60 and WB.16. WB.14--WB.17 therefore retain the
stated storage and work exponents. There is no hidden cost depending on the
unknown quantile or center. The small-label branch must retain both its
enlarged orders and FC.62, as the candidate states; the exact zero-label
branch is separate.

The universal-\(\alpha_0\) alternative also has the advertised confidence
\(1-2\alpha_0-\delta/8\). For \(\alpha_0\le1/128\), its
one-member ball failure is at most \(1/64\), so the same amplification
margin applies. It cannot yield arbitrary \(1-\delta\) at a fixed
positive target-ball failure.

Two clarifications would improve the later paper integration without
changing the proof:

1. At the first definition of \(\gamma\), call \(Q^{(L)}\) the
   **uncentered** feature second-moment matrix, or give its formula.
   This makes the admissible constant-feature example immediately
   consistent with \(\gamma=1\); a centered covariance would vanish.
2. Include the two-event intersection above when stating the eventual
   factor-three corollary, and keep its unquantified width visibly separate
   from the explicit decoder gate.

The candidate already states the essential distinctions. In particular,
the old analytic upper certificate must receive a different symbol wherever
it is retained for accuracy inversion; the present audit does not approve
silently relabeling its mesh lower bound as an actual-variability property.

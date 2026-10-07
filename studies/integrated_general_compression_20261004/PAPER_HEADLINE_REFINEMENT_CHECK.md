# Internal check of the joint working-paper headline

Date: 2026-10-07. This is a scoped internal consistency check, not an
independent promotion review. The checked inputs are `paper/main.tex`,
`paper/results.tex`, `paper/methods.tex`, `paper/costs.tex`, the relevant
statements and proofs in this study's `RESULT.md`, and the complete
`VARIABILITY_DECODER_REFINEMENT.md`. No other study or archive was read.
The canonical-notation instructions and neural-network reference were
applied, together with the rigorous-mathematics checking guidance.

## Verdict and scope

No blocking error was found in the headline's parameter exponents, label
normalization, model inventories, or fixed-quantile probability convention.
The statement is an eventual theorem for each fixed admissible problem,
with a separately qualified independent-reference decoder. It is not a
uniform theorem for parameters growing with width and not an optimality
theorem. Two presentation qualifications are recommended below.

This check verifies the new headline against the existing sufficient
certificates and the proposed decoder refinement. It does not repeat the
underlying source-theorem proofs or independently re-audit the finite
generator backend. The proposed refinement remains a scoped author result.

## Parameter and label calculation

Write \(r=m/\gamma\) and \(\ell_n=\log(en)\) in this check only. The
main theorem explicitly assumes \(r\ge1\), so replacing \(1+r\) by
\(Cr\) is valid without concealing a gap-dependent constant. Its fixed
small-label cap gives \(Y\le1\) after the activation/depth constant is
chosen sufficiently small. All final errors in the new main text are
absolute errors; the common benchmark is not divided by \(Y\).

For Legendre, `(Legendre forward)` gives

\[
\|f_{\rm Leg,n,q}-f_n\|_*
\le CYr^6q^{-2}\sqrt{\ell_n\log(eq)}\,e^{\sqrt{\ell_n}}.
\]

The prescribed sufficient order
\(q=\lceil Cr^3n^{1/4}\ell_n^2e^{\sqrt{\ell_n}/2}\rceil\)
has \(\log(eq)\le C\ell_n\) eventually for each fixed problem.
Substitution gives \(CY/(\sqrt n\ell_n^3)\). The exact moving
inventory, `(Legendre-storage)`, is
\(n(d+1)+1+2(L-1)mnq\). Consequently the headline moving envelope
\(Cmr^3n^{5/4}\ell_n^2e^{\sqrt{\ell_n}/2}\) is valid eventually.
The omitted \(nd\) term is absorbed by a width threshold depending on
the fixed data even when \(m<d\). The fixed inventory remains
\((L-1)n^2\), and ordinary training data remain additional.
The cubic gap factor and outer response-memory multiplicity \(m\)
have both been retained. No factor of \(\sqrt Y\) belongs in this
label-scaled target calculation.

For Harmonic, use the target \(\varepsilon=Y/n\) in `(Harmonic
inverse)` and `(Harmonic inverse storage)`, or equivalently use the exact
integer inverse. The unshortened inverse logarithm is

\[
\log(en)+\log\bigl(e+Cr(1+\sqrt r)n\bigr),
\]

which is \(O(\ell_n)\) eventually at fixed structural parameters,
without introducing \(\log(1/Y)\). The displayed sufficient count is

\[
C(m+d)^2+(C/d)^{d+1}r^4\ell_n^{3d+2}.
\]

This follows by enlarging the exact factor \((Yr)^4\) to \(r^4\)
using \(Y\le1\); it does not spend the label cap to cancel powers of
\(r\). The exponent is \(d+(2d+2)=3d+2\). The inventory in
`(Harmonic all retained inventory)` includes metrics, data, caches and
initial copies; no discarded source array or setup trajectory is counted
as retained. The full-width branch and source overheads are absorbed into
the eventual threshold.

For Logarithmic, `(Logarithmic retained words)` is

\[
Cp^2(m+d+2)^2(1+r)^2Z^6
[d+1+\log(e+(d+1)Z)],
\]

with activation/depth factors absorbed in \(C\). The implemented
\(p\le C\log(em)\), and the explicit width gates give
\(Z\le C\ell_n\). Since this construction additionally assumes
\(m\ge d\) and the joint headline assumes \(m\ge2\),
\((m+d+2)^2\le9m^2\). Also
\(1+r\le2r\) and

\[
d+1+\log(e+(d+1)Z)
\le C[d+\log\log(e^e+n)].
\]

This proves the headline's quadratic sample and inverse-gap factors,
sixth logarithmic word power, and displayed dimension dependence. Word
length is at most \(C\ell_n\); counting bits adds one logarithmic
power. Fixed \(Y>0\) makes the clean gate \(nY\ge1\) eventual.
Below that gate the enlarged \(Z_Y\) recipe is necessary, so these
clean counts must not be read as uniform for arbitrarily vanishing labels.
The headline does not make that claim.

## Quantile and confidence

The main benchmark is the deterministic \(0.9999\)-quantile of the
actual dense-pair trajectory discrepancy. Assigning \(+\infty\) when
a trajectory lacks its required fitted limit preserves the unconditional
law. The regular dense event makes the quantile finite at the qualifying
width; right continuity gives the claimed probability at the quantile
itself, including a possible zero quantile.

The fixed-quantile variant in `VARIABILITY_DECODER_REFINEMENT.md` applies
with pair tail \(\alpha_0=10^{-4}\). Its regular-center selection gives
target-ball failure at most \(2\alpha_0\). With the existing decoder
allocation \(\delta=0.01\), simultaneous code amplification costs at
most \(\delta/8\). Thus the total failure is at most

\[
2\cdot10^{-4}+0.01/8=0.00145<0.01.
\]

This supports the main \(99\%\) confidence without computing the
quantile or changing its level with width. The main theorem says that
each construction has this guarantee; it does not currently assert a
single joint success event for all independently executed constructions.

The proposed decoder comparison is
\(2b_n+C_{\rm num}Yn^{-10}\). For \(m\ge2\), the existing
actual-trajectory lower theorem gives eventually

\[
b_n\ge cY\sqrt\gamma/(\sqrt n\ell_n^{5/2}).
\]

This absorbs the numerical term at a finite fixed-problem threshold and
yields \(3b_n\). The threshold is unquantified because the lower
theorem's onset is unquantified. The manuscript distinguishes this from
the explicit gate for the additive theorem and preserves the one-sample
exception. The dense upper quantile bound follows by running the original
arbitrary-confidence upper theorem at the fixed numerical failure level
needed by the quantile; \((1+r)^5\le32r^5\) justifies its simplified
coefficient.

Legendre's comparison to the lower quantile is bounded by
\(C/(\sqrt\gamma\sqrt{\ell_n})\), and Harmonic's by
\(C\ell_n^{5/2}/(\sqrt\gamma\sqrt n)\). Both vanish for the fixed
problem. The stronger random-denominator convergence uses the source's
arbitrary-confidence lower theorem, not only one fixed \(99\%\) event.
The manuscript correctly refrains from asserting that stronger claim for
the independent decoder.

## Costs and qualifications

The Legendre runtime substitutions retain the outer \(m\) in training
work. Harmonic's \(m^3\) Gram solve is covered by \(mS_{\rm H}\)
because \(S_{\rm H}\ge Cm^2\). Query work uses the refreshed readout
cache. The neural query-workspace column is additional memory; the
decoder's inventory bounds total live query memory. These distinctions
agree with the source's execution contract.

For Harmonic's target \(Y/n\), the exact inverse has source horizon
\(T=O(\ell_n)\) and \(\log(1/\eta)=O(\ell_n)\). Substitution
into the full source-mode, quadrature and local-degree recipes preserves
the fixed-problem orders used by `(Setup-B.10)` and `(Setup-I.33)`.
The explicit near-quadratic and implicit near-linear setup exponents
therefore remain valid for this strengthened target. The original
\(\eta=1/n\) special-case table alone would not have justified that
substitution; the full recipes do. Activation and Gaussian sampling
qualifications are retained in the revised costs text.

Two presentation points were sent to the lead author:

1. The phrase “With \(n\ge\max(m,d)\)” in the cost introduction
   should explicitly retain the theorem's eventual threshold. That simple
   inequality alone does not absorb \(nd\) into the displayed Legendre
   moving envelope when \(d\) is large relative to \(m\).
2. “Optimized” refers to sufficient prescribed choices, not proved
   minimal orders. In particular the extra Legendre logarithmic factor
   was selected to give negligible relative error, stronger than the
   common constant-factor contract. “Prescribed” would remove the
   possible ambiguity. The manuscript already disclaims optimality
   against other compression schemes.

The proposed renaming of the old analytic decoder certificate from
\(b_n\) to \(B_n\) is necessary. Local continuation radii with the
same old letter are separate quantities and should not be changed by a
global replacement. Integration of that rename and full-paper compilation
remain with the lead author; neither was performed by this check.

## Checked snapshot

SHA-256 values recorded during the check, before any subsequent lead-author
polish:

| File | SHA-256 |
| --- | --- |
| `paper/main.tex` | `a7c09bbbfaa5214520f1c9316ec61536f5e74b6b1685de9e2c7c0316cf8a00f8` |
| `paper/results.tex` | `4a272081f93e8df70c0e658beb909e63ef06edb92c4507992da1152caf53586f` |
| `paper/methods.tex` | `9eeec414767eaa02c454530be5e8d42ba6b64cb7576dbaee01f973b5097de7af` |
| `paper/costs.tex` | `c06f6dd3f2aaad50ed2a4aaaf6f1821887675008e35a3f0895b83060fb79f3ab` |
| `VARIABILITY_DECODER_REFINEMENT.md` | `783ce30306b7db97429ff0d6d0b2d044b682ae921d043215195527ccda453224` |

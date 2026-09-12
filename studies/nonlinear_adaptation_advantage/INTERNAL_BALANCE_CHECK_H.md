# Internal balance check H

Reviewer: scoped harmonic-route agent, 2026-09-12.

**Verdict: PASS for the stated exact identities and expressly conditional
calculus statements. No corrective finding.** The follow-up does not establish
a favorable actual-neural sign or a positive E₀ margin, and accurately retains
those gaps.

This is the requested final internal check, not independent promotion review.
The harmonic candidate was frozen before authorized cross-exposure. I already
checked the frozen geometry report and the comparison-transfer note. The
present task introduced only GEOMETRY_SIGN_FOLLOWUP.md; no other study or
route was read, no input was edited, and no new proof search or experiment
was conducted.

## 1. Read coverage and versions

GEOMETRY_SIGN_FOLLOWUP.md, lines 1–351, was read completely in one untruncated output,
including its status, provenance and B1–B17. Its SHA-256 matched the assigned
version before and after the check:

7400b12eb9655a24f8ba23af2fd41b60733947ca5fc184850d2629eafd980719

The already completely read ROUTE_GEOMETRY.md remains at:

e452735f683a6f8c3e4e895949dbd8aa912f470bbdeb475bf676bce4a10b9c04

The prior permitted source coverage remains exactly that recorded in
INTERNAL_CROSSCHECK_H.md: the complete notation contract; global_nonlinear
A.1–A.4, C.4.5.1 §§1–3 and §5, C.4.5.2 §§1–4, C.4.9 model/source unit A
and supplement/unit B through B.4, and C.4.10 completely; special_data_limits
III.F completely; the neutral contract, workflow and required skills/references.
No additional scientific sections were fetched. Their relevant file hashes
were rechecked:

| Source | SHA-256 |
|---|---|
| RESEARCH_CONTRACT.md | 0bbd681da93a44574fbe30d9ee7fd5a984105d363c473c7756f31964c2896c0f |
| docs/global_nonlinear.md | 5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483 |
| docs/special_data_limits.md | 5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489 |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| RESEARCH_WORKFLOW.md | 8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12 |

## 2. Projection and readout acceleration: PASS

Use the follow-up's real raw metric and write $C=GM^{-1}$ temporarily,
to distinguish this rectangular operator from its scalar anchor contrast.
For a fixed residual, $v=b+G\beta$, $b=\Pi v$, and

\[
\partial_b\Pi=-\Pi(\partial_bG)C^*
                         -C(\partial_bG)^*\Pi.
\]

Because $C^*v=\beta$ and $(\partial_bG)^*b=h_A(b,b)$, this gives

\[
\partial_b(\Pi v)
=-C h_A(b,b)+
 \Pi\left(\int r\,(\partial_bg_u)p\,d\rho
                       -(\partial_bG)\beta\right)
=-C h_A(b,b)+\Pi H_\mu b.
\]

This reconstructs B8, including its normal term and sign. The vector
$H_\mu b$ is legitimate as the strong directional derivative of the raw
gradient in the admissible direction $b$; no bounded ambient Hessian on
all raw L² directions is required. The source L⁴ row/query bounds and
bounded readout justify the directional derivative used here.

The actual residual also changes. Its contribution is
$D r'=-2DKr$, while the state contribution is $-2\partial_b(\Pi v)$.
Thus

\[
b'=-2DKr-2\Pi H_\mu b+2C h_A(b,b),
\]

and $\theta''=-2b'$ gives precisely B9.

Readout linearity gives $G^*e_c=y$, and
$H_\mu[b,e_c]=\langle c,J_\mu b_h\rangle=\|b_h\|^2$.
With $n=Cy=GM^{-1}y$ and $a=e_c-n$,
the readout norm satisfies

\[
(\|c\|^2)''
=8\|b_c\|^2+2\langle e_c,\theta''\rangle
=8\{\|b\|^2+\langle e_c,DKr\rangle
              -H_\mu[b,n]-y^TM^{-1}h_A(b,b)\}.
\]

In the pure swap-symmetric diagnostic, $DKr$ is in the negative
raw symmetry sector and $e_c$ is fixed by the isometry, so the cross term
vanishes. This verifies B10 and its stated general-residual correction.
The first norm derivative vanishes by the same sector orthogonality.

For B11, symmetry gives
$M=\left(\begin{smallmatrix}m&d\\d&m\end{smallmatrix}\right)$.
With $y=(1,-1)$ and $g_B=Gy/2$,

\[
B_s=\|g_B\|^2=(m-d)/2,\quad My=2B_sy,\quad
n=g_B/B_s,
\]
\[
y^TM^{-1}h_A=(h_{A,1}-h_{A,2})/(2B_s)=H_B[b,b]/B_s.
\]

All factors of two in B11 therefore check. The positive reference
$B_s$ controls only the denominator. Neither remaining contraction is a
squared norm or removed by this symmetry.

B3–B4 independently agree: differentiating $c'=-2h_\mu$ gives
$c''=4J_\mu J_\mu^*c-2h_{\mu'}$, and inserting
$r'=-2Kr$ and fitted anchor values gives B4's two terms.
The signed spatial density and anchor coefficients are differentiable in
total variation because their prediction/gradient derivatives are continuous
uniformly in input on this compact episode. This is not a claim of
total-variation differentiability of moving joint label distributions.

## 3. Trace/nuclear legitimacy and saturation balances: PASS

There is enough regularity for B12; the middle initialized action itself is
never assigned a Hilbert–Schmidt norm. The underlying trace facts can be
checked directly from rank sums, as follows.

For $T=\sum_j a_j\otimes b_j$ with
$\sum_j\|a_j\|\|b_j\|<\infty$, the series converges in the nuclear norm
defined by the infimum of such sums. This space is complete: a nuclear-Cauchy
sequence has a subsequence with summable successive differences, and choosing
summable rank representations for those differences constructs its limit.
The continuous inclusion into Hilbert–Schmidt operators follows from the
triangle inequality and $\|a\otimes b\|_{HS}=\|a\|\|b\|$.

For a bounded operator $B$ between the same two layer spaces,

\[
\operatorname{Tr}(B^*T)=\sum_j\langle a_j,Bb_j\rangle,\qquad
|\operatorname{Tr}(B^*T)|\le\|B\|\sum_j\|a_j\|\|b_j\|.
\]

This is independent of representation: expanding in any orthonormal basis
of the input space and applying Cauchy–Schwarz gives an absolutely summable
double series and the same displayed value. Taking the infimum gives
continuity in nuclear norm. A rank-one operator has nuclear norm exactly
$\|a\|\|b\|$: its one-term representation gives the upper bound, and pairing
with the norm-one rank operator carrying the normalized $b$ to the normalized
$a$ gives the reverse bound. Rank subtraction has the corresponding
two-factor difference bound.

Each reached middle velocity is a finite-variation integral of these ranks.
Their factors are strongly L²-continuous; hence they are continuous in nuclear
norm by that subtraction bound, and are Bochner integrable in the complete
nuclear space. The resulting integral agrees with the already established
Hilbert–Schmidt state because the inclusion is continuous.
For an explicit finite bound, reference feature time satisfies
$s_\dagger\le10$, $\|c(s)\|_2\le s$, and total reference control mass per unit
feature time equals one. Thus

\[
\|K_\dagger\|_{\rm nuc}\le\int_0^{s_\dagger}s\,ds\le50.
\]

On the selected episode, $\|c\|_2\le c_b$ and control density is at most
$A_s$, so $\|K(\tau)-K_\dagger\|_{\rm nuc}\le c_bA_s\tau$.
Continuous controls and rank factors make this curve strongly differentiable
in nuclear norm. Consequently

\[
\frac d{d\tau}
\{\|K\|_{HS}^2+2\operatorname{Tr}(A_0^*K)\}
=2\operatorname{Tr}((A_0+K)^*K')
\]

is legitimate. This is a finite renormalized increment, not subtraction of
two separately finite population action norms.

For the actual rank velocity,
$\operatorname{Tr}(A^*(\delta\otimes H^1))=\langle\delta,AH^1\rangle$.
Inserting $K'=-2\int\delta\otimes H^1\,d\mu$ therefore gives
$\mathcal A'=-4\int\langle c\phi'(Z^2),Z^2\rangle\,d\mu$.
Subtracting this from $(\|c\|^2)'$ yields B13.
Using the actual adjoint rewrites the same middle derivative as
$-4\int\langle Q,\phi(w\cdot u)\rangle\,d\mu$.
Subtracting $(\|w\|^2)'=-4\int\langle Q,(w\cdot u)\phi'(w\cdot u)\rangle
\,d\mu$ yields B14, with the stated sign.

The scalar defect has
$\chi'=-z\phi''=2z\tanh z\,\operatorname{sech}^2z\ge0$.
Oddness and its limits at infinity give $z\chi(z)\ge0$ and $|\chi|\le1$.
Bounded $\chi$, L² backward/readout fields and finite control variation make
both integrals well defined. Their multipliers are not the corresponding
preactivations, and their control measure is signed. The follow-up correctly
draws no sign conclusion from pointwise saturation.

## 4. Conditional higher derivatives B15–B16: PASS

Here $K,H,J$ denote $K_0,K'_0,K''_0$ in prediction space; the residual
argument in the contractions is the fixed initial $r$. Assuming the additional
derivatives exist with the differentiability needed for the displayed product
rules, direct calculation gives

\[
E'=-4\langle r,Kr\rangle,\qquad
E''=16\langle r,K^2r\rangle-4\langle r,Hr\rangle,
\]
\[
E'''=-64\langle r,K^3r\rangle
             +48\langle r,KHr\rangle-4\langle r,Jr\rangle.
\]

The two sources of the mixed coefficient are 32 from differentiating $K^2$
and 16 from the changing residual in the second term. For real self-adjoint
$K,H$, $\langle r,HKr\rangle=\langle r,KHr\rangle$. Subtracting this from
the frozen derivative gives B15's $-48$ and $+4$.

In the pure symmetric diagnostic, equivariance differentiated in the
negative raw velocity direction makes $H$ interchange the two prediction
symmetry sectors, while $K$ preserves them. Hence $\langle r,KHr\rangle=0$.
If $D''_0$ also exists, differentiating $K=D^*D$ twice, with the argument
$r$ held fixed, gives

\[
\langle r,Jr\rangle
=2\|D'_0r\|^2+2\langle D_0r,D''_0r\rangle.
\]

Multiplication by 4 proves B16's coefficient 8. Its second contraction is
the same order as its positive square. The input expressly does not claim
$K''_0$, $D''_0$, an evaluated next-order remainder, or a sign for the actual
population path. These are conditional algebra checks only.

## 5. Outcome and limitations

| Checked component | Verdict |
|---|---|
| B8 projection derivative and B9 acceleration | PASS |
| B10 readout norm and general-residual correction | PASS |
| B11 reference Gram factor and balance | PASS |
| B12 nuclear/trace construction | PASS on the reached curves |
| B13–B14 exact saturation balances | PASS |
| B15–B16 coefficients and conditional status | PASS |
| Actual favorable next-order or ordinary-family sign | OPEN; not proved |
| E₀ positive risk and relative-component advantage | OPEN; not proved |

The check confirms that the potentially favorable square cannot be isolated
from its same-order signed terms. This validates the scope of the follow-up's
negative conclusion about those particular arguments. It is not a neural
counterexample, a general impossibility statement, or a reason to mark E₀
complete. No repair was requested.

Checks consisted of full reading and the direct algebraic, integral and
rank-series reconstructions above. No numerical or symbolic package, theorem
prover, training run or new external scientific source was used.

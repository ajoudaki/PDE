# Bounded check of the two-gap composition

2026-10-07. Assembly review of the supplied component statements and the
frozen synthesis. This is not a fresh reconstruction of every theorem
imported by those components and is not a promotion review.

**Verdict: PASS for the new composition at its stated component theorem
boundaries.** The revised synthesis resolves the initial probability
allocation ambiguity. The supplied cost file now gives a checked
parameter-explicit internal table, with external interfaces and the
small-label numerical branch retained. This is a bounded assembly check,
not an independent reconstruction of all inherited component proofs.

## Inputs and scope

The initial frozen synthesis was `TWO_GAP_CLOSURE_RESULT.md`, SHA-256
`309c7bb039ad0fa379b18ea0fbeb5139347959302380ff8c6ab5d14eb31f1125`.
The final revised synthesis was read completely and verified at SHA-256
`2f4582ea734165028a67968feb16cc8300dfea64ac71e29f6171f9c9869feb39`.
The intermediate revision
`a91de9f8b478f244f7e9c10c2e454a2ae1e372fd4fa21fa7be0133f8578421bb`
was also read; the last changes specify the finite Gaussian RMS gate,
the tiny-label logarithm decomposition, and the location of the definition
of \(Z\).
The proof inputs read were:

| Input | SHA-256 |
| --- | --- |
| `FULL_FINITE_SOURCE_PROBABILITY.md`, complete | `6ecf89142925ef831b7efbf12ad84eacdfef3dc97f3c5b749bc7547311f9695a` |
| `SOURCE_SEED_EXACT_QUERY.md`, complete | `3a6c5a35bff72af9e5d6ae3dfdcc4258db6e84290e14845f589ece6550e35e39` |
| `NUMERICAL_BENCHMARK_ABSORPTION.md`, Section 5 | `889eccba6d9966e9791ee90802a87318ca044717a02f0cf953fb11ef84809d4b` |
| `GAP_REFINED_PHASE_COSTS.md`, complete | `817617951efb926d2729cd7f20eaccf7cb5c4e25e17eb531502c8b2618e017bc` |
| `FAST_PHYSICAL_QUERY_GRID.md`, complete | `bd275d6163f54e0668d55be576c789bdeedae2e447a3dffe0881c4cc7defaa0a` |
| `POLYNOMIAL_SOURCE_WIDTH.md`, scientific Sections 1--6 | `4821875988b8f7f493e776e9147da09ac27a547125d29eea0e84b98e8559e916` |
| Specifically authorized `studies/integrated_general_compression_20261004/GENERAL_DENSE_COMPARISON.md`, Sections 1--2 and 5 | `ab97a860d7a6e175905a6848a9126ca8a194e08f52764738e94dcde2675100a9` |
| `CLOSURE_COMPOSITION_COSTS.md`, complete initial body and revised Section 6 | `2abd031ffc3f1548fd8cd92b0bc6e3594463327db09321104fb2110953ee44b0` |

The initial complete cost file had hash
`7b4e0893b84e7b691c1457f157a203fc03be2a6c1009e4cf4fb03f687d1f5351`;
the final revision explicitly enumerates its finite-source gates.
The supervisor expanded the original packet to include
`POLYNOMIAL_SOURCE_WIDTH.md` and the specified integrated comparison
sections solely to check the dense-center event and all-time carrier
condition. No further links were followed. Required rigorous-proof
and canonical-notation instructions, including the neural-network reference,
were read. The study README, history, and component review files were not
read. An agent-status metadata request incidentally displayed a completed
component reviewer's short PASS summary after the component checks here
had already been performed. That text supplied no mathematical input to
this review, but strict isolation from all prior verdict text was therefore
imperfect and must not be represented otherwise.

## Source width and common physical model

Write \(\lambda=\gamma/m\), \(\delta_0=\delta/256\), and
\(\rho=2^{-20}\delta\), and use the synthesis's resource logarithm
\[
 Z=\log(en)+\log\left(e+
 \frac{(m+d+2)\beta^{100L}(1+m/\gamma)}\delta\right).
\]
Substitution of \(\rho\) into the supplied
finite-source theorem gives exactly the revised synthesis's values

\[
 p=\max\!\left\{1,\left\lceil
 \frac{\log(2^{22}emL/\delta)}{\log(64e^2)}\right\rceil\right\},
 \qquad
 n\ge\left\lceil\left[
 \frac{2^{20}\beta^{2000L}}\delta
 (1+\lambda^{-1})^4(m+d+p+1)^4
 \right]^{20000}\right\rceil.
\]

No inverse label scale occurs. Its model, normalization, zero initial
readout, original Gaussian physical law, optimizer, width, and complete
fitting/source label intersection agree with the exact-query component.
The finite implementation approximates that physical law through the
stated coupling; its short seeds do not literally encode continuous
Gaussian matrices. The comparison target remains an independently
initialized dense model at this same width.

The complex source result is needed only for the finite training set.
Whole-sphere real feature/operator bounds and the fitted endpoint come
from fitting and its real tail. This suffices both for real passive
queries and for the physical input/time grid. No whole-sphere complex
source, label-dependent test information, or replay of scalar training
is introduced by this composition.

## Dense-center probability condition

The old center theorem's unspecified good-event width cannot simply be
ignored. It can be discharged using the supplied explicit statements.
The new source event contains all-time fitting, residual decay, Gram,
operator and RMS bounds, together with training-carrier bounds through
\(T_n=32\log(en)/\lambda\). The carrier-tail implication in
`POLYNOMIAL_SOURCE_WIDTH.md` (29)--(30) gives the required all-time cap
\(2K_{\rm src}S\sqrt{\log(en)}\), where \(S=16Y/\lambda\), provided

\[
 n\ge\max\left\{1,
 \left[\frac{C_{\rm tail}}{8K_{\rm src}\sqrt{1/\lambda}}\right]^{1/15}
 \right\}.
\]

Here \(C_{\rm tail}\le\beta^{20L}\), \(K_{\rm src}\ge1\), and
\(\lambda\le\beta^{6L}\), so the bracket is at most
\(\beta^{23L}/8\). This gate is dominated by the displayed source
width. The numerical horizon gate
\(n\ge\max\{1,e^{-1}\sqrt{1+66\beta^{100L}/\lambda}\}\)
is also dominated by it. There is no inverse \(Y\) in either gate.

`GENERAL_DENSE_COMPARISON.md` (8)--(10) explicitly derives the
label-refined Lipschitz estimate deterministically for two actual
trajectories satisfying precisely these physical bounds. To recall its
population and fitting constants, with a real standard Gaussian \(g\),
\[
 q_0=1,\qquad q_j=\mathbb E\phi_j(\sqrt{q_{j-1}}g)^2,\qquad
 H=\max(1,\sqrt{q_1},\ldots,\sqrt{q_L}),
\]
\[
 s=\max\{1,\max_j\sup_{|\operatorname{Im}z|\le a/2}|\phi'_j(z)|\},\qquad
 B=9s,\qquad
 F_{\rm dense}=s^2\left[B^{2L-2}+4H^2\sum_{j=0}^{L-2}B^{2j}\right].
\]
These are the same supplied fitting constants. The \(Y\le1\)
condition requires no smaller label cap:
\(F_{\rm dense}\ge4s^2H^2\) and \(\lambda\le H^2\), so the
original fitting allowance gives \(Y\le1/(16s)\le1/16\).
The same scalar McShane extension and Gaussian concentration can
therefore be run on the new explicitly probable good set. Its original
leading structural coefficients need not be replaced by the different
explicit fallback coefficient. Training-carrier bounds suffice; no
carrier bound for complex unseen queries enters that argument.

The revised allocation satisfies \(\rho<\delta_0/4\), as requested
by the original standalone comparison at confidence \(\delta_0\).
It also pays for the independent reference's good event without borrowing
confidence from its Gaussian deviation allowance. One sufficient final
allocation is at most \(\delta/4\) for all coded ensemble medians
and at most \(\rho+\delta_0\) for the independent reference's
physical good event and Gaussian deviation. Their sum is below
\(\delta\). Each fixed-query member has scientific failure at most
\(\rho\), followed by the stated fixed small numerical, replay and
generator allocations; its bad-output probability stays below \(1/16\).
The earlier draft applied the source theorem only at \(\delta_0\),
which did not literally meet the standalone theorem's \(\delta_0/4\)
share. The revised \(2^{-20}\delta\) call resolves that ambiguity.

## Ensemble, uniformity and numerical absorption

The exact-query component appends current empirical contractions and
the complete two-orientation covariance correction to each finite source.
Thus its former passive population approximation is never made, and
there is no statistical passive remainder to absorb afterward. The
source and query share a precision schedule selected before acquisition.
Refining query arithmetic alone would not establish the stated coupling.

The inner generator provides a separate marginal guarantee for each
finite external code. The outer generator amplifies complete source
experiments, including their source failures. For independent member
experiments with bad probability at most \(1/16\), the bad-majority
bound is \(2^J(1/16)^{J/2}=2^{-J}\). Taking an odd
\(J\ge C\log(16N_{\rm ext}/\delta)\) and outer generator error
\(\delta/(16N_{\rm ext})\) makes a union over all codes valid.
No independence of the generated members or repeated passive queries
from one common source is presumed. The physical reference modulus
then transfers the coded statement to arbitrary sphere inputs and
times; the frozen tail includes the fitted endpoint.

For the declared mesh coefficient, Section 5 of the numerical lemma gives

\[
 c_{2,\rm mesh}=\frac{32H^2}{\lambda}
 +\frac{32F_{\rm dense}Y^2}{\lambda^2}
 +\frac{4B^L}{\sqrt\lambda},\qquad
 32\le c_{2,\rm mesh}\le C\beta^{4L}(1+\lambda^{-1}).
\]

The lower bound uses \(\lambda\le q_L\le H^2\). The upper bound
uses the unchanged fitting cap, \(H\le\beta^{2L}\), and
\(B^L\le\beta^{2L}\), as derived there. With the original leading
coefficient and exponential factor retained, the chosen certificate
therefore satisfies \(b_n\ge32Y/n\). Consequently

\[
 2b_n+A_{\rm num}Yn^{-10}\le3b_n
 \quad\text{when}\quad
 n^9\ge A_{\rm num}/32.
\]

This uses no lower bound for the unspecified leading coefficient and no
eventual exponential dominance. It is a declared instantiation of an
unfixed mesh coefficient, not equality to an arbitrary smaller coefficient
previously fixed numerically. At \(Y=0\), the exact zero branch requires
neither normalization nor absorption.

## Cost composition

The modular cost equations in `SOURCE_SEED_EXACT_QUERY.md` give, at
fixed positive label scale and other fixed problem parameters,
\(R=O(Z^{5/2})\), word bits \(O(Z)\), \(J=O(Z)\), inner block
size \(O(Z^6)\), and member-input size \(O(Z^7)\). Substitution
does give the stated \(O(Z^7\log(e+Z))\) retained and peak
training/query bits and the three stated fixed-parameter work exponents.
The source moment order and the modular word length are different
quantities, both named \(p\) in their separate components; they must
remain distinguished in the combined table. Multiplication of the source
field count by the moment order yields its stated powers two in memory,
five in setup/training and four in query work.

The cost file distinguishes moment order \(p\) from word bits \(w\).
Its dimensionless patch recurrence permits \(H=pH_0\),
\(K=K_0+\lceil\log_2p\rceil\), and only \(O(\log p)\)
additional word precision. Here \(H\) is the cost file's patch count,
distinct from the population moment bound used in the preceding checks;
\(K\) is its Taylor degree. In particular shrinking the physical radius
does not require storing \(h^{-K}\)-scaled Taylor derivatives or
multiplying the real stability exponent by \(p\). These conclusions
follow from the local recurrence and propagation inequality explicitly
supplied in its Section 2; their deeper implementation lemmas remain
component inputs to this review.

For the full substitution, let \(D=m+d+2\), \(G=1+m/\gamma\),
\(c=d+1\), and \(\Lambda=\log(e+cZ)\). The resulting retained
and peak training/query memory is

\[
 M_*=Cp^2\beta^{512L}D^2G^2Z^7(c+\Lambda).
\]

The two summands account separately for all ensemble states and the
outer seed. The leading setup and training monomials are
\(JnR^5w^3\) and \(JR^5w^2\), giving exactly the table's
activation exponents \(1335L\), \(1225L\) and logarithmic powers
\(33/2\), \(31/2\). The query row-generator term
\(JnR^4w^2E\) gives \(1024L\) and power \(14\), with the
additional outer-generation term \(Cc p^4\beta^{1024L}D^4G^4
Z^{15}\Lambda\). The inequality \(\Lambda\le CD\sqrt Z\)
absorbs the latter into the setup and training envelopes using their
spare parameter powers. All remaining displayed modular monomials are
bounded by the stated phase envelopes without assuming \(w\le R\).

Peak initialization correctly adds
\(C(np\beta^{311L}DGZ^{7/2}+p^3\beta^{713L}D^3G^3Z^{17/2})\)
to \(M_*\), without multiplying the temporary dense table by the
ensemble size. Equation (17) separately counts regenerated-row
activation calls, and (19) charges evaluator, data, scale, certificate,
query/time acquisition and output interfaces. These costs can dominate
the internal table. The old sixth-power bit table does not apply.
Query work still contains a factor \(n\), and no training-time
speedup follows.

The supervisor supplied the remaining finite-bridge failure term as
source failure plus \(C(R+L)e^{-c_gn}\) plus the allocated finite
precision error, where \(c_g>0\) and \(C\) are universal. This
is a new explicit component boundary, not a claim that this reviewer
read an otherwise unassigned bridge proof. The numerical term has the
sufficient gate

\[
 n\ge C\left[\frac{p\beta^{201L}DG}{\rho}\right]^2.
\]

Indeed, writing the bracket as \(B_{\rm num}\), this gives
\(Z\le C\log(en)\) and
\((R+L)/\rho\le C\sqrt n\log^{5/2}(en)\). Multiplication
by \(e^{-c_gn}\) is at most one after a universal enlargement of the
gate constant. The other finite sampler, one-call total-variation and
scalar rounding-boundary failures are paid by their pre-setup precision
allocations. They do not introduce an unspecified asymptotic width
condition. Also \(B_{\rm num}\le S_{\rm src}\), with
\(S_{\rm src}\) defined below, since \(Dp\le Q^2\). Thus the
scientific gate dominates up to a universal factor. If the literal
numerical value of that factor is not instantiated, retaining the
displayed additional gate is the precise assertion.

The quadratic internal-work gate also checks. Put
\(P=\beta^{1335L}D^5G^5cp^5/\delta\). Under \(n\ge P^2\),
the parameter prefactor is at most \(\sqrt n\) and
\(Z\le2\log(en)\); the finite maximum of
\((1+t)^{33/2}e^{-t/2}\), \(t\ge0\), then gives \(Cn^2\)
bit operations for one setup, all training, and one query. With
\(Q=D+p-1\) and \(S_{\rm src}=\beta^{2000L}G^4Q^4/\rho\),
the inequalities \(D,c,p\le Q\) give \(P\le S_{\rm src}^3\).
Thus the scientific width \(n\ge S_{\rm src}^{20000}\) dominates
this gate. This is an upper bound with a universal constant, not a
coefficient-one comparison to a dense implementation, a statement about
arbitrarily many queries, or an upper bound on arbitrary external costs.

The unchanged word table is a numerical branch requiring \(nY\ge1\).
For smaller positive labels,
\(\log_+(1/Y)\le\log n+\log_+(1/(nY))\); hence the latter is
the additional logarithmic precision beyond a baseline already paying
\(\log n\). It can also require the supplied patch/degree refinement.
It must be propagated through the costs, not described as a free removal
of the numerical gate. This does not alter the source theorem's absence
of an inverse-label width condition.

No experiment, Git operation, promotion, or write outside this report
was performed.

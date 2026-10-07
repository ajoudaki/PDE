# Finite-confidence radius and exact-query ensemble costs

2026-10-07. Scoped author composition and cost check. This is conditional
on the scientific source interface stated in
`FULL_FINITE_SOURCE_PROBABILITY.md`, and on the physical, finite-source,
metric-replay and exact-query interfaces identified below. It does not
independently validate the probability theorem or the final dense-error
comparison. No experiment, Git operation or promotion is involved.

The radius division by the confidence moment order costs one such factor
in the source field-count envelope, up to a universal constant, and only
its logarithm in numerical precision. Composing the exact-query ensemble
therefore costs the square of that order in retained memory, its fifth
power in initialization and complete training, and its fourth power in
the query envelope. The fixed-parameter powers of `SOURCE_SEED_EXACT_QUERY.md`
are preserved. Evaluator and input costs remain additional charged terms.

## 1. Parameters and the conditional interface

The network has width \(n\), \(m\ge d\ge1\) training examples,
input dimension \(d\), depth \(L\ge2\), population feature-Gram gap
\(\gamma>0\), and label RMS \(Y=\|y\|_2/\sqrt m\).
The original Gaussian initialization, zero readout, physical optimizer,
and complete original intersection of upper label conditions are retained.
Let \(\beta\ge10\) be the supplied activation envelope, bounding the
first two derivatives on the half-strip and including the reciprocal
strip width. Activation values may be unbounded. Zero labels have the
separate exact zero predictor.

Take \(0<\delta<1/4\). For a concrete confidence allocation set
\(\rho=2^{-20}\delta\), and define the integer collision/moment order

\[
 p=\max\left\{1,\left\lceil
  \frac{\log(4emL/\rho)}{\log(64e^2)}\right\rceil\right\}.
 \tag{1}
\]

This is the \(p\) of `FINITE_COMPLEX_MOMENT_GATE.md` and the candidate
probability theorem. In contrast, throughout this note \(w\) denotes
**bits per numerical word**: it is the quantity called \(p\) in
`SOURCE_SEED_EXACT_QUERY.md` and `GAP_REFINED_PHASE_COSTS.md`.
The two uses of \(p\) must never be substituted for one another.

For compact parameter accounting define

\[
 D=m+d+2,\qquad G=1+m/\gamma,\qquad c=d+1,
\]
\[
 Z=\log(en)+\log\!\left(e+
       \frac{D\beta^{100L}G}{\delta}\right),\qquad
 \Lambda=\log(e+cZ).
 \tag{2}
\]

All logarithms in asymptotic bounds may be converted to base two at a
universal cost. The choice \(\rho=2^{-20}\delta\) changes the original
precision logarithm only by an absolute additive constant. In particular
\(p\le CZ\) and \(\log p\le CZ\), with universal \(C\).

The scientific assumption is that the candidate source event holds at
failure \(\rho\), on its complete complex training rectangle with
physical half-width

\[
 r_t=\frac1{p\beta^{100L}(1+\gamma/m)\sqrt{\log(en)}}.
 \tag{3}
\]

Its candidate sufficient width is

\[
 n\ge\left\lceil\left[
 \frac{\beta^{2000L}G^4(m+d+p+1)^4}{\rho}
 \right]^{20000}\right\rceil.
 \tag{4}
\]

Equation (4) is used here as an assumed scientific gate, not a review
conclusion. The exact-query construction additionally supplies its
one-member physical comparison, common pre-setup tolerance choices,
finite-transcript generation and whole-source median amplification.
Those correctness statements are separate from the deterministic cost
composition below.

For the clean table assume \(nY\ge1\). This is an implementation
precision gate, not an assumption in the proposed source-probability
theorem and not a tighter upper label allowance. Section 5 gives the
explicit alternative for smaller positive \(Y\).

Only fixed small scientific failure is needed for each ensemble member.
Thus taking \(\rho=2^{-20}\), independently of \(\delta\), is also
possible within the stated exact-query interface. Equations (1)--(4)
give a convenient conservative allocation that exposes every confidence
dependence without using that improvement.

## 2. What the smaller radius changes

Normalize time by \(\tau=(\gamma/m)t\). Equation (3) becomes

\[
 r_\tau=\frac1{p\beta^{100L}G\sqrt{\log(en)}}.
 \tag{5}
\]

Let \(H_0\) be the old certified equal-patch count and \(K_0\) the old
Taylor degree from `GAP_DEGREE_REFINEMENT.md`. Its patch lengths satisfy
\(h_0\le[64\beta^{100L}G\sqrt{\log(en)}]^{-1}\).
Choose exactly \(H=pH_0\) equal patches, each of length
\(h=h_0/p\). Then \(4h\le r_\tau/16\), so every local complex disk
fits the new radius, and the local contraction estimates only improve.
This construction preserves the certified-ceiling convention and avoids
a very short final interval.

The numerical recurrence really uses the dimensionless patch variable
\(\xi=(\tau-\tau_j)/h\). In the notation of the normalized state
\(\bar u\) and its local vector field \(\overline F_j\), its coefficient
identity is

\[
 \bar u[k+1]=\frac{h}{k+1}[\xi^k]\overline F_j(\xi,\bar u(\xi)).
 \tag{6}
\]

This is the recurrence proved in `FAST_TAYLOR_NOISE.md`, Sections 4--6.
It stores dimensionless Taylor coefficients, not derivatives multiplied
by \(h^{-k}\). Centered activation interpolation has coefficient and
scratch bounds \(\exp(CJ_{\rm act})\), where its interpolation degree
\(J_{\rm act}=O(K)\). Its centered-series cap is uniform on
\(|\xi|\le4\). Therefore shrinking \(h\) produces no
\(K\log p\) growth from unscaled derivative storage.

The real propagation inequality in `GAP_DEGREE_REFINEMENT.md` is

\[
 e_{j+1}\le
 (1+2h_j\mu_j+2\sqrt{L+1}\,2^{-K})e_j
       +C h_j\eta+2Mh_j2^{-K},
 \qquad \sum_jh_j\mu_j\le E_+.
 \tag{7}
\]

Here \(e_j\) is the normalized Hilbert-state error, \(\eta\) its
local forcing allowance, \(M\) the reference derivative bound, and
\(E_+\) the integrated one-sided real expansion bound. The latter
depends on the physical trajectory and its horizon, not on patch count.
In particular the only unweighted count contribution to its multiplier
product is \(2\sqrt{L+1}H2^{-K}\). Since

\[
 \log(1+16\sqrt{L+1}\,pH_0)
 \le\log p+\log(1+16\sqrt{L+1}\,H_0),
\]

the degree choice

\[
 K=K_0+\lceil\log_2p\rceil
 \tag{8}
\]

suffices in that note's explicit degree formula. The total forcing sum
still contains \(\sum h_j=T\), not \(H\). No factor \(p\) multiplies
the real stability exponent.

Endpoint rounding must be \(O(h_j\eta)\), so its tolerance tightens
by \(p\). Converting an integrated-coefficient error into a velocity
error introduces the same \(h_j^{-1}\) factor. Local scalar-forcing
caps and summand counts are fixed-degree polynomials in
\(R,K,h_{\min}^{-1}\) and the old physical scales. Their logarithms
therefore gain \(O(\log p)\). The matrix-noise precision in the source
is \(2K+O(\log\eta^{-1})\); centered interpolation and finite
coefficient precision have the same additive dependence.

Finally, `FAST_FINITE_SOURCE_BRIDGE.md` chooses tolerances from a fixed
number of products and minima of the local caps and \(R\), and sums
one-call failure allowances of order \(1/R\). Its exact accumulation
and counter bits add logarithms of counts. With the common source/query
schedule of `SOURCE_SEED_EXACT_QUERY.md`, these operations again add
only \(O(\log p)\) bits. They do not propagate numerical errors through
the expanded row-history graph.

The actual named-field count is \(O(d+mLHK)\), including activation
samples. Thus its precise increase contains
\(p(K_0+\lceil\log_2p\rceil)/K_0\). It is not literally bounded by
\(p\) times every possible old actual count. Because
\(K_0\le C\beta^{100L}Z\), \(\log p\le CZ\), and the old patch
bound is \(C\beta^{100L}GZ\sqrt{\log(en)}\), a sufficient constructive
envelope is

\[
 R\le C p\beta^{201L}DGZ^{5/2},\qquad
 w\le C\beta^{110L}Z.
 \tag{9}
\]

Relative to the same pre-existing precision schedule, the required word
length increases by \(O(\log p)\). Equation (9) absorbs that increase
in its universal constant. The coefficient-work condition \(K\le CH\)
also survives: \(K_0\le CH_0\) and \(\log p\le CpH_0\).
Consequently the source's quadratic row-work bound remains valid with
the enlarged \(R\). These checks establish the factor \(p\) in the
field-count **envelope**, without an additional algebraic precision factor.

## 3. Exact modular costs, with no collision/word ambiguity

Let \(J\) be the odd number of ensemble members. The input/time code
count \(N_{\rm ext}\) has
\(\log N_{\rm ext}\le Cc(Z+\log p)\le CcZ\); the extra patch-index
bits are logarithmic in \(p\). The median construction can therefore use

\[
 J\le CcZ,\quad E=1+\lceil\log_2(n+2)\rceil\le CZ,
 \quad A\le CR^2w,
 \quad b\le C\{R^2wE+\log(N_{\rm ext}/\delta)\}.
 \tag{10}
\]

Here \(A\) is the inner generator block length, and \(b\) is the
complete one-member input block length, including its scalar-noise marks.
Neither is a neural-network weight. One regeneration of all member
blocks costs

\[
 T_{\rm outer}\le CJb^2\log(J+2).
 \tag{11}
\]

The retained internal bits, also bounding peak training/query bits, are

\[
 M_{\rm ret}\le C\{JR^2w+b\log(J+2)\}.
 \tag{12}
\]

Initialization is sequential over members, so its peak is
\(M_{\rm ret}+C(nRw+R^3w)\), with no factor \(J\) on the full
temporary source table. In bit operations the phase costs are

\[
\begin{aligned}
 T_{\rm init}\le{}&CJ\{nR^5w^3+(nR+R^2)w^4+R^5w^2
             +R^4w^3+nR^2w^2+nA^2E\}+T_{\rm outer},\\
 T_{\rm train}\le{}&CJ(R^5w^2+R^4w^3+R^3w^2),\\
 T_{\rm query}\le{}&CJ(L+1)\{n(A^2E+Rw^4+R^2w^2)
                         +R^4w^2+R^3w^3\}\\
 &\quad+T_{\rm outer}+CJw\log(J+2).
\end{aligned}
 \tag{13}
\]

The training line counts the complete update schedule. Scalar marks are
retained, so repeated outer-block regeneration is unnecessary during
training. Even charging one complete regeneration to that phase is
covered by the simplified table below. A query regenerates rows using
immutable acquired scalars and performs the full conditional covariance
correction. It does not replay scalar training updates.

## 4. Parameter-explicit internal table

Substituting (9)--(10) gives

\[
 A\le Cp^2\beta^{512L}D^2G^2Z^6,
 \qquad b\le Cp^2\beta^{512L}D^2G^2Z^7,
\]
\[
 M_*:=Cp^2\beta^{512L}D^2G^2Z^7(c+\Lambda),
 \qquad
 T_{\rm outer}\le Cc p^4\beta^{1024L}D^4G^4Z^{15}\Lambda.
 \tag{14}
\]

All constants in the following table are universal. Units are bits for
memory and bit operations for work. General activation and data interfaces
are added in Section 5; the supplied tanh evaluator fits these internal
envelopes.

| Phase | Internal work | Peak internal memory, including the model |
| --- | --- | --- |
| Initialization | \(Cnc p^5\beta^{1335L}D^5G^5Z^{33/2}\) | \(M_*+C[np\beta^{311L}DGZ^{7/2}+p^3\beta^{713L}D^3G^3Z^{17/2}]\) |
| All training | \(Cc p^5\beta^{1225L}D^5G^5Z^{31/2}\) | \(M_*\) |
| One query | \(Cc p^4\beta^{1024L}D^4G^4[(L+1)nZ^{14}+Z^{15}\Lambda]\) | \(M_*\) |

Retained internal model size is at most \(M_*\). The two contributions
\(c\) and \(\Lambda\) respectively pay for the ensemble's compact
states and its retained outer seed. They cannot both be omitted.

For verification, the leading initialization monomial is
\(JnR^5w^3\), with activation exponent \(5(201)+3(110)=1335\)
and logarithmic exponent \(1+5(5/2)+3=33/2\).
The leading training monomial is \(JR^5w^2\), giving \(1225L\)
and \(31/2\). The query row generator is bounded by
\(J n A^2E\le CJ n R^4w^2E\), giving \(1024L\) and \(14\).
Outer generation contributes the distinct \(Z^{15}\Lambda\) term.

All other monomials in (13) have lower powers in each positive parameter
than their displayed enclosing phase terms, except that outer generation
needs one explicit check for training. Since

\[
 \Lambda=\log(e+cZ)
 \le C\{\log(e+c)+\log(e+Z)\}\le CD\sqrt Z,
 \tag{15}
\]

the outer term is at most
\(Cc p^4\beta^{1024L}D^5G^4Z^{31/2}\), covered by the training
line. It is also covered by the initialization line for \(n\ge1\).
This uses \(D^5\) versus \(D^4\); it does not assume that
\(\log(d+1)\) is universally bounded by \(\sqrt Z\).

At fixed \(m,d,\gamma,\beta,L,\delta\), the moment order \(p\)
is fixed and \(Z=\Theta(\log(en))\). Thus the resulting bounds are

\[
\begin{aligned}
 M_{\rm ret}&=O(\log^7(en)\log\log(e^e+n)),\\
 T_{\rm init}&=O(n\log^{33/2}(en)),\\
 T_{\rm train}&=O(\log^{31/2}(en)),\\
 T_{\rm query}&=O(n\log^{14}(en)
                 +\log^{15}(en)\log\log(e^e+n)).
\end{aligned}
 \tag{16}
\]

Peak initialization memory is additionally
\(O(n\log^{7/2}(en)+\log^{17/2}(en))\). The retained/training/query
bound is not an initialization-memory bound.

## 5. Activation, input, certificate and small-label costs

Let \(\mathcal V_\phi(w)\) and \(\mathcal S_\phi(w)\) be the actual
worst-case bit work and scratch of the supplied activation value evaluator
at the certified argument range and precision. Its code description is
retained. Needed derivative jets are formed by the charged centered
interpolation; an analytic envelope is not an evaluator-time theorem.
Safe value-call counts are

\[
\begin{aligned}
 N_{\phi,\rm init}&\le CJnR
       \le Cnc p\beta^{201L}DGZ^{7/2},\\
 N_{\phi,\rm train}&\le CJR^2
       \le Cc p^2\beta^{402L}D^2G^2Z^6,\\
 N_{\phi,\rm query}&\le CJ(L+1)(nR+R^2)\\
 &\le Cc(L+1)[np\beta^{201L}DGZ^{7/2}
                         +p^2\beta^{402L}D^2G^2Z^6].
\end{aligned}
 \tag{17}
\]

The \(R^2\) query term conservatively covers local preparation. These
are source-row regeneration counts, not the earlier passive-population
sampling count. For each phase add
\(N_{\phi,\rm phase}\mathcal V_\phi(w)\) work and one live evaluator
workspace \(\mathcal S_\phi(w)\). The supplied
\(O(w^3)\)-work, \(O(w)\)-scratch tanh evaluator is already absorbed
by (13)--(16).

The normalized training table has \(m(d+1)\) numerical entries and fits
the internal memory envelope. Acquiring it is an external cost. Raw labels
require at least the requested fractional precision

\[
 w+\lceil\log_2(16\sqrt m)\rceil
       +\lceil\log_2\max(1,1/Y)\rceil.
 \tag{18}
\]

Let \(B_{\rm ext}\) be the actual retained data, evaluator, scale and
certificate-description bits not already counted in the finite table.
Let \(T_{\rm access,phase}\) and \(S_{\rm access,phase}\) be the
actual phase work and workspace to acquire/verify data and certificates,
acquire the query and time code when present, and write the answer.
Then a complete interface-level statement is

\[
\begin{aligned}
 M_{\rm ret,total}&\le M_*+B_{\rm ext},\\
 M_{\rm peak,phase,total}&\le M_{\rm peak,phase}
           +B_{\rm ext}+\mathcal S_\phi(w)+S_{\rm access,phase},\\
 T_{\rm phase,total}&\le T_{\rm phase}
           +N_{\phi,\rm phase}\mathcal V_\phi(w)
           +T_{\rm access,phase}.
\end{aligned}
 \tag{19}
\]

Thus neither gap/strip certificates nor arbitrary data descriptions are
free oracles. These external terms may dominate every internal bound.

For \(0<nY<1\), put
\(\zeta_Y=\log_+(1/(nY))\). Replacing the use of \(Y^{-1}\le n\)
in the local tolerance formulas adds \(C\zeta_Y\) to sufficient word
precision. One must also revisit the degree: the normalized tube/forcing
formulas contain the label scale, so the universally safe substitution is

\[
 Z_Y=Z+\zeta_Y,
 \qquad R\le Cp\beta^{201L}DG Z_Y^{5/2},
 \qquad w\le C\beta^{110L}Z_Y.
 \tag{20}
\]

Equations (10)--(13), with these enlarged counts and any correspondingly
refined code count, are the conservative modular alternative. Merely
changing \(w\) while leaving every degree/count fixed is not asserted
here. The clean table (14)--(16) uses the explicit gate \(n\ge1/Y\).
At fixed positive \(Y\) that gate eventually holds; no uniform
\(Y\)-independent work claim follows from the probability theorem alone.

## 6. An explicit polynomial gate for quadratic internal work

One initialization, all training, and one query together satisfy

\[
 T_{\rm internal}\le
 Cn c p^5\beta^{1335L}D^5G^5 Z^{33/2}.
 \tag{21}
\]

Here \(L+1\le\beta^L\), (15), and the unused activation powers cover
the query and outer-generation terms. More queries pay their individual
query costs; (21) is not a bound for arbitrarily many queries.

A simple additional sufficient gate is

\[
 n\ge\left[
 \frac{\beta^{1335L}D^5G^5c p^5}{\delta}\right]^2.
 \tag{22}
\]

To check it, let the bracket be \(P\). Then the parameter prefactor
in (21) is at most \(P\le\sqrt n\), and
\(D\beta^{100L}G/\delta\le P\). Consequently
\(Z\le2\log(en)\). Writing \(t=\log n\ge0\), the function
\((1+t)^{33/2}e^{-t/2}\) has a finite universal maximum (at \(t=32\)).
Thus (21) is at most \(Cn^2\) bit operations under (22).
The output constant is universal; this is not a numerical coefficient-one
inequality against a particular implementation.

The huge scientific gate (4) already dominates (22), purely algebraically.
Indeed let \(Q=m+d+p+1=D+p-1\) and
\(S_{\rm src}=\beta^{2000L}G^4Q^4/\rho\). Since
\(D,c,p\le Q\) and \(\rho\le\delta\),

\[
 P\le\frac{\beta^{1335L}G^5Q^{11}}{\delta}
       \le S_{\rm src}^3.
\]

Therefore \(n\ge S_{\rm src}^{20000}\) implies \(n\ge P^2\).
This conclusion uses no probability argument and no unspecified
asymptotic source constant. If a numerical coefficient is required in
the work comparison, retain (22) with the chosen universal work constant
inserted in its bracket.

The remaining finite-source gates can be listed explicitly. Besides the
scientific input (4), the clean table uses
\(n\ge d\), \(n\ge1/Y\), and the deterministic horizon condition
\(n\ge\max\{1,e^{-1}\sqrt{1+66\beta^{100L}m/\gamma}\}\).
The stopped finite-source coupling in `FAST_FINITE_SOURCE_BRIDGE.md`
(25) has failure bounded by the supplied scientific failure, its allocated
coupling tolerance, and \(R\exp(-c_g n)\). The appended physical query
adds at most \(C(L+1)\exp(-c_g n)\), where \(c_g>0\) and \(C\)
are universal Gaussian RMS constants. A sufficient explicit gate for
these additional RMS failures to total at most \(\rho\) is

\[
 n\ge C_0\left[
       \frac{p\beta^{201L}DG}{\rho}\right]^2,
 \tag{23}
\]

with a sufficiently large universal \(C_0\). Indeed, writing the
bracket as \(P_{\rm RMS}\), (23) implies \(Z\le C\log(en)\) and
\((R+L+1)/\rho\le C\sqrt n\,[\log(en)]^{5/2}\).
The last quantity times \(\exp(-c_g n)\) is at most one above a
universal width; choose \(C_0\) to enforce that width and pay the
displayed universal constants. This is an ordinary polynomial gate,
not a stochastic eventual-width clause.

If \(A_{\rm num}Yn^{-10}\) is the combined allocated numerical
prediction remainder, its absorption into the instantiated dense
certificate uses the explicit additional condition from
`SOURCE_SEED_EXACT_QUERY.md`, Section 5:

\[
 n\ge\max\{1,(A_{\rm num}/32)^{1/9}\}.
 \tag{24}
\]

Here \(A_{\rm num}\) is the chosen numerical allocation constant; the
source/center/tail correctness statements are separate scientific inputs,
not new onsets introduced by this cost calculation.

Finite Gaussian sampler tails, moment-grid and answer tolerances,
completed-call total variation, scalar rounding-boundary failures, metric
replay, and the two generator errors are controlled by the explicit
precision/confidence allocations in the supplied finite interfaces. They
do not require another asymptotic width condition. In particular the
earlier passive block-sampling gate in `GAP_REFINED_PHASE_COSTS.md` (9)
is not used by this exact-query route: the query streams all \(n\)
regenerated source rows.

For a single enclosing gate, \(P_{\rm RMS}\le S_{\rm src}\) because
\(pD\le Q^2\), and the activation/gap powers in \(S_{\rm src}\)
are larger. The same source scale dominates \(d\) and the displayed
horizon expression. Consequently, with a sufficiently large universal
\(C_*\), all gates (4), (22)--(24) and the deterministic conditions
just listed follow from

\[
 n\ge\max\left\{
 C_*S_{\rm src}^{20000},\;Y^{-1},\;1,\;
 (A_{\rm num}/32)^{1/9}\right\}.
 \tag{25}
\]

The factor \(C_*\) pays only universal finite-source and cost constants;
it has no hidden dependence on data, gap, labels, confidence, or activation
beyond the displayed parameters. No additional finite-source width gate
appears in the supplied interfaces used for this composition. Equation
(25) still presupposes the stated scientific inputs; this note does not
independently approve their probability, center, or tail conclusions.

A standard dense forward pass performs \(\Theta((L-1)n^2+nd)\)
scalar multiply-adds, not \(O(n^2)\) bit operations uniformly in precision
and depth. With schoolbook arithmetic its usual upper bound contains
\(w^2\), and its own activation/data costs must be added. What (22)
proves is a quadratic internal **bit-operation** upper bound for the
composed construction. It does not make arbitrary evaluator or data
access costs quadratic, nor prove a practical speedup at the enormous
source threshold.

## Inputs and scope record

Read completely: `SOURCE_SEED_EXACT_QUERY.md`,
`GAP_REFINED_PHASE_COSTS.md`, `FINITE_COMPLEX_MOMENT_GATE.md`, and
`FULL_FINITE_SOURCE_PROBABILITY.md`; the supervisor then explicitly
expanded the scope to `FAST_TAYLOR_NOISE.md`,
`GAP_DEGREE_REFINEMENT.md`, `SHORT_CAUSAL_TRAINING_PROGRAM.md`, and
`FAST_FINITE_SOURCE_BRIDGE.md`. No linked source, study history, other
study, or review verdict was fetched. The short causal-program note was
not substituted for the newer normalized Taylor implementation.

The exact-query input hash was
`3a6c5a35bff72af9e5d6ae3dfdcc4258db6e84290e14845f589ece6550e35e39`;
the source-probability candidate hash was
`2a7bfd057b33d79970d39fa2a98340203bc8e80b55944e5ef49f200ff4510c40`.
A prompt-only scoped subagent independently checked polynomial expansion
and the quadratic-work gate. That arithmetic check is not an independent
scientific review. Only this assigned file was written.

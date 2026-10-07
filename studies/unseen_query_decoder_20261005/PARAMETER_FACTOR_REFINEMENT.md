# Explicit parameter factors and cached finite-response evaluation

2026-10-06. Scoped author derivation in the existing study. This is a
proof-only scheduling and accounting refinement, not independent review,
promotion, an experiment, or a new scientific approximation theorem.

Retaining completed-call coefficient vectors and selected-row values removes
repeated historical work. In particular, one query needs only the current
passive-layer matrix preparations. Its preparation cost loses one full
history-count factor. Keeping input dimension separate from sample count also
sharpens the displayed polynomial factors. The complete pair table, finite
prior, source precision, statistical block size, scientific assumptions and
accuracy qualifications remain those of the supplied local-precision decoder.

## 1. Setting and the certificates being counted

Use dense width \(n\), training sample count \(m\), input dimension \(d\),
depth \(L\ge2\), population feature-Gram gap \(\gamma>0\), label RMS

\[
Y=\|y\|_2/\sqrt m,\qquad G=1+m/\gamma,\qquad
\ell=\log(en),
\]
\[
Z=\log(en)+\log\!\left(e+
\frac{(m+d+2)\beta^{100L}G}{\delta}\right).
\tag{1}
\]

Here \(m\ge d\ge1\), the training inputs span the input space and lie on
its radius-\(\sqrt d\) sphere, and \(0<\delta<1/4\). The activation
envelope \(\beta\ge10\) is exactly that of
`FAST_LOCAL_EFFICIENCY_RESULT.md`: it includes the common strip reciprocal,
values at zero, and first two half-strip derivative bounds. The dense model,
zero readout, all learned layers, mean squared loss and mobilities

\[
(n,1,\ldots,1,n)
\]

are unchanged. Preserve the entire inherited label intersection, not only its
consequence \(16Ym/\gamma\le1\). The \(Y=0\) branch is the exact zero
predictor; the following resource calculation concerns \(Y>0\).

Let \(H\) be the number of equal Taylor patches and \(K\) the local Taylor
degree. The supplied construction gives

\[
H\le C\beta^{100L}GZ\sqrt\ell,\qquad
K\le C\beta^{100L}GZ,
\tag{2}
\]

and its activation interpolation degree is at most \(CK\). Write

\[
N=mHK.
\tag{3}
\]

This is the number of sample/patch/coefficient indices at one layer, up to
fixed multiplicities. Let \(R\ge2\) denote an actual named-field/action
certificate comparable to the actual named-field count, including first-layer
roots, innovations and the constant field. The complete pair schedule has

\[
P\asymp R^2,\qquad D\le CR,
\]

where \(P\) is the scalar acquisition count and \(D\) the row-packet
dimension. Its sharp source bound is

\[
R\le C(d+LN)
\le C\{d+mL\beta^{200L}G^2 Z^2\sqrt\ell\}.
\tag{4}
\]

Throughout this note the sufficient numerical word length remains

\[
p\le C\beta^{110L}(d+1)GZ.
\tag{5}
\]

These are constructive sufficient choices with universal constants. No
comparison between an actual \(p\) and an actual \(R\) is inferred by dividing
their upper envelopes. The explicit substitution in Section 6 uses only
upper bounds with nonnegative powers. The query cancellation uses the actual
complete pair count, not an arbitrarily inflated upper certificate.

## 2. Local matrix dimensions

For one initialized hidden matrix, there are \(O(mHK)=O(N)\) forward
coefficient queries and the same number of reverse queries. Its conditioning
matrices use only these histories for this matrix label. The complete pair
table contains more entries, but cross-layer auxiliary pairs do not enlarge
a physical posterior coefficient system.

The learned rank list has \(O(mHK^2)\) scalar weights at each layer.
Its row factors are the \(O(mHK)\) stored feature and backward coefficient
fields; the additional \(K\) counts products between these factors, not
new independent row factors. Thus the passive master histories formed by
concatenating posterior query/answer and learned-rank factors also have

\[
r_{\rm layer}\le C(d+N)\le CN
\tag{6}
\]

columns. The last inequality uses \(d\le m\le N\). This includes the
first layer's \(d\) original Gaussian columns. It includes the final
readout factors as well. There is no global \(R\)-dimensional covariance
system required merely because the private selected-coordinate metric has
dimension as large as \(R\).

Use the residual-controlled symmetric matrix routine in
`SANE_DECODER_CORE.md`, Sections 3--4. At dimension \(r\) its work and
scratch are

\[
C(r^4p^2+r^3p^3),\qquad Cr^2p.
\tag{7}
\]

Its inverses, roots and Sylvester solves retain their original positive
floors. Formula (7) counts their logarithmic reciprocal floors in \(p\);
it is not unit-cost matrix arithmetic or an inverse-gap-length iteration.
There are \(O(LN)\) historical conditioning calls. Preparing each only
when its coefficient inputs have become available therefore costs

\[
C L(N^5p^2+N^4p^3).
\tag{8}
\]

This replaces the coarser \(C(R^5p^2+R^4p^3)\) for these preparations.
It does not change the dimension of the metric-construction problem.

## 3. Cache immutable fields and their metric images

Let \(q\le CR\) be the number of selected packets and let
\(\widehat M\in\mathbb R^{q\times q}\) be the retained finite metric.
For each created field \(v\), retain its selected values
\(v(I)\in\mathbb R^q\). Their creation-time scalar arguments are
immutable. A later scalar acquisition therefore never invalidates an old
cached value. Extend the finite row program at each newly created field;
do not reevaluate all its old predecessors at every pair request.

The complete finite row circuit has \(O(R^2)\) scalar arithmetic operations
per packet, including centered activation interpolation and first-layer
input contractions, by `FAST_TAYLOR_NOISE.md` (40) and
`SANE_DECODER_CORE.md` (14). Running it incrementally at the selected
packets costs \(CqR^2p^2\le CR^3p^2\).

This cache also fits the active interpolation scratch. During one patch,
its \(mL\) active centers need \(O(mLK^2)\) scalar scratch per row.
The source proves \(K\le CH\), so this is at most \(CR\). Completed
patch scratch can be discarded while its named field outputs remain.
For \(q\) rows both the field-value array and this active scratch use

\[
CqRp\le CR^2p
\tag{9}
\]

bits. There is no requirement to retain all interpolation scratch from all
patches simultaneously.

At creation of \(v\), additionally compute and retain

\[
w_v=\widehat M v(I).
\tag{10}
\]

All later pairs involving \(v\) use the exact dot product \(u(I)^T w_v\).
Equation (10) costs \(Cq^2p^2\) per field; the \(P\) requested pairs
cost \(CqPp^2\) in total. Hence the whole metric-contraction work is

\[
C(q^2R+qP)p^2\le CR^3p^2.
\tag{11}
\]

The additional images \(w_v\) use another \(CqRp\) bits. Products and
sums in (10)--(11) are exact dyadic operations before the prescribed
scalar grid rounding. Their lengths are a fixed multiple of \(p\), since
\(\log R\) is already covered. Reassociation of these exact sums changes
no rounded scalar answer.

The pair-acquisition order, scalar marks and rounding rules are unchanged.
Mandatory innovation contractions stay inside their own original call,
with frozen coefficient arrays and no intervening solve. The additional
complete-table pairs are still acquired only at completed-call boundaries.
Only computationally available operands are cached. This schedule preserves
the same finite tape on the original replay event; it does not need a new
rounding-boundary probability argument.

## 4. Retain historical affine coefficients, prepare only new query systems

A completed finite matrix call has the form

\[
\widehat y=Q_{h_y}(\widetilde m+U\widetilde T\widehat t+c\widehat g),
\tag{12}
\]

with finite row-independent coefficients, completed scalar innovation
moments \(\widehat t\), and a row-independent affine representation of
\(\widetilde m\) in older named fields. The finite source explicitly
rounds its small coefficient arrays once and performs the final affine
combinations exactly. Thus after \(\widehat t\) is acquired, the vector
\(\widetilde T\widehat t\), the mean's coefficient vector and \(c\)
give the identical finite row operation (12). This is also the last
conclusion of `SANE_DECODER_CORE.md`, Lemma 2.

Store these completed-call coefficient vectors when the call occurs and
discard its spectral scratch. Across all calls there are at most

\[
CLN^2\le CR^2
\tag{13}
\]

finite coefficients. Other row-independent projection/rank/interpolation
templates and scalar rank weights fit the existing \(CR^2\) allowance.
Only already acquired coefficients are retained: no future scalar answer or
future coefficient vector is saved during offline initialization. Every
cached coefficient is a deterministic function of the current acquired
prefix, so this introduces no extra conditioning information into the
passive posterior.

At an unseen query, evaluate the old finite row interpreter using these
stored coefficients. Its row-dependent activation centers, interpolation
values and nonlinear arithmetic are still recomputed at each sampled prior
packet and remain in the \(CR^2p^2\) row cost. The cache saves historical
matrix solves; it does not treat old nonlinear row values at a new packet
as already known.

The new passive forward recursion has \(Q\le C(L+1)\) stages. At each
stage only a bounded number of current master-Gram functions, posterior
mean/Sylvester arrays, variance matrices and whitening arrays are prepared.
Their dimensions obey (6). Current time-dependent scalar rank coefficients
can be assembled once, with \(CR^2p^2\) work as a conservative allowance.
Consequently the preparation for one query is bounded by

\[
C\{Q(r_{\rm layer}^4p^2+r_{\rm layer}^3p^3)+R^2p^2\}.
\tag{14}
\]

All matrices are finite functions of the retained complete pair table,
current time and incoming passive context. Fix that context while evaluating
its block moments. The history coefficient cache is present before querying;
there is no scalar training replay. The temporary passive matrix arrays and
stored historical coefficients both fit \(CR^2p\) bits.

## 5. Complete modular costs, keeping the median count explicit

Let \(J\) be the odd median block count, \(s\) the prescribed prior-block
length, \(A\) the finite generator's block parameter and \(E\) its level
count. Keep the supplied block-generator interface: one packet uses

\[
C\{Rp^4+R^2p^2+A^2E\}
\tag{15}
\]

bit work, counting the finite Gaussian sampler, row arithmetic and generator
work separately. This form permits a separate refinement of \(J,A,E\)
without changing the caching proof.

Initialization, all compact training updates, and one query have the bounds

\[
\begin{aligned}
W_{\rm init}\le C\{&nR^5p^3+(nR+R^2)p^4\\
&+L(N^5p^2+N^4p^3)+nR^2p^2\},\\
W_{\rm train}\le C\{&L(N^5p^2+N^4p^3)+R^3p^2\},\\
W_{\rm query}\le C\{&QJs(Rp^4+R^2p^2+A^2E)\\
&+Q(r_{\rm layer}^4p^2+r_{\rm layer}^3p^3)+R^2p^2\}.
\end{aligned}
\tag{16}
\]

The metric term \(nR^5p^3\) and its exact-integer scratch are unchanged.
Source generation includes all finite Gaussian marks, all row arithmetic
and all source coefficient preparations. Scalar marks used by compact
training were generated and retained at initialization.

Including retained seeds and all block vectors, the post-initialization
peak and retained memory are bounded by

\[
C\{R^2p+QAE+RJp\}.
\tag{17}
\]

One stage's block vectors suffice; seeds for all stages are retained. The
initialization peak additionally contains \(C(nRp+R^3p)\).

For the currently supplied choices \(J\le Cp\), \(A\le CRp\),
\(E\le Cp\), (17) becomes the unchanged memory bound

\[
C\{R^2p+(L+1)Rp^2\}.
\tag{18}
\]

The complete pair schedule and scalar-noise choice still give

\[
K_*\asymp R^2p/\alpha,\qquad
K_*\le\widehat K_*\le2K_*,\qquad
s=\left\lfloor\frac{n}{128\widehat K_*}\right\rfloor,
\quad n\ge512\widehat K_*,
\tag{19}
\]

with the same allocated confidence share \(\alpha>0\). In particular
\(s\le Cn/(R^2p)\). The stream part of (16) is therefore at most

\[
CQn(p^4/R+p^3).
\tag{20}
\]

This cancellation uses (19), and does not assume \(p\le R\). Since
the packet includes the \(d\) initial root fields, \(R\ge d\ge1\)
is sufficient for the explicit query envelope below.

## 6. Fully substituted bounds with the original word certificate

For this section alone use \(d\le m\) to absorb the additive \(d\) in
(4): \(R\le CmL\beta^{200L}G^2Z^2\sqrt\ell\). Keep \(d+1\)
separate in (5), and keep explicit factors of \(L\), without inflating
the activation exponents to absorb them. Substitution in (16)--(20) gives
the following sufficient internal bounds with universal constants:

\[
\begin{aligned}
S_{\rm model},\ S_{\rm train/query}
&\le C\beta^{510L}m^2L^2(d+1)G^5Z^5\ell,\\[1mm]
W_{\rm init}
&\le Cn\beta^{1330L}m^5L^5(d+1)^3G^{13}Z^{13}\ell^{5/2},\\[1mm]
S_{\rm init}
&\le Cn\beta^{310L}mL(d+1)G^3Z^3\ell^{1/2}\\
&\quad+C\beta^{710L}m^3L^3(d+1)G^7Z^7\ell^{3/2},\\[1mm]
W_{\rm train}
&\le C\beta^{1220L}m^5L(d+1)^2G^{12}Z^{12}\ell^{5/2},\\[1mm]
W_{\rm query}
&\le CnL\beta^{440L}(d+1)^3G^4Z^4\\
&\quad+C\beta^{1020L}m^4L(d+1)^2G^{10}Z^{10}\ell^2.
\end{aligned}
\tag{21}
\]

For memory, the separate seed/block-vector term before domination is

\[
C(L+1)mL\beta^{420L}(d+1)^2G^4Z^4\sqrt\ell.
\]

Its ratio to the displayed model envelope is bounded using
\((d+1)/m\le2\), \((L+1)/L\le3/2\), \(G,Z,\ell\ge1\), and
\(\beta^{-90L}\le1\). The two coefficient terms before domination
in the training bound are

\[
CLm^5\beta^{1220L}(d+1)^2G^{12}Z^{12}\ell^{5/2},\qquad
CLm^4\beta^{1130L}(d+1)^3G^{11}Z^{11}\ell^2.
\]

The first dominates the second by the same parameter inequalities. It
dominates the cached-row term \(CR^3p^2\), since its remaining ratio
contains \(\beta^{400L}/L^2\). The analogous query preparation terms
have activation powers \(1020L\) and \(930L\), with the first again
dominating. The query stream uses \((d+1)^4/d\le2(d+1)^3\).
Every Gaussian-generation term in initialization is dominated after
substitution; for example its largest parameter envelope without \(n\) is

\[
Cm^2L^2\beta^{840L}(d+1)^4G^8Z^8\ell,
\]

which is below the displayed initialization work using \(n\ge1\) and
\(d+1\le2m\). No extra eventual-width gate is used for this accounting.

At fixed other parameters the resulting powers are six in post-initialization
bits, \(31/2\) in width-normalized initialization work, \(29/2\) in
training work, and four in width-normalized query-stream work plus twelve
in query preparation. The twelve replaces the historical-recompilation
preparation power \(29/2\). These are upper bounds for this schedule, not
lower bounds on possible decoder resources.

## 7. Actual evaluators, label scale and scientific width remain charged

The real activation sampling construction uses at most
\(2nmLH(J_{\rm act}+1)\le CnR\) value-evaluator calls to initialize
the source, where \(J_{\rm act}\le CK\) is its interpolation sample
count, distinct from the median block count \(J\). The cached selected
rows use at most \(CqR\le CR^2\) such calls over all compact updates.
Thus sufficient explicit activation-call counts are

\[
Cn mL\beta^{200L}G^2Z^2\sqrt\ell,
\qquad Cm^2L^2\beta^{400L}G^4Z^4\ell
\tag{22}
\]

for initialization and training. The common requested precision/range
allowance is (5). Each fresh query packet still pays \(CR\) calls for
its complete old row interpreter and fresh passive operation. The inherited
safe query evaluator allowance \(CQ(JsR+R^2)\) remains available; (19)
and \(J\le Cp\) give \(CQ(n/R+R^2)\). This conservative allowance
also covers fixed coefficient-literal/data work; the caching proof does
not require a stronger claim about that interface.

Multiply these counts by the actual work of the supplied evaluators and
add one live evaluator workspace. Input descriptions, evaluator descriptions,
certificates and output-scale encoding remain additive storage. Training
coordinates and labels can be obtained once at their required precision;
their \(O(md+m)\) finite values fit the model's \(O(R^2p)\) numerical
allowance, while the work of obtaining them is charged separately. Raw-label
normalization at precision \(p\) requires the additional fractional bits

\[
\lceil\log_2(16\sqrt m)\rceil+
\lceil\log_2\max(1,1/Y)\rceil.
\tag{23}
\]

Charge query/time acquisition, certificate acquisition/verification and
output writing. There is no hidden internal power of \(1/Y\), but input
precision at tiny \(Y\) is not free. Analyticity and the envelope \(\beta\)
alone supply no universal finite-bit activation evaluator. The tanh evaluator
bound stated in the supplied headline can be substituted into these call
counts, but is not a claim about arbitrary analytic activations.

All scientific and label gates remain, including

\[
nY\ge1,\qquad
n\ge\max\{1,e^{-1}\sqrt{1+66\beta^{100L}m/\gamma}\},
\]

and the sampling gate (19). The finite passive theorem still gives

\[
\sup_{t\in[0,\infty],\ \|v\|=1}
|\widehat f(t,v)-f_n^{\rm independent}(t,v)|
\le2b_n+CY\mathcal P
\sqrt{(R+1)(K_*+1)/n}+CYn^{-10}.
\tag{24}
\]

Here \(b_n\) is the inherited dense-pair upper certificate, and
\(\mathcal P\) is exactly the finite-depth passive amplification of
`FAST_FINITE_PASSIVE.md` (4), with its supplied physical cap and confidence
dependence. Neither is redefined by this resource refinement. The larger
vector-sampling factor in (24) is retained. Its eventual absorption into
the original upper certificate, and the original stochastic scientific
width threshold, remain unquantified. No polynomial bound in
\(m,d,\gamma^{-1},\beta,L,Y^{-1},\delta^{-1}\) on that onset is asserted.
In particular a favorable runtime bound for shorter statistical blocks must
not be reported without their gate and enlarged remainder.

## 8. Status and input boundary

The new claims are exact reuse of immutable finite outputs, exact cached
metric contractions, the local matrix inventory, and the resource consequences
(16)--(22), conditional on the supplied finite-source/decoder interfaces.
They do not establish an improved statistical rate, a lower-than-six
logarithmic bit-memory power, polylogarithmic query work, or a practical
crossover width. This note preserves the whole sphere, all physical times,
endpoint, independent dense run and original dense-pair upper-certificate
target. It is not near-\(1/n\) approximation of a specified initialized run.

Only the eight assigned scientific inputs were read completely:
`FAST_LOCAL_EFFICIENCY_RESULT.md`, `FAST_LOCAL_COMPOSITION.md`,
`SANE_DECODER_CORE.md`, `FAST_TAYLOR_NOISE.md`,
`FAST_FINITE_SOURCE_BRIDGE.md`, `FAST_FINITE_PASSIVE.md`,
`SANE_METRIC_PACKETS.md`, and `FAST_SMALL_MATRIX_FUNCTIONS.md`.
No referenced review, unassigned study, prior verdict, or extra source was
retrieved. The research, rigorous-proof, canonical-notation and neural-network
instructions were read and applied. The supervisor's separate precision/
confidence suggestion was deliberately not used in deriving this note;
(16)--(17) leave \(J,A,E\) explicit for an independently justified substitution.

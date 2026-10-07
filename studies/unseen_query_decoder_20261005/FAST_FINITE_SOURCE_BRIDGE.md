# A finite iid-packet source with local physical coupling

2026-10-06. Scoped author theorem, conditional on the supplied physical
Taylor and scalar-forcing lemmas. No independent review, experiment,
promotion, Git operation, or complete passive-decoder claim.

A finite source with iid finite row packets can couple to the original
physical noisy Taylor calculation using local precision
\[
 p_{\rm loc}\le C\{\chi+\log(1/\rho)\},\qquad
 \chi=\beta^{100L}(1+m/\gamma)Z,\quad 0<\rho<1/4.             \tag{1}
\]
Here \(Z\) includes the input-size logarithm in FAST_TAYLOR_NOISE.md.
Actual activation/data evaluator work and input descriptions remain
charged interfaces. Equation (1) is not a uniform work bound for an
arbitrary analytic activation.

The physical comparison executes the **same finite postprocessing** as
the source. An affine Gaussian pair is introduced only for the proof.
The source's actual rounded-innovation-before-answer calculation is a
function of this completed pair. Common postprocessing costs no extra
total variation. Its difference from the raw physical answer is a small
local forcing defect. This avoids both global history sensitivity and
the need to match every matrix-answer rounding boundary.

## 1. Scope and inherited physical interfaces

Keep the original nonlinear network, all trained layers, zero initial
readout, loss, physical mobilities, full label intersection, and all
source width/probability gates. Zero labels retain the zero predictor.
On the nonzero branch let
\[
 r=m/\gamma,\qquad Y=\|y\|_2/\sqrt m\ge n^{-1},\qquad
 B=\beta^{100L},\qquad \chi=B(1+r)Z.
\]
The displacement norm is
\[
 \|A-A_0\|_F/\sqrt n+
 \sum_{j=2}^L\|W^{(j)}-W_0^{(j)}\|_F+\|w\|_2/\sqrt n,       \tag{2}
\]
and the source normalizes displacement by \(Y\) and uses \(\tau=t/r\).

FAST_TAYLOR_NOISE.md supplies the patch schedule, interpolation,
coefficientwise matrix noise, local arithmetic and strict-slack guards.
FAST_SCALAR_FORCING.md, frozen at SHA-256
6b74c2a49046bdce4d30b0bf46535ddbc6498332b91fb3d516fefb0bd09f23bb,
supplies physical pair errors relative to the **actual current
operands**. Let \(\epsilon_{\rm pair},\epsilon_{\rm ans}>0\) be
sufficient tolerances from those notes for pairs and local principal
coefficient/answer defects. They may be decreased by fixed factors and
have logarithmic reciprocals at most \(C\chi\). Their causal
prefix-completion argument covers the physical guards.

The physical matrix noise satisfies \(\log(1/\sigma)\le C\chi\).
The action and named-field count remains
\[
 R\le C\{d+mL\beta^{200L}(1+r)^2Z^2\sqrt{\log(en)}\}.          \tag{3}
\]
Enlarge \(R\) by an absolute factor for first-layer roots, innovations,
and the constant field. There are \(P\le CR^2\) pair acquisitions and
\(D\le d+CR\) row-root coordinates. Thus
\(\log(e+n+R)+\log(e+P)\le C\chi\).

Only physical query/answer Grams enter the protected posterior
coefficient formulas. Innovation/physical moments have separate caps.
A fresh innovation moment never enters a coefficient solve or PSD
projection during its own call.

## 2. Finite Gaussian samplers and iid packets

For \(T_G\ge2,\epsilon_G>0\), a finite uniform-bit sampler has a coupling
to \(g\sim N(0,1)\) with
\[
 |\widehat g-g|\le\epsilon_G\quad\text{if }|g|\le T_G,\qquad
 |\widehat g|\le T_G+1.                                    \tag{4}
\]
The coupled finite value can be a deterministic function of \(g\).
Indeed put \(u=\Phi(g)\), take the midpoint of its \(b_G\)-bit binary
interval, and approximate the inverse normal CDF clipped to
\([-T_G,T_G]\). The clipped inverse is Lipschitz with constant at most
\(\sqrt{2\pi}e^{T_G^2/2}\). It suffices to use inverse-evaluation error
\(\epsilon_G/2\) and
\[
 b_G\log2\ge T_G^2/2+\log(C/\epsilon_G).                    \tag{5}
\]
The interval index is uniform on its \(2^{b_G}\) possibilities, so the
algorithm uses genuine finite uniform bits. The Gaussian-CDF series
and certified bisection in SANE_DECODER_CORE.md provide finite work and
scratch; inverse CDF evaluation is not free.

Use independent copies for row-root coordinates and scalar marks. With
\[
 N_G=n(d+R)+P+1,\qquad
 T_G=\left\lceil2+\sqrt{2\log(1024N_G/\rho)}\right\rceil,     \tag{6}
\]
the union of failures in (4) is below \(\rho/512\).
Coordinate types can use distinct precisions but identical laws across
rows; the resulting finite vector packets are iid. The source samples
finite bits directly and never computes the inverse proof coupling.

## 3. The actual finite chronology

All named fields are dyadic. Their finite row evaluator is deterministic.
Old fields retain creation-time scalar arguments. Numerical coefficient
outputs are finite bit strings, not exact-real oracles.

For an ordinary pair acquisition use exact dyadic products and integer
summation, retain division by \(n\) rationally, then set
\[
 C_a=Q_h\left(n^{-1}\sum_i u_a(i)v_a(i)+\eta\widehat E_a\right).
                                                               \tag{7}
\]
Here \(Q_h\) is nearest-grid rounding with a fixed tie rule,
\(0<h\le\eta\) are dyadic, and the fresh finite scalar mark is
independent of all packets and earlier scalar marks. The operands are
already-created finite fields.

At a forward call, let \(U\) collect the old finite reverse queries
and let \(s\le R\) be its column count. Before reading the fresh
innovation coordinate, prepare finite protected mean coefficients,
a symmetric finite correction matrix \(\widetilde T\), and a finite
positive scalar \(c\). Write
\[
 \widetilde m,\quad B_c=U\widetilde T,\quad
 A_c=U^T/n,\quad c>0.                                     \tag{8}
\]
The mean uses old finite answer/query fields. Round small coefficient
arrays once to dyadic outputs and perform their final linear
combinations exactly. Round symmetric entries identically.
A guard \(c\ge\sigma/2\) is inactive on the successful range.

Read one new finite row mark \(\widehat g_i\) per row and execute
\[
 \widehat t=Q_{h_t}(A_c\widehat g+\eta\widehat e),\qquad
 \widehat y=Q_{h_y}(\widetilde m+B_c\widehat t+c\widehat g).
                                                               \tag{9}
\]
The first operation is an empirical pair acquisition with fresh finite
scalar marks. The second is rowwise affine dyadic arithmetic before
rounding. Coefficients stay frozen throughout (9), and no matrix call
is inserted between its two operations. Reverse calls exchange
orientations. Required new physical-field pairs are acquired afterward.

Finite innovation marks can be used in all later formulas and pairs
specified by the compiler; they are included in the proof below.
Physical interpolation, convolution, rank lists, residuals and guards
use the finite local instructions of the supplied physical notes.
Thus this is an explicit finite iid-packet source, including its
innovation-before-answer chronology.

## 4. An affine shadow with the same finite postprocessor

At a fixed complete past take independent standard Gaussians
\(g\in\mathbb R^n,e\in\mathbb R^s\), only for the proof, and define
\[
 t=A_cg+\eta e,\qquad y=\widetilde m+B_ct+cg.                \tag{10}
\]
Its answer covariance is
\[
 \widetilde\Gamma=\widetilde S^2+\eta^2B_cB_c^T,\qquad
 \widetilde S=cI_n+B_cA_c.                                \tag{11}
\]
Symmetry uses symmetric \(\widetilde T\). Positivity on the comparison
range is checked below, not inferred from a noisy projected Gram.

Since \(c,\eta>0\), the map is invertible:
\[
 g=(y-\widetilde m-B_ct)/c,\qquad e=(t-A_cg)/\eta.           \tag{12}
\]
Consequently (9), including every finite mark the call will ever use
later, is a deterministic function \(J_H(y,t)\): reconstruct (12) in
the proof, apply the fixed finite-sampler functions of Section 2, and
execute the actual finite arithmetic (9).
The algorithm computes this output directly from finite marks and
never performs (12). In particular its precision does not pay for
this proof-only inversion of \(\eta\).

The function \(J_H\) may be discontinuous. Common postprocessing
cannot increase total variation.

### Completed-call posterior and safe future-used marks

Let \(H\) contain previous raw answers, finite fields, scalar acquisitions
and consumed auxiliary marks. It excludes raw physical answer noises,
unconsumed future packet coordinates, and private selected packets or
metric. External initial fields are independent of the hidden matrices.

Let \(Q_H(dy,dt)\) be (10), with conditional law \(Q_H(dt\mid y)\).
Compare it to the physical call
\[
 y=W_0q+\sigma\xi,\quad \xi\sim N(0,I_n)
       \text{ fresh and hidden},\qquad
 t\mid(H,y,W_0)\sim Q_H(dt\mid y).                         \tag{13}
\]
Apply \(J_H\) and use its finite answer in the physical program.
The conditional augmentation is independent of all initialized matrices
once \(H,y\) are fixed. Its likelihood factor cancels from Bayes' formula.
Thus conditioning additionally on \(t,J_H(y,t)\), or any reconstructed
finite innovation mark, leaves the posterior given \(H,y\) unchanged.
Posterior independence across matrix labels is preserved.

If \(P_H\) is the true physical raw-answer Gaussian law, then
\[
 \|Q_H(dy,dt)-P_H(dy)Q_H(dt\mid y)\|_{\rm TV}
       =\|Q_H(dy)-P_H(dy)\|_{\rm TV}.                     \tag{14}
\]
Integration against the common conditional kernel gives one inequality,
and projection onto \(y\) gives the other. Common finite postprocessing
can only decrease this distance.

An intermediate prefix revealing only \(\widehat t\) need not have a
Gaussian posterior. No matrix call uses that prefix's posterior.
The entire finite transcript of (9) is a projection of the completed
call and is still controlled by (14).

## 5. Local finite defects and one-call Gaussian comparison

Let \(b\ge2\) bound physical query and raw-answer RMS on the supplied
good range, with fixed rounding slack and \(\log b\le C\chi\). Set
\[
 z=C(2+R+b+\sigma^{-1}),\qquad
 \mathcal M=(n+1)z^{120}.                                 \tag{15}
\]
This bounds local coefficient magnitudes, \(|c|\),
\(\|A_c\|_{\infty\to\infty}\), and
\(\|B_c\|_{\infty\to\infty}\). For \(A_c\), Cauchy--Schwarz gives
the bound \(b\). For \(B_c\), combine \(|U_{ij}|\le\sqrt n b\),
at most \(R\) summands and the coefficient bound \(z^{100}\).
These are one-call bounds, not a history recurrence.

On (4), direct subtraction in (9)--(10) gives
\[
 \|\widehat t-t\|_\infty
       \le(\mathcal M+1)\epsilon_G+h_t/2=:d_t,\qquad
 \|\widehat y-y\|_\infty
       \le h_y/2+\mathcal M d_t+\mathcal M\epsilon_G.       \tag{16}
\]
Take
\[
 h_t\le\min\{\eta,h_y/(64\mathcal M)\},\qquad
 \epsilon_G\le\min\{h_t/(64\mathcal M),
                         h_y/(64\mathcal M^2)\}.         \tag{17}
\]
Then the answer discrepancy is below \(h_y\), in coordinates and RMS.

At a shared history both laws use the same actual finite query.
Replacing raw answers by finite answers changes a query/answer pair
by at most \(b h_y\), and an answer/answer pair by at most
\(2b h_y+h_y^2\).
Ordinary acquired pairs differ from their actual finite empirical
values by at most \(\eta(T_G+1)+h/2\).
Hence the current coefficient inputs have error at most
\[
 e_{\rm mom}\le
 C\{(b+1)h_y+h_y^2+\eta(T_G+1)+h\}.                       \tag{18}
\]
The true table here uses actual raw answers at this same history, not
answers recomputed at a different history. This removes the apparent
need for a global history-error recurrence.

Let local coefficient outputs have entrywise error \(\epsilon_c\)
relative to the protected exact maps on the finite input table.
Put \(e_c=e_{\rm mom}+z^{10}\epsilon_c\), including dimension
conversions and assembly. The local coefficient and Gaussian estimates
in FAST_LOCAL_KERNEL_AUDIT.md, with this additional triangle-inequality
error, yield the conservative one-call bound
\[
 \kappa\le z^{230}\{\sqrt n\,e_c+n\eta^2\},                \tag{19}
\]
when its right side is at most \(1/32\). The same smallness gives
\(\|\widetilde S-S\|\le\sigma/2\), so
\(\widetilde S\succeq\sigma I/2\).
Here \(S\) is the positive square root of the physical covariance.

For completeness the inputs to that calculation are
\(\|\widetilde m-m\|_2\le\sqrt n\,\operatorname{poly}(z)e_c\),
\(\|\widetilde S-S\|\le\operatorname{poly}(z)e_c\), and
\(\|\eta^2B_cB_c^T\|_F\le\eta^2nRb^2z^{200}\).
At reference covariance floor \(\sigma^2\), the Gaussian
relative-entropy formula and \(x-\log(1+x)\le x^2\) for
\(|x|\le1/2\), followed by the entropy-to-TV bound, prove (19).
Exponent 230 enlarges the audit's 220 for finite coefficient errors
and dimension factors. There is no inverse empirical-Gram gap.

## 6. Choice order and local precision

First choose the physical schedule, caps and tolerances, and then set
\[
 \xi_0=\frac{\rho}{2^{20}(R+1)(n+1)z^{240}}.              \tag{20}
\]
Take dyadics within a factor two below the following bounds:
\[
 \begin{split}
 \eta&\le\min\{\epsilon_{\rm pair},\xi_0\}/[64(T_G+1)],\\
 h&\le\eta/4,\\
 h_y&\le\min\{\epsilon_{\rm ans}/16,\xi_0/[64(b+1)]\},\\
 \epsilon_c&\le\xi_0/(64z^{10}).
 \end{split}                                            \tag{21}
\]
Decrease fixed absolute constants further if needed for (19).
Then choose \(h_t,\epsilon_G\) by (17), and the sampler by (5).
For the later metric replay set \(\alpha_{\rm acq}=\rho/16\)
and also take
\[
 \eta\epsilon_G\le
       \frac{\alpha_{\rm acq}\min(h,h_t)}{64(P+1)}.
                                                               \tag{21a}
\]
This is the finite scalar-mark coupling allowance used by its
rounding-boundary lemma; it is at most that lemma's
\(\zeta=\alpha_{\rm acq}\min(h,h_t)/(64P)\).
The sampler failure in (6) is below \(\alpha_{\rm acq}/2\).
Thus both its error and probability hypotheses hold. This adds only
\(C[\chi+\log(1/\rho)]\) precision and no scientific restriction.
Physical pair error is below \(\epsilon_{\rm pair}/8\), answer
postprocessing error below \(\epsilon_{\rm ans}/16\), and one-call
TV below \(\rho/[64(R+1)]\). The covariance positivity hypotheses
hold. Other local physical arithmetic uses the remaining tolerance.

Couple finite first-layer roots to the original Gaussian first matrix.
Their normalized initial displacement is at most
\(\sqrt d\,\epsilon_G/Y\).
Let \(\epsilon_{\rm init}\) be the final normalized source tolerance
times \(e^{-2E-2}/64\), or a smaller allocated allowance, and impose
\[
 \epsilon_G\le Y\epsilon_{\rm init}/(\sqrt d+1).           \tag{22}
\]
The physical recurrence then starts at this small nonzero error.
The finite first matrix is a numerical initial state near the original
Gaussian initialization; the scientific initialization is unchanged.
The bounds \(Y\ge n^{-1},E\le C\chi\) make (22) a \(C\chi\)-bit cost.

All choices obey
\[
 \log(1/\eta)+\log(1/h)+\log(1/h_y)+\log(1/h_t)
 +\log(1/\epsilon_G)+\log(1/\epsilon_c)
 \le C\{\chi+\log(1/\rho)\}.                              \tag{23}
\]
This is a fixed number of precision requirements, not a product over
past calls.

The residual-controlled small-matrix algorithms in SANE_DECODER_CORE.md
compute each protected coefficient array with word length
\(C[\log(1/\epsilon_c)+\log(1/\sigma)+\log(n+R+b+2)]\);
their iteration count adds only logarithmic guard positions.
Centered activation interpolation and local physical arithmetic use
FAST_TAYLOR_NOISE.md, (31), (36)--(39).
Exact empirical accumulation adds \(\log n\) bits, and the bounded
number of dyadic products in (9) changes word length by an absolute
factor. Thus (1) holds, within the charged input/primitive interface.

No Lipschitz bound for the entire rounded row map is claimed.
Identical finite packet and prefix arguments reproduce identical bits.

## 7. Stopped coupling and physical conclusion

Extend the finite source only for the proof with the independent raw
Gaussians behind its samplers. At each complete call maximally couple
its affine shadow answer to the physical Gaussian answer. On matching
answers use the same conditional augmentation \(Q_H(dt\mid y)\).
Both sides execute \(J_H\), identical other finite operations, and
identical fresh ordinary scalar marks.

The finite tapes agree exactly until the first coupling failure.
At most \(R\) instances of (19) cost less than \(\rho/64\); discrepancies
are not propagated along a numerical history.

Stop at coupling failure, latent sampler failure or a first physical
range violation. The source marginal has independent raw latent
Gaussians, giving (6). The physical marginal retains the original
initialized matrices and fresh independent raw answer noises, whose
RMS event fails with probability at most \(Re^{-cn}\).

Before these stops,
\[
 \widehat y_j=W_0\widehat v_j+\sigma\xi_j+d_j
 \quad\text{or}\quad
 \widehat y_j=W_0^T\widehat u_j+\sigma\xi_j+d_j,\qquad
 \|d_j\|_2/\sqrt n\le h_y.                                \tag{24}
\]
Physical pairs satisfy the current-operand specification in
FAST_SCALAR_FORCING.md; its actual stored rank list defines the
physical matrix. Together with the local arithmetic/interpolation
budgets and (22), these meet the physical forcing hypotheses.
The supplied causal prefix-completion argument excludes the first
physical guard violation on the scientific good event.

Conditioning caps are local: physical RMS bounds give raw Gram caps,
(18) gives nearby finite inputs, the gapped formulas give coefficient
caps, and finite marks satisfy (4). Choose fixed slack throughout.
Innovation contractions remain outside the physical PSD projection.

The stopping bound may charge sampler failure on the source marginal
and physical failure on the physical marginal. Their augmented histories
agree before coupling failure, so these marginal failure probabilities
add. A coupling therefore has total failure at most
\[
 \Pr(\text{inherited scientific failure})+Re^{-cn}+\rho.   \tag{25}
\]
On its complement, the actual finite rank-list parameters meet the
normalized Taylor tolerance after allocating the fixed error fractions.
Their parameter-defined predictor has the supplied all-time,
whole-sphere accuracy, including the frozen fitted endpoint.
No efficient retained-state decoder for new queries is supplied here.

## 8. Finite acquisition and remaining passive obligations

The source satisfies the finite-source premises of
FAST_LOCAL_PRECISION_TEST.md: iid finite packets, independent finite
scalar marks coupled to fresh Gaussians, deterministic dyadic fields,
exact-product pairs, immutable creation-time arguments, and rounded
noisy scalar updates.

Innovation scalars have grid \(h_t\); ordinary scalars have grid \(h\).
Apply that note's boundary estimate separately to each grid, using
\(\min(h,h_t)\) for a common metric-error budget. Both have the
logarithmic bound (23), so literal finite-tape replay gives acquisition
base
\[
 O(R^2p_{\rm loc})                                       \tag{26}
\]
bits for selected packets, metric, current scalar history, finite
scalar marks and existing explicit coefficient arrays, besides input
descriptions and charged primitive interfaces. Scalar rank weights
and interpolation scratch fit the existing \(O(R^2)\) scalar count.
Metric construction retains its separate exact-integer preprocessing
cost. Full field tables and future scalar answers are discarded.

Private selection never enters the matrix posterior filtration.
Conceptual offline availability of all packet coordinates does not
permit the causal physical program to use unconsumed future marks.

A passive statistical decoder still requires a separate theorem for
this finite iid-packet, rounded-scalar law or an explicitly coupled
continuous reference. Continuous Gaussian-channel entropy is not
automatically an entropy theorem for finite noise. Exchangeability
and an information bound by transcript bit length alone do not prove
the passive neural normal form, common-Gram buffers, query rounding
or a compact seed. The raw proof history in (13) is richer than the
retained scalar prefix; marginalizing it does not leave a Gaussian
matrix posterior.

Likewise (26) does not prove local error control for a new arbitrary
row packet substituted into the expanded training-response circuit.
The source runs on its realized finite tape, and exact metric replay
preserves that tape. Passive query/reference stability remains separate.

## 9. Status and provenance

| Claim | Status and scope |
|---|---|
| Finite iid-packet schedule (7)--(9) | Explicit finite algorithm with charged primitives |
| Future-used innovation marks preserve completed-call posterior | Proved by (12)--(14); future coordinates and private selection excluded |
| Local coefficient and Gaussian-law error | Proved by (18)--(21) on the physical capped range |
| Physical finite-source coupling | Conditional theorem (24)--(25), using frozen forcing interfaces |
| Local source/acquisition precision | Proved within inherited primitive/input interface |
| Full locally precise passive decoder | Open; does not follow from this bridge |

Complete newly scoped inputs read: FAST_LOCAL_KERNEL_AUDIT.md,
FAST_LOCAL_PRECISION_TEST.md, FAST_SCALAR_FORCING.md,
FAST_TAYLOR_NOISE.md, NOISY_TWO_ORIENTATION_TRANSCRIPT.md,
NOISY_SCALAR_HISTORY_ACQUISITION.md and RECALIBRATION_FREE_MOMENTS.md.
Previously authorized physical/Taylor/core/metric interfaces were used.
Research/proof skills and relevant contract, evidence and adversarial
instructions were applied. The private canonical-notation skill was
permission-inaccessible; the supervisor-authorized maintained-notation
fallback was used. No review, research history, unassigned study source,
experiment or Git state was read. Only this assigned artifact was written.

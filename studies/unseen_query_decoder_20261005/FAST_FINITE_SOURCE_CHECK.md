# Bounded reconstruction of the finite physical-source bridge

2026-10-06. Component reconstruction, not a fresh isolated review,
promotion review, or complete passive-decoder verdict.

## Verdict and scope

**PASS, conditional on the physical Taylor/scalar-forcing interfaces and
scientific good event explicitly inherited by the target.** I found no
blocking defect in the finite-source coupling, completed-call chronology,
local precision, or exact metric-replay interface at the frozen target
hash below. No correction to this target was required during this check.

This verdict does not re-establish the original scientific width gates,
physical response estimates, or fitting theorem from their underlying
sources. Those sources are outside the assigned inputs. It also does not
establish a passive finite-law neural normal form, new-packet response
stability, a statistical block bound, query rounding, or a full decoder.
The target correctly keeps those conclusions separate.

This reviewer previously reconstructed other components in this study
(uniform queries, local acquisition precision, physical query grids, and
finite posterior bookkeeping). Accordingly this is not a fresh isolated
review. Their verdicts and unassigned scientific artifacts are not used as
proof inputs here. Unchanged assigned core/metric/precision sources that
had already been read completely were reused; the other assigned inputs
were read completely for this check. No study history, another review,
experiment, Git state, external scientific source, or maintained source
was consulted. Only this report was written.

The required research, rigorous-mathematics, and canonical-notation skills,
including the neural-network notation reference, were applied. They
governed the scope separation and the reconstruction below; they supply
no scientific premise.

## 1. Frozen inputs and precise claim

All paths below are in `studies/unseen_query_decoder_20261005/`.

| Complete input | SHA-256 |
|---|---|
| `FAST_FINITE_SOURCE_BRIDGE.md` | `7ef69972a213fb26b77cd1c0ed4dcbd8b7d12f9e3b06906f351f7443f79894e6` |
| `FAST_SCALAR_FORCING.md` | `6b74c2a49046bdce4d30b0bf46535ddbc6498332b91fb3d516fefb0bd09f23bb` |
| `FAST_LOCAL_KERNEL_AUDIT.md` | `0d019d666b9d286391da75e0310340803d74eb048285ee9e89740d8056b042af` |
| `FAST_LOCAL_PRECISION_TEST.md` | `af2a238a3ea1ed73059fd61321ca8408ce487399542156dc44e5e06f5a3e2f91` |
| `FAST_TAYLOR_NOISE.md` | `71c67ce4de343077f3795aa9a9892052560da7b7ab51a59f6609027744c8881c` |
| `NOISY_TWO_ORIENTATION_TRANSCRIPT.md` | `0c422a0c06b00b606c220a2631482ecab81911857aa05620ed395ce134bf8aac` |
| `NOISY_SCALAR_HISTORY_ACQUISITION.md` | `b301507a73de79310634ca67da75a9f5817a139edc498ad145aaeb857cae6fab` |
| `SANE_DECODER_CORE.md` | `701de0d9ed9a429e6f9d771a9e4a96854872c9600509866a617da70690139fa4` |
| `SANE_METRIC_PACKETS.md` | `1683563689c824593613cb636590ae3180f4cc897913c8ed5acb3c12170adeea` |

Write \(r=m/\gamma\), \(Y=\|y\|_2/\sqrt m\),
\(\chi=\beta^{100L}(1+r)Z\), and
\(\|v\|_{2,n}=\|v\|_2/\sqrt n\). On the nonzero branch the
assigned source assumes \(Y\ge n^{-1}\). Its normalized time is
\(\tau=t/r\), and normalized parameter errors divide the target's
block norm (2) by \(Y\).

The audited conclusion is existence of a finite iid-packet source, with
local word allowance \(p_{\rm loc}=O(\chi+\log(1/\rho))\), and a
coupling to one physical initialization and its whole causal noisy tape.
At every successful call its finite answer has the form

\[
 \widehat y_j=W_0\widehat v_j+\sigma\xi_j+d_j
 \quad\text{or}\quad
 \widehat y_j=W_0^T\widehat u_j+\sigma\xi_j+d_j,
 \qquad \|d_j\|_{2,n}\le h_y.
\]

Here the same initialized matrix is used at all calls to that label,
different labels retain their original independent initialization, and
the physical raw answer noises are fresh independent standard Gaussians.
They are not separately revealed to the program. The assigned physical
forcing results then give the asserted parameter/prediction comparison.

## 2. Finite iid sampling and the actual algorithm

For a standard Gaussian \(g\), \(\Phi(g)\) is uniform. Its first
\(b_G\) binary digits therefore give exactly a uniform fixed-length bit
block. Replacing that uniform value by its cell midpoint changes it by
at most \(2^{-b_G-1}\). The inverse CDF clipped to \([-T_G,T_G]\)
is globally Lipschitz with constant at most
\(\sqrt{2\pi}e^{T_G^2/2}\): inside the interval this follows from the
inverse derivative, and outside it the map is constant. A finite inverse
evaluation with error \(\epsilon_G/2\) therefore gives the target's
coordinate coupling under (5). On \(|g|\le T_G\), clipping adds no
error. Dyadic evaluation supplies finite outputs, including at the tails.

The prescribed cutoff gives
\(2N_Ge^{-T_G^2/2}<\rho/512\). As the target permits, take the
enlarged \(R\) to dominate the actual fresh row-coordinate count, so
\(nD+P\le N_G\). Independent blocks give independent scalar marks
and iid row packets, even when different coordinate types have different
fixed precisions. The sampler is an actual uniform-bit algorithm, not
sampling arbitrary real probabilities at unit cost.

The core's certified CDF intervals and bisection avoid exact comparisons
with transcendental CDF values. With word allowance \(p_{\rm loc}\),
their coarse cost is \(O(p_{\rm loc}^4)\) bit operations per Gaussian
coordinate and \(O(p_{\rm loc})\) scratch, or the stated larger
packet scratch when the packet is retained. Such source-generation work
must still be added to metric-construction work.

The finite call in (9) has a crucial fixed order: prepare the mean
coefficients, symmetric \(\widetilde T\), and \(c\); read the fresh
row innovation; acquire its opposite-query contractions; then form and
round the answer. No coefficient solve, PSD projection, or new matrix
call may occur between those contractions and the answer. Ordinary pairs
use exact finite products and sums and exact rational division by \(n\)
until the outer rounding. These instructions meet the finite-source
requirements of the acquisition lemma.

## 3. Completed pairs, safe auxiliary marks, and one matrix tape

Fix a complete past \(H\), and put
\(A_c=U^T/n\), \(B_c=U\widetilde T\). For independent Gaussian
\(g\in\mathbb R^n\), \(e\in\mathbb R^s\), the affine shadow is

\[
 t=A_cg+\eta e,\qquad y=\widetilde m+B_ct+cg.
\]

Since \(c,\eta>0\), the displayed inverse (12) recovers both \(g\)
and \(e\) from \((y,t)\). Thus one deterministic postprocessor
\(J_H\) recovers every finite sampler mark, carries out the actual
rounded contractions and answer arithmetic, and returns any marks that
later instructions will use. It is important to include those marks,
not merely the finite answer, in this postprocessor. The proof-only
division by \(\eta\) is not performed by the finite algorithm and
does not impose an algorithmic precision requirement.

Let \(Q_H\) be this joint Gaussian pair law and let \(P_H\) be the
physical conditional raw-answer law. Augment the physical answer with
the common conditional kernel \(Q_H(dt\mid y)\). Direct integration
and projection give

\[
 \|Q_H(dy,dt)-P_H(dy)Q_H(dt\mid y)\|_{\rm TV}
 =\|Q_H(dy)-P_H(dy)\|_{\rm TV}.
\]

Applying the same \(J_H\) to both sides cannot increase this distance,
regardless of its rounding discontinuities. Consequently no matrix-answer
rounding-boundary estimate is required.

The posterior argument also survives this augmentation. At a fixed rich
history, the physical likelihood is the product of the original Gaussian
answer likelihoods, multiplied by augmentation/ordinary-scalar factors
that do not depend on any initialized matrix once the observed prefix
and each raw answer are fixed. Those factors cancel from Bayes' formula.
This gives exactly the two-orientation Gaussian posterior derived in the
assigned transcript, with its original \(\sigma^2\) floor and its
conditional independence across matrix labels. Finite innovation marks
reconstructed from \((H,y,t)\) add no further information given that
completed history.

This is not a claim that conditioning on \(\widehat t\) alone leaves
a Gaussian posterior. The prohibition on a matrix call at that intermediate
prefix is necessary. Nor may the program read future innovation coordinates
or the privately selected metric/panel. Reading a consumed mark later is
allowed; reading an unconsumed one early is a different filtration.

Chronological coupling of these observable kernels yields a coupling of
whole tapes. The physical marginal is the causal process generated from
one initial matrix per label and its fresh answer noises; equivalently,
after coupling the observable laws, their physical latent variables can
be attached using that process's conditional law. This construction does
not replace a reused matrix by a fresh draw at each call.

## 4. Local defects and conditional Gaussian error

With the target's \(z=C(2+R+b+\sigma^{-1})\) and
\(\mathcal M=(n+1)z^{120}\), all required local norms fit the stated
cap. For example \(\|A_c\|_{\infty\to\infty}\le b\). Even the
coarse entrywise estimate
\(\|B_c\|_{\infty\to\infty}\le\sqrt n\,bR^2z^{100}\)
is absorbed by \(\mathcal M\). This estimate uses no earlier-phase
error amplification.

Subtracting the finite and shadow equations gives exactly (16). Conditions
(17) imply \(\|\widehat y-y\|_\infty<h_y\), hence also the RMS
bound, while \(\widehat t\) has its stated small local defect.

At a shared completed history, the true posterior uses past raw answers;
the finite coefficients use their finite postprocessed versions. Both use
the same finite queries. For every old answer the already established
coordinate defect is at most \(h_y\). Cauchy--Schwarz therefore gives
the query/answer and answer/answer errors in (18). Adding the ordinary
pair perturbation gives that equation's \(e_{\rm mom}\).

There is also a direct substitution of old finite answer vectors for raw
ones in the posterior mean, not just a change in scalar Gram entries.
Its Euclidean error is at most \(\sqrt n\,\operatorname{poly}(z)h_y\)
by the bounded mean-coefficient norms and the \(O(R)\) old fields.
It is covered by the target's \(\sqrt n\operatorname{poly}(z)e_c\)
estimate. The covariance root uses old queries only. PSD projection is
nonexpansive in Frobenius norm around the genuine raw Gram, and the gapped
inverse/root/Sylvester formulas have polynomial local sensitivity. These
facts justify applying the kernel estimate at the same history, without
comparing that history to a separately evolved unperturbed tape.

For clarity, let \(\Gamma=S^2\succeq\sigma^2I\) be the physical
answer covariance. The source covariance is
\(\widetilde\Gamma=\widetilde S^2+\eta^2B_cB_c^T\).
The bounds on the mean difference, root difference, and added covariance
give

\[
 \|\widetilde m-m\|_2\le\sqrt n\operatorname{poly}(z)e_c,
 \quad
 \|\widetilde\Gamma-\Gamma\|_F
 \le\operatorname{poly}(z)(\sqrt n e_c+n\eta^2).
\]

Set \(E_\Gamma=\Gamma^{-1/2}(\widetilde\Gamma-\Gamma)
\Gamma^{-1/2}\). When its operator norm is below \(1/2\), the
Gaussian relative entropy is bounded by half the sum of
\(\sigma^{-2}\|\widetilde m-m\|_2^2\) and
\(\|E_\Gamma\|_F^2\), using
\(x-\log(1+x)\le x^2\). The entropy-to-TV inequality proves the
form of (19). The displayed exponents 100, 220 and the additional finite
dimension/assembly allowances fit its conservative exponent 230. The
same smallness ensures \(\widetilde S\succeq\sigma I/2\).
No empirical Gram eigenvalue is used.

With (20)--(21), \(e_c\) is at most a fixed small multiple of
\(\xi_0\). Thus \(z^{230}\sqrt n e_c\) is well below
\(\rho/[64(R+1)]\); the \(z^{230}n\eta^2\) term is smaller.
The remaining fixed constants can indeed be decreased as stated.

## 5. Stopping and the physical forcing interface

Couple complete calls while their finite histories agree. A matching raw
answer uses the same conditional \(t\), hence the same postprocessed
finite answer and every future-used mark. Common ordinary scalar marks
then preserve all other finite instructions. The first mismatch probability
is bounded by the sum of the local TV errors, below \(\rho/64\).

The sampler-tail event is charged on the source marginal, where its latent
Gaussians really are independent. The scientific event and raw-noise RMS
event are charged on the physical marginal, where the matrices retain
their original law and the answer noises are independent. No independence
between these events is needed to add their failure probabilities. Stop
before using any estimate outside its local capped range.

Before stopping, the source satisfies the physical action identity in
Section 1 and the actual-current-operand pair specification. In particular,
an actual rank list \(D=n^{-1}\sum_\mu c_\mu a_\mu b_\mu^T\)
has learned-action defect

\[
 \sum_\mu c_\mu a_\mu
 \bigl(\widehat p(b_\mu,v)-\langle b_\mu,v\rangle_n\bigr).
\]

This is bounded by the scalar-forcing note's local rank-count and factor
caps; it does not require separately tracking unperturbed rank factors.
Freezing realized coefficient errors into forcing polynomials costs
\(4^K\), not a power indexed by earlier calls. Residual errors are
normalized by \(Y\) once. Integrated coefficient errors and independent
endpoint rounding have the separately supplied local allocations.

The strict-slack guard argument is causal: at a proposed first active
guard, retain the already realized defects, complete future defects with
zero, construct the supplied holomorphic comparison, and identify the
already computed coefficients. Cauchy/endpoint bounds and the pair-based
norm-test margin then contradict guard activation. This argument does
not introduce the older zero-slack residual projection into the Taylor
recurrence. Conditioning caps follow separately from genuine physical
Grams and the local gapped formulas; fresh innovation moments stay outside
that projection.

The first-layer sampler adds normalized initial error at most
\(\sqrt d\,\epsilon_G/Y\). Equation (22) pays for its amplification
by the endpoint recurrence. Its "final normalized source tolerance" must
retain the supplied source's thin-tube allowance as well as its prediction
allowance; the inherited Taylor tolerance is the minimum of those two.
With this unchanged interpretation, (22) supplies the required slack.

The additive bounds give the target's
\(\Pr(\text{scientific failure})+Re^{-cn}+\rho\), with room in
the \(\rho\) allocation. The inherited physical comparison then
applies to the finite rank-list parameters, uniformly over the supplied
time interval, sphere, and frozen endpoint. This is a conditional use of
that physical theorem, not a new audit of its underlying scientific event.

## 6. Precision, exact replay, and resource boundary

All relevant logarithms are local:
\(\log z+\log\mathcal M+\log(n+R+P)\le C\chi\), and
\(T_G^2=O(\chi+\log(1/\rho))\). Equations (17), (20)--(22),
including (21a), contain a fixed number of products and minima. Choosing
dyadics within a fixed factor below their bounds therefore gives (23).
The sampler bit length, numerical coefficient words, exact accumulation
with its \(\log n\) term, and the bounded-degree exact dyadic affine
products all have allowance \(C[\chi+\log(1/\rho)]\).

The source's local interpolation/physical-arithmetic estimates are used
here, not the core's global \(R\chi\) sensitivity estimate. Real
activation/data evaluators, their descriptions, input precision, and
their actual working space remain charged interfaces. This component
does not bound them solely in terms of \(\beta\).

For exact acquisition let \(h_* = \min(h,h_t)\) and
\(\alpha_{\rm acq}=\rho/16\). At each update, conditional on all
row packets and earlier scalar marks, the empirical pair is fixed and
the fresh latent scalar Gaussian is independent. This remains true for
innovation contractions: their fresh row mark is already in the packet
array, while their scalar noise is separate. For either grid \(h_a\),
the assigned Gaussian boundary lemma gives

\[
 \Pr\{\operatorname{dist}(A_a+\eta E_a,
 h_a(\mathbb Z+1/2))\le v\mid\text{past and packets}\}
 \le2v(h_a^{-1}+\eta^{-1}).
\]

Take \(\zeta=\alpha_{\rm acq}h_*/(64(P+1))\).
Condition (21a) bounds finite scalar-mark error by \(\zeta\), and
the source sampler-tail event is below \(\alpha_{\rm acq}/2\).
The same \(4\zeta\)-boundary union proof works over both kinds of
updates because \(h_*\le h_a\le\eta\). A rounded selected metric
with entry error at most \(\zeta/(2q^2B_f^2)\), where \(B_f\)
is the finite field-coordinate cap, changes each acquired pair by at most
\(\zeta\). Here \(\log B_f=O(p_{\rm loc})\).

Inductively equal prefixes give identical selected row bits at their
creation-time arguments. Exactness of the metric on the completed source
then applies, and both pre-rounding values stay in the same cell. Every
scalar is reproduced literally. Dependence of the selected metric on all
future source fields and scalar noise is harmless: the deterministic
metric error bound is used only after the source's boundary event is
proved, without conditioning on that selected metric. The acquisition
failure can be added to the earlier physical failure within the remaining
\(\rho\) slack if a joint source-and-replay conclusion is desired.

The retained count is consequently \(O(R^2p_{\rm loc})\): at most
\(O(R)\) selected packets of dimension \(O(R)\), their quadratic
metric, \(O(R^2)\) scalar marks and acquired prefix, and the existing
coefficient/rank description. At one completed conditioning call only
its \(O(R)\) final row-combination coefficients need remain; its
\(O(R^2)\) temporary correction matrix can be discarded. Across all
calls this is quadratic, not cubic, storage. The inherited
\(K,J\le CR\) bounds and Taylor arithmetic counts cover rank weights
and interpolation scratch within the same scalar envelope. Indices and
exact rational source accumulation fit the included logarithmic words.

The assigned exact metric construction still has separate work
\(O(nR^5p_{\rm loc}^3)\) and peak bits
\(O(nRp_{\rm loc}+R^3p_{\rm loc})\), including its longer exact
rational intermediates. These are not total initialization bounds:
source generation, finite Gaussian generation, protected coefficient
solves, and actual activation/data evaluator work must also be charged.
No compact initialization peak bound is proved.

Finally, exact replay is a statement about the realized source tape.
It neither bounds the sensitivity of the expanded row circuit at a new
packet nor makes the raw proof history identical to the retained scalar
prefix. In particular marginalizing the richer history does not preserve
the Gaussian matrix posterior. The target explicitly states these limits,
and they remain outside this passing component verdict.

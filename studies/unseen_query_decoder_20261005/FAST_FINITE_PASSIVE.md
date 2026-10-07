# Passive moments for the locally precise finite source

2026-10-06. Scoped author theorem, not an independent review or a complete
resource theorem. This transports the passive statistical argument to the
finite source of FAST_FINITE_SOURCE_BRIDGE.md. No experiment, Git action,
or other-study source is used.

The passive moment construction can use the same finite iid packet prior
and the same deterministic finite training-row interpreter. No continuous
approximation to that interpreter is needed at a new packet. The Gaussian
comparison concerns only a fixed-depth passive query after training
history marks have been computed exactly as finite bit strings.

The result below retains the original scientific assumptions, full label
intersection, learned hidden layers, sphere, physical times and endpoint.
Its scientific failure shares stay fixed with width. Local numerical
tolerances may be decreased before initializing the source. The result
does not give polylogarithmic query sampling or a complete cost theorem.

## 1. Statement and numerical order of choices

Use the frozen finite source
7ef69972a213fb26b77cd1c0ed4dcbd8b7d12f9e3b06906f351f7443f79894e6,
and FAST_FINITE_POSTERIOR.md at
f3cc565c52e848611d576d877ca893964cf45a74fb35f86c0494fbe8b09413db.
The notation \(n,m,d,L,\gamma,Y,\beta,Z,R,\sigma\) is unchanged.
Write
\[
 \chi=\beta^{100L}(1+m/\gamma)Z,\qquad \epsilon=n^{-10}.    \tag{1}
\]
All normalized predictions below are divided by \(Y>0\). The zero-label
branch remains exact. Input descriptions and actual activation evaluation
work/scratch stay charged interfaces.

Let \(\mu\) be the **actual finite packet prior** of the source,
including its chosen quantized first-layer and innovation coordinates.
At a retained scalar prefix \(c\), every training history field is the
output of the actual finite interpreter with arguments \((z,c)\),
using each field's creation-time scalar arguments. These finite outputs
are the mathematical row marks in this note. They are not approximations
to a globally Lipschitz continuous row function.

Let \(\mathcal B\ge2\) be the small passive feature cap from
FAST_COMPOSITION.md, Section 7.2. One available bound is
\[
 \mathcal B\le C\beta^{110L}\sqrt{d+1}\,Z^{3/2}.           \tag{2}
\]
It follows from the supplied whole-sphere physical response event and
the source parameter accuracy. It is not a cap on earlier Taylor
coefficient fields. A smooth capped activation \(\psi_\ell\) agrees on
the physical range and obeys
\[
 |\psi_\ell|\le\mathcal B,\qquad
 |\psi_\ell'|\le a_1,\qquad |\psi_\ell''|\le a_2,\qquad
 a_1+a_2\le C(1+\beta)^2.                                \tag{3}
\]
These caps impose no bounded-activation assumption.

Choose a fixed confidence allocation \(0<\delta<1/4\).
Let \(\mathcal C\) bound the normalized readout RMS and the posterior
mean-plus-learned-displacement operator norms on the good prefix event
constructed in Section 3. It can be taken polynomial in the original
physical constants and \(\sqrt{(L+1)/\delta}\).
For clarity define a sufficient fixed-depth amplification
\[
 \mathcal P=(1+\mathcal C)
 [C(1+\mathcal B)^2(1+\mathcal C)(1+\beta)^2]^{L+2}.        \tag{4}
\]
Every use below is with an enlarged absolute \(C\).

The free numerical parameters of the finite source are chosen once,
before generating its packets and tape, also to meet Sections 4 and 6.
Their sufficient word lengths are
\[
 C\{\chi+\log\mathcal P+\log(1/\delta)\}.                 \tag{5}
\]
There is no factor \(R\chi\). This refines numerical tolerances within
the source algorithm; it does not alter a generated tape afterward.
The enlarged local certificate in the lead's composition can cover (5).

For the scalar-shadow information certificate let
\[
 K_*=\max\left\{1,\frac{P}{2\alpha}
                    \log(1+B_F^2/\eta^2)\right\},        \tag{6}
\]
where \(P\le CR^2\), \(B_F\) bounds the source pair tests, and
\(\alpha\) is a fixed confidence share. The normalized population
comparison bound proved below is
\[
 e_n=C\mathcal P\sqrt{(K_*+R+1)/n}+C\epsilon.             \tag{7}
\]
The implemented prior-block estimator has the separately counted
cross-moment error \(C\mathcal B\sqrt{R/s}\), not merely the
full-array scale in (7), with
\(s=\lfloor n/(128\widehat K_*)\rfloor\),
\(K_*\le\widehat K_*\le2K_*\), subject to the displayed sampling
width gate making \(s\) positive. It still uses width-order blocks up
to the information factor.

## 2. One source law for posterior marks and physical comparison

Use the continuous-scalar-noise, rounded shadow of
FAST_FINITE_POSTERIOR.md. Its packets still have the finite law \(\mu\).
Only scalar noise is temporarily continuous:
\[
 C_a=Q_{h_a}\left(n^{-1}\sum_i F_a(Z_i;C_{<a})+\eta E_a\right).
                                                               \tag{8}
\]
There are the two predetermined grids \(h\) and \(h_t\), both at most
\(\eta\); put \(h_{\max}=\max(h,h_t)\).
The proof of that note applies to different grids update by update,
using their minimum for the finite-noise coupling allowance.

Its scalar-boundary coupling identifies the entire finite packet array,
all acquired prefixes and all finite row fields with those of the
implemented finite source except on an allocated numerical failure.
Combine this joint coupling with FAST_FINITE_SOURCE_BRIDGE.md's
physical coupling through their common finite source. One can construct
the joint law by conditioning on that common source and sampling the
two supplied conditional couplings. This is a proof construction, not
an algorithmic posterior oracle.

Let \(\mathcal G\) denote the resulting complete event on which:

- shadow and implemented finite tapes agree;
- the finite source has the original physical Gaussian-matrix coupling;
- all local physical/cap/error conclusions hold, at every checkpoint;
- the original dense-to-center scientific event holds;
- the observable Gaussian posterior mean event of Section 3 holds.

Its probability is controlled by the inherited scientific failure at a
fixed share of \(\delta\), plus explicit numerical/TV and Gaussian
failures. None is assigned confidence \(\delta\) divided by the number
of external codes.

At a scalar prefix \(c\) of (8), let \(\pi_c\) be the finite packet-array
posterior and \(\nu_c\) its common one-row marginal. The finite-prior
entropy identity is
\[
 D(\pi_c\Vert\mu^{\otimes n})
 =D(\pi_c\Vert\nu_c^{\otimes n})+nD(\nu_c\Vert\mu).
                                                               \tag{9}
\]
It follows by expanding the log density ratio and using the one-row
marginals. The all-prefix information event gives both terms at most
\(K_*\). Exchangeability follows from the source's symmetric empirical
pair operations and rowwise deterministic formulas.

The raw physical history used in the coupling is not the retained
scalar prefix. Given that raw history the matrices are independent
Gaussian posteriors. Given only \(c\) they are generally mixtures.
There are also two distinct scalar-prefix random variables: the
physical construction's \(C^{\rm ph}\) and the shadow's \(C^{\rm sh}\).
They agree on \(\mathcal G\), but the latter need not be measurable
in the former's raw history. The proof keeps the Gaussian calculation
under the physical marginal law and the finite-prior entropy calculation
under the shadow marginal law. Section 7 joins their high-mass intervals
on matching prefixes; it never conditions a Gaussian assertion on
\(C^{\rm sh}\).

## 3. Raw Gaussian means and their finite-history substitutes

At any completed physical call let \(\mathcal H\) contain raw matrix
answers, queries, finite fields and the safe conditional augmentations
from the source bridge. It excludes raw answer noise and future marks.
The augmentation cancels from the matrix likelihood. Thus
\[
 \overline W_\ell=\mathbb E[W_\ell(0)\mid\mathcal H]
\]
is the ordinary two-orientation posterior mean.

For each layer, the process
\(\mathbb E[\|W_\ell(0)\|_{\rm op}^2\mid\mathcal H_j]\) is a
nonnegative martingale. The initialized Gaussian operator norm has
bounded second moment, by the sphere-net Gaussian bound described in
FAST_COMPOSITION.md. The first-crossing inequality and conditional
Jensen give, simultaneously at all completed training prefixes,
\[
 \|\overline W_\ell\|_{\rm op}
       \le\sqrt{C(L+1)/\delta}                            \tag{10}
\]
outside a fixed allocated failure. No conditioning on a small realized
matrix norm is inserted in the Gaussian likelihood.

The finite learned matrix \(D_\ell(c,\theta)\), at within-patch time
\(\theta\in[0,1]\), is its actual stored rank list. Its operator norm
is bounded by source accuracy and the strict-slack physical guard,
uniformly in \(\theta\). Thus (10) bounds
\(\overline W_\ell+D_\ell\). The normalized readout is bounded similarly.

Now compute a finite posterior mean substitute using the acquired
physical pair table and the finite query/answer fields. The exact raw
mean is
\[
 \overline W=YCV^T/n+UDX^T/n+UEV^T/n,                     \tag{11}
\]
with the \(\sigma^2\)-gapped inverse and Sylvester coefficients from
NOISY_TWO_ORIENTATION_TRANSCRIPT.md. Replace raw \(X,Y\) by their
stored finite versions and compute those protected coefficient maps
to local precision on the acquired pair table. Add the actual learned
rank list. The result is
\[
 \widetilde M_\ell
       =T_\ell A_{\ell,0}(c,\theta)S_\ell^T/n.            \tag{12}
\]
The history columns \(S_\ell,T_\ell\) consist solely of named finite
fields. Concatenate the columns needed in (11) with the input/output
factors of the learned rank list. Their number is at most \(CR\).
The matrix \(A_{\ell,0}\) is finite and prefix-computable; it contains
no raw physical answers inaccessible to the source.

Let \(b\) bound physical query/answer RMS and let \(\mathcal A\) be a
common cap for local raw coefficient norms, rank weights, dimensions,
history Gram norms, normalized readout coefficients and \(\sigma^{-1}\).
The source ledger gives
\[
 \log\mathcal A\le C\chi.                                \tag{13}
\]
This cap is independent of subsequently reducing \(\eta,h,h_t\).

On \(\mathcal G\), old finite answers differ from their raw ancestors
by at most \(h_y\) coordinatewise. The input moment error is bounded
locally by
\[
 e_{\rm raw}
 =C\{(b+1)h_y+h_y^2+\eta(T_G+1)+h_{\max}+\epsilon_c\},
                                                               \tag{14}
\]
with dimension factors included in a power of \(\mathcal A\).
The one-call gapped identities imply
\[
 \|\widetilde M_\ell-(\overline W_\ell+D_\ell)\|_{\rm op}
                  \le\mathcal A^C e_{\rm raw}.           \tag{15}
\]
To verify the norm conversion, replacing one answer block in (11)
costs at most \(\sqrt R h_y\) for that block divided by \(\sqrt n\);
the other block has norm at most \(\sqrt R b\).
Each inverse/Sylvester coefficient changes by a fixed polynomial in
\(R,b,\sigma^{-1}\) times its current moment error.
Subtract each of the three products separately. The learned rank
matrix is identical on both sides. This proves (15) without comparing
old answers at different histories.

All time dependence in (12) lies in the finite scalar rank weights.
Old fields remain fixed. There is one local mean reconstruction per
passive layer, not one reconstruction error for every earlier call.

## 4. Common Grams for finite marks

Acquire all pairs needed by the master histories in (12); this is
the existing \(CR^2\) pair schedule. Scaled copies such as division
by \(Y\), or linear combinations giving the readout at a time, can
instead be formed from this complete pair table by scalar algebra.
The gate \(Y\ge n^{-1}\) makes these scaling logarithms part of \(\chi\).

The scalar-shadow noise martingale in FAST_FINITE_POSTERIOR.md gives
at every good prefix
\[
 |\nu_c(F_a)-c_a|\le\eta\sqrt{P/\alpha}+h_{\max}/2.
\]
For a fixed conditional failure share \(\rho_G>0\), its corresponding
posterior empirical event has mass at least \(1-\rho_G\). Use the
slightly larger error allowance
\[
 e_G=\eta\max\{\sqrt{P/(\alpha\rho_G)},T_G+1\}
                                      +h_{\max}/2.      \tag{16}
\]
All pair tests retain creation-time arguments, so these statements
refer to the exact same finite marks used in (12).
Under the physical construction the ordinary finite scalar marks are
bounded by \(T_G+1\), and their pair tests are the actual finite empirical
pairs. Thus the same error allowance controls that empirical pair table
on \(\mathcal G\), without invoking a shadow posterior inside the
physical law.

For any master history \(S\) with at most \(CR\) columns, let
\(Q_{S,\rm obs}\) be its retained symmetric pair table and define
\[
 Q_S^*=\tau I+(Q_{S,\rm obs}+\tau I)_+.                   \tag{17}
\]
Choose \(CR e_G\le\tau/8\). On the good prefix event,
\(Q_S^*=Q_{S,\rm obs}+2\tau I\), it dominates both
\(\nu_c(SS^T)\) and, on the posterior empirical event,
\(S^TS/n\), and its distance from either is at most \(3\tau\).
The globally protected definition has floor \(\tau\).

Write the whitened row marks and coefficient as
\[
 U_\ell=(Q_{T_\ell}^*)^{-1/2}T_\ell,\qquad
 V_{\ell-1}=(Q_{S_\ell}^*)^{-1/2}S_\ell,\qquad
 A_\ell=(Q_{T_\ell}^*)^{1/2}A_{\ell,0}(Q_{S_\ell}^*)^{1/2}.
                                                               \tag{18}
\]
Here \(S_\ell,T_\ell\) in the row formulas denote their column-value
vectors at one row. Empirical/population raw second moments of each
whitened mark vector are at most identity on the indicated events.

If \(q\) caps the two empirical Grams, the elementary square-root
subtraction estimate gives
\[
 \|A_\ell\|\le\|\widetilde M_\ell\|
       +2\|A_{\ell,0}\|\sqrt{3\tau(q+3\tau)}.             \tag{19}
\]
Indeed use the partial-isometry factorizations of \(S/\sqrt n,T/\sqrt n\)
and \(\|P^{1/2}-Q^{1/2}\|\le\sqrt{\|P-Q\|}\).
The normalized readout coefficient has the analogous bound: its squared
common-coordinate norm is its empirical RMS squared plus at most
\(3\tau\) times its raw coefficient norm squared.

Section 7 supplies positive physical conditional mass to \(\mathcal G\)
at every good common prefix. Choose one compatible physical extended
array there. Its empirical Gram satisfies (16), so (10), (15), (19)
bound \(A_\ell(c,\theta)\). This matrix depends only on \(c,\theta\);
the resulting bound is therefore deterministic at that prefix and
uniform in time. Shadow population/empirical Gram control is then used
with the same coefficient. This is an existence-of-a-good-physical-array
argument, not conditioning the Gaussian posterior on a norm event or
identifying the two scalar posteriors.

The forward-query columns \(V\) of a Gaussian history are included in
\(S_\ell\). If \(J_\ell\) selects them, the variance matrix is
\[
 P_\ell=(\sigma^2I+J_\ell Q_{S_\ell}^*J_\ell^T)^{-1/2}
                    J_\ell(Q_{S_\ell}^*)^{1/2},
 \qquad \|P_\ell\|\le1.                                 \tag{20}
\]
The inequality follows by multiplying by its transpose.
Replacing the empirical forward Gram by this dominating table changes
the scalar conditional variance by at most
\[
 3\tau\,c_{\rm in}/\sigma^2.                             \tag{21}
\]
This is the resolvent identity with
\(v^T(\sigma^2I+Q_V)^{-1}v\le c_{\rm in}\); no small empirical
eigenvalue is required.

A concrete valid choice order is: bound \(\mathcal A,q,\mathcal P\)
first, then choose \(\tau>0\) so
\[
 2\mathcal A\sqrt{3\tau(\mathcal A+3\tau)}
                  \le\epsilon/(64\mathcal P),\qquad
 3\tau\mathcal B^2/\sigma^2
                  \le[\epsilon/(64\mathcal P)]^2,       \tag{22}
\]
and next decrease source scalar/grid/coefficient tolerances so (16)
and
\[
 \mathcal A^C e_{\rm raw}
                  \le\epsilon/[64\mathcal P(1+\mathcal B)]
                                                               \tag{23}
\]
hold. Each logarithmic inverse is bounded by (5).
This is not circular: raw coefficient caps and \(\sigma\) were fixed
before \(\eta\). The scalar-shadow and finite-replay sampler allowances
are then imposed as in the source bridge. No label or scientific width
condition is strengthened.

## 5. Passive Gaussian normal form for this finite array

Condition first on a complete physical history \(\mathcal H\) in the
good observable range. Append a passive forward query, using every
hidden initialized matrix once and fresh physical Gaussian answer noise
of level \(\sigma_q>0\). It may equal \(\sigma\), or be smaller by the
local precision necessary for normalized error \(\epsilon\).

For input field \(q\), the exact answer covariance has the form
\[
 \Gamma(q)=\beta(q)I-K(q),\quad
 0\preceq K(q)\preceq\beta(q)I,\quad
 \operatorname{rank}K(q)\le R,
\]
\[
 \beta(q)=\sigma_q^2+\|q\|_2^2/n
       -(V^Tq/n)^T(\sigma^2I+V^TV/n)^{-1}(V^Tq/n).
                                                               \tag{24}
\]
The source conditional augmentations do not change these formulas.
Conditional centered matrices in different layers remain independent;
the passive incoming field is independent of its next layer's centered
matrix.

Couple the exact covariance action to \(\sqrt{\beta(q)}\,g\).
Only at most \(R\) eigendirections change, so
\[
 \mathbb E\|\Gamma(q)^{1/2}g-\sqrt{\beta(q)}g\|_2^2/n
       \le(\sigma_q^2+\|q\|_2^2/n)R/n.                   \tag{25}
\]
Higher exact posterior matrices propagate RMS errors with factor at
most \(\sqrt{1+\|\overline W_\ell+D_\ell\|^2}\), because their
centered covariance is dominated by the Gaussian prior. Use one
layer hybrid at a time and the global Lipschitz caps (3).
The normalized output comparison costs at most
\(C\mathcal P\sqrt{R/n}\). This is conditional at each query, not a
simultaneous query-noise realization.

In the same layer hybrids replace the mean mixer by (12) and the
variance Gram by (17), always comparing at the identical current input
field. Equations (22)--(23) make this additional fixed-depth RMS error
at most \(C\epsilon\). For the variance replacement use the same
Gaussian and \(|\sqrt a-\sqrt b|\le\sqrt{|a-b|}\): the squared
budget in (22) pays explicitly for this strong comparison. All higher
layers in that hybrid still use their exact posterior matrices, whose
RMS propagation was just bounded. The later statistical moment
comparison uses the stronger weak variance estimate, but it is not
substituted for a strong comparison here. Neither estimate uses an
expanded source-row sensitivity.

The resulting array recursion depends only on its finite training
marks, scalar prefix, external query and fresh independent Gaussian
array. Denote this common conditional output kernel by \(\mathsf K\).
It is defined for both training laws, using the same protected formulas
and caps off the good events. Matching finite arrays and prefixes give
identical outputs if the same fresh Gaussians are supplied. The physical
comparison just proved concerns the physical marginal of this kernel;
it does not assert any shadow posterior law for the physical array.

The mathematical population reference for the shadow marginal is
\[
 h_\ell=\psi_\ell\!\left(
 U_\ell^T A_\ell b_{\ell-1}
       +\sqrt{\sigma_q^2+c_{\ell-1}
                         -\|P_\ell b_{\ell-1}\|^2}\,g_\ell\right),
\]
\[
 b_\ell=\mathbb E_{\nu_c,g}[V_\ell h_\ell],\qquad
 c_\ell=\mathbb E_{\nu_c,g}[h_\ell^2].                    \tag{26}
\]
Choose master mark systems so \(V_\ell\) contains the next layer's
incoming factors and the final readout factors where needed.
Every variance in the exact reference is feasible by the upper Gram
bound; numerical contexts use
\(\sigma_q^2+\max\{0,c-\|Pb\|^2\}\).

The first layer is the finite initial first-row mark plus the actual
first-layer learned rank sum applied to the external input. It has no
posterior hidden-matrix operation. It is a deterministic capped row
test in the same finite marks. The readout is a final cross moment
with its normalized common-coordinate coefficient. Both are covered
by the same upper Gram argument.

Thus (26) uses the actual finite history marks.
Their discontinuity as functions of hypothetical continuous roots is
irrelevant. Only the newly introduced passive Gaussian is continuous
in this mathematical reference. Section 6 compares the shadow marginal
of \(\mathsf K\) with (26); Section 7 joins it to the physical comparison.

## 6. Empirical and finite numerical moment propagation

By (9), the packet-array posterior has relative entropy at most
\(K_*\) against \(\nu_c^{\otimes n}\). The self-normalized entropy
bound in DENSE_BUDGET_GEOMETRY.md therefore gives, for a fixed bounded
test \(G\), \(|G|\le\mathcal B\), and common normalized mark \(V\),
\[
 \mathbb E_{\pi_c}\!\left[
 \left\|n^{-1}\sum_iV_iG_i-\nu_c(VG)\right\|^2
 \mathbf1_{\{n^{-1}\sum_iV_iV_i^T\preceq I\}}\right]
       \le C\mathcal B^2(K_*+R+1)/n.                     \tag{27}
\]
Its proof uses only second moments and relative entropy, so a finite
packet law satisfies exactly the same hypotheses. The scalar test
\(G^2\) gives \(C\mathcal B^4(K_*+1)/n\).

Apply (27) to the tests at the deterministic reference parameters of
(26). Fresh array query Gaussians add conditional cross-moment variance
at most \(\mathcal B^2R/n\) and scalar variance at most
\(\mathcal B^4/n\). Earlier random incoming moments are handled by
the weak recursion, not inserted as random tests into (27).

If \(x_\ell,y_\ell\) are cross- and second-moment errors, integration
of the fresh Gaussian before comparison gives
\[
 \begin{split}
 x_\ell&\le a_1\mathcal C x_{\ell-1}
       +\tfrac12a_2(y_{\ell-1}+2\mathcal Bx_{\ell-1})+e_\ell,\\
 y_\ell&\le2\mathcal B a_1\mathcal C x_{\ell-1}
       +(a_1^2+\mathcal B a_2)
                      (y_{\ell-1}+2\mathcal Bx_{\ell-1})+z_\ell .
 \end{split}                                             \tag{28}
\]
For the variance dependence, differentiate the Gaussian expectation
and integrate by parts twice; its derivative is half the expectation
of the second derivative. Add a common positive variance and pass
to zero for the boundary case. Upper Grams give RMS mean error at
most \(\mathcal Cx\), \(\|b\|\le\mathcal B\), and
\(\|\nu(Vq)\|\le\|q\|_{L^2(\nu)}\). These facts prove (28).
Minkowski and (27) give the posterior RMS scale (7) on the empirical
Gram event. Its complement has the fixed conditional mass \(\rho_G\).

### Finite query arithmetic without a global row approximation

On a prior packet sampled from finite \(\mu\), evaluate all training
history marks by the exact same finite interpreter as the source.
There is no rounding comparison in this step: its result is the
definition of the mathematical finite mark.

Whitening, current mean/variance coefficients, the first-layer input
contraction, and each fresh passive activation are new local operations.
Their operands have explicit finite caps with logarithms bounded by
\(C(\chi+\log\mathcal P+\log\delta^{-1})\), and protected matrix
floors are \(\tau,\sigma^2,\sigma_q^2\).
Compute these local quantities, including each final row integrand,
to absolute error \(\epsilon_{\rm row}\), with
\(\log\epsilon_{\rm row}^{-1}\) bounded by (5).

Use an independent finite sampler for each new passive Gaussian.
It can approximate the continuous expectation uniformly in every
guarded context without comparing continuous training-row maps.
Under its coupling, on \(|g|\le T\),
the feature error is at most \(a_1\sqrt{\sigma_q^2+\mathcal B^2}\epsilon_g\)
plus local arithmetic/value error. On the tail the capped features
differ by at most \(2\mathcal B\).
The training mark multiplier is bounded by its numerical cap.
Choose \(T^2,\log\epsilon_g^{-1}\) and local precision to make the
**entire row integrand expectation** error at most
\(\epsilon/(64\mathcal P)\), uniformly in the finite training packet
and guarded context. Only local cap logarithms enter. This deterministic
bias estimate has no external-code union factor.

For the implemented finite row integrand, its coordinate second moment
under \(\nu_c\) is at most a fixed multiple of \(\mathcal B^2\)
for a cross moment, and \(\mathcal B^4\) for a second moment.
Indeed subtract its uniformly small local error from the corresponding
exact normalized-mark integrand and use the upper Gram bound.
Chebyshev on \(\nu_c^{\otimes s}\), followed by
\[
 \|\nu_c^{\otimes s}-\mu^{\otimes s}\|_{\rm TV}
       \le\sqrt{sK_*/(2n)},
\]
therefore gives the same prior-block median guarantee, with enlarged
absolute constants. Finite new Gaussian marks are appended identically
to both product laws and add no relative entropy.

In particular, the coordinatewise block estimates, assembled in Euclidean
norm, have cross-moment error at most
\(C\mathcal B\sqrt{R\widehat K_*/n}\); scalar second-moment error
is at most \(C\mathcal B^2\sqrt{\widehat K_*/n}\).
Use \(\widehat K_*\le2K_*\) in (28). The resulting normalized
decoder error relative to its population target is at most
\(C\mathcal P\sqrt{(R+1)(K_*+1)/n}+C\epsilon\).
The extra vector factor cannot be removed by the full-array entropy
estimate (27), which concerns a different estimator.

The estimator thus targets its actual finite row integrand. Its
deterministic local expectation bias is then added in (28), whose
reference remains the smooth Gaussian map (26). No differentiability
of finite rounding, finite Gaussian laws or the old row interpreter
is asserted or needed. Moment projection guards are nonexpansive.
The finite fixed-context tests required by the inherited generator
remain exact tests of this implemented row algorithm.

## 7. Dense center, all prefixes, and physical external codes

Let the inherited deterministic dense center be \(f_0(t,v)\), and let
\(b_n\) be its original dense-pair upper certificate at the chosen fixed
confidence share. Conditional on the complete scientific good event,
the coupled source dense trajectory is within \(b_n\) of this center
uniformly over the whole sphere and all times.

### Two scalar filtrations and one common auxiliary kernel

On the joint training coupling apply the first-crossing inequality
separately to the nonnegative martingales
\[
 \Pr(\mathcal G^c\mid C^{\rm ph}_{\le j}),\qquad
 \Pr(\mathcal G^c\mid C^{\rm sh}_{\le j}).
\]
Append a terminal reveal of \(\mathbf1_{\mathcal G^c}\) to both.
Outside probability at most \(2\Pr(\mathcal G^c)/q_0\), the actual
joint sample is good and every prefix in both filtrations has
conditional good mass at least \(1-q_0\). Take, for example,
\(q_0=1/64\), and allocate the inherited scientific failure a fixed
sufficiently small share of \(\delta\) before applying its theorem.
Intersect with the shadow's all-prefix entropy and scalar-noise events.
Only completed-call prefixes are used for Gaussian passive queries;
the scalar martingales may include the intervening scalar updates.

Fix one common good prefix \(c\) and an input/time. Under the physical
marginal, \(\mathcal H\) contains \(C^{\rm ph}=c\); the conditional
Gaussian calculation of Section 5 can therefore be integrated over
the physical raw histories at that prefix. The source/dense-center
event loses conditional mass at most \(q_0\). Source parameter
accuracy and physically inactive query caps put the exact passive
physical query within \(b_n+CY\epsilon\) of \(f_0(t,v)\), except for
an additional fixed small conditional loss. Fresh passive Gaussian
RMS tails cost at most \(CL e^{-cn}\), uniformly in a fixed query,
conditional on each good observable physical history; choose their
scale so their perturbation contributes \(CY\epsilon\).
Equation (25), (22)--(23), and Markov's inequality then imply for the
physical marginal of \(\mathsf K\) a high-mass interval
\[
 I_{\rm ph}=[f_0(t,v)-r_{\rm ph},\,f_0(t,v)+r_{\rm ph}],
 \qquad
 r_{\rm ph}=b_n+CY\mathcal P\sqrt{R/n}+CY\epsilon.
\]
Enlarge the fixed constant in this radius so its conditional failure
probability is \(q_{\rm ph}\le1/8\).
This is solely a physical-marginal assertion. In particular no raw
Gaussian history is conditioned on \(C^{\rm sh}\).

Under the shadow marginal at \(C^{\rm sh}=c\), the finite-prior entropy
argument (27)--(28) and its empirical Gram event instead give for
\(\mathsf K\) the interval
\[
 I_{\rm sh}=[Yd_\nu(c;t,v)-r_{\rm sh},\,
             Yd_\nu(c;t,v)+r_{\rm sh}],\qquad
 r_{\rm sh}=CY\mathcal P\sqrt{(K_*+R+1)/n}+CY\epsilon,
\]
with conditional failure \(q_{\rm sh}\le1/8\).
All constants here are fixed independently of the external code count.

To join the assertions, append fresh independent Gaussians to the
joint training coupling and apply the same kernel \(\mathsf K\) on
both sides. Their auxiliary outputs are identical on \(\mathcal G\).
For this prefix write
\[
 p_{\rm ph}=\Pr(C^{\rm ph}=c),\quad
 p_{\rm sh}=\Pr(C^{\rm sh}=c),\quad
 m_c=\Pr(\mathcal G,C^{\rm ph}=c)
     =\Pr(\mathcal G,C^{\rm sh}=c)>0.
\]
The two good-prefix properties imply
\(m_c\ge(1-q_0)p_{\rm ph}\) and
\(m_c\ge(1-q_0)p_{\rm sh}\).
The common matched mass outside either interval is at most
\[
 q_{\rm ph}p_{\rm ph}+q_{\rm sh}p_{\rm sh}
 \le\frac{q_{\rm ph}+q_{\rm sh}}{1-q_0}m_c<m_c.
\]
Thus the two intervals intersect on positive matched mass. This proves
\[
 |Yd_\nu(c;t,v)-f_0(t,v)|
                  \le b_n+Y(e_n+C\epsilon).             \tag{29}
\]
This deterministic implication applies separately to every query on
the same prefix event. It requires no union of fresh-query Gaussian
failures over the sphere or over the code grid. The argument uses
conditional high mass supplied by two global martingales, not a
total-variation bound divided by the probability of a rare prefix.

### Finite query seeds and physical extension

Now use the physical external grid of FAST_PHYSICAL_QUERY_GRID.md.
Its logarithmic code count is \(C(d+1)\Theta_{\rm local}\), and its
rounding error is paid using the true dense prediction's input/time
Lipschitz bounds, not continuity of the decoder.
Independent stage seeds and the reachable-context argument of
FAST_UNIFORM_QUERY.md union finite estimator failures over these
codes. Tightening the quantified numerical/generator error is allowed.
The inherited scientific/source event keeps its fixed confidence.

At each code, (28) and the finite block estimates approximate the same
\(d_\nu\) in (29). Append the same independent query seeds to the
three-way coupling of Section 2. On its matching event the shadow and
implemented finite decoder execute exactly the same deterministic
algorithm. Projecting the resulting **whole final code-accuracy
event**, including all prefixes, to the finite-source marginal proves
the claimed high probability there. One could equivalently apply the
whole-law bound of FAST_FINITE_POSTERIOR.md to that final event.
Neither argument conditions a total-variation estimate on a rare
prefix. The finite metric replay event identifies compact acquisition.

Finally round an arbitrary unseen input/time to its code in the already
acquired patch, and add only the physical reference change. Include
both patch endpoints and the frozen terminal state. For an independent
dense reference trajectory satisfying the same center certificate,
\[
 \sup_{t\in[0,\infty],\,\|v\|=1}
 |\widehat f(t,v)-f_n^{\rm independent}(t,v)|
       \le 2b_n+CY\mathcal P\sqrt{(R+1)(K_*+1)/n}+CY\epsilon.
                                                               \tag{30}
\]
At fixed admissible problem parameters, the additional term is a fixed
logarithmic power times \(n^{-1/2}\). Its absorption into the original
certificate uses precisely the inherited explicit eventual-width
comparison with the certificate's positive
\(\exp(CY^2\sqrt{\log(en)})\) factor. No new effective polynomial
scientific-width claim follows.

The only fresh Gaussian conditional failure requirement here is a
fixed inequality such as \(CL e^{-cn}<1/64\). No unquantified source
theorem is invoked with a confidence shrinking as the grid grows.

## 8. Boundaries and provenance

The source law, posterior finite prior, finite row interpreter, pair
table, conditional mean substitute and passive estimator above are the
same objects throughout. Additional precision in (22)--(23) is selected
before source initialization. No future training field, private metric,
population expectation or dense matrix is supplied to the query algorithm.
Computing old row-response formulas at a supplied scalar prefix does not
reexecute scalar training.

During bounded reconstruction the prior-block vector sampling factor was
corrected explicitly: (7) and (29) concern the population comparison,
whereas the implemented decoder in (30) includes the larger
\(\sqrt{(R+1)(K_*+1)/n}\) term. This correction changes neither
the finite algorithm nor its local precision and storage interfaces.

This author argument closes the passive law/geometry transport under
the named physical and dense-center interfaces. It does not supply a
new generator theorem, eliminate width-order statistical blocks, or
complete the total resource ledger. All actual primitive costs and
input encoding lengths remain explicit interfaces.

Complete new inputs read were FAST_FINITE_POSTERIOR.md,
FAST_PHYSICAL_QUERY_GRID.md, FAST_UNIFORM_QUERY.md, FAST_COMPOSITION.md
and DENSE_BUDGET_GEOMETRY.md, together with the previously complete
RECALIBRATION_FREE_MOMENTS.md and finite-source inputs.
No linked other-study source or review was fetched.
Required research/proof instructions and the authorized canonical
notation fallback remained current. Only FAST_FINITE_PASSIVE.md was
written in this bounded continuation.

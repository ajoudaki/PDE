# Independent check of the dense-budget probabilistic bridge

2026-10-06. Frozen-input mathematical reconstruction; no experiments or
changes to the construction.

**PASS for the scoped bridge with the parameterwise precision repair
proved in Section 6 below.** Candidate Sections 2, 4, 5, 6 and 8 give
a valid source-to-passive-normal-form and posterior-to-all-query bridge,
conditional on the physical/source guarantees explicitly supplied in the
frozen inputs and on the stated acquisition, calibrated-law, numerical
compiler, cubature, and dense-pair-center interfaces. The resulting
statistical error is a fixed power of `log(en)` divided by `sqrt(n)`;
there is no required `n^(-1/4)` loss. This is not a PASS for the complete
decoder or its counted numerical implementations. In particular, the
underlying dense-pair certificate defining `b_n` is not among these inputs.

**FAIL for an unqualified application of the frozen candidate's
deterministic-rounding sentence to a privately selected numerical
prefix.** A numerical acquisition can depend on private packets beyond
the ideal prefix. Its output need not be a deterministic rounding of
that ideal prefix. The supervisor specifically supplied this interface
issue during the check. Section 6 proves the proposed repair, with no
new statistical or rate assumption: the final deterministic comparison
holds for every numerical prefix within the certified approximation
radius. The candidate must state this quantifier before it covers that
acquisition interface. This is a repairable application gap, not a
counterexample to the source-to-decoder rate.

The reconstruction below makes three choices explicit: preserve the
observable-prefix filtration when using Gaussian laws; take the variance
history Gram from the same enlarged input history used by the mean; and
use success events through posterior mass or indicators, without
reconditioning a Gaussian or entropy identity on success.

## 1. Scope, unavailable material, and frozen inputs

I read all five assigned inputs completely, and no linked scientific
source, study history, prior review, README, other study, or Git history.
The shared `AGENTS.md`, the `investigate-conjectures` skill and its
research-contract/adversarial-audit references, and the
`solve-math-rigorously` skill were read. The one prescribed attempt to
read `/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`
returned `Permission denied`. Accordingly this report keeps the supplied
notation, defines additional symbols locally, and does not claim access
to that skill or its neural-network reference.

The source construction and its inherited analytic/physical good events
are supplied hypotheses of this check. The finite-precision acquisition,
existence and computation of a certified calibrated law, and simultaneous
finite-seed cubature are separate interfaces, not proved here. The
information and posterior-maximal claims needed below can be reconstructed
from the displayed scalar observation model, so their omitted linked
notes do not create an additional assumption in this bridge.

SHA256 hashes of the frozen scientific inputs:

| File | SHA256 |
|---|---|
| `DENSE_BUDGET_DECODER_CANDIDATE.md` | `e34fbff0633d020010256a72beaf313c216afe789f51720f3c6df525c93bffdc` |
| `DENSE_BUDGET_GEOMETRY.md` | `50950e2df4d5d9e9eb20201769da7afee39ef2dee389f1ab97744a25ef88df0e` |
| `PHYSICAL_NOISY_PROGRAM_BRIDGE.md` | `b20650d28fe3a4c8ebc76105bd5f4347503bd0485bcced588dd1680bc65cadc6` |
| `NOISY_TWO_ORIENTATION_TRANSCRIPT.md` | `0c422a0c06b00b606c220a2631482ecab81911857aa05620ed395ce134bf8aac` |
| `SOURCE_SUPREMUM_EXTENSION.md` | `8623e2d8adaf3b730274dd704fcbd44533a67fe67d47e18ce38701b7d6cb6a6f` |

## 2. Finite source, scalar information, and physical caps

Write \(\|v\|_{2,n}=\|v\|_2/\sqrt n\). The supplied physical
source has \(R\le C\log^8(en)\) fields/calls and at most
\(P\le CR^2\) scalar averages, through \(T=C\log(en)\), followed
by its frozen output tail. Its completed states and passive predictions
have any prescribed inverse-polynomial error on one training good event,
with a uniform conditional fresh-query failure bound. This statement,
including its uniformity in requested time and input, is used as supplied.

Adding all pair products of the named physical factors still uses
\(O(R^2)\) observations. Each field keeps its older scalar arguments,
so acquiring a pair after both fields exist does not change the field.
Before scalar perturbation these pairs are measurable functions of the
observable matrix transcript and reveal no additional matrix information.
The same assertion would not be justified for separately revealed raw
oracle noises; those remain hidden.

For clarity, let \(M_F\) bound all capped retained row tests, reserving
\(B\) for the much smaller passive-feature cap below. The scalar model is

\[
 C_r=n^{-1}\sum_i F_r(Z_i;C_{<r})+\eta E_r,
 \qquad |F_r|\le M_F,
\]

with iid prior packets and independent standard Gaussian scalar noises.
The source gives polynomial bounds in \(\log n\) for \(P\),
\(\log M_F\), and the logarithms of all circuit sensitivities. Choose
\(\log(1/\eta)\) of this same type, after the other tolerances.

At a fixed earlier prefix, the next empirical average is in
\([-M_F,M_F]\). The conditional entropy of its noisy observation is
at most that of a Gaussian with variance \(M_F^2+\eta^2\), whereas
its entropy conditional on all packets is the entropy of \(\eta E_r\).
The mutual-information chain rule therefore gives

\[
 I(Z;C_{1:P})\le H:=\frac P2\log(1+M_F^2/\eta^2)
                    =\operatorname{polylog}(n).
\]

For the nested ideal-prefix filtration, put
\(K_j=D(\pi_{C_{1:j}}\Vert\mu^{\otimes n})\).
Convexity of relative entropy and the posterior-mixture identity make
\(K_j\) a nonnegative submartingale. Its terminal expectation is the
mutual information above. The first-crossing bound gives
\(\Pr(\max_jK_j>H/\alpha)\le\alpha\).
Exchangeability is preserved by the symmetric scalar averages, and
relative-entropy tensorization gives
\(nD(\pi_c^1\Vert\mu)\le K(c)\).

Similarly, \(\mathbb E[\sum_{r=1}^P E_r^2\mid C_{1:j}]\)
is a nonnegative martingale with initial expectation \(P\). With
outer failure at most \(\alpha\), it is at most \(P/\alpha\)
at every prefix. Conditional Markov then bounds the posterior probability
that the whole acquired scalar-noise vector exceeds any chosen fixed
multiple of \(\sqrt{P/\alpha}\). Thus all acquired raw pair moments
are within \(\eta\operatorname{polylog}(n)\) of the retained values
on a posterior event with any allocated fixed failure probability.
An entrywise bound must be multiplied by the history dimension to obtain
an operator-norm bound; that dimension is polylogarithmic.

For every actual physical preactivation, the supplied complex-time
interface gives a disk of radius \(r=c/\sqrt{\log(en)}\) on which
its imaginary part is bounded by a fixed constant \(s\). Reality on
the real axis makes its Taylor coefficients real. Its first sine
coefficient on the circle yields

\[
 r\,\partial_t z_i(t,x)=\pi^{-1}\int_0^{2\pi}
  \operatorname{Im}z_i(t+re^{i\theta},x)\sin\theta\,d\theta,
 \qquad |\partial_tz_i|\le4s/(\pi r).
\]

At initialization, condition on earlier layers. A fixed-input coordinate
is Gaussian with bounded variance on their RMS event. A sphere net of
mesh \(n^{-2}\) has polynomial cardinality because \(d\) is fixed;
a Gaussian tail union over this net, neurons, and fixed layers gives a
coordinate bound \(C\sqrt{\log(en)}\). The initialized operator
bounds give whole-vector input Lipschitz constant \(C\sqrt n\),
so net interpolation contributes only \(Cn^{-3/2}\) per coordinate.
Integration to \(T\), and bounded activation slope, give the claimed
uniform physical feature cap \(B=C\log^{3/2}(en)\).

A smooth cap of the activation's output is globally bounded by \(2B\)
with fixed first and second derivative bounds. It is inactive on the
physical range after a fixed enlargement of \(B\). The supplied
completed-state error, chosen with exponent greater than two, gives
coordinate error at most \(\sqrt n\,n^{-a}\); the smaller noises
are absorbed as well. No such cap is asserted for early Picard fields.
Their possibly large coordinates are handled only by their raw Grams.
If the source's passive RMS projections are retained in its original
definition, the auxiliary passive network may omit them: on the physical
comparison event the strict source radii make them inactive. The later
global comparison uses the bounded smooth coordinate caps.

## 3. Exact conditioning and removal of finite-rank covariance

Let \(\mathcal F_j\) include the independent initial row field and
the first \(j\) observable noisy matrix answers, but no raw answer-noise
roots. Predictable queries are fixed inside each chronological likelihood
factor. Multiplying the factors gives independent Gaussian posterior
matrix blocks. For one matrix, with forward query columns \(V\) and
reverse query columns \(U\), the centered posterior covariance is

\[
 \frac{\sigma^2}{n}
 (\sigma^2 I+\mathcal L_{UU^T/n}+\mathcal R_{VV^T/n})^{-1}.
\]

The two nontrivial operators commute. In their product eigenbasis,
the entry variances are
\(\sigma^2/[n(\sigma^2+a_i+b_j)]\), at most \(1/n\).
For a fresh forward input \(q\), the covariance of the answer including
its fresh noise is therefore

\[
 \Gamma(q)=\beta(q)I-K(q),\quad
 0\preceq K(q)\preceq\beta(q)I,\quad \operatorname{rank}K(q)\le R,
\]

where, with \(Q_V=V^TV/n\), \(v=V^Tq/n\), and
\(c=\|q\|_{2,n}^2\),

\[
 \beta(q)=\sigma^2+c-v^T(\sigma^2 I+Q_V)^{-1}v.
\]

The correction is supported on the reverse-input span. The explicit
mean in the transcript input is a finite sum of outer products of
physical input/answer fields; adjoining the learned displacement leaves
the form \(T B_0 S^T/n\). No history-Gram inverse is used.

For a common standard Gaussian \(g\), diagonalizing \(K\) gives

\[
 \mathbb E\|\Gamma(q)^{1/2}g-\sqrt{\beta(q)}g\|_{2,n}^2
 \le\beta(q)R/n\le(\sigma^2+c)R/n.
\]

To bound conditional means uniformly over observable prefixes, apply
the first-crossing bound to
\(\mathbb E[\|W_\ell(0)\|_{\rm op}^2\mid\mathcal F_j]\).
The Gaussian prior expectation is bounded independently of width, and
conditional Jensen bounds the squared norm of the posterior mean by this
martingale. For example, the prior expectation bound follows from
one-quarter nets of both unit spheres and the Gaussian tail of
\(u^TWv\), whose variance is \(1/n\), followed by tail integration.
Intersecting over fixed depth costs only a fixed factor. Add the supplied
bound on the finite source's learned displacement. This produces a
history-measurable bounded-mean event without conditioning the Gaussian
law on a small realized matrix norm.

Each matrix is used once in the passive forward network. Conditional on
the training transcript and preceding passive layers, the incoming
difference is independent of that layer's centered posterior matrix.
The covariance bound above gives

\[
 \mathbb E\|W_{\rm centered}v\|_{2,n}^2\le\|v\|_{2,n}^2.
\]

The mean and centered cross term vanishes, so the complete mean-plus-
centered map has squared factor at most \(C^2+1\). A layer hybrid
removes one correction, and uses shared exact upper-layer matrices to
propagate it. The fresh upper-layer observation noises cancel. Smooth
caps are globally Lipschitz, and the readout has bounded RMS on the
training event. Summing the fixed number of hybrids proves conditional
RMS prediction error \(C_L B\sqrt{R/n}\), uniformly as a bound for
each requested time and input. No simultaneous random-function coupling
is needed or asserted.

## 4. Scalar perturbation and the innovation filtration

The scalar-noised program itself does not have the posterior law in
Section 3. The prescribed source coupling is necessary. With the same
training packets, the unperturbed and perturbed summaries obey the
explicit finite-circuit bound

\[
 \max_r|\widetilde C_r-C_r|
 \le\eta nP(1+\Lambda)^P
\]

when all scalar noises have magnitude at most \(n\). The row fields,
their actual empirical moments, and all gapped matrix coefficients have
the corresponding \(\eta\exp(\operatorname{polylog}(n))\)
sensitivity. Adding the pair moments changes only the polynomial-size
instruction graph. Choose \(\eta\) after the ridge and all these
sensitivities, so the complete query perturbation is below \(n^{-10}\).
The square-root sensitivity can use the positive \(\sigma\) floor;
its logarithmic cost is still polylogarithmic.

At a requested prefix, discard the unused future training innovation
coordinates. The used training innovations are measurable functions of
the original observable prefix through the invertible formula
\(g=\Gamma^{-1/2}(y-\overline Wq)\). The original scalar-noised
prefix is a function of this original prefix and the independent scalar
noise tape. New passive innovations are independent standard Gaussians
conditional on the original observable prefix and successive passive
answers. Adding the independent scalar tape preserves this independence.
Consequently they can drive the perturbed query with the same coupling.

They need not be independent of unused future training innovations, nor
of complete initialized matrices. Conditioning on either would invalidate
the asserted fresh iid law. The candidate explicitly discards the former;
the physical error guarantee conditional on a complete training tape is
instead obtained from fresh *raw* query noises, exactly as in the source.
These are two compatible uses of the original coupling, not one enlarged
Gaussian conditioning filtration.

## 5. Common Grams, distinct bases, and the weak recurrence

Fix an ideal retained prefix \(c\), and fix an arbitrary deterministic
numerical prefix \(\widehat c\) within its certified uniform error
radius. The latter is a comparison parameter here, not an assertion
about how the actual acquisition computes it. Let \(\nu\) be the
certified calibrated law computed from this numerical prefix. Moment tolerances and
rounding imply that, on a posterior event of allocated high probability,
the empirical raw Gram and its \(\nu\)-Gram differ by at most
\(\delta_G=\eta\operatorname{polylog}(n)\) in operator norm.
Use all physical factors needed by a layer, and put

\[
 Q_S^*=Q_{S,\nu}+\tau I,\qquad
 Q_T^*=Q_{T,\nu}+\tau I,\qquad \tau\ge\delta_G,
\]

with additional fixed slack for numerical Gram error. Both empirical and
population Grams are dominated by these matrices. For
\(M=T B_0 S^T/n\), the mean in whitened coordinates has matrix

\[
 A=(Q_T^*)^{1/2}B_0(Q_S^*)^{1/2}.
\]

Partial-isometry factorizations give
\(\|M\|=\|Q_{T,\mathrm{emp}}^{1/2}B_0
 Q_{S,\mathrm{emp}}^{1/2}\|\), including rank deficiency.
The square-root operator inequality then bounds

\[
 \|A\|\le\|M\|+2\|B_0\|\sqrt{D(q+D)},
 \quad D=\tau+\delta_G,
\]

where \(q\) bounds the two empirical Gram norms. The source's explicit
\(\sigma^2\)-gapped formulas bound \(\|B_0\|\) and \(q\)
by exponentials of polylogarithms, independently of the subsequently
chosen scalar noise. Thus \(\tau\) can make the added term negligible
at polylogarithmic precision cost. This is a bound on the unchanged
physical mean in new coordinates, not an ungapped regression replacement.

There is an important basis detail. Include the forward-history columns
\(V\) among the input columns \(S\), and write \(V=SJ^T\) for
their coordinate-selection matrix \(J\). Use
\(Q_V^*=JQ_S^*J^T\) for the variance replacement. If
\(b=(Q_S^*)^{-1/2}S^Tq/n\), then the variance term is
\(\|P b\|^2\), where

\[
 P=(\sigma^2 I+Q_V^*)^{-1/2}J(Q_S^*)^{1/2},\qquad
 PP^T=(\sigma^2 I+Q_V^*)^{-1/2}Q_V^*
             (\sigma^2 I+Q_V^*)^{-1/2}\preceq I.
\]

Thus \(P\) is a contraction even when the mean input basis has extra
columns. Independently selected incompatible Grams would not establish
this assertion; taking the principal block above does, using exactly
the already retained pair moments.

For the original empirical forward Gram \(Q_V\), resolvent congruence
gives

\[
 0\le v^T[(\sigma^2 I+Q_V)^{-1}
               -(\sigma^2 I+Q_V^*)^{-1}]v
 \le D\sigma^{-2}c.
\]

The proof is to conjugate the increment by
\((\sigma^2 I+Q_V)^{-1/2}\) and use
\(I-(I+E)^{-1}\preceq E\), followed by
\(v^T(\sigma^2 I+Q_V)^{-1}v\le c\). Choose the ridge small
enough that this variance bias, with its fixed-depth propagation, is
negligible too. Both empirical and population enlarged-Gram variances
are nonnegative, because their joint moment block has a dominating
history block.

The history marks used to measure a layer's outgoing moments need not
equal its mean's output marks. At each layer let \(U_\ell\) be the
whitened mean-output marks and \(V_\ell\) the whitened marks needed
as input moments at the next layer (or for the final readout). Both
systems separately have second moment at most identity under the
empirical and population laws. In these coordinates the new row is

\[
 h_\ell=\chi_\ell(U_\ell^TA_\ell b_{\ell-1}
              +\sqrt{\beta_\ell}g_\ell),\qquad
 \beta_\ell=\sigma^2+c_{\ell-1}-\|P_\ell b_{\ell-1}\|^2,
\]

with \(\|A_\ell\|\le C\), \(\|P_\ell\|\le1\), and
\(b_\ell=\mathbb E[V_\ell h_\ell]\),
\(c_\ell=\mathbb E[h_\ell^2]\). This requires no equality
between the two history bases.

The supplied tilt certificates give
\(D(\nu\Vert\mu)\le Ch\) and multiplier norm at most
\(Ch/\text{slack}\), with \(h=\operatorname{polylog}(n)/n\).
The exact exponential-family identity, using exchangeability, is

\[
 D(\pi_c\Vert\nu^{\otimes n})
 =D(\pi_c\Vert\mu^{\otimes n})-nD(\nu\Vert\mu)
 -n\lambda^T(\pi_c^1F-\nu F).
\]

Both moment errors are bounded by a fixed multiple of the feasibility
slack, so this full-array entropy is polylogarithmic. Uniform numerical-prefix error
belongs inside that tolerance; no continuity of optimal multipliers is
needed.

Here is a direct check of the statistical estimate used in the recurrence.
For a deterministic bounded test \(|G|\le B\) and a mark vector
\(U\) with \(\nu(UU^T)\preceq I\), restrict to
\(E=\{n^{-1}\sum_iU_iU_i^T\preceq I\}\). For each unit
direction, center \(X=(a^TU)G\). Its variance is at most \(B^2\),
and its sample squared centered values average at most \(4B^2\)
on \(E\). The inequality \(e^{x-x^2}\le1+x+x^2\), followed
by independent multiplication under \(\nu^{\otimes n}\), gives
the restricted tail \(2e^{-nt^2/(20B^2)}\). A half-radius sphere
net of size at most \(5^{\dim U}\), and tail integration, give
an exponential moment for the squared vector discrepancy times
\(\mathbf1_E\). The entropy inequality then yields

\[
 \mathbb E_{\pi_c}\left[\mathbf1_E
 \left\|n^{-1}\sum_iU_iG_i-\nu(UG)\right\|^2\right]
 \le\frac{CB^2}{n}
    [D(\pi_c\Vert\nu^{\otimes n})+\dim U+1].
\]

This uses no pointwise bound on normalized marks and does not assert
that \(E\) is typical under iid sampling. Its high posterior probability
comes from the acquired pair moments. The corresponding bounded
second-moment test costs \(CB^4(K+1)/n\), where
\(K=D(\pi_c\Vert\nu^{\otimes n})\).

Integrate each fresh scalar Gaussian before comparing empirical and
population parameters. If \(|\chi|\le B\),
\(|\chi'|\le a_1\), \(|\chi''|\le a_2\), then
\(\mathbb E\chi(m+\sqrt v g)\) is Lipschitz with constants
\(a_1\) in \(m\) and \(a_2/2\) in \(v\ge0\).
The variance derivative is obtained by two Gaussian integrations by
parts; adding a common positive variance and taking it to zero covers
the boundary. For \(\chi^2\) the constants are \(2Ba_1\)
and \(a_1^2+Ba_2\).

Let \(x_\ell\) denote the norm of the cross-moment error and
\(y_\ell\) the absolute second-moment error. Upper raw-Gram bounds
give \(\|b^{(j)}\|\le B\), RMS mean error at most
\(Cx_{\ell-1}\), and variance error at most
\(y_{\ell-1}+2Bx_{\ell-1}\). By duality,
\(\|\mathbb E[V_\ell q]\|\le\|q\|_2\).
Consequently the two errors obey

\[
\begin{aligned}
 x_\ell&\le a_1Cx_{\ell-1}
  +\tfrac{a_2}{2}(y_{\ell-1}+2Bx_{\ell-1})+\varepsilon_\ell,\\
 y_\ell&\le2Ba_1Cx_{\ell-1}
  +(a_1^2+Ba_2)(y_{\ell-1}+2Bx_{\ell-1})+\zeta_\ell.
\end{aligned}
\]

The tests supplying \(\varepsilon_\ell,\zeta_\ell\) are
evaluated at deterministic population parameters. The random empirical
parameter difference is the separately displayed propagation term.
Conditional on training marks and earlier passive layers, the fresh row
noises contribute cross-moment squared error at most
\(B^2\dim(V_\ell)/n\) and second-moment variance at most
\(B^4/n\). These are added to the source terms. Minkowski's inequality
and fixed depth give posterior RMS error
\(C\log^{C_L}(en)/\sqrt n\) on the common-Gram event.

The first affine layer is a bounded deterministic row test of the first
Gaussian row marks and the acquired first-layer displacement; it supplies
the starting errors by the same empirical estimate. The readout is a
final cross moment. If a time-patch readout is represented as a linear
combination of named history factors, use that finite span: its common
Gram bounds its whitened coefficient norm by its physical RMS plus the
already budgeted ridge error. No observation at every continuous time
and no pointwise cap on the readout are required.

All mean matrices in this recurrence are fixed once the prefix and
requested time are fixed. Their norm bounds follow on the intersection
of the original good-history event and the raw-Gram event. If these
events have positive posterior mass, existence of one such realization
already proves the bound for that deterministic matrix. This observation
allows the statistical estimate to remain under \(\pi_c\), with
\(\mathbf1_E\), rather than under a success-conditioned law.

## 6. Posterior probability and the all-query conclusion

The required finite-precision formulation is parameterwise. For a fixed
ideal prefix \(c\) in the common information/noise event, define

\[
 \mathcal B_\rho(c)=\{\widehat c:\|\widehat c-c\|_\infty\le\rho\}.
\]

Take an arbitrary deterministic \(\widehat c\) in this set. All
posterior comparisons continue to use \(\pi_c\). Uniform circuit
Lipschitz bounds give, for every retained test,
\(|F(z;\widehat c)-F(z;c)|\le\Lambda\rho\). The target moment
changes by at most \(\rho\) as well. Choose \(\rho\) so that
\((1+\Lambda)\rho\) is a small fixed fraction of the feasibility
slack, with the stronger source/covariance error tolerances also included.
Then \(\pi_c^1\) is a strictly feasible witness for every such
numerical prefix. The supplied calibrated-law certificates therefore
hold uniformly in this ball. The exponential-family identity in Section 5
uses \(F(\cdot;\widehat c)\) and \(\nu_{\widehat c}\), so it
still bounds \(D(\pi_c\Vert\nu_{\widehat c}^{\otimes n})\)
without any continuity assumption on the optimizing multiplier.

The same uniform test bounds preserve the empirical raw-Gram event;
uniform source sensitivity preserves the original-to-perturbed query
coupling. For each fixed \(\widehat c\), the self-normalized tests,
population parameters, and mean matrices are deterministic under
\(\pi_c\), exactly as required above. The argument below consequently
gives a deterministic inequality for the decoder value at *every*
\(\widehat c\in\mathcal B_\rho(c)\), with the same proof center
and uniform radius. It does not assert that a single posterior sample
satisfies every test at once, and does not take a probability union over
\(\widehat c\). After obtaining this deterministic conclusion one
may substitute the actual numerical prefix, even when it depends on
private selected packets beyond \(c\). This proves the proposed
precision repair. The uniform approximation radius for that actual
prefix remains the separate acquisition interface.

Let \(\mathcal H\) be the complete-tape good event collecting the
supplied physical/source guarantee, the given dense-to-deterministic-
center bound, the observable mean-operator event, and the small scalar
noise event. Its unconditional failure can be made an assigned small
fixed fraction of the requested confidence, plus the stated vanishing
failures. For the ideal prefix filtration,

\[
 M_j=\Pr(\mathcal H^c\mid C_{1:j})
\]

is a nonnegative martingale. Hence
\(\Pr(\max_j M_j>q)\le\Pr(\mathcal H^c)/q\).
This supplies one retained-prefix event at every acquisition time.
Intersect it with the information and posterior-noise events from
Section 2. Future complete-tape information appears here only inside
\(\mathcal H\), not inside the Gaussian conditioning filtration.

Let \(a(t,x)\) be the supplied deterministic proof center and assume
the given dense-pair interface
\(|f_n(t,x)-a(t,x)|\le b_n\) for every input and time on
\(\mathcal H\). For a retained prefix in the event above and each
requested \((t,x)\), the source coupling implies that the original
passive output puts mass at least \(1-q-o(1)\) in

\[
 [a(t,x)-b_n-n^{-10},\ a(t,x)+b_n+n^{-10}].
\]

The finite-rank, scalar-perturbation, and weak-moment comparisons give
mass at least \(1-q'\), for any allocated fixed \(q'>0\), in
an interval of radius \(C\log^{C_L}(en)/\sqrt n\) about the
deterministic calibrated moment decoder. This follows from the restricted
second moments and Markov, adding the posterior failures of their
training/Gram events. No Gaussian formula is conditioned on
\(\mathcal H\).

Choose \(q+q'+o(1)<1\). The two intervals have common posterior
mass and therefore intersect. Their deterministic centers differ by at
most the sum of their radii. The premises and radius bounds hold for an
arbitrary requested input and time on the *same* retained-prefix event,
so the resulting deterministic inequality holds for every input and time
there. No union over fresh query-noise realizations or sphere points is
being used. The actual dense trajectory is also within \(b_n\) of
the same proof center on the actual good tape.

Intersecting with the separately supplied simultaneous numerical seed
event, and adding its stated errors, therefore gives the candidate's

\[
 \sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
 |f_C(t,x)-f_n(t,x)|
 \le 2b_n+C\log^{C_L}(en)/\sqrt n.
\]

The finite source patches and its supplied frozen tail cover all times.
The fixed seed event is conditioned on training and independent of the
seed; its implementation and count remain outside this report. The
candidate's claim that the remainder is eventually below \(b_n\) for
fixed nonzero labels is conditional on the stated positive exponential
factor in that absent certificate; this check does not rederive it.

## 7. Audit disposition

The inspected bridge does not insert noisy moments into an exact Gaussian
posterior, condition fresh innovations on unused future training roots,
assume bounded coordinates for Picard history fields, invert an empirical
history Gram without a noise floor, or propagate a variance discrepancy
by taking its square root. The finite-rank correction is the only strong
Gaussian comparison needed, and its rank bound gives root-width error
directly. The common raw-Gram event is supplied by retained observations,
not inferred from a low-entropy row marginal alone.

The result is conditional on the expressly named supplied interfaces.
This report supplies no independent validation of the omitted short
solver, dense-pair certificate, acquisition, compiler, or cubature code or
proof. The frozen candidate must incorporate the parameterwise numerical-
prefix statement above before claiming applicability to arbitrary private
finite-precision acquisition. With that repair, there is no surviving
major bridge defect or counterexample to the stated statistical rate.
No experiment, external
retrieval, Git mutation, or edit outside this report was performed.

## 8. Recheck of the revised complete assembly

2026-10-06. This addendum supersedes the frozen candidate's application
FAIL above for the new candidate hash listed here. The earlier analysis
and its hashes are preserved as the record of what was checked first.
The supervisor expanded this isolated assignment to the complete tilt
compiler and robust cubature notes. I read all three newly authorized
versions completely; no other review or linked scientific source was read.

**PASS: the revised complete assembly closes the inspected mathematical
and numerical interfaces, under the inherited physical/source/dense
certificates, the stated finite-precision acquisition guarantee, and the
named counted numerical-primitive interfaces.** No further assembly gap
was found. This is a conditional complete-assembly check, not an
independent reproof of those inherited certificates, a software
implementation, or promotion review.

New frozen inputs:

| File | SHA256 |
|---|---|
| `DENSE_BUDGET_DECODER_CANDIDATE.md` | `931227ba250cb442013f1ecd42e1fea314b1efa22879cdd12055220fb7769c93` |
| `DENSE_BUDGET_TILT_COMPILATION.md` | `e66ec00d90f58d75e329cca97b4fa59123d52607563125543ec93999417face3` |
| `DENSE_BUDGET_ROBUST_CUBATURE.md` | `a9dc2b37d41c78387c8d479a2a630916d25534b5ccb77f6d5227c88ed00a518e` |

### 8.1 Required bridge corrections are present

Candidate Sections 2, 3 and 8 now prove the posterior comparison for
every numerical prefix in the certified error ball before substituting
the actual privately acquired value. This is the parameterwise repair
proved in Section 6 of this report; it resolves the earlier application
FAIL without a probability union, optimizer continuity, or additional
conditioning on private packets.

Candidate Section 4 now takes the variance Gram as a principal block of
the master mean-input Gram and explicitly allows different mean-output
and outgoing-moment bases. It treats the readout as a finite history
span with bounded RMS and source-bounded time coefficients. It also
justifies omitting the passive source's inactive RMS projections before
using the smooth capped auxiliary network. These statements supply
precisely the choices used in the reconstruction above.

The finite cached Gram is explicit. Entrywise error at most
\(\tau/(4r)\) in dimension \(r\) gives operator error at most
\(\tau/4\). Adding \(2\tau I\) after symmetrization gives a
matrix between \(Q_\nu+7\tau I/4\) and
\(Q_\nu+9\tau I/4\). With empirical-to-population error at most
\(\tau/4\), this one finite matrix dominates both actual Grams,
has a known positive floor, and differs from either by \(O(\tau)\).
Its principal blocks preserve the variance contraction. Thus the proof
and numerical whitening use the same regularized geometry.

### 8.2 The finite compiler supplies the law used by the bridge

The compiler's hypotheses are met by the fixed numerical-prefix circuit:
its dimension and instruction count are absolute-polylogarithmic, its
global amplitude and Lipschitz bounds have absolute-polylogarithmic
logarithms, and the same posterior row marginal remains a strict
feasibility witness throughout the numerical-prefix ball. Its parameter
choices \(a=2s\), with \(s\) the scalar-observation tolerance,
give compiled moment error below \(7s/2\), entropy below \(2h\),
and multiplier norm at most \(2(1+h/s)\).

The addend one in the multiplier bound is now accounted for. In the
change-of-reference identity the two moment errors sum to at most
\(11s/2\), so the extra full-array entropy is bounded by
\(11n(h+s)\). Choosing the subsequently selectable scalar noise
so that \(s\le h\) gives at most \(22nh\), which remains
absolute-polylogarithmic. The row law returned at the finite multiplier
is the exact reference law for this identity; approximating its cached
normalizer is a separate numerical operation.

The compiler is constructive: the strict-slack dual objective confines
an exact multiplier to a bounded ball; its finite dyadic grid contains
a point that passes moment and entropy checks with room for certified
error. For each candidate, streaming Gaussian quadrature bounds its
relative tail, uses short grid counters, and evaluates log sums by a
two-pass maximum-and-sum procedure. The tolerances have logarithmic bit
cost, including when the log weights themselves have very large
magnitude. No normalizer oracle or stored grid is required.

The same quadrature computes all raw history-Gram entries, since their
pair products were added to the retained test list. Refining these
integrals to the buffer tolerance and caching their finite values adds
only polynomially many counters/entries and precision bits. The
compiler's allowed unrestricted acquisition runtime is essential here;
none of these quadratures is charged as a late-query procedure.

### 8.3 Cubature matches the actual passive moment calls

For each call the history mark vector is whitened by the cached
dominating Gram. Its \(\nu\)-second moment is at most identity.
The new passive scalar test is bounded by \(B\), and the
second-moment test by \(B^2\). The tilt depends only on acquired
training coordinates. Append the fresh passive Gaussian coordinates
independently to both reference laws; the tilt density is constant in
those new coordinates. Thus Gaussian smoothing in the weak recurrence
remains applicable when the same integral is evaluated numerically.

With \(w=\min(d\nu/d\mu,4)\), the cubature note proves
removed mass \(O(h)\), whitened cross-moment bias \(O(B\sqrt h)\),
and coordinate second moment at most \(4B^2\) under the easy prior.
For scalar second moments the direct clipping bias is \(O(B^2h)\)
and the sampling variance bound is \(O(B^4)\); this changes only
an absolute logarithmic factor. No clipped sampling estimate replaces
the cached raw training Grams.

Independent median-of-means blocks with pairwise-independent rows have
the claimed variance and confidence bounds. The finite-field seeds,
clipped Gaussian quantiles, and proof-only within-cell coupling preserve
that construction. Their cutoff is a sample-coupling event, not an
uncontrolled truncation of the population law. The parameter set includes
every guarded intermediate query moment, so the event holds at
seed-dependent intermediate arguments without an independence assertion
for those arguments. A shared finite seed therefore defines one
repeatable decoder over every prefix, input and time patch.

The required local amplitude and continuity bounds follow from the
globally capped source circuits, finite multiplier and normalizer,
positive Gram buffer, and guarded moment boxes. Their logarithms are
absolute-polylogarithmic. A layer's square root is at worst one-half
Hölder in its guarded variance parameter; its net cost is logarithmic.
This does not replace the linear variance dependence of the exact
Gaussian expectation used for propagation. Numerical moment guards can
include a bound on the cross-moment norm and a nonnegative variance
projection; the true population moments lie inside these guards, and
the projections do not increase their approximation error.

Weight evaluation requires no exponential at an enormous negative
argument: after forming the clipped log density, return zero below a
threshold determined by the desired absolute integrand error and the
known local whitened-mark bound. Above that threshold its exponential
argument has only polylogarithmic magnitude. The cached normalizer
precision is chosen using the same local bound, as required by the
cubature note. The retained Grams and multiplier themselves are not
re-estimated during queries.

Using \(\varepsilon=n^{-3/4}\), the complete row counts, independent
blocks, finite-field and Gaussian routines, row-circuit evaluations,
small matrices and all moment calls give
\(Cn^{3/2}\log^k(en)\) primitive work with absolute \(k\).
Only the seed, one row, block accumulators, cached matrices and counters
are live, with an absolute-polylogarithmic bit count. Fixed-depth weak
propagation gives numerical error
\(n^{-3/4}\log^{C_L}(en)=o(n^{-1/2})\); clipping and the
posterior comparison give \(\log^{C_L}(en)/\sqrt n\).
The large local row sensitivities enter precision and covering counts,
not the sample-variance bound or the weak propagation factor.

The named primitive interfaces retained here are counted Gaussian
quantile generation, finite-field arithmetic with its preprocessing
polynomial, gapped small-matrix functions, and the source's counted
activation/data/row-evaluation precision access. The construction counts
activation primitives as stipulated. Polynomial bit-time additionally
requires polynomial-time precision access; polynomial-space access alone
does not establish it. No such stronger claim is made by the assembly.

### 8.4 The stated outer probability allocation is valid

The complete-tape failure probability is at most \(\delta/64\),
including the dense certificate invoked at \(\delta/256\).
For threshold \(1/16\), its posterior-failure martingale costs at
most \(\delta/4\) by the first-crossing bound. To ensure that the
actual tape is good on this same event, extend this martingale filtration
by the terminal indicator of complete-tape success: its last failure
posterior is \(\mathbf1_{\mathcal H^c}\). The crossing event then
contains actual tape failure. This augmentation is used only for the
probability bound, not for the Gaussian conditioning or entropy laws.

The information and posterior-noise maxima each cost \(\delta/8\),
and the one cubature-seed event costs \(\delta/4\). Together these
are \(3\delta/4\); the reserved \(\delta/4\) covers the stated
separate acquisition/source failures. Conditional Gram, finite-rank and
weak-comparison failures can have fixed total below \(1/4\), by
constant choices in their radius and posterior-noise thresholds. The
posterior interval masses then sum to more than one. This proves the
same all-input/all-time deterministic-center conclusion with total outer
failure at most \(\delta\), without a growing prefix or query union.

Thus the revised assembly yields
\(2b_n(\delta/256)+C\log^{C_L}(en)/\sqrt n\) and the stated
counted resources under its named interfaces. For fixed nonzero labels,
the supplied positive exponential factor in \(b_n\) absorbs the
additional logarithmic root-width term eventually, giving the stated
\(3b_n(\delta/256)\) certificate. The result is the same error
scale, not the old literal \(2b_n+1/n\) remainder. The absolute
storage exponent is not numerically extracted, acquisition runtime is
unrestricted, and the sufficiently-large-width threshold is unquantified
and may depend on all fixed problem parameters. These limitations are
stated explicitly in the revised candidate and are not additional gaps.

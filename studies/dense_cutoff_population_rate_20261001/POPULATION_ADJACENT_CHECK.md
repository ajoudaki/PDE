# Internal check of the adjacent-width, tagged-response and localization note

2026-10-03. Scoped internal reconstruction of
POPULATION_ADJACENT_ATTEMPT.md. This checker authored
POPULATION_NEGATIVE_SEARCH.md and POPULATION_DIRECT_CHECK.md, but not
the candidate or its insertion dependencies. This is collaborative
internal validation, not a promotion review.

**Verdict.** The original frozen version required one correction to the
conditioning argument for maximum cutoffs. The author made that
correction during this check. The repaired version passes for its
stated local and conditional claims: conditional insertion, first
variations under bounded tagged histories, exact integrated pulse/trace
identities, and the weighted finite-center comparison under its explicit
Lipschitz-extension hypothesis. No adjacent-width bias cancellation or
dense-to-population rate is proved by these results.

The original source hash was
b0d03c2238b72664ac5c1ce1fad47bbcbc4d6be09f4d318209a7eb1eddd8cc80.
The repaired hash is
f8171c28e5744d4e9c3b4af9caf97795bfa5d98141f6a99a06fb373f532a3df9.
The exact change and presentation checks are recorded separately in
Section 8 below.

## 1. Scope and claim-by-claim outcome

Keep fixed depth, fixed finite compatible training data, the canonical
Gaussian initialization, zero stored readout, sufficiently small fixed
labels, and \(C^3\) activations with bounded first three derivatives.
Activation values may grow linearly. Fixed sample weights \(p_a>0\)
sum to one; \(r_a=f_a-y_a\) and
\(\rho^2=\sum_a p_a r_a^2\).
The labels can be decreased by a further fixed threshold to accommodate
the finitely many enlarged localization budgets and physical tubes.
No threshold depends on width.

The local norm bounds use
\[
 A_n=\exp\{C\sqrt{\log(e+n)}\},\qquad
 \epsilon_n=n^{-1/2}\exp\{C'\sqrt{\log(e+n)}\},\qquad
 T_n=C_T\log(e+n),
 \tag{1}
\]
with a fixed number of enlargements permitted. These envelopes remain
\(n^{o(1)}\).

| Candidate claim | Outcome and qualification |
|---|---|
| Exact width-\(n\) cavity to width-\(n-1\) normalization bridge | Checks pathwise |
| Gaussian variance derivative | Checks when differentiation/integration by parts is justified, as expressly required |
| Adjacent bias cancellation at \(n^{-3/2+o(1)}\) | Open; not supplied by the candidate |
| Finite-dimensional Stein comparison from an integrable innovation error | Checks, including singular covariance |
| Conditional insertion/no-exit on each cavity's own good set | Checks with fixed enlarged bounds chosen before the label threshold |
| Tagged-history C1 estimate | Checks for the derivative at zero, in bounded-history to field-supremum operator norm, through \(T_n\) |
| Averaged forward/reverse pulse identities | Exact |
| Removing adaptive residual differentiation in integrated traces | Checks at \(n^{-1+o(1)}\) on the logarithmic horizon |
| Expected modulus between cavity weights | Original conditioning prose needed repair; repaired proof checks |
| Weighted conditional observable versus deterministic finite-width center | Checks under the separately stated global Lipschitz-extension hypothesis for that observable |
| Population identification, off-diagonal response-density convergence, or a two-layer simultaneous deletion theorem | Not established or inferred here |

The candidate was read completely. The local insertion dependencies had
already been read completely in the preceding check; their unchanged
hashes were verified and the relevant calculations were reused. This
does not convert their internally established finite good event into
an unconditional expectation theorem.

## 2. Normalization, adjacent cancellation and the Stein test

Put \(k=n-1\), \(c=k/n\). In the candidate's comparison family,
\[
 f_{k;\alpha,\tau}=\frac{\alpha}{k}w^\top h^{(L)},\qquad
 W_0^{(\ell)}=\sqrt{\tau/k}\,G^{(\ell)}\quad(\ell\ge2).
 \tag{2}
\]
The parameter-gradient of the prediction has prefactor \(\alpha/k\).
Multiplying its first/readout blocks by mobility \(k/\alpha\)
therefore leaves their velocities \(-2\sum_a p_ar_a\delta_av_a^\top\)
and \(-2\sum_a p_ar_ah_a^{(L)}\). Hidden blocks have mobility
one and coefficient \(-2\alpha/k\).
At \((\alpha,\tau)=(c,c)\), these are exactly the retained
width-\(k\) system with every original normalization still \(n\).
At \((1,1)\), they are the canonical width-\(k\) system.
Thus the candidate's diagonal-segment identity has the correct
normalization, mobility and sign.

At fixed time where the flow is regular, differentiability follows
from the finite-dimensional \(C^2\) vector field and its smooth
parameter dependence. The derivative in \(\alpha\) includes the
whole trained trajectory. For compactly supported smooth tests of
initialized hidden entries, Gaussian density differentiation gives
\[
 \partial_\tau\mathbb EF_k
   =\frac1{2k}\sum_{\ell,i,j}
             \mathbb E\partial_{W_{0,ij}^{(\ell)}}^2F_k.
 \tag{3}
\]
The \(1/(2k)\) factor follows because each variance is \(\tau/k\).
The source correctly leaves passage to the original trained
observable conditional on integrability/localization.

The mean decomposition
\[
 b_n-b_{n-1}
  =D_n-\int_c^1(\partial_\alpha+\partial_\tau)
                            \mathbb EF_k(s,s)\,ds
 \tag{4}
\]
is algebraically exact whenever those expectations exist and the
integral identity may be averaged. A bound
\(n^{-3/2}e^{C\sqrt{\log n}}\) for (4) would have near-root
summable tails: on the dyadic block starting at \(2^jn\), its sum is
bounded by
\[
 Cn^{-1/2}2^{-j/2}
        e^{C\sqrt{\log n}}e^{C\sqrt{(j+1)\log2}},
 \tag{5}
\]
and the sum over \(j\) is finite.

No such cancellation is proved. In particular the retained nonlinear
remainder \(U\) has norm \(\epsilon_n\), while
\(\|D_\Theta f\|\le C/\sqrt n\), so its prediction contribution
can be \(n^{-1+o(1)}\). It is of the leading deletion order and
cannot be omitted in a calculation seeking \(n^{-3/2+o(1)}\).
Statements about individual \(n^{-1+o(1)}\) terms in (4) do not
supply cancellation. Removing one neuron in every layer also requires
a finite sequential rectangular-cavity comparison if a quantitative
bound for that particular \(D_n\) is to be invoked; the exact
normalization bridge itself needs no such theorem.

For the Stein statement, with fixed finite-dimensional centered
Gaussian \(G\) of covariance \(Q\), the identity
\(\mathbb EG_i\psi(G)=\sum_jQ_{ij}\mathbb E\partial_j\psi(G)\)
holds even when \(Q\) is singular: write \(G=A\xi\), apply
one-dimensional Gaussian integration by parts to the independent
coordinates of \(\xi\), and use \(AA^\top=Q\).
The candidate's subtraction identity then bounds its Stein defect by
\(C_{\psi,Q}\mathbb E[(1+|G|)|I-G|]\). No derivative of
the innovation error and no inverse of \(Q\) is used.

## 3. Conditional insertion and legitimate innovation localization

Fix retained initialization in the candidate's cavity-measurable good
set. It has a strict initial Gram margin, the physical fitting tube,
bounded activity, fixed joint exponential budget, and coordinate
maximum at most \(M_n/2\), with \(M_n=C_D\sqrt{\log(e+n)}\).
Stop the restored full path at maximum \(M_n\), or at exit from
the larger physical tube.

Before that stop its omitted controls are bounded by
\(C(1+M_n)\). The conditional Gaussian-kernel event from the
checked direct theorem consequently gives the improved retained
full/cavity comparison, with conditional failure \(Cn^{-D}\).
Retained coordinates cannot cause the stop: they differ from their
reference coordinates by \(\epsilon_n\), and the reference has
the factor-two margin.

For the omitted neuron the amplitude-sensitive trace estimates give
\[
 \frac{K_i}{S}
  \le G_{{\rm back},i}+C(1+S^2B)(1+Z_i)+O(\epsilon_n),
 \qquad
 Z_i\le G_{{\rm forward},i}
       +CS^2(1+S^2\sqrt B)\frac{K_i}{S}+O(\epsilon_n).
 \tag{6}
\]
Here \(Z_i,K_i\) are running maxima, and \(S>0\) is the fixed
activity scale. The reference Gaussian suprema have uniform
sub-Gaussian tails conditional on the cavity: the forward coefficient
path has bounded normalized variation in activity; the backward one
has the budget-controlled square-root activity modulus.
All constants are deterministic on the cavity good set.

Choose the fixed budget first and the fixed label threshold afterward,
so that the product of the two coefficients in (6) is below \(1/2\).
Solving these two scalar inequalities yields
\[
 Z_i+K_i/S
       \le C(1+G_{{\rm forward},i}+G_{{\rm back},i})
                                                 +O(\epsilon_n).
 \tag{7}
\]
The omitted coordinate therefore stays below \(M_n\) except with
conditional probability \(Cn^{-D}\), after increasing \(C_D\).
The first layer substitutes its Gaussian input row for the forward
reference; at the top the exact readout inequality
\(|w_i|/S\le C(1+Z_i)\) supplies the same absorption.

The physical tube does not need a full-dependent good indicator.
The omitted Gaussian row and column have bounded Euclidean norms
except with exponentially small conditional probability; a fixed list
of Gaussian input values is at most \(C_D\sqrt{\log n}\) except
with probability \(n^{-D}\). Restoring the neuron changes the
initial feature Gram by \(n^{-1/2}\operatorname{polylog}n\).
It enlarges initial hidden operator bounds by only a fixed constant.
The zero-readout deterministic small-label fitting proof therefore
applies with a fixed larger initial norm bound and the retained strict
Gram margin. Choosing this bound before the label threshold avoids
assuming the restored tube. The first-weight Frobenius RMS change
vanishes.

This proves the conditional no-exit claim on \([0,T_n]\) for
every cavity in the specified set. It does not give a quantitative
probability for that cavity set under the original initialization.
Crude physical tails extend the coordinate/prediction consequences;
they do not by themselves extend arbitrary first-variation or
unfrozen memory-kernel assertions to infinite time.

For a fixed finite list of innovation coordinates, define the auxiliary
innovation to equal the actual one on success and \(G\) on failure.
Its weighted mean error is \(C\epsilon_n\), using only Gaussian
moments. For a compactly supported \(C^2\) test, both
\(I_i\psi(I)\) and \(\partial_j\psi(I)\) are bounded. Replacing
this auxiliary variable by any finite measurable extension on failure
therefore changes the Stein functional by \(C_{\psi,Q}n^{-D}\).
The compact-support qualification matters: an arbitrary bounded
noncompact test need not make \(I_i\psi(I)\) bounded.

## 4. First variations under tagged histories

The C1 assertion is a statement at zero perturbation. Add a bounded
forward-preactivation history or reverse-carrier history to the tagged
neuron. Write its amplitude as \(\varepsilon u_a(t)\), with
\(\|u\|_\infty\le1\), and differentiate at \(\varepsilon=0\).
The comparison scalar equations must include the same direct history:
the forward equation gains \(\varepsilon u\) for a forward pulse,
and the carrier equation gains it for a reverse pulse.
The reference cavity and its coefficients remain fixed.
For a reverse pulse the inserted derivative
\(b_a=\delta_{a,i}\) includes the added carrier through
\(\delta=\phi'(z)k\). These conventions make the differentiated
deletion identity exact.

The unperturbed full variational propagator has norm \(A_n\).
A coordinate forward pulse has forcing equal to an adaptive
rank-one term plus the residual-weighted coordinate column of the
mixed parameter/external derivative. A reverse pulse has forcing
\(-2p_ar_aD_\Theta h_a^\top e_i u_a\).
Their norms, integration over \(T_n\) for residual-free terms,
and finite activity for residual-weighted terms imply
\[
 \|\partial_\varepsilon\Theta_{\rm full}\|_2\le A_n,\qquad
 \max_{a,t}\{|a_a'|+|b_a'|\}\le A_n.
 \tag{8}
\]
The full response is bounded before the retained/cavity derivative
comparison, so the latter is not a circular estimate for the unknown
control derivatives.

Here is the exact retained Jacobian check. At fixed external controls
put
\[
 g_a=\nabla_\Theta\mathcal F_a(\Theta,e),\qquad
 v_a=D_\Theta h_a^{(j-1)}(\Theta)^\top q_a.
 \]
The retained field is \(-2\sum_a p_ar_a(g_a+v_a)\), whereas
\(D_\Theta r_a=g_a^\top/n\). Thus
\[
 DF_{\rm aug}
 =-2\sum_a p_a\left[
       \frac{(g_a+v_a)g_a^\top}{n}
           +r_a(D_\Theta^2\mathcal F_a+D_\Theta v_a)\right].
 \tag{9}
\]
In particular its extra rank-one term is \(v_ag_a^\top/n\);
the residual does not acquire an artificial \(q^\top h\) term.

The checked insertion event gives coordinate field differences
\(\epsilon_n\), ordinary field differences \(A_n\), and
retained hidden-matrix differences \(A_n/\sqrt n\).
Forward Jacobian differences are consequently \(\epsilon_n A_n\):
feature changes in a matrix derivative are divided by \(\sqrt n\),
and gate changes use their coordinate maximum. In the large Hessian
diagonal,
\[
 |k\phi''(z)-k^0\phi''(z^0)|
 \le \|\phi''\|_\infty|k-k^0|
       +\| \phi'''\|_\infty |k^0|\,|z-z^0|
 \le\epsilon_n A_n.
 \tag{10}
\]
Mixed weight terms retain \(1/\sqrt n\).
The ordinary gradient difference has norm \(A_n\), so the
normalized gradient-Gram difference is \(A_n/\sqrt n\).
The remaining \(D_\Theta v_a\) is the reverse-probe Hessian:
its reference probe is coordinatewise small, and the checked probe
subtraction preserves a bound \(\epsilon_n A_n\) at the actual
retained state. Also
\(\|v_ag_a^\top/n\|\le A_n/\sqrt n\).
These terms verify source (17), rather than assuming generic control
of a third derivative of the flow.

For completeness, differentiating the external forward-source map in
(9) produces
\[
 -\frac{2p_a}{n}(g_a+v_a)d_a^\top-2p_ar_aB_a^\top.
 \tag{11}
\]
Its extra \(v_ad_a^\top/n\) term is \(A_n/\sqrt n\), and its
other factors have the same controlled differences. The external
reverse-source map is \(-2p_ar_a C_a^\top\).
Thus all external derivative-map differences have size
\(\epsilon_n A_n\), including the small extra term caused by
the reverse force.

Differentiate the exact learned omitted-row/column integrals.
Each differentiated scalar control is bounded by (8); a retained
vector has norm \(C\sqrt n\), a differentiated one has norm
\(A_n\), and the hidden update has factor \(1/n\).
The differentiated residual is at most \(A_n/\sqrt n\).
After integration, the learned source derivatives have size
\(A_n/\sqrt n\). At the top the omitted prediction has derivative
\(A_n/n\), giving a retained forcing derivative \(A_n/\sqrt n\).

Let \(\Theta'\) be the retained derivative and \(V'\) the cavity
linear insertion with controls \(a',b'\). Their difference solves
the cavity variational equation with sources
\((DF_{\rm aug}-DF_0)\Theta'\), the external-map differences,
and the learned-source derivative remainders. Equations (8)--(11),
the finite horizon, and the cavity propagator give
\[
 \sup_{t\le T_n}\|\Theta'-V'\|_2\le\epsilon_n A_n.
 \tag{12}
\]
Forward/backward reconstruction and scalar pairing preserve this rate.
The Gaussian kernel event is uniform for bounded controls before
integration; derivative controls of amplitude \(A_n\) cost only
another fixed envelope. In learned scalar row/column equations,
derivatives of normalized pairings and of residuals cost
\(A_n/\sqrt n\). Thus the claimed tagged-history first-variation
error follows without differentiating an unknown remainder.

This is an operator-norm estimate from bounded histories to field
suprema, at zero perturbation. It neither supplies a width-uniform
finite-amplitude neighborhood nor permits division by a shrinking
pulse duration to claim pointwise memory-density convergence.

## 5. Exact pulse averages and residual freezing

For one layer let \(B_a=D_\Theta\delta_a\), and let \(E_a\)
be its direct external-preactivation derivative. A coordinate-\(i\)
forward pulse yields
\[
 \Theta_i'(t)
 =\sum_b\int_0^tJ(t,s)
       [P_b(s)-2p_br_b(s)B_b(s)^\top]e_i u_b(s)\,ds,
 \]
\[
 \delta_{a,i}'(t)
       =e_i^\top B_a(t)\Theta_i'(t)
                         +e_i^\top E_a(t)e_i u_a(t).
 \tag{13}
\]
Summing (13) over the coordinate-matched separate experiments and
dividing by \(n\) gives exactly source (20), including its
instantaneous term and rank-one adaptive-residual term. It would not
give the same trace for one simultaneous all-coordinate pulse.
The normalized rank-one trace contributes \(A_n/n\), after the
time integral is absorbed into the envelope.

For a reverse pulse, \(C_a=D_\Theta h_a\) at the lower layer and
\[
 \Theta_i'(t)=-2\sum_b p_b\int_0^t
                r_b(s)J(t,s)C_b(s)^\top e_i u_b(s)\,ds.
 \tag{14}
\]
Pairing with \(e_i^\top C_a(t)\), summing and dividing by \(n\)
gives source (21). Signs, sample weights and normalization all check.

Let \(J_{\rm fr}\) omit the negative gradient-Gram term from the
generator while preserving the realized residual coefficients.
Both propagators have norm \(A_n\). Duhamel's identity gives
\[
 J(t,s)-J_{\rm fr}(t,s)
   =-\int_s^t J(t,u)
       \left[\frac2n\sum_a p_ag_a(u)g_a(u)^\top\right]
                                 J_{\rm fr}(u,s)\,du.
 \tag{15}
\]
The middle matrix has rank at most \(m\) and bounded operator norm.
Between either pair of endpoints \(B\) or \(C\), the trace of
each integrand is therefore bounded by \(C_m A_n\), independently
of the ambient parameter dimension. Dividing by \(n\) and integrating
over \(T_n\) gives \(A_n/n\). Thus the asserted integrated
trace comparison with frozen residual differentiation is justified.

The candidate correctly leaves comparisons with a second deleted neuron,
particularly in neighboring layers, as an additional obligation.
The shared initialized edge cannot be counted as two independent
Gaussian roots. None of (13)--(15) establishes that missing comparison.

## 6. Cavity cutoffs and the repaired maximum argument

The cutoffs can be defined as bounded measurable functions of a
cavity's own initialization. If a physical/budget descriptor is not
finite, assign cutoff zero; on nonzero support the fixed positive
initial margin and norm bounds ensure the relevant physical trajectory
exists. The scalar cutoff functions can be Lipschitz in their descriptor
values without being globally Lipschitz in Gaussian roots. No such
root Lipschitz property is used for \(\chi_i\).

Choose plateaus and supports with fixed strict gaps, and choose the
label threshold after all larger support budgets and norm bounds.
The completed finite-cavity theorem gives
\(\mathbb E\chi_i\to1\) qualitatively. Restoration from a supported
cavity has conditional failure \(n^{-D}\), so unioning over
supported indices gives a polynomially small unconditional exception.
The improved insertion applied to every other, separately stopped
cavity gives its comparison to the controlled full path. Larger
budget and maximum margins exclude earlier stops.

The initial requirements in this step are available from the complete
unbounded initialization argument: Gaussian operator/Frobenius bounds
hold with exponentially small failure, and projected fresh-row
Gaussian estimates give simultaneous \(o(1)\) initialized coordinate
differences for all singleton deletions, with superpolynomial failure.
The initial Gram changes by \(n^{-1/2}\operatorname{polylog}n\)
on those events. This supplies the starting maximum/budget margins;
a deterministic Gram comparison alone would not supply initialized
coordinate maxima.

For shared retained coordinates, the joint exponential-budget
difference is bounded by
\[
 C\epsilon_n A_n e^{C\eta M_0}
                    +\frac{C}{n}e^{C\eta M_0},
 \qquad M_0=C\sqrt{\log(e+n)}.
 \tag{16}
\]
The first term is the mean-value bound for each exponential; the
second accounts for the finitely many nonshared coordinates.
It remains near root width. The initial Gram and budget scalar
cutoffs inherit this modulus.

The raw maximum requires separate treatment. If the nonshared
coordinates stay below the plateau, any maximum in the transition
region is attained among shared retained coordinates, and their
comparison controls the cutoff. If the problematic coordinate is \(j\),
let \(A_{n,j}^{\rm large}\) denote cavity \(j\)'s own larger
good set. The common-success construction puts that cavity in this set
whenever any weight is supported, outside the controlled exception.
The repaired argument uses
\[
 \Pr\{A_{n,j}^{\rm large},
      \text{restored tagged }j\text{ exceeds }M_0-O(\epsilon_n A_n)\}
 \le Cn^{-D}.
 \tag{17}
\]
To prove (17), condition on cavity \(j\), apply its conditional
insertion and Gaussian reference bounds, and then average. This
conditioning is valid whether or not \(\chi_j\) is zero.
The full/cavity coordinate comparison transfers the bound to the
nonshared coordinate of a different cavity.

In the original frozen paragraph, the instruction to use a different
supported cavity when only its weight was nonzero did not preserve
this omitted-root conditioning. That was a real gap in the stated
proof, though the already constructed larger good sets provide the
repair. The author's replacement paragraph implements (17).

Initial operator/Frobenius cutoff differences are handled on one
Gaussian event where all such cutoffs equal one. The complement is
exponentially small, and cavity submatrix operator norms do not exceed
the corresponding full initial norms. This does not assert a
deterministic small deletion modulus for operator norms.

Unioning the controlled conditional exceptions, taking \(D\) large
enough to absorb all fixed polynomial counts, and using
\(|\chi_i-\chi_j|\le1\) on failure gives
\[
 \mathbb E|\chi_i-\chi_j|
     \le n^{-1/2}e^{C\sqrt{\log(e+n)}}+Cn^{-D_0}.
 \tag{18}
\]
The constants may be selected for each prescribed fixed \(D_0\).
No quantitative bound on the complement of the original full
high-probability event was inserted into this argument.

## 7. Weighted observations versus a finite-width center

Let \(|\Phi_i|\le H_n\le A_n\) be an equivariant bounded scalar
observable, and \(F_n=n^{-1}\sum_i\Phi_i\).
Permutation invariance gives
\(\mathbb E[\Phi_j\chi_i]=\mathbb E[\Phi_i\chi_j]\), hence
\[
 \mathbb E[\Phi_i\chi_i]-\mathbb E[F_n\chi_i]
  =\mathbb E\left[\Phi_i\left(\chi_i-\frac1n\sum_j\chi_j\right)\right].
 \tag{19}
\]
Equations (18)--(19) bound this difference by \(\epsilon_n A_n\).
Independence of the neurons or of their weights is not needed.

Now assume, as the candidate explicitly does, that this particular
\(F_n\) has a bounded global Gaussian-root Lipschitz extension
\(\widetilde F_n\) with Lipschitz constant \(\epsilon_n A_n\),
agreeing with \(F_n\) on the full event constructed from supported
cavities. Clamp its range to \([-H_n,H_n]\), which preserves
agreement and Lipschitz continuity. Let \(c_n=\mathbb E\widetilde F_n\).
The Gaussian concentration bound already proved in
GENERAL_SELF_AVERAGING.md gives
\(\mathbb E|\widetilde F_n-c_n|\le C\epsilon_n A_n\).
Conditional no-exit on the support of \(\chi_i\) gives
\[
 \mathbb E[|F_n-\widetilde F_n|\chi_i]\le C H_n n^{-D_0}.
 \tag{20}
\]
Combining (19)--(20) and using \(\mathbb E\chi_i\ge1/2\)
for sufficiently large width yields
\[
 \left|\frac{\mathbb E[\Phi_i\chi_i]}{\mathbb E\chi_i}-c_n\right|
                      \le n^{-1/2}e^{C\sqrt{\log(e+n)}}.
 \tag{21}
\]
Only convergence of \(\mathbb E\chi_i\) to one is used, not its
rate. The weight stays cavity measurable when the conditional
Gaussian identities are applied.

The extension hypothesis is substantive. Prediction concentration does
not automatically supply it for empirical covariances or response
traces. Their derivative estimates remain to be proved individually.
Even with those estimates, \(c_n\) is a finite-width center; (21)
does not compare it to the canonical population.

## 8. Source versions, repair and verification record

The initial source was read completely at the requested hash. After
the conditioning issue was sent to the author and coordinator, the
author replaced only the missing-coordinate paragraph in Section 7.
A no-index diff against the frozen copy verified that Sections 5–6
and every other paragraph were unchanged. The repaired paragraph
was read and reconstructed in Section 6 above.

Both original and repaired files contain **zero form-feed bytes**.
In particular source equation (24) already contains a valid
\(\frac1n\). No presentation correction was necessary, and this
checker did not edit the source.

| Read source/version | SHA-256 |
|---|---|
| POPULATION_ADJACENT_ATTEMPT.md, original | b0d03c2238b72664ac5c1ce1fad47bbcbc4d6be09f4d318209a7eb1eddd8cc80 |
| POPULATION_ADJACENT_ATTEMPT.md, repaired | f8171c28e5744d4e9c3b4af9caf97795bfa5d98141f6a99a06fb373f532a3df9 |
| Candidate Sections 5–6, unchanged | 8a0c7e13e257c1f07fc1dc2940b4971252f9080bdd3fafc9194cbb3c36dfcc6a |
| POPULATION_DIRECT_COUPLING.md | 145895536ea2e006ff444e2ca4eeb8b408ee1adf594dc317e9ea28a05936cb00 |
| DEPTH_CAVITY_ROUTE.md | e8f9f43c137a9c74b751cbd2e54cf5a2b13f090c560d912b4b17994c53bc1478 |
| DEPTH_INSERTION_CHECK.md | 77c51e725629e736a33c16dbe4ec179b5aa859b527539815f55422a818a1e977 |
| DEPTH_RESPONSE_MODULUS.md | e32e3608e5a02d6f9aefb88cf77890f9110a8d65bede6faedf2f215d84dc6d24 |
| UNBOUNDED_ACTIVATION_CANDIDATE.md | e939e971d7a9e1b884b42d73d3ce65f5b1f548d9e25ab9cfe76c0502aa591713 |
| UNBOUNDED_INSERTION_CHECK.md | bec5707fccc99597570ce51c94d3a487fd0b1ede14578617275cb708fdd95578 |
| GENERAL_SELF_AVERAGING.md | bfbc14cbb3cccf902420db74ca6e3627e341f27a84b52a229362848b376a56d5 |

Complete dependency reading and their local reconstruction are recorded
in POPULATION_DIRECT_CHECK.md. The unchanged required skills,
canonical manuscript model and maintained notation contract were reused.
No other study, archived book, external scientific source or numerical
experiment was used.

Original and repaired source copies are retained for comparison in
data/generated/dense_cutoff_population_rate_20261001/population_adjacent_check_20261003/.
Commands used were source reads, SHA-256 calculations, byte counts,
and a no-index source diff. Mathematical verification consisted of
the normalization substitution, Gaussian density identity, exact
augmented Jacobian, first-variation subtraction, coordinate-matched
trace contraction, rank-\(m\) Duhamel estimate, conditional
maximum calculation and exchangeability identity written above.
No simulation, GPU probe, Git staging or commit was performed.

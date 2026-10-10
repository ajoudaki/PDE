# Internal check of the multisample nonlinear bad-basin theorem

2026-10-10. Checker: /root/residual_alignment_route.

**PASS for the stated theorem.** No correction or unresolved mathematical
objection was found in the frozen source. This is a reused-context internal
check, not a blind independent attempt or promotion review. Its conclusion
is limited to the specified activation pair, label family, admissible finite
dataset, and positive-probability basin at each fixed width.

## Source, coverage, and method

The sole scientific input was the complete 603-line
MULTISAMPLE_NONLINEAR_BAD_BASIN.md, SHA-256:

0900b6bd77d1e622a74ccda3d4190996a6700283b37041bbce718a59615a8d33

I read every scientific line, all nine sections and equations (1)--(25),
including proof bodies, the example, provenance, and qualifications.
The complete cat read was not truncated; sha256sum verified the version
and wc -l verified the line count. Required proof, canonical-notation,
neural-network, and research-process instructions were applied.

No other study, author route message, external paper, simulation, or formal
verification was used. The agent previously checked related study material,
but reconstructed this proof from its assigned self-contained source.
Prior findings were not proof dependencies. The check used algebraic
reconstruction, dimensions, normalization, edge cases, and probability
and limit-order audits.

Before this report, HEAD was c17cb8c2e8d486ccc1d2b80e8cd173ba551145ae
and the shared index was empty. The untracked source was not edited.
This report is the only assigned write; no staging or commit was performed.

## Model, regularity, and existence

The factors in (5) agree with mean loss, readout normalization 1/n, and
mobilities (n,1,n). The first-layer and readout mobilities cancel the
output derivative's 1/n, while the hidden-matrix update retains it.
The residual is correctly outside the backward vector.

The label norm is
\[
\|y\|^2=a^2[(m+1)^2+(m-1)]=a^2m(m+3).
\]
Thus the initial loss and label RMS are correct. The displayed tanh
modulus formula proves the bound on the closed strip of half-width
pi/4. The stated Cauchy disks lie inside that bounded holomorphic region.
Cosine and its derivatives have the asserted bounds on fixed strips.
Both activations meet the stipulated bounded strip-analytic subclass.

The energy identity and Cauchy--Schwarz give (6). At a hypothetical
finite maximal time the parameters are Cauchy in a fixed positive
metric and have a finite limit where local existence extends the
solution. This proves finite-time global existence, without an
infinite-time boundedness claim. The argument also applies to the
nonzero-readout states used for local trapping.

## Data span and Gaussian population gaps

Every hyperplane in Section 3 is proper: its normal is an input vector,
a difference of distinct inputs, or a sum of non-antipodal inputs.
A finite union cannot cover the ambient space. The selected projections
are therefore nonzero with distinct absolute values, including when m>d.

For an annihilating relation, restriction to g=t b first cancels the
limiting signs as t tends to positive infinity. After subtraction, the
smallest absolute projection supplies the unique slowest exponential.
Rescaling isolates its coefficient. Removing that entire term permits
iteration until all coefficients vanish. Integer-multiple relations
between projection magnitudes do not obstruct this procedure.
The available feature vectors thus span the whole sample space.

One may select m finite first-weight rows giving independent feature
rows and pad to any n>=m. This gives full column rank without input
linear independence.

For each nonzero sample vector, its linear combination of first
features is continuous and nonzero somewhere, hence on an open set of
positive Gaussian measure. This proves Q^(1)>0. The resulting Gaussian
has full support in R^m. The second activation maps this space onto
[1,2]^m, which is not contained in any proper linear hyperplane.
The same continuity and density argument proves Q^(2)>0. All moments
exist because the activations are bounded.

These are positive gaps for each fixed admissible dataset. There is
no uniform conditioning claim near repeated or antipodal inputs.
Those excluded configurations would invalidate the first span step.

## Reference path and full-network local minimum

The right-inverse construction in (9) gives W_*U_*=Z_* exactly.
Vanishing top derivatives keep both hidden blocks fixed on the reference
path. For v=(2,1,...,1),
\[
\|v\|^2=m+3,\qquad v^\top y=a(m+3),\qquad v^\top(av-y)=0.
\]
The scalar readout equation, its rate, and loss (11) follow with the
stated factors. The endpoint residual has squared norm
a^2(m-1)(m+3), giving (4).

Positive readouts and the activation interval [1,2] imply all cone
inequalities f_1<=2f_j. The residual pairing in (12) is exactly
a times the sum of 2f_j-f_1 over j>=2. This proves local minimality
under full parameter variations in a positive-readout neighborhood.
Signed readouts elsewhere can fit using any full-rank feature matrix.
The rank-one reference is correctly distinguished from the theorem's
full-rank perturbed starts.

## Coordinates, Hessian, and open trapping

Equation (13) is an explicit smooth inverse whenever the selected
m-by-m minor of U(A) is invertible. The coordinate dimension is
\[
nm+nd+n(n-m)+n=nd+n^2+n,
\]
the original parameter dimension. No invertibility of W_* is needed.
For n=m the complementary weight block is empty and the chart remains
valid.

At fixed complementary coordinates the loss depends only on Z and w.
The quadratic coefficient of the mean-readout shift is (m+3)/m.
Pairing the quadratic cosine changes with residuals -(m-1)a and 2a
gives exactly (14). Terms involving that shift times squared feature
deviations are cubic. Differentiation gives all Hessian entries in (15),
including the factors of two. They are uniformly positive for m>=2,
a>0, and the stipulated positive-readout neighborhood.

On a smaller box, Taylor's integral formula gives quadratic loss-excess
bounds and a lower bound on the transverse gradient. Bounded chart
derivatives on a compact neighborhood transfer that bound to the
physical gradient with fixed positive mobility. Tangential equilibrium
directions do not invalidate this argument.

With metric speed V, one has -E'=V^2 and V>=c_3 sqrt(E). Thus
\[
V=\frac{-E'}{V}\le\frac{-E'}{c_3\sqrt E}
\]
where E>0. Integration gives the exact 2/c_3 factor in (17).
At E=0, local coercivity puts the state on the equilibrium manifold,
resolving the zero-denominator case.

A smaller starting neighborhood has positive distance from the outer
boundary and arbitrarily small loss excess. The length estimate
excludes first exit. Exponential excess decay, finite total path, and
completeness give a finite equilibrium limit. This is an ambient open
attracting set, including complementary parameter directions.

At a finite time the exact path enters that set. Its continuous
preimage is open in the full hidden-parameter space with readout fixed
at zero. No positive-mass assertion about a zero-readout hyperplane under
a nondegenerate random-readout law is being used; zero readout is
prescribed.

## All-time first-feature conditioning

The outer box can enforce operator distance less than sigma_*/2 from
U_*. For every sample vector,
\[
\|U(A)c\|\ge\|U_*c\|-\|(U(A)-U_*)c\|
\ge\frac{\sigma_*}{2}\|c\|.
\]
This yields sigma_*^2/(4n) in (18). Uniform finite-time continuous
dependence around the reference, whose first weights remain constant,
gives the same bound before entry into the box; trapping gives it
afterwards. This is a valid all-time estimate local to the basin,
not a nonlinear balance invariant or typical-Gaussian bound.

## Full initial rank and actual motion in both layers

Subtracting the first row from the next m-1 rows of the proposed
feature minor gives determinant 2 times the product of delta_j.
It is nonzero for the stated perturbations, including m=2 and n=m.
The associated W perturbation can be arbitrarily small through the
fixed finite right inverse of U_*.

At zero readout the hidden velocities vanish. Differentiating their
updates leaves only the term arising from dot(w)=2Hy/m. This reproduces
both equations (20), including the extra width factor in ddot(W).

With only entry (2,2) perturbed, the single nonzero response entry has
the stated coefficient because
\[
y_2=-a,\qquad (Hy)_2=a(m+3-\delta_2),\qquad
\phi_2'(\pi+\epsilon_2)=\tfrac12\sin\epsilon_2.
\]
It is negative and nonzero for sufficiently small positive epsilon_2.
All lower activation derivatives are strictly positive at finite
parameters. The selected weight row is nonzero because it produces a
nonzero preactivation row; the normalized input has norm one. These
facts prove both nonzero expressions in (21), including actual motion
of the first feature vector rather than just its weights.

Full column rank makes the selected lower feature column nonzero, so
ddot(W) is nonzero. Differentiating Z=WU produces exactly the two
nonnegative squared-norm terms in (22), multiplied by the same
nonzero coefficient. No cancellation is possible. Multiplication by
the nonzero top derivative yields a nonzero negative top-feature
acceleration. Initial preactivation velocity is zero, so its squared
velocity contributes nothing. Only the selected input's self-inner-
product is used; correlated cross-sample products are not discarded.

For m>2, fixing epsilon_2 first and choosing all other nonzero
perturbations sufficiently smaller preserves these strict nonzero
quantities by continuity, while the determinant ensures full rank.
Basin membership, initial Gram positivity, and nonzero accelerations
are open conditions. Their intersection gives the claimed ambient
open set.

This proves movement at each fixed width. It does not give a
width-uniform lower bound on motion amplitude or an order-one nonlazy
limit. The source explicitly retains that limitation.

## Strict loss decrease, tangent cancellation, and probability

Near the reference, Hy has positive entries. The initial squared
metric speed is 4||Hy||^2/(m^2 n), agreeing with (23).
A nonstationary solution of a smooth autonomous equation cannot reach
an equilibrium at finite time: backward local uniqueness would
identify it with the constant solution and extend that equality back
to initialization. Thus the loss derivative is strictly negative at
every finite time.

At the endpoint all top activation derivatives vanish. This removes
every hidden-parameter derivative of each prediction, including paths
through the nonlinear first layer. That conclusion needs more than
feature rank loss, and the proof supplies the required derivative
condition. The remaining readout Gram is vv^T, which annihilates the
actual limiting residual.

Formula (25) has the correct normalization:
\[
-\frac d{dt}\log\mathcal L
=\frac4m\frac{r^\top Kr}{\|r\|^2},\qquad
\frac{\mathcal L(0)}{\mathcal L(\infty)}=\frac m{m-1}.
\]
Integration gives m log(m/(m-1))/4. Positive limiting loss prevents
a zero denominator.

The Gaussian hidden law has positive density everywhere, so the
nonempty open basin has positive probability at each fixed dataset,
width, and amplitude. No probability lower bound uniform in those
parameters follows. The basin's empirical initial gaps need not
approximate its positive population gaps.

The construction works at every a>0. It therefore does not identify
a critical large-label threshold or establish necessity of a small-label
hypothesis in a high-probability theorem. The gap and probability
quantifiers in such a theorem are separate.

## Edge cases, example, and final scope

The m=2 specialization consistently gives the endpoint, loss ratio,
rates, Hessian coefficients, single rank perturbation, and residual
integral. The n=m chart has the correct empty complement. The m>d
case is covered by functional independence, not input-vector
independence.

The three-sample circle example has the stated inner products and
linearly dependent inputs. It gives initial loss 6a^2, limiting loss
4a^2, reference readout rate four, and excess-loss rate eight.
Those reference finite-time formulas are correctly not asserted for
the perturbed trajectories.

No mathematical correction is requested. The precisely stated theorem
is internally checked: an explicit nonlinear bad basin with full initial
feature rank, actual feature motion, and a local all-time first-feature
gap. It is not a theorem for arbitrary labels or activations, a
width-uniform Gaussian failure result, or a compression lower bound.
No broader research claim was investigated or accepted in this check.

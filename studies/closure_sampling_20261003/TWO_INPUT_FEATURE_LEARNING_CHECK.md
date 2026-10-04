# Internal check of width-independent two-input feature motion

2026-10-03. Scoped complete reconstruction of
`TWO_INPUT_FEATURE_LEARNING.md`, 410 lines, SHA-256
`acea496ead5b36e57ed5b6712c52eb1d9137b15ebb9203a8d183a774cbc27e0d`.
The full source was read, including its compressed-model transfer and
claim boundaries. Previously read authorized model, real stability,
source, and compression notes supplied context; no other reviewer's
verdict was used. No experiment, source alteration, Git operation, or
cross-study input was used. Canonical notation, rigorous-proof, and
adversarial-audit instructions apply.

**Verdict: PASS for the stated claim.** The proof gives simultaneous
width-independent lower and upper bounds `c|y|^2,C|y|^2` on both
training-feature tuple displacements at one fixed positive physical time,
on a label-independent initialization event of probability tending to
one. No blocking gap was found. The compressed-model consequence is
valid for each fixed nonzero small label vector after the previously
checked source and comparison inputs are supplied; its width threshold
may depend on that fixed label magnitude.

This is an internal collaborative check, not an independent promotion
review or permission to modify the maintained book.

## 1. Exact model and short-time estimates

With normalized inputs `e_1,e_2`, loss `sum_a(f_a-y_a)^2/2`, and
mobilities `(n,1,n)`, the displayed equations have precisely the correct
normalization. The regular-coordinate relation
`Psi'(a)=cosh^2(a)` gives `u_dot_a=c_a W^T delta_a`, while
`sigma'(u_a)=sech^4(a_a)`.

The real tangent matrix is positive semidefinite, so its residual
equation implies `|c(t)|<=Y=|y|` on every existence interval.
For `0<=t<=1`, `Y<=1`, and initialized operator bound `K`, integration
gives `||w||_infinity<=CYt`, `||W-W_0||_F<=CY^2t^2`, and
`||u_a-u_{a,0}||_n<=CY^2t^2`. The operator tube and real Lipschitz
gates then give all forward bounds (4)--(5). At fixed finite width these
increment estimates prevent escape, justifying existence on the full
short interval.

The residual tangent matrix has bounded operator norm on this tube:
its top Gram is bounded, its mixer Gram is `O(Y^2t^2)`, and the
first-layer diagonal is bounded by the normalized squared carrier norm,
also `O(Y^2t^2)`. Therefore `c(t)-y=O(Yt)` with a dimension-free
constant. For the initialized readout velocity
`v=sum_b y_b g_{b,0}`, bounded initial gates imply
`||v||_infinity<=sqrt(2)Y`. Integrating the readout equation gives

\[
 \|w(t)-tv\|_n\le CYt^2.
\]

Pairing this estimate with bounded gates, and bounding the gate change
by `||v||_infinity ||z_a-z_{a,0}||_n`, gives
`||delta_a-t d_{a,0}^v||_n<=CYt^2`. Multiplication by `W_0^T`
and the learned-mixer correction give
`||k_a-t k_{a,0}^v||_n<=CYt^2`. Consequently the difference between
`u_dot_a` and `t y_a k_{a,0}^v` has normalized norm at most
`CY^2t^2`, proving the integrated remainder `CY^2t^3` in (7).

Only normalized second moments occur in this calculation. In particular,
the proof does not infer an `L^2` bound on the quadratic remainder of
`sigma` from an `L^2` bound on its argument increment.

## 2. The initialized moment event is uniform over label directions

For the fixed truncation radius `R_0>0`, every map
`a -> tanh(a)` and `a -> tanh(a) 1_{|a|<=R_0}` is bounded and odd.
Thus the empirical covariance of the four initialized feature columns
converges to a block diagonal matrix, with no cross-sample correlations.
Within one sample, the full variance is `q`, the truncated variance is
`q_R`, and their covariance is also `q_R`.

Conditioned on these first-layer columns, each row of their mixer images
is a centered Gaussian tuple with that empirical covariance. For each
entry of `M_n`, the row summand is one Gaussian coordinate times bounded
gates. Its conditional second moment is at most the variance of that
coordinate, hence uniformly bounded by one. Conditional Chebyshev gives
an `O(1/n)` probability bound for any fixed deviation from the conditional
mean. The conditional means converge by continuity of Gaussian
expectations. That continuity remains valid for the linearly growing
summand: bounded covariance gives uniformly bounded second moments, and
therefore uniform integrability in a Gaussian square-root coupling.

For a limiting sample pair `(Z_a,Z_a^R)`, Gaussian regression gives
`E[Z_a^R|Z_a]=(q_R/q)Z_a`. The other sample is independent. The
diagonal mean is therefore

\[
 \tau=(q_R/q)\,\mathbb E[Z\tanh Z\operatorname{sech}^2Z]>0,
 \qquad Z\sim N(0,q).
\]

The off-diagonal means vanish because the other sample's tanh is odd
and centered. Thus `M_n -> tau I_2` in probability. The matrix need
not be symmetric at finite width, but its symmetric part has the stated
gap with probability tending to one, which is exactly what a quadratic
form `y^T M_n y` needs.

For `H_{a,n}`, the conditional summands are bounded, and the same
covariance limit gives the displayed positive diagonal limit and zero
off-diagonal entries. The lower-feature Gram tends to `qI_2` by the
ordinary law of large numbers. There are only finitely many entries and
matrices, so their gap events can be intersected with the operator event
while preserving probability tending to one.

No label occurs in the definitions of these random matrices or their
event. Their matrix gaps consequently hold simultaneously for every
label direction. No finite net over labels, independence from an adaptive
label choice, or lower bound on an individual label component is needed.

## 3. First-layer lower bound without hidden fourth moments

The initialized test
`b_a=h_{a,0}^R odot sech^{-4}(a_{a,0})` is bounded by the fixed
constant `B_0=cosh^4(R_0)` because it vanishes outside the cutoff.
It is a test vector only; the network dynamics and its initialization
are unchanged. Its product with `sigma'(u_{a,0})` equals
`h_{a,0}^R` exactly.

Applying the scalar Taylor formula to `sigma` and then pairing with
this bounded test gives

\[
 \sum_a\langle b_a,h_a(t)-h_{a,0}\rangle_n
 =\frac{t^2}{2}\sum_{a,b}y_ay_b
       \langle W_0h_{a,0}^R,
           g_{b,0}\operatorname{sech}^2z_{a,0}\rangle_n
   +E_h(t).
\]

This is precisely `t^2 y^T M_n y/2`. The linear remainder is
`O(B_0Y^2t^3)` by (7). The nonlinear remainder is estimated in
normalized `L^1` after pairing:

\[
 |\langle b_a,R_a\rangle_n|
 \le CB_0\,n^{-1}\sum_i|u_{a,i}(t)-u_{a,i}(0)|^2
 \le CB_0Y^4t^4.
\]

Thus the claimed bound uses exactly the known `L^2` increment norm and
does not require an `L^4` increment or a maximum trained carrier.
The positive symmetric gap gives leading term at least
`tau Y^2t^2/4`. A fixed sufficiently small `t_*` makes the remainder
at most half that quantity for every `Y<=Y_*<=1`. Cauchy--Schwarz
with test-tuple norm at most `sqrt(2)B_0` proves (14), with its
displayed normalization and a constant independent of width and labels.
The already proved short-time RMS estimate gives the upper bound.

## 4. Exact second-layer identity and its positive leading energy

Here `v` remains fixed at its initialized value, while
`d_a^v(t)=v odot sech^2 z_a(t)` and
`K_a^v(t)=W(t)^T d_a^v(t)` use the current hidden state. The initialized
gap gives `||d_a^v(0)||_n^2=y^T H_{a,n}y>=mu_0Y^2`. Bounded
gate derivatives imply its norm changes by at most `CY^3t^2`.
The lower-feature Gram changes by `CY^2t^2`. Choosing the same fixed
time and label thresholds smaller preserves both inequalities in (15).

For
`P(t)=sum_a y_a <v,g_a(t)-g_{a,0}>_n`, differentiating the true
forward pass gives exactly

\[
 \dot P=
 \sum_{a,b}y_ac_b\langle d_a^v,\delta_b\rangle_n
                       \langle h_a,h_b\rangle_n
 +\sum_a y_ac_a\langle K_a^v,\sigma'(u_a)\odot k_a\rangle_n.
\]

The mixer contribution has two factors of `1/n`, one from its update
and one from the prediction pairing, as encoded by the two normalized
inner products. The first-layer contribution follows by moving the
current matrix to its transpose. Neither term differentiates a carrier.

The decomposition `delta_a=t d_a^v+epsilon_a` is exact, with
`||epsilon_a||_n<=CYt^2` from the readout estimate; applying `W^T`
gives the stated carrier decomposition. Substituting these decompositions
and `c=y+O(Yt)` gives the two leading energies in (17). Every remainder
is `O(Y^4t^2)`: for example a mixer error contributes at most
`|y_a c_b| ||d_a^v||_n ||epsilon_b||_n<=CY^4t^2`, while replacing
`c_b` in a leading term contributes
`t |y_a| |c_b-y_b| ||d_a^v||_n ||d_b^v||_n<=CY^4t^2`.
The first-layer error is bounded identically after using the operator
bound for `W^T epsilon_a`. These arguments do not require coordinate
maxima of `K_a^v` or `k_a`.

The mixer energy is the exact Frobenius square

\[
 \left\|n^{-1}\sum_a y_a d_a^v h_a^\top\right\|_F^2
   =y^\top(D\odot Q_h)y,
 \qquad D_{ab}=\langle d_a^v,d_b^v\rangle_n.
\]

Write `Q_h=q_0 I/2+R` with `R` positive semidefinite. Since `D`
is also a Gram matrix, `D odot R` is a Gram matrix of tensor products
and is positive semidefinite. Therefore this square is at least
`(q_0/2) sum_a y_a^2 ||d_a^v||_n^2>=c_0Y^4`, for every sign
pattern. The other leading term is manifestly a sum of nonnegative
squared norms with coefficients `y_a^2`.

For fixed `t_*<=c_0/(2C)`, the error cannot cancel more than half
the leading `c_0Y^4t` contribution. Integration gives
`P(t_*)>=c_0Y^4t_*^2/4`. The test tuple has norm
`Y||v||_n<=sqrt(2)Y^2`, so Cauchy--Schwarz yields the stated
`cY^2` lower bound on the second-feature displacement itself. The
short-time forward estimate gives its upper bound.

All time restrictions in Sections 3--4 are fixed inequalities involving
`K,R_0,tau,q_0,mu_0`. Their minimum is a fixed positive `t_*`.
All label restrictions can likewise be met by one fixed positive `Y_*`.
This verifies that the proof establishes finite positive physical-time
motion, rather than only a nonzero curvature at time zero.

## 5. Transfer to the weighted compressed dynamics

For either layer, expand the squared feature displacement into its two
same-time pairings and its mixed pairing with initialization. The source
cubature controls each pairing with absolute error `Cepsilon`; therefore
the selected weighted squared displacement differs from the full empirical
one by at most `Cepsilon`, uniformly over the two training samples.
This step controls squared norms and cannot be replaced by an unsupported
pointwise state estimate on the selected nodes.

The dynamical comparison supplies first-feature error `Cepsilon` in the
weighted norm through the real Lipschitz coordinate map. For second
features it supplies `Cepsilon` using the bounded mixer and the separate
forward source defect. Initial selected training features match exactly.
For fixed `Y>0`, choose width large enough that
`Cepsilon` is smaller than a fixed multiple of the full squared-motion
lower bound `Y^4`, and that the dynamical feature error is smaller than
a fixed multiple of `Y^2`. Taking square roots and applying the triangle
inequality gives (21). No minimum cubature mass enters.

The first condition can be the stricter one for small labels. Since
`epsilon=O(n^{-1/2})`, this transfer does not assert one width threshold
uniform over the entire punctured label ball. The source explicitly
states the correct quantifiers: full-network bounds hold simultaneously
over that ball on one event, while compressed transfer is for each fixed
nonzero label vector at sufficiently large width. Existing finite
curvature vectors may remain in the source spaces but are unnecessary
for this stronger transfer.

## 6. Scope and remaining boundaries

No missing estimate or blocking inference was found in the checked
source. The proof establishes a lower bound for the tuple of the two
training features in each hidden layer. It does not assert the same
lower bound for each sample individually, a uniform shrinking-label
compression regime, or nonzero displacement at the fitted endpoint.
Those stronger claims are neither needed nor made.

The result strengthens the previously checked finite-width curvature
certificate to motion of order `Y^2` at a fixed positive physical time,
with constants independent of width. Its initialized truncation is only
inside a bounded test vector and does not replace the canonical Gaussian
network. The full-network result uses no complex source theorem; only
its compressed-model consequence depends on that separately checked
construction.

## 7. Final author-version confirmation

The author subsequently changed only dependency and check-status prose
in the feature note, giving SHA-256
`75d317cbcfca5cbf3f4a2b4e11a07bd094ab7daff78fcae204b19760db3fb8c7`.
That complete version was reread. All definitions, estimates, probability
quantifiers, and proofs checked above are unchanged. The PASS verdict
therefore covers this final version as well. References to other check
files in the revised source were read as status prose only; those other
verdict files were not opened or used as mathematical evidence.

The revised assembly, stability, and complex-source versions were also
reread, with final hashes and the scope of their changes recorded in
Section 8 of `TWO_INPUT_CANONICAL_COMPRESSION_CHECK.md`. None changes
the mathematical transfer in Section 5 of this check. In particular the
feature lower bound transfers to the actual continuing autonomous
compressed model at the same fixed positive physical time.

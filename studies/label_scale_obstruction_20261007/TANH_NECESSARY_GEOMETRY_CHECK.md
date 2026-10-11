# Cross-check of the finite-equilibrium geometry

Verdict: PASS for the stated algebraic and local-minimum results. No substantive
mathematical error or missing hypothesis was found. The result does not prove
attraction, convergence of trajectories, or Gaussian saddle avoidance.

This is a reused-context author cross-check by the
`tanh_global_limits` scoped agent, not an isolated review and not a promotion
review. The reviewer previously authored
`GLOBAL_FAILURE_ALTERNATIVES.md` in this study and received the supervisor's
four-sample escape construction. Those facts are disclosed because this check
must not be counted as fresh independent promotion evidence.

## Frozen input and method

The complete 694-line scientific input was
`TANH_NECESSARY_GEOMETRY.md`, SHA256

```text
770527741d5a9acf76cb9c44e917be8eb9894edff6f02fc03c922f3ecb795b0f
```

The hash was verified before and after the check. All lines, including the
second-variation formulas, analytic continuation argument, separation lemma,
and cubic-descent calculation, were read. Required process and mathematical
skills had already been read and remained current. No other study, external
scientific source, experiment, or candidate edit was used.

Method: reconstruct the chain-rule formulas; expand each null-direction mixed
variation directly; check rank implications and all zero-coordinate cases;
verify the real-analytic continuation and ridge-separation arguments; and
recompute the full-column-rank classification and its descent coefficient.
The report records the actual algebraic checks below. No numerical test is
needed for these exact statements.

## Findings

### Gradient, Hessian, and Schur-complement test

The gradient factors \(2/(mn)\) and all matrix dimensions agree with

\[
f=H^\top w/n,\qquad
\mathcal L=\|f-y\|^2/m.
\]

In particular,

\[
\delta^2(WU)=2C\,\delta U+W\,\delta^2U
\]

along an affine direction \((B,C)\), so the mixed term in equation (4) is
necessary and correctly included. The output expansion gives

\[
\delta^2\mathcal L
=\frac2m\left(\|\delta f\|^2+r^\top\delta^2f\right),
\]

with both readout/hidden mixed contributions represented in equation (5).

The block decomposition (7) is exact. Since \(G=F^\top F\) and
\(\ker G=\ker F\), a positive-semidefinite block matrix requires
\(Kv=0\) for \(v\in\ker F\). For those vectors the term \(J^\top Fv\)
vanishes, leaving precisely \(C_0v=0\). The stated completion of the square
then proves both directions of (8)--(9), including singular \(G\).
The result is correctly described as an exact Hessian test, not as a
classification of higher-order local minimality.

### Universal derivative annihilation

For an inactive readout coordinate \(w_i=0\), varying only row \(i\) of
\(W\) leaves the output constant along the entire affine line. Its pure
Hessian value is therefore zero. A positive-semidefinite Hessian must pair
this direction to zero with every other direction, including the readout
coordinate \(i\). The mixed output derivative is

\[
\frac1n\operatorname{diag}(d_i)U^\top c.
\]

Pairing with \(2r/m\) gives exactly

\[
\frac{2}{mn}c^\top U(d_i\odot r).
\]

Thus Proposition 1 validly extends the first-order active-neuron equation to
every second-layer row. Because each \(d_i\) has positive entries, a nonzero
residual then forces both \(\operatorname{rank}U<m\) and
\(\operatorname{rank}H<m\). No unjustified division by \(w_i\) occurs.

### Redundant-row geometry

For \(b\in\ker U^\top\), the direction

\[
C=\varepsilon_i b^\top
\]

satisfies \(CU=0\), and thus leaves the output constant when \(A,w\) are
fixed. Pair it with an arbitrary first-layer direction \(B\). Its first
output derivative is zero, eliminating the squared-Jacobian contribution.
The second activation's curvature term also vanishes because its
first preactivation derivative in the \(C\) direction is zero. The only
mixed preactivation term is

\[
C\,[E\odot(BX)].
\]

Consequently the mixed loss Hessian is exactly

\[
\frac{2w_i}{mn}
\sum_j b_j B_{j,:}X(e_j\odot d_i\odot r).
\]

The independent freedom of each row of \(B\) proves (16) whenever
\(w_i\ne0\) and \(b_j\ne0\). The definition of the redundant index set
allows \(b\) to depend on \(j\), so there is no unsupported common-vector
requirement. Stacking the resulting equations with Proposition 1 yields
the rank condition for \(\mathcal T_U\).

The count of at least \(n-\operatorname{rank}U\) redundant indices is valid:
the nonredundant rows are linearly independent, hence number at most
\(\operatorname{rank}U\). A zero row is correctly included as redundant.
The width assumption \(n\geq m\) makes this set nonempty at positive-loss
second-order stationary points.

### Critical-zero interpretation

In the definition of \(\Phi_i\), both \(r\) and \(d_i\) are explicitly frozen.
With this convention,

\[
\nabla\Phi_i(A_{j,:}^\top)=X(e_j\odot d_i\odot r)
\]

is correct; differentiating those coefficients as if the entire network
were changing would be a different operation. Proposition 1 gives the
zero-value condition for every first-layer row, while Proposition 2 gives
the critical-point condition only for redundant rows and active second-layer
indices. The text keeps these quantifiers separate.

Lemma 4 applies to the stipulated nonzero, distinct, nonantipodal columns
and ensures that \(\Phi_i\) is not identically zero when \(r\ne0\). It
does not rule out critical zeros, neuron collisions, or other singular
configurations; the candidate makes no such claim.

### Zero-readout and flat-coordinate arguments

At \(w=0\), all hidden-only loss derivatives vanish because the prediction
is identically zero under hidden-only changes. The Hessian is therefore
positive semidefinite exactly when every hidden/readout mixed block
vanishes, leaving only \(2HH^\top/(mn^2)\). The two families of mixed blocks
are exactly (19) and (20), with no missing cross-neuron sum.

For Proposition 5, a local minimum at zero readout implies
\(y^\top h_i(A,W)=0\) on an open hidden-parameter neighborhood: otherwise
the linear term of the one-coordinate readout variation lowers the loss
for a sufficiently small signed readout. The real-analytic identity
principle applies on the connected full Euclidean parameter space.
The subsequent one-row construction reduces the identity to the
one-dimensional ridge-separation lemma and forces \(y=0\), contradicting
positive loss.

The continuation argument is valid: restricting a real-analytic function
to an affine line gives a real-analytic function on the whole real line;
vanishing on an interval extends across any finite endpoint by its
convergent Taylor series. The separation lemma is likewise valid. After
choosing pairwise distinct nonzero absolute projections, subtracting the
constant large-\(t\) limit isolates the smallest exponential rate and
eliminates coefficients one at a time. It does not require rationally
independent rates or linearly independent input columns.

Propositions 6 and 6a correctly use nearby flat points as local minima:
they have the original minimum value, and sufficiently small balls around
them remain inside the original minimizing neighborhood. Thus stationarity
holds throughout the relevant open flat slice. Analyticity and Lemma 4 then
give the grouped residual condition for one zero readout coordinate and
exclude zero columns of \(W\) at positive-loss local minima. Zero feature
columns, exact sign collisions, and arbitrary nonzero scalar multiples are
handled correctly; the sign partition does not incorrectly merge different
absolute magnitudes.

### Full-column-rank classification and cubic descent

Assume \(\operatorname{rank}X=m\), \(n\geq m\), and \(y\ne0\).
Positive-loss second-order stationarity implies
\(\operatorname{rank}U<m\), hence there is a redundant first-layer row.
For any such row \(j\),

\[
X\operatorname{diag}(e_j)
\]

has column rank \(m\). This contradicts Proposition 2 if \(w\ne0\), so
\(w=0\). At zero readout, equation (20), injectivity of \(X\), and positivity
of \(e_j,d_i\) force every \(W_{ij}=0\). Equation (19) then reduces to
\(Uy=0\). Conversely these three conditions make the gradient and all
Hessian blocks vanish. The classification

\[
w=0,\qquad W=0,\qquad Uy=0
\]

is therefore both necessary and sufficient for positive-loss
second-order stationarity in the stated data class.

The explicit first-layer direction

\[
B_{j,:}
=(y^\top\oslash e_j^\top)(X^\top X)^{-1}X^\top
\]

is well-defined and produces \(\delta U_{j,:}=y^\top\).
Along the candidate's affine parameter path, direct expansion gives

\[
f(t)=\frac{t^2}{n}u_j+\frac{t^3}{n}y+O(t^4).
\]

The condition \(Uy=0\) cancels the order-two residual pairing.
The squared prediction starts at order four, so the leading loss change is
indeed

\[
\mathcal L(t)-\mathcal L(0)
=-\frac{2\|y\|^2}{mn}t^3+O(t^4).
\]

This coefficient is strictly negative for positive \(t\) and changes sign
for negative \(t\). Thus the Hessian-zero points are not local minima.
Any other positive-loss stationary point has a non-positive-semidefinite
real symmetric Hessian and consequently a negative eigenvalue.
The theorem's classification is complete for second-order stationary points,
and its conclusion that every local minimum fits is justified.

The \(y=0\) edge case is correctly settled using readout stationarity:
\(w^\top Hr=n\|f\|^2=0\), so every stationary point fits regardless of
input rank.

## Limits of this check

The candidate explicitly leaves dependent-input local-minimum classification,
attraction, boundedness, escape, all-time loss convergence, and avoidance from
the zero-readout initialization slice unresolved. This report preserves those
limits. The exact Hessian test and necessary rank conditions cannot themselves
close any of those dynamical questions.

No changes to the frozen candidate were made or requested.

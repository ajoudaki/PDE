# Internal audit of the orthogonal Gaussian tanh theorem

2026-10-10. This is a reused-context internal mathematical audit, **not an
independent promotion review**. No experiment was run and no proof was
edited.

The complete frozen candidate input was `GAUSSIAN_POSITIVE_GEOMETRY.md`,
SHA256

```text
d220fba99906085e9770aceb33b939b5d0cfa2bb2bc005909f31fe2449afa574
```

The additional required maintained input was
`docs/12-three-sample-learning.qmd`, III.F.1–11. The supplied lines 316–1000
were read completely. SHA256 of that exact line range is

```text
dfa7caceb02b1acf7c6519ec94b5ce9e2698a97c258e4cb757c5d1b78a764a51
```

Both hashes were rechecked after completing the audit and remained unchanged.

The candidate's Sections 11 and 13 are the audited fitting theorem. Sections
1, 2, 4, and 6 provide its exact geometry and capture dependencies; these
were also checked directly. Historical references to other chapters were
not used to replace missing hypotheses.

## Verdict and precise scope

**PASS for the stated orthogonal-input theorem and its open label
neighborhood extension.** I found no substantive mathematical error in the
chain from natural-coordinate existence to Gaussian identification,
population fitting, full sample-space readout-plus-middle coercivity, and
exact finite-width capture.

For fixed \(m,d\), orthonormal columns \(X^\top X=I_m\), any fixed
\(a>0\), and any fixed sign vector \(\sigma\), the argument proves that
the actual Gaussian-initialized, exactly-zero-readout, two-hidden-layer tanh
flow fits \(a\sigma\) with probability tending to one. It also proves the
stated deterministic width-independent all-time exponential rate on such
events. For each fixed label vector in a sufficiently small open
neighborhood of \(a\sigma\), it proves actual finite-width fitting by the
same capture mechanism. The neighborhood statement is not a claim of one
event simultaneously covering an uncountable label set.

The input restriction is essential to this proof. It does not construct the
nonorthogonal tanh population flow or settle arbitrary label ratios on
arbitrary data. No promotion conclusion follows from this internal check.

Two small explanatory clarifications would make the proof easier to audit,
but neither changes the theorem: explicitly mention the constant component
of \(A\) orthogonal to the input span when recovering the full parameter
array, and use continuity of the accumulated residual, rather than an
unstated continuity of \(\|w\|_\infty\), when describing the open-label
snapshot bounds. Both details are supplied below.

## 1. Exact natural coordinates

The map

\[
 \zeta(z)=z/2+\sinh(2z)/4
\]

has derivative \(\cosh^2z>0\) and tends to both infinities, so it is a
smooth increasing bijection. Its inverse has derivative
\(\operatorname{sech}^2z\le1\). For
\(\psi(\xi)=\tanh(\zeta^{-1}(\xi))\), direct differentiation gives

\[
 \psi'=\operatorname{sech}^4z,\qquad
 \psi''=-4\tanh z\,\operatorname{sech}^6z.
\]

Thus both inverse recovery and the first transformed activation are
globally Lipschitz; \(\psi\) is bounded and has the required bounded
derivatives.

Under the original scalar ascent of \(g=m^{-1}\sum_a f_a\), the first
preactivation satisfies

\[
 (Ax_a)'=\frac1m\operatorname{sech}^2(Ax_a)\,W^*b_a
\]

when \(X^\top X=I_m\). Multiplying by \(\zeta'\) cancels this one gate
exactly. The middle and readout equations are unchanged. This verifies
(9), including all factors of \(m\). The same calculation gives (10) with
the physical factors \(2/m\). For the opposite-label pair, it gives (6)
and (7) with the displayed signs and one-half factors.

There is no learning-rate or model replacement. The transformed norm is
used only for existence and approximation; the original mobility metric
remains the metric for the gradient and energy identities.

If \(d>m\), write

\[
 A(t)=A(0)(I-XX^\top)+\sum_a z_a(t)x_a^\top,
 \qquad z_a(t)=\zeta^{-1}(\xi_a(t)).
\]

The first term is constant because every original \(\dot A\) is in the
input span. It may be carried as unused independent Gaussian roots in the
population construction and has no effect on predictions or learning.
Thus the transformed sample coordinates recover the full original
trajectory, not a different first-layer parametrization.

## 2. Strong population ODE and removal of the readout clip

For a fixed smooth bounded clip, the coordinate map

\[
 (w,z)\longmapsto\operatorname{clip}_P(w)
                         \operatorname{sech}^2z
\]

is globally \(C^1\) with bounded first partial derivatives. Forward fields
are locally Lipschitz in the tuple of \(L^2\) first coordinates,
Hilbert–Schmidt middle increment, and \(L^2\) readout. Reverse action obeys

\[
 \|W^*b-\widetilde W^*\widetilde b\|_2
 \le\|W\|_{\mathrm{op}}\|b-\widetilde b\|_2
       +\|W-\widetilde W\|_{\mathrm{op}}\|\widetilde b\|_2.
\]

The Hilbert–Schmidt rank-one difference inequality controls the middle
velocity, while Cauchy--Schwarz controls the scalar predictions and
residuals. These estimates prove local Lipschitzness on an actual open
Hilbert-space neighborhood, with constants independent of finite width on
the corresponding bounded balls. The proof does not mistake a bounded
\(L^\infty\) set for an open \(L^2\) neighborhood.

For scalar ascent, \(w'=\bar h\) is pointwise bounded by one whether or
not the clip is active. Hence \(\|w(s)\|_\infty\le s\), and a clip larger
than the chosen finite horizon is inactive. The bounds on \(W\) and
\(\xi_a'\) follow from \(\|u_a\|_2\le1\) and
\(\|b_a\|_2\le s\). They rule out finite-time escape in transformed
state space and permit continuation through every finite feature horizon.

For physical flow, inverse recovery uses the strong curve chain rule of
III.F.9. Tanh satisfies the hypotheses of III.F.10 for scalar prediction
differentiability in the raw parameter space. Therefore the recovered
unclipped curve has the actual gradient energy identity. While the clip is
inactive, \(\|r\|_2\le a\sqrt m\), so
\(\|\dot w\|_\infty\le2a\). A clip above \(2aT+1\) cannot be reached
before \(T\). On local bounded intervals \(\dot w\) is bounded in
\(L^\infty\), so this first-exit statement is also valid for the
pointwise-essential bound, not merely for an \(L^2\) norm. The remaining
state velocities are bounded as stated, giving global strong continuation.

No Frechet differentiability of the nonlinear map \(L^2\to L^2\) is
needed. The bounded-derivative chain rule along strong curves is enough for
inverse recovery, and the maintained scalar-functional result supplies
the gradient identities.

## 3. Fixed finite Gaussian programs: hypotheses and limit order

The initialized transformed coordinates are iid neuronwise tuples
\((\zeta(G_1),\ldots,\zeta(G_m))\) with independent standard Gaussian
entries before transformation. Since \(\zeta\) has at most exponential
growth, these roots have every finite moment. They are independent of the
initialized middle matrix; the second-layer readout root is deterministically
zero. III.F.1 explicitly permits roots with finite second moments without
requiring them to be generated by a bounded-derivative coordinate map.
Thus the unbounded derivative of \(\zeta\) at initialization is harmless.

Every fixed Euler program uses only the following admissible operations:

- bounded-derivative coordinate maps \(\psi,\tanh\), smooth clips, and the
  clipped upper backward product;
- the one initialized Gaussian matrix and its actual transpose, reused
  with their respective layer types;
- finite linear combinations and normalized same-layer contractions;
- locally Lipschitz causal scalar feedback, including residuals and
  coefficients multiplying vector nodes.

The learned middle action is expanded into its original Gaussian action
and finitely many prior rank-one increments. There is no extra random
matrix or unjustified independent resampling of a reverse query. The
feedback extension in III.F.6 covers the scalar coefficients in this
expansion. No division by residuals is used in the finite program.

Zero initial readout creates singular and repeated queries. III.F.5
expressly covers those cases, so no hidden rank-stability assumption is
required. The source rules retain the responses due to forward/transpose
reuse. The proof does not treat an adaptive query as independent of the
initialized matrix.

III.F.7 supplies a common generated pair of probability spaces, a bounded
initialized action, and its actual Hilbert adjoint. The permitted coordinate
functions and real coefficients can be included in the language or obtained
by its stated extension. Both scalar and physical programs can therefore
be realized on the same spaces before using ODE uniqueness. The later
continuous-dependence argument in the labels does not require choosing an
unrelated population space for every label vector.

On the event of initialized operator norm at most ten and bounded
normalized root norms, the transformed clipped vector field has
width-independent local bounds. The common a priori trajectory bounds
permit a slightly larger state ball and a sufficiently small fixed Euler
step. The ordinary Lipschitz Euler estimate then gives a uniform
\(O(\Delta)\) error for finite widths and for the population flow.

The order of approximation is valid: fix the finite Euler mesh; take width
to infinity using III.F; then refine that mesh using the width-independent
error estimate. No fixed-program theorem is applied to a number of
instructions growing with width. Pairwise contractions identify precisely
the readout and middle tangent blocks. Their bounded-factor continuity and
uniform state-speed bounds give the stated compact-time uniform convergence
by a finite time net. This part of the proof uses no first-layer backward
tail estimate and no unproved removal of an unbounded product cap.

## 4. Deterministic symmetry, scalar fitting, and nonextinction

Sign absorption is exact because the whole network is odd in each input:
replacing \(x_a\) by \(\sigma_a x_a\) changes its prediction to
\(\sigma_a f_a\) for every parameter state. The squared loss against
\(a\mathbf1\) is identically the original loss against \(a\sigma\), so
the parameter gradient fields coincide. Orthonormality and the initialized
Gaussian law are preserved.

For positive equal labels, orthogonal transformations permuting the input
columns preserve the Gaussian initialization and the scalar and physical
equations. The already-established limits of predictions and same-layer
contractions are deterministic. Therefore their permutation identities hold
as deterministic population identities. No finite draw is assumed to have
paired neurons, equal predictions, or an exactly symmetric kernel.

Initially the first features are independent centered copies with second
moment \(q_1>0\). The first forward Gaussian-program calculation gives
independent top preactivations of variance \(q_1\), and independent centered
top features with second moment \(q_2>0\). Consequently
\(\|\bar h(0)\|_2^2=q_2/m\), exactly as stated.

The raw gradient identities give \(R'=2g\),
\(g'=\|\nabla g\|^2\ge\|\bar h\|_2^2\), and
\(g^2\le R\|\bar h\|_2^2\). The initial expansions at zero readout
justify the limit of \(R/g^2\), whose derivative is nonpositive.
Thus \(\|\bar h(s)\|_2^2\ge q_0\) and \(g'\ge q_0\) hold globally
along the constructed scalar path. This gives the unique finite endpoint
\(g(s_*)=a\).

Substitution of \(\dot s=2(a-g)\) into the scalar equations gives the
physical equations because every population prediction is \(g\). Strong
uniqueness on the common state space identifies the two paths. The clock
approaches \(s_*\): if it had a smaller limit, its derivative would stay
strictly positive. The displayed exponential loss bound and
\(2\int_0^\infty\sqrt{\mathcal L_\infty}=s_*\) follow with the correct
normalization.

For distinct samples, subtracting the exact natural-coordinate equations
gives the stated inequality

\[
 \| (\xi_a-\xi_b)'\|_2
 \le\frac{2SM^2}{m}\|\xi_a-\xi_b\|_2.
\]

It uses only bounded readout, bounded action, the identity
\(\operatorname{sech}^2z=1-\tanh^2z\), and the Lipschitz constants of
tanh and \(\psi\). Its backward norm inequality prevents finite-time
extinction from the positive initial norm. Injectivity of \(\psi\) then
prevents the first-feature difference from vanishing. For the opposite-label
pair, the analogous sum-coordinate calculation in Section 11.3 has the
correct factor and proves nonzero common first feature.

## 5. Full sample-space endpoint margin

Permutation symmetry gives the entire readout-plus-middle sample matrix
the form \(\alpha I+\beta\mathbf1\mathbf1^\top\), not just equality of
its diagonal entries. The common direction has a strictly positive
readout contribution because \(\|\bar h\|_2^2\ge q_0\).

For any contrast \(f_a-f_b\), a nonzero top-feature difference already
gives a nonzero readout gradient. If that difference is zero, strict
monotonicity gives equal top preactivations and therefore equal backward
vectors. At \(s>0\), \(g(s)>0\) forces \(w\ne0\). Top preactivations
are finite almost everywhere because they are in \(L^2\), and
\(\operatorname{sech}^2z>0\) at every finite real value. Thus this common
backward vector is nonzero. Its tensor product with the nonzero
first-feature difference has positive Hilbert–Schmidt norm. Hence every
pair contrast has strictly positive quadratic form, implying \(\alpha>0\).

This proves positivity on both sample-space eigenspaces. At time zero the
readout Gram is \(q_2I\). Strong continuity, bounded readout on the finite
feature interval, and compactness then yield a deterministic strictly
positive minimum eigenvalue \(\kappa\) on \([0,s_*]\).

This is a full \(m\)-dimensional margin. It is sufficient to control
finite-width errors outside the symmetric residual direction and does not
require positivity of the output-feature Gram alone.

## 6. Exact finite-width capture and all-time exponential decay

I checked all normalizations in the capture formulas. With
\(s=2\int_T^t\sqrt{\mathcal L}\), the exact moving-parameter bounds give
\(\|\Delta W\|_F\le ps+s^2/2\). Since
\(\|X\|_{\mathrm{op}}=1\), the normalized first-feature displacement is
at most

\[
 \alpha(s)=\frac1{\sqrt m}\left[bM_p(s)+M_p(s)^2/2\right].
\]

The top-feature bound \(\delta\), backward-vector bound \(\chi\), and
concatenated Jacobian bound \(J\) then follow by product differences and
\(|\Delta\operatorname{sech}^2z|\le2|\Delta h|\). The readout-plus-middle
Jacobian is measured in the actual mobility metric.

If its initial sample Gram is at least \(\lambda I\), a Jacobian
displacement smaller than \(\sqrt\lambda/2\) leaves the Gram at least
\(\lambda I/4\). On this interval loss decays at rate \(\lambda/m\),
which bounds the remaining accumulated residual by
\(4\sqrt m\|r(T)\|_2/\lambda\). The strict displayed condition on
\(J\) therefore prevents a first exit. This proves actual finite-width
zero limiting loss and controls every later physical time.

The snapshot is reached using a single deterministic physical time.
Compact-time convergence gives the residual and kernel bounds, and uniform
loss convergence gives convergence of the accumulated residual by
\(|\sqrt u-\sqrt v|\le\sqrt{|u-v|}\). Exact finite-width bounds then
give \(\|w_n(T)\|_\infty\le s_*+1\) and
\(\|W_n(T)\|_{\mathrm{op}}\le10+(s_*+1)^2/2\) with probability tending
to one. No infinite-time approximation theorem is assumed.

On \([0,T]\), compact-time kernel convergence and the population margin
\(\kappa\) give a finite-width gap \(\kappa/2\), hence loss decay rate
\(2\kappa/m\). Combining this with the later rate \(\lambda/m\) proves
the stated bound from time zero with
\(c=\min\{2\kappa,\lambda\}/m\). The initial prefactor remains exactly
\(\mathcal L_n(0)=a^2\). Width appears only in the probability of entering
the deterministic estimates; the infinite-time fitting conclusion is
proved separately at each finite width.

## 7. Open label neighborhoods

On a fixed physical horizon, a single sufficiently large readout clip is
inactive for all labels in a bounded neighborhood of the equal-label
vector. The clipped transformed vector field is jointly locally Lipschitz
in state and labels on the common bounded ball. Subtracting its integral
equations and applying Gronwall gives uniform strong continuous dependence
on labels. Predictions and the readout-plus-middle kernel consequently
depend continuously on labels.

To justify the snapshot norm bounds without invoking continuity of an
\(L^\infty\) norm, define

\[
 S_y(T)=2\int_0^T\sqrt{\mathcal L_{\infty,y}(t)}\,dt.
\]

Uniform prediction continuity makes \(S_y(T)\) continuous in \(y\).
The exact bounds
\(\|w_y(T)\|_\infty\le S_y(T)\) and
\(\|W_y(T)\|_{\mathrm{op}}\le10+S_y(T)^2/2\) thus preserve any
conservative strict choices of \(p,b\) near the reference labels.
The kernel and residual inequalities also have strict margins. All capture
conditions persist on a sufficiently small open label neighborhood.

For each fixed label vector in that neighborhood, the fixed-time Gaussian
identification transfers its snapshot, and the exact finite-width capture
argument controls its infinite future. Shrinking the neighborhood below
the common positive amplitude preserves signs, and exact sign absorption
returns the stated neighborhoods around \(a\sigma\). This is a label
neighborhood only, as the candidate explicitly states.

## Final audit boundary

The natural-coordinate construction resolves the strong-ODE and
finite-width-identification gaps for orthogonal data in this proof. Its
dependence on orthogonality is explicit: nonorthogonal inputs introduce
ratios of first-layer derivatives that the current \(L^2\) Lipschitz
argument does not control. The conditional obtuse-pair result does not
remove that construction gap. The audited candidate is therefore a valid
orthogonal special-family theorem, including arbitrary fixed common
amplitudes and open label neighborhoods, rather than the unresolved broad
nonorthogonal theorem.

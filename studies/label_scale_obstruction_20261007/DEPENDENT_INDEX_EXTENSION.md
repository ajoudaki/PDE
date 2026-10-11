# A full unstable-index criterion on a three-sample rank-two feature stratum

2026-10-11. Scoped theoretical continuation; complete proof and author checks
below. This is a partial pointwise theorem, not independently reviewed or
promoted. No simulation, new scientific search, or Git operation was used.
The frozen `DEPENDENT_INPUT_PUSH.md` was not modified.

At a finite critical point with three samples, rank-two first features,
full-support residual, and active top-feature rank two, each active top
neuron supplies a negative Hessian direction. Each inactive neuron supplies
another if its readout/middle-weight mixed derivative is nonzero. Therefore
the complete \(n\)-direction unstable index holds when all readouts are
nonzero, or when every inactive neuron satisfies the stated mixed-derivative
condition. This does not cover every bad critical point for dependent inputs.

The scientific sources for this continuation were the assigned
`GAUSSIAN_RANK_ONE_COMPLETION.md`, `TANH_NECESSARY_GEOMETRY.md`, the complete
`DEPENDENT_GEOMETRY_RENEWAL.md`, and `docs/notation.qmd`, together with the
supervisor's proposed rank-two route. The three-coordinate diagonal-form
argument also appears as Lemma 6 of the frozen `DEPENDENT_INPUT_PUSH.md`
(SHA-256 `5c98619efefa4e1a8e3e3ac058d622b6f346d87f06bdfa31647c17e51805a7fb`).
It is proved again here so that the index argument is self-contained.
Required research, rigorous-proof, and canonical-notation guidance remains
in force.

## 1. Exact statement and normalization

Let \(X=(x_1,x_2,x_3)\in\mathbb R^{d\times3}\) contain the fixed unit
inputs, with no two parallel. They may be linearly dependent. For width
\(n\), parameters \(A\in\mathbb R^{n\times d}\),
\(W\in\mathbb R^{n\times n}\), and \(w\in\mathbb R^n\), define
\[
 U=\tanh(AX),\qquad Z=WU,\qquad H=\tanh Z,
 \qquad f=H^\top w/n,
 \qquad r=f-y,
 \qquad\mathcal L=\|r\|^2/3.
\]
These are the study's unit-input coordinates: the book's input
\(1/\sqrt d\) factor is already absorbed into \(X\). Put
\[
 D=1-H^2,\qquad
 T=\operatorname{diag}(w)D\operatorname{diag}(r),
\]
where the square is entrywise. All entries of \(D\) are strictly
positive at finite parameters. The physical mobilities are \((n,1,n)\).
The proof concerns the Euclidean loss Hessian; these positive mobilities
preserve its unstable index by positive-definite congruence.

For each top neuron \(i\), let \(z_i=Z_{i,:}^\top\) and
\(h_i=H_{i,:}^\top\) denote its sample vectors. Define the active
set and the mixed-derivative vectors by
\[
 I=\{i:w_i\ne0\},\qquad
 k_i=U(r\odot D_{i,:}^\top)\in\mathbb R^n.
\]
The notation \(H_{I,:}\) means the matrix restricted to active rows.

**Theorem.** Suppose a finite parameter state is critical for \(\mathcal L\)
and satisfies
\[
 \operatorname{rank}U=2,
 \qquad r_a\ne0\quad(a=1,2,3),
 \qquad\operatorname{rank}H_{I,:}=2.                         \tag{1}
\]
Then
\[
 \operatorname{ind}_{-}(\nabla^2\mathcal L)
 \ge |I|+\#\{i\notin I:k_i\ne0\}.                         \tag{2}
\]
In particular the Hessian has at least \(n\) negative eigenvalues if
\(I=\{1,\ldots,n\}\), or more generally if every inactive neuron has
\(k_i\ne0\). The rank assumptions already imply \(n\ge2\).

This is a deterministic pointwise theorem for arbitrary fixed labels.
It asserts neither that all critical points satisfy (1) nor that a
trajectory stays in this stratum.

## 2. A three-coordinate diagonal-form lemma

**Lemma.** Let \(b\in\mathbb R^3\) have no zero coordinate and let
\(z\in\mathbb R^3\) satisfy
\[
 b^\top z=0,\qquad\sum_a b_a\sinh(2z_a)=0.                  \tag{3}
\]
If the three \(|z_a|\) are not all equal, then
\[
                        \sum_a b_a\tanh(z_a)v_a^2            \tag{4}
\]
is indefinite on \(b^\perp\).

*Proof.* If one coordinate of \(z\) is zero, exactly one is zero:
two zero coordinates and \(b^\top z=0\) would force the last one
to vanish, contrary to the hypothesis. The two nonzero coefficients
\(b_a\tanh z_a\) have opposite signs, since \(b^\top z=0\).
A vector supported on the zero coordinate and the positive coefficient,
chosen orthogonal to \(b\), gives a positive value in (4). Using
the negative coefficient gives a negative value.

Suppose now that every \(z_a\ne0\). There cannot be exactly two
distinct absolute values. Grouping (3) by a positive magnitude \(s\)
gives two linear equations with columns \((s,\sinh(2s))^\top\).
For distinct magnitudes these columns are independent, because
\(\sinh(2s)/s\) is strictly increasing for \(s>0\). Its derivative
has numerator \(2s\cosh(2s)-\sinh(2s)\), whose derivative is
\(4s\sinh(2s)>0\) and whose value at zero is zero. Both grouped
coefficients would therefore vanish. One group is a singleton and
has coefficient \(\pm b_a\ne0\), a contradiction. Hence all three
absolute values are distinct.

Set \(D_a^*=b_a\tanh z_a\). They have the signs of \(b_az_a\),
so there are both signs. Negating \(b\) if necessary, suppose exactly
one coefficient \(D_k^*\) is negative. A positive direction in
\(b^\perp\) exists on the other two coordinates. Put
\[
 s_a=|z_a|,\qquad p_a=\frac{b_az_a}{-b_kz_k}>0\quad(a\ne k).
\]
Equations (3) give
\[
 \sum_{a\ne k}p_a=1,\qquad
 \sum_{a\ne k}p_a\frac{\sinh(2s_a)}{2s_a}
                  =\frac{\sinh(2s_k)}{2s_k}.                \tag{5}
\]
The function \(\sinh(2s)/(2s)\) is increasing and convex in \(s^2\),
as its power series has positive coefficients. Jensen therefore gives
\(\sum_{a\ne k}p_as_a^2\le s_k^2\).
The function \(\chi(s)=\coth(s)/s\) is decreasing and strictly
convex in \(s^2\). The required signs follow from
\[
 \chi'(s)=-\operatorname{csch}^2s/s-\coth s/s^2<0,
\]
and
\[
 s\chi''(s)-\chi'(s)
 =2\operatorname{csch}^2s\coth s
  +3\operatorname{csch}^2s/s+3\coth s/s^2>0;
\]
the latter expression divided by \(4s^3\) is the second derivative
with respect to \(s^2\). The endpoint magnitudes are distinct, so
strict Jensen followed by monotonicity yields
\[
 \sum_{a\ne k}p_a\chi(s_a)>
 \chi\!\left(\sqrt{\sum_{a\ne k}p_as_a^2}\right)
 \ge\chi(s_k).
\]
Consequently
\[
 \sum_a\frac{b_a^2}{D_a^*}
 =\sum_ab_a\coth z_a
 =(-b_kz_k)\left[\sum_{a\ne k}p_a\chi(s_a)-\chi(s_k)\right]>0.
                                                               \tag{6}
\]
Let \(R=\sum_{a\ne k}b_a^2/D_a^*>0\), and choose
\(v_a=b_a/D_a^*\) for \(a\ne k\), \(v_k=-R/b_k\).
Then \(b^\top v=0\) and
\[
 \sum_aD_a^*v_a^2=R(1+D_k^*R/b_k^2)<0,
\]
where the sign is equivalent to (6), since \(D_k^*<0\).
This and the positive direction prove the lemma. \(\square\)

## 3. Every active top row supplies one negative direction

At the critical point, readout and middle-weight stationarity give
\[
                              Hr=0,\qquad TU^\top=0.          \tag{7}
\]
Because \(\operatorname{rank}U=2\), the nullspace of \(U\) has
dimension one. Choose a nonzero vector \(b\) spanning it. The active
set is nonempty by (1); an active row of \(T\) has full support
because \(r\) does. Equation (7) therefore shows that every \(b_a\)
is nonzero and \(\operatorname{rank}T=1\). For each \(i\in I\),
there is a nonzero scalar \(\gamma_i\) with
\[
                          r\odot D_{i,:}^\top=\gamma_i b.     \tag{8}
\]
In particular all active gate vectors are proportional.

The top preactivation \(z_i\) lies in
\(\operatorname{row}U=b^\perp\). Using (7)--(8) and
\(\tanh z/\operatorname{sech}^2z=\sinh(2z)/2\),
\[
 b^\top z_i=0,\qquad
 0=r^\top h_i=\frac{\gamma_i}{2}\sum_ab_a\sinh(2z_{ia}).
                                                               \tag{9}
\]

No active row can have constant absolute preactivation. If one did,
its gate vector would be constant across samples. Proportionality in
(8) would make every active gate vector sample-constant, and hence
every nonzero active preactivation would have the form
\(\rho_i\sigma_i\), where \(\rho_i>0\),
\(\sigma_i\in\{-1,1\}^3\), and \(b^\top\sigma_i=0\).
There is at most one such sign vector modulo overall sign. Indeed,
for two inequivalent ones, change the overall sign of one so that
they differ in exactly one coordinate; subtracting their orthogonality
equations would force the corresponding \(b_a=0\). Thus every
active feature row would lie on one line, contradicting
\(\operatorname{rank}H_{I,:}=2\). This argument also excludes an
active row with \(z_i=0\), whose gate vector is constant.

The lemma now applies to each pair \((b,z_i)\) in (9). For an
attainable top-preactivation variation \(v\in\operatorname{row}U\),
the residual-contracted curvature from that neuron is
\[
 w_i\sum_ar_a\tanh''(z_{ia})v_a^2
 =-2w_i\gamma_i\sum_ab_a\tanh(z_{ia})v_a^2.                 \tag{10}
\]
Its scalar prefactor is nonzero, so the form is indefinite. Choose
one \(v_i\) with a strictly negative value in (10). There is a
middle-row direction \(c_i\in\mathbb R^n\) with
\(U^\top c_i=v_i\), because \(U^\top\) surjects onto
\(\operatorname{row}U\). This produces one negative residual
direction for each active row, independently across rows.

## 4. Exact neuronwise Hessian and readout cancellation

Keep \(A\) fixed. Let \(C\) vary \(W\), let \(v\) vary the
readout, and write row \(i\) of \(C\) as \(c_i^\top\). Then
\[
 \delta Z=CU,\qquad
 \delta f=\bigl[H^\top v+(D\odot CU)^\top w\bigr]/n.
\]
Direct second differentiation of the squared mean loss gives
\[
 \begin{aligned}
 D^2\mathcal L[(0,C,v),(0,C,v)]
 &=\frac23\|\delta f\|^2\\
 &\quad+\frac{2}{3n}\sum_i
 \left[
   w_i\sum_ar_a\tanh''(z_{ia})(c_i^\top u_a)^2
   +2v_i c_i^\top k_i
 \right],                                                   \tag{11}
 \end{aligned}
\]
where \(u_a=U_{:,a}\). The second term in brackets is the mixed
readout/middle-weight derivative. There are no cross-neuron residual
terms: the prediction is the sum of the top-neuron contributions.

For \(i\in I\), middle-weight stationarity gives \(k_i=0\), so
the active directions from Section 3 contribute independent strictly
negative diagonal terms to the bracketed residual form. Initially
take their readout variations to be zero.

For each inactive neuron with \(k_i\ne0\), choose a one-dimensional
direction
\[
                         c_i=t_i k_i,\qquad v_i=-t_i.
\]
Its bracket in (11) is exactly
\(-2t_i^2\|k_i\|^2\), since \(w_i=0\). This provides another
strictly negative residual direction. Set all other inactive variations
to zero. Combining these choices yields a linear subspace of dimension
equal to the right side of (2), on which the residual part of (11)
is negative definite.

It remains to remove the nonnegative squared-Jacobian term exactly.
For all of these preliminary directions, \(r^\top\delta f=0\).
For a readout variation this follows from \(Hr=0\); for an active
middle-row variation it follows from \(k_i=0\); an inactive middle-row
variation has zero first prediction differential because \(w_i=0\).
Thus \(\delta f\in r^\perp\).

By (1) and \(Hr=0\), the active feature rows span the entire
two-dimensional plane \(r^\perp\). We can therefore choose, linearly
in the preliminary direction, a compensating readout variation
\(\widehat v\) supported on \(I\) such that
\[
                           H_{I,:}^\top\widehat v_I=-n\delta f.
                                                               \tag{12}
\]
For example, fix a right inverse of this surjective map onto
\(r^\perp\). Replace \(v\) by \(v+\widehat v\). Equation (12)
makes the final first prediction differential zero, while the
residual form in (11) is unchanged: its only readout-dependent
residual terms are \(2v_i c_i^\top k_i\), and \(k_i=0\) for every
coordinate on which \(\widehat v\) is supported.

The compensated subspace has the same dimension. Every independent
coordinate chosen above has a nonzero middle-weight direction on its
own neuron, so adding readout coordinates cannot destroy injectivity.
The entire Hessian is now negative definite on this subspace. This
proves (2). \(\square\)

## 5. Scope and checks

The residual-full-support assumption is substantive. It makes the
one-dimensional annihilator vector \(b\) have no zero coordinates;
the cube-sign argument and the diagonal-form lemma use that fact.
No assertion is made here for a residual with a zero coordinate.

The active-feature-rank condition is also substantive. Rank one leaves
one sample direction that active readout variations cannot cancel,
and the argument then does not supply (2). An inactive neuron with
\(k_i=0\) contributes no negative direction by the mixed block used
here; such neurons are explicitly omitted from the bound.

The proof uses only middle weights and readout at the critical point.
It does not replace first-layer parameter variations by inaccessible
free feature variations. Nor does it assume quantitative feature-rank
persistence, bounded trajectories, or a future kernel gap.

The author checked the factors \(2/3\), \(1/n\), and \(2\) in (11),
the strictness and zero-coordinate cases of the diagonal-form lemma,
the full-support use in excluding multiple sign vectors, and the
absence of residual terms introduced by (12). These are derivational
checks, not independent certification.

If the right side of (2) equals \(n\), the point has the unstable
index required by the existing center-stable argument for the exact
zero-readout initialization slice. This note does not repeat or expand
that dynamical theorem. It establishes no Gaussian fitting result,
no avoidance conclusion for the omitted strata, and no exclusion of
escape to infinity.

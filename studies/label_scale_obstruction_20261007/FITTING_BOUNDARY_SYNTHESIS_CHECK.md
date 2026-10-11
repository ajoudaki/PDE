# Internal synthesis check: fitting and non-fitting coexist

2026-10-10. Bounded audit in the reused negative-label research context.
This is not an isolated promotion review. The reviewer authored
NEGATIVE_LABEL_BOUNDARY.md and had already reconstructed the all-amplitude
capture mechanism with the supervisor. No independence from that theorem
is claimed.

Assigned scope: compatibility of the synthesis's quantifiers, identical
inputs and labels for both basins, amplitude normalization, retained loss,
genericity inside positive-correlation regions, Gaussian probability
scope, and differential-loss factors. No experiments, external retrieval,
or edits to the synthesis were performed.

## Inputs and verdict

The synthesis initially read completely had SHA-256
3ee95591eaaa5fdf08e72e8491b0d16f752a66a35d0139a8e4cbef12d4eea2fe.
One minor qualification was requested and corrected by the author.
The corrected Section 4 was reread and the final synthesis hash verified:

969cb4484c7cc5b2d4d795b56a5005f91b1afeebf93ac6bfd0d909c91aef7eea.

Other complete inputs read or already read in the current scope were:

- POSITIVE_ARBITRARY_LABELS.md, hash
  605af3050555b2a005e1683b3da5666cf3870e7a5c46ee7bad1c6eb59460199a.
- POSITIVE_ARBITRARY_LABELS_CHECK.md, hash
  3f0663e26c2759c165bceccbd17664c5ed138d79e78d5cc912655626143156af.
- NEGATIVE_LABEL_BOUNDARY.md, hash
  fa1f21f8407401529248a6e1390f2bd4b07dc41b73f4a932f3ec2b25e297eedd.
- TANH_REPLICATION_CLASS.md, TANH_NECESSARY_GEOMETRY.md, and the
  complete all-amplitude capture argument and TANH_LARGE_RESIDUAL_CAPTURE.md.

**Verdict: PASS for the stated coexistence synthesis after the minor
zero-initial-loss qualification.** No central theorem correction is
needed. This audit does not establish any width-uniform probability bound.
The synthesis's references to earlier infinite-parameter escape examples
and the separate geometry-route report were outside the assigned
scientific inputs and were not independently rechecked here.

## 1. The same fixed data and labels support both basins

Fix \(d\ge2\), \(m\ge d^2+3d+4\), an input configuration \(X\) in
the negative theorem's open dense class, and \(0<\eta<1\).
The negative theorem chooses one mixed vector \(y^\circ(X,\eta)\)
with \(\|y^\circ\|_\infty=1\). For every \(a>0\) and \(n\ge m\),
it supplies a bad initialization basin for labels \(y=a y^\circ\).

For those exact \(X,a,n\), the positive theorem applies with Euclidean
label radius \(B=a\|y^\circ\|_2\), or with \(B=a\sqrt m\).
It therefore gives an open fitting basin for the identical labels,
width, zero-readout slice, architecture, and mobilities. Its initialization
set works uniformly over that entire label ball. The bad set concerns
the particular direction and amplitude. Neither theorem asserts a single
initialization event uniform over unbounded amplitudes.

For the positive set, the constructed center has full-rank \(U_*\);
continuity preserves this in a smaller open neighborhood, and its
initial top-feature spectral gap ensures full-rank \(H(0)\).
For the negative set, intersect the open basin with the dense open set
where both feature matrices have column rank \(m\). Thus the synthesis
correctly imposes both initial rank conditions on both basins.

## 2. All-amplitude normalization and retained loss

The construction fixes \(h_*\ne0\), \(r_0\ne0\), and
\(h_*^\top r_0=0\). The extra moment \(\sum_a r_{0,a}=0\) makes
\(r_0\) mixed-sign. A sufficiently large finite \(M\) both satisfies
the amplitude-independent capture threshold and makes
\(v=h_*-Mr_0\) mixed-sign.

Let \(Q=\|v\|_\infty>0\). The normalized labels \(a y^\circ\),
where \(y^\circ=v/Q\), are exactly the capture lemma's labels \(sv\)
with \(s=a/Q>0\). Its same fixed \(M\) works for every \(a\).
Neither \(Q\) nor the label direction depends on width or amplitude.

Every start in the bad basin has zero readout, and every endpoint lies
on the same constant-loss critical manifold. Consequently
\[
\mathcal L(0)=\frac{s^2}{m}
  \bigl(\|h_*\|^2+M^2\|r_0\|^2\bigr),\qquad
\mathcal L(\infty)=\frac{s^2M^2}{m}\|r_0\|^2,
\]
and
\[
\frac{\mathcal L(\infty)}{\mathcal L(0)}
=\frac{M^2\|r_0\|^2}{\|h_*\|^2+M^2\|r_0\|^2}.
\]
This applies to every basin trajectory, not only its symmetric center.
It is strictly between zero and one, and increasing \(M\) makes it
exceed \(1-\eta\). The direction is allowed to depend on \(\eta\),
as stated. The choice \(a=1\) gives maximum label magnitude exactly one.

At each endpoint, all first-layer rows equal \(p_*^\top\), and all
middle-layer row sums equal \(q_*>0\). Thus both feature matrices have
identical nonzero rows and rank one. The theorem proves finite parameter
convergence; an escaping trajectory is not being substituted.

## 3. Genericity inside positive-correlation regions

The moment functions have a nonzero analytic evaluation determinant on
the connected manifold \((S^{d-1})^m\). Its nonzero set is open dense.
Adjoining the constant function preserves independence because the other
functions are odd. The sufficient threshold is therefore \(d^2+3d+4\),
which equals fourteen when \(d=2\); no necessity statement is made.

An open dense set intersects every nonempty open region in a relatively
open dense set. The region with distinct inputs and all pairwise
correlations positive is nonempty: place all finitely many inputs in a
spherical cap of angular radius strictly below \(\pi/4\), choosing them
distinct. Every pair then has angle below \(\pi/2\). These conditions
are open. Hence the claimed positive-correlation classes follow from
the generic theorem and do not rely on paired-data symmetry.

## 4. Probability scope and positive-theorem constants

At each fixed width the independent Gaussian hidden-weight law has a
strictly positive density everywhere, with variances \(1\) and \(1/n\).
Both nonempty open basins have positive probability under this exact
law and exact zero readout. The support argument gives no lower bound
uniform in width. The synthesis states this limitation and does not
infer typical Gaussian failure.

The positive theorem's source uses \(Y\) for the Euclidean label radius
and \(B\) for \(\|W_0\|_{\rm op}\). The synthesis correctly renames the
radius \(B\), and writes the weight norm explicitly. Its three sufficient
inequalities and rate \(c=\lambda/m\) match the source.
The construction \(W_*=2RSU_*^+\) has norm linear in \(R\), while
\(\operatorname{sech}^2(R/2)\le4e^{-R}\). Thus the exponential factor
dominates the resulting quadratic polynomial, establishing a nonempty
event for every fixed finite label radius.

## 5. Loss factors and the resolved edge case

Let \(J_f\) be the prediction Jacobian and
\(D=\operatorname{diag}(nI_A,I_W,nI_w)\) the mobility matrix.
Direct differentiation gives
\[
\dot r=-\frac2m J_fDJ_f^\top r=-\frac2m\mathcal K r,\qquad
\dot{\mathcal L}=-\frac4{m^2}r^\top\mathcal K r.
\]
For positive loss define \(c(t)=r^\top\mathcal K r/\|r\|^2\).
Since \(\|r\|^2=m\mathcal L\),
\[
\frac{d}{dt}\log\mathcal L=-\frac4m c(t).
\]
This verifies the synthesis's integral formula and factor \(4/m\).
The positive gap gives \(c(t)\ge\lambda/4\), and hence the stated
rate \(\lambda/m\). For \(C>0,\alpha>0\), taking logarithms also yields
\[
\mathcal L(t)\le C\mathcal L(0)e^{-\alpha t}
\quad\Longleftrightarrow\quad
\int_0^t c(s)\,ds\ge\frac{m\alpha}{4}t-\frac m4\log C.
\]

The initial draft needed a qualification when \(\mathcal L(0)=0\):
the trajectory is then stationary and the quotient defining \(c\)
is undefined. The corrected synthesis explicitly treats this case
separately. For \(\mathcal L(0)>0\), residual zero cannot first be
reached at finite time, since the smooth vector field vanishes there
and local uniqueness backwards would force the preceding trajectory
to be constant. Thus \(c(t)\) is defined at every finite time and its
integral diverges exactly when limiting loss is zero.

Finally, at zero readout, hidden derivatives of the prediction vanish.
Therefore \(\mathcal K(0)=H(0)^\top H(0)/n\), and nonzero labels with
full-rank initial top features give
\[
\dot{\mathcal L}(0)=-\frac4{m^2n}\|H(0)y\|^2<0.
\]
This proves the assertion of strictly initial learning on the bad basin.

# Internal check of capture at every positive label scale

2026-10-10. Reviewer: positive_geometry_route, in the existing study research
context. This is an internal cross-check, not an isolated promotion review.
The reviewer had previously examined related positive geometry routes and
the complete replication note. The new candidate, its seed construction,
and its replication dependency were read completely. No prior verdict on
this candidate, experiment, or external scientific source was used.

Frozen scientific inputs:

| File | SHA-256 |
|---|---|
| TANH_LARGE_RESIDUAL_CAPTURE.md | c2d11d60db89a68766e793a3f9384285b3a8099dc1db0d437b2656b91c2efb5f |
| TANH_BAD_BASIN.md | f975c3bd44d9ad97ca22102908e69a181ac1bd4de491781497e9ce65d3d55a53 |
| TANH_REPLICATION_CLASS.md | 3e0bcb142b985d5e79c8a56f6a66ee91e06fe22b3a41bb1a262c1f8eaf32e14b |

The candidate was initially read at hash
15372e5b9fb23451477b6d9de4b29a75ef6ac1f082e0aadd385d116fe69afef2.
Its author then corrected only the two bare “quad” tokens in equation (27).
The final hash above was coordinated with the author and verified before
this report. No candidate or dependency was edited by this reviewer.

**Verdict: PASS for the stated capture lemma and its application to open
bad basins at every positive scale of one constructed label direction.**
All displayed sufficient constants close. The threshold for the residual
multiplier is independent of the label scale. The actual full-network
mobility, exact zero-readout slice, and fixed-width Gaussian probability
claims are preserved. No mathematical correction is required.

## The metric and the quantifiers

The lemma uses a smooth feature map \(h:\mathbb R^k\to\mathbb R^m\), a
point \(\theta_*\), and a residual direction \(r_0\) with
\[
h_*:=h(\theta_*)\ne0,\qquad
r_0^\top h_*=0,\qquad Dh(\theta_*)^\top r_0=0,\qquad
Q=\nabla^2(r_0^\top h)(\theta_*)\succ0.
\]
For fixed \(M,s>0\), labels are \(y=s(h_*-Mr_0)\) and the physical
readout is \(c=sb\). The physical reduced loss is
\[
L(\theta,c)=\frac1m\|c\,h(\theta)-s(h_*-Mr_0)\|^2
=s^2\ell_M(\theta,b).
\]
Since \(\partial_c L=s\,\partial_b\ell_M\), Euclidean gradient flow in
\((\theta,c)\) gives
\[
\dot\theta=-s^2\nabla_\theta\ell_M,\qquad
\dot b=-\partial_b\ell_M.
\]
This confirms equation (4). The scale changes the relative speed of the
hidden variables in the \(b\) coordinates; it does not change the original
optimizer.

The proof fixes \(h,r_0,\rho,\mu,\Lambda,H,D,E,K,C\), and then one
\(M>M_0\), before choosing any \(s>0\). Every constant defining \(M_0\)
is independent of \(s\). The final statement is therefore
\[
\exists M_0<\infty\quad
\forall M>M_0\quad\forall s>0:
(\theta(0),b(0))=(\theta_*,0)
\ \Longrightarrow\ 
(\theta(t),b(t))\to(\theta_*,1).
\]
The convergence rate may depend on \(s\); the lemma neither requires nor
claims a positive lower rate uniform as \(s\downarrow0\).

## Every face of the invariant tube

Let \(F=r_0^\top h\), \(\delta=\theta-\theta_*\), and use the
candidate's bounds
\[
\mu I\preceq\nabla^2F\preceq\Lambda I,\qquad
\|h\|\le H,\quad \|Dh\|_{\mathrm{op}}\le D,\quad
\|D^2h[v,z]\|\le E\|v\|\|z\|.
\]
The hypotheses give \(F(\theta_*)=0\) and
\(\nabla F(\theta_*)=0\), so all three Taylor inequalities (9) follow
by integration along the segment from \(\theta_*\).

On the hidden boundary \(\|\delta\|=K/M\), \(0\le b\le2\),
\[
\delta^\top Dh^\top(bh-h_*+Mr_0)
\ge -3DH\|\delta\|+M\mu\|\delta\|^2
=\frac K M(\mu K-3DH)>0.
\]
Here \(H\ge\|h_*\|\) because the bound holds on a ball containing
\(\theta_*\). Hence the hidden radial velocity is strictly inward when
\(b>0\) and zero when \(b=0\). Multiplication by the possibly very
large or very small positive \(s^2\) does not change this sign.

For the readout, put \(e=h-h_*\), so \(\|e\|\le DK/M\). For
\(0\le b\le1/2\), the exact identity
\[
h^\top h_*-\frac12\|h\|^2
=\frac12(\|h_*\|^2-\|e\|^2)
\]
and \(F\le\Lambda K^2/(2M^2)\) give the candidate's bound (12).
The conditions \(M>6DK/H_0\) and
\(M>4\Lambda K^2/H_0^2\), with \(H_0=\|h_*\|\), more than suffice
for
\[
h^\top h_*-b\|h\|^2-MF\ge H_0^2/4.
\]
Thus \(\dot b\ge H_0^2/(2m)>0\) on that entire portion of the tube,
including its lower face.

At \(b=2\),
\[
2\|h\|^2-h^\top h_*+MF
\ge H_0^2-3H_0DK/M>H_0^2/2,
\]
so the upper readout face also points strictly inward. At a corner
with \(b=0\), the positive readout velocity prevents exit through that
face while the hidden velocity is zero. Once \(b>0\), the hidden
boundary is strictly inward. The ordinary first-exit argument therefore
applies to the whole compact tube, with no missing corner case.

Smoothness on a neighborhood of that compact tube gives continuation
for all time. Integrating the readout lower bound gives a first hit of
\(b=1/2\) by \(T\le m/H_0^2\), independent of \(s\). The same bound
on that lower face keeps \(b\ge1/2\) afterwards.

## Hessian constants and convergence

Differentiating \(\ell_M=m^{-1}\|bh-h_*+Mr_0\|^2\) reproduces all
three Hessian blocks in (17). On the upper tube,
\[
A_{\theta\theta}\succeq(M\mu/2-6HE)I,\qquad
\|A_{\theta b}\|\le5DH+\Lambda K=C,\qquad
A_{bb}\ge H_0^2/4.
\]
The bound \(6HE\) uses \(b\le2\) and
\(\|bh-h_*\|\le3H\). The residual-curvature term has no hidden
dependence on \(s\).

The condition \(M>24HE/\mu\) gives
\(A_{\theta\theta}\succeq aI\) for \(a=M\mu/4\).
Set \(d=H_0^2/4\). Young's inequality gives
\[
a\|v\|^2-2C|z|\|v\|+dz^2
\ge\frac a2\|v\|^2+
\left(d-\frac{2C^2}{a}\right)z^2.
\]
The condition \(M>64C^2/(\mu H_0^2)\) is exactly sufficient for
\(a>4C^2/d\), making the last coefficient at least \(d/2\).
Restoring the factor \(2/m\) proves
\[
\nabla^2\ell_M\succeq\lambda I,\qquad
\lambda=\frac{\min(M\mu,H_0^2)}{4m}.
\]
All numerical factors in (8), (18), and (19) are consistent.

The upper tube is convex and contains the critical point
\((\theta_*,1)\). Integrating this Hessian bound along its line
segments proves both the quadratic lower bound and the
gradient-dominance inequality (20). Thus
\[
\frac d{dt}(\ell_M-\ell_*)
\le-2\lambda\min(s^2,1)(\ell_M-\ell_*).
\]
The resulting loss-excess estimate and quadratic lower bound imply
exponential convergence to the specified point. The actual limiting
loss is \(s^2M^2\|r_0\|^2/m>0\). No assumed parameter boundedness,
asymptotic compactness theorem, or unspecified stability theorem is used.

## Verification of the finite tanh seed

The entire nine-function construction in TANH_BAD_BASIN.md was checked.
After dividing a putative relation by the positive top derivative and
using \(t=\operatorname{arctanh}u\), its coefficients are analytic near
\(u=1\). Separating powers of \(\log(1-u)\) forces the three analytic
coefficients to vanish. The remaining exponential-polynomial identity
forces all nine original coefficients to vanish. This justifies the
existence of an invertible evaluation matrix on \((3/4,7/8)\).

Its prescribed moment vector gives, with the actual paired residual
weights \(\rho_j/2\), precisely
\[
\begin{gathered}
\sum_a r_{0,a}h_a=0,\qquad
\sum_a r_{0,a}\psi_a u_a=0,\qquad
\sum_a r_{0,a}\psi_a\chi_aX_a=0,\\
\sum_a r_{0,a}\sigma_a u_a\chi_aX_a=0,\qquad
\sum_a r_{0,a}\sigma_a\chi_a^2X_aX_a^\top=0,\\
\sum_a r_{0,a}\psi_a\tau_aX_aX_a^\top=I_2,\qquad
\sum_a r_{0,a}\sigma_a u_a^2=1.
\end{gathered}
\]
Here \(u=\tanh(p_*^\top X_a)\),
\(\chi=\tanh'(p_*^\top X_a)\),
\(\tau=\tanh''(p_*^\top X_a)\),
\(\psi=\tanh'(u)\), and \(\sigma=\tanh''(u)\), with \(q_*=1\).
The hidden Hessian blocks are consequently
\[
Q_{pp}=0+I_2,\qquad Q_{pq}=0+0,\qquad Q_{qq}=1.
\]
Thus \(Q=I_3\), \(\alpha_0=1\), and \(q_*B_0=I_2\), exactly as
claimed in (29). The feature vector is nonzero because all selected
nodes are positive. The label direction \(h_*-Mr_0\) is nonzero by
orthogonality and \(h_*\ne0\).

## Transfer to full-network open bad basins

For replicated states
\(A_{j:}=p^\top,\ W_{ij}=q/n,\ w_i=sb\), the canonical metric restricts
to \(\|\delta p\|^2+\delta q^2+s^2\delta b^2\). Direct substitution
or the verified exact replication equations therefore gives precisely
the reduced flow above, for every width.

At the limiting symmetric profile the physical residual is \(sMr_0\).
The coherent Hessian is
\[
\frac2m\left[
\|h_*\delta c+sDh(\theta_*)\delta\theta\|^2+
s^2M\,\delta\theta^\top Q\delta\theta
\right].
\]
The omitted residual-weighted mixed term is zero because
\(Dh(\theta_*)^\top r_0=0\). Positivity of \(Q\) and nonzero \(h_*\)
make this coherent form positive definite for every fixed \(s>0\).
The two splitting coefficients of the complete rank-one replication
formula are \(s^2M\alpha_0>0\) and \(s^2Mq_*B_0\succ0\).
Therefore all conditions of the strict-normal criterion in
TANH_REPLICATION_CLASS.md are met.

The Hessian kernel is exactly tangent to the displayed affine critical
manifold. All points of that manifold are critical with identical
positive loss, as follows directly from the first-derivative residual
moments. Positive normal curvature persists locally by continuity.
Taylor's formula and the fixed positive metric then give the stated
loss-excess and remaining-length bounds, so an inner open neighborhood
is attracted to the manifold. This verifies the dependency's hypotheses
and its local trapping conclusion, including directions that break
neuron symmetry.

The lemma supplies a zero-readout symmetric trajectory that enters this
full attracting neighborhood in finite time at every fixed \(n,s\).
Continuous dependence of the finite-time full flow pulls it back to a
nonempty open hidden-initialization set on the exact slice \(w=0\).
The preimage need not have a uniform radius in \(n\) or \(s\), and no such
claim is made.

The simultaneous full-feature-rank set is open and dense for these
distinct nonantipodal unit inputs, by the supplied analytic determinant
construction. Its intersection with the open basin is nonempty and
open. The same full-rank realizations permit exact interpolation by
the readout, proving that the limiting positive-loss minima are
nonglobal. Finally, the actual Gaussian hidden-weight law has strictly
positive density everywhere at fixed width. It therefore assigns this
open full-rank basin strictly positive probability.

## Exact conclusion and remaining limitation

One fixed sufficiently large \(M\) gives one fixed nonzero label
direction \(v=h_*-Mr_0\). At every \(s>0\), and every \(n\ge18\), labels
\(y=sv\) admit the stated open zero-readout bad basin. The same
direction works across widths. Choosing \(s=a/\|v\|\) realizes any
prescribed norm \(a>0\). Adding inputs with zero added residual preserves
all contracted moments; the argument extends to each fixed \(m>18\)
with its corresponding constants.

The ratio
\[
\frac{L_*}{L(0)}
=\frac{M^2\|r_0\|^2}{\|h_*\|^2+M^2\|r_0\|^2}
\]
is correct and independent of \(s\). This establishes capture at every
positive scale along the new constructed direction, not along the
earlier \(M=1\) direction and not for arbitrary label vectors.

Positive failure probability at each fixed width disproves an
almost-sure fitting assertion at that width for this family. It does
not disprove sufficiently-large-width high-probability fitting: the
basin probability may tend to zero with width. This distinction is
preserved throughout the candidate.

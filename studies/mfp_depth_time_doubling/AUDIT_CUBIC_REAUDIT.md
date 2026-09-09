# Fresh hostile re-audit of the fixed-operator cubic bridge

## Verdict

**PASS for the cubic bridge on the finite reachable smooth core.**  The
fixed construction

\[
 W_{a,0}=I_a+J_a^*,\qquad W_{a,0}^*=I_a^*+J_a
\]

really does remove the circular source-list, singular-covariance, and
moving-query defects identified in `AUDIT_CUBIC.md`.  It supplies one
bounded operator before training, reproduces the complete inverse-free
response DAG at every finite step size, and gives the common directional
\(C^3\) scalar germ needed for the gradient/Euler calculation.  I found no
remaining mathematical gap in the cubic identity after auditing both
`CUBIC_DEPTH_TIME.md` and `OPERATOR_BRIDGE_CHECK.md` independently.

The current text correctly restricts its higher regularity argument to
finite scalar slices through the reachable all-moment core.  It makes no
global \(C^3\) claim on an open \(L^2\) ball and no claim for arbitrary
\(L^2\)-only directions.  Thus the scope defect found during the first
pass of this re-audit has been removed.

## 1. Simultaneous Hilbert-space construction

The simultaneous isometry construction is consistent.  Take each
\(\Omega_a\) to carry countably many independent standard Gaussians.  Its
first chaos is a separable infinite-dimensional Hilbert space.  Partition
an orthonormal basis of that chaos into the finitely many incident-connector
blocks and seed blocks, each connector block still countably infinite.
Also \(H_a=L^2(\Omega_a)\) is separable infinite-dimensional.  Hence an
onto real-Hilbert isometry exists from each required domain \(H_{a-1}\) or
\(H_a\) onto its allocated block.  There are only finitely many choices at
fixed depth, so they can be made simultaneously; none is defined in terms
of a later state or covariance.

The apparent two-way use of adjacent spaces creates no circularity.
\(I_a\) and \(J_a\) are fixed bounded linear maps between spaces that have
already been chosen.  Their adjoints then exist automatically.  In
particular,

\[
 \|W_{a,0}\|\le \|I_a\|+\|J_a^*\|=2.
\]

The initialization matrix is therefore represented by a genuine bounded,
non-Hilbert--Schmidt operator; it is never inserted into the trainable
Hilbert--Schmidt parameter block.

## 2. Raw Gaussian laws and independence

Because the range of \(I_a\) is first chaos, every \(I_ax\) is centered
Gaussian, even when \(x\) is a nonlinear field in \(H_{a-1}\).  Isometry
gives, for every finite list,

\[
 \mathbb E[(I_ax_i)(I_ax_j)]=\langle x_i,x_j\rangle.
\]

The same calculation holds for \(J_a\).  Thus the complete source block,
not merely each marginal, has exactly the feature or cotangent Gram as its
covariance.

At an internal layer, the incoming-forward block \(I_a(H_{a-1})\) and the
outgoing-transpose block \(J_{a+1}(H_{a+1})\) occupy orthogonal first-chaos
subspaces.  Orthogonal Gaussian subspaces generate independent Gaussian
sigma-fields.  Together with the product of the layer probability spaces
and the unused endpoint blocks, this gives exactly the primitive-source and
seed independence required by the temporal DAG.  No additional
independence is claimed for states obtained after nonlinear processing.

As a direct stress test, if \(c\in H_a\), then

\[
 W_{a,0}(J_ac)=I_a(J_ac)+c.
\]

The fresh term has the required Gaussian norm and the second term is the
unit response.  Symmetrically,

\[
 W_{a,0}^*(I_ax)=J_a(I_ax)+x.
\]

These are the first nontrivial reused-matrix cycles and agree with the
row/column conditioning law.

## 3. Nonlinear response and singular histories

Let \(x=\psi(J_ac_1,\ldots,J_ac_q,\zeta)\), with \(\zeta\) independent of
the allocated \(J_a\)-block.  For arbitrary \(y\in H_a\), including
\(y\) outside the span of the history,

\[
 \langle y,J_a^*x\rangle
 =\mathbb E[(J_ay)x]
 =\sum_j\langle y,c_j\rangle\,\mathbb E[\partial_j\psi].
\]

Riesz uniqueness therefore yields

\[
 J_a^*x=\sum_j\mathbb E[\partial_j\psi]c_j.
\]

This derivation uses the underlying first-chaos coordinates directly and
does not invert their Gram.  If two history vectors coincide or are
linearly dependent, the same identity still holds.  Different redundant
coordinate descriptions give the same sum because both sums equal the
intrinsic vector \(J_a^*x\).  The symmetric calculation for \(I_a^*c\) is
identical.  Hence singular history enlargement is compatible by literal
restriction of fixed operators, not by a parameter-dependent covariance
square root.

The moving-query issue is also genuinely resolved.  For an
\(H_{a-1}\)-valued \(C^r\) curve,

\[
 \frac{d^q}{d\lambda^q}J_a^*x(\lambda)
 =J_a^*x^{(q)}(\lambda),qquad q\le r,
\]

by bounded linearity.  Thus the operator acts on the full nonlinear curve;
the proof no longer infers this action from a finite list of origin jets.

## 4. Exact equality with the temporal DAG

The chronology used in Section 4.3 is complete.  Before the forward call
at \((a,s)\), the lower feature can depend on the connector's transpose
block only through

\[
 J_a\Delta_{a,r},\qquad r<s.
\]

There is no current-time transpose source because the current backward pass
has not occurred.  The response identity therefore gives exactly

\[
 W_{a,0}X_{a-1,s}
 =I_aX_{a-1,s}+\sum_{r<s}\rho^a_{sr}\Delta_{a,r}.
\]

Before the reverse call, the current forward sweep has occurred, so
\(\Delta_{a,s}\) can depend on the forward block through precisely

\[
 I_aX_{a-1,r},\qquad r\le s.
\]

The adjoint response is therefore exactly

\[
 W_{a,0}^*\Delta_{a,s}
 =J_a\Delta_{a,s}+\sum_{r\le s}\sigma^a_{sr}X_{a-1,r}.
\]

The accumulated rank-one update contributes, with no omitted terms,

\[
 \mathcal K_{a,s}X_{a-1,s}
 =\sum_{r<s}\varepsilon_rQ^{a-1}_{rs}\Delta_{a,r},
\]

\[
 \mathcal K_{a,s}^*\Delta_{a,s}
 =\sum_{r<s}\varepsilon_rK^a_{rs}X_{a-1,r}.
\]

These four identities are exactly the forward and reverse temporal nodes.
They establish equality by the stated forward-then-reverse chronological
induction for every value of the finitely many step variables, including
zero.  Because the raw maps are isometries, their joint source covariances
are the displayed Grams automatically.  I found no missing same-time term
and no hidden rank assumption.

## 5. Generated-core regularity

The qualitative \(C^3\) claim needed for the cubic law is valid on the
reachable core.  The useful estimates are intrinsic:

\[
 \|I_ax\|_{L^p}=\bigl(\mathbb E|G|^p\bigr)^{1/p}\|x\|_2,
 \qquad
 \|J_ac\|_{L^p}=\bigl(\mathbb E|G|^p\bigr)^{1/p}\|c\|_2,
\]

and, for a finite-cylindrical core query,

\[
 \|J_a^*x\|_{L^p}
 \le \sum_j|\mathbb E\partial_j\psi|\,\|c_j\|_{L^p},
\]

with the symmetric estimate for \(I_a^*\).  A learned connector is a finite
sum of rank-one maps, so its action is a finite sum of deterministic inner
products times core fields.  Starting from Gaussian seeds, these estimates,
bounded activation derivatives, linear growth of \(\phi\), and Holder's
inequality propagate all finite moments through any fixed finite
chronology.

On an affine family spanned by the generated directions, repeated scalar
difference quotients give only finite sums of products of those core fields
and bounded derivatives of \(\phi\).  The preceding moment bounds dominate
them in a sufficiently high \(L^p\).  Hence the state and output maps are
\(C^3\) in the finite scalar coordinates and mixed derivatives commute.
This argument does not require the Nemytskii map to be globally \(C^3\) on
an open \(L^2\) ball.

The construction of
\(\mathbf h=D\mathbf g[\mathbf g]\),
\(D\mathbf g[\mathbf h]\), and
\(D^2\mathbf g[\mathbf g,\mathbf g]\) is non-circular: first differentiate
the one-coordinate line in \(\mathbf g\), freeze the resulting all-moment
field \(\mathbf h\), and then use a finite affine family containing both
directions.  The same fixed \(I_a,J_a\) act throughout.

The proof now expressly uses only these finite all-moment scalar slices;
it does not extend this moment argument to a generic \(L^2\)-only
direction.

## 6. Gradient and Euler cubic calculation

For a core variation \(v\), ordinary reverse differentiation with the
genuine adjoints gives

\[
 D\mathcal F[v]=\langle\mathbf g,v\rangle_{\mathcal P_L}.
\]

Consequently mixed scalar derivatives on the common core make
\(D\mathbf g\) self-adjoint on every generated pair.  With

\[
 \mathbf h=D\mathbf g[\mathbf g],\quad
 \mathbf k=D\mathbf g[\mathbf h],\quad
 \mathbf r=D^2\mathbf g[\mathbf g,\mathbf g],
\]

an independent differentiation of
\(\theta_{s+1}=\theta_s+h\mathbf g(\theta_s)\) gives

\[
 \theta_N'=N\mathbf g,qquad
 \theta_N''=N(N-1)\mathbf h,
\]

\[
 \theta_N'''=6\binom N3\mathbf k
 +\frac{N(N-1)(2N-1)}2\mathbf r.
\]

Applying the third-order chain rule, using
\(\langle\mathbf g,\mathbf k\rangle=\|\mathbf h\|^2\) and
\(\langle\mathbf g,\mathbf r\rangle
=D^3\mathcal F[\mathbf g,\mathbf g,\mathbf g]\), yields

\[
 F_{N,L}^{(3)}(0)
 =\frac{N(4N^2-3N+1)}2\,\mathsf S_{phi,L}
 +2N(N-1)(2N-1)\,\mathsf H_{phi,L}.
\]

Thus

\[
 \frac{8F_{t,L}^{(3)}(0)-F_{2t,L}^{(3)}(0)}6
 =-\frac{t(2t-1)}2
   (\mathsf S_{phi,L}+4\mathsf H_{phi,L}).
\]

All time coefficients were recomputed in this audit; none is imported from
the previous audit or the compact-recursion script.

## 7. Limit order and final claim status

The fixed operator represents the already width-limited inverse-free DAG.
The proof differentiates that population construction only after its exact
fixed-step equality with the DAG has been established.  It performs no
finite-width Taylor expansion and no exchange of \(n\to\infty\) with
\(h\to0\).  Identification with the actual finite-width network remains a
separate fixed-\(h\) theorem, as `CUBIC_DEPTH_TIME.md` explicitly states.

| Claim | Fresh audit status |
|---|---|
| Simultaneous fixed-space isometries | pass |
| Exact Gaussian source covariances and primitive independence | pass |
| Nonlinear response at singular histories | pass |
| History-enlargement compatibility | pass |
| Equality with the temporal DAG for all finite step variables | pass |
| \(C^3\) regularity on the generated all-moment core | pass |
| Gradient identity and Euler cubic coefficient | pass |
| Local \(C^5\) on finite reachable all-moment slices | pass |
| Actual finite-width identification | external to this note |

The repaired operator bridge cleanly passes this adversarial audit.

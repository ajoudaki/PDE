# Dependent-input Hessian bounds and a minimal-circuit obstruction

2026-10-11. Scoped theoretical continuation. Candidate proofs, author-audited;
not independently checked or promoted. No simulation, external scientific
retrieval, or Git operation was performed. Only this file was written.

The new results are an index bound using the actual accessible first-layer
variations, and a geometric theorem for minimally dependent unit inputs. For
such inputs, a nonzero tanh ridge combination has no local extremum at level
zero. Consequently every positive-loss local minimum of a sufficiently wide
two-hidden-layer network must satisfy `rank U <= m-2`. This eliminates the
first deficient-rank stratum, but does not eliminate the more collapsed
strata for general circuits. For a signed regular triangle, a further
argument eliminates every positive-loss local minimum below initial loss
at widths at least three, for arbitrary labels. Neither result proves
Gaussian fitting beyond the already available small-label regime. In
particular, no width-uniform Gaussian failure probability is proved here.

The permitted scientific sources, read completely, were
`GAUSSIAN_RANK_ONE_COMPLETION.md`, `TANH_NECESSARY_GEOMETRY.md`,
`TANH_LARGE_RESIDUAL_CAPTURE.md`, `NEGATIVE_LABEL_BOUNDARY.md`,
`ZERO_LABEL_OPEN_EXTENSION.md`, and maintained `docs/notation.qmd`.
The supervisor subsequently supplied its own rank-one/minimal-circuit lift
and three-sample reduction for comparison; the complete arguments retained
below are given explicitly. No other study, route output, or linked research
dependency was read. The required canonical-notation, rigorous-proof, and
conjecture-investigation skills and their applicable references were used.

## 1. Canonical model and the accessible mixed Hessian

Let the fixed data be unit columns of
\(X=[x_1,\ldots,x_m]\in\mathbb R^{d\times m}\). For finite parameters
\(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\), and
\(w\in\mathbb R^n\), define
\[
U=\tanh(AX),\quad Z=WU,\quad H=\tanh Z,\quad
f=H^\top w/n,\quad r=f-y,\quad \mathcal L=\|r\|_2^2/m.
\]
These are the study's unit-input coordinates, with no additional
\(1/\sqrt d\) factor. Put
\[
E=1-U^2,\qquad D=1-H^2,\qquad
T=\operatorname{diag}(w)D\operatorname{diag}(r).
\]
Products and powers in the definitions of \(E,D\) are entrywise.
The residual is always \(f-y\). The physical mobilities are \((n,1,n)\).

At a finite critical point,
\[
Hr=0,\qquad TU^\top=0,\qquad
\bigl[E\odot(W^\top T)\bigr]X^\top=0.                 \tag{1}
\]
In contrast to full-column-rank data, the last equation does not imply
\(W^\top T=0\). For a variation \(B\) of \(A\), the accessible first
feature variation is exactly
\[
                         \delta U=E\odot(BX).          \tag{2}
\]

Let \(q=\operatorname{rank}U\), \(h=n-q\), and choose
\(Q\in\mathbb R^{n\times h}\) with orthonormal columns spanning
\(\ker U^\top\). The directions
\[
                         \delta W=VQ^\top,
\qquad V\in\mathbb R^{n\times h},                     \tag{3}
\]
leave the complete predictions exactly fixed. Their pure loss Hessian is
zero. Their mixed Hessian against (2) is
\[
D^2\mathcal L[(0,VQ^\top,0),(B,0,0)]
=\frac2{mn}\left\langle
 [E\odot(QV^\top T)]X^\top,B\right\rangle_F.            \tag{4}
\]
Indeed, the first prediction variation in (3) is zero. The only mixed
second prediction term comes from \(\delta W\delta U\), yielding
\(2\langle T,\delta W\delta U\rangle_F/(mn)\), which is (4).

Define the linear map
\[
\mathscr B(V)=[E\odot(QV^\top T)]X^\top.
\]
The Hessian has at least \(\operatorname{rank}\mathscr B\) negative
eigenvalues. To verify this elementary index assertion, retain a subspace
on which the mixed block has full row rank \(p=\operatorname{rank}\mathscr B\).
The restricted Hessian has the form
\(\left(\begin{smallmatrix}0&B_0\\B_0^\top&C_0\end{smallmatrix}\right)\)
with \(B_0\) of row rank \(p\). If \(R\) is a right inverse of \(B_0\),
its quadratic form on \((v,-\varepsilon Rv)\) equals
\(-2\varepsilon\|v\|^2+\varepsilon^2(Rv)^\top C_0Rv\).
It is negative definite for sufficiently small positive \(\varepsilon\).

This formula is valid for dependent data and requires no coordinate
surjectivity from \(A\) to \(U\).

## 2. The index loss is controlled by residual-support nullity

Assume \(r\ne0\), \(w\ne0\), and write
\[
S=\{a:r_a\ne0\},\quad
k_S=|S|-\operatorname{rank}X_{:,S},\quad g=\operatorname{rank}T\ge1.
\]
Then the negative index is at least
\[
\max\{0,\;g(n-q)-nk_S\}
\ \ge\ \max\{0,\;n(g-k_S)-g(m-g)\}.                    \tag{5}
\]

Here is the dimension calculation. The map \(V\mapsto QV^\top T\)
has image dimension \(hg\): each of the \(h\) rows of \(V^\top T\)
can independently range over the \(g\)-dimensional row space of \(T\),
and left multiplication by \(Q\) is injective. Every row of this image
is supported in \(S\). On all matrices supported in these columns,
the rowwise map \(M\mapsto[E\odot M]X^\top\) has a kernel of dimension
\(nk_S\). This is because the positive diagonal multiplication by
\(E_{j,S}\) is invertible, and each row's remaining map has kernel
dimension \(k_S\). Restriction to a subspace can lose no more than
this kernel dimension. Thus \(\operatorname{rank}\mathscr B\ge hg-nk_S\).
Finally \(TU^\top=0\) gives orthogonal row spaces and hence
\(q+g\le m\), proving the second bound.

For a sharper state-dependent version, define
\[
g_j=\operatorname{rank}
\left(T\operatorname{diag}(E_{j,:})X^\top\right).
\]
The same argument gives
\[
        \operatorname{rank}\mathscr B\ge\sum_{j=1}^n g_j-qg.       \tag{6}
\]
Indeed, on the \(ng\)-dimensional space of matrices whose rows belong
to \(\operatorname{row}T\), the rowwise map has rank \(\sum_jg_j\).
The image \(\{QV^\top T\}\) has codimension \(qg\) in that space.
Restricting a linear map to a subspace of codimension \(qg\) lowers its
rank by at most \(qg\). Since \(g_j\ge g-k_S\), (6) implies (5).

In particular the full \(n\)-direction index conclusion holds whenever
\[
g\ge k_S+2,\qquad
n\ge \frac{g(m-g)}{g-k_S-1}.                             \tag{7}
\]
For all \(g\ge k_S+2\) at once, the sufficient width
\[
n\ge\max\{1,(k_S+2)(m-k_S-2)\}                          \tag{8}
\]
works whenever that rank range is nonempty. To check this, put
\(a=k_S+1\). The ratio in (7) is
\[
\frac{g(m-g)}{g-a}=m-a-g+\frac{a(m-a)}{g-a},
\]
which decreases for \(g>a\), because \(m\ge g>a\). Its maximum
over the stated range occurs at \(g=k_S+2\).

For example, input nullity one retains the full index on every stratum
with \(g\ge3\) once \(n\ge\max\{1,3(m-3)\}\). If the residual support
itself has independent columns, then \(k_S=0\), and the familiar
\(n\ge\max\{1,2m-4\}\) suffices for all \(g\ge2\), even when
other input columns are dependent.

These are pointwise statements. They do not assert that all critical
points satisfy their rank hypotheses. The supplied dependent-data minima
have \(g=1\) and fall outside (7).

## 3. Minimal unit circuits have no ridge extremum at level zero

Call the inputs a minimal unit circuit when
\[
\operatorname{rank}X=m-1,\qquad
\ker X=\operatorname{span}\{c\},\qquad c_a\ne0\quad(1\le a\le m),
                                                               \tag{9}
\]
and the columns are unit, distinct, and nonantipodal. Equivalently,
every \(m-1\) columns are independent. Necessarily \(m\ge3\).
The following strict triangle inequalities will be used:
\[
                      |c_b|<\sum_{a\ne b}|c_a|
                      \quad\text{for every }b.          \tag{10}
\]
For the weak inequality take norms in
\(c_bx_b=-\sum_{a\ne b}c_ax_a\). Equality would force all nonzero
vectors \(c_ax_a\), \(a\ne b\), to point in the same direction as
\(-c_bx_b\), by the equality condition in the Euclidean triangle
inequality. This would make some distinct input columns equal or
antipodal, so equality is excluded.

**Theorem 1.** For inputs (9) and any \(b\in\mathbb R^m\setminus\{0\}\),
define
\[
                         F_b(a)=\sum_{s=1}^m b_s\tanh(a^\top x_s).
\]
If \(F_b(a)=0\) and \(\nabla F_b(a)=0\), then either
\(X^\top a=0\), or the Hessian of \(F_b\) has both a strictly positive
and a strictly negative direction in \(\operatorname{span}\{x_s\}\).
At every zero of \(F_b\), each neighborhood contains a point with
positive value and a point with negative value. Thus level zero contains
no local minimum or maximum of \(F_b\).

*Proof.* Set \(z=X^\top a\), \(e_s=\operatorname{sech}^2z_s\).
Criticality gives \(X\operatorname{diag}(e)b=0\), so
\[
                      b_s e_s=\lambda c_s\quad(1\le s\le m)
                                                               \tag{11}
\]
for a nonzero scalar \(\lambda\). The scalar is nonzero because
\(b\ne0\) and each \(e_s>0\). The input relation and the zero value
become
\[
            \sum_s c_sz_s=0,\qquad
            \sum_s c_s\sinh(2z_s)=0.                    \tag{12}
\]
The Hessian is
\[
\nabla^2F_b(a)=-2\lambda X
       \operatorname{diag}(c_s\tanh z_s)X^\top.           \tag{13}
\]
Since \(X^\top\) maps the input span bijectively onto \(c^\perp\),
it suffices to prove that the diagonal form with entries
\(d_s=c_s\tanh z_s\) is indefinite on \(c^\perp\), whenever \(z\ne0\).

The first equation in (12) implies that there are both positive and
negative entries of \(d\). If some \(d_s=0\), choose a vector supported
on this index and one positive index, with its two coordinates chosen
to make it perpendicular to \(c\). Its quadratic value is positive.
Using a negative index instead gives a negative value. Thus this case
is settled. If there are at least two entries of each sign, the
two-coordinate positive and negative subspaces each intersect
\(c^\perp\) nontrivially, again giving indefiniteness.

It remains to treat exactly one negative entry, say index \(k\),
all others positive. The case of exactly one positive entry follows
by replacing \(c\) with \(-c\). Set
\[
s_i=|z_i|>0,\qquad
p_i=\frac{c_i z_i}{-c_kz_k}>0\quad(i\ne k),\qquad
\sum_{i\ne k}p_i=1.
\]
The second equation in (12) says
\[
\sum_{i\ne k}p_i\,\phi(s_i)=\phi(s_k),\qquad
\phi(s)=\frac{\sinh(2s)}{2s}.                            \tag{14}
\]
As a function of \(v=s^2>0\), \(\phi(\sqrt v)\) is strictly
increasing and strictly convex: its power series is
\(\sum_{j\ge0}2^{2j}v^j/(2j+1)!\), with positive coefficients.
Consequently (14) and Jensen's inequality give
\(\sum_{i\ne k}p_is_i^2\le s_k^2\).

The function \(\chi(s)=\coth(s)/s\) is strictly decreasing and
strictly convex as a function of \(s^2\). For completeness,
\[
\chi'(s)=-\frac{\operatorname{csch}^2s}{s}
          -\frac{\coth s}{s^2}<0,
\]
and
\[
s\chi''(s)-\chi'(s)
=2\operatorname{csch}^2s\coth s
 +\frac{3\operatorname{csch}^2s}{s}
 +\frac{3\coth s}{s^2}>0.
\]
The latter expression divided by \(4s^3\) is the second derivative
with respect to \(v=s^2\). Jensen, followed by monotonicity, now yields
\[
\sum_{i\ne k}p_i\chi(s_i)
\ge \chi\!\left(\sqrt{\sum_{i\ne k}p_is_i^2}\right)
\ge\chi(s_k).                                          \tag{15}
\]
Equality would require all \(s_i\), including \(s_k\), to be equal.
Then \(\sum_i c_i z_i=0\), with exactly one negative product,
would give \(|c_k|=\sum_{i\ne k}|c_i|\), contradicting (10).
Thus (15) is strict, and
\[
\sum_i\frac{c_i^2}{d_i}
=\sum_i c_i\coth z_i
=(-c_kz_k)\left[\sum_{i\ne k}p_i\chi(s_i)-\chi(s_k)\right]>0.
                                                               \tag{16}
\]

To see directly that (16) supplies a negative direction, let
\(S_+=\sum_{i\ne k}c_i^2/d_i>0\), set \(v_i=c_i/d_i\) for
\(i\ne k\), and choose \(v_k=-S_+/c_k\). Then \(c^\top v=0\),
and
\[
\sum_i d_iv_i^2
=S_+\left(1+\frac{d_kS_+}{c_k^2}\right)<0,
\]
because (16) is \(S_++c_k^2/d_k>0\) and \(d_k<0\).
The positive directions already follow from the at least two positive
entries, since \(m\ge3\). This proves the Hessian assertion.

A regular zero has both signs nearby by its nonzero derivative. An
indefinite critical zero has both signs nearby by second-order Taylor
expansion. Finally, if \(X^\top a=0\), then
\(F_b(a+v)=F_b(v)\), an odd analytic function. It is not identically
zero: choose a direction with nonzero input projections of distinct
absolute values, possible by avoiding the finitely many hyperplanes
orthogonal to \(x_i\) and \(x_i\pm x_j\). On that line a putative
identity reduces to \(\sum_i\beta_i\tanh(t\alpha_i)=0\) with
\(0<\alpha_1<\cdots<\alpha_m\). Taking \(t\to\infty\), then
subtracting the resulting constant and successively isolating the
slowest exponential in
\(\tanh(t\alpha)-1=-2e^{-2t\alpha}(1+o(1))\), forces every
\(\beta_i=0\), contrary to \(b\ne0\). Nonzero analyticity prevents
vanishing on a neighborhood, and oddness supplies both signs there.
This proves the final assertion. \(\square\)

## 4. The first deficient feature stratum cannot contain a bad minimum

**Theorem 2.** For minimal unit-circuit inputs and \(n\ge m\), every
positive-loss local minimum of the canonical network satisfies
\[
                         \operatorname{rank}U\le m-2.   \tag{17}
\]
This conclusion is for all labels and every finite parameter state;
it is not a trajectory theorem.

*Proof.* First, a positive-loss local minimum cannot have \(w=0\).
If it did, all small changes of hidden parameters would still have
zero prediction when \(w=0\). Local minimality with respect to a
small readout coordinate would require \(y^\top H_{i,:}=0\) on an
open hidden-parameter neighborhood. Analyticity would extend the
identity to all hidden parameters. Choosing one first-layer row whose
input projections have distinct nonzero absolute values, and varying
the corresponding coefficient in one row of \(W\), reduces this
identity to the linearly independent scalar tanh family in Theorem 1.
It forces \(y=0\), contradicting positive loss at zero readout.
This reproduces the needed zero-readout argument from the permitted
necessary-geometry source.

At any positive-loss local minimum, (1) and positive top gates now
give \(T\ne0\). Thus \(\operatorname{rank}U\le m-1\). Suppose it equals
\(m-1\). Then \(TU^\top=0\) implies
\[
                    T=t b^\top,
\qquad t\ne0,\quad b\ne0,\quad\operatorname{row}U=b^\perp.       \tag{18}
\]
Because \(n\ge m\), some row index \(j\) is redundant: there exists
\(v\in\ker U^\top\) with \(v_j\ne0\). Equivalently, the other rows
of \(U\) span \(b^\perp\).

We may arrange \((W^\top t)_j\ne0\) while retaining local minimality.
Choose \(i\) with \(t_i\ne0\) and replace \(W\) by
\(W+\varepsilon e_i v^\top\). This leaves \(WU\), the predictions,
the residual, and \(T\) exactly fixed; for sufficiently small
\(\varepsilon\), the new point belongs to the original minimizing
neighborhood and is itself a local minimum. The coefficient changes by
\(\varepsilon t_i v_j\), so it can be made nonzero. Fix such a point.

Write the current row \(j\) of \(A\) as \(a_j^\top\), and its
feature row as \(u_j^\top\). Vary only that row initially. For a
nearby \(a\), decompose
\[
\tanh(X^\top a)-u_j=d(a)+\alpha(a)b,
\qquad d(a)\in b^\perp,
\qquad \alpha(a)=\frac{F_b(a)}{\|b\|^2},                 \tag{19}
\]
where \(F_b(a_j)=b^\top u_j=0\). Since the remaining unchanged
feature rows span \(b^\perp\), choose coefficients \(\ell_k(a)\),
\(k\ne j\), depending linearly on \(d(a)\), such that
\(d(a)=\sum_{k\ne j}\ell_k(a)u_k\). A right inverse of this finite
surjective map gives continuous coefficients vanishing at \(a_j\).

Change the other columns of \(W\) by
\(W_{:,k}\mapsto W_{:,k}-W_{:,j}\ell_k(a)\), leaving column \(j\)
unchanged. This is a parameter perturbation tending to zero with
\(a-a_j\). Its preactivations are exactly
\[
                             Z(a)=Z+\alpha(a)W_{:,j}b^\top.
                                                               \tag{20}
\]
Let \(J(\alpha)\) be the loss obtained from the right side of (20)
with the fixed readout. Its derivative at zero is
\[
J'(0)=\frac2{mn}\sum_{i,s}r_sw_iD_{is}W_{ij}b_s
=\frac{2\|b\|^2}{mn}(W^\top t)_j\ne0.                 \tag{21}
\]
Theorem 1 says that \(F_b\), and therefore \(\alpha\), takes both
signs arbitrarily close to \(a_j\). Choosing the sign opposite to
\(J'(0)\) makes \(J(\alpha)<J(0)\) for sufficiently small nonzero
\(\alpha\). Equations (19)--(20) realize this by arbitrarily small
actual parameter variations, contradicting local minimality.
Hence (17). \(\square\)

The proof does not claim that these points all have \(n\) negative
Hessian eigenvalues. At the original point, (21) may vanish; moving
within the constant-loss set and then descending can reveal behavior
beyond the Hessian. Theorem 2 therefore cannot be inserted directly
into the existing Gaussian center-stable argument.

## 5. What remains in the three-sample circuit case

Every three distinct nonantipodal unit inputs of rank two form a
minimal circuit. Theorem 2 leaves only \(\operatorname{rank}U\le1\)
as a possible positive-loss local-minimum stratum. If \(U=0\), then
\(H=0\), so the loss is the initial loss \(\|y\|^2/m\); this cannot
be a finite limit after a strict initial decrease. The unresolved
stratum below initial loss is therefore \(\operatorname{rank}U=1\).

There is an exact additional reduction at a second-order stationary
point of that rank, provided at least two rows of \(U\) are nonzero.
All its rows are then redundant. The flat-direction argument (4)
and positive semidefiniteness force
\[
                       T\operatorname{diag}(E_{j,:})X^\top=0
                       \quad\text{for every }j.        \tag{22}
\]
Choose a nonzero row of \(T\), denoted \(b^\top\). Since
\(\ker X=\operatorname{span}\{c\}\), (22) yields
\(b\odot E_{j,:}=\lambda_j c\), with each \(\lambda_j\ne0\).
Thus all the first derivative-gate rows are proportional.

Write \(U_{j,:}=\alpha_j u^\top\) for a fixed nonzero vector \(u\).
If two values \(\alpha_j^2\) differ, proportionality of
\(1-\alpha_j^2u_s^2\) and \(1-\alpha_k^2u_s^2\) forces all \(u_s^2\)
to be equal: equating any two coordinates after cross multiplication
gives \((\alpha_j^2-\alpha_k^2)(u_s^2-u_t^2)=0\).
But constant nonzero absolute values in a feature row would make
\(X^\top a=\rho\sigma\), \(\sigma\in\{-1,1\}^3\), and therefore
\(\sum_s c_s\sigma_s=0\). For three nonzero coefficients this
contradicts the strict triangle inequalities (10). Hence all
\(\alpha_j^2\) are equal and nonzero. All first-layer feature rows
are sign copies of one profile; there are no zero rows.

This reduction does not by itself prove a negative Hessian direction.
The unrestricted middle matrix has components invisible on the current
rank-one features, and these components enter the second variation of
first-layer splitting. The indefinite single-ridge Hessian cannot be
substituted for the full network Hessian without controlling those terms.
The case of exactly one nonzero first-feature row can instead be
excluded below initial loss. Here is the complete argument. Let \(j\)
be that row and write its feature vector as \(u\ne0\). Every other
row is zero and redundant. Applying (22) to a zero row gives
\(T=t c^\top\), since its derivative gates are all one. In particular,
\(t\ne0\) and the residual has full support. The equation \(TU^\top=0\)
gives \(c^\top u=0\).

At the nonzero row \(a_j\), \(\nabla F_c(a_j)\ne0\). Otherwise
\(X(c\odot\operatorname{sech}^2(X^\top a_j))=0\) would imply that
all first derivative gates, hence all \(|(X^\top a_j)_s|\), are
equal. Their common magnitude would be positive because \(u\ne0\).
The relation \(c^\top X^\top a_j=0\) would then contradict (10),
as in the preceding three-sample argument. First-layer stationarity
therefore forces \((W^\top t)_j=0\).

Put \(q_i=W_{ij}\), so the second preactivation row is \(q_i u\).
For active readout indices, the equations
\(w_iD_{i,:}\odot r=t_i c\) imply that the positive gate vectors
\(D_{i,:}\) are proportional. There are two distinct magnitudes
among \(|u_s|\), since constant magnitude was just ruled out. For
\(0\le\alpha<\beta\), the function
\[
q\longmapsto\frac{\operatorname{sech}^2(q\beta)}
                    {\operatorname{sech}^2(q\alpha)}
\]
is strictly decreasing for \(q>0\): the derivative of its logarithm
is \(-2\beta\tanh(q\beta)+2\alpha\tanh(q\alpha)<0\).
Hence proportionality of the gate vectors forces a common magnitude
\(|q_i|=q\) for all active indices. If \(q=0\), then \(f=0\).
Otherwise write \(q_i=\sigma_iq\), \(\sigma_i\in\{-1,1\}\).
Their gates are identical, so \(t_i=\kappa w_i\) for a common
nonzero \(\kappa\). The equation \((W^\top t)_j=0\) becomes
\(\kappa q\sum_iw_i\sigma_i=0\), and therefore
\[
f=\frac{\tanh(qu)}n\sum_iw_i\sigma_i=0.
\]
Thus this case also has exactly the initial loss, and cannot occur
at a positive-loss second-order stationary point strictly below it.

Combining the cases, for three-sample minimal unit circuits and
\(n\ge3\), a positive-loss local minimum below the initial loss
would have to have all first-feature rows equal up to sign to one
nonzero profile. This is a precise remaining stratum, not an example
of actual Gaussian nonfitting dynamics.

## 6. Complete local-minimum exclusion for a signed regular triangle

There is a complete special case of the remaining stratum. Call three
unit inputs a signed regular triangle if signs can be chosen so that
their signed sum is zero. Equivalently, the absolute values of the
three entries in their unique circuit vector are equal. Distinctness
and nonantipodality make their rank two. Changing an input and its
label by the same sign preserves the loss and parameter flow, since
the bias-free network is odd. We can therefore take
\[
                        x_1+x_2-x_3=0,\qquad c=(1,1,-1)^\top.
                                                               \tag{23}
\]

**Theorem 3.** For signed regular-triangle inputs, arbitrary labels,
and \(n\ge3\), there is no finite local minimum with
\[
                     0<\mathcal L<\|y\|^2/3.           \tag{24}
\]
This is a local-minimum theorem, not an almost-sure fitting theorem
or a statement that every bad critical point has \(n\) negative
eigenvalues.

*Proof.* Suppose such a local minimum exists. Sections 4--5 reduce it
to a point whose first-feature rows are sign copies of one nonzero
profile. First-neuron sign flips, accompanied by sign flips of the
corresponding columns of \(W\), are exact parameter symmetries. Use
them to make all first-feature rows equal to one vector \(u\).
Their relevant first preactivations are then equal to one vector
\(z\), with \(u=\tanh z\). Components of first weights orthogonal
to the input span have no effect and can be ignored. Let \(a_*\)
denote the common projection of these rows onto the input span.

All first rows are redundant. At a second-order stationary point,
(22) and \(TU^\top=0\), applied to one nonzero row of \(T\), give
\(\sum_s c_s\sinh(2z_s)=0\), as in (11)--(12). Since
\(z_3=z_1+z_2\), the identity
\[
\sinh(2z_1)+\sinh(2z_2)-\sinh(2(z_1+z_2))
=-4\sinh z_1\sinh z_2\sinh(z_1+z_2)
\]
forces one of \(z_1,z_2,z_3\) to vanish. By a sample permutation
and, if needed, simultaneous input/label sign flips preserving (23),
we may therefore write
\[
                     u=(0,v,v)^\top,\qquad v\ne0.        \tag{25}
\]
Put \(e=1-v^2>0\).

Every top preactivation row has the form \(q_i u\), where
\(q_i=\sum_jW_{ij}\). Thus every row of \(H\) is proportional to
\((0,1,1)\). The prediction is nonzero by (24), so some existing
readout coordinate multiplies a nonzero row of \(H\). It is possible
to perturb the readout arbitrarily slightly, keeping \(H^\top w\)
exactly fixed, so that every readout coordinate becomes nonzero:
the affine hyperplane prescribing the one nontrivial output coefficient
is not contained in any coordinate hyperplane whose coordinate is
currently zero. Its complement of all coordinate hyperplanes is
dense. A sufficiently small such perturbation stays in the original
minimizing neighborhood and is again a local minimum. Fix this point.

For any one top row, (22) gives
\[
             r_1=\lambda,\qquad
             r_2=\frac{\lambda}{D e},\qquad
             r_3=-\frac{\lambda}{D e},                 \tag{26}
\]
where \(D=\operatorname{sech}^2(q_i v)\) and \(\lambda\ne0\).
The scalar is nonzero because \(r\ne0\), \(c\) has full support,
and the gates are positive. Applying the same identity to every
other row shows that its \(\operatorname{sech}^2(q_i v)\) equals
this same \(D\). Hence all \(|q_i|\) have one common value \(q\).
If \(q=0\), then \(H=0\) and \(f=0\), contradicting (24).
Use the exact top-neuron sign symmetry to make every \(q_i=q>0\).
All top features and gates are now identical, although their
nonzero readout coefficients can have either sign. Write
\[
h=\tanh(qv),\qquad S_w=\sum_iw_i\ne0.
\]
The last inequality follows again from the nonzero prediction.

Write \(D_s=\operatorname{sech}^2(q u_s)\) for the common top gate
at sample \(s\). Consider a middle-weight variation with row sums \(b_i\); every
\(b\in\mathbb R^n\) is realizable. Its first prediction variation is
\(D_su_s\sum_iw_ib_i/n\). In particular it vanishes when \(w^\top b=0\).
Its residual-contracted pure second variation vanishes for every
\(b\), because
\[
\alpha:=\sum_s r_s\tanh''(q u_s)u_s^2=0;                \tag{27}
\]
the first term is zero and the last two cancel by (25)--(26).
Thus every \(b\in w^\perp\) is a zero quadratic direction of the
full Hessian.

For its mixed Hessian against a first-layer variation, the direct
\(\delta W\delta U\) term vanishes by
\(\sum_s r_sD_s(1-u_s^2)x_s=0\), which is (22).
The Gauss--Newton term vanishes because \(w^\top b=0\).
The remaining mixed term is proportional to
\[
\sum_{i,j} w_i b_i W_{ij}\,v_0^\top\delta a_j,
\qquad
v_0:=\sum_s r_s\tanh''(q u_s)u_s(1-u_s^2)x_s
       =2\lambda hv\,x_1\ne0.                         \tag{28}
\]
The last equality uses \(x_2-x_3=-x_1\) and (26).
Positive semidefiniteness of the Hessian forces (28) to vanish for
all \(b\in w^\perp\) and all first-layer row variations.
For every column \(j\), therefore,
\(\operatorname{diag}(w)W_{:,j}\in\operatorname{span}\{w\}\).
Every \(w_i\ne0\), so all rows of \(W\) are equal:
\[
                    W=\mathbf1\rho^\top,\qquad
                    \sum_j\rho_j=q\ne0.               \tag{29}
\]

Every \(\rho_j\) must be nonzero at a positive-loss local minimum.
If a column of \(W\) were zero, its first-layer row could vary on
an open neighborhood without changing predictions, residual, or loss.
Every sufficiently nearby such point would remain a local minimum.
Stationarity of the \((i,j)\) middle-weight entry, for an active
readout index \(i\), would require
\(\sum_s r_sD_s\tanh(a^\top x_s)=0\) throughout that neighborhood.
Analytic continuation and the ridge independence proved in Theorem 1
would force \(r_sD_s=0\) for every sample, contrary to \(r\ne0\).
This is the needed zero-column exclusion, proved here without assuming
anything about a remote point on a flat parameter set.

Choose \(\beta\in\rho^\perp\) with
\(C_\beta:=\sum_j\rho_j\beta_j^2\ne0\). Such a vector exists:
since \(n\ge3\) and all \(\rho_j\ne0\), there are two indices
\(j,k\) with \(\rho_j+\rho_k\ne0\). Otherwise the equations for
three pairs would force their nonzero entries to vanish. Take
\(\beta_j=\rho_k\), \(\beta_k=-\rho_j\), and all other entries
zero. Then \(C_\beta=\rho_j\rho_k(\rho_j+\rho_k)\ne0\).

Let \(b_s=r_sD_s\) and \(F_b(a)=\sum_s b_s\tanh(a^\top x_s)\).
At the common first-layer row this function has value zero, gradient
zero, and an indefinite Hessian by Theorem 1, since (25) is nonzero.
For an arbitrary input-space vector \(a\), vary first-layer row \(j\)
by \(\beta_j a\), keeping \(W,w\) fixed. Equations (29) and
\(\rho^\top\beta=0\) make all first top-preactivation variations
zero. Consequently the Gauss--Newton and top-activation second
derivative terms vanish. The remaining exact loss Hessian is
\[
D^2\mathcal L[\delta A,\delta A]
=\frac{2S_w C_\beta}{3n}\,a^\top\nabla^2F_b(a_*)a.      \tag{30}
\]
Both scalar factors \(S_w,C_\beta\) are nonzero. Since the ridge
Hessian is indefinite, choose \(a\) making (30) strictly negative.
This contradicts positive semidefiniteness at the nearby local
minimum, and proves the theorem. \(\square\)

The use of nearby constant-loss readout states in this argument is
essential. It does not establish a uniform lower bound on the
negative index at the original critical point, so it leaves the
Gaussian avoidance implication open even for this special geometry.

## 7. Gaussian initialization and exact limits of the new conclusions

The non-tangency \(Hy\ne0\) on the exact slice \(w=0\) holds almost
surely for all pairwise distinct nonantipodal nonzero inputs and
\(y\ne0\); full input rank is unnecessary. Indeed each component of
\(Hy\) is analytic in \((A,W)\), and at least one is not the zero
analytic function, by the two-layer ridge-separation construction
used in Section 4. The zero set of a nonzero real-analytic function
on Euclidean space has Lebesgue measure zero. One elementary proof is
induction on dimension and Fubini: choose a coordinate derivative at
a fixed coordinate value which is a nonzero analytic function of the
remaining coordinates; away from its measure-zero zero set, the
one-dimensional analytic section has only isolated zeros. Countable
boxes cover the space. The Gaussian hidden law has a density, proving
the assertion. The initial readout velocity is \(2Hy/m\), so the
loss strictly decreases initially almost surely.

Consequently the existing local center-stable argument can exclude
finite limiting critical points satisfying the new index condition
(7), on the same exact Gaussian initialization slice. The local
center-stable theorem and the countable-cover implementation remain
the supplied dependency from `GAUSSIAN_RANK_ONE_COMPLETION.md`, Section 5;
the new ingredient is the valid accessible index calculation (4)--(7).
No assertion is made about limits in the complementary low-rank strata.

The stronger desired Gaussian conclusion remains open. In particular:

- The supplied open dense dependent-input bad-basin construction already
  disproves an all-dependent-data finite-critical-point index theorem.
  Its positive Gaussian probability at each width does not establish
  a nonvanishing large-width failure probability.
- Theorem 2 excludes one local-minimum stratum for every minimal unit
  circuit and every label vector. It neither excludes saddles of smaller
  index nor supplies almost-sure avoidance of nonhyperbolic limits.
- The rank-one three-sample stratum is eliminated for local minima on
  signed regular triangles by Theorem 3. Its general-circuit version,
  the Gaussian avoidance of other finite bad critical limits, and
  all-time fitting remain open.
- Initial-Gram capture proves small-label fitting for every admissible
  fixed dataset, including dependent ones; the supervisor identified
  this as an existing baseline, so it is not counted as a new positive
  result here.
- Boundedness, escape to infinity, and a width-uniform probability of
  entering a bad basin were not established by this route.

The route is therefore **partial, with new geometric restrictions**.
Its highest-leverage unresolved step is the full-network Hessian or
higher-order analysis on the general three-sample rank-one stratum,
including the unrestricted middle-weight components; for regular
triangles the missing step is a sufficiently strong avoidance theorem.
Reopening a generic
all-dependent index claim without such a restriction would contradict
the supplied bad minima.

## Source versions and author checks

The source SHA-256 values at reading were:

| File | SHA-256 |
|---|---|
| `GAUSSIAN_RANK_ONE_COMPLETION.md` | `fb58eca18b958e720ca7cf6ab58e6eef849daa247f1e7b287a3896b7204ce60c` |
| `TANH_NECESSARY_GEOMETRY.md` | `770527741d5a9acf76cb9c44e917be8eb9894edff6f02fc03c922f3ecb795b0f` |
| `TANH_LARGE_RESIDUAL_CAPTURE.md` | `c2d11d60db89a68766e793a3f9384285b3a8099dc1db0d437b2656b91c2efb5f` |
| `NEGATIVE_LABEL_BOUNDARY.md` | `fa1f21f8407401529248a6e1390f2bd4b07dc41b73f4a932f3ec2b25e297eedd` |
| `ZERO_LABEL_OPEN_EXTENSION.md` | `5cbd8ffa45eca9f2bc7be0f277dde2700aa52366c5bc8c8dafa25a5371da6556` |

The author checked the mixed-Hessian normalization, the loss of dimension
in (5)--(6), the sign reversal in (16), all zero-coordinate cases in
Theorem 1, and the exact compensating parameter construction (19)--(20).
These checks are derivational, not numerical or independent. No claim of
completed independent checking or promotion is made.

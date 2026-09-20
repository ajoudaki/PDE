# Independent review of cubic and higher-order descent

Date: 2026-09-19. Internal mathematical review, not a promotion review.

## Assignment, frozen inputs, and coverage

I read the neutral assignment, the required `solve-math-rigorously` skill,
and all of these frozen scientific inputs:

| Input | SHA-256 |
| --- | --- |
| `docs/observable_p1.md` | `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `studies/p1_stochastic_escape_20260918/cubic_and_higher_descent.md` | `d469d54a466fb60464f6c3c9e79d831718f333b09e98de20a9d7ff7fc78b9fe1` |

The hashes were checked before review. All line references below refer to this
candidate version. I did not read study history, other research artifacts,
prior verdicts, or another reviewer's findings. No simulations or external
scientific sources were used. Section 5's descriptions of earlier examples
were treated as context, as instructed; their original proofs were not inputs.
The main results in sections 1–4 have no missing dependency on those examples.

I checked the exact reduced model, its admissible variations, the Hilbert
directional regularity argument, all three cases following (5), the four-input
data, both explicit higher-order expansions, both general finite-order bounds,
and exact representability. I also checked the supervisor's requested
extension of the vanishing quadratic/cubic terms to the unfolded dictionary.

## Result and required correction

**The substantive mathematical claims are verified. One local normalization
correction is required in the Hessian wording.** I found no failure of the
counterexample, descent formulas, finite-order bounds, or exact-fit theorem.

At candidate lines 125–126, “The collapsed state's physical Hilbert Hessian
is the quadratic form in (5)” identifies the quadratic Taylor coefficient
with the Hessian without its factor of two. For a direction
\(\delta=(h,k,N)\), the precise identity is

\[
\frac12 D^2L(S_*)[\delta,\delta]
 =-2v_k^TM_*A_hm_y,
\qquad
D^2L(S_*)[\delta,\delta]
 =-4v_k^TM_*A_hm_y.
\]

Replace those sentences with:

> The quadratic term in (5) is one half of the physical Hilbert Hessian
> evaluated on the direction twice. Its polarization is a bounded symmetric
> bilinear form.

Explicitly, for \(\delta'=(h',k',N')\), that bilinear form is

\[
D^2L(S_*)[\delta,\delta']
 =-2\left(v_k^TM_*A_{h'}m_y+v_{k'}^TM_*A_hm_y\right).
\]

This correction does not change any zero-Hessian statement, sign, or descent
order in the candidate. It also avoids calling a quadratic form itself a
bilinear form.

## Detailed verification

### 1. Exact model, carriers, and admissibility

Equation (1) uses the unhalved weighted squared loss, inputs
\(u_i=x_i/\sqrt d\), fixed correlated lower marks, independent upper marks,
and the actual evolving matrix. These agree with the supplied model source.
The full trainable matrix in the odd sector is \(d\times2d\); none of the
arguments replaces it by diagonal or fixed-rank dynamics. The constants can
be omitted in this sector because the lower activations and readout are odd,
and the constant row and column stay inactive. All constructed witnesses
remain in that sector.

The normalized marks are bounded. Their nonconstant Grams are positive
definite: a nonzero reverse-feature coefficient has strictly positive
conditional variance given the lower Gaussian coordinates, and any remaining
nonzero forward-feature coefficient has positive variance. Coordinate
independence and invertible normalization preserve this conclusion. The upper
coordinates have a strictly positive density on their open product interval.
For the lower coordinates, the map from each Gaussian pair to
\((\tanh G_i,\tanh(\sqrt\tau Z_i+\alpha\tanh G_i))\) is an invertible smooth
map onto \((-1,1)^2\) with nonzero Jacobian. The subsequent normalization
is invertible. Thus the lower law is absolutely continuous, and every
nonzero linear form in the lower marks has no atom at zero.

The canonical \(D\) is nonzero, since its first diagonal band is
\(\alpha v/(ac)>0\). For any nonzero matrix \(M_*\), choose \(s\) with
\(M_*^Ts\ne0\). Then

\[
s^TM_*E_1[b_1\operatorname{sign}(s^TM_*b_1)]
 =E_1|s^TM_*b_1|>0.
\]

Consequently \(M_*A\ne0\), the sign field satisfies \(e^2=1\) almost surely,
and \(Z=b_2^TM_*A\) has interval support containing zero. These facts justify
all subsequent nondegeneracy and polynomial-independence arguments. The sign
field need only be measurable and square integrable; no continuity in the
Gaussian marks is assumed by this population state space.

### 2. Expansion for arbitrary fixed L2 directions

For \(u_i=x_i/\sqrt d\), let \(X_i=h\cdot u_i\). The integral Taylor formula
and boundedness of \(\phi''\) give

\[
\frac{\phi(\epsilon X_i)-\epsilon X_i}{\epsilon^2}
 =X_i^2\int_0^1(1-t)\phi''(t\epsilon X_i)\,dt.
\]

The integrand tends to zero because \(\phi''(0)=0\), and is bounded by a
constant times \(|h|^2\). This proves the stated lower-moment remainder
\(o(\epsilon^2)\) for every fixed \(h\in L^2\), without an L3 assumption.
Multiplication by \(M_*+\epsilon N\) and bounded \(b_2\) gives a uniform
upper argument of order \(\epsilon\). The upper tanh remainder is then
\(O(|\epsilon|^3)\). Because \(k\in L^2\subset L^1\), multiplication by
\(\epsilon k\) yields exactly the expansion for \(f_i\) at lines 99–100.
Its square contributes only \(O(\epsilon^4)\), establishing (5).

The ordinary third directional derivative claim also holds. The lower
moment is C2 along the fixed line, since its first and second differentiated
integrands are dominated by constants times \(|h|\) and \(|h|^2\).
The upper contraction \(F_i\) is C2 by bounded marks and \(k\in L^1\).
Thus \(f_i=\epsilon F_i\) has a third derivative at zero, with

\[
f_i'''(0)=3F_i''(0)=6v_k^TNA_hu_i,
\qquad
L'''(0)=-12v_k^TNA_hm_y.
\]

This proves actual vanishing of the third directional derivative when
\(m_y=0\), not merely vanishing of a formal Taylor coefficient. It does not
require a third Frechet derivative on the whole Hilbert space.

The Hilbert Hessian exists at the collapsed state. For small increments,
\(a_i=A_hu_i+O(\|h\|_2^2)\), uniformly over the finite sample set.
Expanding the exact physical gradient gives its linear blocks

\[
(D\nabla L(S_*)\delta)_w
 =-2(b_1^TM_*^Tv_k)m_y,
\qquad
(D\nabla L(S_*)\delta)_c
 =-2b_2^TM_*A_hm_y,
\qquad
(D\nabla L(S_*)\delta)_M=0.
\]

The remaining gradient has norm \(O(\|\delta\|^2)\): bounded marks control
the finite moments and upper activations, while Lipschitz continuity of
\(\phi'\) gives
\(\|\phi'(h\cdot u_i)-1\|_2\le C\|h\|_2\).
This supplies the Hilbert, rather than only directional, justification for
the zero Hessian at \(m_y=0\).

### 3. Quadratic/cubic consequences and unfolded extension

The maps \(h\mapsto A_hm_y\) and \(k\mapsto v_k\) are onto when
\(m_y\ne0\), by the displayed Gram-inverse constructions. Those
constructions are bounded and odd. For \(M_*\ne0\), choosing
\(v=M_*a\ne0\) gives the strictly negative quadratic coefficient
\(-2|M_*a|^2\). For \(M_*=0\), choosing \(N=va^T\) gives the strictly
negative cubic coefficient \(-2|v|^2|a|^2\). For \(m_y=0\), both
coefficients vanish for every direction and every matrix. All three stated
consequences are correct.

The requested unfolded extension is justified. Replacing the feature vectors
by the full bounded vectors, including their constant coordinates, changes
only the dimensions in the calculation of (5). No step in that calculation
or in the zero-Hessian argument uses oddness or the absence of constants.
In particular, at the embedded state \((0,0,D)\) of the four-input example,
the quadratic and third directional derivatives vanish for arbitrary fixed
L2 fields and every full matrix variation, including variations of the
constant row and column. A suitable note to add after (5) is:

> Equation (5), and hence the vanishing quadratic and third directional
> derivatives when \(m_y=0\), also hold in the full unfolded p=1 model with
> the constant dictionary features and arbitrary fixed L2 variations. The
> proof uses only bounded marks and \(\tanh''(0)=0\). The explicit descent
> witnesses below remain in the odd sector.

This note does not extend section 4's finite-order theorem to every arbitrary
constant-containing unfolded \(M_*\). The latter theorem is proved for the
nonconstant matrices stated in section 1.

For completeness, the heading “complete quadratic/cubic classification”
need not be read as saying that cubic directions fail when both \(m_y\)
and \(M_*\) are nonzero. They also exist in the stated reduced dimensions:
choose nonzero \(a\in\ker M_*\), nonzero \(v\), and \(N=va^T\).
Then the quadratic coefficient is zero and the cubic coefficient is negative.
The kernel is nontrivial because \(M_*\) has \(2d\) columns and only \(d\)
rows. This is an optional strengthening, not a correction to the three
consequences actually asserted.

### 4. Four-input counterexample and explicit orders

For (6), normalization follows from \(C^2+S^2=1\); \(C,S>0\) gives
distinct, nonparallel, nonantipodal inputs. Direct summation gives
\(m_y=0\) and initial loss 1. Therefore the absence of every cubic
descending direction at \((0,0,D)\) follows from (5).

With \(P_i=(e_1+e_2)\cdot u_i\), the exact lower moment is
\(A\tanh(\epsilon P_i)\), because \(e^2=1\). Thus the displayed upper
composition and its uniform cubic expansion are correct. Writing
\(Q_3=-(Z+Z^3)/3\), the field in (8) is exactly its residual after
orthogonal projection onto \(Z\). Hence
\(E[kZ]=0\) and \(E[kQ_3]=\|k\|_2^2>0\). Finally,

\[
\frac{(C+S)^3+(C-S)^3-2C^3}{4}
 =\frac32CS^2.
\]

This proves the coefficient \(-3CS^2\|k\|_2^2\) in (9), including its
sign and its two-sided quartic descent. Squared predictions start at order
eight and are contained in the stated order-six remainder.

For the origin witness, expansion of
\(\tanh(\epsilon Z\tanh(\epsilon P_i))\) followed by contraction with
\(-\epsilon Z\) gives

\[
f_i=-E[Z^2]P_i\epsilon^3
       +\tfrac13E[Z^2]P_i^3\epsilon^5+O(\epsilon^7).
\]

The order-three loss term cancels by \(m_y=0\), while the order-five term
is \(-E[Z^2]CS^2\epsilon^5\). Squared predictions start at order six.
Equation (10) is therefore correct and gives descent for positive epsilon.

### 5. Finite-order theorem

The excluded hyperplanes are proper under the stated data assumptions, so
the chosen \(P_i\) are nonzero with distinct squares. The Vandermonde
argument then gives at least one odd \(q\le2m-1\) with \(T_q\ne0\).
The proof also covers \(m=1\), where the projection onto earlier powers
means projection onto the zero subspace.

The tanh recurrence at lines 261–263 is correct for \(n\ge1\): its
positive right side proves all odd Taylor coefficients are nonzero.
For nonzero \(M_*\), the coefficient polynomial \(Q_j(Z)\) has degree
exactly \(j\), with leading coefficient equal to the outer tanh coefficient.
Interval support of \(Z\) makes these polynomials linearly independent in
L2. Orthogonal projection therefore yields a nonzero bounded odd
\(R_q\). Its contraction kills each earlier coefficient separately,
which is essential for suppressing earlier positive squared-output terms.
Uniform Taylor expansion yields (12). The squared-output order
\(2q+2\) is at least \(q+3\) for all \(q\ge1\). Thus the leading
negative term has even order \(q+1\le2m\).

For \(M_*=0\), expand the upper tanh by its odd outer power \(\ell\):

\[
\tanh(\epsilon Z\tanh(\epsilon P_i))
 =\sum_{\ell\ \mathrm{odd}}a_\ell\epsilon^\ell Z^\ell
                         \tanh(\epsilon P_i)^\ell.
\]

The readout projection annihilates every outer power \(\ell<q\)
exactly. At \(\ell=q\), multiplication by the readout's extra epsilon
gives the first term at order \(2q+1\), and the next inner term is at
order \(2q+3\). Higher outer powers start later. This verifies (13),
including its sign. Squared outputs have order \(4q+2\ge2q+3\).
The resulting positive-epsilon descent has odd order
\(2q+1\le4m-1\). Both claimed bounds are existence bounds, as stated;
no optimality of these orders is needed or proved.

### 6. Exact representability and scope of the conclusion

At \(w=er\), \(M=D\), let \(t_i=\tanh P_i\). These slopes are nonzero
with distinct squares. If \(\sum_i\lambda_i\tanh(t_iZ)=0\) almost
surely, continuity and interval support give equality on an interval around
zero. Comparing the first \(m\) odd derivatives gives
\(\sum_i\lambda_it_i(t_i^2)^j=0\) for \(0\le j<m\); every omitted tanh
coefficient is nonzero. The Vandermonde matrix is invertible, so
\(\lambda=0\). Thus the Gram \(K_{ij}=E_2[H_iH_j]\) is positive definite,
and the proposed bounded odd readout gives \(f_i=y_i\) exactly.

Every collapsed state has zero individual-sample gradient, so the claim of
zero minibatch noise exactly there is correct for updates formed from those
sample gradients. These proofs do not establish arrival from initialization,
escape under any noise process, global convergence, quantitative uniform
escape rates, or approximation by finite populations or finite networks.
The candidate states these limitations appropriately.

## Final verdict

Internal review: substantive claims pass, with the minor Hessian wording
correction specified above. The unfolded vanishing-coefficient note is
mathematically justified. The frozen version's main proof needs no additional
scientific source, computation, or hypothesis. This verdict covers only the
listed frozen inputs and the stated exact population model; contextual
claims about earlier studies' examples and promotion requirements remain
outside this review.

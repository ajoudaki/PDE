# Check: arbitrary antipodal orientations and the exact discrete symmetries

Post-freeze comparison, 2026-09-16. Read `scalar_margin_extension.md` and the
author's frozen `arbitrary_pair_local.md`. The additionally named
`pair_global.md` was not present at the supplied study path when requested.
Its initialization result is not needed for this check: the frozen arbitrary-
pair map proves positive initial contrast for every distinct pair directly.
No frozen route was modified and no numerical work was performed.

**Verdict.** The scalar theorem does upgrade every antipodal orientation to
every label amplitude `A>0`. It also covers the four signed-permutation
reflections, including reflections across the two diagonal lines. These
diagonal families are valid additional orientations, requiring no rotation
of the dictionary. Generic oriented, non-antipodal pairs remain outside this
symmetry argument.

## 1. The scalar monotonicity argument is valid

For the exact auxiliary gradient flow of `F=<c,U(h)>`, in the fixed physical
metric, write `q=||c||_2^2`, `C=||U||_2^2` and
`K=C+||grad_h F||^2`. Linearity in the readout gives exactly

\[
 F_s=K,\qquad q_s=2F,\qquad F^2\le qC\le qK.
\]

With zero initial readout and `C_0>0`, the Taylor limits are
`c=sU_0+o(s)`, `F=sC_0+o(s)`, `q=s^2C_0+o(s^2)`.
Thus `F,q>0` at positive times, and

\[
 \left(\frac q{F^2}\right)_s
 =-\frac{2(qK-F^2)}{F^3}\le0,
 \qquad \lim_{s\downarrow0}\frac q{F^2}=\frac1{C_0}.
\]

Combining the resulting upper bound on `q/F^2` with Cauchy–Schwarz gives
`C>=F^2/q>=C_0`. This inference has the correct direction and does not
require pointwise monotonicity of `C`. In particular `F_s>=C_0` ensures
that the target `A` is reached in finite auxiliary time at most `A/C_0`.
The stated finite-auxiliary-time characteristic bounds preclude premature
escape. The positive physical clock and energy-to-length argument in the
scalar report consequently give its claimed global physical-time theorem.

## 2. Every antipodal orientation, every amplitude

For any `u in S1`, the exact bias-free closure has

\[
 H(-u)=-H(u),\qquad f(-u)=-f(u)
\]

at every represented state. Thus the opposite-label antipodal probability
law is exactly the one-output objective `(f(u)-A)^2`, without requiring a
mark-space reflection that preserves the dictionary. This remains true
for unequal probabilities on the two compatible antipodal labels.

The initialized map in the frozen arbitrary-pair route is

\[
 H_0(u)=\tanh(Z\cdot\nu(u)),\qquad
 \nu(u)=(\Phi(u_1),\Phi(u_2)),
\]

with `Phi` odd and strictly increasing, and `Z_i=tanh xi_i` having positive
density on `(-1,1)^2`. Since `u` is a unit vector, `nu(u)!=0`; positive
density therefore gives

\[
 C_0(u)=E\tanh^2(Z\cdot\nu(u))>0.
\]

All scalar-theorem hypotheses are now verified for this objective and exact
initialization. For every `A>0`,

\[
 \mathcal L(t)\le A^2e^{-4C_0(u)t},\qquad
 C(X_t)\ge C_0(u),\qquad
 \int_t^\infty\|\dot X\|_{\rm physical}\,dt
 \le\sqrt{\mathcal L(t)/C_0(u)}.
\]

The complete state converges to a fitting state, with the joint-law and
bounded-characteristic conclusions of the scalar theorem. This is an
arbitrary-amplitude result, not a reuse of the small-label basin hypothesis.

There is even an explicit orientation-independent positive rate bound. Let
`sigma_0>0` be the lower bound on `Phi'` from (12) of
`arbitrary_pair_local.md`, and put `gamma=Phi(1)>0`. Then
`||nu(u)||>=sigma_0` and `|Z.nu(u)|<=2gamma`. Integrating the derivative of
tanh on `[-2gamma,2gamma]` gives
`|tanh x|>=sech^2(2gamma)|x|` there. Independence and centering of the two
upper marks yield `E(Z.nu)^2=tau||nu||^2`. Hence

\[
 C_0(u)\ge\tau\sigma_0^2\operatorname{sech}^4(2\gamma)>0
 \qquad\text{uniformly over }u\in S^1.
\]

No claim is made that this conservative analytic constant is numerically
useful.

## 3. Four exact reflection families

The canonical dictionary admits simultaneous signed permutations of the two
input coordinates. Let `P` be a signed-permutation matrix with `P^2=I`.
Its nontrivial possibilities are `-I` and the four reflections

\[
 \begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
 \begin{pmatrix}-1&0\\0&1\end{pmatrix},\quad
 \begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
 \begin{pmatrix}0&-1\\-1&0\end{pmatrix}.                 \tag{1}
\]

The last two are reflections across the diagonal lines. To check these at
the actual normalization, transform `(g,zeta)` to `(Pg,Pzeta)` and `xi` to
`Pxi`; these preserve their Gaussian laws. Raw features transform by signed
permutations `Q_1,Q_2` fixing the constant. Their raw Grams and contraction
obey

\[
 Q_\ell G_\ell Q_\ell^T=G_\ell,
 \qquad Q_2 C Q_1^T=C.
\]

These identities follow directly from the identical independent coordinate
blocks and the equal same-coordinate contraction rows. For the prescribed
Cholesky factors define

\[
 O_\ell=L_\ell^{-1}Q_\ell L_\ell.
\]

Since the ridge matrix also commutes with `Q_l`, one has
`O_l O_l^T=I`; also `O_l^2=I`. Thus these are genuine orthogonal
coefficient-coordinate transformations for the original normalization.
They satisfy `b_l circ S_l=O_l b_l` and
`D=O_2 D O_1^T`.

The state transformation

\[
 \mathcal T_P(w,c,M)
 =(P w\circ S_1,\ -c\circ S_2,\ O_2MO_1^T)
\]

is an isometry of the exact physical metric, fixes initialization, and
changes the predictor to `-f(Pu)`. For two equally weighted inputs
`u,v=Pu`, with targets `+A,-A`, it preserves the loss. The gradient field
is therefore equivariant; uniqueness preserves the fixed-state subspace,
on which `f(v)=-f(u)`. This also follows by substituting into the exact
equations; the transpose transforms as the actual transpose of the same
middle matrix.

For any distinct `u,v`, the frozen initialization map gives `nu(u)!=nu(v)`.
Strict injectivity of tanh and positive mark density then give

\[
 C_0(u,v)=\tfrac14 E[H_0(u)-H_0(v)]^2>0.
\]

The scalar theorem therefore applies to every distinct pair related by
one of (1), for every `A>0`. This includes the coordinate-reflection
families and the diagonal-reflection families, with all their nonzero
angular separations. The four possible bisector lines are the two coordinate
axes and the two diagonals, interpreted as unoriented lines; antipodal
pairs have already been treated in every orientation.

Equal probabilities matter in this reflection argument because the
transformation exchanges two distinct data terms. Unlike the antipodal case,
unequal probabilities do not automatically preserve its loss.

## 4. Why a generic rotation does not supply the missing symmetry

Gaussian-root isotropy alone does not preserve this finite initialized
dictionary. For a row `(a,b)` of an input rotation with `ab!=0`, the function
`tanh(a g_1+b g_2)` does not belong to the raw lower span

`span{1,tanh g_1,tanh g_2,tanh p_1,tanh p_2}`.

Indeed, if such an identity held almost surely, positive joint density and
continuity would extend it to all `(g,zeta)`. Differentiating in each
`zeta_i` forces the coefficient of `tanh p_i` to vanish. The remaining
constant-plus-coordinate sum has zero mixed derivative in `g_1,g_2`, whereas
the mixed derivative of `tanh(a g_1+b g_2)` is
`ab tanh''(a g_1+b g_2)`, which is not identically zero. This is a
contradiction.

Thus the ordinary linear-Gaussian input rotations or reflections preserving
the initialized feature span must have one nonzero entry per row: they are
signed permutations. Quarter-turn signed permutations do not exchange a
non-antipodal two-point set while preserving these opposite labels; their
square is `-I`, so they supply no further two-point symmetry of this form.

This rules out the proposed rotational-isotropy shortcut. It is not a claim
that no entirely different dynamical argument can handle generic pairs, or
an exhaustive theorem about every imaginable nonlinear state isometry.

**Remaining gap:** generic oriented, non-antipodal pairs need not have exact
opposite predictions along training. Their physical vector field need not
be a scalar multiple of `grad F`, so the scalar normalized-margin proof
cannot be applied merely from positive initialized readout rank. The frozen
small-label theorem covers those pairs; arbitrary-amplitude convergence
still needs a two-residual argument or another genuine invariant mechanism.

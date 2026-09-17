# Internal audit: normalized-readout noncollapse principle

Date: 2026-09-16. Scope: internal continuation audit, not promotion review.

**Verdict: PASS under the explicitly stated symmetry and `C_0>0`
hypotheses.** The normalized-readout argument is valid. It proves
`C(X_t)>=C_0`, the stated physical-time loss rate and readout bound,
finite total remaining physical path length, and convergence of the
complete saved state. The singular initialization is handled correctly,
and the crossing argument is not circular. No individual backward-sign
or lower-layer cross-sign condition is required.

This verdict does not prove `C_0>0` throughout the reflected family, and
does not extend the scalar physical-flow reduction to generic oriented
pairs. Those remain separate obligations exactly as the candidate says.

## Inputs and coverage

The complete frozen candidate was read, its hash checked, and the needed
symmetry/auxiliary-flow argument in `proof.md` and canonical state,
equations, physical metric, and local-existence argument were reread.
The rigorous mathematics and adversarial-audit instructions read for the
earlier audit remain the process basis. No other new route or reviewer
finding was read. No numerical experiment was run and no author file
was modified.

| Input | SHA256 |
|---|---|
| `scalar_margin_extension.md`, complete | `3bbf89335a49f9b9c97e4aab8ace450f62d16fc2febe59eaa068b61fcf1dd5e7` |
| `proof.md` | `8cb77d4a1a1f879fa75780efc521f39c63c56feafec4a6c32f15e97ca1621dd0` |
| `docs/global_nonlinear.md` | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

The canonical chapter was not read in its entirety. This continuation
reread `proof.md:77-120` and `docs/global_nonlinear.md:12253-12369`, in
addition to the relevant canonical material already read in the earlier
audit. All source hashes above agree with the previously audited edition
where applicable. The audit covers all mathematical claims of the new
candidate, especially lines 19–60, 74–106, and 114–141.

## 1. Exact metric, scalar reduction, and regularity

The raw physical metric is the fixed product metric

\[
 \|\delta X\|^2
 =E_1|\delta w|^2+\|\delta M\|_F^2+E_2|\delta c|^2.
\]

With `h=(w,M)`, the readout enters linearly:
`F=<c,U(h)>`. Consequently its physical readout gradient is exactly
`U`, without an additional population weight or factor of two, and
`K=||grad F||^2=C+||grad_h F||^2` is the correct orthogonal block
decomposition.

The required symmetry means an actual initialized metric isometry `T`
with `TX_0=X_0` and predictor transformations
`f_+(TX)=-f_-(X)`, `f_-(TX)=-f_+(X)`. These imply invariance of both
the data loss and `F`. Uniqueness therefore preserves the fixed-point
class for both their gradient flows and gives `f_-=-f_+`. This is the
concrete content of the candidate's stated symmetry hypothesis; Gaussian
root isotropy alone is insufficient.

There is no mistake from differentiating only a restricted loss. At any
such symmetric state, let `e=A-F`. The ambient gradient of the actual
unhalved equally weighted loss is

\[
 \nabla\mathcal L
 =(f_+-A)\nabla f_+ +(f_-+A)\nabla f_-
 =-e\nabla f_+ +e\nabla f_-
 =-2e\nabla F.
\]

Thus the entire physical state equation, including transverse
coordinates, is `X_dot=2e grad F` on this invariant class.

The existing characteristic solution space uses bounded `w-g`, bounded
`c`, and finite `M`. Smooth bounded tanh gates and bounded feature marks
make the auxiliary vector field locally Lipschitz there. Along the
resulting differentiable curves, the finite population integrals and
bounded gate derivatives justify differentiating `F` and `q`. In
particular these derivatives are their physical gradient pairings.
The unbounded fixed Gaussian `g` does not obstruct the argument because
it occurs inside bounded gates and has finite second moment.

The finite auxiliary-time bounds invoked from `proof.md` also apply to
every pair of canonical unit directions, not just the earlier narrow
angular interval. Their derivation uses only `|u_+|=|u_-|=1`,
`||U||infinity<=1`, contraction of the feature maps, and `||D||op<=2`:

\[
 \|c_s\|_\infty\le1,\qquad
 \|M_s\|_F\le s,\qquad
 \|w_s\|_\infty\le B_1(2+s^2/2)s.
\]

Integrating supplies the stated bounds. These are bounds in the actual
local-existence norms, so bounded speeds give finite-time endpoints and
continuation through every finite auxiliary interval. This continuation
does not depend on any fitting or noncollapse conclusion.

## 2. Singular initialization and monotonicity

At `c=0`, all hidden gradients of `F` vanish. Therefore
`grad F(X_0)=(0,U(h_0))` in the hidden/readout decomposition, and

\[
 c_s(0)=U(h_0),\qquad F_s(0)=C_0>0.
\]

Differentiability gives the expansions stated in the candidate. Squaring
the readout expansion is legitimate in the Hilbert norm and gives the
additional explicit step

\[
 q(s)=s^2 C_0+o(s^2),\qquad
 F(s)^2=s^2 C_0^2+o(s^2).
\]

Thus `q/F^2 -> 1/C_0` as `s` decreases to zero. Also `F(s)>0` for
small positive `s`; the identity `F_s=K>=0` extends that positivity
to every finite positive `s`. Since `F=<c,U>`, this ensures `q>0`
throughout the same interval. All subsequent divisions are therefore
valid, with no assumption that a crossing has already occurred.

Linearity in the readout and the auxiliary equation give exactly

\[
 q_s=2\langle c,c_s\rangle=2F,\qquad
 F_s=K.
\]

Cauchy–Schwarz in the same upper-population `L2` metric yields
`F^2<=qC<=qK`. Hence for every positive `s`,

\[
 \frac d{ds}\left(\frac q{F^2}\right)
 =\frac{2F}{F^2}-\frac{2qK}{F^3}
 =-\frac{2(qK-F^2)}{F^3}\le0.
\]

To avoid treating the singular initial point as an ordinary
differentiability point, fix `0<r<s`, apply monotonicity on `[r,s]`,
and let `r` decrease to zero using the proved limit. This gives
`q/F^2<=1/C_0`. Combining with Cauchy–Schwarz proves

\[
 C\ge\frac{F^2}{q}\ge C_0,\qquad K\ge C_0
\]

for every finite positive `s`, with equality `C(0)=C_0` at
initialization. This closes the noncollapse step without a hidden
continuity assumption about the ambient ratio at `F=0`.

The equivalent normalized margin `F/sqrt(q)` is nondecreasing and
has initial one-sided limit `sqrt(C_0)`. Its upper bound `sqrt(C)`
is just Cauchy–Schwarz. The decomposition

\[
 qK-F^2=(qC-F^2)+q\|\nabla_hF\|^2
\]

is exact. Since `F>0`, equality in its first term means positive
alignment of `c` and `U`; the second term vanishes precisely when
the hidden gradient vanishes. Neither decomposition implies that `C`
itself is pointwise monotone, and the candidate does not claim that.

## 3. Crossing, physical clock, and constants

Global existence on every finite auxiliary interval was established
first. The now-proved bound `F_s>=C_0` implies
`F(s)>=C_0 s`. At `S=A/C_0`, this is at least `A`. Continuity and
strict monotonicity yield a unique `s_*` in `(0,S]` with
`F(s_*)=A`. There is no circular use of the endpoint in the proof of
noncollapse or existence.

The function `K` is continuous on the compact interval `[0,s_*]`;
the displayed speed estimates also give an explicit finite bound
`K<=1+S^2+(2+S^2/2)^2 S^2`. The scalar clock
`s_dot=2(A-F(s))` consequently stays below `s_*` at finite physical
times. On its positive-residual interval,

\[
 e_t=-2K(s(t))e,\qquad
 e(t)=A\exp\left[-2\int_0^t K(s(v))\,dv\right].
\]

The finite upper bound on `K` excludes finite-time arrival at zero
residual; the lower bound `K>=C_0` forces `e(t)->0`. The increasing
bounded clock then tends to the unique `s_*`. Direct substitution
and physical uniqueness identify this composed curve with the actual
training flow.

All stated factors now check:

\[
 \mathcal L(t)=e(t)^2\le A^2e^{-4C_0t},\qquad
 C(X_t)\ge C_0,\qquad
 \|c(t)\|^2\le F(X_t)^2/C_0\le A^2/C_0.
\]

Also `||X_dot||=2e sqrt(K)` and `-e_t=2eK`, so

\[
 \int_t^\infty\|\dot X(v)\|\,dv
 \le\frac{e(t)}{\sqrt{C_0}}
 =\sqrt{\mathcal L(t)/C_0}.
\]

Multiplying the auxiliary derivative of `P` by `s_dot=2e` gives
exactly `P_dot=-4(A-F)(qK-F^2)/F^3` for `t>0`. It is a
nonincreasing current-state functional along this solution. No decay
to zero, ambient extension, or strict Lyapunov property on neutral
directions is needed or claimed.

## 4. Complete-state convergence and scope

The bounded finite-auxiliary-time solution is continuous through
`s_*`; hence the physical state converges to `X(s_*)`. The path-length
bound also proves this in the complete raw product Hilbert space.
Bounded speeds in the stronger local-existence norms give supremum
convergence of `w-g` and `c`, and Frobenius convergence of `M`.
The endpoint is a fitting state because symmetry gives predictions
`+A,-A` there. “Finite fitting endpoint” refers to a finite state
at finite auxiliary time; it is reached only as physical time tends
to infinity, as the candidate's preceding equations explicitly show.

For the complete saved laws `Law(b_1,g,w)` and `Law(b_2,c)`, coupling
all frozen marks identically bounds their squared `W2` distances by
`E|w(t)-w(s_*)|^2` and `E|c(t)-c(s_*)|^2`. Bounded marks and
Gaussian `g` supply the required second moments. The stored `D` is
fixed and the evolving matrix converges. Thus there is no hidden loss
of part of the saved state in the claimed topology.

For the reflected family `(a,b),(a,-b)`, the earlier isometry calculation
uses only `R(a,b)=(a,-b)` and the unchanged dictionary sign reversal.
It does not use the earlier restriction on `a`. Consequently that
symmetry extends to the whole stated range `a>=0,b>0,a^2+b^2=1`.
Its angular separation is `2 arccos(a)`, ranging over `(0,pi]`.
Positivity of the associated initialized `C_0` over this entire range
is still a separate calculation; this audit does not supply or assume it.

The generic-oriented-pair limitation is necessary and can be seen
directly. Put `G=(f_++f_-)/2`. For any two equally weighted
opposite-label samples,

\[
 \mathcal L=(F-A)^2+G^2,\qquad
 \dot X=2(A-F)\nabla F-2G\nabla G.
\]

Without preserved `G=0`, the second term need not vanish. In particular,
the actual physical readout norm obeys
`q_dot=4F(A-F)-4G^2`, rather than the scalar clock's expression.
The auxiliary monotonicity remains an identity for ascent of `F`, but
does not by itself govern that generic physical trajectory. Initial
`G=0` alone is insufficient without its preservation.

The argument proves noncollapse, not strict learned contrast gain for
every pair. A positive hidden-gradient or misalignment contribution
would be needed for strict normalized-margin growth; a quantitative
positive endpoint contrast gain requires the corresponding quantified
argument. The candidate correctly retains the earlier gain theorem
only within its already-proved scope.

## Adversarial disposition and minor wording

| Objection | Discriminator | Disposition |
|---|---|---|
| Undefined ratio at zero invalidates the starting bound | Expand both numerator and denominator to order `s^2`; apply monotonicity from positive `r` | Ruled out along the initialized path; no ambient extension asserted |
| Noncollapse assumes successful fitting | Inspect order of continuation, positivity, ratio, and crossing arguments | Ruled out; each preceding step is independent of crossing |
| Wrong population metric or loss factors | Differentiate the actual two-atom ambient loss and readout norm | Ruled out; factors `2`, `4`, and the loss exponent agree |
| Narrow-angle bounds were applied outside their domain | Recheck the auxiliary speed and reflection calculations | Ruled out; they use unit inputs and reflection, not a small angle |
| Hidden state can drift despite small loss | Integrate the full physical speed and use finite auxiliary endpoint continuity | Ruled out in the stated saved-state topology |
| Potential contains future information | Inspect definitions of `P,F,q,C_0` and the operational equations | Ruled out; all are current or initialized quantities, and `s_*` is proof-only |
| Generic orientations are silently included | Expand the loss using the mean output `G` | Ruled out as a claim of this candidate; the generic case remains open here |
| Strict feature learning follows automatically | Inspect equality in `qK-F^2` | Not established, and explicitly not claimed |

Two minor editorial improvements would make the statement less ambiguous:

1. Line 118 repeats the earlier `u_+`/`nu_+` naming mismatch; use
   `nu_+` consistently.
2. At line 99, “a finite limiting fitting state” is clearer than
   “a finite fitting endpoint,” since fitting occurs asymptotically in
   physical time.

Neither affects the proof. No fatal, witness-fatal, or major objection
survives for the conditional scalar theorem. The wider arbitrary-
orientation research target is not resolved by this result alone.

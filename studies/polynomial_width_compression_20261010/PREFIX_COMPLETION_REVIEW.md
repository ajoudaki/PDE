# Independent audit of the stopping-prefix completions

2026-10-10. Verdict: **PASS for the two specified completions, at the
conditional scope below.** The revised Taylor construction proves a
uniform Gaussian insertion event over every admissible common domain
prefix, given its stated raw map and actual-control bounds. The rectangular
inward-grid construction resolves the corresponding endpoint issue on
homothetic rectangles. The training-span reduction is an exact
distributional and dynamical identity and imposes no ordering between
the original training count and input dimension.

This is not a certification of the entire Taylor source theorem or the
complete finite-source probability chain asserted in SOURCE_SCOPE_CHECK.md.
The Taylor numerical augmented-map ledger (35) is a supplied input to this
assignment, and the rectangular construction uses its stated enlarged raw
derivative bound. I checked their map interfaces and the new
interpolation/probability arithmetic; I did not independently reconstruct
all upstream numerical bounds, nonlinear insertion remainders,
initialization estimates, scalar absorption, or moment composition from
their original finite-source notes. Nor does this report certify the
Legendre history argument, selected dynamics, or dense-run lower event.

## Frozen inputs and revision disclosure

The following five assigned inputs were read completely. The hashes below
identify the versions supporting the final verdict:

| Input | SHA-256 |
| --- | --- |
| TAYLOR_ROUTE.md | d9153aa789ec23d23683b79f9e5e5a6215a4bb884757079ff1b516235504030e |
| TAYLOR_PREFIX_REPAIR.md | 7e9e027676f68fa362cf4016f578ee4ff96cc8cfbaa7ba63d6457417ebcb0c48 |
| SOURCE_SCOPE_CHECK.md | 767d252e9b5083a3f9e8372856ead1c481b62d3fdfa959d67f73c55b8d78dded |
| paper/compact_foundations.tex | 6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0 |
| studies/unseen_query_decoder_20261005/INSERTION_MAP_MODULI.md | ea71fbc226d4ac02031661a96650256a44260553550ef2b2fd0e10a68b78c93e |

The first three paths are in this study. I also inspected only the
receiving setup in paper/compact.tex, lines 1–150 (file hash
460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe),
and the mobility/comparison interface in paper/compact_legendre.tex,
lines 290–370 (file hash
862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9).

The initial Taylor-repair hash was
e642bcc128153e223cb13d49f40fbb0c8526f1e3ff11ef5e99bf74c391a6fb64.
During this audit I identified an amplitude-envelope mismatch in its
control-net norm estimate. The author replaced that estimate by the affine
control argument now surrounding (23), yielding intermediate hash
2c69ec24b47eeb8425e8f2c80bac23afe96a43ea47f32328f37c1523196a05df.
The author then specified the exact spatial-grid subdivision and corrected
the description of the common amplitude envelope, giving the final hash
above. I reread and checked both revisions. The other assigned and
receiving files did not change between their recorded reads and final
hash check.

The rigorous-math skill and the canonical-notation skill, including its
neural-network reference, were read and applied. No prior review,
study README, study history, additional research source, archived book,
or Git history was used. Only this report was written.

## Taylor: the conditional uniform-prefix event

Use the repair's notation: \(N=m+p\) counts the declared training and
passive inputs, \(u\) bounds same-layer deletions, \(\ell=\log(en)\),

\[
\kappa=1/4000,\qquad
\mathcal C=\beta^{1000L}(1+\lambda^{-1})^2,\qquad
\mathcal A=\mathcal C^4(N+d+u+1)^8.
\]

At its gate \(n\ge\lceil(\mathcal A/\delta)^{40000}\rceil\),
the inequalities used below are
\(\mathcal A\ell^{16}\le n^{1/1000}\),
\(u\le n^{1/8000}\), and
\(\ell\le n^{1/16000}\). They follow from the displayed width
calculation and the definition of \(\mathcal A\); the numerical constants
in the subsequent power comparisons have ample room already at
\(L=2,\beta=10,\delta<1/4\).

The supplied local interface consists of the linear/quadratic operator
bound, control modulus, actual analytic derivative bound, and actual
control amplitude/speed bounds in repair (4)–(6). Its interpretation
matches INSERTION_MAP_MODULI.md: displacement is divided by \(S\),
forward ports remain unscaled, backward fields and reverse ports are
divided by \(S\), and omitted learned parameters and the top prediction
offset remain separate nonlinear sources. The rank-one changed-residual
forcing is present in repair (15). The forward/backward recursions agree
with both the map note and the compact foundation. The augmented response
uses the training driver \(a\), declared evaluated input \(b\), its
additional outgoing port, the direct lower reverse observable, and the
forward images of \(C_a^\top y_i\). None of these probes was removed from
the event. The first-layer and top exceptions match the source interface.

For a fixed cavity, its own stop \(\sigma_c\), its coefficient paths, and
the endpoints \(P_{\min(s_j,\sigma_c)}q\) are measurable in retained
initialization. Conditional on that information, the omitted hidden roots
still have law \(g\sim N(0,I_r/n)\), \(r\le2un\). First-layer incoming
roots need not belong to this concatenation: there is no reverse port
below that layer, and their effect on actual scalar controls is covered
by the eventual uniform substitution. A failed own initialization test
produces zero maps by the declared convention. No full-network survival
event enters this conditioning.

The canonical contour in repair (12) runs along the real axis and then
vertically, followed by a constant segment. Each moving piece lies inside
the tested cavity domain. At negative real coordinates the allowed
vertical radius is constant, so that boundary case is valid too. Its
derivative is \(1,-1,i,-i\), or zero almost everywhere. Integrating against
that derivative gives exactly the forced integral equation (16)–(17);
the frozen portion contributes no length or activity. Consequently the
own-clamped coefficient field is never used as an allegedly holomorphic
extension. A bounded measurable one-dimensional control history is
sufficient for every fixed-contour test.

The net construction has interpolation error at most \(\tau/32\) from
unrounded samples and \(\tau/16\) from real-component rounding, where
\(\tau=n^{-1/8}\). The complex-component error is therefore below
\(\tau\). The logarithmic net size is bounded by (22), namely
\(\mathcal A\ell^8n^{5/8}\le n^{0.627}\). Actual control restrictions,
continued constantly after their contour endpoint, have the required
arclength Lipschitz bound. This constant continuation is an operation on
the contour parameter, not analytic continuation in the plane.

The revised amplitude calculation is necessary and correct. The net
covers the common envelope \(M=\mathcal C\ell\), which can exceed
the original per-type stopped amplitudes. The forced ODE is linear in
controls and its homogeneous propagator is control independent. The
endpoint recursions preserve this dependence; independent probes add a
possible constant term. Scaling a control difference into the original
allowed ball therefore extends its operator modulus to arbitrary bounded
histories. With net norm at most \(2\mathcal C\ell\),

\[
\max(\|L\|,\|R\|)
\le4\mathcal C^2\sqrt u\,n^\kappa\ell^5
\le\mathcal A\ell^{16}n^\kappa
\le n^{1/800}<n^{1/200}.
\]

Thus the enlarged net pays no additional power of \(n\) in the asserted
map bound. The original uncorrected inference that doubling the common
envelope merely doubled the original map bound was not sufficient.

I checked the Gaussian estimates with their displayed constants. For a
real symmetric matrix, expansion of the Gaussian square moment gives

\[
\Pr\{|g^\top Rg-\operatorname{tr}(R)/n|>a\}
\le2\exp\!\left[-\frac18\min\left(
\frac{n^2a^2}{\|R\|_{\rm HS}^2},
\frac{na}{\|R\|}\right)\right].
\]

Indeed the centered log moment is at most
\(2\theta^2\|R\|_{\rm HS}^2/n^2\) for
\(|\theta|\le n/(4\|R\|)\); choosing
\(\theta=\min\{n^2a/(4\|R\|_{\rm HS}^2),n/(4\|R\|)\}\)
and applying the same argument to the opposite sign proves the formula.
The zero matrix gives the inequality directly without these divisions.
For complex symmetric \(R\), test real and imaginary parts and use
\(\|R\|_{\rm HS}^2\le2un^{1.01}\). At
\(t=n^{-1/10}/8\), the quadratic exponents are at least

\[
\min\{n^{0.79}/(2048u),\ n^{0.895}/(64\sqrt2)\},
\]

and the linear-coordinate exponent is \(n^{0.79}/256\). These exceed
\(n^{0.78}\) under the stated gate. The Euclidean image mean is at most
\(\sqrt{2u}n^{1/200}<n^{1/100}/4\); its Gaussian Lipschitz constant
is at most \(n^{-1/2+1/200}\). Its threshold \(n^{1/100}/2\)
therefore has tail at most \(e^{-n^{1.01}/32}\).

On \(\|g\|\le2\sqrt{2u}\), whose failure is at most
\(e^{-un}\), the centered quadratic modulus is

\[
|\mathcal Q_{R_1}(g)-\mathcal Q_{R_2}(g)|
\le(\|g\|^2+r/n)\|R_1-R_2\|
\le10u\|R_1-R_2\|,
\qquad \mathcal Q_R(g)=g^\top Rg-\operatorname{tr}(R)/n.
\]

This explicitly includes the trace; a linear image has a smaller root
multiplier. Thus control interpolation costs at most
\(10n^{-0.12375}<n^{-1/10}/8\), as claimed in (28).

Now select any actual common prefix \(D_\sigma\), with
\(0\le\sigma\le\sigma_c\), after the event has been formed. The
selection may depend on every omitted root. Choose the largest deterministic
level \(s_j\le\sigma\), and a nearby spatial grid point \(q\). The
already tested endpoint is exactly \(P_{s_j}q\), and its entire contour
lies in \(D_\sigma\). Actual controls are therefore defined on every
point where they are substituted. This is the step that is missing from
a construction which merely clamps endpoints by the full random stop.

For completeness, the domains and retractions used here are

\[
D_s=\{x+iy:-sh(0)\le x\le sT_+,\ |y|\le s h(\max(x,0))\},
\]
\[
P_s(x+iy)=X_s(x)+i\operatorname{clip}_{[-s h(X_s(x)_+),
s h(X_s(x)_+)]}y,\qquad
X_s(x)=\operatorname{clip}_{[-s h(0),sT_+]}x.
\]

Here \(h\) is the positive flaring function in TAYLOR_ROUTE.md (5),
with \(0\le h'\le1/8\), and \(H=128\ell/\lambda\) bounds the
enclosing rectangle's side lengths. The level modulus
\(\|P_s-P_t\|_\infty\le3H|s-t|\) and the spatial Lipschitz constant
\(9/8\) give

\[
|z-P_{s_j}q|\le(3/16+9\sqrt2/64)\xi,
\qquad \xi=\frac{n^{-2}}{1+\mathcal A\ell^8}.
\]

The image under \(P_\sigma\) of the segment joining these endpoints is
a curve inside \(D_\sigma\) of length less than \(\xi/2\). Its use
does not require convexity. For each fixed realized collection of actual
analytic control functions, the linear ODE has holomorphic coefficients
and forcing. The interior of \(D_\sigma\), for \(\sigma>0\), is simply
connected by vertical contraction to its real interval. Local linear-ODE
existence, continuation on compact paths, and uniqueness consequently give
one holomorphic solution there. Its restrictions to the canonical contours
are precisely the tested solutions. The algebraic endpoint maps and traces
are holomorphic as well. Their supplied derivative bound is therefore
applicable to this interpolation curve, giving at most

\[
10\mathcal C u^{3/2}n^{\kappa+1/2}\ell^8\xi
\le10n^{-3/2+\kappa}<n^{-1/10}/8.
\]

Boundary values follow from smaller prefixes by continuity; \(D_0\)
contains only the already tested origin. The net threshold and both
interpolation margins total \(3n^{-1/10}/8<n^{-1/10}\).
The Euclidean-image margin also remains sufficient. Neither Gaussianity
nor conditional centering is asserted after adaptive substitution;
\(\operatorname{tr}(R)/n\) is then the value of the frozen-map trace.

Finally, the specified ceiling subdivision gives at most \(n^6\)
spatial points, and the deterministic level mesh has at most \(n^3\)
levels. Including at most \(\mathcal A n^3\) tests per endpoint and
\(uLn^u\) deletion choices, the logarithmic union cost is below
\(n^{0.65}\). This yields (35)'s total failure
\(e^{-n^{0.7}}<\delta/16\). The endpoint cardinality does increase
from \(n^6\) to \(n^9\); its logarithmic cost is absorbed at the
unchanged width gate. There is no increase in the raw map width powers,
the numerical width-gate exponent, the radius, or the Taylor panel and
retained-state counts from this completion.

## Rectangular inward grid and training-span reduction

Here \(p\) denotes the finite source's deletion/moment count, as in
SOURCE_SCOPE_CHECK.md, and \(D_1=[-r,T+r]+i[-r,r]\).
For \(D_\tau=\tau D_1\), rounding both coordinates of \(z\in D_\tau\)
toward zero produces \(g\in h\mathbb Z^2\cap D_1\) satisfying

\[
g\in D_\tau,\qquad [g,z]\subset D_\tau,
\qquad |z-g|\le\sqrt2h.
\]

In this section \(h\) is the lattice spacing, not the Taylor flaring
function. The origin lies in every rectangle. The real-then-vertical
contour to \(g\), including the harmless split at its anchor in \([0,T]\),
stays in \(D_\tau\). The tests at a fixed grid point use the cavity's own
clipped contour and integrate against that contour's increments. These
are retained-measurable Gaussian maps; clipped pieces freeze or shorten
monotonically, so they add no activity or propagator growth. On a common
prefix \(\tau\le\sigma_c\), the clipping is the identity along the
chosen inward contour. Actual analytic controls may thus be substituted
at \(g\), followed by derivative interpolation along \([g,z]\).

For the supplied enlarged derivative bound
\(B\sqrt p\,n^{1/2+1/4000}\ell^8\), where
\(B=X^{1000}\chi^2\), the centered quadratic interpolation error is

\[
10\sqrt2 Bp^{3/2}n^{1/2+1/4000}\ell^8
\frac{n^{-2}}{1+\mathcal A_d\ell^8}
\le10\sqrt2 n^{-3/2+1/4000}<n^{-1/10}/8.
\]

Here \(X=\beta^L\), \(\chi=1+\lambda^{-1}\), and
\(\mathcal A_d=B^2(m+d+p+1)^4\), so \(Bp^{3/2}\le\mathcal A_d\).
The same calculation covers linear images. Counting the fixed lattice by
\([2+(T+2r)/h][2+2r/h]\) gives the original \(n^6\) bound under
the stated gate. There are no random boundary points to test. Own-clamped
scalar references and separately extended common-cavity differences
retain their Gaussian independence and global Lipschitz bounds; Euclidean
ball projection is nonexpansive. The real anchor commutes with the
rectangle clamp. Thus the asserted geometric completion is valid. It is
specific to these rectangles, and establishes no arbitrary-domain or
sphere-frame interpolation result.

For the dimension reduction, take deterministic orthonormal columns
\(V\in\mathbb R^{d\times k}\) spanning the normalized training inputs,
where \(1\le k\le\min(m,d)\), and complete them by \(V_\perp\).
Set \(v'_a=V^\top v_a\), \(A'=W^{(1)}V\), and
\(A_\perp=W^{(1)}V_\perp\). Then \(\|v'_a\|=1\), and orthogonal
Gaussian invariance makes \(A'(0)\) an independent standard Gaussian
matrix, independent also of \(A_\perp(0)\) and the later layers. For the
canonical residual \(r_a=f_a-y_a\) and residual-free backward field
\(\delta_a^{(1)}\), the first-layer flow gives exactly

\[
\dot A'=-\frac2m\sum_a r_a\delta_a^{(1)}v_a'^\top,
\qquad \dot A_\perp=0.
\]

The reduced inputs \(x'_a=\sqrt k\,v'_a\) therefore have the required
input normalization. The forward trajectories, residuals, carriers, and
later flows agree, in the same physical time; local uniqueness also
identifies their complex continuations. The equality
\(v_a'^\top v_b'=v_a^\top v_b\) preserves the entire population Gram
recursion, its gap, and all label and activation parameters. Neuron deletion
commutes with this transformation. Moving first-layer Frobenius norms are
preserved because every increment is \((\Delta A')V^\top\).

The response normalization is also exact. In Euclidean mobility coordinates
\(\theta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)\),
put \(\Theta=\sqrt n\,\theta\), \(F_a=nf_a\). Then

\[
R_{ba}^{(j)}:=D_\theta z_b^{(j)}\nabla_\theta f_a
=D_\Theta z_b^{(j)}\nabla_\Theta F_a.
\]

The factors \(\sqrt n\) and \(n^{-1/2}\) cancel. With
\(c_{ab}^{(j)}=h_a^{(j)\top}h_b^{(j)}/n\) and
\(Q_{ba}^{(j)}=\phi_j'(z_b^{(j)})\odot R_{ba}^{(j)}\), its explicit
recursion is (8): a first-layer term
\(\delta_a^{(1)}v_a^\top v_b\), followed by
\(\delta_a^{(j)}c_{ab}^{(j-1)}+W^{(j)}Q_{ba}^{(j-1)}\).
Every factor is preserved by reduction, with both training indices retained.

Let \(J\) embed reduced mobility variations by \(U\mapsto UV^\top\)
in the first block and act identically elsewhere. For the training feature
Jacobian \(C_a=D_\Theta h_a^{(j-1)}\), its reduced version \(C'_a\)
satisfies \(C_a=C'_aJ^\top\), hence
\(C_bC_a^\top=C'_bC_a'^\top\). Training functions are independent
of the inactive first-layer directions, so their Hessians vanish on those
directions, including mixed blocks. The full variational propagator is
the embedded reduced propagator plus the identity on the inactive
subspace. Endpoint Jacobians annihilate that identity component; cyclicity
of trace then preserves every endpoint contraction and its normalization
by \(1/n\). There is no parameter-dimension multiplier. Interior omitted
row roots still have covariance \(I/n\); first-layer omitted rows retain
the same training-preactivation covariance.

This gives an exact transfer of any valid reduced training-source theorem
to the original problem, with \(\mathcal A_k\le\mathcal A_d\), and
does not require \(m\ge d\). It does not identify full ambient first-layer
operator norms with reduced ones. For an arbitrary unit query \(v\), the
term \(A_\perp(0)V_\perp^\top v\) remains in its preactivation and
must be stored or otherwise preserved by any claimed ambient decoder.
The original ambient fitting/operator event remains necessary. The
candidate states this limitation correctly. The numerical validity and
failure allocation of that upstream fitting event and of the entire
finite-source chain are outside this bounded verdict.

No unresolved defect was found in the final revised completions at this
scope. Their positive verdict must not be substituted for the outstanding
independent checks of the larger source and compression theorems.

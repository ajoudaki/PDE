# Bounded independent audit of the repaired Legendre route

2026-10-10. Fresh scoped proof audit. The candidate was read at SHA-256
`59b7258a1063aba3a4fe158e726f2abad9e49ac28e18df8eae0d01ab10bb466b`.
The hash was unchanged after the mathematical audit. This review changes
neither the candidate nor the paper.

**Verdict: PASS for the new lemmas and their deterministic assembly,
conditional on the supplied finite-source theorem.** I found no missing
implication or counterexample in the finite anti-concentration argument,
conditional innovation lower bound, or the repaired unchanged-closure
\(q^{-3}\) estimate. In particular, the actual physical closure defect does
not invalidate the differentiation in (27), and subtracting its feature
primitive does not invalidate the use of the projection-growth identity
in (34).

This is not an independent certification of the full finite-source theorem
or an approval to promote the assembled headline theorem. Its insertion,
trace and probability-composition proof packet is an explicitly supplied
dependency in this bounded assignment. The distinction matters for both
the quantitative event and its applicability to the full current data
class; see the final section.

## Scope and inputs

The reviewed candidate is `DENSE_LEGENDRE_ROUTE.md`, equations (1)--(42).
I read `paper/compact.tex`, `paper/compact_legendre.tex`, and
`paper/compact_foundations.tex`, and the complete
`unseen_query_decoder_20261005/EXPLICIT_FITTING_WIDTH.md`. I inspected the
statement and parameter interface of
`unseen_query_decoder_20261005/FULL_FINITE_SOURCE_PROBABILITY.md` and
`unseen_query_decoder_20261005/WIDTH_GATE_REFINEMENT.md`; their complete
inherited proof dependencies were not reconstructed. Prior review reports,
study histories, other route outputs and the archived book were not read.
Status descriptions inside the supplied scientific notes were not used as
proof. The rigorous-mathematics skill and canonical-notation skill,
including its neural-network reference, governed this audit.

Throughout, \(X=\beta^L\ge100\), \(\lambda=\gamma/m\le1\),
\(\chi=1+\lambda^{-1}\), \(z=Y/\lambda\le X^{-30}\),
\(\ell=\log(en)\), and \(u=\sqrt\ell\). In particular \(Y\le1\).
For a neuron vector write \(\|v\|_n=\|v\|_2/\sqrt n\), and for a
sample-by-neuron family use the aggregate normalization
\((mn)^{-1/2}\). These are the candidate's normalizations, not additional
assumptions.

## Finite anti-concentration and the dense witness

The characteristic-function calculation in (8) is valid. For a centered
scalar variable \(V\), with variance \(\sigma^2>0\) and
\(\mathbb E|V|^3\le M_3\), an independent copy satisfies
\(\mathbb E|V-V'|^3\le8M_3\). Consequently

\[
|\mathbb E e^{itV}|^2
\le1-\sigma^2t^2+\tfrac43M_3|t|^3
\le1-\tfrac12\sigma^2t^2
\]

when \(|t|\le3\sigma^2/(8M_3)\). Taking square roots gives the
stated Gaussian characteristic-function bound. Gaussian smoothing gives
a central contribution at most \(\sqrt{2e}\,a/\sigma<3a/\sigma\).
The complementary contribution is at most

\[
2\sqrt e\exp[-9a^2\sigma^4n/(128M_3^2)],
\]

which is smaller than the displayed coefficient four. With
\(a=\eta\sigma_0/12\) and \(\sigma\ge\sigma_0\), the width in (9)
makes these contributions at most \(\eta/4\) each. This proves (9)
uniformly over the shift, including conditionally on the specified
sigma-field.

The conditional Gram argument in (10)--(11) follows from the fitting
note's two separate recurrences for standard-deviation and covariance
errors. The chosen \(\epsilon\) ensures

\[
s^2E_{L-1}+D\Delta_{L-1}\le\gamma/(4m).
\]

The operator error is therefore at most \(\gamma/4\), and the conditional
mean top Gram has gap at least \(3\gamma/4\). No inverse of an intermediate
covariance or input-rank condition is used. The Gaussian sixth-moment
estimate \(b+2sH\|G\|_{L^6}\le X^4\) is also valid. The explicit
fitting coefficients give a sufficient envelope smaller than the stated
\(C X^{40}\chi^2\log[32L(m+1)^2/\rho]\).

For completeness, the general innovation estimate requires only
\(\overline Q=\mathbb E UU^\top\succeq gI\), \(m\ge2\), and a finite
fourth moment. Put \(c=\overline Qy\), \(T=\operatorname{tr}\overline Q\),
\(M_4=\mathbb E\|U\|^4\), and

\[
N=y^\top\overline Q^2(TI-\overline Q)y.
\]

The squared-area inequality, split at
\(\|U\|^2=2M_4/[T-c^\top\overline Qc/\|c\|^2]\), gives

\[
\sum_a\operatorname{Var}[U_a(U^\top y)]
\ge \frac{N^2}{4M_4\|\overline Qy\|^2}.
\]

Every eigenvalue \(x\) of \(\overline Q\) lies between \(g\) and
\(T-(m-1)g\). Thus
\(N\ge(m-1)g\|\overline Qy\|^2\) and
\(N\ge g^2(T-g)\|y\|^2\), proving (12). With
\(g=\gamma/2\), \(M_4\le m^2X^{16}\), and
\(\|y\|^2=mY^2\), the largest coordinate variance is at least

\[
\frac{(m-1)^2}{m^2}\frac{g^4Y^2}{4X^{16}}
\ge\frac{Y^2\gamma^4}{256X^{16}}.
\]

This verifies (13) without assuming equal conditional diagonal moments.
Choosing the smallest maximizing index is measurable with respect to
the first network through layer \(L-1\). Conditioning additionally on
the entire second initialization leaves the first network's final rows
conditionally iid and turns the second derivative into an arbitrary shift.

The third-moment bound is
\(M_3\le8m^3Y^3X^{24}\), so
\(M_3^2\sigma_0^{-6}\le2^{30}m^6X^{96}\gamma^{-12}\).
Apply (9) with \(\eta=\delta/2\). The initial derivative multiplier is
\(2/(m\sqrt n)\), giving exactly the threshold in (15).
Condition (14) dominates the resulting
\(2^{43}m^6X^{96}\gamma^{-12}\delta^{-2}\log(32/\delta)\) gate.
Conditional failure is at most \(\delta/4\); allocating at most
\(\delta/4\) to conditional-Gram failure proves the stated
\(\delta/2\) total. No inverse power of \(Y\) remains.

The derivative-to-trajectory conversion also checks. With
\(r=c_\rho/\sqrt\ell\), \(N\le4\ell\), and the prediction envelope
\(32X^6Y/\lambda\), the paper's lemma gives exactly (16).
Making its remainder at most half the first term requires the numerical
coefficient \(2\cdot768\cdot6144=9{,}437{,}184<2^{24}\), hence (17)
suffices. The coefficient \(a_\delta\) in (18) is smaller than the one
obtained this way. Two source failures of size \(\delta/8\), together
with the derivative failure above, leave a valid total budget below
\(\delta\). The maximizing training witness is admissible for the
trajectory norm and has strictly positive time.

## The actual closure velocity and the second forward-history derivative

The response definition (4) and recurrence (5) have the correct mobility
normalization. Indeed the output-gradient blocks in the coordinates
\(\theta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)\) are
\(\delta_a^{(1)}v_a^\top/\sqrt n\),
\(\delta_a^{(j)}h_a^{(j-1)\top}/n\), and
\(h_a^{(L)}/\sqrt n\). Substitution into \(D_\theta z_b\nabla_\theta f_a\)
gives (5), including its lack of an extra factor \(n\).

The all-time response extension in (7) is consistent with one-reference
subtraction. The finite-time coordinate bound is used only on the
reference at \(T\); changed gates multiply this reference response.
The dense parameter tail supplies \(e^{-16\ell}\), and the final
RMS-to-coordinate conversion costs a single \(\sqrt n\), giving
\(n^{-31/2}\). A polynomial gate absorbs the tail without a lower
bound on \(Y\). The same subtraction gives (23)--(24), with substantial
power slack. Under the bootstrap \(D_{T_0}\le Y/\sqrt n\), their
coordinate conversion gives (25).

Here is a direct coefficient check for (27). The all-order physical bounds
imply, uniformly over training samples and layers,

\[
\|\widehat h\|_n\le X^3,\qquad
\|\widehat\delta\|_n+\|\widehat k\|_n\le YX^5\chi,
\qquad \|\widehat R\|_n\le YX^{16}\chi.
\]

The last bound follows directly from (5); it does not use a coordinate
maximum. The ordinary hidden speeds, together with the all-order
pointwise defect, satisfy the candidate's loose bound
\(YX^{20}\chi^3\widehat\rho\) in the sum of hidden block norms.
For example, the total defect coefficient is bounded by
\(X^{12}\sqrt{8z}(8Y/\sqrt\lambda)^2
=64\sqrt8 X^{12}Yz^{3/2}\), which is smaller than
\(YX^{15}\). The readout speed is bounded separately by
\(X^4\widehat\rho\); it need not carry an extra factor \(Y\).
Forward differentiation then gives the first line of (27).

For backward differentiation, the curvature product is

\[
\|\phi''(\widehat z)\dot{\widehat z}\odot\widehat k\|_n
\le X\|\dot{\widehat z}\|_n\|\widehat k\|_\infty
\le Y^2X^{81}\chi^4(1+u)\widehat\rho.
\]

The remaining terms are changed mixers and propagated backward
derivatives, with the top forcing from \(\dot{\widehat w}\).
Propagation by \(9s\) across at most \(L\) layers is covered by
the exponent 110 in the second line of (27).

Differentiating (5) produces precisely the five types listed in the
candidate. Its potentially dangerous curvature term satisfies

\[
\|\widehat W\,[\phi''(\widehat z)
                 \dot{\widehat z}\odot\widehat R]\|_n
\le Y^2X^{167}\chi^7(1+u)\widehat\rho.
\]

The \(\dot\delta\,c\) term is at most
\(X^{116}\chi^4(1+u)\widehat\rho\); feature-pairing and changed-mixer
terms are smaller. Thus the stated forcing envelope
\(X^{180}\chi^8(1+u)\widehat\rho\), and after propagation the
exponent 220, are sufficient. No \(\dot{\widehat z}\) coordinate bound
is used in either differentiation.

Finally, for the ordinary feature velocity per unit residual activity,

\[
a_b^{(j)}=-\frac2m\phi'_j(\widehat z_b^{(j)})\odot
                       \sum_a\widehat v_a\widehat R_{ba}^{(j)},
\qquad \widehat v=\widehat r/\widehat\rho,
\]

sample Cauchy--Schwarz uses \(\|\widehat v\|_m=1\) and
\(\|\dot{\widehat v}\|_m\le X^{11}\). The differentiated response
term contains \(\widehat\rho\le Y\); the normalized-residual
derivative term instead uses \(\|\widehat R\|_n\le YX^{16}\chi\).
The differentiated gate uses the response coordinate maximum and the
preactivation RMS speed. These give the last line of (27), with exponent
230 and the displayed \(\chi^8(1+u)\). The closure defect has been
included throughout in \(\dot{\widehat z}\),
\(\dot{\widehat\delta}\), and \(\dot{\widehat R}\).

Define \(g\) by the primitive subtraction (28). The hidden feature
differential has RMS operator bound at most \(X^5\), so integration
and \(A\le2\) imply (29). On \((1,A)\), exactly

\[
\partial_\tau g=a(t),\qquad
\partial_\tau^2g=\dot a(t)/\widehat\rho(t).
\]

At initialization the readout is zero, hence every ordinary hidden
velocity is zero and \(a(0)=0\). This matches the zero derivative of
the constant prefix. The primitive itself is zero at the join. Thus
there is neither a jump in \(g\) nor a distributional first-derivative
jump in its second derivative. The all-order proof excludes a finite
residual zero for \(Y>0\); all these differentiations are therefore
legitimate at a finite horizon.

For \(\mathscr D_Ag=-\partial_\xi[\xi(A-\xi)\partial_\xi g]\),

\[
\mathscr D_Ag
=-(A-2\xi)a-\xi(A-\xi)\dot a/\widehat\rho
\quad (\xi=\tau(t)>1).
\]

Use \(\xi\le2\) and
\((A-\tau(t))/\widehat\rho(t)\le4/\lambda\). Equation (30)
follows uniformly in the finite horizon. This is the step that handles
the possibly singular activity-clock second derivative at the limiting
endpoint; no endpoint smoothness of \(\widehat v\) is assumed.

The shifted Legendre eigenvalues are \(j(j+1)\). Integrating against
the normalized eigenfunctions twice has zero boundary flux, since
\(g'\) is bounded and \(\xi(A-\xi)\) vanishes at both endpoints.
The prefix join adds no flux. Bessel's inequality consequently gives
(31). Projection contraction applied to \(h-g\) then gives (32),
since \(1+u\le2\ell\) and \(P=X^{500}\chi^{10}\) dominates all the
preceding coefficients.

## Projection defect, absorption and the current order

The inherited backward-history estimate gives (33). Its coefficient
\(b_0+b_1\sqrt{\log q}\) is bounded by \(YP\ell\) when
\(q\le\sqrt n\), and \(B_d\sqrt{4z}\le P\ell\).
The bootstrap then makes its comparison error no larger than
\(YP\ell/q\).

Equation (34) applies the growing-interval identity to the original
histories \(h,b\) of the one closure trajectory. For any fixed finite
horizon, these are fixed functions on \([0,A]\), and their prefix
projection tails vanish. Thus the activity integral of each squared
endpoint error equals its final squared projection tail. Sample and
activity Cauchy--Schwarz give
\(d_{T_0}\le2(L-1)H_{T_0}B_{T_0}\). The corrected history \(g\) is
used only to bound the final forward tail. No projection-growth identity
for a horizon-dependent corrected history is being substituted here.

The signed comparison coefficient also has the asserted numerical bound.
Put \(a=X^{36}z^2\le X^{-24}\). Since
\(\sqrt{1+\log n}\le1+\tfrac12\log n\),

\[
\log\mathcal A_n
\le1+\log X+a+\tfrac a2\log n
\le2\log X+\tfrac1{64}\log n.
\]

This proves (36) uniformly, without an exponential qualifying width.
Substituting (32)--(33) into (34) yields

\[
d_{T_0}\le
\frac{2Y^2P^3\ell^2}{q^3}
+\frac{2YP^3\ell}{q}d_{T_0}.
\]

The condition \(q\ge4P^3\ell\) absorbs the second term. Using
\(Y\le1\) gives exactly (37); the proof actually retains an extra
factor \(Y\) before this last enlargement.

For the unchanged order
\(q=\lceil\lambda^{-3}n^{1/4}\ell^2e^{u/2}\rceil\), all three
conditions in (39) hold under \(n\ge(CP)^{64}\) with a universal
constant. The supplied bound
\(\ell^2e^{u/2}\le e^{100}n^{1/8}\) proves the first, including
the ceiling. The second already follows from \(n^{1/4}\ge4P^3\).
The elementary bound
\(\ell^2\le e^{1/64}(128/e)^2n^{1/64}\) proves the third under a
smaller power gate than \((CP)^{64}\).

Consequently (37) improves the bootstrap to
\(D_{T_0}\le Y/(2\sqrt n)\). The discrepancy supremum is continuous
in a finite horizon, starts at zero, and cannot have a first exit.
Uniformity in that horizon and the all-order fitted limits then give
the complete-time estimate. Whole-sphere forward subtraction costs
at most \(X^7D_{T_0}\), giving (40). The moving inventory is the
original \(n(d+1)+1+2(L-1)mnq\); \(n\ge d^4\) suffices to absorb
the first-layer term into the claimed headline order. The initialized
fixed mixers remain additional storage.

Dividing (40) by (18) gives exactly (41). Since
\(\ell^{9/2}n^{-7/64}\) has a finite universal supremum, (42) follows.
Confidence splitting needs only a union bound, not independence between
the approximation and variability events. The closure order is independent
of the requested relative tolerance.

## Boundary of the conclusion

The new deterministic mechanism has been independently reconstructed at
the stated order, with the actual closure defect and the stated polynomial
parameter coefficients. The conditional innovation and finite
anti-concentration proof are likewise quantitative and do not hide a
qualitative central-limit onset or an inverse-label width threshold.

The complete source theorem remains a supplied dependency. Its statement
has the source rectangle and caps used by the candidate; the refinement's
stated power-1100 envelope agrees with (2). Its scientific insertion maps,
common-cavity moment proof, finite probability composition and complete
local dependencies were not independently re-audited here. Reading the
compact foundation argument does not by itself certify that separate
quantitative refinement.

The original source statement retains \(m\ge d\), whereas the current
paper does not. The explicitly read fitting proof proves that its own
argument does not need this restriction, and the new initialization,
innovation and Legendre arguments above do not need it either. The
candidate additionally asserts that the finite-source insertion and
concentration argument extends without it. This bounded review does not
certify that inherited extension merely from the fitting observation.
For a fully unconditional statement over the entire current setup, the
source audit must verify that extension (or supply the source theorem for
that setup). Conditional on the source event with the stated properties,
the new proof above has no residual use of \(m\ge d\).

No conclusion is reached here about repairing Harmonic or Taylor, practical
onset widths, the stronger original dense lower-bound coefficient, or
promotion of these research results.

## Addendum: completed source scope and polynomial-width assembly

2026-10-10. I read `SOURCE_SCOPE_CHECK.md` completely at SHA-256
`767d252e9b5083a3f9e8372856ead1c481b62d3fdfa959d67f73c55b8d78dded`.
The Legendre candidate remains at the hash recorded above. For the specific
stopping-prefix issue, I also read the complete named scientific dependency
`INSERTION_MAP_MODULI.md` and checked the source's maximum, moment and
failure-allocation formulas in `FULL_FINITE_SOURCE_PROBABILITY.md`,
Sections 5--7. No other review report or study history was used.

The source completion supplies precisely the premises required by this
review. The following checks discharge the previously identified scope
and assembly boundary.

First, the training-span reduction is exact. With deterministic
orthonormal columns \(V\) spanning the training inputs and
\(k=\dim\operatorname{span}\{v_a\}\), one has
\(1\le k\le\min(m,d)\), unit reduced inputs \(V^\top v_a\), and
\(W^{(1)}v_a=(W^{(1)}V)(V^\top v_a)\). The reduced first matrix
has the stipulated independent standard Gaussian entries, independent of
its orthogonal complement. Its update has the original normalization and
physical learning rate; the orthogonal complement has zero update.
Training trajectories, covariances, \(\gamma,Y,\lambda\), neuron
deletions, and the moving parameter norm are preserved. Applying the
finite source in dimension \(k\le m\) therefore establishes its
training conclusions for arbitrary original \(m,d\), without assuming
that an ambient query lies in this span.

The ambient real fitting event is retained separately. In particular,
the first-layer contribution
\(W^{(1)}(0)V_\perp V_\perp^\top v\) for a general unit query is
preserved, and the original \(d\)-dimensional sphere bounds control
the whole-sphere Legendre comparison. The source width uses
\(\mathcal A_d=X^{2000}\chi^4(m+d+p+1)^4\), which is at least the
reduced-dimensional coefficient. Its two consequences

\[
\mathcal A_d\ell^{16}\le n^{1/1000},\qquad
n\ge64mL/\rho
\]

also dominate the explicit ambient fitting gate. The source reconstruction
retains total failure less than \(5\rho/8\) before adding an ambient
fitting failure \(\rho/32\), leaving total failure below
\(21\rho/32<\rho\). Thus this extension does not require replacing
\(\rho\) by a smaller number inside \(p\), changing the radius, or
increasing the outer power 1100.

Second, the response interface is the required one. Since
\(\Theta=\sqrt n\theta\) and \(F_a=nf_a\),

\[
D_\theta z_b^{(j)}\nabla_\theta f_a
=D_\Theta z_b^{(j)}\nabla_\Theta F_a.
\]

The span reduction preserves its recurrence (5) and its lower-probe
contractions \(C_bC_a^\top\); inactive parameter directions contribute
zero. The trace normalization remains \(1/n\). The supplied coordinate
bound is consequently exactly
\(16(Y/\lambda)X^{26}\sqrt\ell\) for this response on the finite
training rectangle. It is uniform in both training indices, which also
permits the measurable witness index in the dense-variability argument.
Sections 6 of the completion and 1 of the candidate then provide the
all-time carrier cap (6) and response cap used in (24)--(27). Their real
tail extensions have polynomial gates already dominated by the source
width. No additional probability event or inverse-label threshold appears.

Third, the new inward grid addresses the specific stopping-prefix
interpolation issue. Rounding a point of the rectangle \(D_\tau\)
toward the origin produces a point of the fixed deterministic tensor grid
which is also in \(D_\tau\), with the joining segment inside that
rectangle. The canonical contour to that grid point stays inside the
same rectangle. On a common surviving prefix, each cavity's own clamp
is therefore the identity there. At a fixed grid point, the tested contour
depends only on retained initialization, so the omitted-root Gaussian
calculation remains valid. Actual analytic controls may then be substituted
on the uniform grid event, and the terminal derivative estimate applies
along the interior joining segment. This matches the distinction made
explicitly in `INSERTION_MAP_MODULI.md`: arbitrary one-dimensional control
nets are used for the conditional tests, while off-grid complex
interpolation is used only for the actual analytic controls.

The new mesh \(h=n^{-2}/(1+\mathcal A_d\ell^8)\) makes the centered
quadratic interpolation error at most the quantity in source-completion
(13). The prefactor after substitution is bounded by
\(10\sqrt2 Bp^{3/2}/\mathcal A_d\), with
\(B=X^{1000}\chi^2\), while the width power is
\(n^{-3/2+1/4000}\). It is smaller than \(n^{-1/10}/8\) on the
existing gate. The real side length is at most
\(32\ell/\lambda+2\), the imaginary side at most two, and the same
gate bounds the tensor-grid count by \(n^6\). The completion therefore
does not add an unpaid entropy or failure cost. No Gaussian assertion at
an endpoint clamped by the full-network stop is needed.

The source result used by Legendre is now, for every \(0<\rho<1/4\),
an event of failure at most \(\rho\) under the unchanged explicit
power-1100 width, providing the ambient real fitting bounds and the training
analytic rectangle with

\[
r=[p_\rho X^{100}(1+\lambda)\sqrt\ell]^{-1}.
\]

Its training forward/backward RMS bounds give the prediction envelope
needed for the derivative-to-trajectory step. This radius is the one used
in candidate (16)--(18). It does not supply the larger radius
\(1/(\lambda\sqrt\ell)\) appearing in the original compact statement.

For an explicit final assembly, fix \(0<\delta<1\) and a desired
relative tolerance \(\epsilon>0\). Apply the candidate's dense lower
bound with failure parameter \(\zeta=\delta/2\), and use its source
allocation \(\rho=\zeta/8=\delta/16\). The deterministic Legendre
estimate applies on the coupled run's source event with this same
\(\rho\). Even treating these two events separately, their union
failure is at most \(\delta/2+\delta/16<\delta\). No independence
is needed. On their intersection,

\[
\|f_{\rm Leg}-f_n\|_{\mathcal X}
\le4YP^5\ell^2n^{-47/64},\qquad
\|f_n-\widetilde f_n\|_{\mathcal X}
\ge a_\zeta Y n^{-1/2}\ell^{-5/2},
\]

where \(P=X^{500}\chi^{10}\) and

\[
a_\zeta=
\frac{\zeta\gamma^2}
{2^{20}mp_{\zeta/8}X^{108}(1+\lambda)}.
\]

Taking the maximum of the source gate, the candidate's initialization
and anti-concentration gates, its derivative-transfer gate, the
\((CP)^{64}\) bootstrap gate, and
\([4C_2P^5/(a_\zeta\epsilon)]^8\) proves the claimed relative tolerance
with probability at least \(1-\delta\). Each gate is polynomial in
the exposed activation/depth envelope, sample and ambient dimensions,
inverse gaps, inverse confidence and inverse tolerance, with the stated
logarithmic moment-order dependence. There is no inverse power of \(Y\).
The original order
\(q=\lceil\lambda^{-3}n^{1/4}\ell^2e^{\sqrt\ell/2}\rceil\),
optimizer, moving inventory and fixed mixer storage are unchanged.
The bounds include all physical times, the fitted endpoint and the full
ambient sphere.

**Updated assembly conclusion:** the polynomial-width Legendre guarantee
is now internally justified by the completed finite-source reconstruction
and the independently reconstructed new lemmas in this review. The
previously outstanding \(m<d\) applicability issue and the precise
source-to-Legendre interface are discharged. This follow-up verifies the
new span/grid completion and final assembly; it is not a second complete
independent reconstruction of every nonlinear insertion, trace and moment
calculation in the nine-file inherited source packet. That remaining
review-scope limitation is distinct from an identified mathematical gap
in this assembled route.

The conclusion retains the weaker explicit coefficient \(a_\zeta\).
It does not establish polynomial onset for the original stronger lower
coefficient \(c_{\phi,L,\delta}\sqrt\gamma\), which was stated to
depend only on activations, depth and confidence apart from
\(\sqrt\gamma\). Nor does this addendum certify the selected methods,
practical widths, or promotion to the maintained paper or book.

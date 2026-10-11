# Width-onset transfer: exact positive statements and remaining Harmonic gap

2026-10-11. Scoped reconstruction for this study. Only this file is written;
the manuscript, maintained book, and Git index are unchanged. This is an
internal transfer note, not a promotion or an independent review of the
entire inherited source chain.

**Continuation update.** The user subsequently authorized the three raw
dependency files listed below. `WIDTH_DEPENDENCY_CHECK.md` now reconstructs
their coefficients and the complete finite source-probability composition,
closing the uninspected-input qualification in this initial transfer note.
The earlier reading-scope account below is retained as an audit record, not
as a current unresolved permission request. `HARMONIC_ONSET_ROUTE.md` and
its separate check also establish a source-class obstruction to a uniformly
polynomial fixed-dimension onset over shrinking-label/gap families; they do
not settle fixed positive labels or arbitrary output-only compression.

The permitted prior study contains positive polynomial-width repairs for
Legendre and Taylor. It explicitly leaves the fixed-dimension Harmonic
repair open. The growing-dimension Harmonic obstruction does not settle
that fixed-dimension question. The positive dense lower bridge concerns a
supremum over the complete trajectory; it gives no same-time denominator
bound.

## 1. Receiving setup and the source-evidence boundary

Use the network of `paper/compact.tex`. For unit normalized inputs
\(v=x/\sqrt d\), width \(n\), and \(L\ge2\),

\[
z^{(1)}=W^{(1)}v,\qquad
z^{(j)}=W^{(j)}h^{(j-1)},\qquad
h^{(j)}=\phi_j(z^{(j)}),\qquad f_n=w^\top h^{(L)}/n.
\]

There are \(m\ge2\) training samples, residuals \(r_a=f_n(x_a)-y_a\),
loss \(m^{-1}\sum_a r_a^2\), independent first-layer \(N(0,1)\)
entries, independent later \(N(0,1/n)\) entries, and zero initialized
readout. Physical gradient-flow mobilities are \((n,1,\ldots,1,n)\).
The activations are real on the real axis, holomorphic on a common strip,
and have bounded first derivative there; their values may be unbounded.
The activation envelope \(\beta\ge10\), population feature Gram
\(Q^{(L)}\), gap \(\gamma=\lambda_{\min}(Q^{(L)})>0\), and label
RMS \(Y=\|y\|_2/\sqrt m>0\) have exactly the manuscript definitions.
Set, for this note,

\[
X=\beta^L,\quad \lambda=\gamma/m\le1,\quad
z=Y/\lambda\le X^{-30},\quad \chi=1+\lambda^{-1},\quad
\ell=\log(en).
\tag{1}
\]

The scalar \(z\) here is the label-to-gap ratio, not a preactivation.
No assumption \(m\ge d\), input-rank assumption, bounded activation-value
assumption, or stronger label cap is added. Taylor has \(p\) passive
inputs fixed before initialization and \(N=m+p\); they receive no labels.

For a query set \(\mathcal X\), define

\[
\|g\|_{\mathcal X}
=\sup_{t\in[0,\infty]}\sup_{x\in\mathcal X}|g(t,x)|,
\tag{2}
\]

where infinity denotes the fitted limit. Legendre and Harmonic use the
whole sphere; Taylor uses the declared panel. Each probability assertion
is at each individual width, for fixed data and parameters, not on one
event simultaneous over all independent widths.

The original manuscript's fitting/source statements are eventual:
`compact_foundations.tex` uses fixed-order limits in its budget-removal
argument and qualitative absorption of coefficient factors. Merely using
that event leaves an unspecified threshold \(N_{\rm event}\).

The permitted prior study supplies stronger, explicit source assertions.
For \(0<\rho<1/4\), put

\[
u_\rho=\max\left\{1,\left\lceil
\frac{\log(4emL/\rho)}{\log(64e^2)}\right\rceil\right\}.
\]

- **Finite-training source assertion \(S_L\).**
  `SOURCE_SCOPE_CHECK.md`, especially (2), (10), (18), and (20), supplies
  the ambient real fitting event, training source rectangle, carrier caps,
  and normalized training-response caps with failure at most \(\rho\) at

  \[
  n\ge N_{L,\mathrm{src}}(\rho):=
  \left\lceil\left[
  \frac{X^{2000}\chi^4(m+d+u_\rho+1)^4}{\rho}
  \right]^{1100}\right\rceil.
  \tag{3}
  \]

  Its rectangle has \(T=32\ell/\lambda\) and radius
  \(r=[u_\rho X^{100}(1+\lambda)\sqrt\ell]^{-1}\).
  This is smaller than the manuscript's eventual
  \(1/(\lambda\sqrt\ell)\) radius. It must not be substituted for
  that radius without carrying the loss through the lower bound.

- **Finite-panel source assertion \(S_T\).** `TAYLOR_ROUTE.md` (26),
  with its endpoint paragraph replaced by `TAYLOR_PREFIX_REPAIR.md`,
  supplies the capped flaring source event, with failure at most \(\rho\),
  at

  \[
  n\ge N_{T,\mathrm{src}}(\rho):=
  \left\lceil\left[
  \frac{X^{4000}\chi^8(N+d+u_\rho+1)^8}{\rho}
  \right]^{40000}\right\rceil.
  \tag{4}
  \]

These are proposed full quantitative source gates in the prior study,
not just deterministic approximation gates. They contain no \(Y^{-1}\).
They are polynomial in the displayed parameters, with fixed numerical
degrees, though enormous.

**Direct reconstruction and its limit.** I read the complete source-scope
note, both Taylor notes, dense/Legendre route, finite anti-concentration
lemma, and fixed-dimension Harmonic scope note, together with the complete
receiving fitting, foundations, Legendre, and selected proof modules.
The training-span reduction preserves every training inner product and
the Gaussian first matrix, while its frozen orthogonal complement must
remain for sphere queries. The inward rectangular mesh and the Taylor
deterministic-level mesh both resolve the root-dependent stopping-endpoint
problem: Gaussian tests are formed conditional only on a cavity, then the
successful uniform event is evaluated on actual controls.

The Taylor repair's proof explicitly assumes its raw map estimates (4)--(6).
Three exact dependency files under
`studies/unseen_query_decoder_20261005/` are needed for a fresh audit of
the unreproduced numerical details:

- `INSERTION_MAP_MODULI.md`: recurrences (4)--(20) for the map norms,
  scalar-control Lipschitz constants, terminal derivatives, and the
  coefficient envelope used by Taylor (35) and prefix-repair (4)--(6).
- `EXPLICIT_FITTING_WIDTH.md`: finite initialized norm and covariance
  concentration, including singular intermediate covariances, behind
  the polynomial Gram gate; the manuscript proves this convergence
  qualitatively.
- `QUANTITATIVE_INSERTION_WIDTH.md`: explicit normalized forcing and
  port-map constants behind the prefix repair's integrated map (18).

These files are outside this subagent's assigned scope and were not
fetched. The permitted notes reconstruct the composition,
and the manuscript gives the actual differential/remainder identities;
they do not reproduce every underlying quantitative recurrence. Thus this
note checks the new deterministic calculations, stopping-mesh repairs, and
the following assembly, while taking (3)--(4), including their numerical
local-map envelopes, as named study-level source lemmas. It does not claim
a fresh complete independent certification of unseen source files.
There is no additional *unquantified* source threshold in (3)--(4) as
stated. If only the manuscript source theorem is accepted, the statements
below instead have threshold \(\max(N_{\rm event},N_{\rm structural})\),
and the full sufficient width has not thereby been shown polynomial.

## 2. Dense trajectory lower bridge and exact scope

On \(S_L\) for both independent runs, the route proves, after the
additional explicit gates below,

\[
\Pr\!\left\{
\|f_n-\widetilde f_n\|_{\mathcal X}
\ge a_\delta\frac{Y}{\sqrt n\ell^{5/2}}
\right\}\ge1-\delta,
\qquad
a_\delta=
\frac{\delta\gamma^2}
{2^{20}m u_{\delta/8}X^{108}(1+\lambda)}.
\tag{5}
\]

The query set may be any promised domain containing the training inputs.
This coefficient is weaker than the manuscript coefficient
\(c_{\phi,L,\delta}\sqrt\gamma\); the latter's polynomial onset is
not established by this replacement.

Here is the direct lower-bound reconstruction. Conditional on the first
run through layer \(L-1\) and the entire second run, let \(U_i\in\mathbb R^m\)
be the first run's iid final-layer feature rows. Quantitative initialized
covariance concentration gives
\(\mathbb E[U_iU_i^\top\mid\mathcal F]\succeq\gamma I/2\) and
\(\max_a\|U_{i,a}\|_{L^6(\cdot\mid\mathcal F)}\le X^4\).
The squared-area inequality applied to \(U(U^\top y)\) then supplies a
training index measurable in \(\mathcal F\) with centered row-product
variance at least \(Y^2\gamma^4/(256X^{16})\) and third absolute moment
at most \(8m^3Y^3X^{24}\). The exact initial identity is

\[
\dot f_n(0,x_a)=\frac2{mn}\sum_{i=1}^n U_{i,a}(U_i^\top y).
\]

For centered iid \(V_i\), variance \(\sigma^2\), third absolute moment
at most \(M_3\), Gaussian smoothing of the characteristic function gives

\[
\sup_b\Pr\!\left(
\left|n^{-1/2}\sum_iV_i-b\right|\le h\right)
\le\frac{3h}{\sigma}
 +4\exp\!\left[-\frac{9h^2\sigma^4n}{128M_3^2}\right].
\tag{6}
\]

The characteristic-function bound follows from symmetrization:
\(|\mathbb Ee^{itV}|^2\le1-\sigma^2t^2+(4/3)M_3|t|^3\), so
\(|\mathbb Ee^{itV}|\le e^{-\sigma^2t^2/4}\) on
\(|t|\le3\sigma^2/(8M_3)\). Fourier inversion of the Gaussian
majorant gives (6). The second run and the conditional means contribute
only the shift. Thus no conditional CLT or matched conditional mean is
needed.

One sufficient derivative gate supplied in the route is

\[
n\ge2^{44}m^6X^{96}\gamma^{-12}\delta^{-2}\log(64/\delta),
\tag{7}
\]

in addition to the conditional covariance gate (its explicit (11), bounded
by a universal multiple of
\(X^{40}\chi^2\log[32L(m+1)^2/\rho]\)). On the resulting event the
initial derivative difference is at least
\(\delta Y\gamma^2/(192mX^8\sqrt n)\).
For a scalar holomorphic difference \(g\), the manuscript's elementary
Chebyshev argument gives

\[
\sup_{[0,r]}|g|
\ge\frac{r|g'(0)|}{2K^2}-24M2^{-K}.
\]

Use \(K=\lceil2\ell/\log2\rceil\),
\(M=32X^6Y/\lambda\), and the smaller radius in (3). The remainder
is absorbed, for example, under the explicit gate

\[
n^{3/2}\ge
2^{24}u_\rho X^{114}
\frac{m(1+\lambda)}{\lambda\delta\gamma^2}\ell^{5/2}.
\tag{8}
\]

A sufficiently large universal multiple of
\([u_\rho X^{120}m\chi(1+\gamma^{-1})^2\delta^{-1}]^4\)
implies (8). Allocate \(\rho=\delta/8\) to each source and the
remaining failure to covariance and scalar concentration to obtain (5).

The witness is a training input at some strictly positive time because
both runs start at zero. It need not be a fixed or common prescribed time.
Both runs fit the same labels, so their discrepancy at each training
input is zero at infinity. In particular (5) cannot justify
\(\sup_t\|f_{\rm model}(t)-f_n(t)\|/\|f_n(t)-\widetilde f_n(t)\|\),
a pointwise-in-time lower event, or an endpoint denominator.

## 3. Legendre: unchanged method, polynomial structural gates

The moments, initialized hidden mixers, residual-activity clock, physical
optimizer, and order are unchanged. Take

\[
q=\left\lceil\lambda^{-3}n^{1/4}\ell^2e^{\sqrt\ell/2}\right\rceil,
\qquad P=X^{500}\chi^{10}.
\tag{9}
\]

On the fitting/source event, at
\(n\ge(CP)^{64}\) for a sufficiently large universal \(C\), the
new route proves

\[
\|f_{\rm Leg}-f_n\|_{\mathcal X}
\le4YP^5\ell^2n^{-47/64}.
\tag{10}
\]

Its exact moving count and separate fixed count are

\[
n(d+1)+1+2(L-1)mnq,
\qquad (L-1)n^2.
\tag{11}
\]

Consequently, with the additional polynomial simplification gate
\(n\ge d^4\), (11) has the unchanged headline moving bound
\(C m(m/\gamma)^3n^{5/4}\ell^2e^{\sqrt\ell/2}\), with
activation/depth-only \(C\). Data storage is additional.

The extra approximation order is obtained without changing the closure.
Let \(d_T\) be the integrated hidden physical defect and \(D_T\) the
supremum of the sum of mobility-block discrepancies up to time \(T\).
Subtract the integrated defect contribution from the forward history,

\[
g(\tau(t))=\widehat h(t)
-\int_0^tD_\theta h(\widehat\theta(s))\mathcal E(s)\,ds.
\]

Then \(\partial_\tau g\) is the ordinary feature velocity per unit
residual activity, evaluated on the actual closure trajectory. Its
derivative includes the actual defect in that trajectory. The route
bounds curvature products using coordinate caps on reference responses
and RMS bounds on preactivation velocities; it never inserts an
uncontrolled coordinate maximum of that velocity. The constant prefix
joins with zero first derivative because the readout starts at zero.
For final clock value \(A\), the endpoint weight in
\(-\partial_\xi[\xi(A-\xi)\partial_\xi]\) cancels the possible
\(1/\widehat\rho\) singularity, since
\((A-\tau(t))/\widehat\rho(t)\le4/\lambda\).

The resulting forward/backward projection tails satisfy, on the bootstrap
\(D_T\le Y/\sqrt n\) and \(q\le\sqrt n\),

\[
H_T\le YP\ell/q^2+Pd_T,\qquad
B_T\le2YP\ell/q,
\]

while the exact growing-interval projection identity gives
\(d_T\le2(L-1)H_TB_T\). The signed physical comparison gives
\(D_T\le\mathcal A_nd_T\), with
\(\mathcal A_n\le eX\exp(X^{36}z^2\sqrt\ell)\le Pn^{1/64}\).
The small-label condition is used here to bound the exponent, not to
erase a displayed sample/gap storage power. Absorbing the term linear in
\(d_T\) when \(q\ge4P^3\ell\) gives

\[
d_T\le4YP^3\ell^2/q^3,
\qquad D_T\le4YP^4\ell^2n^{1/64}/q^3.
\]

The width above (10) also implies
\(q\le\sqrt n\), \(q\ge4P^3\ell\), and
\(8P^4\ell^2\le n^{15/64}\); hence the bootstrap improves strictly.
Sphere prediction subtraction costs at most \(X^7D_T\), proving (10)
uniformly over finite horizons and then at the existing fitted limits.

For requested trajectory-ratio tolerance \(\varepsilon>0\), intersect
(10) with (5), splitting the failure budget. The ratio is at most
\(4P^5a_\delta^{-1}\ell^{9/2}n^{-15/64}\).
Since \(\ell^{9/2}\le C_2n^{7/64}\) for a universal constant,

\[
n\ge[4C_2P^5/(a_\delta\varepsilon)]^8
\tag{12}
\]

is a further polynomial sufficient gate. This is a complete deterministic
and probability assembly given \(S_L\), with no inverse-label gate.
At widths below these gates, the exact count (11) remains the count; the
all-order fitting theorem holds on its initialization event, but (10) is
not asserted. The proof restriction \(q\le\sqrt n\) is not a restriction
in the definition of the closure.

## 4. Taylor: changed proof radius, unchanged runtime and headline powers

The selected optimizer, exact-metric selection, origin-jet provenance, and
declared query panel are unchanged. The source radius and consequently
the deterministic proof partition are changed. With the source constants
\(\eta_*,\mathcal K,U_{\rm fin}\) defined by the recurrences in
`compact_foundations.tex`, set \(a_0=\min(a,1)\),

\[
b_n=\log(e+\ell),\quad B_n=1+(256z^2/\eta_*)b_n,\quad B=X^{300},
\]
\[
r_n=\min\left\{
\frac{a_0}{1024\lambda z^2U_{\rm fin}\sqrt\ell},
\frac1{B(1+\lambda B_n)\sqrt{b_n}}\right\}.
\tag{13}
\]

The source construction uses
\(h(t)=(2\mathcal K)^{-1}\log(1+2\mathcal Kr_ne^{\lambda t/4})\)
and disks of radius \(h(t)/[2(1+\lambda/(8\mathcal K))]\).
Its partition count obeys

\[
J\le1+X^{400}\left[z^2\sqrt\ell+\lambda^{-1}\log(e+\ell)\right]
\tag{14}
\]

after harmless enlargement of an activation/depth coefficient. The cap
contains no confidence order. The direct check is
\(4\mathcal Kr_n+(2C_g/\sqrt{\mathcal K})B_nYr_n<\log(3/2)\);
the sum, not just its maximum, controls the propagator. Also
\(b_n^{3/2}\le4\sqrt\ell\), so the extra cap cost is absorbed by
the already present second term of (14).

The probabilistic change uses fixed exponential moments for each complete
common-cavity reference before multiplying distinct-root factors. Only
the small singleton/common-cavity differences use the confidence order.
The prefix repair tests endpoints
\(P_{\min(s_j,\sigma_c)}q\) on deterministic level and spatial meshes,
where \(\sigma_c\) is the cavity's own stop. On a later selected common
prefix \(\sigma\), choose the largest \(s_j\le\sigma\).
Actual controls are then defined on the complete tested contour.
The mesh has at most \(n^9\) endpoint tests, and the total logarithmic
union cost is below \(n^{0.65}\), dominated by Gaussian tails
\(4e^{-n^{0.78}}\). This is the precise replacement for the invalid
argument that clamps a fixed grid by a full-network-dependent stop.

Take \(C_{\rm sel}=X^{60}\) and exactly the current source tolerance

\[
\eta=\min\left\{1,Y,16z,
\frac{\lambda}{2C_{\rm sel}n(1+\lambda^{-1/2})
(1+\sqrt\ell)e^{\sqrt\ell}}\right\}.
\tag{15}
\]

On \(S_T\), the selected comparison gives complete-trajectory error
\(\|f_{\rm Taylor}-f_n\|_{\mathcal X}\le Y/n\) under the additional
tail gate

\[
n^7\ge2C_{\rm sel}\lambda^{-1}(1+\lambda^{-1/2}).
\tag{16}
\]

For the exact count, let \(k\) be the dimension of the declared input
span, \(M_n=X^6\sqrt n\), and

\[
K=\max\{0,\lceil\log_2(8M_n/\eta)\rceil\},\qquad
R=2m+k+1+2(2m+p)J(K+1).
\tag{17}
\]

The exact sufficient inventory is

\[
1020(L+1)R^2+36R+10m(k+1)+pk+N+3Nd.
\tag{18}
\]

It includes selected mixers, metrics, initial copies, data, and working
arrays. Dense arrays, coefficient vectors, jets, and partition anchors
are discarded after compilation. Initialization cost and numerical
precision are not bounded; nonprimitive activation-evaluator costs remain
separately charged.

The additional, explicitly separate simplification gate

\[
n\ge[32X^6(1+C_{\rm sel})\lambda^{-3/2}(1+Y^{-1})]^4
\tag{19}
\]

implies \(K+1\le8\ell\). Squaring (17), using (14) and
\(k\le N\), yields the unchanged headline

\[
C(m+p)^2\left[z^4\ell^3+
\lambda^{-2}\ell^2\{\log(e+\ell)\}^2\right]+C(m+p)d.
\tag{20}
\]

Here \(C\) depends only on activation bounds and depth and can be bounded
by a fixed power of \(X\). The inverse-label gate belongs to this
simplified storage display, not to (4) or (16). Without (19), use the exact
\(K\), which exposes its \(\log(1/Y)\) dependence.

Intersect with the lower event (5). Since
\(\ell^{5/2}\le64n^{1/4}\), the additional gate

\[
n\ge[64/(a_\delta\varepsilon)]^4
\tag{21}
\]

suffices for trajectory-ratio error at most \(\varepsilon\). Failure
budgets are split between (4) and (5); no independence is needed.
Thus (3)--(4), (7)--(8), (16), (19), and (21) give a polynomial sufficient
width conditional on the named quantitative source assertions. Its
parameter dependence is polynomial in
\(X,m,d,p,\gamma^{-1},Y^{-1},\delta^{-1},\varepsilon^{-1}\).

For small widths where selection would use all neurons, full selection
\(E_j=\mathbb R^n\), \(I_j=\{1,\ldots,n\}\),
\(M_j=D_j=I/n\) is exact. On the fitting event the invariant
\(c_C=y-f_n\) makes the corrected readout equal to the ordinary readout,
so this is the dense trajectory. It costs dense storage, not (20).
Such a fallback does not make (20) an all-width bound or provide an
initialization success probability below the stated source gates.

## 5. Fixed-dimension Harmonic: two obligations remain

The actual whole-sphere source proof uses the working radius

\[
r_t^{\rm work}=\frac{a}{1024\lambda z^2U\sqrt\ell},
\]

where \(U\) is the explicit sphere-response coefficient. Already its
required \(r_t^{\rm work}\le1/8\) forces

\[
\ell\ge\frac{a^2}{16384U^2\lambda^2z^4}.
\tag{22}
\]

Fixing \(d,L,\beta,z>0\) and letting \(\lambda\downarrow0\) is
admissible when \(Y=\lambda z\). For example, with
\(d=m=L=2\), \(\phi(t)=t+\cos t\), and two unit inputs whose
correlation tends to one, the strictly positive final Gram gap tends to
zero. Formula (22) demands an exponential sufficient width along that
family, even though \(Y^{-1}\) is only proportional to
\(\lambda^{-1}\). This proves a remaining requirement of this proof,
not a singularity or impossibility for the network itself.

Even granting a whole-sphere event on the capped radius
\(\widehat r_t=\min(r_t,R_n)\), with \(R_n\) the second member
of (13), the global time cutoff has

\[
\widehat\alpha_T^{-1}=4T/\widehat r_t
=128\max\{X^{30}z^2\sqrt{d+3}\,\ell^{3/2},
X^{300}\lambda^{-1}\ell(1+\lambda B_n)\sqrt{b_n}\}.
\tag{23}
\]

The unchanged Chebyshev--Harmonic count consequently gives, at fixed
dimension and after polynomial logarithmic simplification gates,

\[
C_d(m+d)^2+C_d\left[
z^4\ell^{3d+2}+\lambda^{-2}\ell^{3d+1}\log(e+\ell)\right].
\tag{24}
\]

To absorb its new term by the old headline through this estimate requires

\[
\frac{\ell}{\log(e+\ell)}\ge c_d\lambda^{-2}z^{-4},
\tag{25}
\]

again incompatible with polynomial width along the fixed-\(d,z\)
family. The additive \((m+d)^2\) term is constant there. The
\(C_d\) notation is for this fixed-dimension diagnosis only; replacing
the headline coefficient \((C/d)^{d+1}\) by an arbitrary hidden
dimension dependence would be a different theorem.

The two unresolved obligations are therefore (i) a quantitative
whole-sphere source event, including angular fields and a valid stopped
frame mesh, and (ii) a source-rank or approximation argument that avoids
the extra term in (24) while preserving the headline. The finite-panel
Taylor source and the dense trajectory lower event supply neither one.
Coefficient-vector counts need not equal actual source rank, so (24)--(25)
are not lower bounds on retained storage. The prior growing-dimension
rank obstruction cannot be reinterpreted as a fixed-dimension theorem.

The original Harmonic construction does permit full-neuron selection when
\(9R\ge n\). That gives the dense-storage fallback described above; it
does not pay the original Harmonic headline throughout the intermediate
width range and therefore does not remove (22) or (25).

## 6. Transfer verdict

| Claim | What the permitted proofs support |
|---|---|
| Legendre deterministic repair | Same closure, optimizer, order and headline; improved \(q^{-3}\) defect control and polynomial structural gates. |
| Taylor deterministic repair | Same runtime, optimizer, panel and headline powers; capped source radius and repaired deterministic prefix mesh; inverse-label gate only for simplified count. |
| Fully polynomial Legendre/Taylor sufficient widths | Follows from the named explicit source lemmas (3)--(4) and the displayed composition; the numerical inherited local-map ledgers are a stated evidence boundary of this transfer check. |
| Original manuscript good events alone | Still leave an unquantified \(N_{\rm event}\); structural polynomial gates do not quantify it. |
| Fixed-dimension Harmonic at the unchanged headline | Open in the permitted study; (22) and (24)--(25) exhibit the remaining proof gates. |
| Polynomial same-time denominator onset | Not supplied by any trajectory lower bound reconstructed here. |

No empirical computation is involved. The direct checks above reconstruct
the error powers, probability composition, prefix geometry, exact counts,
small-width qualifications, and Harmonic non-implication. They do not use a
prior PASS label as a mathematical premise.

## Frozen source hashes

SHA-256 values at this read; file names in the first six rows are relative
to `studies/polynomial_width_compression_20261010/`.

| Source | SHA-256 |
|---|---|
| `DENSE_LEGENDRE_ROUTE.md` | `59b7258a1063aba3a4fe158e726f2abad9e49ac28e18df8eae0d01ab10bb466b` |
| `SOURCE_SCOPE_CHECK.md` | `767d252e9b5083a3f9e8372856ead1c481b62d3fdfa959d67f73c55b8d78dded` |
| `TAYLOR_ROUTE.md` | `d9153aa789ec23d23683b79f9e5e5a6215a4bb884757079ff1b516235504030e` |
| `TAYLOR_PREFIX_REPAIR.md` | `7e9e027676f68fa362cf4016f578ee4ff96cc8cfbaa7ba63d6457417ebcb0c48` |
| `HARMONIC_FIXED_DIMENSION_SCOPE.md` | `15c7f7b09cb69344d64740124ca2bb9e39bdde82b989d49f4391485a23258fda` |
| `FINITE_ANTI_CONCENTRATION.md` | `f723ee3101a145c37ab767ea1c047e4d18b5310ba8a42093b3cbd82183d209fa` |
| `paper/compact.tex` | `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `paper/compact_foundations.tex` | `6a49f8e35bb637416b7e330f7ace06286e482c942302bf57a46c8253a4cffbf0` |
| `paper/compact_legendre.tex` | `862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9` |
| `paper/compact_selected.tex` | `3add2b694f38a4d7dbce90e51dafd375a7e8dee2e06d26b2d5af451bddb44885` |

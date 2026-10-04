# Improving the label, depth and dimension dependence

2026-10-04. Continuation of the same sampling study and explicit-constant
investigation. This note assembles three proof/representation improvements:
rescaling the carrier exponential moment, separating the actual mixer norm
from the source coefficient, and retaining only weighted-degree source
coefficients. The reference network, loss, clock and compressed optimizer
are unchanged. The new source basis is built from initialization alone.

These are internal study results relative to the previously proved source
and insertion interfaces, not promoted manuscript theorems. The component
proofs and exact check records appear below. No experiment was run.

## 1. Statement with explicit constants

Use the same canonical width-n dense model and autonomous corrected-readout
representation as `EXPLICIT_ARCHITECTURE_CONSTANTS.md`. Explicitly, for
v=x/sqrt(d), the reference forward pass is

\[
z^{(1)}=Av,\qquad z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\qquad
h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad
f_n=w^\top h^{(L)}/n.
\]

All hidden widths equal n, L>=2 is fixed, A(0) has independent N(0,1)
entries, the hidden W(0) have independent N(0,1/n) entries, all arrays
are independent, and w(0)=0. Train on m fixed inputs of norm sqrt(d)
with mean squared loss and mobilities (n,1,...,1,n) in physical time.
The data need not be orthogonal. Every activation is real on the real
axis, holomorphic on |Im z|<a, and bounded there by a common B_phi.

Define the activation-only number

\[
B=\max(1,B_\phi),\qquad
\beta=\max\{10,B,4B/a,32B/a^2,16/a\}.
\tag{1}
\]

The Cauchy derivative estimates in (1) are optional. If certified numbers
s,t_phi>=1 bound |phi'_ell| and |phi''_ell| on |Im z|<=a/2, all the
results below also hold with
\[
\beta=\max\{10,B,s,t_\phi,16/a\}.
\tag{1a}
\]
Use the actual real activation/derivative norm in the runtime, bounded by
max(B,s,t_phi), rather than its optional Cauchy overestimate. The proofs
use exactly those first-two-derivative bounds. Higher derivatives remain
bounded by Cauchy's formula using the outer strip and enter only the
inherited local remainder and width-threshold constants.

For tanh one may take a=1, B_phi=2, s=2 and t_phi=4, giving **beta=16**.
Indeed
\[
|\tanh(x+iy)|^2
=\frac{\sinh^2x+\sin^2y}{\sinh^2x+\cos^2y}.
\]
For |y|<1, cos(y)>1/2 and |sin(y)|<1 show the ratio is below four;
the denominator cannot vanish. For |y|<=1/2, cos(2y)>0 makes the
ratio at most one. The identities phi'=1-phi² and
phi''=-2phi(1-phi²) then give the inner-strip derivative bounds 2 and 4.
This avoids further loss from a generic derivative estimate.

The common bounds a,B_phi do not vary with the number of layers. Let
Q^(0)_ab=x_a^T x_b/d, and recursively set
Q^(ell)_ab=E[phi_ell(Z_a)phi_ell(Z_b)] for Z~N(0,Q^(ell-1)). Define

\[
\gamma=\lambda_{\min}(Q^{(L)})>0,\qquad
Y=\left(m^{-1}\sum_a y_a^2\right)^{1/2},\qquad
\ell_n=\log(en).
\]

There is no extra division by m in gamma. The following explicit label
condition suffices for the *complete* source and runtime construction:

\[
Y\le\frac\gamma m\,\beta^{-62L}.
\tag{2}
\]

For any fixed confidence 1-delta, the construction succeeds with probability
at least 1-delta for each sufficiently large width n. It retains at most

\[
\operatorname{size}(C)\le
\beta^{82Ld}\frac{(d+3)^{3d-2}}{(d!)^2}
\left(\frac m\gamma\right)^2\ell_n^{3d+2}
       +10m(d+1)
\tag{3}
\]

real coordinates, counting fixed and moving arrays, data and solve caches.
A simpler slightly looser bound is

\[
\operatorname{size}(C)\le
\beta^{84Ld}(d+3)^d
\left(\frac m\gamma\right)^2\ell_n^{3d+2}
       +10m(d+1).
\tag{4}
\]

The error against the same realized dense initialization obeys

\[
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}
|f_C(t,x)-f_n(t,x)|
\le\beta^{124L}Y\left(\frac m\gamma\right)^{3/2}n^{-1/2}.
\tag{5}
\]

Both flows fit and converge. The time supremum includes the fitted
endpoint and compares equal physical times. Zero labels are covered
separately by the exact stationary zero predictor.

All constants in (2)--(5) are explicit and depend on activation through
(1). The width threshold remains unquantified and can depend on all the
fixed architecture, data, labels and confidence parameters. The statement
is not an event simultaneously over every width, nor a growing-depth or
growing-dimension theorem. Exact-real preprocessing work and precision
are outside the retained-coordinate resource contract, as before.

The compressed optimizer is still the existing autonomous system with
fixed neuron metrics, a moving internal residual and algebraically
corrected readout. It is not ordinary reduced-network gradient flow.
It uses its own current features and residual; no reference trajectory,
original-width arrays, or time-dependent fitted tables remain at runtime.

## 2. What improved

The previous compact version used A_phi=beta^1024 and gave label coefficient
exp(-A_phi^L), error coefficient A_phi^(L²), and leading retained-size
coefficient A_phi^(Ld)(d+3)^(3d). Those remain valid conservative bounds;
they are superseded for this investigation by (2)--(5).

| Dependence | Previous form | Current form |
| --- | --- | --- |
| Label coefficient multiplying gamma/m | exp(-beta^(1024L)) | beta^(-62L) |
| Error coefficient multiplying Y(m/gamma)^(3/2)/sqrt(n) | beta^(1024L²) | beta^(124L) |
| Leading dimension/depth storage coefficient | beta^(1024Ld)(d+3)^(3d) | beta^(84Ld)(d+3)^d |
| Logarithmic width exponent | 3d+2 | 3d+2 |

These are improvements in the proved sufficient estimates, not new lower
bounds or claims of optimality. In particular the storage still has
exponential depth/dimension dependence and the numerical activation powers
remain conservative. The factorial expression (3) is the more informative
count; (4) is useful for comparing its dimension growth with the old bound.

## 3. Proof: the carrier scale removes the double exponential

For this proof put lambda=min(1,gamma/m), S=16Y/lambda. The previous
carrier budget used exp(|k|/S). Its normalized Gaussian tail and singleton
shift could have size beta^(O(L)), so their exponential moments forced
an exponentially large budget, followed by another exponential in the
small-label coefficient.

`LABEL_DEPTH_RESCALING_ROUTE.md` uses instead the proof-only quantity

\[
\frac1n\sum_{\ell<L,i}
\exp\left(\frac\eta S\sup_z|k_{a,i}^{(\ell)}(z)|\right),
\tag{6}
\]

separately for each training sample. The exponent eta is chosen from
explicit depth-dependent gains; the network itself is not clipped or
rescaled. A stopped budget 2 mathcal B gives

\[
\|D^2(nf_a)\|_{p,n}
\le A_H+\frac{S D_H}{\eta}p(2\mathcal B)^{1/p},\qquad
\|D^2(nf_a)\|_{2,n}\le H_2.
\]

Crucially, the Hilbert--Schmidt coefficient H2 and the first term AH are
independent of eta. Summing the response-endpoint expansion without
merging these coefficients gives the singleton shift bound

\[
S\left[D_0+D_1\mathcal B S^4/\eta^3\right]+o(1),
\tag{7}
\]

where D0,D1 are finite depth recurrences. Inside (6), the nonvanishing
cost is eta D0+D1 mathcal B S^4/eta². The fourth power of S matters:
it makes the increased inverse-eta coefficient compatible with a small
activity chosen only polynomially in the layer gains.

The tail split must also be adjusted. At activity separation v, use
carrier threshold

\[
\frac{4S}{\eta}\log\frac{8\sqrt{2\mathcal B}}{\eta v}.
\]

This yields the same eta-independent Gaussian modulus G provided
S²[log(e+mathcal B)+log(1/eta)]/eta<=1. Omitting log(1/eta) would not
justify this conclusion. The explicit choices

\[
\eta=\min\{1,B^{-1},D_0^{-1},(128G)^{-1}\},\qquad
\mathcal B=64e^2L
\]

and the finite smallness minimum in that route control the variational
propagator, all endpoint feedback and asymmetric query traces. The
Gaussian exponential moment is below 4, the shift cost is at most 2,
and the fixed-sample moment ratio is at most 1/16. Fixed-order common
cavity moments remove the stops with the original order of limits.

The route's explicit bookkeeping proves that Y/lambda<=beta^(-32L)
suffices for the source theorem, including its complex-query extension.
The carrier coefficient K<=beta^(5L), coordinate accuracy n^-1 and
the response constants U*,V*<=beta^(30L)sqrt(d+3) are unchanged.
The inverse-eta factors in the complex correction multiply a term tending
to zero at fixed depth, so its Gaussian exponential moment remains
bounded at sufficiently large width. No nonvanishing label or radius
coefficient is moved into the width threshold.

## 4. Proof: propagate the actual mixer norm

`DEPTH_CONSTANT_SEPARATION.md` observes that the previous runtime used
the source coefficient K also as a bound for each mixer, then propagated
K+1 through L layers. Since K<=beta^(5L), this created the artificial
quadratic depth exponent.

The initialized compressed mixers are contractions of the original
matrices between exact source isometries. Their norm is at most 8, so
use tube 9 and leave K only in its actual source-error/carrier roles.
The global hidden displacement bound is at most 1/4 under the revised
smallness conditions, giving a strict margin inside that tube.

Every finite runtime coefficient then has exponent linear in depth. The
complete table in that route gives a sufficient condition
Y/lambda<=beta^(-60L) and all-time error

\[
\beta^{122L}Y\lambda^{-3/2}/\sqrt n.
\tag{8}
\]

It uses the existing exact cancellation of the residual discrepancy's
least-norm feature lift with the raw readout discrepancy. Source errors
are still coordinate errors n^-1; no finer tolerance is used to absorb
the improved error coefficient. The source horizon
T=32 lambda^-1 log(en) controls both exponentially fitting tails.

The revised runtime condition implies the source condition beta^(-32L).
Also gamma<=B², hence lambda>=gamma/(mB²). Thus (2) implies
Y/lambda<=B² beta^(-62L)<=beta^(-60L), and (8) implies (5), since
B³<=beta^(2L) for L>=2. This assembles the full singly exponential
label restriction, rather than stating a source improvement with an
unresolved stronger runtime restriction.

## 5. Proof: retain weighted degree and separate angular radius

For d>=2, `DIMENSION_PREFACTOR_OPTIMIZATION.md` uses the same stopped
source responses with separate radii

\[
c_t=\min\{1/8,a/(512U_*)\},\qquad
c_a=\min\{1/(8d),a/[128(d-1)V_*]\},
\]

and complex widths c_t/sqrt(ell_n), c_a/sqrt(ell_n). Both short time
pieces, including an excursion beyond [0,T], contribute at most a/64
to the preactivation displacement. All angular pieces together contribute
at most a/128. The total 3a/128 leaves the same strict pole margin.
The continued source proof uses this anisotropic rectangle directly;
it is not claimed to be a subset of the old equal-radius rectangle.
For d=1 the angular quantities are omitted and the two time-only query
families are retained.

Under the rescaled budget of Section 3, its short complex correction is
bounded by a fixed multiple of
r_t[1+(S²/eta)log(e+ell_n)], rather than the old eta=1 expression.
Its Gaussian mean and tail scales still tend to zero. All RMS endpoint
coefficients and the asymmetric trace caps are unchanged, so the
explicit inverse radii keep the bounds

\[
c_t^{-1}\le\beta^{32L}(d+3)^{1/2},\qquad
c_a^{-1}\le\beta^{32L}(d+3)^{3/2}.
\tag{9}
\]

After the cosine substitution t=T(1+cos u)/2, let
alpha=c_t lambda/(128 ell_n^(3/2)) and r=c_a/sqrt(ell_n).
The source Fourier coefficients satisfy

\[
|\widehat G(k_0,k')|
\le M_n\exp[-\alpha|k_0|-r\|k'\|_1],\qquad
M_n\le\beta^{4L}\sqrt n.
\]

Retain the weighted-degree set alpha|k0|+r||k'||_1<=H, with the explicit
tail choice H=2log[16M_n 6^d/(epsilon alpha r^(d-1))], epsilon=n^-1.
The sum of omitted coefficients is at most epsilon/16. A disjoint-unit-cube
count, including the angular sign choices and even temporal cosine modes,
gives at most

\[
\frac{2^{d-1}[H+\alpha+(d-1)r]^d}{d!\alpha r^{d-1}}
\]

real source vectors. This supplies the factorial gain. The required nodal
values are computed from finitely many initial derivatives; a temporary
tensor DFT can compute the retained coefficients. Its discarded values
are not runtime storage. Applying identical scalar linear operations to
each initialized image pair preserves exact paired actions, with the
coordinate approximation error controlled for both members separately.

Including all exact initial sources and the constant vector proves

\[
R\le R_0:=\beta^{36Ld}\frac{(d+3)^{3d/2-1}}{d!}
              \lambda^{-1}\ell_n^{3d/2+1}.
\tag{10}
\]

For d=1 take both time-only queries -1,+1; the stated count includes
their factor two. In every dimension R0>=m,d, so the previous complete
runtime inventory is bounded by
1020(L+1)R0²+10m(d+1). Substituting (10) and the capped-gap inequality
lambda^-2<=B^4(m/gamma)^2 proves (3), because
1020(L+1)B^4<=beta^(10Ld).

Finally d!>=(d/e)^d implies

\[
\frac{(d+3)^{3d-2}}{(d!)^2}
\le e^{2d+6}(d+3)^{d-2}
\le\beta^{2Ld}(d+3)^d,
\]

which proves (4). Neither the factorial saving nor the actual pole-radius
dimension factors are hidden in a larger width threshold. As before,
fixed terms inside logarithms and d log log n enter the stated
sufficiently-large-width threshold; the source note lists them explicitly.

## 6. What remains expensive and what is open

The strongest current gains are qualitative: double-exponential label
smallness becomes exponential; the error exponent changes from L² to L;
and the dimension-only storage coefficient drops from roughly d^(3d) to
d^d. The logarithmic exponent 3d+2 and exponential gain raised to Ld remain.

The remaining depth loss comes from products of actual layer-response
bounds, and the remaining dimension loss comes from approximating functions
uniformly on the whole sphere with the present analytic source spaces.
This proof does not show that either loss is necessary for arbitrary
autonomous compression. Reducing them substantially further requires
new control of layer gains or a different whole-query representation,
rather than the three accounting corrections completed here.

These are existence and real-coordinate-count results, not practical
precision or setup-cost bounds. The numeric exponents 62,82,84,124 are
safe envelopes, not optimum constants. Their finite recurrences remain
available in the component files for sharper evaluations.

## 7. Component proofs and reconstruction

| Component | Frozen source SHA-256 |
| --- | --- |
| [Label scale](LABEL_DEPTH_RESCALING_ROUTE.md) | `d06ceea6598bf3f86e0843682c5600365ef01b4b80eaad6544ceec1a9d4ec1f1` |
| [Runtime separation](DEPTH_CONSTANT_SEPARATION.md) | `6e23f2eb95b1979e7be722f76bafb43ee239f83cc5175d58d17a0f9e73fcb17f` |
| [Source representation](DIMENSION_PREFACTOR_OPTIMIZATION.md) | `8e149122bcd83a8f64bceba97a6617f644f10e59fd97456f3cfa0e10273c8f2e` |

The separate reconstruction is
[ARCHITECTURE_OPTIMIZATION_CHECK.md](ARCHITECTURE_OPTIMIZATION_CHECK.md).
The label author also checked the runtime and their precise interface in
[LABEL_RUNTIME_ASSEMBLY_CHECK.md](LABEL_RUNTIME_ASSEMBLY_CHECK.md), frozen
at `b1043c80ec45cc93f8de48dc67e3044fe9d0dd0eaa479ab22f6cf093aa03ade4`.
That additional interface check is not an independent review of its
author's label derivation. The dimension route records its parent-supplied
construction and the timing of cross-route messages; the full dimension
proof is subject to the separate reconstruction. No formal proof assistant,
numerical experiment, independent promotion review, or manuscript edit
is claimed.

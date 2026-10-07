# Independent finite-panel audit

Frozen first-route result, 2026-10-05. This route did not read another route's
output. The deterministic adaptation below gives logarithmic storage exponent
5. Its probabilistic conclusion inherits the existing source and selection
interfaces, including their unquantified stochastic width threshold. Accuracy
relative to an actual random dense-to-dense discrepancy requires a separate
lower-probability statement; an upper certificate alone does not supply it.

## 1. Scope and exact passive-data identity

Let \(v_a=x_a/\sqrt d\), \(1\le a\le p\), be the declared unit inputs.
The first \(m\) inputs train the network, with labels \(y_a\), and the remaining
inputs are passive. The dense model, activations, initialization, depth and
mobilities are exactly those of the study README and the reused source.
Write \(r_a=f_n(v_a)-y_a\) only for \(a\le m\), and

\[
Y=\|y\|_2/\sqrt m,\qquad \lambda=\gamma/m>0,\qquad
\ell_n=\log(en),\qquad S=16Y/\lambda,
\qquad T=32\lambda^{-1}\ell_n.
\]

Here \(\gamma\) is the positive width-independent initialized training
covariance gap used in the inherited theorem. Mere positivity of an empirical
gap that can tend to zero with \(n\) does not give a width-independent constant.

The training equations remain

\[
\dot A=-\frac2m\sum_{a=1}^m r_a\delta_a^{(1)}v_a^T,
\quad
\dot W^{(j)}=-\frac2{mn}\sum_{a=1}^m
r_a\delta_a^{(j)}(h_a^{(j-1)})^T,
\quad
\dot w=-\frac2m\sum_{a=1}^m r_ah_a^{(L)}.
\]

Equivalently, these are sums over the panel with coefficients equal to one
for \(a\le m\) and zero otherwise, retaining the denominator \(m\). No test
label is needed, and no passive residual becomes a state variable. In
particular replacing \(m\) by \(p\) changes the physical clock and is invalid.
Replacing the positive training Gram by the full panel Gram is also invalid:
the panel can contain repeated inputs or more points than its feature rank.

For \(Y>0\), retain the full existing label allowance

\[
\frac Y\lambda\le
\min\left\{\frac1{8H_d\sqrt{F_d}},
\frac1{16H_c\sqrt{F_c}},\frac{S_*^{\rm src}}{16}\right\}.
\tag{1}
\]

The constants in (1) are exactly the dense fitting, compressed fitting and
source recurrences supplied in the authorized input. The convenient smaller
condition \(Y\le\lambda\beta^{-30L}\) must not silently replace (1).
Zero labels give the stationary zero predictor separately.

## 2. The time-only approximation lemma

The inherited source event gives holomorphy of each coordinate of all four
families

\[
h^{(j)}(t,v),\quad W_0^{(j)}h^{(j-1)}(t,v),\quad
\delta^{(j)}(t,v),\quad
(W_0^{(j+1)})^T\delta^{(j+1)}(t,v)
\tag{2}
\]

on a neighborhood of the closed time rectangle around \([0,T]\), with
half-width

\[
r_t=\frac{c_t}{\sqrt{\ell_n}},\qquad
c_t=\frac{a_{\rm strip}}{64YSU}.
\tag{3}
\]

The coefficient \(U\) is the actual source recurrence, including its depth,
activation, dimension and label dependence. Its value is independent of \(n\)
when the problem parameters are fixed. A coordinate bound is

\[
M_n=M_0\sqrt n,\qquad
M_0=10\max(H_{\max},\max_j\tau_j).
\tag{4}
\]

The source supplies (2)--(4) uniformly over the sphere, so restricting them
to the finite panel introduces no new probability argument or panel Gram
condition. It preserves unbounded activation values: (4) follows from RMS
bounds and linear growth, not from a bound on \(\phi\).

Here is an explicit finite-dimensional replacement for the spatial harmonic
count. Put

\[
A_t=\frac{128}{c_t\lambda}
=2^{17}\frac U{a_{\rm strip}}\left(\frac Y\lambda\right)^2,
\qquad
\alpha_t=\frac{r_t}{4T}=\frac1{A_t\ell_n^{3/2}},
\qquad \epsilon=n^{-1}.
\tag{5}
\]

Assume \(\alpha_t\le1\). For a scalar source coordinate \(g\), the even
periodic function

\[
G(u)=g\big(T(1+\cos u)/2\big)
\]

is holomorphic for \(|\operatorname{Im}u|\le\alpha_t\). Indeed its imaginary
time displacement is at most \(T\sinh(\alpha_t)/2\le T\alpha_t\), and its
real overshoot is at most \(T(\cosh\alpha_t-1)/2\le T\alpha_t\); both are
at most \(r_t/4\). Fourier contour translation gives

\[
|\widehat G_k|\le M_ne^{-\alpha_t|k|}.
\]

The degree-\(K\) cosine truncation therefore has coordinate error at most

\[
\frac{2M_ne^{-\alpha_t(K+1)}}{1-e^{-\alpha_t}}
\le\frac{4M_n}{\alpha_t}e^{-\alpha_t(K+1)}.
\]

Choose

\[
K=\left\lceil\alpha_t^{-1}
\log\frac{16M_n}{\alpha_t\epsilon}\right\rceil.
\tag{6}
\]

Its exact truncation error is at most \(\epsilon/4\). Finite coefficient
approximation can consume a further \(\epsilon/4\), leaving slack within
the source tolerance \(\epsilon\). Identical quadratures and scalar
operations are used for a source and its initialized image, preserving the
image identity exactly, as in the inherited construction.

Impose the explicit counting gate

\[
\log(16M_0A_t)\le\ell_n.
\tag{7}
\]

Since \(\tfrac32\log\ell_n\le\ell_n\) for \(\ell_n\ge1\), the logarithm in
(6) is at most \(4\ell_n\). The gate \(\alpha_t\le1\) also gives

\[
K+1\le4A_t\ell_n^{5/2}+2\le6A_t\ell_n^{5/2}.
\tag{8}
\]

Thus each vector source at one declared input contributes at most

\[
N_t=6A_t\ell_n^{5/2}
\]

coefficient vectors. The source approximation is one-dimensional in time;
the \(p\) inputs are a discrete list, not \(p\) polynomial variables.

## 3. Source rank, runtime and full retained storage

Retain all four families (2) for all \(p\) inputs. This conservative choice
includes passive backward sources and their initialized adjoint images.
Keep the original exact additions: initialized training features and their
forward images, first-weight columns, and the constant. The source rank at
each layer is then at most

\[
R\le B_p\ell_n^{5/2}+2m+d+1,\qquad
B_p=24pA_t
=3\cdot2^{20}p\frac U{a_{\rm strip}}
\left(\frac Y\lambda\right)^2.
\tag{9}
\]

Applying the inherited selection interface gives at most \(9R\) selected
coordinates per layer. This is conditional on the interface applying to the
new finite paired coefficient spaces; the interface is stated in the input
as a finite source-space construction, not as a restriction to spherical
harmonics. The present route has not independently re-proved that older
selection theorem.

The autonomous runtime is unchanged. If \(V_C\) has the \(m\) training
feature columns divided by \(\sqrt m\), and \(r_C\) is its training
residual, its effective readout is

\[
\widehat w_C=w_C+V_C(V_C^*V_C)^{-1}
\left[(y+r_C)/\sqrt m-V_C^*w_C\right].
\tag{10}
\]

A star is the adjoint for the fixed selected metrics. Formula (10) uses only
training columns. Every panel prediction is the actual pairing

\[
f_C(v_a)=\widehat w_C^TM_Lh_C^{(L)}(v_a).
\]

No special passive output equation or fictitious zero-weight fitting
constraint is imposed. Gates are not self-adjoint under a nondiagonal
metric. Consequently a passive evolution equation obtained by pretending
the specified optimizer is the gradient of this corrected predictor would
require a separate proof; it is unnecessary here.

The input's all-retained inventory is at most

\[
1020(L+1)R^2+10m(d+1).
\]

Add stored passive inputs, all \(p\) output values if desired, and a
sequential live forward workspace. The latter needs at most \(9LR\)
coordinates beyond the existing training caches. A safe rounded inventory,
including a finite model/evaluation program of length \(P_{\rm prog}\), is

\[
\operatorname{size}(C)
\le2048(L+1)R^2+16p(d+1)+P_{\rm prog}.
\tag{11}
\]

For example, raw passive data plus panel outputs use at most

\[
(p-m)d+p
\]

additional scalar slots. Since \(R\ge1\), the workspace increment is
already covered by the rounding in (11). One can overwrite the query
workspace between inputs; it is still counted while live.

Equations (9)--(11), \((a+b)^2\le2a^2+2b^2\), and \(\ell_n\ge1\) give

\[
\operatorname{size}(C)\le C_{\rm panel}\ell_n^5,
\tag{12}
\]

with the entire displayed prefactor

\[
C_{\rm panel}=
4096(L+1)\left[B_p^2+(2m+d+1)^2\right]
+16p(d+1)+P_{\rm prog}.
\tag{13}
\]

The exponent 5 is absolute. It does not depend on activation, depth,
dimension, training sample count, or panel size. Their dependence has not
disappeared: it is explicit in (13), through the source recurrence \(U\),
the gap, and the label allowance. In particular, (12) is a fixed-parameter
statement. If \(p=p(n)\), its coefficient has a \(p(n)^2\) term and its data
storage is at least order \(p(n)d\) for a directly retained arbitrary panel.
If \(L,d,m\), the gap, or the activation bounds vary with \(n\), their
coefficients and width gates must likewise be substituted before describing
the resulting width dependence.

The construction uses finite initial-jet continuation and coefficient
quadrature from the initialized network. Original-width coefficient
vectors, quadratures, jets and dense arrays are discarded after the fixed
selected matrices and metrics are formed. Runtime coefficients do not read
a future dense solution, and no time table is retained. Restarting uses the
current compressed arrays and its own \(m\)-dimensional residual. Setup work
is not asserted to be small. This is retained scalar storage, as in the
reused proof, not a finite-bit complexity theorem. A finite activation
evaluation description is needed to assign \(P_{\rm prog}\); strip
regularity alone does not specify a computable finite program for an
arbitrary activation. An uncharged arbitrary function oracle would exceed
the stated memory contract.

## 4. Why the deterministic comparison survives

The comparison in `COMPACT_FULL_LABEL_RANGE.md` uses training backward
sources to compare hidden update directions and the normalized training
Gram. Its panel output step uses forward sources, paired initialized
forward actions, the selected readout pairing defect, and the error in the
effective readout. All those sources are present in (2). The proof does not
differentiate an approximation error and does not need a coordinate maximum
of a passive carrier. The source maximum multiplying a changed gate is a
training-carrier maximum, exactly as in the original comparison.

Since coordinate source accuracy, paired image identities, selected-metric
isometry, exact training initialization and the runtime equations are
unchanged, every deterministic comparison inequality applies with the
supremum over queries replaced by the maximum over the panel. In particular
the full label interval (1) retains its existing all-time error bound

\[
\max_{a\le p}\sup_{t\in[0,\infty]}
|f_C(t,v_a)-f_n(t,v_a)|
\le E_0\frac{(1+\sqrt{\ell_n})e^{32\sqrt{\ell_n}}}{n},
\tag{14}
\]

where the inherited theorem gives

\[
E_0=C_0\beta^{42L}\frac Y\lambda
\max(1,\lambda^{-1/2})
\]

for a universal numerical \(C_0\). The input does not give that universal
constant a numerical value. This is not a gap in the logarithmic storage
exponent, but it matters for fully numerical tolerances.

For an entirely numerical alternative, source Section 13 gives the
explicit recurrence coefficients \(C_{\rm out},a_0,b_0,\mathcal K,B_f\)
and the valid conservative bound

\[
\max_{a\le p}\sup_{t\in[0,\infty]}|f_C-f_n|
\le\frac{C_{\rm out}}n e^{a_0+b_0\sqrt{\ell_n}}
+\frac Y\lambda(16\mathcal K+4B_f)e^{-8\ell_n}.
\tag{15}
\]

No smaller label range is needed for (15). The large parameter-dependent
comparison coefficient in it can be retained explicitly in the width
threshold instead of silently claiming a sharp prefactor.

The endpoint in (14)--(15) is justified by independent exponential fitting
tails of both actual autonomous systems. For \(t\ge T\), compare each
solution to its own value at \(T\), and integrate its remaining speed.
The source approximation is needed only through \(T\). There is no frozen
post-\(T\) predictor or exchange of compact-time and infinite-time limits.

## 5. Explicit width qualifications and variability comparison

The construction retains the inherited stochastic source/fitting event.
Its success probability tends to one at each fixed problem, but its
confidence-dependent threshold is unquantified in these inputs. Required
deterministic gates include

\[
n^{-1}\le\min(1,Y,S),\qquad
\sqrt{\ell_n}\ge c_t\max\left\{8,\lambda,
\frac{4\mathcal K}{\log2},32YSD_W\right\},
\tag{16}
\]

where \(D_W\) and \(\mathcal K\) are source Section 8's explicit
recurrences. Retain the source moment gate

\[
\ell_n\ge\max(e^2,2\mathcal B)
\]

and any remaining gates of the inherited source event. Add

\[
\ell_n\ge A_t^{-2/3},\qquad
\ell_n\ge\log(16M_0A_t)
\tag{17}
\]

for the elementary time count. The old spherical harmonic counting gates
are unnecessary for this time-only approximation. One may keep them as
redundant sufficient restrictions when reusing the original complete event;
they do not change the exponent in (12). In particular \(c_t\) grows as
labels shrink, so (16) is not uniform as \(Y\downarrow0\).

For any prescribed positive root-width tolerance coefficient \(P\), the
fully explicit additional gate supplied by source (53) is

\[
n\ge\left\lceil\max\left\{
e^{\max(8a_0,64b_0^2,2)},
\left(\frac{2e^{1/4}C_{\rm out}}P\right)^4,
\left(\frac{2Y(16\mathcal K+4B_f)}{\lambda P}\right)^{2/15}
\right\}\right\rceil.
\tag{18}
\]

It makes (15) at most \(P/\sqrt n\). Equation (18) must be intersected
with (16)--(17) and the unquantified stochastic threshold. Thus the
subpolynomial exponential in (14) need not be mistaken for a settled
numerical accuracy statement.

Let

\[
D_n=\max_{a\le p}\sup_{t\in[0,\infty]}
|f_n(t,v_a)-f_n'(t,v_a)|
\]

be the actual discrepancy of two independent dense initializations.
An upper certificate \(D_n\le U_n\) does not imply that error at most

\[
\theta U_n
\]

is at most \(\theta D_n\). If a separate valid lower result gives

\[
\Pr\{D_n\ge b/\sqrt n\}\ge1-\delta_{\rm low}
\]

with \(b>0\), then (18) with \(P=\theta b\), intersected with the
compressor-success event, yields error at most \(\theta D_n\) with
probability at least \(1-\delta_{\rm low}-\delta_{\rm src}\). No independence
between these two events is needed for that union bound. This route has
not read or established a dense-discrepancy lower theorem. Without one,
the actual-discrepancy comparison remains conditional. At a fixed finite
width, a uniform deterministic positive discrepancy lower bound is in
general unavailable because two Gaussian initializations can be
arbitrarily close on a bounded finite-dimensional initialization region.

## 6. Audit verdict and provenance

The dimension-dependent logarithmic exponent in the compact source count
comes from requiring a continuum of queries. Replacing that observable
contract by a predeclared finite panel removes that factor. Time degree
is \(O(\ell_n^{5/2})\); dense selected matrices square it to exponent 5.
Depth enters the number of matrices and recurrence constants, not the
logarithmic exponent. No feature freezing, linearization, orthogonal-data
assumption, bounded-value activation assumption, or compact-time
substitution is used.

The remaining major dependencies are the inherited finite source-selection
interface and stochastic source theorem, a finite counted activation
evaluator if a computational representation is claimed, and a separate
lower theorem if the tolerance means actual random dense variability.
These are qualifications of the composed theorem, not no-go results for
finite-panel compression.

Completely read scientific inputs: the new study README, `docs/notation.qmd`,
and the following five authorized files in
`studies/integrated_general_compression_20261004/`:

- `UNBOUNDED_COMPRESSOR_BRIDGE.md` (1,281 lines);
- `EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md` (232 lines);
- `COMPACT_SOURCE_ENERGY.md` (596 lines);
- `COMPACT_POLYNOMIAL_COMPARISON.md` (599 lines);
- `COMPACT_FULL_LABEL_RANGE.md` (898 lines).

Required rigorous-math and conjecture-investigation skills, the adversarial
audit and research-contract references, current shared instructions, and
workflow Part 1 were read. The custom canonical-notation skill remained
permission denied; the explicit user contract and maintained notation were
applied. No older study, old book, other route, external source, experiment,
Git mutation, or maintained-file edit was used. This report is the sole
owned output and is a scoped theoretical audit, not a promotion review.

Input SHA-256 hashes, in the above file order after the notation contract:

```text
notation: 78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023
source: e018f0291b4456913a6541d5db7d90a678c4564928edcd5f47dd8c5326336f5d
runtime: d1ce6c1d7ab5bac41a965d92d356bd705f45683d437bfbcc85ac20fd439c4e92
energy: 65a99b7f4249e83c5ad9c97fdc81193c5a49ad5eef04fe7e0582d2e376936c89
comparison: 893abe1447627438f3530a8b5a83b8214eb680beca7513bd99fee360f7fe336f
full labels: 90aeb1a3aba585aab27f0b46cb23ad7391614abbc64272dccf16ab25fb80b071
```

## 7. Post-freeze audit of the localized time radius

The independent Sections 1--6 were frozen before the supervisor supplied
this challenge, at SHA-256
fc824e4d9dfb2fbb6d5123a17d246b756b0441750d717de2d5a698dae3d9542e.
Afterward the supervisor explicitly authorized the additional source
GENERAL_TRAJECTORY_LOWER_BRIDGE.md; all 545 lines were read. No other
route output was read. This addendum strengthens the coefficient in (13)
without changing its absolute exponent.

That source localizes the query argument to any fixed finite collection
of real inputs, replacing the frame-mesh Gaussian constant by 64. Its
response coefficient is \(U_{\rm fin}(S)\), and it proves the time rectangle
with

\[
r_t=\frac{\chi(S)}{\lambda\sqrt{\ell_n}},\qquad
\chi(S)=\min\left\{1,\frac{a_{\rm strip}}
 {4S^2U_{\rm fin}(S)}\right\}.
\tag{19}
\]

The full source cap gives

\[
\chi(S)\ge\chi_{\rm act}
=\min\left\{1,\frac{a_{\rm strip}}
 {4(S_*^{\rm src})^2U_{\rm fin}(S_*^{\rm src})}\right\}>0.
\tag{20}
\]

Here \(\chi_{\rm act}\) depends only on activation and depth. Under the
separate simple cap \(Y/\lambda\le\beta^{-30L}\), that source proves
\(\chi(S)=1\). The larger label allowance is preserved by (19)--(20).

Although the localized note's displayed final observable is a predictor
difference, its event suffices for all four families in (2). The training
weight solution is holomorphic; every passive query preactivation stays
inside the safe activation strip. Passive backward fields are finite
compositions and products of those gates, the readout, and hidden
transposes. They are therefore holomorphic on the same rectangle.
Its complex operator and readout bounds give

\[
\frac{\|h^{(j)}(t,v_a)\|_2}{\sqrt n}\le H_j,\qquad
\frac{\|\delta^{(j)}(t,v_a)\|_2}{\sqrt n}\le S\tau_j.
\]

Applying initialized matrices of norm at most eight bounds the two paired
image families. Thus (4), all four source approximation families, paired
selection, and the unchanged runtime comparison follow. No new passive
coordinate maximum or trained passive moment budget is being inferred.

Substitute \(c_t=\chi/\lambda\) in the time lemma. Then

\[
A_t=\frac{128}{\chi},\qquad
\alpha_t=\frac{\chi}{128\ell_n^{3/2}},\qquad
B_p=\frac{3072p}{\chi}.
\tag{21}
\]

The gate \(\alpha_t\le1\) is automatic; the remaining counting gate can be
taken as

\[
\ell_n\ge\log(2048M_0/\chi).
\]

Consequently (12)--(13) hold with the improved full prefactor

\[
C_{\rm panel}
=4096(L+1)\left[
\left(\frac{3072p}{\chi}\right)^2+(2m+d+1)^2\right]
+16p(d+1)+P_{\rm prog}.
\tag{22}
\]

One may replace \(\chi\) by \(\chi_{\rm act}\) for a bound uniform over
the full label allowance. Its leading coefficient then has no dimension,
sample/gap or label factor. Under the simple cap, it is purely numerical
apart from \(p^2(L+1)\). The padding, label admissibility and width gates
still depend on the original problem. The looser factor 4096 explicitly
allows a live sequential query workspace; the inherited factor 2040 can
be retained if that workspace is verified to lie in its existing inventory.

The additional source also supplies a conditional route to actual
variability. If a declared input \(v_0\) has positive initialized onset
variance \(\sigma(v_0,y)^2\), its proof witnesses the discrepancy at that
single query. Thus its lower bound applies to the panel maximum itself,
not just to the whole-sphere maximum:

\[
D_n\ge \frac{P}{\sqrt n\,\ell_n^{5/2}},
\qquad P=\frac{u\chi(S)\sigma(v_0,y)}{64\lambda}>0,
\]

with the source's stated asymptotic probability
\(2[1-\Phi(u)]\). The variance condition, CLT and probability threshold
remain inherited inputs; this addendum does not establish that a suitable
query is in every allowed panel.

For a desired fraction \(\theta>0\), use (15) with
\(C_{\rm tail}=(Y/\lambda)(16\mathcal K+4B_f)\). The explicit sufficient
deterministic conditions are

\[
\ell_n\ge\max(8a_0,64b_0^2,2),\qquad
n^{1/4}\ge
\frac{2e^{1/4}C_{\rm out}}{\theta P}\ell_n^{5/2},\qquad
n^{15/2}\ge
\frac{2C_{\rm tail}}{\theta P}\ell_n^{5/2}.
\tag{23}
\]

They make the compressor error at most
\(\theta P/(\sqrt n\,\ell_n^{5/2})\), while keeping source tolerance
\(1/n\) and the storage exponent 5. Intersect with the lower event and
the construction events to obtain error at most \(\theta D_n\). A
root-width certificate alone would be insufficient for this weaker
logarithmically reduced lower scale.

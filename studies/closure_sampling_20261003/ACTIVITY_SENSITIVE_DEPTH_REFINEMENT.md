# What improves when activation gains and label activity are kept separate

2026-10-04. Coordinator synthesis of the present continuation. This file
supersedes the tanh numerical envelope in INPUT_DIMENSION_REFINEMENT.md;
that file's general-activation and query-folding statements remain intact.
No manuscript or maintained-book promotion is made. Component proofs and
their explicit reconstruction status are recorded below. No training
experiment was run; the only numerical work evaluates displayed finite
recurrences.

The main improvement applies to ordinary tanh and full-rank data. It
substantially reduces, but does not remove at every depth, the joint
depth--dimension exponent. A separate small-slope nonlinear subclass
removes that exponent. Neither statement supplies practical constants
for the full earlier class, or an impossibility theorem for better ones.

## 1. Model and comparison that stay fixed

There are m fixed inputs x_a with ||x_a||=sqrt(d), arbitrary fixed signed
labels y_a, and L>=2 hidden layers, each of width n. Put v=x/sqrt(d).
The canonical dense reference is

\[
z^{(1)}=Av,\quad z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\quad
h^{(\ell)}=\phi_\ell(z^{(\ell)}),\quad f_n=w^\top h^{(L)}/n.
\]

Initialization is independent Gaussian A_ij~N(0,1),
W_ij^(ell)~N(0,1/n), with w=0. Training is mean squared loss with
mobilities (n,1,...,1,n), exactly as in the component proofs. Define
Q^(0)_ab=v_a^T v_b and Q^(ell)_ab=E[phi_ell(Z_a)phi_ell(Z_b)],
where Z has covariance Q^(ell-1). The data quantities are

\[
\gamma=\lambda_{\min}(Q^{(L)})>0,\qquad
Y=\left(m^{-1}\sum_a y_a^2\right)^{1/2}.
\]

The compressor is the existing initialization-only, weighted-neuron
construction with the autonomous corrected-readout optimizer, not an
ordinary narrower iid initialization or an unmodified q-closure. It
evolves all retained hidden parameters using its own state and residual.
All moving coordinates, fixed small matrices, metrics, retained data and
work arrays are counted. No original-width matrix or trained-path table
is retained. Preprocessing work and real-number precision remain outside
the coordinate-count claim.

Every probabilistic statement is at fixed confidence for each sufficiently
large n, with data and architecture fixed. Constants are independent of
n and physical time. The comparison is with the same realized dense run,
at the same time, uniformly over the entire query sphere, including both
fitted endpoints. The stochastic width threshold remains unquantified.

## 2. Ordinary tanh: a much smaller full-rank storage coefficient

Set phi_ell=tanh. One may retain the old label assumption

\[
                    Y\le \frac\gamma m\,16^{-62L}.
\tag{1}
\]

The sharper finite label cap is equation (3) of
[RUNTIME_SMALL_ACTIVITY_CONSTANT_ROUTE.md](RUNTIME_SMALL_ACTIVITY_CONSTANT_ROUTE.md):
the minimum of the explicitly evaluated source, fitting, angular and time
caps. Its source recurrences are in
[ACTIVATION_CONSTANTS_REFINEMENT_ROUTE.md](ACTIVATION_CONSTANTS_REFINEMENT_ROUTE.md).
These are evaluated recurrences, not unspecified activation constants.
The older cap (1) implies the new one, so the result below adds no
label restriction to the previous tanh theorem.

For d>=2, define the dimension/depth coefficient

\[
 a_{L,d}=\frac{4096\,9^d}{d!}
 \left[\frac{4096}{5}\left(\frac{64}{15}\right)^{L-2}+32\right]^{d-1}
 (d+3)^{d/2}.
\tag{2}
\]

The source rank is bounded by

\[
R\le a_{L,d}\frac m\gamma\log^{3d/2+1}(en)+2m+d+1,
\]

and the total retained size by

\[
\begin{split}
\operatorname{size}(C)\le{}&
2040(L+1)a_{L,d}^2\left(\frac m\gamma\right)^2\log^{3d+2}(en)\\
&+2040(L+1)(2m+d+1)^2+10m(d+1).
\end{split}
\tag{3}
\]

The exact radius expression in the component proof, equation (20), is
slightly smaller than (2). For d=1 use its separate two-query time count;
there is no query-angle exponent. No input-span folding is used in (2)--(3).

In place of the old depth factor 16^(82Ld), the depth-dependent factor
in the leading coefficient now grows as

\[
                     (64/15)^{2(L-2)(d-1)}.
\tag{4}
\]

This describes the depth growth of the fully explicit (2), not an equality
between isolated coefficients: its bracket also contains the displayed
additive 32 and numerical factor 4096/5. In particular, at two hidden
layers the joint depth--dimension growth vanishes from that bracket.
The numerical-base-to-dimension powers remain. At higher depth, (4)
still multiplies depth and dimension; no complete removal is claimed.

The error retains the form

\[
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|f_C(t,x)-f_n(t,x)|
 \le E_L\,Y\left(\frac m\gamma\right)^{3/2}\frac1{\sqrt n},
\tag{5}
\]

Here E_L is the explicit finite expression (20)--(22) in the new runtime
proof, or its sharper (24) when the elementary test (23) holds. Rounded
diagnostics from those formulas are

| Hidden depth L | Sufficient coefficient in Y <= coefficient * gamma/m | E_L |
| ---: | ---: | ---: |
| 2 | 2.857681e-7 | 2.714204e5 |
| 3 | 1.138046e-9 | 2.043381e6 |
| 5 | 3.567411e-14 | 1.152144e8 |

These rounded numbers are illustrations; the theorem uses the exact
recurrences. The following simpler depth-two pair has also been certified
by exact rational inequalities:

\[
\boxed{Y\le2.8\,10^{-7}\frac\gamma m},\qquad
\boxed{\sup_{t\in[0,\infty],\,\|x\|=\sqrt d}|f_C-f_n|
 \le2.8\,10^5Y(m/\gamma)^{3/2}/\sqrt n.}
\tag{5a}
\]

At the largest permitted label scale, its complete error prefactor is at
most 0.0784 sqrt(m/gamma). This is an absolute-error statement at that
small label scale; it does not make the relative error coefficient or
the label restriction mild. Zero labels give identically zero predictions.

At L=2 the old coefficients were approximately 10^-149 and 10^299.
The first refinement in the source proof gave 4.756e-16 and 1.644e24;
the later runtime reconstruction supersedes that intermediate table.
The final improvement is large, but the label allowance remains small
and the constants remain conservative. At L=2,d=100, the base-ten logarithm of the leading
storage coefficient drops from about 19632.9 to 664.7. A coefficient
of order 10^665 is still not reasonable storage in a practical sense.

## 3. Why the large savings are legitimate

The previous common envelope beta combined several unrelated quantities.
For tanh the actual certified bounds are

\[
|\tanh z|\le1\quad (|\Im z|<1/2),\qquad
|\tanh' z|\le16/15,\quad |\tanh''z|\le1
                    \quad (|\Im z|\le1/4).
\]

The real value, slope and curvature bounds are all at most one.
An elementary Gaussian net estimate certifies initialized mixer norm
7/2, with real and complex tubes 15/4 and 4. Thus the actual complex
propagation gain is 64/15, not a large power of an activation envelope.

More significantly, let S=16Ym/gamma be the existing contour activity
allowance. An adaptive query correction has one factor S from the
integral of residuals and another from the training carrier. Its bound
is S^2 times the response coefficient. The previous proof discarded
this square by using S<=1 before estimating the query radius. The new
proof keeps it until the existing small-label assumption absorbs it.
The time displacement similarly retains its factor YS. Consequently,
only the Gaussian forward derivative bound, rather than the larger
adaptive-response constant, determines the depth dependence of query
resolution.

Finally, every constructed source has coordinate error epsilon=n^-1
with multiplier one. That approximation multiplier need not equal the
larger coefficient controlling the maximum backward signal. Separating
them removes repeated artificial powers in the deterministic comparison.
The source accuracy, optimizer and target network are unchanged.

The final runtime improvement uses the same principle in the comparison
itself. The coefficient of the accumulated readout error is exactly one;
changed hidden-state feedback retains its label factors. Source defects
stay additive instead of contributing to exponential amplification. The
residual damping pays the combined hidden/readout error once, and the
endpoint speed estimate also keeps its squared activity factor. At depth
two, the comparison exponential consequently has exponent below 0.026.
The main remaining numerical error coefficient comes from finite source
forcing and query reconstruction, rather than a huge amplification factor.

## 4. A nonlinear subclass with no additional exponential Ld factor

The separate [contractive route](CONTRACTIVE_DEPTH_CONSTANT_ROUTE.md)
uses phi_ell(z)=c tanh(z), 0<c<=1/40, at every layer. The actual complex
slope bound is 2c and the source propagation factor 10(2c)<=1/2;
the corrected-runtime metric also has propagation factor below one.
The geometric sums can therefore be bounded directly rather than
raised to depth. With the correction below, its sufficient bounds are

\[
Y\le\frac{\gamma}{m}\frac{2^{-90}}L,\qquad
\sup_{t,x}|f_C-f_n|\le2^{150}L\,Y(m/\gamma)^{3/2}/\sqrt n,
\]

\[
\begin{split}
\operatorname{size}(C)\le{}&2040(L+1)2^{56d}
       \frac{(d+3)^d}{(d!)^2}(m/\gamma)^2\log^{3d+2}(en)\\
 &+2040(L+1)(2m+d+1)^2+10m(d+1).
\end{split}
\tag{6}
\]

There is no C^(Ld) factor in (6). The numerical powers of two remain
conservative. This is a different activation subclass, not a claim
that ordinary tanh is contractive under the same operator argument.

**Correction to the frozen contractive candidate.** Its equation (13)
must define the external-insertion curvature coefficient as

\[
E=\max_{1\le p\le L}
 t\sum_{\ell=p}^L q_{\rm src}^{2(\ell-p)}K_\ell,
\qquad q_{\rm src}=10s\le1/2,
\]

or replace it by the valid upper bound t sum_ell K_ell<=0.4. The
candidate's earlier expression selected p=1, a simplification that
requires q_src>=1 and is invalid in this subclass. The corrected bound
is still 0.4, exactly the bound used in every numerical estimate;
therefore all displayed label, radius, size and error conclusions survive.
The reconstruction report records this correction and checks the other
uses of a subunit gain. The frozen candidate is preserved, not silently
rewritten.

There is a real depth cost left in the data gap. For this subclass,
|c tanh x|<=c|x| gives Q^(ell)_aa<=c^(2ell), so

\[
                         \gamma\le c^{2L}.
\]

Thus (6) is not a bound polynomial in depth at a fixed absolute label
scale. It removes the extra structural Ld exponent while keeping the
remaining inverse-gap dependence explicit. It does not make deep
contractive networks uniformly well conditioned.

## 5. General tanh and broader activations: claim boundaries

The root's [initialization calculation](NONEXPANSIVE_INITIAL_QUERY_ROUTE.md)
proves that, for real |phi'|<=1 and bounded |phi''|, normalized RMS
query derivatives at Gaussian initialization are at most 1+epsilon,
uniformly over the entire real input ball and all layers, with probability
tending to one at fixed d,L. Their coordinate maxima are likewise
O(sqrt(d log n)) with no exponential depth coefficient. Thus the
remaining deterministic layer-product bound is not already necessary
for those initial real query derivatives.

Its extension through training is open here. Differentiating a query
derivative J=D_v z along the actual trajectory produces the mixed
quantity ||R_a J||_(2,n), where R_a is the residual-free forward
response. Separate RMS bounds do not control that product, and the
Gaussian matrix is reused during training. This is a concrete remaining
adaptive-response estimate, not a theorem that removing (4) is impossible.

[ACTIVATION_CLASS_EXTENSION_ROUTE.md](ACTIVATION_CLASS_EXTENSION_ROUTE.md)
and its complete internal reconstruction establish a qualitative extension.
Bounded activation values can be replaced by

\[
\phi_\ell\text{ holomorphic on }|\Im z|<a,\qquad
\max_\ell|\phi_\ell(0)|<\infty,\qquad
\sup_{\ell,|\Im z|<a}|\phi_\ell'(z)|<\infty,
\]

with real values on the real axis. This includes identity and the
nonaffine unbounded activations z+epsilon tanh(z), epsilon!=0. The
positive initialized Gram gap and sufficiently small fixed labels remain
required. A joint complex preactivation/carrier budget replaces the old
use of bounded features and bounded readout coordinates.

This extension preserves all-time whole-sphere C/sqrt(n) error, but its
currently checked total storage is C log^(2[d(L+5)+1])(en)+Cm(d+1),
with fixed-data constants, rather than the sharper tanh formula (3).
Its explicit small-label coefficient and numerical error constant have
not been optimized. The two results must not be merged by silently
substituting derivative bounds into the old beta expression.

The separate affine construction has C/n error and O(log^4 n) total
storage at fixed data. It uses constant-preserving orthogonal source
projection, which commutes exactly with affine activation. Identity's
Gram is precisely the input Gram and hence requires linearly independent
training inputs, with m<=d. General affine activations require m<=d+1
under the gap hypothesis. This affine boundary case is not evidence that
the same projection commutes with nonlinear activations.

## 6. Evidence and checks

The complete tanh candidate is frozen at SHA-256
407f0b1079c7f65dd09960bc45c78a4f266c30054585c9aa9df8b7ab61859660.
The later runtime candidate is frozen at
061d46972a7b026bd6b6b5176fc411214e82bd1e9d9e18ec5bd8e119fedbeaa2.
The complete contractive candidate is frozen at
88f9a621c918bf8b9dbf210bd79085b8650a3533ad08655638afdd03a92787ac;
the explicit correction in Section 4 takes precedence over its E formula.
Root read both complete candidates and their relevant source/runtime
interfaces, independently checked the activity-factor and radius algebra,
and reran both embedded tanh evaluators. The reported tables were
reproduced. The elementary initialization note is a root derivation and
self-check, not an independent review.

The later runtime proof was read completely and reconstructed in
[RUNTIME_SMALL_ACTIVITY_CONSTANT_CHECK.md](RUNTIME_SMALL_ACTIVITY_CONSTANT_CHECK.md).
Its exact rational depth-two certificate and independently evaluated
finite recurrences are reproducible with
[check_small_activity_constants.py](check_small_activity_constants.py).
The coordinator participated in the proof search, so this is a
collaborative internal reconstruction, not an independent promotion review.

The separate scoped reconstructions are
[ACTIVATION_CONSTANTS_REFINEMENT_CHECK.md](ACTIVATION_CONSTANTS_REFINEMENT_CHECK.md),
[CONTRACTIVE_DEPTH_CONSTANT_CHECK.md](CONTRACTIVE_DEPTH_CONSTANT_CHECK.md),
and [ACTIVATION_CLASS_EXTENSION_CHECK.md](ACTIVATION_CLASS_EXTENSION_CHECK.md).
They are internal checks relative to the explicitly named, previously
read mathematical interfaces. They are not promotion reviews or claims
that all older research in the repository is an established theorem.

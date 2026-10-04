# Compact comparison: a label-explicit width refinement and its limitation

2026-10-04. Scoped continuation of the same integrated study. This note
refines the deterministic width conversion for the existing autonomous
compact model. It preserves the source construction, its actual fourth
power of the label size in storage, the logarithmic exponent \(3d+2\),
the whole sphere, and the original physical times. It proves no new
stochastic estimate and makes no changes to the canonical statement.

Inputs read completely for the relevant argument are
`GENERAL_EXPLICIT_FITTING.md`,
`EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md`, the source/comparison argument
of `UNBOUNDED_COMPRESSOR_BRIDGE.md`, and the power ledger in
`SIMPLE_CONSTANTS_SOURCE_CHECK.md`. The relevant exact comparison is
source equations (42)--(53). Its inputs are inherited here; the algebra
below is new and explicit.

## 1. Setup and outcome

Keep the full model, activation, data and initialization hypotheses of
`SIMPLE_EXPLICIT_STATEMENT.md`. In particular \(L\ge2\),
\(\lambda=\gamma/m>0\), \(Y=\|y\|_2/\sqrt m>0\), and
\[
\beta=\max\left\{10,1+\max_j|\phi_j(0)|,16/a,
\max_{j,k=1,2}\sup_{|\operatorname{Im}w|\le a/2}
|\phi_j^{(k)}(w)|\right\},
\qquad B=\beta^{100L}.
\tag{1}
\]
Assume the same sufficient label condition
\[
0<Y\le\lambda\beta^{-30L}.
\tag{2}
\]
The original unbounded-value strip class is unchanged. Only the first
derivative must be bounded on the full open strip; the displayed constants
are its finite half-strip bounds.

For the derivation define temporary abbreviations
\[
X=\beta^L\ge100,\qquad z=Y/\lambda,\qquad
h=1+\lambda^{-1},\qquad \ell_n=\log(en).
\tag{3}
\]
The current source comparison improves to the following numerical width
condition, with no replacement of the displayed \(z\) by its upper cap:
\[
\boxed{
n\ge\left\lceil\max\left\{
N_0(\delta),\quad
\exp\!\left[\max\left\{
8Bzh(1+z\sqrt h),\
64B^2z^4h^2(1+z\sqrt h)^2,\ 2\right\}\right],\quad
\left(\frac{4B\sqrt h}{Y}\right)^4
\right\}\right\rceil .}
\tag{4}
\]
Here \(N_0(\delta)\) still includes the source/initialization probability
and construction conditions, as in the existing theorem; it depends on
all fixed problem parameters, including \(Y\). On its probability
\(1-\delta\) event, (4) implies
\[
\sup_{t\in[0,\infty],\,\|x\|=\sqrt d}
|f_C(t,x)-f_n(t,x)|\le Y/\sqrt n.
\tag{5}
\]
The storage bound remains exactly
\[
\operatorname{size}(C)\le
\beta^{(64+6d)L}\frac{(d+3)^d}{(d!)^2}
\left(\frac{Y}{\lambda}\right)^4\ell_n^{3d+2}
+2040(L+1)(2m+d+1)^2+10m(d+1).
\tag{6}
\]
Neither the approximation accuracy \(1/n\) nor the source rank or
coordinate selection has been changed.

At fixed positive admissible \(z\), the exponent in (4) grows like
\(\lambda^{-3}\) as \(\lambda\downarrow0\), improving the
\(\lambda^{-8}\) sufficient threshold obtained by replacing all four
comparison constants by \(\beta^{100L}(1+\lambda^{-1})^4\).
This does **not** remove gap dependence from the exponential. Section 4
identifies an exact obstruction in the current positive-coefficient
comparison; it is not a lower bound for the compact model itself.

## 2. Keeping the label factor in the existing comparison constants

The following are the same constants as in source (42)--(49); no new
trajectory bound is assumed. To avoid confusing them with (1), write
\(B_{\rm back}\) for the backward-error coefficient in source (46).
The checked power ledger gives
\[
\begin{gathered}
\lambda\le X^4,\quad Y\le X^{-26}<1,\quad z\le X^{-30},\quad
H_r,H_C,P_h\le X^4,\quad P_\delta\le X^5,\\
F\le X^9,\quad B_w\le X^6\sqrt h,\quad
B_{\rm back}\le X^{14}\sqrt h,\quad
K_{\rm src}\le X^{21},\\
\mathcal K\le X^7,\quad B_f\le X^{12}\sqrt h,\quad
\max_jd_j^c\le X^3,\quad \tau\le X^4.
\end{gathered}
\tag{7}
\]
Here \(H_r,H_C\) bound the selected true and compressed features;
\(F\) is the feature subtraction coefficient; \(\mathcal K\) and
\(B_f\) are the dense and compressed endpoint coefficients. Their exact
definitions, including all activation/depth recurrences, are in the
stated input. Inequalities (7) are the proved inequalities (18)--(24)
of `SIMPLE_CONSTANTS_SOURCE_CHECK.md`, with its temporary \(q\)
renamed \(h\).

Retain the actual factor \(z\) in the source's response/readout bounds:
\[
\begin{aligned}
D_r&=16z(\tau+3)\le zX^5,\qquad
D_C=5z\sqrt\lambda\max_jd_j^c\le zX^6,\\
W_r&=16zH_r\le zX^5,\qquad O=16zP_h\le zX^5.
\end{aligned}
\tag{8}
\]
For example \(32\le X\), \(5\le X\), and
\(\sqrt\lambda\le X^2\) prove these four bounds. Previously these
quantities were all replaced by small powers of \(X^{-1}\).

The exact Gram-difference coefficient is
\[
\begin{aligned}
G={}&(H_C+H_r)F+P_h
 +[1+(L-1)H_C^2](D_C+D_r)B_{\rm back}\\
&+(L-1)D_r^2(H_C+H_r)F
 +16zP_\delta[1+(L-1)H_r^2]
 +(L-1)(16z)^2\tau^2P_h.
\end{aligned}
\tag{9}
\]
Use \(L\le X\), \(H_C+H_r\le X^5\),
\(1+(L-1)H_C^2\le X^{10}\), and
\(D_C+D_r\le zX^7\). Its six summands are at most
\[
X^{14},\quad X^4,\quad zX^{31}\sqrt h,\quad
z^2X^{25},\quad zX^{16},\quad z^2X^{15},
\]
respectively. Only in bounding the last three smaller terms use
\(z\le X^{-30}\); each is then at most one. It follows that
\[
G\le X^{32}(1+z\sqrt h).
\tag{10}
\]
The unchanged bounds for the velocity-difference coefficients are
\(P_v\le X^5\) and \(Q_v\le X^{21}\sqrt h\). Since
\(\lambda^{-1}\le h\), the exact source definition
\(A=4P_vG/\lambda+Q_v+2G\) now yields
\[
A\le X^{39}h(1+z\sqrt h).
\tag{11}
\]
Indeed its three terms total at most
\((4X^{37}+X^{21}+2X^{32})h(1+z\sqrt h)\), and this is less
than \(X^{39}h(1+z\sqrt h)\).

The exact exponent coefficients are \(a_0=AS/2\) and
\(b_0=AK_{\rm src}S^2/2\), with \(S=16z\). Thus
\[
\begin{gathered}
a_0\le X^{40}zh(1+z\sqrt h),\qquad
b_0\le X^{62}z^2h(1+z\sqrt h),\\
C_{\rm out}\le X^{11}\sqrt h,\qquad
C_{\rm tail}=z(16\mathcal K+4B_f)\le X^{13}z\sqrt h.
\end{gathered}
\tag{12}
\]
The factors \(8\le X\) and \(128\le X^2\) establish the first
line. The output bound is the checked bound from (7); the tail follows
from \(16X^7+4X^{12}\sqrt h\le X^{13}\sqrt h\).

Every power of \(X\) in (12) is at most \(X^{100}=B\).
Consequently the four bounds used in (4) are
\[
\boxed{a_0\le Bzh(1+z\sqrt h),\quad
b_0\le Bz^2h(1+z\sqrt h),\quad
C_{\rm out}\le B\sqrt h,\quad
C_{\rm tail}\le Bz\sqrt h.}
\tag{13}
\]
The finer powers in (12) can be retained if numerical sharpness matters.
The proof has used the existing small-label hypothesis to control
auxiliary coefficients, while preserving the displayed actual label
factors in (12)--(13). It makes no assertion for large labels.

## 3. The width conversion, with every label dependence retained

The inherited all-time comparison is
\[
\|f_C-f_n\|_*
\le C_{\rm out}n^{-1}e^{a_0+b_0\sqrt{\ell_n}}
 +C_{\rm tail}e^{-8\ell_n}.
\tag{14}
\]
For the desired coefficient \(Y\), source (53) requires
\[
n\ge\max\left\{
e^{\max(8a_0,64b_0^2,2)},\quad
(2e^{1/4}C_{\rm out}/Y)^4,\quad
(2C_{\rm tail}/Y)^{2/15}\right\}.
\tag{15}
\]
The exponential part of (4) dominates the first part of (15) by (13).
Its polynomial part dominates the second, since \(2e^{1/4}<4\).
For the tail, (13) gives
\[
(2C_{\rm tail}/Y)^{2/15}
\le(2B\lambda^{-1}\sqrt h)^{2/15}
\le(2Bh^{3/2})^{2/15}.
\]
Because \(Y<1\), \(B,h\ge1\), one has
\[
\left[(4B\sqrt h/Y)^4\right]^{15/2}
=(4B\sqrt h/Y)^{30}\ge2Bh^{3/2}.
\]
This proves domination of the third part of (15). Therefore (4) implies
(5), on the same event and without changing the source construction.

In particular the former polynomial term proportional to
\(B^4(1+\lambda^{-1})^{16}/Y^4\) can be replaced by
\(256B^4(1+\lambda^{-1})^2/Y^4\). Its actual inverse-fourth
power of \(Y\) has not been absorbed into an unspecified constant.

## 4. Exact obstruction in the current positive-coefficient comparison

This section identifies what cannot be obtained merely by further
upper-bounding or cancelling terms in source (42)--(48). It is not a
claim that a different comparison proof cannot improve the result.

Fix any positive \(z\le\beta^{-30L}\) and let \(\lambda\downarrow0\),
with \(Y=z\lambda\). All activation/depth constants and the source
activity \(S=16z\) are fixed. The coefficient
\[
G_0=(H_C+H_r)F+P_h>0
\]
is also independent of \(\lambda\). Every summand in source (47) is
nonnegative. In particular \(P_v\ge2H_C\), \(G\ge G_0\), so
\[
A\ge8H_CG_0/\lambda,\qquad
a_0\ge64H_CG_0z/\lambda,\qquad
b_0\ge1024H_CG_0K_{\rm src}z^2/\lambda.
\tag{16}
\]
There is a stronger obstruction from its selected-response term. The
definitions imply
\[
B_{\rm back}\ge B_L\ge2sB_w\ge4s/\sqrt\lambda,
\qquad D_r=16z(\tau+3).
\]
Consequently
\[
G\ge D_rB_{\rm back}\ge64s(\tau+3)z/\sqrt\lambda,
\]
\[
A\ge512H_Cs(\tau+3)z/\lambda^{3/2},\qquad
b_0\ge65536H_Cs(\tau+3)K_{\rm src}
                  z^3/\lambda^{3/2}.
\tag{17}
\]
Together with (12), this shows that, for fixed positive \(z\), the
existing exact \(b_0\) grows at order \(\lambda^{-3/2}\), up to
positive constants depending on activation, depth, and \(z\).
Thus its existing sufficient conversion term \(e^{64b_0^2}\) has
an exponent of order \(\lambda^{-3}\). Algebra within these
nonnegative coefficients cannot turn that conversion into a polynomial
in \(\lambda^{-1}\).

This parameter regime is admissible. For example take the identity
activation in every layer, fixed \(L\), \(d=m=2\), and two unit
inputs \((1,0)\) and \((\cos\theta,\sin\theta)\). The initialized
covariance is unchanged across layers and has gap
\(\gamma=1-\cos\theta>0\). It tends to zero as \(\theta\to0\)
while the activation/depth envelope stays fixed. Labels of RMS
\(Y=z\gamma/2\) satisfy (2). This example demonstrates the domain
of the coefficient obstruction, not a prediction-error lower bound.

## 5. A cancellation that is valid, and the remaining stability bridge

The effective-readout formula admits one useful exact improvement over
the triangle inequality used in source (45). Let \(V\) be the current
compressed training feature map divided by \(\sqrt m\), with its
fixed selected neuron metric. Let \(P=V(V^*V)^{-1}V^*\) be its
orthogonal training-feature projector. Let \(w_r\) be the proof-only
selected dense raw readout, and let
\[
e=(y-c_n)/\sqrt m-V^*w_r
\]
be its current observation defect. Direct substitution gives
\[
\widehat w_C-w_r
=(I-P)(w_C-w_r)+V(V^*V)^{-1}
\left((c_n-c_C)/\sqrt m+e\right).
\tag{18}
\]
Because \(\|V(V^*V)^{-1}\|\le2/\sqrt\lambda\),
\[
\|\widehat w_C-w_r\|
\le\|w_C-w_r\|+\frac{2}{\sqrt\lambda}
\left(\|c_C-c_n\|_2/\sqrt m+\|e\|_2\right).
\tag{19}
\]
In particular the extra factor \(H_C/\sqrt\lambda\) multiplying
raw-readout discrepancy in the previous bound is unnecessary.
Separating hidden parameter discrepancy from raw-readout discrepancy
also avoids charging feature changes to the latter.

These valid improvements do not by themselves provide the missing signed
stability inequality. Unsigned integration of raw-readout error and
residual error still introduces the inverse residual gap. One would need
a new coupled estimate that uses the readout/residual cancellation rather
than bounding those two errors independently.

The canonical-gradient positive-semidefinite Hessian argument cannot be
imported without checking this point. In a selected neuron metric \(M\),
the metric adjoint of the activation derivative \(D=\operatorname{diag}
\phi'(z)\) is \(M^{-1}DM\), generally different from \(D\).
The specified compact optimizer uses \(D\) itself in its backward pass,
with non-diagonal selected metrics, and its effective readout includes an
independent residual correction. It is not the canonical gradient flow
whose parameter-discrepancy equation supplies that Hessian cancellation.
The individual energy identity and its positive-semidefinite residual
Gram do not establish the needed cross-trajectory signed identity.

Accordingly no sample-independent exponential coefficient, or polynomial
gap-dependent comparison threshold, is claimed here. Equations
(18)--(19) are an identified improvement available for a future coupled
stability argument; they are not silently substituted into (4).

## 6. The separate source-construction width cost

Even if a future comparison argument removes the gap from its exponential,
the present label-sensitive source construction has a separate explicit
gate. Source (30)--(31) requires
\[
\ell_n\ge64c_t^2
=\frac{a^2\lambda^2}{16384Y^4U^2},
\qquad c_t=\frac{a\lambda}{1024Y^2U}.
\tag{20}
\]
For the fixed \(z=Y/\lambda\) regime above, the recurrence for \(U\)
is fixed, so the right side is a positive constant times
\(\lambda^{-2}\). Equivalently this particular gate requires
\[
n\ge\exp\!\left\{\frac{a^2\lambda^2}{16384Y^4U^2}-1\right\}.
\tag{21}
\]
It is one of the deterministic gates already included in \(N_0(\delta)\).
The other construction gates and the genuinely unquantified source
probability threshold also remain. No statement that the complete
existing construction has polynomial dependence on the sample/gap or
label parameters follows from this note.

## Status

Proved here: the label-explicit coefficient bounds (12)--(13), the
improved sufficient threshold (4), unchanged storage (6), and the exact
projector identity (18). Identified precisely: the obstruction to a
polynomial gap threshold within the current positive-coefficient
comparison, and the separate source gate (20).

Not proved: a new signed stability theorem for the corrected optimizer,
an intrinsic lower bound on its approximation error or necessary width,
or an effective stochastic success threshold. The obstruction is scoped
to the stated proof and construction, not to every possible compressor
or proof.

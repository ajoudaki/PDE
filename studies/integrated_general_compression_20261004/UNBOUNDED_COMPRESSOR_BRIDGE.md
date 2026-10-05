# Joint sample budgets and the sharp unbounded-activation source bridge

**Interface correspondence (2026-10-05).** The common statement is
[RESULT.md](RESULT.md). Its compact neuron budget uses this note's
`q_j <= 9R` selection and `R <= A_n(Y)+2m+d+1` in §9, with the existing
activation-envelope bounds substituted. Those are upper bounds on
selected dimensions, not an invertible size/error relation. Sections 9
and 13 retain source tolerance `1/n`; the runtime has no independent
Taylor, spatial, or memory order. These preprocessing choices are discarded
after construction. All original construction gates and equations remain.

The current error comparison is proved in
[COMPACT_POLYNOMIAL_COMPARISON.md](COMPACT_POLYNOMIAL_COMPARISON.md) and
[COMPACT_FULL_LABEL_RANGE.md](COMPACT_FULL_LABEL_RANGE.md). It removes
the sample/gap and activation-depth factors from the comparison
exponential throughout the original label allowance, without changing
this source construction. Section 13 below retains its valid source
pairing/action lemmas and conservative comparison derivation as proof
support; its additional root-conversion thresholds are **not requirements
of the current integrated theorem**. Only the construction gates and
source probability threshold are inherited by the new comparison.

2026-10-04. Scoped derivation for the integrated study. This is new internal
research relative to the inherited, checked Gaussian insertion interface;
it is not an independent promotion review. The new part is the separate
**joint** sample budget and its RMS feedback closure, followed by the sharp
complex domain. No trained moment condition is assumed. The numerical
benchmarks with exponents 62, 124 and 82 are not asserted merely by removing
the bounded-value hypothesis.

The conclusion is an explicit finite source-smallness recurrence independent
of sample count and input dimension, a complex time radius proportional to
\((YS\sqrt{\log(en)})^{-1}\), a query radius proportional to
\(\log(en)^{-1/2}\), and retained source rank proportional to
\((Ym/\gamma)^2\log(en)^{3d/2+1}\). The existing corrected-readout
construction consequently has the fourth power of label activity in its
leading storage coefficient, at the same physical times and with all-time,
whole-sphere error \(C_{\rm data}/\sqrt n\), after imposing its separate
deterministic runtime fitting allowance. Every persistent constant in
the new source argument is defined below. The final deterministic runtime
error coefficient remains its separately stated interface, not a claim that
the benchmark \(\beta_\partial^{124L}\) has been verified.

## 1. Model, hypotheses, and inherited interfaces

Fix \(d,m\ge1\), \(L\ge2\), and training inputs
\(v_a=x_a/\sqrt d\in S^{d-1}\). At width \(n\), the dense network is
\[
z^{(1)}(v)=Av,\qquad z^{(j)}(v)=W^{(j)}h^{(j-1)}(v),\qquad
h^{(j)}(v)=\phi_j(z^{(j)}(v)),\qquad f_n(v)=w^\top h^{(L)}(v)/n.
\]
The middle recurrence starts at \(j=2\). Initially the entries of
\(A\) are independent \(N(0,1)\), hidden-mixer entries are independent
\(N(0,1/n)\), all blocks are independent, and \(w=0\). Write
\[
r_a=f_n(v_a)-y_a,\quad Y=\|y\|_2/\sqrt m,\quad
k_a^{(L)}=w,\quad \delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot k_a^{(j)},
\quad k_a^{(j)}=W^{(j+1)\top}\delta_a^{(j+1)}.
\]
The squared mean loss and mobilities \((n,1,\ldots,1,n)\) give
\[
\dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\quad
\dot W^{(j)}=-\frac2{mn}\sum_a r_a\delta_a^{(j)}h_a^{(j-1)\top},\quad
\dot w=-\frac2m\sum_a r_ah_a^{(L)}.                 \tag{1}
\]
No sign restriction is imposed on the fixed labels.

Each activation is real on the real axis, holomorphic on
\(|\operatorname{Im}z|<a\), with
\[
b=\max_j|\phi_j(0)|,\qquad
s=\max\{1,\sup_{j,|\operatorname{Im}z|\le a/2}|\phi_j'(z)|\},
\qquad
t=\max\{1,\sup_{j,|\operatorname{Im}z|\le a/2}|\phi_j''(z)|\}.
                                                               \tag{2}
\]
The hypothesis is still a bounded first derivative on the full open strip;
(2) uses its sharper half-strip derivative constants. Integration along
the straight segment from zero, which stays inside the safe half-strip,
and the definition of \(t\) give
\[
|\phi_j(z)|\le b+s|z|,\qquad
|\phi_j''(z)|\le t\quad (|\operatorname{Im}z|\le a/2).
\]
If \(s_{\rm full}=\max\{1,\sup_{j,|\operatorname{Im}z|<a}
|\phi_j'(z)|\}\), Cauchy's formula bounds every higher derivative
needed by the finite insertion graph on the safe strip by
\((q-1)!s_{\rm full}(4/a)^{q-1}\) for order \(q\ge2\).
These higher local coefficients enter only the stochastic eventual width.
Every persistent recurrence below uses (2). Thus no zeroth-order activation
bound is present, and the root's half-strip envelope satisfies
\(b+1,s,t\le\beta_\partial\).

Define initialized covariances by
\[
Q^{(0)}_{ab}=v_a^\top v_b,\qquad
Q^{(j)}_{ab}=\mathbb E[\phi_j(Z_a)\phi_j(Z_b)],\quad
Z\sim N(0,Q^{(j-1)}),\qquad
\gamma=\lambda_{\min}(Q^{(L)})>0.
\]
Put \(\lambda=\gamma/m\), without capping it at one. Linear growth
makes these moments finite. Conditional row laws, conditional fourth
moments on bounded covariance sets, and continuity under
\(Q^{1/2}G\) give empirical covariance convergence. Singular intermediate
covariances cause no difficulty. No population-training law is used.

The physical input is the independent small-label fitting result: real
operator caps \(\|A\|_{\rm op}/\sqrt n,\|W^{(j)}\|_{\rm op}<9\),
positive normalized Gram margin, and
\[
\rho(t):=\|r(t)\|_2/\sqrt m\le Ye^{-\lambda t/4}.
                                                               \tag{3}
\]
The root's `GENERAL_EXPLICIT_FITTING.md` supplies a sufficient explicit
condition for this input. This file does not assume (3) as an extra
scientific hypothesis: it is a separately proved deterministic fitting
interface, to be intersected with the source allowance below. Fixed-size
rectangular cavities retain the same normalization \(n\) and inherit a
strict initial margin at sufficiently large width.

The nontrivial probabilistic input is the inherited local insertion theorem
for linearly growing activations, from the complete unbounded candidate
and its local/probability checks in the authorized prior study, and its
complex extension in `ACTIVATION_CLASS_EXTENSION_ROUTE.md` and its check.
Its precise interface is: independently stopped cavities, actual-amplitude
forward and reverse source traces, coordinate error \(O_p(n^{-1/30})\)
for each fixed deletion count, control-uniform Gaussian and centered-form
events, and projected common-cavity errors of Gaussian radius
\(O_p(n^{-1/2+1/100})\). The underlying local coefficients may change
the eventual width; their strict powers of width are retained. Sections
3--8 below check all changed stopping and trace inputs of this interface.

Take \(Y>0\), and define
\[
S=16Y/\lambda,\qquad \ell_n=\log(en),\qquad
T=32\lambda^{-1}\ell_n,\qquad d\nu=2\rho\,|dz|.       \tag{4}
\]
Here \(d\nu\) is a proof measure along a contour, not a change of
physical time. Its real mass is at most \(S/2\) by (3). The earlier
absolute-residual measure is bounded by it. Cauchy--Schwarz across the
driving samples is why this larger measure is useful below. Zero labels
give the exact stationary zero predictor separately.

## 2. Explicit RMS, derivative, and trace coefficients

Use the complex operator caps ten and query input norm at most two.
Define the forward feature RMS bounds
\[
H_1=\max(1,b+20s),\qquad H_j=\max(1,b+10sH_{j-1})\quad(j\ge2).
                                                               \tag{5}
\]
Indeed \(\|Av\|_{2,n}\le20\), and linear growth followed by the
operator bound proves \(\|h^{(j)}\|_{2,n}\le H_j\), where
\(\|u\|_{2,n}=\|u\|_2/\sqrt n\). Integrating the readout equation
over a contour of \(\nu\)-mass at most \(S\) gives
\(\|w\|_{2,n}\le SH_L\). Define
\[
k_L=H_L,\quad k_j=10s k_{j+1},\quad \tau_j=sk_j,
\qquad P_1=3,\quad P_j=H_{j-1}+10sP_{j-1}+1,
\qquad f_j=sP_j.                                      \tag{6}
\]
Thus carrier and response RMS bounds are \(Sk_j,S\tau_j\).
The derivative numbers \(P_j\) also cover additive preactivation ports
at every layer: augment the mobility coordinates
\(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\)
by vectors \(e^{(j)}\) entering additively in \(z^{(j)}\), and
evaluate derivatives at \(e=0\). The direct first map has norm at
most \(2+1\); every later direct map contributes
\(H_{j-1}+1\). The recurrence proves the claimed augmented derivative
bound. These ports are proof variables and are never retained at runtime.

For \(F_a=nf_n(v_a)\), define
\[
A_*=2sP_L+2s^2\sum_{j=2}^Lk_jP_{j-1},\qquad
D_*=t\sum_{j=1}^LP_j^2,\qquad
H_*=A_*+t\sum_{j=1}^LP_j^2k_j.                     \tag{7}
\]
There are two readout cross terms of rank at most \(n\), two mixed
terms per hidden matrix, and curvature terms
\(Dz_a^{(j)\top}\operatorname{diag}(\phi_j''k_a^{(j)})Dz_a^{(j)}\).
The rank-normalized Schatten bounds consequently use (7), as shown in
Section 3. Crucially, \(D_\Theta\delta_a^{(j)}\) is a subblock of
this augmented Hessian, since \(\partial_{e^{(j)}}F_a=\delta_a^{(j)}\).
The same constants therefore cover both endpoints of the carrier trace;
no additional unproved endpoint estimate is needed.

Let \(f_* =\max_j f_j\), \(k_* =\max_jk_j\), and
\(H_{\max}=\max_jH_j\). Define
\[
E=t\sum_{j=1}^L(10s)^{2(j-1)}k_j,
\quad T_0=2H_*^2+4A_*^2(e^2-1),
\]
\[
D_0=(1+b+s)(1+T_0+E+s^2k_*^2),\qquad
D_1=576e^3(1+b+s)D_*^3,
\qquad C_F=s(8f_*^2+H_{\max}^2+1),
\qquad C_{\rm abs}=8(D_0+1).                       \tag{8}
\]
The subscript in the last constant means the scalar absorption coefficient.
It is unrelated to the initial first-weight matrix. All quantities in
(5)--(8) depend only on depth and activation bounds.

For the real activity moduli, set
\[
V_1=\tau_1,\qquad
V_j=\tau_jH_{j-1}^2+10sV_{j-1},
\]
\[
G_L=sH_L+14tV_L+s,\qquad
G_j=10sG_{j+1}+s^3k_{j+1}^2H_j+14tV_j+s,
\]
\[
W_{\rm G}=128\{1+H_{\max}+s\max_jV_j+\max_jG_j\}.
                                                               \tag{9}
\]
Their interpretation and derivation are in Section 5. Finally choose in
the stated order
\[
\eta=\min\{1,(1024C_{\rm abs}W_{\rm G})^{-1}\},\qquad
\mathcal B=1024e^2L,\qquad
\Lambda=\log(e+\mathcal B)+\log(1/\eta),
\]
\[
\begin{split}
S_*^{\rm src}=\min\bigg\{&1,\ (4A_*)^{-1},\
\sqrt{\eta/(4000D_*)},\
\sqrt{\eta/[16eD_*\sqrt{2\mathcal B}]},\
\sqrt{\eta/\Lambda},\
(\eta^3/(D_1\mathcal B))^{1/4},\
(8D_0C_F)^{-1/2}\bigg\}.                         \tag{10}
\end{split}
\]
Every denominator is strictly positive by (2), (5)--(9). The sufficient
source condition is \(S\le S_*^{\rm src}\), or
\(Y/\lambda\le S_*^{\rm src}/16\), together with the separate
real-fitting condition. This is a finite evaluable recurrence, independent
of \(m,d,\gamma,Y,n\), confidence, and empirical moment degree.

## 3. Separate joint budgets retain samplewise Schatten control

For each training sample separately let
\[
Z_{a,i}^{(j)}=\sup_z|z_{a,i}^{(j)}(z)|,\qquad
K_{a,i}^{(j)}=\sup_z|k_{a,i}^{(j)}(z)|,
\qquad
\mathcal H_a=\frac1n\sum_{j=1}^L\sum_i
 e^{\eta(Z_{a,i}^{(j)}+K_{a,i}^{(j)}/S)}.             \tag{11}
\]
The suprema are over each current stopped time rectangle. Stop every
\(\mathcal H_a\) at \(\mathcal B\), and each independently defined
cavity budget at \(2\mathcal B\). This includes the top carrier
\(k^{(L)}=w\). There is no maximum over samples inside an exponential.
The sample RMS running amplitudes at a neuron are
\[
Z_i^{(j)}=\left(m^{-1}\sum_a(Z_{a,i}^{(j)})^2\right)^{1/2},
\qquad U_i^{(j)}=\left(m^{-1}\sum_a(K_{a,i}^{(j)}/S)^2\right)^{1/2}.
                                                               \tag{12}
\]
These RMS quantities are not themselves the stopping budget. A single
RMS budget would not automatically control each sample's Schatten norms;
retaining (11) is essential.

For every sample, layer, and real \(p\ge2\), the elementary inequality
\(x^p\le(p/e)^pe^x\) yields
\[
\|k_a^{(j)}\|_{p,n}\le (S/\eta)p(2\mathcal B)^{1/p},\qquad
\|k_a^{(j)}\|_\infty\le(S/\eta)\log(2n\mathcal B).
\]
The augmented Hessian decomposition and (7) then prove
\[
\|D^2F_a\|_{p,n}\le A_*+(SD_*/\eta)p(2\mathcal B)^{1/p},
\quad \|D^2F_a\|_{2,n}\le H_*,
\]
\[
\|D^2F_a\|_{\rm op}\le A_*+(SD_*/\eta)\log(2n\mathcal B).
                                                               \tag{13}
\]
Here \(\|M\|_{p,n}=n^{-1/p}\|M\|_{S_p}\), also for rectangular
maps. The mixed blocks use the RMS of reference features; their action
is \(U_Hh/\sqrt n\), which is bounded by
\(H_j\|U_H\|_F\). Only the carrier diagonals need exponential
moments. Normalized residual mixtures retain (13), since
\(\sum_a|r_a|/(m\rho)\le1\).

The negative-Gram variational base contracts along the real solution.
All short complex/backwards pieces together have norm cost at most two,
after the explicit width condition in Section 8. The full propagator is
therefore bounded by
\[
2\exp\{SA_*+(D_*S^2/\eta)\log(2n\mathcal B)\}.
\]
Condition (10) gives \(D_*S^2/\eta\le1/4000\), leaving the inherited
\(n^{1/1000}\) variational cap at sufficiently large width. This
coefficient of \(\log n\) has not been moved into a width threshold.

The local graph uses only polynomial logarithmic coordinate caps. Every
samplewise cap in (11) gives such a cap without a factor \(m\).
Deleted forward amplitudes now have size \(b+sZ_{a,i}\); learned
columns and rows satisfy the inherited \(n^{-1/2}\operatorname{polylog}n\)
source bounds. The exact top residual offset multiplies both the retained
gradient and reverse force. Their norms are respectively
\(n^{-1/2}\operatorname{polylog}n\) and
\(n^{-1}\operatorname{polylog}n\). Thus the complete unbounded local
proof, including its uniform control net and nonlinear remainders, applies
on this stronger collection of stops. Its strict powers of width do not
change. This invokes the inherited local theorem in its actual form;
it does not assume independence after conditioning on full survival.

## 4. Actual-amplitude traces close in sample RMS

At an interior omitted neuron, the incoming row and outgoing column are
independent \(N(0,I/n)\) roots conditional on retained initialization.
Let \(G_{h,a,i}\) and \(G_{\delta,a,i}\) be the suprema of their
forward-feature and backward-response cavity pairings. Divide the latter
by \(S\) below. First establish the trace bounds for deterministic
control paths; the inherited Gaussian event is uniform over those paths.

In the backward trace, the two endpoints and \(h\) Hessian factors use
Schatten exponent \(h+2\). The zero-insertion term is at most
\(2H_*^2\). For \(h\ge1\), the integrated bound is
\[
\frac{2S^h}{h!}
 [A_*+(SD_*/\eta)(h+2)(2\mathcal B)^{1/(h+2)}]^{h+2}.
\]
Split the power into its bounded and carrier parts. Their sums are bounded
by \(4A_*^2(e^{2SA_*}-1)\) and
\[
\frac{8e^2D_*^2S^2\mathcal B}{\eta^2}
\sum_{h\ge1}(2eD_*S^2/\eta)^h(h+2)^2
\le\frac{576e^3D_*^3\mathcal B S^4}{\eta^3}.
\]
The last inequality uses \(\sum_{h\ge1}q^h(h+2)^2\le36q\) for
\(q\le1/2\), and follows by summing the geometric series and its first
two derivatives. Conditions (10) imply this restriction and \(SA_*\le1\).
The direct external trace is at most \(ES\): its curvature contraction
at layer \(j\) has nuclear norm per width at most
\(t(10s)^{2(j-1)}Sk_j\). The learned outgoing column adds at most
\(s^2k_*^2S^3\) times its actual forward amplitude. These are exactly
the terms in (8).

The substantive new point is to retain the sum over driving samples.
For each evaluated sample \(a\), each endpoint trace coefficient is
bounded by the same number, uniformly in driving sample \(b\). Hence
\[
\frac1m\sum_b|r_b|\,|h_{b,i}|\le
\rho\,(b+sZ_i),\qquad
\frac1m\sum_b|r_b|\,|\delta_{b,i}|\le\rho sS U_i.       \tag{14}
\]
These inequalities follow from Cauchy--Schwarz and the normalized sample
RMS in (12). They do not replace the time supremum by an instantaneous
quantity: the running amplitudes dominate every past integrand.

For the forward reverse-force trace the two forward endpoints have
operator and normalized Hilbert--Schmidt bound \(f_*\). In every term
with \(h\ge1\) insertions, give one endpoint exponent two, the other
infinity, and each Hessian exponent \(2h\). Its split series is bounded
by \(e^{2SA_*}-1\) and
\(\sqrt{2\mathcal B}\sum_{h\ge1}(4eD_*S^2/\eta)^h\).
Under (10) each is at most one. Including the zero term gives the
normalized trace bound \(8f_*^2\). Its learned incoming row has
norm at most \(sS^2U_iH_{j-1}/\sqrt n\); pairing against a retained
feature costs at most \(sS^2U_iH_{j-1}^2\). The first layer's direct
update costs at most \(sS^2U_i\). Thus \(C_F\) bounds all forward
feedback coefficients.

The uniform insertion expansion, (8), and (14) now give, sample by sample,
\[
K_{a,i}/S\le G_{\delta,a,i}/S+
 [D_0+D_1\mathcal B S^4/\eta^3](1+Z_{a,i}+Z_i)+o(1),
\qquad
Z_{a,i}\le G_{h,a,i}+C_FS^2U_i+o(1).                \tag{15}
\]
Independent incoming/outgoing cross forms are centered and their uniform
fluctuations are already in the insertion event. The direct external
trace at the evaluated sample multiplies its own current control
\(h_{a,i}\), not an average over driving samples. Its coefficient
\(ES\) costs \(ES(b+sZ_{a,i})\), explaining the separate
\(Z_{a,i}\) term. Only the integrated trace and learned-column terms
use (14)'s driving-sample RMS. This distinction is essential.

At the first layer, \(G_{h,a,i}\) is the initialized Gaussian row
paired with \(v_a\). At the top there is no outgoing root and
\(\sup|w_i|/S\le b+sZ_i\) by (14); take
\(G_{\delta,a,i}=0\). Thus both endpoints admit the same scalar
argument when their direct terms are assigned as specified below.

Taking sample RMS in (15), set
\(\overline G_h=(m^{-1}\sum_aG_{h,a,i}^2)^{1/2}\) and
\(\overline G_\delta=(m^{-1}\sum_a(G_{\delta,a,i}/S)^2)^{1/2}\).
Condition (10) gives backward coefficient at most \(2D_0\), and
forward coefficient \(D=C_FS^2\le1/(8D_0)\). Taking sample RMS
keeps both forward amplitudes and gives
\[
U_i\le\overline G_\delta+2D_0(1+2Z_i)+o(1),\qquad
Z_i\le\overline G_h+DU_i+o(1).
\]
The feedback product is \(4D_0D\le1/2\). Consequently
\[
U_i\le2\overline G_\delta+4D_0+8D_0\overline G_h+o(1),\qquad
Z_i\le\tfrac12+2\overline G_h+
                      \overline G_\delta/(4D_0)+o(1).
\]
For an individual sample,
\(Z_{a,i}\le G_{h,a,i}+\tfrac12+\overline G_h+
\overline G_\delta/(4D_0)+o(1)\). Substitution into its backward
inequality gives coefficients at most \(4D_0\) for the constant,
\(2D_0\) for \(G_{h,a,i}\), \(6D_0\) for
\(\overline G_h\), and one for \(\overline G_\delta\).
Adding the forward estimate proves the convenient envelope
\[
Z_{a,i}+K_{a,i}/S\le C_{\rm abs}
(1+G_{h,a,i}+G_{\delta,a,i}/S+
                  \overline G_h+\overline G_\delta)+o(1).          \tag{16}
\]
The constants in (8) include the direct evaluated-sample term. The coefficient is independent of
sample count and deletion count. The smallness choice precedes the
empirical moment degree.

## 5. Sample-uniform Gaussian moments, with no assumed moment law

Parameterize a real cavity by its own activity
\(u=\nu([0,t])/S\in[0,1]\), freezing after its endpoint. With
\(v=|u-u'|\), direct integration of (1) and (5)--(6) gives
\[
\|\Delta w\|_{2,n}\le H_LSv,\quad
\|\Delta A\|_F/\sqrt n\le\tau_1S^2v,\quad
\|\Delta W^{(j)}\|_F\le\tau_jH_{j-1}S^2v,
\]
\[
\|\Delta z_a^{(j)}\|_{2,n}\le V_jS^2v,\qquad
\|\Delta h_a^{(j)}\|_{2,n}\le sV_jS^2v.             \tag{17}
\]
For a changed backward gate, split the reference carrier at \(SR\).
The high part is bounded by
\[
\|k\mathbf1_{|k|>SR}\|_{2,n}
 \le(4S/\eta)\sqrt{2\mathcal B}\,e^{-\eta R/4},
\]
using \(x^2e^{-x/2}\le16\) and (11). Choose
\(R=(4/\eta)\log[8\sqrt{2\mathcal B}/(\eta v)]\) for \(v>0\).
The high changed-gate contribution is at most \(sSv\). The low
part is at most \(tV_jS^3Rv\). Since
\(R\le\eta^{-1}[10\Lambda+4\log(1/v)]\), the condition
\(S^2\Lambda/\eta\le1\), together with
\(v\log(1/v)\le2\sqrt v/e\), bounds that part by
\(14tV_jS\sqrt v\). The top carrier is treated by this same split;
it does not require a coordinate bound on the readout.

At the top, the other contribution is \(sH_LSv\). At a lower
layer, the changed mixer costs
\(s^3k_{j+1}^2H_jS^3v\), and propagation costs ten times the gate
bound \(s\). This proves the recurrence (9) and
\[
\|\delta_a^{(j)}(u)-\delta_a^{(j)}(u')\|_{2,n}/S
\le G_j\sqrt{|u-u'|}.                              \tag{18}
\]
All constants are independent of \(\eta,\mathcal B,m\) after the
explicit smallness restriction; the displayed recurrences already
include the top-carrier repair.

Condition on any autonomous cavity. For either of its scalar Gaussian
references, its initial variance and its square-root activity modulus
are bounded by (5), (9), (17)--(18). Dyadic grids of spacing \(4^{-q}\)
give at most \(2\cdot4^q\) increments of standard deviation bounded
by \(2G2^{-q}\). Gaussian tails with thresholds proportional to
\(2^{-q}\sqrt{z^2+4(q+1)}\), summed over all levels and with the
initial Gaussian value added, give
\[
\Pr\{X>W_{\rm G}(1+z)\mid\text{cavity}\}\le4e^{-z^2}.
                                                               \tag{19}
\]
Here \(X\) can be \(G_{h,a,i}\) or \(G_{\delta,a,i}/S\).
The coefficient 128 in (9) exceeds the sum of these dyadic thresholds
and the initial-value threshold. Integrating (19), or dominating the
positive excess by a variable with that tail, gives
\[
\mathbb E[e^{X^2/(16W_{\rm G}^2)}\mid\text{cavity}]<2.           \tag{20}
\]
For example, use \((1+z)^2\le2(1+z^2)\) and
\(\mathbb E e^{Z^2/8}\le1+4/7\) for a tail at most
\(4e^{-z^2}\); the resulting \(e^{1/8}(1+4/7)\) is below two.

For any collection of possibly dependent samplewise references,
\(\overline X^2=m^{-1}\sum_aX_a^2\). Convexity of the exponential
therefore gives the pointwise inequality
\[
e^{\overline X^2/(16W_{\rm G}^2)}
\le m^{-1}\sum_a e^{X_a^2/(16W_{\rm G}^2)}.
\]
Equation (20) thus holds for both RMS references in (16), with the same
constant and no independence between samples. Completing the square gives
\(\mathbb E e^{qX}\le2e^{4q^2W_{\rm G}^2}\) for each of the four
references. Hölder for their sum and (16) imply a moment bound
\[
\mathbb E e^{q(Z_{a,i}+K_{a,i}/S)}
\le 2\exp\{qC_{\rm abs}+64q^2C_{\rm abs}^2W_{\rm G}^2\}+o(1).
                                                               \tag{21}
\]
For \(q\le8\eta\), the right side is below four eventually by (10).
All higher fixed \(q\) also have finite moments. This is a consequence
of the stopped equations and Gaussian roots, not a premise concerning
trained coordinates.

Initial budgets are valid independently: at zero readout only forward
preactivations appear. On bounded preceding covariance sets, their
conditional second exponential moments are finite and their conditional
means continuous. Conditional Chebyshev gives convergence in probability
of each empirical layer budget. Its limiting mean is at most
\(2e^{\eta^2H_{\max}^2/2}<3\), so every initial sample budget is
below \(\mathcal B/2\) with probability tending to one. A fixed
sample union is allowed here. The inherited coordinate-small deletion
comparison transfers this margin to every fixed-size cavity. It does
not union-bound an \(O(1/n)\) estimate over deletion subsets.

## 6. Maximum, mixed endpoints, and explicit query coefficients

Impose training-coordinate maximum stops in addition to (11). Define
\[
C_G=32\max(1,H_{\max},\max_j\tau_j),\qquad
K_{\rm src}=16C_{\rm abs}(1+C_G).                    \tag{22}
\]
For cavity Gaussian references on a time rectangle of bounded width,
a mesh of size \(n^{-2}\) has a fixed multiple of \(n^5\) points.
Neurons, layers and the fixed sample count increase this to at most
\(n^7\) eventually. Complex Gaussian splitting gives tail
\(4e^{-u^2/(4\sigma^2)}\). The RMS coefficients are at most
\(H_{\max}\) and \(S\max\tau_j\), so (22) supplies strict
Gaussian margins of order \(\sqrt{\ell_n}\). Stopped derivatives
are polynomial logarithmic in normalized norm; the corresponding raw
coordinate derivatives are at most \(\sqrt n\operatorname{polylog}n\),
making the off-grid error vanish. The scalar inequalities (15)--(16)
therefore improve the full stops to
\[
\max_{a,j,i}|z_{a,i}^{(j)}|\le K_{\rm src}\sqrt{\ell_n},\qquad
\max_{a,j,i}|k_{a,i}^{(j)}|\le K_{\rm src}S\sqrt{\ell_n}.        \tag{23}
\]
This uses a polynomial Gaussian grid, not Gaussian supremum moments or
budget removal. Hence it precedes the complex moment argument.

For a complex great circle \(q(z)=u\cos z+v\sin z\), with real
orthonormal \(u,v\), define
\[
R_a^{(j)}=D_\Theta z^{(j)}(q)\nabla_\Theta F_a,
\qquad Q_a^{(j)}=\phi_j'(z^{(j)}(q))\odot R_a^{(j)},
\qquad J^{(j)}=\partial_z z^{(j)}(q(z)).
\]
These are residual-free response vectors, not physical velocities.
For \(|\operatorname{Im}z|\le1/8\), the input and every fixed
input derivative have norm below two. Put
\[
g=\tau_1+\sum_{j=2}^L\tau_jH_{j-1},\quad
r_j=P_jg,\quad q_j=f_jg,\quad j_j=20(10s)^{j-1},\quad b_j=sj_j,
\]
\[
e_1=tr_1P_1,\qquad
e_j=tr_jP_j+s(q_{j-1}+\tau_jH_{j-1}f_{j-1}+10e_{j-1}),
\]
\[
a_1=tj_1P_1+2s,\qquad
a_j=tj_jP_j+s(b_{j-1}+10a_{j-1}),
\]
\[
T_Q=8f_*\max_j(f_jH_*+e_j),\qquad T_J=8f_*\max_ja_j.          \tag{24}
\]
Here the layer coefficients \(r_j\) have a layer index, while the
physical residual \(r_a\) has a sample index. RMS bounds on
\(R,Q,J\) are \(Sr_j,Sq_j,j_j\). To derive the mixed endpoint,
differentiate \(Q=Dh\nabla F\): the first term uses \(DhD^2F\)
and (13); the second term uses the curvature diagonal
\(\operatorname{diag}(\phi''R)Dz\), the map
\(U_HQ/\sqrt n\), and a rank-one weight-gradient term. Their normalized
Hilbert--Schmidt coefficients are exactly the three forcing terms and
propagation in \(e_j\). The angular endpoint substitutes \(J\) for
\(R\); its first-layer additional map is \(U_Aq'\), whose
normalized Hilbert--Schmidt norm is at most two. This gives \(a_j\).
Neither endpoint uses a lower-layer coordinate maximum. Applying the
asymmetric trace from Section 4 with endpoint Hilbert--Schmidt norm
\(\max(f_jH_*+e_j)\) or \(\max a_j\) proves (24).

Set \(G_d=16\sqrt{d+3}\), and define
\[
U_1=4sK_{\rm src},
\]
\[
U_j=2\{sK_{\rm src}[H_{j-1}^2+f_{j-1}^2+ST_Q
                  +S^2H_{j-1}q_{j-1}]+G_dq_{j-1}+1\},\quad j\ge2,
\]
\[
V_1^{\rm qry}=2(2G_d+2sK_{\rm src}S^2+1),
\]
\[
V_j^{\rm qry}=2\{G_db_{j-1}+sK_{\rm src}S^2
                            (T_J+H_{j-1}b_{j-1})+1\},\quad j\ge2,
\qquad U=\max_jU_j,\quad V=\max_jV_j^{\rm qry}.       \tag{25}
\]
The four deterministic forward-response terms are, in order, the direct
feature pairing, direct reverse observable trace, exterior residual
integral, and learned-row correction. Their normalized coefficients are
the four terms inside the bracket. The centered Gaussian pairing gives
\(G_dq_{j-1}\). For the angular derivative both corrections have one
activity factor and one training carrier, hence \(S^2\). These are
the exact row-insertion terms from the inherited endpoint proof with each
bounded activation value replaced by its actual layer RMS (5).

Frames \((u,v)\) form a bounded subset of \(\mathbb R^{2d}\).
A frame mesh and the three real time/tube coordinates have at most
\(n^{4d+10}\) points eventually. The multiplier \(G_d\) dominates
the complex Gaussian tail union. Nearby frames are joined by polar
normalization of their linear interpolation; its derivative is bounded
near the orthonormal-frame manifold. Thus the same off-grid estimates
apply without chart multiplication. The inherited local graph, with a
temporary passive-query preactivation cap \(C\ell_n^2\), has only
polynomial logarithmic deleted controls. Query forward-control terms are
centered independent-root forms; the only nonzero same-root query trace
uses the training reverse control. The unbounded source check verifies
this exact distinction. Consequently the improved coordinate estimates are
\[
\max|R_a^{(j)}|\le US\sqrt{\ell_n},\qquad
\max|J^{(j)}|\le V\sqrt{\ell_n}.                    \tag{26}
\]
The initial whole-sphere preactivation maximum is \(C\sqrt{\ell_n}\)
by fresh-row Gaussian tails and a polynomial sphere mesh. Real-time
integration of (26) adds at most \(US^2\sqrt{\ell_n}\), so the
temporary passive-query size cap is strictly improved. No additional
query-coordinate exponential budget is needed.

## 7. Sharp complex derivative and joint-budget removal

Equation (1) and (24)--(26) give
\[
\|\dot z_a^{(j)}\|_{2,n}\le2\rho Sr_j,\qquad
\|\dot z_a^{(j)}\|_\infty\le2\rho SU_j\sqrt{\ell_n}.
\]
Let \(N_* =\max_j(r_j,U_j)\), and take any real \(p\ge4\).
Interpolate the velocity to exponent \(2p/(p-2)\), then apply
Hölder with the carrier \(p\)-norm from (11). This yields
\[
\|k_a^{(j)}\odot\dot z_a^{(j)}\|_{2,n}
\le (2\rho S^2N_*/\eta)p(2\mathcal B\ell_n)^{1/p}.
\]
For \(\ell_n\ge\max(e^2,2\mathcal B)\), take
\(p=\max(4,\log(2\mathcal B\ell_n))\). The last exponential factor
is at most \(e\), and \(p\le2\log(e+\ell_n)\). This is a
deterministic consequence of the stopped exponential budget at a growing
real exponent; it does not require growing deletion sets.

Define
\[
J_L^{\rm time}=2sH_L+4etN_*,\qquad
J_j^{\rm time}=10sJ_{j+1}^{\rm time}
                    +2s^3k_{j+1}^2H_j+4etN_*,\qquad
J_*^{\rm time}=\max_jJ_j^{\rm time}.
\]
Differentiating the backward recursion gives respectively the readout,
changed mixer, and changed gate contributions in this recurrence. Therefore
\[
\|\dot\delta_a^{(j)}\|_{2,n}
\le J_*^{\rm time}\rho
       [1+(S^2/\eta)\log(e+\ell_n)].                 \tag{27}
\]
The forward derivative is at most \(2\rho S\max q_j\). Thus, on
any time rectangle whose half-width is \(c_t/\sqrt{\ell_n}\) with
fixed \(c_t>0\), both normalized complex-minus-real Gaussian coefficient
radii tend to zero. For the backward coefficient divided by \(S\),
the explicit bound is
\[
D_n=(\lambda c_tJ_*^{\rm time}/4)\ell_n^{-1/2}
                     [1+(S^2/\eta)\log(e+\ell_n)].     \tag{28}
\]
The two time-parameter Lipschitz coefficients have the same bracket times
fixed constants. Their parameter interval has length \(O(\ell_n)\).
Dyadic Gaussian nets therefore have mean
\(O(\ell_n^{-1/2}[\log(e+\ell_n)]^{3/2})\) and tail scale
\(O(\ell_n^{-1/2}\log(e+\ell_n))\). Both vanish. Their exponential
moments at every fixed order tend to one, as do fixed squared-exponential
moments; the latter also transfer to RMS sample corrections by the Jensen
argument of Section 5.

Each cavity is frozen or clamped on its own domain and assigned zero
reference paths on failed own initialization. All Gaussian laws are then
conditional on retained initialization alone. Common-cavity path
differences are projected onto deterministic Euclidean balls of radius
\(C_pn^{1/100}\). Projection is nonexpansive and preserves independence
from the omitted root. Its Gaussian radius is \(C_pn^{-49/100}\),
so the real activity moduli and the complex nets give vanishing moments
at every fixed order. No full-network survival event is used as a Gaussian
conditioning event.

For a fixed sample and a fixed layer, expand the \(p\)th empirical
moment at fixed integer \(p\). Distinct neurons have independent root
pairs conditional on their common same-layer cavity. Equations (16),
(21), and the vanishing corrections give a main moment base below sixteen.
A fixed Hölder split handles projected errors at orders proportional to
\(p\); these moments tend to one at each fixed \(p\). Collision tuples
have \(O_p(n^{p-1})\) choices and finite higher fixed moments, hence
vanishing normalized contribution. The local exceptional probabilities
are superpolynomial and the stopped budgets are bounded.

The coordinate comparison transfers each individual joint budget:
\[
\mathcal H_a^{\rm cavity}\le
 e^{\eta o(1)(1+1/S)}\mathcal H_a+O_p(1/n)<2\mathcal B.
\]
Remove full-event indicators only after bounding by the nonnegative,
cavity-measurable Gaussian references. If any budget is hit, some sample
and layer has empirical budget at least \(\mathcal B/L\). Thus
\[
\limsup_{n\to\infty}\Pr\{\hbox{a joint budget is hit}\}
\le mL(16L/\mathcal B)^p.                            \tag{29}
\]
Take the width limit for each fixed \(p\), then its infimum over
positive integers. Since \(16L/\mathcal B<1\), the right side tends
to zero. This removes all joint budgets. Sample count affects a fixed
union and eventual width, not the source allowance in (10).

## 8. Label-sensitive time radius and the whole-sphere domain

Take
\[
c_t=\frac a{64YSU},\qquad
c_q=\min\{1/8,a/(8V)\},\qquad
r_t=c_t/\sqrt{\ell_n},\qquad r_q=c_q/\sqrt{\ell_n}.   \tag{30}
\]
For \(d\ge2\), the intrinsic query tube consists of
\(u\cosh h+i v\sinh h\), with real orthonormal \(u,v\) and
\(|h|\le r_q\). It is exactly the complex quadric neighborhood
\(q^\top q=1\), \(\|\operatorname{Im}q\|_2\le\sinh r_q\).
For \(d=1\), retain the two queries \(\pm1\) separately.

Set
\[
\mathcal K=H_L^2+S^2[\tau_1^2+
                    \sum_{j=2}^L\tau_j^2H_{j-1}^2],\qquad
D_W=\max\{\tau_1,\max_{j\ge2}\tau_jH_{j-1}\}.
\]
The actual algebraic residual Gram divided by \(m\), and the
negative-Gram variational generator divided by its factor two, have
operator norm at most \(\mathcal K\). This follows by summing the
squared normalized gradient-block norms, not by complex positivity.
Impose the explicit eventual width conditions
\[
n^{-1}\le Y,\qquad
\sqrt{\ell_n}\ge c_t\max\{8,\lambda,
                             4\mathcal K/\log2,32YSD_W\}.       \tag{31}
\]
Follow the real solution to the nearest real anchor in \([0,T]\),
then at most two short pieces of total length \(2r_t\). Their residual
growth and base-propagator cost are at most \(e^{4\mathcal Kr_t}\le2\).
The extra \(\nu\)-activity is at most \(8Yr_t\le S/2\).
The first-weight normalized and hidden-mixer increments are at most
\(8YSD_Wr_t\le1/4\), preserving strict margins inside cap ten.
No long horizontal complex contour is used.

The exact physical derivative is
\(\partial_tz^{(j)}=-(2/m)\sum_ar_aR_a^{(j)}\). On the short
pieces, \(\rho\le2Y\), so (26) bounds its coordinate magnitude
by \(4YSU\sqrt{\ell_n}\). The short time pieces and one intrinsic
query segment therefore have total preactivation displacement at most
\[
8c_tYSU+c_qV\le a/8+a/8=a/4.                         \tag{32}
\]
Full pole stops at \(3a/8\) and cavity stops at \(7a/16\) have
strict separation inside the derivative strip \(a/2\). Equation (32)
improves the full stop, and the coordinate comparison transfers its prefix
to all fixed-size cavity stops. The passive-query size stop improves by
Section 6. The logical order is local transfer, maximum improvement,
mixed endpoint and response improvement, query size/pole improvement,
complex Gaussian moments, and only then (29). Holomorphy holds on a
neighborhood of the closed rectangle times the closed query tube.

The radius coefficient \(c_t\) need not be at most one: its actual
radius shrinks at each fixed \(Y>0\). Condition (31) explicitly includes
\[
\ell_n\ge64c_t^2
 =a^2\lambda^2/(16384Y^4U^2).
\]
Thus the label-sensitive statement is not uniform as \(Y\downarrow0\).
No large fixed radius coefficient is used at an unchanged width.

## 9. Exact coefficient count, initialization-only construction, inventory

The four source families are
\[
h^{(j)}(t,v),\quad W_0^{(j)}h^{(j-1)}(t,v),\quad
\delta^{(j)}(t,v),\quad W_0^{(j+1)\top}\delta^{(j+1)}(t,v).
\]
Backward fields at a query are passive. On the proved domain their RMS
bounds are (5)--(6); hence every coordinate is bounded by
\(M_n=M_0\sqrt n\), where
\(M_0=10\max(H_{\max},\max\tau_j)\). The initialized images use
operator cap eight. This magnitude is obtained from RMS, not bounded
activation values.

For \(d\ge2\), apply the proved spherical coefficient theorem with
\[
\alpha=r_t/(4T)=c_t\lambda/(128\ell_n^{3/2}),\quad
b_d=2d-2,\quad D_d=2^{d+1}d^{d-2},\quad \epsilon=n^{-1},
\]
\[
P=\frac{18D_db_d!2^{b_d+1}}{\alpha r_q^{b_d+1}},\qquad
H=2\log(16M_nP/\epsilon).
\]
The time change \(t=T(1+\cos u)/2\) maps its strip into the time
rectangle. Fourier contour translation and the harmonic projection
bound give coefficient size
\(M_nD_d(j+1)^{b_d}e^{-\alpha|k|-r_qj}\). Splitting the omitted
exponential into two equal factors gives tail at most \(\epsilon/16\)
outside \(\alpha|k|+r_qj\le H\). The exact real coefficient count
per source family is
\[
N=\sum_{0\le j\le H/r_q}h_j
 [1+\lfloor(H-r_qj)/\alpha\rfloor],\qquad
h_j={j+d-1\choose d-1}-{j+d-3\choose d-1}.
\]
Impossible binomial coefficients are zero. Since
\(h_j\le2{j+d-2\choose d-2}\), disjoint unit cubes in a weighted
simplex give
\[
N\le\frac{2[H+\alpha+(d-1)r_q]^d}
                    {d!\alpha r_q^{d-1}}.             \tag{33}
\]
This retains the zero modes and lattice enlargement at finite width.

Let
\[
C_d^*=16\cdot128\cdot18M_0D_db_d!2^{b_d+1}
 \lambda^{-1}c_t^{-1}c_q^{-(b_d+1)}.
\]
In addition to (31), require
\[
\log C_d^*\le\ell_n,\quad (d+1)\log\ell_n\le\ell_n,
\quad(d-1)c_q/\sqrt{\ell_n}\le1,\quad\alpha\le1.      \tag{34}
\]
Then \(H\le7\ell_n\) and the enlarged radius in (33) is at most
\(9\ell_n\). Four source families and the exact initialized additions
therefore give
\[
R\le A_n(Y)+2m+d+1,
\qquad
A_n(Y)=\frac{2^{20}9^d}{d!}\frac Ua\,c_q^{-(d-1)}
               (Y/\lambda)^2\ell_n^{3d/2+1}.          \tag{35}
\]
The identity responsible for this dependence is
\[
\lambda^{-1}c_t^{-1}=1024(U/a)(Y/\lambda)^2.
\]
No inverse-radius coefficient has been put into a width threshold.
For \(d=1\), the two sphere points supply eight temporal source
families; the safe replacement is
\[
A_n(Y)=8\cdot514\cdot1024\,(U/a)(Y/\lambda)^2\ell_n^{5/2}.
                                                               \tag{36}
\]

The exact initial additions are training features and their forward
images, first-weight columns, and the constant. Finite harmonic quadrature
and finite initial-jet continuation approximate every coefficient from the
initialization, data and labels. The proved time strip has positive radius
at each fixed width, so the finite Taylor continuation procedure applies.
Apply identical scalar operations to a source and its initialized image;
their image identities are exact, while each member has its own coordinate
error. Jets, quadratures, original-width source vectors and dense initial
arrays are discarded after the reduced matrices and metrics are formed.

The inherited selection has at most \(9R\) selected coordinates per
layer, a fixed metric \(H_j^{\rm sel}\) satisfying
\(D_j/4\preceq H_j^{\rm sel}\preceq D_j\), and exact source
isometry. Its corrected-readout runtime retains moving first weights,
hidden mixers, raw readout and its own residual; fixed metrics and copies;
training data; training feature/backward arrays; and current Gram/solve
caches. The unchanged inventory is
\[
\operatorname{size}(C)\le1020(L+1)R^2+10m(d+1)
\]
\[
\le2040(L+1)A_n(Y)^2+
       2040(L+1)(2m+d+1)^2+10m(d+1).                 \tag{37}
\]
The exact initialization term remains explicit. Formula (35), or (36),
is the honest replacement for an unverified \(\beta_\partial^{82Ld}\)
envelope. It preserves the factorial dimension count and logarithmic
power \(3d+2\), with explicit layer-dependent coefficients.

## 10. Runtime transfer and claim boundary

The selected metric's exact source isometry and inclusion of the constant
give \(\|1\|_{H^{\rm sel}}=1\), \(\|1\|_D\le2\), and hence
\[
\|\phi(z)\|_{H^{\rm sel}}\le2b+2s\|z\|_{H^{\rm sel}},\qquad
\|\operatorname{diag}(\phi'(z))\|_{H^{\rm sel}\to H^{\rm sel}}\le2s.
\]
These are the needed replacements in its independent real fitting proof.
They follow from diagonal domination and linear growth, with no dependence
on the minimum selected weight. All first-weight columns are exact source
members, so the initial selected first-weight operator is bounded as well.
The corrected readout's orthogonal decomposition and raw-velocity energy
identity give its independent RMS tube and fitting under its own small-label
allowance, specified in
[EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md](EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md),
(5)–(6). Condition (10) alone
is not asserted to imply the runtime's deterministic fitting hypotheses.

Every pairing and learned-action defect uses source coordinate accuracy
and feature/response RMS only. A changed backward gate is multiplied by
the true reference carrier, now controlled by (23), including the readout.
The complete unbounded deterministic comparison therefore has its inherited
form
\[
\sup_{t\le T,\|v\|=1}|f_C(t,v)-f_n(t,v)|
\le C_{\rm data}\epsilon
       \exp\{C_{\rm data}(1+K_{\rm src}S\sqrt{\ell_n})S\}.
                                                               \tag{38}
\]
At \(\epsilon=n^{-1}\), the spare half power of width absorbs the
\(\exp(C\sqrt{\log n})\) factor for each fixed dataset. Independent
fitting of both autonomous systems gives sphere-uniform exponential tails,
so a sufficiently large fixed horizon coefficient extends (38) to all time
and the fitted endpoint. If its deterministic tail rate requires enlarging
the coefficient 32 in (4), every occurrence of 128 in the source count
must be enlarged by the same ratio; it is not silently absorbed. Under
the stated common rate \(\lambda/4\), coefficient 32 suffices.

The runtime uses current compressed features and its own evolving residual,
with an algebraically reconstructed readout. It is autonomous from
initialization and trains all hidden arrays, but it is the inherited
corrected optimizer, not ordinary gradient flow under a non-diagonal
neuron metric. No trained reference state or time-dependent source table
is stored. All comparisons are with the same realized canonical dense
initialization at the same physical times.

The new conclusions are the separate joint sample budget, sample-RMS
feedback/moment closure, and the transfer of sharp and label-sensitive
source radii to unbounded activation values. The local Gaussian insertion
theorem, deterministic harmonic approximation, source selection, and
corrected-runtime comparison remain identified inherited inputs. Exact-real
setup work and precision remain outside the retained-coordinate contract.
The stochastic width threshold is unquantified; (31) and (34) are additional
explicit sufficient conditions, not a claim to quantify that threshold.

The finite recurrences (5)--(10), (22), (24)--(25), (35)--(37) are the
numerical source objects. Their explicit activation-power audit is in
[SIMPLE_CONSTANTS_SOURCE_CHECK.md](SIMPLE_CONSTANTS_SOURCE_CHECK.md).
The current error theorem uses the coupled readout–residual proof linked
above, not the conservative unsigned coefficient in (38). All retained
size/count formulas in this source note are unchanged.

## 11. Input coverage and correction record

Complete source/check pairs read: activation-class extension; intrinsic
spherical source dimension; integrated label storage; the unbounded prior
activation candidate, local insertion check and probability check. Complete
additional reads: explicit source constants including reconciliation,
depth-independent exponent, label-depth rescaling, general analytic
compression, general weighted comparison, and quadratic corrected-readout
storage. These are in `closure_sampling_20261003` and
`dense_cutoff_population_rate_20261001`, as explicitly authorized for
this task. Canonical notation, neural-network conventions and the rigorous
proof skill were read. The maintained book and unrelated studies were not
read by this scoped agent. No experiment, external literature search,
Git mutation, or maintained-file edit was performed.

During drafting, the direct external trace was distinguished from the
integrated forcing trace: it uses \(Z_{a,i}\), while integrated forcing
uses \(Z_i\). Equation (15) keeps both. The explicit absorption following
it verifies that the allowance in (10) and coefficient in (8) already
cover that distinction. No samplewise-to-RMS replacement is used for an
unaveraged instantaneous control. This correction is incorporated before
delivery of the candidate for reconstruction.

## 12. Optional quadratic-exponential training budget

There is a useful consequence of the new Gaussian domination. It concerns
training preactivations and carriers, including the top readout, and adds
no label restriction. It does not assert the same result for a passive
query response \(R_a^{(j)}\) or a marked parameter-adjoint field.

Define the running scalar amplitude
\(X_{a,i}^{(j)}=Z_{a,i}^{(j)}+K_{a,i}^{(j)}/S\), with the same
time supremum as in (11), and put
\[
\eta_2=\min\{(2560C_{\rm abs}^2W_{\rm G}^2)^{-1},
                         (400K_{\rm src}^2)^{-1}\},\qquad
\mathcal B_2=128L.
                                                               \tag{39}
\]
Then, under the already established source event and (10), with probability
tending to one,
\[
\max_a\frac1n\sum_{j,i}\exp\{\eta_2(X_{a,i}^{(j)})^2\}
\le\mathcal B_2.                                      \tag{40}
\]
For the real training trajectories, the same statement, with the same
constants after an eventual strict-margin enlargement of the width, holds
with running suprema over all physical time.

Here is the additional argument. The square of (16)'s five-term sum is
at most five times the sum of their squares. Applying Hölder to the four
Gaussian-reference square exponentials and using (20), the first choice
in (39) leaves a bounded one-root expectation even at coefficient
\(4\eta_2\). The constants have substantial slack: the resulting
coefficient on each reference square is at most
\(80\eta_2C_{\rm abs}^2\le1/(32W_{\rm G}^2)\), below the
threshold \(1/(16W_{\rm G}^2)\) in (20). The constant term and the
vanishing scalar remainders give a limiting main moment base less than
eight. The complex and projected corrections have square-exponential
moments tending to one at every fixed coefficient, by their vanishing
Gaussian radius and mean. This proves the analogous common-cavity
distinct-root moment bound for the quadratic exponent.

There is an essential difference from the linear-exponential proof:
a Gaussian square does not have exponential moments at every coefficient.
One must not control collision tuples by an arbitrarily high fixed
multiple of \(\eta_2\). Instead, use the already proved maximum (23).
It gives \(X_{a,i}^{(j)}\le2K_{\rm src}\sqrt{\ell_n}\), hence
\[
e^{\eta_2(X_{a,i}^{(j)})^2}\le(en)^{1/100}.           \tag{41}
\]
For a term with \(k<p\) distinct neurons in the \(p\)th moment
expansion, use one quadratic exponential per distinct neuron in the
common-cavity estimate. Bound each remaining repeated factor by (41).
Its normalized count is \(O_p(n^{k-p})\), so its contribution is
at most a fixed constant times
\(n^{-(99/100)(p-k)}\), and vanishes. Local exceptional probabilities
are superpolynomial, while (41) bounds the stopped moment by a fixed
power of width at each fixed \(p\).

The same layer/sample union and Markov argument now gives
\[
\limsup_n\Pr\{\hbox{(40) fails on the source event}\}
\le mL(8L/\mathcal B_2)^p.
\]
Take width to infinity first and then the infimum over fixed \(p\).
This proves (40). For the all-time real extension, the independent physical
tube gives a raw coordinate carrier tail bounded by a fixed constant times
\(nS e^{-\lambda T/4}\), with a no-larger preactivation tail. At
\(T=32\lambda^{-1}\ell_n\) this is \(O(n^{-7})\) at fixed data.
Multiplication by the existing \(O(\sqrt{\ell_n})\) running maximum
shows that the change of the squared exponent is \(o(1)\). The proof's
strict moment ratio absorbs this change. Thus (40) controls real running
training carriers through infinity with no post-horizon trajectory oracle.

In particular (40) gives
\(\|k_a^{(j)}\|_{p,n}\le C S\sqrt p\) for all real \(p\ge2\),
with explicit coefficient obtained from
\(x^p\le[p/(2e\eta_2)]^{p/2}e^{\eta_2x^2}\) and
\(\mathcal B_2^{1/p}\). It does not by itself control products of
a carrier with an independently unbounded response field. Such a product
requires its second factor's corresponding moment bound or a separate
mixed-response argument; neither is implied by a coordinate maximum alone.

## 13. Explicit deterministic source-to-runtime comparison

This section supplies the numerical source pairing/action definitions
used by the current polynomial comparison. Its final unsigned comparison
is a conservative supporting estimate, not the current error interface.
Its additional input is the complete
`EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md`: intersect its explicit allowance
\(Y\le\lambda/(16H_c\sqrt{F_c})\) with (10) and the dense fitting
allowance. Here \(H_c,F_c\), the response coefficients \(d_j^c\),
and the endpoint coefficient \(B_f\) are exactly that file's equations
(5) and (11). It gives compressed feature RMS at most \(2H_c\),
hidden operator norm below nine, normalized top Gram at least
\(\lambda/4\), effective readout norm at most \(5Y/\sqrt\lambda\),
and residual rate \(\lambda/2\). No additional probabilistic premise
is used below. The notation in this section avoids identifying the
compressed neuron metric with the forward RMS constants (5).

Assume \(\epsilon=n^{-1}\le\min(1,Y,S)\). All constants below are
finite formulas. Set
\[
H_r=H_{\max}+3,\quad H_C=2H_c,\quad \tau=\max_j\tau_j,
\quad D_r=S(\tau+3),\quad
D_C=(5Y/\sqrt\lambda)\max_jd_j^c,\quad W_r=SH_r,
\]
\[
P_h=6H_{\max}+9,\qquad P_\delta=6\tau+9,
\quad A_f=18+S^2(\tau+3)P_h,
\quad A_b=18+S^2H_rP_\delta,\quad O=SP_h.             \tag{42}
\]
Every actual forward source restricted to the selected coordinates has
norm at most \(H_r\); every selected backward source has norm at most
\(D_r\). To check the constants, a coordinate error \(\epsilon\)
has empirical norm at most \(\epsilon\) and selected-metric norm at
most \(2\epsilon\). If two actual source norms are at most \(U,V\),
insert their exactly isometric approximants in the two pairings. The
empirical defect is at most \(\epsilon(U+V+\epsilon)\), and the
selected defect is at most \(2\epsilon(U+V)+8\epsilon^2\). Their
sum is at most
\[
3\epsilon(U+V)+9\epsilon^2.                         \tag{43}
\]
This gives \(P_h\epsilon\) for forward pairings and
\(SP_\delta\epsilon\) for backward pairings, using
\(\epsilon\le S\).

For proof only, use the selected true first weights and raw readout, and
the initialized selected mixers plus rank-one integrals of true selected
features/responses driven by \(c_n=y-f_n\). These are exactly the
reference arrays of the inherited runtime comparison, not runtime inputs.
Their initial forward and reverse actions on a source have defect at most
\((8\cdot2+2)\epsilon=18\epsilon\): the initialized operator norm
is eight and both members of each image pair have coordinate accuracy
\(\epsilon\). Learned forward actions add at most
\(S^2(\tau+3)P_h\epsilon\), learned reverse actions at most
\(S^2H_rP_\delta\epsilon\), by (43) and total residual activity
at most \(S\). Thus their forward/reverse action defects are
\(A_f\epsilon,A_b\epsilon\). Their readout observation defect is
at most \(O\epsilon\), by integrating the forward pairing defect.
The selected raw reference readout has norm at most \(W_r\).

Let \(d(t)\) be the sum of all first-weight, hidden-matrix, and raw
readout distances from these proof-only reference arrays, using the fixed
metric Hilbert--Schmidt norms. Let
\(u(t)=\|c_C(t)-c_n(t)\|_2/\sqrt m\). Define forward coefficients
\[
F^z_1=1,\quad F^h_1=2s,\qquad
F^z_j=9F^h_{j-1}+H_r+A_f,\quad F^h_j=2sF^z_j,
\quad F=\max_jF^h_j.                                \tag{44}
\]
Subtract the two forward passes, using the compressed operator bound nine
and selected activation Lipschitz constant \(2s\). The three terms in
\(F_j^z\) respectively propagate the lower feature error, multiply the
parameter difference by the true selected feature, and bound the action
defect. Thus the feature error at layer \(j\) is at most
\(F_j^h(d+\epsilon)\), uniformly on the query sphere.

Set
\[
C_r=H_C+W_rF+O,\qquad
B_w=1+(2/\sqrt\lambda)(1+C_r).                      \tag{45}
\]
The correction residual in the effective readout formula is bounded by
\(u+C_r(d+\epsilon)\): add and subtract the selected true prediction,
then use its observation defect, the raw readout difference, and (44).
The current inverse Gram gives
\(\|F_CQ_C^{-1}v\|\le2\|v\|_m/\sqrt\lambda\).
Consequently effective-readout error is at most
\(B_w(d+u+\epsilon)\).

Let \(M\ge1\) bound every true reference carrier coordinate. Define
backward error coefficients
\[
B_L=2sB_w+2tF_L^z,
\qquad B_j=2s(9B_{j+1}+D_r+A_b)+2tF_j^z\quad(j<L),
\qquad B=\max_jB_j.                                 \tag{46}
\]
Every changed gate is multiplied by the true selected carrier; its norm
cost is at most \(2tM\) times the preactivation error. The other term
uses the upper backward difference, a parameter difference times a true
selected backward vector of norm at most \(D_r\), and reverse action
defect \(A_b\epsilon\). Downward induction proves backward-response
error at most \(BM(d+u+\epsilon)\). There is one factor \(M\),
not one such factor per layer.

The following coefficients bound every term in the actual residual Gram
difference and every parameter velocity difference:
\[
\begin{split}
G={}&(H_C+H_r)F+P_h
 +[1+(L-1)H_C^2](D_C+D_r)B\\
&+(L-1)D_r^2(H_C+H_r)F
 +SP_\delta[1+(L-1)H_r^2]
 +(L-1)S^2\tau^2P_h,
\end{split}
\]
\[
P_v=2\{D_C[1+(L-1)H_C]+H_C\},
\]
\[
Q_v=2\{B[1+(L-1)H_C]+(L-1)D_rF+F\},
\qquad A=4P_vG/\lambda+Q_v+2G,
\qquad C_{\rm out}=H_CB_w+W_rF+O.                    \tag{47}
\]
To verify \(G\), first compare compressed pairings to selected true
pairings. The top feature pairing costs \((H_C+H_r)F\); response
pairings cost \((D_C+D_r)B M\); hidden-layer products add the feature
pairing cost multiplied by \(D_r^2\). Then compare selected true
pairings to empirical true pairings using (43). These last contributions
are \(P_h\), \(SP_\delta\),
\((L-1)SP_\delta H_r^2\), and
\((L-1)S^2\tau^2P_h\). Each entry is bounded by
\(GM(d+u+\epsilon)\); the normalized sample operator norm is at
most the maximum absolute entry. This proves
\(\|(K_C-K_n)/m\|\le GM(d+u+\epsilon)\), with no sample-count
factor. For \(P_v,Q_v\), subtract each rank-one velocity: its residual
difference uses compressed feature/response norms, while its remaining
terms use true residual times forward or backward errors. The readout
contributes the final \(H_C,F\) terms. This gives
\[
d(t)\le P_v\int_0^tu+Q_vM\int_0^t\rho(d+u+\epsilon).
\]

Both residual equations are exact, despite the corrected optimizer's
non-gradient form. Its independent Gram margin gives
\[
D^+u\le-\lambda u/2+2GM\rho(d+u+\epsilon).
\]
Regularizing the norm at zero justifies this inequality there. Integrate
once with damping and once after dropping damping:
\[
\int_0^tu\le(4GM/\lambda)\int_0^t\rho(d+u+\epsilon),\qquad
u(t)\le2GM\int_0^t\rho(d+u+\epsilon).
\]
Since \(d(0)=u(0)=0\), substitution and integral Gronwall prove
\[
d(t)+u(t)+\epsilon
\le\epsilon\exp\{AM\int_0^t\rho\}
\le\epsilon e^{AMS/2},
\]
\[
\sup_{t\le T,\|v\|=1}|f_C(t,v)-f_n(t,v)|
\le C_{\rm out}n^{-1}
 \exp\{a_0+b_0\sqrt{\ell_n}\},\qquad
a_0=AS/2,\quad b_0=AK_{\rm src}S^2/2.                \tag{48}
\]
Here \(M=1+K_{\rm src}S\sqrt{\ell_n}\) was substituted only at
the last step. No elapsed-time factor or unquantified comparison constant
occurs in (42)--(48).

For the dense flow, its all-time physical RMS bounds give
\(|\dot f_n(v)|\le2\mathcal K\rho\), with \(\mathcal K\)
from Section 8. Its endpoint tail is at most
\((8\mathcal K Y/\lambda)e^{-\lambda t/4}\). The runtime input
gives endpoint tail \((2B_fY/\lambda)e^{-\lambda t/2}\).
Comparing both trajectories to their values at \(T\), rather than
freezing either flow, proves the explicit all-time bound
\[
\sup_{t\in[0,\infty],\|v\|=1}|f_C-f_n|
\le \frac{C_{\rm out}}n e^{a_0+b_0\sqrt{\ell_n}}
 +\frac Y\lambda(16\mathcal K+4B_f)e^{-8\ell_n}.       \tag{49}
\]
The faster compressed tail was enlarged to the same last exponential.

There are two honest ways to state a root-width consequence. Young's
inequality \(b_0\sqrt{\ell_n}\le\ell_n/2+b_0^2/2\) gives the
explicit coefficient
\[
C_{\rm all}=C_{\rm out}e^{a_0+b_0^2/2+1/2}
                  +(Y/\lambda)(16\mathcal K+4B_f).     \tag{50}
\]
This can be exponentially ill-conditioned. To retain a prefactor
polynomial in the sample/gap parameters, instead display the additional
deterministic width threshold
\[
N_{\rm det}=\left\lceil
 \exp\{\max(4a_0,16b_0^2,2)\}\right\rceil.           \tag{51}
\]
For \(n\ge N_{\rm det}\),
\(a_0+b_0\sqrt{\ell_n}\le\ell_n/2\), and (49) gives
\[
\sup_{t,v}|f_C-f_n|\le
\frac{\sqrt e\,C_{\rm out}+(Y/\lambda)(16\mathcal K+4B_f)}{\sqrt n}.
                                                               \tag{52}
\]
The coefficients in (42)--(47) are finite sums/products and reciprocal
powers of \(\sqrt\lambda\), using the source allowance \(S\),
and are independent of \(m\) except through \(Y,\lambda\). Thus
(52) has an explicitly polynomial sample/gap prefactor; the conditioning
cost has moved into the **displayed deterministic** threshold (51).
The stochastic source threshold remains unquantified and must still be
intersected with (51). This is not a fully effective success-width theorem.

For clarity about label-scaled benchmark coefficients, an even stronger
explicit threshold can give a prescribed positive coefficient \(P\).
Replace (51) by
\[
\left\lceil\max\left\{
 e^{\max(8a_0,64b_0^2,2)},\quad
 (2e^{1/4}C_{\rm out}/P)^4,\quad
 [2Y(16\mathcal K+4B_f)/(\lambda P)]^{2/15}
 \right\}\right\rceil.                              \tag{53}
\]
The first term makes the finite-horizon contribution at most
\(e^{1/4}C_{\rm out}n^{-3/4}\); the other terms allocate half of
\(P/\sqrt n\) to it and half to the tail. For example,
\(P=Y\lambda^{-3/2}\) is allowed at every fixed \(Y>0\), with
its full explicit additional width cost in (53). Such a statement does
not establish that a proposed small prefactor is a sharp stability
constant, nor does it remove the unknown stochastic threshold. Equations
(48)--(52) expose the actual comparison constants without relying on an
arbitrary prefactor absorbed into an unspecified eventual width.

# Original frozen-top NTH: a nonlinear growing-order storage obstruction

Status: proved for the stated witness and internally checked, 2026-10-10.
The general two-tanh-layer problem remains open. This is research material,
not a completed independent promotion review.

For the subsequent fixed-finite-window formulation, see
[FINITE_TIME_RESULT.md](FINITE_TIME_RESULT.md). The same lower bound holds
for worst error on every fixed `[0,T]` at the passive query `-e_1`, while
the same-window dense-pair upper bound improves to `C_T sqrt(log(n)/n)`.
This sharpens the benchmark, not the necessary storage exponent below.

## Headline and exact scope

For a fixed, genuinely nonlinear first activation in the family
\[
\phi^{(1)}(z)=z+\varepsilon\sin z,\qquad
1/8\le\varepsilon\le1/4,\qquad \phi^{(2)}(z)=z,
\]
original frozen-top NTH cannot match dense-run variability with any
fixed-power polylogarithmic budget of explicit tensor entries. A necessary
direct-array size, along \(n_k=\lceil e^k\rceil\), is
\[
\exp\!\left(c_\eta\frac{\log n_k}{\log\log n_k}\right).
\tag{1}
\]
The positive constant is independent of width. This grows faster than
every fixed power of \(\log n\), but slower than every positive power of
\(n\). It is not an \(\Omega(n)\) or superpolynomial-in-width lower bound.

The model has two trained hidden layers, \(m=d=L=2\), orthogonal normalized
training inputs, canonical independent Gaussian initialization, zero
readout, and feature-learning mobility \((n,1,n)\). Labels are
\((\eta,0)\), where \(0<\eta\le10^{-62}\) is fixed independently of width.
For each fixed label, the theorem holds for Lebesgue-almost every single
fixed \(\varepsilon\in[1/8,1/4]\). The activation is not selected after
initialization or changed with width. A prescribed value such as
\(\varepsilon=1/4\) has not been certified.

This is a worst-case witness within the allowed analytic activation class,
not a theorem for two tanh activations or every correlated dataset. It
concerns literal NTH tensor arrays, not all encodings or all compressed
neural dynamics. No positive upper bound for the broader nonlinear class
is claimed.

## Canonical model, closure, and accuracy

For \(v=x/\sqrt2\), \(\|v\|=1\), the network is
\[
h^{(1)}(v)=\phi^{(1)}(W^{(1)}v),\qquad
h^{(2)}(v)=W^{(2)}h^{(1)}(v),\qquad
f_n(v)=u^\top h^{(2)}(v)/n.
\tag{2}
\]
The matrices have shapes \(n\times2\) and \(n\times n\); their independent
initial entries are \(N(0,1)\) and \(N(0,1/n)\), and \(u_0=0\). Train on
\(v_1=e_1,v_2=e_2\) with
\[
\mathcal L=((f_1-\eta)^2+f_2^2)/4,\qquad
\dot\theta=-M\nabla\mathcal L,\qquad M=\operatorname{diag}(n,1,n).
\tag{3}
\]
Define \(K_1(a)=f_a\), \(V_b=M\nabla f_b\), and
\[
K_{s+1}(a_1,\ldots,a_s,b)=D K_s(a_1,\ldots,a_s)[V_b].
\tag{4}
\]
The order-\(q\) original NTH copies all initialized tensors through rank
\(q\), freezes rank \(q\), and evolves each lower rank by
\[
\dot K_s^{(q)}(a_1,\ldots,a_s)
=\frac12\sum_{b=1}^2(y_b-f_b^{(q)})
 K_{s+1}^{(q)}(a_1,\ldots,a_s,b),\qquad f^{(q)}=K_1^{(q)}.
\tag{5}
\]
Thus the closure uses its own residual. Nothing is restarted, continued,
resummed, replaced by expected coefficients, or supplied with later dense
weights. Polynomial paths below are proof devices, not new algorithms.

Let \(E_n(q)\) be the supremum of \(|f_n-f^{(q)}|\) over the two training
inputs and all physical times. A missing global solution or required
fitted limit counts as approximation failure. Let
\[
D_n=\sup_{t\in[0,\infty]}\sup_{\|v\|=1}
 |f_n(t,v)-\widetilde f_n(t,v)|
\tag{6}
\]
for an independently initialized dense copy. The denominator uses the
whole circle. Failure even against this larger denominator rules out a
constant-factor comparison in the same finite-panel or whole-circle norm.

The population feature Gram is \(\gamma I_2\), where
\(\gamma=\mathbb E(G+\varepsilon\sin G)^2\ge9/16\).
The maintained strip hypotheses hold with \(\beta=10\), allowing unbounded
activation values. Also \(Y=\eta/\sqrt2\le(\gamma/m)\beta^{-30L}\).
No label or stability threshold shrinks with width. Both hidden parameter
blocks have nonzero order-\(\eta^2\) initial physical accelerations on a
width-independent, overwhelmingly likely event; this is verified in
[NONLINEAR_WITNESS.md](NONLINEAR_WITNESS.md).

## Quantitative theorem

For every fixed allowed label and almost every fixed activation parameter,
there is \(C_\eta<\infty\) such that, with probability tending to one,
simultaneously for every \(2\le q\le\lfloor k/4\rfloor\),
\[
E_{n_k}(q)\ge
\exp[-C_\eta q\{\log(q+1)+\log(k+1)\}].
\tag{7}
\]
The constants can be chosen uniformly in the activation interval, but
the sufficient onset may depend on the selected activation. The witness
is at a positive early time that may shrink with width, not necessarily
at the fitted endpoint.

For these same ordinary dense networks,
\[
\Pr\{D_n\le Cn^{-1/64000}\}\longrightarrow1.
\tag{8}
\]
This deliberately nonsharp whole-circle, complete-trajectory bound is
proved in [SINE_DENSE_VARIABILITY.md](SINE_DENSE_VARIABILITY.md). Any
positive polynomial rate suffices here; no sharp dense upper bound or
unproved population limit is imported.

Consequently every \(q_n=o(\log n/\log\log n)\) satisfies, along \(n_k\),
\[
E_{n_k}(q_{n_k})/D_{n_k}\longrightarrow\infty
\quad\text{in probability}.
\tag{9}
\]
A zero denominator counts as failure of constant-factor approximation.
The same exclusion holds for any absolute accuracy \(O(n^{-a})\), with
fixed \(a>0\), in particular \(n^{-1/2}\).

More precisely, for every fixed comparison factor \(A<\infty\), there is
\(c_\eta>0\) such that
\[
\Pr\left\{E_{n_k}(q)\le A D_{n_k}
 \text{ for some }2\le q\le c_\eta k/\log(k+1)\right\}\longrightarrow0.
\tag{10}
\]
This is simultaneous in the displayed orders, so initialization-dependent
order selection does not evade a deterministic budget below this range.
The literal training arrays have \(2^{q+1}-2\) entries; omitting a
redundant frozen odd top changes the count by at most a factor of two.
Equation (10) proves (1) as a necessary budget for positive fixed success
probability. Passive query inputs cannot remove the obstruction on a
training input.

The same error lower bound holds at the single distinct unlabeled query
\(v=-e_1\), supplied at initialization. Both activations are odd, so
\(f(-e_1)=-f(e_1)\) identically in the parameters. Every tensor with
first index \(-e_1\) is therefore the negative of the corresponding
first-index-\(e_1\) tensor. Initialization, top freezing, and (5) preserve
this relation exactly, giving \(f^{(q)}(-e_1)=-f^{(q)}(e_1)\).
Thus the prediction-error magnitude is identical on this passive input,
without a query label or an added training term. This is one specified
unseen input, not a lower bound for every possible passive query.

## Proof

The argument has four parts: an exact unmatched physical coefficient;
polynomial dependence on the fixed activation parameter; finite Gaussian
jet and real-time remainder bounds; and a polynomial coefficient
inequality that prevents cancellation among later Taylor terms.

### 1. Exact physical coefficient, including own-residual feedback

Readout reflection shows every odd-rank initialized tensor vanishes.
An odd top order has exactly the dynamics of the preceding even order.
Put \(j=2\lfloor q/2\rfloor+1\). The error derivatives below \(j\) vanish
at zero, and its degree-\(j\) Taylor coefficient is exactly
\[
J_{n,q}(\varepsilon)
=\frac{(\eta/2)^j}{j!}K_{j+1}^{\varepsilon}(1,\ldots,1)(0).
\tag{11}
\]
At the effective even top rank, the first derivative difference is zero
by parity, and the second is the twofold initial residual contraction of
the first nonzero omitted tensor. Each lower equation propagates that
discrepancy by one derivative. Residual differences are proportional to
the prediction difference and enter strictly later. The second initial
residual is zero, so every index in the surviving word is one.
This proves (11) without identifying dense and closure residual clocks.

At fixed weights, the prediction and each source vector field are affine
in \(\varepsilon\); (4) makes \(J_{n,q}\) a polynomial of degree at most
\(j+1\). At \(\varepsilon=0\), the exact initialized linear calculation in
[STRONGER_SOURCE.md](STRONGER_SOURCE.md) proves, simultaneously for all
orders on an event of probability at least \(1-Ce^{-cn}\),
\[
J_{n,q}(0)\ge(\eta/16)^j.
\tag{12}
\]
Only this coefficient is used, not the linear approximation theorem.
Its proof uses the source invariants
\(WW^\top-cc^\top=W_0W_0^\top\) and
\(\|a\|^2-\|c\|^2=\|a_0\|^2\) to obtain
\[
c''=(\|a_0\|^2 I+W_0W_0^\top)c+2\|c\|^2c.
\]
In an eigenbasis with nonnegative initial velocity its coefficients are
nonnegative. Comparison with \(2\tan(s/2)\), using
\(\|a_0\|^2,\|W_0a_0\|^2\ge1/2\), gives
\(K_{j+1}(1,\ldots,1)\ge j!8^{-j}\), hence (12).
The complete recurrence and simultaneous initialization event are
proved in that same-study dependency.

### 2. One fixed nonlinear parameter

Interpolation at measure-quantile points proves that a polynomial \(p\)
of degree at most \(D\) obeys
\[
\big|\{\varepsilon\in[1/8,1/4]:|p(\varepsilon)|\le\tau\}\big|
\le e\,(\tau/|p(0)|)^{1/D}.
\tag{13}
\]
[NONLINEAR_WITNESS.md](NONLINEAR_WITNESS.md) gives the full interpolation
calculation. Applying (13) to (11)--(12), followed by a union bound and
Borel--Cantelli on the parameter interval, proves that for almost every
single fixed \(\varepsilon\), eventually with probability at least
\(1-1/k\), simultaneously for \(2\le q\le k\),
\[
|J_{n_k,q}(\varepsilon)|\ge
L_{k,q}:=(\eta/16)^j(8e\,k^4)^{-(j+1)}.
\tag{14}
\]
Indeed the exceptional parameter measure is at most \(1/(8k^4)\) per
order. After summing over orders, the integral of the failure probability
over parameters is at most \(1/(8k^3)+Ce^{-cn_k}\). The measures of
parameter sets with failure probability greater than \(1/k\) are
summable. This constructs a deterministic full-measure set of fixed
activations, not an initialization-dependent choice.

### 3. Width-uniform initialized jets and genuine remainders

[INITIAL_JET_MOMENTS.md](INITIAL_JET_MOMENTS.md) proves a conditional
\(L^p\) bound
\[
[C(r+1)p(1+R_0)]^{C(r+1)}
\tag{15}
\]
for each initialized order-\(r\) physical or sample-word derivative,
including normalized state norms and each raw coordinate individually,
when initialized first preactivations have maximum at most \(R_0\).
Raw coordinate maxima are obtained by the subsequent union bound.

The proof explicitly differentiates the trained matrix actions.
Each resulting monomial is a forest of Gaussian matrix edges and bounded
initial gates, with normalized pairings. In a \(p\)-th moment, Wick
pairings leave at most \(pE/2+pS\) free neuron indices, cancelling
\(n^{-pE/2-pS}\); here \(E\) counts Gaussian edges and \(S\) normalized
scalar components. Each derivative adds bounded local expression size
at one Leibniz site, giving size \(O(r)\) and \((Cr)^{Cr}\) monomials.
The proof includes differentiated residuals and repeated uses of the
same matrix, not fresh-independent-matrix replacements.

Taking \(R_0=C\sqrt{\log n}\), \(p=C\log n\), and a union bound yields
one high-probability event through order \(\lfloor\log(en)\rfloor\),
retaining each order's own envelope. Through any smaller final order
\(R\), the state Taylor coefficients have geometric bounds \(B^r\),
where \(B\) is a fixed power of \(C(R+1)\log(en)\).

Section 7 of [SINE_REMAINDER.md](SINE_REMAINDER.md) then proves that
both the actual dense output and the original NTH output have
degree-\(R\) Taylor remainders bounded by
\[
C(Bt)^{R+1},\qquad 0\le t\le B^{-1},
\tag{16}
\]
after increasing the fixed polynomial power defining \(B\).
All constants are uniform in width and the fixed activation interval.
The discrepancy's combined remainder has the same form after increasing
\(C\).

For the dense output, set \(T'=1/\phi'\). The transformed scalar
activation has a uniform complex disk about every real point.
The finite state Taylor polynomial lies inside those disks for a
reciprocal-polynomial time. Cauchy's formula bounds its equation defect;
width-independent real stability compares it to the true flow. No
complex-domain theorem for the true dense trajectory is assumed.
For NTH, weighting rank \(s\) by \(B^s\) gives initial max norm one
and the majorant \(X'=2B^2X^2\). These weights are proof norms, not
changes to the closure. The resulting analytic remainder is (16).

### 4. Preventing cancellation by the later coefficients

Take \(R=2j\), which is within the initialized-jet range when
\(2\le q\le k/4\). A degree-\(R\) polynomial \(P\) with coefficient
\(J\) at degree \(j\) satisfies
\[
\sup_{0\le s\le t}|P(s)|\ge |J|t^j/(3\cdot7^R).
\tag{17}
\]
To verify it, expand \(P(tx)\) in \(T_r(2x-1)\). The expansion coefficients
are at most twice its supremum. The shifted Chebyshev recurrence gives
coefficient \(\ell^1\)-norm at most \(7^r\); sum the geometric series.

Let \(C_+=\max(1,C)\) in the combined remainder (16). Apply (17) to
the degree-\(2j\) Taylor polynomial of the actual discrepancy, and set
\[
\tau=\frac{L_{k,q}^{1/(j+1)}}{64C_+B^2}.
\tag{18}
\]
It is inside the remainder interval. The remainder-to-leading-bound
ratio is at most \((3/64)(49/64)^j<1/2\). Hence
\[
\sup_{0\le t\le\tau}|f_{n_k,1}(t)-f_{n_k,1}^{(q)}(t)|
\ge \frac16 L_{k,q}^2(3136C_+B^2)^{-j}.
\tag{19}
\]
The slight weakening uses \(0<L_{k,q}<1\).
Here \(\log B\le C\{\log(q+1)+\log(k+1)\}\). Substituting (14)
into (19) proves (7). The proof uses a degree-\(2j\) polynomial to
control all intervening cancellations; it does not simply discard
the later Taylor coefficients.

Finally choose \(c_\eta\) in (10) small enough that (7) is at least
\(e^{-k/128000}\) throughout that order range. Equation (8) is at
most \(Ce^{-k/64000}\) with probability tending to one. This proves
(9)--(10), and the tensor-array count gives (1).

## Resolution and remaining boundary

The four steps close an actual nonlinear growing-order prediction and
storage lower bound for the original frozen-top hierarchy. The earlier
cube-root order estimate obtained by isolating one leading term at an
unnecessarily tiny time is superseded by (7).

The following remain unresolved: two tanh hidden layers with general
correlated data; an \(\Omega(n)\) or stronger width lower bound;
a matching upper bound for this nonlinear witness; and lower bounds
for arbitrary implicit tensor encodings. The separate tanh Gaussian
sector and averaged Gaussian Taylor examples are diagnostics, not
proofs of these extensions.

The same-study checks are recorded in
[ASSEMBLY_CHECK.md](ASSEMBLY_CHECK.md), [SINE_CHECK.md](SINE_CHECK.md),
and the audit section of
[SINE_REMAINDER.md](SINE_REMAINDER.md). These are internal checks,
not independent promotion reviews. No experiments, commits, paper
edits, or maintained-book edits were performed in this continuation.

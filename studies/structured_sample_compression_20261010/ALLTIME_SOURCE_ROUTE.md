# Initial spectral sources and all-time nonlinear activity

Date: 2026-10-10. Bounded theoretical route within
`structured_sample_compression_20261010`; no experiments, paper edits or Git
operations. Scientific inputs: `paper/compact.tex`,
`paper/compact_selected.tex`, and this study's `RESULT.md` and
`SPECTRAL_ROUTE.md`. No `paper/compact_dense.tex` exists. Required proof,
conjecture and canonical-notation instructions were read. All results below
are derived here and are internally checked, not independently reviewed or
promoted.

The route does not close the requested theorem. It gives a static sufficient
certificate for all-time activity of the actual nonlinear network, and an
all-time comparison estimate without a spectral gap. Neither certificate
has been established uniformly in the sample count for the prescribed
Gaussian deep network. Ordinary relative kernel control plus arbitrarily
smooth initial labels is insufficient for residual activity; an explicit
nonlinear least-squares example proves that narrower negative statement.

## 1. Exact model and the proposed replacement for the gap

Use the paper's width `n`, sample count `m`, input dimension `d`, hidden
depth `L`, normalized input \(v=x/\sqrt d\), and network

\[
z^{(1)}=W^{(1)}v,\qquad
z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\qquad
h^{(\ell)}=\phi_\ell(z^{(\ell)}),\qquad
f_\theta(x)=\frac{w^\top h^{(L)}(x)}n.
\]

The activations satisfy the paper's strip analyticity and bounded strip
derivative assumptions; their values may be unbounded. The Gaussian initial
matrices and zero initial readout are unchanged. In mobility-normalized
coordinates

\[
\theta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n),
\qquad r_a=f_\theta(x_a)-y_a,
\qquad \mathcal L=\|r\|_m^2,
\]

where \(\|u\|_m^2=m^{-1}\sum_a u_a^2\), the physical training flow is
\(\dot\theta=-\nabla_\theta\mathcal L\). Let
\(J_\theta:\mathbb R^P\to\mathbb R^m\) be the prediction derivative,
where \(P=(L-1)n^2+n(d+1)\), with the ordinary Euclidean norm in parameter
space and \(\|\cdot\|_m\) in sample space. Thus

\[
(J_\theta u)_a=D f_\theta(x_a)[u],\qquad
J_\theta^*r=\frac1m\sum_a r_a\nabla_\theta f_\theta(x_a),\qquad
A(\theta)=J_\theta J_\theta^*.
\]

In matrix entries \(A_{ab}=m^{-1}\langle\nabla f(x_a),\nabla f(x_b)\rangle\).
These definitions include the paper's block mobilities exactly. The flow,
residual equation and energy identity are

\[
\dot\theta=-2J_\theta^*r,\qquad
\dot r=-2A(\theta)r,\qquad
\frac d{dt}\|r\|_m^2=-4\langle r,A(\theta)r\rangle_m
                    =-\|\dot\theta\|_2^2.                 \tag{1}
\]

At initialization only readout derivatives are nonzero, so

\[
A_0:=A(\theta_0),\qquad
(A_0)_{ab}=\frac{h_a^{(L)}(0)^\top h_b^{(L)}(0)}{nm},
\qquad r(0)=-y.                                         \tag{2}
\]

The source norm proposed here is \(\|A_0^{-s}y\|_m\), when defined;
it concerns the realized initialized kernel, not a future learned kernel.
For a singular \(A_0\), a finite source requires
\(y\in\operatorname{ran}A_0\) and inverses on that range. Merely replacing
\(A_0\) by its population limit would require a separate concentration
estimate in this inverse-weighted norm. Ordinary entrywise concentration
does not provide it.

The intended compression still requires initialization-only coefficients,
autonomous runtime, data storage independent of `m` at fixed accuracy, and
comparison to the same-initialization dense trajectory on the stated query
domain. A kernel identity with an externally supplied \(A(t)\) is not such
a runtime.

## 2. What initial source norms actually prove for a frozen operator

Let \(A\succeq0\) on a finite sample Hilbert space, \(\|A\|\le\Lambda\),
\(\Lambda>0\), and \(y=A^s g\), with \(s>1\). For the auxiliary frozen
equation \(\dot r=-2Ar\), \(r(0)=-y\), diagonalization gives

\[
\|r(t)\|_m\le\|g\|_m\sup_{0\le\lambda\le\Lambda}
                       \lambda^s e^{-2\lambda t}.
\]

For \(t\le(2\Lambda)^{-1}\) use \(\Lambda^s\); afterwards maximize
\(\lambda^s e^{-2\lambda t}\) over all positive \(\lambda\), obtaining
\((s/(2et))^s\). Integration proves

\[
\int_0^\infty\|r(t)\|_m\,dt
\le \frac12\left(1+\frac{(s/e)^s}{s-1}\right)
       \Lambda^{s-1}\|g\|_m.                            \tag{3}
\]

There is no smallest-eigenvalue factor or explicit dimension factor.
The source assumption can hold with a fixed nonzero label RMS `Y` as `m`
grows. It is a data regularity assumption, not a consequence of label
bandlimitation or smoothness in the input coordinates.

The restriction \(s>1\) cannot simply be lowered to \(s=1\) for a
dimension-independent residual-activity bound based only on this Hilbert
source norm. In an orthonormal sample basis take eigenvalues
\(1,2^{-1},\ldots,2^{-N}\) and label coefficients
\(1,2^{-1}/\sqrt N,\ldots,2^{-N}/\sqrt N\). Then
\(\|A^{-1}y\|=\sqrt2\), and the label norm lies between `1` and
\(\sqrt{4/3}\). On each disjoint interval
\([2^{j-1},2^j]\), the `j`th slow residual component has magnitude at
least \(2^{-j}e^{-2}/\sqrt N\). Its integral on that interval is at
least \(e^{-2}/(2\sqrt N)\). Summing the intervals gives activity at
least \(e^{-2}\sqrt N/2\). Rescaling all labels by their norm makes
`Y=1` and changes these constants by at most \(\sqrt{4/3}\).
The operator trace remains below `2`.

For \(0<s<1\), a fast unit label coordinate together with a slow
coordinate \(\lambda^s\), \(\lambda\downarrow0\), keeps the source
norm bounded and the label norm bounded away from zero, but the slow
activity is \(\lambda^{s-1}/2\). Thus a first inverse moment or an
initial RKHS norm does not by itself bound the residual activity used by
the paper's present proof. This says nothing against alternative proofs
based directly on parameter displacement or dissipation.

## 3. A static sufficient certificate for the actual nonlinear flow

Here is a non-circular positive statement. All its hypotheses are defined
on a ball known at initialization, not on an unknown future trajectory.
They are stronger than ordinary relative kernel control.

Assume \(A_0\) is positive definite. Fix a radius \(R>0\), put
\(\Lambda=\|A_0\|>0\), and define the finite initial-data quantities

\[
G=\|A_0^{-2}y\|_m,
\quad
B_R=\sup_{\|\theta-\theta_0\|\le R}\|J_\theta\|,
\quad
b_R=\sup_{\|\theta-\theta_0\|\le R}
       \|A_0^{-2}(A(\theta)-A_0)\|.                     \tag{4}
\]

The last norm is an ordinary operator norm in sample Hilbert space; its
product is not generally self-adjoint. Suppose

\[
q:=16\Lambda b_R<1,
\qquad
D:=\frac{2B_R\Lambda G}{1-q}<R.                       \tag{5}
\]

Then the actual nonlinear gradient flow is global, stays strictly within
the ball, fits the labels, and converges in parameter space. Quantitatively,

\[
\begin{aligned}
\|r(t)\|_m&\le\frac{G\Lambda^2}{1-q}(1+\Lambda t)^{-2},\\
\int_0^\infty\|r(t)\|_m\,dt&\le\frac{G\Lambda}{1-q},\\
\int_t^\infty\|\dot\theta(u)\|_2\,du
&\le D(1+\Lambda t)^{-1}.                              \tag{6}
\end{aligned}
\]

To prove this, stop before the first exit from the ball, and write
\(E(t)=A(\theta(t))-A_0\). Variation of constants in (1) is exact:

\[
r(t)=-e^{-2A_0t}A_0^2g
       -2\int_0^t e^{-2A_0(t-u)}A_0^2
                       [A_0^{-2}E(u)]r(u)\,du,
\quad g=A_0^{-2}y.
\]

For \(0\le\lambda\le\Lambda\), the inequality
\((1+\lambda t)e^{-\lambda t}\le1\) gives

\[
\|A_0^2e^{-2A_0t}\|\le k(t),\qquad
k(t)=\frac{\Lambda^2}{(1+\Lambda t)^2},\qquad
\int_0^\infty k(t)\,dt=\Lambda.
\]

Splitting the convolution at \(t/2\), the larger-time factor is at
most \(4k(t)\) on each half. Therefore
\((k*k)(t)\le8\Lambda k(t)\). On any finite stopped interval let
\(M=\sup_t\|r(t)\|_m/k(t)\). The exact formula gives
\(M\le G+16b_R\Lambda M\), hence \(M\le G/(1-q)\).
Integrating, and using \(\|\dot\theta\|\le2B_R\|r\|_m\), proves
(6). The path length is less than `R`, so the first exit cannot occur.
The smooth vector field has no finite-time escape inside a compact ball,
which gives global continuation. The integrable parameter velocity gives
a limit, and the first line of (6) gives fitting.

For a compact query set \(\mathcal X\), set

\[
B_R^{\mathcal X}
=\sup_{\|\theta-\theta_0\|\le R,\ x\in\mathcal X}
                           \|\nabla_\theta f_\theta(x)\|.
\]

The same path integral then gives, for every \(t\ge T\), including
the endpoint,

\[
\sup_{x\in\mathcal X}|f_\theta(t,x)-f_\theta(T,x)|
\le B_R^{\mathcal X}D(1+\Lambda T)^{-1}.                \tag{7}
\]

Consequently two nonlinear systems satisfying such certificates can be
compared for all time by a finite-time comparison through `T` plus the
sum of their two bounds (7). This is a genuine initial-data sufficient
condition for the tail bridge in `RESULT.md`.

If \(A_0\) is singular, this proof extends on its range only when
\(y\) belongs to that range and the ball satisfies
\(A(\theta)-A_0=A_0^2 C(\theta)\) with bounded \(C\).
Self-adjointness then also forces the evolving kernel to annihilate
\(\ker A_0\). At zero readout \(\operatorname{rank}A_0\le n\), so
positive definiteness already requires \(m\le n\). The singular
extension suppresses kernel rank creation and is not a generic consequence
of feature learning.

### An alternative certificate using weighted absolute coefficients

For activity alone there is a simpler, alternative sufficient test.
Let \((e_j)\) be an orthonormal eigenbasis in the empirical inner product
for positive definite \(A_0\), with eigenvalues \(\lambda_j>0\).
Define \(y_j=\langle e_j,y\rangle_m\), and for each parameter state
write \(E_{ij}(\theta)=\langle e_i,(A(\theta)-A_0)e_j\rangle_m\).
The following quantities again use only the initialized problem and its
chosen parameter ball:

\[
S=\sum_j\frac{|y_j|}{\lambda_j},\qquad
\eta_R=\sup_{\|\theta-\theta_0\|\le R}
                 \max_j\sum_i\frac{|E_{ij}(\theta)|}{\lambda_i}.
\]

If \(\eta_R<1\) and \(B_RS/(1-\eta_R)<R\), the actual nonlinear
flow is global, fits, has a parameter limit, and satisfies

\[
\int_0^\infty\|r(t)\|_m\,dt\le\frac{S}{2(1-\eta_R)},
\qquad
\int_0^\infty\|\dot\theta(t)\|\,dt
\le\frac{B_RS}{1-\eta_R}.
\]

Indeed, let \(r_j(t)=\langle e_j,r(t)\rangle_m\). The residual
equation gives, in upper right derivatives at zeros,

\[
\frac d{dt}\sum_i\frac{|r_i|}{\lambda_i}
\le-2\sum_i|r_i|+
    2\sum_j|r_j|\sum_i\frac{|E_{ij}(\theta)|}{\lambda_i}
\le-2(1-\eta_R)\sum_j|r_j|.
\]

Integrate and use \(\|r\|_m\le\sum_j|r_j|\) and
\(\|\dot\theta\|\le2B_R\|r\|_m\). The strict path-length
bound closes the ball as before. The finite path gives a parameter and
residual limit; integrable residual norm makes that limit zero. This
argument establishes activity but states no uniform tail rate. Storing
the full eigenbasis is not a sample-compressed runtime, and neither `S`
nor `eta_R` is bounded uniformly in `m` by the current deep-network
assumptions. The inverse-weighted leakage remains the missing estimate.

## 4. Explicit network dependencies and what is missing

The quantities (4) are computable definitions from initial data, architecture
and a specified compact ball. Their finiteness does not imply useful or
sample-uniform bounds. To make this distinction explicit, let

\[
a_1=\|W^{(1)}(0)\|_{\mathrm{op}}/\sqrt n+R,
\qquad a_\ell=\|W^{(\ell)}(0)\|_{\mathrm{op}}+R\quad(\ell\ge2),
\]

and let \(b=\max_\ell|\phi_\ell(0)|\),
\(s=\max_\ell\sup_{\mathbb R}|\phi'_\ell|\),
\(t_2=\max_\ell\sup_{\mathbb R}|\phi''_\ell|\); all are at most
the paper's \(\beta\). The following deterministic recurrences are
valid over the whole input sphere and the parameter ball:

\[
\begin{aligned}
H_1&=b+sa_1,& H_\ell&=b+sa_\ell H_{\ell-1},\\
Z_1&=1,& Z_\ell&=H_{\ell-1}+a_\ell P_{\ell-1},\\
P_\ell&=sZ_\ell,\\
Q_1&=t_2\sqrt n,&
Q_\ell&=s(2P_{\ell-1}+a_\ell Q_{\ell-1})
                   +t_2\sqrt n Z_\ell^2\quad(\ell\ge2).
\end{aligned}                                         \tag{8}
\]

Here `H` bounds feature RMS, `P` bounds first parameter directional
derivatives in neuron RMS, and `Q` bounds mixed second derivatives for
two unit parameter directions. The first-layer normalization gives
\(\|D z^{(1)}\|/\sqrt n\le1\). In later layers differentiate
\(W^{(\ell)}h^{(\ell-1)}\) once and twice. The second activation
derivative uses
\(\|u\odot v\|/\sqrt n\le\sqrt n\|u\|_n\|v\|_n\),
which explains the explicit \(\sqrt n\). Differentiating the readout
therefore gives the envelopes

\[
B_R,\ B_R^{\mathcal X}\le B:=H_L+RP_L,
\qquad
\sup_{\theta,x}\|D^2 f_\theta(x)\|\le H:=2P_L+RQ_L.
                                                               \tag{9}
\]

These bounds allow unbounded activation values. They contain no explicit
`m`; `d` occurs through the initialized first-layer norm. Since
\(DA=(DJ)J^*+J(DJ)^*\), (9) gives only

\[
b_R\le\frac{2BHR}{\lambda_{\min}(A_0)^2}.              \tag{10}
\]

This generic consequence of the activation assumptions loses the gap
twice. It does not prove (5) uniformly in `m`. Proving a much smaller
inverse-weighted derivative bound is the substantive missing step, not a
change of notation in the existing theorem.

For completeness, the initialized operator factors admit elementary
probability bounds. At confidence \(1-\delta\), simultaneously,

\[
\begin{aligned}
\|W^{(1)}(0)\|_{\mathrm{op}}/\sqrt n
&\le2\sqrt{2\left[(1+d/n)\log9+n^{-1}\log(2L/\delta)\right]},\\
\|W^{(\ell)}(0)\|_{\mathrm{op}}
&\le2\sqrt{2\left[2\log9+n^{-1}\log(2L/\delta)\right]}
\quad(2\le\ell\le L).
\end{aligned}                                         \tag{11}
\]

Indeed, a maximal `1/4`-separated subset of a unit sphere is a `1/4`-net
with size at most \(9^{\text{dimension}}\), by disjoint balls and volume
comparison. Approximating both unit vectors in a bilinear form gives
\(\|G\|_{\mathrm{op}}\le2\max_{u,v\text{ in nets}}|u^\top Gv|\).
Each such Gaussian bilinear form has variance equal to the entry variance.
The Gaussian exponential moment and Markov inequality give tail
\(2e^{-t^2/(2\sigma^2)}\). A union bound over the two nets and `L`
matrices gives (11). Independence across matrices is unnecessary for
that union bound.

Thus (8)--(11) are explicit in `n,d,L`, the activation envelope and the
initialization confidence. The source norm `G` and the inverse-weighted
drift `b_R` retain their actual data dependence. No bound independent of
`m` is asserted for them. Even if (5) were established uniformly, the
tail in (7) is algebraic. Taking comparison accuracy `Y/n` would generally
require a horizon of order `n`, rather than the logarithmic horizon used
by the paper. These estimates do not preserve its sharp width exponents.

## 5. Relative kernel closeness does not preserve initial source regularity

The following exact nonlinear example defeats the tempting replacement of
`b_R` by an ordinary Loewner relative bound. It is an analytic nonlinear
least-squares model, **not** the prescribed Gaussian deep architecture;
its negative conclusion is limited to that proposed abstract implication.

Use two examples, parameters \((u,v)\), labels \((\sqrt2,0)\), and
predictions

\[
f_1(u,v)=\sqrt2\,u,\qquad
f_2(u,v)=\sqrt{2\varepsilon}
          [v+\eta\log\cosh u],
\quad 0<\varepsilon\le1,\quad 0<\eta\le\tfrac14.
\]

Initialize \((u,v)=(0,0)\), so outputs vanish and `Y=1`. Write
\(g(u)=\log\cosh u\) and \(s_0=v+\eta g(u)\). The averaged square
loss and its exact gradient flow are

\[
\mathcal L=(u-1)^2+\varepsilon s_0^2,\qquad
\dot u=2(1-u)-2\varepsilon\eta\tanh(u)s_0,
\qquad \dot v=-2\varepsilon s_0.                       \tag{12}
\]

The region \(0\le u\le1\), \(v\le0\), \(s_0\ge0\) is invariant.
At `u=0` the first velocity is `2`; at `u=1` it is nonpositive; at
`v=0` the second velocity is nonpositive. On `s_0=0`,
\(\dot s_0=2\eta\tanh(u)(1-u)\ge0\). The region also has
\(-\eta g(1)\le v\le0\), hence it is compact.

Its exact normalized tangent kernel is

\[
A(u)=\begin{pmatrix}
1&\eta\sqrt\varepsilon\tanh u\\
\eta\sqrt\varepsilon\tanh u&
\varepsilon(1+\eta^2\tanh^2u)
\end{pmatrix},\qquad
A_0=\begin{pmatrix}1&0\\0&\varepsilon\end{pmatrix}.
\]

For every source exponent \(s>0\),
\(\|A_0^{-s}y\|_m=1\). Nevertheless the small-eigenvalue direction
is populated after initialization. In fact

\[
\|A_0^{-1/2}A(u)A_0^{-1/2}-I\|
\le\eta+\eta^2=:\alpha<1,
\qquad
(1-\alpha)A_0\preceq A(u)\preceq(1+\alpha)A_0.         \tag{13}
\]

This follows by separating the off-diagonal matrix of norm at most
`eta` and the nonnegative diagonal addition of norm at most `eta^2`.
The lower bound implies
\(\mathcal L(t)\le\mathcal L(0)e^{-4(1-\alpha)\varepsilon t}\)
by (1). Consequently \(u\to1\), \(s_0\to0\), and
\(v\to-\eta g(1)\). Integrating the second equation in (12) gives
the exact slow-component activity

\[
\int_0^\infty\frac{|r_2(t)|}{\sqrt2}\,dt
=\int_0^\infty\sqrt\varepsilon\,s_0(t)\,dt
=\frac{\eta\log\cosh1}{2\sqrt\varepsilon}.             \tag{14}
\]

Thus the full residual activity diverges as
\(\varepsilon\downarrow0\), despite fixed labels, initial source norms
of every order equal to `1`, uniformly bounded kernel trace, and arbitrarily
small fixed relative distortion (13). The scalar nonlinearity `g` is
holomorphic on every strictly narrower strip than
\(|\operatorname{Im}z|<\pi/2\), with bounded derivative there.
The example does not prove a lower bound on parameter path length or on
compression dimension: its whole runtime has just two coordinates.

The obstruction is specifically that relative forms allow a coupling of
size \(\sqrt\varepsilon\) between fast and slow modes. This produces a
residual of size \(\sqrt\varepsilon\) lasting time
\(\varepsilon^{-1}\). Initial label smoothness does not prevent this
transfer. Establishing its absence, sufficient suppression, or harmlessness
for the actual deep-network observable requires a separate argument.

## 6. A stronger gap-free all-time comparison estimate

An activity obstruction is not automatically a comparison obstruction.
Here is an exact comparison statement allowing noncommuting,
time-dependent kernels. Let `A(t)` and `B(t)` be continuous positive
semidefinite self-adjoint operators on the same sample Hilbert space.
Suppose

\[
|\langle u,(A(t)-B(t))v\rangle_m|
\le\zeta\langle u,B(t)u\rangle_m^{1/2}
          \langle v,A(t)v\rangle_m^{1/2}                \tag{15}
\]

for all `u,v,t`. Let \(r'=-2Ar\), \(\widehat r'=-2B\widehat r\),
with \(r(0)=\widehat r(0)=-y\). Then

\[
\sup_{t\ge0}\|\widehat r(t)-r(t)\|_m
\le\frac\zeta2\|y\|_m.                               \tag{16}
\]

Indeed, for \(e=\widehat r-r\),
\(e'=-2Be+2(A-B)r\). Set
\(a^2=\langle e,Be\rangle_m\),
\(b^2=\langle r,Ar\rangle_m\). Then

\[
\frac d{dt}\|e\|_m^2\le-4a^2+4\zeta ab
=-4(a-\zeta b/2)^2+\zeta^2b^2.
\]

The reference energy identity gives
\(\int_0^\infty b^2\,dt\le\|y\|_m^2/4\), proving (16).
For an initial discrepancy `e(0)`, the right side squared becomes
\(\|e(0)\|_m^2+\zeta^2\|y\|_m^2/4\).
If both residual limits exist, the same bound includes their endpoints;
the comparison calculation alone does not establish existence of those
limits for arbitrary time-dependent kernels.

A sufficient static relative-form version of (15) is
\(A(t),B(t)\succeq cA_0\),
\(A(t)-B(t)=A_0^{1/2}E(t)A_0^{1/2}\), and
\(\|E(t)\|\le\xi\); then Cauchy--Schwarz gives
\(\zeta=\xi/c\). No common eigenvectors or positive full spectral
gap are needed. This improves the commuting illustration in
`SPECTRAL_ROUTE.md`, as a propagation statement only.

Equation (16) controls empirical RMS training predictions. It does not
control the whole-sphere supremum, and it does not construct or compare
the underlying feature-learning parameter trajectories. Actual full-data
and weighted-subset trajectories do not automatically have two
self-adjoint residual generators in the same original empirical metric.
Condition (15) itself requires equal kernel nullspaces at every time, for
any finite `zeta`. If \(u\in\ker B\), its right side vanishes for every
`v`, so \((A-B)u=0\) by self-adjointness, and hence \(Au=0\).
If \(v\in\ker A\), the same argument using all `u` gives \(Bv=0\).
Thus \(\ker A=\ker B\). In particular a lower-rank kernel cannot satisfy
(15) against a full-rank one. Likewise, ordinary full relative-form error
below `1` against a positive definite kernel is impossible for a lower-rank
kernel. Source-restricted or observable-restricted accuracy is needed for a
useful spectral truncation.

## 7. Status and the unresolved bridge

Proved here: the frozen-source activity estimate (3), the actual nonlinear
initial-ball certificate (4)--(7), explicit envelope recurrences (8)--(11),
the nonlinear diagnostic obstruction (12)--(14), and the noncommuting
relative comparison estimate (15)--(16).

Not proved: sample-uniform initial inverse-source norms and inverse-weighted
kernel drift for the canonical Gaussian deep model; a compressed autonomous
update realizing the needed relative accuracy; whole-query comparison;
or retention of the paper's width exponents. The local certificate replaces
a future regularity hypothesis by a static one, but does not show that the
user's requested data and network assumptions satisfy that static condition.

The sharp bottleneck exposed by this route is nonlinear transfer from
initially fast label directions into weak kernel directions. Ordinary
analyticity, low label complexity, a smooth initial kernel source, and
Loewner relative stability do not jointly suppress that transfer in general
nonlinear least squares. The prescribed deep architecture could have extra
structure; that remains open here. Failure of this residual-activity route
is not an impossibility theorem for all-time sample compression.

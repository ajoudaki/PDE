# Initial data, finite jets, and the cost of finite-panel source construction

2026-10-08. Scoped theoretical source audit and construction. No training,
experiment, shared-code edit, or promotion was performed. All guarantees below
are conditional on the inherited finite-panel analytic-source, coordinate
selection, fitting, and comparison interfaces. This note does not reprove their
stochastic eventual-width event.

The existing initial-jet construction can be made fully explicit for a finite
panel, and its final metric model retains the absolute exponent-five storage
bound. It can produce the compressed temporal coefficients directly from jets
at time zero without computing a sequence of trained dense states. Its certified
jet order, however, is exponential in a constant times `log(en)^(3/2)`. The
existing near-quadratic setup instead continues the dense network across the
whole source horizon. Calling each continuation step local does not make that
computation a short-prefix initializer.

The analytic strip alone cannot certify a substantially cheaper origin-jet or
short-prefix source oracle: an explicit bounded analytic adversary gives the
same exponential order. This is an obstruction for that information model,
not an impossibility theorem for a compiler that uses the complete network
weights and vector field. A structured label-amplitude expansion remains a
concrete possible escape, with a precisely identified missing theorem.

## 1. Model, information contract, and inherited source envelope

Use the user's convention of `m` training inputs and `p` additional declared
passive inputs, and write \(N=m+p\) for their total number. The previous
finite-panel study calls this total number \(p\); every occurrence of its
panel size is therefore replaced here by \(N\). No span condition is needed;
all normalized inputs \(v_i=x_i/\sqrt d\) have unit
Euclidean norm. There are \(L\ge2\) hidden layers of width \(n\).

Let \(W^{(1)}\in\mathbb R^{n\times d}\),
\(W^{(j)}\in\mathbb R^{n\times n}\) for \(2\le j\le L\), and
\(W^{(L+1)}\in\mathbb R^n\). Define

\[
z_i^{(1)}=W^{(1)}v_i,\qquad
z_i^{(j)}=W^{(j)}h_i^{(j-1)},\qquad
h_i^{(j)}=\phi_j(z_i^{(j)}),\qquad
f_i=\frac{W^{(L+1)T}h_i^{(L)}}n.
\]

Training residuals are \(r_a=f_a-y_a\), \(a\le m\), and the loss is
\(\mathcal L=m^{-1}\sum_{a\le m}r_a^2\). With

\[
\delta_i^{(L)}=W^{(L+1)}\odot\phi_L'(z_i^{(L)}),\qquad
\delta_i^{(j)}=\phi_j'(z_i^{(j)})\odot W^{(j+1)T}\delta_i^{(j+1)},
\]

the exact dense flow has mobilities \((n,1,\ldots,1,n)\):

\[
\begin{aligned}
\dot W^{(1)}&=-\frac2m\sum_{a\le m}r_a\delta_a^{(1)}v_a^T,\\
\dot W^{(j)}&=-\frac2{mn}\sum_{a\le m}r_a\delta_a^{(j)}h_a^{(j-1)T}
\quad(2\le j\le L),\\
\dot W^{(L+1)}&=-\frac2m\sum_{a\le m}r_ah_a^{(L)}.
\end{aligned}                                                    \tag{1}
\]

Initialization has independent Gaussian first weights of variance one,
hidden weights of variance \(1/n\), and exactly zero readout. Passive inputs
have no labels, residuals, or update terms. The readout symbol in the supplied
source notes is \(w=W^{(L+1)}\), and their first matrix is \(A=W^{(1)}\).

Put \(Y=\|y\|_2/\sqrt m\), \(\lambda=\gamma/m\), and
\(\ell=\log(en)\), where \(\gamma>0\) is the population training-feature
Gram gap specified in the inherited theorem. Let \(\beta\) be its activation
envelope, including the strip width and first two derivative bounds. On the
existing full label allowance, the finite-panel source event supplies

\[
T=32\lambda^{-1}\ell,\qquad
r=\frac{\chi}{\lambda\sqrt\ell},\qquad \chi>0,                  \tag{2}
\]

and holomorphic continuation of all required source curves to a neighborhood
of \([-r,T+r]+i[-r,r]\). On that rectangle each coordinate has modulus at
most \(M=M_0\sqrt n\). The four families at a layer are

\[
h_i^{(j)},\quad W_0^{(j)}h_i^{(j-1)},\quad
\delta_i^{(j)},\quad W_0^{(j+1)T}\delta_i^{(j+1)},                \tag{3}
\]

with boundary omissions. Taking all four at every panel point gives a safe
upper count \(4N\); only training backward fields are actually necessary.
The initialized image matrices in (3) are fixed at time zero.

The explicit coefficients are
\(H_1=\max(1,b+20s)\), \(H_j=\max(1,b+10sH_{j-1})\),
\(\tau_j=sH_L(10s)^{L-j}\), and
\(M_0=10\max_j\{H_j,\tau_j\}\), where \(b\) bounds activation values
at zero and \(s\ge1\) bounds their first derivatives on the safe half-strip.
Since \(\beta\ge10,b,s\), these recurrences give the convenient loose
bound \(M_0\le\beta^{5L}\). To expose the label and gap dependence, use
the uncapped analytic radius supplied by the current source audit:
\(\chi=a/[1024(Y/\lambda)^2U_{\rm fin}]\), where \(a\) is the activation
strip width and \(U_{\rm fin}\) is its finite-query source recurrence.
The earlier source note instead caps this number at one. That smaller radius
remains an optional valid specialization; the uncapped choice is used below.
The eventual gate \(\alpha\le1\) is stated explicitly. Nothing below
spends the small-label allowance to hide the leading dependence on
\(Y,m/\gamma,a,U_{\rm fin}\).

The admissible information here is the initialized dense arrays, training
data and labels, declared passive inputs, and a specified activation value/jet
backend. A claim about cheap setup must also count operations, transient
memory, and derivative generation. Merely observing that uniqueness makes
future training a function of these inputs does not establish cheap setup.
The case \(Y=0\) has identically zero predictor and is handled separately.

## 2. Explicit initial-jet compiler preserving exponent-five storage

### Temporal coefficients and a finite quadrature

Fix one vector source \(u(t)\) from (3), and put

\[
g(\theta)=u\left(\frac T2(1+\cos\theta)\right),\qquad
\alpha=\frac r{4T}=\frac\chi{128\ell^{3/2}}.
\]

Assume the eventual gate \(\alpha\le1\). The indicated complex strip maps
inside the source rectangle. Its Fourier
coefficients \(c_k\) obey \(\|c_k\|_\infty\le M e^{-\alpha|k|}\), by
shifting the integration contour vertically. Evenness and reality give
\(c_{-k}=c_k\in\mathbb R^n\). For a supplied source tolerance
\(0<\eta_s\le1\), put \(\varepsilon=\eta_s\) and choose

\[
K=\left\lceil\alpha^{-1}
             \log\frac{64M}{\varepsilon\alpha}\right\rceil .   \tag{4}
\]

The tail of \(c_0+2\sum_{k=1}^Kc_k\cos(k\theta)\) is at most
\(4M\alpha^{-1}e^{-\alpha(K+1)}\le\varepsilon/16\).

Here is an explicit finite replacement for its integrals, avoiding any
uncounted quadrature oracle. Choose an integer

\[
N_t\ge\max\left\{2K+1,\ \frac{\log2}{\alpha},\
 K+\frac1\alpha\log\frac{128M(2K+1)}\varepsilon\right\}.       \tag{5}
\]

Use the equally spaced angles \(2\pi j/N_t\) and weights \(1/N_t\).
Absolute Fourier convergence proves the discrete coefficient identity
\(c_k^{\mathrm{disc}}=\sum_{s\in\mathbb Z}c_{k+sN_t}\). Thus, for
\(0\le k\le K\),

\[
\|c_k^{\mathrm{disc}}-c_k\|_\infty
\le\frac{2M e^{-\alpha(N_t-K)}}{1-e^{-\alpha N_t}}
\le4M e^{-\alpha(N_t-K)}.
\]

Their total reconstructed error is at most \(\varepsilon/32\). Approximate
each nodal source value with coordinate error at most

\[
\eta=\frac\varepsilon{16(2K+1)}.                              \tag{6}
\]

The positive quadrature weights give coefficient error at most \(\eta\),
and total reconstructed error at most \((2K+1)\eta=\varepsilon/16\).
The sum of these three errors is less than \(\varepsilon\). Computing the
real cosine sums directly gives real source coefficients. A common symmetric
rule, common jets, and identical scalar operations preserve exact initialized
forward/reverse image relations.

### Reconstructing the quadrature only from zero-time jets

The appendix's origin-jet map specializes as follows. Define

\[
A=\frac{\pi T}{8r},\quad b_0=\tanh A,\quad
b_1=\tanh(A+\pi/4),\quad \vartheta=b_0/b_1,\quad
\psi(\xi)=\frac{\xi-\vartheta}{1-\vartheta\xi},
\]
\[
\mathfrak t(\xi)=\frac T2+
\frac{2r}{\pi}\log\frac{1+b_1\psi(\xi)}{1-b_1\psi(\xi)},\qquad
\xi_* =\frac{2\vartheta}{1+\vartheta^2}.                       \tag{7}
\]

The disk automorphism maps the unit disk into itself. For \(|w|<b_1\),
the logarithm has imaginary part smaller than \(\pi/2\), and real part
bounded in modulus by \(2\operatorname{arctanh}b_1\). Hence (7) maps into
the source rectangle, satisfies \(\mathfrak t(0)=0\), and maps
\([0,\xi_*]\) monotonically onto \([0,T]\). Its branch is fixed by
continuity from real \(\xi=0\).

For normalized jets \(u_j=\partial_t^ju(0)/j!\), define

\[
a_j=\sum_{k=0}^j u_k[\xi^j]\mathfrak t(\xi)^k.                 \tag{8}
\]

Because \(\mathfrak t(0)=0\), only jets through order \(j\) enter.
The composed analytic source is bounded by \(M\) on the unit disk, so
\(\|a_j\|_\infty\le M\). A sufficient explicit common jet cutoff is

\[
J=\left\lceil
\frac{\log\{M/[\eta(1-\xi_*)]\}}{-\log\xi_*}
\right\rceil .                                                \tag{9}
\]

Then \(\sum_{j=0}^Ja_j\xi^j\) has coordinate error at most \(\eta\)
for every \(0\le\xi\le\xi_*\), by summing its geometric tail.

The jets themselves require no positive-time dense states. Write the dense
ODE as \(\dot\Theta=F(\Theta)\), where \(\Theta\) collects the arrays
in (1). Its normalized coefficients satisfy the triangular recurrence

\[
\Theta_{j+1}=\frac1{j+1}[t^j]
          F\left(\sum_{k=0}^j\Theta_kt^k\right).                \tag{10}
\]

Each step uses already computed coefficients; the network forward/backward
recursions and scalar activation compositions then give the source jets.
Every activation derivative is evaluated at an initialized preactivation.
Ordinary analyticity proves that these formal coefficients agree with the
local solution derivatives; the explicit continuation supplies their use
outside the initial disk.

One can avoid even materializing approximate future source values. Let
\(\xi_l\) correspond under (7) to the predetermined quadrature time at
angle \(2\pi l/N_t\), and let \(\omega_{kl}\) contain that cosine weight
and normalization. Form scalar arrays

\[
E_{kj}=\sum_l\omega_{kl}\xi_l^j,\qquad
B_{ks}=\sum_{j=0}^JE_{kj}[\xi^j]\mathfrak t(\xi)^s.             \tag{11}
\]

The actual retained coefficient vector is simply
\(\sum_{s=0}^JB_{ks}u_s\). Thus source assembly is a fixed scalar linear
map of zero-time jets. This is a literal initialization-only construction;
it does not integrate dense states through the interval. Its high algebraic
cost remains charged below.

Since differentiation and every scalar operation in (8),(11) commute with
\(W_0^{(j)}\) and its transpose, a common computation gives exact paired
coefficient identities. Each of the four analytic families has its own
coordinate bound \(M\), so their errors are certified separately rather
than multiplying a coordinate error by a potentially width-dependent
matrix infinity norm.

### Retained dimension and unchanged prediction guarantee

The number of coefficient vectors is governed by \(K\), not by \(J\).
Adding the exact initial training features and their images, the first matrix
columns, and the constant vector gives

\[
R=4N(K+1)+2m+d+1.
\]

For the specialization \(\eta_s=1/n\), under
\(\log_+(8192M_0/\chi)\le\ell\), \(\alpha\le1\), and
\(\ell/\alpha\ge1\), (4) yields

\[
K+1\le768\chi^{-1}\ell^{5/2},\qquad
R\le3072N\chi^{-1}\ell^{5/2}+2m+d+1.                          \tag{12}
\]

Apply the existing exact-metric selector to these finite spaces, with at
most \(9R\) selected coordinates per layer, then use its corrected-readout
autonomous optimizer. This changes only coefficient provenance, so its
source tolerance and all comparison hypotheses are unchanged. With all jets,
dense coefficients, projections and setup arrays discarded, the retained
coordinate bound, without assuming \(d\le m\), is

\[
2048(L+1)R^2+16N(d+1)
\quad\text{plus the fixed activation/runtime program}.          \tag{13}
\]

Here \(R\) is the exact expression above (12). For general \(\eta_s\),
this is
\(O((L+1)N^2\chi^{-2}\ell^3
\log^2[64M/(\eta_s\alpha)]+(L+1)(m+d+1)^2+N(d+1))\).
For polynomial source accuracy, including \(\eta_s=1/n\), it has absolute
logarithmic exponent five. In particular its leading coefficient retains
\(\chi^{-2}=2^{20}(Y/\lambda)^4(U_{\rm fin}/a)^2\). Additional eventual
width gates may absorb the fixed additive dimension term, but it is not
silently bounded by \(N\) here.

For \(\eta_s=1/n\) on the original simple label allowance, the inherited
all-time prediction guarantee is

\[
\sup_{t\in[0,\infty]}\max_{i\le N}|f_C(t,x_i)-f_n(t,x_i)|
\le10\beta^{40L}\frac Y\lambda
          (1+\lambda^{-1/2})\frac{e^{2\sqrt\ell}}n.             \tag{14}
\]

The full label allowance has its original larger comparison coefficient
\(C\beta^{42L}(Y/\lambda)\max(1,\lambda^{-1/2})
(1+\sqrt\ell)e^{64\sqrt\ell}/n\), using the current audited conservative
exponent, without changing the exponent five. For a general supplied
\(\eta_s\), use the source-to-prediction bound and horizon-tail budget of
the accompanying panel theorem; (14) specifically records its original
\(1/n\) specialization and must not omit the tail when \(\eta_s\) is smaller.
For \(m\ge2,Y>0\), intersecting with the inherited independent-dense lower
bound \(c_{\phi,L,\delta}Y\sqrt\gamma/(\sqrt n\,\ell^{5/2})\)
gives a compression-error/dense-variability ratio tending to zero. This is
the whole-trajectory panel norm, not pointwise or fitted-training-endpoint
relative error. No probability independence between the two events is needed.

## 3. Explicit setup order and arithmetic dependence

Write \(E=e^{-2A}\) and \(q=e^{-\pi/2}\). Direct subtraction of the
two hyperbolic tangents gives

\[
1-\vartheta=\frac{2(1-q)E}{(1+E)(1-qE)},\qquad
1-\xi_* =\frac{(1-\vartheta)^2}{1+\vartheta^2}.                 \tag{15}
\]

Under the additional eventual gate \(T/r=32\chi^{-1}\ell^{3/2}\ge1\),
universal positive constants
bound \(1-\xi_*\) above and below by constant multiples of
\(e^{-\pi T/(2r)}\). Also \(-\log\xi_*\) is comparable to
\(1-\xi_*\). Therefore the sufficient cutoff (9) has order

\[
J=O\left(
e^{16\pi\chi^{-1}\ell^{3/2}}
\left[\log\frac{M(2K+1)}\varepsilon+
                       \chi^{-1}\ell^{3/2}\right]\right).      \tag{16}
\]

Equations (2),(4),(6),(9) specify every constant before this asymptotic
display. The common explicit factor \(\lambda^{-1}\) cancels in \(T/r\),
but the uncapped \(\chi^{-1}=1024(Ym/\gamma)^2U_{\rm fin}/a\) retains
the sample/gap and label dependence. In particular the exponent in (16)
is \(16384\pi(Ym/\gamma)^2(U_{\rm fin}/a)\ell^{3/2}\).
Activation/depth dependence is explicit through
\(M_0\le\beta^{5L}\), \(U_{\rm fin}/a\), and the activation backend.
There is no additional panel-size or input-dimension factor in that
exponent. For fixed parameters this
jet order at \(\eta_s=1/n\) is superpolynomial in \(n\), since
\(\log J/\log n\) grows like a positive multiple of \(\sqrt{\log n}\).

For a concrete conservative execution bound put
\(P=nd+(L-1)n^2+n\). Let \(\mathcal A_\phi(J)\) and
\(\mathcal B_\phi(J)\) count one online scalar composition with both
\(\phi,\phi'\), including generation of the needed derivatives and its
workspace. A materialized dense coefficient recursion has source-production
work bounded by

\[
\begin{aligned}
O\big(&P(m+N)(J+1)^2
 +Ln(m+N)\mathcal A_\phi(J)\\
 &+N_t(K+1)(J+1)+(K+1)(J+1)^2\\
 &+LnN(K+1)(J+1)\big).                                      \tag{17}
\end{aligned}
\]

The first line is online series propagation: summing coefficient convolutions
over degrees costs \(O(J^2)\) per scalar product. The second compiles (11),
using the appendix's two-term differential recurrence for powers of the
logarithmic map, and the third applies it to the source arrays. One sufficient
peak-memory bound is

\[
O\big(P(J+1)+Ln(m+N)[J+1+\mathcal B_\phi(J)]
 +(K+1)(J+1)+LnN(K+1)+Nd\big).                                \tag{18}
\]

This loose bound may stream passive queries and reduce workspace. The
appendix's factored weight jets reduce matrix-copy cost further, but cannot
remove the required order (16) from this reconstruction method. Selection and
metric assembly have additional finite costs depending on \(n,L,R\); (17)
is explicitly source-production cost. A sufficient classical arithmetic
inventory for the remaining operations is as follows: dense basis whitening
costs \(O(LnR^2+LR^3)\); \(9R\) BSS selection steps with naive row scoring
and matrix inverses cost \(O(L[nR^3+R^4])\); selected-mixer assembly by
ordinary dense actions costs \(O(L[n^2R+nR^2+R^3])\). Their additional peak
storage is \(O(P+LnR+LR^2+Nd)\). These are sufficient upper bounds, not
optimality claims. They do not make (16) a cheap setup theorem.

For the scalar conformal and quadrature constants, (17) uses exact-real
unit-cost evaluation of elementary functions (including logarithm, hyperbolic
tangent, cosine, and the inverse-node map). This is an explicit additional
arithmetic convention, not supplied by activation analyticity. If each such
evaluation instead costs at most \(A_{\rm elem}\) operations and
\(W_{\rm elem}\) additional words at the chosen precision, add
\(O((N_t+1)A_{\rm elem})\) work and \(O(W_{\rm elem})\) peak workspace.
The inverse nodes are obtained directly: for a quadrature time \(t_l\),
set \(w_l=b_1^{-1}\tanh(\pi(t_l-T/2)/(4r))\) and
\(\xi_l=(w_l+\vartheta)/(1+\vartheta w_l)\). Fourier cosines for each
node can be generated from its first cosine by the two-term recurrence.
No precision-independent bit complexity is claimed by this convention.

For familiar finitely represented activations, scalar differential identities
can make \(\mathcal A_\phi(J)\) polynomial in \(J\). For an unspecified
abstract holomorphic activation, computability and derivative costs are extra
inputs. Counts (13),(17),(18) use real arithmetic. They do not establish bit
complexity or numerical stability of high-order jets, conformal coefficients,
or selected metrics.

## 4. Why the analytic envelope cannot justify cheap local extrapolation

This section makes a restricted, deterministic information claim. It applies
to algorithms whose only information about an arbitrary bounded analytic
source is a finite collection of source values or derivatives. It does not
apply to every algorithm given the full neural-network weights and ODE.

For \(|\operatorname{Im}t|\le r\), set
\(b(t)=\tanh(\pi t/(4r))\). Its poles have imaginary part at least
\(2r\), and

\[
|\tanh(x+iy)|^2
 =\frac{\cosh(2x)-\cos(2y)}{\cosh(2x)+\cos(2y)}\le1
\quad\text{when }|y|\le\pi/4.
\]

The two sources \(g_\pm(t)=\pm M b(t)^{J+1}\) are holomorphic on a
neighborhood of the closed source rectangle, bounded there by \(M\), and
have identical derivatives through order \(J\) at zero. Any reconstruction
from these derivatives returns the same value for both. By the triangle
inequality, at least one of its endpoint errors is at least
\(M b(T)^{J+1}\). A uniform error bound \(\varepsilon<M\) therefore
requires

\[
J+1\ge
\frac{\log(M/\varepsilon)}{-\log\tanh(\pi T/(4r))}
\sim\frac12 e^{\pi T/(2r)}\log(M/\varepsilon).                 \tag{19}
\]

This matches the exponential aspect-ratio dependence of (16), up to
logarithmic factors. Thus changing only the scalar continuation formula
cannot turn the inherited strip hypothesis into a polylogarithmic origin-jet
order theorem for arbitrary bounded analytic sources.

The same argument covers finite exact information on a short prefix. Suppose
all query times \(t_a\) lie in \([0,\tau]\), \(\tau<T\), and at time
\(t_a\) the method receives derivatives through order \(q_a-1\). Define
\(Q=\sum_a q_a\). The product

\[
B(t)=\prod_a\tanh\left(\frac{\pi(t-t_a)}{4r}\right)^{q_a}
\]

has all those derivatives zero, is bounded by one on the strip, and satisfies

\[
B(T)\ge\tanh\left(\frac{\pi(T-\tau)}{4r}\right)^Q.
\]

The adversaries \(\pm MB\) force

\[
Q\ge
\frac{\log(M/\varepsilon)}
 {-\log\tanh(\pi(T-\tau)/(4r))}.                              \tag{20}
\]

For adaptive deterministic queries, run the algorithm on zero answers, then
choose this product at the finite queried nodes. Both adversaries generate
the same query transcript. Exact knowledge of an entire nonempty real
interval is a different, infinite-information object and is not excluded by
(20); uniqueness of analytic continuation from that object is compatible
with the bound.

These analytic sources have not been realized as trajectories of the
specified random neural network. They also do not impose the network's full
residual, parity, parameter-sharing, and all-time fitting constraints. Therefore
(19),(20) refute an inference from the strip alone, not initialization-only
neural compression or every use of network structure. In particular they
cannot justify describing the requested cheap compiler as impossible.

## 5. What strictly local production already certifies

At time zero the disk \(|t|\le r\) lies in the analytic rectangle. Direct
Taylor truncation through order \(q\) gives, for any \(0\le\tau<r\),

\[
\sup_{0\le t\le\tau}
\left\|u(t)-\sum_{j=0}^q u_jt^j\right\|_\infty
\le M\frac{(\tau/r)^{q+1}}{1-\tau/r}.                         \tag{21}
\]

For \(\tau=r/2\), degree
\(q\ge\lceil\log_2(2M/\varepsilon)\rceil\) is sufficient.
At \(\varepsilon=1/n\) this is
\(O(\log n+L\log\beta)\). Initial jets and initialized image pairs then
give local source dimension at most \(4N(q+1)+2m+d+1\), using
\(O(LN^2\log^2 n)\) retained coordinate scale at fixed parameters.
The certified time window is only
\(\chi m/(2\gamma\sqrt\ell)\). This is a local source theorem, not
the requested all-time prediction theorem. No endpoint or all-time comparison
is claimed from (21).

For a larger but fixed physical prefix \(\tau=O(m/\gamma)\), replacing
\(T\) by \(\tau\) in (7)--(9) gives jet order
\(\exp(O(\chi^{-1}\sqrt\ell))\) times logarithmic factors, hence
\(n^{o(1)}\) at fixed parameters. Thus genuinely initial algebra can certify
a nonvanishing short interval within near-quadratic source arithmetic when
the activation backend is polynomial. This still leaves almost all of the
\(T=32(m/\gamma)\ell\) source horizon uncertified.

A tiny local rollout can supply the same local sources and may be much
easier numerically. It changes neither the unresolved far-time source defect
nor (20)'s implication under a generic analytic-source oracle model. The
existing `LOCAL_CONTINUATION_SETUP.md` instead uses
\(O(\ell^{3/2})\) restarted dense Taylor panels of degree \(O(\ell)\)
covering all of \([0,T]\). Its near-quadratic arithmetic result is useful,
but that full-interval reconstruction does not meet a short-prefix contract.

## 6. A structured escape and its exact missing bridge

The strongest explicit initialization-only alternative found in the permitted
source packet is expansion in a scalar label amplitude \(\zeta\), replacing
\(y\) by \(\zeta y\) while leaving all initialized weights fixed.
At \(\zeta=0\), the zero readout makes every parameter stationary.
The transformation \((\zeta,W^{(L+1)},y-f)\mapsto
(-\zeta,-W^{(L+1)},-(y-f))\) preserves the equations, so hidden parameters
and forward sources are even in amplitude and backward sources are odd.

If \(H_0\) collects the initialized top training features and
\(G_0=2H_0^TH_0/(mn)\), the order-one deficit coefficient is exactly
\(e^{-G_0t}y\). Every subsequent amplitude coefficient solves a fixed linear
equation forced by lower amplitude orders. Its scalar time dependence is a
finite combination of \(t^k e^{-(\nu_1\omega_1+\cdots+\nu_m\omega_m)t}\),
where \(\omega_i>0\) are the eigenvalues of \(G_0\). Alternatively a
bivariate time/amplitude recurrence at \((t,\zeta)=(0,0)\) computes those
coefficients without eigenvalue-separation assumptions or positive-time dense
training. These are finite-order identities, not convergence at \(\zeta=1\).

A sufficient new theorem would give, uniformly for real \(t\in[0,T]\)
and all declared panel inputs, holomorphic dependence of every source on
\(\zeta\) in

\[
[-b_n,1+b_n]+i[-b_n,b_n],\qquad
|u_i(t;\zeta)|\le Cn^A,                                      \tag{22}
\]

with \(b_n\ge c/\sqrt\ell\). Applying the same conformal reconstruction
in amplitude, now across an interval of length one, needs only
\(\exp(O(\sqrt\ell))=n^{o(1)}\) amplitude order at polynomial accuracy.
The bivariate calculation in `POLYNOMIAL_SETUP_INITIAL_ROUTE.md` then has
\(n^{2+o(1)}\) source arithmetic for fixed structural parameters and a
polynomial-cost activation backend. The finite-panel quadrature (5) already
has polylogarithmic node count, so no spatial quadrature remains. The selected
source rank and retained metric inventory stay governed by (12),(13).
A weaker radius \(c/\ell\) would give polynomial, but not necessarily
near-quadratic, source-production work.

The missing part is (22) for the complete admitted nonlinear network class
and original label allowance. The physical-time strip does not imply it.
Real fitting for each real amplitude does not bound singularities in complex
amplitude. A generic parameter-to-neuron estimate loses \(\sqrt n\), yielding
an inadequate radius. Proving the desired tube requires a reachable-direction
coordinate estimate for amplitude variations, with control of the complex
training Gram and activation strip. Positivity of the real Gram cannot be
used after replacing real variables by complex ones with algebraic transposes.

A short prefix reducing the residual to a power of \(1/\log n\) might help
an amplitude expansion around its stationary fitted-label anchor. It introduces
the full tangent Gram and loses the zero-readout parity. More seriously, the
trained anchor and its centered labels depend on all Gaussian rows: omitted-row
independence must be proved through that prefix, not declared anew. The
permitted source packet leaves both this cavity argument and the needed
complex-amplitude coordinate estimate open. This note does not claim to close
them.

## 7. Implementation audit and defensible conclusion

In `paper/figures/capture_trajectory.py`, `deep_rollout_sources` (line 3730)
concatenates training and calibration inputs, constructs observation nodes
through the supplied full horizon, and calls `integrate` on a disposable
float32 `DeepDense`. It fits degree-eight temporal polynomials and applies a
randomized low-rank truncation. The reported holdout errors concern measured
source nodes, and it explicitly returns `source_certificate=False`. Deleting
the teacher afterward reduces retained storage but does not make source
production local. The routine deliberately omits scored query inputs; its
empirical test scope is therefore different from a theorem for a declared
panel containing every scored input.

`DeepHarmonic` (line 205) accepts source columns, adds their initialized forward
and reverse images, builds the metric optimizer, and discards setup arrays.
That runtime distinction is sound; it does not supply a new provenance or
approximation certificate for the provided source columns.

`finite_panel_initial_jets` (line 3248) is a genuine zero-time implementation
of order-two jets, using zero initial readout. It supplies initialized features
and half their second derivatives, plus first backward derivatives and half
their second derivatives. It is specialized to the two-hidden-layer tanh
`Dense` state. It does not implement arbitrary-depth `DeepDense` jets or
prove an all-time source certificate. Increasing its fixed order, using Padé
continuation, or fitting more local snapshots may be sensible empirical
proposals; none alone supplies the missing uniform source estimate.

The current strongest proved implication, conditional on the stated source
and runtime interfaces, is thus (4)--(14): finite
zero-time compilation with exponent-five retained storage and the inherited
dense-variability calibration, at the explicit expensive order (9),(16).
Equations (19),(20) explain why analyticity alone cannot certify the desired
cheap local upgrade. Equations (21),(22) separate a proved cheap local source
construction from a concrete all-time structural route that still needs a
new theorem. No neural-network impossibility theorem, efficient all-time
zero-time compiler, or certified short-prefix extrapolator is established.

Scientific inputs were limited to the supervisor-assigned maintained notation,
`finite_panel_absolute_compression_20261005/PANEL_SOURCE.md` and `RESULT.md`,
the directly relevant origin-jet and execution sections of
`paper/integrated_appendix.tex`, `LOCAL_CONTINUATION_SETUP.md`,
`POLYNOMIAL_SETUP_INITIAL_ROUTE.md` and relevant supplied checks in the approved
integrated study, and the specified source-generation/runtime code. The
rigorous-math, conjecture-research, canonical-notation and neural-response
instructions were applied. No other study or frozen archive was consulted.

## 8. Focused follow-up: residual cancellation in the label sensitivity

This follow-up tests whether small labels and a positive training Gram already
imply the missing complex amplitude tube. It establishes a bound on real
parameter sensitivity uniform in physical time by cancelling persistent label
forcing. A further quantitative complex-neighborhood argument gives a
certificate much narrower than the logarithmic width needed by (22).
Thus the parameter-norm part closes, while the neuron-coordinate part does not.

Fix a real amplitude \(0\le\sigma\le1\) and the real trajectory trained on
\(\sigma y\). Use normalized parameters
\(\theta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},W^{(L+1)}/\sqrt n)\).
Define normalized training outputs, labels, Jacobian and deficit by

\[
F(\theta)=\frac{(f_1(\theta),\ldots,f_m(\theta))^T}{\sqrt m},\quad
v=\frac y{\sqrt m},\quad J=D_\theta F,\quad
c=\sigma v-F(\theta),\quad Q=JJ^T .
\]

Here \(J\) is \(m\)-by-\(P\), \(\|v\|_2=Y\), and the exact flow is
\(\dot\theta=2J^Tc\), \(\dot c=-2Qc\). Suppose its real source/fitting
bounds give

\[
Q\succeq\mu I,\quad \|J\|_{\rm op}\le G,\quad
\|D_\theta J[u]\|_{\rm op}\le H_*\|u\|_2,\quad
\int_0^\infty\|c(t)\|_2\,dt\le\frac{\sigma Y}{2\mu}.             \tag{23}
\]

One may use \(\mu=\lambda/4\). The endpoint-gradient estimate in
POLYNOMIAL_SETUP_ODE_ROUTE.md (3),(5), differentiated at the real endpoint,
supplies \(G\) and \(H_*=J(M_n)\) in that note's notation, with
\(M_n=2K_{\rm src}(16Y/\lambda)\sqrt\ell\). Its recurrence is affine in
\(M_n\), so these constants are explicit in its activation/depth recurrences,
\(Y/\lambda\) and \(\ell\). No passive Gram gap is used.

Let \(U=\partial_\sigma\theta\), with \(U(0)=0\). Differentiation gives

\[
\dot U=-2J^TJU+2BU+2J^Tv,\qquad
B=\sum_{a=1}^m c_aD_\theta^2F_a .                              \tag{24}
\]

For unit parameter vectors \(u,w\), the identity
\(u^TBw=c^T(DJ[w])u\) proves \(\|B\|_{\rm op}\le H_*\|c\|_2\).
The forcing \(2J^Tv\) need not be integrable. Instead introduce the current
training right inverse and its label lift:

\[
A=J^TQ^{-1},\qquad V=Av,\qquad Z=U-V .
\]

The singular values of \(J\) give \(\|A\|_{\rm op}\le\mu^{-1/2}\),
\(JV=v\), and \(\|V\|_2\le Y/\sqrt\mu\). Differentiating gives exactly

\[
\dot A=(I-AJ)\dot J^TQ^{-1}-A\dot JA .
\]

Because \(J\) is real and has full row rank, \(I-AJ\) is an orthogonal
projection. Thus \(\|\dot A\|\le2\|\dot J\|/\mu\). The identity
\(\dot J=DJ[2J^Tc]\) then yields
\(\|\dot V\|_2\le4H_*GY\|c\|_2/\mu\). Substitution in (24) cancels the
label forcing:

\[
\dot Z=-2J^TJZ+2B(Z+V)-\dot V .                               \tag{25}
\]

The first term has nonpositive real energy. Differentiating \(\|Z\|_2\),
using upper right derivatives at zero, gives

\[
\frac d{dt}\|Z\|_2
\le2H_*\|c\|_2\|Z\|_2+
\left(\frac{2H_*Y}{\sqrt\mu}+\frac{4H_*GY}{\mu}\right)\|c\|_2 .
\]

Since \(Z(0)=-V(0)\), multiplying by the scalar integrating factor and
using (23) proves

\[
\sup_{t\ge0}\|U(t)\|_2\le C_U,\qquad
C_U=\frac Y{\sqrt\mu}
+e^{H_*Y/\mu}\left[
\frac Y{\sqrt\mu}+\frac{H_*Y^2}{\mu^{3/2}}
+\frac{2H_*GY^2}{\mu^2}\right].                               \tag{26}
\]

This bound has no physical horizon. It does not freeze the Jacobian or
neglect hidden updates. In particular, the kernel of \(J\) can be large;
its directions are not made coercive by the training Gram, and the
residual-weighted curvature \(B\) remains.

### An explicit complex neighborhood and its insufficient width

Use the complex parameter balls constructed in LOCAL_CONTINUATION_SETUP.md
(14), centered at the real reference \(\theta(t)\). Their radius can be
taken as

\[
b_n=\min\left\{\frac14,\frac{a}{16\sqrt nP_*},
                      \frac1{\sqrt n\kappa_*(M_n)}\right\}.    \tag{27}
\]

The recurrences for \(P_*,\kappa_*\) are that note's (6),(7), with operator
caps eleven and readout allowance \(1+16(Y/\lambda)H_L\). The balls remain
inside the safe activation strip and have carrier bound \(M_n+1\).
Endpoint subtraction gives a pairwise complex Lipschitz bound \(L_n\)
for the parameter vector field, and a bound \(H_t\) on \(DJ\) throughout
the same balls. At fixed parameters both are \(O(\sqrt\ell)\); one can
use that note's explicit gradient recurrence at carrier bound \(M_n+1\).

Write
\(\mathcal F_\zeta(\theta)=2J(\theta)^T[\zeta v-F(\theta)]\).
Its derivative \(D\mathcal F_\sigma\) is holomorphic and bounded by \(L_n\)
on each full ball. Applying Cauchy's formula in any unit parameter direction
on a circle of radius \(b_n/2\) shows that its second parameter derivative
on the half-radius ball is bounded by \(2L_n/b_n\). Its Taylor remainder
therefore has norm at most \(D_n\|E\|_2^2\), with \(D_n=L_n/b_n\).

For complex \(\delta\), let
\(E(t)=\theta(t;\sigma+\delta)-\theta(t;\sigma)\). Its linearized equation
is (24) with forcing \(2\delta J^Tv\); its remainder is bounded by

\[
D_n\|E\|_2^2+2|\delta|H_tY\|E\|_2 .                           \tag{28}
\]

The reference linear generator \(-2J^TJ+2B\) is real symmetric at each
time. Its propagator, also on complex vectors, has norm at most \(e^{A_n}\),
where \(A_n=H_*Y/\mu\), by integrating \(2H_*\|c\|_2\).
The linear forced solution is exactly \(\delta U\).
Duhamel's formula and (26),(28) exclude a first crossing of
\(\sup_{s\le t}\|E(s)\|_2=2|\delta|C_U\) when

\[
|\delta|<b_\zeta:=
\min\left\{\frac12,\frac{b_n}{4C_U},
 \frac1{8e^{A_n}T(D_nC_U+H_tY)}\right\}.                      \tag{29}
\]

Indeed before a crossing the nonlinear contribution is at most
\(4e^{A_n}T|\delta|^2C_U(D_nC_U+H_tY)<|\delta|C_U/2\), while the linear
term is at most \(|\delta|C_U\). The middle condition keeps the solution
inside the half-radius ball. Local holomorphic existence and dependence on
\(\zeta\) follow by contraction of the finite-dimensional integral equation.
The strict tube bound prevents finite-time exit and patches those solutions
uniquely through \([0,T]\). This establishes a holomorphic amplitude disk
with the source-field bounds supplied by the safe parameter tube.

At fixed positive task parameters, the displayed recurrences imply

\[
b_n^{-1}=O(\sqrt{n\ell}),\quad
D_n=O(\sqrt n\,\ell),\quad A_n=O(\sqrt\ell),\quad
b_\zeta^{-1}=O\!\left(\sqrt n\,\operatorname{poly}(\ell)
                                         e^{C\sqrt\ell}\right). \tag{30}
\]

This is a sufficient narrow-neighborhood certificate, not an upper bound
on the true analytic radius. A full rectangle around \([0,1]\) additionally
requires the real bounds (23) and carriers uniformly along that amplitude
family. Such a uniform probability event is not supplied by a theorem for
one fixed label vector. The disk result at one fixed \(\sigma\) only uses
the event for that trajectory.

The desired radius is \(c/\sqrt\ell\). Even removing the exponential in
(26) would leave the \(\sqrt n\) loss in (27), since the available forward
perturbation estimate is

\[
\max_{a,j,i}|D_\theta z_{a,i}^{(j)}U|
\le\sqrt nP_*\|U\|_2 .
\]

Moreover \(H_*Y/\mu\) has the form
\(C_0Y/\lambda+C_1(Y/\lambda)^2\sqrt\ell\). A fixed small-label cap makes
these coefficients small but does not keep this expression bounded for
arbitrarily large widths. Imposing that would add a width-dependent label
restriction and change the task.

Using just the safe radius (29), amplitude conformal reconstruction has a
sufficient order exponential in \(1/b_\zeta\), with safe upper bound
\(\exp[O(\sqrt n\,\operatorname{poly}(\ell)e^{C\sqrt\ell})]\) at polynomial
accuracy. This is a poor upper bound, not a lower bound on network computation.
It does not give cheap setup. If the stronger radius \(c/\sqrt\ell\) were
proved, the existing bivariate scheme would instead use amplitude order
\(Q=n^{o(1)}\), time order
\(O(Q\ell+\log(1/\eta_s))=n^{o(1)}\) at polynomial source accuracy,
and \(n^{2+o(1)}\) initial source arithmetic, plus the selector/metric costs
specified in Section 3.

The focused route therefore closes a useful sensitivity calculation and a
finite complex-neighborhood construction. It leaves a precise outstanding
estimate: control \(D_\theta z\,U\) along the reachable amplitude family
without the generic \(\sqrt n\) conversion, while preserving the Gaussian
dependence structure and complex fitting. No claim that such an estimate is
false, or that the efficient initialization compiler is impossible, follows.

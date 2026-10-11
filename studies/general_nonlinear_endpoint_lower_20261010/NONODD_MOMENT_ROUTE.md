# Training coordinate moments for the nonodd endpoint route

2026-10-11. Scoped derivation from `paper/compact.tex`, the complete
`paper/compact_fitting.tex`, the complete `paper/compact_foundations.tex`,
and this study's `PRODUCT_QUERY_ROUTE.md`. No experiment or manuscript edit.
The rigorous-math and canonical-notation instructions and the neural-network
reference were applied. This note extracts a stronger intermediate consequence
of the current source proof; it does not assert a new independent proof of
that source proof or an endpoint lower theorem.

The training readout fourth moment is available, including for unbounded and
nonodd activations. The relevant input is the source proof's empirical
exponential budget, not its public coordinate maximum. The resulting scale is
`Y/(gamma/m)`, not the smaller readout energy scale `Y/sqrt(gamma/m)`.
The distinction matters for the proposed arbitrary-depth scalar comparison.

## 1. Model, event, and the source-proof input

Let there be \(L\ge2\) hidden layers of width \(n\), normalized training inputs
\(v_a\in\mathbb R^d\) with \(\|v_a\|=1\), and \(m\ge2\) labels. The forward
map, residuals and loss are

\[
z_a^{(1)}=W^{(1)}v_a,\qquad
z_a^{(j)}=W^{(j)}h_a^{(j-1)},\qquad
h_a^{(j)}=\phi_j(z_a^{(j)}),\qquad
f_a=n^{-1}w^\top h_a^{(L)},
\quad r_a=f_a-y_a,\quad \mathcal L=m^{-1}\sum_a r_a^2.
\]

Here \(W^{(1)}\in\mathbb R^{n\times d}\), \(W^{(j)}\in\mathbb R^{n\times n}\)
for \(j\ge2\), and \(w\in\mathbb R^n\). Define the backward carriers and
responses by

\[
k_a^{(L)}=w,\qquad
\delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot k_a^{(j)},\qquad
k_a^{(j)}=W^{(j+1)\top}\delta_a^{(j+1)}\quad(j<L).
\]

The dynamics are exactly

\[
\dot w=-\frac2m\sum_a r_a h_a^{(L)},\qquad
\dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,
\qquad
\dot W^{(j)}=-\frac2{nm}\sum_a r_a
                 \delta_a^{(j)}h_a^{(j-1)\top}\quad(j\ge2).
\]

The first-layer initialization has independent \(N(0,1)\) entries, hidden
matrices have independent \(N(0,1/n)\) entries, blocks are independent, and
\(w(0)=0\). Assume precisely the strip assumptions and the positive population
Gram gap \(\gamma\) of `compact.tex`. Put

\[
\lambda=\gamma/m\le1,\qquad Y=\|y\|/\sqrt m,
\qquad \varepsilon=Y/\lambda,
\qquad 0<\varepsilon\le\beta^{-30L}.
\]

Write \(\rho(t)=\|r(t)\|/\sqrt m\) for the residual RMS.

The symbol \(S_0=16\varepsilon\) below is the scalar denoted \(S\) in the
source proof; it is unrelated to the training-input span. Set

\[
T=32\log(en)/\lambda,\qquad
\mathcal B=1024e^2L,
\qquad \eta_*=(1024C_{\rm abs}W_G)^{-1}.
\]

The last equality agrees with the source proof's minimum with one because
its explicitly defined \(C_{\rm abs},W_G\) both exceed one. They depend only
on activations and depth. Its local power calculation gives

\[
\eta_*^{-1}\le\beta^{25L+4},\qquad
\mathcal B\le\beta^{L+3}.
\tag{1}
\]

The exact intermediate source-proof conclusion needed here is the following:
with probability tending to one, for every training sample \(a\),

\[
\frac1n\sum_{j=1}^L\sum_{i=1}^n
\exp\left\{\eta_*\left(
 \sup_{0\le t\le T}|z_{a,i}^{(j)}(t)|+
 S_0^{-1}\sup_{0\le t\le T}|k_{a,i}^{(j)}(t)|\right)\right\}
\le\mathcal B.
\tag{2}
\]

This is `cp:src-budget` after `cp:src-budget-removal` and the domain
verification, restricted from its complex domain to the real interval. It
is stronger than the public maximum bound `cp:carrier`.

For clarity, the probability and applicability checks behind this invocation
are as follows. The proof defines each deleted-neuron cavity and its stopped
coefficient path before integrating the omitted Gaussian roots. Its real
reference moment estimate is `cp:src-main-moment`. It retains the nonzero
conditional traces in `cp:src-traces`, absorbs scalar feedback, and only then
substitutes adaptive controls into uniform estimates. It does not claim that
trained coordinates are Gaussian. For every fixed positive integer \(u\),
its complete-path cavity comparison yields

\[
\limsup_{n\to\infty}\Pr\{\text{a full budget is hit}\}
\le mL(16L/\mathcal B)^u.
\]

The infimum over fixed \(u\) is zero. The width limit precedes this infimum;
there is no growing deletion count and no additional confidence-dependent
label restriction. The explicit allowance \(S_0\le S_*\) required throughout
that argument is supplied by `cp:src-powers` from the existing
\(Y\le\lambda\beta^{-30L}\) assumption. The proof uses only linear growth
\(|\phi_j(z)|\le b+s|z|\), where
\(b=\max_j|\phi_j(0)|\) and \(s\ge1\) bounds the first derivatives.
It assumes neither oddness nor bounded activation values.

If the training span \(V=\operatorname{span}\{v_a\}\) is proper, apply fitting
and the finite-list source proof to the network on the input space \(V\).
The projected first-layer rows are again independent standard Gaussians in
an orthonormal basis of \(V\); training Grams, normalizations and the actual
active dynamics are unchanged. Thus the event in (2) can be chosen measurable
with respect to the active initialization. For a fixed unit \(v\in V^\perp\),

\[
Z=W^{(1)}(0)v\sim N(0,I_n)
\]

is independent of this event and of the complete active training trajectory.
Since every first-layer velocity is a sum of rows proportional to \(v_a^\top\),
\(W^{(1)}(t)v=Z\) for all \(t\). No event involving this orthogonal Gaussian
query is included in (2).

## 2. The readout fourth moment, uniformly through the endpoint

Let \(M_i=\sup_{t\in[0,\infty]}|w_i(t)|\). Since \(k_a^{(L)}=w\), dropping
nonnegative terms in (2) gives

\[
\frac1n\sum_i\exp\{\eta_*S_0^{-1}
                 \sup_{0\le t\le T}|w_i(t)|\}\le\mathcal B.
\tag{3}
\]

The fitting theorem uses the parameter norm

\[
\|\theta\|_{\rm par}^2
=n^{-1}\|W^{(1)}\|_F^2+
 \sum_{j=2}^L\|W^{(j)}\|_F^2+n^{-1}\|w\|^2
\]

and gives

\[
\sup_{t\ge T}\|\theta(t)-\theta(T)\|_{\rm par}
\le 2Y\lambda^{-1/2}e^{-16\log(en)}.
\]

Consequently, for every coordinate,

\[
\sup_{t\ge T}\frac{|w_i(t)-w_i(T)|}{S_0}
\le \frac{\sqrt{n\lambda}}8 e^{-16\log(en)}
\le\frac18.
\tag{4}
\]

The endpoint satisfies the same estimate by parameter convergence. Combining
(3), (4), and \(\eta_*\le1\) gives, on the same event,

\[
\frac1n\sum_i e^{\eta_*M_i/S_0}\le2\mathcal B.
\tag{5}
\]

For \(p>0\) and \(x\ge0\), maximizing \(x^pe^{-x}\) gives
\(x^p\le(p/e)^pe^x\). In particular,

\[
\frac1n\sum_iM_i^4
\le C_4\left(\frac Y\lambda\right)^4,
\qquad
C_4=2\mathcal B\left(\frac{64}{e\eta_*}\right)^4
\le\beta^{114L}.
\tag{6}
\]

For the last explicit estimate, \(2(64/e)^4<10^6\le\beta^6\), so (1) gives
\(C_4\le\beta^{101L+25}\le\beta^{114L}\) for \(L\ge2\). These powers are
deliberately coarse. Every fixed \(p>0\) likewise has

\[
\frac1n\sum_iM_i^p
\le2\mathcal B\left(\frac{16p}{e\eta_*}\right)^p\varepsilon^p.
\tag{7}
\]

There is no logarithm of width in (6) or (7). All randomness in their event
belongs to the actual active initialization and its canonical dynamics.

## 3. Additional training moments and row bounds

The same extraction works for every training preactivation and carrier.
To extend both beyond \(T\), the fitting tube gives, for fixed activation/depth
constants \(A_j\),

\[
\sup_{t\ge T}\|z_a^{(j)}(t)-z_a^{(j)}(T)\|_\infty
\le A_j\sqrt n\,2Y\lambda^{-1/2}e^{-16\log(en)}.
\]

One may take \(A_1=1\), \(A_j=2H+9sA_{j-1}\), where
\(H=\max_{0\le j\le L}\sqrt{Q_{11}^{(j)}}\) is the fitting lemma's constant. The recursion
comes from subtracting two forward passes in its operator/feature tube.
The source proof's real-tail carrier subtraction gives

\[
\max_{a,j}\sup_{t\ge T}
\|k_a^{(j)}(t)-k_a^{(j)}(T)\|_\infty
\le \beta^{20L}n\,2Y\lambda^{-1/2}e^{-16\log(en)}.
\]

After division of the second display by \(S_0\), both tails tend to zero
for each fixed problem. Thus, eventually, (2) holds on the whole real
trajectory with its right side replaced by \(2\mathcal B\). It follows that
for every fixed \(p\ge1\), training sample \(a\), and layer \(j\),

\[
\begin{aligned}
\frac1n\sum_i\sup_t|z_{a,i}^{(j)}(t)|^p
 &\le2\mathcal B\left(\frac p{e\eta_*}\right)^p,\\
\frac1n\sum_i\sup_t|k_{a,i}^{(j)}(t)|^p
 &\le2\mathcal B\left(\frac{16p}{e\eta_*}\right)^p\varepsilon^p.
\end{aligned}
\tag{8}
\]

Linear activation growth bounds the corresponding activation moment by
\(2^{p-1}[b^p+s^p\,2\mathcal B(p/(e\eta_*))^p]\). Bounded derivatives multiply
the carrier moment by \(s^p\) to bound the response moment. Cauchy--Schwarz
therefore controls arbitrary products of two squared training quantities,
even at different times or different training samples. For example, the
empirical mean of
\(\sup_t|h_{a,i}^{(j)}(t)|^2\sup_u|k_{b,i}^{(j)}(u)|^2\)
is at most \(C_{\phi,L}\varepsilon^2\).

For a hidden matrix write \(E^{(j)}=W^{(j)}(\infty)-W^{(j)}(0)\), and define

\[
D_i^{(j)}=\left(\frac1m\sum_a
                       \sup_t|\delta_{a,i}^{(j)}(t)|^2\right)^{1/2}.
\]

Sample Cauchy--Schwarz, the fitting feature bound \(2H\sqrt n\), and
\(\int_0^\infty\rho(t)\,dt\le2Y/\lambda\) imply

\[
\|E_{i,:}^{(j)}\|\le
 \frac{8H\varepsilon}{\sqrt n}D_i^{(j)}\quad(j\ge2),
\qquad
\|E_{i,:}^{(1)}\|\le4\varepsilon D_i^{(1)}.
\tag{9}
\]

Jensen in the sample index and (8) give
\(n^{-1}\sum_i(D_i^{(j)})^4\le s^4C_4\varepsilon^4\).
Thus the empirical fourth moments of the hidden row norms multiplied by
\(\sqrt n\), or of the unscaled first-layer row norms, are at most explicit
activation/depth constants times \(\varepsilon^8\). These are estimates for
actual trained matrices.

At the top layer, the sharper \(D_i^{(L)}\le b_LM_i\), where
\(b_L=\sup_{x\in\mathbb R}|\phi_L'(x)|\), yields

\[
\|E_{i,:}^{(L)}\|\le
 \frac{8Hb_L\varepsilon}{\sqrt n}M_i,
\qquad
|E_{i,:}^{(L)}\mathbf1|\le8Hb_L\varepsilon M_i.
\tag{10}
\]

Together with (6), these give the precise weighted estimates

\[
\sum_iw_i(\infty)^2\|E_{i,:}^{(L)}\|^2
 \le64H^2b_L^2C_4\varepsilon^6,
\qquad
\sum_iw_i(\infty)^2(E_{i,:}^{(L)}\mathbf1)^2
 \le64H^2b_L^2C_4n\varepsilon^6.
\tag{11}
\]

## 4. Exact two-layer scalar consequence

Take \(L=2\), a unit query orthogonal to the training span, and condition on
the active event above. Set

\[
H_i^{\rm q}=\phi_1(Z_i),\quad
\mu=\mathbb EH_i^{\rm q},\quad
\sigma^2=\operatorname{Var}(H_i^{\rm q}),\quad
W_0=W^{(2)}(0),\quad E=E^{(2)},\quad w=w(\infty).
\]

Here the \(Z_i\) are independent standard Gaussians; linear growth ensures
all displayed query moments exist. Write
\(b_1=\sup|\phi_1'|\), \(b_2=\sup|\phi_2'|\), and
\(b_{22}=\sup|\phi_2''|\), with real suprema. The scalar Gaussian Poincare
calculation in `PRODUCT_QUERY_ROUTE.md` gives

\[
\begin{aligned}
\operatorname{Var}_Z\left[
 \frac1n w^\top\{\phi_2((W_0+E)H^{\rm q})-\phi_2(W_0H^{\rm q})\}\right]
\le\frac{2b_1^2}{n^2}\Big[&b_2^2\|E\|_{\rm op}^2\|w\|^2\\
 &+\|W_0\|_{\rm op}^2b_{22}^2
   \sum_iw_i^2\{\sigma^2\|E_{i,:}\|^2+
                         \mu^2(E_{i,:}\mathbf1)^2\}\Big].
\end{aligned}
\tag{12}
\]

Its hypotheses hold conditionally: the matrices and readout are fixed,
the query Gaussian remains independent, and bounded activation derivatives
give the required square-integrable gradient. No value bound on \(\phi_2\)
is needed. The fitting theorem gives
\(\|E\|_F\le8U_2Y^2/\lambda^{3/2}\),
\(\|w\|^2\le4nY^2/\lambda\), and \(\|W_0\|_{\rm op}\le8\), where
\(U_2=2Hs\). Substitution of (11) into (12) proves

\[
\operatorname{Var}_Z[\cdots]
\le
\frac{512b_1^2b_2^2U_2^2Y^6}{n\lambda^4}
+\frac{8192b_1^2b_2^2b_{22}^2H^2C_4Y^6}{n\lambda^6}
                  \left(\mu^2+\frac{\sigma^2}{n}\right).
\tag{13}
\]

This closes the moment gap identified in equations (8)--(9) of
`PRODUCT_QUERY_ROUTE.md` for arbitrary permitted unbounded outer activations.
It supplies an \(O(\varepsilon^3/\sqrt n)\) centered scalar error at fixed
data, with the actual gap factors displayed. It does not control the scalar
mean, prove a random-feature lower bound, or improve this normalization to
\(O((Y/\sqrt\lambda)\varepsilon^2/\sqrt n)\).

## 5. Boundary of the result

The source exponential budget is a training-source statement. Its treatment
of passive backward fields gives operator/RMS envelopes and analytic
continuation; it does not establish an empirical fourth moment for passive
carriers, or a conditional Gaussian-query fourth moment for them.

In particular, for a fixed terminal readout \(a=w(\infty)\), the fields

\[
p_t^{(L)}(Z)=a,\qquad
p_t^{(j)}(Z)=W^{(j+1)}(t)^\top
 [\phi_{j+1}'(z_t^{(j+1)}(Z))\odot p_t^{(j+1)}(Z)]
\]

are mixed-time observables. Except when the relevant times coincide, they
are not the training carriers in (8). The sufficient deeper scalar bound

\[
\left(\frac1n\mathbb E_Z\sum_i
 [p_{t,i}^{(j)}(Z)]^2[\dot z_{t,i}^{(j)}(Z)]^2\right)^{1/2}
\le C_{\phi,L}\rho(t)
       \frac{\|a\|}{\sqrt n}\frac{\|w(t)\|}{\sqrt n}
\]

does not follow from (6)--(11), and is not proved here. Replacing the two
readout energy factors by \(\varepsilon^2\) would already weaken the
normalization, and even that query extension requires additional analysis.
Operator/Frobenius energy alone does not provide it. No Gaussianity of trained
weights, centering of nonodd features, or boundedness of activation values
has been inserted to bridge this gap.

## 6. Why an energy-normalized fourth moment cannot hold in the full class

The stronger proposed conclusion
\[
\frac1n\sum_i|w_i(\infty)|^4\le C_{\phi,L}e^4,
\tag{14}
\]
with a constant independent of the training data, is false for the full
activation class of the paper. Here \(e\) may be the RMS norm of the frozen
random-feature minimum-norm readout, or the RMS norm of the actual endpoint
readout. The following construction uses fixed depth and fixed activations.
It also explains the precise, more limited conclusion available when all
layers must be nonaffine.

Fix \(L\ge2\), use identity activations in layers \(1,\ldots,L-1\), and use
\(\phi_L(z)=\cos z\). These satisfy the strip assumptions, with the same
\(\beta=16\), for example on the strip of width one. For an integer \(k\ge2\),
set \(m=2^k\), \(d=k+2\), \(t=(2k)^{-1/2}\), and index the training inputs
by \(\sigma\in\{-1,1\}^k\):
\[
v_\sigma=(2^{-1/2},t\sigma_1,\ldots,t\sigma_k,0),\qquad
c_\sigma=2^{-k}\prod_{j=1}^k\sigma_j.
\]
Each input is a unit vector. The final zero coordinate leaves a proper
training span and supplies an orthogonal query if one is needed.

Identity lower layers leave the population input Gram unchanged. Thus the
limiting top feature vector has coordinates \(\cos(G^\top v_\sigma)\),
where \(G\) is a standard Gaussian vector. Its parity combination is exactly
\[
\begin{aligned}
T_k(G)&=\sum_\sigma c_\sigma\cos(G^\top v_\sigma)\\
 &=\cos(G_0/\sqrt2+k\pi/2)\prod_{j=1}^k\sin(tG_j).
\end{aligned}
\tag{15}
\]
To check the identity, expand the real part of
\(2^{-k}e^{iG_0/\sqrt2}\prod_j(e^{itG_j}-e^{-itG_j})\).
All factors on the right side of (15) are independent. Their second moments
are positive. For \(x=e^{-2t^2}\), the Gaussian characteristic function gives
\[
\mathbb E\sin^2(tG_1)=\frac{1-x}{2},\qquad
\mathbb E\sin^4(tG_1)=\frac{3-4x+x^4}{8},
\]
and hence
\[
\frac{\mathbb E\sin^4(tG_1)}
 {(\mathbb E\sin^2(tG_1))^2}
 =\frac{x^2+2x+3}{2}.
\]
The factorization
\(x^4-4x+3=(x-1)^2(x^2+2x+3)\) verifies the cancellation.
Since \(x=e^{-1/k}\ge e^{-1/2}>1/2\), this last ratio exceeds two.
Cauchy--Schwarz gives a kurtosis of at least one for the first factor in
(15). Therefore
\[
\frac{\mathbb ET_k^4}{(\mathbb ET_k^2)^2}>2^k.
\tag{16}
\]

Let \(Q\) be the population Gram of these cosine features. It is strictly
positive definite. Indeed, a zero-variance linear combination would vanish
almost everywhere under a Gaussian density and, by continuity, everywhere
as a function of \(G\). Its exponential expansion has distinct frequencies
\(\{v_\sigma,-v_\sigma\}\), since every \(v_\sigma\) has positive first
coordinate. Finite exponentials with distinct frequencies are linearly
independent: restrict to a line having distinct projected frequencies and
differentiate at zero to obtain an invertible Vandermonde system. Thus every
coefficient vanishes.

Choose \(y_0=Qc\) and \(y=\alpha y_0\), with \(\alpha>0\). The population
minimum-norm random-feature readout is \(\alpha T_k\), and its squared energy
is
\[
e_0^2\alpha^2=\alpha^2y_0^\top Q^{-1}y_0
             =\alpha^2\mathbb ET_k^2>0.
\]
For each fixed \(k\), \(\alpha\) can be as small as necessary to satisfy the
original label cap; (16) is independent of \(\alpha\). The condition
\(\lambda=\lambda_{\min}(Q)/m\le1\) also holds, since every cosine feature
has second moment at most one.

### Transfer to the actual canonical endpoint

This step does not assume a random-feature model for trained weights. Write
\(\mathsf H_t=[h_a^{(L)}(t)]_a\) and
\(Q_n=\mathsf H_0^\top\mathsf H_0/n\), and use
\(\|u\|_{p,n}=(n^{-1}\sum_i|u_i|^p)^{1/p}\) for neuron vectors.
For this fixed dataset, on the fitting event and uniformly in width,
\[
\sup_t\frac{\|\mathsf H_t-\mathsf H_0\|_F}{\sqrt n}
 \le C_{\rm data}\alpha^2,\qquad
\|w_\infty\|_{2,n}\le C_{\rm data}\alpha,\qquad
\int_0^\infty\|r(t)\|\,dt\le C_{\rm data}\alpha.
\tag{17}
\]
These are exactly the fitting displacement, readout and activity bounds;
their constants may depend on this fixed \(k,Q,y_0\), but not on \(n\) or
on sufficiently small \(\alpha\). Put
\[
b=-\frac2m\int_0^\infty r(t)\,dt,\qquad
v=-\frac2m\int_0^\infty(\mathsf H_t-\mathsf H_0)r(t)\,dt.
\]
The readout equation gives \(w_\infty=\mathsf H_0b+v\), and (17) gives
\(\|v\|_{2,n}\le C_{\rm data}\alpha^3\).
Endpoint fitting then gives
\[
\alpha y_0
=Q_nb+\frac{\mathsf H_0^\top v}{n}
      +\frac{(\mathsf H_\infty-\mathsf H_0)^\top w_\infty}{n}
=Q_nb+O_{\rm data}(\alpha^3)
\]
in the Euclidean sample norm. The fitting event gives
\(\lambda_{\min}(Q_n)\ge\gamma/2\). Consequently
\[
\left\|\frac{w_\infty}{\alpha}
       -\mathsf H_0Q_n^{-1}y_0\right\|_{2,n}
\le C_{\rm data}\alpha^2.
\tag{18}
\]
The top cosine is bounded, so its exact readout equation also gives
\(\|w_\infty/\alpha\|_\infty\le4Y_0/\lambda\), where
\(Y_0=\|y_0\|/\sqrt m\). Every initialized cosine feature is at most one
in absolute value, and
\(\|Q_n^{-1}y_0\|_1\le2\sqrt m\|y_0\|/\gamma\). Both vectors in (18)
therefore have uniform, data-dependent coordinate bounds. The elementary
inequality
\(\|u\|_{4,n}\le\|u\|_\infty^{1/2}\|u\|_{2,n}^{1/2}\) upgrades (18) to
\[
\left\|\frac{w_\infty}{\alpha}
       -\mathsf H_0Q_n^{-1}y_0\right\|_{4,n}
\le C_{\rm data}\alpha.
\tag{19}
\]

For this fixed finite dataset, initialized empirical second and fourth
moments of \(\mathsf H_0c\) converge to those of \(T_k\). To verify this,
condition on all lower initialized layers: the top rows are independent
Gaussian preactivation vectors whose covariance converges to the input
Gram. Cosine is bounded, so conditional Chebyshev and continuity of Gaussian
expectations give both moment limits. Also \(Q_n\to Q\) and
\(Q_n^{-1}y_0\to c\). The bounded top features transfer those moment limits
to \(\mathsf H_0Q_n^{-1}y_0\).

Given any proposed finite constant in (14), choose \(k\) so that (16)
exceeds that constant by a strict margin. Then choose a fixed positive
\(\alpha\), satisfying the existing cap, so small that (18)--(19) preserve
the margin. Sending \(n\) to infinity proves failure of (14) with
probability tending to one. This works both for
\(e=\alpha\sqrt{y_0^\top Q_n^{-1}y_0}\) and for
\(e=\|w_\infty\|_{2,n}\). The all-time fourth moment is at least its endpoint
value, so the same counterexample applies to that stronger formulation.

### What this proves for an all-nonaffine activation class

For each fixed \(k\), replace every lower identity activation by
\(\phi_j(z)=z+\tau\tanh z\), with \(\tau>0\), and retain the top cosine.
Every layer is now nonaffine. A common strip of width one and the common
envelope \(\beta=16\) work for \(0<\tau\le1\): the poles of \(\tanh\) lie
outside this strip, its derivative is bounded there, and its first two
derivatives on the half strip have bounded magnitudes below sixteen.

For this fixed panel, each layer's population Gram is continuous at
\(\tau=0\). This follows recursively from Gaussian square-root coupling
and domination by a Gaussian polynomial, since the activation family has
uniform linear growth. The final cosine feature combination's second and
fourth moments are continuous as well, since it is bounded. Strict positivity
of the final Gram persists for sufficiently small \(\tau>0\). Thus, for each
fixed \(k\), a sufficiently small \(\tau=\tau(k)>0\) preserves arbitrarily
much of (16); choosing \(y_0=Q_\tau c\) and using (17)--(19) transfers this
to actual training too.

This rules out a universal energy-normalized fourth-moment bound depending
only on the common envelope \(\beta\) and depth, even when every layer is
nonaffine. It does not by itself rule out an unspecified finite constant
\(C_{\phi,L}\) for each fixed all-nonaffine activation tuple, because the
constructed tuple changes with \(k\). In contrast, the identity-lower/cosine-top
counterexample uses one fixed tuple and does rule out such an activation-only
constant for the full class stated in the paper.

No passive-query exponential-budget extension is established by this
counterexample or by the preceding training-moment extraction. Even with
the contemporaneous readout \(w(t)\), extending the training budget to passive
backward fields requires a separate stopped-observable moment argument.
The source proposition's passive RMS and holomorphy statements alone do not
supply it. Mixed terminal-readout probes add a further requirement.

# Direct prediction through a resummed real-time response

2026-10-06. Scoped author derivation; no experiment or promotion. The full
efficient late-query decoder is **not proved**. The new partial result is a
factorially convergent expansion of the actual initialization response,
uniform in physical time under explicit inherited bounds. It does not use a
complex label disk, posterior sampling, or a history covariance inverse.

The expansion resums the positive Gauss--Newton part of the loss Hessian
and expands only its residual-weighted curvature. Under the inherited
all-time residual and carrier bounds, order
`O(log(en)/log log(e^e n))` suffices for any prescribed inverse-polynomial
response error. Its Gauss--Newton part reduces to a two-time training kernel.
The unresolved implication is a polynomial-time, compact evaluator for the
remaining curvature contractions. A scalar integral or dense operator is
not counted as one register in this note.

## 1. Model and inherited interface

Use the actual network and notation of `POPULATION_DECODER.md`: inputs
\(v_a=x_a/\sqrt d\), fixed \(L\ge2\), Gaussian first matrix \(A\),
Gaussian hidden mixers \(W^{(\ell)}\) with entry variance \(1/n\),
zero initial readout \(w\), prediction
\(f_n(t,v)=w(t)^Th^{(L)}(t,v)/n\), mean squared loss, and
mobilities \((n,1,\ldots,1,n)\). All original spanning-data, activation,
label-allowance and feature-Gram assumptions are retained.

The Euclidean mobility coordinates and normalized residual are

\[
 \theta=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n),
 \qquad e_a(\theta)=\frac{f_n(\theta,v_a)-y_a}{\sqrt m},
 \qquad \rho(t)=\|e(\theta(t))\|_2.
 \tag{1}
\]

The loss is \(\|e\|_2^2\) in these coordinates. Define the full
parameter Jacobian \(\mathcal J(t)\) to have columns
\(\nabla_\theta e_a(\theta(t))\). This differs from the
hidden-only operator denoted \(J\) in `LABEL_SERIES_DECODER.md`.

For upper backward carriers use

\[
 k_a^{(L)}=w,\quad
 k_a^{(\ell)}=(W^{(\ell+1)})^T\delta_a^{(\ell+1)},\quad
 \delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)}.
 \tag{2}
\]

The following interface is stated explicitly so that its role is visible.
On a good initialization event, assume uniform operator bounds for the
mixers, uniform RMS bounds for the sphere forward fields and training
backward fields, and

\[
 \int_0^\infty\rho(t)\,dt\le C Y,
 \qquad
 \max_{a,\ell}\sup_{t\ge0}\|k_a^{(\ell)}(t)\|_\infty
                 \le C Y\sqrt{\log(en)}.
 \tag{3}
\]

Here \(Y=\|y\|_2/\sqrt m\), and constants may depend on the fixed
original problem. The supervisor supplied (3) as an inherited interface;
the integrated artifact was not imported into this scoped route. The
allowed `SOURCE_SUPREMUM_EXTENSION.md` separately states the carrier and
complex source bounds on \([0,T_n]\), with \(T_n=C\log(en)\).
All results below remain valid on that finite interval with (3) replaced
by the corresponding finite-interval bounds. Loss monotonicity alone then
gives the weaker but still absolute-polylogarithmic truncation order
\(O(\log(en)^{3/2})\). The sharper all-time corollary uses precisely (3).

## 2. A Hessian bound in the actual mobility norm

There is a constant independent of width such that

\[
 \|\nabla_\theta^2 f_n(t,v_a)\|_{\rm op}
 \le C\left(1+\max_\ell\|k_a^{(\ell)}(t)\|_\infty\right).
 \tag{4}
\]

Here and below the operator norm uses the direct-sum Frobenius/Euclidean
norm in (1). This normalization is essential.

To prove (4), let \(\xi,\zeta\) be parameter variations in that norm.
Their physical first-matrix and readout variations are
\(\sqrt n\xi_A,\sqrt n\xi_w\), while the hidden-matrix variations
are \(\xi_{W^{(\ell)}}\). Layerwise differentiation, the mixer
operator bounds, the feature RMS bounds and bounded \(\phi_\ell'\)
give

\[
 \|Dz^{(\ell)}[\xi]\|_2+
 \|Dh^{(\ell)}[\xi]\|_2\le C\sqrt n\|\xi\|_2.
 \tag{5}
\]

The first-layer starting bound is
\(\|\sqrt n\xi_Av_a\|_2\le\sqrt n\|\xi_A\|_F\).
At each following layer use
\(Dz^{(\ell)}[\xi]=\xi_{W^{(\ell)}}h^{(\ell-1)}+
W^{(\ell)}Dh^{(\ell-1)}[\xi]\); this proves (5) by induction.

Contracting the second forward variation backwards gives three kinds of
terms in \(D^2 f_n[\xi,\zeta]\):

\[
\begin{split}
 &\frac{(\sqrt n\xi_w)^TDh^{(L)}[\zeta]
       +(\sqrt n\zeta_w)^TDh^{(L)}[\xi]}{n},\\
 &\frac1n\sum_{\ell=2}^L(\delta_a^{(\ell)})^T
       \left(\xi_{W^{(\ell)}}Dh^{(\ell-1)}[\zeta]
            +\zeta_{W^{(\ell)}}Dh^{(\ell-1)}[\xi]\right),\\
 &\frac1n\sum_{\ell=1}^L\sum_i k_{a,i}^{(\ell)}
       \phi_\ell''(z_{a,i}^{(\ell)})
       Dz_{a,i}^{(\ell)}[\xi]Dz_{a,i}^{(\ell)}[\zeta].
\end{split}\tag{6}
\]

This identity follows by differentiating
\(h^{(\ell)}=\phi_\ell(z^{(\ell)})\) twice: the second variation
of a matrix product gives the two mixed terms, and the second variation
of an activation gives the final line. Reverse propagation contracts
each local term against its upper carrier. There is no second variation
of the first affine preactivation.

The first two lines of (6) are bounded by
\(C\|\xi\|_2\|\zeta\|_2\), using (5) and the backward RMS bound.
For the third, Cauchy--Schwarz bounds the coordinate product sum by the
product of the two preactivation variation norms. The strip assumption
supplies bounded real \(\phi_\ell''\): apply the one-variable Cauchy
formula to bounded \(\phi_\ell'\) on a circle of radius half the
strip width about each real point. This proves (4).

Define the residual curvature

\[
 \mathcal H(t)=\sum_{a=1}^m e_a(t)\nabla_\theta^2e_a(\theta(t)).
 \tag{7}
\]

Since \(\nabla^2e_a=\nabla^2f_n(\cdot,v_a)/\sqrt m\),
Cauchy--Schwarz in the sample index and (4) give

\[
 \|\mathcal H(t)\|_{\rm op}
       \le C\rho(t)\left(1+\max_{a,\ell}
                                      \|k_a^{(\ell)}(t)\|_\infty\right).
 \tag{8}
\]

Consequently, under (3), its total action satisfies

\[
 M_n:=2\int_0^\infty\|\mathcal H(t)\|_{\rm op}\,dt
       \le C Y\left(1+Y\sqrt{\log(en)}\right)
       \le C\sqrt{\log(en)}.
 \tag{9}
\]

No stronger label restriction is used. For the finite-horizon variant,
\(\dot e=-2\mathcal J^T\mathcal J e\) implies
\(d\|e\|_2^2/dt=-4\|\mathcal J e\|_2^2\le0\), so
\(\rho\le Y\). The source cap on \([0,T_n]\) then gives
\(M_{n,T_n}\le C\log(en)^{3/2}\) without invoking (3).

## 3. Factorial response convergence without a label expansion

Let \(U(t,s)\) be the derivative propagator of the actual parameter flow,
mapping a variation at time \(s\) to its variation at time \(t\).
Differentiating \(\dot\theta=-2\mathcal J e\) gives exactly

\[
 \partial_tU(t,s)
   =-2\bigl(\mathcal J(t)\mathcal J(t)^T+\mathcal H(t)\bigr)U(t,s),
 \qquad U(s,s)=I.
 \tag{10}
\]

Let \(S(t,s)\) solve the same equation with \(\mathcal H\) omitted.
For any vector \(v\),

\[
 \frac d{dt}\|S(t,s)v\|_2^2
       =-4\|\mathcal J(t)^TS(t,s)v\|_2^2\le0,
 \qquad \|S(t,s)\|_{\rm op}\le1.
 \tag{11}
\]

Define \(U_0=S\), and recursively

\[
 U_k(t,s)=-2\int_s^t S(t,u)\mathcal H(u)U_{k-1}(u,s)\,du.
 \tag{12}
\]

The ordered-simplex integral and (11) prove

\[
 \|U_k(t,s)\|_{\rm op}
   \le\frac{\left(2\int_s^t\|\mathcal H(u)\|_{\rm op}du\right)^k}{k!}.
 \tag{13}
\]

Indeed the ordered integral of a product of the same nonnegative scalar
function is \(1/k!\) times its integral over the full cube; the cube is
partitioned, up to measure zero, by the \(k!\) possible orders. Thus
\(\sum_kU_k\) converges uniformly in operator norm on every interval
where the curvature action is finite. Substituting the absolutely
convergent series into (12) gives the variation-of-constants equation
for (10); uniqueness of its finite-dimensional linear integral equation
identifies the sum with \(U\). In particular,

\[
 \sup_{0\le s\le t<\infty}
 \left\|U(t,s)-\sum_{k=0}^KU_k(t,s)\right\|_{\rm op}
       \le\sum_{k>K}\frac{M_n^k}{k!}.
 \tag{14}
\]

For each fixed \(A>0\), (9) permits

\[
 K=O_A\!\left(\frac{\log(en)}{\log\log(e^e n)}\right)
 \quad\text{with the right side of (14) at most }n^{-A}.
 \tag{15}
\]

Here is the elementary asymptotic check. Put \(h=\log(en)\) and
\(k_0=K+1=c_Ah/\log(e+h)\), rounded upwards. From
\(M_n\le C\sqrt h\), for sufficiently large width,
\(\log(k_0/(eM_n))\ge\tfrac13\log h\) and
\(M_n/(k_0+1)\le1/2\). Also
\(k!\ge(k/e)^k\), since
\(\log k!=\sum_{j=1}^k\log j\ge\int_1^k\log x\,dx\).
The tail is therefore at most
\(2(eM_n/k_0)^{k_0}\le2e^{-c_Ah/4}\).
Choosing \(c_A>4(A+1)\) proves (15), after increasing the width
threshold. With the weaker finite-horizon action, taking
\(K+1\ge\max\{2eM_{n,T_n},(A\log n+2)/\log2\}\)
instead gives \(K=O_A(\log(en)^{3/2})\).

Equations (10)--(15) retain the actual nonlinear trajectory in their
coefficients. They are not a lazy-training substitution. They prove
convergence of an operator expansion, not compact storage of its terms.

## 4. The positive part reduces to a training-only scalar kernel

Define the \(m\times m\) two-time kernel
\(\mathcal K(t,s)=\mathcal J(t)^T\mathcal J(s)\). Its entries are
explicitly

\[
\begin{split}
 m\mathcal K_{ab}(t,s)
  ={}&(v_a^Tv_b)\frac{\delta_a^{(1)}(t)^T\delta_b^{(1)}(s)}n
       +\frac{h_a^{(L)}(t)^Th_b^{(L)}(s)}n\\
     &+\sum_{\ell=2}^L
       \frac{\delta_a^{(\ell)}(t)^T\delta_b^{(\ell)}(s)}n
       \frac{h_a^{(\ell-1)}(t)^Th_b^{(\ell-1)}(s)}n.
\end{split}\tag{16}
\]

This is the inner product of the parameter gradients in (1): the hidden
gradient is the outer product \(\delta h^T/(n\sqrt m)\), while
the normalized first and readout gradients carry \(1/\sqrt{mn}\).
Thus the positive part requires only training-history pairings already
of the scalar-moment type used by the current response construction.

For any parameter vector \(v\), set
\(b(t)=\mathcal J(t)^TS(t,s)v\). Integrating the equation for \(S\)
and multiplying by \(\mathcal J(t)^T\) gives exactly

\[
 b(t)=\mathcal J(t)^Tv-2\int_s^t\mathcal K(t,u)b(u)\,du,
 \qquad
 S(t,s)v=v-2\int_s^t\mathcal J(u)b(u)\,du.
 \tag{17}
\]

No history-Gram inverse appears. The Volterra resolvent kernel is the
unique solution

\[
 \mathcal R(t,s)=\mathcal K(t,s)
       -2\int_s^t\mathcal K(t,u)\mathcal R(u,s)\,du.
 \tag{18}
\]

If \(g(t)=\mathcal J(t)^Tv\), then the first equation in (17) has
solution \(b(t)=g(t)-2\int_s^t\mathcal R(t,u)g(u)du\).
Substitution and an interchange of two integrals over a finite triangle
verify the identity using (18). Existence and uniqueness follow from
the same ordered-simplex convergence argument as in Section 3.

There is a useful *representation count*, distinct from its acquisition.
On the source complex-time rectangle around \([0,T_n]\), (16) is
holomorphic in its two times and bounded by a fixed constant: the
complex pairings use ordinary transposes, and their absolute values are
bounded by the stated RMS bounds. The iterated-integral construction
of (18) along straight complex segments is holomorphic on the product
rectangle and has bound \(C\exp(C|t-s|)\le n^C\). Its order-\(j\)
integrand has norm at most \(C(2C|t-s|)^j/j!\), which justifies both
uniform convergence and holomorphy there.

With time radius \(r_n=c/\sqrt{\log(en)}\), cover each axis by
\(O(\log(en)^{3/2})\) inner half-radius patches. Degree
\(p=O_A(\log(en))\) in each time gives error \(n^{-A}\) from
Cauchy coefficient bounds and two geometric-series tails. Hence a
piecewise representation of \(\mathcal R\) uses

\[
 O_{m,A}(\log(en)^5)
 \tag{19}
\]

scalar coefficients and polynomial evaluation work. This count has an
absolute exponent and involves no query inputs or spatial grid.
It does **not** grant those coefficients as free input: a completed
algorithm must acquire them causally from its retained history, with
numerical errors controlled. Equation (18) gives the causal relation;
(19) alone is not that acquisition proof. In addition, (17) still
contains the parameter vectors \(\mathcal J(u)\) when applied to a
general argument. The scalar resolvent table by itself is not the
entire parameter propagator.

## 5. Response-trace truncation does not lose a power of width

The Gaussian response notes require the scalar trace

\[
 \mathcal T(s,t,v)=\frac1{n^{3/2}}\sum_{i,j}
           \partial_{M_{ij}}\{c_i(s)h_j(t,v)\},
 \tag{20}
\]

where \(M\) is an initialized standard-Gaussian hidden block. The
derivatives are total derivatives. Consider first fields which are
functions of the trained parameters; any explicit initialized-matrix
dependence is differentiated separately and exactly.

The initialized mobility coordinates are a linear image of the Gaussian
root with operator norm \(1/\sqrt n\). Thus replacing \(U(t,0)\)
in their initialization derivatives by (12) through order \(K\), with
operator error \(\varepsilon\), changes their root Jacobians by at
most \(A_c\varepsilon\) and \(A_h\varepsilon\), provided

\[
 \|D_\theta c\|_{\rm op}\le\sqrt n A_c,\quad
 \|D_\theta h\|_{\rm op}\le\sqrt n A_h,\quad
 \|c\|_2\le B_c\sqrt n,\quad\|h\|_2\le B_h\sqrt n.
 \tag{21}
\]

For the source fields, forward differentiation gives \(A_h\le C\)
uniformly over sphere queries; training backward differentiation gives
\(A_c\le C(1+\max\|k\|_\infty)\). A changed gate is bounded by
\(\|k\|_\infty\|\phi''\|_\infty\|Dz\|_2\); the other
terms use the mixer operator and backward RMS bounds. Induction over
the fixed depth proves these claims. Initialized images obey the same
implicit-derivative estimates using their operator bounds.

To bound the trace error, define \(\mathcal B_h:\mathbb R^n\to\mathbb R^{n^2}\)
by \((\mathcal B_hz)_{ij}=z_i h_j\), so
\(\|\mathcal B_h\|_{\rm op}=\|h\|_2\).
The first product-rule term in (20) is
\(n^{-3/2}\operatorname{tr}((D_Mc)\mathcal B_h)\). For an \(n\times n\)
matrix \(Q\), \(|\operatorname{tr}Q|\le n\|Q\|_{\rm op}\)
by summing \(|e_i^TQe_i|\). Therefore the error of this term is at
most \(B_hA_c\varepsilon\). Applying the same argument with the
two matrix orientations interchanged to the other product-rule term gives

\[
 |\mathcal T-\mathcal T_K|
       \le (B_hA_c+B_cA_h)\varepsilon.
 \tag{22}
\]

All actual fields in (20) remain unchanged in this comparison; only their
response operator is truncated. Choosing the exponent in (15) slightly
larger absorbs the \(\sqrt{\log(en)}\) factor in (21). Thus the
response-trace *truncation error* can be \(n^{-A}\), uniformly on the
same good event over all permitted source times and sphere queries.
This is not an evaluation of \(\mathcal T_K\), and does not replace
the separate Gaussian-divergence source error by \(n^{-A}\).
No endpoint derivative is asserted. Once a predictor construction is
available up to \(T_n\), the inherited prediction tail can handle
\(t\ge T_n\) and the fitted endpoint without endpoint derivatives.

## 6. Residual curvature need not have small rank

An admissible example prevents a premature low-rank closure of (12).
Take \(d=m=1\), \(v_1=1\), \(L=2\),
\(\phi_1(z)=\tanh z\), \(\phi_2(z)=z\), and any nonzero label
inside the original small-label allowance. Both activations obey the
strip assumptions; the second has unbounded values. The feature Gram
has a positive scalar population gap. The network is

\[
 f=\frac1n w^TW\tanh A,
 \qquad k^{(1)}=W^Tw.
 \tag{23}
\]

Its Hessian block in the normalized first coordinates is exactly

\[
 \nabla_{A/\sqrt n}^2f
             =\operatorname{diag}\bigl(k_i^{(1)}\tanh'' A_i\bigr).
 \tag{24}
\]

At initialization \(\dot w(0)=2yW_0\tanh A_0\), while
\(\dot W(0)=\dot A(0)=0\). Consequently

\[
 \frac d{dt}k^{(1)}(0)=2yW_0^TW_0\tanh A_0.
 \tag{25}
\]

Almost surely all \(A_{0,i}\ne0\), hence all
\(\tanh'' A_{0,i}\ne0\) and all \(\tanh A_{0,i}\ne0\).
Conditional on such an \(A_0\), each coordinate of
\(W_0^TW_0\tanh A_0\) is a nonzero polynomial in the entries of
\(W_0\): setting \(W_0=I\) proves it is not identically zero.
A nonzero polynomial vanishes on a Lebesgue-null set, by induction on
its variable count, the finite root set of a nonzero univariate
polynomial, and Fubini. The Gaussian density therefore makes every
coordinate in (25) nonzero almost surely.

For each such finite initialization, continuity gives a sufficiently
short interval \(0<t<t_*\) on which every diagonal entry in (24)
is nonzero and \(e(t)=f(t)-y\ne0\). Thus the corresponding principal
block of \(\mathcal H(t)\) has rank \(n\), although
\(\mathcal J(t)\mathcal J(t)^T\) has rank at most one. Moreover
\(\ddot A_i(0)=4y^2\tanh'(A_{0,i})
(W_0^TW_0\tanh A_0)_i\ne0\), so the example has actual hidden
feature motion. It is not a frozen-feature example.

This defeats the assertion that finite sample count makes residual
curvature exactly low rank. It does not rule out an approximate
functional representation of its diagonal actions, spectral
approximation, or any other compact decoder.

## 7. Precise remaining implication and claim status

The new route changes the unresolved object. Instead of a conditional
posterior integral, seek a direct representation of contractions of

\[
 S(t,t_k)\mathcal H(t_k)S(t_k,t_{k-1})\cdots
                    \mathcal H(t_1)S(t_1,0),\qquad k\le K,
 \tag{26}
\]

with the forward/backward/query fields entering (20), using the current
acquired scalar history and counted initialization-dependent marks.
The scalar kernel (16), its resolvent (18), and the real curvature
action bound (9) are available structural reductions. They are not a
compact evaluator of (26).

A sufficient missing lemma would have to provide, together:

1. A polynomial-size recurrence for the *sum* of the required ordered
   contractions through \(K\), with relative/absolute error tolerances
   and accumulated errors specified. Enumerating an exponentially
   growing family of diagrams is not polynomial query work.
2. Acquisition of every training coefficient from the compact current
   state without storing future scalar outputs; subsequent query
   evaluation must not run scalar training updates again.
3. Evaluation of the new-query boundary fields for all sphere inputs
   using the same retained representation, with an error bound uniform
   in the query, the current time and all allowed prefixes.
4. A comparison/stability argument taking the Gaussian response source
   errors and contraction errors to prediction at the inherited
   whole-sphere dense-self-variability scale, plus the existing fitted
   prediction tail. A trace identity alone does not close dynamics.

No such lemma is derived here. The full path and dense matrices appearing
in the proof of (26) are proof objects, not authorized decoder oracles.
Replacing their contractions by unspecified population Gaussian
integrals merely relocates the unresolved computation. The workspace
of a small recursion stack and its runtime are separate requirements.
Runtime statements must also be relative to the fixed activation
primitives unless a polynomial-time precision interface is supplied.

The exact Hessian formula, factorial response theorem, scalar resolvent
identity, and trace-error estimate are proved here under their displayed
conditions. The all-time rate (15) uses the inherited interface (3).
The \(O(\log^5 n)\) scalar-resolvent count is a representation lemma,
not a causal acquisition theorem. The rank example concerns one
specific low-rank proposal. The original efficient decoder conjecture
is neither established nor refuted.

## 8. Provenance and check status

Complete allowed scientific inputs read: `CURRENT_STATE_DECODER_CANDIDATE.md`,
`ROOT_RESPONSE_AND_COVARIANCE.md`, `SOURCE_SUPREMUM_EXTENSION.md`,
`LABEL_SERIES_DECODER.md`, `POPULATION_DECODER.md`, and `QUERY_TIME_ROUTE.md`.
No linked research artifacts, other route outputs, other study contents,
book/archive passages, external scientific sources or experiments were
used. The supervisor's followup supplied the explicit bounds in (3).

Process inputs were Part 1 of `RESEARCH_WORKFLOW.md`, the complete
`investigate-conjectures` skill and its research-contract and
adversarial-audit references, and `solve-math-rigorously`. The custom
canonical-notation skill returned `Permission denied`; the supervisor's
authorized fallback applies the explicit user/AGENTS notation requirements
and the notation of the allowed sources. Its unavailable neural-network
reference was not read.

The derivations have been checked by their author only. No independent
internal PASS or promotion is claimed. The author edited only this file;
the shared index was empty before the write, and HEAD was
`7ee13decc7ff43d289ec64c0b2463906afbb3090`.

Input SHA-256 values at the read/write checkpoint:

| Input | SHA-256 |
|---|---|
| `CURRENT_STATE_DECODER_CANDIDATE.md` | `9b1e87e3c2e2e74efdf56a40c130c8ff91d74484ab215d6afe03c8ae2c808411` |
| `ROOT_RESPONSE_AND_COVARIANCE.md` | `fc5aeaaf56dc9c4e55f71eb40e81ed6fcede8c21f1eab715617654e60d66deea` |
| `SOURCE_SUPREMUM_EXTENSION.md` | `8623e2d8adaf3b730274dd704fcbd44533a67fe67d47e18ce38701b7d6cb6a6f` |
| `LABEL_SERIES_DECODER.md` | `91f7996ae238c53f9e7ad40f3a950607505ae01ee703eafc57d037ff831cc333` |
| `POPULATION_DECODER.md` | `9d7ac82eed17036686cef3d679022a8df4404e78212e87e5df83d0503733f54d` |
| `QUERY_TIME_ROUTE.md` | `64de3f1d6de8fe541c20c537b2b6e124a68739122d66c364804bd6075f8648fc` |

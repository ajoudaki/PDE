# Strict all-time population rate: two hidden linear layers

2026-10-03. Coordinator candidate proof from the large-label negative
search. This is a special-case positive theorem, not a resolution for
nonlinear activations or general multi-sample data. Every layer is trained
with the canonical mobility. No clipping, frozen trained layer or numerical
experiment is used. Initial status: awaiting complete internal reconstruction.

## 1. Statement and exact reduction

Use identity activations and
\[
 f_n(t,x)=n^{-1}w(t)^\top W(t)A(t)x/\sqrt d .
\]
Initially \(A_{ij}\sim N(0,1)\), \(W_{ij}\sim N(0,1/n)\), independently,
and \(w=0\). Train on one input \(\|x_0\|=\sqrt d\), with any fixed label
\(y\in\mathbb R\), squared loss \((f_n(x_0)-y)^2\), mobilities \(n\) for
read-in/readout and one for the hidden matrix. For a fixed query law
\(\mu\) with finite second moment and every fixed confidence \(1-\delta\),
the claim is
\[
 \Pr\left\{\left(\int\sup_{t\ge0}|f_n(t,x)-f_\infty(t,x)|^2d\mu(x)
                  \right)^{1/2}\le C_{\delta,y,\mu}/\sqrt n\right\}
       \ge1-\delta
 \tag{1}
\]
for all sufficiently large \(n\). Constants are independent of width and
time. The canonical population is identified below, including its bias:
\[
 f_\infty(\infty,x)=y\,\langle x,x_0\rangle/d .
 \tag{2}
\]
Identity activation belongs to the permitted derivative class. This is
not a theorem for a nonlinear activation.

Take \(y=Y>0\). Negative labels reverse \(w,f\) and preserve hidden
physical dynamics; zero labels give stationary zero predictors.
Introduce control \(s\) by \(ds/dt=2(Y-f_n(x_0))\), and define
\[
 a=A x_0/\sqrt d,\quad v=a/\sqrt n,\quad u=w/\sqrt n,\quad
 P_n=u^\top Wv,\quad q_n=\|v(0)\|^2 .
\]
Primes mean control derivatives. The exact controlled equations are
\[
 u'=Wv,\qquad v'=W^\top u,\qquad W'=uv^\top,\qquad
 u(0)=0,\quad v(0)=a_0/\sqrt n .
 \tag{3}
\]
Their balances and second-order reduction are
\[
 WW^\top-uu^\top=W_0W_0^\top=:T_n,\qquad
 \|v\|^2-\|u\|^2=q_n,
\]
\[
 u''=[T_n+(q_n+2\|u\|^2)I]u,\qquad
 u'(0)=W_0v(0)=:b_n,\qquad P_n=\langle u,u'\rangle .
 \tag{4}
\]
Differentiation verifies each equality. The learned matrix contributes
the \(2\|u\|^2\) term; (4) does not replace training by a frozen model.

Diagonalize \(T_n\). Its positive spectral measure in \(b_n\) is defined
by \(\int F\,d\nu_n=b_n^\top F(T_n)b_n\) for polynomials \(F\).
Let
\[
 \psi_n''(s,\lambda)=[\lambda+q_n+2R_n(s)^2]\psi_n(s,\lambda),
 \quad \psi_n(0,\lambda)=0,\quad\psi_n'(0,\lambda)=1 .
\]
Then (4) gives
\[
 R_n^2=\|u\|^2=\int\psi_n^2d\nu_n,\qquad
 P_n=\int\psi_n\psi_n'd\nu_n .
 \tag{5}
\]

## 2. Controlled energy, continuation and fitting

The controlled equations are ascent of \(P=f(x_0)\) in the canonical
mobility metric. Hence
\[
 P'=\|u'\|^2+\|v'\|^2+\|W'\|_F^2 .
 \tag{6}
\]
For \(R=\|u\|>0\), \(R'=P/R\), and
\[
 P'\ge\|u'\|^2\ge(P/R)^2=(R')^2,\qquad R''\ge0 .
\]
Since \(R'(0+)=\|b_n\|\), it follows first near zero and then throughout
existence that
\[
 P_n'\ge Q_n,\qquad P_n(s)\ge Q_n s,\qquad
 Q_n=\|b_n\|^2=\nu_n([0,\infty)) .
 \tag{7}
\]
Indeed \(R'\ge\sqrt{Q_n}\) prevents a later return to \(R=0\).

Every fixed target \(H>0\) is reached by control time \(H/Q_n\) when
\(Q_n>0\). The trajectory cannot cease first while \(P\le H\): (6)
bounds its integrated squared velocity by \(H\), and its length on
\([r,s]\) is at most \(\sqrt{(s-r)H}\). At a finite maximal endpoint
therefore the state has a finite limit, where its polynomial vector
field continues it. On \(s\le U,P\le H\), each normalized parameter
displacement is at most \(\sqrt{UH}\).

The same argument holds for the population product Hilbert space,
using first-layer/readout \(L^2\) and learned hidden-increment
Hilbert--Schmidt norms. The initialized operator is bounded. The
linear model's vector field is locally Lipschitz on this product
space, because its operations are bounded operator actions and
rank-one products. Thus the bounded-output continuation argument
also establishes population existence through every finite target,
without invoking the manuscript's small-label theorem at large labels.

Returning to physical time gives
\[
 |f_n(t,x_0)-Y|\le Ye^{-2Q_nt},\qquad
 0\le s_n(t)\le s_{n,*}\le Y/Q_n .
 \tag{8}
\]
All states converge to the finite controlled state at \(s_{n,*}\).

## 3. Quantitative Gaussian moments, with explicit growth in order

Set \(C_p=(p+1)^{-1}\binom{2p}{p}\). For \(k\ge0\), write \(p=k+1\).
Independence of \(a_0\sim N(0,I_n)\) and \(W_0\) yields
\[
 \nu_{n,k}:=\int\lambda^kd\nu_n
      =\frac1n a_0^\top(W_0^\top W_0)^p a_0 .
 \tag{9}
\]
We prove
\[
 \|\nu_{n,k}-C_{k+1}\|_{L^2}
        \le C(4p)^p/\sqrt n,\qquad
 \|q_n-1\|_{L^2}=\sqrt{2/n}.
 \tag{10}
\]

Gaussian integration by parts, iterated on products, gives the pairing
formula for even Gaussian moments. Expand
\(n^{-1}\operatorname{tr}(W_0^\top W_0)^p\) as an alternating closed
walk of length \(2p\) in row/column indices. A pairing identifies
both endpoints of each paired matrix entry and contributes \(n^{-p}\).
Its connected quotient graph has at most \(p\) edges and \(p+1\) free
vertices. With the trace normalization, each pairing contributes at
most one.

The terms with \(p+1\) vertices are trees, with every edge traversed
twice. First visits and returns form a Dyck path: each return must
close the last still-open edge of a tree. Conversely each such path
defines one nested pairing. There are \(C_p\) of them. Every other
pairing has at most \(p\) vertices and contributes at most \(1/n\).
There are \((2p-1)!!\le(2p)^p\) pairings. Consequently
\[
 \left|\mathbb E\frac1n\operatorname{tr}(W_0^\top W_0)^p-C_p\right|
       \le (2p)^p/n .
 \tag{11}
\]
Index assignments with accidentally equal distinct vertices are included
in these sums; they need not be excluded for this counting argument.

For the variance, expand two trace walks. Pairings without a pair
across the walks are exactly the product of expectations and cancel.
Each remaining pairing makes the quotient graph connected, with at most
\(2p\) edges and \(2p+1\) vertices. The two trace normalizations give
at most \(1/n\) per pairing. Hence
\[
 \operatorname{Var}\left(\frac1n\operatorname{tr}(W_0^\top W_0)^p\right)
       \le (4p-1)!!/n\le (4p)^{2p}/n .
 \tag{12}
\]
Conditional Gaussian averaging over \(a_0\) gives conditional mean
\(\operatorname{tr}(W_0^\top W_0)^p/n\) and conditional variance
\(2\operatorname{tr}(W_0^\top W_0)^{2p}/n^2\). The same one-trace bound
makes the expectation of this variance at most \(2(4p)^{2p}/n\).
The conditional variance identity and (11)–(12) prove (10). Its
row-norm statement follows directly from independent Gaussian squares.
These loose bounds are valid for all orders and widths.

We also use a fixed operator event
\(\|W_0\|_{\rm op}\le K\) with probability \(1-Ce^{-cn}\).
A proof needs only two \(1/4\)-nets of the unit sphere, each with at most
\(9^n\) points by the disjoint-ball volume argument. The operator norm
is at most twice the largest absolute bilinear form on the nets.
Each form is \(N(0,1/n)\), giving failure probability at most
\(2\cdot81^n e^{-nK^2/8}\); choose a sufficiently large fixed \(K\).

## 4. Canonical population identification

Let \(\nu\) be the probability measure on \([0,4]\) with density
\[
 d\nu/d\lambda=(2\pi)^{-1}\sqrt{\lambda(4-\lambda)}
                              \mathbf1_{(0,4)}(\lambda).
 \tag{13}
\]
Its moments are
\[
 \int\lambda^k d\nu=C_{k+1}.
 \tag{14}
\]
For detail, substitution \(\lambda=4r\) gives
\(4^{k+2}B(k+3/2,3/2)/(2\pi)\); evaluation by the beta-integral
recursion gives \((k+2)^{-1}\binom{2k+2}{k+1}\).
In particular its mass is one.

Replace \(q_n,\nu_n\) in (5) by \(1,\nu\), and call the solution
\(\psi,R,P\). This is the canonical population reduction. Indeed
the manuscript's initialized Gaussian operator and Gaussian first-row
field \(a_0\) satisfy
\[
 \langle W_0a_0,(W_0W_0^*)^kW_0a_0\rangle=C_{k+1}.
\]
The same finite pairing calculation and fixed-program limiting rule
give this identity. The operator is bounded (its norm bound two also
follows from POPULATION_RESPONSE_TRANSPORT). The map from polynomials
of \(W_0W_0^*\) applied to \(W_0a_0\) to polynomials of \(\lambda\)
in \(L^2(\nu)\) is an isometry by (14). It intertwines the bounded
operators on this cyclic subspace. Completing this isometry, using
polynomial approximation on the compact support, identifies (4) with
(5) using \(1,\nu\). The nonlinear coefficient depends only on the norm,
so the cyclic subspace is invariant.

The population controlled energy argument has \(Q=1\). It proves
existence until every finite target is reached and \(P'\ge1\).
A direct check in the scalar representation is the conserved identity
\[
 \int(\psi')^2d\nu-\int(\lambda+1)\psi^2d\nu-R^4=1 ,
 \tag{15}
\]
obtained by differentiating. It also supplies a continuation bound
when \(P\) and control time stay bounded.

## 5. Factorial summation closes the entire initialization bias

Fix \(Y\), and let \(U\) be the population control time with
\(P(U)=Y+1\); then \(U\le Y+1\). Stop the finite path at \(U\)
or its first value \(P_n=Y+2\). Restrict initially to \(q_n\le2\)
and \(\|W_0\|_{\rm op}\le K\). The controlled energy bound gives
a deterministic \(A_Y\) bounding both potentials \(q_n+2R_n^2\)
and \(1+2R^2\) before this stop.

For every continuous \(0\le a(s)\le A_Y\), let
\(\psi_a''=(\lambda+a(s))\psi_a\), with initial data \(0,1\).
The Volterra expansion has nonnegative coefficients in \(\lambda\).
Coefficientwise comparison with constant potential \(A_Y\) gives
\[
 [\lambda^k]\psi_a(s,\lambda)
    \le \cosh(U\sqrt{A_Y})\,U^{2k+1}/(2k+1)!,
\quad
 [\lambda^k]\psi_a'(s,\lambda)
    \le \cosh(U\sqrt{A_Y})\,U^{2k}/(2k)! .
 \tag{16}
\]
To check the first bound, expand
\(\sinh(s\sqrt{\lambda+A_Y})/\sqrt{\lambda+A_Y}\).
Use
\(\binom{k+r}{r}\le\binom{2k+2r+1}{2r}\) in the coefficient indexed
by \(k+r\), and sum \(A_Y^rU^{2r}/(2r)!\).
The derivative bound follows from the corresponding hyperbolic-cosine
series. Volterra iteration proves coefficientwise comparison for a
nonconstant potential.

The reciprocal-factorial convolution in either \(\psi_a^2\) or
\(\psi_a\psi_a'\) is an odd-binomial sum with total index \(2k+2\)
or \(2k+1\). Therefore, for some constants \(C_Y,B_Y\ge1\), both
products have coefficients bounded by
\[
 C_Y B_Y^k/(2k)! ,
 \tag{17}
\]
uniformly over all these potentials and \(s\le U\).

Define
\[
 E_n=|q_n-1|+
      \sum_{k\ge0}\frac{B_Y^k}{(2k)!}|\nu_{n,k}-C_{k+1}|.
 \tag{18}
\]
Minkowski and (10) give
\[
 \|E_n\|_{L^2}\le C_Y/\sqrt n.
 \tag{19}
\]
The required scalar series converges:
\(\sum_k B_Y^k(4(k+1))^{k+1}/(2k)!\) has successive ratio tending
to zero. Thus factorial decay of the exact spectral evolution absorbs
the growth of all Gaussian moment errors. No unspecified mean-bias
remainder is retained.

Equation (17) bounds the difference of integrating either product
against \(\nu_n\) and \(\nu\) by \(C_YE_n\), even when \(a\) is
the actual random finite potential. The coefficient bound is uniform
over such potentials. Absolute summability, or positivity followed
by the moment bounds, justifies exchanging the series and integrals.

For \(0\le\lambda\le4\), subtract the scalar second-order equations
for the two potentials and write them as first-order systems.
Their solutions and coefficients are bounded before the stop, giving
\[
 |\psi_n(s,\lambda)-\psi(s,\lambda)|
 +|\psi_n'(s,\lambda)-\psi'(s,\lambda)|
 \le C_Y\int_0^s
          [|q_n-1|+|R_n(v)^2-R(v)^2|]\,dv .
 \tag{20}
\]
First compare integration of \(\psi_n^2\) against the two measures
using (17), then use (20) under \(\nu\). Integral Gronwall gives
\[
 \sup_{s\ {\rm before\ stop}}|R_n^2-R^2|
       +\sup_{s\ {\rm before\ stop}}|P_n-P|\le C_Y E_n .
 \tag{21}
\]
If \(C_YE_n<1/2\), the exit \(P_n=Y+2\) would contradict
\(P\le Y+1\) and (21). Bounded-output continuation excludes an
earlier blowup. Thus (21) holds through \(U\), where \(P_n(U)>Y\),
so both fitted controls lie in \([0,U]\). Also \(Q_n=\nu_{n,0}\ge1/2\)
when \(E_n\) is sufficiently small. By (19) and the operator event,
the exceptional probability is at most \(C_Y/n+Ce^{-cn}\).

## 6. Equal physical times and passive inputs

Let \(s_n,s_\infty\) solve
\[
 \dot s_n=2[Y-P_n(s_n)],\qquad
 \dot s_\infty=2[Y-P(s_\infty)],\qquad s_n(0)=s_\infty(0)=0.
\]
On the preceding event \(P_n'\ge1/2\). Subtract the equations,
use the mean-value integral for \(P_n(s_n)-P_n(s_\infty)\), and
integrate the resulting damped scalar equation. It gives
\[
 \sup_{t\ge0}|s_n(t)-s_\infty(t)|
      \le2\sup_{s\le U}|P_n(s)-P(s)|\le C_YE_n .
 \tag{22}
\]
The derivative of \(P\) is bounded on \([0,U]\), so the training
prediction error at equal physical times is also at most \(C_YE_n\),
including the fitted endpoint.

Choose an orthonormal input basis beginning with \(x_0/\sqrt d\).
The other columns \(a_j\) of \(A_0\) are independent standard
Gaussians, independent of the trained state on \(x_0\), and never
move. Set \(c(x)=\langle x,x_0\rangle/d\) and
\(b_j(x)=\langle x,e_j\rangle/\sqrt d\). Exactly,
\[
 f_n(t,x)=c(x)P_n(s_n(t))
       +n^{-1/2}\sum_{j=1}^{d-1}b_j(x)a_j^\top\beta_n(s_n(t)),
 \qquad\beta_n(s)=W(s)^\top u(s).
 \tag{23}
\]
The controlled energy/operator bounds and (3) imply
\(\beta_n(0)=0\), \(\sup_{s\le U}\|\beta_n'(s)\|\le C_Y\).
Conditional on the training initialization, the fundamental theorem
of calculus, Cauchy--Schwarz and the Gaussian second moment give
\[
 \mathbb E\sup_{s\le U}
  \left|n^{-1/2}\sum_j b_j(x)a_j^\top\beta_n(s)\right|^2
 \le\frac{U}{n}\int_0^U\sum_j b_j(x)^2\|\beta_n'(s)\|^2ds
 \le\frac{C_Y}{n}\frac{\|x-c(x)x_0\|^2}{d}.
 \tag{24}
\]
The canonical population predictor is
\[
 f_\infty(t,x)=c(x)P(s_\infty(t)).
 \tag{25}
\]
This follows either from (23)–(24) and the identified canonical
scalar limit, or from input-rotation symmetry of the deterministic
linear population predictor. Such symmetry fixes \(x_0\) and
reverses every orthogonal direction.

Integrating (24), using (19), (21)–(23), gives
\[
 \mathbb E\left[\mathbf1_{\rm good}
      \int\sup_{t\ge0}|f_n(t,x)-f_\infty(t,x)|^2d\mu(x)\right]
       \le C_{Y,\mu}/n,\qquad
 \Pr({\rm good}^c)\le C_Y/n+Ce^{-cn}.
 \tag{26}
\]
The good event depends only on the training initialization, so it
does not change the conditional Gaussian calculation for \(a_j\).
Only the second query moment is used. Markov's inequality proves
(1); fitting and (25) prove (2). Constants may grow with the fixed
label magnitude, but never with width or elapsed time.

## 7. Interpretation and provenance

The failed negative idea was that large fixed labels might force
one-sample linear training to select an exceptional spectral mode
and have a slow population limit. The exact balances instead give
a shared scalar potential acting on the initialized spectral measure.
Its response is analytic in the spectral variable on every
bounded-output segment, so summing quantitative Gaussian moment
errors closes both fluctuations and bias.

This is a direct positive result obtained from that negative test.
It is not a claim about general nonlinear multi-sample training.
Those questions remain open outside the scopes proved here.

Inputs: the current canonical manuscript and its Gaussian population
construction, this study's scalar energy identity and population
operator construction, and the elementary Gaussian calculations
proved above. The coordinator and geometry-route author independently
derived (4), then exchanged the identity before this rate proof.
The moment summation and complete rate proof were developed by the
coordinator. No external random-matrix rate theorem, experiment,
manuscript edit, promotion or Git write was used.


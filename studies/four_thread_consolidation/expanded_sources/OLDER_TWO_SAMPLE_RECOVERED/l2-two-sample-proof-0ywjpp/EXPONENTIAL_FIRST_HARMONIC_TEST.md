# Exponential first layer: exact first reverse law and conditional damping

2026-09-06. Bounded analytic sidecar. No experiments, other agents, project
history, or global population-existence assumption. The only mathematical
dependency read was `HARMONIC_FULL_RESPONSE_TEST.md`, which is under audit.
Its initial causal-source conventions are used below, but all needed
coefficients and integrals are derived here. The procedural
`solve-math-rigorously` skill was also read. Only this file is written.

**Verdict.** The complete first label-weighted reverse query has a strictly
positive exponential self coefficient at every fixed allowed angle,
despite its negative current block. Rare initial coordinates therefore
point outward.
More strongly, the first nonzero explicit bottom update has infinite
positive exponential-feature moments at every positive mesh: the next
uncut Gaussian covariance cannot be selected. These are exact statements
about this finite causal program, not trained continuous-flow blowup.
For the prescribed continuous ODE, the current term does yield a coercive
radial bound, and a stronger feature cap under a forcing-to-damping bound.
Those useful conditional estimates do not establish the required bound
on the actual trained retarded forcing, even on a common small interval.

The calculation proceeds through the first reverse query, its Gaussian
covariance, and the rare-coordinate test. The continuous estimates are
proved separately so that no mesh identity is promoted to an existence
or continuation theorem for the trained population.

## 1. Initialization and the first top integrals — exact finite prefix

Let

\[
 C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\quad -1<\rho<1,
 \qquad Y=\operatorname{diag}(1,-1),\qquad \varepsilon=1/20.
\]

All exponentials of vectors below are componentwise. The specified
initialization gives

\[
 G\sim N(0,C),\qquad F_a=e^{G_a},\qquad
 K=E[FF^T]=\begin{pmatrix}v&t\\t&v\end{pmatrix},
 \quad v=e^2,\quad t=e^{1+\rho}.
 \tag{1}
\]

Indeed, completing the square in the Gaussian density gives
\(E e^{u^TG}=e^{u^TCu/2}\); use \(u=2e_a\) or \(u=(1,1)^T\).
In particular all initial feature moments are finite. Set

\[
 \chi=v-t>0,\qquad c=e^{-\chi}\in(0,1),\qquad
 \alpha=\varepsilon^2c>0,\qquad
 \kappa=\varepsilon^2(1-c)>0.
 \tag{2}
\]

The initial top pair is \(X\sim N(0,K)\), on the second neuron
population. Define

\[
 h(x)=\varepsilon(\sin x+\cos x),\quad
 p(x)=h'(x)=\varepsilon(\cos x-\sin x),\quad p'=-h,
 \qquad D=h(X_1)-h(X_2).
 \tag{3}
\]

The constant in \(\phi_2=1+h\) cancels from the label difference.
The initial top and bottom populations are distinct; expectations below
are on the population carrying the displayed variables.

The exact top second moments are

\[
 \Gamma:=E[p(X)p(X)^T]
   =E[h(X)h(X)^T]
   =\varepsilon^2\begin{pmatrix}1&c\\c&1\end{pmatrix},
 \qquad E[D h(X_a)]=y_a\kappa,\qquad ED^2=2\kappa.
 \tag{4}
\]

To verify these identities without factoring dependent variables, use

\[
 p(x)p(z)=\varepsilon^2\{\cos(x-z)-\sin(x+z)\},\qquad
 h(x)h(z)=\varepsilon^2\{\cos(x-z)+\sin(x+z)\}.
\]

Centered Gaussian symmetry kills the sine term, and
\(\operatorname{Var}(X_1-X_2)=2\chi\) gives
\(E\cos(X_1-X_2)=e^{-\chi}\). For the diagonal, use
\(p(x)^2=\varepsilon^2(1-\sin 2x)\) and
\(h(x)^2=\varepsilon^2(1+\sin 2x)\). Subtraction proves the
remaining identities in (4).

## 2. The whole first reverse query — exact finite prefix

Use an explicit feature-Euler mesh of length \(\Delta\) and put
\(\lambda=\Delta/2\). Let \(M_k\) denote the trained second-layer
matrix at mesh index \(k\), to distinguish its layer from its time index.
The normalized tensor \(u\otimes v\) acts by
\(x\mapsto uE[vx]\); its finite-width version is \(uv^T/n\).
The relevant mesh increments are

\[
 \begin{aligned}
 M_{k+1}-M_k&=\lambda\sum_b y_b\delta_{kb}\otimes F_{kb},\\
 w_{k+1}-w_k&=\lambda\sum_b y_b[1+h(Z^2_{kb})],\\
 Z^1_{k+1}-Z^1_k&=\lambda C\operatorname{diag}(e^{Z^1_k})Yq_k.
 \end{aligned}
 \tag{5}
\]

These are bookkeeping equations for the specified finite causal
Gaussian program. No width-limit identification is invoked.

The population readout root is exactly zero. Consequently

\[
 w_0=0,\quad\delta_0=q_0=0,\quad M_1=M_0,\quad
 Z^1_0=Z^1_1=G,\quad F_{0a}=F_{1a}=F_a,\quad Z^2_0=Z^2_1=X,
\]
\[
 w_1=\lambda D,\qquad
 \delta_{1a}=\lambda Dp(X_a),\qquad
 E[w_1(1+h(X_a))]=y_ag_1,\quad g_1=\lambda\kappa.
 \tag{6}
\]

The equality of attained top values is not an identification of their
formal source slots. Write those slots as \(\xi_0,\xi_1\).
Source derivatives freeze the deterministic coefficients and Gaussian
covariances, and are evaluated only after differentiation.

Here is the reverse rule, with the learned term explicitly retained:

\[
 q_{ka}=\zeta_{ka}+\sum_{r\le k,b}B_{ka,rb}F_{rb},\qquad
 B_{ka,rb}=E[\partial_{\xi_{rb}}\delta_{ka}]
    +\lambda\mathbf1_{r<k}y_b E[\delta_{ka}\delta_{rb}].
 \tag{7}
\]

The Gaussian source selection is
\(E\zeta_{ka}\zeta_{rb}=E\delta_{ka}\delta_{rb}\), with the
reverse Gaussian group independent of \(G\). The learned summand in
(7) follows directly from

\[
 M_k-M_0=\lambda\sum_{r<k,b}y_b\delta_{rb}\otimes F_{rb}:
\]

its transpose acting on \(\delta_{ka}\) gives precisely that summand
times \(F_{rb}\). Thus the learned memory is not absorbed into the
source response or omitted.

The first forward return is also well defined. A formal initial reverse
impulse, although its attained variance is zero, gives

\[
 \partial_{\zeta_{0b}}F_{1a}
     =\lambda C_{ab}y_b F_aF_b.
\]

Adding the forward learned term yields

\[
 A_{10}=\lambda(K+C\odot K)Y
   =\lambda\begin{pmatrix}2v&(1+\rho)t\\(1+\rho)t&2v\end{pmatrix}Y.
 \tag{8}
\]

Its attained action is \(A_{10}\delta_0=0\), and
\(\partial_{\xi_0}\delta_0=0\). Therefore
\(\partial_{\xi_0}Z^2_1=0\). Differentiation of (6) in the
separate source slots gives

\[
 \begin{aligned}
 \partial_{\xi_{0b}}\delta_{1a}
     &=\lambda y_b p(X_b)p(X_a),\\
 \partial_{\xi_{1b}}\delta_{1a}
     &=-\lambda\mathbf1_{a=b}D h(X_a).
 \end{aligned}
\]

Using (4), the complete coefficient blocks are

\[
 B_{10}=\lambda\Gamma Y,\qquad
 B_{11}=-\lambda\kappa Y=-g_1Y.
 \tag{9}
\]

At this mesh the learned transpose term in (7) is exactly zero because
its only historical factor is \(\delta_0=0\). Its first possible
nonzero occurrence is at index 2. Inserting a term involving
\(E\delta_1\delta_1^T\) into \(q_1\) would instead introduce a
same-time matrix update and change this explicit causal mesh.

Let \(\eta\) be a centered Gaussian vector, independent of \(G\), with

\[
 \Sigma_{ab}:=E\eta_a\eta_b=E[D^2p(X_a)p(X_b)].
 \tag{10}
\]

The covariance of this centered Gaussian is the **uncentered second
moment** of \(Dp(X)\), as prescribed by (7); it is not in general
\(\operatorname{Cov}(Dp(X))\). No mean is subtracted in (10), and
\(\eta\) is not identified with that non-Gaussian vector.
Equations (7)-(10) give the exact complete first nonzero reverse law:

\[
 \begin{aligned}
 q_1
 &=\lambda\eta+\lambda\Gamma YF-\lambda\kappa YF\\
 &=\lambda\left\{\eta+
       \alpha(F_1-F_2)\begin{pmatrix}1\\1\end{pmatrix}\right\}.
 \end{aligned}
 \tag{11}
\]

In particular, the negative current term has already been included in
(11). It leaves \(\Gamma-\kappa I=\alpha\mathbf1\mathbf1^T\).
For the label-weighted forcing convention in the question, set

\[
 \begin{aligned}
 Q_1&:=\lambda\{Y\eta+Y\Gamma YF\}\\
 &=\lambda\begin{pmatrix}
     \eta_1+\varepsilon^2(F_1-cF_2)\\
     -\eta_2+\varepsilon^2(F_2-cF_1)
   \end{pmatrix}.
 \end{aligned}
 \tag{12}
\]

Then exactly \(Yq_1=Q_1-g_1F\). This is the historical source
response plus Gaussian forcing, with zero learned transpose memory at
this index, followed by the current term \(-g_1F\).

## 3. Closed Gaussian covariance — exact finite prefix

No expectation in (10) needs to remain unevaluated. Introduce

\[
 U=(X_1+X_2)/2,\qquad V=(X_1-X_2)/2.
\]

They are independent centered Gaussians with variances
\((v+t)/2\) and \(\chi/2\), respectively. Set
\(r_0=e^{-4(v+t)}\), and define the positive constants

\[
 a_+=\frac{\varepsilon^4}{4}(3-r_0)(1-c^4),\qquad
 a_-=\frac{\varepsilon^4}{4}(1+r_0)(3-4c+c^4).
 \tag{13}
\]

The answer is

\[
 \Sigma=\begin{pmatrix}a_++a_-&a_+-a_-\\a_+-a_-&a_++a_-\end{pmatrix}.
 \tag{14}
\]

Equivalently, \(\eta_+=(\eta_1+\eta_2)/2\) and
\(\eta_-=(\eta_1-\eta_2)/2\) are independent Gaussians with
variances \(a_+\) and \(a_-\). Positivity follows from
\(0<c<1\), \(0<r_0<1\), and
\(3-4c+c^4=(1-c)^2(c^2+2c+3)>0\).

For verification, the addition formulas give

\[
 D=2p(U)\sin V,\quad
 p(X_1)=p(U)\cos V-h(U)\sin V,\quad
 p(X_2)=p(U)\cos V+h(U)\sin V.
\]

The mixed term in the square of either last expression has zero
expectation after multiplying by \(D^2\), because it is odd in
\(V\). The four required integrals are

\[
 \begin{aligned}
 E p(U)^4&=\tfrac{\varepsilon^4}{2}(3-r_0),&
 E[p(U)^2h(U)^2]&=\tfrac{\varepsilon^4}{2}(1+r_0),\\
 E[\sin^2V\cos^2V]&=(1-c^4)/8,&
 E\sin^4V&=(3-4c+c^4)/8.
 \end{aligned}
\]

For example, \(p(U)^4=\varepsilon^4(1-\sin2U)^2\) and
\(p(U)^2h(U)^2=\varepsilon^4\cos^2 2U\).
The identities for \(V\) follow from the double-angle formulas and
\(E\cos(2V)=c\), \(E\cos(4V)=c^4\).
Thus the diagonal of (10) is

\[
 4E p(U)^4 E[\sin^2V\cos^2V]
 +4E[p(U)^2h(U)^2]E\sin^4V=a_++a_-,
\]

and the off-diagonal has the minus sign between these terms. This proves
(13)-(14), retaining every dependence within the top population.

For completeness, the mean that must not be subtracted in (10) is

\[
 E[Dp(X)]=\mu\begin{pmatrix}-1\\1\end{pmatrix},\qquad
 \mu=\varepsilon^2\{e^{-(v+t)}-e^{-2v}\}>0.
\]

Indeed \(h(x)p(z)=\varepsilon^2\{\sin(x-z)+\cos(x+z)\}\),
so \(E[h(X_a)p(X_a)]=\varepsilon^2e^{-2v}\) and
\(E[h(X_1)p(X_2)]=E[h(X_2)p(X_1)]=\varepsilon^2e^{-(v+t)}\).
Thus \(\operatorname{Cov}(Dp(X))\) would subtract
\(\mu^2\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\) from (14);
the reverse Gaussian covariance does not.

## 4. Rare initial coordinates and loss of the next mesh covariance

**Exact finite-prefix sign.** Hold \(G_2\) and \(\eta\) bounded and
let \(G_1=x\to+\infty\). Then (11)-(12) give

\[
 \frac{q_{1,1}}{\lambda e^x}\longrightarrow\alpha,
 \qquad \frac{q_{1,2}}{\lambda e^x}\longrightarrow\alpha,
 \qquad
 \frac{Q_{1,1}}{g_1e^x}\longrightarrow
       \frac{\varepsilon^2}{\kappa}=\frac1{1-c}>1.
 \tag{15}
\]

The historical self term therefore exceeds the current damping on
this tail. Smallness of \(c\) does not alter its strictly positive sign
for any fixed \(-1<\rho<1\).

The first nonzero explicit bottom update is the coordinatewise finite
random vector

\[
 \begin{aligned}
 \widetilde G_1:=Z^1_{2,1}
 &=G_1+\lambda^2\{F_1\eta_1-\rho F_2\eta_2
               +\alpha(F_1-\rho F_2)(F_1-F_2)\},\\
 \widetilde G_2:=Z^1_{2,2}
 &=G_2+\lambda^2\{\rho F_1\eta_1-F_2\eta_2
               +\alpha(\rho F_1-F_2)(F_1-F_2)\}.
 \end{aligned}
 \tag{16}
\]

Hence

\[
 \frac{\widetilde G-G}{\lambda^2 e^{2x}}
     \longrightarrow\alpha\begin{pmatrix}1\\\rho\end{pmatrix}.
 \tag{17}
\]

There is also an outward metric-radial sign at the state \(G\). For
the instantaneous vector \(\tfrac12 C\operatorname{diag}(F)Yq_1\),
with the attained \(q_1\), the derivative of \(Z^TC^{-1}Z\) is

\[
 \lambda\{G_1F_1[\eta_1+\alpha(F_1-F_2)]
      -G_2F_2[\eta_2+\alpha(F_1-F_2)]\}
       \sim\lambda\alpha x e^{2x}>0.
 \tag{18}
\]

This is a test of the first attained vector, not a description of that
vector along a later continuous trajectory.

**Exact obstruction to extending this uncut finite Gaussian program.**
For every \(\lambda>0\) and every \(m>0\),

\[
 E e^{m\widetilde G_1}=E e^{m\widetilde G_2}=+\infty.
 \tag{19}
\]

Here is a direct tail proof. Restrict to \(|G_2|\le B\) and
\(\|\eta\|_\infty\le M\), with any fixed \(B,M>0\).
The latter event has positive probability and is independent of \(G\).
Uniformly on this event, for sufficiently large \(G_1=x\),

\[
 F_1\eta_1-\rho F_2\eta_2
      +\alpha(F_1-\rho F_2)(F_1-F_2)
       \ge\tfrac\alpha2 e^{2x}.
\]

This follows by expanding the product: its leading term is
\(\alpha e^{2x}\), and every other term is bounded in magnitude by
a constant times \(e^x+1\). Since \(|\rho|<1\), the joint Gaussian
density on \(G_1=x\ge0, |G_2|\le B\) has a lower bound
\(b_B e^{-a_Bx^2}\) with positive constants. For example use
\(2|\rho|Bx\le x^2+\rho^2B^2\) in its density formula.
Consequently the expectation in (19) for coordinate 1 bounds below a
positive constant times

\[
 \int_R^\infty
    \exp\{mx+\tfrac{m\lambda^2\alpha}{2}e^{2x}-a_Bx^2\}\,dx
    =+\infty.
\]

For coordinate 2, restrict \(G_1\) and \(\eta\) to bounded sets
and let \(G_2\to+\infty\) in the second line of (16); its leading
term is again \(\lambda^2\alpha e^{2G_2}\). This proves (19).

Thus the next feature \(F_{2a}=e^{\widetilde G_a}\) lacks even a
first positive moment, and the required next forward Gaussian variance
\(E F_{2a}^2\) is infinite. This is not just an uncontrolled
Taylor remainder. Even the fresh forward-return coefficient would have
the formal expression

\[
 A_{2a,1b}
  =\lambda y_b(1+C_{ab})E[e^{\widetilde G_a}F_b].
 \tag{20}
\]

Indeed, differentiation in \(\zeta_{1b}\) gives
\(\partial_{\zeta_{1b}}\widetilde G_a=\lambda C_{ab}y_bF_b\),
and the learned forward term adds
\(\lambda y_b E[e^{\widetilde G_a}F_b]\).
The same tail event proves that each expectation in (20) is infinite:
the other initial feature is bounded below on the event, and the large
initial feature is at least one. In particular the diagonal coefficient
would require \(2\lambda y_a E[e^{\widetilde G_a}F_a]\), not a
finite number. Formula (20) diagnoses failure of the next coefficient;
it is not a defined finite coefficient block.

The initialized prefix through \(q_1\) is valid and has finite
polynomial moments of its ingredients. The vector \(\widetilde G\)
itself also has all polynomial moments. Exponentiating it is what
prevents the next population Gaussian selection. Thus neither the
bounded-activation finiteness argument nor the second-update response
expansion in the dependency can be imported for \(\phi_1=e^z\).
There is no defined later uncut mesh block in this calculation whose
learned transpose term could repair the earlier missing covariance.

This obstruction concerns a positive explicit mesh on the unbounded
population. It asserts neither a divergent finite-width coordinate nor
nonexistence or blowup of the trained continuous population flow.

## 5. Current damping in the continuous equation — conditional ODE results

Fix a finite interval \([0,T]\). Here \(Q:[0,T]\to\mathbb R^2\)
and \(g:[0,T]\to\mathbb R\) are prescribed functions, and \(Z\)
is any existing absolutely continuous solution of

\[
 Z'=\tfrac12 C\operatorname{diag}(e^Z)(Q-ge^Z),\qquad Z(0)=Z_0.
 \tag{21}
\]

In the trained notation, \(Q\) would include the label-weighted
Gaussian source, all historical source responses, and all learned
transpose memory. Prescribing it in this section makes no assertion
about its trained dependence on \(Z\) or its past.

The sign of the current term is the one derived in (9). More generally,
whenever a symmetric causal population law and its expectations exist,
the current-source derivative is \(-\delta_{ab}E[w h(Z^2_a)]\).
Exchange symmetry gives \(Ew=0\) and
\(E[w h(Z^2_a)]=y_ag\); multiplication by \(Y\) then gives
\(-g e^Z\) in (21). Positivity of \(g\) on a later interval is
an assumption for the following estimates, not a consequence of that
source-derivative identity.

### 5.1 A coercive radial bound

**Conditional statement.** Suppose \(g(s)>0\) for almost every
\(s\in(0,T]\), and

\[
 \int_0^T\left(g+\|Q\|_1+\frac{\|Q_+\|_2^2}{g}\right)ds<\infty,
 \tag{22}
\]

where \(Q_+\) is the componentwise positive part. Values at the single
point \(s=0\) do not enter this condition. Let

\[
 V=Z^TC^{-1}Z,\qquad R=\sqrt{1+V},\qquad r=|\rho|.
\]

Then

\[
 R(s)\le R(0)
   +\frac{\sqrt{1+r}}8\int_0^s\frac{\|Q_+(u)\|_2^2}{g(u)}\,du
   +\frac1{2e}\int_0^s(\|Q(u)\|_1+g(u))\,du.
 \tag{23}
\]

This is coercive in both coordinates, since the eigenvalues of \(C\)
are \(1\pm\rho\) and hence

\[
 \frac{\|Z\|_2^2}{1+r}\le V\le\frac{\|Z\|_2^2}{1-r}.
\]

To prove (23), cancel the sample metric before taking any absolute
values:

\[
 V'=\sum_{a=1}^2 Z_a e^{Z_a}(Q_a-ge^{Z_a}).
 \tag{24}
\]

If \(z\ge0\), completing the square gives
\(e^z Q-ge^{2z}\le Q_+^2/(4g)\). If \(z<0\), use
\((-z)e^z\le1/e\) and \((-z)e^{2z}\le1/(2e)\). Thus

\[
 V'\le\frac1{4g}\sum_a Z_a^+(Q_a^+)^2
          +\frac{\|Q\|_1}{e}+\frac ge.
\]

Since \(Z_a^+\le\|Z\|_2\le\sqrt{1+r}\,R\), division by
\(2R\ge2\) and integration prove (23). If needed, integrate first
from \(\delta>0\) and let \(\delta\downarrow0\), using (22)
and continuity of \(Z\).

The actual negative large-positive-coordinate term can also be retained:
the inequality \(uQ_+\le gu^2/2+Q_+^2/(2g)\) gives

\[
 V'+\frac g2\sum_a Z_a^+e^{2Z_a}
 \le\frac1{2g}\sum_a Z_a^+(Q_a^+)^2
       +\frac{\|Q\|_1}{e}+\frac ge.
 \tag{25}
\]

There is no uniformly negative radial drift in every direction. At
\(Q=0\), \(Z=(-L,-L)\), \(L>0\), (24) equals
\(2gL e^{-2L}>0\). The result is a coercive finite-interval bound,
not an inward-pointing assertion outside every sufficiently large ball.

### 5.2 A stronger feature cap under a relative forcing bound

**Conditional statement.** Suppose instead that \(g\ge0\),
\(g\in L^1[0,T]\), and there is a finite constant \(A\ge0\) such
that

\[
 \|Q(s)\|_\infty\le A g(s)\quad\hbox{for almost every }s\in[0,T].
 \tag{26}
\]

The constant may depend on the chosen neuron coordinate or its random
roots, but must bound the entire prescribed interval for that coordinate.
Put

\[
 \beta=\frac{1+r}{1-r},\qquad
 L=\max\{e^{Z_{01}},e^{Z_{02}},\beta A\}.
\]

Then the useful upper-tail estimate is

\[
 \max_a e^{Z_a(s)}\le L\qquad(0\le s\le T).
 \tag{27}
\]

For proof, let \(f(s)=\max_a e^{Z_a(s)}\). At almost every time
it differentiates through an active maximizing coordinate \(a\).
For the other coordinate \(b\), \(e^{Z_b}\le f\), so

\[
 \begin{aligned}
 Z_a'
 &\le\tfrac12\{(1+r)f\|Q\|_\infty-(1-r)gf^2\},\\
 f'&\le\tfrac12(1-r)g f^2(\beta A-f).
 \end{aligned}
\]

In the first inequality, the damping estimate is
\(f^2+\rho e^{2Z_b}\ge(1-r)f^2\); this handles either sign of
\(\rho\). The derivative of \((f-L)_+\) is nonpositive whenever
\(f>L\), and it starts at zero. Integration proves (27).

The negative tails are also bounded on the prescribed interval, since

\[
 \|Z(s)-Z_0\|_\infty
 \le\frac{1+r}{2}L
      \int_0^s(\|Q(u)\|_\infty+g(u)L)\,du
 \le\frac{1+r}{2}L(A+L)\int_0^s g(u)\,du.
 \tag{28}
\]

This follows directly from taking absolute values in (21) after using
(27). In particular, no finite escape is possible on this interval for
the prescribed ODE under (26). For continuous prescribed \(Q,g\),
these bounds also justify ordinary local continuation: \(Z\) stays
in a compact set, the right-hand side and its \(Z\)-derivative are
bounded there, and the integral equation extends from its finite endpoint
limit by local contraction on a sufficiently short time interval. This
is solely a statement about the prescribed finite-dimensional ODE.

For a random family of such equations on the same interval, (27) also
has a population consequence *if its premise holds*: if
\(E A^m<\infty\) and \(E\max_a e^{mZ_{0a}}<\infty\), then
\(E\sup_{s\le T,a} e^{mZ_a(s)}<\infty\). This stronger cap,
unlike a generic radial bound exponential in \(A\), can preserve
feature moments. The premise is the bound on \(Q/g\), not merely
the sign of the current term.

### 5.3 The singular origin and what the first mesh actually supplies

**Conditional near-origin analysis.** If
\(g(s)\sim\gamma s\) with \(\gamma>0\), the potentially singular
integral in (22) is of the form

\[
 \int_0^T\frac{\|Q_+(s)\|_2^2}{s}\,ds.
 \tag{29}
\]

A bound \(Q_+(s)=O(s^a)\) with any \(a>0\) makes (29)
integrable. Mere convergence to zero does not: one positive component
\(Q(s)=1/\sqrt{\log(e/s)}\) gives a divergent integral near zero.
A nonzero positive limiting component also fails (29). These failures
are failures of the hypotheses for (23); they are not necessary
conditions for every individual solution to exist. A continuous
prescribed equation with finite initial data can have local solutions
even when this particular estimate from zero is unavailable.

The stronger premise (26) needs \(Q=O(s)\) with a bound valid on
the chosen interval when \(g\sim\gamma s\). Thus the zero of \(g\)
does not itself invalidate damping, but dividing by \(g\) without a
compatible forcing estimate would be unjustified.

There is a conditional reason for the proposed slope of \(g\). If a
symmetric trained continuous population law exists with top coordinates
continuous at their initial values, then the bounded top activation gives

\[
 w(s)=\tfrac12\int_0^s
       [h(Z^2_1(u))-h(Z^2_2(u))]\,du,
 \qquad \frac{w(s)}s\longrightarrow\frac D2.
\]

Because \(|h|\le\sqrt2\varepsilon\), both \(w(s)/s\) and
\(h(Z^2_a(s))\) are bounded. Dominated convergence then yields

\[
 \frac{g(s)}s=E\left[\frac{w(s)}s h(Z^2_1(s))\right]
          \longrightarrow\frac\kappa2>0.
 \tag{30}
\]

This implication assumes the existing continuous law and its top
continuity; it does not construct that law or bound its reverse forcing.

**Exact mesh fact, followed by a conditional illustration.** At the
first mesh time \(s=\Delta=2\lambda\), (6) and (12) say exactly

\[
 g_1=\tfrac s2\kappa,\qquad
 Q_1=\tfrac s2 A_0,\qquad A_0=Y\eta+Y\Gamma YF.
 \tag{31}
\]

The first forcing coefficient obeys

\[
 \frac{\|A_0\|_\infty}{\kappa}
 \le A_*:=\frac{\|\eta\|_\infty+
                 \varepsilon^2(1+c)\max(F_1,F_2)}{\kappa}.
 \tag{32}
\]

For each fixed \(\rho\), \(A_*\) has all finite positive moments:
the Gaussian source has them, and
\(E e^{mG_a}=e^{m^2/2}\).

To test damping while retaining the evolving current exponential,
one may *prescribe* on a finite interval

\[
 Q(s)=\tfrac s2 A_0,\qquad g(s)=\tfrac s2\kappa,
 \qquad Z(0)=G.
 \tag{33}
\]

This is an illustrative forcing prescription, not the later trained
retarded law. For this equation (26) holds with \(A=A_*\), so

\[
 \sup_{s\le T,a} e^{Z_a(s)}
      \le\max\{F_1,F_2,\beta A_*\}.
 \tag{34}
\]

All its positive feature moments therefore remain finite on the
prescribed interval. The forcing and \(g\) vanish at compatible
rates at zero; the outward initial coefficient in (15) does not destroy
this continuous cap. This explicitly demonstrates why the mesh moment
failure (19) cannot be relabeled continuous-flow blowup.

Conversely, (31) supplies no estimate such as (26) for the *actual*
trained \(Q(s)\) on a common positive interval. Even a coordinatewise
first-order tangent, if separately established, would require additional
uniform domination to supply a random envelope with finite moments on
one interval for the whole population. The rare-coordinate divergence
in (19) specifically rules out importing the bounded-activation mesh
domination argument to fill that gap. There is no all-time control of
\(Q\) here.

## 6. Scope of the answer

| Result | Status |
|---|---|
| Initial \(K\), \(\Gamma\), \(\kappa\), and the closed covariance \(\Sigma\) | Exact in the initialized finite causal program |
| First reverse law (11), including the historical source response, current term, and zero learned transpose memory | Exact finite-prefix identity |
| Positive rare-coordinate self coefficient for every fixed \(-1<\rho<1\) | Exact first-query sign |
| Infinite feature moments after the first nonzero explicit bottom update | Exact obstruction to the next uncut Gaussian mesh selection |
| Coercive radial bound (23) | Conditional on (22) for prescribed forcing and an existing ODE solution |
| Feature cap and finite-interval escape bound (27)-(28) | Conditional on the relative forcing bound (26) |
| Slope \(g(s)/s\to\kappa/2\) | Conditional on an existing symmetric continuous population law with top continuity |
| Moment preservation under prescription (33) | Conditional illustrative ODE result, not a trained-law assertion |
| A common small-time trained population solution, actual control of \(Q\), or a global theorem | Not established |

Exponential first activation has real damping available for a suitably
controlled continuous forcing, including a useful cap compatible with
Gaussian/lognormal initial moments. It does not make the first canonical
attained reverse field dissipative on rare positive coordinates, and the
uncut explicit Gaussian mesh encounters an immediate moment obstruction.
The missing step for a trained small-time result is an actual common-
interval forcing estimate and a justified continuous construction; the
negative current block by itself provides neither.

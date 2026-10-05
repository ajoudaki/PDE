# Exact endpoint variability for canonical deep linear networks

2026-10-04. **Internally checked lower-bound construction.** This note
treats identity activation at every layer, a permitted special case of
the general strip-holomorphic bounded-derivative class. It preserves the
canonical Gaussian ensemble, zero readout, mean loss, mobilities, and
physical time. It proves an exact conditional endpoint law, an explicit
root-width lower bound, and a matching upper scale for the hardest label
direction. It is not a lower-bound theorem for every activation or every
data set in the general class.

Only docs/notation.qmd and the current study's
GENERAL_EXPLICIT_FITTING.md were read for this continuation. The complete
fitting theorem and proof were read, including its initialization event.
The canonical-notation and rigorous-math instructions were applied. No
source insertion theorem, outside-study result, or experiment is used.

## 1. Model and statement

Let \(L\ge2\), \(1\le m\le d\), and let
\(v_a=x_a/\sqrt d\in\mathbb R^d\) be unit vectors. Put
\[
 V=[v_1\ \cdots\ v_m],\qquad
 G=V^\top V,\qquad \gamma=\lambda_{\min}(G)>0,\qquad
 \lambda=\gamma/m,\qquad Y=\|y\|_2/\sqrt m.
 \tag{1}
\]
Thus \(V\) has rank \(m\). Let
\[
 \mathcal S=\operatorname{range}(V),\qquad k=d-m,\qquad
 a_y=\sqrt{y^\top G^{-1}y}.
 \tag{2}
\]
The new scalar \(a_y\) is the Euclidean norm of the unique vector in
\(\mathcal S\) fitting the labels by a linear predictor. It records the
actual label direction, rather than only the worst Gram eigenvalue.

All activations are \(\phi_j(z)=z\). With \(A\in\mathbb R^{n\times d}\),
hidden mixers \(W^{(2)},\ldots,W^{(L)}\in\mathbb R^{n\times n}\), and
readout \(w\in\mathbb R^n\), the network is
\[
 h^{(1)}(v)=Av,\qquad h^{(j)}(v)=W^{(j)}h^{(j-1)}(v),\qquad
 f_n(t,v)=w(t)^\top h^{(L)}(t,v)/n.
 \tag{3}
\]
Initially \(A\) has independent \(N(0,1)\) entries, the hidden mixers
have independent \(N(0,1/n)\) entries, all blocks are independent, and
\(w(0)=0\). The loss is \(m^{-1}\sum_a(f_n(v_a)-y_a)^2\), with
mobilities \((n,1,\ldots,1,n)\).

For this activation the population recursion has \(Q^{(j)}=G\) at every
layer. Hence the \(\gamma\) in (1) is exactly the original top-feature
gap, with no changed kernel or normalization. Identity is entire, has
bounded derivative on every strip, and has unbounded values.

Define the explicit depth constant
\[
 F_L=9^{2L-2}+4\sum_{j=0}^{L-2}9^{2j}
     =\frac{21\,9^{2L-2}-1}{20}.
 \tag{4}
\]
Assume
\[
 0<Y\le\frac{\lambda}{8\sqrt{F_L}}.
 \tag{5}
\]
In particular the stronger common small-label cap in the integrated study
is covered. There is no restriction on the signs of \(y_a\).

For two independent canonical initializations, let
\[
 D_\infty=\sup_{\|v\|_2=1}
       |f_n(\infty,v)-f_n'(\infty,v)|.
 \tag{6}
\]
Let \(N_{\rm lin}(\varepsilon)\) be the explicit threshold in Section 2.
For \(k\ge1\) and \(n\ge N_{\rm lin}(1/8)\),
\[
 \boxed{\displaystyle
 \Pr\left\{D_\infty\ge
               \frac{a_y}{2}\sqrt{\frac{d-m}{n}}\right\}
       \ge\frac1{16}.}
 \tag{7}
\]
The event in (7) includes existence and fitting of both endpoints.
Since the all-physical-time sphere supremum dominates \(D_\infty\), the
same lower bound holds for that stronger norm.

More precisely, on an active-initialization event of probability at least
\(1-2\varepsilon\), the conditional law is exactly
\[
 \boxed{\displaystyle D_\infty\ \stackrel{\rm law}{=}\ \sigma\,\chi_k,
 \qquad
 \frac{a_y}{\sqrt{2n}}\le\sigma
       \le\frac{2\sqrt2\,9^{L-1}Y}{\sqrt{\lambda n}}.}
 \tag{8}
\]
Here \(\chi_k\) is the Euclidean norm of \(k\) independent standard
Gaussians, and \(\sigma\) is measurable with respect to the active
initializations. The meaning of this conditioning is made exact in
Sections 3--5; it does not condition on the unused Gaussian coordinates.

If \(y\) lies in the \(\gamma\)-eigenspace of \(G\), then
\[
 a_y^2=\frac{\|y\|_2^2}{\gamma}=\frac{mY^2}{\gamma},
 \qquad
 \frac{a_y}{2}\sqrt{\frac{d-m}{n}}
 =\frac Y2\sqrt{\frac{m(d-m)}{\gamma n}}.
 \tag{9}
\]
Thus the lower and upper scales in (8) match in \(n,m,d,\gamma,Y\)
for this label direction, up to constants depending only on fixed depth.

## 2. An explicit fitting event independent of unused directions

Choose deterministic matrices \(U\in\mathbb R^{d\times m}\) and
\(U_\perp\in\mathbb R^{d\times k}\) whose columns are orthonormal bases
of \(\mathcal S\) and \(\mathcal S^\perp\). If \(k=0\), the second
matrix is empty. Define
\[
 A_{\mathcal S}=AU,\qquad A_\perp=AU_\perp,\qquad
 C=U^\top V.
 \tag{10}
\]
The matrix \(C\) is invertible and \(G=C^\top C\). The active normalized
inputs are the columns of \(C\), each of norm one.

By orthogonal invariance of each Gaussian row of \(A_0\),
\[
 A_{\mathcal S,0}\in\mathbb R^{n\times m}
 \quad\hbox{and}\quad
 A_{\perp,0}\in\mathbb R^{n\times k}
 \tag{11}
\]
have independent standard Gaussian entries and are independent of one
another and of all hidden mixers. Consequently the fitting theorem can
be applied in input dimension \(m\), using only
\((A_{\mathcal S,0},W_0^{(2)},\ldots,W_0^{(L)})\).

Here is its threshold specialized completely. For \(0<\varepsilon<1\),
set
\[
 e_0=\min(1/4,\lambda/2),\qquad
 P_0=(1+8^{L+1})^m,
 \]
\[
 \boxed{\displaystyle
 N_{\rm lin}(\varepsilon)=\left\lceil\max\left\{
 1,\,
 \frac{\log(8L/\varepsilon)}{8-2\log9},\,
 \frac{m\log9+\log(8/\varepsilon)}{8-\log9},\,
 \frac{192L^3(m^2+P_0)}{\varepsilon e_0^2}
 \right\}\right\rceil .}
 \tag{12}
\]
Indeed the fitting constants are \(b=0,s=1,t_2=0,H=1\), its covariance
Lipschitz constant is one, its propagation sum is \(L\), its fourth-moment
bound is 96, and its sphere-mesh radius is \(1/(4\,8^L)\). This produces
exactly (12) from the current study's quantitative initialization theorem.
All denominators in (12) are positive.

For \(n\ge N_{\rm lin}(\varepsilon)\), that theorem gives an event
\(\mathcal E\), measurable with respect to the active initialization
alone, with probability at least \(1-\varepsilon\). Under (5), on
\(\mathcal E\), the reduced network exists for every physical time,
its physical parameters converge, and its endpoint fits all labels.
Moreover, for all times and all unit \(u\in\mathbb R^m\),
\[
 \|A_{\mathcal S}(t)\|_{\rm op}/\sqrt n<9,\qquad
 \max_{j\ge2}\|W^{(j)}(t)\|_{\rm op}<9,\qquad
 \|h^{(j)}(t,u)\|_2/\sqrt n<2,
 \]
\[
 \|w(t)\|_2/\sqrt n\le2Y/\sqrt\lambda,\qquad
 \rho(t)\le Ye^{-\lambda t/2}.
 \tag{13}
\]
Because the first activation is identity, the layer-one feature statement
in (13) is sharper than its separate matrix cap:
\[
 \boxed{\|A_{\mathcal S}(t)\|_{\rm op}/\sqrt n\le2.}
 \tag{14}
\]
The same bound holds at infinity. Thus no extra random-matrix event is
needed to obtain the first-layer operator bound used in the lower bound.

This reduced event is essential. A fitting event requiring full
\(d\)-dimensional sphere bounds would generally depend on
\(A_{\perp,0}\), so conditioning on it would not preserve the Gaussian
law needed below. Neither (12) nor \(\mathcal E\) uses those coordinates.
The threshold depends on \(m,L,\gamma,\varepsilon\), and not on \(d-m\).

## 3. The active dynamics close and the other columns stay frozen

Define the effective vector
\[
 b(t)=\frac{W^{(2)}(t)^\top\cdots W^{(L)}(t)^\top w(t)}n.
 \tag{15}
\]
Then \(f_n(t,v)=v^\top A(t)^\top b(t)\). In particular the first
backward response is \(\delta_a^{(1)}=nb(t)\), independent of the
input. The exact canonical equations are
\[
 \dot A=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top
        =-\frac{2n}{m}b\,r^\top V^\top,
 \]
\[
 \dot W^{(j)}
 =-\frac2{mn}\sum_a r_a\delta_a^{(j)}h_a^{(j-1)\top},
 \qquad
 \dot w=-\frac2m\sum_a r_a h_a^{(L)}.
 \tag{16}
\]
The factors in (16) use precisely the mean loss and the prescribed
mobilities, with no change of time.

Since \(V^\top U_\perp=0\), (16) gives
\[
 \dot A_\perp=0,\qquad A_\perp(t)=A_{\perp,0}.
 \tag{17}
\]
All training forward values depend only on \(A_{\mathcal S}\), the
hidden mixers, and the readout. Multiplying the first equation of (16)
by \(U\) gives the first-weight equation of the reduced \(m\)-dimensional
canonical network with inputs \(U^\top v_a\). Its hidden and readout
equations are unchanged. Thus the active system is autonomous and never
uses \(A_{\perp,0}\).

Local uniqueness for its polynomial vector field and the fitting theorem
on \(\mathcal E\) identify the full trajectory with this active trajectory
and the frozen columns (17). The full parameters therefore exist and
converge on \(\mathcal E\), regardless of the values of the unused
Gaussian columns. The limit
\[
 b_\infty=\lim_{t\to\infty}b(t)
 \tag{18}
\]
is measurable with respect to the active initialization alone. This follows
also directly by taking a limit of the finite-time measurable solution
maps. Values outside \(\mathcal E\) can be assigned arbitrarily when
stating conditional laws restricted to \(\mathcal E\).

## 4. Fitting fixes the active coefficient and bounds the effective vector

Let \(\beta_\infty=A_\infty^\top b_\infty\) be the linear coefficient
in normalized input coordinates. Fitting says
\[
 y=V^\top\beta_\infty=C^\top A_{\mathcal S,\infty}^\top b_\infty.
 \]
Consequently
\[
 A_{\mathcal S,\infty}^\top b_\infty=C^{-\top}y,\qquad
 P_{\mathcal S}\beta_\infty=U C^{-\top}y=VG^{-1}y,
 \]
\[
 \|C^{-\top}y\|_2^2=y^\top G^{-1}y=a_y^2.
 \tag{19}
\]
The active component is deterministic, independently of the initialization
and the particular fitted parameter factorization.

Equation (14) and (19) imply the lower bound
\[
 a_y=\|A_{\mathcal S,\infty}^\top b_\infty\|_2
       \le2\sqrt n\,\|b_\infty\|_2,
 \qquad
 \boxed{\|b_\infty\|_2\ge\frac{a_y}{2\sqrt n}.}
 \tag{20}
\]
The operator and readout bounds in (13) give the complementary estimate
\[
 \boxed{\displaystyle
 \|b_\infty\|_2
 \le 9^{L-1}\frac{\|w_\infty\|_2}{n}
 \le\frac{2\,9^{L-1}Y}{\sqrt{\lambda n}}.}
 \tag{21}
\]
The upper estimate is the actual canonical training-energy bound propagated
through the hidden mixers. It does not require an implicit-bias or
minimum-parameter-norm characterization of the endpoint.

## 5. Exact conditional Gaussian law for two endpoints

Take two independent copies, with corresponding active sigma-algebras
\(\mathcal A,\mathcal A'\) and events \(\mathcal E,\mathcal E'\).
Their intersection has probability at least \(1-2\varepsilon\).
Conditional on \(\mathcal A,\mathcal A'\), both unused matrices
\(A_{\perp,0},A_{\perp,0}'\) remain independent standard Gaussian
matrices, by (11).

By (17)--(19), on \(\mathcal E\cap\mathcal E'\),
\[
 \beta_\infty-\beta_\infty'
 =U_\perp\big(A_{\perp,0}^\top b_\infty
                       -A_{\perp,0}'{}^\top b_\infty'\big).
 \tag{22}
\]
Each coordinate inside parentheses is a centered Gaussian of variance
\[
 \sigma^2=\|b_\infty\|_2^2+\|b_\infty'\|_2^2,
 \tag{23}
\]
and the coordinates are conditionally independent. Since \(U_\perp\)
is an isometry and a linear functional has sphere supremum equal to its
coefficient norm,
\[
 D_\infty=\|\beta_\infty-\beta_\infty'\|_2
 \quad\hbox{has conditional law}\quad \sigma\chi_k.
 \tag{24}
\]
In particular this is the full sphere difference, not merely its
restriction to unseen directions: the active difference is exactly zero.
Equations (20)--(21) imply (8).

The associated exact conditional second moment is
\[
 \mathbb E[D_\infty^2\mid\mathcal A,\mathcal A']
    =k\sigma^2,\qquad
 \frac{k a_y^2}{2n}\le k\sigma^2
             \le\frac{8\,9^{2L-2}kY^2}{\lambda n},
 \tag{25}
\]
on the active good event. No independence between trained coordinates is
asserted; only the independent, exactly unused initial columns are sampled
after conditioning.

For a single fixed unit direction \(v\in\mathcal S^\perp\), the
conditional endpoint difference is instead \(N(0,\sigma^2)\). Thus the
\(\sqrt{d-m}\) gain is specific to the sphere supremum. At training
inputs the endpoint difference is exactly zero.

## 6. Lower probabilities and matching high-dimensional bounds

For \(X=\chi_k^2\), direct Gaussian moments give
\[
 \mathbb E X=k,\qquad \mathbb E X^2=k^2+2k.
 \]
For completeness the elementary second-moment argument gives
\[
 \Pr\{X\ge k/2\}
 \ge\frac{(\mathbb E X-k/2)^2}{\mathbb E X^2}
 =\frac{k^2}{4(k^2+2k)}\ge\frac1{12}\quad(k\ge1).
 \tag{26}
\]
Indeed split the expectation of \(X\) below and above \(k/2\), then
apply Cauchy--Schwarz on the upper event. Combining (8), (24), and
(26) gives, for \(n\ge N_{\rm lin}(\varepsilon)\),
\[
 \Pr\left\{\mathcal E\cap\mathcal E',\
 D_\infty\ge\frac{a_y}{2}\sqrt{\frac{k}{n}}\right\}
           \ge\frac{1-2\varepsilon}{12}.
 \tag{27}
\]
Taking \(\varepsilon=1/8\) proves (7).

There is also an explicit high-probability version. The Gaussian integral
gives
\[
 \mathbb E e^{tX}=(1-2t)^{-k/2}\quad(t<1/2).
 \]
The inequalities
\[
 \log\mathbb E e^{t(X-k)}\le\frac{kt^2}{1-2t}
       \quad(0<t<1/2),\qquad
 \log\mathbb E e^{-t(X-k)}\le kt^2\quad(t>0)
 \]
follow by integrating \(1/(1-u)\) and \(1/(1+u)\), respectively.
Chernoff's inequality, with \(t=\sqrt{x}/(\sqrt k+2\sqrt{x})\)
for the upper tail and \(t=\sqrt{x/k}\) for the lower tail, gives
\[
 \Pr\{X>k+2\sqrt{kx}+2x\}\le e^{-x},\qquad
 \Pr\{X<k-2\sqrt{kx}\}\le e^{-x}.
 \tag{28}
\]
Thus, for \(n\ge N_{\rm lin}(\varepsilon)\), with probability at
least \(1-2\varepsilon-2e^{-x}\), both endpoints fit and
\[
 \frac{a_y}{\sqrt{2n}}\sqrt{(k-2\sqrt{kx})_+}
 \le D_\infty
 \le\frac{2\sqrt2\,9^{L-1}Y}{\sqrt{\lambda n}}
                          \sqrt{k+2\sqrt{kx}+2x}.
 \tag{29}
\]
Here \(r_+=\max(r,0)\). A negative lower probability is interpreted as
a vacuous assertion.

In particular, for \(0<\delta<1\), if
\[
 n\ge N_{\rm lin}(\delta/4),\qquad
 d-m\ge16\log(4/\delta),
 \]
take \(\varepsilon=\delta/4\) and \(x=\log(4/\delta)\) to obtain
with probability at least \(1-\delta\),
\[
 \boxed{\displaystyle
 \frac{a_y}{2}\sqrt{\frac{d-m}{n}}
 \le D_\infty
 \le4\,9^{L-1}Y\sqrt{\frac{m(d-m)}{\gamma n}}.}
 \tag{30}
\]
Indeed \(k-2\sqrt{kx}\ge k/2\) and
\(k+2\sqrt{kx}+2x\le13k/8\). For the hard label direction in (9),
the two sides of (30) differ only by the depth factor and an absolute
constant. For small \(d-m\), (27) supplies the nonvanishing-probability
lower bound without an artificial dimension restriction.

## 7. What this example establishes and what it does not

For fixed nonzero labels and fixed data with \(d>m\), the canonical fitted
endpoint has independent-copy fluctuations of root-width order. Along the
smallest-eigenvalue label direction, the explicit scale is
\[
 Y\sqrt{\frac{m(d-m)}{\gamma n}}.
 \]
All parameters are the original ones: no parameter or time rescaling is
introduced in the dynamics, and the query sphere \(\|x\|=\sqrt d\)
is exactly \(\|v\|=1\). There is no additional factor \(\sqrt d\)
from changing input notation.

The label-direction quantity \(a_y\) cannot in general be replaced in the
lower bound by \(Y\sqrt{m/\gamma}\): only the inequality
\(a_y\le Y\sqrt{m/\gamma}\) always holds, with equality for (9).
The result therefore provides a worst-direction dependence on the gap,
not a uniform hard-direction claim for every label vector.

If \(d=m\), then \(k=0\), (22) is identically zero, and all fitted linear
predictors agree on the entire input space. Hence this construction gives
no positive endpoint lower bound without unseen directions. If \(Y=0\),
the flow is stationary and its prediction is zero. These cases prevent
reading the construction as a universal positive endpoint fluctuation
theorem under the broad hypotheses alone.

The result supplies a rigorous lower benchmark inside the general
activation class. It neither proves a corresponding lower bound for every
nonlinear activation nor closes the general strict-root upper-bound gap.
Unlike the previous source-based upper bounds, the probability and width
conditions used for this example are fully explicit and require no
unquantified insertion threshold.

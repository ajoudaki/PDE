# The canonical Gaussian action has no universal higher-moment bound

This note concerns the initial matrix action on the generated coordinate
spaces in `LOCAL_ACTION_SPACE_AND_FLOW.md`. It refutes a universal
bounded (L^\infty\to L^p), or (L^p\to L^p), norm for (p>2).
It makes no assertion about the inputs reached by the trained flow and
does not refute the desired global mean-field or gradient-flow theorem.
No experiment is used.

## Statement

Write (W=W^{(3)}_0:L^2(\Omega_2)\to L^2(\Omega_3)) for the canonical
initial action, and (W^*) for its canonical transpose action. For every
finite (p>2),

\[
 \sup\{\|Wh\|_{L^p(\Omega_3)}:
        h\in L^\infty(\Omega_2),\ \|h\|_\infty\le1\}=\infty.
 \tag{1}
\]

The supremum already diverges over inputs obtained by a family of
three-query finite Gaussian programs. Each program uses only the
constant vector, (W,W^*), deterministic scalar coefficients, and
bounded smooth globally Lipschitz coordinate maps. Each of its outputs
has every finite moment. The same assertion holds with the layers and
the two directions interchanged.

In particular, there is no finite constant (C_p) such that
\(\|Wh\|_p\le C_p\|h\|_p\) for all such bounded generated inputs.
The Lipschitz constants of the coordinate maps are allowed to depend
on the member of this family. This result does not address estimates
with additional bounds on those constants or on reachable responses.

## A three-query program and its exact limiting law

Fix a smooth even function \(\psi:\mathbb R\to[0,1]\), equal to one
on \([-1/2,1/2]\) and equal to zero outside \([-1,1]\). For
\(0<\varepsilon\le1\), let

\[
 v_\varepsilon
 =\mathbb E\psi(G/\varepsilon)^2>0,
 \qquad G\sim N(0,1).
\]

This is a deterministic constant fixed before the program. Perform
the following calls in order, applying the indicated coordinate maps
between them:

\[
 Y=W\mathbf1\quad\text{on layer 3},\qquad
 e_\varepsilon=\psi(Y/\varepsilon),
\]
\[
 q_\varepsilon=W^*e_\varepsilon\quad\text{on layer 2},\qquad
 h_\varepsilon=\tanh(q_\varepsilon/\sqrt{v_\varepsilon}),
\]
\[
 T_\varepsilon=Wh_\varepsilon\quad\text{on layer 3}.
 \tag{2}
\]

The fixed-program rule proved in
`/tmp/L3_FIXED_MESH_SOURCE_IDENTIFICATION.md` gives

\[
 Y\sim N(0,1),\qquad
 q_\varepsilon\overset d=\sqrt{v_\varepsilon}G.
 \tag{3}
\]

Indeed, the response coefficient in the transpose call is

\[
 \mathbb E\frac{d}{dY}\psi(Y/\varepsilon)
 =\mathbb E[Y\psi(Y/\varepsilon)]=0,
\]

where Gaussian integration by parts applies to the bounded smooth
function and the final equality uses evenness. Thus the transpose
call has no response along the layer-2 constant input.

Define the positive constants

\[
 c=\mathbb E\operatorname{sech}^2G,
 \qquad \sigma^2=\mathbb E\tanh^2G.
\]

In the final forward call, the derivative of its input with respect
to the transpose Gaussian source has expectation
\(c/\sqrt{v_\varepsilon}\). The new forward Gaussian source has
variance \(\sigma^2\) and covariance with the first forward source
equal to \(\mathbb E\tanh G=0\). Those two forward sources are jointly
Gaussian. Consequently the exact population joint law on layer 3 is

\[
 (Y,T_\varepsilon)
 \overset d=
 \left(Y,\ \sigma H+
       \frac{c}{\sqrt{v_\varepsilon}}\psi(Y/\varepsilon)\right),
 \qquad Y,H\text{ independent }N(0,1).
 \tag{4}
\]

Here \(G\) describes the layer-2 marginal law in (3); no neuron
indices or random coordinates on distinct layers are paired. The
independent \(H\) in (4) is the final query's canonical Gaussian
innovation. It is not an extra input seed.

All nodes in (2) belong to the original generated spaces. The
construction note identifies finite calculations with real scalar
coefficients and arbitrary globally Lipschitz coordinate maps on
those same spaces, using its countable dense family and the
continuous (L^2) extensions. Thus (2) requires no enlargement of
the root tuple or of the population sigma-fields. Taking only
\(\varepsilon=1/k\) already proves (1).

## Direct finite-width conditional check

For completeness, (4) can also be read directly from two Gaussian
conditioning steps. Let (W_n) have iid (N(0,1/n)) entries, and put
\(y=W_n\mathbf1\), \(e_i=\psi(y_i/\varepsilon)\), and

\[
 a_n=\frac{y^Te}{n},\qquad v_n=\frac{e^Te}{n},\qquad
 P=I-\frac{\mathbf1\mathbf1^T}{n}.
\]

The coordinates of (y) are iid standard Gaussian. Conditional on

\(y\), the transpose answer satisfies

\[
 q=W_n^Te\ \overset d=\ a_n\mathbf1+\sqrt{v_n}Pg,
 \qquad g\sim N(0,I_n)\text{ independent of }y.
 \tag{5}
\]

On \(v_n>0\), conditional on \((y,q)\), the matrix law is

\[
 W_n\overset d=
 \frac{y\mathbf1^T}{n}
 +\frac{e(q-a_n\mathbf1)^T}{nv_n}
 +P_{e^\perp}\widetilde W_nP,
 \tag{6}
\]

where \(\widetilde W_n\) is a fresh matrix with the original Gaussian
law. The event \(v_n>0\) has probability tending to one for each
fixed \(\varepsilon\).

Let \(h_i=\tanh(q_i/\sqrt{v_\varepsilon})\),
\(m_n=n^{-1}\mathbf1^Th\), and
\(s_n=\|Ph\|_2/\sqrt n\). Multiplication in (6) gives the exact
conditional vector law

\[
 W_nh\overset d=
 m_ny+
 e\frac{(q-a_n\mathbf1)^Th}{nv_n}
 +s_nP_{e^\perp}g',
 \tag{7}
\]

with fresh standard Gaussian (g'). For fixed \(\varepsilon\), the
law of large numbers, (5), and the Lipschitz property of tanh give

\[
 a_n\to0,\quad v_n\to v_\varepsilon,\quad
 m_n\to0,\quad s_n^2\to\sigma^2,
\]
\[
 \frac{(q-a_n\mathbf1)^Th}{nv_n}
 \to\frac{\mathbb E[G\tanh G]}{\sqrt{v_\varepsilon}}
 =\frac{c}{\sqrt{v_\varepsilon}}.
\]

The last equality is integration by parts against the standard
Gaussian density. The projection removed from (g') has expected
squared norm divided by (n) equal to (1/n), conditional on the
transcript. It therefore vanishes in empirical mean square. These
facts identify (7)'s joint population law with (4). This derivation
retains the dependence caused by querying the same matrix in both
directions.

## Moment divergence

Every (h_\varepsilon) has the law of \(\tanh G\). In particular,

\[
 \|h_\varepsilon\|_\infty=1,\qquad
 \|h_\varepsilon\|_p=(\mathbb E|\tanh G|^p)^{1/p}\in(0,1),
 \tag{8}
\]

independently of \(\varepsilon\). Conditional Jensen applied to
(4) gives

\[
 \mathbb E|T_\varepsilon|^p
 \ge \frac{c^p}{v_\varepsilon^{p/2}}
       \mathbb E\psi(Y/\varepsilon)^p.
 \tag{9}
\]

Write \(\gamma(t)=(2\pi)^{-1/2}e^{-t^2/2}\) for the standard
Gaussian density. The support and plateau of \(\psi\) imply,
for \(0<\varepsilon\le1\),

\[
 v_\varepsilon\le\mathbb P(|Y|\le\varepsilon)
                    \le2\gamma(0)\varepsilon,
\]
\[
 \mathbb E\psi(Y/\varepsilon)^p
 \ge\mathbb P(|Y|\le\varepsilon/2)
 \ge\gamma(1)\varepsilon.
\]

Therefore

\[
 \|Wh_\varepsilon\|_p
 \ge
 \frac{c\,\gamma(1)^{1/p}}{\sqrt{2\gamma(0)}}
 \varepsilon^{1/p-1/2}\longrightarrow\infty
 \qquad(p>2).
 \tag{10}
\]

Equations (8)--(10) prove both claimed failures. Interchanging (W)
and (W^*), starting from the available layer-3 constant, proves
the identical result for the reverse action.

There is no conflict with the (L^2) action bound: (4) gives exactly
\(\mathbb E T_\varepsilon^2=\sigma^2+c^2\), independent of
\(\varepsilon\). All arguments take the width limit for each fixed
\(\varepsilon\) first. The higher-moment lower bound is then computed
from the identified population law; it does not assume convergence
of finite-width (p)-th moments from (W_2) convergence.

## Consequence for the global-tail route

A bounded-operator argument on the entire generated commutative

(L^p) spaces cannot supply the proposed universal higher-moment
bound. The obstruction uses only canonical Gaussian matrix reuse,
three queries, and bounded smooth inputs. A global continuation
argument would need additional properties of the actual reachable
inputs, such as controlled coordinate sensitivities or response
structure. Whether those properties hold for the trained trajectory
remains open in this note.

# A sharp boundary for a general nonlinear feature-learning certificate

Date: 2026-10-10. Author-derived result, awaiting an independent check.

## Headline

The assumptions common to the paper's three compression theorems do **not**
imply nonvanishing hidden-feature motion or separation from the frozen initial
tangent-kernel flow. This remains false if every hidden activation is analytic
and nonaffine. Consequently neither the requested all-layer property nor the
weaker last-layer property can be added as a corollary over the paper's current
scope.

The obstruction is not merely the inclusion of affine activations. For an
antipodal training pair with equal labels, odd hidden activations followed by
a shifted odd activation have a positive top feature-Gram gap, while symmetry
makes the width-limit optimizer learn only the constant readout component.
Finite-width symmetry breaking is of sampling order and produces vanishing
hidden motion over the complete training trajectory.

A separate exact identity identifies the missing condition. At zero readout,
the label-direction cubic departure from frozen-NTK training is

\[
 y^\top\{f_n(t)-f_{\rm NTK}(t)\}
 =\frac m3\,\|\ddot\theta_{\rm hid}(0)\|_2^2t^3+o(t^3),       \tag{1}
\]

where
\(\theta_{\rm hid}=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)})\)
uses the paper's mobility coordinates and both prediction vectors are evaluated
on the training inputs. Thus a positive hidden-acceleration limit would certify
the first nonlazy term. The present Gram-gap assumption does not force that
coefficient to be positive.

## 1. Counterexample inside the compression scope

Fix any hidden depth \(L\ge2\). Take \(m=2,d=1\),

\[
 x_+=1,\qquad x_-=-1,\qquad y_+=y_-=\varepsilon>0.          \tag{2}
\]

Use

\[
 \phi_1=\cdots=\phi_{L-1}=\tanh,
 \qquad \phi_L(z)=1+\tanh z.                               \tag{3}
\]

Every activation is analytic and nonaffine. On a strip narrower than the
nearest pole of \(\tanh\), their values and derivatives meet the paper's
activation assumptions. Bounded real activation values are allowed because
the paper permits, rather than requires, unbounded values.

### Positive top feature-Gram gap

At every layer before the last, antipodality and oddness give
\(h_-^{(\ell)}=-h_+^{(\ell)}\). Hence its population feature Gram has the
form

\[
 q_\ell
 \begin{pmatrix}1&-1\\-1&1\end{pmatrix},
 \qquad q_\ell>0.
\]

At the last layer write \(U=\tanh Z\), where \(Z\) is the nondegenerate
centered Gaussian preactivation for \(x_+\). The two feature coordinates of
one population neuron are \(1+U\) and \(1-U\). Therefore

\[
 Q^{(L)}=
 \begin{pmatrix}
 1+\mathbb E U^2&1-\mathbb E U^2\\
 1-\mathbb E U^2&1+\mathbb E U^2
 \end{pmatrix}.                                            \tag{4}
\]

Its eigenvalues are \(2\) and \(2\mathbb E U^2\), both positive. Thus the
paper's top feature-Gram condition holds with
\(\gamma=2\min\{1,\mathbb E U^2\}>0\). Choose the fixed label
\(\varepsilon\) small enough to satisfy the paper's label cap. All remaining
data, initialization, depth and mobility assumptions are unchanged.

### Exact finite-width symmetry identities

The following relations hold for every realization and at every time, not only
at initialization. Put

\[
 u(t)=\tanh z_+^{(L)}(t),\qquad
 a(t)=\frac{w(t)^\top\mathbf1}{n},\qquad
 b(t)=\frac{w(t)^\top u(t)}n.                              \tag{5}
\]

Oddness gives opposite features through layer \(L-1\), opposite last
preactivations, and

\[
 h_+^{(L)}=\mathbf1+u,qquad h_-^{(L)}=\mathbf1-u.
\]

All activation derivatives are even, so the two residual-free backward
responses are identical at every layer. The two predictions and residuals are

\[
 f_+=a+b,\qquad f_-=a-b,qquad
 r_+=(a-\varepsilon)+b,qquad r_-=(a-\varepsilon)-b.        \tag{6}
\]

Substitution into the paper's exact gradient-flow equations gives

\[
 \dot w=-2(a-\varepsilon)\mathbf1-2bu,                     \tag{7}
\]

and every hidden-layer velocity is proportional to \(b\). Explicitly,

\[
 \dot W^{(1)}=-2b\,\delta_+^{(1)}v_+^\top
               =-2b\,\delta_+^{(1)},
 \qquad
 \dot W^{(\ell)}=-\frac{2b}{n}\,
       \delta_+^{(\ell)}h_+^{(\ell-1)\top}
       \quad(2\le\ell\le L).                              \tag{8}
\]

Thus the population-symmetric state \(b=0\) has no hidden motion. Its readout
obeys \(\dot a=-2(a-\varepsilon)\) and fits the equal labels.

### Finite-width motion vanishes over the complete trajectory

We now verify that initialization sampling noise does not restore order-one
feature learning. Let

\[
 \bar u(t)=\frac{\mathbf1^\top u(t)}n,
 \qquad
 P(t)=\int_0^t\left{
 \frac{\|\dot W^{(1)}(s)\|_F}{\sqrt n}
 +\sum_{\ell=2}^L\|\dot W^{(\ell)}(s)\|_F\right}\,ds.     \tag{9}
\]

On the paper's real fitting event, all operator, feature, backward-response and
readout RMS bounds are fixed independently of width for all training times.
Equations (8), forward Lipschitz recursion, and \(|\tanh'|\le1\)
consequently give, for a constant depending only on the fixed problem,

\[
 \dot P\le C|b|,qquad
 |\bar u(t)-\bar u(0)|
 +\max_{a\in\{+,-\},\ell}
 \frac{\|h_a^{(\ell)}(t)-h_a^{(\ell)}(0)\|_2}{\sqrt n}
 \le CP(t).                                                \tag{10}
\]

Put locally

\[
 c=a-\varepsilon,\qquad s=\frac{\|u\|_2^2}{n}.
\]

There is an especially useful exact form of the output dynamics. In Euclidean
mobility coordinates, the hidden prediction-Jacobian row at the negative input
is the negative of its row at the positive input. If \(\kappa(t)\ge0\) is the
squared norm of the latter row, the tangent Gram therefore gives

\[
 \dot c=-2(c+\bar u b),\qquad
 \dot b=-2\{\bar u c+(s+\kappa)b\}.                        \tag{11}
\]

This also verifies directly that the term \(w^\top\dot u/n\) obtained by
differentiating (5) is nonpositive damping in the odd output direction.

Let \(B(t)=\int_0^t|b(r)|\,dr\). The forward bounds used in (10) also give
\(|s(t)-s(0)|\le CP(t)\). At initialization, conditional independence and the
law of large numbers give, with probability tending to one,

\[
 s(0)\ge s_*>0,\qquad
 \bar u(0)=O_{\mathbb P}(n^{-1/2}),                       \tag{12}
\]

where \(s_*\) is fixed. On a bootstrap interval on which
\(s\ge s_*/2\), variation of constants in (11) yields

\[
 B(t)\le \frac2{s_*}\int_0^t|\bar u(r)c(r)|\,dr,
 \qquad
 \int_0^t|c(r)|\,dr
 \le\frac\varepsilon2+
      \sup_{r\le t}|\bar u(r)|B(t).                       \tag{13}
\]

Moreover (10) gives
\(\sup_{r\le t}|\bar u(r)|\le|\bar u(0)|+CB(t)\).
Start the bootstrap with this supremum small, so the term quadratic in it on
the right side of (13) is absorbed. Then choose the fixed label
\(\varepsilon\) smaller if necessary; this remains inside the paper's label
allowance and absorbs the resulting term proportional to
\(\varepsilon B(t)\). Thus

\[
 \sup_{t\ge0}B(t)+\sup_{t\ge0}P(t)
 \le C\varepsilon|\bar u(0)|.                            \tag{14}
\]

For large width the right side is small enough to close the bootstrap for
\(s\), so (14) is valid over all time. For completeness, conditionally on the
layer-\((L-1)\) initialized features, the last preactivation coordinates are
independent centered Gaussians. Oddness and boundedness of \(\tanh\) give
\(\mathbb E[\bar u(0)\mid h_+^{(L-1)}(0)]=0\) and conditional variance at
most \(1/n\), which proves the second part of (12).

Combining (10), (12), and (14), and using that the fitting event has
probability tending to one, proves

\[
 \max_{a\in\{+,-\},\,1\le\ell\le L}
 \sup_{t\ge0}
 \frac{\|h_a^{(\ell)}(t)-h_a^{(\ell)}(0)\|_2}{\sqrt n}
 \xrightarrow{\mathbb P}0.                                \tag{15}
\]

The same conclusion holds for the complete hidden parameter path length in
(9). This rules out an order-one feature-learning lower bound in every hidden
layer.

### The frozen initial kernel gives the same limiting trajectory

At zero readout the initial tangent kernel contains only the readout block.
Its flow is exactly readout training with \(u\) frozen at \(u(0)\). If its two
output coordinates are written \(\widehat a\pm\widehat b\), then

\[
 \dot{\widehat a}=-2(\widehat a-\varepsilon)
                   -2\widehat b\,\bar u(0),
 \qquad
 \dot{\widehat b}=-2(\widehat a-\varepsilon)\bar u(0)
                   -2\widehat b\frac{\|u(0)\|_2^2}{n}.     \tag{16}
\]

Both start at zero. The variation-of-constants argument above applies to (16)
with \(u\) frozen. It shows that the actual flow and (16) both converge
uniformly over the entire nonnegative time axis to

\[
 a_*(t)=\varepsilon(1-e^{-2t}),\qquad b_*(t)=0.
\]

Therefore, on the entire input sphere in dimension one,

\[
 \sup_{t\ge0}\max_{a\in\{+,-\}}
 |f_n(t,x_a)-f_{{\rm NTK},n}(t,x_a)|
 \xrightarrow{\mathbb P}0.                                \tag{17}
\]

Equations (15) and (17) disprove both requested universal conclusions in a
single admissible, genuinely nonaffine example.

## 2. Exact onset identity for a corrected theorem

Although positivity is not automatic, the first nonlazy coefficient has a
simple exact form. This section works at an arbitrary fixed width and with the
paper's general data and activations.

Let \(f_n(t)\in\mathbb R^m\) be the vector of training predictions. In the
Euclidean mobility coordinates write

\[
 \theta_{\rm hid}
 =(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)}),
 \qquad u=w/\sqrt n.                                      \tag{18}
\]

Let \(J_{\rm hid}\) and \(J_u\) be the corresponding prediction Jacobian
blocks, and put \(K=J_{\rm hid}J_{\rm hid}^\top+J_uJ_u^\top\). The flow is

\[
 \dot f_n=-\frac2mK(f_n-y).                                \tag{19}
\]

At zero readout, \(J_{\rm hid}(0)=0\),
\(\dot\theta_{\rm hid}(0)=0\), and \(\dot J_u(0)=0\). Define only within this
proof \(A=\dot J_{\rm hid}(0)\). Differentiating the hidden flow gives

\[
 \ddot\theta_{\rm hid}(0)=\frac2mA^\top y.                \tag{20}
\]

Because the prediction is linear in the readout, write it locally as
\(f_n=J_u(\theta_{\rm hid})u\). For every hidden direction \(v\), equality of
mixed derivatives gives

\[
 Av=\frac2m\,D J_u(0)[v]J_u(0)^\top y.                    \tag{21}
\]

The hidden part of \(y^\top\ddot K(0)y\) is
\(2\|A^\top y\|_2^2\). The readout part is

\[
 2\left\langle J_u(0)^\top y,
 D J_u(0)[\ddot\theta_{\rm hid}(0)]^\top y\right\rangle
 =2\|A^\top y\|_2^2,                                     \tag{22}
\]

where (20)--(21) were substituted in the last equality. Consequently

\[
 y^\top\ddot K(0)y
 =4\|A^\top y\|_2^2
 =m^2\|\ddot\theta_{\rm hid}(0)\|_2^2.                   \tag{23}
\]

Let \(f_{\rm NTK}\) solve (19) with \(K(t)\) replaced by \(K(0)\), from the
same zero prediction. Since \(\dot K(0)=0\), the two output vectors have the
same first two derivatives. Differentiating (19) twice gives

\[
 \frac{d^3}{dt^3}\{f_n-f_{\rm NTK}\}(0)
 =\frac2m\ddot K(0)y.                                     \tag{24}
\]

Take the inner product with \(y\), use (23), and apply Taylor's formula. This
proves (1). No probabilistic limit, activation approximation, or compression
argument enters this identity.

The individual initialization accelerations are also explicit. First

\[
 \dot w(0)=\frac2m\sum_a y_a h_a^{(L)}(0).                \tag{25}
\]

Starting at the top and moving backward, define the actual time derivatives
of the residual-free responses at zero by

\[
 \begin{aligned}
 \dot\delta_a^{(L)}(0)
 &=\dot w(0)\odot\phi_L'(z_a^{(L)}(0)),\\
 \dot\delta_a^{(\ell)}(0)
 &=\phi_\ell'(z_a^{(\ell)}(0))\odot
   W^{(\ell+1)}(0)^\top\dot\delta_a^{(\ell+1)}(0).
 \end{aligned}                                            \tag{26}
\]

Then

\[
 \begin{aligned}
 \ddot W^{(1)}(0)
 &=\frac2m\sum_a y_a\dot\delta_a^{(1)}(0)v_a^\top,\\
 \ddot W^{(\ell)}(0)
 &=\frac2{mn}\sum_a y_a\dot\delta_a^{(\ell)}(0)
                  h_a^{(\ell-1)}(0)^\top,
       \qquad 2\le\ell\le L.                             
 \end{aligned}                                            \tag{27}
\]

Feature accelerations follow from

\[
 \begin{aligned}
 \ddot z_a^{(1)}(0)&=\ddot W^{(1)}(0)v_a,\\
 \ddot z_a^{(\ell)}(0)
 &=\ddot W^{(\ell)}(0)h_a^{(\ell-1)}(0)
   +W^{(\ell)}(0)\ddot h_a^{(\ell-1)}(0),\\
 \ddot h_a^{(\ell)}(0)
 &=\phi_\ell'(z_a^{(\ell)}(0))\odot\ddot z_a^{(\ell)}(0).
 \end{aligned}                                            \tag{28}
\]

Thus a valid positive theorem needs lower bounds on the quantities in (28),
or at least on the total hidden acceleration in (23), together with a
width-uniform real-time Taylor remainder. The current top feature-Gram gap
controls the initial readout direction, but the counterexample proves that it
does not control these hidden-response contractions.

## Consequence for the paper

The existing wording is mathematically accurate: the model retains
feature-learning mobilities and exact nonlinear gates, but the theorem does not
assert nonzero feature motion for every activation and dataset. Calling the
compression theorem itself a certificate of nonlinear feature learning would
be false. A later positive proposition must either restrict data/labels enough
to eliminate the symmetry above, or assume and verify explicit positive
initial hidden-response coefficients. Neither change preserves the exact
current scope.

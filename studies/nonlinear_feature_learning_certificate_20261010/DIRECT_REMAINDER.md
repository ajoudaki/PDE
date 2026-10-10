# Direct finite-width short-time remainder argument

Candidate proof, conditional only on the stated finite initialization program
and real energy bootstrap. This document does not prove those two inputs or
invoke a population evolution theorem. All limits below are along individual
widths, with the training data, depth, input dimension, and activations fixed.

## Setup and the precise inputs

For training inputs \(v_a=x_a/\sqrt d\in\mathbb R^d\), \(1\le a\le m\), use

\[
z_a^{(1)}=W^{(1)}v_a,\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),\qquad
f_a=\frac{w^\top h_a^{(L)}}n.
\]

The loss is \(\mathcal L=\|f-y\|_2^2/m\), \(r=f-y\), and the mobilities of
\(W^{(1)},W^{(2)},\ldots,W^{(L)},w\) are \(n,1,\ldots,1,n\). Thus

\[
\begin{aligned}
\dot w&=-\frac2m\sum_a r_a h_a^{(L)},\\
\dot W^{(1)}&=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\\
\dot W^{(\ell)}&=-\frac2{mn}\sum_a
r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},\qquad 2\le\ell\le L,
\end{aligned}
\]

where

\[
\delta_a^{(L)}=w\odot\phi_L'(z_a^{(L)}),\qquad
\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot
W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]

Write a subscript (0) for initialization and assume \(w_0=0\). The proof
uses only bounded real first and second derivatives of each activation;
analyticity and Gaussian initialization enter the supplied initialization
and bootstrap inputs, not the remainder estimates themselves. Activation
values need not be bounded.

For width-\(n\) vectors put

\[
\langle u,v\rangle_n=\frac{u^\top v}{n},\qquad
\|u\|_n^2=\langle u,u\rangle_n.
\]

For a tuple \(U=(U^{(1)},\ldots,U^{(L)})\) of hidden-weight directions, use
the inverse-mobility norm

\[
\|U\|_{\mathrm{mob}}^2
=\frac{\|U^{(1)}\|_F^2}{n}
+\sum_{\ell=2}^L\|U^{(\ell)}\|_F^2.
\]

Define the finite initialization program by

\[
\begin{aligned}
S&=\sum_b y_b h_{b,0}^{(L)},
&q&=\frac2m S=\dot w(0),\\
P_a^{(L)}&=S,
&B_a^{(L)}&=\phi_L'(z_{a,0}^{(L)})\odot P_a^{(L)},\\
P_a^{(\ell)}&=W_0^{(\ell+1)\top}B_a^{(\ell+1)},
&B_a^{(\ell)}&=\phi_\ell'(z_{a,0}^{(\ell)})\odot P_a^{(\ell)}.
\end{aligned}
\]

Here \(P_a^{(\ell)}\) is the backward vector **before** multiplication by
the layer-\(\ell\) activation derivative. Set

\[
\begin{aligned}
V^{(1)}&=\frac4{m^2}\sum_a y_aB_a^{(1)}v_a^\top,\\
V^{(\ell)}&=\frac4{m^2n}\sum_a
y_a B_a^{(\ell)}h_{a,0}^{(\ell-1)\top},\qquad\ell\ge2.
\end{aligned}
\]

These are the exact initial hidden accelerations. The corresponding
preactivation and feature accelerations are given by the forward recursion

\[
\begin{aligned}
Z_a^{(1)}&=V^{(1)}v_a,
&A_a^{(1)}&=\phi_1'(z_{a,0}^{(1)})\odot Z_a^{(1)},\\
Z_a^{(\ell)}&=V^{(\ell)}h_{a,0}^{(\ell-1)}
+W_0^{(\ell)}A_a^{(\ell-1)},
&A_a^{(\ell)}&=\phi_\ell'(z_{a,0}^{(\ell)})\odot Z_a^{(\ell)}.
\end{aligned}
\]

The two required inputs are as follows.

1. **Fixed bootstrap event.** There are deterministic \(C<\infty\) and
   \(T_0>0\), independent of width, such that an event of probability tending
   to one supports the real flow on \([0,T_0]\) and, for all \(0\le t\le T_0\),

   \[
   \begin{gathered}
   \max_{\ell\ge2}\|W_0^{(\ell)}\|_{\mathrm{op}}
   +\max_{a,\ell}\|h_{a,0}^{(\ell)}\|_n\le C,
   \qquad \|w(t)\|_n\le Ct,\\
   \frac{\|W^{(1)}(t)-W_0^{(1)}\|_{\mathrm{op}}}{\sqrt n}
   +\max_{\ell\ge2}\|W^{(\ell)}(t)-W_0^{(\ell)}\|_{\mathrm{op}}
   \le Ct^2,\\
   \max_{a,\ell}\bigl(
   \|z_a^{(\ell)}(t)-z_{a,0}^{(\ell)}\|_n
   +\|h_a^{(\ell)}(t)-h_{a,0}^{(\ell)}\|_n\bigr)\le Ct^2.
   \end{gathered}
   \]

   Constants can be enlarged a finite number of times. In particular,
   \(\max_{a,\ell}\|h_a^{(\ell)}(t)\|_n\le C\),
   \(\|f(t)\|_2\le Ct\), and \(\|r(t)\|_2\le C\) then hold on the same
   type of event. The output estimate follows directly from
   \(|f_a|\le\|w\|_n\|h_a^{(L)}\|_n\).

2. **Finite initialization limit with second moments.** The empirical joint
   laws of the finite initialization vectors above converge in probability
   to deterministic laws, with convergent second moments. In particular,
   every vector in the families \(h_{a,0}^{(\ell)}\), \(P_a^{(\ell)}\), and
   \(Z_a^{(\ell)}\) has bounded normalized second moment with probability
   tending to one, and satisfies the following precise tail condition:
   for every \(\eta>0\), some finite \(R\) has

   \[
   \mathbb P\left\{
   \max_u\frac1n\sum_i |u_i|^2\mathbf1_{\{|u_i|>R\}}>\eta
   \right\}\longrightarrow0.
   \tag{1}
   \]

   The maximum ranges over the stated finite families. Convergence to a
   deterministic finite-second-moment law with second moments gives (1)
   by choosing a sufficiently large continuity radius of the limiting
   tail integral. Fixed finite linear combinations, including \(S,q\),
   also have (1). Assume additionally

   \[
   E_n:=\|V\|_{\mathrm{mob}}^2\longrightarrow E>0
   \quad\text{in probability}.
   \tag{2}
   \]

The pre-gated vectors \(P_a^{(\ell)}\) and preactivation accelerations
\(Z_a^{(\ell)}\) must really be included in input 2. A normalized operator
bound and a second-moment bound alone do not give their tail condition.

## A uniform remainder convention and multiplier estimate

Write \(R_n=o_*(t^k)\) in a specified norm if

\[
\forall\varepsilon>0\ \exists T_\varepsilon\in(0,T_0]
\quad
\mathbb P\left\{
\sup_{0<t\le T_\varepsilon}
\frac{\|R_n(t)\|}{t^k}>\varepsilon
\right\}\longrightarrow0.
\tag{3}
\]

The time \(T_\varepsilon\) is deterministic and does not depend on width or
confidence. The strong quantifier in (3), rather than only a double-limit
in-probability statement, follows from the deterministic limits in input 2
and the fixed bootstrap constant in input 1. Finitely many such remainders
can be controlled on one interval by taking the minimum of their times.

Here is the only nonlinear estimate needed. Suppose a fixed initialization
vector \(u_n\) satisfies (1), \(g\) is bounded by \(M\) and Lipschitz with
constant \(D\), and
\(\sup_{t\le T}\|x_n(t)-x_n(0)\|_n\le CT^2\). Then

\[
\begin{aligned}
\sup_{t\le T}
\|[g(x_n(t))-g(x_n(0))]\odot u_n\|_n^2
&\le D^2R^2 C^2T^4\\
&\quad+4M^2\frac1n\sum_i |u_{n,i}|^2
\mathbf1_{\{|u_{n,i}|>R\}}.
\end{aligned}
\tag{4}
\]

On \(|u_{n,i}|\le R\), use the Lipschitz bound; on its complement, use
the bound \(2M\) for the multiplier difference. Given an error tolerance,
first choose \(R\) by (1), then choose \(T\) for the first term. Therefore
the product in (4) is \(o_*(1)\), uniformly in time. The same argument
holds uniformly with \(x_n(t)-x_n(0)\) replaced by
\(\theta[x_n(t)-x_n(0)]\), \(0\le\theta\le1\).

No coordinate maximum and no fourth moment appears in (4).

## Backward responses and weight increments

The readout equation gives

\[
\dot w(t)-q
=\frac2m\sum_a\bigl[y_a(h_a^{(L)}(t)-h_{a,0}^{(L)})
-f_a(t)h_a^{(L)}(t)\bigr].
\]

The bootstrap bounds its RMS norm by \(Ct\), so integration gives

\[
\left\|\frac{w(t)}t-q\right\|_n\le Ct.
\tag{5}
\]

At the top layer,

\[
\frac{\delta_a^{(L)}(t)}t-\frac2mB_a^{(L)}
=\phi_L'(z_a^{(L)}(t))\odot\left(\frac{w(t)}t-q\right)
+[\phi_L'(z_a^{(L)}(t))-\phi_L'(z_{a,0}^{(L)})]\odot q.
\]

The first term tends to zero by (5), and the second by (4). For a lower
layer put \(D_a^{(\ell)}(t)=\operatorname{diag}(\phi_\ell'(z_a^{(\ell)}(t)))\).
An exact subtraction gives

\[
\begin{aligned}
\frac{\delta_a^{(\ell)}(t)}t-\frac2mB_a^{(\ell)}
={}&D_a^{(\ell)}(t)W^{(\ell+1)}(t)^\top
\left(\frac{\delta_a^{(\ell+1)}(t)}t-\frac2mB_a^{(\ell+1)}\right)\\
&+\frac2mD_a^{(\ell)}(t)
[W^{(\ell+1)}(t)-W_0^{(\ell+1)}]^\top B_a^{(\ell+1)}\\
&+\frac2m[D_a^{(\ell)}(t)-D_a^{(\ell)}(0)]P_a^{(\ell)}.
\end{aligned}
\tag{6}
\]

The first term is bounded by a fixed operator constant times the next
layer's error. The second is \(O(t^2)\) in RMS. The third is \(o_*(1)\)
by (4) with \(u=P_a^{(\ell)}\). Downward induction proves

\[
\max_{a,\ell}
\left\|\delta_a^{(\ell)}(t)-\frac{2t}{m}B_a^{(\ell)}\right\|_n
=o_*(t).
\tag{7}
\]

Inserting (7) into the weight equations, using \(r_a=-y_a+O(t)\) and
\(h_a^{(\ell)}(t)=h_{a,0}^{(\ell)}+O_{\|\cdot\|_n}(t^2)\), yields

\[
\|\dot W(t)-tV\|_{\mathrm{mob}}=o_*(t).
\tag{8}
\]

To check the normalization explicitly, the needed rank-one identities are

\[
\frac{\|uv^\top\|_F}{\sqrt n}=\|u\|_n\|v\|_2
\quad(v\in\mathbb R^d),\qquad
\frac{\|u h^\top\|_F}{n}=\|u\|_n\|h\|_n
\quad(h\in\mathbb R^n).
\]

Every product in the difference of the weight equations therefore has
one small factor and remaining factors bounded on an event of probability
tending to one. Integrating (8) gives

\[
\left\|W(t)-W_0-\frac{t^2}{2}V\right\|_{\mathrm{mob}}
=o_*(t^2).
\tag{9}
\]

Indeed an upper bound \(\varepsilon s\) on the integrand gives an upper
bound \(\varepsilon t^2/2\) on its integral, uniformly for \(t\le T\).

## Forward increments without an \(L^2\) Fréchet derivative

The first-layer preactivation expansion follows directly from (9):

\[
z_a^{(1)}(t)-z_{a,0}^{(1)}
=\frac{t^2}{2}Z_a^{(1)}+o_{*,\|\cdot\|_n}(t^2).
\]

For any layer, suppose this preactivation expansion holds and write
\(\Delta z=z_a^{(\ell)}(t)-z_{a,0}^{(\ell)}\). The coordinatewise identity

\[
\phi_\ell(z_0+\Delta z)-\phi_\ell(z_0)
=\int_0^1\phi_\ell'(z_0+\theta\Delta z)\odot\Delta z\,d\theta
\]

shows that the feature remainder equals

\[
\begin{aligned}
&\int_0^1\phi_\ell'(z_0+\theta\Delta z)\odot
\left(\Delta z-\frac{t^2}{2}Z_a^{(\ell)}\right)d\theta\\
&\qquad+\frac{t^2}{2}\int_0^1
[\phi_\ell'(z_0+\theta\Delta z)-\phi_\ell'(z_0)]
\odot Z_a^{(\ell)}\,d\theta.
\end{aligned}
\tag{10}
\]

The first integral is \(o_*(t^2)\), since the derivative is bounded.
The second is \(o_*(t^2)\) by (4), uniformly in \(\theta\), using the
initial tail condition for \(Z_a^{(\ell)}\). Hence

\[
h_a^{(\ell)}(t)-h_{a,0}^{(\ell)}
=\frac{t^2}{2}A_a^{(\ell)}+o_{*,\|\cdot\|_n}(t^2).
\tag{11}
\]

At a subsequent layer the exact forward subtraction is

\[
\Delta z_a^{(\ell)}
=\Delta W^{(\ell)}h_{a,0}^{(\ell-1)}
+W_0^{(\ell)}\Delta h_a^{(\ell-1)}
+\Delta W^{(\ell)}\Delta h_a^{(\ell-1)}.
\]

The first two terms have coefficient \(Z_a^{(\ell)}/2\), by (9) and
(11). The last is \(O(t^4)\) in RMS, since the weight increment is
\(O(t^2)\) in operator norm and the feature increment is \(O(t^2)\)
in RMS. An \(o_*(t^2)\) Frobenius weight remainder acts on an initial
feature vector with RMS remainder bounded by
\(\|R\|_F\|h_0\|_n\). This closes induction and proves both

\[
\max_{a,\ell}\left\|z_a^{(\ell)}(t)-z_{a,0}^{(\ell)}
-\frac{t^2}{2}Z_a^{(\ell)}\right\|_n=o_*(t^2),
\qquad\text{and (11).}
\tag{12}
\]

The proof does not assume that composition by a nonaffine activation is
Fréchet differentiable as a map from \(L^2\) to \(L^2\). That generally
false assertion is replaced by (10) and the tail control of the actual
initial direction \(Z_a^{(\ell)}\).

## Tangent kernel and its exact positive coefficient

The mobility-weighted tangent kernel is

\[
\begin{aligned}
K_{ab}(t)={}&\langle h_a^{(L)}(t),h_b^{(L)}(t)\rangle_n\\
&+(v_a^\top v_b)\langle\delta_a^{(1)}(t),\delta_b^{(1)}(t)\rangle_n\\
&+\sum_{\ell=2}^L
\langle\delta_a^{(\ell)}(t),\delta_b^{(\ell)}(t)\rangle_n
\langle h_a^{(\ell-1)}(t),h_b^{(\ell-1)}(t)\rangle_n.
\end{aligned}
\tag{13}
\]

It satisfies \(\dot f=-(2/m)K(f-y)\), and its initial value is the
readout Gram \(K_{0,ab}=\langle h_{a,0}^{(L)},h_{b,0}^{(L)}\rangle_n\).
Equations (7) and (11), together with bounded initial RMS norms, give

\[
K_n(t)=K_{0,n}+t^2K_{2,n}+o_*(t^2)
\tag{14}
\]

in any matrix norm on the fixed \(m\times m\) space, where

\[
\begin{aligned}
(K_{2,n})_{ab}={}&\frac12\bigl(
\langle A_a^{(L)},h_{b,0}^{(L)}\rangle_n
+\langle h_{a,0}^{(L)},A_b^{(L)}\rangle_n\bigr)\\
&+\frac4{m^2}(v_a^\top v_b)\langle B_a^{(1)},B_b^{(1)}\rangle_n\\
&+\frac4{m^2}\sum_{\ell=2}^L
\langle B_a^{(\ell)},B_b^{(\ell)}\rangle_n
\langle h_{a,0}^{(\ell-1)},h_{b,0}^{(\ell-1)}\rangle_n.
\end{aligned}
\tag{15}
\]

The coefficient matrices \(K_{0,n},K_{2,n}\) are bounded on an event of
probability tending to one. Their entrywise convergence is available from
the supplied joint second-moment initialization limits but is not needed
for the following coefficient identity.

For every hidden-weight direction \(U\), the forward chain rule and
backward recursion give the exact finite-width identity

\[
\begin{aligned}
\frac1n\sum_a y_aS^\top D_Wh_{a,0}^{(L)}[U]
&=\frac{m^2}{4}\left[
\frac{\langle V^{(1)},U^{(1)}\rangle_F}{n}
+\sum_{\ell=2}^L\langle V^{(\ell)},U^{(\ell)}\rangle_F
\right].
\end{aligned}
\tag{16}
\]

For example, the layer-\(\ell\ge2\) term on the left before substituting
\(V\) is ((1/n)\sum_a y_a\langle
B_a^{\(\ell\)}h_{a,0}^{\(\ell-1\)\top},U^{\(\ell\)}\rangle_F);
the first-layer expression replaces the previous feature by \(v_a\).
This verifies every normalization in (16). Taking \(U=V\) gives

\[
\left\langle S,\sum_a y_a A_a^{(L)}\right\rangle_n
=\frac{m^2}{4}E_n.
\tag{17}
\]

The label contraction of the first line of (15) is the left side of
(17). The label contraction of the remaining lines equals
\(m^2E_n/4\) by expanding the squares in the definition of \(V\). Thus

\[
y^\top K_{2,n}y=\frac{m^2}{2}E_n.
\tag{18}
\]

The feature-motion and hidden-gradient contributions each equal
\(m^2E_n/4\); no sign assumption on individual labels is used.

## Cubic separation from the frozen initial NTK

Let \(f_{\mathrm{NTK},n}\) solve

\[
\dot f_{\mathrm{NTK},n}
=\frac2mK_{0,n}(y-f_{\mathrm{NTK},n}),\qquad
f_{\mathrm{NTK},n}(0)=0.
\]

Writing \(e_n=f_n-f_{\mathrm{NTK},n}\), variation of constants gives
the exact formula

\[
e_n(t)=\frac2m\int_0^t
e^{-(2/m)K_{0,n}(t-s)}
[K_n(s)-K_{0,n}][y-f_n(s)]\,ds.
\tag{19}
\]

Here \(K_{0,n}\) is positive semidefinite, so the exponential has norm at
most one; moreover its difference from the identity is \(O(t-s)\) on
the fixed operator event. Use (14), \(\|f_n(s)\|_2\le Cs\), and the
boundedness of \(K_{2,n}\) to obtain

\[
e_n(t)=\frac{2t^3}{3m}K_{2,n}y+o_*(t^3).
\tag{20}
\]

More explicitly, if the kernel remainder is bounded by
\(\varepsilon s^2\) for \(s\le T\), its contribution to (19) is at most
\(C\varepsilon t^3\). The factors \(f_n(s)\) and the difference between
the exponential and the identity each contribute at most \(Ct^4\).
Choosing first the kernel tolerance and then \(T\) proves (20) with
exactly the quantifier (3). Combining (18) and (20) yields

\[
y^\top\bigl(f_n(t)-f_{\mathrm{NTK},n}(t)\bigr)
=\frac m3 E_n t^3+o_*(t^3).
\tag{21}
\]

Consequently a deterministic \(T_*>0\) can be chosen so that

\[
\mathbb P\left\{
\forall t\in(0,T_*]:\quad
y^\top(f_n(t)-f_{\mathrm{NTK},n}(t))
\ge\frac{mE}{6}t^3
\right\}\longrightarrow1.
\tag{22}
\]

For instance, combine \(E_n\ge3E/4\), whose probability tends to one,
with a scalar remainder at most \(mEt^3/12\). In particular every fixed
\(t\in(0,T_*]\) has a strictly positive, width-independent label-projected
gap with probability tending to one. The vector gap is at least
\(mEt^3/(6\|y\|_2)\) on the same event.

## Hidden-feature activity and useful variants

If the layer energies

\[
E_{1,n}=\|V^{(1)}\|_F^2/n,\qquad
E_{\ell,n}=\|V^{(\ell)}\|_F^2\quad(\ell\ge2)
\]

converge to positive constants, (9) gives width-independent lower bounds
of order \(t^4\) for the squared inverse-mobility weight increments at
every layer, simultaneously on a sufficiently small deterministic interval.

Feature activity is not inferred merely from a nonzero weight increment.
For \(j\le L\), apply (16) to \(U^{(\ell)}=V^{(\ell)}\) for
\(\ell\le j\), and \(U^{(\ell)}=0\) above \(j\). Backpropagating from
the top only to layer \(j\) gives

\[
\sum_a y_a\langle P_a^{(j)},A_a^{(j)}\rangle_n
=\frac{m^2}{4}\sum_{\ell\le j}E_{\ell,n}.
\tag{23}
\]

Cauchy--Schwarz therefore implies

\[
\left(\sum_a\|A_a^{(j)}\|_n^2\right)
\left(\sum_a y_a^2\|P_a^{(j)}\|_n^2\right)
\ge\frac{m^4}{16}
\left(\sum_{\ell\le j}E_{\ell,n}\right)^2.
\tag{24}
\]

The second factor is bounded on an event of probability tending to one.
If \(E_{1,n}\to E_1>0\), every layer's feature-acceleration norm is thus
bounded below. Using (11), there are constants \(c_j>0\) and one
deterministic \(T_*>0\) such that

\[
\mathbb P\left\{
\forall t\in(0,T_*],\ \forall j\le L:\quad
\frac1n\sum_a
\|h_a^{(j)}(t)-h_{a,0}^{(j)}\|_2^2\ge c_jt^4
\right\}\longrightarrow1.
\tag{25}
\]

If only total \(E>0\) is known, (17) still proves top-layer feature
activity. It does not by itself prove activity at all earlier layers.

All the forward and backward remainder arguments apply to any fixed
passive panel if the bootstrap and initialization inputs include that
panel. In particular, let \(c_a\) be coefficients on such a panel with
\(\sum_a c_a=0\) and \(\sum_a c_av_a=0\). They annihilate every affine
function of the input. If the initialization module proves

\[
\left\|\sum_a c_a A_a^{(j)}\right\|_n^2\longrightarrow a_*>0,
\]

then (11) gives a positive order-\(t^4\) lower bound for
\(\|\sum_a c_a[h_a^{(j)}(t)-h_{a,0}^{(j)}]\|_n^2\), with probability
tending to one on a deterministic small interval. This transfers a finite
nonaffinity witness from the initial acceleration to actual positive time.
It does not claim convergence of the entire feature trajectory at fixed time.

## Exact scope and remaining obligations

The proof establishes (7), (9), (12), (14), and (21) from the two stated
inputs, with the strong quantifier (3). It also establishes actual feature
activity through (23)--(25), once the corresponding initial energy is
positive. A full population-flow theorem is unnecessary for these claims.

The initialization module must nevertheless provide the finite law and
second-moment limits for the actual tied forward/transpose/acceleration
program. Independent Gaussian surrogates for these tied uses cannot be
substituted without proof. It must include the pre-gated backward vectors
and the preactivation acceleration vectors used in (4), (6), and (10).

If the available bootstrap constants are only bounded in probability,
or empirical limits are random with no fixed deterministic bounds, the
same estimates generally give only

\[
\lim_{T\downarrow0}\limsup_n
\mathbb P\left\{\sup_{0<t\le T}\frac{\|R_n(t)\|}{t^k}
>\varepsilon\right\}=0.
\]

That weaker quantifier permits choosing time with the requested confidence;
it does not automatically imply (22) or (25) with one fixed time and
failure probability tending to zero. The deterministic inputs stated here
are what remove that gap.

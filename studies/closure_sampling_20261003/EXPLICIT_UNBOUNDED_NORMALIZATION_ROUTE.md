# Explicit normalized unbounded fitting, and the remaining compression bridge

2026-10-04. Scoped theoretical continuation in closure_sampling_20261003.
This note gives a complete explicit all-time **dense fitting and tail**
theorem for normalized smooth Lipschitz activations, including unbounded
ones. It does not claim a complete explicit compressor theorem. The existing
unbounded compression theorem remains qualitative in its label allowance,
and requires strip analyticity beyond smooth Lipschitz regularity.

The useful improvement is that Gaussian second-moment normalization controls
the initialized feature RMS over the whole real query sphere. A fixed
operator-tube argument then keeps that RMS bounded during training, without
a global activation-value bound or a recursively growing feature bound.
Depth still enters exponentially through worst-case derivative propagation.

Complete scientific inputs read were ACTIVATION_CLASS_EXTENSION_ROUTE.md,
ACTIVATION_CLASS_EXTENSION_CHECK.md, EXPLICIT_LABEL_CONSTANTS_ROUTE.md,
EXPLICIT_SOURCE_CONSTANTS_ROUTE.md, and
RUNTIME_SMALL_ACTIVITY_CONSTANT_ROUTE.md. No prior-study source was needed,
and no additional source was followed. Required canonical-notation,
neural-network, rigorous-proof, research-contract, evidence, and adversarial
audit instructions were read. There were no experiments, Git operations,
README edits, or maintained-book changes. This is a scoped internal
derivation, not an isolated promotion review.

## 1. Precise real theorem

Fix hidden depth \(L\ge2\), input dimension \(d\ge1\), sample count \(m\),
unit inputs \(v_a\in S^{d-1}\), and labels \(y_a\). Let each activation
\(\phi_\ell:\mathbb R\to\mathbb R\) be \(C^2\) with bounded first
derivative. Define

\[
s=\max\{1,\max_{1\le\ell\le L}\|\phi_\ell'\|_\infty\},
\qquad
\mathbb E\phi_\ell(G)^2=1,
\qquad G\sim N(0,1).
\tag{1}
\]

No bound on \(\phi_\ell\) itself is assumed. The \(C^2\) hypothesis
ensures local Lipschitz continuity of the finite-dimensional gradient vector
field; smooth Lipschitz activations meet it.

Use the canonical network and physical time:

\[
\begin{aligned}
z^{(1)}(v)&=Av,&
z^{(\ell)}(v)&=W^{(\ell)}h^{(\ell-1)}(v),&
h^{(\ell)}(v)&=\phi_\ell(z^{(\ell)}(v)),\\
f_n(v)&=n^{-1}w^\top h^{(L)}(v),&
c_a&=y_a-f_n(v_a),&
\rho&=\|c\|_2/\sqrt m,\qquad Y=\|y\|_2/\sqrt m.
\end{aligned}
\tag{2}
\]

Here \(A\in\mathbb R^{n\times d}\), the hidden matrices are
\(W^{(\ell)}\in\mathbb R^{n\times n}\), \(2\le\ell\le L\), and
\(w\in\mathbb R^n\). Backpropagation and the flow are

\[
\begin{aligned}
k_a^{(L)}&=w,&
\delta_a^{(\ell)}&=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)},&
k_a^{(\ell)}&=W^{(\ell+1)\top}\delta_a^{(\ell+1)},\\
\dot A&=\frac2m\sum_a c_a\delta_a^{(1)}v_a^\top,&
\dot W^{(\ell)}&=\frac2{mn}\sum_a
c_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},&
\dot w&=\frac2m\sum_a c_ah_a^{(L)}.
\end{aligned}
\tag{3}
\]

Initialize independent \(A_{ij}\sim N(0,1)\), independent
\(W_{ij}^{(\ell)}\sim N(0,1/n)\), and \(w(0)=0\).
For \(u\in\mathbb R^n\), write \(\|u\|_n=\|u\|_2/\sqrt n\).
The initialized limiting covariances are

\[
Q^{(0)}_{ab}=v_a^\top v_b,\qquad
Q^{(\ell)}_{ab}
=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
\qquad Z\sim N(0,Q^{(\ell-1)}).
\tag{4}
\]

Assume \(\gamma=\lambda_{\min}(Q^{(L)})>0\), and put

\[
\lambda=\gamma/m.
\tag{5}
\]

Normalization (1) gives \(Q^{(\ell)}_{aa}=1\) at every layer. Thus
\(\gamma\le1\) and \(0<\lambda\le1/m\le1\); no cap or hidden
rescaling of the gap is required.

Let \(\mathsf H(t)\in\mathbb R^{n\times m}\) have columns
\(h_a^{(L)}(t)\). The exact initialized event used below is

\[
\begin{split}
\mathcal E_n=\{&\|A(0)\|_{\rm op}/\sqrt n\le8,\quad
\max_{2\le\ell\le L}\|W^{(\ell)}(0)\|_{\rm op}\le8;\\
&\max_{1\le\ell\le L}\sup_{\|v\|=1}
\|h^{(\ell)}(0,v)\|_n\le3/2;\\
&\lambda_{\min}(\mathsf H(0)^\top\mathsf H(0)/(mn))
\ge\lambda/2\}.
\end{split}
\tag{6}
\]

All quantities in (6) concern initialization. At fixed architecture,
activations, inputs, and positive gap, \(\Pr(\mathcal E_n)\to1\).
Section 2 proves this assertion; a numerical width-confidence threshold
is not claimed.

Define explicit nonnegative layer constants by

\[
\begin{gathered}
q=9s,\qquad D_\ell=sq^{L-\ell},\qquad U_1=D_1,\qquad
U_\ell=2D_\ell\quad(2\le\ell\le L),\\
F_1=sU_1,\qquad
F_\ell=s(2U_\ell+9F_{\ell-1})\quad(2\le\ell\le L),\\
F=F_L=s^2\left[q^{2L-2}+4\sum_{j=0}^{L-2}q^{2j}\right].
\end{gathered}
\tag{7}
\]

In particular \(F\ge\max(1,U_1,\ldots,U_L,F_1,\ldots,F_L)\).
There are no unspecified constants in (7).

**Theorem.** On \(\mathcal E_n\), if

\[
0<Y\le\frac{\lambda}{8\sqrt F},
\tag{8}
\]

then the solution of (3) exists for all real \(t\ge0\), converges in
parameter space, and satisfies, for every such \(t\),

\[
\begin{gathered}
\sup_{\|v\|=1}\|h^{(\ell)}(t,v)\|_n\le2,\qquad
\|A(t)\|_{\rm op}/\sqrt n<9,\qquad
\|W^{(\ell)}(t)\|_{\rm op}<9,\\
\lambda_{\min}(\mathsf H(t)^\top\mathsf H(t)/(mn))
\ge\lambda/4,\qquad
\rho(t)\le Ye^{-\lambda t/2},\qquad
\int_0^\infty\rho(t)\,dt\le\frac{2Y}{\lambda}.
\end{gathered}
\tag{9}
\]

Use the physical parameter norm

\[
\|(A,W,w)\|_{\rm par}^2
=\|A\|_F^2/n+\sum_{\ell=2}^L\|W^{(\ell)}\|_F^2+\|w\|_2^2/n.
\tag{10}
\]

Its total path length and the readout RMS obey

\[
\int_0^\infty\|\dot\theta(t)\|_{\rm par}\,dt
\le\frac{2Y}{\sqrt\lambda},\qquad
\|w(t)\|_n\le\frac{2Y}{\sqrt\lambda}.
\tag{11}
\]

The individual hidden displacements and whole-sphere feature displacements
have the sharper activity powers

\[
\begin{aligned}
\|A(t)-A(0)\|_F/\sqrt n
&\le8U_1\frac{Y^2}{\lambda^{3/2}},\\
\|W^{(\ell)}(t)-W^{(\ell)}(0)\|_F
&\le8U_\ell\frac{Y^2}{\lambda^{3/2}},\\
\sup_{\|v\|=1}\|h^{(\ell)}(t,v)-h^{(\ell)}(0,v)\|_n
&\le8F_\ell\frac{Y^2}{\lambda^{3/2}}.
\end{aligned}
\tag{12}
\]

The limiting predictor fits all training labels and has the explicit tail

\[
\begin{split}
\sup_{\|v\|=1}|f_n(\infty,v)-f_n(t,v)|
&\le16\left(1+F\frac{Y^2}{\lambda}\right)
\frac{Y}{\lambda}e^{-\lambda t/2}\\
&\le\frac{65}{4}\frac{Y}{\lambda}e^{-\lambda t/2}.
\end{split}
\tag{13}
\]

The zero-label case is stationary with zero predictor and needs none of
the divisions by \(Y\). The theorem concerns the original dense network;
no reduced state or storage claim is part of it.

## 2. Why the initialized event has probability tending to one

A \(1/4\)-net of the unit sphere in \(\mathbb R^k\) can be chosen with
at most \(9^k\) points, by disjoint-ball volume comparison. Approximation
of the two maximizing vectors gives an operator norm at most twice the
maximum absolute bilinear form over the two nets. A fixed bilinear form
of \(W_0^{(\ell)}\) has variance \(1/n\). Hence

\[
\Pr\{\|W_0^{(\ell)}\|_{\rm op}>8\}
\le2e^{-n(8-2\log9)},\qquad
\Pr\{\|A_0\|_{\rm op}/\sqrt n>8\}
\le2e^{-8n+(n+d)\log9}.
\tag{14}
\]

These probabilities tend to zero for fixed \(d,L\).

For a fixed unit query \(v\), conditional on the preceding initialized
features, the next-layer preactivations are independent \(N(0,q_n)\)
with \(q_n=\|h^{(\ell-1)}(0,v)\|_n^2\). The first layer has \(q_n=1\).
Linear growth, \( |\phi_\ell(x)|\le|\phi_\ell(0)|+s|x| \), gives
uniform fourth moments for \(q_n\) in any compact interval. Conditional
Chebyshev therefore implies convergence of the empirical activation second
moment to \(\mathbb E\phi_\ell(\sqrt{q_n}G)^2\). This expectation is
continuous in \(q_n\), by the same linear-growth domination. Induction and
(1) give \(\|h^{(\ell)}(0,v)\|_n\to1\) in probability.

On the operator event in (14), the map
\(v\mapsto h^{(\ell)}(0,v)\), with output norm \(\|\cdot\|_n\), is
\((8s)^\ell\)-Lipschitz. Fix a sphere net of mesh
\([4(8s)^L]^{-1}\); its size is finite and independent of width. With
probability tending to one the feature norms at every net point and every
layer are at most \(5/4\). Interpolation adds at most \(1/4\), proving
the whole-sphere \(3/2\) bound in (6). For \(d=1\), use the two sphere
points directly.

For the finite training set, the same conditional argument applied to
products \(\phi_\ell(Z_a)\phi_\ell(Z_b)\) proves empirical covariance
convergence to (4). Conditional fourth moments bound the product variance.
Continuity at possibly singular covariance matrices follows by writing
\(Z=Q^{1/2}G\), using continuity of the positive-semidefinite square root
and Gaussian moment domination. Consequently
\(\mathsf H(0)^\top\mathsf H(0)/(mn)\to Q^{(L)}/m\) entrywise and
in operator norm, so the last event in (6) also has probability tending
to one. The preceding intersections are finite; no independence between
their events was used.

## 3. Complete stopped-flow proof

Stop when any sphere feature norm reaches 2, either initialized operator
cap 8 grows to 9, or the normalized top-feature Gram margin falls to
\(\lambda/4\). These are strict initial conditions on (6).
On this tube, backward recursion gives

\[
\|\delta_a^{(\ell)}\|_n\le D_\ell\|w\|_n.
\tag{15}
\]

Because (3) is negative gradient flow for \(\mathcal L=\rho^2\) in
the metric (10),

\[
-\partial_t\rho^2=\|\dot\theta\|_{\rm par}^2.
\tag{16}
\]

The readout part alone of the right-hand side is
\(4c^\top[\mathsf H^\top\mathsf H/(mn)]c/m\), at least
\(\lambda\rho^2\) on the stopped tube. Thus
\(-\dot\rho\ge\lambda\rho/2\), proving the stopped versions of
the residual and activity estimates in (9).

Where \(\rho>0\), changing variables from time to the decreasing residual
in (16) yields

\[
\begin{split}
\int_0^t\|\dot\theta\|_{\rm par}\,ds
&=\int_{\rho(t)}^Y
\sqrt{\frac{2\rho}{-\dot\rho}}\,d\rho\\
&\le\frac2{\sqrt\lambda}(Y-\rho(t))
\le\frac{2Y}{\sqrt\lambda}.
\end{split}
\tag{17}
\]

If the residual reaches zero, the velocity is zero and the same bound
continues. In particular (11) follows on the stopped tube.

Let \(W_* =2Y/\sqrt\lambda\), solely as a bound for readout RMS.
The triangle inequality in (3), (15), the training feature cap 2, and
\(m^{-1}\sum_a|c_a|\le\rho\) give

\[
\|\dot A\|_F/\sqrt n\le2\rho U_1W_*,
\qquad
\|\dot W^{(\ell)}\|_F\le2\rho U_\ell W_*.
\tag{18}
\]

Integration using \(\int\rho\le2Y/\lambda\) proves the first two
lines of (12). For a unit query, subtract the initialized forward pass:

\[
\begin{split}
\|\Delta h^{(1)}\|_n&\le s\|\Delta A\|_F/\sqrt n,\\
\|\Delta h^{(\ell)}\|_n
&\le s\{2\|\Delta W^{(\ell)}\|_F
             +9\|\Delta h^{(\ell-1)}\|_n\}.
\end{split}
\tag{19}
\]

For the second line write the preactivation difference as
\(\Delta W^{(\ell)}h^{(\ell-1)}(t)
+W^{(\ell)}(0)\Delta h^{(\ell-1)}\).
Its second coefficient is actually at most 8; using 9 matches (7) and
also covers the time-derivative recurrence below. Equations (7) and (18)
prove the last line of (12).

Under (8), every feature displacement and every normalized operator
displacement is at most

\[
8F\frac{Y^2}{\lambda^{3/2}}\le\frac{\sqrt\lambda}{8}\le\frac18.
\tag{20}
\]

Thus the sphere norms are at most \(13/8<2\), and the operators at most
\(65/8<9\). The normalized feature map from \(\mathbb R^m\) to
\((\mathbb R^n,\|\cdot\|_n)\) is
\(u\mapsto\mathsf H u/\sqrt m\). Its operator change is at most the
largest training feature change, hence at most \(\sqrt\lambda/8\).
Its least singular value remains at least

\[
\sqrt{\lambda/2}-\sqrt\lambda/8>\sqrt\lambda/2.
\tag{21}
\]

This strictly improves the Gram stop. No stop can therefore occur.
For each finite width, the parameter path stays in a bounded subset of
its finite-dimensional parameter space. The locally Lipschitz vector
field extends the solution globally. The finite path length gives a
parameter limit, and residual decay gives fitting at that limit.

The same propagation as (19), now applied to the differentiated forward
pass and (18), gives for every query

\[
\|\dot h^{(\ell)}(t,v)\|_n\le2\rho W_*F_\ell,
\qquad \|\dot w\|_n\le4\rho.
\tag{22}
\]

Consequently

\[
|\dot f_n(t,v)|
\le 8\rho+2F W_*^2\rho
=8\left(1+F\frac{Y^2}{\lambda}\right)\rho.
\tag{23}
\]

Integrate the exponential residual bound from \(t\) to infinity to obtain
the first inequality of (13). Since \(FY^2/\lambda\le\lambda/64\le1/64\),
its second inequality follows. This completes the real theorem.

## 4. What normalization does and does not control

The derivative second moment

\[
\chi_\ell=\mathbb E\phi_\ell'(G)^2
\tag{24}
\]

is not used as a substitute for \(s\) in (7). It is an average under a
single Gaussian law; (15), (18), and (19) require a bound for the actual
gates on the trained path. Replacing \(9s\) by \(\sqrt\chi\) in those
inequalities is not valid. A proof exploiting \(\chi\approx1\) would
need new control of products of the dependent trained gates and weights
on the relevant response directions.

The real theorem supplies a specific exponential-depth fallback:
\(\sqrt F\) is comparable, with explicitly bounded factors, to
\(s(9s)^{L-1}\). It proves neither polynomial depth dependence nor a
growing-depth probability theorem. The initialized-event limit remains
at fixed \(d,L,m\).

Normalization and a known real slope bound do bound the intercept:

\[
|\phi_\ell(0)|
\le\mathbb E|\phi_\ell(G)|+s\mathbb E|G|
\le1+s\sqrt{2/\pi}.
\tag{25}
\]

Thus for the strip-analytic subclass with a known strip slope bound,
the value at zero is not an additional independent quantitative input.
An analytic strip width and its derivative bound still must be supplied.

The two Gaussian moments alone do not even control \(s\). Here is a
concrete smooth unbounded family. Fix a nonzero even \(C^\infty\) bump
\(\eta\) supported in \([-1,1]\), and for integers \(N\ge2\) put

\[
b_N(x)=\eta(N(x-N))-\eta(N(x+N)),\qquad
\sigma_N^2=\mathbb E[G+b_N(G)]^2,\qquad
\phi_N(x)=\frac{x+b_N(x)}{\sigma_N}.
\tag{26}
\]

Each activation is smooth, globally Lipschitz, and unbounded, and its
Gaussian second moment is exactly one. The bump is supported where
\(N-1/N\le|x|\le N+1/N\), with Gaussian probability at most

\[
p_N=\frac4{N\sqrt{2\pi}}e^{-(N-1/N)^2/2}.
\tag{27}
\]

Writing \(M_j=\|\eta^{(j)}\|_\infty\), disjointness of the two
supports gives

\[
\mathbb E b_N(G)^2\le M_0^2p_N,\qquad
\mathbb E b_N'(G)^2\le N^2M_1^2p_N,\qquad
|\mathbb E G b_N(G)|\le(N+1/N)M_0p_N.
\tag{28}
\]

Integration by parts against the Gaussian density has no boundary term
and gives \(\mathbb E b_N'(G)=\mathbb E G b_N(G)\). Hence

\[
\chi_N-1
=\frac{\mathbb E b_N'(G)^2-\mathbb E b_N(G)^2}{\sigma_N^2}
\longrightarrow0,\qquad \sigma_N\longrightarrow1.
\tag{29}
\]

But \(\|\phi_N'\|_\infty\ge(NM_1-1)/\sigma_N\to\infty\).
The nonzero compact bump also precludes real analyticity: the activation
agrees with \(x/\sigma_N\) on an open interval but not everywhere.
This example establishes that moments near the requested normalization
do not provide the missing uniform slope or analytic strip data. It does
not disprove a different compression method for smooth activations.

## 5. The quantitative bridge still required for compression

The qualitative unbounded extension assumes bounded derivative on a complex
strip. Its checked mechanism is a **joint preactivation and carrier budget**,
including the top readout carrier. The real theorem above does not replace
that mechanism.

For example, a bound \(\|w\|_n\le W_*\) gives only
\(\max_i|w_i|\le\sqrt n W_*\). It supplies no logarithmic coordinate
bound. The vector \(\sqrt n e_1\) demonstrates the logical distinction.
In the runtime backward subtraction, a changed gate is multiplied by the
reference carrier coordinate. Substituting this deterministic
\(\sqrt n\) bound into the existing Gronwall comparison does not give
an \(n^{-1/2}\) compression error from source tolerance \(n^{-1}\).
Similarly, an RMS bound alone allows a coordinate time or angular speed
of order \(\sqrt n\); the resulting guaranteed analytic radius can be of
order \(n^{-1/2}\), which is insufficient for the existing polylogarithmic
source-rank argument. Coordinate concentration is an essential theorem
input, not an optional improvement of its numerical prefactor.

More precisely, let \(S\) be a deterministic residual-activity allowance,
let \(Z_i\) and \(K_i\) be the stopped training maxima of preactivation
and carrier at neuron \(i\), and stop the layer-summed exponential budget
\(n^{-1}\sum_{\ell,i}\exp\{\eta(Z_i+K_i/S)\}\) at \(B\ge1\).
The unbounded route/check obtain, up to vanishing width errors,

\[
u_i\le g_{\delta,i}+A(1+Z_i),\qquad
Z_i\le g_{h,i}+D u_i,\qquad u_i=K_i/S,
\tag{30}
\]

with

\[
A=C_1(1+S^2B),\qquad D=C_2S^2(1+S^2\sqrt B).
\tag{31}
\]

Here \(g_h,g_\delta\) are the independent-cavity Gaussian reference
suprema, with the reverse one divided by \(S\). These are two coupled
inequalities, absent from the bounded-value label proof. Exact elimination
requires \(AD<1\) and gives

\[
u_i\le\frac{g_{\delta,i}+A(1+g_{h,i})}{1-AD},\qquad
Z_i+u_i\le g_{h,i}
+\frac{1+D}{1-AD}[g_{\delta,i}+A(1+g_{h,i})].
\tag{32}
\]

The transparent sufficient restrictions

\[
S^2B\le1,\qquad S^2\le(8C_1C_2)^{-1}
\tag{33}
\]

give \(AD\le1/2\). To turn this into an explicit label theorem, one must
also quantitatively bound the exponential moments of the Gaussian
references in (32), with a base independent of \(B\) after the allowed
smallness restrictions; that base then selects \(B\) before \(S\).
These bounds require the incoming forward modulus as well as the outgoing
reverse modulus, the learned-column term with its actual amplitude
\(1+Z_i\), the reciprocal forward trace, and the top carrier curvature.
The surviving Hessian coefficient multiplying \(S^2\log n\) must also
be bounded explicitly to retain the insertion propagator's small power
of width. Its coefficient cannot be moved into a width threshold.

The bounded explicit label/source routes quantify a different set of
inequalities: they use a fixed activation bound for the incoming omitted
control and a pointwise readout bound for the top Hessian curvature and
top changed gate. In particular their scalar singleton shift has no
\(Z_i\leftrightarrow K_i/S\) feedback to close. Their numeric recurrences
therefore do not specify the constants or moment base needed in
(30)--(33). This is the unresolved quantitative proof obligation; it is
not repaired by replacing an activation bound with a feature RMS bound
inside the existing formulas.

Once that obligation is resolved, one must still propagate its stated
carrier and complex-radius coefficients through the chosen source count
and runtime. RUNTIME_SMALL_ACTIVITY_CONSTANT_ROUTE.md starts from a
specified tanh source constant and fixed derivative/feature coefficients;
its numerical error certificate does not already quantify the unbounded
case. A new bound may use the real theorem here, but that would require
the corresponding selected-metric and source-defect derivation.

For a merely smooth activation the earlier obstruction is even prior to
these quantitative steps: no holomorphic extension or finite-jet analytic
continuation has been supplied. Smooth jets need not determine later
values. For instance the ODE \(x'=1+\eta(x-2)\), \(x(0)=0\), with a
nonnegative smooth bump positive on \((-1,1)\) and zero outside, has the
same initial jet as \(x'=1\) yet changes after entering the bump. This
illustrates the route-specific failure of analytic continuation from
initial derivatives; it is not a claim that every initialization-only
method is impossible.

## 6. Result status

| Claim | Status in this note |
| --- | --- |
| Explicit all-time dense fitting for normalized smooth Lipschitz activations | Proved by (6)--(23), conditional on the exact initialized event whose probability tends to one |
| Uniform real sphere feature RMS without a global activation-value bound | Proved, with cap 2 and explicit displacement estimates |
| Explicit all-time dense output tail and fitted endpoint | Proved in (13) |
| Polynomial-depth replacement using only \(\mathbb E\phi^2=1\), \(\chi\approx1\) | Not proved; those moments do not supply the pathwise derivative estimates |
| Existing strip-analytic unbounded qualitative compressor | Retains its prior conditional internal status; this note finds no counterexample to it |
| Fully explicit label/error/size theorem for that compressor | Open here: the joint quantitative insertion/budget bridge above was not closed |
| Same analytic compression theorem for all smooth Lipschitz activations | Not established by the supplied sources; its analyticity hypothesis is absent |

No exponential or polynomial envelope is assigned to an unnamed source
constant. The explicit fallback proved here has an exponential-depth
label coefficient, but it is a fitting theorem rather than a compression
theorem. This distinction is necessary when incorporating the result into
the current study's final claim.

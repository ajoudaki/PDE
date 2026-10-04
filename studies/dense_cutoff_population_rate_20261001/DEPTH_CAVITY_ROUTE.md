# Fixed-depth finite deletion with forward and reverse sources

2026-10-03. **Internally reconstructed bounded-activation result.**
This note gives a finite-width carrier theorem at every fixed depth.
The local calculation is checked in `DEPTH_INSERTION_CHECK.md`; the
probability chain is checked in `DEPTH_CAVITY_PROBABILITY_CHECK.md`.
These are collaborative study checks, not independent promotion reviews.
It retains the actual adaptive residual and the original
unclipped dense flow. No experiment or Git mutation was performed.

Scientific inputs read completely: `Q_ORDER_POSITIVE_ROUTE.md`,
`Q_ORDER_INSERTION_CHECK.md`, `Q_ORDER_POSITIVE_PROBABILITY_CHECK.md`,
`FINITE_MIXED_MOMENT_ROUTE.md`, `FINITE_MIXED_MOMENT_CHECK.md`, current
`paper/main.tex` and all its included mathematical files, `docs/index.qmd`,
and `docs/notation.qmd`. Required process and mathematical skills were read.
The basic middle-layer deletion identity, supremum-budget trace method,
cutoff modulus, and weakened Gaussian-net exponents were developed before
root messages supplied matching constructions. Those messages and their
reverse-probe reconstruction were subsequently used in this writeup. No
sibling new route file has been read. Accordingly this is a collaborator
construction, not a blind review. Writes are confined to this file.
The coordinator subsequently restored mathematical delimiters, made the
initialization event and fixed-weight variant explicit, and reconciled
Section 9 with the checked deterministic study route. Those amendments
are included in the final source versions recorded by the checks.

## 1. Statement and normalization

Fix depth \(L\ge2\), finite data \(v_a=x_a/\sqrt d\in\mathbb R^d\),
\(a=1,\ldots,m\), and activations

\[
 \phi_\ell\in C^3(\mathbb R),\qquad
 \max_{0\le j\le3}\|\phi_\ell^{(j)}\|_\infty\le C_\phi.
 \tag{1}
\]

The network is
\[
 z_a^{(1)}=W^{(1)}v_a,\quad
 z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\quad
 h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),\quad
 f_a=n^{-1}w^\top h_a^{(L)},\quad r_a=f_a-y_a.
\]
The loss is \(m^{-1}\sum_a r_a^2\), with mobilities
\((n,1,\ldots,1,n)\). First weights are independent \(N(0,1)\),
hidden entries independent \(N(0,1/n)\), and \(w(0)=0\). All initial
blocks are independent. Define the backward carriers and derivatives by
\[
 k_a^{(L)}=w,\qquad
 \delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)},
 \qquad k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}
 \quad(\ell<L).
\]
Assume the initialized limiting readout-feature Gram has a positive gap.
The manuscript's deterministic small-label fitting argument, including
rectangular cavities with normalization still \(n\), then supplies common
constants \(K,\kappa,C>0\) and a fixed sufficiently small label threshold.
Put \(Y=(m^{-1}\sum_a y_a^2)^{1/2}\) and \(S=2Y/\kappa\). The case
\(Y=0\) is stationary. On common initialization events of probability
tending to one, the full flow and every fixed-size cavity obey
\[
 \rho(t)\le Y e^{-\kappa t},\quad
 \max_{\ell\ge2}\|W^{(\ell)}\|_{\rm op}\le K,\quad
 \|w\|_\infty\le CS,\quad
 \max_{a,\ell}\frac{\|k_a^{(\ell)}\|_2}{\sqrt n}\le CS.
 \tag{2}
\]
Here and below constants depend on fixed depth, data, activation bounds,
and Gram margin. They do not depend on the finite deletion count except
where a subscript explicitly permits this. The width threshold may depend
on that count. The positive label threshold must not.

**Finite carrier theorem.** For sufficiently small fixed labels there are
events of probability tending to one on which
\[
 \sup_{t\ge0}\max_{a,\ell,i}|k_{a,i}^{(\ell)}(t)|
 \le C S\sqrt{\log(e+n)}.
 \tag{3}
\]
No clipping or carrier-moment hypothesis remains in this conclusion.
This note proves the finite carrier input; the final closure comparison
uses the separately checked deterministic study result built from the
manuscript's all-depth fitting and projection arguments, as detailed
in Section 9.

## 2. Exact deletion of an interior neuron

Choose one layer \(j\in\{1,\ldots,L-1\}\) and delete a fixed set
\(I\subset\{1,\ldots,n\}\), \(|I|=r\). Delete the corresponding
incoming rows of \(W^{(j)}\) and outgoing columns of \(W^{(j+1)}\).
Every other layer has width \(n\); layer \(j\) has width \(n-r\).
Every normalization remains \(n\). The autonomous zero-source cavity
uses its own prediction and residual.
Deletion means a rectangular retained layer, or equivalently zero
embedding of an omitted activation. It does not mean setting its
preactivation to zero: these operations differ when \(\phi_j(0)\ne0\).

For \(j\ge2\), write the omitted initialized incoming rows as columns
\(y_i=W^{(j)\top}_{0,i,:}\in\mathbb R^n\), and the outgoing columns
as \(x_i=W^{(j+1)}_{0,:,i}\in\mathbb R^n\). Conditional on retained
initialization, all \((x_i,y_i)_{i\in I}\) are independent
\(N(0,I_n/n)\). At \(j=1\) only the \(x_i\) are used; the omitted
first-layer rows need not enter any retained equation.

Use Euclidean mobility coordinates
\[
 \Theta=(W^{(1)},H^{(2)},\ldots,H^{(L)},w),\qquad
 H^{(\ell)}=\sqrt n W^{(\ell)}.
\]
In the retained forward pass insert an external vector \(e_a\) at
preactivation \(z_a^{(j+1)}\). Let
\(\mathcal F_a(\Theta,e)=w^\top h_a^{(L)}\), and keep
\(r_a=\mathcal F_a/n-y_a\). Let \(D_\Theta h_a^{(j-1)}\) denote
the derivative of the lower activation vector with respect to all retained
parameters. It has uniformly bounded operator norm on the physical tube.
An additional reverse vector \(q_a\in\mathbb R^n\), for \(j\ge2\),
gives the exact retained equation
\[
 \dot\Theta=-\frac2m\sum_a r_a
 \left[\nabla_\Theta\mathcal F_a(\Theta,e)
       +D_\Theta h_a^{(j-1)}(\Theta)^\top q_a\right].
 \tag{4}
\]
For \(j=1\) the second term is absent. Importantly, the residual in
(4) is the forward residual and does not include an artificial scalar
\(q_a^\top h_a^{(j-1)}\).

For the actual full-network path the sources are
\[
 e_a=\sum_{i\in I}W^{(j+1)}_{:,i}\,h_{a,i}^{(j)},\qquad
 q_a=\sum_{i\in I}W^{(j)\top}_{i,:}\,\delta_{a,i}^{(j)}.
 \tag{5}
\]
To verify (4), hold the omitted coordinates fixed while differentiating
the retained forward function. Its derivative misses only paths passing
through the omitted activation. Their chain-rule contribution is
\(\sum_i\delta_{a,i}^{(j)}W^{(j)\top}_{i,:}\) at the derivative
of \(h_a^{(j-1)}\), which is precisely the second term in (4).
All retained gradient blocks therefore equal those of the full network.
This reverse term is necessary at interior layers.

## 3. Stops, controls, and the deterministic Hessian structure

For each retained neuron set
\[
 K_i^{(\ell)}(t)=\max_a|k_{a,i}^{(\ell)}(t)|,
 \qquad
 \mathcal H_\eta(t)=\frac1n\sum_{\ell=1}^{L-1}\sum_i
 \exp\left\{\frac\eta S\sup_{0\le u\le t}K_i^{(\ell)}(u)\right\}.
 \tag{6}
\]
Fix \(\eta>0\) and a budget \(B>L\), to be chosen later. Stop the full
flow at the first attainment of \(B\), capped at
\(T_n=c_T\log(e+n)\), and denote its stop by \(\sigma\).
Each cavity has its own stop \(\sigma_{-I}\), with budget \(2B\).
Its omitted coordinates can be filled by zero carriers in (6), at a cost
\(r/n\). The budget is a proof device, not part of the training flow.
It implies the weak maximum directly:
\[
 \max_{a,\ell,i,u\le\sigma}|k_{a,i}^{(\ell)}(u)|
 \le\frac S\eta\log(nB)\le M_n:=A_0S\log(e+n),
 \tag{7}
\]
for \(A_0>2/\eta\) and sufficiently large width. The cavity bound
uses \(2B\) and the same \(A_0\). The readout satisfies (2).

The deterministic external control class is
\[
 e_a(t)=\sum_{i\in I}x_i a_{a,i}(t)+\zeta_a(t),\qquad
 q_a(t)=\sum_{i\in I}y_i b_{a,i}(t)+\chi_a(t),
 \tag{8}
\]
where \(|a_{a,i}|\le C\), \(|b_{a,i}|\le CM_n\), all control
Lipschitz constants are at most \(C_r\sqrt n(\log(e+n))^{C_L}\),
and
\[
 \sup_{a,t}(\|\zeta_a\|_2+\|\chi_a\|_2)
 \le C_r n^{-1/2}(\log(e+n))^{C_L}.
 \tag{9}
\]
The small remainders may be adaptive: estimates are pathwise along an
existing solution. No well-posedness claim for arbitrary feedback rules
is intended. The actual network sources are continuous and meet these
requirements on the common stopped prefix.

For this last statement, physical forward speeds have RMS at most
\(CS\rho\). Differentiating backwards, using (7), gives backward
speeds with RMS at most \(C\rho(1+SM_n)\). Converting RMS to a
coordinate bound costs \(\sqrt n\), yielding the control Lipschitz
bound. Moreover the omitted column and row increments obey
\[
 \|W^{(j+1)}_{:,i}-x_i\|_2\le CS^2/\sqrt n,
 \qquad
 \|W^{(j)\top}_{i,:}-y_i\|_2\le CS M_n/\sqrt n.
 \tag{10}
\]
The first estimate uses bounded \(h_i\) and the upper response RMS;
the second uses \(|\delta_i|\le CM_n\) and bounded activation RMS.
Pairing the second with \(b_i=\delta_i\) gives
\(CSM_n^2/\sqrt n\), which is allowed in (9).

Here is the Hessian fact used throughout. At a zero-source cavity let
\(Z_a^{(\ell)}U=D_\Theta z_a^{(\ell)}[U]\) for a Euclidean parameter
variation \(U\). Its operator norm is at most \(C\): recursively,
\[
 Z_a^{(1)}U=U_1v_a,\qquad
 Z_a^{(\ell)}U=(U_{H^{(\ell)}}/\sqrt n)h_a^{(\ell-1)}
 +W^{(\ell)}\operatorname{diag}(\phi_{\ell-1}')Z_a^{(\ell-1)}U.
\]
Suppress evaluations at \(z_a^{(\ell)}\). Direct differentiation gives
\[
\begin{aligned}
 D^2\mathcal F_a[U,V]={}&
 U_w^\top\operatorname{diag}(\phi_L')Z_a^{(L)}V
 +V_w^\top\operatorname{diag}(\phi_L')Z_a^{(L)}U\\
 &+\sum_{\ell=1}^L
 (Z_a^{(\ell)}U)^\top
 \operatorname{diag}(k_a^{(\ell)}\odot\phi_\ell'')Z_a^{(\ell)}V\\
 &+\sum_{\ell=2}^L\frac1{\sqrt n}\delta_a^{(\ell)\top}
 \left[U_{H^{(\ell)}}\operatorname{diag}(\phi_{\ell-1}')
 Z_a^{(\ell-1)}V
 +V_{H^{(\ell)}}\operatorname{diag}(\phi_{\ell-1}')
 Z_a^{(\ell-1)}U\right].
 \tag{11}
\end{aligned}
\]
Thus \(D^2\mathcal F_a=H_{0,a}+H_{1,a}\), where \(H_{0,a}\)
has rank at most \(C_Ln\) and operator norm at most \(C\), and \(H_{1,a}\)
is a fixed sum of bounded-map conjugations of the displayed carrier
diagonals. There are no products of two reference carriers in (11).
For the normalized Schatten norm
\(\|A\|_{p,n}=(n^{-1}\operatorname{tr}|A|^p)^{1/p}\),
the supremum budget gives, for \(p\ge2\),
\[
 \|H_{1,a}\|_{2,n}\le CS,\qquad
 \|H_{1,a}\|_{p,n}\le CS p(2B)^{1/p},\qquad
 \|D^2\mathcal F_a\|_{\rm op}\le C(1+M_n).
 \tag{12}
\]
For noninteger \(p\), \(x^p\le (p/e)^pe^x\) gives the same estimate.
The \(p=2\) estimate uses the deterministic RMS bound, independently of
the budget. Normalization is by \(n\), although the parameter dimension
is \(O(n^2)\).

## 4. Linearization and the conditional insertion event

Write \(F_0\) for (4) at zero sources, and \(J(t,s)\) for its
variational propagator along the cavity. Its exact derivative is
\[
 D_\Theta F_0=-\mathsf L\mathsf L^\top
       -\frac2m\sum_a r_aD^2\mathcal F_a,
 \qquad
 \mathsf L=\sqrt{\frac2{mn}}[\nabla\mathcal F_a]_a.
 \tag{13}
\]
The first term is the adaptive-residual contribution. Its propagator
\(U_0(t,s)\) is contractive by differentiation of squared norm. Using
(12), total residual activity \(CS\), and (7), choose \(S\) small
with a strict margin so that
\[
 \sup_{s\le t\le\sigma_{-I}}\|J(t,s)\|_{\rm op}
 \le \exp\{CS(1+M_n)\}\le n^{1/1000}.
 \tag{14}
\]
This smallness choice is independent of \(r\).

Let \(d_a=\delta_a^{(j+1)}\), \(B_a=D_\Theta d_a\), and
\(C_a=D_\Theta h_a^{(j-1)}\). External differentiation of (4) at
zero sources gives
\[
 P_a=-\frac2{mn}\nabla\mathcal F_a d_a^\top,\qquad
 Q_a=-\frac2m r_a B_a^\top,\qquad
 T_a=-\frac2m r_a C_a^\top.
 \tag{15}
\]
Here \(P_a\) has rank one and norm \(CS\);
\(\|B_a\|\le C(1+M_n)\), \(\|C_a\|\le C\).
The \(T_a\) term is absent for \(j=1\). For fixed deterministic
controls, the full first variation with zero initial value is
\[
 V(t)=\sum_{a,i\in I}\int_0^tJ(t,s)
 \big[(P_a+Q_a)x_i a_{a,i}(s)+T_a y_i b_{a,i}(s)\big]\,ds.
 \tag{16}
\]
The response \(d_a\) also has its direct forward-source derivative
\(E_a=D_{e_a}d_a\). There is no direct reverse-source derivative of
this upper response.

The conditional good event includes the Euclidean bounds \(n^{1/100}\)
for \(V\) and its full linear preactivation, activation, readout, and
backward-vector variations, and the coordinate bounds \(n^{-1/10}\)
for all these vector variations. It also includes coordinate bounds
\(n^{-1/10}\) for every lower adjoint probe obtained by propagating each
\(y_i\) through the cavity's lower forward derivative. The latter are
centered Gaussian vectors with covariance operator \(O(1/n)\).
Include the corresponding direct forward source coordinates and all
centered quadratic and cross-bilinear pairings used below.

For each fixed control, all these linear maps have operator norm at most
\(n^{1/200}\) for large \(n\), by (14) and polynomial logarithmic
factors. Each coordinate therefore has variance at most
\(C_rn^{-1+1/100}\). Its tail at \(n^{-1/10}/2\) is at most
\(2\exp(-c_rn^{79/100})\). The full Euclidean image has Gaussian
input dimension at most \(2rn\), irrespective of parameter dimension,
so Gaussian concentration gives the stated \(n^{1/100}\) norm bound.

For a deterministic matrix \(R\), the elementary Gaussian-square
calculation gives
\[
 \Pr\{|x^\top Rx-\operatorname{tr}R/n|>u\}
 \le2\exp\left[-c\min\left\{
 \frac{n^2u^2}{\|R\|_{\rm HS}^2},
 \frac{nu}{\|R\|_{\rm op}}\right\}\right].
 \tag{17}
\]
The same estimate, up to constants and with zero mean, applies to
\(x^\top Ry\) for independent Gaussian \(x,y\): apply (17) to the
symmetric block matrix with off-diagonal blocks \(R/2,R^\top/2\).
At the above operator bounds and \(u=n^{-1/10}/2\), the exponent is
again \(n^{79/100}\).

Use an internal uniform control net at accuracy \(n^{-1/8}\).
Sampling time with spacing accuracy divided by the Lipschitz bound and
rounding values proves
\[
 \log N\le C_r n^{5/8}(\log(e+n))^{C_L}.
 \tag{18}
\]
Interpolation errors are at most \(n^{-1/8+1/200}\) times fixed
Gaussian norm bounds, hence \(o(n^{-1/10})\). Include a polynomially
fine terminal-time grid: bounded first three derivatives and the stopped
physical tube give polynomial time moduli for all response operators,
so this costs only \(O(\log n)\) in log cardinality. Consequently
one conditional event, of failure at most
\(C_r\exp(-n^{7/10})\), covers all controls and all terminal times.
This uniformity permits the actual controls to depend on the omitted
Gaussian variables after the event is established.

## 5. Nonlinear insertion remainder

Set \(a=1/100\), \(b=1/10\), and let
\(U=\Theta-\Theta^0-V\), \(u=\|U\|\le n^{-1/25}\).
In every forward and backward coordinate expansion split the increment
into the linear part \(V\), whose coordinate norm is \(n^{-b}\),
and the unknown remainder \(U\). Set, only for this calculation,
\[
 R=n^{a-b}+n^{-b}u+u^2,
 \qquad P=n^{-1/2}(n^{2a}+n^au+u^2).
 \tag{19}
\]
Every scalar gate Taylor remainder has Euclidean norm at most \(CR\),
since
\[
 \|v^2\|_2\le\|v\|_\infty\|v\|_2\le n^{a-b},\quad
 \|v\odot u_0\|_2\le n^{-b}\|u_0\|_2,\quad
 \|u_0^2\|_2\le\|u_0\|_2^2.
\]
Forward expansion proceeds layer by layer. Each matrix cross product
has the factor \(1/\sqrt n\), hence costs \(CP\); propagation through
reference operators and gates has bounded norm. Thus each forward
remainder costs \(C_L(R+P)\).

The backward expansion then proceeds from the top. A reference-carrier
times gate remainder costs \(CM_nR\). A changed gate times a changed
carrier uses the coordinate bounds of both linear variations. Its
product of two linear variations costs \(Cn^{a-b}\); each mixed
linear-and-remainder term uses the linear coordinate bound, and the
product of two remainder terms costs a polynomial
in \(1+M_n\) times \(u^2\). Matrix cross terms again retain
\(1/\sqrt n\). The source \(q\) enters additively in the lower
carrier before this recursion; its Gaussian linear coordinates are
already in the event. Descending a fixed number of layers gives a
gradient remainder bounded by
\[
 C_L(1+M_n)^{C_L}(R+P).
 \tag{20}
\]
This argument uses the linear backward coordinate event as well as the
linear forward event. Replacing a mixed bound by \(n^a u\) would be
invalid at the required scale.

For an explicit independent control of the reverse-source dependence,
consider \(\psi_y(\Theta)=y^\top h_a^{(j-1)}(\Theta)\).
At the reference its backpropagated probe carriers have coordinate size
\(n^{-b}\) and Euclidean norm \(O(1)\). On the segment
\(\Theta^0+v(V+U)\), \(0\le v\le1\), forward differences have
Euclidean size \(C(n^a+u)\). Backward probe subtraction therefore gives
\[
 \|\text{probe}(v)-\text{probe}(0)\|_2
 \le C_L\{n^{-b}(n^a+u)+n^{-1/2}(n^a+u)\}.
 \tag{21}
\]
At each stage the changed gate multiplies the *reference* probe with
the coordinate bound \(n^{-b}\); the changed matrix multiplies a
bounded Euclidean probe and has operator size \(C(n^a+u)/\sqrt n\).
The changed probe propagates through bounded matrices. This proves
(21) inductively, without assuming delocalization of a changed probe.
The Hessian formula for \(\psi_y\), analogous to (11), then gives
\[
 \sup_v\|D^2\psi_y(\Theta^0+v(V+U))\|_{
 \rm op}
 \le C_L\{n^{a-b}+n^{-b}u+n^{-1/2}(1+n^a+u)\}.
 \tag{22}
\]
Thus subtracting the reverse linear forcing leaves a term bounded by
\(\rho^0(\log n)^{C_L}[n^{2a-b}+n^{a-b}u+n^{-b}u^2]\),
plus the residual-adaptation products described next. This slightly
weaker alternative to the recursion (20) still closes the bootstrap.

The scalar residual has first variation \(O((n^a+u)/\sqrt n)\)
and scalar Taylor remainder
\(O((1+M_n)(n^{2a}+n^au+u^2)/n)\). This follows from (11)
for the forward scalar function, including the external \(e\) variable,
on its joining segment. The preceding expansions keep every segment
carrier within its reference maximum plus \(o(1)\); hence that Hessian
bound is valid on the segment. Multiplication by the reference gradient,
of norm \(C\sqrt n\), and the cross product of residual and gradient
differences produce the unweighted \(P\) term. For the reverse forcing,
the residual difference times the reference probe has the same
\(n^{-1/2}\) factor, times polynomial logarithms.

Combining the deliberately weaker reverse estimate with (20), the full
vector-field remainder in (4) is bounded by
\[
 C_r(1+M_n)^{C_L}
 \left[\rho^0\{n^{2a-b}+n^{a-b}u+n^{-b}u^2+R\}+P\right].
 \tag{23}
\]
The principal new exponent is \(2a-b=-8/100\).
Variation of constants multiplies the integrated bound by \(n^{1/1000}\).
Its residual-weighted part integrates with mass \(CS\); the unweighted
part integrates over \(T_n=O(\log n)\). At \(u\le n^{-1/25}\)
the largest terms are \(n^{-8/100}\) and \(u^2=n^{-8/100}\),
up to logarithms. After propagation they are \(o(n^{-1/25})\).
The small adaptive sources (9) cost only
\(n^{-1/2+1/1000}(\log n)^{C_L}\). Continuity therefore closes
the remainder bound. All retained carriers differ from their cavity
counterparts by at most
\[
 \varepsilon_{n,r}=C_r n^{-1/30}=o(1),
 \tag{24}
\]
after absorbing logarithmic factors. The response \(d_a\) differs in
ordinary Euclidean norm by at most \(C_rn^{1/100}\). These estimates
hold until the common prefix of full and cavity stops. They do not
assume the cavity survives first.

## 6. Endpoint trace with all upper carrier factors retained

The mixed derivative \(B_a=D_\Theta\delta_a^{(j+1)}\) has the same
decomposition as the Hessian in (11), with one argument restricted to
the external preactivation. Consequently
\[
 \|B_a\|_{2,n}\le C,
 \qquad \|B_a\|_{p,n}\le C[1+Sp(2B)^{1/p}].
 \tag{25}
\]
Both endpoints in the trace must retain these carrier factors; treating
\(B_a\) as bounded in operator norm independently of width is incorrect.

Write the residual Hessian as \(\mathcal A(t)d\mu(t)\), where
\(d\mu=(2/m)\sum_a|r_a|dt\), \(\mu([0,\infty)\)\le CS).
By (12), 
\(\|\mathcal A(t)\|_{p,n}\le C[1+Sp(2B)^{1/p}]\).
The term with \(h\ge1\) residual-Hessian insertions in
\(B_b(t)(J(t,s)-U_0(t,s))B_a(s)^\top\) is a product of \(h+2\)
noncontraction factors. Normalized Schatten Holder at exponent \(h+2\)
therefore bounds its normalized trace by
\[
 \frac{(CS)^h}{h!}
 \left[C\{1+S(h+2)(2B)^{1/(h+2)}\}\right]^{h+2}.
 \tag{26}
\]
The simplex factorial follows from replacing the integrands by their
common budget bounds; the contractions \(U_0\) do not increase any norm.
The normalization powers cancel because their reciprocal exponents sum
to one. There is no ambient-parameter dimension factor.

Using \((u+v)^{h+2}\le2^{h+1}(u^{h+2}+v^{h+2})\), the terms not
containing the budget sum to \(CS\). For the other terms,
\((h+2)^{h+2}/h!\le C^{h+1}(h+2)^2\), giving
\[
 \sum_{h\ge1}\text{bound in (26)}
 \le CS+CS^4 B
 \tag{27}
\]
for sufficiently small fixed \(S\). The \(h=0\) contraction term is
bounded by \(\|B_b\|_{2,n}\|B_a\|_{2,n}\le C\), using the
deterministic \(p=2\) estimate. The exterior forcing \(Q_a\) has a
residual factor whose integral is \(CS\). Thus its trace contribution
is at most \(CS+CS^5B\), and in particular at most
\(CS(1+S^2B)\).

The direct external derivative \(E_a=D_{e_a}\delta_a^{(j+1)}\)
is a sum, over upper layers, of matrices

\[
 T_\ell^\top\operatorname{diag}(k_a^{(\ell)}\odot\phi_\ell'')T_\ell,
 \qquad \|T_\ell\|_{\rm op}\le C.
\]
Its normalized trace is at most
\(C\sum_\ell n^{-1}\sum_i|k_{a,i}^{(\ell)}|\le CS\), by RMS.
The adaptive \(P_a\) term has rank one; (14) and the logarithmic
operator bound on \(B_b\) give normalized trace
\(n^{-1+1/1000}(\log n)^{C_L}\) after time integration, which vanishes.

For singleton deletion, the upper-response first variation has the form

\[
 d_a-d_a^{-i}=R^{xx}_a x_i+R^{xy}_a y_i+o_{\ell^2}(1).
\]
The notation records which Gaussian vector enters the linear response;
both matrices are deterministic conditional on the cavity and fixed
controls. The \(y_i\) term is absent at the first layer. Pairing with
\(x_i\), (17) centers the first term at its trace and the second at zero.
Uniformity over controls remains essential here. Adding the learned
outgoing-column correction from (10), whose pairing with the upper
response is \(CS^3\), gives
\[
 \sup_{a,t\le\min(\sigma,\sigma_{-i})}
 |k_{a,i}^{(j)}(t)-x_i^\top d_a^{-i}(t)|
 \le R(B,S)+o(1),\qquad R(B,S)=CS(1+S^2B).
 \tag{28}
\]
The singleton constant does not depend on any later empirical moment
degree or deletion count.

## 7. Gaussian whole-path references without a derivative-moment assumption

The supremum budget controls the time modulus needed for Gaussian
chaining; a width-uniform bound on the Euclidean variation of deeper
backward responses is not assumed. For one cavity set
\(u(t)=\mu([0,t])/S\), which has bounded total range. Physical speeds
give, for \(v=|u(t)-u(s)|\le1\),
\[
 \|w(t)-w(s)\|_2/\sqrt n\le CSv,\quad
 \max_\ell\|W^{(\ell)}(t)-W^{(\ell)}(s)\|_{
 \rm appropriate\ normalized\ norm}\le CS^2v,
 \quad\max_{a,\ell}\|z_a^{(\ell)}(t)-z_a^{(\ell)}(s)\|_2/\sqrt n
 \le CS^2v.
\]
The middle norm is Frobenius for hidden matrices and Frobenius divided
by \(\sqrt n\) for the first matrix. At a backward gate, split the
reference carrier at physical cutoff \(SR\). The changed-gate term is
at most
\[
 C S^3Rv+CS\sqrt{2B}\,e^{-c_\eta R}.
\]
The other terms propagate a backward difference by bounded operators
or cost \(CS^3v\). Choose
\(R=C_\eta[1+\log(e+B)+\log(1/v)]\); the tail is at most \(CSv\).
Descending through fixed depth gives
\[
 \frac{\|\delta_a^{(\ell)}(t)-\delta_a^{(\ell)}(s)\|_2}{S\sqrt n}
 \le C v[1+S^2\log(e+B)+S^2\log(1/v)]
 \le C\sqrt v
 \tag{29}
\]
provided \(S^2\log(e+B)\le1\). The final constant is independent
of \(B\) after this smallness choice. At \(v=0\) continuity or the
unchanged parameter state gives zero. Extending the activity range to
its fixed upper bound only changes \(C\).

Freeze a cavity response at its own stop, and set the whole proof
reference to zero if its cavity-measurable initialization conditions
fail. It is independent of all deleted \(x_i,y_i\). Equation (29)
implies that the Gaussian process
\(x_i^\top d_a^{-I}(t)/S\) has covering number at metric resolution
\(\epsilon\) at most \(C\epsilon^{-2}\), uniformly in its physical
horizon. Its initial value is zero. A dyadic net and the Gaussian tail
bound give
\[
 \Pr\{Z_i^{-I}>C(1+z)\mid\text{cavity}\}\le Ce^{-cz^2},
 \quad Z_i^{-I}=\max_a\sup_{t\le T_n}|x_i^\top d_a^{-I}(t)|/S.
 \tag{30}
\]
Indeed level \(k\) has at most \(C2^{2k}\) increments of standard
deviation \(C2^{-k}\); a union bound bounds them by
\(C2^{-k}(\sqrt{k+1}+z)\), and summation proves (30).
In particular for every fixed \(\lambda\ge0\),
\[
 \mathbb E[e^{\lambda Z_i^{-I}}\mid\text{cavity}]\le\mathcal L(\lambda),
 \tag{31}
\]
with deterministic finite \(\mathcal L(\lambda)\), independent of
width, fixed deletion count, and \(B\), under the stated smallness
condition. Conditional on the common cavity, the variables for distinct
\(i\in I\) are independent.

## 8. Removal of stops and the all-time carrier maximum

Let \(\mathcal G_n\) be the full-network initialization event with
fixed bounds on the first-weight Frobenius RMS, initial training
preactivation RMS, and hidden operator norms, and with an initial
readout-feature Gram at least \(2\lambda I_m\), where \(\lambda>0\)
is a fixed fraction of its positive limiting gap. Gaussian initialization
and the finite-data feature law of large numbers give
\(\Pr(\mathcal G_n)\to1\). Choose its norm bounds with strict
margins. This event is defined from the full initialization, independently
of the moment degree used below.

Every fixed deletion set inherits the deterministic fitting event from
the full initialization at sufficiently large width. Removing \(r\)
bounded initialized activations changes the next preactivation by
Euclidean norm at most \(C\sqrt r\), and forward propagation through
bounded operators gives normalized top-feature change \(C\sqrt{r/n}\).
The readout Gram therefore keeps a smaller fixed margin, uniformly over
all sets of that fixed size. The required first-layer and operator bounds
do not increase under deletion. Fix the common smaller \(\kappa\)
before setting \(S\).

Union the insertion events over all same-layer deletion sets of each
fixed size. Their failure remains superpolynomially small. Apply (24)
only to the common stopped prefix. For every retained coordinate its
running supremum differs by at most \(\varepsilon_{n,r}\), hence
\[
 \mathcal H_\eta^{-I}(t)
 \le e^{\eta\varepsilon_{n,r}/S}\mathcal H_\eta(t)+O(r/n)
 \le B+o(1)<2B.
 \tag{32}
\]
Thus no cavity reaches its budget before the full stop. This is a
strict-margin continuation argument and does not condition on the full
stop as an independence event.

For a fixed set \(I\ni i\) in one layer, full-to-singleton and
full-to-\(I\) comparisons give
\[
 \sup_{a,t\le\sigma}\|d_a^{-i}(t)-d_a^{-I}(t)\|_2
 \le C_rn^{1/100}.
 \tag{33}
\]
Their entire frozen difference is independent of \(x_i\), but (33)
holds only on a full-dependent prefix. Project the entire difference
onto the Euclidean ball of radius \(C_rn^{1/100}\). The resulting
process is independent of \(x_i\), agrees with the difference on the
successful prefix, and retains the modulus (29), since projection is
1-Lipschitz. For two cavity activity clocks use their sum, whose total
range is bounded. Its Gaussian pairing has variance at most
\(D_n^2=C_rn^{-1+2/100}\), and covering number at metric scale
\(\epsilon\) at most \(C(S/\epsilon)^2\). Chaining from diameter
\(D_n\) gives mean supremum
\(CD_n\sqrt{\log(e+S/D_n)}=o(1)\), and tail at \(n^{-1/10}\)
at most \(C_re^{-n^c}\). Consequently, simultaneously over fixed-size
sets,
\[
 \sup_{a,t\le\sigma}|x_i^\top(d_a^{-i}(t)-d_a^{-I}(t))|
 \le n^{-1/10}
 \tag{34}
\]
outside a superpolynomially small event. The same projection construction
as in the two-layer route is valid because the modulus, rather than total
variation, provides the entropy estimate.

For each layer \(j<L\), let
\[
 H_{n,j}=\mathbf1_{\mathcal G_n}\frac1n\sum_i
 \exp\{\eta\sup_{t\le\sigma}K_i^{(j)}(t)/S\}.
\]
Fix an integer \(p\ge1\) independently of width. Expand \(H_{n,j}^p\).
For a tuple of distinct indices use its set as the common deleted block.
Equations (28), (34), and (31) bound its expected product by
\[
 [\mathcal L(\eta)e^{\eta R(B,S)/S}]^p+o(1).
\]
Drop good-event and full-prefix indicators before conditional expectation.
The common-cavity Gaussian variables are independent. For collision
tuples, multiplicities \(d_i\) replace \(\mathcal L(\eta)\) by
the finite constants \(\mathcal L(d_i\eta)\); their count is
\(O_p(n^{p-1})\), so their normalized contribution vanishes. The
bad insertion event contributes \(o(1)\), since the stopped total
budget is at most \(B\). Therefore
\[
 \limsup_n\mathbb EH_{n,j}^p\le D(B,S)^p,
 \quad D(B,S)=\mathcal L(\eta)e^{C\eta(1+S^2B)}.
 \tag{35}
\]
The base is independent of \(p\). Constants and width thresholds for
fixed \(p\) may depend on \(p\).

There is no need for independence between layers. Minkowski's inequality
and (35) give
\[
 \limsup_n\mathbb E\Big(\sum_{j<L}H_{n,j}\Big)^p
 \le[(L-1)D(B,S)]^p.
 \tag{36}
\]
Choose \(B>4(L-1)\mathcal L(\eta)e^{C\eta}\) first, and then
choose \(S>0\) small enough for all preceding inequalities and
\(e^{C\eta S^2B}\le2\). All choices are independent of \(p\),
confidence and width. They give \((L-1)D(B,S)<B\). If the full
budget reaches \(B\) by \(T_n\), then \(\sum_{j<L}H_{n,j}=B\)
on \(\mathcal G_n\). For every fixed \(p\), Markov gives
\[
 \limsup_n\Pr\{\mathcal G_n,\text{budget reached by }T_n\}
 \le[(L-1)D(B,S)/B]^p.
\]
Taking the infimum over fixed integers \(p\) gives zero. Width tends
to infinity first at fixed \(p\); there is no growing-deletion theorem.

With the stops removed through \(T_n\), singleton insertion and (30),
unioned over the finitely many layers and \(n\) neurons, give (3) on
\([0,T_n]\), with a fixed sufficiently large constant. The trace shift
is fixed and is absorbed by \(S\sqrt{\log(e+n)}\).

To extend to every physical time, use the deterministic all-time tube
without any moment assumption. RMS gives the crude coordinate bound
\(\max|k|\le CS\sqrt n\). Backward differentiation and physical
forward speeds then give
\[
 \max_{a,\ell}\frac{\|\dot\delta_a^{(\ell)}\|_2+
                         \|\dot k_a^{(\ell)}\|_2}{\sqrt n}
 \le C(1+\sqrt n)\rho(t).
\]
After integrating and converting to a coordinate bound,
\[
 \sup_{t\ge T_n}\max_{a,\ell,i}
 |k_{a,i}^{(\ell)}(t)-k_{a,i}^{(\ell)}(T_n)|
 \le CS n e^{-\kappa T_n}=o(S)
 \tag{37}
\]
provided \(c_T\kappa>1\), for example \(c_T\kappa=2\).
This deliberately coarse tail avoids the unjustified reuse of the
two-layer condition \(c_T\kappa>1/2\). It proves the candidate
all-time carrier statement (3).

## 9. Scope of the closure consequence

The carrier theorem concerns the actual finite dense network. On its
good event choose \(M=CS\sqrt{\log(e+n)}+1\). Apply the separately
checked deterministic all-depth comparison in `DEPTH_TRACKING_ROUTE.md`
and `DEPTH_TRACKING_CHECK.md`. That study result uses the manuscript's
fitting and projection identities and proves
\[
 D_{n,q}\le CA_M\frac{1+M+\sqrt{\log(e+q)}}{q^2},
 \qquad A_M=Ce^{CM},
 \tag{38}
\]
whenever \(C(1+M)A_M/q\le1/4\), after fixing the prefactor in the
threshold. Here \(D_{n,q}\) is the all-time
normalized parameter distance between the actual same-width dense and
residual-RMS Legendre closure with shared initialization. Taking
the order
\[
 q_n=\left\lceil n^{1/4}\exp\{A\sqrt{\log(e+n)}\}\right\rceil
 \tag{39}
\]
with fixed sufficiently large \(A\), the absorption condition holds for
all sufficiently large width and every term in (38) is \(O(n^{-1/2})\).
The constants can be increased to absorb polynomial logarithmic factors.
The manuscript's whole-input inequality then gives for every fixed query
law \(\nu\) with finite second moment
\[
 \left(\int\sup_{t\ge0}|\widehat f_{n,q_n}(t,x)-f_{n,D}(t,x)|^2
                         d\nu(x)\right)^{1/2}
 \le C_\nu n^{-1/2}.
 \tag{40}
\]
This consequence uses that checked study source argument with its
feedback absorption, not an assumed direct all-depth \(q^{-2}\) defect.
The memory order is \(n^{1/4+o(1)}=o(n)\), and moving state has size
\(n^{5/4+o(1)}\) for fixed data and depth. Initialized dense matrices
remain stored and applied exactly.

The present theorem retains the positive initial feature-Gram condition.
Removing it for particular bounded activations and compatible sphere data
is a separate algebraic input, owned by the coordinating author. No
unbounded-activation extension, dense-to-population numerical rate,
incompatible-label theorem, or larger-label canonical theorem is claimed
by this file. The complete local and probability reconstructions are
recorded in the reports named at the start.

All conclusions also hold with fixed positive sample weights summing to
one. Replace every sample average by that weighted average and use weighted
residual RMS. With \(H_L(0)=[h_a^{(L)}(0)]_a\) and
\(D_p=\operatorname{diag}(\sqrt{p_a})\), the initial Gram becomes
\(D_pH_L(0)^\top H_L(0)D_p/n\); this agrees with the original
normalization when \(p_a=1/m\). The exact source identities then
have coefficient \(-2p_a\) instead of \(-2/m\). Cauchy--Schwarz still
bounds \(\sum_a p_a|r_a|\) by the residual RMS; the residual-Hessian
measure has the same activity bound. All other bounds use only the fixed
number of samples and fixed operator/Gram constants. In particular the
constants selecting the budget and label threshold remain independent
of the deletion count and empirical moment degree. This variant permits
the exact compatible data quotients used by the coordinator's activation
lemma.

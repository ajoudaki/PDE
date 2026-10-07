# Fixed-order insertion remainders with an absolute cutoff power

2026-10-07. Scoped author derivation, not an independent review or a
source-probability theorem.

The local nonlinear gradient estimate can use one power of the reference
carrier cutoff, with a coefficient bounded by a fixed power of
\(\beta^L\). The adaptive residual and the original reverse deletion
force preserve this property. Converting the learned row/column corrections
and the top-layer prediction offset into additional forces needs at most
three powers of the joint coordinate cutoff. This removes the
depth-dependent cutoff exponent in the corresponding *deterministic local
remainder estimate*. It does not quantify the Gaussian control event,
common-cavity comparison, collision moments, or source success probability.

## 1. Inputs, coordinates, and the local hypotheses

Complete scientific inputs read were exactly:

- `studies/unseen_query_decoder_20261005/EXPLICIT_FITTING_WIDTH.md`, hash
  `62d018c6448b0e6af6085827a856667ba58747810c6b284452dea21ce800919d`;
- `studies/dense_cutoff_population_rate_20261001/UNBOUNDED_INSERTION_CHECK.md`,
  hash `bec5707fccc99597570ce51c94d3a487fd0b1ede14578617275cb708fdd95578`;
- `studies/dense_cutoff_population_rate_20261001/DEPTH_CAVITY_ROUTE.md`,
  hash `e8f9f43c137a9c74b751cbd2e54cf5a2b13f090c560d912b4b17994c53bc1478`;
- `studies/dense_cutoff_population_rate_20261001/DEPTH_INSERTION_CHECK.md`,
  hash `77c51e725629e736a33c16dbe4ec179b5aa859b527539815f55422a818a1e977`;
- `studies/integrated_general_compression_20261004/UNBOUNDED_COMPRESSOR_BRIDGE.md`,
  hash `e018f0291b4456913a6541d5db7d90a678c4564928edcd5f47dd8c5326336f5d`.

Their linked research files were not followed. The canonical-notation and
rigorous-math skills apply. No experiments or Git operations were used, and
this is the only artifact written for this subtask.

Use the original mobility coordinates, with ordinary Euclidean/Frobenius
norm on their direct sum:
\[
\Theta=(A,H^{(2)},\ldots,H^{(L)},w),\qquad
H^{(j)}=\sqrt nW^{(j)},\qquad F_a=nf_a=w^\top h_a^{(L)}.
\]
Here \(H^{(j)}\) is a rescaled weight matrix, not a feature norm.
All retained hidden widths are at most \(n\); rectangular deletion keeps
every normalization equal to \(n\). For proof purposes, add a vector
\(e_a^{(j)}\) at each preactivation. Thus
\[
z_a^{(1)}=Av_a+e_a^{(1)},\qquad
z_a^{(j)}=H^{(j)}h_a^{(j-1)}/\sqrt n+e_a^{(j)},\qquad
h_a^{(j)}=\phi_j(z_a^{(j)}).
\]
An actual interior deletion uses only the port at layer \(j+1\).
Let \(X_a=(\Theta,e_a)\) denote the augmented coordinates for sample
\(a\). All norms below are unnormalized Euclidean norms unless a factor
\(1/\sqrt n\) is displayed.

Take the finite activation envelope \(\beta\) of the fitting note (11),
and the strip assumptions in the source bridge. In particular
\(\beta\ge10\), \(b,\|\phi'_j\|_\infty,\|\phi''_j\|_\infty\le\beta\)
on the real axis. Cauchy's formula on a circle of radius \(a/4\) gives
\(\|\phi'''_j\|_{L^\infty(\mathbb R)}\le4\beta/a\le\beta^2\).

At a real zero-port reference \(X_a^0\), assume
\[
\|A^0\|_{\rm op}/\sqrt n\le10,\qquad
\max_{j\ge2}\|W^{(j),0}\|_{\rm op}\le10,\qquad
\|w^0\|_2/\sqrt n\le\beta^{3L},\qquad
\max_{a,j}\|k_a^{(j),0}\|_\infty\le M.
\tag{1}
\]
The carrier and response definitions are the originals:
\[
k_a^{(L)}=w,\qquad
\delta_a^{(j)}=\phi'_j(z_a^{(j)})\odot k_a^{(j)},\qquad
k_a^{(j)}=W^{(j+1)\top}\delta_a^{(j+1)}.
\]
The source's physical tube with \(S\le1\) implies the readout bound
in (1): its recurrence gives \(H_L\le(21\beta)^L\le\beta^{3L}\).
The dense-fitting readout bound is stronger.

Write the augmented displacement as \(\eta_a=V_a+U_a\), where
\(V_a=(V_\Theta,e_a)\), \(U_a=(U_\Theta,0)\). Assume, uniformly over
samples,
\[
\|V_a\|\le N,\quad \|U_a\|\le u,\quad
N\ge1,\quad 0\le u,d_0\le1,\quad N+u\le\sqrt n.
\tag{2}
\]
For each vector \(g=z^{(j)},h^{(j)},k^{(j)},\delta^{(j)},w\), assume
the reference linear variation has the two bounds
\[
\|Dg(X_a^0)V_a\|_2\le N,\qquad
\|Dg(X_a^0)V_a\|_\infty\le d_0.
\tag{3}
\]
These are deterministic hypotheses about the Gaussian linear-response
event, not assertions of its probability. No localization hypothesis is
made for \(U_\Theta\). Define the two remainder scales
\[
R=d_0N+d_0u+u^2,\qquad
P=(N+u)^2/\sqrt n,
\qquad u+R+P\le1.
\tag{4}
\]
The last restriction will be used only to control the carrier along the
joining segment for the scalar residual Taylor estimate. The forward and
gradient remainder estimates below do not require it.

## 2. Uniform physical and first-derivative bounds

Every point \(X_a^0+t\eta_a\), \(0\le t\le1\), has normalized
first-weight operator norm at most eleven, hidden operator norms at most
eleven, and each port norm at most \(\sqrt n\). The feature RMS
recurrence is bounded by
\(H_j\le2\beta+11\beta H_{j-1}\), with \(H_0=1\). Thus
\[
\max_j\|h_a^{(j)}\|_2/\sqrt n\le(13\beta)^L\le\beta^{3L}.
\]
Also \(\|w\|_2/\sqrt n\le\beta^{4L}\), so backward propagation
gives carrier RMS at most \(\beta^{7L}\) and response RMS at most
\(\beta^{8L}\). These estimates use no coordinate cutoff.

The forward derivative recurrence is
\[
Dz^{(1)}[U]=U_Av+U_{e^{(1)}},
\]
\[
Dz^{(j)}[U]=U_{H^{(j)}}h^{(j-1)}/\sqrt n
 +W^{(j)}\operatorname{diag}(\phi'_{j-1})Dz^{(j-1)}[U]
 +U_{e^{(j)}}.
\]
Summing the geometric recursion gives, throughout the segment,
\[
\max_j\{\|Dz^{(j)}\|_{\rm op},\|Dh^{(j)}\|_{\rm op}\}
\le J:=\beta^{10L},\qquad
\|DF_a\|_2\le\beta^{13L}\sqrt n.
\tag{5}
\]
For example, the preactivation derivative sum is at most
\(2L\beta^{3L}(11\beta)^{L-1}\le\beta^{7L}\), before the final
activation slope. The gradient bound follows from the blocks
\[
\nabla_A F_a=\delta_a^{(1)}v_a^\top,\quad
\nabla_{H^{(j)}}F_a=\delta_a^{(j)}h_a^{(j-1)\top}/\sqrt n,\quad
\nabla_wF_a=h_a^{(L)},\quad D_{e^{(j)}}F_a=\delta_a^{(j)}.
\tag{6}
\]

At the reference, differentiating the backward recursion gives
\[
D\delta^{(j)}[U]
=\phi'_j\odot Dk^{(j)}[U]
 +\phi''_j\odot Dz^{(j)}[U]\odot k^{(j),0},
\]
\[
Dk^{(j)}[U]
=W^{(j+1),0\top}D\delta^{(j+1)}[U]
 +U_{H^{(j+1)}}^\top\delta^{(j+1),0}/\sqrt n.
\]
There is a single reference carrier in each forcing term. The geometric
sum, using (5) and the response RMS, gives
\[
\max_j\{\|Dk^{(j)}(X_a^0)\|_{\rm op},
           \|D\delta^{(j)}(X_a^0)\|_{\rm op}\}
\le J_b:=\beta^{20L}(1+M).
\tag{7}
\]
In particular a derivative evaluated on \(U_a\) has norm at most
\(Ju\) in a forward vector and \(J_bu\) in a backward vector.

## 3. Exact forward and backward Taylor remainders

For any vector-valued network quantity \(g\), use
\[
g_1=g(X_a^0+\eta_a),\quad g_0=g(X_a^0),\quad
g_{[1]}=Dg(X_a^0)\eta_a,\quad
E_g=g_1-g_0-g_{[1]}.
\]
The notation \(g_{[1]}\) denotes the first variation, not layer one.
For a forward preactivation,
\[
\|(z_{[1]})^{\odot2}\|_2
\le d_0N+2d_0Ju+J^2u^2\le3J^2R.
\tag{8}
\]
Both mixed terms use the coordinate bound on the \(V_a\) variation;
there is no term \(Nu\) without a small coordinate or width factor.

At layers \(j\ge2\), exact subtraction gives
\[
E_{z^{(j)}}=W_1^{(j)}E_{h^{(j-1)}}
 +\Delta H^{(j)}h^{(j-1)}_{[1]}/\sqrt n,
\qquad E_{z^{(1)}}=0.
\tag{9}
\]
To estimate an activation remainder, compare first at
\(z_0+z_{[1]}\):
\[
E_h=\phi(z_0+z_{[1]}+E_z)-\phi(z_0+z_{[1]})
 +\phi(z_0+z_{[1]})-\phi(z_0)-\phi'(z_0)z_{[1]}.
\]
Consequently \(\|E_h\|_2\le\beta\|E_z\|_2+
\frac\beta2\|(z_{[1]})^{\odot2}\|_2\). The matrix cross term in
(9) has norm at most \(JP\). Propagating by the bounded *perturbed*
mixers in (9) therefore yields
\[
\max_j(\|E_{z^{(j)}}\|_2,\|E_{h^{(j)}}\|_2)
\le A_f(R+P),\qquad A_f=\beta^{30L}.
\tag{10}
\]
The forcing coefficient before the geometric sum is at most
\(2\beta J^2\), and the propagation sum is at most
\(L(11\beta)^{L-1}\le\beta^{4L}\), which verifies this envelope.

The corresponding exact backward identities are
\[
E_{k^{(L)}}=0,\qquad
E_{k^{(j)}}=W_1^{(j+1)\top}E_{\delta^{(j+1)}}
 +\Delta H^{(j+1)\top}\delta^{(j+1)}_{[1]}/\sqrt n,
\tag{11}
\]
and, with \(g_i=\phi'(z_i)\),
\[
E_\delta
=g_1\odot E_k+(g_1-g_0)\odot k_{[1]}
 +k_0\odot[g_1-g_0-\phi''(z_0)z_{[1]}].
\tag{12}
\]
The first term propagates with slope at most \(\beta\); its coefficient
does not contain \(M\). For the second term use
\[
\|z_{[1]}\odot k_{[1]}\|_2
\le d_0N+d_0(J+J_b)u+JJ_bu^2\le3JJ_bR,
\]
\[
\|E_z\odot k_{[1]}\|_2
\le A_f(R+P)(d_0+J_bu)\le2A_fJ_b(R+P).
\]
For the last term, insert \(z_0+z_{[1]}\) as above and use bounded
second and third activation derivatives. Its norm is at most
\[
M\left[\beta\|E_z\|_2+
        \frac{\beta^2}{2}\|(z_{[1]})^{\odot2}\|_2\right].
\]
The cross term in (11) is at most \(J_bP\). Thus all additive
backward forcing terms have coefficient at most
\(\beta^{53L}(1+M)\), and their geometric propagation gives
\[
\max_j(\|E_{k^{(j)}}\|_2,\|E_{\delta^{(j)}}\|_2)
\le\beta^{60L}(1+M)(R+P).
\tag{13}
\]
This is where a repeated multiplication by the carrier cutoff is avoided:
the only homogeneous propagation in (11)–(12) uses bounded perturbed
mixers and slopes. The reference-carrier multiplier is always in an
additive forcing term.

For a hidden gradient block, exact product subtraction gives
\[
E_{\delta h^\top/\sqrt n}
=\frac1{\sqrt n}
 [E_\delta h_1^\top+\delta_{[1]}(h_1-h_0)^\top
                         +\delta_0E_h^\top].
\tag{14}
\]
Use feature and response RMS for the first and last terms. The middle
term is at most \(JJ_bP\), because
\(\|h_1-h_0\|_2\le J(N+u)\). Including the first and readout blocks
and the at most \(L+1\) blocks yields the explicit gradient lemma
\[
\|\nabla_\Theta F_a(X_a^0+\eta_a)-\nabla_\Theta F_a(X_a^0)
             -D\nabla_\Theta F_a(X_a^0)\eta_a\|_2
\le\beta^{70L}(1+M)(R+P).
\tag{15}
\]
The order is quadratic in the perturbation; only derivatives through order
three occur. Neither the activation values nor a derivative order growing
with depth enters the coordinate-cutoff power.

## 4. Scalar residual and its contribution to the vector field

Apply (13) to \(t\eta_a=tV_a+tU_a\). Its remainder scales do not
exceed \(R,P\), and its backward first variation has coordinate bound
at most \(d_0+J_bu\). Condition (4) implies the segment carrier bound
\[
\max_{a,j,t}\|k_a^{(j)}(X_a^0+t\eta_a)\|_\infty
\le\beta^{62L}(1+M).
\tag{16}
\]
The augmented Hessian identity consists of two readout cross terms,
two mixed weight terms per hidden layer, and curvature terms
\[
Dz^{(j)\top}\operatorname{diag}(k^{(j)}\odot\phi_j'')Dz^{(j)}.
\]
Mixed weight terms retain \(1/\sqrt n\) and use response RMS. Bounds
(5) and the physical RMS estimates give, at carrier maximum \(M'\),
\(\|D^2F_a\|_{\rm op}\le\beta^{24L}(1+M')\). Substituting (16)
therefore proves on the entire segment
\[
\|D^2F_a\|_{\rm op}\le\beta^{87L}(1+M).
\tag{17}
\]
No segment coordinate bound was silently assumed.

Let \(r_a=F_a/n-y_a\), \(g_a=\nabla_\Theta F_a\), and
\(\rho_0=(m^{-1}\sum_a|r_a^0|^2)^{1/2}\). Integration of (5), (17)
gives
\[
|r_a^1-r_a^0|\le\beta^{13L}(N+u)/\sqrt n,
\]
\[
|r_a^1-r_a^0-Dr_a^0\eta_a|
\le\tfrac12\beta^{87L}(1+M)(N+u)^2/n,
\qquad
\|g_a^1-g_a^0\|_2\le\beta^{87L}(1+M)(N+u).
\tag{18}
\]
The exact product remainder is
\[
r_a^1g_a^1-r_a^0g_a^0-r_a^0Dg_a^0\eta_a
 -(Dr_a^0\eta_a)g_a^0
=r_a^0E_{g_a}+
 (r_a^1-r_a^0-Dr_a^0\eta_a)g_a^0
 +(r_a^1-r_a^0)(g_a^1-g_a^0).
\]
Since \(\|g_a^0\|_2\le\beta^{13L}\sqrt n\), the last two terms
cost at most \(2\beta^{100L}(1+M)P\). Averaging the first term uses
\(m^{-1}\sum_a|r_a^0|\le\rho_0\). Thus the original forward-residual
gradient flow has remainder bounded by
\[
\beta^{110L}(1+M)[\rho_0R+(1+\rho_0)P].
\tag{19}
\]
The residual has not been frozen or treated as an external control.

## 5. The original reverse deletion force

Delete \(r_{\rm del}\) neurons at an interior layer \(j\). With omitted
initialized incoming rows \(y_i\), the prescribed reverse source is
\(q_a=\sum_i y_i b_{a,i}\). Suppose
\[
\|y_i\|_2\le2,\qquad |b_{a,i}|\le\beta M,
\]
and every reference lower adjoint carrier obtained by backpropagating
\(y_i\) through \(h_a^{(j-1)}\) has coordinate norm at most \(d_0\).
These again are deterministic event hypotheses. For the aggregate probe
\(q_a\), its norm is at most \(Q=2r_{\rm del}\beta M\), and its
reference probe-carrier maximum is at most
\(p=r_{\rm del}\beta Md_0\).

For a fixed probe \(q\), write
\(\psi_q(\Theta)=q^\top h^{(j-1)}(\Theta)\). Along the parameter
segment, subtract its adjoint recursions by multiplying each changed gate
by the *reference* probe, and propagate the probe difference through the
perturbed bounded maps. Forward changes have norm at most \(J(N+u)\),
and a changed mixer has norm at most \((N+u)/\sqrt n\). Therefore
\[
\max_\ell\|k_{q,t}^{(\ell)}-k_{q,0}^{(\ell)}\|_2
\le\beta^{20L}(p+Q/\sqrt n)(N+u).
\tag{20}
\]
The probe itself has Euclidean norm at most \((11\beta)^LQ\).
The scalar lower-network Hessian has curvature terms weighted by its
probe carriers and mixed terms with \(1/\sqrt n\). Hence
\[
\sup_t\|D^2\psi_q(\Theta^0+t\Delta\Theta)\|_{\rm op}
\le\beta^{50L}
 [p(1+N+u)+Q(1+N+u)/\sqrt n].
\]
Integrating this Hessian gives
\[
\|(Dh_1^{(j-1)}-Dh_0^{(j-1)})^\top q\|_2
\le\beta^{50L}
 [p(N+u+(N+u)^2)+Q(N+u+(N+u)^2)/\sqrt n].
\tag{21}
\]

The exact retained vector field, with its original residual, is
\[
\mathcal V(\Theta,e,q)
=-\frac2m\sum_a r_a(\Theta,e)
 [\nabla_\Theta F_a(\Theta,e)
               +Dh_a^{(j-1)}(\Theta)^\top q_a].
\tag{22}
\]
At zero sources the linear reverse term is
\(-2m^{-1}\sum_a r_a^0Dh_a^{(j-1),0\top}q_a\). Subtracting it
leaves the two exact terms
\[
-\frac2m\sum_a
 \left[r_a^0(Dh_a^1-Dh_a^0)^\top q_a
              +(r_a^1-r_a^0)Dh_a^{1\top}q_a\right].
\]
The first uses (21); the second uses (18) and
\(\|Dh_a^{1\top}q_a\|_2\le JQ\). Since \(N+u\ge1\), the result
combines with (19) to give
\[
\begin{aligned}
&\|\mathcal V(\Theta^0+\Delta\Theta,e,q)-\mathcal V(\Theta^0,0,0)
 -D_\Theta\mathcal V_0\Delta\Theta-D_e\mathcal V_0e-D_q\mathcal V_0q\|_2\\
&\quad\le\beta^{120L}(1+r_{\rm del})(1+M)
 \left[\rho_0\{R+d_0(N^2+Nu+u^2)\}+(1+\rho_0)P\right].
\end{aligned}
\tag{23}
\]
Here the derivatives are evaluated at \((\Theta^0,0,0)\), and
\(D_e\) includes the sample-dependent forward ports. In particular,
for the port at layer \(j+1\), it contains both original contributions
\(-2m^{-1}r_a^0(D_\Theta\delta_a^{(j+1)})^\top e_a\) and
\(-2(mn)^{-1}g_a^0\delta_a^{(j+1),0\top}e_a\). The latter is the
adaptive-residual term. At the first layer the reverse source is absent.

With the inherited choices \(N=n^{1/100}\), \(d_0=n^{-1/10}\), and
\(u\le n^{-1/25}\), the braces in (23) have exactly the width powers
\[
n^{-8/100}+n^{-9/100}u+n^{-1/10}u^2
 +n^{-9/100}+n^{-1/10}u+u^2.
\]
Thus (23) replaces the local \((1+M)^{C_L}\) coefficient with
\(\beta^{120L}(1+r_{\rm del})(1+M)\), retaining the useful small
coordinate factors. A generic Euclidean Taylor bound proportional to
\(N^2\) would not yield this conclusion.

## 6. Learned directions and the top residual offset

Suppose the actual deleted controls obey the joint stop
\(|z_{a,i}|,|k_{a,i}|\le M\), so
\(|a_{a,i}|\le\beta(1+M)\) and \(|b_{a,i}|\le\beta M\).
Assume the source physical activity and response RMS bounds
\(\int2\rho\,dt\le S\le1\) and
\(\|\delta_a^{(\ell)}\|_2/\sqrt n\le S\beta^{8L}\).
Integrating the original column and row updates gives
\[
\|W^{(j+1)}_{:,i}(t)-x_i\|_2
\le S^2\beta^{9L}(1+M)/\sqrt n,
\]
\[
\|W^{(j)\top}_{i,:}(t)-y_i\|_2
\le S\beta^{4L}M/\sqrt n.
\]
Multiplying by their actual controls and summing shows that the forward
and reverse source corrections \(\zeta_a,\chi_a\) satisfy
\[
\max_a(\|\zeta_a\|_2+\|\chi_a\|_2)
\le\beta^{11L}(1+r_{\rm del})(1+M)^2/\sqrt n.
\tag{24}
\]
They can be adaptive; the estimates apply to an existing actual path.
On a local port-interpolation segment satisfying the same physical bounds
and carrier envelope (16), differentiation of (22) with respect to its
ports shows that their additional vector-field force is at most
\[
\beta^{130L}(1+r_{\rm del})^2(1+M)^3
                         (1+\rho)/\sqrt n.
\tag{25}
\]
Indeed the forward port derivative has a Hessian factor bounded by (17),
the scalar residual derivative costs \(\beta^{8L}/\sqrt n\), and the
reverse port derivative is \(-2r_aDh_a^\top/m\). Thus at most one
additional cutoff factor multiplies (24). The segment condition in this
statement is explicit; for small port corrections it can be checked by
the same forward/backward estimates above. It is not an assertion about
an arbitrary large adaptive feedback perturbation.

For top-layer deletion the prediction offset is
\(d_a=n^{-1}\sum_{i\in I}w_i h_{a,i}^{(L)}\). It multiplies both
the retained gradient and the reverse force:
\[
\dot\Theta=-\frac2m\sum_a(r_a^0+d_a)
 [\nabla_\Theta F_a^{\rm ret}+Dh_a^{(L-1)\top}q_a].
\]
The joint cap gives \(|d_a|\le r_{\rm del}\beta(1+M)^2/n\).
If each current deleted row norm is at most three, then
\(\|q_a\|_2\le3r_{\rm del}\beta M\). Equations (5)–(6) bound the
entire offset force by
\[
\beta^{16L}(1+r_{\rm del})^2(1+M)^3/\sqrt n.
\tag{26}
\]
The current-row bound follows, for example, from initial row norm at most
two and the displayed row increment at most one. The reverse-offset term
has been included explicitly.

## 7. Complex applicability and remaining obligations

The proved real lemma uses only additions, products, transposes, Taylor
integrals, and Euclidean norm inequalities. Its algebra also applies to
complex vectors and the holomorphic continuation of the algebraic
transpose gradient. It does not use complex positivity or a gradient
energy inequality.

For a complex application, one must additionally keep all actual and
auxiliary scalar Taylor segments inside a derivative strip. One sufficient
local condition, for reference preactivation imaginary parts at most
\(7a/16\), is
\[
d_0+\beta^{10L}u+\beta^{30L}(R+P)\le a/32.
\tag{27}
\]
On a first-exit prefix the forward estimates place every joining-segment
preactivation and every auxiliary point \(z_0+z_{[1]}\) within
\(15a/32<a/2\); continuity therefore closes this local strip condition.
Cauchy's formula at distance \(a/64\) from those points bounds the
third derivative by \(64\beta/a\le4\beta^2\). Replacing \(\beta\)
by \(\beta^2\) in all displayed envelopes is a conservative way to
cover these constants. Thus the complex conditional version of (23) has
coefficient \(\beta^{240L}(1+r_{\rm del})(1+M)\). No entire complex
trajectory or source event is inferred from this local statement.

What remains outside this derivation is quantitative production of the
linear coordinate event (3), its uniformity over the original control
class, explicit control-net and Gaussian-form probabilities, propagator
constants, common-cavity projection errors, the finite moment-degree
dependence, and the joint-budget removal remainder. This note supplies a
fixed-order local estimate usable in such a program. It does not turn the
inherited asymptotic source interface into a finite-confidence theorem.

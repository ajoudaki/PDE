# Amplitude-scaled local insertion remainder without inverse activity

2026-10-07. Bounded author corollary. This concerns a deterministic local
Taylor estimate conditional on specified localized linear variations. It
does not prove a probability estimate, budget removal, or a decoder theorem.

The full local remainder proof transfers to the amplitude coordinates with
unscaled forward ports. Its coefficient remains
\(\beta^{120L}(1+r_{\rm del})(1+M)\), where \(M\) bounds the
*scaled* reference carriers. Learned-direction and top-offset corrections
have cutoff degree at most three. No coefficient or local size condition
introduced by the transfer contains \(S^{-1}\).

## 1. Inputs and exact scaled architecture

The main input is the complete frozen local lemma
`FIXED_ORDER_INSERTION_JETS.md`, SHA-256
`dcc9dad21a3141e5c2e2a1f4e81eb1cea43f14a7d552f680f137b0d71cc82f7f`.
The only additional current-study mathematical input is §6 of
`QUANTITATIVE_INSERTION_WIDTH.md`; its file hash at the read was
`40fc026d7e0d18b968ae1526a94792290dc25cd56f97972db526dfd3e8aeb31b`.
That section supplies the exact scaled flow, not a probability premise.
The previously assigned original sources and required mathematical skills
remain the scope of the parent derivation. No other derivations were used.

Fix \(0<S\le1\). Retain the original mobility coordinates
\[
\Theta=(A,H^{(2)},\ldots,H^{(L)},w),\qquad H^{(j)}=\sqrt nW^{(j)},
\]
and the original initialized parameter \(\Theta_0\), whose readout is
zero. Define
\[
\bar u=(\Theta-\Theta_0)/S,
\qquad \bar F_a(\bar u,e)=F_a(\Theta_0+S\bar u,e)/S,
\qquad \bar r_a=\bar F_a/n-y_a/S,
\qquad \bar q_a=q_a/S.
\tag{1}
\]
The forward ports \(e_a^{(j)}\) are unscaled. In particular the actual
architecture, including its readout, is
\[
\begin{aligned}
z_a^{(1)}&=(A_0+S\bar u_A)v_a+e_a^{(1)},\\
z_a^{(j)}&=(H_0^{(j)}+S\bar u_{H^{(j)}})
                       h_a^{(j-1)}/\sqrt n+e_a^{(j)},\\
h_a^{(j)}&=\phi_j(z_a^{(j)}),\qquad
\bar F_a=\bar u_w^\top h_a^{(L)}.
\end{aligned}
\tag{2}
\]
The last identity uses the zero initialized readout. It is essential to
the uniform bound; an arbitrary fixed nonzero initial readout divided by
\(S\) would require separate control.

Define scaled carriers by the actual recursion
\[
\bar k_a^{(L)}=\bar u_w,\qquad
\bar\delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot\bar k_a^{(j)},\qquad
\bar k_a^{(j)}=W^{(j+1)\top}\bar\delta_a^{(j+1)}.
\tag{3}
\]
Then \(k=S\bar k\), \(\delta=S\bar\delta\), and the gradient
blocks are
\[
\nabla_{\bar u_A}\bar F_a=S\bar\delta_a^{(1)}v_a^\top,
\quad
\nabla_{\bar u_{H^{(j)}}}\bar F_a
 =S\bar\delta_a^{(j)}h_a^{(j-1)\top}/\sqrt n,
\quad
\nabla_{\bar u_w}\bar F_a=h_a^{(L)}.
\tag{4}
\]
Also \(D_{\bar u}h=S D_\Theta h\), while
\(\nabla_{\bar u}\bar F=\nabla_\Theta F\). Substituting
\(r=S\bar r\), \(q=S\bar q\) and \(\dot\Theta=S\dot{\bar u}\)
in the original retained flow therefore gives exactly
\[
\dot{\bar u}=\overline{\mathcal V}(\bar u,e,\bar q)
=-\frac2m\sum_a\bar r_a
 [\nabla_{\bar u}\bar F_a+D_{\bar u}h_a^{(j-1)\top}\bar q_a].
\tag{5}
\]
The residual is the forward residual in (1). No scalar reverse-source
term is added to it.

## 2. Exact contraction underlying the transfer

Introduce a proof-only effective parameter
\[
\widetilde\Theta
=(A_0+S\bar u_A,H_0^{(2)}+S\bar u_{H^{(2)}},\ldots,
 H_0^{(L)}+S\bar u_{H^{(L)}},\bar u_w).
\]
Its hidden arrays are the actual arrays, and its readout is the scaled
readout. Let \(T_S\) be the block diagonal map multiplying every hidden
parameter block by \(S\), and the readout block by one. The augmented
map \(\widehat T_S\) also acts as identity on all forward ports. Both
have Euclidean operator norm one. Affine offsets have no derivatives.

Let \(F^{\rm eff}(\widetilde\Theta,e)\) be the ordinary unnormalized
network output with these effective parameters. Formula (2) gives
\[
\bar F=F^{\rm eff}(\widetilde\Theta,e),\quad
\nabla_{\bar u}\bar F=T_S^\top\nabla_{\widetilde\Theta}F^{\rm eff},
\quad
D_{\bar u}h^\top\bar q=T_S^\top D_{\widetilde\Theta}h^\top\bar q.
\tag{6}
\]
Consequently the entire vector field is the exact pullback
\[
\overline{\mathcal V}
=T_S^\top\mathcal V^{\rm eff}(\widetilde\Theta,e,\bar q),
\tag{7}
\]
where \(\mathcal V^{\rm eff}\) has precisely the retained-field form
in the frozen lemma, with labels \(y/S\). In a first-order Taylor
subtraction, its parameter increment is \(T_S\Delta\bar u\), and its
forward and reverse increments are \(e,\bar q\). The residual remainder
vector is also multiplied by \(T_S^\top\). None of these operations
enlarges a norm.

This observation does not require the effective system to be the trained
physical trajectory of another network. The frozen lemma is a pointwise
statement about the forward map and retained vector field at a local
reference and perturbation.

## 3. Local hypotheses and forward/backward remainder audit

At the scaled reference \(\bar u^0\), assume the physical hidden
operator bounds ten from the frozen lemma and
\[
\|\bar u_w^0\|_2/\sqrt n\le\beta^{3L},\qquad
\max_{a,j}\|\bar k_a^{(j),0}\|_\infty\le M.
\tag{8}
\]
Use an augmented displacement
\(\eta_a=V_a+U_a\), with \(V_a=(V_{\bar u},e_a)\),
\(U_a=(U_{\bar u},0)\). Impose exactly the frozen lemma's numerical
conditions
\[
\|V_a\|\le N,\quad \|U_a\|\le u,\quad N\ge1,\quad
0\le u,d_0\le1,\quad N+u\le\sqrt n,
\]
\[
R=d_0N+d_0u+u^2,\quad P=(N+u)^2/\sqrt n,
\qquad u+R+P\le1.
\tag{9}
\]
For every \(z^{(j)},h^{(j)},\bar k^{(j)},\bar\delta^{(j)},\bar u_w\),
assume its reference first variation on \(V_a\) has Euclidean norm at
most \(N\) and coordinate maximum at most \(d_0\). These are the
localized *scaled* variations. Equation (6) identifies them exactly with
the effective-network variations on \(\widehat T_S V_a\); their
unlocalized error directions also have norm at most \(u\).

The forward differential illustrates why unscaled ports cause no inverse
factor:
\[
Dz^{(1)}[U]=S U_Av+U_{e^{(1)}},
\]
\[
Dz^{(j)}[U]=S U_{H^{(j)}}h^{(j-1)}/\sqrt n
 +W^{(j)}\operatorname{diag}(\phi'_{j-1})Dz^{(j-1)}[U]
 +U_{e^{(j)}}.
\tag{10}
\]
The fixed port derivative has coefficient one, and each direct hidden
variation has coefficient \(S\le1\). The feature RMS and first-derivative
recurrences therefore have exactly the frozen upper bounds.

For a quantity \(g\), put \(g_{[1]}=Dg_0\eta\) and
\(E_g=g_1-g_0-g_{[1]}\). Exact forward subtraction is now
\[
E_{z^{(j)}}=W_1^{(j)}E_{h^{(j-1)}}
 +S\Delta\bar u_{H^{(j)}}h_{[1]}^{(j-1)}/\sqrt n.
\tag{11}
\]
The scalar activation Taylor remainder and the product estimate
\(\|(z_{[1]})^{\odot2}\|_2\le3\beta^{20L}R\) are unchanged.
Thus the forward remainder is at most \(\beta^{30L}(R+P)\).

The scaled backward differential and remainders are
\[
D\bar k^{(L)}[U]=U_w,
\]
\[
D\bar k^{(j)}[U]
=W^{(j+1)\top}D\bar\delta^{(j+1)}[U]
 +S U_{H^{(j+1)}}^\top\bar\delta^{(j+1)}/\sqrt n,
\]
\[
D\bar\delta^{(j)}[U]
=\phi_j'\odot D\bar k^{(j)}[U]
 +\phi_j''\odot Dz^{(j)}[U]\odot\bar k^{(j)},
\tag{12}
\]
\[
E_{\bar k^{(j)}}=W_1^{(j+1)\top}E_{\bar\delta^{(j+1)}}
 +S\Delta\bar u_{H^{(j+1)}}^\top
                         \bar\delta_{[1]}^{(j+1)}/\sqrt n.
\tag{13}
\]
Writing \(g_i=\phi'(z_i)\), the gate identity is exactly
\[
E_{\bar\delta}
=g_1\odot E_{\bar k}+(g_1-g_0)\odot\bar k_{[1]}
 +\bar k_0\odot[g_1-g_0-\phi''(z_0)z_{[1]}].
\tag{14}
\]
The carrier in the last term is \(\bar k_0\), bounded by \(M\).
There is no physical carrier divided by \(S\) left to estimate. The
mixed linear/remainder products use the same localized coordinate bounds;
the matrix cross term in (13) is decreased by \(S\). Accordingly the
backward remainder remains at most
\(\beta^{60L}(1+M)(R+P)\).

For a hidden gradient block, (4) multiplies the entire exact product
remainder by \(S\):
\[
E_{\nabla_{\bar u_H}\bar F}
=\frac S{\sqrt n}
 [E_{\bar\delta}h_1^\top
  +\bar\delta_{[1]}(h_1-h_0)^\top+\bar\delta_0E_h^\top].
\tag{15}
\]
The first-layer block similarly has factor \(S\); the readout block is
the unchanged \(E_{h^{(L)}}\). This verifies, block by block,
\[
\|\nabla_{\bar u}\bar F_1-\nabla_{\bar u}\bar F_0
 -D\nabla_{\bar u}\bar F_0\eta\|_2
\le\beta^{70L}(1+M)(R+P).
\tag{16}
\]

## 4. Mixed derivatives, reverse force, and adaptive residual

There is also an exact mixed-Hessian check. In the coordinate groups
hidden parameters, scaled readout, and unscaled ports, the pullback factors
relative to the effective canonical Hessian are respectively
\[
\begin{array}{c|ccc}
 &\text{hidden}&\text{readout}&\text{port}\\ \hline
\text{hidden}&S^2&S&S\\
\text{readout}&S&0&1\\
\text{port}&S&1&1
\end{array}
\]
The zero entry records linearity in the readout. In particular the
port–port Hessian is an ordinary scaled-carrier curvature term, not a
quantity divided by \(S\). Third mixed derivatives likewise acquire
one factor \(S\) per hidden-coordinate argument and no negative power.
These statements follow by differentiating the affine map in (6), whose
second and higher derivatives vanish.

The segment-carrier proof using (13)–(14) is unchanged, so the augmented
Hessian and gradient satisfy
\[
\sup_{0\le t\le1}\|D^2\bar F(\bar X^0+t\eta)\|_{\rm op}
\le\beta^{87L}(1+M),\qquad
\sup_t\|D\bar F(\bar X^0+t\eta)\|_2
\le\beta^{13L}\sqrt n.
\tag{17}
\]
Consequently
\[
|\Delta\bar r|\le\beta^{13L}(N+u)/\sqrt n,
\quad
|\Delta\bar r-D\bar r_0\eta|
\le\tfrac12\beta^{87L}(1+M)(N+u)^2/n.
\tag{18}
\]
The constant label \(y/S\) cancels from both differences. Multiplying
the second remainder by the reference gradient, and the first residual
difference by the gradient difference, costs
\(\beta^{CL}(1+M)P\) exactly as before. The undifferentiated reference
residual enters only through
\(\bar\rho_0=(m^{-1}\sum_a|\bar r_a^0|^2)^{1/2}\).

For the original reverse source write
\(\bar q_a=\sum_i y_i\bar b_{a,i}\), with
\(|\bar b_{a,i}|\le\beta M\), \(\|y_i\|_2\le2\), and the same
reference raw lower adjoint-probe coordinate bound \(d_0\). The probe
recursion depends only on the actual hidden weights and activations.
Changing \(\bar u\) changes a hidden matrix by
\(S\Delta\bar u_H/\sqrt n\), so the subtraction argument for probe
carriers only improves. More exactly, for
\(\psi_{\bar q}=\bar q^\top h^{(j-1)}\),
\[
D_{\bar u}\psi_{\bar q}=T_S^\top D_{\widetilde\Theta}\psi_{\bar q},
\qquad
D_{\bar u}^2\psi_{\bar q}
=T_S^\top D_{\widetilde\Theta}^2\psi_{\bar q}T_S.
\]
There is no readout dependence in this lower feature. Both derivatives
are norm contractions of the quantities already bounded in the frozen
reverse-probe proof.

The nonlinear reverse force after subtracting its first-order source is
the sum of
\[
\bar r_a^0(D_{\bar u}h_a^1-D_{\bar u}h_a^0)^\top\bar q_a,
\qquad
(\bar r_a^1-\bar r_a^0)D_{\bar u}h_a^{1\top}\bar q_a.
\]
The first uses the probe Hessian; the second uses (18). The direct
forward-source derivative also retains both exact terms
\[
-\frac2m\bar r_a^0(D_{\bar u}\bar\delta_a^{(j+1)})^\top e_a,
\qquad
-\frac2{mn}\nabla_{\bar u}\bar F_a^0
                     \bar\delta_a^{(j+1),0\top}e_a.
\tag{19}
\]
The second term is the adaptive-residual contribution. Thus no forward,
reverse, mixed, or residual term has been lost in the scaling.

Combining these estimates, or taking the norm contraction of the exact
Taylor remainder identity (7), gives
\[
\begin{aligned}
&\|\overline{\mathcal V}(\bar u^0+\Delta\bar u,e,\bar q)
 -\overline{\mathcal V}(\bar u^0,0,0)
 -D_{\bar u}\overline{\mathcal V}_0\Delta\bar u
 -D_e\overline{\mathcal V}_0e-D_{\bar q}\overline{\mathcal V}_0\bar q\|_2\\
&\quad\le\beta^{120L}(1+r_{\rm del})(1+M)
 \left[\bar\rho_0\{R+d_0(N^2+Nu+u^2)\}
                           +(1+\bar\rho_0)P\right].
\end{aligned}
\tag{20}
\]
All derivatives in the subtraction are evaluated at the reference with
zero ports. No inverse \(S\) appears in this bound or its local
hypotheses. On the source contours, the separate bounds
\(2\int\bar\rho\,|dt|\le1\), \(\bar\rho\le\lambda/8\) can be
inserted without introducing one.

## 5. Learned source corrections and the top offset

The amplitude factors should also be retained before estimating learned
directions. From (4)–(5), a physical hidden mixer obeys
\[
\dot W^{(j)}
=-\frac{2S^2}{mn}\sum_a\bar r_a
                  \bar\delta_a^{(j)}h_a^{(j-1)\top}.
\tag{21}
\]
Suppose \(2\int\bar\rho\,|dt|\le1\), the scaled response RMS is
at most \(\beta^{8L}\), and the actual deleted coordinates obey
\(|z_{a,i}|,|\bar k_{a,i}|\le M\). Then their controls obey
\(|a_{a,i}|\le\beta(1+M)\), \(|\bar b_{a,i}|\le\beta M\).
Integrating (21) gives
\[
\|W^{(j+1)}_{:,i}-x_i\|_2
\le S^2\beta^{9L}(1+M)/\sqrt n,
\qquad
\|W^{(j)\top}_{i,:}-y_i\|_2
\le S^2\beta^{4L}M/\sqrt n.
\]
The actual reverse source is
\(q_a=S\sum_iW^{(j)\top}_{i,:}\bar b_{a,i}\). Therefore
\(\bar q_a=\sum_iW^{(j)\top}_{i,:}\bar b_{a,i}\) directly, and its
learned-row remainder retains \(S^2\). Both source corrections satisfy
\[
\max_a(\|\zeta_a\|_2+\|\bar\chi_a\|_2)
\le S^2\beta^{11L}(1+r_{\rm del})(1+M)^2/\sqrt n.
\tag{22}
\]
Under the same explicit local port-interpolation conditions as the frozen
lemma, their additional scaled vector-field force is consequently at most
\[
S^2\beta^{130L}(1+r_{\rm del})^2(1+M)^3
                                      (1+\bar\rho)/\sqrt n.
\tag{23}
\]
This also verifies the adaptive learned-source terms rather than dividing
an unscaled error estimate by \(S\).

At the top layer, the scaled prediction offset is exactly
\[
\bar d_a=\frac1n\sum_{i\in I}\bar u_{w,i}h_{a,i}^{(L)},
\qquad |\bar d_a|\le r_{\rm del}\beta(1+M)^2/n.
\]
It multiplies both retained terms:
\[
-\frac2m\sum_a\bar d_a
 [\nabla_{\bar u}\bar F_a^{\rm ret}
                 +D_{\bar u}h_a^{(L-1)\top}\bar q_a].
\]
With the same current deleted-row bound three as in the frozen lemma,
the whole offset force is at most
\(\beta^{16L}(1+r_{\rm del})^2(1+M)^3/\sqrt n\). The reverse-offset
product is included. This term has no inverse \(S\), although unlike
(23) it need not have an extra \(S^2\).

## 6. Exact conclusion and limits

For the complex local version, the real contraction \(T_S\) is also a
contraction in complex Euclidean norm. The frozen lemma's explicit strip
condition and auxiliary Taylor-point condition remain sufficient, with
the same conservative replacement of the coefficient by
\(\beta^{240L}\). The algebraic transpose gradient is continued
holomorphically; no complex energy inequality is invoked.

The result is uniform for \(0<S\le1\) under the stated scaled physical
bounds and localized scaled first-variation hypotheses. The quantity
\(y/S\) is the exact normalized label and occurs only through the actual
normalized residual. In the source convention \(S=16Y/\lambda\), its
sample RMS is \(Y/S=\lambda/16\). The local remainder constants and
smallness conditions do not impose a positive lower bound on \(S\).

This does not justify dividing a previously unscaled
\(O(n^{-1/30})\) coordinate estimate by \(S\) and declaring it uniform.
The scaled Gaussian linear event, its uniform control and time estimates,
the scaled nonlinear bootstrap, common-cavity comparison, and budget
removal must be proved in these coordinates. Equation (20) supplies the
nonlinear local remainder needed for that argument, conditional on its
localized inputs. No global probability conclusion is claimed.

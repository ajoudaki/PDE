# Compact first saturation and a linear-tail top activation: a finite RawGF clock theorem

This is a new finite-width result for the exact two-input RawGF below. Its only source is `COMPACT_GATE_CONFINEMENT_TEST.md` in this directory. No other mathematical files, experiments, external results from the project, or other agents were used. All estimates needed beyond the canonical equations and the frozen first rows are proved here.

**Conclusion.** The proposed strategy works. A positive frozen first-feature Gram and an actually achieved loss strictly below 2 imply a bounded weighted residual clock, bounded upper parameters, exponential optimization, and a finite total unweighted residual clock. Moreover, for every fixed input correlation in \((-1,1)\), the specified independent canonical Gaussian initialization achieves a fixed loss margin below 2 by a fixed time on an explicit event whose probability tends to one with width. The short-time argument uses the exact energy identity and an initial readout-feature Gram bound; it needs no upper-curvature estimate or maximum-readout-weight bound.

Both endpoint correlations are excluded here. In particular, nothing below treats the antiparallel case \(\rho=-1\). This is not a mean-field existence, convergence, uniqueness, or persistent-nonlinear-learning theorem.

## 1. Canonical model, ordinary norms, and the unchanged first rows

Fix \(d\ge2\), two inputs with
\[
 \|x_1\|_2^2=\|x_2\|_2^2=d,\qquad
 x_1^Tx_2/d=\rho\in(-1,1),\qquad y=(1,-1)^T.
\]
Both hidden widths equal the finite integer \(n\). Let \(p\) be an even, nonnegative \(C^\infty\) function, supported on \([-R,R]\), positive on \((-R,R)\), and define
\[
 \phi_1(z)=\int_0^z p(u)\,du,\qquad
 A=\int_0^R p(u)\,du>0,\qquad P=\|p\|_\infty.
 \tag{1}
\]
The top activation is fixed, with fixed \(\varepsilon>0\):
\[
 \phi_2(z)=z+\varepsilon\arctan z,\qquad M=1+\varepsilon.
 \tag{2}
\]
In particular,
\[
 |\phi_1|\le A,\qquad
 1\le\phi_2'(z)=1+\frac{\varepsilon}{1+z^2}\le M,
 \qquad |\phi_2(z)|\le M|z|.
 \tag{3}
\]
Use the canonical matrices and readout vector
\[
 W^1\in\mathbb R^{n\times d},\qquad W^2\in\mathbb R^{n\times n},
 \qquad W^3\in\mathbb R^n.
\]
For sample indices \(a=1,2\), set
\[
 z^1_a=W^1x_a,\quad h^1_a=\phi_1(z^1_a),\quad
 z^2_a=W^2h^1_a,\quad h^2_a=\phi_2(z^2_a),\quad
 f_a=\frac1n(W^3)^Th^2_a,\quad r_a=f_a-y_a.
 \tag{4}
\]
Activations and their derivatives act coordinatewise. Write
\[
 \delta^2_a=W^3\odot\phi_2'(z^2_a),\qquad
 \delta^1_a=\phi_1'(z^1_a)\odot (W^2)^T\delta^2_a.
\]
The dynamics are exactly
\[
 \dot W^1=-\frac2d\sum_{a=1}^2r_a\delta^1_ax_a^T,\qquad
 \dot W^2=-\frac2n\sum_{a=1}^2r_a\delta^2_a(h^1_a)^T,\qquad
 \dot W^3=-2\sum_{a=1}^2r_ah^2_a.
 \tag{5}
\]
All vector norms below are ordinary Euclidean norms, all Frobenius norms are ordinary Frobenius norms, and all operator norms are induced Euclidean norms. Normalizing factors are written explicitly. In particular, define
\[
 H^k=(h^k_1,h^k_2)\in\mathbb R^{n\times2},\quad
 G_1=\frac1n(H^1)^TH^1,\quad L=\|r\|_2^2,\quad s=\sqrt L,
\]
\[
 A_0=W^2(0),\quad \|A_0\|_{\rm op}\le a_0,\quad
 B=W^2-A_0,\quad a=\|B\|_F,\quad
 b=\frac{\|W^3\|_2}{\sqrt n},\quad b_0=b(0),
 \quad X(t)=\int_0^t s(u)b(u)\,du.
 \tag{6}
\]
Here \(a_0\) bounds the initial operator norm, not its Frobenius norm; \(a(0)=0\). The letter \(a\) as a scalar function in (6) is distinct from a sample index under a sum.

A first row with both initial coordinates outside \((-R,R)\) is unchanged by (5). Indeed, fixing that entire row makes both factors \(\phi_1'(z^1_{ja})\) zero for all time, so its row equation is zero. The smooth finite-dimensional ODE has local uniqueness, making this the actual row evolution. Let \(N_s\) and \(N_o\) count respectively the initially saturated same-sign and opposite-sign rows. Their exact, unchanged Gram contribution is
\[
 G_F=\frac{A^2}{n}
 \begin{pmatrix}N_s+N_o&N_s-N_o\\N_s-N_o&N_s+N_o\end{pmatrix},
 \qquad G_1(t)\succeq G_F\succeq\gamma_n I_2,
 \quad \gamma_n=\frac{2A^2}{n}\min(N_s,N_o).
 \tag{7}
\]
The remaining rows contribute a positive semidefinite matrix. Thus one row of each sign type suffices for strict positivity. Until the probability calculation, assume a deterministic constant \(\gamma>0\) with \(\gamma_n\ge\gamma\). No other first row is held fixed.

## 2. Exact dissipation and global finite-time existence

With \(C_{ab}=x_a^Tx_b/d\), the residual equation is
\[
 \dot r=-2Kr,\qquad K=K_1+K_2+K_3,
 \tag{8}
\]
where
\[
 (K_1)_{ab}=\frac{C_{ab}}n(\delta^1_a)^T\delta^1_b,
 \quad (K_2)_{ab}=\frac{(h^1_a)^Th^1_b}{n^2}
                         (\delta^2_a)^T\delta^2_b,
 \quad K_3=\frac1n(H^2)^TH^2.
 \tag{9}
\]
Each is a Gram matrix: for example \(K_1\) is the Gram of
\(\delta^1_ax_a^T/\sqrt{nd}\) in Frobenius inner product. Hence all are positive semidefinite. Direct substitution of (5) gives both forms of the exact energy identity:
\[
\begin{split}
 -\dot L={}&4r^TKr\\
 ={}&\frac4n\left\|\sum_a r_ah^2_a\right\|_2^2
 +\frac4{n^2}\left\|\sum_a r_a\delta^2_a(h^1_a)^T\right\|_F^2
 +\frac4{nd}\left\|\sum_a r_a\delta^1_ax_a^T\right\|_F^2\\
 ={}&\frac{\|\dot W^3\|_2^2}{n}
       +\|\dot W^2\|_F^2
       +\frac d n\|\dot W^1\|_F^2.
\end{split}
 \tag{10}
\]
Consequently, on every interval of existence,
\[
 \|W^2(t)-A_0\|_F\le\sqrt{tL(0)},\quad
 \frac{\|W^3(t)-W^3(0)\|_2}{\sqrt n}\le\sqrt{tL(0)},\quad
 \sqrt{\frac d n}\|W^1(t)-W^1(0)\|_F\le\sqrt{tL(0)}.
 \tag{11}
\]
These follow by integrating each squared speed and applying Cauchy--Schwarz. They establish existence for all finite times, even without (7): the smooth vector field gives a unique local solution, while (11) prevents any finite-time parameter blow-up. More explicitly, on an interval with a finite right endpoint, the same speed estimate between two times gives a constant times the square root of their separation. All parameters therefore have finite limits at that endpoint, and local existence at the limiting state extends the solution.

For each second neuron, let
\[
 D_i=\operatorname{diag}\bigl(\phi_2'(z^2_{i1}),\phi_2'(z^2_{i2})\bigr).
\]
The exact second kernel is
\[
 K_2=\frac1n\sum_{i=1}^n(W^3_i)^2D_iG_1D_i
 \succeq\frac\gamma n\sum_i(W^3_i)^2D_i^2
 \succeq\gamma b^2 I_2.
 \tag{12}
\]
This uses congruence of positive semidefinite matrices, not an entrywise comparison. It proves
\[
 \dot L\le-4\gamma b^2 L,\qquad
 \dot s\le-2\gamma b^2s\quad\hbox{where }s>0.
 \tag{13}
\]
If the residual ever becomes zero, all three velocities vanish and it stays zero.

## 3. The exact centered balance and the weighted clock

Define the bounded homogeneity defect
\[
 D(z)=z\phi_2'(z)-\phi_2(z)
 =\varepsilon\left(\frac z{1+z^2}-\arctan z\right),\qquad
 D_*:=\|D\|_\infty=\frac{\varepsilon\pi}{2}.
 \tag{14}
\]
For verification, \(D(0)=0\), \(D'(z)=-2\varepsilon z^2/(1+z^2)^2\), and its limits at positive and negative infinity are \(-\varepsilon\pi/2\) and \(+\varepsilon\pi/2\).

Use the explicit constants
\[
 C_B=2\sqrt2 MA,\qquad C_f=\sqrt2 MA,\qquad
 C_D=4\sqrt2(D_*+Ma_0A).
 \tag{15}
\]
Since \(\|h^1_a\|_2\le A\sqrt n\), the second-layer velocity satisfies
\[
 \|\dot B\|_F
 \le\frac2n\sum_a|r_a|M\|W^3\|_2\|h^1_a\|_2
 \le C_Bsb.
\]
In particular,
\[
 a(t)\le C_BX(t).
 \tag{16}
\]
The two norm-square derivatives are
\[
 \frac d{dt}a^2=-\frac4n\sum_a r_a
   \left\langle W^3,\phi_2'(z^2_a)\odot Bh^1_a\right\rangle,
 \qquad
 \frac d{dt}b^2=-\frac4n\sum_a r_a\langle W^3,\phi_2(z^2_a)\rangle
              =-4\langle r,f\rangle.
\]
Using \(Bh^1_a=z^2_a-A_0h^1_a\), their difference is exactly
\[
 \frac d{dt}(a^2-b^2)
 =-\frac4n\sum_a r_a
 \left\langle W^3,
 D(z^2_a)-\phi_2'(z^2_a)\odot A_0h^1_a\right\rangle.
 \tag{17}
\]
There is no missing feature-transport derivative: (17) differentiates the two parameter norms, not the preactivation. It is valid for the actual moving \(H^1(t)\). In particular,
\[
 \left|\frac d{dt}(a^2-b^2)\right|
 \le C_Dsb,
 \qquad
 |a(t)^2-b(t)^2+b_0^2|\le C_DX(t).
 \tag{18}
\]
Thus
\[
 a^2\le b^2+C_DX,\qquad
 a\le b+\sqrt{C_DX},\qquad
 b^2\le a^2+b_0^2+C_DX.
 \tag{19}
\]
Centering at \(A_0\) is essential for the width-uniform estimate: the error uses \(\|A_0\|_{\rm op}\), whereas \(\|A_0\|_F\) is typically of order \(\sqrt n\).

The prediction bound is
\[
 \|f\|_2
 \le \frac{\|H^2\|_{\rm op}\|W^3\|_2}{n}
 \le C_f b\,\|W^2\|_{\rm op}
 \le C_f b(a_0+a)
 \le C_f b\bigl(a_0+b+\sqrt{C_DX}\bigr).
 \tag{20}
\]
Here \(\|H^2\|_F\le M\|W^2\|_{\rm op}\|H^1\|_F\) follows from (3), and \(\|H^1\|_F\le A\sqrt{2n}\).

## 4. Deterministic all-time optimization after an actual loss margin

**Theorem 1.** Assume \(\gamma_n\ge\gamma>0\), \(\|A_0\|_{\rm op}\le a_0\), and that the actual solution satisfies
\[
 L(t_0)\le2-\delta\quad\hbox{for some finite }t_0\ge0,
 \qquad 0<\delta\le2.
 \tag{21}
\]
Then \(X(\infty)<\infty\), \(\int_0^\infty\sqrt{L(t)}\,dt<\infty\), the upper norms \(\sup_t\|W^2(t)\|_{\rm op}\) and \(\sup_t\|W^3(t)\|_2/\sqrt n\) are finite, and the loss tends to zero exponentially after \(t_0\). All parameters have finite limits and the limiting predictions equal \(y\).

Here are explicit constants and a proof. Write \(s_0=s(t_0)\), \(X_0=X(t_0)\), and put
\[
 \eta=\sqrt2-s_0>0,\qquad
 c=\min\left\{1,\frac{\eta}{C_f(a_0+1+\sqrt{C_D})}\right\}>0.
 \tag{22}
\]
Loss monotonicity and the reverse triangle inequality give
\(\|f(t)\|_2\ge\sqrt2-s(t)\ge\eta\) for \(t\ge t_0\). If \(b(t)\le1\), (20) yields
\[
 \eta\le C_f b(t)(a_0+1+\sqrt{C_D})(1+\sqrt{X(t)}).
\]
If \(b(t)\ge1\), the following inequality holds directly. Thus in both cases
\[
 b(t)\ge\frac{c}{1+\sqrt{X(t)}}>0\qquad(t\ge t_0).
 \tag{23}
\]
Define the elementary increasing unbounded function
\[
 F(x)=\int_0^x\frac{du}{1+\sqrt u}
     =2\bigl(\sqrt x-\log(1+\sqrt x)\bigr),\qquad x\ge0.
 \tag{24}
\]
Combining \(X'=sb\), (13), and (23) gives
\[
 \dot s\le-2\gamma bX'
 \le-2\gamma c\frac{X'}{1+\sqrt X}.
\]
Integration, with the constant continuation used if \(s\) reaches zero, proves
\[
 s(t)+2\gamma c\bigl(F(X(t))-F(X_0)\bigr)\le s_0
 \qquad(t\ge t_0).
 \tag{25}
\]
This time-domain argument also covers intervals where \(X'=0\); it does not assume that the clock has a globally differentiable inverse. Since \(F\) is unbounded, (25) bounds \(X\) on the entire infinite time axis.

For a fully explicit, slightly loose bound, the inequality
\(\log(1+u)\le u/2+\log2\) for \(u\ge0\) gives \(F(x)\ge\sqrt x-2\log2\). The logarithm inequality follows, for example, by maximizing \(\log(1+u)-u/2\), whose maximum occurs at \(u=1\) and is \(\log2-1/2\). Set
\[
 \overline X=\left(F(X_0)+\frac{s_0}{2\gamma c}+2\log2\right)^2,
 \quad \overline a=C_B\overline X,
 \quad \overline b=\sqrt{C_B^2\overline X^2+b_0^2+C_D\overline X},
 \quad U=a_0+\overline a,\quad
 \beta=\frac{c}{1+\sqrt{\overline X}}>0.
 \tag{26}
\]
Equations (16), (19), and (25) now imply
\[
 X(t)\le\overline X,\quad a(t)\le\overline a,\quad
 b(t)\le\overline b,\quad \|W^2(t)\|_{\rm op}\le U
 \qquad(t\ge0),\qquad b(t)\ge\beta\quad(t\ge t_0).
 \tag{27}
\]
For times before \(t_0\), the clock bound follows from its monotonicity. Finally (13) gives
\[
 L(t)\le L(t_0)e^{-4\gamma\beta^2(t-t_0)}\quad(t\ge t_0),
 \qquad
 S_\infty:=\int_0^\infty s(t)\,dt
 \le t_0\sqrt{L(0)}+\frac{s_0}{2\gamma\beta^2}<\infty.
 \tag{28}
\]
The quantities used in (26) are finite before invoking this conclusion; for example (11) gives the independent pre-threshold estimate
\[
 X_0\le \sqrt{L(0)}\,b_0t_0
             +\frac23 L(0)t_0^{3/2}.
 \tag{29}
\]
There is consequently no assumption of finite total clock hidden in the constants.

For completeness, all three parameter paths have finite total variation. In addition to (16), the exact equations imply
\[
 \frac{\|\dot W^3\|_2}{\sqrt n}
 \le C_BUs,
 \qquad
 \sqrt{\frac d n}\|\dot W^1\|_F
 \le2\sqrt2 PMU\,sb.
 \tag{30}
\]
For the second inequality, use
\(\|\delta^1_a\|_2\le PMU\sqrt n\,b\) in (5). Hence
\[
 \int_0^\infty\|\dot W^2\|_Fdt\le C_B\overline X,
 \quad
 \int_0^\infty\frac{\|\dot W^3\|_2}{\sqrt n}dt\le C_BUS_\infty,
 \quad
 \int_0^\infty\sqrt{\frac d n}\|\dot W^1\|_Fdt
       \le2\sqrt2 PMU\overline X.
 \tag{31}
\]
Finite-dimensional completeness gives parameter limits. Continuity of (4) and (28) makes their predictions exactly \(y\).

The original first-layer controls also become integrable, as a consequence rather than an assumption. Specifically, with
\[
 q_{ja}=-2r_a\left[(W^2)^T
                    (W^3\odot\phi_2'(z^2_a))\right]_j,
\]
one has for each sample
\[
 \int_0^\infty\frac{\|q_{:,a}(t)\|_2}{\sqrt n}\,dt
 \le2MU\overline X.
 \tag{32}
\]
This supplies actual finite-width integrable controls for the first-coordinate confinement equation. It was not needed to assume their integrability at infinite time.

## 5. A deterministic short-time lemma that supplies the loss margin

The next argument does not use \(\phi_2''\), nor a bound on an individual \(W^3_i\).

**Lemma 2.** Suppose initially
\[
 \|A_0\|_{\rm op}\le a_0,\qquad
 L(0)\le\overline L,\qquad K_3(0)\succeq\kappa I_2,
 \quad \overline L>0,\quad\kappa>0.
\]
Define
\[
 \tau=\min\left\{
 \frac1{\overline L},\,
 \frac{\kappa}{8M^2\overline L[A+P(a_0+1)]^2}
 \right\}>0.
 \tag{33}
\]
Then, throughout \([0,\tau]\),
\[
 K_3(t)\succeq\frac\kappa4I_2,\qquad
 L(t)\le L(0)e^{-\kappa t}.
 \tag{34}
\]

To prove it, Lipschitz continuity of \(\phi_1\), the input norms, and (11) give
\[
 \frac{\|H^1(t)-H^1(0)\|_F}{\sqrt n}
 \le\sqrt2P\sqrt{tL(0)}.
\]
Since \(\|W^2(t)\|_{\rm op}\le a_0+\sqrt{tL(0)}\), expand
\[
 W^2(t)H^1(t)-A_0H^1(0)
 =B(t)H^1(0)+W^2(t)[H^1(t)-H^1(0)].
\]
Lipschitz continuity of \(\phi_2\) then yields
\[
 \frac{\|H^2(t)-H^2(0)\|_F}{\sqrt n}
 \le M\sqrt{2tL(0)}
       [A+P(a_0+\sqrt{tL(0)})].
 \tag{35}
\]
Let \(Q(t)=H^2(t)/\sqrt n\). For any unit \(v\in\mathbb R^2\),
\[
 \|Q(t)v\|_2\ge\|Q(0)v\|_2-\|Q(t)-Q(0)\|_{\rm op}
              \ge\sqrt\kappa-\|Q(t)-Q(0)\|_F.
\]
For \(t\le\tau\), (33)--(35) make the final norm at most \(\sqrt\kappa/2\). Thus \(K_3(t)=Q(t)^TQ(t)\succeq\kappa I_2/4\), proving (34) through (10).

In particular, if in addition
\[
 L(0)\le2e^{\kappa\tau/2},
\]
then the **actual** trajectory has
\[
 L(\tau)\le2e^{-\kappa\tau/2}=2-\delta_*,\qquad
 \delta_*=2(1-e^{-\kappa\tau/2})>0.
 \tag{36}
\]
This also covers initial losses slightly above 2.

## 6. Discharging the short-time assumptions under canonical Gaussians

Now impose the precise independent initialization
\[
 W^1_{ij}(0)\sim N(0,1/d),\qquad
 W^2_{ij}(0)\sim N(0,1/n),\qquad
 W^3_i(0)\sim N(0,n^{-2}),
 \tag{37}
\]
with all entries in all three layers independent. In particular this readout is nonzero almost surely; it is not replaced by zero.

Let \((Z_1,Z_2)\) be centered Gaussian with covariance
\(\left(\begin{smallmatrix}1&\rho\\\rho&1\end{smallmatrix}\right)\), and define
\[
 m_s=\Pr(Z_1\ge R,Z_2\ge R)+\Pr(Z_1\le-R,Z_2\le-R),
\]
\[
 m_o=\Pr(Z_1\ge R,Z_2\le-R)+\Pr(Z_1\le-R,Z_2\ge R),
 \qquad \gamma=A^2\min(m_s,m_o)>0,
 \qquad \kappa=\gamma/2.
 \tag{38}
\]
Positivity follows because the nondegenerate Gaussian density is strictly positive on every open corner. These constants are fixed at fixed \(\rho,R,p,\varepsilon\); no endpoint uniformity is asserted.

The reservoir event
\[
 E_F=\{N_s/n\ge m_s/2,\ N_o/n\ge m_o/2\}
\]
implies \(\gamma_n\ge\gamma\), and
\[
 \Pr(E_F^c)\le\frac4n
 \left(\frac{1-m_s}{m_s}+\frac{1-m_o}{m_o}\right).
 \tag{39}
\]
Indeed each count is a sum of independent Bernoulli variables, with variance \(nm(1-m)\); apply Markov's inequality to its squared centered value at threshold \((nm/2)^2\), and then take a union bound. Independence between the two counts is not required.

### 6.1 Initial readout-feature coercivity

Conditional on \(H^1(0)=H\), the second-preactivation row pairs are independent centered Gaussians with covariance \(G=H^TH/n\). On \(E_F\), \(G\succeq\gamma I_2\) and \(G_{aa}\le A^2\). For one row write \(Z=(Z_1,Z_2)^T\) and \(V=\phi_2(Z)\). We first prove
\[
 \mathbb E[VV^T\mid H]\succeq\gamma I_2.
 \tag{40}
\]
Represent \(Z=U+\sqrt\gamma\,\xi\), where \(U\) is centered Gaussian with covariance \(G-\gamma I_2\) and \(\xi\) has two independent standard normal coordinates, independently of \(U\). Such a representation has exactly the required covariance. For any scalar random variable \(T\) of finite variance and its independent copy \(T'\),
\[
 \operatorname{Var}(\phi_2(T))
 =\frac12\mathbb E[(\phi_2(T)-\phi_2(T'))^2]
 \ge\frac12\mathbb E[(T-T')^2]
 =\operatorname{Var}(T),
\]
because \(\phi_2'\ge1\). Conditional on \(U\), the coordinates of \(V\) are independent and each has variance at least \(\gamma\). Thus, for every \(v\in\mathbb R^2\),
\[
 \mathbb E[(v^TV)^2\mid H]
 \ge\mathbb E[\operatorname{Var}(v^TV\mid U,H)\mid H]
 \ge\gamma\|v\|_2^2,
\]
which proves (40) without an assumption of nonnegative input correlation.

The Gaussian fourth moment and (3) also give, for either pair of coordinates,
\[
 \mathbb E[V_a^2V_b^2\mid H]
 \le M^4\sqrt{\mathbb E[Z_a^4\mid H]\mathbb E[Z_b^4\mid H]}
 =3M^4G_{aa}G_{bb}\le3M^4A^4.
\]
Consequently, using independence of the \(n\) second-layer rows,
\[
 \mathbb E\left[
 \left\|K_3(0)-\mathbb E[VV^T\mid H]\right\|_F^2\middle|H\right]
 \le\frac{12M^4A^4}{n}.
\]
Markov's inequality at squared threshold \(\gamma^2/4\) and (40) yield
\[
 \Pr\left(K_3(0)\not\succeq\kappa I_2\mid H\right)
 \le\frac{48M^4A^4}{n\gamma^2}
 \qquad\text{whenever }H\in E_F.
 \tag{41}
\]
The notation \(H\in E_F\) here means a first-layer realization satisfying that event. More formally one can condition on the entire initial \(W^1\); the same calculation applies. No independence between (41) and an operator-norm event for \(A_0\) will be assumed.

### 6.2 Two elementary Gaussian norm bounds

Choose the fixed constant \(a_0=8\). Then
\[
 \Pr(\|A_0\|_{\rm op}>8)
 \le2e^{-c_A n},\qquad c_A=8-2\log9>0.
 \tag{42}
\]
Here is a direct proof with constants. The Euclidean unit sphere has a \(1/4\)-net of size at most \(9^n\): take a maximal separated set and compare volumes of disjoint balls of radius \(1/8\), all contained in the ball of radius \(9/8\). For two such nets,
\(\|A_0\|_{\rm op}\le2\max_{u,v}|u^TA_0v|\), by approximating the two unit vectors attaining the norm and bounding the two errors by \(\|A_0\|_{\rm op}/4\) each. Every fixed bilinear form is \(N(0,1/n)\), so its probability of absolute value exceeding 4 is at most \(2e^{-8n}\). This tail follows from the Gaussian exponential moment \(\mathbb E e^{tZ}=e^{t^2/(2n)}\) and Markov's inequality, optimized in \(t\). The union bound over the two nets gives (42).

Likewise, writing \(W^3_i(0)=\xi_i/n\),
\[
 \Pr(b_0>2/n)\le e^{-c_b n},\qquad c_b=1-\tfrac12\log2>0.
 \tag{43}
\]
Indeed \(b_0^2=n^{-3}\sum_i\xi_i^2\), and
\(\mathbb E e^{\xi_i^2/4}=\sqrt2\). Markov's inequality bounds
\(\Pr(\sum_i\xi_i^2>4n)\) by \(e^{-n}2^{n/2}\). The Gaussian exponential moments used here follow by completing the square in the Gaussian density.

### 6.3 An explicit width threshold and probability

Fix \(a_0=8\), \(\overline L=4\), \(\gamma,\kappa\) from (38), and \(\tau\) from (33). Put
\[
 q_0=2MAa_0,\qquad
 N_*=\left\lceil\max\left\{
 2,\ \frac{q_0}{\sqrt2-1},\
 \frac{q_0}{e^{\kappa\tau/4}-1}
 \right\}\right\rceil.
 \tag{44}
\]
This is finite and independent of width and input dimension. On
\(\|A_0\|_{\rm op}\le a_0\) and \(b_0\le2/n\), (20) at time zero gives
\[
 \|f(0)\|_2\le\frac{2\sqrt2 MAa_0}{n}
                =\frac{\sqrt2 q_0}{n},\qquad
 L(0)\le2(1+q_0/n)^2.
 \tag{45}
\]
For \(n\ge N_*\), this simultaneously implies
\(L(0)\le4\) and \(L(0)\le2e^{\kappa\tau/2}\).

**Theorem 3 (actual canonical initialization).** For every fixed \(\rho\in(-1,1)\), fixed first activation (1), and fixed \(\varepsilon>0\), let \(n\ge N_*\). With probability at least \(\max\{0,1-p_n\}\), where
\[
 p_n=
 \frac4n\left(\frac{1-m_s}{m_s}+\frac{1-m_o}{m_o}\right)
 +\frac{48M^4A^4}{n\gamma^2}
 +2e^{-(8-2\log9)n}
 +e^{-(1-\frac12\log2)n},
 \tag{46}
\]
the exact finite RawGF has \(G_1(t)\succeq\gamma I_2\) for all time, reaches the actual margin (36) at \(t_0=\tau\), and satisfies every conclusion of Theorem 1.

The event is the intersection of \(E_F\), \(K_3(0)\succeq\kappa I_2\), \(\|A_0\|_{\rm op}\le8\), and \(b_0\le2/n\). Its probability follows by (39)--(43) and a union bound; (41) is integrated only over first-layer realizations in \(E_F\). No false independence between overlapping second-layer events is used. Lemma 2 and (45) then prove (36). In particular, this argument does not infer \(L(0)<2\) from the small Gaussian readout, and does not merely infer a short-time decrease from a strictly negative initial derivative.

## 7. Uniform constants on the successful canonical event

The all-time bounds in Theorem 3 can be chosen independently of \(n\) on its event, not merely separately for each successful realization. The following conservative choices make that assertion explicit. In (15) fix \(a_0=8\), and set
\[
 s_*=\sqrt2e^{-\kappa\tau/4},\qquad
 \eta_*=\sqrt2-s_*>0,\qquad
 c_*=\min\left\{1,\frac{\eta_*}{C_f(a_0+1+\sqrt{C_D})}\right\},
\]
\[
 X_{\rm pre}=2\tau+\frac83\tau^{3/2},\qquad
 X_* =\left(F(X_{\rm pre})+\frac{s_*}{2\gamma c_*}+2\log2\right)^2,
\]
\[
 U_*=a_0+C_BX_*,\quad
 b_* =\sqrt{C_B^2X_*^2+1+C_DX_*},\quad
 \beta_*=\frac{c_*}{1+\sqrt{X_*}}>0,\quad
 S_*=2\tau+\frac{s_*}{2\gamma\beta_*^2}.
 \tag{47}
\]
Indeed \(s(\tau)\le s_*\), \(L(0)\le4\), and \(b_0\le2/n\le1\). Equation (29) gives \(X(\tau)\le X_{\rm pre}\). Using the fixed lower bound \(\eta_*\) in the proof of Theorem 1 yields
\[
 \sup_{t\ge0}\|W^2(t)-W^2(0)\|_F\le C_BX_*,\quad
 \sup_{t\ge0}\|W^2(t)\|_{\rm op}\le U_*,\quad
 \sup_{t\ge0}\frac{\|W^3(t)\|_2}{\sqrt n}\le b_*,
\]
\[
 X(\infty)\le X_*,\qquad S_\infty\le S_*,\qquad
 L(t)\le s_*^2e^{-4\gamma\beta_*^2(t-\tau)}\quad(t\ge\tau).
 \tag{48}
\]
The total variation bounds (31)--(32) have the same uniform replacements. Also, for each sample,
\[
 \sup_t\frac{\|z^2_a(t)\|_2}{\sqrt n}\le AU_*.
 \tag{49}
\]
These bounds use normalized Euclidean moments for the readout and preactivations. They do not bound their coordinatewise maxima uniformly in width.

## 8. Exact proved/open boundary

The proved dynamic assertion is stronger than a conditional heuristic: Theorem 1 closes the proposed centered-balance and divergent-clock argument, and Theorem 3 supplies its actual loss-margin hypothesis for the prescribed nonzero Gaussian readout on an explicit high-probability event. The argument is finite dimensional throughout. It establishes all finite-time existence, optimization to zero loss, finite total residual time, bounded upper operator/normalized readout norms, and convergence of the finite parameter vectors.

An exact zero-readout initialization provides a separate simple diagnostic: if \(W^3(0)=0\) and \(K_3(0)\succ0\), then \(f(0)=0\), \(L(0)=2\), and \(\dot L(0)=-4y^TK_3(0)y<0\), so a loss margin occurs at a positive time. This diagnostic is not used to prove Theorem 3 and is not a substitute for (37).

The theorem does not cover every finite Gaussian draw or prove almost-sure optimization at each fixed width. Outside the stated event, the reservoir can be missing or the quantitative short-time assumptions can fail; the present proof makes no conclusion about those trajectories beyond global finite-time existence. Constants need not remain bounded as \(\rho\) approaches either endpoint. The antiparallel problem is excluded, and no separate antiparallel source was read.

Finally, the result does not give an upper bound on the curvature factor \(W^3_i\phi_2''(z^2_{ia})\) uniform in width or across parameter states. Although \(\phi_2''(z)=-2\varepsilon z/(1+z^2)^2\) is bounded, (48) only yields \(|W^3_i|\le\sqrt n\,b_*\); it does not control the required coordinatewise product uniformly. No global mean-field flow, limiting uniqueness, propagation result, persistent moving mass, nonlazy behavior, or second-layer distributional nonaffinity is inferred from these finite optimization and clock estimates.

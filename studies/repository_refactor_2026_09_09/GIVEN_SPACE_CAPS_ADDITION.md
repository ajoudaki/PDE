## 12. Dissipative caps on given operator spaces

This section concerns a different two-hidden-layer model, with three fixed
normalized inputs and the fixed activation
\[
 \phi(z)=\tfrac34(1+z)+\tfrac14\tanh z.
 \tag{12.1}
\]
It constructs global capped flows on prescribed Hilbert spaces. A separate
conditional theorem removes these caps if specified exponential tails hold.
Neither theorem constructs the Gaussian action spaces or identifies a
finite-width GF/GD limit. The cap is different from the coordinate-query cap
and the finite metric projection elsewhere in the book.

We use the half-sum loss \(E=\frac12\sum_{a=1}^3r_a^2\) and its physical
gradient-flow time throughout this section. The canonical mean squared loss
is \(\mathcal L=2E/3\). Consequently its uncapped gradient field is \(2/3\)
times the field here: evaluating an \(E\)-flow at time \(2t/3\) gives the
mean-loss flow at time \(t\). The same time rescaling applies if the entire
capped field is multiplied by \(2/3\). No raw-GD identity is inferred.

### 12.1. Spaces, fields and the loss chain rule

Let \((\Omega_\ell,\mathbb P_\ell)\), \(\ell=1,2\), be probability spaces
whose real Hilbert spaces \(\mathcal H_\ell=L^2(\Omega_\ell)\) are separable.
Give a bounded operator
\(W^{(2)}_0:\mathcal H_1\to\mathcal H_2\), together with its genuine
adjoint. It need not be Hilbert–Schmidt. This is an assumption on given
spaces, not a substitute construction of an initialized Gaussian operator.
For fixed inputs \(x_a\in\mathbb R^d\), put \(u_a=x_a/\sqrt d\) and assume
\(\|u_a\|_2=1\). The Gram \(G_{ab}=u_a^Tu_b\) may be singular; inputs
may coincide. Labels satisfy \(y_a\in\{-1,1\}\).

The state, its Hilbert norm, and initialization are
\[
 \Theta=(W^{(1)},U,W^{(3)})\in\mathcal H
 =L^2(\Omega_1;\mathbb R^d)\oplus
   \mathrm{HS}(\mathcal H_1,\mathcal H_2)\oplus\mathcal H_2,
\]
\[
 \|\Theta\|_{\mathcal H}^2
 =\mathbb E_1|W^{(1)}|^2+\|U\|_{\rm HS}^2+
   \mathbb E_2|W^{(3)}|^2,
 \qquad \Theta_0=(W^{(1)}_0,0,0),
 \tag{12.2}
\]
where \(\|W^{(1)}_0\cdot u_a\|_{L^2(\Omega_1)}=1\).
There is no distributional assumption on this first field. Set
\(W^{(2)}=W^{(2)}_0+U\).

For clarity, the Hilbert–Schmidt facts needed here can be obtained directly.
For an orthonormal basis \((e_j)\) of \(\mathcal H_1\), define
\(\|U\|_{\rm HS}^2=\sum_j\|Ue_j\|^2\) and use the corresponding sum
of inner products. Cauchy–Schwarz in the basis expansion of a vector gives
\(\|U\|_{\rm op}\le\|U\|_{\rm HS}\). Conversely any square-summable
family \((v_j)\) defines \(U\sum_j c_je_j=\sum_jc_jv_j\); this series
converges by Cauchy–Schwarz. The identification with
\(\ell^2(\mathcal H_2)\) proves completeness. Expanding in an orthonormal
basis of \(\mathcal H_2\) and interchanging nonnegative sums proves
basis independence by Parseval. In particular,
\[
 \|B\otimes H\|_{\rm HS}=\|B\|_{\mathcal H_2}\|H\|_{\mathcal H_1},
 \qquad
 \langle B\otimes H,U\rangle_{\rm HS}=\langle B,UH\rangle_{\mathcal H_2},
 \tag{12.3}
\]
where \((B\otimes H)V=B\mathbb E_1[HV]\).

Define the population fields, with all products taken on their own layer,
\[
 \begin{aligned}
 Z_a^{(1)}&=W^{(1)}\cdot u_a,& H_a^{(1)}&=\phi(Z_a^{(1)}),\\
 Z_a^{(2)}&=W^{(2)}H_a^{(1)},& H_a^{(2)}&=\phi(Z_a^{(2)}),\\
 f_a&=\mathbb E_2[W^{(3)}H_a^{(2)}],&r_a&=f_a-y_a,\\
 \Delta_a^{(2)}&=W^{(3)}\phi'(Z_a^{(2)}),&
 Q_a^{(1)}&=(W^{(2)})^*\Delta_a^{(2)},\\
 P_a&=r_aQ_a^{(1)},&P&=\bigl(\textstyle\sum_a P_a^2\bigr)^{1/2}.
 \end{aligned}
 \tag{12.4}
\]
The residual-free backward fields are \(\Delta_a^{(2)}\) and
\(\Delta_a^{(1)}=\phi'(Z_a^{(1)})Q_a^{(1)}\). The true loss directions
and the uncapped field are
\[
 \begin{aligned}
 g_1&=\sum_a\phi'(Z_a^{(1)})P_au_a,\\
 g_2&=\sum_a r_a\Delta_a^{(2)}\otimes H_a^{(1)},\\
 g_3&=\sum_a r_aH_a^{(2)},\qquad F(\Theta)=-(g_1,g_2,g_3).
 \end{aligned}
 \tag{12.5}
\]

The bounds \(|\phi(z)|\le1+|z|\), \(3/4\le\phi'(z)\le1\), and
\(|\phi''(z)|\le1/2\) follow from the displayed activation. They imply
that every field in (12.4) is in its indicated \(L^2\) space. On each
bounded state ball, all these norms, residuals and direction norms are
bounded by constants depending on the ball, the fixed data and
\(\|W^{(2)}_0\|_{\rm op}\). Forward fields and residuals are Lipschitz
there: expand each operator product into its operator difference and input
difference, use (12.3), and use the scalar activation's Lipschitz bound.
Backward fields are continuous there; local Lipschitzness is not assumed.

Here is the needed continuity argument. If \(A_j\to A\) and \(V_j\to V\)
in \(L^2\), and \(b\) is bounded and continuous, then
\[
 A_jb(V_j)\longrightarrow Ab(V)\quad\hbox{in }L^2.
 \tag{12.6}
\]
The part \((A_j-A)b(V_j)\) is bounded by
\(\|b\|_\infty\|A_j-A\|_2\). Every subsequence of \(V_j\) has a
further almost-surely convergent subsequence; dominated convergence against
\(|A|^2\) handles the other part. If the whole sequence failed to converge,
a subsequence separated from zero would contradict this conclusion.
Apply this argument to each gate product, then the operator and rank-one
estimates, to obtain continuity of all fields and of \(F\).

A strong solution is a \(C^1\) curve in \(\mathcal H\) satisfying the
indicated integral equation, hence its differential equation. For every
\(C^1\) state curve the loss satisfies
\[
 E'=\langle g_1,\dot W^{(1)}\rangle
     +\langle g_2,\dot U\rangle_{\rm HS}
     +\langle g_3,\dot W^{(3)}\rangle.
 \tag{12.7}
\]
To justify the chain rule in \(L^2\), the Bochner integral of a continuous
velocity gives coordinatewise absolutely continuous representatives on a
compact time interval. Indeed its time integral of \(L^1\) norms is
finite by Cauchy–Schwarz, so Fubini applies. The ordinary scalar chain rule
gives \(\dot H_a^{(1)}=\phi'(Z_a^{(1)})\dot Z_a^{(1)}\); (12.6) makes
this velocity continuous in \(L^2\). Its integrated identity therefore
also proves Hilbert-space differentiation. Next
\(\dot Z_a^{(2)}=\dot U H_a^{(1)}+W^{(2)}\dot H_a^{(1)}\), and the
same reasoning gives \(\dot H_a^{(2)}\). Differentiate \(f_a\), multiply
by \(r_a\), and use the genuine adjoint and (12.3) to obtain (12.7).
No Fréchet differentiability of the nonlinear activation on all of \(L^2\)
has been used.

### 12.2. Global dissipative approximants

Choose a smooth nonincreasing \(\eta:[0,\infty)\to[0,1]\), equal to one
on \([0,1]\) and zero on \([2,\infty)\). An explicit choice on \((1,2)\)
is \(\rho(2-s)/(\rho(2-s)+\rho(s-1))\), where
\(\rho(s)=e^{-1/s}\) for \(s>0\) and zero otherwise. In this section
\(\eta\) is a cutoff function, not a GD step. For \(R\ge1\), set
\[
 \tau_R(s)=\operatorname{sgn}(s)R\int_0^{|s|/R}\eta(v)\,dv,
 \quad \chi_R(s)=\begin{cases}\tau_R(s)/s&s\ne0,\\1&s=0,\end{cases}
 \quad C_R(p)=\chi_R(|p|)p\quad(p\in\mathbb R^3).
 \tag{12.8}
\]
Both \(\tau_R\) and \(C_R\) are smooth and 1-Lipschitz, equal to the
identity inside radius \(R\), and bounded in magnitude by
\(\min(|\text{input}|,2R)\). In fact their radial derivative is
\(\tau_R'\in[0,1]\); the radial map's tangential eigenvalues are
\(\tau_R(|p|)/|p|\in(0,1]\). Integrating the Jacobian on segments gives
the Lipschitz bound, and near zero the map is the identity. In particular,
\(0<\chi_R\le1\) and
\[
 |p-C_R(p)|\le|p|\mathbf1_{|p|>R},\qquad
 |s-\tau_R(s)|\le|s|\mathbf1_{|s|>R}.
 \tag{12.9}
\]

**Theorem 12.1.** For every \(R\ge1\), the equations
\[
 \dot W_R^{(1)}=-\sum_a\phi'(Z_{R,a}^{(1)})C_R((P_{R,b})_b)_a u_a
               =-\chi_R(P_R)g_{1,R},
 \quad \dot U_R=-g_{2,R},\quad
 \dot W_R^{(3)}=-\tau_R(g_{3,R})
 \tag{12.10}
\]
have a unique global strong solution from \(\Theta_0\). They satisfy
\[
 E_R(t)+\int_0^t\|\dot\Theta_R(s)\|_{\mathcal H}^2ds\le E_0=3/2,
 \quad \|\Theta_R(t)-\Theta_0\|_{\mathcal H}\le\sqrt{3t/2},
 \quad |W_R^{(3)}(t)|\le2Rt\quad\hbox{a.e.}
 \tag{12.11}
\]
On every finite horizon, all true field norms and \(\|F(\Theta_R)\|\)
are bounded uniformly in \(R\).

**Proof.** Fix a finite \(T>0\), and put \(M=1+2RT\). Temporarily replace
\(W^{(3)}\) by \(\tau_M(W^{(3)})\) only in
\(\Delta_a^{(2)}\) and the backward fields derived from it. Use these
modified backward fields in the first two equations of (12.10), retaining
the original forward fields, residuals and readout equation. This defines
an autonomous extension on all of \(\mathcal H\).

For two states in a fixed ball its top-gate difference is bounded by
\[
 \|\tau_M(W^{(3)})\phi'(Z_a^{(2)})
   -\tau_M(\bar W^{(3)})\phi'(\bar Z_a^{(2)})\|_2
 \le\|W^{(3)}-\bar W^{(3)}\|_2+M\|Z_a^{(2)}-\bar Z_a^{(2)}\|_2.
 \tag{12.12}
\]
The factor \(M\) uses \(|\tau_M|\le2M\) and
\(\operatorname{Lip}(\phi')\le1/2\). Apply the genuine adjoints and
\(\|U-\bar U\|_{\rm op}\le\|U-\bar U\|_{\rm HS}\) to compare
the incoming fields. Their residual-weighted differences obey
\[
 \|P_a-\bar P_a\|_2\le
 |r_a|\|Q_a^{(1)}-\bar Q_a^{(1)}\|_2
 +|r_a-\bar r_a|\|\bar Q_a^{(1)}\|_2.
 \tag{12.13}
\]
For the lower gate, apply the vector cap before estimating multiplication:
\[
 \|\phi'(Z_a^{(1)})C_R(p)_a-
       \phi'(\bar Z_a^{(1)})C_R(\bar p)_a\|_2
 \le\|p-\bar p\|_{L^2(\Omega_1;\mathbb R^3)}
     +R\|Z_a^{(1)}-\bar Z_a^{(1)}\|_2.
 \tag{12.14}
\]
Finally expand a rank-one difference and use
\[
 \|B\otimes H-\bar B\otimes\bar H\|_{\rm HS}
 \le\|B-\bar B\|_2\|H\|_2+\|\bar B\|_2\|H-\bar H\|_2.
 \tag{12.15}
\]
Together with the forward bounds and the readout cap's Lipschitz bound,
these estimates give a ball-wise Lipschitz constant \(K_{B,T}(1+R)\).
There is no product of the two cap sizes: the input Lipschitz constant in
(12.14) is one. The field norm on a fixed ball is bounded independently of
\(R,M\), since every cap decreases magnitude.

Choose a short interval whose length times the field bound keeps a closed
continuous-path ball inside the state ball, and whose length times its
Lipschitz constant is less than one. The integral map is a contraction on
this complete path space. Its iterates give a unique local strong solution.
The readout integral gives \(|W^{(3)}(t)|\le2Rt<M\) before \(T\), so
the auxiliary top cap is inactive. Substitution into (12.7) yields
\[
 E_R'=-\mathbb E_1[\chi_R(P_R)|g_{1,R}|^2]
      -\|g_{2,R}\|_{\rm HS}^2
      -\mathbb E_2[\chi_R(g_{3,R})|g_{3,R}|^2]
 \le-\|\dot\Theta_R\|_{\mathcal H}^2.
 \tag{12.16}
\]
The inequality is \(\chi_R^2\le\chi_R\). One common nonnegative scalar
multiplies the entire first-row gradient, so this remains valid when sample
directions cancel. Integration and time Cauchy–Schwarz prove (12.11).

If a maximal interval ended before \(T\), the energy estimate would keep
its states in a fixed ball. The bounded field makes the path Cauchy at its
endpoint. Completeness supplies a state there; its readout bound is preserved
by strong \(L^2\) convergence, by an almost-sure subsequence. The same local
extension continues the curve, a contradiction. Two choices of \(T\) agree
on overlaps: choose one auxiliary top cap larger than both readout bounds
and apply local uniqueness successively. Every strong solution of (12.10)
has that readout bound, so uniqueness applies to all such solutions. The
uniform true-field bounds follow from the energy ball bounds. \(\square\)

### 12.3. What an exponential-tail premise would give

**Theorem 12.2 (conditional continuation).** In addition to Theorem 12.1,
suppose that for every finite \(T>0\) there exist \(K_T,c_T>0\) with
\[
 \sup_{R\ge1,\,0\le t\le T}
 \left(\|P_R(t)\mathbf1_{P_R(t)>a}\|_{L^2(\Omega_1)}
 +\|g_{3,R}(t)\mathbf1_{|g_{3,R}(t)|>a}\|_{L^2(\Omega_2)}\right)
 \le K_T e^{-c_Ta}\quad(a\ge1).
 \tag{12.17}
\]
Then \(\Theta_R\) converges in \(C([0,T];\mathcal H)\), for each finite
\(T\), to a global strong solution of \(\dot\Theta=F(\Theta)\).
All fields in (12.4), and \(\Delta_a^{(1)}\), converge uniformly in their
strong \(L^2\) norms. The three true raw kernel blocks converge uniformly:
\[
 K^{(1)}_{ab}=G_{ab}\mathbb E_1[\Delta_a^{(1)}\Delta_b^{(1)}],\quad
 K^{(2)}_{ab}=\mathbb E_2[\Delta_a^{(2)}\Delta_b^{(2)}]
                  \mathbb E_1[H_a^{(1)}H_b^{(1)}],\quad
 K^{(3)}_{ab}=\mathbb E_2[H_a^{(2)}H_b^{(2)}].
 \tag{12.18}
\]
The limit has the exact loss energy identity. It is unique against strong
competitors with the same initial state on their common compact intervals,
and it restarts uniquely at every state reached by this initialized curve.
The premise (12.17) is not proved here.

**Proof.** First (12.17) gives readout tails. For \(a\ge1\),
\(\mathbb P_2(|g_{3,R}|>a)\le K_T^2a^{-2}e^{-2c_Ta}\); enlarge
constants to include smaller thresholds. The identity
\[
 \mathbb E|X|^j=j\int_0^\infty a^{j-1}\mathbb P(|X|>a)\,da
\]
and repeated integration by parts in the exponential integral give
\(\|g_{3,R}(t)\|_{L^j}\le D_Tj\) for integers \(j\ge2\), uniformly
in cap and time. Here \(j!\le j^j\) bounds the resulting factorial.
The readout integral and Minkowski give
\(\|W_R^{(3)}(t)\|_{L^j}\le TD_Tj\).
For sufficiently large \(a\), choose
\(j=\lfloor a/(eTD_T)\rfloor\ge2\) in Markov's inequality. The bound
\((TD_Tj/a)^j\le e^{-j}\) supplies an exponential probability tail.
Smaller \(a\) are covered by enlarged constants. Applying
\[
 \mathbb E[X^2\mathbf1_{|X|>a}]
 =a^2\mathbb P(|X|>a)+\int_a^\infty2v\mathbb P(|X|>v)\,dv
\]
and absorbing polynomial factors into a smaller exponential rate yields
\[
 \sup_{R,t\le T}\|W_R^{(3)}(t)\mathbf1_{|W_R^{(3)}(t)|>a}\|_2
 \le D'_T e^{-c'_Ta}\quad(a\ge1).
 \tag{12.19}
\]

We need tails only on a reference state. For bounded Lipschitz \(b\),
splitting at \(|A|=L\) proves
\[
 \|A[b(V)-b(\bar V)]\|_2
 \le\operatorname{Lip}(b)L\|V-\bar V\|_2
      +2\|b\|_\infty\|A\mathbf1_{|A|>L}\|_2.
 \tag{12.20}
\]
For two states in a common bounded ball, split their top-gate difference as
\[
 (W^{(3)}-\bar W^{(3)})\phi'(Z_a^{(2)})
 +\bar W^{(3)}[\phi'(Z_a^{(2)})-\phi'(\bar Z_a^{(2)})].
\]
Use (12.20) with the reference readout and (12.19). Apply the operator
difference estimate and (12.13) to bound the incoming differences. At the
lower gate split
\[
 g_1-\bar g_1=\sum_a\left\{
 \phi'(Z_a^{(1)})(P_a-\bar P_a)
 +\bar P_a[\phi'(Z_a^{(1)})-\phi'(\bar Z_a^{(1)})]\right\}u_a.
\]
Use (12.20) with \(\bar P_a\), whose tail is bounded by the reference
\(\bar P\) tail. The first term multiplies the already estimated incoming
difference by a bounded gate, so there is only one cutoff factor, not its
square. Equation (12.15) handles the matrix direction, and the readout
direction uses only forward differences. With \(s=\|\Theta-\bar\Theta\|\),
the result is
\[
 \|F(\Theta)-F(\bar\Theta)\|\le K(1+L)s+Ke^{-cL}.
 \tag{12.21}
\]
Constants may depend on the horizon and ball, but not the caps. Choose
\(L=\max(1,c^{-1}\log(1/s))\) for \(0<s<1\), and use bounded field
norms for larger distances. Enlarging constants gives
\[
 \|F(\Theta)-F(\bar\Theta)\|\le b_Ts\log(B_T/s).
 \tag{12.22}
\]
Take \(B_T\) larger than \(e\) times the ball's distance range, so this
modulus is increasing there. At zero it is interpreted as zero. It applies
between approximants, and against any other bounded state when the reference
alone has (12.17), (12.19).

The defects of (12.10) relative to the true field satisfy
\[
 \|\dot\Theta_R-F(\Theta_R)\|
 \le\sqrt3\|P_R\mathbf1_{P_R>R}\|_2
       +\|g_{3,R}\mathbf1_{|g_{3,R}|>R}\|_2
 \le Ke^{-cR}.
 \tag{12.23}
\]
The factor \(\sqrt3\) is Cauchy–Schwarz in the three unit input vectors;
there is no matrix defect. Comparing any two cap values \(R'\ge R\)
by their integral equations gives the absolutely continuous distance
inequality
\[
 s'\le b_Ts\log(B_T/s)+\delta_R,\quad s(0)=0,
 \qquad \delta_R=K'e^{-cR}.
 \tag{12.24}
\]
One can prove its comparison estimate directly. Start a positive scalar
majorant at \(Y(0)=\delta_R\), with
\(Y'=b_TY\log(B_T/Y)+\delta_R\). Before leaving the comparison range,
\(Y\ge\delta_R\) and \(\log(B_T/Y)\ge1\), whence
\(Y'\le(b_T+1)Y\log(B_T/Y)\). Differentiating
\(\log(B_T/Y)\) gives
\[
 Y(t)\le B_T(\delta_R/B_T)^{\exp(-(b_T+1)t)}.
 \tag{12.25}
\]
The distance is bounded by this majorant: away from zero the scalar right
side is locally Lipschitz, and the positive initial gap permits the usual
first-crossing comparison (or a strictly enlarged forcing followed by a
limit). For large \(R\), (12.25) stays inside the comparison range for all
\(t\le T\), by a first-exit argument. This proves uniform Cauchy convergence
of the full real-indexed cap family in the complete path space.

Continuity of a field map gives its uniform convergence on the paths, without
asserting compactness of a bounded Hilbert ball. Indeed, if uniform convergence
failed, choose \(R_j\to\infty\), \(t_j\in[0,T]\) witnessing a fixed
discrepancy and a subsequence with \(t_j\to t_*\). Uniform state convergence
implies both \(\Theta_{R_j}(t_j)\) and \(\Theta(t_j)\) tend to
\(\Theta(t_*)\), contradicting continuity. Apply this argument to all field
maps, using (12.6) also for \(\Delta_a^{(1)}\). Equations (12.23) and
the integral equations pass to
\(\Theta(t)=\Theta_0+\int_0^tF(\Theta(v))\,dv\). The integrand is
continuous, so the limit is strong. Cauchy–Schwarz and the uniform field
bounds give (12.18). The exact energy identity follows from (12.7).

At each time strong \(L^2\) convergence has an almost-sure subsequence.
On the event that the limit field exceeds threshold \(a\), its approximants
eventually exceed \(a/2\); Fatou bounds its squared tail by the uniform
approximating tails at \(a/2\). Adjust constants for \(1\le a<2\).
Thus the limit inherits (12.17), (12.19), uniformly in time, even though the
subsequence may depend on time. Compare a strong competitor to this reference
limit using (12.20)–(12.22). Every strong competitor is bounded on its compact
time intervals. Its distance has zero initial value and zero forcing in
(12.24). A positive initial majorant tending to zero in (12.25), now without
forcing, proves equality. The same comparison identifies overlapping horizons
and proves uniqueness starting at every reached state. The already constructed
global curve supplies existence of those continuations. \(\square\)

Theorem 12.1 supplies neither (12.17) nor a canonical Gaussian action.
Bounded \(L^2\) norms do not imply uniform square tails: on \((0,1)\),
\(A_j=\sqrt j\,\mathbf1_{(0,1/j)}\) has norm one, entirely above each
fixed amplitude threshold for large \(j\). This is an example about norms,
not a trained-path counterexample. The conditional theorem establishes
continuation on the specified spaces if its quantitative tails hold. Identifying
these spaces and comparing actual finite GF and simultaneous raw GD, including
the small random stored readout, remain separate obligations. No fitting or
persistent nonlinear feature-motion conclusion is supplied by either theorem.

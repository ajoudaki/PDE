# Single-sample residual-clock route

Scope: prompt-only independent theory for the finite canonical two-hidden-layer tanh model. No repository scientific sources, experiments, GPU work, or Git operations were used. The solve-math-rigorously and investigate-conjectures skills were applied. All arguments below are derived here.

**Conclusion.** At fixed finite width, zero readout and nonzero initial features give a bounded residual clock. For dictionaries containing the *actual sample's* initialized update coefficients through time degree \(p+1\), complex analyticity along that bounded clock gives an explicit geometric-in-\(p\) projection tail. This yields an all-physical-time estimate for orthogonal projected gradient flow. Whole-operator compression contributes an independent initialization error; ridge coefficient geometry contributes an independent mobility error. A genuine \(p\)-convergence theorem follows for a modified, background-preserving orthogonal closure. Constants are explicit, extremely conservative, and width-dependent. This is not a convergence theorem for the executed population-derived fixed-axis ridge closure.

## 1. Exact equations and finite clock

Assume \(\|x\|_2=1\), put \(g=W_1x\), and write \(W=W_2\). Components of \(W_1\) orthogonal to \(x\) stay fixed. Set
\[
h=\tanh g,\quad z=Wh,\quad H=\tanh z,\quad
D_g=\operatorname{diag}(\operatorname{sech}^2g),\quad
D_z=\operatorname{diag}(\operatorname{sech}^2z),\quad a=D_zc.
\]
For \(\theta=(c,g,W)\), use
\[
\|\delta\theta\|^2=\|\delta c\|_n^2+\|\delta g\|_n^2+\|\delta W\|_F^2.
\]
Then \(f=\langle c,H\rangle_n\) has gradient
\[
G(\theta)=(H,D_gW^Ta,ah^T/n)
\]
in this metric. Physical gradient flow is \(\dot\theta=(y-f)G\), and
\[
\dot f=(y-f)K,\qquad
K=\|H\|_n^2+\|D_gW^Ta\|_n^2+\|a\|_n^2\|h\|_n^2.
\tag{1}
\]

Assume \(c_0=0\), \(y\ne0\), and \(H_0\ne0\). Define
\[
\varepsilon=\operatorname{sgn}y,\quad q(t)=\int_0^t|y-f(u)|\,du,
\quad \kappa_0=\|H_0\|_n^2.
\]
The residual preserves its sign by (1). In clock time, \(\theta_q=\varepsilon G\). Direct differentiation gives
\[
c_q=\varepsilon H,\qquad
z_q=\varepsilon(\|h\|_n^2I+WD_g^2W^T)D_zc,
\]
\[
c_{qq}=B(q)c,\qquad
B=D_z(\|h\|_n^2I+WD_g^2W^T)D_z\succeq0.
\tag{2}
\]
For \(R(q)=\|c(q)\|_n>0\),
\[
R''=\frac{\|c_q\|_n^2-(R')^2+\langle c,Bc\rangle_n}{R}\ge0
\]
by Cauchy--Schwarz. Since \(c(q)=\varepsilon qH_0+O(q^2)\), \(R'(0+)=\|H_0\|_n\). Convexity gives \(R'\ge\|H_0\|_n\), \(R\ge q\|H_0\|_n\), and prevents a later zero of \(R\). Therefore
\[
\|H(q)\|_n=\|c_q(q)\|_n\ge R'(q)\ge\sqrt{\kappa_0},
\qquad \varepsilon f(q)=RR'\ge\kappa_0q.
\tag{3}
\]
Consequently
\[
K(t)\ge\kappa_0,\quad |y-f(t)|\le |y|e^{-\kappa_0t},
\quad q_\infty\le |y|/\kappa_0,\quad f(t)\longrightarrow y.
\tag{4}
\]
This is an exact global result with initialization-derived constants.

The same radial argument applies when feature-parameter gradient flow uses any fixed self-adjoint positive-semidefinite mobility. Indeed, if \(J\) is the feature map's differential in the indicated Hilbert metrics, then \(c_{qq}=J\Lambda J^*c\), with \(\Lambda\succeq0\). The readout metric must remain the canonical one. Both orthogonal projection and fixed-basis coefficient gradient flow satisfy this condition.

For the exact or orthogonally projected clock flow,
\[
\|c(q)\|_\infty\le q,\quad
\|W(q)-W(0)\|_F\le q^2/2,\quad
\|W(q)\|_{\rm op}\le\|W(0)\|_{\rm op}+q^2/2,
\]
\[
\|g(q)-g_0\|_n\le\|W(0)\|_{\rm op}q^2/2+q^4/8.
\tag{5}
\]
Integrate respectively \(\|c_q\|_\infty\le1\), \(\|W_q\|_F\le q\), and \(\|g_q\|_n\le(\|W(0)\|_{\rm op}+q^2/2)q\). These bounds exclude finite-clock blowup and justify global physical-time existence. If \(c_0=H_0=0\), the model is stationary; for \(y\ne0\) its residual clock is infinite.

## 2. Nonzero readout: a nonstationary infinite-clock example

The finite-clock claim is false for arbitrary \(c_0\), even when \(H_0\ne0\). Take \(n=d=x=1\), \(y>0\), and define, for \(u>0\),
\[
Z(u)=\frac{\sinh^2u}{\cosh u},\qquad
F(u)=\int_0^u
\frac{2\tanh Z(v)}
{\sinh v\,\operatorname{sech}^2Z(v)\,\operatorname{sech}^2v}\,dv.
\]
The positive integrand is \(2v+O(v^3)\), so \(F(u)=u^2+O(u^4)\). Start from any \(g_0>0\) with \(w_0=\sinh g_0\), \(c_0=-\sqrt{F(g_0)}\). The canonical clock equations preserve
\[
w=\sinh g,\quad c=-\sqrt{F(g)},\quad
g_q=-\sqrt{F(g)}\,\sinh g\,\operatorname{sech}^2Z(g)\,
\operatorname{sech}^2g.
\tag{6}
\]
Differentiating the first identity gives \(w_q=c\,\operatorname{sech}^2z\,\tanh g\); differentiating the second and using the integrand gives \(c_q=\tanh z\), with \(z=Z(g)\). Thus these are exactly the canonical equations.

The last right-hand side is negative and equals \(-g^2+O(g^4)\) near zero. It follows, by comparison with negative constant multiples of \(g^2\), that \(g(q)>0\) for finite \(q\), decreases to zero, and takes infinite clock time to reach zero. Along it,
\[
f(q)=-\sqrt{F(g(q))}\tanh Z(g(q))<0,\qquad f(q)\to0.
\]
Since \(q_t=y-f\ge y\) and is bounded above on this bounded trajectory, both physical time and clock tend to infinity; the residual tends to \(y\). This defeats the universal clock claim, not every possible approximation argument.

## 3. Exact dictionary condition and explicit analytic tail

Let \(P,Q\) be orthogonal projections onto the frozen left and right dictionaries, and let \(\Pi X=PXQ\). The required condition is
\[
\Pi\,\partial_t^jW(0)=\partial_t^jW(0),\qquad 1\le j\le p+1.
\tag{7}
\]
Including every factor in the actual sample's full update coefficients through degree \(p+1\) suffices. Different axis probes need not satisfy (7). Because \(q_t(0)=|y|\ne0\), recursive inversion and substitution of the local analytic time series shows that (7) also holds for the clock coefficients through that degree. Hence
\[
\zeta(q)=(I-\Pi)(W(q)-W_0)
\]
has a zero of order at least \(k=p+2\) at zero. This is a statement about the update, not the initial operator.

Fix \(S>0\), and put
\[
B=\|W_0\|_{\rm op}+S^2/2,\quad
a_*=\min\left\{1,\frac{\pi}{8\sqrt n(1+2B)}\right\},
\]
\[
M_*=\sqrt{1+4(S+a_*)^2+16(B+a_*)^2(S+a_*)^2},\quad
\rho=\frac{a_*}{4M_*},\quad A_*=\frac{S^2+a_*}{2},\quad
N=\left\lceil\frac{4S}{\rho}\right\rceil.
\tag{8}
\]
Then
\[
\sup_{0\le q\le S}\|\zeta(q)\|_F
\le A_*\,2^{-(p+2)/2^N}.
\tag{9}
\]
This is a proved geometric \(p\)-rate at fixed width and fixed initialized data. Its exponent can be extremely small. It uses neither future-trajectory coefficients nor a Taylor-convergence disk spanning all training.

Here is the full analytic argument. Complexify the equations without conjugating transposes. On the complex state ball of radius \(a_*\) around a real \(\theta(q_0)\), \(0\le q_0\le S\), one has
\[
\|\operatorname{Im}g\|_\infty\le\sqrt n\,a_*\le\pi/8,\qquad
\|\operatorname{Im}z\|_\infty\le\sqrt n(2B+1)a_*\le\pi/8.
\]
For the second inequality use \(\|h-h(q_0)\|_n\le2a_*\), \(\|h\|_n\le1\), and \(\|z-z(q_0)\|_n\le2Ba_*+a_*\). The elementary formulas for tanh give \(|\tanh u|\le1\), \(|\operatorname{sech}^2u|\le2\) when \(|\operatorname{Im}u|\le\pi/4\). The complex vector field is therefore holomorphic and bounded by \(M_*\) on the ball: its component norms are at most \(1\), \(4(B+a_*)(S+a_*)\), and \(2(S+a_*)\).

Cauchy's formula in any unit direction bounds the derivative by \(2M_*/a_*\) on the half ball. Picard iteration on \(|q-q_0|<\rho\) maps analytic paths in that half ball into themselves, moves the state by at most \(a_*/4\), and has contraction factor at most \(1/2\). It constructs a holomorphic solution there. Overlapping disks agree on their common real interval and hence on their overlap. Thus the exact solution extends to the tube formed by all these disks, and there
\[
\|\zeta(q)\|_F\le S^2/2+a_*/2=A_*.
\]

A bounded holomorphic function of norm at most \(A_*\), with an order-\(k\) zero at the center of a radius-\(\rho\) disk, has norm at most \(A_*2^{-k}\) on the half disk. Divide by \(q^k\), apply the maximum principle on radii approaching \(\rho\), and multiply back. This applies to vector-valued functions through scalar linear functionals.

Take \(N\) equal steps from zero to \(S\), each at most \(\rho/4\). If one half disk has bound \(A_*\eta\), the next quarter disk lies inside it; the next full disk has bound \(A_*\). The three-circles inequality at radii \(\rho/4,\rho/2,\rho\) bounds the next half disk by \(A_*\sqrt\eta\). To verify the inequality, compare \(\log|v|\) on the annulus with the affine function of \(\log|q-q_0|\) interpolating its two boundary bounds, and apply the maximum principle; zeros can be removed by a limiting regularization. Apply this to scalar functionals and take the supremum. After \(N\) steps the bound is \(A_*2^{-k/2^N}\); the half disks cover the interval. This proves (9).

## 4. All-time bound for precisely specified projected closures

Retain the canonical \(g,c\) equations and consider:

1. Whole-operator orthogonal projection: \(\widehat W(0)=\Pi W_0\), \(\widehat W_q=\varepsilon\Pi(\widehat a\widehat h^T/n)\).
2. Fixed-background update projection: \(\widehat W(0)=W_0\), with the same projected velocity. This retains the dense \(W_0\) and is a changed architecture.

In case 1 assume \(\widehat H_0=\tanh((\Pi W_0)h_0)\ne0\), and set
\[
\kappa=\min\{\|H_0\|_n^2,\|\widehat H_0\|_n^2\},\quad S=|y|/\kappa,
\quad \delta_0=\|(I-\Pi)W_0\|_F.
\tag{10}
\]
In case 2 set \(\kappa=\kappa_0\), \(S=|y|/\kappa_0\), \(\delta_0=0\).
Both physical clocks stay in \([0,S]\) by (4). Construct (8) at this \(S\). Define
\[
M=\sqrt{1+S^2+B^2S^2},\qquad
T=\begin{pmatrix}
0&B&1\\
B&2\sqrt n\,BS+2SB^2&S+2SB\\
1&S+2SB&2S
\end{pmatrix},\qquad L=\|T\|_F.
\tag{11}
\]
Then
\[
\sup_{t\ge0}|f(t)-\widehat f(t)|
\le \min\left\{|y|,
M\left(1+\frac{M^2}{\kappa}\right)e^{LS}
\left[\delta_0+A_*2^{-(p+2)/2^N}\right]\right\}.
\tag{12}
\]
It is an actual \(p\)-convergence theorem when \(\delta_0=0\), including case 2. For case 1 the initial operator term has no proved \(p\)-decay.

For completeness, \(G\) is \(L\)-Lipschitz on the convex region \(\|c\|_\infty\le S,\ \|W\|_{\rm op}\le B\). Use
\[
\|\delta z\|_n\le B\|\delta g\|_n+\|\delta W\|_F,\quad
\|\delta a\|_n\le\|\delta c\|_n+2S\|\delta z\|_n,\quad
\|W^Ta\|_\infty\le\sqrt n BS.
\]
The three rows of \(T\) bound differences of \(G_c,G_g,G_W\), respectively, using \(|\tanh''|\le2\). In the same region, \(\|G\|\le M\), \(f\) is \(M\)-Lipschitz, and the exact clock kernel obeys \(K\le M^2\).

Compare trajectories first at equal \(q\). Project the exact state, using the affine projection for case 2. Its distance from the exact state is at most
\[
D=\delta_0+A_*2^{-(p+2)/2^N}.
\]
Its initialization agrees with the closure. The difference between projected exact and closure states has norm derivative at most \(L\) times its norm plus \(LD\). Integration gives
\[
\sup_{[0,S]}\|\theta(q)-\widehat\theta(q)\|\le e^{LS}D,\quad
\sup_{[0,S]}|F(q)-\widehat F(q)|\le Me^{LS}D=:\delta_f,
\tag{13}
\]
where \(F=\varepsilon f\), \(\widehat F=\varepsilon\widehat f\).

To compare at equal physical time, both clocks start at zero and obey
\[
\dot q=|y|-F(q),\qquad
\dot{\widehat q}=|y|-\widehat F(\widehat q).
\]
Since \(F'\ge\kappa\), their difference satisfies the upper Dini derivative inequality
\[
D^+|q-\widehat q|\le-\kappa|q-\widehat q|+\delta_f,
\]
so \(|q-\widehat q|\le\delta_f/\kappa\), uniformly in physical time. Combining \(F'\le M^2\) with (13) proves the nontrivial term in (12). Both outputs move monotonically from zero toward \(y\), proving the additional bound \(|y|\). No Gronwall factor proportional to unbounded physical time is used.

The same argument bounds the reduced state by
\[
\sup_{t\ge0}\|\theta(t)-\widehat\theta(t)\|
\le(1+M^2/\kappa)e^{LS}D.
\]

## 5. Whole-operator ridge coefficient geometry

For \(W=B_2MB_1^T/n\), Euclidean coefficient gradient flow induces
\[
\mathcal A Z=K_2ZK_1,\qquad K_i=B_iB_i^T/n.
\tag{14}
\]
Indeed \(\nabla_Mf=B_2^T(ah^T/n)B_1/n\), and differentiating the representation yields (14). Let \(P_i\) project onto the column spans, \(\Pi Z=P_2ZP_1\), and put
\[
\alpha=\|\mathcal A\|_{F\to F},\quad\lambda=\max(1,\alpha),\quad
\beta=\|\mathcal A-\Pi\|_{F\to F},\quad
\delta_{\rm fit}=\|\widehat W_0-\Pi W_0\|_F.
\]
Only exact normalized orthonormality \(B_i^TB_i/n=I\) makes \(\mathcal A=\Pi\). Ridge normalization need not do so.

Assume both initial feature vectors are nonzero. Use (10), with the actual \(\widehat W_0\), and take
\[
B=\max(\|W_0\|_{\rm op},\|\widehat W_0\|_{\rm op})+\lambda S^2/2.
\]
Construct (8), (11) with this larger \(B\). The nontrivial right side of (12) becomes
\[
M\left(1+\frac{M^2}{\kappa}\right)e^{\lambda LS}
\left[\delta_0+\delta_{\rm fit}+A_*2^{-(p+2)/2^N}
+\frac{\beta S^2}{2}\right].
\tag{15}
\]
Here \(\delta_0=\|(I-\Pi)W_0\|_F\). The extra source is \((\mathcal A-\Pi)G_W\), bounded by \(\beta q\), whose integral is at most \(\beta S^2/2\); the initial projected discrepancy is \(\delta_{\rm fit}\). The flow's positive-semidefinite mobility still gives (4). Other coefficient metrics require computing their actual induced mobility. Neither initial error nor mobility error has a rate in \(p\) merely from update-jet inclusion.

## 6. Fixed-two-axis obstruction for an arbitrary single sample

Take \(d=2,n=3,c_0=0\), \(b>0\), \(W_1\)'s columns
\[
(b,0,b)^T,\qquad(0,b,b)^T,
\]
and \(W_0=e_1(-1,-1,1)\). For each axis probe \(e_i\), \(W_0\tanh(W_1e_i)=0\). Thus both probe flows are stationary and every \(W-W_0\) Taylor coefficient vanishes at every order.

For the actual normalized sample \(x=(e_1+e_2)/\sqrt2\),
\[
W_0\tanh(W_1x)
=e_1[\tanh(\sqrt2b)-2\tanh(b/\sqrt2)]\ne0.
\]
Writing \(u=\tanh(b/\sqrt2)>0\), the bracket equals \(2u/(1+u^2)-2u<0\). Therefore the exact actual-sample flow fits every \(y\ne0\) by (4).

A dictionary consisting only of the nonzero update-factor fields from these stationary probes has zero left span. Its whole-operator compression has \(W=0\), and zero-readout flow remains at output zero. Hence
\[
\sup_{t\ge0}|f(t)-\widehat f_p(t)|=|y|\quad\hbox{for every }p.
\tag{16}
\]
An implementation retaining additional generators even when all update coefficients vanish must state that enrichment; the zero-span conclusion applies only to the exact finite-probe derivative-factor construction. In particular it is not a counterexample to a finite implementation that substitutes ideal population moments into a symbolic dictionary builder: such formulas can generate extra nonzero fields in this degenerate finite example. This is a witness obstruction and a demonstration that (7) does not follow for arbitrary samples. It does not rule out every enriched dictionary or a probabilistic generic-initialization theorem.

## 7. Status and limits

- Proved: zero-readout global clock and explicit path bounds; fixed finite-width analytic update tail; all-time projected-flow estimates with separately identified initialization and mobility defects.
- Proved for a modified construction: background-preserving orthogonal projection with matched single-sample jets has a genuine explicit geometric \(p\)-rate.
- Falsified as universal claims: finite clock for arbitrary nonzero readout; success of minimal stationary two-axis update dictionaries on arbitrary samples.
- Open here: width-uniform or practically useful rates; decay of whole-operator initialization error or ridge mobility error; a convergence theorem for the executed population-derived fixed-axis closure.

Finite width is fixed before \(p\) tends to infinity. No width/order/infinite-time limit interchange is asserted. The output bound concerns training on this one sample, not generalization or multiple-sample dynamics. The analytic source estimate uses initialized derivatives of the target one-sample flow; it does not treat a conditional future-trajectory defect bound as a \(p\)-rate.

For the fixed-background orthogonal hierarchy, all constants in (12) are independent of \(p\). For whole-operator or ridge hierarchies, the displayed constants can additionally vary with \(p\) through the compressed initial feature norm and mobility; uniform control of those constants is another requirement for drawing a hierarchy-convergence conclusion.

# L=2 harmonic full-response test

2026-09-06. Bounded theoretical sidecar; author derivation, not an isolated
review. No experiments, simulations, external theorems, or other agents.

## Result and precise boundary

**User's sine follow-up, included in this same bounded search:** taking
\(\phi_1(z)=\sin z\) makes the first curvature exactly \(-Fq\), but
does not literally cancel the pre-source temporal row. Section 8 derives
that row and computes the complete first nontrivial averaged forward
coefficient at \(\rho=0\), including learned forward memory. A nonzero
pre-source contribution survives. Its sign in that particular averaged
coefficient is favorable; this is not a proof of response growth or a
no-go theorem for a Catalan/Bessel bound. The signed full-kernel failure
below also holds for this unshifted sine choice at \(\rho=0\).

The complete label-weighted transpose-response kernel is **not dissipative**
even with just one trained hidden matrix. For

\[
 \ell(z)=\phi_1(z)=1+\tfrac1{10}\arctan z,\qquad
 \phi_2(z)=1+h(z),\qquad h(z)=\varepsilon(\sin z+\cos z),
 \quad\varepsilon=1/20,
 \tag{1}
\]

and **every fixed** \(\rho\in[-1,1)\), the actual uncut finite causal
Gaussian program has, on its first two updates and for sufficiently small
positive mesh, both a positive and a negative direction for

\[
 \mathcal Q_B(v)=\sum_{k=0}^{2}v_k^T Y(Bv)_k,
 \qquad Y=\operatorname{diag}(1,-1).
 \tag{2}
\]

Here \(B\) includes the full source derivative, all retarded forward
returns, and the learned transpose rank memory. The test has \(v_0=0\)
and zero variations in every initial root. It is not the observation that
one retarded entry can be positive. It is a positive quadratic form of
the complete kernel, with its negative current blocks included.

Thus the proposed full-kernel estimate
\(\mathcal Q_B(v)\le0\) for all formal source directions, and its
stronger version bounded above by the current damping alone, are false.
The same failure holds if the left test is the mean forward sensitivity
instead of the source direction. For \(\phi_1=\arctan\), the identical
test already works at the fixed allowed angle \(\rho=3/4\).

This does **not** exclude an inequality with readout and matrix storage,
or an estimate restricted to physically induced source directions.
An exact finite-mesh energy balance with all these memory terms is given
below. Its remaining curvature and bottom-response terms are not closed.
No useful arbitrary-horizon energy bound, population-limit identification,
or global theorem is claimed. The bounded search stops after the full
kernel test and the sine follow-up's first nontrivial coefficient.

## 1. Contract, provenance, and normalization

The new L=2 contract was read completely. Only the indicated previous
sidecars were consulted for the causal-source convention and the old
retarded counterterm; the old project was not audited. Hashes are SHA256
of the source files consulted:

| Source | SHA256 |
|---|---|
| `/tmp/l2-two-sample-proof-0ywjpp/CONTRACT_AND_SEARCH.md` | `b4a9f991c1949ae195a37d4244c644c9ea231bd7e960ebfd045d6139abff82f7` |
| `/tmp/l3-two-sample-proof-DLuelg/SHIFTED_HARMONIC_CAUSAL_RESPONSE.md` | `fbb08acfe9decd7e4797266be32a68b6a5a84e892e50ae1acb958b10353770ae` |
| `/tmp/l3-two-sample-proof-DLuelg/OPPOSITE_LABEL_MODE_RESPONSE.md` | `1318581760487566cc467b2952016ce502a4d2da4a2cbf841e15c19e88a9776b` |

The investigate-conjectures skill and its contract, evidence-ledger, and
adversarial-audit references were used to separate finite algebra from
continuation claims. Only this deliverable is written.

The input Gram is \(C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\),
and \(y=(1,-1)\). Gaussian initialization and the raw optimizer are those
of the contract. In particular, the finite-width rescaled readout still
has variance \(n^{-2}\). Its limiting root is zero; this is why the finite
Gaussian program below has zero attained initial readout.

On an existing symmetric population GF before fitting, \(f_a=y_ag\)
and \(ds/dt=4(1-g)\). A feature mesh of step \(\Delta\), with
\(\lambda=\Delta/2\), has the normalized increments

\[
 \begin{split}
 W_{k+1}-W_k&=\frac\lambda n\sum_b y_b\delta_{kb}F_{kb}^T,\quad W=W^{(2)},\\
 w_{k+1}-w_k&=\lambda\sum_b y_bH_{kb},\quad w=W^{(3)},\\
 Z^1_{k+1,a}-Z^1_{ka}&=\lambda\sum_b C_{ab}y_b\ell'(Z^1_{kb})q_{kb}.
 \end{split}\tag{3}
\]

Here \(F=\ell(Z^1)\), \(H=\phi_2(Z)\), \(\delta=w\phi_2'(Z)\),
and \(q=W^T\delta\). Equation (3) is a finite feature-Euler bookkeeping
program. It is not asserted to equal finite-width raw GD after a scalar
time change: finite-width residuals need not lie exactly in the label
mode. No physical clock, initialization, or optimizer is being replaced.
The negative result is an algebraic test in the prescribed finite causal
Gaussian program, the same status as the requested older counterterm.
No width-limit theorem is imported to strengthen that status.

Write \(p=\phi_2'=h'\). Then

\[
 p'=-h,\qquad h^2+p^2=2\varepsilon^2=:b^2,
 \qquad |h|,|p|\le b.
 \tag{4}
\]

The choices (1) are fixed, bounded, smooth, nonaffine, and independent of
angle, labels, width, and time. Their distributional nonaffinity and
nonfreezing at every later finite time are not proved by this note.

## 2. Entire finite causal law, including learned memory

There are two different neuron populations. Population 1 carries
\(G\sim N(0,C)\) and the reverse-source process \(\zeta\).
Population 2 carries the forward-source process \(\xi\), the top fields,
and the readout. Use \(E_1,E_2\) for their expectations. The three Gaussian
groups \(G,\zeta,\xi\) are independent; all time and sample correlations
inside each process are retained. For \(i=(k,a),j=(r,b)\), write
\(j\prec i\) when \(r<k\). The uncut program is

\[
\begin{aligned}
 Z^1_{ka}&=G_a+\lambda\sum_{r<k,b}C_{ab}y_b\ell'(Z^1_{rb})q_{rb},
 &F_i&=\ell(Z^1_i),\\
 Z_i&=\xi_i+\sum_{j\prec i}A_{ij}\delta_j,
 &H_i&=1+h(Z_i),\\
 w_k&=w_*+\lambda\sum_{r<k,b}y_bH_{rb},
 &\delta_i&=w_kp(Z_i),\\
 q_i&=\zeta_i+\sum_{r\le k,b}B_{i,rb}F_{rb},
 &w_*&=0\quad\hbox{on the attained law}.
\end{aligned}\tag{5}
\]

The deterministic covariance and response selections are

\[
\begin{aligned}
 E\xi_i\xi_j&=E_1F_iF_j,& E\zeta_i\zeta_j&=E_2\delta_i\delta_j,\\
 S_{ij}&=E_1\partial_{\zeta_j}F_i,
 &A_{ij}&=S_{ij}+\lambda y_bE_1F_iF_j, &&j\prec i,\\
 D_{ij}&=E_2\partial_{\xi_j}\delta_i,
 &B_{ij}&=D_{ij}+\lambda\mathbf1_{r<k}y_bE_2\delta_i\delta_j,
 &&r\le k.
\end{aligned}\tag{6}
\]

The letters \(D_{ij}\) for a derivative matrix and the scalar \(D\)
used in the two-update calculation below are distinguished by indices.
Every derivative in (6) freezes deterministic coefficients and covariance
parameters, and is taken before evaluation. In particular \(\xi_0\) and
\(\xi_1\) remain different slots when their attained values coincide.
Zero-variance \(\zeta_0\) and the zero readout root are not deleted before
differentiating. Varying selected statistics would be a derivative of the
law, a different object for which this note claims no stability estimate.

The two learned terms in (6) follow by unrolling the single matrix in (3):

\[
 W_k-W_0=\lambda\sum_{r<k,b}y_b\delta_{rb}\otimes F_{rb}.
 \tag{7}
\]

The tensor has the normalized finite-width meaning \(uv^T/n\); between
population spaces it is \(x\mapsto uE[vx]\). Forward action gives the
learned part of \(A\), and transpose action gives the learned part of
\(B\). Neither is frozen or omitted. The expected-derivative terms in
(6) are the specified causal Gaussian reuse terms, not a new theorem
identifying their width limit.

At every fixed finite prefix all these expectations exist. Indeed
\(|w_k|\le k\Delta b\) on the attained zero-root law, features and gates
are bounded, and each reverse query is its Gaussian source plus a finite
sum of bounded features with deterministic finite coefficients. Causal
induction gives finite source derivatives bounded by polynomials in the
finitely many absolute Gaussian coordinates. Gaussian moments are finite.
This proves fixed-prefix finiteness, with no uniform bound in its length.

The sample involution exchanges ordinary fields \((G,\xi,Z^1,Z,F,H)\)
and negates-and-exchanges backward fields \((\zeta,q,\delta)\), while
sending \(w\) to \(-w\). Since \(y\) changes sign under exchange,
substitution in (5)-(6) verifies this inductively, including singular
covariances. Thus, exactly in this deterministic finite law,

\[
 E_2w_k=0,\qquad E_2[w_kH_{ka}]=y_ag_k,\qquad
 E_2[w_kh(Z_{ka})]=y_ag_k.
 \tag{8}
\]

## 3. Both modes and all initial-source variations

For any pair set \(X_\pm=(X_1\pm X_2)/2\), and write
\(U^1=F_+,V^1=F_-,U^2=H_+,V^2=H_-\).
Let \(p^1_\pm=(\ell'(Z^1_1)\pm\ell'(Z^1_2))/2\), and define
\(p^2_\pm\) similarly from \(p\). Put
\(d^1_a=\ell'(Z^1_a)q_a\), \(d^2_a=\delta_a\).
The entire modal equations are

\[
\begin{aligned}
 Z^1_{k,+}&=G_++\lambda(1+\rho)\sum_{r<k}d^1_{r,-},&
 Z^1_{k,-}&=G_-+\lambda(1-\rho)\sum_{r<k}d^1_{r,+},\\
 d^1_+&=p^1_+q_++p^1_-q_-,&d^1_-&=p^1_+q_-+p^1_-q_+,\\
 Z_{k,+}&=\xi_{k,+}+\sum_{r<k}A^{+-}_{kr}d^2_{r,-},&
 Z_{k,-}&=\xi_{k,-}+\sum_{r<k}A^{-+}_{kr}d^2_{r,+},\\
 q_{k,+}&=\zeta_{k,+}+\sum_{r\le k}B^{+-}_{kr}V^1_r,&
 q_{k,-}&=\zeta_{k,-}+\sum_{r\le k}B^{-+}_{kr}U^1_r,\\
 w_k&=\Delta\sum_{r<k}V^2_r,&d^2_{k,\pm}&=w_kp^2_{k,\pm}.
\end{aligned}\tag{9}
\]

On the attained law the modal coefficient blocks have zero diagonal and

\[
\begin{aligned}
 A^{+-}_{kr}&=E_1\partial_{\zeta_{r,-}}U^1_k+\Delta E_1U^1_kU^1_r,
 &A^{-+}_{kr}&=E_1\partial_{\zeta_{r,+}}V^1_k+\Delta E_1V^1_kV^1_r,\\
 B^{+-}_{kr}&=E_2\partial_{\xi_{r,-}}d^2_{k,+}
       +\Delta\mathbf1_{r<k}E_2d^2_{k,+}d^2_{r,+},
 &B^{-+}_{kr}&=E_2\partial_{\xi_{r,+}}d^2_{k,-}
       +\Delta\mathbf1_{r<k}E_2d^2_{k,-}d^2_{r,-}.
\end{aligned}\tag{10}
\]

The mode transform has inverse \((X_+,X_-)\mapsto(X_++X_-,X_+-X_-)\);
therefore \(\partial_{\xi_{r,\pm}}=\partial_{\xi_{r1}}\pm
\partial_{\xi_{r2}}\), with no extra half. The covariance identities are

\[
 E\xi_{k,+}\xi_{r,+}=E_1U^1_kU^1_r,\quad
 E\xi_{k,-}\xi_{r,-}=E_1V^1_kV^1_r,\quad
 E\zeta_{k,\pm}\zeta_{r,\pm}=E_2d^2_{k,\pm}d^2_{r,\pm}.
 \tag{11}
\]

Mixed source-mode covariances vanish by the involution. This does not
make evolved modes independent. At \(\rho=-1\), \(G_+=0\) and
\(Z^1_{k,+}=0\); (9) still retains the feature average, backward modes,
and all formal source slots. No inverse of \(C\) is used.

For completeness, take arbitrary deterministic source directions
\((v^G,v^\zeta,v^\xi,\omega)\), where \(\omega\) varies \(w_*\).
Write \(R=D_vZ^1,Q=D_vq,P=D_vZ,T=D_v\delta,u=D_vw\). Full
fixed-coefficient differentiation of (5) gives

\[
\begin{aligned}
 R_{0a}&=v^G_a,\qquad
 R_{k+1,a}=R_{ka}+\lambda\sum_bC_{ab}y_b
   [\ell''(Z^1_{kb})q_{kb}R_{kb}+\ell'(Z^1_{kb})Q_{kb}],\\
 Q_i&=v^\zeta_i+\sum_{r\le k,b}B_{i,rb}\ell'(Z^1_{rb})R_{rb},\\
 P_i&=v^\xi_i+\sum_{j\prec i}A_{ij}T_j,\\
 u_0&=\omega,\qquad
 u_{k+1}=u_k+\lambda\sum_b y_bp(Z_{kb})P_{kb},\\
 T_i&=p(Z_i)u_k-w_kh(Z_i)P_i.
\end{aligned}\tag{12}
\]

In particular, the last two equations retain the accumulated readout
derivative, and the first retains the initial-root derivative.
With \(h_\pm=(h(Z_1)\pm h(Z_2))/2\), the last equation is explicitly

\[
 T_+=p^2_+u-w(h_+P_++h_-P_-),\qquad
 T_-=p^2_-u-w(h_-P_++h_+P_-).
 \tag{13}
\]

Thus neither mode is suppressed. At the initial attained law,
\(\partial_{G_b}F_{0a}=\mathbf1_{a=b}\ell'(G_a)\),
\(\partial_{\zeta_{0b}}q_{0a}=\mathbf1_{a=b}\), and
\(\partial_{w_*}\delta_{0a}=p(\xi_{0a})\), despite the latter two
roots having zero attained variance/value. Later derivatives of these
roots follow (12). All are set to zero in the source test of Section 7.

## 4. Exact current response and full finite-mesh energy balance

Strict causality in (12) yields

\[
 B_{ka,kb}=D_{ka,kb}=-\mathbf1_{a=b}y_ag_k.
 \tag{14}
\]

For a current-slot impulse, \(P\) in that row is deterministic and \(u_k=0\).
For historical slots, with \(x_i=E_2P_i,t_i=E_2T_i\), the exact identity is

\[
 t_i=-y_ag_kx_i+
 \lambda\sum_{r<k,b}y_bE_2[p(Z_i)p(Z_{rb})P_{rb}]
 -\operatorname{Cov}_2(w_kh(Z_i),P_i)
 \tag{15}
\]

when \(\omega=0\). With a readout-root direction, add
\(\omega E_2p(Z_i)\). No product in (15) is factored.

A stronger energy calculation is possible as an identity, but does not
give the sought bound. Take any top-source direction \(v=v^\xi\),
zero other directions and \(\omega=0\), and a prefix \(k=0,\ldots,M\).
In this section \(\mathcal Q_B\) extends (2) by summing through \(M\).
Define auxiliary sums, all initially zero,

\[
\begin{aligned}
 J_{k+1}-J_k&=\lambda\sum_a y_a\delta_{ka}v_{ka},
       &&\text{on population 2},\\
 N_{k+1}-N_k&=\lambda\sum_a y_aT_{ka}F_{ka},
       &&\text{on the product of populations 2 and 1}.
\end{aligned}\tag{16}
\]

Products in \(N\) use independent population coordinates solely to
represent the deterministic product \(E_2[T_iT_j]E_1[F_iF_j]\).
This is not an independence assertion about any evolved fields within
one population. Set \(\delta u_k=u_{k+1}-u_k\), and analogously
\(\delta J_k,\delta N_k\). Then the **full** identity is

\[
\begin{aligned}
 \lambda\mathcal Q_B(v)
 ={}&\frac12E_2u_{M+1}^2-\frac12\sum_{k=0}^M E_2(\delta u_k)^2\\
 &+\frac12E_2J_{M+1}^2-\frac12\sum_{k=0}^M E_2(\delta J_k)^2\\
 &-\frac12E_{1,2}N_{M+1}^2
       +\frac12\sum_{k=0}^M E_{1,2}(\delta N_k)^2\\
 &-\lambda\sum_{k,a}y_aE_2[w_kh(Z_{ka})P_{ka}^2]\\
 &-\lambda\sum_{i,j:\,j\prec i}y_aS_{ij}E_2[T_iT_j].
\end{aligned}\tag{17}
\]

Derivation, including each sign:

1. Since \(v_i=P_i-\sum_{j\prec i}A_{ij}T_j\),
   \(\lambda\sum_i y_av_iE_2T_i
   =\lambda\sum_i y_aE_2P_iT_i
    -\lambda\sum_{j\prec i}y_aA_{ij}E_2T_iT_j\).
2. Use \(T_i=p_i u_k-w_kh_iP_i\) and
   \(\delta u_k=\lambda\sum_a y_ap_iP_i\).
   The identity \(2u_k\delta u_k=u_{k+1}^2-u_k^2-(\delta u_k)^2\)
   gives the first line and the curvature line of (17).
3. Split \(A=S+\lambda y_bE_1F_iF_j\). Its learned part is
   \(-\lambda^2\sum_{j\prec i}y_ay_bE_2T_iT_jE_1F_iF_j\).
   Telescoping \(N^2\) gives the third line, with the displayed positive
   mesh correction. The response part is the final line.
4. The learned part of \(B\) contributes
   \(\lambda^2\sum_{j\prec i}y_ay_bv_iv_jE_2\delta_i\delta_j\).
   Telescoping \(J^2\) gives the second line.

These sums retain both samples at each time; the squared increments
therefore also retain all same-time sample cross terms. There is no
unrecorded diagonal learned term.

If \(\omega\ne0\), the same proof gives (17) with first boundary term
\((E_2u_{M+1}^2-\omega^2)/2\) and left side
\(\lambda\sum_i y_av_i\{E_2T_i+[(B-D)v]_i\}\).
This explicitly accounts for the initial readout-source energy. Root
directions at population 1 are already retained in (12); (17) tests
zero such directions and has no missing population-1 root forcing.

The curvature line cannot be replaced by
\(-\lambda\sum g_kE_2P_{ka}^2\): it has the additional term
\(-\lambda\sum y_a\operatorname{Cov}_2(w_kh(Z_{ka}),P_{ka}^2)\).
The last line uses the **full** bottom response \(S\), whose equation
(12) still contains \(\ell''(Z^1)qR\). Reduction to L=2 removes a
middle population but removes neither of these products. Equation (17)
is an exact balance, not a new sufficient criterion or a closed estimate.

## 5. Initial Gaussian integrals and the entire first update

Let \(F_a=\ell(G_a)\), \(K_{ab}=E_1F_aF_b\), and
\(J^1_{ab}=E_1\ell'(G_a)\ell'(G_b)\). Define

\[
 \sigma^2=K_{11}=K_{22},\qquad
 \chi=K_{11}-K_{12}=\tfrac12E_1(F_1-F_2)^2,\qquad c=e^{-\chi}.
 \tag{18}
\]

The initialized top pair \(X\) is centered Gaussian with covariance
\(K\). Put \(D=h(X_1)-h(X_2)\). Elementary trigonometry and Gaussian
integration give exactly

\[
 \Gamma:=E_2[p(X)p(X)^T]
   =\varepsilon^2\begin{pmatrix}1&c\\c&1\end{pmatrix},\qquad
 E_2[h(X)h(X)^T]=\Gamma,\qquad
 \kappa:=E_2[Dh(X_1)]=\varepsilon^2(1-c).
 \tag{19}
\]

For example
\(p(x)p(z)=\varepsilon^2[\cos(x-z)-\sin(x+z)]\), while the corresponding
formula for \(h(x)h(z)\) has a plus sign. A centered Gaussian kills the
sine expectation, and \(X_1-X_2\) has variance \(2\chi\), giving
\(E\cos(X_1-X_2)=e^{-\chi}\). Also
\(p(x)^2=\varepsilon^2(1-\sin 2x)\) and
\(h(x)^2=\varepsilon^2(1+\sin 2x)\). This proves every entry of (19).
Exchange gives \(E_2[Dh(X_2)]=-\kappa\).

The first hidden update has zero attained value, so
\(Z^1_1=G\), \(Z_1=Z_0=X\), and \(\xi_1=\xi_0=X\) on the law.
These are value identities only. The full first coefficient blocks are

\[
\begin{gathered}
 B_{00}=0,\qquad
 A_{10}=\lambda(K+C\odot J^1)Y,\\
 B_{10}=\lambda\Gamma Y,\qquad
 B_{11}=-\lambda\kappa Y,\qquad
 w_1=\lambda D,\quad g_1=\lambda\kappa,\quad
 \delta_{1a}=\lambda Dp(X_a).
\end{gathered}\tag{20}
\]

The symbol \(\odot\) means entrywise matrix product. In particular the
response part of \(A_{10}\) comes from the nonzero formal derivative

\[
 \partial_{\zeta_{0b}}F_{1a}
   =\lambda C_{ab}y_b\ell'(G_a)\ell'(G_b).
 \tag{21}
\]

The source \(\xi_{0b}\) differentiates the readout in \(\delta_1\),
giving \(B_{10}\); the different slot \(\xi_{1b}\) differentiates its
current gate, giving \(B_{11}\). No learned transpose term has yet
appeared, since \(\delta_0=0\) on the law.

Writing \(\zeta_1=\lambda\eta\), the exact first reverse query is

\[
 q_1=\lambda\{\eta+(\Gamma-\kappa I)YF\},\qquad
 E\eta_a\eta_b=E_2[D^2p(X_a)p(X_b)].
 \tag{22}
\]

Here \(\eta\) is centered Gaussian independent of \(G\). In fact
\(\Gamma-\kappa I=\varepsilon^2c\begin{pmatrix}1&1\\1&1\end{pmatrix}\).
Thus the deterministic shift is the same in both query samples, and
\(q_{1,-}=\lambda\eta_-\). This is a useful check that the current and
historical modal assignments have not been interchanged.

## 6. Complete second-update blocks and controlled remainder

Keep exactly two updates and let \(\lambda\downarrow0\); this is a finite
algebraic expansion, not an experiment or a fixed-time continuum limit.
The second bottom state and the fresh forward coefficient are exactly

\[
 \widetilde G=Z^1_2=G+\lambda CY\operatorname{diag}(\ell'(G))q_1,
 \tag{23}
\]

\[
 A_{2a,1b}=\lambda y_b
 \left\{E_1[\ell(\widetilde G_a)F_b]
       +C_{ab}E_1[\ell'(\widetilde G_a)\ell'(G_b)]\right\}.
 \tag{24}
\]

The first summand is learned matrix memory, and the second is the full
immediate bottom-source response. To specify also the initial reverse
root column, put \(U=\lambda CY\operatorname{diag}(\ell'(G))\).
Then

\[
\begin{aligned}
 A_{20}={}&E_1\Big[\operatorname{diag}(\ell'(\widetilde G))
  \big\{I+\lambda CY\operatorname{diag}(\ell''(G)q_1)\\
 &\hspace{40mm}
       +\lambda CY\operatorname{diag}(\ell'(G))B_{11}
                                  \operatorname{diag}(\ell'(G))\big\}U\Big]
       +\lambda E_1[\ell(\widetilde G)F^T]Y.
\end{aligned}\tag{25}
\]

Indeed \(D_{\zeta_0}Z^1_1=U\),
\(D_{\zeta_0}q_1=B_{11}\operatorname{diag}(\ell'(G))U\), and
differentiating (23) before evaluation gives (25). In particular, this
column was not deleted because it multiplies zero attained \(\delta_0\).

Set \(Z=Z_2\). On the attained law,

\[
 w_2=2\lambda D,\qquad
 Z_a=\xi_{2a}+\lambda\sum_bA_{2a,1b}Dp(X_b).
 \tag{26}
\]

The derivative of the value identity \(w_2=2\lambda D\) is never used.
For a source \(\xi_{1b}\), formal causality instead gives

\[
 u_1=0,\quad T_{1c}=-\mathbf1_{c=b}\lambda Dh(X_b),\quad
 u_2=\lambda y_bp(X_b),\quad
 P_{2a}=-\lambda A_{2a,1b}Dh(X_b).
 \tag{27}
\]

Consequently the **complete** retarded block is

\[
\begin{aligned}
 B_{2a,1b}={}&\lambda y_bE_2[p(Z_a)p(X_b)]\\
 &+2\lambda^2A_{2a,1b}E_2[D^2h(Z_a)h(X_b)]\\
 &+2\lambda^3y_bE_2[D^2p(Z_a)p(X_b)].
\end{aligned}\tag{28}
\]

The second line is the full curvature-sensitivity return, not its
factorization; the third is the learned transpose rank memory. Both
are present in every use of \(B_{21}\) below.

For completeness the initial forward-root column and the current block
are

\[
\begin{aligned}
 B_{2a,0b}={}&\lambda y_bE_2[p(Z_a)p(X_b)]
 -2\lambda^2y_b\sum_cA_{2a,1c}
              E_2[Dh(Z_a)p(X_c)p(X_b)],\\
 B_{2a,2b}={}&-\mathbf1_{a=b}y_ag_2,\qquad
 g_2=2\lambda E_2[Dh(Z_1)].
\end{aligned}\tag{29}
\]

To check the first line, a \(\xi_{0b}\) variation has
\(P_1=0\), \(u_1=u_2=\lambda y_bp(X_b)\), and
\(T_{1c}=\lambda y_bp(X_c)p(X_b)\); insert these into (12).
There is no learned term with \(\delta_0\), which has zero attained
value. Equations (20), (24)-(25), and (28)-(29) specify every coefficient
block on this prefix, including all initial columns.

Here are the remainder checks, so that the sign test does not assume
unproved response regularity. Since \(D,p,F\) are bounded, (22) gives
\(q_1=O_{L^m}(\lambda)\) for every fixed finite \(m\). Hence
\(\widetilde G-G=O_{L^m}(\lambda^2)\) by (23). All relevant derivatives
of \(\ell\) are bounded, so (24)-(25) imply

\[
 A_{21}=\lambda(K+C\odot J^1)Y+O(\lambda^3),\qquad A_{20}=O(\lambda).
 \tag{30}
\]

The covariance prescription directly gives

\[
 E(\xi_{2a}-X_a)^2=E_1[\ell(\widetilde G_a)-F_a]^2=O(\lambda^4).
 \tag{31}
\]

Gaussian moments give the analogous \(L^m\) bound. Equation (26) now
gives \(Z-X=O_{L^m}(\lambda^2)\). This reasoning uses no inverse of a
possibly singular historical covariance. Boundedness and Lipschitzness
of \(h,p\), together with (28)-(29), therefore prove

\[
 B_{21}=\lambda\Gamma Y+O(\lambda^3),\qquad
 B_{22}=-2\lambda\kappa Y+O(\lambda^3).
 \tag{32}
\]

The error matrices are deterministic, with finite constants for each
fixed allowed angle. In particular, the learned transpose term and the
curvature return are explicitly bounded \(O(\lambda^3)\) remainders;
they have not been discarded on a sign premise. No uniform-in-prefix
or positive-horizon expansion is asserted.

## 7. Algebraic failure of the proposed signed full-kernel estimate

Let \(e_-=(1,-1)^T/\sqrt2\) and take the deterministic formal direction

\[
 v_0=0,\qquad v_1=e_-,\qquad v_2=e_-.
 \tag{33}
\]

All bottom-root, reverse-source, and readout-root directions are zero.
The output includes every causal block of \(B\). Terms in its initial
column vanish because the chosen input there is zero, not because that
column was omitted from the law. By (20) and (32),

\[
\begin{aligned}
 \mathcal Q_B(v)
 &=e_-^TYB_{11}e_-+e_-^TYB_{21}e_-+e_-^TYB_{22}e_-\\
 &=\lambda\{\varepsilon^2(1+c)-3\kappa\}+O(\lambda^3)\\
 &=\lambda\varepsilon^2(4c-2)+O(\lambda^3).
\end{aligned}\tag{34}
\]

Indeed \(Ye_-=(1,1)^T/\sqrt2\), so the historical quadratic term uses
the **average-gate eigenvalue** \(\varepsilon^2(1+c)\). Both current
terms have the negative values \(-\lambda\kappa\) and
\(-2\lambda\kappa+O(\lambda^3)\). These are both sample modes in the
label-weighted pairing, not a trace or a single-entry sign test.

For (1), global Lipschitzness with constant \(1/10\) gives

\[
 0<\chi\le\frac{1-\rho}{100}\le\frac1{50},\qquad
 c=e^{-\chi}\ge1-\chi\ge\frac{49}{50},\qquad
 \varepsilon^2(4c-2)\ge\frac3{625}>0.
 \tag{35}
\]

The strict inequality \(\chi>0\) holds because \(G_1-G_2\) has positive
variance for every \(\rho<1\), and \(\ell\) is strictly increasing.
This includes \(\rho=-1\). Thus (34)-(35) prove, for every fixed allowed
\(\rho\), that \(\mathcal Q_B(v)>0\) at all sufficiently small positive
meshes. This is an existence of a strictly positive algebraic sign at a
specified finite prefix, not a numerical search for a mesh threshold.

The same full kernel has a negative direction: take only \(v_1=e_-\)
nonzero. Its quadratic form is exactly
\(-\lambda\kappa<0\). Hence neither choice of overall sign makes the
full label-weighted kernel semidefinite on formal source directions.
Positive time quadrature by the common factor \(\lambda\) or \(\Delta\)
does not change these signs.

If one instead tests against \(x_i=E_2P_i\), (27) gives

\[
 x_1=v_1,\qquad x_2=v_2-\lambda\kappa A_{21}Yv_1
                  =v_2+O(\lambda^2).
 \tag{36}
\]

Since \((Bv)_1,(Bv)_2=O(\lambda)\), replacing the left vector in (34)
by \(x\) changes it only by \(O(\lambda^3)\); strict positivity persists.
Thus the mean-forward-sensitivity formulation does not repair the
proposed nonpositivity estimate.

For the alternative \(\ell(z)=\arctan z\), take the fixed angle
\(\rho=3/4\). Then \(0<\chi\le1/4\), \(c\ge3/4\), and the leading
coefficient in (34) is at least \(\varepsilon^2>0\). The same proof
applies. No claim is made that this particular test has the same sign
at every angle for that alternative activation.

## 8. Unshifted first sine: the pre-source row does not cancel

This section responds to the user's additional analytic lead within the
same two-update budget. Set \(\ell(z)=\sin z\), keep the top activation
in (1), and write \(F=\sin Z^1,p^1=\cos Z^1\). The full finite law,
source derivatives, energy identity, and coefficient formulas in
Sections 2-6 hold with this substitution. In particular \(\ell''=-F\).
Monotonicity of \(\ell\) was used only for (35), not for those formulas.

### 8.1 Exact causal discrimination, for every angle

Take a bottom reverse-source impulse in slot \((r,b)\), with zero
initial-root direction, and let \(R_k=D_{\zeta_{rb}}Z^1_k\).
Then \(R_u=0\) for \(u\le r\), and
\(R_{r+1}=\lambda CY\operatorname{diag}(p^1_r)e_b\).
For \(k>r\), the exact derivative equation is

\[
 R_{k+1}=R_k-\lambda CY\operatorname{diag}(F_kq_k)R_k
    +\lambda CY\operatorname{diag}(p^1_k)
        \sum_{r<u\le k}B_{ku}\operatorname{diag}(p^1_u)R_u.
 \tag{S1}
\]

There is no direct source injection at these later rows. Substituting
\(q_k=\zeta_k+\sum_{u\le k}B_{ku}F_u\) displays the pre-source part

\[
 -\lambda CY\operatorname{diag}
    \left(F_k\left[\zeta_k+\sum_{u\le r}B_{ku}F_u\right]\right)R_k.
 \tag{S2}
\]

The brackets and products in (S2) are componentwise except for the
displayed sample matrices. The differentiated return in (S1) has no
\(u\le r\) summands because their sensitivities are zero; their attained
features in (S2) need not be zero. The terms with \(r<u<k\) are retained
in (S1) as well, on both sides of the product rule.

The current \(B_{kk}=-g_kY\) combines its two occurrences to give

\[
 -\lambda g_k C\operatorname{diag}((p^1_k)^2-F_k^2)R_k
   =-\lambda g_k C\operatorname{diag}(\cos(2Z^1_k))R_k.
 \tag{S3}
\]

This is not identically zero and its diagonal multiplier is not
pointwise nonnegative. The identity \((p^1)^2+F^2=1\) has the wrong
sign to turn the difference in (S3) into a positive constant.

One can check the remaining current Gaussian coefficient without any
expectation or inequality: since \(R_k,F_k\) and the differentiated
return in (S1) do not depend on the current formal \(\zeta_k\),

\[
 \partial_{\zeta_{kc}}R_{k+1,a}
     =-\lambda C_{ac}y_cF_{kc}R_{kc}\qquad(k>r).
 \tag{S4}
\]

All deterministic coefficients remain fixed as required by the source
convention. For example at \(C=I,k=1,r=0,c=a=b\), (S4) is
\(-\lambda^2\sin G_a\cos G_a\), nonzero with positive Gaussian
probability. Thus the pathwise prehistory multiplier has not vanished.
This fact alone would not exclude cancellation after expectation. The
next calculation checks that issue at its first nontrivial order.

### 8.2 Complete first averaged return at the fixed angle rho=0

Now take \(\rho=0\), so the two initial roots are independent standard
Gaussians. This is a discriminating calculation at one admissible angle,
not a restriction of the desired all-angle theorem. Write

\[
\begin{gathered}
 F_a=\sin G_a,\quad p_a=\cos G_a,\quad
 K_0=E F_a^2=\frac{1-e^{-2}}2,\quad
 J_0=E p_a^2=\frac{1+e^{-2}}2,\\
 \chi=K_0,\quad c=e^{-K_0},\quad\kappa=\varepsilon^2(1-c),\\
 m_{22}=E[p_a^2F_a^2]=\frac{1-e^{-8}}8>0,\qquad
 m_4=E p_a^4=\frac{3+4e^{-2}+e^{-8}}8.
\end{gathered}\tag{S5}
\]

These identities follow by writing the squares and fourth powers as
cosines of \(2G\) and \(4G\), with Gaussian expectations \(e^{-2}\)
and \(e^{-8}\). Odd cross-sample factors have zero expectation.

The top historical and current returns remain **both** those of (20):
\(B_{10}=\lambda\Gamma Y\), \(B_{11}=-\lambda\kappa Y\).
By (22), define

\[
 t_a=\eta_a+y_a\varepsilon^2c(F_a-F_b),\quad b\ne a,
 \qquad q_{1a}=\lambda t_a,\qquad
 Z^1_{2a}=G_a+\lambda^2y_ap_at_a.
 \tag{S6}
\]

The Gaussian vector \(\eta\) is independent of \(G\) with covariance
in (22); no factorization between its two coordinates is required.

For the formal initial impulse \(\partial_{\zeta_{0a}}\), differentiating
before evaluation gives exactly

\[
\begin{aligned}
 R_{1a}&=\lambda y_ap_a,\\
 \partial_{\zeta_{0a}}q_{1a}
      &=B_{11,aa}p_aR_{1a}=-\lambda^2\kappa p_a^2,\\
 R_{2a}&=\lambda y_ap_a-\lambda^3F_ap_at_a
                              -\lambda^3y_a\kappa p_a^3.
\end{aligned}\tag{S7}
\]

The \(B_{10}F_0\) part contributes to the attained \(q_1\) in this
formula, although its derivative is zero. Taylor expansion of the
output gate, with a bounded second derivative, yields

\[
 \cos(Z^1_{2a})=p_a-\lambda^2y_aF_ap_at_a+O_{L^m}(\lambda^4).
 \tag{S8}
\]

Multiplying (S7)-(S8) and taking expectations gives the full response
coefficient, with neither the gate variation nor the self-return omitted:

\[
 S_{2a,0a}=\lambda y_aJ_0
       -\lambda^3y_a[2\varepsilon^2c\,m_{22}+\kappa m_4]
       +O(\lambda^5).
 \tag{S9}
\]

Indeed \(E[p_a^2F_at_a]=y_a\varepsilon^2c\,m_{22}\): the noise is
centered and independent of \(G\), and the term containing \(F_b\)
has zero expectation. This use of independence is confined to the
initialized variables for which it is part of the exact law.

There is a further cancellation with the **learned forward** memory,
which must also be included. Expansion of its exact value gives

\[
 \lambda y_aE[\sin(Z^1_{2a})F_a]
   =\lambda y_aK_0+\lambda^3y_a\varepsilon^2c\,m_{22}
                                      +O(\lambda^5).
 \tag{S10}
\]

Using \(K_0+J_0=1\), the complete coefficient is therefore

\[
 \boxed{\displaystyle
 A_{2a,0a}=\lambda y_a
       -\lambda^3y_a[\varepsilon^2c\,m_{22}+\kappa m_4]
       +O(\lambda^5).}
 \tag{S11}
\]

Every remainder asserted here follows from the exact displacement
\(\lambda^2y_ap_at_a\), bounded sine/cosine derivatives, and finite
Gaussian moments of \(\eta\). No continuum or long-prefix regularity
is needed.

To locate the pre-source contribution without altering the model, use
the exact identity \(\varepsilon^2c=\varepsilon^2-\kappa\) in (S11):

\[
 \varepsilon^2c\,m_{22}+\kappa m_4
    =\underbrace{\varepsilon^2m_{22}}_{\text{historical }B_{10}}
       +\underbrace{\kappa(m_4-m_{22})}_{\text{current }B_{11}}.
 \tag{S12}
\]

The first term is nonzero. The attribution follows directly by keeping
\(q_1=\zeta_1+B_{10}F_0+B_{11}F_1\) separated in (S7)-(S10): the
historical diagonal has coefficient \(\varepsilon^2\), its off-diagonal
term averages to zero here, and the current diagonal has coefficient
\(-\kappa\). Learned forward memory cancels one of two such response
contributions, leaving (S12). This is bookkeeping within the actual
canonical coefficient, not a modified initialization or an auxiliary
model counterexample.

The top learned **transpose** memory first appears in \(B_{21}\), as
the third line of (28). It is already included in the full-kernel test.
It cannot alter (S11) because \(A_{20}\) is selected before \(q_2\) by
causal order. Thus no still-unincluded learned term can retroactively
cancel this first averaged pre-source contribution.

The correction in \(y_aA_{2a,0a}\) in (S11) is negative. This is
favorable for that one coefficient, and is not promoted to an absolute
response bound. It establishes that the proposed literal cancellation
does not occur, without claiming that the surviving term is harmful
in every possible energy.

### 8.3 Full-kernel sign and the Catalan/Bessel question

For this same sine choice and \(\rho=0\), (S5) gives
\(c\ge1-K_0=(1+e^{-2})/2\), so
\(\varepsilon^2(4c-2)\ge2\varepsilon^2e^{-2}>0\).
The complete-kernel calculation (34), including (28), consequently has
the same strictly positive direction, while its current-only test is
negative. Thus changing the first activation to an unshifted harmonic
does not repair the all-slot nonpositivity estimate.

A pure triangular convolution majorant would need an actual derivation
in which the pre-source row in (S2) is canceled, favorably controlled,
or absorbed with a separately bounded propagation factor. Equations
(S2)-(S4) and the nonzero term (S12) prevent asserting the first of those
options as an identity. The other options remain open: the favorable
sign of (S11) has not been extended to the two-mode, all-history system
or to the mixed terms of (17). No Riccati row-sum bound is treated as a
blow-up theorem, and no Catalan/Bessel majorant is claimed merely from
causality. This completes the requested first nontrivial discrimination.

## 9. What this resolves, and where the energy attempt stops

The failed assertion is precise: current harmonic damping cannot be
promoted to \(\sum v^TYBv\le0\) for the complete causal kernel, even
with one trained hidden matrix and with zero initial-source variation.
This is a canonical finite-program failure for the chosen nonlinear
activations, not an arbitrary ambient model or a changed training path.

The positive direction is expected to create readout-sensitivity energy:
in (17), \(u_3\) need not vanish for (33). Therefore (34) does not refute
a storage inequality which retains \(E_2u_3^2/2\), or one which also
retains the two learned-memory energies. It does not refute a bound
restricted to a covariance-supported forcing class. Historical source
slots are formal, and (33) need not lie in the support of their singular
joint Gaussian covariance. The proposed all-slot kernel estimate is
exactly the claim tested, without silently passing to such a quotient.

Trying the more informative storage balance (17) leaves these two
specific terms:

\[
 -\lambda\sum_{k,a}y_aE_2[w_kh(Z_{ka})P_{ka}^2],\qquad
 -\lambda\sum_{j\prec i}y_aS_{ij}E_2[T_iT_j].
 \tag{37}
\]

The first retains a curvature-weighted squared sensitivity, and the
second couples the full bottom response to same-population top-response
products. The bottom variation equation still contains
\(\ell''(Z^1)qR\), with both angle modes. No sign, domination by the
displayed storage, or mesh-uniform bound for their combined contribution
has been proved. A first-moment or trace statement cannot replace these
terms. Merely assuming control of (37) would be an equivalent missing
criterion, and is not reported as progress.

| Claim | Status and scope |
|---|---|
| Full L=2 causal and modal equations, all root variations, both learned actions | Exact in the stated finite Gaussian program |
| Storage identity (17), with learned forward and reverse memory and mesh defects | Exact; not a closed bound |
| All coefficient blocks through the second update and the remainder in (32) | Derived with finite-moment estimates |
| Full signed-kernel nonpositivity, even with zero initial-root forcing | Falsified by (33)-(35), for every fixed allowed angle for (1) |
| Opposite sign / positive semidefiniteness of the same kernel | Falsified by the single-current-source test |
| First sine makes the pre-source row cancel identically | Falsified as a literal identity by (S2)-(S4), with a surviving averaged contribution in (S11)-(S12) |
| Full-kernel nonpositivity for first sine at rho=0 | Falsified by (34) and (S5) |
| A Catalan/Bessel majorant for the actual first-return recursion | Open; no all-history cancellation or bounded propagation factor derived |
| A richer storage/passivity estimate for the actual causal recursion | Open; (37) remains uncontrolled |
| Global existence, restart uniqueness, exact GD/GF/MF convergence, all observables, later-time nonaffinity/nonfreezing | Not proved or upgraded |

The skill's claim-level separation matters here: the new conclusion is a
failure of a specified signed full-kernel proof route, stronger than the
old isolated retarded-counterterm sign observation. It is not a general
impossibility claim. The authorized finite-mesh derivation and first
nontrivial checks, including the user-requested sine follow-up, are
complete; this sidecar stops without opening a further search branch.

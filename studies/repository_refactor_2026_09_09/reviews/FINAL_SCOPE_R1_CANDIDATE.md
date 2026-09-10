# Remaining scoped theory additions

These five independent fragments use the shared notation. Equations are
numbered locally within each fragment. Their dependencies are the exact
finite model and metric in the finite-dynamics chapter, special-data
Sections III.M and III.F, and, in E, the explicit two-sample model and
estimates in Part II. Initialization, formal initial
coefficients, finite-time dynamics, and conditional source estimates have
different conclusions.

## A. Three-hidden-layer tanh: vanishing-time continuity and zero-label stationarity

Take one input equal to one, three hidden layers, unit mobilities, full
square loss and **order-one stored Gaussian readout**. Thus the independent
initial variables are
\[
 W^{(1)}_i(0),W^{(4)}_i(0)\sim N(0,1),\qquad
 W^{(2)}_{ij}(0),W^{(3)}_{ij}(0)\sim N(0,1/n).
\]
Write \(\Gamma^{(\ell)}=W^{(\ell)}(0)\), use \(\phi=\tanh\), and
reconstruct the forward and backward fields as in the finite-dynamics
chapter. In particular
\[
 q^{(2)}=(W^{(3)})^T\delta^{(3)},\quad
 q^{(1)}=(W^{(2)})^T\delta^{(2)},\quad
 \delta^{(3)}=W^{(4)}\phi'(z^{(3)}),\quad
 \delta^{(j)}=\phi'(z^{(j)})q^{(j)}\ (j=1,2).
\]
The immutable reverse queries are
\(\bar q^{(j)}=(\Gamma^{(j+1)})^T\delta^{(j+1)}\).
The raw metric is
\[
 \|d\theta\|_{\rm raw}^2
 =\frac{\|dW^{(1)}\|_2^2+\|dW^{(4)}\|_2^2}{n}
   +\|dW^{(2)}\|_F^2+\|dW^{(3)}\|_F^2.
\]
Let \(r=f_n-y\). The exact flow is \(\dot\theta=-2r\nabla f_n\),
where the gradient uses this metric, and its raw kernel is
\[
 K_n=\frac{\|h^{(3)}\|_2^2}{n}
 +\frac{\|\delta^{(3)}\|_2^2\|h^{(2)}\|_2^2}{n^2}
 +\frac{\|\delta^{(2)}\|_2^2\|h^{(1)}\|_2^2}{n^2}
 +\frac{\|\delta^{(1)}\|_2^2}{n}.                       \tag{A.1}
\]
Consequently \(\dot f_n=-2rK_n\), \(\dot r=-2rK_n\), and
\(\frac d{dt}r^2=-4r^2K_n\). All statements below concern this exact
continuous flow; no new raw-GD theorem is asserted.

**Theorem.** For every fixed label and every deterministic \(t_n\downarrow0\),
\[
 \sup_{0\le t\le t_n}|K_n(t)-K_n(0)|\longrightarrow0
 \quad\hbox{in probability}.                            \tag{A.2}
\]
The same is true of every forward/backward field's RMS displacement from
its own initialization and of the two immutable reverse queries. In addition,
\[
 \max_{t\le t_n,j=1,2,i}|\bar q_i^{(j)}(t)|
 =O_{\mathbb P}\!\left(\sqrt{\log n}
            +\sqrt{nt_n\log(e/t_n)}\right),              \tag{A.3}
\]
so its quotient by \(\sqrt n\) vanishes in probability. For target \(y=0\),
on every fixed physical interval \([0,T]\),
\[
 \sup_{t\le T}\bigl(|f_n(t)|+|r_n(t)|+r_n(t)^2
                       +|K_n(t)-K_0|\bigr)\longrightarrow0
 \quad\hbox{in probability},                            \tag{A.4}
\]
where, for a standard normal \(G\),
\[
 q_1=E\tanh^2G,\quad q_2=E\tanh^2(\sqrt{q_1}G),\quad
 q_3=E\tanh^2(\sqrt{q_2}G),
\]
\[
 s_3=E\operatorname{sech}^4(\sqrt{q_2}G),\quad
 s_2=s_3E\operatorname{sech}^4(\sqrt{q_1}G),\quad
 s_1=s_2E\operatorname{sech}^4G,
 \qquad K_0=q_3+s_3q_2+s_2q_1+s_1.                     \tag{A.5}
\]
This is a stationary limiting trajectory. It does not establish
order-one feature learning for nonzero labels.

*Proof.* We first verify the initialization and then transfer its square
tails through each gate on a short feature interval.

Successive fresh forward Gaussian rows give the variances \(q_1,q_2,q_3\).
The fixed-program law in special-data III.F applies directly after an odd
smooth truncation of the independent Gaussian readout at level \(M\).
The top gate/readout product then has bounded first derivatives. The first
reverse response coefficient is the expectation of the truncated centered
readout times \(\phi''(Z^{(3)})\), hence zero. The resulting reverse
innovation is independent of the preceding layer and has variance
\(E[a_M^2]s_3\), where \(a_M\) is the truncated readout. For the next
reverse call, first replace this Gaussian query by an odd
smooth scalar clip at level \(N\). Its product with the next gate has
bounded derivatives, and its response coefficient is zero because the
clipped query is centered and independent of \(Z^{(2)}\). Remove \(N\)
after this fixed-program limit: the previous joint \(\mathcal W_2\) law
gives vanishing empirical squared query tails, multiplication by the
bounded gate costs at most one, and the next action costs only its
operator norm. The variance consequently tends to \(E[a_M^2]s_2\).
The final gated square passes from the joint \(\mathcal W_2\) law by
truncating that final query and then removing its square tails.
Thus the gates give squared backward norms \(E[a_M^2]s_j\).

These conclusions hold for joint tuples with each preceding layer.
The finite comparison on removing \(M\) is direct: all forward fields
are unchanged, and the backward recursion is linear in the readout with
gate norms at most one and initialized operator norms bounded in probability.
Thus its RMS error is at most a tight constant times
\(\|W^{(4)}(0)-a_{M,n}\|_2/\sqrt n\). The law of large numbers and Gaussian
square tails make this vanish in the order \(n\to\infty\), then
\(M\to\infty\). The same comparison holds for the generated population
actions. Since \(E a_M^2\to1\), the kernel converges to (A.5).
No growing program or empirical all-moment theorem is used.

For the tail estimate, condition on all initial variables except the
readout. For every coordinate, the initial immutable queries are centered
Gaussian linear forms in that readout, with variances at most
\[
 \|\Gamma^{(3)}_{:,i}\|_2^2,
 \qquad
 \|\Gamma^{(3)}\|_{op}^2\|\Gamma^{(2)}_{:,i}\|_2^2.
\]
The operator-norm event of III.F.2 also bounds every column norm. Choose
one deterministic sufficiently large \(L\). Conditional Gaussian
integration and Markov's inequality yield
\[
 \frac1n\sum_i\left[
 e^{W_i^{(4)}(0)^2/L^2}+
 e^{\bar q_i^{(2)}(0)^2/L^2}+
 e^{\bar q_i^{(1)}(0)^2/L^2}\right]=O_{\mathbb P}(1).    \tag{A.6}
\]
Independence between query coordinates is unnecessary. A conditional
Gaussian union bound also gives their maximum \(O_{\mathbb P}(\sqrt{\log n})\).

For either fixed sign \(\sigma\in\{-1,1\}\), use the exact feature
flow \(d\theta/ds=\sigma\nabla f_n\). Bounded activations imply
\(\|W^{(4)}(s)\|_2/\sqrt n\le\|W^{(4)}(0)\|_2/\sqrt n+s\).
The upper rank-one update then bounds \(W^{(3)}\), and the next update
bounds \(W^{(2)}\), on every fixed feature interval. The bottom velocity
is bounded by their operator norms times the readout RMS. These estimates
also exclude finite feature-time escape. Alternatively the exact path
length satisfies
\[
 \int_0^s\sqrt{K_n(v)}\,dv
 \le\sqrt{s\int_0^s K_n(v)\,dv}
 \le\sqrt{s\{2\|W^{(4)}(0)\|_2/\sqrt n+s\}},            \tag{A.7}
\]
since \(d(\sigma f_n)/ds=K_n\) and \(|f_n|\le\|W^{(4)}\|_2/\sqrt n\).
Thus raw parameter displacements, and then all forward RMS displacements,
are \(O_{\mathbb P}(\sqrt s)\), uniformly up to a small \(s\) and in
both signs. Rank-one Frobenius bounds control action differences.

Here is the multiplier estimate used in the reverse transfer. For
\(|w_i|\le1\), put \(u=n^{-1}\sum_iw_i^2\) and
\(M_v=n^{-1}\sum_i e^{v_i^2/L^2}\). If \(u>0\), set
\(p_i=w_i^2/(nu)\). Jensen's inequality for the logarithm gives
\[
 \sum_i p_i\frac{v_i^2}{L^2}
 \le\log M_v+\sum_i p_i\log(np_i)
 \le\log M_v+\log(1/u).
\]
For the first inequality, apply Jensen to
\(\sum_{p_i>0}p_i\log(e^{v_i^2/L^2}/(np_i))\), whose exponential
average is at most \(M_v\). The second uses \(np_i\le1/u\).
Therefore
\[
 \frac{\|vw\|_2^2}{n}
 \le L^2u\log(M_v/u),                                  \tag{A.8}
\]
with value zero when \(u=0\).

Write the top backward difference as
\[
 \phi'(z^{(3)}(s))[W^{(4)}(s)-W^{(4)}(0)]
 +[\phi'(z^{(3)}(s))-\phi'(z^{(3)}(0))]W^{(4)}(0).
\]
The first term is controlled by (A.7). Apply (A.8) to the second
using (A.6); the bounded Lipschitz gate difference has squared RMS
\(O_{\mathbb P}(s)\). Thus this backward difference is
\(O_{\mathbb P}(\sqrt{s\log(e/s)})\).
Next subtract the actual \(W^{(3)}\) action and apply the same split to
\(\delta^{(2)}\), now with the **fixed initial** query \(q^{(2)}(0)\)
as the multiplier. Repeat at \(\delta^{(1)}\) with \(q^{(1)}(0)\).
Each action costs only a bounded operator norm, and each new gate is
paired with an initially controlled variable; no logarithm is iterated.
All backward/query displacements have this same bound. The four squared
terms in (A.1) consequently prove feature-time kernel equicontinuity.

For the immutable query maximum, use
\[
 \max_i|\Gamma_{:,i}^Tv|
 \le\max_i\|\Gamma_{:,i}\|_2\,\|v\|_2
\]
and the preceding backward displacement, together with the initial
Gaussian maximum. This proves (A.3) in feature time. In physical time
\(s(t)=2\int_0^t|r_n(v)|\,dv\le2t|r_n(0)|\); the sign is
\(-\operatorname{sgn}r_n(0)\). The initial residual is tight. Localizing
its magnitude and then removing the localization proves (A.2)–(A.3).
The same argument proves the two-limit equicontinuity statement with
\(\lim_{\rho\downarrow0}\limsup_n\) on a deterministic feature interval.

For \(y=0\), conditionally on the initial hidden weights,
\(f_n(0)\) is centered Gaussian with variance at most \(1/n\), so
\(r_n(0)=O_{\mathbb P}(n^{-1/2})\). Residual magnitude decreases, and
therefore \(s(T)=O_{\mathbb P}(n^{-1/2})\). For any fixed \(\rho>0\),
the probability that this clock exceeds \(\rho\) tends to zero.
Use the just-proved uniform small-clock estimate, then let \(\rho\downarrow0\),
to obtain the kernel part of (A.4). The other parts follow already from
\(|f_n(t)|=|r_n(t)|\le|r_n(0)|\). This proves the theorem.

The same estimates exclude a nonvanishing square-energy concentration
on any set of \(o(n)\) coordinates at vanishing time: the initial fields
have uniformly integrable squares by (A.6), and their RMS perturbations
vanish. They give no positive-time tail estimate for a nonzero fixed label.
In particular a proposed nonzero-label proof still needs actual adaptive
query tails and uniform comparison/source/cutoff arguments.


A further exact finite-flow estimate controls the first gate's inverse.
Let \(u=W^{(1)}\), \(g_j=W^{(2)}_{:,j}\),
\(\gamma_j=\Gamma^{(2)}_{:,j}\), and \(p_j=g_j-\gamma_j\).
Set \(\Phi(u)=\frac12\sinh^2u\), so
\(\Phi'(u)=\tanh(u)/\operatorname{sech}^2(u)\).
In either signed feature flow,
\[
 g_j'=\frac\sigma n\tanh(u_j)\delta^{(2)},\qquad
 u_j'=\sigma\operatorname{sech}^2(u_j)q_j^{(1)}.
\]
Direct differentiation gives the two coordinate identities
\[
 \frac d{ds}\left(\Phi(u_j)-\frac n2\|g_j\|_2^2\right)=0,
 \qquad
 \frac d{ds}\left(\Phi(u_j)-\frac n2\|p_j\|_2^2\right)
   =\sigma\tanh(u_j)\bar q_j^{(1)}.                    \tag{A.9}
\]
Indeed \(g_j^T\delta^{(2)}=q_j^{(1)}\), and subtracting the
increment derivative leaves exactly the initialized-column pairing.
The preceding compact feature-time bounds imply
\(\sqrt n\|p_j(s)\|_2\le\int_0^s\|\delta^{(2)}(v)\|_2/\sqrt n\,dv\le C_S\)
uniformly in \(j\), and \(\|\bar q^{(1)}(s)\|_2/\sqrt n\le C_S\).
Minkowski applied to the integrated second identity proves
\[
 \sup_{s\le S}\frac{\|\Phi(u(s))\|_2}{\sqrt n}
 =O_{\mathbb P,S}(1),\qquad
 \sup_{s\le S}\frac{\|\operatorname{sech}^{-2}(u(s))\|_2}{\sqrt n}
 =O_{\mathbb P,S}(1),                                  \tag{A.10}
\]
because \(E\Phi(G)^2<\infty\) and
\(\operatorname{sech}^{-2}u=1+2\Phi(u)\).
These are exact continuous-flow bounds. They do not give square tails
of the ungated reverse query: a coordinate with
\(q_j=\sqrt n\), gate \(n^{-1/2}\), and all other coordinates bounded
is compatible with bounded normalized squared norms of \(q\), gated
\(q\), and \(\Phi(u)\). Such a static comparison is not a claim of
canonical reachability. No Euler remainder estimate is inferred from
the continuous balance.

## B. Sin-plus-cosine initialization and exact initial coefficient geometry

Use \(\phi(z)=\sin z+\cos z\), three hidden layers, finitely many distinct
normalized inputs and binary labels. Set \(G_{ab}=x_a^Tx_b/d\),
\(\gamma=2/m\), and use full mean square loss with the shared raw
mobilities. Initialize first weights with variance one, hidden matrices
with variance \(1/n\), and the **stored** readout with variance
\(1/n^2\). The limiting readout is zero. The finite equations and four
kernel blocks are those of the finite-dynamics chapter with this \(\phi\).

For standard jointly Gaussian \((X,Y)\) with correlation \(\rho\),
\[
 E[\phi(X)\phi(Y)]=E[\phi'(X)\phi'(Y)]=e^{\rho-1}.       \tag{B.1}
\]
Indeed the product-to-sum identities reduce the expectations to
\(E\cos(X-Y)\); the additional sine terms vanish by simultaneous sign
symmetry. The Gaussian characteristic function gives the result. Thus
\[
 Q_1=e^{\circ(G-\mathbf1\mathbf1^T)},\quad
 Q_2=e^{\circ(Q_1-\mathbf1\mathbf1^T)},\quad
 Q_3=e^{\circ(Q_2-\mathbf1\mathbf1^T)}                  \tag{B.2}
\]
are exactly the initialized feature Grams; every diagonal is one.
Each is positive definite even if \(G\) is singular.

For the first assertion, write \(u_a=x_a/\sqrt d\) and expand
\(e^{u_a^Tu_b}\) into tensor powers. A vector in the nullspace would
satisfy \(\sum_a v_a u_a^{\otimes k}=0\) for every \(k\ge0\), hence
\(\sum_a v_aP(u_a)=0\) for every polynomial. The polynomial
\[
 P_j(u)=\prod_{k\ne j}
 \frac{(u-u_k)^T(u_j-u_k)}{\|u_j-u_k\|_2^2}
\]
is one at \(u_j\) and zero at every other sample. Thus \(v_j=0\).
For later layers use any Euclidean Gram realization of \(Q_1\), then
\(Q_2\). Its vectors are distinct because the previous Gram is
positive definite, so the same argument applies.

Here is an explicit finite Gaussian construction of all first hidden
kernel coefficients. Its independent innovations encode actual transpose
responses, not independent replacement matrices. Let
\(Z_1\sim N(0,G)\), \(Z_2\sim N(0,Q_1)\), \(Z_3\sim N(0,Q_2)\)
in their respective layers and put \(H_\ell=\phi(Z_\ell)\).
Set \(a=\gamma y\) and define
\[
 C_1=a^TH_3,\quad D_3^\mu=C_1\phi'(Z_3^\mu),\quad
 R_3^{\mu\nu}=E[D_3^\mu D_3^\nu],
\]
\[
 J_3^{\mu\alpha}=a_\alpha Q_3^{\mu\alpha}
                    -\mathbf1_{\mu=\alpha}(Q_3a)_\mu.
\]
With \(\Xi_3\sim N(0,R_3)\) independent of \(Z_2\), put
\[
 P_2=\Xi_3+J_3H_2,\quad D_2^\mu=\phi'(Z_2^\mu)P_2^\mu,
 \quad R_2^{\mu\nu}=E[D_2^\mu D_2^\nu],
\]
\[
 J_2^{\mu\alpha}=J_3^{\mu\alpha}Q_2^{\mu\alpha}
    -\mathbf1_{\mu=\alpha}\sum_\beta J_3^{\mu\beta}Q_2^{\mu\beta}.
\]
Finally let \(\Xi_2\sim N(0,R_2)\) be independent of \(Z_1\), and put
\[
 P_1=\Xi_2+J_2H_1,\quad D_1^\mu=\phi'(Z_1^\mu)P_1^\mu,
 \quad R_1^{\mu\nu}=E[D_1^\mu D_1^\nu].                \tag{B.3}
\]
Each \(R_j\) is positive definite. To prove this for \(R_3\), for
\(v\ne0\) its quadratic form is
\(E[(a^T\phi(Z_3))^2(v^T\phi'(Z_3))^2]\).
Both factors are nonzero continuous trigonometric functions whose zero
sets have empty interior: if either vanished on an open rectangle,
differentiation in each separate coordinate would force all its
coefficients to vanish. Their nonzero sets therefore intersect in an
open set. The Gaussian covariance \(Q_2\) is positive definite, so that
open set has positive probability. The quadratic form is strictly positive.
By independence and the vanishing innovation mean,
\[
 R_2=Q_2\circ R_3+
 E[(\phi'(Z_2)\odot J_3H_2)(\phi'(Z_2)\odot J_3H_2)^T],
 \quad R_1\succeq Q_1\circ R_2.                        \tag{B.4}
\]
These are positive definite. To check strictness without invoking a
Schur-product theorem, if \(Q_{ab}=u_a^Tu_b\) has positive diagonal and
\(R_{ab}=v_a^Tv_b\) is positive definite, then the vectors
\(u_a\otimes v_a\) are independent. Apply a linear functional dual to
\(v_j\) to any vanishing linear combination; it gives \(c_ju_j=0\),
hence \(c_j=0\). This also proves \(G\circ R_1\succ0\) at singular \(G\).

The expected derivative of \(D_3^\mu\) with respect to \(Z_3^\alpha\)
is exactly \(J_3^{\mu\alpha}\), using \(\phi''=-\phi\) and (B.1).
Differentiating \(\phi'(Z_2^\mu)(\Xi_3+J_3H_2)_\mu\) similarly gives
\(J_2\); the independent centered \(\Xi_3\) term has zero expectation.
The fixed source rule III.F.4 therefore proves (B.3). Its use for this
one unbounded product is legitimate by truncating \(P_2\): its scalar
law is Gaussian plus a bounded term, so the values and first source
derivatives have every finite moment. Smooth truncations converge locally
with their first derivatives; those moments dominate the derivative
remainders and pass their expectations. Finite-array RMS errors pass
through the bounded actions and bounded gates. No unbounded coordinate
instruction is silently assigned a bounded derivative.

In formal initial-time coefficient notation only, the three hidden
kernel blocks have degree-two terms
\[
 t^2(G\circ R_1),\qquad t^2(Q_1\circ R_2),\qquad
 t^2(Q_2\circ R_3),                                    \tag{B.5}
\]
respectively, and the readout block has constant term \(Q_3\).
This follows by differentiating the finite equations at zero readout:
\(\dot C(0)=C_1\), all hidden velocities vanish, and each first
backward coefficient is (B.3). It is an algebraic initialization
statement, without an analytic remainder or a constructed trajectory.
Writing \(M=G\circ R_1+Q_1\circ R_2+Q_2\circ R_3\), the label quadratic
form of the total formal kernel has coefficients
\[
 y^TK(t)y=y^TQ_3y+2t^2y^TMy+\text{terms of degree at least three}. \tag{B.6}
\]
For the readout contribution, set \(h_y=\sum_a y_aH_3^a\) and let \(J_y\) be its bounded formal hidden-parameter linearization.
No Fréchet derivative of an L²-valued activation map is asserted. Hidden acceleration is
\(\gamma^2J_y^*h_y\). Since hidden velocity is zero at initialization,
\(\frac{d^2}{dt^2}\|h_y\|^2|_0=2\gamma^2\|J_y^*h_y\|^2=2y^TMy\).
Thus that block supplies \(t^2y^TMy\), as do the three hidden blocks
combined. This proves (B.6) as a coefficient identity.

All these Gaussian integrals are explicit finite sums. For
\(Z\sim N(0,Q)\), any finite derivative orders \(r_j\), and
\(\theta_r=-\pi/4+r\pi/2\),
\[
 E\prod_{j=1}^k\phi^{(r_j)}(Z_{i_j})
 =2^{-k/2}\sum_{\varepsilon\in\{-1,1\}^k}
 \cos\!\left(\sum_j\varepsilon_j\theta_{r_j}\right)
 \exp\!\left[-\tfrac12\sum_{j,l}\varepsilon_j\varepsilon_lQ_{i_ji_l}\right].
\]
Expand each \(\sqrt2\cos(Z+\theta_r)\) into its two complex exponentials
and use the Gaussian characteristic function to verify the formula.
At a standard Gaussian marginal, orthogonal projection onto \(1,G\) gives
\[
 \inf_{b,c}E|\phi(G)-bG-c|^2=1-2/e>0,                  \tag{B.7}
\]
because \(E\phi(G)=E[G\phi(G)]=e^{-1/2}\) and \(E\phi(G)^2=1\).

A specific rejected tail claim can also be checked from one finite node.
For one input and label one, the first zero-readout Euler step of size
\(h\) has \(C_1=2hH_3(0)\) and
\(q^{(2)}_1=2h(\Gamma^{(3)})^T\cos(2z^{(3)}(0))\).
Its source response is zero, since \(E\sin(2G)=0\), so its limiting
law is \(h\sigma G\), \(\sigma^2=2(1+e^{-8})\).
An estimate \(\|q\|_p\le Kh e^{Khp}\) with one constant for all
\(p\ge2\) and small \(h\) would, by first sending \(h\downarrow0\)
at fixed \(p\), bound all Gaussian \(L^p\) norms. They are unbounded:
\(\|G\|_p\ge B\Pr(|G|>B)^{1/p}\) for every \(B\).
This disproves that estimate, not a continuous-time limit theorem.
The broader local construction, when applied with its own hypotheses,
has its own independent proof; it does not validate this rejected estimate.

## C. A fixed-offset affine reference: global flow and its fitting boundary

Let \(u_1,u_2,u_3\) be unit vectors spanning a finite-dimensional real
Hilbert space \(V\). Let \(\mathcal H_\ell=L^2(\Omega_\ell)\) be
three separate probability Hilbert spaces with constant vectors \(e_\ell=1\).
Take initialized bounded operators \(A_0:\mathcal H_1\to\mathcal H_2\),
\(B_0:\mathcal H_2\to\mathcal H_3\), and
\(W_0:V\to\mathcal H_1\). Train
\[
 W:V\to\mathcal H_1,\quad A\in A_0+\mathcal S_2,\quad
 B\in B_0+\mathcal S_2,\quad C\in\mathcal H_3,
\]
using the product Hilbert–Schmidt/readout metric. Here \(\mathcal S_2\)
denotes Hilbert–Schmidt increments between the specified spaces.
For \(\phi(z)=z+1\), define
\[
 H_{1i}=e_1+Wu_i,\quad H_{2i}=e_2+AH_{1i},\quad
 H_{3i}=e_3+BH_{2i},\quad f_i=\langle C,H_{3i}\rangle.
\]
Use \(\mathcal L=\frac12\sum_i(f_i-y_i)^2\) and \(r=f-y\).
Let \(Xv=\sum_i v_i u_i\), \(H_\ell v=\sum_i v_iH_{\ell i}\),
\(G=X^*X\), \(Q_\ell=H_\ell^*H_\ell\),
\(q_2=B^*C\), and \(q_1=A^*q_2\). The exact raw flow is
\[
 \dot C=-H_3r,\quad \dot B=-C\otimes H_2r,\quad
 \dot A=-q_2\otimes H_1r,\quad \dot W=-q_1\otimes Xr.    \tag{C.1}
\]

**Global given-space theorem.** For every finite initial state of this
form and every real label vector, (C.1) has a unique global strong \(C^1\)
solution, with restart from every reached state. In particular, with
\(C(0)=0\) and binary labels,
\[
 \int_s^t\|\dot\theta(v)\|_{raw}^2dv=\mathcal L(s)-\mathcal L(t),
 \quad
 \|\theta(t)-\theta(s)\|_{raw}
 \le\sqrt{(t-s)[\mathcal L(s)-\mathcal L(t)]}
 \le\sqrt{3(t-s)/2}.                                  \tag{C.2}
\]

To prove it, bounded bilinear action, adjunction and rank-one multiplication
make each component of (C.1) a polynomial map on the raw Hilbert space,
locally bounded and Lipschitz on balls. On a ball with field bound \(M\)
and Lipschitz bound \(L\), Picard's integral map is a contraction for
\(tM\) below its radius and \(tL<1\). Its uniformly convergent iterates
construct the local solution. Direct differentiation of the finite sum of
squared scalar predictions gives
\(\dot{\mathcal L}=-\|\dot\theta\|_{raw}^2\).
Cauchy–Schwarz gives (C.2), with \(\mathcal L(0)\) in place of \(3/2\)
for general initialization. At a hypothetical finite maximal endpoint,
(C.2) gives a strong Cauchy endpoint in this complete affine Hilbert
space. The local contraction at that endpoint extends the solution,
a contradiction. Uniqueness and restart follow from the same local
Lipschitz estimate.

In the canonical initialized Gaussian action spaces, \(W_0\) is an
isometry on \(V\), its image is orthogonal to \(e_1\), and the first
Gaussian feature covariance is \(G\). Successive fresh centered forward
calls, followed by adding the constant one, give exactly
\[
 Q_\ell(0)=G+\ell\mathbf1\mathbf1^T\quad(\ell=1,2,3).  \tag{C.3}
\]
This uses just the fixed initial programs of III.F. Since \(C(0)=0\),
the initial total kernel is \(Q_3(0)\).

Differentiating (C.1) gives
\[
 \dot H_1=-q_1r^TG,\quad
 \dot H_2=-q_2r^TQ_1-Aq_1r^TG,
\]
\[
 \dot H_3=-Cr^TQ_2-BB^*Cr^TQ_1-BAA^*B^*Cr^TG.
\]
Thus
\[
 K=Q_3+\|C\|^2Q_2+\|q_2\|^2Q_1+\|q_1\|^2G,
 \qquad \dot r=-Kr.                                   \tag{C.4}
\]
There is also a useful full augmented-Gram lower bound:
\[
 K\succeq
 \frac{\|q_1\|^2}{1+2\|W\|_{op}^2+2\|A\|_{op}^2}
                      (G+\mathbf1\mathbf1^T).          \tag{C.5}
\]
For any \(v\in\mathbb R^3\), put \(d=Xv\), \(s=\sum_i v_i\).
The first two summands of the raw squared gradient give
\(v^TKv\ge\|q_1\|^2\|d\|^2+\|q_2\|^2\|Wd+se_1\|^2\).
Furthermore
\(s^2\le2\|Wd+se_1\|^2+2\|W\|^2\|d\|^2\), and
\(\|q_1\|\le\|A\|\|q_2\|\). Multiplying the last two estimates by
the coefficient in (C.5) proves that its right-hand quadratic form
is bounded by those first two gradient terms. This includes \(q_1=0\)
without division by \(q_1\) or \(A\).

The offsets create exact defects in homogeneous balance laws. If
\(s_r=\sum_i r_i\), product differentiation gives
\[
 \frac d{dt}(A^*A-WW^*)=-s_r(e_1\otimes q_1+q_1\otimes e_1),
\]
\[
 \frac d{dt}(B^*B-AA^*)=-s_r(e_2\otimes q_2+q_2\otimes e_2),
 \quad
 \frac d{dt}(C\otimes C-BB^*)=-s_r(e_3\otimes C+C\otimes e_3).
                                                               \tag{C.6}
\]
For example \(H_1r=WXr+s_re_1\); subtracting the differentiated
\(WW^*\) from \(A^*A\) cancels precisely the \(WXr\) terms.
The other two equations use the corresponding identity at their layer.
Compress each equation on both sides by
\(P_\ell=I-e_\ell\otimes e_\ell\). Its right side vanishes, proving
three projected balance invariants. Full balances need not be constant.
Training a homogeneous augmented matrix would train the fixed offset
columns as well, and would change (C.1).

Suppose now that the three unit inputs are distinct. Then
\(G+\mathbf1\mathbf1^T\succ0\): the vectors \((u_i,1)\) are independent.
Indeed dependence would make the three points affinely collinear, but a
line intersects a unit sphere in at most two points, as follows by
substituting the line into the quadratic norm equation. At every stationary
raw state the predictor is either zero, exactly \(y\), or the constant
\((\sum_i y_i)/3\). If \(C=0\), it is zero. Otherwise stationarity of
\(B\) gives \(H_2r=0\), and stationarity of \(C\) then gives
\(s_r=0\). If \(q_1\ne0\), stationarity of \(W\) gives \(Xr=0\);
augmented independence forces \(r=0\). If \(q_1=0\), expand
\[
 f_i=\langle C,e_3\rangle+\langle q_2,e_2\rangle
      +\langle q_1,e_1\rangle+\langle q_1,Wu_i\rangle.
\]
It is constant and \(s_r=0\) identifies its value. For binary labels,
the possible stationary losses are zero, \(3/2\), and, for mixed
labels, \(4/3\). At canonical initialization
\(-\dot{\mathcal L}(0)=y^T(G+3\mathbf1\mathbf1^T)y\ge3\).
This initial decrease does not imply crossing below \(4/3\).

A conditional fitting implication makes that gap precise. Suppose the
canonical reference has **positive raw Gram** \(G\succeq\lambda I\),
\(\lambda>0\), mixed binary labels, and at some time its loss is
at most \(4/3-\epsilon_0\), with \(0<\epsilon_0\le4/3\).
Until residual zero, introduce its residual-length clock
\[
 u(t)=\int_0^t\|r(v)\|_2dv,\qquad R(u)=\|r(t(u))\|_2.
\]
The raw gradient identity gives
\[
 R_u=-\|\theta_u\|_{raw}^2,\quad
 \int_0^u\|\theta_v\|_{raw}^2dv\le\sqrt3,\quad
 \|\theta(u)-\theta(0)\|_{raw}^2\le\sqrt3u.             \tag{C.7}
\]
These follow from \(\mathcal L=R^2/2\),
\(\theta_u=-\nabla\mathcal L/R\) and Cauchy–Schwarz.
Let \(P\) project off the constant sample vector and set
\(\nu=\sqrt{8/3}-\sqrt{8/3-2\epsilon_0}>0\).
For mixed binary labels \(\|Py\|=\sqrt{8/3}\), so monotonicity of loss
implies \(\|Pf\|\ge\nu\) thereafter. The predictor formula yields
\[
 \nu\le\|X\|\|W\|\|q_1\|\le\sqrt3\|W\|\|q_1\|.
\]
By (C.7) and \(\|W_0\|=1\),
\(\|W\|^2\le(1+3^{1/4}\sqrt u)^2\le4(1+u)\).
Thus, writing \(u_0\) for the entry clock,
\[
 K\succeq\frac{\lambda\nu^2}{12(1+u)}I,
 \quad R_u=-\frac{r^TKr}{\|r\|^2}
       \le-\frac{\lambda\nu^2}{12(1+u)}\quad(u\ge u_0).
\]
Integrating until any admissible clock gives
\[
 1+u_\infty\le(1+u_0)
       \exp\!\left(\frac{12R(u_0)}{\lambda\nu^2}\right). \tag{C.8}
\]
Otherwise the integrated upper bound for the nonnegative \(R\) would
be negative. The finite clock and (C.7) give a strong endpoint and a
bounded raw path. On that clock the displayed kernel lower bound is
uniformly positive; \(\dot R\le-cR\) proves exponential fitting in
physical time. If the residual reaches zero earlier the state is stationary
and the same conclusions hold.

Neither raw-Gram positivity with a uniform margin nor entry below the
mixed-label level follows from pairwise input separation. Hence (C.8)
is conditional, and no positive-nonlinearity theorem for
\((1-\theta)(z+1)+\theta\arctan z\) is inferred.


## D. Same-array Gaussian values under causal response bounds

This finite-array lemma is an auxiliary implication. Its coefficients and
Gaussian covariance belong to the **same actual source program**. It does
not estimate those response coefficients from a neural energy bound.

Fix \(0=t_0<\cdots<t_N\le S\), write \(h_j=t_{j+1}-t_j\), and use
three-dimensional sample blocks with induced maximum norm. Let \(A\) be
strictly lower triangular and \(B\) lower triangular block arrays, with
\[
 \|A_{kj}\|_\infty\le\alpha h_j\ (j<k),\qquad
 \sup_k\sum_{j\le k}\|B_{kj}\|_\infty\le b.             \tag{D.1}
\]
All coefficients are deterministic. Let \(\xi,\zeta\) be jointly centered
finite Gaussian arrays with any positive semidefinite covariance; the two
groups need not be independent. Fix \(0<\varepsilon\le1/2\),
\(a=1-\varepsilon\), and coordinate clips satisfying
\(|\tau_R(q)|\le|q|\). Suppose the source equations are
\[
 Z=\xi+Ad,\quad q=\zeta+BH,\quad
 H=aZ+\varepsilon\arctan Z,\quad
 d=aq+\varepsilon(1+Z^2)^{-1}\tau_R(q).                 \tag{D.2}
\]
Strict causality makes this a finite recursion: first determine \(Z_k\)
from the past, then \(H_k,q_k,d_k\). Suppose also that the **actual**
fields obey \(\max_{k,i}\|q_{ki}\|_2\le Q\) and
\(\max_{k,i}\|Z_{ki}\|_2\le F\).

Set
\[
 E=\exp(a^2\alpha bS),\quad k_0=\varepsilon a\alpha bE,
 \quad d_0=\varepsilon(\pi/2)bE,\quad
 V=Q(1+k_0S)+d_0,
 \quad M=(4V+d_0)e^{k_0S}.                            \tag{D.3}
\]
Then, for every \(p\ge2\),
\[
 \max_{k,i}\|q_{ki}\|_p\le M\sqrt p.                   \tag{D.4}
\]
Moreover, with
\(V_Z=F+\varepsilon\alpha ESQ+\varepsilon a(\pi/2)\alpha bES\),
\[
 \max_{k,i}\|Z_{ki}\|_p
 \le[4V_Z+\varepsilon\alpha ESM
          +\varepsilon a(\pi/2)\alpha bES]\sqrt p.      \tag{D.5}
\]
The constants are independent of cap, number of nodes and minimum mesh
step. There is no smallness assumption on \(\varepsilon S\), but the
constants can grow rapidly with \(S\).

*Proof.* The strictly lower triangular arrays \(AB\) and \(BA\) are
nilpotent, so define
\[
 \mathcal R=(I-a^2AB)^{-1},\quad
 \mathcal T=(I-a^2BA)^{-1},\quad U=\mathcal RA.
\]
Their complete block-row norms are at most \(E\). Here is a check that
also permits concentrated old columns of \(B\). Replace each block by
its nonnegative scalar norm and bound products by the corresponding
products of scalar majorants. For \(AB\), the equation for its inverse
acting on the all-ones vector gives the running-maximum inequality
\[
 x_k\le1+a^2\alpha b\sum_{j<k}h_j\max_{r\le j}x_r.
\]
Induction bounds this by \(\prod_j(1+a^2\alpha bh_j)\le E\).
For \(BA\), its strict \((k,j)\) block has norm at most
\(b\alpha h_j\), so the same induction applies directly. Thus
\[
 \|U_{kj}\|_\infty\le\alpha Eh_j,\quad
 \|(BU)_{kj}\|_\infty\le b\alpha Eh_j\quad(j<k),
 \quad \|\mathcal TB\|_{row}\le bE.                   \tag{D.6}
\]
The last assertion also follows from \(\mathcal TB=B\mathcal R\).
There is no assertion that \(AB\) itself has a column-density bound
\(\alpha bh_j\).

Put \(r_Z=\arctan Z\) and \(v=(1+Z^2)^{-1}\tau_R(q)\).
Eliminating (D.2) at these fixed arrays gives
\[
 Z_G=\mathcal R\xi+aU\zeta,\quad
 q_G=\mathcal T\zeta+aB\mathcal R\xi,
\]
\[
 Z-Z_G=\varepsilon Uv+\varepsilon aUB r_Z,
 \quad q-q_G=\varepsilon aBUv+\varepsilon\mathcal TB r_Z. \tag{D.7}
\]
These Gaussian parts use the actual coefficients and covariance; they
are not coefficients recomputed for an affine trajectory.
Since \(|v|\le|q|\) and \(|r_Z|\le\pi/2\), (D.6) and the actual
second-moment bound give \(\|(q_G)_{ki}\|_2\le V\).
No independence from the nonlinear remainder is needed.
For a scalar centered Gaussian of standard deviation at most \(V\),
\(\|G_V\|_p\le4V\sqrt p\). For example,
\(E\exp(G_V^2/(4V^2))\le\sqrt2\), while maximizing
\(x^p\exp[-x^2/(4V^2)]\) bounds its \(p\)-th moment by a constant
at most \((4V\sqrt p)^p\); \(V=0\) is immediate.

Taking each marginal \(L^p\) norm in the second identity of (D.7)
and writing \(m_k=\max_i\|q_{ki}\|_p\) gives
\[
 m_k\le4V\sqrt p+d_0+k_0\sum_{j<k}h_jm_j.
\]
Its induction solution is bounded by
\((4V\sqrt p+d_0)\prod_j(1+k_0h_j)\le M\sqrt p\), proving (D.4).
The first identity in (D.7) gives \(\|(Z_G)_{ki}\|_2\le V_Z\).
Apply the same Gaussian moment estimate, then (D.4) to its \(Uv\)
term, to obtain (D.5). Also \(|aZ+\varepsilon\arctan Z|\le|Z|\),
so the forward feature has the same moment bound.

A \(C\sqrt p\) bound gives an exponential-square tail, for instance
by expanding \(E\exp(|q|^2/K^2)\) and using the \(p=2j\) moments
with \(K\) sufficiently larger than \(C\); the ratio of consecutive
majorants is then below one. Uniform versions of (D.1) and the actual
second-moment premises therefore yield uniform Gaussian value tails.
Neither (D.1) nor the second-moment premise for nongradient caps is
proved by this lemma. Their continuation at arbitrary physical time,
and the finite-algorithm and full-observable identifications, remain
separate obligations in a nonlinear application.


### D.1. Related initialization and exact residual-coordinate identities

For three unit inputs with \(|G_{ij}|\le1-\delta\) when \(i\ne j\),
\(0<\delta\le1\), at most one eigenvalue of \(G\) is below \(\delta\).
Indeed every two-coordinate principal restriction has minimum eigenvalue
at least \(\delta\). If the two smallest eigenvalues of \(G\) were
both below \(\delta\), their two-dimensional eigenspace would intersect
any two-coordinate plane in a nonzero vector whose Rayleigh quotient
is below \(\delta\), a contradiction. Write eigenvalues increasingly;
then \(\lambda_2(G)\ge\delta\).

Use \(\phi(z)=az+\varepsilon\arctan z\) and the parameters of (D.2),
with unit initial feature variance at layer zero and zero population
readout. At an initial Gaussian layer whose common preactivation variance
is \(q_{\ell-1}>0\), put
\[
 \beta_\ell=\frac{E[Z_i\arctan Z_i]}{q_{\ell-1}}
            =E\frac1{1+q_{\ell-1}G_0^2},\qquad
 c_\ell=a+\varepsilon\beta_\ell\in[a,1],
\]
where \(G_0\) is standard normal. Gaussian integration by parts gives
the equality. Let \(R_\ell\) be the Gram of
\(\arctan Z_i-\beta_\ell Z_i\). Gaussian regression gives orthogonality
of each residual to every \(Z_j\), even at singular covariance: write
\(Z_j=(E[Z_iZ_j]/q_{\ell-1})Z_i+N\), with independent centered
Gaussian remainder. Thus the exact initial recurrence is
\[
 Q_\ell=c_\ell^2Q_{\ell-1}+\varepsilon^2R_\ell,
 \qquad R_\ell\succeq0,
 \qquad\|R_\ell\|_{op}\le\operatorname{tr}R_\ell\le3.  \tag{D.8}
\]
The last bound uses \(|\phi(z)|\le|z|\) to bound every initial variance
by one, and orthogonal projection to bound each residual second moment
by \(E(\arctan Z_i)^2\le E Z_i^2\). Variances remain positive because
\(|\phi(z)|\ge a|z|\). Iterating three layers gives
\[
 K(0)=Q_3=\kappa G+\varepsilon^2R,\quad
 \kappa=c_1^2c_2^2c_3^2\in[a^6,1],\quad 0\preceq R\preceq9I.
                                                               \tag{D.9}
\]
The equality with the full initial kernel uses zero readout, which makes
all hidden raw gradients zero at initialization.

In a fixed eigenbasis of \(G\), split off its weakest direction from
the other two. The corresponding blocks obey
\[
 K_{ff}(0)\succeq a^6\delta I_2,\quad
 \|K_{fs}(0)\|\le9\varepsilon^2,\quad
 \|K_{ff}(0)^{-1}K_{fs}(0)\|
       \le9\varepsilon^2/(a^6\delta).                  \tag{D.10}
\]
These are initialized bounds, not invariants of training.

For any already existing raw strong flow with \(\dot r=-Kr\), use
that same fixed basis and assume \(K_{ff}\) invertible. Define
\(L=K_{ff}^{-1}K_{fs}\), \(z=r_f+Lr_s\), and
\(\sigma=K_{ss}-K_{sf}L\). If \(L\) is absolutely continuous,
substitution and the product rule give almost everywhere
\[
 \dot r_s=-\sigma r_s-K_{sf}z,
 \qquad
 \dot z=-(K_{ff}+LK_{sf})z+(\dot L-L\sigma)r_s.         \tag{D.11}
\]
In particular the derivative of the moving coupling cannot be omitted.
Also, if a hidden feature operator \(H_f\) has invertible readout Gram
\(Q_{ff}=H_f^*H_f\), the constraint \(H_f^*C=y_f\) implies
\[
 C=H_fQ_{ff}^{-1}y_f+C_\perp,
 \quad
 f_s=Q_{sf}Q_{ff}^{-1}y_f+
           \langle C_\perp,(I-P_{H_f})h_s\rangle.        \tag{D.12}
\]
This follows by orthogonal projection onto \(\operatorname{ran}H_f\).
Both the offset and the orthogonal subspace generally depend on hidden
parameters. Equations (D.10)–(D.12) do not supply a positive trained Schur
lower bound, coupling-variation control or a scalar autonomous closure.

## E. Actual positive-time failure of raw-Hilbert local Lipschitzness

This result concerns three hidden layers and two normalized inputs of
correlation \(-1\le\rho<1\), with either binary label pair. Use the
single activation
\[
 \phi(z)=1+\tfrac1{10}\arctan(\sinh z),\quad
 \phi'(z)=\tfrac1{10}\operatorname{sech}z,\quad
 \phi''(z)=-\tfrac1{10}\operatorname{sech}z\tanh z.
\]
The separate layer Hilbert spaces, independent canonical Gaussian
initialization and true adjoints are those of special-data Part II:
first-weight variance one, hidden-matrix variance \(1/n\), and stored
readout variance \(1/n^2\), with zero limiting initial readout.
The loss in this fragment is the **sum**
\(\mathcal L=\sum_{a=1}^2(f_a-y_a)^2\), not its mean.
Raw population increments have the first-row \(L^2\), two
Hilbert–Schmidt, and readout \(L^2\) product metric of III.F.8.
The first sample-field metric is
\(E[v^TG^{-1}v]\) when \(|\rho|<1\), where
\(G=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}\);
at \(\rho=-1\), it is the one-field metric on \((v,-v)\).

**Theorem.** There is \(S_0>0\), depending on this fixed data and label
pair, such that at every fixed feature time \(0<S\le S_0\), every
sample \(a\), every real interval \(I\) of positive length, and each
sign \(\sigma\),
\[
 \Pr\{Z_a^{(2)}(S)\in I,\ \sigma q_a^{(2)}(S)>R\}
 \ge c_I\exp[-C_I(R+1)^2]\quad(R\ge1),                 \tag{E.1}
\]
with positive finite constants. Here
\(q_a^{(2)}=(W^{(3)})^*\Delta_a^{(3)}\) is the actual reached middle
query. At each such state, the scalar loss has second directional
derivatives of both signs unbounded over raw unit directions. These
are individually bounded rank-one perturbations of \(W^{(2)}\).
Consequently its raw Hilbert gradient is not locally Lipschitz there.
These states lie on an already constructed unique local population flow;
this is not a nonexistence or nonuniqueness result.

### E.1. The contained local construction and its exact source interface

Only value, slope and curvature bounds were used in the numerical
induction II.B:
\[
 5/6<\phi<7/6,\quad0<\phi'\le1/10,\quad|\phi''|\le1/5.
\]
They hold for the present activation since \(|\arctan(\sinh z)|<\pi/2<5/3\).
Its fixed higher derivatives are bounded, by differentiating the
polynomials in \(\operatorname{sech}z,\tanh z\). The bottom raw-sensitivity
estimate II.B.6 uses the gate bound \(1/10\), curvature bound \(1/5\),
and \(|G_{ab}|\le1\). The middle and top derivatives II.B.10–II.B.16
use precisely those same bounds and \(|W^{(4)}(s)|\le(7/6)s\).
Their induction order and constants therefore remain valid with no
arctangent change of variables. This proves on \([0,3/2]\)
\[
 \max_{k,a}\sum_{r\le k,b}|B^{(3)}_{ka,rb}|<1,\quad
 \max_{k,a}\sum_{r\le k,b}|B^{(2)}_{ka,rb}|<97/100,
 \quad |A^{(\ell)}_{ka,rb}|\le3\Delta/4\ (r<k).        \tag{E.2}
\]
It also proves \(E\exp[(q_a^{(j)})^2/16]\le2\) for both reverse queries
in every fixed-cap Euler law. These are actual source coefficients:
all learned memories and both transpose response terms remain those
of II.B.1–II.B.2.

The common generated actions follow from III.F.1–III.F.7, whose fixed-cap
coordinate maps have bounded derivatives after the readout is truncated
outside its already proved bound. II.C.1–II.C.2 then apply verbatim:
primal bounds are cap independent; the two-query asymmetric comparison
costs \(C(1+R)\) once and the two reference tails are at most
\(32e^{-R^2/256}\). Its bound \(Ce^{CR-R^2/256}\) constructs the strong
uncut flow on \([0,3/2]\), identifies its raw velocities and
Hilbert–Schmidt increments, and proves uniqueness and reached-state
restart on that interval. This transfer uses neither the same-label
fitting lower bound nor any cubic-jet/sign-change statement.
The fixed-cap Euler laws converge first as their proof mesh vanishes;
the cap is removed afterwards. Those two strong limits include all
named terminal fields and their second moments.

For clarity, write the local feature equations and the exact middle
source interface explicitly. In the following proof, local equation
numbers (1)–(24) are confined to this fragment. Set
\(g=\frac12\sum_a y_af_a\) and use \(\theta'=\nabla g\), so
\[
 (Z_b^{(1)})'=\tfrac12\sum_aG_{ba}y_a\Delta_a^{(1)},\quad
 (W^{(\ell)})'=\tfrac12\sum_a y_a\Delta_a^{(\ell)}\otimes H_a^{(\ell-1)},
 \quad (W^{(4)})'=\tfrac12\sum_a y_aH_a^{(3)}.          \tag{1}
\]
Here \(\ell=2,3\),
\(\Delta_a^{(3)}=W^{(4)}\phi'(Z_a^{(3)})\),
\(\Delta_a^{(2)}=\phi'(Z_a^{(2)})q_a^{(2)}\), and
\(\Delta_a^{(1)}=\phi'(Z_a^{(1)})(W^{(2)})^*\Delta_a^{(2)}\).
The proof below uses \(\delta\) as a local synonym for these population
backward fields, and \(a_+=7/6\) as the uniform activation bound,
written simply \(a\) when it is not a sample subscript.

For the fixed mesh \(t_k=k\Delta\) and two scalar one-Lipschitz odd
caps \(\tau_Q\), the second-population law is
\[
 Z^{(2)}_{ka}=\xi_{ka}+\sum_{r<k,b}A_{ka,rb}\delta^{(2)}_{rb},\quad
 q^{(2)}_{ka}=\zeta_{ka}+\sum_{r\le k,b}B_{ka,rb}H^{(2)}_{rb},
\]
\[
 H^{(2)}_{ka}=\phi(Z^{(2)}_{ka}),\qquad
 \delta^{(2)}_{ka}=\phi'(Z^{(2)}_{ka})\tau_Q(q^{(2)}_{ka}). \tag{2}
\]
The complete **centered** Gaussian groups \(\xi,\zeta\) are independent;
all within-group time/sample correlations, including singular ones,
are retained. Their deterministic arrays obey
\[
 |A_{ka,rb}|\le(3/2)\Delta/2\ (r<k),\quad
 \sup_{k,a}\sum_{r\le k,b}|B_{ka,rb}|\le1,              \tag{3}
\]
\[
 E\xi_{ka}\xi_{rb}=E[H^{(1)}_{ka}H^{(1)}_{rb}],\qquad
 E\zeta_{ka}\zeta_{rb}=E[\delta^{(3)}_{ka}\delta^{(3)}_{rb}]. \tag{4}
\]
Source variations hold every coefficient and covariance fixed. The
actual fields are not claimed independent. The readout obeys
\(|W^{(4)}(s)|\le as\), with \(a=7/6\); below also put
\(c_-=5/6\), \(e=1/10\), and \(c_\phi=1/5\).

Finally the actual population trajectory has
\[
 f_a=y_ag.                                             \tag{4a}
\]
To check this for either label pair, first use a simultaneous
label/readout reversal to reduce to \(y=(1,\sigma)\). Exchange the
first sample fields and multiply the readout by \(\sigma\). All
backward fields are exchanged and multiplied by \(\sigma\); odd caps
preserve this rule. The updates are equivariant because the input
Gram commutes with sample exchange. The initial Gaussian pair is
exchangeable and the hidden matrices are unchanged. Finite predictors
therefore have the same law as \((\sigma f_2,\sigma f_1)\).
Their deterministic finite-program limits, followed by the two strong
limits above, give (4a). No samplewise finite-width clock is assumed.
The full-loss physical clock is consequently \(ds/dt=4(1-g)\).

### E.2. Lower tails and the full-loss obstruction

In the following detailed proof, its claimed probability event is
\[
 \Pr\{Z_a^{(2)}(S)\in I,\ \sigma q_a^{(2)}(S)>R\}
          \ge c_Ie^{-C_I(R+1)^2},                      \tag{5}
\]
and the corresponding signed curvature multiplier is
\[
 y_a\phi''(Z_a^{(2)}(S))q_a^{(2)}(S).                  \tag{6}
\]

#### Gaussian path bound uniform in mesh and cap

First verify a temporal covariance estimate for zeta using only primal
bounds. In a finite raw Euler system on [0,3/2], with initial hidden
operator norms at most 10, readout increments are bounded coordinatewise
by a Delta. Current readout is at most as. Successively bounding the
rank-one increments gives deterministic bounds for both hidden operator
norms. The top delta has RMS at most eaS; hence q^(2), delta^(2),
q^(1), and the bottom raw Euler velocity have bounded RMS, independently
of either cap, since |tau_Q(q)|<=|q|.

Therefore between adjacent nodes the RMS changes of each raw first
field are at most C Delta, and matrix increments have operator norm at
most C Delta. For each forward layer use the exact split

  W_(k+1)h_(k+1)-W_k h_k
       =(W_(k+1)-W_k)h_(k+1)+W_k(h_(k+1)-h_k).

Bounded features, bounded gates, and the preceding RMS increment show
that all forward preactivations change by at most C Delta in RMS.
Finally split the top delta difference into the readout difference
times the new gate and the old bounded readout times the gate difference.
Its RMS is at most D Delta for a deterministic D. Telescoping gives

  ||delta^(3)_(k,a)-delta^(3)_(j,a)||_2 <= D|t_k-t_j|.     (7)

At fixed mesh and caps the empirical second moments converge to the
finite Gaussian program. The initial norm event has probability tending
to one, so (7) passes to that law. Constants are uniform in mesh/caps.
The covariance rule (4) now gives

  (E|zeta_(k,a)-zeta_(j,a)|^2)^(1/2) <= D|t_k-t_j|,
  zeta_(0,a)=0.                                         (8)

Linearly interpolate this FINITE Gaussian array between its nodes.
Its increments still obey (8), by adding within-cell and full-cell
increments and the triangle inequality in L2. It is a continuous
Gaussian process; no limiting Gaussian path theorem is being assumed.

We use this elementary estimate: if a centered continuous finite-dimensional
Gaussian process G on [0,S] starts at zero and has increment standard
deviation at most D|t-u|, then

  (E sup_(t<=S)|G(t)|^2)^(1/2) <= C D S.                (9)

To prove it, approximate each time by its successive dyadic left
endpoints. Continuity expresses G(t) as the sum of its dyadic increments
(include the endpoint S in the level-zero bound). At level j there are
at most 2^(j+1) increments, each of standard deviation at most DS2^(-j).
For N centered Gaussians, not necessarily independent, of variance at
most v^2, the exponential-moment Gaussian bound and a union bound give
P(max|G_i|>u)<=min(1,2N exp(-u^2/(2v^2))). Integration of this bound
gives E max|G_i|^2<=2v^2(log(2N)+1). Minkowski's inequality and
sum_j 2^(-j)sqrt(j+1)<infinity prove (9). Applying it to both samples
costs only a fixed factor. The same proof works for any orthogonal
Gaussian residual after projecting onto a single scalar Gaussian:
projection can only decrease increment variances.

#### A large reverse source with controlled whole path

Fix S>0 sufficiently small for the following elementary nondegeneracy.
At initialization the first feature Gram is positive definite: if
|rho|<1 this follows from positive Gaussian density and nonconstant phi;
if rho=-1, the features are 1+b(G),1-b(G) with nonconstant odd b.
The next two Gaussian forward pairs are consequently nondegenerate,
and their feature Grams are positive definite by the same argument.
Thus V_0=(1/2)sum_a y_a H^(3)_(0,a) has positive squared norm for
either label mode. From (1), W^(4)(S)/S tends in L2 to V_0.
Choose S_0 so small that W^(4)(S) is nonzero in L2 for every
0<S<=S_0, the first feature Gram remains positive definite, and |g(S)|<1/2.
Strict positivity of phi' then implies

  v_a(S)=E[(delta^(3)_a(S))^2]>0.                       (10)

For this fixed S, cut removal and then fixed-cap mesh convergence give
E[(delta^(3)_(M,a))^2]>=v_0:=v_a(S)/2>0 for every sufficiently large
common cap and then every sufficiently fine mesh Delta=S/M. Its upper
bound is v_1=(eaS)^2. Thresholds may depend on S and the configuration;
all estimates below depend only on v_0,v_1,D and fixed constants, not
on the subsequently chosen cap or mesh.

Put X=zeta_(M,a), v=E X^2. For every source coordinate write its exact
Gaussian regression as

  zeta_(k,b)=c_(k,b) X+G_res_(k,b),
  c_(k,b)=E[zeta_(k,b)X]/v.                              (11)

The entire residual array G_res is independent of X: the joint Gaussian
characteristic function factors because all its covariances with X
are zero. This remains valid for singular source covariances. By
Cauchy--Schwarz, |c_(k,b)|<=eaS/sqrt(v_0). The interpolated residual
starts at zero and inherits increment estimate (8). Equation (9) and
Markov's inequality give a constant B_0 such that

  P(max_(k,b)|G_res_(k,b)|<=B_0)>=1/2.                      (12)

For a desired sign sigma and R>=1, restrict

  sigma X in [R+a+1,R+a+2].                             (13)

The density of N(0,v), v in [v_0,v_1], gives probability at least
c exp(-C(R+1)^2). This event is independent of (12). Call their intersection E_R; it is measurable from the reverse source
alone. It therefore has probability at least c exp(-C(R+1)^2), and on it

  max_(k,b)|zeta_(k,b)| <= B_R <= C(R+1),
  sigma q^(2)_(M,a) >= R+1.                             (14)

The second assertion uses (2)-(3) and |H^(2)|<=a, hence
|q^(2)_(M,a)-zeta_(M,a)|<=a. It holds for EVERY realization of the
independent forward source xi, not just its original realization.

#### An independent forward source places the preactivation in the interval

Condition on the complete reverse source in E_R. The query conclusion
in (14) then holds for every forward-source realization. Let
X_f=xi_(M,a). By (4), its variance v_f satisfies c_-^2<=v_f<=a^2.
Regress the whole forward source onto this scalar:

  xi_(k,b)=d_(k,b) X_f+F_(k,b),
  |d_(k,b)|<=a^2/c_-^2=:d_0,
  d_(M,a)=1, F_(M,a)=0.                                 (15)

The residual array F is independent of X_f. The whole forward group
is independent of the reverse group. Fix any value of F in its regression
support, so F_(M,a)=0; this holds almost surely under its law. Varying X_f=x
with all deterministic coefficients fixed defines a continuous finite
recursion (2), which we now control uniformly.

First, on (14), every q^(2) coordinate is bounded by B_R+a, whatever x
and F are. Thus |delta^(2)|<=e(B_R+a). The first equation in (2) gives

  |Z^(2)_(M,a)(x)-x| <= (3/2)S e(B_R+a)=:D_R<=C(R+1). (16)

The cancellation of F_(M,a) in (15) is essential here; no bound on F is
needed. For two values x,x', put E_k=max_(j<=k,b)|Z_(j,b)(x)-Z_(j,b)(x')|.
The second equation in (2) and the gate Lipschitz bound imply

  |q_(r,b)(x)-q_(r,b)(x')|<=e E_r,
  |delta_(r,b)(x)-delta_(r,b)(x')|
                  <=[c_phi(B_R+a)+e^2]E_r=:L_R^0 E_r.      (17)

This uses the cutoff's one-Lipschitz property for the query difference
and |tau_Q(q)|<=|q| for the separate gate difference; no derivative of
A,B or a covariance is taken. Equation (3) then gives

  E_k <= d_0|x-x'|+(3/2)Delta L_R^0 sum_(r<k)E_r,
  E_M <= d_0 exp((3/2)S L_R^0)|x-x'|=:L_R|x-x'|,
  1<=L_R<=C exp(C(R+1)).                                (18)

The middle inequality follows by induction from
(1+(3/2)Delta L_R^0)^k<=exp((3/2)t_k L_R^0).

Choose a fixed closed interval [b-h,b+h] inside the interior of I,
where h>0. By (16), at x=b-D_R-1 the output Z_(M,a)(x) is at most b-1;
at x=b+D_R+1 it is at least b+1. The intermediate value theorem gives
x_0 in that bounded interval with Z_(M,a)(x_0)=b. For

  |x-x_0|<=r_R:=min(1/2,h/(2L_R)),

the output lies in [b-h/2,b+h/2]. No measurable selection of x_0 is
required: the measurable preimage of this fixed closed interval has
Gaussian measure at least that of one such interval. All these x lie
in |x|<=|b|+D_R+3/2, and r_R>=c exp(-C(R+1)).

The density of X_f, with variance in [c_-^2,a^2], is bounded below there
by

  (sqrt(2pi)a)^(-1)
    exp[-(|b|+D_R+3/2)^2/(2c_-^2)].

Therefore, conditionally on ANY F and ANY reverse source in E_R,

  P{Z^(2)_(M,a) in [b-h/2,b+h/2] | F,zeta}
                           >=c exp(-C(R+1)^2).          (19)

Together with (14), this proves uniformly in the relevant caps/meshes

  P{Z^(2)_(M,a) in [b-h/2,b+h/2],
                         sigma q^(2)_(M,a)>=R+1}
                           >=c exp(-C(R+1)^2).          (20)

The constants may be enlarged when multiplying the two lower bounds.
Singular time/sample covariances never cause an inverse-Gram problem:
only the scalar variances v and v_f, explicitly bounded away from zero,
were divided by.

#### Passage to the actual local population law

For fixed sufficiently large cap, let Delta=S/M tend to zero. The joint
law of the two named terminal coordinates converges to that of the cut
flow. The event in (20) is closed in R^2, so its limiting probability is
at least the limsup of the preceding probabilities. This elementary
closed-set inequality follows by dominating its indicator by continuous
functions max(0,1-j dist(x,F)), then letting j tend to infinity.
Next send the cap to infinity, using the joint strong local convergence
and the same closed-set inequality. Constants in (20) do not depend on
either limit. The resulting event lies inside the event in (5), because
its query threshold is R+1 and its preactivation interval lies in I.
This proves (5) along the actual uncut local flow.

For (6), fix a closed interval inside (1,2). There phi'' has one sign
and its absolute value is between two positive finite constants, since
phi''=-0.1 sech(z)tanh(z). Apply (5) with the appropriate query sign and
threshold divided by the lower derivative bound. Its Gaussian lower
bound follows. The upper bound follows from bounded phi'' and
E exp((q^(2)_a)^2/16)<=2, by exponential Markov. In particular both
essential tails are unbounded. The lower bound is not an assertion of
independence between the evolved preactivation and reverse query.

#### The full loss's second directional derivative at the reached state

Fix 0<S<=S_0 and freeze the state there. Let K_ab=E_1[H^(1)_a H^(1)_b],
positive definite by the choice of S_0. For a chosen sample a define

  B_a=(sum_b (K^(-1))_ab H^(1)_b)/sqrt((K^(-1))_aa),
  d_a=1/sqrt((K^(-1))_aa).

Then E B_a^2=1 and E[B_a H^(1)_b]=d_a 1_(a=b). For ANY bounded
second-population field v of L2 norm one, perturb ONLY W^(2) in the
rank-one direction v tensor B_a. Its Hilbert--Schmidt norm is one.
All raw first fields, W^(3) and the readout remain fixed along this
test line. The preactivation variations are

  D Z^(2)_b=d_a v 1_(a=b),
  D Z^(3)_a=d_a W^(3)[phi'(Z^(2)_a)v],
  D^2 Z^(3)_a=d_a^2 W^(3)[phi''(Z^(2)_a)v^2].            (21)

The other sample is unchanged on this entire line. Because v is bounded,
its square is in L2, so the last formula makes sense. Scalar Taylor
expansion with bounded derivatives proves the second-order expansion
of H^(2) in L2. The bounded operator W^(3) transfers it to Z^(3).

At the last activation the scalar pairing has an ordinary second
derivative even though D Z^(3) need not be in L4. Write the L2 curve
there as z(t), with z'(0)=u and z''(0)=b. The first derivative of its
scalar pairing is E[W^(4)phi'(z(t))z'(t)]. In the difference quotient
of this expression at zero, the term involving (z'(t)-u)/t tends in
L2 to b. The other term pairs W^(4)u in L2 with

  [phi'(z(t))-phi'(z(0))]/t
    =[(z(t)-z(0))/t] integral_0^1
        phi''(z(0)+v(z(t)-z(0)))dv.

The first factor converges in L2 to u; the second is uniformly bounded
and converges in probability to phi''(z(0)). Truncating the fixed L2
factor proves strong L2 convergence of their product. The derivative
is E[W^(4)phi'(z(0))b]+E[W^(4)phi''(z(0))u^2]. Equivalently, for
z(t)=z(0)+tu+r_t with ||r_t||_2=O(t^2), the scalar Taylor cross
remainder is bounded by

  c_phi||W^(4)||_infinity
       (|t| ||u||_2 ||r_t||_2+||r_t||_2^2/2)=o(t^2).

The factor |t| is retained. Thus (21) gives the following exact
ordinary second directional derivative:

  D^2 g[v tensor B_a,v tensor B_a]
    =(y_a d_a^2/2)E_2[phi''(Z^(2)_a)q^(2)_a v^2]
     +(y_a d_a^2/2)E_3[W^(4)phi''(Z^(3)_a)
                           (W^(3)[phi'(Z^(2)_a)v])^2]. (22)

Adjunction in the first term uses phi''(Z^(2)_a)v^2 in L2 and the
actual delta^(3) in L2. The second term has absolute value at most

  (d_a^2/2) aS c_phi ||W^(3)||_op^2 e^2,                  (23)

uniformly over these unit directions. The first term in (22) has both
unbounded signs over that class: choose v to be the indicator of an
event where y_a phi''(Z^(2)_a)q^(2)_a exceeds any fixed level, divided
by the square root of its positive probability. Such v is individually bounded,
has L2 norm one, and its squared weight averages the multiplier over
exactly that event. No common L-infinity bound over the chosen directions
is claimed. Use the negative tail for the other sign.

The scalar predictor gradients are bounded at this fixed primal state:
forward linearization uses bounded gates/features, bounded operators and
the L2 readout; adjunction yields a finite raw gradient norm. Thus the
sum of their squared first directional derivatives is uniformly bounded
over the displayed unit directions. Equation (4a) gives f_a=y_a g at
the BASE STATE for either label configuration, not along the perturbation
line. Differentiate the full sum L=sum_a(f_a-y_a)^2 along that line and
only then substitute its base-state residuals. The exact scalar identity is

  -D^2 L[v,v]=4(1-g)D^2 g[v,v]-2 sum_a(D f_a[v])^2.      (24)

Here v in (24) denotes the full raw test direction just constructed,
not an identification of the three neuron populations. Since |g|<1/2,
(22)-(24) prove both unbounded signs of the full loss's second
directional derivative on unit directions. If its raw gradient were
Lipschitz on a neighborhood of this state with a finite constant L_0,
each such second directional derivative would have magnitude at most
L_0: pair the gradient difference along the test line with its fixed
unit direction, divide by the line parameter and pass to zero. This
contradicts the unbounded values just proved.

Finally the local physical clock is ds/dt=4(1-g)>0, so the reached
states in this theorem occur at deterministic positive physical times
t(S)=integral_0^S [4(1-g(u))]^(-1)du. This is a local statement only.
No exact samplewise finite-width clock or global physical continuation
is asserted for opposite labels.


At \(|g|<1/2\), the clock gives \(S/6\le t(S)\le S/2\),
so these are deterministic positive physical times. The theorem concerns
the actual population states, with constants allowed to depend on that
positive time and the fixed geometry. It supplies no finite-width
fixed-positive-time Hessian limit and no opposite-label global
continuation theorem. Gaussian tails coexist with the unbounded
multiplication operator, and failure of local Lipschitzness does not
contradict the strong local existence, uniqueness or restart proved above.

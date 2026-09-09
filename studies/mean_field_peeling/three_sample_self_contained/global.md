## Part G. Uniform geometry, a bounded residual clock, and global dynamics

### G.1. Separation controls the augmented input Gram

**Lemma G.1.** Under (M.1),
\[
              \Gamma+\mathbf1\mathbf1^T\succeq(\delta^2/4)I_3.
                                                               \tag{G.1}
\]
**Proof.** Put \(u_i=x_i/\sqrt d\). For a coefficient vector \(q\),
\[
 q^T(\Gamma+\mathbf1\mathbf1^T)q
             =(\sum_iq_i)^2+\|\sum_iq_iu_i\|^2 .
                                                               \tag{G.2}
\]
If the nonzero coefficients have one sign, the first term is
at least \(\sum_iq_i^2\), which suffices since \(\delta\le2\).
Otherwise, change the overall sign and permute the three indices
to write \(q=(\alpha_1,\alpha_2,-b)\), where
\(\alpha_1,\alpha_2\ge0\), \(A=\alpha_1+\alpha_2>0\), and \(b>0\).
Define
\[
 D=\{\alpha_1(1-u_1^Tu_3)+\alpha_2(1-u_2^Tu_3)\}/A
                         \in[\delta,2].
\]
The projection of \(\sum q_i u_i\) onto the unit vector \(u_3\)
is \((1-D)A-b\). Therefore (G.2) is at least
\[
 (A-b)^2+((1-D)A-b)^2
 =\begin{pmatrix}A&b\end{pmatrix}
   \begin{pmatrix}1+(1-D)^2&-(2-D)\\-(2-D)&2\end{pmatrix}
   \begin{pmatrix}A\\b\end{pmatrix}.
\]
The positive matrix has determinant \(D^2\) and trace
\(D^2-2D+4\le4\). Its smaller eigenvalue is at least its
determinant divided by its trace, hence at least \(\delta^2/4\).
Finally \(A^2+b^2\ge\alpha_1^2+\alpha_2^2+b^2\). This proves
(G.1), including all singular cases of \(\Gamma\). \(\square\)

For scale, the power \(\delta^2\) is sharp. The unit vectors
\[
 u_1=(1-\delta,\sqrt{2\delta-\delta^2}),\quad
 u_2=(1-\delta,-\sqrt{2\delta-\delta^2}),\quad u_3=(1,0)
\]
satisfy the pairwise condition for \(0<\delta\le3/2\).
For \(q=(1,1,-2+\delta)\), the quotient in (G.2) divided by
\(\|q\|^2\) is \(2\delta^2/(6-4\delta+\delta^2)\).
Only the lower bound (G.1), not this example, is used below.

### G.2. Initial features and a positive nonlinear margin

Let \(Z=(Z_1,Z_2,Z_3)\) be centered Gaussian, with a common
positive marginal variance \(v\) and covariance \(Q\).
Write \(Z=Q^{1/2}G_3\), with \(G_3\) a standard Gaussian
three-vector; a singular square root is allowed. Gaussian
integration by parts on the independent coordinates of \(G_3\)
shows that the orthogonal projection in \(L^2\) of
\(\phi(Z_i)=a+aZ_i+e\arctan Z_i\) onto constants and Gaussian
linear functions is
\[
                    a+b_vZ_i,\qquad
 b_v=a+e\,E[Z_i\arctan Z_i]/v\ge a.                         \tag{G.3}
\]
The residuals are orthogonal to both terms of every such
projection, and their Gram is positive semidefinite. Thus
\[
 E[\phi(Z)\phi(Z)^T]\succeq a^2\mathbf1\mathbf1^T+a^2Q.
                                                               \tag{G.4}
\]
All initialized sample marginals at a given layer have the
same variance, by (M.3), equal input norms, and the fresh
Gaussian forward call at that layer. With \(Q_0=\Gamma\),
iteration of (G.4) gives
\[
 K^4(0)=Q_3\succeq a^6\Gamma+(a^6+a^4+a^2)\mathbf1\mathbf1^T
                           \succeq\lambda a^6I_3,
 \qquad \lambda=\delta^2/4.                                \tag{G.5}
\]
The first preactivation variance is one. Later scalar
preactivation variances are at least one because
\(|az+e\arctan z|\ge a|z|\) for \(a\ge1,e\ge0\).

For a variable with positive variance, minimization over an
intercept and slope gives
\[
 \mathcal R(Z)=\operatorname{Var}(\arctan Z)
       -\frac{\operatorname{Cov}(Z,\arctan Z)^2}
                         {\operatorname{Var}(Z)}.             \tag{G.6}
\]
For \(G\sim N(0,1)\), \(\mathcal R(\sigma G)>0\) whenever
\(\sigma>0\): otherwise a zero \(L^2\) residual would make
arctangent affine almost everywhere under a full-support
Gaussian law, and then everywhere by continuity. Its derivative
is not constant. The expression is continuous in \(\sigma>0\)
by coupling with the same \(G\) and dominated convergence.
Symmetry and (G.6) also give
\[
 \mathcal R(\sigma G)
 =E[\arctan(\sigma G)^2]-(E[G\arctan(\sigma G)])^2
 \longrightarrow\frac{\pi^2}{4}(1-2/\pi)>0.                  \tag{G.7}
\]
For the second expectation use the integrable dominator
\(\pi|G|/2\); the limit uses \(E|G|=\sqrt{2/\pi}\).
Continuity on compact positive intervals and the positive
limit in (G.7) prove the strict positivity of \(\eta_*\)
defined in (M.21).

We will use a quantitative stability fact. Suppose
\(\operatorname{sd}(Z_0)\ge1\),
\(\mathcal R(Z_0)\ge\eta_*\), and \(\|Z-Z_0\|_2\le t_*\).
Centering is an orthogonal projection, so standard deviation
is 1-Lipschitz in \(L^2\) and \(\operatorname{sd}(Z)\ge1/2\).
The optimal arctangent regression slope at \(Z\) has magnitude
at most \((\pi/2)/\operatorname{sd}(Z)\le\pi\).
Testing its affine predictor at \(Z_0\), using the triangle
inequality and the 1-Lipschitz property of arctangent, gives
\[
 \sqrt{\mathcal R(Z_0)}
       \le\sqrt{\mathcal R(Z)}+(1+\pi)\|Z-Z_0\|_2.
\]
The definition of \(t_*\) in (M.21) therefore implies
\[
                         \mathcal R(Z)\ge\eta_*/4.          \tag{G.8}
\]
No Gaussian assumption on \(Z\) is needed in this implication.

### G.3. Controlled flows and all positive Euler meshes

Fix a smooth even function \(\chi:\mathbb R\to[0,1]\) equal
to one on \([-1,1]\) and zero outside \([-2,2]\).
For \(R>0\), put
\(\tau_R(q)=R\int_0^{q/R}\chi(v)\,dv\).
It is smooth, odd, 1-Lipschitz, equal to \(q\) on \([-R,R]\),
and satisfies \(|\tau_R(q)|\le\min(|q|,2R)\).
Use the auxiliary gate
\[
 D_R(z,q)=aq+e(1+z^2)^{-1}\tau_R(q)                         \tag{G.9}
\]
at all backward levels, leaving every forward activation
unchanged. The three auxiliary backward fields are
\[
 \delta_i^3=D_R(z_i^3,C),\quad
 q_i^2=B^*\delta_i^3,\quad \delta_i^2=D_R(z_i^2,q_i^2),\quad
 q_i^1=A^*\delta_i^2,\quad \delta_i^1=D_R(z_i^1,q_i^1).
                                                               \tag{G.10}
\]
The map \(D_R\) has bounded continuous first derivatives:
\[
 |(D_R)_q|\le a+e,\qquad |(D_R)_z|\le2eR .
                                                               \tag{G.11}
\]

For a measurable deterministic control \(c:[0,S]\to\mathbb R^3\)
with \(\|c(s)\|_1\le1\), consider the raw controlled equation
\[
 w'=d^{-1}\sum_i c_i\delta_i^1x_i,\quad
 A'=\sum_i c_i\delta_i^2\otimes h_i^1,\quad
 B'=\sum_i c_i\delta_i^3\otimes h_i^2,\quad
 C'=\sum_i c_i h_i^3.                                      \tag{G.12}
\]
Primes denote this control time, not physical time. We also use
its exact Euler updates on any positive mesh, with a control
vector of \(\ell^1\) norm at most one at each node. The affine
comparison sets \(e=0\) and uses the identical mesh and controls.

Let
\[
 D=\sqrt d\|w-w_0\|_2+\|A-A_0\|_{\rm HS}+\|B-B_0\|_{\rm HS}.
                                                               \tag{G.13}
\]
On \(D\le1\), current action norms are at most 11. Population
first projections have norms at most 2; finite initial
projection norms at most 2 give current norms at most 3.
For \(0\le e\le1\), \(|\phi(z)|\le a(3+|z|)\) and
\(|D_R(z,q)|\le2a|q|\). Direct forward and reverse propagation
therefore gives, also in finite normalized norms,
\[
 \begin{array}{c|ccc}
  &1&2&3\\ \hline
  \|h_i^\ell\|&6a&70a^2&800a^3\\
  \|\delta_i^\ell\|&
            968a^3\|C\|&44a^2\|C\|&2a\|C\|
 \end{array} .                                               \tag{G.14}
\]
For example the first backward factor is
\((2a)11(2a)11(2a)=968a^3\).
The three hidden raw speeds in (G.12) sum to at most
\[
 (968+44\cdot6+2\cdot70)a^3\|C\|
                         \le1400a^3\|C\|,
 \qquad \|C'\|\le800a^3.                                   \tag{G.15}
\]
Since the population and the affine comparator have \(C_0=0\),
integration before an exit yields
\[
 \|C(s)\|\le800a^3s,\qquad
 D(s)\le560000a^6s^2\le10^6a^6s^2.                         \tag{G.16}
\]
For Euler, \(\|C_k\|\le800a^3s_k\), and the same estimate follows
from \(\sum_{j<k}h_js_j=(s_k^2-\sum_{j<k}h_j^2)/2\).
This also rules out a first discrete overshoot: every preceding
node satisfies the stopped estimates, and their sum bounds the
alleged first exiting node strictly inside the stopping ball.

Choose \(a,S\) as in (M.21), and write
\[
 C_S=9600/(\lambda a^3),\qquad
 D_S=1.44\cdot10^8/(\lambda^2a^6).
                                                               \tag{G.17}
\]
Since \(a^6\ge6.4\cdot10^{19}\lambda^{-3}\) and
\(0<\lambda\le9/16\), these constants obey
\[
 D_S<\min\{1/2,\lambda/(3\cdot10^7)\},\quad C_S<1,\quad
                  6\cdot10^6C_S^2<\lambda/4.               \tag{G.18}
\]
The second lower bound on \(a\) in (M.21) gives
\[
             615a^2D_S\le0.08856\,t_*<t_* .                \tag{G.19}
\]
Thus every controlled prefix of duration at most \(S\)
stays in these bounds. At fixed \(R\), (G.11), forward
Lipschitzness and bounded bilinear actions give a raw field
bounded and locally Lipschitz on primal balls, uniformly in
control. The integral map is a contraction on a sufficiently
short interval, also for measurable \(c\), because its
Lipschitz bound is uniform in \(s\). Its fixed point is an
absolutely continuous strong controlled path. A strong
endpoint and the same construction continue it through \(S\).
For continuous autonomous physical controls the path is \(C^1\).

These estimates verify the affine finite-array hypothesis of
the response theorem in Part R with \(B=12\). Indeed, at finite
width the initial projection norms are at most 2 and the
initialized action norms at most 10 with probability tending
to one. Set only the auxiliary affine comparator's initial
readout to zero. Bounds (G.14)--(G.18) control its first
projections, current operators, and readout by 12 at every
node, on every admitted positive control mesh. Each finite
operator increment is bounded directly by its rank-one
update lengths. No convergence of trained finite operator
norms is assumed.

### G.4. Readout coercivity dominates the capped hidden contribution

For a controlled state, compare features with their own
initialized features, using the same activation and actions.
The raw hidden distance (G.13) gives
\[
 \begin{split}
 \|\Delta h_i^1\|&\le2aD,\\
 \|\Delta z_i^2\|&\le 6aD+10(2aD)=26aD,\\
 \|\Delta h_i^2\|&\le52a^2D,\\
 \|\Delta z_i^3\|&\le70a^2D+10(52a^2D)\le615a^2D,\\
 \|\Delta h_i^3\|&\le1500a^3D .
 \end{split}                                                \tag{G.20}
\]
Let \(F_3:\mathbb R^3\to H_3\) have columns \(h_i^3\).
Then \(K^4=F_3^*F_3\),
\(\|F_3\|,\|F_3(0)\|\le800\sqrt3a^3\), and
\(\|\Delta F_3\|\le1500\sqrt3a^3D\). Consequently
\[
 \|K^4-K^4(0)\|\le7.2\cdot10^6a^6D,\qquad
                         K^4\succeq(3/4)\lambda a^6I_3.
                                                               \tag{G.21}
\]

Let \(J_h:\mathcal X_h\to\mathbb R^3\) be the true hidden
prediction differential, where \(\mathcal X_h\) is the
three-block hidden raw Hilbert increment space.
Let \(U_{h,R}:\mathbb R^3\to\mathcal X_h\) map coefficients to
the hidden directions in (G.12).
The same bounds (G.14)--(G.15) hold for the true gate
\((a+e/(1+z^2))q\), so
\[
 \|J_h\|,\|U_{h,R}\|\le\sqrt3\,1400a^3\|C\|,\qquad
 \|J_hU_{h,R}\|\le6\cdot10^6a^6C_S^2\le\lambda a^6/4 .
                                                               \tag{G.22}
\]
Part F proves the strong forward chain rule used here.
In the physical capped system the readout direction is
unchanged, while the hidden direction is \(-U_{h,R}r\).
Thus the exact residual equation is
\[
               \dot r=-(K^4+J_hU_{h,R})r.                   \tag{G.23}
\]
The second operator in parentheses need not be symmetric or
positive. Its absolute quadratic contribution is bounded by
(G.22). Combining with (G.21) proves
\[
 \frac{d}{dt}\|r\|_2\le-\frac{\lambda a^6}{2}\|r\|_2
                      \quad\hbox{when }\|r\|_2>0.
\]
At a zero residual all four raw directions vanish, so the
physical path stays stationary there by fixed-cap uniqueness.
Since \(r(0)=-y\),
\[
 \|r(t)\|_2\le\sqrt3e^{-\lambda a^6t/2},\qquad
 \int_0^\infty\|r(t)\|_1dt
          \le\sqrt3\int_0^\infty\|r(t)\|_2dt
          \le\frac6{\lambda a^6}=\frac S2.                  \tag{G.24}
\]

This argument is initially stopped before
\(s(t)=\int_0^t\|r(v)\|_1dv\) reaches \(S\).
Where the residual is nonzero, reparametrization gives
precisely (G.12) with \(c=-r/\|r\|_1\).
Consequently all the preceding controlled bounds are valid
before that stop. Equation (G.24) excludes the stop with
strict slack. Fixed-cap local Lipschitzness, bounded primal
states and bounded raw speeds give a strongly Cauchy limit
at any finite physical endpoint, from which local existence
continues the solution. Every population cap flow is
therefore global, with bounds uniform in its cap. The proof
has not assumed that capped dynamics dissipate energy as
a gradient flow.

### G.5. One response threshold for every physical horizon

Apply the response theorem of Part R at the fixed numerical
arguments \(a,B=12,S\). Choose \(e\le e_*(a,12,S)\).
For a fixed-cap physical Euler program, rewrite each step by
\[
 h_j=\Delta t_j\|r_j\|_1,\qquad
 c_j=-r_j/\|r_j\|_1,                                       \tag{G.25}
\]
omitting zero-residual steps. This reproduces every actual
raw update exactly. In the population program these are
deterministic causal contractions. Fixed-cap strong Euler
convergence and the strict bound \(S/2\) in (G.24) imply
\(\sum_jh_j<S\) on all sufficiently fine physical meshes
on each fixed finite horizon.

The response theorem permits every such positive effective
mesh and every such control sequence. Its affine comparator
uses the identical frozen values in (G.25). Source partial
derivatives never differentiate those controls.
The resulting bounds pass through fixed-cap mesh convergence
by truncated second-moment inequalities. For one finite
constant \(K=K(a,12,S)\),
\[
 \sup_{R>0,t\ge0}
   \{\|C_R(t)\|_p+\|q_R^2(t)\|_p+\|q_R^1(t)\|_p\}
                       \le K\sqrt p,\qquad p\ge2.          \tag{G.26}
\]
Here sample triples use the maximum coordinate norm; the
fixed sample factor is absorbed into \(K\).
The selection of \(e\), and the bound \(K\), do not depend
on the physical horizon.

The moment bound implies a Gaussian \(L^2\) tail bound.
For instance, taking \(p\) proportional to \(R^2/K^2\) in
Markov's inequality gives
\(\Pr(|Q|>R)\le C\exp(-cR^2/K^2)\) for large \(R\).
Integration of this tail, or the same estimate with two
additional powers, yields
\[
       \|Q\mathbf1_{\{|Q|>R\}}\|_2\le C_0e^{-c_0R^2}.
                                                               \tag{G.27}
\]
The constants apply to all incoming fields in (G.26),
uniformly over caps and physical times.

### G.6. Application of the internal cap-transfer argument

Part V proves the following precise implication from the facts
already obtained: global canonical fixed-cap physical paths
with bounded primal quantities and the uniform reference
tails (G.27) have a unique strong uncut limit on every finite
interval, including convergence of raw directions and HS
increments. Its proof uses the asymmetric estimate
\[
 \begin{split}
 |D_{R'}(z_A,q_A)-D_R(z_B,q_B)|
 \le{}&(a+e)|q_A-q_B|+2eR|z_A-z_B|\\
       &+2e|q_B|\mathbf1_{\{|q_B|>R\}},
                         \qquad R'\ge R,                  \tag{G.28}
 \end{split}
\]
where \(R'=\infty\) denotes the true gate. Only the reference
\((z_B,q_B)\) needs tails. Sequential backward substitution
gives a single linear loss in \(R\), and the resulting
compact-time error is \(C_T\exp(C_TR-c_0R^2)\).
Part V includes that derivation, the actual three-residual
coefficient comparison, and the strong forward and
backward passages; it is not an external invocation.

Consequently the cap paths have one consistent uncut
\(C^1\) limit on all integer horizons and hence on
\([0,\infty)\). Their canonical spaces may be chosen
simultaneously by the countable construction in Part F.
Uniqueness against bounded-primal strong competitors and
unique continuation from reached states follow from the
same reference-only estimate, also proved in Part V.
The limiting equations are the autonomous physical equations
(M.12). The scalar prediction differentiation in Part F
identifies their vector field as the raw gradient of \(L\).
Bounds (G.17)--(G.24) pass to this limit.

The fixed-cap finite-program convergence, actual finite GF
and raw GD transfer, true kernels, velocities, generated
probes, and path-space limits are proved in Part V under
exactly these bounds. Thus it supplies all assertions
(M.16)--(M.18), with the stated limit order.

Finally, each initial scalar preactivation is Gaussian with
standard deviation at least one. Equations (G.19)--(G.20)
and the stability estimate (G.8), first for cap paths and
then for their strong limit, give
\(\mathcal R(z_i^\ell(t))\ge\eta_*/4\) for every \(t,i,\ell\).
Absorb \(a(1+Z)\) into the free affine predictor to obtain
\[
 \inf_{\alpha,\beta}E[\phi(Z)-\alpha-\beta Z]^2
                              =e^2\mathcal R(Z).
\]
This proves (M.19). Part N supplies the remaining
initial-acceleration and changing-kernel assertions.

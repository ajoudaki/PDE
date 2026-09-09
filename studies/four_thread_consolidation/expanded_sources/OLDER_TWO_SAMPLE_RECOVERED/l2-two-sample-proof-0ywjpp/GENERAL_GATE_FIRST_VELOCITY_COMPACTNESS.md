# First-velocity compactness for bounded smooth activations

Root candidate, 2026-09-06. UNVERIFIED. This proves an actual finite-network
first-layer estimate, not a mean-field identification or uniqueness theorem.
It does not require a positive activation derivative or an inverse input
Gram matrix. Smooth saturation is included. There are no experiments or
external theorem imports.

## 1. Model and conclusion

Fix two deterministic inputs \(x_a\in\mathbb R^d\) with
\(|x_a|^2=d\), labels \(y_a\in\{-1,1\}\), and
\(C_{ab}=x_a^Tx_b/d\). Thus \(C\) is positive semidefinite and
\(\|C\|_{\rm op}\le2\), including either singular endpoint.
Both hidden layers have width \(n\). The fixed scalar activations satisfy
\[
 \phi_\ell\in C^2(\mathbb R),\qquad
 |\phi_\ell|\le B_\ell,\quad |\phi_\ell'|\le P_\ell,\quad
 |\phi_\ell''|\le L_\ell,\qquad \ell=1,2.                 \tag{1}
\]
The bounds are finite and independent of width. No sign assumption is made.
The canonical finite fields and rescaled readout are
\[
\begin{aligned}
 z^{(1)}_a&=W^{(1)}x_a,&h^{(1)}_a&=\phi_1(z^{(1)}_a),\\
 z^{(2)}_a&=W^{(2)}h^{(1)}_a,&h^{(2)}_a&=\phi_2(z^{(2)}_a),\\
 f_a&=(W^{(3)})^Th^{(2)}_a/n,&c_a&=-2(f_a-y_a),\\
 \delta^{(2)}_a&=W^{(3)}\odot\phi_2'(z^{(2)}_a),&
 q^{(1)}_a&=(W^{(2)})^T\delta^{(2)}_a,\\
 \delta^{(1)}_a&=\phi_1'(z^{(1)}_a)\odot q^{(1)}_a .
\end{aligned}                                                     \tag{2}
\]
The loss is \(L=\sum_a(f_a-y_a)^2\). The raw metric is
\[
 \|V\|_{\rm raw}^2=\frac d n\|V^{(1)}\|_F^2+
                   \|V^{(2)}\|_F^2+\frac1n|V^{(3)}|^2.
\]
GF and simultaneous raw GD use the directions
\[
 \dot W^{(1)}=\frac1d\sum_a c_a\delta^{(1)}_a x_a^T,\quad
 \dot W^{(2)}=\frac1n\sum_a c_a\delta^{(2)}_a(h^{(1)}_a)^T,\quad
 \dot W^{(3)}=\sum_a c_a h^{(2)}_a.                         \tag{3}
\]
GD adds \(\eta=n^{-2}\) times the old-node directions. Raw parameters
are affinely interpolated and every hidden field is recomputed.
Write the same-neuron sample pairs as
\(z_i=(z^{(1)}_{1,i},z^{(1)}_{2,i})\),
\(h_i=(h^{(1)}_{1,i},h^{(1)}_{2,i})\), and set
\(v_i=\dot z_i,\ s_i=\dot h_i\) almost everywhere.
These temporary pair symbols never combine different neuron populations.

Fix \(T>0\) and deterministic bounds
\(\|W^{(2)}(0)\|_{\rm op}\le a\),
\(\|W^{(3)}(0)\|_\infty\le b\).
There are finite constants \(K,J,A\) and an integer \(n_0\), depending
only on these bounds, \(T\), and (1), with the following properties.
For GF at every width, and GD at every \(n\ge n_0\),
\[
 \sup_{t\le T}\frac1n\sum_i|v_i(t)|^2\le K^2,\qquad
 \frac1n\sum_i\int_0^T(|v_i|^3+|s_i|^3)\,dt\le J,          \tag{4}
\]
where the supremum for step velocities uses their held node values.
For \(0<\tau<\min(1,T)\), uniformly over all these outcomes and widths,
\[
 \frac1n\sum_i\int_0^{T-\tau}
  \bigl(|v_i(t+\tau)-v_i(t)|^2+
        |s_i(t+\tau)-s_i(t)|^2\bigr)\,dt
       \le A\tau^{1/3}.                                   \tag{5}
\]
For GF alone the exponent in (5) can be \(1/2\).
The exponents concern squared \(L^2\) shift errors, not their roots.
If also \(n^{-1}\sum_i|z_i(0)|^4\le m\), the joint empirical laws of
\((z_i,v_i,h_i,s_i)\) have one deterministic compact closure in
\[
 \mathcal P_2\bigl(C([0,T];\mathbb R^2)\times L^2([0,T];\mathbb R^2)
       \times C([0,T];\mathbb R^2)\times L^2([0,T];\mathbb R^2)\bigr).
                                                               \tag{6}
\]
The product norm is the square root of the sum of the four squared
ordinary path norms; \(W_2\) is the infimum root-mean-square coupling
distance for that norm. Constants and the compact set do not require
invertibility of \(C\). No inference about unweighted kernels is made.

## 2. Actual bounds supplying the argument

At fixed width (3) is locally Lipschitz. The elementary contraction
construction gives a local solution. Differentiating \(L\) gives
\(-\dot L=\|\dot W\|_{\rm raw}^2\). Integrated squared speed is at most
\(L(0)\), so finite-time raw displacement is at most \(\sqrt{TL(0)}\).
Thus a proposed finite maximal endpoint stays in a bounded
finite-dimensional set. Bounded velocity there gives an endpoint limit
and local contraction restarts it. This proves global finite GF.

On each fixed interval the loss bounds \(\sum_a|c_a|\).
Bounded \(\phi_2\) then bounds \(W^{(3)}\) coordinatewise.
The rank-one equation for \(W^{(2)}\) bounds its operator norm, since
its right side has norm at most
\(\sum_a|c_a|P_2\|W^{(3)}\|_\infty B_1\).
Consequently there is a deterministic \(M_T\) such that
\[
\begin{gathered}
 \sum_a|c_a|+\|W^{(3)}\|_\infty+\|W^{(2)}\|_{\rm op}\le M_T,\\
 \frac{|q^{(1)}_a|}{\sqrt n}
 +\frac{|\dot z^{(1)}_a|}{\sqrt n}
 +\frac{|\dot h^{(1)}_a|}{\sqrt n}
 +\frac{|\dot z^{(2)}_a|}{\sqrt n}\le M_T.                 \tag{7}
\end{gathered}
\]
The last bound follows from
\(\dot z^{(2)}_a=\dot W^{(2)}h^{(1)}_a+W^{(2)}\dot h^{(1)}_a\).
The product rules
\[
 \dot\delta^{(2)}_a=\dot W^{(3)}\odot\phi_2'(z^{(2)}_a)
 +W^{(3)}\odot\phi_2''(z^{(2)}_a)\odot\dot z^{(2)}_a,\quad
 \dot q^{(1)}_a=(\dot W^{(2)})^T\delta^{(2)}_a+
                    (W^{(2)})^T\dot\delta^{(2)}_a
\]
give \(|\dot q^{(1)}_a|/\sqrt n\le M_T\), after enlargement.
Direct differentiation of \(f_a\) using (7) gives \(\sum_a|\dot c_a|\le M_T\).
For \(u_{a,i}=c_a q^{(1)}_{a,i}\), this proves
\[
 \frac1n\sum_i|u_i(t)|^2\le M_T^2,\qquad
 \frac1{\sqrt n}|u(t)-u(t')|\le M_T|t-t'|.               \tag{8}
\]
The norm in the second formula is the ordinary Euclidean norm of the
array of all two-component rows.

We verify the same boundedness and node increment assertions for raw GD
without comparing it to GF. Put
\(R_0=\sqrt2(B_2b+1)\), fix the padded horizon \(T+1\), and suppose
there is a first node with \(\sqrt L>R_0+1\).
Every direction leading to that node has bounded old-node controls.
Summing the readout and rank-one increments therefore bounds
\(W^{(3)}\) in infinity norm and \(W^{(2)}\) in operator norm through
that candidate node and, by convexity, along every connecting raw segment.
All constants in the remainder of this paragraph refer to these
deterministic bounds, not to an assumed descent theorem.

For a unit raw tangent \(U\),
\(|U^{(1)}x_a|/\sqrt n\le1,\ \|U^{(2)}\|_F\le1,\ |U^{(3)}|/\sqrt n\le1\).
Thus \(|D_Uz^{(2)}_a|/\sqrt n\) and \(|D_Uf_a|\) are bounded.
For two unit tangents the second derivative of \(z^{(2)}_a\) consists of
the two cross terms
\(U^{(2)}[\phi_1'(z^{(1)}_a)V^{(1)}x_a]\) and its interchange,
and
\[
 W^{(2)}[\phi_1''(z^{(1)}_a)
                      (U^{(1)}x_a)(V^{(1)}x_a)] .
\]
Their RMS norms are bounded by a constant times \(1+\sqrt n\);
use \(|\xi\odot\zeta|\le|\xi||\zeta|\) for the last one.
The second output differential has two readout cross terms, the
top curvature term
\(n^{-1}(W^{(3)})^T[\phi_2''(z^{(2)}_a)D_Uz^{(2)}_aD_Vz^{(2)}_a]\),
and the term involving \(D_UD_Vz^{(2)}_a\). Cauchy--Schwarz and the
coordinatewise readout bound give
\(|D_UD_Vf_a|\le C_T(1+\sqrt n)\).
The raw gradient at the old node is bounded in raw norm, so each
candidate segment has raw length at most \(C_T\eta\).
The first differential bound therefore bounds its residuals too.
It follows that \(\|D^2L\|_{\rm raw}\le C_T(1+\sqrt n)\) on that
segment. Taylor's integral remainder proves
\[
 L_{k+1}\le L_k-\eta\left(1-\tfrac12 C_T\eta(1+\sqrt n)\right)
                        \|\operatorname{grad}_{\rm raw}L_k\|_{\rm raw}^2 .
\]
For all sufficiently large \(n\), the parenthesis is at least \(1/2\).
Applying this through the candidate node contradicts its first-exit
definition. Hence the bounds hold on the whole padded horizon.
Product differences, or differentiation along its raw segments,
now give RMS \(O_T(\eta)\) node increments for \(z^{(1)},z^{(2)},
\delta^{(2)},q^{(1)}\), and increments \(O_T(\eta)\) for \(c\).
For example
\(\Delta q^{(1)}_a=(\Delta W^{(2)})^T\delta^{(2)}_{k,a}
 +(W^{(2)}_{k+1})^T\Delta\delta^{(2)}_a\).
Thus (8) at nodes holds with \(M_T|k-l|\eta\).
Raw \(z^{(1)}\) has RMS velocity bounded independently of width.

For GF define
\(U_i=\sum_a|u_{a,i}(0)|+\int_0^T\sum_a|\dot u_{a,i}|\);
for GD replace the integral by the sum of absolute node increments
through the padded horizon. The Euclidean triangle inequality and
(8) give \(n^{-1}\sum_i U_i^2\le C_T\), and \(|u_i(t)|\le U_i\)
for GF or held-node \(u_i\) for GD. The exact row work identity is
\[
 d|\dot W^{(1)}_i|^2=\sum_a u_{a,i}\dot h^{(1)}_{a,i}.
\]
Integration by parts and bounded \(h^{(1)}\) give row action at most
\(2B_1U_i\). Since \(C^2\preceq2C\), this implies
\(\int|v_i|^2\le4B_1U_i\); also \(\sup|v_i|\le2P_1U_i\).
Their product proves the cubic bound in (4).
For GD let \(E_{k,i}=d|\Delta W^{(1)}_{k,i}/\eta|^2\).
Taylor's formula and \(|\Delta z_i|^2\le2\eta^2E_{k,i}\) give
\[
 \sum_a u_{k,a,i}\Delta h^{(1)}_{k,a,i}
 =\eta E_{k,i}+\mathcal R_{k,i},\qquad
 |\mathcal R_{k,i}|\le L_1\eta^2 U_iE_{k,i}.
\]
Here \(\eta L_1\max_iU_i\le C_Tn^{-3/2}\le1/2\) for large \(n\).
Summation by parts bounds the summed left side by \(2B_1U_i\);
absorbing the error gives \(\sum_k\eta E_{k,i}\le4B_1U_i\).
Consequently \(\int|v_i|^2\le8B_1U_i\) and
\(\int|v_i|^3\le16B_1P_1U_i^2\) on the actual raw interpolation.
In both schemes \(s_i=\phi_1'(z_i)\odot v_i\), proving (4) for \(s\).
The same estimates imply, for both schemes,
\[
 \frac1n\sum_i\left(\int_0^T|v_i|^2\right)^2\le C_T,\qquad
 \frac1n\sum_i\sup_{t\le T}|z_i(t)|^4
       \le\frac8n\sum_i|z_i(0)|^4+C_T.                    \tag{9}
\]
The second follows from
\(\sup|z_i|\le|z_i(0)|+\sqrt T(\int|v_i|^2)^{1/2}\).

## 3. An L1 shift estimate, then interpolation

Put \(\epsilon=0\) for GF and \(\epsilon=\eta\) for GD.
Let \(\bar z,\bar u\) denote current values for GF and held old-node
values for GD. Equations (3) give exactly
\[
 v_i(t)=C[\phi_1'(\bar z_i(t))\odot\bar u_i(t)] .          \tag{10}
\]
Telescoping the node estimates in (8) and the corresponding
preactivation increments, or using their continuous versions, gives
\[
\begin{aligned}
 \left(\frac1n\sum_i\int_0^{T-\tau}
  |\bar u_i(t+\tau)-\bar u_i(t)|^2dt\right)^{1/2}
       &\le C_T(\tau+\epsilon),\\
 \left(\frac1n\sum_i\int_0^{T-\tau}
  |\bar z_i(t+\tau)-\bar z_i(t)|^2dt\right)^{1/2}
       &\le C_T(\tau+\epsilon).
\end{aligned}                                                    \tag{11}
\]
There are at most \(\tau/\eta+1\) crossed steps. Also
\(n^{-1}\sum_i\int_0^{T-\tau}|\bar u_i(t)|^2dt\le C_T\).
Subtract (10). The term with the difference of \(u\) is bounded in
empirical \(L^1\) by \(2P_1\sqrt T\) times the first norm in (11).
The other term is bounded pointwise by
\(2L_1|\bar z_i(t+\tau)-\bar z_i(t)|\,|\bar u_i(t)|\).
Cauchy--Schwarz in the time integral and neuron sum proves
\[
 \frac1n\sum_i\int_0^{T-\tau}|v_i(t+\tau)-v_i(t)|\,dt
                         \le C_T(\tau+\epsilon).        \tag{12}
\]
The nonlinearity may have zeros or change derivative sign: this estimate
uses only a product in \(L^1\), not a multiplication operator on \(L^2\).

The actual, non-held position obeys the RMS shift bound \(C_T\tau\),
because its RMS speed is bounded. Since
\(s_i(t)=\phi_1'(z_i(t))\odot v_i(t)\), the same subtraction gives
\[
 \frac1n\sum_i\int_0^{T-\tau}|s_i(t+\tau)-s_i(t)|\,dt
 \le P_1 C_T(\tau+\epsilon)
 +L_1\left(\frac1n\sum_i\int|\Delta_\tau z_i|^2\right)^{1/2}
       \left(\frac1n\sum_i\int|v_i|^2\right)^{1/2}
 \le C_T(\tau+\epsilon).                                 \tag{13}
\]
Thus recomputed GD activation velocities, not held activation values,
are being estimated.

For any vector-valued measurable array \(w_i(t)\), Cauchy--Schwarz gives
the elementary interpolation inequality
\[
 \frac1n\sum_i\int|w_i|^2
 \le\left(\frac1n\sum_i\int|w_i|\right)^{1/2}
      \left(\frac1n\sum_i\int|w_i|^3\right)^{1/2}.         \tag{14}
\]
Apply it to each shift difference. Its cubic integral is at most
eight times the bound for the original velocity, by
\(|x-y|^3\le4(|x|^3+|y|^3)\).
Equations (4), (12), and (13) therefore prove
\[
 \frac1n\sum_i\int_0^{T-\tau}
 (|\Delta_\tau v_i|^2+|\Delta_\tau s_i|^2)
                         \le C_T(\tau+\epsilon)^{1/2}.   \tag{15}
\]

To remove \(\eta\) uniformly, for \(0<\tau\le\eta\) the step function
\(v\) changes between shifted times only when their interval crosses
a node. There are at most \(T/\eta\) internal nodes, each contributing
a set of starting times of length at most \(\tau\).
The RMS squared difference at any time is at most \(4K^2\).
Hence its squared shift integral is at most \(4TK^2\tau/\eta\).
For larger shifts use \(4TK^2\).
Together with (15), the squared \(v\) shift is bounded by
\[
 \min\{C_T(\tau+\eta)^{1/2},\,4TK^2\min(1,\tau/\eta)\}.
\]
Split \(\eta\) at \(\tau^{2/3}\). The first bound if
\(\eta\le\tau^{2/3}\), and the second otherwise, are at most
\(C_T\tau^{1/3}\). This proves the \(v\) part of (5).

For the activation velocity, split its difference instead as
\[
 \Delta_\tau s_i=
  \phi_1'(z_i(t+\tau))\odot\Delta_\tau v_i+
  [\phi_1'(z_i(t+\tau))-\phi_1'(z_i(t))]\odot v_i(t).
\]
The first term has squared \(L^2\) shift error at most
\(P_1^2C_T\tau^{1/3}\). The second term has empirical \(L^1\) norm
at most \(C_T\tau\), and cubic integral at most
\((2P_1)^3 n^{-1}\sum_i\int|v_i|^3\le C_T\).
Equation (14) bounds its squared \(L^2\) norm by \(C_T\tau^{1/2}\).
The squared triangle inequality and \(\tau\le1\) prove (5).
For GF, (15) already gives its stated stronger exponent.

## 4. Compactness and interpretation

On a uniform partition of length \(h\), let \(P_h\) average velocities
on each cell and let \(\Pi_h\) interpolate the position node values.
The identity
\[
 \int_I|v-\operatorname{avg}_Iv|^2
       =\frac1{2h}\int_I\int_I|v(t)-v(s)|^2\,ds\,dt
\]
and (5), followed by integrating shifts \(0<\tau<h\), give average
squared projection errors at most \(C_Th^{1/3}\) for both velocities.
Absolute continuity gives average squared uniform errors at most
\(C_Th\) for both positions. Coupling each empirical tuple to its own
projection therefore has squared cost \(C_T(h^{1/3}+h)\), tending to
zero uniformly over all good outcomes and admissible widths.

By (9), bounded activations, and \(|s|\le P_1|v|\), the joint tuples
have uniformly bounded fourth moments in the product norm of (6).
The projected tuples have the same bound: averaging contracts \(L^2\)
and polygonal interpolation contracts the uniform norm.
For a fixed partition the range is finite dimensional. Moving its law
outside a radius \(R\) ball to zero costs at most \(C_T/R^2\) in squared
transport. A finite grid in that ball approximates the remainder;
the mass vectors on this grid lie in a compact finite simplex.
Thus projected laws are totally bounded in \(W_2\), uniformly, and
so are the original laws by the vanishing projection error.

For completeness, every Cauchy sequence selected from these finite
empirical laws has a convergent subsequence: select successive \(W_2\)
distances smaller than \(2^{-j-1}\), choose finite transport tables
with costs smaller than \(2^{-j}\), and glue them by their conditional
transition probabilities. Splitting a unit interval recursively
constructs a common coupling with summable \(L^2\) increments.
Its random tuples converge almost surely and in \(L^2\) in the complete
product space \(C\times L^2\times C\times L^2\).
The limit law is the \(W_2\) limit. Approximating points in the closure
by empirical laws proves sequential compactness of that closure;
in a metric space finite nets and a convergent-subsequence contradiction
give the open-cover compactness statement too. This proves (6).
The integral identities \(z(t)=z(0)+\int_0^t v\),
\(h=\phi_1(z)\), and \(s=\phi_1'(z)v\) pass to these joint limits.
For the last identity, uniform convergence of \(z\) and strong \(L^2\)
convergence of \(v\) suffice by the bounded continuous derivative.
These are compatibility statements, not identification of the driving
fields \(q^{(1)}\).

For the prescribed independent Gaussian initialization
\(W^{(1)}_{ij}\sim N(0,1/d)\),
\(W^{(2)}_{ij}\sim N(0,1/n)\), \(W^{(3)}_i\sim N(0,n^{-2})\),
the deterministic assumptions hold with \(a=8,b=1,m=13\) except on an
event of probability at most
\[
 b_n=\frac{1680}{n}+2e^{-(8-2\log9)n}+2ne^{-n^2/2}.        \tag{16}
\]
Indeed a \(1/4\) sphere net has at most \(9^n\) points by disjoint
radius-\(1/8\) balls in the radius-\(9/8\) ball. Approximating both
vectors gives \(\|W^{(2)}\|_{\rm op}\le2\max|u^TW^{(2)}v|\).
Each fixed scalar has variance \(1/n\), so its threshold-four Gaussian
tail and a union bound give the middle term in (16).
The threshold-one readout union bound gives the last term.
For a first Gaussian pair \(G\), direct Gaussian moments give
\(\mathbb E|G|^4=8+4C_{12}^2\le12\) and
\(\mathbb E|G|^8\le8(105+105)=1680\).
Independent rows and the second-moment Markov inequality give the
first term. These moment and tail formulas follow by integrating
the Gaussian density, or completing its square for the exponential
tail. Hence (6) is compact containment in probability for the actual
initialization, not an assumed population regularity property.

The proof neither assumes nor establishes independence of trained
neurons, convergence of the full width sequence, equality of GF/GD
subsequential laws, strong second-layer velocities, or a globally
restartable population flow. In particular a smooth saturated activation
retains this first-velocity compactness without a positive gate margin;
that fact does not resolve the separate adaptive Gaussian-response
problem or certify nonlazy feature learning.

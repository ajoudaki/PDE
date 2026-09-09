# Independent adversarial audit: first-velocity compactness

Date: 2026-09-06.

Source audited: [GENERAL_GATE_FIRST_VELOCITY_COMPACTNESS.md](/tmp/l2-two-sample-proof-0ywjpp/GENERAL_GATE_FIRST_VELOCITY_COMPACTNESS.md), all 382 lines, 17,492 bytes.

Scope: the actual finite-network GF and simultaneous raw-GD first-layer compactness candidate in this document. No other project files, named dependencies, histories, ledgers, agents, or reviews were consulted. No experiments, subagents, browsing, or external theorem imports were used. The audit consists of direct mathematical checks of the supplied argument. The source was not edited.

SHA-256 before reading:

    319f0843407592ecca8b9fd10523a0b0bdd188cb62c67383a9bd46440b3b4b92

SHA-256 after the audit:

    319f0843407592ecca8b9fd10523a0b0bdd188cb62c67383a9bd46440b3b4b92

## Verdict

**The stated finite-network first-layer compactness result passes this audit. I found no substantive mathematical gap and no required correction to its hypotheses, conclusions, or proof.**

In particular, the argument establishes the actual GF bounds and the actual simultaneous raw-GD bounds for all sufficiently large widths, obtains the cubic gain without a positive gate assumption, proves a modulus uniform over the admissible GD step sizes for the recomputed activation velocities, and upgrades finite-dimensional approximation to compact closure in the stated strong \(W_2\) topology. The Gaussian exceptional-probability estimate is correct and remains valid at both singular endpoints of the input Gram matrix.

Several short passages benefit from expansion. Those expansions are supplied below. They use estimates already established in the candidate and do not introduce additional assumptions. Optional wording improvements are separated at the end.

The result being accepted is exactly this: for fixed \(T,a,b\) and the activation bounds, there are width-independent \(K,J,A,n_0\) giving (4)–(5) for GF at every width and GD at \(n\ge n_0\). With a fixed additional initial fourth-moment bound \(m\), the entire corresponding family of empirical first-layer path laws has compact closure in the space in (6). The compact set can depend on \(m\). No mean-field identification, uniqueness, GF/GD agreement, or other excluded conclusion is needed for this statement.

## 1. Metric normalization, equations, and global finite GF

Source: lines 11–49 and 86–92.

For a vector or a two-sample array, write \(\|p\|_n=|p|/\sqrt n\), where the array norm includes both sample coordinates. All constants below are independent of width. Their values can increase from one estimate to another.

### 1.1 The directions are the negative raw gradient

The ordinary parameter gradients of the specified loss are

\[
\begin{aligned}
 \nabla_{W^{(1)}}L
   &=-\frac1n\sum_a c_a\delta^{(1)}_a x_a^T,\\
 \nabla_{W^{(2)}}L
   &=-\frac1n\sum_a c_a\delta^{(2)}_a(h^{(1)}_a)^T,\\
 \nabla_{W^{(3)}}L
   &=-\frac1n\sum_a c_a h^{(2)}_a.
\end{aligned}
\]

Inverting the three metric coefficients \(d/n,1,1/n\) gives exactly (3). In particular, the first-layer factor is \(1/d\), the middle-layer factor is \(1/n\), and there is no \(1/n\) in the readout direction. There is no normalization or sign discrepancy.

Consequently

\[
 \frac{dL}{dt}
 =-\|\operatorname{grad}_{\rm raw}L\|_{\rm raw}^2
 =-\|\dot W\|_{\rm raw}^2.
\]

This also confirms the descent direction used in the GD Taylor calculation.

### 1.2 Global existence is justified at each finite width

The finite-dimensional loss is \(C^2\) under (1), so its raw gradient is \(C^1\) and locally Lipschitz. The local contraction construction applies. Along the resulting solution,

\[
 \int_0^t\|\dot W(r)\|_{\rm raw}^2\,dr\le L(0),
 \qquad
 \|W(t)-W(0)\|_{\rm raw}\le \sqrt{tL(0)}.
\]

If the maximal forward endpoint \(t_*\) were finite, these bounds place the trajectory in a bounded finite-dimensional set. At fixed width the raw norm is a positive definite norm equivalent to the ordinary parameter norm. The vector field is bounded on the closure of that set. Thus \(W(t)\) has a limit as \(t\uparrow t_*\), and the local construction at that limit extends the trajectory. This contradicts maximality.

There is no need for a width-uniform bound on the whole initial \(W^{(1)}\). Finite-width existence uses its actual finite initial value; the subsequent width-uniform field estimates use bounded activations and derivatives instead.

**Finding:** the normalization, energy identity, and global finite-GF argument are correct.

## 2. Actual GF field bounds and forcing variation

Source: lines 94–126.

Set

\[
 R_0=\sqrt2(B_2b+1).
\]

At initialization, \(|f_a(0)|\le B_2b\), hence \(L(0)\le R_0^2\). Loss descent therefore gives

\[
 \sum_a|c_a(t)|
 =2\sum_a|f_a(t)-y_a|
 \le 2\sqrt2\,R_0=:r.
\]

The readout and middle-layer equations imply

\[
\begin{aligned}
 \|W^{(3)}(t)\|_\infty
 &\le b+rB_2t=:H_t,\\
 \|\dot W^{(2)}(t)\|_{\rm op}
 &\le \frac1n\sum_a|c_a|\,|\delta^{(2)}_a|\,|h^{(1)}_a|
 \le rP_2H_tB_1,\\
 \|W^{(2)}(t)\|_{\rm op}
 &\le a+rP_2B_1\int_0^tH_s\,ds.
\end{aligned}
\]

The same rank-one estimate bounds \(\|\dot W^{(2)}\|_F\). The factors of \(\sqrt n\) in the two vectors cancel the \(1/n\) exactly.

Let \(H,D\) be bounds for the readout infinity norm and middle-layer operator norm over the interval. Then

\[
 \|\delta^{(2)}_a\|_n\le P_2H,
 \qquad
 \|q^{(1)}_a\|_n\le DP_2H.
\]

The first-layer preactivation derivative is

\[
 \dot z^{(1)}_a
 =\sum_b C_{ab}c_b
       \bigl(\phi_1'(z^{(1)}_b)\odot q^{(1)}_b\bigr).
\]

Since \(|C_{ab}|\le1\), its normalized Euclidean norm is bounded. Multiplication by \(\phi_1'\) also bounds \(\|\dot h^{(1)}_a\|_n\). The formula

\[
 \dot z^{(2)}_a
 =\dot W^{(2)}h^{(1)}_a+W^{(2)}\dot h^{(1)}_a
\]

then bounds \(\|\dot z^{(2)}_a\|_n\). These are the bounds in (7).

For the differentiated backpropagated fields,

\[
\begin{aligned}
 \|\dot\delta^{(2)}_a\|_n
 &\le P_2\|\dot W^{(3)}\|_\infty
      +HL_2\|\dot z^{(2)}_a\|_n,\\
 \|\dot q^{(1)}_a\|_n
 &\le \|\dot W^{(2)}\|_{\rm op}\|\delta^{(2)}_a\|_n
      +D\|\dot\delta^{(2)}_a\|_n.
\end{aligned}
\]

Both are bounded independently of width. No coordinatewise bound on \(q^{(1)}\) is used.

Direct output differentiation gives

\[
 |\dot f_a|
 \le B_2\|\dot W^{(3)}\|_\infty
       +HP_2\|\dot z^{(2)}_a\|_n.
\]

Thus \(\sum_a|\dot c_a|\) is bounded. For \(u_a=c_aq^{(1)}_a\),

\[
 \|\dot u_a\|_n
 \le |\dot c_a|\|q^{(1)}_a\|_n
       +|c_a|\|\dot q^{(1)}_a\|_n.
\]

Combining the two samples gives a uniform bound for \(\|u\|_n\) and \(\|\dot u\|_n\), and integration gives (8).

This establishes the forcing variation from the actual GF equations. It does not assume a population regularity property or a time-regularity bound for an unidentified limiting field.

**Finding:** every estimate in the GF chain is supported by the available norms and by \(C^2\) regularity alone.

## 3. Actual raw GD: first exit, Hessian, and node increments

Source: lines 128–177.

### 3.1 The first-exit bounds are not circular

Use the padded horizon \(S=T+1\). Suppose a first node in this horizon satisfies \(\sqrt{L_k}>R_0+1\). Every preceding node has

\[
 \sum_a|c_{j,a}|\le2\sqrt2(R_0+1)=:r_*.
\]

Summing readout increments first gives, through the candidate node,

\[
 \|W^{(3)}_j\|_\infty\le b+r_*B_2S=:H_*.
\]

Then summing middle-layer increments gives

\[
 \|W^{(2)}_j\|_{\rm op}
 \le a+r_*P_2H_*B_1S=:D_*.
\]

These estimates use only residual control at the old nodes. They do not require loss descent or residual control at the candidate new node. Convexity of both norms extends the same bounds to each connecting affine parameter segment.

The order of this construction matters: readout control precedes middle-layer control, which precedes the uniform first-differential and Hessian estimates. The candidate uses that order correctly.

### 3.2 Unit raw tangents give the stated first-differential bounds

For \(\|U\|_{\rm raw}=1\),

\[
 |U^{(1)}x_a|
 \le\|U^{(1)}\|_F|x_a|
 \le\sqrt{n/d}\sqrt d=\sqrt n,
 \quad
 \|U^{(2)}\|_{\rm op}\le\|U^{(2)}\|_F\le1,
 \quad
 |U^{(3)}|\le\sqrt n.
\]

Writing

\[
 Z_*:=B_1+D_*P_1,
\]

we obtain on every candidate segment

\[
 \|D_Uz^{(2)}_a\|_n
 \le \|U^{(2)}h^{(1)}_a\|_n
       +\|W^{(2)}[\phi_1'(z^{(1)}_a)U^{(1)}x_a]\|_n
 \le Z_*.
\]

Also

\[
 |D_Uf_a|
 \le B_2+H_*P_2Z_*=:F_*.
\]

Both constants are width independent and require no bound on the values of \(z^{(1)}\).

### 3.3 The raw Hessian bound is \(O(1+\sqrt n)\)

For two unit raw tangents \(U,V\), the full second derivative of the second-layer preactivation is

\[
\begin{aligned}
 D_UD_Vz^{(2)}_a
 ={}&U^{(2)}[\phi_1'(z^{(1)}_a)V^{(1)}x_a]\\
 &+V^{(2)}[\phi_1'(z^{(1)}_a)U^{(1)}x_a]\\
 &+W^{(2)}[
       \phi_1''(z^{(1)}_a)
       (U^{(1)}x_a)\odot(V^{(1)}x_a)].
\end{aligned}
\]

The first two terms each have normalized norm at most \(P_1\). For the last term,

\[
 \frac1{\sqrt n}
 \left|W^{(2)}[
       \phi_1''(z^{(1)}_a)
       (U^{(1)}x_a)\odot(V^{(1)}x_a)]\right|
 \le D_*L_1\sqrt n,
\]

using \(|\xi\odot\zeta|\le|\xi||\zeta|\). Therefore

\[
 \|D_UD_Vz^{(2)}_a\|_n
 \le2P_1+D_*L_1\sqrt n.
\]

There are exactly four types of terms in the second output differential:

\[
\begin{aligned}
 D_UD_Vf_a={}&
 \frac1n(U^{(3)})^T[
       \phi_2'(z^{(2)}_a)\odot D_Vz^{(2)}_a]\\
 &+\frac1n(V^{(3)})^T[
       \phi_2'(z^{(2)}_a)\odot D_Uz^{(2)}_a]\\
 &+\frac1n(W^{(3)})^T[
       \phi_2''(z^{(2)}_a)
       D_Uz^{(2)}_a\odot D_Vz^{(2)}_a]\\
 &+\frac1n(W^{(3)})^T[
       \phi_2'(z^{(2)}_a)\odot D_UD_Vz^{(2)}_a].
\end{aligned}
\]

The two readout cross terms together are bounded by \(2P_2Z_*\). The upper activation-curvature term is bounded by

\[
 \frac{H_*L_2}{n}
     \sum_i|(D_Uz^{(2)}_a)_i(D_Vz^{(2)}_a)_i|
 \le H_*L_2Z_*^2.
\]

The last term is bounded by

\[
 H_*P_2(2P_1+D_*L_1\sqrt n).
\]

Thus \(|D_UD_Vf_a|\le C_*(1+\sqrt n)\), exactly as claimed. In particular, the top curvature term does not introduce an extra factor of \(\sqrt n\); the coordinatewise readout bound permits the displayed \(\ell^1\) product estimate.

At an old node,

\[
 \|\operatorname{grad}_{\rm raw}L_k\|_{\rm raw}
 \le \sum_a|c_{k,a}|F_*\le r_*F_*.
\]

The candidate segment therefore has raw length at most \(\eta r_*F_*\), and the uniform first-differential bound controls the residual throughout that segment. One can also bound these residuals directly by \(B_2H_*+1\), since the activation and readout bounds already hold throughout the segment. Either argument is independent of descent.

Finally,

\[
 D_UD_VL
 =2\sum_a\left[
     (D_Uf_a)(D_Vf_a)
       +(f_a-y_a)D_UD_Vf_a\right]
\]

gives

\[
 \|D^2L\|_{\rm raw}\le C_*(1+\sqrt n).
\]

Only second derivatives of the activations occur. A Lipschitz Hessian or bounded third derivative is unnecessary.

### 3.4 Taylor descent closes the first-exit argument

On the actual simultaneous update segment, Taylor's integral remainder gives

\[
 L_{k+1}
 \le L_k-\eta\|\operatorname{grad}_{\rm raw}L_k\|_{\rm raw}^2
       +\frac{\eta^2}{2}C_*(1+\sqrt n)
          \|\operatorname{grad}_{\rm raw}L_k\|_{\rm raw}^2.
\]

Because \(\eta=n^{-2}\), the correction coefficient tends to zero like \(n^{-3/2}\). Choose \(n_0\) sufficiently large that

\[
 \tfrac12 C_*n^{-2}(1+\sqrt n)\le\tfrac12
\]

for every \(n\ge n_0\). Applying the resulting descent inequality to every segment through the proposed first exit yields \(L_k\le L(0)\le R_0^2\), contradicting its definition.

Thus the stopped bounds hold throughout the padded horizon. This is an actual GD estimate; no comparison with GF has entered.

### 3.5 Recomputed fields have the required node increments

Along an affine raw segment, the held parameter directions obey

\[
 \|\dot W^{(3)}\|_\infty\le C_*,
 \quad
 \|\dot W^{(2)}\|_{\rm op}\le C_*,
 \quad
 \|\dot z^{(1)}_a\|_n\le C_*.
\]

The recomputed fields satisfy

\[
\begin{aligned}
 \dot z^{(2)}_a(t)
 &=\dot W^{(2)}_k h^{(1)}_a(t)
       +W^{(2)}(t)\dot h^{(1)}_a(t),\\
 \dot\delta^{(2)}_a(t)
 &=\dot W^{(3)}_k\odot\phi_2'(z^{(2)}_a(t))
       +W^{(3)}(t)\odot\phi_2''(z^{(2)}_a(t))
                           \odot\dot z^{(2)}_a(t),\\
 \dot q^{(1)}_a(t)
 &=(\dot W^{(2)}_k)^T\delta^{(2)}_a(t)
       +W^{(2)}(t)^T\dot\delta^{(2)}_a(t).
\end{aligned}
\]

Every right-hand side has bounded normalized norm by the same estimates as in the GF calculation. Output differentiation also gives a bounded \(|\dot c_a(t)|\). Integration over a segment of length \(\eta\) proves the claimed \(O(\eta)\) node increments.

For example,

\[
 \Delta u_a
 =c_{k+1,a}\Delta q^{(1)}_a
       +(\Delta c_a)q^{(1)}_{k,a}
\]

has normalized norm \(O(\eta)\). Summing increments gives the node version of (8).

The padding is sufficient for a final incomplete step: if \(N=\lceil T/\eta\rceil\), then \(N\eta\le T+1\), since \(\eta\le1\).

**Finding:** the first-exit argument, its Hessian estimate, and all node increment assertions are valid. There is no assumed descent hidden in the controls used to prove descent.

## 4. Row-work identity, signed gates, and the cubic gain

Source: lines 179–212.

### 4.1 The rowwise variation majorants have bounded empirical second moment

For GF define

\[
 U_i=|u_i(0)|_1+\int_0^T|\dot u_i(t)|_1\,dt.
\]

Minkowski's inequality in the finite neuron index and \(|w|_1\le\sqrt2|w|\) give

\[
 \left(\frac1n\sum_iU_i^2\right)^{1/2}
 \le\sqrt2\left(
       \|u(0)\|_n+\int_0^T\|\dot u(t)\|_n\,dt\right)
 \le C_T.
\]

For GD, replace the integral by the sum of the absolute node increments through the padded horizon. The corresponding bound follows from

\[
 \sum_k\|\Delta u_k\|_n
 \le C_T\sum_k\eta\le C_T(T+1).
\]

Thus in both cases

\[
 \frac1n\sum_iU_i^2\le C_T,
 \qquad
 \sup_t|u_i(t)|_1\le U_i
\]

for GF, and for the held \(u_i\) in GD. The continuous derivative bound needed here was established in Section 2 of this report; the candidate does not infer coordinatewise variation from a mere bound on values.

### 4.2 The positive quantity is supplied by the Gram matrix

For a fixed row put

\[
 g_i=\phi_1'(z_i)\odot u_i.
\]

For GF,

\[
 \dot W^{(1)}_i=\frac1d\sum_a g_{a,i}x_a,
 \qquad
 v_i=Cg_i.
\]

Consequently

\[
 d|\dot W^{(1)}_i|^2
 =g_i^TCg_i
 =u_i\cdot\bigl(\phi_1'(z_i)\odot v_i\bigr)
 =u_i\cdot s_i.
\]

No component of \(u_i\), \(g_i\), or \(\phi_1'\) is required to be nonnegative. The scalar on the left is nonnegative because \(C\) is positive semidefinite.

Since \(C\) has eigenvalues in \([0,2]\),

\[
 C^2\preceq2C,
 \qquad
 |v_i|^2=g_i^TC^2g_i\le2g_i^TCg_i.
\]

This is the necessary one-sided comparison. There is no reverse coercivity inequality and no use of \(C^{-1}\).

### 4.3 GF action and cubic integrability

Integration by parts, with each component of \(h_i\) bounded by \(B_1\), gives

\[
\begin{aligned}
 \int_0^Tg_i^TCg_i\,dt
 &=u_i(T)\cdot h_i(T)-u_i(0)\cdot h_i(0)
       -\int_0^T\dot u_i\cdot h_i\,dt\\
 &\le B_1\left(
       |u_i(T)|_1+|u_i(0)|_1
          +\int_0^T|\dot u_i|_1\,dt\right)\\
 &\le2B_1U_i.
\end{aligned}
\]

It follows that

\[
 \int_0^T|v_i|^2\,dt\le4B_1U_i,
 \qquad
 \sup_t|v_i(t)|\le2P_1U_i.
\]

Multiplying these estimates yields

\[
 \int_0^T|v_i|^3\,dt\le8B_1P_1U_i^2.
\]

Averaging over rows is now legitimate because the available majorant is \(U_i^2\). This is the actual cubic gain; a bound by \(U_i^3\) would not have sufficed.

### 4.4 GD action: Taylor error and absorption

At a GD node use

\[
 g_{k,i}=\phi_1'(z_{k,i})\odot u_{k,i},
 \qquad
 E_{k,i}=g_{k,i}^TCg_{k,i}.
\]

The raw update gives exactly

\[
 \Delta z_{k,i}=\eta Cg_{k,i},
 \qquad
 |\Delta z_{k,i}|^2\le2\eta^2E_{k,i}.
\]

Scalar Taylor expansion in each sample coordinate yields

\[
 \sum_a u_{k,a,i}\Delta h_{k,a,i}
 =\eta E_{k,i}+\mathcal R_{k,i},
\]

where

\[
\begin{aligned}
 |\mathcal R_{k,i}|
 &\le\frac{L_1}{2}
       \sum_a|u_{k,a,i}|\,|\Delta z_{k,a,i}|^2\\
 &\le\frac{L_1}{2}U_i|\Delta z_{k,i}|^2\\
 &\le L_1\eta^2U_iE_{k,i}.
\end{aligned}
\]

The sign of \(u_{k,a,i}\) is handled by the absolute value in this remainder bound.

The empirical bound on \(U_i^2\) implies

\[
 \max_iU_i\le\left(\sum_iU_i^2\right)^{1/2}\le C_T\sqrt n.
\]

Therefore \(\eta L_1\max_iU_i\le C_Tn^{-3/2}\), and the original \(n_0\) may be enlarged so that this quantity is at most \(1/2\). This enlargement uses only the already established deterministic bounds.

For any complete collection of steps through the required time horizon,

\[
\begin{aligned}
 \sum_{k=0}^{N-1}u_{k,i}\cdot(h_{k+1,i}-h_{k,i})
 ={}&u_{N-1,i}\cdot h_{N,i}-u_{0,i}\cdot h_{0,i}\\
 &-\sum_{k=1}^{N-1}(u_{k,i}-u_{k-1,i})\cdot h_{k,i}.
\end{aligned}
\]

The absolute-value bound on the right is at most \(2B_1U_i\). Absorbing the Taylor remainder on the left consequently gives

\[
 \sum_k\eta E_{k,i}\le4B_1U_i.
\]

The actual \(v_i\) is the held \(Cg_{k,i}\) on each raw segment, so

\[
 \int_0^T|v_i|^2\,dt\le8B_1U_i,
 \qquad
 \int_0^T|v_i|^3\,dt\le16B_1P_1U_i^2.
\]

For an incomplete last step, include the entire last step in the sum, which is available within the padded horizon, and restrict the nonnegative integrals back to \([0,T]\).

This GD proof does not use the continuous GF work identity for recomputed GD activations. It uses the displayed discrete Taylor identity, which is the correct replacement.

### 4.5 Activation velocities and fourth moments

In both schemes the actual first-layer position is absolutely continuous, and

\[
 s_i(t)=\phi_1'(z_i(t))\odot v_i(t)
\]

almost everywhere. Hence \(|s_i|\le P_1|v_i|\), which proves the stated cubic bound for \(s_i\) as well.

Let \(A_i=\int_0^T|v_i|^2\). The row action estimate gives

\[
 \frac1n\sum_iA_i^2\le C_T.
\]

Absolute continuity gives

\[
 \sup_t|z_i(t)|\le |z_i(0)|+\sqrt T\,A_i^{1/2}.
\]

Using \((x+y)^4\le8(x^4+y^4)\) gives exactly the second estimate in (9). In particular, (9) controls the fourth moment of the \(L^2\) path norm of \(v_i\), not a pointwise fourth moment of velocity. The former is the quantity needed later.

### 4.6 Zero gates and singular endpoints

Write

\[
 C=\begin{pmatrix}1&\rho\\ \rho&1\end{pmatrix},
 \qquad -1\le\rho\le1.
\]

At \(\rho=1\),

\[
 g^TCg=(g_1+g_2)^2,
 \quad
 Cg=(g_1+g_2,g_1+g_2),
 \quad
 |Cg|^2=2g^TCg.
\]

At \(\rho=-1\),

\[
 g^TCg=(g_1-g_2)^2,
 \quad
 Cg=(g_1-g_2,-g_1+g_2),
 \quad
 |Cg|^2=2g^TCg.
\]

Thus the crucial comparison remains valid, with the same constant, at both endpoints. Null directions create zero row velocity and do not invalidate the bound.

If a gate vanishes, the corresponding component of \(g\) vanishes. If gates change sign, the same quadratic-form identities still hold. A sample coordinate can move because of the other sample even when its own gate is zero; the proof uses the full pair identity and does not incorrectly assume otherwise. No division by a gate or positive lower bound is present. Constant activations also cause no exception.

**Finding:** the row-work argument, the GD remainder estimate, its absorption, and every claimed moment consequence are correct for signed and zero gates and for singular \(C\).

## 5. \(L^1\) shifts, interpolation, and removal of the step size

Source: lines 214–305.

Use the common measure

\[
 d\nu(i,t)=\frac1n\sum_{i=1}^n\delta_i\,dt
\]

on the neuron index and the indicated time interval. All \(L^p\) calculations below use this measure; there is no change from empirical to unweighted norms.

### 5.1 Held-field shifts

Equation (10) is exact:

\[
 v_i(t)=C[\phi_1'(\bar z_i(t))\odot\bar u_i(t)].
\]

For GF the bars do nothing. For GD they select the old node that supplies the raw first-layer direction.

For GD, the two held indices at times \(t,t+\tau\) differ by at most \(\tau/\eta+1\) steps. The node increment bounds therefore give, at each time,

\[
 \|\bar u(t+\tau)-\bar u(t)\|_n+
 \|\bar z(t+\tau)-\bar z(t)\|_n
 \le C_T(\tau+\eta).
\]

Integration in time gives (11), with \(\sqrt T\) absorbed into the constant. GF gives the same estimate with \(\eta\) replaced by zero.

### 5.2 The nonlinear product is estimated in \(L^1\)

Subtracting (10) and placing the difference of \(u\) in one term gives

\[
\begin{aligned}
 |\Delta_\tau v_i|
 \le{}&2P_1|\Delta_\tau\bar u_i|\\
 &+2L_1|\Delta_\tau\bar z_i|\,|\bar u_i(t)|.
\end{aligned}
\]

The first term has \(L^1(\nu)\) norm bounded by \(2P_1\sqrt T\) times its \(L^2(\nu)\) norm. For the second, Cauchy–Schwarz gives

\[
 \int|\Delta_\tau\bar z|\,|\bar u|\,d\nu
 \le
 \left(\int|\Delta_\tau\bar z|^2\,d\nu\right)^{1/2}
 \left(\int|\bar u|^2\,d\nu\right)^{1/2}.
\]

This proves (12). A product of two \(L^2\) factors is used only in \(L^1\), as permitted. No unsupported \(L^2\) multiplication estimate or inverse-gate argument is hidden here.

### 5.3 Recomputed activation-velocity shifts

For the actual, non-held first-layer position,

\[
 z_i(t+\tau)-z_i(t)=\int_t^{t+\tau}v_i(r)\,dr.
\]

Minkowski's inequality and the uniform empirical squared-speed bound give

\[
 \left(\frac1n\sum_i|\Delta_\tau z_i(t)|^2\right)^{1/2}
 \le K\tau.
\]

Thus its \(L^2(\nu)\) shift norm is at most \(K\sqrt T\,\tau\), with no step-size error.

Using the exact identity \(s=\phi_1'(z)\odot v\), subtraction gives

\[
 \int|\Delta_\tau s|\,d\nu
 \le P_1\int|\Delta_\tau v|\,d\nu
       +L_1\|\Delta_\tau z\|_{L^2(\nu)}
                       \|v\|_{L^2(\nu)}
 \le C_T(\tau+\epsilon).
\]

This proves (13) for the recomputed activation velocity. It is not a statement about a held approximation to \(s\).

### 5.4 The interpolation inequality and its exponents

For any vector-valued \(w\),

\[
 \int|w|^2\,d\nu
 =\int |w|^{1/2}|w|^{3/2}\,d\nu
 \le
 \left(\int|w|\,d\nu\right)^{1/2}
 \left(\int|w|^3\,d\nu\right)^{1/2}.
\]

This is (14), including its normalization and exponents.

For a shift difference,

\[
 |\Delta_\tau w_i(t)|^3
 \le4\bigl(|w_i(t+\tau)|^3+|w_i(t)|^3\bigr).
\]

Each of the two restricted time integrals is bounded by the full cubic integral, giving the stated factor eight. Applying (14) to \(v\) and \(s\) proves (15).

For GF, \(\epsilon=0\), so the squared \(L^2\) shift error has exponent \(1/2\). The exponent for the unsquared \(L^2\) norm would be \(1/4\); the candidate explicitly states the squared-error convention and makes no exponent error.

### 5.5 Uniformity over all admissible GD widths

Estimate (15) alone would leave a nonzero error when \(\tau\downarrow0\) at a fixed GD width. The candidate supplies the additional estimate needed to remove it.

For \(0<\tau\le\eta\), a held \(v\) can change between \(t\) and \(t+\tau\) only if that interval crosses a grid node. There are at most \(T/\eta\) internal nodes, and each contributes at most \(\tau\) to the measure of the possible starting times. At every such time,

\[
 \frac1n\sum_i|v_i(t+\tau)-v_i(t)|^2
 \le2\frac1n\sum_i|v_i(t+\tau)|^2
       +2\frac1n\sum_i|v_i(t)|^2
 \le4K^2.
\]

Consequently the squared shift integral \(D_v(\tau)\) satisfies

\[
 D_v(\tau)
 \le4TK^2\min(1,\tau/\eta).
\]

Combining this with (15) gives

\[
 D_v(\tau)
 \le\min\left\{
       C_T(\tau+\eta)^{1/2},
       4TK^2\min(1,\tau/\eta)\right\}.
\]

For \(0<\tau<1\):

1. If \(\eta\le\tau^{2/3}\), then \(\tau+\eta\le2\tau^{2/3}\), so the first bound is \(O(\tau^{1/3})\).
2. If \(\eta>\tau^{2/3}\), then \(\eta>\tau\), so the second bound is at most \(4TK^2\tau^{1/3}\).

This proves a single modulus for all admissible widths, including fixed widths. It is not merely an estimate obtained by taking \(n\to\infty\) before taking \(\tau\to0\).

### 5.6 The within-step change in \(s\) is correctly retained

The node-crossing argument cannot be applied directly to \(s\), because \(\phi_1'(z(t))\) can vary inside a step. The candidate instead uses

\[
\begin{aligned}
 \Delta_\tau s_i
 ={}&\phi_1'(z_i(t+\tau))\odot\Delta_\tau v_i\\
 &+[\phi_1'(z_i(t+\tau))-\phi_1'(z_i(t))]
                                  \odot v_i(t).
\end{aligned}
\]

The first term has squared \(L^2\) norm at most \(P_1^2D_v(\tau)\).

Call the second term \(B_i(t)\). Its \(L^1\) norm is bounded by

\[
 \int|B|\,d\nu
 \le L_1\|\Delta_\tau z\|_{L^2(\nu)}
                    \|v\|_{L^2(\nu)}
 \le C_T\tau.
\]

The bounded derivative gives the separate cubic estimate

\[
 \int|B|^3\,d\nu
 \le(2P_1)^3\int|v|^3\,d\nu\le C_T.
\]

Interpolation now gives \(\int|B|^2\,d\nu\le C_T\tau^{1/2}\). Finally,

\[
 \int|\Delta_\tau s|^2\,d\nu
 \le2P_1^2D_v(\tau)+2C_T\tau^{1/2}
 \le C_T\tau^{1/3}.
\]

No fourth moment of pointwise velocity is assumed here.

**Finding:** (11)–(15), the step-size elimination, and the recomputed activation-velocity argument are all correct. The proof establishes precisely the moduli claimed in (5).

## 6. Elementary compactness in the specified \(W_2\) space

Source: lines 307–351.

Let

\[
 \mathcal E
 =C([0,T];\mathbb R^2)\times L^2([0,T];\mathbb R^2)
       \times C([0,T];\mathbb R^2)\times L^2([0,T];\mathbb R^2)
\]

with the product norm in the candidate, and write

\[
 X_i=(z_i,v_i,h_i,s_i),
 \qquad
 \mu=\frac1n\sum_i\delta_{X_i}.
\]

### 6.1 Velocity projection errors follow from the shift bound

Choose an equal-cell partition with \(h=T/N<\min(1,T)\). For a cell \(I\), expansion of the square gives

\[
 \int_I|v-\operatorname{avg}_Iv|^2
 =\frac1{2h}\int_I\int_I|v(t)-v(s)|^2\,ds\,dt.
\]

By symmetry in \(s,t\), summing over cells and writing \(\tau=|t-s|\) yields

\[
 \frac1n\sum_i\|v_i-P_hv_i\|_{L^2}^2
 \le\frac1h\int_0^h
       \frac1n\sum_i\int_0^{T-\tau}
                    |\Delta_\tau v_i(t)|^2\,dt\,d\tau.
\]

The restriction that both times lie in the same cell can be discarded for this upper bound. Applying (5) gives \(O(h^{1/3})\); the same calculation applies to \(s\). This argument deals directly with the finite interval and does not need an extension past its endpoints.

### 6.2 Uniform position projection errors follow from absolute continuity

For \(t=a+\theta h\) in a cell \([a,a+h]\),

\[
 z(t)-\Pi_hz(t)
 =(1-\theta)\int_a^t v(r)\,dr
       -\theta\int_t^{a+h}v(r)\,dr.
\]

Cauchy–Schwarz bounds its square by

\[
 \theta(1-\theta)h\int_a^{a+h}|v(r)|^2\,dr
 \le\frac h4\int_0^T|v(r)|^2\,dr.
\]

Taking the supremum over cells and times and then averaging gives an \(O(h)\) squared uniform error. Replacing \(z,v\) by \(h_i,s_i\) gives the same estimate for the activation position.

Therefore the explicit coupling

\[
 X_i\longmapsto
 F_hX_i:=(\Pi_hz_i,P_hv_i,\Pi_hh_i,P_hs_i)
\]

has mean squared cost at most \(C_T(h^{1/3}+h)\). This is a coupling in the joint product space, preserving the pairing of each neuron's four paths.

The projections need not preserve the nonlinear identity \(h=\phi_1(z)\). They are approximation centers in the ambient space; the proof does not require them to be network trajectories.

### 6.3 The required tail control is a fourth moment of the product path norm

The first estimate in (9) says

\[
 \frac1n\sum_i\|v_i\|_{L^2}^4\le C_T.
\]

Also

\[
 \|s_i\|_{L^2}^4\le P_1^4\|v_i\|_{L^2}^4,
 \qquad
 \|h_i\|_\infty^4\le4B_1^4,
 \qquad
 \frac1n\sum_i\|z_i\|_\infty^4\le8m+C_T.
\]

Since the square of a sum of four nonnegative numbers is at most four times the sum of their squares,

\[
 \int\|X\|_{\mathcal E}^4\,d\mu(X)\le M_{T,m}
\]

for a uniform finite constant depending also on the fixed deterministic controls and activation bounds.

Both component projections are contractions in their respective norms: averaging contracts \(L^2\), and polygonal interpolation of node values contracts the uniform norm. Thus the same fourth-moment bound holds for \(F_h{}_\#\mu\).

This is enough to control second-moment tails, which is essential for \(W_2\) rather than merely weak compactness.

### 6.4 Finite-dimensional approximation gives total boundedness

For fixed \(h\), the range of \(F_h\) is a finite-dimensional subspace of \(\mathcal E\). For a projected random tuple \(Y\), replacing \(Y\) by zero outside the radius-\(R\) ball costs

\[
 \mathbb E[\|Y\|_{\mathcal E}^2
                    \mathbf1_{\{\|Y\|_{\mathcal E}>R\}}]
 \le R^{-2}\mathbb E\|Y\|_{\mathcal E}^4
 \le M_{T,m}/R^2.
\]

A finite mesh in that finite-dimensional ball then approximates the truncated tuples at arbitrarily small squared cost.

For completeness, probability laws on the resulting finite grid are totally bounded in \(W_2\): keep the common mass at each grid point and transport the unmatched mass. If the grid diameter is \(D\), the resulting squared cost between mass vectors \(p,q\) is at most

\[
 D^2\,\frac12\sum_j|p_j-q_j|.
\]

The finite probability simplex has finite meshes in this ordinary finite-dimensional distance. Hence the projected laws are totally bounded in \(W_2\).

Choosing \(h\) first, then \(R\), then the spatial and mass meshes, and using the vanishing coupling error from Section 6.2 proves total boundedness of the original family. The construction does not mistake bounded moments in an infinite-dimensional ball for compactness.

### 6.5 The supplied completeness argument is sufficient

The source gives an elementary construction specialized to the finite empirical laws. Its details can be made explicit as follows.

From a \(W_2\)-Cauchy sequence of such laws, choose a subsequence \(\mu_j\) whose successive \(W_2\) distances are below \(2^{-j-1}\). By the definition of the infimum, choose finite transport tables with root-mean-square costs below \(2^{-j}\).

Start with the finite distribution \(\mu_1\). Split intervals of a unit interval according to the conditional transition probabilities of the first transport table, then split each resulting interval according to the next table, and continue. Conditional probabilities from zero-mass states are immaterial. This gives random tuples \(X_j\) on one probability space with the prescribed laws and consecutive pair couplings.

They satisfy

\[
 \sum_j
 \bigl(\mathbb E\|X_{j+1}-X_j\|_{\mathcal E}^2\bigr)^{1/2}
 <\infty.
\]

Consequently

\[
 \mathbb E\sum_j\|X_{j+1}-X_j\|_{\mathcal E}<\infty,
\]

so the increments are absolutely summable almost surely. Completeness of the product of the ordinary \(C\) and \(L^2\) spaces gives an almost-sure limit \(X\).

Minkowski's inequality for finite tails and then passage to the limit give

\[
 \bigl(\mathbb E\|X-X_j\|_{\mathcal E}^2\bigr)^{1/2}
 \le\sum_{\ell\ge j}
       \bigl(\mathbb E\|X_{\ell+1}-X_\ell\|_{\mathcal E}^2\bigr)^{1/2}
 \longrightarrow0.
\]

Since \(X_1\) has finite second moment, so does \(X\). Its law is therefore in \(\mathcal P_2(\mathcal E)\), and these couplings prove \(W_2\) convergence.

This verifies the source's summability claim. If its word “cost” is interpreted as squared cost below \(2^{-j}\), the resulting \(L^2\) increments are bounded by \(2^{-j/2}\), which are also summable; either convention works.

To pass from the family to its closure, approximate the \(j\)-th member of a Cauchy sequence in the closure by a finite empirical law within \(1/j\). The approximating sequence is Cauchy and has a convergent subsequence by the construction above, hence so does the original sequence. Combining this property with total boundedness gives sequential compactness of the closure. The usual elementary finite-net argument in metric spaces gives open-cover compactness as well.

No general transport compactness theorem, general gluing theorem, or infinite-product existence theorem is needed for this construction.

### 6.6 Compatibility identities are closed in the claimed topology

Suppose \(z_j\to z\) and \(h_j\to h\) uniformly, and \(v_j\to v\) and \(s_j\to s\) strongly in \(L^2\), with the three identities in the source holding for each \(j\).

The integration map is continuous because

\[
 \sup_t\left|\int_0^t(v_j-v)\right|
 \le\sqrt T\,\|v_j-v\|_{L^2}.
\]

Thus \(z(t)=z(0)+\int_0^t v\). Bounded \(\phi_1'\) gives

\[
 \|\phi_1(z_j)-\phi_1(z)\|_\infty
 \le P_1\|z_j-z\|_\infty,
\]

so \(h=\phi_1(z)\). Finally,

\[
\begin{aligned}
 \|\phi_1'(z_j)\odot v_j-\phi_1'(z)\odot v\|_{L^2}
 \le{}&P_1\|v_j-v\|_{L^2}\\
 &+L_1\|z_j-z\|_\infty\|v\|_{L^2}
 \longrightarrow0.
\end{aligned}
\]

Therefore \(s=\phi_1'(z)\odot v\). The set of compatible tuples is closed. Applying the preceding coupling construction to a convergent subsequence of empirical laws shows that the limit law is supported on this set.

These identities concern only the retained first-layer positions and velocities. They do not identify \(q^{(1)}\), and the compactness proof does not require such identification.

**Finding:** the proof establishes compact closure in the actual strong \(W_2\) space in (6), including second-moment tail control and compatibility of the joint limits.

## 7. Gaussian initialization, probability quantifiers, and endpoint covariance

Source: lines 353–374.

### 7.1 Middle-layer operator norm

A maximal \(1/4\)-separated subset of the unit sphere is a \(1/4\)-net. The radius-\(1/8\) balls around its points have disjoint interiors and lie in the radius-\(9/8\) ball. Comparing volumes gives at most \(9^n\) points.

For unit vectors \(u,v\), choose net points \(u_0,v_0\). For any real matrix \(A\),

\[
 |u^TAv-u_0^TAv_0|
 \le |(u-u_0)^TAv|+|u_0^TA(v-v_0)|
 \le\tfrac12\|A\|_{\rm op}.
\]

Taking the supremum gives

\[
 \|A\|_{\rm op}\le2\max_{u_0,v_0}|u_0^TAv_0|.
\]

For fixed unit net vectors and the prescribed \(W^{(2)}\), the scalar \(u_0^TW^{(2)}v_0\) is Gaussian with variance

\[
 \frac1n\sum_{i,j}u_{0,i}^2v_{0,j}^2=\frac1n.
\]

The elementary two-sided Gaussian tail bound gives probability at most \(2e^{-8n}\) of exceeding four in absolute value. A union bound over at most \(9^{2n}\) pairs gives

\[
 \Pr(\|W^{(2)}\|_{\rm op}>8)
 \le2e^{-(8-2\log9)n}.
\]

The exponent is positive: \(8-2\log9>0\).

### 7.2 Readout infinity norm

The notation \(N(0,n^{-2})\) specifies variance \(n^{-2}\), so the standard deviation is \(1/n\). At threshold one,

\[
 \Pr(|W^{(3)}_i|>1)\le2e^{-n^2/2}.
\]

Union over the \(n\) coordinates gives \(2ne^{-n^2/2}\), as in (16).

### 7.3 Initial first-layer fourth moment

Each first-layer sample pair is centered Gaussian with covariance \(C\), and different rows are independent. This follows directly from

\[
 \mathbb E[z^{(1)}_{a,i}(0)z^{(1)}_{b,i}(0)]
 =\frac1d x_a^Tx_b=C_{ab}.
\]

Let \(\rho=C_{12}\). One representation valid for the entire interval \([-1,1]\) is

\[
 G_1=X,\qquad G_2=\rho X+\sqrt{1-\rho^2}\,Y,
\]

with independent scalar standard Gaussians \(X,Y\). It follows that

\[
 \mathbb E(G_1^2G_2^2)=3\rho^2+(1-\rho^2)=1+2\rho^2.
\]

Consequently

\[
 \mathbb E|G|^4
 =3+3+2(1+2\rho^2)
 =8+4\rho^2\le12.
\]

For the eighth moment,

\[
 |G|^8=(G_1^2+G_2^2)^4
 \le8(G_1^8+G_2^8),
\]

and the scalar Gaussian moment recursion gives \(\mathbb EG_a^8=105\). Thus

\[
 \mathbb E|G|^8\le1680.
\]

Let \(Y_i=|z_i(0)|^4\). Then

\[
 \mathbb EY_i\le12,
 \qquad
 \operatorname{Var}(Y_i)\le1680.
\]

Independence across rows gives

\[
 \operatorname{Var}\left(\frac1n\sum_iY_i\right)\le\frac{1680}{n}.
\]

The event \(\frac1n\sum_iY_i>13\) requires a positive deviation from its mean of at least one. The second-moment Markov inequality therefore gives the first term \(1680/n\) in (16).

At \(\rho=\pm1\), the representation reduces to \(G=(X,\pm X)\). It remains valid without a nonsingular two-dimensional Gaussian density. In fact, at these endpoints \(\mathbb E|G|^4=12\) and \(\mathbb E|G|^8=1680\), so the chosen bounds cover the extremal covariance cases exactly at the level of these raw moments.

### 7.4 The correct probability statement

Define the initialization event

\[
 E_n=\left\{
   \|W^{(2)}(0)\|_{\rm op}\le8,\ 
   \|W^{(3)}(0)\|_\infty\le1,\ 
   \frac1n\sum_i|z_i(0)|^4\le13
   \right\}.
\]

The three preceding calculations and a union bound give

\[
 \Pr(E_n^c)\le b_n,
 \qquad b_n\longrightarrow0.
\]

For fixed \(T\), activations, and the specified input setup, let \(\mathcal K\) be the deterministic compact closure supplied by the deterministic theorem with \(a=8,b=1,m=13\), including GF and all admissible GD widths.

Then

\[
 \Pr(\mu_n^{\rm GF}\in\mathcal K)\ge1-b_n
\]

for every width, and

\[
 \Pr(\mu_n^{\rm GD}\in\mathcal K)\ge1-b_n
\]

for \(n\ge n_0\). If both schemes are run from the same initialization at such a width, the same event \(E_n\) ensures both inclusions, so their simultaneous inclusion also has probability at least \(1-b_n\).

Equivalently, for every \(\varepsilon>0\), all sufficiently large widths have containment probability at least \(1-\varepsilon\) in this fixed deterministic compact set.

For small \(n\), \(b_n\) can exceed one; then the displayed lower bound is merely vacuous. This does not affect the asymptotic assertion. The \(1680/n\) estimate is not summable, and it supplies no claim of almost-sure eventual containment across a sequence of widths. The source does not make that stronger claim.

The proof also does not need independence of trained neurons. Independence is used only for the specified initial Gaussian entries and initial first-layer rows.

**Finding:** all three terms of (16), the compact-containment interpretation, and the singular-covariance cases are correct.

## 8. Required corrections versus optional exposition

### Required corrections

None found.

No extra positive gate assumption, Gram-matrix invertibility, higher activation derivative, pointwise fourth velocity moment, GF/GD comparison, or mean-field theorem is needed to complete the stated argument.

### Optional clarifications

1. **Label the continuous work identity explicitly as the GF identity** at lines 184–191. The following GD paragraph supplies the correct separate discrete argument, so the intended scope is clear. An explicit “For GF” would prevent a reader from applying the continuous identity to held-node \(u\) and recomputed GD \(h\).

2. **State the partition choice as \(h=T/N\)** at line 309. This makes the exact cell-length denominator in the projection identity immediate. Such a sequence of partitions is already sufficient for the proof.

3. **Display the dependence on \(m\) in the compactness tail constant** at lines 323–329, for example as \(M_{T,m}\). Equation (9) already makes this dependence explicit; the deterministic velocity constants do not need \(m\).

4. **Specify root-mean-square or squared transport cost in the completeness paragraph** at lines 334–339. Both readings of its geometric bound give summable \(L^2\) increments, so this is a terminology clarification.

5. **Write the event \(E_n\) and the inclusion-probability statement explicitly** at lines 353–374. This would make the fixed-horizon, per-width probability quantifiers and the restriction \(n\ge n_0\) for GD especially easy to verify.

These points are editorial. None repairs a failed mathematical inference, and none is a condition for accepting the compactness candidate.

## 9. Final assessment within the requested scope

The proof supplies the finite dynamics and time regularity that its compactness conclusion needs. Its delicate steps withstand direct checks: the first-exit Hessian grows only like \(1+\sqrt n\); the discrete row-work error is absorbable at \(\eta=n^{-2}\); the cubic gain averages a controlled second moment of rowwise variation; the nonlinear shift product is estimated in \(L^1\); the step-size modulus handles within-step activation changes; and the \(W_2\) argument includes both finite-dimensional approximation and uniform second-moment tails.

The probability estimates are uniform over the allowed two-input Gram matrices, including \(\rho=\pm1\), and justify the stated containment in probability. The document's exclusions remain appropriate: this first-layer compactness result does not by itself identify a limiting driving field or establish any of the explicitly excluded mean-field conclusions.

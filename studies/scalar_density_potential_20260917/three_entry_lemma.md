# Three-input finite-time entry lemma

This is a finite-time perturbation result for the exact scalar population
flow in `potential.md`. It does not prove fitting or exponential convergence
for any fixed three-input dataset. The proof uses the pair theorem in that
file and its physical dissipation identity. No simulation is used.

Write \(u(\theta)=(\cos\theta,\sin\theta)\), and use physical inputs
\(x_i=\sqrt2u(\theta_i)\), where

\[
\theta_1=\pi/3+\varepsilon,\quad
\theta_2=\pi/3-\varepsilon,\quad \theta_3=2\pi/3.
\]

The labels are \((1,1,-1)\), weights are \((1/4,1/4,1/2)\), and the
initialization, including the fixed scalar dictionary, is exactly that of
`potential.md`. Denote the resulting loss by \(\mathcal L_\varepsilon\).
At \(\varepsilon=0\), combining the duplicated positive input gives
the proved opposite-label reflected pair with \(\delta=1/2\). Let
\(K_0>0\) be that pair's initialized upper activation norm squared.

**Lemma.** For every \(\ell>0\), there are \(T<\infty\) and
\(\varepsilon_0>0\) such that

\[
0<\varepsilon<\varepsilon_0
\quad\Longrightarrow\quad \mathcal L_\varepsilon(T)<\ell.
\]

For \(0<\ell<2\), one may take
\(T=\log(2/\ell)/(4K_0)\). For arbitrary \(\ell>0\), the uniformly
valid choice replaces \(\ell\) in this formula by
\(\bar\ell=\min\{\ell,1\}\). Each of the datasets with
\(0<\varepsilon<\min\{\varepsilon_0,\pi/6\}\) consists of three
distinct, non-antipodal inputs, and its three upper readout constraints are
linearly independent at initialization.

## Hilbert continuity estimate without a bounded-Gaussian assumption

Use the original fixed carriers and the Hilbert state space

\[
\mathcal H=L^2(P_1;\mathbb R^2)\times L^2(P_2;\mathbb R)\times\mathbb R,
\qquad X=(w,c,M).
\]

The Gaussian initial state \(w=g\) belongs to \(L^2\); no bound on
\(\|g\|_\infty\) is assumed. Put \(B_i=\|b_i\|_\infty<\infty\),
and use \(|\phi|,|\phi'|\le1\), \(|\phi''|\le2\). For states
\(X,\widetilde X\) in a Hilbert ball of radius \(R\ge1\), and normalized
inputs \(|u|,|\widetilde u|\le1\), write

\[
D_w=\|w-\widetilde w\|_2,\quad D_c=\|c-\widetilde c\|_2,
\quad D_M=|M-\widetilde M|,\quad D_u=|u-\widetilde u|.
\]

All quantities with tildes are evaluated at \((\widetilde X,\widetilde u)\).
The basic estimates are

\[
|a-\widetilde a|\le B_1(D_w+R D_u),\qquad |a|\le B_1,
\]
\[
\|H-\widetilde H\|_\infty
\le B_2\{B_1D_M+R|a-\widetilde a|\}=:Q,
\]
\[
|f-\widetilde f|\le D_c+RQ,\qquad |f|\le R,
\]
\[
|d-\widetilde d|\le B_2D_c+2B_2RQ,\qquad |d|\le B_2R.
\]

For the lower derivative vector \(P=b_1\phi'(w\cdot u)u\),

\[
\|P\|_2\le B_1,\qquad
\|P-\widetilde P\|_2
\le B_1\{2(D_w+R D_u)+D_u\}.
\]

For example, the input variation in the first estimate is bounded by
\(E|b_1\widetilde w\cdot(u-\widetilde u)|
\le B_1\|\widetilde w\|_2D_u\). The analogous gate estimate uses
\(\|\widetilde w\cdot(u-\widetilde u)\|_2\le R D_u\).
These are \(L^2\) estimates, not uniform bounds on the Gaussian marks.

For fixed labels and weights, the exact vector field consists of sums of
the products

\[
-2p_i r_i M d_iP_i,\qquad -2p_i r_iH_i,
\qquad -2p_i r_id_ia_i.
\]

Here \(|r_i|\le R+1\). Telescoping each product and applying the displayed
bounds gives a finite constant \(C_R\), depending only on
\(R,B_1,B_2\), such that

\[
\|V_U(X)-V_{\widetilde U}(\widetilde X)\|_{\mathcal H}
\le C_R\left(\|X-\widetilde X\|_{\mathcal H}
             +\max_i|u_i-\widetilde u_i|\right).
\]

This establishes joint local Lipschitzness in Hilbert state and inputs.
The same residual estimates give a constant \(D_R<\infty\) with

\[
|\mathcal L_U(X)-\mathcal L_{\widetilde U}(\widetilde X)|
\le D_R\left(\|X-\widetilde X\|_{\mathcal H}
             +\max_i|u_i-\widetilde u_i|\right),
\]

since \(|r_i^2-\widetilde r_i^2|\le2(R+1)|r_i-\widetilde r_i|\).

All trajectories here have initial loss one. Dissipation therefore gives,
uniformly in \(\varepsilon\),

\[
\int_0^T\|\dot X_\varepsilon(t)\|_{\mathcal H}^2\,dt\le1,
\qquad
\sup_{t\le T}\|X_\varepsilon(t)\|_{\mathcal H}
\le\|X(0)\|_{\mathcal H}+\sqrt T.
\]

Choose \(R\) larger than this last bound. Since
\(\max_i|u_i(\varepsilon)-u_i(0)|\le\varepsilon\), the integral
equations and Gronwall's inequality give, enlarging \(C_R>0\) if needed,

\[
\|X_\varepsilon(t)-X_0(t)\|_{\mathcal H}
\le\varepsilon(e^{C_Rt}-1),\qquad 0\le t\le T.
\]

Consequently

\[
|\mathcal L_\varepsilon(T)-\mathcal L_0(T)|
\le D_R\varepsilon e^{C_RT}.
\]

## Entry and independence

The pair proof gives directly
\(\dot{\mathcal L}_0=-4\Theta\mathcal L_0\), with
\(\Theta\ge K_0\) and \(\mathcal L_0(0)=1\). Hence

\[
\mathcal L_0(T)\le e^{-4K_0T}=\bar\ell/2.
\]

This uses the direct loss equation; there is no extra factor
\(\Phi_0=1/K_0\). For example, the choice

\[
\varepsilon_0=\min\left\{\frac\pi6,
\frac{\bar\ell}{2D_Re^{C_RT}}\right\}
\]

gives \(\mathcal L_\varepsilon(T)<\bar\ell\le\ell\) whenever
\(0<\varepsilon<\varepsilon_0\).

For independence, let \(q_i=\cos\theta_i\). If \(0<\varepsilon<\pi/6\),

\[
0<q_1<\frac12<q_2<1,\qquad q_3=-\frac12.
\]

The initialized Gaussian covariance formula in the pair proof is
\(a_i(0)=A(q_i)/\sqrt{\nu+\eta}\), where \(A\) is odd and strictly
increasing. Thus \(s_i=M_0a_i(0)\) are nonzero and their squares are
distinct. The upper mark law has positive density near zero. Any relation
\(\sum_i v_i\tanh(bs_i)=0\) in its \(L^2\) space therefore holds on
an interval by continuity. Its first, third and fifth derivatives at zero
give

\[
\sum_i v_i s_i=\sum_i v_i s_i^3=\sum_i v_i s_i^5=0.
\]

The coefficients of these tanh Taylor terms are nonzero. This is a
Vandermonde system in the distinct values \(s_i^2\), after multiplying
each unknown by its nonzero \(s_i\); therefore all \(v_i=0\).
The initialized three-by-three readout Gram, weighted or unweighted, is
strictly positive definite. Thus no readout fitting constraint is redundant.

The angles are distinct and all pairwise differences have magnitude less
than \(\pi\), so there is no antipodal pair. The perturbation is genuinely
three-input, even though its zero-perturbation comparison has a duplicated
positive input.

The quantifiers matter: \(\varepsilon_0\) depends on the requested loss
level \(\ell\). This argument does not give one fixed nonzero
\(\varepsilon\) for every loss level, does not prove that the readout Gram
stays invertible, and does not establish an all-time decaying potential.

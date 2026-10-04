# Finite mixed moments: an averaged sensitivity reduction and a transport route

2026-10-03. Scoped internal proof attempt, restricted to the canonical dense
network with two tanh hidden layers, zero initial readout, fixed finite data,
and the small-label fitting event. Input orthogonality is not assumed.

**Status.** The required finite exponential carrier moment remains open. This
note proves a conditional, deterministic finite-width sensitivity estimate
that uses an empirical exponential carrier budget rather than a carrier
maximum. It includes the derivative of the adaptive residual. It also gives
the exact finite Gaussian integration-by-parts identity, a sufficient
Gaussian transport lemma, and the unresolved domain and mixed-response
requirements. Neither population Gaussian marginals nor a finite-to-population
rate is used. No root-width comparison theorem is claimed.

Scientific inputs were the complete current `paper/main.tex`, complete
`paper/results.tex`, `paper/proof_alltime.tex`, and
`paper/proof_tracking.tex`, and this study's complete `FINITE_TAIL_ROUTE.md`
and `NONORTHOGONAL_TAIL_ROUTE.md`. The canonical-notation skill and its neural
reference, the conjecture-investigation skill and its contract/audit
references, and the rigorous-proof skill were applied. There were no
experiments, other-study reads, Git operations, or manuscript edits.

## 1. Actual finite-network target

Write \(v_a=x_a/\sqrt d\), \(G_{ab}=v_a^\top v_b\), and
\[
 z_a^{(1)}=Av_a,\quad h_a=\tanh z_a^{(1)},\quad
 z_a^{(2)}=Wh_a,\quad h_a^{(2)}=\tanh z_a^{(2)},\quad
 f_a=n^{-1}w^\top h_a^{(2)}.
\]
Here \(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\), and
\(w\in\mathbb R^n\). The residual is \(r_a=f_a-y_a\), its RMS is
\(\rho=(m^{-1}\sum_a r_a^2)^{1/2}\), and the loss is \(\rho^2\).
Define the gates and responses
\[
 g_a=\operatorname{sech}^2 z_a^{(1)},\qquad
 \gamma_a=\operatorname{sech}^2 z_a^{(2)},\qquad
 \delta_a=w\odot\gamma_a,\qquad k_a=W^\top\delta_a.
\]
All unlabelled fields below belong to this dense finite network.

Put \(db_a=-2r_a\,dt/m\). The equations are
\[
 dA=\sum_a(g_a\odot k_a)v_a^\top db_a,\qquad
 dw=\sum_a h_a^{(2)}db_a,\qquad
 dW=n^{-1}\sum_a\delta_a h_a^\top db_a.                 \tag{1}
\]
On the manuscript's fitting event \(\mathcal G_n\), choose fixed constants
\(K,\kappa>0\) so that
\[
 \rho(t)\le Ye^{-\kappa t},\quad
 \|W(t)\|_{\rm op}\le K,\quad
 \Gamma_w(t)\succeq cI_m,
 \qquad S=2Y/\kappa\le1.                               \tag{2}
\]
The constants may depend on the fixed data and Gram gap. Assume \(Y>0\);
zero labels give a stationary path.

The activity measure and the largest sample carrier at neuron \(i\) are
\[
 d\mu(t)=\frac2m\sum_a|r_a(t)|\,dt,\qquad
 K_i(t)=\max_a|k_{a,i}(t)|.
\]
They satisfy
\[
 \mu([0,\infty))\le S,\qquad
 d\mu(t)\le\kappa S e^{-\kappa t}dt,\qquad
 \rho(t)dt\le\frac{\sqrt m}{2}\,d\mu(t).                \tag{3}
\]
For a fixed positive exponential parameter \(\eta\), define the actual
finite empirical budget
\[
 \mathcal M_\eta
 =\kappa\int_0^\infty e^{-\kappa t}
       \frac1n\sum_{i=1}^n
            \exp\{\eta K_i(t)/S\}\,dt.                 \tag{4}
\]
This definition has a deterministic time weight. Differentiating it with
respect to initialization therefore does not introduce a derivative of the
residual weight. It is not a population marginal quantity.

**Sufficient target.** A bound
\[
 \mathbb E[\mathbf1_{\mathcal G_n}\mathcal M_\eta]\le C   \tag{5}
\]
with fixed \(\eta,C>0\), independent of width and small labels, implies the
requested simultaneous exponential finite tails. Indeed, on
\(\mathcal M_\eta\le L\), for \(R\ge1\),
\[
 \begin{aligned}
 Z_n(SR)
 &:=\mathbf1_{\mathcal G_n}\int_0^\infty\rho(t)
       \max_a\frac{\|k_a(t)\mathbf1_{|k_a(t)|>SR}\|_2}{\sqrt n}\,dt\\
 &\le C_\eta S^2\sqrt L\,e^{-\eta R/4}.                \tag{6}
 \end{aligned}
\]
To verify this, use
\(x^2\mathbf1_{x>R}\le C_\eta e^{-\eta R/2}e^{\eta x}\)
for \(x\ge0\), take the empirical square root, and apply
Cauchy--Schwarz in the measure \(d\mu\). Equation (3) gives
\(\int n^{-1}\sum_i e^{\eta K_i/S}d\mu\le S\mathcal M_\eta\).
The readout tail vanishes for \(R\ge1\), since \(\|w\|_\infty\le S\).
The ordinary RMS bounds cover \(0\le R<1\) after increasing the constant.
Thus the conclusion holds simultaneously for every real cutoff. Markov's
inequality applied to (5), with \(L=C/\delta\), would give
\(Z_n(YR)\le C_\delta Y^2e^{-aR}\) on an event of probability at least
\(1-\delta-\Pr(\mathcal G_n^c)\), with fixed \(a>0\).

Equation (5), not the deduction (6), is unresolved.

## 2. Full finite variational equation, including adaptation

Use the mobility-Euclidean coordinates
\[
 H=\sqrt nW,\qquad \Theta=(A,H,w),\qquad
 \mathcal F_a(\Theta)=w^\top\tanh((H/\sqrt n)\tanh(Av_a))=nf_a.
\]
The Euclidean inner product is the sum of the Frobenius/Euclidean inner
products of the three blocks. Equation (1) reads
\[
 \dot\Theta=-\frac2m\sum_a r_a\nabla\mathcal F_a.
\]
For the derivative \(J(t)=D_{\Theta(0)}\Theta(t)\), the exact equation is
\[
 \dot J=(-L L^\top+\rho\mathcal A)J,\qquad J(0)=I,
 \quad
 L=\sqrt{\frac2{mn}}\,[\nabla\mathcal F_a]_{a=1}^m,
 \quad
 \rho\mathcal A=-\frac2m\sum_a r_a\nabla^2\mathcal F_a.  \tag{7}
\]
At a zero residual the last expression defines the product without division.
The negative semidefinite term \( -LL^\top\) is exactly the derivative of
the adaptive residual. Treating the integrated residual as a deterministic
driver would omit it. For deterministic prescribed drivers it is absent.

Here is the full Hessian, which also identifies every mixed block. For
variations \(U=(U_A,U_H,U_w)\), \(V=(V_A,V_H,V_w)\), put
\[
 \alpha_U=U_Av_a,\quad
 z_U=W(g_a\odot\alpha_U)+U_Hh_a/\sqrt n,
\]
and define \(\alpha_V,z_V\) in the same way. With
\(g_a'=-2h_a\odot g_a\) and
\(\gamma_a'=-2h_a^{(2)}\odot\gamma_a\),
\[
\begin{aligned}
 D^2\mathcal F_a[U,V]
 ={}&U_w^\top\operatorname{diag}(\gamma_a)z_V
     +V_w^\top\operatorname{diag}(\gamma_a)z_U\\
 &+z_U^\top\operatorname{diag}(w\odot\gamma_a')z_V\\
 &+\frac1{\sqrt n}\delta_a^\top
       \{U_H(g_a\odot\alpha_V)+V_H(g_a\odot\alpha_U)\}\\
 &+k_a^\top(g_a'\odot\alpha_U\odot\alpha_V).            \tag{8}
\end{aligned}
\]
The last line gives a block diagonal operator on the \(A\) rows. Its \(i\)th
block is \(k_{a,i}g'_{a,i}v_av_a^\top\). The first four lines have operator
norm at most a fixed \(C\): the \(z_U\) map has bounded operator norm,
\(\|w\|_\infty\le S\), and \(\|\delta_a\|_2/\sqrt n\le S\).
Their rank is at most \(5n\): the readout cross terms have rank at most
\(2n\), the top curvature at most \(n\), and the \(A,H\) mixed pair at most
\(2n\). Summing over the fixed samples preserves a rank bound \(Cn\).

This rank statement matters. The total parameter dimension is of order
\(n^2\), but the instantaneous Hessian acts through only \(O(n)\) directions.

## 3. A proved conditional averaged sensitivity bound

Let \(U_0(t,s)\) be the propagator of \(\dot u=-L(t)L(t)^\top u\).
It is a contraction: differentiating \(\|u\|_2^2\) gives
\(-2\|L^\top u\|_2^2\le0\).

For a finite matrix \(B\), define its normalized Schatten norm by
\[
 \|B\|_{p,n}=(n^{-1}\operatorname{tr}|B|^p)^{1/p},\qquad p\ge2.
\]
The normalization is by \(n\), even on the full parameter space. The
Schatten Hölder inequality used below is
\(\|B_1\cdots B_j\|_{2,n}\le\prod_{r=1}^j\|B_r\|_{2j,n}\).
It applies to finite rectangular or square products of compatible sizes;
operator-norm contractions inserted between the factors do not increase
the right side.

Write the residual-Hessian part of (7) as \(\mathcal B(t)d\mu(t)\).
Equation (8) gives, for every \(p\ge2\),
\[
 \|\mathcal B(t)\|_{p,n}
 \le C\left[1+
        \left(\frac1n\sum_i K_i(t)^p\right)^{1/p}\right]. \tag{9}
\]
The constant is independent of \(p,n\). To see this, the bounded part has
rank \(Cn\), and the local \(d\times d\) blocks have norms at most
\(CK_i\). The factors \(C^{1/p}\) and \(d^{1/p}\) are bounded for \(p\ge2\).

For integers \(p\ge2\), \(x^p\le p!e^x\) for \(x\ge0\).
Jensen's inequality in \(d\mu\), (3), and (4) imply
\[
 \int\|\mathcal B(t)\|_{p,n}d\mu(t)
 \le CS+C\frac{S^2p}{\eta}\mathcal M_\eta^{1/p}.        \tag{10}
\]
For every finite horizon the Duhamel series for \(J-U_0\) is convergent.
Its term with \(j\) residual Hessians is bounded, using Hölder and the
symmetry of the scalar product integrand over ordered times, by
\[
 \frac1{j!}
 \left[\int\|\mathcal B(t)\|_{2j,n}d\mu(t)\right]^j.
\]
Insert (10), use \((x+y)^j\le2^{j-1}(x^j+y^j)\), and use
\(j!\ge(j/e)^j\). The first resulting series is bounded by \(CS\); the
second is bounded by
\(\sqrt{\mathcal M_\eta}\sum_{j\ge1}(CS^2/\eta)^j\).
Consequently, if \(CS^2\le\eta/2\),
\[
 \sup_{t\ge0}\frac{\|J(t)-U_0(t,0)\|_{\rm HS}}{\sqrt n}
 \le CS+C\frac{S^2}{\eta}\sqrt{\mathcal M_\eta}.        \tag{11}
\]
The constants can be fixed before decreasing the label threshold. For
prescribed deterministic controls, \(U_0=I\). Every statement here is about
the finite network; it is not a limiting response rule.

The estimate also keeps the correct small-label scale for the top response.
Let \(P_H\) embed variations of the initialized \(H\) block and let
\(B_a(t)=D_\Theta\delta_a(t)\). Then
\[
 \|B_a(t)\|_{\rm op}\le C,\qquad
 \sup_t\frac{\|B_a(t)J(t)P_H\|_{\rm HS}}{\sqrt n}
 \le CS+C\frac{S^2}{\eta}\sqrt{\mathcal M_\eta}.        \tag{12}
\]
For completeness, the contraction part in (12) needs an argument; bounding
it by \(C\) would lose the factor \(S\). Split \(L=(L_s,L_w)\) into the
slow blocks \((A,H)\) and the readout block. Along the reference,
\[
 \|L_s\|_{\rm op}\le CS,\quad
 L_w^\top L_w\succeq cI_m,\quad \|L_w\|_{\rm op}\le C,\quad
 \int_0^\infty\|\dot L_w\|_{\rm op}dt\le CS^2.         \tag{13}
\]
The last bound follows from the actual feature-speed estimate
\(\|\dot h_a^{(2)}\|_2/\sqrt n\le CS\rho\).
For \(q=U_0(t,0)P_Hv\), contraction gives \(\|q\|\le\|v\|\).
Let \(P(t)\) project onto the orthogonal complement of the columns of
\(L_w(t)\). The gap in (13) gives
\(\|\dot P\|\le C\|\dot L_w\|\). Since
\((Pq_w)'=\dot Pq_w\), one has \(\|Pq_w\|\le CS^2\|v\|\).
The vector \(p=L_w^\top q_w\) satisfies
\[
 \dot p=\dot L_w^\top q_w-
        (L_w^\top L_w)(p+L_s^\top q_s).
\]
Its damped norm inequality and (13) give \(\|p\|\le CS\|v\|\).
Thus \(\|q_w\|\le CS\|v\|\). Finally
\[
 B_a[U]=\gamma_a\odot U_w+
        (w\odot\gamma_a')\odot D z_a^{(2)}[U]
\]
shows \(\|B_aU_0P_H\|_{\rm op}\le CS\). Its rank is at most \(n\),
so its Hilbert--Schmidt norm is at most \(CS\sqrt n\). Combining with
(11) proves (12).

This is a useful one-way implication: an empirical exponential budget
controls aggregate finite sensitivities, including mixed and adaptive terms.
It does not reverse the implication and does not prove (5).

## 4. Exact column Stein identity and the missing weighted estimate

Fix a neuron \(i\), let \(g_i=\sqrt nW_{0,i}\sim N(0,I_n)\), and condition
on all remaining initialization. Let \(I_i\) embed a column variation in
the \(H\) block. At a fixed physical time define
\[
 U_{a,i}=g_i^\top\delta_a/\sqrt n,\quad
 X_{a,i}=U_{a,i}/S,\quad
 C_{a,i}=D_{g_i}\delta_a=B_aJI_i.
\]
The learned column obeys
\[
 \|W_i-W_{0,i}\|_2\le S^2/(2\sqrt n),\qquad
 |k_{a,i}-U_{a,i}|\le S^3/2.                            \tag{14}
\]
Thus a moment for \(X_{a,i}\) controls the actual carrier, with a bounded
exponential factor \(e^{\eta S^2/2}\).

For a smooth compact localization \(\chi(g_i)\) and a smooth test \(F\),
Gaussian integration by parts gives exactly
\[
\begin{aligned}
 \mathbb E_i[\chi X_{a,i}F(X_{a,i})]
 ={}&\mathbb E_i\!\left[
       \chi\frac{\operatorname{tr}C_{a,i}}{S\sqrt n}F(X_{a,i})\right]\\
 &+\mathbb E_i\!\left[
       \chi\frac{\|\delta_a\|_2^2+g_i^\top C_{a,i}\delta_a}
                    {nS^2}F'(X_{a,i})\right]\\
 &+\mathbb E_i\!\left[
       \frac{\delta_a^\top\nabla\chi}{S\sqrt n}F(X_{a,i})\right].
                                                               \tag{15}
\end{aligned}
\]
The identity follows by differentiating
\(\chi\delta_{a,j}F(X_{a,i})\) in each Gaussian coordinate and summing.
It contains a trace response, a directional response multiplied by the
same Gaussian column, and a localization derivative. No one of those
terms may be omitted. For the actual residual-driven path, \(C_{a,i}\)
contains the negative-Gram contribution in (7).

Equation (12) controls the unweighted aggregate
\[
 \sum_i\|C_{a,i}\|_{\rm HS}^2
   =\|B_aJP_H\|_{\rm HS}^2.
\]
It does not bound the trace or directional response under
\(F(X)=e^{\lambda X}\) with the same exponential parameter. The trace
contraction makes the issue explicit. For weights \(w_i=e^{\lambda X_{a,i}}\),
let \(\mathcal I_w v\) be the \(H\)-block matrix \(vw^\top\). Then
\[
 \sum_i w_i\operatorname{tr}C_{a,i}
       =\operatorname{tr}(B_aJ\mathcal I_w),\qquad
 \|\mathcal I_w\|_{\rm op}=\|w\|_2.                  \tag{16}
\]
Every nonzero singular value of this injection is \(\|w\|_2\).
Consequently a black-box Schatten estimate on (16) reads an empirical
moment at \(2\lambda\). Merely choosing a Schatten exponent close to one
does not change this vector norm. Factoring a diagonal weight on the full
\(n^2\)-dimensional matrix block introduces an unwanted width factor.

This observation does not rule out a more detailed blockwise argument.
It says exactly why (11)--(12) alone fail to close a finite exponential
moment bootstrap. Initial carriers being zero supplies all exponential
parameters at time zero, but a terminal-time inequality involving the
unknown moment at \(2\lambda\) is not yet a causal variable-parameter
estimate. One must derive that additional inequality.

## 5. The full directional system and the reinsertion issue

The following exact linearized system specifies what a blockwise proof must
retain. For a variation write
\[
 \alpha_a=(\Delta A)v_a,\quad \nu=\Delta w,\quad V=\Delta W,
 \quad\eta_a=g_a\odot\alpha_a,
\]
\[
 \zeta_a=Vh_a+W\eta_a,\quad
 \chi_a=\gamma_a\odot\nu+(w\odot\gamma_a')\odot\zeta_a,
 \quad\upsilon_a=V^\top\delta_a+W^\top\chi_a.
\]
For a fixed driver,
\[
\begin{aligned}
 d\alpha_a
  &=\sum_bG_{ab}\{g_b\odot\upsilon_b+
                     (g_b'\odot k_b)\odot\alpha_b\}\,db_b,\\
 d\nu&=\sum_b\gamma_b\odot\zeta_b\,db_b,\\
 dV&=n^{-1}\sum_b(\chi_bh_b^\top+\delta_b\eta_b^\top)\,db_b.
                                                               \tag{17}
\end{aligned}
\]
For the actual driver add respectively
\[
 \sum_bG_{ab}(g_b\odot k_b)\,d(\Delta b_b),\qquad
 \sum_bh_b^{(2)}\,d(\Delta b_b),\qquad
 n^{-1}\sum_b\delta_bh_b^\top\,d(\Delta b_b),
\]
where
\[
 d(\Delta b_b)=-\frac2{mn}
        \{\nu^\top h_b^{(2)}+\delta_b^\top\zeta_b\}\,dt. \tag{18}
\]
These terms are the block version of the negative Gram in (7).

For a column perturbation \(V(0)=E/\sqrt n\), the two initialized-matrix
sources are \(Eh_a/\sqrt n\) and \(E^\top\delta_a/\sqrt n\).
Eliminating \(V-V(0)\) from (17) produces time integrals of these forward
and reverse sources through the same finite response system. In a cavity
reinsertion calculation, a putative leading quadratic form must retain
both sources and all terms in (17)--(18).

In particular, bounds of the form
\(\|J\|_{\rm op}\le n^{o(1)}\) on a maximum-carrier stop do not by
themselves prove a small reinsertion remainder. The third term in
the exact cavity decomposition
\[
 k_{a,i}=W_{0,i}^\top\delta_a^{-i}
       +W_{0,i}^\top(\delta_a-\delta_a^{-i})
       +(W_i-W_{0,i})^\top\delta_a
\]
is \(O(S^3)\). The second term requires either a genuine conditional
quadratic-form expansion with a controlled second variation, or another
finite conditional argument. The cavity response evaluated at the full
network's driver is independent of the omitted column when that driver is
prescribed independently of the column. A cavity generating its own
residual driver is also independent of the column, but comparison then has
different drivers and requires the terms (18). A stop depending on the full
trajectory cannot be conditioned on as if it were independent of the
omitted column.

## 6. A proved Gaussian transport lemma

There is a way to avoid estimating the tilted directional term in (15)
separately. The lemma below is finite dimensional and elementary.

Let \(g\sim N(0,I_N)\), and let \(v:\mathbb R^N\to\mathbb R^N\) be \(C^1\)
with, everywhere,
\[
 \|v\|\le1,\qquad \|Dv\|_{\rm op}\le\ell,\qquad
 |\operatorname{div}v|\le D,\qquad \|Dv\|_{\rm HS}\le H.
\]
For \(\lambda\ge0\) satisfying \(\lambda\ell\le1/2\),
\[
 \mathbb E e^{\lambda g^\top v(g)}
   \le\exp\{\lambda D+\lambda^2(H^2+1/2)\}.           \tag{19}
\]
The same statement applies with \(v\) replaced by \(-v\).

To prove it, \(T(g)=g-\lambda v(g)\) is a global \(C^1\) bijection.
Injectivity follows from its lower Lipschitz bound; for each target \(y\),
the map \(g\mapsto y+\lambda v(g)\) is a contraction and gives the inverse.
The determinant has positive sign by continuation from \(I\), and the
convergent logarithm series gives
\[
 \log\det(I-\lambda Dv)
 \ge-\lambda\operatorname{div}v
     -\sum_{j\ge2}\frac{\lambda^j}{j}
                \|Dv\|_{\rm HS}^2\|Dv\|_{\rm op}^{j-2}
 \ge-\lambda D-\lambda^2H^2.
\]
The change of variables in the Gaussian density therefore gives
\[
 1=\mathbb E\left[
 e^{\lambda g^\top v-\lambda^2\|v\|^2/2}
             \det(I-\lambda Dv)\right]
 \ge e^{-\lambda D-\lambda^2(H^2+1/2)}
             \mathbb E e^{\lambda g^\top v},
\]
which is (19).

For the network, the intended vector field is
\(v(g_i)=\delta_a/(S\sqrt n)\). Its norm is at most one. The other
hypotheses would concern the *finite column response*
\(C_{a,i}/(S\sqrt n)\), and in particular its divergence. This lemma
does not assume Gaussianity of a trained carrier.

There is a useful localized version that avoids a global extension. Fix
\(\lambda\ge0\), with the case \(\lambda=0\) immediate, and let
\(D\subset\mathbb R^N\) be a measurable good domain. Suppose
\(\|v\|\le1\), the divergence bound, and the Hilbert--Schmidt bound hold
on \(D\), while \(\|Dv\|_{\rm op}\le\ell\) holds on its open
\(2\lambda\)-neighborhood and \(\lambda\ell\le1/2\). Then the same proof yields
\[
 \mathbb E[\mathbf1_D e^{\lambda g^\top v(g)}]
 \le\exp\{\lambda D_0+\lambda^2(H^2+1/2)\},             \tag{20}
\]
where \(D_0\) denotes the divergence bound. Indeed, if two points of \(D\)
have the same image under \(T\), their distance is at most \(2\lambda\)
because \(\|v\|\le1\) there. The joining segment lies in the enlarged
domain, so the derivative bound proves injectivity. The change of
variables now gives Gaussian mass of \(T(D)\), which is at most one.
The determinant estimate is needed only on \(D\).

The network domain requirement is therefore concrete: conditional on the
other initialization, the empirical-budget and sensitivity estimates must
remain valid under all fixed-column Gaussian-root perturbations of radius
\(2\lambda\). A trajectory-defined budget domain need not already have this
property. A derivative bound only on that domain does not prove
injectivity. Multiplying \(v\) by a smooth moment cutoff instead creates
\(v\otimes\nabla\chi\); estimating that term requires the carrier-weighted
sensitivity that was missing in (15).

A higher exponential budget can control the derivative of a lower one by
Hölder, so an enlarged domain at a larger exponential parameter is a
plausible route to (20). This still leaves a parameter hierarchy. No
causal estimate with a decreasing parameter has been derived here to close
that hierarchy. Similarly, a maximum-carrier stop of order
\(S\sqrt{\log n}\) gives only \(n^{o(1)}\) generic operator sensitivities;
that alone does not show that fixed-size column perturbations preserve the
same maximum stop.

## 7. Current claim ledger and precise continuation target

| Claim | Status | Scope |
|---|---|---|
| An empirical finite budget (5) implies simultaneous finite tails (6) | Proved conditional implication | Actual dense finite trajectories, all cutoffs and all time |
| Adaptive residual differentiation contributes a negative Gram | Exact | Equation (7), with its block expansion (18) |
| Every mixed Hessian block and its rank are controlled | Proved | Equation (8), bounded operator event and small labels |
| Empirical exponential budget controls averaged sensitivities | Proved conditional implication | Equations (11)--(12), no carrier maximum |
| Gaussian column Stein identity includes trace, directional, and localization terms | Exact | Equation (15), smooth localization |
| A global bounded Gaussian transport field gives its exponential moment | Proved | Equation (19), all hypotheses stated globally |
| Bounds on an enlarged good domain suffice for a truncated transport moment | Proved conditional implication | Equation (20), fixed-column neighborhoods required |
| The finite carrier budget (5) holds without orthogonality | Open | Neither the conditional sensitivity lemma nor population tails prove it |
| A variable exponential parameter closes the mixed-moment hierarchy | Open | Requires an actual causal inequality, not terminal Hölder doubling |
| Stopped reinsertion is a conditional quadratic form plus a small remainder | Open | Requires adaptive-driver terms, stop independence, and a second-variation bound |
| Strict root-width closure-versus-dense comparison follows | Not established here | Finite tail input is still missing |

The most concrete new reduction is (11)--(12). It removes the maximum from
an averaged finite sensitivity estimate while retaining the full adaptive
flow. The next necessary estimate must control a weighted trace/divergence
at the same exponential parameter, or validate the global transport
hypotheses after localization. No conclusion in this note treats those
requirements as automatic consequences of small labels.

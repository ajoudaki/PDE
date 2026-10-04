# Fixed-depth feedback and two-initialization stability

2026-10-03. Scoped continuation of the dense self-averaging question.
This file proves the deterministic good-set stability lemma requested by
the coordinator and records the exact stronger feedback estimate still
needed for a strict root-width controlled-reference argument. It does not
claim that the latter estimate follows from empirical moments.
No experiments, manuscript edits, other-study reads, or Git operations.

The complete relevant sources read are CONTROLLED_FEEDBACK_STABILITY.md,
AUTONOMOUS_SELF_AVERAGING.md, their complete checks, and
FINITE_TAIL_ROUTE.md, together with the already read current manuscript
and this study's completed fixed-depth physical/carrier arguments.
The first two source hashes are respectively
6a5b99cbaf1b7a905eb5666e77211e6e8ce705246d3146968c4b281a46568abb and
a15921824dad13a27e396f37fdb31bdd7817d0700b0dff260dbe197c70ffe271.
The finite-tail source hash is
da251f231832e69c74581ba4291e649d1322737eebd46b2a4d9c6ca1a8dd0d65.

## 1. Model and physical hypotheses

Fix finite inputs \(v_a=x_a/\sqrt d\), positive weights \(p_a\) with
\(\sum_a p_a=1\), and fixed depth \(L\). The dense network is
\[
 z_a^1=W^1v_a,\qquad z_a^\ell=W^\ell h_a^{\ell-1},\qquad
 h_a^\ell=\phi_\ell(z_a^\ell),\qquad f_a=w^\top h_a^L/n .
\]
Its loss is \(\sum_a p_a(f_a-y_a)^2\), and its block mobilities
are \((n,1,\ldots,1,n)\). Activations have bounded first derivatives
and globally Lipschitz first derivatives. The completed finite carrier
theorem additionally uses \(C^3\) activations with bounded first three
derivatives. Values may have linear growth. Both initial readouts are
zero.

Write
\[
 k_a^L=w,\qquad
 \delta_a^\ell=\phi_\ell'(z_a^\ell)\odot k_a^\ell,\qquad
 k_a^\ell=W^{\ell+1\top}\delta_a^{\ell+1}.
\]
For two actual autonomous trajectories, use an unprimed reference and a
primed comparison. Both have the same labels and fixed physical bounds
\[
 \|W^\ell(t)\|_{\rm op},\|W^{\ell\prime}(t)\|_{\rm op}\le C
 \quad(\ell\ge2),\qquad
 \|W^1(t)\|_F/\sqrt n,\|W^{1\prime}(t)\|_F/\sqrt n\le C,
\]
\[
 \|h_a^\ell(t)\|_2/\sqrt n,\|h_a^{\ell\prime}(t)\|_2/\sqrt n\le C,
 \qquad
 \|k_a^\ell(t)\|_2/\sqrt n,\|k_a^{\ell\prime}(t)\|_2/\sqrt n\le CS.
 \tag{1}
\]
Here \(S>0\) is a fixed small activity scale, comparable to the label
RMS \(Y=(\sum_a p_a y_a^2)^{1/2}\). Assume
\[
 \rho(t)\le Ye^{-\kappa t},\qquad
 \rho'(t)\le Ye^{-\kappa t},\qquad
 \int_0^\infty\rho(t)\,dt\le CS .
 \tag{2}
\]
The weighted training tangent matrix of the primed trajectory has a
fixed gap \(\lambda>0\). This follows from the positive readout-feature
Gram in its physical tube. Only the unprimed trajectory needs the
coordinate carrier envelope
\[
 \sup_{a,\ell,i,t}|k_{a,i}^\ell(t)|\le M.
 \tag{3}
\]
The completed probability theorem provides these hypotheses on a good
initialization set with \(M=C_{\rm car}S\sqrt{\log(e+n)}\).

The case of zero labels is stationary and has identically zero
prediction for every initialization.

## 2. Global pairwise parameter stability on this set

Define the hidden and readout discrepancies by
\[
 D_h(t)=\frac{\|W^{1\prime}-W^1\|_F}{\sqrt n}
             +\sum_{\ell=2}^L\|W^{\ell\prime}-W^\ell\|_F,\qquad
 D_w(t)=\frac{\|w'-w\|_2}{\sqrt n},\qquad D=D_h+D_w.
 \tag{4}
\]
All constants below depend only on the fixed model and physical margins.
They are independent of width and elapsed time.

Forward subtraction using bounded operators and slopes gives, for
training inputs,
\[
 \max_{a,\ell}
 \frac{\|z_a^{\ell\prime}-z_a^\ell\|_2+
       \|h_a^{\ell\prime}-h_a^\ell\|_2}{\sqrt n}
 \le C D_h.
 \tag{5}
\]
For example, a hidden preactivation difference is
\[
 W^{\ell\prime}(h_a^{\ell-1\prime}-h_a^{\ell-1})
       +(W^{\ell\prime}-W^\ell)h_a^{\ell-1}.
\]
Both terms use an operator or RMS norm already bounded in (1).

For backward subtraction use
\[
 \delta_a^{\ell\prime}-\delta_a^\ell
 =\phi_\ell'(z_a^{\ell\prime})\odot
                    (k_a^{\ell\prime}-k_a^\ell)
 +[\phi_\ell'(z_a^{\ell\prime})-\phi_\ell'(z_a^\ell)]
                    \odot k_a^\ell .
 \tag{6}
\]
The carrier in the second term is the unprimed reference, so (3)
applies. Also
\[
 k_a^{\ell\prime}-k_a^\ell
 =W^{\ell+1\prime\top}(\delta_a^{\ell+1\prime}-\delta_a^{\ell+1})
   +(W^{\ell+1\prime}-W^{\ell+1})^\top\delta_a^{\ell+1}.
\]
Descending from \(k^L=w\) and using (5) yields
\[
 \max_{a,\ell}
 \frac{\|\delta_a^{\ell\prime}-\delta_a^\ell\|_2+
       \|k_a^{\ell\prime}-k_a^\ell\|_2}{\sqrt n}
 \le C[D_w+(M+S)D_h].
 \tag{7}
\]
At fixed depth the factors in \(M\) add; they are not multiplied
through the recursion.

Use Euclidean mobility coordinates
\[
 \Theta=(W^1,\sqrt n W^2,\ldots,\sqrt n W^L,w),
 \qquad \mathcal F_a=n f_a,\qquad g_a=\nabla_\Theta\mathcal F_a .
\]
The gradient blocks are
\[
 (g_a)_{W^1}=\delta_a^1v_a^\top,\quad
 (g_a)_{\sqrt n W^\ell}
       =\delta_a^\ell h_a^{\ell-1\top}/\sqrt n,\quad
 (g_a)_w=h_a^L .
\]
Their normalized Euclidean norms satisfy
\[
 \|(g_a)_h\|_2/\sqrt n\le CS,\quad
 \|(g_a)_w\|_2/\sqrt n\le C,
\]
\[
 \|(\Delta g_a)_h\|_2/\sqrt n
       \le C[D_w+(M+S)D_h],\qquad
 \|(\Delta g_a)_w\|_2/\sqrt n\le CD_h .
 \tag{8}
\]
Here the hidden components are concatenated; equivalence with the sum
of block norms costs only a fixed-depth constant.

Let \(r_a=f_a-y_a\) and \(e_a=r_a'-r_a\). Subtracting
\(\dot\Theta=-2\sum_a p_a r_a g_a\), splitting with the primed
gradient on the \(e_a\) term and the unprimed residual on the remaining
term, gives the integral inequality
\[
 D(t)\le D(0)+C\int_0^t\|D_p e(s)\|_2\,ds
             +C(1+M)\int_0^t\rho(s)D(s)\,ds,
 \tag{9}
\]
where \(D_p=\operatorname{diag}(\sqrt{p_a})\).
No interpolation between the two parameter states is used.

Define the raw tangent matrix
\(\Lambda_{ab}=n^{-1}\langle g_a,g_b\rangle\).
The readout part of its difference is bounded by \(CD_h\).
For each hidden part, one factor has norm \(CS\) and its difference
is bounded by (8). Thus
\[
 \|\Lambda'-\Lambda\|_{\rm op}
 \le C[(1+SM)D_h+SD_w]\le C(1+SM)D .
 \tag{10}
\]
The residual equation is exact:
\[
 \frac{d}{dt}(D_p e)
 =-2D_p\Lambda'D_p(D_p e)
       -2D_p(\Lambda'-\Lambda)D_p(D_p r).
 \tag{11}
\]
Because both initial readouts vanish, \(e(0)=0\), even when the
hidden initializations differ. The first matrix in (11) has gap
\(\lambda\), so the nonautonomous propagator is bounded by
\(e^{-2\lambda(t-s)}\). Variation of constants and (10) give
\[
 \|D_p e(t)\|_2
 \le C(1+SM)\int_0^t e^{-2\lambda(t-s)}
                            \rho(s)D(s)\,ds .
\]
Integrating and applying Tonelli,
\[
 \int_0^t\|D_p e(s)\|_2\,ds
 \le C(1+SM)\int_0^t\rho(s)D(s)\,ds .
 \tag{12}
\]
Substitution in (9) and Gronwall against \(\rho(t)dt\) prove
\[
 \boxed{\displaystyle
 \sup_{t\ge0}D(t)\le
       C\exp\{CS(1+M)\}\,D(0).}
 \tag{13}
\]
This is a global pairwise estimate on the stated good set. Arbitrarily
large initial discrepancies do not require a separate bootstrap:
the product subtractions always use physical bounds on their respective
states, not a bound along their joining segment.

## 3. Gaussian-root Lipschitz bound and physical-time modulus

Let \(G\) concatenate the standard Gaussian arrays
\[
 G^1=W_0^1,\qquad G^\ell=\sqrt n W_0^\ell\quad(\ell\ge2).
\]
The initial readouts are zero, so
\[
 D(0)\le C_L\|G-G'\|_2/\sqrt n .
 \tag{14}
\]
For an arbitrary query \(v=x/\sqrt d\), the physical tube and linear
activation growth give
\[
 \|h^\ell(x)\|_2/\sqrt n\le C(1+\|v\|),\qquad
 \|\Delta h^\ell(x)\|_2/\sqrt n
                      \le C(1+\|v\|)D_h .
\]
The prediction product subtraction therefore gives
\[
 \boxed{\displaystyle
 \sup_{t\ge0}|f_G(t,x)-f_{G'}(t,x)|
 \le
 \frac{C(1+\|x\|/\sqrt d)e^{CS(1+M)}}{\sqrt n}
       \|G-G'\|_2 .}
 \tag{15}
\]
Only a reference carrier maximum on training inputs enters (15);
no query carrier maximum is required. The query backward RMS is at most
\(CS\), by bounded slopes and matrix operators.

In fact the normalized parameter gradient at a query has norm at most
\(C(1+\|v\|)\). Hence its tangent pairing with each training gradient
is at most that amount, and
\[
 |\partial_t f_G(t,x)|
 \le C(1+\|v\|)\rho(t)
 \le C(1+\|v\|)Ye^{-\kappa t}.
 \tag{16}
\]
Consequently all good-set predictions have the deterministic modulus
\[
 |f_G(t,x)-f_G(s,x)|
 \le C(1+\|v\|)\frac{Y}{\kappa}
             |e^{-\kappa t}-e^{-\kappa s}|,
 \quad s,t\in[0,\infty],
 \tag{17}
\]
where \(e^{-\kappa\infty}=0\).
The amplitude bound is \(CS(1+\|v\|)\).
The same constants apply throughout the good set.

With \(M=C_{\rm car}S\sqrt{\log(e+n)}\), (15) has Gaussian-root
Lipschitz constant
\[
 \frac{C(1+\|v\|)}{\sqrt n}
       \exp\{C S^2\sqrt{\log(e+n)}\}.
 \tag{18}
\]
This supports a subpolynomial-loss self-averaging argument, not a strict
width-independent root-width constant. Its exponent must not be silently
discarded.

## 4. What the controlled-reference argument still needs

For an external integrated residual \(b\) of total variation at most
\(S\), controlled motion has
\[
 d\Theta=\sum_a g_a(\Theta)\,db_a .
 \tag{19}
\]
Small total variation and initial physical bounds supply the usual
width-independent physical tube: readout RMS \(O(S)\), hidden block
displacement and total variation \(O(S^2)\), bounded feature RMS and
matrix operators. This statement needs no initial Gram gap, since the
control is prescribed rather than fitted.

For completeness, this controlled tube follows by a direct bootstrap.
Bound initial hidden operator norms and first-layer Frobenius RMS by
\(K\). While these quantities stay below \(2K+1\), forward recursion
and linear growth bound every training feature RMS by a fixed \(C_K\).
Readout integration then gives RMS at most \(C_K S\). Backward recursion
gives carrier and response RMS at most \(C_K S\). Every hidden control
vector field consequently has normalized block norm at most \(C_K S\),
so its total displacement and variation are at most \(C_K S^2\).
Taking \(S\) small relative to \(K\) closes the strict bootstrap.
For each finite width, these bounds prevent finite-time escape of the
finite-dimensional controlled ODE on the activity interval. Its locally
Lipschitz vector fields therefore give a unique solution throughout that
interval, independently of its physical-time parametrization.

Writing \(h_x^L(0)\) for the initialized final feature, define
\[
 Q_0(x,a)=n^{-1}h_x^L(0)^\top h_a^L(0).
\]
Readout integration gives the exact decomposition
\[
 f^b(t,x)=\sum_a Q_0(x,a)b_a(t)+R^b(t,x),
 \qquad
 |R^b(t,x)|\le C(1+\|v\|)S^3 .
 \tag{20}
\]
For example, write
\[
 w^b=\sum_a h_a^L(0)b_a+e_w^b,\qquad
 e_w^b=\sum_a\int[h_a^{L,b}(s)-h_a^L(0)]\,db_a(s).
\]
Then \(\|e_w^b\|_2/\sqrt n\le CS^3\), while the query feature
displacement is at most \(C(1+\|v\|)S^2\). Substituting in the
prediction proves (20).

To reproduce the strict feedback transfer, one needs the stronger
two-control estimate
\[
 \boxed{\displaystyle
 \sup_{t\le T}|R^b(t,x)-R^c(t,x)|
 \le C(1+\|v\|)S^2
              \max_a\sup_{t\le T}|b_a(t)-c_a(t)|,}
 \tag{21}
\]
with \(C\) independent of width and physical horizon, for the controls
and initializations actually required by the reference construction.
The separate absolute \(O(S^3)\) estimates in (20) do not imply (21).

For general geometry and depth the controlled variational equation is
\[
 dV=\sum_a D_\Theta^2\mathcal F_a\,V\,db_a
                +\sum_a g_a\,d(\Delta b_a).
 \tag{22}
\]
It does not contain the negative Gram contribution of autonomous
residual feedback, because the residual driver is prescribed.
The Hessian includes
\[
 \sum_\ell Z_{a,\ell}^\top
       \operatorname{diag}(k_a^\ell\phi_\ell''(z_a^\ell))
       Z_{a,\ell},
 \qquad Z_{a,\ell}=D_\Theta z_a^\ell .
 \tag{23}
\]
The proved empirical budget bounds normalized Schatten norms of (23).
It does not bound its operator norm independently of width, nor its
action on an arbitrary \(V\).
Using the trained maximum directly gives an amplification of the form
\(e^{CS(1+M)}\), as in (13), and cannot prove (21) with a fixed
constant. The orthogonal two-tanh-layer argument avoided this term by
an exact coordinate change; that cancellation is absent in general.

No assertion is made here that (21) is false. It is the remaining
structured-response inequality for that particular strict feedback
route. The already proved budget applies to the actual autonomous
path; its validity for every interpolated prescribed-control path is
also not automatic.

## 5. Exact restricted commutator reduction for strict feedback

There is a more precise remaining inequality than an operator bound on
the full controlled propagator. It also proves a genuine special case
beyond the earlier orthogonal two-layer calculation.

Take two absolutely continuous controls \(b,c\) with variation at most
\(S\), a common initialization, and \(e=b-c\). For \(0\le\theta\le1\)
put \(b^\theta=c+\theta e\). Its variation is at most \(S\), so the
preceding controlled tube applies. Let \(\Theta^\theta\) be its state
and \(J^\theta(t,s)\) the variational propagator generated by
\(\sum_c H_c\,db_c^\theta\), where
\[
 g_a=\nabla_\Theta\mathcal F_a,\qquad
 H_a=D_\Theta^2\mathcal F_a .
\]
All quantities in the next formulas are evaluated on
\(\Theta^\theta\). Smooth finite-dimensional dependence on \(\theta\)
and variation of constants give
\[
 V^\theta(t):=\partial_\theta\Theta^\theta(t)
       =\sum_a\int_0^tJ^\theta(t,s)g_a(s)\,de_a(s).
\]
Since \(e(0)=0\), integration by parts is exact:
\[
 V^\theta(t)
 =\sum_a g_a(t)e_a(t)
  -\sum_{a,c}\int_0^t
       J^\theta(t,s)\mathcal B_{ac}(s)e_a(s)\,db_c^\theta(s),
 \qquad
 \mathcal B_{ac}=H_a g_c-H_c g_a.
 \tag{24}
\]
Indeed,
\(d_s[J^\theta(t,s)g_a(s)]
 =\sum_cJ^\theta(t,s)(H_a g_c-H_c g_a)\,db_c^\theta(s)\).
No exchange involving a stochastic expectation is used.

For a query \(x\), define \(\mathcal F_x=nf(x)\) and
\(g_x=\nabla_\Theta\mathcal F_x\). The controlled tangent pairing is
\(\Lambda_{xa}=n^{-1}\langle g_x,g_a\rangle\).
The physical tube alone proves
\[
 |\Lambda_{xa}^\theta(t)-Q_0(x,a)|
       \le C(1+\|v\|)S^2.
 \tag{25}
\]
Its readout part uses feature displacement \(O(S^2)\); its hidden
part pairs gradients of normalized norms \(O(S)\) and
\(O((1+\|v\|)S)\).
Combining (24) with the definition of \(R\) in (20) yields
\[
 \begin{split}
 \partial_\theta R^{b^\theta}(t,x)
 ={}&\sum_a[\Lambda_{xa}^\theta(t)-Q_0(x,a)]e_a(t)\\
 &-\sum_{a,c}\int_0^t
       \mathcal C_{xac}^\theta(t,s)e_a(s)\,db_c^\theta(s),\\
 \mathcal C_{xac}^\theta(t,s)
 ={}&\frac1n
   \left\langle g_x(\Theta^\theta(t)),
       J^\theta(t,s)\mathcal B_{ac}(\Theta^\theta(s))\right\rangle .
 \end{split}
 \tag{26}
\]
It therefore suffices to prove, for the required controls,
\[
 \boxed{\displaystyle
 \sup_{\theta,a,t}
 \sum_c\int_0^t
       |\mathcal C_{xac}^\theta(t,s)|\,|db_c^\theta(s)|
       \le C(1+\|v\|)S^2 .}
 \tag{27}
\]
A stronger sufficient form is
\[
 |\mathcal C_{xac}^\theta(t,s)|
       \le C(1+\|v\|)S
 \quad\text{for all relevant indices and times}.
 \tag{28}
\]
Then (25)–(26), integration in \(\theta\), and the variation bound
prove exactly (21). This is a scalar restricted-response inequality;
it does not require a uniform operator bound for \(J^\theta\).

For a single training sample, \(a=c=1\) and
\(\mathcal B_{11}=0\) identically. Equations (25)–(26) prove (21)
with a width-independent constant at arbitrary fixed depth and with
linearly growing smooth activations. The same conclusion holds when
both controls are restricted to one fixed direction
\(b_a=u_a\beta,\ c_a=u_a\gamma\), since there is then only one
effective vector field and its self-commutator is zero.
This special case does not resolve the full multi-sample question.

For comparison, suppose an additional envelope \(M_*\) holds along
every interpolating controlled trajectory. Splitting parameters into
hidden and readout blocks gives
\[
 (H_a)_{ww}=0,\qquad
 \|(H_a)_{wh}\|+\|(H_a)_{hw}\|\le C,\qquad
 \|(H_a)_{hh}\|\le C(S+M_*).
 \tag{29}
\]
Thus
\[
 \|(\mathcal B_{ac})_h\|_2/\sqrt n\le C(1+SM_*),\qquad
 \|(\mathcal B_{ac})_w\|_2/\sqrt n\le CS .
 \tag{30}
\]
Blockwise Gronwall over remaining activity at most \(S\) propagates
(30) with a factor bounded by \(C e^{CS(1+M_*)}\).
The propagated readout block remains at most
\(CS(1+SM_*)e^{CS(1+M_*)}\) in RMS, because its equation is
driven only by the hidden block. Pairing with \(g_x\), whose hidden
RMS is \(O((1+\|v\|)S)\), yields the valid but weaker bound
\[
 |\mathcal C_{xac}^\theta(t,s)|
 \le C(1+\|v\|)S(1+SM_*)e^{CS(1+M_*)}.
 \tag{31}
\]
It retains precisely the width-dependent amplification that strict
feedback must remove.

The joint empirical exponential budget does not by itself repair
(31). A diagonal with one entry \(c\log n\) and all others zero has
a bounded normalized exponential average for sufficiently small fixed
exponential parameter, but its operator norm diverges. Nor does a
normalized Hilbert--Schmidt bound control its pairing with an arbitrary
rank-one endpoint: vectors concentrated on that coordinate see the
largest entry. In (26) the endpoints are structured network gradients,
so a cancellation or a further delocalization estimate could still prove
(27). None has been established here. The earlier Schatten trace
argument has different endpoint structure and cannot be substituted.

The bounded attempt therefore ends with: the global good-set stability
lemma (13)–(18) is proved; strict feedback (21) is proved for one
effective control direction; for general data its exact remaining
estimate is (27), together with a justified controlled-path domain for
that estimate. No strict all-depth self-averaging theorem is claimed by
this route.

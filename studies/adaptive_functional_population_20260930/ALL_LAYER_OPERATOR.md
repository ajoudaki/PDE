# All-layer operator route: a streaming forward theorem and the backward obstruction

Status: independent scoped derivation, 2026-09-30. Inputs were the supervisor's assignment and required mathematical/research skills only. No other study artifact, book passage, external scientific source, or experiment was used. This is an internally checked route report, not promoted theory.

## Conclusion

Nuclear variation does yield an explicit deterministic streaming representation of every learned hidden matrix, with $O(nr)$ learned numbers per layer and operator error $O(V/r)$, where $V$ is a width-independent nuclear-variation bound. This is stronger than a best-rank existence statement: a signed version of the covariance shrinkage algorithm below consumes rank-one updates and never stores their dependency graphs.

Combining this algorithm with the given energy inequality proves a driven, width-uniform encoding of **all forward histories**, uniformly over inputs and current times on a fixed horizon. The retained dense initial matrices remain unchanged. First-layer snapshots cost $nd$ numbers each, readout snapshots cost $n$, and hidden learned snapshots cost $O(Lnr)$; the number of snapshots and rank do not depend on width or data count.

This argument does **not** prove the requested all-layer backward-history theorem. There is an explicit Gaussian-core example in which an $O(n^{-1/2})$ operator perturbation changes a normalized backward vector by order one, despite bounded hidden operator norms, bounded readout coordinates, bounded learned nuclear norm, and the stronger $O(n^{-1/2})$ learned-column bound. Thus the missing backward estimate cannot be inferred from these norm bounds. The example is a snapshot counterexample, not a gradient-flow reachable-state counterexample, and does not disprove the original conjecture.

The precise missing bridge is uniform integrability of the exact backward carriers across neuron coordinates, along the canonical flow. A quantitative version of that bridge is given below. No such estimate is assumed in the unconditional forward theorem.

## 1. Contract and elementary bounds

All hidden layers have width $n$; $L,T,d,R$ are fixed. Write

\[
 |v|_n=\|v\|_2/\sqrt n,
 \qquad M_j=\|\phi^{(j)}\|_\infty,
 \qquad B=\|\phi\|_\infty.
\]

The assigned network, residual $r=f-y$, and gradient flow are unchanged. The data law $P$ may be an empirical law with any number $m$ of observations. Only $\|x\|/\sqrt d\le R$ and finite initial square loss $\mathcal L_0$ are used. Assume the canonical flow exists on $[0,T]$. The approximation is an **encoder driven by that exact flow**, not an autonomous training system. It receives current first-layer/readout states, the scalar residual norm, and rank-one hidden update atoms. Its cost accounting includes this dependence.

For simplicity take $w(0)=0$. All bounds extend with the indicated initial readout norm added. The loss identity is

\[
 -\dot{\mathcal L}
 =\frac{\|\dot W_1\|_F^2}{n}
  +\sum_{\ell=2}^L\|\dot W_\ell\|_F^2
  +\frac{\|\dot w\|_2^2}{n}.
\]

It follows directly by differentiating the loss and substituting the assigned flow; the factors $n$ for the first layer and readout exactly cancel their $1/n$ loss gradients. In particular, with $\rho=\|r\|_{L^2(P)}$,

\[
 \rho(t)\le\sqrt{\mathcal L_0},\qquad
 Q:=\int_0^T\rho\,dt\le T\sqrt{\mathcal L_0},\qquad
 \tau(t)=1+\int_0^t\rho\,ds\le 1+Q.
\]

Let

\[
 A_0=\max_{2\le\ell\le L}\|W_\ell(0)\|_{\rm op},\quad
 A=A_0+\sqrt{T\mathcal L_0},\quad
 W=\sqrt{T\mathcal L_0}.
\]

Energy and Cauchy--Schwarz give, uniformly in $t,x$,

\[
 \|W_\ell(t)\|_{\rm op}\le A,\qquad
 |w(t)|_n\le W,\qquad |h_\ell(t,x)|_n\le B,
\]

and the backward recursion gives the valid, width-independent **second-moment** bound

\[
 |\delta_\ell(t,x)|_n\le D_\ell,
 \qquad D_\ell=W M_1^{L-\ell+1}A^{L-\ell}.
 \tag{1}
\]

This bound does not control coordinate tails. Separately, the readout equation does give

\[
 \|w(t)\|_\infty\le 2B Q.
 \tag{2}
\]

For every hidden matrix, the exact rank-one update formula implies

\[
 \begin{split}
 V_\ell&:=\int_0^T\|\dot W_\ell(s)\|_*\,ds\\
 &\le 2\int_0^T\mathbb E\bigl[
 |r|\,|\delta_\ell|_n\,|h_{\ell-1}|_n\bigr]ds
 \le 2 B D_\ell Q.
 \end{split}
 \tag{3}
\]

For the streaming construction use the possibly larger atom mass

\[
 \widetilde V_\ell(t)
 =2\int_0^t\mathbb E\bigl[
 |r|\,|\delta_\ell|_n\,|h_{\ell-1}|_n\bigr]ds
 \le 2BD_\ell Q.
 \tag{4}
\]

The distinction matters: cancellation can make the nuclear variation in (3) smaller than the update-stream mass available to an algorithm. The same exact formula gives the stronger column estimate

\[
 \|(W_\ell(t)-W_\ell(0))e_j\|_2
 \le \frac{2BD_\ell Q}{\sqrt n}.
 \tag{5}
\]

No Gaussian claim is needed for the deterministic theorem: it holds on every initialization with the stated $A_0$. For Gaussian hidden matrices, a direct net argument makes $A_0$ bounded with width-uniform probability. Indeed a $1/4$-net of the unit sphere has at most $9^n$ points; approximating both arguments of a bilinear form gives

\[
 \Pr(\|G\|_{\rm op}>2s)
 \le 2\,9^{2n}\exp(-ns^2/2)
\]

for entries $N(0,1/n)$. A union bound over the fixed $L-1$ hidden matrices supplies a constant depending only on $L$ and the desired failure probability. This follows from the scalar Gaussian moment-generating function and the covering bound; no independent limit theorem is being invoked. The first-layer Gaussian operator norm is unnecessary because the first-layer snapshots are retained exactly.

## 2. Deterministic signed streaming sketch

Here is an explicit algebraic statement for a finite stream. In this section the integer rank budget is denoted $r$; the residual $r(t,x)$ retains its separate function-valued meaning in the canonical update formulas. Suppose

\[
 M=\sum_{j=1}^N c_j a_jb_j^T,
 \qquad c_j\ge0,\quad \|a_j\|_2=\|b_j\|_2=1,
 \quad V=\sum_jc_j.
\]

Signs are included in $a_j$. Set $v_j=(a_j,b_j)/\sqrt2\in\mathbb R^{2n}$ and

\[
 C=\sum_j c_jv_jv_j^T.
\]

Then $\operatorname{tr}C=V$, and the upper-right block of $C$ is $M/2$.

Maintain a matrix $S\in\mathbb R^{r\times2n}$, initially zero. Insert the row $\sqrt{c_j}v_j^T$ into an empty row. When this creates $r+1$ nonzero rows, form the thin singular-value decomposition of this $(r+1)\times2n$ matrix. Write its squared singular values as $\lambda_1\ge\cdots\ge\lambda_{r+1}$. Subtract $\lambda_{r+1}$ from all of them, discard the resulting zero direction, and use the remaining square-root singular values and right singular vectors as the new $r$ rows. If the inserted matrix has rank at most $r$, simply keep an exact $r$-row factor.

At a shrinkage step, the covariance removed is positive semidefinite, is bounded above by $\lambda_{r+1}I$, and has trace $(r+1)\lambda_{r+1}$. Summing over steps therefore gives

\[
 0\preceq C-S^TS\preceq
 \Bigl(\sum_{\rm shrink}\lambda_{r+1}\Bigr)I,
 \qquad
 (r+1)\sum_{\rm shrink}\lambda_{r+1}\le\operatorname{tr}C=V.
\]

Partition $S=(S_a,S_b)$ into two $r\times n$ blocks and decode

\[
 \widehat M=2S_a^TS_b.
\]

The norm of an off-diagonal block does not exceed the norm of the full error matrix, so

\[
 \boxed{\|M-\widehat M\|_{\rm op}\le\frac{2V}{r+1}.}
 \tag{6}
\]

This proves the needed streaming bound rather than appealing to best-rank approximation. There are $2rn$ stored numbers, and a new atom requires $O(nr^2+r^3)$ arithmetic by a thin Gram-matrix implementation. Applying the learned correction or its transpose to a vector costs $O(nr)$. Rank-one atoms have no retained reference to the source network, data sample, or earlier snapshot once their two vectors have been inserted.

For the canonical update, use

\[
 a=-\operatorname{sgn}(r)\frac{\delta_\ell}{\|\delta_\ell\|_2},\quad
 b=\frac{h_{\ell-1}}{\|h_{\ell-1}\|_2},\quad
 dc=2|r|\,|\delta_\ell|_n|h_{\ell-1}|_n\,dt\,dP.
\]

Zero-mass atoms are omitted. Equation (4) bounds the total mass. Thus choose

\[
 r+1\ge\frac{2\max_\ell\widetilde V_\ell(T)}{\eta}
\]

to obtain hidden learned-operator error at most $\eta$.

**Numerical/provenance qualification.** The finite-stream statement (6) is an executable algorithm and is exact. Continuous gradient flow supplies a measure-valued stream, not a finite list of machine operations. A finite quadrature or exact-update driver with operator error at most $\zeta$ gives total error at most $\zeta+2V/(r+1)$. For each fixed finite network, integrability of the atoms permits finite simple-function approximations; refining these makes $\zeta\to0$. The constants for the *compression* error are width-uniform. This report does not prove a width-uniform cost for producing the driving quadrature, nor hide that cost inside the sketch. Applying the sketch to an empirical time-stepped full-gradient stream processes $m$ atoms per layer per step, so its construction runtime depends on $m$, while its stored state does not. A population expectation requires its own integration/sampling oracle.

## 3. Width-uniform driven forward-history theorem

Let

\[
 e(t)^2=\frac{\|\dot W_1\|_F^2}{n}
 +\sum_{\ell=2}^L\|\dot W_\ell\|_F^2
 +\frac{\|\dot w\|_2^2}{n}.
\]

The energy inequality is $\int_0^T e^2\le\mathcal L_0$. Differentiating the forward recursion gives

\[
 |\dot h_1|_n\le M_1R e,
 \qquad
 |\dot h_\ell|_n\le M_1B e+M_1A|\dot h_{\ell-1}|_n.
\]

Define $C_1=M_1R$, $C_\ell=M_1B+M_1AC_{\ell-1}$. Consequently, uniformly over admissible inputs,

\[
 |h_\ell(t,x)-h_\ell(s,x)|_n
 \le C_\ell\sqrt{|t-s|\mathcal L_0}.
 \tag{7}
\]

Partition physical time with mesh at most $\Delta$, using $N\le 1+\lceil T/\Delta\rceil$ left-endpoint snapshots $t_i$. At each snapshot save the exact $W_1(t_i)$, optionally the exact $w(t_i)$, the current hidden sketch factors, and the scalar $u_i=\tau(t_i)$. The dense initialized matrices are shared once by all snapshots. A snapshot is decoded by an ordinary forward pass through its own first layer and $W_\ell(0)+\widehat{\Delta W_\ell}(t_i)$.

Suppose each decoded hidden matrix has operator error at most $\epsilon=\eta+\zeta$. Let $F_1=0$ and $F_\ell=M_1B+M_1AF_{\ell-1}$. The decomposition

\[
 \widehat W_\ell\widehat h_{\ell-1}-W_\ell h_{\ell-1}
 =W_\ell(\widehat h_{\ell-1}-h_{\ell-1})
 +(\widehat W_\ell-W_\ell)\widehat h_{\ell-1}
\]

and bounded activations give

\[
 |\widehat h_\ell(t_i,x)-h_\ell(t_i,x)|_n\le F_\ell\epsilon.
 \tag{8}
\]

No carrier estimate appears here.

Let $p_k$ be any fixed finite family of polynomials on $[0,1]$, with $P_k=\sup|p_k|$. Extend the forward path by its initial value on the prefix $u\in[0,1]$. On the remaining pseudo-time interval decode the left physical-time snapshot. At current time $t$, form

\[
 \widehat H_{\ell,k}(t,x)
 =h_\ell(0,x)\int_0^1p_k(u/\tau(t))\,du
 +\sum_{i:t_i<t}\widehat h_\ell(t_i,x)
   \int_{u_i}^{u_{i+1}\wedge\tau(t)}p_k(u/\tau(t))\,du,
 \tag{9}
\]

where the final open interval ends at the current exact scalar $\tau(t)$. The integrals of $p_k$ are finite scalar computations, so (9) does not store a residual-norm trajectory. If $\rho=0$ on an interval its pseudo-time length is zero and it contributes nothing.

Equations (7)--(8), integrated against $|p_k|$, prove

\[
 \boxed{
 \sup_{0\le t\le T}\sup_x
 |\widehat H_{\ell,k}(t,x)-H_{\ell,k}(t,x)|_n
 \le(1+Q)P_k\left(C_\ell\sqrt{\Delta\mathcal L_0}
 +F_\ell\epsilon\right).
 }
 \tag{10}
\]

This is a real uniform encoding bound at fixed depth and horizon. It also implies the corresponding $L^2(P;\ell^2_n)$ bound for every data law, independently of $m$. Given a requested accuracy, choose $\Delta$, $r$, and driving accuracy $\zeta$ from (10); $N,r$ depend on the displayed regularity/horizon/loss constants, not on $n,m$.

**State and runtime.** Saving readout as well costs at most

\[
 N\bigl(nd+n+2(L-1)rn+O(1)\bigr)
\]

learned real numbers, plus one shared immutable copy of the original initialized matrices. The current live sketch uses another $2(L-1)rn$ numbers. The first layer is retained explicitly, so dependence on $d$ is stated, not hidden. Any independently proved first-layer encoder can replace that component after adding its forward error.

For a new input, one snapshot costs $O(nd+(L-1)n^2+(L-1)nr)$, because multiplying by the retained generic dense Gaussian matrices still costs $O(n^2)$. Evaluating $K$ history indices from all snapshots adds $O(KLNn)$ accumulation work. Neither query requires the training dataset or the past update graphs. This is a saving in **learned state**, not a subquadratic dense-core evaluation theorem. The driver still runs the full canonical model; neither autonomous training nor restartability of the canonical dynamics follows.

## 4. Why operator accuracy does not settle backward history

Define the exact carrier $q_L=w$ and $q_\ell=W_{\ell+1}^T\delta_{\ell+1}$ for $\ell<L$. Comparing two snapshots gives the gate term

\[
 \bigl(\phi'(z_\ell)-\phi'(\widehat z_\ell)\bigr)\odot q_\ell.
 \tag{11}
\]

An $L^2$ bound on each factor does not bound their product in $L^2$, uniformly in $n$. The following example shows an actual discontinuity in the relevant normalized topology.

Take tanh, depth three, a fixed $c\in(0,1)$, and a snapshot with $h_1=c\mathbf 1$. It can be realized with $d=1,x=1,W_1=\operatorname{arctanh}(c)\mathbf1$. Let $G_2,G_3$ be the exact Gaussian initialized hidden matrices, with variance $1/n$, and set

\[
 P=\frac{h_1h_1^T}{\|h_1\|_2^2},\qquad
 W_2=G_2(I-P),\qquad W_3=G_3.
\]

Write $g=G_3e_1$, choose $w_i=\operatorname{sgn}(g_i)$, and fix $a\ne0$. Compare this snapshot with the one having

\[
 \widehat W_2=W_2+\frac{a e_1h_1^T}{\|h_1\|_2^2}
\]

and all other states unchanged. Then

\[
 \|\widehat W_2-W_2\|_{\rm op}
 =\|\widehat W_2-W_2\|_*
 =\frac{|a|}{c\sqrt n}\longrightarrow0.
 \tag{12}
\]

Both learned offsets from the *same retained* $G_2$ have bounded nuclear norm, since $G_2P$ has rank one and nuclear norm at most $\|G_2\|_{\rm op}$. Their column norms are $O(n^{-1/2})$. All hidden operator norms are bounded on the Gaussian bounded-operator event, and $|w|_\infty=|w|_n=1$.

For the first snapshot, $z_2=h_2=z_3=h_3=0$, and

\[
 \delta_2=G_3^Tw,\qquad
 (\delta_2)_1=\sum_i|g_i|.
\]

For the perturbed snapshot,

\[
 \widehat z_2=ae_1,\quad
 \widehat h_2=(\tanh a)e_1,\quad
 \widehat z_3=(\tanh a)g,
\]

and hence

\[
 (\widehat\delta_2)_1
 =\operatorname{sech}^2(a)
   \sum_i|g_i|\operatorname{sech}^2((\tanh a)g_i).
\]

Writing $g_i=Z_i/\sqrt n$, the law of large numbers gives

\[
 \frac1{\sqrt n}\sum_i|g_i|
 =\frac1n\sum_i|Z_i|\ \longrightarrow\sqrt{2/\pi}.
\]

Moreover $0\le1-\operatorname{sech}^2(v)=\tanh^2(v)\le v^2$, so

\[
 \frac1{\sqrt n}\sum_i|g_i|
 \bigl[1-\operatorname{sech}^2((\tanh a)g_i)\bigr]
 \le\frac{\tanh^2(a)}{n^2}\sum_i|Z_i|^3\longrightarrow0.
\]

Therefore

\[
 \liminf_{n\to\infty}|\widehat\delta_2-\delta_2|_n
 \ge\sqrt{2/\pi}\,\tanh^2(a)>0.
 \tag{13}
\]

Even an arbitrarily small rank-one tail can therefore matter to backward evaluation. This defeats a universal backward modulus inferred from operator/nuclear/column bounds alone. It does not show that every sensitivity-aware sketch must fail; this particular tail is itself rank one and could be retained by a suitable sketch.

**Reachability boundary.** The example deliberately chooses a readout correlated with one Gaussian column. It is not established that the prescribed zero-readout canonical gradient flow reaches these snapshots. The states lie in bounded metric-distance and nuclear/column balls around initialization, but bounded energy is only a necessary condition for gradient-flow reachability. No claim about actual $B$-history failure is inferred by holding these artificial states fixed over time. An integrated-history theorem may exploit canonical dynamics in a way that instantaneous arbitrary-snapshot stability cannot.

## 5. A precise sufficient bridge, left unproved for the flow

For each exact carrier, define the normalized coordinate-tail energy

\[
 \omega(K)=\sup_{n,\ell,t\le T,x}
 \left(\frac1n\sum_{j=1}^n
 |q_{\ell,j}(t,x)|^2\mathbf1_{\{|q_{\ell,j}(t,x)|>K\}}
 \right)^{1/2}.
\]

If one could prove $\omega(K)\to0$ for the canonical class, then splitting (11) at $|q|=K$ would give

\[
 |(\phi'(z)-\phi'(\widehat z))\odot q|_n
 \le M_2K|z-\widehat z|_n+2M_1\omega(K).
 \tag{14}
\]

Together with ordinary operator-error propagation in the backward recursion, this yields a width-uniform backward modulus by first choosing $K$, then the snapshot accuracy. A sufficient quantitative condition is

\[
 \sup_{n,\ell,t,x}|q_\ell(t,x)|_{p,n}\le Q_p
 \quad\text{for some }p>2,
\]

where $|v|_{p,n}=(n^{-1}\sum|v_j|^p)^{1/p}$. Hölder and interpolation then give

\[
 |(\phi'(z)-\phi'(\widehat z))\odot q|_n
 \le Q_p(2M_1)^{2/p}
       (M_2|z-\widehat z|_n)^{1-2/p}.
 \tag{15}
\]

The exact carrier is used in (14)--(15); no tail assumption on the approximate carrier is necessary. Indeed

\[
 \delta_\ell-\widehat\delta_\ell
 =\widehat J_\ell\bigl[
 W_{\ell+1}^T(\delta_{\ell+1}-\widehat\delta_{\ell+1})
 +(W_{\ell+1}-\widehat W_{\ell+1})^T\widehat\delta_{\ell+1}
 \bigr]
 +(J_\ell-\widehat J_\ell)q_\ell,
\]

Here $J_\ell=\operatorname{diag}(\phi^\prime(z_\ell))$ and $\widehat J_\ell=\operatorname{diag}(\phi^\prime(\widehat z_\ell))$. Approximate backward second moments follow from its bounded operators and the retained readout. At the top layer (2) supplies the tail bound. The unresolved issue is its propagation through retained Gaussian matrices that have become correlated with learned gates and readout. Treating these matrices as independent of their trained arguments would be invalid.

Under this additional bridge, the same snapshots would also approximate backward histories. The change of clock removes division by small residual norm:

\[
 B_{\ell,k}(t,x)
 =\int_0^t p_k(\tau(s)/\tau(t))\,r(s,x)\delta_\ell(s,x)\,ds,
 \tag{16}
\]

with zero initial-prefix contribution when $w(0)=0$. Thus one should integrate (16) by quadrature in physical time, rather than divide approximate residuals by $\rho$. Under the $p>2$ bound, forward energy regularity and (15) give backward temporal modulus $O(|t-s|^{(1-2/p)/2})$; the output has an $O(|t-s|^{1/2})$ uniform modulus by differentiating $\langle w,h_L\rangle_n$. For polynomial $p_k$, left quadrature of (16) consequently has error $O(\Delta^{(1-2/p)/2})$ in $L^2(P;\ell^2_n)$, while compressed snapshot error is $O(\epsilon^{1-2/p})$. The residual only needs its given $L^2(P)$ bound because the vector errors in this proposed sufficient criterion are uniform in $x$.

These are conditional implications that identify the missing theorem. They are not claims that the required carrier tail estimate follows from the supplied assumptions.

## 6. Claim ledger and next bottleneck

| Claim | Status | Scope |
|---|---|---|
| Hidden update atom mass is width-independent | Proved | Exact canonical flow, conditional on the bounded initialization operator event |
| Rank-$r$ deterministic streaming hidden sketch has error $2V/(r+1)$ | Proved | Finite atom stream; continuous driver accuracy explicitly separated |
| All forward histories admit $O(NLnr+Nnd)$ learned state | Proved driven bound | Uniform input/current-time error (10); unchanged dense initial cores |
| The same operator accuracy automatically controls backward vectors | False | Gaussian-core snapshot example (12)--(13) |
| Canonical-flow backward histories cannot be compressed | Not established | Snapshot obstruction is not a reachability or integrated-history no-go |
| Uniform carrier coordinate-tail control closes this sketch route | Proved sufficient bridge | Equations (14)--(16) |
| Such tail control holds for the canonical trained Gaussian system | Open here | Training dependence cannot be ignored |
| Encoder is an autonomous, restartable population model | Not claimed | Exact flow/update driver remains necessary |

The highest-leverage next proof obligation is therefore a reachable-state carrier-tail theorem, or an integrated-in-time replacement strong enough for (16). Refining the operator sketch alone cannot establish that bridge.

# Fixed-offset arctangent: explicit response bootstrap

Status: candidate proof, not independently audited. This is a finite-program
population response lemma, not by itself the full MF/GF/GD theorem.
It concerns the newly authorized activation, not canonical arctangent.

The explicit source representation used below is the one derived in
L3_LOCAL_COMPLETE_PROOF.md, SHA256
f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4,
sections “Fixed-mesh Gaussian conditioning and source identification”
and “Coefficientwise local response bootstrap”. Its coordinate maps are
changed as displayed here. In particular, covariances are uncentered
second moments of the queries, not covariances of centered activations.
The transfer of that representation and the passage to flows are separate
obligations. Everything after the displayed source system is proved here.

## Statement and exact scalar system

Fix, in all three hidden layers,
\[
 \phi(z)=1+\tfrac1{10}\arctan z,\qquad
 F(z)=10(z+z^3/3),\qquad \chi=\phi\circ F^{-1}.
\]
Put \(a=7/6\). The elementary bounds used throughout are
\[
 5/6<\phi<a,\quad 0<\phi'\le1/10,\quad
 |\phi''|\le1/5,\quad |\chi'|\le1/100.
\]
Let \(S=M\Delta\le3/2\), with \(\Delta>0\). For an auxiliary smooth
clipping map assume \(|\tau_R(u)|\le |u|\) and
\(|\tau_R'(u)|\le1\). Consider the following causal finite scalar
program with zero initial population readout:
\[
 X^{(1)}_k=F(Z^{(1)}_0)+\Delta\sum_{r<k}q^{(1)}_r,
 \qquad H^{(1)}_k=\chi(X^{(1)}_k),
\]
\[
 Z^{(\ell)}_k=\xi^{(\ell)}_k+
       \sum_{r<k}a^{(\ell)}_{kr}\delta^{(\ell)}_r,
 \qquad H^{(\ell)}_k=\phi(Z^{(\ell)}_k),\quad \ell=2,3,
\]
\[
 W^{(4)}_k=\Delta\sum_{r<k}H^{(3)}_r,
 \qquad\delta^{(3)}_k=W^{(4)}_k\phi'(Z^{(3)}_k),
\]
\[
 q^{(2)}_k=\zeta^{(2)}_k+
            \sum_{v\le k}b^{(3)}_{kv}H^{(2)}_v,
 \qquad\delta^{(2)}_k=\phi'(Z^{(2)}_k)\tau_R(q^{(2)}_k),
\]
\[
 q^{(1)}_k=\zeta^{(1)}_k+
            \sum_{v\le k}b^{(2)}_{kv}H^{(1)}_v.
\]
For \(\ell=2,3\), the deterministic coefficients are
\[
 a^{(\ell)}_{ks}=
 \mathbb E\frac{\partial H^{(\ell-1)}_k}
                    {\partial\zeta^{(\ell-1)}_s}
       +\Delta\mathbb E[H^{(\ell-1)}_kH^{(\ell-1)}_s],\quad s<k,
\]
\[
 b^{(\ell)}_{ks}=
 \mathbb E\frac{\partial\delta^{(\ell)}_k}{\partial\xi^{(\ell)}_s}
       +\Delta\mathbf1_{s<k}
                    \mathbb E[\delta^{(\ell)}_k\delta^{(\ell)}_s],
 \quad s\le k.
\]
The four centered Gaussian source groups are independent of one another
and of \(Z^{(1)}_0\sim N(0,1)\). Within each group they may be arbitrarily
correlated, including singularly. Their second moments are
\[
 \mathbb E[\xi^{(\ell)}_k\xi^{(\ell)}_s]
     =\mathbb E[H^{(\ell-1)}_kH^{(\ell-1)}_s],\qquad
 \mathbb E[\zeta^{(\ell-1)}_k\zeta^{(\ell-1)}_s]
     =\mathbb E[\delta^{(\ell)}_k\delta^{(\ell)}_s].
\]
All source derivatives mean derivatives of these explicit coordinate
expressions with the deterministic coefficients fixed. No covariance
factorization is differentiated. All same-time terms \(b_{kk}\), in
particular the return through \(b^{(3)}_{kk}\) when differentiating
\(\delta^{(2)}_k\), are retained.

We prove, uniformly in \(R,M,\Delta\), that
\[
 U_k:=\sum_{s\le k}|b^{(2)}_{ks}|<9/10,\qquad
 V_k:=\sum_{s\le k}|b^{(3)}_{ks}|\le3067/3200<1,
 \qquad k\le M.
\]
Consequently
\[
 \mathbb P\{|q^{(2)}_k|>7/6+x\}
 \le2\exp\{-x^2/[2(7/40)^2]\},\qquad x>0.                 \tag{1}
\]

## Causal induction and bottom response

At time zero the readout and both backward fields vanish, so
\(U_0=V_0=0\). Suppose all rows strictly before \(k\) obey \(U_r,V_r\le1\).
Set \(A=3/2\), a coefficient bound distinct from \(a=7/6\).
The bottom recursion, differentiated at one \(\zeta^{(1)}_s\), gives
\[
 \left|\frac{\partial X^{(1)}_j}{\partial\zeta^{(1)}_s}\right|
 \le\Delta\mathbf1_{s<j}+
 \frac{\Delta}{100}\sum_{r<j}\sum_{v\le r}|b^{(2)}_{rv}|
       \left|\frac{\partial X^{(1)}_v}{\partial\zeta^{(1)}_s}\right|.
\]
Discrete Gronwall and \(|\chi'|\le1/100\) imply
\[
 \left|\frac{\partial H^{(1)}_j}{\partial\zeta^{(1)}_s}\right|
 \le\frac{\Delta}{100}\exp(S/100),\qquad s<j\le k.
\]
Since \(\exp(3/200)<2\) and \(49/36+1/50<3/2\),
\[
 |a^{(2)}_{js}|\le\Delta[a^2+\exp(S/100)/100]<A\Delta.     \tag{2}
\]

## Middle response and integrable exponential envelope

Let
\[
 \mathcal R_j=\sum_{s\le j}
  \left|\frac{\partial Z^{(2)}_j}{\partial\xi^{(2)}_s}\right|,
 \qquad
 E_j=\exp\left\{A\Delta\sum_{r<j}
             \left(\frac{|q^{(2)}_r|}{5}+\frac{V_r}{100}\right)\right\}.
\]
For every source derivative,
\[
 |\partial\delta^{(2)}_r|
 \le\tfrac15|q^{(2)}_r|\,|\partial Z^{(2)}_r|
       +\tfrac1{10}|\partial q^{(2)}_r|.
\]
For a \(\xi^{(2)}\) source,
\[
 |\partial q^{(2)}_r|
 \le\tfrac1{10}\sum_{v\le r}|b^{(3)}_{rv}|
                           |\partial Z^{(2)}_v|.
\]
Using (2), summing over source indices, and applying discrete Gronwall
therefore gives \(\max_{v\le j}\mathcal R_v\le E_j\) for \(j\le k\).
For one \(\zeta^{(2)}_s\) source there is the additional direct derivative
\(\mathbf1_{r=s}\) in \(q^{(2)}_r\). Its first contribution to
\(Z^{(2)}_j\) has magnitude at most \(A\Delta/10\). The same Gronwall
argument gives
\[
 \left|\frac{\partial Z^{(2)}_j}{\partial\zeta^{(2)}_s}\right|
 \le\tfrac{A\Delta}{10}E_j,
 \qquad
 \left|\frac{\partial H^{(2)}_j}{\partial\zeta^{(2)}_s}\right|
 \le\tfrac{A\Delta}{100}E_j,\quad s<j\le k.              \tag{3}
\]
The current \(\zeta^{(2)}_j\) does not enter \(Z^{(2)}_j\).

The pointwise readout bound is \(|W^{(4)}_r|\le aS\), hence
\[
 |\delta^{(3)}_r|\le aS/10,\quad
 \operatorname{Var}(\zeta^{(2)}_r)\le(aS/10)^2\le(7/40)^2,
 \qquad |q^{(2)}_r|\le|\zeta^{(2)}_r|+aV_r.
\]
For \(p\ge1\), Jensen over the finitely many past times and the bound
\(\mathbb E\exp(\lambda|G|)\le2\exp(\lambda^2\operatorname{Var}(G)/2)\)
for a centered Gaussian give
\[
 \mathbb E E_j^p
 \le2\exp\left\{pAS\left(\frac a5+\frac1{100}\right)
              +\frac12\left(\frac{pAS}{5}\right)^2
                              \left(\frac{aS}{10}\right)^2\right\}
 \le2\exp\left\{\frac{219p}{400}+
                         \frac{3969p^2}{1280000}\right\}.       \tag{4}
\]
At \(j=0\), use \(E_0=1\) directly. For \(j>0\), the Jensen step is
\[
 \exp\left\{\frac{pA\Delta}{5}\sum_{r<j}|\zeta^{(2)}_r|\right\}
 \le\frac1j\sum_{r<j}
                  \exp\{pAj\Delta|\zeta^{(2)}_r|/5\}.
\]
No independence across times, or between the source and its bounded
response shift, is asserted or needed. For \(p=1,2\) the exponent in
(4), after taking the \(p\)-th root, is less than \(3/5\).
Since \(\exp(3/5)<2\), we obtain
\[
 \|E_j\|_1<4,\qquad \|E_j\|_2<3.                         \tag{5}
\]
For completeness, \(\exp(3/5)<2\) follows from \(e<3\) and
\(3^3<2^5\). Equations (3)--(5) yield
\[
 |a^{(3)}_{js}|\le\Delta(a^2+4A/100)
       =\Delta(49/36+3/50)<A\Delta.                      \tag{6}
\]

## Top response and the current middle query

Write \(T_j=\sum_{s\le j}|\partial Z^{(3)}_j/\partial\xi^{(3)}_s|\).
Differentiating the readout integral and the top gate gives
\[
 \sum_{s\le j}\left|
       \frac{\partial\delta^{(3)}_j}{\partial\xi^{(3)}_s}\right|
 \le\frac{\Delta}{100}\sum_{r<j}T_r+\frac{aS}{5}T_j
 \le\frac{73}{300}S\max_{v\le j}T_v.
\]
Using (6) in the strictly causal top recursion and Gronwall gives
\[
 \max_{v\le j}T_v\le\exp\{A(73/300)S^2\}
 \le\exp(657/800)<5/2.
\]
Indeed \(657/800<5/6\), and \(e^{5/6}<3^{5/6}<5/2\), since
\(3^5 2^6=15552<15625=5^6\). Adding the learned-rank term to the
expected derivative row proves
\[
 V_k\le\frac{73}{300}S\frac52+
              \frac{a^2 S^3}{100}
 \le\frac{73}{80}+\frac{147}{3200}
 =\frac{3067}{3200}<1.                                   \tag{7}
\]
Only rows before \(k\) have been assumed bounded. In particular (7)
is available before estimating the current \(q^{(2)}_k\). The Gaussian
variance and bounded shift then give
\[
 \|q^{(2)}_k\|_2\le aS/10+aV_k\le 7/40+7/6=161/120=:Q,
 \qquad \|\delta^{(2)}_k\|_2\le Q/10.                    \tag{8}
\]
The same bound holds for every earlier row, by the same induction.

## Closing the bottom response without a current-row assumption

Summing the current \(\xi^{(2)}\) source derivatives, including the
same-time \(b^{(3)}_{kk}\) return, gives
\[
 \sum_{s\le k}\left|
       \frac{\partial\delta^{(2)}_k}{\partial\xi^{(2)}_s}\right|
 \le\left(\frac{|q^{(2)}_k|}{5}+\frac{V_k}{100}\right)E_k.
\]
Cauchy--Schwarz, (5), (7), (8), and the covariance part of \(b^{(2)}\)
give
\[
 \begin{split}
 U_k&\le (Q/5+1/100)\,3+S Q^2/100\\
 &\le\frac{167}{200}+\frac{77763}{2880000}
 =\frac{2482563}{2880000}<9/10<1.                         \tag{9}
 \end{split}
\]
Thus a first index with \(U_k>1\) or \(V_k>1\) is impossible.
Equivalently, simultaneous induction proves the strict bounds (7),(9).
There is no use of \(U_k\) to establish either one: the causal order is
\(a^{(2)}_{k\cdot},H^{(2)}_k,a^{(3)}_{k\cdot},\delta^{(3)}_k,
b^{(3)}_{k\cdot},q^{(2)}_k,\delta^{(2)}_k,b^{(2)}_{k\cdot}\).

Finally \(q^{(2)}_k=\zeta^{(2)}_k+\beta_k\), with
\(|\beta_k|\le aV_k\le7/6\) and
\(\operatorname{Var}(\zeta^{(2)}_k)\le(7/40)^2\). This proves (1).
In particular its positive-part tail second moment tends to zero at a
Gaussian rate, uniformly in every mesh and auxiliary clipping level.

## Physical-horizon margin: a separate implication

Suppose the uncut population feature flow has been constructed on
\([0,3/2]\), with its actual gradient identity
\(df/ds=K^{(1)}+K^{(2)}+K^{(3)}+K^{(4)}\), all terms nonnegative and
\(K^{(4)}=\mathbb E[(H^{(3)})^2]\). Then \(f(0)=0\) and
\(f'\ge25/36\). There is a unique \(s_*\le36/25<3/2\) with
\(f(s_*)=1\). If \(f'\) is continuous, it is bounded above on this
interval. Therefore \(s'=2(1-f(s)),\ s(0)=0\), stays strictly below
\(s_*\) at every finite physical time and defines the uncut physical
flow globally. To see nonattainment, with \(B=\sup_{[0,s_*]}f'\),
\(1-f(s)\le B(s_*-s)\); Gronwall bounds \(s_*-s(t)\) below by
\(s_*\exp(-2Bt)>0\).

This implication does not assume that auxiliary clipped flows are
gradient flows. It does not yet prove cutoff removal, autonomous
restartability, raw-GD transfer, or non-laziness. Those must be supplied
in the assembled theorem. The raw-GD natural-coordinate update is not
the transformed Euler update used in this lemma.

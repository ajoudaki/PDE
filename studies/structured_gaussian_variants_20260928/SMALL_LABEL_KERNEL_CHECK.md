# Small-label kernel check

Status: complete scoped derivation, not promoted material. Inputs: the supervisor's assignment and `docs/notation.qmd` only. No experiments, other study material, or external results were used.

## Precise statement and conventions

Let $L\ge2$, with $m,n,d\ge1$, and put $q_a=x_a/\sqrt d$, so that $\|q_a\|_2=1$. Write $v=W^{(L+1)}$, use tanh at every hidden layer, and use exactly the canonical network

\[
h_a^{(1)}=\tanh(W^{(1)}q_a),\qquad
h_a^{(\ell)}=\tanh(W^{(\ell)}h_a^{(\ell-1)}),\quad
f_a=\frac{v^Th_a^{(L)}}n.
\]

The loss is $m^{-1}\sum_a(f_a-y_a)^2$. Unit mobility multipliers mean the actual block mobilities are $n,1,\ldots,1,n$, as stipulated in the notation contract. In particular, the prediction equation below has the factor $2$.

Assume $v(0)=0$ and $\|W^{(\ell)}(0)\|_{\mathrm{op}}\le M$ for $2\le\ell\le L$, with $M\ge0$. The proof does not need an initial bound on $W^{(1)}$. If an additional initial first-layer bound is intended, the conclusions remain valid, but see the width caveat below.

Set

\[
A=M+1,\quad S=\sum_{j=0}^{L-1}A^{2j},\quad
Y=\frac{\|y\|_2}{\sqrt m},\quad
\rho(t)=\frac{\|r(t)\|_2}{\sqrt m},\quad
s(t)=\int_0^t\rho(u)\,du,
\]

where $r=f-y$. Here $s$ is an auxiliary integrated residual; it is not the separately defined canonical one-sample feature clock.

Let $H_L(t)\in\mathbb R^{n\times m}$ have columns $h_a^{(L)}(t)$, and assume

\[
K_0=\frac{H_L(0)^TH_L(0)}{mn},\qquad
\lambda_0=\lambda_{\min}(K_0)>0.
\]

The following sufficient smallness condition is explicit:

\[
Y\le\frac{\lambda_0^{3/2}}{\sqrt{8S}}.
\tag{1}
\]

Then the all-layer flow exists globally, and, with $B=Y/\lambda_0$,

\[
\rho(t)\le Ye^{-\lambda_0t},\qquad
s(t)\le B(1-e^{-\lambda_0t})\le B.
\tag{2}
\]

The full tangent kernel $K(t)$, normalized by $m$, satisfies

\[
\sup_{t\ge0}\|K(t)-K_0\|_{\mathrm{op}}\le8SB^2.
\tag{3}
\]

For every passive input $x$ with $\|x\|_2=\sqrt d$, define the normalized tangent row $p_x(t)\in\mathbb R^{1\times m}$ by $\dot f_x(t)=-2p_x(t)r(t)$, and its frozen initial value $p_x^0=p_x(0)$. Then

\[
\sup_{t\ge0}\sqrt m\,\|p_x(t)-p_x^0\|_2\le8SB^2.
\tag{4}
\]

The factor $\sqrt m$ in (4) is necessary when comparing a row acting on the residual with its RMS norm. Equivalently, the ordinary row norm is at most $8SB^2/\sqrt m$.

Let $\bar f$ be the frozen readout-only kernel flow, initialized at zero:

\[
\dot{\bar f}=-2K_0(\bar f-y),\qquad
\dot{\bar f}_x=-2p_x^0(\bar f-y),\qquad
\bar f(0)=0,\quad\bar f_x(0)=0.
\]

Then

\[
\sup_{t\ge0}\frac{\|f(t)-\bar f(t)\|_2}{\sqrt m}
\le\frac{4S}{\lambda_0^3}Y^3,
\tag{5}
\]

and, uniformly over all normalized passive inputs,

\[
\sup_{t\ge0}|f_x(t)-\bar f_x(t)|
\le\frac{16S}{\lambda_0^3}
\left(1+\lambda_0^{-1/2}\right)Y^3.
\tag{6}
\]

The constants depend only on $M,L,\lambda_0$, not separately on width or sample size. A width-uniform assertion requires a width-uniform positive lower bound on $\lambda_0$.

## Bootstrap and global existence

With the canonical backward variables, gradient flow is exactly

\[
\dot v=-\frac2m\sum_a r_a h_a^{(L)},\quad
\dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}q_a^T,\quad
\dot W^{(\ell)}=-\frac2{mn}\sum_a r_a\delta_a^{(\ell)}(h_a^{(\ell-1)})^T
\quad(2\le\ell\le L).
\tag{7}
\]

Because $|\tanh|\le1$, $|\tanh'|\le1$, and $m^{-1}\sum_a|r_a|\le\rho$, on any interval where all middle-layer operator norms are at most $A$,

\[
\|h_a^{(\ell)}\|_2\le\sqrt n,\qquad
\|\delta_a^{(\ell)}\|_2\le A^{L-\ell}\|v\|_2,\qquad
\frac{\|v(t)\|_2}{\sqrt n}\le2s(t).
\tag{8}
\]

The last bound follows by integrating $\|\dot v\|_2/\sqrt n\le2\rho$. Substituting it in (7) and integrating $\int_0^t s\rho=s(t)^2/2$ gives

\[
\|W^{(\ell)}(t)-W^{(\ell)}(0)\|_F
\le2A^{L-\ell}s(t)^2\quad(2\le\ell\le L),
\tag{9}
\]

\[
\frac{\|W^{(1)}(t)-W^{(1)}(0)\|_F}{\sqrt n}
\le2A^{L-1}s(t)^2.
\tag{10}
\]

These are precisely the proposed increment constants.

For any normalized training or passive input, put
$d_\ell=\|h^{(\ell)}(t)-h^{(\ell)}(0)\|_2/\sqrt n$.
The Lipschitz property of tanh, followed by the decomposition

\[
W^{(\ell)}(t)h^{(\ell-1)}(t)-W^{(\ell)}(0)h^{(\ell-1)}(0)
=W^{(\ell)}(t)(h^{(\ell-1)}(t)-h^{(\ell-1)}(0))
+(W^{(\ell)}(t)-W^{(\ell)}(0))h^{(\ell-1)}(0),
\]

gives

\[
d_1\le2A^{L-1}s^2,\qquad
d_\ell\le A d_{\ell-1}+2A^{L-\ell}s^2,
\qquad d_L\le2Ss^2.
\tag{11}
\]

In particular, $\|H_L(t)-H_L(0)\|_F/\sqrt{mn}\le2Ss^2$. Since both feature matrices have Frobenius norm at most $\sqrt{mn}$,

\[
\left\|\frac{H_L(t)^TH_L(t)}{mn}-K_0\right\|_{\mathrm{op}}
\le4Ss^2.
\tag{12}
\]

Thus the readout kernel has smallest eigenvalue at least $\lambda_0-4Ss^2$.

Every tangent block is positive semidefinite. Consequently $\dot r=-2K(t)r$ implies, wherever $\rho>0$,

\[
\dot\rho\le-2\lambda_{\min}(K(t))\rho
\le-2(\lambda_0-4Ss^2)\rho.
\tag{13}
\]

For completeness, $\operatorname{tr}K_0\le1$, hence $\lambda_0\le1$. If $Y=0$, the zero residual makes the whole trajectory stationary. Otherwise consider the first possible time that $s$ reaches $B$ or a middle-layer norm reaches $A$. Before that time, (1) gives $4Ss^2\le\lambda_0/2$, so (13) yields (2). At every finite time the resulting bound on $s$ is strictly less than $B$. Also, (9) gives

\[
\max_{2\le\ell\le L}\|W^{(\ell)}(t)-W^{(\ell)}(0)\|_{\mathrm{op}}
\le2A^{L-2}B^2
\le\frac{\lambda_0 A^{L-2}}{4S}\le\frac14.
\]

The last inequality uses $A\ge1$, $S\ge A^{L-2}$, and $\lambda_0\le1$. Thus no middle norm can reach $M+1$. These strict bounds exclude a finite bootstrap stopping time. They also bound every parameter block, including the first block through (10), on every maximal solution. The finite-dimensional vector field is smooth; on a bounded neighborhood it has bounded derivative and is Lipschitz, so a finite maximal existence time would have a finite parameter limit from which the local solution extends. This proves global existence and (2).

## Full tangent kernel and passive rows

The full normalized tangent kernel is the sum of the readout block and the following hidden blocks:

\[
K^{(1)}_{ab}
=\frac{G_{ab}}{mn}(\delta_a^{(1)})^T\delta_b^{(1)},
\qquad
K^{(\ell)}_{ab}
=\frac{((\delta_a^{(\ell)})^T\delta_b^{(\ell)})
((h_a^{(\ell-1)})^Th_b^{(\ell-1)})}{mn^2}
\quad(2\le\ell\le L).
\tag{14}
\]

They are Gram matrices of the appropriately mobility-weighted parameter derivatives and therefore positive semidefinite. Since $G_{aa}=1$, (8) gives

\[
\left\|\sum_{\ell=1}^L K^{(\ell)}\right\|_{\mathrm{op}}
\le\sum_{\ell=1}^L\operatorname{tr}K^{(\ell)}
\le\left(\sum_{\ell=1}^L A^{2(L-\ell)}\right)
\frac{\|v\|_2^2}{n}
\le4Ss^2.
\tag{15}
\]

Combining (12) and (15) proves the stronger time-dependent estimate $\|K(t)-K_0\|_{\mathrm{op}}\le8Ss(t)^2$, hence (3). The initial hidden tangent blocks vanish exactly because $v(0)=0$.

For a normalized passive input $x$, denote the unnormalized tangent kernel by $k$, so $p_{x,a}=k(x,x_a)/m$. The readout entry satisfies

\[
|k_{\rm read}(x,x_a;t)-k_{\rm read}(x,x_a;0)|
\le\frac{\|h_x(t)-h_x(0)\|_2\|h_a(t)\|_2
+\|h_x(0)\|_2\|h_a(t)-h_a(0)\|_2}{n}
\le4Ss^2.
\]

The hidden self-kernel bound from (15), with its sample average removed, is $k_{\rm hidden}(x,x;t)\le4Ss^2$. Applying Cauchy–Schwarz to its derivative feature vectors gives $|k_{\rm hidden}(x,x_a;t)|\le4Ss^2$. Thus each unnormalized full-kernel entry differs from its frozen readout value by at most $8Ss^2$. Dividing by $m$ and taking the row norm proves (4).

## Stable predictor comparison

Let $D=8SB^2$, $E(t)=e^{-2K_0t}$, and $e=r-\bar r=f-\bar f$. The exact residual difference equation is

\[
\dot e=-2K_0e-2(K(t)-K_0)r,\qquad e(0)=0.
\]

Its variation-of-constants formula, (2), and $\|E(t)\|_{\mathrm{op}}\le e^{-2\lambda_0t}$ yield

\[
\frac{\|e(t)\|_2}{\sqrt m}
\le2DY\int_0^t e^{-2\lambda_0(t-u)}e^{-\lambda_0u}\,du
=\frac{2DY}{\lambda_0}(e^{-\lambda_0t}-e^{-2\lambda_0t}).
\tag{16}
\]

Because $\sup_{z\in[0,1]}(z-z^2)=1/4$, this proves (5). Both training predictions converge to $y$; their training discrepancy tends to zero, despite the uniform transient bound.

For the sharper passive estimate used in (6), a frozen-feature inequality removes an unnecessary factor $\lambda_0^{-1/2}$. Write

\[
F=\frac{H_L(0)}{\sqrt{mn}},\qquad b_x=\frac{h_x^{(L)}(0)}{\sqrt n}.
\]

Then $K_0=F^TF$, $p_x^0=b_x^TF/\sqrt m$, $\|b_x\|_2\le1$, and $FK_0^{-1/2}$ has orthonormal columns. Therefore

\[
\sqrt m\,\|p_x^0K_0^{-1/2}\|_2\le1,
\qquad
\sqrt m\,\|p_x^0K_0^{-1}(I-E(\tau))\|_2
\le\lambda_0^{-1/2}\quad(\tau\ge0).
\tag{17}
\]

Let $\Delta K=K-K_0$, $\Delta p_x=p_x-p_x^0$, and $q_x=f_x-\bar f_x$. Integrating $\dot q_x=-2\Delta p_x r-2p_x^0e$ and substituting the formula for $e$ gives

\[
q_x(t)=-2\int_0^t
\left[\Delta p_x(u)-p_x^0K_0^{-1}(I-E(t-u))\Delta K(u)\right]r(u)\,du.
\tag{18}
\]

Here exchanging the integrals is valid because their integrands are continuous on the finite triangular domain; integrating $E$ gives $K_0^{-1}(I-E)/2$. Equations (3), (4), and (17), together with $\int\rho\le Y/\lambda_0$, imply

\[
|q_x(t)|\le2D(1+\lambda_0^{-1/2})\int_0^t\rho(u)\,du
\le\frac{2DY}{\lambda_0}(1+\lambda_0^{-1/2}),
\]

which is (6). Both passive predictors have limits: their derivatives are bounded by a constant times the integrable residual RMS. Thus (6) also bounds the endpoint discrepancy. The frozen predictor is explicitly

\[
\bar f_x(t)=p_x^0K_0^{-1}(I-e^{-2K_0t})y.
\]

## A non-Gaussian example with cubic error at every width

The $O(Y^3)$ bound is not an arbitrary-accuracy approximation at fixed $Y$. There is a simple exact family for which increasing width does not change the discrepancy at all. This family has a deterministic, non-Gaussian initializer. It refutes an inference of arbitrary accuracy from the deterministic norm, gap, and small-label bounds alone; it is not a counterexample to a separate compression claim for the canonical Gaussian initializer.

Take $L=2,m=1,d=2$, training input $x=\sqrt2e_1$, passive input $x_*=\sqrt2e_2$, positive initial scalars $a_0,b_0$, and

\[
W^{(1)}(0)=\mathbf1_n(a_0,a_0),\quad
W^{(2)}(0)=\frac{b_0}{n}\mathbf1_n\mathbf1_n^T,\quad
v(0)=0.
\]

The middle operator norm is $b_0$, and $\lambda_0=h_0^2>0$, where $h_0=\tanh(b_0\tanh a_0)$. Symmetry and (7) preserve

\[
W^{(1)}(t)=\mathbf1_n(a(t),a_0),\quad
W^{(2)}(t)=\frac{b(t)}n\mathbf1_n\mathbf1_n^T,\quad
v(t)=c(t)\mathbf1_n.
\]

Define $h(a,b)=\tanh(b\tanh a)$. The resulting scalar equations, independent of $n$, are

\[
\dot c=2(Y-ch)h,\qquad
\dot a=2(Y-ch)c h_a,\qquad
\dot b=2(Y-ch)c h_b.
\tag{19}
\]

For $Y>0$ sufficiently small, the preceding theorem applies. Positivity of $a,b,h,h_a,h_b$, together with the scalar residual equation, gives $Y-ch>0$ at finite times and monotonicity of $c$. Using $u=c^2/2$ as coordinate in (19) gives

\[
\frac{da}{du}=\frac{h_a}{h},\qquad
\frac{db}{du}=\frac{h_b}{h}.
\]

These right-hand sides are smooth near $(a_0,b_0)$ because $h_0>0$. Taylor expansion of their integral equations therefore yields

\[
a_\infty-a_0=\frac{h_{a,0}}{2h_0^3}Y^2+O(Y^4),\qquad
b_\infty-b_0=\frac{h_{b,0}}{2h_0^3}Y^2+O(Y^4).
\tag{20}
\]

To justify the endpoint substitution, $c_\infty h(a_\infty,b_\infty)=Y$ and the bootstrap gives $a_\infty-a_0,b_\infty-b_0=O(Y^2)$. Hence $u_\infty=Y^2/(2h_0^2)+O(Y^4)$, which inserted in the integral-equation expansions gives (20).

At the passive input the first hidden scalar stays $a_0$. The frozen features at the two inputs coincide, so $\bar f_{x_*}(\infty)=Y$, whereas

\[
f_{x_*}(\infty)
=Y\frac{h(a_0,b_\infty)}{h(a_\infty,b_\infty)}
=Y-\frac{h_{a,0}^2}{2h_0^4}Y^3+O(Y^5),
\tag{21}
\]

with

\[
h_{a,0}=b_0\operatorname{sech}^2(b_0\tanh a_0)
\operatorname{sech}^2a_0>0.
\]

The coefficient in (21) is strictly positive, and the whole finite-width trajectory is identical for every $n$. For any sufficiently small fixed positive $Y$, the endpoint discrepancy is thus nonzero and cannot be reduced by increasing width. This is an explicit possible error floor, not a claim that every dataset has a positive discrepancy.

## Scope qualifications

- The initial operator bound used above concerns the middle matrices $W^{(2)},\ldots,W^{(L)}$. If it also bounds the unscaled first matrix by $M$, then the estimates still hold, but normalized inputs imply $\|h_a^{(L)}(0)\|_2\le M^L$, hence $\lambda_0\le M^{2L}/(mn)$. Under that extra interpretation a width-uniform positive gap is impossible with fixed $M,m,L$. The non-Gaussian replicated counterexample uses a first-layer scale of order one per entry, with first-layer operator norm proportional to $\sqrt n$.
- These bounds compare all-layer training to an explicitly frozen readout-only predictor. They do not derive a finite-dimensional moment closure of the all-layer dynamics.
- The result is a deterministic small-label perturbation theorem with a cubic predictor error budget. At fixed nonzero $Y$, it supplies no arbitrary-$\varepsilon$ approximation, and (21) shows that a width limit alone cannot supply one in general.

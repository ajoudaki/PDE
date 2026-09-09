# Independent adversarial audit of the unaligned curvature budget

## Input, procedure, and verdict

The sole mathematical input was
`/tmp/l3-two-sample-proof-DLuelg/UNALIGNED_CURVATURE_BUDGET.md`
(279 lines). Its SHA-256 at the start of this audit was:

```text
a173459960cccbf09fd9a4a1eb9ea1aa44bb88e86427d965fe8009ec266f0e3d
```

I personally read the complete procedural skill at
`/etc/codex/skills/solve-math-rigorously/SKILL.md`. I did not read other project mathematics, previous reviews, or history; use agents; run mathematical experiments; or edit the candidate. All calculations and counterexamples below are analytic reconstructions from the specified input. Line references refer to that input, not this review.

**Verdict:** No required mathematical repair was found in the scalar estimate (2), its arbitrary-zero-set and absolutely continuous extensions, or the conditional Hilbert-gradient consequence (7). The constants displayed in those estimates, the action bounds, the forward forcing estimate, and the coarse bound are valid. Section 4's scalar objective is indeed continuously Fréchet differentiable on the stated affine Hilbert state space; this does not require Fréchet differentiability of the activation map from $L^2$ to $L^2$.

The qualification is the one already in the statement: Section 4 assumes an existing curve of the actual raw gradient, zero initial readout, the action endpoint bound, and a common exchange-symmetric positive-definite current feature Gram throughout a finite interval. Neither persistence of these Gram properties nor existence of the curve is proved. No exponential-response, uniqueness, or finite-to-population theorem follows. I do not assess the claim of novelty against external literature.

Several proofs are compressed in the candidate. This review supplies their details, particularly the scalar $C^1$ argument, the factor at $\rho=-1$, the single smoothing-error constant, and the passage to almost every neuron. None of the clarifications below requires changing the stated inequalities.

## 1. Activation constants and the exact scalar setup

Throughout, $0\le S<\infty$, all scalar states are real, and all $L^2$ spaces in Section 4 are real spaces over probability measures. Write

\[
q_0(z)=\frac{e^z}{1+e^z},\qquad
p(z)=1+q_0(z),\qquad
\phi''(z)=q_0(z)(1-q_0(z)).
\]

Thus $1<p<2$, $0<\phi''\le1/4$, and

\[
r(z)=\frac{q_0(1-q_0)}{1+q_0}.
\]

For $f(q)=q(1-q)/(1+q)$,

\[
f'(q)=\frac{1-2q-q^2}{(1+q)^2}.
\]

The unique critical point in $(0,1)$ is $q=\sqrt2-1$; the numerator changes from positive to negative there. The endpoint limits are zero, and substitution gives

\[
\max r=3-2\sqrt2=:R.
\]

The constant in lines 6–11 is exact. Also

\[
0<\log p<\log2,\qquad (\log p)'=r,
\qquad |\phi(x)-\phi(y)|\le2|x-y|.
\]

Since $\phi(0)=\log2$, this last inequality gives the global bound

\[
|\phi(z)|\le 2|z|+\log2.
\tag{A1}
\]

The derivative $p>1$ makes $\phi$ strictly increasing. Its limits at the two ends of the real line are respectively $-\infty$ and $+\infty$, so it is a bijection onto $\mathbb R$. Both $p$ and $\log p$ are strictly increasing.

The scalar assumptions are exactly equations (1), continuous $g,h$ with $g>|h|$, and either the stated $C^1$/continuous-forcing regularity or the stated absolutely continuous/integrable-forcing regularity. In particular $g>0$. On the compact interval, set

\[
A=\max_{[0,S]}(g+|h|),\quad
H=\max_{[0,S]}h_+,\quad c=g-h_+>0.
\]

All these upper bounds are finite. No derivative of $g$ or $h$ will be taken. The curvature is nonnegative and satisfies

\[
\beta=\begin{cases}
w\phi''(z_1)/2,&w>0,\\
(-w)\phi''(z_2)/2,&w<0,\\
0,&w=0,
\end{cases}
\qquad \beta\le |w|/8.
\tag{A2}
\]

For an absolutely continuous readout, the real chain rule gives $(w^2)'=2ww'=2wF$ almost everywhere. Hence, with no condition on the initial readout,

\[
|wF|\mathbf1_{\{wF<0\}}=(-wF)_+
=\tfrac12[-(w^2)']_+
\quad\text{almost everywhere}.
\tag{A3}
\]

This verifies the interpretation in lines 41–47, including its factor $1/2$.

## 2. Reconstruction on each nonzero readout sector

Let $q=|w|$, with $z_+=z_1,z_-=z_2$ for $w>0$, and the opposite choices for $w<0$. Direct substitution into both equations for $z_a'$ gives

\[
z_+'=\tfrac q2(gp_+-hp_-)+\ell_+,
\qquad \beta=\tfrac q2\phi''(z_+).
\]

Consequently

\[
(\log p(z_+))'
=\beta\left(g-h\frac{p_-}{p_+}\right)+r(z_+)\ell_+.
\tag{A4}
\]

If $h\le0$, subtracting $c\beta=g\beta$ leaves

\[
-h\frac{p_-}{p_+}\beta\ge0.
\]

If $h>0$, subtracting $c\beta=(g-h)\beta$ leaves

\[
h\frac{p_+-p_-}{p_+}\beta.
\tag{A5}
\]

The sign of $p_+-p_-$ is the sign of $wF$: for $w>0$, $2F=\phi(z_+)-\phi(z_-)$; for $w<0$, $2F=-(\phi(z_+)-\phi(z_-))$. Thus (A5) is nonnegative on the aligned sector $wF\ge0$.

In the remaining sector, the feature-coordinate estimate can be proved without any inverse-function regularity issue. If $x>y$,

\[
p(x)-p(y)=\int_y^x\phi''(t)\,dt
\le R\int_y^x p(t)\,dt
=R(\phi(x)-\phi(y)).
\]

Interchanging $x,y$ proves the absolute-value version. It follows that

\[
|p_+-p_-|\le2R|F|,
\qquad \frac{\beta}{p_+}=\frac{q r(z_+)}2\le\frac{qR}2.
\]

Their product, including the coefficient $h\le H$, is at most

\[
H(2R|F|)(qR/2)=HR^2|wF|.
\]

Finally $r(z_+)\ell_+\ge-R(|\ell_1|+|\ell_2|)$. Therefore, wherever $w\ne0$ and the equations hold,

\[
(\log p(z_+))'\ge c\beta
-HR^2|wF|\mathbf1_{\{wF<0\}}
-R(|\ell_1|+|\ell_2|).
\tag{A6}
\]

This confirms (3)–(4), including the sample reversal for negative readout, the absence of an alignment assumption, and the coefficient $HR^2$ without an extra factor two.

## 3. Arbitrary readout zero sets and absolute continuity

Choose a nonzero nonnegative smooth even bump supported in $[-1,1]$, integrate it from the left, and normalize its total integral so that the result increases from $-1$ to $1$. Rescaling by $\varepsilon>0$ gives a smooth nondecreasing $\sigma_\varepsilon$ equal to $-1$ on $w\le-\varepsilon$ and to $1$ on $w\ge\varepsilon$. Define

\[
\lambda_\varepsilon=(1+\sigma_\varepsilon(w))/2,\qquad
L_\varepsilon=\lambda_\varepsilon\log p_1
+(1-\lambda_\varepsilon)\log p_2.
\]

Since $0\le\lambda_\varepsilon\le1$,

\[
0\le L_\varepsilon\le\log2.
\tag{A7}
\]

For each fixed $\varepsilon$, differentiation gives

\[
L_\varepsilon'
=\lambda_\varepsilon(\log p_1)'
+(1-\lambda_\varepsilon)(\log p_2)'
+\frac{\sigma_\varepsilon'(w)}2F(\log p_1-\log p_2).
\tag{A8}
\]

The last term is nonnegative: $\sigma_\varepsilon'\ge0$, while $F$ and $\log p_1-\log p_2$ have the same sign. This argument does not use the sign of $w$, the shape of its zero set, or isolated crossings.

On $|w|\ge\varepsilon$, the convex combination is the active gate derivative in (A6). On the remaining strip, write $D_i$ for the drift part of $(\log p_i)'$, excluding $r_i\ell_i$. The two actual formulas imply

\[
|D_1|\le \tfrac12 R|w|(gp_1+|h|p_2)\le RA\varepsilon,
\]

and the same bound holds for $D_2$. Also

\[
0\le c\beta\le g|w|/8\le A\varepsilon/8.
\]

Therefore

\[
\lambda_\varepsilon D_1+(1-\lambda_\varepsilon)D_2
\ge -RA\varepsilon
\ge c\beta-A(R+1/8)\varepsilon.
\tag{A9}
\]

This calculation verifies the candidate's single constant

\[
C_G=\max_s(|g|+|h|)(R+1/8)=A(R+1/8).
\]

The candidate's wording that the separate terms are each bounded by $C_G\varepsilon$ would, if used alone, give a wasteful factor two. The sharper separate bounds $RA\varepsilon$ and $A\varepsilon/8$ in (A9) prove exactly its displayed constant; the constant itself needs no repair.

The forcing part of the convex combination is bounded below by

\[
-R\{\lambda_\varepsilon|\ell_1|+(1-\lambda_\varepsilon)|\ell_2|\}
\ge-R(|\ell_1|+|\ell_2|).
\]

On the strip, subtracting the additional nonnegative backward-motion cost only lowers the proposed right side. Combining both regions with (A8)–(A9) proves on the whole interval, almost everywhere,

\[
L_\varepsilon'\ge c\beta-HR^2|wF|\mathbf1_{\{wF<0\}}
-R(|\ell_1|+|\ell_2|)-C_G\varepsilon.
\tag{A10}
\]

After integration and (A7),

\[
\int_0^S c\beta\,ds
\le\log2+HR^2\int_0^S|wF|\mathbf1_{\{wF<0\}}\,ds
+R\int_0^S(|\ell_1|+|\ell_2|)\,ds+C_G\varepsilon S.
\]

Letting $\varepsilon\downarrow0$ proves (2). It is not necessary to take a limit of $L_\varepsilon'$, of the positive switching term, or of an unsmoothed gate potential. No summation over sign intervals, bounded number of crossings, or bounded-variation premise on a selected gate is hidden in the proof. Zeros of positive measure, tangencies, and infinitely accumulating crossings are all covered. The endpoint bound costs $\log2$, not $2\log2$.

For the absolutely continuous extension, real AC functions are continuous and bounded on the finite interval. Composition with the smooth functions used here, and products of their bounded AC values, preserve absolute continuity. The real AC chain and product rules therefore justify (A4) and (A8) almost everywhere, using $w'=F$ there. Each error term is integrable: $g,h,w,z_a,F$ are bounded, $\ell\in L^1$, and for fixed $\varepsilon$ the derivative of $\sigma_\varepsilon$ is bounded. The fundamental theorem for AC functions gives the integrated inequality. The same reasoning works on every closed subinterval, with that subinterval's endpoints and, if desired, its own smaller upper constants.

This establishes the complete scalar claim, including lines 25–27 and 87–120.

## 4. The complete Hilbert state and its metric

Let $\mathcal H_i=L^2(\Omega_i,\mu_i;\mathbb R)$ with $\mu_i(\Omega_i)=1$. The operator blocks are the affine Hilbert spaces

\[
W^{(2)}_0+\mathfrak S_2(\mathcal H_1,\mathcal H_2),
\qquad
W^{(3)}_0+\mathfrak S_2(\mathcal H_2,\mathcal H_3),
\]

where the fixed base operators are bounded and $\mathfrak S_2$ denotes the Hilbert–Schmidt class. A Hilbert–Schmidt increment is bounded, with operator norm at most its Hilbert–Schmidt norm. Therefore every operator appearing in the architecture is bounded. It need not have an integral-kernel representation, and none is required.

For $-1<\rho<1$, the first block is $\mathcal H_1^2$ with inner product

\[
\langle v,u\rangle_C
=\mathbb E_1[v^TC^{-1}u],
\quad C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},
\quad C^{-1}=\frac1{1-\rho^2}
\begin{pmatrix}1&-\rho\\-\rho&1\end{pmatrix}.
\]

Both eigenvalues $1+\rho,1-\rho$ are positive, so this is a Hilbert norm, equivalent to the ordinary product norm for each fixed $\rho$. At $\rho=-1$, the first state and tangent space are restricted to pairs $(x,-x)$, identified isometrically with $\mathcal H_1$ using $\|(x,-x)\|_{\rm raw}^2=\mathbb E_1x^2$. The readout block is $\mathcal H_3$. The direct sum of these metrics and the two Hilbert–Schmidt metrics is the raw Hilbert metric.

In particular, the first-pair convention at $\rho=-1$ is not the ordinary product metric, which would give $2\mathbb E_1x^2$. This factor is material and the candidate uses the correct convention.

For every first-pair tangent and either sample,

\[
|v_a|=|(C^{1/2}e_a)^T(C^{-1/2}v)|
\le \sqrt{e_a^TCe_a}\sqrt{v^TC^{-1}v}
=\sqrt{v^TC^{-1}v}.
\]

After integration, $\|v_a\|_2\le\|v\|_C$. For $\rho=-1$, the same conclusion follows from $v_2=-v_1$. Thus, for a whole-state tangent $\dot\theta$,

\[
\|\dot Z^{(1)}_a\|_2\le\|\dot\theta\|_{\rm raw},
\quad
\|\dot W^{(\ell)}\|_{\rm op}
\le\|\dot W^{(\ell)}\|_{\rm HS}
\le\|\dot\theta\|_{\rm raw}.
\tag{A11}
\]

These inequalities have no missing correlation-dependent factor, even as $\rho$ approaches an allowed boundary.

The bound (A1), probability normalization, and boundedness of the operators inductively put every $Z^{(\ell)}_a,H^{(\ell)}_a$ in its displayed $L^2$ space. Cauchy–Schwarz then makes $J$ a finite real scalar. On every bounded neighborhood in raw coordinates, all forward maps are locally Lipschitz into their $L^2$ spaces: the activation is globally $2$-Lipschitz, and the bilinear map $(W,H)\mapsto WH$ obeys $\|WH\|_2\le\|W\|_{\rm op}\|H\|_2$. This local Lipschitz statement does not assert differentiability of the activation as an $L^2$-valued map.

## 5. Direct proof that the scalar objective is $C^1$

### 5.1 The weighted scalar remainder

For $z,v,B\in L^2$ define

\[
R_z(v)=\phi(z+v)-\phi(z)-p(z)v.
\]

The pointwise Taylor bound and the Lipschitz bound, respectively, are

\[
|R_z(v)|\le |v|^2/8,
\qquad |R_z(v)|\le4|v|.
\]

Truncating the fixed factor $B$ at magnitude $N$ gives exactly

\[
|\langle B,R_z(v)\rangle|
\le \frac N8\|v\|_2^2
+4\|B\mathbf1_{\{|B|>N\}}\|_2\,\|v\|_2.
\tag{A12}
\]

For fixed $N$, divide by $\|v\|_2$ and let $\|v\|_2\to0$. The limsup is bounded by the second coefficient. It tends to zero as $N\to\infty$, since $B\in L^2$. Thus

\[
\langle B,R_z(v)\rangle=o(\|v\|_2).
\tag{A13}
\]

The bounded-part constant is $N/8$, not $N/4$; the tail constant $4$ is valid, though not sharp. The little-oh conclusion is a two-stage limit, as the candidate explicitly states. It is uniform in the base field $z$ for each fixed $B$, which is more than is needed here.

### 5.2 Full expansion from the scalar output

Fix a base state. For a perturbation of raw norm $t$, write its blocks as $h_a$ in the first fields, $U$ in $W^{(2)}$, $V$ in $W^{(3)}$, and $k$ in the readout. Every coordinate perturbation is $O(t)$ in its specified norm by (A11). Let $\Delta H^{(\ell)}_a,\Delta Z^{(\ell)}_a$ denote the actual changes in the corresponding forward fields. The local Lipschitz bounds just proved give

\[
\|\Delta H^{(\ell)}_a\|_2+
\|\Delta Z^{(\ell)}_a\|_2=O(t)
\]

for each applicable layer. The exact bilinear identities are

\[
\begin{aligned}
\Delta Z^{(2)}_a
&=W^{(2)}\Delta H^{(1)}_a+U H^{(1)}_a
+U\Delta H^{(1)}_a,\\
\Delta Z^{(3)}_a
&=W^{(3)}\Delta H^{(2)}_a+V H^{(2)}_a
+V\Delta H^{(2)}_a.
\end{aligned}
\tag{A14}
\]

The last term in each line is $O(t^2)$ in $L^2$, using the operator norm bound on the increment. No product of two unrestricted $L^2$ fields is being declared an $L^2$ field.

For one sample, the exact scalar prediction change is

\[
\Delta\langle w,H^{(3)}_a\rangle
=\langle k,H^{(3)}_a\rangle
+\langle w,\Delta H^{(3)}_a\rangle
+\langle k,\Delta H^{(3)}_a\rangle.
\]

The last term is $O(t^2)$. Applying (A13) with the fixed base readout $B=w$ gives

\[
\langle w,\Delta H^{(3)}_a\rangle
=\langle wp(Z^{(3)}_a),\Delta Z^{(3)}_a\rangle+o(t).
\]

Define the base-state backward fields

\[
\delta^{(3)}_a=wp(Z^{(3)}_a),\quad
\delta^{(2)}_a=p(Z^{(2)}_a)(W^{(3)})^*\delta^{(3)}_a,\quad
\delta^{(1)}_a=p(Z^{(1)}_a)(W^{(2)})^*\delta^{(2)}_a.
\tag{A15}
\]

Each belongs to $L^2$, since the gates are bounded and the adjoint operators are bounded. Insert (A14), move the fixed $W^{(3)}$ across the inner product, and use (A13) with the fixed factor $(W^{(3)})^*\delta^{(3)}_a$. This gives

\[
\langle w,\Delta H^{(3)}_a\rangle
=\langle\delta^{(3)}_a,VH^{(2)}_a\rangle
+\langle\delta^{(2)}_a,\Delta Z^{(2)}_a\rangle+o(t).
\]

Repeat with the second linearly propagated term, this time using the fixed factor $(W^{(2)})^*\delta^{(2)}_a$. The result is

\[
\begin{aligned}
\Delta\langle w,H^{(3)}_a\rangle
={}&\langle k,H^{(3)}_a\rangle
+\langle\delta^{(3)}_a,VH^{(2)}_a\rangle\\
&+\langle\delta^{(2)}_a,UH^{(1)}_a\rangle
+\langle\delta^{(1)}_a,h_a\rangle+o(t).
\end{aligned}
\tag{A16}
\]

There are only finitely many scalar remainders, each $o(t)$, and all bilinear error terms are $O(t^2)$. Taking half the difference of the two samples proves Fréchet differentiability of the scalar objective in the entire raw Hilbert norm.

### 5.3 Actual Riesz gradient blocks, including $\rho=-1$

For $u,v$ in the target and source Hilbert spaces, respectively, the rank-one operator $(u\otimes v)h=u\langle v,h\rangle$ has

\[
\|u\otimes v\|_{\rm HS}=\|u\|_2\|v\|_2,\qquad
\langle u\otimes v,U\rangle_{\rm HS}=\langle u,Uv\rangle.
\]

Thus (A16) gives the two operator gradients

\[
\nabla_{W^{(\ell)}}J=
\tfrac12\bigl(\delta^{(\ell)}_1\otimes H^{(\ell-1)}_1
-\delta^{(\ell)}_2\otimes H^{(\ell-1)}_2\bigr),
\quad \ell=2,3,
\tag{A17}
\]

and the readout gradient

\[
\nabla_wJ=(H^{(3)}_1-H^{(3)}_2)/2.
\tag{A18}
\]

The first-field differential is $\mathbb E_1[b^Th]$, where

\[
b=(\delta^{(1)}_1,-\delta^{(1)}_2)^T/2.
\]

For $-1<\rho<1$, its Riesz representative in the $C^{-1}$ metric is $Cb$, because $\mathbb E_1[(Cb)^TC^{-1}h]=\mathbb E_1[b^Th]$.

At $\rho=-1$, a tangent has the form $(h,-h)$, and the differential is

\[
\tfrac12\mathbb E_1[(\delta^{(1)}_1+\delta^{(1)}_2)h].
\]

The scalar-coordinate gradient is therefore $(\delta^{(1)}_1+\delta^{(1)}_2)/2$. As a pair it is

\[
\left(\frac{\delta^{(1)}_1+\delta^{(1)}_2}{2},
-\frac{\delta^{(1)}_1+\delta^{(1)}_2}{2}\right)=Cb.
\tag{A19}
\]

It lies in the restricted tangent space and uses exactly the metric specified by the candidate. There is no missing factor $1/2$ from the singular correlation case. These are gradients of $J$ itself; inserting a loss residual or changing the operator normalization would describe a different flow.

### 5.4 Continuity of the gradient

Suppose base states converge in raw norm. Their operators converge in operator norm and remain locally bounded; the forward fields converge strongly in $L^2$. To propagate backward fields, the key elementary fact is that, for a fixed $B\in L^2$ and $z_n\to z$ in $L^2$,

\[
\|(p(z_n)-p(z))B\|_2
\le \frac N4\|z_n-z\|_2
+\|B\mathbf1_{\{|B|>N\}}\|_2.
\tag{A20}
\]

Here $p$ is $1/4$-Lipschitz and its range has diameter one. Taking first $n\to\infty$ and then $N\to\infty$ proves convergence to zero. If also $B_n\to B$, the extra term $p(z_n)(B_n-B)$ has norm at most $2\|B_n-B\|_2$. Bounded-operator multiplication is continuous under the just-established convergences. Applying these facts successively in (A15) proves strong $L^2$ convergence of every backward field.

Rank-one gradients converge in Hilbert–Schmidt norm because

\[
\|u_n\otimes v_n-u\otimes v\|_{\rm HS}
\le\|u_n-u\|_2\|v_n\|_2+\|u\|_2\|v_n-v\|_2.
\]

The readout and first-pair gradients converge in their own Hilbert norms as well, using (A18)–(A19) and the fixed metric. This completes the scalar $C^1$ proof. The argument uses neither an $L^2$-valued Taylor remainder of order $o(\|v\|_2)$ nor operator-norm continuity of the gate multiplication maps.

## 6. Chain rule, action identity, and readout motion

Now impose precisely the conditional premise in lines 182–184: an existing $C^1$ curve on the finite interval, satisfying $\theta'=\nabla_{\rm raw}J$, with $w(0)=0$ almost surely and $J(S)\le1$. Since the objective is $C^1$, its composition with this curve obeys

\[
\frac d{ds}J(\theta(s))
=DJ(\theta(s))[\theta'(s)]
=\langle\nabla_{\rm raw}J,\theta'\rangle_{\rm raw}
=\|\theta'\|_{\rm raw}^2.
\]

The zero initial readout gives $J(0)=0$. Integrating yields

\[
A_{\rm act}:=\int_0^S\|\theta'\|_{\rm raw}^2\,ds
=J(S)\le1.
\tag{A21}
\]

In particular $J(S)\ge0$ under these premises. No loss identity, clipped-flow identity, or limit of approximations has been substituted for this direct chain rule.

Let $F=w'$, which is (A18). The readout block is one summand of the raw squared norm, so

\[
A_F:=\mathbb E_3\int_0^S F^2\,ds\le A_{\rm act}\le1.
\tag{A22}
\]

For almost every neuron, $w(s)=\int_0^sF(u)\,du$. Cauchy–Schwarz gives

\[
w(s)^2\le s\int_0^sF(u)^2\,du.
\]

Tonelli's theorem applies to these nonnegative functions. Integrating explicitly,

\[
\begin{aligned}
\mathbb E_3\int_0^S w(s)^2\,ds
&\le \mathbb E_3\int_0^S
\left(\int_u^S s\,ds\right)F(u)^2\,du\\
&=\frac12\mathbb E_3\int_0^S(S^2-u^2)F(u)^2\,du\\
&\le \frac{S^2}{2}A_F.
\end{aligned}
\tag{A23}
\]

On the product of time and neuron probability, Cauchy–Schwarz now gives

\[
\begin{aligned}
\mathbb E_3\int_0^S|wF|\mathbf1_{\{wF<0\}}\,ds
&\le
\left(\mathbb E_3\int_0^S w^2\,ds\right)^{1/2}
\left(\mathbb E_3\int_0^S F^2\,ds\right)^{1/2}\\
&\le\frac S{\sqrt2}A_F\le\frac S{\sqrt2}.
\end{aligned}
\tag{A24}
\]

Thus the constants in lines 187–201 are correct. This estimate is deliberately coarse: it bounds the negative part by the full absolute product.

## 7. Along-curve chain rules and the actual forward forcing

### 7.1 Representatives and differentiation along the curve

The Hilbert-valued fundamental theorem used here is the following: an absolutely continuous curve $u:[0,S]\to\mathcal H$, with $\mathcal H$ a Hilbert space, has a Bochner integrable derivative $f$ and satisfies $u(s)=u(0)+\int_0^sf(t)\,dt$ in $\mathcal H$. For the assumed $C^1$ raw curve this holds directly with a continuous derivative. It also applies to the AC forward curves constructed below.

When $\mathcal H=L^2(\Omega)$, a strongly measurable $f\in L^1([0,S];L^2)$ has a jointly measurable representative, obtained from its simple-function approximations. Since the measure is a probability measure,

\[
\int_0^S\mathbb E|f(t)|\,dt
\le\int_0^S\|f(t)\|_2\,dt<\infty.
\]

Fubini therefore makes

\[
\widetilde u(s,\omega)=u(0,\omega)+\int_0^s f(t,\omega)\,dt
\]

an absolutely continuous scalar curve for almost every $\omega$, representing $u(s)$ in $L^2$ for every $s$. This constructs a single usable null set, rather than selecting unrelated pointwise versions at every time.

The real AC chain rule gives

\[
\phi(\widetilde u(s))-\phi(\widetilde u(0))
=\int_0^s p(\widetilde u(t))f(t)\,dt
\quad\text{almost surely}.
\]

The integrand is Bochner integrable in $L^2$, with norm at most $2\|f(t)\|_2$. Measurability and the required multiplier convergence follow by the truncation argument (A20); alternatively they follow from jointly measurable representatives and simple approximations. Thus the same identity holds in $L^2$, proving the along-curve chain rule

\[
\frac d{ds}\phi(u(s))=p(u(s))u'(s)
\quad\text{in }L^2\text{ almost everywhere}.
\tag{A25}
\]

This is independent of Fréchet differentiability of the activation map. For a $C^1$ $L^2$ curve the right side is even continuous in $L^2$, by (A20) and continuity of $u'$.

The product rule needed here follows from bounded bilinearity of the operator action: if $W$ is $C^1$ in operator norm and $H$ is AC in $L^2$, their product is AC with derivative $W'H+WH'$ almost everywhere. In the present situation the operator curves are $C^1$ in Hilbert–Schmidt increments, hence in operator norm, and are uniformly bounded on the compact interval. This verifies all hypotheses of this product rule; no differentiability theorem for arbitrary AC curves in the space of bounded operators is needed.

### 7.2 The radius and each forward constant

Cauchy–Schwarz in time and (A21) give, for $s\le S$,

\[
\|\theta(s)-\theta(0)\|_{\rm raw}
\le\int_0^s\|\theta'(u)\|_{\rm raw}\,du
\le\sqrt{sA_{\rm act}}\le\sqrt S.
\tag{A26}
\]

Let $M_0$ bound the two initial first-field $L^2$ norms and the two initial operator norms, as in the candidate. With

\[
M=M_0+\sqrt S,\qquad B_1=2M+\log2,
\]

(A11), (A26), and (A1) yield

\[
\|Z^{(1)}_a\|_2\le M,\quad
\|W^{(2)}\|_{\rm op},\|W^{(3)}\|_{\rm op}\le M,\quad
\|H^{(1)}_a\|_2\le B_1.
\tag{A27}
\]

Writing $V(s)=\|\theta'(s)\|_{\rm raw}$, the exact forward derivative formulas and (A25) give

\[
\|(H^{(1)}_a)'\|_2\le2V,
\]

\[
\begin{aligned}
\|(Z^{(2)}_a)'\|_2
&=\|(W^{(2)})'H^{(1)}_a+W^{(2)}(H^{(1)}_a)'\|_2\\
&\le B_1\|(W^{(2)})'\|_{\rm HS}
+M\|(H^{(1)}_a)'\|_2
\le(B_1+2M)V,
\end{aligned}
\]

and

\[
\|(H^{(2)}_a)'\|_2\le2(B_1+2M)V.
\tag{A28}
\]

The forcing is exactly

\[
\ell_a=W^{(3)}(H^{(2)}_a)'.
\tag{A29}
\]

The term $(W^{(3)})'H^{(2)}_a$ is reserved for the top Gram drift; including it again in $\ell_a$ would double-count it. From (A27)–(A29),

\[
\|\ell_a\|_2\le2M(B_1+2M)V,
\]

so summing the two squared sample bounds and integrating gives

\[
\begin{aligned}
\mathbb E_3\int_0^S(|\ell_1|^2+|\ell_2|^2)\,ds
&\le 8M^2(B_1+2M)^2\int_0^S V^2\,ds\\
&\le C_S^2,\qquad C_S=2\sqrt2\,M(B_1+2M).
\end{aligned}
\tag{A30}
\]

This verifies every coefficient in lines 204–227. The initial operators need only be bounded: no Hilbert–Schmidt norm bound on their fixed base parts has entered.

## 8. Common Gram coefficients, top equations, and neuronwise applicability

Let $U_a=H^{(2)}_a$. Their Gram is the scalar matrix

\[
G(s)=
\begin{pmatrix}
\langle U_1,U_1\rangle&\langle U_1,U_2\rangle\\
\langle U_2,U_1\rangle&\langle U_2,U_2\rangle
\end{pmatrix}.
\]

The stipulated equality of the two diagonal entries makes this $[[g,h],[h,g]]$. Its eigenvalues are $g+h$ and $g-h$, so positive definiteness is exactly $g>|h|$. The entries are continuous because the feature fields are continuous in $L^2$. They are inner products over $\Omega_2$, and therefore are common scalars for every neuron in $\Omega_3$. There is no pointwise third-layer normalization or neuron-dependent Gram hidden in these definitions.

From the actual gradient (A17),

\[
(W^{(3)})'
=\tfrac12\left((wp_1)\otimes U_1-(wp_2)\otimes U_2\right).
\]

Applying this rank-one operator to each current feature gives in $\mathcal H_3$

\[
(W^{(3)})'U_1=\tfrac w2(gp_1-hp_2),\qquad
(W^{(3)})'U_2=\tfrac w2(hp_1-gp_2).
\]

Together with the product rule, (A18), and (A29), these are exactly equations (1). All factors $1/2$ and sample signs agree. This derivation is valid for arbitrary bounded base operators; the derivative operator itself is finite rank.

The readout and the two top preactivations admit the simultaneous coordinatewise AC representatives constructed in Section 7. Their derivative identities hold in $L^2$ almost everywhere in time. Fubini transfers the finitely many identities to almost every neuron, holding for almost every time on one common full-measure set. The forcing belongs to $L^2([0,S]\times\Omega_3)^2$ by (A30), hence is integrable in time for almost every neuron. The top equations' remaining terms are legitimate $L^2$ fields: their gates are bounded, $w$ is in $L^2$, and the Gram scalars are bounded.

These statements verify every hypothesis of the AC scalar lemma for almost every neuron on the whole interval. Pointwise $C^1$ regularity of Hilbert-valued coordinates, point evaluations as bounded linear maps on $L^2$, and a countable neuron index set are not required.

For an explicit trajectory-independent upper Gram constant, set

\[
B_2=2MB_1+\log2.
\]

Then $\|Z^{(2)}_a\|_2\le MB_1$, $\|U_a\|_2\le B_2$, and Cauchy–Schwarz gives

\[
0\le H=\max h_+\le \max g\le B_2^2.
\tag{A31}
\]

Thus $H$ in the candidate is common and finite, and can, if desired, be replaced by this bound depending only on $M_0,S$. No $L^\infty$ bound in the neuron variables is needed.

For a single fixed curve, continuity and strict positivity on the compact interval already imply

\[
c_{\min}=\min_{s\in[0,S]}(g(s)-h(s)_+)>0.
\tag{A32}
\]

Consequently the phrase “if additionally $c\ge c_*>0$” is unnecessary if it merely means some curve-dependent number. Its useful interpretation is a supplied quantitative lower bound uniform over a family of curves or approximations. Such a lower bound does not follow from the upper initial bounds. There is no extra neuron-uniformity issue for this architecture because $c$ is already common; uniformity across trajectories or approximation parameters is a separate requirement.

The feature Gram's symmetry and positive definiteness remain assumptions. The state specification or the raw action identity alone does not assert them or establish their persistence.

## 9. Averaging and the coarse estimates

Apply (2) to almost every neuron. Its common quantities $c(s)$ and $H$ can be kept outside the neuron expectation. The expected backward-motion cost is bounded by (A24). For the force, Cauchy–Schwarz on time, neuron probability, and the two-point sample counting measure yields

\[
\begin{aligned}
\mathbb E_3\int_0^S(|\ell_1|+|\ell_2|)\,ds
&\le \sqrt{2S}
\left(\mathbb E_3\int_0^S(|\ell_1|^2+|\ell_2|^2)\,ds\right)^{1/2}\\
&\le\sqrt{2S}\,C_S.
\end{aligned}
\tag{A33}
\]

The expectation of the universal endpoint budget is $\log2$, since $\mu_3$ is a probability measure. Tonelli applies to the nonnegative terms, and the displayed bounds make the right side finite. This proves exactly

\[
\mathbb E_3\int_0^S c(s)\beta(s)\,ds
\le\log2+HR^2\frac S{\sqrt2}+R\sqrt{2S}\,C_S.
\tag{A34}
\]

This is (7), with no missing probability, sample, or time factor. If a valid uniform $c_*>0$ is available, division by it bounds the unweighted expectation. Replacing $H$ by $B_2^2$ in (A34) is an optional upper-bound simplification.

Independently of the Gram assumptions, (A2), (A23), and product-space Cauchy–Schwarz give

\[
\begin{aligned}
\mathbb E_3\int_0^S\beta\,ds
&\le\frac18\mathbb E_3\int_0^S|w|\,ds\\
&\le\frac{\sqrt S}{8}
\left(\mathbb E_3\int_0^S w^2\,ds\right)^{1/2}
\le\frac{S^{3/2}}{8\sqrt2}.
\end{aligned}
\tag{A35}
\]

The coarse constant in lines 259–261 is correct.

There is a modest optional strengthening, not a repair. For $K(\omega)=\int_0^S\beta(s,\omega)\,ds$, the zero initial readout also implies pathwise

\[
\begin{aligned}
K
&\le\frac18\int_0^S\int_0^s|F(u)|\,du\,ds\\
&=\frac18\int_0^S(S-u)|F(u)|\,du
\le\frac{S^{3/2}}{8\sqrt3}
\left(\int_0^S F(u)^2\,du\right)^{1/2}.
\end{aligned}
\]

Consequently

\[
\mathbb E_3K\le\frac{S^{3/2}}{8\sqrt3},
\qquad
\mathbb E_3K^2\le\frac{S^3}{192}.
\tag{A36}
\]

This shows that the action premise supplies a second moment as well. The candidate does not claim otherwise; neither this improvement nor its stated first moment yields an exponential moment.

## 10. Analytic counterexamples and failed stronger inferences

The following are adversarial checks of nearby stronger interpretations. None contradicts (2) or the conditional statement (7).

### 10.1 The activation really need not be Fréchet differentiable into $L^2$

On the nonatomic probability space $(0,1)$, take the base field $z=0$ and perturbations $v_n=\mathbf1_{(0,1/n)}$. If the map $z\mapsto\phi(z)$ from $L^2$ to $L^2$ had a Fréchet derivative at zero, its derivatives along bounded fixed directions, followed by density, would force that derivative to be multiplication by $p(0)=3/2$. But

\[
\frac{\|\phi(v_n)-\phi(0)-\tfrac32v_n\|_2}{\|v_n\|_2}
=\phi(1)-\phi(0)-\tfrac32>0
\]

for every $n$, by strict convexity of $\phi$. This refutes that stronger differentiability assertion. It does not refute the scalar argument, since (A12) pairs the remainder with a fixed $L^2$ field before estimating.

### 10.2 Deleting the forcing cost destroys the scalar budget

Take constant $g=1,h=0$, $w=1$, $z_1=z_2=0$, and

\[
\ell_1=-3/4,\qquad \ell_2=3/4.
\]

Since $p(0)=3/2$, equations (1) hold exactly with $F=0$. Here $c=1$ and $\beta=1/8$, so $\int_0^S c\beta=S/8$. It exceeds $\log2$ whenever $S>8\log2$. This disproves a version of (2) with its forcing term omitted. The example is within the scalar lemma's assumptions; the scalar lemma does not require zero initial readout.

### 10.3 Unaligned sectors can have negative active-gate drift

At a time with $g=1,h=3/4,w=1$, take

\[
z_1=-\log9,\qquad z_2=\log9.
\]

Then $p_1=11/10$, $p_2=19/10$, $\phi''(z_1)=9/100$, and $F<0$. With $\ell=0$ at this state,

\[
z_1'=\tfrac12\left(\frac{11}{10}-\frac34\frac{19}{10}\right)
=-\frac{13}{80},
\]

so $(\log p_1)'<0$, whereas $c\beta=(1/4)(9/200)>0$. Thus the drift inequality with the unaligned correction deleted is false. This is a local algebraic obstruction to that proof shortcut; it is not asserted to disprove every conceivable stronger integrated inequality.

### 10.4 Strict Gram positivity gives no common lower gap from upper bounds

Use two-point probability spaces for the first two layers, with mass $1/2$ at each point, and choose $\rho=0$. Let the first sample's initial first field be $(a,b)$ and the second's $(b,a)$, with fixed $a\ne b$, and take $W^{(2)}=\varepsilon I$, $0<\varepsilon\le1$, identifying the two copies of the two-point $L^2$ space. The remaining operator and readout can initially be zero. The second-layer features are $(u_\varepsilon,v_\varepsilon)$ and $(v_\varepsilon,u_\varepsilon)$, where

\[
u_\varepsilon=\phi(\varepsilon\phi(a)),
\qquad v_\varepsilon=\phi(\varepsilon\phi(b)).
\]

For sufficiently small positive $\varepsilon$, both are positive and unequal. Their Gram is exactly exchange symmetric, with

\[
g=\frac{u_\varepsilon^2+v_\varepsilon^2}{2},\qquad
h=u_\varepsilon v_\varepsilon,\qquad
c=g-h=\frac{(u_\varepsilon-v_\varepsilon)^2}{2}>0.
\]

Both eigenvalues are positive, but $c\to0$ as $\varepsilon\to0$, while the first-field and operator upper bounds stay bounded. This is already a counterexample at the level of admissible states to a lower-gap conclusion from upper initial bounds alone. It does not challenge the compactness argument (A32) for one fixed curve.

### 10.5 Finite moments do not imply exponential moments

Let $t$ be uniform on $(0,1)$ and

\[
X(t)=\frac{t^{-1/4}}{\sqrt2}.
\]

Then $\mathbb EX^2=1$, whereas $\mathbb E e^{\lambda X}=\infty$ for every $\lambda>0$. Indeed, the substitution $y=t^{-1/4}$ converts the latter integral to

\[
4\int_1^\infty e^{\lambda y/\sqrt2}y^{-5}\,dy=\infty.
\]

Multiplication by any positive constant preserves this absence of exponential integrability while reducing either finite-moment bound as much as desired.

One can also realize the obstruction within the forced scalar systems and the readout/forcing estimates themselves, without merely choosing an abstract curvature random variable. On $[0,1]$, use this neuron variable $X$, common $g=1,h=0$, and

\[
w(s,t)=sX(t),\qquad z_1(s,t)=0,\qquad
z_2(s,t)=\phi^{-1}(\log2-2X(t)).
\]

These fields belong to $L^2$: the inverse of $\phi$ is $1$-Lipschitz, so $|z_2|\le2X$. Their readout derivative is exactly $F=X$. Put

\[
\ell_1=-\frac34sX,\qquad
\ell_2=\frac12sX\,p(z_2).
\]

Then both preactivation derivatives are zero and equations (1) hold exactly. The zero initial readout and $\mathbb E\int_0^1F^2\,ds=1$ hold, and the total squared forcing integral is finite, since $p<2$. But

\[
\int_0^1\beta\,ds=\int_0^1\frac{sX}{8}\,ds=\frac X{16}
\]

has no positive exponential moment. This is an exact example for the forced scalar family plus the readout and forcing information. It is **not** claimed to be an entire raw-gradient trajectory of the Section 4 architecture, or to satisfy its full-state action identity. Its role is to show precisely why the scalar estimate and these moment controls alone cannot close a response-tail argument.

## 11. Exact claim scope, clarifications, and disposition

The scalar result is a pathwise finite-interval weighted estimate for the stated forced equations. It allows either sign of $h$, either sign of the readout, every unaligned excursion, arbitrary readout zero sets, and the specified AC regularity. It is valid on subintervals without any reset of the readout to zero.

The Section 4 consequence is for an already existing, uncut, raw-gradient-ascent curve of the displayed scalar objective on the specified affine Hilbert state space. Its action-dependent constants use the zero initial readout and $J(S)\le1$. The expected weighted bound uses the additional common exchange-symmetric positive-definite Gram hypothesis throughout the interval. The scalar lemma itself does not create this symmetry, preserve positive definiteness, or construct the curve.

With empirical probability measures, the same Hilbert identities and constants apply to a finite system that satisfies exactly these metric and current-Gram premises. Approximate symmetry is not exact symmetry, and an initialization law or a population symmetry does not by itself supply the required finite pathwise equality. The candidate's finite-system observation should be read only in this conditional sense.

The integrating-factor discussion in Section 5 is a warning about a missing inference, not a specified propagator theorem: no tangent equation, quantified $\Lambda$, or complete estimate of all tangent couplings is stated there. Its mathematically testable assertion is that the available first moment cannot justify exponential integrability, which is correct. Even (A36) does not close that gap. A full response estimate would require its own treatment of the coupled dynamics and distribution of costs.

The following are useful clarifications, not required repairs:

1. The smoothing constant is proved by adding the separate bounds $RA\varepsilon$ and $A\varepsilon/8$, as in (A9).
2. The compact scalar $C^1$ paragraph is justified by the explicit fixed-backward-field expansion (A14)–(A16), together with gradient continuity (A20).
3. At $\rho=-1$, the restricted first gradient is explicitly (A19); the metric is $\mathbb E v_1^2$.
4. For one compact-interval curve, a positive minimum of $c$ is automatic. A useful family-uniform numerical lower bound is an additional issue; upper initial bounds do not supply it.
5. The action premise actually gives the optional second-moment estimate (A36). This improves the coarse information without altering the response limitation.

There are no outstanding repair requirements for the conditional theorem as written, and no counterexample to its stated hypotheses and conclusions was found. All counterexamples above target stronger assertions or omitted hypotheses and are labeled accordingly. No candidate changes were made.

The source SHA-256 was rechecked after the reconstruction and report drafting and matched the exact hash recorded at the beginning of this review.

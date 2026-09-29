# Gaussian block weak bias: a proved tangent rate and the trained gap

Frozen candidate: 2026-09-28. Scoped proof attempt with an initial
independent phase. The candidate was written before the parent sent its
consolidation message reporting independently obtained kernel and cubic
remainder bounds; this final audit considered that message. This file
is the only research artifact written by this route. No experiments,
other studies, other-route reports, or external theorem dependencies were
used. This is not an isolated independent review.

## Result and exact status

For every fixed depth and finite correlated training list, the Gaussian
block population's **initial readout Gram has weak bias $O(k^{-1})$**.
This holds without invertibility of the input Gram and uniformly in a
normalized passive input. A positive dense readout-Gram gap therefore
persists for all sufficiently large block sizes.

There is also a useful nonlinear statement. Subject to the existence of
the regular global-update block population in the question, the actual
small-label trained predictor satisfies

\[
 \sup_{t\ge0}\|f_k(t)-f_\infty(t)\|_{L^2(\mu)}
 \le C\{Y/k+Y^3\}.                                      \tag{1}
\]

Here $Y=(m^{-1}\sum_a y_a^2)^{1/2}\le Y_0$, and $C,Y_0,k_0$ depend
on the fixed depth, mobilities, sample count and initial dense Gram gap,
but not on $k\ge k_0$. Inputs, including the support of the probability
law $\mu$, have norm at most $\sqrt d$. This is an a priori theorem for
the stipulated regular flows, not a construction or uniqueness theorem
for the unbounded block-initializer population.

The proof derives the uniform cubic remainder directly from the exact
gradient-flow equations. It does **not** assume a trained Taylor series.
In particular it proves that the actual predictor map is differentiable
at zero labels in the uniform-in-time passive-prediction norm, and that
its derivative has $O(k^{-1})$ bias.

Equation (1) is **not** a trained width rate for fixed positive $Y$: its
cubic term does not vanish as $k\to\infty$. No exponent

\[
 \sup_{t\ge0}\|f_k(t)-f_\infty(t)\|_{L^2(\mu)}
       \le C_Y k^{-\beta},\qquad \beta>2/3,               \tag{2}
\]

is proved here. The precise missing estimate is a width-decaying
comparison of the nonlinear remainders. An exact finite-system Gaussian
interpolation identity below isolates the additional cancellation it
would require. Neither regularity nor the initial Gram gap supplies that
cancellation.

## Scientific inputs and contract

Read inputs were `docs/index.qmd`, `docs/notation.qmd`, the complete
sections 1--4 and A.3--A.4 of `docs/02-gaussian-reuse.qmd`, its complete
section 13.1, and the model portion of the fixed-depth theorem in
`docs/09-trainability.qmd`. The last is a different activation/data theorem
and was not imported. Section A.3's contained proof supplies the bounded
dense initialized action norm, at most two, on its generated spaces.
The present argument proves its other estimates below.

The canonical model has $L\ge2$ tanh hidden layers, fixed $m,d,L$,
unhalved mean-square loss, mobilities

\[
 n\kappa_1,\ \kappa_2,\ldots,\kappa_L,\ n\kappa_{L+1},
\]

and zero stored readout. First-layer rows are standard Gaussian. Dense
hidden initial entries have variance $1/n$. The surrogate initializer
at $n=Bk$ has $B$ diagonal Gaussian $k\times k$ blocks per hidden
matrix, each with entry variance $1/k$; different layers and blocks
are independent. This variance rescaling is essential: retaining
variance $1/n$ in only the diagonal blocks would erase the hidden bulk
as $B\to\infty$.

Every learned increment remains the **global** rank sum from the
canonical gradient flow. In particular, updates are not projected back
to the initial blocks. The order of limits is first $B\to\infty$
at fixed $k$, then $k\to\infty$. The reference is the dense regular
population flow assumed in the question, not an independently trained
width-$k$ network and not a frozen-feature replacement.

The frozen-feature evolution used below is an explicitly auxiliary
first-order approximation with a proved error. It is not substituted
for the target.

## 1. Exact global-update block equations

Let $\omega$ carry one block's independent first-layer rows and hidden
Gaussian matrices $A_0^{(2)},\ldots,A_0^{(L)}\in\mathbb R^{k\times k}$.
Layer spaces are typed copies of

\[
 \mathcal H_{k,\ell}=L^2\bigl(\omega;\mathbb R^k,k^{-1}\|\cdot\|_2^2\bigr),
 \qquad
 \langle U,V\rangle=\mathbb E\,[U(\omega)^TV(\omega)/k].
\]

The notation for the inner product is used only for these typed abstract
Hilbert spaces. The local block RMS is always written explicitly as

\[
 d_{\ell,x}(\omega,s)=\|\Delta_x^{(\ell)}(\omega,s)\|_2/\sqrt k.
\]

The fixed initializer acts pointwise in $\omega$. It is generally
**unbounded** as an operator on the entire $L^2$ space: its essential
supremum block norm is infinite. A bound for its moments is not an
operator-norm bound. This distinction is retained throughout the proof.
For example, apply it to the first basis vector supported on the
positive-probability event $|A_{11}|>R$; the output/input norm ratio
is at least $R$, for every $R$.

Put $c=W^{(L+1)}$, $W^{(\ell)}=A_0^{(\ell)}+K^{(\ell)}$, with
the rank-one convention $U\otimes V:g\mapsto U\langle V,g\rangle$.
The exact equations are

\[
\begin{aligned}
 \dot c&=-\frac{2\kappa_{L+1}}m\sum_a r_aH_a^{(L)},\\
 \dot K^{(\ell)}&=-\frac{2\kappa_\ell}m\sum_a
       r_a\Delta_a^{(\ell)}\otimes H_a^{(\ell-1)},
                  &&2\le\ell\le L,\\
 \dot Z_x^{(1)}&=-\frac{2\kappa_1}m\sum_a
       r_aG_{ax}\Delta_a^{(1)},
       &G_{ax}&=x_a^Tx/d,\\
 Z_x^{(\ell)}&=(A_0^{(\ell)}+K^{(\ell)})H_x^{(\ell-1)},
       &H_x^{(\ell)}&=\tanh Z_x^{(\ell)},\\
 \Delta_x^{(L)}&=c\odot\tanh'(Z_x^{(L)}),\\
 \Delta_x^{(\ell)}&=\tanh'(Z_x^{(\ell)})\odot
       (A_0^{(\ell+1)}+K^{(\ell+1)})^*\Delta_x^{(\ell+1)},\\
 f_x&=\langle c,H_x^{(L)}\rangle,\qquad r_a=f_a-y_a.
\end{aligned}                                                   \tag{3}
\]

For a passive $x$, its backward field in (3) is only a derivative used
to evaluate a kernel; it contributes no update. At finite $B$, every
inner product in (3) is the average over all $B$ blocks and all their
coordinates. Replacing it by a within-block average changes the model.

The following estimates apply to every regular solution of (3). They
also apply to finite $B$ after replacing expectations by block
averages and using the corresponding empirical moment bounds. Thus
they are a priori bounds, not an assumed quantitative $B$-limit.

## 2. Initial Gaussian kernel: weak bias $1/k$, variance $1/k$

For a fixed list of $p$ inputs with normalized lengths at most one,
let $G\in\mathbb R^{p\times p}$ be its Gram. Define

\[
 \Phi(Q)_{ab}=\mathbb E[\tanh Z_a\tanh Z_b],
       \quad Z\sim N(0,Q),
 \qquad q_1=\Phi(G),\quad q_\ell=\Phi(q_{\ell-1}).      \tag{4}
\]

For one finite Gaussian block let

\[
 Q_\ell=\frac1k\sum_{i=1}^k
       H_i^{(\ell)}H_i^{(\ell)T}\in\mathbb R^{p\times p}.
\]

Then, for constants $C_{p,L}$ independent of $G,k$,

\[
 \mathbb E\|Q_\ell-q_\ell\|_F^2\le C_{p,L}/k,
 \qquad
 \|\mathbb E Q_\ell-q_\ell\|_F\le C_{p,L}/k.            \tag{5}
\]

The second inequality is the useful weak estimate; applying
Cauchy--Schwarz to the first would give only $k^{-1/2}$.

**Covariance differentiation including singular covariances.** For

\[
 \psi_{ab}(z)=\tanh z_a\tanh z_b
\]

all spatial derivatives through order four are bounded. Along any
segment $Q+uD\succeq0$, Gaussian integration by parts gives

\[
\begin{aligned}
 \frac d{du}\mathbb E\psi_{ab}(N(0,Q+uD))
     &=\frac12\sum_{i,j}D_{ij}\mathbb E\partial_{ij}\psi_{ab},\\
 \frac {d^2}{du^2}\mathbb E\psi_{ab}(N(0,Q+uD))
     &=\frac14\sum_{i,j,v,w}D_{ij}D_{vw}
                            \mathbb E\partial_{ijvw}\psi_{ab}.
\end{aligned}                                                   \tag{6}
\]

For positive definite covariance this follows by differentiating its
Gaussian density: its covariance derivative equals one half of the
specified linear combination of second spatial derivatives of that
density. Integrating those derivatives twice by parts produces (6);
Gaussian decay removes boundary terms. For a singular segment, add
$\epsilon I$, prove the identity, and integrate once or twice in $u$.
Coupling Gaussian vectors by their positive semidefinite square roots
and boundedness of the spatial derivatives allow dominated convergence
as $\epsilon\downarrow0$. This proves the integrated identity, hence
the Taylor estimates actually used, without differentiating a singular
square root.

Consequently there are finite $M_p,N_p$, independent of $Q,Q'$,
such that on positive semidefinite matrices

\[
\begin{aligned}
 \|\Phi(Q')-\Phi(Q)\|_F&\le M_p\|Q'-Q\|_F,\\
 \|\Phi(Q')-\Phi(Q)-D\Phi(Q)[Q'-Q]\|_F
       &\le N_p\|Q'-Q\|_F^2.                         \tag{7}
\end{aligned}
\]

The symbol $D\Phi(Q)$ in (7) denotes the bounded linear expression
given by the first line of (6); its restriction to any admissible
covariance segment is all that is needed.

**Recursion.** The first-layer feature rows are iid bounded vectors, so

\[
 \mathbb E Q_1=q_1,\qquad
 \mathbb E\|Q_1-q_1\|_F^2\le p^2/k.
\]

Conditional on all previous layers, the next preactivation rows are
independent $N(0,Q_{\ell-1})$ vectors. Therefore

\[
 Q_\ell=\Phi(Q_{\ell-1})+E_\ell,\qquad
 \mathbb E[E_\ell\mid Q_{\ell-1}]=0,\qquad
 \mathbb E\|E_\ell\|_F^2\le p^2/k.                    \tag{8}
\]

Writing $V_\ell=\mathbb E\|Q_\ell-q_\ell\|_F^2$, conditional
centering removes the cross term and (7) gives

\[
 V_\ell\le p^2/k+M_p^2V_{\ell-1}.
\]

At fixed $L$, this is $C_{p,L}/k$. Writing
$b_\ell=\|\mathbb E Q_\ell-q_\ell\|_F$, the second line of (7)
gives the stronger recursion

\[
 b_\ell\le M_pb_{\ell-1}+N_pV_{\ell-1},\qquad b_1=0.
\]

This proves both inequalities in (5).

The initial block-population kernel is

\[
 \Gamma_k(x,x')=\mathbb E Q_L(x,x'),
\]

whereas the dense initialized kernel is $\Gamma_\infty=q_L$. Taking
$p=m$ gives a training-Gram error $C/k$; taking $p=m+1$ gives the
same bound for every training/passive pair, with constants independent
of the passive input. In particular, if

\[
 \lambda_{\min}(\Gamma_\infty^{\rm train})\ge\lambda>0,
\]

then $\lambda_{\min}(\Gamma_k^{\rm train})\ge\lambda/2$ for
$k\ge k_0=\lceil2C_{m,L}/\lambda\rceil$, after enlarging the
constant to bound the operator norm as well. No input-Gram inverse is
used.

## 3. A uniform small-force bound for the actual learned flow

This section proves the nonlinear remainder estimate; it is not a
formal expansion. Put

\[
 R(t)=\left(m^{-1}\sum_a r_a(t)^2\right)^{1/2},
 \qquad S(t)=2\int_0^tR(u)\,du.                        \tag{9}
\]

Where $R>0$, use $s=S(t)$ and coefficients

\[
 v_a(s)=-r_a(t)/(mR(t)),\qquad \sum_a|v_a(s)|\le1.     \tag{10}
\]

The last inequality is Cauchy--Schwarz. If the residual reaches zero,
the entire flow stops and all following conclusions extend by
constancy. In this clock, (3) has the same formulas with $-2r_a/m$
replaced by $v_a$.

### Uniform block-norm moments

Set $a_\ell(\omega)=\|A_0^{(\ell)}(\omega)\|_{op}$.
For each finite $p\ge1$,

\[
 \sup_{k\ge1}\mathbb E a_\ell^p<\infty.               \tag{11}
\]

Here is a direct proof sufficient for all uses below. A maximal
$1/4$-separated set on the unit sphere has at most $9^k$ points:
the disjoint radius-$1/8$ Euclidean balls centered at its points fit
in the ball of radius $9/8$, and volume comparison gives $9^k$.
It is a $1/4$-net by maximality. Approximate each vector in the
bilinear characterization of the operator norm by this net; the two
errors sum to at most half the norm. Thus

\[
 \|A\|_{op}\le2\max_{u,v\in\mathcal N}|u^TAv|.
\]

For fixed unit $u,v$, $u^TAv\sim N(0,1/k)$, and the elementary
Gaussian exponential-moment bound gives

\[
 \mathbb P\{a_\ell>R\}
 \le 2\,9^{2k}\exp(-kR^2/8).
\]

For $R$ above a fixed numerical threshold this is at most
$2\exp(-kR^2/16)\le2\exp(-R^2/16)$. Integrating
$pR^{p-1}\mathbb P\{a_\ell>R\}$ proves (11). Products of the
finitely many $a_\ell$'s have all fixed moments by Hölder. The
matrices at different layers are independent, although the argument
below needs only these product-moment bounds.

### Backward fields: a descending polynomial envelope

The readout equation and (10) imply the pointwise bound

\[
 |c_i(\omega,s)|\le\kappa_{L+1}s,
 \qquad d_{L,x}(\omega,s)\le\kappa_{L+1}s.             \tag{12}
\]

For $s\le1$, construct polynomials $P_\ell$ of the $a_j$'s,
with nonnegative coefficients independent of $k$, so that

\[
 d_{\ell,x}(\omega,s)\le sP_\ell(\omega),
 \qquad \|\Delta_x^{(\ell)}(s)\|_{\mathcal H_{k,\ell}}
       \le C_\ell s.                                \tag{13}
\]

These estimates hold uniformly over all normalized training and
passive inputs. Start with $P_L=C_L=\kappa_{L+1}$. If (13) holds
at layer $\ell+1$, the exact adjoint memory in (3) is

\[
 K^{(\ell+1)}(s)^*\Delta_x^{(\ell+1)}(s)
  =\kappa_{\ell+1}\int_0^s\sum_a v_a(u)H_a^{(\ell)}(u)
       \langle\Delta_a^{(\ell+1)}(u),
                    \Delta_x^{(\ell+1)}(s)\rangle\,du.
\]

Because each local feature RMS is at most one, its local RMS is at
most

\[
 \kappa_{\ell+1}C_{\ell+1}^2
       s\int_0^s u\,du
 =\tfrac12\kappa_{\ell+1}C_{\ell+1}^2s^3.
\]

The initialized adjoint contributes at most
$a_{\ell+1}sP_{\ell+1}$. Since $|\tanh'|\le1$, one may take

\[
 P_\ell=a_{\ell+1}P_{\ell+1}
             +\tfrac12\kappa_{\ell+1}C_{\ell+1}^2,
 \qquad
 C_\ell\ge\sup_k(\mathbb E P_\ell^2)^{1/2}.           \tag{14}
\]

The supremum is finite by (11). Descending induction proves (13).
This avoids treating the unbounded block initializer as a bounded
population operator.

### Hidden features move only quadratically in force

There are nonnegative polynomials $Q_\ell$ with uniformly bounded
second moments such that

\[
 \|H_x^{(\ell)}(\omega,s)-H_x^{(\ell)}(\omega,0)\|_2/\sqrt k
        \le s^2Q_\ell(\omega),\qquad s\le1.           \tag{15}
\]

For the first layer, $|G_{ax}|\le1$, (10), (13) and the
one-Lipschitz property of tanh yield

\[
 Q_1=\tfrac12\kappa_1P_1.
\]

At layer $\ell\ge2$, write exactly

\[
 Z_x^{(\ell)}(s)-Z_x^{(\ell)}(0)
 =A_0^{(\ell)}\{H_x^{(\ell-1)}(s)-H_x^{(\ell-1)}(0)\}
          +K^{(\ell)}(s)H_x^{(\ell-1)}(s).
\]

The second term's local RMS is bounded by

\[
 \kappa_\ell\int_0^s\sum_a |v_a(u)|
   d_{\ell,a}(\omega,u)
   |\langle H_a^{(\ell-1)}(u),H_x^{(\ell-1)}(s)\rangle|\,du
 \le\tfrac12\kappa_\ell P_\ell(\omega)s^2.
\]

Thus the valid recursion is

\[
 Q_\ell=a_\ell Q_{\ell-1}+\tfrac12\kappa_\ell P_\ell.
                                                               \tag{16}
\]

It uses no independence between $a_\ell$ and $Q_{\ell-1}$;
their polynomial product moments are enough. Let

\[
 C_H\ge\sup_k(\mathbb E Q_L^2)^{1/2}.
\]

Then, for every normalized passive or training input,

\[
 \|H_x^{(L)}(s)-H_x^{(L)}(0)\|_{\mathcal H_{k,L}}
       \le C_Hs^2.                                  \tag{17}
\]

For the dense regular population, the identical proof is performed
directly in the layer Hilbert norms, using
$\|A_0^{(\ell)}\|\le2$ in place of the local norms $a_\ell$.
Pointwise bounded readout still proves (12), and the exact global
rank memories prove all the remaining inequalities. Enlarge the
constants once to cover both populations.

### Kernel drift and closing the all-time estimate

Let $\Gamma(s)_{xx'}=\langle H_x^{(L)}(s),H_{x'}^{(L)}(s)\rangle$.
Using feature norms at most one and (17),

\[
 |\Gamma(s)_{xx'}-\Gamma(0)_{xx'}|\le2C_Hs^2.         \tag{18}
\]

Differentiating the scalar prediction with the exact adjoint fields
in (3) gives the actual trained kernel

\[
\begin{aligned}
 \Theta_{xx'}(s)
  ={}&\kappa_{L+1}\langle H_x^{(L)},H_{x'}^{(L)}\rangle\\
    &+\kappa_1G_{xx'}\langle\Delta_x^{(1)},\Delta_{x'}^{(1)}\rangle\\
    &+\sum_{\ell=2}^L\kappa_\ell
       \langle\Delta_x^{(\ell)},\Delta_{x'}^{(\ell)}\rangle
       \langle H_x^{(\ell-1)},H_{x'}^{(\ell-1)}\rangle.
\end{aligned}                                                   \tag{19}
\]

Each training block is positive semidefinite, since it is a Gram of
the corresponding parameter gradients. Explicitly, products of Grams
are Grams of tensor products, and the first-layer term is the Gram
of $(x_a/\sqrt d)\otimes\Delta_a^{(1)}$.
At zero readout every hidden term vanishes. Equations (13), (18) give

\[
 |\Theta_{xx'}(s)-\kappa_{L+1}\Gamma(0)_{xx'}|
       \le C_\Theta s^2,
 \quad C_\Theta=2\kappa_{L+1}C_H+
                        \sum_{\ell=1}^L\kappa_\ell C_\ell^2.
                                                               \tag{20}
\]

Let $\gamma>0$ be a common lower bound for the initial training
readout Grams. By section 2 one may take $\gamma=\lambda/2$ for
the dense population and all $k\ge k_0$. Set

\[
 s_* =\min\{1,\sqrt{\gamma/(4mC_H)}\},
 \qquad \alpha=\kappa_{L+1}\gamma/m.                 \tag{21}
\]

Up to the first exit from $S<s_*$, (18) implies
$\Gamma(S)\succeq(\gamma/2)I$, so
$\Theta(S)\succeq(\kappa_{L+1}\gamma/2)I$. The exact residual
equation is

\[
 \dot r=-(2/m)\Theta r.
\]

Differentiating $R^2=m^{-1}r^Tr$ therefore gives

\[
 R(t)\le Ye^{-\alpha t},\qquad
 S(t)\le2Y/\alpha.                                  \tag{22}
\]

Choose $Y_0\le\alpha s_*/4$. The right side of the second bound
is at most $s_*/2$, which excludes the supposed first exit by
continuity. Thus (22) holds for all times of the regular flow, and
its uniform bounds preclude growth of the displayed fields. In this
statement global continuation still belongs to the regular-flow
hypothesis; a field bound alone is not a uniqueness theorem on an
unbounded-operator population space.

## 4. Actual uniform cubic remainder and the $1/k$ first derivative

Fix either population, and let $f^{\rm lin}$ be the auxiliary
readout-only evolution with all hidden features frozen at initialization.
Its training residual is

\[
 r^{\rm lin}(t)=-\exp[-(2\kappa_{L+1}/m)\Gamma(0)t]y.
\]

For $e=r-r^{\rm lin}$, subtracting the residual equations gives

\[
 \dot e=-(2\kappa_{L+1}/m)\Gamma(0)e
       -(2/m)[\Theta(t)-\kappa_{L+1}\Gamma(0)]r(t),
 \qquad e(0)=0.                                     \tag{23}
\]

By (20), (22), the norm of the forcing in (23), measured in the
training RMS, is at most $C Y^3e^{-\alpha t}$.
The homogeneous semigroup has norm at most $e^{-2\alpha t}$.
Integrating its variation-of-constants formula proves both

\[
 \sup_{t\ge0}\|e(t)\|_2/\sqrt m\le C Y^3,
 \qquad
 \int_0^\infty\|e(t)\|_2/\sqrt m\,dt\le C Y^3.       \tag{24}
\]

For clarity, the integral of the convolution is bounded by
$C Y^3(2\alpha)^{-1}\alpha^{-1}$; its supremum is bounded by
$C Y^3/\alpha$. All constants are independent of $k$.

For a passive input, the exact scalar derivative is

\[
 \dot f_x=-(2/m)\sum_a\Theta_{xa}(t)r_a(t).
\]

Subtract its frozen counterpart and integrate. Using
$|\Gamma(0)_{xa}|\le1$, (20), (22), (24), and
$m^{-1}\sum_a|r_a|\le R$, gives

\[
\begin{aligned}
 |f_x(t)-f_x^{\rm lin}(t)|
 &\le2\kappa_{L+1}\int_0^t\|e(u)\|_2/\sqrt m\,du
       +2C_\Theta\sup_uS(u)^2\int_0^tR(u)\,du\\
 &\le C Y^3.
\end{aligned}                                                   \tag{25}
\]

This is uniform in $x,t,k$, so also holds in $L^2(\mu)$ for
any probability law on normalized inputs. It directly proves

\[
 \sup_{t\ge0}\|f(t;\varepsilon y)
                -\varepsilon f^{\rm lin}(t;y)\|_{L^2(\mu)}
       \le C|\varepsilon|^3Y^3.                     \tag{26}
\]

Consequently the uniform-in-time predictor map has the asserted
first derivative at zero labels. No differentiation under a Gaussian
expectation, convergence of a Taylor series, or assumed analyticity
was used to reach (26).

It remains to compare the two linearized evolutions. For
$j\in\{k,\infty\}$, write $\Gamma_j$ for the training Gram and
$g_j(x)=(\Gamma_j(x,x_a))_{a=1}^m$. Direct integration gives

\[
 f_j^{\rm lin}(t,x)
  =g_j(x)^T\Gamma_j^{-1}
       [I-e^{-(2\kappa_{L+1}/m)\Gamma_jt}]y.           \tag{27}
\]

By (5), both $\|\Gamma_k-\Gamma_\infty\|_{op}$ and
$\sup_x\|g_k(x)-g_\infty(x)\|_2$ are $O(k^{-1})$.
The inverse difference identity

\[
 \Gamma_k^{-1}-\Gamma_\infty^{-1}
       =\Gamma_k^{-1}(\Gamma_\infty-\Gamma_k)
                              \Gamma_\infty^{-1}
\]

has norm $O(k^{-1})$ because both Grams have gap at least
$\gamma$. With $a=2\kappa_{L+1}/m$, Duhamel's identity gives

\[
\begin{aligned}
 &e^{-a\Gamma_kt}-e^{-a\Gamma_\infty t}\\
 &\quad=-a\int_0^t e^{-a\Gamma_k(t-u)}
          (\Gamma_k-\Gamma_\infty)e^{-a\Gamma_\infty u}\,du,
\end{aligned}
\]

whose norm is at most
$a t e^{-a\gamma t}\|\Gamma_k-\Gamma_\infty\|_{op}$.
The maximum of $at e^{-a\gamma t}$ is $1/(e\gamma)$.
Substitution in (27) proves

\[
 \sup_{t\ge0,x}|f_k^{\rm lin}(t,x)-f_\infty^{\rm lin}(t,x)|
         \le CY/k.                                  \tag{28}
\]

Combining (25) for both actual flows with (28) proves (1).

## 5. What Gaussian interpolation would still have to prove

The following identity isolates a concrete sufficient cancellation
for a trained rate. It does not assume a Gaussian law for trained
coordinates.

Take a finite system of width $n=2Bk$, grouped into $B$ groups
of $2k$ coordinates, each split into two halves. For each initialized
hidden matrix retain the $B$ diagonal $2k\times2k$ blocks, and
interpolate independent entry variances as

\[
 v_{ij}(\tau)=
 \begin{cases}
   (2-\tau)/(2k),&i,j\text{ in the same half},\\
   \tau/(2k),&i,j\text{ in different halves},
 \end{cases}
 \qquad 0\le\tau\le1.                               \tag{29}
\]

At $\tau=0$ this is the size-$k$ block initializer with $2B$
blocks; at $\tau=1$ it is the size-$2k$ initializer with $B$
blocks. All learned updates remain global. Let
$F_{B,k,t,x}$ be the actual finite-flow prediction as a function
of its initialized arrays, with first-layer arrays integrated as
additional independent roots.

There is an exact covariance interpolation formula on
$0<\tau<1$. It can be stated without assuming integrability of
classical initializer Hessians. Define the Gaussian weak-Hessian
entry

\[
 \mathcal J_{ij}^{(\ell)}(\tau)
 =\mathbb E_\tau\left[
   \left(\frac{(A_{ij}^{(\ell)})^2}{v_{ij}(\tau)^2}
                         -\frac1{v_{ij}(\tau)}\right)
                F_{B,k,t,x}\right].                 \tag{30}
\]

At every fixed $t$, loss dissipation gives $R(t)\le Y$, and
the readout equation gives $|F_{B,k,t,x}|\le2\kappa_{L+1}Yt$.
Thus (30) is integrable. Differentiating the finite product Gaussian
density under its integral is justified on each compact subinterval
of $0<\tau<1$, using this bound and integrable Gaussian scores.
It yields

\[
 \frac d{d\tau}\mathbb E_\tau F_{B,k,t,x}
 =\frac1{4k}\sum_{\ell=2}^L\sum_{\rm groups}\sum_{i,j}
           \sigma_{ij}\mathcal J_{ij}^{(\ell)}(\tau),
 \qquad
 \sigma_{ij}=\begin{cases}-1,&\text{same half},\\+1,&\text{different halves}.
                       \end{cases}                  \tag{31}
\]

If ordinary second derivative integrability and the necessary boundary
terms are proved separately, two scalar integrations by parts identify
$\mathcal J_{ij}=\mathbb E_\tau\partial_{A_{ij}}^2F$.
That extra identification is not silently assumed here.

There are $2Bk^2$ entries of each sign per layer. Let
$J_{\rm same}^{(\ell)}$ and $J_{\rm cross}^{(\ell)}$ denote
their respective averages. Formula (31) becomes

\[
 \frac d{d\tau}\mathbb E_\tau F_{B,k,t,x}
  =\frac{Bk}{2}\sum_{\ell=2}^L
        [J_{\rm cross}^{(\ell)}-J_{\rm same}^{(\ell)}].
                                                               \tag{32}
\]

Therefore the following would suffice, together with the indicated
limit identifications:

\[
 \left\|\sum_{\ell=2}^L
     [J_{\rm cross}^{(\ell)}-J_{\rm same}^{(\ell)}]
 \right\|_{L^2(\mu)}
       \le \frac{C_Y}{B k^{1+\beta}}                 \tag{33}
\]

uniformly in time, interpolation parameter, and $B$, with endpoint
integrability in $\tau$. Integrating (32) would give
$\sup_t\|f_{2k}-f_k\|_{L^2(\mu)}\le C_Y k^{-\beta}$ after
passing $B\to\infty$. A dyadic sum would then give a rate to the
block hierarchy's limit. Identifying that limit as the stipulated
dense flow is still necessary, although qualitative compact-time
identification would suffice once the all-time dyadic bound is known.

Uniformity in finite $B$ in (33) is a convenient sufficient formulation,
not a necessary condition for the desired population theorem. It would
also suffice to justify the integrated interpolation identity after
$B\to\infty$ at each fixed time and then prove a time-uniform contrast
bound there. This respects the prescribed order of limits and avoids
silently imposing an all-time estimate on every small finite system.

For $\beta=1$, (33) requires a same/cross Hessian contrast of order
$1/(Bk^2)$. A bound of order $1/(Bk)$ on each Hessian entry, even
if proved, gives only an order-one right side in (32). Thus merely
obtaining smooth dependence on every Gaussian entry does not produce
a weak-bias rate. One additional power of block size must come from
the **contrast**, not from norm stability.

At initialization section 2 obtains the needed cancellation by
conditional centering and a second covariance derivative. After
training, a block affects both orientations of the reused initializer,
all the global coefficient histories and the residual. A leave-one-out
proof must differentiate those global histories as well. Freezing them
while deleting a row or column is a different derivative and does not
establish (33).

The small-force estimates above control the total size and propagation
of these histories. They give no extra $1/k$ factor in their
same/cross response contrast. This is a precise missing estimate, not
a proof that the contrast cannot have that cancellation.

## 6. Why a finite small-label expansion does not remove the gap

Define the actual nonlinear remainders by

\[
 \mathcal R_j(t;y)=f_j(t;y)-f_j^{\rm lin}(t;y),
       \qquad j\in\{k,\infty\}.
\]

Section 4 proves

\[
 \|\mathcal R_j(\cdot;y)\|_{L^\infty_tL^2_\mu}\le CY^3.
\]

For the requested fixed-label theorem, what is needed is instead

\[
 \|\mathcal R_k(\cdot;y)-\mathcal R_\infty(\cdot;y)
            \|_{L^\infty_tL^2_\mu}
       \le C_Y k^{-\beta}.                           \tag{34}
\]

The first inequality says nothing quantitative about the second.
Even proving width bias $O(1/k)$ for every separately fixed Taylor
coefficient would leave the dependence on expansion order open. To
extract a fixed-$Y$ width rate one must also prove a remainder bound
uniform in $k$ at an order growing with $\log k$, and control the
growth of the coefficient-bias constants at those orders. A fixed-order
remainder $C_qY^{q+1}$ does not decay with $k$.

Real smoothness and Gaussian moments do not supply the missing
analyticity. For example,

\[
 g(z)=\mathbb E\frac1{1+z^2G^2},\qquad G\sim N(0,1),
\]

has derivatives of every order at zero: finite-order differentiation
is justified by the Gaussian moments and a real-variable polynomial
envelope on each finite derivative. Its formal even coefficients are
$(-1)^q\mathbb E G^{2q}=(-1)^q(2q-1)!!$, whose $2q$-th roots
diverge: at least $\lfloor q/2\rfloor$ factors in the product
$(2q-1)!!$ are at least $q$. The Taylor series has radius zero.
This is a diagnostic of
the inference from Gaussian moments to analyticity, not a claim that
the tanh training flow has this particular function or a divergent
label series.

## 7. Claim ledger and consequence for learned-state cost

| Claim | Status | Exact limitation |
|---|---|---|
| Initial block readout-Gram bias $O(k^{-1})$ and second-moment error $O(k^{-1})$ | Proved | Fixed $L,m$; no trained reuse in this lemma |
| Gap for all sufficiently large $k$ | Proved | Depends on the stipulated positive dense initial gap |
| Uniform small-label force, $O(Y^2)$ feature motion, exponential fitting | Proved a priori for regular flows | Does not construct the unbounded-operator block population |
| Actual nonlinear remainder $O(Y^3)$, uniform in time and $k$ | Proved a priori for those flows | Gives no width decay of the remainder difference |
| Actual first predictor derivative at zero labels has all-time bias $O(k^{-1})$ | Proved under the same regular-flow premise | A statement at zero label scale, not fixed positive labels |
| Full fixed-$Y$ trained bias $O(k^{-\beta})$, $\beta>2/3$ | Open | Requires (34), or an interpolation/response estimate such as (33) |
| Explicit sub-dense learned-state $\varepsilon$-cost for the requested surrogate | Not established by this route | The trained bias source is missing before complexity optimization |

If one uses (1) alone, a total error target below a constant multiple
of $Y^3$ cannot be certified by increasing $k$. Letting the labels
shrink with $k$ would change the fixed-label problem. Nor can the
constant $Y^3$ be absorbed into $C_Yk^{-\beta}$ for unbounded $k$.

The strongest new bounded proof result from this route is therefore
the actual uniform cubic remainder together with the explicit $1/k$
first-derivative bias. The highest-leverage unresolved lemma is the
trained same/cross Gaussian response cancellation (33), or an
equivalent direct comparison (34). Neither the desired theorem nor
its impossibility is claimed.

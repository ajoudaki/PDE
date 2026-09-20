# Rotation obstruction for the scalar population closure

Status: proved obstruction to an unconditional fitting theorem over all genuine three-point data. This is a scoped, prompt-only proof route. No other study artifacts, experiments, or external sources were used.

The strongest conclusion is an actual obstruction for the prescribed initialization, rather than a failure of a proposed coercivity estimate. For every fixed pairwise nonparallel triple of input directions and every fixed \(q\in(0,1)\setminus\{1/2\}\), at least one simultaneous rotation of the triple has a nonstationary canonical trajectory satisfying

\[
L(t)\ge \frac12\qquad\text{for every }t\ge0.
\]

Consequently, excluding the exact initial stalls does not suffice for an unconditional fitting or exponential-to-zero potential theorem. The proof does not identify the bad angle or establish that a bad angle has a positive-definite initial readout Gram matrix.

## Exact setting

Write \(v_i=x_i/\sqrt2\in S^1\). The fixed labels are \(y=(1,1,-1)\) and the weights are \(p=(q/2,(1-q)/2,1/2)\). Let \(R_\theta\) be planar rotation and let the data in the \(\theta\)-system be \(v_i^\theta=R_\theta v_i\). Every system starts from the same \(w_0(g)=g\), \(M_0>0\), and \(c_0=0\), with the same fixed Gaussian variables and probes \(b_1(g)\), \(b(Z)\) from the assignment. Define

\[
a_i^\theta=\mathbb E_1 b_1\tanh(w^\theta\cdot v_i^\theta),
\quad s_i^\theta=M^\theta a_i^\theta,
\quad f_i^\theta=\mathbb E_2 c^\theta\tanh(bs_i^\theta),
\quad d_i^\theta=\mathbb E_2 c^\theta b\operatorname{sech}^2(bs_i^\theta).
\]

The exact evolution is the assigned gradient flow, with \(r_i=f_i-y_i\) and \(L=\sum_i p_i r_i^2\):

\[
\begin{split}
\dot c&=-2\sum_i p_i r_i\tanh(bs_i),\\
\dot w&=-2b_1M\sum_i p_i r_i d_i\operatorname{sech}^2(w\cdot v_i)v_i,\\
\dot M&=-2\sum_i p_i r_i d_i a_i.
\end{split}
\]

All identities below use finite-time states only. Global finite-time existence, uniqueness, and the energy identity are part of the supplied exact model.

## Finite-time continuity in the angle

Use the Hilbert state space

\[
\mathcal H=L^2(\gamma_2;\mathbb R^2)\times\mathbb R\times L^2(\gamma_1),
\qquad X=(w,M,c).
\]

Both probes are bounded. Set \(B_1=\|b_1\|_\infty\), \(B_2=\|b\|_\infty\), and \(A=\mathbb E_1|b_1|\le B_1\). For unit \(v,\widetilde v\), the Lipschitz bound for tanh gives

\[
|a(w,v)-a(\widetilde w,\widetilde v)|
\le B_1\bigl(\|w-\widetilde w\|_2+
\|\widetilde w\|_2|v-\widetilde v|\bigr),
\qquad |a|\le A.
\]

For \(H_s(b)=\tanh(bs)\) and \(D_s(b)=b\operatorname{sech}^2(bs)\),

\[
\|H_s\|_2\le1,
\quad\|H_s-H_u\|_2\le B_2|s-u|,
\quad\|D_s\|_2\le B_2,
\quad\|D_s-D_u\|_2\le2B_2^2|s-u|.
\]

Thus \(a,s,f,d\), and the three components of the vector field, are Lipschitz on any bounded state ball, uniformly over all rotated input triples. For the \(w\)-component, use in addition

\[
\|\operatorname{sech}^2(w\cdot v)
-\operatorname{sech}^2(\widetilde w\cdot\widetilde v)\|_2
\le2\bigl(\|w-\widetilde w\|_2+
\|\widetilde w\|_2|v-\widetilde v|\bigr).
\]

The energy identity and \(L(0)=1\) imply

\[
\int_0^T\|\dot X^\theta(t)\|_{\mathcal H}^2\,dt\le1,
\qquad
\|X^\theta(t)\|_{\mathcal H}
\le\sqrt{2+M_0^2}+\sqrt T
\quad(0\le t\le T),
\]

uniformly in \(\theta\). The preceding Lipschitz estimates therefore apply on one common ball for every angle on every fixed finite horizon. Subtracting the integral equations gives, for a constant \(C_T<\infty\),

\[
\|X^\theta(t)-X^\vartheta(t)\|_{\mathcal H}
\le C_T\int_0^t\bigl(
\|X^\theta(u)-X^\vartheta(u)\|_{\mathcal H}
+\operatorname{dist}_{S^1}(\theta,\vartheta)\bigr)\,du.
\]

The elementary integral Gronwall inequality gives a bound by

\[
C_Tt e^{C_Tt}\operatorname{dist}_{S^1}(\theta,\vartheta).
\]

In particular, for each finite \(t\), the maps \(\theta\mapsto a_i^\theta(t)\) and \(\theta\mapsto L^\theta(t)\) are continuous. No all-time compactness of the state trajectory is used.

## Exact antipodal covariance

For every \(\theta\), uniqueness gives

\[
w^{\theta+\pi}=w^\theta,
\qquad M^{\theta+\pi}=M^\theta,
\qquad c^{\theta+\pi}=-c^\theta.
\]

To verify this directly, substitute the right-hand side into the system with input directions \(-v_i^\theta\). Oddness of tanh and evenness of its derivative give

\[
a_i^{\theta+\pi}=-a_i^\theta,
\quad s_i^{\theta+\pi}=-s_i^\theta,
\quad f_i^{\theta+\pi}=f_i^\theta,
\quad r_i^{\theta+\pi}=r_i^\theta,
\quad d_i^{\theta+\pi}=-d_i^\theta.
\]

The \(c\)-velocity changes sign. In the \(w\)-velocity, the two sign changes are those of \(d_i\) and \(v_i\); in the \(M\)-velocity, they are those of \(d_i\) and \(a_i\). These velocities therefore remain unchanged. The transformed state has the prescribed initial condition because \(c_0=0\). In particular,

\[
L^{\theta+\pi}(t)=L^\theta(t),
\qquad a_i^{\theta+\pi}(t)=-a_i^\theta(t).
\]

## Persistent loss floor

Fix an index \(i\) and a finite time \(T\ge0\). The continuous function \(\theta\mapsto a_i^\theta(T)\) changes sign between antipodal angles, unless it is already zero there. The intermediate value theorem supplies an angle \(\theta_T\) with

\[
a_i^{\theta_T}(T)=0.
\]

At that angle \(s_i(T)=0\), hence \(f_i(T)=\mathbb E_2 c(T)\tanh(0)=0\). Since \(y_i^2=1\),

\[
L^{\theta_T}(T)\ge p_i.
\]

For each positive integer \(n\), let

\[
E_n=\{\theta\in S^1:L^\theta(n)\ge p_i\}.
\]

Each \(E_n\) is nonempty by the preceding argument and closed by finite-time continuity. The loss is nonincreasing in time, so \(E_{n+1}\subseteq E_n\). Compactness of the angle circle now gives a common angle \(\theta_*\in\bigcap_{n\ge1}E_n\). Explicitly, choose \(\theta_n\in E_n\), extract a convergent subsequence, and use closedness of each fixed \(E_N\) together with nesting to put the limit in every \(E_N\).

For any finite \(t\ge0\), choose an integer \(n\ge\max\{1,t\}\). Then

\[
L^{\theta_*}(t)\ge L^{\theta_*}(n)\ge p_i.
\]

Taking \(i=3\) proves the advertised floor \(1/2\). More generally the same argument, with an index of largest weight, gives a persistent floor \(\max_i p_i\). The proof does not assert that the same sample remains at zero along the limiting trajectory; only the loss floor passes to the common angle.

## Why the bad trajectory is not an initial stall when \(q\ne1/2\)

The following argument also verifies the initial-stall classification supplied in the assignment. Put

\[
A_0(\rho)=\frac{
\mathbb E[\tanh G\,\tanh(\rho G+\sqrt{1-\rho^2}H)]}
{\sqrt{\nu+\eta}},
\qquad G,H\text{ independent standard Gaussians}.
\]

Then \(a_i(0)=A_0((v_i)_1)\). The function \(A_0\) is odd and strictly increasing on \([-1,1]\). For completeness, differentiation for \(-1<\rho<1\), followed by Gaussian integration by parts in \(G\) and \(H\), gives

\[
A_0'(\rho)=\frac{
\mathbb E[\operatorname{sech}^2G\,
\operatorname{sech}^2(\rho G+\sqrt{1-\rho^2}H)]}
{\sqrt{\nu+\eta}}>0.
\]

Indeed, the direct derivative contains

\[
\mathbb E\tanh G\operatorname{sech}^2(V)
\left(G-\frac{\rho H}{\sqrt{1-\rho^2}}\right),
\qquad V=\rho G+\sqrt{1-\rho^2}H.
\]

Integration by parts in the \(G\)-term gives

\[
\mathbb E\operatorname{sech}^2G\operatorname{sech}^2V
+\rho\mathbb E\tanh G\,\tanh''V,
\]

and integration by parts in the \(H\)-term cancels the second summand. Boundedness and smoothness of tanh justify these operations on every compact subinterval of \((-1,1)\); continuity extends strict monotonicity to the endpoints. Oddness follows by changing \(H\) to \(-H\).

The functions \(b\mapsto\tanh(tb)\), for finitely many distinct positive \(t\), are linearly independent in the readout space. A vanishing combination is zero on an open interval because the law of \(b\) has positive density on its support; real analyticity extends the identity to all real \(b\). If \(0<t_1<\cdots<t_m\), taking \(b\to+\infty\) first gives the sum of the coefficients equal to zero. Subtracting that constant and multiplying by \(e^{2t_1b}\) gives the first coefficient equal to zero, using

\[
\tanh(tb)-1=-2e^{-2tb}+O(e^{-4tb}).
\]

Repeating proves independence.

At initialization \(d_i=0\), so \(\dot w=\dot M=0\), whereas

\[
\dot c(0)=qH_{s_1(0)}+(1-q)H_{s_2(0)}-H_{s_3(0)}.
\]

By independence after grouping the nonzero nodes according to absolute value, a zero combination cannot have a magnitude represented by only one index. All three nonzero nodes cannot share one absolute value: strict odd monotonicity of \(A_0\) would make all three \(|(v_i)_1|\) equal, while a fixed absolute first coordinate on the unit circle gives at most two distinct unoriented lines. This contradicts pairwise nonparallelity. All three nodes cannot be zero for the same reason.

The only remaining possibility is a pair with the same nonzero absolute value and one zero node. A pair containing index 3 cannot cancel, because its coefficients have unequal absolute values \(1\) and either \(q\) or \(1-q\). The pair must therefore be indices 1 and 2, whose coefficients cancel precisely when

\[
q=\frac12,
\qquad s_1(0)=-s_2(0)\ne0,
\qquad s_3(0)=0.
\]

Equivalently,

\[
q=\frac12,
\qquad(v_1)_1=-(v_2)_1\ne0,
\qquad(v_3)_1=0.
\]

Thus for \(q\ne1/2\) every rotated system has \(\dot c(0)\ne0\), so \(\dot L(0)=-\|\dot c(0)\|_2^2<0\). The persistent-loss rotation proved above is therefore initially moving and immediately lowers its loss, yet can never lower it below \(1/2\).

## Scope and audit

- The bad angle is a single fixed angle valid for all finite times, obtained from nested closed sets. Choosing a separate adversarial angle at every time without compactness would not suffice; the proof explicitly supplies the compactness step.
- Compactness is used only for the circle of data rotations, not for the infinite-time parameter trajectory.
- The labels, weights, Gaussian probes, normalization constants, initialization, architecture, and exact gradient flow are unchanged. Rotation preserves pairwise nonparallelity.
- The obstruction applies to the canonical trajectory and persists after exact initial stalls are excluded by \(q\ne1/2\).
- The argument establishes existence, not a computable bad angle, a positive-measure bad set, or a bad angle with a positive-definite initial readout Gram. Each of those would be an additional claim requiring proof.
- A positive-definite initial readout Gram remains an additional restriction: for a fixed nonparallel triple, failure of nonzero distinct absolute initial nodes occurs at finitely many rotation angles, and the present existence argument does not prove that its bad angle avoids them.
- Any potential theorem that would force \(L(t)\to0\) for every such rotated data set is contradicted. A theorem restricted by additional data geometry or initialization conditions is not decided by this argument.

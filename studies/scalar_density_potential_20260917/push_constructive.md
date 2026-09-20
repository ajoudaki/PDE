# Canonical nonstalled trajectories with positive all-time loss

This is a scoped, prompt-only mathematical audit. Its scientific inputs are the supervisor's model, finite-horizon well-posedness/continuous-dependence premise, and proposed antipodal-data symmetry. No other study material, experiment, or external source was used. The original constructive route was superseded within this assignment by the supervisor's request to audit the rotation obstruction.

**Status:** internally proved for the supplied exact global flow; finite-time continuity is derived below from its energy identity. This disproves an all-data theorem that removes only initial stalls. It does **not** disprove the existence of a particular asymmetric three-input family that learns, and it does **not** prove that the bad rotation has a positive-definite initial feature Gram matrix.

## Statement

Let \(u_1,u_2,u_3\in S^1\) be pairwise distinct. Fix labels \((1,1,-1)\) and weights
\[
p_1=q/2,\qquad p_2=(1-q)/2,\qquad p_3=1/2,
\quad q\in(0,1)\setminus\{1/2\}.
\]
For \(\theta\in[0,2\pi]\), take inputs \(x_i(\theta)=\sqrt2 R_\theta u_i\) and run the supplied unique global canonical gradient flow from the stated fixed initialization.

Then there exists a fixed \(\theta_*\in[0,2\pi]\) such that
\[
L(t;\theta_*)\ge \frac12\qquad\text{for every }t\ge0.
\]
Every rotation has nonzero initial gradient; in particular the counterexample is not an initial stall. The same conclusion holds with \(p_i\) in place of \(1/2\) for any designated sample \(i\).

One may choose the data-only template
\[
u_1=(\cos60^\circ,\sin60^\circ),\quad
u_2=(\cos70^\circ,\sin70^\circ),\quad
u_3=(\cos230^\circ,\sin230^\circ),\qquad q=3/4.
\]
It has no duplicate or antipodal pair. It is homogeneously linearly separable: the vector at angle \(60^\circ\) has positive dot products with \(u_1,u_2\) and a negative dot product with \(u_3\). These properties survive all rotations. Thus the obstruction is present in an explicit compact family of three distinct, pairwise nonparallel, separable datasets.

The proof supplies an existential member of this entirely data-defined rotation family. It does not locate \(\theta_*\) numerically or choose training coefficients from a future fitting endpoint.

## Exact model and antipodal-data symmetry

Write \(\phi=\tanh\), \(g\sim N(0,I_2)\), \(Z\sim N(0,1)\),
\[
\nu=\mathbb E\phi(G)^2,\qquad
\tau=\mathbb E\phi(\sqrt\nu G)^2,\qquad \eta=1/4096,
\]
\[
b_1(g)=\frac{\phi(g_1)}{\sqrt{\nu+\eta}},\qquad
b(Z)=\frac{\phi(\sqrt\nu Z)}{\sqrt{\tau+\eta}},\qquad
M_0=\frac{\nu(1-\tau)}{\sqrt{(\nu+\eta)(\tau+\eta)}}>0.
\]
The initialization is \(w_0(g)=g\), \(c_0(Z)=0\). For unit input directions \(u_i=x_i/\sqrt2\), set
\[
a_i=\mathbb E_g b_1\phi(w\cdot u_i),\quad
H_i=\phi(bMa_i),\quad f_i=\mathbb E_Z cH_i,
\]
\[
d_i=\mathbb E_Z bc\phi'(bMa_i),\quad r_i=f_i-y_i,\qquad
L=\sum_i p_i r_i^2.
\]
The supplied equations are
\[
\dot w=-2\sum_i p_i r_i b_1 M d_i\phi'(w\cdot u_i)u_i,
\quad \dot c=-2\sum_i p_i r_i H_i,
\quad \dot M=-2\sum_i p_i r_i d_i a_i,
\]
with
\[
\dot L=-\|\dot w\|^2-\|\dot c\|^2-|\dot M|^2\le0.
\]

Replace all directions by their antipodes \(u_i'=-u_i\). Given a solution for the original dataset, define
\[
w'=w,\qquad c'=-c,\qquad M'=M.
\]
Oddness of \(\phi\) and evenness of \(\phi'\) give
\[
a_i'=-a_i,\quad H_i'=-H_i,\quad f_i'=f_i,\quad
r_i'=r_i,\quad d_i'=-d_i.
\]
In the \(w\) equation, the signs from \(d_i'\) and \(u_i'\) cancel. In the \(M\) equation, the signs from \(d_i'\) and \(a_i'\) cancel. The \(c\) equation changes sign. The transformed state has the same initialization because \(c_0=0\). Uniqueness therefore gives, exactly,
\[
a_i(t;\theta+\pi)=-a_i(t;\theta),\qquad
L(t;\theta+\pi)=L(t;\theta).
\]
No rotational equivariance of the fixed mark \(b_1\) is claimed or needed.

## Finite-time continuity follows from the energy bound

Use the Hilbert state space
\[
\mathcal X=L^2_g(\mathbb R^2)\times L^2_Z(\mathbb R)\times\mathbb R,
\qquad S=(w,c,M).
\]
The initial state belongs to this space. Since \(L(0)=1\), the energy identity and Cauchy--Schwarz imply, uniformly over the rotation angle,
\[
\|S(t;\theta)-S_0\|_{\mathcal X}
\le \int_0^t\|\dot S(s;\theta)\|_{\mathcal X}\,ds
\le\sqrt t.
\]
Thus all states up to time \(T\) lie in one Hilbert ball of radius \(R_T=\|S_0\|+\sqrt T\).

On every fixed such ball, the vector field \(F(S;u_1,u_2,u_3)\) is Lipschitz jointly in the state and the unit directions, with a constant depending only on the ball radius and the fixed model constants. For completeness, boundedness and Lipschitz continuity of \(\phi,\phi'\), boundedness of \(b,b_1\), and Cauchy--Schwarz give, for two states and two direction collections in the ball,
\[
|a_i-\widetilde a_i|
\le \|b_1\|_\infty\bigl(\|w-\widetilde w\|_2
+R_T|u_i-\widetilde u_i|\bigr).
\]
This bounds the differences of \(H_i\) in \(L^\infty_Z\), and therefore bounds the scalar differences of \(f_i,d_i,r_i\) by a constant times
\(\|S-\widetilde S\|_{\mathcal X}+\max_j|u_j-\widetilde u_j|\).
For the only remaining functional factor in the \(w\) equation,
\[
\|\phi'(w\cdot u_i)u_i-
\phi'(\widetilde w\cdot\widetilde u_i)\widetilde u_i\|_2
\le |u_i-\widetilde u_i|
+\|\phi''\|_\infty
\bigl(\|w-\widetilde w\|_2+R_T|u_i-\widetilde u_i|\bigr).
\]
Products with the already bounded scalar factors give the stated vector-field estimate.

Since \(|R_\theta u_i-R_\psi u_i|\le|\theta-\psi|\), integrating the difference of the two ODEs and applying the elementary integral Gronwall inequality yields
\[
\sup_{0\le t\le T}\|S(t;\theta)-S(t;\psi)\|_{\mathcal X}
\le (e^{C_TT}-1)|\theta-\psi|
\]
for a finite constant \(C_T\). This proves all the finite-time continuity used below. No bound uniform as \(T\to\infty\) is asserted or needed.

## Compactness converts moving zeros into one bad dataset

Fix a sample \(i\) and a finite time \(t\). The continuous function
\(\theta\mapsto a_i(t;\theta)\) takes opposite values at \(0\) and \(\pi\), so the intermediate value theorem provides at least one \(\theta_t\) with
\[
a_i(t;\theta_t)=0.
\]
At this angle, \(H_i=\phi(0)=0\), hence \(f_i=0\). Since \(|y_i|=1\),
\[
L(t;\theta_t)\ge p_i.
\]
For each integer \(n\ge0\), define the closed set
\[
E_n=\{\theta\in[0,2\pi]:L(n;\theta)\ge p_i\}.
\]
Every \(E_n\) is nonempty by the preceding argument. Loss monotonicity at each fixed angle gives \(E_{n+1}\subseteq E_n\). These are nested nonempty closed subsets of the compact interval \([0,2\pi]\); their intersection is nonempty. For any \(\theta_*\) in that intersection and any real \(t\ge0\), choose an integer \(n\ge t\). Then
\[
L(t;\theta_*)\ge L(n;\theta_*)\ge p_i.
\]
Taking \(i=3\) proves the stated \(1/2\) lower bound.

Equivalently, one can choose zeros at times tending to infinity and pass to a convergent subsequence of angles; finite-time continuity and loss monotonicity give the same conclusion. No convergence of the parameter trajectories, no interchange of an infinite-time state limit with an angle limit, and no sign assumption on \(M\) is used.

## Every dataset in this family is nonstalled at initialization

First establish two elementary facts.

**Strict monotonicity of the initialized scalar feature.** For a unit vector with first coordinate \(\rho\), Gaussian symmetry gives
\[
a_i(0)=A(\rho),\quad
A(\rho)=\frac{\mathbb E[\phi(G_1)\phi(\rho G_1+\sqrt{1-\rho^2}G_2)]}
{\sqrt{\nu+\eta}}.
\]
The function \(A\) is continuous and odd. For \(-1<\rho<1\), put \(V=\rho G_1+\sqrt{1-\rho^2}G_2\). Differentiation under the Gaussian expectation, justified locally in \(\rho\) by bounded derivatives and integrable Gaussian factors, followed by integration by parts gives
\[
\begin{aligned}
\sqrt{\nu+\eta}\,A'(\rho)
&=\mathbb E\!\left[\phi(G_1)\phi'(V)
\left(G_1-\frac{\rho}{\sqrt{1-\rho^2}}G_2\right)\right]\\
&=\mathbb E[\phi'(G_1)\phi'(V)]>0.
\end{aligned}
\]
The terms containing \(\phi''(V)\) cancel. Endpoint continuity makes \(A\) strictly increasing on \([-1,1]\) as well. In particular, \(A(\rho)=0\) iff \(\rho=0\), and \(A(\rho)=A(\rho')\) iff \(\rho=\rho'\).

**Independence of distinct positive tanh scales.** If \(0<z_1<\cdots<z_k\), then \(b\mapsto\tanh(z_jb)\) are linearly independent under the law of \(b\). Indeed, that law has a density positive throughout a nonempty interval around zero. An almost-sure linear relation is therefore a continuous identity on that interval, and real analyticity extends it to all real \(b\). Letting \(b\to+\infty\) first gives \(\sum_j\lambda_j=0\). After subtracting this constant limit, multiplying by \(e^{2z_1b}\), and using
\[
\tanh(zb)-1=-\frac{2}{e^{2zb}+1},
\]
the limit gives \(-2\lambda_1=0\). Repetition eliminates every coefficient.

At initialization \(c=0\), so \(d_i=0\), \(\dot w=0\), and \(\dot M=0\), while
\[
\dot c(0)=2\left[p_1\tanh(bM_0a_1(0))
+p_2\tanh(bM_0a_2(0))
-p_3\tanh(bM_0a_3(0))\right].
\]
Suppose this were zero in \(L^2\). Independence of distinct positive scales means that the signed coefficients must cancel separately in each group having common nonzero \(|a_i(0)|\). There are only three samples, so every possible grouping can be checked:

1. If exactly one \(a_i(0)\) is nonzero, its coefficient cannot cancel.
2. If exactly two are nonzero, they must have equal magnitude and equal weights to cancel. The only equality of two weights allowed by \(0<q<1\) is \(p_1=p_2\), which requires \(q=1/2\), excluded here.
3. If all three are nonzero, each occupied group must have at least two members, so all three must have a common magnitude. Cancellation would require
   \[
   p_1\operatorname{sgn}(a_1)+p_2\operatorname{sgn}(a_2)
   -p_3\operatorname{sgn}(a_3)=0.
   \]
   Because \(p_3=p_1+p_2\) and \(p_1,p_2>0\), equality forces all three signs to agree. Thus all three \(a_i(0)\) are equal. Strict monotonicity of \(A\) forces equal first coordinates of all three unit directions. A line of fixed first coordinate intersects the unit circle in at most two points, contradicting distinctness.
4. If all three \(a_i(0)\) vanish, all three unit directions have first coordinate zero, again impossible for three distinct circle points.

Therefore \(\dot c(0)\ne0\) for every rotation, and
\[
\dot L(0)=-\|\dot c(0)\|^2<0.
\]
The bad trajectory initially learns in the strict loss-decrease sense, yet its loss can never drop below \(1/2\).

## Scope and hostile audit

- The result concerns the exact canonically initialized flow, not an arbitrary inaccessible state.
- All three sample weights are strictly positive. The explicit template has no duplicate or antipodal pair and remains separable under every rotation.
- Finite-time continuity follows directly from the supplied energy identity and local Lipschitz estimates above. The proof does not infer all-time continuity from a finite-time bound.
- No stationary-point classification at positive time, bounded trajectory, limiting kernel, compactness of parameter space, or external convergence theorem is used. Compactness is only of the one-dimensional data-angle interval.
- The lower bound is \(1/2\), not merely \(p_{\min}\). It is obtained by selecting the negative sample in the moving-zero argument.
- The argument does not identify an explicit numerical bad angle. For refuting a universal claim, existence in the fixed explicit family suffices.
- Genuine geometric distinctness does not automatically imply a positive-definite feature Gram at the canonical initialization: it can fail when some initialized \(a_i\) is zero or two have equal absolute values. The proof does not exclude the bad angle from that finite exceptional set.
- Consequently the result refutes “every genuine three-input dataset learns once initial stalls are excluded.” It leaves open an existential constructive family, or a theorem restricted to a quantitatively stronger initial nondegeneracy class.
- An all-time nonnegative state potential that dominates the loss and tends exponentially to zero cannot exist on every one of these nonstalled datasets. A potential decaying toward a positive residual floor is not ruled out.

The original pair-splitting question therefore remains a possible existential route, but it cannot be used to assert a universal nonstalled-data result.

## Additional audit: finite representability for the equilateral family

This subsection answers a subsequent scoped supervisor request. Fix
\[
v_i(\theta)=R_\theta
\left(\cos\frac{2\pi(i-1)}3,\sin\frac{2\pi(i-1)}3\right),
\quad i=1,2,3,
\]
with labels \((1,1,-1)\) and weights \((3/8,1/8,1/2)\). The three directions are pairwise nonparallel at every angle. For each fixed angle, there is a finite zero-loss state with the canonical frozen marks, \(M=M_0\), and an arbitrarily small bounded perturbation of \(w=g\). Thus the positive-loss trajectory established above does not arise from failure of finite representability.

To prove this, suppress \(\theta\) and define bounded vector-valued functions
\[
h_j(g)=b_1(g)\phi'(g\cdot v_j)v_j,\qquad j=1,2,3.
\]
Their Hilbert Gram matrix is
\[
K_{ij}=\mathbb E_g[h_i(g)\cdot h_j(g)]
=\mathbb E_g\!\left[b_1(g)^2
\phi'(g\cdot v_i)\phi'(g\cdot v_j)\,v_i\cdot v_j\right].
\]
We first prove \(K\) is positive definite. If \(\beta^T K\beta=0\), the nonnegative square norm in its expectation vanishes almost surely, so
\[
\sum_{j=1}^3\beta_j b_1(g)\phi'(g\cdot v_j)v_j=0
\quad\text{for Gaussian-almost every }g.
\]
The zero set of \(b_1\) is the measure-zero line \(g_1=0\). Division off this line, continuity, and the Gaussian law's full support imply
\[
\sum_{j=1}^3\beta_j\phi'(g\cdot v_j)v_j=0
\quad\text{for every }g\in\mathbb R^2.
\]
For a fixed \(k\), choose a unit \(z_k\perp v_k\) and put \(g=t z_k\). Pairwise nonparallelness ensures \(z_k\cdot v_j\ne0\) for \(j\ne k\). Since \(\phi'(0)=1\) and \(\phi'(s)=\operatorname{sech}^2(s)\to0\) as \(|s|\to\infty\), letting \(t\to+\infty\) yields \(\beta_k v_k=0\). Thus \(\beta_k=0\), and doing this for each \(k\) proves positive definiteness. The extension to every \(g\) precedes this ray argument, so no issue arises if one of the chosen rays lies on \(b_1=0\).

Now restrict the lower state to the finite-parameter family
\[
w_z(g)=g+\sum_{j=1}^3 z_j h_j(g),\qquad z\in\mathbb R^3,
\]
and define the feature map
\[
\mathcal A(z)_i=\mathbb E_g b_1(g)\phi(w_z(g)\cdot v_i).
\]
The map \(\mathcal A:\mathbb R^3\to\mathbb R^3\) is continuously differentiable: boundedness of \(h_j,b_1,\phi',\phi''\) justifies differentiation under the expectation and continuity of the derivative. Its derivative at zero is exactly
\[
\frac{\partial\mathcal A_i}{\partial z_j}(0)
=\mathbb E_g b_1\phi'(g\cdot v_i)(h_j\cdot v_i)
=K_{ij}.
\]
The finite-dimensional inverse function theorem used here says that a continuously differentiable map between open subsets of \(\mathbb R^3\), with invertible derivative at a point, maps some neighborhood of that point diffeomorphically onto a neighborhood of its image. All its hypotheses hold by the preceding derivative calculation and positive definiteness. Hence the image of every sufficiently small neighborhood of \(z=0\) contains a neighborhood of \(a(0)\).

The finite union of hyperplanes
\[
\bigcup_i\{a_i=0\}
\;\cup\!\bigcup_{i<j}\{a_i=a_j\}
\;\cup\!\bigcup_{i<j}\{a_i=-a_j\}
\]
has empty interior. Choose an image point outside this union and its preimage \(z\) in the small inverse-function neighborhood. Then the resulting three scalar features are nonzero and have pairwise distinct absolute values. The perturbation can be made arbitrarily small, with the explicit bound
\[
\|w_z-g\|_{L^\infty_g}
\le\|b_1\|_\infty\sum_j|z_j|.
\]

Keep \(M=M_0>0\), and define
\[
H_i(b)=\tanh(bM_0\mathcal A(z)_i),\qquad
G_{ij}=\mathbb E_Z H_iH_j.
\]
The distinct-positive-scale independence proved earlier, after extracting the signs of the nonzero \(\mathcal A(z)_i\), shows that the three \(H_i\) are linearly independent in \(L^2_Z\). Therefore \(G\) is positive definite. With \(y=(1,1,-1)^T\), set
\[
\gamma=G^{-1}y,\qquad c(b)=\sum_{j=1}^3\gamma_jH_j(b).
\]
Then
\[
f_i=\mathbb E_Z cH_i=(G\gamma)_i=y_i,
\qquad L=0.
\]
All coefficients are finite, and \(\|c\|_\infty\le\sum_j|\gamma_j|<\infty\). The marks \(b_1,b\), their laws, and \(M_0\) were never changed. Moreover, \(h_j(-g)=-h_j(g)\), so \(w_z\) has the same odd parity as initialization; \(c\) is odd in \(b\); and \(w_z(g)=g\) on \(b_1(g)=0\). The construction respects these immediate canonical symmetries.

This is a representability result. It does not assert that the canonical gradient trajectory reaches the constructed state. As the lower perturbation is reduced, \(G^{-1}\) and \(\|c\|\) may become large; no bound uniform in perturbation size is claimed or required for finite representability.

## Additional audit: uniform strict initial progress

For the equilateral family, define
\[
J(\theta)=\|\dot c(0;\theta)\|_{L^2_Z}^2.
\]
The previous nonstall proof applies because the directions are distinct and \(q=3/4\ne1/2\). Thus \(J(\theta)>0\) for every angle. The initialized features \(A((v_i(\theta))_1)\) are continuous in \(\theta\), and the bounded Lipschitz function \(\tanh\) makes \(\dot c(0;\theta)\) continuous in \(L^2_Z\). Consequently \(J\) is continuous on the compact angle circle and
\[
J_*:=\min_{\theta\in[0,2\pi]}J(\theta)>0.
\]
Since \(\dot w(0)=0\) and \(\dot M(0)=0\),
\[
\dot L(0;\theta)=-J(\theta)\le-J_*
\qquad\text{for every }\theta.
\]
This also gives a uniform short-time loss decrease. To verify that extension explicitly, use the state bound \(\|S(t;\theta)-S_0\|\le\sqrt t\) and a vector-field Lipschitz constant \(C\) on the common state ball for \(0\le t\le1\). Then
\[
\|\dot S(t;\theta)-\dot S(0;\theta)\|\le C\sqrt t.
\]
Choose \(t_0\in(0,1]\) so that
\(C\sqrt{t_0}\le(1-1/\sqrt2)\sqrt{J_*}\). If \(C=0\), any \(t_0\le1\) works. For every angle and \(0\le t\le t_0\),
\[
\|\dot S(t;\theta)\|\ge\sqrt{J_*}-C\sqrt t
\ge\sqrt{J_*/2}.
\]
Integrating the energy identity gives
\[
L(t;\theta)\le1-\frac{J_*}{2}t
\qquad(0\le t\le t_0).
\]
In particular every rotation makes a common positive amount of progress by time \(t_0\), while at least one fixed rotation still satisfies \(L(t)\ge1/2\) for all time. The obstruction cannot be dismissed as a sequence of rotations approaching an initial stall: this entire fixed family has a strictly positive uniform initial gradient margin.

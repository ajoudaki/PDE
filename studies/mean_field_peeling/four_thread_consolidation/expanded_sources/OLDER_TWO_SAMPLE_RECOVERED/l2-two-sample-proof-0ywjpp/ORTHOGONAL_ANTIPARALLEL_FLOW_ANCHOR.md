# Deterministic L2 common-action flow at orthogonal and antiparallel inputs

Date: 2026-09-06.

Scope: a deterministic, all-finite-physical-time L=2 flow and discretization
lemma for rho=0 and rho=-1. This is a mathematical construction, not a
review, an arbitrary-angle result, a population-limit identification, or a
full mean-field theorem. No experiments or agents were used.

The only project source read was
`/tmp/l2-two-sample-proof-0ywjpp/CONTRACT_AND_SEARCH.md`.
Its initial source-snapshot SHA-256 was
`b4a9f991c1949ae195a37d4244c644c9ea231bd7e960ebfd045d6139abff82f7`.
The contract was updated concurrently and reread before completion; that
source snapshot had SHA-256
`74efa193f00cc6c21d53940b98b1de2b05ffdfc56c3673412262c0d4c8e7e5df`.
The update added research-progress information and explicitly confirmed
this sidecar's scope; it did not change the relevant equations. No files
referenced by the contract were read.
The final section specifies a reproducible proof-content hash.

## 1. Statement and architecture

Choose, once and for all in both layers and both geometries,

\[
 \phi_1(z)=\phi_2(z)=\arctan z,
 \qquad \phi_\ell'(z)=D(z):=(1+z^2)^{-1}\quad(\ell=1,2).
\]

These are fixed, bounded, genuinely nonlinear scalar activations. No
linearization of either activation is used. Write

\[
 B=\pi/2,\qquad F(z)=z+z^3/3,\qquad g=F^{-1}.
\]

Then F is a bijection of R,

\[
 g'(u)=D(g(u)),\qquad
 |g(u)-g(v)|\leq |u-v|,\qquad
 |\phi_1(g(u))-\phi_1(g(v))|\leq |u-v|.
\tag{1.1}
\]

Also \(|\phi_\ell|\leq B\), \(0<D\leq1\), and
\(|D'|=2|z|/(1+z^2)^2\leq1\).

**Lemma.** On two separate probability spaces, fix an actual bounded
operator from the first L2 population to the second, a fixed Gaussian
first-layer pair of the specified geometry, and initial readout zero.
The equations below define a unique autonomous physical gradient flow
on [0,infinity), with uniqueness at every reached restart. The same assertion holds
on the finite normalized spaces, for each actual finite initialization,
including its nonzero random readout. More generally, the deterministic
lemma allows any bounded initial readout. All bounds and stability
constants use ordinary L2 norms, a true operator norm, and optionally a
Hilbert--Schmidt norm for operator increments; they are independent of
width. The transformed equations have width-independent Euler consistency
and stability. At finite width, exact raw GD with eta=n^-2 has accumulated
cubic-coordinate defect O_T(n^-3/2) under the explicit primal bounds in
Section 8. Those bounds can themselves be obtained by an elementary
bootstrap on the stated high-probability initialization event.

Here “common-action flow” has a precise meaning: prescribed scalar
controls drive the same deterministic equations on each population
realization, and solutions are L2 stable under a common control or an L1
perturbation of the controls. Orthogonal inputs require two controls.
Antiparallel inputs reduce to one control. No scalar common clock is
asserted for the orthogonal problem.

The proof removes the first-layer multiplier by F, proves L2 stability on
bounded-readout sets, bounds readout and operator by accumulated control,
and then uses the exact loss dissipation identity to control that action
on each physical horizon. Finally, the cubic identity for F measures the
difference between raw GD and Euler in the transformed coordinates.

The existence of a bounded population operator with the *canonical joint
initialization and reuse laws* is not an output of this lemma. Whenever
the population statement is used, such an operator is part of its input.
Section 10 lists the remaining bridges.

## 2. Spaces, normalization, and the fixed initial state

Let \(H_1=L^2(\Omega_1,\mu_1)\) and
\(H_2=L^2(\Omega_2,\mu_2)\), with probability measures. The two populations
remain distinct. Let

\[
 A=W^{(2)}:H_1\longrightarrow H_2,\qquad b=W^{(3)}\in H_2.
\]

The population adjoint is \(W^{(2)*}=A^*\). For
\(v\in H_2,w\in H_1\), define

\[
 (v\otimes w)e=v\langle w,e\rangle_{H_1}.
\]

This is an actual rank-one operator, with

\[
 \|v\otimes w\|_{\rm op}
 =\|v\otimes w\|_{\rm HS}=\|v\|_2\|w\|_2.
\tag{2.1}
\]

In particular, \(A^*\) is not replaced by a separately sampled operator.
There is no assertion of iid coordinates after operator reuse and no
extension of A to arbitrary Lp spaces.

For a finite width n, use separate copies
\(H_{1,n}=H_{2,n}=(\mathbb R^n,\langle v,w\rangle_n=v^T w/n)\).
The finite operator A acts by the raw matrix \(W^{(2)}\), not by an
additional normalization of that matrix. Its adjoint is exactly the
finite transpose \(W^{(2)T}\). In these spaces

\[
 v\otimes w=vw^T/n,\qquad
 \|A\|_{\rm op}=\|W^{(2)}\|_{\ell^2\to\ell^2},\qquad
 \|A\|_{\rm HS}=\|W^{(2)}\|_F.
\tag{2.2}
\]

At population initialization fix random variables on \(\Omega_1\), once:

* rho=0: \((G_1,G_2)\) are jointly standard Gaussian with covariance zero,
  hence independent; they are the two sample fields on the *same* first
  neuron population.
* rho=-1: \((G_1,G_2)=(G,-G)\), with G standard Gaussian.

Set \(z^{(1)}_a(0)=G_a\), fix any specified bounded
\(A_0:H_1\to H_2\), and set \(b_0=0\). Neither G nor A0 is redrawn at a
restart. A Gaussian G satisfies
\(\mathbb E F(G)^2=1+2+15/9=14/3\), so the initial cubic coordinate is in
ordinary L2. The proof actually permits any initial cubic coordinates in
H1 and any \(b_0\in L^\infty(\Omega_2)\).

At finite width use exactly the contract initialization:

\[
 W^{(1)}_{ij}(0)\sim N(0,1/d),\quad
 W^{(2)}_{ij}(0)\sim N(0,1/n),\quad
 W^{(3)}_i(0)\sim N(0,n^{-2}),
\]

independently. Fix the resulting first pair
\(G_{a,n}=W^{(1)}(0)x_a\) and the actual finite b0. Its first-neuron pairs
have the Gaussian laws above. The finite readout is never reset to zero.

Use either of the Banach state spaces

\[
 \mathcal E_p=H_1^m\times\mathcal I_p(H_1,H_2)\times H_2,
 \qquad
 \|(\Delta u,\Delta A,\Delta b)\|_{\mathcal E_p}
 =\sum_{a=1}^m\|\Delta u_a\|_2
   +\|\Delta A\|_p+\|\Delta b\|_2,
\tag{2.3}
\]

where \(\mathcal I_{\rm op}\) is the space of bounded operators and
\(\mathcal I_{\rm HS}\) is the Hilbert--Schmidt class. In the latter case
the operator coordinate is the increment \(A-A_0\). A0 itself need not be
Hilbert--Schmidt. We use m=2 for rho=0 and m=1 for rho=-1.

## 3. The orthogonal equations and exact raw metric

For rho=0 define, for a=1,2,

\[
\begin{aligned}
 u_a&=F(z^{(1)}_a),& z^{(1)}_a&=g(u_a),&
 h^{(1)}_a&=\phi_1(z^{(1)}_a),\\
 z^{(2)}_a&=A h^{(1)}_a,&
 h^{(2)}_a&=\phi_2(z^{(2)}_a),&
 f_a&=\langle b,h^{(2)}_a\rangle_{H_2},\\
 r_a&=f_a-y_a,& (y_1,y_2)&=(1,-1),\\
 \delta^{(2)}_a&=b\phi_2'(z^{(2)}_a),&
 q^{(1)}_a&=A^*\delta^{(2)}_a,&
 \delta^{(1)}_a&=\phi_1'(z^{(1)}_a)q^{(1)}_a.
\end{aligned}
\tag{3.1}
\]

For finite matrices the expression for q is
\(q^{(1)}_a=W^{(2)T}\delta^{(2)}_a\). Products of fields in (3.1) are
pointwise. The residual is not included in either delta.

For prescribed real controls \(c_1,c_2\in L^1_{\rm loc}\), the controlled
flow is

\[
 \dot u_a=c_a q^{(1)}_a,\qquad
 \dot A=\sum_{a=1}^2c_a\delta^{(2)}_a\otimes h^{(1)}_a,\qquad
 \dot b=\sum_{a=1}^2c_a h^{(2)}_a.
\tag{3.2}
\]

The physical autonomous flow uses \(c_a=-2r_a\), without a time rescaling.
Indeed, the contract gives

\[
 \dot z^{(1)}_a=-2\sum_b r_b C_{ab}\delta^{(1)}_b,
 \qquad C_{ab}=x_a^T x_b/d.
\]

For C=I this is \(\dot z^{(1)}_a=-2r_a D(z^{(1)}_a)q^{(1)}_a\), and
\(F'(z)D(z)=1\) gives (3.2) component by component. Equations (2.2) give
the precise finite raw A and b updates and velocities in the contract.

The original finite first matrix is recovered, without changing its
unobserved component, by

\[
 W^{(1)}(t)=W^{(1)}(0)
 +\sum_{a=1}^2
   [z^{(1)}_a(t)-G_{a,n}]x_a^T/d.
\tag{3.3}
\]

Since \(x_a^T x_b/d=\delta_{ab}\), its increments and velocities satisfy

\[
 \frac d n\|\Delta W^{(1)}\|_F^2
 =\sum_{a=1}^2\|\Delta z^{(1)}_a\|_n^2.
\tag{3.4}
\]

Thus this is the contract's raw physical gradient flow, including the
normalization of its first-layer metric.

## 4. The antiparallel equations: both labels, raw factor four

If rho=-1, equality in Cauchy--Schwarz gives \(x_2=-x_1\). For every raw
parameter state, not merely in distribution or at initialization,

\[
 z^{(1)}_2=-z^{(1)}_1,\quad h^{(1)}_2=-h^{(1)}_1,\quad
 z^{(2)}_2=-z^{(2)}_1,\quad h^{(2)}_2=-h^{(2)}_1,\quad f_2=-f_1.
\tag{4.1}
\]

The first equality comes from the inputs; the others use the oddness of
both actual activations and linearity of A and the readout. There is no
restriction or symmetry imposed on b. Since both derivatives D are even,

\[
 \delta^{(2)}_2=\delta^{(2)}_1,\quad
 q^{(1)}_2=q^{(1)}_1,\quad
 \delta^{(1)}_2=\delta^{(1)}_1.
\tag{4.2}
\]

Suppress only the sample index 1 in the following reduced definitions:
\(u=F(z^{(1)}_1)\), \(h=h^{(1)}_1\), \(k=h^{(2)}_1\),
\(\delta=\delta^{(2)}_1\), \(q=q^{(1)}_1\), \(f=f_1\), and \(r=f-1\).
Layer indices in (3.1) still define all these quantities. Both labels give

\[
 (r_1,r_2)=(r,-r),\qquad L=r_1^2+r_2^2=2r^2.
\tag{4.3}
\]

For general per-sample controls the effective control is
\(c=c_1-c_2\). The reduced controlled system is

\[
 \dot u=cq,\qquad \dot A=c\delta\otimes h,\qquad \dot b=ck.
\tag{4.4}
\]

In physical time \(c_1=-2r,c_2=2r\), and therefore

\[
 \dot u=-4rq,\qquad \dot A=-4r\delta\otimes h,\qquad
 \dot b=-4rk.
\tag{4.5}
\]

For example, the first sample's original derivative is
\(-2[r\delta^{(1)}_1+(-1)(-r)\delta^{(1)}_2]
=-4r\delta^{(1)}_1\). Thus the factor four is forced by loss SUM and the
raw clock. The finite raw GD step is exactly (4.5) times eta in the raw
variables, followed by recomputation of hidden fields.

Here (3.3) has just its a=1 summand and (3.4) just one squared field norm.
One does not count the same first-matrix motion twice merely because
there are two opposite sample fields.

The finite and population kernel blocks are, respectively with finite
normalized inner products and population inner products,

\[
\begin{aligned}
 K^{(1)}_{ab}&=C_{ab}\langle\delta^{(1)}_a,\delta^{(1)}_b\rangle_{H_1},\\
 K^{(2)}_{ab}&=\langle\delta^{(2)}_a,\delta^{(2)}_b\rangle_{H_2}
                 \langle h^{(1)}_a,h^{(1)}_b\rangle_{H_1},\\
 K^{(3)}_{ab}&=\langle h^{(2)}_a,h^{(2)}_b\rangle_{H_2}.
\end{aligned}
\tag{4.6}
\]

In the antiparallel geometry every block has the form

\[
 K^{(\ell)}=\kappa_\ell
   \begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad
 (\kappa_1,\kappa_2,\kappa_3)
 =\big(\|D(z^{(1)}_1)q\|_2^2,
        \|\delta\|_2^2\|h\|_2^2,\|k\|_2^2\big).
\tag{4.7}
\]

Consequently, for \(\kappa=\kappa_1+\kappa_2+\kappa_3\),

\[
 \dot r=-4\kappa r,\qquad
 r(t)=r(0)\exp\left(-4\int_0^t\kappa(v)\,dv\right).
\tag{4.8}
\]

At population zero readout, r(0)=-1. The scalar action
\(s(t)=\int_0^t-4r(v)\,dv\) is strictly increasing on each finite physical
horizon. In this case (4.4) in action time reads
\(du/ds=q,dA/ds=\delta\otimes h,db/ds=k\), while the physical clock still
satisfies \(ds/dt=-4r\). For general finite b0, r(0) can have either sign
or be zero; use the signed control (4.4) and its total variation. No
finite-readout symmetry or initial prediction sign is needed.

## 5. L2 Lipschitz bounds, local construction, and common-action stability

All norms in this section are ordinary normalized L2 norms, unless marked
otherwise. Fix two states with
\(\|A\|_{\rm op},\|\widetilde A\|_{\rm op}\leq a\) and
\(\|b\|_\infty,\|\widetilde b\|_\infty\leq M\). Put
\(x_a=\|u_a-\widetilde u_a\|_2\),
\(e=\|A-\widetilde A\|_p\), and \(v=\|b-\widetilde b\|_2\).
Here p can be op or HS, and \(\|A-\widetilde A\|_{\rm op}\leq e\).
Equations (1.1), the boundedness of h, and (2.1) give

\[
\begin{aligned}
 \|z^{(1)}_a-\widetilde z^{(1)}_a\|_2,
 \|h^{(1)}_a-\widetilde h^{(1)}_a\|_2&\leq x_a,\\
 \|z^{(2)}_a-\widetilde z^{(2)}_a\|_2,
 \|h^{(2)}_a-\widetilde h^{(2)}_a\|_2&\leq ax_a+Be,\\
 \|\delta^{(2)}_a-\widetilde\delta^{(2)}_a\|_2
 &\leq v+M(ax_a+Be),\\
 \|q^{(1)}_a-\widetilde q^{(1)}_a\|_2
 &\leq av+Ma^2x_a+M(aB+1)e,\\
 \|\delta^{(2)}_a\otimes h^{(1)}_a
       -\widetilde\delta^{(2)}_a\otimes\widetilde h^{(1)}_a\|_p
 &\leq Bv+M(Ba+1)x_a+MB^2 e,\\
 |f_a-\widetilde f_a|&\leq Bv+M(ax_a+Be).
\end{aligned}
\tag{5.1}
\]

For instance the delta estimate splits its difference into
\((b-\widetilde b)D(z^{(2)}_a)
+\widetilde b[D(z^{(2)}_a)-D(\widetilde z^{(2)}_a)]\).
This is exactly where a bounded readout is needed. No L-infinity norm of
a *difference* is used. No bounded multiplier property is assumed for q.

Let V_a be the vector field consisting of q in u-coordinate a,
\(\delta^{(2)}_a\otimes h^{(1)}_a\) in the operator coordinate, and
\(h^{(2)}_a\) in the readout coordinate. In the reduced antiparallel case
write V. One convenient explicit set of constants is

\[
\begin{aligned}
 L_0(a,M)&=(a+B)+[Ma^2+M(Ba+1)+a]
                       +[M(aB+1)+MB^2+B],\\
 V_0(a,M)&=(a+B)M+B,\\
 L_f(a,M)&=B+Ma+MB.
\end{aligned}
\tag{5.2}
\]

Then each V_a is L0-Lipschitz in (2.3), has norm at most V0, and each
prediction is Lf-Lipschitz. The physical field is locally Lipschitz on
these bounded-readout sets, with constant

\[
 L_{\rm phys}=4[(BM+1)L_0+V_0L_f]
\tag{5.3}
\]

in *both* geometries. For rho=0 this follows by summing two terms
\(-2r_aV_a\); for rho=-1 there is one term \(-4rV\). The elementary bound
\(|r_a|\leq BM+1\) is sufficient here. The constants do not involve
\(\|u\|_2\), initial first-layer maxima, dimension, or width.

There is a minor functional-analytic issue: a ball in L-infinity is not
an open subset of L2. The following construction resolves it. Replace b
by its pointwise truncation \(P_M b=\max(-M,\min(M,b))\) in f and delta
when defining the vector field, keeping b itself as the L2 state
coordinate. The truncation is 1-Lipschitz in L2 and bounded by M, so
(5.1) proves local Lipschitz continuity of this modified field on the
whole Banach space (2.3). On a sufficiently small closed ball about the
initial state the field is bounded and Lipschitz. The integral map on
continuous paths in that ball maps the ball into itself when time times
the drift bound is smaller than the radius, and is a contraction when
time times the Lipschitz constant is less than one. Its iterates converge
geometrically in the complete path space; the limit solves the integral
equation. The same contraction inequality proves uniqueness there.
For prescribed L1 controls replace time in these two conditions by
\(\int\sum_a|c_a|\); their absolute continuity gives short suitable
intervals. This constructs an absolutely continuous controlled solution,
and a C1 solution for the continuous autonomous physical field.

The integral readout equation gives a bounded representative satisfying

\[
 \|b(t)-b(0)\|_\infty
 \leq B\int_0^t\sum_a|c_a(v)|\,dv.
\tag{5.4}
\]

For the truncated physical field one can first use
\(|r_a|\leq BM+1\) to get the same short-time conclusion. Choosing
\(M>\|b(0)\|_\infty\) and shortening the interval makes the truncation
inactive. This proves local existence for the original system. Every
L2 solution of its integral equation with bounded initial readout has
the representative (5.4), so this uniqueness does not silently exclude
another locally admissible solution by imposing an extraneous topology.

For two controlled solutions in the above bounds, subtraction and (5.1)
give, with \(E(t)\) their distance (2.3),

\[
 E(t)\leq E(0)+L_0\int_0^t\sum_a|c_a(v)|E(v)\,dv
       +V_0\int_0^t\sum_a|c_a(v)-\widetilde c_a(v)|\,dv.
\]

Multiplying the corresponding scalar integral majorant by
\(\exp[-L_0\int_0^t\sum_a|c_a|]\) yields

\[
 E(t)\leq e^{L_0S(t)}
 \left(E(0)+V_0\int_0^t\sum_a|c_a-\widetilde c_a|\right),
 \qquad S(t)=\int_0^t\sum_a|c_a|.
\tag{5.5}
\]

For the antiparallel reduction S means \(\int|c|\). This is the promised
common-action stability. Physical solutions also satisfy the direct
estimate \(E(t)\leq e^{L_{\rm phys}t}E(0)\) whenever both remain within
the displayed bounds. These comparisons are between states on identified
spaces. They do not assert an identification of different widths with a
population space.

## 6. Global action bounds, loss dissipation, and autonomous restart

Write \(a_0=\|A_0\|_{\rm op}\), \(b_2=\|b_0\|_2\), and
\(b_\infty=\|b_0\|_\infty\). For either controlled geometry,
\(\|\delta^{(2)}_a\|_2\leq\|b\|_2\), so (5.4) and (2.1) imply

\[
\begin{aligned}
 \|b(t)\|_\infty&\leq b_\infty+BS(t),&
 \|b(t)\|_2&\leq b_2+BS(t),\\
 \|A(t)-A_0\|_p&\leq Bb_2S(t)+\tfrac12 B^2S(t)^2,&
 \|A(t)\|_{\rm op}&\leq a_0+Bb_2S(t)+\tfrac12 B^2S(t)^2.
\end{aligned}
\tag{6.1}
\]

For p=HS the operator increment bound follows by integrating the
rank-one HS derivative; it holds even when A0 is only bounded. An
operator-norm construction therefore has HS increments as well. Further,

\[
\begin{aligned}
 \sum_{a=1}^m\|u_a(t)-u_a(0)\|_2
 &\leq P(S(t)),\\
 P(S)&=a_0b_2 S+\tfrac12(a_0B+Bb_2^2)S^2
             +\tfrac12B^2b_2S^3+\tfrac18B^3S^4.
\end{aligned}
\tag{6.2}
\]

To check the coefficients, integrate
\((a_0+Bb_2v+B^2v^2/2)(b_2+Bv)\) from 0 to S. The increment of
\(z^{(1)}\) is bounded by the same expression by (1.1), and
\(\|z^{(2)}_a\|_2\leq B\|A\|_{\rm op}\).

Thus every prescribed control of finite total variation on compact time
intervals gives a global controlled solution. To spell out the extension
argument, on a finite putative maximal interval (6.1)--(6.2) bound all
state coordinates and the Lipschitz constants. The state derivative is
bounded by a fixed constant times \(\sum|c_a|\), so the state has a limit
in the complete space (2.3) at the endpoint. The readout is Cauchy in
L-infinity by (5.4), so the limit is still bounded. The local construction
at this limit extends the solution and contradicts finite maximality.

For the physical feedback, loss controls S. First justify differentiation
without assuming a false Frechet differentiability statement for a
nonlinear Nemytskii map from L2 to L2. If v(t) is C1 in L2 and a scalar
map psi is C1 with bounded derivative, then

\[
 \frac d{dt}\psi(v(t))=\psi'(v(t))\dot v(t)\quad\hbox{in L2}.
\tag{6.3}
\]

Indeed, replace \(v(t+h)\) by \(v(t)+h\dot v(t)\); the Lipschitz bound
makes the resulting difference quotient error tend to zero. For the
fixed direction \(\dot v(t)\), the scalar difference quotients converge
pointwise and are bounded by a constant times \(|\dot v(t)|\). Dominated
convergence for their squares gives (6.3). Products with an actual
bounded operator and differentiation of a Hilbert inner product then
justify the layerwise calculation. This applies to g and both arctans.

Differentiating f through its three parameter groups gives exactly

\[
 \dot f_a=-2\sum_b
 (K^{(1)}_{ab}+K^{(2)}_{ab}+K^{(3)}_{ab})r_b.
\tag{6.4}
\]

For clarity, the readout contribution is
\(-2\sum_b r_b\langle h^{(2)}_a,h^{(2)}_b\rangle\); the A contribution
is \(-2\sum_b r_b\langle\delta^{(2)}_a,\delta^{(2)}_b\rangle
\langle h^{(1)}_a,h^{(1)}_b\rangle\); and the first-layer contribution is
\(-2\sum_b r_bC_{ab}\langle\delta^{(1)}_a,\delta^{(1)}_b\rangle\).
The last expression follows by moving A through its actual adjoint.

Each block is positive semidefinite: the first is the Gram matrix of
\((x_a/\sqrt d)\otimes\delta^{(1)}_a\) in the finite case (or the same
two-dimensional input Gram realization at population level), the second
is a Gram matrix of rank-one operators, and the third is a Gram matrix
of fields. Equivalently, the equations directly give

\[
 \dot L=-\mathcal V(t)^2,\qquad
 \mathcal V(t)^2=
 \begin{cases}
 \sum_{a=1}^2\|\dot z^{(1)}_a\|_2^2
      +\|\dot A\|_{\rm HS}^2+\|\dot b\|_2^2,&\rho=0,\\
 \|\dot z^{(1)}_1\|_2^2
      +\|\dot A\|_{\rm HS}^2+\|\dot b\|_2^2,&\rho=-1.
 \end{cases}
\tag{6.5}
\]

At finite width this is precisely
\(d\|\dot W^{(1)}\|_F^2/n+\|\dot W^{(2)}\|_F^2
+\|\dot W^{(3)}\|_2^2/n\), with a minus sign in the loss derivative.
For rho=-1 (6.5) says \(\dot L=-16r^2\kappa\), agreeing with
\(L=2r^2\) and (4.8).

Let \(R_0=\sqrt{L(0)}\). On every interval of existence,

\[
 \|r(t)\|_{\mathbb R^2}\leq R_0,\qquad
 S(t)\leq2\sqrt2 R_0t,\qquad
 \int_0^T\mathcal V(t)^2\,dt=L(0)-L(T)\leq L(0).
\tag{6.6}
\]

For rho=0 use \(S=2\int(|r_1|+|r_2|)\); for rho=-1 use
\(S=4\int|r|\) and \(\sqrt L=\sqrt2|r|\).
Combining (6.6) with (6.1)--(6.2) rules out every finite-time escape and
proves global physical existence. It also proves that the integral in
(4.8) is finite on finite horizons, since
\(\kappa\leq\|A\|_{\rm op}^2\|b\|_2^2
+B^2\|b\|_2^2+B^2\).

At any reached time t0 the full state \((u(t0),A(t0),b(t0))\) has cubic
coordinate in H1, a bounded operator, and bounded readout. The same local
construction and uniqueness therefore apply from that state; concatenated
solutions agree by (5.3). All equations depend only on the current state.
This proves autonomous restart, including nonzero reached population
readout. It does not replace that readout by its time-zero value.

The uniqueness assertion also applies to the original ordinary-L2
physical integral equations; it is not just uniqueness among paths
assumed in advance to have an L2 cubic transform. To verify this, take
any such solution with the prescribed initial state, operator-norm
continuous A, and continuous L2 fields. Its predictions and residuals
are continuous: bounded Lipschitz activations are continuous in L2,
and the final scalar inner product is jointly continuous. On a compact
interval the readout integral equation therefore gives an L-infinity
bound by (5.4). Hence q is locally integrable in L2 and the raw first
equation has the form
\(\dot z=cD(z)q\) for each independent first field. Its Bochner integral
has a representative with an absolutely continuous scalar path for
almost every first-neuron point: this follows directly from Fubini and
\(\int\|cD(z)q\|_2<\infty\). On each such path the ordinary scalar
chain rule, with no unbounded-multiplier estimate, gives

\[
 F(z(t))=F(z(0))+\int_0^t c(v)q(v)\,dv.
\tag{6.7}
\]

The integral on the right is in L2 because
\(\int|c(v)|\|q(v)\|_2dv<\infty\). Thus the original solution
automatically belongs to the cubic-coordinate class and satisfies its
integral equation. Section 5 proves its uniqueness. The antiparallel
relations hold automatically for actual raw matrices; if both sample
fields are retained in an abstract population integral formulation,
their first-field derivatives sum to zero for C with rho=-1, so their
initial opposition is preserved there as well.

For use in the continuity statements above, if bounded scalar
multipliers converge in measure and have a common bound, their products
with a fixed L2 field converge in L2. One proof splits the field into a
bounded part and an L2-small tail; on the bounded part bounded
convergence in measure gives convergence of the integral, and the tail
is uniformly small. Splitting a difference with a varying L2 field into
two terms then proves the needed product continuity. Together with
(6.3), this also gives continuity of the original hidden-field
derivatives and of the kernel blocks along the physical flow.

## 7. Width-independent transformed Euler consistency and stability

Let \(Y=(u,A,b)\), and let \(\mathcal G(Y)\) denote the physical field
(3.2) or (4.5). On any physical horizon T, (6.1) and (6.6) put the exact
solution in fixed operator/readout bounds. Equations (5.2)--(5.3) then
give constants \(V_T,L_T\), depending on T, a0, and the initial readout
bounds, but independent of width and the size of the initial cubic
coordinate, such that

\[
 \|\dot Y(t)\|_{\mathcal E_p}\leq V_T,\qquad
 \|\mathcal G(Y(t))-\mathcal G(Y(s))\|_{\mathcal E_p}
 \leq L_TV_T|t-s|.
\]

Integrating the second inequality proves the local consistency estimate

\[
 \|Y(t+\eta)-Y(t)-\eta\mathcal G(Y(t))\|_{\mathcal E_p}
 \leq \tfrac12 L_TV_T\eta^2.
\tag{7.1}
\]

This uses no coordinate supremum of q or of a hidden field.

For completeness, genuine untruncated Euler iterates are also bounded
and converge on each fixed horizon for a width-independent sufficiently
small step. Here is a bootstrap that will also apply to raw GD. Put
\(R=R_0+1\), and work up to the first mesh index at which
\(\|(r_1,r_2)\|_{\mathbb R^2}>R\). Before this index the accumulated
discrete action through time T+1 is at most

\[
 S_*:=2\sqrt2 R(T+1).
\]

The explicit b update gives \(\|b_k\|_\infty\leq b_\infty+BS_*\),
and summing the explicit A update gives

\[
 \|A_k-A_0\|_p
 \leq Bb_2S_*+\tfrac12B^2S_*^2.
\tag{7.2}
\]

To see the half coefficient discretely, if \(\alpha_k\geq0\) are the
action increments and \(S_k=\sum_{j<k}\alpha_j\), then
\(\sum_k\alpha_kS_k=(S_N^2-\sum_k\alpha_k^2)/2\leq S_N^2/2\).
The same bounds include the first candidate exit index, because its
update uses the previous residual. Choose the common constants a,M in
(5.1) large enough for these bounds and the exact flow through T+1.

If a numerical sequence satisfies

\[
 Y_{k+1}=Y_k+\eta\mathcal G(Y_k)+d_k,\qquad Y_0=Y(0),
\]

then (7.1) and (5.3), while the bounds hold, give

\[
 e_{k+1}\leq(1+\eta L_T)e_k+C_T\eta^2+\|d_k\|_{\mathcal E_p},
 \qquad e_k=\|Y_k-Y(k\eta)\|_{\mathcal E_p}.
\]

Iterating this finite geometric inequality proves

\[
 \max_{k\eta\leq T+\eta}e_k
 \leq e^{L_T(T+1)}
       \left(C_T(T+1)\eta+\sum_k\|d_k\|_{\mathcal E_p}\right).
\tag{7.3}
\]

For Euler, d_k=0. By (5.1), the norm of the two-residual difference from
the exact flow is at most \(\sqrt2L_fe_k\), in either geometry. Choose
eta so that the right side of (7.3), times \(\sqrt2L_f\), is below 1/2.
Then the candidate exit index cannot have residual norm exceeding
R0+1, because the exact residual norm is at most R0. This closes the
bootstrap and proves O_T(eta) convergence for the piecewise linear
transformed Euler interpolation. Its piecewise constant velocities also
converge to the transformed GF velocities at O_T(eta), using (5.3).

## 8. Raw GD: exact cubic defect and explicit primal assumptions

Fix a finite width and keep the contract's exact raw updates, loss SUM,
and \(\eta=n^{-2}\). At each mesh point define u from the raw first
field using F; do not replace the raw update by an update in u.

For either geometry, in each independent first-field coordinate the raw
increment has the form

\[
 \Delta z=\eta c D(z)q,
 \qquad c=-2r_a\ (\rho=0),\quad c=-4r\ (\rho=-1).
\tag{8.1}
\]

The polynomial identity

\[
 F(z+\Delta z)-F(z)
 =(1+z^2)\Delta z+z(\Delta z)^2+(\Delta z)^3/3
\]

is exact coordinatewise. Thus the raw endpoint update in transformed
coordinates is

\[
 u^+=u+\eta cq+\varepsilon,
 \qquad
 \varepsilon=\eta^2c^2zD(z)^2q^2
                  +\tfrac13\eta^3c^3D(z)^3q^3.
\tag{8.2}
\]

There is no discretization defect in the A or b coordinates relative to
Euler evaluated at this state. Both raw variables already use their
correct physical vector fields.

Here are sufficient, explicit high-probability primal assumptions on a
time horizon, if supplied from another argument: on events E_n(T) with
probability tending to one, uniformly over \(k\eta\leq T+\eta\),

\[
 \|(r_{1,k},r_{2,k})\|\leq R_T,\qquad
 \|W^{(2)}_k\|_{\rm op}\leq A_T,\qquad
 \|W^{(3)}_k\|_\infty\leq M_T,
\tag{8.3}
\]

where R_T,A_T,M_T are deterministic and independent of n. No
post-training Gaussianity, independence, pointwise q bound, or first
preactivation maximum is assumed. In fact Section 8.2 below establishes
(8.3) from a simple initialization event for this finite-GD/GF comparison.

### 8.1 The defect order under (8.3)

On (8.3), with \(Q=A_TM_T\),

\[
 \|q\|_n\leq Q,\qquad \|q\|_\infty\leq\sqrt n Q.
\tag{8.4}
\]

The second inequality is just the comparison of normalized Euclidean
and coordinate maximum norms. Since \(|z|D(z)^2\leq1\) and D<=1,

\[
\begin{aligned}
 \|\varepsilon\|_n
 &\leq\eta^2c^2\|q\|_\infty\|q\|_n
       +\tfrac13\eta^3|c|^3\|q\|_\infty^2\|q\|_n\\
 &\leq\eta^2c^2\sqrt n Q^2
       +\tfrac13\eta^3|c|^3 nQ^3.
\end{aligned}
\tag{8.5}
\]

There are at most two independent first coordinates, and
\(|c|\leq4R_T\) suffices in both cases. Consequently, at eta=n^-2,

\[
\begin{array}{ll}
 \text{one-step cubic-coordinate defect:}
   &O_T(n^{-7/2}+n^{-5}),\\
 \text{sum of defect norms through T:}
   &O_T(n^{-3/2}+n^{-3}),\\
 \text{defect divided by one raw step:}
   &O_T(n^{-3/2}+n^{-3}).
\end{array}
\tag{8.6}
\]

The constants concern the assumed primal bounds only. In particular, no
factor \(\max_i|z_i|\) has been hidden in them; the first derivative
cancellation and \(|z|D(z)^2\leq1\) removed it.

Apply (7.3) with d_k consisting of these first-coordinate defects and
zero operator/readout defects. The comparison flow is the exact GF
starting from the *same finite initial matrices and readout*. On (8.3),
after also including that GF's bounds in a,M,

\[
 \max_{k\eta\leq T}
 \|Y_k^{\rm GD}-Y^{\rm GF}(k\eta)\|_{\mathcal E_p}
 \leq C_T(\eta+\eta\sqrt n+\eta^2n)
 =O_T(n^{-3/2}).
\tag{8.7}
\]

This is a deterministic comparison on an event. It is not a comparison
with any as-yet-unconstructed canonical population limit.

### 8.2 A closed bootstrap and an elementary initialization event

The assumptions (8.3) need not be assumed indefinitely. On any finite
initialization with \(\|A_0\|_{\rm op}\leq a_*\) and
\(\|b_0\|_\infty\leq b_*\), the first-exit bootstrap in Section 7 also
applies to raw GD: its A and b updates are identical to those used to
prove (7.2), and its sole error is (8.2). Before the first residual exit,
take a,M from (7.2), use (8.5), and apply (7.3). For all sufficiently large
n (depending on T,a_*,b_*), its bound is below the residual-exit margin.
The candidate exit is impossible. Since
\(R_0\leq\sqrt2(Bb_*+1)\), all constants can be chosen uniformly over
these initializations. This proves (8.3) for exact raw GD through T and
proves (8.7), rather than assuming a trained-field probabilistic theorem.

For the contract initialization take a_*=8 and b_*=1. An explicit event
with these properties has probability at least

\[
 1-2\exp[-(8-2\log9)n]-2n\exp(-n^2/2).
\tag{8.8}
\]

Here is an elementary verification. A maximal 1/4-separated subset of
the unit sphere is a 1/4-net of size at most \(9^n\), by comparing
disjoint balls of radius 1/8 about its points with the ball of radius
9/8. Approximating both arguments of a bilinear form by this net gives
\(\|A_0\|_{\rm op}\leq2\max_{u,v\text{ in net}}|u^TA_0v|\).
For fixed unit u,v, the latter scalar has law N(0,1/n). The inequality
\(\mathbb P(|N(0,1)|>t)\leq2e^{-t^2/2}\) follows from
\(\mathbb E e^{sN}=e^{s^2/2}\), Markov's inequality, and minimization at
s=t, applied to each sign. A union bound at t=4 sqrt(n) therefore gives
the operator term in (8.8). The same scalar tail bound and a union bound
for \(b_{0,i}\sim N(0,n^{-2})\) give its second term. No independence
between the two events is needed for this final union bound.

These estimates do not alter any initialization. One can additionally
record \(\|b_0\|_\infty\leq\sqrt{6\log n}/n\) with probability at least
\(1-2n^{-2}\). This explains why zero is the intended initial population
readout, without itself identifying the rest of the population limit.
No extra first-layer tail event is required for the consistency bounds.

## 9. Raw interpolation, original velocities, and the limits of these corollaries

The contract interpolates the raw matrices linearly and recomputes hidden
fields. For \(t=k\eta+\theta\eta\), \(0\leq\theta\leq1\), its first
field is \(z_k+\theta\Delta z_k\), so the corresponding cubic coordinate
differs from the straight interpolation of the two cubic endpoints by

\[
 (\theta^2-\theta)z_k(\Delta z_k)^2
       +(\theta^3-\theta)(\Delta z_k)^3/3.
\tag{9.1}
\]

Equation (8.5) bounds (9.1) by O_T(eta^2 sqrt(n)+eta^3 n). Hence (8.7)
holds uniformly in continuous physical time for the actual raw
interpolation, its recomputed cubic coordinate, and either p metric.
Within the open mesh interval its cubic-coordinate derivative is

\[
 cq+2\theta z_k(\Delta z_k)^2/\eta
                       +\theta^2(\Delta z_k)^3/\eta,
\tag{9.2}
\]

whose difference from cq is O_T(eta sqrt(n)+eta^2 n). Equations (5.3),
(8.7), and (9.2) give uniform O_T(n^-3/2) comparison of transformed
velocities. The same bound applies at mesh nodes when using right
velocities at interior nodes and the left velocity at a terminal node.
It does not assert that the two one-sided velocities of GD agree.

Predictions, loss, both first hidden fields, and both second hidden fields
are Lipschitz in the bounded sets of (5.1), so their finite-GD/GF uniform
L2 comparisons have rate O_T(n^-3/2). The same operator estimate controls
both forward and transpose applications to any fixed finite probes of
uniformly bounded normalized L2 norm; for example
\(\|(A^{\rm GD}-A^{\rm GF})v\|_n
\leq\|A^{\rm GD}-A^{\rm GF}\|_{\rm op}\|v\|_n\), and identically for
the actual transposes. This statement is about comparison at a fixed
width, not convergence of probes across widths.

For original first-layer velocities it would be incorrect simply to
claim dimension-free L2 Lipschitz continuity of \(D(z^{(1)})q^{(1)}\).
At finite width a sufficient weaker estimate is

\[
 \|D(z)q-D(\widetilde z)\widetilde q\|_n
 \leq\|q-\widetilde q\|_n
      +\|\widetilde q\|_\infty\|z-\widetilde z\|_n.
\tag{9.3}
\]

Using (8.4), the transformed error (8.7), and the O_T(eta) motion from
the preceding mesh state gives original first-layer velocity error
O_T(sqrt(n) n^-3/2)=O_T(n^-1). The readout and hidden-matrix velocity
errors, in L2 and HS respectively, remain O_T(n^-3/2) by (5.1).
The raw first-matrix velocity metric is exactly the one in (3.4) or its
one-field antiparallel version.

All individual original hidden-field velocities are bounded in L2
uniformly over width on this horizon: for example
\(\dot z^{(2)}=\dot A h^{(1)}+A D(z^{(1)})\dot z^{(1)}\).
Applying (9.3) also to
\(\dot h^{(1)}=D(z^{(1)})\dot z^{(1)}\), and then to the analogous
second-layer identity, shows their finite-GD/GF velocity differences are
O_T(n^-1). In these applications the needed finite coordinate maximum
is at most sqrt(n) times its uniformly bounded L2 norm. This argument
uses no Lp boundedness of A.

It follows from \(|\|v\|^2-\|w\|^2|\leq(\|v\|+\|w\|)\|v-w\|\)
that the integrated squared raw parameter velocities for finite GD and
its finite GF differ by O_T(n^-1). The same holds for each of the
individual hidden-field velocity energies just described. The exact
GF identity (6.5) does not become an exact loss identity for raw GD.

For completeness, the finite-GD/GF kernel comparisons are
O_T(n^-1) for K^(1), using (9.3), and O_T(n^-3/2) for K^(2),K^(3),
using (5.1) and bounded inner-product factors in (4.6). If desired, the
same-neuron coupling of the two finite hidden-path empirical measures
also has W2 distance O_T(n^-1) on C([0,T]) with its supremum norm:
each path difference starts at zero and
\(\sup_t|e_i(t)|^2\leq T\int_0^T|\dot e_i(t)|^2dt\); sum over neurons
and both samples. This compares GD with GF at the same n only.

## 10. Why this does not cover intermediate rho; remaining bridges

For a general fixed \(-1<\rho<1\), the exact first-layer physical system
has C off diagonal equal to rho. Applying this same F gives, for b!=a,

\[
 \dot u_a=-2r_aq^{(1)}_a
 -2\rho r_b
   \frac{\phi_1'(z^{(1)}_b)}{\phi_1'(z^{(1)}_a)}q^{(1)}_b
 =-2r_aq^{(1)}_a
 -2\rho r_b
   \frac{1+(z^{(1)}_a)^2}{1+(z^{(1)}_b)^2}q^{(1)}_b.
\tag{10.1}
\]

At rho=0 the second term vanishes. At rho=-1 the actual invariant
relation \(z^{(1)}_2=-z^{(1)}_1\), and the corresponding equal q fields,
make it the same single-field equation with the correct factor four.
For nonzero intermediate rho neither simplification holds. Even at a
nondegenerate correlated Gaussian first pair, the ratio in (10.1) is
essentially unbounded: sets with one coordinate arbitrarily large and
the other bounded have positive Gaussian probability. Multiplication
by that ratio is not a bounded L2 operator. More explicitly, if a
measurable multiplier R is essentially unbounded, for every N there is
a positive-measure set E with |R|>=N; the unit L2 function
\(1_E/\sqrt{\mu(E)}\) is sent to a function with L2 norm at least N
(or infinite). Thus no estimate using only its input L2 norm can justify
the cross term. The bounded-operator hypothesis on A provides only an
L2 bound for q, and no such multiplication estimate.

This shows exactly why the present coordinate proof does not extend. It
is not a counterexample to the actual canonical trajectory: in
particular, population q is zero at initial zero readout. A trajectory
may have additional structure that this lemma has not established.
Opposite labels alone do not impose pathwise f2=-f1 at intermediate
angles, nor do they impose odd pairing of the hidden fields or a
readout symmetry. No such relation was used for the orthogonal case.

The remaining bridges are explicit:

1. **Canonical population realization and convergence.** Construct the
   separate population spaces, the specified initial Gaussian fields,
   and a genuine bounded A0 with the correct joint forward/adjoint and
   operator-reuse laws of the canonical matrices. Then identify a
   full-sequence finite-width limit in a framework compatible with the
   common-action stability here. A random finite matrix is not declared
   to be an iid integral kernel on a continuum. No tensor-program
   convergence theorem or specialized nonclassical theorem was invoked
   or proved in this note.
2. **Population observables.** Identify the canonical joint same-neuron
   two-sample path laws, fixed admissible probes in both directions, all
   kernel blocks, and population velocities/velocity energies. The
   same-width deterministic comparisons in Sections 7--9 do not by
   themselves perform any of these identifications. In particular,
   operator-norm closeness across arbitrary different-width
   realizations is not supplied here.
3. **Nontrivial learning and distributional nonaffinity.** The scalar
   functions here are exactly arctan at every time, but a proof that
   both canonical hidden layers genuinely learn and both evolved
   activation distributions remain nonaffine at every finite time is
   still needed. The deterministic operator class even allows A0=0,
   b0=0, in which case the state can be stationary. No nontriviality
   conclusion is inferred from this anchor.
4. **Other angles and depth.** Overcome (10.1) for all nonzero
   intermediate rho with a fixed admissible activation design and the
   prescribed initialization/clock. The all-angle L=2 target and the
   active L=3 target are not established here.

### Proof-content SHA-256

Hash convention: SHA-256 of all UTF-8 bytes strictly before the line
`### Proof-content SHA-256`, including the newline immediately preceding
that line. This avoids a self-referential whole-file digest. The source
contract snapshot hashes are recorded above. The whole-file digest may additionally
be reported outside this document.

Proof-content digest:
`3e1da9dc804fc922ece75a1cf66f4cb3290971d99478547de59fa915a9a84af9`.

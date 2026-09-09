# Variational obstructions for the exact two-hidden-layer raw loss

2026-09-08. This is a theoretical route audit for
\(\phi(z)=\tfrac34(1+z)+\tfrac14\tanh z\) and the exact contract in
../CONTRACT.md. No experiment, replacement action, or external theorem is
used. The constructions cover every admissible three-input Gram, including
singular Grams.

**Result.** Arbitrarily close to canonical initialization, the actual raw
loss has unit-direction second derivatives unbounded below, is not weakly
lower semicontinuous, and remains not weakly lower semicontinuous after adding
any positive quadratic proximal penalty. Its bounded nonlinear activation
remainder is not compact. These facts rule out several ambient variational
shortcuts; they do not contradict existence or uniqueness along the reached
trajectory.

No strong-flow existence or width-identification theorem is proved here.
The sequences below are admissible states, not claimed outputs of true
gradient dynamics, energy-dissipating approximations, or finite algorithms.

## 1. The actual scalar potential and its positive regularity

Use \(w=\sqrt d W\), \(u_i=x_i/\sqrt d\), and the raw Hilbert space

\[
\mathcal X=L^2(\Omega_1;\mathbb R^d)
\oplus\mathrm{HS}(H_1,H_2)\oplus H_2,\qquad
\Theta=(w,U,C),\quad A=A_0+U.
\]

The squared raw norm is the sum of the three squared Hilbert norms, with no
remaining factor \(d\). The initialized action is the actual canonical
\(A_0\), with its genuine adjoint, and need not be Hilbert--Schmidt. Write

\[
z_i=w\cdot u_i,\quad h_i=\phi(z_i),\quad v_i=Ah_i,\quad
f_i=\langle C,\phi(v_i)\rangle,\qquad
E=\frac12\sum_i(f_i-y_i)^2.
\]

Initialization is \(\Theta_0=(w_0,0,0)\). The raw loss is continuously Frechet
differentiable, with gradient bounded on bounded primal balls. Here is an
elementary verification sufficient for the later coordinate argument. Forward
field increments caused by a raw increment of size \(\varepsilon\) are
\(O(\varepsilon)\) in \(L^2\). For fixed \(a\in L^2\),

\[
\int |a|\,|\phi(v+\delta v)-\phi(v)-\phi'(v)\delta v|
=o(\|\delta v\|_2).
\tag{1}
\]

The remainder is at most both \(\tfrac14|\delta v|^2\) and \(2|\delta v|\).
Split into \(|a|\le M\) and its complement to bound the integral by

\[
\frac M4\|\delta v\|_2^2+
2\|a\mathbf1_{|a|>M}\|_2\|\delta v\|_2.
\]

First send \(\|\delta v\|_2\) to zero, then \(M\) to infinity. Apply (1)
successively with the fixed readout and genuine backward fields. Products
of two raw increments contribute \(O(\varepsilon^2)\). This gives the true
raw gradient

\[
g_w=\sum_i r_i\phi'(z_i)q_i u_i,\quad
g_U=\sum_i r_i b_i\otimes h_i,\quad
g_C=\sum_i r_i\phi(v_i),\qquad
b_i=C\phi'(v_i),\quad q_i=A^*b_i.
\tag{2}
\]

A uniformly bounded multiplier converging in probability converges strongly
against a fixed \(L^2\) function: extract an almost-sure subsequence and use
dominated convergence, then apply the subsequence criterion. This proves
continuity of the gates in (2); bounded actions and rank-one products prove
continuity of the gradient. Bounded slopes and linear growth give its
boundedness on primal balls. No Frechet differentiability of the activation
Nemytskii map on ambient \(L^2\) is asserted.

## 2. A genuine rank-one variation isolates one top preactivation

Let \(h_i^0=\phi(w_0\cdot u_i)\) and
\(H_{ij}=\langle h_i^0,h_j^0\rangle\). Then \(H\) is positive definite,
including when the input Gram \(\Gamma\) is singular.

Indeed, if \(\sum_i c_i h_i^0=0\), expectations give \(\sum_i c_i=0\).
For \(G\sim N(0,1)\) and \(\kappa=\mathbb E\operatorname{sech}^2G\),

\[
\mathbb E[w_0\phi(w_0\cdot u_i)]
=\left(\frac34+\frac14\kappa\right)u_i.
\tag{3}
\]

To check (3), decompose \(w_0=Gu_i+w_\perp\); the orthogonal Gaussian
component has zero conditional mean. Integration by parts gives
\(\mathbb E[G\tanh G]=\mathbb E\operatorname{sech}^2G\), with a vanishing
Gaussian boundary term. All \(\|u_i\|=1\), so the coefficient is common and
positive. Thus \(\sum_i c_i u_i=0\). Three distinct sphere points are affinely
independent: otherwise they lie on a line, whereas a line intersects a sphere
in at most two points, by the quadratic equation for its squared norm.
Separation guarantees distinctness. Therefore \(c=0\).

Define

\[
h_i^\dagger=\sum_j(H^{-1})_{ij}h_j^0,\qquad
\langle h_i^\dagger,h_j^0\rangle=\delta_{ij},\qquad
D_i=\|h_i^\dagger\|_2>0.
\tag{4}
\]

For \(a\in H_2\), a Hilbert--Schmidt perturbation of the actual action satisfies

\[
(a\otimes h_i^\dagger)h_j^0=\delta_{ij}a,\qquad
\|a\otimes h_i^\dagger\|_{\mathrm{HS}}=D_i\|a\|_2.
\tag{5}
\]

Thus it changes only one sample's top preactivation. This is an exact slice
of the original network, not a substitute architecture or action.

The initialized tuple \(v^0=(A_0h_i^0)_i\) is centered Gaussian with covariance
\(H\), by the actual first forward query. It is nondegenerate. Choose a
positive-measure event \(B\) on which every \(|v_j^0|\le K\), as small in
measure as desired. The restricted space on \(B\) is nonatomic: one may take
a bounded rectangle of this nondegenerate Gaussian tuple and subdivide it
using a continuously distributed coordinate.

## 3. One fixed bad state in each initialization neighborhood

Fix a sample \(i\). Set \(x_*=-1\) if \(y_i\ge0\), and \(x_*=1\) if \(y_i<0\).
The values \(\phi(x_*)\) and \(\phi''(x_*)\) have opposite nonzero signs.
This choice works for either binary-label convention.

Take \(B\) as above and set

\[
U_*=[(x_*-v_i^0)\mathbf1_B]\otimes h_i^\dagger.
\tag{6}
\]

Its norm is at most \(D_i(|x_*|+K)\sqrt{\mu(B)}\). It sets \(v_i=x_*\) on
\(B\), leaves \(v_i\) unchanged outside \(B\), and leaves all \(v_j\), \(j\ne i\),
unchanged.

Partition \(B\) into \(B_m\), \(m\ge1\), with
\(\mu_m:=\mu(B_m)=15\mu(B)2^{-4m}\), whose measures sum to \(\mu(B)\).
For \(\sigma>0\), set

\[
C_*=\sum_{m\ge1}M_m\mathbf1_{B_m},\qquad M_m=\sigma2^m.
\tag{7}
\]

Then \(C_*\ge0\) is unbounded and
\(\|C_*\|_2^2=5\sigma^2\mu(B)\). Choose \(B\) small and then \(\sigma\) small
so that \(\Theta_*=(w_0,U_*,C_*)\) lies strictly inside any prescribed raw
initialization neighborhood.

Since \(C_*\) is supported where \(v_i=x_*\),

\[
f_i(\Theta_*)=\phi(x_*)\int C_*,\qquad
r_i(\Theta_*)\phi''(x_*)=-c_*<0.
\tag{8}
\]

If \(y_i\ge0\), then \(f_i<0\), \(r_i<0\), and \(\phi''(-1)>0\).
If \(y_i<0\), then \(f_i>0\), \(r_i>0\), and \(\phi''(1)<0\).
Thus \(c_*\) is strictly positive and fixed once the state is chosen.
Other predictions are finite by Cauchy--Schwarz.

## 4. No local semiconvexity in any equivalent Hilbert norm

At this one state choose unit raw directions

\[
\xi_m=\left(0,\,
\frac{\mathbf1_{B_m}}{D_i\sqrt{\mu_m}}\otimes h_i^\dagger,\,0\right).
\tag{9}
\]

Only \(f_i\) changes along these lines. For each fixed \(m\), scalar
differentiation under the integral is legitimate: its perturbation is bounded
and supported on \(B_m\), where \(C_*=M_m\). Therefore

\[
\begin{split}
\frac d{dt}f_i(\Theta_*+t\xi_m)\big|_{t=0}
&=\frac{M_m\sqrt{\mu_m}}{D_i}\phi'(x_*),\\
\frac {d^2}{dt^2}f_i(\Theta_*+t\xi_m)\big|_{t=0}
&=\frac{M_m}{D_i^2}\phi''(x_*),\\
\frac {d^2}{dt^2}E(\Theta_*+t\xi_m)\big|_{t=0}
&=\frac{M_m^2\mu_m\phi'(x_*)^2-c_*M_m}{D_i^2}
\longrightarrow-\infty.
\end{split}
\tag{10}
\]

The first term tends to zero, since \(M_m^2\mu_m\) has order \(2^{-2m}\).

No neighborhood of \(\Theta_*\) therefore admits a finite semiconvexity
constant: convexity of \(E(\Theta)+(\lambda/2)\|\Theta\|^2\) would imply
a lower second-derivative bound \(-\lambda\) along every sufficiently short
unit-direction line, contradicting (10). Since \(\Theta_*\) lies strictly
inside an arbitrarily small initialization ball, no raw initialization
neighborhood is semiconvex either. This says nothing about second
directional derivatives exactly at \(C=0\).

For a fixed equivalent Hilbert norm
\(\|\xi\|_G^2=\langle G\xi,\xi\rangle\), \(0<aI\le G\le bI<\infty\),
the proposed lower bound is still at least \(-\lambda b\) on these directions.
Thus an equivalent norm does not repair the obstruction. The corresponding
bound
\(\langle\nabla E(\Theta)-\nabla E(\bar\Theta),\Theta-\bar\Theta\rangle
\ge-L\|\Theta-\bar\Theta\|^2\)
also fails: differentiating it along a line would give the same lower bound.
Likewise the loss-relative quantity

\[
E(\Theta)-E(\Theta_*)-
\langle\nabla E(\Theta_*),\Theta-\Theta_*\rangle
\]

has no lower quadratic bound in raw distance near \(\Theta_*\).

## 5. Weak lower semicontinuity fails after every quadratic proximal penalty

On each fixed \(B_m\), construct balanced Rademacher functions \(e_n\),
taking \(1,-1\) on equal-measure parts and pairwise orthogonal in \(L^2(B_m)\).
Recursive equal-halves partitions supply them on the nonatomic space.
They converge weakly to zero: finite orthogonal projections give

\[
\sum_{n\le N}|\langle a,e_n/\sqrt{\mu_m}\rangle|^2\le\|a\|_2^2
\]

for each \(a\in L^2(B_m)\); hence each coefficient tends to zero.

For fixed \(m\) and small \(\alpha>0\), let

\[
\Theta_n=\Theta_*+
(0,\alpha e_n\mathbf1_{B_m}\otimes h_i^\dagger,0).
\tag{11}
\]

Then \(\Theta_n\rightharpoonup\Theta_*\) in the raw Hilbert space and
\(\|\Theta_n-\Theta_*\|^2=\alpha^2\mu_mD_i^2\). Put

\[
\Delta(\alpha)
=\frac{\phi(x_*+\alpha)+\phi(x_*-\alpha)}2-\phi(x_*)
=\frac12\phi''(x_*)\alpha^2+o(\alpha^2).
\tag{12}
\]

The balance of \(e_n\) gives, exactly and independently of \(n\),

\[
f_i(\Theta_n)=f_i(\Theta_*)+M_m\mu_m\Delta(\alpha),
\qquad f_j(\Theta_n)=f_j(\Theta_*)\quad(j\ne i).
\]

It follows that

\[
E(\Theta_n)-E(\Theta_*)
=r_iM_m\mu_m\Delta(\alpha)
+\frac12[M_m\mu_m\Delta(\alpha)]^2.
\tag{13}
\]

By (8), this is negative for each fixed \(m\) and all sufficiently small
\(\alpha>0\). The sequence can be kept inside any neighborhood of \(\Theta_*\).
Thus the actual loss is not weakly lower semicontinuous there.

Now fix any center \(\Theta_{\rm old}\in\mathcal X\) and \(h>0\), and set

\[
J_h(\Theta)=E(\Theta)+\frac1{2h}\|\Theta-\Theta_{\rm old}\|^2.
\tag{14}
\]

The penalty's cross term vanishes as \(n\to\infty\) by weak convergence.
For fixed \(m\), then \(\alpha\to0\), (12)--(14) give

\[
\frac{\lim_{n\to\infty}J_h(\Theta_n)-J_h(\Theta_*)}
{\mu_m\alpha^2}
=-\frac{c_*M_m}{2}+\frac{D_i^2}{2h}+o(1).
\tag{15}
\]

Choose \(m\) with \(c_*M_m>D_i^2/h\), then choose \(\alpha\) small.
The right side is negative. Therefore every positive quadratic proximal
penalty fails to restore weak lower semicontinuity near this one fixed state,
regardless of its center.

This defeats the direct-method argument using weak compactness of Hilbert
balls and weak lower semicontinuity of the proximal functional. It also
defeats a unique-proximal-step argument based on adding sufficiently large
quadratic curvature. It does not prove that any particular proximal problem
lacks a minimizer, or that no selected implicit scheme converges; neither
assertion follows merely from failure of weak lower semicontinuity.

## 6. The bounded nonlinear remainder is not compact

Use (6), now at \(\widehat\Theta_*=(w_0,U_*,0)\). On a fixed
positive-measure \(B\), take balanced orthogonal \(e_n\) and set

\[
\widehat\Theta_n
=\widehat\Theta_*+(0,\alpha e_n\mathbf1_B\otimes h_i^\dagger,0).
\tag{16}
\]

All readouts vanish, so residuals are \(-y_j\). For this gradient illustration
choose \(y_i\ne0\), as available for the usual \(\pm1\) labels or any nonzero
binary-label vector. The scalar Nemytskii noncompactness conclusion below
does not depend on labels.

The top readout gradient is \(g_C=-\sum_jy_j\phi(v_j)\). Replace only the
top activation by \(\phi_{\rm aff}(v)=\tfrac34(1+v)\), holding the actual lower
features fixed. The difference of the true and top-affine readout gradients is

\[
N_C=-\frac14\sum_j y_j\tanh(v_j).
\]

Only \(v_i\) varies along (16). For
\(d_\alpha=[\tanh(x_*+\alpha)-\tanh(x_*-\alpha)]/2>0\), orthogonality gives

\[
\|N_C(\widehat\Theta_n)-N_C(\widehat\Theta_k)\|_2
=\frac{|y_i|d_\alpha}{4}\sqrt{2\mu(B)}>0,\qquad n\ne k.
\tag{17}
\]

Thus these bounded states, as small around \(\widehat\Theta_*\) as desired,
have nonlinear gradient remainders with no strongly convergent subsequence.
The same example proves that \(v\mapsto\tanh(v)\) itself is noncompact from
\(L^2\) to \(L^2\), without any label restriction. If every label were zero,
the \(C=0\) slice would be stationary, so this particular gradient illustration
would not apply; the semiconvexity and proximal obstructions in Sections 3--5
still apply with their nonzero readout.

Affine growth plus a bounded scalar nonlinear term therefore does not give
a compact nonlinear perturbation on the actual canonical spaces. This
statement does not confuse compact scalar range with strong compactness of
a family of random variables.

## 7. Regular coordinate changes and relative output energy

Suppose \(\Psi\) is a \(C^2\) local coordinate diffeomorphism at \(\zeta_*\),
with \(\Psi(\zeta_*)=\Theta_*\), bounded derivative and inverse derivative,
and bounded second derivative near that point. Define
\(\eta_m=D\Psi(\zeta_*)^{-1}\xi_m\), with norms bounded above and below.
The symmetric second-difference expansion gives

\[
\lim_{t\to0}
\frac{E(\Psi(\zeta_*+t\eta_m))+E(\Psi(\zeta_*-t\eta_m))-2E(\Theta_*)}{t^2}
=
\frac {d^2}{dt^2}E(\Theta_*+t\xi_m)\big|_{t=0}
+\langle\nabla E(\Theta_*),
D^2\Psi(\zeta_*)[\eta_m,\eta_m]\rangle.
\tag{18}
\]

For rigor without a full Frechet Hessian of \(E\), expand
\(\Psi=\Theta_*+t\xi_m+\tfrac12t^2D^2\Psi[\eta_m,\eta_m]+o(t^2)\).
Since \(E\in C^1\), its change under this second-order displacement is
evaluated by \(\nabla E(\Theta_*)\) up to \(o(t^2)\). The straight-line
second derivative exists by (10). The correction in (18) is uniformly bounded
in \(m\); the negative divergence survives. A semiconvex function has the
corresponding lower bound on every symmetric second difference, so these
regular coordinates cannot restore local semiconvexity. This uses no
unproved classical second derivative along the curved coordinate path.

An unbounded state-dependent weight, such as one containing \(|C_*|\) on
top-preactivation directions, lies outside this argument. It defines a
stronger direction space and requires additional regularity not supplied by
the raw energy bound. Using it as a training metric also generally changes
the prescribed raw gradient. It could still be used solely for analysis,
if its properties were proved along the actual reached states.

The output-relative energy
\(\frac12\sum_i(f_i(\Theta)-f_i(\bar\Theta))^2\) is nonnegative, but cannot
control raw distance: for zero readouts it vanishes for arbitrary hidden
parameters, whose raw distance and readout-kernel block can differ. Therefore
prediction convergence alone does not identify the required canonical
parameters, hidden fields, or all kernel blocks.

## 8. Scope and the remaining opening

These are obstructions for the exact scalar potential on its actual
canonical raw domain. They strengthen the previous ambient non-Lipschitz
observation: no initialization neighborhood is semiconvex, every raw
quadratic proximal penalty can fail weak lower semicontinuity, and bounded
nonlinearity does not supply a compact remainder. All constructions allow
singular input Grams and use only genuine Hilbert--Schmidt increments of
the actual initialized action.

They establish no bad reached state, nonunique strong trajectory, failure of
finite-width convergence, or absence of a global strong solution. Finite
width lacks the infinite orthogonal sequences used here; global finite GF
is entirely consistent with these results.

A successful variational argument must consequently use a property of the
reached states or an additional dynamical relative-energy identity. It cannot
rest only on the loss being nonnegative and \(C^1\), its gradient being
bounded on primal balls, bounded scalar nonlinearity, or weak compactness of
a Hilbert ball. This note supplies no such additional reached-state identity.

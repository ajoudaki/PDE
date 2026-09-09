# Arctangent \(L=2\) continuous-time limit reconstructed as MFP

## 1. The theorem and its scope

Let \(H_n=\mathbb R^n\) with
\(\langle v,w\rangle_n=n^{-1}v^{\mathsf T}w\).  Initialize
\[
 A_{0,i},u_{0,i}\stackrel{\rm iid}{\sim}N(0,1),\qquad
 G_{0,ij}\stackrel{\rm iid}{\sim}N(0,1/n),
\]
with the three families mutually independent.  Put
\[
 X=\phi(u),\qquad Z=GX,\qquad Y=\phi(Z),\qquad
 f_n=\langle A,Y\rangle_n,\qquad \phi(x)=\arctan x.
\]
The \(A,u\) blocks use the normalized \(H_n\) metric, while \(G\) uses
the Frobenius metric.  For the full square loss
\(\mathcal L_n=(y-f_n)^2\), use the corresponding gradient flow.

There is a deterministic, autonomous operator-MFP state whose readouts
\(f,K,e^2\) satisfy, for every \(T<\infty\),
\[
 \sup_{t\le T}\bigl(
 |f_n(t)-f(t)|+|K_n(t)-K(t)|
 +|(y-f_n(t))^2-e(t)^2|
 \bigr)\xrightarrow{\mathbb P}0.                       \tag{1.1}
\]
The state is restartable after retaining one immutable two-sided Gaussian
action source.  This is a compact-time theorem for the canonical iid
initialization.  It is not operator-norm convergence, a finite-dimensional
scalar closure, or a theorem for arbitrary deterministic spike states.

The only imported probability input is the fixed-finite-program MFP master
law: any fixed DAG formed from \(G_0,G_0^{\mathsf T}\), coordinatewise
pseudo-Lipschitz maps, normalized inner products, and scalar feedback has
deterministic joint empirical laws and every fixed finite moment in the
width limit.  The singular-Gram form needed here is the no-rank-stability
\(\mathrm{NETSOR}^{T+}\) result obtained using the Tensor Programs III
core-set/rewrite theorem (Theorem E.15), not Moore--Penrose notation alone.
Real mesh constants follow from rational approximation and fixed-depth
\(L^2\) stability.

## 2. Exact finite feature flow

Define
\[
 d(z)={1\over1+z^2},\qquad B=A\odot d(Z),\qquad Q=G^*B.
\]
Feature ascent of \(f_n\) is exactly
\[
 A'=Y,\qquad
 u'={1\over1+u^2}\odot Q,\qquad
 G'=B\otimes X,                                       \tag{2.1}
\]
where
\[
 (b\otimes x)v=b\langle x,v\rangle_n
 ={1\over n}bx^{\mathsf T}v.
\]
The factor \(1/n\) makes the last equation exactly the Frobenius gradient.

Introduce the global natural coordinate
\[
 \Theta(u)=u+{u^3\over3},\qquad
 \rho=\Theta(u),\qquad \iota=\Theta^{-1}.
\]
Set
\[
 \Psi(\rho)=\arctan\iota(\rho),\qquad
 c(\rho)={1\over1+\iota(\rho)^2}.
\]
Since \(\Theta'=1/\phi'\),
\[
 \rho'=Q,\qquad \Psi'(\rho)=c(\rho)^2.                 \tag{2.2}
\]
Thus (2.1) becomes
\[
 A'=Y,\qquad \rho'=Q,\qquad G'=B\otimes X,             \tag{2.3}
\]
with
\[
 X=\Psi(\rho),\quad Z=GX,\quad Y=\arctan Z,\quad
 B=A\,d(Z),\quad Q=G^*B.                              \tag{2.4}
\]
All nonlinear multipliers except \(A\) are bounded and globally Lipschitz.

Differentiating the forward DAG gives
\[
 X'=c(\rho)^2Q,\qquad
 Z'=B\langle X^2\rangle_n+G\{c(\rho)^2Q\}.
\]
Consequently
\[
 {d f_n\over ds}=K_n,                                  \tag{2.5}
\]
where
\[
 K_n=
 \langle Y^2\rangle_n
 +\langle B^2\rangle_n\langle X^2\rangle_n
 +\langle c(\rho)^2Q^2\rangle_n\ge0.                  \tag{2.6}
\]
This is an exact finite-width identity.

## 3. MFP peeling of every fixed Euler mesh

Write
\[
 G(s)=G_0+q(s),\qquad
 q(s)=\int_0^sB(\sigma)\otimes X(\sigma)\,d\sigma.
\]
For an Euler feature mesh \(h\),
\[
 q^k=h\sum_{\ell<k}B^\ell\otimes X^\ell.
\]
The two reused-matrix nodes peel exactly as
\[
 Z^k
 =G_0X^k+h\sum_{\ell<k}
 B^\ell\langle X^\ell,X^k\rangle_n,                   \tag{3.1}
\]
\[
 Q^k
 =G_0^*B^k+h\sum_{\ell<k}
 X^\ell\langle B^\ell,B^k\rangle_n.                   \tag{3.2}
\]
Equations (3.1)--(3.2) are the operator-MFP recursion.  They retain every
same-matrix response: \(G_0X^k\) and \(G_0^*B^k\) are evaluated using one
shared two-sided Gaussian source, not refreshed Gaussian variables.

For fixed \(h\) and a fixed feature horizon, this is one finite MFP DAG.
The finite-program master law therefore gives the deterministic limiting
joint fields and all Gram coefficients in (3.1)--(3.2).

Taking a countable projective completion of all finite MFP programs produces
two probability Hilbert spaces \(H_R,H_C\), source marks
\[
 a_0\in H_R,\qquad
 \rho_0=u_0+u_0^3/3\in H_C,
\]
and a bounded operator
\[
 \Gamma:H_C\to H_R,\qquad \|\Gamma\|\le2.
\]
The finite identity
\(\langle G_0x,b\rangle_n=\langle x,G_0^*b\rangle_n\)
passes to the limit, so the peeled reverse action is the genuine Hilbert
adjoint \(\Gamma^*\).  The immutable MFP source is
\[
 \mathfrak G=(H_R,H_C;a_0,\rho_0,\Gamma).              \tag{3.3}
\]

## 4. The autonomous operator-MFP equation

Let \(q\in\mathfrak S_1(H_C,H_R)\) and \(G=\Gamma+q\).  The limiting
feature equation is
\[
 A'=Y,\qquad \rho'=Q,\qquad q'=B\otimes X,             \tag{4.1}
\]
where (2.4) is evaluated using the probability-space functional calculus.
The current state is \((A,\rho,q)\); past rank-one updates are compressed
into the single current trace-class operator \(q\).

Let \(a=\pi/2\).  Since
\[
 |X|,|Y|\le a,\qquad |B|\le|A|,
\]
one has on every bounded feature interval
\[
 \|A(s)\|_2\le\|a_0\|_2+a|s|,                         \tag{4.2}
\]
\[
 \|q(s)\|_1
 \le a\left(\|a_0\|_2|s|+{a\over2}s^2\right),         \tag{4.3}
\]
\[
 \|\rho(s)\|_2
 \le\|\rho_0\|_2+
 \int_0^{|s|}\|\Gamma+q(\sigma)\|_{\rm op}
 \{\|a_0\|_2+a\sigma\}\,d\sigma.                      \tag{4.4}
\]
These bounds exclude finite feature-time escape.

The only non-Lipschitz-looking map on the natural \(L^2\) phase space is
\(A\,d(Z)\), because \(A=a_0+\alpha\) with \(\alpha\) bounded but \(a_0\)
Gaussian.  If \(h\) is bounded Lipschitz and
\(\delta=\|z-\widetilde z\|_2\), Gaussian moments and interpolation give
\[
 \|a_0\{h(z)-h(\widetilde z)\}\|_2
 \le C\,\delta\sqrt{\log(e/\delta)}.                   \tag{4.5}
\]
The reciprocal integral of the modulus in (4.5) diverges.  Cut off \(a_0\),
solve the resulting locally Lipschitz Banach-space ODE, use (4.2)--(4.4)
for global continuation, and then remove the cutoff.  Bihari--Osgood
applied to (4.5) gives uniqueness and continuous dependence in the
Gaussian-envelope class
\[
 A(s)=a_0+\alpha(s),\qquad
 \sup_{|s|\le S}\|\alpha(s)\|_\infty<\infty.           \tag{4.6}
\]
The Gaussian cutoff is quantitative:
\[
 d(U^{(N)},U^{(M)})
 \le C_Se^{C_SM}
 \|a_0^{(N)}-a_0^{(M)}\|_2,
\]
and the Gaussian clipping tail decays as
\((1+M)e^{-M^2/4}\), which dominates \(e^{C_SM}\).

Therefore (4.1) has a unique global restartable solution and its limiting
readouts satisfy
\[
 F' = K
 =\langle Y^2\rangle
 +\langle B^2\rangle\langle X^2\rangle
 +\langle c(\rho)^2Q^2\rangle.                        \tag{4.7}
\]

## 5. Width identification and the repaired kernel step

First cut off \(a_0\) at level \(M\).  On a fixed feature interval, the
finite- and infinite-width cutoff vector fields have width-independent
bounds and Lipschitz constants on the high-probability event
\(\|G_{0,n}\|_{\rm op}\le L\).  Hence exact finite and limiting flows differ
from their common Euler discretizations by at most
\[
 C(M,S,L)h.                                            \tag{5.1}
\]
For fixed \(M,h,S\), the Euler system is the finite MFP DAG
(3.1)--(3.2), so width tends to infinity by the finite-program theorem.
Then \(h\downarrow0\).  This proves the state and bounded-readout limit in
the required order.

The raw term
\[
 \langle c(\rho)^2Q^2\rangle
\]
requires square uniform integrability.  A direct use of a fixed-mesh
\((2+\varepsilon)\)-moment bound uniformly as \(h\downarrow0\) would be
invalid.  The correct argument has two stages.

For one fixed auxiliary mesh, the MFP theorem gives a finite
\((2+\varepsilon)\)-moment for all its finitely many \(Q^h\) nodes.  The
dimension-free Euler comparison gives
\[
 \sup_{|s|\le S}\|Q_n(s)-Q_n^h(s)\|_2=O_{\mathbb P}(h).
\]
Using
\[
 q^2{\bf1}_{\{|q|>R\}}
 \le4(q-v)^2+2v^2{\bf1}_{\{|v|>R/2\}},                \tag{5.2}
\]
first choose this auxiliary mesh sufficiently fine and then choose \(R\)
sufficiently large.  This proves square-tail tightness for the exact
continuous cutoff trajectory:
\[
 \lim_{R\to\infty}\limsup_{n\to\infty}
 \Pr\!\left\{
 \sup_{|s|\le S}
 \langle Q_n(s)^2{\bf1}_{\{|Q_n(s)|>R\}}\rangle_n
 >\varepsilon\right\}=0.                              \tag{5.3}
\]

After (5.3) is established, use a separate comparison mesh.  Truncate at
the fixed level \(R\), pass the bounded part using \(L^2\) Euler convergence,
and pass the tail using (5.3).  This yields convergence of
\(c(\rho)Q\) in \(L^2\), hence convergence of its squared norm.  No
mesh-uniform high moment is assumed.

Finally remove the readout cutoff.  The asymmetric comparison
\[
 \sup_{|s|\le S}
 \{d(U_n,U_{n,M})+\|Q_n-Q_{n,M}\|_2\}
 \le C_Se^{C_SM}\|A_{0,n}-A_{0,n}^{(M)}\|_2           \tag{5.4}
\]
and the Gaussian tail give uniform cutoff removal in probability.  Applying
(5.2) again transfers (5.3) to the uncut trajectory.  Thus both \(f_n\) and
\(K_n\) converge uniformly on compact feature-time intervals.

## 6. Return to loss-gradient time

Let \(F(s)\) and \(K(s)=F'(s)\) be the feature readouts.  Define
\[
 \dot s=2\eta e,\qquad e=y-F(s),\qquad s(0)=0.
\]
Then
\[
 \dot e=-2\eta eK(s),\qquad
 e(t)=y\exp\!\left\{-2\eta\int_0^tK(s(\tau))\,d\tau\right\},              \tag{6.1}
\]
and
\[
 |s(t)|\le2\eta|y|t.                                  \tag{6.2}
\]
The feature solution is global in both signs of \(s\), so (6.1)--(6.2)
give a unique global physical trajectory, including negative labels.
At finite width \(f_n(0)\to0\) in probability, and the already proved
uniform convergence of \(F_n,K_n\) gives convergence of the scalar clocks.
Composition proves (1.1), with
\[
 f(t)=y-e(t),\qquad
 \dot{\mathcal L}(t)=-4\eta K(t)\mathcal L(t).
\]

## 7. Why the quadratic no-go does not transfer

For arctangent, \(A'=Y\) is pointwise bounded, so
\(A(s)=a_0+\) a uniformly bounded displacement; \(X,Y,d,c\) are bounded;
the learned connector has uniformly bounded trace norm; and (5.3) excludes
adaptive square-energy condensation in \(Q\).

For \(x^2\), neither the forward activation nor its derivative is bounded,
the Gaussian envelope is destroyed, and rare coordinates generate the
vanishing-time concentration layer.  The two conclusions therefore concern
the same iid MFP initialization but different activation classes and are
consistent.

## 8. Audit status and the discrete-GD boundary

An earlier proof attempted to remove the mesh by applying a
\((2+\varepsilon)\)-moment bound whose constant depended on the mesh.  That
argument was broken.  Sections 5.2--5.3 above are the repaired
square-tail-first proof.  Under the fixed-finite-program MFP master law, the
repaired theorem has no remaining conditional step for (1.1), namely the
width limit of the exact finite-width continuous ODE.

There is a different, presently open statement:
\[
 \lim_{h\downarrow0}\left[\lim_{n\to\infty}
 \{\text{actual discrete gradient descent of step }h\}\right].
 \tag{8.1}
\]
The auxiliary MFP scheme above updates the natural coordinate by
\[
 \rho^+=\rho+hQ.
\]
Actual Euler descent updates the original coordinate by
\[
 u^+=u+h\,{Q\over1+u^2}.
\]
Because \(\Theta(u)=u+u^3/3\), its exact transformed update is
\[
 \rho^+
 =\rho+hQ
 +h^2{uQ^2\over(1+u^2)^2}
 +{h^3Q^3\over3(1+u^2)^3}.                            \tag{8.2}
\]
For each fixed \(h\), (8.2) is again a finite MFP program.  To remove its
mesh after taking width first, however, one needs uniform reachable
high-moment control, for example bounds strong enough that
\[
 h\sum_{k<T/h}\|Q_k\|_4^2=O(1),\qquad
 h\sum_{k<T/h}\|Q_k\|_6^3=O(1),                       \tag{8.3}
\]
together with the corresponding state-stability estimates.  Fixed-\(h\)
MFP moments do not give (8.3), and the square-tail argument used for
\(\langle Q^2\rangle\) along the exact ODE does not imply it.

Thus the current proof is correct for (1.1), but it must not be cited as a
proof of the width-first actual-discrete-GD limit (8.1).

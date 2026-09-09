# Three separated inputs with the odd mixture: rigorous progress and the open bridge

2026-09-07. This is a theory-only research note. It does not assert the full
three-input theorem. No prior proof files were changed and no experiments
were run.

The target is the original three-hidden-layer raw model, with RMS-unit
inputs, all binary labels, pairwise absolute correlations at most
\(1-\delta\), and the same activation
\(\phi(z)=az+e\arctan z\), where \(a=1-e\), \(0<e\le1/2\), in every
hidden layer. In particular, the offset and the large gain of the older
three-input theorem are not admissible substitutes.

## 1. Authoritative existing facts

The proofs in
`studies/mean_field_peeling/odd_mixture_separation_quantitative/THREE_INPUT_GEOMETRY.md`
give the following facts, including singular input Grams.

Write \(u_i=x_i/\sqrt d\), \(\Gamma_{ij}=u_i\cdot u_j\),
\(s_\delta=\delta(2-\delta)\), and
\(b_3=(1-2E(1+G^2)^{-1})/\sqrt6\ne0\), where \(G\) is standard
normal. Cubic lifting and the third Gaussian chaos give
\[
 \Gamma^{\circ3}\succeq\frac{s_\delta^2}{3}I_3,
 \qquad
 Q_1(0)\succeq e^2b_3^2\frac{s_\delta^2}{3}I_3,
 \qquad
 Q_3(0)\succeq a^4Q_1(0).
\]
The worst-case first-feature minimum eigenvalue is
\(\Theta(e^2\delta^2)\), up to absolute constants. Thus the initial
nonlinear signal is strictly positive even at singular \(\Gamma\).
The same note proves the algebraic nonzero initial acceleration of each
hidden block and of every sample in every hidden layer; interpreting
these as trajectory derivatives requires the strong-solution chain rule.

Here is a self-contained proof of the initialization lower bound. For
\(i\ne j\), define
\[
 v_{ij}=\frac{u_i-\Gamma_{ij}u_j}{\sqrt{1-\Gamma_{ij}^2}}.
\]
The denominator is positive by \(\delta>0\). This vector has norm one,
is orthogonal to \(u_j\), and satisfies
\(\langle u_i,v_{ij}\rangle=\sqrt{1-\Gamma_{ij}^2}
\ge\sqrt{s_\delta}\). Let \(T_i=u_i^{\otimes3}\), and, with
\(\{i,j,k\}=\{1,2,3\}\), let
\(R_i=u_i\otimes v_{ij}\otimes v_{ik}\). Then \(\|R_i\|=1\),
\(\langle T_j,R_i\rangle=\langle T_k,R_i\rangle=0\), and
\(\langle T_i,R_i\rangle\ge s_\delta\). For any real coefficients
\(c_i\), Cauchy--Schwarz gives
\[
 |c_i|s_\delta\le\left\|\sum_j c_jT_j\right\|.
\]
Squaring and adding these three inequalities yields
\[
 \left\|\sum_jc_jT_j\right\|^2
 \ge\frac{s_\delta^2}{3}\sum_jc_j^2.
\]
Since \(\langle T_i,T_j\rangle=\Gamma_{ij}^3\), this proves the
cubic-Gram inequality without an inverse or a rank assumption.

To calculate the nonlinear coefficient, let
\(m=E(1+G^2)^{-1}\). Strict convexity of \(t\mapsto(1+t)^{-1}\)
on \([0,\infty)\), together with nonconstancy of \(G^2\), gives
\(m>(1+EG^2)^{-1}=1/2\). Gaussian integration by parts gives
\[
 E[\arctan(G)(G^3-3G)]
 =E\frac{G^2-1}{1+G^2}=1-2m.
\]
For completeness, the first equality follows by integrating the
Gaussian density derivative in
\(E[G\arctan(G)(G^2-1)]\), then subtracting
\(2E[G\arctan(G)]\). The boundary terms vanish because the factors
have polynomial growth. Thus \(b_3=(1-2m)/\sqrt6\ne0\).

Let \(Z_i=u_i\cdot g\) for a standard input Gaussian \(g\), and put
\(P_i=(Z_i^3-3Z_i)/\sqrt6\). For jointly standard normal variables
of correlation \(\rho\), expansion of
\(Z_i=\rho Z_j+\sqrt{1-\rho^2}G'\) gives
\(E[Z_i^3-3Z_i\mid Z_j]=\rho^3(Z_j^3-3Z_j)\).
The same formula holds at \(\rho=\pm1\) by direct substitution.
Using \(E(G^3-3G)^2=6\), one obtains
\[
 E[P_iP_j]=\Gamma_{ij}^3,
 \qquad E[\phi(Z_i)P_j]=e b_3\Gamma_{ij}^3.
\]
Thus the residuals \(\phi(Z_i)-eb_3P_i\) are orthogonal to every
\(P_j\). Their Gram is positive semidefinite, giving
\(Q_1(0)\succeq e^2b_3^2\Gamma^{\circ3}\).

At each subsequent initialized layer, its three preactivations are
centered jointly Gaussian with the preceding feature Gram as covariance
and a common positive marginal variance \(q\). This is the fixed
forward-query Gaussian initialization rule (Appendix C, Part F, of
`odd_mixture_separation_quantitative/REPORT.md`). Define
\[
 c_q=E[\phi(\sqrt qG)G]/\sqrt q
     =a+(e/q)E[\sqrt qG\arctan(\sqrt qG)]\ge a.
\]
Gaussian conditional expectation shows that
\(\phi(Z_i)-c_qZ_i\) is orthogonal to every \(Z_j\), including
singular covariances. Consequently its feature Gram is at least
\(c_q^2Q\succeq a^2Q\). Applying this twice proves the stated
\(Q_3(0)\) bound.

The older complete theorem at
`studies/mean_field_peeling/three_sample_separated_angle_theorem/PROOF.md`
uses \(a_\delta(1+z)+e\arctan z\), with a large gain
\(a_\delta\). Its initialization margin is already positive at
\(e=0\), because the offset contributes \(\mathbf1\mathbf1^T\).
That proof therefore does not establish the present odd-mixture target.

## 2. Exact obstruction to an affine reference

Oddness permits folding labels: replace \((x_i,y_i)\) by
\((y_i x_i,1)\). The loss, GF and raw GD parameter trajectories do not
change, and absolute pairwise separation is preserved.

At \(e=0\), every network prediction is linear in its input, at every
parameter state. Hence
\[
 f\in\operatorname{ran}\Gamma,
 \qquad v^Tr=-v^Ty\quad(v\in\ker\Gamma).
\]
If \(v^Ty\ne0\), the affine residual norm stays bounded below and its
residual-length clock is infinite. The pairwise condition does not
exclude this situation.

The sharpest example is the equilateral planar triple
\[
 u_1+u_2+u_3=0,\qquad \Gamma_{ij}=-1/2\ (i\ne j),
 \qquad y=(1,1,1).
\]
It is admissible for the closed condition whenever \(\delta\le1/2\)
(and for the strict condition whenever \(\delta<1/2\)). At affine
population initialization \(C_0=0\), every hidden feature sum is zero,
so \(\dot C=0\). All hidden derivatives contain \(C\), so they vanish
as well. The affine population trajectory is exactly stationary with
loss \(3/2\).

The positive initialization Gram in Section 1 shows why this is not a
counterexample to the positive-\(e\) theorem.

## 3. New quantitative obstruction: successful fitting must leave every uniformly bounded state set

This statement holds at every raw parameter state, independently of the
training algorithm. Let \(v\in\ker\Gamma\), so
\(\sum_i v_i x_i=0\). For \(\ell=1,2,3\), define
\[
 S_\ell=\sum_i v_i h_i^\ell,
 \qquad T_\ell=\sum_i v_i\arctan z_i^\ell.
\]
Using \(z_i^2=Ah_i^1\), \(z_i^3=Bh_i^2\), and the activation
identity gives exactly
\[
 S_1=eT_1,\quad S_2=aAS_1+eT_2,
 \quad S_3=e\{a^2BAT_1+aBT_2+T_3\}.                 \tag{1}
\]
The neuron measure is a probability measure, and
\(|\arctan z|\le\pi/2\). Therefore
\[
 \|T_\ell\|_2\le\frac\pi2\|v\|_1,
\]
and Cauchy--Schwarz applied to \(v^Tf=\langle C,S_3\rangle\)
proves
\[
 |v^Tf|\le\frac\pi2 e\|v\|_1\|C\|_2
       \{1+a\|B\|+a^2\|B\|\|A\|\}.              \tag{2}
\]
Both (1) and (2) also hold at finite width with normalized Euclidean
norms and the actual matrices.

For the equilateral equal-label triple take \(v=\mathbf1\). If each
prediction is at least \(1/2\), then (2) implies
\[
 \|C\|_2\{1+a\|B\|+a^2\|B\|\|A\|\}
       \ge\frac1{\pi e}.                              \tag{3}
\]
The same implication holds if the loss is at most \(3/8\): then
\(\|r\|_2\le\sqrt3/2\), and
\(\sum_i f_i=3+\sum_i r_i\ge3-\sqrt3\|r\|_2\ge3/2\).

Assume the canonical initialized action bounds
\(\|A_0\|,\|B_0\|\le10\), and \(C_0=0\). If \(R\) denotes the
raw Hilbert distance from initialization, then
\[
 \|C\|_2\le R,
 \qquad \|A\|,\|B\|\le10+R.
\]
Here the action increments are Hilbert--Schmidt, and their operator
norms are bounded by their Hilbert--Schmidt norms, each at most \(R\).
As \(a\le1\), the left side of (3) is at most
\[
 R\{1+(10+R)+(10+R)^2\}
 \le R(11+R)^2\le(11+R)^3.
\]
Consequently any such fitted state satisfies
\[
 R\ge (\pi e)^{-1/3}-11.                              \tag{4}
\]
This is meaningful for sufficiently small \(e\), and forces
\(R\to\infty\) as \(e\downarrow0\), even while \(\delta\) is held
fixed, for example at \(\delta=1/4\).

If an uncut strong GF exists up to a fitting time \(T\) and has the
usual energy identity, its raw length satisfies
\[
 R\le\int_0^T\|\dot\Theta(t)\|_{\rm raw}\,dt
 \le\sqrt{T\{L(0)-L(T)\}}\le\sqrt{3T/2}.
\]
Together with (4), this yields the conditional lower bound
\[
 T\ge\frac23\big[(\pi e)^{-1/3}-11\big]_+^2.          \tag{5}
\]
This is a lower bound on a successful fitting time, not a proof that
fitting or a global population solution occurs. In particular, a global
odd-mixture proof cannot simply preserve an \(e\)-independent bounded
neighborhood of the stationary affine state and simultaneously prove
small training loss.

## 4. A nonlinear scalar-clock lemma that repairs the primal obstruction in the symmetric case

The following lemma applies to any hidden architecture with a linear
readout, not only the present network. Its conclusions are conditional
on a strong ascent trajectory and the indicated chain rule.

Let \(v\) range over a real Hilbert space of hidden parameters and let
\(H(v)\) be a continuous map into a readout Hilbert space. Assume the
scalar functional \(J\) below is continuously Fréchet differentiable,
satisfies the strong-trajectory chain rule, and has readout gradient
\(\nabla_CJ=H(v)\). The actual network has these scalar and trajectory
properties by Appendix C, Part F, Sections 9--10, of the cited report;
Fréchet differentiability of its vector-valued Nemytskii map on all of
\(L^2\) is not required. Define
\[
 J(v,C)=\langle C,H(v)\rangle,
 \qquad v'=\nabla_vJ,\qquad C'=H(v),\qquad C(0)=0.
\]
Suppose \(H_0=H(v(0))\ne0\). On every interval of strong existence,
the ascent chain rule gives
\[
 J'=\|\nabla_vJ\|^2+\|H(v)\|^2\ge0.
\]
Moreover \(C(s)=sH_0+o(s)\) and
\(J(s)=s\|H_0\|^2+o(s)\). Hence \(J(s)>0\) for small positive
\(s\), and monotonicity makes it positive subsequently. Since
\((\|C\|^2)'=2J\), one has \(\|C(s)\|>0\) for every \(s>0\).
Set
\[
 q(s)=\frac{J(s)}{\|C(s)\|}.
\]
Differentiation, followed by Cauchy--Schwarz, gives
\[
 q'=
 \frac{J'-J^2/\|C\|^2}{\|C\|}
 =\frac{\|\nabla_vJ\|^2+
          \|H(v)\|^2-|\langle C/\|C\|,H(v)\rangle|^2}
        {\|C\|}\ge0.
\]
Since \(q(s)\to\|H_0\|\) as \(s\downarrow0\), it follows that
\[
 J'\ge q^2\ge\|H_0\|^2.                              \tag{6}
\]
Thus, if the trajectory continues until reaching \(J=1\), the first
hitting clock is at most \(S=\|H_0\|^{-2}\). On its portion where
\(J\le1\), ascent energy and Cauchy--Schwarz imply
\[
 \int_0^s\|(v',C')\|\,du
 \le\sqrt{sJ(s)}\le\|H_0\|^{-1}.                    \tag{7}
\]
More precisely, (6) forces a hit by \(S\) if the solution exists
through \(S\); otherwise (7) is an a priori bound up to its existence
endpoint and supplies a strong endpoint in the raw Hilbert space.
It does not supply existence from that endpoint for a merely
continuous, non-Lipschitz infinite-dimensional vector field.

For a symmetric equilateral population trajectory, all three predictions
agree. Take \(H(v)=\frac13\sum_i h_i^3(v)\) and \(J=f_i\).
Symmetry is conditional here on the canonical strong construction or
uniqueness; it is not asserted for arbitrary finite-width samples.
Physical GF is
\[
 \dot\Theta=3(1-J)\nabla J,
 \qquad \dot J=3(1-J)\|\nabla J\|^2.
\]
Whenever the ascent parametrization is valid, (6) gives
\[
 0<1-J(t)\le\exp(-3\|H_0\|^2t),
 \qquad 3\int_0^t(1-J(u))\,du\le\|H_0\|^{-2}.       \tag{8}
\]
At a finite physical time, strict positivity follows by integrating
the scalar equation for \(1-J\), because the strong trajectory has
a bounded continuous gradient on each compact interval.

The initial Gram lower bound gives
\[
 \|H_0\|^2\ge a^4e^2b_3^2s_\delta^2/9.
\]
In the equilateral geometry (1), evaluated at initialization, also gives
\(\|H_0\|\le (\pi/2)e(1+10a+100a^2)\). Thus at fixed separation
the clock certificate \(S=\|H_0\|^{-2}\) has size
\(\Theta(e^{-2})\), and the path bound is \(O(e^{-1})\).

This lemma is a real primal improvement over the stationary affine
comparison for the symmetric triple. It does not prove the generic
three-residual theorem, does not control response tails, and does not
preserve the trained activation regression gap by itself.

## 5. Why the present controlled-source theorem does not finish this route

The old controlled-source lemma requires the actual affine Euler arrays
for the same frozen controls to remain bounded through a fixed clock
\(S\), then imposes an amplitude condition containing
\[
 e\le (2K\exp(KS))^{-1},                              \tag{9}
\]
with \(K\) depending on the fixed affine bounds and \(S\), alongside
other restrictions. That lemma is an affine perturbation statement.

For the symmetric triple the affine path with equal controls is
stationary, but the nonlinear clock from (8) grows as \(e^{-2}\).
Substitution of this clock into (9) is circular. In particular, even
replacing \(K\) by a fixed positive lower bound leaves a sufficient
condition of the form \(e\exp(c/e^2)\le C\), which fails for all
sufficiently small \(e\). Making the activation closer to affine does
not close this particular certificate.

Generic triples present an additional difficulty: label folding does
not create a transitive input symmetry unless the folded off-diagonal
Gram entries all agree. Thus a single scalar objective and the exact
one-dimensional clock of Section 4 do not represent their physical
three-residual dynamics.

## 6. Energy-preserving regularization: what was checked

For any already-existing true strong GF, the exact energy identity
provides a bounded raw path and a strong endpoint at a finite terminal
time. The same argument proves global finite-dimensional GF existence.
The infinite-dimensional missing step is construction or continuation
of the uncut strong field, together with uniqueness and identification
with the full width-sequence limit. Merely continuous Hilbert-space
vector fields do not have a general Peano existence theorem available
in the supplied framework.

The existing incoming-field clips give locally Lipschitz Hilbert
fields, but they are not loss gradients and cannot be assigned the true
energy identity. Two alternative regularizations were checked:

1. Radially clipping each complete raw gradient block preserves
   \(\dot L\le-\|\dot\Theta\|^2\). It does not automatically make
   the field locally Lipschitz. Sample cancellations can make a summed
   gradient small while its derivative still contains an unbounded
   incoming field. The elementary local model
   \(Q[g(z_1)-g(z_2)]\) at \(z_1=z_2\), with unbounded
   \(Q\in L^2\) and bounded smooth \(g\) with \(g'\ne0\), has
   zero value but derivative \(Qg'(z_1)\,dz_1\). Clipping its value
   near zero does not bound that multiplication operator on \(L^2\).
   Thus an additional regularity argument is necessary.
2. Finite-dimensional/Galerkin loss regularization is smooth and
   energy preserving. Its uniform energy bound gives only weak
   compactness and equicontinuity unless a uniform-integrability or
   stronger source estimate is supplied. The nonlinear Nemytskii maps
   and parameter/action products in this model are not automatically
   weakly continuous. An energy bound alone therefore does not justify
   passage to the required strong solution and observable limits.

Neither check rules out a better energy-based proof. They identify the
precise assertion that cannot be silently imported from finite GF.

## 7. Current conclusion and the missing complete route

The full three-input odd-mixture theorem remains open in this research
note. No counterexample to the positive-\(e\) theorem was found.
Pairwise absolute separation does give a uniform positive nonlinear
initialization Gram and removes the exact zero-signal obstruction.
Successful learning in singular directions must nevertheless make a
large excursion as \(e\) decreases, quantified in (4), so it requires
a genuinely nonlinear reference or a new continuation argument.

A complete proof would need, for one \(e_\delta>0\) fixed independently
of the horizon and singular Gram, either:

* a direct source-tail and continuation theorem on arbitrary bounded
  physical intervals, with energy-preserving regularizations and no
  amplitude restriction shrinking to zero as the horizon increases; or
* a nonlinear reference retaining the cubic signal in Gram-null
  directions, with uniform response, cap-removal and trained-law
  nondegeneracy estimates.

In either case one must still prove nonsymmetric strong uniqueness,
reached-state restart, positive activation regression error at every
finite time, and the finite GF/raw-GD, action, kernel, path and velocity
limits. The existing finite-program and compact-reference bridge
results can then be applied with their actual hypotheses checked.
Initialization positivity and the conditional symmetric scalar lemma
do not establish those hypotheses.

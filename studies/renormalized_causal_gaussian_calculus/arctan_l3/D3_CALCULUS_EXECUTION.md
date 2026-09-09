# Depth-three execution of the promoted calculus

**Provenance:** isolated theorem executor; it received only the promoted
rules, the exact D3 equations, and the audited two-colour witness. It had no
repository access and no communication with other agents.

**Date:** 2026-08-24  
**Verdict:** **fail at G2/G4**. The calculus does not currently prove the D3
limit. The failure is exact and occurs at the first middle-backward
multiplier estimate; it is not a counterexample to existence of the width
limit itself.

## Exact point of failure

All elementary compact-time orbit bounds and all readout differences through
\(Q_2\) close. The top multiplier

\[
 \Delta B_3=d(Z_3)\Delta A+widetilde A
   \{d(Z_3)-d(\widetilde Z_3)\}
\]

is handled by current-\(A\) saturation and the immutable Gaussian-mark
Osgood modulus. The next line is

\[
 \boxed{
 \Delta B_2=d(Z_2)\Delta Q_2+widetilde Q_2
   \{d(Z_2)-d(\widetilde Z_2)\}.}                     \tag{1}
\]

The promoted action calculus gives only
\(\|\widetilde Q_2\|_2\) and \(\|\Delta Z_2\|_2\). It gives no
dimension-free control of their product in \(L^2\).

This failure is order one on an abstract \(L^2\) ball. In normalized
coordinates take

\[
 q_n=\sqrt n\,e_1,qquad z_n=0,qquad \widetilde z_n=e_1.
\]

Then \(\|q_n\|_{2,n}=1\),
\(\|z_n-\widetilde z_n\|_{2,n}=n^{-1/2}\), but for
\(d(z)=(1+z^2)^{-1}\),

\[
 \|q_n\{d(z_n)-d(\widetilde z_n)\}\|_{2,n}=1/2.
\]

Thus no width-independent continuity modulus exists on \(L^2\)-bounded
sets.

## Why a fixed \(L^p\) upgrade is insufficient

On a set of empirical mass \(\varepsilon\), take
\(q=\varepsilon^{-1/p}{\bf1}_E\), \(z=0\), and
\(\widetilde z={\bf1}_E\). Then \(\|q\|_p=1\), while with
\(s=\|z-\widetilde z\|_2=\sqrt\varepsilon\),

\[
 \|q\{d(z)-d(\widetilde z)\}\|_2
 =\tfrac12 s^{1-2/p}.                                 \tag{2}
\]

Every finite \(p\) therefore gives only a Hölder modulus with exponent
strictly below one. It is non-Osgood and cannot propagate a zero mesh defect
uniquely. Square uniform integrability without a quantitative rate is also
insufficient.

Moving the full state to \(L^p\) does not solve this abstractly, because a
Gaussian action is not dimension-free on arbitrary source-dependent
\(L^p\) vectors. If \(\Gamma_{ij}=g_{ij}/\sqrt n\) and
\(x_j=g_{1j}\), then \(\|x\|_{p,n}=O(1)\), but

\[
 (\Gamma x)_1=n^{-1/2}\sum_jg_{1j}^2\asymp\sqrt n,
 \qquad \|\Gamma x\|_{p,n}\gtrsim n^{1/2-1/p}.
\]

Any stronger topology must therefore be orbit/source-structural rather than
an unrestricted \(L^p\) Banach replacement.

## The exact missing tail certificate

The source split localizes the issue:

\[
 Q_2=\Gamma_3^*B_3+q_3^*B_3.
\]

The learned rank-one-history term is coordinatewise bounded on compact time,
because it is an integral of bounded \(X_2\) fields with bounded scalar
coefficients. The unresolved term is the **dependent** Gaussian action
\(\Gamma_3^*B_3\).

A sufficient certificate would be a uniform empirical subexponential tail
for this term and the tangent fields it generates, for example

\[
 \tau_T(R):=\sup_{n,\pi,t}
  \|Q_2^\pi(t){\bf1}_{\{|Q_2^\pi(t)|>R\}}\|_2
 \lesssim(1+R)e^{-cR}.                                \tag{3}
\]

Then

\[
 \inf_R\{R s+\tau_T(R)\}\lesssim s\log(e/s),          \tag{4}
\]

which is Osgood and would make (1) stable. No promoted rule proves (3).

## Why finite second response is not yet a solution

The first tangent contains

\[
 DB_2[T]=d(Z_2)T_{Q_2}+d'(Z_2)Q_2T_{Z_2},
\]

whose energy includes
\(n^{-1}\sum_iQ_{2,i}^2T_{Z_2,i}^2\). A fixed moment estimate asks for a
higher tangent moment; differentiating that estimate asks for another. The
second variation contains the same multiplier and products of first
tangents. The audited two-colour word proves that the first such response
energy is generically order one, so it cannot be thrown away. A finite
second-order closure remains a conjecture, not a consequence.

## Consequences for the promotion gates

- Exact finite dynamics, compact orbit bounds, and every fixed Euler-grid
  limit pass.
- Limiting uncut action-IDE well-posedness in the declared state class is not
  certified because (1) lacks an Osgood modulus.
- Dimension-free exact/Euler comparison cannot be invoked.
- The two-mesh UI rule becomes circular because it needs that comparison
  first.
- Uniform integrability and convergence of the middle and bottom raw kernel
  terms are not proved.
- Cutoff removal, physical-time convergence, and elimination of proof-only
  response objects therefore do not follow.

The irreducible missing machinery is a mesh- and time-uniform quantitative
Orlicz/Osgood estimate for dependent two-sided Gaussian actions and their
tangent returns, or an equivalent local response/traffic theorem. This is a
substantial program. It is not “one clever lemma,” and the present calculus
does not spit out the D3 answer.

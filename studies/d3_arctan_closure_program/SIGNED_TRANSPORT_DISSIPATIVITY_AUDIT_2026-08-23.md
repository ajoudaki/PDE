# Signed-transport and dissipativity audit

**Date:** 23 August 2026.

**Verdict:** the arctangent characteristic removes every local amplitude
self-multiplier, but it does not reveal a pathwise contraction.  The residual
top-layer transport is a signed graph Laplacian with genuine positive modes.
Consequently PSD, a uniformly equivalent positive diagonal metric,
gradient-flow monotonicity, or a plain Gaussian log-Sobolev argument cannot
prove the required middle-query tail.  This is a proof-route obstruction, not
a counterexample to the canonical iid-Gaussian trajectory.

## 1. Exact transformed tangent

Suppress layer indices and write the top feature subsystem as

\[
 A'=\phi(z),\qquad z'=Kb,\qquad b=DA,
 \qquad D=\operatorname{diag}d(z),\quad d(z)=(1+z^2)^{-1}.
\]

For a variation \(a=\delta A\), \(v=\delta z\), put

\[
 \eta=D^{-1}v,\qquad \ell=d'/d.
\]

Direct differentiation, with no probabilistic approximation, gives

\[
 a'=D^2\eta,
\]

and

\[
 \boxed{
 \eta'=D^{-1}(\delta K)b+D^{-1}KD\,a
       +D^{-1}{\cal T}_{K,b}(d'\eta),}
 \tag{1.1}
\]

where

\[
 [\mathcal T_{K,b}y]_i
 =\sum_kK_{ik}b_k(y_k-y_i)
 =[K\operatorname{diag}(b)-\operatorname{diag}(Kb)]y_i .
 \tag{1.2}
\]

Also

\[
 \delta b=Da+\operatorname{diag}(b)d'\eta.             \tag{1.3}
\]

Thus the potentially unbounded local coefficient \(A_i d'(z_i)\) cancels
exactly.  Its only amplitude-sensitive survivor is the zero-row-sum signed
transport (1.2).

## 2. Exact quadratic identity and loss of sign

The transport satisfies

\[
 \left\langle by,\mathcal T_{K,b}y\right\rangle_n
 =-\frac1{2n}\sum_{i,k}K_{ik}b_ib_k(y_i-y_k)^2.        \tag{2.1}
\]

Even when \(K\succeq0\), the edge weights \(K_{ik}b_ib_k\) need not be
nonnegative.  For example,

\[
 K=\begin{pmatrix}1&\rho\\ \rho&1\end{pmatrix},
 \qquad b=(-2,1),\qquad 0<\rho<1,
\]

gives

\[
 \mathcal T_{K,b}=\rho
 \begin{pmatrix}-1&1\\-2&2\end{pmatrix},
\]

whose eigenvalues are \(0\) and \(\rho>0\).  Hence the residual transport is
not dissipative.

This cannot be repaired by a uniformly positive diagonal reweighting.  If
\(\Pi=\operatorname{diag}(\pi_i)>0\) symmetrizes the transport, every nonzero
edge must satisfy

\[
 \pi_iK_{ik}b_k=\pi_kK_{ik}b_i.
\]

Thus \(\pi_i/b_i\) is constant on each connected component, which is
impossible when \(b\) changes sign.  Sign changes occur with positive
probability in the canonical Gaussian initialization.

## 3. Why pathwise operator bounds are too strong

For \(\eta=e_k\), an off-diagonal component of the last term in (1.1) is

\[
 [D^{-1}\mathcal T_{K,b}(d'\eta)]_i
 =D_i^{-1}K_{ik}b_kd'_k,\qquad i\ne k.                \tag{3.1}
\]

A large Gaussian output mark \(A_{0,k}=L\), with \(z_k\) in a fixed region
where \(d,d'\asymp1\), makes this coefficient order \(L\), while the
normalized energy remains order one whenever \(L^2\ll n\).  Therefore no
deterministic, width-independent tangent-operator Gronwall estimate follows
from normalized energy and operator norms.  Rare high-amplitude modes may
nevertheless have negligible overlap with a fixed raw Gaussian query, so
this does not falsify the desired annealed logarithmic-moment theorem.

The transformed scalar top subsystem also has the form

\[
 A'=\theta,\qquad \theta'=DKDA=:M(t)A,qquad M(t)\succeq0,
\]

and therefore \(A''=M(t)A\).  At \(z=0\), with a frozen scalar
\(K=\kappa\), the tangent generator has eigenvalues
\(\pm\sqrt\kappa\).  The relevant structure is hyperbolic rather than an
entropy contraction.

## 4. Active Gaussian moment identity

Fix a middle coordinate \(j\), set

\[
 g=\sqrt n\,\Gamma_{2,:,j}\sim N(0,I_n),\qquad
 h=n^{-1/2}g^{\mathsf T}b,qquad J=D_gb,
\]

and define

\[
 S=n^{-1/2}\operatorname{tr}J,qquad
 B=\|b\|_n^2,qquad
 R=n^{-1}g^{\mathsf T}Jb.
\]

Gaussian integration by parts gives, for every even integer \(q\),

\[
 \boxed{
 \mathbb E h^q
 =\mathbb E[Sh^{q-1}]
 +(q-1)\mathbb E[(B+R)h^{q-2}].}                      \tag{4.1}
\]

This identity retains the full same-column response.  Since

\[
 |S|\le\|J\|_{\rm F},\qquad
 |R|\le\|g\|_n\|b\|_n\|J\|_{\rm F},                 \tag{4.2}
\]

the estimate

\[
 \sup_{t\le T}
 \|D_{\sqrt n\Gamma_{2,:,j}}B_3(t)\|_{L^q({\rm F})}
 \le C_Tq,qquad q\le c_T\log n,                     \tag{4.3}
\]

implies \(\|h\|_q\le C_Tq\) by applying Holder to (4.1) and solving the
resulting quadratic inequality.  At time zero, (4.3) holds directly because

\[
 J(0)=\operatorname{diag}\left{
 \frac{X_{2,j}(0)}{\sqrt n}A_{0,i}d'(Z_{3,i}(0))
 \right}.
\]

Thus (4.1) independently confirms the Gaussian-divergence reduction: the
irreducible leaf is the annealed Frobenius response estimate (4.3).

## 5. Consequence for the live proof search

A successful route must preserve cancellation in the signed off-diagonal
transport before taking absolute values.  A plausible organization is to
solve the diagonal hyperbolic blocks exactly, expand only index-changing
off-diagonal insertions, and use time ordering plus Gaussian collision
counting.  The unresolved issue is adaptivity: every transport coefficient
depends on the same raw matrices.  A valid proof therefore needs either an
augmented all-reaching response expansion or a dressed no-self-loop
decoupling lemma.  Plain log-Sobolev merely returns (4.3) as its Lipschitz
constant and does not bypass it.

# Audit: causal Orlicz expansion, restart, and diagonal dressing

## Verdict

The causal response expansion gives a genuine mesh-uniform estimate on one
short time slab.  It does **not** concatenate from a bound on the state or on
the expected coefficient total variation.  At a restart the random boundary
response is multiplied by later curvature marks, and the required joint
moments are not determined by either marginal \(\psi _1\) bounds or signed
first-chaos energy.

The arctangent identity resums every repeated instantaneous diagonal return,
but transfers the problem to the time integral of the signed off-diagonal
bath.  Positive semidefiniteness, normalized energy, and the algebraic neural
form \(\alpha I+GD^2G^*\) do not by themselves control that bath.  These are
route falsifiers, not a counterexample to the canonical iid trajectory.

## 1. What the causal expansion proves locally

For explicit Euler, every strict time edge in a regression-response diagram
carries \(h\).  After expanding a term with \(m\) strict descents, the number
of ordered labels satisfies

\[
 h^m\#\{j<t_m<\cdots<t_1<k\}\le {\tau^m\over m!}
\]

on a slab of length \(\tau\).  If the curvature beads satisfy
\(\|H(t)\|_q\le Lq\), generalized Holder contributes at most factorial
growth.  Consequently the fully typed series is summable for
\(C L\tau<1\), uniformly in the mesh.  In particular, the first slab can be
closed without assuming its own conclusion; the predictable correction is
then sub-Gaussian (hence subexponential) on that slab.

This is a real local result.  Its radius is also real: the simplex factorial
is consumed by the factorial moments of a subexponential curvature mark.

## 2. Exact restart obstruction

At the next slab a response term has the form

\[
 \mathbb E\{H(t_1)\cdots H(t_m)V(t_0,j)\}.
\]

Neither \(\sum_j|\mathbb EV(t_0,j)|\), nor
\(\sum_j\mathbb E|V(t_0,j)|\), nor a marginal \(\psi _1\) estimate for the
state controls these joint quantities.  Restart would require a conditional
Orlicz estimate, a hierarchy of response moments, or a direct invariant
bound for the complete reachable propagator.

The failure already occurs in the scalar causal system

\[
 \delta Z^k=\delta\xi^k+h\sum_{a<k}\delta B^a,
 \qquad \delta B^k=Y\delta Z^k,
 \qquad Y\sim {\rm Exp}(1).
\]

Here every strict edge carries \(h\), the only diagonal bead obeys
\(\|Y\|_q\le q\), and

\[
 c_{kk}=\mathbb EY,
 \qquad
 c_{kj}=h\,\mathbb E\{Y^2(1+hY)^{k-j-1}\}\quad(j<k).
\]

All terms are nonnegative, so for \(h=T/N,k=N\),

\[
 \sum_{j\le k}|c_{kj}|
 =\mathbb E\{Y(1+TY/N)^N\}
 =\sum_{m=0}^N {N\choose m}(T/N)^m(m+1)!.
\]

The limit is \((1-T)^{-2}\) for \(T<1\), and the sequence diverges for
\(T\ge1\).  Thus separately restarting the local estimate would amount to
the false factorization of one exponential moment across consecutive slabs.

## 3. Exact arctangent diagonal resummation

Write one coordinate of the preactivation flow as

\[
 \dot Z_i=K_{ii}B_i+G_i,
 \qquad G_i=\sum_{j\ne i}K_{ij}B_j,
 \qquad B_i=R_i d(Z_i),
\]

and put \(H_i=B_i\rho(Z_i)\), where
\(d(z)=(1+z^2)^{-1}\) and \(\rho=d'/d\).  Then

\[
 K_{ii}H_i={d\over dt}\log d(Z_i)-\rho(Z_i)G_i.
\]

The complete local return therefore has the exact propagator

\[
 \mathcal E_i(t,s)
 ={d(Z_i(t))\over d(Z_i(s))}
 \exp\!\left\{-\int_s^t\rho(Z_i(r))G_i(r)\,dr\right\}.
\]

The naked amplitude has disappeared.  What remains is not harmless:

\[
 |\mathcal E_i(t,s)|
 \le (1+Z_i(s)^2)
      \exp\!\left\{\int_s^t|G_i(r)|\,dr\right\}.
\]

For Euler, Taylor's theorem gives the additional exact-order remainder

\[
 \log d(Z_i^{k+1})-\log d(Z_i^k)
 =hK_{ii}H_i^k+h\rho_i^kG_i^k+\mathcal R_k,
 \qquad
 |\mathcal R_k|\le h^2|K_{ii}B_i^k+G_i^k|^2,
\]

because \(\|(\log d)''\|_\infty\le2\).  A continuum argument must therefore
also control the accumulated discrete remainder.

## 4. Why the neural Gram form is not enough

Let

\[
 K_\varepsilon=
 \begin{pmatrix}1&1-\varepsilon\\1-\varepsilon&1\end{pmatrix}
 =\varepsilon I+(1-\varepsilon){\bf1}{\bf1}^{\mathsf T}.
\]

This is positive semidefinite and has exactly the algebraic form
\(\alpha I+GD^2G^*\).  Take \(R=(Y,-Y)\),
\(Y\sim{\rm Exp}(1)\), and \(Z(0)=(-1,1)\).  Symmetry gives
\(B=(Yd,-Yd)\) and

\[
 \dot Z_1=\varepsilon Yd(Z_1),
 \qquad
 H_1=H_2={2Yx\over(1+x^2)^2}>0,
 \quad x=-Z_1.
\]

For the first row the bath is
\(G_1=-(1-\varepsilon)Yd(Z_1)\), hence

\[
 (\log d(Z_1))'=\varepsilon H_1,
 \qquad -\rho(Z_1)G_1=(1-\varepsilon)H_1.
\]

Almost all of the positive diagonal curvature has merely moved into the
bath.  The corresponding frozen-\(R\) tangent has row sum

\[
 \exp\!\left\{(2-\varepsilon)\int_0^T H(t)\,dt\right\}.
\]

On \(Y\le(2\varepsilon T)^{-1}\), \(x(t)\in[1/2,1]\) and
\(H(t)\ge Y/2\).  Its expectation therefore diverges as
\(\varepsilon\downarrow0\) once the horizon is large enough.  An analogous
Euler example takes \(\varepsilon=h\).

Spectral coercivity does not imply coordinate coercivity: even for fixed
\(\alpha>0\), with \(K=\alpha I+vv^{\mathsf T}\), suitable mixed-sign
\(B\) makes a chosen coordinate of \(KB\) vanish.  For a Gaussian Gram bath,
a leave-one-row calculation gives conditional variance of order one, not a
vanishing perturbation.  Training also destroys automatic conditional
centering through the learned row history.

This example does not establish reachability under the canonical iid
training flow.  It proves that the logarithmic gate identity plus PSD/Gram
structure cannot be the missing theorem.

## 5. Surviving positive leaf

A proof can still use the local causal estimate and the exact diagonal
dressing, but it must add a canonical statement controlling the *invariant
predictable response*, not raw regression coefficient total variation.
One sufficient form is an all-parameter exponential estimate for the
reachable off-diagonal bath integral, stable under both layer switches and
under Euler remainders.  Equivalently, one may prove a covariance/RKHS norm
for the dressed predictable correction that upgrades directly to
\(\psi _1\).  Neither follows from the currently established energy and
positivity bounds.

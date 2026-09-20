# Finite stationary geometry of the canonical three-input p=1 closure

Status: independently derived and frozen candidate, 2026-09-18. This is an
internal mathematical result, not promoted material. No numerical experiment
was run. Scientific inputs were the complete `docs/observable_p1.md`,
`docs/global_nonlinear.md` C.4.7.9, the fixed-dimensional existence statement
C.4.7.10.C.3, and the state, equations and existence portion of
C.4.7.10.D.3. Required research and rigorous-mathematics skills were read.
No other study or another route's findings were read before this freeze.

The main conclusion is an unconditional landscape theorem for the exact
population p=1 system: for three pairwise nonparallel directions, every
positive-loss stationary point in the canonical bounded-displacement state
class is a saddle. All such stationary points with nonzero middle matrix
have a negative second variation. The theorem does not establish that the
particular deterministic canonical trajectory avoids saddles, stays bounded
as time tends to infinity, or converges to zero loss.

## 1. Exact object and state classes

Take three unit vectors \(u_i\in\mathbb R^2\), pairwise nonparallel
(neither equal nor opposite), labels \(y=(1,1,-1)\), and positive masses
\[
 \mu_1=q/2,\qquad \mu_2=(1-q)/2,\qquad \mu_3=1/2,
 \qquad 0<q<1.
\]
The feature-independence and lower-submersion lemmas do not depend on labels.
The loss values and saddle statements below use the displayed nonzero binary
labels and positive masses; no all-zero-label extension is asserted.

Use exactly the active canonical p=1 features, with the source's scalar
constants and ridge \(\eta=1/4096\):
\[
 b_1=\left(h/a,\ (k-\beta h/(v+\eta))/b\right)\in\mathbb R^4,
 \qquad b_2=H/c_*\in\mathbb R^2.
\]
Here \(a,b,c_*\) denote the three positive normalization constants; the
moving readout remains \(c\). Both populations and their full joint mark
laws are the ones in `observable_p1.md`. Constants are removed only by its
proved simultaneous-sign parity invariance. The argument does not diagonalize
the moving matrix or assert rotational invariance of p=1 initialization.

The upper feature law has a strictly positive density on the open square
\((-1/c_*,1/c_*)^2\). The lower feature law has a strictly positive density
on the open set \(S\) obtained by an invertible linear transformation of
\((-1,1)^4\). Indeed, \((G_i,Z_i)\mapsto(h_i,k_i)\) is a smooth
bijection onto \((-1,1)^2\): recover
\(G_i=\operatorname{arctanh}h_i\) and then
\(Z_i=(\operatorname{arctanh}k_i-\alpha h_i)/\sqrt\tau\).
In particular, \(0\in S\), every small ball around zero has positive
density, and \(g\) is a smooth function of \(b_1\) on \(S\).

The moving variables are \(w,c,M\), with the full
\(M\in\mathbb R^{2\times4}\). Write
\[
 \begin{split}
 a_i&=E_1[b_1\tanh(w\cdot u_i)],&z_i&=Ma_i,\\
 h_i^2(b_2)&=\tanh(b_2\cdot z_i),&f_i&=E_2[c h_i^2],\\
 d_i&=E_2[b_2c\operatorname{sech}^2(b_2\cdot z_i)],
 &p_i&=M^Td_i,\qquad R_i=\mu_i(f_i-y_i).
 \end{split}                                                    \tag{1}
\]
The superscript on \(h_i^2\) is a layer label, not a square. The exact
velocities are
\[
 \begin{split}
 \dot w&=-2\sum_iR_i(b_1\cdot p_i)
                  \operatorname{sech}^2(w\cdot u_i)u_i,\\
 \dot c&=-2\sum_iR_i h_i^2,\\
 \dot M&=-2\sum_iR_i d_i a_i^T.
 \end{split}                                                    \tag{2}
\]
These are gradients in the population \(L^2,L^2\) and coefficient
Frobenius metrics, respectively. Thus
\[
 \dot{\mathcal L}=-\|\dot w\|_2^2-\|\dot c\|_2^2
                         -\|\dot M\|_F^2,
 \qquad \mathcal L=\sum_i\mu_i(f_i-y_i)^2.             \tag{3}
\]

Distinguish two domains.

* **Ambient active fields:** the displayed integrals and derivatives exist,
  with fixed canonical feature marginals. Section 3 characterizes the
  displayed active equations without a reachability claim. Outside odd
  parity this is an auxiliary reduced extension, not the unrestricted full
  p=1 model with potentially active constant coordinates.
* **Canonical bounded-displacement class:** \(w-g\in L^\infty\),
  \(c\in L^\infty\), and finite \(M\), with the same joint lower marks,
  and odd \(w,c\) under simultaneous negation of their respective marks.
  Every canonical state at every finite time belongs to this class by the
  fixed-order global existence bounds in the cited sources. The class is
  substantially larger than the set of reached states.

All perturbations constructed below can be chosen odd, so every saddle
statement remains inside the invariant class of the full p=1 model. The
lower-submersion proof also holds without parity for the active equations,
but no unrestricted-full-state classification is inferred from that extension.

## 2. Upper ridge functions: complete independence criterion

**Lemma 1.** For any finite list of at most three vectors \(z_i\), the only
linear relations among \(\tanh(b_2\cdot z_i)\) in upper-population
\(L^2\) are those caused by \(z_i=0\) and by \(z_i=\pm z_j\).

**Proof.** Collapse nonzero vectors into equivalence classes modulo sign and
choose representatives \(\zeta_1,\ldots,\zeta_k\). An almost-sure
linear identity holds on the whole open square, because its left side is
continuous and the density is positive. Choose \(e\in\mathbb R^2\)
outside the finitely many lines where
\(e\cdot\zeta_j=0\) or
\(e\cdot\zeta_j=\pm e\cdot\zeta_l\). Substitution \(b_2=te\)
near zero and the coefficients of \(t,t^3,t^5\) give a Vandermonde
system in the distinct positive numbers \((e\cdot\zeta_j)^2\).
For \(k\le3\), the required tanh coefficients are
\(1,-1/3,2/15\), all nonzero. Its determinant is nonzero, so every
coefficient vanishes. Zero vectors and sign repetitions have exactly the
claimed relations. ∎

Let \(I_0=\{i:z_i=0\}\). On each nonzero class \(C\), write
\(z_i=\epsilon_i\zeta_C\), with \(\epsilon_i\in\{\pm1\}\).
Then \(f_i=\epsilon_i F_C\), where
\(F_C=E_2[c\tanh(b_2\cdot\zeta_C)]\), and
\(d_i=d_C\) on that class. Readout stationarity is exactly
\[
 \sum_{i\in C}\epsilon_iR_i=0
 \quad\Longleftrightarrow\quad
 F_C=\frac{\sum_{i\in C}\mu_i\epsilon_i y_i}
             {\sum_{i\in C}\mu_i}.                       \tag{4}
\]
On \(I_0\), \(f_i=0\), \(R_i=-\mu_i y_i\), and all \(d_i\)
equal \(d_0=E_2[b_2c]\). This exhausts the readout equation; a collinear
but unequal-magnitude pair of upper vectors is independent.

## 3. All ambient stationary conditions

For arbitrary admissible ambient fields, stationarity is equivalent to the
following three conditions, with no rank assumption:
\[
 \begin{cases}
 \sum_{i\in C}\epsilon_iR_i=0&\text{for every nonzero class }C,\\
 \sum_iR_i d_i a_i^T=0,\\
 \sum_iR_i(b_1\cdot M^Td_i)\operatorname{sech}^2(w\cdot u_i)u_i=0
        &\text{almost surely on the lower population.}
 \end{cases}                                                \tag{5}
\]
Necessity is (2) and Lemma 1; sufficiency is direct substitution in (2).
This exact characterization includes all rank-zero and rank-one matrices.
It does not replace the last two equations by the readout condition alone.

It is generally false that the three lower features can vary independently
on the entire ambient space. For example, at \(w=0\), the differential
of \((a_1,a_2,a_3)\) has adjoint kernel
\(\xi_i=\lambda_i v\), where
\(\sum_i\lambda_i u_i=0\) and \(v\in\mathbb R^4\) is arbitrary.
This state lies outside \(w-g\in L^\infty\). Thus a lower
nondegeneracy claim requires the next argument.

## 4. The lower feature differential is onto throughout the canonical class

**Lemma 2.** For every \(w\) with \(w-g\in L^\infty\), the map
\[
 \mathcal A:w\longmapsto(a_1,a_2,a_3)\in\mathbb R^{4\times3}
\]
has a surjective differential on bounded lower perturbations. Equivalently,
if \(\xi_i\in\mathbb R^4\) satisfy
\[
 \sum_{i=1}^3(b_1\cdot\xi_i)
       \operatorname{sech}^2(w\cdot u_i)u_i=0\quad\text{a.s.},       \tag{6}
\]
then every \(\xi_i=0\).

**Proof.** Since the three directions are pairwise nonparallel, their unique
linear dependence \(\sum_i\lambda_i u_i=0\) has every
\(\lambda_i\ne0\). If any \(\xi_i=0\), the remaining two independent
directions force the other two linear forms to vanish almost surely. The
positive density of \(b_1\) on an open set then makes their coefficients
zero.

Suppose all three are nonzero. At almost every mark, (6) gives
\[
 \frac{(b_1\cdot\xi_i)\operatorname{sech}^2(w\cdot u_i)}{\lambda_i}
 =\frac{(b_1\cdot\xi_j)\operatorname{sech}^2(w\cdot u_j)}{\lambda_j}.
                                                               \tag{7}
\]
On a sufficiently small closed ball centered at zero inside \(S\), the
recovered \(g\) is bounded. Because \(w-g\) is essentially bounded,
every lower gate on this ball lies between one common positive constant and
one. Equation (7) therefore implies
\(|b_1\cdot\xi_j|\le C|b_1\cdot\xi_i|\) almost everywhere there.
The two sides are continuous linear-form magnitudes, so positive density
extends this inequality to the whole ball. Consequently the kernel of
\(\xi_i\) is contained in that of \(\xi_j\). Nonzero linear forms
with this property are proportional. Write \(\xi_i=t_i\xi\), with all
\(t_i\ne0\).

After cancelling \(b_1\cdot\xi\), which vanishes on a null hyperplane,
(7) makes every ratio of the three lower gates a positive constant almost
surely. Since
\[
 \log\operatorname{sech}^2s
 =-2|s|+\log4-2\log(1+e^{-2|s|}),
\]
this implies \(\big||w\cdot u_i|-|w\cdot u_j|\big|\) is bounded
almost surely. The bounded displacement then gives the same conclusion for
\(\big||g\cdot u_i|-|g\cdot u_j|\big|\). That random variable is
unbounded: along \(g=tu_i\), its value is
\(t(1-|u_i\cdot u_j|)\), and small open neighborhoods of arbitrarily
large such points have positive Gaussian measure. This contradiction proves
(6) has only the zero solution.

For completeness, let \(J=D\mathcal A\). Its adjoint is the bounded
function displayed in (6). The matrix \(JJ^*\) is positive definite by
the proved injectivity, and
\(J^*(JJ^*)^{-1}\) is a right inverse whose outputs are bounded functions.
Thus the differential is onto even when variations are restricted to
\(L^\infty\). If \(w\) is odd, the gates are even and this right
inverse is odd, as required by canonical parity. ∎

This is pointwise qualitative nondegeneracy. Its least singular value may
tend to zero along an unbounded trajectory; no uniform coercivity has been
assumed or proved.

**Corollary 3: stationary classification in the canonical class.** Here
(5) is equivalent to
\[
 \sum_{i\in C}\epsilon_iR_i=0,\qquad
 R_iM^Td_i=0\quad\text{for every }i,\qquad
 \sum_iR_i d_i a_i^T=0.                                  \tag{8}
\]

The rank cases are exact.

* If \(\operatorname{rank}M=2\), (8) reduces to readout stationarity and
  \(R_i d_i=0\) for every sample; the middle equation is then automatic.
* If \(\operatorname{rank}M=1\), every residual-active \(d_i\) must
  belong to the one-dimensional \(\ker M^T\). Writing those vectors as
  \(d_i=\delta_i n\), the remaining matrix constraint is
  \(\sum_iR_i\delta_i a_i=0\). It cannot be discarded.
* If \(M=0\), every prediction vanishes and \(\mathcal L=1\).
  Stationarity is precisely
  \[
       d_0S^T=0,\qquad S=\sum_i\mu_i y_i a_i,
       \quad\text{equivalently }d_0=0\text{ or }S=0.       \tag{9}
  \]

## 5. Exact singularity test for the full prediction differential

Let \(F=(f_1,f_2,f_3)\) and use the physical block metrics. A vector
\(x\in\mathbb R^3\) annihilates its differential if and only if
\[
 \sum_{i\in C}\epsilon_i x_i=0,\qquad
 x_iM^Td_i=0\ (i=1,2,3),\qquad
 \sum_i x_i d_i a_i^T=0.                                  \tag{10}
\]
This follows by pairing \(x\) with each of the three block variations,
then applying Lemmas 1 and 2. The full prediction differential is singular
exactly when (10) has a nonzero solution. Positive data weights merely
conjugate the associated Gram matrix and do not change singularity.

For rank two, singularity occurs exactly when either a zero upper vector
has \(d_0=0\), or a nonzero sign class of size at least two has
\(d_C=0\). A collision with \(d_C\ne0\) is repaired by the trained
lower block. For rank one, (10) retains the stated transverse matrix
constraint. At \(M=0\), the full differential has rank
\(\operatorname{rank}[a_1\ a_2\ a_3]\) if \(d_0\ne0\), and
rank zero if \(d_0=0\).

## 6. Positive-loss stationary points are saddles

We need one upper-population fact beyond Lemma 1.

**Lemma 4.** Let \(H\) be the span of the current upper ridges. If
\(z_i\ne0\), then
\[
       p(b_2)=(b_2\cdot z_i)\operatorname{sech}^2(b_2\cdot z_i)
                                                               \tag{11}
\]
does not belong to \(H\). If \(z_i=0\), any nonzero linear function
\(p(b_2)=b_2\cdot v\) does not belong to \(H\).

**Proof.** Choose a generic line as in Lemma 1, so the nonzero ridge
arguments have distinct nonzero magnitudes \(|\ell_j|\). Every odd tanh
Taylor coefficient is nonzero: writing
\(\tanh t=\sum_{n\ge0}(-1)^n a_nt^{2n+1}\), the identity
\(\tanh'=1-\tanh^2\) gives \(a_0=1\) and
\((2n+1)a_n=\sum_{k+l=n-1}a_ka_l>0\) for \(n\ge1\).

If (11) were in the ridge span, coefficient comparison would express
\((2n+1)\ell_i^{2n+1}\) as a fixed linear combination of
\(\ell_j^{2n+1}\) for every \(n\ge0\). Put
\(X_j=\ell_j^2\), and apply the shift polynomial
\(P(E)=\prod_j(E-X_j)\) to these sequences. It kills the right side,
but on \((2n+1)X_i^n\) gives
\(2X_i^{n+1}P'(X_i)\ne0\). Contradiction. For a linear function,
the coefficients with \(n=1,\ldots,k\) force all ridge coefficients
to zero by Vandermonde, whereas the coefficient of \(t\) is nonzero
after also choosing the line not perpendicular to \(v\). ∎

**Theorem 5.** In the bounded-displacement canonical class:

1. Every positive-loss stationary point with \(M\ne0\) has a negative
   second variation of the exact physical loss.
2. At a stationary point with \(M=0\), there is a negative second
   variation unless both \(d_0=0\) and \(S=0\). In that exceptional
   case the Hessian is identically zero but there is a cubic descent curve.
3. Consequently every local minimum has zero training loss. These statements
   remain true with variations restricted to the parity-invariant class.

**Proof for \(M\ne0\).** Choose a sample with \(R_i\ne0\). By (8),
\(M^Td_i=0\). If \(z_i\ne0\), set \(v=z_i\); otherwise choose any
nonzero \(v\in\operatorname{im}M\). By Lemma 2 choose a bounded
\(\delta w\) with \(M\delta a_i=v\) and
\(\delta a_j=0\) for \(j\ne i\). Define
\[
 p(b_2)=(b_2\cdot v)\operatorname{sech}^2(b_2\cdot z_i),
 \qquad \delta c=p-\operatorname{Proj}_H p.
\]
Lemma 4 gives \(\|\delta c\|_2>0\). This is a bounded odd function,
orthogonal to every current upper ridge. Along the combined direction
\((\delta w,\lambda\delta c,0)\), all first prediction variations
vanish: the readout variation is orthogonal to every ridge and the only
nonzero first upper-vector variation satisfies \(d_i\cdot v=0\).
The loss second variation therefore has the form
\[
        Q(\lambda)=Q(0)+4\lambda R_i\|\delta c\|_2^2.     \tag{12}
\]
There is no \(\lambda^2\) term, because predictions depend linearly on
the readout and its first variations vanish. The mixed term comes from
\(2E_2[\delta c\,p]\) in the second prediction variation. Choosing a
finite \(\lambda\) of the appropriate sign and magnitude makes (12)
negative. All pure \(w\) second-variation terms are included in finite
\(Q(0)\); none is omitted.

**Proof for \(M=0\).** Let \(A_i=a_i\), and use arbitrary bounded
first variations \(\delta A_i\), available by Lemma 2. Let
\(N=\delta M\), \(m=E_2[b_2\delta c]\), and
\(\delta S=\sum_i\mu_i y_i\delta A_i\). At \(M=0\), direct
differentiation gives
\[
 Q=2\sum_i\mu_i(d_0^TNA_i)^2
       -4m^TNS-4d_0^TN\delta S.                          \tag{13}
\]
Every \(m\in\mathbb R^2\) is available from a bounded odd
\(\delta c\): take
\(\delta c=b_2^T\Sigma^{-1}m\), where
\(\Sigma=E_2[b_2b_2^T]\) is positive definite.

If \(d_0\ne0\), stationarity makes \(S=0\). Choose \(N\) with
\(d_0^TN\ne0\), then scale \(\delta S\) to make (13) negative.
If \(d_0=0\) and \(S\ne0\), choose \(m,N\) with \(m^TNS>0\).
If both are zero, (13) vanishes for every direction. Along
\(w(t)=w+t\delta w\), \(M(t)=tN\), \(c(t)=c+t\delta c\),
Taylor expansion gives
\[
 \sum_i\mu_i y_i f_i(t)
 =t^3\left[m^TN\delta S
       -\frac13\sum_i\mu_i y_i E_2[c(b_2^TNA_i)^3]\right]+O(t^4).
                                                               \tag{14}
\]
The order \(t\) term vanishes by \(d_0=0\), and the order \(t^2\)
term vanishes by \(S=0\). Choose \(m,N\) with \(m^TN\ne0\), then
choose \(\delta S\) so the bracket is positive. All predictions are
\(O(t^2)\), so their squared terms contribute only \(O(t^4)\).
Hence \(\mathcal L(t)=1-Ct^3+O(t^4)<1\) for small positive \(t\),
where \(C>0\). This proves descent even in the zero-Hessian case.
Bounded gates and perturbations justify every Taylor remainder under the
population integrals. ∎

The value zero is attainable in this same class. To see this without an
initial-feature rank assumption, start at \(w=g\) and use Lemma 2 to
prescribe a first variation of \(A=[a_1\ a_2\ a_3]\) that fills any
missing singular directions. In singular-vector coordinates, choose that
variation to put ones in the missing diagonal entries of a three-row
minor and zeros in its existing nonzero diagonal block. Along the resulting
bounded odd perturbation,
\(A(t)=A(0)+t\delta A+O(t^2)\). If \(A(0)\) has rank \(r\), that
minor has determinant a nonzero constant times \(t^{3-r}\), plus
\(O(t^{4-r})\). Hence \(A(t)\) has rank three for small positive
\(t\). Choose a finite \(M\) mapping its columns to
\(e_1,e_2,e_1+e_2\). Lemma 1 makes the three upper ridges linearly
independent, so their Gram is positive definite. Solving that three-by-three
Gram system gives a bounded odd readout in their span with predictions
exactly equal to the three labels. This is an existence construction,
not a claim that canonical gradient flow finds those parameters.

## 7. Stationary loss values for the specified labels

At every ambient stationary state, (4) already fixes the loss. A nonzero
class has signed targets \(\epsilon_i y_i\in\{\pm1\}\). Let
\(P_C,N_C\) be the sums of masses carrying the two signed targets. Its
loss is
\[
       \frac{4P_CN_C}{P_C+N_C}.                           \tag{15}
\]
Each zero-vector sample contributes \(\mu_i\). Thus all stationary
losses belong to a finite explicit set, irrespective of rank. This is a
necessary list; it does not assert that every listed partition is realizable
by a full stationary state.

Every positive value in the list is at least
\(\min_i\mu_i=\min(q,1-q)/2\). For a mixed sign class, both
\(P_C,N_C\) are at least this minimum, and
\(4P_CN_C/(P_C+N_C)\ge2\min(P_C,N_C)\); any nonempty zero subset
already contributes at least the minimum mass.

For three samples the possibilities are:

* singleton nonzero classes contribute zero;
* a zero subset contributes its total mass;
* a nonzero pair contributes either zero or
  \(4\mu_i\mu_j/(\mu_i+\mu_j)\), with a possible additional zero
  singleton contribution;
* one nonzero class containing all three contributes either zero or
  \(4\mu_i(1-\mu_i)\) for one isolated signed target.

For \(q=3/4\), every stationary loss belongs to
\[
 \left\{0,\frac18,\frac38,\frac25,\frac7{16},\frac12,
 \frac58,\frac{31}{40},\frac67,\frac78,\frac{15}{16},
 \frac{55}{56},1\right\}.                               \tag{16}
\]
In particular every positive stationary loss is at least \(1/8\).
The list and the landscape theorem apply to every equilateral rotation;
they use pairwise nonparallel directions, not rotation invariance of the
p=1 dictionary, initializer, trajectory, or loss curve.

## 8. Reachability and unresolved implications

The fixed-order existence proof supplies
\(w(t)-g\in L^\infty\), \(c(t)\in L^\infty\), and finite full
\(M(t)\) on every compact physical-time interval. Therefore Lemma 2,
the differential test (10), and Theorem 5 apply at every reached finite
state. No assumption about future kernel coercivity was used.

Ordinary local uniqueness also implies that a trajectory starting from a
nonstationary point cannot hit any stationary point in finite time: a
constant trajectory through a hit point and the original trajectory would
contradict uniqueness backward on a short interval, and repetition returns
to initialization. This statement is conditional only on initial
nonstationarity; this route has not separately proved that condition for
every possible three-input geometry.

If strict loss descent has occurred, any state with all \(z_i=0\), and
in particular \(M=0\), is excluded from all subsequent reached times,
because those states have loss one. This exclusion does not rule out
rank-one matrices or individual zero/colliding upper vectors.

The missing bridges for a zero-loss theorem remain substantive:

* A deterministic initialization may lie on a saddle's stable set. A
  negative Hessian direction alone does not prove avoidance.
* Compact-time bounded displacement need not be uniformly bounded for all
  time. A limiting raw \(L^2\) state need not retain the Banach class used
  in Lemma 2.
* Strict qualitative surjectivity at every finite state gives no uniform
  lower eigenvalue bound at large times.
* Loss can approach a positive value while parameters escape or the
  differential degenerates asymptotically. The finite stationary-loss list
  does not by itself exclude this.

These limits are compatible with, and do not weaken, the unconditional
finite-state landscape and singularity statements proved above.

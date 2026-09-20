# Finite-input tail route: a degenerate bad equilibrium and scoped extensions

Frozen independent candidate, 2026-09-18. Internally checked theory; not
promoted. No computation or experiment was used. Scientific inputs were
exactly the complete `docs/observable_p1.md`, `dependent_basin_functional.md`,
`dependent_finite_fitting.md`, and `DEPENDENT_BASIN_RESULTS.md`, plus the
supervisor's neutral assignment. No other study or sibling route was read.
The investigate-conjectures and solve-math-rigorously skills and the
research-contract, evidence-ledger, and adversarial-audit process references
were applied. This is the only file written by this route.

The target is the unrestricted physical-Hilbert, point-convergent bad-basin
theorem for any finite equal-weight family of normalized, pairwise
nonparallel inputs, retaining the exact correlated marks and full trainable
matrix. The main result here is an obstruction to its *strict-saddle
premise*, not a counterexample to basin nullity: seven inputs in dimension
three have an exact equilibrium with loss 48/49 and nonnegative second
directional loss variation in every Hilbert direction. A bounded cubic
descent direction exists, so this is not a local minimum. Two separate
restricted basin extensions are given at the end.

## 1. Exact model and the seven inputs

Use the canonical odd marks `b_1 in R^6`, `b_2 in R^3` from
`docs/observable_p1.md`, including their exact correlation with `g`, reverse
response, and ridge 1/4096. Let `phi=tanh`. The state is

\[
 \theta=(w-g,c,M)\in\mathcal H_3
 =L^2_{\rm odd}(\Omega_1;\mathbb R^3)
  \oplus L^2_{\rm odd}(\Omega_2)\oplus\mathbb R^{3\times6}.
\]

All entries of M remain trainable. The choice of a rank-one value for M
below imposes no restriction on the state space or its variations. Put

\[
 a_i=E_1[b_1\phi(w\cdot u_i)],\quad v_i=Ma_i,\quad
 H_i=\phi(b_2\cdot v_i),\quad f_i=E_2[cH_i],\quad
 \rho_i=p_i(f_i-y_i),\quad
 d_i=E_2[b_2c\phi'(b_2\cdot v_i)].
\]

The exact flow is

\[
 \dot w=-2\sum_i\rho_i\phi'(w\cdot u_i)(b_1\cdot M^Td_i)u_i,
 \quad \dot c=-2\sum_i\rho_iH_i,
 \quad \dot M=-2\sum_i\rho_i d_i a_i^T.
 \tag{1}
\]

Choose any `C,S>0` with `C^2+S^2=1`. Let `e_1,e_2,e_3` be the ordinary
coordinate vectors of R3, and write

\[
 u(\alpha)=Ce_1+S(\cos\alpha\,e_2+\sin\alpha\,e_3).
\]

The positive class consists of the three angles
`0,2pi/3,4pi/3`; the negative class consists of the four angles
`pi/8,5pi/8,9pi/8,13pi/8`. Assign every point weight `p_i=1/7`.
All inputs are unit, no angles coincide, and none of the inputs are
antipodal because their first coordinate is the same positive C.
Physical inputs are `x_i=sqrt(3)u_i`.

The classwise averages of both the first and the second moment agree:

\[
 {1\over3}\sum_+u_i={1\over4}\sum_-u_i=Ce_1,
 \qquad
 {1\over3}\sum_+u_iu_i^T={1\over4}\sum_-u_iu_i^T
 =C^2e_1e_1^T+{S^2\over2}(e_2e_2^T+e_3e_3^T).
 \tag{2}
\]

These identities follow by summing the roots of unity at powers one and
two in each regular polygon. In the formulas below the common prediction
will be `m=-1/7`; consequently

\[
 \rho_i=-8/49\quad(i\in+),\qquad
 \rho_i=6/49\quad(i\in-).
\]

Equation (2) gives exactly

\[
 \sum_i\rho_i=0,\qquad \sum_i\rho_i u_i=0,\qquad
 \sum_i\rho_i u_iu_i^T=0.\tag{3}
\]

## 2. An exact positive-loss equilibrium

Let `q in R^6` select the normalized `h_1=tanh G_1` lower coordinate;
thus `q dot b_1=h_1/a_0`, where `a_0=sqrt(v+eta)>0` is the canonical
normalization constant. Set

\[
 \epsilon=\operatorname{sign}(q\cdot b_1),\qquad
 A=E_1[b_1\epsilon],\qquad \kappa=q\cdot A=E_1|q\cdot b_1|>0.
\]

The zero-sign event has probability zero. Choose `a>0` and define

\[
 w=a\epsilon e_1,\qquad M=e_1q^T,\qquad t=\phi(aC),
 \quad v=t\kappa e_1,\quad H=\phi(t\kappa b_{2,1}),
 \quad K=E_2H^2>0,\quad c={m\over K}H,\quad m=-1/7.
 \tag{4}
\]

The fields w,c are bounded and odd. The displacement `w-g` is square
integrable but not essentially bounded. This state belongs to the exact
physical Hilbert space, while lying outside the bounded-displacement
endpoint class of the earlier tail theorem.

For every input, `w dot u_i=aC epsilon`, so

\[
 a_i=tA,\qquad v_i=v,\qquad H_i=H,\qquad f_i=m.
\]

All `d_i` therefore equal a common vector d. The readout and matrix
equations in (1) vanish by `sum rho_i=0`. The lower derivative gate is
the same number `s=phi'(aC)>0` at every input and lower mark. Thus the
lower equation is `-2s(b_1 dot M^Td)sum rho_i u_i=0`, by (3).
This verifies every block of stationarity.

The loss is

\[
 L={1\over7}\left[3(-8/7)^2+4(6/7)^2\right]
   ={48\over49}=1-m^2\in(0,1).\tag{5}
\]

Moreover each individual coefficient `T_i=rho_i M^Td_i` is nonzero.
Indeed, symmetry and independence of the canonical upper coordinates give
`d=d_1e_1`, and

\[
 d_1={m\over K}E_2[b_{2,1}\phi(t\kappa b_{2,1})
                         \phi'(t\kappa b_{2,1})]<0.
 \tag{6}
\]

The expectation is strictly positive because `t kappa>0`, the derivative
gate is positive, and `b_{2,1}` has nonzero probability away from zero.
Hence `M^Td=d_1q!=0`. This also disproves individual critical-coefficient
cancellation for unrestricted equal-weight finite-input Hilbert endpoints.

## 3. Every second directional variation is nonnegative

Consider an arbitrary physical Hilbert direction
`(h,k,N) in H_3` and the straight path `(w+lambda h,c+lambda k,M+lambda N)`.
Primes in this section mean derivatives at `lambda=0`.
Let

\[
 B=E_1[b_1h^T],\quad a_*=tA,\quad
 v_0=Na_*,\quad V=sMB.
\]

Because `phi'(w dot u_i)=s` and
`phi''(w dot u_i)=epsilon phi''(aC)`, differentiation gives

\[
 a_i'=sBu_i,\qquad
 a_i''=\phi''(aC)E_1[b_1\epsilon(h\cdot u_i)^2],
\]
\[
 v_i'=v_0+Vu_i,\qquad v_i''=2Na_i'+Ma_i''.\tag{7}
\]

These second derivatives exist for every h in L2: bounded marks and bounded
scalar second derivatives dominate the Taylor remainder by a constant times
`|h|^2`, which is integrable. The upper functions depend on finite vectors;
all their derivatives are bounded functions of upper marks on this finite
path. Pairing with c,k in L2 is legitimate by Cauchy--Schwarz.

Applying (3) to (7) gives

\[
 \sum_i\rho_i v_i'=0,\qquad
 \sum_i\rho_i v_i''=0,\qquad
 \sum_i\rho_i v_i'(v_i')^T=0.\tag{8}
\]

For the second identity, the only possibly nontrivial lower term is
`E[b_1 epsilon h^T(sum rho_i u_i u_i^T)h]`, which vanishes pointwise.
For the third, expand `(v_0+Vu_i)(v_0+Vu_i)^T` and use all three
identities in (3).

The second prediction variation is

\[
 f_i''=2E_2[k\phi'(b_2\cdot v)(b_2\cdot v_i')]
 +E_2[c\phi''(b_2\cdot v)(b_2\cdot v_i')^2]
 +E_2[c\phi'(b_2\cdot v)(b_2\cdot v_i'')].
\]

Each residual-weighted sum on the right vanishes by (8). Therefore

\[
 D^2_{\rm dir}L[(h,k,N),(h,k,N)]
 =2\sum_i p_i(f_i')^2+2\sum_i\rho_i f_i''
 =2\sum_i p_i(f_i')^2\ge0.\tag{9}
\]

This checks arbitrary matrix directions, arbitrary readout directions and
their mixed terms, not merely a restricted lower-field slice. There is no
negative fixed-direction curvature anywhere in the physical tangent space.
Equation (9) is a directional assertion; it does not assert a second Frechet
differential on H. In particular, it supplies no unstable eigenvalue for
the strict-saddle trapping argument.

## 4. A cubic descent direction: not a bad local minimum

Set `aC=1/4`, so `phi'''(aC)!=0` and in fact it is negative, since
`phi'''(z)=2 sech^2(z)(3 tanh^2(z)-1)` and `tanh(1/4)<1/4`.
Choose `b>0` with `P(|G_2|<=b)=1/4`, and put

\[
 \psi=\mathbf1_{\{|G_2|\le b\}}-1/4,
 \qquad \eta=\epsilon\psi,\qquad h=\eta e_2,
 \qquad k=0,\qquad N=0.\tag{10}
\]

This is a bounded odd direction. Canonical *coordinate-pair* independence
and the exact correlation within each pair imply `E_1[b_1 eta]=0`:
the coordinate-one entries factor against `E psi=0`; every other entry
factors against `E epsilon=0`. No independence of b_1 and g is used.
Consequently `a_i'=v_i'=f_i'=0` for every i. Furthermore

\[
 E_1[(q\cdot b_1)\eta^3]
 =\kappa E\psi^3={3\kappa\over32}>0.\tag{11}
\]

The third input moment in the e2 direction is

\[
 \sum_i\rho_i(u_i\cdot e_2)^3
 =-{8\over49}S^3\sum_{j=0}^2\cos^3(2\pi j/3)
 =-{6S^3\over49}<0;\tag{12}
\]

the square contributes zero by antipodal pairing of its transverse angles.
Along (10), `phi'''(w dot u_i)=phi'''(aC)`, and all upper third-chain-rule
terms involving `v_i'` vanish. Thus

\[
 {d^3\over d\lambda^3}L(\theta+\lambda(h,0,0))\big|_{0}
 =2d_1\phi'''(aC)\,{3\kappa\over32}
                  \left(-{6S^3\over49}\right)<0.\tag{13}
\]

Every derivative here is justified by bounded perturbations and bounded
marks. Since the first and second derivatives vanish, Taylor expansion gives
strictly smaller loss for sufficiently small positive lambda, and strictly
larger loss for sufficiently small negative lambda. The equilibrium is a
degenerate saddle with a cubic descent direction.

This neither proves nor disproves a positive-measure attraction basin.
For gradient flows a higher-order descent direction by itself supplies no
replacement for the nonzero unstable linear subspace used in the existing
graph proof. The basin of this specific state and the union of all such
degenerate endpoint basins remain open in this route.

## 5. Bounded-displacement extension with several independent relations

Here is a separate proved family beyond global input-kernel dimension one.
Partition the inputs into finitely many nonempty sets `J_1,...,J_k` such
that their spans `W_l=span{u_i:i in J_l}` form a direct sum and, within
each block, the column matrix has kernel dimension at most one. Orthogonality
of the spaces is not required. Assume the endpoint displacement `w_*-g`
is essentially bounded.

At lower stationarity, apply the linear projection onto W_l along the sum
of the other block spans. This gives, separately for each l,

\[
 \sum_{i\in J_l}\phi'(w_*\cdot u_i)(b_1\cdot T_i)u_i=0.
\]

The complete one-relation cancellation lemma in
`dependent_basin_functional.md`, Section 2, applies to this equation in the
original Gaussian carrier and yields `T_i=0` for all i in J_l. It requires
only the stated within-block kernel bound, pairwise nonparallel normalized
inputs, and bounded displacement; upper and matrix stationarity are not
used. Doing this for every block gives every `T_i=0`.

The finite-family negative-curvature proof in that source's Section 7 needs
bounded displacement and `M!=0`, but no input-kernel restriction. At an
endpoint with `0<L<1`, the condition `M!=0` is automatic. Its Hilbert
remainder estimate, finite-rank spectral splitting and full basin argument
therefore apply verbatim, with rank at most `(3d+1)m+2d^2`.

Consequently the basin of these positive-loss bounded-displacement endpoints
has a countable closed Lipschitz-hypersurface hull, is meagre, and has a shy
Borel hull annihilated by the specified translated/scaled full-support
Gaussian field randomization. Arbitrary positive data weights are allowed.
For example, k nonparallel dependent triples in independent two-dimensional
planes give `m=3k`, `d=2k`, and global input-kernel dimension k. This is an
endpoint-restricted result, not the unrestricted finite-m conclusion.

## 6. A full-support conditional-mark criterion

A second sufficient endpoint condition works for every finite input count
and every dependence pattern, but is not known to follow from the physical
flow or from bounded displacement. Let the law of `w_*` have support all of
R^d and assume that the exact conditional *second-moment* matrix

\[
 Q(s)=E_1[b_1b_1^T\mid w_*=s]
\]

is positive definite for the law of `w_*` almost every s. This statement
retains, rather than replaces, the correlations of the canonical carrier.
At lower stationarity define the matrix

\[
 B(s)=\sum_i\phi'(s\cdot u_i)u_iT_i^T.
\]

The equation is `B(w_*)b_1=0`. Its squared conditional expectation gives
`tr(B(s)Q(s)B(s)^T)=0`, hence `B(s)=0` almost everywhere for the law of w.
Continuity and full support yield `B(s)=0` for all s. Choose a vector e for
which the finitely many `|e dot u_i|` are distinct and nonzero. Along
`s=te`, multiply by the exponential corresponding to the smallest slope
and let t tend to infinity. The identity
`sech^2(at)=4 exp(-2|a|t)(1+o(1))` forces `u_iT_i^T=0` for that index,
so `T_i=0`. Remove it and repeat. Thus every coefficient cancels.

Full support of w also supplies strict negative curvature at every positive
loss endpoint with `M!=0`: each residual-group function
`R_J(s)=sum_(i in J)rho_i phi'(s dot u_i)u_i` with a nonzero coefficient
is a nonzero analytic function by the same line argument. It is nonzero on
some open set and hence with positive w probability. The bounded mixed
variation construction in the assigned functional report then produces
negative curvature, without using bounded displacement. The coefficient
cancellation supplies its Hilbert Frechet remainder estimate. The same
countable-graph basin theorem follows for this endpoint class.

Neither premise is automatic. In the counterexample (4), w has two-point
support. Even at canonical `w=g`, the conditional Q has rank at most d+1,
because the h coordinates are fixed after conditioning on g and only the
d reverse coordinates retain randomness. For d>1 that does not meet
positive definiteness in R^(2d). This criterion is therefore a genuinely
additional endpoint hypothesis, not an established property of initialized
or convergent trajectories.

## 7. Claim status and missing implications

| Claim | Status | Reason |
|---|---|---|
| Every finite equal-weight bad H equilibrium is a strict saddle | Falsified | Exact seven-input state (4), loss (5), nonnegative variation (9) |
| Every such equilibrium has individual `T_i=0` | Falsified | Equation (6) makes every T_i nonzero |
| The seven-input state is a local minimum | Falsified | Bounded cubic descent (10)--(13) |
| Its basin has positive probability | Open | No basin-volume assertion follows from cubic descent or PSD directional curvature |
| Full finite equal-weight bad-point-basin nullity | Open | Degenerate endpoints need a new trapping/nullity mechanism |
| Several direct-sum relation blocks, bounded lower endpoint displacement | Proved conditional endpoint theorem | Blockwise cancellation plus complete existing finite-family graph argument |
| Arbitrary finite dependence with full support and conditional Q positive definite | Proved conditional endpoint theorem | Conditional squared identity, gate separation, mixed negative curvature |
| Bounded displacement alone handles arbitrary relation patterns | Open in this route | Joint b,g tail correlations prevent treating coefficient size as independent of a Gaussian tail event |

The example refutes a proof premise, not the user's entire desired theorem.
It uses the actual physical space, exact canonical mark laws, equally
weighted distinct normalized inputs, the full trainable matrix, and all
state directions. Its only special choice is a legitimate ambient endpoint.
It is not asserted reachable from canonical initialization or from a set of
positive probability. No result here establishes state convergence,
excludes escape, or locates the deterministic canonical initial state
relative to a null set.

## 8. Comparison exposure and bounded followup

Sections 1--7 were completed and frozen before receiving any sibling result.
Afterward the supervisor reported that another independently frozen route
found the same latitude moment-matching obstruction. The supervisor also
provided a different readout construction imposing `E c H=m` and
`E c J=0`, where `J(B)=B phi'(zB)`, `B=b_(2,1)`, and
`z=kappa phi(s_0)>0`. This makes every d_i zero and is assigned to the
other route; it is not part of this report's independent candidate.

The following is a post-comparison higher-order check for that construction.
It removes any need to guess the third derivative of a particular
two-function projected readout. Put `s_0=aC>0` and define the bounded odd
upper function

\[
 K_3(B)=\left.{d^3\over ds^3}\phi(\kappa B\phi(s))\right|_{s=s_0}.
\]

The three functions `H=phi(zB)`, J, and K_3 are linearly independent in
the actual upper L2 law. To verify this, an a.s. analytic identity extends
from an interval of positive upper density to all real B. If
`K_3=A H+D J`, the positive-infinity limit forces A=0. The third chain
rule gives

\[
 K_3=\kappa^3\phi'(s_0)^3 B^3\phi'''(zB)
 +3\kappa^2\phi'(s_0)\phi''(s_0)B^2\phi''(zB)
 +\kappa\phi'''(s_0)B\phi'(zB).
\]

Since `phi'''(zB)=16 exp(-2zB)(1+o(1))`, division by
`B^3 exp(-2zB)` gives a nonzero limit for K_3 and zero for D J.
This is a contradiction. The same constant-limit and exponential
comparison proves independence of H and J. All three functions are
bounded on the actual compact upper-mark support and odd.

Their positive-definite 3-by-3 Gram therefore yields a bounded odd readout
c satisfying exactly

\[
E_2[cH]=-1/7,\qquad E_2[cJ]=0,\qquad E_2[cK_3]=1.
\]

The coordinate-sign symmetry of the actual upper law makes every component
of d transverse to e1 zero, and its e1 component is `E c J=0`. Thus all
d_i and all T_i vanish. The stationarity verification and loss calculation
in Section 2 still apply. The regular-endpoint estimates (13)--(16) of
`dependent_basin_functional.md` use only `T_i=0` at their center and
bounded marks, not bounded lower displacement once cancellation has been
obtained. They give a genuine Frechet derivative of the physical field
here, with a remainder having O(r) Lipschitz constant on H-balls of radius
r. Consequently the loss has an H Frechet Hessian at this equilibrium.

For every direction `(h,k,N)`, the first prediction variation is now simply
`Df_i[h,k,N]=E_2[kH]`, since d_i=0. The residual second derivative still
vanishes by the complete calculation (7)--(8). Hence the actual Hessian is

\[
 D^2L[(h,k,N),(h,k,N)]=2(E_2[kH])^2,\qquad
 D^2L(h,k,N)=2\langle k,H\rangle(0,H,0).
\]

It is positive semidefinite of rank one. The flow derivative has exactly
one nonzero eigenvalue, `-2K<0`, and zero on the orthogonal complement of
`(0,H,0)`. There is no positive linearized flow eigenvalue. This strengthens
the original independent candidate's directional obstruction to a regular
Hilbert equilibrium with a verified Hessian.

Keep the lower state and matrix from (4), and vary only the bounded odd
lower field in direction `h=epsilon e_2`. The predictions then have the
exact scalar form

\[
 f_i(\lambda)=F(s_0+\lambda S\cos\alpha_i),\qquad
 F(s)=E_2[c\phi(\kappa B\phi(s))].
\]

Here `F(s_0)=-1/7`, `F'(s_0)=0` and `F'''(s_0)=1`.
The residual moment identities give `L'(0)=L''(0)=0` and

\[
 L'''(0)=2\sum_i\rho_i(S\cos\alpha_i)^3
 =-{12S^3\over49}<0.
\]

Thus the d_i=0 variant can be chosen to have a verified cubic descent
direction as well. This remains a proof-premise obstruction, not a
basin-probability counterexample. The supplied regular-endpoint remainder
estimate applies to this d_i=0 variant; any complete theorem about its
basin still needs an argument for a degenerate endpoint with no unstable
linear subspace.

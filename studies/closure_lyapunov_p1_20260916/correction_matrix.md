# An initialized interpolation correction and its actual decay defect

2026-09-16. Independent scoped analytic route, frozen before comparison.
No experiment, additional state variable, or promotion is used.

**Result and gap.** The formula (4) below is a new, nonsingular current-state
matrix extension of the normalized-readout potential. It uses the initialized
readout interpolation cost, present predictions, and present readout norm.
It does not invert the evolving tangent Gram, and its exact derivative does
not contain a derivative of that Gram. Its normalization is chosen by checking
the actual flow decay defect: the first natural matrix normalization gives the
wrong second-order sign at initialization; the corrected normalization repairs
that sign exactly. The complete first/second trained defect expansion is
given below. The resulting potential has a proved all-time exponential
inequality on every exact symmetric seed, and in open nonsymmetric input
neighborhoods of every unit-label seed whose fitting endpoint has full tangent
rank. The latter endpoint hypothesis is the already identified good-set
condition; this route has **not** proved it on a broader unit-label rho range.
Thus the requested broader theorem remains open, despite an actual new
potential and a verified decay-defect correction.

Inputs read in full within the assigned scope: `docs/NOTATION.md`,
`docs/observable_p1.md`, `docs/global_nonlinear.md` C.4.7.9 and
C.4.7.10 B/C.1/D.3, and this study's `three_coordinate_candidate.md`,
`perturbation_modes.md`, `perturbation_metric_template.md`,
`sphere_second_variation.md`, and `rho_endpoint_extension.md`.
References to other study reports were not followed. The
investigate-conjectures and solve-math-rigorously skills and the former's
contract, evidence, and adversarial-audit references were applied.

## 1. Exact model and finite initialized interpolation geometry

Keep the canonical d=3 p=1 Gaussian populations, eta=1/4096, correlated
lower marks, initialized matrix D, all evolving entries of M, the actual
transpose M^T, and the population-L2/Frobenius metric of the candidate.
Absorb labels (1,1,-1) into the unit inputs, so every target is one. Write

\[
 n=\mathbf1/\sqrt3,\quad p=(f(v_1),f(v_2),f(v_3))^T/\sqrt3,
 \quad r=p-n,\quad L=|r|^2,\quad q=E_2c^2.
\tag{1}
\]

The full normalized tangent Gram is

\[
 K_{ij}=\tfrac13\left\{E_2H_iH_j
 +(d_i\cdot d_j)(a_i\cdot a_j)
 +(v_i\cdot v_j)E_1[g_i g_j Q_iQ_j]\right\},
\tag{2}
\]

where a_i, H_i, d_i, Q_i and g_i=sech^2(w.v_i) are the exact canonical
fields. In particular Q_i=b_1^TM^Td_i. The physical equations imply

\[
 p'=-2Kr,\qquad L'=-4r^TKr,\qquad q'=-4r^Tp.
\tag{3}
\]

Let the frozen initialized readout feature map be
H_0 z=sum_i z_i H_i(0)/sqrt(3), and set Gamma_0=H_0^*H_0.
This matrix is positive definite at every noncoincident symmetric triple
in the assigned rho family, including rho=-1/2, by the candidate's rank-three
initialization theorem. It remains positive definite in an open input
neighborhood of each such triple. Restrict this construction to the open
set of data where Gamma_0>0.

Define C_0=n^T Gamma_0 n and

\[
 \mu_0=(n^T\Gamma_0^{-1}n)^{-1}>0,\qquad
 S=\Gamma_0+pp^T,\qquad
 \Phi_{\rm mat}=L+\mu_0(1+q)r^TS^{-1}r.
\tag{4}
\]

The number mu_0 is the reciprocal minimum squared readout norm needed to
fit the three labels using the initialized features. Indeed
c_0^*=H_0 Gamma_0^{-1}n obeys H_0^*c_0^*=n and has squared norm
n^T Gamma_0^{-1}n. Any other feasible c differs from c_0^* by an element
of ker H_0^*, orthogonal to c_0^*. Expanding the squared norm proves the
minimum. This is an initialized Gaussian integral and finite linear algebra
calculation, not a future interpolating endpoint.

Since S>=Gamma_0>0, (4) is finite at every finite current state for those
data, even if the current readout Gram or full tangent Gram becomes singular.
It uses only present predictions, present q, and frozen initialized
integrals. In particular it is restartable from the saved population state.
It obeys L<=Phi_mat, and at initialization

\[
 \Phi_{\rm mat}(0)=1+\mu_0 n^T\Gamma_0^{-1}n=2.
\tag{5}
\]

At symmetric data, p=Fn and Gamma_0=C_0 nn^T+nu_0(I-nn^T), nu_0>0.
Then mu_0=C_0, r=-(1-F)n, and (4) is exactly the old potential
L[1+C_0(1+q)/(C_0+F^2)]. Thus the candidate proves, on every exact
symmetric initialized trajectory, Phi_mat'<=-4C_0 Phi_mat and
L<=Phi_mat<=2L. The parameter mu_0 is fixed in physical time, but changes
with the dataset.

## 2. Exact physical decay defect and why the normalization matters

Put R=S^{-1}, and introduce only for this calculation

\[
 u=r^TRr,\quad v=p^TRr,\quad a=r^TRKr,\quad
 b=r^Tp,\quad k=r^TKr.
\]

Differentiating S using (3) gives

\[
 S'=-2(Krp^T+pr^TK),\qquad
 R'=2R(Krp^T+pr^TK)R,
\]
\[
 u'=-4a+4av=-4(1-v)a.
\]

Consequently the complete derivative and defect at any fixed rate lambda
are

\[
 \Phi_{\rm mat}'=-4k-4\mu_0\{(1+q)(1-v)a+bu\},
\tag{6}
\]
\[
 \mathscr D_\lambda:=\Phi_{\rm mat}'+\lambda\Phi_{\rm mat}
 =-4k+\lambda L+
 \mu_0\{-4(1+q)(1-v)a-4bu+\lambda(1+q)u\}.
\tag{7}
\]

Every entry in (6)--(7) is a current-state contraction. No K' estimate has
been omitted: none occurs for this metric. Positive semidefiniteness of K
alone does not determine the sign of a=r^TRKr, because R and K need not
commute. Nor does it determine the sign of the combined expression (7).

There is a concrete reason for using mu_0 rather than the initially more
obvious C_0 in (4). At initialization p=q=0, r=-n, K=Gamma_0. Hence

\[
 \Phi_{\rm mat}'(0)=-4(C_0+\mu_0),\qquad
 \mathscr D_{4\mu_0}(0)=-4(C_0-\mu_0)\le0.
\tag{8}
\]

To see the last inequality and its perturbative meaning, choose an
orthonormal 3-by-2 matrix E with E^Tn=0, and write

\[
 \Gamma_0=\begin{pmatrix}C_0&\beta_0^T\\\beta_0&D_0\end{pmatrix}
 \quad\hbox{in the basis }(n,E).
\]

Block elimination gives exactly

\[
 \mu_0=C_0-\beta_0^TD_0^{-1}\beta_0.
\tag{9}
\]

Thus (8) is -4 beta_0^T D_0^{-1} beta_0. At a symmetric seed beta_0=0,
D_0=nu_0 I, and along an input perturbation beta_0=epsilon beta_1+O(epsilon^2),

\[
 \mathscr D_{4\mu_0}(0)
 =-\frac{4\epsilon^2}{\nu_0}|\beta_1|^2+O(\epsilon^3).
\tag{10}
\]

Both first variation and the sign of this second variation concern the
actual decay defect. In contrast, using C_0 in place of mu_0 would give
initial value 1+C_0/mu_0 and

\[
 \mathscr D^{\rm naive}_{4C_0}(0)
 =4C_0(C_0/\mu_0-1)\ge0,
\]

strictly positive whenever beta_0 is nonzero. The interpolation normalization
repairs this particular second-order defect, while preserving Phi(0)=2.
It does not by itself prove (7)<=0 later in training.

## 3. The actual added terms near a symmetric seed

Write p=Fn+E zeta, e=1-F, d=C_0+F^2. Thus L=e^2+|zeta|^2. In the
same basis as above,

\[
 S=\begin{pmatrix}d&h^T\\h&T\end{pmatrix},\qquad
 h=\beta_0+F\zeta,\quad T=D_0+\zeta\zeta^T,
 \quad B=T-hh^T/d>0.
\]

Solving the block linear system gives

\[
 r^TS^{-1}r=\frac{e^2}{d}
 +(\zeta+eh/d)^TB^{-1}(\zeta+eh/d).
\tag{11}
\]

This inverse is of the positive, frozen-initialization-augmented matrix S,
not the evolving tangent Gram. Formula (11) is only a transparent expansion
of the globally regular expression (4).

Let Phi_old=L[1+C_0(1+q)/d], using the perturbed dataset's own C_0.
Their difference is exactly

\[
 \Phi_{\rm mat}-\Phi_{\rm old}
 =(1+q)\left\{
 \mu_0(\zeta+eh/d)^TB^{-1}(\zeta+eh/d)
 -\frac{C_0|\zeta|^2}{d}
 +\frac{(\mu_0-C_0)e^2}{d}\right\}.
\tag{12}
\]

The correction need not be nonnegative, but the complete potential is
positive and loss controlling by (4). On each fixed finite horizon, let
zeta=epsilon zeta_1+O(epsilon^2) and beta_0=epsilon beta_1+O(epsilon^2).
In the following coefficient use the symmetric base values F,q,C_0 and
nu_0, and put

\[
 P=\frac{C_0+F}{d},\qquad H=\frac e d,\qquad
 Z=P\zeta_1+H\beta_1.
\]

The exact second-order correction coefficient is

\[
 \Phi_{\rm mat}-\Phi_{\rm old}
 =\epsilon^2\mathcal Q+O_T(\epsilon^3),
\]
\[
 \mathcal Q=(1+q)\left\{
 C_0\left(\frac{|Z|^2}{\nu_0}-\frac{|\zeta_1|^2}{d}\right)
 -\frac{e^2|\beta_1|^2}{d\nu_0}\right\}.
\tag{13}
\]

Indeed B^{-1}=nu_0^{-1}I+O_T(epsilon), mu_0-C_0
=-epsilon^2|beta_1|^2/nu_0+O(epsilon^3), and
zeta+eh/d=epsilon Z+O_T(epsilon^2). These identities give (13)
without assuming that the mean observables lack first variations.
Their first-order changes multiply already quadratic terms and affect
only the next order. At initialization zeta_1=F=q=0, and the two beta_1
terms cancel: Q(0)=0, as required by (5).

For an explicitly dynamical version, use the mode note's complete first
response

\[
 \zeta_1'=2e b_1-2\nu\zeta_1,\qquad
 b_1=\partial_\epsilon(E^TK n)|_0,\quad E^TKE=\nu I
 \quad\hbox{on the symmetric base}.
\tag{14}
\]

Here b_1 includes the first response of w,c,M and of the input directions;
it is not an externally imposed forcing. beta_1 is constant in physical
time. With k_mean=n^TKn,

\[
 F'=2e k_{\rm mean},\quad q'=4eF,\quad d'=4eF k_{\rm mean},
\]
\[
 P'=\frac{2e k_{\rm mean}(C_0-2C_0F-F^2)}{d^2},\qquad
 H'=-\frac{2e k_{\rm mean}}d-\frac{4e^2F k_{\rm mean}}{d^2},
\]
\[
 Z'=P'\zeta_1+P(2e b_1-2\nu\zeta_1)+H'\beta_1.
\tag{15}
\]

If
J=C_0(|Z|^2/nu_0-|zeta_1|^2/d)-e^2|beta_1|^2/(d nu_0), then

\[
 \begin{split}
 \mathcal Q'+\lambda\mathcal Q
 ={}&[4eF+\lambda(1+q)]J\\
 &+(1+q)\left\{
 \frac{2C_0 Z\cdot Z'}{\nu_0}
 -\frac{2C_0\zeta_1\cdot\zeta_1'}d
 +\frac{C_0|\zeta_1|^2d'}{d^2}
 +\frac{|\beta_1|^2}{\nu_0}
       \left(\frac{4e^2k_{\rm mean}}d+\frac{e^2d'}{d^2}\right)
 \right\}.
 \end{split}
\tag{16}
\]

This is the added second-order *decay-defect* term, not just a Hessian
of Phi. In particular the coefficient of b_1 in its right side is

\[
 4e(1+q)C_0
 \left\{\left(\frac{P^2}{\nu_0}-\frac1d\right)\zeta_1
              +\frac{PH}{\nu_0}\beta_1\right\}\cdot b_1.
\tag{17}
\]

There is no general sign or cancellation of this term. The repaired
initial defect therefore does not imply an all-time repaired defect.

## 4. Complete first and second trained defect coefficients

The preceding mode formula isolates the newly added quadratic terms.
For arbitrary directions, including the invariant first variation and all
mixed sphere directions, the following finite recurrence gives every
coefficient of the full defect (7). It avoids an unreadable expanded
six-by-six formula while specifying each operation exactly.

Take one sphere-chart curve epsilon, and expand each quantity as
A=A_0+epsilon A_1+epsilon^2 A_2+O_T(epsilon^3); thus A_2 is half the
second derivative. Use the complete trained response equations from
`sphere_second_variation.md` for p_j,q_j,K_j. They retain normal sphere
acceleration and every mixed state/input term. Gamma_{0,j} is obtained
by applying the same initialized feature derivative formulas, with state
responses zero. Then

\[
 r_0=p_0-n,\quad r_j=p_j\ (j=1,2),\qquad
 S_j=\Gamma_{0,j}+\sum_{a+b=j}p_a p_b^T,
\]
\[
 R_0=S_0^{-1},\quad R_1=-R_0S_1R_0,\quad
 R_2=R_0S_1R_0S_1R_0-R_0S_2R_0.
\tag{18}
\]

Compute the coefficients of Gamma_0^{-1} by the same three formulas,
with S_j replaced by Gamma_{0,j}. If t_j are the coefficients of
n^T Gamma_0^{-1}n, then

\[
 \mu_{0,0}=t_0^{-1},\quad \mu_{0,1}=-t_1/t_0^2,\quad
 \mu_{0,2}=t_1^2/t_0^3-t_2/t_0^2.
\tag{19}
\]

All sums below run over nonnegative indices adding to j<=2:

\[
 L_j=\sum_{a+b=j}r_a^Tr_b,\qquad
 k_j=\sum_{a+b+c=j}r_a^TK_b r_c,\qquad
 b_j=\sum_{a+b=j}r_a^Tp_b,
\]
\[
 u_j=\sum_{a+b+c=j}r_a^TR_b r_c,\qquad
 v_j=\sum_{a+b+c=j}p_a^TR_b r_c,\qquad
 a_j=\sum_{a+b+c+d=j}r_a^TR_bK_c r_d.
\tag{20}
\]

Let A_j=q_j+1_{j=0}, B_j=1_{j=0}-v_j, and use ordinary polynomial
convolution, denoted by a star. Then exactly

\[
 (\mathscr D_\lambda)_j
 =-4k_j+\lambda L_j+
 [\mu_0\star\{-4A\star B\star a-4b\star u+
                    \lambda A\star u\}]_j,
 \qquad j=0,1,2.
\tag{21}
\]

For the dataset-dependent proposed rate lambda=4mu_0, replace every
lambda product in (21) by convolution with the coefficients 4mu_{0,j}.
Mixed second coefficients follow by polarization, or by the identical
two-variable convolution. These are first/second perturbations of the
**flow derivative plus rate times potential**. The second K coefficient,
which involves the complete second trained state response, appears in
(20) and is not discarded. Weighted Gaussian response bounds from the
supplied sphere report justify the Taylor operations on each fixed
horizon; no all-time response bound follows from them.

## 5. A proved all-time theorem for the corrected potential

Fix a member of the signed rho family with labels exactly (1,1,-1),
and suppose its fitting endpoint X_* has K_*>0. Then there exist an
open neighborhood of its three signed unit inputs and a fixed lambda>0
such that every canonically initialized flow for those data satisfies

\[
 \Phi_{\rm mat}'\le-\lambda\Phi_{\rm mat},\qquad
 L\le\Phi_{\rm mat}\le2e^{-\lambda t},\qquad t\ge0.
\tag{22}
\]

Here the middle inequality means the exponentially bounded potential,
not a claim Phi_mat<=2L off symmetry. All constants depend on the seed
and canonical initialization. Neither X_* nor a trajectory integral is
part of the definition (4).

**Proof.** Initial rank gives a neighborhood where Gamma_0 stays uniformly
positive. By continuity of the full Gram in the physical state norm on
bounded c,M sets, a sufficiently small state ball about X_* and input
neighborhood have K>=kappa I for some kappa>0. This continuity uses
bounded dictionaries and gates: integrated coefficient differences are
bounded by row/readout L2 differences, while Q_i and the gates are bounded
on the common c,M ball. Input differences use ||w||_2 times their Euclidean
size. Thus the Gaussian row is not treated as bounded.

Choose a finite T with the symmetric seed close enough to X_* and with
sqrt(L_seed(T)) sufficiently small. Finite-horizon continuous dependence
puts nearby-data states strictly inside that ball at T with the same small
loss. As long as they stay in it,

\[
 L'=-\|X'\|^2\le-4\kappa L,\qquad
 -\frac d{dt}\sqrt L\ge\sqrt\kappa\|X'\|.
\tag{23}
\]

The latter follows from ||X'||^2=4r^TKr and
||X'||>=2sqrt(kappa L). Its integral bounds remaining path length by
sqrt(L(T)/kappa). Choosing this smaller than the unused ball radius
contradicts a first exit. Hence the trajectories stay in the ball and
fit exponentially. At zero loss uniqueness makes them stationary.

It remains to verify decay of the new potential, not only decay of L.
Write

\[
 P=I+\mu_0(1+q)(\Gamma_0+pp^T)^{-1},\qquad
 \Phi_{\rm mat}=r^TPr.
\]

At the symmetric fitting center p_*=n, both P_* and K_* are scalar on
the mean and transverse permutation subspaces. Thus they commute, and

\[
 2(K_*P_*+P_*K_*)=4K_*P_*>0.
\]

This strictly positive inequality persists in a sufficiently small
state/data neighborhood in the form 2(KP+PK)>=3k_*P, where
k_*=lambda_min(K_*)>0. To justify it, conjugate by P^{-1/2}; the smallest
eigenvalue of the symmetric three-by-three matrix is continuous, and its
value at the center is at least 4k_*.

On that neighborhood, P is bounded and differentiable in present p,q;
Gamma_0 and mu_0 are constant in time. Equation (3), bounded K and bounded p
give ||P'||<=B|r| for a fixed finite B. Direct differentiation yields

\[
 \Phi_{\rm mat}'
 =-2r^T(KP+PK)r+r^TP'r
 \le-3k_*\Phi_{\rm mat}+B|r|^3.
\tag{24}
\]

Since P>=I, choose T and then the data neighborhood so that
B|r(T)|<=k_*. Loss monotonicity preserves this bound. Equation (24)
then gives Phi_mat'<=-2k_*Phi_mat throughout the tail. If B=0 this extra
choice is unnecessary. Notice that K>=kappa I alone would not justify
the matrix anticommutator step; commutation at the symmetric center and
continuity supplied the needed fact.

On the finite interval [0,T], the symmetric Phi_mat equals the candidate's
potential, is bounded away from zero, and satisfies
Phi_mat'/Phi_mat<=-4C_0. The exact expression (6) and finite-time
continuous dependence preserve Phi_mat'/Phi_mat<=-2C_0 after one more
reduction of the data neighborhood. Taking
lambda=min(2C_0,2k_*) proves (22), using Phi_mat(0)=2. This proof allows
interior rank-loss events before the endpoint. It proves the assertion
for the actual full-block initialized flow, with no changed optimizer.

The length estimate in (23) gives a full physical-Hilbert-state limit.
On the tail, bounded dictionaries and bounded c,M make the row and
readout essential-supremum speeds at most a constant times sqrt(L).
They are integrable. Therefore w-g and c also converge in their
essential-supremum norms, M converges, and the common frozen-mark
coupling gives W2 convergence of both saved joint populations.

## 6. Precise surviving obstruction and claim boundary

At any symmetric fitting endpoint, write k_*=n^TK_*n and
nu_*=lambda_min(E^TK_*E). The quadratic expansion of the new potential
in a purely transverse residual at that fixed center has weight

\[
 P_{*,\perp}=1+\frac{C_0(1+q_*)}{\nu_0}>0,
\]

and its linear residual-flow decay defect has coefficient

\[
 (\lambda-4\nu_*)P_{*,\perp}|\zeta|^2.
\tag{25}
\]

The positive initial feature eigenvalue nu_0 regularizes the potential;
it cannot create physical decay when the current transverse tangent
eigenvalue vanishes. If nu_*=0, (25) is positive for any lambda>0.
This is an obstruction to a uniform ambient residual inequality at that
center. It is not a proof that initialized nearby trajectories excite
that direction, nor a counterexample to their convergence: at a singular
point the admissible first state/output variations themselves need care.
It does show exactly why matrix normalization alone cannot replace the
missing dynamical estimate.

For the present rho family, the supplied endpoint report identifies
nu_*=0 precisely with theta_perp=0 and d_parallel=0 at F=1. No inequality
derived here excludes those simultaneous equations at unit labels, and
the first/second defect terms (17),(21) have not supplied a sign that
bypasses them. The finite exceptional-amplitude theorem does not control
the prescribed amplitude-one slice. No almost-every-rho conclusion is
inferred from it.

| Claim | Status and scope |
|---|---|
| Explicit nonsingular correction (4), Phi(0)=2 and loss control | Proved on the initialized-rank-three data set |
| Exact physical derivative and defect (6)--(7) | Proved, all current full tangent blocks retained |
| Repair of the wrong initial second-order defect | Proved exactly in (8)--(10) |
| Complete first/second trained defect recurrence | Proved on each fixed finite horizon |
| All-time symmetric inequality | Proved for every admitted rho, both orientations |
| All-time corrected-potential inequality in nonsymmetric neighborhoods | Proved for every unit-label seed with K_*>0 |
| New unit-label rho range away from previously known good seeds | Not obtained |
| Uniform all-time sign of (7) from initialized matrix moments alone | Open |

This route therefore supplies an actual correction and a proved use of it,
but does not claim the broader all-time result sought in the assignment.
The decisive remaining requirement is an initialized-flow estimate ruling
out, or otherwise controlling the transverse dynamics at, a singular
unit-label endpoint. Neither the old Hessian calculation nor this repaired
initial decay defect closes that requirement.

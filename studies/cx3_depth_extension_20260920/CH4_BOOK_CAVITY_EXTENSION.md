# Extending the book's Gaussian column-deletion argument

2026-09-20. Supervisor derivation for the renewed C-X3 proof attempt.
The contract is unchanged. The unconditional results below concern actual
finite GF. The population-construction result in section 4 has an explicit
unproved susceptibility premise. **This file does not complete C-X3.**

Inputs: CONTRACT.md, CH3_LOCAL_PROOF.md and the previous study comparison
and fitting reports; maintained global_nonlinear.md B.1, complete C.4.6.3
(7652–8427), and the statements/construction mechanisms of C.4.7; maintained
special_data_limits.md J.1; docs/NOTATION.md. The earlier book-scope search
is used only to locate these established sources. No other study is an input.
No experiment, finite training run or maintained-file edit was performed.

The book's column-deletion proof has three steps: a Gaussian probe of an
independent cavity flow; stability between actual and cavity flows; and an
exact bounded learned-memory term. The first and third steps extend to every
fixed depth. At depth three the middle stability step remains to be proved.
The following makes this separation quantitative and also shows that an
actual-finite-GF certificate could replace uniform Euler response caps for
constructing the orthogonal reference.

## 1. Actual finite dynamics and depth-dependent deterministic bounds

Fix L>=2, T>0, and the two normalized inputs e_1,e_2 with labels +1,-1
and masses 1/2. Use exactly the stored weights, independent Gaussian
initialization, all trained blocks, mobilities and mean loss of CONTRACT §2.
Use ordinary finite Euclidean/Frobenius/operator norms; display 1/sqrt(n)
for every vector RMS. Put A_l=W^(l), K_l=A_l-A_l,0 and c=W^(L+1).

Let E_n be the initialized event

    max_(2<=l<=L) ||A_l,0||op<=10,
    ||w_0||F/sqrt(n)<=2,       ||c_0||infinity<=1.             (1)

Its probability tends to one by the established Gaussian action bound,
the fixed two-dimensional row second-moment law, and
P(max_i|c_0,i|>1)<=2n exp(-n^2/2). The actual random c_0 is retained.

At fixed width the smooth GF exists globally. Indeed the raw energy identity
bounds its Euclidean displacement on each finite interval (the metric is
positive definite at that width); a finite endpoint extends by the local
finite-dimensional ODE. On (1), |f_a(0)|<=1, so loss(0)<=4. Energy and
Cauchy–Schwarz give raw path displacement at most 2sqrt(T). Thus, with

    B=10+2sqrt(T),   C=1+2sqrt(T),
    W=2+2sqrt(T),    H=1+4T,                                (2)

all actual paths on E_n satisfy

    ||A_l(t)||op<=B,       ||K_l(t)||F<=2sqrt(T),
    ||c(t)||2/sqrt(n)<=C, ||w(t)||F/sqrt(n)<=W,
    sum_a |r_a(t)|<=4,    ||c(t)||infinity<=H.               (3)

The readout supremum follows by integrating c'=-sum_a r_a h_L,a.
Backward induction and the rank-update formulas give

    ||delta_l(u)||2/sqrt(n)<=C B^(L-l),
    ||w'||F/sqrt(n)<=4C B^(L-1),
    ||K_l'||F<=4C B^(L-l),       ||c'||infinity<=4.          (4)

The first inequality is uniform over passive unit inputs u; the updates use
only the two training inputs. Define

    D_1=4C B^(L-1),
    D_l=4C B^(L-l)+B D_(l-1),       2<=l<=L.

The forward product and chain rules imply
||partial_t z_l(u)||2/sqrt(n)<=D_l. In particular

    D_L=4C sum_(j=0)^(L-1) B^(2j).                         (5)

For the top backward operand U(t,u)=delta_L(t,u)=c(t)phi'(z_L(t,u)),
where phi=tanh, this yields

    ||U||2/sqrt(n)<=C,
    ||partial_t U||2/sqrt(n)<=D_t:=4+2H D_L,
    ||U(t,u)-U(t,v)||2/sqrt(n)<=D_u |u-v|,
    D_u:=2H W B^(L-1).                                     (6)

The last line follows from the forward input bound
||z_L(u)-z_L(v)||2/sqrt(n)<=W B^(L-1)|u-v|. These are
deterministic estimates on actual GF, at every fixed depth and horizon.
No backward source cap, population limit or finite-network fitting was used.

## 2. The Gaussian cavity probe still has a uniform Gaussian bound

For each neuron i in population L-1, let a_i=A_L,0 e_i and replace only
the initialized top hidden matrix by

    A_L,0^(i)=A_L,0-a_i e_i^T.                              (7)

Train the full resulting network, with every learned column retained and
the same other initialized variables. Denote its actual GF by superscript
(i). In particular its learned top column is not held at zero. This finite
flow is independent of a_i conditional on all remaining initialized variables.

Let E_n^i be event (1) with the deleted initial matrix in place of A_L,0.
It is measurable in those remaining variables, and E_n is a subset of E_n^i
because deleting a column is right multiplication by an orthogonal projection.
All constants (2)–(6) apply to the cavity on E_n^i.

Set

    Z_i(t,u)=a_i^T U^(i)(t,u),
    Z_i^#=sup_(0<=t<=T,u in S1) |Z_i(t,u)|.                 (8)

Conditionally on the remaining initialization, this is a centered Gaussian
process, with covariance U^(i)(t,u)^T U^(i)(s,v)/n. Equations (6) give
variance at most C^2 and canonical-metric Lipschitz constants D_t,D_u.
The contained dyadic Gaussian-grid argument in C.4.6.3 §4 applies unchanged:
parameterize t=Tq_1 and u=(cos(2pi q_2),sin(2pi q_2)), bound each grid
increment by its Gaussian variance and a union bound, then sum its maxima
over dyadic levels. It gives, for every real p>=2,

    (E_(a_i) [(Z_i^#)^p])^(1/p)
       <= C_Z sqrt(p) on E_n^i,
    C_Z=64(C+T D_t+2pi D_u).                                (9)

The process is continuous since the finite GF is smooth. The same grid
argument handles arbitrary correlations between its times and inputs.
Consequently ||1_(E_n) Z_i^#||_(L^p(initialization))<=C_Z sqrt(p).
Conditioning was done on E_n^i, not on the column-dependent event E_n.

Thus the independent Gaussian probe is controlled at any fixed depth and
time without assuming that the actual trained operand is independent of
its original column.

## 3. Exact localization to a column-deletion susceptibility

For every actual top backward answer P_(L-1)(t,u)=A_L(t)^T U(t,u),
the learned part has the exact coordinate expression

    [K_L(t)^T U(t,u)]_i
      =-sum_a integral_0^t r_a(v) h_(L-1),a,i(v)
                   [delta_L,a(v)^T U(t,u)/n] dv.

Using (3) and bounded tanh proves

    sup_(t,u) |[K_L(t)^T U(t,u)]_i|<=4T C^2 on E_n.        (10)

Define the susceptibility with its important normalization:

    S_(n,i)=sup_(t<=T,u in S1)
                    ||U(t,u)-U^(i)(t,u)||2.               (11)

This is the ordinary Euclidean norm, equivalently sqrt(n) times the
normalized RMS difference. Raw O(1) RMS bounds would only give O(sqrt(n))
here and are insufficient. Since ||a_i||2<=10 on E_n, subtracting the
cavity operand in a_i^T U gives the pathwise inequality

    N_(n,i):=sup_(t,u)|P_(L-1),i(t,u)|
          <=Z_i^#+10 S_(n,i)+4T C^2 on E_n.                (12)

There is no fresh-Gaussian replacement of the actual answer in (12).
Its complete dependence error is the displayed susceptibility.

Here is a sufficient, as yet unproved, finite-network certificate:
there exists K_T<infinity, independent of n,i,p, such that

    ||1_(E_n) S_(n,i)||_Lp <= K_T p,
                for all n,i and real p>=2.                (SC)

It is enough that (SC) hold for all sufficiently large n. Together with
(9)–(12), it implies

    ||1_(E_n) N_(n,i)||_Lp <= K p,
    K=C_Z+10K_T+4TC^2.                                    (13)

For R>=2eK choose p=R/(eK)>=2. The p-th moment and
N^2 1_(N>R)<=N^p R^(2-p) give

    E[1_(E_n) N_(n,i)^2 1_(N_(n,i)>R)]
                       <=R^2 exp(-R/(eK)).                (14)

Average over i and take a square root by Jensen. With

    tauhat_(n,R)=[n^-1 sum_i N_(n,i)^2
                                     1_(N_(n,i)>R)]^(1/2),

one obtains, enlarging the constant to cover 1<=R<2eK,

    E[1_(E_n) tauhat_(n,R)]<=M exp(-aR),
    M=4eK,       a=1/(4eK).                                (15)

For the large-R absorption, max_(R>=0) R exp(-R/(4eK))=4K.
For small R the p=2 bound in (13) gives E[1_E tauhat]<=2K.
The envelope in (15) controls every actual time and passive input at once.

The conclusion (15) is conditional on (SC). Neither the Gaussian-probe
bound (9) nor the learned-memory bound (10) proves (SC).

## 4. Why this certificate would construct the depth-three reference

This section states and proves the conditional construction, to specify
what (SC) would actually resolve. Take L=3 and fix the physical horizon T.
Assume (SC) for the actual finite reference GF and its top-column cavities.
No population solution or uniform Euler source estimate is assumed.

Introduce the two first-row clocks X_a using w_a=j(X_a,g_a), where
j_X=phi'(j), j(0,g)=g. Orthogonality makes the exact physical first-row
equation equivalent to X'_a=-r_a P_1,a. The state is

    (X_1,X_2,K_2,K_3,c),

with clock L2, increment HS and readout L2 norms. The scalar bounds
|j(X,g)-j(Y,g)|<=|X-Y| and
|phi(j(X,g))-phi(j(Y,g))|<=|X-Y| hold with the same roots.

On a common bounded state ball, the forward fields, delta_3 and P_2
are Lipschitz in this state distance. For P_2 this follows by subtracting
A_3* [c phi'(Z_3)]; the readout in the gate difference is bounded.
The only additional backward product is delta_2=phi'(Z_2)P_2.
Writing barred fields for the reference endpoint, its subtraction is

    delta_2-deltabar_2
       =phi'(Z_2)(P_2-Pbar_2)
          +[phi'(Z_2)-phi'(Zbar_2)] Pbar_2.

Cut the last reference field at R. Since |phi'|<=1 and Lip(phi')<=2,

    ||delta_2-deltabar_2||2
       <=C(1+R) d +2 tau_R(Pbar_2).                        (16)

In finite width each displayed vector norm has the corresponding 1/sqrt(n).
Subtraction of P_1=A_2*delta_2, the two rank velocities, the readout
velocity, residuals and first-clock velocities gives

    ||F(theta)-F(thetabar)||sum
       <=C[(1+R)d+sum_(a=1,2) tau_R(Pbar_2,a)].            (17)

There is no P_1-tail term: its varying first gate was removed by the
orthogonal clock, and the P_1 difference uses (16) followed by the bounded
actual action A_2*. The constant depends on T and the common norm bounds,
not n, R or a mesh.

Construct transformed Euler on any fixed proof mesh, retaining the actual
finite initialization. Its global bounds do not need source caps. Its
readout update obeys the elementary discrete Gronwall bound; bounding
the top action first, then the next action and finally the clocks gives
finite mesh-independent bounds by the same downward induction as the
study's CH4_REACHED_ESTIMATES §2. All rank Frobenius increments and clock
RMS velocities are bounded. The identical construction on canonical
Gaussian action spaces is a finite program at each fixed mesh.

Compare finite transformed Euler of maximum step h to actual finite GF,
using GF as the tail-bearing endpoint in (17). Its preceding-node error
is at most C h. On E_n both paths are in a common ball. Let d_n^*(t)
be the maximum state distance through time t, and let
y_n(t)=E[1_(E_n) d_n^*(t)]+h. Norms and running maxima of the finite
absolutely continuous curves are absolutely continuous. Their derivatives,
(17), and (15) give, for every fixed R>=1, almost everywhere,

    y_n'(t)<=C[(1+R)y_n(t)+M exp(-aR)],  y_n(0)=h.        (18)

One first takes the countable set of integer R so a common full-measure
time set exists. Rounding an optimizing real R up adds at most C y_n.
For 0<y<=1 choose R=max(1,a^-1 log(M/y)); this yields
y_n'<=C' y_n log(H'/y_n), with fixed H'>1, C'<infinity.
Direct integration of log(H'/y_n) gives a modulus Psi_T(h)->0, uniformly
in n, for sup_(t<=T)y_n(t). A first-exit argument validates the bound
below one for sufficiently small h. Thus

    E[1_(E_n) sup_(t<=T) d_n(GF,Euler_h)]<=Psi_T(h).       (19)

The use of actual finite GF in (19) is intentional; no unproved uniform
tail estimate for the Euler family has been substituted.

At each fixed h the complete initialized program and its finite unions
have their established Gaussian value limit. This includes the continuous
at-most-linear j instruction of B.1/A.1, both matrix orientations, finite
empirical contraction feedback, and the actual vanishing initial readout.
The finite-rank identity

    ||sum_j a_j tensor b_j||HS^2
       =sum_(j,k) <a_j,a_k><b_j,b_k>

identifies the ordinary finite Frobenius distance of learned increments.
This is the same fixed-program/actual-rank proxy argument as B.1 and
CH3_LOCAL_PROOF §8; it is used only at fixed meshes, never with a graph
whose length grows with width. Any fixed-node cutoff needed for a
bounded-factor product is removed only after that fixed-program limit.

Compare two finite Euler paths to the same finite GF via (19). Take width
to infinity at the two fixed meshes. Their finite-union program identifies
the limiting clock/HS/readout distance, which is deterministic on the common
canonical carrier. Fatou along an almost-sure subsequence, using P(E_n)->1,
bounds that distance by Psi_T(h)+Psi_T(h'). Uniformity in time follows by
finite time grids and the common state velocity bounds. Hence the population
Euler family is Cauchy in C([0,T];clock-L2 x HS x HS x L2).

Strong multiplier continuity and the actual bounded action/adjoint pairs
pass its integrated equations to the limit. Converting w=j(X,g) gives
a strong raw GF with both learned increments strongly C1 in HS. The
scalar first-clock representation holds conversely for every competing
strong raw orthogonal-reference solution, by the scalar ODE and Fubini.

For completeness, the required target tails follow from the finite bound
rather than being assumed. P_2 is Lipschitz in the clock state on the
common balls. Equations (19) and the fixed-program limits therefore identify
its actual finite-GF joint law at every finite list of times and passive
inputs with the constructed target. Bounded truncations of their maximum
p-th moments, (13), and monotone convergence pass the same moment bound
to each such finite list. Take a countable dense time/input family; L2
continuity controls every other deterministic query, as in C.4.6.3 §6.
The target consequently has uniform exponential P_2 RMS tails.

Using it as the barred endpoint of (17) proves uniqueness and reached
restart by the same scalar Osgood inequality. A competing path needs no
tail assumption of its own; its compact raw path bounds its actions and
residuals, and integrating the bounded last activation bounds its readout
supremum. Whole-input predictions and fixed admitted same-layer observations
are identified by (19), fixed-program identification and the compact-target
cutoff argument of CH3_LOCAL_PROOF §9. This proves the conditional reference
construction and actual finite-GF capture through T.

This statement concerns only the orthogonal reference. It does not assert
a supported-law radius, numerical hierarchy convergence, or actual raw-GD
capture for nearby laws. Those remain additional C-X3 obligations.

## 5. The missing stability step in the book's proof

At L=2 the cavity comparison is (C.4.6.S21)–(C.4.6.S26): the whole
clock-state difference is O(n^-1/2) times the independent Gaussian probe,
and U=delta_2 is Lipschitz in that state with bounded readout. This gives
S_(n,i)<=C_T(1+Z_i^#) on E_n and proves even a sqrt(p) version of (SC).

At L=3 the same subtraction contains

    [phi'(z_2)-phi'(z_2^(i))] P_2^(i).                     (20)

The new factor is the cavity's adaptive incoming field, not the bounded
readout. A raw norm bound controls its RMS only. Cutting it at R gives
the propagation factor C(1+R) and a cavity-tail error. Multiplying a
state comparison by sqrt(n), as required in (11), also multiplies that
tail error by sqrt(n). A cutoff chosen after width is fixed does not
prove (SC), and a width-dependent cutoff would require a separately
proved quantitative cavity-tail estimate. Using the desired source
bound here would be circular.

Trying to clock the middle preactivation does not simply repeat B.1.
The exact derivative includes

    z_2,a' = K_2' h_1,a + A_2[phi'(w_a) w_a'].

The second term is a changing-input contribution; it need not contain the
factor phi'(z_2,a). Dividing by that factor creates an inverse-gate term.
No estimate for this new term has been obtained from the bounded top
readout or from the Gaussian probe calculation.

The finite susceptibility (SC) is therefore the unresolved part of this
route. The calculations establish a precise alternative certificate and
its conditional construction consequence, but do not establish that
certificate along the actual trained network. No finite-time failure of
the requested limiting dynamics is inferred.

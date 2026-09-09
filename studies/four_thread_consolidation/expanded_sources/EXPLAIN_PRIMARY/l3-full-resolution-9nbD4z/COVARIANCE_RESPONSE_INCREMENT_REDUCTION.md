# Covariance response increments and Gaussian action decomposition

## Status and scope

This note proves an exact structural reduction and a global-in-feature-time
bound for contracted response increments of every fixed clipped program.
It does not prove global cutoff removal, a tail bound, or stability of a
pruned network. The initialization, both Gaussian matrices, and both reused
transposes are those of L3_LOCAL_COMPLETE_PROOF.md.

The new conclusion is that the earlier-memory contraction has a uniform
L2 bound without an absolute variation bound for its coefficient kernel.
The corresponding contraction against a tangent field is still unbounded
by the estimates here. Thus this resolves a regularity issue for the
contracted memory, not the global continuation problem.

## Gaussian creation maps on the common action spaces

For each adjacent pair of layer spaces there are linear isometries

    G_l : H_{l-1} -> H_l,    J_l : H_l -> H_{l-1},

such that every fixed G_l U and J_l V is centered Gaussian with variance
||U||_2^2 and ||V||_2^2, respectively, and

    W_{l,0} = G_l + J_l^*,      W_{l,0}^* = J_l + G_l^*.       (1)

Here a star is the Hilbert-space adjoint. Each range is the closed first
Gaussian chaos of its corresponding oriented source group. On a layer
containing two source groups, those Gaussian groups remain independent;
the root on layer one remains independent of its reverse source group.

Here is a construction from the proved finite-program result. Enumerate
the countable calculation class used to construct the common population
spaces, append the finitely many required instructions at each stage,
and retain the Gaussian source coordinates at every matrix query.
The finite source theorem applies to every finite prefix. Its causal
Gaussian extensions and coordinate expressions give consistent laws for
these enlarged prefixes. A query with input U receives a source g_U with

    E[g_U g_V] = E[UV].

These sources are already measurable on the generated action spaces:
at each finite query the source equals the matrix-answer node minus its
finite response combination of earlier nodes. Thus retaining them does
not require enlarging the original generated L2 spaces.

Consequently sources for two equal L2 inputs agree almost surely, and
g_{aU+bV}=a g_U+b g_V whenever the three inputs have been included. This
defines G_l on the dense span of the input nodes. It extends uniquely to
an isometry on H_{l-1}. The reverse query sources define J_l identically.
L2 limits of these jointly Gaussian variables remain jointly Gaussian.

For a finite-program input U, let its finitely many earlier reverse
source coordinates be zeta_s=J_l V_s. The finite source rule gives

    W_{l,0} U = G_l U + sum_s V_s E[partial_{zeta_s} U].       (2)

To identify the sum, append any reverse query with input V. Its source
J_l V has covariance E[V_s V] with zeta_s, and has no additional
dependence on U beyond these old Gaussian coordinates: its fresh
innovation is independent of U and all its other source groups.
Degenerate Gaussian integration by parts therefore gives

    E[U J_l V] = sum_s E[V_s V] E[partial_{zeta_s} U].

Thus the correction in (2) is J_l^* U. This proves (1) on the dense
finite-program span and hence everywhere by continuity. No inverse
covariance matrix or limiting pseudoinverse is used. It also gives
||W_{l,0}||_op <= 2; the earlier conservative bound 10 remains valid.

This construction concerns the same generated action spaces. It does
not replace the trained matrices by independent resamplings.

## All-time covariance inequalities

Fix a finite feature mesh, a clipping level, and a finite horizon S.
Use full history vectors h_l=(H_{l,k})_k and d_l=(delta_{l,k})_k,
and their second-moment matrices Gamma_h and Gamma_d. Let A_l and B_l
denote only the Gaussian response parts of a_l and b_l:

    A_{l,ks} = E partial_{zeta_{l-1,s}} H_{l-1,k},
    B_{l,ks} = E partial_{xi_{l,s}} delta_{l,k}.

Future coefficients are zero under the formal-coordinate convention.
The projection identities are

    P_{ran J_l} H_{l-1,k} = sum_s A_{l,ks} zeta_{l-1,s},
    P_{ran G_l} delta_{l,k} = sum_s B_{l,ks} xi_{l,s}.

Since orthogonal projection is a contraction, simultaneously for all
deterministic linear combinations of times,

    A_l Gamma_{d_l} A_l^T <= Gamma_{h_{l-1}},
    B_l Gamma_{h_{l-1}} B_l^T <= Gamma_{d_l}.               (3)

The inequalities are in the positive-semidefinite order and remain
valid for singular covariance matrices. Unlike an individual row-norm
estimate, (3) directly controls differences of whole response rows.

The contracted response processes are exactly

    sum_s A_{l,ks} delta_{l,s} = J_l^* H_{l-1,k},
    sum_s B_{l,ks} H_{l-1,s} = G_l^* delta_{l,k}.           (4)

In particular,

    ||sum_s (A_{2,k+1,s}-A_{2,k,s}) delta_{2,s}||_2
       <= ||H_{1,k+1}-H_{1,k}||_2 <= C_S Delta,           (5)

with C_S independent of clipping and mesh. The last estimate follows
from the transformed bottom update and the already proved global
polynomial primal bounds. Similarly,

    ||sum_s (B_{3,k+1,s}-B_{3,k,s}) H_{2,s}||_2
       <= ||delta_{3,k+1}-delta_{3,k}||_2 <= C_S Delta.    (6)

For (6), the readout is bounded pointwise by aS, its increment is at
most a Delta, and the top preactivation increment has L2 size at most
C_S Delta by the forward operator and velocity bounds. Bounded phi''
therefore controls the top backward-field increment uniformly in R.

## The earlier-memory contraction itself

Define a_{2,k,k}=0, and use the complete forward coefficient a_2,
including its learned contribution. Then

    Z_{2,k+1}-Z_{2,k}
      = xi_{2,k+1}-xi_{2,k}
        + a_{2,k+1,k} delta_{2,k}
        + sum_{s<k}(a_{2,k+1,s}-a_{2,k,s}) delta_{2,s}.    (7)

The adjacent response coefficient is exactly

    A_{2,k+1,k}=Delta E[chi'(X_{1,k+1})],

and hence has magnitude at most Delta. Subtracting its contraction
from (5) controls the old-time part of the response-row difference.
For the learned part and s<k,

    (a^learn_{2,k+1,s}-a^learn_{2,k,s})/Delta
       = E[(H_{1,k+1}-H_{1,k}) H_{1,s}].

Bound this contraction by

    sum_{s<k} a ||H_{1,k+1}-H_{1,k}||_2 ||delta_{2,s}||_2
       <= C_S,

using k Delta<=S and (5). Consequently the exact discrete old-memory
field

    M_{2,k} = sum_{s<k}
          [(a_{2,k+1,s}-a_{2,k,s})/Delta] delta_{2,s}

satisfies

    sup_{R,Delta,k Delta<=S} ||M_{2,k}||_2 <= C_S.         (8)

All constants use the explicit polynomial primal bounds, not a
response-row bootstrap. Also
||xi_{2,k+1}-xi_{2,k}||_2 <= C_S Delta. Thus (7) defines a
uniformly bounded L2 forcing after separating the current-site term,
without first positing a differentiable scalar kernel a_2(t,s).

For a fixed clipped continuum flow, (1) and (4) define its contracted
response derivative directly as J_2^* H_1'(t). This is a strong L2
derivative. The learned term is differentiable by its rank-one integral
formula. These definitions require no absolute coefficient variation
and no division by a covariance eigenvalue.

## Uniform Gaussian bounds for entire source paths

On every finite S, the three source processes xi_2, xi_3, and zeta_2
have uniform Gaussian bounds for their supremum over time. This holds
uniformly in clipping and mesh; it uses no independence across times.

For example, linearly interpolate xi_{3,k} on its mesh. On an interval
of length Delta its derivative is centered Gaussian with standard
deviation

    ||H_{2,k+1}-H_{2,k}||_2/Delta <= C_S.

Writing c_p=||N(0,1)||_p<=sqrt(p), pointwise integration followed by
Minkowski gives

    ||sup_{t<=S}|xi_3(t)||_p
      <= c_p [||H_{2,0}||_2
                    + sum_k ||H_{2,k+1}-H_{2,k}||_2]
      <= C_S sqrt(p),                                    (9)

for p>=2. The identical proof uses H1 for xi_2 and delta3 for zeta_2.
The required increments are uniformly bounded by C_S Delta above;
zeta_2(0)=0 because the initial readout is zero. Consequently, for a
larger finite K_S independent of mesh and clipping,

    E exp[(sup_{t<=S}|xi_l(t)|)^2/K_S^2] <= 2,  l=2,3,
    E exp[(sup_{t<=S}|zeta_2(t)|)^2/K_S^2] <= 2.          (10)

One can derive (10) by expanding the exponential and using (9) at
p=2m together with m!>=(m/e)^m. The fixed-clipping continuum sources
have the same estimates: apply the Gaussian isometries to the C1 L2
input paths, then integrate their L2 derivatives to obtain continuous
sample-path versions. The same Minkowski proof applies.

No analogous cutoff-uniform assertion for zeta_1 is made here: it
would require uniform time-increment control of delta2, which these
primal estimates do not supply. Equations (9)--(10) control the
Gaussian sources, not the transported projection G_3^* delta3.

## Why this does not close continuation

Neither (3) nor (8) bounds the same coefficient row acting on a formal
tangent delta-field. The tangent may have a different covariance, and
there is no proved domination by Gamma_{d_l}. This is the missing
step if (8) is inserted into the characteristic response calculation.

Nor does a Gaussian-isometry adjoint preserve subexponential tails,
even on bounded smooth inputs. Let G be one of the isometries and let
V be any unit L2 variable in its domain. Set

    b(x)=arctan(x)/(1+x^2),       U=b(GV).

The variable U is bounded and smooth in one standard Gaussian. For
every test vector w, Gaussian integration by parts yields

    E[U Gw] = c <V,w>,
    c=E[G_0 b(G_0)]>0,          G_0~N(0,1).

Therefore G^*U=cV. The input V may have no exponential moment.
This is an obstruction to inferring tails from (1) and boundedness
alone. It is not a counterexample to training: an arbitrary V need not
be an actual bounded hidden-feature path, and U need not have the
actual history-dependent form C(t) phi'(Z_3(t)).

The preserved new reduction is therefore (1), (3), and especially
the mesh-uniform contracted-memory estimate (8). A successful next
step must use the actual coupled top history to control the tails of
G_3^* delta_3(t), or control its action on the relevant perturbations.
No global theorem follows from the estimates in this note alone.

# Scoped author-side check of the cavity extension

Date: 2026-09-20. This is author-side synthesis checking, not an independent
promotion review or a proof of the missing susceptibility estimate.

## Frozen target, inputs and verdict

The complete target is `CH4_BOOK_CAVITY_EXTENSION.md` (355 lines), SHA-256

```
61d19b82426e8a33caa83649a853bb6f3796ed1b42332c4b2e0910316a4e9a40
```

The check read the complete maintained `docs/global_nonlinear.md`
C.4.6.3, lines 7652–8427. Other available inputs were the complete study
`CONTRACT.md` and `CH3_LOCAL_PROOF.md`, the previously read complete book
B.1, C.4.5.1 and C.4.7.1–4, and their allowed maintained dependencies.
The fixed-program hypotheses A.1/A.2/A.4 at book lines 1842–1896 were
also checked. No other study report was read. In particular, the target's
reference to `CH4_REACHED_ESTIMATES` was not followed: the elementary
Euler bounds needed at that point are supplied below.

This checker previously performed a maintained-book scope search and
wrote `CH4_BOOK_SOURCE_EXTENSION.md`. That report remains frozen at
SHA-256

```
a22515ab840411f139fbf0695de2e11a3f475ed08504471b10907ed3d48885d2
```

**Verdict:** the implication from (SC) to the claimed orthogonal-reference
construction passes this scoped check. No width/mesh interchange or
circular population-tail assumption was found. The general fixed-depth
Gaussian probe and exact learned-memory estimates also pass. Two compressed
steps deserve the explicit details recorded below: uniform clock-Euler
bounds and removal of the finite empirical-feedback discrepancy at each
fixed mesh. They need no new hypothesis and no mesh-uniform source cap.

This is a conditional result. The normalized finite cavity susceptibility
(SC) remains unproved. Thus neither unconditional depth-three continuation
nor the full C-X3 contract follows from the checked report.

## 1. Normalization, finite-depth bounds and Gaussian probe

Target lines 23–84 use ordinary matrix operator/Frobenius norms and vector
RMS norms. The energy displacement bound controls every learned matrix's
ordinary Frobenius norm, hence its operator norm. With all activation and
gate suprema at most one, backward induction gives

    ||delta_l||RMS <= C B^(L-l).

For forward time derivatives the recursion in the target is

    D_1 = 4 C B^(L-1),
    D_l = 4 C B^(L-l) + B D_(l-1).

Its top value is indeed `D_L = 4 C sum_(j=0)^(L-1) B^(2j)`.
For the top operand `U=c phi'(z_L)`, differentiation, the bounded readout,
and `Lip(phi')<=2` yield the stated RMS time and input Lipschitz bounds.
These arguments work at every fixed finite depth; the constants may grow
with depth and horizon, as allowed.

The cavity in target lines 86–110 deletes only the initialized top column:

    a_i=A_L,0 e_i,  A_L,0^(i)=A_L,0-a_i e_i^T.

It does not freeze the corresponding learned column. Conditional on all
remaining initialization, its trained trajectory and `U^(i)` are independent
of `a_i~N(0,I/n)`. Deletion is right multiplication by a coordinate
projection and does not increase the initial operator norm. Consequently
the larger cavity event `E_n^(i)` contains `E_n` and is measurable with
respect to the conditioning variables. This is the correct event for the
conditional Gaussian estimate; conditioning directly on `E_n` would not
preserve the needed Gaussian law.

For the probe `Z_i(t,u)=a_i^T U^(i)(t,u)`, the conditional covariance is

    Cov(Z_i(t,u),Z_i(v,z)) = <U^(i)(t,u),U^(i)(v,z)>RMS.

Thus its variance and canonical metric are controlled by `C,D_t,D_u`.
Parametrizing the unit circle and rescaling time to a unit interval gives
a two-parameter process whose metric is bounded by
`T D_t |dq_1|+2 pi D_u |dq_2|`. The complete dyadic chaining argument in
maintained C.4.6.3 applies with these constants. The target's generous
constant `C_Z=64(C+T D_t+2 pi D_u)` gives the stated `sqrt(p)` moment bound.
Restricting the resulting estimate to `E_n` via `E_n^(i)` is valid.

There is no depth-dependent growth of the indexing dimension: the probe
still has only time and passive input as its parameters. Depth affects its
deterministic metric constants, not the chaining argument's applicability.

## 2. Exact memory and (SC) imply exponential RMS tails

The learned top matrix has the actual rank-one integral equation. Its
transpose applied to the current operand has coordinate

    (K_L(t)^T U(t,u))_i
      = -sum_a int_0^t r_a(v) h_(L-1),a,i(v)
          <delta_L,a(v),U(t,u)>RMS dv.

All powers of `n` in target lines 129–142 are correct: the inner product
above is the ordinary inner product divided by `n`. Bounded activation,
the residual bound and Cauchy–Schwarz bound this coordinate by `4 T C^2`.
This is an exact memory term for the trained network, not a replacement
of its learned operator by an independent one.

The susceptibility in target line 144 must be, and is, an **ordinary
Euclidean** norm:

    S_(n,i)=sup_(t,u) ||U(t,u)-U^(i)(t,u)||_Euclidean.

Since `||a_i||_Euclidean<=10` on `E_n`, the exact decomposition gives

    N_(n,i) <= Z_i^# + 10 S_(n,i) + 4 T C^2.

There is no missing `sqrt(n)` in this inequality. Replacing `S_(n,i)` by
an RMS norm without restoring that factor would invalidate it.

Under (SC), the Gaussian probe bound and Minkowski yield

    ||1_(E_n) N_(n,i)||_p <= K p,  p>=2,
    K=C_Z+10 K_T+4 T C^2.

For `R>=2eK`, use `p=R/(eK)` to get

    E[1_(E_n) N_(n,i)^2 1_(N_(n,i)>R)]
       <= R^2 exp(-R/(eK)).

Averaging over `i` needs no independence. Jensen then bounds the expected
empirical RMS tail by `R exp(-R/(2eK))`. The target's constants
`M=4eK`, `a=1/(4eK)` dominate this for large `R`; for small `R`, the
`p=2` bound is at most `2K` and is also dominated. Thus (15) is correct,
including its envelope over actual finite-GF times and passive inputs.

## 3. Details filling the fixed-mesh construction

### 3.1 Uniform Euler bounds without source caps

Here are self-contained bounds for target lines 237–244. They also show
that the unavailable cross-reference is not needed for this implication.
Use any mesh of total length at most `T`, with the actual initialization
on `E_n`. If `c_k^*=||c_k||infinity`, the readout update gives

    c_(k+1)^*+1 <= (1+2h_k)(c_k^*+1).

Hence `c_k^*<=cbar=2 exp(2T)-1`. Take
`rbar=2(cbar+1)` as a uniform bound for the sum of residual magnitudes.
Define bounds downward, starting with the top action:

    Abar_L=10+T rbar cbar,
    Abar_l=10+T rbar cbar product_(j=l+1)^L Abar_j.

Then

    ||delta_l||RMS <= cbar product_(j=l+1)^L Abar_j.

Summing rank-one Euler increments proves the indicated action and
Frobenius bounds. The bottom clock velocities have total RMS norm at most
`rbar cbar product_(j=2)^L Abar_j`. These bounds apply to finite Euler
and to its fixed-program population counterpart; all are independent of
the mesh and width. Affine interpolation in the clock state gives a
uniform state velocity bound. No Euler Gaussian-tail estimate was used.

### 3.2 Empirical feedback at a fixed mesh

Target lines 269–282 correctly insist that graph length remain fixed
when width tends to infinity. A.1's fixed-program theorem alone should
not be read as a theorem about arbitrary adaptive coefficients. The
needed finite-step proxy argument is as follows.

Fix the mesh. Form its deterministic-coefficient population program,
including its residuals and contraction coefficients, and evaluate that
same finite program with the finite initialized matrices. Its joint value
limit and quadratic uniform integrability follow from A.1/A.2 and the
continuous at-most-linear clock instruction. At a given step compare the
actual finite update with this proxy, inductively assuming vanishing RMS
and Frobenius state discrepancies at the preceding steps.

Forward differences and the top backward difference are controlled by
bounded operators and readouts. At the only unbounded multiplication,
truncate the proxy operand `P_2` at a fixed level `R`:

    ||[phi'(z_2)-phi'(z_2,proxy)] P_2,proxy||RMS
       <= 2R ||z_2-z_2,proxy||RMS + 2 tau_R(P_2,proxy).

First send width to infinity at this fixed step and fixed `R`, then send
`R` to infinity using that proxy's fixed-program quadratic uniform
integrability. This proves a vanishing backward discrepancy. No uniform
bound over meshes is required. The clock avoids a further varying-gate
product at layer one. Residuals and contraction coefficients converge by
Cauchy–Schwarz; the rank-one Frobenius difference follows from the product
norm identity. Finite induction proves actual/proxy agreement for the
entire fixed mesh. The same argument applies to a finite union of meshes.

This supplies the precise meaning of the target's fixed-program/actual-
rank proxy invocation. It does not assume the uniform tail conclusion
being constructed later.

## 4. Width first, then mesh: no circular passage

The one-reference estimate (17), target lines 210–235, is valid on bounded
clock-state balls with bounded readout. The forward fields, top operand,
and `P_2=A_3^*[c phi'(Z_3)]` are Lipschitz there. Splitting the middle-gate
product at `R` leaves only the reference `P_2` tail. The exact clock
equation removes the varying first gate, so no `P_1` tail is required.

Use actual finite GF as that reference. Its (SC)-conditional tails were
already proved without any population limit. The preceding-node Euler
error is `O(h)` by the bounds above. On `E_n`, all state speeds are bounded
deterministically, which justifies absolute continuity, running maxima,
and differentiation under expectation in (18). Taking integer `R` first
gives a common full-measure time set; optimizing after taking expectation
is legitimate. The resulting Osgood modulus in (19) is uniform in width.

The order of operations is then exactly:

1. Fix two meshes `h,h'` and compare both finite Euler paths with the
   **same actual finite GF** using (19).
2. Let width tend to infinity at these two fixed meshes. Their finite
   union has the fixed-program limit established above. The rank Gram
   identity identifies Frobenius distances with population HS distances.
3. Use a subsequence with almost-sure distance convergence and
   `1_(E_n)->1` almost surely, available since `P(E_n)->1`, and apply
   Fatou. This yields the population distance bound
   `Psi_T(h)+Psi_T(h')`. Finite deterministic time grids and uniform state
   speeds upgrade it to the supremum in time.
4. Only now refine the meshes. The population Euler family is Cauchy in
   the stated complete clock/HS/readout path space.

No assertion about a growing tensor-program graph at width `n` appears
in this sequence. No joint prescription `h=h(n)` is necessary.

Strong bounded-multiplier continuity passes the middle products to the
limit: for a fixed limiting `P_2` in L2, bounded gate differences tending
to zero in measure multiply it to something tending to zero in L2.
Thus strong passage of the equations at this step does not already
require exponential limiting tails. Continuous velocities give the
claimed strong integral solution and C1 HS increments.

## 5. Tail transfer, uniqueness and the unresolved premise

The tail transfer at target lines 298–306 is also noncircular. At every
finite deterministic list of time/input queries, the Lipschitz property
of `P_2`, the finite-GF/Euler comparison and the two-stage limit identify
the actual finite-GF empirical law with the constructed target. For each
fixed list, use bounded tests

    min(B, max_j |P_2(t_j,u_j)|^p).

Convergence in probability of their empirical averages implies convergence
of expectations. Inserting `1_(E_n)` changes these expectations by at
most `B P(E_n^c)`. The finite envelope moment bound then bounds the target
expectation by `(Kp)^p`, independently of list length. Send `B` to infinity
and enlarge the finite lists within a countable dense family by monotone
convergence. L2 continuity supplies an almost-sure subsequence for any
other deterministic query and therefore its domination by the same
envelope. No simultaneous pointwise continuity of every population
representative is needed or asserted. This proves the required reference
exponential RMS tails. Merely invoking W2 convergence for unbounded
`p`-th moments would have been insufficient; the target's bounded
truncations avoid that error.

A competing strong raw reference solution has bounded action norms and
residuals on a compact interval. Integrating its readout equation gives
a bounded readout representative. Its scalar first-row equation has the
clock representation by the scalar ODE and Fubini. Apply (17) using the
constructed solution as the tail-bearing endpoint. Osgood gives uniqueness
without any tail assumption on the competitor. Restriction of the already
constructed path gives existence at reached restarts. The conditional
finite-GF capture follows from the same triangle argument; admitted fixed
observations use the compact-target cutoff already available in CH3.

Finally, target lines 321–355 identify a real remaining issue. At depth
three the cavity subtraction contains

    [phi'(z_2)-phi'(z_2^(i))] P_2^(i).

An RMS cutoff leaves an additive cavity tail. Restoring the ordinary
Euclidean susceptibility multiplies that additive error by `sqrt(n)`.
The scalar Osgood comparison sufficient for qualitative convergence does
not by itself prove a width-uniform `O(1)` Euclidean susceptibility or its
linear-in-p moment bound. No step of sections 1–4 supplies that estimate.
The target preserves this distinction correctly. The conditional result
does not establish a supported-law radius or raw-GD capture for nearby
laws, and it does not meet the remaining C-X3 obligations.

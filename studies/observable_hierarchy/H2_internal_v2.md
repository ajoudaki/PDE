# Internal mathematical audit of H2 candidate v2

**Verdict: no blocking mathematical defect found within the stated C-H1
observation contract.** The candidate gives an admissible finite population
construction and a complete direct comparison to the established canonical
GF, conditional only on the supplied established dependencies. The main
source defect tends to zero by strong operator approximation on compact
target sets, rather than by an assumed tail estimate for the approximations.
The suggested changes below clarify existing implications; they do not
replace a missing convergence argument.

This is an internal audit, not an independent promotion review. The earlier
direct-hierarchy route was frozen before this candidate was read. The full
candidate and the complete previously read C-H1/dependency packet were used;
no other study or outside route was consulted. The numerical prototype and
source-synchronization assertions about maintained files were not checked.
No training experiment was performed.

Audited artifact: `studies/observable_hierarchy/H2_candidate_v2.md`, 466 lines.

SHA-256:

    00f2ff10a6240f28df2d53158ea9f267d6d20162a5784e3f4de5221e4f93edd4

The candidate was read in full and was not edited by this auditor.

## 1. Finite-state admissibility and initialization

The saved state consists of two joint laws and one finite matrix:

    Γ₁ = Law(b₁,g,w),     Γ₂ = Law(b₂,c),     M∈R^(d₂×d₁).

The first law has dimension `d₁+4`, the second dimension `d₂+1`.
The frozen `b` coordinates are finite initialized observable vectors with
an explicit finite Gaussian-program provenance. They are not arbitrary
functions supplied as marks. The moving row `w∈R²` and scalar `c` are
expressly admitted C-H1 neuronal observables. Neither law contains a row
of the original middle matrix or its parameter density.

The strongest alternative interpretation is that `M` merely renames a
representative dense network's middle weights. The construction does not
have that form. Its indices enumerate initialized observable features,
not neurons. At fixed N the neurons still range over two probability
populations with nonlinear current coordinates; their population laws
are not empirical laws of `d₁` and `d₂` neurons. The initialization matrix
`D=U₂* A₀ U₁` is deterministic and obtained from Gaussian contractions.
Its dimensions and coefficients are independent of the original width.
The actual finite-population action is a finite feature kernel, not an
arbitrarily resampled Gaussian middle array. Finite particle quadrature
could approximate these laws, but is not the mathematical construction.

All required within-population correlations are retained in Γ. For example,
`E₁[b tanh(w·u)]` uses the joint law of frozen features and current rows.
Replacing it by a product of marginals would change the equations; the
candidate does not make that replacement. Cross-layer neuron pairings are
neither stored nor needed.

### Grammar and a conservative count

The tree grammar exhausts finite rational-marked initialized C-H1 words:

* signed integer numerators `s(p)` and positive denominators `q+1`
  enumerate every rational;
* scalar multiplication and same-population addition generate rational
  affine expressions, including constant offsets;
* the unary functions, bounded products, and both typed action directions
  are direct constructors;
* every constructor references smaller codes, since each unpaired integer
  is at most `k` and the parent code is `4+8k+j`;
* unfolding a finite DAG produces a finite tree, so using trees does not
  omit shared-node observations.

Invalid code references are skipped in their causal order. The extra
addition constructor `j=7` is redundant but harmless.

The pilot has fourteen nodes and eight bounded outputs: five in population
1 and three in population 2. A code prefix contributes at most `N+1`
outputs, hence

    d₁+d₂ ≤ N+9,
    (d₁+4)+(d₂+1) ≤ N+14,
    d₁d₂ ≤ (N+9)²/4.

These conservative bounds already count duplicates. They verify the
candidate's looser `N+15` population-dimension bound. The matrix entries,
two law domains, and frozen/current joints are explicit. For a requested
output tuple of length k, its law is a pushforward on `R^k`; it is an
output of the fixed saved population law, not an additional retained state.

Initialization also has a finite constructive count if one is wanted.
Compute the unnormalized bounded words first. For `D`, append the calls
`A₀ ψ₁,j`, then form all cross contractions with `ψ₂` and normalize by
finite matrix multiplication. This uses at most `N+15+d₁≤2N+24` word
nodes before the deterministic normalization. It is equivalent to calling
`A₀ b₁,j` by linearity. Thus no hidden infinite action list is required
to define the saved initial laws or matrix.

Every nonconstant normalized feature is a finite linear combination of
bounded initial words. Singular source covariances remain covered by H6.
The ridge normalization does not require inverting a singular empirical
Gram or assuming continuity of such an inverse. Both directions are
initialized in one finite union with their response corrections. In
particular, transposing D preserves the retained reverse contractions;
it does not claim that a reverse Gaussian answer has no innovation.

## 2. Ridge filters, density, and both directions

Write `S a=ψᵀa`, `G=S*S`, `U=S(G+ηI)^(-1/2)`, and
`Q=UU*=S(G+ηI)^(-1)S*`. Then

    U*U = (G+ηI)^(-1/2) G (G+ηI)^(-1/2)
         = G(G+ηI)^(-1) ≤ I.

Consequently U and U* are contractions, and Q is a positive contraction.
For `v=S a`,

    (I-Q)v = η S(G+ηI)^(-1)a.

Diagonalize G. On its eigenvalue λ the norm multiplier is
`η sqrt(λ)/(λ+η)≤sqrt(η)/2`, including λ=0. It follows that

    ||(I-Q_N)S_N a||₂ ≤ sqrt(η_N)||a||/2.

For a vector from a fixed earlier span, zero-pad its unnormalized ψ
coefficients; that coefficient norm does not change. Since `η_N→0`, the
error tends to zero. For an arbitrary vector in the initialized observable
space, approximate it by such a fixed span and use `||I-Q_N||≤1` on the
approximation error. The bounded Fourier-cylinder density result from
C-H1 supplies precisely this dense span. Rational marks suffice by finite
graph L² approximation with bounded action norms and locally uniform
bounded-node envelopes. The initial `z₂⁰(v)` seeds are generated from g
and A₀ and introduce no additional independent fields.

Thus Q converges strongly to the identity on each initialized observable
space. Its normalization need not be nested coordinate by coordinate;
only the unnormalized lists and their spans are nested.

The following useful bound is implicit in the candidate and should be
displayed when the global estimates first use it:

    D_N = U₂,N* A₀ U₁,N,       ||D_N||op ≤ 2.              (A1)

It follows from the two contraction bounds and the established canonical
initialized action norm. Therefore

    B_N=U₂,N D_N U₁,N*=Q₂,N A₀ Q₁,N,
    B_N*=Q₁,N A₀* Q₂,N,       ||B_N||op≤2.

For v in the first observable space,

    ||B_N v-A₀v||₂
      ≤2||(Q₁,N-I)v||₂+||(Q₂,N-I)A₀v||₂ →0.

The same calculation for A₀* proves reverse strong convergence. The spaces
are a reducing pair for A₀ by C-H1, so all arguments lie in the spaces
where convergence was proved. On a compact set, approximate by a finite
net and use the uniform operator bound on the distance to that net. This
proves uniform strong convergence on compact sets in both orientations.

This argument does not claim norm convergence of B_N to A₀. Such a claim
would generally be false for a noncompact initialized action, and is not
needed later.

## 3. Exact coefficient gradient and global fixed-N flow

Use the fixed mark spaces carrying `(b₁,g)` and `b₂`. With w, c, and M
variable, the finite model is

    a=E₁[b₁ tanh(w·u)],  z₂=b₂ᵀ M a,
    f=E₂[c tanh(z₂)],    d=E₂[b₂ c φ'(z₂)],
    q=b₁ᵀ Mᵀ d,         φ=tanh.

For an arbitrary matrix perturbation H,

    δ_M f[H]=E₂[c φ'(z₂)b₂ᵀH a]=dᵀH a
             =〈d aᵀ,H〉F.

For a row perturbation v, differentiating a and then the preceding scalar
pairing gives

    δ_w f[v]=E₁[φ'(w·u)q(u)(v·u)].

For readout perturbation h, `δ_c f[h]=E₂[h tanh(z₂)]`.
Multiplying each derivative by `2(f-y)`, integrating μ, and taking the
negative gradient in the stated L²/Frobenius product metric gives exactly
equations (5). There is no missing factor of n, two, or Gram matrix.

In particular, the coefficient metric is the ordinary Frobenius metric on
M. It is **not** the metric on K induced by a possibly dependent feature
list. Confusing these metrics would incorrectly introduce a Gram inverse.
The coefficient metric is deliberately chosen to generate Q filtering.
With `K_N=U₂(M-D)U₁*`,

    K_N' = -2∫ r_N (U₂d)⊗(U₁a) dμ
          = Q₂ F_K(w_N,A_N,c_N) Q₁.                       (A2)

Here `U₂d=Q₂Δ₂,N` and `U₁a=Q₁H₁,N`; the rank identity verifies every
factor. This is the exact middle equation needed by the comparison.

The scalar derivatives are legitimate along the fixed-N characteristic
paths: features b have finite supremum bounds, g is fixed, tanh and its
derivatives are bounded, and the local characteristic increments and c
are bounded. Dominated differentiation and actual finite-matrix adjunction
therefore yield

    L_N' = -||w_N'||₂²-||M'||F²-||c_N'||₂².

Since `L_N(0)=∫y²dμ≤Y²`, Cauchy–Schwarz gives `∫|r_N|dμ≤Y`. Hence

    ||c_N(t)||∞≤2Yt,
    ||a(u)||≤1,             ||d(u)||≤||c_N||₂≤2Yt,
    ||M'||F≤4Y²t,           ||M-D||F≤2Y²t²,
    ||M||op≤2+2Y²t².

The first two contraction estimates use the static b marginals of Γ,
which are preserved. Integrating

    ||w_N'||₂≤4Y²t(2+2Y²t²)

gives exactly the row bound in (8). On any fixed finite interval,

    ||w_N'||∞≤4Y²t L₁||M||op

controls the row increment `w-g` in the local existence norm. The
candidate does not need an N-uniform L∞ feature envelope: fixed-N
envelopes suffice for existence, and the comparison uses only the
N-uniform action/L²/readout bounds.

The integral contraction construction on bounded
`L∞×L∞×R^(d₂×d₁)` sets applies to the displayed vector field. The energy
bounds prevent escape on any finite time interval, and the bounded speeds
give endpoint limits in those same norms. Thus the local construction
extends globally for each fixed N. Taking pushforwards produces positive
probability solutions of the continuity equations. The characteristic
solution class is stated explicitly; no uniqueness theorem for arbitrary
uncontrolled weak solutions is being inferred.

## 4. Saved-current-state restart

At a reached time the joint current laws include all local variables
appearing in the drift and all frozen feature coordinates. To restart,
sample the current laws themselves and treat their current w/c values as
initial labels for new characteristics. This is a proof representation
of the saved laws, not a new stored coordinate field.

The drift is locally Lipschitz in moving values and current contractions,
using the same fixed feature bounds. Coupling identical current samples
at restart gives zero initial discrepancy; the same integral contraction
or its continuation estimate forces identical future characteristics
and laws. The saved M and fixed initialization data determine all action
calculations. No earlier conditional correlation is missing, because
the b/w and b/c correlations are already in Γ. The claimed own-reached-
state restart therefore follows. It is not an assertion of canonical
restart from every possible formal hierarchy state.

## 5. Canonical invariance and actual source decay

The canonical comparison is legitimate on one carrier. Apply C-H1's
invariance argument at its actual initial state with the same μ. It proves
that canonical future w and c remain in the initialized observable
spaces and that K and K' are supported between them. This is exactly the
reached-state domain covered by that argument. It does not require a
formal hierarchy to be dynamically realizable.

The three source terms in candidate (10) really tend to zero:

1. `{H₁(t,u):t≤T,u∈S¹}` is compact in L² by joint continuity on the
   compact parameter domain. Strong-compact convergence of B_N applies.
2. The same is true of `{Δ₂(t,u)}`. Subtracting c and then applying the
   bounded-multiplier lemma proves joint L² continuity of this field.
   Strong-compact convergence of B_N* applies.
3. `K':[0,T]→S₂` is continuous. For a rank `a⊗b`,

       Q₂(a⊗b)Q₁=(Q₂a)⊗(Q₁b),

   so convergence in HS norm follows from strong Q convergence and the
   rank difference inequality. Approximate any HS operator by a finite
   sum of such ranks using its square-summable matrix entries; Q
   contractions control the remainder. A finite net of the compact K'
   curve then makes the convergence uniform in time.

These prove `ε_N→0` for every separately fixed μ. No effective rate or
uniform law-ball rate is needed by the claim. The target-dependent
quantities are only proof errors. Every approximation order, ridge,
coefficient, and initial law was fixed without them. Thus this use of
the known path is not trajectory-dependent initialization or playback.

## 6. Comparison and identification

Let `A_N=B_N+K_N`, `A=A₀+K`, and use candidate (9). Both trajectories
have N-uniform raw/action bounds. The exact forward expansion is

    A_NH₁,N-AH₁
       =A_N(H₁,N-H₁)+(K_N-K)H₁+(B_N-A₀)H₁.

This yields (11). The upper backward expansion uses bounded reference c:

    Δ₂,N-Δ₂ = φ'(Z₂,N)(c_N-c)
                     +[φ'(Z₂,N)-φ'(Z₂)]c.

Its L² norm is bounded by `C(e_N+ε_N)`. Applying the adjoint expansion
from (12) then gives the same bound for `q_N-q`. The only remaining
unbounded gate multiplier is the reference q, and splitting it at R gives

    ||[φ'(w_N·u)-φ'(w·u)]q||₂
       ≤2R||w_N-w||₂+2τ_R(q).

This is precisely the established one-reference mechanism. It does not
assume tails for q_N or any other arbitrary approximate action output.

For the middle block, (A2) gives candidate (14) exactly. Its first term
is controlled by the rank difference estimate and Q contractions. Its
second term is the proved HS source error from §5. No small operator-norm
difference between B_N and A₀ has been smuggled into the estimate.

Combining the three component inequalities yields

    e_N'≤C(1+R)(e_N+ε_N)+CM exp(-aR),    e_N(0)=0.

All constants here are independent of N; the established target supplies
the tails. The norm derivatives exist almost everywhere and are bounded
above by the corresponding velocity difference, including at zero norm.
For `v=e_N+ε_N+η∈(0,1]`, choose `R=1+a⁻¹log(1/v)`. Then

    v'≤L v log(e/v),
    log(e/v(t))≥exp(-Lt)log(e/v(0)).

Exponentiating gives candidate (16). For sufficiently small `ε_N+η`,
its upper bound is below one throughout `[0,T]`, which validates the
cutoff by first exit. Letting η decrease to zero gives uniform e_N
convergence. This includes the case `ε_N=0`.

The limiting object is therefore the already established actual
canonical GF. Neither formal-hierarchy uniqueness nor a new dynamic
lifting theorem is used. The construction fixes `T=1/200` and one
positive law radius independently of N, with no restriction to atomic
or orthogonal-input laws. Equation (11) directly controls the whole
circle uniformly, so no unproved interpolation of input marks is needed.

## 7. All C-H1 joints, powers, and second moments

Every fixed C-H1 graph is evaluated by the specified finite feature
kernel and local coordinate operations on Γ. For its action node,

    A_NV_N-AV=A_N(V_N-V)+(K_N-K)V+(B_N-A₀)V.

The first two terms tend uniformly to zero by the proved convergence
and norm bounds. The last tends uniformly to zero on the compact
target node curve. The adjoint expansion is identical with reversed
types. The frozen upper seed uses D, so the same initialized-action
argument applies and its derivative is exactly zero.

All bounded nodes have a common finite envelope at fixed graph marks.
In particular, for any separately fixed integer p≥1, putting `C=2YT`
gives

    |c_N^p-c^p|≤p C^(p-1)|c_N-c|.

Thus arbitrary fixed powers of the bounded readout, including their
use in later bounded products or action operands, are covered. The
candidate does not accidentally restrict to first powers of c.

For a bounded continuous gate multiplying an L² field, uniformity in
time can also be checked by contradiction: a failing sequence of times
has a convergent subsequence; uniform convergence of the arguments and
continuity of the target curves reduce it to one application of the
strong bounded-multiplier lemma. No unrestricted L² algebra estimate
is required.

For k fields on one population, their actual canonical-carrier coupling
gives

    W₂²(Law(V₁,N,...,V_k,N),Law(V₁,...,V_k))
       ≤Σ_i ||V_i,N-V_i||₂².

It therefore gives the claimed joint convergence uniformly in time,
with true second moments and quadratic pairings. Initial/current
observations use the same coupling; there is no replacement by separate
marginal laws. Both action orientations and arbitrarily nested but
separately fixed C-H1 programs are included.

The finite-network interpretation of the limiting object is exactly the
established C-H1/C.4.7 bridge. Its finite Gaussian readout remains in
place. The population zero readout is its limit, not a change to the
finite model. The candidate claims no joint growing-order/width rate and
does not need one for its stated population approximation theorem.

## 8. Suggested clarifications and scope

No correction to the equations or convergence mechanism is required by
this audit. The following additions would make the proof easier to check:

1. Display `(A1)`, `||D_N||op≤2`, where the bound on M is first used.
2. Say explicitly that the **unnormalized dictionaries and feature spans**
   are nested. Ridge-normalized coordinates themselves change with N;
   no projective equality of finite-order solution laws is asserted.
3. Keep the theorem's observation claim tied to the C-H1 alphabet. If
   the larger dependency-packet alphabet is also desired, define the
   optional A₀ decoder using D and the K decoder using `M-D`, in both
   orientations. Strong B_N convergence and HS K_N convergence already
   prove the analogous fixed-graph result. This extension is not needed
   for the current C-H1 statement.
4. Keep the separate characterizations visible: fixed-N existence uses
   finite feature supremum bounds, whereas N-uniform convergence uses
   contraction/operator bounds and canonical reference tails. An
   N-uniform L∞ bound for b is neither proved nor needed.

The model is an exact-real population construction. Gaussian quadrature,
floating ridge normalization, conditioning, and numerical integration
remain additional approximations. This theorem-only audit does not
certify a prototype or practical C-H3 complexity. It also does not replace
the repository's independent promotion-review and user-approval process.

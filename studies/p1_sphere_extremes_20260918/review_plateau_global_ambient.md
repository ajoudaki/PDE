# Within-study cross-audit of the global and ambient plateau candidates

Status: completed analytical cross-audit, 2026-09-18. No experiment was
run. This is not a fresh isolated review, an external review, or a
promotion authorization. Frozen input files were preserved.

## Provenance and frozen inputs

The reviewer independently derived and froze `plateau_finite_critical.md`
before reading either candidate below. During that derivation, the
supervisor sent a sketch of a nonzero-middle, loss-8/9 ambient state.
That exposure was explicitly recorded in the independently frozen
report; the sketch was not used there. Only after freezing did the
reviewer read both candidate files completely for this assigned audit.
Thus the independently derived saddle theorem provides corroboration,
but this report is transparently a within-study cross-audit rather than
a fresh isolated verdict.

SHA-256 of the complete reviewed files:

| File | SHA-256 |
|---|---|
| `plateau_global_convergence.md` | `24536587cf5d83d7208127b7c4af1470f813728f364175eff493269ef5ea5e53` |
| `plateau_ambient_counterexample.md` | `e0cba915f6a1d7a9bd83e0b88045320d8eddce79fcfd9083cdfb48f5b6df4d54` |
| Previously frozen `plateau_finite_critical.md` | `c39efcc8ed4b553b7a0b3bca06a21bbb743593911730168152e96d887159906d` |

The exact canonical initialization/equations and complete assigned
`terminal_geometry.md`, `architectural_loss_floor.md`, and
`initialization_positivity.md` had already been read for the independent
derivation. The same-data fitting checks below use the fully read
`terminal_geometry.md`; no additional protected-family result is needed.
No other study, experiment, or unassigned scientific source was used.

## Verdict and one correction

The finite-time strict-descent theorem, the independent-input
strict-saddle theorem, both explicit full-row-rank loss-8/9 constructions,
their negative-curvature conclusions, and the same-data initialized
fitting statements pass the checks below. No substantive gap was found
in those proofs. Their conclusions remain finite-state or specifically
initialized-family results, as declared. Universal initialized fitting
remains open.

One correction is required in the global route's **description of its
remaining gaps**, not in its proved theorems. Its lines 54–58, 353–360,
and the final ledger row at line 374 list `M_*=0` as an additional
possible nonoptimal finite initialized endpoint. For every nonstationary
canonical trajectory this is already excluded:

\[
 \mathcal L(t_0)<1\quad(t_0>0),\qquad
 \mathcal L(t)\le\mathcal L(t_0)\quad(t\ge t_0),
\]

whereas a finite state with `M=0` has every upper activation and prediction
zero, hence `L=1`. Continuity of loss at a finite strong endpoint or
accumulation point supplies the contradiction. In the stationary case,
the initialized trajectory is already globally minimizing, and its middle
matrix is the nonzero `D` anyway. The corrected unresolved alternatives
are approach to a nonoptimal strict saddle with nonzero middle matrix,
or failure to produce a finite strong endpoint/accumulation point.

This is overcautious bookkeeping rather than an invalid positive theorem.
The frozen input is left unchanged; a synthesis should use this correction.

## 1. Canonical equations, metric, and strict finite-time descent

Both reports use the exact canonical correlated lower marks, positive
ridge normalization, independent upper coordinates, all entries of the
full nonconstant `3 x 6` matrix, and its actual transpose. Removing the
constant coordinates is legitimate in the initialized odd sector; each
omitted feature pairing and its matrix-gradient row/column is zero.
Every perturbation used in either report is also odd in the appropriate
population marks, so each is an admissible direction in that same sector.

For the unhalved loss and physical population/Frobenius metric,

\[
 D\mathcal L=2\sum_i\mu_i r_i Df_i,\qquad
 \theta'=-\nabla\mathcal L,
 \qquad \mathcal L'=-\|\theta'\|_{\rm physical}^2.
\tag{R1}
\]

The displayed gradients in global Section 2 agree with direct
differentiation: `D_M f_i=d_i a_i^T`, the lower reverse coefficient is
`b_1^T M^T d_i`, and `D_c f_i=H_i`. There is no extra population weight
inside the already weighted L2 gradient and no missing factor two.

At a finite time where `L'=0`, every velocity is zero almost surely,
including the finite matrix velocity. In the declared characteristic
state space this is a stationary state. The vector field is locally
Lipschitz in bounded lower displacement/readout and the matrix norm, so
the reversed local equation has the same uniqueness property. The
original trajectory therefore agrees locally backward with the constant
one, and uniqueness on the bounded finite prefix extends that agreement
to initialization. Thus a nonstationary trajectory cannot reach a
critical state at finite time.

The initialized stationarity characterization in
`architectural_loss_floor.md` supplies the remaining premise: only
`L_odd=1` laws are stationary at initialization, and these already achieve
their architectural minimum. Every other law has `L'(0)<0`, hence
`L'(t)<0` at every finite time. This proof supplies no uniform negative
upper bound for `L'` over an unbounded horizon, and the global report
correctly does not infer one.

## 2. Independent-input lower perturbations

For independent `u_i`, dual vectors `t_i.u_j=delta_ij` exist, including
when fewer than three active inputs remain. The matrix

\[
 S_i=E_1[b_1b_1^T\operatorname{sech}^4(w\cdot u_i)]
\]

is positive definite: each lower gate is positive almost surely at a
finite state, and the unweighted lower Gram is positive definite for
the exact correlated marks. The conditional reverse Gaussian variance
is positive, so the lower `(h,k)` covariance does not collapse; the
ridge Cholesky transform is invertible. No independence of `h` and `k`
has been substituted for their actual joint law.

For the proposed perturbation
`delta w=t_i sech^2(w.u_i) b_1^T S_i^{-1} A`, differentiation gives

\[
 \delta a_j=
 \delta_{ij}E_1[b_1b_1^T\operatorname{sech}^4(w\cdot u_i)]
                        S_i^{-1}A=\delta_{ij}A.
\tag{R2}
\]

The perturbation is bounded because marks and gates are bounded and
`S_i^{-1}` is a fixed finite matrix. It is odd, since its scalar gate is
even and the `b_1` factor is odd. For `j!=i`, the scalar argument
`w.u_j` is actually unchanged along the whole straight perturbation,
so the claim that only input `i` contributes mixed hidden/readout terms
is justified beyond first order as well. Large inverse norms do not
invalidate an individual bounded direction; they only preclude a uniform
curvature estimate, which the report does not claim.

Criticality and independent inputs also give
`lambda_i M^T d_i=0`. For the selected nonzero `lambda_i`, it follows
that every `d_i^T M A=0`, as used to make the lower perturbation's first
prediction differential vanish.

## 3. Confluent Vandermonde and upper feature separation

The upper law has positive density on an open cube. A putative L2
dependence among the continuous upper features therefore holds throughout
that cube. Grouping signed duplicate nonzero effective vectors leaves
at most three representatives. A generic line through the origin has
nonzero products `t_j=e.z_j` with pairwise distinct squares `x_j=t_j^2`.

Along this line, the derivative feature is
`s t_1 sech^2(s t_1)=s(d/ds)tanh(s t_1)`. Therefore its coefficient at
degree `2n+1` is `(2n+1)` times the corresponding tanh coefficient.
The four coefficients used for `n=0,...,3` are indeed
`1,-1/3,2/15,-17/315`; none vanishes. The proposed dependence reduces
to

\[
 \sum_j C_j x_j^n+B(2n+1)x_1^n=0,
                 \qquad n=0,\ldots,k.
\]

Writing `P(x)=sum_n p_n x^n=product_j(x-x_j)` and taking the combination
with coefficients `p_n` yields

\[
 0=\sum_j C_jP(x_j)+B[2x_1P'(x_1)+P(x_1)]
   =2B x_1P'(x_1).
\tag{R3}
\]

The product derivative is nonzero because all roots are distinct, and
`x_1>0`, so `B=0`. The remaining ordinary Vandermonde equations force
all `C_j=0`. Thus the derivative feature is outside the current feature
span. This verifies the confluent argument including its nonzero-root
hypothesis and exact polynomial identity.

For a zero effective vector, the derivative feature is the nonzero
linear function `b.z`. There are then at most two nonzero feature
representatives. The odd coefficients of degrees `3,...,2k+1` form an
ordinary Vandermonde matrix multiplied by nonzero diagonal factors
`t_j x_j`; they annihilate every proposed ridge coefficient. The linear
coefficient then contradicts `e.z!=0`. The empty-span case is immediate.
All cases in global Section 3.2 are covered.

## 4. Mixed Hessian and physical factors

Set `psi=G_i-P_VG_i` as in the global report. This is a bounded odd
function with `||psi||_2>0`. Its readout prediction differential vanishes
because it is orthogonal to each `H_j`. The lower direction also has zero
first prediction differential by (R2) and criticality. Hence the bilinear
Hessian of the loss is

\[
 D^2\mathcal L[\delta w,\psi]
 =2\sum_j\mu_j r_j D^2f_j[\delta w,\psi]
 =2\lambda_i\|\psi\|_2^2.
\tag{R4}
\]

The pure readout second loss derivative is zero. Expanding in the
combined direction `(delta w,s psi,0)` doubles the mixed bilinear term,
giving exactly `4s lambda_i ||psi||_2^2` in the report's equation (7).
There is no missing factor of two or weight. A finite coefficient `s`
of suitable sign gives negative curvature, irrespective of the finite
pure lower Hessian term. Smooth differentiation and fixed-direction
Taylor expansion are justified by the bounded marks, state increments,
readout, and tanh derivatives. Full row rank of `M` is not used.

This checks the precise independent-input theorem. The independently
frozen `plateau_finite_critical.md` extends the conclusion to dependent
distinct nonantipodal triples by a different lower-separation argument;
that extension is corroborating research, not a premise needed to repair
the reviewed proof.

## 5. Two explicit full-row-rank critical states

In both constructions, the exact initialized lower vectors `a_i` are
nonzero, pairwise orthogonal, and have the same norm. Their coefficients
are `nu/a` and `beta eta/((nu+eta)b)`, including the ridge subtraction.
The first is positive; the positivity of the second is also justified
by the assigned initialization results. No empirical coefficient is used.

In global Section 4, `p_i=a_i/R^2` gives `p_i.a_j=delta_ij`, while the
displayed `n_i` are normalized, mutually orthogonal, and orthogonal to
all `a_j`. Therefore the matrix rows in (8) are nonzero and orthogonal,
and `Ma_i=(+e_1,-e_1,+e_1)`. In the ambient report, the first row is
`(a_1+a_2+a_3)^T/A`, with `A=||a_i||^2`, and the other two rows lie
orthonormally in the three-dimensional perpendicular complement. These
rows also give rank three, now with `Ma_i=e_1` for every `i`.

Let `Z=b_(2,1)`, `H=tanh Z`, and `J=Z sech^2 Z`. The projection of `H`
off `J` is nonzero: their Taylor cubic coefficients differ after their
linear coefficients fix the only possible proportionality constant.
Equivalently, `H/J=sinh(2Z)/(2Z)` is nonconstant on the positive-density
interval. Thus every displayed readout denominator is strictly positive.
The chosen readout has `E[cH]=1/3` and `E[cJ]=0`. Its remaining reverse
coordinates vanish by independence and centering of the other upper
marks, giving `d_i=0` exactly in both constructions.

For the global report's all-positive labels, the feature signs are
`(+,-,+)`, predictions are `(1/3,-1/3,1/3)`, and
`sum_i mu_i r_i H_i=0`. For the ambient report's labels `(+,+,-)`, all
features are `H`, predictions are `(1/3,1/3,1/3)`, and
`sum_i mu_i r_i=0`. The lower and matrix gradients vanish because
`d_i=0`; the preceding identities eliminate the readout gradient. Both
unhalved losses are `(4+16+4)/27=8/9` in the appropriate ordering.
Both states preserve boundedness, odd parity, exact static marks, and
the full actual-transpose equations.

The ambient report also supplies a directly checked descending direction:
`delta M=e_1 a_3^T/A` changes only effective vector three and
`zeta=J-P_span(H)J` obeys `q=E[zeta J]=||zeta||_2^2>0`. Every first
prediction variation is zero, while

\[
 D^2f_3=2s q+E[cZ^2\tanh''Z],\qquad
 D^2\mathcal L=2(1/3)(4/3)D^2f_3
             =\tfrac89[2s q+E[cZ^2\tanh''Z]].
\tag{R5}
\]

This verifies its factor `8/9`, the sign choice, and the strict-saddle
claim independently of the global general theorem. Matrix full row rank
persists for sufficiently small perturbation size by openness of a
nonzero rank-three minor. The same construction disproves a positive
global PL bound relative to the zero minimum: its loss is positive and
its complete gradient vanishes.

## 6. Same-data initialized fitting and the remaining dynamical gap

The global report's example uses `u_i=e_i,y_i=1`, directly covered by the
signed-axis theorem of `terminal_geometry.md` with every label positive.
The ambient report's positive-axis inputs with labels `(+,+,-)` require
the additional signed-coordinate conjugacy it states. That conjugacy is
valid for the exact canonical marks, without assuming arbitrary rotation
invariance.

Here is an explicit check. Let `S=diag(1,1,-1)` on input/upper coordinates
and `P=diag(S,S)` on the two lower feature blocks. Negate the corresponding
lower Gaussian and reverse-noise coordinates, and the upper Gaussian
coordinate. These measure-preserving involutions, denoted `T_1,T_2`, obey

\[
 b_1(T_1\omega)=P b_1(\omega),\quad
 g(T_1\omega)=Sg(\omega),\quad
 b_2(T_2\omega)=S b_2(\omega),\quad S D P=D.
\]

The last equality uses the exact scalar-diagonal bands of `D`, including
both bands. Transform states by

\[
 \bar w(\omega)=S w(T_1\omega),\quad
 \bar c(\omega)=c(T_2\omega),\quad \bar M=SMP.
\]

Changing variables in the population integrals gives
`bar a(u)=P a(Su)` and `bar f(u)=f(Su)`. These state transformations are
isometries for the physical metric, preserve initialization, and conjugate
the losses for data `u_i` and `S u_i` with unchanged labels. Their complete
gradient flows are therefore conjugate. The reflected data are
`(e_1,e_2,-e_3)` with labels `(+,+,-)`, exactly the supplied theorem's
family `u_i=y_i e_i`. Its fitting conclusion transfers to the original
positive-axis triple. This verifies the claimed same-data distinction:
the constructed ambient saddles are not limits of those canonical flows.

Finally, the report's auxiliary gradient-flow example
`E(x,y)=x^2+(y^2-1)^2` has the stated trajectory
`(exp(-2t),0)`, energy `1+exp(-4t)`, and endpoint Hessian `diag(2,-4)`.
It correctly disproves the general inference that strict finite-time
descent plus strict-saddle geometry excludes deterministic saddle
approach. It is explicitly separated from the canonical model. Likewise,
finite-time bounds do not establish an all-time strong accumulation point;
boundedness in this population state space would not by itself establish
strong compactness. Apart from the removable `M_*=0` entry identified
above, the reports' stated dynamical gaps are justified and remain open.

## Post-repair verification

The supervisor revised the global report after the cross-audit above.
The reviewer then reread that entire revised file and checked its new
SHA-256:

`114986a7865eda0924a45cd34e09d786431dab3c4a22f11d0c643f6dab134c05`.

The ambient report was rehashed and remains unchanged at
`e0cba915f6a1d7a9bd83e0b88045320d8eddce79fcfd9083cdfb48f5b6df4d54`.
The original hashes and correction above remain the record of what was
first reviewed; this paragraph records the repaired version separately.

**Repair passes.** The status header, opening gap paragraph, Section 5,
and final ledger now consistently exclude a finite initialized endpoint
with `M_*=0` using strict descent below loss one. Section 5 correctly
distinguishes this exclusion from a sequence with `M -> 0` and unbounded
readout: such a sequence need not have a finite strong endpoint and is
not ruled out by the finite-state argument. The remaining stated gaps
are deterministic saddle approach and control of finite endpoints or
accumulation points.

The strict-descent, independent-input perturbation, upper separation,
mixed Hessian, and explicit critical-state theorem/proof/construction
equations are unchanged on rereading, so checks (R1)–(R5) continue to
apply. No new scientific claim, experiment, source edit, or independent
review status is introduced by this repair verification. The single
correction requested by this cross-audit is resolved.

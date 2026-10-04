# Geometric query transport and self-consistent bilinear feedback

2026-09-30. Scoped theory and frozen experiment protocol. This note is
unreviewed research within the existing study. Initial scientific inputs
were the complete kernel route, scalar module, circle results, and decoder
audit. The supervisor subsequently authorized the nine saved scalar
endpoints and exactly two passive decoder tests. No dense training or new
scalar training is authorized in this subtask.

## Decision and coefficient provenance

The existing completion is a selected fourth-order kernel term, not the
true fourth-order feature response. Its large off-training effect is
transported through a poorly conditioned initial feature geometry. These
are separable problems. Two parameter-free passive transports are frozen
below. A more substantive bilinear feedback closure is then derived; it is
not part of the present endpoint experiment.

All coefficients are contractions of the same width-1024 Gaussian
initialization, regenerated with seed streams `[1,1]` and `[1,101]`, or the
saved exact contractions. No coefficient uses a trained dense output. Dense
endpoints are evaluation targets only. There are no evolving neurons,
histograms, training samples of an initial population, fitted trajectories,
or query-grid-dependent training states.

Put alpha=2/m and retain the original definitions K0,S,z,J,P,M,N,fcub.
Write D=y+r-fcub(train). For a query x define the row vectors

    b_x[i] = alpha^2 sum_bc J[bc] S[(x,i),(b,c)],
    B_x[a] = k_x[a] + alpha^2 sum_bc C[x,a,b,c] J[bc],

where C is the existing combined cubic decoder tensor. At training inputs,
b_train=M.T and B_train=K0+M+M.T+N. The second identity follows by
J+J.T=z z.T. All expressions are explicit functions of the saved state.

## Frozen passive candidate G: moving features

    G = K0+M.T
    f_G(x) = fcub(x)+(k_x+b_x) solve(G,D).

This is the exact interpolation obtained by writing a correction readout
delta_c in span{H_i}, evaluating it against the quadratic moving features
H_x+h2,2,x, and requiring its training values to equal D. Indeed, if
delta_c=sum_i v_i H_i, its training values are Gv and its query value is
(k_x+b_x)v. At every training alias the formula returns y+r exactly.

The interpretation is exact for this reconstructed correction, not for the
unknown true neural fifth-order correction. D=O(a^5) and b,M=O(a^2), so its
difference from the original decoder is O(a^7) for a fixed coercive dataset.
It therefore leaves all existing cubic coefficients unchanged. It is a
rational continuation of a chosen higher-order correction.

It needs no additional dynamic state and one separate query B tensor
S[(x,i),(b,c)] with q*m^3 static scalars. That tensor cannot in general be
recovered from the combined C. Matrix G need not remain invertible for
arbitrary labels; an ill-conditioned solve is a recorded failure, with no
ridge, pseudoinverse, clipping, or alternate decoder substituted.

## Frozen passive candidate T: cubic tangent geometry

    B = K0+M+M.T+N
    f_T(x) = fcub(x)+B_x solve(B,D).

The correction is transported by the same instantaneous cubic tangent
geometry used to differentiate fcub. It aliases exactly and differs from
the original decoder at O(a^7) for small labels. Its geometric motivation
does not identify the true fifth-order feature dynamics. It adds no
dynamic state and needs only the existing C and k_x coefficients. We
require B to be positive definite and well conditioned; failure is
retained, with no PSD projection substituted. Neither passive candidate
changes the original training trajectory, training loss or fitted endpoint.

## Frozen endpoint experiment

Run both G and T on all nine unchanged saved original endpoints. The
canonical circle metric is raw RMS difference from the saved dense output
on all 256 angles. Also report original errors, correction RMS, smallest
eigenvalues (for symmetric B), 2-norm condition numbers and every alias
error. Each prediction must be finite; the solve condition must be at most
1e10; maximum alias error must be at most 1e-8. Regenerated initial K0
must agree with its saved value to 1e-12. Reconstructed original predictions
must agree with saved predictions to 1e-10.

The primary discriminator for a substantial repair is at least a factor
two error reduction on both near_pair_sin9 and cluster_triple_cos9, with
no absolute error increase exceeding 0.05 on another task. Passing supports
this passive transport only, not the missing dynamics or a uniform theorem.
Failure on either difficult task rejects the candidate as a joint repair
of those failures. Invalid numerical gates are inconclusive. Every task
and failure remains in the report. There are no hyperparameters, selection
among amplitudes, additional endpoints or conditional training branches.

Hard execution budget: 20 seconds total for the endpoint process, one
BLAS thread, exactly 18 decoder evaluations, no integration. Save products
under data/generated/structured_full_rank_scalar_20260926/
cubic_feedback_repair_20260930/geometric_decoder/. Existing products are
not overwritten. The script and this pre-result note are hashed before
execution. Any post-result update is appended separately below.

## Frozen dynamic candidate F: bilinear feedback in aggregate coordinates

The stronger candidate replaces cumulative frozen-readout forcing with
the current projected readout. Keep v in R^m and Theta in R^(m*m), both
initialized to zero, and form

    M[i,a] = sum_bc Theta[b,c] S[(a,i),(b,c)],
    b_x[i] = sum_bc Theta[b,c] S[(x,i),(b,c)],
    f_F,train = (K0+M.T) v,
    r = f_F,train-y,
    v' = -alpha (I+solve(K0,M)) r,
    Theta' = -alpha outer(r,v).

These equations close with m^2+m training scalars. There is no separate r
or z state and no skew compression: feedback destroys the old identity
J+J.T=z z.T. Static training storage remains K0,S of order m^4. The
training equations retain no width-sized objects. The naive RHS cost is
O(m^4), plus an m-dimensional solve with the fixed initial Gram.

Let Phi_bc be the initial hidden-parameter gradient feature whose Gram
is S[(b,c),(d,e)]. Represent a hidden displacement theta=sum_bc
Theta_bc Phi_bc and a readout c=sum_i v_i H_i. Replace h2,x by its
first-order hidden-parameter expansion H_x+D h2,x theta. The resulting
finite bilinear prediction is exactly (k_x+b_x)v. The displayed equations
are its gradient flow, with readout metric K0 and the original hidden
parameter metric. Differentiation gives the positive training kernel

    K_F = (I+solve(K0,M)).T K0 (I+solve(K0,M)) + N(v),
    N(v)[q,a] = sum_ic v[i] v[c] S[(q,i),(a,c)],
    r' = -alpha K_F r.

PSD follows from two Gram constructions, and at r=0 every derivative
vanishes. This is an exact gradient identity for the specified bilinear
surrogate, not for the original tanh network. The two consequential
feedbacks are moving features in v' and moving readout in Theta'. Their
leading orders are v=-alpha*z+O(a^3), Theta=alpha^2*J+O(a^4), so K_F
has exactly the same order-zero and order-two training kernel as the
original cubic scheme. The quartic completion now belongs to an actual
coupled model rather than an independently added residual kernel term.

The direct query readout lacks the cubic component of readout motion
orthogonal to span{H_i}. Restore precisely that component with passive
integrals T[a,b,c]'=r[a]*Theta[b,c], T(0)=0. Define

    d[i] = sum_abc T[a,b,c] S[(a,i),(b,c)],
    f_F(x) = (k_x+b_x)v
             -alpha*(sum_abc T[a,b,c] S[(a,x),(b,c)]
                     - k_x solve(K0,d)).

The bracket is identically zero at every training input. Since
T=alpha^2*P+O(a^5), it restores the missing cubic coefficient at every
query, without feeding query states back into training. Thus the total
dynamic state count is m^2+m+m^3. Query coefficients are k_x and the two
separate response slices A and B, totaling q*(m+2*m^3) static scalars.
Shuffle identities verify the cubic equality: z_i J_bc is the sum of
P_i;bc, P_b;ic and P_b;ci, accounting for the three B contributions;
the extra bracket supplies the missing A contribution.

This feedback candidate is frozen as written, with no future-dense
coefficient fit. Strong-learning fidelity, large-motion tanh saturation,
global-in-time approximation accuracy, and any useful error bound remain
open. In particular the feature map is still linearized, so this candidate
does not contain the genuine fourth-order hidden-feature curvature.

## What a true joint fourth-order Gram would need

The exact quadratic-feature norm is
Q_ab=<h2,2,a,h2,2,b>. It is not M.T solve(K0,M). Their difference is
the Gram of components of h2,2 orthogonal to span{H_i}, hence PSD.
Knowing only cross-Grams with H_i does not determine that orthogonal Gram.
Computing Q requires additional initialization contractions with six
training indices (two feature-response pairs and two observation indices).
Even Q alone omits cross-Grams with the genuine fourth-order feature
motion and the fourth-order backward tangent corrections. It is therefore
incorrect to present either Q or the artificial completion as the true
next-order neural kernel. Its positive sign also prevents arguing that
adding this omitted norm must damp the current overshoot.

The present proposals are distinct: G and T test passive geometric
transport; F restores self-consistent feedback in a bilinear approximation;
none claims to compute the full fifth-order neural output.

## Endpoint experiment result (appended after the frozen test)

Both variants completed all nine unchanged endpoints in 1.1617 seconds;
there was no training. All conditioning, coefficient reproduction, finite
prediction and training-alias gates passed. The raw RMS results are:

| Task | Original | Moving features G | Cubic tangent T |
|---|---:|---:|---:|
| pair_cos3 | 0.121253 | 0.080603 | 0.080124 |
| pair_orthogonal_cos1 | 0.045205 | 0.043281 | 0.042975 |
| near_pair_sin9 | 1.205628 | 0.677354 | 0.731767 |
| cluster_triple_cos9 | 1.337774 | 0.726065 | 0.770426 |
| cluster_triple_cos1 | 0.042561 | 0.040290 | 0.042593 |
| triple_wide_mixed | 0.007535 | 0.007197 | 0.007225 |
| quartet_mixed | 0.039916 | 0.034833 | 0.034190 |
| broad_ridge6 | 0.043183 | 0.040030 | 0.038437 |
| alternating3 | 0.089800 | 0.085130 | 0.086229 |

Neither candidate passes the frozen factor-two reduction on both difficult
tasks. G improves every task, but leaves large errors 0.677 and 0.726.
T leaves 0.732 and 0.770. These are failed proposed complete repairs with
useful causal evidence: transport through the initial feature geometry
amplifies the error, but changing that transport alone is insufficient.
There are no hidden excluded cases or fitted coefficients.

Executable: cubic_geometric_decoder_repair.py. The saved manifest contains
the pre-result protocol and script hashes. Per-task NPZ products include
the separate A and B query slices, so a later explicitly authorized feedback
test can reuse initialization coefficients without repeating width-sized
work. All raw gates and metrics are in the run's results.json.

## Feedback implementation and algebra checks (no training)

The supervisor authorized implementation of F for root-owned round-two
training. cubic_bilinear_repair.py supplies BilinearModel(labels,K0,S),
rhs, initial_state, residual, predict(state,query_gram,query_A,query_B),
blocks, size and training_size. It uses the minimal v,Theta state and
derives the residual algebraically; its counts are exactly m^2+m for
training and m^2+m+m^3 with passive query integrals.

A deterministic no-integration check used seed 8091, m=3, a synthetic SPD
K0 and paired PSD S. It directly differentiated the bilinear training
prediction and compared it to -alpha*K_F*r. It checked arbitrary passive
integral states against exact training aliases, exact stopping when labels
equal the current training prediction, positivity, and the cubic decoder
identity on a two-segment residual path whose third integrals were computed
analytically. Maximum gaps were 4.45e-16 for the gradient identity,
1.49e-16 for aliases, and 1.39e-17 for cubic consistency. The tested kernel's
smallest eigenvalue was 0.9898. This validates implementation identities,
not strong-learning fidelity; this subagent ran no training solve.

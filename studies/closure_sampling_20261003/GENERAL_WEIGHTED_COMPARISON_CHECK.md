# Reconstruction of the general weighted comparison

2026-10-03. Internal complete reconstruction of
`GENERAL_WEIGHTED_COMPARISON.md`, SHA-256
`8f8363e36dd6575a0ac490181e7e8c17924ab94669fa209c3526b4b32f35c4f3`.
The allowed input is that complete note, the canonical normalization,
and the previously assigned source/cubature notes. Section 7's prior carrier
theorem is accepted only as its explicitly named proposition; its other-study
source and checks were not fetched. This is a collaborative check, not an
independent promotion review and not a proof of general complex regularity.

**Result:** Sections 1--6 give a valid deterministic conditional implication.
The only trajectory assumptions beyond small-label fitting are the stated
real carrier maximum and simultaneous paired source approximations. The
amplification is linear-exponential in the carrier bound, with no factor
depending on the physical horizon. It does not require special first-layer
coordinates, orthogonal data, or a positive lower bound on selected masses.
The corrections needed in the source text are presentational: two occurrences
of `,quad` should be `,\\quad`, and rho_n should be defined explicitly as
the original residual RMS. Zero labels are the trivial stationary branch;
the positive epsilon assumption concerns Y>0.

## 1. Exact normalization and weighted geometry

Use the source's notation: v_a=x_a/sqrt(d), c_a=y_a-f_a,
rho=||c||_m with ||c||_m^2=m^{-1}sum_a c_a^2, and mean squared loss.
The original gradient equations have factors 2/m in the first weights and
readout and 2/(mn) in hidden matrices. In the selected model the empirical
hidden pairing is replaced by D_{ell-1}; thus its hidden rank-one matrix is

\[
 \frac2m\sum_a c_a\delta_a^{(\ell)}h_a^{(\ell-1)\top}D_{\ell-1}.
 \tag{C1}
\]

Its Hilbert--Schmidt norm is calculated after conjugating by
D_ell^{1/2} and D_{ell-1}^{-1/2}. A single rank-one term has exactly
the product ||delta||_{D_ell}||h||_{D_{ell-1}}. The same calculation
shows the weighted adjoint is D_{ell-1}^{-1}B^T D_ell. All inverse
masses occur inside this Hilbert-space representation; no estimate replaces
a weighted norm by an unweighted coordinate maximum.

For a first-weight perturbation E, ||Ev_a||_{D_1} is at most the
weighted Frobenius norm of E times |v_a|. Thus general finite data enter
only through fixed input norms and pairings. The first-weight term in the
tangent Gram is the Gram of delta_a^(1) tensor v_a, including all
nonorthogonal cross terms.

Writing inner products with the empirical masses or selected D_ell,
direct differentiation of the forward pass gives

\[
 \dot f_a=\frac2m\sum_b c_b K_{ab},\qquad
 K_{ab}=\langle h_a^{(L)},h_b^{(L)}\rangle
 +\sum_{\ell=2}^L
   \langle\delta_a^{(\ell)},\delta_b^{(\ell)}\rangle
   \langle h_a^{(\ell-1)},h_b^{(\ell-1)}\rangle
 +\langle\delta_a^{(1)},\delta_b^{(1)}\rangle v_a^\top v_b.
 \tag{C2}
\]

Therefore dot c=-(2/m)Kc exactly. Every summand is a Gram matrix.
If the top readout Gram is at least gamma I, the damping rate in the
sample RMS norm is 2 gamma/m. Absorbing this fixed factor into kappa
is consistent throughout the note; no 2/m normalization is lost.

## 2. Initialization and independent fitting

Let U_ell be a basis normalized by U_ell^T U_ell/n=I. Matching the
constant and all r_ell(r_ell+1)/2 basis products gives at most one plus
that many selected nodes. To verify elimination, if more nodes have
positive masses, their feature-product vectors are linearly dependent.
Because the constant is included, a nonzero dependence has both signs.
Move along it until the first mass reaches zero. All moments and positivity
are preserved. Repetition terminates with the asserted count.

The selected basis map is an isometry from coefficient Euclidean space
into the weighted neuron space; its weighted adjoint has norm one. The
middle coefficient matrix in the projected mixer is
U_ell^T W_0 U_{ell-1}/n, whose norm is at most ||W_0||. These facts
prove the initial operator bound and both orientation identities on paired
vectors. Inclusion of each initial training activation and its true forward
image inductively reproduces the complete initialized training pass. Exact
top-feature pairing preserves its Gram gap. Inclusion of all A_0 columns
also preserves the initial weighted first-weight Frobenius RMS.

For either the full or compressed model let S(t)=int_0^t rho(s)ds.
Bounded activations and zero readout give ||w||_infty<=CS. On a fixed
hidden operator tube, descending through bounded gates gives each backward
response RMS at most CS. Integrating (C1) gives hidden Hilbert--Schmidt
increments CS^2; the first-weight equation gives the same bound in its
weighted Frobenius norm. Forward subtraction through fixed depth gives
feature RMS displacement CS^2. Hence the readout Gram changes by CS^2.

Choose a fixed small S_0 so that this change uses at most half the initial
gap and every operator increment stays strictly inside its tube. Then (C2)
gives rho(t)<=Y exp(-kappa t) while S<=S_0. The consequent bound
S<=Y/kappa prevents the first exit for sufficiently small fixed Y.
All state norms stay finite. At any fixed selected system, positive masses
make these genuine finite-dimensional norms, so finite coordinate escape
is excluded. No quantitative constant here depends on the smallest mass.

For a bounded query set, ||dot A||, ||dot B|| are at most CY rho and
||dot w|| at most C rho. Differentiating its forward pass gives feature
speed at most C_X Y rho; the output speed is consequently at most
C_X rho. Integrating the exponential residual tail proves

\[
 |f(t,x)-f(T,x)|\le C_{\mathcal X}Y e^{-\kappa T}
 \quad(t\ge T, x\in\mathcal X),
 \tag{C3}
\]

including t=infinity. This is a separate property of each autonomous
model, so the tail transfer does not impose common residuals after T.

## 3. Selected norms, products, and all mixer orientations

If ||s-v||_infty<=epsilon with v in S_ell, then

\[
 \|s_I\|_D\le\|v_I\|_D+\epsilon
 =\|v\|_2/\sqrt n+\epsilon
 \le\|s\|_2/\sqrt n+2\epsilon.
 \tag{C4}
\]

For source pairs s,t, insert their approximants. Their mutual inner product
is exact by cubature. All other terms contain an error vector with empirical
or selected norm at most epsilon, and a source or approximant with bounded
norm. This proves the O(epsilon) pairing estimate, including sources at
different times. If both sources are backward responses, their source and
approximant norms are O(Y) because epsilon<=Y; the sharper pairing bound
is O(Y epsilon). The weaker displayed O(epsilon) bound is sufficient.

The readout also has a source-space approximation with coordinate error
CY epsilon. This need not assume a measurable choice of approximants:
approximate its continuous time integral by finite Riemann sums and replace
each source in the sum by an admissible approximant. The distance of each
sum to S_L is bounded by the same summed error; pass to the limit using
the 1-Lipschitz distance to the closed finite-dimensional subspace. This
proves the claimed distance bound without ever storing the integral
coefficients or evaluating them in the algorithm.

For each ell>=2, the forward initial action error follows from a paired
approximant v,W_0v: subtract v from the true lower feature, apply the
bounded projected operator to the selected remainder, and subtract the
selected forward-source remainder. This costs C epsilon in the upper
weighted norm. The learned-matrix remainder is

\[
 \frac2m\sum_a\int_0^t c_a(s)\delta_a^{(\ell)}(s)_I
 \left[\langle h_a^{(\ell-1)}(s)_I,h^{(\ell-1)}(t,x)_I\rangle_D
       -\frac{h_a^{(\ell-1)}(s)^\top h^{(\ell-1)}(t,x)}n\right]ds.
 \tag{C5}
\]

It has weighted norm at most CY^2 epsilon using (C4), pairing error,
and residual activity. In particular it is O(epsilon).

For every ell<L, the reverse learned remainder has exactly the form

\[
 \frac2m\sum_b\int_0^t c_b(s)h_b^{(\ell)}(s)_I
 \left[\langle\delta_b^{(\ell+1)}(s)_I,
                   \delta_a^{(\ell+1)}(t)_I\rangle_D
       -\frac{\delta_b^{(\ell+1)}(s)^\top\delta_a^{(\ell+1)}(t)}n
 \right]ds.
 \tag{C6}
\]

Its initial action is controlled by the independently required paired
reverse approximant. Thus every reverse defect is O(epsilon). This covers
all hidden orientations, including the carrier entering the first layer.
At the top the carrier is the readout itself, which is retained exactly in
the proof reference. No separate top mixer is missing. Finally the readout
pairing defect follows from (C4) applied to w and the top query feature.

The reference matrix norm is bounded by integrating selected response RMS
O(Y), selected feature RMS O(1), and residual activity O(Y). Its first
weights move by CY^2 because the selected delta^(1) source is explicitly
included in S_1. Merely assuming upper-layer sources would not have sufficed
for this last conclusion; the source statement does include all layers.

## 4. One-reference subtraction and the absence of cubic norm losses

Let d be the source's sum of weighted block distances. First-layer query
preactivation error is bounded by C_X d. At each higher layer, insert the
true selected feature and reference matrix, use (C5), and propagate the
lower forward error through the bounded compressed operator. This proves
all forward errors are C_X(d+epsilon).

At any backward layer use precisely

\[
 \delta_C-\delta_I
 =\phi'(z_C)(k_C-k_I)+[\phi'(z_C)-\phi'(z_I)]k_I.
 \tag{C7}
\]

The first multiplier is bounded. The second is at most C M times the
forward error because the actual selected reference carrier has maximum M.
The carrier difference at ell<L is

\[
 B_C^*(\delta_C^{(\ell+1)}-\delta_I^{(\ell+1)})
 +(B_C-B_R)^*\delta_I^{(\ell+1)}
 +[B_R^*\delta_I^{(\ell+1)}-k_I^{(\ell)}].
 \tag{C8}
\]

The terms cost respectively C times the next response error, CY d, and
C epsilon. The top carrier difference is the readout difference. Descending
through fixed depth gives C(1+M)(d+epsilon). The M contribution is added
at each gate and propagated only by bounded operators and gates, so it
does not become M to the power L.

This expansion resolves the potentially dangerous weighted products. No
estimate multiplies three arbitrary L2 vectors. The only product of two
coordinate-dependent differences is avoided by (C7): the gate difference
is multiplied by the true reference carrier, for which the explicit L-infinity
assumption is available. Rank-one products use products of two norms.
Scalar products use Cauchy--Schwarz. The compressed carriers may have very
large individual coordinates at tiny selected masses; no step bounds them
by converting their RMS norms into a coordinate maximum.

## 5. Tangent-Gram damping and accumulated comparison

Compare each scalar pairing in K_C first to its selected reference pairing
and then to its empirical reference pairing. Forward differences cost
C(d+epsilon), backward differences C(1+M)(d+epsilon), and both models'
backward RMS norms are O(Y). The source pairings cost C epsilon by (C4).
In the product of a forward Gram and backward Gram, use
ab-a'b'=(a-a')b+a'(b-b'), with both undifferenced factors bounded.
Thus

\[
 \|K_C-K_n\|_{\mathrm{op}}
 \le C(1+M)(d+\epsilon).
 \tag{C9}
\]

This step compares actual tangent Grams. It does not differentiate the
observation error, which would require additional derivative source bounds.

Put u=c_C-c_n. Exact residual equations give

\[
 \dot u=-\frac2m K_Cu-\frac2m(K_C-K_n)c_n.
 \tag{C10}
\]

The preserved compressed Gram gap and (C9) imply

\[
 D^+\|u\|_m\le-\kappa\|u\|_m
      +C(1+M)\rho_n(d+\epsilon),\qquad u(0)=0.
 \tag{C11}
\]

The zero-norm case follows by regularizing the norm and letting its positive
regularizer vanish, or by the upper Dini derivative. Integration and the
nonnegative terminal value give

\[
 \int_0^t\|u\|_m\le C(1+M)\int_0^t\rho_n(d+\epsilon).
 \tag{C12}
\]

For velocity subtraction write a typical hidden contribution as
(c_C-c_n)delta_C h_C^T+c_n(delta_C h_C^T-delta_I h_I^T).
The residual-difference term uses the independently bounded compressed
RMS norms. Split the remaining outer product into one backward difference
and one forward difference; use (C7)--(C8). First-layer velocities use
the same response difference times the fixed input, and readout velocities
use the forward difference. Hence

\[
 d(t)\le C\int_0^t\|u\|_m
       +C(1+M)\int_0^t\rho_n(d+\epsilon).
 \tag{C13}
\]

Substituting (C12) leaves a single coefficient C(1+M), not its square.
The scalar integral inequality implies

\[
 d(t)\le\epsilon\left[
       \exp\left(C(1+M)\int_0^t\rho_n(s)ds\right)-1\right]
 \le C(1+M)e^{C(1+M)Y}\epsilon.
 \tag{C14}
\]

For example apply the integrating factor to the right side of (C13) after
adding epsilon; its derivative is bounded by C(1+M)rho_n times itself.
The total residual integral is CY, so no T-dependent factor occurs.
Forward subtraction and the readout pairing defect transfer (C14) to
queries. Adding the separate tails (C3) proves the all-time estimate.

## 6. Complexity and dependency boundary

If every source dimension is at most R, cubature uses O(R^2) nodes per
layer, and fixed depth gives O(R^4) matrix entries plus smaller first-weight,
readout and mass storage. This count includes fixed and moving coordinates.
The reference state, original matrices, source spaces and cubature bases are
proof/setup objects and do not appear in the runtime equations.

Under M<=C_0 sqrt(log(en)), choose D larger than the fixed coefficient
in exp(CM). Then

\[
 (1+M)e^{CM}\,\frac{n^{-1/2}e^{-D\sqrt{\log(en)}}}{\log(en)}
 \le Cn^{-1/2}.
 \tag{C15}
\]

The exponent and logarithm signs are correct. The accuracy adjustment has
log(1/epsilon)=O(log n); therefore a source-space dimension polynomial in
that logarithm and inverse strip widths remains polylogarithmic. Taking
T=C_T log(en) absorbs the two fitting tails. For each fixed Y>0,
epsilon<=Y holds at sufficiently large n. For Y=0 all outputs are zero
identically and no comparison argument is necessary.

Sections 1--6 do not derive the input spaces, their dimension, or their
initialization-only provenance. They assume those objects explicitly. Section 7
invokes a named prior real-carrier theorem only to provide M of order
sqrt(log n), under its stronger bounded C3 activation hypotheses and
canonical initialization conditions. I did not independently recheck that
prior theorem. Even accepting it leaves all actual complex-source and
initialization-only approximation obligations open for arbitrary depth/data.
In particular W^(ell) dot h^(ell-1) needs its own coordinate bound;
neither this reconstruction nor (C14) supplies it.

The deterministic implication is therefore verified as stated, with the
minor notation repairs above. It creates no unconditional arbitrary-depth
or nonorthogonal-data sampling theorem by itself.

## 7. Confirmation of the coordinator's revision

I read the complete revised source at SHA-256
`71f0f3671d03cb7c76eb34cb13d9c4a8e25ee17bd28ef29bccd044dd3fd3493b`.
It explicitly defines rho_n, separates Y=0, repairs both quad commands,
and incorporates the Riemann-sum argument from Section 3 above. These
changes preserve and clarify the verified mathematical implication. A
character scan identifies one remaining typesetting defect in revised
equation (7): a formfeed character precedes `rac2m` where the TeX fraction
command belongs. The coordinator was notified; replacing that character
by a backslash is a purely typographical repair. The corresponding control
character in this check's equation (C15) has been repaired, and the
activation route file was checked and contains no such characters.

The coordinator subsequently repaired that final fraction command. The
verified final source SHA-256 is
`1dcb779135b616aa66be4cd830d2bd2f3217a56eeae8f3cdf7394a52262a4306`.
This final change is typographical and leaves the reconstructed equations
and conclusion unchanged.

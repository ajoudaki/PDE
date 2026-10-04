# Internal check of the finite-jet neuron cubature construction

2026-10-03. Scoped internal mathematical check, not an independent isolated
promotion review. No experiment, trained-path evaluation, Git operation,
or edit to the source note was performed.

**Verdict: PASS for the stated finite-jet theorem.** The retained spaces,
weighted mixer and adjoint, moment induction, and neuron counts are
consistent. The initialization-derived setup does not require a trained
trajectory. This verdict does not certify the requested all-time
root-width prediction guarantee, which the source explicitly leaves open.

The complete source checked was
`NEURON_GLOBAL_POSITIVE.md`, SHA-256
`0509450305e7f73809283ebde33a46c30c7e7db3f6fc487154c432dcdea4e21c`.
Sections 1--5 were reconstructed in detail. The displayed arguments in
Section 6 were also checked, conditional on its cited history-domain and
regularity estimate; those separate history artifacts were not read or
recertified for this assignment. The manuscript's original residual-RMS
closure and its deterministic all-order fitting argument supply the model
and fitting conventions. Required canonical-notation, rigorous-proof,
and research-audit instructions were applied.

## 1. Source spaces and exact mixer actions

The source uses $A=W^{(1)}$, $W=W^{(2)}$, and readout $w$, with the
original normalized prediction $w^\top h^{(2)}/n$. Its vectors
$h_{a,k}^{(\ell)}$ and $\delta_{a,k}^{(2)}$ are actual physical-time
derivatives at zero, without division by $k!$. Their setup is legitimate
for $Y>0$: at fixed finite $n,q$, the raw vector field is analytic near
the initialization, since $\tau(0)=1$ and the argument of the square
root defining $\rho(0)=Y$ is positive. Differentiating this finite vector
field generates any prescribed finite jet using initialization and labels.
The zero-label case is stationary and needs no construction.

Let $S_1,S_2$ be the source's two spaces, and let
$V^\top V/n=I_r$, $U^\top U/n=I_s$ be their empirical orthonormal
bases. The positive rules satisfy

\[
 V_I^\top D_1V_I=I_r,\qquad U_J^\top D_2U_J=I_s.
 \tag{1}
\]

These identities preserve every bilinear pairing between vectors in
the corresponding space, not just squared norms. For example, if
$u=V\alpha$ and $v=V\beta$, then
$u_I^\top D_1v_I=\alpha^\top\beta=u^\top v/n$.
Matching symmetric basis products suffices for (1), because every matrix
entry of these Grams is one of those products.

Define, exactly as in the source,

\[
 B=U^\top W_0V/n,\qquad
 B_0=U_JBV_I^\top D_1.
 \tag{2}
\]

The weighted adjoint is

\[
 D_1^{-1}B_0^\top D_2
   =V_IB^\top U_J^\top D_2=B_0^*.
 \tag{3}
\]

There is no missing width factor: the population contractions in the
reduced model use $D_1,D_2$, while the full model uses $1/n$.
Furthermore, $V/\sqrt n$ and $U/\sqrt n$ are Euclidean isometries,
so $\|B\|_{\rm op}\le\|W_0\|_{\rm op}$. The selected basis
matrices are weighted isometries by (1), and their weighted adjoints
are contractions. Consequently
$\|B_0\|_{D_1\to D_2}\le\|W_0\|_{\rm op}$ as claimed.

For every included forward jet, $h_{a,k}^{(1)}\in S_1$ and its
image $W_0h_{a,k}^{(1)}\in S_2$. If
$h_{a,k}^{(1)}=V\alpha$, then the image equals $UB\alpha$;
(1)--(2) therefore imply

\[
 B_0(h_{a,k}^{(1)})_I=(W_0h_{a,k}^{(1)})_J.
 \tag{4}
\]

For every included upper backward jet,
$\delta_{a,k}^{(2)}\in S_2$ and
$W_0^\top\delta_{a,k}^{(2)}\in S_1$. Reversing the same calculation
gives

\[
 B_0^*(\delta_{a,k}^{(2)})_J
    =(W_0^\top\delta_{a,k}^{(2)})_I.
 \tag{5}
\]

Thus the construction preserves both directions of the same fixed source
on every needed derivative vector. It does not assume that either
source space is invariant under the mixer on all its vectors.

## 2. Induction on the actual closure jets

The key span statements are correct. Differentiating a forward-moment
equation produces linear combinations of first-feature derivatives;
differentiating a backward-moment equation produces linear combinations
of upper backward-field derivatives. The coefficients are scalar
derivatives of $r_a,\rho,\tau^{-1}$ and the fixed Legendre mixing
coefficients. The constant forward prefix belongs to $S_1$, and the
backward prefix is zero. All orders of a moment needed through order
$p$ therefore lie in the spaces already listed. Positive-order readout
derivatives of order $k$ are linear combinations of upper-feature
derivatives of orders at most $k-1$, and the initial readout vanishes.

Assume the reduced raw-state jets through order $k$ agree with the
selected full coordinates, and the scalar clock jets agree. The required
computational order is then:

1. The first-feature jets agree by componentwise composition with tanh.
2. In the upper preactivation, the fixed-source term agrees by (4).
   Every learned-mixer term is an upper backward-moment jet times a
   scalar pairing between a lower forward-moment jet and a lower
   feature jet. Both vectors in that pairing lie in $S_1$, so (1)
   preserves it, including across different samples and memory modes.
3. Upper features agree by componentwise composition. Prediction jets
   are pairings between readout jets and upper-feature jets, all in
   $S_2$, so they agree by (1). Hence residual and residual-RMS jets
   agree; $\rho(0)>0$ justifies differentiating the square root.
4. Upper backward jets agree by the coordinatewise readout/gate formula.
   The fixed transpose action agrees by (5). The learned transpose
   contracts an upper backward-moment jet against an upper response jet;
   both lie in $S_2$. Its pairing is preserved by (1), and the lower
   gate agrees. Thus the lower backward jets agree.
5. The raw update equations give the next first-matrix, readout, clock,
   and moment derivatives.

Initialization closes the base case: the selected first rows give the
selected first features; (4) gives selected upper preactivations; readout,
predictions, and backward moments are zero; forward prefixes and clocks
match. This proves all stated derivatives through $p$. The proof can even
compute matching raw-state derivatives of order $p+1$ from the included
order-$p$ fields, but this extra fact is not needed by the proposition.

The weighted learned reconstruction has the correct normalization:

\[
 W_C=B_0-\frac2{m\tau_C}\sum_{a,j<q}(2j+1)
     \bar\delta_{C,a,j}^{(2)}\bar h_{C,a,j}^{(1)\top}D_1.
 \tag{6}
\]

Its weighted adjoint replaces the trailing $D_1$ by $D_2$ and exchanges
the two moment factors. Thus both contractions in the preceding induction
are the exact reduced versions of the original $1/n$ pairings. The source
keeps the original physical-time equations and residual clock. It does
not substitute dense-flow derivatives for order-$q$ closure derivatives.

## 3. Neuron count, stored state, and autonomy

Counting the listed spanning vectors gives

\[
 r\le d+2m(p+1),\qquad s\le3m(p+1).
 \tag{7}
\]

There are $r(r+1)/2$ symmetric products downstairs. Matching their
empirical mean by affine-dependence elimination, together with mass one,
uses at most $1+r(r+1)/2$ selected indices. The upper count is
$1+s(s+1)/2$. Eliminating zero weights leaves strictly positive
weights on the retained support. Degenerate or zero source spaces cause
no problem; the rules may then consist of one mass-one node. The support
also cannot exceed the original finite population size.

For $K$ fixed passive probes, only their lower feature jets, upper
feature jets, and forward mixer images are added. They do not drive the
loss, so no query backward-response vectors are needed. This gives

\[
 r\le d+(2m+K)(p+1),\qquad s\le(3m+2K)(p+1),
 \tag{8}
\]

and exactly the same forward/prediction induction handles their jets.

The exact moving count is

\[
 dN_1+N_2+mq(N_1+N_2)+1.
 \tag{9}
\]

For fixed $d,m,K$, this is $O((p+1)^2q)$ and the retained neuron
counts are $O((p+1)^2)$. No factor of $q$ is missing from the source
span count: every one of the $q$ moment modes uses the same finite list
of feature or response derivatives, with different scalar coefficients.
Setup time and the computation of those coefficients may depend strongly
on $q$; the theorem does not claim otherwise.

Fixed storage is separate. A materialized $B_0$ uses $N_1N_2$
entries, or $O((p+1)^4)$ for fixed data dimensions, while its displayed
factorization can use fewer. The positive masses are also fixed data.
The original width-$n$ arrays and derivative vectors are used during
setup and can then be discarded. They are not consulted during the
reduced training or query evaluation. Learned mixer actions can be
evaluated from (6) without storing a dense moving $N_2\times N_1$
matrix.

This is a meaningful finite autonomous model: the retained first rows,
readout, moments, and clock determine every future update, and the model
can restart from these values. Computing initial derivatives from the
known finite vector field is not a trained-path oracle. There is no
claim that this preprocessing is cheap or numerically well conditioned;
arbitrarily small positive weights and large derivatives could obstruct
a subsequent numerical or approximation theorem without invalidating
these exact algebraic identities.

## 4. Fitting is correctly conditional in the checked version

Equation (1) preserves the initial upper training Gram because every
initial training feature lies in $S_2$. It preserves
$A_{0,I}^\top D_1A_{0,I}=A_0^\top A_0/n$ because every first-matrix
column lies in $S_1$. Thus the initial first-layer RMS bounds are
inherited, as is the fixed-mixer norm bound from (2)--(3).

The current proposition explicitly requires fixed deterministic
initialization bounds, a positive training-Gram gap, and sufficiently
small labels before asserting fitting. This is the right scope. The
weighted proof uses weighted Euclidean and Hilbert--Schmidt norms,
bounded tanh gates, and the identity
$\|u v^\top D_1\|_{\rm HS}=\|u\|_{D_2}\|v\|_{D_1}$.
The Legendre estimates hold in these finite Hilbert spaces, so the
fitting bootstrap does not introduce an inverse minimum mass.

An earlier formulation read during this check did not make these
additional hypotheses explicit. It has been corrected in the checked
version. Without them, fitting would be false for arbitrary finite
initializations: $A_0=W_0=0$, zero readout, and a nonzero label gives
stationary zero features and no fitting. This correction leaves the
unconditional finite-jet theorem unchanged. The source's Section 6 now
also distinguishes the original and revised prefix hashes, so its
provenance statement reflects that correction.

## 5. Checks of the stated approximation limitations

The Gaussian analytic-radius lemma in Section 3 is correct. For every
fixed derivative order, the random displacement has enough moments to
differentiate in $L^2$. A positive $L^2$ Taylor radius would imply
almost-sure absolute scalar convergence at every sufficiently small
fixed radius, by Tonelli. The actual scalar radius is the distance to
the nearest tanh pole divided by the magnitude of the displacement;
the unbounded conditional Gaussian displacement makes that radius
arbitrarily small on events of positive probability. This contradicts
the proposed positive common radius. The lemma concerns the displayed
affine response field, as stated; it is not a theorem that the complete
neural trajectory has zero Taylor radius.

The finite empirical-radius estimate for independent Gaussian pairs
also has the correct tail scaling. The strip counterexample
$\tanh(\pi t/(4r))^{p+1}$ has a zero of order $p+1$ and modulus at
most one in $|\operatorname{Im}t|<r$, while becoming close to one
at long real times unless its power is exponentially large. Its use as
a limitation of a proposed continuation argument is sound.

Taylor's integral remainder in Section 4 is valid at each fixed finite
$n,q$ where the error is differentiable, and the source correctly
identifies the missing derivative bound. The all-order fitting estimates
control the far-time variation under their fitting hypotheses, but do
not control the high derivative in that Taylor remainder. Matching
finitely many probes likewise does not establish the continuum-query
norm. The resource calculation
$Nq=n^{2\gamma+1/6+o(1)}$ conditional on $p=n^{\gamma+o(1)}$ is
correct; it is explicitly not a proved fidelity choice.

## 6. Bounded check of the added history discussion

Conditional on the cited domain statement for
$\mathcal L_Ah=-[\xi(A-\xi)h']'$ and its bound $B_A$, the spectral
identities in Section 6 are consistent:

- The weighted squared coefficient bound follows from the Legendre
  eigenvalues $j(j+1)$.
- Holder's inequality gives the claimed $\ell^p$ amplitude sum for
  $p>2/5$; its summability exponent is
  $4p/(2-p)>1$ for $p<2$.
- Multiplication by the fixed $W_0$ preserves the bound up to
  $\|W_0\|_{\rm op}$ even for an endogenous history.
- The rank-$J$ temporal truncation bounds the squared Hilbert--Schmidt
  tail, and $J s_{2J}^2\le\sum_{k>J}s_k^2$ gives the stated
  $s_{2J}=O(B_AJ^{-5/2})$ estimate.

The two-sided conditional Gaussian formula is also valid for the stated
predictable matrix-query transcript. Its residual covariance projects
onto matrices of the form $(I-P_D)X(I-P_H)$, and the forward
cross-covariance is
$[v^\top(I-P_H)w/n](I-P_D)$ for next predictable vectors $v,w$.
The source correctly refuses to apply this formula to a temporal
coefficient that uses the not-yet-revealed future path.

Finally, the displayed one-sample acceleration is exact:
$\ddot h^{(1)}(0)=2y\operatorname{diag}(\operatorname{sech}^4a)
W_0^\top u$. Its contraction against the revealed upper response is a
nonconstant nonnegative Gaussian quadratic form under the stated
conditioning, rather than a Gaussian scalar. Revealing the reverse
response before the next forward action restores the claimed
predictability and projected covariance. This supports the stated
distinction between temporal coefficient decay and predictable Gaussian
source amplitudes.

These checks validate the implications displayed in Section 6, not its
underlying external history theorem or a neuron-cubature convergence
rate. No unresolved mathematical defect was found in the checked
finite-jet construction. The global approximation claim remains open.

## Version follow-up

After the full check, the source changed its dilation sentence from
"either moment" to "each moment" and updated its version-provenance
paragraph accordingly. Both changed passages were reread. The new full
source SHA-256 is
`00aefc9cbccee65a8d4ddaa603709395d1eace1a2e91d54aa4da7c85389e8819`.
The revised wording states correctly that every forward and backward
moment has the displayed dilation term. No equation, construction,
induction, or substantive theorem claim changed, so the PASS verdict
applies to this version as well.

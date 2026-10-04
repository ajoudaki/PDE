# Exponential cap dependence: fresh combined audit

2026-10-01. **PASS for M_LOG_SCALE_RESULT.md at the frozen versions below.**
The stronger conditional all-time population bound has an error constant
and width threshold at most single exponential in M. This is an internal
check, not promotion. The earlier triple-exponential check is unchanged
and is not used as a premise for this verdict.

## Exact claim and audit scope

The model is the exact smooth q=1 closure in SMOOTH_SETUP.md, including
both gates c_M(s)=M tanh(s/M), the original Gaussian mixer and its actual
transpose, normalized memories, and residual-RMS clock. The training
dataset is fixed, its initial population readout-feature Gram has a
positive gap, and the query law has bounded support.

There is one positive label threshold independent of M>=1. For one
fixed nonzero label vector below that threshold, constants C,c>0 can
be chosen so that

\[
\left(\mathbb E\left[\int\sup_{t\ge0}
 |f_{n,M}(t,x)-f_{\infty,M}(t,x)|^2\,d\mu(x)
 \;\middle|\;\mathcal G_n\right]\right)^{1/2}
 \le \frac{Ce^{CM}}{\sqrt n},\qquad n\ge Ce^{CM},
\]

with P(G_n^c)<=Ce^{-cn}. The event is independent of M. The error includes
the finite-width mean bias and fitted endpoint, and the reference is the
closure's own smooth population at the same M.

I read the complete new synthesis and both new route files, and reread
their substantive repairs before freezing the hashes. The supporting
smooth and cap-dependent notes listed below were read completely in the
same scoped audit context and their needed calculations reconstructed.
No prior verdict is a proof premise, and no other study, numerical
experiment, manuscript change, or Git operation was used. Required
research, rigorous-proof, and canonical-notation instructions remain
applied. The foundational common-action construction is used in the
precise form supplied by CLIPPED_POPULATION_ROUTE.md Section 4; its
underlying maintained-book theorem was not reopened in this scoped check.

One substantive gap was found in the initial stronger draft: an
operator-norm bound alone did not justify a root-width Gaussian gradient
for products of upper feature velocities. The final M_ROW_CAVITY_ROUTE.md
Sections 2a--2c supply the missing coordinate moments and explicit gradient
calculation. The verdict applies to that repaired version.

## 1. Strong covariance concentration: the missing moment is supplied

For prescribed deterministic histories, use activity x in [0,S]. Let
q_a=h'_a be the lower feature velocity and Z_a=W_0 q_a its reused forward
action. Primes here denote activity derivatives. Each q_a coordinate is
bounded by CM and is a smooth finite-graph observable with bounded
fixed-order derivatives. The coordinates of Z_a are not deterministically
bounded uniformly in width.

The passive finite cavity identity gives, for each fixed target time and
coordinate,

\[
Z_{ai}=G^q_a+\sum_c A^q_{ac}d_{ci}
 +\sum_b\int_0^x\lambda_b(u)R^q_{ab}(x,u)d_{bi}(u)\,du
 +\varepsilon^q_{ai}.
\]

This identity precedes scalar-law evaluation and population comparison.
On a fixed cavity operator cutoff, its conditional Gaussian variance is
at most CM^2; its direct atom is bounded; its finite response trace is
at most exp(CM); and its Taylor remainder has every fixed moment bounded
by exp(CM)/sqrt(n). The reinserted d path is coordinatewise bounded by
CS. Thus every fixed coordinate moment of Z is at most exp(CM), without
assuming response-row concentration or the desired mean-law theorem.
Outside the cutoff, the crude bound |Z_ai|<=CM sqrt(n)||W_0||op and the
Gaussian operator tail suffice. Hölder then supplies the same estimate
weighted by any fixed polynomial and exponential in ||W_0||op^2.

The finite state/root Jacobians of q_a,Z_a,z_a,w have ordinary operator
bounds of the form

\[
A_M(K)=C(1+M)^b(1+K)^b
 \exp\{CS_0(1+M+K^2)\},\qquad K=\|W_0\|_{\rm op}.
\]

For Z this uses DZ[v]=DW_0[v]q+W_0Dq[v], including the Gaussian-root
normalization W_0=G_0/sqrt(n). No maximum coordinate of Z occurs.
The exact upper velocity is

\[
d'_a=a_a\odot Z_a+b_a,
\]

where a_a and b_a are coordinatewise bounded and their root Jacobians
have the preceding operator bounds. In the gradient of
X=<d'_a(x),d'_b(y)>_n, the only new quadratic-carrier term is bounded by

\[
\frac{A_M(K)^2}{n^2}
 \sum_i C\bigl(|Z_{ai}(x)Z_{bi}(y)|^2+|Z_{ai}(x)|^2\bigr)
\]

for the squared gradient norm. The weighted coordinate moments just
proved bound its expectation by exp(CM)/n. The remaining terms require
only normalized Euclidean bounds and the ordinary root Jacobians.
Lower-velocity products are simpler because q is coordinatewise bounded.
This validates Gaussian Poincare for all integrands in the two-time
fundamental-theorem expansion of <H_a(x),H_b(y)>_n, for H=h,d.

Subtracting expectations in that expansion and applying Minkowski to its
two edge integrals and mixed double integral proves the covariance
supremum inside L2 at scale exp(CM)/sqrt(n). The mixed derivative uses
one derivative of each time argument and never differentiates lambda,
K', or the residual ratio.

## 2. Strong response rows and the localized tagged moments

For a fixed response source u, write its finite regular trace as
T(x,u)=n^{-1}tr[D_UH(x)Phi(x,u)J(u)], with the bounded deterministic
source coefficient lambda(u) separated. Integrate its target derivative
from x=u, apply Gaussian Poincare there and to the derivative, and then
apply Minkowski. This yields an L2 bound exp(CM)/sqrt(n) for the target
supremum at each fixed source. Integrating |lambda(u)| over sources
gives the required strong response-row norm. There is no source-time
derivative.

For H=d, the derivative (D_Ud)' contains z'=Z plus bounded terms. The
explicit formula in Section 2c has at most one diag(Z) factor in each
trace product. Its Frobenius norm is ||Z||_2<=CM K sqrt(n). A root
variation of any other factor has ordinary Hilbert--Schmidt norm at
most A_M(K)||v||_2; a variation of Z has Euclidean norm at most the
same bound. The trace Hilbert--Schmidt inequality therefore gives a
root-gradient bound A_M(K)/sqrt(n). It does not require an operator
bound on diag(Z). The atom derivative has the same one-Z structure.
Gaussian operator moments give all required L2 estimates above a
width threshold independent of M.

Full-versus-deleted tuples have the same strong scale: ordinary state
deletion bounds control both-time covariance errors, and ordinary
Hilbert--Schmidt Jacobian/source/output deletion bounds control the
response traces before source integration. Consequently the random
cavity tuple is exp(CM)/sqrt(n) close in strong L2 to the full
deterministic expected tuple.

The law route's separate tagged-moment hypothesis is satisfied as well.
Each actual tagged diagonal response is bounded by the product of
operator norms of D_UH, Phi, and J or the upper source matrix. These
bounds hold uniformly in target and source. Their moments are exp(CM);
integrating the source coefficient and adjoining the bounded atom gives
the strong output moment required to discard bad environments. This
does not require concentration of an individual tagged neuron.

## 3. Uniform comparison needs row masses, not uniform densities

The input covariance variances and mean-square increments have common
cap-independent bounds on the fixed operator cutoff, directly from
normalized signal estimates and |c_M(s)|<=|s|. The full expected tuple
has the same bounds after Gaussian averaging, and the constructed
population tuple fits an enlarged common constant. Convex covariance
interpolation preserves them and positive semidefiniteness.

On inputs with response-row masses and upper atom at most B S, the
lower carrier has a Gaussian supremum envelope bounded by
S(L Z_*+CB+C), with Z_* having a fixed sub-Gaussian tail. The estimates
|partial_alpha^j F_M|<=C_j|p| and the uniform bounds for derivatives
containing a p differentiation imply finite Gaussian-averaged total
history-derivative masses through the required fixed orders. After
requiring BS<=1, these constants are independent of M and of the
pointwise response density bound. The upper total-derivative calculation
uses |w|<=CS and the small integrated feedback mass.

Thus the map has strict output row-and-atom bounds C_0 S, where C_0 is
independent of the chosen large B once BS is small. Its two comparison
inequalities are

\[
d_H(\mathcal L D,\mathcal L\widetilde D)
 \le C_LS\,d_D(D,\widetilde D),\qquad
d_D(\mathcal U H,\mathcal U\widetilde H)
 \le C_U d_H(H,\widetilde H).
\]

For random cavity inputs the strong input error is measurable with
respect to the cavity environment. It factors outside the conditional
Gaussian expectation before the total derivative envelope is averaged.
This is why the stronger random norm is sufficient here. There is no
exchange of an expected supremum with a supremum of expectations and
no need for a common deterministic entrywise tensor over large densities.
Singular covariances are allowed by the inverse-free interpolation.

The proof correctly does not call this an invariant covariance-regularity
domain. A narrow peak in Q_h can survive in the upper output term
A(x)Q_h(x,u)A(u), and rapid target variation can enlarge output covariance
increments. Only output row masses and the comparison inequalities are
used. The physical inputs' covariance regularity is supplied separately.

## 4. Localization and event-localized consistency

On a prefix where the deterministic mean lower row and upper
row-plus-atom norms are at most B S, strong cavity-to-mean concentration
places the cavity tuple inside the larger 2B S domain except on an
event of probability exp(CM)/n+Ce^{-cn}. The fixed operator cutoff is
included. Both events are cavity measurable and preserve independence
of the removed Gaussian row or column.

On the complement the proof replaces the auxiliary input before scalar
evaluation. It discards the actual tagged statistic using its strong
moment and Cauchy--Schwarz. This costs exp(CM)/sqrt(n), since finite
products and squares of exp(CM) remain of that form after changing C.
The safe scalar tuple has bounded corresponding moments. The proof
never evaluates a potentially unstable scalar equation at the bad
original input; doing so would restore the unwanted iterated exponential.

On the retained event, upper scalar reinsertion has a common small
homogeneous feedback factor, because the row mass is small and pure-z
upper derivatives have size O(S). Lower scalar reinsertion has an
ordinary differential equation with coefficient C(1+M+B), giving
exp(CM). The instantaneous upper atom is inside that lower ODE.

A qualification necessary for the tagged calculation is explicit in
the repaired Section 8: at a specified source u the upper regular
response contains Q_h(x,u)A(u). Row mass alone does not bound its target
supremum. The physical cavity density is bounded by exp(CM)|lambda(u)|,
which supplies this forcing with a linear exp(CM) cost; homogeneous
absorption still uses only row mass. This remains single exponential.
Alternatively its source integral is controlled directly by row mass.
No density-independent pointwise response estimate is asserted.

The directly computed tagged Taylor remainder, with a source atom and
its causal tail kept separate, consequently yields target-uniform
regular errors at each source with the factor |lambda(u)|. Integrating
that source proves consistency in the row norm. This verifies the
event-localized consistency hypothesis in M_ROW_DOMAIN_ROUTE.md,
including both regular responses and the separate atom. It is not
obtained by differentiating a state-error bound.

Uniform conditional law comparison then replaces retained random data
by the full deterministic mean. Including safe replacement gives a
complete mean-map defect at most exp(CM)/sqrt(n) while the mean remains
inside the provisional barrier.

## 5. First exit closes at an exponential width threshold

Choose B>4C_0 and then one activity bound S_0 small enough for 2B S_0<=1
and C_L C_U S_0<1/2, as well as the cap-independent fitting condition.
These choices do not involve M. Use a fixed absolute response barrier
B S_0, or the equivalent full-interval S normalization. The normalizing
activity and barrier do not shrink with the prefix endpoint.

The finite expected response rows are continuous in the target-time
L1 topology and the atom is continuous. The finite cap-dependent
regularity bounds and their Gaussian moments suffice for this assertion;
uniform regularity constants are not needed. The running norms start
at zero. If a first exit existed, the localized consistency proof
would apply on its closed prefix, including the alleged exit time.
The strict law output bound would then give

\[
B S_0\le C_0 S_0+C_Ye^{CM}/\sqrt n.
\]

After increasing the fixed constants, n>=Ce^{CM} makes the last error
smaller than (B-C_0)S_0, a contradiction. Constants may depend on the
fixed nonzero labels; no uniform claim as Y tends to zero is needed.
There is no division by a vanishing prefix length and no reduction
of the labels as M increases.

The full expected tuple thus lies in the common comparison domain.
The defect and the two uniform comparison inequalities above, applied
against the already constructed common-domain law fixed point, give
distance exp(CM)/sqrt(n) by substitution and absorption of the fixed
factor C_L C_U S_0. No large-domain Gronwall is used here. The
qualitative fixed-M finite-program/common-action limit identifies the
same observables with the own forced closure population, in the same
order as the supplied smooth argument. The finite-width means serve
only as prescribed histories, not as a definition of the population.

## 6. Passive sources, autonomous restoration, and schedules

The passive velocity argument is correctly restricted to a fixed target
time t, with constants uniform in t. Its additional covariance block
contains <h(u),q(t)> and <q(t),q(t)>. For the first quantity only u is
differentiated, producing <q(u),q(t)> with bounded coordinates and
controlled root Jacobians. One-variable integration therefore controls
the supremum over u. The second quantity is a fixed-target pairing.
The passive response uses a source-integrated trace at the fixed
target, with its current atom included. No derivative of q(t), no
two-time passive-velocity supremum, and no derivative of r/rho is used.

The added Gaussian coordinate is correlated with the upper history;
interpolation uses the full positive-semidefinite joint covariance.
Its conditional variance has a common bound on the retained operator
event by the normalized velocity estimate. Since the upper observable
is linear in that coordinate, the conditional Gaussian derivative
envelopes suffice. These calculations supply prediction and key-moment
velocity sources rho(t) exp(CM)/sqrt(n), rather than merely value errors.

The cap-independent fitting estimate, scalar freezing, and damped
state/residual comparison retain their previously derived
polynomial(M) exp(CM) constants. The residual-difference term in the
state comparison uses normalized signal size, while residual damping
absorbs coefficient values O(S_0^2), not their cap-dependent Lipschitz
constants. Integrating the velocity sources and restoring residual,
clock, and memory feedback therefore keeps a single exponential.
Adding the centered conditional all-time fluctuation estimate proves
the full mean-bias-inclusive claim. Bounded-query uniformity and
conditional Markov give the stated query-integrated and fixed-confidence
forms.

For M(n)=[log(e+n)]^alpha, 0<alpha<1, the logarithm of both the error
prefactor and width threshold is o(log n). Thus the width restriction
holds eventually and the rate is n^{-1/2+o(1)}. For
M(n)=max(1,a log n), a<1/(2C), the width condition also holds eventually
and the rate is O(n^{-1/2+Ca}). For the log-log schedule the prefactor
is a fixed power of log n. These deductions use the same enlarged C
that bounds the width threshold and error constant.

No remaining gap was found in this repaired stronger chain. The verdict
does not cover a cap-independent root-width constant, a simultaneous
supremum over M, the actual all-time second moment on exceptional
initializations, or identification of the moving target with an
unclipped population. Those remain separate stronger claims.

## Frozen inputs

| File | SHA-256 |
|---|---|
| M_LOG_SCALE_RESULT.md | e9196f77dbc0a3d212044f57d8db8d3683c11f2049cd00c1cfae6d752ae30db4 |
| M_ROW_CAVITY_ROUTE.md | 9d65b20419362d82cf46064e0fcdfed539e67dd37a474c4e233e8747d9f541f2 |
| M_ROW_DOMAIN_ROUTE.md | 5d7446287a0e801bfa381554e82c36f42b4f9c8af4df4a2ecef104e153167539 |
| M_UNIFORM_CAVITY_ROUTE.md | 674edcc8b8c19e107bb4d203d36d70681f82678db50592a4b822adab5e045f71 |
| M_UNIFORM_LAW_ROUTE.md | a140dbb446d502c704939c2799a1a297f55ca9260f931fbc0e347891398a5c0f |
| M_CAP_SCHEDULE_ROUTE.md | 88ecd7b169fa52f532e826b210369d7363f606b4b5a7225b043a46823a82c3dc |
| SMOOTH_SETUP.md | a9a2166984c946a5cceebd6f01c168b052e1b74da2b52a2df92c111aa830eee6 |
| SMOOTH_RESULT.md | 525ee04832a67240ef751c27ce054b545a4d9c6859a180a372e32abb78e6d110 |
| SMOOTH_CAVITY_ROUTE.md | 9e22c3f455a6c0447a654a9af6154c0a6c38247bacf2f5aaf40a408895982315 |
| SMOOTH_MEAN_MAP_ROUTE.md | 9ca3c42741683d9ba37c5dac9a2df6018e606326756b671b89023fbeaba3b95e |
| SMOOTH_FEEDBACK_COMPLETION.md | eb3454d7c13c94ce4a89da8491bca0ff65e207c4d4275a2122ae588cd381d7e2 |
| CLIPPED_POPULATION_ROUTE.md | 63bdd715efc7d05875acd4b591d8d2751f38a4f15246f78b7ebfab44c36b5082 |
| SMOOTH_ALLINIT_ROUTE.md | db8b43883fb81c4e1afc3cb9961620bfda5b5ed0933f55ec57e422085b16ee8a |

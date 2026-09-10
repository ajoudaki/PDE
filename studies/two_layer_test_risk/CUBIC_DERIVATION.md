# The moving-flow cubic coefficient, with both Gaussian responses

Author: `cubic_derivation`, 2026-09-10. This is study source, not established
material or a promotion review. This independent reconstruction uses analytic
approach A only. It derives the first *possible* matched-risk term. Its sign
and nonvanishing are not asserted here; numerical evaluation, if supplied
elsewhere, does not change that qualification without an integration bound.

## Contract and dependencies

The model is exactly the one in this study's README: two tanh hidden layers,
stored readout, no biases, first/connector/readout initialization variances
`1, 1/n, 1/n^2`, raw mobilities `(n,1,n)`, and mean square loss on the three
specified angles. Put `phi=tanh`, `p_a=y_a/3`, and let `mu` be normalized
Lebesgue angle measure on the whole circle. Lowercase `a,b` in sums index
training examples only. A subscript `x` may denote any passive circle input.

The proof uses the actual strong population flow supplied by
`docs/global_nonlinear.md`, C.1--C.2, on a sufficiently short positive
physical interval. Its initial connector and adjoint are denoted `W` and
`W*`; every expectation below pairs fields in the same neuron population.
The weighted correction following C.3 is essential: all initial forcing
labels in the C.3 onset calculation are `p`, not `y`. Finite moving jets in
`docs/gaussian_calculus.md` are an algebraic cross-check, not a reason to
interchange width limits and derivatives. All asymptotics below are obtained
from the population integral equations themselves.

For the present data, with `c=(1+sqrt(5))/4` and `q=(sqrt(5)-1)/4`,

\[
G=\begin{pmatrix}1&c&c\\c&1&q\\c&q&1\end{pmatrix},\qquad
y=(1,-q,-q)^\top,\qquad p=y/3.
\]

This is the original rank-two input Gram. It is never inverted or whitened.

## Initial fields and the hidden onset

Let `Z_x` be the first initialized preactivation and set

\[
h_x=\phi(Z_x),\quad Y_x=Wh_x,\quad H_x=\phi(Y_x),
\quad Q_{xb}=E_1[h_xh_b],\quad K_{xb}=E_2[H_xH_b].
\]

The lower vector `Z` is Gaussian with covariance `G`; conditional width
averaging makes `Y` a centered Gaussian vector with covariance `Q`.
Define the following fixed initialized fields:

\[
\begin{aligned}
S&=\sum_b p_bH_b,& U_x&=S\phi'(Y_x),\\
B_b&=\phi'(Z_b)W^*U_b,&
T_x&=\sum_bG_{xb}p_bB_b,\\
A_x&=\phi'(Z_x)T_x,&
M_x&=\sum_bp_bQ_{xb}U_b,\\
R_x^{\mathrm{hid}}&=M_x+WA_x,& E_x&=\phi'(Y_x)R_x^{\mathrm{hid}}.
\end{aligned}\tag{1}
\]

`R_x^{hid}` is a hidden acceleration field and is unrelated to the test
risk functional. Every field is in its indicated population's `L2`.
Indeed tanh and its derivative are bounded, `S,U` are bounded, and `W,W*`
are bounded `L2` actions; all remaining operations in (1) preserve `L2`.

Write the evolving readout as `v(t)`. The exact equations with this loss are

\[
\begin{aligned}
\dot Z_x^{(1)}&=-2\sum_bG_{xb}\frac{r_b(t)}3
 \phi'(Z_b^{(1)}(t))W(t)^*[v(t)\phi'(Z_b^{(2)}(t))],\\
\dot W(t)&=-2\sum_b\frac{r_b(t)}3
 [v(t)\phi'(Z_b^{(2)}(t))]\otimes H_b^{(1)}(t),\\
\dot v(t)&=-2\sum_b\frac{r_b(t)}3 H_b^{(2)}(t).
\end{aligned}\tag{2}
\]

Since `v(0)=0` and `r_b(0)=-y_b`, continuity, division by `t`, and
integration give, in `L2` for fields and operator norm for `W`,

\[
\begin{aligned}
v(t)&=2tS+o(t),\\
v(t)\phi'(Z_b^{(2)}(t))&=2tU_b+o(t),\\
Z_x^{(1)}(t)-Z_x&=2t^2T_x+o(t^2),\\
W(t)-W&=2t^2\sum_bp_bU_b\otimes h_b+o(t^2),\\
Z_x^{(2)}(t)-Y_x&=2t^2R_x^{\mathrm{hid}}+o(t^2),\\
H_x^{(2)}(t)-H_x&=2t^2E_x+o(t^2).
\end{aligned}\tag{3}
\]

For example the first equation gives `v/t -> 2S`; multiplying by the
bounded continuous upper derivative gives the next line. Applying the
actual adjoint and multiplying by the bounded lower derivative supplies
the coefficient `2B_b` in the lower backward field. The first two
integrals in (2) therefore give the third and fourth lines of (3). In the
upper preactivation, the trained-matrix term is `2t^2 M_x` and the moved
first activation term is `2t^2 WA_x`. Both terms are required.

Here is the `L2` activation difference-quotient justification, which avoids
an invalid Frechet-differentiability premise. If `e_t/t^2 -> A` in `L2`,

\[
\frac{\phi(z+e_t)-\phi(z)}{t^2}
=\left(\int_0^1\phi'(z+u e_t)\,du\right)\frac{e_t}{t^2}
\longrightarrow\phi'(z)A.
\]

First subtract `A` using the bounded derivative. For the remaining product,
truncate the fixed `A` at magnitude `M`; the bounded part converges by
`e_t -> 0` in probability, and the discarded `L2` tail tends to zero as
`M -> infinity`. This proves each activation line of (3).

These estimates are uniform over the circle on a common passive-input
realization. To check this specifically, the lower initial fields are
`Z_x=g^T x/sqrt(2)` with a common two-dimensional Gaussian root. The moving
lower fields and their leading increments are linear in `x`, with only
three training fields in their coefficients. The maps `x -> Z_x,h_x,A_x`
are `L2`-continuous. Boundedness of `W` gives the corresponding continuity
of `Y_x,R_x^{hid}`. Thus each limiting field family is a compact `L2`
family. Such a family has uniformly small squared tails: cover it by
finitely many `L2` balls and truncate their finitely many centers. The
preceding bounded-multiplier argument is then uniform in `x`. Repeating
the finite forward expansions proves the uniform form of (3).
The passive-input construction/capture itself is a supporting corollary
of the established flow, addressed by the coordinator; no new learning
theorem is inferred from that capture.

## Comparison with the frozen flow retains the moving residual

Let `w(t)` be the frozen-feature readout and `g_t(x)=E_2[w(t)H_x]`. It solves

\[
\dot w(t)=-2\sum_b\frac{g_t(x_b)-y_b}{3}H_b,\qquad w(0)=0.
\tag{4}
\]

This model has the full initial tangent kernel: the hidden kernel blocks
contain the zero readout at population initialization and vanish. It is
not a different initialization or a readout with an order-one initial law.

Set `e(t)=v(t)-w(t)` and `d_x(t)=H_x^{(2)}(t)-H_x`. Direct subtraction,
with neither residual frozen, gives

\[
\begin{aligned}
\dot e(t)&=-2\sum_b\frac{f_t(x_b)-g_t(x_b)}3H_b
 -2\sum_b\frac{f_t(x_b)-y_b}3d_b(t),\\
f_t(x)-g_t(x)&=E_2[e(t)H_x]+E_2[v(t)d_x(t)].
\end{aligned}\tag{5}
\]

From (3), uniformly in `x`, `||d_x(t)||_2=O(t^2)` and `||v(t)||_2=O(t)`.
The residuals are bounded on the fixed local interval. Equations (5) imply

\[
\|e(t)\|_2\le C\int_0^t\|e(s)\|_2\,ds+Ct^3,
\]

and iteration of this inequality gives `||e(t)||_2=O(t^3)`. Hence
`f_t-g_t=O(t^3)` uniformly over the circle. Divide the first equation
in (5) by `t^2`. Its first sum tends to zero, whereas its second sum
tends in `L2` to `4 sum_b p_b E_b`. Integrating gives

\[
e(t)=\frac43t^3\sum_bp_bE_b+o_{L^2}(t^3).
\]

Using `v(t)/t -> 2S` in the second equation in (5) yields the actual
population, moving-residual expansion

\[
f_t(x)-g_t(x)=t^3J_x+o(t^3),\qquad
J_x=4E_2[SE_x]+\frac43\sum_bp_bE_2[H_xE_b].
\tag{6}
\]

The remainder here is uniform in `x`. In particular there is no linear
or quadratic feature-learning advantage in the predictor comparison.
The common lower-order terms are those of the true frozen residual flow,
`g_t(X)=(I-exp(-2Kt/3))y` on training inputs. Replacing the residual by
its initial value would erase its nonzero quadratic term and would not
justify (5)--(6).

An independent algebraic check is the kernel expansion. With
`D_ab=E_1[B_aB_b]`, `V_ab=E_2[U_aU_b]`, its `t^2` coefficient is

\[
K^{[2]}_{ab}
=4G_{ab}D_{ab}+4Q_{ab}V_{ab}
 +2E_2[E_aH_b+H_aE_b].\tag{7}
\]

Adjunction gives

\[
E_2[SE_a]=\sum_bp_b(G_{ab}D_{ab}+Q_{ab}V_{ab}).\tag{8}
\]

Therefore `J=(2/3)K^[2] p` on training inputs, agreeing exactly with
integration of the output equation `f'=-2K(t)(f-y)/3`. Equation (7)
retains both hidden blocks and the changing readout block.

## Loss matching and the candidate risk sign

For this dataset the input directions are pairwise nonparallel. Bounded
ridge-function independence from C.3 makes `Q` positive definite, despite
singularity of `G`. The upper training Gaussian has full support. If
`sum_b c_b tanh(Y_b)=0` almost surely, continuity extends the identity
to every point in `R^3`; varying only coordinate `b` forces `c_b=0`.
Thus `K` is positive definite too. Set

\[
B_0=E_2[S^2]=p^\top Kp>0,\qquad
\mathcal A=p^\top(G\circ D+Q\circ V)p>0.
\tag{9}
\]

Strict positivity of `mathcal A` follows from C.3's full response proof:
`V` is positive definite, `Q_aa>0`, and so `Q circ V` is positive
definite; the other summand is positive semidefinite. This positive number
measures hidden learning in the training direction, not test improvement.
Equations (6) and (8) give the useful normalization certificate

\[
p^\top J=\frac{16}{3}\mathcal A.\tag{10}
\]

The frozen training residual is `-exp(-2Kt/3)y`. For every finite `t>=0`
it is nonzero, since the matrix exponential is invertible and `y!=0`.
Thus its loss derivative `-(4/9)r^T Kr` is strictly negative. Spectral
decomposition of positive-definite `K` also gives frozen loss tending to
zero as `t -> infinity`. Its loss therefore bijects `[0,infinity)` onto
`(0,L(0)]`. The actual loss has derivative `-4B_0<0` at zero and is
positive for a sufficiently short interval by continuity. Consequently
there is a unique `tau(t)>=0` satisfying the prescribed matching there,
with `tau(0)=0`. The inverse is continuously differentiable near zero
because the frozen loss derivative is nonzero.

Let `a_x=2E_2[SH_x]=g'_0(x)`. From (6),

\[
\mathcal L(f_t)-\mathcal L(g_t)
=-2p^\top J\,t^3+o(t^3).
\]

Apply the mean-value theorem to the frozen loss between `t` and `tau(t)`;
its slope tends to `-4B_0`. This first proves `tau(t)-t=O(t^3)` and then

\[
\tau(t)=t+ct^3+o(t^3),\qquad
c=\frac{p^\top J}{2B_0}
=\frac{8\mathcal A}{3B_0}>0.\tag{11}
\]

In particular the matching removes a *positive* training-speed advantage.
Uniform continuity of the frozen predictor derivative gives

\[
f_t(x)-g_{\tau(t)}(x)=t^3(J_x-ca_x)+o(t^3),\qquad
p^\top(J-ca)=0.\tag{12}
\]

The last identity is required by equal training loss at the leading order;
it is another direct check on all time/loss factors. Let
`Y_teacher(alpha)=cos(3 alpha)`. Expanding the difference of the two
squares and using (12) gives

\[
\Delta(t)=\chi t^3+o(t^3),\qquad
\chi=2\int Y_{\rm teacher}(x)(J_x-ca_x)\,d\mu(x).
\tag{13}
\]

The integral exchanges are justified by the uniform remainder and bounded
teacher on a probability space. Formula (13) is not a proved nonzero
contribution until `chi!=0` is established. If `chi=0`, this study has to
record that cubic cancellation and either derive the next term within its
bound or stop with that obligation. If a rigorous positive (negative)
lower (upper) bound for `chi` is obtained, the uniform little-o remainder
proves positive (negative) risk difference on some width-independent
interval. This file supplies no numerical radius or explicit modulus for
that remainder. A claim of a quantitatively specified risk bound requires
the separate remainder work.

## Fully explicit inverse-free Gaussian expectations

The actions in (1) can be eliminated from the scalar coefficient without
deleting either response. Fix one test angle and let `I={x,1,2,3}`;
temporarily regard these as four formal coordinate slots, even when their
joint Gaussian law is singular. Set `p_x=0`. Generate the lower tuple by
two independent standard Gaussian roots,

\[
Z_i=\xi_1\cos\alpha_i+\xi_2\sin\alpha_i,
\qquad (\xi_1,\xi_2)\sim N(0,I_2).
\]

Compute `Q_ij=E_1[phi(Z_i)phi(Z_j)]` from this actual rank-two law,
then take `Y~N(0,Q)` in at most four Gaussian dimensions. The following
bottom moments and upper moments completely specify the coefficient:

\[
L_{ab}=E_1[\phi'(Z_a)\phi'(Z_b)],\qquad
T_{abij}=E_1[\phi'(Z_a)\phi'(Z_b)\phi(Z_i)\phi(Z_j)].\tag{14}
\]

For bounded smooth upper functions `F,G` of the formal tuple `Y`, define

\[
\Lambda_{ab}(F,G)
=L_{ab}E_2[FG]
 +\sum_{i,j\in I}T_{abij}
       E_2[\partial_iF]E_2[\partial_jG].\tag{15}
\]

Then define, with the summation index `b` restricted to the three training
examples as everywhere else,

\[
\mathcal C_a(F)
=\sum_b p_b\{Q_{ab}E_2[FU_b]
                     +G_{ab}\Lambda_{ab}(F,U_b)\}.\tag{16}
\]

The complete formula for (6) is

\[
J_x=4\mathcal C_x(U_x)
 +\frac43\sum_ap_a\mathcal C_a(H_x\phi'(Y_a)).\tag{17}
\]

Every derivative appearing here is explicit. With `p_x=0`,

\[
\partial_iU_a
=p_i\phi'(Y_i)\phi'(Y_a)
 +\mathbf1_{i=a}S\phi''(Y_a),\tag{18}
\]
\[
\partial_i[H_x\phi'(Y_a)]
=\mathbf1_{i=x}\phi'(Y_x)\phi'(Y_a)
 +\mathbf1_{i=a}H_x\phi''(Y_a).\tag{19}
\]

When `x` is one of the training inputs, either identify the coincident
slots first or retain them as formally distinct slots in (18)--(19).
The source-response convention yields the same contraction because a
zero-variance Gaussian linear relation is also a zero `L2` relation among
its source input fields. No small Gram eigenvalue is divided by.

To prove (15)--(17), the simultaneous reused-transpose law is

\[
W^*F=\mu_F(Z)+\Gamma_F,\qquad
\mu_F(Z)=\sum_{i\in I}\phi(Z_i)E_2[\partial_i F],\qquad
E[\Gamma_F\Gamma_G]=E_2[FG],\tag{20}
\]

where the jointly Gaussian `Gamma` family is independent of the lower
roots. In particular its covariance is the **full** second moment, not a
second moment with the deterministic response subtracted. For nonsingular
`Q`, finite Gaussian conditioning gives response coefficients
`Q^{-1}E[YF]`; Gaussian integration by parts gives
`E[YF]=Q E[nabla F]`, which proves (20). The same identity for singular
covariance follows by representing `Y=A gamma` and performing scalar
Gaussian integration by parts in `gamma`; the finite regularization and
bounded-action approximation in global_nonlinear Section 3.4 verify that
it is the actual matrix law at coincident or antipodal test slots too.
All functions used in (18)--(19) and their derivatives are bounded, so
the conditional expectations and integration-by-parts boundary terms are
integrable with vanishing Gaussian tails.

Multiply the two equations (20), condition on the lower roots, and use
zero mean and the displayed covariance of `Gamma`. Multiplication by
`phi'(Z_a)phi'(Z_b)` and expectation gives exactly

\[
E_1[\phi'(Z_a)\phi'(Z_b)(W^*F)(W^*G)]
=\Lambda_{ab}(F,G).\tag{21}
\]

Finally adjunction and the definition of `A_a` give

\[
\begin{aligned}
E_2[F R_a^{\mathrm{hid}}]
&=\sum_bp_bQ_{ab}E_2[FU_b]+E_1[(W^*F)A_a]\\
&=\sum_bp_b\{Q_{ab}E_2[FU_b]
             +G_{ab}\Lambda_{ab}(F,U_b)\}
=\mathcal C_a(F).
\end{aligned}\tag{22}
\]

Taking `F=U_x` or `F=H_x phi'(Y_a)` proves (17). This adjunction step
accounts for the reused forward call `WA_a` without pretending it is a
fresh independent Gaussian. The mean-product term in (15) is generally
present and must be retained. Deleting it changes the scientific model.

## Status, attacks, and exact remaining obligation

The following checks were performed analytically in this reconstruction:

1. The raw factor `2/3` appears in both actual and frozen flows. Training
   labels in onset fields are `p=y/3`; (10) and (12) check this normalization.
2. The direct moving-readout subtraction (5) and the kernel integration
   (7)--(8) produce the same `J`; both account for moving residuals.
3. Lower and connector feature motion contribute separately through
   `G Lambda` and `Q E[FU]` in (16). The initial connector response
   mean remains in (15).
4. Singular original input geometry is retained through the two-root
   representation. Formal repeated passive slots require no inverse.
5. Strictly positive training contraction (10) and positive clock shift
   (11) do **not** determine (13): the teacher integral is a different
   linear functional, and subtracting `ca` removes the speed direction.

The unresolved scalar obligation is a rigorous sign/nonzero bound for
the explicit number `chi` in (13), with `J` specified by (14)--(19).
It is a finite Gaussian/angle integral, with no unknown learned trajectory
inside its integrand. A floating-point sign alone is insufficient. If the
sign is certified, a uniform controlled remainder giving a usable
width-independent `t0` must be supplied at the claimed level. Formula (3)
and the argument above provide a uniform little-o remainder, but not an
explicit computable modulus. This route has not established a positive
or negative finite-time test-risk theorem by itself.

No network training, parameter sweep, random sampling, or API execution
was performed by this author. No maintained source or Git index was
modified. The author only writes this assigned proof file.

## Read and provenance record

Read completely: root AGENTS and workflow Part 1 (Part 2 was also visible
but no promotion action was taken); this study README; docs README and
NOTATION; finite_dynamics Sections 1--4; global_nonlinear Sections 2--3,
Appendix A.1--A.4, C.1--C.3 including its weighted correction;
gaussian_calculus Sections 1--3, 7.1, and finite-depth jet Appendix E;
the complete current CONTINUATION_DISPOSITION. These are the operative
statement/proof/dependency scopes for the derivation. Unrelated activation,
global-continuation, polynomial high-order and historical campaign sections
were not used. No implementation API was used, so code README was not a
dependency of this independent analytic subtask.

Required skills read: `solve-math-rigorously/SKILL.md` and
`investigate-conjectures/SKILL.md`, with the latter's research-contract,
adversarial-audit, proof-search-orchestration, and evidence-ledger references.
This is an internal reconstruction, not an isolated promotion review.

Source hashes observed before writing:

| File | SHA-256 |
|---|---|
| AGENTS.md | `a5e5b3749d9e9ee088c659bc2cf4ddb2d88adf371d98bf34140ded532020a517` |
| RESEARCH_WORKFLOW.md | `4323e5ada1a4875af2c8121c742c50f07d8ff5b569c3aa71e11ef9a14605b442` |
| docs/README.md | `4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453` |
| docs/NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| docs/global_nonlinear.md | `8c575acb99ed713ef688cafb39fe9d8d8430e80815d2a69ac6686bac2cc19101` |
| docs/finite_dynamics.md | `a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a` |
| docs/gaussian_calculus.md | `d2f6a065432b5dadc7a1973f11b335cbd0f180caa29a81f863c58fff3ac5ef5e` |
| CONTINUATION_DISPOSITION.md | `0dfdfcca323de9f8147529cfd18fa15cc5ff2899143f0af728c625531dea4f48` |

Initial observed HEAD: `02af27154186dd3e45f83989a8ddf78e92ebceff`.
Initial status contained unrelated exporter/maintenance changes, preserved.

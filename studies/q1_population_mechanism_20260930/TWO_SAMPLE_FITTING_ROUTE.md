# Two-sample fitting route: exact channels and the remaining sign problem

Author: scoped subagent `pair_fitting_route`, 2026-09-30.

Status: frozen theoretical candidate; conditional identities with complete
arguments below, self-audited but not independently reviewed. No experiment,
finite-width replacement, dense surrogate, external scientific source, or
fresh-Gaussian substitution was used. This does **not** prove global fitting
of the canonical Gaussian population.

## Scope and contract

Scientific input was only the supervisor's self-contained assignment: the
two-sample canonical population equations, zero readout and second-layer
memory initialization, Gaussian initialization, signed-input reduction to
two labels equal to one, and swap-equivariant uniqueness. Required process
inputs read were `AGENTS.md`, Part 1 of `RESEARCH_WORKFLOW.md`, the
`solve-math-rigorously` and `investigate-conjectures` skills, and the latter's
research-contract and adversarial-audit references. No book, paper, study
README, other route, or study history was read. Git HEAD at the initial
metadata check was `7fce699a7decf2239dc3eb50486eca661783b535`.

The question is whether the exact two-input, nonlinear, population flow has
a cooperative channel structure strong enough to prove fitting, and what
it forces about the learned function. We analyze the supplied feature clock
on an interval where the common training prediction is below one. There is
no width, approximation parameter, experiment, or limit exchange in the
calculations. All equations below retain the same fixed forward operator
and its true adjoint.

Take unit signed inputs `u_1,u_2` with inner product `c` in `(-1,1)`.
Unit normalization is used only in the geometric coordinate equations;
the operator and dissipation identities do not need it. Write

\[
 q=2+s,\qquad X_\pm=(X_1\pm X_2)/2,
 \qquad \langle\cdot,\cdot\rangle_j=\mathbb E_{\Omega_j}[\cdot\,\cdot].
\]

Norms refer to the corresponding real population Hilbert spaces. For the
vector field `A`, the norm additionally uses the Euclidean input inner
product. We require that the stated flow and true adjoint exist, that all
displayed quantities are integrable, and that the displayed Hilbert-space
chain rules and differentiation under expectation are valid. These are
assumptions on a defined flow, not a proof that the Gaussian limit exists.

For the diagonal channel identities we use **joint swap invariance** of
the evolving populations. In particular, expectations of an even quantity
times an odd quantity vanish on each population. This follows from a full
swap-equivariant initialization and unique equivariant evolution; equality
of the two scalar outputs alone is insufficient. If the assignment's
swap-equivariance means only that scalar equality, the diagonal identities
below need this stronger joint-invariance hypothesis.

## 1. Exact hidden channel equations

Define the first-layer coordinates and gates by

\[
 p=A\cdot (u_1+u_2)/2,\qquad m=A\cdot (u_1-u_2)/2,
\]
\[
 H_+=\frac{\sinh(2p)}{\cosh(2p)+\cosh(2m)},\qquad
 H_-=\frac{\sinh(2m)}{\cosh(2p)+\cosh(2m)}.
 \tag{1}
\]

Indeed the two preactivations are `p+m,p-m`, and (1) follows by adding
and subtracting their hyperbolic tangents. In particular `H_+` has the sign
of `p`, and `H_-` has the sign of `m`.

Set

\[
 a_\pm=\|H_\pm\|_1^2,\qquad
 b_\pm=\langle K_\pm,H_\pm\rangle_1,\qquad
 d_\pm=\langle V_\pm,D_\pm\rangle_2.
 \tag{2}
\]

The name `b_\pm` avoids confusing these moving correlations with the fixed
input correlation `c`. Joint swap invariance gives

\[
 \langle K_+,H_-\rangle_1=\langle K_-,H_+\rangle_1=0,
 \qquad
 \langle V_+,D_-\rangle_2=\langle V_-,D_+\rangle_2=0.
 \tag{3}
\]

The exact effective middle operator is

\[
 B=V_+\otimes K_+ + V_-\otimes K_-,
 \qquad (v\otimes k)h=v\langle k,h\rangle_1.
\]

Thus, writing `J_a=(T+B)^*D_a`, equations (3) imply

\[
 Z_\pm=TH_\pm+b_\pm V_\pm,\qquad
 J_\pm=T^*D_\pm+d_\pm K_\pm.                 \tag{4}
\]

This diagonalization applies to memory contractions; it does not replace
the reused source `T` by an independent Gaussian at any later time.

Put `E_H=1-H_+^2-H_-^2` and `E_G=1-G_+^2-G_-^2`. These are the averages
of the two nonnegative tanh derivatives, hence are nonnegative. Addition
and subtraction of `D_a=W(1-G_a^2)` give

\[
 D_+=W E_G,\qquad D_-=-2W G_+G_- .             \tag{5}
\]

The same algebra in the first layer gives

\[
 L_+=E_HJ_+-2H_+H_-J_-,\qquad
 L_-=E_HJ_--2H_+H_-J_+ .                     \tag{6}
\]

Taking the inner products of the supplied equation for `A'` with the two
orthogonal input directions now yields

\[
 p'=\frac{1+c}{2}L_+,\qquad
 m'=\frac{1-c}{2}L_-,                        \tag{7}
\]
\[
 W'=G_+,\qquad V_\pm'=D_\pm,\qquad
 K_\pm'=\frac{H_\pm-K_\pm}{q}.              \tag{8}
\]

Equations (1)--(8), with `G_a=tanh Z_a`, are an exact population channel
representation. They remain equations for random fields and the fixed
operator, rather than a closure in the finitely many correlations (2).
They show why deleting the minus channel is invalid: both (5) and (6)
couple the channels even though the two output predictions agree.

## 2. A precise sample-interaction identity

Combining `W'=G_+` with (5) gives the pointwise identity

\[
 \boxed{\quad V_-'=-(W^2)'G_- .\quad}        \tag{9}
\]

Consequently, at every population point and time where `(W^2)'` is
nonnegative, the minus-memory velocity has the opposite sign to the
current output difference `G_-`. The plus-memory velocity `V_+'=W E_G`
has the sign of the readout. These statements are exact local
reinforcement and suppression relations.

They do not show that `V_-G_-` is nonpositive, that `Z_-` decreases, or
that `W^2` increases. For example, integrating (9), when the product rule
is valid and `W(0)=0`, gives

\[
 V_-(s)=-W(s)^2G_-(s)+\int_0^s W(r)^2G_-'(r)\,dr. \tag{10}
\]

The history term in (10) has no sign established by the assignment.
In addition, the current odd preactivation contains the moving source
`TH_-` and the moving multiplier `b_-` in (4). Thus an instantaneous
opposition in (9) is weaker than contraction of the odd hidden field.

## 3. Exact fitting derivative and the missing signs

Joint swap invariance gives `F=\langle W,G_+\rangle_2`. Along the supplied
feature flow,

\[
\begin{split}
 F'={}&\|G_+\|_2^2+\|A'\|_1^2\\
 &+\sum_{\epsilon\in\{+,-\}}
 \left[b_\epsilon\|D_\epsilon\|_2^2
       +\frac{d_\epsilon(a_\epsilon-b_\epsilon)}{q}\right].
                                                        \tag{11}
\end{split}
\]

Here is the chain rule in full. For fixed memories, the derivative of the
mean output with respect to `A` is

\[
 \nabla_A F=\frac{L_1u_1+L_2u_2}{2}=A',
\]

so its contribution is `\|A'\|_1^2`; the readout contribution is
`\|G_+\|_2^2`. For a variation `\delta V_\epsilon`, the variation of
each `Z_a` is `\delta V_\epsilon\langle K_\epsilon,H_a\rangle_1`.
Averaging `\langle D_a,\delta Z_a\rangle_2` over the samples and using
(3) gives `\nabla_{V_\epsilon}F=b_\epsilon D_\epsilon`. Contracting
with `V_\epsilon'=D_\epsilon` gives the first summand in brackets.
For a variation `\delta K_\epsilon`, the same computation gives
`\nabla_{K_\epsilon}F=d_\epsilon H_\epsilon`; contracting with (8)
gives the second summand. All parameter blocks have therefore been
included exactly once.

The histories entering the two potentially indefinite terms are explicit:

\[
 K_\epsilon(s)
 =\frac{2H_\epsilon(0)+\int_0^s H_\epsilon(r)\,dr}{q},                 \tag{12}
\]
\[
 b_\epsilon(s)
 =\frac{2\langle H_\epsilon(0),H_\epsilon(s)\rangle_1
       +\int_0^s\langle H_\epsilon(r),H_\epsilon(s)\rangle_1\,dr}{q},\tag{13}
\]
\[
 d_\epsilon=\tfrac12(\|V_\epsilon\|_2^2)'.                         \tag{14}
\]

Equation (12) follows by differentiating `qK_\epsilon`, using `q'=1`,
and applying the specified initialization. Equation (13) is its inner
product with the current hidden field, and (14) uses `V_\epsilon'=D_\epsilon`.
In particular, these are genuine current-past overlaps, not the
nonnegative current norms `a_\epsilon`. Setting `b_\epsilon=a_\epsilon`
would silently remove the memory law.

For comparison only, nonnegative current-past overlaps, nondecreasing
hidden norms, and nondecreasing `\|V_\epsilon\|_2` would imply
`0\le b_\epsilon\le a_\epsilon` and `d_\epsilon\ge0`, making all the
brackets in (11) nonnegative. The bound `b_\epsilon\le a_\epsilon`
would follow from Cauchy--Schwarz applied to every past overlap in (13).
None of those three trajectory properties is proved here. Treating them
as established would assume the missing mechanism.

There is one unconditional readout balance:

\[
 \frac12(\|W(s)\|_2^2)'=F(s),\qquad
 \int_0^s F(r)\,dr=\tfrac12\|W(s)\|_2^2\ge0.                       \tag{15}
\]

It proves nonnegativity of the integrated prediction, not pointwise
prediction monotonicity or fitting.

## 4. Why the missing derivative estimate would suffice

The following comparison is a conditional consequence, not a fitting
theorem for the canonical flow.

Suppose a twice differentiable feature flow exists up to its first
crossing of `F=1`, with `W(0)=0`,

\[
 \kappa=\|G_+(0)\|_2^2>0,\qquad F'\ge\|G_+\|_2^2.                 \tag{16}
\]

Then throughout that interval

\[
 F'(s)\ge\kappa,\qquad F(s)\ge\kappa s.                           \tag{17}
\]

To prove this, let `n(s)=\|W(s)\|_2`. Wherever `n>0`, equations (15),
(16), and `W'=G_+` give

\[
 n''=\frac{F'}{n}-\frac{F^2}{n^3}
 \ge\frac{\|W'\|_2^2}{n}-\frac{\langle W,W'\rangle_2^2}{n^3}
 \ge0.
\]

The last inequality is Cauchy--Schwarz. Since
`W(s)=sG_+(0)+o(s)`, the right derivative `n'(0+)=\sqrt\kappa`.
Thus `n'\ge\sqrt\kappa` and `n\ge\sqrt\kappa s` wherever the argument
applies; this also precludes a later zero of `n`. Finally
`F'=n'^2+nn''\ge\kappa`, proving (17).

If the feature flow remains regular through `s=1/\kappa` unless it
crosses earlier, continuity yields a first crossing
`s_*\le1/\kappa`. In physical time, `s'=2(1-F)` and the common
residual `e=1-F` satisfies

\[
 \dot e=-2F'(s(t))e\le-2\kappa e,\qquad
 0<e(t)\le e^{-2\kappa t}.                                        \tag{18}
\]

This is valid while the physical flow is defined below the crossing;
regularity of the feature curve through `s_*` gives the usual global
physical reparametrization approaching that root. Thus a lower bound on
the readout feature norm at later times is not an additional necessary
lemma: the derivative estimate in (16) propagates its own initial lower
bound by the convexity of `\|W\|`.

At initialization, `A'=D_\pm=0`, so (11) yields
`F'(0)=\kappa`. Under continuity and `\kappa>0`, fitting starts in the
correct direction for a nonzero feature-time interval. If the canonical
initial forward law gives a nondegenerate centered Gaussian pair
`(Z_1(0),Z_2(0))`, then `\kappa>0`: its positive density assigns positive
mass to an open region where both preactivations are positive, on which
`G_+>0`. Deriving that initial Gaussian law from a particular definition
of `T` lies outside the supplied prompt.

## 5. Intrinsic geometry of the learned function

For a test input `x`, the exact population prediction is

\[
 f_s(x)=\left\langle W,
 \tanh\!\left(T\tanh(A\cdot x)
 +V_+\langle K_+,\tanh(A\cdot x)\rangle_1
 +V_-\langle K_-,\tanh(A\cdot x)\rangle_1\right)
 \right\rangle_2.                                                 \tag{19}
\]

This identity is not advertised as a solved representation of the
trajectory. Two exact restrictions give it intrinsic geometric content.
First,

\[
 A(s)-A(0)\in\operatorname{span}\{u_1,u_2\}
 \quad\text{pointwise on }\Omega_1,                               \tag{20}
\]

because the velocity `A'` always lies in this span. Orthogonal first-layer
coordinates therefore retain their initial values, although the readout
and fixed-source correlations can still make the full output depend on
test-input transverse norm.

Second, suppose the full initialization is isotropic in input space and
the deterministic population flow is uniquely equivariant under input
orthogonal transformations preserving the labeled sample set. Put

\[
 e_+=\frac{u_1+u_2}{\sqrt{2(1+c)}},\qquad
 e_-=\frac{u_1-u_2}{\sqrt{2(1-c)}},\qquad
 x=\alpha e_++\beta e_-+x_\perp.
\]

Then there is a deterministic function `\Phi_s` such that

\[
 f_s(x)=\Phi_s(\alpha,\beta,\|x_\perp\|),\qquad
 \Phi_s(\alpha,-\beta,r)=\Phi_s(\alpha,\beta,r),\qquad
 \Phi_s(-\alpha,\beta,r)=-\Phi_s(\alpha,\beta,r).                   \tag{21}
\]

The radial assertion is understood only for transverse norms that occur
in the input dimension. To prove it, orthogonal transformations acting
only on the transverse subspace fix each training input, hence preserve
the learned population function by the stated equivariance. The
reflection of `e_-` exchanges the equally labeled samples and gives the
evenness in `\beta`. Finally the bias-free architecture in (19) is odd
under `x\mapsto-x` at every fixed state. Combining this oddness with the
evenness in `\beta` and invariance under transverse negation yields
the last identity of (21).

In particular,

\[
 f_s(x)=0\qquad\text{whenever }x\cdot(u_1+u_2)=0.                 \tag{22}
\]

This is an exact, all-defined-times decision-boundary restriction.
It proves neither the sign of `f_s` on the two open half-spaces nor
that this hyperplane is its only zero set. A fitted training value, if
obtained, would therefore not by itself determine the full function.

## 6. Cooperative-cone audit and frozen outcome

The tempting local cone argument has two distinct problems. First, the
channel Jacobian of the tanh map in (1) is

\[
 \begin{pmatrix}E_H&-2H_+H_-\\-2H_+H_-&E_H\end{pmatrix};
\]

its off-diagonal sign changes with the hidden coordinates. More
fundamentally, the source terms in (4) are a Gaussian forward map and
its true adjoint, with no positivity-preserving assumption. Gaussian
forward fields already have both signs at initialization.

For precision, in any realization of the canonical source where two
source-independent nonnegative nonproportional test functions produce
a nondegenerate centered Gaussian pair, the source is not positive on
that pointwise cone. Nor can one output sign gauge make both images
nonnegative: their product is negative on an event of positive
probability, and a common sign gauge leaves their product unchanged.
The Gaussian pair has positive density in either opposite-sign quadrant,
which proves the assertion without a finite-width example. This argument
is conditional on the stated initial source law and only concerns that
natural pointwise cone. An adaptive cone adapted to the actually
reachable trajectory remains possible and unproved.

The exact derivative (11) is the sharper obstruction to the present
proof route. Symmetry eliminates cross-channel expectations but does
not imply positivity of current-past overlaps in (13), monotonicity of
the memory norms in (14), or a compensating inequality involving
`\|A'\|^2`. Neither failure of a generic order argument nor the existence
of indefinite terms in an identity disproves fitting of the actual
Gaussian trajectory.

The strongest frozen results are (4)--(9), (11)--(15), and the geometric
restrictions (20)--(22), under their displayed defined-flow and symmetry
assumptions. The conditional comparison (16)--(18) identifies a useful
target: prove that the last line of (11), together with `\|A'\|^2`, is
nonnegative along the canonical reachable flow. Requiring each bracket
separately to be nonnegative may be unnecessarily strong.

Missing inputs for stronger claims are a precise construction/domain of
the fixed Gaussian operator and adjoint, verified differentiability and
integrability of the population curve, the exact full equivariance law,
and a global continuation theorem. Even if those inputs are supplied,
the sign/compensation estimate in (11) remains a substantive open proof
obligation. No claim here identifies a finite-width limit, establishes
all-time Gaussian-population existence, or proves eventual fitting.

Self-checks performed: the middle operator was recomputed directly from
the two sample sum; every parameter-block contribution to (11) was
derived before imposing parity; (9) was checked against both original
sample derivatives; the memory solution was differentiated back into
the ODE; the comparison included the zero-readout endpoint and its
nonvanishing argument; the function symmetries were separated from any
unproved sign classification. There were no executed scientific tests.

## Addendum: the odd-channel memory sign fails locally

Scope update, 2026-09-30: after the original note was frozen, the supervisor
authorized this bounded follow-up and supplied the initial second-layer
channel derivatives. This addendum therefore uses that post-freeze
cross-pollination as well as the original prompt and this note; it is not
an independent attempt. No other scientific input or experiment was used.

The stronger proposed condition

\[
 d_-(s)\bigl(a_-(s)-b_-(s)\bigr)\ge0                              \tag{23}
\]

does **not** bootstrap from Gaussian initialization. Under the initial
Gaussian covariance property stated precisely below, it is strictly
negative for all sufficiently small positive feature times. This is a
local property of the Gaussian-initialized defined flow, not an arbitrary
source-operator or arbitrary-state counterexample. It does not rule out
positivity of the *total* derivative in (11).

### A. Precise initial Gaussian input needed

Let `\mathcal H_0` denote the source-independent first-layer functions
of `A(0)`. The property used here is: for every finite list in
`\mathcal H_0`, their initial forward images are centered jointly
Gaussian under the second-layer population expectation, with

\[
 \langle Th,Tk\rangle_2=\sigma_T^2\langle h,k\rangle_1,
 \qquad h,k\in\mathcal H_0,\quad \sigma_T>0.                       \tag{24}
\]

We need (24) only for the finitely many initial functions explicitly
appearing below. It is the usual initial forward covariance rule for an
independent Gaussian source. We do **not** extend it to adaptive fields
at positive time, assert that `T^*T` is scalar on the full evolving
space, or replace a reused source by a fresh one. As throughout the
note, the true-adjoint pairing and the indicated population derivatives
are assumed to exist. If the intended canonical source does not satisfy
(24) even on these initial functions, this result is conditional on a
missing scientific input, rather than a statement about that source.

All unlabelled variables in subsections B--C are evaluated at `s=0`.
Gaussian isotropic `A(0)` makes `p,m` independent centered Gaussian
variables with strictly positive variances because `-1<c<1`. Hence
`H_+` is odd in `p` and even in `m`, while `H_-` is even in `p` and odd
in `m`. Both `a_+,a_-` are strictly positive and
`\langle H_+,H_-\rangle_1=0`. Equation (24) consequently makes
`Z_+=TH_+` and `Z_-=TH_-` independent nondegenerate centered Gaussians.

Put

\[
 E=1-H_+^2-H_-^2,\quad C=-2H_+H_-,\quad
 P=1-G_+^2-G_-^2,\quad R=-2G_+G_-,\quad
 \lambda_\pm=(1\pm c)/2,
\]
\[
 f_+=PG_+,\qquad f_-=RG_+=-2G_+^2G_- .                           \tag{25}
\]

Both `E` and `P` are strictly positive at finite Gaussian
preactivations. Define the two scalar coefficients

\[
 \eta_+=\frac{\langle Z_+,f_+\rangle_2}{a_+}>0,\qquad
 \eta_-=\frac{\langle Z_-,f_-\rangle_2}{a_-}<0.                    \tag{26}
\]

Their signs are pointwise: `G_+` has the sign of `Z_+`, and `G_-` the
sign of `Z_-`; thus `Z_+PG_+>0` and
`-2Z_-G_-G_+^2<0` almost surely outside null sets.

For any initial test function `h\in\mathcal H_0`, joint Gaussian
regression gives

\[
 \langle h,T^*f_+\rangle_1=\eta_+\langle h,H_+\rangle_1,
 \qquad
 \langle h,T^*f_-\rangle_1=\eta_-\langle h,H_-\rangle_1.             \tag{27}
\]

For completeness, subtract
`\langle h,H_+\rangle_1 Z_+/a_+ +
 \langle h,H_-\rangle_1 Z_-/a_-` from `Th`. By (24) this centered
Gaussian remainder has zero covariance with both `Z_+,Z_-`, so is
independent of the pair. Its inner product with any integrable function
of that pair is therefore zero. The remaining cross terms vanish:
`f_+` is odd in `Z_+` and even in `Z_-`, and `f_-` is even in `Z_+`
and odd in `Z_-`. Applying the true-adjoint identity proves (27).
This is a weak identity against initial source-independent test
functions; it is not a claimed pointwise formula for the full adjoint.

### B. The first-layer difference energy initially decreases

At initialization, `A'=H_\pm'=K_\pm'=0` and

\[
 D_\pm'=f_\pm,\qquad J_\pm'=T^*f_\pm.                            \tag{28}
\]

The memory part of `J_\pm` has zero derivative there, since `V=D=0`.
Differentiating (6)--(8) once, then applying the Jacobian of (1), gives

\[
 \begin{split}
 H_+''&=(\lambda_+E^2+\lambda_-C^2)T^*f_+ + EC\,T^*f_-,\\
 H_-''&=EC\,T^*f_+ +(\lambda_+C^2+\lambda_-E^2)T^*f_- .
 \end{split}                                                     \tag{29}
\]

There are no second-derivative-of-tanh terms in (29), because both first
coordinate velocities vanish at zero. Pair the second equation with
`H_-`. All test functions thereby multiplying `T^*f_\pm` depend only on
`A(0)`, so (27) applies. Define

\[
 J=\mathbb E_1[H_+^2H_-^2E]>0,\qquad
 Q_-=\mathbb E_1[H_-^2(\lambda_+C^2+\lambda_-E^2)]>0.
\]

Using `C=-2H_+H_-`, we obtain

\[
 \chi_-:=\langle H_-,H_-''\rangle_1
       =-2\eta_+J+\eta_-Q_-<0.                                  \tag{30}
\]

Strict positivity of `J,Q_-` follows from the nondegenerate Gaussian
`p,m`, strict positivity of `E`, and `\lambda_\pm>0`. The corresponding
plus calculation gives

\[
 \begin{split}
 Q_+&=\mathbb E_1[H_+^2(\lambda_+E^2+\lambda_-C^2)]>0,\\
 \chi_+&:=\langle H_+,H_+''\rangle_1
         =\eta_+Q_+-2\eta_-J>0.                                \tag{31}
 \end{split}
\]

Thus `a_-''(0)=2\chi_-<0`, while `a_+''(0)=2\chi_+>0`. The exact
initial first-layer learning reinforces the common component and
suppresses the difference in population squared norm. This verifies the
same direction of interaction as the supervisor's supplied initial
second-layer calculation without making it a global invariant.

### C. Consequence for the proposed memory sign

Because `K_\pm(0)=H_\pm(0)` and `H_\pm'(0)=K_\pm'(0)=0`, the
memory equation implies `K_\pm''(0)=0`. Differentiating the quantities
in (2) twice therefore gives

\[
 (a_\pm-b_\pm)''(0)=\chi_\pm,\qquad
 a_\pm(s)-b_\pm(s)=\tfrac12\chi_\pm s^2+o(s^2).                  \tag{32}
\]

Also, (28) and zero memory initialization give

\[
 V_\pm(s)=\tfrac12s^2f_\pm+o(s^2),\quad
 D_\pm(s)=sf_\pm+o(s),\quad
 d_\pm(s)=\tfrac12s^3\|f_\pm\|_2^2+o(s^3).                       \tag{33}
\]

These expansions hold in the Hilbert norms needed for the indicated
inner products. The nondegenerate Gaussian pair makes
`\|f_-\|_2^2>0`. Equations (30), (32), and (33) yield the strict local
failure

\[
 d_-(s)(a_-(s)-b_-(s))
   =\tfrac14\chi_-\|f_-\|_2^2s^5+o(s^5)<0.                      \tag{34}
\]

The odd lag contribution to (11) and its time integral satisfy

\[
 \frac{d_-(a_--b_-)}{2+s}
   =\tfrac18\chi_-\|f_-\|_2^2s^5+o(s^5),\qquad
 \int_0^s\frac{d_-(a_--b_-)}{2+r}\,dr
   =\tfrac1{48}\chi_-\|f_-\|_2^2s^6+o(s^6)<0.                   \tag{35}
\]

Thus replacing the pointwise sign of this particular lag term by
nonnegativity of its cumulative integral does not repair the argument.
The initial shared-channel lag term instead has positive sign by (31).

This does **not** say that the full odd-memory contribution is negative.
Indeed its other summand in (11) satisfies

\[
 b_-(s)\|D_-(s)\|_2^2=a_-(0)\|f_-\|_2^2s^2+o(s^2)>0,            \tag{36}
\]

which dominates the order-five loss in (35) near zero. The original
local fitting conclusion is preserved, and `b_-(s)>0` still holds for
small times by continuity. No conclusion about later positivity of
`b_-`, or about the all-time balance between (35) and (36), is implied.

### D. Frozen outcome and remaining obligation

The termwise sign route is disproved locally under (24): contrast
suppression necessarily makes its historical first-layer memory lag
behind the shrinking present contrast. That lag contributes negatively
to the instantaneous output derivative. Both its pointwise and cumulative
nonnegativity are unavailable as proof lemmas.

A global proof must allow this negative term and show compensation by
the positive memory response and/or first-layer gradient norm in (11),
or identify a different Lyapunov functional. The supplied local
reinforcement/suppression derivatives do not supply that estimate.
Proving it along the canonical reachable Gaussian flow remains a
theorem-strength obligation; this bounded follow-up stops here.

The derivation was checked by recomputing the first-layer Jacobian,
its two input-metric factors, the Gaussian regression coefficients,
and the orders `s^2,s^3,s^5,s^6` separately. The strict signs use only
initial nondegeneracy and no later Gaussianity. There was no numerical
experiment, arbitrary-operator replacement, or assertion that global
fitting is false. The source-law and defined-flow assumptions remain
explicit pending the supervisor's check against the actual canonical
construction.

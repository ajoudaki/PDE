# Trained data response at a nonlinear fitted reference

Author/assembler: `/root`, with component authors named in their proofs.
Status: candidate theorem under author reconstruction; not independently
accepted or promoted. The conclusions below require the complete component
proofs, not their summaries.

## 1. Model and meaning of the response

Let `Y≥1`, `u=x/sqrt(2)∈S¹`, and use two tanh hidden layers of equal width n,
no biases, and

\[
 z^1=W^1u,\quad h^1=\tanh z^1,\quad z^2=W^2h^1,\quad
 h^2=\tanh z^2,\quad f_n=(W^3)^Th^2/n.
\]

All initialized entries and blocks are independent centered Gaussians, with
stored variances `(1,1/n,1/n²)`. The mobilities are `(n,1,n)` and the loss
is the unhalved mean square. Time t is physical GF time. For a nonatomic
training law the finite loss is integrated exactly against that law.

Fix `nu*=½delta_(sqrt(2)e1,+1)+½delta_(sqrt(2)e2,-1)` and any deterministic
Borel probability law nu on `Z=sqrt(2)S¹×[-Y,Y]`. Set
`mu_epsilon=(1-epsilon)nu*+epsilon nu`, `sigma=nu-nu*`. Use the same three
initialized arrays for every epsilon, retaining the actual finite Gaussian
readout. The observable is the right derivative

\[
 D_\sigma f_n(t,x)=\left.\frac{d}{d\epsilon^+}
                  f_{n,\mu_\epsilon}(t,x)\right|_{\epsilon=0}.
 \tag{1}
\]

This derivative is taken at each finite n before n tends to infinity.
It is not defined by differentiating a nonlinear population law-to-flow
map. No such perturbed population map through an arbitrary T is assumed.

## 2. State, exact equation and observations

Use the established canonical reference action spaces
`H_i=L²(Omega_i)` and the actual reference `(w(t),A(t),c(t))`, including its
full first row and both orientations of `A=A0+K`. The initialized action
A0 is bounded and its reverse is its actual Hilbert adjoint; only K is
Hilbert–Schmidt. The fitted endpoint is the established first b=1 state
of the autonomous reference feature equation, at feature time at most ten.

Put `phi=tanh`, `F(z)=z/2+sinh(2z)/4`, and
`X_a=F(w_a)-F(g_a)`. The tangent Hilbert space and finite same-width norm are

\[
 \mathcal V=L^2(\Omega_1;\mathbb R^2)\oplus
             \mathcal S_2(H_1,H_2)\oplus H_2,\qquad
 \|V\|_{\mathcal V}^2=\|\xi\|_2^2+\|B\|_{HS}^2+\|d\|_2^2,
 \tag{2}
\]
\[
 \|V_n\|^2=\|\xi_n\|_F^2/n+\|B_n\|_F^2+\|d_n\|_2^2/n.
 \tag{3}
\]

Here `V=(xi,B,d)` and the raw variation is
`((phi'(w_a)xi_a)_a,B,d)`. Thus its raw norm is at most `||V||_V`.
The inverse conversion need not be bounded. The population norm (2) and
finite norm (3) are never subtracted across different carriers.

At every passive direction u define

\[
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad
 H^2(u)=\phi(Z^2(u)),\quad \delta(u)=c\phi'(Z^2(u)),\quad
 Q(u)=A^*\delta(u),\quad r(u,y)=\langle c,H^2(u)\rangle-y.
 \tag{4}
\]

The forcing, linear in the signed measure sigma, is

\[
 b_\sigma(t)=-2\int_Z r(t,u,y)
 \left(
  \left(u_a\frac{\phi'(w(t)\cdot u)}{\phi'(w_a(t))}Q(t,u)\right)_{a=1,2},
  \delta(t,u)\otimes H^1(t,u),\ H^2(t,u)
 \right)\,d\sigma(u,y).
 \tag{5}
\]

The rank-one action is `(q tensor h)v=q E_1[hv]`; its finite representative
is `q h^T/n`. Formula (5) includes the loss factor two and the signed
reference subtraction. It also retains the forward and adjoint uses of
the same initialized Gaussian action.

With the exact synthesis, evaluation and residual-curvature operators
defined in PROPAGATOR.md (8)–(11), the forced evolution is

\[
 \dot V_\sigma(t)=\mathcal L(t)V_\sigma(t)+b_\sigma(t),\qquad
 \mathcal L(t)=-2S(t)E(t)+\mathcal C(t),\qquad V_\sigma(0)=0.
 \tag{6}
\]

All coefficients are computed from the autonomous reference state.
Their source is not a future-trajectory oracle. They define bounded
strongly continuous operators on (2); no ambient Fréchet differentiability
of an L²-valued nonlinear vector field is asserted.

The prediction derivative produced by (6) is

\[
 \mathscr D_\sigma f(t,\sqrt2u)=\ell(t,u)V_\sigma(t),
 \quad \ell(t,u)V=\langle d,H^2(u)\rangle+
 \langle\delta(u),BH^1(u)+A[\phi'(w\cdot u)
                   \sum_a u_a\phi'(w_a)\xi_a]\rangle.
 \tag{7}
\]

The lower hidden response has norm at most `||V||_V`; both the upper
preactivation and activation responses have norm at most `(3+sqrt(10))||V||_V`.
Uniformly in all physical times and circle inputs,
`||ell(t,u)||≤L0<17`, with L0 defined in PROPAGATOR.md (12).

## 3. Candidate conclusions and constants

The complete proofs are PROPAGATOR.md, WEIGHTED_SOURCE.md, and
FINITE_CAPTURE.md. Together they establish the following proposed claims.

**Admissible forcing and well-posed evolution.** Let `M_0(Z)` be the real
Banach space of finite signed Borel measures of mass zero, with total
variation *mass* `||sigma||TV=|sigma|(Z)` (no factor one-half).
The integrand in (5) is a continuous V-valued function and the integral is
a Bochner integral. Its bounded linear extension to `M_0(Z)` is justified
by (5), rather than by a two-sided probability neighborhood. Equation (6)
has a unique strong solution for every such sigma and every finite horizon.

The weighted-source proof establishes finiteness of the reference quantity

\[
 M_w=\sup_{t\ge0,\,u\in S^1,\,a=1,2}
          \|\cosh^2(w_a(t))Q(t,u)\|_2<\infty.
 \tag{8}
\]

In particular, putting

\[
 C_{b,Y}=2(\sqrt{10}+Y)\sqrt{M_w^2+11},
 \qquad \sup_{t\ge0}\|b_\sigma(t)\|_{\mathcal V}
                       \le C_{b,Y}\|\sigma\|_{TV},
 \tag{9}
\]

is valid: the row norm uses `sum_a u_a²=1`, the middle rank has norm
at most `sqrt(10)`, and the readout factor has norm at most one.
The exact envelope `cosh² w_a≤cosh² g_a+2|X_a|` and actual finite cavity
moments supply the weighted integrability in (8). RMS value convergence
alone is not the proof of that step.

**Actual finite-GF capture.** For every fixed nu as above and every fixed
`T<infinity`, including `T=40`,

\[
 \sup_{0\le t\le T,\,x\in\sqrt2S^1}
       |D_\sigma f_n(t,x)-\mathscr D_\sigma f(t,x)|
          \longrightarrow0\quad\hbox{in probability}.
 \tag{10}
\]

The probability is over the initialized arrays. The state is identified
by same-width finite-program approximations in the uniform-in-time norm
(3), whose canonical counterparts converge in (2). Their finite rank
expansions identify middle Hilbert–Schmidt inner products and both action
directions. Joint named same-layer fields converge with their second moments
at every finite list of times and passive inputs. FINITE_CAPTURE.md specifies
this topology and proves the stronger comparison needed to justify (10).
It does not assert operator-norm convergence of finite matrices to operators
on another carrier, or hidden tangent path laws beyond the stated topology.

Every deterministic estimate is independent of the support size, smallest
atom weight and Gram rank of nu. Convergence is for each fixed nu; a failure
probability uniform over all laws is not part of (10). No rate is asserted.

**Uniform population propagation.** Let U(t,s) be the homogeneous evolution
of (6). PROPAGATOR.md proves

\[
 \sup_{0\le s\le t<\infty}\|U(t,s)\|\le C_U<\infty,
 \qquad V_\sigma(t)=\int_0^tU(t,s)b_\sigma(s)\,ds,
 \tag{11}
\]
\[
 \sup_{t\le T}\|V_\sigma(t)\|_{\mathcal V}
       \le C_U C_{b,Y}T\|\sigma\|_{TV},\qquad
 \sup_{t\le T,x}|\mathscr D_\sigma f(t,x)|
       \le L_0 C_U C_{b,Y}T\|\sigma\|_{TV}.
 \tag{12}
\]

The admissible general forcing norm is `L¹([0,T];V)`; (11) bounds response
by C_U times that norm. In (12), contamination directions obey `||sigma||TV≤2`.

For conditioning, `K_infty=E_infty S_infty=S_infty*D_infty S_infty`,
where `D_infty` multiplies the row blocks by `phi'(w_a,infty)²` and is
identity on the other blocks. This operator is injective, although not
uniformly coercive. Hence `ker K_infty=ker S_infty=ker E_infty*`.
The reference Gram may be singular. Its finite-dimensional pseudoinverse
is well defined and the explicit bound is

\[
 B_\infty=1+\|S_\infty\|\|K_\infty^+\|\|E_\infty\|,
 \qquad C_U=B_\infty\exp(B_\infty J_0),
 \tag{13}
\]

with the completely specified finite J0 in PROPAGATOR.md (22). The proofs
give finiteness through reference quantities, not an evaluated numerical
certificate for endpoint conditioning or a useful numerical response constant.
They assume no spectral gap or full-rank endpoint Gram. Uniform population
propagation is separate from fixed-horizon finite-width convergence (10).

## 4. Interpretation and what the next milestone receives

At the fitted endpoint,
`P_infty=I-S_infty K_infty+ E_infty` projects onto `ker E_infty`.
Under the raw conversion it is the canonical raw-metric orthogonal
projection off the span of the weighted training gradients. These directions
preserve both fitted predictions to first order; their unseen evaluations
are `ell(infty,u)P_infty V` and need not be determined by training outputs.
This is an exact decomposition of the actual endpoint tangent operator.
It asserts neither a nonzero unseen change for every direction nor a sign
or risk benefit. A changed scalar clock alone does not describe the response.

The next nonlinear-continuation milestone receives an actual trained
propagator, an admissible full-row clock/HS/readout state, a total-variation
data-to-forcing map, and controlled passive observations. It still must
control nonlinear products away from the reference, including changes of
off-support inverse-gate factors times reverse queries, products of readout
and hidden increments, and the quadratic remainder of hidden activation
changes. These are not bounded bilinear maps on arbitrary L² directions
merely because the present linear equation is bounded.

No nonlinear perturbed population flow, finite-contamination remainder,
large path of laws, sampling CLT, expected-risk expansion, endpoint
continuity, transport forcing modulus, or raw-GD derivative theorem is
included. Empirical laws of nonatomic distributions do not approach them
in total variation. Nothing here is a convergence claim for a training-time
Taylor series or evidence of superiority of one learning mechanism.

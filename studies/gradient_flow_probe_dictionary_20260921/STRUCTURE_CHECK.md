# Independent structure check: gradient-flow probe dictionary

## Assignment, sources, and isolation

This is a prompt-only independent mathematical check of a proposed finite-probe dictionary for a two-hidden-layer tanh network. Its scientific inputs were exclusively the supervisor's initial assignment and the supervisor's explicit initialization/source-response rule supplied in a follow-up message. The required process skill `/etc/codex/skills/solve-math-rigorously/SKILL.md` was read. No repository scientific files, study history, other studies, external sources, or other reviewers' findings were read. This report is the only assigned output file.

The source-response rule below is an **assumed input**, not a result proved by this check. In particular, this report does not independently establish that rule from a finite-width Gaussian matrix limit. Conclusions involving conditional innovations are conditional on that rule and its stated joint Gaussian and independence properties.

## Setup and supplied initialization rule

At the lower level, let `g=(g1,g2)` have independent standard Gaussian components and put

\[
h_a=\tanh(g_a/\sqrt2),\qquad a\in\{1,2\}.
\]

The two canonical probes are `x1=e1` and `x2=e2`. The reused initialized middle operator is `W0`, with its true adjoint `W0*`. At the upper level,

\[
Y_a=W_0h_a=\Xi_a,\qquad H_a=\tanh\Xi_a,
\]

where the supplied rule states that `Xi1,Xi2` are independent centered Gaussians with variance

\[
v=\mathbb E_g h_1^2>0.
\]

For an admissible smooth upper query `F(Xi1,Xi2)`, the supplied reverse response is

\[
W_0^*F=\zeta_F+\sum_{j=1}^2h_j\,\mathbb E_\Xi[\partial_{\Xi_j}F].
\]

The family `zeta_F` is jointly centered Gaussian, independent of the lower `g`, with

\[
\mathbb E[\zeta_F\zeta_G]=\mathbb E_\Xi[FG].
\]

All queries used below are bounded smooth functions with bounded derivatives, so their upper moments and the displayed derivative expectations exist. Define

\[
\tau=\mathbb E_\Xi H_1^2,\qquad
m_4=\mathbb E_\Xi H_1^4,\qquad
m_6=\mathbb E_\Xi H_1^6,\qquad
\alpha=1-\tau.
\]

Here `0<tau<1`, and all displayed moments are finite because `|H1|<1`. The old lower core is

\[
(h_1,h_2,k_1,k_2),\qquad
Z_j=W_0^*H_j=\zeta_{H_j}+\alpha h_j,\qquad
k_j=\tanh Z_j.
\]

The old upper polynomial core consists of polynomials in `H1,H2`.

## 1. What gradient-flow alignment does and does not establish

The proposed generators arise by differentiating the physical gradient-flow equations and retaining their chain-rule expressions at initialization. This is a concrete local connection to the dynamics: after all required intermediate fields are retained and operator calls are represented exactly, the corresponding finite collection of time derivatives can be matched.

With zero initial readout, the initial hidden-weight velocities themselves vanish. The expressions discussed here are potential leading nonzero coefficients in their time expansions; special labels or other degeneracies can make those coefficients vanish as well. The assignment does not fix all loss, learning-rate, and normalization constants, so this report checks the structural factors rather than an absolute velocity coefficient.

The leading displayed upper factor is

\[
U_{ab}:=H_b\tanh'(Y_a)=H_b(1-H_a^2)=H_b-H_bH_a^2.
\]

Consequently, all four such upper factors already belong to the upper polynomial span of total degree at most three. The lower activation derivative is likewise already polynomial:

\[
\tanh'(g_a/\sqrt2)=1-h_a^2.
\]

Thus these activation factors alone do not distinguish the proposed construction from a polynomial core of sufficient degree. The substantive new lower primitives are the reverse calls

\[
Q_{ab}=W_0^*U_{ab},
\]

and, for first-layer motion, their products `(1-ha^2)Qab`. These calls follow the physical differentiation graph and must use the same initialized operator and its true adjoint. Replacing each call by a newly independent Gaussian operator would not preserve that graph's joint correlations or adjoint identities.

This alignment does not, by itself, prove that the dictionary is minimal, that its time Taylor series converges, that truncation is accurate at a specified positive time, or that it improves long-time performance. Nor does the comparison below establish absence from any larger previously defined hierarchy: it concerns only the explicitly specified old four-feature lower core.

## 2. Exact conditional innovations and non-representability in the old core

Let `S=span(H1,H2)` in the upper real `L2` space, and let `P_S` be orthogonal projection. Independence and symmetry give

\[
\mathbb E H_1H_2=0,\qquad \|H_1\|_2^2=\|H_2\|_2^2=\tau.
\]

### Cross queries

If `a != b`, then

\[
\langle U_{ab},H_a\rangle=0,\qquad
\langle U_{ab},H_b\rangle=\tau(1-\tau),
\]

so

\[
P_SU_{ab}=\alpha H_b,\qquad
R_{ab}:=U_{ab}-P_SU_{ab}=H_b(\tau-H_a^2).
\]

Its squared norm is the finite value

\[
\nu_{\mathrm{cross}}
=\|R_{ab}\|_2^2
=\tau\operatorname{Var}(H_1^2)
=\tau(m_4-\tau^2)>0.
\]

Strict positivity follows because `tau>0` and the nondegenerate Gaussian `Xi1` makes `tanh(Xi1)^2` nonconstant. Differentiating `Uab` also gives

\[
\mathbb E[\partial_{\Xi_a}U_{ab}]=0,\qquad
\mathbb E[\partial_{\Xi_b}U_{ab}]=\alpha^2.
\]

The first identity uses the independent odd factor `Hb`; the second uses independence to factor the product `(1-Ha^2)(1-Hb^2)`.

### Diagonal queries

For `a=b`, symmetry and independence give

\[
P_SU_{aa}=cH_a,\qquad
c=1-\frac{m_4}{\tau}.
\]

Hence

\[
R_{aa}=H_a\left(\frac{m_4}{\tau}-H_a^2\right),
\qquad
\nu_{\mathrm{diag}}=\|R_{aa}\|_2^2
=m_6-\frac{m_4^2}{\tau}>0.
\]

Indeed, Cauchy–Schwarz applied to `H1` and `H1^3` gives `m4^2 <= tau m6`. Equality would require `H1^3=lambda H1` almost surely for a fixed scalar `lambda`. Since `Xi1` has positive density on the real line and tanh is strictly monotone onto `(-1,1)`, `H1` has interval support and `H1^2` is not constant on its nonzero values. Equality is therefore impossible. The derivative expectation is

\[
d:=\mathbb E[\partial_{\Xi_a}U_{aa}]
=\mathbb E[(1-3H_a^2)(1-H_a^2)]
=1-4\tau+3m_4,
\]

and the derivative with respect to the other Gaussian coordinate is zero.

### Conditioning on the old features

Joint Gaussianity and the covariance rule imply the decompositions

\[
\zeta_{U_{ab}}=\alpha\zeta_{H_b}+\eta_{ab}\quad(a\ne b),
\qquad
\zeta_{U_{aa}}=c\zeta_{H_a}+\eta_{aa},
\]

where the centered Gaussian residual is independent of `(zeta_H1,zeta_H2,g)`, with variance `nu_cross` or `nu_diag`, respectively. To verify this directly, subtract the stated Gaussian linear predictor: its covariance with either old Gaussian source is zero by the defining orthogonality of `R`. A jointly Gaussian vector with zero cross-covariance is independent. Independence from `g` is part of the supplied rule. The covariance formula also justifies linearity of the Gaussian-source representation up to almost-sure equality, since any discrepancy has variance zero.

Let

\[
\mathcal C=\sigma(h_1,h_2,k_1,k_2).
\]

The invertibility of tanh yields

\[
g_j=\sqrt2\operatorname{arctanh}h_j,\qquad
\zeta_{H_j}=\operatorname{arctanh}k_j-\alpha h_j.
\]

Thus `C` is exactly the sigma-algebra generated by the old Gaussian sources and `g`, up to completion. Combining the response rule with the decompositions gives the explicit conditional forms

\[
Q_{ab}=\alpha Z_b+\eta_{ab}\quad(a\ne b),
\]

\[
Q_{aa}=cZ_a+(d-c\alpha)h_a+\eta_{aa}.
\]

In particular,

\[
\operatorname{Var}(Q_{ab}\mid\mathcal C)
=\begin{cases}
\tau(m_4-\tau^2),&a\ne b,\\
m_6-m_4^2/\tau,&a=b,
\end{cases}
\]

and both values are finite and strictly positive. Therefore

\[
\operatorname{Var}((1-h_a^2)Q_{ab}\mid\mathcal C)
=(1-h_a^2)^2\operatorname{Var}(Q_{ab}\mid\mathcal C)>0
\quad\text{almost surely}.
\]

Any additional nonzero deterministic chain-rule normalization rescales this variance by its square. A square-integrable random variable measurable with respect to `C` has conditional variance zero, so neither `Qab` nor `(1-ha^2)Qab` can be a measurable function of the old four features. In particular, no exact finite polynomial in those features can represent it, regardless of degree. This is stronger than the observation that recovering `Zj` from `kj` requires the nonpolynomial function arctanh.

For completeness, the four residual upper functions `R11,R22,R12,R21` are pairwise orthogonal. Terms of incompatible parity integrate to zero; the remaining diagonal/cross pairings have a factor `E(tau-Hj^2)=0`. Their corresponding four Gaussian innovations are therefore mutually independent under the supplied joint Gaussian rule. This is a statement about these source residuals, not an assertion that every physical Taylor coefficient contains all four independently after label symmetries or data degeneracies are imposed.

## 3. Fixed probes, sample count, and arbitrary new inputs

For a fixed number `q` of probes and a fixed time order `N`, the chain and product rules generate finitely many expression nodes. For the usual square-loss gradient flow, separating their symbolic label coefficients also produces finitely many coefficient fields at each order. Inductively, a finite derivative expression at order `r` differentiates into another finite expression at order `r+1`; analytic or smooth activation derivatives are evaluated at initialized fields. This is a finite-jet argument, not a claim of convergence of the resulting time series.

With `q=2`, the dictionary size can consequently depend on the order and chosen closure rules while remaining independent of how many samples repeat those two inputs. For square loss, repeated data at each input enter the vector field through the empirical input weight and empirical label sum at that input. Sample replication does not generate new input-conditioned random fields. Retaining ordered index expressions gives a sufficient dictionary; symbolic coefficients or symmetry can make a smaller one possible.

For arbitrarily many distinct new inputs, the same differentiation rules yield finitely many **types of expressions with free input slots**. That is a reusable construction template. It does not imply finite dimension of the span of all instantiated fields.

This distinction already matters before training. For distinct positive scalars `c1<...<cn`, consider

\[
f_j(g)=\tanh(c_jg_1/\sqrt2).
\]

Suppose `sum_j a_j f_j=0` almost surely. The left side is continuous and Gaussian measure has full support, so it is zero everywhere. Write `t=g1/sqrt2`. Sending `t` to positive infinity gives `sum_j a_j=0`. Subtracting that limiting relation and using

\[
\tanh(ct)-1=-\frac{2e^{-2ct}}{1+e^{-2ct}}
\]

shows that multiplication by `exp(2c1 t)` and passage to the limit gives `-2a1=0`. Removing that term and repeating proves every coefficient zero. Since `n` is arbitrary, the family has infinite-dimensional linear span.

Even restricting to unit input directions does not rescue a fixed finite linear dictionary in two dimensions. Choose distinct angles in `(0,pi/2)` and inputs `xj=(cos(theta_j),sin(theta_j))`. An almost-sure relation among `tanh(g dot xj/sqrt2)` is again an everywhere relation by continuity and Gaussian full support. Restriction to `g2=0` reduces it to the preceding argument with distinct positive `cj=cos(theta_j)`.

This excludes a universal finite-dimensional **linear feature span** representing all such input fields exactly. It does not exclude all finite nonlinear parameterizations: for example, the two values `h1,h2` recover `g1,g2`, from which `tanh(g dot x/sqrt2)` can be evaluated nonlinearly for any input `x`. Nor does it establish impossibility for every conceivable nonlinear state representation of the evolving network.

## 4. Constructive extensions and exact projected jet matching

Two constructions have different, explicit scopes.

1. **Exact finite-probe jets.** Fix a finite probe set independently of sample count. Generate all required intermediate fields and symbolic coefficient fields through the desired time order. Include the arguments and results of each initialized forward and reverse operator call. Then the finite dictionary can represent the corresponding finite-probe jets exactly, subject to the required differentiability and operator-domain hypotheses. This includes arbitrarily many repeated labeled samples at those probes.

2. **A fixed-dimensional approximation for unrestricted samples.** Choose fixed lower and upper Galerkin spaces independently of sample count, and project arbitrary-input fields and subsequent nonlinear operations into those spaces. They may be enriched with the finite-probe jet fields above. The evolving coefficient state then has dimension independent of the number of input samples; the empirical loss still sums over samples when computing its vector field. Exact representation of unrestricted physical dynamics is replaced by an approximation. Neither an error tolerance nor convergence under space refinement follows without additional stability, regularity, and approximation estimates.

The relevant exactness condition for the first construction can be stated directly. Let `L,U` be finite-dimensional lower and upper subspaces of their population Hilbert spaces, with orthogonal projections `P_L,P_U`, and define

\[
B=P_UW_0|_L.
\]

Assuming the required vectors belong to the operator and adjoint domains, its Hilbert-space adjoint satisfies

\[
B^*=P_LW_0^*|_U.
\]

Indeed, for `f in L` and `u in U`,

\[
\langle Bf,u\rangle
=\langle W_0f,u\rangle
=\langle f,W_0^*u\rangle
=\langle f,P_LW_0^*u\rangle.
\]

If a required forward argument `f` belongs to `L` and its true result `W0 f` belongs to `U`, then `Bf=W0 f`. Similarly, if a required reverse argument `u` belongs to `U` and `W0* u` belongs to `L`, then `B* u=W0* u`. Retaining both ends of every needed action therefore makes those calls exact. In particular, initialized forward preactivations `Xi_a=W0 h_a` must be represented, not merely their activations `H_a=tanh Xi_a`: replacing `Xi_a` by an inaccurate projection changes the activation evaluated by the projected model. A finite polynomial span in `H1,H2` alone cannot contain the unbounded Gaussian `Xi_a`, because every such polynomial is bounded on `[-1,1]^2`.

If the other intermediate outputs used by the finite differentiation graph are also retained and each projected operation reproduces its required inputs and outputs, induction through that graph gives matching of the represented time derivatives. This is a sufficient closure condition; a particular model might admit equivalent algebraic reductions requiring fewer stored fields. Operator reuse and the adjoint relation remain essential throughout.

An implementation in nonorthonormal bases must use the appropriate population Gram inner products; the adjoint need not be the ordinary transpose of its coordinate matrix. Exact Gram projection, including a correctly handled dependent basis, can preserve membership exactly. Ridge regression generally cannot: if a nonzero target has coefficient vector `c` in a basis with positive-definite Gram matrix `G`, ridge with `lambda>0` returns

\[
\widehat c=(G+\lambda I)^{-1}Gc,
\]

which differs from `c` because equality would imply `lambda c=0`. Ridge can be a useful approximation, but its bias must be included when claiming jet matching. Finite-sample estimates of population inner products likewise require their own numerical-error assessment.

## Conclusion

The new upper factors in the leading displayed term are already degree-three polynomials in the old upper core. Under the supplied reverse-response rule, their reverse images carry explicit positive conditional Gaussian variances absent from the old four-feature lower core, so increasing only that core's polynomial degree cannot recover them. A fixed two-probe construction gives finite dictionaries for finite time jets and arbitrary replication at those probes. Extension to arbitrary new inputs is either a template with potentially infinitely many instantiated fields or a fixed-dimensional approximation with stated projection error. Exact finite-probe jet matching additionally requires retention of operator-call arguments and results, true operator reuse and adjoints, and unbiased projection on the retained spaces.

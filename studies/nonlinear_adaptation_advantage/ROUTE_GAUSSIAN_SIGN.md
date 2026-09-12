# Frozen Gaussian-sign route for E₀

Date: 2026-09-12. Author: fresh scoped `gaussian_sign_route` agent.

**Status.** The route proves a neural-specific signed covariance statement on
the actual reference trajectory near its start. It also identifies precisely
why direct Gaussian association and a positive-response induction do not
settle the sign at the fitted endpoint. It proves no favorable nonlinear versus
full-frozen risk gap, and no favorable relative component learning during the
added-data episode. E₀ remains open by this route. Failure of these particular
Gaussian arguments is not an impossibility theorem for E₀.

The candidate below was frozen before inspecting another route's artifact or
receiving its findings. No experiments, training solvers, Git writes, or target
redesign were used. Only this assigned file was written.

## 1. Scientific input and exact scope

The scientific inputs were the neutral `RESEARCH_CONTRACT.md`,
`docs/NOTATION.md`, and these established units:

- `docs/global_nonlinear.md` A.1–A.4;
- C.4.5.1 §§1–3 and §5, and C.4.5.2 §§1–4;
- C.4.9's model and determining equation;
- C.4.10.2 §1 and the complete strong-derivative proof in §5;
- C.4.10.3, including its complete signed-measure separation and conditioning
  proofs;
- `docs/special_data_limits.md` III.F in full.

The source excerpts sometimes included the heading or first lines of the next
permitted unit. No other study contents, this study's README or reports,
concurrent route files, code, external scientific sources, or Git history were
read. The shared AGENTS and workflow Part 1 and both required mathematical
skills, including the contract and adversarial-audit references, were read.
Repository status was checked as metadata only; concurrent changes were left
untouched. HEAD at that check was
`88172930b86b57f302ae53d0ae28c8bcc33838e4`, with empty staged index.

The exact model is bias-free two-hidden tanh, stored variances
`(1,1/n,1/n²)`, mobilities `(n,1,n)`, output divided by `n`, and unhalved loss.
The actual finite initial readout is retained. The population reference has
zero limiting initial readout and is the actual original-initialization
reference characterized in C.4.5.1. The raw metric contains the full first row,
the learned middle Hilbert–Schmidt increment, and readout. The middle action
and its actual adjoint are retained together. Reference feature time below is
`s`; the E₀ comparison uses the separate canonical added-data slow time
`tau=epsilon t`. The two clocks are not identified.

The fixed family remains

\[
q=q_0+h(a_0\cos\alpha+b_0\sin\alpha
                 +a_1\cos3\alpha+b_1\sin3\alpha+\zeta),
\quad q_0=\cos^3\alpha-\sin^3\alpha,\quad h=\sin^2(2\alpha),
\]

with normalized full-circle measure `rho`, fixed `0<R<=1/8`, independently
varying `a0,b0 in [R/16,R/8]`, `a1,b1 in [R/48,R/24]`, odd `zeta` satisfying
`||zeta||infinity+Lip(zeta)<=R/2048`, and normalized density satisfying
`||p-1||infinity+Lip(p)<=1/4`. No target is chosen around `F_*`.

## 2. A strict signed covariance on the actual reference trajectory

This result concerns reference formation and is independent of the added
family. It is useful because it tests a proposed Gaussian positivity mechanism
on the actual reached states rather than on arbitrary Hilbert-space states.

Let `phi=tanh`. Write `Z_a(s)=A(s)phi(w_a(s))` and

\[
\delta_a(s)=c(s)\phi'(Z_a(s)),\qquad a=1,2.
\]

These are the actual upper backward gates of C.4.5.1–2. Let

\[
v_0=E\tanh^2G\in(0.39,0.4),\qquad
X=Z_1(0),\quad Y=-Z_2(0).
\]

The numerical interval is the rigorous rational certificate in C.4.5.1 §5,
not a new numerical evaluation. The initial forward Gaussian law makes `X,Y`
independent `N(0,v0)`. The sign on `Y` simply expresses the odd network's
second training pair `(e2,-1)` as the exactly equivalent pair `(-e2,+1)`;
there is no change of training problem, metric, or clock.

For a scalar `Z~N(0,v0)`, set

\[
T=\tanh Z,\quad S=\operatorname{sech}^2Z=1-T^2,\quad
\mu=E S,\quad D=E[T^2S]>0,
\]
\[
\eta=E[S^2-2T^2S].
\tag{G1}
\]

Define the actual mixed-covariance matrix

\[
B_{ab}(s)=v_0^{-1}E_2[\delta_a(s)X_b],
\qquad (X_1,X_2)=(X,Y).
\tag{G2}
\]

These are covariances divided by `v0`, since `X_b` is centered. The gates need
not be Gaussian. In particular (G2) does not discard source responses or
pretend that the current state is independent of the initialized action.

**Proposition.** On the actual reference trajectory,

\[
\lim_{s\downarrow0}\frac{B(s)}s
 =\frac12\begin{pmatrix}\eta&\mu^2\\\mu^2&\eta\end{pmatrix},
\qquad 0<\eta<\mu^2,
\qquad \eta-\mu^2\le-\frac25D.
\tag{G3}
\]

Consequently, for `e_+=(1,1)/sqrt(2)` and `e_-=(1,-1)/sqrt(2)`, there is
an actual positive reference interval `0<s<s0` on which

\[
e_+^TB(s)e_+>0,\qquad e_-^TB(s)e_-<0.
\tag{G4}
\]

The statement is about mixed covariance of backward gates with the original
forward Gaussian variables. It is not an assertion that a Gram matrix has a
negative eigenvalue, nor that a tangent kernel is indefinite.

**Proof.** The actual strong reference equations give

\[
\frac{c(s)}s\longrightarrow
\frac12\{\tanh X+\tanh Y\}\quad\hbox{in }L^2(\Omega_2),
\qquad Z_a(s)\longrightarrow Z_a(0)\quad\hbox{in }L^2.
\tag{G5}
\]

The first assertion is the integral equation `c_s=(phi(Z1)-phi(Z2))/2`
and continuity of its right-hand side. The second follows from the strong
continuity of the actual raw reference and bounded action. Bounded-multiplier
continuity, applied after subtracting `c(s)/s` from its limit, gives

\[
\frac{\delta_1(s)}s\to\tfrac12(\tanh X+\tanh Y)\operatorname{sech}^2X,
\qquad
\frac{\delta_2(s)}s\to\tfrac12(\tanh X+\tanh Y)\operatorname{sech}^2Y
\tag{G6}
\]

in `L2`. Pairing with the fixed `L2` variables `X,Y` proves convergence of
every entry in (G2). Gaussian integration by parts is legitimate for the
bounded smooth functions here: integrating their product with the Gaussian
density has zero boundary term and gives `E[Z f(Z)]=v0 E f'(Z)`.
Independence and oddness remove the irrelevant means. The diagonal entry is

\[
\frac{1}{2v_0}E[Z\tanh Z\operatorname{sech}^2 Z]
 =\tfrac12 E[(\tanh Z\operatorname{sech}^2Z)']
 =\eta/2.
\]

The off-diagonal entry is

\[
\tfrac12 E[\operatorname{sech}^2X]\,
       v_0^{-1}E[Y\tanh Y]=\mu^2/2.
\]

The first diagonal expression also proves `eta>0`, since
`Z tanh Z sech²Z` is strictly positive almost surely except at zero.

For the strict contrast sign, the contained Gaussian Poincaré proof in A.3,
after scaling a standard Gaussian by `sqrt(v0)`, states

\[
\operatorname{Var}(f(Z))\le v_0 E|f'(Z)|^2.
\]

Its hypotheses hold for the smooth bounded function `f=sech²`, with bounded
derivative `f'=-2 tanh Z sech² Z`. Thus

\[
\operatorname{Var}(S)\le4v_0 E[T^2S^2]\le4v_0D.
\]

Using (G1),

\[
\eta-\mu^2=\operatorname{Var}(S)-2D
 \le(4v_0-2)D\le-\frac25D<0.
\tag{G7}
\]

This proves (G3). The two limiting quadratic forms are
`(eta+mu²)/2>0` and `(eta-mu²)/2<=-D/5<0`. Their strictness and the entrywise
limit prove (G4) for some common positive `s0`. For example the negative
form is at most `-sD/10` after decreasing `s0`.

No higher source derivative, ambient Hessian, formal time series, or exchange
of width with an increasing transcript was used. This is an `L2` first-order
limit of an already established actual continuous flow, followed by a strict
covariance inequality. It does not supply an evaluated `s0` or any added-time
risk margin. ∎

The size `D` itself has an elementary explicitly positive lower bound, if
desired:

\[
D\ge\frac{2e^{-2}}{\sqrt{2\pi}}
 \tanh^2(\sqrt{0.39})\operatorname{sech}^2(2\sqrt{0.4})>0.
\tag{G8}
\]

Restrict a standard Gaussian to `1<=|G|<=2`; its two-sided probability is at
least `2e^-2/sqrt(2pi)`, and the other two factors bound the increasing tanh
square and decreasing sech square on this event. This bound is not proposed
as an E₀ constant.

## 3. What the covariance calculation invalidates

The following stronger claims would be sufficient ingredients for some simple
Gaussian sign inductions, but they are false already at the leading actual
reference response.

1. **Positive semidefinite mixed Gaussian response in every direction.**
   Equation (G4) contradicts this for the actual mixed covariance (G2). Even
   after rewriting both training labels as positive, the sum and contrast
   have opposite signs. All four entries of the limiting matrix are positive;
   entrywise positivity must not be confused with positive semidefiniteness.

2. **Coordinatewise increasing backward gates.** For the first exact Euler
   readout increment, or equivalently the normalized limit (G6), the first
   gate is

   \[
   d_1(x,y)=\tfrac12(\tanh x+\tanh y)\operatorname{sech}^2x.
   \]

   Its partial derivatives are

   \[
   \partial_y d_1=\tfrac12 S_xS_y>0,\qquad
   \partial_x d_1=\tfrac12 S_x
       [1-3\tanh^2x-2\tanh x\tanh y].
   \tag{G9}
   \]

   The second derivative is positive at `(0,0)` and negative at `(1,0)`:
   `tanh(1)>1/sqrt(3)`, for instance because `e²>7` gives `tanh(1)>3/4`.
   Each sign persists on an open set of positive Gaussian measure. No fixed
   sign flip of either source turns this derivative into a one-signed
   function. Thus a Gaussian-association argument whose hypothesis is
   monotonicity of these gates fails at its stated hypothesis. This does not
   exclude a more specialized covariance identity using cancellations.

3. **Every individual named response coefficient has a meaningful positive
   sign.** At a new current forward slot, the reference source rule contains
   `E[c phi''(Z_a)]`. The actual value statistic has

   \[
   E[c(s)\phi''(Z_1(s))]=-sD+o(s),\qquad
   E[c(s)\phi''(Z_2(s))]=+sD+o(s).
   \tag{G10}
   \]

   This follows from (G5), independence, and
   `phi''=-2 tanh sech²`. But a named-slot sign alone is not a valid
   invariant obstruction: coincident Gaussian slots can have singular
   covariance, and III.F.5 explains that individual derivative coefficients
   are representation-dependent while their contracted response is
   invariant. That is why (G2)–(G7) use actual mixed moments after combining
   the relevant responses. Merely quoting the negative term in (G10) would
   miss the positive derivative of the readout and would not prove (G3).

For comparison, at untrained initialization an identical-feature covariance
does enjoy ordinary positivity: if `(U,V)` are standard jointly Gaussian
with correlation `r>=0`, then `E[tanh(U)tanh(V)]>=0`. A contained verification
is to differentiate its Gaussian integral in `r`: integration by parts gives
`d/dr E[tanh(U)tanh(V)]=E[sech²(U)sech²(V)]>0` for `|r|<1`; at `r=0` the
expectation is zero. Bounded convergence handles endpoints. Gaussian density
derivatives are integrable on every compact subinterval of `(-1,1)`, which
justifies that differentiation. This theorem does not apply to the
nonmonotone gates (G9), and it does not identify the trained fields as jointly
Gaussian.

## 4. Why the fitted reference is still the decisive gap

C.4.5.2 supplies a precise Gaussian-plus-response construction, not a Gaussian
law for all trained fields. At a fixed mesh its forward answer has the form

\[
Z_{ka}^2=\xi_{ka}+\sum_{r<k,b}a_{ka,rb}\delta_{rb},
\]

and its reverse answer has the form

\[
Q_{ka}=\zeta_{ka}+\sum_{r\le k,b}b_{ka,rb}H_{rb}^1.
\tag{G11}
\]

The Gaussian source covariance is the Gram of its corresponding queries.
The response coefficients include derivatives through the whole prior
program. Source groups for opposite orientations are independent; the actual
answers of the action and adjoint are dependent through the response terms.
The first-row roots are independent of the reverse Gaussian source group,
but not of the full adaptive clock or full response remainder.

At the actual feature endpoint, the established bound is

\[
Q_a(s)=\zeta_a(s)+D_a(s),\qquad
|D_a(s)|\le225400e^{2880}+180.
\tag{G12}
\]

No independence of `D_a` from `zeta_a` is asserted. Consequently conditioning
on the response remainder does not leave the Gaussian source unchanged.
Nor is (G12) a small perturbation estimate suitable for carrying a covariance
sign from initialization to `s_dagger`. Its valid use is tail control and
well-posed continuation. The actual feature endpoint only satisfies
`s_dagger<=10`; it is not supplied with a perturbatively small feature-time
bound. Equations (G3)–(G4) therefore cannot be continued to it by the
currently proved estimates.

Even a sign for (G2) at `s_dagger` would not by itself compare E₀ learners:
reference formation is common to the nonlinear learner and the full frozen
comparator. A further signed assertion during the added-data evolution is
necessary.

To see precisely which terms a Gaussian sign would have to control, the
unprojected raw kernel at any reached state is

\[
\begin{aligned}
\kappa_\theta(u,v)={}&(u\cdot v)E_1[
 \phi'(w\cdot u)\phi'(w\cdot v)Q(u)Q(v)]\\
&+E_2[c^2\phi'(Z(u))\phi'(Z(v))]
               E_1[H^1(u)H^1(v)]
 +E_2[H^2(u)H^2(v)].
\end{aligned}
\tag{G13}
\]

This is just the inner product of the three raw gradient blocks, including
the actual Hilbert–Schmidt tensor identity. The projected kernel is

\[
k_\theta(u,v)=\kappa_\theta(u,v)
 -b_\theta(u)^TM_\theta^{-1}b_\theta(v),
\qquad b_\theta(u)=G_\theta^*g_\theta(u).
\tag{G14}
\]

Neither differentiating the expectation products in (G13) nor differentiating
the anchor subtraction in (G14) produces squares alone. The strong
derivative proof C.4.10.2 §5 explicitly contains
`c phi''(Z) Z'`, `A*delta'`, and the derivative of the Gram inverse. A sign
for a single feature covariance, a squared Hermite coefficient, or one
unprojected block would leave those other signed terms uncontrolled.
Equations (G13)–(G14) do not assert that their total derivative has either
sign.

## 5. Exact parity information for the fixed family

This subsection restricts to `p=1,zeta=0` for the orthogonal component
interpretation. It preserves all four prescribed independently variable
coefficients. No extension of a favorable sign to the perturbed family is
claimed because no favorable sign has been proved even in this subcase.

Let `P(u1,u2)=(u2,u1)` and let `Uf=f composed with P`. The population
reference symmetry C.4.5.1 gives `UF_*=-F_*`. Its probability-space isometry
also gives

\[
k_\dagger(Pu,Pv)=k_\dagger(u,v).
\tag{G15}
\]

For completeness, the raw transformation sends predictions to `-f(Pu)` and
is an isometry of the raw increment metric. Its gradient transforms by the
corresponding isometry and a minus sign. The two anchor columns are swapped
and both change sign, so their span and its orthogonal projection transform
under the same isometry. Their projected-gradient inner product proves
(G15). The initial Gaussian law and uniqueness of the actual reference
provide the needed identification of the transformed endpoint. This uses
the actual trained population law, not pointwise symmetry of a finite
network.

Thus the frozen integral operator commutes with `U` on `L2(rho)`. The
orthogonal, independently interpretable decomposition is exchange-symmetric
versus exchange-antisymmetric prediction error:

\[
q_+=\frac h2[(a_0+b_0)(\cos\alpha+\sin\alpha)
                  +(a_1-b_1)(\cos3\alpha-\sin3\alpha)],
\]
\[
q_-=q_0+\frac h2[(a_0-b_0)(\cos\alpha-\sin\alpha)
                  +(a_1+b_1)(\cos3\alpha+\sin3\alpha)].
\tag{G16}
\]

Here `Uq_+=q_+`, `Uq_-=-q_-`; the third-harmonic signs follow from
`cos(3(pi/2-alpha))=-sin(3alpha)` and
`sin(3(pi/2-alpha))=-cos(3alpha)`. The guaranteed symmetric first-harmonic
coefficient and antisymmetric third-harmonic coefficient both remain
quantitatively active under the stated ranges.

The frozen flow evolves these two error sectors separately. The nonlinear
selected flow is equivariant under `(p,q)->(p composed with P,-q composed
with P)` by its actual projected determining equation and uniqueness. In
particular, for uniform density, its total risk and the frozen total risk
satisfy the exact finite-time identity

\[
\mathcal E_{q_-+q_+}(P_{q_-+q_+}(\tau))
=\mathcal E_{q_--q_+}(P_{q_--q_+}(\tau)),
\tag{G17}
\]

with the same identity for the frozen flow, on the common bounded-law
episode. Change variables `u->Pu`, use the transformed predictor
`-P_{q_-+q_+}(tau,Pu)`, and square the transformed residual to prove (G17).
The transformed task need not lie in the fixed coefficient rectangle; (G17)
is an identity of the determining equations, not a paired counterexample
inside the family. It implies that a purported total-risk contribution odd
in the whole symmetric target part must cancel in any differentiable local
description. It gives no sign for the remaining even contribution.

For general allowed density, antipodal symmetrization
`p_s(u)=(p(u)+p(-u))/2` leaves odd-predictor risk and force integrals unchanged,
as C.4.10.3 shows. It does not make the density invariant under coordinate
exchange. Accordingly the two sectors in (G16) need not be orthogonal in
the actual metric `L2(p rho)` and the frozen operator need not preserve
them. A use of this decomposition for E₀ would have to treat those density
interactions, not silently replace `p` by its coordinate-swap average.

## 6. Claims, checks, and the remaining obligation

| Claim | Result and check status | Logical limit |
|---|---|---|
| Actual early-reference mixed covariance has opposite sum/contrast signs | Proved above from the actual strong equations, independent initial Gaussian law, integration by parts, and the contained Gaussian Poincaré inequality; algebra and signs self-checked | Reference time near zero; not the fitted endpoint and not added-time risk |
| A naive monotone-backward-gate Gaussian association induction applies | Its monotonicity hypothesis is contradicted by (G9) | More specialized cancellation identities remain possible |
| A negative named coefficient alone rules out positivity | Rejected as an invalid argument; singular-support coefficients must be contracted | Invariant mixed moments (G2) avoid this loophole |
| Frozen parity sectors are independent at `p=1` | Exact, from the reference raw isometry and kernel covariance | No ordered learning rate or nonlinear advantage |
| Gaussian covariance provides a uniform favorable E₀ sign | Open | No signed endpoint-to-added-flow bridge |
| Finite-time advantage, relative component benefit, empirical and finite-network gap | Not proved by this route | Existing continuation cannot manufacture a missing population comparison |

The most consequential unresolved Gaussian obligation is to control a
**contracted signed response of the actual fitted source history**, including
all raw blocks and the anchor projection, in a way that remains signed on a
positive added-time interval for the entire fixed coefficient rectangle.
Ordinary covariance positivity for the initial tanh features, PSD of tangent
Grams, and reference conditioning do not supply that assertion. The early
negative contrast covariance is a concrete reason that an induction asserting
positive response in every Gaussian direction is unavailable.

There has been no independent audit of this report and no promotion. The
self-check was analytical: verify the actual-flow `L2` limit, integrate the
two Gaussian moments directly, apply the stated Poincaré inequality with its
scaling, check the derivative signs at two finite points, and check the
coordinate-swap signs of every listed harmonic. No empirical or numerical
evidence is claimed.

Source hashes at freeze:

```text
AGENTS.md
7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba
RESEARCH_WORKFLOW.md
8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12
docs/NOTATION.md
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b
docs/global_nonlinear.md
5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483
docs/special_data_limits.md
5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489
studies/nonlinear_adaptation_advantage/RESEARCH_CONTRACT.md
0bbd681da93a44574fbe30d9ee7fd5a984105d363c473c7756f31964c2896c0f
```

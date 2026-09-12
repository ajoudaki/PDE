# Internal check of the frozen Gaussian-sign route

Checker: `/root/geometry_route`, 2026-09-12.

Input: `ROUTE_GAUSSIAN_SIGN.md`, all 484 lines, SHA256
`2b1d2397526624922f932a9fcea9e2cf0471f10335f211cb2c44e3814e36093c`.
The frozen input is preserved. This is an internal mathematical check,
not a promotion review, numerical certificate, or new sign-search route.

**Verdict: PASS for the stated claims and limitations.** I independently
reconstructed G1–G17 and found no required scientific correction. In
particular, G3–G8 prove a strict signed mixed covariance on a positive
initial interval of the actual reference feature trajectory. The proof
does not reach the fitted endpoint or compare the added-data learners.
The report expressly maintains those limitations.

## 1. Actual reference, Gaussian normalization, and label sign

C.4.5.1 R1–R5 use the full first row, initialized action and its actual
adjoint, learned Hilbert–Schmidt increment, and readout in the prescribed
raw metric. Initially the two first-layer features are independent odd
functions of independent standard Gaussians. Their uncentered Gram is
v0 I2, where v0=E tanh²G. The initial forward Gaussian rule therefore
makes Z1(0), Z2(0) independent N(0,v0). Negating the second variable leaves
that independent Gaussian law unchanged. The interval 0.39<v0<0.4 is the
already established rational certificate; no numerical evaluation was
performed in this check.

The population c(0)=0 is the established limit of the specified finite
Gaussian readout, not a substituted finite initialization. The reference
equation is exactly

\[
c_s=\tfrac12\{\tanh Z_1(s)-\tanh Z_2(s)\}.
\]

Thus, for X=Z1(0) and Y=-Z2(0), its initial velocity is
(tanh X+tanh Y)/2, including the factor 1/2. The use of feature time s
does not identify it with physical time or the added-data slow time.

The second training observation (e2,-1) can indeed be written as
(-e2,+1). For every raw state the bias-free odd predictor satisfies
f(-e2)=-f(e2), so the squared loss and its raw gradient are identical
under this rewriting. Upper backward gates c phi'(Z) remain unchanged
because phi' is even. Other gradient blocks transform with their proper
input/feature signs. Accordingly G2 is a correctly oriented mixed moment,
not a change to the task, optimizer, or metric.

## 2. Strong limit and strict covariance: G1–G8

Strong continuity of the reference gives the Bochner-integral limit

\[
c(s)/s\longrightarrow h_0=(\tanh X+\tanh Y)/2
\quad\hbox{in }L^2.
\]

Also Z_a(s) converges strongly in L2: subtract the bounded action and
the Lipschitz first-layer feature separately. To obtain G6, write

\[
\frac{c(s)}s\phi'(Z_a(s))-h_0\phi'(Z_a(0))
=\left(\frac{c(s)}s-h_0\right)\phi'(Z_a(s))
 +h_0\{\phi'(Z_a(s))-\phi'(Z_a(0))\}.
\]

The first term tends to zero by boundedness of phi'; the second by the
contained bounded-multiplier lemma. This supplies L2 convergence without
a higher time derivative, an ambient L2 Hessian, or an empirical
high-moment passage. Pairing with each fixed Gaussian X_b is continuous
by Cauchy–Schwarz. Since E X_b=0, E[delta_a X_b] is the covariance even
without separately proving the gate mean is zero.

For Z~N(0,v0), integration by parts gives
E[Zf(Z)]=v0 E[f'(Z)] for the bounded smooth functions at issue. With
T=tanh Z and S=sech²Z,

\[
(TS)'=S^2-2T^2S,\qquad T'=S.
\]

The diagonal entry of B(s)/s therefore tends to eta/2. The cross term
is (E S)E[ZT]/(2v0)=mu²/2; the other terms vanish by independence and
oddness. This proves the full matrix limit in G3. Moreover,

\[
\eta=v_0^{-1}E[ZT S]>0,
\]

because the integrand is positive away from zero. D=E[T²S] is likewise
strictly positive.

For the Poincaré step, apply the contained standard-normal inequality to
g(x)=f(sqrt(v0)x). Its derivative is sqrt(v0) f'(sqrt(v0)x), giving

\[
\operatorname{Var}(f(Z))\le v_0 E|f'(Z)|^2.
\]

There is no missing variance factor or inverse variance. Taking f=S and
using S'=-2TS and 0<S<=1 yields

\[
\eta-\mu^2
=\operatorname{Var}(S)-2D
\le4v_0 E[T^2S^2]-2D
\le(4v_0-2)D\le-\tfrac25D<0.
\]

All hypotheses hold: S and its derivative are smooth and bounded.
The limiting sum and contrast quadratic forms are respectively
(eta+mu²)/2>0 and (eta-mu²)/2<=-D/5. Entrywise convergence gives a common
positive interval with the G4 signs. It also justifies the stated
eventual contrast bound -sD/10. No effective numerical value of that
interval is proved or claimed.

For G8, on 1<=|G|<=2 the standard-normal probability is at least
2 exp(-2)/sqrt(2pi). The variance interval gives
sqrt(0.39)<=|Z|<=2sqrt(0.4). Monotonicity of tanh² and sech² on the
positive half-line supplies the two displayed lower factors. Thus G8
is an explicitly positive valid lower bound for D, with no extra
factor of v0 or interval length missing.

## 3. Monotonicity, named sources, and the endpoint limitation

I directly differentiated d1 in G9. The derivatives are
Sx Sy/2 and Sx(1-3Tx²-2Tx Ty)/2. The latter is positive at (0,0) and
negative at (1,0); the elementary bound e²>7 gives tanh(1)>3/4 and
hence proves the negative sign. Continuity gives positive Gaussian
measure for both signs. Reversing a fixed source coordinate preserves
this sign change somewhere. This invalidates the indicated
coordinatewise-monotone gate induction, without excluding specialized
covariance cancellations.

The first exact Euler readout update has unchanged w and K because
their initial velocities contain c(0)=0. Its backward gate divided by
the step is exactly the d1 expression. Hence the diagnostic concerns
the actual reference program, rather than an invented state.

G10 also has the correct original-anchor signs. Pairing the G5 limit
with phi''(X)=-2TX SX gives -D; pairing it with
phi''(-Y)=2TY SY gives +D. These are valid value statistics. Their
identification as individual named response terms does not make the
sign of an arbitrary named coefficient representation invariant.

The singular-source caveat agrees precisely with III.F.5. If the source
covariance is Gamma, equal expressions on its Gaussian support have
expected derivative vectors differing in ker Gamma. The associated
input vector annihilates that difference almost surely because its
Gram is also Gamma. Therefore the contracted response is invariant,
while individual coefficients need not be. G2 instead pairs actual
fields with the fixed actual initial forward Gaussian variables, so
its sign is unaffected by this ambiguity. The report correctly avoids
inferring G3 from the negative current coefficient alone.

The comparison concerning ordinary initial tanh covariance is valid.
For correlation r in (-1,1), differentiating the bivariate Gaussian
density and integrating by parts yields
d E[tanh U tanh V]/dr=E[sech²U sech²V]>0. The density derivatives are
integrable on compact correlation intervals, and bounded convergence
handles r=1. This establishes positivity for r>=0, but supplies no
monotonicity theorem for G9 or Gaussian law for trained gates.

G11 reproduces the causal source recursion with all earlier response
terms, including the learned-rank contributions in its coefficients.
Independent oriented Gaussian source groups do not imply independent
forward and reverse answers. G12 is the established common-flow
Gaussian-plus-bounded representation, with the stated bound
225400 exp(2880)+180. That bound asserts neither independence of the
remainder nor a perturbatively small error. The report therefore
correctly refuses to condition on the remainder as if the Gaussian
source law were unchanged, or to transport the early sign to s_dagger.

G13 is the exact inner product of the three raw gradient blocks. Its
middle term follows from the Hilbert–Schmidt tensor identity. G14 is
the orthogonal anchor projection formula. Their derivatives include
signed gate, adjoint, and projector terms; the report does not erase
them or infer a sign from a single unprojected covariance. A negative
mixed covariance is not a negative Gram eigenvalue or an E₀ risk gap.

## 4. Reference symmetry, finite-time parity, and density limits

The raw transformation (w,A,c)->(wP,A,-c) is an isometry and sends a
prediction f to -f composed with P. The established probability-space
coordinate isometry identifies the transformed reference with the
actual reference. Differentiating the prediction identity transforms
gradients by the same raw isometry and a minus sign. The anchor columns
are exchanged and negated; their span and its orthogonal projector
transform with that isometry. The projected-gradient inner product
therefore proves G15 for the full fitted-reference kernel. Prediction
symmetry alone would not suffice; the report supplies the required
gradient and projector argument.

For uniform density, U:f->f composed with P is a unitary involution
and G15 implies K U=U K. Its +1 and -1 eigenspaces are orthogonal and
are preserved by the full frozen semigroup. Direct substitution of
alpha->pi/2-alpha gives

\[
\cos\alpha\mapsto\sin\alpha,\quad
\sin\alpha\mapsto\cos\alpha,\quad
\cos3\alpha\mapsto-\sin3\alpha,\quad
\sin3\alpha\mapsto-\cos3\alpha.
\]

Together with Uq0=-q0 and Uh=h, these give every sign in G16. The
coefficients (a0+b0)/2 and (a1+b1)/2 have respective lower bounds
R/16 and R/48. This is compatible with all four original coefficients
varying independently; no favorable subset is selected. The two parity
sectors are invariant linear subspaces, not a claim of statistical
independence or an ordered learning rate.

The projected determining equation is equivariant under
(p,q,f)->(p composed with P,-q composed with P,-f composed with P).
The same raw isometry transports the full anchor projector, and the
reference initial condition is preserved under its population
identification. Uniqueness therefore identifies the transformed flow
on the common bounded-law interval. With q=q_-+q_+ this changes the
target to q_--q_+, giving G17 by change of variables. The frozen flow
has the same property. If risk includes binary-label conditional
variance, it remains invariant too: the integrand is
f²-2fq+1, or equivalently (f-q)²+1-q², and both terms transform
correctly. No variance term is missing from the parity identity.

The transformed target need not belong to the positive coefficient
rectangle. The report says so explicitly and uses the symmetry as an
identity on bounded laws, not as a within-family sign reversal. Where
a differentiable expansion in the whole symmetric component exists,
its odd contributions cancel. This conclusion does not assert higher
regularity or determine the remaining even terms.

For a general allowed density, antipodal symmetrization is legitimate
because f, q and the raw gradient feature are odd: squared-risk and
residual-times-gradient integrands are even. Coordinate-swap
symmetrization is a different operation. In fact the kernel identity
gives K_p U=U K_(p composed with P); it need not give K_p U=U K_p.
The two parity sectors need not be orthogonal in L2(p rho).

As a direct check of that caveat within the permitted density bounds,
take p(alpha)=1+epsilon cos(2alpha) with 0<epsilon<=1/16. Its integral
is one and ||p-1||infinity+Lip(p)<=3epsilon<1/4, including for chord
distance on the unit circle. It is already antipodally even but changes
under the swap. The odd functions cos(alpha)+sin(alpha) and
cos(alpha)-sin(alpha) have opposite swap parity, while their weighted
inner product is epsilon/2. This is a check of the report's density
limitation, not a new task family or a sign experiment. No favorable
sign is asserted for these perturbations or for nonzero zeta.

## 5. Read coverage, checks, and limits

The frozen report was read completely in consecutive scopes 1–260 and
261–484. The following allowed established material had already been
read completely in this agent context and was available for this check:

- `docs/global_nonlinear.md`: 1840–1898 (A.1–A.4), 5475–5782
  (C.4.5.1 §§1–3), 5999–6103 (§5), 6104–6521 (C.4.5.2 §§1–4),
  and 12994–17016 (complete C.4.9–C.4.10).
- `docs/special_data_limits.md`: 3785–4326, complete III.F.
- Neutral `RESEARCH_CONTRACT.md` and `docs/NOTATION.md`: complete.
- The required rigorous-math and conjecture-investigation skills,
  their previously required process references, and the research
  workflow: complete prior process coverage, unchanged instructions.

During this check I reread global_nonlinear 1840–1898, 5475–5782,
5999–6103, 6104–6244, 6430–6521, and 16536–16598. A batched reread of
the already-complete III.F source was output-truncated; the relevant
source-response and singular-support material was then reread explicitly
and completely at 3946–4053. The complete prior III.F read is not inferred
from that truncated output. Targeted location searches supplied metadata
only. No other current route or review was read for this check.

Source hashes:

| Input | SHA256 |
|---|---|
| ROUTE_GAUSSIAN_SIGN.md | `2b1d2397526624922f932a9fcea9e2cf0471f10335f211cb2c44e3814e36093c` |
| RESEARCH_CONTRACT.md | `0bbd681da93a44574fbe30d9ee7fd5a984105d363c473c7756f31964c2896c0f` |
| docs/NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| docs/global_nonlinear.md | `5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483` |
| docs/special_data_limits.md | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| RESEARCH_WORKFLOW.md | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| /etc/codex/skills/solve-math-rigorously/SKILL.md | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| /etc/codex/skills/investigate-conjectures/SKILL.md | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |

All new checks were analytic reconstructions and elementary substitutions.
No training, quadrature, random simulation, external source, other study,
Git history, or Git write was used. The only file written is this check.
The result is a checked actual-neural early-reference covariance sign and
checked limitations; the signed fitted-endpoint and finite added-time
comparison obligations remain unresolved.

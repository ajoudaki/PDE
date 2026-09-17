# Isolated audit of the singular response and quartic obstruction

2026-09-16. Fresh isolated mathematical review. No experiment, external
scientific source, author history, other review, or promotion was used.

**Verdict: the principal conditional response theorems and the stated ambient
residual-quadratic obstruction pass this audit.** I found no missing
coercivity premise, incorrect limiting forcing, or incorrect normalization in
those arguments. Two short summary phrases should be tightened, as specified
below. Neither report proves that a canonical unit-label seed has a singular
endpoint, that its actual quadratic disagreement is nonzero, or that generic
initialized exponential fitting fails.

The complete frozen reports reviewed were:

- `correction_flow.md`, SHA-256
  `8c14dfa7337cf573f26a8f4ecc0c7af8a4c368e63835a2949533dc2964f20169`;
- `correction_design.md`, SHA-256
  `d93ea65f2a6fe5b1929a6b7877bb06e3752319e9e449cb3da8e7bad0fc718cf7`.

Permitted dependencies actually read were `docs/NOTATION.md`,
`docs/observable_p1.md`, `docs/global_nonlinear.md` C.4.7.9 and C.4.7.10
B/C.1/D.3, and the complete same-study `three_coordinate_candidate.md`,
`perturbation_modes.md`, `sphere_second_variation.md`,
`rho_singular_hessian.md`, and `rho_endpoint_extension.md`. References from
these inputs to additional reports were not followed. The
solve-math-rigorously skill and the adversarial-audit instructions of
investigate-conjectures were applied. The main review scope is the conditional
singular endpoint argument and the quartic/neighborhood obstruction; this is
not an independent review of every theorem in the dependency library.

## 1. Precise hypotheses and topology

Fix one admitted symmetric input triple, with its prescribed Gaussian marks,
dictionary, eta=1/4096, full matrix, unit labels, and physical metric. All
constants below may depend on this seed and the chosen finite input
directions. There is no uniformity assertion over the entire rho family.
Assume its initialized symmetric fitting endpoint is singular. The rank-loss
criterion in `rho_endpoint_extension.md`, Sections 3–4, applies also at
rho=-1/2 and gives

    z_i=kS, d_i=0, m_i=1,
    g_i=g=(0,H,0), H=tanh(kS), C_*=E2 H^2>0, k!=0.

The base curve comes from the bounded auxiliary interval [0,s_*] of
`three_coordinate_candidate.md`, Sections 6–7. Since F_s>=C0,

    e(t)<=exp(-2C0 t),
    C0(s_*-s(t))<=F(s_*)-F(s(t))=e(t).

Bounded auxiliary speed therefore yields exponential convergence of the base
in the norm of bounded row increments, bounded readout, and finite matrix.
In particular w(t)-w_* converges in unweighted L-infinity, although w_* itself
has the unbounded Gaussian part G. Here G denotes the lower Gaussian mark,
and g denotes the common prediction gradient above. This distinction is essential to the
operator estimates below.

For p=1+|G|, use the spaces E_j with row norm ess sup |h_w|/p^j, readout
L-infinity norm, and matrix Frobenius norm. Their embeddings into the physical
Hilbert space follow from E1 p^(2j)<infinity. The finite-horizon derivatives
are actual data derivatives in the topology of `sphere_second_variation.md`,
namely lower L2, upper L-infinity, and the finite matrix norm. They are
identified there by an E6 Taylor-defect estimate and Gaussian domination;
the response fields themselves have E1 and E2 envelopes.

The all-time argument uses those fields as solutions of bounded linear
equations on E1/E2. It does not require the input-to-state map to be C2 into
E1 or E2, or the nonlinear vector field to be Frechet C2 on an unrestricted
Hilbert ball. `correction_design.md`, Section 6, states this distinction
explicitly. `correction_flow.md` is valid with the same interpretation.

## 2. First initialized response: source decay and neutral limit

Write r_i=m_i-1 in the unnormalized convention of `correction_flow.md`.
Along the symmetric base, r_i=-e. Differentiating the physical gradient flow
in a state direction gives the linear response operator

    A(t)=-(2/3) sum_i g_i tensor g_i
                         +(2e/3) sum_i D_X g_i.

On every fixed E_j it has the decomposition

    A(t)=-2g tensor g+E(t),
    ||E(t)||_(E_j -> E_j)<=C_j exp(-a t).

This is a justified operator statement. For example, with
u_i=w.v_i, t_i=tanh'(u_i), and h=(h_w,h_c,h_M),

    a_i'[h]=E1[b1 t_i(h_w.v_i)],
    z_i'[h]=b2^T(h_M a_i+M a_i'[h]),
    d_i'[h]=E2[b2{h_c tanh'(z_i)+c tanh''(z_i)z_i'[h]}].

The only unintegrated row multiplier in D_X g_i[h] beyond these finite
contractions is a bounded coefficient times h_w.v_i. Thus its E_j norm is
bounded by a constant times ||h||_E_j. Comparing coefficients at X(t) and
X_* uses their unweighted base convergence and the bounded derivatives of
tanh; integrating a polynomial row envelope uses finite Gaussian moments.
The same reasoning applies to the rank-one terms. No product of arbitrary
L2 perturbations is being asserted to lie in L2.

The direct fixed-state input derivative is

    m_i^d=d_i^T M E1[b1 t_i(w.eta_i)].

At X_* it vanishes because d_i=0. Along the base, d_i=O(exp(-a t)); the
remaining contraction is uniformly finite because |w.eta_i|<=C p. Hence
m_i^d=O(exp(-a t)). The direct input gradient derivative g_i^d is uniformly
bounded in E1. Consequently the actual forcing

    V_1=-(2/3) sum_i(m_i^d g_i+r_i g_i^d)

decays exponentially in E1. This checks both sources; small residual alone
would not control the first summand without the zero-reverse identity.

Let P h=g<g,h>/C_* and Q=I-P. The semigroup of -2g tensor g is
Q+exp(-2C_*t)P and is bounded on each E_j. For

    h1_dot=(-2g tensor g+E(t))h1+V_1(t), h1(0)=0,

variation of constants gives an integral inequality with integrable
coefficient ||E(t)|| and integrable source ||V_1(t)||. Multiplication by the
scalar integrating factor gives a uniform bound for h1. Then
Q h1_dot=Q(E h1+V_1) is exponentially integrable, proving exponential
convergence of Qh1. The P equation is a scalar stable equation with
exponentially decaying forcing. The possible factor 1+t when exponents agree
is absorbed by lowering the rate. Therefore

    h1(t)->h1_*, <g,h1_*>=0,
    m_i'[t]=<g_i(t),h1(t)>+m_i^d(t)->0.

This proves boundedness and convergence of the state derivative, and decay
of the output derivative. It does not prove h1_*=0. The finite integral of
the homogeneous transverse damping cannot override the cancellation in this
actual forced response system.

## 3. Second response: a normal forcing and a transverse output limit

The second variation can be separated without assuming its boundedness:

    m_i''=<g_i,h2>+B_i(t),
    g_i''=D_X g_i[h2]+G_i^(2)(t).

Here B_i and G_i^(2) contain only the known base, first response, and direct
first/second input derivatives, including sphere curvature. Since h1 is
bounded and converges in E1, these sources are bounded and converge
exponentially in E2. A product of two lower first variations costs at most
p^2; all such contractions have finite Gaussian moments. Their construction
does not presume a limit of h2.

At the endpoint put

    ell_i=h1_{*,M} a_i
             +M_* E1[b1 tanh'(w_*.v_i)(h1_{*,w}.v_i+w_*.eta_i)],
    z_i^(1)=b2^T ell_i.

In the predictor second derivative, the entire term
E2[c_* tanh'(z) z_i^(2)] equals d_i^T times a finite coefficient and is
zero. Thus the second hidden response and sphere acceleration have zero
coefficient at this endpoint; they have not been omitted before
differentiation. The remaining source is exactly

    B_i=2E2[h1_{*,c} tanh'(z) z_i^(1)]
                         +E2[c_* tanh''(z)(z_i^(1))^2].

The full second equation is consequently

    h2_dot=(-2g tensor g+E(t))h2+f2(t),
    f2(t)=-(2/3)sum_i{B_i(t)g_i+2m_i' g_i'+r_i G_i^(2)},
    f2(t)->-2 bar B g, bar B=(B_1+B_2+B_3)/3.

The limiting forcing is purely normal to ker <g,.>. In particular there is
no unaccounted constant neutral forcing at second order. Let
k0=-bar B g/C_*. Then

    (-2g tensor g)k0-2 bar B g=0.

The equation for h2-k0 has exponentially decaying forcing, including the
extra E(t)k0 term, and the same integrable operator perturbation. The P/Q
argument just proved gives exponential convergence in E2 and

    <g,h2_*>=-bar B,
    lim_(t->infinity) m_i''(t)=B_i-bar B.

In `correction_design.md`, q_i in (24) is exactly this B_i: expand
z_i^(1)=b2^T ell_i. Its residual is divided by sqrt(3), so (25) is
precisely

    lim r2=(I-nn^T)B/sqrt(3).

All factors of 2, 3, and sqrt(3) agree between the two reports. Mixed
directions follow by polarization of the bilinear finite-horizon responses
and the same bounds.

The third-order coefficient in `correction_flow.md` (20) also has the correct
product-rule factor. The third physical variation contains
-(2/3)sum_i 3m_i'' g_i', leaving -2sum_i b_i Gamma_i, where
b_i=B_i-bar B. Its other nondecaying source is parallel to g. Finite-order
tanh differentiation and polynomial envelopes construct the third response
on each finite interval. More explicitly, the first, second, and third row
responses have envelopes p, p^2, and p^3. Substituting their degree-three
Taylor polynomial into the equation leaves a defect bounded by
C_T |epsilon|^4 p^12 in the lower block, with the corresponding finite
integrated bounds in the other blocks. Bounded derivatives of tanh and its
gate and the E12 integral comparison give an actual O_T(|epsilon|^4)
Hilbert remainder, as in the permitted second-variation proof. The bounded limiting forcing and integrable E(t)
first give O(1+t) growth. Hence E(t)h3(t) is integrable, and projection and
integration yield

    Qh3(t)=-2t sum_i b_i QGamma_i+O(1).

This checks the displayed conditional secular coefficient, not its
nonvanishing for a canonical input direction.

## 4. The explicit state path does establish the ambient obstruction

The construction in `correction_flow.md`, Section 6, supplies the step that
mere singularity of the tangent Gram would not supply: an admissible nearby
state path with positive residual loss in a weak direction.

Set T=S sech^2(kS), and let h_c be its component perpendicular to H.
The Taylor coefficients of T and H at zero show they cannot be proportional
when k!=0. Positive upper density gives ||h_c||_2^2>0. Exchangeability then
gives exactly

    E2[b2 h_c sech^2(kS)]=gamma 1,
    gamma=||h_c||_2^2/(3R_Z)>0.

Next M_*^T 1 cannot be zero because M_*a_i=R_Z k1. The lower active
features are independent: conditioning on G makes the independent reverse
noises eliminate every reverse-feature coefficient in a vanishing linear
combination, and independence of tanh G_j eliminates the remaining ones.
Thus V0=b1^T M_*^T1 is a nonzero bounded lower field. For

    h_w=V0(t_1 v_1-t_2 v_2), t_i=sech^2(w_*.v_i),

pairwise nonparallelism gives
|t_1v_1-t_2v_2|^2>=(1-|rho|)(t_1^2+t_2^2)>0. This remains valid at
rho=-1/2. The mixed pairing is therefore

    E2[h_c sech^2(z)(z_1^(1)-z_2^(1))]
                                 =gamma ||h_w||_2^2>0.

For h=(h_w,alpha h_c,0), the difference B_1(alpha)-B_2(alpha) has nonzero
slope. At least one of alpha=0 and alpha=1 has nonzero difference; this is
a finite explicit choice rather than an unsupported genericity argument.
The direction is neutral because <H,h_c>=0. Choosing

    k0=(0,-bar B H/C_*,0),
    X_tau=X_*+tau h+(tau^2/2)k0

removes precisely the common quadratic output component. Taylor expansion
along these bounded directions gives

    r_i(X_tau)=(tau^2/2)b_i+O(tau^3),
    sum_i b_i=0, b!=0,
    L(X_tau)=(tau^4/12)sum_i b_i^2+O(tau^5),
    ||grad L(X_tau)||=O(|tau|^3).

The last statement uses g_i(X_tau)=g+O(tau) and sum_i b_i=0. Consequently
|L_dot|/L=O(tau^2). If the opening phrase “a cubic physical velocity” is
read as exact order, it also follows: differentiating the smooth scalar
expansion along X_tau yields

    <grad L(X_tau),h+tau k0>
                       =(tau^3/3)sum_i b_i^2+O(tau^4),

so ||grad L|| is bounded below by a positive multiple of |tau|^3 for small
nonzero tau. There is no missing lower-order velocity.

Now consider P=(1/3)r^T A(X)r with the stated local positive lower bound,
bounded A, and locally bounded first differential in the physical norm.
Along this path P is bounded above and below by positive multiples of
tau^4. Its differential obeys

    DP[h]=(2/3)(Ar)^T J h+(1/3)r^T DA[h]r,

so ||DP||=O(tau^2). Therefore

    |Lie_V P|<=||DP|| ||grad L||=O(|tau|^5)=o(P).

This contradicts Lie_V P<=-lambda P for any fixed lambda>0 on an entire
neighborhood containing the path. It applies to the gradient-square
correction because its residual matrix is W I+(4kappa/3)G, with W>=1 and
the required bounded derivatives on this bounded path. The proof is also
valid for a finite smooth residual metric supplied by a curvature completion.

The path is a valid current characteristic state perturbation with the same
marks and matrix dimensions. The proof makes no claim that it is reached by
changing only the inputs from canonical initialization. Its use is therefore
legitimate for a full state neighborhood and insufficient for a reachable-set
no-go statement, exactly as the report says.

## 5. Other exact identities and the narrower matrix obstruction

Direct rederivation confirms the mean/disagreement identities, complete old
potential derivative, homological correction equations, trained-chain-rule
terms, and gradient-square derivative in `correction_flow.md` (2)–(12).
In particular the differentiation of the actual initialization constant and
of the vector field is not silently frozen.

For `correction_design.md`, differentiation of chi=zeta+e b/k gives
chi_dot=-2(H-bb^T/k)zeta+e(b/k)_dot. The inverse derivative and the two
metric-derivative terms in (12) have their correct signs and coefficients.
No favorable sign for their sum is proved or used. The positive curvature
Gram on a fixed symmetric compact segment follows from the positive
quadratic-contact coefficient of the full gradients in the permitted rho
endpoint report. It supplies regularity of the metric, not physical
transverse damping.

At a stationary singular state, P_dot=0. For a null vector Kv=0, both
v^T KPv and v^T PKv are zero, so the proposed positive matrix certificate
cannot hold. This is only an all-residual sufficient-certificate obstruction
unless an actual residual path is supplied. The design report states that
qualification correctly; the flow report supplies the stronger ambient path
argument separately.

The fitting readout c_dagger is also algebraically valid. Its denominator is
the squared norm of the component of tanh(z) perpendicular to the three
fields b2_j sech^2(z). Positive cube density and the nonzero cubic term of
sinh(2z)/2 exclude a zero denominator for zbar!=0. The projection identities
give both fitting and zero reverse coefficient. Its moving-comparison energy
has exactly the final hidden-motion term displayed in (19), so no omitted
negative sign turns it into the claimed all-time theorem.

## 6. Localized wording corrections and unresolved claims

There are no blocking mathematical defects in the principal results reviewed.
The following wording changes would prevent stronger readings than the
proofs support:

1. `correction_design.md:429` says “First initialized input-flow response
   tends to zero.” The state response is only proved to converge to a neutral
   limit, which may be nonzero. Replace this by “First initialized output
   response tends to zero; the first state response converges to a neutral
   limit.” The body of Section 6 already has the correct statement.
2. `correction_flow.md:30` says the second derivative “can tend to a nonzero
   disagreement.” Read in isolation this can suggest that a nonzero actual
   response has been exhibited. Replace it by “The second tends to the
   explicit centered quadratic vector below; whether that vector is nonzero
   for an actual canonical seed direction is unresolved.” Sections 5 and 8
   already preserve this boundary.

For topology clarity, the phrase “finite-time weighted-space
differentiability” at `correction_flow.md:119` would be safer if it explicitly
named the Hilbert derivatives and polynomial weighted estimates. The source
does prove a Taylor estimate in a higher weighted space; this is not a
mathematical defect, but it must not be paraphrased as C2 data dependence in
the sharp E1/E2 response-envelope norms.

The conditional results leave the following statements unverified:

- existence of a singular unit-label endpoint in the prescribed initialized
  family;
- nonvanishing or universal vanishing of B_i-bar B for the actual first
  initialized response;
- nonvanishing of the third-order secular coefficient on such a response;
- an all-time Taylor remainder uniform at a fixed nonzero input perturbation,
  or interchange of input differentiation and the nonlinear endpoint limit;
- a uniformly decaying corrected potential on the initialized reachable set,
  or broad generic failure of exponential fitting.

These are appropriately left open in the reports. The verified conclusions
are internal conditional theorems and an ambient obstruction with explicit
hypotheses, not a promotion or a counterexample to the requested initialized
perturbation theorem.

## Versioned addendum: wording corrections verified

2026-09-16, revision 2. The original frozen review above is preserved.
I verified the three revised passages against the issues in Section 6 and
confirmed these current SHA-256 identifiers:

- `correction_flow.md`:
  `8602bc182425614c916908cb6e5aa791221e204b428b504c51e04c383261da9f`;
- `correction_design.md`:
  `3d09ecb900e902f3b1e42b6c74fe57f7da9dbf40dce33b6825222e297efd9efe`.

All three wording issues are resolved. The design status table distinguishes
decay of the first output response from convergence of the first state
response to a possibly nonzero neutral limit. The flow opening explicitly
leaves nonvanishing of the actual centered quadratic response unresolved.
Its regularity paragraph now identifies Hilbert data derivatives with
polynomial weighted estimates and expressly avoids C2 dependence in the
sharp E1/E2 envelope norms.

This addendum verifies those textual clarifications. The original mathematical
verdict and its conditional scope are unchanged: the reviewed response and
ambient obstruction arguments pass, while the unresolved existence,
nonvanishing, reachable-set, and nonlinear all-time claims remain open.

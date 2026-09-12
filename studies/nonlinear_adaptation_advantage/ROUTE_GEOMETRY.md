# Route G: constrained curvature and prediction-metric separation

Status at freeze: **partial theoretical result; E₀ unresolved**. The exact tanh
model yields a well-defined signed constrained-curvature functional. Neither its
negative sign on an ordinary task box nor a beneficial normalized component sign
has been proved. This report supplies exact identities, a uniform finite-time
comparison bound, and a remainder criterion. It does not claim nonlinear
superiority, a promotion-ready theorem, or an impossibility result.

Author: independent scoped agent `/root/geometry_route`, 2026-09-12. No other
route or study was read. The supervisor supplied only the neutral contract,
allowed established sources, process instructions, and a later permission to
read the common-action dependency III.F. No experiments or Git writes occurred.

## 1. Exact scope and an ordinary test family

The model, raw metric, actual initialized Gaussian action and adjoint, complete
first rows, actual finite Gaussian readout, anchor weights, and original-start
physical GF are exactly those in the contract and C.4.9–C.4.10. This report
analyzes their already established selected curve on the common interval
`[0,T_c]`; it does not restart an actual finite network at the fitted endpoint.
Write all predictions in angular pullback, and use the slow clock
`tau=epsilon t`. Put `r_tau=P_nu(tau)-q`, with the required residual sign.

Here is a fixed four-coefficient box on which to investigate the sign, chosen
without using a trained prediction. Fix `0<R<=1/8`, use `s=1,N=1`, and set

\[
v=a_0\cos\alpha+b_0\sin\alpha+a_1\cos3\alpha+b_1\sin3\alpha,
\quad a_0,b_0\in[R/16,R/8],\quad a_1,b_1\in[R/48,R/24]. \tag{G1}
\]

The four coefficients vary independently on intervals of positive relative
length; their weighted absolute sum is at most `R/2`. Take

\[
q=q_0+h(v+\zeta),\quad q_0=\cos^3\alpha-\sin^3\alpha,
\quad h=\sin^2(2\alpha),
\quad\|\zeta\|_\infty+\operatorname{Lip}(\zeta)\le R/2048, \tag{G2}
\]

where `zeta` is odd. The target robustness topology is this explicitly
factorized odd Lipschitz topology; all perturbations preserve the anchors.
In the usual uniform-plus-Lipschitz target norm the perturbation is at most
`3R/2048`, since `||h'||infinity<=2`. The central box has finite cap; its
robustness neighborhood need not. For densities take

\[
\int p\,d\rho=1,\qquad
\|p-1\|_\infty+\operatorname{Lip}(p)\le1/4. \tag{G3}
\]

Thus `3/4<=p<=5/4`; support is the entire circle, and density robustness is
stated in the same uniform-plus-Lipschitz norm. Labels may retain exactly
C.4.10's bounded centered noise `|xi|<=h/8`. Indeed
`||v+zeta||infinity<=R/2+R/2048<1/8`, so its label-bound argument applies.

Quantitative activity concerns actual target harmonics as well as parameters.
The unperturbed coefficients at frequencies five and seven are
`(-a_0/4,-b_0/4)` and `(-a_1/4,-b_1/4)`. Any real Fourier coefficient of
`h zeta` has magnitude at most `2||zeta||infinity<=R/1024`. Consequently
each fifth-harmonic coefficient has magnitude at least `15R/1024`, and each
seventh-harmonic coefficient at least `13R/3072`.

The family is uniformly nonstationary. Let `S alpha=pi/2-alpha`. The reference
residual `F_*-q_0` is antisymmetric under `S`. The symmetric part of `v` is

\[
A(\cos\alpha+\sin\alpha)+B(\cos3\alpha-\sin3\alpha),
\quad A=(a_0+b_0)/2\ge R/16,\quad |B|\le R/96.
\]

Both functions after multiplication by `h` have squared uniform-circle norm
`3/8`: square the sum or difference, and integrate `h^2 sin(2alpha)` or
`h^2 sin(6alpha)`, each of which vanishes by Fourier orthogonality. The triangle
inequality, followed by symmetric/antisymmetric orthogonality, gives

\[
\|r_0\|_p^2\ge e_G:=\frac34R^2
 \left(\frac5{96}\sqrt{3/8}-\frac1{2048}\right)^2>0. \tag{G4}
\]

C.4.10.3's injectivity then gives a nonzero full projected initial force.
This exclusion of stationary cases is proved on the whole box; it is not a
selection rule using trained outcomes. No favorable curvature sign is asserted
for this box, and it has not been shrunk after examining such a sign.

## 2. Exact predictor equation and a finite-time comparison

For a fixed density use the real prediction Hilbert space
`H_p=L2(p rho)` (or its closed odd subspace). Define

\[
\mathsf D_\tau a=\int a(u)d_{\theta_\nu(\tau)}(u)p(u)d\rho(u),
\qquad \mathsf K_\tau=\mathsf D_\tau^*\mathsf D_\tau. \tag{G5}
\]

All raw blocks are retained. The contract's frozen kernel operator is
`K_0`, not the initialized kernel. Scalar differentiation and actual
adjunction in C.4.10.2 give the exact equations

\[
r_\tau'=-2\mathsf K_\tau r_\tau,\qquad
r^{\rm fr}_\tau=e^{-2\tau\mathsf K_0}r_0,\qquad
E_\nu(P_\nu)'=-4\|\mathsf D_\tau r_\tau\|_{raw}^2. \tag{G6}
\]

Since `K_0` is bounded positive self-adjoint, its exponential can be defined
by the norm-convergent power series. Its derivative is `-2K_0` times itself,
and differentiation of the squared norm proves it is a contraction. This
requires no unproved spectral convergence or compactness-to-coercivity step.

Set `S(t)=exp(-2t K_0)` and

\[
I(t)=\int_0^t S(t-s)(\mathsf K_s-\mathsf K_0)r_s\,ds.
\]

Subtract (G6), differentiate its integrating factor (bounded operators
commute with their own exponential), and use the zero initial discrepancy.
This proves

\[
r_t-r_t^{\rm fr}=-2I(t),\qquad
E_\nu(F_{\rm fr}(t))-E_\nu(P_\nu(t))
=4\langle S(t)r_0,I(t)\rangle_p-4\|I(t)\|_p^2. \tag{G7}
\]

This is a finite-time identity. Its first term contains every changing-kernel
interaction and its second term has an adverse sign. A positive kernel-motion
norm alone supplies no lower bound on (G7).

There is a stronger time estimate than the raw-state square-root bound. Use
the explicit constants `L,k,A_s,T_g` of C.4.10.2, with `Y_0=1`, and put

\[
D_G=A_sT_g(1+4L/\sqrt k),\quad
\kappa_G=2LD_G,\quad B_G=2L^3+D_G. \tag{G8}
\]

The constrained controls have total variation at most `A_s`. NSC28 and the
exact projector derivative give

\[
\|\Pi'\|\le2\|GM^{-1}\|\|G'\|
 \le4T_gA_s/\sqrt k,
\quad \sup_u\|d_\tau'(u)\|\le D_G,
\quad\|\mathsf K_\tau'\|\le\kappa_G. \tag{G9}
\]

For the first inequality differentiate `Pi=I-GM^{-1}G*`, or use
`Pi'=-Pi G'(GM^{-1})*-(GM^{-1})G'^*Pi`. The anchor gap is `k/2`,
`||G'||<=sqrt(2)T_g A_s`, and `||GM^{-1}||<=sqrt(2/k)`.
Bochner integration gives the second inequality; the third follows by the
product rule for `D*D` and `||D||<=L`. The strong absolutely continuous
identities of NSC25–NSC28 justify each derivative. No ambient L2 Hessian is
assumed.

Let `R_0=||r_0||p`. Both residual norms are at most `R_0`, by (G6).
Contraction in (G7) and `||K_s-K_0||<=kappa_G s` therefore imply, for every
`0<=t<=T_c`,

\[
\|P_\nu(t)-F_{\rm fr}(t)\|_p\le\kappa_G R_0t^2,
\quad
|E_\nu(F_{\rm fr}(t))-E_\nu(P_\nu(t))|
 \le2\kappa_G R_0^2t^2. \tag{G10}
\]

This is a proved uniform finite-horizon bound, not a favorable remainder sign.

For comparison with total learning put
`lambda=||D_0 r_0||raw²/R_0²>0`. Differentiating `b_tau=D_tau r_tau`
and using (G6),(G9) gives `||b_tau'||<=B_G R_0`. If
`t<=sqrt(lambda)/(2B_G)`, then `||b_tau||>=sqrt(lambda)R_0/2` throughout
the interval. Integrating (G6) yields

\[
E_\nu(F_*)-E_\nu(P_\nu(t))\ge\lambda R_0^2t,
\qquad
\frac{|E_\nu(F_{\rm fr}(t))-E_\nu(P_\nu(t))|}
 {E_\nu(F_*)-E_\nu(P_\nu(t))}
\le\frac{2\kappa_Gt}{\lambda}. \tag{G11}
\]

On the central finite-cap box one may take the established uniform
`lambda_1` in place of `lambda`. On the full robustness family a uniform
positive `lambda_G` also exists: the closed odd Lipschitz ball for `zeta`
and the density class are compact in the uniform topology by finite-net
equicontinuity; all coefficients live in a compact box; the ratio is
continuous, its denominator is bounded below by (G4), and injectivity makes
its numerator positive at every point. This argument does not evaluate
`lambda_G`. In particular (G11) exhibits the small relative size of any
advantage proved only at a very short stop.

## 3. The signed constrained-curvature functional

Here and below all endpoint quantities use the actual trained reference.
For an admissible raw direction `z=(z_w,z_K,z_c)` with `z_w in L4` and
`z_c in Linfinity`, put

\[
a_z(u)=\phi'(w_\dagger\cdot u)(z_w\cdot u),\quad
Z_z(u)=z_KH^1(u)+A_\dagger a_z(u).
\]

The directional second derivative of the scalar prediction is

\[
\begin{aligned}
\mathcal H_u[z,z]={}&2\langle z_c,\phi'(Z^2(u))Z_z(u)\rangle
 +\langle c_\dagger,\phi''(Z^2(u))Z_z(u)^2\rangle\\
&+\langle c_\dagger,\phi'(Z^2(u))
 [2z_Ka_z(u)+A_\dagger\{\phi''(w_\dagger\cdot u)(z_w\cdot u)^2\}]
 \rangle. \tag{G12}
\end{aligned}
\]

All terms exist: `a_z` and `(z_w.u)^2` are in `L2`, `Z_z` is in `L2`,
the squared upper term is in `L1` and is paired with bounded `c_dagger`,
and `z_K` is bounded by its HS norm. Formula (G12) follows by two scalar
differentiations of the affine curve and dominated convergence. Equivalently
differentiate the raw gradient in this direction using NSC27: the only extra
row product is `z_w Q`, controlled in `L2` by their `L4` norms. Thus this is
a directional identity, not an unrestricted C2 assertion on raw L2 space.

For any bounded odd residual `r` at fixed `p`, set

\[
v_r=\int r(u)g_\dagger(u)p(u)d\rho(u),\quad
\beta_r=M_\dagger^{-1}G_\dagger^*v_r,\quad b_r=\Pi_\dagger v_r,
\]
\[
\mathcal C_p(r)=\int r(u)\mathcal H_u[b_r,b_r]p(u)d\rho(u)
       -\sum_{a=1}^2(\beta_r)_a\mathcal H_{e_a}[b_r,b_r]. \tag{G13}
\]

The direction `b_r` is admissible: it is a finite-variation integral of
gradients, whose row has all fixed moments by the source bound, and whose
readout block is pointwise bounded. Equation (G13) is a continuous cubic
functional of `r` on each bounded target space. The anchor subtraction is
essential; dropping it would compare with the wrong tangent system.

Write `H=K'_0` along the actual selected curve with initial residual `r_0`.
Then

\[
\langle r_0,Hr_0\rangle_p=-4\mathcal C_p(r_0). \tag{G14}
\]

Proof: with `v=v_r,b=Pi v`, first hold `r` fixed while differentiating
`Pi v` in direction `b`. Since `v=b+G beta` and `Pi Pi' Pi=0`,

\[
\langle b,(\partial_b\Pi)v\rangle
 =-\langle b,(\partial_bG)\beta\rangle
 =-\sum_a\beta_a\mathcal H_{e_a}[b,b].
\]

The other derivative term is `int r H_u[b,b]p`, so their sum is `C_p(r)`.
Now `theta'_0=-2b`; differentiating `||D_tau r||²` with `r` fixed gives
`2<b,partial_{-2b}(D r)>=-4C_p(r)`, which is (G14).

Consequently the first possible signed risk difference is

\[
E_\nu(F_{\rm fr}(t))-E_\nu(P_\nu(t))
       =-8\mathcal C_p(r_0)t^2+o(t^2). \tag{G15}
\]

The continuity needed for this little-o is justified in §5 below. A positive
quadratic advantage requires `C_p(r_0)<0`. No positivity property of tanh or
of the full gradient Gram establishes that inequality. In (G12), the
readout/feature cross term, both tanh curvature terms, and the anchor
subtraction have uncontrolled signs on the declared family.

## 4. Symmetry, intrinsic scalar removal, and task components

One exact symmetry constraint is useful but does not give the desired sign.
For `p=1`, let `Jr(u)=-r(Su)`, where `S` swaps coordinates. The joint
generated-program symmetry in C.4.5.1 R7 induces a raw isometry fixing the
reference state, preserving the anchor level, and intertwining predictions
with `J`. Therefore the exact definition (G13) obeys
`C_1(Jr)=C_1(r)`. If `r=r_A+r_S` is its swap-antisymmetric/symmetric split,
and `c` is the symmetric trilinear polarization of this cubic, then

\[
\mathcal C_1(r_A+r_S)
 =c(r_A,r_A,r_A)+3c(r_A,r_S,r_S). \tag{G16}
\]

Indeed `Jr_A=r_A,Jr_S=-r_S`, so the polynomial is even in `r_S`.
The pure symmetric cubic and the term linear in `r_S` vanish. Thus the
independent symmetric component used to prove (G4) supplies nonstationarity
but no sign for the mixed term in (G16). For a purely symmetric residual the
quadratic risk comparison vanishes even when the initial force is nonzero.
That is a diagnostic of the signed mechanism; targets constructed around
`F_*` are not proposed as members of E₀'s ordinary family.

Scalar kernel acceleration must be removed in prediction norm, not a raw
parameter norm. Let

\[
v=\mathsf K_0r_0\ne0,\qquad \eta=Hr_0,\qquad
\alpha=\frac{\langle v,\eta\rangle_p}{\|v\|_p^2},\qquad
\xi=\eta-\alpha v. \tag{G17}
\]

This is the orthogonal projection of the actual second-order prediction
correction off the one-dimensional scalar-speed direction. It is invariant
under orthonormal coordinate changes in prediction space and uses the same
`L2(p rho)` metric for both learners. The locally matched frozen clock
`s(t)=t+alpha t²/2` gives

\[
F_{\rm fr}(s(t))-P_\nu(t)=t^2\xi+o_{H_p}(t^2). \tag{G18}
\]

This scalar control interprets the effect. It does not change the matched-clock
base comparison, claim superiority to arbitrary acceleration, or introduce an
unbudgeted optimized frozen trajectory. The coefficient is computed at the
reference, from the task and the explicit derivatives, before its episode.

For an independently interpretable component decomposition, let `Q_L` be
orthogonal projection in `H_p` onto
`span{cos alpha,sin alpha,cos 3alpha,sin 3alpha}` and `Q_H=I-Q_L`.
This distinguishes coarse angular variation from finer variation; it is fixed
from input geometry and the common metric, independently of trained predictions.
It is not an assertion that the kernel diagonalizes Fourier modes. All
cross-mode interactions remain in `K_tau`, `eta`, and `xi`.

Normalize component improvement by `s_i²=||Q_i q||p²`, `i=L,H`. These are
target energies, not residual or trained-output normalizers. They are positive
on (G1)–(G3). For the fine component, norm equivalence and the seventh cosine
coefficient give
`s_H>=sqrt(3/8)13R/3072`. For the coarse component,
`s_L>=sqrt(3/4)sqrt(5/8)-sqrt(5/4)(R/2+R/2048)>0`, since `q_0` belongs
to the coarse space and has squared uniform norm `5/8`.

The signed relative fine-versus-coarse advantage beyond scalar speed has
leading coefficient

\[
\mathcal R_p(r_0,q)=
 \frac{2\langle Q_Hr_0,Q_H\xi\rangle_p}{s_H^2}
 -\frac{2\langle Q_Lr_0,Q_L\xi\rangle_p}{s_L^2}. \tag{G19}
\]

To check its interpretation, expand the exact component risk difference
`||Q_i(F_fr(s(t))-q)||²-||Q_i(P_nu(t)-q)||²` using (G18). It equals
`2t²<Q_i r_0,Q_i xi>+o(t²)`. Thus a positive (G19) is precisely a larger
normalized relative gain in the fine component for this interpretation.
Nonzero `xi` does not imply this sign, nor even a benefit in either component.
A complete result should give a favorable component's individual sign as well
as the relative contrast and the matched-clock total-risk sign. None is
established here for the actual tanh family.

## 5. An explicit remainder criterion; what remains unevaluated

The gradient derivative is continuous in time, uniformly in input, for every
fixed member, and uniformly over the compact family above. Here are the
regularity details rather than an assumed Taylor radius. Raw path continuity
and the source tails give `L4` query continuity by interpolation from `L2`
and a common `L8` bound. The signed control measures have continuous total
variation coefficients because predictions and the two anchor multipliers are
continuous. Their row velocities are therefore `L4`-continuous. NSC27 then
gives continuous strong `L2` derivatives of the forward and backward fields.
For the first row of the differentiated gradient, the product `w'Q` is
continuous in `L2` by the two `L4` convergences. In the upper expressions,
subtract the varying `L2` vector first and apply bounded-multiplier continuity
to its fixed limit; both `c` and `c'` have a uniform pointwise bound. The
finite anchor inverse differentiation is continuous because of its gap.
These arguments apply jointly to a convergent family/time/input sequence,
using the law continuity NSC24 and compactness. Hence `K'_tau` is operator
norm continuous, including its right endpoint derivative at zero.

Define, only for recording the exact remaining remainder problem,

\[
\Omega(t)=\sup_{\text{family}}\sup_{0\le s\le t}
                 \|\mathsf K'_s-\mathsf K'_0\|,
\qquad \Omega(t)\longrightarrow0. \tag{G20}
\]

This modulus has **not** been bounded by a numerically evaluable function of
the source and family constants. Its definition involves reached trajectories
and therefore is not an admissible substitute for the contract's evaluated
positive stopping rule. It is used here to expose, rather than conceal, that
remaining obligation.

The exact integral (G7) yields the following quantitative remainder formula:

\[
\|r_t^{\rm fr}-r_t-t^2\eta\|_p
 \le R_0t^2\{\Omega(t)+2L^2\kappa_Gt\}, \tag{G21}
\]
\[
\left|E_\nu(F_{\rm fr}(t))-E_\nu(P_\nu(t))
              +8\mathcal C_p(r_0)t^2\right|
 \le R_0^2t^2\{2\Omega(t)+8L^2\kappa_Gt+\kappa_G^2t^2\}. \tag{G22}
\]

For verification, write `K_s-K_0=sH+R_s`, `||R_s||<=s Omega(t)`, in `I(t)`.
The remainder contributes `R_0 Omega(t)t²/2`. Replacing `r_s` by `r_0`
costs `2L² kappa_G R_0 int_0^t s² ds`, because
`||r_s-r_0||<=2L²R_0s`. Replacing `S(t-s)` by identity costs
`2L² kappa_G R_0 int_0^t (t-s)s ds`. Their sum is
`L² kappa_G R_0t³`. Multiply by two to obtain (G21). In
`Delta E=2<r_fr,r_fr-r>-||r_fr-r||²`, use (G10), (G21), and
`||r_fr-r_0||<=2L²R_0t`; this gives (G22), with the stated signs.

There is also a controlled component remainder. If `|alpha|t<=1`, then
`s(t)>=0`, and the frozen equation gives

\[
\|F_{\rm fr}(s(t))-P_\nu(t)-t^2\xi\|_p
 \le R_0t^2\{\Omega(t)+2L^2\kappa_Gt+3|\alpha|L^4t\}. \tag{G23}
\]

Indeed integrate `F_fr'=-2K_0 r_fr` between `t` and `s(t)` and bound its
deviation from `-2v` by `4L^4R_0` times the intermediate time. For either
orthogonal component the absolute remainder after its leading term
`2t²<Q_i r_0,Q_i xi>` is at most

\[
R_0^2t^2\left\{2\Omega(t)+(10L^2\kappa_G+6|\alpha|L^4)t
                  +(\kappa_G+|\alpha|L^2)^2t^2\right\}. \tag{G24}
\]

Use `||xi||<=kappa_G R_0`, `||r_fr(s(t))-r_0||<=3L²R_0t`, and
`||F_fr(s(t))-P(t)||<=R_0(kappa_G+|alpha|L²)t²` in the difference of
squared norms. Divide (G24) by `s_i²`; the sum of those divided bounds
controls the relative contrast in (G19). This accounts for all finite-time
interactions if an actual bound for (G20) and actual signed margins are
provided. Also `|alpha|<=kappa_G/lambda`, by
`||K_0r_0||>=<r_0,K_0r_0>/R_0=lambda R_0`.

The known source constants are already extremely poorly conditioned; for
example C.4.5.2 contains `B_Q=225400 exp(2880)+180`. Neither that fact nor
the compactness minima evaluates a negative curvature margin. The report
does not claim a practical horizon or advantage.

## 6. Counterchecks, claim status, and the smallest open step

Two exact finite-dimensional checks guard against invalid geometric inference.
They are checks of purported general implications, not replacement networks
or counterexamples to E₀.

* Let `f(theta)=(theta,c theta²/2)`, `theta_0=0`, target `(a,b)`, and use
  Euclidean prediction metric and unhalved squared loss. Then
  `r_0=(-a,-b)`, `b_r=-a`, `C(r_0)=-a²bc`, and the actual risk difference
  begins `8a²bc t²`. Reversing `b` reverses its sign, while initial tangent
  learning remains nonzero. Curvature can help or hurt.
* For `f(theta)=(theta,c theta²/2,d theta²/2)` and target `(a,b,0)` with
  `a,b,d!=0`, one obtains `eta=(-2abc,-2a²c,-2a²d)`, `alpha=2bc`, and
  `xi=(0,-2a²c,-2a²d)`. Thus `xi!=0`; choosing `bc<0` nevertheless makes the quadratic total-risk
  advantage negative. A nonzero intrinsic shape change is not a benefit.

The first check also gives zero quadratic gain for `b=0` despite curvature.
The linear-output case `c=d=0` makes (G7) exactly zero, as it must.
Changing the residual sign reverses the cubic (G13). These checks verify the
loss factor, the factor `-8` in (G15), and the necessity of a signed argument.

| Claim | Status and boundary |
|---|---|
| Four independently active harmonic coefficients, robust full-circle class, nonstationarity | Proved by (G1)–(G4); no advantage claim |
| Exact full-projected predictor and finite-time comparison | Proved using the established selected flow, (G5)–(G11) |
| Actual constrained directional curvature identity | Proved, (G12)–(G15); no unrestricted ambient C2 theorem |
| Symmetry cancellation and scalar-speed quotient | Proved, (G16)–(G18) |
| A meaningful component contrast | Defined and derived, (G19), with finite remainder (G24) |
| Actual tanh curvature sign on the declared ordinary family | **Open** |
| Beneficial component sign beyond scalar speed | **Open** |
| Evaluated positive common stop and nonzero advantage | **Open**; (G20) is unevaluated |
| Sample and original-finite-network advantage transfer | Not claimed: no population advantage is available to transfer |

The smallest decisive first obligation for this route is to establish a
strict negative bound for the explicit endpoint cubic (G13), uniformly on a
nontrivial ordinary box such as (G1) and its declared robust neighborhood.
At `p=1`, (G16) reduces this to finitely many reference contractions of the
antisymmetric residual and the two symmetry sectors; their signs remain
unknown. It is smaller than the full finite-time theorem because it uses
only the independently specified reference and task coefficients, yet it is
not a consequence of the available positive Gram bounds. A positive cubic
at a member would defeat a sufficiently short-stop proof on that member,
not rule out a later advantage or another ordinary family.

Even success at that first step would leave the independent beneficial
component inequalities in (G19) and a computable upper bound replacing
(G20). Formulae (G22) and (G24) specify exactly what those bounds must beat.
No sampling theorem or continuation theorem repairs a missing sign.

Recommendation: freeze this route as **blocked on an actual reference sign**.
Do not extend preliminary jets into a theorem, and do not run a training
search. Reopen only with a concrete analytic mechanism or a certified
reference-tensor calculation that can determine the sign on a substantial
coefficient box. Sampling, finite frozen realizations, and width-first /
contamination-second / sample-last transfer remain separate obligations if
a population advantage is eventually proved.

## 7. Actual read scope, versions, and checks

Read completely: the neutral contract; `docs/NOTATION.md`; the two required
skills; investigate-conjectures references `research-contract.md`,
`adversarial-audit.md`, and `proof-search-orchestration.md`; and
`RESEARCH_WORKFLOW.md` (both parts were present in the complete read, although
this route does not attempt promotion). The initial combined output omitted
the end of NOTATION in its rendering; the entire notation file was reread.

Scientific source coverage in `docs/global_nonlinear.md`:

* C.4.9 completely, lines 12994–15323, including the source-control supplement;
* C.4.10 completely, lines 15324–17016/end; the truncated passage of the large
  second read was repaired by a separate read of lines 16324–16540, and its
  ending was read separately;
* A.1–A.4, lines 1840–1898, completely;
* C.4.5.1 §§1–3, lines 5475–5782, completely, plus its rational constant
  certificate §5, lines 5999–6103, completely; §4 hidden-motion estimates
  were not read or used;
* C.4.5.2 §§1–4, lines 6104–6521, completely; its later finite-GF bridge was
  not read or used as a separate input.

Also read `docs/special_data_limits.md` III.F completely, lines 3785–4326,
after the supervisor expressly expanded permitted dependency scope. The
remaining scientific contents of both files were not read. A heading/label
search of `global_nonlinear.md` was used only to locate allowed dependencies.
The routes, study README/history, and other studies were not read.

The complete C.4.9 source formulas and their supplement were used directly;
their equivalent links to C.4.6 source tails and C.4.7 recursions were not
additional scientific inputs. The needed raw clock construction, passive
source proof, adjunction, source regularization, and scalar chain rules are
contained in the actual scope above. No external scientific theorem was
retrieved or invoked by name without its needed argument here.

SHA-256 at freeze preparation:

| File | SHA-256 |
|---|---|
| `studies/nonlinear_adaptation_advantage/RESEARCH_CONTRACT.md` | `0bbd681da93a44574fbe30d9ee7fd5a984105d363c473c7756f31964c2896c0f` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/global_nonlinear.md` | `5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483` |
| `docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `/etc/codex/skills/investigate-conjectures/SKILL.md` | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| Its `references/research-contract.md` | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| Its `references/adversarial-audit.md` | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
| Its `references/proof-search-orchestration.md` | `6f288341eb90f9618ab9fa6fc8c37225f41230de6a40285761c17cc257edecdd` |

Initial metadata-only Git check: HEAD
`ec3be9b188d1b89cbbcd054fb23f567d533104a5`; index had no staged paths.
Concurrent modified/untracked paths were preserved. Actual verification here
was author algebraic reconstruction of (G7), (G14), and (G21)–(G24), symmetry
and elementary finite-dimensional counterchecks, plus complete listed source
reading. No numerical training, symbolic computation, formal proof checker,
or independent review of this report was performed. The old rational source
certificate was read, not re-executed. Therefore this is a frozen research
route report, not an independently checked or promoted addition.

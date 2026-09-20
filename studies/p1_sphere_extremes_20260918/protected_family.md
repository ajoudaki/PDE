# Independent protected-family route

Status: **complete theorem candidate, frozen after authorized comparison**,
2026-09-18. The scalar-clock lemma and cyclic initial-activity argument
were frozen before comparison. The separately frozen analytic
initialization certificate was then checked, closing the endpoint and
open-family obligations. This is an internally derived candidate, not
promoted repository theory or an independent-review verdict.

Scope: exact population-expectation d=3, p=1 closure, canonical
`w=g,c=0,M=D`, all entries of the 3-by-6 matrix trained, unit normalized
inputs, unhalved weighted square loss, physical gradient flow. Scientific
inputs read: `docs/observable_p1.md` in full and the equations/existence
parts of `docs/global_nonlinear.md` C.4.7.9.3--4 and C.4.7.10.D.3.
No other studies or experimental results were used. The research and
rigorous-mathematics skills were applied. No experiment was run by this
route. After its independent freeze, the lead author explicitly
authorized comparison with this study's separately frozen
`initialization_positivity.md`; Section 6 checks and incorporates that
analytic argument. Its separate diagnostic is not an input to this proof.

## Final theorem and exact claim scope

For the canonical d=3, p=1 population closure, there is theta_0>0 such
that the uniform three-point datasets

`u_j=P^j[cos(theta) v+sin(theta) e]`, `j=0,1,2`, `0<theta<theta_0`,

with `v=(1,1,1)/sqrt3`, `e=(2,-1,-1)/sqrt6` and all labels +1,
have linearly independent inputs and exact physical loss
`L(t)<=exp(-4 k_theta t)`. Here `k_theta` is the squared L2 norm of
the initialized averaged upper activation and has a strictly positive
lower bound independent of theta on this small-opening family.
All moving blocks remain bounded and converge to actual fitted
endpoints. Around every one of these noncollapsed triples is an open
neighborhood of independently perturbed unit inputs and positive
probability weights for which the canonical flow has bounded fitted
endpoints and `L'(t)<=-lambda L(t)` for every t>=0, hence
`L(t)<=exp(-lambda t)L(0)`, with lambda>0 uniform on a sufficiently
small chosen neighborhood. The loss itself is the current-state
potential, including the finite entrance interval.

The same statements hold for labels `(+,+,-)` after negating the third
input. Equal reference weights are 1/3, so this signed version has label
masses 2/3 and 1/3. A balanced-label constraint is not asserted. Every
entry of the full 3-by-6 M follows its original trained equation.
The theorem uses only actual signed-coordinate/permutation symmetries
of the canonical dictionary; it asserts no rotation invariance.

The symmetric reference rate stays bounded away from zero as the
geometric triple becomes arbitrarily nearly dependent. The guaranteed
rate and neighborhood for arbitrary independent perturbations may
shrink as theta decreases to zero. Consequently the result excludes
stalling and supplies exponential fitting on an open family, but does
not assert a uniform transverse rate over all nearly dependent triples,
all labels, balanced weights, all sphere data, finite quadrature rules,
or finite neural networks.

## 1. Exact scalar-residual protection lemma

Let a finite dataset with equal target +1 have a symmetry preserved by
the initialized dictionary, the canonical state and the complete vector
field, with that symmetry transitive on its equally weighted inputs.
Write

\[
 F(\theta)=\frac1m\sum_j f_\theta(u_j),\qquad
 \bar h_\theta=\frac1m\sum_j h_{2,\theta}(u_j),\qquad
 k=\|\bar h_{\theta_0}\|_{L^2(\lambda_2)}^2.
\]

Assume only the **initialized** quantity `k>0`. The gradient metric is
population L2 in w,c and Frobenius in the full M. Symmetry and uniqueness
give `f(u_j)=F` at every reached state. Consequently the exact physical
equation is

\[
 \dot\theta=2(1-F)\nabla F.
\]

Consider instead the autonomous ascent clock

\[
 \frac{d\theta}{ds}=\nabla F,\qquad\theta(0)=\theta_0.
 \tag{1}
\]

This changes only the common scalar speed and retains all three moving
blocks and every entry of M. In this clock,

\[
 F_s=\|\nabla F\|^2\ge\|\bar h\|_2^2,\quad
 c_s=\bar h,\quad F=\langle c,\bar h\rangle.
 \tag{2}
\]

Put `C=||c||_2^2`. Then `C_s=2F`. At zero,
`c(s)=s bar h_0+o(s)` and `F(s)=ks+o(s)`, whence
`C(s)=ks^2+o(s^2)`. Since `F_s>=0` and `k>0`, both F and C are
strictly positive for s>0. Cauchy--Schwarz gives `F_s>=F^2/C` and

\[
 \left(\frac{F^2}{C}\right)_s
 =\frac{2F}{C^2}(CF_s-F^2)\ge0,
 \qquad \lim_{s\downarrow0}\frac{F(s)^2}{C(s)}=k.
 \tag{3}
\]

Thus, throughout the ascent trajectory,

\[
 F_s\ge F^2/C\ge k,
 \qquad F(s)\ge ks.
 \tag{4}
\]

These are current-state identities and inequalities. In particular they
do not assume a future Gram lower bound, frozen hidden features, a
fixed M, or a restricted diagonal/rank ansatz for M.

For completeness the clock solution exists on every finite s interval.
Let `L_l=ess sup |b_l|`, `A=L_1 L_2`, and `D_0=||D||_F`. The exact
equations and bounded gates imply

\[
 \|c(s)\|_\infty\le s,\quad
 \|M(s)\|_F\le D_0+As^2/2,\quad
 \|w(s)-g\|_\infty
 \le AD_0s^2/2+A^2s^4/8.
 \tag{5}
\]

Indeed `|a_j|<=L_1`, `|d_j|<=L_2s`, so
`||M_s||_F<=As`; and `|q_j|<=A s ||M||_F`, so
`||w_s||_infty<=A s(D_0+As^2/2)`. The bounded feature/gate local
Lipschitz argument of the permitted existence source applies in
`L-infinity(w-g) x L-infinity(c) x R^(3x6)`. The bounds prevent escape;
bounded speeds give a Cauchy endpoint at every finite proposed maximal
time, after which the local contraction argument continues the solution.

There is therefore a unique `s_*` with

\[
 F(s_*)=1,\qquad 0<s_*\le1/k.
 \tag{6}
\]

The physical clock solves `ds/dt=2(1-F(s))`, `s(0)=0`. It remains
below s_* at every finite t, by scalar uniqueness at the equilibrium
s_*, and tends to s_*: a limiting value below s_* would leave a
strictly positive clock speed. The exact physical loss is
`L=(1-F)^2`, and hence

\[
 \dot L=-4F_sL\le-4kL,
 \qquad L(t)\le e^{-4kt}.
 \tag{7}
\]

The state converges in the stated supremum/Frobenius norms to the actual
bounded endpoint `theta(s_*)`; this follows from clock convergence and
finite-clock continuity, not from an assumed limit of feature Grams.
The endpoint is regular in the scalar fitted direction, since
`||grad F(theta(s_*))||^2>=k`. Equation (5) at `s=1/k` supplies
explicit all-time state bounds.

This proves exponential fitting and excludes positive-loss stalling
for this exact symmetry class. It does not yet give a full-rank
three-residual endpoint Jacobian or stability under symmetry-breaking
input perturbations.

## 2. Genuine cyclic triples arbitrarily close to the diagonal

Let `P` cyclically permute the three coordinates, and define

\[
 v=(1,1,1)/\sqrt3,\quad e=(2,-1,-1)/\sqrt6,\quad
 u_\vartheta=\cos\vartheta\,v+\sin\vartheta\,e,\quad
 u_j=P^ju_\vartheta\quad(j=0,1,2).
 \tag{8}
\]

Each input is a unit vector. Their Gram eigenvalues are
`3 cos^2 vartheta` once and `(3/2) sin^2 vartheta` twice. They are
therefore linearly independent for `0<vartheta<pi/2`, while collapsing
to v as vartheta decreases to zero.

The canonical lower marks transform by `diag(P,P)`, upper marks by P,
and g by P. Their exact laws are invariant and
`P D = D diag(P,P)`. These identities follow directly from the
coordinate-independent exact coefficients in the permitted p=1 source.
They make the complete equations equivariant under P, including the
full M equation and its actual transpose. Uniform weights and common
labels therefore supply exactly the transitive symmetry in Section 1.

Initial activity holds for every sufficiently small nonzero opening;
the following argument avoids assuming that it holds at the collapsed
diagonal itself. Write the source's scalar normalization constants as
`a,b,c_0` (the last symbol avoids confusion with the moving readout) and
the two positive bands of D as `d_h,d_k`. Define, for `-1<r<1`,

\[
 A_h(r)=E[\tanh G\,\tanh(rG+\sqrt{1-r^2}V)],
\]
\[
 A_k(r)=E[\tanh(\alpha\tanh G+\sqrt\tau Z)
                  \tanh(rG+\sqrt{1-r^2}V)],
\]
\[
 T(r)=\frac{d_h}{a}A_h(r)
 +\frac{d_k}{b}\left(A_k(r)-\frac\beta{v_0+\eta}A_h(r)\right),
 \tag{9}
\]

where G,Z,V are independent standard Gaussians and `v_0=E tanh^2 G`
is the coefficient called v in the source. For a unit input u, independence
of the other Gaussian coordinates gives

\[
 D a_0(u)=(T(u_1),T(u_2),T(u_3))^T.
 \tag{10}
\]

The functions in (9) are real analytic on (-1,1). One direct
verification expands each bounded function of G in the orthonormal
Gaussian Hermite basis: correlation at r is the sum
`sum_{n>=0} a_n b_n r^n`. Cauchy--Schwarz makes this power series
absolutely convergent on every disk `|r|<1`. For A_k first take
conditional expectation over Z. The Gaussian correlation identity for
Hermite polynomials follows by comparing coefficients in
`E exp(tG-t^2/2) exp(sY-s^2/2)=exp(rts)`.

T is not identically zero. By dominated convergence at r=1,

\[
 T(1)=d_h\frac{v_0}{a}
       +d_k\frac{\beta\eta}{b(v_0+\eta)}>0.
 \tag{11}
\]

Here `beta>0`: conditional on `h=tanh G`, the mean of
`tanh(alpha h+sqrt(tau) Z)` is an odd strictly increasing function
of h, so its product with h is strictly positive off h=0.
All the other constants in (11) are positive by the source formulas.
A nonzero analytic function has isolated zeros: otherwise its first
nonvanishing Taylor coefficient at an accumulation point could not
exist, making every coefficient zero and then the function identically
zero on the connected interval by overlapping Taylor disks.

Choose a neighborhood of `r_*=1/sqrt3` with no zero of T except
possibly r_* itself. For all sufficiently small nonzero vartheta,
the coordinates of u_vartheta lie in that neighborhood and are not
all equal r_*. Thus `z=D a_0(u_vartheta) !=0`.

The initialized upper averaged feature is

\[
 \bar h_0(B)=\tfrac13\sum_{j=0}^2\tanh(B^TP^jz),
 \qquad B=b_2.
 \tag{12}
\]

It cannot vanish identically when z is nonzero. If the coordinates
of z have nonzero sum, its linear Taylor term at B=0 is nonzero.
If they sum to zero, put `l_j(B)=B^T P^j z`; then
`l_0+l_1+l_2=0` and `sum l_j^3=3 l_0 l_1 l_2`.
Every l_j is a nonzero linear polynomial, so their product is nonzero.
The cubic Taylor term of (12) is therefore nonzero. The law of B has
a strictly positive density on an open box containing zero, since
its coordinates are independent scaled tanh transforms of nondegenerate
Gaussians. Continuity now yields `k=E bar h_0(B)^2>0`.

Consequently every sufficiently small nonzero opening in (8) obeys
the full conclusion (7), with its data-only constant k. This is a
theorem about linearly independent triples, not duplicate inputs.
It is also valid for signed-folded labels `(+,+,-)` on
`(u_0,u_1,-u_2)`: bias-free oddness gives `f(-u)=-f(u)` at every
state, so flipping an input and its label leaves its square loss and
the complete gradient vector field unchanged.

At this route's initial freeze the argument had not established
`T(1/sqrt3)!=0`, so uniformity at collapse remained open. The analytic
certificate checked in Section 6 now proves this nonvanishing.
Continuity of (12) therefore gives a strictly positive uniform lower
bound for k for all sufficiently small openings, including the
collapsed reference. The earlier isolated-zero argument remains a
logically independent proof of activity for genuine nearby triples.

## 3. Endpoint extension: open obligation at the freeze

For three linearly independent inputs, the complete prediction Jacobian
has full row rank whenever each lower reverse field q_j is nonzero
in L2. Indeed a relation among its lower-row components is

\[
 \sum_j\xi_j q_j\operatorname{sech}^2(w\cdot u_j)u_j=0
 \quad\text{almost surely}.
\]

Input independence forces each scalar coefficient to vanish almost
surely; the gates are strictly positive at finite w, so nonzero q_j
forces xi_j=0. This verifies full row rank without relying on the
readout-feature Gram. At the initial freeze the missing obligation was
nonzero q_j at the actual endpoints followed by trapping/entrance for
independently perturbed triples. Sections 4--6 now close those obligations.

## 4. Conditional open-family bridge (proved separately after the freeze)

The following bridge is complete, conditional only on the expressly
named endpoint rank premise. Let a reference three-input canonical
trajectory have a bounded fitted endpoint theta_* and converge to it
in the Hilbert state norm

\[
 \|(\delta w,\delta c,\delta M)\|_X^2
 =\|\delta w\|_2^2+\|\delta c\|_2^2+\|\delta M\|_F^2.
\]

Suppose its prediction derivative `J_*:X -> R^3` has full row rank.
Then an open neighborhood of its input triple and positive weights,
with the same prescribed labels, has canonical trajectories that remain
bounded and fit exponentially. Input perturbations are independent;
no symmetry is required of the perturbed data.

Here are the regularity and entrance details. Use the weighted residual
`e_j=sqrt(mu_j)(f(u_j)-y_j)`, weighted derivative
`A=sqrt(diag(mu)) J`, and loss `L=|e|^2`. On a bounded X ball, bounded
dictionary features make `a(u)` a continuously differentiable finite
vector map with locally Lipschitz derivative. For example, subtraction
of its derivative gives

\[
 \left|E[b_1(\operatorname{sech}^2(w\cdot u)
       -\operatorname{sech}^2(\widetilde w\cdot u))
                    (\delta w\cdot u)]\right|
 \le 2L_1\|w-\widetilde w\|_2\|\delta w\|_2.
\]

Forward upper preactivation differences are bounded pointwise by a
constant times `||w-w_tilde||_2+||M-M_tilde||_F`. Therefore every
prediction gradient block is locally Lipschitz in X, including the
readout factor in d, by Cauchy--Schwarz and the bounded upper gate.
In the lower gradient `q gate u`, q is uniformly bounded by
`L_1||M|| L_2||c||_2`; this gives its L2 difference bound without an
L-infinity hypothesis on c. Input differences are controlled by
`||(u-u_tilde) dot w||_2 <= |u-u_tilde| ||w||_2` plus the explicit
u factor in the lower gradient. Thus J, A and the exact vector field
are locally Lipschitz jointly in state and the finite data parameters.

This also supplies local Hilbert-space existence and finite-horizon
continuous dependence by the elementary integral contraction and
Gronwall estimate. The existing canonical characteristic solutions
are those solutions by uniqueness. Neither boundedness of g nor
input continuity in a supremum norm has been used.

Full row rank gives `A_* A_*^T >= 2 kappa I` for some kappa>0.
By the proved continuity, choose a state radius delta>0 and a data
neighborhood such that

\[
 AA^T\ge\kappa I,\qquad \|A\|\le B
 \tag{13}
\]

throughout that state ball and data neighborhood. The exact equations
within this neighborhood give

\[
 \dot L=-4e^TAA^Te\le-4\kappa L,
 \qquad\|\dot\theta\|_X\le2B\sqrt L.
 \tag{14}
\]

Choose a finite reference time T with
`||theta_ref(T)-theta_*||_X<delta/4` and
`(B/kappa) sqrt(L_ref(T))<delta/8`.
Such a T exists by fitted endpoint convergence. Shrink the data
neighborhood using finite-horizon continuous dependence so that all
perturbed trajectories satisfy

\[
 \|\theta(T)-\theta_*\|_X<\delta/2,
 \qquad (B/\kappa)\sqrt{L(T)}<\delta/4.
 \tag{15}
\]

Until a possible exit from the radius-delta ball, (14) integrates to

\[
 L(t)\le L(T)e^{-4\kappa(t-T)},\qquad
 \int_T^t\|\dot\theta(s)\|_Xds
 \le (B/\kappa)\sqrt{L(T)}<\delta/4.
 \tag{16}
\]

An exit would require at least delta/2 movement from the time-T
point, contradicting (16). The trajectory consequently stays in the
ball for all time and has an actual Cauchy endpoint in X. Loss tends
to zero there. This establishes the needed entrance and invariant
neighborhood rather than assuming a future Gram bound.

The complete characteristic state is bounded also in the stronger
`||w-g||_infinity, ||c||_infinity, ||M||_F` norms. The finite prefix
has the source's finite-time bounds. On the tail, X-bounded M,c and
bounded features give
`||w_dot||_infinity+||c_dot||_infinity+||M_dot||_F <= C sqrt(L)`.
Equation (16) makes the right side integrable, so all these norms
remain bounded and the moving coordinates have endpoints in these
norms as well.

For the scalar-clock reference used here, the potential estimate can
also be made differential from time zero, with no prefactor. On its
finite prefix [0,T], write `r_ref=1-F_ref`. The physical scalar clock
has `r_ref(t)>0` at finite times, and Section 1 gives
`||grad F_ref||^2>=k_ref>0`. Thus

\[
 \|A_{\rm ref}^T e_{\rm ref}\|_X
 =r_{\rm ref}\|\nabla F_{\rm ref}\|_X
 \ge r_{\rm ref}(T)\sqrt{k_{\rm ref}}=:2m>0.
\]

Shrink the data neighborhood once more using joint finite-horizon
continuity. Then `||A^T e||_X>=m` for every perturbed trajectory on
[0,T]. The initial loss is exactly one because the labels have
absolute value one, the weights sum to one and the canonical readout
is zero. Energy monotonicity gives `L<=1`, so on this prefix

\[
 \dot L=-4\|A^Te\|_X^2\le-4m^2\le-4m^2L.
\]

Together with (14), this proves for all t>=0

\[
 \dot L\le-\lambda L,\qquad L(t)\le e^{-\lambda t}L(0),
 \quad\lambda=\min(4m^2,4\kappa)>0.
 \tag{16a}
\]

The loss itself is therefore the current-state potential throughout
the reached trajectory, including the finite entrance interval.

The bridge by itself does not establish its endpoint rank premise.
Sections 5--6 now verify that premise for the sufficiently small
nonzero cyclic openings in Section 2.

## 5. Reduction of the endpoint obligation to one initialized number

This section was derived independently conditional on exactly
`T(1/sqrt3)!=0`. Section 6 now verifies that premise using the
separately frozen analytic initialization certificate.

For the collapsed single input v, use full coordinate permutation
symmetry. It gives `a=(a_h 1,a_k 1)`, `M a=rho v`, and `d=delta v`.
Set `B=b_2 dot v`. The ascent readout equation is
`c_s=tanh(rho B)`. Initially `rho_0=sqrt3 T(1/sqrt3)`, which is
nonzero by the expressly stated premise. Reverse B if necessary, so
the proof can take rho_0>0. As long as rho stays positive, c has the
strict sign of B at all s>0. Consequently

\[
 \delta=E[Bc\operatorname{sech}^2(\rho B)]>0
 \quad(s>0).
 \tag{17}
\]

Differentiate the lower contraction in the ascent clock. Since the
input v is unit,

\[
 a_s=S M^Td,\qquad
 S=E[b_1b_1^T\operatorname{sech}^4(w\cdot v)]\succeq0.
\]

Together with `M_s=d a^T`, this gives

\[
 \rho_s=\delta\{\|a\|^2+v^TMSM^Tv\}\ge0.
 \tag{18}
\]

The argument closes by continuity: rho cannot first reach zero from
its positive initial value, because it is nondecreasing on the entire
interval before such a putative first time. Thus (17)--(18) hold all
the way to the bounded fitted endpoint from Section 1.

At that endpoint delta is strictly positive. Also `M^T v !=0`, since
otherwise `rho=v^TMa=0`. The lower feature covariance is positive
definite: different coordinate pairs are independent and centered,
and in each pair h has positive variance while k has strictly positive
conditional variance given h, from its independent nondegenerate
Gaussian reverse noise. Hence `vs-beta^2>0`, and the invertible ridge
normalization preserves positive definiteness. It follows that

\[
 q_*=\delta b_1^T M^T v\ne0\quad\hbox{in }L^2.
 \tag{19}
\]

Now let the exact symmetric triples (8) approach the collapsed input.
Section 4's Hilbert Lipschitz estimates also apply to the ascent clock
on any fixed bounded s interval. The polynomial bounds (5) give a
common existence ball there. Thus these ascent trajectories converge
uniformly in X to the collapsed trajectory on that interval. Their
initialized k values converge to the strictly positive collapsed k,
so for all sufficiently small openings `k>=k_collapsed/2`.
Their fitting times lie in a common finite interval by (6), and are
continuous in the opening: uniform convergence of F, strict monotonicity
and the common lower derivative bound force convergence of its unique
level-one crossing. Therefore their actual fitted endpoints converge
to the collapsed fitted endpoint.

Each endpoint reverse field q_j depends continuously on the state and
its input, by the already-proved contractions. Equation (19) therefore
persists for all three inputs at every sufficiently small nonzero
opening. Their input independence, proved in Section 2, gives full
prediction-Jacobian row rank by Section 3. Section 4 then supplies a
genuine open family of independently perturbed three-input and
positive-weight datasets around each such reference triple, with
exponential loss decay and bounded fitted endpoints.

Under the single initialization premise, the scalar exponential rate
is uniform for the symmetric triples as their opening tends to zero.
The independently perturbed neighborhoods and their guaranteed rates
may shrink with that opening, because full three-residual rank
degenerates at the coincident limit. No uniform transverse rate is
claimed.

## 6. Analytic initialization certificate checked after comparison

The lead author's independently frozen `initialization_positivity.md`
was authorized for comparison only after the preceding route was
frozen. Its key inequality is reproduced and checked here so that the
final theorem does not hide an initialization premise.

Use the exact source coefficients `nu=E tanh^2 G`, tau, alpha, beta,
gamma, eta=1/4096 and a,b,c_0,d_h,d_k. Let

\[
 K(h)=E_Z\tanh(\sqrt\tau Z+\alpha h),\quad
 \Psi(h)=\frac{d_h}{a}h+\frac{d_k}{b}
             \left(K(h)-\frac\beta{\nu+\eta}h\right).
\]

This is the conditional initialized row of D b_1 given G, with
`h=tanh G`. It is odd. Since `0<K'(h)<=alpha`,
`0<beta<=alpha nu`. Gaussian integration by parts in Z, followed
by Cauchy--Schwarz applied to
`Z [tanh(sqrt(tau)Z+alpha h)-(beta/nu)h]`, gives

\[
 b^2\ge\tau\gamma^2+\eta,\qquad
 0<B:=c_0d_k/b
 =\frac{\alpha\beta\eta/(\nu+\eta)+\tau\gamma}{b^2}
 \le1/\gamma.
 \tag{20}
\]

The last numerator is at most `eta/gamma+tau gamma`, since
`alpha beta/(nu+eta)<=alpha^2<=1<=1/gamma`. Also
`sech^2 z>=1-z^2` gives, by integrating K' from zero to h,

\[
 K(h)/h\ge\alpha^2(1-\alpha/3)=:m_0<\alpha
 \quad(0<h\le1).
\]

Because `m_0-alpha<0`, using the upper bound in (20) has the required
inequality direction and yields

\[
 \frac{c_0\Psi(h)}h
 \ge\frac\alpha\gamma
 \left[\frac{\gamma\nu}{\nu+\eta}-1+\alpha-\frac{\alpha^2}3\right].
 \tag{21}
\]

The following purely analytic bounds make the bracket positive.
Integrating `tanh z<=z` gives `log cosh z<=z^2/2`, hence

\[
 \nu\le1-1/\sqrt3<3/7,\qquad
 \alpha\ge(1+2\nu)^{-1/2}\ge\sqrt{7/13}>11/15.
\]

Also `nu>1/64`: the event `1/2<=|G|<=1` has probability greater
than 1/5, and `tanh(1/2)>=1/2-(1/2)^3/3=11/24`, whose square
is greater than 1/5. Thus `nu>1/25>1/64` and
`eta/(nu+eta)<1/65`. Finally `|tanh z|<=|z|` implies
`gamma>=alpha-alpha^2 nu`. Since gamma<=1, the bracket in (21)
is at least

\[
 2\alpha-1-\alpha^2(\nu+1/3)-1/65
 \ge\frac7{15}-\frac{1936}{4725}-\frac1{65}
 =\frac{2552}{61425}>0.
 \tag{22}
\]

For the second inequality, its left expression increases with alpha
on `[11/15,1]` when nu<=3/7, since its alpha derivative is at least
`2-2(3/7+1/3)>0`; it decreases with nu. Therefore substitution of
alpha=11/15 and nu=3/7 has the stated direction. The actual ridge
eta is included in every bound.

Equations (21)--(22) prove that Psi(h) has the strict sign of h.
The function T of Section 2 is exactly

\[
 T(r)=E[\Psi(\tanh G)
       \tanh(rG+\sqrt{1-r^2}V)].
\]

For r>0, conditioning the second factor on G gives an odd strictly
increasing function of G, with the strict sign of G. Its product
with Psi(tanh G) is therefore positive almost surely off G=0,
so `T(r)>0`. In particular `T(1/sqrt3)>0`, exactly the premise
required by Section 5.

This completes the unconditional endpoint-rank proof, the finite
entrance argument, and the open independent-perturbation theorem
stated at the beginning. No numerical diagnostic, quadrature value,
future feature-Gram assumption or external study result is needed.

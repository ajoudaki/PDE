# Stability of paired moments under different residual clocks

28 September 2026. Scoped continuation of the direct closure-width route.
Inputs: `DIRECT_CLOSURE_WIDTH_ROUTE.md`,
`ACTIVATION_NEAR_QUADRATIC_ALLTIME.md`,
`ACTIVATION_QUADRATIC_DETERMINISTIC.md`, and the same-study direct
predictor resolvent. No other study, external source, experiment,
additional agent, maintained manuscript edit, or Git mutation was used.

**Result.** The reconstructed learned matrix has a clock-mismatch bound
with coefficient independent of `q`, under exactly the forward
clock-Lipschitz and backward RMS bounds already available for the actual
closure. The backward history need only be bounded and measurable. The
comparison uses the two actual clocks and the actual raw backward
measures; it introduces no shared oracle clock and no bounded ratio of
the residuals. The proof differentiates the *paired projection* under
insertion of clock length, rather than estimating the moment transport
matrix norm. Sections 1--5 first prove a subpower bound; Section 6 proves
the elementary uniform-BV improvement and replaces every logarithmic
factor in (5) by a constant. Section 7 gives the separate damped residual
`L1` resolvent in terms of the total variation of the predictor source.

This is a reconstruction/stability lemma. It does not by itself establish
the quantitative Gaussian width theorem or close every feedback term in
the full closure comparison.

## 1. Statement in Hilbert spaces

Let `E,F` be real Hilbert spaces. The rank-one operator `b tensor h`
maps `v in F` to `b <h,v>_F` and has Hilbert--Schmidt norm
`||b||_E ||h||_F`. Fix a finite physical endpoint `T`.

For `j=0,1`, assume:

* `rho_j:[0,T]->[0,infinity)` is measurable with
  `integral rho_j<=S`;
* `h_j:[0,T]->F` is absolutely continuous,
  `sup_t ||h_j(t)||<=H`, and
  `||dot h_j(t)||<=L rho_j(t)` almost everywhere;
* `R_j:[0,T]->E` is strongly measurable with
  `||R_j(t)||<=B rho_j(t)` almost everywhere.

Define the actual clocks and their endpoints by

\[
 \tau_j(t)=1+\int_0^t\rho_j(u)\,du,
 \qquad A_j=\tau_j(T)\le A_*:=1+S.
 \tag{1}
\]

The forward clock history is constant `h_j(0)` on `[0,1]` and equals
`h_j(t)` at clock position `tau_j(t)`. Denote it by `f_j(s)`. It is
`L`-Lipschitz on `[0,A_j]`. Indeed, the physical derivative bound gives
`||h_j(t)-h_j(u)||<=L|tau_j(t)-tau_j(u)|`. Thus flat clock intervals
cause no ambiguity.

Let the backward clock history `b_j` have zero prefix and satisfy

\[
 b_j(\tau_j(t))\rho_j(t)=R_j(t)
 \tag{2}
\]

in the change-of-variable sense. It has norm at most `B` almost
everywhere. One can define it as the Radon--Nikodym density of the
pushforward of `R_j(t)dt` with respect to Lebesgue clock measure.
The bound on `R_j` guarantees this density and its bound; no division
is made on a zero-density physical interval.

Let `Pi_q^A` be the orthogonal projection onto polynomials of degree
less than `q` in `L2(0,A)`, with Hilbert-valued coefficients. The paired
moment operator is

\[
 M_q[\rho_j,h_j,R_j]
 =\int_0^{A_j}(\Pi_q^{A_j}b_j)(s)
               \otimes(\Pi_q^{A_j}f_j)(s)\,ds.
 \tag{3}
\]

Put

\[
 \Delta_\rho=\int_0^T|\rho_1-\rho_0|\,dt,
 \qquad \Delta_R=\int_0^T\|R_1-R_0\|_E\,dt,
\]
\[
 E_h^2=\|h_1(0)-h_0(0)\|_F^2
 +\max_{j=0,1}\int_0^T\rho_j(t)
                         \|h_1(t)-h_0(t)\|_F^2\,dt.
 \tag{4}
\]

There is an absolute constant `C`, independent of `q,T` and both
Hilbert-space dimensions, such that

\[
 \|M_q[\rho_1,h_1,R_1]-M_q[\rho_0,h_0,R_0]\|_{\rm HS}
 \le B\sqrt S\,E_h
 +[H+C A_*L\sqrt{\log(e+q)}]\Delta_R
 +C A_*BL\sqrt{\log(e+q)}\Delta_\rho.
 \tag{5}
\]

If `S=0`, both raw backward measures vanish and both paired operators
are zero. The assertion includes `q=1`. No derivative of either backward
history is required.

## 2. Three elementary Legendre estimates

Write

\[
 e_k^A(s)=\sqrt{\frac{2k+1}{A}}P_k(2s/A-1),
 \qquad p_f=\Pi_q^A f,
 \qquad p_b=\Pi_q^A b.
 \tag{6}
\]

Suppose `f:[0,A]->F` is `L`-Lipschitz, `||f||infinity<=H`, and
`||b||infinity<=B`. Then

\[
 \|f(A)-p_f(A)\|\le\frac{C AL}{\sqrt q},
 \qquad
 \|p_b(A)\|\le C B\sqrt{q\log(e+q)},
 \tag{7}
\]
\[
 \int_0^A\|p_f'(s)\|\,ds
       \le C AL\sqrt{\log(e+q)},
 \qquad
 \|p_f\|_\infty\le H+C AL\sqrt{\log(e+q)}.
 \tag{8}
\]

Here and below all vector norms are the relevant Hilbert norms.

To prove the first estimate in (7), let
`K_q(A,s)=sum_{k<q} e_k^A(A)e_k^A(s)`. The elementary Legendre
antiderivative identity telescopes to

\[
 F_q(s):=\int_0^sK_q(A,u)\,du
  =\frac12\{P_q(2s/A-1)+P_{q-1}(2s/A-1)\}.
 \tag{9}
\]

It holds also for `q=1`. Since `F_q(0)=0`, `F_q(A)=1`, integration
by parts gives
`p_f(A)-f(A)=-integral_0^A F_q(s)f'(s)ds`.
Orthogonality yields

\[
 \int_0^A|F_q(s)|^2ds
 =\frac A4\left(\frac1{2q+1}+\frac1{2q-1}\right)
 \le\frac{CA}{q}.
 \tag{10}
\]

Cauchy--Schwarz gives `||F_q||L1<=CA/sqrt(q)` and proves the first
bound.

For the second bound, (9) gives

\[
 \int_0^A|K_q(A,s)|ds
 \le\frac12\int_{-1}^1
             (|P_q'(x)|+|P_{q-1}'(x)|)\,dx.
 \tag{11}
\]

The Legendre differential equation and orthogonality give

\[
 \int_{-1}^1(1-x^2)|P_k'(x)|^2dx
     =\frac{2k(k+1)}{2k+1}\le Ck.
 \tag{12}
\]

Also `|P_k(x)|<=1` on `[-1,1]` and the telescoping derivative
identity
`P_k'=sum_{j<k, k-j odd}(2j+1)P_j` give
`||P_k'||infinity<=k(k+1)/2`.
Split the integral of `|P_k'|` into endpoint intervals of length
`1/[4(k+1)^3]` and their complement. The endpoint contribution is
bounded by a constant. On the complement, Cauchy--Schwarz with weight
`1-x^2` and (12) bounds the integral by
`C sqrt(k log(e+k))`. This proves the second estimate in (7) by
(11) and the bound on `b`.

For (8), the same weighted derivative orthogonality used for the
Legendre approximation theorem gives

\[
 \int_0^A s(A-s)\|p_f'(s)\|^2ds
 \le\int_0^A s(A-s)\|f'(s)\|^2ds
 \le L^2A^3/6.
 \tag{13}
\]

It remains to control the two endpoints without using an unweighted
derivative norm. Subtract the constant `f(0)` before expanding in
Legendre modes. Its remaining coefficient vector has squared norm at
most `L^2 A^3/3`. The preceding derivative bound for `P_k` gives

\[
 \sup_{0\le s\le A}\|(p_f)'(s)\|
 \le\left(\sum_{k<q}\|\langle f-f(0),e_k^A\rangle\|^2\right)^{1/2}
      \left(\sum_{k<q}\|(e_k^A)'\|_\infty^2\right)^{1/2}
 \le C Lq^3.
 \tag{14}
\]

For `q>=2`, use endpoint intervals of length `A/(4q^3)` in (14).
Their total contribution to the derivative `L1` norm is at most `CAL`.
On the complement, (13) and
`integral ds/[s(A-s)]<=C log(e+q)/A` give the first inequality in
(8). For `q=1` the derivative vanishes. Finally use the endpoint
estimate in (7) and integrate `p_f'` from `A` to any current point
to obtain the supremum estimate in (8).

The calculation is Hilbert-valued: all integrations by parts are valid
for absolutely continuous Hilbert-valued functions, and coefficient
Cauchy--Schwarz or orthonormal coordinate approximation gives the
displayed estimates. The logarithmic loss is sufficient here; no claim
of sharpness is made.

## 3. Exact derivative under insertion of clock length

Fix one physical history triple and a terminal clock endpoint `A`.
Keep its physical forward values and raw backward measure fixed. Insert
an infinitesimal amount of forward clock length at a physical time with
clock coordinate `a in [1,A]`. Equivalently, existing later clock
positions move to the right by the inserted amount, the endpoint `A`
moves by the same amount, and the inserted forward value is `f(a)`.
There is zero new raw backward mass.

The derivative of the paired projection (3) under this insertion is

\[
 J_q(a)=p_b(A)\otimes[f(A)-p_f(A)]
       +\int_a^A\{b(s)\otimes p_f'(s)
                         -p_b(s)\otimes f'(s)\}\,ds.
 \tag{15}
\]

Here is an algebraic derivation that does not differentiate `b`.
Let `B_k=integral b e_k^A`, `H_k=integral f e_k^A`. Then
`M_q=sum_k B_k tensor H_k`. Differentiating basis orthonormality on
the moving interval gives

\[
 \langle\partial_Ae_i^A,e_j^A\rangle
 +\langle e_i^A,\partial_Ae_j^A\rangle
 =-e_i^A(A)e_j^A(A).
 \tag{16}
\]

The basis derivatives have degree less than `q`, so their contributions
to the paired moment derivative are exactly
`-p_b(A) tensor p_f(A)`. Motion of the later clock positions and the
inserted forward mass contribute

\[
 p_b(a)\otimes f(a)
 +\int_a^A\{b(s)\otimes p_f'(s)+p_b'(s)\otimes f(s)\}\,ds.
 \tag{17}
\]

Integrate only `p_b' tensor f` by parts. Its lower boundary cancels
the insertion term and its upper boundary combines with (16). The
result is (15). The argument only uses the derivative of the polynomial
`p_b`; it requires no derivative or continuity of the actual `b`.

The estimates (7)--(8), projection contraction, and Cauchy--Schwarz give

\[
 \|J_q(a)\|_{\rm HS}
 \le\|p_b(A)\|\,\|f(A)-p_f(A)\|
       +B\int_0^A\|p_f'\|
       +L\sqrt A\,\|p_b\|_{L^2(0,A)}
 \le C ABL\sqrt{\log(e+q)}.
 \tag{18}
\]

This bound is uniform in the insertion position. It also applies to a
signed infinitesimal change of clock density by linearity of the
derivative.

## 4. Interpolation of the two actual histories

For `lambda in [0,1]`, interpolate in physical time:

\[
 \rho_\lambda=(1-\lambda)\rho_0+\lambda\rho_1,
 \quad h_\lambda=(1-\lambda)h_0+\lambda h_1,
 \quad R_\lambda=(1-\lambda)R_0+\lambda R_1.
 \tag{19}
\]

These are proof-only comparison histories. Their endpoints are the two
actual systems, and their clocks are computed from their own densities.
The inequalities

\[
 \|\dot h_\lambda\|\le L\rho_\lambda,
 \qquad \|R_\lambda\|\le B\rho_\lambda,
 \qquad \|h_\lambda\|\le H
 \tag{20}
\]

hold by convexity, with the same constants. Thus every interpolated
forward clock history remains `L`-Lipschitz and every backward clock
history remains bounded by `B`, including if a density vanishes.

The derivative of `M_q` with respect to `lambda` has three parts.

The forward-value part, with density and raw backward measure fixed, is
bounded by projection contraction:

\[
 \|\partial_\lambda M_q\vert_h\|_{\rm HS}
 \le\|b_\lambda\|_{L^2(0,A_\lambda)}
       \|h_1-h_0\|_{L^2(d\tau_\lambda)}
 \le B\sqrt S\,E_h.
 \tag{21}
\]

The prefix is included in the second norm, as in (4). The first norm
has no prefix contribution, because that backward prefix is zero.

The raw backward measure part is exactly
`integral_0^T (R_1-R_0)(t) tensor p_{f_lambda}(tau_lambda(t))dt`.
By (8) it is bounded by

\[
 [H+C A_*L\sqrt{\log(e+q)}]\Delta_R.
 \tag{22}
\]

Finally changing the density by `rho_1-rho_0` inserts its signed clock
mass at each physical time. Formula (15) gives the exact derivative

\[
 \partial_\lambda M_q\vert_\rho
 =\int_0^T J_{q,\lambda}(\tau_\lambda(u))
                     [\rho_1(u)-\rho_0(u)]\,du.
 \tag{23}
\]

One can verify (23) directly by writing the moments as

\[
 B_k=\int_0^T e_k^A(\tau(t))R(t)\,dt,
\]
\[
 H_k=\int_0^1e_k^A(s)h(0)\,ds
             +\int_0^T e_k^A(\tau(t))h(t)\rho(t)\,dt.
 \tag{24}
\]

Use `partial_lambda A=integral delta rho` and
`partial_lambda tau(t)=integral_0^t delta rho`, and exchange the order
of the resulting integrals. The three terms are precisely (16)--(17).
For fixed `q`, basis derivatives are bounded on `1<=A<=A_*`, so the
integrable hypotheses justify this differentiation and Fubini. Thus
strict positivity or smoothness of the densities is unnecessary.

Equations (18) and (23) bound the density part by the last term of
(5). Integrating the three bounds in `lambda` proves (5).

## 5. Application to the actual closure and residual damping

For each hidden layer and sample use the Hilbert norms
`||v||_2/sqrt(n)` on the two neuron populations, and set

\[
 h_j=h_{\ell-1,a,j},\qquad
 R_j=r_{a,j}\delta_{\ell,a,j},\qquad
 \rho_j=\|r_j\|_m.
 \tag{25}
\]

The established actual-closure estimates give, uniformly in width, order
and physical endpoint,

\[
 S\le CY,\qquad H\le C,\qquad L\le CY,\qquad B\le CY.
 \tag{26}
\]

The factor `sqrt(m)` in `|r_a|<=sqrt(m)rho` is absorbed into the
fixed-data constant. The forward clock-Lipschitz estimate in (26) is
exactly the supplied `||dot h||_RMS<=CY rho`. The backward bound uses
only `||delta||_RMS<=CY`; no derivative of the backward gate is invoked.

In these Hilbert spaces, `b tensor h` is the matrix `b h^T/n` and
its Hilbert--Schmidt norm is ordinary matrix Frobenius norm. Therefore
the learned hidden matrix is `-(2/m) sum_a M_q`, and (5), summed over
the fixed layer/sample indices, controls its actual reconstruction.
Different initialized matrices contribute their ordinary Frobenius
difference separately.

The raw measure discrepancy admits the useful bound

\[
 \Delta_R\le CY\int_0^T|r_{a,1}-r_{a,0}|\,dt
       +\int_0^T|r_{a,0}(t)|
               \|\delta_{\ell,a,1}-\delta_{\ell,a,0}\|_{\rm RMS}\,dt,
 \tag{27}
\]

and the clock discrepancy satisfies

\[
 \Delta_\rho\le\int_0^T\|r_1-r_0\|_m\,dt.
 \tag{28}
\]

Thus the clock mismatch is controlled by the same time-integrated
residual difference which appears in a damped output comparison; a
ratio of the two residual norms never appears.

For example, if only a uniform training-output discrepancy
`delta=sup_t||r_1-r_0||_m` is available, the two established residual
envelopes still give

\[
 \int_0^\infty\|r_1-r_0\|_m\,dt
 \le\int_0^\infty\min\{\delta,2Ye^{-\kappa t}\}\,dt
 =\frac\delta\kappa\left[1+\log\frac{2Y}{\delta}\right]
 \quad(0<\delta\le2Y).
 \tag{29}
\]

At `delta=0` the integral is zero. This converts uniform output control
to the clock and residual portions of (27)--(28) with only a logarithmic
loss. If a stronger damped comparison already controls their time integral,
that estimate can be used directly.

All constants in (5), (26)--(29) are independent of the terminal physical
time. Letting `T` increase therefore gives the all-time reconstruction
bound whenever its displayed difference quantities are finite, as they
are under the common physical envelope and tube. The backward moments
remain well defined at a zero residual using their raw measure form (24).

The result removes the proposed `||A_q||=O(q^2)` loss specifically from
clock comparison of the learned reconstruction. Its order dependence
is `sqrt(log(e+q))`, not a power of `q`. Closing the entire stochastic
comparison must still estimate the forward-history and backward-field
differences in (4), (27), and the Gaussian innovation source. No claim
is made that a subsequent feedback argument may square or exponentiate
these factors without tracking the resulting order dependence.

In particular, the direct readout resolvent controls the *signed*
primitive `E(t)=integral_0^t(r_1-r_0)`, whereas the clock estimate uses
the total variation quantity `integral||r_1-r_0||`. They are different
norms. Formula (29) is a conversion for a discrepancy that has already
been controlled; inserting it into a feedback inequality of the form
`delta<=a+C sqrt(log q) delta log(1/delta)` does not close that
inequality. A complete width proof still needs a causal comparison or
a damped residual `L1` estimate from its natural error source. The
static reconstruction lemma does not assert this missing stability step.

## 6. Uniform-in-order improvement

In fact the logarithms in (5) can all be removed. The sharpened conclusion
is

\[
 \|M_q[\rho_1,h_1,R_1]-M_q[\rho_0,h_0,R_0]\|_{\rm HS}
 \le B\sqrt S\,E_h+(H+C A_*L)\Delta_R
                   +C A_*BL\Delta_\rho,
 \tag{30}
\]

with one absolute constant independent of `q`. Here is a complete
elementary proof of the Legendre fact needed for this improvement.

First,

\[
 \int_{-1}^1|P_k'(x)|\,dx\le C\sqrt k\qquad(k\ge1).
 \tag{31}
\]

We derive this estimate without importing an asymptotic expansion.
For `0<theta<pi`, the Mehler--Dirichlet integral identity is

\[
 P_k(\cos\theta)=\frac{\sqrt2}{\pi}
  \int_0^\theta
   \frac{\cos((k+1/2)u)}{\sqrt{\cos u-\cos\theta}}\,du.
 \tag{32}
\]

To verify (32), multiply its right side by `r^k` and sum, for
`0<=r<1`. The cosine sum is
`(1-r)cos(u/2)/(1-2r cos u+r^2)`. Substitute
`v=sin(u/2)/sin(theta/2)` and then `v=sin psi`. The sum becomes

\[
 \frac{2(1-r)}\pi\int_0^{\pi/2}
  \frac{d\psi}{(1-r)^2+4r\sin^2(\theta/2)\sin^2\psi}
 =\frac1{\sqrt{1-2r\cos\theta+r^2}}.
 \tag{33}
\]

For the equality, the substitution `z=tan psi` reduces the integral
to `integral_0^infinity dz/[a^2+(a^2+b)z^2]`, where
`a=1-r>0` and `b=4r sin^2(theta/2)`. This gives
`pi/[2a sqrt(a^2+b)]`. The last expression in (33) is the Legendre
generating function, so coefficient comparison proves (32).
Uniform geometric convergence and integrability of the square-root
endpoint singularity justify the summation under the integral.

For `omega>0`, the elementary oscillatory integral bound is

\[
 \sup_{x\ge0}\left|\int_0^x e^{i\omega v}v^{-1/2}dv\right|
       \le C\omega^{-1/2}.
 \tag{34}
\]

Split at `1/omega`; the first piece has absolute integral at most
`2/sqrt(omega)`. Integrate the remaining piece by parts once; its
boundary terms and the integral of `v^{-3/2}/omega` have the same
bound. Integration by parts against a bounded-variation scalar
amplitude `a` therefore gives

\[
 \left|\int_0^x e^{i\omega v}v^{-1/2}a(v)dv\right|
 \le C\omega^{-1/2}(\|a\|_\infty+\operatorname{Var}(a)).
 \tag{35}
\]

Take `0<theta<=pi/2` and put

\[
 a_\theta(v)=
 \sqrt{\frac{v\sin\theta}{\cos(\theta-v)-\cos\theta}},
 \qquad 0\le v\le\theta,
 \qquad a_\theta(0)=1.
 \tag{36}
\]

The denominator divided by `v` is the average of `sin(theta-s)` on
`0<=s<=v`; it decreases in `v`. Concavity of sine on `[0,theta]`
places this average between `sin(theta)/2` and `sin(theta)`.
Thus `a_theta` is increasing, lies between `1` and `sqrt(2)`, and
has bounded variation at most `sqrt(2)-1`. The amplitude
`a_theta(v)sin(theta-v)` has supremum plus total variation at most
`C sin(theta)`, by the product variation inequality.

Put `omega=k+1/2`. Changing variables `v=theta-u` in (35) now gives

\[
 I:=\int_0^\theta
   \frac{\sin u\sin(\omega u)}{\sqrt{\cos u-\cos\theta}}\,du,
 \qquad |I|\le C\sqrt{\frac{\sin\theta}{k}}.
 \tag{37}
\]

Use (32) for `k-1` and `k`. Their difference, with coefficient
`cos(theta)`, has numerator

\[
 \cos((\omega-1)u)-\cos\theta\cos(\omega u)
 = (\cos u-\cos\theta)\cos(\omega u)
                    +\sin u\sin(\omega u).
 \tag{38}
\]

The integral of the first term divided by the square root is

\[
 \int_0^\theta\sqrt{\cos u-\cos\theta}\cos(\omega u)du
       =\frac{I}{2\omega},
 \tag{39}
\]

by ordinary integration by parts; its boundary terms vanish at both
endpoints. Consequently (37)--(39) and
`(1-x^2)P_k'(x)=k[P_{k-1}(x)-xP_k(x)]` imply

\[
 |P_k'(\cos\theta)|
       \le\frac{C\sqrt k}{(\sin\theta)^{3/2}}.
 \tag{40}
\]

Reflection gives the same bound for `pi/2<=theta<pi`.
Integrating against `dx=sin(theta)dtheta` proves (31), because
`integral_0^pi (sin theta)^{-1/2}dtheta` is finite.

Next let `f` be an absolutely continuous Hilbert-valued function on
`[-1,1]`, with `g=f' in L2`. Write `Pi_n` for projection onto degrees
at most `n`, and let
`gamma_k=(2k+1)integral_{-1}^1 g(x)P_k(x)dx/2`.
For `n>=1`, coefficient integration by parts and telescoping give

\[
 (\Pi_n f)'=\Pi_{n-1}g
 -\frac{\gamma_n}{2n+1}P_{n-1}'
 -\frac{\gamma_{n+1}}{2n+3}P_n'.
 \tag{41}
\]

Indeed, if `alpha_k` is the `k`th Legendre coefficient of `f`, then
`alpha_k=gamma_{k-1}/(2k-1)-gamma_{k+1}/(2k+3)` for `k>=1`.
Insert this into
`P_k'=sum_{j<k, k-j odd}(2j+1)P_j`; all interior coefficients
telescope, leaving precisely the two displayed boundary coefficients.
The boundary term in the coefficient integration by parts is zero
because `P_{k+1}-P_{k-1}` vanishes at both endpoints.

Cauchy--Schwarz gives

\[
 \left\|\frac{\gamma_k}{2k+1}\right\|
 \le\frac{\|g\|_{L^2}}{\sqrt{2(2k+1)}}.
 \tag{42}
\]

Projection contraction bounds the `L1` norm of the first term in (41)
by `sqrt(2)||g||L2`; (31)--(42) bound both other terms by the same
constant multiple of `||g||L2`. Therefore

\[
 \|(\Pi_n f)'\|_{L^1(-1,1)}\le C\|f'\|_{L^2(-1,1)}.
 \tag{43}
\]

Rescaling to `[0,A]` proves, for the `L`-Lipschitz forward history,

\[
 \int_0^A\|p_f'(s)\|ds\le CAL,
 \qquad \|p_f\|_\infty\le H+CAL.
 \tag{44}
\]

The supremum estimate uses the already proved endpoint error in (7).
The constant projection `q=1` satisfies (44) directly. Formula (11)
and (31) also sharpen the backward endpoint estimate to

\[
 \|p_b(A)\|\le CB\sqrt q.
 \tag{45}
\]

Substituting (44)--(45) into the exact insertion identity (15) gives
`||J_q(a)||HS<=C ABL`, with no order factor. The proof in Section 4
then proves (30) verbatim, using (44) in the raw-measure term.
This is the asserted order-uniform clock comparison. No extra
regularity of the backward history has entered its improvement.

## 7. A damped residual L1 resolvent with a variation source

There is a separate exact way to obtain the `L1` residual norm needed
by (28). Let a reference forward kernel `Q_*(t,s)`, `0<=s<=t`, obey

\[
 Q_*(t,t)\succeq\lambda I_m,
 \qquad \sup_{0\le s\le t}\|\partial_tQ_*(t,s)\|\le a(t),
 \qquad A_0:=\int_0^\infty a(t)dt<\infty.
 \tag{46}
\]

Assume the kernel is absolutely continuous in its first argument with
the displayed domination, and let an absolutely continuous source `D`
have finite total variation
`TV(D)=integral_0^infinity||D'(t)||_m dt`. If

\[
 e(t)=D(t)-2\int_0^tQ_*(t,s)e(s)ds,
 \tag{47}
\]

then

\[
 \int_0^\infty\|e(t)\|_m dt
 \le\frac{\|D(0)\|_m+\operatorname{TV}(D)}{2\lambda}
                                  e^{A_0/\lambda}.
 \tag{48}
\]

To prove it, differentiate (47) on a finite interval:

\[
 e'=-2Q_*(t,t)e-2\int_0^t\partial_tQ_*(t,s)e(s)ds+D'.
 \tag{49}
\]

The propagator of the first term has norm at most
`exp(-2lambda(t-u))`, by the Gram gap. Write
`V(T)=integral_0^T||e(t)||_m dt`. Variation of constants, followed by
Tonelli's theorem for the norm bounds, gives

\[
 V(T)\le\frac{\|D(0)\|_m+\int_0^T\|D'(u)\|_mdu}{2\lambda}
             +\frac1\lambda\int_0^T a(u)V(u)du.
 \tag{50}
\]

The integral integrating factor proves (48) as `T` increases. No
smallness beyond the reference gap and integrability in (46) is used.
The established forward velocity bounds give
`a(t)<=CY rho_*(t)` and hence `A_0<=CY^2` for the reference kernel
in this study.

For the actual two-time forward-Gram discrepancy source

\[
 D(t)=-2\int_0^t[Q_n(t,s)-Q_*(t,s)]r_n(s)ds,
 \tag{51}
\]

the required variation source has the exact bound

\[
 \operatorname{TV}(D)\le
 2\int_0^\infty\|Q_n(t,t)-Q_*(t,t)\|\rho_n(t)dt
 +2\int_0^\infty\int_0^t
    \|\partial_t(Q_n-Q_*)(t,s)\|\rho_n(s)dsdt.
 \tag{52}
\]

This follows by differentiating (51) and integrating the resulting
norm bound. It exposes a sufficient causal source metric for the
clock comparison. The finite tube and damping give coarse finite bounds
for these integrals; a near-root-width estimate for their *discrepancy*
is not proved here. In particular an iid empirical reference estimate
for a forward kernel and its physical-time derivative would address its
own empirical component, but does not identify the actual reused-matrix
finite system with that reference.

Equations (30) and (48) remove both the moment-transport order loss and
the signed-primitive mismatch from the deterministic list of obligations,
provided the explicit variation source (52) is controlled. Establishing
that source at the claimed width rate remains part of the Gaussian
comparison. These are complete deterministic implications, not a claim
that the full width theorem has been proved.

# Exact Gaussian normalization of analytic activations

2026-10-04. Scoped independent route in the current study. This note proves
activation-level statements from elementary Gaussian integration. Its complete
scientific inputs are `ACTIVATION_CLASS_EXTENSION_ROUTE.md`,
`ACTIVATION_CLASS_EXTENSION_CHECK.md`, and
`ARCHITECTURE_CONSTANT_REFINEMENT.md`; no linked sources or sibling new notes
were read. The canonical-notation, neural-network, and rigorous-proof skills
were applied. The existing all-time compression interfaces are inputs, not
reproved here. Nothing is promoted into the maintained book.

This note concerns the mean-square normalization: the square is inside
each expectation in (1). Normalization by squared expectations is a
different question and is outside this route's scope.

The main result is constructive: every nonconstant smooth activation with
bounded derivative admits a positive output rescaling and one of two output
offsets for which
\[
\mathbb E[\phi(Z)^2]=\mathbb E[\phi'(Z)^2]=1,
\qquad Z\sim N(0,1).
\tag{1}
\]
For a nonaffine activation these normalizations necessarily have nonzero
Gaussian mean. Exact GELU is an unbounded analytic example satisfying the
complex-strip derivative condition of the supplied extension. Neither (1)
nor this example removes the all-time theorem's depth-dependent constants.

## 1. A complete normalization formula

Let `g:R->R` be twice continuously differentiable, with bounded first and
second derivatives. All examples below have these properties. Define
\[
\mu=\mathbb E g(Z),\qquad
Q=\mathbb E g(Z)^2,\qquad
V=Q-\mu^2,\qquad D=\mathbb E g'(Z)^2.
\tag{2}
\]
The bounded derivative gives linear growth, so all expectations are finite.
Assume `g` is nonconstant; then `D>0`. Gaussian Poincare, proved below in the
form needed here, says `V<=D`, with equality precisely for affine `g`.
Consequently both functions
\[
\phi_\pm(z)
=\frac{g(z)-\mu\pm\sqrt{D-V}}{\sqrt D}
\tag{3}
\]
satisfy (1). Indeed their derivative second moment is `D/D`, and their
value second moment is `[V+(D-V)]/D`. These are exactly the possibilities
`a g+b` with positive multiplier `a`: the derivative condition fixes
`a=D^(-1/2)`, and the value condition fixes the Gaussian mean to
`+/-sqrt(1-V/D)`.

Here is a proof of the needed inequality and its equality case. Let `X,Y`
be independent standard Gaussians, let
`Y_r=rX+sqrt(1-r^2)Y`, and put
`C(r)=E[g(X)g(Y_r)]` for `0<=r<=1`. For `0<r<1`, differentiation and
Gaussian integration by parts give
\[
\begin{aligned}
C'(r)
&=\mathbb E\!\left[g(X)g'(Y_r)
 \left(X-\frac r{\sqrt{1-r^2}}Y\right)\right]\\
&=\mathbb E[g'(X)g'(Y_r)].
\end{aligned}
\tag{4}
\]
The two terms containing `g(X)g''(Y_r)` cancel. Bounded derivatives and
Gaussian integrability justify these operations on compact subintervals
of `(0,1)`; continuity and the uniform bound `|C'(r)|<=D` extend the
integral identity to the endpoints. Thus
\[
V=C(1)-C(0)=\int_0^1\mathbb E[g'(X)g'(Y_r)]\,dr\le D.
\tag{5}
\]
The last inequality is Cauchy--Schwarz, since both marginals are standard
Gaussian. Its deficit has the useful exact form
\[
D-V=\frac12\int_0^1
\mathbb E[(g'(X)-g'(Y_r))^2],dr.
\tag{6}
\]
If `D=V`, the integrand vanishes for almost every `r`. Choose one such
`r` in `(0,1)`. The pair `(X,Y_r)` has strictly positive density on all of
`R^2`; continuity then makes `g'(x)=g'(y)` for every `x,y`. Hence `g` is
affine. An affine function attains equality directly.

There are two immediate limitations. A centered nonaffine `phi` cannot
satisfy (1), because then `V=1=D` would force affinity. Also for an odd
nonaffine `g`, neither an output rescaling alone nor a combination of
nonzero input and output rescalings can satisfy (1): oddness gives `mu=0`
and strict inequality `Q<D`. An output offset breaks oddness and is a
change to the activation used by the network, not a change of notation.

## 2. Tanh, erf, identity, and an unbounded near-identity family

For `g(z)=tanh(z)`, define the two exact Gaussian integrals
\[
Q_{\tanh}=\frac1{\sqrt{2\pi}}\int_{\mathbb R}
 \tanh^2z\,e^{-z^2/2}\,dz,
\qquad
D_{\tanh}=\frac1{\sqrt{2\pi}}\int_{\mathbb R}
 \operatorname{sech}^4z\,e^{-z^2/2}\,dz.
\tag{7}
\]
Oddness gives `mu=0`, and (6) gives `D_tanh>Q_tanh`. The normalized
activation is therefore
\[
\phi_\pm(z)=\frac{\tanh z\pm\sqrt{D_{\tanh}-Q_{\tanh}}}
 {\sqrt{D_{\tanh}}}.
\tag{8}
\]
It remains bounded. Direct quadrature, used only as an arithmetic check,
gives `Q_tanh=0.3942944904`, `D_tanh=0.4644029024`, and
`phi_+(z)=1.4674135916 tanh(z)+0.3885416701` to the shown precision.
The exact definition is (7)--(8).

For erf, state the input scale explicitly: let
`g_alpha(z)=erf(alpha z)`, where `alpha>0` and
`erf(u)=(2/sqrt(pi)) int_0^u exp(-t^2)dt`. Its mean is zero and
\[
Q_\alpha=\frac2\pi\arcsin\frac{2\alpha^2}{1+2\alpha^2},
\qquad
D_\alpha=\frac{4\alpha^2}{\pi\sqrt{1+4\alpha^2}}.
\tag{9}
\]
The expression for `D_alpha` is the Gaussian integral of
`g_alpha'(z)^2=(4alpha^2/pi) exp(-2alpha^2 z^2)`.
For the first expression, differentiate `E erf(alpha Z)^2` in `alpha`
and integrate the Gaussian factor by parts:
\[
\frac d{d\alpha}\mathbb E\operatorname{erf}(\alpha Z)^2
=\frac{8\alpha}{\pi(1+2\alpha^2)\sqrt{1+4\alpha^2}}.
\]
For example the integral used here is
`E[Z erf(alpha Z)e^(-alpha^2 Z^2)]
=2alpha/[sqrt(pi)(1+2alpha^2)sqrt(1+4alpha^2)]`.
The derivative agrees with that of the right side of (9), and both
vanish at `alpha=0`, proving the formula. Equation (3) now gives
\[
\phi_\pm(z)=\frac{\operatorname{erf}(\alpha z)
 \pm\sqrt{D_\alpha-Q_\alpha}}{\sqrt{D_\alpha}}.
\tag{10}
\]
For `alpha=1`, this is numerically
`phi_+(z)=1.3252183529 erf(z)+0.4291149937`. It remains bounded.

For identity, `g(z)=z` has `mu=0` and `Q=D=1`; the positive-rescaling
construction gives exactly `phi(z)=z` and no offset. Allowing a negative
rescaling adds `phi(z)=-z`. More generally the only normalized affine
activations are `+z` and `-z`: for `phi=az+b`, (1) requires `a^2=1`
and then `a^2+b^2=1`, hence `b=0`.

The source's unbounded nonaffine example also admits a transparent exact
normalization. Let `g_epsilon(z)=z+epsilon tanh(z)`, with
`epsilon` any nonzero real number, and put
`u=E sech^2(Z)`. Gaussian integration by parts gives
`E[Z tanh Z]=u`, so
\[
D_\varepsilon=1+2\varepsilon u+\varepsilon^2D_{\tanh},
\qquad
Q_\varepsilon=1+2\varepsilon u+\varepsilon^2Q_{\tanh}.
\]
Here `D_epsilon>0`, because `1+epsilon sech^2(z)` is not identically
zero. Thus the unbounded nonaffine activations
\[
\phi_\pm(z)=
\frac{z+\varepsilon\tanh z
 \pm|\varepsilon|\sqrt{D_{\tanh}-Q_{\tanh}}}
 {\sqrt{1+2\varepsilon u+\varepsilon^2D_{\tanh}}}
\tag{11}
\]
satisfy (1) and converge to identity as `epsilon->0`. At fixed nonzero
`epsilon`, they do not inherit the affine projection commutation identity.

## 3. Exact GELU: closed-form constants and both offsets

Define the Gaussian density and distribution function by
\[
\varphi(z)=\frac1{\sqrt{2\pi}}e^{-z^2/2},\qquad
\Phi(z)=\frac12+\int_0^z\varphi(u)\,du,
\]
where the integral defines their entire complex extensions. Exact GELU is
`g(z)=z Phi(z)`, rather than a tanh approximation. Its first two derivatives
are
\[
g'(z)=\Phi(z)+z\varphi(z),\qquad
g''(z)=(2-z^2)\varphi(z).
\tag{12}
\]
The exact moments are
\[
\mu=\frac1{2\sqrt\pi},\qquad
Q=\frac13+\frac1{2\pi\sqrt3},\qquad
D=\frac13+\frac2{3\pi\sqrt3},\qquad
D-Q=\frac1{6\pi\sqrt3}.
\tag{13}
\]
For verification, integration by parts gives
`E[Z Phi(Z)]=E varphi(Z)=1/(2sqrt(pi))`. Since `Phi(Z)` is uniform
on `(0,1)`, `E Phi(Z)^2=1/3`. The remaining elementary integrals are
\[
\mathbb E\varphi(Z)^2=\frac1{2\pi\sqrt3},\quad
\mathbb E[Z\Phi(Z)\varphi(Z)]=\frac1{4\pi\sqrt3},\quad
\mathbb E[Z^2\varphi(Z)^2]=\frac1{6\pi\sqrt3}.
\tag{14}
\]
The middle identity follows by integrating
`z varphi(z)^2=-(1/2)(varphi(z)^2)'`; the other two are Gaussian
integrals. Expanding `g'^2` proves the expression for `D`.
The identity `E[Z^2F(Z)]=E F(Z)+E F''(Z)`, applied to `F=Phi^2`,
gives `Q=1/3+2E varphi^2-2E[Z Phi varphi]`, proving (13).

Define two raw output offsets
\[
b_\pm=-\frac1{2\sqrt\pi}
 \pm\sqrt{\frac1{4\pi}+\frac1{6\pi\sqrt3}}.
\tag{15}
\]
Both normalized GELU functions are
\[
\phi_\pm(z)=
\frac{z\Phi(z)+b_\pm}
 {\sqrt{\frac13+\frac2{3\pi\sqrt3}}}.
\tag{16}
\]
The plus branch is numerically
\[
\phi_+(z)=1.4811144127\,z\Phi(z)+0.0738770773.
\tag{17}
\]
Its mean is about `0.4916917392`; the minus branch has the opposite
mean. The raw offsets are about `b_+=0.0498793859` and
`b_-=-0.6140689694`. Both are unbounded and nonaffine, and (13)--(16)
verify (1) exactly. The decimals are supplementary evaluations, not premises.

Output rescaling alone cannot normalize exact GELU, because `D>Q`.
Changing its input scale does not fix that obstruction. Indeed, for
`g_alpha(z)=z Phi(alpha z)` with `alpha>0`, let
`I=E varphi(alpha Z)^2=1/[2pi sqrt(1+2alpha^2)]`.
Integration by parts gives
\[
\mathbb E[Z\Phi(\alpha Z)\varphi(\alpha Z)]
=\frac{\alpha I}{1+\alpha^2},\qquad
\mathbb E[Z^2\varphi(\alpha Z)^2]=\frac I{1+2\alpha^2}.
\]
Writing `U=E Phi(alpha Z)^2`, expansion of the derivative square and
the second Gaussian integration-by-parts identity give
\[
D_\alpha=U+\frac{2\alpha^2I}{1+\alpha^2}
              +\frac{\alpha^2I}{1+2\alpha^2},\qquad
Q_\alpha=U+\frac{2\alpha^2I}{1+\alpha^2}.
\]
Therefore
\[
D_\alpha-Q_\alpha
=\frac{\alpha^2}{2\pi(1+2\alpha^2)^{3/2}}>0.
\tag{18}
\]
The family `GELU(alpha z)` differs from `g_alpha` only by an output
factor, so the same impossibility applies at every finite nonzero scale.

## 4. Complex-strip derivative bounds, including GELU

The unbounded-value source requires an activation real on the real axis,
holomorphic on `|Im z|<a`, with finite value at zero and uniformly
bounded first derivative on that strip. Formula (3) preserves these
properties whenever `g` has them: its derivative bound is divided by
`sqrt(D)` and its value at zero is the explicit finite constant in (3).
This verifies the source's actual condition; boundedness of `g` itself
is unnecessary.

For tanh, on `|Im z|<pi/4`,
\[
|\tanh z|\le1,\qquad
|\tanh'(z)|=|\operatorname{sech}^2z|\le2,
\]
because `|cosh(x+iy)|^2=sinh^2(x)+cos^2(y)` and
`|sinh(x+iy)|^2=sinh^2(x)+sin^2(y)`.
The derivative bounds for (8) and (11) are respectively
`2/sqrt(D_tanh)` and `(1+2|epsilon|)/sqrt(D_epsilon)` on this strip.

For `erf(alpha z)`, every finite strip width `a>0` is allowed, and
\[
\sup_{|\operatorname{Im}z|<a}|g_\alpha'(z)|
\le\frac{2\alpha}{\sqrt\pi}e^{\alpha^2a^2}.
\tag{19}
\]
Thus (10) has the same bound divided by `sqrt(D_alpha)`.
It is also bounded in each finite strip: integrate its derivative on the
vertical segment from the real axis, where `|erf(alpha x)|<=1`.

For GELU and `z=x+iy` with `|y|<a`,
\[
|\varphi(z)|\le\frac{e^{a^2/2}}{\sqrt{2\pi}}e^{-x^2/2},
\qquad
|\Phi(z)|\le1+\frac{a e^{a^2/2}}{\sqrt{2\pi}}.
\]
The second inequality integrates along the same vertical segment and
uses `0<=Phi(x)<=1`. Since
`sup_x |x|exp(-x^2/2)=exp(-1/2)`, (12) gives
\[
\sup_{|\operatorname{Im}z|<a}|g'(z)|
\le1+\frac{e^{a^2/2}}{\sqrt{2\pi}}(2a+e^{-1/2}).
\tag{20}
\]
Dividing this by `sqrt(D)` proves the required finite strip bound for
both branches in (16), for every fixed `a>0`. GELU's entire extension
does not give a width-independent bound as `a->infinity`; (20) records
the actual dependence. Cauchy's formula applied to the bounded first
derivative on radius-`a/4` disks yields, on `|Im z|<=a/2`,
\[
|\phi^{(j)}(z)|\le (j-1)!s(4/a)^{j-1},\qquad j\ge2,
\tag{21}
\]
where `s` is any certified strip bound for `|phi'|`. This also makes all
fixed Gaussian higher derivative moments finite.

Identity has strip derivative bound one for every strip. The normalized
nonlinear examples have a strictly larger real supremum of `|phi'|`.
If that supremum were at most one, (1) would force `|phi'|=1` everywhere
by continuity and full Gaussian support. A continuous derivative with
values in `{+1,-1}` is constant, forcing affinity. Thus Gaussian
normalization cannot set the actual deterministic derivative bound to one
for any of these nonaffine examples.

## 5. What the normalization controls, and a GELU variance issue

For the canonical Gaussian covariance recursion in the supplied sources,
unit-norm inputs give diagonal `Q^(0)_aa=1`. If every layer uses an
activation satisfying (1), then induction gives `Q^(ell)_aa=1` at every
layer. This is an exact statement about the infinite-width initialized
covariance recursion, with fixed depth. It does not state an exact empirical
identity for a finite initialized network, or a Gaussian law during training.

In particular the positive gap `gamma=lambda_min(Q^(L))` still needs
control. Unit diagonal gives `trace Q^(L)=m` and hence `gamma<=1`, but
provides no positive lower bound. For identity, `Q^(L)=Q^(0)` exactly,
so a positive gap requires linearly independent training inputs and `m<=d`.
The supplied unbounded theorem keeps its explicit gap hypothesis for
nonlinear activations as well.

There is also a distinction between the derivative-square condition and
stability of a variance perturbation. Define
\[
F(q)=\mathbb E\phi(\sqrt q Z)^2,\qquad q>0.
\]
Although `F(1)=1`, differentiation followed by Gaussian integration by
parts gives
\[
F'(1)=\mathbb E\phi'(Z)^2+\mathbb E[\phi(Z)\phi''(Z)]
=1+\mathbb E[\phi(Z)\phi''(Z)].
\tag{22}
\]
Thus (1) does not ensure `F'(1)<=1`. For the exact GELU branches,
Gaussian integration gives
\[
\mathbb E g''(Z)=\frac3{4\sqrt\pi},\qquad
\mathbb E[g(Z)g''(Z)]=\frac1{6\pi\sqrt3}.
\]
For the second identity, write
`J_k=E[Z^k Phi(Z)varphi(Z)]`; (14) gives `J_1`, and integration of
`z^3 varphi(z)^2` gives `J_3=1/(3pi sqrt(3))`. Hence
`E g g''=2J_1-J_3=1/(6pi sqrt(3))`. Substitution in (22) yields
\[
F_\pm'(1)=1+
\frac{\frac1{6\pi\sqrt3}+\frac{3b_\pm}{4\sqrt\pi}}D.
\tag{23}
\]
The plus branch is locally expanding in this scalar variance direction:
`F_+'(1)=1.1134920638...`. The minus branch gives
`F_-'(1)=0.4971840106...`. Both satisfy (1).

These signs can also be checked without decimals. Put
`A=1/(4pi)` and `c=1/(6pi sqrt(3))`; then
`mu=sqrt(A)`, `b_+=sqrt(A+c)-sqrt(A)>0`, and the plus numerator
in (23) is positive. For the minus branch that numerator is
`c-(3/2)sqrt(A)(sqrt(A)+sqrt(A+c))`, which is negative because
`c<3A`. Its magnitude is less than `D`: the inequality
`sqrt(A(A+c))<=A+c/2` bounds it above by `3A-c/4<1/3<D`.
Thus `0<F_-'(1)<1` holds exactly. The decimal evaluations simply
quantify it.

This is an initialized scalar recursion observation, not a counterexample
to a trained-network polynomial-depth theorem. It does show that replacing
every forward or perturbative layer gain by one using only (1) would be
invalid, even for normalized exact GELU.

## 6. Higher moments and higher response order are separate requirements

For a nonaffine normalized analytic activation and any real `p>2`, strict
Jensen gives
\[
\mathbb E|\phi'(Z)|^p>
(\mathbb E|\phi'(Z)|^2)^{p/2}=1.
\tag{24}
\]
Strictness follows because a constant value of `|phi'|` would force the
affine case as above. Consequently a scalar chain of independent Gaussian
gates, `J_L=prod_(ell=1)^L phi'(Z_ell)`, obeys
\[
\mathbb E|J_L|^2=1,\qquad
\mathbb E|J_L|^p=(\mathbb E|\phi'(Z)|^p)^L.
\tag{25}
\]
This is an exact example showing that the second moment alone cannot
replace higher moments by one. It is not a lower bound for the normalized
Schatten moments of a wide dense-network Jacobian: Gaussian mixing and
path averaging must be analyzed in that model before drawing such a
conclusion.

There is a complementary positive statement at each fixed derivative order
for the initialized, normalized correlation map. Define
\[
K(r)=\mathbb E[\phi(X)\phi(Y_r)],\qquad -1\le r\le1.
\]
Repeated use of (4), with the finite derivative bounds above, gives the
one-sided endpoint identities
\[
K(1)=K'(1)=1,\qquad
K^{(j)}(1)=\mathbb E\phi^{(j)}(Z)^2\quad(j\ge2).
\tag{26}
\]
For a nonaffine activation put `a=E phi''(Z)^2>0` and
`b=E phi'''(Z)^2`. For identical activations at every layer, the
depth-`L` correlation is the `L`-fold composition `K_L=K o ... o K`.
The chain rule gives exactly
\[
K_L'(1)=1,\qquad K_L''(1)=La,\qquad
K_L'''(1)=Lb+\frac32L(L-1)a^2.
\tag{27}
\]
For either GELU branch, the constants in this display are explicitly
\[
a=\frac{\sqrt3}{2\pi D},\qquad
b=\frac{29}{18\pi\sqrt3 D}.
\]
Indeed `g''=(2-z^2)varphi` and `g'''=(z^3-4z)varphi`; integration
against `varphi(z)^3` uses Gaussian variance `1/3` and gives the
displayed second moments before division by `D`. The offset has no
effect on these constants.
For completeness every fixed derivative order `j` is a polynomial in
`L` of degree at most `j-1`. To prove this, start with `K_0(r)=r`.
In the derivative formula for `K(K_L(r))`, the term with one derivative
of `K` is exactly `K_L^(j)(1)`. Each remaining term is a fixed
coefficient `K^(k)(1)`, `k>=2`, times products of derivatives of
`K_L` of orders summing to `j`, with exactly `k` factors. By induction
their degrees sum to at most `j-k<=j-2`. Thus the increment from depth
`L` to `L+1` is polynomial of degree at most `j-2`; summing it gives
degree at most `j-1`. Formula (27) is the direct second/third-order
instance. This proof controls each fixed order; it gives no constants
uniform in the response order.

In particular, an endpoint expansion that sums all response orders still
needs bounds on those polynomial coefficients and their order dependence.
Equation (21) allows factorial growth with derivative order, and the
original complex proof uses actual higher Schatten/moment estimates to
sum its endpoint expansion. Fixed-order statements (26)--(27) cannot
replace that summation step. Nor do they address the trained finite-network
response, an entire query sphere, or the compressed runtime comparison.

## 7. Exact interface with the existing compression claims

The normalized tanh and erf examples remain bounded strip-analytic
activations, so their actual strip constants can be inserted into the
bounded-activation theorem's stated definition of `beta`. Their Gaussian
normalization does not change that definition: it includes the floor ten,
strip width, and actual supremum bounds, and it is not a Gaussian
root-mean-square parameter.

Normalized GELU, identity, and (11) satisfy the supplied linear-growth
extension's activation hypothesis. Relative to that source's inherited
interfaces, they are therefore legitimate activation examples for its
qualitative all-time compressor when the explicit positive gap and
sufficiently small fixed labels are imposed. That extension proves
`C n^(-1/2)` error and retained logarithmic exponent
`2[d(L+5)+1]` for the corrected-readout runtime. Its coefficients remain
unquantified in depth. The affine identity case has the separate
`O(log(en)^4)` source construction and `C/n` error under its gap condition;
its unspecified constants are not proved depth-uniform.

No statement here transfers the bounded theorem's numerical label cap
`Y<=(gamma/m) beta^(-62L)`, error envelope `beta^(124L)`, or improved
`3d+2` logarithmic exponent to normalized GELU. No statement replaces
`beta` by one. The new rigorous content is the normalization construction,
the exact examples and strip verification, and the distinctions between
unit Gaussian second moments, variance stability, fixed-order correlation
derivatives, and higher response-moment control. A polynomial-depth
all-time compression theorem needs additional analysis of the last three
interfaces in the actual network and runtime.

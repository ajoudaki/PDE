# Arbitrary fixed depth and finite data: analytic neuron compression

2026-10-03. Coordinator synthesis and construction. **Internally checked
research theorem.** The complete complex-source and activation proof,
deterministic comparison, and construction have each passed the separate
reconstructions linked below. These are internal collaborative checks,
not independent promotion reviews or established manuscript claims.

The representation contract is inherited from the completed two-input
theorem: finite exact-real preprocessing from initialization, labels and
training data is allowed; its work, temporary workspace and precision
are not bounded. All real numbers retained after setup, both moving and
fixed, count. The output must be a smaller autonomous network with its
own residuals and trained hidden layers, with no trained reference
trajectory supplied to it. This is a direct dense-network result, not a
claim about leaving the order-$q$ closure equations unchanged.

## 1. Exact model, scope and conclusion

Fix an input dimension $d\ge2$, hidden depth $L\ge2$, sample count
$m\ge1$, training inputs $x_1,\ldots,x_m\in\sqrt d S^{d-1}$, and
labels $y=(y_1,\ldots,y_m)$. Put $v_a=x_a/\sqrt d$ and
$Y=(m^{-1}\sum_a y_a^2)^{1/2}$. These quantities are independent of
width. No orthogonality or label sign condition is imposed.

For each hidden layer $\ell$, assume $\phi_\ell$ is real valued on
the real axis, holomorphic on a fixed strip $|\operatorname{Im}z|<b$,
and bounded there by a fixed constant. Different layers can use different
activations. On a narrower strip Cauchy's formula supplies bounded
derivatives of every fixed order. This is a wider class than tanh,
but a stricter class than the bounded-$C^3$ assumption in the previous
closure tracking result. Analyticity is an explicit assumption.

The original model has width $n$ in every hidden layer:

\[
 z^{(1)}(x)=Ax/\sqrt d,\quad
 h^{(\ell)}(x)=\phi_\ell(z^{(\ell)}(x)),\quad
 z^{(\ell)}(x)=W^{(\ell)}h^{(\ell-1)}(x)\quad(\ell\ge2),
 \qquad f_n(x)=w^\top h^{(L)}(x)/n.                 \tag{1}
\]

Entries of $A_0$ are independent $N(0,1)$, entries of each
$W_0^{(\ell)}$ are independent $N(0,1/n)$, all arrays are independent,
and $w_0=0$. The squared mean training loss and mobilities
$(n,1,\ldots,1,n)$ give, with $c_a=y_a-f_n(x_a)$,

\[
 \dot A=\frac2m\sum_a c_a\delta_a^{(1)}v_a^\top,
 \quad \dot W^{(\ell)}=\frac2{mn}\sum_a
 c_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},
 \quad \dot w=\frac2m\sum_a c_ah_a^{(L)},             \tag{2}
\]

where $k_a^{(L)}=w$,
$\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)}$,
and $k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}$ for
$\ell<L$. All derivatives below refer to this physical time.

Assume the deterministic limiting initialized top-feature Gram is
positive definite. It can be specified without any population-training
assumption: set $Q^{(0)}_{ab}=v_a^\top v_b$ and recursively

\[
 Q^{(\ell)}_{ab}
 =\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
 \qquad (Z_1,\ldots,Z_m)\sim N(0,Q^{(\ell-1)}),
 \qquad Q^{(L)}\succeq\gamma I_m,
                                                        \tag{3}
\]

for some fixed $\gamma>0$. Conditional independence of the Gaussian
rows, bounded-variable concentration, and continuity of Gaussian
expectations prove by induction that the empirical top-feature Gram
converges in probability to $Q^{(L)}$. The initialization gap is thus
an explicit data/activation condition, not a condition on the later
training trajectory. It is the existing small-label fitting hypothesis.

**Theorem.** There are constants $Y_*>0$, $C<\infty$ and
$P=4[d(L+5)+1]$, depending only on the fixed data, activations, depth
and gap, such that the following holds. For any fixed $y$ with
$Y\le Y_*$, and any fixed $0<\eta<1/2$, for all sufficiently large
$n\ge n_0(y,\eta)$ an initialization-only construction gives a smaller
autonomous weighted network with at most

\[
                  C[\log(en)]^P=o(n)                 \tag{4}
\]

total retained real coordinates, and with probability at least $1-\eta$,

\[
 \sup_{t\in[0,\infty]}\sup_{x\in\sqrt d S^{d-1}}
          |f_C(t,x)-f_n(t,x)|\le C/\sqrt n.          \tag{5}
\]

On this same event, both networks continue training for all time, interpolate all their
training labels, and converge. Their endpoints are included in (5).
The confidence assertion is for every sufficiently large width, not a
claim of one probability event covering all widths simultaneously.
The constants do not grow with width or elapsed training time.
The exponent in (4) is deliberately conservative. The case $Y=0$
has identically zero output and needs no dynamics. For $d=1$ there
are two sphere queries, and the angular factors below can be omitted.

## 2. Source approximation and the retained dimensions

This section applies the separately proved complex-source theorem.
Put $\lambda=\log(en)$,
$K=L+4$, $T=C_T\lambda$, and $r=c\lambda^{-K}$. The
deep source theorem supplies, with probability tending to one,
holomorphic extensions of the following vectors to the time rectangle
$-r\le\operatorname{Re}t\le T+r$, $|\operatorname{Im}t|\le r$,
and the product strip $|\operatorname{Im}\theta_j|\le r$ for a
standard periodic sphere parameterization $x=\sqrt d\,v(\theta)$:

\[
 h^{(\ell)}(t,x),\quad
 W_0^{(\ell)}h^{(\ell-1)}(t,x),\quad
 \delta_a^{(\ell)}(t),\quad
 W_0^{(\ell+1)\top}\delta_a^{(\ell+1)}(t).             \tag{6}
\]

Their coordinate bounds are at most $C\lambda^{L+2}$; gates themselves
are uniformly bounded. Only the first two families depend on the query.
All layer ranges in (6) are the natural ones. The real finite-network
carrier theorem supplies, on a further event of probability tending to
one, $\max_{a,\ell,i,t\ge0}|k_{a,i}^{(\ell)}(t)|\le C\sqrt\lambda$.

Take

\[
 \epsilon=n^{-1/2}e^{-D\sqrt\lambda}/\lambda.          \tag{7}
\]

For fixed nonzero $Y$, this is at most $\min(1,Y)$ for large $n$.
The coordinate approximation is a tensor polynomial, algebraic in time
and trigonometric in each of the $d-1$ angles. For completeness, a
Bernstein ellipse of parameter $e^{cr/T}$ gives a temporal coefficient
tail at most $CM(T/r)e^{-cpr/T}$ when the coordinate bound is $M$.
Moving each angular Fourier integral to its strip edge gives a tail
at most $CMr^{-(d-1)}e^{-crJ}$ after truncating every angular degree
at $J$. Tensor aliasing changes these fixed-dimensional estimates by
constants and polynomial factors in $p,J$; their logarithms are absorbed
in the following choices:

\[
 p\le C\lambda^{K+2},\qquad J\le C\lambda^{K+1}.
                                                        \tag{8}
\]

One can choose the constants so the final coordinate error is at most
$\epsilon$ for every source. Each source then has at most

\[
 (p+1)(2J+1)^{d-1}
       \le C\lambda^{K+2+(d-1)(K+1)}
       =C\lambda^{d(L+5)+1}                           \tag{9}
\]

real coefficient vectors. Training-only sources use at most $p+1$.
The harmless enlargement needed for the finite values at initialization
does not change (9).

These coefficients can be obtained from initial derivatives alone.
Use the explicit conformal map in Section 4 of
`TWO_INPUT_STABLE_GEOMETRY.md` to map a disk centered at the initialized
time to the whole time rectangle. Its inverse maps $[0,T]$ into a
compact interval of the disk with distance at least $ce^{-CT/r}$ from
the boundary. A finite Taylor truncation of the composed source therefore
approximates all temporal interpolation nodes to any prescribed positive
tolerance. Its coefficients are finite linear combinations of
$\partial_t^j h(0,x)$ or the corresponding source derivatives.
Those derivatives are computed by differentiating (2), never by
observing a trained path. Apply the temporal discrete cosine transform
and the tensor angular discrete Fourier transform, using a sufficiently
smaller initial tolerance to absorb their finite operator norms.
All intermediate jets and scalar arrays are discarded after the final
coefficient vectors have been formed. The finite but potentially enormous
derivative order is not included in the post-setup state count.

Use identical scalar operations on a source and its initialized matrix
image. Thus every lower forward coefficient $u$ has its exact image
$W_0^{(\ell)}u$ among the upper coefficients, and every upper backward
coefficient $v$ has its exact image $W_0^{(\ell)\top}v$ among the
lower coefficients. Both members are approximated with their own
coordinate error bound. This is stronger than inferring a coordinate
bound from an operator norm.

Let $S_\ell\subset\mathbb R^n$ be the real span of all these
coefficients belonging to layer $\ell$. Include $h_a^{(\ell)}(0)$
in $S_\ell$, and $W_0^{(\ell)}h_a^{(\ell-1)}(0)$ in $S_\ell$
for $\ell\ge2$. Include the $d$ columns of $A_0$ in $S_1$.
Then $\dim S_\ell\le R=C\lambda^{d(L+5)+1}$. No invariant finite
feature space is being assumed: these spaces approximate the actual
moving sources for the whole required finite time window.

## 3. Coordinated neuron selection and the autonomous model

Choose real bases $U_\ell$ satisfying $U_\ell^\top U_\ell/n=I$.
Positive cubature on the constant and all pairwise products of their
columns gives a subset $I_\ell$ and diagonal positive masses $D_\ell$
such that

\[
 |I_\ell|\le1+R(R+1)/2,\qquad
 \mathbf1^\top D_\ell\mathbf1=1,\qquad
 U_{\ell,I_\ell}^\top D_\ell U_{\ell,I_\ell}=I.
                                                        \tag{10}
\]

To obtain these masses start with mass $1/n$ at each original neuron.
If there are more support points than matched scalar moments, a linear
dependence among their moment vectors gives a signed mass change
preserving every moment. Move along it until a mass reaches zero and
repeat. Positivity and exact moment matching persist. No random
independent resampling occurs.

Set $A_C(0)=A_{0,I_1}$, $w_C(0)=0$, and

\[
 B_C^{(\ell)}(0)=U_{\ell,I_\ell}
    \frac{U_\ell^\top W_0^{(\ell)}U_{\ell-1}}n
    U_{\ell-1,I_{\ell-1}}^\top D_{\ell-1}.             \tag{11}
\]

The reduced forward pass uses the same activations and these smaller
matrices, and its prediction is $w_C^\top D_Lh_C^{(L)}$. The adjoint
of an edge is
$B^{(\ell)*}=D_{\ell-1}^{-1}B^{(\ell)\top}D_\ell$.
Compute $c_{C,a}=y_a-f_C(x_a)$ and all backward responses using only
this model. Its exact autonomous flow is

\[
 \dot A_C=\frac2m\sum_a c_{C,a}\delta_{C,a}^{(1)}v_a^\top,
 \quad \dot B_C^{(\ell)}=\frac2m\sum_a c_{C,a}
       \delta_{C,a}^{(\ell)}h_{C,a}^{(\ell-1)\top}D_{\ell-1},
 \quad \dot w_C=\frac2m\sum_a c_{C,a}h_{C,a}^{(L)}.    \tag{12}
\]

There is no original-width object, basis, trained reference value or
external residual in (12). Retain only the small first weights, small
hidden matrices, readout, masses, fixed activations and training data.
The total count is

\[
 d|I_1|+\sum_{\ell=2}^L|I_\ell||I_{\ell-1}|+|I_L|
       +\sum_\ell|I_\ell|+O(md+m)
             \le CR^4.                               \tag{13}
\]

Including a stored copy of each small initialized matrix only changes
the constant. Thus (9) gives (4). This counts the smaller learned dense
matrices as well as their neuron coordinates.

The isometries in (10) make (11) contractive in the weighted operator
norm. Paired source images give exact initial training features, by
forward induction, and exact initialized readout Gram. The original
and reduced flows therefore both satisfy the small-label fitting proof:
bounded residual activity controls hidden displacement by $CY^2$,
preserves the positive readout Gram, and gives residual decay
$\rho(t)\le Ye^{-\kappa t}$. This proof has no dependence on the
smallest selected mass or number of selected neurons.

## 4. Full same-time error, including selection bias

Apply `GENERAL_WEIGHTED_COMPARISON.md` to (6)--(12). Its proof uses
all original/reduced pairing defects, both matrix orientations, all
hidden updates and both models' own residuals. In particular it does
not compare independent realizations, or compare either model to an
unproved population limit.

Let $M$ be the actual original carrier maximum on $[0,T]$, enlarged
to at least one. The deterministic result gives

\[
 \sup_{t\le T,x}|f_C(t,x)-f_n(t,x)|
        \le C(1+M)e^{CM}\epsilon.                    \tag{14}
\]

The essential damping equation is the exact difference of the two
residual flows, $\dot u=-(2/m)K_Cu-(2/m)(K_C-K_n)c_n$.
Both tangent Grams are their actual moving Grams. Positivity of $K_C$
controls the integrated residual difference. The remaining state
comparison is amplified by residual activity $\int\rho_n\le CY$,
not by $T$. Multiplying each changed backward gate by the true original
carrier gives the factor $M$ only once per depth recursion. This is
why a modest width-dependent intermediate amplification is affordable.

On the finite-network carrier event $M\le C_0\sqrt\lambda$, choose
$D$ in (7) larger than the constant multiplying $\sqrt\lambda$ in
(14). Then (14) is at most $C/\sqrt n$, with a width-independent
constant. Both models have sphere-uniform tails $CYe^{-\kappa T}$
by their own fitting argument. Taking $C_T$ sufficiently large proves
(5), including the limit $t=\infty$. No trajectory is frozen at $T$.
Selection bias is part of (14); no population-centering term is omitted.

## 5. Concrete data, activations and feature learning

The activation class contains tanh, the logistic sigmoid, erf, arctan,
and sine, as well as fixed finite sums and affine rescalings that retain
a common strip. Here are direct bounds. Tanh and sigmoid have no poles
on a sufficiently narrow closed horizontal strip and are uniformly bounded
there from their exponential formulas. For erf, integration vertically
from the real axis gives
$|\operatorname{erf}(x+iy)|\le1+(2/\sqrt\pi)|y|e^{y^2}$.
For arctan on $|y|\le b<1$, its derivative
$1/(1+z^2)$ has magnitude at most $1/(1-b^2)$, so the analogous
bound is $\pi/2+b/(1-b^2)$. Finally
$|\sin(x+iy)|^2=\sin^2x+\sinh^2y\le\cosh^2b$.
In particular, monotonicity and nowhere-zero slopes are unnecessary.

For nonconstant activations in this class the Gram assumption is
automatic if the nonzero training inputs are pairwise nonproportional.
This is the manuscript's initialized-data criterion, with the same proof:
if $\sum_a b_a\phi_1(u^\top v_a)=0$ identically and $b_a\ne0$,
choose for each $j\ne a$ a direction orthogonal to $v_j$ but not
to $v_a$. Taking the corresponding $m-1$ finite differences kills
every term except the $a$th. All $(m-1)$-fold scalar finite differences
of $\phi_1$ then vanish. Mollifying and differentiating in the increments
shows that each mollification is a polynomial of degree at most $m-2$;
interpolation at $m-1$ real points and convergence of the mollification
give the same conclusion for $\phi_1$. A bounded nonconstant function
cannot be such a polynomial. For $m=1$ its nonzero Gaussian square
expectation suffices. Full support of the first Gaussian input converts
a zero Gram quadratic form to the preceding continuous identity.
After this first layer, a positive definite Gaussian covariance has
full support on $\mathbb R^m$; varying one coordinate in
$\sum_a b_a\phi_\ell(z_a)=0$ proves every $b_a=0$.
This propagates positivity through all hidden layers. On the sphere,
distinct points without antipodal pairs satisfy nonproportionality.
Thus there is no requirement $m\le d$ in this joint result.

The reduced dynamics train every hidden matrix. A direct feature-motion
certificate is also available in a substantial subcase: linearly
independent training inputs, nonconstant activations, and nonzero labels.
At initialization put
$v=\dot w(0)=(2/m)\sum_a y_ah_a^{(L)}(0)$,
$p_a^{(\ell)}=\dot k_a^{(\ell)}(0)$, and
$d_a^{(\ell)}=\dot\delta_a^{(\ell)}(0)$. Then $p_a^{(L)}=v$,
$d_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)}(0))\odot p_a^{(\ell)}$,
and $p_a^{(\ell)}=W_0^{(\ell+1)\top}d_a^{(\ell+1)}$.
Every initialized slope is nonzero almost surely: the derivative zeros
of a nonconstant analytic activation are discrete and initialized
preactivations have nondegenerate Gaussian laws conditionally layer by
layer. The same reasoning gives nonzero activation vectors. Gaussian
hidden matrices are invertible almost surely. The Gram gap gives $v\ne0$,
so all $d_a^{(1)}$ are nonzero. Linear independence of the $v_a$ implies
$\ddot A(0)=(2/m)\sum_a y_a d_a^{(1)}v_a^\top\ne0$.

The prefix energy identity is

\[
 \frac2m\sum_a y_a
       \frac{p_a^{(\ell)\top}\ddot h_a^{(\ell)}(0)}n
 =\frac{\|\ddot A(0)\|_F^2}{n}
        +\sum_{s=2}^\ell\|\ddot W^{(s)}(0)\|_F^2>0.
                                                        \tag{15}
\]

All hidden velocities initially vanish. Differentiate the forward pass
twice, pair with $p_a^{(\ell)}$, and use the backward adjoints to
move the lower-prefix term down one layer. The current-edge term equals
$\|\ddot W^{(\ell)}(0)\|_F^2$ by (2). The first-layer term is
$\|\ddot A(0)\|_F^2/n$, also for nonorthogonal inputs. This proves
(15) by induction. Every hidden feature layer therefore moves. Adding
the finitely many vectors $d_a^{(\ell)}$ and their initialized reverse
images to the cubature spaces preserves $\ddot A$'s positive weighted
norm and the same identity in the smaller model. It does not change the
state exponent. This is an exact nonzero-motion certificate, not a
width-independent lower bound on its magnitude, nor a claim that motion
benefits unseen labels. The previous two-layer theorem supplies a separate
width-independent motion bound in its stated subcase.

## 6. Status and limitations

The deterministic comparison is proved in `GENERAL_WEIGHTED_COMPARISON.md`
and fully reconstructed in `GENERAL_WEIGHTED_COMPARISON_CHECK.md`.
The actual source theorem is proved in `DEEP_COMPLEX_SOURCE.md` and
`DEEP_ACTIVATION_EXTENSION.md`; their complete reconstruction is
`DEEP_COMPLEX_SOURCE_CHECK.md`. The initialization-only approximation,
positive selection, state count, same-time bound, endpoint transfer and
additional claims in this file were fully reconstructed in
`GENERAL_ANALYTIC_COMPRESSION_CHECK.md`. That check verifies the assembly
as an implication from its named source theorem; the separate source
check proves that the input has actually been supplied. The coordinator
read and reconstructed the entire chain and all complete reports;
`GENERAL_COMPRESSION_COORDINATOR_CHECK.md` records versions and scope.
No extra source-regularity assumption remains in the stated theorem.

This theorem does not prove the same result for
every bounded-$C^3$ activation, for growing $d,m,L$, or with efficient
bounded-precision preprocessing. It is not a population-limit theorem,
nor an unchanged-order-$q$ compression theorem. These distinctions are
part of the result's mathematical scope.

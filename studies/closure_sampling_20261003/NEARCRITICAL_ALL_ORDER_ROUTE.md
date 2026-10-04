# All initialized response orders from a positive covariance majorant

2026-10-04. Coordinator derivation in the current study. This closes an
all-orders initialization question left open by the earlier fixed-order
Hermite identities. It does not close the trained, finite-network response
estimate. The complete input is NEARCRITICAL_GEOMETRY_ROUTE.md, Sections
2, 4 and 6, read and reconstructed by the coordinator. No experiment or
external mathematical input is needed.

## 1. Activation and explicit constants

Fix a>0 and set

\[
 Q=a^2+2a/\sqrt\pi+1/3,\qquad
 D=a^2+2a/\sqrt\pi+2/(\pi\sqrt3),
\]
\[
 0<\chi\le D/Q,\qquad
 \phi(z)=\sqrt{\chi/D}\,[az+\operatorname{erf}(z/\sqrt2)]
                 \mathbin{\pm}\sqrt{1-\chi Q/D}.
 \tag{1}
\]

This is an unbounded nonlinear entire, real Lipschitz activation. It has
E phi(Z)^2=1 and E phi'(Z)^2=chi. Its Gaussian covariance map is

\[
 F(c)=1-\chi Q/D+\frac\chi D
 \left[(a^2+2a/\sqrt\pi)c+\frac2\pi\arcsin(c/2)\right].
 \tag{2}
\]

The power series at zero has nonnegative coefficients and radius two;
F(1)=1 and F'(1)=chi. At depth L>=1 write

\[
 K_L=F^{\circ L},\quad S_L=\sum_{j=0}^{L-1}\chi^j,\quad
 B=\frac{24\chi}{7\pi\sqrt7 D},\quad
 r_L=\min\left\{\frac1{4\max(1,\chi^L)},
                         \frac\chi{4B S_L}\right\}.
 \tag{3}
\]

All constants in (1)--(3) are explicit; r_L is a covariance increment,
not an input-space radius. The input-space radius below is proportional
to its square root.

## 2. Every covariance derivative is bounded at once

For every integer k>=1,

\[
 \frac{K_L^{(k)}(1)}{k!}
       \le 2\chi^L r_L^{1-k}.
 \tag{4}
\]

In particular, at chi=1 set

\[
 c_a=\min\{1/4,\ 7\pi\sqrt7D/96\}>0.
\]

Then r_L>=c_a/L, and simultaneously for all L,k>=1,

\[
 \frac{K_L^{(k)}(1)}{k!}\le2(L/c_a)^{k-1}.
 \tag{5}
\]

The right side controls the order dependence as well as the depth
dependence. Thus it can be summed in a positive-radius Taylor series;
a list of separate fixed-k asymptotics would not justify that step.

To prove the claims, the explicit derivative of (2) gives
F''(u)<=B on [1,3/2]. For e in [0,1/2],

\[
 F(1+e)-1\le\chi e+(B/2)e^2.
 \tag{6}
\]

Start e_0=r_L and put e_(j+1)=F(1+e_j)-1. The recursion is well
defined through depth L, and e_j<=2chi^j e_0<=1/2. Here is the
short majorant argument, including the needed bootstrap. Put
u_j=e_j/chi^j. Assuming u_j<=2e_0 through a given prefix, (6) gives

\[
 u_{j+1}-u_j\le (B/(2\chi))\chi^j u_j^2.
\]

Summing the prefix bounds gives
u_(j+1)<=e_0+(2B/chi)e_0^2 S_L<=3e_0/2. The other part of (3)
keeps every resulting e_j at most one half, so the bootstrap extends
through all L. In particular,

\[
 K_L(1+r_L)-1\le2\chi^L r_L.
 \tag{7}
\]

The nonnegative power coefficients of F give nonnegative power
coefficients of every finite composition, wherever the defining series
converges absolutely. Monotone summation and the finite scalar recursion
just proved show absolute convergence at 1+r_L. Expanding each monomial
about one then gives nonnegative Taylor coefficients there. For a fully
explicit justification, use the binomial theorem at 1+u with
0<=u<r_L and exchange the two sums by nonnegativity. The coefficients
are finite because their nonnegative sum at r_L is bounded by (7).
This also proves analyticity about one for |u|<r_L, and identifies the
coefficients as K_L^(k)(1)/k!. Each individual nonconstant term is no
larger than the entire nonconstant sum at r_L. Inequality (4) follows
from (7). At chi=1, (3) gives r_L=min(1/4,7pi sqrt(7)D/(96L)),
which proves (5).

## 3. All initialized angular derivatives in the feature Hilbert space

Expand K_L(c)=sum_j p_(L,j)c^j, with p_(L,j)>=0 and sum_j p_(L,j)=1.
For a real unit input v define the population feature realization

\[
 \Phi_L(v)=\bigoplus_{j\ge0}\sqrt{p_{L,j}}\,v^{\otimes j}.
 \tag{8}
\]

Its inner product is K_L(v^top w). Complexify each tensor space using
the Hermitian inner product. Then, wherever the series is finite,

\[
 \|\Phi_L(v)\|^2=K_L(v^*v).
 \tag{9}
\]

Fix orthonormal real v,u and let v(theta)=v cos(theta)+u sin(theta)
for complex theta. It satisfies
v(theta)^*v(theta)=cosh(2 Im theta). Set

\[
 \tau_L=\frac12\sqrt{r_L}.
 \tag{10}
\]

Because r_L<=1/4, we have tau_L<=1/4. The elementary power-series
bound cosh(2t)-1<=4t^2 for |t|<=1/2 shows that
cosh(2 Im theta)<=1+r_L on this closed strip. Thus (7) and (9) give

\[
 \sup_{|\operatorname{Im}\theta|\le\tau_L}
       \|\Phi_L(v(\theta))\|^2
 \le1+2\chi^L r_L\le3/2.
 \tag{11}
\]

The function is Hilbert-space holomorphic on the open strip. Indeed,
on each smaller closed strip, the nonnegative norm tail in (9)
converges uniformly by domination with the convergent scalar series
at 1+r_L. Finite tensor sums are holomorphic; their uniform convergence
on compact subsets proves the asserted Hilbert holomorphy. Applying
the scalar Cauchy formula to every continuous linear functional of norm
one, then taking the supremum, gives for every real theta and k>=0

\[
 \frac1{k!}\left\|\frac{d^k}{d\theta^k}
                   \Phi_L(v(\theta))\right\|
 \le\sqrt{3/2}\left(\frac2{\sqrt{r_L}}\right)^k.
 \tag{12}
\]

For k>0 first apply the bound on a circle of radius strictly below
tau_L, then take its radius up to tau_L. At chi=1 the right side is
at most sqrt(3/2)[2sqrt(L/c_a)]^k. This is a uniform all-order
angular estimate with a polynomial-depth analytic radius.

## 4. Scope of the advance

Equations (4) and (12) control all derivative orders of the initialized
population feature map, including unbounded activations of ordinary
forward scale and tunable derivative gain. They are not statements about
an independent scalar product of gates. Mixing has already been included
through the Gaussian covariance composition.

The actual finite-network trained response remains a different object.
In particular NORMALIZED_COMPLEX_FINITE_WIDTH_AUDIT.md proves that, for
the same activations and every finite n, a second-layer feature at any
fixed nonreal great-circle query has infinite unconditional second
moment. Thus (11) cannot be used as an unconditional finite-n complex
moment bound. It can motivate a stopped high-probability proof, but does
not supply one, and it does not estimate the adaptive mixed product
phi''(z) R_a J during training. No improved label cap, runtime error,
storage count, or compression impossibility follows from this note alone.

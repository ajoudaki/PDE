# A uniformly small force can have a fixed eventual exponent

2026-09-19. Auxiliary scalar example for the current rate-limit question.
This is not the population closure and is not a canonical trajectory
counterexample. It distinguishes a fixed late exponent from a uniform
from-start accuracy guarantee. No external scientific input is used.

Take L(x)=x^4, x(0)=1. Ordinary GF is x'=-4x^3, with
x^0(t)=(1+8t)^(-1/2). For 0<epsilon<=1 consider the smooth perturbation

\[
 x_\varepsilon'=-4x_\varepsilon^3
                   -\varepsilon\tanh(x_\varepsilon/\varepsilon).
 \tag{1}
\]

The deviation of its vector field from GF is bounded by epsilon over
the entire real line, for all times. Every trajectory stays in (0,1]
at finite positive times and decreases to zero. Indeed the right-hand
side is locally Lipschitz, vanishes at zero, and is strictly negative
for positive x; uniqueness prevents crossing zero, boundedness gives
continuation, and a strictly positive limiting x would have a uniformly
negative velocity, a contradiction.

For completeness the finite-horizon approximation has the direct bound

\[
 0\le x^0(t)-x_\varepsilon(t)\le\varepsilon t.
 \tag{2}
\]

To check the lower inequality without invoking a comparison theorem,
write q=x^0-x_epsilon and subtract the equations:

 q'=-4[(x^0)^2+x^0 x_epsilon+x_epsilon^2]q
       +epsilon tanh(x_epsilon/epsilon),  q(0)=0.

Multiplying by the positive integrating factor gives q>=0. Consequently
q'<=epsilon, giving the upper inequality. Thus this is a globally small
force and a compact-time GF approximation, with no delayed activation.

Nevertheless at every fixed epsilon>0,

\[
 -\frac{d}{dt}\log L(x_\varepsilon(t))
 =16x_\varepsilon(t)^2+
 4\frac{\tanh(x_\varepsilon(t)/\varepsilon)}
        {x_\varepsilon(t)/\varepsilon}
 \longrightarrow4,
\]
\[
 \lim_{t\to\infty}\frac1t\log L(x_\varepsilon(t))=-4.
 \tag{3}
\]

The first limit uses x_epsilon(t)->0 and tanh(u)/u->1. Integrating the
logarithmic derivative proves the second: its average differs from four
by an arbitrarily small tail bound plus a finite initial integral divided
by t. The exponent therefore does not vanish in the small-force limit.

There is still an explicit diverging warmup bound. Let

\[
 B_\varepsilon=
 \left(\frac18+\frac1{\tanh1}\right)\varepsilon^{-2/3}.
\]

Equation (2) shows the time to x<=epsilon^(1/3) is at most
(epsilon^(-2/3)-1)/8. While epsilon<=x<=epsilon^(1/3), the speed toward
zero is at least epsilon tanh(1), so the additional time is at most
epsilon^(-2/3)/tanh(1). Thus x<=epsilon by time B_epsilon.
For 0<=u<=1, tanh(u)>=u tanh(1): the derivative of
tanh(u)/u is nonpositive because tanh(u)-u sech²(u) has derivative
2u sech²(u)tanh(u)>=0 and value zero at u=0. Hence after B_epsilon,

\[
 L(x_\varepsilon(t))
 \le \varepsilon^4
      e^{-4\tanh(1)(t-B_\varepsilon)},\qquad t\ge B_\varepsilon.
 \tag{4}
\]

This bound exposes a fixed exponent and a potentially enormous prefactor.
More intrinsically, no estimate C exp(-lambda t), with fixed finite C
and lambda>0 uniform in epsilon, can hold: (2) would transfer it to
(1+8t)^(-2), and e^(lambda t)/(1+8t)^2 is unbounded.

The lesson is precise. Uniformly small forces do not force the eventual
exponent to vanish. They cannot turn a slower limiting GF into an
epsilon-uniform exponential estimate with bounded prefactor. In this
example the perturbation supplies a linear restoring force inside a
shrinking region x=O(epsilon); reaching that region is not uniformly
fast. A corresponding construction for the actual closure would need
a proof of access to, and control within, an appropriate fitting region.
It is not established by this scalar calculation.

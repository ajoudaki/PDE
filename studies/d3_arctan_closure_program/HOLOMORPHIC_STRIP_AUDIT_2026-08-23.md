# Audit: holomorphic-strip and complex-Gaussian closure

## Verdict

Complex analyticity does not provide a width-uniform shortcut to the missing
response estimate.  Three different versions fail:

1. a coordinatewise complex strip must shrink at least on the natural
   \(n^{-1/2}\) scale under aligned column perturbations;
2. an \(\ell_2\) complex tube gives operator-direction control but not the
   Hilbert--Schmidt column response needed by Gaussian divergence;
3. arctan and its natural-coordinate inverse have genuine complex
   singularities whose Gaussian \(L^p\) integrability is worse than the
   desired real-variable estimate.

These are no-go results for an analytic proof method, not counterexamples to
the real canonical flow.

## Meromorphic obstruction

The real activation is benign,

\[
 \phi(z)=\arctan z,\qquad \phi'(z)=\frac1{1+z^2},
\]

but its holomorphic continuation has poles/branch singularities at
\(z=\pm i\).  Consequently a complex Gaussian perturbation of a real
preactivation can approach a pole with positive planar density.  Negative
powers of the distance to the pole are not integrable at the orders needed
for a \(p\asymp\log n\) hierarchy.  In particular, treating \(B_3\) itself as
a complex-Gaussian holomorphic observable does not yield even a uniform
second-moment Cauchy bound.

The natural coordinate

\[
 \Theta(u)=u+\frac{u^3}{3}
\]

does not remove this complex obstruction.  Its inverse branches become
singular where \(\Theta'(u)=1+u^2=0\), again at \(u=\pm i\).  The derivative of
the inverse has nonintegrable complex-Gaussian powers already at finite
orders (in particular at the fourth-moment level).  Thus a proof cannot move
to the cubic coordinate, complexify, and appeal to a dimension-free
holomorphic Gaussian estimate.

## Shrinking coordinatewise strip

There is also a purely differential obstruction before one reaches the
poles.  At initialization, choose a perturbation of one raw middle column
whose coordinate signs align with the relevant backpropagated vector.  In
the exact differentiated equations, the mixed time/disorder derivative of a
tagged middle preactivation contains a term of the form

\[
 \partial_tD_s Z_{2,j}(0)
 =c_n\sqrt n\,d(Z_{2,j})H_{jj}
   +e_j^\top H D_2v,
\qquad
c_n=\frac{\|b\|_1}{n},
\]

where \(H\) is a positive Gram-type block
\(\alpha I+G_1D_1^2G_1^*\); on an event of nonvanishing probability
\(c_n\) is bounded below and the second term is only order one.  A positive
fraction of coordinates therefore have an order-\(\sqrt n\) aligned
derivative.

Schwarz--Pick or Cauchy control in a coordinatewise strip would bound such a
derivative by the reciprocal strip radius.  Hence after any fixed positive
time the radius certified by this route is at most \(C/(t\sqrt n)\).  Cauchy
estimates on that strip reproduce, rather than eliminate, the forbidden
\(\sqrt n\) loss.  The calculation is a method obstruction: it uses an
aligned direction, not the random signed Frobenius average whose canonical
law may still be controlled.

## Why an \(\ell_2\) tube is too weak

Replacing the polydisc by an \(\ell_2\) tube controls the derivative in one
unit direction.  Gaussian divergence needs the square sum over all \(n\)
column-coordinate derivatives.  Even the linear map \(F(w)=aw\) has
directional operator norm \(|a|\) but derivative Hilbert--Schmidt norm
\(|a|\sqrt n\).  No holomorphic inequality converts the former into the
latter without a trace, rank, or target-specific covariance input.  That
missing input is precisely the response-delocalization/covariant-response
problem.

## Consequence

Real analyticity of arctan remains useful for finite Taylor identities and
exact characteristic cancellations.  It does not supply a uniform complex
domain or an off-the-shelf hypercontractive estimate for the continuous
trained flow.  Any viable proof must operate on the real signed response and
exploit its canonical source/covariance structure before taking absolute
values.

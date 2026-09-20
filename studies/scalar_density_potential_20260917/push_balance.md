# Exact dilation balance: a circulation obstruction

This is a scoped, fresh theoretical attempt using only the supervisor's supplied
model and the required mathematical-process skills. No other research artifacts,
external sources, or experiments were used. The target is an unconditional,
state-only exponential potential for the genuine three-sample canonical flow.
That target remains open in this attempt. The results below concern the exact
upper-layer balance route; they are not a counterexample to the canonical flow.

## 1. Exact identity and its functional setting

Let the upper variable have law \(\mu\), write
\(\langle f,h\rangle=\int fh\,d\mu\), and set
\[
 D h(b)=b\partial_bh(b),\qquad H_s(b)=\tanh(sb).
\]
The canonical upper variable is
\[
 b=B\tanh(\sqrt\nu Z),\qquad B=(\tau+\eta)^{-1/2},
\]
so \(\mu\) is even, has positive density on \((-B,B)\), and assigns zero mass to
\(b=0\). Its density, with \(z=b/B\), is
\[
 \rho(b)=\frac{\exp[-\operatorname{arctanh}(z)^2/(2\nu)]}
 {B\sqrt{2\pi\nu}(1-z^2)}.
\]
For smooth bounded functions and derivatives, integration by parts is valid:
\(b\rho(b)\) vanishes at both endpoints, since its logarithmic Gaussian decay
dominates every power of the distance to the endpoint. It gives
\[
 D^*=-D-\bigl(1+b\partial_b\log\rho\bigr).
\]
In particular, \(D\) is not self-adjoint in the actual upper \(L^2(\mu)\).
Its symmetric part is multiplication by
\[
 S(b)=-\frac12\bigl(1+b\partial_b\log\rho(b)\bigr).
\]
This multiplier is negative at zero and tends to positive infinity at the
support endpoints. Therefore replacing dilation by its symmetric part does not
give a positive quadratic energy either.

Writing \(h_i=Ma_i\), the supplied equations imply
\[
 \dot c=-2\sum_i p_i r_iH_{h_i},\qquad
 M\dot M=-2\sum_i p_i r_i\langle c,DH_{h_i}\rangle
          =\langle c,D\dot c\rangle.
 \tag{1}
\]
The equality uses \(DH_{Ma_i}=bMa_i\operatorname{sech}^2(bMa_i)\), including
the signs of \(M\) and \(a_i\). No division by these quantities is needed.

Set \(m=M^2/2\). Then (1) reads
\[
 dm=\omega_c(dc),\qquad \omega_c(h)=\langle c,Dh\rangle.
 \tag{2}
\]
The question is whether this one-form can be integrated into a state-only
readout correction, possibly nonlinear or nonlocal in \(b\).

## 2. Genuine tanh profiles have strictly nonzero circulation

Choose any \(0<s<t\), and let \(u=H_s\), \(v=H_t\). Define
\[
 K=\langle u,Dv\rangle-\langle v,Du\rangle.
\]
For \(b\ne0\),
\[
 \frac{DH_s(b)}{H_s(b)}=\frac{2sb}{\sinh(2sb)}.
\]
The function \(x/\sinh x\) is even and strictly decreasing for \(x>0\): its
derivative has numerator \(\sinh x-x\cosh x\), whose derivative is
\(-x\sinh x<0\) and whose value at zero is zero. Thus
\[
 u(b)Dv(b)-v(b)Du(b)
 =u(b)v(b)\left[\frac{2tb}{\sinh(2tb)}
                    -\frac{2sb}{\sinh(2sb)}\right]<0
\]
for every \(b\ne0\). Both factors \(u,v\) have the same sign. Integrating yields
\[
 K<0. \tag{3}
\]
This conclusion holds for the exact canonical upper law; it does not depend on
a Gaussian surrogate, an endpoint approximation, or a polynomial replacement
of tanh.

The differential of \(\omega\) on the two-dimensional plane
\(\operatorname{span}\{u,v\}\) is nonzero:
\[
 (d\omega)(u,v)=\langle u,Dv\rangle-\langle v,Du\rangle=K.
\]
Consequently there is no \(C^2\) functional \(Q(c)\), even allowing dependence
on the entire readout and its derivatives, such that
\[
 dQ(c)[h]=\langle c,Dh\rangle
\]
for all \(c,h\) in this plane. Indeed, differentiating in the two orders would
require its symmetric Hessian to satisfy
\(\langle u,Dv\rangle=\langle v,Du\rangle\), contradicting (3).
The obstruction is not limited to quadratic norm corrections.

There is a related statement for general nonlinear invariants of (2). On
coordinates \((x,y,m)\), with \(c=xu+yv\), the two controlled tangent fields are
\[
 V_u=\partial_x+\langle xu+yv,Du\rangle\partial_m,\qquad
 V_v=\partial_y+\langle xu+yv,Dv\rangle\partial_m.
\]
Their bracket is \([V_u,V_v]=K\partial_m\). If a \(C^2\) state function
\(F(x,y,m)\) were constant for every path satisfying (2), then
\(V_uF=V_vF=0\), hence \(K\partial_mF=0\). Equation (3) gives
\(\partial_mF=0\), and the first two equalities then give
\(\partial_xF=\partial_yF=0\). Such a universal invariant is locally constant.

The quantifier “every path satisfying (2)” matters. This rules out deriving an
invariant from the dilation identity alone. It does not exclude an invariant or
monotone function that uses additional restrictions of the actual residual and
lower-layer dynamics.

## 3. Canonical zero readout and finite energy do not remove circulation

There is an explicit smooth path satisfying (1), starting at the canonical
\(c(0)=0\) and any prescribed \(M(0)=M_0>0\), for which the readout stays in a
bounded two-dimensional set, total kinetic energy is finite, but \(M\) diverges.
This path is a stress test of the balance argument, not a solution of the
training equations.

For an amplitude \(R>0\), put
\[
 c_\theta=R[(\cos\theta-1)u-\sin\theta\,v],\qquad \theta\ge0.
\]
Set
\[
 \Psi(\theta)=R^{-2}\int_0^\theta
       \langle c_\alpha,D\partial_\alpha c_\alpha\rangle\,d\alpha.
\]
To calculate its increment, abbreviate
\(A=\langle u,Du\rangle\), \(B_1=\langle u,Dv\rangle\),
\(C_1=\langle v,Du\rangle\), and \(E=\langle v,Dv\rangle\). Then
\[
 \Psi'(\theta)=
 -A(\cos\theta-1)\sin\theta
 -B_1(\cos\theta-1)\cos\theta
 +C_1\sin^2\theta+E\sin\theta\cos\theta.
\]
The integral over a period is
\[
 \Psi(2\pi)=\pi(C_1-B_1)=-\pi K>0.
\]
Hence
\[
 \Psi(\theta)=\kappa\theta+P(\theta),\qquad
 \kappa=-K/2>0,
\]
where \(P\) is a bounded smooth \(2\pi\)-periodic function with \(P(0)=0\).
Choose \(R\) small enough that
\(R^2\|P\|_\infty\le M_0^2/4\), and define
\[
 \theta(t)=\log(1+t),\qquad
 m(t)=M_0^2/2+R^2\Psi(\theta(t)),\qquad
 M(t)=\sqrt{2m(t)},\qquad c(t)=c_{\theta(t)}.
 \tag{4}
\]
Then \(m(t)\ge M_0^2/4\), so the square root is smooth and positive. Direct
differentiation verifies \(M\dot M=\langle c,D\dot c\rangle\). Furthermore,
\[
 M(t)^2=2R^2\kappa\log(1+t)+O(1)\longrightarrow\infty.
 \tag{5}
\]
The readout and every fixed-order derivative with respect to \(b\) are uniformly
bounded, because \(c\) stays in a bounded subset of the fixed span of \(u,v\).
Also \(\dot\theta=(1+t)^{-1}\), so
\[
 \int_0^\infty\|\dot c(t)\|_{L^2(\mu)}^2\,dt<\infty,
 \qquad
 \int_0^\infty\dot M(t)^2\,dt<\infty.
\]
For the second assertion use
\(\dot M=R^2\Psi'(\theta)/[(1+t)M]\), the boundedness of \(\Psi'\), and the
positive lower bound for \(M\). Both integrals can be made arbitrarily small by
decreasing \(R\).

One can therefore define a nonnegative decreasing *abstract* energy
\[
 \mathcal E(t)=1-\int_0^t
       [\|\dot c(s)\|_2^2+\dot M(s)^2],ds
\]
by taking \(R\) sufficiently small. It satisfies the usual kinetic dissipation
identity and, by Cauchy–Schwarz,
\[
 \|c(t)\|_2^2\le t[1-\mathcal E(t)],\qquad c(t)=o(\sqrt t).
\]
Thus the exact dilation identity, canonical zero readout, finite total kinetic
energy, and these readout growth bounds jointly permit (5).

There is a decisive limitation: \(\mathcal E\) has not been identified with the
neural squared loss. In fact, at every complete loop \(c=0\), so the neural loss
would be one again; strict dissipation precludes this for a nonconstant actual
trajectory. Consequently (4) is not a counterexample to training convergence or
to existence of the requested exponential potential. It shows precisely why
the balance-and-energy identities alone are insufficient.

## 4. What a successful repair must add

The antisymmetric contribution
\[
 \int_0^t\langle c,A\dot c\rangle\,ds,
 \qquad A=(D-D^*)/2,
\]
is a signed area of the readout path. Writing \(D=S+A\) gives the exact relation
\[
 \frac{M(t)^2-M_0^2}{2}
 =\frac12\langle c(t),Sc(t)\rangle
   +\int_0^t\langle c,A\dot c\rangle\,ds,
 \tag{6}
\]
whenever the functions are in the above smooth domain. The zero initial readout
was used in the first term. A derivative penalty, monotone rearrangement, or
nonlocal functional of the current readout cannot universally replace the area
term by an exact endpoint correction: the loop calculation already contradicts
that possibility. Adding the area as a new evolving variable records history
and does not itself provide a coercive state-only functional of the original
model.

A repair may still exploit the actual relation
\(\dot c=-2\sum_i p_i(f_i-y_i)H_{Ma_i}\), its coupling to the evolving lower
distribution, and the exact squared-loss formula. This attempt has not proved a
sign or a coercive bound for the area term under those restrictions. It has also
not proved that canonical readout shapes remain in any invariant monotonicity
cone. Those are missing dynamical claims, not consequences of (1).

The established conclusion is limited but exact: no nonlinear readout-only
integration of the universal dilation balance supplies the desired invariant;
even finite energy and canonical zero readout do not repair that route. The
unconditional exponential-potential target remains unresolved.

# The Euler consistency forcing and its variational propagation

This note establishes two scoped facts. For the canonical arctangent
network, the full Euler consistency source is small at
\(\eta=n^{-2}\), and its exact algebra identifies the remaining
signed curvature terms. Separately, an explicit bilinear-readout
gradient system disproves a width-independent bound on the
corresponding principal forced variational response based only on
bounded speed, finite action, and positive readout acceleration.
That example does not prove a discrepancy between the actual GD and
GF trajectories, and it is not a Gaussian arctangent-network example.

## Exact canonical consistency source

Use the canonical state
\(\theta=(z^{(1)},W^{(2)},W^{(3)},W^{(4)})\), with the forward
equations, backward vectors, and exact feature vector field \(G\)
of EXACT_GD_COERCIVITY.md. The parameter inner product is
\[
\langle \xi,\widetilde\xi\rangle_{\rm par}
=\frac{(\xi^{(1)})^{\mathsf T}\widetilde\xi^{(1)}}n
 +\operatorname{tr}((\Xi^{(2)})^{\mathsf T}\widetilde\Xi^{(2)})
 +\operatorname{tr}((\Xi^{(3)})^{\mathsf T}\widetilde\Xi^{(3)})
 +\frac{(\xi^{(4)})^{\mathsf T}\widetilde\xi^{(4)}}n,
\]
where \(\xi=(\xi^{(1)},\Xi^{(2)},\Xi^{(3)},\xi^{(4)})\).
Write \(\|\xi\|_{\rm par}^2=\langle\xi,\xi\rangle_{\rm par}\).
Then \(G=\nabla_{\rm par}f\),
\(H=DG\) is self-adjoint in this inner product, and
\[
K=\|G\|_{\rm par}^2
=\frac{\|h^{(3)}\|_2^2}{n}
 +\frac{(W^{(4)})^{\mathsf T}PW^{(4)}}n.
\]
Here
\[
\begin{aligned}
P=D_3\Bigg[
&\frac{\|h^{(2)}\|_2^2}{n}I\\
&+W^{(3)}D_2\left(
\frac{\|h^{(1)}\|_2^2}{n}I
 +W^{(2)}D_1^2(W^{(2)})^{\mathsf T}
\right)D_2(W^{(3)})^{\mathsf T}
\Bigg]D_3\succeq0.
\end{aligned}
\]
Physical gradient flow and its explicit Euler method have vector field
\[
\mathcal F(\theta)=2(1-f(\theta))G(\theta).
\]
The following identities are exact:
\[
D\mathcal F
=2(1-f)H-2G\otimes G,
\]
\[
D\mathcal F\,\mathcal F
=4(1-f)^2HG-4(1-f)K G,                                \tag{1}
\]
where \((G\otimes G)\xi=G\langle G,\xi\rangle_{\rm par}\).
The second term in (1) is tangent to the orbit. The first contains
the feature-flow acceleration \(HG\).

For completeness, the potentially troublesome components of \(HG\)
can be differentiated without a stability estimate. Put
\[
\beta^{(2)}=(W^{(3)})^{\mathsf T}\delta^{(3)},\qquad
\beta^{(1)}=(W^{(2)})^{\mathsf T}\delta^{(2)},
\]
and let \(u^{(\ell)}=Dz^{(\ell)}G\) denote actual feature-time
preactivation velocities. Thus \(u^{(1)}=\delta^{(1)}\) and
\[
u^{(2)}
=\left(\frac{\|h^{(1)}\|_2^2}{n}I
 +W^{(2)}D_1^2(W^{(2)})^{\mathsf T}\right)\delta^{(2)}.
\]
A dot below means a directional derivative along \(G\):
\[
\dot\delta^{(3)}
=D_3h^{(3)}
 +\phi''(z^{(3)})\odot u^{(3)}\odot W^{(4)},
\]
\[
\dot\delta^{(2)}
=D_2h^{(2)}\frac{\|\delta^{(3)}\|_2^2}{n}
 +D_2(W^{(3)})^{\mathsf T}\dot\delta^{(3)}
 +\phi''(z^{(2)})\odot u^{(2)}\odot\beta^{(2)},
                                                                    \tag{2}
\]
\[
\dot\delta^{(1)}
=D_1h^{(1)}\frac{\|\delta^{(2)}\|_2^2}{n}
 +D_1(W^{(2)})^{\mathsf T}\dot\delta^{(2)}
 +\phi''(z^{(1)})\odot\delta^{(1)}\odot\beta^{(1)}.
\]
The four components of \(HG\) are consequently
\[
\dot\delta^{(1)},\qquad
\frac{\dot\delta^{(2)}(h^{(1)})^{\mathsf T}
       +\delta^{(2)}(D_1\delta^{(1)})^{\mathsf T}}n,
\]
\[
\frac{\dot\delta^{(3)}(h^{(2)})^{\mathsf T}
       +\delta^{(3)}(D_2u^{(2)})^{\mathsf T}}n,\qquad
PW^{(4)}.                                                       \tag{3}
\]

On an orbit with width-independent hidden operator-norm bounds and
bounded \(\|W^{(4)}\|_2/\sqrt n\), the normalized Euclidean norms
of every \(\delta^{(\ell)},\beta^{(\ell)},u^{(\ell)}\) in these
displays are bounded independently of \(n\). The product inequality
\[
\frac{\|v\odot w\|_2}{\sqrt n}
\le\sqrt n\,\frac{\|v\|_2}{\sqrt n}
              \frac{\|w\|_2}{\sqrt n}
\]
and \(|\phi''|\le2\) therefore give, successively in (2)--(3),
\[
\|HG\|_{\rm par}\le C\sqrt n.                            \tag{4}
\]
The constant depends only on the stated orbit bounds. The readout
component in (3) has the sharper bound
\(\|PW^{(4)}\|_2/\sqrt n\le C\).
For the matrix components use the exact identity
\(\|vw^{\mathsf T}/n\|_{\rm F}
=(\|v\|_2/\sqrt n)(\|w\|_2/\sqrt n)\).

The finite-flow coercivity theorem supplies these orbit bounds
uniformly for the prescribed initialization on its high-probability
event. On that event, \(1-f\) and \(K\) are also uniformly bounded.
Thus (1) and (4) imply
\[
\|D\mathcal F\,\mathcal F\|_{\rm par}\le C\sqrt n.
\]
Integrating the exact physical acceleration gives the genuine
one-step consistency estimate, along the exact flow,
\[
\|\theta(t+\eta)-\theta(t)-\eta\mathcal F(\theta(t))\|_{\rm par}
\le\frac C2\,\eta^2\sqrt n.                             \tag{5}
\]
The sum of these local defect norms over a fixed physical interval
\([0,T]\) is at most \(C_T\eta\sqrt n=C_Tn^{-3/2}\).
This estimates production of error; no bound on its propagation is
used in, or implied by, (5).

## The exact error equation and remaining signed term

Let \(\bar\theta_\eta(t)\) be the piecewise-linear physical Euler
interpolation, \(\theta(t)\) the exact flow from the same initial
state, and \(E=\bar\theta_\eta-\theta\). On
\([k\eta,(k+1)\eta)\), write \(\tau=t-k\eta\). Exactly,
\[
E'=D\mathcal F(\theta)E+\mathcal N+\mathcal R_\eta,
\]
\[
\mathcal N
=\int_0^1
[D\mathcal F(\theta+vE)-D\mathcal F(\theta)]E\,dv,
\]
\[
\mathcal R_\eta
=-\int_0^\tau
D\mathcal F(\bar\theta_\eta(k\eta)
              +v\mathcal F(\bar\theta_\eta(k\eta)))
 \mathcal F(\bar\theta_\eta(k\eta))\,dv.                 \tag{6}
\]
Its principal frozen defect is
\(-\tau D\mathcal F\,\mathcal F\). The average of \(\tau\) on one
physical step is \(\eta/2\). Accordingly the precisely specified
principal forced variational problem is
\[
\zeta'
=D\mathcal F(\theta(t))\zeta
 -\frac12D\mathcal F(\theta(t))\mathcal F(\theta(t)),
\qquad \zeta(0)=0.                                     \tag{7}
\]
All subsequent assertions about (7) are assertions about this exact
linear problem. They do not replace (6) by a width-uniform
asymptotic expansion.

Its energy identity is
\[
\begin{aligned}
\frac12\frac d{dt}\|\zeta\|_{\rm par}^2
={}&2(1-f)\langle\zeta,H\zeta\rangle_{\rm par}
 -2\langle G,\zeta\rangle_{\rm par}^2\\
&-2(1-f)^2\langle\zeta,HG\rangle_{\rm par}
 +2(1-f)K\langle\zeta,G\rangle_{\rm par}.                \tag{8}
\end{aligned}
\]
To identify its curvature exactly, for any parameter variation
\(\xi\), define
\[
v^{(1)}=\xi^{(1)},\qquad
v^{(2)}=\Xi^{(2)}h^{(1)}+W^{(2)}D_1v^{(1)},\qquad
v^{(3)}=\Xi^{(3)}h^{(2)}+W^{(3)}D_2v^{(2)}.
\]
Twice differentiating the forward equations gives
\[
\begin{aligned}
\langle\xi,H\xi\rangle_{\rm par}
={}&\frac2n(\xi^{(4)})^{\mathsf T}D_3v^{(3)}
 +\frac2n(\delta^{(3)})^{\mathsf T}\Xi^{(3)}D_2v^{(2)}
 +\frac2n(\delta^{(2)})^{\mathsf T}\Xi^{(2)}D_1v^{(1)}\\
&+\frac1n\sum_i W_i^{(4)}\phi''(z_i^{(3)})
                   (v_i^{(3)})^2\\
&+\frac1n\sum_i\beta_i^{(2)}\phi''(z_i^{(2)})
                   (v_i^{(2)})^2
 +\frac1n\sum_i\beta_i^{(1)}\phi''(z_i^{(1)})
                   (v_i^{(1)})^2.                      \tag{9}
\end{aligned}
\]
In particular, even with the exact source (2), the signed middle
contribution in (8) is
\[
\frac{2(1-f)}n\sum_i
\beta_i^{(2)}\phi''(z_i^{(2)})
\bigl(v_i^{(2)}[\zeta]\bigr)^2.                         \tag{10}
\]
The first-layer term in (9) has the same issue. The identity
\(\phi''/\phi'=-2z/(1+z^2)\) replaces
\(\beta^{(2)}\phi''(z^{(2)})\) by a bounded scalar factor
times \(\delta^{(2)}\), but (10) still pairs it with the square
of the actual forced variation. The available mean-square and
action estimates do not bound that pairing by a width-independent
multiple of \(\|\zeta\|_{\rm par}^2\).
No cancellation of (10) against the third term of (8) has been
established for the Gaussian arctangent trajectory.

Equivalently, varying the readout acceleration identity itself gives
for a homogeneous feature-time variation
\[
\frac{d^2\xi^{(4)}}{ds^2}
=P\xi^{(4)}+(DP[\xi])W^{(4)}.                          \tag{11}
\]
The positivity of \(P\) does not assign a sign to the second term.
Equations (8)--(11), with the forcing fixed by (1)--(3), specify the
remaining comparison problem.

## Exact counterexample to a generic cancellation inference

The following example retains a bilinear readout and its positive
acceleration identity, but changes the feature map. It therefore
tests what follows from those structures alone, not what follows
from arctangent or Gaussian initialization.

For \(\lambda\ge1\), in three Euclidean coordinates \((x,y,c)\), set
\[
v=y-\frac{x^2}{2},\qquad
h_\lambda(x,y)
=1+x+\frac{x^3}{3}+xv+\frac1\lambda\log\cosh(\lambda v),
\qquad
f_\lambda(x,y,c)=c\,h_\lambda(x,y).                     \tag{12}
\]
Use Euclidean gradient ascent \(G_\lambda=\nabla f_\lambda\)
as feature flow, and physical flow
\(\mathcal F_\lambda=2(1-f_\lambda)G_\lambda\).
All coordinates initially equal zero.

With \(t_\lambda(v)=\tanh(\lambda v)\),
\[
\partial_xh_\lambda=1+v-x t_\lambda(v),\qquad
\partial_yh_\lambda=x+t_\lambda(v).
\]
Thus feature flow satisfies
\[
x'=c[1+v-x t_\lambda(v)],\qquad
y'=c[x+t_\lambda(v)],\qquad c'=h_\lambda,
\]
and
\[
v'=c[(1+x^2)t_\lambda(v)-xv].                          \tag{13}
\]
The curve \(v=0\) is exactly invariant. On the exact trajectory put
\[
h_0(x)=1+x+x^3/3.
\]
Then
\[
y=x^2/2,\qquad x'=c,\qquad c'=h_0(x),\qquad
c(x)^2=2x+x^2+x^4/6.                                  \tag{14}
\]
The last identity follows by dividing
\((c^2)'=2ch_0(x)\) by \(x'=c\) for \(s>0\) and then
integrating from \(x=0\). It also extends continuously to the
initial state.

The distinguished readout satisfies, at every state along feature
flow, the exact identity
\[
c''=c\,\|\nabla h_\lambda\|_2^2=P c,\qquad
P=\|\nabla h_\lambda\|_2^2\ge0.                         \tag{15}
\]
Along (14), \(P=1+x^2\) and
\[
G_\lambda=(c,cx,h_0(x)).
\]
Hence the exact orbit, its velocity, and \(P\) are independent of
\(\lambda\). The predictor along it is \(c(x)h_0(x)\).
It increases from zero and exceeds one at \(x=1/2\), so there is
a unique \(x_*\in(0,1/2)\) with \(c(x_*)h_0(x_*)=1\).
Since
\[
\frac{df_\lambda}{ds}
=\|G_\lambda\|_2^2=h_0(x)^2+c^2(1+x^2)\ge1,
\]
the feature horizon to target is at most one and
\[
\int_0^{s_*}\|G_\lambda\|_2^2\,ds=1.                  \tag{16}
\]
The whole orbit to target, its speed, and the readout amplitude
are bounded independently of \(\lambda\). Physical gradient flow
approaches that target as \(t\to\infty\).
The function \(h_\lambda\) and its first derivatives are also bounded
uniformly in \(\lambda\) on any fixed compact box: use
\(\lambda^{-1}\log\cosh(\lambda v)\le |v|\) and
\(|t_\lambda(v)|\le1\).

Now solve the exact principal forced variational problem (7) for
this system, and define its normal component
\[
w(t)=\zeta_y(t)-x(t)\zeta_x(t).
\]
Linearizing (13) along \(v=0\) gives the normal coefficient
\[
a_\lambda(x)=\lambda(1+x^2)-x.
\]
The homogeneous physical normal equation is
\(w'=2(1-f_\lambda)c\,a_\lambda(x)w\).
The normal component of the forcing in (7) can be computed without
the full Hessian. Along the exact curve \(y=x^2/2\),
\[
\ddot y-x\ddot x=\dot x^2
=[2(1-f_\lambda)c]^2.
\]
Since \(D\mathcal F_\lambda\,\mathcal F_\lambda\) is this exact
physical acceleration, (7) gives
\[
\frac{dw}{dt}
=2(1-f_\lambda)c\,a_\lambda(x)w
 -2(1-f_\lambda)^2c^2.
\]
Using \(dx/dt=2(1-f_\lambda)c>0\) away from the initial point,
this becomes exactly
\[
\frac{dw}{dx}
=a_\lambda(x)w-[1-c(x)h_0(x)]c(x),\qquad w(0)=0.
                                                                    \tag{17}
\]
The coefficients extend in the integral formulation to \(x=0\).
Therefore
\[
w(x)=
-\int_0^x[1-c(u)h_0(u)]c(u)
\exp\left(\int_u^x a_\lambda(v)\,dv\right)\,du.          \tag{18}
\]

For \(u\in[1/16,1/8]\), (14) gives
\[
\frac13<c(u)<\frac35,\qquad
h_0(u)<\frac65,\qquad
[1-c(u)h_0(u)]c(u)>\frac{7}{75}>\frac1{12}.
\]
Also \(a_\lambda(u)\ge\lambda-1/8>0\) on this interval.
Retaining only this interval in (18) yields
\[
|w(1/8)|
\ge
\frac{\exp((\lambda-1/8)/16)-1}
     {12(\lambda-1/8)}.                                \tag{19}
\]
The physical time
\[
T=\int_0^{1/8}
\frac{du}{2[1-c(u)h_0(u)]c(u)}
\]
is positive, finite, and independent of \(\lambda\). Finiteness at
zero follows from \(c(u)\sim\sqrt{2u}\); the residual stays
uniformly positive up to \(1/8\). Thus (19) is an exponential
lower bound on the exact forced variational response at one fixed
physical time \(T\).

For an indexed family \(\lambda=\sqrt n\) and \(\eta=n^{-2}\),
even \(\eta|w(T)|\) diverges. The index \(n\) here labels this
three-dimensional family; it does not turn (12) into an
\(n\)-neuron network.

## Exact force of the counterexample

Equations (12)--(19) disprove the inference that bilinear readout,
positive readout acceleration, uniformly bounded exact speed,
bounded feature horizon, and finite action automatically bound
the principal Euler-forced variational response. The forcing used
is exactly \(-\tfrac12D\mathcal F\,\mathcal F\), not an arbitrary
adversarial source.

They do not establish nonconvergence of actual Euler trajectories
at \(\eta=n^{-2}\). Such a claim would require control of the
nonlinear error and the remainder in (6) uniformly in \(\lambda\);
the large first-order response is not that control.
The example uses the synthetic feature map (12) and deterministic
initialization, so it also does not refute the Gaussian
arctangent-network GF/GD comparison.

For that canonical comparison, (1)--(5) close the source estimate.
The unclosed quantity is the propagated variation in (8)--(11),
specifically its signed first- and second-layer gate-curvature
pairings, together with the nonlinear remainder in the exact
error equation (6). A cancellation specialized to the actual
arctangent Gaussian trajectory remains a distinct possible
mechanism; this note neither proves nor rules it out.

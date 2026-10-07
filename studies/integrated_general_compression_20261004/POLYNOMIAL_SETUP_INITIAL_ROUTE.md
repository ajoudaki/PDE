# Initial algebra through a scalar label parameter

2026-10-06. Scoped theoretical continuation of the Harmonic setup question.
This note does not change `RESULT.md` or assert a completed polynomial-setup
theorem. Its conclusion is a conditional route with one new scientific
analyticity obligation. No experiment or dense training rollout was performed.

The scientific inputs are the current `RESULT.md`, specifically its shared
setup, full Harmonic statement, source equations and analytic domains, finite
initial-jet construction, and setup-cost qualifications, together with
`docs/notation.qmd`. No other study or archived book material was consulted.
The required canonical-notation skill could not be opened: both the ordinary
read and read-only escalation returned OS `Permission denied`; no accessible
copy was found in the installed skill roots. The maintained notation contract,
rigorous-math skill, and investigation/research-contract/adversarial-audit
instructions were read and applied.

## Conclusion and unchanged target

Expanding in scalar label amplitude, rather than reconstructing the whole
physical-time interval from unrestricted physical-time jets, has an exact
initialization-only implementation. The coefficient hierarchy at zero label
amplitude is unusually simple because the initial readout is zero. A bivariate
Taylor calculation at the stationary zero-label initialization computes its
coefficients in polynomial work in the two truncation orders. It does not
advance a dense nonlinear state through physical training time.

The missing assertion is a bounded complex label-amplitude tube around the
real interval from zero to the prescribed labels. A tube of width
`constant / log(en)` would suffice for polynomial setup at polynomial target
accuracy. Width `constant / sqrt(log(en))` would make the initial coefficient
calculation take `n^(2+o(1))` work at fixed problem parameters. Neither tube
follows from the physical-time source strip proved in `RESULT.md`.

The candidate preserves the intended model if that assertion is proved:
arbitrary fixed hidden depth \(L\ge2\), the stated strip-analytic activations
with possibly unbounded values, the original correlated sphere inputs and
positive feature Gram, the entire existing Harmonic label interval, the same
nonlinear dense gradient flow, and the same comparison over all inputs and
all physical times. It changes only how the source coefficient vectors are
computed. The selected architecture, exact initialized additions, metrics,
autonomous optimizer, retained storage, and existing comparison proof would
be unchanged.

## 1. Exact coefficient hierarchy at zero label amplitude

Keep the realized initialized parameters \(A_0,W_0^{(2)},\ldots,W_0^{(L)}\)
fixed. Introduce one dimensionless scalar \(\zeta\), and replace the labels by
\(\zeta y\). This scalar is a setup variable, not a new model order. The
residual and deficit are, respectively,
\[
r_a(t;\zeta)=f_n(t,x_a;\zeta)-\zeta y_a,
\qquad c_a(t;\zeta)=-r_a(t;\zeta).
\]
At \(\zeta=1\) this is precisely the prescribed dense reference. At
\(\zeta=0\) every parameter is stationary, because \(w(0)=0\).

For any parameter or source field \(g\), write its normalized amplitude
coefficient as
\[
g_r(t)=\frac1{r!}\left.\partial_\zeta^r g(t;\zeta)\right|_{\zeta=0}.
\]
Finite-time local analytic dependence near \(\zeta=0\) follows also from
the explicit local-ball argument in Section 3 below. Consequently these are
actual derivatives, as well as coefficients obtainable by formal algebra.
No convergence at \(\zeta=1\) is assumed here.

Changing \((\zeta,w,c)\) to \((-\zeta,-w,-c)\), while fixing the hidden
parameters, preserves the dense equations and initialization. Local uniqueness
therefore gives even hidden parameters and forward fields, and odd \(w,c\)
and backward fields. In particular,
\[
A(t;\zeta)=A_0+O(\zeta^2),\quad
W^{(j)}(t;\zeta)=W_0^{(j)}+O(\zeta^2),\quad
w(t;\zeta)=O(\zeta),\quad c(t;\zeta)=O(\zeta).
\]

Let \(H_0\in\mathbb R^{n\times m}\) have columns
\(h_n^{(L)}(0,x_a/\sqrt d)\), and define the positive symmetric matrix
\[
G_0=\frac{2H_0^T H_0}{mn}.
\]
The dense initialized feature-gap event makes \(G_0\) positive definite.
Let \(Q(t;\zeta)=K_n(t;\zeta)/m\), where \(K_n\) is the full dense
unnormalized tangent Gram. The exact deficit equation is
\[
\dot c=-2Q c,\qquad Q_0=G_0/2.
\]
Thus
\[
c_1(t)=e^{-G_0t}y,
\qquad
(\partial_t+G_0)c_r
 =-2\sum_{k=1}^{r-1}Q_kc_{r-k}\quad(r\ge2),
\tag{1}
\]
with \(c_r(0)=0\) for \(r\ne1\). The sum is empty when \(r=1\).

The other exact coefficient equations, with \(v_a=x_a/\sqrt d\), are
\[
\dot A_r=\frac2m\sum_a\sum_{p+q=r}c_{a,p}\delta_{a,q}^{(1)}v_a^T,
\]
\[
\dot W_r^{(j)}=\frac2{mn}\sum_a\sum_{p+q+s=r}
 c_{a,p}\delta_{a,q}^{(j)}h_{a,s}^{(j-1)T},
\qquad
\dot w_r=\frac2m\sum_a\sum_{p+q=r}c_{a,p}h_{a,q}^{(L)}.
\tag{2}
\]
All nonconstant initialized parameter coefficients vanish at \(t=0\).
Since \(c_0=\delta_0=0\), the hidden coefficient at order \(r\) uses only
\(c,w\) coefficients of order at most \(r-1\). Its forward coefficients can
then be evaluated by Taylor composition of the activations at the initialized
preactivations. Equation (1) needs only \(Q_k\) with \(k<r\). After it is
solved, the readout coefficient and then the passive backward coefficient at
order \(r\) follow from (2) and backpropagation. This is a triangular hierarchy.

Only derivatives of the activations at initialized preactivations occur.
Training coefficients are shared across all passive queries; a passive query
never adds an update force. These facts distinguish the calculation from
performing nonlinear dense training and saving its path.

### An exact finite function class

This observation is not needed for the eigenvalue-free implementation below,
but explains why the coefficient hierarchy is simpler than a generic time
strip. Let \(\omega_1,\ldots,\omega_m>0\) be the eigenvalues of \(G_0\),
counted with multiplicity. Every scalar order-\(r\) parameter or source
coefficient is a finite linear combination of
\[
t^p e^{-(k_1\omega_1+\cdots+k_m\omega_m)t},
\quad k_i\in\mathbb N_0,\quad \sum_i k_i\le r,\quad 0\le p\le r.
\tag{3}
\]
There are at most
\[
(r+1){r+m\choose m}
\tag{4}
\]
displayed functions. Repeated eigenvalues or repeated sums only reduce the
dimension.

To verify the assertion, diagonalize \(G_0\) for this proof only. Products
add frequency multiindices and polynomial degrees. A scalar convolution with
\(e^{-\omega_i t}\) sends \(t^p e^{-\nu t}\) to a sum with frequencies
\(\nu,\omega_i\); polynomial degree grows by at most one, and only in the
resonant case \(\nu=\omega_i\). A plain primitive of a positive-frequency
term has the same frequency and a constant term, without increasing degree.
Inductively all deficit coefficients have positive frequency. They always
occur in the forcing in (2), so the primitives there never integrate a
zero-frequency forcing term.

A degree budget that makes the induction explicit is: deficit, readout, and
backward coefficients at order \(r\ge1\) have polynomial degree at most
\(r-1\); nonzero hidden, feature, and Gram coefficients at order \(r\ge2\)
have degree at most \(r-2\). The forcing in (1) has degree at most \(r-3\)
because a nonconstant Gram coefficient starts at order two. Resonance adds
at most one. The forcing in each hidden equation in (2) has degree at most
\(r-2\), and the readout forcing has degree at most \(r-1\). Activation
composition adds the degrees of factors whose positive label orders sum to
the required order. This proves the budget and (3).

This is an exact coefficient statement, not a convergence assertion about
the amplitude expansion. It does not require an assumption on rational
independence or separation of the initialized Gram eigenvalues.

## 2. The missing complex-label statement

Here is a sufficient form of the unresolved lemma. Constants may depend on
the fixed problem parameters and activations, but not on \(n\), time,
requested accuracy, or the setup cutoffs.

**Complex-label tube obligation.** On a fixed-confidence eventual-width
event, uniform in setup accuracy, there are \(C,A,c>0\) and a radius
\(0<b_n\le1/4\) such that each coordinate of the four current Harmonic
source families for the dense system with labels \(\zeta y\) has a
holomorphic extension in \(\zeta\) to a neighborhood of
\[
\mathcal R_{b_n}=\{\zeta:-b_n\le\operatorname{Re}\zeta\le1+b_n,
                    \ |\operatorname{Im}\zeta|\le b_n\},
\]
and satisfies
\[
\sup_{t\ge0,\ v\in S^{d-1},\ \zeta\in\mathcal R_{b_n}}
 |g_i(t,v;\zeta)|\le Cn^A.
\tag{5}
\]
For polynomial setup the required radius is
\[
b_n\ge c/\log(en).
\tag{6}
\]
For the stronger near-quadratic coefficient calculation, it is enough to
prove
\[
b_n\ge c/\sqrt{\log(en)}.
\tag{7}
\]

The four families in (5) include initialized-matrix forward images and
transpose images separately, as in `RESULT.md`. The lemma must hold for
every label vector in the existing full Harmonic interval, including its
boundary. It cannot silently shrink that interval. The event may enlarge
an already existential sufficient-width threshold, but cannot introduce an
accuracy-dependent probability gate. The use of \(t\ge0\) is a clean
sufficient statement; an alternative bound on every required finite horizon
would also work if it retained the indicated radius and explicit acceptable
growth in \(T\).

### Conditional amplitude reconstruction

Assume (5) for one source coordinate. Apply the existing conformal-map
construction with interval length one and strip radius \(b_n\). Explicitly,
put
\[
\chi=\frac\pi{8b_n},\quad b_0=\tanh\chi,\quad
b_1=\tanh(\chi+\pi/4),\quad \vartheta=b_0/b_1,
\]
\[
\psi(\xi)=\frac{\xi-\vartheta}{1-\vartheta\xi},\qquad
\sigma(\xi)=\frac12+\frac{2b_n}{\pi}
 \log\frac{1+b_1\psi(\xi)}{1-b_1\psi(\xi)}.
\]
The same elementary logarithm estimates as in `RESULT.md` place this map
inside \(\mathcal R_{b_n}\), with \(\sigma(0)=0\) and
\[
\sigma(\xi_*)=1,\qquad
\xi_* =\frac{2\vartheta}{1+\vartheta^2}<1.
\]
The composed coefficients are
\[
a_j(t,v)=\sum_{r=0}^j g_r(t,v)[\xi^j]\sigma(\xi)^r.
\tag{8}
\]
Cauchy's bound and (5) give
\[
\left|g(t,v;1)-\sum_{j=0}^Ka_j(t,v)\xi_*^j\right|
 \le\frac{Cn^A\xi_*^{K+1}}{1-\xi_*}.
\tag{9}
\]
The identity
\[
1-\xi_* =\frac{(1-\vartheta)^2}{1+\vartheta^2}
\]
and the elementary formula for the difference of the two hyperbolic tangents
give universal positive constants bounding \(1-\xi_*\) above and below by
constant multiples of \(\exp[-\pi/(2b_n)]\), for \(b_n\le1/4\).
Consequently nodal accuracy \(\tau>0\) requires only
\[
K=O\!\left(e^{\pi/(2b_n)}
       [\log(Cn^A/\tau)+b_n^{-1}]\right).
\tag{10}
\]
For a polynomially small nodal tolerance and (6), this is polynomial in
\(n\). Under (7), it is \(\exp(O(\sqrt{\log(en)}))\), hence \(n^{o(1)}\).
This removes the factor \(T=O(\log n)\) from the aspect ratio in the
original global time-jet continuation. It uses new amplitude derivatives,
so it does not contradict a lower bound for generic reconstruction from
physical-time derivatives alone.

## 3. Polynomial initial algebra for the amplitude coefficients

The following estimate is proved independently of the unresolved tube.
It gives a practical mathematical implementation of (8) without taking
eigenvalues as extra unit-cost primitives or assuming separated frequencies.

Use the normalized parameter coordinates
\[
u=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n).
\]
Their Euclidean norm is precisely the parameter norm used in the all-time
tail proof in `RESULT.md`. In these coordinates the dense equation is the
negative gradient of the stated mean squared loss. For complex arguments its
analytic extension uses ordinary transpose products, without conjugation.

**Local-ball lemma.** On the existing initialized operator event there are
positive constants \(b,C_1,C_2,C_3\), independent of \(n\) and \(T\ge1\),
such that the initialized dense solution, jointly with every real-sphere
passive source, is holomorphic on
\[
|t|\le2T,\qquad |\zeta|\le R_{n,T},\qquad
R_{n,T}=\frac{b}{4C_2\sqrt n(1+2T)e^{2C_1T}},
\tag{11}
\]
after decreasing \(b\) or increasing \(C_2\ge1\) if necessary, and all source
coordinates there have magnitude at most \(C_3\sqrt n\).

Here and below a closed domain means a holomorphic neighborhood with the
displayed bounds, obtainable by choosing strict slack in the constants.

**Proof.** Work in the complex Euclidean ball
\(\|u-u_0\|_2<b/\sqrt n\). The initialized first operator divided by
\(\sqrt n\) and the hidden operators have fixed bounds. Their perturbations
on this ball have smaller fixed bounds. The first forward differential and
the layerwise recursion give, for every real unit query and every unit
parameter increment,
\[
\frac{\|Dh^{(j)}\|_2}{\sqrt n}\le C,
\qquad
\frac{\|D^2h^{(j)}\|_2}{\sqrt n}\le C\sqrt n.
\tag{12}
\]
To obtain the second estimate, use
\[
\frac{\|a\odot b\|_2}{\sqrt n}
 \le\sqrt n\frac{\|a\|_2}{\sqrt n}
                 \frac{\|b\|_2}{\sqrt n}
\]
in the second-derivative activation term, and the fixed operator bounds in
all propagation terms. There are only the fixed \(L\) layers. The first
estimate also bounds each preactivation displacement by
\(C\sqrt n\|u-u_0\|_2\). Choose \(b\) sufficiently small that the straight
segment from the real initialized state remains strictly in the activation
half-strip. A first-exit argument then justifies (12) throughout the ball.
Only the existing first- and second-derivative strip bounds and linear
activation growth were used.

The readout component \(u_w=w/\sqrt n\) has norm at most \(b/\sqrt n\).
Since \(f=u_w^T h^{(L)}/\sqrt n\), differentiating the readout pairing gives
\[
|f|\le C/\sqrt n,\qquad \|Df\|\le C,
\qquad \|D^2f\|\le C(1+\sqrt n\|u_w\|_2)\le C.
\tag{13}
\]
The two cross terms in \(D^2f\) use the first bound in (12); its hidden-hidden
term uses the second bound and the small readout. This cancellation is why
the local vector-field Lipschitz constant does not cost \(\sqrt n\).

Let \(F(u;\zeta)\) be the dense gradient vector field. Differentiating
\(F=-2m^{-1}\sum_a(f_a-\zeta y_a)Df_a^T\), using (13), and averaging
the labels with Cauchy--Schwarz gives, uniformly for \(|\zeta|\le1\),
\[
\|D_uF(u;\zeta)\|\le C_1,
\qquad \|F(u_0;\zeta)\|\le C_2|\zeta|.
\tag{14}
\]
The constants may depend on \(Y\), as permitted at a fixed problem, but not
on \(n\). Complex norms here use absolute values; no complex Gram positivity
is asserted.

Continue along a radial complex-time segment, stopping at the ball boundary.
The integral inequality from (14) gives
\[
\|u(t;\zeta)-u_0\|_2
 \le C_2|\zeta||t|e^{C_1|t|}.
\]
For (11) this is strictly smaller than \(b/(4\sqrt n)\). Local holomorphic
existence follows by contraction of the integral map on a smaller ball;
the strict bound allows continuation throughout the disk. Uniqueness glues
the local solutions. The forward and backward formulas then give joint
holomorphy of the sources. Their normalized Euclidean norms are bounded
by constants using linear activation growth, fixed operator bounds, and
bounded derivative gates. Conversion to a coordinate bound costs only
\(\sqrt n\). The same applies to each initialized-matrix image. This proves
the lemma.

### Two Taylor orders with an explicit sufficient relation

Cauchy's formula in \(\zeta\), applied to (11), bounds each amplitude
coefficient by
\[
\sup_{|t|\le2T,v\in S^{d-1}}|g_r(t,v)|
 \le C_3\sqrt n\,R_{n,T}^{-r}.
\tag{15}
\]
Let \(g_{r,N}\) be the degree-\(N\) Taylor polynomial in \(t\) at zero of
\(g_r\). A second Cauchy bound gives
\[
\sup_{0\le t\le T,v}|g_r(t,v)-g_{r,N}(t,v)|
 \le2C_3\sqrt n\,R_{n,T}^{-r}2^{-(N+1)}.
\tag{16}
\]
The conformal map in Section 2 obeys \(|\sigma(\xi)|\le2\) on the disk.
Thus \(|[\xi^j]\sigma(\xi)^r|\le2^r\), including by a limiting Cauchy
argument at radius one. Substitution in the degree-\(K\) sum (8) shows that
replacing all \(g_r\) by \(g_{r,N}\) contributes at most
\[
2C_3\sqrt n\,(K+1)^2(2/R_{n,T})^K2^{-N}.
\tag{17}
\]
For \(R_{n,T}\le1\), it suffices to choose
\[
N\ge K\log_2(2/R_{n,T})+
       \log_2\!\left(2C_3\sqrt n(K+1)^2/\tau\right).
\tag{18}
\]
In particular,
\[
N=O\!\left(K[\log(en)+T+\log(1+T)]
             +\log((K+1)/\tau)\right).
\tag{19}
\]
For \(T=O(\log n)\), polynomial nodal accuracy, and the radius (7), both
\(K\) and \(N\) are \(n^{o(1)}\). The tiny local radius in (11) is sufficient
for this coefficient calculation because its logarithm, rather than its
reciprocal exponential, appears in (18). The global tube (5) remains
necessary only for continuation to the actual label amplitude one.

### Actual operations and cost qualification

Compute in the finite ring
\[
\mathbb R[t,\zeta]/(t^{N+1},\zeta^{K+1}).
\]
The initialized parameters are the constant coefficients. The actual dense
ODE determines consecutive time coefficients by division by their positive
time degree. Forward evaluation, the residual, backward evaluation, and
rank-one updates use additions, matrix products, and truncated polynomial
products. Because the zero-label hidden state is stationary, its
preactivation increment is divisible by \(\zeta^2\); activation Taylor
composition at an initialized preactivation therefore needs only finitely
many derivatives, at most order \(K\). A brute-force convolution or Horner
implementation already has polynomial cost in \(K,N\).

With \(N_x\) streamed spatial queries, one deliberately loose bound on
non-activation arithmetic for a materialized implementation is
\[
O\!\left(L(m+N_x)(n^2+nd+mn)
                  (K+1)^4(N+1)^4\right).
\tag{20}
\]
This upper bound allows recomputing truncated compositions during each
time-degree step; it is not an optimized cost. Setup workspace can be bounded
by a polynomial in \(K,N,m,L\) times the dense array size. No such arrays are
retained after the selected model is assembled. The arithmetic model and
activation-backend qualification are the same as in `RESULT.md`: add the
cost of generating activation derivatives and Gaussian draws. Analyticity
alone does not give a unit-cost activation oracle or a bit-complexity bound.

All coefficients are obtained at \(t=\zeta=0\). Evaluating the resulting
polynomials at quadrature nodes is not a nonlinear dense time-stepping
operation. No trained dense state at one positive time is used to obtain
the next one, and no fitted dense endpoint is supplied as input.

## 4. Reconnection to the current Harmonic construction

Use (9) and (17), with split nodal error budgets, in place of the original
global physical-time-jet evaluation. Apply the same amplitude map, the same
two cutoffs, and the same linear coefficient operations to every paired
source family. Because \(W_0\) is fixed,
\[
\partial_t^k\partial_\zeta^r(W_0g)
 =W_0\partial_t^k\partial_\zeta^r g,
\]
and likewise with \(W_0^T\). Both source members have their own coordinate
error certificate from (5), (15), and (17). Their computed coefficient
vectors satisfy the initialized-image relation exactly. No conversion of
one member's coordinate error through the matrix infinity norm is needed.

The cosine/harmonic truncation and its source dimension are unchanged.
The exact initialized additions are unchanged. Therefore the current
coordinate-selection, exact source-metric, initialized action, fitting,
and all-time comparison arguments apply to these new coefficient vectors
without a change in their retained inventory or error certificate.

At the polynomial accuracy regimes in `RESULT.md`, the required horizon is
\(O(\log n)\), the logarithm of the required nodal accuracy is \(O(\log n)\),
and the retained source dimension is polylogarithmic. Under (6), (20) is
polynomial in \(n\). Even the existing Riemann-quadrature approach has a
polynomial node count there: coordinate and basis derivative bounds are
polynomial in \(n\) and in the retained degrees, the angle domain has fixed
dimension, and the required quadrature error is polynomially small.

For a total \(n^{2+o(1)}\) setup claim, (7) must be combined with a certified
\(n^{o(1)}\)-node time/sphere quadrature implementation. Analytic quadrature is
the natural candidate, but that implementation and its explicit bounds are
not proved in this note. The near-quadratic claim proved conditionally here
concerns the initial coefficient calculation (20) when \(N_x=n^{o(1)}\).
The retained model and its runtime have no amplitude or bivariate-jet state.

## 5. Why the decisive obligation is still open

The existing physical-time theorem controls one fixed label vector and a
complex time neighborhood of its real trajectory. It does not control
complex perturbations of the labels. Real fitting for every smaller real
label amplitude also does not supply the missing complex neighborhood.
For example, the scalar family
\[
g(\zeta,t)=\frac{\epsilon^2}{\epsilon^2+(\zeta-1/2)^2}
\]
is bounded by one for real \(\zeta\), is entire and constant in \(t\), and
has amplitude singularities at distance \(\epsilon\) from the real
interval. This is only a counterexample to that inference; it is not a
counterexample realized by the neural-network gradient flow.

The proved local-ball lemma has radius approximately
\(n^{-1/2}e^{-CT}\). Substituting that radius into the global amplitude
continuation would be far too expensive. It was used only to bound the
finite amplitude coefficients. To prove (5)--(6), one needs a stronger
reachable-direction estimate along the real amplitude family, controlling
complex amplitude variations without the worst-case conversion from a
parameter norm to a neuron-coordinate maximum. An estimate for the real
trajectory alone does not establish this. Nor may the positive real Gram
be treated as positive after analytic continuation: its complex extension
uses transposes, not conjugate transposes.

The original small-label allowance must be retained when proving that
estimate, including the \(Y\)-dependence and the boundary of the interval.
Constants that grow with \(T\) so strongly that the amplitude tube becomes
smaller than order \(1/\log n\) would not establish the stated polynomial
claim. A derivative bound with an \(e^{C\sqrt{\log n}}\) amplification in
the denominator of the allowable amplitude radius would likewise be
insufficient for this particular continuation map.

| Claim | Status after this round |
|---|---|
| Triangular amplitude hierarchy and exponential-polynomial coefficients | Proved by (1)--(4) |
| Initial bivariate computation with \(N\) as in (18) | Proved under the existing initialized operator event |
| Polynomial reconstruction from a width-\(c/\log n\) amplitude tube | Conditional, with explicit map and cutoff |
| Such a tube for the full admitted nonlinear network class and label interval | Open; decisive new scientific obligation |
| Complete near-quadratic setup | Open; additionally needs the stated quadrature/backend qualifications |
| Unchanged retained Harmonic guarantees after accurate paired coefficients are supplied | Direct application of the current construction |

No polynomial-setup theorem is established by this note. Its concrete
advance is the initial algebraic reduction: the new theorem needed is a
quantitative complex-label continuation bound, rather than a claim that
more physical-time Taylor coefficients or a renamed dense rollout are cheap.

## 6. Bounded audit of the source proof and a short-prefix variant

The current finite-deletion argument does not already prove the missing
amplitude tube. Its mixed source endpoint is the instantaneous field
\(R_a^{(j)}=D_\Theta z^{(j)}\nabla_\Theta F_a\), where
\(\Theta=(A,\sqrt nW^{(2)},\ldots,w)\) and \(F_a=nf_a\), as in the source
proof. Multiplication by the actual residual gives the physical velocity.
That residual factor supplies the bounded activity integral.

In contrast, \(U=\partial_\zeta\Theta\) satisfies exactly
\[
\dot U=-\mathcal H U+\frac2m\sum_a y_a\nabla_\Theta F_a,\qquad U(0)=0,
\]
\[
\mathcal H=\frac2{mn}\sum_a\nabla_\Theta F_a\nabla_\Theta F_a^T
             +\frac2m\sum_a r_aD_\Theta^2F_a.
\]
If \(\Phi(t,s)\) is the propagator of \(-\mathcal H\), the new query endpoint
is therefore
\[
\partial_\zeta z^{(j)}(t,v)
 =\frac2m\sum_a y_a\int_0^t
 D_\Theta z^{(j)}(t,v)\Phi(t,s)\nabla_\Theta F_a(s)\,ds.
\tag{21}
\]
This endpoint is transported between two different physical times, and the
displayed forcing is not residual weighted. The instantaneous source bound
cannot simply be integrated with the old activity measure.

There is an exact formulation that could recover the damping. Put
\(e=\partial_\zeta c\), and retain \(Q=K_n/m\). Then
\[
\dot e=-2Qe-2(\partial_\zeta Q)c,\qquad e(0)=y,
\]
\[
\dot U=\frac2m\sum_a
 \left[e_a\nabla_\Theta F_a+c_aD_\Theta^2F_a\,U\right].
\tag{22}
\]
A sufficient new stopped-domain estimate would bound the integral of
\(\|e(t)\|_2/\sqrt m\) and the reachable coordinate field
\(D_\Theta z^{(j)}U\), uniformly along the complex amplitude slab. In
particular a coordinate bound
\[
\sup_{t,v,j,i}|\partial_\zeta z_i^{(j)}(t,v;\zeta)|
 \le C\log(en)
\tag{23}
\]
on the appropriate stopped slab, together with complex fitting and operator
bounds, would leave a strip margin at amplitude distance of order
\(1/\log(en)\). Replacing the right side by \(C\sqrt{\log(en)}\) would support
the stronger radius. A bound only on real amplitude derivatives is not
enough; the stopped complex extension must improve its own boundary.

The current source argument has no joint moment budget or endpoint trace
calculation for (21)--(22). Its worst-case propagator estimate is only
\(n^{1/1000}\) eventually; the sharper carrier-based scalar stability bound
can still cost \(\exp(C\sqrt{\log n})\). Neither gives (23). Naively
integrating the undamped forcing in (21) also incurs the physical horizon.
The cavity proof must be extended to this new coupled tangent-deficit
system, preserving omitted-root independence and the full original label
allowance. This is a substantive missing argument, not a relabeling of the
existing time/query derivative estimates.

For complex fitting there is a useful exact identity: if a complex Jacobian
is \(J=J_{\rm re}+iJ_{\rm im}\), then the Hermitian part of \(J^T J\) is
\[
J_{\rm re}^T J_{\rm re}-J_{\rm im}^T J_{\rm im}.
\]
It can preserve a gap when the imaginary Jacobian is controlled. It does
not supply the required coordinate strip control or bound that imaginary
Jacobian by itself.

### What a short dense prefix would and would not repair

Under the supervisor's clarified authorization, a prefix at
\(t_0=O((m/\gamma)\log\log(en))\) would reduce the residual to an inverse
power of \(\log(en)\), while \(t_0/T_0\to0\). At its endpoint
\(\theta_\circ=\theta(t_0)\), consider the artificial labels
\[
y(\zeta)=f(\theta_\circ,X)+
          \zeta\,[y-f(\theta_\circ,X)].
\]
The anchor is stationary at \(\zeta=0\), although its readout is nonzero.
The linearized coefficient equation then uses the full tangent Gram at
the anchor. Hidden coefficients can start at order one; parity and the
special ordering in (1)--(2) must be replaced by the full fixed-Jacobian
linear system. This does not invalidate the stationary-amplitude idea.

The residual reduction is useful only with a coordinate estimate that
avoids the factor \(\sqrt n\). A generic parameter-to-coordinate bound
requires residual size \(O(n^{-1/2})\) to retain a fixed strip margin,
which forces a prefix of order \(\log n\) and loses the proposed advantage.
The existing finite-deletion proof also cannot be restarted at the trained
anchor by declaring its rows independent Gaussian. A cavity must continue
from its own original initialization to its own anchor. Moreover the
centered labels \(f(\theta_\circ,X)\) depend on the full network, hence on
the omitted root; replacing them by cavity-centered labels introduces a
new forcing difference that must be estimated.

Thus the short-prefix variant has an exact stationary construction and a
potentially favorable small residual, but still lacks a certified
coordinatewise complex continuation estimate and a compatible cavity
comparison. This bounded audit does not establish a valid short-prefix
polynomial setup theorem either.

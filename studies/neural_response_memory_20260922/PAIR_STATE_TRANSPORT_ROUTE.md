# Exact conditional pair-state transport of the learned matrix

This note uses only the supervisor's prompt. It does not establish the existence of a closed finite per-neuron state for the original network, a width limit, or an efficient finite-statistic representation. It establishes the requested conversion conditional on the stated reversible state dynamics.

Let both hidden layers have width (n), and suppose
\[
W_{2,ij}(t)=W_{0,ij}+\frac1n w_{ij}(t),\qquad
\dot w_{ij}(t)=-2r(t)D(m_{2,i}(t))H(m_{1,j}(t)),\qquad w_{ij}(0)=0.
\]
Here (H) and (D) are the scalar activation and backpropagated readouts specified in the assignment. The residual convention and all learning-rate factors are those of this stipulated equation.

Assume the neuron states lie in finite-dimensional spaces (M_1,M_2), with any necessary fixed marks included, and solve
\[
\dot m_{\ell,i}=F_\ell(t,m_{\ell,i};\mathcal Q_t),\qquad \ell=1,2.
\]
The shared current state \(\mathcal Q_t\) may contain distributions, interaction fields, and fixed initialization data. For a given continuous path \(\mathcal Q_t\), suppose the vector fields are continuous in time and (C^1) in state, with continuous state derivatives locally bounded on the trajectories considered. Work on a time interval where their flows \(\Phi_\ell(t,s)\) exist and are (C^1) diffeomorphisms between the corresponding transported domains. Assume (H,D\) are (C^1) and (r\) is continuous; boundedness on these domains or sufficient integrability is required for continuum integrals. Fixed marks have zero velocity. These are conditional regularity and reversibility hypotheses, not consequences proved about the network.

## Pair field and exact reconstruction

On the transported product domain, define a scalar current-coordinate field by
\[
\left(\partial_t+F_2(t,b;\mathcal Q_t)\cdot\nabla_b
                 +F_1(t,a;\mathcal Q_t)\cdot\nabla_a\right)k_t(b,a)
=-2r(t)D(b)H(a),\qquad k_0(b,a)=0. \tag{1}
\]
The solution is uniquely specified by its values along the product characteristics:
\[
k_t\bigl(\Phi_2(t,0)b_0,\Phi_1(t,0)a_0\bigr)
=-2\int_0^t r(s)D\bigl(\Phi_2(s,0)b_0\bigr)
                         H\bigl(\Phi_1(s,0)a_0\bigr)\,ds. \tag{2}
\]
For each initial pair \((b_0,a_0)\), the right side is differentiable in time, with derivative equal to the source in (1) along that characteristic. The assumed (C^1) dependence of the flows and readouts gives (C^1) dependence on the initial pair, locally by differentiation under the integral on a compact characteristic neighborhood. The diffeomorphism hypothesis therefore defines (k_t\) uniquely at each current pair and gives its (C^1) state regularity. The chain rule proves (1). If two solutions exist, their difference has zero derivative on every product characteristic and starts at zero, so it is zero everywhere in the transported domain. This proves conditional local existence and uniqueness for (1), for the given coefficient path. It does not prove well-posedness of the full coupled system determining \(\mathcal Q_t\).

Evaluating (1) along the actual neuron pair gives
\[
\frac{d}{dt}k_t(m_{2,i}(t),m_{1,j}(t))
=-2r(t)D(m_{2,i}(t))H(m_{1,j}(t)).
\]
Its initial value is zero, exactly as for (w_{ij}\). Subtraction and time integration yield
\[
w_{ij}(t)=k_t(m_{2,i}(t),m_{1,j}(t)). \tag{3}
\]
This is an exact finite-width identity. If a nonzero learned correction is present initially, its values must first be representable by an initial pair field; one then replaces (k_0=0\) by that field.

The characteristic formula is a proof of exactness. An implementation can instead evolve (1) forward from (k_0=0\), alongside the state distributions. It need not replay individual neuron trajectories backward or retain a list of past gradients. What it retains is the entire current pair field. Invertibility is used to make that field single-valued in the current coordinates.

## Current-state interaction and normalization

Let
\[
\mu_{\ell,t}^{n}=\frac1n\sum_{i=1}^n\delta_{m_{\ell,i}(t)}.
\]
The learned forward and backward interaction fields are
\[
L_{2,t}(b)=\int k_t(b,a)H(a)\,\mu_{1,t}^{n}(da),
\qquad
L_{1,t}(a)=\int k_t(b,a)D(b)\,\mu_{2,t}^{n}(db). \tag{4}
\]
Using (3), their values at the neurons are exactly
\[
L_{2,t}(m_{2,i})=\frac1n\sum_j w_{ij}H(m_{1,j}),\qquad
L_{1,t}(m_{1,j})=\frac1n\sum_i w_{ij}D(m_{2,i}). \tag{5}
\]
There is no extra factor of (n\) or learning-rate factor in (4): the (1/n\) in (W_2-W_0\) is precisely supplied by the normalized empirical measure. When the network multiplies directly by (W_2\), the complete matrix products are
\[
\sum_j W_{2,ij}H(m_{1,j})
=\sum_j W_{0,ij}H(m_{1,j})+L_{2,t}(m_{2,i}),\tag{6}
\]
\[
\sum_i W_{2,ij}D(m_{2,i})
=\sum_i W_{0,ij}D(m_{2,i})+L_{1,t}(m_{1,j}).\tag{7}
\]
Any additional normalization in a differently defined network matrix product would multiply both terms in these equations.

For every (C^1) test function \(\varphi\) for which the integrals exist,
\[
\frac{d}{dt}\int\varphi(m)\,\mu_{\ell,t}^{n}(dm)
=\int\nabla\varphi(m)\cdot F_\ell(t,m;\mathcal Q_t)\,\mu_{\ell,t}^{n}(dm).
\]
This follows by differentiating the finite sum and using the neuron ODE. Thus, distributionally,
\[
\partial_t\mu_\ell+\nabla\cdot(F_\ell\mu_\ell)=0. \tag{8}
\]
For an arbitrary initial probability measure transported by the same flow, the same weak identity follows by differentiating \(\int\varphi(\Phi_\ell(t,0)m_0)\,\mu_{\ell,0}(dm_0)\), under the assumed integrability. Equations (1), (4), and (8) therefore make sense as a continuum system, provided the remaining current-state equations defining \(F_\ell\), \(r\), and \(\mathcal Q_t\) are specified. Existence of such a system does not itself establish convergence of finite networks to it.

## What must remain in the coupled state

Equations (4)–(5) are algebraic empirical-measure identities. They do not assume statistical independence of neurons, independence across layers, or independence of the initial matrix and the evolving states. For example, integrating over the product of the two realized empirical measures is simply summing over all ordered layer pairs. Replacing a random empirical product by the product of unconditional one-neuron laws would be a separate, generally unjustified step.

The terms involving (W_0\) in (6)–(7) remain necessary. The two unmarked state marginals generally cannot recover them: an arbitrary fixed initial matrix carries edge information and develops correlations with the states that it drives. One can retain the initial matrix as a fixed operator on indexed neurons. An equivalent exact representation includes fixed neuron identities in the states and a fixed pair kernel. Specifically, let \(\alpha_j\), \(\beta_i\) denote fixed marks distinguishing the two layers' neurons, and set
\[
B_0(\beta_i,\alpha_j)=nW_{0,ij}.
\]
Writing \(\alpha(a)\) and \(\beta(b)\) for these mark coordinates, (6) can be expressed as
\[
\int\bigl[B_0(\beta(b),\alpha(a))+k_t(b,a)\bigr]H(a)\,\mu_{1,t}^{n}(da),\tag{9}
\]
at \(b=m_{2,i}\), and (7) has the corresponding integral against \(D(b)\mu_{2,t}^{n}(db)\). The mark-normalized kernel may depend on (n\) and need not have a regular continuum limit. A more general formulation retains an appropriate full joint law of fixed edge data and current marked states. In either description, the fixed pair coupling is retained; it is not inferred from unmarked marginals or replaced by an independence assumption.

For a closed current-state model, the postulated velocities must be evaluable from this complete retained state, including (k_t\) and whatever initialization coupling is required. If the velocity of a neuron still depends on unavailable individual history, merely writing (1) has not supplied closure. If two neurons with the same proposed state need different velocities or different learned pair values, those coordinates are insufficient: the state must be enlarged until the stipulated single-valued reversible dynamics hold. Giving every neuron a unique fixed mark can remove labeling ambiguity, but does not by itself prove a useful width-independent closure.

## Claim level and remaining cost

Under the stated hypotheses, the canonical learned-matrix time integral is exactly equivalent to a forward transport equation for one scalar field on (M_2\times M_1\), coupled to current-state distributions. This field is a current macroscopic state variable that contains the accumulated pair memory. No low-rank hypothesis appears: instantaneous rank-one sources can accumulate into a matrix of unrestricted rank, and (1) imposes no separation-rank bound on (k_t\).

Finite-dimensional neuron coordinates make the pair domain finite-dimensional. They do not make its function space finite-dimensional. The representation can therefore be exact without being computationally inexpensive or reducible to finitely many scalar moments. Its local existence proof is conditional on the neuron-flow coefficients; closure and well-posedness of the full network-derived macroscopic equations remain separate obligations.

## Audit of the supervisor's message-moment hierarchy

After the pair-field derivation above, the supervisor supplied the following additional route for verification. For a fixed (C^1\) test function (f:M_1\to\mathbb R\), define
\[
A_f(t,b)=\int k_t(b,a)f(a)\,\mu_{1,t}(da),\qquad
\mathcal L_{1,t}f(a)=F_1(t,a;\mathcal Q_t)\cdot\nabla f(a).
\]
With (\mathcal D_2=\partial_t+F_2\cdot\nabla_b\), the proposed identity is correct:
\[
\mathcal D_2 A_f(t,b)
=-2r(t)D(b)\int H(a)f(a)\,\mu_{1,t}(da)
  +A_{\mathcal L_{1,t}f}(t,b). \tag{10}
\]
For a direct proof with the empirical measure, follow any second-layer characteristic (b(t)\) and differentiate
\[
A_f(t,b(t))=\frac1n\sum_j k_t(b(t),m_{1,j}(t))f(m_{1,j}(t)).
\]
The derivative of the first factor is the source in (1); the derivative of the second is \(\mathcal L_{1,t}f(m_{1,j}(t))\). The product rule gives (10), with no boundary terms. For a transported continuum measure, use its initial-coordinate representation and the same product rule, with differentiation under the integral justified by the assumed bounds. Equivalently, transport of \(\mu_1\) cancels precisely the \(-F_1\cdot\nabla_a k\) term from (1); there is no remaining \(\nabla\cdot F_1\) contribution.

For a fixed (C^1\) test function (g:M_2\to\mathbb R\), set
\[
B_g(t,a)=\int k_t(b,a)g(b)\,\mu_{2,t}(db),\qquad
\mathcal L_{2,t}g(b)=F_2(t,b;\mathcal Q_t)\cdot\nabla g(b).
\]
The same argument, now following a first-layer characteristic, gives
\[
\left(\partial_t+F_1\cdot\nabla_a\right)B_g(t,a)
=-2r(t)H(a)\int D(b)g(b)\,\mu_{2,t}(db)
  +B_{\mathcal L_{2,t}g}(t,a). \tag{11}
\]
If (f\) or (g\) depends explicitly on time, including time dependence through current global quantities, replace \(\mathcal L_{\ell,t}\) in the last terms by \(\partial_t+\mathcal L_{\ell,t}\), using the full time derivative of the test function. In the displayed fixed-readout setup the actual fields are (L_2=A_H\) and (L_1=B_D\); hence
\[
\mathcal D_2 A_H=-2rD\int H^2\,d\mu_1+A_{\mathcal L_{1,t}H},\qquad
\left(\partial_t+F_1\cdot\nabla_a\right)B_D
=-2rH\int D^2\,d\mu_2+B_{\mathcal L_{2,t}D}. \tag{12}
\]

These equations expose the successive additional message fields needed to evolve the actual interactions. A test family invariant under the relevant time-dependent generator can close the number of message fields; otherwise the process generally generates an infinite hierarchy. If successive tests are themselves time-dependent, their full \(\partial_t+\mathcal L_{\ell,t}\) derivatives must be tracked. Polynomial vector fields do not generally preserve a bounded-degree polynomial test space, so polynomiality alone supplies no finite closure.

Even a finite list of generator-invariant tests gives a finite list of functions of the other layer's state, not automatically finitely many scalar statistics. A scalar reduction must also close their dependence on that other state, the source moments \(\int Hf\,d\mu_1\) and \(\int Dg\,d\mu_2\), and every additional quantity required by the velocities and residual. Nothing in (10)–(12) assumes or proves those extra closures.

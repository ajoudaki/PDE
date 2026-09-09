# Canonical bounded-readout two-species DMFT

## 1. Status and target

The target finite-width feature-ascent flow is exactly the canonical model in
`../../global_proxy_campaign/reference/canonical_model.py`:

\[
z_i=\frac1{\sqrt n}\sum_jW_{ij}u_j^2,
\qquad
f_n=\frac1n\sum_i a_i z_i^2,
\]

\[
\dot a_i=z_i^2,
\qquad
\dot W_{ij}=\frac2{\sqrt n}a_i z_i u_j^2,
\qquad
\dot u_j=\frac4{\sqrt n}u_j\sum_iW_{ij}a_i z_i.
\tag{1}
\]

Dots in this report mean **feature time**.  Physical squared-loss time is a
later scalar time change by (2(1-f)).

Only the initial readout law is changed in the bounded prototype:

\[
a_i(0)\stackrel{\rm iid}\sim N(0,1)\mid |a_i(0)|\le A,
\qquad A=3
\tag{2}
\]

for the primary campaign.  Its variance is not reset to one.  All (u(0))
and (W(0)) coordinates remain independent standard Gaussians.

Equations (1), the matrix-elimination identities below, and the observable
readouts are exact at finite width.  The stochastic DMFT is the canonical
formal width-limit candidate obtained from the feature-learning DMFT of
Bordelon--Pehlevan.  Identification of this candidate with the bounded
finite-width limit is **open** in this repository.

## 2. Exact two-species finite-width skeleton

Set

\[
x_j=u_j^2,
\qquad b_i=a_i z_i,
\qquad
p_j=\frac1{\sqrt n}\sum_iW_{ij}b_i,
\qquad q_j=2p_j.
\]

Then (1) is equivalently

\[
\dot a_i=z_i^2,
\qquad \dot x_j=4x_jq_j,
\qquad \dot W_{ij}=\frac2{\sqrt n}b_i x_j.
\tag{3}
\]

Eliminating the trained matrix gives the exact identities

\[
W_{ij}(t)=W_{ij}(0)+\frac2{\sqrt n}
\int_0^t b_i(s)x_j(s)\,ds,
\tag{4}
\]

\[
z_i(t)=\eta_i(t)+2\int_0^t C_x(t,s)b_i(s)\,ds,
\quad
\eta_i(t)=\frac1{\sqrt n}\sum_jW_{ij}(0)x_j(t),
\tag{5}
\]

\[
q_j(t)=\xi_j(t)+4\int_0^t C_b(t,s)x_j(s)\,ds,
\quad
\xi_j(t)=\frac2{\sqrt n}\sum_iW_{ij}(0)b_i(t),
\tag{6}
\]

where

\[
C_x(t,s)=\frac1n\sum_jx_j(t)x_j(s),
\qquad
C_b(t,s)=\frac1n\sum_i b_i(t)b_i(s).
\tag{7}
\]

The fields \(\eta\) and \(\xi\) are not fresh independent noises.  They use
the same (W(0)) in opposite orientations, and their conditional means are
the reciprocal Onsager responses.  Dropping those responses is precisely the
gradient-independence ablation, not the canonical limit.

## 3. Formal cavity/response limit

There are two representative, independently sampled species.

### First-layer species

Let (U_0\sim N(0,1)).  Conditional on the current kernels, let \(\Xi\) be a
centered Gaussian process with covariance (G_2).  Define

\[
U(t)=U_0+\int_0^t2U(s)Q(s)\,ds,
\tag{8}
\]

\[
Q(t)=\Xi(t)+\int_0^t
\{B(t,s)+G_2(t,s)\}U(s)^2\,ds.
\tag{9}
\]

### Second-layer/readout species

Let (A_0) have law (2).  Conditional on the current kernels, let \(H\) be a
centered Gaussian process with covariance \(\Phi_1\), independent of (A_0).
Define

\[
Z(t)=H(t)+2\int_0^t
\{A(t,s)+\Phi_1(t,s)\}A_r(s)Z(s)\,ds,
\tag{10}
\]

\[
A_r(t)=A_0+\int_0^tZ(s)^2\,ds.
\tag{11}
\]

The subscript on (A_r) distinguishes the random readout path from the
response kernel (A(t,s)).

### Self-consistency and responses

\[
\Phi_1(t,s)=\mathbb E[U(t)^2U(s)^2],
\qquad
G_2(t,s)=4\mathbb E[A_r(t)Z(t)A_r(s)Z(s)],
\tag{12}
\]

\[
A(t,s)=\mathbb E\!\left[
\frac{\delta U(t)^2}{\delta\Xi(s)}\right],
\qquad
B(t,s)=\mathbb E\!\left[
\frac{\delta(2A_r(t)Z(t))}{\delta H(s)}\right].
\tag{13}
\]

These are the specialization of the four order-parameter families
\((\Phi^\ell,G^\ell,A^\ell,B^\ell)\) in the primary DMFT derivation
[Self-Consistent Dynamical Field Theory of Kernel Evolution in Wide Neural
Networks](https://arxiv.org/abs/2205.09653).  The mapping uses two hidden
layers, \(\phi(r)=r^2\), one sample, feature strength \(\gamma_0=1\), and
constant feature-ascent error signal \(\Delta=1\).  Replacing the top static
Gaussian field by (2) is exact for the declared bounded initialization inside
this formal single-site construction; it is not a proof of width convergence.

The remaining order parameters and observables are

\[
\Phi_2(t,s)=\mathbb E[Z(t)^2Z(s)^2],
\qquad
G_1(t,s)=4\mathbb E[U(t)Q(t)U(s)Q(s)],
\tag{14}
\]

\[
F_A(t)=\mathbb E[A_r(t)Z(t)^2],
\tag{15}
\]

\[
K_A(t)=
\underbrace{\Phi_2(t,t)}_{K_a}
+\underbrace{G_2(t,t)\Phi_1(t,t)}_{K_W}
+\underbrace{G_1(t,t)}_{K_u}.
\tag{16}
\]

A correct solution must obey

\[
F_A'(t)=K_A(t).
\tag{17}
\]

## 4. Exact initialization and response gates

Write

\[
m_2(A)=\mathbb E[A_0^2\mid |A_0|\le A].
\]

At initialization,

\[
\Phi_1(0,0)=3,
\quad G_2(0,0)=12m_2(A),
\quad \Phi_2(0,0)=27,
\quad G_1(0,0)=48m_2(A),
\]

and therefore

\[
\boxed{K_A(0)=27+84m_2(A).}
\tag{18}
\]

As (A\to\infty), this becomes (27+36+48=111).  The exact finite-width
counterpart is

\[
\mathbb E K_{a,n}(0)=27+\frac{288}{n},
\]

\[
\mathbb E(K_{W,n}(0)+K_{u,n}(0))
=m_2(A)\left(84+\frac{1056}{n}\right).
\tag{19}
\]

For the left-contact Euler convention of `PROTOCOL.md`, the first strict
subdiagonal path derivatives be

\[
R^x_{km}=\mathbb E\frac{\partial U_k^2}{\partial\Xi_m},
\qquad
R^b_{km}=\mathbb E\frac{\partial(2A_{r,k}Z_k)}{\partial H_m}.
\]

The stored response **densities** are

\[
A_{km}=R^x_{km}/h,\qquad B_{km}=R^b_{km}/h,
\]

and the Volterra equations retain their factors \(h\sum_{m<k}\).  The first
strict subdiagonal responses obey

\[
A_{1,0}=4
\tag{20}
\]

exactly in population, and

\[
B_{1,0}\longrightarrow12+28m_2(A)
\qquad(h\downarrow0).
\tag{21}
\]

Indeed, \(A_{1,0}=4\) makes the first forward coefficient
\(\Phi_{1,0}+A_{1,0}=3+4=7\), hence

\[
Z_1=H_1+14hA_0H_0.
\]

Differentiating \(2A_{r,1}Z_1\) with respect to \(H_0\), holding \(H_1\)
fixed, gives \(4H_0^2+28A_0^2\) after division by \(h\).  Its expectation is
\(12+28m_2(A)\).  This matches the direct finite-width initial drift:
trained-\(W\) motion contributes \(6az\), while reuse of \(W(0)\) through
first-layer motion contributes \(8az\).

The response-free ablation sets both quantities to zero and therefore fails
an exact architecture-specific gate before any positive-time comparison.

## 5. Reconciliation with the older tagged-site Riccati report

The older report
`../../../../quadratic_nonclosure/mean_field_single_source_conjecture_audited_resolution.md`
assumes a projected tagged second-layer equation

\[
z(t)=\xi(t)+\int_0^tM(t,s)a(s)z(s)\,ds
\]

with a continuous positive initial self-response.  Conditional on that
equation and an unbounded Gaussian readout, its Riccati comparison is a
coherent tail argument.

What is not supplied there is the bridge from the fully coupled pair
(8)--(13) to that one-kernel projection, including:

1. existence and uniqueness of the coupled covariance/response fixed point;
2. identification of its projected (M) and proof of the required short-time
   positivity after both reciprocal responses are included;
3. convergence of bounded finite-width networks to that DMFT on a common
   positive-time interval;
4. uniform integrability allowing the cutoff (A\to\infty) to be exchanged
   with width, expectation, and positive time.

Accordingly, the Riccati result is retained as **exact under its tagged-DMFT
assumptions**, while its identification with the canonical finite-width
limit remains open.  The present bounded campaign removes the readout-tail
step but does not prove any of those four bridges.

## 6. Claim ladder

| Claim | Status |
|---|---|
| Finite-width equations (1), elimination (4)--(7), and kernel decomposition | Exact |
| Mapping of the standard two-hidden-layer DMFT equations to (8)--(16) | Formal/exact conditional on the DMFT saddle-point construction |
| Truncated initialization formulae (18)--(21) | Exact |
| Numerical fixed point of the declared discretization | To be gated |
| Equality with the bounded finite-width (n\to\infty) curve | Open |
| Removal of (A=3) cutoff | Outside this protocol |
| Unbounded-Gaussian global curve or Stieltjes identification | Outside this protocol |

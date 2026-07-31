# Audited resolution of the pure mean-field finite single-source closure conjecture

## Verdict

For the two-hidden-layer, single-input, quadratic network with an unbounded Gaussian trainable readout, the meaningful uniform-in-time finite-closure conjecture is **false**.

The obstruction occurs entirely inside the deterministic infinite-width dynamical mean-field theory (DMFT). It is not a finite-width effect.

In the canonical causal DMFT, a tagged second-layer neuron has a continuous Gaussian cavity field and a causal self-response kernel. The self-response is strictly positive at initialization. A tagged neuron whose initial readout weight is \(A\gg1\) then reaches a Riccati-type singular regime in time

\[
O\!\left(\frac{\log A}{A}\right).
\]

Because the Gaussian readout law has positive mass above every finite \(A\), every output level below the label is reached at time zero. The natural monotone, no-overshoot loss trace is therefore

\[
\mathcal L_{\mathrm{MF}}(0)=1,
\qquad
\mathcal L_{\mathrm{MF}}(t)=0\quad(t>0).
\]

Every ordinary finite autonomous ODE, and every finite-dimensional invariant reduction of a locally well-posed one-source PDE, has a continuous loss curve. No continuous curve can approximate this step uniformly with error below \(1/2\). If the surrogate matches the initial loss exactly, its uniform error is at least \(1\).

Thus there is no family of continuous finite-dimensional single-source closures with arbitrarily small uniform error on \([0,\infty)\).

---

## 1. Network, scaling, and notation

There is one fixed input, so it is suppressed. Both hidden layers have width \(n\), and

\[
\phi(u)=\frac12u^2.
\]

The first hidden layer is

\[
h_i^{(1)}=\phi\!\left(z_i^{(1)}\right)
=\frac12\left(z_i^{(1)}\right)^2.
\]

The second hidden layer is

\[
z_j^{(2)}=\sum_i W_{ji}^{(2)}h_i^{(1)},
\qquad
h_j^{(2)}=\frac12\left(z_j^{(2)}\right)^2.
\]

Writing \(a_j=W_j^{(3)}\), the output is

\[
f=\frac1n\sum_j a_jh_j^{(2)}
=\frac1{2n}\sum_j a_j\left(z_j^{(2)}\right)^2,
\]

and the label-one squared loss is

\[
\mathcal L=(1-f)^2.
\]

Initialization is

\[
z_i^{(1)}(0)\sim N(0,1),
\qquad
a_j(0)\sim N(0,1),
\qquad
W_{ji}^{(2)}(0)\sim N\!\left(0,\frac\gamma n\right),
\]

independently, with \(\gamma>0\).

The \(\mu\)P physical-time gradient flow is

\[
\dot z^{(1)}=-n\nabla_{z^{(1)}}\mathcal L,
\qquad
\dot W^{(2)}=-\nabla_{W^{(2)}}\mathcal L,
\qquad
\dot a=-n\nabla_a\mathcal L.
\]

Put

\[
r=1-f,
\qquad
z=z^{(2)},
\qquad
u=a\odot z,
\qquad
q=\frac1n\sum_i\left(h_i^{(1)}\right)^2,
\]

and

\[
K=W^{(2)}\operatorname{diag}\!\left(h^{(1)}\right)(W^{(2)})^\top.
\]

Direct differentiation gives the exact physical-time equations

\[
\dot a_j=r z_j^2,
\]

\[
\dot z_j=2r\bigl(q\,u_j+2(Ku)_j\bigr).
\]

The output satisfies

\[
\dot f=2r\kappa,
\]

where \(\kappa\ge0\) is the mean-field tangent kernel. Its readout-gradient contribution gives the important lower bound

\[
\kappa\ge\frac14\,\mathbb E[z^4].
\]

At initialization, \(a(0)\) is centered and independent of \(z(0)^2\), so

\[
f(0)=0,
\qquad
\mathcal L(0)=1.
\]

---

## 2. The canonical pure mean-field equation

The infinite-width object is the canonical causal tagged-site DMFT, not a finite network and not a subsequent width limit.

For a tagged second-layer neuron, let

- \(a(t)\) be its readout weight;
- \(z(t)\) be its second-layer preactivation;
- \(\xi(t)\) be its cavity Gaussian field;
- \(M(t,s)\) be the deterministic retarded self-response kernel.

The tagged mean-field equation is

\[
z(t)
=
\xi(t)
+\int_0^t r(s)M(t,s)a(s)z(s)\,ds,
\]

\[
\dot a(t)=r(t)z(t)^2.
\]

The mean-field setup has the following standard causal properties.

1. \(\xi\) is a nondegenerate continuous Gaussian process.
2. \(a(0)\sim N(0,1)\) is independent of the entire cavity process \(\xi\).
3. \(M\) is deterministic, causal, and continuous on an initial triangle \(0\le s\le t\le\delta_0\).
4. The output is the self-consistent mean-field expectation, and \(\dot f=2(1-f)\kappa\) wherever the classical flow exists.

Independent Gaussian single-site fields plus retarded response kernels are the standard DMFT representation of feature learning in infinite-width \(\mu\)P networks. See Bordelon and Pehlevan, [Self-Consistent Dynamical Field Theory of Kernel Evolution in Wide Neural Networks](https://arxiv.org/abs/2205.09653), especially their closed stochastic Volterra equations and functional-response kernels.

The response term is essential. Treating the reused initial middle-layer row as fresh independent Gaussian noise would omit the Onsager/self-response contribution. The proof below retains the full response through \(M\).

---

## 3. Precise finite-closure conjecture

An admissible accuracy-\(\varepsilon\) closure consists of:

1. a finite-dimensional autonomous state \(x_\varepsilon(t)\in\mathbb R^{D(\varepsilon)}\);
2. a locally well-posed vector field
   \[
   \dot x_\varepsilon=V_\varepsilon(x_\varepsilon);
   \]
3. a continuous predicted loss
   \[
   \widehat{\mathcal L}_\varepsilon(t)
   =\Lambda_\varepsilon(x_\varepsilon(t));
   \]
4. coefficients constructed from the mean-field equations and initialization law rather than from samples of the already-solved loss curve;
5. dimension \(D(\varepsilon)\) independent of any requested physical training horizon.

The finite ODE may be encoded as a one-field, one-source, finite-jet PDE; this changes only its syntax.

The conjecture asserts that, for every \(\varepsilon>0\), such a closure can satisfy

\[
\sup_{t\ge0}
\left|
\widehat{\mathcal L}_\varepsilon(t)
-\mathcal L_{\mathrm{MF}}(t)
\right|
\le\varepsilon.
\]

The continuity/local-well-posedness requirement is indispensable. If impulses or a discontinuous source at \(t=0\) were allowed, one could encode the target step by fiat, which would not be a dynamical closure.

---

## 4. Positive initial self-response

Let

\[
h_0=\frac12G^2,
\qquad G\sim N(0,1).
\]

Then

\[
\mathbb E[h_0]=\frac12,
\qquad
\mathbb E[h_0^2]=\frac34.
\]

The diagonal middle-layer Gram order parameter at initialization is determined directly by the mean-field initialization law:

\[
K_{\mathrm{diag}}(0)
:=\gamma\mathbb E[h_0]
=\frac\gamma2.
\]

From

\[
\dot z_j=2r\bigl(q\,u_j+2(Ku)_j\bigr),
\]

the coefficient multiplying the tagged \(u_j=a_jz_j\) at time zero is

\[
2q_0+4K_{\mathrm{diag}}(0),
\qquad
q_0=\mathbb E[h_0^2].
\]

Therefore, in the convention where \(r(s)\) is factored outside the memory kernel,

\[
\boxed{
M(0,0)
=2\mathbb E[h_0^2]+4\gamma\mathbb E[h_0]
=\frac32+2\gamma>0.
}
\]

The off-diagonal field does not alter this tagged instantaneous coefficient: in the canonical DMFT it belongs to the cavity Gaussian and retarded response, while the displayed diagonal is fixed by the exact local drift.

Since \(M\) is continuous, there are \(m>0\) and \(\delta_0>0\) such that

\[
M(t,s)\ge m,
\qquad
0\le s\le t\le\delta_0.
\]

This local positivity is all that the proof uses. No global sign assumption on the full matrix \(K\) or on off-diagonal messages is made.

---

## 5. A positive Gaussian cavity event

Because \(\xi\) is continuous and nondegenerate at zero, one can choose \(z_*>0\) and, after decreasing \(\delta_0\) if necessary, obtain

\[
p_\xi
:=
\Pr\!\left[
\inf_{0\le t\le\delta_0}\xi(t)\ge z_*
\right]
>0.
\]

A direct justification is to use the event

\[
\xi(0)\ge2z_*, ,
\qquad
\sup_{t\le\delta_0}|\xi(t)-\xi(0)|\le z_*.
\]

The first part has positive probability. Continuity makes the probability of the second part tend to one as \(\delta_0\downarrow0\), so their intersection has positive probability for a sufficiently short interval.

Independence of \(a(0)\) and \(\xi\) gives, for every finite \(A\),

\[
p_A
:=
\Pr\!\left[
a(0)\ge A,
\ \inf_{t\le\delta_0}\xi(t)\ge z_*
\right]
=p_\xi\Pr[a(0)\ge A]
>0.
\]

The probability can be extremely small. Only strict positivity matters.

---

## 6. Cooperative comparison and its blow-up time

Fix any subtarget \(y\in(0,1)\). Suppose, toward a contradiction, that the output remains below \(y\) on a positive interval. Then

\[
r(t)=1-f(t)\ge c:=1-y>0
\]

on that interval.

On the event defining \(p_A\), the tagged DMFT gives

\[
a(t)
\ge
A+c\int_0^t z(s)^2\,ds,
\]

\[
z(t)
\ge
z_*+cm\int_0^t a(s)z(s)\,ds,
\]

as long as the subtarget has not been hit.

Compare this with

\[
\dot b=cv^2,
\qquad
\dot v=cm\,bv,
\qquad
b(0)=A,
\qquad
v(0)=z_*.
\]

Both right-hand sides are increasing in \(b,v\ge0\). Standard monotone Volterra comparison therefore gives

\[
a(t)\ge b(t),
\qquad
z(t)\ge v(t)
\]

until the comparison trajectory blows up or the output reaches \(y\).

The comparison system has the invariant

\[
v(t)^2-z_*^2
=m\bigl(b(t)^2-A^2\bigr).
\]

For \(A>z_*/\sqrt m\), define

\[
\alpha
=\sqrt{A^2-\frac{z_*^2}{m}}.
\]

Then

\[
\dot b=cm\bigl(b^2-\alpha^2\bigr).
\]

Its blow-up time is

\[
\boxed{
T_A
=
\frac{1}{2cm\alpha}
\log\!\left(\frac{A+\alpha}{A-\alpha}\right).
}
\]

As \(A\to\infty\),

\[
T_A
=O\!\left(\frac{\log A}{A}\right)
\longrightarrow0.
\]

This is the mean-field extreme-readout condensation scale.

---

## 7. The tangent kernel forces every subtarget hitting time to zero

Before the output reaches \(y\),

\[
\dot f=2r\kappa
\ge
\frac c2\mathbb E[z^4],
\]

because \(\kappa\ge\frac14\mathbb E[z^4]\).

On the event of probability \(p_A>0\), \(z\ge v\). Hence

\[
\dot f(t)
\ge
\frac{cp_A}{2}v(t)^4.
\]

The comparison trajectory satisfies

\[
\int_0^{T_A}v(t)^4\,dt=+\infty.
\]

Indeed, near \(T_A\), both \(b\) and \(v\) grow like a positive constant times \((T_A-t)^{-1}\).

Consequently \(f\) cannot remain below the finite level \(y\) until \(T_A\). It must hit \(y\) strictly before \(T_A\).

For every \(\delta>0\), choose \(A\) so large that

\[
T_A<\min\{\delta,\delta_0\}.
\]

It follows that the first hitting time \(T_y\) satisfies \(T_y<\delta\). Since \(\delta\) was arbitrary,

\[
\boxed{
T_y=0
\qquad
\text{for every }y\in(0,1).
}
\]

This conclusion uses the continuum Gaussian tail directly. There is no network width and no probabilistic width limit in the argument.

---

## 8. The natural mean-field loss is a step

For an ordinary squared-loss trajectory starting below the label,

\[
r(t)
=
r(0)\exp\!\left(-2\int_0^t\kappa(s)\,ds\right),
\]

so the target-side branch has

\[
0\le f(t)\le1
\]

and is nondecreasing. The natural relaxed continuation keeps these two properties and interprets an infinite cumulative hazard as \(r=0\).

Since every \(y<1\) has hitting time zero, monotonicity and no overshoot imply

\[
f(t)=1
\qquad(t>0).
\]

Together with \(f(0)=0\), this gives

\[
\boxed{
\mathcal L_{\mathrm{MF}}(t)
=
\begin{cases}
1,&t=0,\\
0,&t>0.
\end{cases}
}
\]

Equivalently: the unbounded-Gaussian canonical DMFT has no classical output continuous at initialization. The displayed step is the unique loss trace within the natural monotone, no-overshoot relaxed class. Without specifying such a relaxed selection, the rigorous conclusion is nonexistence of a classical continuous mean-field solution rather than a different regular loss curve.

---

## 9. Uniform finite closure is impossible

Let \(\widehat{\mathcal L}\) be the loss curve of any admissible finite closure. It is continuous at zero.

Put

\[
E
=
\sup_{t\ge0}
\left|
\widehat{\mathcal L}(t)-\mathcal L_{\mathrm{MF}}(t)
\right|.
\]

At time zero,

\[
|\widehat{\mathcal L}(0)-1|\le E.
\]

For positive times tending to zero, the target loss is zero and continuity gives

\[
|\widehat{\mathcal L}(0)|\le E.
\]

The triangle inequality then gives

\[
1
\le
|1-\widehat{\mathcal L}(0)|
+|\widehat{\mathcal L}(0)|
\le2E.
\]

Therefore

\[
\boxed{
E\ge\frac12.
}
\]

If the closure is required to match the correct initialization,

\[
\widehat{\mathcal L}(0)=1,
\]

then continuity instead yields the sharper bound

\[
\boxed{E\ge1.}
\]

Hence the error cannot be made arbitrarily small. The conjecture is false.

---

## 10. Why a one-source PDE does not evade the theorem

Any \(D\)-state ODE

\[
\dot x_j=V_j(x_0,\ldots,x_{D-1})
\]

can be encoded as one field and one source by setting

\[
U(t,s)=\sum_{j=0}^{D-1}x_j(t)e^{js}
\]

and using the coefficient extractors

\[
\mathcal C_j[U]
=e^{-js}
\prod_{\substack{0\le k<D\\k\ne j}}
\frac{\partial_s-k}{j-k}\,U.
\]

On this ansatz, \(\mathcal C_j[U]=x_j\), so

\[
\partial_tU
=
\sum_{j=0}^{D-1}
V_j\!\left(\mathcal C_0[U],\ldots,\mathcal C_{D-1}[U]\right)e^{js}
\]

is exactly equivalent to the ODE.

If its source and coefficients are locally regular, \(U(t,\cdot)\) and every continuous observable of it are continuous in \(t\). The \(1/2\) lower bound therefore applies unchanged. One-source syntax cannot remove the discontinuity obstruction.

---

## 11. Audit of possible loopholes

### This is not a finite-width result

The proof starts from the tagged infinite-width DMFT. The width-normalized network formulas above only identify its local coefficients; no width-convergence estimate, concentration argument, finite-replica approximation, or interchange of width and time limits is used.

### Tiny Gaussian tail probability does not save the flow

For each finite \(A\), the favorable event has strictly positive probability. Although that probability decays rapidly with \(A\), the integrated fourth moment of the comparison process diverges at \(T_A\). A positive constant times infinity is still infinity.

### Off-diagonal signs are not assumed

Earlier coordinate arguments could fail because \((Ku)_j\) has no fixed sign. Here the entire cavity/Onsager effect is represented by the canonical Gaussian field plus the total retarded response kernel. Only the exact positive response diagonal and its short-time continuity are used.

### Wick–Taylor divergence is not the proof

The previously proved zero radius of the ordinary Wick–Taylor series is consistent with this singularity, but zero Taylor radius alone would not prove it. The present proof is a real-time Volterra comparison argument.

### Stability of squared loss does not help

Squared-loss stability converts an already accurate regular approximation into an all-time accurate one. Here the exact target has a jump at initialization, so no continuous surrogate is even uniformly accurate on an arbitrarily short initial interval.

### A discontinuous finite source would be oracular

Allowing an impulse that sets the surrogate loss to zero at \(t=0^+\) would reproduce the answer by stipulation. Such a system is not a classical finite continuation module and falls outside the non-oracular closure conjecture.

---

## 12. Final classification

| Statement | Status |
|---|---|
| Pure mean-field tagged Gaussian/response representation | Part of canonical causal DMFT |
| Initial total self-response | \(M(0,0)=\frac32+2\gamma>0\) |
| Extreme tagged-neuron time scale | \(O(\log A/A)\) |
| Hitting time of every output level \(y<1\) | Zero |
| Classical continuous Gaussian DMFT output at \(t=0\) | Impossible |
| Natural monotone no-overshoot loss trace | \(1\) at \(0\), \(0\) for \(t>0\) |
| Best possible uniform error of a continuous finite closure | At least \(1/2\) |
| Best error when initialization is matched exactly | At least \(1\) |
| Arbitrarily accurate uniform all-time finite closure | False |

The resolved theorem is therefore

\[
\boxed{
\text{unbounded Gaussian readout tail}
+
\text{positive causal self-response}
\Longrightarrow
\text{instantaneous mean-field fitting}
\Longrightarrow
\text{no uniform continuous finite closure}.
}
\]

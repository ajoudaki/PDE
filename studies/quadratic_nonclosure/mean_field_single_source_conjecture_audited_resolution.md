# Conditional tagged-site comparison for the pure mean-field closure conjecture

> **Corrected status.**  The tagged-site Volterra equation used below is a
> representation hypothesis; it is not derived or identified with the
> finite-network mean-field limit in this source.  The monotone,
> no-overshoot step trace is a further relaxed-selection hypothesis.  The
> Riccati comparison and continuity lower bound are exact implications from
> those assumptions, not an unconditional result about the canonical
> network.

## Verdict

Assume that the intended infinite-width dynamics admit the tagged-site
Volterra representation in Section 2, including independence and continuity
of the cavity field, a continuous response kernel with positive initial
diagonal, and the stated output/tangent-kernel identity.  Under those
assumptions, a tagged neuron whose initial readout weight is \(A\gg1\) reaches
a Riccati-type comparison singularity in time

\[
O\!\left(\frac{\log A}{A}\right).
\]

Because the Gaussian readout law has positive mass above every finite \(A\),
the asserted equations imply that no classical solution can remain below an
output level on a positive interval (equivalently, its hitting time is zero
if defined).  If one additionally selects the monotone, no-overshoot
relaxed continuation, its stipulated loss trace is

\[
\mathcal L_{\mathrm{rel}}(0)=1,
\qquad
\mathcal L_{\mathrm{rel}}(t)=0\quad(t>0).
\]

Every ordinary finite autonomous ODE, and every finite-dimensional invariant reduction of a locally well-posed one-source PDE, has a continuous loss curve. No continuous curve can approximate this step uniformly with error below \(1/2\). If the surrogate matches the initial loss exactly, its uniform error is at least \(1\).

Thus no family of continuous finite-dimensional single-source closures can
uniformly approximate **that selected trace** arbitrarily well.  This does
not settle the network closure question: the tagged law, its self-consistency
and positive-time solution, network-to-DMFT identification, and the relaxed
selection are not proved here.

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

Let \(a_j\) be the rescaled readout coordinate, so that the raw forward
coefficient is \(a_j/n\). The output is

\[
f_n=\frac1n\sum_j a_jh_j^{(2)}
=\frac1{2n}\sum_j a_j\left(z_j^{(2)}\right)^2,
\]

and the label-one squared loss is

\[
\mathcal L_n=(1-f_n)^2.
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
\dot z^{(1)}=-n\nabla_{z^{(1)}}\mathcal L_n,
\qquad
\dot W^{(2)}=-\nabla_{W^{(2)}}\mathcal L_n,
\qquad
\dot a=-n\nabla_a\mathcal L_n.
\]

Put

\[
r_n=1-f_n,
\qquad
z=z^{(2)},
\qquad
u_n=a\odot z,
\qquad
q_n=\frac1n\sum_i\left(h_i^{(1)}\right)^2,
\]

and

\[
K_n=W^{(2)}\operatorname{diag}\!\left(h^{(1)}\right)(W^{(2)})^\top.
\]

Direct differentiation gives the exact physical-time equations

\[
\dot a_j=r_n z_j^2,
\]

\[
\dot z_j=2r_n\bigl(q_n(u_n)_j+2(K_nu_n)_j\bigr).
\]

At finite width the output satisfies

\[
\dot f_n=2r_n\kappa_n,
\]

where \(\kappa_n\ge0\) is the finite-width tangent kernel. Its
readout-gradient contribution gives
the exact empirical lower bound

\[
\kappa_n\ge\frac1{4n}\sum_{j=1}^n z_j^4.
\]

At initialization, \(a(0)\) is centered and independent of \(z(0)^2\), so
\(\mathbb E[f_n(0)]=0\); the corresponding law-of-large-numbers candidate is

\[
f(0)=0,
\qquad
\mathcal L(0)=1.
\]

---

## 2. The postulated tagged-site mean-field equation

The argument now **assumes** an infinite-width tagged-site object.  It is not
constructed as a width limit in this document.

For a tagged second-layer neuron, let

- \(a(t)\) be its readout weight;
- \(z(t)\) be its second-layer preactivation;
- \(\xi(t)\) be its cavity Gaussian field;
- \(M(t,s)\) be the deterministic retarded self-response kernel.

The postulated tagged equation is

\[
z(t)
=
\xi(t)
+\int_0^t r(s)M(t,s)a(s)z(s)\,ds,
\]

\[
\dot a(t)=r(t)z(t)^2.
\]

The conditional theorem assumes all of the following properties.

1. \(\xi\) is a nondegenerate continuous Gaussian process.
2. \(a(0)\sim N(0,1)\) is independent of the entire cavity process \(\xi\).
3. \(M\) is deterministic, causal, and continuous on an initial triangle \(0\le s\le t\le\delta_0\).
4. The output is a self-consistent mean-field expectation with \(f(0)=0\),
   and, wherever the classical flow exists,
   \[
   \dot f=2(1-f)\kappa,
   \qquad
   \kappa\ge\frac14\mathbb E[z^4].
   \]

Gaussian single-site fields plus retarded response kernels occur in DMFT
formulations of wide-network feature learning.  That general precedent does
not derive these particular equations, their kernel, or their
self-consistency for this architecture.  The cited comparison is Bordelon
and Pehlevan, [Self-Consistent Dynamical Field Theory of Kernel Evolution in
Wide Neural Networks](https://arxiv.org/abs/2205.09653).

The response term is essential within the assumed model. Treating the reused
initial middle-layer row as fresh independent Gaussian noise would omit the
Onsager/self-response contribution.  Writing a kernel \(M\), however, does
not prove that it is the correct response of the network.

No derivation, network-to-DMFT identification, self-consistency theorem,
classical positive-time existence theorem, or uniqueness theorem for this
system is supplied below.

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

After the extra relaxed selection is made, the conditional surrogate
question asks whether, for every \(\varepsilon>0\), such a closure can
satisfy

\[
\sup_{t\ge0}
\left|
\widehat{\mathcal L}_\varepsilon(t)
-\mathcal L_{\mathrm{rel}}(t)
\right|
\le\varepsilon.
\]

The continuity/local-well-posedness requirement is indispensable for this
conditional lower bound. If impulses or a discontinuous source at \(t=0\)
were allowed, one could encode the selected step by fiat. Conversely,
refuting continuous approximation of a stipulated step does not establish
that the network itself has that target.

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

The finite-network diagonal middle-layer Gram coefficient has initialization
limit

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

This exact instantaneous coefficient is a consistency check for a candidate
tagged-site limit; it does not derive the full memory kernel.  The argument
below therefore additionally assumes that, in the convention where \(r(s)\)
is factored outside the postulated kernel,

\[
\boxed{
M(0,0)
=2\mathbb E[h_0^2]+4\gamma\mathbb E[h_0]
=\frac32+2\gamma>0.
}
\]

The assignment of all remaining effects to the cavity field and retarded
response is part of the representation hypothesis, not a consequence of the
instantaneous finite-network drift.

Since \(M\) is continuous, there are \(m>0\) and \(\delta_0>0\) such that

\[
M(t,s)\ge m,
\qquad
0\le s\le t\le\delta_0.
\]

This assumed local positivity is all that the comparison uses. No global sign
assumption on the full matrix \(K\) or on off-diagonal messages is made.

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
\xi(0)\ge2z_*,
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

On the event defining \(p_A\), the postulated tagged equation gives

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

This is the extreme-readout scale of the comparison system.

---

## 7. The comparison forbids positive subtarget delay for a classical solution

Suppose a classical solution exists on a positive interval and remains below
some \(y\in(0,1)\) there. Before the output reaches \(y\),

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

Thus no such solution can remain below \(y\) for any positive \(\delta\).
Equivalently, if its first hitting time \(T_y\) is defined, then

\[
\boxed{
T_y=0
\qquad
\text{for every }y\in(0,1).
}
\]

This conclusion uses the continuum Gaussian tail directly.  It is an exact
property of the asserted continuum equations; precisely for that reason it
does not supply the missing width-limit or network-identification theorem.
If the asserted system has no positive-time classical solution, the result is
a nonexistence/continuity obstruction rather than a hitting-time statement
for a constructed flow.

---

## 8. Step trace under an additional relaxed-selection rule

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

and is nondecreasing. Now impose an additional relaxed-selection rule: keep
these two properties and interpret an infinite cumulative hazard as \(r=0\).
This rule is not derived from a classical positive-time solution or a
uniqueness theorem.

Under the additional relaxed interpretation, the no-positive-delay result
for every \(y<1\), together with monotonicity and no overshoot, implies

\[
f(t)=1
\qquad(t>0).
\]

Together with \(f(0)=0\), this gives

\[
\boxed{
\mathcal L_{\mathrm{rel}}(t)
=
\begin{cases}
1,&t=0,\\
0,&t>0.
\end{cases}
}
\]

More precisely: no output continuous at initialization can satisfy all of the
asserted tagged equations and response properties. The displayed step is the
loss trace selected after adding the monotone, no-overshoot axiom. Without
that axiom, the conditional conclusion is a continuity obstruction, not an
independently constructed classical step-valued flow.

---

## 9. Continuity lower bound for the selected trace

Let \(\widehat{\mathcal L}\) be the loss curve of any admissible finite closure. It is continuous at zero.

Put

\[
E
=
\sup_{t\ge0}
\left|
\widehat{\mathcal L}(t)-\mathcal L_{\mathrm{rel}}(t)
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

Hence the selected trace cannot be approximated arbitrarily well by a
continuous surrogate. Relevance to the network closure conjecture remains
conditional on the representation and selection hypotheses.

---

## 10. Why one-source syntax does not evade the conditional lower bound

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

If its source and coefficients are locally regular, \(U(t,\cdot)\) and every
continuous observable of it are continuous in \(t\). The \(1/2\) lower bound
therefore applies unchanged to the stipulated trace. One-source syntax cannot
remove that continuity obstruction, but operator-valued, singular, or
integro-differential descriptions of a different actual target are not ruled
out.

---

## 11. Audit of possible loopholes

### The starting representation is an unproved hypothesis

The comparison starts from the asserted tagged infinite-width equations. The
width-normalized network formulas above provide an instantaneous consistency
check; they do not identify the full memory law. No width-convergence,
self-consistency, classical-existence, uniqueness, finite-replica, or
width/time-interchange theorem is supplied.

### Tiny Gaussian tail probability does not save the flow

For each finite \(A\), the favorable event has strictly positive probability. Although that probability decays rapidly with \(A\), the integrated fourth moment of the comparison process diverges at \(T_A\). A positive constant times infinity is still infinity.

### Off-diagonal signs are not assumed

Earlier coordinate arguments could fail because \((Ku)_j\) has no fixed sign.
Here the entire cavity/Onsager effect is **assumed** to be represented by the
Gaussian field plus the total retarded response kernel. Only its postulated
positive response diagonal and short-time continuity are used.

### Wick–Taylor divergence is not the proof

The proved zero radius of the formal annealed Wick–Taylor jet is compatible
with this comparison singularity, but zero Taylor radius alone does not prove
the postulated Volterra law, a step loss, or any positive-time behavior.

### Stability of squared loss does not help

Squared-loss stability converts an already accurate regular approximation
into an all-time accurate one. Here the **selected trace** has a jump at
initialization, so no continuous surrogate is uniformly accurate to that
trace on an arbitrarily short initial interval.

### A discontinuous finite source would be oracular

Allowing an impulse that sets the surrogate loss to zero at \(t=0^+\) would reproduce the answer by stipulation. Such a system is not a classical finite continuation module and falls outside the non-oracular closure conjecture.

---

## 12. Final classification

| Statement | Status |
|---|---|
| Tagged Gaussian/response representation for this network | **Postulated; not derived or identified** |
| Kernel continuity and initial response \(M(0,0)=\frac32+2\gamma>0\) | Representation hypothesis; finite drift supplies only a consistency check |
| Extreme comparison time scale | \(O(\log A/A)\), exact under the hypotheses |
| Positive delay below an output level \(y<1\) | Impossible for a classical solution under the asserted equations; hitting time is zero if defined |
| Classical output continuous at \(t=0\) satisfying all asserted equations | Impossible, conditional on the asserted equations |
| Monotone/no-overshoot step trace | Additional relaxed-selection axiom |
| Uniform error of a continuous surrogate to that selected trace | At least \(1/2\), or \(1\) under matched initialization |
| Arbitrarily accurate continuous closure of the actual network loss | **Not resolved by this argument** |

The exact logical statement is therefore

\[
\boxed{\begin{gathered}
\text{asserted tagged-site Volterra/response law}
+
\text{unbounded Gaussian readout tail}
\Longrightarrow
\text{no positive subtarget delay for a classical solution},\\
\text{plus relaxed selection}
\Longrightarrow
\text{continuity lower bound for the selected step trace}.
\end{gathered}}
\]

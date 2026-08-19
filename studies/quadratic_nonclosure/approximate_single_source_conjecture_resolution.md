# Resolution of the approximate one-source Wick--Taylor conjecture

> **Corrected scope.**  Read \(c_k\) below as the fixed-order **annealed**
> coefficient
> \(
> c_k=\lim_{n\to\infty}\mathbb E[D_{+,n}^k f_n(0)]/k!
> \), now supplied by the exact special quadratic forest compiler.  This
> source's earlier claims of convergence of the random derivatives in
> probability and \(L^1\) are retracted: concentration and identification
> with derivatives of an actual positive-time mean-field trajectory remain
> open.  The step limit below belongs to the prescribed Taylor-closure
> family, not to the network loss.

## Two-hidden-layer quadratic \(\mu\)P network, squared loss, label \(1\)

## Executive verdict

The stability theorem proved previously is correct, but the missing approximation
lemma is false under the stated unbounded Gaussian initialization.

More precisely, two statements had been conflated.

1. **Propagation of a known small closure defect.** If a finite model already
   approximates the readout-ascent profile on the finite feature-time interval,
   squared-loss clock contraction turns that error into a uniform-in-physical-time
   loss error. This statement is true.
2. **Smallness of the concrete Wick--Taylor truncation defect.** The degree-\(M\)
   initial-source polynomial, built from the first \(M+1\) fixed-order Wick
   coefficients, was conjectured to converge as \(M\to\infty\). This statement is
   false.

The failure is decisive. If

\[
c_k=\lim_{n\to\infty}\mathbb E\!\left[
\frac{D_{+,n}^k f_n(0)}{k!}\right],
\]

then an odd subsequence obeys a factorial lower bound implying

\[
\limsup_{k\to\infty}c_k^{1/k}=+\infty.
\]

Thus the formal Wick--Taylor series has radius of convergence zero. Since all
coefficients are nonnegative, its partial sums diverge to \(+\infty\) at every
positive feature time. The associated physical-time PDE predictions develop an
initial boundary layer: their losses converge pointwise to \(1\) at \(t=0\) and
to \(0\) at every \(t>0\). Consequently they do not converge uniformly on any
time interval containing zero and cannot satisfy the proposed global shadowing
conjecture.

This does **not** prove that every conceivable non-Taylor approximation is
impossible. A Borel/Pad\'e resummation, real-axis Wick--Picard compiler, or
weighted message Galerkin scheme is a different conjecture and requires a new
nonperturbative real-axis estimate. Fixed-order Wick calculus does not supply
that estimate.

---

## 1. Exact model and feature-time derivation

For one fixed input, suppress the input and write

\[
h_i^{(1)}=\frac{(z_i^{(1)})^2}{2},
\qquad
z_j^{(2)}=\sum_{i=1}^n W_{ji}h_i^{(1)},
\qquad
h_j^{(2)}=\frac{(z_j^{(2)})^2}{2},
\qquad
f_n=\frac1n\sum_{j=1}^n a_jh_j^{(2)},
\]

where \(a_j\) is the rescaled readout coordinate: the corresponding raw
output weight is \(a_j/n\). For compactness below, write
\(h=h^{(1)}\) and \(z=z^{(2)}\). The squared loss is

\[
\mathcal L_n=(1-f_n)^2.
\]

Initialization is independent:

\[
z_i^{(1)}\sim N(0,1),
\qquad
a_j\sim N(0,1),
\qquad
W_{ji}\sim N\!\left(0,\frac\gamma n\right),
\quad \gamma>0.
\]

The maintained exact compiler uses unit Gaussian middle weights and unit
activation scale.  To map it to this historical convention, write
\(\lambda=\gamma\) and set

\[
W^\circ=\sqrt{\frac n\lambda}\,W,
\qquad
z^\circ=\frac1{\sqrt n}W^\circ(z^{(1)})^{\odot2},
\qquad
f^\circ=\frac1n\sum_j a_j(z_j^\circ)^2.
\]

Then

\[
z=\frac{\sqrt\lambda}{2}z^\circ,
\qquad
f_n=\frac\lambda8f^\circ,
\]

and, if \(D_a^\circ,D_{z^{(1)}}^\circ,D_W^\circ\) are the three block
contributions to \(n\nabla f^\circ\mathbin\cdot\nabla\),

\[
D_{+,n}
=\frac18\left(
\lambda D_a^\circ+\lambda D_{z^{(1)}}^\circ+D_W^\circ
\right).
\]

Hence this is the same decorated-forest grammar with constant block weights,
not literally the unit-block-metric point.  In particular,

\[
\mathbb E[D_{+,n}^k f_n]
=\frac\lambda{8^{k+1}}
\mathbb E\!\left[
(\lambda D_a^\circ+\lambda D_{z^{(1)}}^\circ+D_W^\circ)^k f^\circ
\right].
\]

This identity is the bridge by which the exact leading-forest selection
applies here. At \(\lambda=4/3\) the block-weighted expression gives the
historical first coefficient \(17/6\); the separate unit-block point gives
\(111\).

Let \(D_{+,n}\) denote differentiation along \(\mu\)P gradient ascent on the
readout \(f_n\):

\[
D_{+,n}z_i^{(1)}=n\frac{\partial f_n}{\partial z_i^{(1)}},
\qquad
D_{+,n}W_{ji}=\frac{\partial f_n}{\partial W_{ji}},
\qquad
D_{+,n}a_j=n\frac{\partial f_n}{\partial a_j}.
\]

The exact primitive equations are

\[
D_{+,n}a_j=\frac12z_j^2,
\]

\[
D_{+,n}W_{ji}=\frac1n a_jz_jh_i,
\]

\[
D_{+,n}z_i^{(1)}=z_i^{(1)}\sum_jW_{ji}a_jz_j.
\]

Define

\[
q_n=\frac1n\sum_i h_i^2,
\qquad
K_n=W\operatorname{diag}(h)W^\top.
\]

Then

\[
D_{+,n}z
=
q_n(a\odot z)+2K_n(a\odot z).
\tag{1}
\]

If \(\Theta_n(\tau)\) is this readout-ascent orbit and

\[
F_n(\tau)=f_n(\Theta_n(\tau)),
\]

then \(F_n'=\kappa_n\ge0\), where \(\kappa_n\) is the full \(\mu\)P tangent
kernel. Squared-loss flow follows the same orbit with the residual clock

\[
\dot\tau_n(t)=2\bigl(1-F_n(\tau_n(t))\bigr),
\qquad
f_n(t)=F_n(\tau_n(t)).
\tag{2}
\]

Equation (2) is the source of the valid loss-stability theorem.

---

## 2. The precise conjecture being resolved

The concrete construction proposed previously takes the deterministic
fixed-order annealed Wick coefficients

\[
c_k=\lim_{n\to\infty}\mathbb E\!\left[
\frac{D_{+,n}^kf_n(0)}{k!}\right]
\tag{3}
\]

and forms

\[
F_M(s)=\sum_{k=0}^M c_ks^k.
\tag{4}
\]

It then solves the one-field, one-source PDE

\[
\partial_tU_M(t,s)
=
2\bigl(1-U_M(t,0)\bigr)\partial_sU_M(t,s),
\qquad
U_M(0,s)=F_M(s),
\tag{5}
\]

and predicts

\[
f_M(t)=U_M(t,0),
\qquad
\mathcal L_M(t)=(1-f_M(t))^2.
\tag{6}
\]

Because the polynomial space of degree at most \(M\) is invariant, (5) is
equivalent to the finite system

\[
\dot u_k=2(1-u_0)u_{k+1},
\quad 0\le k<M,
\qquad
\dot u_M=0,
\tag{7}
\]

with \(u_k(0)=k!c_k\).

The historical conjecture wrote an unqualified distance to the random
finite-width curve.  To make the probability mode explicit, for \(T>0\) set

\[
d_T(g,h)=\min\!\left\{1,
\sup_{0\le t\le T}|g(t)-h(t)|\right\}.
\]

A precise weak Wick--Taylor shadowing conjecture is

\[
\lim_{M\to\infty}
\limsup_{n\to\infty}
\mathbb E\!\left[d_T(\mathcal L_M,\mathcal L_n)\right]=0
\qquad\text{for every }T>0.
\tag{8}
\]

The proposed proof route additionally required (4) to approximate a finite
target-reaching feature profile uniformly on its feature-time interval. The
theorem below refutes the precise probabilistic formulation. Expected
untruncated uniform error is stronger and also fails. Deterministic mean-curve
shadowing is a different, generally weaker condition, but its common-target
version is likewise ruled out by the same Cauchy triangle argument.

---

## 3. A positive embedded scalar branch

Freeze the first hidden-layer variables while retaining training of \(a\) and
\(W\). Then \(q_n\) is constant and the first term of (1) gives, for each upper
neuron,

\[
a'=\frac12z^2,
\qquad
z'=qaz.
\]

Introduce the scalar derivation

\[
\mathscr D_0
=
\frac{z^2}{2}\partial_a+qaz\,\partial_z,
\qquad
g(a,z)=\frac12az^2,
\]

and the normalized iterates

\[
P_k(a,z;q)=\frac1{k!}\mathscr D_0^kg(a,z).
\tag{9}
\]

Every coefficient of \(P_k\) is nonnegative. It is homogeneous of total degree
\(k+3\). Each application of \(\mathscr D_0\) reverses the parity of the power
of \(a\). Therefore, for odd \(k\), with

\[
m=\frac{k+3}{2},
\]

we can write

\[
P_k(a,z;q)
=
\sum_{u+v=m}p_{uv}(q)a^{2u}z^{2v},
\qquad
p_{uv}(q)\ge0.
\tag{10}
\]

The ray

\[
z=\sqrt{2q}\,a
\]

is invariant. On this ray,

\[
a'=qa^2,
\qquad
g=qa^3.
\]

Starting at \(a(0)=1\),

\[
g(\tau)=\frac{q}{(1-q\tau)^3}.
\]

Comparison of Taylor coefficients gives the exact identity

\[
P_k(1,\sqrt{2q};q)
=
q^{k+1}\binom{k+2}{2}.
\tag{11}
\]

This scalar branch is not a toy external to the network. It is the exact word
obtained from the full derivation by selecting the \(q_n(a\odot z)\) term in
(1) at every hit and never differentiating \(q_n\).

---

## 4. Why the full network cannot cancel this branch

In the independent primitive Gaussian coordinates,

\[
f_n
=
\frac1{8n}
\sum_{j,i,\ell}
a_jW_{ji}W_{j\ell}(z_i^{(1)})^2(z_\ell^{(1)})^2.
\tag{12}
\]

Every numerical coefficient in (12) is nonnegative. Every component of the
readout-ascent vector field is a partial derivative of this polynomial times a
positive learning-rate factor, so it also has nonnegative polynomial
coefficients.

Consequently, if a polynomial has nonnegative coefficients, applying
\(D_{+,n}\) preserves that property. Hence every product-rule history in
\(D_{+,n}^kf_n\) has nonnegative primitive polynomial coefficients.

For independent centered Gaussians, the expectation of a primitive monomial is
zero if any exponent is odd and positive if every exponent is even. Therefore
every omitted history has nonnegative Wick expectation. In particular, the
embedded \(\mathscr D_0^k\) history is a genuine lower bound after expectation;
there is no cancellation loophole.

Conditionally on the first-layer activations,

\[
z_j\sim N(0,\gamma q_n),
\qquad
a_j\sim N(0,1),
\]

independently, and

\[
q_n\longrightarrow q_0:=\mathbb E[h^2]=\frac34.
\tag{13}
\]

The current exact quadratic decorated-forest compiler supplies the annealed
limit in (3) by an exact derivative grammar, leading-width Wick selection,
and factorization.  It does not supply concentration of the random quantity
\(D_{+,n}^kf_n(0)/k!\), convergence in probability or \(L^1\), or a
width/time derivative interchange theorem.

---

## 5. Factorial lower bound and zero radius

Let

\[
A\sim N(0,1),
\qquad
Z\sim N(0,\gamma q_0)
\]

be independent, and set

\[
b_\gamma=\frac12\min\left\{1,\frac\gamma2\right\}>0.
\tag{14}
\]

For \(u+v=m\), Gaussian moments give

\[
\frac{\mathbb E[A^{2u}Z^{2v}]}{(2q_0)^v}
=(2u-1)!!(2v-1)!!\left(\frac\gamma2\right)^v.
\]

Using the convention \((-1)!!=1\) at the endpoint cases \(u=0\) or \(v=0\),
and then using

\[
(2u-1)!!\ge u!,
\qquad
(2v-1)!!\ge v!,
\qquad
u!v!=\frac{m!}{\binom mu}\ge\frac{m!}{2^m},
\]

we obtain

\[
\mathbb E[A^{2u}Z^{2v}]
\ge
m!b_\gamma^m(2q_0)^v.
\tag{15}
\]

Combining (10), (11), and (15), then using the no-cancellation comparison with
the full network, proves the main theorem.

> **Zero-radius theorem.** For every odd \(k\), with
> \(m=(k+3)/2\),
> \[
> c_k
> \ge
> m!b_\gamma^m q_0^{k+1}\binom{k+2}{2}.
> \tag{16}
> \]
> Consequently,
> \[
> \limsup_{k\to\infty}c_k^{1/k}=+\infty.
> \tag{17}
> \]

Indeed, Stirling's formula gives

\[
(m!)^{1/k}\asymp\sqrt{k}.
\]

For the variance-normalized value \(\gamma=4/3\), one may take

\[
b_\gamma=\frac13,
\]

so (16) becomes

\[
c_k
\ge
m!\,3^{-m}\left(\frac34\right)^{k+1}
\binom{k+2}{2}.
\tag{18}
\]

Thus no estimate of the form

\[
|c_k|\le CR^{-k}
\]

holds for any \(R>0\). If a macroscopic profile \(F\) exists and its
derivatives satisfy \(F^{(k)}(0)=k!c_k\), then \(F\) is not analytic at zero
and its Taylor series does not represent it. Without that identification, the
unconditional statement is that the **formal limiting Wick series** has radius
zero.

---

## 6. Direct failure of the one-source PDE in physical time

The conclusion is stronger than failure of a complex-analytic proof.

All statements in this section use the conjecture's prescribed iterated order:
first take \(n\to\infty\) at each fixed Wick order, and then let the truncation
order \(M\to\infty\). They do not assert failure of a fixed-\(n\) Taylor germ
inside its own random radius, nor do they analyze a coupled diagonal \(M=M(n)\).

All limiting coefficients \(c_k\) are nonnegative, and \(c_0=0\). By (17), for
every fixed \(s>0\), the terms \(c_ks^k\) fail to tend to zero along the odd
subsequence. Hence

\[
F_M(s)=\sum_{k=0}^M c_ks^k\longrightarrow+\infty
\qquad(s>0).
\tag{19}
\]

For \(y\in(0,1)\), let \(r_M(y)\) be the first positive source point satisfying

\[
F_M(r_M(y))=y.
\]

If \(k\le M\) is odd, then

\[
y=F_M(r_M(y))\ge c_kr_M(y)^k,
\]

so

\[
r_M(y)\le\left(\frac{y}{c_k}\right)^{1/k}.
\]

Taking increasing odd \(k\) gives

\[
r_M(y)\longrightarrow0.
\tag{20}
\]

The characteristic clock for (5) satisfies

\[
\dot s_M=2(1-F_M(s_M)),
\qquad
s_M(0)=0.
\]

The physical time needed to reach output \(y\) is

\[
t_M(y)
=
\int_0^{r_M(y)}\frac{ds}{2(1-F_M(s))}
\le
\frac{r_M(y)}{2(1-y)}
\longrightarrow0.
\tag{21}
\]

Therefore, for every fixed \(t>0\),

\[
f_M(t)\longrightarrow1,
\qquad
\mathcal L_M(t)\longrightarrow0,
\tag{22}
\]

whereas

\[
\mathcal L_M(0)=1
\qquad\text{for every }M.
\tag{23}
\]

The pointwise limit is the discontinuous step

\[
\mathcal L_\infty(t)
=
\begin{cases}
1,&t=0,\\
0,&t>0.
\end{cases}
\]

Since every \(\mathcal L_M\) is continuous, uniform convergence on any
\([0,T]\), \(T>0\), is impossible. In fact the family is not uniformly Cauchy.

This alone refutes (8), independently of whether the true finite-width loss
curves possess a regular large-width limit. If (8) held, then the bounded
metric triangle inequality gives, for any \(M,M'\),

\[
d_T(\mathcal L_M,\mathcal L_{M'})
\le
\limsup_{n\to\infty}\mathbb E\!\left[
d_T(\mathcal L_M,\mathcal L_n)
+d_T(\mathcal L_n,\mathcal L_{M'})
\right],
\]

which would force \((\mathcal L_M)\) to be uniformly Cauchy, a contradiction.

Squared-loss residual gating has therefore not failed as a stability mechanism.
Rather, its hypothesis has failed: the truncation defect does not tend to zero.
Increasing \(M\) inserts increasingly large Gaussian-moment responses and moves
the predicted transition toward time zero.

---

## 7. A finite-width check: real stability does not imply a Taylor disk

There is also an exact deterministic illustration inside the full network. The
symmetric manifold

\[
z_i^{(1)}=\zeta,
\qquad
a_j=a,
\qquad
W_{ji}=\frac wn
\]

is invariant under feature ascent. On it,

\[
f=\frac18aw^2\zeta^4,
\quad
a'=\frac18w^2\zeta^4,
\quad
w'=\frac14aw\zeta^4,
\quad
\zeta'=\frac12aw^2\zeta^3.
\]

Choose

\[
a(0)=-1,
\qquad
w(0)=2,
\qquad
\zeta(0)=\sqrt8.
\]

The invariants

\[
w^2-2a^2=2,
\qquad
\zeta^2-4a^2=4
\]

reduce the dynamics to

\[
a'=4(1+a^2)^3,
\qquad
f=4a(1+a^2)^3.
\]

The forward orbit crosses zero and reaches \(f=1\). Its backward blow-up
distance obeys

\[
B
=
\int_1^\infty\frac{ds}{4(1+s^2)^3}
\le\frac1{64},
\]

while the target time is larger than the time needed merely to reach \(a=0\):

\[
\tau_*
>
\int_0^1\frac{ds}{4(1+s^2)^3}
\ge\frac1{32}.
\]

Thus its Taylor radius is smaller than its target-reaching feature time even
though squared-loss physical dynamics are bounded and converge gracefully.
Real-axis stability cannot provide the complex-disk estimate used in the
original argument.

---

## 8. What remains true: the observable stability theorem

Suppose some independently constructed monotone profile \(\widetilde F\)
approximates the true feature profile \(F\) on a common target-reaching interval
and

\[
0<\mu\le F'\le K,
\qquad
\|F-\widetilde F\|_\infty\le\varepsilon.
\]

Let the two squared-loss clocks be driven by \(F\) and \(\widetilde F\). The
previous clock-comparison proof remains valid:

\[
\sup_{t\ge0}|\widetilde\tau(t)-\tau(t)|
\le\frac\varepsilon\mu,
\]

\[
\sup_{t\ge0}|\widetilde f(t)-f(t)|
\le
\left(1+\frac K\mu\right)\varepsilon,
\]

and

\[
\sup_{t\ge0}
|\widetilde{\mathcal L}(t)-\mathcal L(t)|
\le
2(1-f_0)
\left(1+\frac K\mu\right)\varepsilon.
\tag{24}
\]

The derivative bounds can be replaced by a strict-monotonicity separation
modulus if only qualitative convergence is needed. Thus the global loss
observable is genuinely input-to-state stable. Equation (24) simply cannot be
applied with \(\varepsilon=\|F-F_M\|_\infty\), because that quantity does not
tend to zero for the Wick--Taylor sequence.

---

## 9. Current classification

The following table separates resolved formal/compiler statements from the
remaining concentration and trajectory questions.

| Claim | Verdict |
|---|---|
| Squared loss turns a known small residual-compatible defect into a bounded global loss error | True |
| Fixed-order annealed derivative/Wick coefficients exist | True for this exact special quadratic compiler |
| The random derivatives concentrate at those coefficients | Open |
| The formal annealed initial Taylor series has positive radius | False; its radius is zero |
| The degree-\(M\) zero-flux source jet approximates an identified feature orbit | Not established; the prescribed family is internally non-Cauchy |
| The prescribed PDE losses converge uniformly in physical time | False for that closure family |
| The formal jet is the derivative jet of an actual positive-time mean-field curve | Open |
| Real target fitting implies the target lies inside the initial Taylor disk | False |
| Every possible non-Taylor finite-source approximation is impossible | Not proved and not implied |

The last row is not a technical caveat. An unrestricted statement saying
"there exists some finite model" is not a determinate non-cheating conjecture
until the admissible compiler, information access, approximation norm, and
order of the width/refinement limits are fixed. A resummation may use the same
divergent coefficients nonlocally; a real-axis Galerkin method need not use the
initial Taylor series at all.

A legitimate non-Taylor candidate is a finite feature-time Picard or
Runge--Kutta program generated only from the polynomial network vector field,
followed by finite Wick contraction and a positivity-preserving polynomial
compression of its approximate tangent kernel. Another is projection of the
message hierarchy onto diagrams of grade at most \(M\).

For either construction, the missing model-specific statement is a genuinely
nonperturbative real-axis estimate such as

\[
\lim_{h\downarrow0}\limsup_{n\to\infty}
\Pr\!\left[
\int_0^T
|\widehat\kappa_{n,h}(s)-\kappa_n(\Theta_n(s))|\,ds
>\delta
\right]=0,
\tag{25}
\]

or a weighted message-Galerkin residual bound \(\rho_M\to0\). Fixed-program
Wick convergence does not justify the diagonal limit in (25).

The obvious worst-case ODE estimate is unavailable: already at initialization,
the scaled Hessian contains row blocks of norm

\[
|z_j|\sqrt{q_n},
\]

so its operator norm grows at least like \(\sqrt{\log n}\) under Gaussian
initialization. In the frozen-first-layer subsystem, rare Gaussian upper
neurons rigorously create a feature-time boundary layer. For the fully trained
model the same mechanism is plausible, but a componentwise comparison is not
currently valid because \(K_n(a\odot z)\) need not have the sign of
\(a\odot z\). It would be incorrect to claim that boundary-layer theorem for
the full model without a new proof.

Accordingly, (25) is a **different conjecture**, not a remaining step in the
Wick--Taylor proof. It may require bounded or truncated initialization, a
weighted real-axis hierarchy space, an explicit fast-time variable, or a
justified resummation.

---

## Final conclusion

The prescribed approximate one-source PDE family built from the formal
annealed Wick jet is not merely unproved; it is internally non-Cauchy. The
factorial Gaussian-moment tail forces zero Taylor radius, collapse of that
family's target times, and failure of uniform physical-time convergence. This
is not a theorem that the actual Gaussian quadratic network loss is a step or
that every finite PDE fails.

The genuinely positive insight survives intact: squared loss makes the loss
observable stable **once** a small residual-compatible feature-profile error
has been established. What it cannot do is make a divergent hierarchy
truncation small.

Thus the exact resolution is:

> **Global loss stability under its hypotheses: proved. The prescribed formal
> Wick--Taylor closure family: disproved.**
> Any affirmative approximate-PDE theorem for the same Gaussian full model must
> be nonperturbative and real-axis in nature; it cannot be obtained by summing
> or truncating the fixed-order Wick/Taylor jet in the ordinary sense.

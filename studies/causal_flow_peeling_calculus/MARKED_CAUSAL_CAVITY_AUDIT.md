# Marked Causal Cavity Peeling: Exact Skeleton and Failed Completion Gate

## Verdict

Marked-neuron cavity peeling has a sound and reusable **finite-width
skeleton**:

- an internal neuron is exposed by deleting its upper source column and its
  lower incident source row;
- the two removed stars are independent of the rerun cavity flow;
- the exposed forward and backward fields split into conditional Gaussian
  innovations plus order-one learned/Onsager response;
- the correct perturbation norm is anisotropic: order one at the marked
  coordinate and order `n^-1/2` in normalized bulk fields.

The proposed completion certificate does not survive audit.  Its
square-exponential response occupation is infinite at every finite width,
already at initialization, for every positive exponent.  Replacing that
weight by exponential-linear moments removes the immediate Gaussian
singularity, but propagating the corresponding response-weighted estimate is
the same unresolved reachable-stability mechanism needed for mesh removal.
Thus the cavity construction is retained as an exact diagnostic/calculus
component and rolled back as a completed proof machinery.

## 1. Exact source and learned-feedback identities

For every layer,

\[
 G_l(t)=\Gamma_l+int_0^t b_{l+1}(s)\otimes_nx_l(s)\,ds.
\]

Consequently, with

\[
 Q_l(s,t)=\langle x_l(s),x_l(t)\rangle_n,
 \qquad
 P_{l+1}(s,t)=\langle b_{l+1}(s),b_{l+1}(t)\rangle_n,
\]

one has exactly

\[
 z_{l+1}(t)
 =\Gamma_lx_l(t)+\int_0^tQ_l(s,t)b_{l+1}(s)\,ds,
\tag{1}
\]

\[
 r_l(t)
 =\Gamma_l^\top b_{l+1}(t)
  +\int_0^tP_{l+1}(s,t)x_l(s)\,ds.
\tag{2}
\]

The Volterra terms in (1)--(2) are order one.  Treating them as a negligible
cavity error, or refreshing the transpose source, changes the model.

There is also an exact lower tangent recursion.  If

\[
 D_l=\operatorname{diag}\phi'(z_l),\qquad
 \Theta_1=I,
\]

then

\[
 \Theta_{l+1}
 =\|x_l\|_n^2I+G_lD_l\Theta_lD_lG_l^\top,
 \qquad z_l'=\Theta_lb_l.
\tag{3}
\]

Hence `Theta_l` is positive semidefinite.  The backward/upper response has no
corresponding sign because `A phi''` and `phi'' r_l` change sign.

## 2. Exact one-star and two-star cavities

For a column `j` of source `Gamma_a`, write

\[
 \gamma^+=\Gamma_ae_j,
 \qquad
 \Gamma_a^\circ=\Gamma_a(I-e_je_j^\top).
\]

The valid cavity reruns the entire flow from `Gamma_a^circ`; deleting the
column only in a final contraction does not create independence.  The rerun
flow is measurable with respect to all undeleted data and is exactly
independent of `gamma+`.

For an internal neuron `(a,j)`, a closed marked description also deletes

\[
 \gamma^-=\Gamma_{a-1}^\top e_j,
 \qquad
 \Gamma_{a-1}^\circ=(I-e_je_j^\top)\Gamma_{a-1}.
\tag{4}
\]

The two stars in (4) are mutually independent and independent of the
double-cavity trajectory.  One column is enough to decouple a marked
transpose contraction.  Both stars are necessary to describe jointly the
forward and backward fields of an internal neuron.

The natural marked norm is

\[
 \|\delta v\|_{\star,j}
 =|\delta v_j|
  +\sqrt n\|(I-e_je_j^\top)\delta v\|_n.
\tag{5}
\]

The preregistered C1 experiment supports (5) through `T=0.5`: the marked
`r_2` response is order one, while every tested bulk field has width exponent
near `-1/2`.  This is empirical evidence only; see
`experiments/C1_MARKED_COLUMN_CAVITY_RESULTS.md`.

## 3. Gaussian innovation and the necessary Onsager term

In the cavity environment,

\[
 \eta_a^+(t)=(\gamma^+)^\top b_{a+1}^\circ(t),
 \qquad
 \eta_a^+\mid\mathcal F^\circ
 \sim \operatorname{GP}(0,P_{a+1}^\circ),
\tag{6}
\]

and analogously the lower innovation has covariance `Q_(a-1)^circ`.
The full marked contraction also contains the response to its own exposed
star.  In the static cell

\[
 \gamma_i=g_i/\sqrt n,
 \qquad b_i=\psi(h_i+\gamma_iq),
\]

one has

\[
 \gamma^\top b
 =n^{-1/2}\sum_i g_i\psi(h_i)
 +q\,n^{-1}\sum_i g_i^2\psi'(h_i)+o_P(1).
\tag{7}
\]

The second term in (7) is order one.  A valid limiting marked equation must
retain the analogous causal trace/Onsager response.

## 4. Exact upper-star response at depth three

At initialization perturb the upper matrix by

\[
 \delta G_2=\gamma e_j^\top,
 \qquad \gamma\sim N(0,n^{-1}I),
\]

and put `q=x_(2j)` and

\[
 C_3=\operatorname{diag}(A\phi''(z_3)).
\]

Then

\[
 \delta z_3=\gamma q,
 \qquad
 \delta b_3=C_3\gamma q,
\]

\[
 \boxed{
 \delta r_2=e_j\gamma^\top b_3+qG_2^\top C_3\gamma.}
\tag{8}
\]

Equation (8) proves the anisotropic scaling: the first term is a direct
order-one marked response, while each unmarked coordinate of the second term
is typically `O(n^-1/2)`.

For a lower-star perturbation `alpha~N(0,n^-1 I)`, the first nonzero lower
return is

\[
 \delta z_2(t)=tG_1D_1^2\alpha+O(t^2).
\tag{9}
\]

These are actual-flow response directions, not arbitrary ambient tangents.

## 5. Falsification of the square-exponential certificate

At `t=0`, condition on

\[
 \mathcal H=\sigma(u(0),G_1(0),G_2(0)).
\]

Since `A(0)` is an independent standard Gaussian vector,

\[
 r_{2i}
 =\sum_{m=1}^nG_{2,mi}A_m\phi'(z_{3m})
\]

is conditionally Gaussian with variance

\[
 S_i=\sum_{m=1}^nG_{2,mi}^2\phi'(z_{3m})^2.
\tag{10}
\]

The random variable `S_i` has unbounded support.  Indeed, with positive
probability `x_(2i)` is arbitrarily small, one entry `G_(2,mi)` is arbitrarily
large, and the remaining contribution to `z_(3m)` is small.  On this event
`phi'(z_(3m))` stays bounded below while the corresponding term in (10) is
arbitrarily large.

For a centered Gaussian of variance `s`,

\[
 \mathbb E e^{\lambda Z^2}
 =(1-2\lambda s)^{-1/2}
\]

when `2 lambda s<1`, and the expectation is infinite otherwise.  Because
(10) crosses every fixed threshold with positive probability,

\[
 \boxed{
 \mathbb E e^{\lambda r_{2i}(0)^2}=+\infty
 \quad\text{for every }\lambda>0
 \text{ and every finite }n.}
\tag{11}
\]

The same obstruction persists after multiplying by the squared actual upper
response in (8), and after multiplying by the leading lower response in
(9), on positive-probability events where those responses are nonzero.
Therefore the proposed uniform estimate

\[
 \mathbb E\langle e^{\lambda r_2^2}|V|^2,1\rangle_n
 \le C\,\mathbb E\langle|V|^2,1\rangle_n
\]

is false, not merely unproved.

## 6. What an additional mark actually computes

Let `c~N(0,n^-1 I)` be independent of cavity data, put

\[
 \eta=c^\top b,\qquad q=n^{-1}\|b\|_2^2,
\]

and let `K` be cavity-measurable and positive semidefinite.  Exact Gaussian
integration gives

\[
\begin{aligned}
 \mathbb E_c[e^{\lambda\eta^2}c^\top Kc]
 ={}&(1-2\lambda q)^{-1/2}\Big[
 n^{-1}\operatorname{Tr}K\\
 &+\frac{2\lambda}{n^2(1-2\lambda q)}b^\top Kb
 \Big],
\end{aligned}
\tag{12}
\]

when `2 lambda q<1`; otherwise it diverges in the relevant directions.  A
second mark therefore exposes random trace and aligned quadratic-form terms
and a singular denominator.  It does not make the weight independent of the
response.

For a linear exponential, however,

\[
 \mathbb E_c[e^{\theta\eta}c^\top Kc]
 =e^{\theta^2q/2}
 \left[n^{-1}\operatorname{Tr}K
 +\theta^2n^{-2}b^\top Kb\right].
\tag{13}
\]

Equation (13) has no finite-radius singularity and is compatible with
exponential-linear/subexponential certificates.

There is a matching exact initialization bound.  From (10),

\[
 S_i\le\sum_mG_{2,mi}^2.
\]

Conditioning first on the matrices and then using the chi-square moment
bound for one Gaussian column gives, for every `p>=2`,

\[
 \|r_{2i}(0)\|_p
 \le C\sqrt p\,\|S_i^{1/2}\|_p
 \le Cp,
\tag{14}
\]

uniformly in width.  Thus the rare event that kills every
square-exponential norm still lies in the endpoint subexponential class.
The open issue is propagating (14), jointly with response occupation,
through positive time.

## 7. The repaired route and why it is not yet a reduction

A repaired certificate would control, for every fixed `kappa`,

\[
 \limsup_n\mathbb E\sup_{t\le T}
 \langle e^{\kappa(|A|+|r_2|)},1\rangle_n
\tag{15}
\]

and, for every unit star-generated bulk response `V`,

\[
 \limsup_n n\mathbb E\sup_{t\le T}
 \langle e^{\kappa(|A|+|r_2|)}|V|^2,1\rangle_n.
\tag{16}
\]

The exact arctangent tangent energy produces precisely the weighted
occupation

\[
 \langle(|A|+|r_2|)
 (|\delta z_2|^2+|\delta z_3|^2),1\rangle_n.
\tag{17}
\]

If (15)--(16) were known, (17), clipping, uniform Euler comparison, and the
one-time restartable state would follow by standard estimates.  But a
two-star cavity does not prove (16).  Its comparison remainder requires
response-weighted first and second causal-response bounds, and those bounds
are governed by (17) itself.

Thus (15)--(16) are logically narrower than full convergence but not yet
technically simpler: they are the missing reachable-stability bridge in
another form.  Until a separate summation/factorization theorem proves them,
the repaired cavity route fails the program's genuine-reduction gate.

## 8. Claim ledger

| Claim | Status |
|---|---|
| Exact source plus learned-feedback identities (1)--(2) | Proved |
| Exact one-column and two-star independence | Proved |
| Conditional Gaussian innovations | Proved |
| Order-one causal/Onsager self-response | Proved structurally; cannot be omitted |
| Anisotropic marked/bulk scaling at initialization | Proved |
| Same scaling on sampled D3 trajectories through `T=0.5` | Empirically supported |
| Square-exponential value/response certificate | Falsified by (11)--(12) |
| Additional mark literally factors weight and response | Falsified |
| Exponential-linear integration and `||r_2(0)||_p<=Cp` | Proved by (13)--(14) |
| Compact-time exponential-linear response occupation | Open; currently equivalent in burden to reachable stability |
| Marked cavity completes D3 mesh removal | Not established |

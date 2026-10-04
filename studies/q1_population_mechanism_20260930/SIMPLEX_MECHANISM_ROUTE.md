# Triangle route: unavoidable hidden contrast under one common label

Frozen first candidate: 2026-09-30. Author: scoped agent
`simplex_mechanism_route`. Scientific inputs: the supervisor's self-contained
assignment only. Process inputs: root `AGENTS.md`, workflow Part 1, the
`investigate-conjectures` skill and its research-contract/adversarial-audit
references, and `solve-math-rigorously`. No book, other route, other study,
external source, experiment, or numerical estimate was used.

The question is whether the actual infinite-population q1 flow has a concrete
feature-learning mechanism on a small fixed dataset. The candidate is an
equilateral triangle with all three labels equal to +1. Its content combines
an exact, all-time representation obstruction with a strictly positive
conditional feature innovation in the actual flow. It is not a finite-width
argument and not a closed reduced model.

## 1. Object and regularity contract

Take

\[
u_1=(1,0),\quad u_2=(-1/2,\sqrt3/2),\quad
u_3=(-1/2,-\sqrt3/2),\qquad y_a=1.
\]

Thus \(\sum_a u_a=0\), \(u_a\cdot u_b=-1/2\) for \(a\ne b\), and
\(\sum_a u_au_a^T=(3/2)I_2\). Use precisely the q1 equations supplied in
the assignment, with canonical fixed Gaussian \(T\), its true transpose,
\(A_0\sim N(0,I_2)\), \(W_0=V_{a,0}=0\), \(K_{a,0}=H_{a,0}\), and
\(\tau_0=1\). No activation, initialization, metric, or optimizer is changed.

Conditional on a unique regular equivariant population flow, all training
predictions equal a common \(f\). Locally \(f<1\), and the feature clock
\(s=2\int_0^t(1-f(v))\,dv\) gives

\[
W'=\bar G,\quad V_a'=D_a,\quad
A'=\frac13\sum_a L_a u_a,\quad K_a'=\frac{H_a-K_a}{s+2},
\qquad \bar G=\frac13\sum_aG_a.
\]

The all-time algebra below needs no flow existence assumption: it holds for
every finite readin vector at every state where the model is defined. The
acceleration calculation needs the displayed equations twice differentiable
at initialization, the supplied first-transpose law, and the permitted
expectation/derivative exchanges. The finite-small-time innovation conclusion
assumes \(A(s)=A_0+s^2B/2+o_{L^2}(s^2)\); this is explicitly a conditional
regularity requirement, not a construction or well-posedness theorem. For the
corresponding feature expansion, use this expansion in \(L^4\). The stronger
null-condition illustration in Section 5 requires the stated conditional jet.

## 2. Exact all-time obstruction: common-label features require contrast

For any \(a\in\mathbb R^2\), put \(x_i=a\cdot u_i\) and
\(h_i=\tanh x_i\). Since \(x_1+x_2+x_3=0\), the addition formula gives

\[
h_1+h_2+h_3=-h_1h_2h_3. \tag{2.1}
\]

For completeness, \(h_3=-(h_1+h_2)/(1+h_1h_2)\), with strictly positive
denominator because \(|h_1h_2|<1\). Rearrangement proves (2.1).
Define the label component \(\bar h=(h_1+h_2+h_3)/3\), and the contrast
energy \(c(h)=\frac13\sum_i(h_i-\bar h)^2\). Then

\[
\bar h^2=\frac19h_1^2h_2^2h_3^2
\le\frac1{27}\sum_i h_i^2,
\qquad c(h)\ge8\bar h^2. \tag{2.2}
\]

Indeed, each \(h_i^2\le1\), so the product of the three squares is no
larger than each square, hence no larger than their average. Subtracting
\(\bar h^2\) from \(\frac13\sum h_i^2\) proves the second inequality.
The constant 8 is sharp as a supremal boundary value: take
\((x_1,x_2,x_3)=(r,r,-2r)\), realizable by a readin vector, and let
\(r\to\infty\). Then \(h\to(1,1,-1)\), so
\(c(h)/\bar h^2\to8\). For every finite nonzero readin with
\(\bar h\ne0\), the inequality is strict.

Consequently, for every population law of finite readins, at every time,

\[
\frac13\sum_i\|H_i-\bar H\|_{L^2(\Omega_1)}^2
\ge8\|\bar H\|_{L^2(\Omega_1)}^2. \tag{2.3}
\]

Thus at least eight ninths of the first-layer sample feature energy lies in
contrasts. A common-label representation cannot become dominant in this
layer. Exact within-class feature collapse \(H_1=H_2=H_3\) forces all
three to vanish, since tanh is injective and the three preactivations sum to
zero. Under the triangle symmetry, if the first-layer Gram matrix has
common-label eigenvalue \(\lambda_+\) and the repeated contrast eigenvalue
\(\lambda_-\), (2.3) reads

\[
\lambda_-\ge4\lambda_+.
\]

These are restrictions on the instantaneous first layer, not on temporal
keys \(K\), the second layer \(G\), or the readout. In particular they do
not obstruct fitting the labels by the full network.

The identity also identifies the lowest possible nonzero common-label
feature degree. Near \(a=0\),

\[
\bar h=-\frac13\prod_i(a\cdot u_i)+O(|a|^5)
=-\frac1{12}a_x(a_x^2-3a_y^2)+O(|a|^5). \tag{2.4}
\]

The first term is cubic; the linear term vanishes because the data are
centered. No fitting or asymptotic limit is used in (2.1)--(2.3).

## 3. Initial Gaussian law is nondegenerate

In the rest of the note lowercase \(h_a\) means \(H_a(0)\). Let
\(z_a=(Th_a)(0)\), \(g_a=\tanh z_a\),
\(q_a=1-g_a^2\), and \(\bar g=(g_1+g_2+g_3)/3\).
The supplied initialization law makes \(z\) a centered Gaussian with
covariance \(C_{ab}=\mathbb E_1h_ah_b\). By symmetry its diagonal is
\(\kappa\), its off-diagonal is \(\chi\), and

\[
\kappa+2\chi=\frac13\mathbb E_1(h_1+h_2+h_3)^2>0,
\qquad
\kappa-\chi=\frac12\mathbb E_1(h_1-h_2)^2>0. \tag{3.1}
\]

The first strict inequality follows from (2.1): the product \(h_1h_2h_3\)
is nonzero on an open set of readins of positive Gaussian probability.
The second follows from \(u_1\ne u_2\) and strict monotonicity of tanh.
These are all eigenvalues of \(C\), so \(z\) has a positive density on
\(\mathbb R^3\).

## 4. Actual q1 flow creates strictly positive latent contrasts

At initialization \(D_a=L_a=0\), hence \(A'=V_a'=K_a'=0\),
\(W'=\bar g\), and \(Z_a'=G_a'=0\). Therefore

\[
D_a'(0)=U_a:=\bar gq_a,
\quad V_a''(0)=U_a,
\quad B:=A''(0)=\frac13\sum_a p_a u_a T^*U_a,
\qquad p_a=1-h_a^2. \tag{4.1}
\]

The memory part of \(L_a\) makes no contribution here: it contains
\(V_bD_a\), and both factors vanish at initialization. The factor
\((1-H_a^2)\) has zero first derivative at initialization because
\(A'=0\).

Each \(U_a(z)=\bar gq_a\) is bounded and has bounded first derivatives.
The supplied true-transpose law is therefore directly applicable:

\[
T^*U_a=\sum_b\beta_{ab}h_b+\xi_a,
\qquad \beta_{ab}=\mathbb E_2\partial_b U_a,
\qquad \operatorname{Cov}(\xi_a,\xi_b)=M_{ab}:=\mathbb E_2 U_aU_b, \tag{4.2}
\]

where the centered jointly Gaussian \(\xi\) uses roots independent of
\(A_0\). Importantly, the covariance is the full Gram matrix \(M\).
Differentiating \(U\) explicitly gives

\[
\beta_{aa}=d:=\frac13\mathbb E_2q_a^2
-2\mathbb E_2\bar g g_aq_a,
\qquad
\beta_{ab}=o:=\frac13\mathbb E_2q_aq_b>0\quad(a\ne b). \tag{4.3}
\]

Write \(M_d=\mathbb E_2\bar g^2q_1^2\),
\(M_o=\mathbb E_2\bar g^2q_1q_2\), and

\[
\delta=M_d-M_o
=\frac12\mathbb E_2\bar g^2(q_1-q_2)^2>0. \tag{4.4}
\]

Both \(M_o>0\) and the strict inequality in (4.4) follow from full Gaussian
support. For example, a neighborhood of \(z=(1,0,0)\) has
\(\bar g\ne0\), \(q_1\ne q_2\), and all \(q_a>0\). Hence

\[
M=\delta I_3+M_o\mathbf1\mathbf1^T
\]

is positive definite. In particular, the transpose response contains
strictly positive sample contrasts despite the identical labels.

Conditional on \(A_0=a\), (4.1)--(4.3) make \(B\) a Gaussian with mean

\[
\mu(a)=\frac13\sum_i p_i u_i\left[(d-o)h_i+o\sum_jh_j\right] \tag{4.5}
\]

and covariance

\[
\begin{split}
\mathcal C(a)
&=\frac\delta9\sum_i p_i^2u_iu_i^T
+\frac{M_o}9\left(\sum_i p_i u_i\right)
\left(\sum_i p_i u_i\right)^T,\\
\mathcal C(a)&\succeq
\frac\delta6\min_i p_i^2 I_2\succ0. \tag{4.6}
\end{split}
\]

The bound uses \(p_i>0\) at every finite \(a\) and
\(\sum_i u_iu_i^T=(3/2)I_2\). Thus every input direction gets genuinely
new source dependence at the first nonzero feature-learning order. At the
continuous conditional value \(a=0\),

\[
\mu(0)=0,\qquad\mathcal C(0)=\frac\delta6 I_2. \tag{4.7}
\]

There the common Gaussian transpose mode cancels by \(\sum u_i=0\);
the entire nonzero acceleration covariance comes from the contrast mode
\(\delta\). This is a precise mechanism: second-layer saturation makes
the derivatives \(q_i\) unequal, and the reused transpose converts those
sample contrasts into a nonzero learning acceleration of the readin.
If the second-layer derivative were constant, the contrast variance
\(\delta\) would vanish. This is an algebraic mechanism comparison, not
a claim that an altered linear-activation model solves the original task.

## 5. Finite-small-time consequences, with the exact regularity exposed

Suppose the conditional population flow has the \(L^2\) jet specified in
Section 1. Conditional expectation is an orthogonal projection in \(L^2\),
so applying it to that jet and subtracting gives

\[
\begin{split}
\inf_{\Psi\,\mathrm{measurable}}
\mathbb E_1|A(s)-\Psi(A_0)|^2
&=\mathbb E_1|A(s)-\mathbb E_1[A(s)\mid A_0]|^2\\
&=\frac{s^4}4\mathbb E_1\operatorname{tr}\mathcal C(A_0)+o(s^4),
\end{split} \tag{5.1}
\]

and the coefficient is finite and strictly positive. Finiteness follows
from bounded \(p_i\) and the finite Gaussian Gram \(M\); strict positivity
follows pointwise from (4.6). Thus every sufficiently small positive time
has strictly positive conditional feature innovation. No deterministic
transport of \(A_0\) alone, even a nonlinear one chosen separately at
each time, matches the learned readin rootwise to error \(o(s^2)\) in
\(L^2\). This is not a no-go theorem for representing the unconditional
law by a transport or for a closure that retains the extra roots.

For the first-layer features, an \(L^4\) readin jet and bounded tanh
derivatives give

\[
H_i(s)=h_i+\frac{s^2}2p_i u_i\cdot B+o_{L^2}(s^2). \tag{5.2}
\]

Every nonzero sample contrast \(c\in\mathbb R^3\) with
\(\sum_i c_i=0\) has strictly positive conditional innovation in this
coefficient. Indeed, let \(v=\sum_i c_ip_iu_i\). If \(v=0\), the only
linear dependence among the three \(u_i\) implies \(c_ip_i=k\) for all
\(i\). Then \(0=\sum_i c_i=k\sum_i1/p_i\), giving \(k=0\) and
\(c=0\), a contradiction. Therefore
\(v^T\mathcal C(a)v>0\). The same conditional-projection argument as
(5.1) converts this to a positive order-\(s^4\) mean-square innovation
for each nonzero sample contrast. This establishes actual feature motion;
a frozen-feature readout cannot exhibit it.

One illuminating, more local illustration concerns the continuous
conditional jet at \(A_0=0\). If the flow admits this conditional jet in
\(L^6\), then with \(B\sim N(0,(\delta/6)I_2)\),

\[
H_i(s)=\frac{s^2}2(u_i\cdot B)+o_{L^6}(s^2),\qquad
\bar H(s)=-\frac{s^6}{24}\prod_i(u_i\cdot B)+o_{L^2}(s^6). \tag{5.3}
\]

The second identity is obtained from the exact product identity (2.1),
not from a sixth derivative of the flow. Its leading random polynomial is
nonzero, whereas hidden contrasts are already order \(s^2\). Because
\(\{A_0=0\}\) is a null event, (5.3) is only a statement about a
continuous conditional version and is not needed for (5.1)--(5.2).
The nondegenerate neighborhood bound (4.6) and the integrated innovation
theorem (5.1) avoid any null-event interpretation.

## 6. Exact prediction restrictions and the minimality of three samples

At any defined state the full predictor is odd in a query input:
\(H(-u)=-H(u)\), both terms of \(Z\) are linear in \(H(u)\),
\(G(-u)=-G(u)\), and hence \(F(-u)=-F(u)\). Under a unique equivariant
flow, \(F\) is invariant under the triangle's rotations and reflections.
Writing a unit query as \((\cos\theta,\sin\theta)\), these facts imply

\[
F(\theta+2\pi/3)=F(\theta),\qquad
F(\theta+\pi/3)=-F(\theta),\qquad F(-\theta)=F(\theta).
\]

Set \(\theta=\pi/6\). Reflection and the sign rule give
\(F(\pi/6)=-F(-\pi/6)=-F(\pi/6)\), so \(F(\pi/6)=0\).
The same argument applies at all \(\theta=\pi/6+k\pi/3\), and at every
radius. Thus three whole lines of zeros are forced throughout training.
If a limiting state fits the three labels, it predicts \(-1\) at their
antipodes and zero along these three intervening lines. No claim is made
about absence of additional zero lines or the sign inside every sector.

The centered two-point alternative is antipodal. Its identical labels are
incompatible with an odd predictor; at the prescribed zero-readout
initialization, \(\bar g=0\), so \(W,V,A,K\) remain at their initial
values under uniqueness (only the physical clock changes). Three points
are therefore the smallest centered regular-simplex all-plus task that
escapes this exact frozen obstruction while retaining linear cancellation.

## 7. Claim ladder and adversarial checks

* Exact algebra: (2.1)--(2.4), including the sharp 8:1 all-time contrast
  requirement. Does not require a learned-flow construction.
* Exact initialization law, conditional on the Gaussian source contract:
  (3.1) and strict positivity of \(\delta\).
* Conditional flow theorem: (4.1)--(4.7), using the supplied true-transpose
  law and differentiability at zero; (5.1)--(5.2) under the specified norm
  jets. These are direct infinite-population statements.
* Exact symmetry restrictions: Section 6 under the permitted unique
  equivariant-flow assumption.
* Not claimed: population well-posedness, convergence of a Taylor series,
  monotonicity of total contrast energy, a positive finite-time increase in
  that total energy, a closed finite-dimensional law, global fitting,
  global-in-time existence, or endpoint selection.

The mechanism statement concerns *conditional source innovation*, not
necessarily an increase in the unconditional feature variance. A drift can
reduce the latter while new root dependence appears. The positive innovation
is stronger than merely showing \(\|\bar G\|\) initially grows, but it does
not by itself establish that the innovation is needed for fitting or that
the learned prediction outperforms frozen features. The 8:1 bound is an
architecture/geometry fact; combining it with the actual-flow innovation
does not turn either one into a global optimization theorem.

Checks actually performed: direct symbolic derivations of the tanh identity,
its sharp boundary case, Gram eigenvalues, every initial derivative,
the full-transpose covariance, the positive-definite conditional covariance,
and the conditional-projection limit. No software calculation or experiment
was run. Status: frozen author-derived candidate, not independently checked
and not promoted. The supervisor should check this prompt-scoped result
against the complete maintained model before accepting it.

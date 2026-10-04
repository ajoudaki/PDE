# A finite-width obstruction to an unconditional complex-moment shortcut

2026-10-04. Continuation of the normalized-activation investigation. This is
an internally derived theorem about the actual Gaussian initialization,
not a compression lower bound or a statement about real-output error.
Its complete scalar proof is included. The activation normalization is the
one in NORMALIZED_ERF_COMPLEX_GAIN_ROUTE.md; the finite-width argument below
does not assume its limiting Gaussian law for a finite network. No experiment
or unrelated-study input is used.

The conclusion is that taking a finite-network expectation before a width
limit is materially different from taking the Gaussian population limit
first. Even at two hidden layers and at an arbitrarily small nonreal query,
the former second moment is infinite for the explicit normalized erf. The
population moment can be finite. Stopping or exceptional-event control is
therefore necessary for this particular complex-moment proof route.

## 1. Precise statement

Let d>=2 and n>=1. Let A have independent N(0,1) entries, and let W be an
independent n by n matrix with independent N(0,1/n) entries. Put

\[
 h^{(1)}(v)=\phi(Av),\qquad
 h^{(2)}(v)=\phi(W h^{(1)}(v)),
 \qquad \|u\|_{2,n}^2=n^{-1}\sum_i|u_i|^2.
\]

Here phi is the entire activation

\[
 \phi(z)=a z+c\operatorname{erf}(z/\sqrt2)+b,
 \qquad a,b\in\mathbb R,\quad c\in\mathbb R\setminus\{0\}.
 \tag{1}
\]

The usual real network is extended to a complex query by the same algebraic
forward equations. For every real tau != 0 set

\[
 v_\tau=e_1\cosh\tau+i e_2\sinh\tau,
 \qquad v_\tau^\top v_\tau=1.
 \tag{2}
\]

Then at every finite width

\[
 \mathbb E\|h^{(2)}(v_\tau)\|_{2,n}^2=\infty.
 \tag{3}
\]

This includes the bounded-on-the-real-axis critical activation

\[
 a=0,\quad c=\sqrt{\pi\sqrt3/2},\quad
 b=\sqrt{1-\pi/(2\sqrt3)},
 \qquad \mathbb E\phi(Z)^2=\mathbb E\phi'(Z)^2=1.
 \tag{4}
\]

It also includes the normalized unbounded linear-plus-erf activations
constructed in NEARCRITICAL_GEOMETRY_ROUTE.md; the proof needs no result
from that new route, only the explicit form (1). On the real axis all
fixed moments of every fixed-depth initialized feature are finite.

## 2. An elementary lower bound for erf in an imaginary sector

We prove the complex estimate rather than importing an asymptotic formula.
For a complex z, the defining entire integral gives

\[
 \operatorname{erf}(z/\sqrt2)
 =\sqrt{2/\pi}\,z\int_0^1e^{u s^2}\,ds,
 \qquad u=-z^2/2.
 \tag{5}
\]

Fix kappa>0 and consider Re u >= kappa |u| with |u| tending to infinity.
Integration by parts on [1/2,1] gives exactly

\[
 \int_{1/2}^1e^{u s^2}\,ds
 =\frac{e^u}{2u}-\frac{e^{u/4}}u
   +\int_{1/2}^1\frac{e^{u s^2}}{2u s^2}\,ds.
 \tag{6}
\]

Write R=Re u>0. The omitted integral from zero to one half has absolute
value at most e^{R/4}/2. Since 1-s^2 >= 1-s on [1/2,1], the last integral
in (6) has absolute value at most 2e^R/(|u|R). Relative to the magnitude
e^R/(2|u|) of the leading term, the sum of these three errors is at most

\[
 |u|e^{-3R/4}+2e^{-3R/4}+4/R.
\]

It tends to zero uniformly in the fixed cone R>=kappa |u|. In particular,
for sufficiently large |u| the integral in (5) has magnitude at least
e^R/(4|u|). Consequently

\[
 |\operatorname{erf}(z/\sqrt2)|
 \ge \frac12\sqrt{2/\pi}\,
            \frac{\exp[-\operatorname{Re}(z^2)/2]}{|z|}
 \tag{7}
\]

there. The constants and the threshold may depend on the fixed cone but
not on z within its sufficiently large portion. Multiplication by c and
addition of a z+b do not change this exponential lower bound apart from
a factor of two once |z| is sufficiently large, since exponential growth
in this cone dominates every linear function.

## 3. One unusually large first-layer coordinate suffices

For the first row of A, put

\[
 Z=A_{11}\cosh\tau+i A_{12}\sinh\tau,
 \qquad H=\phi(Z)=P+iQ.
\]

The pair (Re Z, Im Z) has a strictly positive density on all of R^2.
At z=iR,

\[
 \phi(iR)=b+i\left[aR+c\sqrt{2/\pi}
                         \int_0^R e^{s^2/2}\,ds\right].
 \tag{8}
\]

The magnitude of the imaginary part is unbounded as R tends to positive
infinity; the real part is b. Continuity therefore shows that the event

\[
 E_n=\{|Q|>2|P|,\quad Q^2-P^2>n/2+1\}
 \tag{9}
\]

has positive probability for every finite n. To see strict positivity
without any tail approximation, choose R for which both inequalities are
strict at (8); a sufficiently small open neighborhood of iR retains them
and has positive probability under Z.

Now condition on all of A. Write the first second-layer preactivation as

\[
 U=W_{11}H+C_A,
 \qquad C_A=\sum_{j=2}^nW_{1j}h_j^{(1)}(v_\tau).
 \tag{10}
\]

For n=1 the sum is zero. Conditional on A and on all W_{1j}, j>=2,
C_A is a finite fixed complex number and T=W_{11} is still N(0,1/n).
On E_n, set t=T and z(t)=tH+C_A. As t tends to positive infinity,

\[
 -\operatorname{Re}(z(t)^2)
 =(Q^2-P^2)t^2+O_{H,C_A}(t)+O_{C_A}(1).
 \tag{11}
\]

Moreover, the direction -z(t)^2 eventually lies in a fixed cone of the
form used in Section 2. Indeed |Q|>2|P| gives
(Q^2-P^2)/(P^2+Q^2)>3/5, and adding the fixed C_A does not change
this limiting ratio. We may use, for example, kappa=1/2 for all
sufficiently large t depending on H,C_A.

By (7) and the final observation of Section 2 there are finite positive
constants C_1,C_2,C_3 and t_0, allowed to depend on this conditioning,
such that for t>=t_0

\[
 |\phi(tH+C_A)|^2
 \ge C_1t^{-2}
       \exp\{(Q^2-P^2)t^2-C_2t-C_3\}.
 \tag{12}
\]

The Gaussian density of T is sqrt(n/(2pi)) exp(-nt^2/2). Its integral
against (12) is infinite by (9): the coefficient of t^2 in the exponent
is strictly positive. Thus

\[
 \mathbb E[|\phi(U)|^2\mid A,(W_{1j})_{j\ge2}]=\infty
 \quad\hbox{on }E_n.
 \tag{13}
\]

All integrands are nonnegative. Iterated integration is therefore valid
even when the answer is infinite. Integrating first over the remaining
row entries and then over A, whose event E_n has positive probability,
proves E|h_1^(2)(v_tau)|^2=infinity. One nonnegative summand suffices to
prove (3).

On real arguments |phi(x)|<=|a||x|+|c|+|b|. Conditional Gaussian moments
and this linear-growth bound prove inductively that every fixed real
feature moment is finite at every finite n and fixed depth. Thus (3) is
not a real-axis moment pathology.

## 4. Why the finite population calculation remains correct

For activation (4), the initialized limiting Gaussian calculation gives,
when 1<=r<2,

\[
 F(r)=1-\frac{\pi}{2\sqrt3}+\sqrt3\arcsin(r/2),
 \qquad \mathbb E|\phi(U_r)|^2=F(r),
\]

where E U_r^2=1 and E|U_r|^2=r. Along (2) the first input has
r_0=cosh(2tau), and the limiting recursion is r_(ell+1)=F(r_ell).
For small enough fixed nonzero tau, r_0 and r_1 are below 2, so the
limiting second-layer moment is finite. The earlier note proves a
polynomially shrinking tube for each fixed depth.

There is no contradiction with (3). A conditional law of large numbers
at typical lower-layer covariance, or convergence in probability after
stopping outside a compact covariance neighborhood, does not give uniform
integrability of the unstopped complex variables. Equation (13) is a
direct failure of that uniform-integrability inference. In particular,
an unconditional finite-width L2 bound cannot be obtained by inserting
the population complex covariance into each reused layer.

## 5. Exact consequence and limits

This invalidates one possible shortcut toward the proposed new source
theorem: a bounded population complex moment cannot simply be treated as
an unconditional finite-network complex moment. The same problem occurs
for a real-bounded activation and for unbounded linear-plus-erf versions,
so lifting the real B_0 bound is not the source of this obstruction.

A stopped or high-probability estimate can still be true: (3) alone gives
no lower bound on the probability of a large value as n grows. This note
does not disprove a high-probability polynomial-depth source radius, a
root-width comparison, or a small autonomous representation. It also
does not contradict the existing pole-safe finite-network proof, which
uses stopped coordinate budgets and bounded complex domains.

Finally the canonical readout is zero at initialization, so f_n(0,v)=0
even at these complex queries. No claim about prediction error follows
from (3). The remaining task is to prove the trained, stopped response
and source estimates with explicit depth constants, then use them in the
autonomous runtime comparison. None of those estimates is assumed here.

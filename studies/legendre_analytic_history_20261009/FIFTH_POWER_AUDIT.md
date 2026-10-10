# Scoped audit of the fifth-power prediction obstruction

Date: 2026-10-10. Verdict: **PASS**, for the stated fixed identity-activation
problem and sufficiently small fixed nonzero labels. The proof establishes
an actual prediction lower bound \(c q^{-5}\), with constants uniform in
width and order on the common initialization event. The separate dense
upper bound \(O_{\mathbb P}(n^{-1/2})\) also passes. Together they give the
literal order boundary described below, including subpolynomial factors.
This is a bounded mathematical audit, not a promotion review.

The complete frozen inputs were `SHARPER_OBSTRUCTION_ROUTE.md`,
`CROSS_TAIL_IDENTITIES.md`, and `IDENTITY_DENSE_UPPER.md`. Their SHA-256
hashes, in that order, were:

```
578b46258b1f5a1116b62630a0da7434f17bd1976e24a445b324120298b30e8b
3fe71dbd91742165e0bc7009c3ed5d1128ca72d50ddede16cac3ce476580094d
94ccc7e639a376f54dd7dea89d5158a2a7f94efcb29fed06e1e2be1c931152e0
```

The audit also checked the canonical setup and fitting equations in
`paper/compact.tex` and `paper/compact_fitting.tex`, and the projection,
construction, and order-independent fitting arguments in
`paper/compact_legendre.tex`. No other study, author history, prior review,
experiment, archived book, or external source was used. The Legendre
asymptotic was checked through the supplied integral derivation; the
external DLMF citation is not needed for the verdict.

## 1. Exact model and common event

For \(m=d=L=2\), identity activation, and normalized training inputs
\(e_1,e_2\), the mobility coordinates are

\[
A=W^{(1)}/\sqrt n,\qquad B=W^{(2)},\qquad c=w/\sqrt n.
\]

The training prediction vector is \(F=A^\top B^\top c\), the residual is
\(r=F-y\), and \(Y=\|y\|_2/\sqrt2>0\). The dense equations in the candidate
are exactly the canonical equations after this scaling. In particular the
hidden-matrix update has coefficient one. The paper's factor \(1/n\)
multiplies histories with two factors \(\sqrt n\), which cancel.

Each trajectory uses its own clock
\(\xi(t)=1+\int_0^t\rho(s)\,ds\), where \(\rho=\|r\|/\sqrt2\).
Its normalized matrix histories are \(h(\xi)=A(\xi)\) and
\(b(\xi)=c(\xi)[r(\xi)/\rho(\xi)]^\top\), continued as \(A_0\) and zero
on the prefix \([0,1]\). Primes below denote clock derivatives.

Let \(\mathcal G_n\) be the initialization event defined in equation (4)
of `IDENTITY_DENSE_UPPER.md`. Its conditions are the identity-network
specialization of the supplied fitting event; its probability tends to
one. The dense fitting lemma and the Legendre order-independent fitting
claim are deterministic on this same event. Thus no union bound over
orders, and no additional event depending on \(q\), is needed.

A common interval with residual RMS at least \(Y/2\) does follow uniformly
in \(q\). To make the candidate's short explanation explicit, the global
physical bounds give \(\|r(t)\|\le\sqrt2Y\), bounded \(\|A(t)\|_{\rm op}\)
and \(\|B(t)\|_{\rm op}\), and hence \(\|\dot c(t)\|\le CY\).
Because \(c(0)=0\), \(\|F(t)\|\le CYt\). The reverse triangle inequality
then gives \(\rho(t)\ge Y/2\) on a fixed sufficiently short physical
interval, for dense and every closure order. Their clocks therefore
cover a common interval \(1\le T\le T_2\).

The clock field is uniformly Lipschitz in the stated difference norm.
Only \(B\)'s operator norm enters coefficients; the Frobenius norm is
used for its difference and its positive-order derivatives. There is no
hidden \(\sqrt n\) factor.

## 2. Global hinge bounds and interior expansion

The truncated-power integral identity has the positive sign and the
correct denominator. The energy bound and differentiated Legendre
equation yield the derivative bound in the region \(j\sin\theta\ge1\).
The endpoint derivative estimate handles its complement. Consequently
the moment and \(L^2\)-tail bounds are uniform as the join approaches an
endpoint, including \(T-1\asymp q^{-2}\).

For the exceptional ramp/quadratic pairing, the endpoint formulas give
exactly

\[
\langle Q_q^T(\xi-1)_+,Q_q^T(\xi-1)_+^2\rangle
=I_q(T)I_{q-1}(T).
\]

Here \(Q_q^T=I-\Pi_q^T\), where \(\Pi_q^T\) is the \(L^2([0,T])\)
orthogonal projection onto polynomials of degree below \(q\), and
\(I_j(T)=\int_1^T(\xi-1)P_j(2\xi/T-1)\,d\xi\).

This is \(O(q^{-5})\), not just the \(O(q^{-4})\) obtained from the two
tail norms. Its interior expansion has the stated coefficient:

\[
I_qI_{q-1}
=\frac{T(T-1)^{3/2}}{2\pi}q^{-5}
 \left[\frac2T-1+\sin(2q\theta(T))\right]+O(q^{-6}),
\qquad \theta(T)=\arccos(2/T-1).
\]

Subtracting the right Taylor jets through degree four makes the
remainders globally \(C^4\). Applying the self-adjoint Legendre operator
twice is legitimate: its integration-by-parts boundary terms vanish at
the endpoints, and there are no distributional join terms because the
required derivatives match. The resulting \(O(q^{-4})\) remainder tails
are uniform in width and \(T\). In matrix-valued histories the same
argument applies in the Frobenius Hilbert space.

The only jet pairings at order \(q^{-5}\) are the ramp/quadratic pair,
the quadratic/quadratic pair, and the ramp/cubic pair. The last two have
smooth leading terms: their oscillatory coefficient sums are \(O(q^{-6})\)
on a fixed interior interval. The largest remainder pairing is
\(O(q^{-3/2})O(q^{-4})=O(q^{-11/2})\). This verifies the candidate's
expansion

\[
H_q[b_D,h_D](T)
=q^{-5}\{C(T)\sin(2q\theta(T))+D(T)\}+O(q^{-11/2}),
\]

including

\[
C(T)=\frac{T(T-1)^{3/2}}{4\pi}
       b_D'(1+)h_D''(1+)^\top.
\]

The matrix cross-tail used here and below is
\[
H_q[b,h](T)=\int_0^T(Q_q^Tb)(\xi)(Q_q^Th)(\xi)^\top\,d\xi;
\]
the subscript \(D\) denotes the dense histories.

The coefficient functions and their first derivatives are uniformly
bounded on the fixed interior interval. No derivative bound on the
oscillatory remainder is required. A scalar lower bound is a supremum
over a nondegenerate interval, not a pointwise lower bound at every
\(T\); for example the scalar pairing vanishes at \(T=2\).

## 3. Transfer to the order-dependent closure

The reconstructed matrix obeys the exact integral equation

\[
\widehat B(T)=B_0-\int_1^T\widehat b\,\widehat h^\top\,d\xi
                         +H_q[\widehat b,\widehat h](T).
\]

There are no omitted mixed projection terms, because orthogonality
removes them. For the running state-and-time difference \(E(T)\), expand
the difference of the two bilinear cross-tails. Projection contraction,
the dense-tail bounds, and local Lipschitz continuity of \(c(r/\rho)^\top\)
give

\[
\|H_q[\widehat b,\widehat h]-H_q[b_D,h_D]\|_F
\le Cq^{-3/2}E(T)+CE(T)^2.
\]

Both history differences vanish on the prefix; their remaining \(L^2\)
norms are at most \(C\sqrt{T_2-1}E(T)\). Thus the estimate does not assume
any \(q\)-uniform derivatives of the closure histories.

In the resulting Volterra inequality, first restrict \(E\) below a fixed
small bootstrap threshold, and then take \(q\) large enough to absorb
the linear \(q^{-3/2}E\) term. Gronwall gives \(E\le Cq^{-5}\), which
strictly improves that threshold for all sufficiently large \(q\).
Continuity from \(E(1)=0\) closes the argument on the whole interval.
Substitution improves the cross-tail difference to \(O(q^{-13/2})\).

Consequently the candidate's decomposition
\(\Delta B=H_q[b_D,h_D]+S_B+O(q^{-13/2})\) has
\(\|S_B'\|_F=O(q^{-5})\); the derivatives of the other state differences
and of the physical-time difference are also \(O(q^{-5})\). This is
sufficient for the output argument, and does not differentiate the small
remainder.

## 4. Same-time prediction and cancellation

With \(\Delta t=t_{\rm Leg}(T)-t_D(T)\), expansion of the actual dense
prediction at physical time \(t_D(T)+\Delta t\) gives the correction
\(-\dot F_D(t_D(T))\Delta t\), with the sign in the candidate. Its
derivative is \(O(q^{-5})\), and its quadratic error is \(O(q^{-10})\).
The same estimates hold for the terms involving \(\Delta A\),
\(\Delta c\), and \(S_B\). Hence the same-time discrepancy has the
claimed form

\[
g_q(T)=q^{-5}V(T)\sin(2q\theta(T))+R_q(T)+O(q^{-11/2}),
\qquad \|R_q'(T)\|\le Cq^{-5}.
\]

The leading coefficient is an actual output coefficient, not merely a
parameter discrepancy. With

\[
u=B_0A_0y,\qquad G=A_0^\top B_0^\top B_0A_0,
\]

the join derivatives are

\[
b_D'(1+)=-uy^\top/Y^2,
\qquad h_D''(1+)=B_0^\top uy^\top/Y^2.
\]

Thus \(C(T)\) is a negative scalar multiple of \(uu^\top B_0\).
Using \(A_D(t)=A_0+O(t^2)\), \(c_D(t)=ut+O(t^2)\), and
\(G\succeq I_2/2\), the stated expansion of \(V\) has a nonzero leading
term proportional to \(t\|u\|^2Gy\). A fixed sufficiently small interior
clock interval therefore has \(\|V(T)\|\ge v_*>0\), uniformly on the
initialization event.

Adjacent opposite Legendre phases are separated by \(O(q^{-1})\).
Their \(R_q\) values differ by \(O(q^{-6})\), whereas their leading
oscillatory terms differ by \(2q^{-5}V(T_+)+O(q^{-6})\). The remaining
error is \(O(q^{-11/2})\). At least one of the two actual prediction
errors is consequently at least \(cq^{-5}\).

These clock times lie in a deterministic positive physical interval:
on the common interval, \(Y/2\le\rho\le Y\), so

\[
\frac{T-1}{Y}\le t_{\rm Leg}(T)\le\frac{2(T-1)}Y.
\]

This verifies the uniform fixed-interval statement, including the same
physical-time requirement and the possibility of readout cancellation.

## 5. Bounded orders

The candidate's main argument is for \(q\ge q_0\). Its reference to an
earlier onset result was not used as an audit input. The needed bounded
order fact can be checked directly from the frozen construction.

For fixed \(q\), put \(a=T-1\). The normalized histories start as
\(b=b_1a+O(a^2)\), \(h=A_0+h_2a^2/2+O(a^3)\), where \(b_1,h_2\) are
the displayed join derivatives. Since their nonconstant parts are
supported on \([1,1+a]\), their full pairing is
\(b_1h_2^\top a^4/8+O(a^5)\). The projected pairing of those parts is
\(O_q(a^5)\): their moments are respectively \(O(a^2)\) and \(O(a^3)\),
and the finite projection kernel stays bounded for fixed \(q\).
Therefore the leading matrix difference is

\[
\Delta B(T)
=-\frac{\|y\|^2}{8Y^4}uu^\top B_0\,a^4+O_q(a^5).
\]

The ordinary clock equations then give

\[
\Delta c(T)
=-\frac{\|y\|^2\|u\|^2}{40Y^5}u\,a^5+O_q(a^6),
\qquad \Delta A=O_q(a^6),\qquad \Delta t=O_q(a^6).
\]

Indeed the leading readout derivative difference is
\(\Delta B\,A_0y/Y\); the first-layer derivative difference has an
additional factor \(c_D=O(a)\), and the residual difference is
\(O(a^5)\). Passing to the same physical time, \(a=Yt+O(t^2)\), yields

\[
F_{\rm Leg}(t)-F_D(t)
=-\frac{3}{20}\|y\|^2\|u\|^2Gy\,t^5+O_q(t^6).
\]

The coefficient is uniformly nonzero on the good event. For the finite
set \(1\le q<q_0\), the remainder constants can be maximized and one
common sufficiently small positive time chosen. Finite-order local
regularity follows from the finite moment ODE with positive residual;
its derivatives use the same dimension-independent matrix bounds.
Thus bounded orders have a positive uniform discrepancy as well. This
closes the bounded-\(q\) case in the asymptotic consequences below.

## 6. Dense variability upper bound

The entire proof in `IDENTITY_DENSE_UPPER.md` is valid. In particular:

- The Jacobian and Hessian bounds use operator norms for states and
  Euclidean/Frobenius norms for increments, so their constants are
  independent of \(n\). The state tube needed for these bounds is
  convex; no convexity of the initialization good set is assumed.
- The signed gradient-flow comparison retains the negative residual
  square and bounds parameter separation uniformly in time. Combining
  this with \(K\succeq\kappa I_2\), zero initial prediction difference,
  and exponential residual decay gives the integrable velocity
  Lipschitz bound \(Cn^{-1/2}(1+t)e^{-\kappa t}\).
- The good set is nonempty and compact at every \(n\ge2\). The scalar
  McShane extensions agree with actual velocities there and are jointly
  continuous. Gaussian Poincare is applied to the unconditioned full
  Gaussian roots, not to a conditioned law.
- Integrating the expected difference of the extended velocities is
  legitimate by Tonelli. It bounds the whole-time supremum, avoiding
  any time discretization. Identity activation makes the whole-sphere
  query norm exactly the Euclidean norm of the two training outputs.
- The bad initialization probability is added after this estimate.
  Assigning infinite discrepancy to missing trajectories or limits
  does not affect \(O_{\mathbb P}(n^{-1/2})\), because that probability
  tends to zero.

The note proves an upper bound at scale \(n^{-1/2}\). It does not by
itself establish a matching lower bound, and none is needed below.

## 7. Exact consequence at the one-tenth boundary

Define the all-time, whole-sphere errors

\[
E_{n,q}=\|f_{\rm Leg}-f_n\|_{\mathcal X},\qquad
D_n=\|f_n-\widetilde f_n\|_{\mathcal X},
\qquad \mathcal X=\{x:\|x\|=\sqrt2\}.
\]

The previous sections give \(E_{n,q}\ge cq^{-5}\) on an event whose
probability tends to one, with the bounded-order case included after
possibly reducing \(c\), and \(\sqrt nD_n=O_{\mathbb P}(1)\). No
independence between numerator and denominator events is required.

If \(q=q(n)=o(n^{1/10})\), then

\[
\sqrt nE_{n,q}\ge c\left(\frac{n^{1/10}}q\right)^5
\longrightarrow\infty
\]

on the common event. Tightness of \(\sqrt nD_n\) implies
\(E_{n,q}/D_n\to\infty\) in probability, with the paper's convention
that missing limits or zero denominators are failures. Thus no fixed
constant factor comparison can hold with probability tending to one.
This includes orders such as \(n^{1/10}/\log\log n\).

If \(q(n)\le C_0n^{1/10}\), then \(\sqrt nE_{n,q}\ge cC_0^{-5}>0\)
on the common event. For every fixed confidence \(1-\varepsilon\),
tightness supplies an \(M<\infty\) such that eventually

\[
\Pr\left\{\frac{E_{n,q}}{D_n}
       \ge\frac{c}{C_0^5M}\right\}\ge1-\varepsilon-o(1).
\]

Consequently the ratio cannot tend to zero. This does not rule out a
constant factor comparison at \(q\asymp n^{1/10}\). A necessary order
condition for a ratio tending to zero is \(q(n)/n^{1/10}\to\infty\);
the audit proves no sufficiency assertion at or above that boundary.

Finally, attaining the absolute target
\(CY/[\sqrt n(\log(en))^3]\) requires
\(q\ge c_{\rm problem}n^{1/10}(\log(en))^{3/5}\), as stated. All these
conclusions concern this fixed admissible identity-network example;
they are obstructions to a universal guarantee for the unchanged
method, not a claim that every admissible problem has the same lower
bound.

The subsequently supplied `FIFTH_POWER_RESULT.md` was also checked as an
assembly of these conclusions. Its constant-factor versus vanishing-ratio
distinction, subsequence argument, absolute-target logarithm, and necessary
moving-state counts agree with the audited results. The cited separate
upper-route stability lemma was outside this audit's input scope; no
independent verdict on that lemma is included here.

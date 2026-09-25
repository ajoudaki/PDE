# Current-state clocks for the encoded response histories

Status: scoped theoretical derivation; not independently reviewed or promoted.
Author: scoped agent `clock_encoded_history`, 2026-09-25.
Derivation inputs: supervisor's self-contained assignment and follow-up
assumptions only; required rigor/research skills and repository process
instructions. No scientific repository source, other study, external reference,
or experiment was consulted during the derivation. A subsequent explicitly
scoped synthesis check is recorded at the end of this report.
The exact architecture was not supplied, so architecture-specific numerical
constants and degree bounds below are intentionally not instantiated.

## 1. Scope and strongest conclusion

Write the exact finite-dimensional evolution as
\(\dot\theta=V(\theta)\), and put
\[
q_a(\theta)=r_a(\theta)\delta_a(\theta),\qquad
\rho(\theta)=\|r(\theta)\|_2/\sqrt M.
\]
The given middle-layer increment is
\[
\Delta W(t)=-\frac{2}{nM}\sum_{a=1}^M
 \int_0^t q_a(v)h_a(v)^\top\,dv.
\tag{1}
\]
All norms below are Euclidean/operator norms on the stated finite-dimensional
objects. Bounds on individual sample histories are uniform over the finite
sample set.

An algebraic current-state clock can bound derivatives of the actual encoded
histories, including the normalization in the backward history. A useful
choice is
\[
g(\theta)=\sqrt{\rho(\theta)}\,c(\theta).
\tag{2}
\]
On a bounded region, the constant choice \(c=1\) already suffices under the
explicit gradient-flow estimates in Section 3. Under global polynomial
envelopes, Section 4 gives an explicit polynomial \(c\) making the derivatives
of \(h_a\), \(\delta_a\), and \(q_a/g\) at most one in clock time.

This guarantees regularity, not a small normalized-interval approximation
complexity. Constants and clock length may depend strongly on width,
architecture, data, and parameter size. No finite total clock, population
limit, or autonomous truncated-system accuracy follows. The original zero
backward prefix has a jump that no ordinary time change removes. A matching
prefix and an exactly known subtraction repair that representation separately.

## 2. Exact arbitrary-clock reconstruction and moment equations

Let \(g(\theta(t))>0\) on the nonstationary interval under consideration and
define
\[
\tau(t)=\int_0^t g(\theta(v))\,dv,\qquad L(t)=1+\tau(t).
\]
For the active part of the history define
\[
a_a(1+\tau(t))=h_a(t),\qquad
b_a(1+\tau(t))=\frac{q_a(t)}{g(\theta(t))}.
\tag{3}
\]
Use the prescribed length-one prefix \(a_a(s)=h_a(0)\), \(b_a(s)=0\) for
\(0\le s<1\). Since \(ds=g\,dt\), the substitution in (1) gives exactly
\[
\Delta W(t)=-\frac{2}{nM}\sum_a\int_0^{L(t)}
b_a(s)a_a(s)^\top\,ds.
\tag{4}
\]
Changing the clock while retaining \(r_a\delta_a/\rho\) as the encoded backward
history generally invalidates (4). The denominator has to change to \(g\).

For the shifted orthonormal Legendre polynomials
\(\ell_j(x)=\sqrt{2j+1}\,P_j(2x-1)\), let the *raw* moments be
\[
H_{aj}=\int_0^L a_a(s)\ell_j(s/L)\,ds,\qquad
Q_{aj}=\int_0^L b_a(s)\ell_j(s/L)\,ds.
\]
Then
\[
\Delta W(t)=-\frac{2}{nM L}\sum_a\sum_{j\ge0}
 Q_{aj}H_{aj}^\top.
\tag{5}
\]
The identity holds whenever both histories are in \(L^2\), by applying
orthogonal expansion componentwise; the series of outer products is
absolutely summable in Frobenius norm by Cauchy--Schwarz.

Define \(T_{jk}\) by
\[
x\ell'_j(x)=\sum_{k=0}^jT_{jk}\ell_k(x),\qquad
T_{jj}=j,\quad
T_{jk}=\sqrt{(2j+1)(2k+1)}\quad(k<j).
\]
The diagonal follows from leading coefficients. For \(k<j\), integration by
parts gives the endpoint product \(\ell_j(1)\ell_k(1)\); the remaining
integral vanishes because its other factor has degree at most \(k\).
Differentiation of the raw moments now gives
\[
\dot H_{aj}=g h_a\sqrt{2j+1}
 -\frac gL\sum_{k=0}^jT_{jk}H_{ak},
\qquad
\dot Q_{aj}=q_a\sqrt{2j+1}
 -\frac gL\sum_{k=0}^jT_{jk}Q_{ak}.
\tag{6}
\]
Thus the forward source changes from \(\rho h_a\) to \(g h_a\); the backward
source remains \(q_a=r_a\delta_a\); and the transport coefficient changes
from \(\rho/L\) to \(g/L\). For normalized moments \(A=H/L,B=Q/L\), replace
\(T\) in the transport term by \(T+I\), divide the sources by \(L\), and
replace the factor \(1/L\) in (5) by \(L\).

For a differentiable current-state clock, on \(\rho>0\), the actual history
derivatives are
\[
\frac{da_a}{ds}=\frac{Dh_a[V]}g,\qquad
\frac{db_a}{ds}
=\frac{Dq_a[V]}{g^2}-\frac{q_a Dg[V]}{g^3}.
\tag{7}
\]
Monitoring only \(Dh_a[V]\) and \(D\delta_a[V]\) therefore does not establish
a bound on \(db_a/ds\). Defining \(g\) in terms of the right side of (7)
without resolving its occurrence through \(Dg[V]\) is an implicit differential
condition on \(g\), not an explicit algebraic state monitor. A dynamically
evolved extra clock variable could be a different construction, but it must
be identified as extra state. The envelope below avoids this circularity.

## 3. Square-root activity clock on a bounded region

Assume, on the trajectory of interest, that \(\rho\le\rho_0<\infty\) and
\[
\|\dot h_a\|\le A\rho,\quad
\|\dot\delta_a\|\le A_\delta\rho,\quad
\|\delta_a\|\le D,\quad
\|\dot q_a\|\le B\rho,\quad
|\dot\rho|\le C\rho.
\tag{8}
\]
Take \(g=\sqrt\rho\). At every point where \(\rho>0\),
\[
\left\|\frac{da_a}{ds}\right\|\le A\sqrt{\rho_0},\qquad
\left\|\frac{d\delta_a}{ds}\right\|\le A_\delta\sqrt{\rho_0},
\]
and
\[
\frac{db_a}{ds}=\frac{\dot q_a}{\rho}
 -\frac{q_a\dot\rho}{2\rho^2},\qquad
\left\|\frac{db_a}{ds}\right\|
\le B+\frac{\sqrt M DC}{2}.
\tag{9}
\]
Indeed, \(|r_a|\le\sqrt M\rho\), so \(\|q_a\|\le\sqrt M D\rho\).
Substitution into (7) proves (9), with no residual lower bound. Also
\(\|b_a\|\le\sqrt M D\sqrt\rho\), so this encoded history tends to zero
when the residual tends to zero while the stated bounds persist.

These estimates imply Lipschitz continuity on each active clock interval:
integrate the bounded derivatives between any two clock times. If the clock
interval has a finite endpoint, the Lipschitz estimate gives a unique
continuous extension there. Lipschitz functions are absolutely continuous,
as follows directly by bounding the sum of their increments on disjoint
intervals by the derivative bound times the total interval length.

More generally, \(g=\rho^\alpha\), \(0<\alpha\le1/2\), yields
\[
\|d_s b_a\|\le
(B+\alpha\sqrt M DC)\rho^{1-2\alpha}.
\]
The exponent \(1/2\) is the largest universally sufficient power under (8),
among \(0<\alpha<1\): for \(q=\rho=e^{-t}\),
\(d_s(q/g)=-(1-\alpha)\rho^{1-2\alpha}\), which diverges when
\(1/2<\alpha<1\). The special cancellation at \(\alpha=1\) for this scalar
example does not survive multiple residual directions; Section 5 gives a
counterexample.

### Why the hypotheses hold on finite horizons of smooth square-loss GF

For finite smooth squared-loss gradient flow with a fixed bounded positive
semidefinite preconditioner \(P\), write
\[
E(\theta)=\frac{1}{2M}\|r(\theta)\|^2,\qquad
V=-P\nabla E=-\frac1M P\,Dr^\top r.
\]
On a compact parameter region, \(\|V\|\le K\rho\), with bounded derivatives
of \(r,h_a,\delta_a\). Consequently \(\dot h_a\) and \(\dot\delta_a\) are
\(O(\rho)\),
\[
|\dot\rho|\le\|Dr[V]\|/\sqrt M=O(\rho),
\quad
\dot q_a=Dr_a[V]\delta_a+r_aD\delta_a[V]=O(\rho),
\]
where the final bound uses the region's upper bound on \(\rho\).

For this specific GF, compact containment on every finite physical horizon
does not require a bounded loss sublevel set. Along a solution,
\[
-\dot E=\nabla E^\top P\nabla E,\qquad
\|V\|^2\le\|P\|(-\dot E).
\]
Hence
\[
\|\theta(t)-\theta(0)\|
\le\sqrt{t\,\|P\|\,E(\theta(0))}.
\tag{10}
\]
A smooth vector field is bounded and locally Lipschitz on the resulting
closed finite-dimensional ball. If a maximal solution ended at finite time,
the finite-length estimate on its last time interval would make it Cauchy;
its finite limit would admit a local continuation, a contradiction. Thus
finite horizons exist and the bounds above apply there. This argument uses
square-loss GF and fixed \(P\); it is not a claim about an arbitrary smooth
vector field \(V\).

An all-time bounded region would make the constants in (8) uniform in time.
Such a region is a separate assumption; (10) alone grows with the horizon.

## 4. Explicit state envelope with unit derivative bounds

Here is a conditional theorem that does not use the future trajectory or a
future compact-region bound. Put \(R=r/\sqrt M\),
\(S=1+\|\theta\|^2\), and assume known constants \(A\ge1\), integer
\(m\ge1\), such that, at every state,
\[
\rho,\ \|DR\|,\ \|\delta_a\|,\ \|D\delta_a\|,\ \|Dh_a\|
 \le A S^m,\qquad
\|V\|\le\rho A S^m.
\tag{11}
\]
Let
\[
k=3m,\quad c(\theta)=K S^k,\quad g=\sqrt\rho\,c,
\]
where
\[
K\ge A^{5/2},\qquad
K^2\ge\sqrt M A^3(5/2+2k).
\tag{12}
\]
Then, wherever \(\rho>0\),
\[
\|d_s h_a\|\le1,\qquad
\|d_s\delta_a\|\le1,\qquad
\|d_s(q_a/g)\|\le1.
\tag{13}
\]

Proof. The forward and raw-backward estimates are both bounded by
\[
\frac{\sqrt\rho A^2S^{2m}}{KS^k}
\le\frac{A^{5/2}}K S^{5m/2-k}\le1.
\]
The residual and product estimates are
\[
|\dot\rho|\le\rho A^2S^{2m},\qquad
\|q_a\|\le\sqrt M\rho AS^m,
\]
\[
\|\dot q_a\|\le
\sqrt M(\rho A^3S^{3m}+\rho^2A^2S^{2m})
\le2\sqrt M\rho A^3S^{3m}.
\]
Since
\[
\frac{|\dot c|}{c}
=\frac{2k|\langle\theta,V\rangle|}{S}
\le2k\rho AS^{m-1/2},
\]
expanding (7) for \(g=\sqrt\rho c\) gives
\[
\|d_s b_a\|
\le \frac{\|\dot q_a\|}{\rho c^2}
 +\frac{\|q_a\||\dot\rho|}{2\rho^2c^2}
 +\frac{\|q_a\||\dot c|}{\rho c^3}
\le\frac{\sqrt M A^3(5/2+2k)S^{3m}}{K^2S^{2k}}
\le1.
\]
This proves (13).

For a fixed finite feedforward tanh architecture, fixed finite data, and
fixed square-loss GF scalings, the ingredients of (11) have polynomial
growth in the finite parameter vector. Tanh and the finitely many of its
derivatives used here are bounded; finite forward/reverse differentiation
produces finite sums of products of those bounded factors, parameters, and
fixed data. The residual is polynomially bounded if the final readout is
affine; the gradient field has its explicit residual factor. These facts
provide some computable \(A,m\) through architecture-specific bounds. This
argument does not specify their sharp values or make them independent of
width. Other activations or parameter-dependent preconditioners require
their own verification of (11).

The clock is continuous and vanishes exactly at zero residual, but
\(\sqrt\rho=(M^{-1}\sum_a r_a^2)^{1/4}\) is generally not differentiable
at that set. Its composition with a nonstationary GF trajectory is smooth
where \(\rho>0\), which is all that the calculations require. An initial
zero-residual state is a GF equilibrium and can be assigned a frozen clock
and zero backward history. By uniqueness of a smooth autonomous ODE, a
nonconstant solution cannot hit an equilibrium at finite physical time.

## 5. Obstructions and stationary edge cases

**Residual-proportional clocks need not bound encoded derivatives.**
Consider the quadratic GF residual trajectory
\(r_1=e^{-t},r_2=e^{-\lambda t}\), with \(1<\lambda<2\); it is realized by
the diagonal square-loss system with outputs
\((\theta_1,\sqrt\lambda\theta_2)\), after fixing the loss-time scaling.
Take a constant nonzero backward feature for the second coordinate and
\(g=\rho c(\theta)\), where \(c\) is positive and \(C^1\) near the
limiting equilibrium. Then
\[
b_2=q_2/g\asymp e^{-(\lambda-1)t},\qquad
g\asymp e^{-t},\qquad
|d_s b_2|\asymp e^{(2-\lambda)t}\longrightarrow\infty.
\]
The derivative of \(c\) contributes a smaller relative correction, since
\(\dot\theta=O(e^{-t})\). The raw features may be constant in this example;
normalized residual direction alone produces the obstruction. It refutes
uniform derivative control by this clock class, not absolute continuity
in this particular example.

**A globally smooth nonnegative vanishing clock is too restrictive.**
Already for the scalar system \(\dot\theta=-\theta\), \(q=\rho=\theta>0\),
any nonnegative \(C^1\) clock with \(g(0)=0\) has \(g'(0)=0\), hence
\(g(\theta)=o(\theta)\). If it is positive away from zero, \(q/g\) diverges
along the trajectory. Meanwhile its total late clock length is finite,
because eventually \(g(\theta)\le\theta\). A function with bounded clock
derivative cannot diverge over that finite interval. Thus nonsmoothness
at the zero-residual set is a real allowance in (2), not a removable detail.

**Zero speed is not the same as zero integrand.** At a stationary point with
nonzero residual, raw features may stop changing although individual
\(q_a\) remain nonzero. A monitor based only on feature velocities may
vanish, making \(q_a/g\) undefined. The residual clock above stays positive
there. The sample-summed middle update can vanish by cancellation even
though its individual sample contributions do not. Collapsing a zero-clock
interval is safe for the per-sample construction only when its discarded
contributions vanish and its retained histories have consistent endpoint
values. Zero residual in smooth square-loss GF meets this condition.

**Finite clock length is a separate condition.** Even a bounded smooth GF
trajectory converging to zero residual need not satisfy
\(\int_0^\infty\sqrt\rho\,dt<\infty\). For
\(E(\theta)=\theta^4/2\), \(r(\theta)=\theta^2\),
\(\dot\theta=-2\theta^3\), one has
\(\theta(t)=(\theta(0)^{-2}+4t)^{-1/2}\) for positive initial state.
Thus \(\sqrt\rho=\theta\) has divergent time integral. This is a counterexample
within smooth scalar squared-loss dynamics; it is not asserted to instantiate
the supervisor's unspecified particular architecture.

## 6. Prefix regularity and an exact repair

With the original prefix convention,
\[
b_a(1^-)=0,\qquad b_a(1^+)=q_a(0)/g(\theta(0)).
\]
For a finite positive initial clock rate this is a nonzero jump whenever
\(q_a(0)\ne0\). Changing physical time cannot remove that artificial
discontinuity. In particular the full prefixed history is not absolutely
continuous or \(H^1\), even when its active part has the bounds above.

An exact optional change of representation is to initialize the prefix by
\[
a_a(s)=h_a(0),\qquad b_a(s)=b_{a0}:=q_a(0)/g(\theta(0)),\quad 0\le s\le1,
\]
and subtract its known contribution:
\[
\Delta W(t)=-\frac{2}{nM}\left[
\frac1L\sum_a\sum_{j\ge0}Q_{aj}H_{aj}^\top
-\sum_a b_{a0}h_a(0)^\top\right].
\tag{14}
\]
The raw-moment dynamics (6) are unchanged. Their initial conditions become
\(H_{a0}=h_a(0), Q_{a0}=b_{a0}\) and all higher moments zero.
The correction has rank at most \(M\) before any additional rank
degeneracies; it can be retained as the corresponding fixed factors. Both
extended histories are continuous and piecewise Lipschitz with a common
bound, hence globally Lipschitz and \(H^1\) on every finite clock interval.
This changes the bookkeeping, not the physical middle-layer evolution.
If the initial residual is zero, take \(b_{a0}=0\) and the stationary
construction above.

## 7. What the regularity does and does not establish for Legendre memory

For a fixed history \(f\), monotone time change preserves total variation:
ordered partitions correspond under the change of variable, and the
suprema of sums of increments agree. This applies to \(h_a\) and
\(\delta_a\). The encoded \(b_a=q_a/g\) also changes amplitude when the
clock changes, so its variation is not covered by that invariance argument.

Legendre approximation uses \(x=s/L\), and therefore
\[
\frac{d}{dx}f(Lx)=L f'(Lx).
\]
A unit bound in clock time is not a unit bound on the normalized interval.
For the repaired prefix, the elementary Legendre energy estimate is
\[
\|(I-\Pi_p)F\|_{L^2(0,1)}^2
\le\frac{1}{(p+1)(p+2)}
\int_0^1 x(1-x)\|F'(x)\|^2\,dx,
\quad F(x)=f(Lx).
\tag{15}
\]
To verify it, use
\(-[x(1-x)\ell_j']'=j(j+1)\ell_j\), integrate against \(F\),
and apply Bessel's inequality to
\(\ell'_j/\sqrt{j(j+1)}\) in weighted \(L^2\); these derivatives are
orthonormal there by integration by parts. Summing the resulting coefficient
bounds for \(j>p\) proves (15), with the usual complete Legendre expansion.
If \(\|f'\|\le K_f\), its numerator is at most \(L^2K_f^2/6\).
The omitted reconstruction terms in (14) are bounded by
\[
\frac{2L}{nM}\sum_a
\|(I-\Pi_p)A_a\|_2\,
\|(I-\Pi_p)B_a\|_2,
\quad A_a(x)=a_a(Lx),\ B_a(x)=b_a(Lx).
\]
Thus the repaired histories give an explicit fixed-horizon static
approximation bound, but its length dependence must be retained.

For an interval without the artificial prefix, multiplying a clock by a
constant \(c_0>0\) multiplies its length by \(c_0\), leaves the normalized
forward curve unchanged, and divides the normalized backward history by
\(c_0\). The reconstruction length factor compensates exactly. With the
fixed prefix, scaling also changes the prefix's relative position. Neither
observation supplies a free compression improvement.

The principal unresolved question is quantitative: whether a practical
current-state monitor gives small normalized history tails at useful
finite memory, with controlled width dependence and stable propagation
through the closed approximate dynamics. The derivative theorem alone
does not answer that question.

## 8. Scoped check of the supervisor's synthesis

After freezing the derivation above, the supervisor additionally supplied
`RESPONSE_CLOCK_DESIGN.md`, restricted to Sections 1, 4, 5, 6 and the
claim-status paragraph. I read those sections and the following open-obligation
paragraph completely, and no other scientific source. The inspected file's
SHA256 was
`30beb2f34dc8b1d176002800e7ee8920c711964c11bc24e18bd7d5563ceeb99f`.
The initial derivation file's SHA256 before this check record and its provenance
update was
`6af3cbdc1c650f746ff9b7158f0f001b0e9f745eb1e4396e1b6776e1ba3b6ff8`.

Method: direct algebraic comparison with (3), (6), (7), (9), and (14);
checking normalizations, stationary endpoints, the scope of the polynomial
envelope, and the distinction between the exact GF and the truncated
closure's different vector field. Outcome: the inspected history identities,
square-root derivative bounds, prefix correction, and explicit separation
between exact-GF guarantees and unproved closure guarantees are correct.
The unnormalized-Legendre moment convention used in the synthesis gives its
displayed coefficients \((2j+1)\); the orthonormal convention of this report
gives the square-root coefficients in (6), so there is no discrepancy.

Two precision additions were sent to the supervisor: the metric speed using
\(D^{-1/2}\) requires positive definite mobility or an explicit pseudoinverse
convention; and the square-root clock should explicitly state its
nondifferentiability at the residual-zero set and the stationary zero-residual
convention. The finite-horizon compact-containment argument (10) supplies the
justification for the synthesis's finite-horizon statement. No issues were
found in the stated envelope-versus-efficiency distinction. Claims in unread
Sections 2, 3, and 7, including weighted-Gram identities and optimization
claims, were not audited. This is a scoped same-study check, not an isolated
independent review or a promotion verdict.

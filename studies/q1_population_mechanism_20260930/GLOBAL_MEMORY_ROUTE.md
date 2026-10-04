# Global memory route: exact compensation and a quantified obstruction

Frozen independent first result, 2026-09-30. Author: scoped agent
`global_memory_route`. Scientific inputs: the supervisor's initial model prompt
and its clarification that the canonical fixed Gaussian source operator is a
bounded operator on the common generated population spaces, with norm at most
2 and its true adjoint. No book, other study, other route, external source,
experiment, finite-neuron model, or dense trained-state dynamics was used.
Required AGENTS/workflow Part 1 and the research/proof skills were read.

Status: exact identities and conditional global consequences, with the proofs
below. They have been checked algebraically by their author, but not independently
reviewed. **This route does not prove that the canonical trajectory reaches the
fitted endpoint.** It identifies a precise memory obstruction to the natural
global gradient argument and quantifies how large that obstruction must remain
on an indefinitely positive, nonfitting orbit.

## 1. Selected task and exact population model

Take the three samples

\[
u_1=e_1,\qquad u_2=e_2,\qquad u_3=e_3,\qquad y_a=1
\]

in dimension 3. Permutations act transitively, so the assumed unique equivariant
population flow has synchronized predictions. The task is compatible with the
odd architecture and has three distinct, non-antipodal inputs. For example,
choose a source-independent nonzero bounded root feature \(h\), put
\(A=(\operatorname{arctanh}h)(1,1,1)\), and set \(V_a=0\). Then every
training feature is \(h\), every second-layer feature is
\(g=\tanh(Th)\), and the readout \(W=g/\mathbb E g^2\) fits all three
samples. For the canonical source, \(Th\) is Gaussian with positive variance
\(\mathbb E h^2\), so the denominator is positive. This is an architecture
compatibility witness, not a claim that the initialization reaches this state.

Write \(\langle\cdot,\cdot\rangle_j\) for the real \(L^2(\Omega_j)\)
inner products and let \(q=s+2\). In feature time, the actual model is

\[
\begin{split}
H_a&=\tanh(A\cdot u_a),&
B&=T+\frac13\sum_a V_a\otimes K_a,\\
Z_a&=BH_a,&G_a&=\tanh Z_a,\\
D_a&=W(1-G_a^2),&
L_a&=(1-H_a^2)B^*D_a,\\
W'&=\frac13\sum_aG_a,&V_a'&=D_a,\\
A'&=\frac13\sum_a L_au_a,&
K_a'&=\frac{H_a-K_a}{q}.
\end{split}
\]

Here \((v\otimes k)h=v\langle k,h\rangle_1\), \(T\) is the fixed
canonical source with its actual adjoint, and \(A(0)\) is standard Gaussian,
\(W(0)=V_a(0)=0\), \(K_a(0)=H_a(0)\). All identities are on intervals of
the supplied regular population solution on these same source spaces. No fresh
independence is imposed at positive time. Put

\[
f=\frac13\sum_a\langle W,G_a\rangle_2.
\]

By symmetry each individual training prediction equals \(f\). The identities
below, except synchronization and the explicit three-sample counterpath, also
hold with arbitrary sample count and unit input vectors, after replacing 3 by
that count.

## 2. The exact global memory Gram identity

Define \(J_a=qK_a\). The memory equation gives

\[
J_a'=H_a,\qquad
J_a(s)=2H_a(0)+\int_0^sH_a(r)\,dr.
\tag{1}
\]

Let \(C_{ab}=\langle K_a,H_b\rangle_1\) and
\(M_{ab}=\langle J_a,J_b\rangle_1\). Then

\[
M'_{ab}=q(C_{ab}+C_{ba}),
\]

and consequently

\[
\int_0^s q(r)\operatorname{Sym}C(r)\,dr
=\frac12\bigl(M(s)-4C_0\bigr)
\succeq-2C_0,
\qquad (C_0)_{ab}=\langle H_a(0),H_b(0)\rangle_1.
\tag{2}
\]

The Loewner inequality follows because \(M(s)\) is a Gram matrix. In
particular, for any **fixed** coefficient vector \(c\), with
\(H_c=\sum c_aH_a\) and \(K_c=\sum c_aK_a\),

\[
\int_0^s q\langle K_c,H_c\rangle_1\,dr
\ge -2\|H_c(0)\|_1^2.
\tag{3}
\]

Thus uniformly persistent negative alignment of a fixed sample combination,
even at order \(q^{-2}\), is impossible: if
\(\langle K_c,H_c\rangle_1\le-\epsilon q^{-2}\) for all sufficiently
large \(s\), then the left side of (3) tends to minus infinity as
\(-\epsilon\log q\), contradicting (3).

This result is global in time wherever the regular solution exists. It is
not positivity of \(C(s)\), nor positivity of its contraction against a
time-dependent positive matrix.

## 3. Why the memory identity does not imply ascent

This subsection gives a counterexample to a proposed algebraic implication,
**not a counterexample to the canonical training trajectory**.

At the actual canonical initialization for the selected task, the coordinates
of \(A(0)\) are independent standard Gaussians. Therefore

\[
C_0=cI_3,\qquad
c=\mathbb E\tanh^2(N(0,1))>0.
\]

Consider the continuous scalar path

\[
\lambda(s)=
\begin{cases}1-4s,&0\le s\le\tfrac12,\\-1,&s\ge\tfrac12,\end{cases}
\]

and the population features \(H_a(s)=\lambda(s)H_a(0)\). They can be
realized within the tanh architecture by

\[
A_a(s)=\operatorname{arctanh}\!\bigl(\lambda(s)\tanh A_a(0)\bigr),
\qquad |A_a(s)|\le |A_a(0)|.
\]

This preserves the initial population and is a legitimate bounded feature
path. It is not asserted to satisfy the first-layer training equation. Solving
the actual memory equation along it gives

\[
K_a(s)=k(s)H_a(0),\qquad
k(s)=\frac{2+\int_0^s\lambda(r)\,dr}{s+2}.
\]

For \(1/2<s<5/2\), one has \(\lambda=-1\) and
\(k=(5/2-s)/(s+2)>0\). Hence

\[
\operatorname{Sym}C(s)=-ck(s)I_3\prec0.
\tag{4}
\]

Equation (2) still holds identically. For any nonzero positive semidefinite
matrix-valued weight supported inside this interval, its integrated contraction
against \(C\) is strictly negative. Corners of \(\lambda\) may be smoothed
while preserving a closed subinterval with \(\lambda<0<k\).

Therefore neither canonical Gaussian initialization, the key averaging equation,
bounded tanh features, nor the cumulative Gram identity proves nonnegativity of
the instantaneous key-feature Gram matrix or of its contraction against an
adaptive response Gram matrix. A valid fitting proof must use additional
restrictions from the actual coupled \(A,W,V\) equations.

## 4. Exact output compensation

Define two Hilbert–Schmidt operators from \(L^2(\Omega_1)\) to
\(L^2(\Omega_2)\):

\[
Q=\frac13\sum_aD_a\otimes H_a,\qquad
E=B'-Q
=\frac13\sum_a\left[D_a\otimes(K_a-H_a)+V_a\otimes K_a'\right].
\tag{5}
\]

Equivalently,

\[
E=\frac{1}{3q}\sum_a(V_a-qD_a)\otimes(H_a-K_a).
\tag{6}
\]

These are observables of the specified population flow. No operator is trained
by a replacement dense-model evolution.

Differentiating \(f\), the derivative through \(W\) is \(\|W'\|_2^2\).
The derivative through \(H_a\) is

\[
\begin{split}
\frac13\sum_a\langle D_a,BH_a'\rangle_2
&=\frac13\sum_a\langle(1-H_a^2)B^*D_a,u_a\cdot A'\rangle_1\\
&=\|A'\|_{L^2(\Omega_1;\mathbb R^3)}^2.
\end{split}
\]

The remaining derivative is \(\langle Q,B'\rangle_{HS}\). Thus

\[
f'=\|W'\|_2^2+\|A'\|_2^2+\|Q\|_{HS}^2+\langle Q,E\rangle_{HS}.
\tag{7}
\]

Completing a square gives the exact compensated dissipation identity

\[
\left(f+\frac12\int_0^s\|E(r)\|_{HS}^2dr\right)'
=\|W'\|_2^2+\|A'\|_2^2
+\frac12\|Q\|_{HS}^2+\frac12\|Q+E\|_{HS}^2.
\tag{8}
\]

In particular the compensated quantity is nondecreasing. It contains an
accumulated memory defect and is not a finite-state closure or a bounded
Lyapunov function merely because \(f\) is bounded.

For comparison with (2), the contribution to \(f'\) from \(V'\) alone is

\[
\frac19\sum_{a,b}\langle D_a,D_b\rangle_2\langle K_b,H_a\rangle_1.
\]

Its adaptive positive semidefinite matrix is the response Gram matrix
\((\langle D_a,D_b\rangle_2)\). Equation (2) supplies no sign for its
time-dependent contraction, and it also does not cover the \(K'\) contribution.

## 5. A global obstruction: persistent nonfitting requires logarithmic defect

The readout has a second exact identity:

\[
\frac12\|W(s)\|_2^2=\int_0^s f(r)\,dr.
\tag{9}
\]

Indeed \(\langle W,W'\rangle_2=f\) and \(W(0)=0\).

**Proposition.** Suppose a regular feature-time solution exists for every
\(s\ge0\), never reaches \(f=1\), and satisfies
\(f(s)\ge\delta>0\) for \(s\ge S>0\). Then, for every \(T>S\),

\[
\int_0^T\|E(s)\|_{HS}^2ds
\ge \delta\log(T/S)-\delta-2.
\tag{10}
\]

In particular its memory-defect energy cannot be finite or \(o(\log T)\).

*Proof.* Continuity and \(f(0)=0\) imply \(f(T)<1\). From (8),

\[
\int_0^T\|E\|_{HS}^2ds
\ge 2\int_0^T\|W'\|_2^2ds-2f(T)
>2\int_0^T\|W'\|_2^2ds-2.
\tag{11}
\]

The elementary Hilbert-space Hardy identity is

\[
\int_0^T\|W'\|_2^2ds
=\int_0^T\left\|W'-\frac{W}{2s}\right\|_2^2ds
+\frac{\|W(T)\|_2^2}{2T}
+\frac14\int_0^T\frac{\|W(s)\|_2^2}{s^2}ds.
\tag{12}
\]

To verify it, expand the square and integrate
\(\langle W',W\rangle/s=(\|W\|^2)'/(2s)\) by parts on
\([\epsilon,T]\), then let \(\epsilon\downarrow0\). Since
\(\|W'\|_2\le1\), \(\|W(s)\|_2\le s\), so the lower boundary
term and all possible singularities vanish. Equation (9) and the lower bound
on \(f\) imply
\(\|W(s)\|_2^2\ge2\delta(s-S)\) for \(s\ge S\). Therefore (12)
gives

\[
\int_0^T\|W'\|_2^2ds
\ge\frac\delta2\left[\log(T/S)+S/T-1\right]
\ge\frac\delta2[\log(T/S)-1].
\]

Substitution into (11) proves (10). \(\square\)

There is also a precise finite-energy consequence without a positive lower
bound on \(f\): if the solution never fits and
\(\int_0^\infty\|E\|_{HS}^2<\infty\), then

\[
\frac1s\int_0^s f(r)dr\longrightarrow0.
\tag{13}
\]

Indeed (8) and \(f<1\) imply \(W'\in L^2(ds;L^2(\Omega_2))\).
For every fixed \(S\),

\[
\frac{\|W(s)\|_2}{\sqrt s}
\le\frac{\|W(S)\|_2}{\sqrt s}
+\left(\int_S^s\|W'(r)\|_2^2dr\right)^{1/2}.
\]

Take first \(s\to\infty\), then \(S\to\infty\); the right side tends
to zero. Equation (9) yields (13). This rules out convergence to any strictly
positive subfitting plateau under finite defect energy, but allows collapse or
oscillation whose Cesaro mean tends to zero.

The inequalities do not assume a sign for \(\langle Q,E\rangle\), and are
valid for the actual q1 flow. They are stronger than the local assertion of
initial output growth. Their limitation is equally explicit: the supplied
dynamics have not yielded a sufficiently small upper bound for the defect.

## 6. Finite-feature-time bounds and the fitted endpoint

Bounded tanh and the initial conditions give pointwise

\[
|W(s)|\le s,\qquad |V_a(s)|\le s^2/2,\qquad |K_a(s)|\le1.
\tag{14}
\]

The last inequality follows from (1), a convex average of functions bounded
by 1. Hence

\[
\|B(s)\|\le2+s^2/2,\qquad
\|A'(s)\|_2\le s(2+s^2/2),
\qquad
\|A(s)-A(0)\|_2\le s^2+s^4/8.
\tag{15}
\]

Here \(\|A'\|_2\le\frac13\sum\|B^*D_a\|_2\) uses
\(\|u_a\|=1\), \(|1-H_a^2|\le1\), and \(\|D_a\|_2\le s\).
Also \(\|K_a'\|_2\le2/q\). All state components consequently have
strong limits at a finite terminal feature time in these norms (and \(W,V\)
even have \(L^\infty\) limits). This prevents finite-feature-time blowup
of the displayed norms. It **does not prove a global canonical population
construction**: extending the given regular source solution through those
limits still requires a local theorem on the limiting state class. Boundedness
of a general operator on \(L^2\) alone does not supply the missing source
regularity or an infinite-dimensional existence theorem.

**Conditional endpoint statement.** If the regular feature orbit reaches its
first value \(f(s_*)=1\) at a finite \(s_*>0\), then the physical clock

\[
t(s)=\int_0^s\frac{dr}{2(1-f(r))}
\tag{16}
\]

maps \([0,s_*)\) onto \([0,\infty)\). Thus the physical population
solution exists for all physical time and converges in the displayed norms to
the exactly fitting feature-time endpoint.

To prove divergence in (16), note that (7), (14), and (15) bound \(|f'|\)
on the finite interval. If this bound is \(L\), then
\(0<1-f(s)\le L(s_*-s)\) before the first root. The integral in (16)
therefore diverges logarithmically or faster. For every finite physical time,
the corresponding feature time lies below \(s_*\), and norm convergence
follows from the preceding finite-time bounds. This is a reparameterization of
the assumed source flow, not a new existence theorem for that source flow.

At this fitted endpoint the keys are exactly

\[
K_a^*=\frac{2H_a(0)+\int_0^{s_*}H_a(r)dr}{s_*+2},
\tag{17}
\]

and the fitted function is

\[
F_*(x)=\left\langle W_*,\tanh\left[
\left(T+\frac13\sum_aV_a^*\otimes K_a^*\right)
\tanh(A_*\cdot x)\right]\right\rangle_2.
\tag{18}
\]

There is no reason to replace \(K_a^*\) by \(H_a^*\): once the residual
vanishes, the physical memory clock also stops, so fitting supplies no later
equilibration. The explicit coefficient of \(H_a(0)\) in (17) is positive;
this alone is not a noncancellation theorem, since the integral can in principle
cancel some initial components. A sufficient condition for strict lag is
\(\|H_a(r)\|_2\le\|H_a^*\|_2\) throughout the feature interval, with
strict inequality on a set of positive measure (or strict inequality at the
initial atom). Then the triangle inequality in (17) gives
\(\|K_a^*\|_2<\|H_a^*\|_2\), hence \(K_a^*\ne H_a^*\).

## 7. What is settled and what remains open

The fixed canonical source correlations and actual adjoint survive every
calculation. The strongest unconditional identities, conditional only on the
supplied regular solution, are (2), (7)–(9), and the finite-horizon bounds.
The strongest all-time consequence is (10): sustained positive nonfitting
requires at least logarithmically divergent memory-defect energy. The exact
fitted endpoint, if reached at finite feature time, retains the historical key
in (17), with no subsequent memory equilibration.

The false implication exposed here is “keys are averages, so their current
feature Gram is positive and output ascent follows.” The explicit counterpath
defeats that implication even from the selected task's canonical first-layer
initialization. It does not show that the coupled training equations reach
negative-alignment states, that the actual output decreases, or that fitting
fails.

The remaining decisive obligations are: (i) construction/continuation of the
canonical regular source flow for all needed feature times; and (ii) a
reachable-trajectory restriction strong enough either to control the negative
memory work, or to prove fitting by a different mechanism. Merely citing (2),
source norm boundedness, or a hypothetical positive plateau does not discharge
either obligation. Registry recommendation: retain as a complete invariant and
global-obstruction route; the positive fitting claim is blocked on these named
bridges, with no assertion that they are routine.

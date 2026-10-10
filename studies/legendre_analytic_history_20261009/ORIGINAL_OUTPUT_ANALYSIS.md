# An onset prediction lower bound for the unchanged Legendre model

This is a supplementary assessment dated 2026-10-09, continuing
`CLOCK_ANALYSIS.md` in the same study. The scientific inputs remain the
current setup and first Legendre construction in `paper/compact.tex` and
`paper/compact_legendre.tex`, `paper/compact_fitting.tex`, and the public
source statement in `paper/compact_foundations.tex`. No alternative method,
other study, numerical experiment, or paper edit is involved.

The derivative jump of a history does not itself prove prediction error.
Here the actual prediction difference is computed, and its Taylor
remainder is controlled uniformly in width and polynomially in the
Legendre order. The result applies to the unchanged residual clock,
constant prefix, reconstruction, and optimizer.

## Statement

Take \(L=m=d=2\), identity activations in both layers, normalized
training inputs \(v_1=e_1,v_2=e_2\), and any fixed nonzero label vector
\(y\in\mathbb R^2\) satisfying the paper's small-label condition.
Then \(Y=\|y\|_2/\sqrt2>0\) and the population Gram is \(I_2\), so
\(\gamma=1\). These activations and data satisfy the stated hypotheses.

There are fixed constants \(c_*,\eta>0\), depending on this problem but
independent of width \(n\) and integer order \(q\geq1\), such that,
on the initialization/fitting event of the paper, simultaneously for every
finite order,

\[
\max_{a=1,2}
|f_{\rm Leg}(\eta/q^2,x_a)-f_n(\eta/q^2,x_a)|
\geq c_*q^{-10}.                                             \tag{1}
\]

That event has probability tending to one. In particular this is an
actual prediction lower bound at a positive physical time, and hence a
lower bound for the all-time, whole-sphere prediction norm. It is not a
claim about the fitted endpoint.

The constants may be extremely small under the small-label condition.
The statement concerns the fixed-problem asymptotic regime of the paper,
not the accuracy achievable at accessible widths or fixed practical
tolerances.

## Scaled physical equations

For this proof only, use the scaled blocks

\[
A=W^{(1)}/\sqrt n\in\mathbb R^{n\times2},\quad
B=W^{(2)}\in\mathbb R^{n\times n},\quad
c=w/\sqrt n\in\mathbb R^n.
\]

The vector of the two training predictions and its residual are

\[
f=A^\top B^\top c\in\mathbb R^2,\qquad r=f-y.
\]

The exact dense equations, including all mobility factors, become

\[
\dot A=-B^\top cr^\top,\qquad
\dot B=-c(Ar)^\top,\qquad
\dot c=-BAr.                                                  \tag{2}
\]

For the Legendre trajectory the equations for \(A,c\) are the same,
whereas the reconstructed physical matrix satisfies

\[
\dot B=-c(Ar)^\top+\mathcal E,
\qquad
\mathcal E=\rho\,e_b e_h^\top,
\qquad \rho=\|r\|_2/\sqrt2.                                  \tag{3}
\]

In (3), all quantities are evaluated on the Legendre trajectory. The
matrix histories, with sample columns, are

\[
h(\tau(t))=A(t),\qquad
b(\tau(t))=c(t)r(t)^\top/\rho(t),\qquad
\tau(t)=1+\int_0^t\rho(s)\,ds,
\]

and \(h=A_0,b=0\) on the prefix \([0,1]\). Their endpoint errors are
\(e_g(t)=g(\tau(t))-(\Pi_q^{\tau(t)}g)(\tau(t))\). The two factors
of \(\sqrt n\) in the unscaled history errors exactly cancel the
\(1/n\) in the original defect formula, producing (3).

Define the initialized vector and training Gram

\[
u=B_0A_0y,\qquad G=A_0^\top B_0^\top B_0A_0.
\]

On the initialization event,
\(\|A_0\|_{\rm op},\|B_0\|_{\rm op}\leq8\) and
\(G\succeq I_2/2\). The paper's order-independent fitting bounds give,
for both trajectories and every finite order,

\[
\|A(t)\|_{\rm op}\leq9,\quad
\|B(t)\|_{\rm op}\leq9,\quad
\|r(t)\|_2\leq\sqrt2Y,
\]

and a uniform bound on \(\|c(t)\|_2\). Bounds on
\(\|A(t)\|_F\) follow because it has two columns. Every constant
below is uniform over realizations satisfying this event and independent
of \(n,q\). It may depend on the fixed labels and the displayed bounds.

The notation \(O(q^kt^j)\) means a remainder with norm at most
\(Cq^kt^j\) on the stated time interval, in Euclidean norm for vectors
and Frobenius norm for matrices. Operator norms suffice for each full
mixer; no bound on \(\|B_0\|_F\), which grows with width, is used.

## Endpoint errors on a short active interval

For \(0\leq\xi\leq T\), the endpoint projection kernel satisfies

\[
K_q^T(T,\xi)
=\frac1T\sum_{j<q}(2j+1)P_j(2\xi/T-1),\qquad
|K_q^T(T,\xi)|\leq\frac{q^2}{T}.                            \tag{4}
\]

This uses only \(|P_j|\leq1\), already proved in the paper, and
\(\sum_{j<q}(2j+1)=q^2\). In particular, for a history \(g\) that
vanishes on the prefix,

\[
\| (\Pi_q^{\tau(t)}g)(\tau(t))\|
\leq q^2\int_0^t\rho(s)\|g(\tau(s))\|\,ds.                  \tag{5}
\]

There is no inverse clock factor in (5); the integration variable was
changed using \(d\tau=\rho\,dt\), and \(\tau\geq1\).

Equations (2)-(3) and the common physical bounds first give, on any
bounded short interval,

\[
c(t)=O(t),\qquad A(t)-A_0=O(t^2).
\]

The first bound follows by integrating \(\dot c=-BAr\); the second
then follows by integrating \(\dot A=-B^\top cr^\top\). Also
\(\|b(\tau(t))\|_F=\sqrt2\|c(t)\|_2=O(t)\). Applying (5) to
\(b\) and to \(h-A_0\), and using exact reproduction of the constant
\(A_0\), gives

\[
\|e_b(t)\|_F\leq C(t+q^2t^2),\qquad
\|e_h(t)\|_F\leq C(t^2+q^2t^3).
\]

Consequently, on \(0\leq t\leq\min(1,q^{-2})\),

\[
\mathcal E(t)=O(t^3),\qquad B(t)-B_0=O(t^2).                \tag{6}
\]

For the second assertion, the ordinary term in \(\dot B\) is
\(O(t)\), and the defect just bounded is \(O(t^3)\).

Because \(f=A^\top B^\top c=O(t)\), one has
\(r=-y+O(t)\) and \(\rho=Y+O(t)\). Choose a fixed \(t_*>0\),
independent of width and order, small enough that \(\rho\geq Y/2\)
for \(t\leq t_*\), and reduce it below one if needed. On

\[
0\leq t\leq\min(t_*,q^{-2}),                              \tag{7}
\]

the physical equations now give more precise expansions, for either
trajectory,

\[
\begin{aligned}
c(t)&=ut+O(t^2),\\
A(t)&=A_0+\tfrac12B_0^\top u y^\top t^2+O(t^3),\\
b(\tau(t))&=-u y^\top t/Y+O(t^2).
\end{aligned}                                               \tag{8}
\]

For the first line, \(-BAr=u+O(t)\) by (6) and the preceding residual
bound. Substitution into \(-B^\top cr^\top\) gives the second line.
The third line uses \(r/\rho=-y/Y+O(t)\); the denominator is bounded
away from zero on (7). These remainders are independent of order.

Combining (8) with (5) yields the endpoint expansions

\[
e_b(t)=-u y^\top t/Y+O(q^2t^2),\qquad
e_h(t)=\tfrac12B_0^\top u y^\top t^2+O(q^2t^3).
\]

Their product in (3), together with \(\rho=Y+O(t)\), proves

\[
\mathcal E(t)=E_3t^3+O(q^2t^4),\qquad
E_3=-\tfrac12\|y\|_2^2 u u^\top B_0.                       \tag{9}
\]

The product of the two remainders is \(O(q^4t^5)\), which is
\(O(q^2t^4)\) on (7). This is the required polynomial, rather than
uncontrolled order-dependent, remainder estimate for the forcing.

## Comparing the actual physical trajectories

Write \(\Delta A=\widehat A-A_D\), and similarly for \(B,c,f,r\),
where hats denote Legendre and the subscript \(D\) denotes dense
training. Both start at the same state. Let

\[
D(t)=\|\Delta A(t)\|_F+\|\Delta B(t)\|_F+
\|\Delta c(t)\|_2.
\]

The polynomial vector field (2) is Lipschitz with a dimension-independent
constant on these bounded physical states, with the stated difference
norm. This follows by subtracting each matrix product one factor at a
time and using the bounds on \(\|A\|_F,\|B\|_{\rm op},\|c\|_2\).
For example,

\[
\|\Delta f\|_2
\leq C\big[t\|\Delta A\|_F+t\|\Delta B\|_F+
\|\Delta c\|_2\big]                                       \tag{10}
\]

on (7), because both readouts are \(O(t)\). Integrating the
difference equations and (9) gives
\(D(t)\leq C\int_0^tD(s)\,ds+Ct^4\), hence

\[
D(t)=O(t^4).                                                \tag{11}
\]

The absence of a direct defect in the first layer and readout permits
sharper block estimates. The readout equation gives
\(\Delta\dot c=O(D)=O(t^4)\), so \(\Delta c=O(t^5)\).
Equation (10) then gives \(\Delta r=\Delta f=O(t^5)\).
Subtracting the first-layer equations gives

\[
\|\Delta\dot A\|_F
\leq C\big[t\|\Delta B\|_F+\|\Delta c\|_2+
t\|\Delta r\|_2\big]=O(t^5),
\]

and hence \(\Delta A=O(t^6)\). Subtracting the ordinary hidden-matrix
terms gives

\[
\Delta\dot B-\mathcal E
=O\big(\|\Delta c\|_2+t\|\Delta A\|_F+
t\|\Delta r\|_2\big)=O(t^5).
\]

Integration of (9) therefore proves

\[
\Delta B(t)=\tfrac14E_3t^4+O(q^2t^5).                      \tag{12}
\]

In the readout difference use the exact decomposition

\[
\Delta\dot c
=-\Delta B\,\widehat A\widehat r
 -B_D\Delta A\widehat r-B_DA_D\Delta r.
\]

Since \(\widehat A\widehat r=-A_0y+O(t)\), (12) and the preceding
block estimates yield

\[
\Delta\dot c=\tfrac14E_3A_0y\,t^4+O(q^2t^5),\qquad
\Delta c=\tfrac1{20}E_3A_0y\,t^5+O(q^2t^6).                 \tag{13}
\]

Finally the exact output subtraction is

\[
\Delta f
=\Delta A^\top\widehat B^\top\widehat c
 +A_D^\top\Delta B^\top\widehat c
 +A_D^\top B_D^\top\Delta c.
\]

The first term is \(O(t^7)\). Substituting (8), (12), and (13) in
the remaining two terms gives

\[
\Delta f(t)=
\left[\tfrac14A_0^\top E_3^\top u
      +\tfrac1{20}A_0^\top B_0^\top E_3A_0y\right]t^5
+O(q^2t^6).
\]

Here \(\|u\|_2^2=y^\top Gy\),
\(A_0^\top B_0^\top u=Gy\), and
\(E_3A_0y=-\|y\|_2^2\|u\|_2^2u/2\). Consequently

\[
\begin{aligned}
f_{\rm Leg}(t)-f_n(t)
&=-\frac3{20}\|y\|_2^2(y^\top Gy)Gy\,t^5+R_q(t),\\
\|R_q(t)\|_2&\leq Cq^2t^6.
\end{aligned}                                              \tag{14}
\]

on (7). Formula (14) is an estimate for the actual prediction vector,
not a parameter discrepancy used as a proxy. The coefficient is
independent of \(q\); it is nonzero on the initialization event.
Equivalently the first differing Taylor derivative is
\(-18\|y\|_2^2(y^\top Gy)Gy\) at order five.

## Turning the expansion into the lower bound

Since \(G\succeq I_2/2\), the norm of the fifth-order coefficient
in (14) is at least

\[
a_y:=\frac3{80}\|y\|_2^5>0.
\]

Choose
\(\eta=\min\{t_*,1,a_y/(2C)\}>0\). At
\(t_q=\eta/q^2\), (14) gives

\[
\|f_{\rm Leg}(t_q)-f_n(t_q)\|_2
\geq\frac{a_y}{2}\eta^5q^{-10}.
\]

At least one of the two training errors is at least this value divided
by \(\sqrt2\), proving (1). In fact the whole-sphere supremum at this
time equals the Euclidean norm of the two training errors, because both
networks are linear in the normalized input and \(v_1,v_2\) form an
orthonormal basis.

The initialization event tends to probability one by the supplied
initialization theorem. Its fit and physical bounds support every finite
order on the same event. Thus (1) permits arbitrary width-dependent
orders \(q=q(n)\); it is not a statement that first fixes \(q\) and
then lets \(n\) grow.

## What is and is not settled

For the paper's displayed Legendre accuracy target
\(CY/(\sqrt n[\log(en)]^3)\), (1) imposes the necessary bound

\[
q\geq c_{\rm problem}\,
n^{1/20}[\log(en)]^{3/10},
\]

whenever that accuracy holds on the stated high-probability event, with
the target's fixed prefactor absorbed into \(c_{\rm problem}>0\).
Therefore neither a fixed polylogarithmic order nor more generally an
order \(n^{o(1)}\) can preserve that displayed accuracy for the unchanged
model over the full continuous trajectory under all the stated
activation/data assumptions. This lower bound is much weaker than the
current sufficient \(n^{1/4+o(1)}\) order and makes no optimality claim.

The headline's relative error uses the *actual independent dense-run
variability* as denominator. To rule out that relative statement directly,
one also needs an upper bound on that denominator in this example; its
lower bound in the current paper cannot be used for that purpose. For
example, an independently proved all-time whole-sphere bound
\(\|f_n-\widetilde f_n\|=n^{-1/2+o_{\mathbb P}(1)}\) from above
would combine with (1) to rule out \(q=n^{o(1)}\) for the relative
criterion. This supplementary analysis does not assume or prove that
additional dense-variability upper bound.

There is no contradiction with good accuracy at fixed practical
tolerances: (14) has a coefficient of fifth order in the label size, and
the witnessing time shrinks with the order. The lower bound identifies
what the uniform continuous-time and fixed-positive-label asymptotic
quantifiers require.

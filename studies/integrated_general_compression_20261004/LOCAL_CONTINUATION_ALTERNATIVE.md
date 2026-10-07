# Real-node polynomial Picard continuation for source initialization

2026-10-06. Frozen theoretical candidate; not independently checked or promoted.
No experiment, implementation, or Git write was performed.

This construction computes dense source values from initialization in
\(n^2\operatorname{polylog}n\) arithmetic for fixed problem parameters and
polynomial target accuracy. It uses short Chebyshev panels and a bounded number
of real-node Picard iterations. It reconstructs an approximation through the
whole physical source horizon. The user's current clarification permits this
when the arithmetic is sufficiently small; the older blanket exclusion in the
two input route notes is superseded for this assignment.

The proof first obtains an analytic restarted solution from each computed
anchor, then approximates it by real-node polynomial Picard iteration, and
finally controls accumulated error with the existing nonlinear least-squares
defect theorem. Exact trained states are proof objects, never algorithm inputs.

## Scope, provenance, and status

Scientific inputs were POLYNOMIAL_SETUP_ODE_ROUTE.md and
POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md in full; docs/notation.qmd; and relevant
RESULT.md sections: dense model/global-fitting statement, source coefficients
S.2 and domain sections S.6--S.8, source expansion and finite construction,
all-horizon extension, and arithmetic/activation/setup costs. The source event
and defect lemma are imported hypotheses, not independently re-proved here.
No sibling candidate, check report, other study, history, or archived book was
read. Input SHA-256 hashes:

- RESULT.md: c2cbd1bb0e6a39de87181df89be977eaf2e272fda4f1459ac934396d84e1b278.
- POLYNOMIAL_SETUP_ODE_ROUTE.md: 46e9c2b4ed9f118b3812ce8208d26ebbfa9c9f1fb3efc6e68f3854e0be8cf5a6.
- POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md: 2d58da5a418f6d5a8f1bb54ce343b205978770424c0940789b15231e251daf42.
- docs/notation.qmd: 78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023.

Part 1 of RESEARCH_WORKFLOW.md, investigate-conjectures with its contract and
adversarial-audit references, and solve-math-rigorously were read. The required
canonical-notation skill returned an operating-system permission error. The
supervisor authorized fallback to the accessible rigorous-math instructions,
notation contract, and explicit repository notation rules. The unavailable
skill and its neural-network reference were not read.

The supervisor separately warned that direct comparison to the original path
leaves an anchor-error floor. That issue had already been identified locally
and the approximate-anchor restart below was already being developed. No
independent comparison verdict has been received.

This is an author-derived candidate argument conditional on the two imported
source/stability results and their exact-real operation model. It does not
establish bit complexity or make its imported dependencies independently checked.

## 1. Model and parameter estimates

Use the source document's dense model and physical clock:

\[
z^{(1)}=Av,\quad z^{(j)}=W^{(j)}h^{(j-1)},\quad
h^{(j)}=\phi_j(z^{(j)}),\quad f_n=w^Th^{(L)}/n,\quad \|v\|_2=1.
\]

Here \(A=W^{(1)}\), \(w=W^{(L+1)}\), and \(v=x/\sqrt d\)
are its abbreviations for the book notation. Every block trains and \(w(0)=0\).
Put \(\lambda=\gamma/m\), \(Y=\|y\|_2/\sqrt m>0\), and use Euclidean
mobility coordinates

\[
\theta=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n),
\qquad P=(L-1)n^2+n(d+1).
\]

For \(r_a=f_n(v_a)-y_a\), \(\rho=\|r\|_2/\sqrt m\), and
\(\xi_a=\nabla_\theta f_n(v_a)\), the vector field is

\[
F(\theta)=-\frac2m\sum_a r_a\xi_a,\qquad \dot\theta=F(\theta).
\tag{1}
\]

Its complex extension uses algebraic transpose and absolute Euclidean norms.
No positivity of a complex Gram is used.

Let \(a,b,s,t_2\) be the source activation strip width, value-at-zero bound,
and first/second derivative bounds. Set \(S=16Y/\lambda\). With the existing
source coefficient \(H_L^{\rm src}\), define conservative constants

\[
\begin{split}
R_w&=2+SH_L^{\rm src}+2Y/\sqrt\lambda,\\
H&=(1+b+12s)^{L+1},\qquad B=R_w(1+12s)^L,\\
D_z&=\sqrt L(1+H)(1+12s)^L,\\
D_b(M)&=(1+12s)^{L+1}[1+L(sB+t_2MD_z)],\\
G&=H+\sqrt L\,sB(1+H),\\
J(M)&=sD_z+\sqrt L[(1+H)D_b(M)+s^2BD_z],\\
C_{\rm qry}&=8\max\{sD_z,D_b(B)\}.
\end{split}
\tag{2}
\]

The following estimates apply inside operator caps twelve, readout RMS cap
\(R_w\), and the activation half-strip. Feature RMS is at most \(H\);
carrier RMS is at most \(B\). Forward differentiation gives

\[
\max_j\frac{\|Dz^{(j)}e\|_2}{\sqrt n}\le D_z\|e\|_2,\qquad
\max_j\frac{\|Dh^{(j)}e\|_2}{\sqrt n}\le sD_z\|e\|_2.
\tag{3}
\]

The direct first-layer coefficient is one, later direct coefficients are at
most \(H\), propagation costs \(12s\), and the sum of the \(L\) parameter
block norms is at most \(\sqrt L\|e\|_2\). These facts prove (3) by summing
the finite geometric recurrence; (2) dominates that sum.

If the reference endpoint has carrier coordinate maximum at most \(M\),
backward subtraction similarly gives

\[
\max_j\frac{\|k^{(j)}(u)-k^{(j)}(v)\|_2}{\sqrt n},\quad
\max_j\frac{\|\delta^{(j)}(u)-\delta^{(j)}(v)\|_2}{\sqrt n}
\le D_b(M)\|u-v\|_2.
\tag{4}
\]

The top carrier difference is the readout difference. A changed mixer costs
at most \(sB\) times its block norm; a changed gate costs at most
\(t_2MD_z\|u-v\|_2\); backward propagation costs \(12s\).
There are at most \(L\) terms. The extra factor \(1+12s\) in (2)
covers the top derivative gate. This proves (4). For complex endpoints one
first stops a straight segment at its first strip exit, then closes the stop
with (3). Real endpoints have no strip-exit issue.

The exact gradient blocks are

\[
\xi_a=\left(\frac{\delta_a^{(1)}v_a^T}{\sqrt n},
 \left(\frac{\delta_a^{(j)}h_a^{(j-1)T}}n\right)_{j=2}^L,
 \frac{h_a^{(L)}}{\sqrt n}\right).
\]

Equations (3)--(4) and the norm of an outer product give

\[
\|\xi_a\|_2\le G,\qquad
\|\xi_a(u)-\xi_a(v)\|_2\le J(M)\|u-v\|_2.
\tag{5}
\]

Taking directional limits bounds the Hessian at a state with carrier maximum
\(M\) by \(J(M)\), also for the complex extension.

At a passive real query, carrier maximum is at most \(\sqrt nB\).
Since \(D_b\) is affine with nonnegative coefficients,
\(\sqrt nD_b(\sqrt nB)\le nD_b(B)\). Thus every source family,
including its initialized-matrix image, changes by at most

\[
C_{\rm qry}n\|u-v\|_2
\tag{6}
\]

in each coordinate. The image factor eight is the initialized operator cap.
This polynomial loss affects only precision, not the panel count.

## 2. Analytic restart from a computed anchor

Condition on the original source and fitting event. Through
\(T_0=32\lambda^{-1}\log(en)\), the true trajectory has complex time
radius \(r_t\), preactivation imaginary parts at most \(a/4\), operator
caps ten, readout RMS at most \(SH_L^{\rm src}\), complex residual RMS
at most \(2Y\), and complex training carrier maximum

\[
M_0=K_{\rm src}S\sqrt{\log(en)}.
\]

For later times the all-horizon extension supplies a complex parameter ball
around \(\theta(T_0)\), with preactivation imaginary parts at most \(3a/8\).
Its tail and short-continuation bounds give distance from \(\theta(T_0)\)
at most

\[
D_{\rm late}=
\left(\frac{2Y}{\sqrt\lambda}+8r_t\sqrt{\mathcal K}\,Y\right)(en)^{-16}
\tag{7}
\]

at every late real anchor and complex displacement of length at most \(2r_t\).
Here \(\mathcal K\) is the explicit source Gram upper coefficient.
The straight segment is inside the same ball. Apply (4) with reference
\(\theta(T_0)\), then convert RMS to a coordinate bound. A common complex
carrier bound on all required time disks is consequently

\[
M=M_0+\sqrt nD_b(M_0)D_{\rm late}
=O(\sqrt{\log(en)})
\tag{8}
\]

at fixed admissible parameters. This step does not silently replace a late
real carrier bound by a complex bound.

Define

\[
\begin{split}
\mathscr L&=1+2G^2+2(2Y+G)J(M+1),\\
\mathfrak b_n&=\min\left\{\frac14,\frac{a}{32\sqrt nD_z},
 \frac1{4\sqrt nD_b(M)},\frac1{4\mathscr L}\right\},\\
R_t&=\min\{r_t/2,1/(8\mathscr L)\},\qquad Q=1+4YG.
\end{split}
\tag{9}
\]

A ball of radius \(\mathfrak b_n\) around any true complex state remains
inside the half-strip. Stop at a first exit and use (3): preactivation changes
are at most \(a/32\); even \(3a/8+a/32<a/2\). This closes the stop.
Equation (4) gives carrier-coordinate change at most \(1/4\). Operator and
readout caps have the slack included in (2).

Every state in that ball thus has gradient norm at most \(G\), carrier
maximum at most \(M+1\), and residual RMS at most \(2Y+G\). Therefore

\[
DF=-\frac2m\sum_a[\xi_a\xi_a^T+r_aD\xi_a],
\qquad \|DF\|_{\rm op}\le\mathscr L.
\tag{10}
\]

Its width dependence is \(O(\sqrt{\log(en)})\). The small tube radius
affects required accuracy, not the number of dense matrix actions.

Fix a real anchor \(t_0\) and computed vector \(a_0\) with
\(\|a_0-\theta(t_0)\|_2\le\mathfrak b_n/4\). On \(|z|\le R_t\),
consider the analytic error equation

\[
w(z)=a_0-\theta(t_0)+\int_0^z
 [F(\theta(t_0+\zeta)+w(\zeta))-F(\theta(t_0+\zeta))]\,d\zeta.
\tag{11}
\]

On the supremum ball \(\|w\|_\infty\le\mathfrak b_n/2\) of
holomorphic continuous functions, (10) gives contraction factor at most
\(R_t\mathscr L\le1/8\). The image remains strictly inside the ball:
\(\mathfrak b_n/4+\mathfrak b_n/16<\mathfrak b_n/2\).
Iteration converges uniformly. Cauchy's integral formula shows its limit
is holomorphic, and the same contraction proves uniqueness. Hence

\[
v(z)=\theta(t_0+z)+w(z)
\]

is the restarted exact solution, \(v(0)=a_0\), and
\(\|w\|_\infty\le2\|a_0-\theta(t_0)\|_2\).
It is only a proof object. Also

\[
\|F(v(z))\|_2\le4YG+\mathscr L\mathfrak b_n/2<Q.
\tag{12}
\]

This proves the approximate-anchor analytic bridge without assuming a new
stochastic source theorem at a learned initialization.

## 3. Integrated Chebyshev interpolation and real-node Picard iteration

Choose

\[
h_*=\min\{R_t/4,1/(8Q)\},\qquad
N_{\rm pan}=\lceil T/h_*\rceil,\qquad h=T/N_{\rm pan}.
\tag{13}
\]

Then \(3h\mathscr L\le3/32<1/4\), \(Qh\le1/8\), and the
last equal-length panel ends exactly at \(T\).

For degree \(K\), take
\(x_j=\cos((2j+1)\pi/[2(K+1)])\), \(0\le j\le K\), and let
\(I_K\) denote interpolation at those nodes. Discrete cosine identities give

\[
\|I_Kg\|_{\infty,[-1,1]}\le(2K+1)\max_j\|g(x_j)\|_2.
\tag{14}
\]

Its integrated version has a degree-independent bound:

\[
\sup_{x\in[-1,1]}\left\|\int_{-1}^xI_Kg(u)\,du\right\|_2
\le6\max_j\|g(x_j)\|_2.
\tag{15}
\]

For a direct proof put \(b_k(x)=\int_{-1}^xT_k(u)du\).
The integral is \(\sum_jw_jg(x_j)\), where
\(w_j=(K+1)^{-1}[b_0+2\sum_{k=1}^Kb_k\cos(k\theta_j)]\).
Discrete orthogonality and Cauchy--Schwarz imply

\[
\sum_j|w_j|\le\left(b_0^2+2\sum_{k=1}^Kb_k^2\right)^{1/2}.
\]

Now \(|b_0|\le2\), \(|b_1|\le1/2\), and
\(T_{k+1}/[2(k+1)]-T_{k-1}/[2(k-1)]\) gives
\(|b_k|\le2/(k-1)\) for \(k\ge2\).
Since \(\sum_{j\ge1}j^{-2}\le2\), the displayed square is at most
\(4+1/2+16<36\). This proves (15), including vector-valued data.
After scaling to a physical panel,

\[
\left\|\int_0^\cdot I_Kg(s)ds\right\|_\infty
\le3h\max_j\|g(t_j)\|_2.
\tag{16}
\]

The actual local iteration starts at \(U_0(t)=a_0\) and uses

\[
U_{i+1}(t)=a_0+\int_0^t I_K[F(U_i)](s)ds,\qquad 0\le t\le h.
\tag{17}
\]

Only real network evaluations of \(\phi_j,\phi_j'\) at the nodes occur.
There are no higher activation derivatives, activation-jet or complex
activation oracles, or dense nonlinear-system factorizations.
Chebyshev antiderivatives compute the displayed integral.

The Bernstein ellipse of parameter two maps into the restarted disk,
since its physical coordinate has magnitude at most \(9h/8<R_t\).
Equation (12) bounds \(F(v)\) by \(Q\) there. Cauchy's coefficient
formula for the symmetric Laurent representation gives coefficient norms
at most \(2Q2^{-k}\), hence a degree-\(K\) polynomial approximates
\(F(v)\) with error

\[
\zeta_K=2Q2^{-K}.
\tag{18}
\]

For real \(u\) within distance one of \(v(t)\), use the controlled carrier
at \(v(t)\) in (5) and the identity

\[
F(u)-F(v)=-\frac2m\sum_a
 [(f_a(u)-f_a(v))\xi_a(u)
       +r_a(v)(\xi_a(u)-\xi_a(v))].
\]

It yields

\[
\|F(u)-F(v)\|_2\le\mathscr L\|u-v\|_2.
\tag{19}
\]

Real iterates therefore need not lie in the small complex tube; the
restarted solution is the controlled endpoint.

Let \(E_i=\|U_i-v\|_{\infty,[0,h]}\). Subtraction of the two integral
equations, (16), and interpolation exactness on the approximating polynomial
in (18) give

\[
E_{i+1}\le\tfrac14E_i+4h\zeta_K,\qquad E_0\le Qh\le1/8.
\tag{20}
\]

For \(K\ge4\), induction keeps \(E_i<1/4\), validating (19), and gives

\[
E_i\le4^{-i}/8+(16/3)h\zeta_K.
\tag{21}
\]

The final polynomial satisfies \(U_I'=I_KF(U_{I-1})\).
Insert \(F(v)\) on both sides, and use (14), (18), (19), and (21).
For \(\Lambda_K=2K+1\),

\[
\|U_I'-F(U_I)\|_\infty
\le(\Lambda_K+1)\left[\mathscr L\,4^{-(I-1)}/8+2\zeta_K\right].
\tag{22}
\]

For any \(0<\varepsilon_{\rm def}\le1\), take the first integer
\(K\ge4\) satisfying

\[
4Q(2K+2)2^{-K}\le\varepsilon_{\rm def}/2,\qquad
I=2+\left\lceil\log_4\frac{2(2K+2)\mathscr L}
                              {\varepsilon_{\rm def}}\right\rceil.
\tag{23}
\]

These choices make (22) at most \(\varepsilon_{\rm def}\). The search
terminates no later than
\(K=4+\lceil4\log_2[64Q(1+\mathscr L)/\varepsilon_{\rm def}]\rceil\).
Both degree and iteration count are therefore explicitly logarithmic.

## 4. Global error budget and exact source pairing

Let \(A_n,J_0,C_0\) denote the constants \(A_n,J(M_n),C(M_n)\)
of the imported defect lemma in POLYNOMIAL_SETUP_ODE_ROUTE.md, not the
larger constants in (2). That lemma gives
\(\sup_t\|u(t)-\theta(t)\|_2\le2e^{A_n}E_0\) provided

\[
E_0\le e^{-A_n}/4,\qquad
8(C_0+J_0)^2T e^{2A_n}E_0^2\le1.
\tag{24}
\]

Use the original retained joint modes and the explicit quadrature sizes in
POLYNOMIAL_SETUP_QUADRATURE_ROUTE.md. Let \(\delta_{\rm node}\) be its
common nodal tolerance, with its separate dimension-one prescription.
Put \(T_+=\max(1,T)\) and set

\[
\begin{split}
\nu=e^{-A_n}\min\bigg\{&
 \frac18,\frac1{4\sqrt2(C_0+J_0)\sqrt{T_+}},
 \frac{\mathfrak b_n}{16},
 \frac{\delta_{\rm node}}{4C_{\rm qry}n}\bigg\},\\
\varepsilon_{\rm def}&=\min\{1,\nu/T_+\}.
\end{split}
\tag{25}
\]

Execute the fixed \(I,K\) iterations from (23) on each panel; use each
polynomial endpoint as the next anchor. This makes a continuous piecewise
polynomial parameter path initialized exactly at \(\theta(0)\).
Derivative jumps at boundaries do not affect absolute continuity or the
integrated defect.

The bootstrap is sequential and closes: the first anchor is exact.
Every completed prefix has integrated defect at most
\(T\varepsilon_{\rm def}\le\nu\). Apply (24) using the larger total
horizon \(T\) to get

\[
\sup\|u-\theta\|_2\le2e^{A_n}\nu
\le\min\left\{\mathfrak b_n/8,
             \frac{\delta_{\rm node}}{2C_{\rm qry}n}\right\}.
\tag{26}
\]

The next anchor satisfies the hypothesis of (11). Induction constructs all
panels. The second term of (25) makes the quadratic condition in (24) at
most \(1/4\), leaving strict slack.

At every global time/spatial quadrature node, evaluate the network and
backward responses at \(u(t_r)\). Equation (6) gives coordinate error at
most \(\delta_{\rm node}/2\), including each initialized-matrix image.
Form images by applying the actual \(W_0\) or \(W_0^T\) to the computed
base vector, and use the same scalar quadrature on paired members. The
coefficient pairing is then exact in the adopted arithmetic model.
The quadrature note's error allocation, unchanged rank bound, selector, and
Harmonic prediction/storage guarantee apply.

The final space retains precisely the original modes. Picard nodes and panel
endpoints add no generators, so final storage gains no panel-count factor.
All dense temporary arrays are discarded after setup. The zero-label,
baseline-only, and full-width branches keep their original simpler rules.

## 5. Work, memory, and the Euler comparison

Let \(N_t,N_x,p,H_{\rm harm},R_{\rm src},r,q\) denote the quadrature
note's time/spatial counts, temporal cutoff, full harmonic count,
source-generator bound, actual source rank, and selected neuron budget.
The names \(H_{\rm harm},R_{\rm src}\) here distinguish them from (2) and
(9). They are unrelated to the local \(K,I,N_{\rm pan}\).

One Picard iteration uses \(K+1\) dense vector-field evaluations and direct
scalar interpolation/integration transforms, with non-activation work

\[
O(P[mK+K^2])
\]

and \(O(PK+LmnK+K^2)\) words. The scalar integration matrix can be
generated once in \(O(K^3)\) work from the explicit recurrences.
Thus flow reconstruction costs

\[
O(N_{\rm pan}IP[mK+K^2]+K^3)
\tag{27}
\]

plus \(O(N_{\rm pan}ILmnK)\) scalar activation/first-derivative calls.

Order global coefficient-quadrature nodes by physical time. After completing
a panel, evaluate its polynomial at its nodes, costing \(O(PN_tK)\) in
total. All spatial source queries and initialized images then cost
\(O(PN_tN_x)\) arithmetic and \(O(LnN_tN_x)\) activation calls.
Maintain one temporal accumulator per spatial node and retained temporal
degree, using \(O(LnN_x(p+1))\) words. After time streaming, perform
the harmonic projection. The coefficient arithmetic is exactly the bound
\(O(LnN_x(p+1)(N_t+H_{\rm harm}))\) from the quadrature note, with
this explicitly changed accumulation order and storage.

Including source orthogonalization, selection, and final assembly, a complete
sufficient non-activation envelope is

\[
\begin{split}
\mathcal T_{\rm setup}=O\big(&P+K^3
 +N_{\rm pan}IP(mK+K^2)+PN_t(K+N_x)\\
 &+LnN_x(p+1)(N_t+H_{\rm harm})+\mathcal G_{\rm time}\\
 &+LnR_{\rm src}r+Lnr^3+Ln^2r+Lq^2r\big).
\end{split}
\tag{28}
\]

Peak words are bounded by

\[
O\big(PK+LmnK+K^2+LnN_x(p+1)+LnR_{\rm src}+Lq^2
       +m(d+1)+\mathcal G_{\rm memory}\big).
\tag{29}
\]

The geometry costs \(\mathcal G_{\rm time},\mathcal G_{\rm memory}\)
are the explicit ones in the quadrature note. Add sampling work/scratch when
initialization is generated. Add actual scalar activation-evaluation costs:
analyticity alone supplies no computability or bit-cost bound for arbitrary
activation descriptions. The result uses the existing exact-real arithmetic
contract without a high-order activation-jet backend.

Fix admissible \(m,d,L,\gamma,Y>0\), activations, and confidence. For
\(T=O(\log(en))\) and \(\log(1/\eta)=O(\log(en))\),

\[
\mathscr L=O(\sqrt{\log(en)}),\quad
R_t^{-1}=O(\sqrt{\log(en)}),\quad
\log(1/\mathfrak b_n)=O(\log(en)),\quad
A_n=O(\sqrt{\log(en)}).
\]

The quadrature nodal tolerance is polynomially small, so (25) gives
\(\log(1/\varepsilon_{\rm def})=O(\log(en))\). Consequently

\[
N_{\rm pan}=O(\log(en)^{3/2}),\qquad K,I=O(\log(en)).
\tag{30}
\]

Equation (27) becomes \(O(P\log(en)^{9/2})\). With the existing
quadrature counts, every term of (28) is
\(n^2\operatorname{polylog}n=n^{2+o(1)}\) on compressed branches
with polylogarithmic \(q\). The displayed terms proportional to \(n^2\)
have logarithmic power at most \(\max\{9/2,3d/2+1\}\); terms proportional
to \(n\) retain their explicit, possibly larger logarithmic powers in (28).
Memory is also near quadratic, and the dense trajectory is not retained
after setup. None of these asymptotics is uniform in dimension or the other
fixed parameters.

For supplied budgets with faster-growing \(T\) or \(\log(1/\eta)\), the
finite algorithm and displayed formulas still apply, but (30) is not asserted.

The dense benchmark must specify its integration method. Fixed-stage Euler
with physical step \(h_{\rm E}\) costs \(\Theta(PmT/h_{\rm E})\).
The setup/dense ratio is the explicit bracket in (28) divided by that
quantity. For fixed problem parameters, \(T\asymp\log n\), and
\(h_{\rm E}=n^{-1/2}\), this ratio tends to zero because every fixed
logarithmic power is dominated by \(n^{1/2}\). The same statement holds for
any inverse-polynomial Euler step.

This theorem does not force that Euler step. A comparison with unit-step
work \(PmT\), or with an equally accurate high-order dense solver, need
not give a speedup. In particular
\(n^2\operatorname{polylog}n\ll n^2T_0\) does not follow from
\(T_0\asymp\log n\). The construction is an efficient one-time source
initializer and is strictly cheaper than the specified sufficiently fine
Euler baseline. It is not a lower-bound separation from all dense solvers.

## 6. Audit boundary and adaptive panels

The true trajectory is used only to prove correctness. Computation uses
initialized parameters, labels, explicit constants, real activation evaluations,
and arithmetic. Approximate-anchor continuation removes the anchor-error floor;
the small complex tube avoids a \(\sqrt n\) panel-count penalty; the global
signed stability estimate avoids multiplying local amplification through time.
Exact pairing and the original source rank are preserved.

Residual decay alone does not justify exponentially growing explicit Picard
panels: the term \(-2m^{-1}\sum_a\xi_a\xi_a^T\) in \(DF\) persists
as residuals vanish. The fixed radius already proves (30). Fewer panels would
require an implicit or damping-aware treatment of that term and a separate
bounded-solve argument; no adaptive-radius improvement is claimed.

Finite precision, effective stochastic width thresholds, and activation
evaluation algorithms remain outside the inherited arithmetic theorem.
Independent mathematical checking is still required, especially for the
explicit constants, complex restart, and defect bootstrap. There are no
experimental claims.


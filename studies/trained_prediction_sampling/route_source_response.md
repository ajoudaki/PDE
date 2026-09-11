# Source-response route: frozen first-round result

Status: internally checked partial lemmas; no sampling theorem claimed. This
independent route used only `docs/global_nonlinear.md`, complete C.4.6 and C.4.7,
and `docs/NOTATION.md`, together with the required mathematical skills. It has
not read another study or another route's findings. The target is the actual
two-hidden-layer nonlinear law-to-prediction map through physical time 40, for
every fixed bounded-label Borel circle law in a positive smaller W1 ball about
the stated opposite-label reference. Both orientations of the actual A0 are
retained. The desired empirical expansion remains unproved here.

The useful result is that N-cap controls every fixed order of **frozen named
source** derivatives, not just the first derivatives displayed in C.4.7.
Combined with Gaussian expectation differentiation, this removes covariance
rank as an obstacle to finite-program coefficient differentiation. It does
not itself control derivatives of the coefficients with respect to the law.

## 1. All fixed-order named-source derivatives under N-cap

Fix one of C.4.7's finite raw Euler programs in the capped neighborhood, with
mesh bounded by its admitted threshold. All derivatives in this section have
exactly the convention before N1: residuals, contractions, covariance laws,
alpha, beta, F and D are frozen. Source slots are formally distinct, including
duplicated or zero-variance slots. Derivatives refer to the displayed smooth
coordinate expression on the full Euclidean source space, not to a function
defined only almost everywhere on the support of a singular Gaussian law.

Let I be the finite list of source slots in a population. For a vector-valued
coordinate expression V, write

\[
 J_j(V)=\sum_{(p_1,\ldots,p_j)\in I^j}
       |\partial_{p_1}\cdots\partial_{p_j}V|,\qquad j\ge1,
\]

using the Euclidean norm for a vector output. Expressions that do not use a
slot have zero derivatives in that slot. All suprema over the finitely many
times in the following bounds are inside the norm; passive-query suprema
remain outside it.

**Lemma 1.** For every fixed j and finite p there are finite constants,
independent of atom count, minimum positive mass, covariance rank, and mesh
length, such that

\[
 \left\|\max_k J_j(w_k)\right\|_{L^p(\Omega_1)}\le C_{j,p},
 \qquad \sup_{k,u}\|J_j(H^{(1)}_{ku})\|_p\le C_{j,p},
\]
\[
 \sup_{k,u}\{J_j(Z^{(2)}_{ku})+J_j(\Delta^{(2)}_{ku})\}
       +\max_kJ_j(c_k)\le C_j
 \quad\text{pointwise on the upper source space}.
\]

The last supremum is justified by bounds on the deterministic coefficient
rows uniform in u; no bound on the values of a Gaussian process maximum is
being asserted. The same bounds apply to any separately fixed finite order
of source derivatives of a lower or upper hidden feature.

**Proof.** Use the constants C0, R0, D0 and fB from N9–N17. In particular

\[
 \sum_q|D_{ku,q}|\le D_0,
 \qquad |F_{ku,sb}|\le f_Bh_sp_b,
 \qquad |\gamma_{ka}|\le2R_0h_kp_a.
\]

Put

\[
 q_k=\sum_ap_a|Q_{ka}|,\quad J=\sum_kh_kq_k,
 \quad A=2R_0D_0T+4R_0J.
\]

N11 proves E exp(lambda J)<infinity uniformly over the entire family, for
every separately fixed lambda. Independence across times or slots is not
needed.

First consider the lower population. Let S_j(k)=max_{l<=k} J_j(w_l).
The tensor sum of a derivative of a scalar composition is bounded by the
finite partition formula

\[
 J_j(a(V))\le
 \sum_{\pi\in\mathfrak P_j}\|a^{(|\pi|)}\|_\infty
                   \prod_{B\in\pi}J_{|B|}(V),
\]

where partitions are of {1,...,j}. This follows by differentiating j times,
grouping derivatives that hit the same factor, summing over their source
indices, and using that a sum of products factors into products of sums.
For a linear scalar projection w.u its J_j is at most J_j(w), uniformly for
|u|=1. The unique partition with one block contributes the highest derivative
linearly. Hence, with polynomials P_j having fixed nonnegative coefficients,

\[
 J_j(H^{(1)}_{lu})\le S_j(k)+P_j(S_1(k),...,S_{j-1}(k)),\quad l\le k.
\]

Here P1=0. N5 gives, for each current query,

\[
 J_j(Q_{ka})\le\mathbf1_{j=1}
       +D_0\{S_j(k)+P_j(S_1(k),...,S_{j-1}(k))\}.
\]

The direct Gaussian coordinate contributes one only at j=1. Differentiate
the first update in N2. In J_j(phi'(w.u)Q), the two highest derivative
contributions are bounded by D0 S_j and 2|Q|S_j, because |phi'|<=1 and
|phi''|<=2. Every other Leibniz/partition term uses strictly lower derivative
orders and is bounded by a fixed polynomial in their S-values times
1+D0+|Q|. Therefore

\[
 S_j(k+1)\le[1+h_k(2R_0D_0+4R_0q_k)]S_j(k)
       +C_jh_k(1+D_0+q_k)
                  P_j^+(S_1(k),...,S_{j-1}(k)),                 \tag{1}
\]

where P_j^+ has nonnegative coefficients and includes its constant term.
For j=1, the sharper forcing 2R0 h_k is available, so

\[
 S_1(k)\le2R_0T e^A.
\]

Iteration of (1), using product(1+x)<=exp(sum x), gives

\[
 \max_k S_j(k)\le C_j e^A((1+D_0)T+J)
       P_j^+(\max_kS_1(k),...,\max_kS_{j-1}(k)).                \tag{2}
\]

Since all initial source derivatives of g vanish, there is no initial term.
Induction on j and Holder's inequality prove every finite p moment of (2):
all exponential moments of J are available, and the induction hypothesis
supplies every finite moment of each of the finitely many factors in its
polynomial. This proves the lower claims, including the first hidden feature
by the partition formula. It also proves fixed-order derivative bounds for
Q if needed. At order two, the forcing in (1) can explicitly be bounded by
C h_k(1+D0+q_k)(S1+S1^2), which checks that no unweighted sum over injected
source slots was introduced.

For the upper population use N5, c's update, and
Delta=c phi'(Z). Let U_j(k)=max_{l<=k,u}J_j(Z_{lu}), and define analogous
maxima for c and Delta. A current source is its own direct coordinate, so

\[
 J_j(Z_{ku})\le\mathbf1_{j=1}
          +f_B\sum_{s<k}h_s\max_bJ_j(\Delta_{sb}).             \tag{3}
\]

The highest derivative terms of c and Delta give

\[
 J_j(c_k)\le2R_0\sum_{s<k}h_s
                   [\max_bJ_j(Z_{sb})+P_j^{c}],
\]
\[
 J_j(\Delta_{ku})\le J_j(c_k)+2C_0J_j(Z_{ku})+P_j^{\Delta}.
                                                                    \tag{4}
\]

The P-terms are polynomials in strictly lower order upper derivative sums.
They are bounded pointwise by induction. For j=1 they vanish. Inserting
(4) into (3), and bounding the resulting double time sum by T times its
single sum, yields

\[
 U_j(k)\le C_j+
      f_B(2R_0T+2C_0)\sum_{s<k}h_s U_j(s).
\]

Discrete Gronwall gives the uniform pointwise bound, and (4) then bounds
c and Delta. No value of Z, which may be unbounded, appears in these
coefficients: all activation derivatives are bounded. This completes the
induction and the proof. ∎

## 2. Gaussian expectation differentiation does not require full rank

**Lemma 2.** Let C(a) be a C2 curve of positive semidefinite d-by-d matrices
on a real interval, including one-sided endpoints, and let G(a,x) be C2 in a
and C4 in x, with the indicated mixed derivatives continuous and of at most
polynomial growth locally uniformly in a. For X_a~N(0,C(a)), set
g(a)=E G(a,X_a). Then

\[
 g'=E G_a+\frac12\sum_{ij} C'_{ij}E G_{ij},                  \tag{5}
\]
\[
 g''=E G_{aa}+\sum_{ij} C'_{ij}E G_{aij}
        +\frac12\sum_{ij}C''_{ij}E G_{ij}
        +\frac14\sum_{ij,kl}C'_{ij}C'_{kl}E G_{ijkl}.         \tag{6}
\]

No lower positive eigenvalue is required. For example, the covariance part
of (5) is bounded by

\[
 \tfrac12\|C'\|_{\max}\ E\sum_{ij}|G_{ij}|,
\]

so Lemma 1 provides bounds independent of the number of slots when these
formulas are applied to the appropriate named derivative expression.

**Proof.** Replace C by C+tau I. Its Gaussian density has parameter
derivative (1/2)sum C'ij times its mixed second x derivative; differentiating
the explicit nonsingular Gaussian density verifies this identity. Twice
integration by parts transfers those derivatives to G. Polynomial growth
and Gaussian density decay remove the boundary terms, proving (5) at
tau>0. Apply (5) again to obtain (6), including the two identical mixed
terms that add to its coefficient one.

On each compact a-interval, C is uniformly bounded. Gaussian moments of
every fixed order are then uniformly bounded, also for 0<tau<=1. The
expectations on the right sides of (5)–(6) converge uniformly as tau tends
to zero: couple X_a^tau=X_a+sqrt(tau)Z, with an independent standard Z,
truncate to a fixed compact x-ball, use uniform continuity on that ball,
and use a higher Gaussian moment for its complement. The same argument
applies to all displayed derivatives and to g itself. Integrate the
tau-identities over an a-interval and pass to the uniform limits. The
fundamental theorem of calculus proves (5) and (6) at tau=0, including
one-sided endpoints. The argument never differentiates a square root. ∎

In applying this lemma to alpha=E partial_zeta H or beta=E partial_xi Delta,
the first covariance derivative uses third named derivatives of H or Delta;
the second uses fifth named derivatives. Lemma 1 supplies these. Repeated
source slots are included in the tensor sums, so duplicated queries and
variance-zero slots cause no omitted diagonal terms.

The polynomial-growth hypothesis is valid for each frozen finite graph:
Q is Gaussian plus a finite bounded sum, the tanh derivatives are bounded,
and finite differentiation of the lower updates produces finite polynomial
Gaussian envelopes. The moment bounds of Lemma 1, rather than those
graph-dependent polynomial constants, provide the uniform estimates above.

## 3. Exact point where full law response still needs work

For a fixed finite graph a parameter changing the law also changes the
coordinate expression G, not only its Gaussian covariance. Write a dot for
that actual parameter derivative. Differentiating N5 would give

\[
 \dot Z_i=\dot\xi_i+\sum_{q<i}
          (\dot F_{iq}\Delta_q+F_{iq}\dot\Delta_q),
\]
\[
 \dot Q_i=\dot\zeta_i+\sum_{q\le i}
          (\dot D_{iq}H_q+D_{iq}\dot H_q),                    \tag{7}
\]

with, in addition to differentiating the actual residuals,

\[
 \dot F_{iq}=\dot\alpha_{iq}+\dot\gamma_qE[H_iH_q]
         +\gamma_qE[\dot H_iH_q+H_i\dot H_q],
\]
\[
 \dot D_{iq}=\dot\beta_{iq}+
  \mathbf1_{q<i}\{\dot\gamma_qE[\Delta_i\Delta_q]
      +\gamma_qE[\dot\Delta_i\Delta_q+\Delta_i\dot\Delta_q]\}.
                                                                    \tag{8}
\]

The covariance derivatives are exactly the corresponding differentiated
contractions. Neither dot alpha nor dot beta is one of N7–N8's frozen
source derivatives. Formula (5) splits each of them into a covariance term
and the expectation of the coefficient/residual derivative of its named
coordinate expression. Lemma 1 bounds the covariance term once the
differentiated contractions are bounded. It does not bound the other term.

This missing estimate is concrete: one must differentiate the lower and
upper source recursions with respect to the changing residual and coefficient
arrays, retain the time/atom masses, and prove a closed causal estimate for
the resulting mixed derivatives and differentiated covariance contractions.
It must be uniform as the graph is refined, and twice differentiation must
retain products of the two law-direction masses. A bare beta row cap or a
fixed-graph smoothness assertion supplies neither conclusion.

The chronological order avoids an algebraic current-node loop: the current
lower feature precedes its forward source, the current upper backward field
precedes its reverse source, and the raw update is last. However this
ordering is not a proved uniform estimate for the differentiated recursion.
For example, replacing an old coefficient bound by an unweighted sum of
individual derivative bounds would lose the atom-mass density that N17 and
N27a explicitly needed even for ordinary law continuity.

At the continuous raw level, a proposed first law variation (v,B,d) has

\[
 \eta H^1(u)=\phi'(w.u)(v.u),\quad
 \eta Z^2(u)=BH^1(u)+A\eta H^1(u),
\]
\[
 \eta\Delta^2(u)=d\phi'(Z^2(u))+
                   c\phi''(Z^2(u))\eta Z^2(u),\quad
 \eta Q(u)=B^*\Delta^2(u)+A^*\eta\Delta^2(u).
\]

The raw first-block linearization includes

\[
 -2\int r\,\phi''(w.u)Q(u)(v.u)u\,d\mu.                 \tag{9}
\]

For a general law, the reference's own-axis gate cancellation does not
remove (9). Named-query moments do not make multiplication by Q bounded on
arbitrary L2 directions. A source proof must show that the *reached* law
variations have the additional integrability needed for (9) and, at second
order, products such as Q(v.u)(\widetilde v.u) and
c\,eta Z2\,widetilde eta Z2. Lemmas 1–2 are a possible mechanism for doing
so through (7)–(8); assuming A0 is bounded on Lp would replace the actual
model's given hypotheses and is not used here.

## 4. What this first round establishes

The named-source jet bound and the inverse-free Gaussian formulas are
proved above. Thus a loss of covariance rank is not in itself a reason to
abandon coefficient differentiation. The remaining major gap is the
uniform first/second **full law** derivative estimate for the causal
coefficient/covariance recursion, followed by passage to the actual reached
flow. Neither an actual influence function about every nearby law nor an
o_p(m^(-1/2)) empirical remainder has been established by this route.

Registry recommendation: promising, incomplete. Reopen on the explicit
mixed coefficient/residual derivative estimates in Section 3, using the
source jets and Gaussian formulas already proved here. This is not a
counterexample to the desired sampling expansion, nor a no-go result for
the source route. No numerical experiment, external theorem, promotion,
or repository commit was performed.

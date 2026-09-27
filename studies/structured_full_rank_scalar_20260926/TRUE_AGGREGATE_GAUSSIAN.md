# Gaussian block structure and a true aggregate closure

2026-09-27. Bounded independent theory route. No training or numerical experiment.

## Scope and conclusion

The target is exactly the Gaussian-block memory system in sections 1–2 of
`AGGREGATE_SCALAR_CONSTRUCTION.md`, with arbitrary fixed memory order H. The
admissible surrogate has finitely many expected scalar statistics, evolves
autonomously, and restarts from those statistics alone. Representative blocks,
particles, density grids, full-joint-law basis expansions, and fields indexed
by initial random labels do not count as a solution. The desired conclusion
would be a useful approximation bound on every prescribed finite horizon,
preferably with polynomial dependence of scalar count on accuracy.

**Conclusion:** Gaussian initialization provides exact response identities, but
does not by itself supply the requested closure. An explicit calculation below
shows that the reused transpose generates an order-one response and creates a
nonzero fourth cumulant of first-layer preactivations at the first nontrivial
training order. Both effects persist as k increases. Therefore a Wick closure
of the current local state, or a rule that discards its higher cumulants on the
sole ground that G has entry variance 1/k, is invalid. This does not rule out
a hierarchy of aggregate response words with a separately proved tail bound.
That hierarchy is formulated here; its decisive tail estimate remains open.

The scientific inputs used are the stipulated model and the complete first two
Gaussian-conditioning sections of `docs/02-gaussian-reuse.qmd`. The original
derivations below are self-contained. The all-input strengthening in section 2
was subsequently supplied by the lead agent and independently checked here.
No other study was used.

## 1. A finite-k exact response already has order one

Use the allowed special case m=1, label y nonzero, and input u with
0<s=|u|<=1. This case is a falsifier for Gaussian closure, not a replacement
for the general construction problem. At initialization write

\[
a_j=w_j(0)u,\qquad h_j=\tanh a_j,\qquad q=Gh,
\qquad Q=k^{-1}\sum_jh_j^2,
\]

so the a_j are independent N(0,s^2). Write
\(\psi(x)=\tanh(x)\operatorname{sech}^2(x)\). Since c(0)=A(0)=0,

\[
c_i'(0)=2y\tanh(q_i),\qquad w_j'(0)=0,
\]

and direct differentiation of the original equations gives

\[
w_j''(0)=4y^2\operatorname{sech}^2(a_j)u
                 \sum_{i=1}^kG_{ij}\psi(q_i).
\tag{1}
\]

The memory correction has zero contribution to this derivative: V contains
A times delta_2, both initially zero. This argument applies to every H.

Conditional on w(0), each q_i is Gaussian with variance Q. Integration by
parts in G_ij, whose variance is 1/k, gives

\[
\mathbb E[G_{ij}\psi(q_i)\mid w(0)]
 =\frac{h_j}{k}\mathbb E[\psi'(\sqrt Q Z)],\qquad Z\sim N(0,1).
\]

Consequently, defining \(\chi(Q)=\mathbb E\psi'(\sqrt QZ)\),

\[
\mathbb E[w_j''(0)\mid w(0)]
 =4y^2\operatorname{sech}^2(a_j)u\,h_j\chi(Q).
\tag{2}
\]

For Q>0 another one-dimensional integration by parts yields

\[
\chi(Q)=Q^{-1}\mathbb E[\sqrt QZ\,
                    \tanh(\sqrt QZ)\operatorname{sech}^2(\sqrt QZ)]>0.
\]

The integrand is positive except at zero, and chi(0)=1. The k terms in the
transpose contraction cancel the 1/k from integration by parts. Thus (2)
is an order-one term, not an order-1/k correction. Replacing this transpose
by an independent fresh Gaussian matrix makes its conditional mean zero
and deletes this feature-learning term.

There is also order-one conditional fluctuation. For Q>0 let
\(P_h=I-hh^T/(kQ)\). Gaussian row conditioning gives exactly

\[
G\mid(h,q)\ \overset d=\ \frac{qh^T}{kQ}+\widetilde G P_h,
\]

where the entries of the independent matrix tilde G are N(0,1/k). Hence

\[
G^T\psi(q)\mid(h,q)\ \overset d=
h\frac{q^T\psi(q)}{kQ}
 +\left(\frac{\|\psi(q)\|_2^2}{k}\right)^{1/2}P_h\gamma,
\tag{3}
\]

with independent standard Gaussian gamma. Conditional laws of large numbers
in the independent rows explain the persistent response and fluctuation at
large k. Formula (3) is an initial-call identity, not a claim that subsequent
adaptive calls have independent innovations.

## 2. A local fourth cumulant survives large block size

Let a_j(t)=w_j(t)u. Its mean is zero at every time for which the characteristic
solution exists. Indeed, changing the sign of initial w_j and column j of G,
and changing the signs of the corresponding first-population rows of w and B,
preserves the initialization law and the equations; the second-population
quantities are unchanged. Thus this symmetry reverses a_j(t).

Set

\[
\kappa_4(t)=\mathbb E[a_j(t)^4]
                  -3\mathbb E[a_j(t)^2]^2.
\]

At time zero, kappa_4=kappa_4'=0. Because a_j'(0)=0, differentiation twice gives

\[
\kappa_4''(0)=4\mathbb E[(a_j^3-3s^2a_j)a_j''(0)]
 =16y^2s^2\mathbb E[(a_j^3-3s^2a_j)\psi(a_j)\chi(Q)].
\tag{4}
\]

All these finite derivatives have integrable bounds: tanh and its fixed-order
derivatives are bounded, and each time-zero derivative contains only a finite
polynomial in Gaussian entries. Near time zero the residual is nonzero, so
rho=|r| introduces no differentiability issue.

For small positive s, Taylor's formula with bounded derivatives gives

\[
\psi(a)=a-\frac43a^3+O(a^5),\qquad
\chi(Q)=1-4Q+O(Q^2),\qquad
Q=\frac1k\sum_\ell a_\ell^2
          +O\!\left(\frac1k\sum_\ell a_\ell^4\right).
\]

The remainder bounds can be chosen globally with polynomial right-hand sides;
Gaussian moment bounds therefore justify the expectation expansion. Put
\(H_3=a_j^3-3s^2a_j\). The Gaussian moments are

\[
\mathbb E[H_3a_j]=0,\qquad
\mathbb E[H_3a_j^3]=6s^6,
\]

and independence gives

\[
\mathbb E\left[H_3a_j\frac1k\sum_\ell a_\ell^2\right]
 =\frac{6s^6}{k}.
\]

Inserting these three identities in (4) proves

\[
\kappa_4''(0)=-128y^2s^8\left(1+\frac3k\right)+O(y^2s^{10}).
\tag{5}
\]

The O(s^10) constant can be chosen independently of k>=1. To see this, write
a_l=s X_l. Every remainder is bounded by a fixed sum of products of fixed
powers of X_j and averages of fixed powers of the X_l. Holder's inequality
and Jensen's inequality bound their expectations uniformly in k.

In particular, choose s>0 sufficiently small, independently of k. Then
kappa_4''(0)<0 for every k, with a negative bound of order y^2s^8 that does not
vanish as k tends to infinity. At each fixed k,
\(\kappa_4(t)=\tfrac12\kappa_4''(0)t^2+o(t^2)\).
No uniform-in-k positive-time remainder is claimed. The uniform nonzero
initial coefficient already disproves the assertion that every local
non-Gaussian cumulant carries a vanishing power of 1/k.

This result concerns the local first-layer preactivation, not merely the
trivial observation that tanh of a Gaussian is non-Gaussian. A large-k theory
may still use Gaussian driving fields together with nonlinear local states
and response memory. It cannot replace those local states by Gaussian
variables justified solely by block size.

### Strict negativity for every nonzero input, including the unit circle

The small-s restriction can be removed. Define the positive even function
\(g(a)=\psi(a)/a\), with g(0)=1. For a>0,

\[
g(a)=\frac{\tanh a}{a}\operatorname{sech}^2a
\]

is strictly decreasing. Both factors decrease: for the first, the derivative
has numerator \(a\operatorname{sech}^2a-\tanh a<0\), since
\(\tanh a-a\operatorname{sech}^2a\) vanishes at zero and has positive derivative
\(2a\operatorname{sech}^2a\tanh a\). Gaussian integration by parts also gives

\[
\chi(Q)=\mathbb E[Z^2g(\sqrt QZ)].
\]

Thus chi is positive and decreasing in Q, including Q=0 by continuity.
Because each h_l^2<=1, Q<=1 and chi(Q)>=chi(1)>0.

Let mu_s be N(0,s^2) and define the probability measure
\(d\nu_s(a)=a^2d\mu_s(a)/s^2\). Under nu_s, X=a^2 has expectation 3s^2.
Condition on the other a_l and put \(S=\sum_{l\ne j}\tanh^2a_l\). Then

\[
\begin{aligned}
&\mathbb E_{\mu_s}[(a^3-3s^2a)\psi(a)
          \chi((\tanh^2a+S)/k)]\\
&\qquad=s^2\operatorname{Cov}_{\nu_s}
 \left(X,g(\sqrt X)\chi((\tanh^2\sqrt X+S)/k)\right).
\end{aligned}
\]

For x>x', let f(x)=g(sqrt(x)) and h(x)=chi((tanh^2(sqrt(x))+S)/k).
Both are decreasing, f is strictly decreasing, and h>=chi(1). Hence

\[
f(x)h(x)-f(x')h(x')
 =h(x)(f(x)-f(x'))+f(x')(h(x)-h(x'))
 \le\chi(1)(f(x)-f(x')).
\]

The covariance identity
\(\operatorname{Cov}(X,F(X))=\tfrac12\mathbb E[(X-X')(F(X)-F(X'))]\),
where X' is an independent copy, proves

\[
\kappa_4''(0)
 \le16y^2s^4\chi(1)
       \operatorname{Cov}_{\nu_s}(X,g(\sqrt X))<0.
\tag{5a}
\]

The strict inequality follows because X is nondegenerate for every s>0 and
g(sqrt(X)) is strictly decreasing. The bound is independent of k. Thus the
initial non-Gaussian coefficient persists for every input norm 0<s<=1,
including the actual unit-circle case s=1. As before, (5a) is a bound on the
initial coefficient; it does not assert a uniform-in-k positive-time Taylor
remainder.

## 3. What Gaussianity does and does not simplify at initialization

Even before training, the unconditional q_i is a Gaussian variance mixture.
Conditional on w(0) it is N(0,Q), so

\[
\operatorname{cum}_4(q_i)
 =3\operatorname{Var}(Q)
 =\frac3k\operatorname{Var}(\tanh^2(sZ)).
\tag{6}
\]

For example the initial output derivative is exactly

\[
f'(0)=2y\,\mathbb E\big[\tanh^2(\sqrt QZ)\big].
\]

The conditional Gaussian integral is low dimensional, and the moments of Q
are computable from independent scalar Gaussian integrals. This is a useful
initialization simplification. It is not a propagation argument: training
correlates w with G, and (2) and (5) identify the first terms that such a
propagation argument must retain.

## 4. Exact integration by parts requires response statistics

Write x for the dynamic coordinates (w,c,A,B) of a tagged block, and let
alpha(t) collect the deterministic population aggregates and clock that enter
its drift. At a fixed population solution,

\[
\dot x=b(G,x;\alpha(t)).
\]

When differentiating with respect to the seed of the tagged block, alpha(t)
is held fixed: it is a deterministic function shared by the whole law, not a
random function of that one Gaussian draw. With e=(i,j) define
\(R_e=\partial_{G_{ij}}x\). Since the original dynamic initialization is
independent of G, R_e(0)=0, and

\[
\dot R_e=(D_xb)R_e+\partial_{G_{ij}}b.
\tag{7}
\]

For a smooth test F(G,x), Gaussian integration by parts gives the following
identity whenever its two sides are integrable and the Gaussian boundary
term vanishes (polynomial growth of the composed test and its seed derivative
is sufficient):

\[
\mathbb E[G_{ij}F(G,x_t)]
 =\frac1k\mathbb E[
       \partial_{G_{ij}}F(G,x_t)+D_xF(G,x_t)R_e(t)].
\tag{8}
\]

The second term cannot be discarded after adaptive reuse. Evolving its
expected products introduces more response correlations. Applying Gaussian
integration by parts to those products introduces second seed derivatives,
whose exact equation is

\[
\begin{aligned}
\dot R_{ef}={}&(D_xb)R_{ef}+D_x^2b[R_e,R_f]\\
 &+(D_x\partial_e b)R_f+(D_x\partial_f b)R_e
                    +\partial_e\partial_f b.
\end{aligned}
\tag{9}
\]

Higher derivatives repeat this pattern. Neither the nonlinear derivatives
nor the required products stop at a fixed order. One can instead retain
expected words containing explicit G entries, avoiding seed responses, but
their derivatives produce longer words. This is an exact hierarchy either
way; (7)–(9) do not prove that every possible finite aggregate representation
fails. This route has not established response integrability uniformly on
arbitrary prescribed finite horizons; it must be part of any such theorem.

Finite adaptive Gaussian conditioning provides another exact description.
It retains the joint forward and transpose transcript and its Gram/response
matrices. Each new independent query can enlarge that transcript. At fixed
k its rank is at most k per orientation, but then the complete random block
information has effectively been recovered; averaging that random information
still needs a closure. Replacing random Grams by their expectations before
inversion is not an exact identity. Thus bounded transcript rank alone is
not an expected-statistics ODE.

## 5. An exact aggregate-word hierarchy without approximating tanh

There is a constructive algebraic starting point for a fixed finite panel of
inputs, including the training inputs. This is only a hierarchy skeleton,
not a solution for arbitrary unseen u.

Let H_a=tanh(wu_a), J_a=tanh(z_2(u_a)), and lambda=1/L. Then

\[
\dot H_a=(1-H_a^2)\odot(\dot w u_a),\qquad
\dot J_a=(1-J_a^2)\odot\dot z_{2,a},\qquad
\dot\lambda=-\rho\lambda^2.
\tag{10}
\]

Products and squares of vector entries are coordinatewise. The first equation
contains only H, J, c, A, B, G, dataset inner products and the current scalar
aggregates, because w' is given by the original backward equation. For each
memory index j,

\[
S_{j,a}=\mathbb E[k^{-1}B_j^TH_a],\qquad
\dot S_{j,a}=\mathbb E[k^{-1}(\dot B_j^TH_a+B_j^T\dot H_a)],
\tag{11}
\]

and

\[
\dot z_{2,a}=G\dot H_a
-\frac2m\sum_{j<H}(2j+1)
 [\dot\lambda A_jS_{j,a}
  +\lambda\dot A_jS_{j,a}+\lambda A_j\dot S_{j,a}].
\tag{12}
\]

Equations (10)–(12), the original equations for c,A,B, and the original
definitions of f,S,V give a finite-degree polynomial local drift with
coefficients depending on finitely many expected local polynomial words and
the scalar rho. Rho is still computed from the residual vector by its norm;
no differentiation or division by rho is needed. The constraints H=tanh(wu)
and J=tanh(z_2) are preserved because (10) is their exact chain rule.

For every local polynomial word P, its expected value obeys the exact equation

\[
\frac{d}{dt}\mathbb E[P]
       =\mathbb E[\nabla P\cdot b_{\rm lifted}].
\tag{13}
\]

After expanding the finite index contractions, the right side is a finite
combination of other expected words and products of such expectations. The
hierarchy starts from the words defining f,S,V and closes under this operation.
Graph labels can encode the contracted G/G-transpose indices; doing so
preserves actual reuse. Expected graph contractions are admissible scalar
statistics. Their initialization is determined by the prescribed Gaussian
law and tanh, never by future training.

Two restrictions are essential. First, enumerating all monomials of the full
joint block state to increasing degree is the excluded full-law basis route;
renaming those monomials as graphs does not repair it. A successful route
must prove that a substantially smaller, observable-relevant family suffices.
Second, setting longer words or higher connected cumulants to zero is not
justified by (13). On-site nonlinear cumulants already have order-one sources,
as (5) shows. Connected correlations between distinct sites are different
objects and require their own k-dependent analysis.

## 6. The missing theorem, stated so it can be checked

An admissible candidate can retain an observable-dependent family W_P of
contracted words, with x_P=(E[W]:W in W_P), and propose an autonomous closure
\(\dot{\widehat x}_P=F_P(\widehat x_P)\). One sufficient route to a finite-horizon
result identifies the *exact reachable-state residual*

\[
\dot x_P(t)=F_P(x_P(t))+\eta_P(t)
\]

and proves all of the following without invoking a full joint-law solver:

1. A constructive bound \(\sup_{t\le T}\|\eta_P(t)\|\le a_P(T)\to0\).
2. Stability of the finite closure on a region containing both trajectories,
   with a computable Lipschitz bound L_P(T), and valid initialization.
3. Control of the target output, including the query-input domain, from the
   retained words and any stated output approximation.
4. A scalar count and coefficient-computation bound, including its dependence
   on k,m,H,T and accuracy. To be useful, growth of L_P cannot overwhelm
   decay of a_P.

For identical initial states, variation of constants in the elementary scalar
error inequality gives the conditional bound

\[
\sup_{t\le T}\|x_P(t)-\widehat x_P(t)\|
 \le a_P(T)\frac{e^{L_P(T)T}-1}{L_P(T)},
\tag{14}
\]

with the quotient interpreted as T at L_P=0. Derivation: subtract the two
equations, use the Lipschitz bound to get e'(t)<=L_P e(t)+a_P in the upper
Dini-derivative sense, multiply by exp(-L_P t), and integrate. An initial
error contributes exp(L_PT)e(0). Equation (14) is only propagation control;
without item 1 it proves no convergence.

These conditions are sufficient, not necessary. A degree-weighted estimate
or a finite-propagation argument can show that an order-one residual at the
highest retained grades has vanishing influence on fixed low observables.
Such a proof need not make the unweighted residual of the entire retained
state small. The separate bounded-tree construction follows that alternative;
the absence of item 1 is therefore not an obstruction to every closure.

For a large-k diagram proposal the source estimate must also separate its
two errors, for example

\[
a_{P,k}(T)\le A_T\theta_T^P+B_{P,T}/k,\qquad 0<\theta_T<1.
\]

This is a possible proof target, not a result. Constants must be controlled
jointly in P,k,T. A bound with fixed P and k tending to infinity does not
establish arbitrary accuracy at a prescribed finite k; nor does suppression
of individual diagrams control the sum of omitted diagrams. No such source
estimate is proved here.

## Claim status and next bottleneck

- **Proved:** finite-k identities (1)–(4), the small-input cumulant coefficient
  (5), its strict negative sign for every nonzero input in (5a), and the
  initialization mixture identity (6).
- **Exact under smooth integrability:** Gaussian response hierarchy (7)–(9).
  Its needed finite-order time-zero regularity is verified above.
- **Exact algebraic skeleton:** the lifted expected-word hierarchy (10)–(13)
  for a finite input panel.
- **Falsified witness:** present-state Wick closure, or elimination of all
  local higher cumulants using only a 1/k argument.
- **Open:** a sparse aggregate word/response hierarchy with a useful global
  finite-horizon residual bound, and consequently the requested polynomial
  accuracy-versus-size result.

The highest-leverage next step is to choose a specific observable-dependent
word family and prove its omitted-source estimate while retaining the
order-one response in (2). Merely deriving more correct initialization jets,
or invoking Gaussian conditioning without a bounded aggregate state, does
not close that gap.

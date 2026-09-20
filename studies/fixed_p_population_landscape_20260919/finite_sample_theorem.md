# A full-dictionary local-minimum theorem with an explicit sample bound

2026-09-19. Lead derivation from the exact closure equations. This is a
partial resolution of the user's unrestricted fixed-order question: the
number of unoriented input directions is bounded by effective dictionary
dimensions. The full dictionary is retained. No earlier study is a premise.

## 1. Statement and exact model

Let x_1,...,x_m lie on sqrt(d) S^(d-1), with no two equal or antipodal.
Let mu_i>0 sum to one and y_i be arbitrary finite real labels. Put
phi=tanh. The fixed lower probability space is nonatomic. The fixed mark
vectors b_1 in R^(k_1), b_2 in R^(k_2) are bounded, with their exact joint
laws unchanged. Write q_l for the dimension of the span of the coordinate
functions of b_l in population L2. Linear redundancies are allowed.

Train unrestricted fields w in L2(Omega_1;R^d), c in L2(Omega_2), and the
full k_2-by-k_1 matrix M, in the physical L2/L2/Frobenius topology. For
u_i=x_i/sqrt(d), define

\[
 a_i=E_1[b_1\phi(w\cdot u_i)],\quad z_i=b_2^TMa_i,
 \quad H_i=\phi(z_i),\quad f_i=E_2[cH_i],\quad r_i=f_i-y_i,
\]
\[
 d_i=E_2[b_2c\phi'(z_i)],\qquad
 L=\sum_i\mu_i r_i^2.                                      \tag{1}
\]

These are the canonical finite-order contraction equations of established
global_nonlinear.md C.4.7.9.3 and C.4.7.10.C.1/D.3. In particular the
reverse action is M^T, not an independent matrix. The initialization and
ridge select the fixed marks and initial M; the theorem concerns every
ambient state on those fixed carriers, not only reached states.

**Theorem. If q_1>=m and q_2>=m, every local minimum of L has L=0.**
No linear independence of the physical inputs is required. There is no
mark-parity hypothesis or polynomial hypothesis. In particular additional
bounded initialized words and their correlations need not be removed.

For the full canonical circle hierarchy, q_2>=binomial(p+2,2), while
q_1 exceeds the entire upper retained length at every p>=1. Consequently
the theorem applies whenever

\[
                  m\le\binom{p+2}{2}.                       \tag{2}
\]

The count verification is separate in dictionary_counts.md. This explicit
bound is sufficient, not asserted necessary. It does not cover every
finite m at a fixed p. In particular it does not prove the unrestricted
statement posed by the user.

## 2. Input ridge independence and finite-moment derivatives

The functions s->phi(s dot u_i) on R^d are linearly independent. Choose
v avoiding the finitely many hyperplanes orthogonal to u_i and u_i +/- u_j.
Then t_i=v dot u_i are nonzero with distinct squares. A linear relation,
restricted to s=t v and differentiated at zero in its first m odd orders,
gives the Vandermonde equations sum_i alpha_i t_i(t_i^2)^j=0 for
0<=j<m. All odd coefficients of tanh are nonzero: writing
tanh t=sum_{n>=0}(-1)^n a_n t^(2n+1), the equation phi'=1-phi^2 gives
a_0=1 and (2n+1)a_n=sum_{j+k=n-1}a_j a_k>0 for n>=1.
The Vandermonde determinant is the nonzero product of all differences
t_i^2-t_j^2, so the relation is zero.

The exact derivatives in the finite moment and matrix variables are

\[
 \delta L=2\sum_i\mu_i r_i d_i^TM\delta a_i,
 \qquad \nabla_ML=2\sum_i\mu_i r_i d_i a_i^T.               \tag{3}
\]

At fixed c,M the loss is a C2 function of finitely many a_i, with a
quadratic Taylor remainder locally uniform in those moments. Bounded b_2,
bounded first two derivatives of phi, and E|c|<=||c||_2 justify this.
Differentiation in c is an unrestricted L2 variation and gives

\[
                 \nabla_cL=2\sum_i\mu_i r_i H_i.             \tag{4}
\]

## 3. A necessary condition forced by small population subsets

At a local minimum define, for a lower population point omega,

\[
 F_\omega(s)=\sum_i\mu_i r_i
              [b_1(\omega)^TM^Td_i]\phi(s\cdot u_i).         \tag{5}
\]

For almost every omega, w(omega) must globally minimize F_omega over
finite s in R^d. Otherwise countability of rational s, positive rational
margins, and integer bounds on |w| gives a fixed s, delta>0, R<infinity
and a positive-measure set B where |w|<=R and
F_omega(s)-F_omega(w)<=-delta. Nonatomicity supplies subsets E of B
with arbitrarily small positive measure epsilon. Replace w by s on E.
The squared physical displacement is at most epsilon(|s|+R)^2, and

\[
 \delta a_i=\int_E b_1[\phi(s\cdot u_i)-\phi(w\cdot u_i)]\,dP_1
                          =O(\varepsilon).
\]

Equation (3) and its quadratic remainder give

\[
 L_{\rm new}-L
 =2\int_E[F_\omega(s)-F_\omega(w)]\,dP_1+O(\varepsilon^2)
 \le-2\delta\varepsilon+O(\varepsilon^2)<0,
\]

contradicting local minimality. For the canonical carrier, the required
arbitrarily small subsets follow directly by intersecting B with
{g_1<=t}: Gaussian g_1 has no atoms, so the mass is continuous in t.

Thus F_omega(w)<=F_omega(0)=0. Matrix stationarity gives

\[
 E_1F_\omega(w)
 =\sum_i\mu_i r_i d_i^TMa_i
 =\tfrac12\langle\nabla_ML,M\rangle_F=0.
\]

It follows that F_omega(w)=0 almost surely. A globally minimized odd
function with minimum zero is identically zero. Input ridge independence
from section 2 therefore gives, separately for every sample,

\[
                 r_i b_1^TM^Td_i=0\quad\hbox{a.s.}           \tag{6}
\]

This condition does not require that b_1 have independent coordinates.

## 4. Prediction-preserving matrix changes expose the full backward vector

Let B_1 be the linear span of the essential range of b_1, equivalently
the orthogonal complement of the nullspace of E_1[b_1b_1^T]. Its dimension
is q_1. Every a_i belongs to B_1. Write A=[a_1 ... a_m].

Suppose first rank A<q_1. Choose nonzero q in B_1 orthogonal to all a_i.
For any z in R^(k_2), the perturbation

\[
                         M_t=M+t zq^T                       \tag{7}
\]

leaves M_t a_i=M a_i for every i, hence preserves every H_i, f_i, r_i,
and d_i exactly. A sufficiently small such perturbation of a local minimum
is itself a local minimum: its value is unchanged and it lies inside
the original minimality ball. Apply (6) at M and at M_t and subtract:

\[
                 t r_i (b_1^Tq)(z^Td_i)=0\quad\hbox{a.s.}
\]

Since q belongs to B_1 and is nonzero, E_1(b_1^Tq)^2>0. Taking each
coordinate vector z and a nonzero sufficiently small t gives r_i d_i=0.

The only remaining possibility under q_1>=m is q_1=m=rank A. In this
case A has full column rank, so A^T has a right inverse R. Set
D_r=[mu_1 r_1 d_1 ... mu_m r_m d_m]. Matrix stationarity is
D_r A^T=0; multiplication by R gives D_r=0. Again r_i d_i=0 for all i.
We have proved at every local minimum that

\[
                            r_i d_i=0\quad(1\le i\le m).    \tag{8}
\]

The equal-dimension case in this paragraph was supplied by the abstract
route author after its independent candidate had frozen; the strict
inequality/null-direction argument was the lead's separate derivation.

## 5. Readout-null changes and the dimension contradiction

Let H=span{H_1,...,H_m} in upper population L2. If L>0, some residual
is nonzero; equation (4) is then a nontrivial linear relation among the
H_i. Therefore dim H<=m-1.

For any k in H-perp, the change c_t=c+t k leaves all predictions and
residuals exactly unchanged. For sufficiently small t it also preserves
local minimality, by the same minimality-ball argument used above.
Fix i with r_i!=0 and apply (8) before and after this change. Linearity
of d_i in c gives

\[
                      E_2[b_2 k\phi'(z_i)]=0
                 \qquad\hbox{for every }k\in H^\perp.       \tag{9}
\]

Each coordinate function of b_2 phi'(z_i) must therefore lie in H.
Multiplication by phi'(z_i)>0 almost surely is injective on the q_2
dimensional span of the b_2 coordinates. It maps that span into L2
because the gate is bounded. Thus its image has dimension q_2, and
(9) implies q_2<=dim H<=m-1, contradicting q_2>=m.
This proves the theorem.

## 6. Attainability and conflicting observations

For the canonical full dictionary at any p>=1, constants belong to the
lower span and X=tanh xi_1 belongs to the upper span, with a positive
density on (-1,1). Let v avoid the finite hyperplanes in section 2 and
set w identically equal to v. Put a_0=E_1 b_1, which is nonzero because
the constant belongs to the lower span. Choose e such that b_2^T e=X
and set M=e a_0^T/|a_0|^2. Then H_i=phi(t_i X), where
t_i=phi(v dot u_i) are nonzero with distinct squares. The same odd Taylor
and Vandermonde argument gives independent H_i. Their Gram K is positive
definite, and c=sum_j(K^(-1)y)_j H_j fits every label exactly. This
construction retains the entire dictionary and has bounded fields.

For arbitrary repeated or antipodal observations, group modulo sign.
Choose representatives x_g and write x_i=s_i x_g, s_i in {-1,1}. Put
p_g=sum_(i in g) mu_i, ybar_g=sum_(i in g)mu_i s_i y_i/p_g, and
C=sum_g sum_(i in g)mu_i(s_i y_i-ybar_g)^2. Input oddness gives

\[
                   L=C+\sum_g p_g(f(x_g)-\bar y_g)^2.       \tag{10}
\]

If the number of groups satisfies the theorem's dimension hypotheses,
every local minimum has loss C. The construction above fits all group
averages, so C is the global minimum. C=0 exactly when the signed labels
agree in each group. Arbitrary linear dependencies among different
representatives are permitted.

## 7. Scope and outstanding claim

This is an exact full-dictionary population theorem under an explicit
sample bound. It is not a theorem for a fixed particle approximation,
an odd-only artificial restriction, or a modified ridge/filter. It uses
no future trajectory, reference endpoint, Gram-conditioning hypothesis,
or assumption of parameter convergence. It supplies no trajectory fitting,
rate, canonical reachability, or basin measure statement.

For each finite compatible circle dataset, a sufficiently large finite p
satisfies (2). For each specified p it includes all datasets with at most
binomial(p+2,2) unoriented input directions, in every angular arrangement.
The requested stronger statement with arbitrary m at that same fixed p
remains unresolved by this proof. Its failure would not be demonstrated
by failure of a derivative-feature separation lemma alone.

Status at first freeze: complete lead proof candidate awaiting internal
review of the argument and the full canonical dimension count.

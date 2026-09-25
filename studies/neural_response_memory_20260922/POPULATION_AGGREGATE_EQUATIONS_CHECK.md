# First scalar aggregates of the chronological population closure

Date: 2026-09-25. Status: scoped author derivation; exact identities for a
fixed history order, with the finite scalar closure question left explicit.
This is not an independent review or a population-limit theorem. The initial
scientific inputs were `MOMENT_CONSTRUCTION.md`, `DEEP_CIRCLE_DERIVATION.md`,
and `docs/NOTATION.md`, all read in full. A subsequent explicitly authorized
scope extension added `deep_moment_engine.py` and `moment_engine.py` for the
bounded deterministic algebra check recorded below; both were read in full.

The construction below starts from the existing chronological Legendre
population fields. It gives a concrete scalar aggregate state that determines
the first velocities of training and fixed-test outputs, differentiates its
history Grams, and exhibits the additional gated and initialized-operator
statistics. It does not start from a dense-network derivative expansion.

## 1. Precise object and normalization

Fix the history order P >= 1, M training inputs U_a=x_a/sqrt(d), and a finite
set of additional query inputs. Let q,p range over the union of training and
query indices, and a,b over training indices only. Write G_qa=U_q^T U_a.
Queries have responses and backward responses, but do not contribute to the
loss or the history sources. Their number must be fixed when counting scalar
state size; this note does not compress a function of every possible input.

Use three probability spaces Omega_1, Omega_2, Omega_3 with expectations
E_1,E_2,E_3. Each initialized internal operator W_{ell,0} maps the preceding
population to population ell, and W_{ell,0}^* is its actual adjoint. The rank
one operator A tensor B acts as v -> A E_{ell-1}[Bv]. At finite width these
are exact notational replacements for a uniform population of n coordinates:
E_ell[UV]=u^T v/n and A tensor B has matrix AB^T/n. The initialized matrix
itself remains the actual W_{ell,0}, without another factor of n.

For a nonatomic population, the equations are conditional on the existence
of these coupled operators, solutions, and integrability sufficient for the
products and differentiations below. For example, a differentiable solution
in finite-dimensional invariant function spaces suffices. No independence
between an initialized action and its evolving arguments is imposed, and no
finite-width-to-population limit is claimed.

Let L be the history length in the supplied derivation, not the number of
hidden layers, and let rho be the residual RMS. Define

\[
 w_k=2k+1,\qquad
 ({\cal T}X)_{k,a}=kX_{k,a}+\sum_{j<k}w_jX_{j,a},\qquad
 \bar A_{\ell,a}=L^{-1}\sum_{k<P}w_kA_{\ell,k,a},\qquad
 \bar B_{\ell,a}=L^{-1}\sum_{k<P}w_kB_{\ell,k,a}.
 \tag{1}
\]

The bars are endpoint history reconstructions, not population expectations.
All fields belong to the current order-P chronological surrogate. Its exact
equations from the assigned sources, in population notation, are

\[
 \dot A_{\ell,k,a}=r_a\Delta_{\ell,a}-(\rho/L)({\cal T}A_\ell)_{k,a},
 \qquad
 \dot B_{\ell,k,a}=\rho H_{\ell-1,a}-(\rho/L)({\cal T}B_\ell)_{k,a},
 \quad \ell=2,3,
 \tag{2}
\]

\[
 W_\ell=W_{\ell,0}-\frac2{ML}
       \sum_{a,k<P}w_k A_{\ell,k,a}\otimes B_{\ell,k,a},
 \quad
 \dot W^{(1)}_j=-\frac2M\sum_a r_a\Delta_{1,a}U_{a,j},
 \quad
 \dot c=-\frac2M\sum_a r_aH_{3,a}.
 \tag{3}
\]

Here W^{(1)}_j is the first-layer weight field for input coordinate j,
Z_{1,q}=sum_j W^{(1)}_j U_{q,j}, Z_{ell,q}=W_ell H_{ell-1,q},
H_{ell,q}=tanh(Z_{ell,q}), f_q=E_3[c H_{3,q}], r_a=f_a-y_a,
and rho^2=M^{-1}sum_a r_a^2. The backward fields are

\[
 \Delta_{3,q}=c(1-H_{3,q}^2),\qquad
 \Delta_{\ell,q}=(1-H_{\ell,q}^2)W_{\ell+1}^*\Delta_{\ell+1,q}
 \quad(\ell=1,2).
 \tag{4}
\]

Products within a population are pointwise. Work first on rho>0 and L>=1;
at a consistent zero training residual state all physical and moment
velocities are zero and every fixed-query prediction is stationary.

## 2. A concrete initial list of scalar aggregates

Form the finite field lists

\[
\begin{aligned}
 \mathcal S_1&=(1,\{W^{(1)}_j\}_{j=1}^d,\{H_{1,q},\Delta_{1,q}\}_q,
                         \{B_{2,k,a}\}_{k,a}),\\
 \mathcal S_2&=(1,\{H_{2,q},\Delta_{2,q}\}_q,
                         \{A_{2,k,a},B_{3,k,a}\}_{k,a}),\\
 \mathcal S_3&=(1,c,\{H_{3,q},\Delta_{3,q}\}_q,
                         \{A_{3,k,a}\}_{k,a}).
\end{aligned}
 \tag{5}
\]

The starting scalar observable map is

\[
 Q^{[0]}=\left(L,\rho,
        \{\mathbb E_\ell[\mathcal S_{\ell,i}\mathcal S_{\ell,j}]\}_{\ell,i\le j}\right).
 \tag{6}
\]

This is an actual finite list of real numbers. Including the constant field
also includes means; including backward fields is a redundant exact lift.
If J is the number of training-plus-query inputs, the three list lengths are
1+d+2J+MP, 1+2J+2MP, and 2+2J+MP. Thus the size of (6) is independent of
width for fixed P,M,d,J. An equation determining its derivative from itself
has not yet been established.

Initialize by the specified network initialization and exact forward and
adjoint passes, followed by A=0, B_{ell,0,a}=H_{ell-1,a}(0), and B_{ell,k,a}=0
for k>0, with L=1. Every coordinate in (6) is then a permitted present-time
expectation; no future trajectory enters. Merely specifying this initialization
does not prove these expectations have finite deterministic descriptions in
a proposed infinite-population limit.

For readable equations, name the following entries or linear combinations
of (6):

\[
\begin{aligned}
 C_\ell(q,p)&=\mathbb E_\ell[H_{\ell,q}H_{\ell,p}],&
 R_\ell(q,p)&=\mathbb E_\ell[\Delta_{\ell,q}\Delta_{\ell,p}],\\
 D_\ell(q;k,a)&=\mathbb E_\ell[\Delta_{\ell,q}A_{\ell,k,a}],&
 V_\ell(k,a;q)&=\mathbb E_{\ell-1}[B_{\ell,k,a}H_{\ell-1,q}],\\
 T_\ell(q,a)&=L^{-1}\sum_kw_kD_\ell(q;k,a),&
 S_\ell(a,q)&=L^{-1}\sum_kw_kV_\ell(k,a;q).
\end{aligned}
 \tag{7}
\]

The f_q are also entries of (6). All sums over k in this note run from 0 to
P-1 unless stated otherwise.

## 3. Exact first A/B Gram equations

For each link define

\[
 X_\ell(k,a;l,b)=\mathbb E_\ell[A_{\ell,k,a}A_{\ell,l,b}],\qquad
 Y_\ell(k,a;l,b)=\mathbb E_{\ell-1}[B_{\ell,k,a}B_{\ell,l,b}].
 \tag{8}
\]

The index l here is a history order; the layer is ell. Applying the product
rule to (2), without a distributional approximation, gives

\[
\begin{aligned}
 \dot X_\ell(k,a;l,b)
 &=r_aD_\ell(a;l,b)+r_bD_\ell(b;k,a)\\
 &\quad-\frac\rho L\left[(k+l)X_\ell(k,a;l,b)
       +\sum_{j<k}w_jX_\ell(j,a;l,b)
       +\sum_{j<l}w_jX_\ell(k,a;j,b)\right],\\
 \dot Y_\ell(k,a;l,b)
 &=\rho\{V_\ell(l,b;a)+V_\ell(k,a;b)\}\\
 &\quad-\frac\rho L\left[(k+l)Y_\ell(k,a;l,b)
       +\sum_{j<k}w_jY_\ell(j,a;l,b)
       +\sum_{j<l}w_jY_\ell(k,a;j,b)\right].
\end{aligned}
 \tag{9}
\]

For P=1 this reduces to dot X(a,b)=r_a D(a;b)+r_b D(b;a) and
dot Y(a,b)=rho(V(b;a)+V(a;b)); neither first derivative calls for higher
history order. It calls for mixed current/history pairings already in (6).

The middle population contains both A_2 and B_3. Its cross Gram
Z(k,a;l,b)=E_2[A_{2,k,a}B_{3,l,b}] has derivative

\[
\begin{aligned}
 \dot Z(k,a;l,b)
 &=r_a\mathbb E_2[\Delta_{2,a}B_{3,l,b}]
   +\rho\mathbb E_2[A_{2,k,a}H_{2,b}]\\
 &\quad-\frac\rho L\left[(k+l)Z(k,a;l,b)
   +\sum_{j<k}w_jZ(j,a;l,b)+\sum_{j<l}w_jZ(k,a;j,b)\right].
\end{aligned}
 \tag{10}
\]

These are legal same-population contractions. An expression E[A_ell B_ell]
would instead be ill-typed across the two populations without an operator.
The full second-moment list (6) includes both new endpoint pairings in (10).

The A/B Grams genuinely control the low-rank learned part. For instance, with
K_ell=W_ell-W_{ell,0},

\[
 \|K_\ell\|_{\rm HS}^2
 =\frac4{M^2L^2}\sum_{a,b,k,l}w_kw_l
        X_\ell(k,a;l,b)Y_\ell(k,a;l,b).
 \tag{11}
\]

Only K_ell is asserted Hilbert--Schmidt here. Nothing in (11) removes the
initialized operator or determines its action on evolving fields.

## 4. Exact training and fixed-test output velocities

Differentiating the projected chronological operator in (3), the same
Legendre triangular cancellation as in the assigned derivation yields

\[
 \dot W_\ell=-\frac2M\sum_a
  \left[r_a\Delta_{\ell,a}\otimes\bar B_{\ell,a}
       +\rho\bar A_{\ell,a}\otimes H_{\ell-1,a}
       -\rho\bar A_{\ell,a}\otimes\bar B_{\ell,a}\right].
 \tag{12}
\]

To verify the cancellation directly, differentiation of
L^{-1}sum_k w_k A_k tensor B_k has two endpoint sources. The derivative of
L^{-1}, the two diagonal transports, and the two strict triangular sums
contribute -rho L^{-2}sum_{k,l}w_kw_l A_k tensor B_l. The diagonal coefficient
is w_k(1+2k)=w_k^2; the triangular sums give the off-diagonal coefficients.
This proves (12) using (2), rather than assuming dense gradient velocities.

The exact chain rule and the actual adjoints give

\[
 \dot f_q=\mathbb E_3[\dot c H_{3,q}]
      +\mathbb E_1[\Delta_{1,q}\dot Z_{1,q}]
      +\sum_{\ell=2}^3
            \mathbb E_\ell[\Delta_{\ell,q}\dot W_\ell H_{\ell-1,q}].
 \tag{13}
\]

Inserting dot Z_{1,q}=-(2/M)sum_a r_aG_qa Delta_{1,a}, (3), and (12) gives

\[
\begin{aligned}
 \dot f_q={}&-\frac2M\sum_a r_a
       \{C_3(q,a)+G_{qa}R_1(q,a)\}\\
 &-\frac2M\sum_{\ell=2}^3\sum_a
   \left\{r_aR_\ell(q,a)S_\ell(a,q)
       +\rho T_\ell(q,a)
               [C_{\ell-1}(a,q)-S_\ell(a,q)]\right\}.
\end{aligned}
 \tag{14}
\]

Consequently (6) determines every first output velocity, as well as
dot L=rho and dot rho=(M rho)^{-1}sum_a r_a dot f_a. Query labels are never
needed. The formula is for the order-P surrogate's own trajectory.
For two hidden layers delete the upper internal link, replace C_3 by C_2,
and use the corresponding two-layer backward fields.

At initialization, bar A=0 and bar B=H(0), so T=0 and S=C for training and
query columns. Formula (14) then has the same initial output velocity as the
dense network. This checks the sign, factors, and fixed-query extension of
the supplied zero-initial-defect identity. It does not prove later agreement.

## 5. The first additional gated and operator-weighted statistics

The mixed pairings that entered (9) obey

\[
\begin{aligned}
 \dot D_\ell(q;k,a)
 &=\mathbb E_\ell[\dot\Delta_{\ell,q}A_{\ell,k,a}]
        +r_aR_\ell(q,a)
        -\frac\rho L\left[kD_\ell(q;k,a)
                    +\sum_{j<k}w_jD_\ell(q;j,a)\right],\\
 \dot V_\ell(k,a;q)
 &=\rho C_{\ell-1}(a,q)
        -\frac\rho L\left[kV_\ell(k,a;q)
                    +\sum_{j<k}w_jV_\ell(j,a;q)\right]
        +\mathbb E_{\ell-1}[B_{\ell,k,a}\dot H_{\ell-1,q}].
\end{aligned}
 \tag{15}
\]

Thus the obstruction is a specified pair of terms, not an unspecified
appeal to nonclosure. For the lower forward mixed pairing, it is exactly

\[
 \mathbb E_1[B_{2,k,a}\dot H_{1,q}]
 =-\frac2M\sum_b r_bG_{qb}
      \mathbb E_1[B_{2,k,a}(1-H_{1,q}^2)\Delta_{1,b}].
 \tag{16}
\]

The right side contains the second moment E[B_2 Delta_1] minus the fourth
mixed moment E[B_2 H_{1,q}^2 Delta_1]. It is therefore a concrete new
statistic relative to the displayed second-moment coordinates. This algebra
alone does not prove that no identity determines it on the reachable states.

For the upper forward mixed pairing, put
J_{2,k,a;q}=E_1[B_{2,k,a} dot H_{1,q}], whose expression is (16). Equations
(3) and (12) give the actual preactivation velocity

\[
\begin{aligned}
 \dot Z_{2,q}
 &=W_{2,0}\dot H_{1,q}
   -\frac2{ML}\sum_{k,a}w_k A_{2,k,a}J_{2,k,a;q}\\
 &\quad-\frac2M\sum_b
   \{r_b\Delta_{2,b}S_2(b,q)
     +\rho\bar A_{2,b}[C_1(b,q)-S_2(b,q)]\}.
\end{aligned}
 \tag{17}
\]

Multiplying (17) by B_{3,k,a}(1-H_{2,q}^2) and taking E_2 lists exactly the
new terms in E_2[B_{3,k,a} dot H_{2,q}]:

\[
\begin{aligned}
 &\mathbb E_2[B_{3,k,a}(1-H_{2,q}^2)W_{2,0}\dot H_{1,q}],\\
 &\mathbb E_2[B_{3,k,a}(1-H_{2,q}^2)A_{2,j,b}],\qquad
 \mathbb E_2[B_{3,k,a}(1-H_{2,q}^2)\Delta_{2,b}].
\end{aligned}
 \tag{18}
\]

The first term in (18), after substituting dot H_1, requires the initialized
operator statistic

\[
 \mathbb E_2\!\left[
  B_{3,k,a}(1-H_{2,q}^2)
  W_{2,0}\big((1-H_{1,q}^2)\Delta_{1,b}\big)\right].
 \tag{19}
\]

Its adjoint form uses the same W_{2,0}^*. Its value is not replaced here by
a product of means or an independent Gaussian action.

The other new term in (15) is determined by the differentiated backward
recurrence, whose exact expressions are

\[
 \dot\Delta_{3,q}=\dot c(1-H_{3,q}^2)
                     -2cH_{3,q}\dot H_{3,q},
 \tag{20}
\]

\[
\begin{aligned}
 \dot\Delta_{\ell,q}
 &=-2H_{\ell,q}\dot H_{\ell,q}\,
                        W_{\ell+1}^*\Delta_{\ell+1,q}\\
 &\quad+(1-H_{\ell,q}^2)
       \{\dot W_{\ell+1}^*\Delta_{\ell+1,q}
                          +W_{\ell+1}^*\dot\Delta_{\ell+1,q}\},
                  \qquad \ell=1,2.
\end{aligned}
 \tag{21}
\]

The transpose of (12) determines dot W^* using those same factors, and
dot H_{ell,q}=(1-H_{ell,q}^2)dot Z_{ell,q}. Thus no untracked derivative is
being prescribed externally in (20)--(21); these are finite substitutions
in the population vector field. On multiplying by A or Delta and averaging,
they introduce readout-gated products and gated initialized-adjoint actions.
For example, the first term of (20) contributes
-(2/M)sum_b r_b E_3[A_{3,k,a}H_{3,b}(1-H_{3,q}^2)] to dot D_3.

Likewise

\[
 \dot C_\ell(q,p)
 =\mathbb E_\ell[\dot H_{\ell,q}H_{\ell,p}
                         +H_{\ell,q}\dot H_{\ell,p}],\qquad
 \dot R_\ell(q,p)
 =\mathbb E_\ell[\dot\Delta_{\ell,q}\Delta_{\ell,p}
                         +\Delta_{\ell,q}\dot\Delta_{\ell,p}]
 \tag{22}
\]

requires the corresponding gated versions. Equations (15)--(22) specify a
constructive first enlargement of (6). Differentiating that enlargement may
create further products and operator compositions; no finite termination is
asserted without a reachable-state relation.

Even ungated initialized-operator pairings carry additional information. If
O_ell(k,a;l,b)=E_ell[A_{ell,k,a} W_{ell,0}B_{ell,l,b}], then

\[
\begin{aligned}
 \dot O_\ell(k,a;l,b)
 &=r_a\mathbb E_\ell[\Delta_{\ell,a}W_{\ell,0}B_{\ell,l,b}]
   +\rho\mathbb E_\ell[A_{\ell,k,a}W_{\ell,0}H_{\ell-1,b}]\\
 &\quad-\frac\rho L\left[(k+l)O_\ell(k,a;l,b)
  +\sum_{j<k}w_jO_\ell(j,a;l,b)+\sum_{j<l}w_jO_\ell(k,a;j,b)\right].
\end{aligned}
 \tag{23}
\]

There is no dot W_{ell,0} term because that operator is fixed. Being fixed
does not make its contractions determined by unweighted Grams. For example,
E_ell[(W_{ell,0}X)(W_{ell,0}Y)] equals
E_{ell-1}[X W_{ell,0}^*W_{ell,0}Y], which depends on an operator-weighted
pairing unless an additional relation on the relevant fields is proved.

## 6. An exact criterion for finishing a finite scalar closure

Fix P and an admissible restart domain R of population states of this
chronological surrogate. Include any allowed finite list of fixed initial
parameters theta explicitly. Let V_P denote its autonomous population
vector field, and Q:R->R^N a continuously differentiable scalar observable
map containing the required outputs. An exact pointwise scalar vector field
g satisfying

\[
 DQ(m)V_P(m)=g(Q(m);\theta)
 \tag{24}
\]

exists on Q(R) if and only if

\[
 Q(m)=Q(m')\ \Longrightarrow\
 DQ(m)V_P(m)=DQ(m')V_P(m')
 \quad\hbox{for all }m,m'\in R
 \tag{25}
\]

with the same theta. Necessity follows by evaluating (24) twice. For
sufficiency define g(q;theta) by the derivative at any preimage; (25) makes
this independent of the preimage. This is a pointwise factorization result.
For a uniquely restartable ODE one must additionally establish suitable
regularity, for example a locally Lipschitz extension of g to a neighborhood
of Q(R). Rational closure requires the stronger fact that the components of
g are rational functions of the retained scalars on their domain.

For the particular Q^{[0]} in (6), equations (15)--(23) name the first terms
whose constancy on its level sets must be shown, or whose values must be
added as further coordinates. Their appearance does not by itself disprove
(25). A proof of failure needs two admissible same-Q states with different
derivatives. A proof of success needs identities valid on the intended
restart domain, not an interpolation along one known trajectory.

One explicit sufficient condition is instructive. Suppose each population
has a finite-dimensional unital algebra of bounded real functions, containing
all initialized fields in (5), closed under pointwise multiplication, and
such that W_{ell,0} and W_{ell,0}^* map the respective algebras into one
another. Every term in (2)--(4), (12), and the rational response lift then
stays in these algebras: learned rank-one actions produce scalar multiples
of retained fields, and gates and backward products remain in the algebras.
In fixed bases with nonsingular expectation Gram matrices, coefficients are
recovered from finitely many linear global averages. They satisfy a finite
rational ODE on rho>0,L>0. This proves a conditional finite closure without
assuming that Gaussian/tanh initialization satisfies the condition.

Finite atomic populations always give such an algebra, but its dimension
can grow with n and therefore do not solve the intended width-independent
compression problem. Treating a basis cell per neuron as a new scalar
aggregate only renames the original population state. No finite invariant
algebra or other finite sufficient statistic has been established here for
the supplied Gaussian initialization and evolving tanh gates.

## 7. What is established and what remains open

Equations (6), (9), (10), and (14) provide a concrete starting aggregate
state and exact first aggregate dynamics inherited from the chronological
order-P population closure. The first extra statistics are the gate-weighted
moments and coupled initialized-operator contractions in (16)--(23).
All retained operator actions and adjoints are those of the same original
initialized operators. No trajectory fitting, training experiment, Gaussian
independence replacement, or direct dense derivative hierarchy was used.

The unresolved step is to prove finite factorization (24), or a controlled
approximation to it, with state and coefficient complexity independent of
width and initialization information confined to a permitted finite list.
A scalar aggregate approximation introduces a second approximation beyond
the history truncation P. Neither its error nor its propagation follows
solely from the already available Legendre omitted-covariance defect.
Failure of a chosen finite statistic list would not rule out a richer finite
list or an accuracy-dependent scalar hierarchy.

## 8. Bounded deterministic algebra check

`check_population_aggregate_equations.py` fixes n=7, d=2, M=3 and two
passive query inputs. For each P=1,2,3 it checks initialization and one
deterministically perturbed nonzero-history state with L=1.37. The latter
states are valid algebraic states of the implemented vector field; no claim
that a training trajectory reaches them is required or made. No ODE is
integrated. The pass threshold was fixed in the script before execution:
max absolute discrepancy divided by max(1, reference max absolute value)
must not exceed 2e-11, with finite values throughout.

There are 198 comparisons over six cases. They cover (9)--(10), (11),
(12), (14)--(17), (19)--(21), and the agreement of the current fields.
Scalar output velocities are compared both with the implemented chain rule
and with automatic directional differentiation of an independently written,
explicit tiny reconstructed-network map. Both training and passive-query
columns are tested. All comparisons passed; the largest normalized
discrepancy was 3.3306690738754696e-16.

Results and environment/source metadata are in
`data/generated/neural_response_memory_20260922/population_aggregate_algebra01/results.json`.
The first launch with the system Python stopped immediately because PyTorch
was absent. The completed launch used the existing interpreter
`/home/amir/miniconda3/bin/python`, CPU only, with OPENBLAS_NUM_THREADS=1,
OMP_NUM_THREADS=1, MKL_NUM_THREADS=1 and PYTHONDONTWRITEBYTECODE=1.
No dependency installation or configuration search was needed. The report
hash in that result identifies the version before this evidence paragraph
and a field-list notation cleanup; the checked equations are unchanged.

This check supports algebraic implementation agreement only. It does not
establish finite scalar closure, population convergence, reachability of the
perturbed states, accuracy at positive training time, or any width-uniform
approximation result.

Read-version SHA256 hashes:

| Input | SHA256 |
|---|---|
| MOMENT_CONSTRUCTION.md | 5d8bf7fb354fbdef138676ca0ee5d59799a9032e6f6f531ca4650c8e0e5a9025 |
| DEEP_CIRCLE_DERIVATION.md | 17ffa7efe44d588a47b8f566c5cbdc72199e012ae058bab232427e6685203bd9 |
| docs/NOTATION.md | 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b |
| deep_moment_engine.py | 97aa9bc3ac99a982ec81ab8abac3e240aca2e05aecb37e1d6a24b3e7f4ba9f23 |
| moment_engine.py | ebf39cf377f1eb0f5dea64fa1ab946fddcb11a662b2368472017abef9237acd9 |

Required process inputs: `solve-math-rigorously/SKILL.md`,
`investigate-conjectures/SKILL.md`, and the latter's research-contract,
adversarial-audit, and decisive-experiments references. Author scope: population aggregate derivation
subagent. No Git mutation or unrelated study access was performed.

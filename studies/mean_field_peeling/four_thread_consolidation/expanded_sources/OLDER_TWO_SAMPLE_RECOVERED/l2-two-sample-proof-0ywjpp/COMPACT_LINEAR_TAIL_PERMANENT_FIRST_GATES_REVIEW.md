# Isolated adversarial audit: permanent individual first gates

Scope: the root and its sole permitted dependency were read in full (147 and
564 lines). No other mathematical/project files, history, reviews, agents,
experiments, imports, or external sources were used. The dependency's opening
reference to another file was not followed; its displayed proof is sufficient
for the uses audited here. No source edits.

SHA256:
- COMPACT_LINEAR_TAIL_PERMANENT_FIRST_GATES.md:
  dcaaea01fe2f22b8848da127eed58fbcf29bc8fe9fba516ebcaa0dde70abac20
- COMPACT_FIRST_LINEAR_TAIL_TOP_CLOCK.md:
  cb0a9abb96ede054190b54cf883f9bd51081b39c3d7b36689eaa335268301e8b

**Verdict: PASS as stated, on the explicitly augmented event.** The claimed
fixed subsets and uniform all-time gate-square lower bounds follow for actual
finite canonical GF. The dependency's successful event alone does NOT imply
unsaturated first-gate mass; a positive-probability counterexample is given
below. The root correctly adds strip-count conditions and their failure cost.

## 1. Exact model and normalization

Write p=phi_1', r=f-y, s=||r||, b=||W^3||/sqrt(n), and c_a=-2r_a.
The displayed canonical model has f_a=(W^3)^T h^2_a/n and loss L=sum_a r_a^2.
Its Euclidean gradients are
    grad_1 L=(2/n)sum_a r_a delta^1_a x_a^T,
    grad_2 L=(2/n)sum_a r_a delta^2_a(h^1_a)^T,
    grad_3 L=(2/n)sum_a r_a h^2_a.
Thus dependency (5) uses block rates n/d, 1, n, respectively. Multiplying
dot W^1 by x_a gives exactly
    dot z^1_a=sum_b C_ab p(z^1_b)c_b q_b,
    C_ab=x_a^T x_b/d,  q_b=(W^2)^T[W^3 p_2(z^2_b)],
where p_2=phi_2'. There is no additional 1/n in this first-coordinate ODE.
The root's q excludes residuals; dependency (32)'s control includes -2r_a.
These conventions agree after multiplying the root's q by c_a.

"Canonical" here means precisely dependency (4), (5), (37); no alternative
external normalization is assumed. The initialization remains independent
N(0,1/d), N(0,1/n), N(0,n^-2) entries in the three displayed blocks.

## 2. Dependency audit: existence, coercivity, balance, and clocks

Dependency (7)--(13) are correct. A row saturated on both inputs has identically
zero first-row velocity on that invariant subspace; local uniqueness fixes
it throughout the actual solution. Its two feature values are ±A.
The frozen Gram eigenvalues are 2A^2 N_s/n and 2A^2 N_o/n. All other rows
add positive semidefinite matrices. Differentiating predictions gives the
three kernels in (9), each a Gram matrix, and exactly
    -dot L=4r^T K r
          =||dot W^3||^2/n+||dot W^2||_F^2+(d/n)||dot W^1||_F^2.
Integrating squared speeds and applying Cauchy--Schwarz gives (11).
On a finite maximal interval the same bound between two times makes the
parameter path Cauchy at its endpoint. Its finite limit and the smooth vector
field extend the solution. This proves global finite-time existence for
every finite initial state, without any success-event hypothesis.

On G_1>=gamma I, the exact identity
    K_2=(1/n)sum_j (W^3_j)^2 D_j G_1 D_j >= gamma b^2 I
uses congruence and p_2>=1, and yields dot s<=-2gamma b^2 s when s>0.
Zero residual makes every velocity zero, resolving that endpoint.

For B=W^2-A_0, a=||B||_F, X(t)=integral_0^t s b, direct differentiation gives
    d(a^2-b^2)/dt
      =-(4/n)sum_a r_a <W^3,D(z^2_a)-p_2(z^2_a) A_0h^1_a>,
    D(z)=epsilon[z/(1+z^2)-arctan z].
D'(z)=-2epsilon z^2/(1+z^2)^2 and the two limits give ||D||_infty=epsilon*pi/2.
With the constants in (15), Cauchy--Schwarz therefore proves
    ||dot B||_F<=C_B s b,  a<=C_B X,
    |a^2-b^2+b_0^2|<=C_D X,
    ||f||<=C_f b(a_0+a)<=C_f b(a_0+b+sqrt(C_D X)).
No derivative of moving features is missing: the differentiated quantities
are parameter norms. The A_0 error uses its operator norm, not its Frobenius
norm. These observations validate the essential width normalization.

After L(t_0)<2, loss monotonicity implies ||f||>=eta=sqrt(2)-s(t_0)>0.
Splitting b<=1 and b>=1 gives dependency (23),
    b>=c/(1+sqrt(X)), c=min{1,eta/[C_f(a_0+1+sqrt(C_D))]}>0.
Since X'=s b>=0,
    dot s<=-2gamma b X'<=-2gamma c X'/(1+sqrt(X)).
Integrating in physical time proves
    s(t)+2gamma c[F(X(t))-F(X(t_0))]<=s(t_0),
    F(x)=2[sqrt(x)-log(1+sqrt(x))].
F is increasing, unbounded, and satisfies F(x)>=sqrt(x)-2log(2).
This proves the stated finite clock bound without inverting X or assuming
its integrability. Equations (16), (19) then bound a,b,||W^2||; (23) gives
b>=beta>0 after t_0. Hence L decays at rate 4gamma beta^2 and the unweighted
clock is finite with exactly the bound in (28).

Before t_0, (11) gives b(t)<=b_0+sqrt(t L(0)), so
    X(t_0)<=sqrt(L(0)) b_0 t_0+(2/3)L(0)t_0^(3/2).
Thus the constants are not circular. The speed bounds (30)--(31) follow
from ||delta^1_a||<=PMU sqrt(n)b and ||h^2_a||<=MAU sqrt(n).
They give finite parameter variation and limits at each finite n.
The separate control bound (32) is also correct:
    integral ||-2r_a q_a||/sqrt(n)<=2MU integral s b.
These ancillary conclusions do not require an additional assumption.

## 3. Dependency audit: actual success event and uniform constants

The short-time lemma is valid. Energy and Lipschitz continuity give
    ||H^1(t)-H^1(0)||_F/sqrt(n)<=sqrt(2)P sqrt(t L(0)),
    ||H^2(t)-H^2(0)||_F/sqrt(n)
      <=M sqrt(2t L(0))[A+P(a_0+sqrt(t L(0)))].
The two restrictions in (33) make the latter at most sqrt(kappa)/2.
Consequently the least singular value of H^2(t)/sqrt(n) is at least
sqrt(kappa)/2, and L(t)<=L(0)exp(-kappa t). Together with (45) and n>=N_*,
this gives the actual margin L(tau)<=2exp(-kappa*tau/2)<2. Neither a
zero readout nor a mere negative initial loss derivative is substituted.

For completeness, the initialization estimates in (38)--(46) check as follows.
- Both frozen corner probabilities m_s,m_o are positive for |rho|<1.
  Each count has variance n m(1-m); squared-deviation Markov bounds give (39).
- Conditional on the first layer, independent second rows have Gaussian
  covariance G=H^T H/n. On E_F, write Z=U+sqrt(gamma)xi with independent
  coordinates in xi and covariance G-gamma I for U. Conditional on U,
  phi_2(Z)'s coordinates are independent. The independent-copy identity
  and |phi_2(t)-phi_2(t')|>=|t-t'| give each conditional variance >=gamma.
  Thus E[VV^T]>=gamma I, including negative input correlations.
- Gaussian fourth moments imply E[V_a^2 V_b^2]<=3M^4A^4.
  Summing the four entry variances gives 12M^4A^4/n. Markov at Frobenius
  threshold gamma/2 gives exactly 48M^4A^4/(n gamma^2).
- Two deterministic 1/4-nets, each of cardinality <=9^n, give
  ||A_0||<=2 max|u^T A_0v|. Each bilinear form is N(0,1/n);
  its tail at 4 is <=2exp(-8n). This verifies (42).
- b_0^2=n^-3 sum_j xi_j^2; the Gaussian square moment at exponent 1/4
  gives P(b_0>2/n)<=exp[-(1-(log 2)/2)n], as in (43).
- On the norm events, ||f(0)||<=sqrt(2)q_0/n. The two nontrivial terms
  in N_* respectively ensure L(0)<=4 and L(0)<=2exp(kappa*tau/2).

Let E be precisely
    E_F intersect {K_3(0)>=kappa I}
        intersect {||A_0||_op<=8} intersect {b_0<=2/n}.
The conditional Gram failure is integrated only over E_F; union bounds
give P(E)>=max(0,1-p_n). No independence of overlapping events is used.

On E, n>=2 gives b_0<=1, and L(0)<=4 gives
X(tau)<=2tau+(8/3)tau^(3/2)=X_pre. Also s(tau)<=s_*.
Substituting these deterministic bounds and c_* in the proved clock argument
gives exactly (47)--(48), in particular sup_t||W^2||_op<=U_* and
integral_0^infinity s b<=X_*. The root imports only justified conclusions.
All these constants are finite and independent of width and time at fixed
activation and rho; the input normalization removes dimension factors.

## 4. Integrated row controls and the infinite integral

Put v_i(t)=sum_a |c_a(t)q_(a,i)(t)| and V_i(T)=integral_0^T v_i(t)dt.
For every finite T, the Euclidean integral triangle inequality gives
    ||V(T)||/sqrt(n)
      <=integral_0^T sum_a |c_a| ||q_a||/sqrt(n)
      <=MU_* integral_0^T (sum_a |c_a|) b
      <=2sqrt(2)MU_* integral_0^T s b <=V_*.
Here ||q_a||<=M||W^2||_op||W^3|| and sum_a|c_a|<=2sqrt(2)s.
Thus the stated factor V_*=2sqrt(2)MU_*X_* is correct.

Each V_i(T) increases to V_i. Monotone convergence of their nonnegative
squares (or the finite sum directly) yields sum_i V_i^2/n<=V_*^2.
Every V_i is finite for each fixed finite n. There is no cancellation,
exchange with a width limit, independence assumption, or unproved
coordinatewise bound uniform in n.

## 5. Protected strip, first exit, and separate sample counts

For i in S_a, put K_i=G_b-rho G_a, so |K_i|>=3R.
Initially |z_a|<=R/2 and |z_b|>=3R-|rho|R/2>R.
Before the first exit from {|z_a|<R, |z_b|>R}, p(z_b)=0 and the exact ODE gives
    z_b-rho z_a=K_i,  dot z_a=p(z_a)c_a q_(a,i).
Since p(±R)=0 and ||p'||_infty=L_1,
    0<=p(x)<=L_1(R-|x|) for |x|<R.
The absolutely continuous distance D=R-|z_a| satisfies almost everywhere
    D'>=-L_1|c_a q_(a,i)|D.
An integrating factor, valid also across zeros of z_a, yields
    D(t)>=(R/2)exp(-L_1 V_i)>0,
    |z_b(t)|>=3R-|rho|R>2R.
At any finite first exit continuity preserves both strict margins,
contradicting exit. They therefore hold at every finite t with the same
time-independent margins, also ruling out approach to saturation at infinity.

The fraction of ALL rows with V_i>B_*=2V_*/sqrt(m_rho) is at most m_rho/4.
For EACH a separately, if |S_a|/n>=m_rho/2, subtracting this same worst-case
bound gives |I_a|/n>=m_rho/4 for I_a=S_a intersect {V_i<=B_*}.
No sharing of a count budget between samples is assumed. These are fixed,
possibly future-dependent subsets, as the root expressly allows.
Their distance is >=delta_*=(R/2)exp(-L_1 B_*), so compactness inside (-R,R)
gives p_*>0 and the claimed uniform lower bound (m_rho/4)p_*^2.

## 6. Probability, counterexample, and exact scope

Each first-row Gaussian pair has covariance C. For either ordered pair,
G_a and G_b-rho G_a have zero covariance and variances 1 and 1-rho^2;
their joint Gaussian law makes them independent. Thus P(i in S_a)=m_rho
exactly as in root (4). Rows are independent. Squared-deviation Markov
and a union bound give strip-count failure <=8(1-m_rho)/(n m_rho).
Writing E_S={both strip counts >=n m_rho/2}, the proved event is E intersect E_S:
    P(E intersect E_S)>=max(0,1-p_n-8(1-m_rho)/(n m_rho)).
Dependence between E, the counts, and trajectory controls is harmless.
This bound can be zero at small allowed widths; it tends to one for fixed
activation and interior rho. No further width threshold is silently needed.

Counterexample to deleting E_S: choose any even n>=N_*. Since the inputs
are linearly independent, first weights can realize n/2 row pairs (2R,2R)
and n/2 pairs (2R,-2R). Every first row is then frozen forever, so all first
gates are zero. Yet N_s=N_o=n/2 satisfies E_F. Choose W^2(0)=I_n and every
W^3_j(0)=1/n. Then ||W^2(0)||_op=1<8, b_0=1/n<2/n, and oddness gives
    K_3(0)=phi_2(A)^2 I_2 > kappa I_2,
because kappa=A^2 min(m_s,m_o)/2<=A^2/4 and phi_2(A)>=A.
All event inequalities have strict margins. An open neighborhood preserves
them and keeps every initial first coordinate strictly saturated.
The prescribed independent Gaussian initialization has positive density
there, so this is a positive-probability counterexample on E itself,
not a change of initialization law or merely a measure-zero configuration.
Here E_S fails. It does not contradict the root's stated theorem.

Required fixes: none for the theorem with its stated augmented event.
Any assertion of permanent unsaturated mass on E alone must retain the
strip-count qualification or otherwise change its hypotheses.
Optional clarification: name E intersect E_S explicitly as the final
successful event to prevent that stronger, false reading.

Final scope verdict: actual finite GF, both samples simultaneously, fixed
individual subsets, all t>=0, on the stated augmented event. No conclusion
about nonzero force, motion, reverse-weighted kernels, nonlazy behavior,
mean-field limits, or top-layer nonaffinity follows from gate positivity.


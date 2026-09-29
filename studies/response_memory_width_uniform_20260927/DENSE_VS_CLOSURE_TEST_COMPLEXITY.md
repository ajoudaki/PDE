# Dense width convergence and compression of the evolving state

28 September 2026. A theoretical consequence of the current study's all-time
test theorem, not a new width-rate theorem. No experiments or manuscript
changes. The baseline is the same canonical dense network, and the reference
is its unique dense population predictor. Fixed initialized matrices are
excluded from both learned-state counts, as requested.

## 1. One target, one error, and the unchanged regime

Fix input dimension d, hidden depth L>=2, training sample count m, canonical
Gaussian tanh initialization, exactly zero readout, a positive limiting
initial readout-feature Gram gap, and one fixed sufficiently small positive
label RMS Y. Let mu be a fixed test law with finite second input moment. Use

\[
 \mathcal E(g,f)=\left[\int\sup_{t\ge0}|g(t,x)-f(t,x)|^2\,\mu(dx)\right]^{1/2}.
 \tag{1}
\]

Every assertion below also holds for the all-time input supremum over any
fixed bounded domain, with its corresponding constants. Neither norm is
restricted to training points. Constants can depend on the fixed data,
depth, Gram gap, label regime and test law, but not elapsed time or width.

Let D_n be (1) between the finite dense network and its dense population
predictor. Let H_n(q) be the same error for the actual finite autonomous
old-clock closure of order q. POPULATION_TEST_ERROR.md proves

\[
 D_n\xrightarrow{\Pr}0,
 \qquad
 H_n(q)\le C\omega(q)+\beta_n,\qquad
 \omega(q)=q^{-1}e^{K\sqrt{\log(e+q)}},\quad
 \beta_n\xrightarrow{\Pr}0,
 \tag{2}
\]

on common events G_n with probability tending to one, simultaneously for
all integer q>=1, with C>0 and K>=0. The remainder beta_n includes dense prediction sampling
error and a dense-carrier empirical-transfer remainder. It is independent
of q but is not known to be comparable to D_n. Its definition in the source
is Psi_mu(b_n)+D_n, so it dominates D_n on G_n. No numerical width rate has
been established for either D_n or beta_n. Rare events outside G_n are
included in each probability assertion; no all-width almost-sure event or
unconditional expectation estimate is asserted.

## 2. Why the dense comparison is genuinely all-time

Let D_n(T) denote (1) with time restricted to [0,T]. The fixed-horizon
dense limit gives D_n(T)->0 in probability for every fixed T. The dense
finite and population trajectories obey common residual decay and hence

\[
 \int_T^\infty\|\dot\theta_D(s)\|\,ds\le C e^{-\lambda T}.
\]

The forward difference estimate bounds prediction motion at x by C||x||
times parameter motion (with the fixed 1/sqrt(d) factor absorbed). Therefore
the finite second input moment gives, on G_n,

\[
 D_n\le D_n(T)+C_\mu e^{-\lambda T}.
 \tag{3}
\]

For any epsilon>0 first choose T so the second term is below epsilon/2.
Then take width large so D_n(T)<=epsilon/2 with probability tending to one.
This proves the first assertion in (2), including the fitted endpoint.
Equivalently, for each epsilon,delta>0 there is a finite N such that
sup_(n>=N) Pr{D_n>epsilon}<delta. The argument supplies no explicit
threshold N(epsilon,delta).

The source SMALL_LABEL_GAUSSIAN.md, Section 4, explicitly obtains the
finite-width passage by fixing a reference program before taking width
large; it supplies no quantitative width threshold. Neurons share reused,
trained matrices, so interpreting n as sampling resolution does not supply
an independence or central-limit theorem for trained predictions.

Even a hypothetical finite-time certificate C exp(aT)n^-b would yield only
n^[-b lambda/(a+lambda)] through (3), by choosing
T=b log(n)/(a+lambda). An all-time root-n claim needs stronger quantitative
control; it does not follow by suppressing a time-dependent constant.

## 3. A proved subquadratic learned-state approximation

The canonical dense implementation retains

\[
 S_D(n)=(L-1)n^2+n(d+1)
 \tag{4}
\]

evolving weight coordinates. An implementation of the original closure
needs its first matrix and readout, two sets of q length-n moments for each
sample and hidden link, and the shared clock:

\[
 S_H(n,q)=2(L-1)mnq+n(d+1)+O(1).
 \tag{5}
\]

Transient forward/backward workspace O(Lmn) does not change the comparison.
The initial dense matrix actions are excluded on purpose; (4)--(5) count
the persistent evolving representation, not total storage or arithmetic.

For every deterministic order sequence satisfying q_n->infinity and
q_n=o(n/m), equations (2), (4), (5) give

\[
 H_n(q_n)\xrightarrow{\Pr}0,
 \qquad \frac{S_H(n,q_n)}{S_D(n)}\longrightarrow0.
 \tag{6}
\]

For fixed m,d,L, both log(n) and log log(n) orders give a near-linear
number of evolving coordinates and converge in the same all-time test
norm as the quadratic-state dense sequence. More generally q_n=n^a,
0<a<1, gives S_H=O(Lm n^(1+a)) and the certificate
H_n<=n^(-a+o(1))+beta_n. It does not assign a rate to beta_n.

This proves approximation of the same population predictor with a smaller
evolving state along the same width sequence. It needs no unique fixed-q
population closure: the joint n,q_n limit is the unique dense predictor
directly by (2).

There is also a same-tolerance existence statement. Fix epsilon,delta>0
and any desired learned-state compression factor R. First choose a fixed
q so C omega(q)<=epsilon/2. Next choose n large enough that
Pr(G_n^c)+Pr{beta_n>epsilon/2}<=delta and S_H(n,q)<=S_D(n)/R. On the
remaining event both predictors have test error at most epsilon. This is
valid even for arbitrarily large R, because n may be increased after q.
It does not compare the minimum sufficient widths for the two methods.

## 4. What matched accuracy would additionally require

The assertion H_n(q_n)->0 does not imply H_n(q_n)=O_p(D_n), nor that the
closure reaches epsilon using fewer learned coordinates than the narrowest
dense network reaching epsilon. For example, a possible dense error
n^-1/2 and a closure order term (log n)^-1+o(1) both tend to zero but have
very different scales. Unknown beta_n is a second obstacle: improving the
dense prediction rate alone need not quantify dense carrier tails.

A sufficient condition for matching certified rates is a deterministic
envelope r_n for both relevant errors, with D_n=O_p(r_n) and beta_n=O_p(r_n). Choosing q
with omega(q)=O(r_n) then gives H_n(q)=O_p(r_n). These are matching upper
certificates; they are not lower bounds or a proof of optimal resource use.

There is a precise criterion for this certificate to permit sublinear order:
for a deterministic r_n->0, a schedule q_n=o(n) with
omega(q_n)=O(r_n) exists if and only if

\[
 r_n/\omega(n)\longrightarrow\infty.
 \tag{6a}
\]

For necessity put v_n=log(n/q_n)->infinity. Since omega(q_n)->0 also
forces q_n->infinity, the identity obtained by rationalizing the two square
roots gives log(omega(q_n)/omega(n))=v_n(1-o(1))->infinity. Thus r_n
must dominate omega(n) by an unbounded factor. For sufficiency omega is
eventually decreasing, and omega(cn)/omega(n)->1/c for every fixed c>0.
Choose the smallest sufficiently large integer q with omega(q)<=r_n.
It tends to infinity; (6a) implies it is eventually no larger than cn for
every c>0, which proves q_n=o(n). This concerns matching upper certificates,
not actual-error ratios or minimum necessary memory.

For illustration, suppose the additional quantitative result is

\[
 D_n=O_p(n^{-a}),\qquad\beta_n=O_p(n^{-a}),\qquad a>0.
 \tag{7}
\]

For q large put z=log(q). Then
log(omega(q))=-z+K sqrt(z)+o(1). Solving
z-K sqrt(z)=a log(n) gives

\[
 z=a\log n+K\sqrt{a\log n}+O(1),\qquad
 q=n^a\exp\{K\sqrt{a\log n}+O(1)\}=n^{a+o(1)}.
 \tag{8}
\]

The bounded term can be enlarged to make the certificate sufficient.
Both methods then have error O_p(n^-a), while

\[
 S_D=\Theta(Ln^2),\qquad
 S_H=O(Lm n^{1+a+o(1)}+nd),\qquad
 \frac{S_H}{S_D}=O(m n^{a-1+o(1)}+d/n).
 \tag{9}
\]

For fixed m,d and 0<a<1 this proves a saving at the same certified rate,
conditional on (7). At a=1, the displayed order certificate generally
needs at least linear order and gives no asymptotic saving; a>1 is worse.
Failure of this certificate to save memory is not an algorithmic lower bound.

At fixed confidence, choosing n proportional to epsilon^(-1/a) in (7)
and q=epsilon^[-1+o(1)] gives sufficient learned-state costs

\[
 S_D=O(L\epsilon^{-2/a}),\qquad
 S_H=O(Lm\epsilon^{-(1+1/a)+o(1)}+d\epsilon^{-1/a}).
 \tag{10}
\]

In the root-n benchmark a=1/2 this is n^(3/2+o(1)) versus n^2 at the
same width, or epsilon^(-3+o(1)) versus epsilon^-4 at matched certified
test accuracy. Root-n behavior for (7) is an unproved benchmark here,
not a theorem imported from a different architecture or fixed-time limit.

## 5. Status and scientific inputs

The unconditional new conclusion is (6), plus the explicitly nonoptimal
same-tolerance existence statement. Equation (3) records why the dense
baseline has the same all-time convergence property. Equations (8)--(10)
are conditional algebra, exposing the two numerical width bounds still
needed for a quantitative comparison. They do not establish a width rate.

Inputs: the complete POPULATION_TEST_ERROR.md and the fixed-program
width-passage paragraph in Section 4 of SMALL_LABEL_GAUSSIAN.md, previously
read in full in this investigation. A scoped prompt-only checker independently
examined the complexity and quantifier implications of (2), without scientific
retrieval. No other study, external source, experiment or Git mutation was used.
Final check scope and hash are recorded in the study README.

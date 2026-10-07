# A deterministic robust center from bounded expectation tests

2026-10-06. Prompt-derived transfer lemma and numerical wrapper. The
expectation evaluator is an explicit conditional input, not constructed
or assumed to be small-space by this note.

A whole-function dense-versus-dense probability bound supplies one event
for the reference initialization on which every pointwise median is close
simultaneously at every query and time. An approximating program need not
define a jointly coupled random function: uniformly accurate pointwise
couplings suffice. A deterministic bisection of bounded smooth expectation
tests constructs an equally robust center, without moments of bad-event
outputs, CDF slope assumptions, or a query net.

## 1. The reference event is a whole-function event

Let $\mathcal Z$ be an arbitrary index set; in the application it is
$[0,\infty]\times S^{d-1}$, with the fitted endpoint included. Let
$f_G:\mathcal Z\to\mathbb R$ be a random dense-model function and
$G'$ an independent initialization with the same law. Write

\[
 \|f_G-f_{G'}\|_*
    =\sup_{z\in\mathcal Z}|f_G(z)-f_{G'}(z)|.
\]

Assume the displayed events and conditional probabilities are measurable,
and suppose

\[
 \Pr_{G,G'}\{\|f_G-f_{G'}\|_*>b\}\le\eta,
 \qquad b\ge0.                                                \tag{1}
\]

For any $0<\alpha<1$, define

\[
 q(G)=\Pr_{G'}\{\|f_G-f_{G'}\|_*>b\},\qquad
 \mathcal E_\alpha=\{G:q(G)\le\alpha\}.
\]

Fubini gives $\mathbb E_Gq(G)\le\eta$. Markov's inequality gives

\[
 \Pr_G(\mathcal E_\alpha)\ge1-\eta/\alpha.
 \tag{2}
\]

For every single reference $G\in\mathcal E_\alpha$, the independent
dense law assigns probability at least $1-\alpha$ to functions lying
within $b$ of that reference at **all** indices simultaneously. The event
$\mathcal E_\alpha$ does not depend on a selected query or time.

This is a probability statement, not an algorithm for recognizing the
reference good event. If (1) is obtained by proving the bound only on a
good pair event of probability at least $1-\eta$, its entire complement
is already included in (1). No conditional good-event probability may be
silently substituted for that unconditional premise.
If a target endpoint is defined only on the inherited good event, one may
give the target an arbitrary measurable extension off that event for this
probability argument, counting its complement in $\eta$. This is not an
instruction for the decoder to recognize that event.

## 2. Pointwise program laws suffice

For each $z\in\mathcal Z$, let $\mu_z$ be the law of a real scalar
program output $X_z$. There is no assumed joint random field
$(X_z)_{z\in\mathcal Z}$. Assume that for every $z$ there is a
coupling of $X_z$ with an independent dense copy $f_{G'}$ having the
correct full dense marginal law, such that

\[
 \Pr\{|X_z-f_{G'}(z)|>\varepsilon\}\le\rho.
 \tag{3}
\]

The constants $\varepsilon\ge0$ and $\rho\ge0$ are uniform in
$z$, but the coupling and program randomness may vary with $z$.
An everywhere-defined program law is required. Its values outside its
accuracy event may be arbitrarily large; no integrability assumption is
made on them.

Fix $G\in\mathcal E_\alpha$ and an arbitrary $z$. Under any coupling
in (3), the dense marginal assigns probability at least $1-\alpha$ to
$\|f_{G'}-f_G\|_*\le b$. Intersecting that event with the success
event in (3) costs at most $\alpha+\rho$. Hence, writing
$r=b+\varepsilon$ and $\beta=\alpha+\rho$,

\[
 \mu_z([f_G(z)-r,f_G(z)+r])\ge1-\beta
 \quad\hbox{for every }z\in\mathcal Z.
 \tag{4}
\]

There is no union bound over $z$: after fixing the reference in the single
event $\mathcal E_\alpha$, this deterministic inequality holds for an
arbitrary index. No selection of a simultaneous coupling is needed.
In particular the reference failure bound in (2) does not become
$(\eta+\rho)/\alpha$.

If a jointly defined numerical training program satisfies the stronger
uniform approximation event
$\Pr\{\|g_{G'}-f_{G'}\|_*\le\varepsilon\}\ge1-\rho$,
then its marginal laws satisfy (3). The pointwise version also permits
recreating a finite-width noisy Gaussian program separately for each
query. It does not replace that law with a limiting population law.

### Exact medians

Assume $\beta<1/2$. A median $m$ of a real law means
$\Pr(X\le m)\ge1/2$ and $\Pr(X\ge m)\ge1/2$. Every real
probability law has a median, for example its lower half-quantile.
Equation (4) forces every such median to lie in
$[f_G(z)-r,f_G(z)+r]$: outside either endpoint, one of the two required
half-probabilities is at most $\beta<1/2$.

Consequently any deterministic pointwise choice $m(z)$ of medians obeys

\[
 \sup_{z\in\mathcal Z}|m(z)-f_G(z)|\le b+\varepsilon
 \quad(G\in\mathcal E_\alpha).
 \tag{5}
\]

Taking $\alpha=1/4$ gives reference success at least $1-4\eta$.
For the exact dense marginal law, $\rho=\varepsilon=0$, so (5)
is the proposed whole-function median transfer. Atoms and nonunique
medians do not alter it.

## 3. Bounded smooth tests and approximate center selection

Exact median computation is unnecessary. Fix a nondecreasing smooth
transition $\psi:\mathbb R\to[0,1]$ with
$\psi(u)=0$ for $u\le-1$ and $\psi(u)=1$ for $u\ge1$.
For a transition width $\tau>0$, define the smoothed CDF

\[
 H_z(s)=\mathbb E_{X\sim\mu_z}
              \psi\!\left(\frac{s-X}{\tau}\right).
 \tag{6}
\]

This expectation always exists: its integrand is bounded even when
$X$ has no first moment. For every $G\in\mathcal E_\alpha$, (4)
implies the two threshold tests

\[
 \begin{array}{ll}
 s\le f_G(z)-r-\tau &\Longrightarrow H_z(s)\le\beta,\\
 s\ge f_G(z)+r+\tau &\Longrightarrow H_z(s)\ge1-\beta.
 \end{array}
 \tag{7}
\]

Only these inequalities, not a density or positive derivative of $H_z$,
will be needed.

Suppose an effective range certificate gives
$\|f_G\|_*\le B$ on a reference event $\mathcal B$.
If $\Pr(\mathcal B^c)\le\eta_B$, the final reference success
probability below is at least $1-\eta/\alpha-\eta_B$.
If the original good-pair certificate already includes reference-range
failure, that probability can instead be accounted for there; it must not
be counted as an unmentioned assumption. This range certificate is only
for the reference, not the program's bad outputs.

Explicitly, if the premise is
$\Pr\{G\in\mathcal B,\ \|f_G-f_{G'}\|_*\le b\}\ge1-\eta$,
replace $q(G)$ by one on $\mathcal B^c$ and leave it unchanged on
$\mathcal B$. Its expectation is still at most $\eta$, and the event
where it is at most $\alpha<1$ is contained in
$\mathcal E_\alpha\cap\mathcal B$. Then the reference success
bound is directly $1-\eta/\alpha$, with no additional range-failure
term. A good-pair certificate including both physical good events has
exactly this implication.

Choose a rational $M\ge B+r+\tau$, a final bracket tolerance
$\delta>0$, and an expectation error $\nu$ satisfying

\[
 \beta<\frac12,\qquad 0<\nu<\frac12-\beta.
 \tag{8}
\]

The conditional evaluator assumption is precise: for every input index
$z$ and rational threshold $s$ encountered below, a deterministic,
repeatable algorithm returns a rational $\widehat H_z(s)$ with

\[
 |\widehat H_z(s)-H_z(s)|\le\nu.
 \tag{9}
\]

Its retained data, Gaussian-law description, input precision and complete
live workspace all belong to that algorithm's separate complexity count.
Neither a small-space implementation of (9) nor an integration oracle
is asserted here.

The center algorithm initializes $l=-M$, $u=M$ and performs

\[
 N=\max\{0,\lceil\log_2(2M/\delta)\rceil\}
\]

bisections. At each step put $s=(l+u)/2$. If
$\widehat H_z(s)<1/2$, replace $l$ by $s$; otherwise replace $u$
by $s$. Equality follows the latter fixed rule. Return
$D(z)=(l+u)/2$.

For every reference in $\mathcal E_\alpha\cap\mathcal B$,
the starting bracket satisfies
$H_z(l)\le\beta$ and $H_z(u)\ge1-\beta$. Every iteration
preserves

\[
 H_z(l)\le\tfrac12+\nu,
 \qquad H_z(u)\ge\tfrac12-\nu.
 \tag{10}
\]

Indeed the lower-endpoint update follows from
$H_z(s)\le\widehat H_z(s)+\nu<1/2+\nu$, and the
upper-endpoint update follows from the reverse inequality. Because
$1-\beta>1/2+\nu$ and $\beta<1/2-\nu$, (7)–(10) imply

\[
 l<f_G(z)+r+\tau,
 \qquad u>f_G(z)-r-\tau.
\]

At termination $u-l\le\delta$, so their midpoint satisfies

\[
 \boxed{\quad
 \sup_{z\in\mathcal Z}|D(z)-f_G(z)|
       \le b+\varepsilon+\tau+\delta/2
 \quad(G\in\mathcal E_\alpha\cap\mathcal B).
 \quad}                                                       \tag{11}
\]

This proof permits atoms, CDF plateaus at height $1/2$, and either
bisection decision when the approximate test is close to $1/2$.
It does not invert a CDF slope. The algorithm is defined even outside
the reference event; only its error guarantee is conditional on that
event. It never tests membership in the event.
Without a CDF slope assumption, constant expectation error need not give
a small horizontal error relative to a particular exact median. The
proved conclusion is the robust-center bound (11), which is what the
dense comparison requires.

For a convenient fixed choice, take $\alpha=1/4$ and $\rho\le1/8$.
Then $\beta\le3/8$, and $\nu=1/16$ satisfies (8). Thus a constant
absolute expectation accuracy suffices, even when the desired spatial
error $\tau+\delta/2$ tends to zero. Setting both $\tau$ and
$\delta$ to at most $n^{-a}$ adds only $3n^{-a}/2$ to the dense
comparison radius and program error.

## 4. An explicit smooth test and the wrapper's information count

For any integer $k\ge2$, an explicit $C^k$ transition is

\[
 \psi_k(u)=
 \begin{cases}
 0,&u\le-1,\\
 \displaystyle
 \frac{\int_{-1}^u(1-v^2)^k\,dv}
      {\int_{-1}^1(1-v^2)^k\,dv},&-1<u<1,\\
 1,&u\ge1.
 \end{cases}
 \tag{12}
\]

The derivative of the middle polynomial is nonnegative and vanishes to
order $k$ at both endpoints, proving the claimed matching and monotonicity.
Its coefficients and normalization are rational with bit length
polynomial in $k$. Expanding the polynomial shows that for $j\le k$
its derivative bounds have logarithm $O(k\log(k+2))$. Scaling by
$\tau$ adds $j\log(\tau^{-1})$ to those logarithmic bounds when
$\tau\le1$. Thus the smoothing step exposes its precision and
derivative scales; it does not presume they are harmless for an arbitrary
underlying expectation evaluator. If that evaluator requires derivatives
through order $q+2$, choose $k\ge q+2$.

With rational $M$, the bisection endpoints and midpoint are exact dyadic
refinements of that rational. If its numerator and denominator have total
bit length $p_M$, their descriptions need $O(p_M+N)$ bits. Besides
the expectation evaluator, the wrapper retains only these endpoints,
one threshold, an iteration counter, the fixed smoothing description and
the supplied precision/range parameters. It makes $N$ sequential calls
to (9) and reuses its workspace.

Therefore, if a counted evaluator for (9) uses peak space $S$, the
wrapper adds only a polynomial amount in
$p_M+k+\log(\tau^{-1})+\log(\delta^{-1})+\log(\nu^{-1})$.
This is an additive wrapper bound, not a proof that $S$ is polylogarithmic.
In particular, a dense random-access initialization interface cannot be
hidden inside $S$ or treated as free input.

The law $\mu_z$ and evaluator are deterministic specifications. Every
query invokes the same bisection rule and a repeatable expectation
algorithm, so $D$ is one consistent deterministic function. Independent
fresh random approximations to (9), with merely per-query success
probabilities, would not imply (11); they are not allowed by the stated
oracle contract. By contrast, the program randomness defining $\mu_z$
need not be jointly realized across queries, because it is integrated out
before the deterministic answer is returned.

## 5. Failure events, eventual bounds and claim boundary

Only bounded test expectations are used. Program failures contribute at
most their probability $\rho$ to the threshold inequalities, regardless
of how large their outputs become. No mean of $X_z$ is taken, so an
opaque good-event complement causes no unbounded expectation bias.
The construction does not need to detect, condition on, or discard that
complement.

If the inherited statements provide only $\eta_n\to0$ and
$\rho_n\to0$ with an unquantified eventual width, choose the fixed
constants above and invoke $\rho_n\le1/8$ only at sufficiently large
width. The result then has the same noneffective eventual qualification;
it does not create an algorithm for finding that threshold. A rational
range bound $M$ and all effective interfaces still have to be supplied
or counted. At fixed problem parameters, such bounds may be hardcoded
when their existence has been certified.

The whole-index norm includes every physical time, unseen sphere point
and the endpoint if those indices are included in (1) and the uniform
pointwise coupling assumption (3). No extra net, joint noisy-program
coupling, or moment hypothesis is introduced to obtain (11).

What is proved: robust-center transfer; its pointwise-coupling variation;
and a deterministic smooth-test bisection wrapper with a counted additive
space overhead. What remains separate: constructing the finite-width
program laws and their couplings, implementing their exact bounded test
expectations in the required total space, and counting every Gaussian
root description and coefficient. This note does not establish a limiting
population representation, autonomous compact training, or the requested
full compression theorem.

## 6. Provenance

This is a bounded continuation from the supervisor's prompt, including
the explicitly suggested pointwise-coupling improvement. The probability,
median, smoothing and bisection proofs above were reconstructed directly.
No new scientific source, external reference, experiment, other route's
file or prior study was consulted for this lemma. The existing notation
and rigorous-proof instructions were applied; the previously reported
inaccessible custom notation skill was not searched for again.

The separate version check requested in the same assignment was appended
only to `SHORT_CAUSAL_TRAINING_PROGRAM_CHECK.md`. That check concerns
candidate SHA-256
`0fbffab2a0782cb34987f49c944491fb50f920c4c4acbd888548947131be35a5`
and is not an input to the abstract transfer proof. No candidate or
maintained file, and no Git index entry, was changed.

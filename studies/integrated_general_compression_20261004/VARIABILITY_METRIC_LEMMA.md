# A pairwise-variability benchmark from scalar couplings

This is a self-contained, internally derived lemma for the assigned study. Its
inputs are the random-function laws, scalar coupling bounds, and extension
events specified below. It does not assume a known population curve, an upper
rate for that curve, or a coupling of the complete decoder and target functions.

## Statement with exact probability budgets

Let \(T\) be an index set, and let \(F,F'\) be independent random real-valued
functions with the same law. Write

\[
 \|f-g\|_\infty=\sup_{t\in T}|f(t)-g(t)|,
 \qquad
 D=\|F-F'\|_\infty.
\]

Assume the evaluations and suprema used below are measurable, including the
joint map needed to integrate distances between two independent functions.
For \(0\leq\eta<1\), define the deterministic quantile

\[
 b_\eta=\inf\{r\geq0:\mathbb P(D\leq r)\geq1-\eta\}.
\]

Assume \(b_\eta<\infty\). Right-continuity of the distribution function gives
\(\mathbb P(D>b_\eta)\leq\eta\). The same proof applies to any finite radius
with this property, whether or not it is the smallest such radius.

Let \(Z\subset T\) be a deterministic finite coding net with
\(|Z|=N\geq1\). Let \(G_1,\ldots,G_s\) be independent complete random functions
with the same law, where \(s\) is a positive odd integer. At each fixed
\(z\in Z\), assume that there exists a scalar coupling \((X_z,Y_z)\) such that

\[
 X_z\stackrel{d}=G_1(z),\qquad
 Y_z\stackrel{d}=F(z),\qquad
 \mathbb P(|X_z-Y_z|>e_{\mathrm{cpl}})\leq p,
\]

where \(e_{\mathrm{cpl}}\geq0\) and \(p\geq0\). These couplings may depend on
\(z\); no compatibility among them is assumed. Define the pointwise median
function by

\[
 G(t)=\operatorname{med}\{G_1(t),\ldots,G_s(t)\}.
\]

Let \(F_{\mathrm{tar}}\) be an independent copy of \(F\), independent of the
decoder members. Let \(\widehat G\) denote the implemented decoder output; it
may equal \(G\). To make the passage outside the net explicit, assume that an
event \(\mathcal E\) satisfies \(\mathbb P(\mathcal E^c)\leq\rho\), and that on
this event

\[
 \|\widehat G-F_{\mathrm{tar}}\|_\infty
 \leq
 \max_{z\in Z}|G(z)-F_{\mathrm{tar}}(z)|+e_{\mathrm{ext}}.       \tag{1}
\]

Here \(e_{\mathrm{ext}}\geq0\) is the sum of the interpolation, tail, and
execution errors required for this implication. No independence of
\(\mathcal E\) from the functions is required.

Set \(q=\eta+p\), and suppose \(q<1/2\). Define the exact binomial tail

\[
 B_s(q)=\sum_{k=(s+1)/2}^{s}\binom{s}{k}q^k(1-q)^{s-k}.
\]

Then

\[
 \mathbb P\!\left(
   \|\widehat G-F_{\mathrm{tar}}\|_\infty
      >2b_\eta+e_{\mathrm{cpl}}+e_{\mathrm{ext}}
 \right)
 \leq\eta+\rho+N B_s(q).                                    \tag{2}
\]

For \(0<q<1/2\), define

\[
 I(q)=-\tfrac12\log\bigl(4q(1-q)\bigr).
\]

The elementary estimates proved below yield

\[
 N B_s(q)\leq N e^{-sI(q)}
       \leq N\exp\!\left[-2s(1/2-q)^2\right].                 \tag{3}
\]

For a specified total failure probability \(\delta\) with
\(\eta+\rho<\delta<1\), it therefore suffices to choose the smallest positive
odd integer satisfying

\[
 s\geq \frac{\log\!\bigl(N/(\delta-\eta-\rho)\bigr)}{I(q)}.
                                                                    \tag{4}
\]

Replacing \(I(q)\) by \(2(1/2-q)^2\) is a simpler sufficient choice.
When \(q=0\), the median term in (2) is zero and \(s=1\) suffices.

For example, the completely explicit allocation

\[
 \eta\leq\min\{\delta/3,1/8\},\qquad
 \rho\leq\delta/3,\qquad p\leq1/8,\qquad
 s\geq8\log(3N/\delta),\quad s\text{ odd},                    \tag{5}
\]

gives failure at most \(\delta\). Thus a fixed majority margin requires
\(s=O(\log(N/\delta))\) complete members. If
\(e_{\mathrm{cpl}}\leq e\) and the *total* extension error
\(e_{\mathrm{ext}}\leq e\), the error bound is \(2b_\eta+2e\).
If instead three separate extension defects are each at most \(e\), their
sum is at most \(3e\), and the corresponding bound is \(2b_\eta+4e\).
The number of defects must be counted; “each defect is at most \(e\)” does
not mean their sum is at most \(e\).

## Proof

The argument first extracts an analysis-only center from the pairwise law,
then transfers its scalar concentration to each decoder coordinate, and
finally amplifies those coordinate probabilities using the complete
independent members.

For a deterministic function \(f\) in the function space, define

\[
 a(f)=\mathbb P(\|F-f\|_\infty>b_\eta).
\]

Independence and integration with respect to the common function law give

\[
 \mathbb E[a(F')]=\mathbb P(\|F-F'\|_\infty>b_\eta)\leq\eta.
                                                                    \tag{6}
\]

There consequently exists a deterministic function \(f_*\), selectable
among realizations of that law, with \(a(f_*)\leq\eta\). Indeed, if
\(a(f)>\eta\) almost surely, its integral would be strictly larger than
\(\eta\). The strict inequality for the integral follows, for example,
because the sets \(\{a(f)-\eta\geq1/n\}\), over positive integers \(n\),
cover a set of probability one, and at least one has positive probability.
Hence

\[
 \mathbb P(\|F-f_*\|_\infty\leq b_\eta)\geq1-\eta.           \tag{7}
\]

This center need not be known, computed, or stored by the decoder. It is not
an assumed population curve or a replacement for the ordinary random target.
Because the center is fixed by an existence argument, there is no additional
random “bad center” event in this proof.

Fix one \(z\in Z\). In its scalar coupling, the triangle inequality gives

\[
 \{|X_z-f_*(z)|>b_\eta+e_{\mathrm{cpl}}\}
 \subseteq
 \{|X_z-Y_z|>e_{\mathrm{cpl}}\}
 \cup\{|Y_z-f_*(z)|>b_\eta\}.
\]

The second event has probability at most \(\eta\), because its marginal is
\(F(z)\), and a coordinate deviation is bounded by the supremum deviation
in (7). It follows that

\[
 \mathbb P\bigl(|G_i(z)-f_*(z)|>b_\eta+e_{\mathrm{cpl}}\bigr)
 \leq p+\eta=q.                                               \tag{8}
\]

This is a statement about the actual scalar marginal of every decoder
member. It does not use a joint coupling across coordinates.

For this fixed \(z\), the failure indicators in (8) are independent, since
the complete members are independent. If the median lies outside the
interval
\([f_*(z)-b_\eta-e_{\mathrm{cpl}},f_*(z)+b_\eta+e_{\mathrm{cpl}}]\),
at least \((s+1)/2\) of those indicators equal one. Their sum is therefore
bounded by the binomial tail \(B_s(q)\). One way to verify this comparison
is to represent independent Bernoulli indicators of probabilities
\(q_i\leq q\) as \(\mathbf 1_{\{U_i\leq q_i\}}\), with independent
uniform \(U_i\), and compare them pointwise to
\(\mathbf 1_{\{U_i\leq q\}}\).

For completeness, let \(K\) be this sum and take \(\lambda>0\). The
exponential version of the elementary Markov inequality and independence
give

\[
 \mathbb P(K\geq s/2)
 \leq e^{-\lambda s/2}\mathbb E[e^{\lambda K}]
 \leq\left[e^{-\lambda/2}(1-q+q e^\lambda)\right]^s.
\]

The choice \(e^\lambda=(1-q)/q\), valid for \(0<q<1/2\), turns the bracket
into \(2\sqrt{q(1-q)}\). Applying this calculation also when the
indicators have probability exactly \(q\) gives
\(B_s(q)\leq e^{-sI(q)}\). Finally,
\(4q(1-q)=1-(1-2q)^2\), and

\[
 -\log(1-u)=\int_0^u\frac{dv}{1-v}\geq u\quad(0\leq u<1)
\]

implies \(I(q)\geq(1-2q)^2/2=2(1/2-q)^2\), proving (3).

A union bound over the \(N\) net coordinates now gives, except on an event
of probability at most \(N B_s(q)\),

\[
 \max_{z\in Z}|G(z)-f_*(z)|\leq b_\eta+e_{\mathrm{cpl}}.
                                                                    \tag{9}
\]

Equation (7) gives a target event of failure probability at most \(\eta\)
on which \(\|F_{\mathrm{tar}}-f_*\|_\infty\leq b_\eta\). On the intersection
of these two good events,

\[
 \max_{z\in Z}|G(z)-F_{\mathrm{tar}}(z)|
 \leq2b_\eta+e_{\mathrm{cpl}}.
\]

Intersecting with \(\mathcal E\), applying (1), and adding the three failure
probabilities proves (2). Dependence among coordinates and dependence of
\(\mathcal E\) on any of these events do not affect this union bound.
In fact the deterministic-center proof needs only the target's marginal
law; the stated target independence is more than this proof requires.

## What an extension event must actually provide

For a typical full-domain construction, let \(\pi:T\to Z\) be a deterministic
net map. Suppose a common good event gives

\[
 \sup_{t\in T}|F_{\mathrm{tar}}(t)-F_{\mathrm{tar}}(\pi(t))|
      \leq e_{\mathrm{tar}},\qquad
 \max_{1\leq i\leq s}\sup_{t\in T}|G_i(t)-G_i(\pi(t))|
      \leq e_{\mathrm{mem}},\qquad
 \|\widehat G-G\|_\infty\leq e_{\mathrm{exec}}.
\]

Then (1) holds with
\(e_{\mathrm{ext}}=e_{\mathrm{tar}}+e_{\mathrm{mem}}+e_{\mathrm{exec}}\).
To see this, order statistics satisfy

\[
 |\operatorname{med}_i u_i-\operatorname{med}_i v_i|
 \leq\max_i|u_i-v_i|.
\]

Indeed, if the maximum is \(r\), at least \((s+1)/2\) of the \(u_i\) are
at most \(\operatorname{med}_i v_i+r\), and at least \((s+1)/2\) are at
least \(\operatorname{med}_i v_i-r\). The same inequalities hold for their
median. Apply this to \(u_i=G_i(t)\), \(v_i=G_i(\pi(t))\), and use the
triangle inequality. Other tail/interpolation constructions are permitted
if they prove (1) with their stated total defect and failure probability.

If member \(i\)'s required good event has failure probability at most
\(\rho_i\), the common event loses at most \(\sum_i\rho_i\), plus the target
and execution failure budgets. Independence of those good events is not
needed. Their probabilities must be included in \(\rho\); good events
cannot be silently assumed to occur for all \(s\) members.

The proof applies the scalar bound and independence *before* intersecting
with \(\mathcal E\). Conditioning on an arbitrary common event can destroy
independence. If the construction instead has a shared random environment,
it is enough that, conditional on that environment, the members are
independent and the scalar coupling bounds to the same marginal \(F(z)\)
hold uniformly on a good environment event; its failure probability must
then be added to the budget. A coupling only to an environment-dependent
target law needs its own conditional concentration argument.

## An alternative bound with coefficient one on the quantile

There is a useful tradeoff if a larger intrinsic failure budget is
acceptable. Fix a number \(\alpha\) with \(0<\alpha<1/2-p\).
Markov's inequality applied to (6) gives

\[
 \mathbb P\bigl(a(F_{\mathrm{tar}})>\alpha\bigr)\leq\eta/\alpha.
\]

Conditional on a target realization \(f\) with \(a(f)\leq\alpha\), its
independence from the decoder preserves the member laws and their
independence. The scalar coupling argument now centers each coordinate at
\(f(z)\), giving a member failure probability at most \(\alpha+p\) outside
radius \(b_\eta+e_{\mathrm{cpl}}\). The same median and extension argument
therefore proves

\[
 \mathbb P\!\left(
 \|\widehat G-F_{\mathrm{tar}}\|_\infty
      >b_\eta+e_{\mathrm{cpl}}+e_{\mathrm{ext}}
 \right)
 \leq \eta/\alpha+\rho+N B_s(\alpha+p).                       \tag{10}
\]

Here the “bad center” is the target itself, and its exact budget is
\(\eta/\alpha\). For instance, \(\alpha=1/4\), \(p\leq1/8\) gives failure
at most \(4\eta+\rho+N e^{-s/32}\). Equation (2) generally gives the more
economical intrinsic failure budget; (10) gives the smaller radius.

## Limitations and the independent realized denominator

The quantile \(b_\eta\) is deterministic. It is not an independently sampled
distance \(\|F_1-F_2\|_\infty\), and neither (2) nor (10) implies a
distribution-free bound by a constant times that realized distance.

For a decisive example, take \(T\) to be a singleton and let \(F\) equal
zero or one with equal probabilities. Take every decoder member to have
exactly this law, so \(p=e_{\mathrm{cpl}}=e_{\mathrm{ext}}=0\). For any odd
\(s\), its median is again a fair zero-or-one random variable. Let the target
and the two denominator samples be independent of each other and of the
decoder. The decoder differs from its target with probability \(1/2\), while
the denominator is zero with probability \(1/2\). Consequently, for every
finite constant \(C\),

\[
 \mathbb P\!\left(
 |G-F_{\mathrm{tar}}|>C|F_1-F_2|
 \right)\geq1/4.
\]

By contrast, \(b_\eta=1\) for every \(\eta<1/2\), and the error is always at
most one. The quantile benchmark is well behaved in this example.

The obstruction is not confined to zero denominators. Replace each atom by
a uniform interval of length \(\varepsilon\), using the equal mixture of
\([0,\varepsilon]\) and \([1,1+\varepsilon]\), with
\(0<\varepsilon<1/(C+1)\). The denominator is positive almost surely.
With probability \(1/2\) its two samples belong to the same interval, giving
distance at most \(\varepsilon\). Independently, with probability \(1/2\)
the median and target belong to different intervals, giving distance at
least \(1-\varepsilon>C\varepsilon\). The comparison again fails with
probability at least \(1/4\). A realized-denominator claim needs an
additional lower-tail or anti-concentration assumption for that denominator.

Other necessary qualifications are as follows.

- A fixed positive \(\eta\) cannot in general support arbitrarily small
  total failure probability. For \(0<\eta<1/2\), set
  \(r=(1-\sqrt{1-2\eta})/2\) and let \(F\) be a Bernoulli variable with
  success probability \(r\). Then \(b_\eta=0\), because
  \(\mathbb P(F\ne F')=2r(1-r)=\eta\). An output independent of the ordinary
  target has probability at least \(r\) of failing to match it exactly,
  regardless of the decoder sample count. Thus an intrinsic failure term
  of order \(\eta\) cannot be removed.
- A fixed positive majority margin \(1/2-\eta-p\) is a sufficient condition
  for the stated logarithmic repetition count. As the margin vanishes,
  the bound on \(s\) worsens. Without appropriate majority information,
  repetition need not amplify success; for example, \(F\equiv0\) and
  members equally likely to equal zero or a large constant have scalar
  failure probability \(p=1/2\), and every odd median fails with probability
  \(1/2\).
- Without (1), values outside \(Z\) are uncontrolled. A deterministic member
  can vanish on \(Z\) and have an arbitrarily large spike elsewhere, while
  \(F\equiv0\), \(b_\eta=p=e_{\mathrm{cpl}}=0\).
- Independence is needed across complete members, not across coordinates.
  Repeating one shared random member \(s\) times does not amplify anything.
  Also, taking a separate scalar majority construction that cannot be
  evaluated as one complete decoder is not what this lemma assumes.
- The case \(b_\eta=0\) is allowed. An infinite quantile gives no finite
  accuracy statement. An uncountable domain requires the stated
  measurability or an explicitly supplied outer-probability formulation.

The conclusion is therefore an actual random-target error bound in the
requested function metric, at a constant multiple of a pairwise variability
quantile, with finite-net and good-event costs fully accounted for.

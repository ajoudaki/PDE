# Query-time routes for the current-state posterior decoder

2026-10-06. Bounded author theory route; no experiment, promotion, or
maintained-source change. Scientific inputs were exactly
`CURRENT_STATE_DECODER_CANDIDATE.md`,
`FOURIER_ROW_PROGRAM_EVALUATION.md`,
`NOISY_TWO_ORIENTATION_TRANSCRIPT.md`,
`PHYSICAL_NOISY_PROGRAM_BRIDGE.md`, and
`NOISY_SCALAR_HISTORY_ACQUISITION.md`, read completely. No prior review
or other study was consulted.

**Conclusion.** No polynomial-time whole-query decoder is proved by this
route. The calculations below identify precise gaps in prior rejection
sampling, a global log-concavity argument, and a direct Gaussian
replacement of the Fourier integrand. They do not give a lower bound for
the actual neural decoder or rule out a different fast representation.
The current whole-sphere, all-time theorem remains a space theorem.

The research-contract, adversarial-audit, and rigorous-math skills were
applied. The required custom canonical-notation skill remained unreadable
even after an escalated read; no accessible copy was found. The supervisor
directed use of the explicit supplied notation conventions, preserving
the notation of the allowed scientific inputs.

## 1. Fixed target and the actual expensive object

At a current prefix of length \(j\), hold the retained coefficients
\(c=(c_1,\ldots,c_j)\) fixed. Let \(Z_1,\ldots,Z_n\) be independent
standard Gaussian row packets. Write

\[
 A_r(Z;c)=\frac1n\sum_{i=1}^n F_r(Z_i;c_{<r}),\qquad
 L_c(Z)=\prod_{r=1}^j\kappa_\eta(c_r-A_r(Z;c)),
 \quad p(c)=\mathbb E L_c(Z),
\]

where \(\kappa_\eta(u)=(\sqrt{2\pi}\eta)^{-1}
e^{-u^2/(2\eta^2)}\). For a bounded passive-query test
\(g_{x,t}(Z;c)\), including its fresh query randomness in the
expectation, the decoder requires

\[
 \frac{\mathbb E[L_c(Z)g_{x,t}(Z;c)]}{p(c)}.
\]

The Fourier construction computes smoothed threshold tests to fixed
constant accuracy, and then a median to output accuracy \(O(1/n)\).
The threshold Lipschitz constant, rather than the final test-expectation
accuracy, carries the inverse output-error scale. All scalar histories
stay fixed during this calculation. Replacing the history by population
moments or a newly noised history changes its target law.

If a query uses \(s\) additional summaries and one row has dimension
\(D\), the supplied conditional tensor rule has
\(Q^{j+2s}Q_z^D\) pairs of outer/inner grid nodes. Its bounds make the
logarithm of this count polynomial in compact description size and
logarithmic precision. That observation supplies a space bound; it does
not make the count polynomial. Evaluating the denominator once removes
repeated denominator work but leaves this numerator problem.

## 2. Prior rejection sampling: an exact cost obstruction for that method

Propose the whole row array from its independent Gaussian prior and
accept it with probability

\[
 \exp\!\left[-\frac1{2\eta^2}
       \sum_{r=1}^j(c_r-A_r(Z;c))^2\right].
\]

This is an exact posterior sampler. Put
\(P_{\max}=(\sqrt{2\pi}\eta)^{-j}\). Its acceptance probability
and mean number of proposals are exactly

\[
 a(c)=p(c)/P_{\max},\qquad \mathbb E N_{\rm prop}=P_{\max}/p(c).
\]

The existing good-density bound \(p(c)\ge d_*\) controls this mean
only by \(P_{\max}/d_*\). The logarithm of that bound is affordable
for memory, but its value is not polynomial in compact state size.

This concern is real for the general bounded analytic row interface.
Consider \(D=j\) and

\[
 F_r(z;c_{<r})=2\Phi(z_r)-1,
\]

where \(\Phi\) is the standard normal distribution function. These
functions are bounded, Lipschitz, and analytic on a fixed horizontal
strip. Each \(F_r(Z_i)\) is uniform on \([-1,1]\), independently
over \(i,r\). Let \(h_n\) be the density of their scalar mean.
For \(n\ge2\), Fourier inversion and absolute integrability give

\[
 \|h_n\|_\infty
 \le\frac n{2\pi}\int_{\mathbb R}
          \left|\frac{\sin u}{u}\right|^n du
 \le C\sqrt n.
\]

Indeed, for \(|u|\le1\), Taylor's inequality gives
\(\sin u/u\le1-u^2/7\le e^{-u^2/7}\); for \(|u|>1\), use
\(|\sin u/u|\le |u|^{-1}\). The two integrals are bounded by
\(\sqrt{7\pi/n}\) and \(2/(n-1)\), respectively. Convolution
with the independent scalar Gaussian noise does not increase a density's
supremum. Independence between coordinates therefore yields

\[
 p(c)\le(C\sqrt n)^j,
 \qquad a(c)\le(C'\eta\sqrt n)^j.
\]

For \(\eta=\exp[-(\log n)^a]\), with fixed \(a>1\), this gives

\[
 \mathbb E N_{\rm prop}
 \ge\exp\!\left(j[(\log n)^a-\tfrac12\log n-O(1)]\right).
\]

For interior states the displayed likelihood envelope is its actual
supremum, so a smaller constant envelope does not repair this particular
prior-proposal sampler. This example is not asserted to be the row
circuit produced by the specified neural training problem. Its logical
force is narrower: the bounded analytic row interface and its density
certificate do not themselves justify efficient prior rejection.

Literal proposals also contain \(nD\) Gaussian coordinates. A streamed
accept/reject test can accumulate all fixed-prefix moments in small
space, but retaining or revisiting the accepted row array for the
interacting passive query needs an additional representation argument.
An unproved short random seed is not an exact replacement for that array.

## 3. Gaussian prior and Gaussian noise do not imply posterior log-concavity

Even one bounded analytic summary can destroy global log-concavity.
Take \(F(z)=\sin z\). Up to a constant, the negative log posterior
on \(\mathbb R^n\) is

\[
 U(z)=\frac12\sum_i z_i^2+
       \frac1{2\eta^2}\left(c-\frac1n\sum_i\sin z_i\right)^2.
\]

At \(z_i=-\pi/2\) for every \(i\), its Hessian is

\[
 \nabla^2U(z)=\left(1-\frac{c+1}{n\eta^2}\right)I_n.
\]

Thus \(|c|<1/2\) and \(\eta^2<1/(2n)\) give a negative definite
Hessian there. These are typical rather than impossible observation
values: symmetry gives zero mean, and independence gives
\(\mathbb P(|C|\ge1/2)\le4(1/n+\eta^2)\) by the second-moment
bound. Consequently a global strong-convexity sampling argument cannot
be inferred from the stated interface. This is not a mixing-time lower
bound, and it leaves specialized samplers and alternative coordinates
open. As in Section 2, no embedding of this example into the exact
neural training circuit is claimed.

## 4. A direct Gaussian Fourier replacement has an unclosed frequency gap

For fixed \(c\), put
\(X=(F_1(Z;c_{<1}),\ldots,F_j(Z;c_{<j}))\),
\(\mu=\mathbb EX\), and
\(\Sigma=\mathbb E[(X-\mu)(X-\mu)^T]\). Assume the existing
coordinate cap \(|X_r|\le B\). For
\(a=2B\|\xi\|_1/n\le1\), Taylor's remainder gives

\[
 \left|\mathbb E e^{-i\xi\cdot(X-\mu)/n}
       -1+\frac{\xi^T\Sigma\xi}{2n^2}\right|
 \le a^3/6.
\]

The difference between \(1-v/2\) and \(e^{-v/2}\), for
\(v=\xi^T\Sigma\xi/n^2\le a^2\), is at most \(a^4/8\).
Both the characteristic function and the Gaussian characteristic
function have modulus at most one. Telescoping their \(n\)-th powers
therefore proves

\[
 \left|\left[\mathbb E e^{-i\xi\cdot X/n}\right]^n
       -e^{-i\xi\cdot\mu-\xi^T\Sigma\xi/(2n)}\right|
 \le C B^3\|\xi\|_1^3/n^2.
\]

This is a proved small-frequency estimate. On the existing full
Fourier box it would require at least \(2BjV/n\le1\), while the
supplied cutoff has scale \(V\gtrsim\eta^{-1}\). The physical
construction deliberately allows \(\log\eta^{-1}\) to be a large
power of \(\log n\); neither that inequality nor a small integrated
error is certified. The same issue applies to the joint training/query
characteristic function, with its additional coordinates and caps.

A saddle-point or local-limit method might prove that a smaller effective
frequency region suffices. Doing so needs quantitative decay or other
structure in the actual row law, together with a relative conditional
numerator/denominator error estimate. The allowed inputs provide neither
such a theorem nor a nondegenerate row-covariance gap. The deliberately
added matrix-observation gap controls a different operator; it is not a
lower bound on \(\Sigma\). This is a gap in this approximation route,
not a claim that the Gaussian approximation must fail on the physical
reachable states.

## 5. What posterior Monte Carlo and derandomization would still require

Fresh Monte Carlo at each query would add query-dependent failures to a
theorem whose decoder is deterministic on one whole-sphere, all-time
event. This does not mean every use of randomness is excluded: randomness
fixed during acquisition could yield a deterministic later function, if
a simultaneous uniform approximation were proved.

The missing construction has three linked requirements: generate correct
posterior samples from a current prefix; retain each sampled response in
absolute-polylogarithmic space; and evaluate its new-query response with
the required accuracy in polynomial time, without training scalar replay.
Finitely many bounded test expectations admit usual sample concentration,
but that fact supplies neither the compact sampled-response representation
nor uniformity over every input and time. A uniform argument can in
principle use a covering bound and a proved common modulus; it cannot be
replaced by a union over uncountably many fixed-query guarantees.

Likewise, the method of conditional expectations needs a computable
pessimistic estimator whose successive conditional expectations are
cheap. Substituting the present posterior integral as that estimator
reintroduces the unresolved integral. No efficient estimator is provided
by the existing sources.

Finally, the finite-bit hypothesis certifies polynomial *space* for
activation/data evaluation, not polynomial time. A polynomial bit-time
theorem would need an appropriate time interface or must explicitly
measure its runtime relative to the existing primitives. This is a
missing complexity hypothesis, not an unconditional separation theorem.

The remaining central proof obligation is a compact, uniformly accurate
representation of the fixed-prefix conditional query law with a counted
fast evaluation algorithm. The explicit calculations above narrow several
routes to that obligation without weakening the model, changing the
small-label condition, or claiming an impossibility result.

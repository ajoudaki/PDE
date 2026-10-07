# Decoder comparison with actual dense-run variability

Author refinement, 2026-10-07. This is a scoped proof contribution for the
working-paper rewrite, not an independent review or a promotion. The result
below replaces the analytic dense-center argument in the decoder comparison.
It uses the existing finite source, scalar-transcript generator, physical
query mesh, and complete-member median construction without changing them.

The conclusion is

\[
\Pr\!\left\{\|f_{\rm Log,n}-f_n^{\rm ind}\|_*
 \le 2b_n(\delta)+A_{\rm num}Yn^{-10}\right\}\ge1-\delta,
\qquad
b_n(\delta)=\inf\!\left\{b\ge0:
 \Pr(\|f_n-\widetilde f_n\|_*\le b)\ge1-\delta/32\right\}.
\tag{VD.1}
\]

Here the two dense trajectories in the definition are independent, ordinary
width-\(n\) dense runs. Thus \(b_n(\delta)\) is an actual variability
quantile, with confidence fixed as width changes. It is not an analytic
upper certificate. Neither this quantile nor the deterministic center used
in the proof is an input to the implemented decoder.

The additive numerical term is necessary in the original admissible class.
In particular the former argument using \(b_n\ge32Y/n\) cannot be reused
after changing the definition of \(b_n\). A verified example below has
positive labels and zero actual dense variability.

## Setup and precise statement

Use the original dense architecture and normalization. For
\(v=x/\sqrt d\in\mathbb S^{d-1}\), its forward pass is

\[
z^{(1)}=Av,\qquad z^{(j)}=W^{(j)}h^{(j-1)},\qquad
h^{(j)}=\phi_j(z^{(j)}),\qquad f_n=w^\top h^{(L)}/n.
\]

The initial entries of \(A\) are independent \(N(0,1)\), those of
each hidden mixer are independent \(N(0,1/n)\), all blocks are independent,
and \(w(0)=0\). Gradient flow minimizes
\(m^{-1}\sum_a(f_n(x_a)-y_a)^2\) with mobilities
\((n,1,\ldots,1,n)\). Set \(Y=\|y\|_2/\sqrt m\),
\(\lambda=\gamma/m\), where \(\gamma>0\) is the minimum
eigenvalue of the last-layer population feature covariance.

Retain all original decoder assumptions: analytic activations with the
stated strip and derivative bounds, \(L\ge2\), normalized inputs,
\(m\ge d\), spanning training inputs, and the entire original common
label interval. In particular no new label cap, covariance nonsingularity,
or actual-variability lower bound is assumed. Fix \(0<\delta<1/4\).
Keep the existing decoder orders, complete explicit enclosing width gate
(or its stated factorized alternative with all physical and implementation
gates), finite-word interfaces, and numerical error allocation. For the
clean branch use \(nY\ge1\). The small-label extension is recorded below.

The norm remains

\[
\|f-g\|_*=
\sup_{t\in[0,\infty]}\sup_{\|x\|_2=\sqrt d}|f(t,x)-g(t,x)|,
\]

including the fitted endpoint. To define a quantile before restricting to a
success event, assign discrepancy \(+\infty\) if either trajectory lacks
a complete trajectory with the uniform fitted limit required by this norm.
For every pair where these objects exist, use its actual discrepancy,
including pairs outside the proof's source-good event. This convention
does not condition or truncate the dense law and changes no success claim.
On successful trajectories, continuity and the uniform tail make the
supremum measurable by a countable dense set of finite times and inputs.

Under these assumptions (VD.1) holds for the existing decoder. In fact the
proof below bounds its failure by \(3\delta/16\), leaving unused budget
for a joint statement. The decoder is independent of the comparison dense
run. Its event covers all times, all sphere inputs, the endpoint, and inputs
selected after inspecting the model or earlier answers.

## A regular deterministic center exists at the actual quantile

Write \(\alpha=\delta/32\), and let \(F,F'\) denote independent
dense trajectories. The finite training-source theorem with reference
failure \(\rho_{\rm ref}=2^{-20}\delta\) supplies a regularity
event \(E_{\rm ref}\) of probability at least
\(1-\rho_{\rm ref}\). Its physical consequences include global fitting,
the real operator and all-sphere feature bounds, and the uniform endpoint
tail. The usual readout and feature estimates give

\[
\sup_{t,x}|F(t,x)|
 \le (2Y/\sqrt\lambda)(2H_D)=4YH_D/\sqrt\lambda
\quad\hbox{on }E_{\rm ref},
\]

where \(H_D\) is the existing dense population feature RMS envelope.
Consequently

\[
\Pr\{\|F-F'\|_*\le8YH_D/\sqrt\lambda\}
 \ge1-2\rho_{\rm ref}>1-\alpha.
\]

The quantile \(b=b_n(\delta)\) is therefore finite without using any
dense concentration rate. By continuity of probability along decreasing
events, its definition implies
\(\Pr\{\|F-F'\|_*>b\}\le\alpha\), including when \(b=0\).

For each deterministic dense trajectory \(f\), define the ball failure

\[
a(f)=\Pr\{\|F-f\|_*>b\}.
\]

Fubini's theorem gives \(\mathbb E[a(F')]
=\Pr\{\|F-F'\|_*>b\}\le\alpha\).
Markov's inequality yields \(\Pr\{a(F')>2\alpha\}\le1/2\).
Since \(\Pr(E_{\rm ref})>1/2\), there exists a realization
\(F'=f_{\rm c}\) in \(E_{\rm ref}\) with

\[
\Pr\{\|F-f_{\rm c}\|_*>b\}\le2\alpha=\delta/16<1/64.
\tag{VD.2}
\]

Fix this realization for the proof. The center \(f_{\rm c}\) inherits
the physical input and normalized-time moduli (FC.57)--(FC.58) and the
fitting tail. These are deterministic bounds with precisely the coefficients
already used in the decoder grid. Choosing a regular center is essential:
an arbitrary center obtained from averaging would not automatically have
these moduli. No algorithm locates, stores, or evaluates \(f_{\rm c}\).

## The finite law certificate transfers each fixed-code test

Fix an external input/time code \(c\). It specifies an input on the
sphere and a time in an acquired panel, or the frozen-tail time. The
existing finite source law has the following sufficient interface:

1. Run the source only through the code's acquired training prefix and
   append the reserved passive-query calls. At this fixed code the iid
   finite program can be coupled to one ordinary Gaussian dense
   initialization. On its physical source, sampler, coupling, and raw-noise
   events, its scalar prediction differs from that dense prediction by
   at most \(e_{\rm loc}\), an allocated multiple of \(Yn^{-10}\).
2. The source-plus-query scalar transcript has \(O(R^2w)\) bits, and
   its one-pass candidate verifier has \(O(R^2w)\) between-row bits.
   With inner error \(\varepsilon_{\rm in}=1/64\), its law under the
   short seed differs from the iid transcript law by at most that total
   variation. In particular this holds for any fixed success interval
   of its final scalar answer.
3. Literal selected-metric replay fails with probability at most
   \(2^{-12}\), also after replacing iid packets by the short seed.
   It only requires the separate fresh scalar marks to remain independent
   of the packet array. It does not require independence among packets.

These interfaces are proved in FC Sections 3--7 and its final transcript
inventory, and WB Section A. Their derivations matter here. The complete
Gaussian matrix call has the joint shadow augmentation (FC.39)--(FC.41);
conditioning only at complete-call boundaries preserves the two-orientation
posterior. Old and new moments use the same pre-setup precision. The
unseen-query contractions (FC.54)--(FC.55) are exact empirical reductions,
and the complete covariance correction is retained. Thus no population
replacement bias enters \(e_{\rm loc}\).

The private metric is excluded from the Gaussian posterior filtration.
One first transfers the virtual source transcript and then uses literal
replay to identify the compact prefix. Revealing the completed source's
future answers before the passive call, or asking for total variation of
the metric together with an entire dense path, would not be justified by
the certificate and is unnecessary here.

By (VD.2), the coupled physical dense answer is within \(b\) of
\(f_{\rm c}(c)\), except with probability at most \(\delta/16\).
This follows from a ball event for that coupled dense marginal; it does not
require the same coupling for two different codes. Apply transcript total
variation to the fixed interval

\[
I_c=[f_{\rm c}(c)-b-e_{\rm loc},
     f_{\rm c}(c)+b+e_{\rm loc}].
\]

The probability that one seeded, selected, complete member returns a value
outside \(I_c\) is at most

\[
\frac{\delta}{16}+\frac1{64}
+\underbrace{\left(2^{-20}+2^{-20}
+2^{-26}+2^{-29}+2^{-12}\right)}_{<1/1024}
<\frac1{16}.
\tag{VD.3}
\]

The five bracketed allocations are source failure, raw-noise RMS failure,
chronological Gaussian coupling failure, finite sampler failure, and metric
replay failure. All are unconditional complete-experiment failures. No
common unamplified source event is imposed across members.

The real endpoints of \(I_c\) cause no computational addition. The
final scalar answer has a finite alphabet; membership in \(I_c\) is
a fixed Boolean transition table in the proof test. WB Section A permits
arbitrary deterministic within-block computation. The implemented decoder
only computes the median and never tests membership in \(I_c\).

## Complete-member amplification and all-query transfer

Let \(N_{\rm ext}\) be the finite external code count, with
\(\log N_{\rm ext}\le C(d+1)Z\) as in (FC.60). Retain the
existing smallest odd ensemble size

\[
J\ge\left\lceil\log_2(16N_{\rm ext}/\delta)\right\rceil.
\]

For independent complete members, if their median lies outside \(I_c\),
at least \((J+1)/2\) members lie outside \(I_c\). Taking a union
over such subsets and using (VD.3) gives the conservative bound

\[
\Pr\{\operatorname{median}_j G_j(c)\notin I_c\}
 \le2^J(1/16)^{J/2}=2^{-J}
 \le\delta/(16N_{\rm ext}).
\]

The outer generator fools this fixed-code bad-member-counter test with
error at most \(\delta/(16N_{\rm ext})\). It needs only the
already counted member workspace and counter between member blocks; no
list of real center values is supplied to the actual model. A union over
codes proves, with failure at most \(\delta/8\),

\[
|f_{\rm Log,n}(c)-f_{\rm c}(c)|\le b+e_{\rm loc}
\quad\hbox{for every external code }c.
\tag{VD.4}
\]

The decoder answers an arbitrary query through one of the existing
qualifying codes. The physical regularity of \(f_{\rm c}\), the
space/time mesh, and the frozen tail give

\[
|f_{\rm c}(t,x)-f_{\rm c}(c)|\le e_{\rm mesh}+e_{\rm tail}.
\]

This holds also for \(t=\infty\), and for either permitted acquired
panel at a boundary. By the pre-existing numerical allocations,
\(e_{\rm loc}+e_{\rm mesh}+e_{\rm tail}
\le A_{\rm num}Yn^{-10}\). Therefore (VD.4) implies

\[
\|f_{\rm Log,n}-f_{\rm c}\|_*
 \le b+A_{\rm num}Yn^{-10}.
\]

An independent dense reference satisfies
\(\|f_n^{\rm ind}-f_{\rm c}\|_*\le b\) except with probability
\(\delta/16\), by (VD.2). The triangle inequality and union bound
give (VD.1), with total failure at most
\(\delta/8+\delta/16=3\delta/16<\delta\).
No full-process coupling of a finite member to a dense path, and no
total-variation statement for an infinite family of queries, has been used.
Adaptively chosen queries are covered because (VD.4) is simultaneous before
any query is selected.

## Resources, confidence, and boundary cases

All implemented orders remain those of the existing construction:

\[
R\le Cp\beta^{201L}(m+d+2)(1+m/\gamma)Z^{5/2},\qquad
w\le C\beta^{110L}Z,\qquad J\le C(d+1)Z.
\]

Nothing in these choices depends on \(b_n(\delta)\) or on the chosen
center. Thus the retained/live word count remains

\[
Cp^2\beta^{402L}(m+d+2)^2(1+m/\gamma)^2Z^6
[d+1+\log(e+(d+1)Z)],
\]

the initialization work retains its \(1115L\) activation power and
\(Z^{29/2}\) factor, the training work retains \(914L\) and
\(Z^{12}\) times its displayed logarithm, and query work retains
\(914L\) with \((L+1)nZ^{12}+Z^{14}\). Every interface cost and
setup peak inventory in the original theorem remains charged. The old
explicit width gates suffice; their numerical absorption gate can simply
be retained even though this new proof does not use it to absorb the
additive error.

For \(0<nY<1\), use the existing enlarged orders, code counts, and
Gaussian-RMS gate (FC.61)--(FC.62), replacing \(Z\) everywhere by
\(Z+\log(1/(nY))\). The same argument and error formula apply.
For \(Y=0\), all dense and compressed predictions are identically zero,
so the quantile and the error are exactly zero.

If a benchmark instead uses one universal failure level
\(0<\alpha_0\le1/128\), independent of both \(n\) and the requested
\(\delta\), the same center argument gives a dense-ball failure
at most \(2\alpha_0\). Assuming that quantile is finite, the unchanged
amplification gives success at least
\(1-2\alpha_0-\delta/8\), not arbitrary \(1-\delta\).
A fixed universal quantile cannot support arbitrarily high confidence for
an independent target without additional tail information. In (VD.1), the
confidence level \(\delta/32\) is fixed in width and is explicit.

The nonzero-label zero-variability case is admissible. Take
\(m=d=1\), \(x_1=1\), \(L\ge2\), and
\(\phi_j(z)\equiv1\). Then \(Q^{(L)}=[1]\), \(\gamma=1\),
the input spans, and a sufficiently small nonzero label satisfies the full
original allowance. All hidden gradients vanish, while

\[
\dot w_i=-2(f_n-y),\qquad
\dot f_n=-2(f_n-y),\qquad
f_n(t)=y(1-e^{-2t}).
\]

Every dense realization is the same nonconstant path, so
\(b_n(\delta)=0\). The prescribed finite time-code decoder has finitely
many scalar output values through its finite horizon and cannot equal this
nonconstant continuous function at every time. A pure bound
\(C b_n(\delta)\) would require exact equality and is therefore false
for this decoder over the complete original admissible class.

Whenever a separately justified lower bound gives
\(b_n(\delta)\ge A_{\rm num}Yn^{-10}\), (VD.1) does imply
the pure factor-three bound. The existing actual-trajectory lower theorem
for fixed admissible problems with \(m\ge2\) and \(Y>0\)
eventually supplies such domination: its
\(cY\sqrt\gamma/(\sqrt n\log^{5/2}(en))\) lower scale dominates
\(Yn^{-10}\). This consequence inherits that theorem's unquantified
eventual width. It must not be substituted into the explicit finite decoder
gate or asserted for the \(m=1\) case. Refining numerical precision
to an arbitrary unknown quantile would instead introduce a new dependence
on its scale and would require fresh resource accounting.

## Reading and integration boundary

The complete finite construction and complete word-backend proofs were
read, together with SOURCE_INSERTION_COMPLETION Sections 1--10; its
initialization section was also read in its identical integrated location.
Relevant complete RESULT source recurrences (S.1)--(S.32), real fitting and
tail proof, decoder statement, transcript transfer, query/amplification,
and resource sections were inspected. The current paper's corresponding
decoder theorem and amplification passages were inspected. The canonical
notation skill, its neural-network reference, and the rigorous-math skill
were applied. No external source theorem is needed for this refinement.

The substantive replacement is the new center argument, the interval test
in the finite program, and the confidence accounting above. The original
analytic upper certificate may still be used independently for explicit
accuracy inversion, but it must receive a different symbol if
\(b_n\) is reassigned to the actual quantile. The old statement that its
mesh term supplies \(b_n\ge32Y/n\), and the resulting unconditional
factor-three claim, must not survive that notation change. This file changes
no source theorem, shared paper, maintained book, code, or Git state.

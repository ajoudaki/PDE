# Independent check of the finite-source posterior interface

2026-10-06. Bounded independent reconstruction of whole-law scalar-noise
coupling, all-prefix information/pair constraints, and the finite-prior
block interface. This report makes no physical-source or full neural
decoder claim. No experiment, Git operation, other-route finding, study
history, or previous report was used. Only this report is written.

## Inputs, corrected assumptions, and verdict

The complete original `FAST_FINITE_POSTERIOR.md` was read at SHA-256
`f18b5aa240a1a7e734de2a1b5b9c9e753c0abe3e02250f1c13f5aa92bcdb9b8e`.
The complete permitted dependencies, already read in their current form,
are:

| Input | SHA-256 |
|---|---|
| `FAST_LOCAL_PRECISION_TEST.md` | `af2a238a3ea1ed73059fd61321ca8408ce487399542156dc44e5e06f5a3e2f91` |
| `FAST_UNIFORM_QUERY.md` | `e59f805980ddc664794eee8c0f310f51667e94592d4ee502978663e77c64bcd9` |

Required research/proof and canonical-notation instructions, including
the neural reference, remain current and were applied. No other
scientific source was fetched.

Two assumptions needed correction in the original:

1. An explicitly samplable finite law is not necessarily the image of a
   fixed finite block of uniform bits. Bernoulli probability \(1/3\)
   gives a finite, exactly rejection-samplable example: any deterministic
   map of \(b\) uniform bits has probabilities with denominator
   \(2^b\), so it cannot produce \(1/3\). The iid statistical lemma
   is valid for general finite priors, but the cited fixed-block PRG
   interface requires a specified bounded, fixed-bit packet sampler.
2. Identically distributed additional randomness alone does not ensure
   total-variation contraction if its dependence on source objects changes.
   The downstream algorithm must use independent additional randomness or
   the same conditional postprocessing kernel in the two models.

Both were corrected. The complete corrected target was read at SHA-256
`f3cc565c52e848611d576d877ca893964cf45a74fb35f86c0494fbe8b09413db`.
It now specifies the fixed-length uniform-bit packet map with bounded,
counted work/space for the generator conclusion, and the common-kernel
condition for postprocessing. The broader entropy/iid assertions are
explicitly kept distinct.

**Verdict for the corrected target: PASS within the assigned component
scope, with no unresolved finding.** The posterior in (4)–(5) remains the
shadow posterior evaluated at a prefix. Whole-law transfer does not assert
the same pointwise bound for the implemented source's own conditional
posterior at every prefix.

## Whole-source coupling

Let \(\delta_h(x)\) be the distance to the rounding boundaries
\(h(\mathbb Z+1/2)\). Along the shadow recursion, condition on all
packets and earlier scalar Gaussian marks. Its current empirical mean is
fixed and the next \(E_r\) is independent standard Gaussian. The
uniform boundary estimate from the assigned local-precision note gives,
for \(\zeta=\alpha h/(64P)\),

\[
 \Pr\{\delta_h(A_r+\eta E_r)\le2\zeta\}
 \le4\zeta(h^{-1}+\eta^{-1})
 \le8\zeta/h=\alpha/(8P).
\]

The admissibility condition \(2\zeta\le h/2\) holds for
\(P\ge1\) and \(0<\alpha<1\). A union over updates costs
\(\alpha/8\). Intersect with the finite-sampler coupling event,
whose failure is at most \(\alpha/2\).

On this intersection, induction starts at the empty prefix. Equal
prefixes give exactly equal finite test values and empirical means, even
if the finite evaluator is discontinuous. The change from
\(\eta E_r\) to \(\eta\widehat E_r\) is at most
\(\zeta\), while the shadow value lies more than \(2\zeta\)
from every boundary. The next rounded scalars agree. Every deterministically
generated row field whose inputs are the packet and scalar-prefix data
then agrees as well, including fields with stored creation-time arguments.

This coupling makes the complete observable finite-source objects unequal
with probability at most \(5\alpha/8\le\alpha\). The coupling
inequality therefore gives their claimed total-variation bound. It is a
joint bound for the entire tape, rather than one bound requiring a union
over every possible scalar value.

The comparison does not include the raw continuous and finite scalar
noises as observable matched objects; their distributions need not be
close in total variation. They serve to construct the coupling. Appending
an independent seed, or applying any common conditional kernel, contracts
the total variation of the observable objects. This validates transfer of
a simultaneous finite-code success event without dividing by a rare
prefix probability.

Private acquisition data must still reach a query only through the allowed
prefix. The separate compact replay result has its own success event and
failure allocation; it is not made deterministic or probability-free by
the scalar-channel comparison here.

## Information bound and all-prefix posterior control

Write \(Z=(Z_1,\ldots,Z_n)\). Given a shadow prefix \(c_{<r}\),
the empirical mean \(A_r\) is a deterministic function of \(Z\)
with \(|A_r|\le B\). Its variance is at most \(B^2\).
For the unrounded next observation \(A_r+\eta E_r\), independent
Gaussian noise gives

\[
 \begin{split}
 I(Z;A_r+\eta E_r\mid c_{<r})
 &=h(A_r+\eta E_r\mid c_{<r})-h(\eta E_r)\\
 &\le\tfrac12\log(1+B^2/\eta^2).
 \end{split}
\]

Here \(h(\cdot)\) in this display is differential entropy, not the
rounding step. The convolution has a continuous Gaussian-smoothed density
and bounded second moment, so the stated maximum-entropy bound applies.
Conditional deterministic rounding cannot increase mutual information.
Sum the conditional inequalities by the chain rule to obtain (3).
No differential entropy of finite noise is used.

For each array point with positive prior mass, its conditional posterior
mass is a martingale under the increasing scalar-prefix filtration.
Convexity of \(u\log u\), summed against the finite product prior,
makes

\[
 K_j=D(\pi_{C_{\le j}}\|\mu^{\otimes n})
\]

a nonnegative submartingale. Its terminal expectation is
\(I(Z;C_{1:P})\), bounded by
\(H=P\log(1+B^2/\eta^2)/2\). The first-crossing inequality gives
\(\Pr\{\max_j K_j>H/\alpha\}\le\alpha\).

The scalar acquisition rule uses the same test on every row, so it is
permutation-invariant. The iid prior and this rule make each posterior
exchangeable. If \(\nu_c\) is its common row marginal, finite sums
give the identity

\[
 D(\pi_c\|\mu^{\otimes n})
 =D(\pi_c\|\nu_c^{\otimes n})+nD(\nu_c\|\mu).
\]

The first term is nonnegative. On the preceding all-prefix event this
proves (4), with its factor \(1/(\alpha n)\), simultaneously at
every prefix. The finite array alphabet ensures all posterior quantities
are well-defined on the support of the prefix law; no Gaussian packet
prior is needed.

## Pair constraints and probability bookkeeping

Let \(S_E=\sum_{r=1}^P E_r^2\). The process
\(\mathbb E[S_E\mid C_{\le j}]\) is a nonnegative martingale
of initial expectation \(P\). Its maximal inequality bounds the
probability of exceeding \(P/\alpha\) at any prefix by \(\alpha\).

At a current prefix \(c_{\le j}\), fix an acquired index \(r\le j\).
Its stored creation-time arguments are now fixed. Conditional expectation
of the rounded observation identity gives

\[
 c_r=\nu_c F_r+\eta\,\mathbb E[E_r\mid c_{\le j}]
                         +\mathbb E[e_r\mid c_{\le j}],
 \qquad |e_r|\le h/2.
\]

Exchangeability justifies the single-row mean. Conditional
Cauchy–Schwarz, followed by the one total-noise bound, yields

\[
 |\nu_c F_r-c_r|
 \le\eta\sqrt{\mathbb E[S_E\mid c_{\le j}]}+h/2
 \le\eta\sqrt{P/\alpha}+h/2.
\]

No additional union over the acquired indices is needed. Markov's
inequality for \(S_E\) also gives a separate empirical pair-constraint
event, simultaneously over all acquired tests, with failure at most
\(\alpha\). If that empirical event is used, its failure must be
allocated in addition to the two all-prefix events.

For (4) and (5) together, the shadow failure is at most \(2\alpha\).
The whole-law comparison transfers the same prefix event to the actual
source at total failure at most \(3\alpha\). This is consistent
with the note's separately allocated shares. It is an event defined using
the shadow family \(c\mapsto\nu_c\). It does not replace that
family by the actual conditional posteriors, which can differ sharply
on rare prefixes. Similarly, an empirical pair event is transferred as an
event in packets and prefixes, without attempting to identify raw noises.
The additive \(h/2\) is necessary and is retained in the stated
common-Gram budget.

## Exact finite-prior blocks and the generator interface

At a fixed good shadow prefix, assume the supplied query-test conditions:
the mark vector \(U\in\mathbb R^r\) satisfies
\(\mathbb E_\nu UU^T\preceq I\), and the scalar factor \(G\)
satisfies \(|G|\le B_q\). These concern the actual specified finite
test functions; neither low entropy alone nor the scalar pair identities
automatically supplies them.

Let \(h_\nu\) be the deterministic row-entropy upper bound in (4).
For \(s h_\nu\le1/128\), product relative entropy and Pinsker's
inequality give
\(\|\nu^{\otimes s}-\mu^{\otimes s}\|_{\rm TV}\le1/16\).
Under the posterior product law each coordinate block mean of \(UG\)
has variance at most \(B_q^2/s\). Chebyshev bounds failure at
\(4B_q/\sqrt s\) by \(1/16\). The exact prior product block
therefore fails with probability at most \(1/8\).

For odd \(J\) independent blocks, at least half must fail for a
coordinate median to fail. The bound
\(2^J(1/8)^{J/2}=2^{-J/2}\), followed by coordinate union, gives
failure at most \(r2^{-J/2}\) and Euclidean error at most
\(4B_q\sqrt{r/s}\). The usual scalar second-moment version is
identical with its stated scalar cap. Positivity of the integer block
size remains a width/information gate, as in the assigned uniform-query
note. This argument is valid for any finite \(\mu\).

For the corrected generator extension, write \(b_\mu\) for the
specified fixed number of uniform bits producing one packet. Pad a
generator block to contain those bits and the required state/error
allowances. Within a block, execute the deterministic packet map and the
same finite row program. Discard row scratch before the next block;
only the running sum, counters, and threshold count survive in a
fixed-coordinate median-failure test. Exact finite sums/rational means,
or the specified finite rounding margins, must be charged consistently
in that test and in the returned estimator.

This is precisely the imported one-pass block interface. Its required
block length must cover \(b_\mu\), persistent state, \(\log N\),
and the log inverse distinguishing error. Packet-map work and scratch,
finite primitive costs, seed bits, and block generation are counted,
rather than inferred to be small from finite support. A proof threshold
may hardwire a finite rational approximation of an inaccessible shadow
moment, as in the assigned uniform-query note; it is not algorithm data.

Thus finite discontinuous row maps create no additional statistical
obstruction: the sampled law and tested functions are the same finite
objects throughout. Their relation to physical Gaussian matrix actions,
posterior passive-neural representations, and all-sphere/all-time accuracy
remains explicitly outside this component. No such relation is inferred
from the finite information or block estimates.

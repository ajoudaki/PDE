# End-to-end check of the Taylor, activation and assembly bridge

2026-10-06. Verdict: PASS for the complete combined construction under the
original source event and exact-real arithmetic contract. No required
correction was found. This verdict concerns the actual interface replacement,
not an inference from the component review verdicts. It is an internal
cross-route check, not an isolated promotion review.

## 1. Frozen inputs and read coverage

The final candidate audited completely is LOCAL_TAYLOR_ASSEMBLY_BRIDGE.md,
SHA-256
dedba0b570d6a73b5c9eabbd414953d01fdc6d46056de023748eede621c64f2b.

The complete necessary component proofs and interfaces were read:

- LOCAL_CONTINUATION_SETUP.md, all 662 lines, SHA-256
  c4c12b38e49e37ac5096e69ceabee1d41be6ad6bc4a1c57ece943959ef425bbe.
- LOCAL_ACTIVATION_BACKEND.md, final explicit-log version in full, SHA-256
  cbf26326c081fc19da31f5d38781eff2dfa2a5b97dee12eb1a8022770a2843e4.
- LOCAL_CONTINUATION_ASSEMBLY.md, all 622 lines, SHA-256
  488216678b1ea31fcfb8da5f396c8323eae3a38be067c2e431de21a600df2fe2.

The reviewer had already read the complete prior quadrature/stability route
notes and the relevant RESULT.md model, source, analytic-extension,
selection, storage and arithmetic proof sections. Those remain the imported
scientific dependencies. The original probabilistic source event and
all-time Harmonic comparison theorem are not freshly re-proved here.

The first read used bridge hash
3b03ba802827a4d13611eb849ac1f8abc78c1f688a348ca1210dda6736df5479
and backend hash
25e8c6dd6381d46b561a839339d538ea38926f4130af62dfb848f91cc6f54cbb.
During the audit the supervisor supplied the final hashes above. The final
bridge and backend were then both read completely. The backend replaces its
logarithm abbreviation by the explicit logarithm, and the bridge updates the
dependency hash and provenance; the mathematical interface, allocation and
cost argument are unchanged. This report binds to the final hashes only.

The reviewer authored the distinct Picard route and previously audited the
assembly argument, but did not author or assemble the present Taylor bridge.
No other study, archived book, Git history, final synthesis, or component
review verdict was used as proof evidence. After the present independent
derivation and preliminary verdict were sent, the supervisor supplied another
reviewer's partial corroborating observations. They were not used to establish
the findings below. This disclosure precludes describing the report as a blind
promotion review.

Required accessible rigorous-math and conjecture instructions, shared process
instructions, and docs/notation.qmd were applied. The canonical-notation skill
and its linked reference remain unavailable under the previously disclosed
permission limitation. No experiment or numerical implementation was run.

## 2. Complex source control and the four-term allocation

The backend's requested tolerance is reset everywhere to

\[
\tau=\frac{\delta_{\rm node}}{32\sqrt n}.
\]

This reset includes its scalar activation approximation, field perturbation,
global defect, and final source-output budgets. The use of a common tighter
tolerance is essential; changing only the final query accuracy would not
justify the argument.

For each real passive query, the exact restarted polynomial-field solution
lies throughout its complex disk inside the moving parameter ball proved in
the backend. Original-activation features and responses there have the core
RMS bounds \(H_j,B_j\). Original passive carriers have RMS at most the
core carrier coefficient and therefore coordinate maximum at most
\(\sqrt n\max_jK_j\). This is precisely the argument used in backend
(A15)--(A16) and (A24), and it applies at complex parameter states as well as
real ones. The query itself remains real.

The original preactivations in this ball lie in backend rectangle (A2).
The replacement forward-error induction moves each activation argument by at
most \(a/512\), inside the derivative-approximation domain. Thus the
activation-replacement estimates apply uniformly on the local complex disk;
they are not only nodal real estimates.

The backend tolerance makes the added source RMS less than one. Indeed the
quadrature definitions give \(\delta_{\rm node}\le1/64\), since
\(\eta\le1\), the mode counts are nonzero, and \(A_d,\mathcal Y\ge1\).
The separate dimension-one definition gives the same bound. Hence its
replacement bound with the above \(\tau\) is much smaller than one.
Consequently

\[
\|g^p(v)\|_2\le\sqrt n\,C_g,\qquad
C_g=\max_j\{H_j+1,B_j+1\},
\]

on the entire complex restart disk. The source is holomorphic there because
the restarted parameter solution is holomorphic and the setup activations
are polynomials.

Cauchy's coefficient bound on a radius-\(\widehat R_n\) disk, summed on
a half-radius panel, gives the source Taylor tail

\[
\|g_K-g^p(v)\|_2\le\sqrt n\,C_g2^{-K}.
\]

The second additional degree prescription in bridge (3) therefore bounds the
first error term by \(\delta_{\rm node}/64\).

The four-term decomposition is an exact addition and subtraction:

\[
g_K-g^0(\theta)
=(g_K-g^p(v))+(g^p(v)-g^0(v))
 +(g^0(v)-g^0(p))+(g^0(p)-g^0(\theta)).
\]

Each remaining term is controlled by an estimate that applies to its actual
arguments:

1. Activation replacement at \(v\) has coordinate error at most
   \(\tau/2\) by backend (A24)--(A25). Converting to Euclidean norm gives
   \(\sqrt n\,\tau/2=\delta_{\rm node}/64\).

2. The parameter Taylor tail is
   \(\|v-p\|_2\le2V\widehat R_n2^{-K}\). The original-source endpoint
   comparison gives coordinate error
   \(C_{\rm src}n\|v-p\|_2\); Euclidean conversion adds \(\sqrt n\).
   The first extra degree requirement in bridge (3) therefore gives
   \[
   2V\widehat R_nC_{\rm src}n^{3/2}2^{-K}
   \le\delta_{\rm node}/64.
   \]

3. The backend's global parameter estimate (A23), with tolerance \(\tau\),
   gives coordinate error at most \(\tau/2\) between original sources
   at \(p\) and at the true trajectory. Its Euclidean error is again
   \(\delta_{\rm node}/64\).

The second item's use of \(C_{\rm src}\) between two approximate states is
valid. That coefficient comes from the real passive-query comparison using
operator caps ten and readout RMS cap \(1+2Y/\sqrt\lambda\), not from a
probabilistic carrier maximum at one of the approximate states. On the real
panel, the backend gives
\(\|v-\theta\|_2\le5b_n/24\), and the constructed path has
\(\|p-\theta\|_2\le b_n/8\), with \(b_n\le1/4\).
Both states therefore lie strictly inside those real operator/readout caps;
their convex parameter segment does as well. The passive carrier RMS bound
and RMS-to-coordinate conversion in the original source comparison apply.
No learned-state source event is needed.

The sum is \(\delta_{\rm node}/16\), strictly below the assembly interface
\(\delta_{\rm node}/8\). All constants \(128,64,32\) in the allocation
are sufficient with the stated normalizations. Increasing \(K\) preserves
the previous geometric tails and defect inequalities, since \(K\ge8\)
and the relevant polynomial-times-exponential bounds decrease.

## 3. Identification of the computed source jets

The assembly originally requests jets of the original dense field. The bridge
expressly replaces this interface by jets of the disposable field
\(\widetilde F\), whose activation functions are the constructed
polynomials \(\psi_j\). This is justified, rather than silently assumed.

The setup field retains the dense mean-square loss, all block mobilities,
and all rank-one gradient equations. At a panel anchor, coefficient comparison
therefore yields exactly

\[
[W^{(j)}]_s=-\frac2{mns}
 \sum_a\sum_{i+k=s-1}[r_a\delta_a^{(j)}]_i
                            [h_a^{(j-1)}]_k^T,
\]

with all features, responses and residuals evaluated using \(\psi_j\).
There is no requirement of zero readout at a learned restart. The cached
contraction formula and grouped endpoint update are algebraic consequences
of this identity, so their previously derived costs remain valid.

The computed parameter coefficients through degree \(K\) are the true Taylor
coefficients of the local solution \(v\) of \(\widetilde F\), by the
causal ODE recurrence. Polynomial composition of two parameter series that
agree through degree \(K\) produces source series agreeing through degree
\(K\). Thus the passive jets computed from the available training/parameter
jets are exactly the coefficients defining \(g_K\) in the error proof.
There is no need for an inaccessible full local solution or higher parameter
coefficients to obtain them.

The last source coefficient of degree \(K\) uses known parameter coefficients
through degree \(K\); the rank-one increment action at that order involves
only lower indices whose sum is \(K-1\). Advancing to a coefficient of
degree \(K+1\) is unnecessary. Multiplication by panel powers to use the
assembly's normalized affine variable does not alter the identity or degree.

## 4. Online scalar composition and exact initialization

For a scalar input series \(z(t)\), compute
\(T_j(z(t)/B)\) by increasing polynomial index \(j\). At time order \(k\),
the coefficient of the recurrence product is

\[
\sum_{i=0}^k [t^i](z/B)\,[t^{k-i}]T_{j-1}(z/B).
\]

Its terms are available: lower time orders were retained, and the order-\(k\)
coefficient for index \(j-1\) was just computed. Hence the recurrence is
online in time order, not merely an offline full-series composition.
There are \(O(D)\) recurrence indices and \(O(k+1)\) operations per
product. Summing over \(k\le K\) proves \(O(DK^2)\) arithmetic with
\(O(DK)\) persistent words. Coefficient accumulation has only \(O(DK)\)
additional work and fits the bound.

Preparing the derivative polynomial once in \(O(D^2)\) arithmetic and
composing it by the same procedure has the same time/memory orders.
The spatial-query computation may use this online procedure or its offline
specialization. No original derivative evaluation or high-order derivative
oracle appears.

This backend evaluates the original activations only at the scalar real
Chebyshev construction nodes and during the separate exact original initialized
forward pass. The latter is necessary because the setup training jets have
degree-zero features from \(\psi_j\), which cannot substitute for the original
\(\phi_j\) training features. The bridge explicitly charges the additional
\(O(mP)\) arithmetic and \(O(Lmn)\) original value calls and retains
those exact source additions.

The polynomial coefficient construction may use inexact real values with the
backend's certified tolerance. Exact original initialized source additions
still use the inherited exact-real evaluation model; the finite-accuracy
allowance for polynomial construction does not establish finite-precision
exact initialization. The bridge correctly leaves finite precision outside
its result. The final compressed runtime uses original activations, original
initialization, and the original optimizer.

## 5. Paired assembly and total charges

For each base source the proved Euclidean node error is at most
\(\delta_{\rm node}/16\). Applying an initialized matrix of operator norm
at most eight gives image coordinate error at most
\(\delta_{\rm node}/2\), within the quadrature's allowance. Moving the
initialized matrix outside the finite scalar projection gives the same
coefficients exactly. Both pair members are compared against their own
original analytic source; no analyticity of the approximate panel sequence
is required for quadrature.

Panel coefficients are accumulated into the original retained global modes.
They add neither new source families nor a panel-count factor to the source
rank. Exact initial additions and paired initialized actions preserve the
original selection and initialization hypotheses.

Substitution of the proved scalar backend into the assembly envelope gives
all terms displayed in bridge (8):

- polynomial construction and exact original initialization;
- factorized training and passive jets, including grouped anchor advancement;
- scalar polynomial composition for training and passive queries;
- local-to-global moment tables and spatial-first projection;
- initialized-image coefficient actions;
- full source orthogonalization, coordinate selection, full-basis initialized
  mixer actions and retained metric assembly;
- the paired choice of geometry work/memory and time-node ordering.

The polynomial field does not introduce another dense matrix factor.
No implicit solve, adaptive rejected panel, high-order derivative oracle, or
unreported full-path cache is used. Certification uses the explicit scalar
radius/degree/tolerance formulas and the proved conditional source event.

The memory bound in (9) retains the \(LmnDK\) online recurrence state,
\(Lm^2K^2\) contraction caches, source coefficients and spatial projection
buffer, original matrices/current anchor, selected arrays, scalar tables,
data and geometry. The lower \(LmnK\) jet arrays and one passive query's
scratch are absorbed because \(D\ge1\) and \(m\ge1\).
There is no missing \(PK\) storage term: the factorized execution stores a
single dense anchor and the training factors, not all dense parameter jets.
The grouped endpoint sum writes the next anchor after the panel's source
processing has finished.

Activation call count \(O(LD+Lmn)\) and fresh Gaussian draws remain separately
exposed. Their inclusion in the headline work bound requires the stated scalar
and sampling cost model. The candidate now makes this qualification explicit.

## 6. Fixed-parameter exponents and Euler ratio

Using the explicit orders in bridge (10), the dominant dense cached-jet term
has logarithmic exponent

\[
\frac32+1+\frac{3(d-1)}2=\frac{3d}2+1.
\]

Initialized-image formation and full-basis mixer assembly have the same dense
exponent. The new scalar-composition term has order

\[
n\log(en)^{\,3/2+3(d-1)/2+3/2+2}
 =n\log(en)^{\,3d/2+7/2}.
\]

It is bounded by the conservative selector term
\(n\log(en)^{9d/2+3}\) for every integer \(d\ge1\).
The other linear-in-\(n\) contractions and projections are smaller.
Scalar moments, geometry, backend construction, and polylogarithmic selected
model arrays contribute only fixed logarithmic powers.

For every fixed \(d\),

\[
\frac{n\log(en)^{9d/2+3}}
     {n^2\log(en)^{3d/2+1}}
 =\frac{\log(en)^{3d+2}}n\longrightarrow0.
\]

This proves the headline
\(O(n^2\log(en)^{3d/2+1})\) under its scalar-cost qualifications.
Dimension one gives \(5/2\), as claimed; no angular grid is silently added.

Peak memory consists of \(P=\Theta(n^2)\) original/current dense arrays,
\(n\) times fixed logarithmic powers, and scalar/selected arrays of
polylogarithmic size. Therefore it is \(O(n^2)\) eventually at each fixed
admissible set of structural parameters. This is not uniform when dimension,
depth, conditioning, or target prescription grows with width.

The retained mode count still gives \(O(\log(en)^{3d+2})\) retained words.
The original comparison with source tolerance \(1/n\) still gives
\(n^{-1+o(1)}\) whole-sphere/all-time prediction error. Setup polynomial
activations are discarded and do not redefine the compared dynamics.

For the specified Euler benchmark, dividing setup work by
\(mPT/h\), with \(T=\Theta(\log(en))\), gives

\[
O(h\log(en)^{3d/2}).
\]

Every fixed inverse-polynomial \(h\) makes this ratio vanish. The candidate
correctly does not assert that Euler requires or attains a particular
accuracy at that step, or that setup is cheaper than dense training with the
same high-order integrator.

## Final assessment

The tightened tolerance, additional source Taylor degree, polynomial-field
factorization, online scalar backend, and assembly contracts fit together.
The combined result has no remaining author-interface gap identified in this
audit. Its essential qualifications remain the imported source event,
eventual fixed-parameter width regime, specified scalar-value and sampling
costs, and exact-real arithmetic rather than numerical/bit complexity.

Check method: complete proof-interface reading; reconstruction of all four
source-error bounds and domain checks; formal-series coefficient
identification; online recurrence and grouped-update analysis; term-by-term
work/memory accounting; dimension-one checks; and explicit exponent and Euler
ratio calculation. No experimental evidence or prior PASS verdict was used
to replace those checks.


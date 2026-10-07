# Bounded reconstruction of the separated confidence allocation

2026-10-07. Separate reconstruction in a reused author context. This agent
previously extracted the final theorem and authored
`IMPLEMENTATION_STREAMLINE.md`. It is not a blind independent review and
does not reconstruct the inherited physical, generator or numerical theorems.

**Verdict: PASS at the supplied component boundaries.** Fixed per-member
source confidence is sufficient for the implemented ensemble. The independent
dense reference retains the original confidence-dependent sufficient width.
The resource substitutions use the smaller member moment order and do not
increase the previous envelopes. The common-center argument and final failure
allocation are detailed below; no required correction to the frozen candidate
was found.

## 1. Exact two-order substitution and width domination

Fix one admissible training problem and one width, with dense width \(n\),
training count \(m\), input dimension \(d\), depth \(L\ge2\), feature
Gram gap \(\gamma>0\), activation envelope \(\beta\), label RMS
\(Y\), and \(0<\delta<1/4\), under all original assumptions.
Set
\[
 \rho_0=2^{-20},\qquad \rho_{\rm ref}=\rho_0\delta,
 \qquad \delta_0=\delta/256.
\]
For a source failure allowance \(\rho\), the finite-source statement
supplies
\[
 p(\rho)=\max\left\{1,\left\lceil
 \frac{\log(4emL/\rho)}{\log(64e^2)}\right\rceil\right\},
\]
\[
 n\ge\left\lceil
 \left[\frac{\beta^{2000L}(1+m/\gamma)^4
                    (m+d+p(\rho)+1)^4}{\rho}\right]^{20000}
 \right\rceil.
 \tag{1}
\]
Substitution gives exactly the candidate's two orders:
\[
 p_{\rm mem}=p(\rho_0)=\max\left\{1,\left\lceil
 \frac{\log(2^{22}emL)}{\log(64e^2)}\right\rceil\right\},
\]
\[
 p_{\rm ref}=p(\rho_{\rm ref})=\max\left\{1,\left\lceil
 \frac{\log(2^{22}emL/\delta)}{\log(64e^2)}\right\rceil\right\}.
 \tag{2}
\]
Both failure allowances lie in the theorem's interval \((0,1/4)\).
Since \(\delta<1\), \(p_{\rm mem}\le p_{\rm ref}\). The
quantity inside brackets in (1) is nondecreasing in \(p\) and in
\(1/\rho\), so the reference gate dominates the member gate, including
integer ceilings. Consequently the original enclosing scientific width,
with \(p_{\rm ref}\) and \(\rho_{\rm ref}\), remains sufficient.
It is not replaced by the fixed-confidence member width.

The inherited carrier-tail and horizon gates are unchanged. One may retain
the old explicit numerical RMS gate as well; it dominates the corresponding
member requirement because its field-count envelope is no smaller and its
failure allowance is smaller. The separate small-label/precision branch and
numerical absorption gate are unaffected. No new confidence-independent
width theorem is established for the dense reference.

## 2. A common center does not require a common analytic radius

The deterministic dense comparison in the supplied synthesis uses real
all-time fitting, feature-Gram, operator and RMS bounds, together with its
all-time training-carrier maximum. Their constants depend on the fixed
problem and \(n\), not on the probability allowance or moment order.
The source theorem plus the stated carrier-tail implication supplies those
bounds for either order in (2).

To make the center choice explicit, fix the set of Gaussian initialization
roots whose physical dense trajectories satisfy precisely those real
inequalities. Apply the supplied deterministic good-pair Lipschitz estimate
and scalar Gaussian extension construction on this fixed set. For each
input/time code, fix this extension and its deterministic center once.
Call the resulting center \(f_{0,n}\), as in the query component.
The same initialization law and same physical predictor are used for member
couplings and the independent dense reference; only their sufficient source
certificates and probability allocations differ.

The reference source theorem proves that this fixed real good set has
probability at least \(1-\rho_{\rm ref}\). The member source theorem
proves the stronger analytic properties needed by the member solver with
failure at most \(\rho_0\), and its success also implies those real
inequalities. Thus both comparisons use the same fixed extension and center.
There is no averaging over centers chosen separately for successful members.
The center remains a proof object and is never decoder input.

In particular the member analytic radius is
\[
 [p_{\rm mem}\beta^{100L}(1+\gamma/m)
                   \sqrt{\log(en)}]^{-1},
\]
which is at least the reference proof radius with \(p_{\rm ref}\).
Neither radius changes the real inequalities defining the common center.
This is the necessary interpretation of the candidate's statement that the
center can remain the same as in the original composition.

The standalone comparison's stringent source-failure share is still available
where needed: \(\rho_{\rm ref}<\delta_0/4\). It is not necessary
to impose \(\rho_0<\delta_0/4\) on the entire finite member experiment.
That member needs only a constant bad-output probability before amplification.
For its physical-center comparison the same extension's Gaussian deviation
bound at \(\delta_0\) remains valid; it is independent of the particular
source solver's radius certificate.

## 3. The per-member and simultaneous quantifiers

Fix a single external input/time code \(z\). The fixed-confidence
scientific source event, shared pre-setup numerical schedule, finite query
coupling, metric replay and inner transcript-generator transfer give one
complete member experiment with
\[
 \Pr\{|\widehat f_j(z)-f_{0,n}(z)|>b_n+\varepsilon_{\rm num}\}
 \le 1/16.
 \tag{3}
\]
Here \(b_n\) is the unchanged declared dense certificate at
\(\delta_0\), and \(\varepsilon_{\rm num}\) is the existing
allocated multiple of \(Yn^{-10}\). The numerical allocations can be
fixed absolute constants in probability: the scientific contribution is
\(\rho_0\), the Gaussian-center deviation contribution is at most
\(\delta_0<1/1024\), and the remaining fixed allocations can have sum
at most \(1/32\). Their sum is below \(1/16\). The component permits
these choices jointly before any source or metric is generated.

Equation (3) is marginal for each code. It does not assert simultaneous
success of every member or independence between events at different codes.
For \(J\) independent complete member inputs, let \(B_j(z)\) denote
the bad-output indicator. If a majority is bad, some subset of at least
\(J/2\) members is bad. Independence between complete experiments gives
\[
 \Pr\left\{\sum_{j=1}^J B_j(z)\ge(J+1)/2\right\}
 \le 2^J(1/16)^{J/2}=2^{-J}.
 \tag{4}
\]
The event includes each member's source, sampler, coupling, replay and inner
generator failures. It is not a majority of fresh query noises from one
common source.

Let \(N_{\rm ext}\) be the finite external-code count and choose odd
\(J\ge\lceil\log_2(16N_{\rm ext}/\delta)\rceil\). The supplied
outer block-generator theorem transfers the single-code bad-majority test
with error at most \(\delta/(16N_{\rm ext})\). Therefore its generated
ensemble has probability at most \(\delta/(8N_{\rm ext})\) of a bad
median at this code. Union over the finite codes gives failure at most
\(\delta/8\), in particular within the previous \(\delta/4\) share.
No independence of generated members is asserted after this substitution.

The independent reference still fails its physical-good-set or Gaussian
deviation conditions with probability at most
\(\rho_{\rm ref}+\delta_0\). Thus even retaining the looser previous
ensemble share gives
\[
 \Pr(\text{final failure})
 \le\delta/4+2^{-20}\delta+\delta/256<\delta.
 \tag{5}
\]
The physical input/time rounding, fitted tail, and numerical absorption
are unchanged deterministic implications on these events. They give the
same \(3b_n\) comparison with probability at least \(1-\delta\).
At \(Y=0\), the exact zero branch requires no normalization or absorption.

## 4. Resource substitution and nonincrease

Keep the candidate's common logarithm \(Z\), the precision envelope,
external-code allowance and ensemble-confidence requirement unchanged.
The cost construction may use
\[
 H_{\rm mem}=p_{\rm mem}H_0,\qquad
 K_{\rm mem}=K_0+\lceil\log_2p_{\rm mem}\rceil,
\]
where \(H_0,K_0\) are the unchanged base patch count and degree.
Both quantities are at most their former values with \(p_{\rm ref}\).
Validity follows from the cost note's argument for each order: the ratio of
patch size to analytic radius stays controlled and
\(p\,2^{-\lceil\log_2p\rceil}\le1\) controls the patch-count term
in the propagation bound. No monotonicity of that last ratio is required.

The sufficient field-count and word envelopes become
\[
 R\le Cp_{\rm mem}\beta^{201L}(m+d+2)(1+m/\gamma)Z^{5/2},
 \qquad w\le C\beta^{110L}Z.
 \tag{6}
\]
Here \(w\), not \(p_{\rm mem}\), is bits per numerical word.
The required precision correction \(O(\log p)\) cannot increase.
One may retain the old word schedule if convenient. The finite code count
has the same safe bound \(\log N_{\rm ext}\le C(d+1)Z\); the
original envelope already included patch-index bits through \(\log p\).

Every displayed modular resource monomial in the cost note is
nondecreasing in the nonnegative field, word and ensemble counts. Applying
(6) with the same common envelopes proves that the previous parameter
tables remain valid with \(p_{\rm mem}^2\) for retained/peak
training/query memory, \(p_{\rm mem}^5\) for setup and complete
training work, and \(p_{\rm mem}^4\) for query work. Setup's additional
peak terms have powers one and three of the same member order; they also
cannot increase. The outer seed, outer regeneration, all member states and
external interfaces stay charged.

This is a nonincrease of proved resource envelopes, not a measurement of
actual runtime or a claim that all confidence dependence vanishes. The
common \(Z\), code/ensemble terms and independent-reference sufficient
width still depend on \(\delta\). No practical width, GPU speedup,
fixed-machine-word guarantee, stronger label interval or quantified leading
dense coefficients follow from this refinement.

## Scope and frozen inputs

The candidate was read completely at SHA-256
`04ab930f8e4d37763f79883a4433efa91af07262e36c008f0c306f0aba9ae0c1`.
The current query component, final synthesis and assembly report were read
completely for this reconstruction. The cost note had already been read
completely in this same author context and its hash was unchanged. The
finite-source theorem's complete statement in Section 1 was reread; its
proof is an imported component boundary, not independently reconstructed
here. Current source hashes were:

| Source | SHA-256 |
| --- | --- |
| `SOURCE_SEED_EXACT_QUERY.md` | `877823e5b1032b93ec60a95e4f879c35aeac616d0983cfb269eef0429b84b524` |
| `CLOSURE_COMPOSITION_COSTS.md` | `2abd031ffc3f1548fd8cd92b0bc6e3594463327db09321104fb2110953ee44b0` |
| `TWO_GAP_CLOSURE_RESULT.md` | `041082caa7a7a6003de7536ae361f03ea4fd2841a6d4ed6e072aa8094abd9e74` |
| `TWO_GAP_CLOSURE_CHECK.md` | `615e780adc5e963742948e110f895329dddcac9318e99aad365755c12b5cd5d4` |
| `FULL_FINITE_SOURCE_PROBABILITY.md` | `6ecf89142925ef831b7efbf12ad84eacdfef3dc97f3c5b749bc7547311f9695a` |

The old assembly report's detailed component boundaries were used, not its
PASS label as a substitute for the confidence argument above. No linked
scientific source, other study, new numerical experiment or external
theorem was retrieved. Required canonical-notation, rigorous-proof and
research instructions were already current. Only this assigned report was
written; the candidate, implementation note, index and concurrent changes
were left untouched. This is a bounded author-context reconstruction and
cannot serve as a blind promotion review.

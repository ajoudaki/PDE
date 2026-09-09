# Hostile audit of 'ROUTE_CAUSAL_COMPOSITE.md'

## Verdict

**FAIL as a theorem about the complete all-source \(L=2\) OMFP grammar.**

The differentiated elementary-symmetric estimate in Lemma 4.1 and the
generating-function calculation in Theorem 5.1 are correct for the abstract
pure-shift skeleton *provided* two hypotheses hold:

1. a branch with \(k\) source shifts has \(k-1\) distinct charged
   chronological factors; and
2. after all moving-pointer and source-history expansions, the multiplicity
   of skeletons over each charged index tuple is bounded by \(C^k\) with one
   numerical \(C\) independent of the horizon and source order.

Neither hypothesis is proved.  The first proof omits dependencies through
the response coefficients and their marked descendants.  The second is
stated as “suppose” and hides both the growing exposed-source list and the
unbounded Leibniz--Faa di Bruno branching.  Consequently (1.1) is a valid
conditional combinatorial estimate, not a proved estimate for the exact
OMFP response propagator.

## 1. The scalar-node branch argument is incomplete

The proof of Lemma 3.1 says that selecting

\[
                    \sigma_{ss}x_s
\]

in \(r_s\) moves a dependency branch to \(x_s\).  A product node has two
children.  A branch may instead enter

\[
 \sigma_{ss}=\mathbb E[a_s\psi''(z_s)],
 \qquad
 z_s=\xi_s+\sum_{i<s}\varepsilon_i
       (Q_{is}+\bar\rho_{si})\delta_i.                \tag{1.1}
\]

It then encounters a historical response \(\bar\rho_{si}\) while still
inside the time-\(s\) slice.  Thus the assertion that a branch has at most
one response vertex at each time is false for the displayed DAG itself.
The historical vertex in this example does carry \(\varepsilon_i\), so the
example does not by itself disprove the weaker \(k-1\) count.  It does
invalidate the proof offered for that count.

More importantly, (2.1)--(2.5) are not a closed dependency grammar.  The
coefficients are generated nodes:

\[
 \bar\rho_{si}=\mathbb E[\psi'(u_s)p_s^i],
 \qquad
 \bar\sigma_{si}=\mathbb E[q_s^i],                    \tag{1.2}
\]

and \(p_s^i,q_s^i\) obey their own mutually coupled causal recurrences.
For example, the normalized top-source recursion contains

\[
 \zeta_s^i=(Q_{is}+\bar\rho_{si})q_i^i
 +\sum_{i<j<s}\varepsilon_j
   (Q_{js}+\bar\rho_{sj})q_j^i,                       \tag{1.3}
\]

so a branch through an outer \(\bar\sigma_{si}\) can immediately enter an
inner \(\bar\rho_{si}\).  Whether the single source-time factor attached to
the outer historical response pays for all such nested shifts can only be
decided from a simultaneous induction on the full \(p,q,\bar\rho,\bar\sigma\)
grammar.  No such induction appears in the note.

## 2. Moving-pointer histories are asserted, not charged

For a moving source direction \(\zeta\), the intrinsic identity is

\[
 D_\zeta(J^*V)=J^*D_\zeta V
              =\mathbb E[D_JD_\zeta V].              \tag{2.1}
\]

Differentiating again creates all mixed source orders.  In a moving
cylindrical representation, derivatives also hit the pointer vectors in

\[
 J^*V=\sum_\nu \mathbb E[\partial_\nu V]\,c_\nu.       \tag{2.2}
\]

The sentence after Corollary 3.2 says these operations merely change the
kernel decorating an existing chronological edge.  That is not a proof:
the derivative of a response kernel is itself another aggregate response
node, and several such nodes may live inside one outer historical summand.
To establish the claimed injection one must:

1. write every marked recurrence for
   \(p,q,\bar\rho,\bar\sigma\), including derivatives of the moving
   pointers \(c_\nu\);
2. define precisely which occurrences count as source shifts;
3. construct an injective map from all but one shift on each expanded
   root-to-leaf branch to distinct step-edge occurrences; and
4. prove the invariant under every Leibniz and Faa di Bruno split.

None of these steps is present.  Holding the marked response kernels as
“edge decorations” removes exactly the source-order hierarchy that the
lemma was supposed to control.

## 3. The branching constant is not horizon-independent as written

Theorem 5.1 assumes:

> “the positive majorant of the total finite branching of one
> response-shift transition is \(CS\).”

For a fixed finite chronology some finite constant always exists, but this
only produces \(C=C_N\).  Horizon independence requires a proof.  There are
two separate unresolved multiplicities.

### 3.1 History-label multiplicity

At time \(s\), an aggregate adjoint or response contains a sum over every
exposed source label \(i<s\).  The number of labels grows with \(s\).
The chronological simplex can absorb this growth only after showing that
each label choice contributes a new, distinct charged step.  That is
precisely the unproved all-source charging assertion in Sections 1--2.
It cannot also be assumed in the definition of \(C\).

### 3.2 Source-order branching

At source order \(m\), Leibniz and Faa di Bruno distribute marks among
products and activation inputs in a number of ways growing with \(m\).
There is no finite “branching of one transition” uniform in all source
orders before the analytic factorial weights and moment losses are used.
Theorem 5.1 does not prove that this weighted convolution has operator norm
bounded by one numerical \(C\).  Treating it as a kernel decoration merely
moves the missing estimate into \(C\).

There are also arbitrarily long non-response state paths between response
vertices.  The note explicitly excludes their transitions from
\(P_N^{\mathrm{resp}}\).  Their number and norms therefore cannot be
included in a horizon-independent \(C\) without a separate Volterra/product
estimate.

Thus \(C\) is neither numerically defined nor proved independent of \(N\),
the source order, or the moving-history list.  The conclusion following
(1.3), that the only horizon factor is \(A_N^d=O(t^d)\), is not established
for the actual OMFP response series.

## 4. What does pass

The following isolated calculations are correct.

1. For \(\varepsilon_i=a_i h\),

   \[
   \sum_{i_1<\cdots<i_r}
   \left|\partial_h^d\prod_{\ell=1}^r\varepsilon_{i_\ell}\right|
   \le A_N^d\frac{\tau^{r-d}}{(r-d)!}.
   \]

2. For the unrestricted positive source shift,

   \[
   \|S^kb\|_{\rho'}
   \le\frac{k!\rho}{(\rho-\rho')^{k+1}}\|b\|_\rho.
   \]

3. Under the two unproved hypotheses at the start of this audit, the series
   in (5.2) sums exactly to

   \[
   A_N^d\,
   \frac{\rho C^{d+1}(d+1)!}
        {\delta^{d+2}(1-C\tau/\delta)^{d+2}}\|V\|_\rho.
   \]

These facts justify a conditional pure-skeleton lemma.

## 5. Required downgrade

The title and Sections 1 and 7 must not say that the exact all-source causal
obstruction has been resolved.  The supported statement is:

> If the fully marked \(L=2\) response grammar admits a distinct-step
> charging injection and a weighted branching constant \(C\) uniform in
> horizon and source order, then Theorem 5.1 gives the displayed
> cross-radius bound.

Both antecedents remain open.  Therefore this note does not close either
graph-specific bridge needed for the uniform \(t^4|h|^5\) theorem.


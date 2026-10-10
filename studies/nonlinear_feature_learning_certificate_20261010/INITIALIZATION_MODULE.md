# Finite initialization module for the feature-learning certificate

Date: 2026-10-10. Scoped assembly dependency check; author-derived proof module,
not an independent promotion review. No paper file was edited.

## Finding and inspected inputs

The paper does not currently contain the required joint initialization
convergence statement. In `paper/compact_foundations.tex`, `cp:source` gives
analytic domains and RMS bounds, `cp:src-local-lemma` gives cavity comparisons,
and `cp:src-moments` develops stopped-path moment bounds. None asserts joint
empirical-law convergence, with second moments, of the initialized forward
arrays, first backward derivatives, and propagated feature accelerations.
The paragraph “Initial cavities and maximum improvements” supplies forward
initialization estimates, not the missing reverse/forward-reuse limit. Thus
there is no existing label in that file that can replace this module.

Actual scientific inputs read: all of `COMPATIBLE_RESULT.md`; the
initialization and exact-adjoint parts of `AUDIT_ACTIVITY.md` (the complete
audit was also visible in a tool result); all of `paper/compact_foundations.tex`;
`paper/compact.tex` through the setup and probability conventions; and
`docs/02-gaussian-reuse.qmd`, Section 2, Section 5.4 including its complete
conditioning proof, and A.1–A.4. The latter confirms the Gaussian conditioning
identity used below. The proof below reproduces that identity and its finite
induction, so it does not import the book's general finite-program theorem
or a trained population-flow theorem. Required canonical-notation and
rigorous-mathematics skills, including neural-network conventions, and
`RESEARCH_WORKFLOW.md` Part 1 were read. No other study was read.

The narrow point is useful: each initialized hidden matrix is queried only
three times, in a predictable order. Its inverted old-query Grams are the
forward feature Gram and the backward-response Gram, both strictly positive.
The new acceleration covariance may be singular; it is never inverted.

## Proposed lemma and proof

Use the paper's fixed data, Gaussian matrices, normalized inputs
\(v_a=x_a/\sqrt d\), zero readout, and physical-time flow. Write
\(k=2/m\) and suppress the initial time in this module. Assume the
forward feature Grams \(Q^{(1)},\ldots,Q^{(L)}\) are positive definite,
\(y\ne0\), and every activation is real analytic, nonaffine, with bounded
first derivative. The paper's stronger strip assumption suffices. The
compatible-input argument in the certificate proves the forward-Gram
premise; no invertibility of \(Q^{(0)}\) is required here.

Finite-width lower-case vectors are in \(\mathbb R^n\). Define

\[
 s=\sum_a y_a h_a^{(L)},\qquad
 b_a^{(L)}=s\odot\phi_L'(z_a^{(L)}),\qquad
 b_a^{(j)}=\phi_j'(z_a^{(j)})\odot
             W_0^{(j+1)\top}b_a^{(j+1)}.                 \tag{I1}
\]

Thus \(\dot\delta_a^{(j)}(0)=k b_a^{(j)}\). Put

\[
 V_1=k^2\sum_a y_a b_a^{(1)}v_a^\top,\qquad
 V_j=\frac{k^2}{n}\sum_a y_a b_a^{(j)}h_a^{(j-1)\top}
       \quad(j\ge2).                                    \tag{I2}
\]

These are exactly \(\ddot W^{(j)}(0)\). The preactivation and feature
accelerations are

\[
 r_a^{(1)}=V_1v_a,\quad
 r_a^{(j)}=V_jh_a^{(j-1)}+W_0^{(j)}a_a^{(j-1)},\quad
 a_a^{(j)}=\phi_j'(z_a^{(j)})\odot r_a^{(j)}.             \tag{I3}
\]

**Finite initialization lemma.** For every layer, the empirical row law of
all its forward vectors, vectors in (I1), reverse matrix answers in (I1),
and vectors in (I3) converges in probability in quadratic Wasserstein
distance to a deterministic finite-second-moment law. Consequently every
normalized same-layer pairwise inner product among these vectors converges
in probability to the corresponding limiting expectation. At layer 1 this
joint convergence includes each entire initialized row
\(g_i=W_{0,i:}^{(1)}\in\mathbb R^d\) and the entire acceleration row
\(V_{1,i:}\in\mathbb R^d\).

Write the limiting row variables as \(Z_a^{(j)},H_a^{(j)},B_a^{(j)},
R_a^{(j)},A_a^{(j)}\); expectations are taken on the indicated layer's
row-law probability space. In particular,

\[
 \frac1n\sum_a\|a_a^{(j)}\|_2^2
    \longrightarrow\sum_a\mathbb E_j|A_a^{(j)}|^2,
 \qquad
 \frac1n\|V_1\|_F^2
    \longrightarrow\mathbb E_1|V_{1,\mathrm{row}}|^2,   \tag{I4}
\]

and the normalized energies in this assertion are uniformly integrable.
The same is true for \(\|V_j\|_F^2\), \(j\ge2\). Every backward Gram
\(D^{(j)}_{ab}=\mathbb E_j[B_a^{(j)}B_b^{(j)}]\) is positive definite.
The complete first-row law includes the exact identities

\[
 g\sim N(0,I_d),\quad Z_a^{(1)}=g^\top v_a,\quad
 V_{1,\mathrm{row}}=k^2\sum_a y_aB_a^{(1)}v_a,\quad
 R_a^{(1)}=V_{1,\mathrm{row}}^\top v_a,\quad
 A_a^{(1)}=\phi_1'(Z_a^{(1)})R_a^{(1)}.                  \tag{I5}
\]

**Proof.** We first record exact conditioning, then perform a finite
forward–backward–forward induction. Only normalized second moments are
needed for the law induction.

For one initialized hidden matrix \(W\), collect its already revealed
forward query and answer in \(H,Z\), and reverse query and answer in
\(U,T\):

\[
 WH=Z,\qquad W^\top U=T.
\]

These matrices have \(n\) rows and a fixed number of columns. On the
event that the query columns are linearly independent, define

\[
 P_H=H(H^\top H)^{-1}H^\top,\qquad
 P_U=U(U^\top U)^{-1}U^\top.
\]

Conditional on the revealed transcript, the exact remaining law is

\[
 W=M+(I-P_U)\widetilde W(I-P_H),\qquad
 M=Z(H^\top H)^{-1}H^\top
    +U(U^\top U)^{-1}T^\top(I-P_H),                    \tag{I6}
\]

where \(\widetilde W\) has independent \(N(0,1/n)\) entries.
Indeed, \(U^\top Z=T^\top H\), so \(MH=Z\) and \(M^\top U=T\).
A homogeneous perturbation preserves the two observed actions precisely
when it equals \((I-P_U)E(I-P_H)\). The displayed \(M\) is
Frobenius-orthogonal to every such perturbation. Orthogonal components
of an isotropic Gaussian vector are independent, which proves (I6).
With no previous reverse query, omit the terms involving \(U\).

This remains valid under interlaced queries to the independent hidden
matrices. Condition first on all first-layer Gaussian roots. Every next
query below is determined by earlier answers. Given these answers, its
new observation is a linear constraint on one remaining Gaussian matrix
subspace. Decomposing that residual along the new query and its orthogonal
complement leaves the latter Gaussian and independent of the other matrix
residuals. Induction on the number of calls proves (I6) conditional on
the global transcript. No unrevealed matrix entry is used to choose a query.

Here are the two instances of (I6) needed after the ordinary forward pass.
For the first reverse call, put

\[
 Q_n=H^\top H/n,\qquad C_n=Z^\top U/n,\qquad D_n=U^\top U/n.
\]

Then, for an independent matrix \(\Xi\) of standard Gaussian entries,

\[
 T=W^\top U
   \overset d=H Q_n^{-1}C_n+(I-P_H)\Xi D_n^{1/2}.       \tag{I7}
\]

The discarded projection has exact conditional normalized energy

\[
 \mathbb E\!\left[\frac1n\|P_H\Xi D_n^{1/2}\|_F^2
                 \,\middle|\,\text{past}\right]
 =\frac{\operatorname{rank}H}{n}\operatorname{tr}D_n.  \tag{I8}
\]

After both calls, a new forward query matrix \(A\) satisfies

\[
 \begin{aligned}
 F_n&=H^\top A/n,&J_n&=T^\top A/n,&E_n&=A^\top A/n,\\
 \Sigma_n&=E_n-F_n^\top Q_n^{-1}F_n,\\
 WA&\overset d=ZQ_n^{-1}F_n
       +UD_n^{-1}(J_n-C_n^\top Q_n^{-1}F_n)
       +(I-P_U)\Xi\Sigma_n^{1/2}.                       \tag{I9}
 \end{aligned}
\]

Here \(\Sigma_n=A^\top(I-P_H)A/n\succeq0\), including when it is
singular. The projection discarded from (I9) has conditional normalized
energy \(\operatorname{rank}(U)\operatorname{tr}(\Sigma_n)/n\).
The two fresh Gaussian matrices in (I7) and (I9) refer to their respective
calls; the latter is introduced after conditioning on the former answer.

We spell out the probabilistic induction needed to take limits in these
identities. Suppose the empirical law of a stored row tuple converges in
\(\mathcal W_2\) to a deterministic law. Appending independent iid
standard Gaussian rows appends independent Gaussian coordinates to that
limiting law: conditional variances of averages of bounded test functions
are \(O(1/n)\), their conditional means are integrals against the stored
empirical law, and the appended empirical second moment obeys the Gaussian
law of large numbers. Bounded continuous tests identify weak convergence;
convergence of total second moments gives \(\mathcal W_2\) convergence.
These statements hold in probability by the same conditional estimates.

Same-layer empirical products converge because they are continuous and
have at most quadratic growth. Coefficients formed from these products
therefore converge, and inverses converge whenever the deterministic limit
Gram is positive definite. Covariance square roots converge even at
singular limits: in fixed dimension the nonnegative square roots are
bounded, every convergent subsequence squares to the limiting covariance,
and uniqueness of its nonnegative square root identifies every subsequence.
Thus Gaussian multiplication by these square roots preserves the joint-law
limit. Equations (I8) and its counterpart for (I9) show that their projected
parts vanish in normalized mean square in probability, since the traces
are bounded in probability. Coupling rows by their indices shows that
adding such a vanishing error does not change a \(\mathcal W_2\) limit.

Finally, every coordinate map used here is continuous and has at most
linear growth in its finite tuple of inputs: the maps are affine
combinations, the Lipschitz activations, and
\((z,q)\mapsto\phi_j'(z)q\). They preserve joint \(\mathcal W_2\)
convergence. One direct verification couples convergent laws in \(L^2\),
uses continuity for convergence in probability, and uses the common linear
envelope and uniform integrability of squared input norms to pass to
\(L^2\). Random scalar coefficients converging to constants can be
handled first as linear combinations, using bounded normalized input norms.

Start with the entire iid first-layer root \(g_i\), not merely its
preactivation projections. Its empirical law converges in
\(\mathcal W_2\) to \(N(0,I_d)\). At the first pass through a hidden
matrix, conditional on the lower features, its output rows are iid
Gaussian with covariance their empirical Gram. The preceding induction
gives the forward limiting laws

\[
 Z^{(j)}\sim N(0,Q^{(j-1)}),\qquad
 H_a^{(j)}=\phi_j(Z_a^{(j)}).
\]

Make every forward call before starting the downward recursion (I1).
At its top, the coordinate map in (I1) is continuous with at most linear
growth, so the top backward tuple has the joint-law limit
\(B_a^{(L)}=(\sum_b y_bH_b^{(L)})\phi_L'(Z_a^{(L)})\).
Its Gram is positive definite. To see this, if \(c^\top B^{(L)}=0\)
almost surely, full support of \(Z^{(L)}\), continuity, and analyticity
give

\[
 \left(\sum_b y_b\phi_L(z_b)\right)
 \left(\sum_a c_a\phi_L'(z_a)\right)=0
        \quad\text{for every }z\in\mathbb R^m.
\]

The first factor is not identically zero since
\(y^\top Q^{(L)}y>0\). The second factor therefore vanishes on a
nonempty open set and, by analyticity, everywhere. Varying one coordinate
and using the nonconstant derivative of a nonaffine activation gives
\(c_a=0\) for each \(a\).

For the downward call from layer \(j+1\) to layer \(j\), (I7) applies
with \(H=[h_a^{(j)}]\), \(Z=[z_a^{(j+1)}]\), and
\(U=[b_a^{(j+1)}]\). No earlier reverse call used this matrix, and the
upper tuple is determined by earlier revealed answers. The induction gives
the same-layer limiting reverse answer

\[
 \sum_bH_b^{(j)}[(Q^{(j)})^{-1}C]_{ba}+\Gamma_a,
 \quad C_{ba}=\mathbb E_{j+1}[Z_b^{(j+1)}B_a^{(j+1)}],
 \quad\Gamma\sim N(0,D^{(j+1)}),                        \tag{I10}
\]

where \(\Gamma\) is independent of the entire previously stored
layer-\(j\) tuple, including \(g\) when \(j=1\). Multiplication by
\(\phi_j'(Z_a^{(j)})\) yields \(B_a^{(j)}\). Hence

\[
 c^\top D^{(j)}c\ge\lambda_{\min}(D^{(j+1)})
       \sum_a c_a^2\mathbb E_j[\phi_j'(Z_a^{(j)})^2]>0
       \quad(c\ne0).                                   \tag{I11}
\]

Each marginal Gaussian preactivation is nondegenerate, and a nonzero
analytic derivative has a discrete real zero set. This proves the strict
last inequality and closes the backward induction. Only the already
positive feature Gram was inverted during this pass.

Now construct (I3) forward. The first-layer row formulas are coordinate
maps of its stored tuple and give exactly (I5). For \(j\ge2\), the
learned-link term is, column by column,

\[
 V_jh_a^{(j-1)}
   =k^2\sum_b y_b b_b^{(j)}Q_{n,ba}^{(j-1)}.             \tag{I12}
\]

Its law converges by the existing feature-Gram and backward-tuple limits.
For the remaining term \(W_0^{(j)}[a_a^{(j-1)}]\), use (I9) with
the previous forward features as \(H\), previous backward query as
\(U=[b_a^{(j)}]\), and new acceleration query as
\(A=[a_a^{(j-1)}]\). This query is known after the preceding acceleration
steps; all its defining matrix answers have already been recorded.
The coefficients \(F_n,J_n,E_n\) are second moments in the lower layer,
while \(C_n,D_n\) are second moments in the upper layer. All therefore
have deterministic limits. The only inverses are \(Q_n\) and \(D_n\),
whose limits have just been proved positive definite. The conditioning
induction proves joint convergence with the previously stored upper tuple.
Adding (I12) and applying the bounded activation derivative proves the
claimed joint laws of \(R^{(j)},A^{(j)}\). This finishes a fixed number,
\(3(L-1)\), of hidden-matrix calls. Finite-width Gram inverses are used
only on events of probability tending to one; their complements do not
affect convergence in probability.

For completeness, uniform integrability does not require controlling a
Gram inverse on those complements. Put

\[
 M_n=1+\|W_0^{(1)}\|_F/\sqrt n
            +\sum_{j=2}^L\|W_0^{(j)}\|_{\mathrm{op}}.
\]

This has bounded moments of every fixed order, uniformly in \(n\).
For the first term this follows from Jensen's inequality and Gaussian
moments. For a hidden matrix, take \(1/4\)-nets of the unit spheres
with at most \(9^n\) points each. The operator norm is at most twice
the maximum net bilinear form, so Gaussian tails give
\(\Pr\{\|W_0^{(j)}\|_{\mathrm{op}}>2t\}
\le2\,9^{2n}e^{-nt^2/2}\). Above a fixed constant this is bounded
by \(2e^{-nt^2/4}\); tail integration gives the moment assertion.

The normalized Frobenius norms of every finite array in (I1)–(I3)
are bounded by a fixed polynomial in \(M_n\). Indeed forward recursion
uses linear activation growth and operator norms; backward recursion uses
bounded activation gates and operator norms; (I2) uses a finite sum of
outer products; and (I3), or (I12), uses those same bounds. For the first
block use \(\|V_1\|_F/\sqrt n\), and for later blocks use
\(\|V_j\|_F\). The fixed polynomial depends on the fixed data,
activations, depth, and labels, not on width. All these squared norms
therefore have a uniformly bounded moment of some order larger than one.
This proves their uniform integrability directly for the original arrays.
It also upgrades convergence of their normalized energies to convergence
in \(L^1\). Together with the empirical \(\mathcal W_2\) convergence,
it supplies squared-tail uniform integrability, both in probability and
after expectation. The proof of the lemma is complete.

## Consequences available to the assembly

The module proves the limit needed in the adjoint argument without
introducing a population weight operator on an entire function space.
Use the exact finite identity from the candidate,

\[
 \sum_a\frac{y_a}{n}(b_a^{(j)})^\top r_a^{(j)}
  =\frac1{k^2}\sum_{q=1}^j\|V_q\|_{\mathrm{mob}}^2,
 \quad
 \|V_1\|_{\mathrm{mob}}^2=\|V_1\|_F^2/n,
 \quad
 \|V_q\|_{\mathrm{mob}}^2=\|V_q\|_F^2\ (q\ge2).
\]

Both sides now converge to their indicated finite-row-law moments. The
parameter-energy limits are

\[
 e_1=k^4y^\top(Q^{(0)}\circ D^{(1)})y,\qquad
 e_j=k^4y^\top(Q^{(j-1)}\circ D^{(j)})y\quad(j\ge2).
\]

They are strictly positive: for any positive semidefinite Gram \(Q\)
with positive diagonal and \(D\succ0\),
\(Q\circ D\succeq\lambda_{\min}(D)\operatorname{diag}(Q)\succ0\).
Thus

\[
 \sum_a y_a\mathbb E_j[B_a^{(j)}R_a^{(j)}]
       =k^{-2}\sum_{q=1}^je_q>0.
\]

At least one \(R_a^{(j)}\) is consequently nonzero in \(L^2\).
Since each \(\phi_j'(Z_a^{(j)})\ne0\) almost surely and
\(A_a^{(j)}=\phi_j'(Z_a^{(j)})R_a^{(j)}\),
\(\sum_a\mathbb E_j|A_a^{(j)}|^2>0\). These statements, the complete
joint first-root/row-acceleration law (I5), and uniform integrability
are sufficient initialization inputs for a separate finite-time argument.
No fixed positive-time feature displacement or full population dynamics
is asserted or imported by this module.

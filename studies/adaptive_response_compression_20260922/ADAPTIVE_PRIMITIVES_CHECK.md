# Scoped check of two adaptive compression primitives

Date: 2026-09-22. This is a prompt-only arithmetic and logical verification
of the supervisor's two supplied lemmas, not an independent creative
attempt, promotion review, or proof of an adaptive population solver.
Only the supplied premises and the required rigorous-math skill were used.
No external sources, prior studies, experiments, or Git operations were
used. A scoped subagent checked the streaming lemma separately from the
same supplied premises.

**Verdict:** both proposed primitives are correct in exact arithmetic,
with the information and norm qualifications below. The streaming
off-diagonal bound is an operator-norm bound. The same construction also
has the Hilbert--Schmidt estimate stated below.

## 1. Gaussian interpolation with forward and reverse queries

Let \(W_0\in\mathbb R^{n\times n}\) have independent \(N(0,1/n)\) entries.
Let \(V,U\subseteq\mathbb R^n\) be the queried input and output spans,
respectively. Write \(P_V,P_U\) for their orthogonal projectors, and
\(Q_V=I-P_V,\ Q_U=I-P_U\). Full forward responses on \(V\) and full
reverse responses on \(U\) reveal \(W_0P_V\) and \(P_UW_0\). The latter
is the adjoint of the observed map \(W_0^*P_U\).

With mutually consistent exact observations, define
\[
 \widehat A=W_0P_V+P_UW_0-P_UW_0P_V
           =W_0P_V+P_UW_0Q_V.
\]
Every term is determined by the observations. Direct multiplication gives
\[
 W_0-\widehat A=Q_UW_0Q_V,\qquad
 \widehat A P_V=W_0P_V,\qquad
 \widehat A^*P_U=W_0^*P_U.
\]
In particular, for every \(h,g\), including directions chosen after
observing the history,
\[
 \|(W_0-\widehat A)h\|
 \le \|W_0\|_{\rm op}\operatorname{dist}(h,V),\qquad
 \|(W_0^*-\widehat A^*)g\|
 \le \|W_0\|_{\rm op}\operatorname{dist}(g,U).
\]
These are deterministic bounds. Moreover,
\[
 \operatorname{rank}\widehat A
 \le\operatorname{rank}(W_0P_V)+\operatorname{rank}(P_UW_0Q_V)
 \le\dim V+\dim U.
\]

For fixed \(U,V\), choose orthonormal coordinates adapted to these
subspaces. The four blocks of \(W_0\) in those coordinates have independent
Gaussian entries: orthogonal changes preserve the covariance
\(n^{-1}I\) of the vector of all entries. The queries reveal every block
except the \(U^\perp\times V^\perp\) block. That remaining block is
independent of the revealed blocks and centered. Therefore the
conditional mean is \(\widehat A\), and the conditional residual law is
\[
 W_0-\widehat A\ \big|\ \text{query history}
 \ \stackrel{\rm law}{=}\ Q_U G Q_V,
\]
where \(G\) is a fresh matrix with independent \(N(0,1/n)\) entries,
independent of the conditioned history.

### Why sequential adaptive directions are allowed

Let \(\mathcal F_k\) contain the directions and full responses of the
first \(k\) queries, together with any auxiliary randomness independent
of \(W_0\). Each next direction and choice of query type must be
\(\mathcal F_k\)-measurable. The claim follows by induction.

Conditioned on \(\mathcal F_k\), suppose the unobserved residual has
law \(Q_U G Q_V\). A new forward query \(v\) reveals no new information
if \(Q_Vv=0\). Otherwise set \(q=Q_Vv/\|Q_Vv\|\), using Euclidean
normalization in this argument. Its new random response is proportional
to \(Q_UGq\). The Gaussian decomposition
\[
 Q_UGQ_V=(Q_UGq)q^*
             +Q_UG(Q_V-qq^*)
\]
has independent summands, because they use orthogonal column directions
of a centered isotropic Gaussian matrix. Conditioning on the response
fixes the first summand and leaves the second centered with precisely
the covariance for the enlarged span \(V+\operatorname{span}\{v\}\).
The updated mean is the displayed interpolation formula for that span.
A reverse query has the same proof with row and column roles exchanged,
enlarging \(U\). This proves the statement at every finite stage.

Decisions to stop based solely on the recorded history reveal no
additional information about the residual beyond that history. The
statement therefore also holds at an almost surely finite such stopping
time, by conditioning separately on each possible stopping index.

The restriction on the information used to choose directions matters.
A direction or extra observation depending on unqueried entries of
\(W_0\) can invalidate the claimed posterior. Also, conditioning here
means conditioning on the complete query history, not merely on the
dimensions of the final spans.

### Adjoint consistency and normalization

Forward and reverse responses must concern the same realized operator
\(W_0\) and its actual adjoint. Sampling two unrelated Gaussian operators
for the two response types does not satisfy the premises. The interpolant's
adjoint is determined, not fitted independently:
\[
 \widehat A^*=P_VW_0^*+W_0^*P_U-P_VW_0^*P_U.
\]
The fresh-\(G\) statement describes a conditional law. It does not permit
forgetting previous responses when generating subsequent responses.

For equally normalized finite population spaces
\(\langle x,y\rangle_n=x^\top y/n\), the matrix adjoint is still transpose,
orthogonal projectors are unchanged, and the operator norm is the usual
spectral norm. Thus all formulas above remain valid with that convention.
There is no implied infinite-population Gaussian conditioning theorem here.

## 2. Deterministic streaming update compression

Let \(\mathcal H_2,\mathcal H_1\) be real Hilbert spaces and use the
orthogonal direct sum with inner product
\[
 \langle(x,y),(x',y')\rangle
 =\langle x,x'\rangle_{\mathcal H_2}
   +\langle y,y'\rangle_{\mathcal H_1}.
\]
This is the sum, not the average, of the two inner products. Tensors
denote Hilbert-space operators: \(u\otimes v:h\mapsto u\langle v,h\rangle\).

Consider a finite stream of real \(a_j\) and unit factors \(u_j,v_j\).
Put
\[
 K_N=\sum_{j=1}^N a_j u_j\otimes v_j,\qquad
 A_N=\sum_{j=1}^N|a_j|,\qquad
 z_j=(\sqrt{|a_j|}\,u_j,\
             \operatorname{sign}(a_j)\sqrt{|a_j|}\,v_j).
\]
For \(a_j=0\), set \(z_j=0\). Then
\[
 C_N=\sum_{j=1}^N z_j\otimes z_j\ge0,\qquad
 (C_N)_{12}=K_N,\qquad
 \operatorname{tr}C_N=2A_N.
\]
The sign occurs in exactly one factor, so the upper-right block has
coefficient \(a_j\), including negative increments.

Fix an integer \(P\ge0\). Start \(S_0=0\). At step \(j\), form
\(B_j=S_{j-1}+z_j\otimes z_j\), which is positive and has rank at most
\(P+1\). If its rank is at most \(P\), set \(S_j=B_j\) and
\(\delta_j=0\). If its rank is \(P+1\), let \(R_j\) be its support
projector and \(\delta_j>0\) its smallest nonzero eigenvalue. Set
\[
 S_j=B_j-\delta_jR_j.
\]
This removes the smallest eigenvalue and subtracts the same value from
every positive eigenvalue. Hence \(S_j\ge0\) and
\(\operatorname{rank}S_j\le P\). A tied minimum can remove several
directions; this preserves the required rank inequality.

Define \(E_N=C_N-S_N\) and \(D_N=\sum_{j=1}^N\delta_j\). At stages with
no shrink, interpret \(\delta_jR_j=0\). Telescoping gives
\[
 E_N=\sum_{j=1}^N\delta_jR_j\ge0,\qquad
 \|E_N\|_{\rm op}\le D_N,\qquad
 \operatorname{tr}E_N=(P+1)D_N.
\]
The trace identity is exact because every nonzero shrink has support
rank \(P+1\). Since \(S_N\ge0\),
\[
 (P+1)D_N
 =\operatorname{tr}C_N-\operatorname{tr}S_N
 \le2A_N.
\]

### The off-diagonal factor of one half

For any bounded positive block operator \(E\), put \(M=\|E\|_{\rm op}\).
Since \(0\le E\le MI\),
\[
 \|E-\tfrac M2 I\|_{\rm op}\le\tfrac M2.
\]
The upper-right block of this centered operator is still \(E_{12}\).
Restricting its domain to \(\mathcal H_1\) and projecting its range to
\(\mathcal H_2\) cannot increase its norm. Therefore
\[
 \|E_{12}\|_{\rm op}\le\tfrac12\|E\|_{\rm op}.
\]
Applying this to \(E_N\) proves the requested estimate, at every prefix:
\[
 \|K_N-(S_N)_{12}\|_{\rm op}
 \le\frac{D_N}{2}
 \le\frac{A_N}{P+1}.
\]
Also \(\operatorname{rank}(S_N)_{12}\le\operatorname{rank}S_N\le P\),
and its reverse-action operator is its actual adjoint
\((S_N)_{21}=((S_N)_{12})^*\).

### Additional Hilbert--Schmidt estimate

All operators at a finite prefix have finite rank. For
\(J=\operatorname{diag}(I,-I)\), positivity implies
\[
 \operatorname{tr}(E_N J E_N J)
 =\operatorname{tr}\bigl((E_N^{1/2}J E_N^{1/2})^2\bigr)\ge0.
\]
Expanding the two-by-two blocks gives
\[
 4\|(E_N)_{12}\|_{\rm HS}^2
 \le\operatorname{tr}(E_N^2)
 \le\|E_N\|_{\rm op}\operatorname{tr}E_N
 \le(P+1)D_N^2.
\]
Consequently,
\[
 \|K_N-(S_N)_{12}\|_{\rm HS}
 \le\frac{A_N}{\sqrt{P+1}}.
\]
Both constants are attained: take \(P+1\) positive increments of equal
weight \(a\), with respective orthonormal systems \((u_j)\) and \((v_j)\).
Their joint vectors are orthogonal and their joint covariance eigenvalues
are all \(2a\). At the first shrink, all directions vanish, so \(S_{P+1}=0\).
The resulting \(K_{P+1}\) has \(P+1\) singular values equal to \(a\),
and \(A_{P+1}=(P+1)a\).

## 3. Edge cases, storage, and limits of the conclusion

- Zero increments do nothing. For \(P=0\), every nonzero appended
  direction is immediately removed, so \(S_N=0\); the inequalities
  still hold.
- Eigenvalue ties are harmless in exact arithmetic. The support
  projector is well defined even when individual eigenvectors are not.
- The recurrence is deterministic and pathwise. It holds even when the
  incoming stream depends on the current sketch, its previous outputs,
  or other causal randomness. The comparison is against the sum of
  that realized stream. It is not a comparison with the increments of
  some different uncompressed evolution.
- The accumulation \(A_N=\sum_j|a_j|\) belongs to that realized stream.
  For an evolving compressed model it is its own accumulated weight,
  say \(\widetilde A_N\). The bound \(A(T)\le R^2T^2/2\) from the
  separate gradient-flow lemma uses the exact energy-dissipating flow
  and zero initial readout. The sketch's evolution does not automatically
  inherit that loss monotonicity or that quadratic-time bound.
- If the supplied increments are canonical weight updates evaluated at
  the current state, the PSD lift compresses those weight updates.
  It is not Euclidean gradient training of freely parametrized factors
  \(U,M,V\); such a parametrization generally induces different weight
  dynamics and would require a separate argument.
- A spectral representation stores at most \(P\) joint vectors and their
  eigenvalues, temporarily \(P+1\) at an update. Low-dimensional Gram or
  eigensystem bookkeeping can use \(O(P^2)\) scalars. No previous stream
  vectors need be retained. In dimension \(n\) per block this is
  \(O(nP+P^2)\) scalar storage. At population level, \(O(P)\) Hilbert
  vectors is not by itself a finite scalar representation or a cost bound.
- With finite normalized population inner products, rank-one operators
  include their inner-product normalization. For example,
  \(u\otimes v=uv^\top/n\) when both blocks use
  \(\langle\cdot,\cdot\rangle_n\). The direct-sum convention above ensures
  \(\|z_j\|^2=2|a_j|\). Normalizing the concatenated vector instead by
  \(1/(2n)\) without compensating factors would change the constants and
  the represented off-diagonal block.
- These are exact-arithmetic statements. Numerical rank decisions,
  accumulated roundoff, and approximate queries require their own error
  accounting.
- Neither primitive establishes stable coupling to the dense gradient
  flow, a population limit, bounded query growth, an autonomous solver,
  or convergence and efficiency as dictionary order increases.

No algebraic correction to either supplied primitive is necessary.
Their stated scope must retain the information restriction in the Gaussian
lemma and the realized-stream comparison in the streaming lemma.

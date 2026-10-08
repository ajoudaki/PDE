# Unbounded Gaussian-response blocks without history-gap constants

2026-10-07. Lead quantitative refinement for the candidate's dense-reference
bridge. This extends the one-reciprocal-block result to unbounded row fields
with a linear Gaussian value envelope. It does not require a covariance
lower bound or a uniformly bounded reverse-query vector.

The proof uses Gaussian conditioning and the covariance-factor lemma of
GAP_FREE_RESPONSE_STEP.md, whose complete proof was read. All additional
truncation, coupling and moment estimates are supplied here. Truncation is
only a proof coupling: the actual query circuit and target response law
remain unclipped. No new label assumption is made.

## 1. A covariance coupling with explicit Gaussian tails

Let \(g_1,\ldots,g_n\) be independent standard Gaussian vectors in
\(\mathbb R^r\), with \(r\ge1\), and let \(v_i=v(g_i)\in\mathbb R^\ell\).
Assume the pointwise bound
\[
 \|v(g)\|\le A(1+\|g\|),\qquad A<\infty .
 \tag{1}
\]
No derivative assumption is needed in this section. Write
\[
 T=\mathbb E[vv^\top],\qquad T_n=\frac1n\sum_i v_iv_i^\top,
 \qquad r_D=\operatorname{rank}T .
\]
There is a joint construction of centered Gaussian vectors \(\xi_n,\xi\)
such that the conditional covariance of \(\xi_n\) given the whole root
sample is \(T_n\), the vector \(\xi\) has covariance \(T\) and is independent
of that whole sample, and
\[
 \mathbb E\|\xi_n-\xi\|^2
 \le \frac{A^2}{n}
 \left[2+(1+R)\sqrt{r_D}\right]^2,
 \qquad
 R=\sqrt{8\log(8n)+4r\log2}.
 \tag{2}
\]
There is no reciprocal covariance eigenvalue in (2).

### 1.1. The population tail, not merely a sample maximum

Put \(s=\|g\|^2\). The inequalities
\[
 (1+\sqrt s)^2\le2(1+s),\qquad
 (1+s)e^{-s/8}\le4,\qquad s\ge0
\]
give
\[
\begin{aligned}
 \tau_R
 &:=
 \mathbb E\big[\|v(g)\|^2\mathbf1_{\{\|g\|>R\}}\big]\\
 &\le 8 A^2 e^{-R^2/8}\mathbb E e^{\|g\|^2/4}
 =8 A^2 e^{-R^2/8}2^{r/2}
 = A^2/n .
\end{aligned}
\tag{3}
\]
For the middle scalar inequality, the maximum occurs at \(s=7\) and is
\(8e^{-7/8}<4\). The Gaussian exponential moment follows by multiplying
the elementary one-dimensional integrals. Thus (3) is a genuine population
bias bound, not an inference from all sampled values lying in a ball.

### 1.2. Three coupled Gaussian pairs

Set \(v_R=v\mathbf1_{\{\|g\|\le R\}}\), and define its population and
sample covariances \(T_R,T_{n,R}\).
This auxiliary vector is bounded by \(A(1+R)\).
The covariance-factor lemma supplies a coupling
\((\xi_{n,R},\xi_R)\) with
\[
 \mathbb E\|\xi_{n,R}-\xi_R\|^2
 \le A^2(1+R)^2\operatorname{rank}(T_R)/n,
 \tag{4}
\]
where \(\xi_R\) is independent of the full root sample. Independence from
the full sample, not just the truncated vectors, follows by implementing
the lemma with a fresh Gaussian vector independent of all \(g_i\).
Every null direction of \(T\) annihilates \(v\) almost surely and hence
annihilates \(v_R\). Therefore
\(\operatorname{rank}(T_R)\le r_D\).

Conditional on the root sample, consider the centered Gaussian block
covariance obtained from the empirical pairs \((v_i,v_{R,i})\):
\[
 \frac1n\sum_i
 \begin{pmatrix}v_i\\v_{R,i}\end{pmatrix}
 \begin{pmatrix}v_i\\v_{R,i}\end{pmatrix}^{\!\top}.
\]
It is positive semidefinite. Extend the already constructed
\(\xi_{n,R}\) to a joint Gaussian pair \((\xi_n,\xi_{n,R})\) with this
block covariance, using an additional fresh Gaussian vector.
Gaussian regression on the support of \(T_{n,R}\), with its null directions
omitted, supplies such an extension even at singular covariance.
The resulting conditional marginal of \(\xi_n\) is exactly \(N(0,T_n)\),
and
\[
 \mathbb E\|\xi_n-\xi_{n,R}\|^2
 =\mathbb E\|v-v_R\|^2=\tau_R.
 \tag{5}
\]

Similarly extend \(\xi_R\) to a Gaussian pair \((\xi,\xi_R)\) using the
deterministic population block covariance of \((v,v_R)\).
The extension uses independent fresh randomness and deterministic
coefficients. Since \(\xi_R\) is independent of the full root sample,
so is \(\xi\), and
\[
 \mathbb E\|\xi-\xi_R\|^2=\tau_R.
 \tag{6}
\]
One need not assert that the *whole* four-vector is jointly Gaussian
conditional on the sample: the stated pairwise marginals and costs suffice.
In fact the constructions can be taken conditionally linear Gaussian;
what matters is preserving the exact conditional end marginals.

Minkowski's inequality for the joint \(L^2\) norm, together with
(3)--(6), gives
\[
 (\mathbb E\|\xi_n-\xi\|^2)^{1/2}
 \le2\sqrt{\tau_R}
   +A(1+R)\sqrt{r_D/n},
\]
which proves (2).
Independent copies of the auxiliary Gaussian seeds give any number of
rows, independent conditional on the shared root sample. The population
end rows are independent of that sample and of each other.

If \(r=0\), the vector \(v\) is deterministic, its sample covariance is
exactly \(T\), and identical Gaussian end variables give zero cost.
The case \(T=0\) is likewise zero. These trivial cases need no logarithmic
construction.

## 2. One reciprocal matrix block with actual unbounded fields

Let \(H\in\mathbb R^{n\times k}\) be independent of the initialized
Gaussian matrix \(G\), whose entries have law \(N(0,1/n)\). Work
conditionally on \(H\), and put
\[
 Q=H^\top H/n,\qquad Y=GH .
\]
Let \(r_H=\operatorname{rank}Q\). Each upper row has a realization
\(Y_i=L g_i^{(1)}\), with \(LL^\top=Q\) and \(g_i^{(1)}\) standard
Gaussian of dimension \(r_H\). Auxiliary row roots are functions of
independent Gaussian coordinates \(g_i^{(2)}\).
Write \(g_i=(g_i^{(1)},g_i^{(2)})\in\mathbb R^r\).

The fixed reverse-query circuit gives \(D_i=\Psi(Y_i,Z_i)\).
Assume Gaussian integration by parts is valid for \(\Psi\), for example
it is \(C^1\) in \(Y\) with derivatives of polynomial growth in these
Gaussian roots. Assume its *actual*, untruncated values obey
\[
 \|\Psi(Lg^{(1)},Z(g^{(2)}))\|
 \le A(1+\|g\|).
 \tag{7}
\]
The constants \(A,r\) are supplied bounds. They may depend on the fixed
circuit and on an upper bound for the covariance/operator norms, but must
not conceal reciprocal history eigenvalues if a gap-free family claim is
desired. Coefficients may be fixed functions of \(H\); they are not
fitted using the same realized upper rows in this theorem.

Define, using the actual unbounded circuit,
\[
 R_{aj}=\mathbb E[\partial_{Y_a}\Psi_j(Y,Z)],\qquad
 T=\mathbb E[\Psi(Y,Z)\Psi(Y,Z)^\top],\qquad r_D=\operatorname{rank}T.
\]
Then the exact dense return \(G^\top D\) admits a coupling to
\[
 \overline X=HR+\Xi
\]
where the rows of \(\Xi\) are independent \(N(0,T)\), independent of all
upper fields/roots conditional on \(H\), and
\[
 \mathbb E\!\left[
 \frac1n\|G^\top D-\overline X\|_F^2\,\middle|\,H\right]
 \le\frac{A^2}{n}
 \left\{4r_H(r+2)+
       \left[2+(1+R_n)\sqrt{r_D}\right]^2\right\},
 \quad
 R_n=\sqrt{8\log(8n)+4r\log2}.
 \tag{8}
\]
Exact singular and arbitrarily nearly singular \(Q,T\) are allowed.
No uniform bound on
\(\mathbb E[\|D\|^2 D^\top T^\dagger D]\)
is required.

### 2.1. Conditional Gaussian decomposition and Stein response

Let \(P_H\) project onto the columns of \(H\).
The exact conditioning identity is
\[
 G^\top D=
 H Q^\dagger \frac{Y^\top D}{n}
 +(I-P_H)\Xi_n,\qquad
 \operatorname{Cov}(\Xi_{n,i}\mid H,Y,Z)=D^\top D/n .
 \tag{9}
\]
Use Section 1 to couple each row of \(\Xi_n\) to a population-covariance
row of \(\Xi\). Its proof uses the complete upper Gaussian root sample;
thus the required population-end independence in (9) is preserved.

Singular Gaussian integration by parts gives
\(\mathbb E[Y\Psi^\top]=QR\). Hence the mean error, measured after it
acts on the real query matrix, has conditional squared RMS expectation
at most
\[
 \frac1n\,\mathbb E[
       \|Q^{\dagger/2}Y\|^2\|\Psi(Y,Z)\|^2].
 \tag{10}
\]
Choose the minimal Gaussian root representation so that
\(\|Q^{\dagger/2}Y\|^2=\|g^{(1)}\|^2\).
By (7),
\[
\begin{aligned}
 \mathbb E[
       \|Q^{\dagger/2}Y\|^2\|\Psi(Y,Z)\|^2]
 &\le2A^2\mathbb E[\|g^{(1)}\|^2(1+\|g\|^2)]\\
 &=2A^2 r_H(r+3).
\end{aligned}
\tag{11}
\]
The last equality follows from independence of the root coordinates and
their Gaussian second/fourth moments:
\(\mathbb E\|g^{(1)}\|^2=r_H\) and
\(\mathbb E[\|g^{(1)}\|^2\|g\|^2]=r_H(r+2)\).
It contains no eigenvalue of \(Q\).

Likewise
\[
 \operatorname{tr}T
 \le2A^2(1+r).
 \tag{12}
\]
The population Gaussian projection loss has conditional squared RMS mean
\(r_H\operatorname{tr}T/n\).

### 2.2. Putting the orthogonal errors together

Exactly as in the bounded-block proof, write the return difference as
\[
 H\left(Q^\dagger Y^\top D/n-R\right)
 -P_H\Xi+(I-P_H)(\Xi_n-\Xi).
\]
The last term is spatially orthogonal to the first two.
The expected cross term between the first two vanishes because \(\Xi\)
is centered and independent of the upper sample conditional on \(H\).
Thus its conditional squared RMS expectation is at most the sum of
(10), the projection loss, and the covariance coupling cost (2).
Equations (11)--(12) sum to \(4A^2r_H(r+2)/n\), proving (8).

This is a coupling of exact dense-program marginals. Given the constructed
\(\Xi_n\), complete the Gaussian matrix with
\[
 \widetilde G^\top=\Xi_nD^\dagger+
       W^\top(I-P_D),\qquad
 G=YH^\dagger+\widetilde G(I-P_H),
\]
using an independent variance-\(1/n\) Gaussian matrix \(W\).
Conditional Gaussian projections verify the original iid Gaussian
marginal and the specified actual matrix answers. The coupling does not
claim that the target primitive \(\Xi\) is independent of the entire
realized \(G\).

## 3. What has and has not been removed

For fixed circuit/root dimensions and a uniform linear Gaussian envelope,
(8) is a root-width RMS estimate with a square-root logarithmic loss.
Markov's inequality gives the explicit fixed-confidence bound
\[
 \mathbb P\left\{\|G^\top D-HR-\Xi\|_{F,n}>
       \sqrt{\frac{A^2}{n\delta}
       \left(4r_H(r+2)+[2+(1+R_n)\sqrt{r_D}]^2\right)}
       \,\middle|\,H\right\}\le\delta .
\]
This is not a polynomially small failure probability with only logarithmic
loss unless a further concentration theorem supplies it.

The original unbounded activation class is not replaced by a bounded
activation. Only the proof couples through a bounded intermediate
Gaussian covariance. Both response means \(R\) and end covariances \(T\)
remain those of the actual untruncated circuit.

The remaining restrictions are real: an independent forward batch,
one reverse batch, fixed shared coefficients during that block, and a
supplied linear Gaussian envelope. A second adaptive direction switch or
full training history still needs its own coupling argument.
Controlling envelope constants and root dimensions as history grows is
not established here. Nor is a full-trajectory bias or fluctuation theorem.

This removes one specific impediment to extending gap-free comparison to
the admitted activation class; it does not declare the global goal solved.


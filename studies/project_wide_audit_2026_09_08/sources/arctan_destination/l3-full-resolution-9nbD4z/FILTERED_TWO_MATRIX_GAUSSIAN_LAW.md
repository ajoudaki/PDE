# Exact two-matrix Gaussian law for the filtered algorithm

Status: candidate proof, not yet independently audited.
This note proves a finite-dimensional equality in distribution for the
actual causal filtered recursion. Its canonical consequence remains a
CLIPPED finite-width approximation, not the uncut population theorem.

The algorithm and its parameters are exactly those in
CAUSAL_FILTERED_QUERY_RANK.md. Its canonical-clipped state comparison
is FILTERED_QUERY_CLIPPED_STABILITY.md, and its growing-cap consequence
is FILTERED_QUERY_GROWING_CLIP_TRANSFER.md. Their final hashes are
recorded at the end. The proof below does not assume any Gaussian
comparison theorem. The construction is the centered one-component,
one-query-column, real-parameter-zero specialization motivated by
[Panahi v1, equations (8)--(9)](https://arxiv.org/pdf/2603.09310v1#page=3).
Neither that paper's Theorem 1, its asymptotic theorem, nor its unproved
complex-continuation claim is a premise.

We prove the covariance identity explicitly, then apply an elementary
sequential Gaussian-conditioning lemma. Consequently merely Lipschitz
clipping suffices: no formal derivatives of the query maps or limiting
covariances are taken.

## 1. The two declared query rules

Fix \(n,K\ge1\) and \(\sigma>0\). For the moment consider a single
matrix. Its raw reverse and forward query vectors are \(v_l,h_l\)
at calls \(1\le l\le K\). Set
\[
 \theta_l=v_l/\sqrt n,\qquad \omega_l=h_l,\qquad
 \Theta_l=[\theta_1,\ldots,\theta_l],\quad
 \Omega_l=[\omega_1,\ldots,\omega_l].
\]
Use the positive-diagonal upper Cholesky factors
\[
 A_{\theta,l}^TA_{\theta,l}=\Theta_l^T\Theta_l+\sigma^2I_l,\qquad
 A_{\omega,l}^TA_{\omega,l}=\Omega_l^T\Omega_l/n+\sigma^2I_l.
 \tag{1}
\]
Leading blocks agree across prefixes. The columns
\[
 t_i=(\Theta_l A_{\theta,l}^{-1})_i,\qquad
 s_i=(\Omega_l A_{\omega,l}^{-1})_i/\sqrt n
 \quad(i\le l)
 \tag{2}
\]
therefore do not change with later calls. In particular
\[
 \sum_{i\le l}t_it_i^T\preceq I_n,\qquad
 \sum_{i\le l}s_is_i^T\preceq I_n.
 \tag{3}
\]
For example the first sum equals
\(\Theta_l(\Theta_l^T\Theta_l+\sigma^2I)^{-1}\Theta_l^T\);
its singular-direction eigenvalues are \(d^2/(d^2+\sigma^2)\).

For the original perturbed rule, let \(G_0\) be an \(n\)-by-\(n\)
standard Gaussian matrix, let \(\Gamma\) be \(K\)-by-\(K\) standard
Gaussian, and let \(U_l,V_l\in\mathbb R^n\) be standard Gaussian.
All entries and arrays are independent. With \(W_0=G_0/\sqrt n\),
the two raw outputs are
\[
 \begin{split}
 {\cal R}_l&=G_0^T\theta_l+
       \sum_{i<l}s_i(\Gamma^TA_\theta)_{il}+\sigma U_l,\\
 {\cal F}_l&=G_0\omega_l/\sqrt n+
       \sum_{i\le l}t_i(\Gamma A_\omega)_{il}+\sigma V_l.
 \end{split}
 \tag{4}
\]
Each product at call \(l\) uses its leading \(l\)-by-\(l\) blocks.
These are exactly the raw outputs of the rank note: in its notation
the two displayed Gamma sums are \(\sqrt n\,k_l,\sqrt n\,g_l\).
The reverse sum is strict.

For the replacement rule, sample mutually independent standard
Gaussian matrices \(Z^{\rm for},Z^{\rm rev}\in\mathbb R^{n\times K}\)
and \(\Lambda\in\mathbb R^{K\times K}\). Write \(Z_i^{\rm for}\) and
\(Z_i^{\rm rev}\) for their columns. With the same query maps and the
same factors (1)--(2), but evaluated on this rule's own transcript,
set
\[
 \begin{split}
 {\cal R}_l^{\rm alt}
 &=\sum_{i\le l}Z_i^{\rm rev}A_{\theta,il}
       +\sum_{i<l}s_i\big((Z_i^{\rm for})^T\theta_l+
                                      \sigma\Lambda_{li}\big),\\
 {\cal F}_l^{\rm alt}
 &=\sum_{i\le l}Z_i^{\rm for}A_{\omega,il}
       +\sum_{i\le l}t_i\big((Z_i^{\rm rev})^T\omega_l/\sqrt n+
                                      \sigma\Lambda_{il}\big).
 \end{split}
 \tag{5}
\]
All vector/matrix dimensions and raw width factors are explicit.
In particular both kinds of output are raw \(n\)-vectors, not
the source's forward output divided by \(\sqrt n\).

Assume that \(\theta_l\) is a finite measurable function of past
outputs, and \(\omega_l\) is a finite measurable function of past
outputs and possibly the current reverse output. Thus the order is
\(\theta_l\), reverse output, \(\omega_l\), forward output.
Both (4) and (5) are explicit causal recursions.
The strict reverse triangle means its factors only require earlier
forward queries; a future forward query is not needed to define it.
Positive Gram regularization ensures finite Cholesky factors and
inverses at every finite history.

The claim is equality in law of the entire output transcript, and
hence every measurable state computed from that transcript. The claim
does not preserve \(G_0\) itself as a jointly observed variable.

## 2. Covariance at an arbitrary fixed history

In this section the query vectors are deterministic arbitrary vectors.
This is a calculation of Gaussian processes at a fixed argument, not
conditioning an adaptive transcript and assuming its primitives remain
independent.

For calls \(l,k\), write
\[
 V_\theta(l,k)=\theta_l^T\theta_k+\sigma^2{\bf1}_{\{l=k\}},
 \quad
 V_\omega(l,k)=\omega_l^T\omega_k/n+\sigma^2{\bf1}_{\{l=k\}},
\]
and \(T_m=\sum_{i\le m}t_it_i^T\),
\(S_m=\sum_{i\le m}s_is_i^T\), with \(T_0=S_0=0\).
The Cholesky identities give
\[
 \sum_{i\le \min(l,k)}A_{\theta,il}A_{\theta,ik}
       =V_\theta(l,k),
 \quad
 \sum_{i\le \min(l,k)}A_{\omega,il}A_{\omega,ik}
       =V_\omega(l,k).
 \tag{6}
\]

For (4), independence and equality of the two indices of a common
Gamma entry give
\[
 \operatorname{Cov}({\cal F}_l,{\cal F}_k)
       =V_\omega(l,k)(I_n+T_{\min(l,k)}),
 \tag{7}
\]
\[
 \operatorname{Cov}({\cal R}_l,{\cal R}_k)
       =V_\theta(l,k)(I_n+S_{\min(l,k)-1}).
 \tag{8}
\]
For (7), the \(G_0\) contribution plus the direct noise is
\(V_\omega(l,k)I_n\); the Gamma contribution is
\(\sum_{i\le\min(l,k)}t_it_i^T
  \sum_{j\le\min(l,k)}A_{\omega,jl}A_{\omega,jk}\).
For (8), the outer-product sum is over \(i<\min(l,k)\)
while the \(A_\theta\) sum includes the diagonal. This proves both
identities and their strict/inclusive endpoints.

Define the two vectors, only for the following cross-covariance,
\[
 a_{l,k}=\sum_{i\le\min(l,k)}t_iA_{\theta,ik},\qquad
 b_{l,k}=\sum_{j\le\min(l,k-1)}s_jA_{\omega,jl}.
\]
Then direct index matching in (4) gives
\[
 \operatorname{Cov}({\cal F}_l,{\cal R}_k)
       =\theta_k\omega_l^T/\sqrt n+a_{l,k}b_{l,k}^T.
 \tag{9}
\]
The first term comes from \(G_0\), and the second uses precisely the
common entries \(\Gamma_{ij}\) with
\(i\le\min(l,k)\), \(j\le\min(l,k-1)\).

For (5), the forward-forward covariance of the \(Z^{\rm for}\)
parts is \(V_\omega(l,k)I_n\). The \(Z^{\rm rev}\) parts give
\((\omega_l^T\omega_k/n)T_{\min(l,k)}\), and the Lambda parts give
\(\sigma^2{\bf1}_{\{l=k\}}T_l\). The three arrays are independent,
so their sum is (7). The same calculation in reverse, with its
strict sums, gives (8).

There are two nonzero cross-covariances in (5):
the first forward term against the second reverse term, and the
second forward term against the first reverse term. Their sum is
\[
 \operatorname{Cov}({\cal F}_l^{\rm alt},{\cal R}_k^{\rm alt})
       =\theta_k b_{l,k}^T+a_{l,k}\omega_l^T/\sqrt n.
 \tag{10}
\]
There is no Lambda cross term: matching \(\Lambda_{il}\) with
\(\Lambda_{kj}\) would require \(i=k\le l=j<k\), an impossibility.
For \(l<k\), (2) implies \(b_{l,k}=\omega_l/\sqrt n\).
For \(l\ge k\), it implies \(a_{l,k}=\theta_k\).
These two cases prove that (9) and (10) agree for every \(l,k\),
including \(l=k\).

Thus the full stacked raw output vectors of (4) and (5) have identical
centered Gaussian covariances at every deterministic query history.
That common covariance is strictly positive definite. Indeed the
stacked direct noises \(\sigma U_l,\sigma V_l\) in (4) are independent
of all other terms and give \(\sigma^2 I_{2nK}\) to its covariance.
This argument concerns fixed arguments; it does not assert that the
actual adaptive output vector is jointly Gaussian.

## 3. Sequential covariance matching implies equality in law

Here is the finite Gaussian-conditioning fact needed to pass from the
preceding computation to actual adaptive histories.

Let \(g\) be a finite-dimensional standard Gaussian vector. Suppose
successive vector observations have the form
\[
 y_j=L_j(y_1,\ldots,y_{j-1})g,\qquad 1\le j\le m,
 \tag{11}
\]
where all coefficient matrices are finite measurable functions.
For a prescribed candidate prefix \(y_1,\ldots,y_{j-1}\), stack the
first \(j\) row blocks into \(L_{\le j}(y)\), and suppose
\(K_{\le j}(y)=L_{\le j}(y)L_{\le j}(y)^T\) is positive definite.
The last row block depends on the prefix but not on \(y_j\).
This convention is used in every entry of \(K_{\le j}\).

The conditional distribution of the next observation is Gaussian
with mean and covariance
\[
 K_{j,<j}(y)K_{<j,<j}(y)^{-1}y_{<j},
 \quad
 K_{j,j}(y)-K_{j,<j}(y)K_{<j,<j}(y)^{-1}K_{<j,j}(y).
 \tag{12}
\]
For \(j=1\), the mean is zero.

To prove this, for deterministic \(L\) of full row rank decompose
\[
 g=L^T(LL^T)^{-1}Lg+
       [I-L^T(LL^T)^{-1}L]g.
\]
The two Gaussian terms have zero cross covariance and hence are
independent; this follows, for example, by factorization of their
joint Gaussian characteristic function. Therefore conditioning on
\(Lg=y\) gives a Gaussian with mean
\(L^T(LL^T)^{-1}y\) and covariance
\(I-L^T(LL^T)^{-1}L\).

Apply this argument first to the first observation. Inductively,
given the previous observations, the next matrix \(L_j(y_{<j})\)
is fixed, so conditioning the current Gaussian posterior on this
next linear observation gives (12). The same update gives posterior
mean \(L_{\le j}^TK_{\le j}^{-1}y_{\le j}\) and covariance
\(I-L_{\le j}^TK_{\le j}^{-1}L_{\le j}\): these identities can be
checked using the block inverse of
\[
 K_{\le j}=
 \begin{pmatrix}K_{<j,<j}&K_{<j,j}\\K_{j,<j}&K_{j,j}\end{pmatrix}
\]
and its Schur complement appearing in (12).
All inverses are measurable, and the positive Schur complements give
ordinary Gaussian conditional densities. This constructs the
conditional kernels inductively, including outside any particular
realized prefix. No assumption of independence of \(g\) from past
observations was used at the inductive step.

Consequently two recursions of the form (11), possibly with Gaussian
vectors of different dimensions, have the same transcript law whenever
their fixed-argument covariance matrices \(K_{\le j}(y)\) agree for
every prefix. Their first conditional kernels agree; (12) makes every
subsequent kernel agree, so iterated integration gives the same joint
law. Independent non-Gaussian initialization can be retained jointly
by first fixing its value and then integrating this equality.

This lemma needs only measurable causal coefficient matrices. It does
not infer a frozen Gaussian isometry for an adaptive output norm.

## 4. Apply the lemma to both interacting matrices

Run the full filtered recursion of the rank note. Its independent
non-matrix seeds are \(z^{(1)}_0\) and \(W^{(4)}_0\), with exactly their
canonical laws. For each matrix label \(b=2,3\), supply an independent
copy of (4), or an independent copy of (5). The two collections of
primitive Gaussian arrays are independent of one another and of these
non-matrix seeds.

Order the output blocks as follows: lower reverse/forward warmup,
upper reverse/forward warmup, and then at each update the lower
reverse/forward pair followed by the upper reverse/forward pair.
The algorithm counts discarded reverse warmup outputs in this list
although its state does not use them.

For each fixed full candidate transcript and fixed non-matrix seeds,
the algorithm determines every query by its previous outputs. At
each update all four arguments are selected from the pre-step state.
The upper warmup forward argument is the activation of the earlier
lower warmup output, so it also obeys this ordering. Every learned
matrix and the returned memory is a finite sum of earlier factors.
There is no direct access to \(W^{(2)}_0,W^{(3)}_0\) outside the
declared calls. This is the measurability property already proved
in the rank note; it holds for every hypothetical finite transcript,
not only for realized outputs.

At a fixed transcript, every output block is a linear function of
the finite vector of all primitive Gaussian entries, with coefficients
depending only on preceding blocks. For (4), the extra direct noise
has coefficient \(\sigma I_n\); for (5), expand the displayed linear
sums. The two matrices' cross covariances are zero at that fixed
argument because their primitive arrays are independent.
Within either matrix, equations (7)--(10) give identical covariances.
These equalities persist for every leading chronological prefix.

The stacked covariance of the original perturbed rule is at least
\(\sigma^2 I\), also on every prefix. The sequential lemma therefore
applies in the combined output space, without pretending that one
matrix's adaptive transcript is an independent seed for the other.
It proves equality in law of the ENTIRE coupled output transcript
for the all-original and all-replacement algorithms, jointly with
\(z^{(1)}_0,W^{(4)}_0\).

Every state register, learned increment, forward activation and middle
backward query computed from this transcript has the same joint law.
In particular both learned matrices and the strict pre-step returned
memory are preserved as computed states. The INITIAL hidden matrices
themselves are not asserted to survive as observed coordinates in the
replacement law. Nor are cross-process pathwise equalities asserted.

The result holds for every finite \(n,K,\sigma>0\) and every fixed
allowed clipping map, even if \(K\) grows with width. No limit or
width-uniform differentiability constant enters this exact equality.
It includes the rank note's identity map at this distributional
level, without asserting its uncut stability.

## 5. The actual conditional innovation in the middle query

Now work in the all-replacement realization. Use matrix label three
in (1)--(5). At a mesh step \(j\), its call is \(l=j+2\), and
\(\theta_l=\delta_j^{(3)}/\sqrt n\),
\(\omega_l=h_j^{(2)}\), exactly as in the rank note.

Let the past immediately before this upper reverse call contain the
non-matrix seeds, both matrices' earlier revealed primitives, and
the already computed current lower pair. The current upper queries
were pre-step queries. Reveal upper primitives at each reverse call
by taking \(Z_l^{\rm rev}\) and the row entries \(\Lambda_{li},i<l\);
at each forward call reveal \(Z_l^{\rm for}\) and
\(\Lambda_{il},i\le l\). This is an acyclic reveal order.
The current lower pair depends on upper primitives only through
earlier upper outputs, so it reveals no fresh upper primitive.

Set
\[
 \begin{split}
 m_l^{(2)}
 &=\sum_{i<l}Z_i^{{\rm rev},(3)}A_{\theta,il}^{(3)}
       +\sum_{i<l}s_i^{(3)}
                  (Z_i^{{\rm for},(3)})^T\theta_l^{(3)},\\
 \nu_l^{(2)}
 &=A_{\theta,ll}^{(3)}Z_l^{{\rm rev},(3)}
                 +\sigma\sum_{i<l}s_i^{(3)}\Lambda_{li}^{(3)}.
 \end{split}
 \tag{13}
\]
All coefficients and the first vector in (13) are measurable from
this past. The second vector is conditionally centered Gaussian with
\[
 \operatorname{Cov}(\nu_l^{(2)}\mid\text{past})
 =(A_{\theta,ll}^{(3)})^2 I_n
             +\sigma^2\sum_{i<l}s_i^{(3)}(s_i^{(3)})^T.
 \tag{14}
\]
This is a statement about joint conditional covariance, not iid
coordinates: the second term need not be diagonal.

The raw reverse output is \(m_l^{(2)}+\nu_l^{(2)}\). Including all
learned upper memory, the middle query is exactly
\[
 q_j^{(2)}
 =m_{j+2}^{(2)}+(M_j^{(3)})^T\delta_j^{(3)}
                    +\nu_{j+2}^{(2)}.
 \tag{15}
\]
There is no omission of the trained part of \(W^{(3)}\).

For \(T=N\eta\le S+1\), on the non-matrix initial event
\(\|W^{(4)}_0\|_\infty\le1\), bounded activation alone gives
\[
 \|W^{(4)}_j\|_\infty\le B_4:=1+(S+1)\pi/2,\qquad
 \|\delta_j^{(3)}\|_2/\sqrt n\le B_4.
 \tag{16}
\]
The Schur-complement diagonal satisfies
\[
 (A_{\theta,ll}^{(3)})^2
 \le\|\theta_l^{(3)}\|_2^2+\sigma^2\le B_4^2+\sigma^2.
\]
Together with (3), this gives the actual innovation bound
\[
 \operatorname{Cov}(\nu_l^{(2)}\mid\text{past})
       \preceq(B_4^2+2\sigma^2)I_n.
 \tag{17}
\]
For every coordinate \(i\), every real \(\lambda\), and every such
past, the Gaussian characteristic/density calculation therefore yields
\[
 \mathbb E[e^{\lambda\nu_{l,i}^{(2)}}\mid\text{past}]
 \le\exp\!\big((B_4^2+2\sigma^2)\lambda^2/2\big),
 \tag{18}
\]
and Markov's inequality optimized in \(\lambda\) gives
\[
 \mathbb P(|\nu_{l,i}^{(2)}|>x\mid\text{past})
 \le2\exp\!\left(-\frac{x^2}{2(B_4^2+2\sigma^2)}\right).
 \tag{19}
\]
The constants are independent of clipping, mesh, filter scale and
query count for a fixed feature horizon and bounded \(\sigma\).
The initial event has probability at least \(1-2ne^{-n^2/2}\).

The learned term in (15) also has a pointwise bound:
\[
 (M_j^{(3)})^T\delta_j^{(3)}
 =\frac{\eta}{n}\sum_{r<j}h_r^{(2)}
                         (\delta_r^{(3)})^T\delta_j^{(3)},
\]
so, for every coordinate,
\[
 \left|[(M_j^{(3)})^T\delta_j^{(3)}]_i\right|
 \le (S+1)(\pi/2)B_4^2.
 \tag{20}
\]
This uses the actual trained update and actual bounded top backward
fields; it is not a frozen-weight replacement.

The unbounded remaining conditional mean is exactly \(m_l^{(2)}\).
Its coefficients depend on earlier Gaussian outputs. In particular
(17)--(20) do not give a Gaussian law, coordinate independence, or
a clipping-uniform tail for the complete query (15).
A union bound over all calls would also introduce the growing call
count; a fixed-call innovation tail is not a uniform path-tail theorem.

## 6. Consequence for canonical clipped trajectories

Take now exactly the parameters of the three proved comparison notes:
\(\eta=n^{-2}\), \(N=\lceil Sn^2\rceil\),
\(\sigma=n^{-1/4}\), \(\varepsilon=n^{-1/8}\), and a prescribed
deterministic common map with cap \(R_n\ge1\), \(R_n=o(\log n)\).
Let the reference be the canonical CLIPPED finite-width feature flow
with the original independent Gaussian matrices and tiny readout.

The growing-cap note gives a coupling of this reference with the
all-original perturbed algorithm whose mesh-state distance tends to
zero in probability, with good-event error \(n^{-1/24+o(1)}\).
The deterministic stability proof also gives, at each \(0\le j<N\),
\[
 \frac{\|\widehat q_j^{(2)}-q^{(2)}(s_j)\|_2}{\sqrt n}
 \le C_S\big(E_j+C_j\big)+b,
 \tag{21}
\]
where \(E_j\) is its slow-state error, \(C_j\) its layer-three error,
and \(b\) its raw query-error bound. Its constant is independent of
\(R_n\): only the subsequent middle gate subtraction introduces the
clipping factor. Thus the same coupling controls the state distance
augmented by the maximum of (21), still at rate
\(n^{-1/24+o(1)}\) on the good event.

Define this augmented distance as the sum of the mesh-state distance
in the growing-cap note and the maximum middle-query error over
\(j<N\), with ordinary vector norms divided by \(\sqrt n\) and
ordinary Frobenius norms for learned matrices. The non-matrix seeds
may also be retained as jointly identical coordinates.

For every test of these augmented arrays that is bounded in absolute
value by one and 1-Lipschitz for this distance, the difference between
its canonical-clipped expectation and its all-replacement expectation
is at most
\[
 n^{-1/24+o(1)}
 +2\big(4e^{-(8-2\log9)n}+2ne^{-n^2/2}+5n^{-2}\big).
 \tag{22}
\]
Indeed compare reference and all-original paths on the proved coupling.
On its good event the test difference is bounded by the distance;
on the complement it is at most two. Section 4 identifies the
all-original expectation with the all-replacement expectation exactly.
Constants can be absorbed into the \(o(1)\) exponent.
No unbounded test, uniform integrability, or exchange of limits is
needed for this conclusion.

Thus the replacement process gives a rigorously connected
finite-width Gaussian-array representation of the canonical CLIPPED
state and middle query on the full growing training mesh.
This does not imply convergence to a fixed population law as \(n\)
changes. In particular (22) does not carry conditional law statements
or arbitrary discontinuous tail indicators to the canonical flow.

The identity map is allowed in the exact finite law and innovation
bounds, but not in the canonical-clipped comparison (22).
The present note supplies no bound on the predictable response
\(m_l^{(2)}\), no uncut clipping removal, no population uniqueness or
autonomous restart, and no physical-time/exact-GD/kernel/velocity
convergence. These remain the original global obligations.

## Frozen dependencies

CAUSAL_FILTERED_QUERY_RANK.md:
7406ffb9c24e8359e7e188c70eb3863ff5aeb9179df3d7bba92103b98aedcfd1.

FILTERED_QUERY_CLIPPED_STABILITY.md:
cecfa8670609c13b345d2c73f1a2c772082fe1253f684ab0db4e345d82b2094b.

FILTERED_QUERY_GROWING_CLIP_TRANSFER.md:
c1d5d50c8720cb3285c3aa15608b08cb9b0bfde968951c33cbe0338df1548fcd.

No experiment, source-task resumption, or replacement of the canonical
initialization/dynamics has been performed.


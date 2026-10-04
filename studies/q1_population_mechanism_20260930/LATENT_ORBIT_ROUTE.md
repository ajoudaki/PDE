# Frozen route: tetrahedral geometry obstructs first-layer XOR dominance

Status: first bounded round, candidate exact theorem with a complete elementary
proof; self-checked, not independently reviewed or promoted. No experiment,
finite-neuron training, external retrieval, or other research route was used.

Scientific input scope: the supervisor's self-contained q1 population equations,
canonical initial Gaussian source law, and assumed regular unique equivariant
population flow. Required process inputs were root `AGENTS.md`, workflow Part 1,
and the investigate-conjectures and solve-math-rigorously skills and applicable
research-contract, adversarial-audit, and proof-search references. No book,
other-study, study-history, or other-route scientific input was read.

## Contract and result

Use exactly four unit inputs and their natural XOR labels:

\[
 u_{st}=(s,t,1)/\sqrt3,\qquad y_{st}=st,
 \qquad (s,t)\in\{-1,1\}^2.
\]

The first-layer feature is \(H_{st}(A)=\tanh(A\cdot u_{st})\). For
\(\chi\in\{1,s,t,y\}\), define its sample Walsh coefficient and population energy

\[
 h_\chi(A)=\tfrac14\sum_{s,t}\chi(s,t)H_{st}(A),
 \qquad E_\chi(t)=\langle h_\chi(A_t)^2\rangle_1.
\]

These observables have a fixed scientific interpretation: `s` and `t` are the
two input-generating latent bits; `y=st` is the supervised XOR. They are specified
before looking at a learned state. A population linear decoder of a latent bit
uses a weight \(b\in L^2(\Omega_1)\) and predicts
\(\langle bH_{st}\rangle_1\). Its minimum squared norm is an operational measure
of accessibility, not an arbitrary symmetry statistic.

**Theorem (conditional on the supplied population-flow existence/equivariance).**
At every time at which that flow exists with finite-valued first-layer weights,

\[
 E_1=E_s=E_t=:L,\qquad E_y=:S\le L.
\]

If the first layer is nonzero on a set of positive population measure, then
\(S<L\). In particular, any nonzero fitted output implies \(L>0\): neither
primitive bit has disappeared from the first-layer representation. Both bits
have exact population linear decoders of squared norm \(1/L\). When \(S>0\),
the XOR has an exact first-layer linear decoder of squared norm \(1/S>1/L\);
when \(S=0\), no first-layer linear decoder can represent the XOR.

Consequently, even conditional on perfect fitting or a zero-loss endpoint, the
first layer cannot become an XOR-dominant representation or discard the primitive
factors in this precise linear-accessibility sense. The actual q1 flow fits the
labels increasingly well on some nonzero initial time interval, so the conclusion
is compatible with nontrivial training from the stated zero readout.

The spectral bound is sharp among tetrahedrally invariant feature populations.
Approaching \(S/L=1\) forces the feature energy to leave every bounded region of
first-layer weight space. The sharp construction uses saturated one-versus-three
gates. This is a geometric endpoint constraint, not a claim that the flow reaches
that endpoint.

This result is about the **first layer**. It does not assert latent suppression
or domination at the second layer, perfect fitting at infinite time, or global
existence. It does not identify a mere loss decrease as feature learning.

## Proof

### 1. Exact signed-input gauge and tetrahedral symmetry

Write \(p_a=y_au_a\), and replace the training labels by \(+1\). Define

\[
 H'_a=y_aH_a,\quad K'_a=y_aK_a,\quad V'_a=y_aV_a,
 \quad Z'_a=y_aZ_a,\quad G'_a=y_aG_a,
 \quad F'_a=y_aF_a,\quad r'_a=y_ar_a.
\]

Keep \(A,W,\tau,T,T^*\) unchanged. Oddness of tanh gives the formulas for
\(H',G'\). Linearity of \(T\) gives

\[
 TH'_a+\tfrac14\sum_bV'_b\langle K'_bH'_a\rangle_1
 =y_a\left(TH_a+\tfrac14\sum_bV_b\langle K_bH_a\rangle_1\right).
\]

The backward quantities are unchanged:
\(D'_a=W(1-(G'_a)^2)=D_a\), and

\[
 L'_a=(1-(H'_a)^2)
 \left[T^*D'_a+\tfrac14\sum_bK'_b\langle V'_bD'_a\rangle_2\right]=L_a.
\]

Thus \(r'_ap_a=r_au_a\), \(r'_aG'_a=r_aG_a\), and every supplied evolution
equation is carried exactly into its all-positive-label counterpart. This also
preserves \(W_0=V_0=0\), \(K_0=H_0\), and the clock equation.

Here

\[
 p_{st}=(t,s,st)/\sqrt3,\qquad
 \sum_{s,t}p_{st}=0,\qquad
 p_a\cdot p_b=-1/3\quad(a\ne b).
\]

Every permutation of these four vertices is implemented by an orthogonal map:
the permutation preserves their Gram matrix, and the only linear relation among
the four spanning vectors is their sum zero, so sending each vertex to its
permuted vertex defines an inner-product-preserving linear map of \(\mathbb R^3\).
The isotropic Gaussian initialization, canonical source law, and the stipulated
equivariance/uniqueness give an exchangeable signed feature law at every existing
time. In particular its Gram matrix has diagonal \(d\) and off-diagonal \(e\).

The signed mean is \(h_y\). The three original Walsh functions \(1,s,t\)
become three orthogonal contrasts after the gauge. Therefore

\[
 S=\frac{d+3e}{4},\qquad
 E_1=E_s=E_t=\frac{d-e}{4}=L,
\]

and all distinct Walsh coefficients are orthogonal in population \(L^2\).
The same exchangeability implies \(F_a=y_af\) for a scalar \(f\), but it does
not by itself imply the spectral ordering \(S\le L\). That ordering is the
additional nonlinear geometric fact proved next.

### 2. A strict cone inequality for every finite tanh tetrahedron

Let \(x_1+\cdots+x_4=0\), and put \(v_i=\tanh x_i\). Then

\[
 \left(\sum_{i=1}^4v_i\right)^2\le\sum_{i=1}^4v_i^2,
 \tag{1}
\]

with strict inequality unless all \(x_i=0\).

Here is a proof including zero coordinates. The identity
\(\tanh(a+b)=(\tanh a+\tanh b)/(1+\tanh a\tanh b)\)
for \(a,b\ge0\) implies both monotonicity and subadditivity of tanh on the
nonnegative half-line. Let \(p_1,\ldots,p_k\) denote the positive entries of
\(v\), and \(-q_1,\ldots,-q_l\) its negative entries, with
\(P=\sum p_i\), \(Q=\sum q_j\). If the vector is nonzero, then \(k,l\ge1\)
and \(k+l\le4\). Reverse all signs if necessary so that \(P\ge Q\).

The equality of total positive and negative preactivation implies

\[
 p_i\le\tanh\!\left(\sum_j\operatorname{artanh}q_j\right)\le Q.
 \tag{2}
\]

If \(P=Q\), (1) is strict immediately. Suppose \(P>Q\). Then \(k=1\)
is impossible, since (2) would give \(P\le Q\). If \(k=2\), then
\(P\le2Q\), hence

\[
 (P-Q)^2\le P^2/4<P^2/2\le\sum_i p_i^2\le\sum_i v_i^2.
\]

If \(k=3\), then \(l=1\); write its only negative magnitude as \(q=Q\).
Since the three positive preactivations are strictly positive,
\(q=\tanh(\sum_i\operatorname{artanh}p_i)>\max_i p_i\), so \(P<3q\).
Cauchy's inequality now gives

\[
 (P-q)^2<P^2/3+q^2\le\sum_i p_i^2+q^2.
\]

This proves (1) and its strictness.

Apply (1) to \(x_a=A\cdot p_a\). Their sum is zero and
\(v_a=y_aH_a\). Walsh Parseval gives

\[
 16h_y(A)^2\le4\bigl(h_1(A)^2+h_s(A)^2+h_t(A)^2+h_y(A)^2\bigr),
\]

or

\[
 3h_y(A)^2\le h_1(A)^2+h_s(A)^2+h_t(A)^2.
 \tag{3}
\]

The tetrahedron spans \(\mathbb R^3\), so equality at finite \(A\) occurs
only at \(A=0\). Integrating (3) and using the symmetry in Step 1 gives
\(S\le L\), strictly if \(\mathbb P(A\ne0)>0\). Equivalently, the signed
first-layer off-diagonal Gram entry satisfies \(e\le0\), strictly for any
nonzero finite feature population. Thus the first-layer signed samples remain
anticorrelated even though all the signed training labels are positive.

### 3. Exact latent decoders and noncollapse under fitting

Walsh inversion reads

\[
 H_{st}=h_1+s h_s+t h_t+st h_y.
\]

The orthogonality from Step 1 shows that, for \(E_\chi>0\),
\(b=h_\chi/E_\chi\) predicts \(\chi\) exactly and has squared norm
\(1/E_\chi\). Any other exact decoder satisfies
\(\langle b h_\chi\rangle_1=1\), so Cauchy's inequality gives
\(\|b\|_2^2\ge1/E_\chi\). If \(E_\chi=0\), that inner-product condition
cannot hold. This proves the minimum-norm claims without a pseudoinverse or an
unstated rank hypothesis.

If \(L=0\), (3) and the equality of the three contrast energies imply
\(H_a=0\) almost surely for all four samples. The actual forward definition
then gives \(Z_a=T0+\tfrac14\sum_bV_b\langle K_b0\rangle_1=0\), hence
\(G_a=F_a=0\). Thus any nonzero output, in particular any nonzero interpolating
output, requires \(L>0\). This is a statement about the full supplied q1
architecture, including its evolving \(V,K\) correction; neither a frozen
feature architecture nor a finite-neuron surrogate was substituted.

### 4. Nonzero training interval from the prescribed initialization

Assume the isotropic Gaussian initialization has variance \(\sigma^2>0\).
Its first-layer covariance is positive definite. Indeed, the four Walsh
coefficients are orthogonal by Step 1; a contrast coefficient is nonzero at
\(A=(a,0,0)\), \(a\ne0\). The label coefficient is nonzero at
\(A=(a,a,a)\), \(a>0\), since with \(r=a/\sqrt3\),

\[
 h_y(A)=\tfrac14(\tanh(3r)-3\tanh r)<0.
\]

The strict inequality follows twice from strict tanh subadditivity for positive
arguments. Continuity and the full support of the initial Gaussian make each
required squared population coefficient strictly positive. Hence all four
eigenvalues of the initial covariance are positive.

The supplied canonical law makes \(Z_0=(TH_a)_a\) a nondegenerate Gaussian
vector. It has positive density everywhere in \(\mathbb R^4\): diagonalizing
its positive covariance represents it as an invertible linear image of four
independent standard Gaussians. The continuous function
\(g_y(z)=\tfrac14\sum_a y_a\tanh z_a\) is not identically zero, so
\(\langle g_y(Z_0)^2\rangle_2>0\).

At time zero, \(W=V=0\), so \(D=L_a=0\),
\(\dot A=\dot V=\dot K=0\), and
\(\dot W=2g_y(Z_0)\). Differentiating the prediction under the assumed
regularity yields

\[
 \dot f(0)=\tfrac14\sum_a y_a\langle\dot W G_a\rangle_2
 =2\langle g_y(Z_0)^2\rangle_2>0.
\]

The normalized squared loss is \((1-f)^2\), initially one. Continuity of
\(\dot f\) gives a positive interval on which \(0<f<1\) and the loss strictly
decreases. The geometric obstruction of Steps 1–3 holds throughout that interval
and every later time on which the assumed flow exists. This calculation only
certifies that the all-time obstruction does not describe a stalled trajectory;
it is not the claimed feature-learning mechanism.

### 5. Sharpness and a quantitative endpoint obstruction

Let \(A=rp_j\), choosing the vertex index \(j\) uniformly, and optionally
randomizing the overall sign. This law is tetrahedrally invariant. As
\(r\to\infty\), the signed feature vector tends to the vector with entry
\(+1\) at vertex \(j\) and \(-1\) at the other three vertices. Its signed
mean has squared value \(1/4\), and each orthogonal Walsh coefficient also
has squared value \(1/4\). Therefore \(S/L\to1\); the theorem's constant
cannot be improved for invariant first-layer populations. Reachability of this
population by the actual flow is not asserted.

For a general finite vector \(A\), put

\[
 B(A)=\tfrac14\sum_a H_a(A)^2=\sum_\chi h_\chi(A)^2,
 \qquad D(A)=B(A)-4h_y(A)^2.
\]

Step 2 gives \(D(A)>0\) for \(A\ne0\). Moreover \(D/B\to1\) as
\(A\to0\): \(\tanh x=x+O(x^3)\), the signed logits sum to zero, so
\(h_y=O(\|A\|^3)\), while
\(B=\|A\|^2/3+O(\|A\|^4)\). Thus \(D/B\), assigned value one at zero,
is continuous and strictly positive on every compact ball. For every finite
\(R\), let \(\delta_R>0\) be its minimum on \(\|A\|\le R\). Then

\[
 \frac{\langle B(A)\mathbf1_{\{\|A\|\le R\}}\rangle_1}{S+3L}
 \le \frac{3(L-S)}{\delta_R(S+3L)}.
 \tag{4}
\]

For any sequence of invariant populations with \(L>0\) and \(S/L\to1\),
the right side tends to zero. Thus approaching the sharp spectral tie forces
first-layer **feature energy**, not necessarily all probability mass, out of
every bounded set. If weights have common bounded support, there is instead a
strict uniform spectral gap depending on that support bound.

## Hostile checks and exact remaining gap

* **Symmetry alone:** exchangeability only gives two eigenvalues. The ordering
  and strictness require the nonlinear cone inequality, so this does not rename
  a symmetry constraint as learning.
* **Trivial fit:** positive initial progress follows from the actual canonical
  Gaussian forward law and zero readout. Full interpolation is not assumed or
  proved; the obstruction also applies conditionally at an interpolating endpoint.
* **No feature dynamics claim:** the theorem does not prove monotonic growth or
  decline of \(S,L\). In particular, it does not establish that training actively
  discovers the primitive bits; it proves their unavoidable continued accessibility
  and limits what “learning XOR while suppressing nuisance factors” can mean here.
* **Population source:** only the supplied first forward Gaussian law is needed
  for the nonzero-training-interval argument. No transpose-noise regression
  subtraction or unprovided later source law is used. The all-time moment symmetry
  is conditional on the stipulated equivariant population flow, including its
  canonical-source law, rather than proved from an existence construction.
* **Degenerate initialization:** \(\sigma=0\) is excluded only from the fitting
  witness. The geometric inequality remains valid and the all-zero state can stall.
* **Endpoint and uniformity:** an unbounded limit can attain the sharp ratio;
  finite weights cannot. Equation (4) states exactly the necessary escape and
  avoids claiming full-mass concentration or dynamical reachability.
* **Layer distinction:** the first-layer spectral obstruction gives no analogous
  order for \(G\); the second-layer Gaussian map and trainable correction can mix
  the three latent contrasts nonlinearly. Proving an actual finite-horizon change
  in \(S/L\), or a second-layer factor suppression result, remains an open next
  bottleneck rather than part of this theorem.

Route recommendation: freeze and retain as a complete all-time conditional
geometric obstruction with an operational decoder interpretation. It is useful
if the research target includes separating successful label fitting from latent
factor collapse. It does not alone deliver a positive claim of feature discovery.

Self-check performed by the route author: exact gauge substitution in every
supplied equation; all nonzero sign patterns and zero-coordinate cases in (1);
normalizations via Walsh Parseval; an explicit sharp symmetric population; and
the small-weight expansion in (4). No independent review or numerical test was
performed. Source SHA-256 is to be recorded after this frozen file is written.

# Single first-neuron cavity at canonical depth L=2

Mathematical candidate, revised 2026-09-06. This note develops a deletion and
restoration calculation for the prescribed random network. It establishes
a weak polynomial path tail for each deterministic first-neuron index,
but not a Gaussian or conditional tail for the complete reverse field.
It proves a Gaussian tail for the independent cavity field, uniform
bounds for two explicit self-response terms, and a normalized logarithmic
singular-value estimate for the bulk restoration propagator. The remaining
quantity is a directional first-layer curvature response, specified below
in terms of the actual network and its deleted-neuron system.

The original construction used the three dependencies
`ALL_ANGLE_FIRST_LAYER_ACTION.md`, `ALL_ANGLE_RAW_GD_ACTION.md`, and
`COMPACT_GATE_CONFINEMENT_TEST.md`, in this directory. The arguments needed
here are included below. The revision also incorporates a symmetry-based
polynomial tail argument identified by an isolated review; its full proof
is included in Section 11, so the review is not an invoked dependency.
There are no experiments, external theorem imports, or claims about a
population limit. In particular, failure
to bound the remaining response is not a negative result about the
canonical dynamics.

## 1. Exact system and the question

Fix deterministic inputs with
\[
 \|x_a\|^2=d,\qquad x_1^T x_2/d=\rho\in(-1,1),\qquad
 C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\qquad y=(1,-1)^T.
\]
Both hidden layers have width \(n\). Write \(A=W^{(2)}\) and
\(w=W^{(3)}\), retaining the canonical layer labels on all hidden fields:
\[
\begin{aligned}
 z^{(1)}_a&=W^{(1)}x_a,&h^{(1)}_a&=\phi_1(z^{(1)}_a),\\
 z^{(2)}_a&=A h^{(1)}_a,&h^{(2)}_a&=\phi_2(z^{(2)}_a),\\
 f_a&=w^T h^{(2)}_a/n,&r_a&=f_a-y_a,&c_a&=-2r_a,\\
 \delta^{(2)}_a&=w\odot\phi_2'(z^{(2)}_a),&
 q^{(1)}_a&=A^T\delta^{(2)}_a,&
 \delta^{(1)}_a&=\phi_1'(z^{(1)}_a)\odot q^{(1)}_a.
\end{aligned}                                                    \tag{1}
\]
All finite transposes are \(T\). No population operator or population
adjoint \(*\) is being identified. Euclidean norms and spectral matrix
norms are ordinary, unnormalized norms; every neuron normalization is
displayed explicitly.

The independent initialization is exactly
\[
 W^{(1)}_{il}(0)\sim N(0,1/d),\qquad
 A_{il}(0)\sim N(0,1/n),\qquad w_i(0)\sim N(0,n^{-2}).       \tag{2}
\]
The raw tangent metric, physical loss, and raw gradient flow are
\[
\begin{gathered}
 \|V\|_{\rm raw}^2={d\over n}\|V^{(1)}\|_F^2
                +\|V^{(2)}\|_F^2+{1\over n}\|V^{(3)}\|^2,
 \qquad L=r_1^2+r_2^2,\\
 \dot W^{(1)}={1\over d}\sum_a c_a\delta^{(1)}_a x_a^T,
 \qquad \dot A={1\over n}\sum_a c_a\delta^{(2)}_a(h^{(1)}_a)^T,
 \qquad \dot w=\sum_a c_a h^{(2)}_a.                       \tag{3}
\end{gathered}
\]
Raw GD is the simultaneous update by \(\eta\) times these directions,
with **\(\eta=n^{-2}\)**. Its interpolation is linear in these raw
parameters, and hidden fields on a segment are recomputed from them.
The discrete calculation is given separately in Section 10.

Take \(\phi_2=\arctan\). The first activation can be \(\arctan\), or
\(\phi_1(s)=\int_0^s\phi_1'(u)du\), where the chosen first derivative is
a fixed nonzero smooth compactly supported function. Explicitly,
\(\phi_1'\in C_c^\infty(\mathbb R)\) and
\(\phi_1'\not\equiv0\). The nonzero assumption is needed for the
positive initially active fraction in Section 12. The main estimates use
\[
 |\phi_\ell|\le B_\ell,\quad |\phi_\ell'|\le P_\ell,
 \quad |\phi_\ell''|\le L_\ell\qquad(\ell=1,2).              \tag{4}
\]
All constants denoted \(C_T\) are deterministic, finite, independent of
\(n,d\), and may depend on the fixed horizon, activation bounds, and fixed
input geometry. No parameter of either activation depends on width.

For a deterministic first-neuron index \(j\), Section 11 already proves
\(\Pr\{\max_a\sup_{t\le T}|q^{(1)}_{a,j}(t)|>v\}
\le\Pr(\mathcal E_n^c)+C_T/v^2\). The stronger research target is a
Gaussian or sufficiently strong continuation tail, a bound conditional
on the deleted-column information, or a directional response estimate
such as a bound on \(\int_0^T\kappa_j\) in (40). A second-moment path
bound does not supply any of these stronger assertions.

## 2. Bounds used below, including the exact raw clock

On
\[
 \mathcal E_n=\{\|A(0)\|_{\rm op}\le8,\ \|w(0)\|_\infty\le1\},
                                                                  \tag{5}
\]
the following constants exist uniformly on each fixed interval:
\[
\begin{gathered}
 \sum_a|c_a|\le K_T,\quad \|w\|_\infty\le M_T,
 \quad \|A\|_{\rm op}\le A_T,\\
 {\|\delta^{(2)}_a\|\over\sqrt n}\le P_2M_T,
 \quad {\|q^{(1)}_a\|\over\sqrt n}\le A_TP_2M_T,\\
 {\|\dot\delta^{(2)}_a\|\over\sqrt n}
 +{\|\dot q^{(1)}_a\|\over\sqrt n}+\sum_a|\dot c_a|\le C_T
 \quad\hbox{for flow}.
\end{gathered}                                               \tag{6}
\]
For GD, differences of node fields in the last line are bounded by
\(\eta C_T\), for all sufficiently large \(n\). Constants also cover
the interval through \(\lceil T/\eta\rceil\eta\).

Here are direct justifications. Differentiating the physical loss gives
\[
 -\dot L={d\over n}\|\dot W^{(1)}\|_F^2
          +\|\dot A\|_F^2+{1\over n}\|\dot w\|^2.          \tag{7}
\]
Thus the residual norm is bounded by its initial norm. The readout update
and bounded \(\phi_2\) give its coordinate bound. Each rank-one update of
\(A\) has norm at most
\(n^{-1}|c_a|\|\delta^{(2)}_a\|\|h^{(1)}_a\|\), giving its spectral
bound. These bounds yield the two field bounds in (6). Next,
\[
 \dot z^{(2)}_a=\dot A h^{(1)}_a+A\dot h^{(1)}_a,
 \quad
 \dot\delta^{(2)}_a=\dot w\odot\phi_2'(z^{(2)}_a)
       +w\odot\phi_2''(z^{(2)}_a)\odot\dot z^{(2)}_a,
\]
and
\(\dot q^{(1)}_a=\dot A^T\delta^{(2)}_a+A^T\dot\delta^{(2)}_a\).
Each right side divided by \(\sqrt n\) is bounded. The prediction
differential is bounded in the raw metric, so its pairing with the
bounded raw gradient direction also bounds \(\dot c\). Formula (7)
bounds finite-time displacement in a fixed finite-dimensional metric;
local existence from contraction of the integral equation therefore
extends to every finite time.

For clarity, the GD assertion needs descent, not an assumed GF comparison.
Stop before a node with \(\|r\|>R_0+1\), where
\(R_0=\sqrt2(B_2+1)\). Summing preceding updates gives fixed bounds
on \(w,A\), including the candidate exit and the connecting raw segment.
For raw unit tangents \(U,V\), \(|D_V f_a|\le C_T\) and
\(|D_UD_Vf_a|\le C_T(1+\sqrt n)\). Indeed all mixed terms are bounded
by Cauchy--Schwarz, except possibly
\[
 {1\over n}\sum_i q^{(1)}_{a,i}\phi_1''(z^{(1)}_{a,i})
                     (U^{(1)}x_a)_i(V^{(1)}x_a)_i,
\]
whose bound is \(C_T\sqrt n\), using
\(\max_i|q^{(1)}_{a,i}|\le\|q^{(1)}_a\|\le C_T\sqrt n\).
The segment residual is bounded because its displacement is
\(\eta\|\operatorname{grad}_{\rm raw}L\|_{\rm raw}\le\eta C_T\).
The scalar integral Taylor formula consequently gives
\[
 L_{k+1}\le L_k-\eta\|\operatorname{grad}_{\rm raw}L_k\|_{\rm raw}^2
   +\tfrac12\eta^2 C_T(1+\sqrt n)
                  \|\operatorname{grad}_{\rm raw}L_k\|_{\rm raw}^2.
\]
Since \(\eta=n^{-2}\), the last coefficient is at most \(\eta/2\)
for large \(n\). This precludes the candidate exit. Product differences
in the preceding field identities now prove the GD version of (6).

The same arguments hold for the deleted system below, with the unchanged
normalization \(n\). Removing a first neuron never increases a bound on
the Euclidean norm of a feature vector.

For later comparison with the available action information, define in
flow
\[
 U_i=\sum_a|c_a(0)q^{(1)}_{a,i}(0)|
       +\int_0^T\sum_a|\partial_t(c_aq^{(1)}_{a,i})|dt.
\]
Equation (6), the product rule, and Euclidean Cauchy--Schwarz give
\(n^{-1}\sum_iU_i^2\le C_T\). For row \(W^{(1)}_i\), direct substitution
in (3) gives
\[
 d\|\dot W^{(1)}_i\|^2=\sum_a c_aq^{(1)}_{a,i}\dot h^{(1)}_{a,i}.
\]
Integration by parts and bounded features imply
\(\int_0^T d\|\dot W^{(1)}_i\|^2dt\le2B_1U_i\).
Writing the two first controls as
\(d_{i,a}=c_aq^{(1)}_{a,i}\phi_1'(z^{(1)}_{a,i})\) gives
\(\dot z^{(1)}_i=Cd_i\) and
\(d\|\dot W^{(1)}_i\|^2=d_i^TCd_i\).
Since the eigenvalues of \(C\) are in \((0,2)\),
\[
 \int_0^T|\dot z^{(1)}_i|^2dt\le4B_1U_i,\qquad
 \sup_{t\le T}|\dot z^{(1)}_i|\le2P_1U_i.
\]
Multiplying these inequalities yields the cubic estimate below.
The path estimate follows from
\(\sup_t|z^{(1)}_i(t)|\le|z^{(1)}_i(0)|+\sqrt{4TB_1U_i}\)
and \((a+b)^4\le8(a^4+b^4)\). Averaging gives
\[
 {1\over n}\sum_i\int_0^T|\dot z^{(1)}_i|^3dt\le C_T,
 \qquad
 {1\over n}\sum_i\sup_{t\le T}|z^{(1)}_i(t)|^4
 \le {8\over n}\sum_i|z^{(1)}_i(0)|^4+C_T.                 \tag{8}
\]
In GD use the discrete total variation of \(c q^{(1)}\). Taylor's
remainder for \(\phi_1\) is bounded by
\(\eta L_1U_i\) times the corresponding row work. Here
\(\eta\max_iU_i\le C_Tn^{-3/2}\), so it can be absorbed; the same bounds
hold for raw interpolations, with enlarged constants. This explains
precisely the action information used in Section 12.

## 3. A deletion independent of the Gaussian column

Choose \(j\) deterministically before initialization, set
\[
 P=I-e_je_j^T,\qquad g=A(0)e_j\sim N(0,I_n/n),\qquad
 \xi_a=z^{(1)}_{a,j}(0),\qquad B(t)=A(t)P.
\]
The first-root pair \(\xi=(\xi_1,\xi_2)^T\sim N(0,C)\) is independent
of \(g\). Let \(\mathcal F_{-j}\) contain all initialization except
\(g\), including \(\xi\).

The cavity has a permanently zero column \(j\), freezes row \(j\) of
\(W^{(1)}\), and trains every other parameter with the same raw rates
and the same denominator \(n\):
\[
\begin{aligned}
 \widehat B(0)&=A(0)P,&\widehat w(0)&=w(0),&
 \widehat z^{(1)}_i(0)&=z^{(1)}_i(0),\\
 \widehat z^{(2)}_a&=\widehat B P\widehat h^{(1)}_a,&
 \widehat q^{(1)}_a&=\widehat B^T\widehat\delta^{(2)}_a,\\
 \dot{\widehat B}&={1\over n}\sum_a\widehat c_a
             \widehat\delta^{(2)}_a(P\widehat h^{(1)}_a)^T,&
 \dot{\widehat w}&=\sum_a\widehat c_a\widehat h^{(2)}_a,\\
 \dot{\widehat z}^{(1)}_{a,i}
   &=\sum_b C_{ab}\widehat c_b\phi_1'(\widehat z^{(1)}_{b,i})
                        \widehat q^{(1)}_{b,i}\quad(i\ne j),&
 \widehat z^{(1)}_{a,j}(t)&=\xi_a.
\end{aligned}                                                     \tag{9}
\]
All hatted upper quantities and residuals are computed from these
parameters. Existence and uniqueness follow as in Section 2. The entire
cavity trajectory is \(\mathcal F_{-j}\)-measurable, hence independent
of \(g\). This deletes the trained column as well as its initial part.
Initializing column \(j\) at zero but allowing it to train would not be
the deletion in (9).

For the actual network write its entire column as
\[
 b(t)=A(t)e_j=g+\ell(t),\qquad
 \ell(t)={1\over n}\sum_b\int_0^t c_b(s)\delta^{(2)}_b(s)
                                      h^{(1)}_{b,j}(s)ds.          \tag{10}
\]
Thus \(A=B+b e_j^T\). In particular the exact omitted input into the
second layer is
\[
 e_a(t)=b(t)h^{(1)}_{a,j}(t),\qquad
 z^{(2)}_a=BPh^{(1)}_a+e_a.                                     \tag{11}
\]
On \(\mathcal E_n\), uniformly up to \(T\),
\[
 \|\ell(t)\|\le {K_TP_2M_TB_1T\over\sqrt n},\quad
 \|b(t)\|\le\|g\|+C_T/\sqrt n,\quad
 \Big(\sum_a\|e_a(t)\|^2\Big)^{1/2}
                   \le\sqrt2B_1(\|g\|+C_T/\sqrt n).             \tag{12}
\]
Although the RMS omitted input is of order \(n^{-1/2}\), the chosen
first root need not be close to its frozen cavity root.

## 4. Exact restoration, including every residual and learned term

For a common field write \(\Delta\) for actual minus cavity, and use
\(\Delta h^{(\ell)}=\phi_\ell(z^{(\ell)})-
\phi_\ell(\widehat z^{(\ell)})\), not a linearized feature difference.
The following identities are exact:
\[
\begin{aligned}
 \Delta z^{(2)}_a
   &=\Delta B\,Ph^{(1)}_a+\widehat B P\Delta h^{(1)}_a+e_a,\\
 \Delta\delta^{(2)}_a
   &=\Delta w\odot\phi_2'(z^{(2)}_a)
    +\widehat w\odot[\phi_2'(z^{(2)}_a)-\phi_2'(\widehat z^{(2)}_a)],\\
 \Delta f_a
   &={1\over n}\{\Delta w^T h^{(2)}_a
                         +\widehat w^T\Delta h^{(2)}_a\},
 \qquad \Delta c_a=-2\Delta f_a,\\
 \Delta q^{(1)}_{a,i}
   &=[\Delta B^T\delta^{(2)}_a
                         +\widehat B^T\Delta\delta^{(2)}_a]_i
                            \quad(i\ne j),\\
 \dot{\Delta B}
   &={1\over n}\sum_a\{
       \Delta c_a\delta^{(2)}_a(Ph^{(1)}_a)^T
       +\widehat c_a\Delta\delta^{(2)}_a(Ph^{(1)}_a)^T
       +\widehat c_a\widehat\delta^{(2)}_a(P\Delta h^{(1)}_a)^T\},\\
 \dot{\Delta w}
   &=\sum_a\{\Delta c_a h^{(2)}_a+
                                      \widehat c_a\Delta h^{(2)}_a\},\\
 \dot{\Delta z}^{(1)}_{a,i}
   &=\sum_b C_{ab}\{\Delta c_b\phi_1'(z^{(1)}_{b,i})q^{(1)}_{b,i}
       +\widehat c_b[\phi_1'(z^{(1)}_{b,i})
                    -\phi_1'(\widehat z^{(1)}_{b,i})]q^{(1)}_{b,i}
       +\widehat c_b\phi_1'(\widehat z^{(1)}_{b,i})
                                      \Delta q^{(1)}_{b,i}\}\quad(i\ne j).
\end{aligned}                                                     \tag{13}
\]
These are obtained by adding and subtracting one factor at a time;
in particular neither residual differences nor changes in learned bulk
weights have been dropped. The distinguished root satisfies
\[
 \dot z^{(1)}_{a,j}=\sum_b C_{ab}c_b\phi_1'(z^{(1)}_{b,j})
             [g^T\delta^{(2)}_b+\ell^T\delta^{(2)}_b],
 \qquad z^{(1)}_{a,j}(0)=\xi_a.                               \tag{14}
\]
Equations (9)--(14) are a closed exact restoration of the actual finite
network, not a system driven by a prescribed future trajectory.

The initial discrepancies are specifically
\[
\begin{gathered}
 \Delta B(0)=0,\quad\Delta w(0)=0,\quad\Delta z^{(1)}_i(0)=0,\\
 \Delta z^{(2)}_a(0)=g\phi_1(\xi_a),\\
 \Delta\delta^{(2)}_a(0)
  =w(0)\odot\{\phi_2'(\widehat z^{(2)}_a(0)+g\phi_1(\xi_a))
                         -\phi_2'(\widehat z^{(2)}_a(0))\},\\
 \Delta f_a(0)={w(0)^T\over n}
   [\phi_2(\widehat z^{(2)}_a(0)+g\phi_1(\xi_a))
                         -\phi_2(\widehat z^{(2)}_a(0))].
\end{gathered}                                              \tag{15}
\]
Thus equal bulk parameters at time zero do not mean equal upper fields
or equal initial residuals. The random first root enters before any
training has taken place.

## 5. Gaussian field and two uniformly controlled response terms

Define the Gaussian cavity field
\[
 G_{j,a}(t)=g^T\widehat\delta^{(2)}_a(t).
\]
Conditional on \(\mathcal F_{-j}\), every finite collection is centered
Gaussian, with the exact covariance
\[
 \mathbb E[G_{j,a}(t)G_{j,b}(s)\mid\mathcal F_{-j}]
   ={1\over n}\widehat\delta^{(2)}_a(t)^T
                                  \widehat\delta^{(2)}_b(s).       \tag{16}
\]
The initial first root may be retained in this conditioning: it is
independent of \(g\), and the cavity does not use its feature.

First, the entire learned-column readback is bounded:
\[
\begin{aligned}
 M_{j,a}(t)&=\ell(t)^T\delta^{(2)}_a(t)\\
  &={1\over n}\sum_b\int_0^t c_b(s)h^{(1)}_{b,j}(s)
                         \delta^{(2)}_b(s)^T\delta^{(2)}_a(t)ds,\\
 |M_{j,a}(t)|&\le T K_T B_1(P_2M_T)^2.                        \tag{17}
\end{aligned}
\]
The proved upper bound is \(O_T(1)\); it provides no vanishing factor
\(n^{-1/2}\). No lower bound is asserted. All learned-column history,
including the changing residual and changing first feature, is present
in (17).

To split the rest exactly, let \(\delta^{(2),0}_a\) denote the backward
field evaluated at the actual bulk parameters but with omitted input
\(e_a=0\), and set
\[
 D_a(t)=\operatorname{diag}\left(
 w_i(t)\int_0^1\phi_2''((BPh^{(1)}_a)_i+\theta e_{a,i})d\theta
                                \right).
\]
The fundamental theorem of calculus gives
\[
 \delta^{(2)}_a=\delta^{(2),0}_a+D_a e_a,\qquad
 \|D_a\|_{\rm op}\le M_TL_2.
\]
Consequently
\[
 q^{(1)}_{a,j}=G_{j,a}+M_{j,a}+S_{j,a}+R_{j,a},
 \quad S_{j,a}=g^TD_a b\,h^{(1)}_{a,j},
 \quad R_{j,a}=g^T(\delta^{(2),0}_a-\widehat\delta^{(2)}_a),    \tag{18}
\]
and
\[
 |S_{j,a}(t)|\le B_1M_TL_2\|g\|(\|g\|+C_T/\sqrt n).        \tag{19}
\]
This is an exact direct self-response bound, with no independence claim
about \(D_a\), \(b\), or the trained first root.

At time zero \(R_{j,a}=M_{j,a}=0\), and (15) gives the sharper
\[
 |q^{(1)}_{a,j}(0)-G_{j,a}(0)|
       \le B_1L_2\|w(0)\|_\infty\|g\|^2.                  \tag{20}
\]
This displays the initial first-root dependence rather than incorrectly
calling the actual initial query an independent Gaussian projection.

There is also a uniform conditional bound for the complete Gaussian
cavity path. On the \(\mathcal F_{-j}\)-measurable event
\(\widehat{\mathcal E}_n=\{\|A(0)P\|_{\rm op}\le8,
\|w(0)\|_\infty\le1\}\), (6) implies
\[
 {\|\widehat\delta^{(2)}_a(t)\|\over\sqrt n}\le D_0,
 \quad {\|\widehat\delta^{(2)}_a(t)-\widehat\delta^{(2)}_a(s)\|
                       \over\sqrt n}\le D_1|t-s|             \tag{21}
\]
with deterministic \(D_0,D_1\) depending only on the horizon and bounds.
For GD, initially use linear interpolation of the cavity node
\(\delta^{(2)}\) values; it satisfies the same estimates.

Here is an elementary proof of the resulting supremum tail. A centered
Gaussian of variance \(\sigma^2\) has moment-generating function
\(e^{\lambda^2\sigma^2/2}\), by completing the square in its density.
Exponential Markov and optimization in \(\lambda\) give
\(\Pr(|Z|>\sigma v)\le2e^{-v^2/2}\). Apply this first at time zero
and to the increment from zero to \(T\). At dyadic level \(m\ge1\)
there are at most \(2^m\) increments to the left parent at level
\(m-1\), each with standard deviation at most \(D_1T2^{-m}\).
Bound each by
\(D_1T2^{-m}(u+2\sqrt{m+1})\). The union of their exceptional
probabilities is at most
\(2e^{-u^2/2}\sum_{m\ge1}2^me^{-2(m+1)}\).
Telescoping the grids, using continuity, and
\(\sum_{m\ge1}(m+1)2^{-m}=3\), gives for the two samples
\[
 \Pr\left(\max_a\sup_{t\le T}|G_{j,a}(t)|>
       6(D_0+D_1T)(1+u)\ \middle|\ \mathcal F_{-j}\right)
       \le12e^{-u^2/2}\qquad(u\ge0)                         \tag{22}
\]
on \(\widehat{\mathcal E}_n\). This proof uses neither a Gaussian
process supremum theorem nor independence of different times.

One must not condition (16) or (22) on the full event \(\mathcal E_n\):
that event also depends on \(g\). Instead apply the conditional bound on
\(\widehat{\mathcal E}_n\), then add the probability of
\(\mathcal E_n^c\) when restricting actual trajectories. For reference,
\[
 \Pr(\mathcal E_n^c)
 \le2e^{-(8-2\log9)n}+2n e^{-n^2/2}.                       \tag{23}
\]
To prove the matrix bound, a maximal \(1/4\)-separated sphere set has
at most \(9^n\) points by disjoint radius-\(1/8\) ball volumes.
Approximating each of two unit vectors shows that the matrix norm is
at most twice its maximum bilinear form on this net. Each such form
for \(A(0)\) has variance \(1/n\); the scalar bound at threshold 4
and the union bound prove (23). The vector bound is the scalar Gaussian
bound at threshold 1, summed over \(n\) entries. The same argument
applies to \(A(0)P\), whose bilinear variances are at most \(1/n\).

## 6. Exact bulk response in the raw metric

Because \(|\rho|<1\), each moving first row is described, up to its
unchanging input-orthogonal part, by its two sample coordinates. Use the
following Euclidean bulk coordinate vector:
\[
 X=\left(\left({C^{-1/2}z^{(1)}_i\over\sqrt n}\right)_{i\ne j},
                    (B_{li})_{i\ne j},\ {w\over\sqrt n}\right)
       \in\mathbb R^m,\qquad m=n^2+2n-2.                    \tag{24}
\]
Indeed \(d\|\Delta W^{(1)}_i\|^2=
(\Delta z^{(1)}_i)^TC^{-1}\Delta z^{(1)}_i\) for changes in the
input span: write the change as a linear combination of the inputs
and multiply by both inputs to verify the formula. Hence (24) is
exactly the restricted raw metric, not a new metric on the actual flow.

For an independent argument \(E=(E_1,E_2)\in\mathbb R^{2n}\), define
\[
 f_a(X,E)={1\over n}w^T\phi_2(BPh^{(1)}_a+\sqrt n E_a),
 \qquad F(X,E)=-\nabla_X\sum_a(f_a(X,E)-y_a)^2.              \tag{25}
\]
When differentiating (25), \(E\) is held fixed. The actual bulk obeys
\(\dot X=F(X,e/\sqrt n)\) and the cavity obeys
\(\dot{\widehat X}=F(\widehat X,0)\). This holds even though the
actual \(e\) is generated by (10)--(14): bulk partial derivatives do
not differentiate the distinguished neuron's parameters.

Put \(\Delta X=X-\widehat X\), \(E=e/\sqrt n\), and define the exact
secant operators
\[
\begin{aligned}
 J(t)&=\int_0^1D_XF(\widehat X+\theta\Delta X,0)d\theta,\\
 \mathcal B(t)&=\int_0^1D_EF(X,\theta E)d\theta,\\
 L_a(t)&={1\over\sqrt n}\int_0^1
        D_X\delta^{(2)}_a(\widehat X+\theta\Delta X,0)d\theta.
\end{aligned}                                                     \tag{26}
\]
Then, with \(Y=\sqrt n\Delta X\),
\[
 \dot Y=JY+v,
 \qquad v=\sum_{b=1}^2\mathcal B_b(t)b(t)h^{(1)}_{b,j}(t),
 \qquad Y(0)=0,\qquad R_{j,a}=g^TL_aY.                    \tag{27}
\]
Here \(\mathcal B_b\) is the block mapping \(\mathbb R^n\) into the
bulk coordinate space. Equations (26)--(27) include the entire residual
derivative of the loss; \(F\) is not a frozen-residual vector field.

Uniformly on \(\mathcal E_n\),
\[
 \|\mathcal B\|_{\rm op}+\|L_a\|_{\rm op}\le C_T,
 \qquad \|v\|\le C_T(\|g\|+n^{-1/2}).                    \tag{28}
\]
For a unit bulk tangent \(V\),
\(\|D_Vz^{(1)}_a\|/\sqrt n\le\sqrt2\) and
\(\|D_Vz^{(2)}_a(X,0)\|/\sqrt n\le B_1+\sqrt2A_TP_1\).
Differentiating \(\delta^{(2)}\) proves the bound for \(L_a\).
For a unit \(E\)-direction \(H\),
\(D_Hz^{(2)}_a=\sqrt n H_a\). The mixed derivative of \(f_a\) is
\[
 D_VD_H f_a={1\over\sqrt n}(D_Vw)^T
                       [\phi_2'(z^{(2)}_a)\odot H_a]
  +{1\over\sqrt n}\sum_i w_i\phi_2''(z^{(2)}_{a,i})
                                     (D_Vz^{(2)}_a)_iH_{a,i}.
\]
Cauchy--Schwarz bounds it by \(C_T\|V\|\|H\|\), as well as bounding
each first differential. Differentiating the squared loss now proves
the bound for \(\mathcal B\). Residuals at the secants are bounded:
their readout is coordinatewise bounded and their features are bounded,
whether or not the secant itself is a gradient trajectory.

Let \(\mathcal U(t,s)\) solve \(\partial_t\mathcal U=J(t)\mathcal U\),
\(\mathcal U(s,s)=I\). Existence follows from successive integration
of the continuous bounded finite-dimensional coefficients; the series
is bounded by the scalar exponential series on a compact interval.
Differentiating variation of constants verifies
\[
\begin{aligned}
 R_{j,a}(t)&=\sum_b\int_0^t h^{(1)}_{b,j}(s)K_{j,ab}(t,s)ds,\\
 K_{j,ab}(t,s)&=g^TL_a(t)\mathcal U(t,s)\mathcal B_b(s)b(s).
\end{aligned}                                                     \tag{29}
\]
This identity does not assume any independence between the Gaussian
column and the response kernel.

## 7. Where the ordinary maximum estimate loses its normalization

The finite differences (13), in metric (24), give
\[
 {d\over dt}\|\Delta X\|
 \le C_T(1+Q_\infty(t))\|\Delta X\|
       +{C_T\over\sqrt n}(\|g\|+n^{-1/2}),\quad
 Q_\infty(t)=\max_{i\ne j,a}|q^{(1)}_{a,i}(t)|,             \tag{30}
\]
in the upper-derivative sense at a zero of the norm. The only maximum
needed in this particular finite-difference proof is in
\([\phi_1'(z^{(1)})-\phi_1'(\widehat z^{(1)})]q^{(1)}\);
all residual-difference terms use the RMS field bound in (6).
For example \(|\Delta c|\le C_T(\|\Delta X\|+\|e\|/\sqrt n)\),
\(\|\Delta q^{(1)}_{-j}\|/\sqrt n\le
C_T(\|\Delta X\|+\|e\|/\sqrt n)\), and the remaining updates
have the same bound. These estimates prove (30) directly.

Multiplication by the scalar integrating factor in (30) yields
\[
 \sup_{t\le T}\|\Delta X(t)\|
 \le {C_T(\|g\|+n^{-1/2})\over\sqrt n}
           \exp\left(C_T\int_0^TQ_\infty(s)ds\right).
\]
But (27) reads the scalar with a factor \(\sqrt n\):
\[
 |R_{j,a}|=\sqrt n\,|g^TL_a\Delta X|
 \le C_T\|g\|(\|g\|+n^{-1/2})
           \exp\left(C_T\int_0^TQ_\infty(s)ds\right).       \tag{31}
\]
The factor \(n^{-1/2}\) has disappeared. On the available spectral
bounds \(Q_\infty\le C_T\sqrt n\), this is at most an
\(\exp(C_T\sqrt n)\) bound. Even a separately proved
\(Q_\infty\le C_T\sqrt{\log n}\) would give
\(\exp(C_T\sqrt{\log n})\), which diverges, though more slowly than
any fixed power of \(n\). The bulk difference in that hypothetical
case would tend to zero; (31) would still not give a uniform scalar
self-response bound. This is the explicit normalization loss at issue.

## 8. A positive trace estimate for the actual restoration propagator

The raw loss Hessian provides a more structured description of \(J\).
At a bulk point \(X_\theta=\widehat X+\theta\Delta X\), with \(E=0\),
let \(c^0_{\theta,a}\) and \(q^{(1),0}_{\theta,a}\) be the residual
coefficient and reverse field computed there. Then
\[
 J=J_0+H,
 \qquad \|J_0\|_{\rm op}\le C_T,\quad J_0^T=J_0,\quad H^T=H,
                                                                  \tag{32}
\]
where \(H\) acts only on the two first coordinates of each bulk neuron:
\[
 H_i(t)=\int_0^1 C^{1/2}
    \operatorname{diag}_{a=1,2}
       [c^0_{\theta,a}q^{(1),0}_{\theta,a,i}
                         \phi_1''(z^{(1)}_{\theta,a,i})]
                      C^{1/2}d\theta\quad(i\ne j).          \tag{33}
\]
To verify the decomposition, differentiate
\(L=\sum_a(f_a-y_a)^2\) twice. The term
\(-2\sum_a Df_a\otimes Df_a\) in \(D_XF\) is bounded in operator
norm. In \(-2r_aD^2f_a\), the readout/hidden cross terms and top
curvature term are bounded by the estimates following (28).
The two second-layer/first-layer cross terms have, for example, size
\[
 {1\over n}|(\delta^{(2),0}_a)^T
                  V^{(2)}[\phi_1'(z^{(1)}_a)\odot D_Uz^{(1)}_a]|
 \le C_T\|V^{(2)}\|_F\|U\|.
\]
The remaining term is precisely
\(n^{-1}\sum_i c_aq^{(1),0}_{a,i}\phi_1''(z^{(1)}_{a,i})
D_Uz^{(1)}_{a,i}D_Vz^{(1)}_{a,i}\); inserting (24) gives (33).
This verifies both the sign and all raw normalization factors.

Every secant point has \(\|B\|_{\rm op}\le A_T\) and
\(\|w\|_\infty\le M_T\). Consequently
\[
 {1\over n}\|H(t)\|_F^2
 ={1\over n}\sum_{i\ne j}\|H_i(t)\|_F^2\le C_T.            \tag{34}
\]
In detail, \(\|C^{1/2}DC^{1/2}\|_F\le\|C\|_{\rm op}\|D\|_F\),
which follows by expanding the Frobenius norm in orthonormal singular
directions and using the spectral bound on each multiplication.
Squaring the integral in (33) and applying scalar Cauchy--Schwarz in
\(\theta\) reduces (34) to
\(n^{-1}\sum_{i,a}|q^{(1),0}_{\theta,a,i}|^2\le C_T\), supplied by
the spectral bound on \(B^T\). Thus (34) is a proved normalized
Schatten-2 estimate on the only unbounded part of the Jacobian. It
does not require a bound on a whole-space \(L^p\) operator.

It also yields a uniform logarithmic singular-value tail for the full
propagator. If \(s_1,\ldots,s_m\) are its singular values, then
\[
 {1\over n}\sum_{\nu=1}^m
 \left[\log_+\left(e^{-C_T(t-s)}s_\nu(\mathcal U(t,s))\right)\right]^2
       \le C_T(t-s)^2\qquad(0\le s\le t\le T).             \tag{35}
\]
In particular the number of singular values exceeding
\(e^{C_T(t-s)+u}\) is at most \(C_T n(t-s)^2/u^2\), for \(u>0\).
Normalization is by the first-population width \(n\), not by the
larger parameter dimension \(m\).

Here is a proof of the required finite-matrix inequality. On a compact
time interval let \(K,H\) be continuous, or piecewise continuous with
finitely many pieces and bounded one-sided limits. Consider the real
matrix equation \(\dot V=(K+H)V\) with \(V(s)=I\),
\(K^T=K\), \(K\preceq cI\), and \(H^T=H\). The solution is invertible:
solving \(\dot Z=-Z(K+H)\), \(Z(s)=I\), gives
\(\partial_t(ZV)=0\). For the positive eigenvalues \(\lambda_\nu\)
of \(VV^T\), differentiating the eigenvalue equation at a simple
eigenvalue gives
\[
 {d\over dt}\log\sqrt{\lambda_\nu}
       =v_\nu^T(K+H)v_\nu.
\]
This formula holds almost everywhere also at coincidences after choosing
an orthonormal eigenbasis diagonalizing the derivative on the repeated
eigenspace. To justify that assertion without a perturbation theorem,
the min-max characterization bounds changes of each ordered eigenvalue
by the norm of the matrix change, hence gives local Lipschitz continuity.
At a repeated value \(\lambda\), decompose into its eigenspace and the
orthogonal complement. At a nearby time the matrix blocks are
\(\lambda I+hD_{11}+o(h)\), \(hD_{12}+o(h)\), and
\(D_{22}^{\,0}+O(h)\), where \(D_{22}^{\,0}-\lambda I\) is invertible.
The complementary component of any nearby eigenvector is therefore
\(O(h)\). Projecting its eigenvalue equation onto the first block gives
the slopes as the eigenvalues of \(D_{11}\). Here
\(D_{11}=2\lambda(K+H)\) restricted to that eigenspace.
Choosing its orthonormal eigenvectors gives the formula at points of
differentiability. Local Lipschitz functions are absolutely continuous,
so their almost-everywhere differential inequalities may be integrated.

Put \(l_\nu=\log s_\nu(V)-c(t-s)\) and
\(F=\sum_\nu(l_\nu)_+^2\). Almost everywhere,
\[
 \tfrac12\dot F\le\sum_\nu(l_\nu)_+v_\nu^THv_\nu
 \le\sqrt F\left(\sum_\nu|v_\nu^THv_\nu|^2\right)^{1/2}
 \le\sqrt F\,\|H\|_F.
\]
The last inequality holds because the diagonal square sum in any
orthonormal basis is at most the full entry square sum in that basis.
Differentiate \(\sqrt{F+\epsilon}\), integrate, and let
\(\epsilon\downarrow0\). It follows that
\(\sqrt F\le\int_s^t\|H(u)\|_Fdu\). Equation (34) proves (35).
The elementary eigenvalue min-max statement used here itself follows
by diagonalizing a real symmetric matrix: every subspace of the requisite
dimension intersects the span of its leading eigenvectors, while that
span and its orthogonal complement attain the two variational bounds.

Estimate (35) is a positive bound on the canonical restoration system.
It is not a bound on its response in the distinguished random direction:
the singular vectors and that direction depend on the same Gaussian
column. No conditional isotropy of those singular vectors is asserted.

## 9. The remaining curvature response can be isolated exactly

Let \(\mathcal U_0\) be the propagator of \(J_0\), so
\(\|\mathcal U_0(t,s)\|_{\rm op}\le e^{C_T(t-s)}\), by differentiating
the squared norm of a solution and integrating its scalar inequality.
Define
\[
 Y_0(t)=\int_0^t\mathcal U_0(t,s)v(s)ds,\qquad
 \Gamma_{j,a}(t)=\int_0^t
            g^TL_a(t)\mathcal U_0(t,s)H(s)Y(s)ds.           \tag{36}
\]
The exact equation (27) implies
\[
 Y=Y_0+\int_0^t\mathcal U_0(t,s)H(s)Y(s)ds,
 \qquad R_{j,a}=g^TL_aY_0+\Gamma_{j,a}.                    \tag{37}
\]
All terms of (18) other than \(G_{j,a}\) and \(\Gamma_{j,a}\) now have
uniform deterministic bounds on \(\mathcal E_n\); indeed
\(\|g\|\le8\) there and \(\|Y_0\|\le C_T\). The insertion of (33)
between a bounded backward test and the forced bulk response is not
controlled deterministically or conditionally by these estimates.
Section 11 does give a weaker unconditional second-moment bound for
this scalar after restriction to \(\mathcal E_n\).

There is a more concrete directional formulation. Let
\(a_{j,a,i}(t,s)\in\mathbb R^2\) be the first-neuron block \(i\) of
\(\mathcal U_0(t,s)^TL_a(t)^Tg\). Then
\[
 \Gamma_{j,a}(t)=\int_0^t\sum_{i\ne j}
               a_{j,a,i}(t,s)^TH_i(s)Y_i(s)ds,              \tag{38}
\]
and the elementary inequalities
\(|u^TMv|\le\|M\|_F|u||v|\) and Cauchy--Schwarz give
\[
 |\Gamma_{j,a}(t)|\le C_T\sqrt n\int_0^t
       \left(\sum_{i\ne j}|a_{j,a,i}(t,s)|^2|Y_i(s)|^2\right)^{1/2}ds.
                                                                  \tag{39}
\]
This identifies a directional overlap that would use the proved
Schatten-2 bound, rather than replacing it by a maximum Hessian.
No bound at the needed \(n^{-1/2}\) overlap scale has been established.

For a sufficient estimate not phrased as a bound on the scalar query
itself, define the actual directional curvature exposure
\[
 \kappa_j(t)={\big(Y(t)^TH(t)Y(t)\big)_+\over1+\|Y(t)\|^2},
 \qquad
 \Pi_j(t)={\left(n\sum_{i\ne j}|Y_i(t)|^4\right)^{1/2}
                                    \over1+\|Y(t)\|^2}.     \tag{40}
\]
Both are measurable quantities of the actual/cavity pair, not freely
chosen controls. Equation (34) proves
\[
 \kappa_j\le C_T\Pi_j,\qquad
 1+\|Y(t)\|^2
       \le\exp\left(C_Tt+2\int_0^t\kappa_j(s)ds\right)
                             \quad\hbox{on }\mathcal E_n.  \tag{41}
\]
For the first inequality, sum
\(|Y_i^TH_iY_i|\le\|H_i\|_F|Y_i|^2\) and apply
Cauchy--Schwarz over \(i\). For the second, differentiate
\(1+\|Y\|^2\) in (27), use (28), (32), and
\(2|Y^Tv|\le\|Y\|^2+\|v\|^2\), then multiply by the integrating
factor. Increasing \(C_T\) absorbs the uniform source bound.

Thus a uniform-in-probability bound on
\(\int_0^T\kappa_j(t)dt\) would suffice for a uniform-in-probability
self-response bound; a bound on \(\int\Pi_j\) would be a more explicit
sufficient route. These are **open proof obligations**, not established
estimates and not assumptions added to the original question. The signed
exposure in (40) is smaller than a full operator-norm bound; (38) is the
still more targeted quantity if only scalar readback is pursued.

## 10. Exact raw GD restoration at eta = n^{-2}

Use subscript \(k\) for actual and cavity node values, with the cavity
obtained by the same simultaneous raw updates on its remaining
parameters. All algebraic identities (11), (13) for field differences,
(15), and (18)--(20) hold verbatim at nodes. In the update equations of
(10), (13), and (14), replace a time derivative by its forward difference
divided by \(\eta\) and evaluate every right side at the old node.
In particular the entire learned column is exactly
\[
 \ell_k={\eta\over n}\sum_{l=0}^{k-1}\sum_b
                  c_{l,b}\delta^{(2)}_{l,b}h^{(1)}_{l,b,j},\qquad
 M_{j,a,k}={\eta\over n}\sum_{l<k,b}c_{l,b}h^{(1)}_{l,b,j}
                            (\delta^{(2)}_{l,b})^T\delta^{(2)}_{k,a}.
                                                                  \tag{42}
\]
There is no current-node term in this learned history.

In bulk coordinates the exact recurrence is
\[
 \Delta X_{k+1}=(I+\eta J_k)\Delta X_k+\eta\mathcal B_kE_k,
 \quad Y_{k+1}=(I+\eta J_k)Y_k+\eta v_k,                    \tag{43}
\]
with the same secants (26), evaluated at nodes. Define ordered products
\[
 \mathcal U_{k,l}=(I+\eta J_{k-1})\cdots(I+\eta J_l),
 \qquad \mathcal U_{l,l}=I.
\]
Then the exact readback restoration is
\[
 R_{j,a,k}=\eta\sum_{l<k,b}h^{(1)}_{l,b,j}
       g^TL_{a,k}\mathcal U_{k,l+1}\mathcal B_{b,l}b_l.      \tag{44}
\]
The index \(l+1\) accounts for the fact that a source at step \(l\)
first appears in \(Y_{l+1}\). Replacing the product by a continuous
GF propagator would not be exact.

The core products \(\mathcal U^0_{k,l}\), obtained from \(J_{0,k}\),
have norms at most \(e^{C_T(k-l)\eta}\). Therefore (36)--(38) become
\[
 Y_{0,k}=\eta\sum_{l<k}\mathcal U^0_{k,l+1}v_l,
 \quad
 \Gamma_{j,a,k}=\eta\sum_{l<k}g^TL_{a,k}
                               \mathcal U^0_{k,l+1}H_lY_l,        \tag{45}
\]
with the same exact split \(R=g^TL Y_0+\Gamma\) and uniform bounds
on every other scalar term.

The directional-energy estimate has a controlled discrete correction.
Since \(\|J_k\|_{\rm op}\le C_T(1+\sqrt n)\), expansion of (43)
and \(\eta=n^{-2}\) give
\[
 1+\|Y_{k+1}\|^2
 \le[1+C_T\eta+2\eta\kappa_{j,k}+C_T\eta^2 n]
                                      (1+\|Y_k\|^2).
\]
Multiplying these inequalities and using \(1+x\le e^x\) for \(x\ge0\)
yields, for \(k\eta\le T+\eta\),
\[
 1+\|Y_k\|^2\le
   \exp\left(C_T(T+1)+2\eta\sum_{l<k}\kappa_{j,l}+C_T/n\right).
                                                                  \tag{46}
\]
The accumulated correction is \(O(T\eta n)=O(T/n)\), not a
time-independent error asserted without calculation.

The logarithmic singular-value bound (35) also holds for the discrete
products. Here is a proof accommodating their noncommutativity. For
large \(n\), \(\eta\|J_k\|\le1/2\), so \(I+\eta J_k\) is symmetric
positive definite. Define the symmetric matrix
\(G_k=\eta^{-1}\log(I+\eta J_k)\) by its real orthonormal
eigendecomposition. The scalar integral identity for \(\log(1+x)\)
gives \(|\log(1+x)-x|\le x^2\) when \(|x|\le1/2\). Hence
\[
 \|G_k-J_k\|_{\rm op}\le\eta\|J_k\|_{\rm op}^2\le C_T/n.
\]
The continuous equation with piecewise constant generator \(G_k\)
has exactly the products \(\mathcal U_{k,l}\) at its nodes. Decompose
\(G_k=(J_{0,k}+G_k-J_k)+H_k\) and apply the proved matrix inequality
in Section 8. This proves (35) with \(t-s=(k-l)\eta\) and enlarged
constants, using (34); it does not assume that the factors commute.

Finally, bounds on nodes extend to the requested raw interpolation.
The bulk coordinate difference and the learned column are linear on
each cell, so their norm bounds persist by convexity. At every segment
point (18) holds with recomputed fields and \(e_a=b h^{(1)}_{a,j}\).
The bound for \(L_a\) in (28) remains valid. For the Gaussian field,
recomputed cavity \(\delta^{(2)}\) has derivative of RMS norm at most
\(C_T\) on each cell: the raw segment direction is the bounded old-node
gradient, \(\dot w\) is bounded coordinatewise, and the product rule
used in (6) applies on the segment. Thus (21)--(22) also apply to this
recomputed cavity process. These observations extend any uniform bound
on \(Y_k\) to the whole raw interpolation without treating it as GF.

## 11. What the estimates actually yield for the full query

For flow, let \(\Gamma_j(T)=\max_a\sup_{t\le T}|\Gamma_{j,a}(t)|\).
Combining (17)--(19), (22), and (36)--(37), and enlarging constants,
gives the useful exact tail reduction
\[
 \Pr\left(\max_a\sup_{t\le T}|q^{(1)}_{a,j}(t)|>
                                      C_T(1+u)+v\right)
 \le12e^{-u^2/2}+\Pr(\mathcal E_n^c)
                 +\Pr(\mathcal E_n\cap\{\Gamma_j(T)>v\})
 \qquad(u,v\ge0).                                           \tag{47}
\]
There is a corresponding node assertion in GD with (45). Alternatively,
(46), if its open exposure term were bounded, would give the complete
raw-interpolation response through Section 10.

Equation (47) alone is a reduction. Its last term has the weak polynomial
bound proved next, but the stronger conditional and directional estimates
remain open. The deterministic estimates (17), (19), and (35) hold on
\(\mathcal E_n\); the Gaussian conditional estimate (22) holds on the
\(\mathcal F_{-j}\)-measurable event \(\widehat{\mathcal E}_n\), not
by conditioning on the full event \(\mathcal E_n\).

Here is the additional actual-network argument. Set
\(Q_i=\max_a\sup_{t\le T}|q^{(1)}_{a,i}(t)|\).
Absolute continuity and Cauchy--Schwarz give
\[
 \frac1n\sum_i Q_i^2
 \le \frac2n\sum_a\|q^{(1)}_a(0)\|^2
    +\frac{2T}{n}\int_0^T\sum_a\|\dot q^{(1)}_a(t)\|^2dt
 \le C_T\quad\hbox{on }\mathcal E_n.                 \tag{47a}
\]
For GF this follows from (6). For raw GD the recomputed identity
\(\dot q^{(1)}_a=\dot A^T\delta^{(2)}_a+
A^T\dot\delta^{(2)}_a\) holds inside every cell. The held old-node
direction bounds \(\|\dot A\|_{\rm op}\), while the product-rule
argument at the end of Section 10 bounds
\(\|\dot\delta^{(2)}_a\|/\sqrt n\). Thus (47a) holds on the
entire raw interpolation too, for all sufficiently large widths.

For any permutation matrix \(P_\pi\), the transformation
\(W^{(1)}\mapsto P_\pi W^{(1)}\),
\(A\mapsto AP_\pi^T\), \(w\mapsto w\) preserves the initialization
law and \(\mathcal E_n\). The equations are equivariant and transform
\(q^{(1)}_a\) into \(P_\pi q^{(1)}_a\). Finite GF uniqueness, or
induction for simultaneous GD followed by raw interpolation, preserves
this symmetry for whole paths. Hence for every deterministic index \(j\),
\[
 \mathbb E[\mathbf1_{\mathcal E_n}Q_j^2]
 =\frac1n\mathbb E[\mathbf1_{\mathcal E_n}\sum_iQ_i^2]\le C_T,
 \qquad
 \Pr(Q_j>v)\le\Pr(\mathcal E_n^c)+C_T/v^2\quad(v>0).    \tag{47b}
\]
The expectation here is over initialization, restricted to the displayed
event. Independence of evolved neurons is not asserted. The assertion
does not apply to an index chosen after seeing the network or to the
maximum over all indices. Since (23) tends to zero, it gives asymptotic
tightness of the fixed-index paths. Finitely many remaining widths can
be included in a qualitative tightness statement because each finite GF
path exists globally and each raw GD path has finitely many finite steps
on the fixed horizon. No polynomial bound on their bad events is claimed.

Let \(G_j^*=\max_a\sup_{t\le T}|G_{j,a}(t)|\). Integrating (22)
against its Gaussian tail, conditional on \(\mathcal F_{-j}\) and on
its measurable event, gives
\(\mathbb E[\mathbf1_{\widehat{\mathcal E}_n}(G_j^*)^2]\le C_T\).
The integration is justified by
\(\mathbb E X^2=\int_0^\infty 2v\Pr(X>v)dv\) for nonnegative
\(X\), obtained by integrating the identity
\(X^2=\int_0^X2v\,dv\). The Gaussian upper bound is integrable.
Since \(\mathcal E_n\subseteq\widehat{\mathcal E}_n\), and the
other three terms in the final decomposition are bounded on
\(\mathcal E_n\), (47b) and the squared triangle inequality yield
\[
 \mathbb E[\mathbf1_{\mathcal E_n}\Gamma_j(T)^2]\le C_T,
 \qquad
 \Pr(\mathcal E_n\cap\{\Gamma_j(T)>v\})\le C_T/v^2.     \tag{47c}
\]
For GD, (47c) concerns the node remainder (45); (47b) already concerns
the complete interpolated query. These scalar bounds give neither a
bound on \(Y\), nor on the exposure or participation in (40), nor on
the directional overlap in (39). In particular, they do not prove a
Gaussian tail for the actual query or a population continuation theorem.

## 12. Precisely what the first action bounds do not yet supply here

The first blocks of the rescaled restoration vector have the explicit
form
\[
 Y_i=C^{-1/2}(z^{(1)}_i-\widehat z^{(1)}_i)\qquad(i\ne j).    \tag{48}
\]
On an initialization event also bounding the empirical initial fourth
moment, applying (8) to both trajectories proves
\[
 \sum_{i\ne j}\sup_{t\le T}|Y_i(t)|^4\le C_{T,\rho} n,
 \qquad
 \sum_{i\ne j}\int_0^T|\dot Y_i(t)|^3dt\le C_{T,\rho} n.    \tag{49}
\]
These statements follow from \(|u-v|^4\le8(|u|^4+|v|^4)\),
\(|u-v|^3\le4(|u|^3+|v|^3)\), and the fixed norm of \(C^{-1/2}\).
No probabilistic independence of the two trajectories is used. The
Gaussian first-root law has
\(\mathbb E|\xi|^4=8+4\rho^2\le12\) and
\(\mathbb E|\xi|^8\le1680\), by expanding Gaussian moments, so
Chebyshev bounds the probability that its empirical fourth moment
exceeds 13 by \(1680/n\).

One sufficient pointwise scale for the participation route (40) is
substantially more specific. If \(\|Y\|=O(1)\), a pointwise bounded
\(\Pi_j\) asks for
\(\sum_i|Y_i|^4=O(n^{-1})\) along the forced response, whereas (49)
only gives \(O(n)\). A bound on the time integral of \(\Pi_j\) would
not require that pointwise bound at every time. For general \(Y\), the universal deterministic
bound is
\[
 \Pi_j\le\sqrt n\,{\|Y\|^2\over1+\|Y\|^2}\le\sqrt n,
\]
because the sum of block fourth powers is at most the squared sum of
block squares. Inserting this into (41) reproduces the growing
exponential. The supplied action estimate does not, by this calculation,
give a bounded exposure integral for the column-induced difference.
It controls each trajectory's motion, not the needed distribution of
this particular sensitivity among first neurons.

For compact first gates there is a useful exact reduction: every
initially doubly saturated bulk neuron is frozen in both systems, so
its block \(Y_i\) is zero and contributes nothing to (38) or (40).
Indeed its two gates initially vanish; Lipschitz continuity of the
gate and the integral equation keep the row fixed, and the same argument
applies in the cavity. For GD, each update of such a row is exactly zero,
so induction gives the same conclusion. For the fixed compact gate and
fixed \(\rho\), the probability that an initial pair is not doubly
saturated lies strictly between zero and one, since its Gaussian density
is positive everywhere. Independence of the initial rows and the variance
bound \(n^{-1}p(1-p)\) show that this remaining set has a positive limiting
fraction of all rows, in probability. No directional-overlap estimate on
that set has
been obtained here. For arctan, (49) holds but there is no such exactly
frozen set. None of these statements invokes a generic abstract
\(L^\infty\)-to-\(L^p\) obstruction.

## 13. Candidate conclusion and the smallest remaining target

The construction gives an auxiliary system independent of the selected
Gaussian column and the exact decomposition
\[
 q^{(1)}_{a,j}
   =\underbrace{g^T\widehat\delta^{(2)}_a}_{\text{Gaussian cavity}}
    +\underbrace{M_{j,a}+S_{j,a}+g^TL_aY_0}_{\text{uniformly bounded on }\mathcal E_n}
    +\underbrace{\Gamma_{j,a}}_{\text{weak tail proved; directional bounds open}}.
\]
Its initial first-root dependence is (15), its learned-column history
is (17) or (42), and its full residual and learned-bulk dependence is
(13), equivalently (26)--(29) or (43)--(45).

For this approach the specific bilinear curvature insertion (38) still
lacks a strong continuation or conditional bound; its weak polynomial
tail is (47c). A concrete sufficient directional route is a
width-uniform bound on the signed directional exposure integral in
(40), with (41) and (46) proving why that would close the response.
The more explicit fourth-order participation or directional overlap
bounds in (39)--(40) would allow use of the already proved normalized
Schatten-2 estimate. They have not been proved for the actual forced
canonical response. The logarithmic singular-value bound (35) makes
the matrix-level gain precise, while leaving that direction-sensitive
step visible.

Accordingly this candidate proves a weak fixed-index path tail for the
actual query at every fixed finite horizon, together with exact
restoration identities and positive component and logarithmic
singular-value estimates. Stronger Gaussian/conditional tails and
directional exposure estimates remain open. It draws no impossibility
conclusion and makes no population-identification claim.

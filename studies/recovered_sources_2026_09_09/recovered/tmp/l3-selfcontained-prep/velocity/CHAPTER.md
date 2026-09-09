# V. Finite raw dynamics, full kernels, hidden velocities, and path laws

We prove the finite-width assertions for three samples and three hidden layers with the fixed activation
\[
 \phi(z)=a(1+z)+e\arctan z,\qquad a\ge1,\quad 0<e\le1,
 \qquad d_\phi=\phi'.
\]
The constants \(a,e\) are those already selected in Parts R and G, independently of width and physical horizon. The proof identifies only fixed finite Gaussian transcripts; mesh refinement, cap removal, and the raw step \(n^{-2}\) are handled by deterministic comparisons.

## V.1. Definitions and exact internal inputs

Let \(x_i\in\mathbb R^d\), \(i=1,2,3\), satisfy \(\|x_i\|^2=d\), let \(y_i\in\{-1,1\}\), and put \(\Gamma_{ij}=x_i^Tx_j/d\). All finite vector norms are normalized RMS, \(\|v\|_n^2=n^{-1}\sum_\alpha v_\alpha^2\); matrix operator and Frobenius norms are ordinary. The rank-one action \(u\otimes_n v=uv^T/n\) has Frobenius norm \(\|u\|_n\|v\|_n\). Population spaces \(H_\ell=L^2(\Omega_\ell,\mu_\ell)\) are separate for the three layers, and \(u\otimes v:q\mapsto u\langle v,q\rangle\). Every inner product belongs to its indicated layer.

The state is \(\theta=(w,A,B,C)\), with \(A:H_1\to H_2\), \(B:H_2\to H_3\); \(A-A_0,B-B_0\) are Hilbert--Schmidt. For differences and directions use
\[
 \|\Delta\theta\|_{\mathcal X}
 =\sqrt d\,\|\Delta w\|_2+\|\Delta A\|_{\rm HS}
             +\|\Delta B\|_{\rm HS}+\|\Delta C\|_2.              \tag{V.1}
\]
At finite width the first term is \(\sqrt{d/n}\|\Delta W^1\|_F\), the two matrix terms are ordinary Frobenius norms, and the readout term is RMS. These compare states on a common population space or at the same width, never operators at unidentified different widths.

For a smooth odd clip with
\[
 |\tau_R(q)|\le\min(|q|,2R),\quad |\tau_R'|\le1,\qquad
 \tau_R(q)=q\quad(|q|\le R),
\]
write
\[
 D_R(z,q)=aq+e(1+z^2)^{-1}\tau_R(q),\qquad
 D_\infty(z,q)=d_\phi(z)q.                                    \tag{V.2}
\]
Thus
\[
 |d_\phi|\le a+e,\quad |d_\phi'|\le ce,\quad
 |D_R(z,q)|\le(a+e)|q|,\quad |(D_R)_q|\le a+e,\quad
 |(D_R)_z|\le ceR.                                           \tag{V.3}
\]
The forward fields are
\[
 z_i^1=w\cdot x_i,\quad h_i^\ell=\phi(z_i^\ell),\quad
 z_i^2=Ah_i^1,\quad z_i^3=Bh_i^2,\quad
 f_i=\langle C,h_i^3\rangle,\quad p_i=y_i-f_i.
\]
The capped backward fields are
\[
 \delta_{R,i}^3=D_R(z_i^3,C),\quad q_{R,i}^2=B^*\delta_{R,i}^3,
 \quad\delta_{R,i}^2=D_R(z_i^2,q_{R,i}^2),
\]
\[
 q_{R,i}^1=A^*\delta_{R,i}^2,\qquad
 \delta_{R,i}^1=D_R(z_i^1,q_{R,i}^1).
\]
Their physical raw field is
\[
 F_{R,w}=d^{-1}\sum_i p_i\delta_{R,i}^1x_i,\quad
 F_{R,A}=\sum_i p_i\delta_{R,i}^2\otimes h_i^1,\quad
 F_{R,B}=\sum_i p_i\delta_{R,i}^3\otimes h_i^2,\quad
 F_{R,C}=\sum_i p_i h_i^3.                                    \tag{V.4}
\]
We reserve \(b_i^\ell=\delta_{\infty,i}^\ell\) for true backward fields, including when evaluated as observations at a capped state.

The finite initialization is exactly
\[
 W^1_{\alpha j}\sim N(0,1/d),\quad
 A_{\alpha\beta},B_{\alpha\beta}\sim N(0,1/n),\quad
 C_\alpha\sim N(0,n^{-2}),                                    \tag{V.5}
\]
independently. Raw GD is simultaneous Euler for \(F_\infty\), with \(\eta_n=n^{-2}\), followed by linear interpolation of the raw parameters. Hidden fields are recomputed from that interpolation. Its raw direction on \([k\eta_n,(k+1)\eta_n)\) is \(F_\infty(\theta_n(k\eta_n))\). At nodes take the right direction, except for the terminal-left convention at a terminal mesh node of an observation interval.

Here are the precise prior conclusions used.

**F: fixed programs and common actions.** For a fixed finite program formed from independent Gaussian roots, the two independent initialized matrices reused in both orientations, \(C^1\) coordinate maps with bounded continuous first derivatives, and causal scalar first/second-moment contractions, every finite within-layer joint empirical tuple converges along the full width sequence in probability in \(\mathcal W_2\). Each oriented matrix has a centered Gaussian source family, with covariance equal to the Gram of its actual inputs. The four oriented families are mutually independent and independent of original scalar roots, while all same-family time/sample covariances are retained. A forward query of an initial matrix on input \(u\) has scalar answer
\[
 \xi_u+\sum_v E[\partial_{\zeta_v}u]\,v,                       \tag{V.6}
\]
where \(v\) ranges over earlier opposite-orientation inputs and \(\zeta_v\) is the named source of their answers; the reverse rule interchanges sides. Derivatives hold all deterministic coefficients, contractions and covariances fixed. Named arguments remain distinct under singular covariance, and unavailable-source derivatives vanish.

The statement remains valid after adjoining finitely many independent Gaussian roots and bounded-derivative query perturbations. At a fixed transcript its source construction, expected first source derivatives, and second moments are continuous under such perturbations with uniformly bounded coordinate first derivatives; the finite chronological proof uses Gaussian covariance square roots, including at rank drops. A countable collection of programs admits common generated \(L^2\) spaces on which \(A_0,B_0\) extend to bounded actions, with norms at most 10 and actual adjoints. Strong \(L^2\) limits of generated inputs have the corresponding action limits. At finite width, \(\|A_0\|_{\rm op},\|B_0\|_{\rm op}\le10\) with probability tending to one.

This lemma has been proved in Part F by finite Gaussian conditioning, independent-query regularization, and Gaussian integration by parts. It asserts neither growing-transcript identification nor an \(L^p\to L^p\) matrix-action bound.

**R and G: global capped bounds and incoming moments.** The selected \(a,e\) give global population physical capped trajectories \(\theta_R\) with common initialization \(C_0=0\) and common initialized actions. Their first projection norms, current action norms, and readout norms have one bound independent of cap and physical time. On every fixed \([0,T]\), their raw directions have a cap-independent bound. For one \(K_*\), independent of \(R,t,p\),
\[
 \sup_{R<\infty,t\ge0,i}
  \{\|C_R(t)\|_p+\|q^2_{R,i}(t)\|_p+\|q^1_{R,i}(t)\|_p\}
                   \le K_*\sqrt p,\qquad p\ge2.               \tag{V.7}
\]
The moment estimate concerns the actual nonlinear incoming fields. It is passed from controlled Euler programs to physical capped flows after freezing each causal physical coefficient in source derivatives; no derivative of a normalized residual is used. The controlled residual-clock bound in Part G makes the constant independent of physical horizon. Only the displayed conclusions of R and G are used below.

## V.2. Raw stability, population cap removal, and uniqueness

On a bounded primal ball, \(\phi\)'s Lipschitz bound and bounded actions give
\[
 \sum_{\ell,i}(\|z_i^\ell-\bar z_i^\ell\|_2+\|h_i^\ell-\bar h_i^\ell\|_2)
       +\sum_i|p_i-\bar p_i|
                \le K\|\theta-\bar\theta\|_{\mathcal X}.       \tag{V.8}
\]
For an upper layer use \(Ah-\bar A\bar h=(A-\bar A)h+\bar A(h-\bar h)\), and for the residual use Cauchy--Schwarz on \(\langle C,h\rangle-\langle\bar C,\bar h\rangle\). Also
\[
 \|u\otimes v-\bar u\otimes\bar v\|_{\rm HS}
 \le\|u-\bar u\|_2\|v\|_2+\|\bar u\|_2\|v-\bar v\|_2.         \tag{V.9}
\]
Successive backward substitution using (V.3) bounds \(F_R\) independently of \(R\) on that ball. At fixed cap it is Lipschitz in \(\mathcal X\), with constant \(K(1+eR)\) independent of width.

More precisely, if \(R'\ge R\), including \(R'=\infty\), then
\[
 |D_{R'}(z,q)-D_R(\bar z,\bar q)|
 \le(a+e)|q-\bar q|+ceR|z-\bar z|
                   +2e|\bar q|\mathbf1_{\{|\bar q|>R\}}.       \tag{V.10}
\]
First change \(q\) to \(\bar q\) inside \(D_{R'}\). The remainder is
\[
 e[(1+z^2)^{-1}-(1+\bar z^2)^{-1}]\tau_R(\bar q)
 +e(1+z^2)^{-1}[\tau_{R'}(\bar q)-\tau_R(\bar q)].
\]
The derivative of \(z\mapsto(1+z^2)^{-1}\) is bounded; \(|\tau_R|\le2R\); and the two clips agree when \(|\bar q|\le R\), while both have absolute value at most \(|\bar q|\). This proves (V.10).

Apply (V.10) successively through the three backward gates. An earlier incoming discrepancy is multiplied only by bounded actions and \(a+e\); a new factor \(R\) multiplies a new forward discrepancy, already controlled by (V.8). Thus only one cap factor occurs:
\[
 \|F_{R'}(\theta)-F_R(\bar\theta)\|_{\mathcal X}
 \le K(1+eR)\|\theta-\bar\theta\|_{\mathcal X}
       +Ke\sum_{Q\in\mathscr Q_R(\bar\theta)}
                   \|Q\mathbf1_{\{|Q|>R\}}\|_2,               \tag{V.11}
\]
where \(\mathscr Q_R=\{C,q^2_{R,i},q^1_{R,i}:1\le i\le3\}\). The sum of backward-field discrepancies satisfies the same bound. Physical residual feedback causes no new cap factor: split \(p_i\delta_i-\bar p_i\bar\delta_i\), then use (V.8), bounded primal quantities and (V.9). The tails in (V.11) belong only to the reference.

For \(Q\) in (V.7), and \(p\ge2\),
\[
 E[Q^2\mathbf1_{\{|Q|>u\}}]\le u^{2-p}E|Q|^p
                  \le u^2(K_*\sqrt p/u)^p.
\]
Choose \(p=(u/(3K_*))^2\ge2\), absorb the prefactor into a smaller exponential rate, and take square roots. Hence
\[
 \sup_{R,t,Q}\|Q\mathbf1_{\{|Q|>u\}}\|_2\le K e^{-cu^2}
                              \quad(u\ge u_0).               \tag{V.12}
\]
No independence of a Gaussian source and a learned shift is needed here.

Integrate (V.11) between two population caps, and use Gronwall:
\[
 \sup_{t\le T}\|\theta_{R'}(t)-\theta_R(t)\|_{\mathcal X}
                      \le K_Te^{K_TR-cR^2}.                  \tag{V.13}
\]
Indeed an inequality \(E(t)\le \epsilon t+L\int_0^tE(s)ds\) gives \(E(t)\le\epsilon t e^{Lt}\) by iterating its integral form. Substitution in (V.11) gives a vanishing bound of the same form, after changing constants, for raw directions and backward fields.

The cap paths and their derivatives are uniformly Cauchy on \([0,T]\). Their limits satisfy \(\theta(t)=\theta_0+\int_0^tV(s)ds\), so \(\theta\in C^1\), \(\dot\theta=V\). Apply (V.11) with the limit state on its left, a cap reference on its right and \(R'=\infty\); (V.12)--(V.13) identify \(V=F_\infty(\theta)\). Bounded multipliers ensure all uncut backward fields are \(L^2\). Integer caps and integer horizons suffice for one countable common-action construction, and the limits agree on overlaps.

Any bounded-primal strong uncut competitor with the same initialization can be compared against \(\theta_R\) by the same estimate. Its bounds may change \(K_T\), but no tails of that competitor are required, so (V.13) still tends to zero. This proves uniqueness. At a reached time \(t_0\), the initial discrepancy from the cap reference already satisfies (V.13); multiplication by another \(e^{K_TR}\) still leaves a vanishing bound. The global trajectory supplies continuation, and its continuation is unique among the stated competitors. No local existence theorem on arbitrary uncut \(L^2\) states is invoked.

## V.3. Fixed-cap source rows from nonlinear Gaussian probes

Fix \(R,T\). Constants in V.3--V.7 may depend on \(R,T,a,e\) and the fixed data, but not on width, mesh, source covariance conditioning, or a moment exponent. Let \(0=t_0<\cdots<t_N=T\), \(h_j=t_{j+1}-t_j\). All sufficiently fine population Euler meshes lie in a fixed enlarged primal ball: this follows from the fixed-cap Lipschitz property, the bounded cap path, and the raw Euler estimate in V.6, whose proof uses no source or velocity bound.

Suppress the subscript \(R\) on capped fields in this section. Freeze the causal \(p_{j,b}=y_b-f_b(\theta_j)\), all other scalar contractions, response coefficients, and covariances in formal derivatives. Exact rank unrolling and F give
\[
 z^1_{k,i}=z^1_{0,i}+\sum_{j<k,b}h_jp_{j,b}\Gamma_{ib}\delta^1_{j,b},
 \qquad C_k=\sum_{j<k,b}h_jp_{j,b}h^3_{j,b},                 \tag{V.14}
\]
\[
 z^\ell_{k,i}=\xi^\ell_{k,i}
                   +\sum_{j<k,b}\mathsf A^\ell_{ki,jb}\delta^\ell_{j,b},
 \qquad
 q^{\ell-1}_{k,i}=\zeta^{\ell-1}_{k,i}
                   +\sum_{j\le k,b}\mathsf D^\ell_{ki,jb}h^{\ell-1}_{j,b},
                                                               \tag{V.15}
\]
for \(\ell=2,3\), with
\[
 \mathsf A^\ell_{ki,jb}
 =E_{\ell-1}\partial_{\zeta^{\ell-1}_{j,b}}h^{\ell-1}_{k,i}
      +h_jp_{j,b}E_{\ell-1}[h^{\ell-1}_{k,i}h^{\ell-1}_{j,b}], \tag{V.16}
\]
\[
 \mathsf D^\ell_{ki,jb}
 =E_\ell\partial_{\xi^\ell_{j,b}}\delta^\ell_{k,i}
      +\mathbf1_{\{j<k\}}h_jp_{j,b}E_\ell[\delta^\ell_{k,i}\delta^\ell_{j,b}].
                                                               \tag{V.17}
\]
Every source variance is the squared norm of its actual initial-matrix input, and is bounded by the primal ball; also \(\sum_b|p_{j,b}|\le K\).

Choose one oriented answer family and a fresh standard Gaussian vector \(g\) in its answer population. Add \(\varepsilon\alpha_{j,b}g\), \(|\alpha_{j,b}|\le1\), at selected answer slots, and recompute all subsequent finite residuals and updates. Lipschitz stability on a larger primal ball gives
\[
 E_{k+1}\le(1+Kh_k)E_k+Kh_k|\varepsilon|\|g\|_n.             \tag{V.18}
\]
Forcing every time gives \(E_k\le K|\varepsilon|\|g\|_n\); forcing only time \(j\) gives \(E_k\le Kh_j|\varepsilon|\|g\|_n\) for \(k>j\). A primary query has the same bounds, with no \(h_j\) for a current answer. The constants include all three recomputed residuals. On \(\|g\|_n\le2\), sufficiently small fixed \(|\varepsilon|\) keeps the perturbed program in the larger ball by first-exit induction. The required finite primal event follows directly from the fixed-mesh primary law and exact update lengths, as established in V.7; it does not require the source-row bounds now being proved.

At fixed mesh and \(\varepsilon\), F gives
\[
 \langle g,V_n^\varepsilon\rangle_n\longrightarrow E[GV^\varepsilon].
\]
In its scalar construction \(G\) is independent of the original roots and source families. The coefficients depend on \(\varepsilon\), but are deterministic. With them frozen, the only explicit occurrences of \(G\) are the answer additions. Thus
\[
 E[GV^\varepsilon]
 =E[\partial_GV^\varepsilon]
 =\varepsilon\sum_{j,b}\alpha_{j,b}
                              E[\partial_{\eta_{j,b}}V^\varepsilon]. \tag{V.19}
\]
For this integration by parts, condition on all other roots and sources. At a fixed finite transcript the scalar expression is Lipschitz in its named Gaussian arguments with a finite deterministic constant, since primary coordinate derivatives are bounded. It has at most linear growth in \(G\), bounded \(G\)-derivative, and a vanishing Gaussian boundary term. Those facts justify both the conditional integral and subsequent expectation.

At this fixed mesh, \(E\partial_\eta V^\varepsilon\to E\partial_\eta V^0\). To verify the continuity premise, induct chronologically: next covariances and learned contractions are second moments of earlier inputs; covariance-square-root coupling passes their \(L^2\) limits, including singular ones. The scalar first derivatives are continuous functions of the preceding finite coefficient list and Gaussian arguments. On a compact neighborhood of that list, bounded coordinate derivatives give deterministic bounds for its finitely many formal derivatives. Dominated convergence passes the next expected derivative; residual contractions pass as continuous inner products. There is no covariance derivative or inverse.

Conditionally on the original unperturbed network, \(\langle g,V_n^0\rangle_n\) is centered Gaussian of variance \(\|V_n^0\|_n^2/n\), hence tends to zero on the bounded-program event. Cauchy--Schwarz and (V.18)--(V.19), first sending width to infinity and then \(\varepsilon\to0\), prove
\[
 \left|\sum_{j,b}\alpha_{j,b}E\partial_{\eta_{j,b}}V_k\right|\le K.
                                                               \tag{V.20}
\]
Choose deterministic signs of the expected derivatives for the absolute expected row. A single strictly past insertion gives \(Kh_j\). Cauchy--Schwarz bounds the learned contractions in (V.16)--(V.17), so
\[
 |\mathsf A^\ell_{ki,jb}|\le Kh_j,\quad
 |\mathsf D^\ell_{ki,jb}|\le Kh_j\ (j<k),\qquad
 |\mathsf D^\ell_{ki,kb}|\le K.                              \tag{V.21}
\]
This has not equated \(|E\partial V|\) and \(E|\partial V|\).

Both current transpose returns are retained. Put
\(a^\ell_{k,i}=(D_R)_z(z^\ell_{k,i},m^\ell_{k,i})\) and
\(v^\ell_{k,i}=(D_R)_q(z^\ell_{k,i},m^\ell_{k,i})\), where
\(m^1=q^1,m^2=q^2,m^3=C\). Then
\[
 \mathsf D^3_{ki,kb}=\mathbf1_{\{i=b\}}Ea^3_{k,i},\qquad
 \mathsf D^2_{ki,kb}=\mathbf1_{\{i=b\}}Ea^2_{k,i}
       +\mathsf D^3_{ki,kb}E[v^2_{k,i}d_\phi(z^2_{k,b})].      \tag{V.22}
\]
Here \(C_k\) and learned forward corrections use strictly past times, and a current forward preactivation contains its own current source with coefficient one. Differentiate the top gate, then the returned current middle gate to obtain (V.22), with all three sample coordinates distinct formal arguments even at singular covariance.

## V.4. Pointwise absolute derivative rows and primary moments

For a scalar field in one population, let
\[
 \mathcal R(F)=\sum_{\eta\ {\rm in\ that\ population}}|\partial_\eta F|, \tag{V.23}
\]
including every primary source through the final mesh time: \(\zeta^1\) in layer 1, \((\xi^2,\zeta^2)\) in layer 2, \(\xi^3\) in layer 3. Future derivatives vanish. Root derivatives could be included at the cost of a constant term. All coefficients are frozen.

Write \(Z^\ell=\mathcal R(z^\ell)\), \(H^\ell=\mathcal R(h^\ell)\),
\(B^\ell=\mathcal R(\delta^\ell)\), \(Q^s=\mathcal R(q^s)\), and
\(C^\partial=\mathcal R(C)\). The coordinate chain rule, (V.14)--(V.15), and (V.21) give pointwise
\[
\begin{aligned}
 Z^1_{k,i}&\le K\sum_{j<k}h_j\sum_bB^1_{j,b},\\
 Z^\ell_{k,i}&\le1+K\sum_{j<k}h_j\sum_bB^\ell_{j,b}\quad(\ell=2,3),\\
 C^\partial_k&\le K\sum_{j<k}h_j\sum_bH^3_{j,b},\\
 H^\ell_{k,i}&\le(a+e)Z^\ell_{k,i},\\
 Q^s_{k,i}&\le1+K\sum_bH^s_{k,b}
                   +K\sum_{j<k}h_j\sum_bH^s_{j,b}\quad(s=1,2),\\
 B^s_{k,i}&\le ceRZ^s_{k,i}+(a+e)Q^s_{k,i}\quad(s=1,2),\\
 B^3_{k,i}&\le ceRZ^3_{k,i}+(a+e)C^\partial_k .
\end{aligned}                                                    \tag{V.24}
\]
Every same-time term in a transpose line is a forward field already determined at that time, so no same-time system needs inversion.

Let \(U_k\) be the maximum of \(C_k^\partial\) and the nine \(Z^\ell_{k,i}\). The last four lines bound each remaining field by \(K(1+U_k+\sum_{j<k}h_jU_j)\). Substitution into the first lines and
\[
 \sum_{j<k}h_j\sum_{r<j}h_rU_r
 =\sum_{r<k}h_rU_r\sum_{r<j<k}h_j
 \le T\sum_{r<k}h_rU_r
\]
give \(U_k\le K+K\sum_{j<k}h_jU_j\). Induction gives
\(U_k\le K\prod_{j<k}(1+Kh_j)\le Ke^{KT}\). Returning to all lines proves
\[
 \mathcal R(F_{k,i})\le K                                    \tag{V.25}
\]
for every primary scalar field. This is a pathwise bound on the absolute derivative row.

The same reduction bounds moments. Replace seminorms by \(L^p\) norms; direct Gaussian sources and first roots have norm at most \(K\sqrt p\); use
\(\|\phi(Z)\|_p\le K+(a+e)\|Z\|_p\) and
\(\|D_R(Z,Q)\|_p\le(a+e)\|Q\|_p\), then Minkowski in the finite sums. Thus
\[
 \sup_{\pi,k,i}\|F^\pi_{k,i}\|_p\le K\sqrt p,\qquad p\ge2,     \tag{V.26}
\]
for all primary fields and \(C\). No independence among time sources is required by Minkowski, and no matrix \(L^p\)-operator bound is used.

## V.5. Appended hidden-velocity queries and their truncations

At an Euler node evaluate instantaneous preactivation and feature velocities in the raw direction \(F_R(\theta_k)\):
\[
 P^1_{k,i}=\sum_b p_{k,b}\Gamma_{ib}\delta^1_{k,b},\qquad
 U^\ell_{k,i}=d_\phi(z^\ell_{k,i})P^\ell_{k,i},                \tag{V.27}
\]
\[
 P^2_{k,i}=\sum_b p_{k,b}\delta^2_{k,b}
                    E_1[h^1_{k,b}h^1_{k,i}]+J^2_{k,i},
 \qquad J^2_{k,i}=A_kU^1_{k,i},                              \tag{V.28}
\]
\[
 P^3_{k,i}=\sum_b p_{k,b}\delta^3_{k,b}
                    E_2[h^2_{k,b}h^2_{k,i}]+J^3_{k,i},
 \qquad J^3_{k,i}=B_kU^2_{k,i}.                              \tag{V.29}
\]
The feature derivative is the true \(d_\phi\), not a capped backward gate.

Append, after the complete primary transcript, all \(A_0U^1_{k,i}\) observations, then all \(B_0U^2_{k,i}\), and add learned rank increments explicitly. They do not feed training. Source derivatives of a time-\(k\) input in later named sources vanish despite this appended order. The source formulas, justified by truncation below, are
\[
 J^\ell_{k,i}=\gamma^\ell_{k,i}
                +\sum_{j\le k,b}\mathsf E^\ell_{ki,jb}\delta^\ell_{j,b},
 \qquad\ell=2,3,                                            \tag{V.30}
\]
\[
 \mathsf E^\ell_{ki,jb}
 =E_{\ell-1}\partial_{\zeta^{\ell-1}_{j,b}}U^{\ell-1}_{k,i}
  +\mathbf1_{\{j<k\}}h_jp_{j,b}
                    E_{\ell-1}[h^{\ell-1}_{j,b}U^{\ell-1}_{k,i}].     \tag{V.31}
\]
The new forward source \(\gamma^\ell\) has variance \(\|U^{\ell-1}_{k,i}\|_2^2\); its covariance with every forward observation is the inner product of their inputs. It is a new named argument. It can be correlated with old sources of the same forward family; the opposite family remains independent.

From (V.25), freezing \(p\) and contractions,
\[
 \mathcal R(P^1_{k,i})\le K,\qquad
 \mathcal R(U^1_{k,i})
 \le |d_\phi'(z^1_{k,i})P^1_{k,i}|\mathcal R(z^1_{k,i})
                      +(a+e)\mathcal R(P^1_{k,i})
 \le K(1+|P^1_{k,i}|).                                      \tag{V.32}
\]
Thus the expected absolute derivative row in (V.31) for \(\ell=2\) is bounded by \(K\), using (V.26). Its learned row is bounded by Cauchy--Schwarz and \(\sum_jh_j=T\). The variance of \(\gamma^2\) is bounded directly by the \(L^2\) norm in (V.27). Source formula (V.30) and Minkowski yield
\[
 \sum_{j\le k,b}|\mathsf E^2_{ki,jb}|\le K,\qquad
 \|J^2_{k,i}\|_p+\|P^2_{k,i}\|_p+\|U^2_{k,i}\|_p\le K\sqrt p. \tag{V.33}
\]
Differentiate (V.30) for \(J^2\) only in layer-2 primary transpose sources \(\zeta^2\). Hold coefficients and the new named forward source \(\gamma^2\) fixed; its formal \(\zeta^2\) derivative is zero, including at singular covariance. Then (V.25), (V.33) give
\[
 \sum_{j,b}|\partial_{\zeta^2_{j,b}}P^2_{k,i}|\le K,\qquad
 \sum_{j,b}|\partial_{\zeta^2_{j,b}}U^2_{k,i}|
                                  \le K(1+|P^2_{k,i}|).     \tag{V.34}
\]
A second use of (V.31) proves
\[
 \sum_{j\le k,b}|\mathsf E^3_{ki,jb}|\le K,\qquad
 \sup_{\pi,k,i,\ell}(\|P^\ell_{k,i}\|_p+\|U^\ell_{k,i}\|_p)
                                  \le K\sqrt p.             \tag{V.35}
\]

We justify this reasoning in the required order. The product map
\((z,P)\mapsto d_\phi(z)P\) has an unbounded \(z\)-derivative and cannot be directly fed to F. Replace it by \(d_\phi(z)\tau_M(P)\). At each fixed \(M\) the coordinate first derivatives are bounded. Its formal derivative is
\[
 \partial_\eta[d_\phi(Z)\tau_M(P)]
 =d_\phi'(Z)\tau_M(P)\partial_\eta Z
                  +d_\phi(Z)\tau_M'(P)\partial_\eta P.       \tag{V.36}
\]
For the bottom query its absolute derivative row is dominated independently of \(M\) by \(K(1+|P^1|)\), integrable by primary bound (V.26). Thus the first-action row estimates and moments are first proved for each truncated action with constants independent of \(M\). Pointwise \(\tau_M(P)\to P\), \(\tau_M'(P)\to1\), and dominated convergence identifies every expected derivative in (V.31).

The empirical passage uses only second moments. If a coupling has \((z_n,p_n)\to(z,p)\) in \(L^2\), then
\[
 \|d_\phi(z_n)p_n-d_\phi(z)p\|_2
 \le(a+e)\|p_n-p\|_2+\|[d_\phi(z_n)-d_\phi(z)]p\|_2\to0.      \tag{V.37}
\]
For the last term, bound the part \(|p|\le L\) by \(ceL\|z_n-z\|_2\) and the rest by \(2(a+e)\|p\mathbf1_{\{|p|>L\}}\|_2\); send \(n\to\infty\), then \(L\to\infty\). Positive-part tails are 1-Lipschitz in \(L^2\), and
\[
 |p|\mathbf1_{\{|p|>L\}}\le2(|p|-L/2)_+.
\]
Hence primary joint \(\mathcal W_2\) convergence makes the empirical bottom clipping error vanish in the iterated width then \(M\) limit. The matrix norm bound transfers it to the actual finite action; common-action continuity transfers it to the population action. Learned contractions converge in \(L^2\), and source covariances converge as input second moments. Covariance-square-root coupling passes the entire finite scalar formula. This proves (V.30)--(V.33) for the first untruncated action and its joint law with the primary transcript.

For the second action, retain an inner clip \(M\) in the first action and an outer clip \(N\) in \(d_\phi(z^2)P^2\). At fixed \(M,N\) the original F applies. As \(M\to\infty\), the first action coefficients converge; its primary \(\zeta^2\) derivative rows obey (V.25), and its new forward source has formal derivative zero. Thus the rows of \(P^2_M\) converge and stay bounded. At fixed \(N\), (V.36) passes the outer expected derivative limits. The \(L^2\) input/action convergence follows from (V.37) and bounded actions. Then send \(N\to\infty\); the domination in (V.34) is \(K(1+|P^2|)\), integrable by the already-proved first-action moments (V.33). This proves (V.30)--(V.35) and joint empirical laws for both actions without a circular velocity-moment premise. Full same-family covariance matrices are retained for any finite set of appended observations.

## V.6. Raw Euler approximation and a deterministic velocity comparison

On a larger primal ball let \(F_R\) have norm at most \(M_0\) and Lipschitz constant \(L_0\), with a bounded reference flow inside it with slack. The local Euler defect on a step \(h_j\) is at most \(L_0M_0h_j^2/2\), because
\[
 \left\|\int_0^{h_j}[F_R(\theta(t_j+s))-F_R(\theta(t_j))]\,ds\right\|_{\mathcal X}
                 \le\int_0^{h_j}L_0M_0s\,ds.
\]
The error recurrence and discrete Gronwall give node error at most
\[
                   \tfrac12 L_0M_0Te^{L_0T}|\pi|.            \tag{V.38}
\]
Linear raw interpolation adds at most \(2M_0|\pi|\). Choosing mesh smaller than the fixed slack closes first-exit induction. The constants are width independent. This proves the bounded population Euler premise used in V.3 from the bounded cap path, without using any source derivative or velocity result.

For states \(\theta,\bar\theta\) on one primal ball and directions \(v,\bar v\) of bounded \(\mathcal X\) norm, put
\(\alpha=\|\theta-\bar\theta\|_{\mathcal X}\) and
\(\beta=\|v-\bar v\|_{\mathcal X}\). Define the actual chain-rule velocities
\[
 P_i^1=v_w\cdot x_i,\quad U_i^\ell=d_\phi(z_i^\ell)P_i^\ell,\quad
 P_i^2=v_Ah_i^1+A U_i^1,\quad P_i^3=v_Bh_i^2+B U_i^2.         \tag{V.39}
\]
For \(\mathcal T_M(X)=\|(|X|-M)_+\|_2\), \(M\ge1\), we claim
\[
 \sum_{\ell,i}(\|P_i^\ell-\bar P_i^\ell\|_2+\|U_i^\ell-\bar U_i^\ell\|_2)
 \le K\left[\beta+(1+M)\alpha+
                       \sum_{\ell,i}\mathcal T_M(\bar P_i^\ell)\right]. \tag{V.40}
\]
The constant depends on the primal/direction bound and fixed activation, not on \(R,M\).

Truncate the reference factor using \(c_M(p)=\operatorname{sgn}(p)\min(|p|,M)\):
\[
 \|[d_\phi(z)-d_\phi(\bar z)]\bar P\|_2
 \le ceM\|z-\bar z\|_2+2(a+e)\mathcal T_M(\bar P).            \tag{V.41}
\]
The first \(P\)-error is at most \(\beta\). For an upper layer expand
\[
\begin{aligned}
 P^\ell-\bar P^\ell={}&
 (v_{W_\ell}-\bar v_{W_\ell})h^{\ell-1}
 +\bar v_{W_\ell}(h^{\ell-1}-\bar h^{\ell-1})\\
 &+(W_\ell-\bar W_\ell)\bar U^{\ell-1}
 +W_\ell(U^{\ell-1}-\bar U^{\ell-1}).
\end{aligned}
\]
The direction and difference operator norms are bounded by their HS norms. Using (V.8), this is at most \(K(\alpha+\beta+\|U^{\ell-1}-\bar U^{\ell-1}\|_2)\) in \(L^2\). The \(U^\ell\)-error is \((a+e)\) times the corresponding \(P^\ell\)-error plus (V.41). Induction proves (V.40). There is a single \(M\): each new \(M\) multiplies a forward discrepancy already controlled by (V.8).

If \(\|\bar P\|_4\le K\), then
\[
 \mathcal T_M(\bar P)\le\|\bar P\mathbf1_{\{|\bar P|>M\}}\|_2
                             \le\|\bar P\|_4^2/M.            \tag{V.42}
\]
Population instantaneous Euler node states and raw directions differ from the flow state/direction at the preceding time by \(K|\pi|\), by (V.38) and fixed-cap Lipschitzness. Use the node as reference in (V.40), apply (V.35), (V.42), and take \(M=|\pi|^{-1/2}\). The hidden velocity error is at most \(K\sqrt{|\pi|}\), uniformly in time. Primary errors are \(K|\pi|\).

Here is the population chain rule needed in that statement. A \(C^1\) \(L^2\)-valued preactivation path has almost-everywhere absolutely continuous coordinate representatives, by its integral representation and Fubini. The scalar chain rule gives derivative \(d_\phi(Z)P\), \(P=\dot Z\). This product is \(L^2\)-continuous by (V.37); its coordinate integral identity holds in \(L^2\) because the multiplier is bounded. Thus \(\phi(Z)\) is \(C^1\) as an \(L^2\) path. Each learned action is \(C^1\) in HS, hence operator norm, so the continuous bilinear product rule gives the next preactivation derivative in (V.39). Repeat through layer 3. This proves the chain rule along both capped and uncut strong trajectories; it assumes no Fréchet differentiability of the activation Nemytskii map on the whole \(L^2\) space.

Strong \(L^2\) node convergence has an almost-sure subsequence for each fixed time. Fatou's lemma passes (V.26), (V.35) to the cap flow:
\[
 \sup_{t\le T}\|X_R(t)\|_p\le K_{R,T}\sqrt p,\qquad p\ge2,    \tag{V.43}
\]
for every primary field and hidden velocity. This is \(\sup_t\|X(t)\|_p\), not \(\|\sup_t|X(t)|\|_p\). The constant is independent of the exponent. Applying (V.40), (V.42) at two flow times also gives a \(K_{R,T}|t-s|^{1/2}\) \(L^2\) velocity modulus, since raw state and direction are Lipschitz in time at fixed cap. No bound on the growth of \(K_{R,T}\) with \(R\) is claimed.

## V.7. Fixed-cap finite GF and fine raw Euler, including the actual readout

At a fixed auxiliary mesh, the primary law in F identifies every node contraction. Exact matrix unrolling gives, for \(\ell=2,3\),
\[
 \max_k\|W_{\ell,k}^{(n)}\|_{\rm op}
 \le\|W_{\ell,0}^{(n)}\|_{\rm op}
  +\sum_{j,b}h_j|p_{j,b}^{(n)}|\|\delta_{j,b}^{\ell,(n)}\|_n
                                    \|h_{j,b}^{\ell-1,(n)}\|_n.       \tag{V.44}
\]
Every term in the finite sum converges, and its limit is bounded uniformly over sufficiently fine population meshes by their primal bound. The first-layer and readout norms at the finitely many nodes converge as well; include the full initial \(d\)-tuple of first weights as a root when its norm is needed. Consequently a deterministic enlarged finite primal ball with slack contains all coarse nodes and raw interpolants with probability tending to one at each fixed sufficiently fine mesh. This proves the finite primal events used in V.3. It uses only the primary fixed-program law, initial operator bounds and update lengths; it is independent of the derivative and velocity estimates.

The finite readout in (V.5) is never reset in training. Its normalized norm is
\[
                       \|C_0^{(n)}\|_n=O_{\Pr}(n^{-1}).       \tag{V.45}
\]
At a fixed cap and fixed transcript, compare it to a same-matrix auxiliary program whose readout root is zero. Stopped finite-step Lipschitz comparison, with the primal slack just established for the zero-root program, gives state and query error \(O_{\Pr}(n^{-1})\); the comparison closes without exit. Thus the actual program has the same fixed-transcript population limit \(C_0=0\). This auxiliary argument justifies the vanishing root within F. Every actual finite GF/GD and every same-width cap comparison below retains the nonzero readout (V.5).

Let \(\theta_{R,n}\) be finite capped flow, or exact raw Euler for \(F_R\) with any deterministic \(\eta_n\to0\). Let \(\theta^\pi_{R,n}\) be the same-width, same-initialization coarse Euler reference. On the event from (V.44), deterministic stopped comparison gives
\[
 \sup_{t\le T}\|\theta_{R,n}(t)-\theta^\pi_{R,n}(t)\|_{\mathcal X}
                                \le K_{R,T}(|\pi|+\eta_n),    \tag{V.46}
\]
where \(\eta_n=0\) denotes flow. To avoid presupposing existence through \(T\), compare until exit. The coarse interpolant has differential-equation defect at most \(L_0M_0|\pi|\), the fine Euler interpolant has defect at most \(L_0M_0\eta_n\), and a flow has zero defect. Integral Gronwall keeps the discrepancy below fixed slack. No exit occurs, and finite-dimensional local existence continues capped GF through \(T\); the same comparison bounds the fine Euler nodes. All constants are width independent at this cap.

At any \(t\), its actual raw direction differs from \(F_R(\theta^\pi_{R,n}(t_k))\), for the preceding coarse node \(t_k\), by at most \(K_{R,T}(|\pi|+\eta_n)\). For fine Euler this uses its preceding fine node and its bounded within-step displacement; it does not substitute the vector field at the interpolated state. Apply (V.40) with the coarse node as reference:
\[
 \sup_{t\le T}\|V_{R,n}(t)-V^\pi_{R,n,k}\|_{\rm sum,2}
 \le K_{R,T}\left[(1+M)(|\pi|+\eta_n)
              +\max_k\sum_{\ell,i}\mathcal T_{M,n}(P^{\ell,\pi}_{R,n,k,i})\right],
                                                               \tag{V.47}
\]
where \(V\) is the full hidden velocity tuple and
\(\mathcal T_{M,n}(v)=\|(|v|-M)_+\|_n\).

For fixed \(\pi,M\), V.5 gives joint empirical \(\mathcal W_2\) convergence of all coarse node velocities. Positive-part tail norms are 1-Lipschitz, so all the finitely many tail norms in (V.47) converge to their population counterparts, bounded by \(K_{R,T}/M\) using (V.35), (V.42). Consequently, for every \(\varepsilon>0\), the probability that the left side exceeds
\(K_{R,T}[(1+M)|\pi|+M^{-1}]+\varepsilon\) tends to zero. At the fixed mesh choose \(M=|\pi|^{-1/2}\), giving width-limit bound \(K_{R,T}\sqrt{|\pi|}\). This is a width-limit upper bound in probability, not an almost-sure uniform finite-width estimate.

Let \(\mu_{R,n,\ell}(t)\) be the empirical law of a same-layer tuple containing all three samples of chosen primary fields and hidden velocities; the readout is included only in layer 3. Coupling actual and coarse observations by their neuron indices gives
\[
\begin{aligned}
 \sup_{t\le T}\mathcal W_2(\mu_{R,n,\ell}(t),\mu_{R,\ell}(t))
 \le{}&\sup_t\|X_{R,n,\ell}(t)-X^\pi_{R,n,\ell,k}\|_n\\
 &+\max_k\mathcal W_2(\mu^\pi_{R,n,\ell,k},\mu^\pi_{R,\ell,k})\\
 &+\sup_t\|X^\pi_{R,\ell,k}-X_{R,\ell}(t)\|_2 .
\end{aligned}                                                    \tag{V.48}
\]
At fixed mesh the middle term vanishes by V.5. The others tend to zero under the subsequent mesh refinement by (V.38), (V.40), (V.47). Therefore
\[
 \sup_{t\le T}\mathcal W_2(\mu_{R,n,\ell}(t),\mu_{R,\ell}(t))
                       \longrightarrow0\quad\hbox{in probability}. \tag{V.49}
\]
For finitely many observation times, concatenate their coordinates and use the same neuron coupling. Squared costs sum over the finitely many times, and the fixed-program law is joint for the complete coarse transcript. This proves joint-time \(\mathcal W_2\) convergence, retaining all correlations within each layer.

The tail functional is also 1-Lipschitz in \(\mathcal W_2\). Under a coupling,
\[
 |\mathcal T_u(X)-\mathcal T_u(Y)|
 \le\|(|X|-u)_+-(|Y|-u)_+\|_2\le\|X-Y\|_2.
\]
Thus all fixed-level empirical tail norms converge uniformly in time. From (V.43) and the moment-to-tail calculation in V.2 one obtains, at a fixed cap,
\[
 \lim_{u\to\infty}\limsup_{n\to\infty}
 \Pr\!\left(\sup_{t\le T}
 \|X_{R,n}(t)\mathbf1_{\{|X_{R,n}(t)|>u\}}\|_n^2>\varepsilon\right)=0. \tag{V.50}
\]
This is asymptotic empirical uniform integrability of second moments; no empirical fourth-moment or finite-width exponential-moment estimate is asserted.

The order throughout V.7 is width at fixed cap, auxiliary mesh and truncation level, followed by mesh refinement. The raw step \(\eta_n\to0\) contributes only its deterministic Euler defect. No Gaussian identification for an increasing transcript length occurs.

## V.8. Full true backward observations and full fixed-cap kernels

On a capped state, true fields \(b_i^\ell=d_\phi(z_i^\ell)q_i^\ell\) are observations distinct from its update fields \(\delta_{R,i}^\ell\). We establish their laws explicitly.

At a fixed finite transcript append, in order, \(b_i^3=d_\phi(z_i^3)C\), the current transpose query \(B^*b_i^3\), the true middle gate, the current transpose query \(A^*b_i^2\), and the true bottom gate. Approximate each gate by \(d_\phi(z)\tau_M(q)\), using nested levels for dependent gates. At fixed levels F applies. Equation (V.37) proves that bounded-gate multiplication preserves joint \(\mathcal W_2\) convergence, and positive-part tail convergence makes its empirical clipping error vanish in the width-limit \(L^2\) sense. A bounded current action transfers input error to output error; learned increments are included as finite rank contractions. Iterate through the finite appended chain. Every true backward observation therefore has its joint empirical \(\mathcal W_2\) limit equal to the corresponding population action and product.

This argument is an observational closure statement only. It does not assert an expected-derivative formula for arbitrary untruncated products without domination. When such formulas are needed at initialization, lemma V.I supplies their separate truncation and domination proof, including the full source covariances and current returns. For the kernel limits here, action continuity suffices.

There is also a trajectory comparison. If \(\alpha=\|\theta-\bar\theta\|_{\mathcal X}\), then
\[
 \sum_{\ell,i}\|b_i^\ell-\bar b_i^\ell\|_2
 \le K\left[(1+M)\alpha+\mathcal T_M(\bar C)
      +\sum_i\{\mathcal T_M(\bar q_i^2)+\mathcal T_M(\bar q_i^1)\}\right], \tag{V.51}
\]
where barred \(q\)'s are true incoming fields. Use (V.41) with \(\bar q\) in place of \(\bar P\), and substitute downwards through the bounded transpose actions. Each new \(M\) multiplies a forward discrepancy controlled by (V.8), so the estimate has a single \(M\).

The true backward map is strongly continuous along converging states on a bounded primal ball: use (V.37) and bounded-action continuity recursively. Along a capped \(C^1\) trajectory the true incoming fields are continuous \(L^2\) paths, with compact time images. Such an image has uniformly vanishing positive-part tails: cover it by finitely many \(L^2\) balls of radius \(\varepsilon\), use the 1-Lipschitz tail property, then send \(M\to\infty\) at the finitely many centers. Hence population coarse Euler true fields converge uniformly to the cap-flow fields, by applying (V.51) with the flow as reference and (V.38). Their tail norms also converge uniformly.

For finite cap GF/fine Euler against the same-width coarse reference, use (V.51). At fixed mesh and \(M\) the coarse empirical tail norms converge by the finite observational closure. Take width, then mesh refinement at fixed \(M\), then \(M\to\infty\), using the compact-tail conclusion. This proves (V.49) and joint-time convergence for the true backward tuple as well.

The four full kernel blocks at any state are
\[
 K^1_{ij}=\Gamma_{ij}\langle b_i^1,b_j^1\rangle,\qquad
 K^2_{ij}=\langle b_i^2,b_j^2\rangle\langle h_i^1,h_j^1\rangle,
\]
\[
 K^3_{ij}=\langle b_i^3,b_j^3\rangle\langle h_i^2,h_j^2\rangle,\qquad
 K^4_{ij}=\langle h_i^3,h_j^3\rangle.                          \tag{V.52}
\]
Finite definitions use normalized inner products. Joint \(\mathcal W_2\) convergence implies convergence of each second moment: under a coupling,
\[
 |E[XY]-E[\bar X\bar Y]|
 \le\|X-\bar X\|_2\|Y\|_2+\|\bar X\|_2\|Y-\bar Y\|_2.
\]
The bounds are uniform in time. Hence every entry of every block, predictions, and loss converge uniformly in time for finite capped GF and fine Euler. In particular all off-diagonals are retained. On a capped trajectory (V.52) is the observed true gradient kernel; it need not be the coefficient matrix of that surrogate trajectory's prediction equation.

## V.9. Same-width comparison for uncut finite GF and exact raw GD

Compare actual uncut finite GF \(\theta_n\) with its same-width physical cap-flow reference \(\theta_{R,n}\), retaining the common nonzero initialization (V.5). By V.7 the reference lies with probability tending to one in a fixed enlarged primal ball containing the population cap path with slack. This comparison ball can be chosen independently of \(R\), using G's cap-independent primal bounds; the width needed for its high-probability containment may depend on the fixed \(R\). Raw direction bounds on that ball are independent of cap.

At fixed \(R\), (V.49) passes reference incoming positive-part tail norms uniformly in time. Since
\[
 |q|\mathbf1_{\{|q|>R\}}\le2(|q|-R/2)_+,
\]
the width-limit upper bound for the reference tail term in (V.11) is at most \(Ke^{-cR^2}\), by (V.12) with adjusted constants. Until uncut exit, Gronwall in (V.11) gives a width-limit state error
\[
                   \varepsilon_R=K_Te^{K_TR-cR^2}\longrightarrow0.   \tag{V.53}
\]
Choose a large fixed cap so this is smaller than primal slack, and then take width. The first-exit comparison rules out exit with probability tending to one. Substitution into (V.11) also gives raw-direction and backward-field error bounds tending to zero with \(R\); polynomial factors are absorbed into a smaller Gaussian rate.

Finite uncut GF exists globally even before this probability argument. Its finite-dimensional field is locally Lipschitz. The exact gradient identity is
\[
 \frac d{dt}\frac12\sum_i(f_i-y_i)^2
 =-\left[\frac dn\|\dot W^1\|_F^2+\|\dot A\|_F^2+
                         \|\dot B\|_F^2+\|\dot C\|_n^2\right].       \tag{V.54}
\]
Its raw Hilbert length on \([0,T]\) is at most \(\sqrt{TL(0)}\), so it cannot escape to infinity in finite-dimensional parameter space in finite time. Local existence therefore continues it globally. The sum norm (V.1) is equivalent to this Hilbert metric up to fixed numerical constants. This identity is used for true finite GF only.

For raw GD let \(t_k=k\eta_n\), \(\eta_n=n^{-2}\), and
\(E(t)=\sup_{s\le t}\|\theta_n(s)-\theta_{R,n}(s)\|_{\mathcal X}\).
Its direction on the interval is \(F_\infty(\theta_n(t_k))\). Apply (V.11) at \(t_k\) against the cap reference there. The additional difference between \(F_R(\theta_{R,n}(t_k))\) and \(F_R(\theta_{R,n}(t))\) is at most \(L_RM_R\eta_n\). Before exit,
\[
 E(t)\le K(1+eR)\int_0^tE(s)\,ds
  +Kt\sup_{s\le T}\sum_{Q\in\mathscr Q_{R,n}(s)}
                           \|Q\mathbf1_{\{|Q|>R\}}\|_n
  +K_{R,T}t\eta_n.                                          \tag{V.55}
\]
The preceding-node discrepancy is bounded by \(E(s)\), since \(t_k\le s\). This yields (V.53) and the same no-exit conclusion. For actual raw directions, use the same pointwise estimate at \(t_k\) and the bounded cap within-step variation. No width-independent Lipschitz bound for the uncut field is used. All finite GD iterates are well defined as finite compositions of algebraic and smooth operations; the comparison supplies the required finite-horizon bound with probability tending to one.

The limits are width at fixed cap after the capped auxiliary-mesh limit, then cap removal. The exact raw step enters solely through \(K_{R,T}\eta_n\). This also proves convergence for any deterministic raw step tending to zero. Both algorithms can use the same initialized cap reference, so their observable limits hold jointly; their same-neuron coupled limiting trajectories agree.

Forward and backward convergence now follow from (V.8), (V.11), (V.53). Population cap fields already converge strongly by V.2. Hence (V.52), predictions, and loss converge uniformly in physical time for the true finite GF and exact raw GD. In this last comparison capped update fields \(\delta_R\) can serve as references, because (V.11) compares them directly to true uncut \(b\). Section V.8 separately supplies the full true kernel assertion for fixed-cap trajectories.

## V.10. Cap removal for hidden velocities with ordered tails

Raw cap states and directions converge uniformly by (V.13). Apply (V.40) using the uncut population velocity as reference. Its preactivation velocities are continuous \(L^2\) paths by V.6, so their compact time images have uniformly vanishing positive-part tails. At fixed \(M\),
\[
 \limsup_{R\to\infty}\sup_{t\le T}\|V_R(t)-V(t)\|_{\rm sum,2}
 \le K\sum_{\ell,i}\sup_{t\le T}\mathcal T_M(P_i^\ell(t)).
\]
Then \(M\to\infty\) proves uniform strong population cap-velocity convergence. The positive-part tail functional is 1-Lipschitz; therefore sufficiently large population caps inherit uniformly vanishing velocity tails from this strong convergence. No estimate for the growth of fixed-cap moment constants in (V.43) is required.

For a finite uncut algorithm versus its same-width cap-flow reference, (V.40) gives
\[
 K\left[\beta_{R,n}+(1+M)\alpha_{R,n}
        +\sum_{\ell,i}\sup_{t\le T}
                      \mathcal T_{M,n}(P^\ell_{R,n,i}(t))\right],     \tag{V.56}
\]
where \(\alpha,\beta\) are raw state and actual direction discrepancies. Their width-limit upper bounds tend to zero with \(R\), by (V.53)--(V.55). The constant in (V.56) depends only on the common primal/direction ball and activation, and is independent of \(R,M\). At fixed \(R,M\), V.7 passes all empirical reference tails to the capped population tails. Send \(R\to\infty\) at fixed \(M\), using the just-proved strong population velocity convergence; then \(M\to\infty\). The bound vanishes.

Neuron-index coupling, capped \(\mathcal W_2\) convergence, and population cap convergence now prove same-layer uncut joint field/velocity \(\mathcal W_2\) convergence uniformly in time. A finite concatenation gives joint laws at any finitely many times. The raw-GD one-sided directions satisfy the same estimates: neighboring reference times differ by at most \(\eta_n\), and its direction is continuous. Node choices do not affect integrated speeds.

The limit orders used are:

1. For product-query identification: fixed transcript and nested clips, width, inner clip removal, outer clip removal.
2. For fixed-cap trajectory identification: fixed cap and auxiliary mesh, width, auxiliary mesh refinement.
3. For population velocity cap removal: cap at fixed velocity-tail level \(M\), then \(M\to\infty\).
4. For finite uncut velocity comparison: width at fixed cap and \(M\), cap at fixed \(M\), then \(M\to\infty\).

In particular, no cap-dependent velocity-moment constant is multiplied by an uncontrolled cap-removal error.

## V.11. Supremum-norm path laws and integrated squared speeds

For layer \(\ell\), let the hidden path tuple be
\[
 X_\ell(t)=(z_1^\ell,z_2^\ell,z_3^\ell,h_1^\ell,h_2^\ell,h_3^\ell)(t).
\]
Its coordinates are almost-everywhere absolutely continuous. Finite recomputed hidden fields along raw interpolation have the same property. The chain rule (V.39), bounded actions and \(\phi'\), and bounded raw directions give a uniform RMS speed bound on the stopped primal/direction ball. The no-exit comparisons remove stopping with probability tending to one. Population speeds are bounded in \(L^2\) on compact horizons.

For an absolutely continuous vector path \(x\) and its linear interpolation \(I_hx\) on a fixed observation grid of maximum interval length \(h\), at \(t\in[u,v]\),
\[
 |x(t)-I_hx(t)|
 \le |x(t)-x(u)|+|x(v)-x(u)|
 \le2\sqrt h\left(\int_u^v|x'(s)|^2\,ds\right)^{1/2}.
\]
Hence
\[
             \|x-I_hx\|_\infty^2
                         \le4h\int_0^T|x'(s)|^2\,ds.         \tag{V.57}
\]
Averaging this same-neuron coupling cost gives a squared path-space \(\mathcal W_2\) approximation cost bounded by \(4h\) times the integrated RMS speed squared, for finite and population laws. Initial second moments and the speed bound also ensure finite second moments of the path supremum norm, so the measures belong to \(\mathcal P_2(C([0,T];\mathbb R^6))\).

At a fixed observation grid, joint node \(\mathcal W_2\) convergence passes through linear interpolation, a Lipschitz map from the finite Euclidean node tuple to the path supremum norm. Apply a triangle inequality with finite and population observation-grid interpolants, first take width at that fixed grid, then let \(h\to0\) in (V.57). Therefore, for both exact algorithms,
\[
 \mathcal W_2\left(\frac1n\sum_{\alpha=1}^n
                  \delta_{X_{\ell,n,\alpha}(\cdot)},
                  \operatorname{Law}(X_\ell(\cdot))\right)
             \longrightarrow0\quad\hbox{in probability},     \tag{V.58}
\]
in \(C([0,T];\mathbb R^6)\) equipped with its supremum norm. This final approximation is necessary: joint fixed-time laws alone do not imply (V.58).

Uniform-time velocity \(\mathcal W_2\) convergence implies uniform convergence of squared norms and all same-layer cross second moments. Under any coupling,
\[
 |\|u\|_2^2-\|v\|_2^2|
                  \le(\|u\|_2+\|v\|_2)\|u-v\|_2,
\]
and the product estimate following (V.52) handles cross moments. The norms are uniformly bounded by the primal/direction bounds. Multiplying the uniform error by \(T\) bounds the error in each time integral. In particular
\[
 \int_0^T\|P^\ell_{n,i}(t)\|_n^2\,dt,\qquad
 \int_0^T\|U^\ell_{n,i}(t)\|_n^2\,dt
\]
converge in probability to their population counterparts, as do their within-layer integrated cross products. These are actual neuron-coordinate speeds from the chain rule, not an assertion that their norms equal metric derivatives of the marginal probability laws.

Raw block speeds converge as well. For uncut GF, (V.4), the rank-one norm identity, and (V.52) give, for each of its four blocks,
\[
                 \|\dot\theta^{(\ell)}(t)\|_{\rm raw}^2
                           =p(t)^TK^\ell(t)p(t).
\]
For exact raw GD the same identity holds with the preceding-node residual and kernel, since that is its actual raw direction. Uniform convergence of predictions and all kernel blocks, together with population continuity and \(\eta_n\to0\), therefore gives convergence of the blockwise squared raw speeds uniformly in time and after time integration. For capped dynamics the identical assertion uses the three capped-update backward Grams in place of the true hidden kernel blocks; those Grams converge by the primary fixed-cap law. Their readout block remains \(K^4\).

Initialized and current action orientations are retained on any fixed finite collection of canonical generated probes. Include the probes and observations in F, or take their common-space \(L^2\) limits. In a same-width or common-population comparison,
\[
 \|Wu-\bar W\bar u\|_2
 \le\|W-\bar W\|_{\rm op}\|u\|_2+\|\bar W\|_{\rm op}\|u-\bar u\|_2,
\]
and the same holds for adjoints. Difference operator norms are bounded by HS differences, and current operator norms were bounded by exact update lengths. Thus both orientations pass through the limits. Population cap increments converge strongly in HS. If finite learned-increment HS contractions are included as scalar observations, exact rank unrolling and Riemann approximation express them through bounded products of the already converging field contractions. No unspecified cross-width operator identification is asserted.

All assertions are full-sequence convergence in probability on every fixed finite physical horizon, for the one fixed activation. The constants may depend on the fixed data and horizon. At each probabilistic application the cap, auxiliary mesh and query truncations are fixed first, and their subsequent removal has been explicitly ordered.

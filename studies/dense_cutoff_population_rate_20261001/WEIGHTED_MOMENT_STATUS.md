# Status of the finite weighted-response route

This is the source-based assessment requested by the user, not a new rate theorem. Scientific inputs are this study's cutoff comparison, three-error transfer, width route, finite-tail proof, prescribed-control fluctuation proof, and their checks.

**Partially attempted: restricted mixed products are proved, but a general finite-network hierarchy of mixed response and carrier moments has not been developed.** It has not been disproved or exhausted. The strict dense-to-population root-width theorem remains open.

## Proved, with explicit scope

1. The general deterministic comparison in [CUTOFF_REMOVAL_ROUTE.md](CUTOFF_REMOVAL_ROUTE.md), equations (23)–(33), bounds finite cutoff removal by residual-weighted empirical carrier tails. It does not require simultaneous cutoff inactivity. With original carriers \(p_a^{(L)}=w\) and \(p_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)}\), its source is
   \[
   Z_n(M)=\mathbf1_{\mathcal G_n}\int_0^\infty\rho_n(t)
     \sum_{\ell=1}^L\max_a
     \left(\frac1n\sum_i|p_{a,i}^{(\ell)}(t)|^2
       \mathbf1_{\{|p_{a,i}^{(\ell)}(t)|>M\}}\right)^{1/2}dt.
   \]
   Here \(\mathcal G_n\) is the initialized fitting event and \(\rho_n\) the original residual RMS.

2. [THREE_ERROR_REASSEMBLY.md](THREE_ERROR_REASSEMBLY.md), Sections 2–3, proves the conditional implication: uniform time-marginal exponential moments of the actual finite carriers on \(\mathcal G_n\) imply
   \[
   \mathbb E[\mathbf1_{\mathcal G_n}
       \mathcal E_\mu(f_n,f_{n,M})^2]\le C_\mu e^{-cM^2}.
   \]
   The prediction norm includes the whole training-time supremum. The proof uses the integrable residual weight, not a maximum over neurons and time. The general finite exponential-moment premise is unproved.

3. [POPULATION_CAVITY_ATTEMPT.md](POPULATION_CAVITY_ATTEMPT.md), equations (8)–(18), proves finite sensitivity/carrier estimates for two tanh layers, orthonormal inputs, and prescribed deterministic integrated-residual controls. In that note \(p=F(z^{(1)})\) is a transformed coordinate and \(k=W^\top\delta^{(2)}\) is the carrier; this differs from the carrier symbol \(p\) above. A tangent-Gram derivative contains
   \[
   \frac1n\sum_i\psi''(p_i)\,\Delta p_i\,k_i^2,
   \]
   bounded by
   \[
   4\frac{\|\Delta p\|_2}{\sqrt n}
       \left(\frac1n\sum_i k_i^4\right)^{1/2}.
   \]
   Initialization/state-variation bounds and fourth carrier moments control the Gaussian initialization gradient of this Gram entry at order \(1/n\) in squared mean.

   The same proof controls exponentially weighted initial-feature perturbations and the correlated product of RMS feature difference with RMS squared carrier. The initial-feature perturbation is deterministic before averaging over the hidden matrix. The resulting Lipschitz estimate concerns the matrix-averaged map, not arbitrary matrix-dependent perturbation weights.

   The consequence is a strict root-width fluctuation bound, uniform over bounded activity time, around the finite-width mean for each deterministic control. It does not identify population bias or permit substitution of an adaptive random control. The complete internal reconstruction is [POPULATION_CAVITY_CHECK.md](POPULATION_CAVITY_CHECK.md).

## Attempted but not closed

The restricted cavity attempt isolated the mean-response obstruction through a deleted-neuron decomposition. It obtained
\[
k_{a,i}=W_{0,i}^{\top}\delta_a^{(2),-i}+R_{a,i},
\qquad |R_{a,i}|\le CS,
\]
where \(S\) bounds total driver variation and the superscript \(-i\) denotes the network with that neuron removed, retaining normalization \(n\). The remainder includes a nonvanishing population response and cannot be discarded as a width error.

The available Euclidean bound on the cavity response difference is \(O(1)\), or \(O(n^{-1/2})\) after RMS normalization. This does not identify the response kernel or make its nonlinear remainder vanish: a coordinatewise quadratic remainder involves \((\sum_j|\Delta z_j|^4)^{1/2}\), which need not be small merely because \(\|\Delta z\|_2=O(1)\). Distribution of the response across coordinates, and consistency of its response kernel, remain unproved. See Section 6 of the cavity attempt.

The general response-weighted repeated-query estimate in [WIDTH_ROUTE.md](WIDTH_ROUTE.md), Section 6, was formulated, not proved or exhaustively attempted. It requires empirical contraction errors centered at their population values, jointly controlled with the finite evolution's responses to those errors. No closed general mixed-moment hierarchy was obtained.

## A precise unclosed mixed quantity

The following identifies a useful type of estimate, not an already established theorem or a necessary condition. Fix a layer, sample, and activity time; the desired constants are uniform in width and time. The proposed comparison must specify the admissible source directions and their size \(\varepsilon\); arbitrary directions of small RMS need not satisfy the fourth-moment bound below. In the original dense recursion, \(\delta=\phi'(z)\odot p\). Let \(U=D z\) and \(V=D p\) be directional responses to one such initialization or feedback-source perturbation. For a smooth activation such as tanh,
\[
D\delta=\phi''(z)\odot p\odot U+\phi'(z)\odot V.
\]
An averaged squared-response estimate therefore encounters
\[
\mathbb E\left[\mathbf1_{\mathcal G_n}\frac1n
                 \sum_i|p_i|^2|U_i|^2\right].
\tag{A}
\]
For the manuscript's \(C^{1,1}\) activations the same product occurs in finite differences:
\[
|[\phi'(z+e)-\phi'(z)]p|
 \le \operatorname{Lip}(\phi')\,|pe|.
\]
The existing general comparison splits this gate difference at a threshold \(R\), paying a coefficient proportional to \(R\) and a carrier-tail source. It does not give a cap-independent mixed-response estimate.

One useful sufficient target for exceptional coordinates is
\[
\mathbb E\left[\mathbf1_{\mathcal G_n}\frac1n
  \sum_i|p_i|^2|U_i|^2\mathbf1_{\{|p_i|>M\}}\right]
\le C\varepsilon^2e^{-cM^2},
\tag{B}
\]
where \(\varepsilon\) measures the prescribed size of the specific source perturbation. This is not asserted for every arbitrary matrix-dependent direction. Hölder would give (B) from suitable finite exponential carrier moments and
\[
\mathbb E\left[\mathbf1_{\mathcal G_n}\frac1n
                       \sum_i|U_i|^4\right]\le C\varepsilon^4.
\tag{C}
\]
Neither general estimate is proved. The lower carrier response also satisfies
\[
D p^{(\ell)}
 =(D W^{(\ell+1)})^\top\delta^{(\ell+1)}
   +W^{(\ell+1)\top}D\delta^{(\ell+1)}.
\]
Thus (C) needs mixed estimates after reused-matrix multiplication. A spectral bound controls Euclidean norm, not coordinate fourth moments with width-independent constants.

The restricted proof's exponentially weighted estimate fixes its perturbation before the matrix expectation. Substituting an adaptive matrix-dependent response into it is unjustified. This is an unavailable extension of the argument, not evidence that such an extension is impossible.

## Not yet attempted systematically

- Closing (A)–(C) for a general finite or stopped finite network, nonorthogonal data, and arbitrary fixed depth.
- Higher response variations and their carrier products needed to identify population response and bound nonlinear cavity remainders.
- Uniform dependence on moment order, cutoff, width, and total learning activity for such a hierarchy.
- A full population-centered, activity-weighted repeated-feedback estimate, including finite-width mean bias and adaptive residual selection.

Failure of a maximum-signal argument does not disprove this route. Weighted cutoff removal is already a proved conditional route. The general finite mixed estimates and the full population comparison remain open.

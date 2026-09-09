# Adaptive Gram martingale for the real comparison perturbation

This note proves a conditional adaptive estimate for the perturbations in
[Panahi v1, PDF (6), (9)](https://arxiv.org/pdf/2603.09310v1), with one
centered mixture component, \(R=I,J=1,z=0\). It does not assume the
queries are independent of the auxiliary Gaussian matrix. The effective
rank premise below remains a premise for the actual perturbed dynamics.

## 1. Causal setup and exact identities

Fix \(n,m,K\ge1\) and \(\sigma>0\). Let \(\Gamma\in
\mathbb R^{K\times K}\) have independent standard Gaussian entries.
Let \(\mathcal H\) contain all other random arrays and seeds, jointly
independent of \(\Gamma\). In the perturbed-original process these
include \(X,U,V\); revealing their entire arrays initially does not
reveal any entry of \(\Gamma\).

Use finite-valued measurable causal query maps with the source's order
\(\theta_l\to p_l\to\omega_l\to q_l\). Define
\[
\mathcal F_l=\mathcal H\vee\sigma(\Gamma_{ij}:i,j\le l),\qquad
\mathcal F_{l-1/2}=\mathcal F_{l-1}\vee
 \sigma(\Gamma_{lj}:j<l).
\]
Here \(\theta_l\in\mathbb R^n\) is \(\mathcal F_{l-1}\)-measurable,
\(p_l,\omega_l\in\mathbb R^m\) are
\(\mathcal F_{l-1/2}\)-measurable, and \(q_l\) is
\(\mathcal F_l\)-measurable. The assertions follow inductively from
(9): its reverse strict-triangular term first uses the fresh row
\(\Gamma_{lj},j<l\); its forward triangular term subsequently uses
the fresh column \(\Gamma_{il},i\le l\). The other terms are already
measurable from the queries and \(\mathcal H\).

For each leading history take the positive-diagonal upper Cholesky
factors
\[
A_\theta^TA_\theta=\Theta^T\Theta+\sigma^2I,\qquad
A_\omega^TA_\omega=\Omega^T\Omega/m+\sigma^2I.
\]
The leading blocks of these factors and their inverses agree between
prefixes. Thus the columns
\[
t_i=(\Theta A_\theta^{-1})_i\in\mathbb R^n,\qquad
s_i=(\Omega A_\omega^{-1})_i/\sqrt m\in\mathbb R^m
\]
never change when later queries arrive. In particular \(t_l\) is
known before the fresh row and \(s_l\) before the fresh column.
An arbitrary horizon-dependent Cholesky sign convention is not allowed.

Put
\[
\mathsf T_l=\sum_{i\le l}t_it_i^T\preceq I_n,\qquad
\mathsf S_l=\sum_{i\le l}s_is_i^T\preceq I_m,
\quad \rho_{\theta,l}=\operatorname{tr}\mathsf T_l,
\quad \rho_{\omega,l}=\operatorname{tr}\mathsf S_l.              \tag{1}
\]
Indeed \(\mathsf T_l=\Theta_l(\Theta_l^T\Theta_l+
\sigma^2I)^{-1}\Theta_l^T\), and the singular-value decomposition
gives eigenvalues \(d_j^2/(d_j^2+\sigma^2)\le1\); the same
calculation applies to \(\Omega_l/\sqrt m\). These traces are the
regularized effective ranks. They increase with the prefix, and
\(\|t_i\|,\|s_i\|\le1\).

Define the rectangular matrices
\[
B_{l-1/2}=\sum_{i\le l,j<l}t_i\Gamma_{ij}s_j^T,\qquad
B_l=\sum_{i,j\le l}t_i\Gamma_{ij}s_j^T,\qquad B_0=0.
\]
Their half-step increments are
\[
B_{l-1/2}-B_{l-1}=t_l a_l^T,
\quad a_l=\sum_{j<l}s_j\Gamma_{lj},\qquad
B_l-B_{l-1/2}=b_l s_l^T,
\quad b_l=\sum_{i\le l}t_i\Gamma_{il}.                        \tag{2}
\]
The first fresh vector is conditionally \(N(0,\mathsf S_{l-1})\),
and the second is conditionally \(N(0,\mathsf T_l)\), at their
respective preceding half-steps. Hence \(B\) is a rectangular matrix
martingale. Its increments have finite moments at every fixed finite
\(n,m,K\), by (1) and the Gaussian moments. No bound on the raw
query norms is needed for this assertion.

Let \(g_l\) be the forward \(\Gamma\)-perturbation in (9), and
\(k_l\) the reverse perturbation divided by \(\sqrt m\).
The exact decompositions are
\[
g_l=\frac{B_l\omega_l}{m}
 +\frac{\sigma^2}{\sqrt m\,A_{\omega,ll}}b_l,\qquad
k_l=\frac{B_{l-1/2}^T\theta_l}{\sqrt m}
 +\frac{\sigma^2}{\sqrt m\,A_{\theta,ll}}a_l.                  \tag{3}
\]
For \(j\le l\), the Gram identity gives
\[
\frac{s_j^T\omega_l}{\sqrt m}
=\big[A_\omega-\sigma^2A_\omega^{-T}\big]_{jl},
\]
so \(A_{\omega,jl}=s_j^T\omega_l/\sqrt m\) for \(j<l\),
and the diagonal has the additional \(\sigma^2/A_{\omega,ll}\).
The same identity holds for \(A_\theta\). Substitution into the two
triangular terms of (9) proves (3), including the strict reverse sum.
Furthermore, each diagonal obeys \(A_{ll}\ge\sigma\): its squared
Schur complement is
\(\sigma^2+x_l^T[I-X_{l-1}(X_{l-1}^TX_{l-1}+
\sigma^2I)^{-1}X_{l-1}^T]x_l\ge\sigma^2\).
Thus both residual coefficients in (3), apart from \(m^{-1/2}\),
are at most \(\sigma\).

## 2. Quantitative adaptive bound

Take deterministic \(R_\theta,R_\omega\ge0\),
\(r=\max(R_\theta,R_\omega)>0\), and \(0<\alpha<1\). Set
\[
E_R=\{\rho_{\theta,K}\le R_\theta,
       \rho_{\omega,K}\le R_\omega\},\quad
u=\log(4K/\alpha),\quad c=\sqrt{2r+4u},
\quad v=\log(2(n+m)/\alpha),
\quad L=2\sqrt{rv}+\tfrac23cv.                               \tag{4}
\]
Then
\[
\mathbb P\left(E_R\cap
 \left\{\max_h\|B_h\|_{\rm op}>L
 \ \text{or}\ \max_l(\|a_l\|\vee\|b_l\|)>c\right\}\right)
\le\alpha,                                                  \tag{5}
\]
where \(h\) runs over all half and full steps through \(K\).
If additionally
\(\max_l\|\theta_l\|\le A\),
\(\max_l\|\omega_l\|/\sqrt m\le C\), then outside the same
exceptional event, on \(E_R\),
\[
\max_l\|g_l\|\le\frac{CL+\sigma c}{\sqrt m},\qquad
\max_l\|k_l\|\le\frac{AL+\sigma c}{\sqrt m}.                 \tag{6}
\]
These norm bounds may instead be imposed on an event and intersected
with \(E_R\). If \(r=0\), both Gram contractions are zero on
\(E_R\), and the claimed perturbations are zero there.

### Proof, including localization and truncation

First stop accepting increments permanently before a rank threshold
would be exceeded. Before row \(l\), both \(\rho_{\theta,l}\)
and \(\rho_{\omega,l-1}\) are known; accept the row only while they
are within their thresholds. Before column \(l\),
\(\rho_{\omega,l}\) is also known; accept the column only if its
threshold has not been exceeded. These acceptance indicators are
predictable at their respective half-steps. The accepted process agrees
with \(B\) on \(E_R\). Its coefficients still refer to the original
adaptive histories; this construction does not alter the query dynamics.

For an accepted untruncated row increment \(X=t_la_l^T\), its two
conditional second-moment matrices are
\[
\mathbb E[XX^T\mid\mathcal F_{l-1}]
 =\rho_{\omega,l-1}t_lt_l^T,\qquad
\mathbb E[X^TX\mid\mathcal F_{l-1}]
 =\|t_l\|^2\mathsf S_{l-1}.
\]
For an accepted column increment \(Y=b_ls_l^T\), they are
\[
\mathbb E[YY^T\mid\mathcal F_{l-1/2}]
 =\|s_l\|^2\mathsf T_l,\qquad
\mathbb E[Y^TY\mid\mathcal F_{l-1/2}]
 =\rho_{\theta,l}s_ls_l^T.
\]
Summing along each realized path, (1) and the threshold rule imply
\[
W_{\rm left}\preceq
 R_\omega\sum_{\rm accepted\ rows}t_lt_l^T
 +\sum_{\rm accepted\ columns}\|s_l\|^2I_n
 \preceq2R_\omega I_n,
\]
\[
W_{\rm right}\preceq
 \sum_{\rm accepted\ rows}\|t_l\|^2I_m
 +R_\theta\sum_{\rm accepted\ columns}s_ls_l^T
 \preceq2R_\theta I_m.                                      \tag{7}
\]
In particular both predictable quadratic variations have norm at most
\(2r\). The unequal left/right constants matter: no factor \(K\)
has been introduced.

To bound increments without an unjustified Gaussian boundedness
assumption, multiply each accepted row increment by
\(\mathbf1_{\{\|a_l\|\le c\}}\), and each accepted column
increment by \(\mathbf1_{\{\|b_l\|\le c\}}\). Conditional
Gaussian symmetry makes the truncated increments centered. Their
conditional second moments are bounded in positive-semidefinite order
by the untruncated ones, so (7) remains valid. Their operator norms are
at most \(c\), since \(\|t_l\|,\|s_l\|\le1\).

At every accepted half-step the fresh Gaussian vector \(Z\) has
covariance at most the identity and trace at most \(r\). Its covariance
eigenvalues \(\lambda_j\in[0,1]\) give
\[
\mathbb E[e^{\|Z\|^2/4}\mid\text{past}]
=\prod_j(1-\lambda_j/2)^{-1/2}\le e^{r/2},\qquad
\mathbb P(\|Z\|>c\mid\text{past})\le e^{-u}.
\]
The product estimate uses \(-\log(1-x)\le2x\) for \(x\le1/2\).
A union bound over at most \(2K\) accepted half-steps costs at most
\(2Ke^{-u}=\alpha/2\). On its complement and \(E_R\), no
truncation or stopping occurred, and the truncated martingale agrees
with \(B\) at every half-step; all residual vectors have norm at most
\(c\).

Apply [Tropp, *Freedman's inequality for matrix martingales*,
Corollary 1.3](https://tropp.caltech.edu/papers/Tro11-Freedmans-Inequality.pdf).
For an \(n\times m\) matrix martingale with increment norms at most
\(c\) and both predictable quadratic variations at most \(2r\),
that corollary bounds the probability its norm ever exceeds \(x\) by
\[
(n+m)\exp\left[-\frac{x^2}{2(2r+cx/3)}\right].
\]
The truncated process starts at zero, is adapted and centered, has bounded
increments and thus is integrable, and satisfies (7); these verify every
hypothesis. For \(x=L\),
\(L^2\ge2v(2r+cL/3)\), so the bound is at most \(\alpha/2\).
Combining it with the truncation failure probability proves (5).
Finally (3), \(A_{ll}\ge\sigma\), and the query norm bounds prove
(6). None of these steps conditions on adaptive histories as though
their Gaussian law were unchanged.

## 3. What this resolves and what it does not

For \(n\asymp m\), polynomial \(K\) and \(\alpha^{-1}\),
\[
L=O\!\left(\sqrt{r\log m}
 +\sqrt{r+\log m}\,\log m\right).
\]
With bounded \(A,C,\sigma\), the two adaptive \(\Gamma\)-queries
in (6) vanish uniformly whenever
\(r\log^2m=o(m)\), on rank events whose probability tends to one.
For an Euler primitive over a fixed physical horizon \(T\), its
supremum is at most \(T\) times the corresponding query supremum.
This conclusion is compatible with the earlier causal counterexample:
\(B\) is a martingale, but multiplying it by adaptive queries need
not preserve centering or the frozen second-moment identity.

The additional \(\sigma U/\sqrt m\) and \(\sigma V/\sqrt m\)
normalized query noises have, by the same Gaussian norm calculation and
a union bound, maxima at most
\(\sigma\sqrt{2n/m+4\log(2K/\delta)/m}\) and
\(\sigma\sqrt{2+4\log(2K/\delta)/m}\), respectively, except on
an event of probability at most \(\delta\). They vanish when
\(n/m\) stays bounded, \(K\) is polynomial, and \(\sigma\to0\).
This assertion concerns their size; it gives no effective-rank estimate
for the histories they generate.

In particular, the deterministic slow-history effective-rank estimate
cannot simply be imposed on actual perturbed paths. Small direct query
noise can produce fresh directions at the same scale as the Gram
regularization and invalidate the required rank bound. An actual rank
estimate (or another replacement for that premise), nonlinear stability
under these query perturbations, regularization removal, and autonomous
unique restart are still unproved. This note establishes no canonical
network convergence theorem. No experiments were performed.

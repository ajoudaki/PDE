# The enlarged marked-response bridge and the temporal cubic law

This note works only with the width-limited inverse-free Gaussian DAG of
the preceding study. The width limit is taken at each fixed step before
any derivative at zero is considered. In particular, no finite-width
learning-rate derivative is used below.

Fix a depth \(L\geq1\) and a finite horizon \(k\geq1\). Give the
successive steps independent sizes

\[
 \varepsilon=(\varepsilon_0,\ldots,\varepsilon_{k-1}).
\]

The diagonal restriction is

\[
 \varepsilon_0=\cdots=\varepsilon_{k-1}=h. \tag{0.1}
\]

The purpose of the independent variables is only to polarize the already
width-limited DAG.

## 1. Statement

For nonconstant \(\phi\), let \(\mathcal T_r\) and \(\mathcal G_r\) be
the scalar and gradient tensors constructed coefficientwise by the
finite marked Gaussian compiler in Section 5. Put

\[
 g=\mathcal G_0,\qquad
 A=\mathcal G_1[g],\qquad
 S_L=\mathcal T_3[g,g,g],\qquad
 H_L=\langle A,A\rangle_{\mathcal P}, \tag{1.1}
\]

and define

\[
 \kappa_{\phi,L}=2H_L+\frac12S_L. \tag{1.2}
\]

Section 5 gives a terminating signed Gaussian-integration algorithm for
these quantities. Thus they are activation- and depth-defined and use no
output derivative, trajectory supremum, or continuity modulus. The
stronger identification of \(H_L,S_L\) with the compact nine-moment
recursion in the preceding CUBIC_COEFFICIENT.md is not used here; it
requires a separate nodewise audit.

**Theorem 1.1 (temporal cubic law).** Under the activation assumptions in
the research contract,

\[
 \frac{F_{2t,L}^{(3)}(0)-8F_{t,L}^{(3)}(0)}6
 =t(2t-1)\kappa_{\phi,L},\qquad t\geq1. \tag{1.3}
\]

If \(\phi\) is constant, both sides are zero.

The substantive point is proving that differentiation of a reused-matrix
response produces all marked source histories with the right
multiplicities. Sections 2--6 supply that bridge.

## 2. Complete marked histories

### 2.1 Multiindex operations

For \(\alpha,\beta\in\mathbb N^k\), write

\[
 |\alpha|=\sum_i\alpha_i,\qquad
 \beta\leq\alpha,\qquad
 {\alpha\choose\beta}=\prod_i{\alpha_i\choose\beta_i}. \tag{2.1}
\]

For every node \(Y(\varepsilon)\), put

\[
 Y^{[\alpha]}=
 \left.D_\varepsilon^\alpha Y(\varepsilon)\right|_{\varepsilon=0},
 \qquad |\alpha|\leq3. \tag{2.2}
\]

Products and step insertions are differentiated by

\[
 (UV)^{[\alpha]}
 =\sum_{\beta\leq\alpha}{\alpha\choose\beta}
 U^{[\beta]}V^{[\alpha-\beta]}, \tag{2.3}
\]

\[
 (\varepsilon_rUV)^{[\alpha]}
 =\mathbf1_{\{\alpha_r>0\}}\alpha_r
 \sum_{\beta\leq\alpha-e_r}
 {\alpha-e_r\choose\beta}
 U^{[\beta]}V^{[\alpha-e_r-\beta]}. \tag{2.4}
\]

For a smooth scalar \(\psi\), \((\psi(Z))^{[\alpha]}\) is the finite
multiset-partition formula

\[
 (\psi(Z))^{[\alpha]}
 =\sum_{\pi\in\Pi(\alpha)}
 \psi^{(|\pi|)}(Z^{[0]})
 \prod_{B\in\pi}Z^{[\nu(B)]}. \tag{2.5}
\]

Here \(\Pi(\alpha)\) partitions the multiset containing \(\alpha_i\)
copies of label \(i\), and \(\nu(B)\) is the multiindex of block \(B\).
For \(\alpha=0\), (2.5) means \(\psi(Z^{[0]})\).

### 2.2 Gram and source marks

Define

\[
 Q_{\ell,rs}^{[\alpha]}
 =\sum_{\beta\leq\alpha}{\alpha\choose\beta}
 \mathbb E[
 H_{\ell,r}^{[\beta]}H_{\ell,s}^{[\alpha-\beta]}],
 \tag{2.6}
\]

\[
 K_{\ell,rs}^{[\alpha]}
 =\sum_{\beta\leq\alpha}{\alpha\choose\beta}
 \mathbb E[
 C_{\ell,r}^{[\beta]}C_{\ell,s}^{[\alpha-\beta]}].
 \tag{2.7}
\]

For each connector \(2\leq\ell\leq L\), append centered Gaussian
coordinates

\[
 \xi_{\ell,s}^{[\alpha]},\qquad
 \chi_{\ell,r}^{[\beta]},\qquad |\alpha|,|\beta|\leq3,
 \tag{2.8}
\]

with

\[
 \mathbb E[
 \xi_{\ell,s}^{[\alpha]}\xi_{\ell,u}^{[\beta]}]
 =\mathbb E[
 H_{\ell-1,s}^{[\alpha]}H_{\ell-1,u}^{[\beta]}],
 \tag{2.9}
\]

\[
 \mathbb E[
 \chi_{\ell,r}^{[\alpha]}\chi_{\ell,v}^{[\beta]}]
 =\mathbb E[
 C_{\ell,r}^{[\alpha]}C_{\ell,v}^{[\beta]}]. \tag{2.10}
\]

Forward and transpose blocks, and different connectors, are independent.
The right sides are finite \(L^2\) Gram matrices, so these Gaussian
arrays exist even when singular.

### 2.3 Marked responses

Let

\[
 \rho_{\ell,sr}^{[\gamma]}=D^\gamma\rho_{\ell,sr}(0),
 \qquad
 \sigma_{\ell,sr}^{[\gamma]}=D^\gamma\sigma_{\ell,sr}(0) \tag{2.11}
\]

be the signed Price derivatives returned chronologically. Define

\[
 \begin{aligned}
 X_{\ell,s}^{[\alpha]}
 ={}&\xi_{\ell,s}^{[\alpha]}\\
 &+\sum_{r<s}\sum_{\beta\leq\alpha}
 {\alpha\choose\beta}
 \rho_{\ell,sr}^{[\alpha-\beta]}C_{\ell,r}^{[\beta]},
 \end{aligned} \tag{2.12}
\]

\[
 \begin{aligned}
 R_{\ell-1,s}^{[\alpha]}
 ={}&\chi_{\ell,s}^{[\alpha]}\\
 &+\sum_{r\leq s}\sum_{\beta\leq\alpha}
 {\alpha\choose\beta}
 \sigma_{\ell,sr}^{[\alpha-\beta]}H_{\ell-1,r}^{[\beta]}.
 \end{aligned} \tag{2.13}
\]

The learned pieces are

\[
 \left(\sum_{r<s}\varepsilon_rQ_{\ell-1,rs}C_{\ell,r}
 \right)^{[\alpha]},\qquad
 \left(\sum_{r<s}\varepsilon_rK_{\ell,rs}H_{\ell-1,r}
 \right)^{[\alpha]}, \tag{2.14}
\]

and are specified by (2.3)--(2.4). The readout and bottom updates are

\[
 a_s=A+\sum_{r<s}\varepsilon_rH_{L,r},\qquad
 Z_{1,s}=U+\sum_{r<s}\varepsilon_rC_{1,r}. \tag{2.15}
\]

Finally use (2.5) in

\[
 H_{\ell,s}=\phi(Z_{\ell,s}),\qquad
 C_{\ell,s}=B_{\ell,s}\phi'(Z_{\ell,s}). \tag{2.16}
\]

An impossible mark is zero: for a time-\(s\) field, \(\alpha_j>0\) with
\(j\geq s\) implies \(Y_s^{[\alpha]}=0\).

The construction is chronological. At time \(s\), construct the bottom
marks. In the upward sweep append every \(\xi_{\ell,s}^{[\alpha]}\)
before \(H_{\ell,s}^{[\alpha]}\). If \(s<k\), construct
\(a_s,C_{L,s}\), then descend, appending every
\(\chi_{\ell,s}^{[\alpha]}\) before \(B_{\ell-1,s}^{[\alpha]}\).
Equations (2.9) and (2.10) use already constructed lower features and
upper cotangents. Hence there is no same-call circularity, and the finite
recursion terminates.

## 3. Marked-response convolution theorem

**Lemma 3.1 (source-response commutation).** Equations (2.12)--(2.13)
are exactly the derivatives of the unmarked inverse-free raw actions
through total order three.

*Proof.* Introduce

\[
 \widehat\chi_r(\varepsilon)
 =\sum_{|\gamma|\leq3}
 \frac{\varepsilon^\gamma}{\gamma!}\chi_r^{[\gamma]},
 \qquad
 \widehat\xi_s(\varepsilon)
 =\sum_{|\gamma|\leq3}
 \frac{\varepsilon^\gamma}{\gamma!}\xi_s^{[\gamma]}. \tag{3.1}
\]

If \(Y(\varepsilon)\) is a smooth cylinder function of
\(\widehat\chi_r(\varepsilon)\), the chain rule gives

\[
 \partial_{\chi_r^{[\beta]}}Y^{[\alpha]}
 =\mathbf1_{\{\beta\leq\alpha\}}
 {\alpha\choose\beta}
 [D^{\alpha-\beta}\partial_{\chi_r}Y]_{\varepsilon=0}.
 \tag{3.2}
\]

Indeed,
\(\partial_{\chi_r^{[\beta]}}\widehat\chi_r(\varepsilon)
=\varepsilon^\beta/\beta!\); coefficient extraction proves (3.2).
Taking expectations yields

\[
 \mathbb E\partial_{\chi_r^{[\beta]}}H_s^{[\alpha]}
 =\mathbf1_{\{\beta\leq\alpha\}}
 {\alpha\choose\beta}\rho_{sr}^{[\alpha-\beta]}, \tag{3.3}
\]

and identically

\[
 \mathbb E\partial_{\xi_r^{[\beta]}}C_s^{[\alpha]}
 =\mathbf1_{\{\beta\leq\alpha\}}
 {\alpha\choose\beta}\sigma_{sr}^{[\alpha-\beta]}. \tag{3.4}
\]

The fixed-Gaussian marked lift also computes the signed derivatives when
the original covariance changes. From (2.9),

\[
 \begin{aligned}
 &D^\gamma\mathbb E[
 \widehat\xi_s(\varepsilon)\widehat\xi_u(\varepsilon)]|_0\\
 &\quad=
 \sum_{\alpha+\beta=\gamma}{\gamma\choose\alpha}
 \mathbb E[
 H_s^{[\alpha]}H_u^{[\beta]}]
 =Q_{su}^{[\gamma]}.
 \end{aligned} \tag{3.5}
\]

The same holds for \(\chi,K\). At a nonsingular covariance, repeated
Price differentiation says the derivative of a Gaussian expectation is
uniquely determined by the covariance and integrand jets. Thus (3.5) and
induction over chronological calls identify all field, Gram, and response
jets.

At a singular covariance apply the singular Price lemma separately to
the original Gaussian curve and to the marked polynomial curve (3.1).
In the proof of that lemma, the covariance of the current unmarked call
is replaced by \(\Sigma(\varepsilon)+\delta I\), the nonsingular identity
is integrated, and \(\delta\downarrow0\). The limiting derivative formula
depends only on the covariance jets and the integrand jets, which agree
by (3.2)--(3.5). The weighted \(C^{12}\) envelope dominates all
integrands and spatial derivatives used here. Notice that this argument
does not add independent \(\delta\)-noise to every derivative coordinate
in (2.8); doing that would alter the covariance jets of (3.1).

Substituting (3.3)--(3.4) gives (2.12)--(2.13). For one variable, the
second response derivative is

\[
 \rho''C+2\rho'C'+\rho C'', \tag{3.6}
\]

and the third is

\[
 \rho'''C+3\rho''C'+3\rho'C''+\rho C'''. \tag{3.7}
\]

Thus the previously omitted \(2\rho'C'\), and all analogues, are
present. \(\square\)

## 4. Causal adjoint and singular quotient

Fix one connector. Index a marked lower query by \(p=(s,\alpha)\) and a
marked upper cotangent by \(q=(r,\beta)\). Write \(q\prec p\) when
\(r<s\), and \(p\preceq q\) when \(s\leq r\). These relations partition
each forward/transpose pair according to which action occurs first.

Put

\[
 Q_{pp'}=\mathbb E[x_px_{p'}],\qquad
 K_{qq'}=\mathbb E[c_qc_{q'}], \tag{4.1}
\]

\[
 R_{pq}=\mathbb E\partial_{\chi_q}x_p,\qquad
 S_{qp}=\mathbb E\partial_{\xi_p}c_q. \tag{4.2}
\]

Causality gives \(R_{pq}=0\) unless \(q\prec p\), and \(S_{qp}=0\)
unless \(p\preceq q\). The complete marked raw actions are

\[
 \mathcal W x_p
 =\xi_p+\sum_{q'\prec p}R_{pq'}c_{q'}, \tag{4.3}
\]

\[
 \mathcal W^*c_q
 =\chi_q+\sum_{p'\preceq q}S_{qp'}x_{p'}. \tag{4.4}
\]

**Lemma 4.1 (causal marked adjoint).** For every marked pair,

\[
 \mathbb E[c_q\mathcal W x_p]
 =\mathbb E[x_p\mathcal W^*c_q]. \tag{4.5}
\]

*Proof.* Degenerate Gaussian integration by parts gives

\[
 \mathbb E[c_q\xi_p]
 =\sum_{p'\preceq q}Q_{pp'}S_{qp'}, \tag{4.6}
\]

because \(c_q\) uses no future forward source, and

\[
 \mathbb E[x_p\chi_q]
 =\sum_{q'\prec p}K_{qq'}R_{pq'}, \tag{4.7}
\]

because \(x_p\) uses no current or future transpose source. Hence

\[
 \begin{aligned}
 \mathbb E[c_q\mathcal W x_p]
 ={}&\sum_{p'\preceq q}Q_{pp'}S_{qp'}
 +\sum_{q'\prec p}R_{pq'}K_{qq'},\\
 \mathbb E[x_p\mathcal W^*c_q]
 ={}&\sum_{q'\prec p}K_{qq'}R_{pq'}
 +\sum_{p'\preceq q}S_{qp'}Q_{pp'}.
 \end{aligned} \tag{4.8}
\]

They coincide. The proof uses the complementary chronological sums; it
does not insert future queries into an earlier transpose action.
\(\square\)

We next prove that this is intrinsic at a singular Gram. Let
\(T_C:\mathbb R^m\to L^2\) be

\[
 T_C\lambda=\sum_q\lambda_qc_q. \tag{4.9}
\]

Then \(K=T_C^*T_C\), and

\[
 \lambda\in\ker K
 \quad\Longrightarrow\quad
 T_C\lambda=0\quad\text{in }L^2. \tag{4.10}
\]

If two smooth ambient extensions agree on the support of the degenerate
Gaussian, their derivative difference normal to that support belongs to
\(\ker K\). Equation (4.10) shows that its contribution to

\[
 \sum_q\mathbb E[\partial_{\chi_q}x]c_q \tag{4.11}
\]

vanishes in \(L^2\). Thus (4.11) is a vector in the Hilbert quotient
\(\mathbb R^m/\ker K\), independent of coordinates and of the off-support
extension. The same argument applies to \(Q\). Degenerate integration by
parts itself follows by writing the source as \(\Sigma^{1/2}G\) and
integrating by parts in the nonsingular standard Gaussian \(G\), so no
coordinatewise regularization ambiguity is present.

Duplicated zero-step histories may therefore be deleted. For example, if
\(\chi_0=\chi_1=\chi\) and \(c_0=c_1=c\), then

\[
 (\mathbb E\partial_0f+\mathbb E\partial_1f)c
 =\mathbb E\left[\frac d{dz}f(z,z)\right]c. \tag{4.12}
\]

Changing \(f\) off the diagonal changes its two partial derivatives by a
normal vector whose sum is zero. Equation (4.12) is the response after
retaining one copy. This proves duplicate-history invariance, not merely
equality of covariance matrices.

## 5. Truncated formal potential and gradient tensors

There is no assertion in this section that a finite span of marked fields
is closed under the nonlinear network on a neighborhood. We work only in
a truncated coefficient algebra.

Fix finitely many formal directions \(u_1,\ldots,u_m\), of the same
top-weight, connector-tensor, and first-layer types as the actual
parameter update. Put

\[
 \mathfrak A_m
 =\mathbb R[z_1,\ldots,z_m]/(z_1,\ldots,z_m)^4. \tag{5.1}
\]

A formal random field is

\[
 \mathbf Y(z)
 =\sum_{|\alpha|\leq3}\frac{z^\alpha}{\alpha!}
 Y^{[\alpha]}. \tag{5.2}
\]

Products, activations, expectations, Grams, and responses in
\(\mathfrak A_m\) are defined coefficientwise by (2.3)--(2.16). At each
forward or transpose call, all source coefficients are adjoined with
the joint Gram (2.9) or (2.10). Lemma 3.1 proves that this is exactly the
signed Price coefficient rule, including every response convolution.
The construction is finite and chronological; it does not evaluate a
nonlinear field at a nonzero point of a finite-dimensional function
space.

The admissible directions are generated recursively. First run the
zero-perturbation forward/reverse pass to construct \(g\). Once the
source histories of \(u_1,\ldots,u_m\) exist, the formal pass below
appends the marked sources needed for
\(\mathcal G_r[u_1,\ldots,u_r]\). Thus the directions in (5.21) are
constructed in the order \(g\), then \(A\), then \(B\) and \(C\).
Every new call uses only direction histories already constructed before
that call, and this recursion terminates at order three.

Let \(\mathscr P\) be the algebraic parameter module generated by the
finitely many coefficient fields that occur. Its three block types are

\[
 L^2(\Omega_L),\qquad
 L^2(\Omega_\ell)\otimes L^2(\Omega_{\ell-1})
 \ (2\leq\ell\leq L),\qquad
 L^2(\Omega_1), \tag{5.3}
\]

restricted to the finite algebraic spans generated by the compiler and
quotiented by their \(L^2\) null spaces. On connector tensors set

\[
 \langle c\otimes x,\widetilde c\otimes\widetilde x\rangle
 =\mathbb E[c\widetilde c]\,\mathbb E[x\widetilde x], \tag{5.4}
\]

and use the direct-sum inner product over parameter blocks. Every space
used below is finite after the directions and order three have been
fixed.

Given the formal perturbation

\[
 \mathbf\theta(z)=\sum_{i=1}^m z_i u_i, \tag{5.5}
\]

write its blocks as
\((\boldsymbol\alpha,\mathbf K_2,\ldots,\mathbf K_L,\mathbf u)\).
The formal forward pass is, coefficientwise,

\[
 \mathbf Z_1=U+\mathbf u,\qquad
 \mathbf H_1=\phi(\mathbf Z_1), \tag{5.5a}
\]

\[
 \mathbf Z_\ell
 =\mathcal W_\ell\mathbf H_{\ell-1}
 +\mathbf K_\ell\mathbf H_{\ell-1},\qquad
 \mathbf H_\ell=\phi(\mathbf Z_\ell). \tag{5.5b}
\]

Here the coefficient of
\(\mathcal W_\ell\mathbf H_{\ell-1}\) of multiorder \(\alpha\) is
defined by adjoining the source \(\xi_\ell^{[\alpha]}\) with (2.9) and
using the complete response sum (2.12) over every marked transpose source
on which that coefficient depends. The formal reverse pass starts from

\[
 \mathbf C_L
 =(A+\boldsymbol\alpha)\phi'(\mathbf Z_L), \tag{5.5c}
\]

and uses, coefficientwise,

\[
 \mathbf B_{\ell-1}
 =\mathcal W_\ell^*\mathbf C_\ell
 +\mathbf K_\ell^*\mathbf C_\ell,\qquad
 \mathbf C_{\ell-1}
 =\mathbf B_{\ell-1}\phi'(\mathbf Z_{\ell-1}), \tag{5.5d}
\]

where (2.10) and (2.13) define every transpose source and response.
All source histories occurring inside the finitely many directions
\(u_i\) are included before this pass. This is a finite dependency DAG:
forward coefficients are constructed upward and reverse coefficients
downward, exactly as in Section 2.

Denote the resulting scalar output by
\(\mathbf\Phi(z)\in\mathfrak A_m\) and its back-propagated parameter
field by

\[
 \mathbf G(z)
 =(\mathbf H_L,\mathbf C_L\otimes\mathbf H_{L-1},
 \ldots,\mathbf C_2\otimes\mathbf H_1,\mathbf C_1).
 \tag{5.6}
\]

Explicitly,

\[
 \mathbf\Phi(z)
 =\mathbb E[(A+\boldsymbol\alpha)\mathbf H_L]. \tag{5.6a}
\]

Define symmetric coefficient candidates by polarization:

\[
 \mathcal T_r[u_1,\ldots,u_r]
 =[z_1\cdots z_r]\,\mathbf\Phi
       \left(\sum_{i=1}^r z_i u_i\right),
 \qquad 0\leq r\leq3, \tag{5.7}
\]

\[
 \mathcal G_r[u_1,\ldots,u_r]
 =[z_1\cdots z_r]\,\mathbf G
       \left(\sum_{i=1}^r z_i u_i\right),
 \qquad 0\leq r\leq2. \tag{5.8}
\]

Here the brackets extract the indicated square-free coefficient. Repeated
directions are defined by polarization, equivalently by using one
variable and the derivative normalization (5.2). The coefficient
construction terminates after finitely many Gaussian integrations of
products of \(\phi\) and its derivatives. Thus (5.7)--(5.8) are explicit
activation-defined tensors, not derivatives of an unknown output.

### 5.1 Formal adjoint identity

Introduce a new square-zero variable \(\tau\), commute it with
\(\mathfrak A_m\), and discard terms of total \(z\)-degree above two in
the coefficient of \(\tau\). For an additional fixed formal parameter
direction

\[
 v=(v_A,V_2,\ldots,V_L,v_1), \tag{5.9}
\]

run the same marked compiler on
\(\mathbf\theta(z)+\tau v\). Write \(\delta_v\) for the coefficient of
\(\tau\).

**Lemma 5.1 (coefficientwise potential-gradient adjoint).** In the
truncated algebra,

\[
 \delta_v\mathbf\Phi(z)
 =\langle\mathbf G(z),v\rangle_{\mathscr P}
 \pmod{(z_1,\ldots,z_m)^3}. \tag{5.10}
\]

Consequently, for \(0\leq r\leq2\),

\[
 \mathcal T_{r+1}[v,u_1,\ldots,u_r]
 =\left\langle
 \mathcal G_r[u_1,\ldots,u_r],v
 \right\rangle_{\mathscr P}. \tag{5.11}
\]

*Proof.* Coefficientwise differentiation of one formal connector gives

\[
 \delta_v\mathbf Z_\ell
 =\mathcal W_\ell(\delta_v\mathbf H_{\ell-1})
 +V_\ell\mathbf H_{\ell-1}
 +\mathbf K_\ell(\delta_v\mathbf H_{\ell-1}). \tag{5.12}
\]

Every coefficient of the first term is a marked forward action (2.12).
Every coefficient of the reverse raw action is (2.13). Lemma 4.1 applies
to each pair of their marked coefficients, and finite summation gives

\[
 \begin{aligned}
 \mathbb E[
 \mathbf C_\ell\,\delta_v\mathbf Z_\ell]
 ={}&
 \mathbb E[
 \mathbf B_{\ell-1}\,\delta_v\mathbf H_{\ell-1}]\\
 &+\langle
 \mathbf C_\ell\otimes\mathbf H_{\ell-1},V_\ell
 \rangle_{\mathscr P}
 \pmod{(z)^3}. 
 \end{aligned} \tag{5.13}
\]

The tensor action and adjoint in the learned term are the algebraic
identities

\[
 (c\otimes x)y=c\,\mathbb E[xy],\qquad
 (c\otimes x)^*\widetilde c
 =x\,\mathbb E[c\widetilde c]. \tag{5.14}
\]

Using
\(\delta_v\mathbf H_{\ell-1}
=\phi'(\mathbf Z_{\ell-1})\delta_v\mathbf Z_{\ell-1}\)
coefficientwise, telescope (5.13) from the top to the bottom. The boundary
terms are

\[
 \begin{aligned}
 \delta_v\mathbf\Phi
 ={}&\mathbb E[\mathbf H_Lv_A]
 +\sum_{\ell=2}^L
 \langle\mathbf C_\ell\otimes\mathbf H_{\ell-1},V_\ell
 \rangle_{\mathscr P}
 +\mathbb E[\mathbf C_1v_1],
 \end{aligned} \tag{5.15}
\]

which is (5.10). The binomial identities in Lemma 3.1 are precisely what
make (5.13) valid in degrees one and two; in particular, its degree-two
coefficient contains the formerly missing
\(2\rho'C'\)-type terms.

Extracting \(z_1\cdots z_r\) proves (5.11). The scalar tensors
\(\mathcal T_r\) are symmetric because the variables in
\(\mathfrak A_m\) commute and the covariance coefficient (3.5) is
symmetric under permutation of direction labels. Equivalently, the
singular Price formula gives the same finite signed expression under
each order of the mixed labels. Equation (5.11) then also proves the
required adjoint symmetry of the generated gradient coefficients.
\(\square\)

### 5.2 Substitution naturality

Let

\[
 \mathfrak A=\mathbb R[z_1,\ldots,z_m]/(z)^4,\qquad
 \mathfrak B=\mathbb R[e_1,\ldots,e_N]/(e)^4,
 \tag{5.15a}
\]

and let \(S:\mathfrak A\to\mathfrak B\) be an augmented algebra
homomorphism: \(S(1)=1\) and \(S((z))\subset(e)\). It may send each
\(z_i\) to an arbitrary polynomial of degrees one through three. Apply
\(S\) coefficientwise to deterministic scalars and random cylinder
fields.

**Lemma 5.2 (naturality of the marked compiler).** Suppose a finite
chronological marked compiler over \(\mathfrak A\) and a compiler over
\(\mathfrak B\) have input leaves related by \(S\). Then, action by
action through order three:

1. sums, products, activation compositions, expectations, tensor
   contractions, and Gram formation in the second compiler are the
   \(S\)-images of those in the first;
2. adjoining a joint forward or transpose Gaussian source block commutes
   with \(S\), up to the canonical isometry of its Gaussian Hilbert
   quotient;
3. every signed-Price \(\rho\)- and \(\sigma\)-response extraction
   commutes with \(S\) in the common labeled ambient coordinates, and
   its aggregate response vector commutes with \(S\) after passage to a
   singular quotient.

*Proof.* We induct over the finite chronological call list.

For algebraic nodes the claim is literal:

\[
 S(X+Y)=SX+SY,\qquad S(XY)=(SX)(SY). \tag{5.15b}
\]

If \(X=X_0+\widetilde X\), \(\widetilde X^4=0\), formal activation is

\[
 \phi(X)=\sum_{j=0}^3\frac{\phi^{(j)}(X_0)}{j!}
 \widetilde X^j. \tag{5.15c}
\]

Because an augmented \(S\) fixes \(X_0\), applying \(S\) to (5.15c)
gives the target formal activation. Expectations are coefficientwise,
so \(S\mathbb E X=\mathbb E SX\). Hence

\[
 S\mathbb E[XY]=\mathbb E[(SX)(SY)], \tag{5.15d}
\]

which proves naturality of every feature Gram, cotangent Gram, and
finite tensor contraction.

Consider a new forward source block. Let \(\{X_\lambda\}\) be the finite
family of coefficient fields of all its new and old queries, indexed by
coefficient linear functionals \(\lambda\) on \(\mathfrak A\). Its
Gaussian Hilbert space is the quotient of the formal span of symbols
\(I(X_\lambda)\) by the null space of

\[
 \langle I(X_\lambda),I(X_\mu)\rangle
 =\mathbb E[X_\lambda X_\mu]. \tag{5.15e}
\]

After substitution, every coefficient of \(SX\) is a finite linear
combination of the \(X_\lambda\). The direct target source adjoining
assigns to those combinations the Gram

\[
 \mathbb E[(SX)_\nu(SX)_{\nu'}], \tag{5.15f}
\]

which, by bilinearity and (5.15d), is exactly the Gram of the same
linear combinations of the source symbols in (5.15e). Therefore the
map induced by \(S\) is Gram preserving. It sends null vectors to null
vectors and defines a canonical isometry onto the target Gaussian
Hilbert quotient. The transpose source proof is identical, with
cotangent query fields in place of feature fields. Direct sums preserve
the stipulated independence of different connectors and directions.

For a response node, first use nonsingular labeled ambient source
coordinates. The exact signed response compiler is made from:

- formal products and sums;
- covariance and integrand coefficients;
- spatial differentiation of the same labeled cylinder polynomial;
- Gaussian expectations; and
- the Price operation
  \(\frac12\Sigma':D^2\).

Each operation commutes with \(S\) by (5.15b)--(5.15f) and the ordinary
formal chain rule. When a differentiated source coordinate is itself
substituted, equation (3.2) supplies exactly the binomial convolution
required by that chain rule. Thus every labeled ambient
\(\rho,\sigma\) coefficient is the \(S\)-image of its source coefficient.

If the Gram is singular, carry out the preceding identity in the
singular Price formula established in Section 3. The source maps on the
two sides have identical kernels by (5.15e)--(5.15f). A change of
ambient response representative lies in that kernel; equation (4.10)
maps it to the zero feature or cotangent field. Hence the aggregate
response vectors commute with \(S\) in the quotient. This also proves
that the quotient isometries constructed at consecutive calls extend
one another. The chronological induction is complete. \(\square\)

### 5.3 Formal temporal recurrence

Put

\[
 g=\mathcal G_0,\qquad
 \mathfrak G(\vartheta)
 =g+\mathcal G_1[\vartheta]
 +\frac12\mathcal G_2[\vartheta,\vartheta] \tag{5.16}
\]

for a formal parameter displacement \(\vartheta\) with zero constant
term, retaining total degree at most two on the right. In the schedule
algebra

\[
 \mathfrak A_k
 =\mathbb R[\varepsilon_0,\ldots,\varepsilon_{k-1}]
 /(\varepsilon_0,\ldots,\varepsilon_{k-1})^4,
\]

define

\[
 \vartheta_0=0,\qquad
 \vartheta_{s+1}
 =\vartheta_s+\varepsilon_s\mathfrak G(\vartheta_s),
 \qquad0\leq s<k. \tag{5.17}
\]

Also define the formal output germ

\[
 \mathfrak F(\vartheta)
 =\mathcal T_0+\mathcal T_1[\vartheta]
 +\frac12\mathcal T_2[\vartheta,\vartheta]
 +\frac16\mathcal T_3[\vartheta,\vartheta,\vartheta].
 \tag{5.18}
\]

**Lemma 5.3 (temporal-jet intertwining).** The signed order-three jet of
the actual width-first horizon-\(s\) temporal DAG is
\(\mathfrak F(\vartheta_s)\).

*Proof.* We compare two coefficientwise constructions.

- The **temporal construction** is the marked schedule DAG of Section 2.
  Its fields and sources carry a superscript \(T\).
- The **substituted construction at time \(s\)** is the formal one-pass
  compiler (5.5a)--(5.6a), with parameter argument
  \(\vartheta_s\). Its current-pass fields and sources carry a superscript
  \(S\). Every source history already occurring in a coefficient of
  \(\vartheta_s\) is retained as an old source of this compiler.

More explicitly, choose a finite parameter basis
\(v_1,\ldots,v_M\) containing every coefficient of \(\vartheta_s\) and
write

\[
 \vartheta_s(\varepsilon)
 =\sum_{j=1}^M p_{s,j}(\varepsilon)v_j.
\]

If \(z_j\) are the parameter variables in the universal formal compiler,
the substituted construction is its image under

\[
 S_s:z_j\longmapsto p_{s,j}(\varepsilon). \tag{5.20a}
\]

Lemma 5.2 proves before the comparison begins that this substitution
commutes with every node and source/response adjoining operation,
including the singular quotient. The induction below identifies this
well-defined \(S_s\)-image with the temporal chronology label by label.

For \(s<k\), order the local operations as

\[
 \mathcal B_s=
 (b_s;\uparrow s,2,\ldots,\uparrow s,L;
 t_s;\downarrow s,L,\ldots,\downarrow s,2;u_s).
 \tag{5.21a}
\]

Here \(b_s\) is the bottom deterministic construction, \(t_s\) constructs
the top cotangent, and \(u_s\) updates the parameter state. Let \(i\) be
the position in this displayed finite list. At terminal time \(k\), use
only \(b_k\), the forward operations, and the terminal readout.

We induct lexicographically on

\[
 (s,i,|\alpha|,\alpha),\qquad |\alpha|\leq3, \tag{5.21b}
\]

where the last order is any fixed order on the finite multiindex set.
At a given action, all marks of its new Gaussian source block are adjoined
simultaneously; the order on \(\alpha\) is used only to enumerate the
coefficient identities.

The induction invariant after \((s,i)\) is the following.

1. There is a Gram-preserving map \(J_{s,i}\) from the Gaussian Hilbert
   quotient of every source coordinate so far used by the substituted
   construction to the quotient of the corresponding temporal source
   coordinates. It is the identity on all histories preceding time \(s\).
2. After applying \(J_{s,i}\), every constructed mark
   \(Z,H,a,B,C\) in the substituted construction equals its temporal
   mark, for every \(|\alpha|\leq3\).
3. Every constructed Gram mark agrees. In particular, whenever the
   current field exists,

   \[
   \begin{aligned}
    (Q_{\ell,rs}^{S})^{[\alpha]}
    &=(Q_{\ell,rs}^{T})^{[\alpha]},\\
    (K_{\ell,rs}^{S})^{[\alpha]}
    &=(K_{\ell,rs}^{T})^{[\alpha]},
   \end{aligned}
   \qquad r\leq s. \tag{5.21c}
   \]

   This includes every current-to-old cross-time entry, not only the
   current variance.
4. In the common labeled ambient compiler, every available response mark
   agrees:

   \[
    (\rho_{\ell,sr}^{S})^{[\alpha]}
    =(\rho_{\ell,sr}^{T})^{[\alpha]},\qquad r<s,
    \tag{5.21d}
   \]

   \[
    (\sigma_{\ell,sr}^{S})^{[\alpha]}
    =(\sigma_{\ell,sr}^{T})^{[\alpha]},\qquad r\leq s.
    \tag{5.21e}
   \]

   After passage to a singular quotient, the corresponding aggregate
   response vectors in (2.12)--(2.13) agree.
5. The full covariance matrix of the new and old marked sources agrees
   under \(J_{s,i}\), including all pairs

   \[
   \mathbb E[
    (\xi_{\ell,s}^{S})^{[\alpha]}
    (\xi_{\ell,r}^{S})^{[\beta]}]
   =
   \mathbb E[
    (\xi_{\ell,s}^{T})^{[\alpha]}
    (\xi_{\ell,r}^{T})^{[\beta]}], \tag{5.21f}
   \]

   \[
   \mathbb E[
    (\chi_{\ell,s}^{S})^{[\alpha]}
    (\chi_{\ell,r}^{S})^{[\beta]}]
   =
   \mathbb E[
    (\chi_{\ell,s}^{T})^{[\alpha]}
    (\chi_{\ell,r}^{T})^{[\beta]}], \tag{5.21g}
   \]

   for all valid older \(r\) and all
   \(|\alpha|,|\beta|\leq3\). Cross-direction and cross-connector source
   covariances are zero in both constructions.
6. Before \(b_s\), the parameter marks agree and have the accumulated
   form

   \[
   \begin{aligned}
    \alpha_s&=\sum_{r<s}\varepsilon_rH_{L,r}^{T},\\
    u_s&=\sum_{r<s}\varepsilon_rC_{1,r}^{T},\\
    K_{\ell,s}
    &=\sum_{r<s}\varepsilon_r
      C_{\ell,r}^{T}\otimes H_{\ell-1,r}^{T}.
   \end{aligned} \tag{5.21h}
   \]

We now prove all parts of the invariant.

**Initial action.** At \(s=0\), \(\vartheta_0=0\). The two constructions
use the same \(U,A\), no older temporal history, and the same
zero-parameter formulas. At \(b_0\),

\[
 (Z_{1,0}^{S})^{[0]}=(Z_{1,0}^{T})^{[0]}=U,
\]

while every positive mark is zero. Formula (2.5) gives equality of all
\(H_{1,0}\) marks. Thus the invariant starts with the identity quotient
map.

Assume next that all operations before time \(s\) have been matched. The
end-of-time update proved below gives (5.21h), so the induction begins at
\(b_s\). Coefficientwise,

\[
 Z_{1,s}^{S}=U+u_s
 =U+\sum_{r<s}\varepsilon_rC_{1,r}^{T}
 =Z_{1,s}^{T}. \tag{5.21i}
\]

Composition by the same formal \(\phi\), using (2.5), gives equality of
every \(H_{1,s}\) mark. Formula (2.6) then gives all new
\(Q_{1,rs}^{[\alpha]}\), including \(r<s\), and proves (5.21c) at the
bottom.

**One forward action.** Suppose the invariant holds immediately before
\((\uparrow,s,\ell)\). The lower current query marks agree. The
substituted compiler appends the entire block
\((\xi_{\ell,s}^{S})^{[\alpha]}\). Its covariance with an arbitrary old
forward source mark is, by its defining Gram,

\[
 \begin{aligned}
 &\mathbb E[
  (\xi_{\ell,s}^{S})^{[\alpha]}
  (\xi_{\ell,r}^{S})^{[\beta]}]\\
 &\quad=\mathbb E[
  (H_{\ell-1,s}^{S})^{[\alpha]}
  (H_{\ell-1,r}^{S})^{[\beta]}]\\
 &\quad=\mathbb E[
  (H_{\ell-1,s}^{T})^{[\alpha]}
  (H_{\ell-1,r}^{T})^{[\beta]}]\\
 &\quad=\mathbb E[
  (\xi_{\ell,s}^{T})^{[\alpha]}
  (\xi_{\ell,r}^{T})^{[\beta]}].
 \end{aligned} \tag{5.21j}
\]

The same calculation with two current marks gives their complete
within-block Gram. All covariances with the independent transpose block
and other connectors vanish in both constructions. Therefore the labeled
map sending every new static source mark to the temporal mark with the
same \((\ell,s,\alpha)\) preserves the full Gram and extends
\(J_{s,i-1}\) to \(J_{s,i}\).

The lower query is the same labeled cylinder polynomial after this map.
Consequently its ambient partial derivative with respect to each old
\(\chi_{\ell,r}^{[\beta]}\) is the same polynomial. Taking expectation
under the just-matched joint Gaussian law and using (3.3) proves
(5.21d) for every \(r<s,\alpha\). Thus the full raw action agrees,
coefficient by coefficient:

\[
 \begin{aligned}
 (X_{\ell,s}^{S})^{[\alpha]}
 ={}&(\xi_{\ell,s}^{S})^{[\alpha]}\\
 &+\sum_{r<s}\sum_{\beta\leq\alpha}
 {\alpha\choose\beta}
 (\rho_{\ell,sr}^{S})^{[\alpha-\beta]}
 (C_{\ell,r}^{S})^{[\beta]}\\
 ={}&J_{s,i}^{-1}(X_{\ell,s}^{T})^{[\alpha]} .
 \end{aligned} \tag{5.21k}
\]

The learned connector in the substituted state is the last line of
(5.21h). Acting on the current lower query gives

\[
 K_{\ell,s}H_{\ell-1,s}^{S}
 =\sum_{r<s}\varepsilon_rC_{\ell,r}^{T}
 \,\mathbb E[
 H_{\ell-1,r}^{T}H_{\ell-1,s}^{S}]. \tag{5.21l}
\]

The coefficient of every multiindex \(\alpha\) in (5.21l), expanded by
(2.3)--(2.4), is exactly the learned
\(\sum_{r<s}\varepsilon_rQ_{\ell-1,rs}^{T}C_{\ell,r}^{T}\)
coefficient in the temporal preactivation. Hence
\(Z_{\ell,s}^{S}=Z_{\ell,s}^{T}\) coefficientwise. Equation (2.5) gives
\(H_{\ell,s}^{S}=H_{\ell,s}^{T}\), and (2.6) gives every new cross-time
\(Q_{\ell,rs}^{[\alpha]}\). This proves all six invariant clauses after
one forward action. Induction over \(\ell=2,\ldots,L\) completes the
forward sweep.

**Top deterministic action.** By (5.21h),

\[
 a_s^{S}=A+\alpha_s
 =A+\sum_{r<s}\varepsilon_rH_{L,r}^{T}=a_s^{T}. \tag{5.21m}
\]

The current \(Z_{L,s}\) marks already agree, so the product/composition
rules give every \(C_{L,s}\) mark. Equation (2.7) gives all
\(K_{L,rs}^{[\alpha]}\), \(r\leq s\), including the full current-to-old
row.

**One transpose action.** Suppose the invariant holds immediately before
\((\downarrow,s,\ell)\). The current upper cotangent marks agree. The
substituted compiler appends
\((\chi_{\ell,s}^{S})^{[\alpha]}\). For every old reverse source mark,

\[
 \begin{aligned}
 &\mathbb E[
  (\chi_{\ell,s}^{S})^{[\alpha]}
  (\chi_{\ell,r}^{S})^{[\beta]}]\\
 &\quad=\mathbb E[
  (C_{\ell,s}^{S})^{[\alpha]}
  (C_{\ell,r}^{S})^{[\beta]}]\\
 &\quad=\mathbb E[
  (C_{\ell,s}^{T})^{[\alpha]}
  (C_{\ell,r}^{T})^{[\beta]}]\\
 &\quad=\mathbb E[
  (\chi_{\ell,s}^{T})^{[\alpha]}
  (\chi_{\ell,r}^{T})^{[\beta]}].
 \end{aligned} \tag{5.21n}
\]

The within-current block and every independent cross block match for the
same reason, so \(J_{s,i-1}\) extends by
\((\chi_{\ell,s}^{S})^{[\alpha]}
 \mapsto(\chi_{\ell,s}^{T})^{[\alpha]}\).

The current cotangent is now the same labeled cylinder polynomial.
Its ambient derivatives with respect to every current or old
\(\xi_{\ell,r}^{[\beta]}\) agree. Taking Gaussian expectations and using
(3.4) proves (5.21e) for all \(r\leq s,\alpha\). Hence

\[
 \begin{aligned}
 (R_{\ell-1,s}^{S})^{[\alpha]}
 ={}&(\chi_{\ell,s}^{S})^{[\alpha]}\\
 &+\sum_{r\leq s}\sum_{\beta\leq\alpha}
 {\alpha\choose\beta}
 (\sigma_{\ell,sr}^{S})^{[\alpha-\beta]}
 (H_{\ell-1,r}^{S})^{[\beta]}\\
 ={}&J_{s,i}^{-1}(R_{\ell-1,s}^{T})^{[\alpha]} .
 \end{aligned} \tag{5.21o}
\]

The learned transpose contraction is

\[
 K_{\ell,s}^*C_{\ell,s}^{S}
 =\sum_{r<s}\varepsilon_rH_{\ell-1,r}^{T}
 \,\mathbb E[C_{\ell,r}^{T}C_{\ell,s}^{S}]. \tag{5.21p}
\]

By (2.3)--(2.4) and (2.7), each coefficient is exactly the temporal
learned term
\(\sum_{r<s}\varepsilon_rK_{\ell,rs}^{T}H_{\ell-1,r}^{T}\).
Thus all \(B_{\ell-1,s}\) marks agree. Multiplication by the already
matched \(\phi'(Z_{\ell-1,s})\) gives all \(C_{\ell-1,s}\) marks, and
(2.7) gives every new cross-time cotangent Gram. Descending from
\(\ell=L\) to \(2\) proves the invariant through the reverse sweep.

**Singular quotient compatibility.** The preceding labelwise comparison
was made in the common ambient compiler. If a source Gram is singular,
(5.21j) or (5.21n) says that the labeled static and temporal Gram
matrices are identical. Therefore the map \(J_{s,i}\) sends their kernels
onto one another and descends to an isometry of Gaussian Hilbert
quotients. If individual ambient response coefficients change after a
basis reduction, their difference is a null coefficient vector.
Equation (4.10) sends that vector to the zero feature or cotangent field.
Thus the aggregate sums (5.21k) and (5.21o), and hence every later field,
are compatible with the quotient map. This proves the quotient clause at
every action, rather than only at the end of a time slice.

**State update.** At the end of the reverse sweep, all gradient blocks
agree:

\[
 G_s^{S}
 =(H_{L,s}^{T},
 C_{L,s}^{T}\otimes H_{L-1,s}^{T},\ldots,
 C_{2,s}^{T}\otimes H_{1,s}^{T},C_{1,s}^{T})
 =G_s^{T}. \tag{5.21q}
\]

The exact temporal update gives

\[
 \vartheta_{s+1}
 =\vartheta_s+\varepsilon_sG_s^{T}
 =\vartheta_s+\varepsilon_s
 \mathfrak G(\vartheta_s)\pmod{\mathfrak m^4}. \tag{5.21r}
\]

The first equality is (5.19)--(5.20), and the second is the
coefficientwise equality just proved. It establishes (5.21h) for time
\(s+1\) and closes the lexicographic induction.

At terminal time \(k\), repeat the bottom and forward parts of the same
induction. Equations (5.21i)--(5.21l) give all terminal feature,
cross-time Gram, source-covariance, and response marks. Equation (5.21m)
gives the terminal readout weight. Therefore the terminal scalar marked
jet equals \(\mathfrak F(\vartheta_k)\).

Finally, the diagonal map
\(\varepsilon_0,\ldots,\varepsilon_{k-1}\mapsto h\) is an algebra
homomorphism from \(\mathfrak A_k\) to
\(\mathbb R[h]/(h^4)\). It commutes with every finite sum, product,
expectation, Gram, marked response convolution, and quotient isometry
above. Hence the common-step signed order-three jet is the diagonal of
the proved schedule identity. \(\square\)

### 5.4 The exact tensor identities needed later

Define

\[
 A=\mathcal G_1[g],\qquad
 B=\mathcal G_2[g,g],\qquad
 C=\mathcal G_1[A], \tag{5.21}
\]

\[
 H=\langle A,A\rangle_{\mathscr P},\qquad
 S=\mathcal T_3[g,g,g]. \tag{5.22}
\]

Lemma 5.1 and symmetry of \(\mathcal T_2,\mathcal T_3\) give, without a
neighborhood gradient map,

\[
 \mathcal T_1[B]
 =\langle\mathcal G_2[g,g],g\rangle
 =\mathcal T_3[g,g,g]=S, \tag{5.23}
\]

\[
 \begin{aligned}
 \mathcal T_1[C]
 &=\langle\mathcal G_1[A],g\rangle
 =\mathcal T_2[g,A]\\
 &=\langle\mathcal G_1[g],A\rangle
 =\langle A,A\rangle=H.
 \end{aligned} \tag{5.24}
\]

Likewise

\[
 \mathcal T_2[g,A]=H. \tag{5.25}
\]

Equations (5.23)--(5.25) are the only potential-gradient identities used
in the Euler calculation.

## 6. Universal gradient-Euler calculation

Use the formal quantities \(g,A,B,C,H,S\) in
(5.21)--(5.22). On the diagonal (0.1), extract the first three
coefficients of the formal recurrence (5.17).

Summing the finite recurrences gives

\[
 \theta_k'(0)=kg,\qquad
 \theta_k''(0)=k(k-1)A, \tag{6.1}
\]

\[
 \theta_k'''(0)
 =k(k-1)(k-2)C
 +\frac{k(k-1)(2k-1)}2B. \tag{6.2}
\]

For completeness, the third-derivative increment at time \(s\) is

\[
 3\mathcal G_2[sg,sg]
 +3\mathcal G_1[s(s-1)A].
\]

The sums
\(\sum_{s<k}s^2=k(k-1)(2k-1)/6\) and
\(\sum_{s<k}s(s-1)=k(k-1)(k-2)/3\) prove (6.2).

By Lemma 5.3, the third signed coefficient of the actual width-first
output is obtained from (5.18). Therefore

\[
 \begin{aligned}
 F_{k,L}^{(3)}(0)
 ={}&\mathcal T_1[\theta_k'''(0)]
 +3\mathcal T_2[\theta_k'(0),\theta_k''(0)]\\
 &+\mathcal T_3[
 \theta_k'(0),\theta_k'(0),\theta_k'(0)].
 \end{aligned} \tag{6.3}
\]

Insert (6.1)--(6.2) and the tensor identities
(5.23)--(5.25). This gives

\[
 F_{k,L}^{(3)}(0)
 =2k(k-1)(2k-1)H
 +\frac{k(4k^2-3k+1)}2S. \tag{6.4}
\]

Substitution of \(2t\) and \(t\) into (6.4) yields

\[
 \frac{F_{2t,L}^{(3)}(0)-8F_{t,L}^{(3)}(0)}6
 =t(2t-1)\left(2H+\frac12S\right). \tag{6.5}
\]

By (1.1) and (5.22), \(H=H_L\) and \(S=S_L\). Thus (6.5) proves
Theorem 1.1. The compact nine-moment formulas proposed in the preceding
study are not needed for this implication and are not asserted here
without a separate nodewise reconstruction.

If \(d=\mathbb E\phi'(G)^2=0\), continuity and Gaussian full support
imply that \(\phi\) is constant. The exact output is linear in total step
size, so the discrepancy and (1.3) vanish.

## 7. Small-case and counterexample audit

### 7.1 Linear activation, one hidden layer

For \(L=1\) and \(\phi(x)=x\),

\[
 \binom{a_{s+1}}{u_{s+1}}
 =\begin{pmatrix}1&h\\h&1\end{pmatrix}
 \binom{a_s}{u_s}.
\]

With independent standard Gaussian \(a_0,u_0\),

\[
 F_{k,1}(h)
 =\frac{(1+h)^{2k}-(1-h)^{2k}}2. \tag{7.1}
\]

Thus \(S=0,H=2\), and the cubic coefficient of the discrepancy is

\[
 {4t\choose3}-8{2t\choose3}=4t(2t-1), \tag{7.2}
\]

which equals \(t(2t-1)(2H+S/2)\).

### 7.2 Time counts

Equation (6.4) gives

\[
 F_{1,L}^{(3)}(0)=S,\qquad
 F_{2,L}^{(3)}(0)=11S+12H,
\]

\[
 F_{4,L}^{(3)}(0)=106S+168H. \tag{7.3}
\]

Consequently the four-versus-two coefficient is
\(3S+12H=6(S/2+2H)\), agreeing with Theorem 1.1 at \(t=2\).

### 7.3 Why the adjoint cannot be omitted

Consider the autonomous but non-gradient-observable recursion

\[
 \theta_{s+1}=\theta_s+h(1+a\theta_s),\qquad
 \theta_0=0,\qquad F_k(h)=\theta_k(h).
\]

Then

\[
 F_k^{(3)}(0)=k(k-1)(k-2)a^2,
\]

and

\[
 \frac{F_{2t}^{(3)}(0)-8F_t^{(3)}(0)}6
 =2a^2t(t-1). \tag{7.4}
\]

Its \(t=1\) coefficient is zero while (7.4) is nonzero for \(t>1\).
Thus \(t(2t-1)\) is not a consequence of autonomous Euler algebra alone;
the marked population gradient identity is essential.

## 8. A weaker fifth-order consequence

The marked construction extends verbatim to \(|\alpha|\leq5\): replace
every upper bound three by five and retain the binomial response identity
(3.2). The assumed \(C^{12}\) envelope is the envelope already proved
sufficient for the fifth signed Price compiler.

For the order-five formal Euler recursion, work in
\(\mathbb R[h]/(h^6)\) and write

\[
 \theta_k(h)\equiv
 \theta_0+\sum_{r=1}^5h^ru_r(k)\pmod{h^6}.
\]

The coefficient recurrence from
\(\theta_{k+1}-\theta_k=hG(\theta_k)\) has

\[
 u_r(k+1)-u_r(k)
 \quad\text{polynomial in \(k\) of degree at most \(r-1\)},
\]

provided this is known below order \(r\). Indeed, every term has the form
\(D^mG[u_{j_1},\ldots,u_{j_m}]\), with
\(j_1+\cdots+j_m=r-1\), and hence degree at most \(r-1\). Since
\(u_r(0)=0\), finite summation proves that \(u_r(k)\) has degree at most
\(r\). The chain rule then shows

\[
 P_r(k):=F_{k,L}^{(r)}(0)
 \quad\text{is a polynomial in \(k\) of degree at most \(r\)}. \tag{8.1}
\]

Writing \(P_5(k)=\sum_{j=1}^5a_jk^j\),

\[
 P_5(2t)-32P_5(t)
 =\sum_{j=1}^4(2^j-32)a_jt^j, \tag{8.2}
\]

so the exact fifth derivative of the step-doubling discrepancy is a
polynomial of degree at most four in \(t\). Equation (8.2) is not by
itself a uniform finite-\(h\) fifth-order remainder estimate. The latter
requires a coupled total-time envelope and is a separate obligation.

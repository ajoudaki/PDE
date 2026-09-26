# Initialization-based populations and exact circle outputs

## Corrected question and source scope

The user clarified that the read-in and readout should be constructed from the
same finite initialization-based functions, derivatives and products as the
book's Gaussian calculus. Target-dependent angular rearrangements, although
valid for a larger representation class, did not answer that question.
This note keeps w=G exactly and chooses bounded readouts from initialized tanh
features and their derivatives. M is a selectable finite matrix. It is a static
calculation, not a claim about training from the zero canonical readout.

The source/response law is global_nonlinear.md Section 3, especially (3.5).
Its polynomial-core dictionary and contraction formula (H3.1) retain the
response from reusing the initial action in reverse. The degree-three
orthogonal-polynomial direction below is already motivated in that book's
"Dense compatible hierarchy and relevant enrichments" passage. Additional
foundations read are gaussian_calculus.md Sections 1–4, 7.1, the factorization
portion of 7.2, 8.3, and the appended derivative-tree and Gaussian-forest
sections A and B. These prove finite identities; convergence of the series
used here is justified separately below. No numerical experiment is used.

## 1. Fixed Gaussian initialization variables

Let G_1,G_2,Z_1,Z_2 be independent standard lower Gaussian marks, and T_1,T_2
independent standard Gaussians in the separate upper population. Write

\[
h_i=\tanh G_i,\quad v=E\tanh^2G,\quad
\Xi_i=\sqrt v T_i,\quad H_i=\tanh\Xi_i,
\quad \tau=EH_i^2,\quad \alpha=1-\tau,
\quad k_i=\tanh(\sqrt\tau Z_i+\alpha h_i).
\]

The last term alpha h_i is the actual reused-action response, not an
independent Gaussian replacement. At p=1 the raw dictionaries are
psi_1=(1,h_1,h_2,k_1,k_2)^T and psi_2=(1,H_1,H_2)^T. At p=2,3 the raw
dictionaries span all polynomials of degree at most p in the respective core
variables; the appended word prefix adds no new feature at those orders.

Let L_l L_l^T=E[psi_l psi_l^T]+eta_p I be the book's ridge Cholesky factors,
b_l=L_l^{-1}psi_l, and define the raw-coordinate matrix

\[
K=L_2^{-T}ML_1^{-1},\qquad M=L_2^T K L_1.
\tag{1}
\]

For u_theta=(cos theta,sin theta), choose the unmodified read-in w=(G_1,G_2).
Writing A_p(theta)=E_1[psi_1 tanh(G dot u_theta)], the exact prediction is

\[
f_{p,K,c}(\theta)=E_2[c\tanh(\psi_2^T K A_p(\theta))].
\tag{2}
\]

Thus only finite deterministic matrix entries and coefficients of specified
initialization words are varied. The Gaussian coordinates are not rearranged.
Unit radius refers to normalized network input u=x/sqrt(2).

## 2. Exact initialization-derivative series for the lower channels

Let He_m be the probabilists' Hermite polynomial, specified by
exp(tx-t^2/2)=sum_m He_m(x)t^m/m!. Repeated Gaussian integration by parts
gives, for smooth bounded functions with bounded derivatives of each fixed
order,

\[
E[F(G)\operatorname{He}_m(G)]=E[F^{(m)}(G)].
\tag{3}
\]

Boundary terms vanish because each fixed Gaussian-density derivative is a
polynomial times that density. Define the initialized scalar constants

\[
d_m=E[\tanh^{(m)}(G)],\quad
j(g)=E_Z\tanh(\sqrt\tau Z+\alpha\tanh g),\quad
e_m=E[j^{(m)}(G)].
\]

All are finite. Differentiation of j is justified by bounded derivatives of
the fixed tanh composition. Only odd m contribute, by parity. For -1<=rho<=1,

\[
A(\rho)=\sum_{m\ {m odd}}\frac{d_m^2}{m!}\rho^m,
\qquad
B(\rho)=\sum_{m\ {m odd}}\frac{e_m d_m}{m!}\rho^m.
\tag{4}
\]

These are exact Hermite covariance series, not unproved Taylor summations.
For correlated standard Gaussians X,Y with correlation rho, their generating
functions give E[He_m(X)He_n(Y)]=1_{m=n}m!rho^m. Expanding the two functions
in their Gaussian L2 Hermite bases and using (3) therefore gives
A(rho)=E[tanh X tanh Y] and B(rho)=E[j(X)tanh Y]. In particular
A(1)=v, A(0)=0. Parseval and Cauchy–Schwarz give

\[
\sum_m d_m^2/m!=v,\qquad
\sum_m |e_m d_m|/m!\le\sqrt{E[j(G)^2]v}.
\]

Consequently both series converge absolutely and uniformly on [-1,1],
including correlations +1 and -1. The Gaussian Hermite basis completeness
used here can be checked as follows: if an L2 Gaussian function is orthogonal
to all He_m, its transform E[F(G)exp(zG-z^2/2)] is entire by Gaussian tails
and Cauchy–Schwarz, and all derivatives at zero vanish. Its imaginary-axis
values show that the Fourier transform of the integrable density F times
the Gaussian density is zero. Fourier uniqueness makes F zero almost surely.
Orthogonality itself follows by expanding E exp(sG-s^2/2)exp(tG-t^2/2)=exp(st).

It follows that the complete raw p=1 lower vector is

\[
A_1(\theta)=
(0,A(\cos\theta),A(\sin\theta),B(\cos\theta),B(\sin\theta))^T.
\tag{5}
\]

This retains the reverse response through j and B. More generally, for a
bounded smooth lower dictionary word F(G,Z), set Fbar(G)=E_Z F(G,Z). With
multiindex a=(a_1,a_2), write a!=a_1!a_2!, u^a=u_1^{a_1}u_2^{a_2}. Then

\[
E[F\tanh(G\cdot u)]
=\sum_{a\in\mathbb N^2}
\frac{E[\partial^a\overline F(G)]d_{|a|}}{a!}u^a,
\qquad |u|=1.
\tag{6}
\]

To check coefficients, the Hermite generating function of G dot u factors
into the two coordinate generating functions, because |u|=1. Integration
by parts then gives the displayed coefficients. Absolute convergence follows
by Cauchy–Schwarz in the multivariate Hermite basis. The total-degree tail is
uniform in u: its second squared factor is
sum_{m>N}d_m^2/m!, since sum_{|a|=m}u^{2a}/a!=1/m!. The first is bounded by
E[Fbar^2]. Thus (6) is a genuine convergent angular description in terms of
finite initialization derivative expectations. It also applies to products
and derivatives in the retained p=3 dictionary.

## 3. A global moment expansion for every finite middle matrix

Equation (2) is already a finite Gaussian integral. To supply a convergent
functional expansion, rather than merely leave that integral unevaluated,
put Q(theta)=psi_2^T K A_p(theta). For p<=3, the retained Chebyshev feature
entries have absolute value at most one. Hence |Q(theta)|<=S for all theta
and upper marks with S=sum_{i,j}|K_ij|. If S=0 the output is zero.

For S>0, define

\[
\gamma_k(S)=\frac2\pi\int_0^\pi
\tanh(S\cos\varphi)\cos(k\varphi)\,d\varphi\quad(k\ge1).
\]

The Chebyshev expansion of tanh(Sx) on [-1,1] has zero even coefficients,
including the constant, and

\[
\tanh(Sx)=\sum_{k\ {m odd}}\gamma_k(S)T_k(x),\qquad
|\gamma_k(S)|\le\frac{2(S+2S^2)}{k^2}.
\tag{7}
\]

For the bound let g(varphi)=tanh(S cos varphi). Its derivative vanishes at
0 and pi, and |g''|<=S+2S^2. Two integrations by parts give (7). The
coefficient bound gives absolute uniform convergence of the cosine series;
it equals g because it has g's Fourier coefficients (Fourier uniqueness,
or the positive approximate-identity convolution proof). This proves (7)
for every finite S, not just within tanh's Taylor radius.

For any specified bounded initialization-word readout c, dominated summation
therefore gives the exact formula

\[
f_{p,K,c}(\theta)=\sum_{k\ {m odd}}\gamma_k(S)
E_2\left[c\,T_k\!\left(\frac{\psi_2^T K A_p(\theta)}S\right)\right].
\tag{8}
\]

Every term is a finite polynomial in the known channel functions A_p(theta).
Its coefficients are finite products/contractions E[c prod_j psi_{2,j}^{a_j}]
of initialized dictionary words, precisely finite Gaussian-calculus data.
Products of tanh functions and their derivatives are bounded at each fixed
order; no polynomial approximation was silently substituted into the network.
The tail after degree N>=1 is bounded uniformly in theta by
2(S+2S^2)E|c|/N. This simple bound is sufficient to justify convergence;
it is not claimed sharp. All M are covered by (1),(8), with constants depending
on their magnitude. The infinite summation is not itself a single finite
forest calculation, and its coefficients need not be rational or elementary.

## 4. A direct initialized readout distinguishing p=1,2 from p=3

Let H=tanh(sqrt(v)T), define mu_j=E H^j, and set

\[
\lambda_0=\mu_4/\mu_2,\qquad
P_3(H)=H^3-\lambda_0H,\qquad
\nu=EP_3(H)^2=\mu_6-\mu_4^2/\mu_2>0.
\tag{9}
\]

Strict positivity holds because the nonzero polynomial P_3 cannot vanish on
the interval supporting H's positive density. This is the monic degree-three
orthogonal polynomial used in the book's enrichment argument: symmetry gives
orthogonality to 1,H^2, and the chosen coefficient gives orthogonality to H.
The same readout can be written using an initialized activation derivative:

\[
c=P_3(H_1)=(1-\lambda_0)\tanh\Xi_1+
\tfrac12\tanh''\Xi_1.
\tag{10}
\]

This uses tanh''(x)=2tanh^3(x)-2tanh(x). It is a bounded finite combination
of initialized words, with coefficients computed from initialized moments.
Keep this SAME readout and w=G for all compared orders.

For p=1 and p=2, P_3(H_1) is orthogonal to every upper retained feature.
Each upper monomial is H_1^a H_2^b with a+b<=2; independence reduces its
pairing to E[P_3(H_1)H_1^a] E[H_2^b], which is zero. Changing to the ridge
normalized basis preserves this zero pairing. Hence for every fixed matrix
direction M_0, writing K_0=L_2^{-T}M_0L_1^{-1},

\[
\left.\frac d{dt}f_{p,tK_0,c}(\theta)\right|_{t=0}=0
\quad(p=1,2).
\tag{11}
\]

The output is odd in t, and |tanh z-z|<=|z|^3/3 gives a uniform O(t^3)
bound for fixed M_0. This concerns variation around zero M with the chosen
nonzero readout; it is not the canonical training initialization M=D,c=0.

At p=3, P_3(H_1) is an available upper direction. In Chebyshev coordinates
it is (1/4)T_3(H_1)+(3/4-lambda_0)T_1(H_1). Select the lower direction h_1.
For a real parameter t, specify raw matrices by their resulting action:

\[
Q_1(\theta)=tH_1 A(\cos\theta),\qquad
Q_3(\theta)=tP_3(H_1)A(\cos\theta).
\tag{12}
\]

Both are realized by finite raw K and actual M through (1): for p=1 set
K_{H_1,h_1}=t; for p=3 set its h_1 column equal to t times the displayed
Chebyshev coefficient vector of P_3. All other entries are zero. These
directions have different normalized Frobenius costs; t is the coefficient
of the stated raw action, not an assertion of equal numerical M norms.

The exact whole-circle functions are

\[
f_1(t,\theta)=E[P_3(H)\tanh(tH A(\cos\theta))],
\quad
f_3(t,\theta)=E[P_3(H)\tanh(tP_3(H) A(\cos\theta))].
\tag{13}
\]

They have the all-t convergent representation (8). More simply, on
|t|v max(1,||P_3||_infinity)<pi/2, write tanh z=sum_{j>=0}a_{2j+1}z^{2j+1},
where a_1=1,a_3=-1/3,a_5=2/15,... . The poles at +/-i pi/2 give this Taylor
radius; the strict uniform argument bound justifies termwise expectations.
With x=A(cos theta), the explicit convergent moment series are

\[
f_1(t,\theta)=\sum_{j\ge0}a_{2j+1}(tx)^{2j+1}
(\mu_{2j+4}-\lambda_0\mu_{2j+2}),
\]
\[
f_3(t,\theta)=\sum_{j\ge0}a_{2j+1}(tx)^{2j+1}
E[P_3(H)^{2j+2}].
\tag{14}
\]

The last coefficients are finite combinations of mu_j by the binomial theorem.
In particular, uniformly over the circle as t tends to zero,

\[
f_1(t,\theta)=-\frac{t^3\nu}{3}A(\cos\theta)^3+O(t^5),
\quad
f_3(t,\theta)=t\nu A(\cos\theta)
-\frac{t^3}{3}E[P_3(H)^4]A(\cos\theta)^3+O(t^5).
\tag{15}
\]

The different leading orders are exact derivative statements with controlled
analytic remainders. In particular they identify an initialization-based
readout channel that p=3 couples to linearly in M, while p=1 and p=2 cannot
couple to it at first order in any M direction. This is a structural/local
response distinction, not global nonrepresentability, matched-norm accuracy
ordering, or a training-performance claim.

## 5. What the corrected answer establishes

The natural comparison fixes finite initialization-based choices such as
w=G and c=P_3(H_1), then studies M and dictionary order. Gaussian calculus
provides exact initialized moments/derivatives; (4),(6),(8) turn them into
convergent circle-function descriptions, and (13)–(15) give a concrete family.
No arbitrary target-dependent population encoding is used. These tanh
expressions need not reduce to elementary functions or finite Fourier sums;
the exact convergent series is the functional description established here.
The unrestricted universality statement in CAPACITY.md does not resolve this
restricted question. Nothing here is an assertion about temporal Taylor
convergence or about what canonical gradient flow learns.

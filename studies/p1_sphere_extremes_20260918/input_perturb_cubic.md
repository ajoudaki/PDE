# The robust PSD equilibria also have cubic descent

2026-09-18. Lead post-comparison corollary. Scientific input is the complete
frozen input_perturb_persist.md and the canonical docs/observable_p1.md;
no experiment or external theorem. This does not imply a positive or null
basin. It verifies that the robust flat equilibria are not local minima.

Use the exact carrier realization of input_perturb_persist.md, Section 2:
epsilon_1=sign(G_1), B_1=q dot b_1, kappa=E|B_1|>0,

\[
w=\epsilon_1\sigma s_J,\quad M=e_1q^T,\quad
a_i=\lambda A,\quad v_i=z e_1,\quad z=\lambda\kappa>0,
\]

where the finite assignment (J,sigma) depends only on |G_2|. All s_j are
nondegenerate critical points of
Q(s)=sum_i rho_i phi(s dot u_i). The common feature is
H=phi(zB), B=b_{2,1}, and the constructed readout has d=0.
All canonical coordinate-pair correlations are retained.

Choose a pair (j,sigma_0) with positive assignment probability. Let E
denote its |G_2| event. Since D²Q(s_j) is invertible, choose r in R3
with r^T D²Q(s_j)r!=0. Such an r exists: otherwise polarization would
make the symmetric Hessian zero.

Let psi be a bounded nonzero centered even function of G_3; for example
psi=1_{|G_3|<=1}-P(|G_3|<=1). Define the bounded odd lower direction

\[
h=\epsilon_1\,\mathbf1_E\,\psi\,r.
\tag{1}
\]

For every i,

\[
Da_i[h]=E_1[b_1\phi'(w\cdot u_i)(h\cdot u_i)]=0.
\tag{2}
\]

On E the gate is the constant phi'(s_j dot u_i). For coordinate-one
mark entries, the independent factor E psi=0 kills the pairing. For
every other coordinate-pair entry the independent factor
E epsilon_1=0 kills it, including coordinate three where psi may be
correlated with the mark. Off E the direction is zero. This proves (2)
without replacing the joint canonical law.

Put J_1=B phi'(zB) and take the upper direction

\[
k=J_1-\frac{E_2[J_1H]}{E_2[H^2]}H,\qquad
D_k=E_2[kJ_1]=\|k\|_2^2>0.
\tag{3}
\]

The strict inequality follows from H,J_1 independence, already proved in
the frozen input. The upper moment vector induced by k is D_k e_1 by
coordinate independence and centering, and E[kH]=0.

Along the straight physical path (w+v h,c+v t k,M), with scalar t
fixed and path parameter v, (2)--(3) and d=0 give f_i'=f_i''=0.
In the third prediction derivative the only surviving term is

\[
f_i'''=3t D_k q^T D^2a_i[h,h].
\]

Indeed every upper chain-rule term with a first effective-vector
variation vanishes by (2), and the unperturbed readout term with the
third effective-vector variation is multiplied by d=0. Bounded h,k,
marks, and activation derivatives justify differentiation.

The unhalved loss therefore has L'=L''=0 and

\[
\begin{aligned}
L'''
&=6tD_k E_1[B_1 h^T D^2Q(w)h]\\
&=6tD_k\,\kappa\,\sigma_0 P_1(E)\,E[\psi^2]\,
          r^T D^2Q(s_j)r.
\end{aligned}
\tag{4}
\]

For the second equality, Q is odd so D²Q is odd; on E,
D²Q(w)=epsilon_1 sigma_0 D²Q(s_j). Also B_1 epsilon_1=|B_1|,
and G_1, |G_2|, G_3 are independent. Every factor apart from its
displayed signs is strictly positive. Choose the sign of t to make
(4) negative. Taylor expansion along this bounded path gives lower
loss for all sufficiently small positive v and higher loss for small
negative v.

Consequently every PSD equilibrium made by the seven-nondegenerate-
critical-point construction admits a bounded cubic descent direction.
This includes the fully freely perturbed open data sets. It is a
degenerate saddle with an actual PSD Hessian, not a bad local minimum.

Cubic descent excludes attraction of a whole neighborhood to this
point, since a lower-loss start cannot converge to a higher-loss
endpoint under gradient flow. It does not determine whether a
one-sided or otherwise proper attracting basin has positive measure.
No claim about Lyapunov stability of an entire equilibrium set or
about canonical initialization follows.


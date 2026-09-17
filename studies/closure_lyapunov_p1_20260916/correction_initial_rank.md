# Domain of the matrix correction for arbitrary three inputs

2026-09-16. Root algebraic extension of the definition domain, not of the
training convergence theorem. Inputs are the complete initialized scalar
map proof in three_coordinate_candidate.md, section 5, and the definition
in correction_matrix.md. No experiment or new network theorem is used.

For the exact canonical d=3, p=1 dictionary, that proof establishes for
every unit vector v the initialized field

    H0(v)=tanh(Z.k(v)), k(v)=(kappa(v1),kappa(v2),kappa(v3)),

where kappa is odd and strictly increasing, and Z has positive density
on the open cube (-1,1)^3. Therefore k(v)!=0, and k(v)=+/-k(u) holds
exactly when v=+/-u.

Let v1,v2,v3 be unit signed inputs such that no two are equal or opposite.
The three fields H0(vi) are linearly independent in upper population L2.
Indeed, suppose sum_i a_i tanh(Z.k(vi))=0 almost surely. Continuity and
the positive density make this identity valid throughout the open cube.
Choose a vector z avoiding the finitely many planes orthogonal to k(vi)
or to k(vi)+/-k(vj). Each plane is proper by the preceding paragraph;
a finite union cannot cover R3, as follows, for example, by restricting
their nonzero product of linear forms to a line on which that polynomial
is nonzero. Put t_i=z.k(vi). Then each t_i is nonzero and their squares
are pairwise distinct.

Restrict the identity to Z=s z for all sufficiently small real s. The
coefficients of s, s^3 and s^5 in tanh(s t_i) give

    sum_i a_i t_i=0,
    sum_i a_i t_i^3=0,
    sum_i a_i t_i^5=0,

using tanh(s)=s-s^3/3+2s^5/15+O(s^7). This linear system has determinant
equal up to sign to

    (t1 t2 t3) product_(i<j)(t_j^2-t_i^2),

which is nonzero. Thus every a_i=0, proving independence.

Consequently the probability-normalized initialized upper Gram Gamma0
is positive definite for EVERY such signed triple, regardless of their
input Gram rank or mutual angles. The matrix potential

    Phi_mat=L+mu0(1+q) xi^T(Gamma0+p p^T)^(-1)xi,
    p=(f(v_i))_i/sqrt(3), xi=p-1/sqrt(3),
    mu0=[n^T Gamma0^(-1)n]^(-1), n=1/sqrt(3),

is well defined at every finite current state for every one of those
data sets. Its loss comparison and initialized value two follow exactly
as in correction_matrix.md. This extends the FORMULA'S domain beyond
neighborhoods of the rho family. It does not prove its derivative has
the required sign on that larger domain. A new theorem about initialized
flow must still control the exact defect in that report.

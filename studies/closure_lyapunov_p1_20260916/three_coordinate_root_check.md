# Author-side reconstruction of the three-coordinate candidate

2026-09-16. Root read all 711 lines of the frozen candidate
`three_coordinate_candidate.md`, SHA-256
`531b1cb1fe5e5844fcc6da25486e6ee52450860030dd770246e3ee78592521ce`,
and reconstructed the argument against the complete established
`docs/observable_p1.md` and the previously read canonical closure sources.
The scalar initialization calculation in `arbitrary_pair_local.md` was
also reread. This is an author-side check, not a fresh isolated review or
promotion review. The separate fresh review is `three_coordinate_audit.md`.

## Scope and exact coefficients

The result changes the input dimension to three. It does not solve the
generic three-input problem for the prescribed two-dimensional circle
dictionary. The physical input scaling becomes x=sqrt(3)u. The marks,
eta=1/4096, lower correlations, reverse-response summand tau gamma,
inverse lower-Cholesky normalization, full M and its transpose all match
the established general-dimensional initialized construction. Its trained
population existence is proved directly, not imported from a network limit.

The feature-map contraction identity is exact:
L^{-1}G L^{-T}=I-eta L^{-1}L^{-T}. Bounded marks make the field locally
Lipschitz on bounded increments w-g and bounded c. Energy and |H|<=1
give, successively, c-infinity<=2t, ||M-D||F<=2t^2 and
||w-g||infinity<=B1(2||D||op t^2+2t^4). These bounds justify continuation
in that Banach space and retain the complete saved-state correlations.

## Symmetry and rank

For any permutation P, changing lower variables by (G,zeta)->(PG,Pzeta)
and upper variables by Xi->P Xi preserves their exact laws. Both normalized
feature bands transform by the orthogonal matrices Q1=diag(1,P,P) and
Q2=diag(1,P). Their repeated scalar Cholesky blocks commute with these
matrices and Q2^T D Q1=D. Direct substitution gives

    a_T(u)=Q1^T a(Pu),    H_T(u)=H(Pu) composed with S2,
    f_T(u)=f(Pu).

The corresponding state transformation is a physical isometry. Thus the
ambient loss gradient, not only the restricted prediction, is equivariant.
Unique initialized evolution preserves all permutations. Architectural
oddness absorbs the third negative label; transitivity then gives three
equal signed predictions and the full equation Xdot=2(1-F) grad F.

The initialized map kappa(t) is dimension-independent because (g_i,g.u)
is a centered unit-variance Gaussian pair with correlation u_i. The proof
retains a possibly negative first regression coefficient and proves the
whole conditional regression function has positive derivative. The
Gaussian integration-by-parts cancellation and endpoint extension are
valid by bounded derivatives and dominated convergence.

With p=kappa(a), z=kappa(b), the coefficient matrix has eigenvalues
p-z,p-z,p+2z. Strict monotonicity gives p!=z. If the last eigenvalue is
zero, any possible functional relation has equal coefficients. Its cubic
derivative on a coordinate line is 12 t0 z^3, nonzero unless t0=0; z=0
would force p=z and is excluded. This proves rank three even in the
exceptional linear coefficient case. The original directions have no
coincident or antipodal pair. Initial rank establishes nonredundant
constraints; the evolving residuals nevertheless have only one direction
because of this exact data symmetry. These are different statements.

## Potential and endpoint

In the auxiliary gradient parameter s, readout linearity gives
F_s=K=||U||^2+||grad_(w,M)F||^2 and q_s=2F. At zero readout,
c=s U0+o(s), F=C0 s+o(s), q=C0 s^2+o(s^2). Hence the initial
one-sided value of q/F^2 is 1/C0. Cauchy--Schwarz gives

    (q/F^2)_s = -2(qK-F^2)/F^3 <= 0,
    q <= F^2/C0,       ||U||^2 >= C0,       K >= C0.

This also verifies every division: C0>0, and F,q>0 for s>0. The regular
factor Psi=(1+q)/(C0+F^2) satisfies

    Psi_s = -2F[(qK-F^2)+(K-C0)]/(C0+F^2)^2 <= 0.

Finite-s existence and K>=C0 ensure a unique finite s* with F(s*)=1.
On [0,s*], K is bounded; the physical reparametrization
s_dot=2(1-F) has strictly positive residual at every finite t and tends
to s*. This removes any potential circular assumption that the physical
residual remains positive or that a fitted endpoint already exists.

For Phi=L(1+C0 Psi), one has 0<C0 Psi<=1 and therefore L<=Phi<=2L.
Differentiating both factors gives exactly candidate equation (43),
including the nonpositive Psi contribution. Thus Phi_dot<=-4C0 Phi
from initialization, with Phi(0)=2, and independently L<=exp(-4C0 t).
There is no changing metric, collapsing distance, or future-defined input
to the potential.

Finally ||Xdot||=2(1-F)sqrt(K)<=-(1-F)_dot/sqrt(C0) gives the claimed
remaining length. The finite auxiliary endpoint additionally gives
convergence in bounded characteristic increments. Same-mark coupling
proves the joint-law W2 conclusions. Neither a uniform full-Gram bound,
strict hidden contrast gain, nor an endpoint unique across initial states
was used or proved.

**Outcome:** every displayed claim passes this author-side reconstruction
at its stated d=3 symmetric-family scope. Acceptance of a dimensional
extension is a separate user preference; this mathematical check does not
convert it into a solution of the original circle problem.

Source versions:

```text
0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba  docs/observable_p1.md
81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c  docs/global_nonlinear.md
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
```

# Root-side check of the cubic residual feedback

This is an independent coefficient calculation during thep7 extension,
before receiving another route's evaluated beta constants. It uses the
previously frozen R,J,beta definitions in P45_DERIVATION_ROUTE.md and the
complete Gaussian source rule in established global_nonlinear sections3.1–3.3.

Let h=tanh(G),ell=1-h²,v=E[h²],kappa=E[ell²],u=E[h²ell²]. Independently,
H=tanh(sqrt(v)G),d=1-H²,e=-2Hd,tau=E[H²]. Put
A_diag=E[d²+He],A_cross=(E[d])². Gaussian reverse response gives
W0*(Sd_a)=zeta+sum_j h_j y_j A_aj, with reverse innovation second moment
E[S²d_a²]. Consequently define

    T_diag=(v+kappa)E[H²d²]+u A_diag²,
    T_cross=(v+kappa)tau E[d²]+v kappa A_cross².

Indeed E[H_a d_b R_b]=(y_a y_b/2)T_ba: moving the initialized adjoint in
the W0L contribution gives kappa times the upper second moment, plus the
lower-root response product E[ell_b²h_a²] A_ba². Upper/lower independent
axis parity kills the other label index. Thus the J pairing contributes
(y_a/6)sum_b y_b²T_ba, and E[S d_a R_a] contributes
(y_a/2)sum_b y_b²T_ab. The tensors are symmetric in the two equal-variance
axes, yielding

    beta_a=(2/3)y_a(T_diag y_a²+T_cross y_(3-a)²).

A256-node one-dimensional Gauss-Hermite arithmetic check gives
beta_self≈0.05349737956078973, beta_cross≈0.1276552562143645.
They differ; beta is not a scalar radial multiple of y in general. This
alone does not prove thatp6 needs a new raw span, since all beta-polarized
factor fields might still combine into existing columns. That separate
containment question must be settled by the full coefficient calculation.

Every coefficient above depends only on initialized Gaussian moments, not
on a task's imposed labels. The numerical check is a deterministic algebra
diagnostic, not a training run, rigorous quadrature enclosure, or strong-flow
regularity theorem. The independent contraction implementation will record
the reproducible resolution comparison before accepting these constants.

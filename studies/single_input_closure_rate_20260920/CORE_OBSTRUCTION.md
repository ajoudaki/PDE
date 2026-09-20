# What polynomial degree alone cannot repair

Author candidate, 2026-09-20. This is a separate scope check, not an obstruction
to the maintained H3 hierarchy, whose bounded-word prefix also grows.

## Precise comparison

Train the canonical two-hidden-tanh population model on normalized input e1
with label +1, retaining a two-coordinate Gaussian first row. Set

    h_i=tanh(g_i), Y_i=A0 h_i, H_i=tanh(Y_i), p_i=A0*H_i, i=1,2.

Write q=E h_1², v=E H_1² and alpha=E sech²(Y_1). The maintained finite
Gaussian source law gives independent Y_i~N(0,q) and

    p_i=zeta_i+alpha h_i,

where (zeta_1,zeta_2)~N(0,v I) is independent of g. The fixed H3 polynomial
core generates precisely

    G1=sigma(g_1,g_2,zeta_1,zeta_2), G2=sigma(Y_1,Y_2).

Indeed tanh is an invertible measurable map and the p_i recover zeta_i from
g. Let P_l be conditional expectation onto L2(G_l), and B=P2 A0 P1.
Consider the same autonomous population gradient flow with initial action B
and middle increments constrained by P2 and P1. Its hidden row and readout
remain measurable in G1 and G2. This is the limiting model of increasing
polynomial degree in this fixed core without appending new action words.

At initialization B h_1=Y_1, since h_1 belongs to G1 and Y_1 to G2. Thus
the two models have identical initial training hidden fields and predictions.

## A missing reverse innovation

Put d=H_1(1-H_1²). Append the query A0*d after the two forward and reverse
core queries. The exact source rule gives

    A0*d=zeta_d+b h_1,   b=E[d'(Y_1)].

The centered reverse Gaussian source has variance E d² and covariance
E[d H_i] with zeta_i; it is independent of g. Symmetry and independence give
E[d H_2]=0. Consequently

    P1 A0*d=(E[d H_1]/v) zeta_1+b h_1,
    A0*d-P1 A0*d=xi,
    E xi²=omega:=E d²-(E[d H_1])²/v>0.

Here xi is centered Gaussian independent of G1. Strict positivity is the
strict Cauchy--Schwarz inequality: d would have to be a constant multiple of
H_1 almost surely, whereas 1-H_1² is nonconstant on its continuous law.

Let J0 be the differential at initialization of the upper hidden feature
h=tanh(A tanh(w_1)) with respect to the raw hidden variables (w,K), using
row L2 and middle HS metrics. Its adjoint applied to H_1 has components

    J0*H_1=(sech²(g_1) A0*d, d tensor h_1).

For the projected model these are

    JB,0*H_1=(sech²(g_1) P1 A0*d, d tensor h_1).

The second component is unchanged since both factors belong to the retained
sigma fields. Orthogonality of xi to G1 yields the exact positive difference

    ||J0*H_1||²-||JB,0*H_1||²
        =omega E sech^4(g_1)=:D>0.                         (1)

## Detectability in prediction

Both single-input models have feature-time equations c_s=h and hidden_s=J*c.
At s=0, c=0 and hidden_s=0. Strong derivatives at zero therefore give

    c_s(0)=H_1, h_s(0)=0,
    hidden_ss(0)=J0*H_1,
    h_ss(0)=J0 J0*H_1,
    c_sss(0)=J0 J0*H_1.

These statements can be read as finite-order expansions, without assuming
three-times Frechet differentiability of a nonlinear map on L2. Here are the
required difference quotients. Bounded c_s=h and strong continuity imply
c(s)/s -> H_1 in L2 and |c(s)/s|<=1. Thus
d_2(s)/s -> d in L2, by subtracting c(s)/s-H_1 and then using bounded
multiplier continuity on H_1. The bounded action/HS continuity gives
A(s)*d_2(s)/s -> A0*d in L2. Multiplication by the lower gate converges
strongly on this convergent L2 vector: truncate its fixed limiting vector
and use bounded convergence on the truncated part. The same rank subtraction
gives K_s(s)/s -> d tensor h_1 in HS. Hence

    (hidden(s)-hidden(0))/s² -> (1/2) J0*H_1.

For a scalar C1 function with bounded continuous derivative, if
(z(s)-z0)/s² -> a in L2, its mean-value integral shows
(phi(z(s))-phi(z0))/s² -> phi'(z0)a in L2: subtract a first, then use
the same bounded-multiplier continuity. Apply this to the lower activation,
then the bounded action product rule, then the upper activation. It gives
(h(s)-H_1)/s² -> (1/2)J0 J0*H_1. Integrating c_s=h gives the stated cubic
expansion of c. Every vector and rank used is square integrable, since the
gates are bounded and the initialized action is bounded. This argument
requires no higher-time derivative or positive Taylor convergence radius.

Expanding just to this finite order gives, for the training prediction,

    f(s)=v s+(2/3)||J0*H_1||² s³+o(s³).

Thus f(s)-f_B(s)=(2/3)D s³+o(s³). The physical clocks satisfy
s_t=2(1-f(s)), with s(0)=0, and their difference is O(t^4) because the
feature prediction difference is O(s³). Since s(t)=2t+O(t²),

    f(t,e1)-f_B(t,e1)=(16/3)D t³+o(t³)>0                 (2)

for sufficiently small positive t. This is an error in approximation of the
same neural prediction, not a risk or model-performance comparison.

## Polynomial-core limit and consequence

Products of Chebyshev polynomials on the bounded core cubes span the
polynomials; continuous functions on a cube admit uniform polynomial
approximation by the elementary multivariate Bernstein construction.
Continuous bounded functions are dense in L2 of the finite core law: first
truncate to a compact interior box, approximate rectangular indicators by
continuous ramps using the continuous joint density, and then approximate
simple functions. Thus the union of polynomial spans is dense in L2(G_l).
With the maintained positive ridge eta_N=1/[1024(N+1)^2], the filter estimate

    ||(I-Q_N)S_N a||2 <= sqrt(eta_N)|a|/2

on every fixed retained polynomial and contraction of Q_N prove Q_N -> P_l
strongly on the full carrier. Consequently B_N -> B and B_N* -> B* strongly,
uniformly on compact L2 sets. Two-sided filtering of any continuous HS
increment curve tends uniformly to its P2/P1 filtering, by finite-rank
approximation followed by a finite time net.

For one training input the scalar clock X=F(w_1)-F(g_1), F'=cosh², removes
the lower gate exactly. Its transformed vector field is Lipschitz on each
bounded feature-time interval in clock L2, increment HS and readout L2,
when the readout supremum and action norm are bounded; both are bounded by
s and 2+s²/2. Indeed J(X,g)=F^-1(F(g)+X) and tanh J(X,g) are 1-Lipschitz
in X; the only varying backward product has bounded reference readout.
Subtracting the transformed equations therefore bounds the sum error by
L times itself plus the three strong-projection defects just described.
Its initial value is zero; integrating yields an error bounded by
S exp(LS) times the supremum defect, which tends to zero. Prediction follows
by bounded gates. Scalar physical clocks converge on any fixed short
physical interval by ordinary scalar Lipschitz comparison. Thus the
polynomial-core-only models converge to the projected flow used in (2).

Equation (2) rules out vanishing prediction error by raising only the
polynomial degree on the fixed Gaussian core. It does not rule out the
maintained complete hierarchy, since that hierarchy eventually includes
bounded functions of the missing reverse query itself. Nor does it contradict
good low-order approximation at practical tolerances.

This candidate still awaits an independent internal check.

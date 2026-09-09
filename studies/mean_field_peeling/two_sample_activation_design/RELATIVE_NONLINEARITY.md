# Relative nonlinearity and a non-vacuous activation design

This note proves elementary quantitative facts. It does not claim the
global trained population theorem for the moderate coefficients below.

## 1. A distribution-independent measure

For any scalar random variable Z with 0<Var(Z)<infinity and any activation
phi with finite positive variance, define

    N_phi(Z) = inf_(b,c) E[phi(Z)-b-cZ]^2 / Var(phi(Z)).

This fraction is invariant under a nonzero affine change of the output
phi. It measures the feature variance left after its best affine fit.

Suppose phi(z)=az+e psi(z), a>e L>=0, and psi is L-Lipschitz.
Then, for every such Z,

    0 <= N_phi(Z) <= (e L/(a-e L))^2.                 (1)

Proof. For independent copies Z,Z',

    Var(psi(Z)) = E[(psi(Z)-psi(Z'))^2]/2
                 <= L^2 Var(Z).

Also phi is increasing with secant slope at least a-e L, so

    Var(phi(Z)) = E[(phi(Z)-phi(Z'))^2]/2
                  >= (a-e L)^2 Var(Z).

Absorbing az into the best affine fit gives the exact numerator
e^2 inf_(b,c) E[psi(Z)-b-cZ]^2, at most e^2 Var(psi(Z)).
Dividing proves (1). No Gaussian hypothesis is used.

Thus a theorem with a microscopic e/a controls a class that is
quantitatively close to affine on every input law. Allowing e=1 while
making a very large does not resolve this issue. This observation is
compatible with nonzero feature motion: even a deep affine network can
learn features and change its kernel.

## 2. An explicit moderate nonlinear candidate

Let G be standard Gaussian, fix omega>0, and set

    b_omega = omega exp(-omega^2/2),
    r_omega(z) = sin(omega z)-b_omega z,
    v_omega = (1-exp(-2 omega^2))/2
                          -omega^2 exp(-omega^2).

The Gaussian characteristic function gives

    E[G sin(omega G)] = b_omega,
    E[sin(omega G)^2] = (1-exp(-2 omega^2))/2.

For completeness the characteristic function follows by differentiating
I(t)=E exp(itG), applying integration by parts to get I'(t)=-tI(t),
and using I(0)=1. Differentiation is dominated by |G|. Taking real
parts and differentiating at omega gives both displayed moments.

Consequently E r_omega(G)=E[G r_omega(G)]=0 and
E r_omega(G)^2=v_omega>0. Positivity follows because sine is not an
affine function on the full Gaussian support.

For b>0 define the single activation

    Phi_(b,omega)(z) = [z+b r_omega(z)]/sqrt(1+b^2 v_omega).

It has exactly unit initialized Gaussian second moment, and

    N_Phi(G) = b^2 v_omega/(1+b^2 v_omega).          (2)

The derivative is bounded below by

    [1-b omega(1+exp(-omega^2/2))]/sqrt(1+b^2 v_omega).

Thus strict monotonicity holds when b omega(1+exp(-omega^2/2))<1.
For example omega=2 and b=2/5 satisfy this inequality, since
exp(-2)<1/4. They give approximately 6.4 percent nonlinear variance
at initialized unit Gaussian input, with coefficients of moderate size.
Equation (2), not a numerical training experiment, gives this value.

Because its unit Gaussian second moment is exactly one, the initialized
Gaussian variance remains one through every hidden layer. The same
nonlinear fraction therefore holds in all three initialized layers.
The companion SINE_INITIALIZATION.md derives the exact correlation map
and its strict contraction toward zero.

This is an affine function plus a bounded smooth sine perturbation,
so its shape is eligible for a perturbative activation-class theorem
after normalizing derivative bounds. The moderate value b=2/5 is NOT
certified by that theorem's smallness condition. Proving the global
trained result for a fixed candidate of this size remains a distinct
research obligation.

## 3. Literature boundary checked in this investigation

[Yang and Hu, Tensor Programs IV, Appendix A](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf)
explicitly distinguishes its discrete training limit from the extra
continuous-time existence and uniqueness problem. The Gaussian middle
matrix initialization is also distinguished there from other multilayer
mean-field scalings. These distinctions prevent importing a theorem
for a different limit or initialization.

[Chen et al., 2025](https://arxiv.org/html/2503.09565v2)
studies feature independence under discrete SGD and gives an optimality
conclusion under its stated convergence condition. Its Corollary 4.6
uses weights that cease changing after a finite discrete time; arbitrary
asymptotic convergence is not substituted for that condition here. This does
not itself supply the continuous-time existence and compact-time joint
limit required here. No external theorem from either paper is used as
a premise for a new global-flow claim in this folder.

# Exact sign protection in the canonical p=1 initialization

Status: analytic argument frozen by the lead author before comparison with
the independent protected-family route. No quadrature estimate is a premise.
The separate preregistered diagnostic provided numerical evidence against
the simpler guess A>=0. The proof below controls the full conditional
coefficient and uses no diagnostic value.

Use phi=tanh and the exact coefficients in docs/observable_p1.md. To avoid
confusing a variance with a direction, write nu=E phi(G)^2. Let

  tau=E phi(sqrt(nu) Z)^2, alpha=1-tau,
  h=phi(G), k=phi(sqrt(tau) Z+alpha h),
  s=E k^2, beta=E hk, gamma=1-s, eta=1/4096,
  a=sqrt(nu+eta), b=sqrt(s+eta-beta^2/(nu+eta)),
  c_*=sqrt(tau+eta),
  d_h=alpha nu/(a c_*),
  d_k=[alpha beta eta/(nu+eta)+tau gamma]/(b c_*).

G,Z are independent standard Gaussians. Define on [-1,1]

  K(h)=E_Z phi(sqrt(tau) Z+alpha h),
  Psi(h)=d_h h/a+(d_k/b)[K(h)-beta h/(nu+eta)].              (1)

Thus Psi(phi(G_j)) is precisely the conditional initialized row of D b1
given G_j, retaining the actual reverse response and Cholesky subtraction.

## Claim

For every h in (0,1],

  c_* Psi(h)/h >= (alpha/gamma) J_*,
  J_*=7/15-1936/4725-1/65=2552/61425>0.                    (2)

Psi is odd. It therefore has strictly the sign of h off zero. Consequently
the initialized effective vector Da_0(v) has the sign of each component of
v, with a strictly nonzero component whenever that input component is
nonzero. In particular the collapsed diagonal direction has a strictly
positive effective scalar coefficient. This is a fixed-initialization
statement, not a claim that these signs persist for arbitrary training.

## Proof of the scalar bound

First 0<nu,tau,s<1, and alpha,gamma>0. K is odd, K(0)=0, and
0<K'(h)<=alpha. It follows that 0<beta<=alpha nu.

The residual k-(beta/nu)h has squared norm s-beta^2/nu. Gaussian
integration by parts in the independent Z gives

  E[Z(k-(beta/nu)h)]=sqrt(tau) E phi'(sqrt(tau) Z+alpha h)
                  =sqrt(tau) gamma.

The boundary terms vanish because k is bounded. Cauchy--Schwarz then gives

  b^2=s+eta-beta^2/(nu+eta)>=tau gamma^2+eta.

Writing B_*=c_* d_k/b, we obtain

  0<B_*=[alpha beta eta/(nu+eta)+tau gamma]/b^2 <=1/gamma,    (3)

because alpha beta/(nu+eta)<=alpha^2<=1<=1/gamma, and the numerator
is at most (eta+tau gamma^2)/gamma.

Since |phi(z)|<=|z|, phi'(z)=1-phi(z)^2>=1-z^2. Integrating K'
between 0 and h therefore proves, for h>0,

  K(h)/h >=alpha[1-tau-alpha^2 h^2/3]
          >=alpha^2(1-alpha/3)=:m.

Here m<alpha. Applying (3), beta/(nu+eta)<=alpha, and (1) gives

  c_* Psi(h)/h
   >=alpha nu/(nu+eta)+B_*(m-alpha)
   >=(alpha/gamma)[gamma nu/(nu+eta)-1+alpha-alpha^2/3].     (4)

It remains to bound the bracket without numerical integrations.
The inequality log cosh(z)<=z^2/2 follows by integrating tanh(z)<=z
on z>=0 and using evenness. Thus

  E phi'(G)>=E exp(-G^2)=1/sqrt(3),
  nu<=1-1/sqrt(3)<3/7,
  alpha=E phi'(sqrt(nu)Z)>=1/sqrt(1+2nu)
       >=sqrt(7/13)>11/15.                                (5)

Also nu>1/64. One explicit elementary verification is to restrict
|G| to [1/2,1]. This event has probability at least the standard Gaussian
density at 1, which exceeds 1/5 since 2*pi*e<24<25. For z>=0,
phi(z)>=z-z^3/3: the derivative of the difference is z^2-phi(z)^2>=0.
Hence phi(1/2)>=11/24 and phi(1/2)^2>1/5, giving nu>1/25>1/64.
It follows that eta/(nu+eta)<1/65.

Finally gamma=1-E phi(sqrt(tau)Z+alpha h)^2 satisfies

  gamma>=1-E(sqrt(tau)Z+alpha h)^2=alpha-alpha^2 nu.

Using gamma<=1, the bracket in (4) is therefore at least

  2alpha-1-alpha^2(nu+1/3)-1/65.

For alpha in [11/15,1] and nu<=3/7, this expression increases with
alpha and decreases with nu: its alpha derivative is at least
2-2(3/7+1/3)>0. Its value at alpha=11/15,nu=3/7 is precisely J_*>0.
This proves (2). All inequalities include the actual positive ridge.

## Consequence for arbitrary initialized input directions

For -1<r<1 define

  T(r)=E[Psi(phi(G)) phi(rG+sqrt(1-r^2)V)],

where G,V are independent standard Gaussians; take endpoint values by
continuity. For a unit direction v in S2, conditioning the full canonical
lower joint law gives

  Da_0(v)=(T(v_1),T(v_2),T(v_3)).                           (6)

For r>0 the conditional expectation
E_V phi(rG+sqrt(1-r^2)V) is odd and strictly increasing in G, so it
has the same sign as G. Equation (2) shows that its product with
Psi(phi(G)) is strictly positive for G!=0. Thus T(r)>0 for r>0;
oddness gives T(r)<0 for r<0, and T(0)=0. The same argument holds
at r=1, with the second factor phi(G).

At v=(1,1,1)/sqrt(3), equation (6) reads

  Da_0(v)=rho_0 v, rho_0=sqrt(3) T(1/sqrt(3))>0.           (7)

This supplies an analytic nonvanishing premise for a diagonal-reference
clock argument. It does not itself establish endpoint nondegeneracy,
trajectory protection or fitting outside the configurations separately
proved in this study.

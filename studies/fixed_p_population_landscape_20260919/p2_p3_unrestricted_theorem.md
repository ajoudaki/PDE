# Every local minimum fits at canonical orders two and three

2026-09-19. Complete lead assembly within the current study. This removes
the sample-count restriction at p=2 and p=3. The main new step uses the
polynomial space in the image of the current matrix, rather than the
entire dictionary. The independent polynomial-route author supplied the
observation that its separation lemma needs no constant in that current
image. The lower small-set argument and constant-image argument are
reproduced from the present study with all necessary details. No other
study or external specialized theorem is a premise.

## 1. Exact theorem and scope

Fix p=2 or p=3 in the full canonical closure of
docs/global_nonlinear.md C.4.7.10.B, C.1 and D.3. Let

\[
 \mu=\sum_{i=1}^m\mu_i\delta_{(x_i,y_i)},\qquad
 \mu_i>0,\quad \sum_i\mu_i=1,\quad x_i\in\sqrt2 S^1,
\]

where m is any positive finite integer and the labels are finite real
numbers (in particular, arbitrary +1 and -1 labels). First assume
x_i differs from both x_j and -x_j for i different from j.

The fixed lower carrier has the exact joint law of (b_1,g), the fixed
upper carrier the exact law of b_2. Train all fields
w in L2(Omega_1;R2), c in L2(Omega_2), and all entries of M. Local
minima use the physical product norm

\[
 \|\delta w\|_{L^2}^2+\|\delta c\|_{L^2}^2+\|\delta M\|_F^2.
\tag{1}
\]

Write phi=tanh, u_i=x_i/sqrt(2), and use the exact canonical contractions

\[
 a_i=E_1[b_1\phi(w\cdot u_i)],\quad z_i=b_2^TMa_i,\quad
 H_i=\phi(z_i),\quad f_i=E_2[cH_i],\quad r_i=f_i-y_i,
\]
\[
 d_i=E_2[b_2c\phi'(z_i)],\qquad
 \mathcal L=\sum_i\mu_i r_i^2.
\tag{2}
\]

**Theorem. Every local minimum of (2) has loss zero and is a global
minimum, for every finite m, at both p=2 and p=3.**

There is no angular-separation lower bound, input linear-independence
assumption, sample-count bound, rank restriction on M, positive hidden
Gram assumption, or convergence assumption. Repeated and antipodal
inputs are treated in section 7: every local minimum attains the explicit
architectural loss floor, which is zero exactly for compatible labels.

The statement concerns the actual fixed-order population state. It is
not a finite-particle theorem, an L-infinity-local-minimum theorem, or a
claim of convergence of the initialized flow. The prescribed joint
initialization, ridge, actual transpose, loss normalization, and metric
are unchanged.

## 2. The structures present in these exact dictionaries

Let

\[
 X_1=(\phi(g_1),\phi(g_2),\phi(p_1),\phi(p_2)),\qquad
 X_2=(\phi(\xi_1),\phi(\xi_2)).
\]

The established joint initialization is
\[
 \xi\sim N(0,vI_2),\quad
 p_j=\zeta_j+\alpha\phi(g_j),\quad
 \zeta\sim N(0,\tau I_2)\ \hbox{independently of }g,
\]
with v,tau,alpha strictly positive and with the lower and upper
expectations on separate carriers. Thus X_1 has positive density on
(-1,1)^4 and X_2 has positive density on (-1,1)^2.

At p=2 and p=3 the complete retained raw lists are precisely all
total-degree-at-most-p Chebyshev products in X_1 and X_2. Codes 0,1
are the already retained constants; codes 2,3 are unbounded lower
Gaussian seeds and are not extra bounded dictionary entries. No word
is deleted to make this assertion. Consequently the lower and upper
dimensions are (15,6) and (35,10), respectively.

With the book's eta_p=[1024(p+1)^2]^{-1}, retain
\[
 L_\ell L_\ell^T=E_\ell[\psi_\ell\psi_\ell^T]+\eta_pI,\quad
 b_\ell=L_\ell^{-1}\psi_\ell,\quad
 D=L_2^{-1}CL_1^{-T},\quad
 C=E_2[\psi_2(A_0\psi_1)^T].
\tag{3}
\]
The canonical initial state remains w=g,c=0,M=D. No numerical value
or modification of D is needed for an ambient landscape theorem.

A polynomial vanishing almost surely on either core law vanishes on
the open cube by continuity and then identically, by applying the
one-variable polynomial root property in each variable. The Chebyshev
products have distinct leading monomials. Their Gram is positive
definite, and the invertible normalization preserves their span.
In particular:

* the normalized marks are bounded;
* E_1[b_1b_1^T] is positive definite and 1 belongs to the lower span;
* the upper mark span is exactly the real polynomial space of degree
  at most p in X_2, including 1 and a nonconstant coordinate;
* the lower carrier is nonatomic, since g_1 has a continuous law.

The proof below uses these facts without replacing the dictionary,
its metric, its correlations, or the actual current matrix.

## 3. Input ridge independence and a physical small-set condition

For any finite set of unit directions distinct modulo sign, the
functions s -> phi(s dot u_i) are linearly independent. Choose e avoiding
the finitely many hyperplanes orthogonal to u_i and u_i +/- u_j.
Then beta_i=e dot u_i are nonzero and their squares are distinct.
Writing tanh t=sum_{n>=0}(-1)^n A_n t^{2n+1}, phi'=1-phi^2 gives
\[
 A_0=1,\qquad (2n+1)A_n=\sum_{j+k=n-1}A_jA_k>0.
\]
Restriction of a linear relation to s=te and comparison of the first
m odd coefficients gives an invertible Vandermonde system in beta_i^2.

At fixed c,M, the loss is a C2 function of the finite moments a_i:
bounded marks and bounded activation derivatives, together with
E|c|<=||c||_2, justify differentiation and a locally uniform quadratic
remainder. The exact first derivatives are
\[
 \delta\mathcal L=2\sum_i\mu_i r_i d_i^TM\,\delta a_i,\qquad
 \nabla_M\mathcal L=2\sum_i\mu_i r_i d_i a_i^T.
\tag{4}
\]
These use M and its actual transpose.

At a local minimum define
\[
 F_\omega(s)=\sum_i\mu_i r_i
             [b_1(\omega)^TM^Td_i]\phi(s\cdot u_i).
\tag{5}
\]
For almost every omega, w(omega) globally minimizes F_omega over
finite s. Otherwise countability of rational comparison vectors,
positive rational margins, and integer bounds on |w| gives one fixed
s, delta>0, R<infinity, and a positive-measure set B on which
|w|<=R and F_omega(s)-F_omega(w)<=-delta.

Choose subsets E of B with positive probabilities epsilon tending to
zero. Such subsets exist on the canonical lower carrier because
t -> P(B intersect {g_1<=t}) is continuous and ranges from zero to P(B).
Replace w by s on E. Its squared L2 displacement is at most
epsilon(|s|+R)^2, whereas every moment change is O(epsilon), by bounded
marks and activation. Taylor expansion in (4) gives
\[
 \mathcal L_{\rm new}-\mathcal L
 =2\int_E[F_\omega(s)-F_\omega(w)]\,dP_1+O(\epsilon^2)
 \le-2\delta\epsilon+O(\epsilon^2)<0,
\]
contradicting local minimality. No derivative surjectivity of the lower
moment map or assumption of independently trainable sample moments is
used.

Therefore F_omega(w)<=F_omega(0)=0. Matrix stationarity gives
\[
 E_1F_\omega(w)
 =\sum_i\mu_i r_i d_i^TMa_i
 =\tfrac12\langle\nabla_M\mathcal L,M\rangle_F=0.
\]
Thus F_omega(w)=0 almost surely. Its global minimum is zero and it is
odd, so F_omega(s)=0 for every s. Ridge independence gives
r_i b_1^TM^Td_i=0 almost surely. Positive definiteness of the lower
mark Gram now gives the samplewise condition
\[
                         r_i M^Td_i=0\qquad(1\le i\le m).
\tag{6}
\]

## 4. Use the image of the current matrix

The crucial finite-dimensional function space is
\[
 V_M=\{b_2^TMv:v\in\mathbb R^{k_1}\}\subset L^2(\Omega_2).
\tag{7}
\]
It consists of polynomials in X_2. It is allowed to have any rank and
need not contain the constant function. Each z_i belongs to V_M.
Equation (6) says
\[
 r_i E_2[c\,h\,\phi'(z_i)]=0\qquad\hbox{for every }h\in V_M.
\tag{8}
\]

Let H=span{H_1,...,H_m}. For any k in H-perp, changing c to c+tk
preserves every prediction exactly. For sufficiently small t this
equal-value state remains inside the original local-minimum ball and
is itself a local minimum on a smaller ball. Its w,M,V_M,z_i and
residuals are unchanged. Apply (8) at both readouts and subtract.
If r_i is nonzero this gives
\[
 E_2[k\,h\,\phi'(z_i)]=0\qquad(k\in H^\perp,\ h\in V_M).
\]
All h are bounded on the actual carrier; h phi'(z_i) belongs to L2.
Since the finite-dimensional H is closed, orthogonal decomposition
gives
\[
             \phi'(z_i)V_M\subseteq
             \operatorname{span}\{\phi(z_j):1\le j\le m\}.
\tag{9}
\]
This condition involves the available current image, not the whole
dictionary. It therefore needs neither a sample-count argument nor
additional matrix directions.

## 5. Polynomial images rule out condition (9)

**Polynomial lemma.** Let V be a real finite-dimensional polynomial
space in X_2 containing a nonconstant polynomial. For any finite
P_1,...,P_m in V and any index i,
\[
 \phi'(P_i)V\not\subseteq
       \operatorname{span}\{\phi(P_j):1\le j\le m\}.
\tag{10}
\]
There is no requirement that 1 belong to V.

Suppose first P_i is nonconstant. Use the direction h=P_i, which is
available in V. A contrary membership would give
\[
 P_i(X_2)\operatorname{sech}^2P_i(X_2)
       =\sum_j\gamma_j\tanh P_j(X_2).
\tag{11}
\]
Continuity and positive core density turn this almost-sure equality
into a pointwise identity on the open cube. Choose a real affine line
with a segment in that cube along which P_i is nonconstant. This is
possible by choosing a point where its gradient is nonzero and a
direction of nonzero directional derivative. Let Q_j(t) be the
polynomial restrictions to that line.

All nonconstant Q_j have only finitely many critical points in C.
For each integer n, the nonconstant polynomial equation
Q_i(t)=i pi(n+1/2) has a complex solution. Different target values
give different solutions. Choose one, t_0, outside the finite union
of the critical points of all nonconstant Q_j.

At t_0, cosh Q_i has a simple zero: sinh Q_i(t_0) is nonzero and
Q_i'(t_0) is nonzero. Therefore Q_i sech^2 Q_i has a double pole,
whose leading coefficient is nonzero because Q_i(t_0) is nonzero.
Each tanh Q_j has at most a simple pole there. For nonconstant Q_j
this follows from the choice of t_0; a constant Q_j is real and
has no pole. Their finite linear combination cannot have a double pole.

The identity on the real line segment is a meromorphic identity in C.
For an explicit justification, multiply (11) restricted to the line
by cosh^2 Q_i times the product of all cosh Q_j. The resulting
entire-function identity holds on the real segment and hence everywhere
by the holomorphic identity theorem. It implies the original identity
where the denominators do not vanish, contradicting the pole orders
near t_0. This excludes (11).

If P_i is constant, select any nonconstant h in V and a real affine
line in the cube on which h restricts to a nonconstant polynomial Q.
A contrary inclusion would give on its real segment
\[
                 \operatorname{sech}^2(P_i)Q(t)
                         =\sum_j\gamma_j\tanh Q_j(t).
\]
Real analyticity extends this identity along the entire real line.
The left side is unbounded, while the right side is bounded by
sum_j|gamma_j|. This contradiction proves (10).

If V_M contains a nonconstant polynomial, (9) and (10) exclude every
nonzero residual, completing this part of the theorem. Notice that the
lemma works for an arbitrary finite list, however large or dependent.

## 6. Constant-image and zero-image states

It remains to handle V_M contained in span{1}. Write
\[
               b_2^TM=v^T,\qquad
               z_i=v\cdot a_i,\qquad
               f_i=(E_2c)\phi(v\cdot a_i),
\tag{12}
\]
where v is a fixed coefficient vector, possibly zero. Assume a
positive-loss local minimum. If v is nonzero, (6) at any nonzero
residual gives E_2c=0, since phi'(v dot a_i)>0. If v=0 all predictions
are zero without this condition. In either case all lower-field
changes with the same c,M preserve zero predictions and r=-y.

We first prove E_2[b_2c]=0. Otherwise matrix stationarity at all
sufficiently nearby lower fields gives
\[
                   \sum_i\mu_i r_i
                       \phi'(v\cdot a_i)a_i=0.
\tag{13}
\]
The nonzero vector E_2[b_2c] has been cancelled from its outer product
with the vector in (13). Nearby equal-value fields are local minima,
which is why stationarity holds at all these fields.

Replace w by a bounded truncation within the local-minimum ball. Its
predictions remain zero and it remains a local minimum. Call the bounded
field w_b. For any fixed finite s in R2 take
w_t=(1-t)w_b+ts. The left side of (13) is real analytic at every real t:
on a bounded t interval the first tanh arguments are uniformly bounded,
and a small complex neighborhood avoids their poles and bounds the
integrands uniformly. Integration against bounded marks preserves
holomorphy, by Cauchy's formula and Fubini. The resulting finite moments
also have a small neighborhood avoiding poles of their outer phi'
functions. Thus the identity valid near t=0 extends to t=1.

Let a_0=E_1b_1, which is nonzero because the lower span contains 1.
At t=1, a_i=a_0 phi(s dot u_i). Setting kappa=v dot a_0, (13) becomes
\[
              \sum_i\mu_i r_i h_\kappa(s\cdot u_i)=0
                    \quad\hbox{for every }s,\qquad
 h_\kappa(t)=\phi(t)\phi'(\kappa\phi(t)).
\tag{14}
\]
These ridge functions are independent. Here is a proof including the
possible missing Taylor coefficients. The function h_kappa is odd,
bounded, real analytic on R, and h_kappa'(0)=1. Its Taylor series has
infinitely many nonzero odd coefficients: otherwise real analytic
continuation would make it a bounded nonconstant polynomial on R.
Choose any m nonzero odd coefficients and restrict s=te with the
nonzero, distinct-square projections from section 3. The resulting
matrix is a generalized Vandermonde matrix at distinct positive nodes.
It is invertible because a polynomial with at most m monomials has at
most m-1 distinct positive roots. To prove that last fact, divide by its
lowest monomial; its derivative has one fewer nonzero monomial, so
induction and Rolle's theorem give the bound, beginning with one
monomial. Singularity of the square evaluation matrix would contradict
this bound. Equation (14) therefore forces r=0, a contradiction.
This proves the claimed necessary condition E_2[b_2c]=0.

If v=0, the readout change c -> c+epsilon preserves every prediction
and local minimality for sufficiently small epsilon. Applying this
necessary condition before and after gives epsilon E_2b_2=0, impossible
because the upper span contains 1 and therefore E_2b_2 is nonzero.

If v is nonzero, E_2c=0 was already proved. Choose a nonconstant bounded
upper mark combination B=e^Tb_2 and put k=B-E_2B. Changing c to
c+epsilon k preserves its mean, all predictions, and local minimality.
The necessary condition before and after gives epsilon E_2[b_2k]=0,
contradicting
\[
                       e^TE_2[b_2k]=\operatorname{Var}(B)>0.
\]
This covers every constant or zero image and completes the theorem.

## 7. Attainment and all duplicate/antipodal cases

Zero loss is attainable for every finite set distinct modulo sign.
Choose s so that the numbers s dot u_i are nonzero with distinct
absolute values, and set w identically s. Let a_0=E_1b_1 and choose
an upper coefficient e with b_2^Te=X_{2,1}. With
\[
 M=e a_0^T/|a_0|^2,\qquad
 t_i=\phi(s\cdot u_i),
\]
the upper features are H_i=phi(t_i X_{2,1}). They are independent:
an almost-sure relation holds on (-1,1) by positive density and
continuity, and the odd Taylor/Vandermonde calculation of section 3
applies to the nonzero t_i with distinct squares. Thus the finite Gram
G_ij=E_2[H_iH_j] is positive definite. The bounded readout
c=sum_j (G^{-1}y)_j H_j gives f_i=y_i.

For arbitrary repeated or antipodal observations, group modulo sign.
Choose a representative x_g and write x_i=s_i x_g with s_i in {+1,-1}.
Define
\[
 p_g=\sum_{i\in g}\mu_i,\qquad
 \bar y_g=p_g^{-1}\sum_{i\in g}\mu_i s_i y_i,\qquad
 C=\sum_g\sum_{i\in g}\mu_i(s_i y_i-\bar y_g)^2.
\]
At every state the bias-free equations give f(-x)=-f(x). Expanding
the weighted squares within each group yields the exact identity
\[
              \mathcal L=C+\sum_g p_g(f(x_g)-\bar y_g)^2.
\tag{15}
\]
The theorem applies to the finite distinct-modulo-sign representatives
and their finite real labels. Hence every local minimum has loss C;
the preceding construction fits all group averages and attains C.
This floor is zero exactly when signed labels agree within every group.
There is no restriction on the finite number of groups.

## 8. What is and is not resolved

The result removes the old bounds m<=6 at p=2 and m<=10 at p=3,
including matrices of every rank and all current population states in
the stated physical L2 topology. It uses the whole canonical
dictionary at these orders. The same proof also covers p=1.

The critical improvement is the use of the current polynomial image
V_M. A lower moment-interiority theorem is unnecessary for this proof;
neither a relaxed model with independently trained sample moments nor
an unproved physical lifting is imported.

This does not by itself imply convergence from canonical initialization,
escape under a specified noisy algorithm, a basin-measure statement,
bounded parameters, a Lyapunov rate, or convergence at infinite sample
count. At other orders the complete initialized-word tail must be
examined before calling its upper image polynomial; the unrestricted
all-orders claim is not asserted here.

Status at first freeze: complete lead candidate, pending internal audit
against its complete argument and exact canonical source.

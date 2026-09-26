# An all-time single-sample certificate for the actual frozen-basis closure

This continues the theoretical assessment of this study's new dictionary.
It is a proof about the actual whole-middle replacement, with its positive
ridge filters. It is not a proof that its error decreases with derivative
order p. The explicitly defined projection defect below still needs an
order-dependent bound. No new training or other study input is used.

The mathematical and research skills, AGENTS.md and Part1 of the shared
workflow were read. Established inputs checked: global_nonlinear.md §1,
§9, C.4.7.9 parts2/5, and the current study's frozen factorization and p7
specification. The main global theorem in that chapter uses a positive
shifted-arctan activation, so its positive activation floor is NOT imported
for tanh. The tanh single-sample argument below proves its own lower bound.

## Statement and contract

There are two hidden tanh layers, one training pair (x,y), with
0<r=||x||<=1. The normalized input used by the network is x; test inputs u
range over ||u||<=r. This includes the corresponding input circle when d=2.
Use loss (f(x)-y)^2/2 and canonical block mobilities. The unhalved loss
only doubles physical time speed and leaves all suprema over t>=0 unchanged.

Finite vectors use <a,b>_n=a.T b/n and ||a||_n; matrix operator norms are
with respect to these normalized spaces, and matrix HS norm is ordinary
Frobenius norm. Population vectors use their typed L2 inner products,
matrices are bounded operators, and increments are Hilbert--Schmidt.
The statement and proof work in either setting on fixed spaces.
Write W0=W^(2)(0). Initial readout is exactly c0=W^(3)(0)=0. This is the
population initialization of the construction; it is NOT the small nonzero
readout in the executed finite-width runs. For the population construction
assume the Gaussian initialized bounded operator W0 of the established
source law and F(W^(1)(0)x) in L2, which holds for Gaussian first rows.

For an arbitrary order p, let Q1,Q2 be its frozen ridge filters. They are
positive self-adjoint contractions, with

Q_l v = B_l B_l.T v/n (finite),
Q_l v = sum_i b_li <b_li,v> (population).

For raw dictionary R_l and Gram G_l, Q_l=R_l(G_l+eta_p I)^(-1)R_l*,
where R_l* includes the normalized population pairing. The nonzero filter
eigenvalues are lambda/(lambda+eta_p), hence 0<=Q_l<=I. Define
B_p=Q2 W0 Q1. The exact middle is W=W0+K and the closure middle is
W_p=B_p+K_p, both with K(0)=K_p(0)=0. Their first weights agree initially.
Their readouts and both first layers train; no dense background is restored.

Let h(s,u)=tanh(W^(1)(s)u), H(s,u)=tanh(W(s)h(s,u)); use subscripts p
for the closure. At the training input set h=h(s,x), H=H(s,x),
delta=c*(1-H^2), and delta_p=c_p*(1-H_p^2).

The label-zero case is stationary in readout and predicts zero everywhere
for both models. Hence suppose Y=|y|>0, sigma=sign(y). Define initial
activation energies

q0=||H(0,x)||_2^2, q0p=||H_p(0,x)||_2^2, kappa=min(q0,q0p)>0,
S=Y/kappa, A=||W0||op, M=A+S^2/2,
L=2+2M+4S+8SM+4SM^2,
C=1+S(M+1), J=1+S^2(1+M^2).

Both q0 and q0p are initialization quantities, not assumptions about an
unknown trained kernel. If q0p=0 with c0=0, the closure is stationary and
cannot fit a nonzero label; the positive condition is necessary here.

On the closure's signed feature-flow segment 0<=s<=S define

a_p(s)=sup_(||u||<=r) ||(W0-B_p) h_p(s,u)||_2,
b_p(s)=||(W0*-B_p*) delta_p(s,x)||_2,
d_p(s)=||delta_p tensor h_p - (Q2 delta_p) tensor(Q1 h_p)||HS,
epsilon_p=sup_(0<=s<=S) [a_p(s)+b_p(s)+d_p(s)].                 (1)

These quantities use only initialization, the chosen dictionary and its
own finite feature-flow trajectory. They require no exact trained dense
trajectory, no future data, no fitted dense endpoint and no hidden forcing
in the closure. They are error-certificate quantities, not evolution inputs.
The operator W0 can be queried for the certificate; its storage/computation
cost is not claimed to be included in the compressed model's inference cost.
The defects are finite: a_p<=2A, b_p<=2AS and d_p<=2S, hence
epsilon_p<=2A(1+S)+2S. They are continuous on the stated compact segment;
for a_p use joint L2 continuity in s,u and compactness of the finite-
dimensional input ball. The crude bound proves finiteness, not smallness.

Then the genuine all-time, whole-input-ball prediction bound is

sup_(t>=0, ||u||<=r) |f(t,u)-f_p(t,u)|
 <= (1+J/kappa) [C (exp(L S)-1)+S] epsilon_p.                (2)

At the training input alone the right side may be replaced by its minimum
with Y, because both signed predictions remain in [0,Y]. All constants
are explicit initialization/label quantities. They can be extremely large.
This is a defect certificate for each p, not a proved decreasing function
of p, and it is not automatically a useful numerical error bar.

## 1. Exact feature flow and existence on its finite segment

Use s as an independent parameter, not physical time. The full equations
are

c_s=sigma H,
K_s=sigma delta tensor h,
W1_s=sigma [(1-h^2) W*delta] x.T.

The closure has the same readout and read-in equations with its own state,
and

(K_p)_s=sigma (Q2 delta_p) tensor(Q1 h_p).                  (3)

Equation(3) is the lifted canonical coefficient gradient of the actual
ridge basis, not an orthogonal-projection substitution. Put g=W1 x,
ell=1-tanh(g)^2 and alpha=r^2. Then g_s=sigma alpha ell W*delta.
The component of W1 orthogonal to x is fixed in each system.

Let F(z)=z/2+sinh(2z)/4, so F'(z)=cosh(z)^2=1/ell(z).
F is a bijection of R with inverse derivative at most1. With X=F(g),

X_s=sigma alpha W*delta.                                  (4)

The maps F^(-1) and tanh composed with F^(-1) are globally1-Lipschitz.
This removes the potentially unbounded product of a first-gate difference
with a backward field in the L2 comparison. It does not change the raw GF.

For every finite feature interval, |c_i(s)|<=s pointwise follows from
|H_i|<=1 and c0=0. The same holds for c_p. Thus

||delta||_2,||delta_p||_2<=s,
||K||HS,||K_p||HS<=s^2/2,
||W||op,||W_p||op<=A+s^2/2.                                (5)

Equation(4) also bounds the change in X by the integral of
alpha(A+s^2/2)s. On a short interval the integral map for (X,K,c)
is a contraction on continuous L2/HS curves in these bounds: the forward
maps are Lipschitz, and
||c phi'(z)-c' phi'(z')||_2<=||c-c'||_2+2S||z-z'||_2
when both readouts are bounded pointwise by S. Iterating the readout
integral always preserves its pointwise bound. Standard contraction
iteration follows directly from the geometric bound on successive
differences. Restarting finitely many such intervals, using(5), constructs
the unique feature curve on [0,S]. The same argument works for every
finite S. Pointwise absolute-continuity versions obtained by integrating
L2 derivatives justify the inverse-coordinate chain rule and recover the
raw equation. No analyticity or all-order Taylor expansion is required.

## 2. A nonvanishing training kernel from zero readout

At the training point let D multiply by phi'(z), E multiply by phi'(g).
Twice differentiating c in feature time gives

c_ss = D[||h||_2^2 I + alpha W E^2 W*]D c = T(s)c,

where T(s) is positive self-adjoint. For the closure,

(c_p)_ss = D_p[<h_p,Q1 h_p> Q2 + alpha W_p E_p^2 W_p*]D_p c_p.

Its bracket is also positive. These identities are valid L2 derivatives
on the bounded-readout curves: scalar gate differentiation is justified
by bounded gates and readout, or by dominated difference quotients. The
positive operators depend on the actual evolving states; no weights or
hidden features are frozen in this argument.

For R(s)=||c(s)||_2 and R>0,

R'' = (||c_s||_2^2-(R')^2+<c,T(s)c>)/R >=0.

The first two terms are nonnegative by Cauchy--Schwarz. Since c(0)=0 and
c_s(0)=sigma H0, R'(0+)=sqrt(q0)>0. Initially R>0, convexity implies
R'>=sqrt(q0), and hence R cannot return to zero. Therefore, for all s>=0,

||H(s,x)||_2=||c_s||_2>=R'>=sqrt(q0),
sigma f(s,x)=<c,c_s>=R R'>=q0 s.                          (6)

The identical conclusion holds with q0p for the closure. The full signed
prediction derivative is the canonical squared gradient norm, and the
closure derivative uses the positive filtered middle term:

sigma f_s=||H||_2^2+alpha||E W*delta||_2^2
                 +||delta||_2^2||h||_2^2 >=q0,
sigma (f_p)_s=||H_p||_2^2+alpha||E_p W_p*delta_p||_2^2
                 +<delta_p,Q2 delta_p><h_p,Q1 h_p> >=q0p.   (7)

Each derivative is at most J on [0,S] by(5). Thus each feature prediction
crosses Y at a unique point no later than S. The scalar physical clocks

s_t=Y-sigma f(s,x),
(s_p)_t=Y-sigma f_p(s_p,x),
s(0)=s_p(0)=0                                             (8)

remain strictly below their respective crossing points at finite time.
For example the deficit r=Y-sigma f satisfies r_t=-K(s(t))r,
K>=q0 and K bounded on [0,S], giving
0<r(t)<=Y exp(-q0 t). Thus the physical solution exists for all t,
s(infinity)<=Y/q0 and the total residual force is bounded. This proves
the lower-kernel condition rather than assuming it along training.

## 3. Compare the actual full and compressed feature curves

Let e(s)=||X-X_p||_2+||K-K_p||HS+||c-c_p||_2. Its initial value is zero;
the changed dense background is kept explicitly in(1), not hidden in e(0).
For a test input with ||u||<=r, the fixed perpendicular first-weight
components give

W1(s)u-W1_p(s)u=(<x,u>/r^2)(g(s)-g_p(s)).

The scalar factor has absolute value at most1. Therefore
||h(s,u)-h_p(s,u)||_2<=||X-X_p||_2. At the training point and uniformly
at those test inputs,

||z-z_p||_2<=M||X-X_p||_2+||K-K_p||HS+a_p(s),
||delta-delta_p||_2<=||c-c_p||_2+2S||z-z_p||_2.             (9)

Subtract(4), splitting W*delta-W_p*delta_p into the delta difference,
the increment difference and the initialized action difference on delta_p.
Use alpha<=1. This bounds the X-error derivative by

2SM^2||X-X_p|| +(2SM+S)||K-K_p|| +M||c-c_p||+2SM a_p+b_p.

Subtract the two matrix equations by first adding delta_p tensor h_p.
The resulting HS error derivative is bounded by

(S+2SM)||X-X_p||+2S||K-K_p||+||c-c_p||+2S a_p+d_p.

The readout error derivative is at most M||X-X_p||+||K-K_p||+a_p.
All norms here have the types used in e. Norms of differentiable Hilbert
curves are absolutely continuous; their upper derivatives satisfy these
bounds even when one difference is zero. Summing, and using the displayed
constant L (which dominates every coefficient), yields

e'(s)<=L e(s)+L[a_p(s)+b_p(s)+d_p(s)], e(0)=0.

Multiplication by exp(-Ls) and integration prove

sup_(s<=S)e(s)<=(exp(LS)-1) epsilon_p.

The same-clock prediction difference, including every declared test input,
is bounded by

||c-c_p||_2+S||z-z_p||_2 <= C e(s)+S a_p(s).

Write E_p=[C(exp(LS)-1)+S]epsilon_p for this uniform bound.

## 4. Return to the same physical time without an exp(constant*t) loss

The exact signed training feature-prediction F_train(s)=sigma f(s,x)
has derivative at least kappa on [0,S]. Subtract(8), and let d=s-s_p.
Monotonicity gives its upper absolute derivative

(|d|)'<=-kappa|d|+E_p,
|d(t)|<=E_p(1-exp(-kappa t))/kappa <=E_p/kappa.             (10)

For any declared test input the closure feature-prediction speed is at
most J: its readout term is at most1, its middle-velocity contribution
is at most S^2, and its first-weight contribution is at most M^2 S^2,
using alpha<=1, ||u||<=r<=1 and (5). Thus

|f(s(t),u)-f_p(s_p(t),u)|
 <=E_p+J|s(t)-s_p(t)| <=(1+J/kappa)E_p,

which is(2), uniformly for every t>=0 and every declared test input.

## What the proof establishes, and the missing p estimate

This is an all-time approximation theorem for each actual frozen-basis
closure with zero readout and nonzero initial training features. It applies
to the new dictionary's positive ridge; there is no unmentioned change to
orthogonal bases or restored dense background. It also controls passive
circle predictions, not merely eventual fitting of the single label.

It does not prove epsilon_p->0 or any explicit order rate. Proving such a
statement requires approximating initialized forward/reverse actions and
the rank-one update factors on this whole finite feature segment. The
complete word hierarchy in established C.4.7.9 has a separate density
proof; the derivative-only fixed-two-probe dictionary has no such proof.
Finite Taylor coefficient containment cannot supply that missing estimate
by itself, particularly after replacing W0 and applying ridge filters.

For the executed nonzero finite readout, the radial argument from zero is
not automatically applicable. A perturbation/global-tail argument is needed
to transfer this all-time certificate; finite-horizon convergence alone
does not establish that transfer. No population/width limit is exchanged
with t->infinity in this proof.

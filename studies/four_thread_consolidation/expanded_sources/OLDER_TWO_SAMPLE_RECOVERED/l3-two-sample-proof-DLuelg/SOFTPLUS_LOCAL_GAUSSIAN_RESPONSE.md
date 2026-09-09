# Short Gaussian response for a shifted-softplus reference law

Root draft, 2026-09-06. UNREVIEWED. This is a mesh/cap-uniform
response lemma for a precisely stipulated finite Gaussian law, under
explicit primal moment and time-regularity hypotheses. It is not a
global theorem or, by itself, a finite-width identification theorem.
The point of the hypotheses is to allow a separate finite-dimensional
primal estimate and fixed-program identification to discharge them.
Those bridges must be proved; they are not inferred from this lemma.

The activation is fixed throughout:

    phi(z)=1+e log(1+exp z),       e=1/10,       c=1/40.

Direct differentiation and log(1+exp z)<=log 2+|z| give

    1<=phi(z)<=2+e|z|,  0<phi'(z)<=e,  |phi''(z)|<=c.       (1)

All constants below are independent of both labels, the input angle,
the number of mesh points, and the three reference caps. The ultimately
chosen feature horizon is a single strictly positive constant. These
reference caps are analytical devices, not a change in the desired
uncut training dynamics.

## 1. The finite law and the exact claim

Let M>=1 be finite, Delta>0, s_k=k Delta, S=M Delta<=1/10. Both
sample labels y_a are in {-1,1}. Let C have diagonal one and
off-diagonal rho in [-1,1]. Start with a centered Gaussian pair G
of covariance C. For each cap R>=1, tau_R is smooth, odd, agrees
with the identity on [-R,R], and satisfies

    |tau_R(v)|<=min(|v|,2R),       0<=tau_R'(v)<=1.

Use three independently chosen cap sizes R_1,R_2,R_w. The law is

    Z^(1)_{ka}=G_a+(Delta/2) sum_(r<k,b) C_ab y_b delta^(1)_{rb},
    H^(1)_{ka}=phi(Z^(1)_{ka}),
    delta^(1)_{ka}=phi'(Z^(1)_{ka})tau_R1(q^(1)_{ka}),

    Z^(ell)_{ka}=xi^(ell)_{ka}
                   +sum_(r<k,b) A^(ell)_{ka,rb}delta^(ell)_{rb},
    H^(ell)_{ka}=phi(Z^(ell)_{ka}),                         ell=2,3,

    W^(4)_k=(Delta/2) sum_(r<k,b)y_b H^(3)_{rb},
    delta^(3)_{ka}=tau_Rw(W^(4)_k)phi'(Z^(3)_{ka}),

    q^(2)_{ka}=zeta^(2)_{ka}
                    +sum_(r<=k,b)B^(3)_{ka,rb}H^(2)_{rb},
    delta^(2)_{ka}=phi'(Z^(2)_{ka})tau_R2(q^(2)_{ka}),

    q^(1)_{ka}=zeta^(1)_{ka}
                    +sum_(r<=k,b)B^(2)_{ka,rb}H^(1)_{rb}.       (2)

The four entire centered Gaussian source groups are mutually independent
and independent of G. Each group retains its full time/sample covariance:

    E[xi^(ell)_{ka}xi^(ell)_{rb}]
        =E[H^(ell-1)_{ka}H^(ell-1)_{rb}],
    E[zeta^(ell-1)_{ka}zeta^(ell-1)_{rb}]
        =E[delta^(ell)_{ka}delta^(ell)_{rb}],              ell=2,3.

The expectations are in the respective neuron population. They are
uncentered input second moments, not covariances of centered features.
Singular source covariances are allowed. The deterministic coefficients
are selected causally by

    A^(ell)_{ka,rb}
       =E[partial H^(ell-1)_{ka}/partial zeta^(ell-1)_{rb}]
            +(Delta/2)y_b E[H^(ell-1)_{ka}H^(ell-1)_{rb}], r<k,

    B^(ell)_{ka,rb}
       =E[partial delta^(ell)_{ka}/partial xi^(ell)_{rb}]
            +(Delta/2)1_(r<k)y_b
                         E[delta^(ell)_{ka}delta^(ell)_{rb}], r<=k. (3)

All formal derivatives freeze previously chosen deterministic
coefficients and covariance parameters. Every source slot remains a
separate variable even when its variance is zero or it agrees almost
surely with a different slot. All sums over b include both samples.
At each time the selection order is A2, Z2, A3, Z3, delta3, B3,
q2, delta2, B2, q1; bottom fields and readout use past updates.

Assume this finite law is well defined, its displayed formal derivative
expectations exist, and it satisfies the following PRIMAL hypotheses:
for each sample and node,

    ||H^(1)_{ka}||_2<=23/10,
    ||H^(2)_{ka}||_2<=453/100,
    ||H^(3)_{ka}||_2<=7,
    ||delta^(3)_{ka}||_2<= (7/10)s_k,
    ||q^(2)_{ka}||_2<= (77/10)s_k,
    ||delta^(2)_{ka}||_2<= (77/100)s_k,                   (4)

and, for ell=1,2 and any pair of nodes,

    ||H^(ell)_{ka}-H^(ell)_{ra}||_2<=|s_k-s_r|.          (5)

Here ||.||_2 is the ordinary L2 norm on the relevant probability
space. No source-response estimate, independence of trained fields,
uncut population flow, energy identity, or higher moment is assumed
in (4)--(5). In particular these are logically independent premises,
not statements justified by the conclusion we now prove.

Claim. There are S_0 in (0,1/10] and positive finite constants
C_B,eta,C_E, independent of the choices above, such that S<=S_0
implies, for all k and r<k,

    |A^(2)_{ka,rb}|<=20 Delta/2,
    |A^(3)_{ka,rb}|<=60 Delta/2,

    max_a sum_(r<=k,b)|B^(ell)_{ka,rb}|<=C_B S<=1/2,
                                                        ell=2,3, (6)

and

    E exp(eta max_(k,a)|Z^(ell)_{ka}|^2)<=C_E,           ell=1,2,3,
    E exp(eta max_k |W^(4)_k/S|^2)<=C_E,
    E exp(eta |q^(j)_{ka}|^2)<=C_E,                    j=1,2.     (7)

The last bound is uniform at each node; it is NOT a supremum-in-time
bound on reverse queries. No such supremum is needed below. The same
statements hold for identity cuts if the finite law and (4)--(5) are
separately known for them. This is not yet a claim that identity cuts
are the limit of the reference laws.

## 2. An elementary Gaussian path bound

We give the concentration ingredient in full rather than invoke a
Gaussian-process theorem. Let X(t), 0<=t<=S, be a centered continuous
Gaussian process obtained by linear interpolation of a finite Gaussian
array. Suppose ||X(0)||_2<=v and

    ||X(t)-X(u)||_2<=D|t-u|.

The elementary scalar bound

    P{|N(0,sigma^2)|>sigma b}<=2 exp(-b^2/2), b>=0,      (8)

follows by applying Markov to exp(lambda X), whose expectation is
exp(lambda^2 sigma^2/2), and optimizing lambda for each of the two
tails. At sigma=0 the asserted bound remains true.

For each j>=1, compare every dyadic point iS/2^j with its parent
floor(i/2)S/2^(j-1). Each nonzero increment has standard deviation
at most DS/2^j. There are at most 2^j such increments. By (8), the
probability that any of them exceeds

    DS 2^(-j)(u+2 sqrt(j)+2)

in absolute value is at most

    2 exp(-u^2/2) exp((log 2-2)j-2),        u>=0.

Also |X(0)|<=v(u+1) except on an event of probability at most
2 exp(-u^2/2). Summing over j gives a failure probability at most
C_G exp(-u^2/2), with an absolute finite C_G. On the complementary
event the dyadic approximants from below to any t<S, starting at
zero at level zero, give by continuity

    |X(t)|<=v(u+1)+DS sum_(j>=1)2^(-j)(u+2sqrt(j)+2)
           <=(v+8DS)(u+1).                               (9)

The last inequality uses sum 2^(-j)=1 and
sum sqrt(j)2^(-j)<=sum j2^(-j)=2. Continuity extends the same
bound to S. This countable union proof uses no independence among
increments. It applies to singular Gaussian arrays as well.

For v<=7, D<=1 and S<=1/10, v+8DS<=8. Thus the maximum N
over TWO such sample paths obeys

    P{N>8(u+1)}<=2C_G exp(-u^2/2).                     (10)

For t>=16, take u=t/8-1>=t/16. The resulting tail bound and
integration of the distribution function show

    E exp(N^2/2048)<=C_0<infinity                       (11)

for an absolute C_0. Explicitly, for nonnegative X and alpha>0,
Tonelli applied to exp(alpha X^2)=1+integral_0^X
2alpha t exp(alpha t^2)dt gives

    E exp(alpha X^2)
       =1+integral_0^infinity 2alpha t exp(alpha t^2)P{X>t}dt.

Use (10) on t>=16, where the exponent is at most
t^2/2048-t^2/512<0; the bounded initial interval causes no problem.

To apply this to xi2 and xi3, (4) supplies their initial variances
and (5) supplies the covariance increment metric at nodes. The linear
interpolant has the same Lipschitz constant in L2: on each mesh
interval its L2 speed is at most one; splitting any interval at nodes
and using the triangle inequality proves the assertion globally.
The Gaussian interpolant is continuous because it has finitely many
linear pieces. Consequently both forward source maxima N_2,N_3
satisfy (11).

The reverse sources need a different and simpler estimate. Their
standard deviations are at most one by (4) and S<=1/10. Put

    V_j=(Delta/S)sum_(r<M) max_a |zeta^(j)_{ra}|, j=1,2.

Convexity of x -> exp(alpha x^2) for x>=0 and time Jensen give

    E exp(alpha V_j^2)
      <=(Delta/S)sum_(r<M) E exp(alpha max_a|zeta^(j)_{ra}|^2)
      <=2(1-2alpha)^(-1/2),                 0<alpha<1/2. (12)

The last step is the scalar Gaussian integral and the bound of a
maximum by the sum of the two exponentials. Time independence is
neither asserted nor used. The root maximum G_* has the same bound.

Set

    T=1+G_*+N_2+N_3+V_1+V_2.

There are universal eta_0>0,C_1<infinity such that

    E exp(eta_0 T^2)<=C_1.                              (13)

Indeed T^2<=6(1+G_*^2+N_2^2+N_3^2+V_1^2+V_2^2);
convexity then bounds exp(eta_0 T^2) by the average of the six
exponentials with coefficients 36 eta_0. Choose
36 eta_0<=1/2048 and use (11)--(12). There is no factorization
of different populations or of evolved random variables in (13).

## 3. Path envelopes under a coefficient bootstrap

Write U_k and V_k for the total absolute B2 and B3 rows respectively;
these V_k are deterministic row norms, distinct from V_j in (12),
which is used only in this section inside T. Suppose past B rows are
at most one and already selected forward coefficients satisfy their
respective bounds in (6). We record envelopes valid up to the current
time whenever their recursions only use those selected coefficients.

Let X_ell(k)=max_(r<=k,a)|Z^(ell)_{ra}|. The first equation in (2)
and |C_ab|<=1 imply

    X_1(k)<=G_*+e Delta sum_(r<k)
                        [max_a|zeta^(1)_{ra}|+2+e X_1(r)].

For nonnegative b_r, the inequality x_k<=d+sum_(r<k)b_r x_r
implies x_k<=d product_(r<k)(1+b_r)<=d exp(sum b_r), by
induction. If d is a nondecreasing function of k one may use its
value at the terminal index throughout. Applying this fact gives

    X_1(k)<=exp(e^2 S)[G_*+eS(V_1+2)].                  (14)

For the middle layer use |delta2|<=e|q2|, the A2 bound and the
past B3 bound. Summing two update samples cancels the denominator
two in A2, and gives

    X_2(k)<=N_2+20e Delta sum_(r<k)
                         [max_a|zeta^(2)_{ra}|+2+e X_2(r)]
           <=exp(20e^2S)[N_2+20eS(V_2+2)].             (15)

The top layer uses no reverse coefficient at its own time. Its
readout formula implies |W^(4)_r|<=s_r[2+e X_3(r)]. Hence

    X_3(k)<=N_3+60e Delta sum_(r<k)s_r[2+e X_3(r)]
           <=exp(60e^2S^2)[N_3+120eS^2].              (16)

The deliberately loose second inequality uses s_r<=S and
Delta sum_(r<k)s_r<=S^2; it is valid also on a one-step mesh.
Set K_3=2+e X_3(M), when the coefficient bootstrap holds through M.
For a partial induction use the same right-hand side of (16), with
the full source maximum N_3, as its upper bound. In either case

    X_ell(k)<=C_2 T,      |W^(4)_k|<=s_k C_2 T,
    K_3<=C_2 T,                                           (17)

with one fixed finite C_2 for S<=1/10. The constant depends only on
20,60,e and the fixed horizon ceiling, not on a row bound yet to be
proved at the current time. All path envelopes have Gaussian-square
moments by (13).

At past times, q1 and q2 are bounded pointwise by their own Gaussian
source plus 2+e X_1 or 2+e X_2. It follows from (14)--(15) that
each of the two nonnegative quantities

    L_1=Delta sum_(r<k)[c max_a|q^(1)_{ra}|+e^2],
    L_2=20 Delta sum_(r<k)[c max_a|q^(2)_{ra}|+e^2]

is at most C_3 S T for a fixed C_3. Thus, uniformly over partial
inductions and S<=1/10,

    E exp(p L_j)<=1+D_p S,           j=1,2, p>=1,       (18)

where each fixed p has a finite D_p. To justify the convergence to
one, use exp(x)-1<=x exp(x), Cauchy--Schwarz and (13):

    E[exp(pC_3ST)-1]
      <=pC_3S (E T^2)^(1/2)
                  (E exp(2pC_3ST))^(1/2).

The final expectation is uniformly finite since lambda T <=
eta_0 T^2/2+lambda^2/(2eta_0). This proof is stronger than merely
bounding the moment by a fixed prefactor which would not approach one.
Choose S_a>0, no larger than 1/10, so that (18) implies

    E exp(L_1)<=2,       ||exp(L_2)||_2<=2.              (19)

No B-row constant was chosen using (19); only the threshold one and
the fixed A bounds 20 and 60 entered its derivation.

## 4. Forward response induction

At time zero W4 and delta3 are identically zero formal functions,
so B3_00=0. Then zeta2_0 is zero on the attained law, but the formal
delta2_0=phi'(xi2_0)tau_R2(zeta2_0) is retained. Its derivative in
xi2_0 vanishes on that law, giving B2_00=0. Its derivative in its
own zeta2_0 slot is phi'(xi2_0), not zero. The analogous bottom slot
is also retained. Thus U_0=V_0=0 without discarding formal variables.

Assume U_r,V_r<=1 for r<k and the previous forward estimates hold.
Bottom fields at k depend only on these past queries. For one fixed
source zeta1_(sb), a variation d satisfies

    |d delta1_ra|<=c|q1_ra||dZ1_ra|+e|dq1_ra|,
    |dq1_ra|<=1_((r,a)=(s,b))
                +e sum_(v<=r,j)|B2_ra,vj||dZ1_vj|.

The first direct injection into a bottom coordinate has size at most
Delta e/2. The row sum over the two bottom update samples is at
most one after dividing by two and multiplying by |C|. Applying
the product induction just proved and then the output feature gate
gives

    |partial H1_ka/partial zeta1_sb|
        <=(Delta e^2/2) exp(L_1).                       (20)

Consequently (3), (4) and (19) show

    |A2_ka,sb|<= (Delta/2)[(23/10)^2+2e^2]
                       <20 Delta/2.                   (21)

This proves the current A2 bound before current middle values are
used. The previously derived envelope (15) is therefore available
up to time k.

For a variation of middle forward sources, let

    R_j=max_a sum_(s<=j,b)|partial Z2_ja/partial xi2_sb|.

Its direct injection row has sum exactly one, not a number of
time/sample slots. Holding all coefficients fixed,

    |d delta2_ra|<=c|q2_ra||dZ2_ra|+e|dq2_ra|,
    |dq2_ra|<=e sum_(v<=r,b)|B3_ra,vb||dZ2_vb|.

Using (21) and the past B3 row bound in the strictly past forward
recursion gives max_(j<=k)R_j<=exp(L_2). For one reverse source
zeta2_sb the direct preactivation injection is at most
20 Delta e/2, and the feature gate adds e. Hence

    |partial H2_ka/partial zeta2_sb|
        <=(20 Delta e^2/2)exp(L_2).                     (22)

Equations (3), (4), (19), and E exp(L_2)<=||exp(L_2)||_2<=2 give

    |A3_ka,sb|<=(Delta/2)[(453/100)^2+40e^2]
                       <60 Delta/2.                   (23)

The A3 estimate and (16) now supply the top envelope at time k.
Neither (21) nor (23) used current B3 or B2.

## 5. Current top response, then current middle response

Let T_j be the maximum total xi3-source derivative row of Z3 at
time j. In this section K denotes the full-source upper bound for
K_3 supplied by (16)--(17), valid throughout the partial induction.
Differentiating the exact readout update, the readout cut, and the
gate gives

    max_a sum_(s<=j,b)|partial delta3_ja/partial xi3_sb|
      <= e^2 Delta sum_(r<j)T_r+c|W4_j|T_j
      <= S(e^2+cK) max_(r<=j)T_r.                      (24)

Both terms are necessary; in particular the unbounded readout has
not been replaced by a deterministic constant. The derivative of its
cut is bounded by one and its cut value by its absolute value.
The forward recursion with (23) is strictly historical. Product
induction in (24) yields

    max_(j<=k)T_j<=exp[60 S^2(e^2+cK)].                 (25)

The Gaussian-square moment of K implies that

    D_0=sup E[(e^2+cK)exp(60S^2(e^2+cK))]<infinity,     (26)

where the supremum ranges over all partial inductions with S<=1/10.
For example use K<=C_2T, (13), and complete the square as in (18).
This defines a deterministic finite constant without using current
backward coefficients.

The learned covariance row in B3 is at most

    Delta sum_(r<k) (7S/10)^2 <= (49/100)S^3

by Cauchy--Schwarz and (4). Thus, BEFORE using current B2,

    V_k<=D_0S+(49/100)S^3<=C_V S,
    C_V=D_0+49/10000.                                  (27)

Now consider current delta2. Its current q2 includes current B3,
which is already bounded by (27). Its full derivative row is at most

    [c|q2_ka|+e^2 V_k] exp(L_2).                       (28)

Indeed the same total Z2-source row bound exp(L_2) includes every
past and current forward slot; summing the q2 returns against it
uses the entire current B3 row. There is no direct zeta injection
when differentiating in xi2. Cauchy--Schwarz, (4), and (19) bound
the expectation of (28) by

    2[c(77/10)S+e^2 C_V S].

The learned B2 row is at most (77/100)^2 S^3. We conclude

    U_k<=C_U S,
    C_U=2[(77/10)c+e^2 C_V]+(77/100)^2/100.            (29)

Put C_B=max(C_U,C_V) and

    S_0=min(S_a,1/10,1/(2C_B)).                         (30)

All constants are finite and positive, so S_0>0. Equations
(27)--(30) improve both bootstrap row bounds from one to at most
one half. This proves the induction for every k and establishes (6).
There is no continuity-in-mesh bootstrap assumption: this is a finite
causal induction, valid even when M=1 and Delta=S.

## 6. Gaussian tails and exact limitations

Having closed the induction, (14)--(17) hold on the full interval.
Their Gaussian-square moments prove the first two lines of (7),
after decreasing eta and increasing C_E if necessary. At any node,
the now-proved B rows imply

    |q1_ka|<=|zeta1_ka|+2+e X_1(M),
    |q2_ka|<=|zeta2_ka|+2+e X_2(M).

Each displayed Gaussian source has variance at most one. The
inequality (x+y+z)^2<=3(x^2+y^2+z^2) and convexity, exactly as
in (13), give the final line of (7) without any independence between
a response shift and its source. Enlarge constants uniformly over
the two samples and layers.

In particular, for Q equal to either reverse query at a node or W4
at a node, there are finite C_4,c_4>0 such that

    E[|Q-tau_R(Q)|^2]<=C_4 exp(-c_4 R^2), R>=1.        (31)

Indeed oddness, monotonicity, and agreement with the identity show
|Q-tau_R(Q)|<=|Q|1_(|Q|>R). For x>=0,
x^2 exp(-eta x^2/2) is bounded; multiply this bound by
exp(eta Q^2)exp(-eta R^2/2) and use (7). The constants may absorb
S<=1/10 when the readout estimate was stated for W4/S.

What has been proved is a local response and tail implication for
the full trained-reference scalar law, not a tail assertion for an
arbitrary L2-bounded operator. The proof explicitly retains both
learned forward/transpose memories and all zero-variance formal slots.
It gives no whole-space L-infinity-to-Lp estimate for a Gaussian action.

Before claiming a canonical local population theorem, one must still
prove fixed-program identification for these unbounded-feature maps,
derive (4)--(5) from the actual finite reference dynamics, construct
their common population operators and adjoints, pass the mesh limit,
and use a valid three-cut comparison to remove the caps. Raw GD,
physical-time comparison, observables and nontriviality are additional
obligations. Even discharging every one of those LOCAL obligations
would not prove the opposite-label all-finite-physical-time theorem.

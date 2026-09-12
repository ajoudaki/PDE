# Check of a readout-linearity and task-variance sign argument

Root, 2026-09-12. **Outcome: the proposed general sign implication is false.**
Training both a readout and a tanh feature does not, by itself, make feature
adaptation beneficial in expectation over varying task components. An exact
two-parameter identity shows why. The same identity gives a counterexample
to that implication with the unchanged G target box on the full circle,
exact anchor constraints, the complete projected tangent comparator, and a
common metric and clock.

The model below is deliberately an auxiliary finite-dimensional prediction
map. It is **not** the prescribed Gaussian two-hidden-layer network or its
reached reference. This is a check of a proposed inference, not a failure
theorem for the E₀ family on the actual network. No task family in the E₀
contract is changed. No training or numerical experiment is performed.

## 1. Exact scalar identity, including the trained readout

Consider f=a tanh w with Euclidean parameter metric and loss (f-q)².
Both a and w train by actual gradient flow:

    a'=-2(f-q)tanh w,
    w'=-2(f-q)a sech²w.

Start at a(0)=sqrt(I)>0, w(0)=0. Direct differentiation gives

    a²-sinh²w=I,
    f'=-2 K(w)(f-q),
    K(w)=tanh²w+a²sech⁴w=1+(I-1)sech⁴w.                (V1)

The invariant follows because
sinh w cosh w sech²w=tanh w. Since a²>=I>0, the initial positive sign of
a persists. The kernel is the sum of the squares of **both** parameter
gradients, including the readout gradient. At the initial state the full
tangent kernel is I and the frozen residual is -q exp(-2It).

The actual residual is exactly

    f(t)-q=-q exp(-2 integral_0^t K(w(s))ds).              (V2)

Consequently f has the sign of q for every t>0 when q is nonzero, and
0<|f(t)|<|q|. Its sign also equals the sign of w. If I>1, then
1<=K(w)<=I, with K(w(t))<I for every t>0 and q!=0. The nonlinear learner
therefore has strictly *larger* risk than the full frozen learner at every
positive matched time. If 0<I<1 the strict inequality reverses. If I=1,
the two prediction evolutions coincide exactly, despite parameter motion.

The sign thus depends on a balance at the reference, rather than on
readout linearity or nonzero feature motion. No conclusion about the
corresponding task-weighted balance of the actual E₀ reference follows.

## 2. The unchanged target box in an auxiliary anchor-preserving model

Use uniform normalized circle measure and the original unperturbed G slice:

    q=q0+sum_{i=1}^4 c_i phi_i,
    q0=cos³(alpha)-sin³(alpha), h=sin²(2alpha),
    (phi_1,phi_2,phi_3,phi_4)
      =h(cos alpha,sin alpha,cos 3alpha,sin 3alpha),
    c_1,c_2 in [R/16,R/8], c_3,c_4 in [R/48,R/24],
    0<R<=1/8.                                            (V3)

These target ranges are taken unchanged from ROUTE_GEOMETRY.md. The
calculation below uses only this explicitly stated slice, not its density
or target-perturbation extensions. It assumes no target chosen from a
trained prediction.

The Gram matrix Gamma of the four phi_i has diagonal 3/16, cross entries
Gamma_13=-1/8, Gamma_24=1/8, and other off-diagonal entries zero. For
example h²=(3-4cos(4alpha)+cos(8alpha))/8 gives all entries by direct
integration. Thus lambda_min(Gamma)=1/16 and lambda_max(Gamma)=5/16.
Define the fixed orthonormal dictionary psi=Gamma^(-1/2)phi. This choice
depends only on the ordinary target components and the common circle
metric, not on task outcomes or a trained state. Write

    q-q0=sum_j y_j psi_j,      y=Gamma^(1/2)c.

In particular

    ||y||²=c^T Gamma c >=5R²/9216,
    ||y||=||q-q0||_2 <=sum_i c_i <=R/3<1.                 (V4)

Each psi_j vanishes at both anchors because every phi_i does.

Now define the auxiliary prediction map

    f_theta(alpha)=z_1 cos³(alpha)+z_2 sin³(alpha)
                   +sum_{j=1}^4 a_j tanh(w_j) psi_j(alpha).

Use the Euclidean metric on all ten parameters. Its reference is
z_1=1, z_2=-1, a_j=sqrt(2), w_j=0, so f_*=q0. The two anchor gradients
are exactly the z-coordinate unit vectors. Their Gram is the identity;
the full anchor-preserving projection drops precisely the two z directions.
All a and w directions remain. Thus the constrained actual flow holds the
anchors fixed and has four independent copies of (V1), each with I=2 and
target y_j, since the psi_j are orthonormal. The complete frozen model has
four kernels equal to 2. Both use unhalved squared loss and the same clock.

There is no readout-only substitution. A readout derivative happens to
vanish at w_j=0, but all raw parameter directions have been included in the
projection and in the frozen kernel. This auxiliary reference is explicitly
specified; it is not asserted to arise from E₀'s Gaussian initialization.

## 3. A uniform finite adverse comparison on that auxiliary model

For I=2, the invariant also implies sinh²w<=f². Indeed, writing
u=sinh²w, one has f²=(2+u)u/(1+u)>=u. Therefore

    a²=2+sinh²w<=2+y_j²<=3,
    tanh²w=f²/a²>=f²/3,
    2-K(w)=2tanh²w-tanh⁴w>=tanh²w.

Since K>=1, (V2) gives |f(t)|>=|y_j|(1-exp(-2t)). Put

    J(T)=integral_0^T (1-exp(-2t))²dt
        =T-(1-exp(-2T))+(1-exp(-4T))/4 >0  (T>0).

It follows that integral_0^T(2-K)dt>=y_j² J(T)/3. The exact residual
formula and exp(x)-1>=x for x>=0 yield

    (f_j(T)-y_j)²-y_j² exp(-8T)
       >=(4/3)y_j^4 exp(-8T) J(T).

Summing, using sum_j y_j^4>=||y||^4/4, and then (V4), proves

    E_q(f_nl(T))-E_q(f_fr(T))
       >= [25R^4/254803968] exp(-8T) J(T)>0               (V5)

for every member of (V3) and every T>0. Thus even averaging over any
probability distribution on all four independently varying original
coefficients cannot create the proposed generic positive adaptation sign.
No favorable sample or continuity enlargement is used in this check.

Global existence used here is elementary: (V2) bounds |f| by |y_j|, the
invariant then bounds |w| and a, and the smooth finite-dimensional vector
field continues on that bounded set. All equations hold at finite time,
without a formal time jet or an assumed Taylor radius.

## 4. Consequence and scope

This falsifies the inference that readout linearity, full nonlinear feature
training, exact anchors, and independent active target components force a
favorable variance-averaged risk comparison. In a tanh model even the scalar
factor can increase, decrease or remain exactly constant depending on the
reference balance. The construction does not prove any sign of the actual
E₀ contractions or rule out an actual-neural structural theorem.

In particular, (V5) is not an E₀ counterexample: the prediction map, raw
fields, initialization and reference formation are different. It isolates
why the proposed general averaging argument cannot replace a signed
calculation at the genuine reference. It supplies no component advantage
beyond scalar gain and no sampling or finite-Gaussian transfer claim.

Proof inputs: the explicit target slice (V3) from ROUTE_GEOMETRY.md, SHA256
e452735f683a6f8c3e4e895949dbd8aa912f470bbdeb475bf676bce4a10b9c04;
the rest is the self-contained calculation above. Root checked the two
parameter derivatives, invariant, kernel simplification, exact residual
formula, circle Gram, coefficient bounds, anchor projection and finite risk
bound directly. No external theorem or experiment is used. Internal check
status is separate from the claim and promotion status.

# Approximate handoff and the residual generator at interpolation

Root continuation after the independent routes were frozen, 2026-09-30.
Dependencies: the complete `TERMINAL_SCALAR_THEOREM.md` and its exact q=1
equations. This note is a conditional extension, not an initialization-only
compression construction. It supplies the error budget that any such
construction would have to meet at its transition to the terminal model.

## 1. Imperfect aggregate data are enough

Use all hypotheses and notation of the terminal theorem. In particular the
actual handoff state has residual r_0, R=||r_0||, coefficients C_0,b_0,
Euclidean contraction margin lambda_0>0, and tube constants H,J. Suppose a
finite earlier calculation instead supplies tilde r_0, tilde C, tilde b,
and optionally tilde tau_0, with certified errors

    ||tilde r_0-r_0|| <= e_0,
    ||tilde C-C_0||_op+||tilde b-b_0|| <= delta < lambda_0,
    |tilde tau_0-tau_0| <= e_tau.

Run only the scalar system

    tilde rdot = -tilde C tilde r + ||tilde r|| tilde b,
    tilde taudot = ||tilde r||/sqrt(m),
    tilde L = ||tilde r||^2/m.

Set R_+=R+e_0 and lambda_-=lambda_0-delta>0. This finite evaluator has
the same storage and operation counts as the exact-coefficient terminal
model. Its own contraction margin is at least lambda_-.

**Proposition.** At equal physical times, for every t>=0,

    ||tilde r(t)|| <= R_+ exp(-lambda_- t),

    sup_t ||r(t)-tilde r(t)||
      <= e_0 + (JH/lambda_0^2) R^2 + delta R_+/lambda_0,          (1)

    sup_t |L(t)-tilde L(t)|
      <= (2R+e_0)/m
           [e_0+(JH/lambda_0^2)R^2+delta R_+/lambda_0],          (2)

    sup_t |tau(t)-tilde tau(t)|
      <= e_tau + (1/sqrt(m))
           [e_0/lambda_0+4JH R^2/lambda_0^3
                  +delta R_+/(lambda_0 lambda_-) ].             (3)

All these statements concern the actual q=1 target from its handoff, with
its finite-tube hypotheses checked. They do not require an accurate
reconstruction of the neuron state from tilde C,tilde b,tilde r_0.

**Proof.** Write T(u)=-C_0u+||u||b_0 and
tilde T(u)=-tilde C u+||u||tilde b. The norm of their difference is at
most delta||u||. Also

    (u-v)^T[tilde T(u)-tilde T(v)]
       <= -(lambda_0-delta)||u-v||^2,

by the same reverse-triangle estimate as for T. Thus tilde r is global,
has the stated exponential bound, and stops at zero.

The full residual satisfies rdot=T(r)+E, with the terminal proof's bound

    ||E(t)|| <= (2JH/lambda_0)R^2 exp(-lambda_0 t/2).

For e(t)=||r(t)-tilde r(t)||, contraction of T gives the upper norm
derivative inequality

    D^+ e <= -lambda_0 e + ||E(t)|| + delta||tilde r(t)||.

Its integral estimate is

    e(t) <= e_0 exp(-lambda_0 t)
       +(4JH/lambda_0^2)R^2
             [exp(-lambda_0 t/2)-exp(-lambda_0 t)]
       +delta R_+ integral_0^t
             exp[-lambda_0(t-u)]exp(-lambda_- u)du.             (4)

This remains valid when delta=0 without dividing by delta. The middle
bracket is at most 1/4. Bounding exp(-lambda_- u) by one bounds the
last term by delta R_+/lambda_0, proving (1). Both residual norms are
bounded by R and R_+, respectively, so their sum is at most 2R+e_0;
factoring the difference of squared norms proves (2).

Integrating (4) over t>=0 gives

    integral_0^infty e(t)dt
      <= e_0/lambda_0+4JH R^2/lambda_0^3
                         +delta R_+/(lambda_0 lambda_-).

For the last term, the nonnegative double integral separates into the
two exponential integrals after writing t=u+v. The norm is 1-Lipschitz,
and the clocks integrate it divided by sqrt(m). This proves (3).

## 2. What precision must the earlier scalar system deliver?

For fixed tube constants and small R, taking

    e_0 = O(R^2),       delta = O(R)

retains the O(R^3) all-time terminal loss error. It also retains O(R^2)
clock error if e_tau=O(R^2). Thus a target terminal loss tolerance epsilon
allows the scaling

    R = O(epsilon^(1/3)),
    residual initialization error = O(epsilon^(2/3)),
    response coefficient error = O(epsilon^(1/3)),               (5)

with sufficiently small constants. Coefficients need substantially less
absolute precision than the target loss. The full earlier loss curve still
needs its requested accuracy; (5) is only a transition budget.

Conversely, an uncontrolled error in a terminal decay coefficient can
produce order R^2 loss error even though both scalar systems fit and stop.
The one-dimensional example in the terminal theorem proves this. Terminal
stability is an error-propagation mechanism, not a substitute for accurate
coefficients.

If only an approximate margin is available, then

    tilde lambda := lambda_min(sym tilde C)-||tilde b||

satisfies |tilde lambda-lambda_0|<=delta. This follows by bounding the
quadratic form of sym(tilde C-C_0) on unit vectors and using the reverse
triangle inequality for b. Hence tilde lambda>delta certifies a positive
exact margin. Bounds on the full tube constants and the true handoff
residual are still required; an approximate positive matrix by itself is
not the full certificate.

## 3. Why the leading residual model need not be a linear kernel

At an interpolating full state X_*, the coefficient functions C(X),b(X)
are smooth even though the feedback norm is not. Holding that state fixed,
the first-degree homogeneous residual map is

    T_*(u)=-C(X_*)u+||u||b(X_*).                                (6)

If b(X_*) is nonzero, this map has no Frechet derivative at u=0. Indeed
T_*(epsilon u)/epsilon=T_*(u) for epsilon>0. A derivative would therefore
have to equal T_* in every direction, but

    T_*(u)+T_*(-u)=2||u||b(X_*)

does not vanish. A linear derivative cannot have that property. This
statement concerns the frozen residual map on R^m; it does not assume that
every residual direction is attainable by nearby network states.

The source of this nonlinearity is exactly the activity-clock update of
the stored key. At interpolation, the residual is zero but an accumulated
value and a current-feature/key gap can remain in formula (3) of the
terminal theorem. Therefore the coefficient of ||r|| need not be zero as
an algebraic identity. No assertion about its typical reached endpoint
value is made here.

Equation (6) is nevertheless globally Lipschitz and, under the stated
margin, strictly contractive. It is therefore an appropriate finite
terminal model even when a linearization in residual coordinates is not.
This is a concrete difference between residual-zero stopping and a
positive frozen-kernel approximation.

## 4. The remaining initialization problem is not removed

The handoff proposition allows approximate aggregate inputs without storing
the hidden populations afterwards. It supplies no algorithm to obtain
those inputs from initialization within the desired budget. The following
are still separate proof obligations:

1. A finite early scalar evaluator with a quantified source error that
   remains valid under its own feedback.
2. An initialized trajectory that reaches a certified terminal region,
   or another rigorously controlled terminal regime.
3. A width-uniform source rate, stable coefficient construction, and
   total storage o(epsilon^-2), including frozen coefficients.

Running the original dynamics until the handoff and then discarding it
does not satisfy the complete task. No such end-to-end claim is attached
to this proposition.

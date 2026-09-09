# Actual material Hessian: the proposed Schwarzian bound is false

Status: exact finite-width identities and an explicit counterexample to
an upper bound for `B' - kappa B^2`, for every fixed real kappa, using
only bounded hidden operator norms and bounded readout RMS. The same
family also rules out a lower bound. This concerns the full actual
canonical parameter field; it does not disprove a bound restricted to
typical prescribed-Gaussian trajectories, nor the open population
theorem. The state construction was supplied by the parent resolver;
the exact material derivative and Rayleigh evaluations below audit it.

## 1. Complete material derivative in the actual coordinates

Use precisely the coordinates and feature-time field of
`ACTUAL_HIDDEN_GRAPH_VOLUME.md`:

    x=(z1,sqrt(n)W2,sqrt(n)W3),   c=W4,
    F(x,c)=c^T h3(x),   b=grad F=(J^T c,h3),
    J=D_x h3,   A=D_x^2 F,   B=Db=[A J^T; J 0].

All primes below are material derivatives along this full field. Write
`D_l=diag(phi'(z_l))`, with `phi=arctan`, and retain

    delta3=D3 c,   q2=W3^T delta3,
    delta2=D2 q2,  q1=W2^T delta2,   delta1=D1 q1.

The exact weight and preactivation velocities are

    W2'=delta2 h1^T/n,    W3'=delta3 h2^T/n,    c'=h3,
    nu1=z1'=delta1,
    nu2=z2'=delta2 ||h1||^2/n + W2 D1 nu1,
    nu3=z3'=delta3 ||h2||^2/n + W3 D2 nu2.

Consequently, with all products inside `diag` coordinatewise,

    D_l'=diag(phi''(z_l) nu_l),
    delta3'=D3' c+D3 h3,
    q2'=(W3')^T delta3+W3^T delta3',
    delta2'=D2' q2+D2 q2',
    q1'=(W2')^T delta2+W2^T delta2'.                 (1)

For a fixed hidden tangent `u=(u1,E2,E3)`, define

    T1 u=u1,
    T2 u=E2 h1/sqrt(n)+W2 D1 u1,
    T3 u=E3 h2/sqrt(n)+W3 D2 T2 u,
    S2 u=E2^T delta2/sqrt(n),
    S3 u=E3^T delta3/sqrt(n).

The derivatives of these operators, evaluated on the same fixed `u`,
are exactly

    T1'=0,
    T2' u=E2 D1 nu1/sqrt(n)+W2' D1 u1+W2 D1' u1,
    T3' u=E3 D2 nu2/sqrt(n)+W3' D2 T2 u
                         +W3 D2' T2 u+W3 D2 T2' u,
    S2' u=E2^T delta2'/sqrt(n),
    S3' u=E3^T delta3'/sqrt(n),
    J'=D3' T3+D3 T3'.                               (2)

Put

    M1=diag(phi''(z1) q1),
    M2=diag(phi''(z2) q2),
    M3=diag(phi''(z3) c).

Their full derivatives are

    M1'=diag(phi'''(z1) nu1 q1+phi''(z1) q1'),
    M2'=diag(phi'''(z2) nu2 q2+phi''(z2) q2'),
    M3'=diag(phi'''(z3) nu3 c+phi''(z3) h3).          (3)

For `sym K=K+K^T`, direct differentiation of the complete Hessian gives

    A'=sum_(l=1)^3 [ (T_l')^T M_l T_l
                    +T_l^T M_l' T_l+T_l^T M_l T_l' ]
       +sym[ (S2')^T D1 T1+S2^T D1' T1 ]
       +sym[ (S3')^T D2 T2+S3^T D2' T2+S3^T D2 T2' ],

    B'=[A' (J')^T; J' 0]=D^3 F[b].                 (4)

Equations (1)-(4) include both trained matrices, all differentiation
through their transposes, readout training, and all mixed Hessian terms.
No backward query has been frozen. For a full tangent `U=(u,v)`, they give

    U^T(B'-kappa B^2)U
       =u^T A' u+2v^T J' u
          -kappa (||Au+J^T v||^2+||Ju||^2).         (5)

## 2. Explicit bounded-primal canonical state

Take any even width `n>=2`. Let `1` be the all-ones vector, let `e` be a
unit vector with `n/2` entries `1/sqrt(n)` and `n/2` entries
`-1/sqrt(n)`, and let `e1,e2` be the first two coordinate vectors. Put

    a=pi/4,   m=a^2<1,
    v=e1-2e2,   w=e1+e2,
    z1=1,   W2=2 w e^T,   W3=1 v^T/sqrt(n),   c=1.  (6)

This is an actual state of the stated three-hidden-layer architecture.
Its primal quantities satisfy

    ||W2||op=2sqrt(2),   ||W3||op=sqrt(5),
    ||c||/sqrt(n)=1,   ||z1||/sqrt(n)=1,
    h1=a1,   z2=z3=h2=h3=0.

In particular every readout coordinate is bounded; only RMS bounds are
needed. The backward fields are

    delta3=1,  q2=delta2=sqrt(n)v,
    q1=-2sqrt(n)e,  delta1=-sqrt(n)e.                (7)

Thus both backward RMS bounds hold, but `q2` has two concentrated
coordinates. Using the actual trained-weight velocities gives

    W2'=a v1^T/sqrt(n),    W3'=0,    c'=0,
    nu1=-sqrt(n)e,
    nu2=sqrt(n)(m v-w),
    nu3=(5m+1)1,
    delta3'=q2'=delta2'=0,   q1'=5a1.               (8)

For example, `W2' h1=m sqrt(n)v`, while
`W2 D1 nu1=-sqrt(n)w`; their sum yields `nu2`. Thus `q2_1>0`
but `nu2_1<0`. Both matrix blocks remain variables of the full field;
the zero instantaneous `W3'` in (8) is evaluated from its training
equation, and mixed variations in that block are retained below.

Here `M2=M3=0`, while `M1=diag(sqrt(n)e)` has operator norm one.
The maps `S2,S3,T2,J` all have width-independent operator bounds.
The complete `B` therefore has a width-independent operator bound at
(6). No such bound holds for its material derivative.

## 3. Exact positive Rayleigh quotient

Choose the unit hidden variation and the corresponding unit full
variation

    u1=0,   E2=e1 1^T/sqrt(n),   E3=0,   U=(u,0).

Equations (2), (6), and the balance of `e` give

    T1u=0,   T2u=a e1,   T2'u=0,
    T3u=a1/sqrt(n),   S3u=0.

In the contraction `u^T A' u`, every bottom-layer and mixed term of
(4) vanishes exactly: the second-layer mixed terms contain `T1u=0`,
and the third-layer mixed terms contain `S3u=S3'u=0`. The remaining
terms are `M2'` and `M3'`. Since `phi''(0)=0` and `phi'''(0)=-2`,

    (M2')_11=-2 nu2_1 q2_1=2(1-m)n,
    M3'=-2(5m+1)I,

    U^T B' U=2m(1-m)n-2m(5m+1).                    (9)

For completeness, the full Hessian acting on this same tangent is

    (Au)_z1=1/(2sqrt(n)) 1,
    (Au)_E2=0,
    (Au)_E3=a1e1^T/sqrt(n),
    Ju=a1/sqrt(n).

The nonzero `E3` block is the mixed trained-third-matrix Hessian term.
Hence, in the ordinary Euclidean/Frobenius metric required by the
canonical raw Gaussian coordinates,

    ||BU||^2=1/4+2m,

    U^T(B'-kappa B^2)U
       =2m(1-m)n-2m(5m+1)-kappa(1/4+2m).           (10)

For every fixed real `kappa`, this tends to positive infinity.
In particular the proposed `kappa=3/2` form is

    2m(1-m)n-10m^2-5m-3/8.                         (11)

No constant depending only on the stated primal bounds can upper-bound
`B'-(3/2)B^2` as a quadratic form. Changing the fixed coefficient in
front of `B^2` does not repair the estimate.

The same state rules out a lower bound. Replace `e1` by `e2` in `E2`
and call the resulting unit full variation `U2`. The same calculation
gives

    U2^T B' U2=-4m(2m+1)n-8m(5m+1),
    ||BU2||^2=1+5m.

Thus `U2^T(B'-kappa B^2)U2` tends to negative infinity for every fixed
real `kappa` as well.

## 4. Why the scalar Schwarzian does not give this matrix bound

The exact scalar identity is

    phi''' phi'-(3/2)(phi'')^2=-2(phi')^4.

It would apply to a scalar material velocity proportional to that same
coordinate's `phi' q`. The actual middle velocity is

    nu2=[ (||h1||^2/n) I+W2 D1^2 W2^T ]delta2.

The bracket is positive semidefinite, but its off-diagonal entries can
make an individual product `nu2_i q2_i` negative. In (6), its rare
two-coordinate block is `mI+ww^T`, and

    q2_1 nu2_1=(m-1)n<0.

At `z2=0`, the corresponding Hessian diagonal vanishes because
`phi''(0)=0`, while its material derivative equals
`-2 q2_1 nu2_1>0`. Equation (10) shows directly that the other actual
Hessian blocks, including matrix-training mixed terms, do not supply a
compensating term of order `n` in `B^2`.

## 5. Exact scope of the conclusion

This falsifies only an instantaneous width-independent signed matrix
bound inferred from the listed primal bounds for all actual network
states. It uses the canonical architecture, scaling, Euclidean metric,
and complete field. It is not a frozen-backward scalar surrogate.

The displayed states are not asserted to be typical under the specified
Gaussian initialization. In fact they have `f=c^T h3/n=0` and `c=1`,
so they cannot be positive-feature-time states of a trajectory started
at exactly zero readout: along this gradient field,
`f'=||b||^2/n>=0`; equality of initial and final `f=0` would require
`b=0` throughout, hence a stationary state with `c=0`. The prescribed
finite-width Gaussian law has full support, but support alone gives no
useful high-probability or expectation obstruction. An estimate requiring additional
trajectory-specific probabilistic structure is left open. No projected
Jacobian, stability, population-flow, or convergence theorem is settled.

## 6. The same ambient obstruction holds in physical time

The physical vector field is alpha b, with alpha=2(1-f) and f=F/n.
Write B_phys for its full Jacobian, and put K=||b||^2/n. Since
grad f=b/n, exactly

    B_phys=alpha B-(2/n)b b^T.

At the state (6), alpha=2. Differentiating at fixed physical time,
using dot alpha=-2 alpha K and dot b=alpha B b, gives

    dot B_phys
      =-4K B+4B'-(4/n)(B b b^T+b b^T B).              (12)

Here B' is the feature-time material derivative already computed;
the factor four is retained because both the prefactor alpha and the
material clock contribute.

At (6), the only nonzero blocks of b are

    b_z1=-sqrt(n)e,    b_E2=a v 1^T,
    ||b||^2=n(1+5m),  K=1+5m.

For each of the two tangents U,U2 above, direct use of their displayed
Hessian images gives

    U^T B U=U2^T B U2=0,
    (BU)^T b=(BU2)^T b=0,
    U^T b=a sqrt(n),        U2^T b=-2a sqrt(n).

Thus the correction terms in (12) have zero quadratic pairing with
both tangents. The exact identities are

    U^T dot B_phys U
        =8m(1-m)n-8m(5m+1),
    ||B_phys U||^2=1+12m+20m^2,                       (13)

    U2^T dot B_phys U2
        =-16m(2m+1)n-32m(5m+1),
    ||B_phys U2||^2=4+36m+80m^2.                     (14)

For example B_phys U=2BU-(2a/sqrt(n))b, and the two terms
are orthogonal, proving the norm in (13). The analogous coefficient
is 4a/sqrt(n) for U2. The full operator B_phys remains uniformly
bounded since B is bounded and ||b||^2/n=1+5m.

Consequently no fixed real kappa makes
dot B_phys-kappa B_phys^2 uniformly bounded above or below on the
same bounded-primal state class. This is an exact physical-time
calculation, not a substitution of trajectory-dependent clock values
into a finite-map derivative. The same non-reachability and Gaussian
scope restrictions in Section 5 remain in force.

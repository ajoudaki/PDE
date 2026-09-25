# A circle function and circle RMS from global scalar aggregates

2026-09-25. Scoped theory route for the existing scalar compression question.
This is a proposed mathematical extension of the old-clock, fixed-P compiler,
not an implemented solver or an independent promotion review. No experiment,
runtime quadrature scheme, dense decoder, or Git operation is part of this
report. The first version is frozen before exchange with other current routes.

The conclusion is affirmative at the level of existence at fixed finite width,
fixed P and prescribed finite time: one can evolve finitely many **integrated
contractions**, including Fourier coefficients of the circle output, instead
of retaining passive query responses at finitely many angles. The enlarged
compiler still has a finite substitution grammar. Its saturated finite
truncations inherit the finite-horizon convergence argument. The crucial
change is that disconnected neuron diagrams sharing one angle must remain
inside the same angular integral. This is not the original connected-neuron
dictionary with an integral applied separately to every factor.

## 1. Contract and supplied assumptions

Fix finite n, training sample count M, input dimension d, history order P,
realized initialization, and T<infinity. The target is the finite-width
three-hidden-layer old activity-clock response-memory system in
`DEEP_CIRCLE_DERIVATION.md`, equations (4)--(8). Its reconstructed matrices
are W-hat_2 and W-hat_3, and its activity length is L>=1. Training sources
use only the M training examples. For definiteness the input circle is

    U(theta)=u_c cos(theta)+u_s sin(theta),  theta in R/(2 pi Z),

with fixed vectors u_c,u_s in R^d; the normalization x/sqrt(d) is included
in these vectors. Set dmu=dtheta/(2 pi) and

    f(t,theta)=c(t)^T h_3(t,theta)/n.

Here h_ell(t,theta) denotes the exact forward response of the current
reconstructed network. These functions define the target observables;
they are not functions stored in the proposed scalar runtime state.

The inherited finite-horizon assumption is the initial-data bound invoked
in `SCALAR_COMPRESSION_BOUND_ASSESSMENT.md`, section 9: for the target old
tanh system, primitive neuron species and initialized entries C_ell=n W_ell0
admit a computable bound on [0,T]. That source uses the parent fixed-depth
theorem to supply the bound. This report checks the angular extension of
the scalar proof, not that upstream theorem, whose full source is outside
this route's input scope. Since |h_ell(t,theta)|<=1 at every real theta,
adding passive angular responses does not enlarge the primitive bound.

Permitted preprocessing uses initialization, training data, P, T, the
equations and desired circle observables. It may compute angular integrals
of initialized contractions, potentially by certified quadrature. No trained
trajectory is permitted as initialization, coefficients or runtime forcing.
The runtime state consists of ordinary real scalar contractions and L.

The two independent approximation resolutions will be K, the contraction
complexity cutoff, and J, the Fourier readout degree. The theorem first
fixes J and lets K increase. An angular regularity bound then permits J to
increase. No uniformity in n, useful state count, cheap preprocessing,
all-time accuracy, or control of loss-based stopping times is asserted.

## 2. What an integrated contraction must retain

Start with the exact normalized neuron diagrams of
`POPULATION_SCALAR_CONSTRUCTION_CHECK.md`. In addition to the training
species, allow h_1(theta),h_2(theta),h_3(theta) as decorations. All query
decorations in a given angular block refer to **the same theta**. If H is
a possibly disconnected neuron diagram with these decorations, write
q_H(t,theta) for its neuron-index contraction at fixed theta. Introduce

    Q[H,p,w](t)=integral p(cos(theta),sin(theta))
                            w(theta) q_H(t,theta) dmu,

where p is a monomial in the two static circle fields and w is one of
1, cos(k theta), sin(k theta) for a selected finite list of k. A time
derivative never differentiates p or w. Static polynomial circle factors
are retained as decorations, rather than converted into shifts of k.
Thus a fixed Fourier test weight generates its own contraction hierarchy;
there is no unmentioned truncation of Fourier convolutions in its RHS.

The coefficient F_k(t)=integral f(t,theta) exp(-i k theta) dmu is read from
two real coordinates:

    F_0=Q[c h_3,1,1],
    F_k=Q[c h_3,1,cos(k theta)]-i Q[c h_3,1,sin(k theta)],  k>=1,
    F_-k=conjugate(F_k).

Neuron factorization before integration remains exact, but does not give
factorization after integration. For example,

    integral cos(theta)^2 dmu=1/2,
    (integral cos(theta) dmu)^2=0.

Consequently, if a generator term at fixed theta contains
q_H1(theta) q_H2(theta), its integrated value is Q[H1 disjoint-union H2,p,w],
not a product of two separately integrated coordinates. To make the first
coefficient equation explicit, define the normalized same-layer pairings

    C_ell(theta,a)=E_ell[h_ell,theta h_ell,a],
    R_ell(theta,a)=E_ell[delta_ell,theta delta_ell,a],
    S_ell(a,theta)=E_(ell-1)[Bbar_ell,a h_(ell-1),theta],
    T_ell(theta,a)=E_ell[delta_ell,theta Abar_ell,a],
    G_(theta,a)=U(theta)^T U_a.

Here E_ell is a normalized neuron average and Abar,Bbar are the history
endpoint reconstructions L^-1 sum_(p<P)(2p+1)A_p,B_p. Query backward fields
delta are expanded through the actual reconstructed adjoints; they need
not be new primitive dynamic species. Write I_k[v]=integral exp(-i k theta)
v(theta) dmu. The exact coefficient velocity obtained from the supplied
output equation is

    F_k_dot=-(2/M) sum_a r_a
                {I_k[C_3(theta,a)]+I_k[G_(theta,a) R_1(theta,a)]}
            -(2/M) sum_(ell=2,3;a)
                {r_a I_k[R_ell(theta,a) S_ell(a,theta)]
                 +rho I_k[T_ell(theta,a)
                       (C_(ell-1)(theta,a)-S_ell(a,theta))]}.

Each I_k on this RHS is an integrated contraction to be included and then
differentiated by the same rules. This is the principled auxiliary state
behind the Fourier coefficients; coefficients alone have not been shown
to close. The theta-dependent input Gram is a fixed linear combination of
cos(theta) and sin(theta), which explains the static circle decorations.

A precise factorization convention is to add one formal angle vertex to
the diagram and attach every query decoration and static circle factor to
that vertex. The Fourier test weight is also attached there. Factor only
components of this augmented incidence diagram. Every component without
the angle vertex is a training-only scalar and can leave the integral.
All components connected through the angle vertex remain together as one
integrated scalar. This convention uses no probabilistic independence.

For two already integrated scalars their product can, if needed, be written
using separate variables theta and phi by the product-integral identity.
One may introduce a fresh angle only in that situation. Replacing shared
theta by independent theta,phi inside one original integrand is invalid.
The present generator needs at most one angle block per monomial, together
with a fixed finite number of training-only factors.

## 3. A finite grammar and an exact hierarchy

The formal query responses obey the actual forward chain rules

    h_1_dot(theta)=(1-h_1(theta)^2) [W_1_dot U(theta)],
    h_2_dot(theta)=(1-h_2(theta)^2)
        [W-hat_2_dot h_1(theta)+W-hat_2 h_1_dot(theta)],
    h_3_dot(theta)=(1-h_3(theta)^2)
        [W-hat_3_dot h_2(theta)+W-hat_3 h_2_dot(theta)].

Products are componentwise. Expand the weight and matrix velocities using
the training equations and their history factors exactly as in the supplied
compiler. This uses finitely many rooted templates, the same initialized
edges in forward and transpose directions, and the two static circle fields.
Query labels and angular integrals never enter training residuals or sources.

Differentiate an integrated contraction by the product rule. A replaced
query decoration uses its rooted query template with the existing angle;
a training decoration uses its usual training template. Attach fresh neuron
indices, retain the single common angle, and factor by the rule in section 2.
The result is a finite sum of products of training contractions and one
integrated contraction, with coefficients polynomial in training residuals
and rho and rational in L with denominators consisting only of powers of L.
Training equations remain an autonomous subsystem. Before clipping, the
angular hierarchy is linear in its angular coordinates conditional on the
training contractions, although it requires arbitrarily complicated angular
coordinates.

At fixed n, all integrands and their time derivatives are continuous on
the compact theta interval and bounded on any compact existence interval:
there are finite neuron sums, finitely many factors in each integrand,
bounded tanh responses and continuous finite-dimensional weight/history
velocities. The time derivative is therefore dominated by an integrable
constant on such an interval. Differentiation under the integral is valid,
so the compiled hierarchy is exact along the target trajectory.

For a concrete complexity, count neuron vertices, initialized edges,
dynamic decorations, static cos/sin factors, the one angle vertex when
present, and one test-weight tag when present. Connectivity includes
query-to-angle incidence, but these incidence relations require no extra
size count. Call this total s(H). Training output diagrams have size 3;
all the Fourier output coordinates can be assigned size 5 by retaining
their angle vertex and tag also at k=0. At a fixed K and finite test-weight
list there are finitely many types, independent of n.

There is a fixed integer delta>=1 such that substitution increases the
sum of component sizes by at most delta, and a fixed bound on the number
of factors produced by one substitution. To see this, each operation
replaces only one decoration by one of the finitely many templates.
It adds a bounded number of neuron vertices, edges, decorations and static
circle factors, while identifying the new angle with the old one. If removal
of the old query decoration detaches its neuron component from the angle,
that creates at most one additional detached factor. All further detached
factors belong to the fixed template. There are at most s(H) choices of the
differentiated decoration. Hence the absolute row coefficient sum is O(s(H)),
with constants independent of K.

These are the three properties used in the existing convergence proof:
bounded total-size increment, bounded factors per term, and linear row
growth. Underlying neuron forests generated by the original outputs can
still be used. Augmented connectivity through the common angle must not
be confused with connectedness or acyclicity of the neuron graph alone.

## 4. Finite saturated closure and its convergence

Retain the training contractions and the augmented connected contractions
with s(H)<=K. Include every desired output coordinate. Delete an entire
generator monomial if any of its factors lies outside this set. Call the
resulting finite generator G_K. The remainder evaluated on the target is
the explicitly deleted sum, exactly as for the original compiler.

The normalized angular integration has mass one. Thus the inherited
primitive bound supplies B_T>=1 for which

    |q_H(t)|<=B_T^s(H),  0<=t<=T,

for both the training and integrated diagrams. Bound every finite-sum
integrand by products of primitive and edge bounds; the normalized neuron
sums and integral do not enlarge that bound. Fourier test weights have
magnitude at most one. Static cos/sin factors also have magnitude at most
one, at every degree.

Choose R>=B_T and clip each real scalar coordinate at its own threshold,

    S_H(z)=max(-R^s(H),min(z,R^s(H))).

The new finite scalar system is

    z_H_dot=G_(K,H)(S(z),L_z),
    L_z_dot=rho(S(z_training_outputs)),  L_z(0)=1.

Initialize retained coordinates by their exact initial contractions.
All residuals and coefficients use clipped training outputs. Report the
clipped Fourier coordinates, storing only k>=0 and imposing conjugate
symmetry in the readout. Independent real-coordinate clipping then defines
a real trigonometric polynomial. This construction is a saturation of the
**enlarged** compiler; it is not a claim that the existing compiler already
evolves these variables.

Here is a verification of the inherited convergence argument. The finite
template properties give constants A,D, independent of K, with

    |G_(K,H)(q,L)|<=A s(H) b^(s(H)+D)

whenever |q_J|<=b^s(J), b>=1 and L>=1. The finite powers of the training
residuals and rho are absorbed in D. Therefore the saturated RHS is bounded
coordinatewise, and

    |z_H_dot|<=A s(H) R^(s(H)+D),
    0<=L_z_dot<=R^3+Y,  Y=(M^-1 sum_a y_a^2)^(1/2).

The finite locally Lipschitz ODE exists for all time. On [0,T], put
R_*=R(1+AT R^D) and L_*=1+T(R^3+Y). Integration and
(1+c)^s>=1+cs for integer s>=1 give

    |z_H(t)|<=R^s(H)(1+AT s(H)R^D)<=R_*^s(H),
    1<=L_z(t)<=L_*.

The true target is unchanged by S on [0,T], and
|S_H(z_H)-q_H|<=|z_H-q_H|. With

    E_m(t)=max(|L_z-L|/L_*,
               max_(s(H)<=m)|z_H-q_H|/R_*^s(H)),  m>=3,

we have E_m<=2. For m+delta<=K there are no deleted terms in rows of size
at most m. Telescope every finite product, use the nonexpansiveness of S,
the Lipschitz bound for the residual norm, and L>=1. The size-increment and
row-growth estimates yield a constant C_T independent of m,K such that

    E_m(t)<=E_m(s)+C_T m integral_s^t E_(m+delta)(u)du.

This inequality includes the clock after increasing C_T. Repeated
substitution r times on an interval of length h yields

    sup E_m <= sum_(j=0)^(r-1)
       [(C_T h)^j/j! product_(i=0)^(j-1)(m+i delta)] E_(m+j delta)(s)
       +2 binomial(r+a-1,r)(C_T delta h)^r,
       a=ceil(m/delta).

The ordered integration simplex supplies 1/j!. The product is bounded by
delta^j times the rising factorial of a. For h with C_T delta h<1, the
last term tends to zero because its binomial prefactor grows polynomially
in r. Suppose every fixed-coordinate error tends to zero at s. First send
K to infinity at fixed r in the finite sum, then send r to infinity. This
proves convergence on the interval. Exact initialization starts this
argument, and finitely many such proof intervals cover [0,T]. No restart
or target refresh occurs in the actual scalar algorithm.

Consequently every fixed finite collection of integrated contractions,
including all |k|<=J Fourier coefficients, converges uniformly in physical
time as K increases. The explicit estimate of the supplied assessment,
section 9, also transfers with output size 3 replaced by its enlarged size
s_*: take

    N=max(1,ceil(16 C_T delta T)),
    a=ceil(s_*/delta),  Q=floor(K/(delta 2^N)).

When Q>=a, each requested real coordinate has error at most

    epsilon_K=2N R_*^s_* 4^(-Q).

Indeed its proof only iterates the displayed E_m inequality, with the same
halving of the controlled grade on each proof interval; all its hypotheses
were verified above. For Fourier coefficients s_*=5 suffices. This is a
possibly enormous sufficient cutoff, not an efficiency claim. Unsaturated
zero-tail equations receive only the corresponding local argument; compact
angular integration does not repair their unresolved large-time stability.

## 5. Arbitrary-angle reconstruction and explicit spatial tails

Let F-hat_k be the clipped Fourier readout and set

    f-hat_(K,J)(t,theta)=sum_(|k|<=J) F-hat_k(t) exp(i k theta).

Evaluation at any requested theta requires this finite sum, without a neuron
forward pass or a query-response ODE. Put

    d_(K,J)(t)^2=sum_(|k|<=J)|F-hat_k(t)-F_k(t)|^2.

If each stored real coordinate has error at most epsilon_K, conjugate
symmetry gives

    d_(K,J)<=sqrt(4J+1) epsilon_K.

Use the normalized L2 norm on the circle. Orthogonality and completeness
of exp(i k theta) give Parseval and the exact identity

    ||f-hat_(K,J)-f||_2^2
      =d_(K,J)^2+sum_(|k|>J)|F_k|^2.                 (1)

For clarity, completeness here requires no source-specific spectral claim.
The Fejer kernel is nonnegative, has integral one, and its mass outside any
fixed neighborhood of zero tends to zero, as follows from
K_N(theta)=(N+1)^-1[sin((N+1)theta/2)/sin(theta/2)]^2.
Splitting its convolution integral into that neighborhood and its complement
proves uniform approximation of every continuous periodic function by
trigonometric polynomials. Such functions are dense in L2 (approximate
interval step functions by continuous ramps). This proves completeness;
orthogonal projection then gives Parseval. The actual finite tanh circle
function is smooth, so all these hypotheses hold.

Suppose B_1 bounds ||partial_theta f(t,.)||_2 uniformly for t<=T.
Integration by parts on the periodic interval gives derivative coefficients
i k F_k, so Parseval for the derivative implies

    sum_k k^2|F_k|^2<=B_1^2.

For J>=0 this gives the explicit RMS tail bound

    (sum_(|k|>J)|F_k|^2)^(1/2)<=B_1/(J+1).         (2)

For J>=1, Cauchy--Schwarz and sum_(k>J) k^-2<=1/J give

    sum_(|k|>J)|F_k|<=B_1 sqrt(2/J).

The Fourier series is absolutely and uniformly convergent under this H1
bound and has the same coefficients as f, so completeness identifies its
sum with the continuous f. Thus

    sup_theta |f-hat_(K,J)-f|
       <=sqrt(2J+1) d_(K,J)+B_1 sqrt(2/J).          (3)

Equations (1)--(3) prove both circle RMS and arbitrary-angle approximation
with separate contraction and Fourier errors. A usable target regularity
constant is

    B_1 <= sup_(t<=T,theta) [ ||c(t)||_2/n
             ||W-hat_3(t)||op ||W-hat_2(t)||op
             ||W_1(t)||op ||U'(theta)||_2 ].

This is obtained by the forward angular chain rule and |tanh'|<=1;
normalization of dmu turns a uniform derivative bound into an L2 bound.
Initial-data physical weight bounds therefore provide a finite B_1 for
the present fixed-n compact-horizon problem.

If instead f has a holomorphic periodic continuation to a neighborhood of
the closed strip |Im theta|<=sigma, with |f|<=A there uniformly for t<=T,
contour shifting gives |F_k|<=A exp(-sigma |k|). For k>0 shift downward
by sigma and for k<0 upward; periodicity cancels the vertical sides.
Geometric summation then gives

    L2 tail <= A sqrt(2) exp(-sigma(J+1))
                             /sqrt(1-exp(-2sigma)),
    uniform tail <=2A exp(-sigma(J+1))/(1-exp(-sigma)).

A positive common strip and its bound must be supplied or proved; they
are not inferred merely from the word tanh, whose complex continuation
has poles. The H1 result above does not require analyticity.

For this finite three-layer network an explicit strip can in fact be
proved from physical bounds. Let a_1,a_2,a_3 bound the induced infinity
matrix norms of W_1,W-hat_2,W-hat_3 on [0,T], and let

    b=||u_c||_infinity+||u_s||_infinity,
    D=b a_1 max(1,2a_2,4a_2 a_3),
    A=sup_(t<=T)||c(t)||_1/n.

All these bounds can be enlarged using the same permitted initial-data
physical bounds. If D>0, choose sigma=asinh(pi/(8D)). For theta=x+i v,
the imaginary input has infinity norm at most b sinh(|v|). The elementary
identities for z=u+i y give, when |y|<=pi/4,

    |Im tanh(z)|=|sin(2y)|/(cosh(2u)+cos(2y))
                  <=tan(|y|)<=2|y|,
    |tanh(z)|^2=(cosh(2u)-cos(2y))
                         /(cosh(2u)+cos(2y))<=1.

The three preactivation imaginary parts are consequently bounded by
b a_1 sinh(sigma), 2b a_1 a_2 sinh(sigma), and
4b a_1 a_2 a_3 sinh(sigma), each at most pi/8. Composition is holomorphic
there and the readout is bounded by A. There is a slightly wider strip
on which the same estimates stay below pi/4, so holomorphy holds in a
neighborhood of the closed strip used in the contour shift. If D=0,
either the circle input or W_1 is zero throughout the bounded family;
with the stated bias-free architecture the output is zero and no tail
remains. Thus an explicit analytic tail certificate is available here,
although sigma may be extremely small. This strengthening was derived
after the first freeze and uses only the already scoped physical equations.

At finite K,J the polynomial's value at a training angle need not equal
the separately evolved training-output coordinate used in rho. Its
discrepancy is bounded by the polynomial error to f plus the training scalar
error. Replacing training residuals by polynomial evaluations would define
another closure and would require a new proof.

## 6. Circle RMS without an evaluation mesh

Let g be a specified real L2 circle reference, with coefficients G_k and
known ||g||_2. Parseval evaluates the actual reconstructed polynomial's RMS
exactly from finitely many readout coefficients and these reference data:

    ||f-hat_(K,J)-g||_2^2
      =sum_(|k|<=J)|F-hat_k-G_k|^2+sum_(|k|>J)|G_k|^2
      =sum_(|k|<=J)|F-hat_k|^2
         -2 Re sum_(|k|<=J)F-hat_k conjugate(G_k)+||g||_2^2.

Only J reference coefficients and their conjugates plus the reference norm
are needed. These are fixed problem data or preprocessing outputs, not
runtime angular quadrature. The reverse triangle inequality gives

    | ||f-hat_(K,J)-g||_2-||f-g||_2 |
       <=||f-hat_(K,J)-f||_2,

which is controlled by (1)--(2). If only training labels are given and no
whole-circle reference g is specified, a circle RMS to that reference is
not defined by the labels alone.

There is also a direct functional alternative when only RMS is desired.
Retain E=integral f(theta)^2 dmu and C_g=integral g(theta)f(theta) dmu.
For E the diagram contains two output components with independently summed
neuron indices but the **same** angle:

    E=integral n^-2 sum_(i,j)
             c_i h_3,i(theta)c_j h_3,j(theta) dmu.

Its generator again uses one angle block. For C_g, add the fixed g(theta)
test weight. Assuming g is bounded, its bound can be included in B_T and
the preceding finite-grammar proof applies unchanged. The identity

    ||f-g||_2^2=E-2C_g+||g||_2^2

requires no Fourier tail. Their exact starting velocities are

    E_dot=2 integral f(theta) f_dot(theta) dmu,
    (C_g)_dot=integral g(theta) f_dot(theta) dmu,

with f_dot given by the same unintegrated output formula above. Inserting
the additional common-angle factor f or fixed weight g generates their
required auxiliary contractions by precisely the same compiler.
With approximate clipped coordinates E-hat,C-hat,
report sqrt(max(0,E-hat-2C-hat+||g||_2^2)). If their errors are eta_E,eta_C,
the RMS error is at most sqrt(eta_E+2eta_C): projection onto [0,infinity)
is nonexpansive and |sqrt(a)-sqrt(b)|<=sqrt(|a-b|) for a,b>=0.
The maximum is necessary because the scalar truncation does not preserve
moment realizability. This direct estimate targets the target-network RMS;
at finite cutoff it is not the exact RMS of the separately reconstructed
Fourier polynomial. The Parseval formula above is the latter quantity.

The extra energy also exposes a spectral-tail diagnostic. Exactly,

    T_J=E-sum_(|k|<=J)|F_k|^2=sum_(|k|>J)|F_k|^2>=0.

Its approximate value T-hat_J=E-hat-sum_(|k|<=J)|F-hat_k|^2 need not be
nonnegative. If |E-hat-E|<=eta_E and the low-coefficient error is bounded
by d, telescoping the squares and applying Cauchy--Schwarz gives

    |T-hat_J-T_J|<=eta_E+2||F-hat_low||_2 d+d^2.

Adding this certified margin to T-hat_J, and projecting upward to zero,
therefore supplies a valid squared-tail upper bound. Without the error
margin, the computed quantity is a diagnostic, not a tail certificate.

## 7. What this establishes and what it does not

There is no evolving passive test mesh in this mathematical construction.
There is no function-valued scalar coordinate: every retained entry is a
single real integral, whose derivative is a finite algebraic expression in
other retained scalars after truncation. Angular response functions occur
only in defining target contractions and evaluating their initial values.
Numerical initialization may still require many original-network forward
evaluations and angular quadrature. Exact-integral initialization is the
theorem's assumption; a real implementation must bound quadrature and
roundoff errors. At a fixed K a finite Lipschitz constant propagates an
initial perturbation eta by at most eta exp(Lambda_K T), so arbitrarily
accurate certified initialization suffices in principle, without a useful
cost bound. Runtime time-stepping introduces another error to certify.

The extension enlarges the state. A pre-existing finite training-only
scalar state does not already contain these Fourier/integrated coordinates,
and this argument provides no rule for recovering their present values
from it. They must be included and initialized before scalar evolution.
The result is a circle-function readout, not reconstruction of individual
dense weights. It does not prove that a dense network can be decoded from
the retained aggregate state or that such a decoder is unique.

For comparison to dense training at the same physical time, add the
independent parent discrepancy by the triangle inequality:

    ||f-hat_(K,J)-f_dense||_2
      <=d_(K,J)+B_1/(J+1)+||f_P-f_dense||_2.

An applicable parent weight-tracking theorem plus a uniform circle readout
bound controls the final term. The contraction theorem holds at fixed P;
it does not itself prove that parent bound, justify simultaneous limits,
or control fitted endpoints reached at different stopping times.

The route's actual positive result is therefore finite-horizon functional
compression at fixed finite n,P, with a specified enlarged hierarchy and
separate, explicit scalar and angular errors. Practical state count,
initialization complexity, stable numerical evaluation, width-uniform
accuracy and empirical usefulness remain untested.

## Scope and provenance

Complete scientific inputs read: `POPULATION_TO_AGGREGATES.md`,
`POPULATION_SCALAR_CONSTRUCTION_CHECK.md`,
`SCALAR_COMPRESSION_BOUND_ASSESSMENT.md`, and `DEEP_CIRCLE_DERIVATION.md`,
all in this study. Their references were not followed to other scientific
files or archives. Required process inputs: the rigorous-math skill and
the conjecture skill with its research-contract and adversarial-audit
references. This report records a scoped derivation and author audit,
not implementation evidence or an independent review.

The first candidate was frozen before any exchange of other route findings
at SHA256 0aba61704d07e15cbb116b3bb8277c50011a73df0a178c3d2b2cad54be350a56.
The subsequent author elaboration displayed the complete first Fourier and
energy/correlation equations; it introduced no external-route input.

## Post-freeze design organization and decoder comparison

Following the supervisor's explicit scope expansion, this author read the
complete `SCALAR_DECODER_LIMITS.md`. Its polynomial-activation construction
provides a different approximate circle decoder from sufficiently rich
training-only contractions. It does not require angular coordinates, and
it can be converted into a finite Fourier polynomial on the circle. Thus
the present proposal's addition of integrated variables is a design choice,
not a necessary condition for every possible circle readout. The statement
in section 7 is only about information directly supplied by this proposal.
At a fixed cutoff neither route asserts an exact inverse, and the
training-only polynomial route requires all of its higher contractions to
have been retained during training. No proof or implementation of its
practical efficiency is imported here.

The selected direct Fourier design has a useful further organization.
Let q denote the complete retained training-only dictionary at cutoff K.
Let Q_w be the vector of all retained angle-block contractions with one
fixed test weight w. Use the same unweighted diagram index list for
w=1,cos(theta),sin(theta),...,cos(J theta),sin(J theta), always counting
one weight tag, even when w=1. Keep pure static angular integrals such as
integral w cos(theta)^a sin(theta)^b dmu as zero-derivative coordinates.
Do not first simplify them to mode-dependent constant forcing.

Under this convention the exact finite unsaturated generator is

    q_dot=G_K^train(q,L),
    L_dot=rho(q_training_outputs),
    (Q_w)_dot=A_K(q,L) Q_w.                           (4)

The same real matrix of scalar coefficient functions A_K applies to every
w. The reason is structural: each replacement retains one common angle,
all other factors are training-only, and the time derivative never acts on
w. Collecting training factors makes each row linear in its angle-block
factor. If that factor has no dynamic decorations it is one of the static
coordinates just retained. Identical size conventions make the deletion
test independent of w. All dependence on k is consequently in the initial
Q_w values and in the final trigonometric readout, not in A_K.

The saturated version is correspondingly

    q_dot=G_K^train(S_train(q),L),
    L_dot=rho(S_train(q_training_outputs)),
    (Q_w)_dot=A_K(S_train(q),L) S_angle(Q_w).         (5)

Its angle block is no longer linear as a function of its raw coordinates,
because clipping is nonlinear. It remains a scalar ODE with the same
coefficient functions for all trigonometric weights. The training trajectory
at the same K is unchanged if its original dictionary and clipping thresholds
are held fixed. The new angular species never enter training residuals or
sources. For the trigonometric weights the old primitive bound already
covers the new static/query factors, which all have magnitude at most one.
If an additional non-unit-bounded test weight g requires larger angular
caps, those caps can be changed separately without changing the training
caps; the proof uses a common upper envelope for both sets.

Equations (4)--(5) can be compiled as sparse scalar expressions. No claim
is made that explicitly materializing the matrix A_K is efficient. This
organization specifies shared algebra across Fourier modes; it does not
eliminate the large mixed-contraction dictionary each mode may require.

### Version-specific collaborative check of the root synthesis

After the scope expansion, this author read all 539 lines of
`SCALAR_CIRCLE_FUNCTION_READOUT.md` at SHA256
786cff262ff17f22662c8ec922e19c86a18aec06e2759fb07b66fa731cf108cf.
No required mathematical correction was identified. The checks covered:
the common-angle factorization rule and finite substitution increment;
the distinction between general augmented diagrams and the selected
one-angle subsystem; retention of static angular coordinates for a common
homogeneous A_K across modes; preservation of the existing training caps;
nonlinearity of saturated angular evolution; readout grades 5 and 8;
the real-coordinate coefficient factor 4J+1; Parseval and H1 tails;
the explicit analytic strip and both geometric-tail constants; the
difference between the polynomial's RMS and the target-network RMS; and
the certified correction margin in the energy-tail diagnostic.

At finite cutoff the Fourier polynomial may differ from the dedicated
training coordinate at a training angle. The root document already states
that residuals use the training coordinates and substituting the polynomial
would change the feedback rule. This is sufficient to keep the theorem's
target unambiguous. The check is collaborative and post-freeze, not an
independent promotion review; it applies to the exact hash recorded above.

The full subsequent 552-line root version was reread at verified SHA256
c771be0dee6d4672fb9a6db7f3c64295bf63a0760e884285dd04a67ee1918a77.
This is the current checked root version and supersedes the preceding hash
for this audit. Its added one-angle/one-tag restriction makes the autonomous
mode-block family explicit. Its added physical-weight-to-circle argument
correctly uses bounded parameter derivatives uniformly over the compact
circle; the physical bound can be taken as a convex norm-bounded region
containing both parameter paths and their joining segments. No required
correction was identified in this version either.

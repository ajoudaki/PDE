# Feature learning changes the initial scalar decay rate

Root derivation, 2026-09-30, from the exact q=1 equations in
`TERMINAL_SCALAR_THEOREM.md`. This is a finite-width initialized theorem for
one training input and arbitrary width. It is not a multi-input fitting
theorem or an approximation guarantee. No neuron symmetry is assumed.

The purpose is to test a specific early scalar representation: a positive
mixture of fixed exponential decay rates. The actual q=1 flow violates that
representation already in its first three loss derivatives, because the
representation begins to improve after the readout starts moving.

## 1. Exact initial derivatives for one input

Take m=1, ||x||=sqrt(d), y in {-1,1}, and the prescribed initialization
w=v=0, k=h, tau=1. No probabilistic assertion is needed: A_0,W_0 are any
finite matrices for which g_0 is nonzero. Suppress initial subscripts in
the following definitions and use <u,v>=u^T v/n:

    h=tanh(A_0 x/sqrt(d)),     g=tanh(W_0 h),
    s=1-h^2,                 j=1-g^2,
    H=<h,h>,                G=<g,g>,
    p=g odot j,             u=s odot W_0^T p,
    D=<p,p>,                E=<u,u>,
    T=E+HD.

All these are scalar aggregates except the displayed auxiliary vectors.
G>0 implies H>0 and D>0, since j has strictly positive finite coordinates.
Consequently T>0.

The scalar coefficient C in the exact residual equation is

    C=2[<g,g>+<ell,ell>+<d,d><k,h>],
    b=tau^(-1)<d,v><h-k,h>,
    rdot=-Cr+|r|b.

At initialization C_0=2G, C'_0=0, and b_0=b'_0=b''_0=0. Direct
differentiation gives

    C''_0=32T.                                                 (1)

Therefore the initialized loss L=r^2, with L_0=1, obeys

    L'_0=-4G,
    L''_0=16G^2,
    L'''_0=-64G^3-64T.                                        (2)

Equivalently,

    (log L)''_0=0,        (log L)'''_0=-64T<0.                 (3)

The effective instantaneous decay rate -d(log L)/dt has zero initial
slope but strictly positive second derivative. Thus a scalar closure must
allow the rate itself to evolve, even in this one-input setting.

### Complete derivative check

At initialization A'=v'=k'=0, B'=h'=g'=0, and w'=2yg. Consequently

    d'=2yp,             ell'=2yu,
    A''=4u x^T/sqrt(d),
    h''=4s odot u=4s^2 odot W_0^T p,
    v''=4p,             B''=4p h^T/n,
    g''=4j odot [Hp+W_0(s^2 odot W_0^T p)].                    (4)

In particular

    <g,g>''=2<g,g''>=8(HD+E)=8T,
    <ell,ell>''=2<ell',ell'>=8E,
    <d,d>''=2<d',d'>=8D.

Because <d,d> and its first derivative vanish initially, only
<d,d>''<k,h>=8DH contributes to the second derivative of its product.
Adding the three contributions and multiplying by two proves (1).

For the b term, d=O(t), v=O(t^2), and h-k=O(t^2), hence b=O(t^5).
The local solution is smooth because r_0=-y is nonzero. On a small time
interval its sign is constant, so

    d(log L)/dt=-2C+2 sign(r)b.

This proves (3), and differentiation of L=exp(log L), using
(log L)'_0=-4G, gives all of (2).

The two contributions to T have distinct sources. E measures the
read-in feature acceleration through the actual W_0^T; HD measures the
learned value-memory contribution through B''. Neither source changes
the first loss slope. Together they change the third derivative with a
strict sign. No statement of all-time rate increase follows.

## 2. A sharp obstruction to fixed positive decay spectra

Suppose a proposed loss curve has the form

    L_mix(t)=integral_[0,infinity) exp(-lambda t) mu(dlambda),

where mu is a probability measure with finite second moment. This includes
every finite positive mixture of fixed decaying exponential modes. Its
initial logarithmic curvature is

    (log L_mix)''_0
       =integral lambda^2 dmu-(integral lambda dmu)^2 >=0.

If L_mix matches the actual q=1 value, slope and second derivative in
(2), this variance must be zero. Integrating the nonnegative square
(lambda-4G)^2 then gives mu=delta_(4G). Hence

    L_mix(t)=exp(-4Gt),      (log L_mix)'''_0=0,

contradicting (3). In fact its discrepancy from the actual loss is

    L(t)-exp(-4Gt)=-(32/3)T t^3+O(t^4).                        (5)

This is an exact initialized obstruction within q=1. It does not exclude
finite nonlinear scalar ODEs, signed exponential sums, controlled rational
approximations, or other encodings. It identifies one requirement on a
successful mechanism: scalar response rates must be allowed to change
through feature learning. A fixed positive spectrum cannot supply the
correct onset, even when one only requests the training loss.

## 3. Limits and relation to the terminal construction

At the outset T>0 forces an evolving response rate. In a certified small
terminal neighborhood, the terminal theorem permits freezing the complete
response generator with O(R^3) loss error. Those two facts suggest a
concrete division of approximation effort: capture response evolution
while residuals are appreciable; later retain its aggregate limiting
effect in a stable finite generator.

This note proves the need for the first part, not an efficient evaluator
for it. The aggregates G,T are computable from initialization at finite
width, but higher fidelity does not follow merely by adding their
derivatives. There is no claimed uniform approximation rate, population
limit, or sublinear-width construction here. A source approximation bound
under the scalar system's own feedback is still needed.

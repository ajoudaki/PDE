# Nonvanishing convex curvature: new local route, not a network theorem

Fix e=1/10 and define one data-independent activation

    phi(z)=1+z+e [ z arctan(z) - (1/2) log(1+z^2) ].

Then a=phi'=1+e arctan(z), b=phi''=e/(1+z^2)>0, and

    1-e*pi/2 <= a <= 1+e*pi/2,
    b'/b=-2z/(1+z^2).

The activation is smooth, strictly convex, globally Lipschitz, and has
bounded positive-order derivatives. Its nonlinear part has linear growth,
not bounded growth; it must NOT be silently substituted into the frozen
bounded-perturbation proof. Since b>0 on every finite z, it has no affine
interval, although its limiting slopes at the two infinities differ.

For the pure tangent pair with both prescribed incoming adjoints,

    M'=a(M)p+V b(M)q,       V'=a(M)q,

define the globally nonsingular scalar coordinate

    U(M) = (2/e) integral_0^M a(x)(1+x^2) dx.

It is an increasing smooth bijection R->R, with U'=2a/b bounded below
by a positive constant. Its magnitude is comparable, with constants
depending only on e, to |M|+|M|^3. Unlike the arctangent and quartic
tangent invariants, this coordinate has no singularity at M=0.

With I=U(M)-V^2 the exact equations are

    I'=k(U(M))p,     V'=a(M)q,
    k(U(M))=2a(M)^2/b(M).

The q terms cancel identically. In addition to positivity,

    k(U) <= C_e(1+|U|^(2/3)),
    dk/dU = 2b-a b'/b
           = 2e/(1+M^2)+2a(M)M/(1+M^2),

so k is globally Lipschitz and grows sublinearly in U. This is a
different forced-invariant structure from the singular defects of the
previous two local activations. For a prescribed finite L1 pair p,q,
|V|<=|V0|+L integral|q| and Bihari integration of
|I|'<=C_e(1+|I|^(2/3)+|V|^(4/3))|p| gives a polynomial state bound
in the initial coordinates and the two L1 driver norms. The precise
derivative bound remains to be established; bounded state growth does
not prove it. The actual network also has trained-operator transport.

Proposed next bounded task: prove a full fixed-driver and forcing
response bound for this nonsingular two-driver system whose dependence
on Gaussian-sized drivers admits every finite moment at fixed e, or
give a rigorous local obstruction to that particular bound. A pure-q
result is insufficient. No network or population continuation is claimed.

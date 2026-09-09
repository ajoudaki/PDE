# Independent audit of the quadratic/ReLU mesh verdict

## Verdict

The normalized-quadratic initial-layer theorem passes.  It proves failure
of compact-uniform convergence to a continuous initialized trajectory, while
leaving the isolated terminal paired loss open.

The width-two ReLU arithmetic and attracting-gate mechanism also pass, after
the three qualifications below are inserted.  None changes the report's
ultimate ReLU verdict: classical fixed-convention flow can fail, whereas the
generalized width-first Euler mesh remains open.

## 1. Quadratic theorem

For φ(x)=x²/√3, every deterministic nonnegative feature schedule
produces a finite-width output polynomial with nonnegative coefficients in
the schedule variables.  This follows before expectation: all coefficients
in the forward and update polynomials are nonnegative.  Gaussian expectation
retains an even raw monomial with a positive double-factorial weight and
annihilates an odd one.  Componentwise schedule monotonicity therefore holds
at finite width and survives each fixed-schedule width limit.

At every fixed finite loss horizon, output self-averaging and the quadratic
moment tower justify the deterministic adaptive schedule

\[
 s_k=h(1-F_k^h).
\]

If (F_k^h<delta<1), then (s_k>(1-delta)h).  With

\[
 t_N=leftlfloor{arepsilonover2h_N}ightfloor,
 qquad
 ho_*={(1-delta)arepsilonover4},
\]

one has eventually (ho_*/t_Nle(1-delta)h_N).  The established
constant-feature-step divergence then contradicts absence of a hit through
time (2t_Nh_Nlearepsilon).  Every quantifier is in the correct order:
width first at each fixed (N), followed by (N	oinfty).

Because a continuous grid interpolation attains (delta) at times tending
to zero, it cannot converge uniformly to a continuous function starting at
zero.  Its half-square loss cannot converge uniformly to a continuous
function starting at (1/2).  This does not control the signed post-hit
schedule and hence does not decide one terminal fine/coarse comparison.

## 2. Width-two ReLU arithmetic

With (c=sqrt2), (n=2),

\[
 u=(1,1),quad W_1=(1,-1),quad W_2=(2,0),quad
 a_1=-1/c,quad a_2=1/(4c),
\]

one obtains (H=(c,c)), (z_1=0), (z_2=2), (f=1/4), and
(r=3/4).  If (s) denotes the selected top-gate slope, the connector
contribution to the first normal velocity is (2ra_1s), and the lower
feature contribution is

\[
 r(2a_1s+2a_2c).
\]

Thus

\[
 dot z_1=r(4a_1s+2a_2c),qquad
 p=3/8,quad q=-21/8.
\]

The arithmetic is exact.

## 3. Required qualifications

First, (p) and (q) are the one-sided normal velocities at the contact,
not constants governing the complete full-state trajectory away from it.
The rigorous local statement is that continuity of the polynomial vector
field in each adjacent sign cell supplies a neighborhood in which

\[
 dot zge p/2>0quad(z<0),qquad
 dot zle q/2<0quad(z>0).
\]

An absolutely continuous solution starting at the contact cannot have a
component in either open half-line.  It must remain on the gate, where its
normal derivative is zero almost everywhere; this contradicts a continuous
nonzero assigned gate velocity.  Transversality and continuity give the
claimed positive-probability open set of nearby Gaussian initializations.

Second, the finite-width a priori constants must retain their initialization
dependence:

\[
 R_T=max{|A(0)|_n^2,|u(0)|_n^2}+T/2,qquad
 g_T=|G(0)|_{mathrm{op}}+2TR_T.
\]

The values (1) and (2) are width-limit or high-probability initialization
values, not deterministic bounds at arbitrary finite Gaussian width.  Also
(0<1-fle1) presupposes (f(0)in[0,1)), as holds for the displayed point
and the width-first initialized trace.  With these corrections, the kernel
bound

\[
 Kle8g_T^2R_T+4R_T^2
\]

is valid.

Third, the exact frozen rotation identity at a gate assumes the standard
contact convention (v(0)=p), or an orbit which never lands exactly at
zero.  With an arbitrary contact reset (v_0), a phase landing exactly at
zero need not obey the displayed rotation step.  The standard-convention or
generic-phase identity is sufficient to show that classical noncontinuation
does not imply failure of an Euler-selected occupation limit.

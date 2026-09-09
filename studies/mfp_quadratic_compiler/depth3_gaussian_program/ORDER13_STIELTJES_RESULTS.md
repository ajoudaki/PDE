# Depth-3 order-thirteen derivative and six-moment Stieltjes result

## Bottom line

The two additional moments were computed exactly.  Both are positive, and
every principal minor of the newly completed ordinary and shifted
(3\times3) Hankel matrices is strictly positive:

\[
H_2\succ0,
\qquad
H_2^+\succ0.
\]

Therefore the raw-quadratic three-hidden-layer model remains compatible with
every Stieltjes condition decidable from the feature jet through order
thirteen.  This is a six-moment result, not an all-order proof.

## New exact feature derivatives

The two exact coefficient routes agree on

\[
\boxed{
F^{(11)}(0)
=4\,838\,138\,568\,305\,355\,772\,330\,223\,426\,228\,537\,958\,334\,464
}
\]

and

\[
\boxed{
F^{(13)}(0)
=1\,123\,706\,942\,060\,914\,791\,445\,507\,530\,161\,609\,246\,735\,618\,530\,394\,112.
}
\]

Orders ten and twelve vanish exactly.  The full accepted order-nine prefix is
unchanged.

## Six exact Stieltjes moments

For

\[
K(y)=F'\!\left(F^{-1}(y)\right)
=14\,175+\sum_{r\ge0}(-1)^r\mu_r y^{2r+2},
\]

the moment prefix is

| moment | exact value | decimal |
|---|---:|---:|
| (\mu_0) | (95641312/275625) | 346.99795736961454 |
| (\mu_1) | (3963629647049188/3230587705078125) | 1.2269066835173064 |
| (\mu_2) | (12164741271894434633792/601040746943206787109375) | 0.020239461856392072 |
| (\mu_3) | (4206861574840394358968837051264/9862678589590839304447174072265625) | 0.00042654351316693563 |
| (\mu_4) | (52706019439078857802390858812108565605376/5201999704599090318757481910288333892822265625) | (1.0131876668982015\times10^{-5}) |
| (\mu_5) | (101941467717521925959195647155186172639980128272/394295321359534174004571011668886058032512664794921875) | (2.5854090118550416\times10^{-7}) |

In particular, every available moment sign is strict.

## New ordinary Hankel decision

The exact full determinant is

\[
\det H_2
=\frac{
307594062486287708470348618146958047797145928662386034696990888626634752
}{
54291694295880760637974956015823843147891242466585026704706251621246337890625
}
=5.6655823045409286\times10^{-6}>0.
\]

All three diagonal minors and all three two-index principal minors are also
strictly positive.  Thus all seven nonempty principal minors pass and
(H_2\succ0).  Its approximate eigenvalues are

\[
1.02628\times10^{-6},
\qquad 1.59091\times10^{-2},
\qquad 3.47002\times10^2.
\]

## New shifted Hankel decision

The exact full determinant is

\[
\det H_2^+
=\frac{
149727900958810667809124859762487199827666057549067484722050515755971792446448013698208883236864
}{
192329039679037943937909881893529487162630437749805012254101434124135827641310925173456780612468719482421875
}
=7.784986667051382\times10^{-13}>0.
\]

Again every diagonal and two-index principal minor is strictly positive, so
all seven principal-minor checks pass and (H_2^+\succ0).  Its approximate
eigenvalues are

\[
6.83973\times10^{-9},
\qquad 9.27448\times10^{-5},
\qquad 1.22724.
\]

The small minimum eigenvalue is only a conditioning diagnostic; the sign is
certified by exact rational principal minors.

Across (H_0,H_1,H_2,H_0^+,H_1^+,H_2^+), all 22 enumerated nonempty
principal-minor checks are strictly positive.

## Validation, resources, and provenance

The derivative jet was independently assembled in ordinary-Taylor and
derivative-normalized/binomial coordinates.  The full vectors agree exactly
through order thirteen.  The two production routes took 13:16 and 13:04,
with peak resident memory 244,648 KiB and 243,616 KiB respectively.  The
largest order-thirteen carrier contained 3,418 monomials.

The moments were then reproduced by two exact transformations:

1. rational series reversion and composition;
2. the triangular identity (F'(t)=K(F(t))), without constructing the
   inverse series.

A source-hash gate detected a one-byte change between the frozen baseline and
the order-thirteen production source.  Recursive comparison against the
pre-change compiled program showed identical bytecode, constants, names,
variable layouts, flags, and line tables for every code object.  Both
order-thirteen routes used the recorded executed-source hash, and the change
is classified as semantically inert whitespace rather than silently ignored.

## Exact cutoff and claim boundary

The next ordinary matrix (H_3) needs (\mu_6), hence (F^{(15)}(0)).  The
next shifted matrix (H_3^+) needs (\mu_7), hence (F^{(17)}(0)).  Neither
is decided here.

The result proves exact six-moment compatibility for the stated width-first
formal jet.  It does not prove the all-order Stieltjes conjecture, existence
of a representing measure for an unknown infinite sequence, series
convergence, or a positive-time mean-field limit.


# Architecture derivative and Stieltjes-moment ledger

## Scope and convention

This ledger distinguishes the core architecture sweep from the older
continuous metric, centering, and input-geometry campaigns.  A hidden-layer
count of two means two nonlinear hidden layers, not one hidden layer plus a
readout.

For every nondegenerate scalar channel, the convention is

\[
K(y)=F'(F^{-1}(y))
=F'(0)+\sum_{r\ge0}(-1)^r\mu_r y^{2r+2},
\]

with Hankel matrices

\[
H_d=(\mu_{i+j})_{i,j=0}^d,
\qquad
H_d^+=(\mu_{i+j+1})_{i,j=0}^d.
\]

Readout reflection makes every core feature jet odd, so all displayed even
derivatives, including \(F(0)\), are zero.

## Executive comparison

| configuration | latest accepted feature jet | moments determined | strongest accessible Stieltjes result |
|---|---:|---:|---|
| one input, raw \(x^2\), 2 hidden layers | \(F^{(17)}\) | \(\mu_0,\ldots,\mu_7\) | all ordinary/shifted matrices through \(H_3,H_3^+\) positive definite |
| one input, raw \(x^2\), 3 hidden layers | \(F^{(13)}\) | \(\mu_0,\ldots,\mu_5\) | all ordinary/shifted matrices through \(H_2,H_2^+\) positive definite |
| one input, raw \(x^3\), 2 hidden layers | \(F^{(9)}\) | \(\mu_0,\ldots,\mu_3\) | \(H_1\succ0\), but \(H_1^+\) is indefinite: exact violation |
| one input, raw or unit-variance sine, 2 hidden layers | \(F^{(9)}\) | \(\mu_0,\ldots,\mu_3\) | all six accessible scalar PSD inequalities fail for both scalings |
| two inputs, equal labels, raw \(x^3\), 2 hidden layers, plus channel | symbolic \(F_+^{(5)}(\rho)\) | \(\mu_0(\rho),\mu_1(\rho)\) | both are strictly positive for every \(-1<\rho\le1\); no \(2\times2\) determinant is yet available |
| one input, raw \(x^2\), 1 hidden layer | \(F^{(13)}\) | \(\mu_0,\ldots,\mu_5\) | shifted \(H_2^+\) has an exact negative determinant |
| one input, normalized centered Hermite \(H_2\), 1 hidden layer | \(F^{(13)}\) | \(\mu_0,\ldots,\mu_5\) | shifted \(H_2^+\) has an exact negative determinant; the other 22 accessible minors are positive |
| one input, identity \(x\), 1 hidden layer | all orders; displayed through \(F^{(13)}\) | all \(\mu_r=C_r/4^r\) | explicit measure on \((0,1)\); \(H_d,H_d^+\succ0\) for every \(d\) |
| one input, identity \(x\), 2 hidden layers | exact formal spectral recursion; computed through \(F^{(81)}\) | \(\mu_0,\ldots,\mu_{39}\) | \(H_d,H_d^+\succ0\) for \(0\le d\le19\); all-order Stieltjes positivity remains open |
| one input, identity \(x\), 3 hidden layers | \(F^{(13)}\) | \(\mu_0,\ldots,\mu_5\) | all ordinary/shifted matrices through \(H_2,H_2^+\) positive definite; all 23 accessible Hankel minors strictly positive |

The finite-order pattern is therefore architecture-dependent.  Raw-square
depth two and three and the three identity controls pass every currently
accessible condition; raw cubic and sine fail; the present two-input cubic
calculation has not yet reached a discriminating two-by-two determinant.

## 1. One input, raw quadratic, two hidden layers

All parameter blocks train with the equal metric.  The exact nonzero
derivatives are

\[
\begin{aligned}
F^{(1)}(0)&=111,\\
F^{(3)}(0)&=1685184,\\
F^{(5)}(0)&=77400633120,\\
F^{(7)}(0)&=7315868433079296,\\
F^{(9)}(0)&=1181161141825400561664,\\
F^{(11)}(0)&=291982832387585872335470592,\\
F^{(13)}(0)&=102853512279246664353620526022656,\\
F^{(15)}(0)&=49079184579077107476764629402991788032,\\
F^{(17)}(0)&=30555969894096099495444855650521777374167040.
\end{aligned}
\]

The exact moments are

| moment | exact value | decimal |
|---|---:|---:|
| \(\mu_0\) | \(280864/4107\) | \(68.3866569272\) |
| \(\mu_1\) | \(38443196932/5616860517\) | \(6.84424988223\) |
| \(\mu_2\) | \(37578479127292096/12802987609542045\) | \(2.93513360110\) |
| \(\mu_3\) | \(21749547365571716077696/13618704359108797313085\) | \(1.59703498894\) |
| \(\mu_4\) | \(2463577914969508668234788122624/2514423905282563683042386470725\) | \(0.979778274377\) |
| \(\mu_5\) | \(43091400402899303445912484475500496/66714012134145460981362191472284175\) | \(0.645912290753\) |
| \(\mu_6\) | \(233701098505506644778710348585571696126248608/523079786422749003601451969851378666466523525\) | \(0.446779066161\) |
| \(\mu_7\) | \(70048496819304110407804100699554764688052780719822/218993917770958359962588987442799241938248378067125\) | \(0.319865033387\) |

Every principal minor accessible through \(H_3\) and \(H_3^+\) is strictly
positive.  The complete exact certificate is
[`F17_MOMENT_HANKEL_AUDIT.json`](../stieltjes_conjecture/resolution_program/canonical_high_order/F17_MOMENT_HANKEL_AUDIT.json).

## 2. One input, raw quadratic, three hidden layers

The exact nonzero derivatives are

\[
\begin{aligned}
F^{(1)}(0)&=14175,\\
F^{(3)}(0)&=139445032896,\\
F^{(5)}(0)&=4298284752832899360,\\
F^{(7)}(0)&=272967464957028310013451264,\\
F^{(9)}(0)&=29466555372596241677766026853605376,\\
F^{(11)}(0)&=4838138568305355772330223426228537958334464,\\
F^{(13)}(0)&=1123706942060914791445507530161609246735618530394112.
\end{aligned}
\]

The six exact moments are

| moment | exact value | decimal |
|---|---:|---:|
| \(\mu_0\) | \(95641312/275625\) | \(346.997957369615\) |
| \(\mu_1\) | \(3963629647049188/3230587705078125\) | \(1.22690668351731\) |
| \(\mu_2\) | \(12164741271894434633792/601040746943206787109375\) | \(0.0202394618563921\) |
| \(\mu_3\) | \(4206861574840394358968837051264/9862678589590839304447174072265625\) | \(0.000426543513166936\) |
| \(\mu_4\) | \(52706019439078857802390858812108565605376/5201999704599090318757481910288333892822265625\) | \(1.01318766689820\times10^{-5}\) |
| \(\mu_5\) | \(101941467717521925959195647155186172639980128272/394295321359534174004571011668886058032512664794921875\) | \(2.58540901185504\times10^{-7}\) |

All 22 enumerated nonempty principal-minor conditions across the available
ordinary and shifted Hankel matrices are strictly positive; in particular
\(H_2\succ0\) and \(H_2^+\succ0\).  See
[`ORDER13_STIELTJES_RESULTS.md`](quadratic_compiler/depth3_gaussian_program/ORDER13_STIELTJES_RESULTS.md).

## 3. One input, raw cubic, two hidden layers

The exact nonzero derivatives are

\[
\begin{aligned}
F^{(1)}(0)&=305775,\\
F^{(3)}(0)&=154118008098000,\\
F^{(5)}(0)&=302467842967104331335000,\\
F^{(7)}(0)&=1412600607141756021360853290900000,\\
F^{(9)}(0)&=12844661809234735951068178383554688801750000.
\end{aligned}
\]

The exact moments are

| moment | exact value | decimal |
|---|---:|---:|
| \(\mu_0\) | \(93960072/114005\) | \(824.175009867988\) |
| \(\mu_1\) | \(5787193487251/147192610783125\) | \(0.0393171468082586\) |
| \(\mu_2\) | \(8262390512438071457518/25655582915973781969921875\) | \(3.22050391117549\times10^{-4}\) |
| \(\mu_3\) | \(2636622646388500249440493088029/5564847635936495462248842835546875000\) | \(4.73799611216991\times10^{-7}\) |

Every moment is positive and

\[
\mu_0\mu_2-\mu_1^2>0,
\]

but the first shifted determinant is exactly negative:

\[
\mu_1\mu_3-\mu_2^2
=-
\frac{3136318387543181669964663532850762952758515589}
{36859700346470723980544924489290665938162841796875000}<0.
\]

Thus \(H_1\succ0\) while \(H_1^+\) is indefinite.  See
[`STIELTJES_RESULTS.md`](cubic_compiler/depth2_gaussian_program/STIELTJES_RESULTS.md).

## 4. One input, sine, two hidden layers

Both raw sine and the unit-Gaussian-variance scaling

\[
\phi(x)=\sqrt{\frac{2}{1-e^{-2}}}\sin x
\]

were computed through order nine.  The nonzero derivatives are

| order | raw \(\sin x\) | unit-variance sine |
|---:|---:|---:|
| 1 | \(1\) | \(4.0370969464656417700\) |
| 3 | \(-1.8869998273059311009\) | \(-103.25733114677418891\) |
| 5 | \(79.414989816144653057\) | \(29944.432342937282364\) |
| 7 | \(-7186.1902521245980087\) | \(-22072427.427508219184\) |
| 9 | \(1194738.0652021462630\) | \(31624398864.162903963\) |

The moments are

| moment | raw sine | unit-variance sine |
|---|---:|---:|
| \(\mu_0\) | \(-0.94349991365296555044\) | \(-3.1677619860813018563\) |
| \(\mu_1\) | \(-2.7154965176305915777\) | \(-3.0399973783784623538\) |
| \(\mu_2\) | \(-5.2226030922470658063\) | \(-2.2096699492914202258\) |
| \(\mu_3\) | \(-7.8931446516883407295\) | \(-1.5977968448910770624\) |

For both scalings, all four moment signs and both two-by-two determinants
\(\mu_0\mu_2-\mu_1^2\) and \(\mu_1\mu_3-\mu_2^2\) are negative.  Hence
\(H_0,H_0^+,H_1,H_1^+\) are all non-PSD.  These are certified
high-precision finite-Fourier values rather than rational numbers.  The
80- and 100-digit routes agree; see
[`ORDER9_RESULTS.md`](sine_compiler/depth2_gaussian_program/ORDER9_RESULTS.md).

## 5. Two inputs, equal labels, raw cubic, two hidden layers

For unit-RMS inputs with Gram matrix

\[
Q(\rho)=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},
\]

the exact plus-channel jet is available through order five:

\[
F_+^{(0)}=F_+^{(2)}=F_+^{(4)}=0.
\]

The complete expanded polynomials \(F_+^{(1)}(0;\rho)\),
\(F_+^{(3)}(0;\rho)\), and \(F_+^{(5)}(0;\rho)\) are listed in
[`ORDER5_SYMBOLIC_RESULTS.md`](cubic_compiler/two_input_plus_gaussian_program/ORDER5_SYMBOLIC_RESULTS.md),
with machine-readable coefficient lists in
[`results_symbolic_order5.json`](cubic_compiler/two_input_plus_gaussian_program/results_symbolic_order5.json).

With the exact factorizations

\[
F_+^{(1)}=\frac{81}{2}(1+\rho)A,
\qquad
F_+^{(3)}=39366(1+\rho)^2P,
\]

and

\[
4(F_+^{(3)})^2-F_+^{(1)}F_+^{(5)}
=\frac{387420489}{4}(1+\rho)^4N,
\]

the two available moments are

\[
\boxed{\mu_0(\rho)=\frac{12P(\rho)}{A(\rho)^2}},
\qquad
\boxed{\mu_1(\rho)=\frac{N(\rho)}{27(1+\rho)A(\rho)^5}}.
\]

Exact Sturm sequences prove \(A,P,N>0\) on \([-1,1]\).  Consequently

\[
\mu_0(\rho)>0,
\qquad
\mu_1(\rho)>0,
\qquad -1<\rho\le1.
\]

| \(\rho\) | \(\mu_0\) | \(\mu_1\) |
|---:|---:|---:|
| \(0\) | \(47090556/114005\) | \(9007737597469/441577832349375\) |
| \(1/2\) | \(146249888/319225\) | \(2226187969218708704/91794899448972309375\) |
| \(1\) | \(93960072/114005\) | \(5787193487251/147192610783125\) |

Therefore the only decidable matrices, \(H_0=[\mu_0]\) and
\(H_0^+=[\mu_1]\), are positive definite for every nondegenerate
correlation.  Their signs are correlation-independent.  At \(\rho=-1\),
the plus feature is zero and the inverse-coordinate moments are undefined.
The determinant of \(H_1\) requires \(\mu_2\), hence \(F_+^{(7)}\), and is
not available.

The exact polynomial coefficients and Sturm data are in
[`stieltjes_order5_audit.json`](cubic_compiler/two_input_plus_gaussian_program/stieltjes_order5_audit.json).

## 6. One input, raw quadratic, one hidden layer

This distinct shallow architecture was obtained as an exact reduction of a
block-metric boundary and then rescaled to the conventional iid model.  Its
nonzero derivatives are

\[
\begin{aligned}
F^{(1)}(0)&=7,&
F^{(3)}(0)&=960,&
F^{(5)}(0)&=376608,\\
F^{(7)}(0)&=326323200,&
F^{(9)}(0)&=527514808320,\\
F^{(11)}(0)&=1428258510766080,&
F^{(13)}(0)&=6004476167091978240.
\end{aligned}
\]

Its moments are

\[
\begin{aligned}
\mu_0&=\frac{480}{49},&
\mu_1&=\frac{43756}{16807},&
\mu_2&=\frac{7214528}{2470629},\\
\mu_3&=\frac{37635527904}{9886633715},&
\mu_4&=\frac{171752915595136}{30520038278205},&
\mu_5&=\frac{2199776554157960896}{246754509479287425}.
\end{aligned}
\]

The shifted three-by-three determinant is

\[
\det H_2^+
=-
\frac{86245462994269879146938487857152}
{516623655319449980325461333747775}<0.
\]

This is an exact formal Stieltjes counterexample.  See
[`SHALLOW_QUADRATIC_CERTIFICATE.json`](../stieltjes_conjecture/resolution_program/SHALLOW_QUADRATIC_CERTIFICATE.json).

## 7. One input, normalized centered Hermite-2, one hidden layer

For

\[
\phi(x)=\frac{x^2-1}{\sqrt2},
\]

the exact nonzero derivatives are

\[
3,\ 192,\ 38592,\ 16882272,\ 13710887424,\
18618267830400,\ 39219558574625280
\]

at orders \(1,3,5,7,9,11,13\), respectively.  The moments are

\[
\left(
\frac{32}{3},\frac{440}{81},\frac{160738}{10935},
\frac{30517412}{688905},\frac{85823505179}{558013050},
\frac{13556868117611}{23675696550}
\right).
\]

All six moments and every accessible one- and two-dimensional Hankel minor
are positive, but

\[
\det H_2^+
=-\frac{515758203187135106171912}
        {485517025870694173125}<0.
\]

Hence normalized centering does not repair the shallow raw-square
counterexample.  See
[RESULTS.md](quadratic_compiler/centered_depth1_order13/RESULTS.md).

## 8. One input, identity activation, one, two, and three hidden layers

At depth one the flow is exactly solvable:

\[
F_1(t)=\sinh(2t),
\qquad
F_1^{(2k)}(0)=0,
\qquad
F_1^{(2k+1)}(0)=2^{2k+1}.
\]

The output-coordinate moments satisfy

\[
\mu_{r,1}=\frac{C_r}{4^r}
=\int_0^1x^r\frac2\pi\sqrt{\frac{1-x}{x}}\,dx.
\]

Consequently \(H_{d,1},H_{d,1}^+\succ0\) for every \(d\ge0\).  The exact
order-thirteen certificate is
[`DEPTH1_ORDER13_RESULTS.md`](identity_compiler/linear_gaussian_program/DEPTH1_ORDER13_RESULTS.md).

At depth two, an independent Gram-invariant/Wishart derivation now gives an
exact all-fixed-order spectral recursion.  It has been evaluated and matched
against both detransposition routes through order 81, determining
\(\mu_0,\ldots,\mu_{39}\).  Exact rational determinants give

\[
H_{d,2}\succ0,\qquad H_{d,2}^+\succ0,
\qquad 0\le d\le19.
\]

No elementary scalar formula for \(F_2\) or \(K_2\), representing measure,
or all-order Hankel-sign proof is presently known.  The exact spectral
closure and coefficient files are in
[depth2_all_order_search/RESULTS.md](identity_compiler/linear_gaussian_program/depth2_all_order_search/RESULTS.md).

Separately from the coefficient and Stieltjes questions, the one-sample
identity model now has an autonomous rooted-path equation at every fixed
hidden depth.  It is a gradient ODE on two endpoint Hilbert vectors, one
trainable Hilbert--Schmidt block operator, and one residual, driven by a
single deterministic rooted-path creation--annihilation source.  It gives
`K(0)=L+1` and drives its residual exponentially to zero.  Positive-time
finite-width convergence is rigorous at depths one and two.  At depth three
and beyond, the path equation retains the required noncommuting mixed words,
but its finite-width identification remains conditional on the multi-edge
rooted-word and coefficient-lift lemmas.  See
[CANONICAL_NOTE.md](identity_compiler/linear_gaussian_program/arbitrary_depth_autonomous_mse_closure/CANONICAL_NOTE.md).

At depth three, the current exact endpoint remains order thirteen.

The identity-specific linear-Gaussian detransposition recurrence gives

\[
F_2^{(13)}(0)=109038689280,
\qquad
F_3^{(13)}(0)=111466749771776.
\]

The exact six-moment prefixes are

\[
\begin{aligned}
(\mu_{r,2})_{r=0}^5
&=\left(
\frac83,\frac{67}{81},\frac{6832}{10935},
\frac{414716}{688905},\frac{182387864}{279006525},
\frac{63196828537}{82864937925}
\right),\\
(\mu_{r,3})_{r=0}^5
&=\left(
5,\frac{61}{32},\frac{11131}{5760},
\frac{3235483}{1290240},\frac{852431627}{232243200},
\frac{314669435827}{54499737600}
\right).
\end{aligned}
\]

For the six-moment prefix displayed above, every one of the 23 distinct
accessible square Hankel minors is strictly positive at both depths.  In
particular,

\[
\det H_{2,2}^+
=\frac{4662092676191348}{2157853448314196325}>0,
\]

\[
\det H_{2,3}^+
=\frac{114573182642874004393}{708802833725521920000}>0.
\]

The full certificate is
[`ORDER13_RESULTS.md`](identity_compiler/linear_gaussian_program/ORDER13_RESULTS.md).

## 9. Broader parameter and input-geometry variants

These are continuum families rather than additional fixed core points.  Their
full polynomial coefficient arrays are large; the linked JSON files are the
exact derivative and moment lists rather than interpolated summaries.

| family | exact derivative endpoint | moments/Hankel result | authoritative coefficient source |
|---|---:|---|---|
| quadratic depth 2, relative metric \(D_a+\lambda(D_u+D_W)\), \(\lambda\ge0\) | \(F^{(9)}(\lambda)\) | \(\mu_0,\ldots,\mu_3\); ordinary and shifted \(2\times2\) tests nonnegative on the full ray, strict after removing forced powers | [`results_order9_q2_order8.json`](quadratic_compiler/campaign1/results_order9_q2_order8.json), [`hankel_certificates_order9_q2_order8.json`](quadratic_compiler/campaign1/hankel_certificates_order9_q2_order8.json) |
| quadratic depth 2, two inputs, equal/opposite label symmetry channels, \(t=\rho^2\in[0,1]\) | both channels through \(F^{(7)}(t)\) | \(\mu_0,\mu_1,\mu_2\) and ordinary \(H_1\) positive throughout each nondegenerate channel | [`certificates_order7.json`](quadratic_compiler/campaign2/certificates_order7.json) |
| quadratic depth 2 with first activation \(u^2-c\), \(0\le c\le2\) | \(F^{(7)}(c)\) | \(\mu_0,\mu_1,\mu_2\) and ordinary \(H_1\) positive by exact Sturm isolation | [`certificates_order7.json`](quadratic_compiler/campaign3/certificates_order7.json) |
| quadratic depth 2, independent metrics \(D_a+\alpha D_u+\beta D_W\) | full quadrant through \(F^{(9)}\); slice \(\beta=1\) through \(F^{(13)}\) | full-quadrant four-moment tests pass; on \(\beta=1\), shifted \(H_2^+\) changes sign once at \(\alpha_*=0.017519225541486\ldots\) and is negative below it | [`results_order9.json`](quadratic_compiler/campaign4/results_order9.json), [`ALPHA_TRANSITION_CERTIFICATE.json`](../stieltjes_conjecture/resolution_program/ALPHA_TRANSITION_CERTIFICATE.json) |
| quadratic depth 2, three equicorrelated equal-label inputs, \(-1/2\le\rho\le1\) | symbolic \(F^{(5)}(\rho)\) | \(\mu_0,\mu_1>0\) throughout; no \(\mu_2\) or Hankel determinant | [`stage_b_connected_order5.json`](quadratic_compiler/campaign5_b3/frozen/stage_b_connected_order5.json), [`certificates_lower_moments.json`](quadratic_compiler/campaign5_b3/certificates_lower_moments.json) |

Hidden-layer norm responses \(Q_1,Q_2\) were also studied, but they are
observables of the canonical architecture rather than separate network
architectures, so they are not counted as additional rows here.

## Claim boundary

Every derivative and rational moment above is an accepted fixed-order,
width-first formal coefficient under its stated compiler assumptions.  The
separate identity result supplies a positive-time width limit at hidden
depths one and two; its arbitrary-depth rooted-path equation is conditional
as a network width limit from depth three onward.  Neither statement upgrades
the nonlinear rows.  The
sine values are independently stabilized high-precision constants.  Passing
a finite collection of Hankel conditions does not prove an infinite
Stieltjes moment sequence or a representing measure.  Conversely, one
negative principal minor is already a decisive finite-order disproof for that
specific configuration.

# Canonical orders 15 and 17: exact downstream audit

The downstream checker described in this note begins **after** the
fixed-order width-limit feature derivative has been computed and imports
neither recurrence implementation.  The directory now also retains the two
independent Gaussian-program recurrence implementations that supplied
\(F^{(15)}(0)\) and \(F^{(17)}(0)\).  The checker's purpose is to turn those
independently supplied values into exact Stieltjes moments and decisive
finite Hankel gates.

## Exact transformation

Put

\[
F(s)=\sum_{j\geq0}\frac{F^{(2j+1)}(0)}{(2j+1)!}s^{2j+1},
\qquad G=F^{-1}.
\]

The checker solves (F(G(y))=y) directly and coefficient by coefficient.
This is algebraically separate from the Lagrange-coefficient calculation in
the earlier scalar certificate.  If

\[
G(y)=\sum_{j\geq0}b_jy^{2j+1},
\]

then the inverse-function identity gives

\[
H(x):=G'(\sqrt{x})=\sum_{j\geq0}(2j+1)b_jx^j,
\qquad
K(\sqrt{x})=\frac1{H(x)}.
\]

Finally,

\[
\frac{K(\sqrt{x})-111}{x}
=\sum_{r\geq0}(-1)^r\mu_rx^r.
\]

Consequently, a feature jet through order (2m+1) determines exactly
(mu_0,\ldots,\mu_{m-1}).  The no-candidate baseline reproduces all six
retained moments through (mu_5), the ordinary (H_2) determinant, and the
shifted (H_2^+) determinant exactly.

## Which new gates become decidable

The two Stieltjes Hankel families are

\[
H_d=(\mu_{i+j})_{i,j=0}^d,
\qquad H_d^+=(\mu_{i+j+1})_{i,j=0}^d.
\]

- (F^{(15)}(0)) determines (mu_6).  This completes the new ordinary
  matrix (H_3).  It does not complete a new shifted leading matrix.
- (F^{(17)}(0)), after (F^{(15)}(0)) is fixed, determines (mu_7).
  This completes the new shifted matrix (H_3^+).  It does not complete a
  larger ordinary leading matrix.

Both already-known leading blocks (H_2) and (H_2^+) are positive
definite.  Therefore Schur complementation gives the exact one-number gates

\[
H_3\succeq0
\iff
\mu_6\geq
(\mu_3,\mu_4,\mu_5)H_2^{-1}(\mu_3,\mu_4,\mu_5)^T,
\]

and, once (mu_6) is known,

\[
H_3^+\succeq0
\iff
\mu_7\geq
(\mu_4,\mu_5,\mu_6)(H_2^+)^{-1}
(\mu_4,\mu_5,\mu_6)^T.
\]

Strict inequality is equivalent to positive definiteness.  Equality gives a
singular PSD boundary point.  The checker additionally evaluates every
principal minor exactly, using the equivalent criterion that a real
symmetric matrix is PSD if and only if all its principal minors are
nonnegative.

## The exact order-15 threshold already fixed by the lower jet

Write (D_{15}=F^{(15)}(0)).  Direct reversion gives

\[
\mu_6=
\frac{226869297289864083824909005077739993968922624}
{523079786422749003601451969851378666466523525}
+\frac{D_{15}}{3757768789970820943591091480362359859200}.
\]

Moreover,

\[
\det H_3=S_{15}(D_{15}-T_{15}),\qquad S_{15}>0,
\]

where

\[
S_{15}=
\frac{20641491091032025540248097723997716702728718990976}
{5094410332201190488374752306408422667366822785750866457994568078649808565366230137021875}
\]

and

\[
T_{15}=
\frac{65743393265975731179732223336891159131752625282961983545652912901909389532771651702960445629216}
{2068766359898401991928790497752880265620760807729959214265}
=3.1779032441925639961\ldots\times10^{37}.
\]

Thus an integer candidate passes the ordinary gate strictly exactly when

\[
D_{15}\geq31779032441925639961712357466606778022.
\]

At order 17, for every fixed exact (D_{15}), the dependence remains affine:

\[
\mu_7=A(D_{15})-
\frac{F^{(17)}(0)}
{11111872622695316363036601151090712598048768000}.
\]

The script reports the exact (A(D_{15})), the corresponding shifted Schur
threshold, and the exact rational threshold for (F^{(17)}(0)) as soon as
the order-15 candidate is supplied.

## Accepted order-15 candidate and the now-fixed order-17 gate

The production finite Gaussian-program recurrence and an isolated direct
recurrence independently returned

\[
F^{(15)}(0)=49079184579077107476764629402991788032.
\]

The downstream audit gives

\[
\mu_6=
\frac{233701098505506644778710348585571696126248608}
{523079786422749003601451969851378666466523525}
=0.44677906616072378627\ldots
\]

and

\[
\det H_3=
\frac{4581116513595315356583611738530988438162599733688069549013816754981347215833268704400090246049792}
{65354315638055287686313547406928749888486398559119734829544762489701014494772697096643566490984375}
=0.07009661823966477867\ldots>0.
\]

All fifteen nonempty principal minors of (H_3) are strictly positive, so
(H_3\succ0).  Thus order 15 passes and canonical V1 remains open at this
stage.

With this exact (F^{(15)}(0)), the shifted order-17 gate is already fixed:

\[
\det H_3^+=S_{17}\bigl(T_{17}-F^{(17)}(0)\bigr),
\qquad S_{17}>0,
\]

where

\[
T_{17}=
\frac{2550870853167034001774061594388073398846068167352515912017809538084093132174994109476581979070018701945005827157043621986304}
{65418790831788537569754007055275766906562138498125646972227866906007860848130625}
=3.8992937972915047034\ldots\times10^{43}.
\]

Therefore an integer order-17 candidate passes the shifted gate exactly when

\[
F^{(17)}(0)\leq38992937972915047033656940766562738478024369.
\]

The retained full order-15 reconstruction, including every principal minor,
is `F15_MOMENT_HANKEL_AUDIT.json`.

The production and isolated recurrences subsequently agreed exactly on

\[
F^{(17)}(0)=30555969894096099495444855650521777374167040.
\]

This gives the eighth output-kernel moment

\[
\mu_7=
\frac{70048496819304110407804100699554764688052780719822}
{218993917770958359962588987442799241938248378067125}
=0.31986503338675607532\ldots
\]

and

\[
\det H_3^+=
\frac{137984062500683379206705700665534552146154930313101025462488622111967390693657363652277493269175099282762503439873283096576}
{4841427533479109861977652240500543777398925508758255281888009610895813561244370117263221332603626422004447587045586035469140625}
=2.8500697686065812\ldots\times10^{-5}>0.
\]

All fifteen nonempty principal minors of (H_3^+) are strictly positive.
Therefore both newly available matrices satisfy

\[
H_3\succ0,\qquad H_3^+\succ0.
\]

Every canonical Stieltjes condition decidable from
(mu_0,\ldots,\mu_7) passes strictly.  This extends finite-order
compatibility by two moments but does not prove canonical V1.  The retained
complete order-17 certificate is `F17_MOMENT_HANKEL_AUDIT.json`.

## Claim update rules

- A negative principal minor of (H_3) or (H_3^+) is an exact finite
  witness that canonical V1 is false.
- If the new matrix is positive definite, that order passes but canonical V1
  remains open: finitely many positive Hankel matrices do not establish the
  all-order Stieltjes property.
- A PSD-singular outcome is not by itself a refutation.  It places the
  sequence on a finite-support boundary and makes consistency of later
  moments especially restrictive.

Run the retained baseline with

```bash
python moment_hankel_audit.py
```

and audit candidates with

```bash
python moment_hankel_audit.py --f15 EXACT_INTEGER
python moment_hankel_audit.py --f15 EXACT_INTEGER --f17 EXACT_INTEGER
```

The JSON output contains every available ordinary and shifted matrix gate,
all principal minors, the affine highest-derivative formulas, and the exact
V1 finite-prefix verdict.

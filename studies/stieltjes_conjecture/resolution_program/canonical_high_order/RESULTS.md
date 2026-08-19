# Canonical feature jet through order seventeen

Status: **accepted exact finite-order computation**, 18 August 2026.

## Result

For the canonical one-input quadratic network with block metric

\[
D_{1,1}=D_a+D_u+D_W,
\]

the proved fixed-order Gaussian-program recurrence gives

\[
\boxed{F^{(15)}(0)
=49\,079\,184\,579\,077\,107\,476\,764\,629\,402\,991\,788\,032}
\]

and

\[
\boxed{F^{(17)}(0)
=30\,555\,969\,894\,096\,099\,495\,444\,855\,650\,521\,777\,374\,167\,040}.
\]

Every accepted derivative through order thirteen was reproduced exactly
before either new value was accepted, and every even derivative through
order sixteen is exactly zero.  An isolated production recurrence and an
independent recurrence with a separate sparse representation and Wick engine
return the same two integers.

## New moments and Hankel gates

Exact coefficientwise inversion of $F$, followed by the canonical
output-kernel transformation, gives

\[
\boxed{\mu_6=
\frac{233701098505506644778710348585571696126248608}
{523079786422749003601451969851378666466523525}}
\]

and

\[
\boxed{\mu_7=
\frac{70048496819304110407804100699554764688052780719822}
{218993917770958359962588987442799241938248378067125}}.
\]

They complete the ordinary and shifted $4\times4$ leading matrices

\[
H_3=(\mu_{i+j})_{i,j=0}^3,
\qquad
H_3^+=(\mu_{i+j+1})_{i,j=0}^3.
\]

Their exact determinants are

\[
\boxed{\det H_3=
\frac{4581116513595315356583611738530988438162599733688069549013816754981347215833268704400090246049792}
{65354315638055287686313547406928749888486398559119734829544762489701014494772697096643566490984375}>0}
\]

and

\[
\boxed{\det H_3^+=
\frac{137984062500683379206705700665534552146154930313101025462488622111967390693657363652277493269175099282762503439873283096576}
{4841427533479109861977652240500543777398925508758255281888009610895813561244370117263221332603626422004447587045586035469140625}>0}.
\]

All fifteen nonempty principal minors of each matrix are strictly positive.
Thus

\[
H_3\succ0,
\qquad
H_3^+\succ0.
\]

Every canonical Stieltjes condition decidable from
$(\mu_0,\ldots,\mu_7)$ therefore passes strictly.

## Validation and resources

Both routes use exact rational/integer arithmetic and independently reproduce
the entire accepted prefix through order thirteen and the parity zeros.

| Route | Order-15 checkpoint/run | Complete order-17 run | Peak RSS at order 17 |
|---|---:|---:|---:|
| Production scalar recurrence | 99.000 s checkpoint | 230.318 s | 189.4375 MiB |
| Independent recurrence | 43.59 s standalone | 163.08 s | 94,060 KiB |

The independent order-seventeen resource line includes its full prefix run;
the production order-seventeen line is likewise the complete terminal run,
not an incremental timing after order fifteen.  Both are far below the frozen
30-minute/8-GiB caps.  Exact commands, checkpoints, term counts, cache sizes,
and resource records are retained in
[PRODUCTION_RESULT.json](PRODUCTION_RESULT.json) and
[INDEPENDENT_RESULT.json](INDEPENDENT_RESULT.json).

The moment and Hankel calculation is separately regenerated using standard-
library exact fractions.  [F17_MOMENT_HANKEL_AUDIT.json](F17_MOMENT_HANKEL_AUDIT.json)
contains all moments and every principal minor, rather than only the two
leading determinants displayed above.

## Claim level and stop

This result extends exact fixed-order width-limit compatibility from six to
eight canonical moments.  It does **not** prove that every later Hankel matrix
is positive semidefinite, that the formal series converges, that a global
width-first feature trajectory exists, that a representing measure is
determinate, or that its resolvent equals the actual neural loss curve.
Canonical V1--V3 therefore remain open.

The branch authorized by [PROTOCOL.md](PROTOCOL.md) ended at order seventeen.
Because the order-seventeen calculation passed comfortably, it supplies the
requested optional extension, but no order-nineteen branch was authorized or
attempted.

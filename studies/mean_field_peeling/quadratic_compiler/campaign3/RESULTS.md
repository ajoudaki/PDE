# Campaign 3 result: a centered-activation continuum

## Outcome

Campaign 3 did not falsify the output-kernel Stieltjes conjecture.  It
strengthened the finite-order evidence from one uncentered activation to an
entire signed one-parameter family.

For

$$
\phi_c(u)=u^2-c=(u^2-1)+t,
\qquad t=1-c\in[-1,1],
$$

the exact functions $\mu_0(t),\mu_1(t),\mu_2(t)$ and

$$
\Delta_1(t)=\mu_0(t)\mu_2(t)-\mu_1(t)^2
$$

are strictly positive for every $c\in[0,2]$.  Each claim was proved by exact
Sturm root counting separately on $t\in[-1,0]$ and $t\in[0,1]$, together
with exact positive endpoint values for both the reduced numerator and
denominator.  This is an interval proof, not a sampling experiment.

It remains finite-order evidence.  It neither proves all Hankel matrices
positive nor identifies a global representing measure.

## Why this parameter is nontrivial

The parameter is not an overall output or time scale.  For example,

$$
F'(0;t)=60+44t^2+7t^4,
$$

while

$$
\begin{aligned}
F^{(3)}(0;t)={}&642048+163328t+566784t^2+111104t^3\\
&+163840t^4+18816t^5+18304t^6+960t^8.
\end{aligned}
$$

The odd powers in the higher jet rule out dependence through the even scale
$F'(0;t)$ alone.  More concretely, at $t=-1,0,1$ the pairs

$$
(F'(0),F^{(3)}(0))
$$

are respectively

$$
(111,1098688),\quad(60,642048),\quad(111,1685184).
$$

The two endpoints have the same first speed but different third jets, so no
single removable scaling explains this family.

## Faithful squared-loss reduction

Only the first hidden activation changes.  The one-sample squared loss,
parameter metric, outer quadratic activation, and mean-field scaling are the
same as in the canonical experiment.  Therefore the scalar reduction remains

$$
\dot f=2(1-f)K_c(f),
$$

where $K_c$ is obtained from the feature-ascent curve by

$$
K_c(y)=F_c'(F_c^{-1}(y)).
$$

Whenever the deterministic mean-field feature-ascent curve exists, the
squared-loss flow is exactly a time change of that corresponding path.  At
the formal-jet level the reduction above is exact.  Identifying the formal
$K_c$ with a global mean-field trajectory remains a separate open obligation;
the present finite-order calculation does not establish that theorem.

## Exact feature jets

The first and third derivatives are given above.  The fifth derivative is

$$
\begin{aligned}
F^{(5)}(0;t)={}&20623116288+8334680064t+24298891264t^2\\
&+8086556672t^3+10573467136t^4+2738685952t^5\\
&+2119035904t^6+382585856t^7+211030912t^8\\
&+19952640t^9+12253824t^{10}+376608t^{12}.
\end{aligned}
$$

The seventh derivative is

$$
\begin{aligned}
F^{(7)}(0;t)={}&1364310912663552+720374877585408t\\
&+2063607715266560t^2+914583171006464t^3\\
&+1235346488131584t^4+449483610095616t^5\\
&+375658721345536t^6+108567180951552t^7\\
&+62823078002688t^8+13730120052736t^9\\
&+6060573290496t^{10}+914741020672t^{11}\\
&+364704438272t^{12}+27445149696t^{13}\\
&+14767755264t^{14}+326323200t^{16}.
\end{aligned}
$$

Every even feature derivative through order six is exactly zero.  At $t=1$
the four odd derivatives reproduce the accepted uncentered values

$$
111,\quad1685184,\quad77400633120,\quad7315868433079296.
$$

At the centered endpoint $t=0$, they are

$$
60,\quad642048,\quad20623116288,\quad1364310912663552.
$$

## Exact interval certificates

After cancellation, every denominator factors into positive powers of

$$
t^2+2\quad\text{and}\quad7t^2+30,
$$

times a positive integer.  Nevertheless, the implementation certifies the
denominator as well as the numerator by the same exact Sturm procedure.

The reduced numerator endpoint values are:

| quantity | $t=-1$ | $t=0$ | $t=1$ | roots on each half |
|---|---:|---:|---:|---:|
| $\mu_0$ | 549344 | 321024 | 842592 | 0, 0 |
| $\mu_1$ | 72482173988 | 51439444992 | 345988772388 | 0, 0 |
| $\mu_2$ | 450563216420358592 | 173894792852275200 | 3043856809310659776 | 0, 0 |
| $\Delta_1$ | 221245871831091951242928 | 42594319475183824404480 | 1966188243577911085866672 | 0, 0 |

Here “0, 0” means zero real roots on $[-1,0]$ and zero real roots on
$[0,1]$, computed by exact rational Sturm sequences.  The complete reduced
polynomials, denominator certificates, endpoint variation counts, and Sturm
sequence degrees are stored in `certificates_order7.json`.

## MFP implementation and audits

The centered coordinate

$$
X=u^2-1
$$

is useful computationally, but it changes the terminal calculus.  A column
decorated by $p$ has moment

$$
C_p=\mathbb E[X^p],
$$

with

$$
C_0=1,\qquad C_1=0,\qquad
C_{p+1}=2p(C_p+C_{p-1}).
$$

Zero decorations are retained because they still carry indices and middle
weights.  The rewrites expand each $X+t$ and $X+1$ factor exactly.

Two independent routes were used.

1. `centered_reference.py` retains labelled weight edges and explicitly
   enumerates every Wick pairing.  It is restricted to order three.
2. `centered_connected.cpp` uses the exact connected-tree peeling recursion,
   bridge Leibniz convolution, and surviving vertex partitions.  It uses
   checked unsigned 1024-bit arithmetic.

They agree coefficient-for-coefficient through order three.  The centered
moment recurrence was also checked against direct binomial expansion through
power fourteen.  All ten durable Campaign-3 tests pass.

## Resource record and order-nine decision

The order-seven production run completed under the frozen 4 GiB and
30-minute caps:

| measurement | value |
|---|---:|
| recursion time at order seven | 197.394 s |
| total wall time | 198.35 s |
| peak RSS | 328048 KiB |
| connected value states | 470968 |
| terminal trees | 400945 |

Order nine was not attempted, as precommitted.  State growth from orders
three to five to seven is approximately factors $30$ and $42$.  A naive
monolithic extrapolation gives roughly 20--25 million states, 17--22 million
terminal trees, tens of gigabytes of memory, and multiple CPU-hours.  That
would violate the current memory cap.  Order nine is feasible only after a
sectorized parameter-polynomial implementation, and its likely value is one
additional shifted $2\times2$ determinant.  It is therefore postponed on
information-per-cost grounds rather than classified as failed.

## Durable artifacts

- `PROTOCOL.md`: frozen setup, gates, and resource boundary.
- `centered_reference.py`: transparent labelled-Wick oracle.
- `centered_connected.cpp`: checked production compiler.
- `frozen/results_order7.json`: exact raw feature jets and timings.
- `postprocess.py`: exact reversion and split-interval Sturm certificates.
- `certificates_order7.json`: exact moment/Hankel expressions and certificates.
- `provenance_order7.json`: source, binary, raw-result and certificate hashes,
  commands, measured resources, and validation status.

# Preregistration: middle-query saturation versus bath cancellation

**Frozen before looking at the new outputs:** 23 August 2026.

## Question

The exact middle velocity is

\[
 \dot Z_2=\underbrace{\|X_1\|_n^2B_2}_{S}
 +\underbrace{G_1D_1^2Q_1}_{H},
 \qquad B_2={R_2\over1+Z_2^2}.
\]

A large value of \(|R_{2,i}|\) is dynamically benign if either its gate
\(D_{2,i}\) is small or the self term \(S_i\) moves \(Z_{2,i}\) without a
finely tuned cancellation by the bath \(H_i\).  This diagnostic distinguishes
that saturation/nonalignment mechanism from a persistent slow-tube mechanism.
It is not a proof of either one.

## Simulation fixed in advance

- exact feature-time equations, unscaled arctangent, independent standard
  Gaussian \(A_0,u_0\) and iid \(N(0,1/n)\) bulks;
- explicit midpoint with step \(h=0.01\), float32 state and float64
  aggregation;
- horizons \(T=1,2,4\);
- widths \(n=512,1024,2048,4096\);
- respectively \(64,32,16,8\) independent replicas, so every primary width
  has 32768 coordinate observations;
- master seed `2026082347`, with width/replica-separated deterministic seeds;
- one common-draw step-halving audit at \(n=512\), 16 replicas, \(h=0.005\);
  and one common-draw float64 audit at \(n=256\), 16 replicas.

The primary checkpoint fields are

\[
 R=G_2^*B_3,\quad D=(1+Z_2^2)^{-1},\quad B=DR,
\]
\[
 S=\|X_1\|_n^2B,qquad H=G_1D_1^2Q_1,qquad V=S+H.
\]

For \(L\in\{2,3,4\}\), define the dangerous event

\[
 E_L=\{|R|\ge L,\ D\ge1/2,\ SH<0,
             \ |V|\le |S|/4\}.                                    \tag{P.1}
\]

It requires a large query, a substantially open gate, an opposing bath, and
at least 75-percent instantaneous cancellation of the self motion.

## Primary statistics and frozen interpretation

At every width and horizon, aggregate across all replica coordinates:

1. \(\|R\|_{q,n}\) and \(\|B\|_{q,n}\) for
   \(q=2,4,6,8,12,16\);
2. \(\lambda^{-1}\log\langle e^{\lambda|R|}\rangle_n\) for
   \(\lambda=0.25,0.5,1\);
3. for each \(L\), the tail frequency \(P_L=\Pr\{|R|\ge L\}\), the
   dangerous frequency \(D_L=\Pr(E_L)\), and the conditional fraction
   \(C_L=D_L/P_L\) (reported as missing if the pooled tail count is below
   25);
4. among \(|R|\ge L\), the median gate \(D\), median relative velocity
   \(|V|/(|S|+|H|+10^{-12})\), and the fraction with \(D<1/2\).

The preregistered evidence-against-saturation flag fires if, for any
\((T,L)\) with at least 100 pooled tail observations at both endpoint widths,

\[
 C_L(4096)>0.10
 \quad\hbox{and}\quad
 C_L(4096)/C_L(512)>1.5,                                \tag{P.2}
\]

using the Haldane correction \((D_L+1/2)/(P_L+1)\) for the ratio.  The
formal-support flag requires no evidence-against cell and also requires:

- every central log-width slope of the \(R\) moment roots divided by \(q\)
  to be at most `0.08` for \(q\le12\);
- every \(4096/512\) ratio of those normalized moment roots to be at most
  `1.25`; and
- the dangerous conditional fraction at \(T=4,L=2\) to be below `0.10` at
  width 4096.

The \(q=16\), \(L=3,4\), maxima, and exponential statistics are diagnostic
because the effective independent tail sample is too small to give them a
standalone formal verdict.

## Numerical audit thresholds

For quantities whose pooled denominator is at least 100, the common-draw
step-halving relative discrepancy must be below `0.08`; moment-root and
log-mean-exponential discrepancies must be below `0.04`.  Float32/float64
thresholds are respectively `0.02` for probabilities and `0.01` for moment
or exponential statistics.  The identity residual

\[
 \max_i|V_i-S_i-H_i|
\]

must be below `5e-5` in float32 and `5e-10` in float64.

## Claim boundary

Passing supports a saturation/nonalignment proof search only at ordinary
sampled tail scales.  It cannot exclude a rarer width-dependent cancellation
event, establish a conditional cavity law, prove a moment bound, or change a
contract rung.  Failing rejects this particular empirical mechanism but does
not falsify the mean-field limit.

# Campaign 3: centered quadratic first activation

## Frozen mathematical family

The network, one-sample squared-loss reduction, output quadratic activation,
width scaling, and parameter metric are exactly those of the accepted
one-input experiment.  Only the first hidden activation changes:

$$
\phi_c(u)=u^2-c=X+t,
\qquad X=u^2-1,
\qquad t=1-c.
$$

The tested compact family is $c\in[0,2]$, equivalently $t\in[-1,1]$.
At $t=1$ ($c=0$), the family is the accepted uncentered quadratic model.  At
$t=0$ ($c=1$), the first-hidden feature is exactly centered.

For one sample the ordinary squared-loss gradient flow remains

$$
\dot f=2(1-f)K_c(f),
$$

where $K_c$ is recovered from the feature-ascent jet exactly as in the
canonical experiment.  Thus this is a loss-faithful parameter family, not an
unrelated feature direction.

## Exact MFP grammar

A connected derivative state is a bipartite tree.  Row decorations are
powers of the readout Gaussian $a$; column decorations are powers of $X$;
edges are middle-weight factors.  Column power zero is a real state and must
not be deleted, because the column index and incident weights still remain.

Every affine factor $X+t$ and every derivative factor
$u^2=X+1$ is expanded exactly.  Terminal column moments use

$$
C_0=1,\qquad C_1=0,\qquad
C_{p+1}=2p(C_p+C_{p-1}).
$$

The production contraction enumerates the exact leading-width surviving
vertex partitions.  The transparent oracle instead keeps labelled edges and
enumerates every Wick pairing explicitly.

## Precommitted validity gates

The order-seven output is accepted only if all conditions below pass.

- Every even feature derivative through order six is exactly zero.
- $\deg_t F^{(k)}(0)\le 2(k+1)$ for $k=1,3,5,7$.
- The exact first derivative is

  $$F'(0)=60+44t^2+7t^4.$$

- At $t=1$, orders one, three, five, and seven reproduce the accepted
  uncentered derivatives.
- The transparent labelled-Wick oracle and checked connected compiler agree
  coefficient-for-coefficient through order three.
- The centered endpoint $t=0$ is independently checked through order three.
- Production arithmetic is checked unsigned 1024-bit integer arithmetic;
  overflow throws instead of wrapping.
- Any timeout, memory failure, normalization failure, or provenance mismatch
  makes the result inconclusive rather than evidence for either sign.

After the jet passes, exact reversion constructs $\mu_0,\mu_1,\mu_2$ and

$$
\Delta_1=\mu_0\mu_2-\mu_1^2.
$$

Each rational sign is certified separately on $t\in[-1,0]$ and
$t\in[0,1]$ by exact Sturm root counts and endpoint signs.  Coefficientwise
positivity is not used on the negative half-interval.

## Frozen resource boundary

- Transparent reference: through order three only.
- Production target: through order seven.
- Virtual-memory cap: 4 GiB.
- Wall-clock cap: 30 minutes.
- No order-nine attempt before the order-seven cost and evidence are reported.

This protocol predates the accepted order-seven run and is not altered to
make a failed computation appear successful.

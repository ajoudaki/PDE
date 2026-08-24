# GPU result: middle-query saturation versus bath cancellation

**Status:** formal empirical support = **True**; numerical audit
pass = **True**.  This is numerical evidence only.

The largest preregistered log-width slope of \(\|R_2\|_q/q\) was
`0.00166966`, and the largest width-4096/512 ratio was
`1.00626`.  The width-4096, \(T=4\), \(L=2\) dangerous
conditional fraction was `0.0`.  There were
`0` evidence-against cells.

| width | R q8 | R q12 | log-mean-exp lambda1 | dangerous/tail L2 | median gate in tail | gate<1/2 in tail |
|---:|---:|---:|---:|---:|---:|---:|
| 512 | 1.7650 | 1.9696 | 1.3087 | 0.0002 | 0.1228 | 1.0000 |
| 1024 | 1.7653 | 1.9766 | 1.3052 | 0.0002 | 0.1239 | 1.0000 |
| 2048 | 1.7626 | 1.9635 | 1.3076 | 0.0002 | 0.1238 | 1.0000 |
| 4096 | 1.7654 | 1.9741 | 1.3101 | 0.0002 | 0.1246 | 1.0000 |

Numerical audit maxima: step moment `1.96e-05`, step probability
`0`, dtype moment `1.13e-07`, dtype
probability `0`, float32 identity
`5.96e-08`, and float64 identity
`1.11e-16`.

Passing this diagnostic supports only the proposed saturation/nonalignment
mechanism at sampled tail scales.  It does not prove a cavity estimate,
exclude rarer cancellations, or change any theorem rung.

# Prefix-compatible coordinate counterexample

The independent review of the frozen indexing theory/report found a minor
example-scope issue. Its full-turn rotating-basis example is valid for arbitrary
square-integrable histories, but rotation across the unit prefix does not obey
the algorithm's constant forward-prefix dictionary and zero backward prefix.
The same obstruction has a simpler example satisfying both prefix conditions.
This correction leaves the frozen reviewed files and source hashes unchanged.

Let e1,e2 be orthonormal real functions on the input probability space, and use
scalar histories h(x,xi)=e1(x) on0<=xi<=2, b(x,xi)=0 on0<=xi<=1, and
b(x,xi)=e1(x) on1<xi<=2. Use dictionary(psi1,psi2)=(e1,e2) on the unit prefix,
and(-e1,-e2) afterward. At every xi its span is the same and its functions are
orthonormal. The single finite dictionary jump is allowed by the write-time
moment equations interpreted almost everywhere.

At tau=2 and q=1, the first forward coefficient is1-1=0; the second is0.
The backward coefficients are(-1,0). Therefore the paired-moment reconstruction
of the history interaction is0. The exact interaction is
integral_0^2 E[b h]d xi=1. Keeping the dictionary orientation constant instead
gives forward coefficients(2,0), backward coefficients(1,0), and reconstructed
interaction(1/tau)*(1*2)=1 exactly. Both histories obey the original prefix.

The example establishes sensitivity to write-time coordinates, even without
changing the represented input span. It is a history/projection counterexample,
not a claim that these particular histories arise from a Gaussian initialized
neural trajectory. No adaptive-input impossibility theorem is inferred.

The independent review's raw-data reconstruction,99-fit audit and exact fresh
GPU replay support the experimental conclusions without numerical corrections.
See STAGE2_INDEX_INDEPENDENT_REVIEW.md for its full scope and frozen hashes.

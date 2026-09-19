# C-X1 corrections and review applicability

The original complete implementation/conditional-closure audit is preserved
as IMPLEMENTATION_AUDIT.md. It reviewed the exact proof/module/test hashes
recorded there and the six-test implementation at commit 4c4bef5.

Required correction: the inherited recursive exponent enumerator descended
once per coordinate and imposed a Python recursion-depth ceiling even at
order one. Replaced it with a study-local iterative weak-composition iterator
in the same total-degree/descending-lexicographic order. Added a seventh test:
exact low-dimensional oracle comparison and d=600/order=1 construction.
This also establishes the separately stated O(d times feature count) syntax
work bound; repeated recursive tuple concatenation had extra cost.

Minor clarification: the numerical theorem now explicitly interprets finite
working observation weights by normalized probability pushforwards for W2.
The dynamics and raw risk/RMS retain literal working weights. Their masses
converge to one in the innermost precision limit.

Corrected validation, declared before rerun: repeat the seven semantic tests
under the original 120-second/512-MiB cap in
`closure/deterministic_v3/`. Repeat exactly the five operational configurations
of VALIDATION_PLAN.md, with no added configurations or changed thresholds,
under the original 360-second/512-MiB cap in `operational_02/`. This rerun
checks the corrected executable; it is not a search for favorable outcomes.

Fresh full reviews must receive the corrected complete candidate and explicit
dependencies, not this correction history or any prior verdict. An old audit
is evidence only for the hashes and claims it actually reviewed.

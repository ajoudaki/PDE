# Proposed destinations and placement rationale

The independent selector proposed a small local general-d p=1 subsection next
to C.4.7.10.B. The assembled alternative keeps the same scientific scope in
`docs/observable_p1.md`, linked from the existing theory and implementation
reading guides. Reason: this chapter explicitly admits arbitrary finite input
rows/dimension and a supplied-state GPU API, while the surrounding C.4.7.10.B
and C.1 impose a circle family and an outer order limit. A separate short
specialization prevents those circle convergence statements being inherited
by proximity, keeps a complete proof directly readable, and avoids editing
an established proof body. This changes placement, not theorem scope. The
independent integration reviewer should assess whether the separate page earns
its maintenance cost; a short local subsection remains a viable destination.

No existing public import or API is changed. The NumPy initializer and optional
Torch modules are separate from the established circle solver. The full source
mapping is generated from `PROMOTION_assemble.py`. Its two literal append strings
are the complete changes proposed for `docs/README.md` and `code/README.md`;
the frozen packet includes both fully assembled files and both original guides.
New runtime material contains no study/generated-path imports.

The candidate claims exact initialized coefficient/normalization identities,
exact real-arithmetic folding and finite-vector-field identities, plus a
working finite implementation at declared arithmetic. It makes no MNIST/PCA
numerical conclusion, universal speed ratio or general-d trained-network theorem.
The bounded synthetic recipe demonstrates operation only; its prediction
discrepancies are not a claimed scientific approximation threshold.

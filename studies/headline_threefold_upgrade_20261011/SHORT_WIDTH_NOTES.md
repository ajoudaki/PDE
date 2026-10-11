# Width-module shortening candidate

Author: scoped agent /root/shorten_width_author. This is an author candidate,
not an independent review or permission to replace established material.

The complete replacement is [SHORT_WIDTH.tex](SHORT_WIDTH.tex). The source
baseline is paper/compact_width.tex at commit
aa28e4693eecb93e6770db404878e959f5161fdf. No paper, book, index or Git file
was edited. The assigned output files are the only files written.

## Preservation and size

The theorem, finite-source lemma, quantitative-separation proposition and
improved-Legendre proposition are byte-for-byte unchanged. All 31 original
labels remain, with no new labels. All public bounds, explicit width maxima,
confidence allocations, query domains, activation assumptions, label
condition, optimizers, retained inventories and initialization provenance are
unchanged.

The original is 1,430 lines, 5,972 whitespace-delimited words, 54,639 bytes.
The candidate is 1,181 lines, 4,880 words, 46,243 bytes: 17.4% fewer lines,
18.3% fewer words and 15.4% fewer bytes. These are source measurements,
not a rendered page-count claim. No font, spacing, margin or preamble change
is involved.

Hashes:

- Original width: 07cdfeda14ee650ae4d8b804cc7317f6046cd470542ec5edfb380b9c5f363988
- Candidate width: 1eb2d00e620824f841fdffcfb47c616242038bbae2669dffc01dded47b26839d

## Exact reduction map

| Original width passage | Candidate location | Reuse or replacement |
| --- | --- | --- |
| Opening and local-source notation, lines 1–117 | Before cp:poly:source | Removes repeated motivation and groups the same local coefficient imports. Every definition needed in this section remains or is imported with its exact equation identifier. |
| Finite initialization, lines 184–316 | Start of cp:poly:source proof | Same covariance interpolation, variance-free propagation, sphere net, explicit initialization gate, deletion comparison and probability costs; shorter exposition. |
| Scalar map recurrences, lines 327–494 | cp:poly:eq:map-coefficients through the coefficient ledger | Replaces parallel scalar recurrences by the exact differentiated products already proved in cp:src-local-lemma plus a finite power-majorant calculation. Retains the parameter Duhamel formula, control-speed recursion, parameter time derivative, and explicit exponent accounting. |
| Response products, lines 496–553 | Before cp:poly:eq:map-interface | Invokes cp:src-response-recursion and cp:src-direct-reverse through their complete local-map proof; retains the two-factor probe subtraction, coordinate localization, amplitude bound and final common envelope. |
| Rectangle and flaring geometry, lines 561–600 | Before cp:poly:eq:absorption-gates | Reuses the deterministic construction and proof of cp:src-panel-working, substituting the capped radius. Keeps all numerical propagator, contour, motion and strip margins. It does not invoke the older eventual probability conclusion. |
| Finite endpoint Gaussian event, lines 602–741 | cp:poly:eq:absorption-gates onward | Same own-cavity stops, retained conditioning, explicit contours, control nets, quadratic tail, common-prefix interpolation, union cost and first-exit powers. Only repeated prose is removed. |
| Trace and maximum improvement, lines 743–770 | Before the budget-removal paragraph | Uses cp:src-traces and its Schatten/scalar-feedback calculation; retains finite residual-trace and remainder bounds, all four response coefficients, multiplier 64 and the failure allowance. |
| Complete-path moments and collision count, lines 772–854 | Budget-removal paragraph | Same order-u proof and every moment/radius/entropy bound. The successful initialization/map/maximum event E is explicitly identified. No new independence assumption and no exchange of a fixed-order limit for the required finite order. |
| Real continuation and panel count, lines 856–893 | End of source proof | Reuses the backward subtraction and disk integral proof, retaining explicit response tail and capped-radius calculation. The reciprocal expression is identified explicitly as 1/(lambda r_n), which is the quantity used in the original count. |
| Innovation inequality, lines 990–1017 | Conditional innovation paragraph | Imports the general squared-area and spectral inequality already proved before the equal-diagonal specialization in cp:innovation; retains the general formula and its conditional substitutions. |
| Derivative-to-trajectory transfer, lines 1037–1064 | End of separation proof | Same constants and gates; compressed substitution prose. |
| Third-order history proof, lines 1109–1295 | cp:poly:legendre proof | Groups backward/response subtraction and actual-flow derivative estimates. Keeps the physical defect, activity clock, zero prefix derivative, weighted second derivative, both integrations by parts, backward freezing bound, signed comparison and bootstrap in full. |
| Taylor source construction, lines 1299–1363 | Start of cp:poly:assembly | Uses the exact coefficient construction and input-span proof of cp:panel. Retains all four coefficient error tolerances, exact source rank and exact inventory, then proves the same quantitative degree/count gates. |
| Final width assembly | cp:poly:eq:legendre-final-width and cp:poly:eq:taylor-final-width | Unchanged displayed maxima and polynomial dependencies. |

The only numbered equation whose mathematical content changes is the local,
externally unused cp:poly:eq:map-coefficients. It previously labeled the
backward map recurrence; it now labels the parameter Duhamel coefficient and
its bound. The backward recurrence is still stated immediately afterwards,
and its bounds are in the preceding shared ledger. Every other numbered
equation is unchanged after whitespace normalization.

## Map-ledger verification

Write X=beta^L, chi=1+lambda^{-1} and kappa_0=1/4000 as in the
candidate. This calculation changes no final coefficient or width power.

The source recurrences bound
H_j,P_j,f_j by X^3; k_j,tau_j by X^4; V_j^0 by X^7; and
A_*,D_*,eta_*^{-1},B,Gamma,J_0 by X^5,X^6,X^27,X^3,X^7,X.
Hence M_0,A_0,B_0,E_0 are bounded by X^31,X^33,X^32,X^38.

The exact three port forces in cp:src-local-lemma, integrated for length
64 ell_n/lambda and normalized activity at most one, give the displayed
parameter coefficient v_0 <= X^80 chi. Forward propagation adds P_j and
one activation derivative, giving X^85 chi. Backward propagation inserts
M_0 only additively; its largest gate forcing has exponent at most
1+31+85=117. The homogeneous propagation and sum over layers cost at most
X^3, below X^125 chi. Replacing control amplitudes by one in these
forcings gives the smaller X^90 chi control coefficient.

The retained reference-speed recursion gives T_j^0 <= X^45 and
D_c <= lambda X^45, and all reference derivative coefficients are
at most lambda X^47. The parameter variation is differentiated through
its ODE, so there is no derivative of the variational Jacobian. Its
coefficient v_t is bounded by X^125 chi. Forward time products have
coefficients at most X^(47+85) chi before gate and propagation factors,
hence fit X^140 chi. Backward time forcing t_2 M_0 z_t fits X^172 chi;
the remaining products fit X^174 chi, and propagation remains below
X^190 chi. A time product has at most one raw coordinate derivative,
so there is only one sqrt(n) loss and at most ell_n^4.

These are the same bounds used previously. Therefore C_0=X^300 chi,
the response envelope C=X^1000 chi^2, and all three expressions in
cp:poly:eq:map-interface are unchanged. In particular A_{N,rho} and
the source exponent 40000 do not increase.

## Sources and checks

Read completely: the current paper/compact.tex, compact_width.tex,
compact_foundations.tex, compact_fitting.tex, compact_legendre.tex and
compact_selected.tex; docs/notation.qmd; AGENTS.md; RESEARCH_WORKFLOW.md;
solve-math-rigorously; explain-with-canonical-notation and its neural
reference. No other study, archive or historical research was used.
compact_initialization.tex was searched mechanically for label references,
not used as a mathematical input. No external theorem was added.

Dependency hashes at reading:

- compact.tex: 62cbca244c507a581f462e0cc8c6a023c21a5ba2d3efba76f5998ffa9ef8bae6
- compact_foundations.tex: 44c201bda34d1eac488c9cc3347a4d2cf608128a3f774df65210584606feaf6a
- compact_fitting.tex: 6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f
- compact_legendre.tex: 862aa37139ad9af67ac04b52949f838031e91077021b2da9060244d36ab4e0f9
- compact_selected.tex: cce32506923384c8124e0a5f965591ad3ae67a51b62377098563eda9b4ff54fd
- notation.qmd: 78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023

Executed checks:

1. Full candidate read after writing, repairing the truncated middle read
   with explicit reads of lines 440–720.
2. JavaScript extraction and comparison of formal theorem/lemma/proposition
   environments: all four statements identical to the original.
3. Label-set comparison: all 31 original labels present, no new labels.
4. Candidate reference extraction against the candidate and permitted paper
   modules: no missing targets.
5. Balanced begin/end environment stack: passes.
6. Numbered-equation comparison after whitespace normalization: 21 of 22
   unchanged; the single local mapping is documented above.
7. Hand check of the substituted map majorants, unchanged finite probability
   sequence, conditional innovation specialization and Legendre defect
   absorption. The local check is an author check, not independent review.
8. wc and sha256sum measurements above; original width hash unchanged.

No assembled LaTeX render was run by this scoped author: only the two assigned
candidate paths were authorized for writes. Render/layout measurement and
independent mathematical review remain coordinator checks. No known new
mathematical gap was found in the rewritten passages.

## Further factoring

The concrete remaining duplication is that the qualitative source proof and
this quantitative refinement each describe independent stops, local events,
trace absorption and budget removal. A larger coordinated rewrite could expose
a deterministic stopped-source lemma plus a finite Gaussian/moment lemma in
compact_foundations.tex, then instantiate it once for qualitative sphere
sources and once for the quantitative finite-panel domains. That would change
another proof module and its interfaces, beyond this assignment. Merely
deleting the remaining finite-width probability calculations would lose the
claimed explicit threshold.


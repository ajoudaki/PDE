# Independent scientific promotion review A — frozen packet v1

**Verdict: REQUIRED CORRECTION; do not accept this packet. Review complete.**

There is one identified required mathematical correction, at
`additions/promotion_09.qmd:333`. The remaining assigned mathematical and
implementation components have no unresolved objection from this review.
The correction is small, but the promotion gate requires a corrected frozen
candidate; passing runtime tests cannot waive it.

## Independence and inputs

Reviewer identity: `/root/scientific_review_a_v1`, a fresh independent context,
not an author, assembler, selector, or historical participant. I received the
neutral scoped assignment and operational coordination only. I did not read a
study README, scientific history, another reviewer report, author verification
outcomes, live manuscript, another study, or archived book. I authored no
candidate changes and used no subagents, research campaign, download, or
external scientific source.

All scientific inputs came from
`/home/amir/Codes/PDE/data/generated/book_promotion_20261010/promotion_review_v1/`.
I began with `assignment.md` and `inputs.json`. The manifest SHA-256 is
`155cdfe9e8cd3f25b0aa3ade60619877f28704a9c8ad48a8e84778b26768cea2`.
All **114** listed files matched their declared bytes and SHA-256 before review;
all matched again after execution. The packet was not modified.

I read the complete frozen `edition/AGENTS.md` and `edition/RESEARCH_WORKFLOW.md`.
Required process material outside the packet was limited to:

- `/etc/codex/skills/solve-math-rigorously/SKILL.md`;
- `/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md`;
- its complete `references/neural-response-memory.md`.

These govern review method and notation, not scientific input substitution.
No additional scientific input was needed or fetched.

## Required correction

**A1 — Incorrect coefficient in the ridge-independence proof (minor mathematical
notation defect; acceptance blocker).**

At `additions/promotion_09.qmd:332–334`, the proof introduces
\(\tanh t=\sum_{j\ge0}(-1)^j A_jt^{2j+1}\), then says
\(\phi'=1-\phi^2\) gives \(a_{\rm reg}=1\). The required base coefficient is
\(A_0=1\). The following recurrence, for \(j\ge1\), then implies that all
\(A_j>0\), which justifies the Vandermonde argument.

This is a false statement about an already defined quantity, rather than a
harmless unnamed symbol. Lines 180–187 define \(a_{\rm reg}\) as a regression
coefficient. Its first normal equation gives

\[
a_{\rm reg}=\frac{\alpha\nu-\beta b_{\rm reg}}{\nu+\eta}
<\frac{\alpha\nu}{\nu+\eta}<1,
\]

using the strictly positive \(\beta,b_{\rm reg},\eta,\nu\) and
\(0<\alpha<1\) established in this section (in particular lines 244–249).
Thus the displayed claim cannot stand literally. Replace only that base
coefficient assertion with \(A_0=1\), and state the recurrence range if desired.
The intended corrected argument is complete and does not require a new
mathematical hypothesis. I did not edit the candidate.

The issue was promptly reported to the supervisor. At the supervisor's request,
I completed the rest of the assigned review to consolidate any other corrections.
There are no other identified required corrections.

## Mathematical review and component verdicts

I read every line of all five additions and all five supplied mathematical
dependency passages. This includes the entire 4,537-line compression chapter,
not only its headline claims or selected lemmas. I checked definitions,
normalizations, intermediate inequalities, dependency uses, stopping arguments,
probability quantifiers, limit order, and construction inputs throughout.

| Component | Verdict | Main adversarial checks and scope |
|---|---|---|
| Fixed-order model, initialization map, landscape, lower-layer trainability, scalar clock and plateau (`promotion_09.qmd`) | **Required correction A1** | Checked the population-weighted physical metric, actual transpose, finite-time continuation bounds, regression/Stein calculation, monotonicity bounds, odd architectural floor, norm-local landscape argument and lower-layer submersion. The local-minimum claim concerns the full declared population state space, and does not prove convergence from initialization. The scalar feature-norm protection and positive-floor example were checked separately. The remaining argument is acceptable after A1. |
| Protected pairs and small-label basin (`promotion_10.qmd`) | No objection | Checked reflected/antipodal invariant sectors, scalar reduction, strict feature gain, and return to physical time. For arbitrary orientations, checked the initialized feature independence, the feature Lipschitz bound, the ball of radius \(\lambda/(8\sqrt5)\), and the retained Gram gap. Arbitrary-amplitude protected pairs and small-amplitude general orientations are separate claims. |
| Cyclic triples (`promotion_12.qmd`) | No objection | Checked the linear-or-cubic nonvanishing argument, compactness producing a positive uniform constant, perturbative fitting estimate, and sign-transformed mixed labels. Homogeneous-linear nonrepresentability does not imply that every trained predictor is nonlinear by the same quantitative measure. |
| Passive predictor freedom (`promotion_13.qmd`) | No objection, depends on correction A1's elementary ridge argument | Checked initialized feature independence, the query residual orthogonal to the training span, and the stationary interpolant construction. This establishes representational freedom at zero training loss, not that the initialized flow can reach every such predictor or arbitrarily select its query value. |
| Complete-trajectory compression (`promotion_compression.qmd`) | No objection | Full proof checked as detailed below. This is an exact-real, sufficiently-wide, fixed-problem result for the explicitly zero initial readout. The practical code does not inherit its initialization-only compiler or continuum error guarantee. |

For compression, the proof coverage and principal attacks were:

1. **Setup and fitting (lines 1–511).** Checked \(v=x/\sqrt d\), hidden storage
   variance \(1/n\), output \(1/n\), unhalved mean loss, and mobilities
   \((n,1,\ldots,1,n)\). Checked the small-label hypothesis
   \(Y\le(\gamma/m)\beta^{-30L}\), bootstrap displacement, residual decay,
   fitted limits, and the signed perturbation estimate. Positive feature-Gram
   gap is required; no input-Gram inverse or orthogonality was silently added.
2. **Analytic sources (lines 512–2305).** Read the entire local-power, local-map,
   passive-remainder, Gaussian-rectangle, provisional-stop, time-derivative,
   whole-sphere, finite-query and residual-adapted panel arguments. Checked the
   stopped/cavity conditioning and adaptive-control discretizations rather
   than treating trained matrix responses as fresh independent Gaussians.
   Conditional trace terms remain in the estimates. Dense all-time training
   carriers are used on their declared scope. Complex continuation uses the
   real frozen Gram in the stable part; it does not assume that a complex
   transpose Gram is positive definite.
3. **Legendre (lines 2306–2921).** Checked the fixed prefix with initial clock
   \(\tau=1\), projection normalization, moment transport, matrix reconstruction
   and actual transpose. Checked the \(2\rho/(mn)\) outer-product defect and its
   propagation, the order-independent bounds, the chosen order, and the
   all-time tail. The moving-state count does not erase the retained dense
   initialization matrices.
4. **Dense fluctuation (lines 2922–3189).** Checked the final-layer conditional
   innovation variance, scalar fluctuation/anti-concentration, and transfer
   from a time derivative to a positive-time trajectory fluctuation. The lower
   bound is sufficient for the all-time denominator; it is not an asserted
   lower bound at the fitted endpoint. Independent-run randomness and the
   coupled reference for approximation remain distinct.
5. **Selected dynamics (lines 3190–3976).** Checked the sparse-coordinate
   barrier construction and exact source metric, its inverse and transpose
   convention, source-to-runtime maps, corrected readout, prescribed moving
   equations, energy identity, independent fitting and endpoint tails, and
   finite-horizon perturbation cancellation. These equations are not assumed
   to be ordinary gradient descent in arbitrary selected Euclidean coordinates.
6. **Compiler and final assembly (lines 3977–4537).** Checked that finite origin
   derivatives contain the information used by the theoretical continuation
   construction, with no runtime trajectory oracle. Checked the joint
   time/sphere approximation and dimension count, the holomorphic sphere
   domain, and the different fixed-panel adaptive partition. Passive inputs
   are declared before initialization and supply no labels. The final ratios
   use the same query domain and include endpoint limits, and their eventual
   probability convention is per sufficiently large individual width. No
   uniform growing-dataset, uniform vanishing-label, practical width,
   finite-precision, or efficient preprocessing conclusion follows.

The five complete book dependency passages were checked against their uses in
the additions. I did not replace them with remembered live-book material.

## Implementation review

All proposed Python bodies, test bodies, example producers, complete guides,
custom browser code, and the 13 full named maintained code dependencies were
read. The only code-text exception is the assignment's explicit exemption for
the unmodified D3 vendor payload on `radial_explorer.html:97`; the authored
viewer code on lines 1–96 and 98–365 was read in full, and the actual bundled
library was exercised by the Node harness.

| Component | Verdict | Checks and limits |
|---|---|---|
| `compression.py` | No objection | Dense mobilities and normalization; both hidden action orientations; Legendre state and defect; selected metric, metric inverse, corrected readout, and positive-Gram solve; source truncation relative to its original scale; initialization ownership; jets versus empirical rollout provenance. Singular selected training Grams correctly reject without ridge or pseudoinverse. |
| `observable_dictionaries.py` and assigned maintained closure dependencies | No objection | Complete retained word enumeration, bounded grammar and joint Gaussian-source compiler; inverse-Cholesky orientation; ridge normalization; finite-carrier contraction and its actual transpose; frozen/random source provenance; finite endpoint caps; physical metric. Native population quadrature and initialized finite-carrier adaptation are different constructions. |
| `compression_data.py` | No objection | Toy target and unit-row generation, local RNG streams, train-only target scaling, stable IDs, disjoint MNIST source pools, balanced class sampling, raw-pixel normalization, and explicit download control. No MNIST data were downloaded. |
| `prediction_views.py` | No objection | Signed geometry, fixed comparison scales, explicit reference and frames, array validation, HTML escaping, offline control behavior. Finite query panels and interpolation do not give a continuum error bound. |
| `radial_explorer.py` and authored HTML/JS | No objection | Query-angle sorting with source IDs, training values and weighted losses, seed averaging as mean of losses, physical-time and loss alignment, endpoint disclosure, degenerate/one-frame controls, safe embedding, and reference/model selectors. Endpoint controls do not certify settling. |
| Guides, examples, package boundary and navigation | No scientific objection | Complete recipe bodies and context were read. Both new bounded producers run with explicit fresh scratch destinations. Root import remains separate from opt-in Torch/plotting/data dependencies. New navigation states the zero-readout compression model separately. This is not a fresh audit of unrelated older chapters/APIs described by the full README. |

The practical Harmonic source producer uses a short dense rollout; numerical
Taylor can use finite origin jets or rollout fits. Those source objects and
their provenance are not the chapter's certified global initialization-only
compiler. The practical selected runtime can retain a fixed finite state after
source construction without that fact proving the theorem's global accuracy.
Likewise, a source-space rank diagnostic, a short fit, or a rendered picture
does not certify all-time or whole-sphere approximation.

## Executed checks and evidence

Execution used only the frozen code via `PYTHONPATH`, with bytecode disabled,
one numerical thread, CPU float64, and the specified Python executable.
Environment: Python 3.10.14, NumPy 1.26.4, Torch 2.9.0+cu130 (CPU execution),
Node v19.9.0. Scratch was exclusively
`data/generated/book_promotion_20261010/reviewer_a_v1/`.

The following path abbreviations describe the actual commands, run from
`/home/amir/Codes/PDE`:

```sh
PACKET=data/generated/book_promotion_20261010/promotion_review_v1
SCRATCH=data/generated/book_promotion_20261010/reviewer_a_v1
PY=/home/amir/miniconda3/bin/python
export PYTHONPATH="$PACKET/edition/code" PYTHONDONTWRITEBYTECODE=1
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
```

1. **Compression suite: 16 tests, all passed (0.663 seconds reported by unittest).**

   ```sh
   "$PY" -B -m unittest discover -s "$PACKET/edition/code/tests" -p test_compression.py -v > "$SCRATCH/compression_tests.log" 2>&1
   ```

   The tests include independent autograd for all six activations and three
   depths, Legendre projection/transport and defect, selected adjoint and energy
   identities, full-retention reduction to the dense vector field, source
   provenance, quadrature, zero labels and singular-Gram handling. I inspected
   the test implementations, not only their names or status.

2. **Remaining proposed suites: 36 tests, all passed (1.265 seconds).**
   With `PDE_OPTIONAL_TEST_SCRATCH`, `TMPDIR` and `MPLCONFIGDIR` directed under
   the assigned scratch, I ran the following Python body with `"$PY" -B -`,
   redirecting both streams to `remaining_tests.log`:

   ```python
   import unittest
   suite = unittest.TestSuite()
   for pattern in ['test_compression_data.py', 'test_observable_dictionaries.py',
                   'test_prediction_views.py', 'test_radial_data.py',
                   'test_radial_viewer.py']:
       suite.addTests(unittest.defaultTestLoader.discover(
           'data/generated/book_promotion_20261010/promotion_review_v1/edition/code/tests',
           pattern=pattern))
   result = unittest.TextTestRunner(verbosity=2).run(suite)
   raise SystemExit(not result.wasSuccessful())
   ```

   These include mocked official-dataset loading without download, dictionary
   counts and finite equations, independent tensor derivatives, complete
   carrier reduction, and actual Node execution of both authored viewers. A
   Torch warning about its legacy TF32 settings API appeared; it was not a
   numerical/test failure.

3. **Independent origin-jet and boundary attack.**

   ```sh
   "$PY" -B "$SCRATCH/independent_checks.py" > "$SCRATCH/independent_checks.json" 2> "$SCRATCH/independent_checks.stderr"
   ```

   This independent script differentiates the full moving Dense vector field
   with nested autograd JVPs, not a frozen-direction substitute. It checks
   initial, first and second hidden/backward fields against the compiled source
   plus required initialized generators for every activation at depths 1, 2
   and 4. Width is 37; the largest tested span is 13, so the projection check
   cannot pass merely by retaining the entire carrier. All 18 configurations
   passed; maximum absolute projection residual was
   **2.886579864025407e-15**. The panel includes a nonunit passive row, an API
   boundary outside the sphere theorem, without claiming a theorem extension.

   The script additionally tests coincident, opposite and zero training rows
   with zero labels: Dense and Legendre preserve the exact zero equilibrium;
   Selected rejects the singular training feature Gram, and preserves the
   zero equilibrium for a positive-Gram dataset (depths 1 and 3).

   The first script invocation stopped because my boundary fixture initially
   expected Selected to accept the singular Gram. The rejection was correct
   under its explicit contract. I corrected only the reviewer fixture to
   assert that rejection, retained the original traceback as
   `independent_checks_first.stderr`, and reran. This is not a candidate bug
   or a hidden failed candidate check. The final script and complete numerical
   results are retained in scratch.

4. **Both proposed bounded example producers: exit 0.** With `TMPDIR` and
   `MPLCONFIGDIR` under scratch:

   ```sh
   "$PY" -B "$PACKET/edition/code/scripts/example_compression.py" --out "$SCRATCH/compression_example" > "$SCRATCH/compression_example.log" 2>&1
   "$PY" -B "$PACKET/edition/code/scripts/example_radial_explorer.py" --out "$SCRATCH/radial_example" > "$SCRATCH/radial_example.log" 2>&1
   ```

   I independently recomputed every emitted source hash against the frozen
   source and every output hash in both manifests: all matched (8 compression
   outputs and 5 radial outputs). These are the prescribed tiny operation
   examples, not evidence for learning quality or theorem error rates.

5. **Manifest integrity and coverage.** A Python `hashlib.sha256`/byte-length
   comparison over every `inputs.json` file entry passed before and after the
   work. The final complete machine-readable record is
   `data/generated/book_promotion_20261010/reviewer_a_v1/hashes_and_read_coverage.json`.
   Exact file hashes and reading status also appear below. No packet file was
   written by these checks.

## Completion and remaining limits

The assigned review is complete: complete compact chapter, complete older
mathematical additions, all supplied mathematical dependency passages, all
proposed implementation/test/example bodies, all full named maintained code
dependencies, all guides and navigation/notation inputs. Truncated reads were
repaired; in particular the 07 dependency passage spanning original lines
5265–5421 was reread completely. The manifest itself was fully parsed and
enumerated after a long combined display was truncated.

The 63 files tagged only as frozen standalone build inputs were hash-verified
but were not line-read as unrelated scientific material. Their exclusion is
part of the neutral assignment; this review does not claim a fresh whole-book
or unrelated-code audit. The listed bundled D3 vendor line was not line-read.
No required scientific input remains unread. There was no formal proof-assistant
verification, CUDA execution, practical large-width accuracy test, MNIST run,
or certified browser rendering audit; none is a premise of this component
review's mathematical judgment. The CPU/Node checks support finite operation,
not infinite-dimensional or asymptotic guarantees.

**Open objection: A1 only.** The packet remains unaccepted until the required
correction is made and reviewed under the promotion process. No blanket PASS
is issued, and no correction has been silently applied.

## Exact frozen-file hashes and reading coverage

All paths in the following inventory are relative to the frozen packet.
`Full` means complete line reading, including complete proof or code body;
`Build only` means hash/byte verification without a fresh scientific line audit.
The HTML exception is recorded explicitly. All observed hashes equal the
manifest values, and all observed byte lengths equal the declared lengths.

| Frozen path | Bytes | Reading | SHA-256 |
|---|---:|---|---|
| `additions/promotion_09.qmd` | 35487 | Full | `0874d7399c125b2639225e65c5a5a94701feb8d318d5a19302e0fec807eede12` |
| `additions/promotion_10.qmd` | 12569 | Full | `82824a92deef50a47c5445c259f42624aaa0d435cfbc7d12a6a35df8040e38c2` |
| `additions/promotion_12.qmd` | 4850 | Full | `a5b40e79c58ee4746a1ecafcf7bf74e33864ae3875a35d9ba3398a844eca3ff1` |
| `additions/promotion_13.qmd` | 4011 | Full | `b637dfbd85b4cedb2fdeebe6ff7eb927edad43bd71ba1571f9fa95b3cd832c57` |
| `additions/promotion_compression.qmd` | 171649 | Full | `5302a2a1e077f5ef18d860374d21b2da484fc67253759d399c1c4ab520b1dca0` |
| `assignment.md` | 2858 | Full | `b0ff4a51dae7faf3b876deb15fb29613ff468007ce6bc4a45826f31d9fb14d75` |
| `book_dependencies/07-observable-closure.qmd.lines-4888-5040.txt` | 8590 | Full | `8d1132b68270f1f4ff5e750faf791e75301f098b2c2e30f958771b19e38e93a3` |
| `book_dependencies/07-observable-closure.qmd.lines-5265-5421.txt` | 7199 | Full | `9419d7c80fedc61dfdb8608801b13448766d75737b7d4d46228ac7f3d6c2535c` |
| `book_dependencies/07-observable-closure.qmd.lines-5461-5492.txt` | 2284 | Full | `1bed870ff26a81829f298c3b9e5488f5b934e9249d5cf5fb10b029deefcfc871` |
| `book_dependencies/08-autonomous-computation.qmd.lines-3119-3393.txt` | 14417 | Full | `dff5d0b73444886a63d206251213b5eb7967cab5b622ff6c1f96c38195bb98db` |
| `book_dependencies/08-autonomous-computation.qmd.lines-5345-5387.txt` | 2021 | Full | `b2af10e2d28b9ae71b6616e86b1461f932703015c0a2476ea276f2c0fc55888c` |
| `edition/AGENTS.md` | 5978 | Full | `d9835366632b1077c371218c67dd43b1da3c002fb55963c3c21b3cb26fa20e97` |
| `edition/RESEARCH_WORKFLOW.md` | 17340 | Full | `459143719de664d1d6669c615b499d5b2f2505c5d7bad0c22dd7657e9ac41dd1` |
| `edition/code/COMPRESSION.md` | 11620 | Full | `43280504b77f738b6ea30a3de9e1ef4cc57f51a985833d030eafe42f44a375e6` |
| `edition/code/COMPRESSION_DATA.md` | 7031 | Full | `189c0a7ffd62364d47d3670f9667f9f83af0ff7fb09c9ff1c3d4c0a2c400f346` |
| `edition/code/GENERAL_P1.md` | 14415 | Full | `6eab7abf57530cae3c4669ad9cecb9cfadaa42f4b638d70ae742ce5334f55b74` |
| `edition/code/OBSERVABLE_DICTIONARIES.md` | 13840 | Full | `807e679baa162ea151e419fef58e0bb570fb253a7e54307f27c9cc61c861ad87` |
| `edition/code/PREDICTION_VIEWS.md` | 6915 | Full | `ea1cce40fcc7d253309351e0e2a0e0c9b9fe1ab4ac79f3fbf36c59dbc31979d5` |
| `edition/code/RADIAL_EXPLORER.md` | 4227 | Full | `c15d04bad246ab801ded97674fdb205cd7f38423ef1890855ad5732d53873f18` |
| `edition/code/README.md` | 71026 | Full | `b038f6033e8e387c602b0e7947ab08a793fb825f179d5afa161d6c12d4495807` |
| `edition/code/pde/__init__.py` | 611 | Full | `65eb96a5dd455041d2ad1f32652e3e26e8c15192eb41bdffba27980f0f69e8c3` |
| `edition/code/pde/closure_comparison.py` | 10587 | Full | `f715624c7d81116fd24d888ab5bce1afc3e8b353406b23553e6a6ff8b4f0a89e` |
| `edition/code/pde/compression.py` | 40427 | Full | `47b0045f128b3ef36431e3311514632724fc5c6208a4466c017094e3685968d3` |
| `edition/code/pde/compression_data.py` | 11659 | Full | `12b8e9c351d368660f8655587e05e828fee4608e369c5ce128c982c19f5557d6` |
| `edition/code/pde/exact_calculus.py` | 32534 | Build only | `7fd7fd515028a924bb4c28dcd374d652a3a3af15c9339c1ce2361390faa48e1a` |
| `edition/code/pde/finite_jets.py` | 22343 | Build only | `a8e22e14c7ce387636a7981a5e80556b975f83f8cf6a2b85ab22af877f5cca4c` |
| `edition/code/pde/finite_network.py` | 15525 | Full | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `edition/code/pde/finite_reductions.py` | 15571 | Build only | `391dc35773a35d86f889cebda9f95820d793a656f2fb05f9b01bb7453be20a4c` |
| `edition/code/pde/finite_torch.py` | 7541 | Full | `76d87cb0ddd25e974acf85935dc8fbfc8bc4a9eb829d5e60782e64d20e4f55a8` |
| `edition/code/pde/gaussian_moments.py` | 4464 | Full | `6c2a21a9f3d101c433b5f06cb3f6e1dcdeca23a814891ea7bd81e73960e854ae` |
| `edition/code/pde/observable_arithmetic.py` | 9286 | Full | `2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb` |
| `edition/code/pde/observable_closure.py` | 31181 | Build only | `f8dc5d16e5de1737444c44aae737ee1c9b4d664188d72f59acd0bb92f457c137` |
| `edition/code/pde/observable_compiler.py` | 24779 | Full | `1add30410ee2e8de05fffca225643dbbbeab7ab8d6420382014bb8c9cceca7ac` |
| `edition/code/pde/observable_dictionaries.py` | 18845 | Full | `4ac8d595f8250e8e2e90cb12e9ad83c61dfb50210057f07060b2a551fe05d5b3` |
| `edition/code/pde/observable_fixed.py` | 7158 | Full | `75c5b6a4478e5365d008bd7ad134cf1c2b6cd6942c68358e0a2d4137207c1225` |
| `edition/code/pde/observable_initialization.py` | 18640 | Full | `6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2` |
| `edition/code/pde/observable_laws.py` | 23687 | Build only | `6fb38416ce02ca77aae0392201927eb9aeba5c672ebe774181822dfb805d0503` |
| `edition/code/pde/observable_p1_initialization.py` | 7909 | Full | `65ded7e9faa352612fb833735d3075cbe41c0b24a535bf742d1fc86849aded6d` |
| `edition/code/pde/observable_solver.py` | 16375 | Full | `711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605` |
| `edition/code/pde/observable_torch_circle.py` | 13321 | Build only | `4fa63eb6abdd1c8573abfa1a7dc0a107d13ec669ae078659e8298cd517000430` |
| `edition/code/pde/observable_torch_p1.py` | 21640 | Full | `d67f0d832d265e75925f0020c42ab4d8e1dd3387e7e485412eff946ae5d20f1f` |
| `edition/code/pde/observable_words.py` | 7827 | Full | `b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5` |
| `edition/code/pde/prediction_views.py` | 21888 | Full | `9f1fa503ed0f4a60e63c0cdda80ea33b9b443be8993c722e52b32ed0a6af2e5f` |
| `edition/code/pde/radial_explorer.html` | 314409 | Authored lines 1–96, 98–365; D3 line 97 excepted | `390499a83fcaba395614cebf31dc2935b072aa0b9cfbd7cdd5832fe8fc08296c` |
| `edition/code/pde/radial_explorer.py` | 16702 | Full | `61412b5c2202a1ed45f49c56ce2092da5234c2fd231119f3bc796833fc903506` |
| `edition/code/scripts/analyze_general_p1.py` | 2974 | Build only | `e09242bd75dcabd1f6bdc759fd8b0a6c669db158ff93285c659ef63856ceca8b` |
| `edition/code/scripts/analyze_observable_horizon.py` | 13721 | Build only | `742ea5a7f46d0f7afb279195d33631a350984280ad7c9a86e70f550657499e14` |
| `edition/code/scripts/analyze_observable_solver.py` | 18661 | Build only | `6c0ae411f567a94ff51e286a09c8f2fec2b90c5d73055ee083c6699f65e75347` |
| `edition/code/scripts/example_compression.py` | 4453 | Full | `90df9f20cef5fb0964b8b09ee7a1970695fbeeb98ba2641adbd316eef8279435` |
| `edition/code/scripts/example_general_p1.py` | 7955 | Build only | `c288ef22b9cb5f167cff37931d35dc9c5b149ca1bb9d1805fcb0145afa2dae41` |
| `edition/code/scripts/example_radial_explorer.py` | 3998 | Full | `706636fcd3868dc2b6f4f19efce073d31fdf17433df8ba917b3222c865d9f525` |
| `edition/code/scripts/run_observable_validation.py` | 15109 | Build only | `d8a66b9a7c16802acc80602f233d76095ed32fcfcdc8a28df321faf9f3d3e0e5` |
| `edition/code/scripts/validate_observable_horizon.py` | 22826 | Build only | `3e1704a460a87e6e9f221ecfb73c15c05627f0a864fd4df01337f65a88ce5cb2` |
| `edition/code/scripts/validate_observable_solver.py` | 7923 | Build only | `54a8c5dbe8ffa0c105a54a2bc2b6969b83fe56f6f78ef9bdbc19c4b689e7f265` |
| `edition/code/scripts/validate_torch_circle.py` | 5813 | Build only | `edb42a5bb72b28f96f484a54ddc2f65043329ab0c8539ff3aa415923f5a885e0` |
| `edition/code/tests/test_book_exporter.py` | 6319 | Build only | `3d271c7d0b26c0853dd4b78d2bf1759ffb73d7e844d434ffdcaa3307c7b15224` |
| `edition/code/tests/test_compression.py` | 17557 | Full | `99c23de2fa009f7af0469166305229f7afa99a589e1dcc4ca420e27ca4ebf95c` |
| `edition/code/tests/test_compression_data.py` | 11212 | Full | `24115018f7f1231bc2b1bdcb8ccb8096bf067e75d0b0837008006cc00bda11d7` |
| `edition/code/tests/test_exact_calculus.py` | 27976 | Build only | `dcb5f213cc5f4598c40f67598e405fef3c1507104e29b507a32e3bcbc8b78028` |
| `edition/code/tests/test_finite_jets.py` | 25053 | Build only | `566b4a6bf93e4a0efca0b7cdbc8ca29ba91c03ffb85f2dec366940eabc8cf555` |
| `edition/code/tests/test_finite_network.py` | 15154 | Build only | `a45ddc72c943b85aff63b6c4d49c88d8784100dbed8878cd9bb710b8256b9931` |
| `edition/code/tests/test_finite_reductions.py` | 18563 | Build only | `7b1a4023334956a25afd4217de7a311145b64c240fc78b87f84b16d2af7dedb0` |
| `edition/code/tests/test_gaussian_moments.py` | 5179 | Build only | `9aeb8a09137edf50fd30db36b08a337a3b1b3cebe9ac85b95ec4c6787f1188ea` |
| `edition/code/tests/test_general_p1.py` | 23072 | Build only | `895ff58b2e348ec7733534c9e969d2cd1579e25b33cc3f3d08525d32aff37215` |
| `edition/code/tests/test_library_boundary.py` | 2357 | Build only | `68f4a03ad25f8cf320e97ee6e1027b6e1d01945895074eed0d5f90b5af899cf2` |
| `edition/code/tests/test_numerical_contract.py` | 10601 | Build only | `c925d71d60aa1965d44900122fa04e5fdfff18f00bdf8a41ddc9a2b91e5e1d92` |
| `edition/code/tests/test_observable_closure.py` | 17631 | Build only | `ecc60bfd7eec882c8ae05140d756f6ec8cf90909b6317aab2c126b3c27439635` |
| `edition/code/tests/test_observable_compiler.py` | 9066 | Build only | `8a5955ad47df01a6110e8b5f3b64264b414e8ee70696e7f93250dcdf9dbb17cb` |
| `edition/code/tests/test_observable_dictionaries.py` | 12124 | Full | `149b3d8be11fed0689b1d8e0389d6e3ab057924b750952277bfdafdfbceb8457` |
| `edition/code/tests/test_observable_horizon_analysis.py` | 3767 | Build only | `13419bb449f03bfb6db540156602e49b20719ff852778d031c45202af22a0314` |
| `edition/code/tests/test_observable_horizon_validation.py` | 15154 | Build only | `5e49bb2b17ff8225287179714ba855f0b901cc246f389795afb965ea75837ca7` |
| `edition/code/tests/test_observable_initialization.py` | 13042 | Build only | `9e36f4c120013d58bb082bd521ea683a574bdf5a3652058fc0479a0e665e6e68` |
| `edition/code/tests/test_observable_laws.py` | 14413 | Build only | `96c3b788a11f721a95daa8f4e86088ee2974be93795c2b910fe58b47936f872b` |
| `edition/code/tests/test_observable_solver.py` | 6534 | Build only | `9bb806d59a0d3c0261261d342d83ce97dddb2eb41645894e6a2f2393ecced7f1` |
| `edition/code/tests/test_observable_torch_circle.py` | 7467 | Build only | `437b9f577621d854afc62171c285129fe424e1eb3ef406b680d8ddd3a72a1181` |
| `edition/code/tests/test_observable_validation.py` | 10671 | Build only | `e1ee08c217ce6f39e64801f1c2b64f71482fe6efe5ee8924fe36c6bacc0201c1` |
| `edition/code/tests/test_prediction_views.py` | 8452 | Full | `4d808ba2bb1a8e832685d09f6a843987eb969044bbe4eac08962d5f6ddead4f7` |
| `edition/code/tests/test_radial_data.py` | 10653 | Full | `4db24ee6165e6d00144fb0a77664052a0f60d951e0bf002090171962a8e6db58` |
| `edition/code/tests/test_radial_viewer.py` | 8548 | Full | `a37a4e2ab0e301bd8069146e1e9c2e2cce53e1c3c81e37168e6dadad85702c0a` |
| `edition/code/tools/book_pdf/README.md` | 5569 | Build only | `b1a56afd3ccd08cb860831e3aec0e2ae1ce9b8e3dacf74508d3342875a9b516e` |
| `edition/code/tools/book_pdf/build-pdf.sh` | 553 | Build only | `f826d05662cb7e8c340ef0dba7e1b70af7b9e94530f515f3dbf2b49d3ffef141` |
| `edition/code/tools/book_pdf/export_book.py` | 13532 | Build only | `0d94a5ef093164c00ac4581607b7161f1e1a7f58854100e1cb10e91611361cd1` |
| `edition/code/tools/book_pdf/layout.tex` | 4026 | Build only | `1a462590696ff0234e05e432e8a446f9150fdc198fbc555686913ebc5e417949` |
| `edition/code/tools/book_pdf/render_book.py` | 9631 | Build only | `0f0d4c4073bcdbec81276314692bbb777002efa4b5219ad3f7c4527495536370` |
| `edition/code/tools/check_library.py` | 4989 | Full | `c47052910683fff26a448f854a55a5f1378346836b9a8c03cccadc373d794054` |
| `edition/code/tools/two_layer_risk/README.md` | 9369 | Build only | `ad842c0921e88e996b999d52b8c4614961655fe5857b2329670de1911e5ee221` |
| `edition/code/tools/two_layer_risk/angle_error_bound.py` | 3566 | Build only | `cc3d750d096212016534056d35d221d6e7840a4a9f192379d283c093b0f94149` |
| `edition/code/tools/two_layer_risk/certificate.py` | 19375 | Build only | `773f8c90c08b17736fe3fb37213ecce6ef3fb5c848fd3ff2e4f73e8f9b909855` |
| `edition/code/tools/two_layer_risk/certificate_kernel.cpp` | 9050 | Build only | `a75b60a5615df7853e54179458ff8f0b5c646a5fe956eb87f31b1431c1251cc7` |
| `edition/code/tools/two_layer_risk/check_driver.py` | 7277 | Build only | `1f70dda734e117dca6ed25e1f2656242fbb085ee8cd0fd6f7ee9b7de8da9a4e2` |
| `edition/code/tools/two_layer_risk/check_kernel.py` | 7022 | Build only | `cc7f3fded02082eee118b5eecd0f947f39486eef27ea47d8095a828d62790be1` |
| `edition/code/validation/observable_horizon_plan.json` | 9890 | Build only | `b89c4a1ff7b8ed335e551f1ff553e7d3aefbe1acdfa914e19444901f080f08e7` |
| `edition/code/validation/observable_solver_plan.json` | 6086 | Build only | `92bf0cdd9cc5dc0147881ffc07c8235ed8e0480fd91631e7276c3e2e0b856e92` |
| `edition/docs/01-training-geometry.qmd` | 196333 | Build only | `ea3b9bf0d19ed2c1023f234737b58e9cb83fc641caf2f7e5ee5b249d30618711` |
| `edition/docs/02-gaussian-reuse.qmd` | 220638 | Build only | `a0f8175c8cd17c4d93aeb7174f2babe83e0917c4ed0f33862c7c9a89685d0a92` |
| `edition/docs/03-local-population.qmd` | 260226 | Build only | `3a6fc52191f815189337309f70e3fb822663b1532eedc54e4dea9402c3fdaebd` |
| `edition/docs/04-continuing-flows.qmd` | 308878 | Build only | `78728dbbcc551392f7dd6cf7b91bad42324e5b540655d4242e830e9c38774a43` |
| `edition/docs/05-continuation-boundaries.qmd` | 297648 | Build only | `fac83b5e732584387e673ebebf346617343561abde29e345a512757d278e40fd` |
| `edition/docs/06-architectures.qmd` | 119892 | Build only | `6831fc07f469eec40d30036b040c636972dab7fdcf9ed0cbd5e10e0f461c6078` |
| `edition/docs/07-observable-closure.qmd` | 279498 | Build only | `792aadb9fed6cf0e988ae5376c559bed14cbb0cdb2566fb29ad30c6d4d9fc6d2` |
| `edition/docs/08-autonomous-computation.qmd` | 271412 | Build only | `72224d6c545531a768e090ac24b681c58046de0a42b37105a9a6ad51316c8b54` |
| `edition/docs/08b-trajectory-compression.qmd` | 171652 | Build only | `bfa2effe1b7247026b38ceb7510aad47997b6a9d51b5541662c283e992d31e82` |
| `edition/docs/09-trainability.qmd` | 336547 | Build only | `26d92e4a77dc4bbebf56960ab578d46731a74f16c35885781e57c76cc2b964a2` |
| `edition/docs/10-correlated-pairs.qmd` | 279136 | Build only | `c9b6190ce38191055336e39a2584e67cba4526c5a4e8d59fecd8522606e0096d` |
| `edition/docs/11-shape-and-depth.qmd` | 408500 | Build only | `81014ee297553b03fa17669b9e30840723f7334b4dbbf4d9f85b11ef5760c3d8` |
| `edition/docs/12-three-sample-learning.qmd` | 274524 | Build only | `8c6ac8b00aaaa8210dd6f4ececd9996c62fee54b3e6eaee88a9eb2f57befdcc7` |
| `edition/docs/13-predictor-selection.qmd` | 286877 | Build only | `132c8c99ec8e32993ce9b06ecd60fd2b5a9d8854e109cc9d0d05ecc88d72ecf5` |
| `edition/docs/14-generalization.qmd` | 243546 | Build only | `2d1cddf57aea48ca596b2b2b3072e3fee5bc42f84223f6951cfe5cb8b396b766` |
| `edition/docs/_quarto.yml` | 1603 | Full | `18e7c1e8241f38e6637a4ac5954f5cc0289ac0704af01e9dccefb906b0ef6192` |
| `edition/docs/index.qmd` | 16358 | Full | `f9f46a53c71d7cc87d4848ab9f79a3d10df73f3f3ef5c7cb6ff47b07b19105d8` |
| `edition/docs/notation.qmd` | 5386 | Full | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |
| `edition/docs/outlook.qmd` | 46673 | Build only | `ab42accddea06a5e88160d6150ee118b09755733bdcb39d5c99849b02de8ffca` |
| `edition/docs/pdf_breakable_tables.lua` | 16495 | Build only | `dd08fd0aa5efc43bf7894d5688d0c2ecfdfbe1367259b09df5aa136b00f4dd48` |
| `edition/docs/references.bib` | 2263 | Build only | `4a542cec661036bc9e89dd06e383549191094fe6a03239c84fd67830baba07a5` |

Required skill inputs, each read in full:

| Skill path | SHA-256 |
|---|---|
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` | `daac37e41dca5e618c5baf2a65689000e526930f059b822ebec61aafbfd1abfc` |
| `/home/amir/.codex/skills/explain-with-canonical-notation/references/neural-response-memory.md` | `c2d570aac8950b5766513d81dd2dada4a9babeba92bbb554f1042107207a52b1` |

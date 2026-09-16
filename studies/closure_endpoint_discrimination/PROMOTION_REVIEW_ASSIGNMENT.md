# Neutral scientific review assignment: finite circle Torch backend

Review the frozen edition supplied in your assignment, verifying its
FROZEN_SHA256.json before and after work. You are an independent isolated
reviewer, distinct from every author, assembler and selector. Do not read
study history, old reports, selection notes, other reviewer outputs, chats or
live replacement dependencies. Read only this assignment, the frozen inputs
and required skills. Write your original complete report to the assigned flat
study path and scratch only in the assigned generated directory.

Authors/assemblers excluded from reviewer roles: current coordinator /root;
historical source contributor roles endpoint_gpu_runner, closure_order_design,
endpoint_design_audit named in the originating record. Selector /root/select_circle
is also excluded. The proposed code was extracted/rewritten by /root from a
study source using the maintained CPU backend. Names record provenance, not a
substitute for fresh context and actual independent work.

The new candidate comprises code/pde/observable_torch_circle.py,
code/tests/test_observable_torch_circle.py,
code/scripts/validate_torch_circle.py, and the final section of code/README.md
headed "Optional GPU backend for the finite circle closure". Also read the
complete code/tools/check_library.py and code/tests/test_library_boundary.py: the
checker adds declared optional Torch/psutil and local scripts imports to its
existing allowlist, so the standalone boundary check covers the optional backend
and existing supervisors. This is a structural check, not a proof validator. The entire guide,
docs/README.md, docs/NOTATION.md, AGENTS.md and RESEARCH_WORKFLOW.md are supplied
and must be read. No new book theorem or historical empirical accuracy/speedup
claim is proposed. All needed finite equations and numerical/storage scope are
in the new guide section. Existing population theorems are explicitly not
extended by this backend.

Read every line of new code, tests, recipe and proof/contract. Read complete
implementation dependencies: code/pde/__init__.py, finite_network.py,
gaussian_moments.py, observable_solver.py, observable_initialization.py,
observable_words.py, observable_arithmetic.py and observable_fixed.py. The
optional generic observable_compiler.py branch is not reached by orders 1,3,5;
verify that dispatch fact. It is supplied and read it if needed to resolve a
claim, rather than relying on excerpts. No older theorem proof is imported to
prove a new convergence result. The rest of the frozen established library is
preserved context, not a new whole-book audit. Declare exact older read scope
and unread complement; report missing inputs and repair any truncated read.

Audit supported p=1,3,5/d=2/float64 range, feature counts and redundant tails,
ridge/Cholesky initialization, retained joint marks, physical loss/mobilities,
true transpose, blocking, storage, precision handling, no hidden history,
ownership, validation, observed pairs/Grams and own-state continuation. Test
noninitial states, unequal weights/populations, boundaries, zero weights,
nonfinite arithmetic, and independent autograd/energy or finite differences.
Do not equate numerical parity with flow accuracy or trained-network convergence.

Execute the deterministic suite from the edition on CPU and CUDA if available:
PYTHONPATH=code CIRCLE_TEST_DEVICE=cpu CIRCLE_TEST_SCRATCH=<scratch>
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
/home/amir/miniconda3/bin/python -B code/tests/test_observable_torch_circle.py
Use the same with CIRCLE_TEST_DEVICE=cuda:0 and CUBLAS_WORKSPACE_CONFIG=:4096:8.
CUDA execution may require sandbox_permissions=require_escalated. Also audit
and execute the fixed producer recipe into a fresh data/established/<review>/
inside this edition; it uses at most three orders, tiny arrays and a 120-second
wall budget. No campaign, parameter search or retained data is needed. Do not
modify frozen sources; preserve all failures and report actual results.

Your full report must state isolation, complete read coverage and hashes,
actual commands/attacks/results, component verdicts and unresolved objections.
Required corrections block acceptance and require two new complete reviews of
a corrected packet. Suggestions must be separated from required corrections.
Do not silently repair the candidate or rely on another reviewer's findings.

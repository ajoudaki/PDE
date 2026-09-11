# Review B: deterministic Wick-check provenance

Preserved by `/root/research_review_b` on 2026-09-11 at the root task's request. This is evidence preservation only. The original review and both frozen scientific inputs were left unchanged.

`R1_REVIEW_B_WICK_CHECK.py` contains the exact Python source executed during the isolated review, originally supplied through standard input. It enumerates every Gaussian pairing for normalized `tr((WᵀW)^k)/n`, for `k=1,2,3`, with independent `N(0,1/n)` matrix entries. A pairing identifies row and column indices separately; its power of `n` is the total remaining index-class count minus `k+1`. The check uses integer counts, no random sampling, no training, and only Python's standard library. It is a low-order consistency check of the Gaussian forward/transpose calculation, not a replacement for the reviewed proof.

The preserved source was rerun in the fresh evidence directory:

`data/generated/training_law_stability/research_review_b/wick_check_20260911_01/`

The actual command, run with working directory `/home/amir/Codes/PDE`, was:

```text
python /home/amir/Codes/PDE/studies/training_law_stability/R1_REVIEW_B_WICK_CHECK.py
```

Rerun interpreter version: **Python 3.10.12**. The resolved executable is recorded in `python_executable.txt`; the literal version output is in `python_version.txt`. The rerun exited with code **0**, produced empty stderr, and reproduced the original recorded stdout byte for byte:

```text
k = 1 Wick count by power of n: {0: 1}
k = 2 Wick count by power of n: {0: 2, -1: 1}
k = 3 Wick count by power of n: {0: 5, -1: 6, -2: 4}
```

The evidence directory contains literal `command.txt`, `cwd.txt`, `stdout.txt`, `stderr.txt`, and `exit_code.txt`, as well as interpreter records and `SHA256SUMS.json`. That hash record covers the checker, these run artifacts, and the unchanged review and scientific inputs.

| Artifact | SHA-256 |
|---|---|
| Checker source | `fa7229658c313da594d02d430d6dcd0b5c82159aec09b3881307cf40460fb36a` |
| Literal stdout | `da46136bbcda531d6efca4bade6f1cd585c6590c8d7e2cb9f8a706ec47aec044` |
| Unchanged `R1_REVIEW_B.md` | `14f811d0ad837b5acdc9f814d3622d37fe064eef791f3df34dda2edc51c503af` |
| Unchanged `R1_PROOF.md` | `b7f2a65252353d0e47af50da9895f7206d4e202dd591ac4342bf6a2696e036c1` |
| Unchanged `R1_DEPENDENCIES.md` | `606fe87a97b91a8cad31a26d9e545c4b51ebefd582e55a7ba1b2311bfa2f9469` |

The original review did not record an interpreter version at the time of its inline check; the version above is explicitly the evidence-preservation rerun's version. No new scientific verdict or modification to the original report is made here.

# Proposed edition v1: deterministic validation record

The frozen scientific manifest is `scientific_manifest_v1.json`, SHA-256
`a64ca6999b833e24a45b9d63581950bada8306496a7008d7bab627c662865d9d`.
The proposed new C.4.10 is `candidate_addition_v1.md`, SHA-256
`0a0cf81422dfbea98661d2fe57b8ae04a02b245be8c1c1b997632605e42eb046`.
All inputs remained unchanged during the checks.

Command from `/home/amir/Codes/PDE`:

```text
python3 studies/nonlinear_selection_generalization/validate_edition_v1.py data/generated/nonlinear_selection_generalization/edition_validation_v1_20260912_01
```

Python 3.10.12, Linux x86_64; exit zero. Full generated report:
`data/generated/nonlinear_selection_generalization/edition_validation_v1_20260912_01/validation.json`.
The standalone selected-file edition is its `edition/` directory. It contains
the proposed full chapter, proposed full reading guide, unchanged notation,
the complete established special-data chapter and shared process guides.
The scientific check reads its inputs from that edition, without study
proofs, previous results or generated arrays.

Observed results:

- All exact rational assertions in the complete C.4.5.1.5 reference
  certificate passed again. Program hash
  `112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e`.
  Output: `[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]`.
- Exact rational checks of the robust Fourier norm and completed-square/
  contraction coefficients passed. Three inverse-Osgood checks had relative
  roundtrip error at most `1.22e-15`.
- The 103 new equation labels are distinct and do not collide with previous
  labels. Display/inline math delimiters balance, the new guide fragment
  resolves, and the addition has no study/generated-data dependency.
- All previous chapter bytes are preserved exactly. The assembled chapter
  hash is `6cb471fc5939b8317007817f61fa53eecb13ab125d80936d9aaac4ff300f61af`;
  proposed reading guide hash is
  `d149815d53784b9093bf22608456a19eabfa91a2cca8c6f0d60df9a187ed313c`.

These are deterministic checks, not experiments or a proof audit. They do
not certify the analytic continuation, separation, learning or transfer
arguments. No training was run, no empirical result is claimed, and no
unrelated exporter/API was changed or tested. Existing links outside the
new addition and unread older scientific content were not re-audited.

The packet was committed as
`13dd024d516f490ea85d5c65878125f089f37f7e`, after a nonblocking shared writer
lock, exact staged-set and file-hash checks. The first whitespace check
reported only the exact frozen extracts' inherited final blank lines; these
were preserved to keep source bytes and review hashes unchanged. The resumed
locked transaction disabled only the `blank-at-eof` check and passed all
remaining whitespace checks. No unrelated staged or working file was adopted.

Before packet freezing, root made two explicit continuation assembly
clarifications: finite capture uses `epsilon in (0,epsilon_0)`, and NSC47's
tail average includes both anchor queries with their full mixture weights.
The continuation author acknowledged both. Its final assembled unit hash
is in the scientific manifest. No scientific-review input has changed since
the packet was dispatched.

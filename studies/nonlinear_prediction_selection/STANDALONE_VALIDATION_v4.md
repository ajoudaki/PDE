# Standalone proposed-edition validation

Coordinator validation, not an independent review. A fresh documentation-only
standalone edition was built without changing established files. Every frozen
scientific review input hash and its unchanged scientific source hash matched.
The current guide baseline was checked separately; the two scoped additions
preserve its complete concurrent roadmap byte for byte. The entire older
global chapter was recovered by reversing the one scope insertion and removing
the append; every other documentation file except the proposed guide was
preserved byte for byte. New chapter links, equation labels and math delimiter
balance passed, and the exact upstream rational certificate passed again.

Exact run record:

```json
{
  "python": "3.10.12",
  "command": "python studies/nonlinear_prediction_selection/validate_proposed_edition_v4.py",
  "output_directory": "/home/amir/Codes/PDE/data/generated/nonlinear_prediction_selection/standalone_v4",
  "candidate_sha256": "c858c7b41d90b490871450b8bf7494afe8c6cd7f39bebd3f1faa89f3604a5879",
  "integration_baseline_guide_sha256": "3f341b52fa6449a4008602f573590b1528158bd1370f17bc26db032813799f5e",
  "preserved_concurrent_guide_lines": 293,
  "proposed_global_sha256": "7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465",
  "proposed_guide_sha256": "26c5f81ad355b892430e015a786df1d0e2e4f6c9a1fc920ea634bd311558412e",
  "notation_sha256": "199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b",
  "preserved_other_documentation_files": 8,
  "new_links_checked": [
    {
      "from": "docs/global_nonlinear.md",
      "target": "#c49-nonlinear-prediction-selection-during-a-finite-added-data-episode"
    },
    {
      "from": "docs/README.md",
      "target": "global_nonlinear.md#c49-nonlinear-prediction-selection-during-a-finite-added-data-episode"
    }
  ],
  "certificate_exit": 0,
  "certificate_output": "[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]",
  "certificate_stdout_sha256": "ad40e8d8f73fed6d22cc9b68a19f7f9e6c3f2f59383d581e372ce0c976786900",
  "patch_sha256": "f15934b5cf3b2b9db9bc7bab32109a8146ba9f0d31baef36d99a89ca9a0c3dbd",
  "limitations": [
    "No new training experiment or empirical claim.",
    "No full-book mathematical audit of the unchanged complement.",
    "No whole-book link audit: newly introduced links checked and older files/links preserved.",
    "No changes applied to established book or code."
  ]
}
```

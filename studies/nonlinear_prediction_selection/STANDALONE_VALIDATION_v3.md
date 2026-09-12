# Standalone proposed-edition validation

Coordinator validation, not an independent review. A fresh documentation-only
standalone edition was built without changing established files. Every frozen
review input hash and its established source hash matched. The entire older
global chapter was recovered by reversing the one scope insertion and removing
the append; every other documentation file except the proposed guide was
preserved byte for byte. New chapter links, equation labels and math delimiter
balance passed, and the exact upstream rational certificate passed again.

Exact run record:

```json
{
  "python": "3.10.12",
  "command": "python studies/nonlinear_prediction_selection/validate_proposed_edition_v3.py",
  "output_directory": "/home/amir/Codes/PDE/data/generated/nonlinear_prediction_selection/standalone_v3",
  "candidate_sha256": "c858c7b41d90b490871450b8bf7494afe8c6cd7f39bebd3f1faa89f3604a5879",
  "proposed_global_sha256": "7633fb054cf02f2359b193fcb090634304cc1153f4d8f978fd0ac30789355465",
  "proposed_guide_sha256": "d5ecdfd35fbddd511d98dccd148a9a9e840f5a4c814658f930c5732bab218bc5",
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
  "patch_sha256": "ce121bad1089ca01e471c5c0a20fbfb8ef58f428258eba6b36ae9dd7e7b5b573",
  "limitations": [
    "No new training experiment or empirical claim.",
    "No full-book mathematical audit of the unchanged complement.",
    "No whole-book link audit: newly introduced links checked and older files/links preserved.",
    "No changes applied to established book or code."
  ]
}
```

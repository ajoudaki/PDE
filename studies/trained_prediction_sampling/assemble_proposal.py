"""Assemble the reviewable book addition without changing established files."""
import hashlib
import json
from pathlib import Path
import re

STUDY = Path(__file__).resolve().parent


def read(name):
    return (STUDY / name).read_text()


def subsection(text):
    return re.sub(r"^#{2,3} ", "###### ", text, flags=re.MULTILINE)


def assemble():
    completion = read("canonical_completion.md")
    setup = completion.split("## 1. Model, spaces, and statement\n", 1)[1]
    setup, rest = setup.split("## 2. The finite estimate needed for the passage\n", 1)
    passage, interpretation = rest.split("## 5. Sampling, covariance, and the mean-square strengthening\n", 1)
    source = read("canonical_source_lemma.md").split(
        "## Uniform first and second derivatives of the population Euler output\n", 1)[1]
    sampling = read("canonical_sampling_lemma.md").split("## Statement\n", 1)[1]
    # Reserve rho for normalized testing-circle measure in the enclosing theorem.
    sampling = sampling.replace("\\rho", "r_{\\rm loc}")
    text = (
        "### C.4.8. Sampling fluctuations of the trained prediction\n\n"
        "Unqualified equation labels below belong to this proof unit. The finite-source "
        "and statistical lemmas state their local notation explicitly.\n\n"
        "##### Model and theorem\n\n" + setup
        + "##### C.4.8.1. Uniform first and second finite-program responses\n\n"
        + subsection(source)
        + "\n##### C.4.8.2. Actual influence for Borel laws\n\n"
        + "###### Finite estimate and actual value completion\n\n"
        + subsection(passage)
        + "\n##### C.4.8.3. A Hilbert sampling lemma\n\n"
        + "###### Statement\n\n" + subsection(sampling)
        + "\n##### C.4.8.4. Covariance and finite-network interpretation\n\n"
        + "###### Sampling and the mean-square strengthening\n\n"
        + subsection(interpretation)
    )
    text = text.replace("the conclusion to be assembled is:", "the following conclusions hold:")
    text = text.replace("The source lemma applies", "The lemma in C.4.8.1 applies")
    text = text.replace("the canonical source lemma", "the source lemma in C.4.8.1")
    text = text.replace("The canonical source lemma", "The source lemma in C.4.8.1")
    text = text.replace("the canonical sampling lemma", "the sampling lemma in C.4.8.3")
    text = text.replace("the lemma's finite-continuous-test", "the lemma's finite-continuous-test")
    text = re.sub(r"(?<=\\tag\{)([PSR]\d+)(?=\})", r"C.4.8.\1", text)
    text = re.sub(r"\(([PSR]\d+)\)", r"(C.4.8.\1)", text)
    if re.search(r"\b(draft|awaiting|study|assembled|unproved)\b", text, re.I):
        raise ValueError("Unresolved editorial status word in proposed mathematical text")
    tags = re.findall(r"\\tag\{([^}]+)\}", text)
    assert len(tags) == len(set(tags)), "Duplicate equation tag"
    used = set(re.findall(r"\((C\.4\.8\.[PSR]\d+)\)", text))
    assert used <= set(tags), sorted(used - set(tags))
    destination = STUDY / "proposal_C4_8.md"
    destination.write_text(text.rstrip() + "\n")
    summary = (
        "Section C.4.8 gives the actual centered influence and an L2(circle) Gaussian "
        "sampling limit at T=40 for every separately fixed Borel law in a smaller "
        "neighborhood, with spatial covariance, a mean-square remainder and a "
        "width-first finite-GF bridge."
    )
    edits = {
        "append": {"path": "docs/global_nonlinear.md", "source": "proposal_C4_8.md"},
        "replacements": [
            {"path": "docs/global_nonlinear.md",
             "old": "a width-first bridge to C.4.6. The local C.4.1–C.4.4 theorem retains the",
             "new": "a width-first bridge to C.4.6. " + summary + "\nThe local C.4.1–C.4.4 theorem retains the"},
            {"path": "docs/README.md",
             "old": "and gives a finite-contamination remainder with a width-first bridge to the response. |",
             "new": "and gives a finite-contamination remainder with a width-first bridge to the response. "
                    + summary.replace("Section C.4.8", "[Section C.4.8](global_nonlinear.md#c48-sampling-fluctuations-of-the-trained-prediction)") + " |"},
            {"path": "docs/README.md",
             "old": "have the stated neighborhood and fixed horizon.",
             "new": "have the stated neighborhood and fixed horizon. " + summary},
        ],
    }
    (STUDY / "promotion_edits.json").write_text(json.dumps(edits, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"candidate": str(destination), "lines": len(text.splitlines()),
                      "tags": len(tags),
                      "sha256": hashlib.sha256(destination.read_bytes()).hexdigest()}, indent=2))


if __name__ == "__main__":
    assemble()

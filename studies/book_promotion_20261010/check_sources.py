"""Check frozen proof bytes and local compact-paper reference completeness."""
import hashlib
import json
from pathlib import Path
import re
import tarfile


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def check():
    study = Path(__file__).resolve().parent
    repository = study.parent.parent
    records = json.loads((study / "sources.json").read_text())["sources"]
    texts, changed_sources = [], []
    for record in records:
        source = repository / record["source"]
        if not source.exists() or sha256(source.read_bytes()) != record["sha256"]:
            changed_sources.append(record["source"])
        if record["snapshot"] is None:
            continue
        data = (study / record["snapshot"]).read_bytes()
        assert len(data) == record["bytes"] and sha256(data) == record["sha256"], record
        texts.append(data.decode())
    assert len(texts) == 5
    # Remove TeX comments, retaining escaped percent signs.
    text = "\n".join(re.sub(r"(?<!\\)%.*", "", value) for value in texts)
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    references = re.findall(r"\\(?:ref|eqref|autoref|cref|Cref)\{([^}]+)\}", text)
    targets = {item.strip() for group in references for item in group.split(",")}
    assert len(labels) == len(set(labels)), "Duplicate compact-paper labels"
    assert not targets - set(labels), sorted(targets - set(labels))
    included = re.findall(r"\\input\{([^}]+)\}", text)
    assert len(included) == 4
    for name in included:
        path = Path(name)
        assert path.parent == Path(".") and path.name.startswith("compact_")
        assert (study / path.with_suffix(".tex")).is_file(), name

    older = json.loads((study / "older_sources.json").read_text())
    with tarfile.open(study / "older_theory_sources.tar.gz", "r:gz") as archive:
        members = {member.name: member for member in archive if member.isfile()}
        assert set(members) == {record["archive_path"] for record in older}
        for record in older:
            data = archive.extractfile(members[record["archive_path"]]).read()
            assert len(data) == record["bytes"]
            assert sha256(data) == record["archive_sha256"], record["id"]
    return dict(status="PASS", compact_files=len(texts), compact_labels=len(labels),
                compact_reference_uses=len(references), proof_includes=len(included),
                archived_source_items=len(older),
                live_contract_or_manuscript_drift=changed_sources)


if __name__ == "__main__":
    print(json.dumps(check(), indent=2))

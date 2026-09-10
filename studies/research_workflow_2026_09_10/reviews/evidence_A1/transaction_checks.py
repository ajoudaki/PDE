"""Additional bounded transaction and baseline-parser checks against frozen helper."""

import contextlib
import importlib.util
import io
from pathlib import Path
import shutil
import tempfile
from types import SimpleNamespace
from unittest import mock

ROOT = Path(__file__).parents[4]
AREA = Path(__file__).parent
spec = importlib.util.spec_from_file_location("frozen_helper", ROOT / "studies/_workflow.py")
wf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wf)

with mock.patch.object(wf.subprocess, "run") as run:
    for status, text, expected in (
        (0, "a" * 40 + "\n", "a" * 40),
        (0, "b" * 64 + "\n", "b" * 64),
        (128, "a" * 40, None),
        (0, "not-a-commit", None),
    ):
        run.return_value = SimpleNamespace(returncode=status, stdout=text)
        assert wf.baseline(ROOT) == expected
    run.side_effect = OSError("synthetic Git executable unavailable")
    assert wf.baseline(ROOT) is None
print("PASS baseline parser: SHA1/SHA256-shaped IDs, command failure, malformed stdout, missing executable; all mocked")


def shell_root():
    root = Path(tempfile.mkdtemp(prefix="transactions-", dir=AREA))
    (root / "README.md").write_text("Synthetic repository\n")
    (root / "data").mkdir()
    (root / "studies").mkdir()
    return root


for adopt in (False, True):
    root = shell_root()
    study = root / "studies/demo"
    if adopt:
        study.mkdir()
        (study / "README.md").write_bytes(b"Existing adopted record\x00\xff")
    initial = {p.name: p.read_bytes() for p in study.iterdir()} if adopt else None
    real = wf.write_new
    count = 0
    def interrupted_write(path, content):
        global count
        count += 1
        if count == 3:
            raise OSError("synthetic third-file failure")
        real(path, content)
    output = io.StringIO()
    with mock.patch.object(wf, "baseline", return_value=None), mock.patch.object(wf, "write_new", side_effect=interrupted_write), contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
        result = wf.main(["adopt" if adopt else "start", "demo", "--question", "q", "--owner", "owner"], root=root)
    assert result == 1
    if adopt:
        assert {p.name: p.read_bytes() for p in study.iterdir()} == initial
    else:
        assert not study.exists()
    shutil.rmtree(root)
    print("PASS", "adopt" if adopt else "start", "third-file interruption rollback; prior bytes preserved")

print("ALL BASELINE/PARTIAL-WRITE CHECKS COMPLETED")

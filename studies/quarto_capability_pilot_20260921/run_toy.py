"""Render the frozen artificial fixture in a fresh generated directory."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument("--quarto", type=Path, required=True)
parser.add_argument("--run-directory", type=Path, required=True)
args = parser.parse_args()
source = Path(__file__).resolve().parent
run = args.run_directory.resolve()
project = run / "book"
project.mkdir(parents=True, exist_ok=False)
quarto = str(args.quarto.resolve())
names = ["_quarto.yml", "index.qmd", "first.qmd", "second.qmd",
         "references.qmd", "_included.md", "references.bib"]
hashes = {}
for name in names:
    shutil.copyfile(source / name, project / name)
    hashes[name] = hashlib.sha256((source / name).read_bytes()).hexdigest()
(run / "source_hashes.json").write_text(json.dumps(hashes, indent=2) + "\n")
env = dict(os.environ)
env["XDG_CACHE_HOME"] = str(run / "cache")
env["XDG_CONFIG_HOME"] = str(run / "config")
commands = []
for fmt in ["html", "pdf", "latex"]:
    command = [quarto, "render", "--to", fmt, "--output-dir", "_out-" + fmt]
    if fmt == "latex":
        command += ["-M", "cite-method:biblatex"]
    started = time.monotonic()
    with (run / (fmt + ".log")).open("w") as log:
        result = subprocess.run(command, cwd=project, env=env, stdout=log,
                                stderr=subprocess.STDOUT, timeout=180)
    item = {"command": command, "cwd": str(project),
            "exit_code": result.returncode,
            "seconds": round(time.monotonic() - started, 2)}
    commands.append(item)
    (run / "commands.json").write_text(json.dumps(commands, indent=2) + "\n")
    print(fmt, result.returncode, item["seconds"], flush=True)
print("Generated evidence:", run, flush=True)
raise SystemExit(1 if any(item["exit_code"] for item in commands) else 0)

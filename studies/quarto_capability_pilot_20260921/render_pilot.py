"""Render a frozen pilot copy, never the maintained book or study source in place."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import time

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--quarto',type=Path,required=True)
parser.add_argument('--run-directory',type=Path,required=True)
args=parser.parse_args()
source=Path(__file__).resolve().parent
run=args.run_directory.resolve(); book=run/'book'
book.mkdir(parents=True,exist_ok=False)
files={'pilot_quarto.yml':'_quarto.yml','pilot_index.qmd':'index.qmd',
       'pilot_linear.qmd':'pilot_linear.qmd','pilot_notation_resource.md':'NOTATION.md'}
for a,b in files.items():
    shutil.copyfile(source/a,book/b)
(run/'source_hashes.json').write_text(json.dumps({a:hashlib.sha256((source/a).read_bytes()).hexdigest() for a in files},indent=2)+'\n')
env=dict(os.environ,XDG_CACHE_HOME=str(run/'cache'),XDG_CONFIG_HOME=str(run/'config'))
commands=[]
for fmt in ['html','pdf','latex']:
    cmd=[str(args.quarto.resolve()),'render','--to',fmt,'--output-dir','_out-'+fmt]
    start=time.monotonic()
    with (run/(fmt+'.log')).open('w') as log:
        proc=subprocess.run(cmd,cwd=book,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=180)
    # PDF export does not consistently copy declared downloadable resources.
    if proc.returncode == 0:
        shutil.copyfile(book/'NOTATION.md',book/('_out-'+fmt)/'NOTATION.md')
    commands.append(dict(command=cmd,cwd=str(book),exit_code=proc.returncode,seconds=round(time.monotonic()-start,2)))
    (run/'commands.json').write_text(json.dumps(commands,indent=2)+'\n')
    print(fmt,proc.returncode,flush=True)
raise SystemExit(1 if any(c['exit_code'] for c in commands) else 0)

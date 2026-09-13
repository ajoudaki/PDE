# Retained verbatim command body from the executed inline rendering check.
# This copy was saved after that execution and has not been rerun.
import resource,subprocess,time,json
from pathlib import Path
scratch=Path('data/generated/observable_hierarchy/H3_v2_integration_v4').resolve()
resource.setrlimit(resource.RLIMIT_CPU,(60,60));resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
command=['xelatex','-interaction=nonstopmode','-halt-on-error','-no-shell-escape','-output-directory',str(scratch),str(scratch/'section_math.tex')]
start=time.monotonic()
with (scratch/'math_render.log').open('x') as log:r=subprocess.run(command,cwd=scratch,stdout=log,stderr=subprocess.STDOUT)
u=resource.getrusage(resource.RUSAGE_CHILDREN)
x=dict(command=command,exit_code=r.returncode,cpu_seconds=u.ru_utime+u.ru_stime,wall_seconds=time.monotonic()-start,peak_rss_bytes=u.ru_maxrss*1024)
(scratch/'math_render_result.json').write_text(json.dumps(x,indent=2)+'\n');print(json.dumps(x))
print((scratch/'math_render.log').read_text()[-3500:])

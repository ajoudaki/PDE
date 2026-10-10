from pathlib import Path
import subprocess,json,sys,hashlib,os
s=Path('../reviewer_one'); results=[]
assert os.environ['PYTHONPATH']=='code'
commands=[['code/scripts/example_mfp_calculus.py'],['code/scripts/example_mfp_mlp_derivative.py'],['code/scripts/example_mfp_kernel_jets.py','--activation','identity'],['code/scripts/example_mfp_calculus.py','--json'],['code/scripts/example_mfp_mlp_derivative.py','--activation','cubic','--json']]
for i,tail in enumerate(commands):
 cmd=[sys.executable,'-B',*tail]
 proc=subprocess.run(cmd,capture_output=True,text=True)
 output=s/f'guide_corrected_command_{i+1}.log';output.write_text(proc.stdout+proc.stderr)
 results.append({'command':cmd,'cwd':str(Path.cwd()),'environment':{'PYTHONPATH':os.environ['PYTHONPATH'],'PYTHONDONTWRITEBYTECODE':os.environ['PYTHONDONTWRITEBYTECODE']},'exit_code':proc.returncode,'output':str(output),'sha256':hashlib.sha256(output.read_bytes()).hexdigest()})
 assert proc.returncode==0,results[-1]
 if '--json' in tail:json.loads(proc.stdout)
(s/'guide_commands.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))

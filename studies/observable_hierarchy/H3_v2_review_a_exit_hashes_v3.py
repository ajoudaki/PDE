import pathlib,json,hashlib,resource,time
resource.setrlimit(resource.RLIMIT_CPU,(10,10))
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.process_time();root=pathlib.Path('/home/amir/Codes/PDE');out=pathlib.Path(__file__).parent
entry=json.loads((out/'entry_hashes.json').read_text());result=[]
for item in entry:
    p=root/item['path'];actual=hashlib.sha256(p.read_bytes()).hexdigest()
    result.append(dict(path=item['path'],expected=item['expected'],entry_sha256=item['actual'],exit_sha256=actual,ok=actual==item['actual']==item['expected']))
record={'files':result,'count':len(result),'status':'pass' if all(x['ok'] for x in result) else 'fail','cpu_seconds':time.process_time()-start}
(out/'exit_hashes.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({k:v for k,v in record.items() if k!='files'}));assert record['status']=='pass'

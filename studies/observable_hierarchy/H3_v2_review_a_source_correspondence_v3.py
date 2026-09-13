import pathlib,re,json,time,resource,hashlib
resource.setrlimit(resource.RLIMIT_CPU,(50,50))
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.process_time();r=pathlib.Path('/home/amir/Codes/PDE/data/generated/observable_hierarchy/H3_v2_edition_v2')
text=(r/'review/dependencies.md').read_text()
matches=list(re.finditer(r'^Source: `([^`]+)`; ([^\n]+)\n\n',text,re.M));results=[]
for i,m in enumerate(matches):
    body=text[m.end():matches[i+1].start() if i+1<len(matches) else len(text)].rstrip()
    if body.endswith('---'):body=body[:-3].rstrip()
    book=(r/m.group(1)).read_text();offset=book.find(body)
    results.append({'source':m.group(1),'scope':m.group(2),'body_sha256':hashlib.sha256(body.encode()).hexdigest(),'complete_exact_substring':offset>=0,'source_line_start':book[:offset].count('\n')+1 if offset>=0 else None,'selected_lines':len(body.splitlines())})
body=(r/'review/proposed_section.md').read_text().rstrip();book=(r/'docs/global_nonlinear.md').read_text();offset=book.find(body)
results.append({'source':'docs/global_nonlinear.md','scope':'proposed C.4.7.10','body_sha256':hashlib.sha256(body.encode()).hexdigest(),'complete_exact_substring':offset>=0,'source_line_start':book[:offset].count('\n')+1 if offset>=0 else None,'selected_lines':len(body.splitlines())})
result={'selections':results,'status':'pass' if all(x['complete_exact_substring'] for x in results) else 'correspondence_needs_inspection','cpu_seconds':time.process_time()-start}
(pathlib.Path(__file__).parent/'source_correspondence.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

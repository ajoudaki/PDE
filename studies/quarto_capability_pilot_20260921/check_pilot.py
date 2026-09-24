"""Check this frozen packet by reversing only its explicitly allowed edits.

This is a preservation checker, not a general Markdown parser or a proof checker.
The independent audit must also validate the conversion contract and boundaries.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
MANIFEST = json.loads((HERE / "pilot_manifest.json").read_text())
SOURCE = (HERE / "pilot_source.md").read_text()
ENV = re.compile(r'^::: \{([^\n]+)\}\n(.*?)^:::[ \t]*$', re.M | re.S)
MARKER = re.compile(r'^<!-- source-block: ([a-z-]+) -->[ \t]*\n', re.M)
OLD_MATH = re.compile(r'\\\[(.*?)\\\]|\\\((.*?)\\\)', re.S)
NEW_MATH = re.compile(r'\$\$(.*?)\$\$|(?<![\\$])\$(?!\$)(.*?)(?<!\\)\$(?!\$)', re.S)


def compact(text):
    return re.sub(r'\s+', ' ', text).strip()


def without_env(match):
    attrs, body = match.groups()
    for item in MANIFEST['statements']:
        if attrs == '#' + item['id'] and item['title']:
            body = re.sub(r'^\s*## ' + re.escape(item['title']) + r'\s*\n', '', body, count=1)
    return body


def normalize(text, candidate=False):
    if candidate:
        text = ENV.sub(without_env, text)
        text = MARKER.sub('', text)
        text = re.sub(r'\s*\{#(?:eq|sec)-[a-z0-9-]+\}', '', text)
    else:
        for item in MANIFEST['statements'] + MANIFEST['proofs']:
            text = text.replace(item['prefix'], '')
        text = text.replace(r'\(\square\)', '')
        for section in MANIFEST['sections']:
            bare = re.sub(r'^(#+ )\d+(?:\.[A-Z])?\. ', r'\1', section['old'])
            text = text.replace(section['old'], bare)

    def math(match):
        payload = next(x for x in match.groups() if x is not None)
        payload = re.sub(r'\\tag\{[^}]+\}', '', payload) if not candidate else payload
        # Preserve a whitespace boundary; never merge separate words/commands.
        return '\x01MATH:' + compact(payload) + '\x02'

    text = (NEW_MATH if candidate else OLD_MATH).sub(math, text)
    # Work only on prose, leaving every mathematical expression untouched.
    chunks = re.split(r'(\x01MATH:.*?\x02)', text, flags=re.S)
    for n in range(0, len(chunks), 2):
        prose = chunks[n]
        if candidate:
            prose = re.sub(r'@(eq|thm|lem|cor)-[a-z0-9-]+', lambda m: 'REF[' + m.group() [1:] + ']', prose)
        else:
            for item in MANIFEST['equations']:
                prose = prose.replace('(' + item['tag'] + ')', 'REF[' + item['id'] + ']')
            for item in sorted(MANIFEST['statements'], key=lambda x: -len(x['old'])):
                prose = re.sub(re.escape(item['old']) + r'(?![\w.])', 'REF[' + item['id'] + ']', prose)
        chunks[n] = prose
    return compact(''.join(chunks))


def snippet_difference(expected, actual):
    stop = next((i for i, (a, b) in enumerate(zip(expected, actual)) if a != b), min(len(expected), len(actual)))
    return {'at': stop, 'expected': expected[max(0,stop-90):stop+200],
            'actual': actual[max(0,stop-90):stop+200]}


def verify(candidate):
    failures = []
    def need(condition, message):
        if not condition:
            failures.append(message)
    need(hashlib.sha256(SOURCE.encode()).hexdigest() == MANIFEST['source_excerpt_sha256'], 'source hash')
    markers = list(MARKER.finditer(candidate))
    need([m[1] for m in markers] == [b['id'] for b in MANIFEST['blocks']], 'coverage/order markers')
    blocks = []
    lines = SOURCE.splitlines(keepends=True)
    if len(markers) == len(MANIFEST['blocks']):
        need(not candidate[:markers[0].start()].strip(), 'unexpected content before first block')
        for i, (marker, block) in enumerate(zip(markers, MANIFEST['blocks'])):
            old = ''.join(lines[block['start']-1:block['end']])
            new = candidate[marker.end():markers[i+1].start() if i+1<len(markers) else len(candidate)]
            a, b = normalize(old), normalize(new, True)
            item = dict(id=block['id'], source_lines=[block['start'],block['end']],
                        candidate_lines=[candidate[:marker.start()].count('\n')+1,
                                         candidate[:markers[i+1].start()].count('\n') if i+1<len(markers) else len(candidate.splitlines())],
                        exact_after_allowed_normalization=a == b)
            if a != b:
                item['difference'] = snippet_difference(a,b)
                failures.append('content preservation: '+block['id'])
            blocks.append(item)

    labels = re.findall(r'\{#([a-z0-9-]+)\}', candidate)
    expected_labels = [s['id'] for s in MANIFEST['sections']+MANIFEST['equations']+MANIFEST['statements']]
    need(sorted(labels) == sorted(expected_labels), 'label inventory/duplicates')
    expected_displays = []
    for m in OLD_MATH.finditer(SOURCE):
        if m[1] is not None:
            tag = re.search(r'\\tag\{([^}]+)\}',m[1])
            expected_displays.append('eq-linear-'+tag[1].lower().replace('.','-') if tag else None)
    actual_displays = [m[2] for m in re.finditer(r'\$\$(.*?)\$\$(?: \{#([^}]+)\})?',candidate,re.S)]
    need(actual_displays == expected_displays, 'display count/labels/order')
    for display in re.finditer(r'^\$\$\n.*?^\$\$(?: \{#[^}]+\})?[ \t]*$', candidate, re.M|re.S):
        before, after = candidate[:display.start()], candidate[display.end():]
        need(not before or before.endswith('\n\n'), 'display lacks preceding blank line')
        need(not after.strip() or after.startswith('\n\n'), 'display lacks following blank line')
        need(not re.search(r'\n[ \t]*\n', display.group()), 'blank paragraph inside display math')
    need('\\tag{' not in candidate and '\\[' not in candidate and '\\(' not in candidate,
         'unconverted delimiters/tags')

    envs = list(ENV.finditer(candidate))
    expected_envs = sorted(MANIFEST['statements']+MANIFEST['proofs'],key=lambda x:x['start'])
    need(len(envs)==len(expected_envs), 'environment count')
    for match, item in zip(envs,expected_envs):
        attrs, body = match.groups()
        expected_attrs = '#'+item['id'] if 'id' in item else '.proof'+(' name="'+item['name']+'"' if item['name'] else '')
        need(attrs==expected_attrs, 'environment type/order: '+expected_attrs)
        if item.get('title'):
            need(body.lstrip().startswith('## '+item['title']+'\n'), 'environment title: '+expected_attrs)
            body = re.sub(r'^\s*## '+re.escape(item['title'])+r'\s*\n','',body,count=1)
        old=''.join(lines[item['start']-1:item['end']])
        need(normalize(old)==normalize(body,True), 'environment boundary/content: '+expected_attrs)
    stripped = ENV.sub(without_env,candidate)
    headings = re.findall(r'^(#+ .+)$',stripped,re.M)
    expected_headings=[re.sub(r'^(#+ )\d+(?:\.[A-Z])?\. ',r'\1',s['old'])+' {#'+s['id']+'}' for s in MANIFEST['sections']]
    need(headings==expected_headings,'heading hierarchy/titles/order')
    refs = re.findall(r'@([a-z]+-[a-z0-9-]+)',candidate)
    need(set(refs)<=set(labels),'unresolved native references')
    for pending in MANIFEST['pending']:
        need(candidate.count(pending['text'])==1,'pending reference altered: '+pending['text'])
    return {'pass': not failures,'failures':failures,'mapping':blocks,'native_labels':len(labels),
            'native_reference_occurrences':len(refs),'display_equations':len(actual_displays),
            'formal_statements':len(MANIFEST['statements']),'proofs':len(MANIFEST['proofs']),
            'pending':MANIFEST['pending'],'candidate_sha256':hashlib.sha256(candidate.encode()).hexdigest()}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('candidate',type=Path)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--fault-tests',action='store_true',help='Inject nine representative defects in memory; each must fail.')
    args=parser.parse_args()
    candidate=args.candidate.read_text()
    result=verify(candidate)
    if args.fault_tests:
        cases={
            'math_constant':candidate.replace('K(0)=4','K(0)=5',1),
            'claim_qualifier':candidate.replace('no additional width/step','an additional width/step',1),
            'valid_but_wrong_reference':candidate.replace('@lem-linear-trace-class','@lem-linear-gaussian-words',1),
            'duplicate_label':candidate.replace('{#eq-linear-1-2}','{#eq-linear-1-1}',1),
            'dropped_sentence':candidate.replace('The common mobility $\\kappa$ is outside $K_n$. ',''),
            'missing_mapping_block':candidate.replace('<!-- source-block: trace-class -->\n','',1),
            'expanded_theorem':candidate.replace('finite-width assertion is made.\n\n:::\n\nThe proof first packages',
                'finite-width assertion is made.\n\nThe proof first packages',1).replace('the exact-GD bridge.\n','the exact-GD bridge.\n\n:::\n',1),
            'missing_display_separation':candidate.replace('has an expansion\n\n$$','has an expansion\n$$',1),
            'blank_paragraph_in_math':candidate.replace('s_2\\ge\\cdots>0,\n$$','s_2\\ge\\cdots>0,\n \n$$',1),
        }
        controls={}
        for name,bad in cases.items():
            found=verify(bad)
            controls[name]={'changed':bad!=candidate,'rejected':not found['pass'],'failures':found['failures']}
        result['negative_controls']=controls
        result['pass']=result['pass'] and all(c['changed'] and c['rejected'] for c in controls.values())
    output=json.dumps(result,indent=2)+'\n'
    if args.output:
        args.output.write_text(output)
    print(output,end='')
    raise SystemExit(0 if result['pass'] else 1)

from pathlib import Path
from fractions import Fraction as F
from math import factorial, comb, isqrt
from functools import lru_cache
import ast, difflib, hashlib, json, re, runpy

root = Path('/home/amir/Codes/PDE')
study = root/'studies/two_layer_test_risk'
out = root/'data/generated/two_layer_test_risk/canonical_check_20260910_01'
checks = {}
def record(name, value):
    checks[name] = value
    assert value, name

# Rebuild the two candidates in memory; intercept both writes.
namespace = runpy.run_path(str(study/'build_signed_candidate.py'))
captured = {}
original_write = Path.write_text
def capture(path, content, *args, **kwargs):
    captured[path.name] = content
    return len(content)
Path.write_text = capture
try:
    namespace['main']()
finally:
    Path.write_text = original_write
for name, content in captured.items():
    record('builder_identical_'+name, content == (study/name).read_text())

candidate = (study/'PROMOTION_SIGN_C4.md').read_text()
sections = re.split(r'(?=^#### C\.4 certificate:)', candidate, flags=re.M)
source_ranges = {
 'base': (study/'PROMOTION_C4.md').read_text(),
 'error': (study/'CERTIFIED_ERROR.md').read_text(),
 'engine': (study/'CERTIFICATION_ENGINE.md').read_text(),
 'angle': (study/'ANGULAR_CERTIFICATE.md').read_text(),
 'driver': (study/'DRIVER_CERTIFICATION.md').read_text(),
}
for index, (name, source) in enumerate(source_ranges.items()):
    canon = sections[index]
    canon = re.sub(r'^##### ', '## ', canon, flags=re.M)
    canon = re.sub(r'C4\.([EAD]\d+)\b', r'\1', canon)
    diff = ''.join(difflib.unified_diff(source.splitlines(True), canon.splitlines(True),
                                      fromfile=name+'_source', tofile=name+'_canonical'))
    (out/(name+'_correspondence.diff')).write_text(diff)

tags = re.findall(r'\\tag\{([^}]+)\}',candidate)
refs = set(re.findall(r'\((C4\.[A-Z]?\d+[a-z]?)\)',candidate))
record('unique_equation_tags', len(tags)==len(set(tags)))
record('all_local_equation_references_resolve', not (refs-set(tags)))
checks['equation_tag_count'] = len(tags)

chi = (F(5358604107658561212253567,19807040628566084398385987584),
       F(21597479156841685713774185,79228162514264337593543950336))
beta = (F(2797504526179671494928101665,79228162514264337593543950336),
        F(2797556156441557459457527739,79228162514264337593543950336))
record('chi_strict_outer_bounds', F(27,100000)<chi[0]<chi[1]<F(273,1000000))
record('beta_strict_outer_bounds',F(35309,1000000)<beta[0]<beta[1]<F(35311,1000000))
record('beta_circle_hypothesis',0<beta[0]<beta[1]<F(1,10))
checks['chi_margin_lower'] = str(chi[0]-F(27,100000))
checks['chi_margin_upper'] = str(F(273,1000000)-chi[1])

# Exact rational reconstruction of (C4.A2)--(C4.A9), no Gaussian integration.
def odd_double_factorial(n):
    result=1
    for j in range(1,n+1,2): result*=j
    return result
def m(r):
    return F([1,1,1,2][r]) if r<4 else factorial(r)*F(4,3)**r
def mu(j):
    return F(odd_double_factorial(j-1)) if j%2==0 else F(4,5)*2**(j//2)*factorial(j//2)
def c(j):
    v=odd_double_factorial(2*j-1)
    n=isqrt(v)
    return n+(n*n<v)
@lru_cache(None)
def stir(k,j):
    if k==j==0:return 1
    if k<=0 or j<=0 or j>k:return 0
    return stir(k-1,j-1)+j*stir(k-1,j)
s=[F(0)]+[sum(m(j)*stir(k,j)*c(j) for j in range(1,k+1)) for k in range(1,9)]
@lru_cache(None)
def bell(k,j):
    if k==j==0:return F(1)
    if k<=0 or j<=0 or j>k:return F(0)
    return sum(comb(k-1,l-1)*s[l]*bell(k-l,j-1) for l in range(1,k-j+2))
low={r:[m(r)]+[sum(m(r+j)*stir(k,j)*mu(j) for j in range(1,k+1)) for k in range(1,9)] for r in range(3)}
up={r:[m(r)]+[sum(m(r+j)*bell(k,j)*mu(j) for j in range(1,k+1)) for k in range(1,9)] for r in range(3)}
def conv(a,b):
    return [sum(comb(k,j)*a[j]*b[k-j] for j in range(k+1)) for k in range(9)]
g=[F(1)]*9
term1=conv(low[0],up[1]);term2=conv(conv(g,low[1]),up[1]);term3=conv(conv(g,low[2]),up[2])
inside=[2*(F(27,50)**3*(F(20,3)*term1[k]+12*term2[k]+4*term3[k]+F(16,3)*up[0][k])+2*F(1,10)*F(27,50)*up[0][k]) for k in range(9)]
D8=conv([F(3**k) for k in range(9)],inside)[8]
angle=F(16,7)*D8/256**8
record('D8_exact',D8==F(41272525446939874982,31640625))
record('angle_fraction_exact',angle==F(20636262723469937491,127677049435953561600000000))
record('angle_below_one_millionth',angle<F(1,1000000))
checks['D8']=str(D8);checks['angle_error']=str(angle)

# Verify the displayed scalar analytic/rounding constants in rational arithmetic.
for x,bound in [(26,195000000000),(30,10000000000000),(32,78900000000000)]:
    record(f'exp_lower_{x}',sum(F(x**j,factorial(j)) for j in range(81))>bound)
for B,lb in [(26,195000000000),(30,10000000000000)]:
    mass=1+F(2,lb-1)
    factor=sum(mass**j for j in range(4))
    strip=F(2,lb-1)*factor
    tail=F(1,10*78900000000000)*factor
    if B==26:
        record('rule_26_strip',strip<F(5,10**11))
        record('rule_26_tail',tail<F(6,10**15))
    else:record('rule_30',strip+tail<F(1,10**12))
u=F(1,2**53)
gamma25=25*u/(1-25*u)
record('primitive_delta0',F(16,9)*gamma25+F(4,3)*F(1,4)**13/factorial(13)<46*u)
record('primitive_exp_rounding',(1+46*u)**256*(1+u)**255-1<F(2,10**12))
ul=F(1,2**64)
record('summation_error',4*64481201*ul/(1-64481201*ul)<F(15,10**12))

# Resolve future relative paths against the declared destination map.
tree=ast.parse((study/'assemble_signed_promotion.py').read_text())
mapping=next(ast.literal_eval(node.value) for node in ast.walk(tree) if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='mapping' for t in node.targets))
virtual={str(root/dst):study/src for src,dst in mapping.items()}
virtual[str(root/'docs/README.md')]=study/'PROMOTION_SIGN_DOCS_README.md'
virtual[str(root/'docs/global_nonlinear.md')]=study/'PROMOTION_SIGN_C4.md'
links=[]
for source,destination in [(study/'PROMOTION_SIGN_C4.md',root/'docs/global_nonlinear.md'),(study/'PROMOTION_SIGN_DOCS_README.md',root/'docs/README.md'),(study/'PROMOTION_CODE_README_APPENDIX.md',root/'code/README.md')]:
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',source.read_text()):
        if '://' in target or target.startswith('#'):continue
        resolved=(destination.parent/target.split('#')[0]).resolve()
        actual=virtual.get(str(resolved),resolved)
        links.append({'source':source.name,'target':target,'resolves':actual.is_file()})
record('future_local_links',all(item['resolves'] for item in links))
checks['links']=links
(out/'checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps({k:v for k,v in checks.items() if k!='links'},indent=2))

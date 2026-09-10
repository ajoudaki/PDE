"""Independent exact inequalities and archived deterministic evidence checks."""
from fractions import Fraction as F
import json, math, pathlib, resource, time
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
start=time.process_time()
out=pathlib.Path(__file__).resolve().parent;base=out.parent
counts={'json':0,'text':0}
for path in (base/'evidence').rglob('*'):
    if path.is_file():
        body=path.read_text()
        if path.suffix=='.json':json.loads(body);counts['json']+=1
        else:counts['text']+=1
for name in ['primitive','lower','upper','singular']:
    assert json.loads((base/f'evidence/kernel_check_20260910_01/{name}.json').read_text())==json.loads((out/f'kernel/{name}.json').read_text())
assert json.loads((base/'evidence/angle_bound_20260910_01/result.json').read_text())==json.loads((out/'angle/result.json').read_text())
old=json.loads((base/'evidence/driver_check_20260910_03/result.json').read_text())
new=json.loads((out/'driver/result.json').read_text())
for key in old:
    if key!='elapsed_seconds':assert old[key]==new[key],key
u=F(1,2**53);gam=25*u/(1-25*u)
delta=F(16,9)*gam+F(4,3)*F(1,4)**13/math.factorial(13)
assert delta<46*u
exp_error=(1+46*u)**256*(1+u)**255-1
assert exp_error<F(2,10**12)
for x,lower in [(26,195000000000),(30,10000000000000),(32,78900000000000)]:
    assert sum(F(x**k,math.factorial(k)) for k in range(81))>lower
# E2 with at most four axes, and pi>3; tail uses sqrt(2pi)>5/2.
for target,ex,coef in [(26,F(195000000000),F(5,10**11)),(30,F(10000000000000),F(1,10**12))]:
    mass=1+2/(ex-1)
    strip_per_axis=2/(ex-1)
    tail_per_axis=F(2)/(F(78900000000000)*8*F(5,2))
    strip_total=strip_per_axis*sum(mass**k for k in range(4))
    tail_total=tail_per_axis*sum(mass**k for k in range(4))
    if target==26:
        assert strip_total<coef and tail_total<F(6,10**15)
    else:assert strip_total+tail_total<coef
ulong=F(1,2**64);n=401**3
assert 4*n*ulong/(1-n*ulong)<F(15,10**12)
# Independent periodic error recomputation using direct recursive Bell sums.
N=8
mm=[F(math.factorial(k))*F(4,3)**k for k in range(11)]
mm[:4]=list(map(F,[1,1,1,2]))
def bell(k,j,values):
    if k==0:return F(j==0)
    if j==0:return F(0)
    return sum(F(math.comb(k-1,r-1))*values[r]*bell(k-r,j-1,values) for r in range(1,k-j+2))
mu=[];cl2=[F(1)]
for k in range(N+1):
    if k%2:mu.append(F(4,5)*2**((k-1)//2)*math.factorial((k-1)//2))
    else:mu.append(F(math.prod(range(1,k,2))))
for k in range(1,N+1):
    z=math.prod(range(1,2*k,2));v=math.isqrt(z);cl2.append(F(v+(v*v<z)))
one=[F(1)]*(N+1)
sigma=[F(1)]+[sum(mm[j]*bell(k,j,one)*cl2[j] for j in range(1,k+1)) for k in range(1,N+1)]
lower=[[mm[r]]+[sum(mm[r+j]*bell(k,j,one)*mu[j] for j in range(1,k+1)) for k in range(1,N+1)] for r in range(3)]
upper=[[mm[r]]+[sum(mm[r+j]*bell(k,j,sigma)*mu[j] for j in range(1,k+1)) for k in range(1,N+1)] for r in range(3)]
def mul(a,b):return [sum(F(math.comb(k,j))*a[j]*b[k-j] for j in range(k+1)) for k in range(N+1)]
v0=mul(lower[0],upper[1]);v1=mul(one,mul(lower[1],upper[1]));v2=mul(one,mul(lower[2],upper[2]))
P=F(27,50)
profile=[2*(P**3*(F(20,3)*v0[k]+12*v1[k]+4*v2[k]+F(16,3)*upper[0][k])+F(1,5)*P*upper[0][k]) for k in range(N+1)]
D=mul([F(3**k) for k in range(N+1)],profile)[N]
err=F(16,7)*D/256**8
assert D==F(41272525446939874982,31640625)
assert err==F(20636262723469937491,127677049435953561600000000)<F(1,10**6)
result={'status':'PASS','all_evidence_files_parsed':counts,
        'archived_deterministic_raw_outputs_match_fresh':True,
        'elementary_exponential_relative_bound':float(exp_error),
        'Horner_initial_bound_in_units_u':float(delta/u),
        'angle_derivative_bound_exact':str(D),'angle_error_exact':str(err),
        'cpu_seconds':time.process_time()-start}
(out/'scalar_result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

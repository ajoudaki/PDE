"""Deterministic exact checks of the study's transfer constants; no training."""
from fractions import Fraction as F
from math import factorial
import json

def exp_lower(x, terms=100):
    x=F(x)
    term=total=F(1)
    for j in range(1,terms+1):
        term*=x/j
        total+=term
    return total

B=12
a=B*(B+1)
transport=2*(B*B*(B**3+1)+(B+1)*3792+(B+1)*B*B+
             B*(B**3+1)+(B+1)*313+(B+1)*B*B+
             B**3+1+(B+1)*a)
assert transport==661180 and transport<10**6
assert 2*(B+1)*(B*B+B+1)==4082
assert 2*(B+1)*B**3==44928
assert 2*10*F(161,2)*140==225400
assert 8*10+28*10**2==2880
# These imply all log inequalities used for MQ,H,K,R and R^2/4096.
assert exp_lower(13)>225580
assert exp_lower(4)>32
assert exp_lower(7)>24
assert exp_lower(18)>40000000
assert exp_lower(9)>4096
assert 2**81>3019
assert 2**2872>3015
assert F(100**16,factorial(16))>4*10**18
# delta<exp(-100), itself more than sufficient for these two bounds.
assert exp_lower(100)>44928*256
assert exp_lower(100)>8*B*B*10**18
# Strict paired activity margin.
j=F(1,2500000**2)-2*(B+1)*F(1,10**18)-F(1,10**18)
assert j>F(159,10**15)>F(1,10**13)
print(json.dumps({"status":"PASS","transport_constant_before_rounding":transport,
  "risk_lipschitz":44928,"raw_speed":4082,"reference_response_exponent":2880,
  "reference_response_prefactor":225400,"T":40,"t_act":"1/200",
  "cutoff":"exp(2900)","radius":"exp(-exp(3000))",
  "state_tolerance":"1e-18","squared_activity_margin":"1e-13"},indent=2))


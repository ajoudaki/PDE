"""Fixed scalar boundary checks only; no trajectory or training."""
from decimal import Decimal as D, localcontext
from fractions import Fraction
from pathlib import Path
import json
import platform


def run():
    with localcontext() as ctx:
        ctx.prec = 80
        def sinh(z):
            return (z.exp()-(-z).exp())/2
        def cosh(z):
            return (z.exp()+(-z).exp())/2
        def gate(z):
            return 1/cosh(z)**2
        def primitive(z):
            return z/2+sinh(2*z)/4
        def residual(w,b,h):
            return primitive(w+h*b*gate(w))-primitive(w)-h*b
        def integral(w,b,h):
            # Fixed composite Simpson integration of the exact remainder.
            count=256
            theta=h*b*gate(w)
            terms=[]
            for i in range(count+1):
                s=D(i)/count
                weight=1 if i in (0,count) else 4 if i%2 else 2
                terms.append(weight*(1-s)*sinh(2*(w+s*theta)))
            return h*h*b*b*gate(w)**2*sum(terms)/(3*count)
        cases=[('zero_velocity','3','0','0.03'),
               ('zero_row','0','-2','0.03'),
               ('positive_saturation','20','-3','0.01'),
               ('negative_saturation','-20','3','0.01'),
               ('ordinary','0.7','1.3','0.02')]
        rows=[]
        for name,ws,bs,hs in cases:
            w,b,h=map(D,(ws,bs,hs)); tiny=D('1e-20')
            rw=(residual(w+tiny,b,h)-residual(w-tiny,b,h))/(2*tiny)
            rb=(residual(w,b+tiny,h)-residual(w,b-tiny,h))/(2*tiny)
            iw=(integral(w+tiny,b,h)-integral(w-tiny,b,h))/(2*tiny)
            ib=(integral(w,b+tiny,h)-integral(w,b-tiny,h))/(2*tiny)
            theta=h*b*gate(w)
            dw_exact=cosh(w+theta)**2*(1-2*h*b*gate(w)*sinh(w)/cosh(w))-cosh(w)**2
            db_exact=h*gate(w)*cosh(w+theta)**2-h
            errors=[abs(residual(w,b,h)-integral(w,b,h)),abs(rw-iw),abs(rb-ib)]
            derivative_errors=[abs(rw-dw_exact),abs(rb-db_exact)]
            assert max(errors)<D('1e-10'),(name,errors)
            assert max(derivative_errors)<D('1e-30'),(name,derivative_errors)
            rows.append(dict(case=name,w=ws,b=bs,h=hs,
                             integral_errors=list(map(str,errors)),
                             derivative_errors=list(map(str,derivative_errors))))
    a=[Fraction(1,3),Fraction(-2,5),Fraction(4,7)]
    b=[Fraction(-1,2),Fraction(3,4),Fraction(2,9)]
    c=[Fraction(2,3),Fraction(1,5),Fraction(-1,7)]
    d=[Fraction(4,5),Fraction(-1,8),Fraction(3,10)]
    n=3
    lhs=sum((a[i]*b[j]/n)*(c[i]*d[j]/n) for i in range(n) for j in range(n))
    rhs=sum(a[i]*c[i] for i in range(n))/n*sum(b[j]*d[j] for j in range(n))/n
    assert lhs==rhs
    activity=Fraction(1,2500000)**2-26*Fraction(1,10**18)-Fraction(1,10**18)
    assert activity>Fraction(159,10**15)>Fraction(1,10**13)
    return dict(status='PASS',scope='five fixed scalar raw-clock identity/derivative cases, exact HS rank pairing and inherited activity margin only',
                python=platform.python_version(),precision_decimal_digits=80,
                fixed_simpson_intervals=256,clock_checks=rows,
                hs_pairing=str(lhs),activity_lower=str(activity))


if __name__=='__main__':
    result=run()
    text=json.dumps(result,indent=2)+'\n'
    Path(__file__).with_suffix('.json').write_text(text)
    print(text,end='')

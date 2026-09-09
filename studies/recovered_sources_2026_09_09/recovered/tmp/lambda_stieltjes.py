import sympy as s,math
l=s.symbols('l')
Ds=[36*l+75*l**2,
15552*l+243216*l**2+760176*l**3+666240*l**4,
11197440*l+558565632*l**2+5751565056*l**3+21144930336*l**4+32357889792*l**5+17576484864*l**6,
11287019520*l+1453203763200*l**2+34569399656448*l**3+297887755714560*l**4+1191606495058944*l**5+2419999440371712*l**6+2422966824972288*l**7+947374026522624*l**8]
a,b,c,d=[Ds[i]/math.factorial(2*i+1) for i in range(4)]
mu0=3*b/a**2;mu1=(6*b**2-5*a*c)/a**5;mu2=(7*a*a*d-26*a*b*c+21*b**3)/a**8
for name,z in [('mu0',mu0),('mu1',mu1),('mu2',mu2),('H1',s.factor(mu0*mu2-mu1**2))]:
 num,den=s.factor(z).as_numer_denom();p=s.Poly(num,l);print(name,'numfactor',s.factor(num));print('negative coeffs',[x for x in p.all_coeffs() if x<0], 'degree',p.degree(),'terms',len(p.terms()))
e=sum([s.Integer(x)*l**(i+1) for i,x in enumerate([14627977297920,4546495309086720,211436756895006720,3490984312448606208,27185927724027592704,114581150906254331904,277387051973394751488,385587855340280672256,285610646257352368128,87101527431460847616])])/s.factorial(9)
mu3=-(9*a**3*e-48*a*a*b*d-20*a*a*c*c+144*a*b*b*c-90*b**4)/a**11
for name,z in [('mu3',mu3),('H1shift',s.factor(mu1*mu3-mu2**2))]:
 num,den=s.factor(z).as_numer_denom();p=s.Poly(num,l);print(name,'factor',s.factor(num));print('negative coeffs',len([x for x in p.all_coeffs() if x<0]),'degree',p.degree(),'terms',len(p.terms()))
H=s.factor(mu0*mu2-mu1**2);Hs=s.factor(mu1*mu3-mu2**2)
alphas=[s.factor(mu1/mu0),s.factor(H/(mu0*mu1)),s.factor(mu0*Hs/(mu1*H))]
for i,z in enumerate(alphas,1):
 num,den=s.factor(z).as_numer_denom();print('alpha',i,'=',s.factor(z));print('num deg terms',s.degree(num,l),len(s.Poly(num,l).terms()),'den',s.factor(den))

from collections import Counter

def pairings(items):
    if not items:
        yield []
        return
    a=items[0]
    for j in range(1,len(items)):
        for rest in pairings(items[1:j]+items[j+1:]):
            yield [(a,items[j])]+rest

def classes(k, pairs, side):
    parent=list(range(k))
    def find(a):
        while parent[a]!=a:
            a=parent[a]
        return a
    def join(a,b):
        parent[find(a)]=find(b)
    def idx(slot):
        i, which=divmod(slot,2)
        return i if side=='row' else (i+which)%k
    for a,b in pairs:
        join(idx(a),idx(b))
    return len({find(i) for i in range(k)})

for k in [1,2,3]:
    counts=Counter()
    for p in pairings(list(range(2*k))):
        exponent=classes(k,p,'row')+classes(k,p,'column')-k-1
        counts[exponent]+=1
    print('k =',k,'Wick count by power of n:',dict(sorted(counts.items(),reverse=True)))

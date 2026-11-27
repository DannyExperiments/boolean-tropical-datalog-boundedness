from itertools import product
from math import inf

def path(n):
    w = [3**(n-i) for i in range(n+1)]
    U, T = [inf]*(n+1), [inf]*(n+1)
    vals = []
    for r in range(1,n+4):
        T = [min(w[i]+U[i],w[i]+T[i+1] if i<n else inf) for i in range(n+1)]
        U = w[:]
        vals.append(T[0])
    costs = [sum(w[:j])+2*w[j] for j in range(n+1)]
    assert vals == [inf,*costs,costs[-1]]
    return len(costs)

for n in range(1,201):
    path(n)
print("200 path families: exact first-attainment rounds and costs verified.")

boolean_cases=0
for n in range(1,4):
    for bits in product((False,True),repeat=n*n+n):
        G,E=bits[:n],bits[n:]
        U,T=(False,)*n,(False,)*n
        for r in range(1,5):
            T=tuple(G[i] and (U[i] or any(E[i*n+j] and T[j] for j in range(n))) for i in range(n))
            U=G
            if r>=2:
                assert T==G and U==G
        boolean_cases+=1
print(f"{boolean_cases} Boolean databases: all IDBs stabilize by round 2.")

for a,b in product([0,1,2,3,inf],repeat=2):
    a0,a1=a<=0,a<=1
    b0,b1=b<=0,b<=1
    assert (min(a,b)<=0,min(a,b)<=1)==(a0 or b0,a1 or b1)
    assert (a+b<=0,a+b<=1)==(a0 and b0,(a0 and b1) or (a1 and b0))
print("25 tropical threshold gate cases verified.")


def minplus(left, right):
    n = len(left)
    return [[min(left[i][k] + right[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def check_companion():
    n = 3
    for weights in product((0, 2, inf), repeat=n*n):
        edges = [list(weights[i*n:(i+1)*n]) for i in range(n)]
        identity_augmented = [row[:] for row in edges]
        for i in range(n):
            identity_augmented[i][i] = 0
        bounded = minplus(edges, minplus(identity_augmented, identity_augmented))
        exact_two = minplus(edges, edges)
        exact_three = minplus(edges, exact_two)
        assert bounded == [
            [min(edges[i][j], exact_two[i][j], exact_three[i][j]) for j in range(n)]
            for i in range(n)
        ]
        for s in range(n):
            for t in range(n):
                has_zero_walk = any(
                    all(edges[a][b] == 0 for a,b in zip(walk, walk[1:]))
                    for k in range(n)
                    for inner in product(range(n), repeat=k)
                    for walk in [(s,*inner,t)]
                )
                assert min(2,1+bounded[s][t]) == (1 if has_zero_walk else 2)
    print("19683 weighted 3-vertex structures: positive-length doubling and threshold reduction verified.")


check_companion()

import numpy
n, m= map(int,input().split())
a=[]
for _ in range(n):
    riga=list(map(int,input().split()))
    a.append(riga)
print(numpy.prod(numpy.sum(a,axis=0)))

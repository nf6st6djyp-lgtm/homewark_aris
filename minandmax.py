import numpy
n, m= map(int,input().split())
a=[]
for _ in range(n):
    riga=list(map(int,input().split()))
    a.append(riga)
print(numpy.max(numpy.min(a,axis=1)))
    

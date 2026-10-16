import numpy
n, m= map(int,input().split())
a=[]
for _ in range(n):
    riga=list(map(int,input().split()))
    a.append(riga)
print(numpy.mean(a, axis=1))
print(numpy.var(a, axis=0))
print(round(numpy.std(a),11))
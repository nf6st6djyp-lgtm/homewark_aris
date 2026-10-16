import numpy
n=int(input())
a=[]
for _ in range(n):
    riga=list(map(int,input().split()))
    a.append(riga)
b=[]
for _ in range(n):
    riga=list(map(int,input().split()))
    b.append(riga)

print(numpy.dot(a,b))
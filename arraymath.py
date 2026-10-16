import numpy
n, m= map(int, input().split())
a=[]
b=[]
for i in range(n*2):
    if i<n:
        a.append(list(map(int,input().split())))
    else:
        b.append(list(map(int,input().split())))
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(numpy.floor_divide(a,b))
print(numpy.mod(a,b))
print(numpy.power(a,b))

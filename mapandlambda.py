cube = lambda x: x**3 

def fibonacci(n):
    if n==0:
        return []
    if n==1:
        return [0]
    l=[0,1]
    for i in range(1,n-1):
        num = l[i] + l[i-1]
        l.append(num)
    return l
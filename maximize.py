from itertools import product

k,m = map(int,input().split(" "))

l=[]
for _ in range(k):
    riga = list(map(int,input().split(" ")))
    vett = riga[1:]
    l.append([(x**2) % m for x in vett])

best=0
for combo in product(*l):
    best = max(best, sum(combo) % m)
    
print(best)

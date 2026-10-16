n, x= map(int,input().split())
liste=[]
for _ in range(x):
    liste.append(list(map(float,input().split())))
studenti=list(zip(*liste))
for voti in studenti:
    somma=0 
    for voto in voti:
        somma+=voto
    print(somma/x)

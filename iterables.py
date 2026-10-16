from itertools import permutations

n = int(input())
s = input().split(" ")
k = int(input())

l = permutations(s, k)

totale = 0
validi = 0

for x in l:
    totale += 1
    if x.count("a") >= 1:
        validi += 1

print(round(validi / totale, 3))

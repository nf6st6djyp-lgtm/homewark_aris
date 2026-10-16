from itertools import combinations

s,k=input().split(" ")
s=sorted(s)

for i in range(1,int(k)+1):
    st=list(combinations((s),int(i)))
    for string in st:
        print("".join(string))
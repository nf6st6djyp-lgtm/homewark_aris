from itertools import permutations
s,k=input().split(" ")

st=list(permutations((s),int(k)))
st.sort()
for string in st:
    print("".join(string))

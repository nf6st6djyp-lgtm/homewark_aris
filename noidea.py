n, m = input().split(" ")
arr=list(input().split(" "))
a=set((input().split(" ")))
b=set((input().split(" ")))

happiness=0

for n in arr:
    if n in a:
        happiness += 1
    elif n in b:
        happiness -= 1
print(happiness)
from collections import Counter


x = int(input())
sizes = list(map(int, input().split()))
n = int(input())


inventory = Counter(sizes)

earnings = 0

for _ in range(n):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        earnings += price
        inventory[size] -= 1  

print(earnings)

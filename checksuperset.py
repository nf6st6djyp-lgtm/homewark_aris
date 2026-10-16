s = set(input().split())
n = int(input())
print(all(s > set(input().split()) for _ in range(n)))
